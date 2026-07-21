M5Unified Core Architecture

# Core Architecture

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5Unified.cpp](src/M5Unified.cpp)
- [src/M5Unified.hpp](src/M5Unified.hpp)

</details>



## Purpose and Scope

This page provides an architectural overview of the M5Unified library's core design, explaining how the `M5Unified` class acts as a central orchestrator to provide a unified hardware abstraction layer across 19+ M5Stack device variants. This document covers the major subsystems, ownership model, and interaction patterns, but defers detailed implementation specifics to dedicated child pages.

For detailed information about specific aspects:
- System initialization sequence and `M5.begin()` → See [System Initialization and Lifecycle](#2.1)
- Board detection mechanisms → See [Board Detection and Hardware Identification](#2.2)
- GPIO pin assignment strategy → See [Pin Mapping System](#2.3)
- Display management → See [Display Management and M5GFX Integration](#2.4)
- The `M5.update()` loop → See [Main Update Loop and Peripheral Polling](#2.5)

---

## Central Orchestrator Pattern

The M5Unified library centers around a single global instance, `M5`, of type `M5Unified` defined in [src/M5Unified.cpp:45](). This instance serves as the primary interface for all hardware interactions.

```mermaid
graph TB
    subgraph "Global Namespace"
        M5Global["M5<br/>(m5::M5Unified)<br/>Global Instance"]
    end
    
    subgraph "M5Unified Class Structure"
        M5Class["M5Unified Class<br/>src/M5Unified.hpp:80-653"]
        
        subgraph "Public Member Subsystems"
            Display["Display<br/>(M5GFX)"]
            Power["Power<br/>(Power_Class)"]
            Speaker["Speaker<br/>(Speaker_Class)"]
            Mic["Mic<br/>(Mic_Class)"]
            Imu["Imu<br/>(IMU_Class)"]
            Rtc["Rtc<br/>(RTC_Class)"]
            Touch["Touch<br/>(Touch_Class)"]
            Log["Log<br/>(Log_Class)"]
            Led["Led<br/>(LED_Class)"]
            Buttons["BtnA/B/C/EXT/PWR<br/>(Button_Class[5])"]
            I2C["In_I2C / Ex_I2C<br/>(I2C_Class)"]
        end
        
        subgraph "Configuration & State"
            Config["config_t"]
            Board["_board<br/>(board_t)"]
            PinTable["_get_pin_table<br/>(int8_t[pin_name_max])"]
            DisplayVec["_displays<br/>(vector<M5GFX>)"]
        end
    end
    
    M5Global --> M5Class
    M5Class --> Display
    M5Class --> Power
    M5Class --> Speaker
    M5Class --> Mic
    M5Class --> Imu
    M5Class --> Rtc
    M5Class --> Touch
    M5Class --> Log
    M5Class --> Led
    M5Class --> Buttons
    M5Class --> I2C
    M5Class --> Config
    M5Class --> Board
    M5Class --> PinTable
    M5Class --> DisplayVec
```

**Sources:** [src/M5Unified.cpp:45](), [src/M5Unified.hpp:80-653]()

### Ownership Model

The `M5Unified` class directly owns instances of all major subsystem classes as public members. This design provides immediate access to hardware abstractions without requiring pointer dereferencing or getter methods.

| Subsystem | Member Name | Type | Purpose |
|-----------|-------------|------|---------|
| Display | `Display` / `Lcd` | `M5GFX` | Primary display interface |
| Power Management | `Power` | `Power_Class` | Battery, charging, sleep modes |
| Audio Output | `Speaker` | `Speaker_Class` | I2S audio playback |
| Audio Input | `Mic` | `Mic_Class` | I2S audio capture |
| Motion Sensing | `Imu` | `IMU_Class` | Accelerometer, gyroscope, magnetometer |
| Real-Time Clock | `Rtc` | `RTC_Class` | Time/date management |
| Touch Input | `Touch` | `Touch_Class` | Touchscreen interface |
| Logging | `Log` | `Log_Class` | Multi-target logging |
| RGB LED | `Led` | `LED_Class` | Addressable LED control |
| Buttons | `BtnA`, `BtnB`, `BtnC`, `BtnEXT`, `BtnPWR` | `Button_Class` | Hardware button state machines |
| I2C Buses | `In_I2C`, `Ex_I2C` | `I2C_Class&` | Internal and external I2C |

**Sources:** [src/M5Unified.hpp:215-248]()

---

## Multi-Board Abstraction Strategy

The M5Unified architecture achieves hardware abstraction through three coordinated mechanisms:

```mermaid
graph LR
    subgraph "Runtime Detection"
        CheckBoard["_check_boardtype()<br/>src/M5Unified.cpp:971-1418"]
        BoardEnum["board_t enum<br/>(19+ variants)"]
    end
    
    subgraph "Configuration Tables"
        PinTables["Pin Mapping Tables<br/>src/M5Unified.cpp:73-326"]
        SetupPinmap["_setup_pinmap()<br/>src/M5Unified.cpp:328-348"]
        GetPin["getPin(pin_name_t)<br/>Static lookup"]
    end
    
    subgraph "Board-Specific Init"
        SetupI2C["_setup_i2c()<br/>src/M5Unified.cpp:1420-1495"]
        SetupLED["_setup_led()<br/>src/M5Unified.cpp:1496-1532"]
        BeginSPK["_begin_spk()<br/>src/M5Unified.cpp:1743-2304"]
        BeginRTC_IMU["_begin_rtc_imu()<br/>src/M5Unified.cpp:2306-2339"]
    end
    
    CheckBoard --> BoardEnum
    BoardEnum --> SetupPinmap
    SetupPinmap --> PinTables
    PinTables --> GetPin
    BoardEnum --> SetupI2C
    BoardEnum --> SetupLED
    BoardEnum --> BeginSPK
    BoardEnum --> BeginRTC_IMU
```

**Sources:** [src/M5Unified.cpp:971-1418](), [src/M5Unified.cpp:73-326](), [src/M5Unified.cpp:328-348](), [src/M5Unified.cpp:1420-1532](), [src/M5Unified.cpp:1743-2339]()

### Board Detection

At startup, `_check_boardtype()` performs runtime hardware identification through:
- ESP32 package variant detection via `m5gfx::get_pkg_ver()`
- GPIO pull-up/pull-down response testing to identify board variants
- I2C device probing for board-specific peripherals
- Touch sensor capacitance measurements (ESP32 only) to distinguish similar boards

The detected board type is stored in the `_board` member variable of type `board_t`.

**Sources:** [src/M5Unified.cpp:971-1418]()

### Pin Mapping System

After board detection, `_setup_pinmap()` populates the static `_get_pin_table[]` array from compile-time constant tables. This array provides O(1) GPIO pin lookups via the `getPin(pin_name_t)` static method.

Pin mapping tables exist for:
- `_pin_table_i2c_ex_in` - Internal and external I2C buses [src/M5Unified.cpp:73-116]()
- `_pin_table_port_bc` - Port B and Port C connectors [src/M5Unified.cpp:118-139]()
- `_pin_table_port_de` - Port D and Port E connectors [src/M5Unified.cpp:141-154]()
- `_pin_table_spi_sd` - SD card SPI pins [src/M5Unified.cpp:156-176]()
- `_pin_table_other0` - RGB LED pin [src/M5Unified.cpp:178-209]()
- `_pin_table_other1` - Power hold pin [src/M5Unified.cpp:211-231]()
- `_pin_table_mbus` - Module bus pins (30 pins) [src/M5Unified.cpp:233-326]()

**Sources:** [src/M5Unified.cpp:73-348]()

---

## Initialization Lifecycle

The `M5.begin()` method orchestrates system initialization through a carefully ordered sequence:

```mermaid
sequenceDiagram
    participant App as "User Application"
    participant M5 as "M5Unified::begin()"
    participant Display as "Display System"
    participant Detect as "_check_boardtype()"
    participant Pinmap as "_setup_pinmap()"
    participant I2C as "_setup_i2c()"
    participant LED as "_setup_led()"
    participant Begin as "_begin()"
    participant SPK as "_begin_spk()"
    participant Update as "update()"
    participant RTC_IMU as "_begin_rtc_imu()"
    
    App->>M5: M5.begin(config)
    M5->>Display: Display.init()
    Display-->>M5: board_t detected
    M5->>Detect: _check_boardtype()
    Detect-->>M5: Confirmed board_t
    M5->>Pinmap: _setup_pinmap(board)
    Note over Pinmap: Populate _get_pin_table[]
    M5->>I2C: _setup_i2c(board)
    Note over I2C: Configure In_I2C & Ex_I2C
    M5->>LED: _setup_led(board)
    M5->>Begin: _begin(config)
    Note over Begin: Power.begin()<br/>Setup GPIO modes<br/>Serial.begin()
    M5->>SPK: _begin_spk(config)
    Note over SPK: Configure Speaker & Mic<br/>Board-specific callbacks
    M5->>Update: update()
    Note over Update: Initialize button states
    M5->>RTC_IMU: _begin_rtc_imu(config)
    Note over RTC_IMU: Detect RTC & IMU<br/>Load calibration
    M5-->>App: Initialization complete
```

**Sources:** [src/M5Unified.hpp:332-603](), [src/M5Unified.cpp:1534-1741]()

### Initialization Methods

The initialization process is split into multiple private methods, each responsible for a specific subsystem:

| Method | Responsibility | Key Actions |
|--------|---------------|-------------|
| `_check_boardtype()` | Board identification | ESP32 package detection, GPIO tests, I2C probing |
| `_setup_pinmap()` | Pin configuration | Load pin mappings from compile-time tables |
| `_setup_i2c()` | I2C bus setup | Configure `In_I2C` and `Ex_I2C` buses, initialize IO expanders |
| `_setup_led()` | LED initialization | Configure RGB LED driver (RMT or PowerHub protocol) |
| `_begin()` | Core subsystems | Initialize `Power`, set GPIO modes, start serial |
| `_begin_spk()` | Audio subsystems | Configure `Speaker` and `Mic` with board-specific callbacks |
| `_begin_rtc_imu()` | Sensor subsystems | Detect and initialize `Rtc` and `Imu` devices |

**Sources:** [src/M5Unified.cpp:971-2339]()

---

## Runtime Operation

After initialization, the application must call `M5.update()` regularly (typically in the Arduino `loop()` function) to maintain button states and other time-sensitive operations.

```mermaid
graph TB
    subgraph "Application Loop"
        LoopFunc["loop() function"]
    end
    
    subgraph "M5.update() Processing"
        UpdateEntry["M5.update()<br/>src/M5Unified.cpp:2341"]
        UpdateTime["_updateMsec = millis()"]
        TouchUpdate["Touch.update(ms)"]
        GPIORead["Read GPIO registers"]
        IOExpRead["Read IO Expander<br/>(PI4IOE5V6408)"]
        PMICRead["Read PMIC button<br/>(BtnPWR)"]
        
        ButtonA["BtnA.setRawState()"]
        ButtonB["BtnB.setRawState()"]
        ButtonC["BtnC.setRawState()"]
        ButtonEXT["BtnEXT.setRawState()"]
        ButtonPWR["BtnPWR.setRawState()"]
    end
    
    subgraph "Button State Machines"
        BtnLogic["Button_Class<br/>Debounce, Click, Hold<br/>Detection"]
    end
    
    LoopFunc --> UpdateEntry
    UpdateEntry --> UpdateTime
    UpdateTime --> TouchUpdate
    UpdateTime --> GPIORead
    UpdateTime --> IOExpRead
    UpdateTime --> PMICRead
    
    TouchUpdate --> ButtonA
    TouchUpdate --> ButtonB
    TouchUpdate --> ButtonC
    GPIORead --> ButtonA
    GPIORead --> ButtonB
    GPIORead --> ButtonC
    GPIORead --> ButtonEXT
    IOExpRead --> ButtonA
    IOExpRead --> ButtonB
    IOExpRead --> ButtonC
    PMICRead --> ButtonPWR
    
    ButtonA --> BtnLogic
    ButtonB --> BtnLogic
    ButtonC --> BtnLogic
    ButtonEXT --> BtnLogic
    ButtonPWR --> BtnLogic
```

**Sources:** [src/M5Unified.cpp:2341-2699]()

### Update Method Responsibilities

The `update()` method at [src/M5Unified.cpp:2341-2699]() performs these operations:

1. **Timestamp Recording**: Updates `_updateMsec` with current `millis()` value
2. **Touch Processing**: Calls `Touch.update()` if touchscreen is enabled
3. **Touch Button Mapping**: Converts touch coordinates to virtual button presses for Core2/CoreS3/Paper/Tab5
4. **GPIO Sampling**: Reads hardware button states from GPIO registers
5. **IO Expander Reading**: Queries IO expander chips for extended button inputs (StampPLC, UnitC6L, NessoN1, Tab5)
6. **PMIC Button Reading**: Reads power button state from PMIC chips (AXP192/AXP2101)
7. **Button State Updates**: Calls `setRawState()` on all `Button_Class` instances to update their state machines

**Sources:** [src/M5Unified.cpp:2341-2699]()

---

## Subsystem Architecture

Each major subsystem follows a consistent architectural pattern:

```mermaid
graph TB
    subgraph "M5Unified Core"
        M5["M5Unified"]
    end
    
    subgraph "Subsystem Classes"
        Power["Power_Class<br/>PMIC abstraction"]
        Speaker["Speaker_Class<br/>I2S playback"]
        Mic["Mic_Class<br/>I2S capture"]
        IMU["IMU_Class<br/>Sensor fusion"]
        RTC["RTC_Class<br/>Time management"]
        Button["Button_Class<br/>State machine"]
    end
    
    subgraph "Hardware Drivers"
        AXP192["AXP192_Class"]
        AXP2101["AXP2101_Class"]
        IP5306["IP5306_Class"]
        MPU6886["MPU6886_Class"]
        BMI270["BMI270_Class"]
        PCF8563["PCF8563_Class"]
        RX8130["RX8130_Class"]
    end
    
    subgraph "Communication Layer"
        I2CIn["In_I2C<br/>(Internal bus)"]
        I2CExt["Ex_I2C<br/>(Port A)"]
        I2S["I2S Driver<br/>(ESP-IDF)"]
    end
    
    M5 --> Power
    M5 --> Speaker
    M5 --> Mic
    M5 --> IMU
    M5 --> RTC
    M5 --> Button
    
    Power --> AXP192
    Power --> AXP2101
    Power --> IP5306
    IMU --> MPU6886
    IMU --> BMI270
    RTC --> PCF8563
    RTC --> RX8130
    
    Power --> I2CIn
    IMU --> I2CIn
    RTC --> I2CIn
    IMU --> I2CExt
    RTC --> I2CExt
    Speaker --> I2S
    Mic --> I2S
```

**Sources:** [src/M5Unified.hpp:215-248](), [src/M5Unified.cpp:1534-2339]()

### Subsystem Initialization Pattern

Most subsystems follow this initialization pattern:

1. **Configuration**: Define a `config_t` structure with hardware parameters
2. **Board-Specific Setup**: Populate configuration based on detected `_board` type
3. **Callback Registration**: Register board-specific enable/disable callbacks (for Speaker/Mic)
4. **Hardware Detection**: Probe I2C bus for compatible devices
5. **Device Selection**: Instantiate appropriate driver class via polymorphism or runtime switching
6. **State Restoration**: Load calibration or persistent state from NVS (IMU, Power)

**Sources:** [src/M5Unified.cpp:1743-2339]()

---

## Integration with M5GFX

The display subsystem integrates tightly with the external M5GFX library [src/M5Unified.hpp:19]():

```mermaid
graph TB
    subgraph "M5Unified Display Management"
        M5["M5Unified"]
        DisplayPrimary["Display<br/>(M5GFX)<br/>Primary display"]
        DisplaysVec["_displays<br/>(vector<M5GFX>)<br/>All displays"]
        PrimaryIdx["_primary_display_index"]
    end
    
    subgraph "M5GFX Base Class"
        M5GFX["M5GFX<br/>(External library)"]
        Init["init() / init_without_reset()"]
        GetBoard["getBoard()"]
        Drawing["Drawing APIs<br/>(inherited from LGFX_Device)"]
    end
    
    subgraph "Display Selection API"
        AddDisplay["addDisplay(M5GFX&)"]
        GetDisplay["getDisplay(index)"]
        SetPrimary["setPrimaryDisplay(index)"]
        SetPrimaryType["setPrimaryDisplayType(board_list)"]
        GetDisplayIndex["getDisplayIndex(board_t)"]
    end
    
    M5 --> DisplayPrimary
    M5 --> DisplaysVec
    M5 --> PrimaryIdx
    DisplayPrimary --> M5GFX
    DisplaysVec --> M5GFX
    
    M5 --> AddDisplay
    M5 --> GetDisplay
    M5 --> SetPrimary
    M5 --> SetPrimaryType
    M5 --> GetDisplayIndex
    
    AddDisplay --> DisplaysVec
    SetPrimary --> PrimaryIdx
    GetDisplay --> DisplaysVec
```

**Sources:** [src/M5Unified.hpp:215-216](), [src/M5Unified.hpp:257-286]()

### Multi-Display Support

M5Unified supports multiple displays simultaneously through a vector-based architecture:

- **Display Registration**: Displays are added to `_displays` vector via `addDisplay()` [src/M5Unified.hpp:263]()
- **Primary Display**: The `Display` member references the active display for drawing operations
- **Display Iteration**: Access individual displays via `getDisplay(index)` or `Displays(index)`
- **Type-Based Selection**: Use `setPrimaryDisplayType()` to select by board type (e.g., prioritizing external displays)

This architecture enables configurations like:
- M5Stack Core + Module Display (dual display)
- M5Atom + Atom Display attachment
- M5Stack Core + Unit OLED (external I2C display)

**Sources:** [src/M5Unified.hpp:215-216](), [src/M5Unified.hpp:257-286](), [src/M5Unified.hpp:332-603]()

---

## Configuration System

The `config_t` structure [src/M5Unified.hpp:83-213]() provides compile-time defaults with runtime overrides:

| Configuration Category | Purpose | Default Behavior |
|------------------------|---------|------------------|
| `serial_baudrate` | Arduino Serial initialization | 0 (disabled) |
| `clear_display` | Clear screen at startup | `true` |
| `output_power` | 5V output to external ports | `true` |
| `internal_*` flags | Enable built-in peripherals | All `true` except `internal_mic` varies by board |
| `external_*` flags | Enable external peripherals | `false` (opt-in) |
| `external_speaker.*` | External speaker detection flags | `0x00` (disabled) |
| `external_display.*` | External display detection flags | `0xFFFF` (all enabled) |
| `fallback_board` | Board type if detection fails | Varies by ESP32 variant |
| `led_brightness` | System LED brightness | 0 (off) |

**Sources:** [src/M5Unified.hpp:83-213]()

---

## Static Pin Table Architecture

The pin mapping system uses a static lookup table to provide fast GPIO pin access without board conditionals in user code:

```mermaid
graph LR
    subgraph "Pin Name Enumeration"
        PinEnum["pin_name_t enum<br/>src/M5Unified.hpp:26-53"]
        Examples["in_i2c_scl<br/>ex_i2c_sda<br/>port_a_pin1<br/>sd_spi_sclk<br/>rgb_led<br/>power_hold<br/>mbus_pin1-30"]
    end
    
    subgraph "Static Storage"
        GetPinTable["_get_pin_table[]<br/>static int8_t[pin_name_max]<br/>src/M5Unified.cpp:62"]
    end
    
    subgraph "Public API"
        GetPin["M5.getPin(pin_name_t)<br/>Returns: int8_t GPIO number"]
    end
    
    PinEnum --> GetPin
    GetPin --> GetPinTable
    Examples --> PinEnum
```

**Usage Example:**
```cpp
// Get the I2C SDA pin for external devices (Port A)
int8_t sda_pin = M5.getPin(m5::pin_name_t::ex_i2c_sda);

// Get SD card CS pin
int8_t sd_cs = M5.getPin(m5::pin_name_t::sd_spi_cs);

// Get RGB LED pin
int8_t led_pin = M5.getPin(m5::pin_name_t::rgb_led);
```

**Sources:** [src/M5Unified.hpp:26-53](), [src/M5Unified.hpp:251](), [src/M5Unified.cpp:62](), [src/M5Unified.cpp:328-348]()

---

## Summary

The M5Unified core architecture achieves its goal of hardware abstraction through:

1. **Centralized Orchestration**: The global `M5` instance provides a single entry point for all hardware access
2. **Direct Subsystem Ownership**: All major peripherals are accessible as public members (e.g., `M5.Power`, `M5.Speaker`)
3. **Runtime Board Detection**: Automatic hardware identification through GPIO testing and I2C probing
4. **Static Pin Mapping**: Fast GPIO lookups via pre-populated tables indexed by symbolic names
5. **Polymorphic Drivers**: Hardware-specific implementations selected at runtime based on detected board type
6. **Ordered Initialization**: Dependencies respected through carefully sequenced initialization methods
7. **Regular Update Loop**: Application-driven polling via `M5.update()` for time-sensitive operations

This architecture enables a single compiled binary to support 19+ M5Stack device variants while maintaining optimal performance and a clean, consistent API surface.

**Sources:** [src/M5Unified.hpp:80-653](), [src/M5Unified.cpp:45](), [src/M5Unified.cpp:328-2699]()