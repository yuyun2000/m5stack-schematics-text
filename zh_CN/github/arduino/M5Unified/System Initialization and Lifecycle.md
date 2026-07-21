M5Unified System Initialization and Lifecycle

# System Initialization and Lifecycle

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5Unified.cpp](src/M5Unified.cpp)
- [src/M5Unified.hpp](src/M5Unified.hpp)

</details>



## Purpose and Scope

This page documents the complete initialization process executed by `M5.begin()` and the subsequent runtime lifecycle of M5Unified applications. It covers the ordered sequence of hardware detection, configuration, and subsystem initialization that prepares M5Stack devices for use.

**Related pages:**
- For hardware identification details, see [Board Detection and Hardware Identification](#2.2)
- For GPIO assignment tables, see [Pin Mapping System](#2.3)
- For display setup specifics, see [Display Management and M5GFX Integration](#2.4)
- For runtime operation, see [Main Update Loop and Peripheral Polling](#2.5)

## Overview

M5Unified follows a strictly ordered, single-pass initialization sequence that:

1. Prevents multiple initialization attempts (begin-once guarantee)
2. Detects the board type at runtime
3. Configures hardware-specific pin mappings
4. Initializes communication buses (I2C, SPI)
5. Sets up peripheral subsystems (Power, Audio, Display, Sensors)
6. Prepares the system for the main application loop

The entire process is orchestrated by the `M5Unified::begin()` method, which delegates to several internal initialization methods.

**Sources:** [src/M5Unified.hpp:332-603](), [src/M5Unified.cpp:1534-1741]()

## Configuration Structure

The `config_t` structure controls initialization behavior. Key configuration fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `serial_baudrate` | uint32_t | 0 | Serial port baud rate (0=disabled) |
| `clear_display` | bool | true | Clear screen during initialization |
| `output_power` | bool | true | Enable 5V output to external ports |
| `pmic_button` | bool | true | Use PMIC button for BtnPWR |
| `internal_imu` | bool | true | Initialize internal IMU |
| `internal_rtc` | bool | true | Initialize internal RTC |
| `internal_mic` | bool | true | Initialize microphone |
| `internal_spk` | bool | true | Initialize speaker |
| `external_imu` | bool | false | Detect external IMU on Port A |
| `external_rtc` | bool | false | Detect external RTC on Port A |
| `led_brightness` | uint8_t | 0 | System LED brightness (0-255) |
| `fallback_board` | board_t | (varies) | Board type if auto-detection fails |

**Sources:** [src/M5Unified.hpp:83-213]()

## Initialization Entry Point

```mermaid
graph TB
    App["Application Code"]
    Begin1["M5.begin()"]
    Begin2["M5.begin(config_t)"]
    Guard["Check _board != board_unknown"]
    Init["Initialization Sequence"]
    Return["Return to Application"]
    
    App --> Begin1
    App --> Begin2
    Begin1 --> |"Creates default config_t"| Begin2
    Begin2 --> Guard
    Guard --> |"Already initialized"| Return
    Guard --> |"First call"| Init
    Init --> Return
    
    style Begin2 fill:#ffcccc
    style Guard fill:#ccccff
```

**Sources:** [src/M5Unified.hpp:323-327](), [src/M5Unified.hpp:332-603]()

The `begin()` method guarantees single execution through the board type check at [src/M5Unified.hpp:335](). If `_board != board_unknown`, the method returns immediately, preventing re-initialization.

## Power Hold Pin (ESP32-S3)

On ESP32-S3 devices (Capsule, Dial, DinMeter), GPIO46 must be set HIGH before any initialization to maintain power:

```mermaid
graph LR
    Start["begin() Entry"] --> Check["#ifdef CONFIG_IDF_TARGET_ESP32S3"]
    Check --> |"S3 Detected"| SetHigh["gpio_hi(GPIO_NUM_46)"]
    SetHigh --> SetOutput["pinMode(46, output)"]
    SetOutput --> Continue["Continue Initialization"]
    Check --> |"Other MCU"| Continue
```

**Sources:** [src/M5Unified.hpp:337-341]()

This prevents the device from powering down during initialization. The operation is MCU-specific and occurs before any other initialization steps.

## Master Initialization Sequence

```mermaid
sequenceDiagram
    participant App as Application
    participant Begin as begin(config_t)
    participant Display as M5GFX Display
    participant Check as _check_boardtype()
    participant Setup as Setup Methods
    participant Internal as _begin()
    participant Audio as _begin_spk()
    participant Update as update()
    participant Sensors as _begin_rtc_imu()
    participant ExtDisp as External Displays
    
    App->>Begin: M5.begin(cfg)
    
    Note over Begin: Save original brightness
    Begin->>Display: setBrightness(0)
    
    alt cfg.clear_display
        Begin->>Display: init()
    else
        Begin->>Display: init_without_reset(false)
    end
    
    Begin->>Check: _check_boardtype(Display.getBoard())
    Check-->>Begin: board_t detected
    
    Note over Begin: Apply fallback if unknown
    
    Begin->>Setup: _setup_pinmap(board)
    Begin->>Setup: _setup_i2c(board)
    Begin->>Setup: _setup_led(board)
    Begin->>Begin: addDisplay(Display)
    
    Begin->>Internal: _begin(cfg)
    Note over Internal: Power, GPIO, Serial
    
    Begin->>Audio: _begin_spk(cfg)
    Note over Audio: Speaker/Mic config
    
    Begin->>Update: update()
    Note over Update: Initialize button states
    
    Begin->>Sensors: _begin_rtc_imu(cfg)
    Note over Sensors: RTC and IMU setup
    
    Begin->>ExtDisp: External display detection
    Note over ExtDisp: Module/Unit displays
    
    Begin->>Display: setBrightness(original)
    Begin-->>App: Initialization complete
```

**Sources:** [src/M5Unified.hpp:332-603]()

## Display Initialization Phase

The display initializes first to enable board detection through hardware probing:

```mermaid
graph TB
    SaveBright["Save Display.getBrightness()"]
    SetZero["Display.setBrightness(0)"]
    CheckClear{"cfg.clear_display?"}
    InitReset["Display.init()"]
    InitNoReset["Display.init_without_reset(false)"]
    GetBoard["Display.getBoard()"]
    CheckBoard["_check_boardtype(board)"]
    
    SaveBright --> SetZero
    SetZero --> CheckClear
    CheckClear --> |"true"| InitReset
    CheckClear --> |"false"| InitNoReset
    InitReset --> GetBoard
    InitNoReset --> GetBoard
    GetBoard --> CheckBoard
    
    style CheckClear fill:#ccccff
```

**Sources:** [src/M5Unified.hpp:343-351]()

The brightness is set to zero to prevent display flicker during initialization, then restored at [src/M5Unified.hpp:599-602]() after all setup is complete.

**Board detection flow:**
1. Display attempts hardware identification through GPIO/I2C probes
2. `Display.getBoard()` returns tentative board type
3. `_check_boardtype()` performs additional verification
4. If `board_unknown`, `cfg.fallback_board` is used

**Sources:** [src/M5Unified.hpp:351-354]()

## Configuration Phase

After board detection, three setup methods configure hardware-specific resources:

```mermaid
graph LR
    Board["board_t detected"]
    PinMap["_setup_pinmap(board)"]
    I2CSetup["_setup_i2c(board)"]
    LEDSetup["_setup_led(board)"]
    
    Board --> PinMap
    Board --> I2CSetup
    Board --> LEDSetup
    
    PinMap --> |"Loads pin tables"| PinTable["_get_pin_table[]"]
    I2CSetup --> |"Configures"| I2C["In_I2C, Ex_I2C"]
    LEDSetup --> |"Initializes"| LED["Led instance"]
```

**Sources:** [src/M5Unified.hpp:355-357]()

These methods are detailed in:
- Pin mapping: See [Pin Mapping System](#2.3)
- I2C setup: [src/M5Unified.cpp:1420-1495]()
- LED setup: [src/M5Unified.cpp:1496-1532]()

## Internal Hardware Initialization (_begin)

The `_begin()` method [src/M5Unified.cpp:1534-1741]() initializes core hardware:

```mermaid
graph TB
    Entry["_begin(cfg)"]
    PowerBegin["Power.begin()"]
    PowerOut["Power.setExtOutput(cfg.output_power)"]
    LED["Set LED brightness"]
    PMICCheck{"PMIC Type?"}
    PMICBtn["Configure PMIC button"]
    ClearDisp{"cfg.clear_display?"}
    DispClear["Display.clear()"]
    BoardSwitch{"Switch on _board"}
    GPIOSetup["Board-specific GPIO setup"]
    Serial{"cfg.serial_baudrate != 0?"}
    SerialBegin["Serial.begin()"]
    
    Entry --> PowerBegin
    PowerBegin --> PowerOut
    PowerOut --> LED
    LED --> PMICCheck
    PMICCheck --> |"AXP192/AXP2101/PY32"| PMICBtn
    PMICCheck --> |"Other"| ClearDisp
    PMICBtn --> ClearDisp
    ClearDisp --> |"true"| DispClear
    ClearDisp --> |"false"| BoardSwitch
    DispClear --> BoardSwitch
    BoardSwitch --> GPIOSetup
    GPIOSetup --> Serial
    Serial --> |"Arduino && enabled"| SerialBegin
    Serial --> |"disabled"| End["Return"]
    SerialBegin --> End
    
    style PowerBegin fill:#ffcccc
    style BoardSwitch fill:#ccccff
```

**Sources:** [src/M5Unified.cpp:1534-1741]()

### Power Management Initialization

Power initialization occurs first and is critical:

```cpp
Power.begin();                      // Auto-detect and initialize PMIC
Power.setExtOutput(cfg.output_power); // Control external port power
if (cfg.led_brightness) {
    Power.setLed(cfg.led_brightness); // System status LED
}
```

**Sources:** [src/M5Unified.cpp:1536-1542]()

For PMIC details, see [Power Management System](#3).

### PMIC Button Configuration

If an AXP192, AXP2101, or PY32PMIC is detected:

```cpp
auto pmic_type = Power.getType();
if (pmic_type == pmic_axp2101 || pmic_type == pmic_axp192 || pmic_type == pmic_py32pmic) {
    _use_pmic_button = cfg.pmic_button;
    BtnPWR.setHoldThresh(BtnPWR.getHoldThresh() * 1.2);
}
```

**Sources:** [src/M5Unified.cpp:1543-1551]()

The hold threshold is extended by 20% to accommodate the AXP192's longer button detection time.

### Board-Specific GPIO Setup

Different boards require specific GPIO configurations:

| Board | GPIO Configuration | Purpose |
|-------|-------------------|---------|
| M5Stack | GPIO15 LOW, SPI pins high-drive | WiFi sensitivity, SD speed |
| StickC/Atom | GPIO0 HIGH output | CH552 overvoltage prevention |
| CoreInk | GPIO5, GPIO27 input | Button pins |
| StampC3 | GPIO3 input pullup | Button pin |
| StickS3 | I2C PMIC GPIO3 config | PA control pin |

**Sources:** [src/M5Unified.cpp:1559-1730]()

## Audio Configuration (_begin_spk)

Audio setup [src/M5Unified.cpp:1743-2304]() is complex due to board-specific codecs and external peripherals:

```mermaid
graph TB
    Entry["_begin_spk(cfg)"]
    MicCfg["Configure mic_cfg defaults"]
    SpkCfg["Configure spk_cfg defaults"]
    
    CheckMic{"cfg.internal_mic?"}
    MicBoard{"Switch on _board"}
    MicSetup["Board-specific mic pins"]
    MicCallback["Set mic enable callback"]
    
    CheckSpk{"cfg.internal_spk?"}
    SpkBoard{"Switch on _board"}
    SpkSetup["Board-specific speaker pins"]
    SpkCallback["Set speaker enable callback"]
    
    ExtSpk{"cfg.external_speaker_value?"}
    ExtDetect["Detect external speakers"]
    ExtConfig["Configure for external"]
    
    ApplyMic["Mic.config(mic_cfg)"]
    ApplySpk["Speaker.config(spk_cfg)"]
    
    Entry --> MicCfg
    Entry --> SpkCfg
    MicCfg --> CheckMic
    CheckMic --> |"true"| MicBoard
    MicBoard --> MicSetup
    MicSetup --> MicCallback
    
    SpkCfg --> CheckSpk
    CheckSpk --> |"true"| SpkBoard
    SpkBoard --> SpkSetup
    SpkSetup --> SpkCallback
    
    SpkCallback --> ExtSpk
    MicCallback --> ExtSpk
    ExtSpk --> |"enabled"| ExtDetect
    ExtDetect --> ExtConfig
    ExtConfig --> ApplyMic
    ExtSpk --> |"disabled"| ApplyMic
    ApplyMic --> ApplySpk
    
    style MicBoard fill:#ccffcc
    style SpkBoard fill:#ccffcc
    style ExtDetect fill:#ffffcc
```

**Sources:** [src/M5Unified.cpp:1743-2304]()

### Microphone Configuration Examples

**CoreS3 (ES7210 codec):**
```cpp
mic_cfg.pin_mck = GPIO_NUM_0;
mic_cfg.pin_bck = GPIO_NUM_34;
mic_cfg.pin_ws = GPIO_NUM_33;
mic_cfg.pin_data_in = GPIO_NUM_14;
mic_cfg.i2s_port = I2S_NUM_1;
mic_cfg.input_channel = input_channel_t::input_stereo;
mic_enable_cb = _microphone_enabled_cb_cores3;
```

**Sources:** [src/M5Unified.cpp:1775-1788]()

**StickC (PDM microphone with AXP192 LDO control):**
```cpp
mic_cfg.pin_data_in = GPIO_NUM_34;
mic_cfg.pin_ws = GPIO_NUM_0;
mic_enable_cb = _microphone_enabled_cb_stickc;
```

**Sources:** [src/M5Unified.cpp:1849-1855]()

### Speaker Configuration Examples

**CoreS3 (AW88298 amplifier):**
```cpp
spk_cfg.pin_bck = GPIO_NUM_34;
spk_cfg.pin_ws = GPIO_NUM_33;
spk_cfg.pin_data_out = GPIO_NUM_13;
spk_cfg.magnification = 4;
spk_cfg.i2s_port = I2S_NUM_1;
spk_enable_cb = _speaker_enabled_cb_cores3;
```

**Sources:** [src/M5Unified.cpp:1931-1942]()

The callback functions handle codec-specific initialization via I2C register writes.

### External Speaker Detection

For ATOM-series devices, external speakers are detected through GPIO probing:

```mermaid
graph TB
    Check["Check cfg.external_speaker"]
    Probe["GPIO pulldown test"]
    CheckAtomic{"GPIOs all HIGH?"}
    SetAtomic["Configure ATOMIC SPK"]
    CheckEcho{"!flg_atomic_spk?"}
    SetEcho["Configure ATOMIC ECHO"]
    Done["Continue"]
    
    Check --> Probe
    Probe --> CheckAtomic
    CheckAtomic --> |"Yes"| SetAtomic
    SetAtomic --> Done
    CheckAtomic --> |"No"| CheckEcho
    CheckEcho --> |"Yes"| SetEcho
    CheckEcho --> |"No"| Done
    SetEcho --> Done
```

**Sources:** [src/M5Unified.cpp:1973-2016]() (ESP32-S3), [src/M5Unified.cpp:2188-2245]() (ESP32)

## First Update Cycle

Immediately after audio configuration, `update()` is called to initialize button states:

```cpp
update();  // Initialize button state machines
```

**Sources:** [src/M5Unified.hpp:407]()

This ensures button states are valid before user code executes. The update process is detailed in [Main Update Loop and Peripheral Polling](#2.5).

## Sensor Initialization (_begin_rtc_imu)

RTC and IMU initialization [src/M5Unified.cpp:2306-2339]() attempts internal then external detection:

```mermaid
sequenceDiagram
    participant Begin as _begin_rtc_imu()
    participant ExI2C as Ex_I2C (Port A)
    participant InI2C as In_I2C (Internal)
    participant RTC as Rtc
    participant IMU as Imu
    participant System as System Time
    
    alt cfg.external_rtc || cfg.external_imu
        Begin->>ExI2C: Ex_I2C.begin()
    end
    
    alt cfg.internal_rtc
        Begin->>RTC: Rtc.begin(&In_I2C, board)
    end
    
    alt !Rtc.isEnabled() && cfg.external_rtc
        Begin->>RTC: Rtc.begin(&Ex_I2C)
        Note over Begin: Sets port_a_used flag
    end
    
    alt Rtc.isEnabled()
        Begin->>System: Rtc.setSystemTimeFromRtc()
        alt cfg.disable_rtc_irq
            Begin->>RTC: Rtc.disableIRQ()
        end
    end
    
    alt cfg.internal_imu
        Begin->>IMU: Imu.begin(&In_I2C, board)
    end
    
    alt !Imu.isEnabled() && cfg.external_imu
        Begin->>IMU: Imu.begin(&Ex_I2C)
        Note over Begin: Sets port_a_used flag
    end
    
    Begin-->>Begin: return port_a_used
```

**Sources:** [src/M5Unified.cpp:2306-2339]()

### Port A Usage Tracking

The `port_a_used` flag prevents certain external displays (like UnitRCA on ATOM) from initializing when Port A is occupied by sensors:

```cpp
bool port_a_used = _begin_rtc_imu(cfg);
// Later used to prevent UnitRCA on ATOM when Port A has sensors
```

**Sources:** [src/M5Unified.hpp:409](), [src/M5Unified.hpp:579-585]()

## External Display Detection

After internal hardware initialization, external displays are probed:

```mermaid
graph TB
    Check{"cfg.external_display_value?"}
    UnitOLED["M5UnitOLED"]
    UnitMiniOLED["M5UnitMiniOLED"]
    UnitGlass["M5UnitGLASS"]
    UnitGlass2["M5UnitGLASS2"]
    UnitLCD["M5UnitLCD"]
    ModuleRCA["M5ModuleRCA"]
    UnitRCA["M5UnitRCA"]
    Add["addDisplay()"]
    
    Check --> |"Enabled flags"| UnitOLED
    Check --> UnitMiniOLED
    Check --> UnitGlass
    Check --> UnitGlass2
    Check --> UnitLCD
    Check --> ModuleRCA
    Check --> UnitRCA
    
    UnitOLED --> |"if init() success"| Add
    UnitMiniOLED --> |"if init() success"| Add
    UnitGlass --> |"if init() success"| Add
    UnitGlass2 --> |"if init() success"| Add
    UnitLCD --> |"if init() success"| Add
    ModuleRCA --> |"if init() success"| Add
    UnitRCA --> |"if init() success"| Add
```

**Sources:** [src/M5Unified.hpp:422-597]()

Each display type has conditional compilation guards and board compatibility checks. I2C pins default to Ex_I2C configuration if not explicitly set.

## Post-Initialization State

After `begin()` returns, the system is in the runtime state:

```mermaid
stateDiagram-v2
    [*] --> Uninitialized
    Uninitialized --> Initializing: M5.begin()
    Initializing --> BoardDetection
    BoardDetection --> PinConfig
    PinConfig --> PowerInit
    PowerInit --> DisplayInit
    DisplayInit --> AudioInit
    AudioInit --> SensorInit
    SensorInit --> Runtime
    Runtime --> Runtime: M5.update()
    Runtime --> [*]: Application ends
    
    note right of Runtime
        All hardware ready
        update() polls inputs
        Subsystems operational
    end note
```

**Key state at runtime:**
- `_board` contains detected/fallback board type
- `_displays` vector contains all registered displays
- Display brightness restored to original value
- All button state machines initialized
- Power management active
- Audio, RTC, IMU ready (if configured)

**Sources:** [src/M5Unified.hpp:332-603]()

## Initialization Ordering Rationale

The initialization order is carefully designed to satisfy dependencies:

| Phase | Rationale |
|-------|-----------|
| **Power Hold** | ESP32-S3 devices require this immediately or they power down |
| **Display Init** | Needed for board detection hardware probes |
| **Board Detection** | Determines all subsequent hardware configuration |
| **Pin Mapping** | Provides GPIO numbers for all other subsystems |
| **I2C Setup** | Required by Power, RTC, IMU, Audio codecs |
| **Power Init** | Enables voltage rails needed by other peripherals |
| **Audio Config** | Uses I2C, may depend on external power |
| **First Update** | Initializes button states before user code |
| **Sensors** | Uses I2C, may conflict with audio if not ordered properly |
| **External Displays** | Uses external power, requires complete I2C setup |

**Sources:** [src/M5Unified.hpp:332-603]()

## Runtime Lifecycle

After initialization, applications enter the main loop:

```mermaid
graph LR
    Init["M5.begin()"]
    Setup["User setup()"]
    Loop["User loop()"]
    Update["M5.update()"]
    UserCode["Application logic"]
    
    Init --> Setup
    Setup --> Loop
    Loop --> Update
    Update --> UserCode
    UserCode --> Loop
```

The `update()` method must be called regularly (typically at the start of `loop()`) to:
- Read button/touch inputs
- Update button state machines
- Maintain PMIC communication
- Service other time-critical tasks

**Sources:** [src/M5Unified.cpp:2341-2683]()

For details on the update cycle, see [Main Update Loop and Peripheral Polling](#2.5).