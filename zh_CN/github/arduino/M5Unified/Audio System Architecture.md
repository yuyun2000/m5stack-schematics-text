M5Unified Audio System Architecture

# Audio System Architecture

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Advanced/Mic_FFT/Mic_FFT.ino](examples/Advanced/Mic_FFT/Mic_FFT.ino)
- [src/utility/Mic_Class.cpp](src/utility/Mic_Class.cpp)
- [src/utility/Mic_Class.hpp](src/utility/Mic_Class.hpp)
- [src/utility/Speaker_Class.cpp](src/utility/Speaker_Class.cpp)
- [src/utility/Speaker_Class.hpp](src/utility/Speaker_Class.hpp)

</details>



The Audio System Architecture provides unified audio input and output capabilities across M5Stack devices through `Speaker_Class` (accessible as `M5.Speaker`) and `Mic_Class` (accessible as `M5.Mic`). The architecture abstracts hardware differences (I2S, DAC, PDM, ADC) and runs audio processing on dedicated FreeRTOS tasks (`spk_task`, `mic_task`) with I2S DMA for non-blocking operation.

## Architecture Overview

**Audio System Component Architecture**
```mermaid
graph TB
    subgraph "Application Layer"
        App["Application Code"]
    end
    
    subgraph "M5Unified Audio API"
        Speaker["Speaker_Class<br/>M5.Speaker<br/>playRaw/playWav/tone"]
        Mic["Mic_Class<br/>M5.Mic<br/>record"]
    end
    
    subgraph "FreeRTOS Task Layer"
        SpkTask["spk_task<br/>TaskHandle_t _task_handle<br/>Priority: _cfg.task_priority"]
        MicTask["mic_task<br/>TaskHandle_t _task_handle<br/>Priority: _cfg.task_priority"]
        SpkSem["SemaphoreHandle_t<br/>_task_semaphore"]
        MicSem["SemaphoreHandle_t<br/>_task_semaphore"]
    end
    
    subgraph "Channel Mixing"
        Channels["channel_info_t _ch_info[8]<br/>wav_info_t wavinfo[2]<br/>flip buffering"]
        PlayBits["atomic<uint16_t><br/>_play_channel_bits"]
        Mixer["spk_task mixing loop<br/>for ch=0 to 8<br/>sound_buf32[]"]
    end
    
    subgraph "Audio Processing"
        SpkProc["Format Conversion<br/>_cfg.use_dac ? DAC : I2S<br/>Volume: _master_volume<br/>magnification"]
        MicProc["recording_info_t _rec_info[2]<br/>_rec_flip<br/>over_sampling<br/>noise_filter_level<br/>_offset auto-adjust"]
    end
    
    subgraph "I2S Driver Abstraction"
        I2SSetupSpk["_setup_i2s<br/>speaker_config_t _cfg"]
        I2SSetupMic["_setup_i2s<br/>mic_config_t _cfg"]
        I2STX["_i2s_write<br/>i2s_channel_write<br/>or i2s_write"]
        I2SRX["_i2s_read<br/>i2s_channel_read<br/>or i2s_read"]
    end
    
    subgraph "Hardware Control"
        Callback["_cb_set_enabled<br/>board-specific enable"]
        ClockDiv["calcClockDiv<br/>PLL_D2_CLK<br/>div_n, div_a, div_b"]
        DACSet["_i2s_set_dac<br/>dac_ll_power_on<br/>I2S0.conf2.lcd_en"]
        ADCSet["_i2s_set_adc<br/>adc_ll_digi_*<br/>I2S0.fifo_conf"]
    end
    
    subgraph "Hardware"
        HW["Audio Codecs<br/>ESP32 DAC/ADC<br/>Buzzer GPIO"]
    end
    
    App --> Speaker
    App --> Mic
    Speaker --> SpkTask
    Mic --> MicTask
    
    SpkTask --> SpkSem
    MicTask --> MicSem
    
    SpkTask --> Channels
    SpkTask --> PlayBits
    Channels --> Mixer
    Mixer --> SpkProc
    
    MicTask --> I2SRX
    I2SRX --> MicProc
    
    Speaker --> I2SSetupSpk
    Mic --> I2SSetupMic
    SpkProc --> I2STX
    
    I2SSetupSpk --> Callback
    I2SSetupMic --> Callback
    I2SSetupSpk --> ClockDiv
    I2SSetupMic --> ClockDiv
    I2STX --> DACSet
    I2SRX --> ADCSet
    
    I2STX --> HW
    I2SRX --> HW
    DACSet --> HW
    ADCSet --> HW
```

The audio architecture consists of two parallel subsystems:

**Speaker_Class Architecture:**
- 8 virtual channels (`channel_info_t _ch_info[8]`) for concurrent playback
- Flip-buffer mechanism (`wavinfo[2]`) for queue-less continuous operation
- Atomic channel tracking (`_play_channel_bits`) for thread-safe state management
- Background task (`spk_task`) mixes all active channels into `sound_buf32[]` buffer
- Sample rate conversion with linear interpolation (`liner_buf[2][2]`)
- Multiple output modes controlled by `_cfg.use_dac` and `_cfg.buzzer`

**Mic_Class Architecture:**
- Double buffering (`recording_info_t _rec_info[2]`, `_rec_flip`) for continuous recording
- Oversampling accumulation (`over_sampling` parameter) for SNR improvement
- Automatic DC offset correction (`_offset` value)
- Noise filtering with exponential smoothing (`noise_filter_level`)
- Background task (`mic_task`) processes I2S input and fills application buffers

Both tasks communicate via FreeRTOS primitives (`xTaskNotifyGive`, `xSemaphoreGive`) to minimize CPU overhead during idle periods.

Sources:
- [src/utility/Speaker_Class.hpp:82-298]()
- [src/utility/Mic_Class.hpp:98-196]()
- [src/utility/Speaker_Class.cpp:356-910]()
- [src/utility/Mic_Class.cpp:422-706]()

## I2S DMA Architecture

The audio system uses I2S (Inter-IC Sound) with DMA (Direct Memory Access) for efficient, non-blocking audio transfer. The I2S peripheral handles the serial audio protocol while DMA automatically transfers data between memory buffers and hardware FIFOs without CPU intervention.

**ESP-IDF Driver Version Abstraction**
```mermaid
graph TB
    subgraph "Compile-Time Detection"
        HasInclude["#if __has_include<driver/i2s_std.h>"]
        IDFVer["ESP_IDF_VERSION_MAJOR"]
    end
    
    subgraph "New Driver API (ESP-IDF ≥5.0)"
        NewTypes["i2s_chan_handle_t _i2s_handle[SOC_I2S_NUM]<br/>i2s_chan_config_t chan_cfg<br/>i2s_std_config_t i2s_config"]
        NewInit["i2s_new_channel(&chan_cfg, &_i2s_handle, nullptr)<br/>i2s_channel_init_std_mode(_i2s_handle, &i2s_config)<br/>i2s_channel_init_pdm_rx_mode(_i2s_handle, &pdm_config)"]
        NewIO["_i2s_write: i2s_channel_write(_i2s_handle, buf, len, result, tick)<br/>_i2s_read: i2s_channel_read(_i2s_handle, buf, len, result, tick)<br/>_i2s_start: i2s_channel_enable(_i2s_handle)<br/>_i2s_stop: i2s_channel_disable(_i2s_handle)"]
    end
    
    subgraph "Legacy Driver API (ESP-IDF <5.0)"
        LegacyTypes["i2s_config_t i2s_config<br/>i2s_pin_config_t pin_config<br/>i2s_port_t i2s_port"]
        LegacyInit["i2s_driver_install(_cfg.i2s_port, &i2s_config, 0, nullptr)<br/>i2s_set_pin(_cfg.i2s_port, &pin_config)<br/>i2s_set_dac_mode(dac_mode)"]
        LegacyIO["_i2s_write: i2s_write(port, buf, len, result, tick)<br/>_i2s_read: i2s_read(port, buf, len, result, tick)<br/>_i2s_start: i2s_start(port)<br/>_i2s_stop: i2s_stop(port)"]
    end
    
    subgraph "Common Interface"
        SetupI2S["esp_err_t _setup_i2s()<br/>Called by begin()"]
        Wrappers["Static wrapper functions:<br/>_i2s_write<br/>_i2s_read<br/>_i2s_start<br/>_i2s_stop<br/>_i2s_driver_uninstall"]
        Tasks["spk_task / mic_task<br/>Use wrapper functions"]
    end
    
    HasInclude -->|"true"| NewTypes
    HasInclude -->|"false"| LegacyTypes
    
    NewTypes --> NewInit
    NewInit --> NewIO
    
    LegacyTypes --> LegacyInit
    LegacyInit --> LegacyIO
    
    NewIO --> Wrappers
    LegacyIO --> Wrappers
    
    SetupI2S --> NewInit
    SetupI2S --> LegacyInit
    
    Wrappers --> Tasks
```

**DMA Buffer Configuration Structure**

The I2S driver uses ping-pong buffering with configurable parameters:

| Parameter | Speaker Default | Mic Default | Purpose |
|-----------|----------------|-------------|---------|
| `dma_buf_count` | 8 | 3 | Number of DMA descriptors |
| `dma_buf_len` | 256 | 128 | Samples per buffer |
| Latency | ~42ms @ 48kHz | ~24ms @ 16kHz | `(dma_buf_len / sample_rate) × dma_buf_count` |

**New Driver Setup (ESP-IDF ≥5.0):**
```
i2s_chan_config_t chan_cfg = I2S_CHANNEL_DEFAULT_CONFIG(_cfg.i2s_port, I2S_ROLE_MASTER);
chan_cfg.dma_desc_num = _cfg.dma_buf_count;
chan_cfg.dma_frame_num = _cfg.dma_buf_len;
i2s_new_channel(&chan_cfg, &_i2s_handle[_cfg.i2s_port], nullptr);
```

**Legacy Driver Setup (ESP-IDF <5.0):**
```
i2s_config.dma_buf_count = _cfg.dma_buf_count;
i2s_config.dma_buf_len = _cfg.dma_buf_len;
i2s_driver_install(_cfg.i2s_port, &i2s_config, 0, nullptr);
```

The wrapper functions (`_i2s_write`, `_i2s_read`, etc.) at [src/utility/Speaker_Class.cpp:82-184]() and [src/utility/Mic_Class.cpp:90-296]() abstract the API differences, allowing the task code to remain version-independent.

Sources:
- [src/utility/Speaker_Class.cpp:82-184]()
- [src/utility/Mic_Class.cpp:90-296]()
- [src/utility/Speaker_Class.cpp:186-297]()
- [src/utility/Mic_Class.cpp:298-417]()
- [src/utility/Speaker_Class.hpp:66-70]()
- [src/utility/Mic_Class.hpp:82-86]()
</thinking>

## Multi-Channel Mixing Architecture

The `Speaker_Class` implements 8 virtual audio channels mixed in real-time by `spk_task`. Each channel maintains independent playback state and supports sample rate conversion, enabling simultaneous playback of audio at different rates.

**Channel Mixing Data Flow**
```mermaid
graph TB
    subgraph "Application Thread"
        PlayRaw["playRaw(data, len, rate, stereo, repeat, channel)"]
        PlayWav["playWav(wav_data, len, repeat, channel)"]
        PlayTone["tone(frequency, duration, channel)"]
    end
    
    subgraph "Channel Management"
        SetNextWav["_set_next_wav(ch, wav_info_t)"]
        PlayBits["_play_channel_bits.fetch_or(1<<ch)<br/>atomic<uint16_t>"]
        ChannelArray["channel_info_t _ch_info[8]"]
    end
    
    subgraph "channel_info_t Structure"
        Flip["flip: bool<br/>current buffer selector"]
        WavInfo0["wavinfo[0]: wav_info_t<br/>data, length, repeat<br/>sample_rate_x256"]
        WavInfo1["wavinfo[1]: wav_info_t<br/>next queued audio"]
        Volume["volume: uint8_t<br/>per-channel 0-255"]
        Index["index: size_t<br/>current sample position"]
        Diff["diff: int<br/>rate conversion accumulator"]
        Liner["liner_buf[2][2]: float<br/>previous/current samples"]
    end
    
    subgraph "spk_task Mixing Loop"
        CheckBits["for ch=0 to 7<br/>if (_play_channel_bits & (1<<ch))"]
        LoadSample["Load sample at ch_info[ch].index<br/>Advance index if diff<0"]
        Interpolate["Linear interpolation:<br/>base=current*spk_rate<br/>step=(current-prev)*in_rate<br/>output=(base+step*diff)/spk_rate"]
        VolumeScale["Apply volume:<br/>ch_v = ch_info[ch].volume²<br/>output *= _master_volume² * ch_v"]
        Accumulate["sound_buf32[idx] += output"]
        NextSample["idx++<br/>diff += in_rate<br/>if (diff>=0) load next sample"]
    end
    
    PlayRaw --> SetNextWav
    PlayWav --> SetNextWav
    PlayTone --> SetNextWav
    
    SetNextWav --> PlayBits
    SetNextWav --> ChannelArray
    
    ChannelArray --> Flip
    ChannelArray --> WavInfo0
    ChannelArray --> WavInfo1
    ChannelArray --> Volume
    ChannelArray --> Index
    ChannelArray --> Diff
    ChannelArray --> Liner
    
    PlayBits --> CheckBits
    CheckBits --> LoadSample
    LoadSample --> Interpolate
    Interpolate --> VolumeScale
    VolumeScale --> Accumulate
    Accumulate --> NextSample
    NextSample --> CheckBits
```

**Channel State Management**

The `channel_info_t` structure at [src/utility/Speaker_Class.hpp:265-274]() maintains per-channel state:

```cpp
struct channel_info_t {
    wav_info_t wavinfo[2];     // Current/next flip buffer
    size_t index;               // Sample position in data
    int diff;                   // Rate conversion accumulator
    volatile uint8_t volume;    // Channel volume 0-255
    volatile bool flip;         // Buffer selector
    float liner_buf[2][2];      // Interpolation state [prev/current][L/R]
};
```

**Flip Buffer Mechanism:**
- `wavinfo[!flip]`: Currently playing audio
- `wavinfo[flip]`: Next queued audio
- When current finishes (`repeat==0`), swap flip flag and clear old buffer
- Allows queueing next audio while current plays without gap

**Atomic Channel Tracking:**
```cpp
std::atomic<uint16_t> _play_channel_bits;  // Bitmask of active channels
```
- Bit N set: channel N is active
- Updated atomically by application thread (`fetch_or`, `fetch_and`)
- Read by `spk_task` to determine which channels to mix
- Thread-safe without mutex overhead

The mixing loop at [src/utility/Speaker_Class.cpp:624-790]() processes all active channels, accumulating their contributions to `sound_buf32[]` with rate conversion and volume scaling applied per sample.

Sources:
- [src/utility/Speaker_Class.hpp:244-274]()
- [src/utility/Speaker_Class.cpp:624-790]()
- [src/utility/Speaker_Class.cpp:290-292]()
- [src/utility/Speaker_Class.cpp:1013-1036]()

## Board-Specific Audio Hardware Control

The audio system integrates with external audio codecs and amplifiers through callback-based board-specific initialization. This abstraction separates audio data flow (I2S) from hardware control (I2C, GPIO).

**Callback-Based Hardware Control Architecture**
```mermaid
graph TB
    subgraph "M5Unified Setup (M5.cpp)"
        BoardDetect["_check_boardtype()<br/>Identifies board_t"]
        BeginSpk["_begin_spk(speaker_config_t)<br/>Pin mapping & callback setup"]
        BeginMic["_begin_mic(mic_config_t)<br/>Pin mapping & callback setup"]
    end
    
    subgraph "Speaker_Class"
        SpkCallback["bool (*_cb_set_enabled)(void* args, bool enabled)<br/>void* _cb_set_enabled_args"]
        SpkBegin["bool Speaker_Class::begin()<br/>Calls _cb_set_enabled(args, true)"]
        SpkEnd["void Speaker_Class::end()<br/>Calls _cb_set_enabled(args, false)"]
        SpkSetup["esp_err_t _setup_i2s()<br/>I2S driver configuration"]
    end
    
    subgraph "Mic_Class"
        MicCallback["bool (*_cb_set_enabled)(void* args, bool enabled)<br/>void* _cb_set_enabled_args"]
        MicBegin["bool Mic_Class::begin()<br/>Calls _cb_set_enabled(args, true)"]
        MicEnd["void Mic_Class::end()<br/>Calls _cb_set_enabled(args, false)"]
        MicSetup["esp_err_t _setup_i2s()<br/>I2S driver configuration"]
    end
    
    subgraph "Board-Specific Implementations"
        Lambda["Lambda function in M5.cpp<br/>[](void* args, bool en) { ... }"]
        I2CWrite["I2C_Class::writeRegister8<br/>Codec register writes"]
        GPIOCtrl["GPIO control<br/>Speaker enable pins"]
        CodecInit["Codec initialization<br/>AW88298, ES8311, ES7210"]
    end
    
    subgraph "Hardware"
        Codec["Audio Codec IC"]
        Amp["Amplifier Enable"]
        PDM["PDM Microphone"]
    end
    
    BoardDetect --> BeginSpk
    BoardDetect --> BeginMic
    
    BeginSpk --> SpkCallback
    BeginMic --> MicCallback
    
    SpkCallback --> Lambda
    MicCallback --> Lambda
    
    SpkBegin --> SpkCallback
    SpkEnd --> SpkCallback
    MicBegin --> MicCallback
    MicEnd --> MicCallback
    
    SpkBegin --> SpkSetup
    MicBegin --> MicSetup
    
    Lambda --> I2CWrite
    Lambda --> GPIOCtrl
    Lambda --> CodecInit
    
    I2CWrite --> Codec
    GPIOCtrl --> Amp
    CodecInit --> Codec
    CodecInit --> PDM
    
    SpkSetup --> Codec
    MicSetup --> PDM
```

**Callback Registration Pattern**

The `Speaker_Class` and `Mic_Class` provide callback registration at [src/utility/Speaker_Class.hpp:242]() and [src/utility/Mic_Class.hpp:161]():

```cpp
class Speaker_Class {
    void setCallback(void* args, bool(*func)(void*, bool)) {
        _cb_set_enabled = func;
        _cb_set_enabled_args = args;
    }
private:
    bool (*_cb_set_enabled)(void* args, bool enabled) = nullptr;
    void* _cb_set_enabled_args = nullptr;
};
```

During `M5.begin()`, the board-specific initialization code registers a callback:
```cpp
// Example from M5Unified initialization
Speaker.setCallback(&board_config, [](void* args, bool enable) {
    if (enable) {
        // Initialize codec via I2C
        // Enable amplifier GPIO
    } else {
        // Disable amplifier
        // Power down codec
    }
    return true;
});
```

**Callback Invocation Points:**
- `Speaker_Class::begin()` at [src/utility/Speaker_Class.cpp:921](): Calls `_cb_set_enabled(args, true)` before I2S setup
- `Speaker_Class::end()` at [src/utility/Speaker_Class.cpp:950](): Calls `_cb_set_enabled(args, false)` after stopping task
- `Mic_Class::begin()` at [src/utility/Mic_Class.cpp:725](): Calls `_cb_set_enabled(args, true)` before I2S setup
- `Mic_Class::end()` at [src/utility/Mic_Class.cpp:757](): Calls `_cb_set_enabled(args, false)` after stopping task

This design separates hardware-specific initialization from the generic audio processing code, allowing the audio classes to remain board-agnostic.

Sources:
- [src/utility/Speaker_Class.hpp:242-243]()
- [src/utility/Mic_Class.hpp:161-162]()
- [src/utility/Speaker_Class.cpp:912-946]()
- [src/utility/Mic_Class.cpp:708-759]()

## Sample Rate Conversion and Interpolation

The audio system performs real-time sample rate conversion to accommodate audio data at arbitrary rates. The speaker uses linear interpolation for upsampling/downsampling, while the microphone uses accumulation-based downsampling.

**Speaker Sample Rate Conversion**
```mermaid
graph LR
    subgraph "Input Audio Data"
        InRate["Input Sample Rate<br/>sample_rate_x256<br/>(e.g., 44100 Hz)"]
        InData["Audio Samples<br/>wav_info_t.data"]
    end
    
    subgraph "Rate Conversion State"
        Index["ch_info.index<br/>Current sample position"]
        Diff["ch_info.diff<br/>Fractional accumulator<br/>(fixed-point)"]
        Liner["ch_info.liner_buf[2]<br/>Previous/Current sample"]
    end
    
    subgraph "Conversion Algorithm"
        Accum["Accumulate: diff += in_rate"]
        Check["diff >= 0?"]
        NextSample["Load next input sample<br/>index++"]
        Interp["Linear Interpolation<br/>between samples"]
        Output["Output sample to<br/>sound_buf32[]"]
    end
    
    subgraph "Output Configuration"
        OutRate["Output Sample Rate<br/>spk_sample_rate_x256<br/>(e.g., 48000 Hz)"]
        OutBuffer["DMA Buffer<br/>dma_buf_len samples"]
    end
    
    InRate --> Diff
    InData --> Index
    Index --> NextSample
    
    Diff --> Accum
    Accum --> Check
    Check -->|"Yes"| NextSample
    Check -->|"No"| Interp
    NextSample --> Liner
    Liner --> Interp
    Interp --> Output
    Output --> Accum
    
    OutRate --> Diff
    Output --> OutBuffer
```

**Speaker Rate Conversion Algorithm**
```mermaid
graph TB
    subgraph "Input State (per channel)"
        InRate["sample_rate_x256<br/>Input rate * 256<br/>(e.g., 44100*256)"]
        Index["ch_info.index<br/>Current sample index"]
        Diff["ch_info.diff<br/>Fractional accumulator<br/>Negative = interpolate"]
        LinerPrev["ch_info.liner_buf[1]<br/>Previous sample"]
        LinerBase["ch_info.liner_buf[0]<br/>Current sample"]
    end
    
    subgraph "Output State"
        OutRate["spk_sample_rate_x256<br/>Output rate * 256<br/>(e.g., 48000*256)"]
        OutIdx["idx in sound_buf32[]<br/>Output sample index"]
    end
    
    subgraph "Processing Loop (per output sample)"
        CheckDiff["diff < 0?"]
        LoadNext["Load wav[index++]<br/>LinerPrev = LinerBase<br/>LinerBase = new_sample<br/>diff -= spk_sample_rate_x256"]
        Interpolate["base_l = LinerBase[0] * spk_rate<br/>step_l = (LinerBase[0] - LinerPrev[0]) * in_rate<br/>output = (base_l + step_l * diff) / spk_rate<br/>Apply volume scaling"]
        Accumulate["sound_buf32[idx] += output"]
        Advance["diff += in_rate<br/>idx++"]
    end
    
    InRate --> Diff
    Index --> LoadNext
    
    CheckDiff -->|"No (diff<0)"| Interpolate
    CheckDiff -->|"Yes (need sample)"| LoadNext
    LoadNext --> CheckDiff
    
    LinerPrev --> Interpolate
    LinerBase --> Interpolate
    OutRate --> Interpolate
    Diff --> Interpolate
    
    Interpolate --> Accumulate
    Accumulate --> Advance
    Advance --> OutIdx
    Advance --> CheckDiff
```

**Linear Interpolation Implementation**

From [src/utility/Speaker_Class.cpp:745-786](), the interpolation calculates intermediate samples:

```cpp
// Fixed-point rate with 256x multiplier
#define SAMPLERATE_MUL 256
const int32_t spk_sample_rate_x256 = output_rate * SAMPLERATE_MUL;
const int32_t in_rate = wav_info.sample_rate_x256;

// Linear interpolation between liner_prev and liner_base
float base_l = liner_base[0];                    // Current sample
float step_l = base_l - liner_prev[0];           // Delta to previous
base_l *= spk_sample_rate_x256;                  // Scale by output rate
base_l += step_l * ch_diff;                      // Add fractional position
step_l *= in_rate;                               // Scale delta by input rate

// Output = (base + step*position) / output_rate
int32_t output = base_l / spk_sample_rate_x256;
```

The `ch_diff` accumulator determines the fractional position between samples:
- Starts negative after loading a new input sample
- Incremented by `in_rate` per output sample
- When `ch_diff >= 0`, load next input sample and subtract `spk_sample_rate_x256`

This allows smooth conversion between arbitrary rates (e.g., 44.1kHz → 48kHz).

**Microphone Oversampling**

From [src/utility/Mic_Class.cpp:603-650](), downsampling uses accumulation:

```cpp
int32_t sum_value[2] = {0, 0};  // Stereo accumulator
int os_remain = over_sampling;  // Samples to accumulate

do {
    sum_value[0] += src_buf[src_idx];    // Accumulate left
    sum_value[1] += src_buf[src_idx+1];  // Accumulate right
    src_idx += 2;
} while (--os_remain && (src_idx < src_len));

// When os_remain==0, output averaged sample
float f_gain = (float)gain / (oversampling << 1);
output_sample = sum_value[0] * f_gain;
```

Oversampling benefits:
- Reduces quantization noise by sqrt(over_sampling)
- Improves effective resolution (3dB SNR per 2x oversampling)
- Configured via `mic_config_t.over_sampling` (1-8x, default 2x)

Sources:
- [src/utility/Speaker_Class.cpp:353-354]()
- [src/utility/Speaker_Class.cpp:745-786]()
- [src/utility/Mic_Class.cpp:422-427]()
- [src/utility/Mic_Class.cpp:603-650]()

## Clock Generation and Platform Differences

The audio system abstracts clock generation differences across ESP32 chip variants using platform-specific PLL configurations and fractional dividers.

**Platform-Specific Clock Configuration**
```mermaid
graph TB
    subgraph "Platform Detection"
        ConfigTarget["CONFIG_IDF_TARGET_*<br/>Compile-time chip detection"]
    end
    
    subgraph "PLL Clock Sources"
        ESP32PLL["ESP32/ESP32-S2:<br/>PLL_D2_CLK = 80 MHz<br/>(160 MHz / 2)"]
        ESP32S3PLL["ESP32-S3/C3/C6:<br/>PLL_D2_CLK = 120 MHz<br/>(240 MHz / 2)"]
        ESP32P4PLL["ESP32-P4:<br/>PLL_D2_CLK = 20 MHz"]
    end
    
    subgraph "calcClockDiv Function"
        Input["Input:<br/>baseClock (PLL_D2_CLK)<br/>targetFreq (sample_rate * bits * div_m)<br/>div_m (MCLK multiplier)"]
        Search["Iterative search:<br/>for n in [2, 255]<br/>for a in [1, 63]<br/>b = round(a * (baseClock/targetFreq - n))"]
        Output["Output:<br/>div_n: integer divider [2-255]<br/>div_a: numerator [1-63]<br/>div_b: denominator [0-62]<br/>Actual freq = baseClock / (n + b/a)"]
    end
    
    subgraph "Speaker Clock Setup"
        SpkBits["bits = use_dac ? 1 : 16"]
        SpkDivM["div_m = pin_mck ? 8 : 32/bits"]
        SpkCalc["calcClockDiv(&div_a, &div_b, &div_n,<br/>PLL_D2_CLK, div_m * bits * sample_rate)"]
        SpkRate["Actual rate:<br/>spk_sample_rate_x256 =<br/>PLL_D2_CLK * 256 / (n + b/a) / div_m / bits"]
    end
    
    subgraph "Mic Clock Setup"
        MicBits["bits = use_adc ? 1 : (use_pdm ? 64 : 16)"]
        MicDivM["div_m = use_pdm ? 2 : 8"]
        MicCalc["calcClockDiv(&div_a, &div_b, &div_n,<br/>PLL_D2_CLK / (bits * div_m), sample_rate * over_sampling)"]
    end
    
    subgraph "Hardware Register Configuration"
        ESP32Regs["ESP32:<br/>dev->clkm_conf.clkm_div_num = div_n<br/>dev->clkm_conf.clkm_div_a = div_a<br/>dev->clkm_conf.clkm_div_b = div_b"]
        ESP32S3Regs["ESP32-S3/C3:<br/>i2s_ll_tx_set_raw_clk_div(dev, div_n, div_x, div_y, div_z, yn1)<br/>Fractional divider with yn1 polarity"]
    end
    
    ConfigTarget --> ESP32PLL
    ConfigTarget --> ESP32S3PLL
    ConfigTarget --> ESP32P4PLL
    
    ESP32PLL --> Input
    ESP32S3PLL --> Input
    ESP32P4PLL --> Input
    
    Input --> Search
    Search --> Output
    
    Output --> SpkBits
    SpkBits --> SpkDivM
    SpkDivM --> SpkCalc
    SpkCalc --> SpkRate
    
    Output --> MicBits
    MicBits --> MicDivM
    MicDivM --> MicCalc
    
    Output --> ESP32Regs
    Output --> ESP32S3Regs
```

**Clock Divider Calculation Algorithm**

The `calcClockDiv()` function at [src/utility/Speaker_Class.cpp:300-351]() computes optimal fractional dividers:

```cpp
void calcClockDiv(uint32_t* div_a, uint32_t* div_b, uint32_t* div_n, 
                  uint32_t baseClock, uint32_t targetFreq) {
    float fdiv = (float)baseClock / targetFreq;
    uint32_t n = (uint32_t)fdiv;  // Integer part
    fdiv -= n;                     // Fractional part
    
    // Search for best a/b approximation
    uint32_t save_diff = UINT32_MAX;
    for (uint32_t a = 1; a < 64; ++a) {
        uint32_t b = roundf(a * fdiv);
        if (a <= b) continue;
        uint32_t diff = abs((int)(check_target - ((check_base * a) / (n * a + b))));
        if (save_diff <= diff) continue;
        save_diff = diff;
        save_a = a; save_b = b; save_n = n;
        if (!diff) break;  // Perfect match
    }
}
```

**Platform Clock Differences**

| Platform | PLL_D2_CLK | Typical Sample Rate | Actual Rate (48kHz target) |
|----------|------------|---------------------|----------------------------|
| ESP32 | 80 MHz | 48000 Hz | 48000.0 Hz |
| ESP32-S3 | 120 MHz | 48000 Hz | 48000.0 Hz |
| ESP32-C3 | 120 MHz | 48000 Hz | 48000.0 Hz |
| ESP32-P4 | 20 MHz | 48000 Hz | 47991.1 Hz |

The fractional divider achieves sub-Hz accuracy on most platforms. From [src/utility/Speaker_Class.cpp:396-400]():
```cpp
const int32_t spk_sample_rate_x256 = (float)PLL_D2_CLK * SAMPLERATE_MUL 
    / ((float)(div_b * div_m * bits) / (float)div_a + (div_n * div_m * bits));
```

Sources:
- [src/utility/Speaker_Class.cpp:300-351]()
- [src/utility/Speaker_Class.cpp:381-400]()
- [src/utility/Mic_Class.cpp:431-447]()
- [src/utility/Speaker_Class.cpp:413-489]()
- [src/utility/Mic_Class.cpp:460-526]()

## Task Synchronization and Double Buffering

The audio tasks use FreeRTOS task notifications and semaphores for efficient synchronization between the application thread and background audio processing tasks.

**Speaker Task Synchronization Flow**
```mermaid
sequenceDiagram
    participant App as "Application Thread"
    participant Spk as "Speaker_Class"
    participant Task as "spk_task<br/>(Priority: _cfg.task_priority)"
    participant Sem as "_task_semaphore"
    participant I2S as "I2S DMA"
    
    App->>Spk: playRaw(data, len, rate, ch)
    Spk->>Spk: _play_raw calls _set_next_wav
    
    loop "Wait for queue space"
        Spk->>Spk: Check wavinfo[flip].repeat
        alt "Queue full"
            Spk->>Sem: xSemaphoreTake(_task_semaphore, 1)
            Note over Spk,Sem: Wait for task to clear buffer
        end
    end
    
    Spk->>Spk: wavinfo[flip] = new wav_info_t
    Spk->>Spk: _play_channel_bits.fetch_or(1<<ch)
    Spk->>Task: xTaskNotifyGive(_task_handle)
    
    Task->>Task: ulTaskNotifyTake(pdFALSE, msec)
    
    loop "Audio Mixing Loop"
        Task->>Task: memset(sound_buf32, 0)
        
        loop "For each active channel"
            Task->>Task: if (_play_channel_bits & (1<<ch))
            Task->>Task: Mix samples to sound_buf32[]
            
            alt "wavinfo[!flip].repeat == 0"
                Task->>Task: Flip buffer: flip = !flip
                Task->>Sem: xSemaphoreGive(_task_semaphore)
                Note over Task,Sem: Signal buffer available
            end
        end
        
        Task->>Task: Apply volume & format conversion
        Task->>I2S: _i2s_write(i2s_port, sound_buf32, len)
        
        alt "No active channels"
            Task->>Task: Send silence buffers
            Task->>Task: ulTaskNotifyTake(pdTRUE, portMAX_DELAY)
            Note over Task: Sleep until new data
        end
    end
```

**Microphone Task Synchronization Flow**
```mermaid
sequenceDiagram
    participant App as "Application Thread"
    participant Mic as "Mic_Class"
    participant Task as "mic_task<br/>(Priority: _cfg.task_priority)"
    participant Sem as "_task_semaphore"
    participant I2S as "I2S DMA"
    
    App->>Mic: record(buffer, len, rate)
    Mic->>Mic: _rec_raw queues recording_info_t
    
    loop "Wait for queue space"
        Mic->>Mic: Check _rec_info[_rec_flip].length
        alt "Queue full"
            Mic->>Sem: xSemaphoreTake(_task_semaphore, 1)
        end
    end
    
    Mic->>Mic: _rec_info[_rec_flip] = new recording_info_t
    Mic->>Task: xTaskNotifyGive(_task_handle)
    
    Task->>Task: ulTaskNotifyTake(pdTRUE, portMAX_DELAY)
    Task->>Mic: _is_recording = true
    
    loop "Recording Loop"
        Task->>I2S: _i2s_read(i2s_port, src_buf, len)
        
        loop "Process samples"
            Task->>Task: Accumulate over_sampling samples
            Task->>Task: Apply noise_filter_level
            Task->>Task: Adjust _offset (DC removal)
            Task->>Task: Store to _rec_info[!_rec_flip].data
        end
        
        alt "_rec_info[!_rec_flip].length == 0"
            Task->>Task: _rec_flip = !_rec_flip
            Task->>Sem: xSemaphoreGive(_task_semaphore)
            Note over Task,Sem: Signal recording complete
        end
        
        alt "_rec_info[_rec_flip].length == 0"
            Task->>Mic: _is_recording = false
            Task->>Task: ulTaskNotifyTake(pdTRUE, portMAX_DELAY)
            Note over Task: Sleep until new request
        end
    end
```

**FreeRTOS Synchronization Primitives**

The audio system uses two synchronization mechanisms:

**1. Task Notifications** (lightweight, faster than semaphores):
```cpp
// Wake up task from application thread
xTaskNotifyGive(_task_handle);

// Task waits for notification
ulTaskNotifyTake(pdTRUE, portMAX_DELAY);   // Clear on take, infinite wait
ulTaskNotifyTake(pdFALSE, wait_msec);      // Don't clear, timeout in ms
```

**2. Binary Semaphores** (for buffer completion signaling):
```cpp
// Task signals buffer ready
xSemaphoreGive(_task_semaphore);

// Application waits for buffer
xSemaphoreTake(_task_semaphore, 1);  // 1 tick timeout
```

**Double Buffering Implementation**

From [src/utility/Speaker_Class.cpp:632-665]() and [src/utility/Mic_Class.cpp:567-590]():

```cpp
// Speaker: per-channel flip buffer
struct channel_info_t {
    wav_info_t wavinfo[2];   // [0]=playing when flip=false, [1]=next
    volatile bool flip;       // Buffer selector
};

// Play current: wavinfo[!flip], queue next: wavinfo[flip]
if (wavinfo[!flip].repeat == 0) {
    flip = !flip;                    // Swap buffers
    xSemaphoreGive(_task_semaphore); // Signal queue space available
}

// Microphone: double record buffer
recording_info_t _rec_info[2];
volatile bool _rec_flip;

// Fill _rec_info[!_rec_flip], queue _rec_info[_rec_flip]
if (_rec_info[!_rec_flip].length == 0) {
    _rec_flip = !_rec_flip;          // Swap buffers
    xSemaphoreGive(_task_semaphore); // Signal recording complete
}
```

This design enables zero-copy streaming: the application queues a buffer pointer, the task processes directly from/to that buffer, then signals completion.

Sources:
- [src/utility/Speaker_Class.cpp:517-576]()
- [src/utility/Speaker_Class.cpp:632-665]()
- [src/utility/Speaker_Class.cpp:1013-1036]()
- [src/utility/Mic_Class.cpp:567-590]()
- [src/utility/Mic_Class.cpp:761-780]()

## Speaker Subsystem

The `Speaker_Class` provides audio playback capabilities with support for:
- Multi-channel audio playback (up to 8 virtual channels)
- Support for 8-bit and 16-bit audio data
- WAV file playback
- Tone generation
- Volume control (master and per-channel)
- Multiple output modes (I2S, DAC, buzzer)

### Speaker Class Structure

```mermaid
classDiagram
    class Speaker_Class {
        +speaker_config_t config()
        +void config(const speaker_config_t&)
        +bool begin()
        +void end()
        +bool isRunning()
        +bool isEnabled()
        +bool isPlaying()
        +size_t isPlaying(uint8_t channel)
        +size_t getPlayingChannels()
        +void setVolume(uint8_t master_volume)
        +uint8_t getVolume()
        +void setAllChannelVolume(uint8_t volume)
        +void setChannelVolume(uint8_t channel, uint8_t volume)
        +uint8_t getChannelVolume(uint8_t channel)
        +void stop()
        +void stop(uint8_t channel)
        +bool tone(float frequency, uint32_t duration)
        +bool playRaw(const int8_t* raw_data, size_t array_len)
        +bool playRaw(const uint8_t* raw_data, size_t array_len)
        +bool playRaw(const int16_t* raw_data, size_t array_len)
        +bool playWav(const uint8_t* wav_data, size_t data_len)
    }
    
    class speaker_config_t {
        +int pin_data_out
        +int pin_bck
        +int pin_ws
        +uint32_t sample_rate
        +bool stereo
        +bool buzzer
        +bool use_dac
        +uint8_t dac_zero_level
        +uint8_t magnification
        +size_t dma_buf_len
        +size_t dma_buf_count
        +uint8_t task_priority
        +uint8_t task_pinned_core
        +i2s_port_t i2s_port
    }
    
    class wav_info_t {
        +uint32_t repeat
        +uint32_t sample_rate_x256
        +const void* data
        +size_t length
        +uint8_t flg
    }
    
    class channel_info_t {
        +wav_info_t wavinfo[2]
        +size_t index
        +int diff
        +uint8_t volume
        +bool flip
        +float liner_buf[2][2]
    }
    
    Speaker_Class --> speaker_config_t : "uses"
    Speaker_Class --o channel_info_t : "has 8 channels"
    channel_info_t --o wav_info_t : "contains"
```

Sources:
- [src/utility/Speaker_Class.hpp:79-296]()

### Speaker Configuration

The `Speaker_Class` is configured using a `speaker_config_t` struct with the following key parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| pin_data_out | I2S data output pin | I2S_PIN_NO_CHANGE |
| pin_bck | I2S bit clock pin | I2S_PIN_NO_CHANGE |
| pin_ws | I2S word select pin | I2S_PIN_NO_CHANGE |
| sample_rate | Output sample rate in Hz | 48000 |
| stereo | Enable stereo output | false |
| buzzer | Use single GPIO buzzer mode | false |
| use_dac | Use DAC output (ESP32 GPIO 25/26) | false |
| dac_zero_level | DAC zero level reference (0=Dynamic) | 0 |
| magnification | Output value multiplier | 16 |
| dma_buf_len | DMA buffer length | 256 |
| dma_buf_count | Number of DMA buffers | 8 |
| task_priority | Background task priority | 2 |
| task_pinned_core | Core to run background task (255=any) | 255 |
| i2s_port | I2S port to use | I2S_NUM_0 |

Sources:
- [src/utility/Speaker_Class.hpp:33-77]()

### Speaker Operation

The `Speaker_Class` operates using a background task (`spk_task`) that processes audio data and outputs it through the configured interface (I2S, DAC, or buzzer). The playback process follows this sequence:

```mermaid
sequenceDiagram
    participant App as "Application"
    participant Spk as "Speaker_Class"
    participant Task as "spk_task()"
    participant I2S as "I2S Driver"
    
    App->>Spk: begin()
    Spk->>I2S: _setup_i2s()
    Spk->>Task: Create task
    
    App->>Spk: playRaw(data, len, rate)
    Spk->>Spk: _play_raw()
    Spk->>Spk: _set_next_wav()
    
    loop Playback Loop
        Task->>Task: Process audio data
        Task->>I2S: _i2s_write()
    end
    
    App->>Spk: stop()
    Spk->>Task: Set stop_current flag
```

Sources:
- [src/utility/Speaker_Class.cpp:340-875]() - `spk_task()` implementation
- [src/utility/Speaker_Class.cpp:877-911]() - `begin()` method
- [src/utility/Speaker_Class.cpp:913-938]() - `end()` method
- [src/utility/Speaker_Class.cpp:940-964]() - `stop()` method
- [src/utility/Speaker_Class.cpp:1000-1026]() - `_play_raw()` method
- [src/utility/Speaker_Class.cpp:1028-1108]() - `playWav()` method

### Speaker Usage Examples

Basic usage of the speaker subsystem:

```cpp
// Initialize M5Unified with default configuration
M5.begin();

// Play a tone at 440 Hz for 1000 ms
M5.Speaker.tone(440, 1000);

// Set the master volume to 128 (range 0-255)
M5.Speaker.setVolume(128);

// Play raw audio data
M5.Speaker.playRaw(audio_data, data_length, 44100, false);

// Play a WAV file
M5.Speaker.playWav(wav_data, wav_length);

// Stop all audio playback
M5.Speaker.stop();
```

Custom speaker configuration:

```cpp
// Custom speaker configuration
auto cfg = M5.config();
cfg.speaker.pin_data_out = 25;  // DAC pin
cfg.speaker.use_dac = true;
cfg.speaker.sample_rate = 44100;
cfg.speaker.stereo = false;
M5.begin(cfg);
```

Multi-channel audio playback:

```cpp
// Play a tone on channel 0
M5.Speaker.tone(440, 1000, 0);

// Play a different tone on channel 1
M5.Speaker.tone(880, 1000, 1);

// Set the volume for channel 0
M5.Speaker.setChannelVolume(0, 200);

// Stop playback on channel 1
M5.Speaker.stop(1);
```

## Microphone Subsystem

The `Mic_Class` provides audio recording capabilities with support for:
- Recording to 8-bit or 16-bit buffers
- Configurable sample rate
- Mono/stereo recording
- Noise filtering
- Multiple input modes (I2S, PDM, ADC)

### Microphone Class Structure

```mermaid
classDiagram
    class Mic_Class {
        +mic_config_t config()
        +void config(const mic_config_t&)
        +bool begin()
        +void end()
        +bool isRunning()
        +bool isEnabled()
        +size_t isRecording()
        +void setSampleRate(uint32_t sample_rate)
        +bool record(uint8_t* rec_data, size_t array_len)
        +bool record(int16_t* rec_data, size_t array_len)
        +bool record(uint8_t* rec_data, size_t array_len, uint32_t sample_rate, bool stereo)
        +bool record(int16_t* rec_data, size_t array_len, uint32_t sample_rate, bool stereo)
    }
    
    class mic_config_t {
        +int pin_data_in
        +int pin_bck
        +int pin_mck
        +int pin_ws
        +uint32_t sample_rate
        +uint8_t left_channel
        +uint8_t stereo
        +input_channel_t input_channel
        +uint8_t over_sampling
        +uint8_t magnification
        +uint8_t noise_filter_level
        +bool use_adc
        +size_t dma_buf_len
        +size_t dma_buf_count
        +uint8_t task_priority
        +uint8_t task_pinned_core
        +i2s_port_t i2s_port
    }
    
    class recording_info_t {
        +void* data
        +size_t length
        +size_t index
        +bool is_stereo
        +bool is_16bit
    }
    
    Mic_Class --> mic_config_t : "uses"
    Mic_Class --o recording_info_t : "has 2 buffers"
```

Sources:
- [src/utility/Mic_Class.hpp:98-196]()

### Microphone Configuration

The `Mic_Class` is configured using a `mic_config_t` struct with the following key parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| pin_data_in | I2S data input pin | -1 |
| pin_bck | I2S bit clock pin | I2S_PIN_NO_CHANGE |
| pin_mck | I2S master clock pin | I2S_PIN_NO_CHANGE |
| pin_ws | I2S word select pin | I2S_PIN_NO_CHANGE |
| sample_rate | Input sample rate in Hz | 16000 |
| input_channel | Input channel (right/left/stereo) | input_only_right |
| over_sampling | Sampling times to obtain average | 2 |
| magnification | Input value multiplier | 16 |
| noise_filter_level | Noise filtering coefficient | 0 |
| use_adc | Use analog input (ADC) | false |
| dma_buf_len | DMA buffer length | 128 |
| dma_buf_count | Number of DMA buffers | 8 |
| task_priority | Background task priority | 2 |
| task_pinned_core | Core to run background task (255=any) | 255 |
| i2s_port | I2S port to use | I2S_NUM_0 |

Sources:
- [src/utility/Mic_Class.hpp:42-96]()

### Microphone Operation

The `Mic_Class` operates using a background task (`mic_task`) that reads audio data from the configured interface (I2S, PDM, or ADC) and stores it in application-provided buffers. The recording process follows this sequence:

```mermaid
sequenceDiagram
    participant App as "Application"
    participant Mic as "Mic_Class"
    participant Task as "mic_task()"
    participant I2S as "I2S Driver"
    
    App->>Mic: begin()
    Mic->>I2S: _setup_i2s()
    Mic->>Task: Create task
    
    App->>Mic: record(buffer, len, rate)
    Mic->>Mic: _rec_raw()
    
    loop Recording Loop
        Task->>I2S: _i2s_read()
        Task->>Task: Process audio data
        Task->>Task: Store in buffer
    end
    
    Note over App,Task: Recording completes when buffer is full
```

Sources:
- [src/utility/Mic_Class.cpp:407-673]() - `mic_task()` implementation
- [src/utility/Mic_Class.cpp:675-712]() - `begin()` method
- [src/utility/Mic_Class.cpp:714-726]() - `end()` method
- [src/utility/Mic_Class.cpp:728-747]() - `_rec_raw()` method

### Microphone Usage Examples

Basic usage of the microphone subsystem:

```cpp
// Initialize M5Unified with default configuration
M5.begin();

// Allocate a buffer for recording
int16_t audio_buffer[1024];

// Record audio data
M5.Mic.record(audio_buffer, 1024, 16000, false);

// Wait for recording to complete
while (M5.Mic.isRecording()) {
  delay(10);
}
```

Custom microphone configuration:

```cpp
// Custom microphone configuration
auto cfg = M5.config();
cfg.mic.pin_data_in = 34;  // ADC pin
cfg.mic.use_adc = true;
cfg.mic.sample_rate = 16000;
cfg.mic.over_sampling = 2;
cfg.mic.noise_filter_level = 32;
M5.begin(cfg);
```

## Implementation Details

### Hardware Support

The Audio System supports various hardware configurations across the M5Stack ecosystem:

#### Speaker Output Options:
- I2S digital audio output (standard for most M5Stack devices)
- DAC analog output (ESP32 GPIO 25/26)
- Simple buzzer output (single GPIO pin)

#### Microphone Input Options:
- I2S digital audio input (standard for most M5Stack microphones)
- PDM digital audio input (used in some MEMS microphones)
- ADC analog input (for analog microphones)

The system automatically adapts to different ESP32 chip versions (ESP32, ESP32-S2, ESP32-S3, ESP32-C3, ESP32-C6) through conditional compilation.

Sources:
- [src/utility/Speaker_Class.cpp:40-64]() - ESP32 version detection
- [src/utility/Mic_Class.cpp:46-73]() - ESP32 version detection

### Speaker Implementation

The Speaker_Class implementation uses a background FreeRTOS task (`spk_task`) that:
1. Sets up the I2S driver with the configured parameters
2. Waits for audio data to be queued for playback
3. Mixes audio data from all active channels
4. Applies volume adjustments and processing
5. Outputs the processed data through I2S, DAC, or buzzer

The implementation supports sample rate conversion, allowing playback of audio data at different rates than the configured output rate.

Sources:
- [src/utility/Speaker_Class.cpp:340-875]() - `spk_task()` implementation
- [src/utility/Speaker_Class.cpp:975-998]() - `wav_info_t` management
- [src/utility/Speaker_Class.cpp:1000-1026]() - `_play_raw()` method

### Microphone Implementation

The Mic_Class implementation uses a background FreeRTOS task (`mic_task`) that:
1. Sets up the I2S driver with the configured parameters
2. Starts I2S input
3. Waits for a recording request
4. Reads audio data from I2S
5. Applies processing (oversampling, noise filtering, etc.)
6. Stores the processed data in the application buffer

The implementation includes automatic zero-level adjustment and optional noise filtering.

Sources:
- [src/utility/Mic_Class.cpp:407-673]() - `mic_task()` implementation
- [src/utility/Mic_Class.cpp:594-596]() - Automatic zero level adjustment
- [src/utility/Mic_Class.cpp:603-616]() - Noise filtering

## Advanced Audio Applications

The Audio System serves as a foundation for more advanced audio applications, including:

- **Real-time FFT Analysis**: Analyzing the frequency spectrum of audio signals
- **Bluetooth A2DP**: Streaming audio via Bluetooth
- **Web Radio**: Streaming audio from Internet radio sources
- **MP3 Playback**: Decoding and playing MP3 files
- **Text-to-Speech**: Converting text to spoken audio

An example of FFT analysis is included in the M5Unified library, demonstrating real-time frequency analysis of microphone input.

```mermaid
graph TD
    Mic["M5.Mic"] --> Record["Record audio data"]
    Record --> WavData["wav_data_t"]
    WavData --> FFTFunction["fft_function_t"]
    FFTFunction --> FFTData["fft_data_t"]
    FFTData --> Visualization["Audio Visualizations"]
    Visualization --> WavDrawer["Waveform Display"]
    Visualization --> FFTDrawer["Spectrum Display"]
    Visualization --> FFTPeak["Frequency Detection"]
    Visualization --> FFTHistory["Spectrogram"]
```

Sources:
- [examples/Advanced/Mic_FFT/Mic_FFT.ino]()