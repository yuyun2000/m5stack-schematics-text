M5UnitUnified GPIO and RMT

# GPIO and RMT

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/m5_unit_component/adapter_gpio.cpp](src/m5_unit_component/adapter_gpio.cpp)
- [src/m5_unit_component/adapter_gpio.hpp](src/m5_unit_component/adapter_gpio.hpp)
- [src/m5_unit_component/adapter_gpio_v1.cpp](src/m5_unit_component/adapter_gpio_v1.cpp)
- [src/m5_unit_component/adapter_gpio_v2.cpp](src/m5_unit_component/adapter_gpio_v2.cpp)
- [src/m5_unit_component/adapter_gpio_v2.hpp](src/m5_unit_component/adapter_gpio_v2.hpp)
- [src/m5_unit_component/identify_functions.hpp](src/m5_unit_component/identify_functions.hpp)
- [src/m5_unit_component/types.hpp](src/m5_unit_component/types.hpp)

</details>



## Purpose and Scope

This page covers the `AdapterGPIO` implementation, which provides unified access to GPIO operations and the RMT (Remote Control) peripheral across different ESP-IDF versions. The adapter supports digital I/O, analog read/write, pulse timing, and precise signal transmission/reception using ESP32's RMT hardware.

For I2C communication, see [I2C Communication](#4.1). For UART communication, see [UART Communication](#4.3). For the general adapter pattern architecture, see [Adapter Pattern](#3.3).

## Architecture Overview

The GPIO adapter uses a version-specific implementation pattern, automatically selecting between RMT v1 (ESP-IDF 4.x) and RMT v2 (ESP-IDF 5.x+) based on compile-time detection.

### Class Hierarchy

```mermaid
graph TB
    subgraph "Adapter Layer"
        AdapterBase["Adapter<br/>(adapter_base.hpp)"]
        AdapterGPIOBase["AdapterGPIOBase<br/>(adapter_gpio.hpp)"]
    end
    
    subgraph "Implementation Interface"
        GPIOImpl["GPIOImpl<br/>Abstract Interface<br/>pin_mode, write_digital,<br/>read_digital, read_analog,<br/>write_analog, pulse_in"]
    end
    
    subgraph "Version-Specific Implementations"
        GPIOImplV1["GPIOImplV1<br/>adapter_gpio_v1.cpp<br/>ESP-IDF 4.x<br/>rmt_config_t<br/>rmt_item32_t"]
        GPIOImplV2["GPIOImplV2<br/>adapter_gpio_v2.cpp<br/>ESP-IDF 5.x+<br/>rmt_tx_channel_config_t<br/>rmt_symbol_word_t"]
    end
    
    subgraph "Public Interface"
        AdapterGPIO["AdapterGPIO<br/>User-facing class"]
    end
    
    AdapterBase --> AdapterGPIOBase
    AdapterGPIOBase --> GPIOImpl
    GPIOImpl --> GPIOImplV1
    GPIOImpl --> GPIOImplV2
    AdapterGPIOBase --> AdapterGPIO
    
    VersionDetect["M5_UNIT_UNIFIED_USING_RMT_V2<br/>define in identify_functions.hpp"] -.selects.-> GPIOImplV1
    VersionDetect -.selects.-> GPIOImplV2
```

**Sources:** [src/m5_unit_component/adapter_gpio.hpp:41-158](), [src/m5_unit_component/adapter_gpio_v1.cpp:117-297](), [src/m5_unit_component/adapter_gpio_v2.cpp:140-196]()

## ESP-IDF Version Detection

The library automatically detects the ESP-IDF version and selects the appropriate RMT implementation at compile time.

### Version Detection Logic

| Define | Condition | RMT Version | ADC API |
|--------|-----------|-------------|---------|
| `M5_UNIT_UNIFIED_USING_RMT_V2` | ESP-IDF ≥ 5.0.0 | RMT v2 | Oneshot |
| Not defined | ESP-IDF < 5.0.0 | RMT v1 | Legacy |

The detection occurs in [src/m5_unit_component/identify_functions.hpp:22-25]():

```cpp
#if ESP_IDF_VERSION >= ESP_IDF_VERSION_VAL(5, 0, 0)
#define M5_UNIT_UNIFIED_USING_RMT_V2
#define M5_UNIT_UNIFIED_USING_ADC_ONESHOT
#endif
```

### Conditional Compilation

The implementation files use conditional compilation to include only the relevant version:

- **RMT v1**: [src/m5_unit_component/adapter_gpio_v1.cpp:13-306]() compiles when `M5_UNIT_UNIFIED_USING_RMT_V2` is not defined
- **RMT v2**: [src/m5_unit_component/adapter_gpio_v2.cpp:12-416]() compiles when `M5_UNIT_UNIFIED_USING_RMT_V2` is defined

**Sources:** [src/m5_unit_component/identify_functions.hpp:13-27](), [src/m5_unit_component/adapter_gpio_v1.cpp:13](), [src/m5_unit_component/adapter_gpio_v2.cpp:12]()

## GPIO Operations

The `AdapterGPIOBase::GPIOImpl` class provides fundamental GPIO operations that work across all ESP32 variants.

### Digital Operations

```mermaid
graph LR
    subgraph "Pin Configuration"
        pinMode["pin_mode()<br/>gpio_config()"]
        ModeEnum["gpio::Mode enum<br/>Input, Output,<br/>InputPullup, etc."]
    end
    
    subgraph "Digital I/O"
        writeDigital["write_digital()<br/>gpio_set_level()"]
        readDigital["read_digital()<br/>gpio_get_level()"]
    end
    
    subgraph "Configuration Table"
        ConfigTable["gpio_cfg_table[]<br/>adapter_gpio.cpp:45-145<br/>9 predefined configs"]
    end
    
    ModeEnum --> pinMode
    ConfigTable --> pinMode
    pinMode --> writeDigital
    pinMode --> readDigital
```

### Pin Mode Configuration

The adapter uses a pre-configured table of `gpio_config_t` structures for different pin modes. Each mode is mapped to a specific configuration:

| Mode | GPIO Mode | Pull-up | Pull-down |
|------|-----------|---------|-----------|
| `Input` | `GPIO_MODE_INPUT` | Disabled | Disabled |
| `Output` | `GPIO_MODE_OUTPUT` | Disabled | Disabled |
| `InputPullup` | `GPIO_MODE_INPUT` | Enabled | Disabled |
| `InputPulldown` | `GPIO_MODE_INPUT` | Disabled | Enabled |
| `OpenDrain` | `GPIO_MODE_OUTPUT_OD` | Enabled | Disabled |
| `OutputOpenDrain` | `GPIO_MODE_OUTPUT_OD` | Disabled | Disabled |
| `Analog` | `GPIO_MODE_DISABLE` | Disabled | Disabled |

The `pin_mode()` function at [src/m5_unit_component/adapter_gpio.cpp:349-358]() applies these configurations.

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:44-145](), [src/m5_unit_component/types.hpp:60-74](), [src/m5_unit_component/adapter_gpio.cpp:349-358]()

### Analog Operations

The adapter provides ADC (Analog-to-Digital Converter) and DAC (Digital-to-Analog Converter) operations with automatic channel mapping.

#### ADC Channel Mapping

Each ESP32 variant has different GPIO-to-ADC channel mappings. The adapter uses lookup tables to convert GPIO numbers to ADC channels:

```mermaid
graph TB
    subgraph "ADC Read Flow"
        GPIO["GPIO Pin Number"]
        LUT["gpio_to_adc_table[]<br/>adapter_gpio.cpp:148-294<br/>Chip-specific mapping"]
        Channel["ADC Channel<br/>0-9: ADC1<br/>10-19: ADC2"]
        API["ADC API Selection"]
    end
    
    subgraph "ESP-IDF 4.x (Legacy)"
        ADC1_V1["adc1_get_raw()<br/>adc1_config_channel_atten()"]
        ADC2_V1["adc2_get_raw()"]
    end
    
    subgraph "ESP-IDF 5.x+ (Oneshot)"
        Oneshot["adc_oneshot_new_unit()<br/>adc_oneshot_config_channel()<br/>adc_oneshot_read()"]
    end
    
    GPIO --> LUT
    LUT --> Channel
    Channel --> API
    API --> ADC1_V1
    API --> ADC2_V1
    API --> Oneshot
```

Example ADC mappings for ESP32:
- GPIO 36-39: ADC1 channels 0-3
- GPIO 32-35: ADC1 channels 4-7
- GPIO 0, 2, 4, 12-15, 25-27: ADC2 channels

The `read_analog()` implementation at [src/m5_unit_component/adapter_gpio.cpp:391-461]() handles both ESP-IDF 4.x and 5.x APIs.

#### DAC Output

DAC is only supported on GPIO 25 and 26 (ESP32 only). The `write_analog()` function at [src/m5_unit_component/adapter_gpio.cpp:373-389]() outputs an 8-bit value (0-255).

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:148-294](), [src/m5_unit_component/adapter_gpio.cpp:298-305](), [src/m5_unit_component/adapter_gpio.cpp:391-461](), [src/m5_unit_component/adapter_gpio.cpp:373-389]()

### Pulse Timing

The `pulse_in()` function at [src/m5_unit_component/adapter_gpio.cpp:463-499]() measures pulse duration using `esp_timer_get_time()` for microsecond precision:

1. Wait for any previous pulse to end
2. Wait for the pulse to start (specified state)
3. Measure time until pulse ends
4. Return duration in microseconds

This is useful for sensors like ultrasonic distance sensors that communicate via pulse width.

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:463-499]()

## RMT Peripheral

The RMT (Remote Control) peripheral enables precise transmission and reception of pulse-coded signals, commonly used for protocols like WS2812 (NeoPixel), infrared remotes, and RF433.

### RMT Item Structures

The basic unit of RMT data differs between versions:

| Version | Type | Members |
|---------|------|---------|
| RMT v1 | `rmt_item32_t` | `duration0`, `level0`, `duration1`, `level1` |
| RMT v2 | `rmt_symbol_word_t` | `duration0`, `level0`, `duration1`, `level1` |

Both represent two pulse edges in a single 32-bit word. The type alias `m5::unit::gpio::m5_rmt_item_t` at [src/m5_unit_component/types.hpp:113-117]() automatically selects the correct type.

**Sources:** [src/m5_unit_component/types.hpp:113-117]()

## Configuration

The `gpio::adapter_config_t` structure at [src/m5_unit_component/types.hpp:80-110]() provides unified configuration for both RMT versions.

### Configuration Structure

```mermaid
graph TB
    subgraph "adapter_config_t"
        Mode["mode: gpio::Mode<br/>RmtRX, RmtTX, RmtRXTX"]
        RXConfig["rx: rx_config_t"]
        TXConfig["tx: tx_config_t"]
    end
    
    subgraph "Common config_t Members"
        TickNS["tick_ns: uint32_t<br/>RMT resolution"]
        GPIO["gpio_num: gpio_num_t<br/>Pin assignment"]
        MemBlocks["mem_blocks: uint8_t<br/>Buffer size"]
        Invert["invert_signal: bool<br/>Logic inversion"]
        DMA["with_dma: bool<br/>(v2 only)"]
    end
    
    subgraph "TX-Specific"
        LoopCount["loop_count: uint16_t"]
        IdleOutput["idle_output_enabled: bool"]
        IdleLevel["idle_level_high: bool"]
        LoopEn["loop_enabled: bool"]
    end
    
    subgraph "RX-Specific"
        RingBuffer["ring_buffer_size: uint16_t<br/>(v1 only)"]
        FilterTicks["filter_ticks_threshold: uint16_t"]
        IdleTicks["idle_ticks_threshold: uint16_t"]
        FilterEn["filter_enabled: bool"]
    end
    
    Mode --> RXConfig
    Mode --> TXConfig
    RXConfig --> TickNS
    RXConfig --> GPIO
    RXConfig --> MemBlocks
    TXConfig --> TickNS
    TXConfig --> GPIO
    TXConfig --> MemBlocks
    
    TXConfig --> LoopCount
    TXConfig --> IdleOutput
    TXConfig --> IdleLevel
    TXConfig --> LoopEn
    
    RXConfig --> RingBuffer
    RXConfig --> FilterTicks
    RXConfig --> IdleTicks
    RXConfig --> FilterEn
```

### Timing Resolution Calculation

The adapter provides helper functions to calculate timing parameters:

**For RMT v1** ([src/m5_unit_component/adapter_gpio.cpp:324-333]()):
```cpp
uint8_t calculate_rmt_clk_div(uint32_t apb_freq_hz, uint32_t tick_ns)
```
Calculates the clock divider (1-255) that produces the desired tick duration.

**For RMT v2** ([src/m5_unit_component/adapter_gpio.cpp:335-345]()):
```cpp
uint32_t calculate_rmt_resolution_hz(uint32_t apb_freq_hz, uint32_t tick_ns)
```
Calculates the resolution frequency that produces the desired tick duration.

**Sources:** [src/m5_unit_component/types.hpp:80-110](), [src/m5_unit_component/adapter_gpio.cpp:324-345]()

## RMT v1 Implementation (ESP-IDF 4.x)

### Channel Management

RMT v1 uses static channel allocation tracked by a bitmap at [src/m5_unit_component/adapter_gpio_v1.cpp:21-47]():

```mermaid
graph LR
    subgraph "Channel Allocation"
        Bitmap["using_rmt_channel_bits<br/>static uint32_t<br/>Tracks used channels"]
        Retrieve["retrieve_available_rmt_channel()<br/>Finds free channel"]
        Declare["declrare_use_rmt_channel()<br/>Marks channel as used"]
        Clear["clear_use_rmt_channel()<br/>Releases channel"]
    end
    
    Retrieve --> Bitmap
    Declare --> Bitmap
    Clear --> Bitmap
```

Some ESP32 variants have channel restrictions:
- **ESP32S3**: RX channels 4-7 only
- **ESP32C6**: RX channels 2-3 only
- **ESP32**: Any channel 0-7 for RX/TX

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:21-47](), [src/m5_unit_component/adapter_gpio_v1.cpp:178-184]()

### Initialization Flow

```mermaid
sequenceDiagram
    participant User
    participant GPIOImplV1
    participant ESP_IDF as ESP-IDF RMT Driver
    
    User->>GPIOImplV1: begin(adapter_config_t)
    
    alt TX Mode
        GPIOImplV1->>GPIOImplV1: retrieve_available_rmt_channel()
        GPIOImplV1->>GPIOImplV1: to_rmt_config_tx()
        GPIOImplV1->>ESP_IDF: rmt_config()
        GPIOImplV1->>ESP_IDF: rmt_driver_install()
        Note over GPIOImplV1,ESP_IDF: Optional: gpio_matrix_out() for invert
        GPIOImplV1->>GPIOImplV1: declrare_use_rmt_channel()
    end
    
    alt RX Mode
        GPIOImplV1->>GPIOImplV1: retrieve_available_rmt_channel(first)
        GPIOImplV1->>GPIOImplV1: to_rmt_config_rx()
        GPIOImplV1->>ESP_IDF: rmt_config()
        GPIOImplV1->>ESP_IDF: rmt_driver_install(ring_buffer_size)
        Note over GPIOImplV1,ESP_IDF: Optional: gpio_matrix_in() for invert
        GPIOImplV1->>ESP_IDF: rmt_rx_start(channel, true)
        GPIOImplV1->>ESP_IDF: xRingbufferReceive() discard garbage
    end
```

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:138-233]()

### TX/RX Operations

**Transmit** ([src/m5_unit_component/adapter_gpio_v1.cpp:235-258]()):
- Uses `rmt_write_items()` to send `rmt_item32_t` array
- Optionally calls `rmt_wait_tx_done()` if `waitMs` is specified

**Receive** ([src/m5_unit_component/adapter_gpio_v1.cpp:260-293]()):
- Uses `rmt_get_ringbuf_handle()` to access FreeRTOS ring buffer
- Calls `xRingbufferReceive()` with 50ms timeout
- Returns received length in first 2 bytes, followed by `rmt_item32_t` data

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:235-293]()

## RMT v2 Implementation (ESP-IDF 5.x+)

### Architecture

RMT v2 uses a handle-based API with separate TX and RX channel types:

```mermaid
graph TB
    subgraph "RMT v2 Components"
        TXHandle["rmt_channel_handle_t _tx_handle<br/>Transmit channel"]
        RXHandle["rmt_channel_handle_t _rx_handle<br/>Receive channel"]
        Encoder["rmt_encoder_handle_t copy_encoder<br/>Shared copy encoder"]
    end
    
    subgraph "Configuration"
        TXConfig["rmt_tx_channel_config_t<br/>resolution_hz, mem_block_symbols,<br/>with_dma, invert_out"]
        RXConfig["rmt_rx_channel_config_t<br/>resolution_hz, mem_block_symbols,<br/>with_dma, invert_in"]
        TransmitConfig["rmt_transmit_config_t<br/>loop_count, eot_level"]
        ReceiveConfig["rmt_receive_config_t<br/>signal_range_min/max_ns"]
    end
    
    subgraph "Memory Management"
        DMABuffer["DMA-capable buffer<br/>heap_caps_malloc(MALLOC_CAP_DMA)"]
        Semaphore["SemaphoreHandle_t _sem<br/>Protects RX buffer"]
    end
    
    TXHandle --> TXConfig
    RXHandle --> RXConfig
    TXHandle --> Encoder
    RXHandle --> DMABuffer
    RXHandle --> Semaphore
```

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:179-196]()

### Initialization Flow

```mermaid
sequenceDiagram
    participant User
    participant GPIOImplV2
    participant ESP_IDF as ESP-IDF RMT v2 API
    
    User->>GPIOImplV2: begin(adapter_config_t)
    
    alt TX Mode
        GPIOImplV2->>GPIOImplV2: to_rmt_tx_config()
        GPIOImplV2->>ESP_IDF: rmt_new_tx_channel()
        GPIOImplV2->>ESP_IDF: rmt_enable(_tx_handle)
        GPIOImplV2->>GPIOImplV2: to_rmt_transmit_config()
    end
    
    alt RX Mode
        GPIOImplV2->>GPIOImplV2: createReceiveTask()
        GPIOImplV2->>GPIOImplV2: heap_caps_malloc(DMA buffer)
        GPIOImplV2->>GPIOImplV2: to_rmt_rx_config()
        GPIOImplV2->>ESP_IDF: rmt_new_rx_channel()
        GPIOImplV2->>ESP_IDF: rmt_rx_register_event_callbacks(callbackReceive)
        Note over GPIOImplV2: GPIO reset sequence for StampS3
        GPIOImplV2->>ESP_IDF: rmt_enable(_rx_handle)
        GPIOImplV2->>GPIOImplV2: to_rmt_receive_config()
        GPIOImplV2->>ESP_IDF: rmt_receive() kick start
    end
    
    GPIOImplV2->>ESP_IDF: rmt_new_copy_encoder()
```

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:198-298]()

### Asynchronous RX with Callbacks

RMT v2 uses an interrupt-driven callback system:

```mermaid
graph TB
    subgraph "RX Reception Flow"
        ISR["callbackReceive()<br/>ISR callback<br/>adapter_gpio_v2.cpp:395-404"]
        Queue["_receive_queue<br/>FreeRTOS queue<br/>Static member"]
        Task["receive_loop_task()<br/>FreeRTOS task<br/>PRO_CPU_NUM"]
        Loop["receive_loop()<br/>Re-arm rmt_receive()"]
    end
    
    subgraph "Data Protection"
        Sem["SemaphoreHandle_t _sem<br/>Mutex for buffer access"]
        Buffer["_rx_buf<br/>DMA-capable buffer<br/>_receive_len<br/>volatile uint16_t"]
    end
    
    ISR -->|xQueueSendFromISR| Queue
    Queue -->|xQueueReceive| Task
    Task --> Loop
    Loop -->|Take| Sem
    Loop --> Buffer
    Loop -->|Give| Sem
    Loop -->|rmt_receive| ISR
```

1. `callbackReceive()` ISR is triggered when RX completes
2. ISR posts to `_receive_queue` with received length
3. Static task `receive_loop_task()` wakes up
4. Takes semaphore, updates `_receive_len`, re-arms `rmt_receive()`
5. `readWithTransaction()` reads from buffer under semaphore protection

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:353-404](), [src/m5_unit_component/adapter_gpio_v2.cpp:377-393]()

### TX/RX Operations

**Transmit** ([src/m5_unit_component/adapter_gpio_v2.cpp:300-321]()):
- Uses `rmt_transmit()` with copy encoder
- Data is `rmt_symbol_word_t` array
- Optionally calls `rmt_tx_wait_all_done()` if `waitMs` is specified

**Receive** ([src/m5_unit_component/adapter_gpio_v2.cpp:323-351]()):
- Takes semaphore to protect buffer access
- Copies `_receive_len` bytes from `_rx_buf` to user buffer
- Returns received length in first 2 bytes, followed by `rmt_symbol_word_t` data

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:300-351]()

## Device Compatibility

The following table summarizes RMT version compatibility across M5Stack devices (from [src/m5_unit_component/adapter_gpio_v2.cpp:422-443]()):

| Device | RMT v1 | RMT v2 |
|--------|--------|--------|
| Core | OK | OK |
| Core2 | OK | OK |
| CoreS3 | OK | OK |
| Dial | OK | OK |
| AtomS3 | OK | OK |
| AtomS3R | OK | OK |
| StickCPlus | OK | OK |
| StickCPlus2 | OK | OK |
| StampS3 | OK | OK |
| NanoC6 | — | OK |
| DinMeter | OK | OK |
| CoreINK | OK | OK |
| Paper | OK | OK |
| Fire | OK | OK |
| AtomMatrix | OK | OK |

NanoC6 only supports RMT v2 as it uses ESP32-C6 with ESP-IDF 5.x.

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:422-446]()

## Usage Example

Typical usage pattern for GPIO adapter with RMT:

```cpp
// Create adapter with RX and TX pins
AdapterGPIO adapter(rx_pin, tx_pin);

// Configure for RMT TX
gpio::adapter_config_t cfg{};
cfg.mode = gpio::Mode::RmtTX;
cfg.tx.tick_ns = 1000;  // 1 microsecond ticks
cfg.tx.mem_blocks = 1;
cfg.tx.idle_output_enabled = true;
cfg.tx.idle_level_high = false;

// Initialize
adapter.begin(cfg);

// Transmit RMT items
gpio::m5_rmt_item_t items[10];
// ... populate items ...
adapter.writeWithTransaction((uint8_t*)items, sizeof(items), 100);
```

**Sources:** [src/m5_unit_component/adapter_gpio.hpp:154-157](), [src/m5_unit_component/types.hpp:80-110]()