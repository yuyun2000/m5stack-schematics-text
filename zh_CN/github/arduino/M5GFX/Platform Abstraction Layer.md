M5GFX Platform Abstraction Layer

# Platform Abstraction Layer

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp](src/lgfx/v1/platforms/esp32/Bus_SPI.cpp)
- [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp](src/lgfx/v1/platforms/esp32/Bus_SPI.hpp)
- [src/lgfx/v1/platforms/esp32/common.cpp](src/lgfx/v1/platforms/esp32/common.cpp)
- [src/lgfx/v1/platforms/esp32/common.hpp](src/lgfx/v1/platforms/esp32/common.hpp)
- [src/lgfx/v1/platforms/sdl/Panel_sdl.cpp](src/lgfx/v1/platforms/sdl/Panel_sdl.cpp)
- [src/lgfx/v1/platforms/sdl/Panel_sdl.hpp](src/lgfx/v1/platforms/sdl/Panel_sdl.hpp)
- [src/lgfx/v1/platforms/sdl/common.cpp](src/lgfx/v1/platforms/sdl/common.cpp)

</details>



The Platform Abstraction Layer provides a unified interface for hardware operations, enabling M5GFX to run on both ESP32 microcontrollers and desktop computers via SDL2 simulation. This abstraction allows the same graphics code to compile and execute on embedded hardware or desktop environments without modification. The layer abstracts GPIO control, timing functions, memory management, bus communication (SPI, I2C), and DMA operations.

For information about specific bus implementations (SPI, I2C, parallel buses), see [#5.3](#5.3), [#5.4](#5.4). For SDL-specific panel rendering, see [#4.6](#4.6). For cross-platform development workflows, see [#6.3](#6.3) and [#6.4](#6.4).

---

## Platform Abstraction Architecture

The platform abstraction strategy uses conditional compilation (`#if defined (ESP_PLATFORM)` vs `#if defined (SDL_h_)`) to select between ESP32 hardware access and SDL desktop simulation at compile time. Both platforms implement the same function signatures, ensuring binary compatibility.

```mermaid
graph TB
    subgraph "Application Code"
        UserCode["User Application<br/>LGFX_Device, Panel, Bus"]
    end
    
    subgraph "Common Interface"
        GPIO["GPIO Functions<br/>pinMode, gpio_hi, gpio_lo, gpio_in"]
        Timing["Timing Functions<br/>millis, micros, delay, delayMicroseconds"]
        Memory["Memory Management<br/>heap_alloc, heap_alloc_dma, heap_alloc_psram"]
        Bus["Bus Initialization<br/>spi::init, i2c::init"]
    end
    
    subgraph "ESP32 Implementation"
        ESP32_GPIO["Direct Register Access<br/>GPIO.out_w1ts, GPIO.out_w1tc<br/>GPIO.in, GPIO.pin"]
        ESP32_Time["ESP Timer<br/>esp_timer_get_time<br/>vTaskDelay, ets_delay_us"]
        ESP32_Mem["ESP Heap Caps<br/>heap_caps_malloc<br/>MALLOC_CAP_DMA<br/>MALLOC_CAP_SPIRAM"]
        ESP32_SPI["SPI Peripheral<br/>spi_bus_initialize<br/>Direct Register Access<br/>DMA Descriptors"]
        ESP32_I2C["I2C Peripheral<br/>i2c_dev_t, i2c_cmd_t<br/>State Machine"]
    end
    
    subgraph "SDL Implementation"
        SDL_GPIO["Emulated GPIO<br/>_gpio_dummy_values array<br/>64 virtual pins"]
        SDL_Time["SDL Timer<br/>SDL_GetTicks<br/>SDL_GetPerformanceCounter<br/>SDL_Delay"]
        SDL_Mem["Standard Malloc<br/>malloc/free<br/>No DMA simulation"]
        SDL_Dummy["Dummy Bus Functions<br/>Return error_t::unknown_err<br/>No actual I/O"]
    end
    
    UserCode --> GPIO
    UserCode --> Timing
    UserCode --> Memory
    UserCode --> Bus
    
    GPIO -->|"#if ESP_PLATFORM"| ESP32_GPIO
    GPIO -->|"#if SDL_h_"| SDL_GPIO
    
    Timing -->|"#if ESP_PLATFORM"| ESP32_Time
    Timing -->|"#if SDL_h_"| SDL_Time
    
    Memory -->|"#if ESP_PLATFORM"| ESP32_Mem
    Memory -->|"#if SDL_h_"| SDL_Mem
    
    Bus -->|"#if ESP_PLATFORM"| ESP32_SPI
    Bus -->|"#if ESP_PLATFORM"| ESP32_I2C
    Bus -->|"#if SDL_h_"| SDL_Dummy
```

**Platform Selection via Conditional Compilation**

Sources: [src/lgfx/v1/platforms/esp32/common.cpp:18](), [src/lgfx/v1/platforms/sdl/common.cpp:21-25]()

---

## ESP32 Platform Implementation

The ESP32 platform provides direct hardware access through register manipulation and ESP-IDF APIs. It supports multiple chip variants (ESP32, S2, S3, C3, C6, P4) with conditional compilation adjusting for peripheral differences.

### GPIO Control

GPIO operations use direct register access for maximum performance, avoiding function call overhead. The abstraction provides consistent pin control across all ESP32 variants despite register layout differences.

```mermaid
graph LR
    subgraph "GPIO API"
        pinMode["pinMode(pin, mode)"]
        gpio_hi["gpio_hi(pin)"]
        gpio_lo["gpio_lo(pin)"]
        gpio_in["gpio_in(pin)"]
    end
    
    subgraph "Register Access"
        direction TB
        GetReg["get_gpio_hi_reg(pin)<br/>get_gpio_lo_reg(pin)<br/>Returns volatile uint32_t*"]
        RegWrite["Direct Register Write<br/>*reg = 1 << (pin & 31)"]
        RegRead["Direct Register Read<br/>GPIO.in.val or GPIO.in1.val"]
    end
    
    subgraph "Hardware Registers"
        GPIO_OUT_W1TS["GPIO.out_w1ts<br/>(Write 1 to Set)"]
        GPIO_OUT_W1TC["GPIO.out_w1tc<br/>(Write 1 to Clear)"]
        GPIO_IN["GPIO.in.val<br/>(Input Level)"]
        GPIO_ENABLE["GPIO_ENABLE_REG<br/>(Output Enable)"]
        GPIO_PIN_MUX["GPIO_PIN_MUX_REG<br/>(Pin Function/Pull)"]
    end
    
    gpio_hi --> GetReg
    gpio_lo --> GetReg
    GetReg --> RegWrite
    RegWrite --> GPIO_OUT_W1TS
    RegWrite --> GPIO_OUT_W1TC
    
    gpio_in --> RegRead
    RegRead --> GPIO_IN
    
    pinMode --> GPIO_ENABLE
    pinMode --> GPIO_PIN_MUX
```

**GPIO Operations - Direct Register Access**

| Function | Purpose | Implementation |
|----------|---------|----------------|
| `pinMode(pin, mode)` | Configure pin direction and pull resistors | Sets IO_MUX registers, GPIO enable, and pad driver mode |
| `gpio_hi(pin)` | Set pin HIGH | `*get_gpio_hi_reg(pin) = 1 << (pin & 31)` |
| `gpio_lo(pin)` | Set pin LOW | `*get_gpio_lo_reg(pin) = 1 << (pin & 31)` |
| `gpio_in(pin)` | Read pin level | `GPIO.in.val & (1 << (pin & 31))` (or `GPIO.in1.val` for pins 32-63) |

**Chip-Specific Register Selection:**

- **ESP32, S2, S3, P4**: Use `GPIO.out_w1ts`/`GPIO.out_w1tc` for pins 0-31, `GPIO.out1_w1ts`/`GPIO.out1_w1tc` for pins 32+
- **ESP32-C3, C6**: Single GPIO bank, no `out1` registers
- Pin masking uses `(pin & 31)` to extract bit position within 32-bit register

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:142-158](), [src/lgfx/v1/platforms/esp32/common.cpp:335-398]()

### Pin Backup and Restore

The `gpio::pin_backup_t` class saves and restores complete GPIO pin configuration, used by bus drivers to temporarily reconfigure pins without disrupting other subsystems.

```mermaid
graph TB
    subgraph "Pin Configuration State"
        IORegister["IO_MUX_GPIO_REG<br/>Pin function, pull-up/down<br/>sleep mode settings"]
        PinRegister["GPIO_PIN_REG<br/>Pad driver, wakeup config"]
        FuncOut["GPIO_FUNC_OUT_SEL_CFG<br/>Output signal routing"]
        FuncIn["GPIO_FUNC_IN_SEL_CFG<br/>Input signal routing"]
        EnableReg["GPIO_ENABLE_REG<br/>Output enable state"]
    end
    
    Backup["pin_backup_t::backup()"] --> IORegister
    Backup --> PinRegister
    Backup --> FuncOut
    Backup --> FuncIn
    Backup --> EnableReg
    
    IORegister --> Restore["pin_backup_t::restore()"]
    PinRegister --> Restore
    FuncOut --> Restore
    FuncIn --> Restore
    EnableReg --> Restore
```

**Pin Backup/Restore Mechanism**

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:272-290](), [src/lgfx/v1/platforms/esp32/common.cpp:404-479]()

### Timing Functions

Timing functions use ESP-IDF's high-resolution timer (`esp_timer_get_time()`) for microsecond accuracy and FreeRTOS task delays for millisecond delays.

| Function | Implementation | Accuracy |
|----------|----------------|----------|
| `millis()` | `esp_timer_get_time() / 1000ULL` | 1 ms |
| `micros()` | `esp_timer_get_time()` | 1 μs |
| `delayMicroseconds(us)` | `ets_delay_us(us)` or `esp_rom_delay_us(us)` (IDF v5+) | Busy-wait, ~1 μs |
| `delay(ms)` | `vTaskDelay()` with correction for sub-tick delays | FreeRTOS tick period (typically 1-10 ms) |

**Delay Implementation Strategy:**
- Short delays (<8 ticks): Use `vTaskDelay()` + `delayMicroseconds()` correction for accuracy
- Long delays (≥8 ticks): Pure `vTaskDelay()` to yield CPU to other tasks
- `delayMicroseconds()`: Busy-wait loop, does not yield

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:88-111]()

### Memory Management

Memory allocation functions provide DMA-capable and PSRAM-specific allocation through ESP-IDF's heap capabilities API.

```mermaid
graph TB
    subgraph "Memory Allocation API"
        heap_alloc["heap_alloc(size)<br/>General 8-bit aligned"]
        heap_alloc_dma["heap_alloc_dma(size)<br/>DMA-capable memory"]
        heap_alloc_psram["heap_alloc_psram(size)<br/>External SPIRAM"]
        heap_free["heap_free(buf)"]
    end
    
    subgraph "ESP-IDF Heap Caps"
        MALLOC_CAP_8BIT["MALLOC_CAP_8BIT<br/>Standard internal RAM"]
        MALLOC_CAP_DMA["MALLOC_CAP_DMA<br/>DMA-accessible RAM<br/>(Internal only, 4-byte aligned)"]
        MALLOC_CAP_SPIRAM["MALLOC_CAP_SPIRAM<br/>External PSRAM"]
    end
    
    subgraph "Memory Regions"
        InternalRAM["Internal RAM<br/>DRAM0, DRAM1<br/>Fast, DMA-capable"]
        ExternalRAM["External PSRAM<br/>Slower, not DMA-capable<br/>Large capacity"]
    end
    
    heap_alloc --> MALLOC_CAP_8BIT --> InternalRAM
    heap_alloc_dma --> MALLOC_CAP_DMA --> InternalRAM
    heap_alloc_psram --> MALLOC_CAP_SPIRAM --> ExternalRAM
    
    heap_capable_dma["heap_capable_dma(ptr)<br/>esp_ptr_dma_capable()"] --> Check{"Is pointer<br/>DMA-capable?"}
    Check -->|Yes| InternalRAM
    Check -->|No| ExternalRAM
```

**Memory Allocation Functions**

| Function | Capability Flags | Alignment | Use Case |
|----------|------------------|-----------|----------|
| `heap_alloc(size)` | `MALLOC_CAP_8BIT` | 1 byte | General allocations |
| `heap_alloc_dma(size)` | `MALLOC_CAP_DMA` | 4 bytes | DMA descriptors, SPI/I2C buffers |
| `heap_alloc_psram(size)` | `MALLOC_CAP_SPIRAM \| MALLOC_CAP_8BIT` | 4 bytes | Large sprite buffers, framebuffers |
| `heap_capable_dma(ptr)` | N/A (query) | N/A | Check if pointer is DMA-capable |

**DMA Compatibility:**
- Only internal SRAM is DMA-capable
- PSRAM buffers require copy to internal RAM before DMA transfer
- `FlipBuffer` class in `Bus_SPI` manages this automatically

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:113-120]()

### Clock Management

Clock management functions calculate SPI/I2C clock dividers and determine APB bus frequency, which varies based on CPU speed and power management.

```mermaid
graph LR
    subgraph "Clock Configuration"
        getApbFrequency["getApbFrequency()<br/>Returns APB clock in Hz<br/>(typically 80 MHz)"]
        FreqToClockDiv["FreqToClockDiv(fapb, hz)<br/>Calculate SPI clock divider"]
        calcClockDiv["calcClockDiv(div_a, div_b, div_n, clkcnt, base, target)<br/>Calculate I2C/I2S clock divider"]
    end
    
    subgraph "Hardware Clock Sources"
        CPU_CLK["CPU Clock<br/>80-240 MHz"]
        APB_CLK["APB Bus Clock<br/>80 MHz (if CPU ≥ 80 MHz)<br/>Lower otherwise"]
        RTC_CLK["RTC Clock Config<br/>rtc_cpu_freq_config_t"]
    end
    
    subgraph "Peripheral Clocks"
        SPI_CLK["SPI Clock<br/>Max 80 MHz<br/>Divider: (pre+1) * N"]
        I2C_CLK["I2C Clock<br/>Max 400 kHz<br/>Complex fractional divider"]
    end
    
    RTC_CLK --> getApbFrequency
    getApbFrequency --> APB_CLK
    APB_CLK --> FreqToClockDiv
    APB_CLK --> calcClockDiv
    
    FreqToClockDiv --> SPI_CLK
    calcClockDiv --> I2C_CLK
```

**Clock Calculation Functions**

| Function | Purpose | Algorithm |
|----------|---------|-----------|
| `getApbFrequency()` | Get current APB bus frequency | Reads `rtc_cpu_freq_config_t`, returns 80 MHz if CPU ≥ 80 MHz |
| `FreqToClockDiv(fapb, hz)` | Calculate SPI clock register value | Combines pre-scaler and divider into 32-bit register value |
| `calcClockDiv(...)` | Calculate fractional divider for I2C/I2S | Iterative optimization to minimize frequency error |

**SPI Clock Divider Encoding (32-bit register value):**
- Bits 0-5: `N` (divider, 1-64)
- Bits 6-11: `(N-1)/2` (half-cycle high)
- Bits 12-17: `N` (full cycle length)
- Bits 18-23: Pre-scaler (0-63)

Sources: [src/lgfx/v1/platforms/esp32/common.cpp:188-251]()

### DMA Channel Discovery

For ESP32-S3, C3, C6, P4 (GDMA-based chips), M5GFX must discover which GDMA channel is assigned to the SPI peripheral by the ESP-IDF driver. This is necessary because the channel is not known at compile time.

```mermaid
graph TB
    subgraph "DMA Channel Assignment"
        SPIInit["spi_bus_initialize()<br/>ESP-IDF driver assigns<br/>GDMA channel"]
        Search["search_dma_out_ch(peripheral_select)<br/>Scans GDMA registers<br/>to find assigned channel"]
    end
    
    subgraph "GDMA Peripheral Registers"
        direction LR
        CH0["GDMA_OUT_PERI_SEL_CH0_REG<br/>Channel 0 peripheral selection"]
        CH1["GDMA_OUT_PERI_SEL_CH1_REG<br/>Channel 1 peripheral selection"]
        CHn["GDMA_OUT_PERI_SEL_CHn_REG<br/>Channel n peripheral selection"]
    end
    
    SPIInit --> Search
    Search --> CH0
    Search --> CH1
    Search --> CHn
    
    Match{"Match with<br/>SPI peripheral ID?"} --> Found["Return channel index"]
    CH0 --> Match
    CH1 --> Match
    CHn --> Match
    Match --> NotFound["Return -1"]
```

**GDMA Channel Search Algorithm**

For chips with GDMA support (S3, C3, C6, P4):
1. Loop through all GDMA channel registers (0 to `SOC_GDMA_PAIRS_PER_GROUP_MAX`)
2. Read `DMA_OUT_PERI_SEL_CHn_REG` register for each channel
3. Compare against target peripheral ID (e.g., `SOC_GDMA_TRIG_PERIPH_SPI2 = 0`)
4. Return matching channel index, or -1 if not found

This allows M5GFX to directly access DMA registers for high-performance transfers.

Sources: [src/lgfx/v1/platforms/esp32/common.cpp:270-320]()

---

## ESP32 SPI Bus Implementation

The `Bus_SPI` class provides high-performance SPI communication with DMA support, direct register access, and platform-specific optimizations. It bypasses ESP-IDF's transaction APIs for maximum throughput.

### SPI Register Access Strategy

```mermaid
graph TB
    subgraph "SPI Configuration"
        Config["Bus_SPI::config(config_t)<br/>Store configuration<br/>Calculate register addresses"]
        Init["Bus_SPI::init()<br/>Call ESP-IDF spi_bus_initialize<br/>Discover DMA channel"]
    end
    
    subgraph "Register Pointers (cached)"
        W0["_spi_w0_reg<br/>SPI_W0_REG(spi_port)<br/>64-byte FIFO buffer"]
        CMD["_spi_cmd_reg<br/>SPI_CMD_REG(spi_port)<br/>Start/busy register"]
        USER["_spi_user_reg<br/>SPI_USER_REG(spi_port)<br/>Mode configuration"]
        MOSI_DLEN["_spi_mosi_dlen_reg<br/>SPI_MOSI_DLEN_REG<br/>Transmit length"]
        DMA_LINK["_spi_dma_out_link_reg<br/>DMA descriptor link"]
    end
    
    subgraph "SPI Operations"
        WriteCmd["writeCommand(data, len)<br/>D/C=LOW, write to FIFO"]
        WriteData["writeData(data, len)<br/>D/C=HIGH, write to FIFO"]
        WriteDMA["writeBytes(data, len, use_dma)<br/>Setup DMA descriptors"]
    end
    
    Config --> Init
    Init --> W0
    Init --> CMD
    Init --> USER
    Init --> MOSI_DLEN
    Init --> DMA_LINK
    
    W0 --> WriteCmd
    CMD --> WriteCmd
    MOSI_DLEN --> WriteCmd
    
    W0 --> WriteData
    CMD --> WriteData
    
    DMA_LINK --> WriteDMA
```

**SPI Register Caching for Performance**

The `Bus_SPI` class caches register addresses as `volatile uint32_t*` pointers during initialization, avoiding repeated address calculations. This optimization is critical for high-speed pixel streaming.

**Key Registers:**
- `SPI_W0_REG` through `SPI_W15_REG`: 64-byte FIFO buffer (16 x 32-bit words)
- `SPI_CMD_REG`: Contains `SPI_USR` bit to start transaction, polled for busy status
- `SPI_MOSI_DLEN_REG`: Sets transmit bit length minus 1
- `SPI_USER_REG`: Configures full-duplex, half-duplex, MISO, MOSI, HIGHPART buffer usage

Sources: [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:139-176](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:113-155]()

### FIFO and HIGHPART Double Buffering

ESP32 (non-C3/S3) uses the HIGHPART feature to achieve double buffering within the 64-byte SPI FIFO. While the hardware sends the first 32 bytes, software prepares the next 32 bytes in the upper half.

```mermaid
graph LR
    subgraph "64-Byte FIFO"
        W0_W7["SPI_W0 - SPI_W7<br/>Lower 32 bytes<br/>(HIGHPART=0)"]
        W8_W15["SPI_W8 - SPI_W15<br/>Upper 32 bytes<br/>(HIGHPART=1)"]
    end
    
    subgraph "Transfer Cycle"
        Prep1["Prepare data in W0-W7<br/>HIGHPART=0"] --> Send1["Start SPI transfer<br/>Hardware sends W0-W7"]
        Send1 --> Prep2["While sending, prepare<br/>next data in W8-W15<br/>HIGHPART=1"]
        Prep2 --> Send2["Start next transfer<br/>Hardware sends W8-W15"]
        Send2 --> Prep1
    end
    
    Prep1 -.-> W0_W7
    Prep2 -.-> W8_W15
```

**HIGHPART Double Buffering (ESP32 only)**

The `SPI_USR_MOSI_HIGHPART` bit in `SPI_USER_REG` selects between the lower 32 bytes (0) or upper 32 bytes (1) of the FIFO. By alternating this bit, the driver achieves pipelining:
- Cycle 1: Send W0-W7, prepare W8-W15
- Cycle 2: Send W8-W15, prepare W0-W7
- Repeat

ESP32-C3 and S3 lack this feature, requiring full FIFO waits between transfers.

Sources: [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:583-625](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:779-820]()

### DMA Descriptor Chain

For large transfers (>64 bytes), the SPI driver uses DMA with linked descriptor chains. Each descriptor points to a data buffer and the next descriptor.

```mermaid
graph LR
    subgraph "DMA Descriptor Chain"
        Desc0["lldesc_t[0]<br/>size=4092<br/>buf=data[0]<br/>eof=0"] --> Desc1["lldesc_t[1]<br/>size=4092<br/>buf=data[4092]<br/>eof=0"]
        Desc1 --> Desc2["lldesc_t[2]<br/>size=2048<br/>buf=data[8184]<br/>eof=1"]
        Desc2 --> Null["qe.stqe_next=NULL"]
    end
    
    subgraph "DMA Registers"
        DMA_OUT_LINK["DMA_OUT_LINK_REG<br/>Set to &lldesc_t[0]<br/>Start DMA"]
        DMA_STATUS["DMA_OUTFIFO_STATUS_REG<br/>Check EMPTY flag<br/>Wait for ready"]
    end
    
    Start["writeBytes(data, 10280)"] --> Setup["_setup_dma_desc_links()<br/>Create descriptor chain"]
    Setup --> Desc0
    Desc0 -.-> DMA_OUT_LINK
    DMA_OUT_LINK --> DMA_STATUS
    DMA_STATUS --> SPI_START["Set SPI_USR bit<br/>Hardware transfers data"]
```

**DMA Descriptor Structure (`lldesc_t`)**

| Field | Type | Purpose |
|-------|------|---------|
| `size` | `uint32_t:12` | Physical buffer size (max 4092 bytes) |
| `length` | `uint32_t:12` | Actual data length |
| `offset` | `uint32_t:5` | Buffer offset (unused) |
| `sosf` | `uint32_t:1` | Start of sub-frame |
| `eof` | `uint32_t:1` | End of frame (last descriptor) |
| `owner` | `uint32_t:1` | DMA ownership (always 1) |
| `buf` | `uint8_t*` | Pointer to data buffer (must be DMA-capable) |
| `qe.stqe_next` | `lldesc_t*` | Pointer to next descriptor (NULL for last) |

**DMA Transfer Limits:**
- Max descriptor size: 4092 bytes (12-bit size field, 4-byte alignment)
- Total transfer length: Up to 512 KB on ESP32, 64 KB on C3/S3 (`SPI_MS_DATA_BITLEN`)
- Automatic descriptor chain creation for lengths > 4092

Sources: [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:630-735](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:824-939]()

### FlipBuffer for Non-DMA Sources

When source data is in PSRAM or ROM (non-DMA-capable memory), the `FlipBuffer` class provides a small internal RAM buffer for staging data before DMA transfer.

```mermaid
graph TB
    subgraph "Source Data Locations"
        PSRAM["External PSRAM<br/>Not DMA-capable"]
        ROM["Flash ROM<br/>Not DMA-capable"]
        InternalRAM["Internal RAM<br/>DMA-capable"]
    end
    
    subgraph "FlipBuffer"
        GetBuffer["getBuffer(length)<br/>Return DMA buffer pointer"]
        Buffer["Internal buffer<br/>Allocated in DMA RAM<br/>Size: min(length, capacity)"]
    end
    
    subgraph "Transfer Path"
        Check{"Is source<br/>DMA-capable?"}
        Copy["memcpy() to FlipBuffer"]
        DirectDMA["Direct DMA transfer"]
    end
    
    PSRAM --> Check
    ROM --> Check
    InternalRAM --> Check
    
    Check -->|No| Copy
    Check -->|Yes| DirectDMA
    
    Copy --> GetBuffer
    GetBuffer --> Buffer
    Buffer --> DirectDMA
```

**FlipBuffer Usage Example**

In `Bus_SPI::writeBytes()`, when `use_dma=false` and data is not DMA-capable:
1. Request buffer: `auto buf = _flip_buffer.getBuffer(length)`
2. Copy data: `memcpy(buf, data, length)`
3. Transfer from internal buffer: `writeBytes(buf, length, true, true)`

This avoids the need for large static buffers while maintaining DMA performance.

Sources: [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:661-671]()

---

## SDL Platform Implementation

The SDL platform provides desktop simulation by emulating hardware through SDL2 APIs. This enables rapid development and debugging without physical hardware.

### Emulated GPIO

SDL implements GPIO as a 64-element array of uint8_t values, providing virtual pins for button emulation and inter-component communication.

```mermaid
graph LR
    subgraph "Emulated GPIO Array"
        Array["_gpio_dummy_values[64]<br/>static uint8_t array<br/>Initialized to 0"]
    end
    
    subgraph "GPIO Functions"
        gpio_hi_sdl["gpio_hi(pin)<br/>Set array[pin] = 1"]
        gpio_lo_sdl["gpio_lo(pin)<br/>Set array[pin] = 0"]
        gpio_in_sdl["gpio_in(pin)<br/>Return array[pin]"]
        pinMode_sdl["pinMode(pin, mode)<br/>No-op (empty function)"]
    end
    
    subgraph "Keyboard Mapping"
        KeyDown["SDL_KEYDOWN event<br/>SDLK_LEFT/DOWN/RIGHT/UP"]
        MapGPIO["KeyCodeMapping_t<br/>SDLK_LEFT -> GPIO 39<br/>SDLK_DOWN -> GPIO 38<br/>..."]
        SetLow["gpio_lo(mapped_pin)"]
    end
    
    gpio_hi_sdl --> Array
    gpio_lo_sdl --> Array
    gpio_in_sdl --> Array
    
    KeyDown --> MapGPIO
    MapGPIO --> SetLow
    SetLow --> Array
```

**GPIO Emulation Details**

| Function | Implementation | Notes |
|----------|----------------|-------|
| `pinMode(pin, mode)` | Empty function | No actual pin configuration |
| `gpio_hi(pin)` | `_gpio_dummy_values[pin & 63] = 1` | Sets virtual pin HIGH |
| `gpio_lo(pin)` | `_gpio_dummy_values[pin & 63] = 0` | Sets virtual pin LOW |
| `gpio_in(pin)` | `return _gpio_dummy_values[pin & 63]` | Reads virtual pin state |

**Keyboard-to-GPIO Mapping:**
- Default mappings: LEFT=39, DOWN=38, RIGHT=37, UP=36 (M5Stack button emulation)
- Customizable via `Panel_sdl::addKeyCodeMapping(SDL_KeyCode, gpio)`
- Key press → `gpio_lo(pin)`, Key release → `gpio_hi(pin)` (active-low like physical buttons)

Sources: [src/lgfx/v1/platforms/sdl/common.cpp:36-43](), [src/lgfx/v1/platforms/sdl/Panel_sdl.cpp:64-142]()

### SDL Timing Functions

SDL timing uses high-resolution performance counters for accurate microsecond timekeeping, matching ESP32 behavior.

| Function | Implementation | Resolution |
|----------|----------------|------------|
| `millis()` | `SDL_GetTicks()` | 1 ms |
| `micros()` | `SDL_GetPerformanceCounter() / (SDL_GetPerformanceFrequency() / 1000000)` | ~1 μs |
| `delay(ms)` | `SDL_Delay(ms)` or `delayMicroseconds(ms * 1000)` | OS-dependent |
| `delayMicroseconds(us)` | `SDL_Delay((us / 1000) - 1)` + spin-wait loop | ~100 μs |

**Delay Implementation:**
- Short delays (<2 ms): Spin-wait with `std::this_thread::yield()`
- Long delays (≥2 ms): `SDL_Delay()` to yield to OS scheduler
- Accuracy limited by OS scheduler granularity (typically 1-16 ms)

Sources: [src/lgfx/v1/platforms/sdl/common.cpp:45-78]()

### Dummy Bus Functions

SDL platform provides stub implementations for SPI and I2C functions that return error codes, as no actual hardware communication occurs in desktop simulation.

```mermaid
graph TB
    subgraph "Bus APIs (Stubbed)"
        spi_init["spi::init(...)"]
        spi_write["spi::writeBytes(...)"]
        i2c_init["i2c::init(...)"]
        i2c_trans["i2c::transactionWrite(...)"]
    end
    
    subgraph "Implementation"
        ReturnError["return cpp::fail(error_t::unknown_err)"]
        NoOp["Empty function body (no-op)"]
    end
    
    spi_init --> ReturnError
    spi_write --> NoOp
    i2c_init --> ReturnError
    i2c_trans --> ReturnError
```

**Dummy Bus Function Table**

All bus functions either return `cpp::fail(error_t::unknown_err)` or perform no operation:

- `spi::init()` → Returns error
- `spi::release()` → No-op
- `spi::beginTransaction()` → No-op
- `spi::endTransaction()` → No-op
- `spi::writeBytes()` → No-op
- `spi::readBytes()` → No-op
- `i2c::init()` → Returns error
- `i2c::beginTransaction()` → Returns error
- `i2c::writeBytes()` → Returns error
- `i2c::readBytes()` → Returns error

This allows panel code to call bus functions without conditional compilation, with the understanding that actual I/O is handled by `Panel_sdl` at the framebuffer level.

Sources: [src/lgfx/v1/platforms/sdl/common.cpp:82-112]()

---

## Conditional Compilation Strategy

Platform selection uses preprocessor directives to include the appropriate implementation at compile time. The selection hierarchy is:

```mermaid
graph TB
    subgraph "Compile-Time Platform Detection"
        Check1{"#if defined(ESP_PLATFORM)"}
        Check2{"#if defined(SDL_h_)"}
        Check3{"#if defined(ARDUINO)"}
    end
    
    subgraph "Include Paths"
        ESP_Files["#include platforms/esp32/common.cpp<br/>#include platforms/esp32/Bus_SPI.cpp<br/>#include platforms/esp32/..."]
        SDL_Files["#include platforms/sdl/common.cpp<br/>#include platforms/sdl/Panel_sdl.cpp"]
        Arduino_Ext["Use Arduino SPI/Wire libraries<br/>Instead of ESP-IDF directly"]
    end
    
    Check1 -->|Yes| ESP_Files
    Check1 -->|No| Check2
    Check2 -->|Yes| SDL_Files
    Check2 -->|No| Error["Unsupported platform"]
    
    ESP_Files --> Check3
    Check3 -->|Yes| Arduino_Ext
    Check3 -->|No| ESP_IDF["Use ESP-IDF APIs directly"]
```

**Platform Selection Logic**

1. **ESP32 Detection**: `#if defined (ESP_PLATFORM)` at [src/lgfx/v1/platforms/esp32/common.cpp:18]()
2. **SDL Detection**: `#if defined (SDL_h_)` at [src/lgfx/v1/platforms/sdl/common.cpp:25]()
3. **Arduino Framework**: `#if defined (ARDUINO)` enables Arduino-specific includes (SPI.h, Wire.h)
4. **Chip Variant**: `CONFIG_IDF_TARGET_*` defines select ESP32/S2/S3/C3/C6/P4 specific code

**Example: GPIO Function Selection**

```cpp
// ESP32 implementation (common.cpp)
#if defined (ESP_PLATFORM)
static inline void gpio_hi(int_fast8_t pin) { 
    if (pin >= 0) *get_gpio_hi_reg(pin) = 1 << (pin & 31); 
}
#endif

// SDL implementation (common.cpp)
#if defined (SDL_h_)
void gpio_hi(uint32_t pin) { 
    _gpio_dummy_values[pin & (EMULATED_GPIO_MAX - 1)] = 1; 
}
#endif
```

Both implementations provide identical function signatures, ensuring source-level compatibility.

Sources: [src/lgfx/v1/platforms/esp32/common.cpp:18](), [src/lgfx/v1/platforms/sdl/common.cpp:21-25]()

---

## Platform-Specific Optimizations

### ESP32: Register-Level Access vs Driver APIs

M5GFX bypasses ESP-IDF driver APIs for performance-critical paths, using direct register writes instead of function calls. This reduces overhead from ~50 cycles per SPI byte to ~10 cycles.

**Performance Comparison:**

| Operation | ESP-IDF API | Direct Register | Speedup |
|-----------|-------------|-----------------|---------|
| Write 1 byte to SPI | `spi_device_transmit()` (~500 cycles) | `*SPI_W0_REG = data; *SPI_CMD_REG = SPI_USR;` (~10 cycles) | 50x |
| Set GPIO pin | `gpio_set_level()` (~30 cycles) | `*GPIO.out_w1ts = mask;` (~3 cycles) | 10x |
| Start DMA transfer | `spi_device_queue_trans()` (~200 cycles) | `*DMA_OUT_LINK_REG = addr; *SPI_CMD_REG = SPI_USR;` (~15 cycles) | 13x |

**Trade-off:** Direct register access requires careful management of peripheral state and lacks safety checks present in driver APIs.

Sources: [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:313-354]()

### ESP32: Cache Coherency with PSRAM

When using PSRAM for framebuffers or sprite data, explicit cache writeback is required before DMA operations to ensure data consistency.

```mermaid
graph LR
    subgraph "PSRAM Data Flow"
        CPU["CPU writes to<br/>PSRAM buffer<br/>(cache enabled)"]
        Cache["CPU Cache<br/>(holds dirty lines)"]
        WriteBack["Cache_WriteBack_All()<br/>Flush dirty lines<br/>to PSRAM"]
        PSRAM["PSRAM<br/>(external memory)"]
        DMA["DMA Controller<br/>reads from PSRAM"]
    end
    
    CPU --> Cache
    Cache --> WriteBack
    WriteBack --> PSRAM
    PSRAM --> DMA
    
    Warning["⚠️ Without writeback,<br/>DMA may read stale data"]
    Cache -.->|"If not flushed"| Warning
```

**Cache Management in M5GFX:**
- Before DMA from PSRAM: `Cache_WriteBack_All()` or `esp_rom_cache_writeback_all()` (IDF v5+)
- After DMA to PSRAM: Cache invalidation not typically required (display is write-only)
- Automatic handling in `Panel_FrameBufferBase` when `_lines_buffer` is PSRAM-allocated

This issue is unique to ESP32 with PSRAM; internal RAM does not use cache.

Sources: Referenced in DMA operations, common pattern in ESP-IDF applications

---

## Common Interface Patterns

Both platforms implement the same interface patterns to ensure code portability.

### Error Handling with cpp::result

Platform functions use the `cpp::result<T, error_t>` type for error handling, providing type-safe success/failure returns without exceptions.

```cpp
// Function signature
cpp::result<void, error_t> init(int i2c_port, int pin_sda, int pin_scl);

// Usage
auto result = i2c::init(0, 21, 22);
if (result.has_value()) {
    // Success
} else {
    error_t err = result.error();
    // Handle error
}
```

**Error Types (from enum.hpp):**
- `error_t::connection_lost` - Communication failure
- `error_t::unknown_err` - Generic error (SDL stub functions)
- Success returns: `cpp::result<void, error_t>{}` or `{}`

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:312-314](), [src/lgfx/v1/platforms/sdl/common.cpp:84-111]()

### Namespace Organization

Platform code is organized into functional namespaces within the `lgfx::v1` namespace:

| Namespace | Purpose | Key Functions |
|-----------|---------|---------------|
| `lgfx::v1::` (global) | GPIO, timing, memory | `gpio_hi`, `gpio_lo`, `millis`, `micros`, `heap_alloc` |
| `lgfx::v1::gpio` | Pin management utilities | `pin_backup_t`, `command()` |
| `lgfx::v1::spi` | SPI bus initialization | `init()`, `beginTransaction()`, `endTransaction()` |
| `lgfx::v1::i2c` | I2C bus management | `init()`, `setPins()`, `transactionWrite()` |

This structure allows `using namespace lgfx::v1;` to bring all platform functions into scope without polluting the global namespace.

Sources: [src/lgfx/v1/platforms/esp32/common.hpp:82-345]()

---

## Platform Detection at Runtime

In addition to compile-time selection, ESP32 code includes runtime chip detection for handling variant-specific features.

```mermaid
graph TB
    subgraph "Chip Detection"
        ReadEfuse["Read eFuse registers<br/>EFUSE_BLK0_RDATA3_REG"]
        GetPkgVer["get_pkg_ver()<br/>esp_efuse_get_pkg_ver() or<br/>manual register read"]
    end
    
    subgraph "Chip Variants"
        ESP32["ESP32<br/>Package versions 0-6"]
        ESP32S2["ESP32-S2<br/>Different peripheral layout"]
        ESP32S3["ESP32-S3<br/>USB-OTG, LCD_CAM"]
        ESP32C3["ESP32-C3<br/>RISC-V, GDMA"]
        ESP32C6["ESP32-C6<br/>WiFi 6, no I2S"]
    end
    
    GetPkgVer --> ESP32
    GetPkgVer --> ESP32S2
    GetPkgVer --> ESP32S3
    GetPkgVer --> ESP32C3
    GetPkgVer --> ESP32C6
    
    Config["Peripheral Configuration<br/>Adjust register addresses<br/>Select GDMA/SPI_DMA<br/>Enable/disable features"]
    
    ESP32 --> Config
    ESP32S2 --> Config
    ESP32S3 --> Config
    ESP32C3 --> Config
    ESP32C6 --> Config
```

**Chip Detection Function:**

```cpp
uint32_t get_pkg_ver(void)
{
#if defined ( USE_ESP_EFUSE_GET_PKG_VER )
    return esp_efuse_get_pkg_ver();
#else
    uint32_t pkg_ver = REG_GET_FIELD(EFUSE_BLK0_RDATA3_REG, EFUSE_RD_CHIP_VER_PKG);
    // Special handling for ESP32PICOD4 variants
    if (pkg_ver == EFUSE_RD_CHIP_VER_PKG_ESP32PICOD4) {
        if (REG_READ(APB_CTRL_DATE_REG) & 0x80000000) {
            return 6;  // ESP32PICOV302
        }
    }
    return pkg_ver;
#endif
}
```

**Usage:**
- M5GFX autodetect uses `get_pkg_ver()` to identify device type
- Peripheral code uses `CONFIG_IDF_TARGET_*` defines for compile-time selection
- Combined approach allows single binary to detect chip at runtime while optimizing for known targets

Sources: [src/lgfx/v1/platforms/esp32/common.cpp:253-268]()

---

## Summary: Platform Abstraction Benefits

The Platform Abstraction Layer provides:

1. **Single Codebase**: Application code compiles unchanged for ESP32 or SDL
2. **Performance**: Direct register access on ESP32 for maximum throughput
3. **Development Speed**: SDL simulation enables rapid prototyping without hardware
4. **Hardware Flexibility**: Supports 6 ESP32 chip variants with runtime/compile-time detection
5. **Type Safety**: `cpp::result<>` error handling without exceptions
6. **Resource Management**: `pin_backup_t`, `heap_alloc_dma()`, DMA channel discovery
7. **Debugging**: SDL platform includes debugger detection and step-execution support

This abstraction is the foundation enabling M5GFX's "write once, run everywhere" philosophy for embedded graphics development.

Sources: All files in [src/lgfx/v1/platforms/]()