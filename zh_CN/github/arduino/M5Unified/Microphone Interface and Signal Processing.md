M5Unified Microphone Interface and Signal Processing

# Microphone Interface and Signal Processing

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Advanced/Mic_FFT/Mic_FFT.ino](examples/Advanced/Mic_FFT/Mic_FFT.ino)
- [src/utility/Mic_Class.cpp](src/utility/Mic_Class.cpp)
- [src/utility/Mic_Class.hpp](src/utility/Mic_Class.hpp)
- [src/utility/Speaker_Class.cpp](src/utility/Speaker_Class.cpp)
- [src/utility/Speaker_Class.hpp](src/utility/Speaker_Class.hpp)

</details>



## Purpose and Scope

This document covers the `Mic_Class` implementation in M5Unified, which provides audio input functionality through I2S and ADC interfaces. The microphone system captures audio data in a background FreeRTOS task, applies signal processing (oversampling, noise filtering, zero-level adjustment), and delivers processed samples to user applications through a double-buffered recording mechanism.

For general audio architecture and I2S configuration details, see [I2S Configuration and Driver Abstraction](#4.1). For board-specific audio codec initialization and microphone hardware differences, see [Board-Specific Audio Configuration](#4.4).

---

## Mic_Class Architecture

The `Mic_Class` provides a non-blocking audio capture interface that runs in a dedicated FreeRTOS task. The architecture separates user-facing recording requests from low-level I2S/ADC data acquisition and signal processing.

### Class Structure

```mermaid
classDiagram
    class Mic_Class {
        -mic_config_t _cfg
        -recording_info_t _rec_info[2]
        -bool _rec_flip
        -TaskHandle_t _task_handle
        -SemaphoreHandle_t _task_semaphore
        -int32_t _offset
        -bool _task_running
        -bool _is_recording
        +begin() bool
        +end() void
        +record() bool
        +isRecording() size_t
        +config() mic_config_t
        -mic_task() void
        -_setup_i2s() esp_err_t
        -_rec_raw() bool
        -_calc_rec_rate() uint32_t
    }

    class mic_config_t {
        +int pin_data_in
        +int pin_bck
        +int pin_ws
        +int pin_mck
        +uint32_t sample_rate
        +bool stereo
        +bool left_channel
        +uint8_t over_sampling
        +uint8_t magnification
        +uint8_t noise_filter_level
        +bool use_adc
        +size_t dma_buf_len
        +size_t dma_buf_count
        +i2s_port_t i2s_port
    }

    class recording_info_t {
        +void* data
        +size_t length
        +size_t index
        +bool is_stereo
        +bool is_16bit
    }

    Mic_Class --> mic_config_t
    Mic_Class --> recording_info_t
```

**Sources:** [src/utility/Mic_Class.hpp:98-196](), [src/utility/Mic_Class.hpp:42-96](), [src/utility/Mic_Class.hpp:163-170]()

---

## Configuration System

The `mic_config_t` structure defines all microphone parameters including I2S pins, sampling rate, signal processing parameters, and hardware mode selection.

### Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `pin_data_in` | int | -1 | I2S data input pin or ADC GPIO pin |
| `pin_bck` | int | -1 | I2S bit clock pin (ignored for PDM/ADC) |
| `pin_ws` | int | -1 | I2S word select pin (or PDM clock) |
| `pin_mck` | int | -1 | I2S master clock pin (optional) |
| `sample_rate` | uint32_t | 16000 | Output sampling rate in Hz |
| `stereo` | bool | false | Stereo input capture |
| `left_channel` | bool | false | Select left channel (when mono) |
| `over_sampling` | uint8_t | 2 | Oversampling factor (1-8) |
| `magnification` | uint8_t | 16 | Output amplitude multiplier |
| `noise_filter_level` | uint8_t | 0 | Low-pass filter strength (0-255) |
| `use_adc` | bool | false | Use ADC instead of I2S (ESP32 only) |
| `dma_buf_len` | size_t | 128 | I2S DMA buffer length |
| `dma_buf_count` | size_t | 8 | Number of DMA buffers |
| `i2s_port` | i2s_port_t | I2S_NUM_0 | I2S peripheral selection |

**Sources:** [src/utility/Mic_Class.hpp:42-96]()

### Hardware Mode Selection

The microphone system supports three hardware input modes determined by pin configuration:

```mermaid
flowchart TD
    Start["Mic_Class::_setup_i2s()"]
    CheckADC{"use_adc == true?"}
    CheckPDM{"pin_bck < 0?"}
    I2SStd["I2S Standard Mode"]
    I2SPDM["I2S PDM Mode"]
    ADCMode["ADC Mode"]
    
    Start --> CheckADC
    CheckADC -->|Yes| ADCMode
    CheckADC -->|No| CheckPDM
    CheckPDM -->|Yes| I2SPDM
    CheckPDM -->|No| I2SStd
    
    I2SStd --> ConfigStd["Configure i2s_std_config_t<br/>BCLK, WS, DIN pins<br/>Standard I2S format"]
    I2SPDM --> ConfigPDM["Configure i2s_pdm_rx_config_t<br/>CLK, DIN pins<br/>PDM downsampling DSR=64"]
    ADCMode --> ConfigADC["Configure ADC registers<br/>12-bit resolution<br/>_i2s_set_adc()"]
    
    ConfigStd --> Init["i2s_channel_init_std_mode()"]
    ConfigPDM --> Init["i2s_channel_init_pdm_rx_mode()"]
    ConfigADC --> Init["ADC DMA configuration"]
```

**Sources:** [src/utility/Mic_Class.cpp:298-417]()

---

## Recording Data Flow

The microphone system uses a producer-consumer pattern with double buffering. The `mic_task` continuously fills recording buffers while user code reads completed buffers asynchronously.

### Double-Buffer Mechanism

```mermaid
sequenceDiagram
    participant App as "Application"
    participant MicClass as "Mic_Class"
    participant Task as "mic_task"
    participant I2S as "I2S Hardware"
    
    App->>MicClass: record(buffer1, length)
    MicClass->>MicClass: _rec_info[_rec_flip] = buffer1
    MicClass->>Task: xTaskNotifyGive()
    activate Task
    
    Task->>Task: _is_recording = true
    Task->>I2S: _i2s_read(src_buf)
    I2S-->>Task: Raw samples
    
    loop Process samples
        Task->>Task: Oversample accumulation
        Task->>Task: Zero-level adjustment
        Task->>Task: Noise filtering
        Task->>Task: Write to buffer1
    end
    
    Task->>Task: buffer1 complete, flip = !flip
    Task->>MicClass: xSemaphoreGive()
    deactivate Task
    
    App->>MicClass: record(buffer2, length)
    Note over App,Task: buffer2 queued while<br/>buffer1 still being read
    
    MicClass->>MicClass: _rec_info[!_rec_flip] = buffer2
    
    Task->>Task: Switch to buffer2
    Note over Task: Continue processing<br/>without blocking
```

**Sources:** [src/utility/Mic_Class.cpp:422-706](), [src/utility/Mic_Class.cpp:567-699]()

### Recording Buffer States

The `recording_info_t` structures maintain the state of each buffer in the double-buffer system:

```mermaid
stateDiagram-v2
    [*] --> Empty: length = 0
    Empty --> Filling: user calls record()
    Filling --> Filling: mic_task writes samples
    Filling --> Complete: length reaches 0
    Complete --> Empty: buffer flipped
    Complete --> Filling: new record() queued
    
    note right of Empty
        Buffer available for
        new record() request
    end note
    
    note right of Filling
        mic_task writing samples
        length decrements
    end note
    
    note right of Complete
        Buffer ready, waiting
        for user to queue next
    end note
```

**Sources:** [src/utility/Mic_Class.cpp:567-591]()

---

## Signal Processing Pipeline

The `mic_task` applies a multi-stage signal processing pipeline to raw I2S/ADC samples before delivering them to the user buffer. This pipeline improves signal quality and removes DC offset.

### Processing Stages Diagram

```mermaid
flowchart LR
    subgraph "I2S/ADC Input"
        I2S["I2S DMA Buffer<br/>dma_buf_len samples<br/>int16_t raw data"]
    end
    
    subgraph "Oversampling"
        Accumulate["Accumulate Samples<br/>sum_value[0] += src[i]<br/>sum_value[1] += src[i+1]<br/>over_sampling iterations"]
    end
    
    subgraph "Zero-Level Adjustment"
        DCRemoval["Automatic DC Offset<br/>offset -= (sum + offset) >> 5<br/>Gradual convergence to zero"]
    end
    
    subgraph "Noise Filtering"
        LowPass["IIR Low-Pass Filter<br/>v = sum*(256-level) + prev*level<br/>prev_value[i] = v"]
    end
    
    subgraph "Gain & Clipping"
        Gain["Apply Magnification<br/>v = sum * f_gain<br/>f_gain = magnification / (os << 1)"]
        Clip["Clamp to Range<br/>8-bit: 0-255<br/>16-bit: INT16_MIN-INT16_MAX"]
    end
    
    subgraph "Output"
        Convert["Stereo/Mono Convert<br/>Write to user buffer<br/>int16_t or uint8_t"]
    end
    
    I2S --> Accumulate
    Accumulate --> DCRemoval
    DCRemoval --> LowPass
    LowPass --> Gain
    Gain --> Clip
    Clip --> Convert
```

**Sources:** [src/utility/Mic_Class.cpp:594-699]()

### Oversampling Implementation

Oversampling reduces quantization noise by capturing samples at a higher rate and averaging them down to the target sample rate. The `over_sampling` parameter controls how many hardware samples are accumulated per output sample.

```cpp
// From mic_task processing loop
do
{
    sum_value[0] += src_buf[src_idx  ];
    sum_value[1] += src_buf[src_idx+1];
    src_idx += 2;
} while (--os_remain && (src_idx < src_len));
```

The effective recording rate is `sample_rate * over_sampling`, calculated by `_calc_rec_rate()`:

**Sources:** [src/utility/Mic_Class.cpp:603-608](), [src/utility/Mic_Class.cpp:84-88]()

### Zero-Level Adjustment

The automatic zero-level adjustment removes DC offset using a first-order IIR filter that gradually converges the signal baseline to zero:

```cpp
auto value_tmp = (sv0 + sv1) << 3;
int32_t offset = self->_offset;
// Automatic zero level adjustment
offset -= (value_tmp + offset + 16) >> 5;
self->_offset = offset;
offset = (offset + 8) >> 4;
sum_value[0] = sv0 + offset;
sum_value[1] = sv1 + offset;
```

This implements: `offset = offset - (signal + offset) / 32`, providing a time constant of approximately 32 samples for DC offset removal.

**Sources:** [src/utility/Mic_Class.cpp:625-632]()

### Noise Filtering

When `noise_filter_level` is non-zero, an IIR low-pass filter smooths the signal:

```cpp
if (noise_filter)
{
    for (int i = 0; i < 2; ++i)
    {
        int32_t v = (sum_value[i] * (256 - noise_filter) + prev_value[i] * noise_filter + 128) >> 8;
        prev_value[i] = v;
        sum_value[i] = v * f_gain;
    }
}
```

The filter coefficient ranges from 0 (no filtering) to 255 (maximum smoothing). Higher values increase latency but reduce high-frequency noise.

**Sources:** [src/utility/Mic_Class.cpp:634-650]()

---

## Clock Configuration

The microphone system requires precise clock configuration to achieve the target sampling rate. The implementation uses fractional dividers to minimize sampling rate error.

### Clock Divider Calculation

```mermaid
flowchart TD
    Start["calcClockDiv()"]
    BaseClock["PLL_D2_CLK<br/>ESP32: 80MHz<br/>ESP32-C3/S3: 120MHz<br/>ESP32-P4: 20MHz"]
    
    PDMCheck{"PDM mode?"}
    BitCalc["bits = 64 (PDM DSR)<br/>div_m = 2"]
    I2SCalc["bits = 16<br/>div_m = 8"]
    
    DivCalc["calcClockDiv(&div_a, &div_b, &div_n,<br/>PLL_D2_CLK / (bits * div_m),<br/>sample_rate * oversampling)"]
    
    RegConfig["Configure I2S registers:<br/>div_x = div_a / div_b - 1<br/>div_y = div_a % div_b<br/>div_z = div_b<br/>div_num = div_n"]
    
    Start --> BaseClock
    BaseClock --> PDMCheck
    PDMCheck -->|Yes| BitCalc
    PDMCheck -->|No| I2SCalc
    BitCalc --> DivCalc
    I2SCalc --> DivCalc
    DivCalc --> RegConfig
```

The actual sampling rate is: `rate = PLL_D2_CLK / (div_m * bits * (div_n + div_b/div_a))`

For PDM mode, the hardware downsamples by DSR=64, so the I2S clock runs at `sample_rate * oversampling * 64`.

**Sources:** [src/utility/Mic_Class.cpp:431-547](), [src/utility/Mic_Class.cpp:419-420]()

---

## Task Lifecycle Management

The `mic_task` runs as a FreeRTOS task with configurable priority and core affinity. The task lifecycle is managed through flags and semaphores to coordinate with user operations.

### Task State Machine

```mermaid
stateDiagram-v2
    [*] --> Stopped: Initial state
    Stopped --> Starting: begin() called
    Starting --> Idle: Task created<br/>_task_running = true
    Idle --> Recording: record() called<br/>xTaskNotifyGive()
    Recording --> Recording: Processing samples
    Recording --> Idle: Both buffers empty<br/>ulTaskNotifyTake()
    Idle --> Stopping: end() called<br/>_task_running = false
    Stopping --> Stopped: Task self-deletes
    Recording --> Stopping: end() called
    
    note right of Idle
        Task waits for notification
        _is_recording = false
    end note
    
    note right of Recording
        Continuously reads I2S
        Processes and fills buffers
        _is_recording = true
    end note
```

**Sources:** [src/utility/Mic_Class.cpp:708-759]()

### Initialization Sequence

```cpp
bool Mic_Class::begin(void)
{
    // Check if already running at same rate
    if (_task_running) {
        auto rate = _calc_rec_rate();
        if (_rec_sample_rate == rate) { return true; }
        
        // Rate changed - restart
        do { vTaskDelay(1); } while (isRecording());
        end();
        _rec_sample_rate = rate;
    }
    
    // Create semaphore for buffer synchronization
    if (_task_semaphore == nullptr) { 
        _task_semaphore = xSemaphoreCreateBinary(); 
    }
    
    // Enable callback (board-specific power control)
    if (_cb_set_enabled) { 
        res = _cb_set_enabled(_cb_set_enabled_args, true); 
    }
    
    // Setup I2S/ADC hardware
    res = (ESP_OK == _setup_i2s()) && res;
    
    // Create background task
    _task_running = true;
    xTaskCreatePinnedToCore(mic_task, "mic_task", stack_size, 
                           this, _cfg.task_priority, 
                           &_task_handle, _cfg.task_pinned_core);
}
```

**Sources:** [src/utility/Mic_Class.cpp:708-745]()

---

## Mono/Stereo Conversion

The signal processing pipeline automatically converts between mono and stereo formats based on the input configuration and output buffer format.

### Conversion Logic

| Input Mode | Output Mode | Operation |
|------------|-------------|-----------|
| Stereo | Stereo | Direct copy, both channels processed |
| Stereo | Mono | Average: `(left + right) / 2` |
| Mono | Mono | Direct copy of single channel |
| Mono | Stereo | Duplicate: `left = right = mono` |

```cpp
if (in_stereo != current_rec->is_stereo)
{
    if (in_stereo)
    { // stereo -> mono convert
        sum_value[0] = (sum_value[0] + sum_value[1] + 1) >> 1;
        output_num = 1;
    }
    else
    { // mono -> stereo convert
        auto tmp = sum_value[1];
        sum_value[3] = tmp;
        sum_value[2] = tmp;
        sum_value[1] = sum_value[0];
        output_num = 4;
    }
}
```

**Sources:** [src/utility/Mic_Class.cpp:652-669]()

---

## ADC Mode Implementation

On ESP32 (not ESP32-S2/S3/C3), the microphone can use the internal ADC for analog input instead of I2S. This mode is enabled by setting `use_adc = true` and specifying an ADC-capable GPIO pin.

### ADC Configuration Process

```mermaid
flowchart TD
    Start["_i2s_set_adc()"]
    CheckPin{"pin_data_in valid?<br/>GPIO 0,2,4,12-15,25-27,32-39"}
    MapChannel["Map GPIO to ADC channel<br/>ADC1_CHANNEL_X or<br/>ADC2_CHANNEL_X"]
    
    SelectUnit{"GPIO >= 32?"}
    Unit1["ADC_UNIT_1"]
    Unit2["ADC_UNIT_2"]
    
    ConfigADC["adc_oneshot_ll_set_output_bits(12bit)<br/>Configure FSM timings<br/>Set sample cycle, clock div"]
    
    PatternTable["Configure pattern table<br/>atten = ADC_ATTEN_DB_12<br/>bit_width = 3 (12-bit)<br/>channel = adc_ch"]
    
    I2SRegs["Configure I2S registers:<br/>I2S0.conf2.lcd_en = true<br/>I2S0.fifo_conf.rx_fifo_mod = true<br/>ADC data via I2S DMA"]
    
    Start --> CheckPin
    CheckPin -->|Valid| MapChannel
    CheckPin -->|Invalid| Fail["Return ESP_FAIL"]
    MapChannel --> SelectUnit
    SelectUnit -->|Yes| Unit1
    SelectUnit -->|No| Unit2
    Unit1 --> ConfigADC
    Unit2 --> ConfigADC
    ConfigADC --> PatternTable
    PatternTable --> I2SRegs
```

**Sources:** [src/utility/Mic_Class.cpp:134-219](), [src/utility/Mic_Class.cpp:239-293]()

### ADC Data Processing

ADC samples are unsigned 12-bit values (0-4095) that must be converted to signed format:

```cpp
if (self->_cfg.use_adc) {
    sv0 -= 2048 * oversampling;  // Remove 2048 center offset
    sv1 -= 2048 * oversampling;
}
```

The ADC zero-point is 2048 (half of 4096), so this conversion centers the signal around zero for proper signal processing.

**Sources:** [src/utility/Mic_Class.cpp:620-623]()

---

## Usage Example

The following example from the Mic_FFT demonstration shows typical microphone usage with continuous recording and FFT analysis:

```cpp
// Configure microphone
auto cfg = M5.Mic.config();
cfg.dma_buf_count = 3;
cfg.dma_buf_len = 256;        // WAVE_BLOCK_SIZE
cfg.over_sampling = 1;
cfg.noise_filter_level = 0;
cfg.sample_rate = 24000;      // SAMPLE_RATE
cfg.magnification = cfg.use_adc ? 16 : 1;
M5.Mic.config(cfg);

// Start microphone
M5.Mic.begin();

// In loop: continuous recording
int wav_idx = wav_data.latest_index;
while (M5.Mic.isRecording() < 2) {
    // Queue next block while previous is processing
    M5.Mic.record(&(wav_data.wav[wav_idx]), 
                  WAVE_BLOCK_SIZE, 
                  SAMPLE_RATE, 
                  false);  // mono
    
    wav_idx += WAVE_BLOCK_SIZE;
    if (wav_idx >= WAVE_TOTAL_SIZE) { wav_idx = 0; }
    wav_data.latest_index = wav_idx;
}
```

This pattern maintains a continuous circular buffer by queuing new recording requests before the previous one completes, ensuring no gaps in audio capture.

**Sources:** [examples/Advanced/Mic_FFT/Mic_FFT.ino:662-741]()

---

## Performance Considerations

### Buffer Sizing

The `dma_buf_len` and `dma_buf_count` parameters affect latency and reliability:

- **Small buffers** (dma_buf_len < 128): Lower latency but higher risk of buffer underrun
- **Large buffers** (dma_buf_len > 512): Higher latency but more robust under CPU load
- **Buffer count** (dma_buf_count): Typically 3-8 buffers provide good balance

### Task Priority

The `task_priority` should be set high enough to prevent I2S buffer underruns:

- Default priority: 2
- Higher priority (3-4) recommended for high sample rates (>48kHz)
- Must be balanced against other real-time tasks

### Stack Size Calculation

The task stack size is calculated dynamically:

```cpp
size_t stack_size = 2048 + (_cfg.dma_buf_len * sizeof(uint16_t));
```

This provides base overhead plus space for the intermediate buffer allocation.

**Sources:** [src/utility/Mic_Class.cpp:730]()

---

## API Reference Summary

| Method | Description |
|--------|-------------|
| `begin()` | Initialize I2S/ADC and start mic_task |
| `end()` | Stop mic_task and release resources |
| `record(uint8_t*, size_t)` | Queue 8-bit mono recording |
| `record(int16_t*, size_t)` | Queue 16-bit mono recording |
| `record(buffer, len, rate, stereo)` | Queue recording with full parameters |
| `isRecording()` | Returns 0/1/2 for idle/recording/queue-full |
| `isEnabled()` | Check if pin_data_in is configured |
| `config()` | Get current mic_config_t |
| `config(cfg)` | Set new mic_config_t |

**Sources:** [src/utility/Mic_Class.hpp:107-157]()