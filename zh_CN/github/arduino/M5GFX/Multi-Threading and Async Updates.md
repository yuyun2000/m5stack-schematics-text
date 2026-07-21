M5GFX Multi-Threading and Async Updates

# Multi-Threading and Async Updates

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/lgfx/v1/misc/enum.hpp](src/lgfx/v1/misc/enum.hpp)
- [src/lgfx/v1/platforms/esp32/Bus_EPD.cpp](src/lgfx/v1/platforms/esp32/Bus_EPD.cpp)
- [src/lgfx/v1/platforms/esp32/Bus_EPD.h](src/lgfx/v1/platforms/esp32/Bus_EPD.h)
- [src/lgfx/v1/platforms/esp32/Panel_EPD.cpp](src/lgfx/v1/platforms/esp32/Panel_EPD.cpp)
- [src/lgfx/v1/platforms/esp32/Panel_EPD.hpp](src/lgfx/v1/platforms/esp32/Panel_EPD.hpp)

</details>



## Purpose and Scope

This page explains the multi-threading architecture used in `Panel_EPD` for asynchronous e-paper display updates. E-paper displays require slow, multi-frame refresh sequences that can take hundreds of milliseconds to complete. To prevent blocking the main application thread during these updates, M5GFX implements a FreeRTOS-based asynchronous update system with queue-based communication and multi-core cache coherency management.

For basic e-paper panel configuration and LUT (Look-Up Table) settings, see [Display-Specific Configuration](#7.4). For general panel driver architecture, see [Panel Driver Architecture](#4). For e-paper-specific features like grayscale transitions, see [E-Paper Panel Driver](#4.2).

---

## Why Asynchronous Updates Are Required

E-paper displays differ fundamentally from LCD panels in their refresh characteristics. While LCDs update pixels in milliseconds via SPI transactions, e-paper displays require:

1. **Multi-frame sequences**: Each grayscale transition requires multiple display frames (15-30 frames for quality mode)
2. **Slow refresh rates**: Each frame takes 10-50ms to apply, resulting in total update times of 200-1500ms
3. **State-dependent transitions**: Pixels must transition gradually from their current grayscale level to the target level using lookup tables

Blocking the main application thread during these updates would make the device unresponsive. The solution is to offload display refresh to a dedicated FreeRTOS task that processes updates asynchronously while the main thread continues executing user code.

**Sources:** [Panel_EPD.cpp:1-296]()

---

## System Architecture

### Component Overview

```mermaid
graph TB
    subgraph "Main Thread (Application)"
        MainApp["Application Code<br/>Drawing Operations"]
        WriteMethods["writePixels()<br/>writeImage()<br/>writeFillRect()"]
        DisplayCall["display(x,y,w,h)"]
        WaitDisplay["waitDisplay()"]
        DisplayBusy["displayBusy()"]
    end
    
    subgraph "Framebuffer Memory (PSRAM)"
        UserBuffer["_buf<br/>(8-bit grayscale pixels)"]
        StepFramebuf["_step_framebuf<br/>(16-bit state + grayscale)"]
        DMABufs["_dma_bufs[2]<br/>(4-pixel packed data)"]
    end
    
    subgraph "Communication Primitives"
        UpdateQueue["_update_queue_handle<br/>QueueHandle_t<br/>xQueueCreate(8, update_data_t)"]
        DisplayBusyFlag["_display_busy<br/>volatile bool"]
    end
    
    subgraph "EPD Update Task (Dedicated Core)"
        TaskHandle["_task_update_handle<br/>TaskHandle_t"]
        TaskUpdate["task_update()<br/>FreeRTOS Task"]
        BlitDmabuf["blit_dmabuf()<br/>LUT Processing"]
        BusWriteScanLine["Bus_EPD::writeScanLine()"]
    end
    
    subgraph "Hardware Layer"
        I80Bus["ESP32 LCD I80 Bus<br/>DMA Transfer"]
        EPDPanel["E-Paper Display<br/>Physical Hardware"]
    end
    
    MainApp --> WriteMethods
    WriteMethods --> UserBuffer
    WriteMethods --> DisplayCall
    DisplayCall -->|"xQueueSend()"| UpdateQueue
    DisplayCall -->|"cacheWriteBack()"| UserBuffer
    DisplayCall --> DisplayBusyFlag
    
    WaitDisplay -->|"Check"| DisplayBusyFlag
    DisplayBusy -->|"Check"| UpdateQueue
    
    UpdateQueue -->|"xQueueReceive()"| TaskUpdate
    TaskUpdate -->|"Read"| UserBuffer
    TaskUpdate -->|"Update"| StepFramebuf
    TaskUpdate --> BlitDmabuf
    BlitDmabuf -->|"Convert pixels"| DMABufs
    BusWriteScanLine -->|"DMA transfer"| I80Bus
    I80Bus --> EPDPanel
    
    TaskUpdate -->|"Set/Clear"| DisplayBusyFlag
    
    style UpdateQueue fill:#e8e8e8
    style DisplayBusyFlag fill:#e8e8e8
    style TaskUpdate fill:#e8e8e8
```

**Key Components:**

- **_buf**: User-facing framebuffer in PSRAM storing 4-bit grayscale pixel pairs (1 byte = 2 pixels)
- **_step_framebuf**: Internal framebuffer tracking refresh progress (upper 8 bits) and target grayscale values (lower 8 bits) per pixel pair
- **_update_queue_handle**: FreeRTOS queue for passing update regions from main thread to task
- **_task_update_handle**: FreeRTOS task handle running on dedicated CPU core
- **_display_busy**: Volatile flag indicating whether updates are in progress

**Sources:** [Panel_EPD.hpp:87-126](), [Panel_EPD.cpp:161-296]()

---

## Task Creation and Initialization

### Initialization Sequence

The asynchronous update system is initialized during `Panel_EPD::init_intenal()`:

```mermaid
sequenceDiagram
    participant App as Application
    participant Init as init_intenal()
    participant Heap as heap_caps_malloc
    participant FreeRTOS as FreeRTOS API
    participant Task as task_update()
    
    App->>Init: init(use_reset)
    Init->>Heap: Allocate _buf (PSRAM)
    Init->>Heap: Allocate _step_framebuf (PSRAM)
    Init->>Heap: Allocate _dma_bufs[2] (DMA-capable)
    Init->>Heap: Allocate _lut_2pixel (DMA-capable)
    
    Init->>Init: memset(_step_framebuf, 0x88)
    Note over Init: Initialize to mid-gray
    
    Init->>FreeRTOS: xQueueCreate(8, sizeof(update_data_t))
    FreeRTOS-->>Init: _update_queue_handle
    
    Init->>FreeRTOS: xTaskCreatePinnedToCore(<br/>"epd", 4096 stack,<br/>priority, pinned_core)
    FreeRTOS-->>Init: _task_update_handle
    FreeRTOS->>Task: Start task_update()
    
    Task->>Task: Enter infinite loop
    Task->>FreeRTOS: xQueueReceive(portMAX_DELAY)
    Note over Task: Wait for first update
```

**Memory Allocation Strategy:**

| Buffer | Size Calculation | Capability | Purpose |
|--------|-----------------|------------|---------|
| `_buf` | `(panel_w × panel_h) / 2` | `MALLOC_CAP_SPIRAM` | User framebuffer (4-bit grayscale pairs) |
| `_step_framebuf` | `(memory_w × memory_h) × 2` | `MALLOC_CAP_SPIRAM` | Progress tracking (2 banks: current + reserved) |
| `_dma_bufs[2]` | `memory_w / 4 + line_padding` | `MALLOC_CAP_DMA` | Double-buffered DMA scanline data |
| `_lut_2pixel` | `lut_total_step × 256 × 2` | `MALLOC_CAP_DMA` | Pre-computed LUT for 2-pixel transitions |

**Task Configuration:**

The task is created with configurable parameters from `config_detail_t`:

- **task_priority**: Default 2 (configurable via `_config_detail.task_priority`)
- **task_pinned_core**: Defaults to opposite core from caller. If `task_pinned_core >= portNUM_PROCESSORS`, it selects `(xPortGetCoreID() + 1) % portNUM_PROCESSORS`
- **Stack size**: 4096 bytes

**Sources:** [Panel_EPD.cpp:213-296](), [Panel_EPD.hpp:42-58]()

---

## Queue-Based Communication

### Update Data Structure

Updates are passed from the main thread to the task via `update_data_t`:

```mermaid
classDiagram
    class update_data_t {
        +uint16_t x
        +uint16_t y
        +uint16_t w
        +uint16_t h
        +epd_mode_t mode
        +operator==(other) bool
        +operator!=(other) bool
    }
    
    class epd_mode_t {
        <<enumeration>>
        epd_quality = 1
        epd_text = 2
        epd_fast = 3
        epd_fastest = 4
    }
    
    update_data_t --> epd_mode_t
```

**Sources:** [Panel_EPD.hpp:99-111](), [enum.hpp:42-52]()

### Display Update Flow

```mermaid
sequenceDiagram
    participant App as Application Thread
    participant Cache as Cache System
    participant Queue as Update Queue
    participant Task as EPD Task Thread
    participant Display as Physical Display
    
    App->>App: drawPixel() / fillRect() / drawImage()
    Note over App: Writes to _buf in PSRAM
    
    App->>App: display(x, y, w, h)
    App->>App: Calculate update region
    App->>Cache: cacheWriteBack(_buf, size)
    Note over Cache: Flush D-cache to ensure<br/>task sees updated data
    
    App->>Queue: xQueueSend(update_data_t, 128ms timeout)
    
    alt Queue send successful
        App->>App: Clear _range_mod region
        App->>App: Return to user code
    else Queue full
        App->>App: Keep _range_mod for retry
        Note over App: displayBusy() returns true
    end
    
    Task->>Queue: xQueueReceive(portMAX_DELAY)
    Queue-->>Task: update_data_t
    
    Task->>Task: Set _display_busy = true
    Task->>Task: Process multi-frame update sequence
    
    loop For each scanline, each frame
        Task->>Task: blit_dmabuf() - LUT conversion
        Task->>Display: Bus_EPD::writeScanLine()
        Display-->>Task: DMA complete callback
    end
    
    Task->>Task: Check queue for next update
    alt Queue empty
        Task->>Task: Set _display_busy = false
        Task->>Queue: xQueueReceive(portMAX_DELAY)
        Note over Task: Block until next update
    else Queue has more updates
        Task->>Queue: xQueueReceive(0 timeout)
        Note over Task: Process immediately
    end
```

**Queue Characteristics:**
- **Depth**: 8 entries (configured in [Panel_EPD.cpp:286]())
- **Item Size**: `sizeof(update_data_t)` = 10 bytes
- **Timeout on Send**: 128ms (`128 / portTICK_PERIOD_MS`)
- **Blocking Behavior**: Task blocks indefinitely (`portMAX_DELAY`) when queue is empty

**Sources:** [Panel_EPD.cpp:553-589](), [Panel_EPD.cpp:887-910]()

---

## Cache Coherency Across Cores

### The Multi-Core Problem

When the main thread runs on Core 0 and the EPD task runs on Core 1 (or vice versa), PSRAM data written by one core may remain in that core's data cache and not be immediately visible to the other core. This manifests as:

1. Main thread writes pixels to `_buf` in PSRAM
2. Data remains in Core 0's D-cache
3. EPD task on Core 1 reads `_buf` from PSRAM
4. EPD task sees stale pixel data, causing display artifacts

### Cache Writeback Implementation

M5GFX solves this with explicit cache management before queueing updates:

```mermaid
flowchart TD
    Start["display() called"] --> CheckPlatform{"Platform supports<br/>cache writeback?"}
    
    CheckPlatform -->|"ESP32-S3 + esp_cache.h"| UseNewAPI["Use esp_cache_msync()"]
    CheckPlatform -->|"ESP32-S3 + rom/cache.h"| UseRomAPI["Use Cache_WriteBack_Addr()"]
    CheckPlatform -->|"Other platforms"| NoOp["No-op (inline stub)"]
    
    UseNewAPI --> AlignStart["start = addr & ~127"]
    AlignStart --> AlignEnd["end = (addr + size + 127) & ~127"]
    AlignEnd --> SyncCache["esp_cache_msync(start, end-start,<br/>ESP_CACHE_MSYNC_FLAG_DIR_C2M |<br/>ESP_CACHE_MSYNC_FLAG_TYPE_DATA)"]
    
    UseRomAPI --> AlignStart2["start = addr & ~127"]
    AlignStart2 --> AlignEnd2["end = (addr + size + 127) & ~127"]
    AlignEnd2 --> SyncCache2["Cache_WriteBack_Addr(start, end-start)"]
    
    SyncCache --> QueueSend["xQueueSend(update_queue)"]
    SyncCache2 --> QueueSend
    NoOp --> QueueSend
    
    QueueSend --> TaskReads["EPD task reads from PSRAM"]
    TaskReads --> End["Correct pixel data visible"]
```

**Cache Alignment:**
- Both implementations align addresses to 128-byte boundaries (cache line size)
- This ensures entire cache lines are flushed, preventing partial updates

**Platform-Specific Code:**

The implementation uses conditional compilation based on available headers:

1. **Modern ESP-IDF (v5.0+)**: Uses `esp_cache_msync()` with `ESP_CACHE_MSYNC_FLAG_DIR_C2M` (cache-to-memory direction) [Panel_EPD.cpp:27-43]()
2. **Legacy ESP32-S3 IDF**: Uses ROM function `Cache_WriteBack_Addr()` [Panel_EPD.cpp:46-52]()
3. **Other platforms**: No-op stub function [Panel_EPD.cpp:69]()

**Critical Call Sites:**
- Before queueing display update: [Panel_EPD.cpp:578]() - `cacheWriteBack(&_buf[y * _cfg.panel_width >> 1], h * _cfg.panel_width >> 1)`

**Sources:** [Panel_EPD.cpp:27-70](), [Panel_EPD.cpp:578]()

---

## Update Processing Loop

### Task Main Loop Structure

```mermaid
stateDiagram-v2
    [*] --> WaitForUpdate: Task starts
    
    WaitForUpdate --> ProcessUpdate: xQueueReceive() gets data
    
    ProcessUpdate --> DetermineMode: Read update_data_t
    
    DetermineMode --> FastMode: mode = epd_fast/fastest
    DetermineMode --> TextMode: mode = epd_text
    DetermineMode --> QualityMode: mode = epd_quality
    
    FastMode --> CopyToStepBuf: Skip eraser LUT
    TextMode --> CopyToStepBuf: Apply eraser first
    QualityMode --> CopyToStepBuf: Apply eraser first
    
    CopyToStepBuf --> ProcessFrames: Copy from _buf to _step_framebuf
    
    ProcessFrames --> BlitScanlines: For each frame in LUT sequence
    BlitScanlines --> NextFrame: For each scanline
    NextFrame --> ProcessFrames: More frames remain
    
    ProcessFrames --> CheckQueue: All frames complete
    
    CheckQueue --> WaitForUpdate: Queue empty (_display_busy=false)
    CheckQueue --> ProcessUpdate: Queue has more data (remain=true)
```

### Frame Processing Detail

The `blit_dmabuf()` function is the performance-critical inner loop that converts pixel state to I80 bus data:

**Function Signature:**
```cpp
static bool blit_dmabuf(uint32_t* dst,      // Output: 4 pixels packed in uint32
                        uint16_t* src,       // Input/Output: _step_framebuf state
                        const uint8_t* lut,  // Input: Current LUT offset
                        size_t len)          // Number of 4-pixel groups
```

**Per-Pixel State Machine:**

Each `uint16_t` in `_step_framebuf` encodes:
- **Upper 8 bits**: Current LUT step (0-255)
- **Lower 8 bits**: Target grayscale value (0-15 for each 4-bit pixel pair)
- **Sign bit (MSB)**: Negative value means "skip processing this pixel"

**Optimization Strategy:**

1. **XTENSA Assembly**: On ESP32/ESP32-S3, uses hand-coded assembly with `loop` instruction and register allocation [Panel_EPD.cpp:591-804]()
2. **Portable C++**: Fallback implementation for other architectures [Panel_EPD.cpp:806-884]()
3. **8-pixel SIMD**: Processes 8 pixels simultaneously per iteration for cache efficiency

**Sources:** [Panel_EPD.cpp:887-1165](), [Panel_EPD.cpp:591-884]()

### LUT-Based Pixel Transitions

```mermaid
graph LR
    subgraph "Pixel State Evolution"
        State0["Initial State<br/>_step_framebuf[i] = 0x0088<br/>(Gray level 8)"]
        State1["After User Draw<br/>Target = 0x00FF<br/>(White)"]
        State2["Frame 0: Eraser LUT<br/>Step = 0, Output = 2<br/>(Drive to white)"]
        State3["Frame 1: Quality LUT<br/>Step = 1, Output = 2<br/>(Continue white)"]
        State4["Frame N: Complete<br/>Step = 255, LUT returns 0<br/>(Switch to reserved buffer)"]
    end
    
    State0 --> State1
    State1 --> State2
    State2 --> State3
    State3 --> State4
    
    State4 -->|"Reserved buffer<br/>becomes current"| State0
```

**LUT Output Encoding:**
- `0`: End of sequence (pixel complete, switch buffers)
- `1`: Drive pixel toward black
- `2`: Drive pixel toward white
- `3`: No operation (maintain current state)

**Sources:** [Panel_EPD.cpp:74-157](), [Panel_EPD.cpp:912-1020]()

---

## Synchronization Mechanisms

### Busy State Management

```mermaid
flowchart TD
    subgraph "Main Thread Operations"
        Draw["Drawing operations<br/>(writePixels, fillRect)"]
        Display["display(x,y,w,h)"]
        WaitFunc["waitDisplay()"]
        BusyFunc["displayBusy()"]
    end
    
    subgraph "Shared State"
        BusyFlag["_display_busy<br/>(volatile bool)"]
        Queue["_update_queue_handle"]
    end
    
    subgraph "EPD Task Operations"
        TaskLoop["task_update() loop"]
        SetBusy["_display_busy = true"]
        ClearBusy["_display_busy = false"]
    end
    
    Draw --> Display
    Display -->|"Check space"| Queue
    Display -->|"Set if queue succeeds"| BusyFlag
    
    WaitFunc -->|"while (_display_busy) vTaskDelay(1)"| BusyFlag
    BusyFunc -->|"Check uxQueueSpacesAvailable()"| Queue
    
    TaskLoop -->|"Before processing"| SetBusy
    TaskLoop -->|"After queue empty"| ClearBusy
    
    SetBusy --> BusyFlag
    ClearBusy --> BusyFlag
```

**API Functions:**

| Function | Behavior | Use Case |
|----------|----------|----------|
| `waitDisplay()` | Blocks until `_display_busy == false` using `vTaskDelay(1)` | Ensure display update complete before critical operations |
| `displayBusy()` | Returns `true` if queue has no space (`uxQueueSpacesAvailable() == 0`) | Non-blocking check before queueing more updates |
| `display()` | Sets `_display_busy = true` before queueing, clears update region on success | Standard update trigger |

**Busy Flag Semantics:**

The `_display_busy` flag has dual semantics:
1. **From main thread perspective**: Indicates whether any updates are pending or processing
2. **From task perspective**: Set when actively processing frames, cleared when queue is empty and waiting

This prevents a race condition where:
1. Task finishes processing and checks queue (empty)
2. Main thread queues new update
3. Task would set `_display_busy = false` incorrectly

The queue's own internal state (`uxQueueSpacesAvailable()`) provides the authoritative busy status from the main thread's perspective.

**Sources:** [Panel_EPD.cpp:299-319](), [Panel_EPD.cpp:905-907]()

---

## Configuration Options

### Task Configuration Structure

The `config_detail_t` structure provides runtime configuration for the async update system:

```mermaid
classDiagram
    class config_detail_t {
        +const uint32_t* lut_quality
        +const uint32_t* lut_text
        +const uint32_t* lut_fast
        +const uint32_t* lut_fastest
        +size_t lut_quality_step
        +size_t lut_text_step
        +size_t lut_fast_step
        +size_t lut_fastest_step
        +uint8_t line_padding
        +uint8_t task_priority
        +uint8_t task_pinned_core
    }
    
    class Panel_EPD {
        -config_detail_t _config_detail
        +config_detail(void) config_detail_t
        +config_detail(const config_detail_t&) void
    }
    
    Panel_EPD *-- config_detail_t
```

**Configuration Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `task_priority` | `uint8_t` | `2` | FreeRTOS task priority (0-configMAX_PRIORITIES) |
| `task_pinned_core` | `uint8_t` | `-1` (auto) | Pin task to specific CPU core (0, 1, or -1 for auto) |
| `line_padding` | `uint8_t` | `0` | Extra bytes added to DMA buffer per scanline |
| `lut_*` pointers | `const uint32_t*` | Built-in | Custom LUT tables for different refresh modes |
| `lut_*_step` | `size_t` | Auto-calculated | Number of frames in each LUT sequence |

**Example Configuration:**

```cpp
// Pin EPD task to Core 1 with high priority
auto epd = new Panel_EPD();
auto cfg = epd->config_detail();
cfg.task_priority = 5;           // Higher priority than default
cfg.task_pinned_core = 1;        // Force to Core 1
cfg.line_padding = 4;            // Add 4 bytes padding per scanline
epd->config_detail(cfg);
epd->init(true);
```

**Core Assignment Logic:**

If `task_pinned_core >= portNUM_PROCESSORS` (typically 2), the code automatically selects the opposite core from the calling thread:

```cpp
if (task_pinned_core >= portNUM_PROCESSORS)
{
    task_pinned_core = (xPortGetCoreID() + 1) % portNUM_PROCESSORS;
}
```

This ensures the EPD task runs on a different core from the main application, maximizing parallelism and cache isolation benefits.

**Sources:** [Panel_EPD.hpp:42-61](), [Panel_EPD.cpp:287-293]()

---

## Performance Considerations

### Memory Bandwidth and Cache Pressure

**Double Buffering in _step_framebuf:**

The `_step_framebuf` uses double buffering with alternating indices:
- **Even indices** (`[0], [2], [4]...`): Currently processing pixel states
- **Odd indices** (`[1], [3], [5]...`): Reserved/next-frame pixel targets

This prevents flickering when new updates arrive during ongoing refresh sequences. The task completes the current frame sequence with old data while preparing the next sequence with new data.

**Memory Access Pattern:**

```
_buf:           [Panel framebuffer, sequential access]
                 ↓ (copy during display())
_step_framebuf:  [State tracking, even/odd interleaved]
                 ↓ (LUT processing)
_dma_bufs[n]:    [Packed I80 data, DMA-capable memory]
                 ↓ (DMA transfer)
I80 Bus:         [Hardware peripheral]
```

**Cache Writeback Overhead:**

On ESP32-S3 with 32KB D-cache, flushing the entire framebuffer (e.g., 540×960÷2 = 259,200 bytes for M5Paper) takes approximately:
- **Cache line size**: 128 bytes
- **Lines to flush**: 259,200 ÷ 128 = 2,025 lines
- **Estimated time**: ~100-200µs at 240MHz CPU clock

This is negligible compared to the multi-frame update duration (200-1500ms) but important for real-time rendering scenarios.

**Sources:** [Panel_EPD.cpp:232](), [Panel_EPD.cpp:578]()

---

## Summary

The `Panel_EPD` multi-threading architecture provides:

1. **Non-blocking updates**: Main application continues running during 200-1500ms refresh sequences
2. **Queue-based decoupling**: Up to 8 pending update regions can be buffered
3. **Multi-core parallelism**: EPD task can run on separate core for true concurrency
4. **Cache coherency**: Explicit writeback ensures correct pixel data visibility across cores
5. **Configurable scheduling**: Task priority and CPU affinity tunable for specific applications
6. **Zero-copy design**: DMA transfers directly from PSRAM buffers without intermediate copies

This design is essential for responsive e-paper applications where display updates must not freeze the UI or interrupt time-sensitive operations like touch input processing or network communication.

**Sources:** [Panel_EPD.cpp:1-1165](), [Panel_EPD.hpp:1-132](), [Bus_EPD.cpp:1-167]()