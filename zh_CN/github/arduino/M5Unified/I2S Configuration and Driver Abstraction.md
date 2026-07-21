M5Unified I2S Configuration and Driver Abstraction

# I2S Configuration and Driver Abstraction

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

This document describes the I2S (Inter-IC Sound) peripheral configuration and driver abstraction layer in M5Unified's audio system. It covers how the library provides a unified interface across multiple ESP-IDF versions and ESP32 variants while handling low-level I2S hardware setup, clock generation, and pin configuration.

For information about the higher-level audio playback and mixing system, see [Speaker Interface and Multi-Channel Mixing](#4.2). For microphone signal processing and recording, see [Microphone Interface and Signal Processing](#4.3). For board-specific audio codec initialization, see [Board-Specific Audio Configuration](#4.4).

---

## ESP-IDF Version Abstraction Strategy

M5Unified supports multiple ESP-IDF versions by detecting the API version at compile time and providing conditional compilation paths. This abstraction is critical because ESP-IDF 5.0+ introduced a completely redesigned I2S driver API.

### Version Detection Logic

```mermaid
graph TD
    CompileTime["Compile-Time Detection"]
    HasInclude["Check __has_include(<driver/i2s_std.h>)"]
    CheckVersion["Check ESP_IDF_VERSION"]
    
    V2["I2S_DRIVER_VERSION = 2<br/>New Driver API"]
    V1["I2S_DRIVER_VERSION = 1<br/>Legacy Driver API"]
    
    DefineConstants["Define API Constants:<br/>COMM_FORMAT_I2S<br/>COMM_FORMAT_MSB<br/>SAMPLE_RATE_TYPE"]
    
    CompileTime --> HasInclude
    HasInclude -->|"Has <driver/i2s_std.h>"| CheckVersion
    HasInclude -->|"No <driver/i2s_std.h>"| V1
    
    CheckVersion -->|">= ESP-IDF 5.0.0"| V2
    CheckVersion -->|"< ESP-IDF 5.0.0"| V1
    
    V2 --> DefineConstants
    V1 --> DefineConstants
    
    DefineConstants --> CompilePath["Compile appropriate code path"]
```

**Sources:** [src/utility/Speaker_Class.cpp:10-72](), [src/utility/Mic_Class.cpp:8-82]()

### Key Macro Definitions

| Macro | Purpose | Values |
|-------|---------|--------|
| `I2S_DRIVER_VERSION` | Selects driver implementation | `1` (legacy) or `2` (new) |
| `COMM_FORMAT_I2S` | I2S standard format constant | `I2S_COMM_FORMAT_I2S` or `I2S_COMM_FORMAT_STAND_I2S` |
| `COMM_FORMAT_MSB` | MSB-first format constant | `I2S_COMM_FORMAT_I2S_MSB` or `I2S_COMM_FORMAT_STAND_MSB` |
| `SAMPLE_RATE_TYPE` | Sample rate data type | `int` or `uint32_t` |
| `NON_BREAK` | C++17 fallthrough attribute | Empty or `[[fallthrough]]` |

The version detection uses multiple checks:
- `__has_include(<esp_idf_version.h>)` - Verify IDF header availability
- `ESP_IDF_VERSION_MAJOR` - Check major version number
- `__has_include(<driver/i2s_std.h>)` - Detect new driver API presence

**Sources:** [src/utility/Speaker_Class.cpp:48-72](), [src/utility/Mic_Class.cpp:55-82]()

---

## Configuration Structures

### Speaker Configuration

The `speaker_config_t` structure defines all parameters for I2S audio output:

```mermaid
classDiagram
    class speaker_config_t {
        +int pin_data_out
        +int pin_bck
        +int pin_mck
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
    
    note for speaker_config_t "Default sample_rate: 48000 Hz\nDefault dma_buf_len: 256\nDefault dma_buf_count: 8\nDefault i2s_port: I2S_NUM_0"
```

**Pin Configuration Fields:**
- `pin_data_out`: I2S data output pin (DOUT/SD)
- `pin_bck`: Bit clock pin (BCLK/SCK)
- `pin_ws`: Word select pin (LRCLK/WS)
- `pin_mck`: Master clock pin (optional, -1 if unused)

**Audio Format Fields:**
- `sample_rate`: Output sampling rate in Hz (default: 48000)
- `stereo`: `true` for stereo output, `false` for mono

**Special Modes:**
- `buzzer`: Use 1-bit delta-sigma PWM for piezo buzzer output
- `use_dac`: Use internal DAC (ESP32 only, GPIO 25/26 only, requires `I2S_NUM_0`)
- `dac_zero_level`: DAC offset level (0 = dynamic adjustment)

**DMA Configuration:**
- `dma_buf_len`: Length of each DMA buffer (max 1024)
- `dma_buf_count`: Number of DMA buffers

**Sources:** [src/utility/Speaker_Class.hpp:33-80]()

### Microphone Configuration

The `mic_config_t` structure defines parameters for I2S audio input:

```mermaid
classDiagram
    class mic_config_t {
        +int pin_data_in
        +int pin_bck
        +int pin_mck
        +int pin_ws
        +uint32_t sample_rate
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
    
    class input_channel_t {
        <<enumeration>>
        input_only_right
        input_only_left
        input_stereo
    }
    
    mic_config_t --> input_channel_t
    
    note for mic_config_t "Default sample_rate: 16000 Hz\nDefault dma_buf_len: 128\nDefault dma_buf_count: 8"
```

**Signal Processing Fields:**
- `over_sampling`: Oversampling factor for averaging (1-8, default: 2)
- `magnification`: Input gain multiplier (default: 16)
- `noise_filter_level`: IIR filter coefficient for noise reduction (0-255, default: 0)

**Channel Selection:**
- `input_only_right` (0): Capture only right channel
- `input_only_left` (1): Capture only left channel
- `input_stereo` (2): Capture both channels

**Special Modes:**
- `use_adc`: Use analog input via ADC (ESP32 only)
- When `pin_bck < 0` and `pin_ws < 0`: Automatically use PDM mode

**Sources:** [src/utility/Mic_Class.hpp:42-96]()

---

## Clock Configuration and Sample Rate Generation

The I2S peripheral requires precise clock generation to achieve accurate sample rates. M5Unified uses fractional dividers to minimize sample rate error.

### PLL Clock Sources by Platform

```mermaid
graph LR
    subgraph "Clock Sources"
        PLL_ESP32["ESP32/ESP32-S2<br/>PLL_D2_CLK = 80 MHz"]
        PLL_C3_S3["ESP32-C3/C6/S3<br/>PLL_D2_CLK = 120 MHz"]
        PLL_P4["ESP32-P4<br/>PLL_D2_CLK = 20 MHz"]
    end
    
    subgraph "Clock Division"
        DivCalc["calcClockDiv()<br/>Fractional Division"]
        DivN["Integer Divider (N)"]
        DivFrac["Fractional Divider (A/B)"]
    end
    
    subgraph "Output"
        MCLK["Master Clock (MCLK)"]
        BCLK["Bit Clock (BCLK)"]
        SampleRate["Sample Rate"]
    end
    
    PLL_ESP32 --> DivCalc
    PLL_C3_S3 --> DivCalc
    PLL_P4 --> DivCalc
    
    DivCalc --> DivN
    DivCalc --> DivFrac
    
    DivN --> MCLK
    DivFrac --> MCLK
    
    MCLK --> BCLK
    BCLK --> SampleRate
```

**Platform-Specific Clock Sources:**

| Platform | Base Clock | Constant Definition |
|----------|------------|---------------------|
| ESP32, ESP32-S2 | 80 MHz | `PLL_D2_CLK = 80*1000*1000` |
| ESP32-C3, ESP32-C6, ESP32-S3 | 120 MHz | `PLL_D2_CLK = 120*1000*1000` |
| ESP32-P4 | 20 MHz | `PLL_D2_CLK = 20*1000*1000` |

**Sources:** [src/utility/Speaker_Class.cpp:381-387](), [src/utility/Mic_Class.cpp:431-437]()

### Clock Divider Calculation Algorithm

The `calcClockDiv()` function computes optimal fractional divider values to achieve the target frequency with minimal error:

**Formula:**
```
Target Frequency = Base Clock / (N + B/A)
```

Where:
- `N`: Integer divider (2-255)
- `A`: Fractional denominator (1-63)
- `B`: Fractional numerator (0 to A-1)

**Algorithm Flow:**

```mermaid
graph TD
    Input["Input: baseClock, targetFreq"]
    Check["baseClock <= targetFreq * 2?"]
    
    MinValues["Set N=2, A=1, B=0<br/>Return minimum values"]
    
    CalcDiv["Calculate fdiv = baseClock / targetFreq"]
    ExtractN["Extract integer: N = floor(fdiv)"]
    ExtractFrac["Extract fraction: fdiv - N"]
    
    SearchLoop["Search A=1 to 63<br/>Calculate B = round(A * fraction)"]
    CheckError["Calculate frequency error"]
    UpdateBest["Update best values if error improves"]
    
    FixDivY["Handle div_y == 0 edge case<br/>Set div_y=1, div_b=511"]
    
    Output["Output: div_a, div_b, div_n"]
    
    Input --> Check
    Check -->|Yes| MinValues
    Check -->|No| CalcDiv
    CalcDiv --> ExtractN
    ExtractN --> ExtractFrac
    ExtractFrac --> SearchLoop
    SearchLoop --> CheckError
    CheckError --> UpdateBest
    UpdateBest -->|Continue| SearchLoop
    UpdateBest -->|Complete| FixDivY
    FixDivY --> Output
    MinValues --> Output
```

The algorithm performs an exhaustive search across all possible `A` values to find the combination that minimizes frequency error. It includes a workaround for the hardware bug where `div_y == 0` causes the fractional component to be ignored.

**Sources:** [src/utility/Speaker_Class.cpp:300-351](), [src/utility/Mic_Class.cpp:419-421]()

### Actual Sample Rate Computation

After configuring the dividers, the actual achieved sample rate differs slightly from the requested rate:

```
Actual Sample Rate = (PLL_D2_CLK * SAMPLERATE_MUL) / 
                     ((div_b * div_m * bits) / div_a + (div_n * div_m * bits))
```

Where:
- `div_m`: BCLK divider (typically 8 for MCLK devices, 32/bits otherwise)
- `bits`: Bits per sample (16 for standard I2S, 1 for DAC, 64 for PDM)
- `SAMPLERATE_MUL`: Scaling factor (256) for precision

**Sources:** [src/utility/Speaker_Class.cpp:388-400](), [src/utility/Mic_Class.cpp:443-447]()

---

## I2S Driver Initialization Flow

### Driver Version Branching

```mermaid
graph TD
    Setup["_setup_i2s() Entry"]
    CheckPin["Check pin_data_out/pin_data_in >= 0"]
    CheckDAC["Check use_dac and i2s_port"]
    
    DriverCheck{{"I2S_DRIVER_VERSION == 2?"}}
    
    subgraph "New Driver Path (v2)"
        NewChanCfg["Create i2s_chan_config_t<br/>Set DMA parameters"]
        NewChannel["i2s_new_channel()<br/>Get i2s_chan_handle_t"]
        NewI2SCfg["Create i2s_std_config_t or i2s_pdm_rx_config_t"]
        NewInit["i2s_channel_init_std_mode() or<br/>i2s_channel_init_pdm_rx_mode()"]
    end
    
    subgraph "Legacy Driver Path (v1)"
        LegacyCfg["Create i2s_config_t<br/>Set mode and format"]
        LegacyPin["Create i2s_pin_config_t"]
        LegacyInstall["i2s_driver_install()"]
        LegacySetPin["i2s_set_pin()"]
    end
    
    SetDAC["Configure DAC mode<br/>_i2s_set_dac()"]
    SetADC["Configure ADC mode<br/>_i2s_set_adc()"]
    
    Return["Return esp_err_t"]
    
    Setup --> CheckPin
    CheckPin -->|"Invalid"| Return
    CheckPin -->|"Valid"| CheckDAC
    CheckDAC -->|"DAC on wrong port"| Return
    CheckDAC -->|"Valid"| DriverCheck
    
    DriverCheck -->|"Version 2"| NewChanCfg
    DriverCheck -->|"Version 1"| LegacyCfg
    
    NewChanCfg --> NewChannel
    NewChannel --> NewI2SCfg
    NewI2SCfg --> NewInit
    NewInit --> SetDAC
    
    LegacyCfg --> LegacyPin
    LegacyPin --> LegacyInstall
    LegacyInstall --> LegacySetPin
    LegacySetPin --> SetDAC
    
    SetDAC -->|"use_dac"| Return
    SetDAC -->|"!use_dac"| SetADC
    SetADC --> Return
```

**Sources:** [src/utility/Speaker_Class.cpp:186-298](), [src/utility/Mic_Class.cpp:298-417]()

### New Driver API (ESP-IDF 5.0+)

**Channel Configuration:**

The new API uses a handle-based approach with separate transmit and receive channels:

```mermaid
sequenceDiagram
    participant App as Application
    participant Setup as _setup_i2s()
    participant Driver as ESP-IDF I2S Driver
    participant HW as I2S Hardware
    
    App->>Setup: Call _setup_i2s()
    Setup->>Setup: Uninstall existing driver
    Setup->>Driver: i2s_new_channel(&chan_cfg, &tx_handle, &rx_handle)
    Driver->>HW: Allocate DMA buffers
    Driver-->>Setup: Return handle
    
    Setup->>Setup: Configure i2s_std_config_t
    Note over Setup: Clock source: I2S_CLK_SRC_PLL_160M<br/>Slot config: stereo/mono<br/>GPIO config: pins
    
    Setup->>Driver: i2s_channel_init_std_mode(handle, &config)
    Driver->>HW: Configure registers
    Driver-->>Setup: ESP_OK
    
    alt DAC Mode (ESP32 only)
        Setup->>Setup: _i2s_set_dac(port, left_en, right_en)
        Setup->>HW: Configure DAC registers
    end
    
    Setup-->>App: ESP_OK
```

**Key Structures:**

- `i2s_chan_config_t`: DMA configuration with `dma_desc_num`, `dma_frame_num`, `auto_clear`
- `i2s_std_config_t`: Standard I2S mode with clock, slot, and GPIO configuration
- `i2s_pdm_rx_config_t`: PDM mode for microphones (if `pin_bck < 0`)

**Sources:** [src/utility/Speaker_Class.cpp:194-243](), [src/utility/Mic_Class.cpp:301-368]()

### Legacy Driver API (ESP-IDF < 5.0)

**Direct Configuration:**

The legacy API uses port-based configuration:

```mermaid
sequenceDiagram
    participant App as Application
    participant Setup as _setup_i2s()
    participant Driver as ESP-IDF I2S Driver
    participant HW as I2S Hardware
    
    App->>Setup: Call _setup_i2s()
    
    Setup->>Setup: Create i2s_config_t
    Note over Setup: mode: MASTER | TX/RX<br/>sample_rate: target rate<br/>bits_per_sample: 16-bit<br/>dma_buf_count/len
    
    Setup->>Driver: i2s_driver_install(port, &config, 0, NULL)
    Driver->>HW: Configure peripheral
    alt Install Failed
        Driver->>Driver: i2s_driver_uninstall(port)
        Driver->>Driver: Retry install
    end
    Driver-->>Setup: ESP_OK
    
    alt Standard I2S Mode
        Setup->>Setup: Create i2s_pin_config_t
        Setup->>Driver: i2s_set_pin(port, &pin_config)
    end
    
    alt DAC Mode (ESP32 only)
        Setup->>Driver: i2s_set_dac_mode(dac_mode)
        Setup->>HW: Configure DAC channels
    end
    
    alt ADC Mode (ESP32 only)
        Setup->>Driver: i2s_set_adc_mode(unit, channel)
        Setup->>HW: Configure ADC
    end
    
    Setup-->>App: ESP_OK
```

**Sources:** [src/utility/Speaker_Class.cpp:244-296](), [src/utility/Mic_Class.cpp:370-416]()

### Handle Management

For the new driver API, M5Unified maintains a global array of channel handles:

```c++
static i2s_chan_handle_t _i2s_handle[SOC_I2S_NUM] = { nullptr, };
```

This allows multiple subsystems to check if an I2S port is in use and prevents double-initialization.

**Sources:** [src/utility/Speaker_Class.cpp:84](), [src/utility/Mic_Class.cpp:92]()

---

## Pin Mapping and GPIO Configuration

### I2S Pin Roles

```mermaid
graph LR
    subgraph "ESP32 I2S Peripheral"
        MCLK["MCLK (Master Clock)<br/>Optional<br/>Typically 128x or 256x sample rate"]
        BCLK["BCLK (Bit Clock)<br/>Required<br/>Bits per sample × channels × sample rate"]
        WS["WS (Word Select / LRCLK)<br/>Required<br/>Toggles each sample<br/>Low=Left, High=Right"]
        DIN["DIN (Data In)<br/>For microphone/ADC"]
        DOUT["DOUT (Data Out)<br/>For speaker/DAC"]
    end
    
    subgraph "External Device"
        Codec["Audio Codec<br/>or<br/>I2S Microphone<br/>or<br/>DAC/ADC"]
    end
    
    MCLK -.->|"Optional clock reference"| Codec
    BCLK <-->|"Bit synchronization"| Codec
    WS <-->|"Channel selection"| Codec
    DIN <--|"Audio samples in"| Codec
    DOUT -->|"Audio samples out"| Codec
    
    style MCLK stroke-dasharray: 5 5
```

**Pin Assignment Rules:**

| Pin | Speaker | Microphone | Required | Notes |
|-----|---------|------------|----------|-------|
| DOUT | ✓ | | Yes | Cannot be -1 for speaker |
| DIN | | ✓ | Yes | Cannot be -1 for microphone |
| BCLK | ✓ | ✓ | Usually | Can be -1 for PDM mode on mic |
| WS | ✓ | ✓ | Usually | Can be -1 for PDM mode on mic, doubles as PDM clock |
| MCLK | ✓ | ✓ | No | Some codecs require this for clock reference |

**Sources:** [src/utility/Speaker_Class.cpp:227-230](), [src/utility/Mic_Class.cpp:325-327, 353-357]()

### GPIO Constraints

**DAC Mode (ESP32 only):**
- Only `GPIO_NUM_25` (right channel, DAC channel 1)
- Only `GPIO_NUM_26` (left channel, DAC channel 2)
- Must use `I2S_NUM_0` (I2S port 1 does not support DAC)

**ADC Mode (ESP32 only):**
- ADC1: GPIO 32-39
- ADC2: GPIO 0, 2, 4, 12-15, 25-27

**General I2S:**
- Any GPIO can be used for BCLK, WS, MCLK, DOUT, DIN
- Avoid input-only GPIOs (34-39 on ESP32) for output pins

**Sources:** [src/utility/Speaker_Class.cpp:190-193, 234-241](), [src/utility/Mic_Class.cpp:134-219, 239-293]()

---

## Special Hardware Modes

### DAC Mode (ESP32 Only)

The ESP32's internal DAC can be used for audio output without external hardware.

```mermaid
graph LR
    subgraph "I2S Peripheral"
        I2S["I2S DMA Engine"]
        LCD_EN["LCD_EN = true<br/>(Parallel mode)"]
    end
    
    subgraph "DAC Subsystem"
        DAC_LL["DAC Low-Level Driver"]
        DAC0["DAC Channel 0<br/>GPIO 25"]
        DAC1["DAC Channel 1<br/>GPIO 26"]
    end
    
    I2S -->|"16-bit samples"| LCD_EN
    LCD_EN -->|"8-bit output"| DAC_LL
    DAC_LL --> DAC0
    DAC_LL --> DAC1
    
    DAC0 -->|"Analog voltage 0-3.3V"| Speaker["Speaker or<br/>Audio Output"]
    DAC1 -->|"Analog voltage 0-3.3V"| Speaker
```

**Configuration Steps:**

1. **Power Management:**
   - Enable DAC power with `dac_ll_power_on(channel)`
   - Configure RTC GPIO mode
   - Disable pull-up/pull-down resistors

2. **Register Configuration:**
   - Set `I2S0.conf2.lcd_en = true` (enables parallel/LCD mode)
   - Configure `I2S0.conf.tx_right_first = false`
   - Set bit shift and sync parameters

3. **Data Format:**
   - I2S outputs 16-bit stereo data
   - Upper 8 bits go to DAC
   - Lower 8 bits ignored
   - Unsigned format: 0x0000 = 0V, 0xFF00 = 3.3V

**Dynamic Zero-Level Adjustment:**

When `dac_zero_level == 0`, M5Unified dynamically adjusts the DC offset to minimize DAC output noise:

- During silence: Gradually reduce DC offset toward zero
- During playback: Set offset to maximum amplitude to prevent clipping
- Benefits: Reduces hiss/noise when no audio is playing

**Sources:** [src/utility/Speaker_Class.cpp:107-143, 164-183, 234-241, 534-549, 563-570, 593-600, 802-837]()

### ADC Mode (ESP32 Only)

The ESP32 can capture audio using the internal ADC via I2S DMA.

```mermaid
graph LR
    subgraph "Analog Input"
        Mic["Electret Microphone<br/>with bias circuit"]
        GPIO["GPIO 32-39 (ADC1)<br/>or<br/>GPIO 0,2,4,12-15,25-27 (ADC2)"]
    end
    
    subgraph "ADC Subsystem"
        ADC["12-bit ADC<br/>0-3.3V range"]
        DigFilter["Digital Filter"]
    end
    
    subgraph "I2S Peripheral"
        DMA["I2S DMA Engine"]
        Buffer["Receive Buffer"]
    end
    
    Mic --> GPIO
    GPIO --> ADC
    ADC -->|"12-bit samples"| DigFilter
    DigFilter --> DMA
    DMA --> Buffer
    Buffer -->|"16-bit format"| App["Application"]
```

**Configuration Steps:**

1. **ADC Unit Selection:**
   - GPIO 32-39 use ADC1
   - GPIO 0, 2, 4, 12-15, 25-27 use ADC2
   - Map GPIO to ADC channel using lookup table

2. **ADC Parameters:**
   - Set attenuation: `ADC_ATTEN_DB_12` (0-2.6V range)
   - Set width: `ADC_WIDTH_BIT_12` (12-bit resolution)
   - Configure sample rate and FSM timing

3. **Register Configuration:**
   - Set `I2S0.conf2.lcd_en = true`
   - Configure RX channel mode
   - Set FIFO mode for proper data alignment

4. **Data Format:**
   - 12-bit ADC values in 16-bit container
   - Center value: 2048 (1.3V input)
   - Subtract 2048 to get signed audio data

**Sources:** [src/utility/Mic_Class.cpp:113-220, 238-293, 361-366, 404-413, 620-623]()

### PDM Mode (Microphone)

PDM (Pulse Density Modulation) microphones are common in M5Stack devices. PDM mode is automatically enabled when `pin_bck < 0`.

```mermaid
graph LR
    subgraph "PDM Microphone"
        MEMS["MEMS Sensor"]
        Modulator["1-bit Sigma-Delta<br/>Modulator"]
        CLK["Clock Input"]
        DATA["Data Output<br/>(1-bit stream)"]
    end
    
    subgraph "ESP32 I2S Peripheral"
        ClkGen["Clock Generator<br/>(via WS pin)"]
        PDM2PCM["PDM to PCM<br/>Decimation Filter"]
        DSR["Downsampling Ratio<br/>DSR=64 or DSR=128"]
    end
    
    subgraph "Processing"
        DMA["DMA Buffer"]
        Oversample["Oversampling<br/>Averaging"]
        Output["16-bit PCM"]
    end
    
    ClkGen -->|"PDM clock"| CLK
    MEMS --> Modulator
    Modulator --> DATA
    DATA -->|"1-bit stream"| PDM2PCM
    PDM2PCM --> DSR
    DSR --> DMA
    DMA --> Oversample
    Oversample --> Output
```

**Configuration for New Driver API:**

```c++
i2s_pdm_rx_config_t i2s_config;
i2s_config.clk_cfg.clk_src = I2S_CLK_SRC_PLL_160M;
i2s_config.clk_cfg.sample_rate_hz = sample_rate;
i2s_config.slot_cfg.slot_mode = I2S_SLOT_MODE_MONO;
i2s_config.slot_cfg.slot_mask = left_channel ? I2S_PDM_SLOT_LEFT : I2S_PDM_SLOT_RIGHT;
i2s_config.gpio_cfg.clk = (gpio_num_t)_cfg.pin_ws;  // PDM clock
i2s_config.gpio_cfg.din = (gpio_num_t)_cfg.pin_data_in;
```

**Configuration for Legacy Driver API:**

```c++
i2s_config.mode = I2S_MODE_MASTER | I2S_MODE_RX | I2S_MODE_PDM;
i2s_config.communication_format = I2S_COMM_FORMAT_STAND_PCM_SHORT;
dev->pdm_conf.rx_sinc_dsr_16_en = 1;  // DSR=128
dev->pdm_conf.pdm2pcm_conv_en = 1;
dev->pdm_conf.rx_pdm_en = 1;
```

**Clock Configuration:**

For PDM mode, the clock divider calculation uses `bits = 64` (DSR ratio) instead of 16, and `div_m = 2` for the clock divider.

**Sources:** [src/utility/Mic_Class.cpp:310-329, 392-395, 429, 446, 462-463, 528-534]()

---

## Platform-Specific Implementation Details

### Register Access Differences

```mermaid
graph TD
    Platform{{"Target Platform"}}
    
    ESP32["ESP32 / ESP32-S2"]
    C3_S3["ESP32-C3 / ESP32-S3"]
    C6["ESP32-C6"]
    P4["ESP32-P4"]
    
    Platform --> ESP32
    Platform --> C3_S3
    Platform --> C6
    Platform --> P4
    
    ESP32 --> ESP32Regs["Register Access:<br/>dev->sample_rate_conf.tx_bck_div_num<br/>dev->clkm_conf.clkm_div_a/b/num<br/>I2S0/I2S1 structs"]
    
    C3_S3 --> C3S3Regs["Register Access:<br/>dev->tx_conf1.tx_bck_div_num<br/>dev->tx_clkm_div_conf.tx_clkm_div_x/y/z<br/>dev->tx_clkm_conf.tx_clkm_div_num<br/>i2s_ll_tx_set_raw_clk_div()"]
    
    C6 --> C6Regs["Register Access:<br/>PCR.i2s_tx_clkm_div_conf<br/>PCR.i2s_tx_clkm_conf<br/>Separate PCR peripheral"]
    
    P4 --> P4Regs["Register Access:<br/>dev->tx_conf.tx_bck_div_num<br/>(no tx_conf1)<br/>20 MHz base clock"]
    
    ESP32Regs --> Features1["Features:<br/>• DAC support<br/>• ADC support<br/>• Simple clock structure"]
    C3S3Regs --> Features2["Features:<br/>• No DAC/ADC<br/>• Advanced fractional divider<br/>• Mono duplication mode"]
    C6Regs --> Features3["Features:<br/>• No DAC/ADC<br/>• PCR clock control<br/>• Separate clock peripheral"]
    P4Regs --> Features4["Features:<br/>• No DAC/ADC<br/>• Different register layout<br/>• Lower base clock"]
```

**Sources:** [src/utility/Speaker_Class.cpp:402-489](), [src/utility/Mic_Class.cpp:449-547]()

### Clock Register Programming

**ESP32 / ESP32-S2:**

```c++
dev->sample_rate_conf.tx_bck_div_num = div_m;
dev->clkm_conf.clkm_div_a = div_a;
dev->clkm_conf.clkm_div_b = div_b;
dev->clkm_conf.clkm_div_num = div_n;
dev->clkm_conf.clka_en = 0;  // PLL_160M
```

**ESP32-C3 / ESP32-S3:**

```c++
dev->tx_conf1.tx_bck_div_num = div_m - 1;

// Calculate fractional components with yn1 optimization
bool yn1 = (div_b > (div_a >> 1));
if (yn1) { div_b = div_a - div_b; }
int div_x = div_b ? (div_a / div_b - 1) : 0;
int div_y = div_b ? (div_a % div_b) : 1;

// Handle div_y == 0 hardware bug
if (div_y == 0) { div_y = 1; div_b = 511; }

i2s_ll_tx_set_raw_clk_div(dev, div_n, div_x, div_y, div_b, yn1);
```

**ESP32-C6:**

```c++
PCR.i2s_tx_clkm_div_conf.i2s_tx_clkm_div_x = div_x;
PCR.i2s_tx_clkm_div_conf.i2s_tx_clkm_div_y = div_y;
PCR.i2s_tx_clkm_div_conf.i2s_tx_clkm_div_z = div_b;
PCR.i2s_tx_clkm_div_conf.i2s_tx_clkm_div_yn1 = yn1;
PCR.i2s_tx_clkm_conf.i2s_tx_clkm_div_num = div_n;
PCR.i2s_tx_clkm_conf.i2s_tx_clkm_sel = 1;  // PLL_240M_CLK
```

**Sources:** [src/utility/Speaker_Class.cpp:422-489](), [src/utility/Mic_Class.cpp:474-525]()

### Mono Duplication Mode

ESP32-C3, C6, and S3 support automatic mono-to-stereo duplication:

```c++
// For mono output on stereo-capable hardware
if (!stereo && !use_dac && !buzzer) {
    dev->tx_conf.tx_mono = 1;
    dev->tx_conf.tx_chan_equal = 1;
}
```

This sends the same mono sample to both left and right channels, eliminating the need for software duplication.

**Sources:** [src/utility/Speaker_Class.cpp:414-419]()

---

## Wrapper Functions and Unified Interface

M5Unified provides wrapper functions that present a consistent interface regardless of the underlying driver version.

### Operation Wrapper Functions

```mermaid
graph TD
    subgraph "Application Layer"
        AppStart["Application calls<br/>_i2s_start(port)"]
        AppStop["Application calls<br/>_i2s_stop(port)"]
        AppWrite["Application calls<br/>_i2s_write(port, buf, len, ...)"]
        AppRead["Application calls<br/>_i2s_read(port, buf, len, ...)"]
    end
    
    subgraph "Abstraction Layer"
        CheckVersion{{"I2S_DRIVER_VERSION?"}}
    end
    
    subgraph "Driver V2 Implementation"
        V2Start["i2s_channel_enable(_i2s_handle[port])"]
        V2Stop["i2s_channel_disable(_i2s_handle[port])"]
        V2Write["i2s_channel_write(_i2s_handle[port], ...)"]
        V2Read["i2s_channel_read(_i2s_handle[port], ...)"]
    end
    
    subgraph "Driver V1 Implementation"
        V1Start["i2s_start(port)"]
        V1Stop["i2s_stop(port)"]
        V1Write["i2s_write(port, ...)"]
        V1Read["i2s_read(port, ...)"]
    end
    
    AppStart --> CheckVersion
    AppStop --> CheckVersion
    AppWrite --> CheckVersion
    AppRead --> CheckVersion
    
    CheckVersion -->|"Version 2"| V2Start
    CheckVersion -->|"Version 2"| V2Stop
    CheckVersion -->|"Version 2"| V2Write
    CheckVersion -->|"Version 2"| V2Read
    
    CheckVersion -->|"Version 1"| V1Start
    CheckVersion -->|"Version 1"| V1Stop
    CheckVersion -->|"Version 1"| V1Write
    CheckVersion -->|"Version 1"| V1Read
```

### Wrapper Function Implementations

**For New Driver API (v2):**

```c++
static i2s_chan_handle_t _i2s_handle[SOC_I2S_NUM] = { nullptr, };

static esp_err_t _i2s_start(i2s_port_t port) {
    if (_i2s_handle[port] == nullptr) { return ESP_FAIL; }
    return i2s_channel_enable(_i2s_handle[port]);
}

static esp_err_t _i2s_stop(i2s_port_t port) {
    if (_i2s_handle[port] == nullptr) { return ESP_OK; }
    return i2s_channel_disable(_i2s_handle[port]);
}

static esp_err_t _i2s_write(i2s_port_t port, void* buf, size_t len, 
                             size_t* result, TickType_t tick) {
    return i2s_channel_write(_i2s_handle[port], buf, len, result, tick);
}

static esp_err_t _i2s_read(i2s_port_t port, void* buf, size_t len,
                            size_t* result, TickType_t tick) {
    return i2s_channel_read(_i2s_handle[port], buf, len, result, tick);
}
```

**For Legacy Driver API (v1):**

```c++
static esp_err_t _i2s_start(i2s_port_t port) {
    return i2s_start(port);
}

static esp_err_t _i2s_stop(i2s_port_t port) {
    return i2s_stop(port);
}

static esp_err_t _i2s_write(i2s_port_t port, void* buf, size_t len,
                             size_t* result, TickType_t tick) {
    return i2s_write(port, buf, len, result, tick);
}

static esp_err_t _i2s_read(i2s_port_t port, void* buf, size_t len,
                            size_t* result, TickType_t tick) {
    return i2s_read(port, buf, len, result, tick);
}
```

**Sources:** [src/utility/Speaker_Class.cpp:84-106, 146-184](), [src/utility/Mic_Class.cpp:90-112, 221-237]()

### Driver Uninstall

The `_i2s_driver_uninstall()` function also has version-specific implementations:

**New Driver API:**

```c++
static esp_err_t _i2s_driver_uninstall(i2s_port_t port) {
    if (_i2s_handle[port] != nullptr) {
        auto res = i2s_del_channel(_i2s_handle[port]);
        _i2s_handle[port] = nullptr;
        return res;
    }
    return ESP_OK;
}
```

**Legacy Driver API:**

```c++
static esp_err_t _i2s_driver_uninstall(i2s_port_t port) {
    return i2s_driver_uninstall(port);
}
```

This wrapper approach allows the rest of the audio system code (in `spk_task` and `mic_task`) to remain identical across ESP-IDF versions, with all version-specific logic isolated to these wrapper functions.

**Sources:** [src/utility/Speaker_Class.cpp:98-106, 159-162](), [src/utility/Mic_Class.cpp:104-112, 234-237]()

---

## Task Integration

The I2S configuration functions are called from the audio processing tasks:

- **Speaker:** `Speaker_Class::spk_task()` calls `_setup_i2s()` via `begin()` [src/utility/Speaker_Class.cpp:912-946]()
- **Microphone:** `Mic_Class::mic_task()` receives pre-configured I2S from `begin()` [src/utility/Mic_Class.cpp:708-745]()

The tasks then use the wrapper functions (`_i2s_start`, `_i2s_write`, `_i2s_read`, etc.) for all I2S operations during runtime, ensuring consistent behavior across different hardware platforms and ESP-IDF versions.

**Sources:** [src/utility/Speaker_Class.cpp:356-910](), [src/utility/Mic_Class.cpp:422-706]()