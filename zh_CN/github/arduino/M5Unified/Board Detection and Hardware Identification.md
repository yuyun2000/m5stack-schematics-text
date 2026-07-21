M5Unified Board Detection and Hardware Identification

# Board Detection and Hardware Identification

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5Unified.cpp](src/M5Unified.cpp)
- [src/M5Unified.hpp](src/M5Unified.hpp)

</details>



## Purpose and Scope

This document describes the board detection and hardware identification mechanism in M5Unified, which automatically determines which M5Stack device is running the code at runtime. This detection occurs during the `M5.begin()` initialization sequence and enables a single compiled binary to work across 19+ different M5Stack hardware variants without modification.

For information about pin mapping configuration that follows board detection, see [Pin Mapping System](#2.3). For the overall initialization sequence, see [System Initialization and Lifecycle](#2.1).

---

## Detection Architecture Overview

The board detection system is implemented primarily in the `_check_boardtype()` method, which employs a multi-strategy approach to identify hardware. The detection result is stored in the `_board` member variable (type `board_t`) and used throughout the initialization process to configure board-specific features.

```mermaid
graph TB
    begin["M5.begin(config)"]
    display_init["Display.init()"]
    check_board["_check_boardtype(board)"]
    fallback{"board ==<br/>board_unknown?"}
    set_board["_board = detected board"]
    use_fallback["_board = config.fallback_board"]
    pinmap["_setup_pinmap(_board)"]
    i2c["_setup_i2c(_board)"]
    
    begin --> display_init
    display_init --> check_board
    check_board --> fallback
    fallback -->|"Yes"| use_fallback
    fallback -->|"No"| set_board
    use_fallback --> pinmap
    set_board --> pinmap
    pinmap --> i2c
    
    style check_board fill:#f9f9f9,stroke:#333,stroke-width:2px
    style fallback fill:#f9f9f9,stroke:#333,stroke-width:2px
```

**Detection Flow in M5.begin()**

Sources: [src/M5Unified.hpp:332-360](), [src/M5Unified.cpp:971-1418]()

---

## Detection Strategies

The `_check_boardtype()` method uses different detection strategies depending on the ESP32 variant. Each strategy is optimized for the hardware capabilities and physical characteristics of different board families.

### Strategy 1: ESP32 Package Version Detection

On the original ESP32 (non-S3/C3/C6/P4), the system reads the ESP32 package type from eFuse registers to perform coarse-grained board identification.

```mermaid
graph LR
    subgraph "ESP32 Original"
        pkg["m5gfx::get_pkg_ver()"]
        cases["Switch on package type"]
        
        pkg --> cases
        
        cases --> D0WDQ6["EFUSE_RD_CHIP_VER_PKG_ESP32D0WDQ6<br/>→ board_M5TimerCam"]
        cases --> PICOD4["EFUSE_RD_CHIP_VER_PKG_ESP32PICOD4<br/>→ GPIO pattern test"]
        cases --> PICOV3["Package 6 (PICOV3_02)<br/>→ board_M5AtomPsram"]
        cases --> DEFAULT["default<br/>→ Check Arduino defines"]
        
        PICOD4 --> GPIO_TEST["GPIO 2,13,19,22,27,33,34<br/>pullup/pulldown tests"]
        GPIO_TEST --> TOUCH["Touch sensor test on G27"]
        TOUCH --> MATRIX_LITE["Distinguish AtomMatrix<br/>vs AtomLite/Echo"]
        
        GPIO_TEST --> G19_22_33["G19,G22,G33 I2S test"]
        G19_22_33 --> ECHO["Detect AtomEcho<br/>vs AtomLite"]
    end
```

**ESP32 Package-Based Detection Logic**

Sources: [src/M5Unified.cpp:971-1114]()

The GPIO pattern test performs the following operations:
1. Backup GPIO states for pins 2, 13, 19, 22, 27, 33, 34
2. Configure pins as input with pullup/pulldown
3. Read pin states to identify board characteristics
4. Restore GPIO states after detection

For the AtomMatrix vs AtomLite distinction, the code uses capacitive touch sensing on GPIO27 (the RGB LED pin). The AtomMatrix has a different capacitance profile due to its 25-LED matrix compared to the single LED on AtomLite/Echo.

Sources: [src/M5Unified.cpp:985-1066]()

### Strategy 2: GPIO Pull Test Patterns

For ESP32-S3 devices, the system uses GPIO pull resistance tests to identify boards. This method leverages the fact that different boards have different external circuitry connected to specific GPIOs.

```mermaid
graph TB
    subgraph "ESP32-S3 Detection (QFN56 Package)"
        start["Package == 0 (QFN56)"]
        backup["Backup GPIO 4,8,10,12,38"]
        pulldown["Set GPIOs to pulldown"]
        pullup["Set G4,G12,G38 to pullup"]
        read["Read G8,G10,G4,G12,G38"]
        pattern["Analyze 5-bit pattern"]
        
        start --> backup
        backup --> pulldown
        pulldown --> pullup
        pullup --> read
        read --> pattern
        
        pattern --> STAMPS3["G38=0 after delay<br/>→ M5StampS3"]
        pattern --> ATOMS3LITE["G4=0, G38=1<br/>→ M5AtomS3Lite"]
        pattern --> ATOMS3U["G4=1, G38=1<br/>→ M5AtomS3U"]
        
        STAMPS3 --> CAPSULE_TEST["G8,G10 == 0b11?"]
        CAPSULE_TEST -->|"Yes"| CAPSULE["M5Capsule<br/>+ I2C STOP on G15,G13"]
        CAPSULE_TEST -->|"No"| STAMPS3_FINAL["M5StampS3"]
    end
    
    subgraph "PowerHub Detection"
        powerhub_start["Unknown after GPIO test"]
        i2c_manual["Manual I2C bit-bang<br/>on GPIO 48,45"]
        probe_0x50["Probe address 0x50"]
        ack_check["Check for ACK"]
        
        powerhub_start --> i2c_manual
        i2c_manual --> probe_0x50
        probe_0x50 --> ack_check
        ack_check -->|"ACK"| POWERHUB["M5PowerHub"]
    end
```

**ESP32-S3 GPIO Pattern Detection**

The StampS3 detection exploits a hardware characteristic: GPIO38 is connected to an SGM2578 power management chip that pulls the line low. On AtomS3Lite/U, GPIO38 is unconnected and remains high when configured as input with pullup.

Similarly, GPIO4 distinguishes AtomS3Lite (infrared receiver pulls it low) from AtomS3U (unconnected, remains high).

Sources: [src/M5Unified.cpp:1116-1192]()

### Strategy 3: I2C Device Probing

Some boards require active I2C communication to identify them. This is done by bit-banging I2C protocol directly using GPIO manipulation.

```mermaid
sequenceDiagram
    participant Code as _check_boardtype()
    participant GPIO as GPIO Registers
    participant Device as I2C Device
    
    Note over Code,Device: PowerHub Detection Example
    
    Code->>GPIO: Configure G48 as SCL output LOW
    Code->>GPIO: Configure G45 as SDA output LOW
    Code->>Code: delay(50ms) for power stabilization
    
    loop I2C Transaction
        Code->>GPIO: SDA LOW (START condition)
        loop 8 address bits + 1 ACK bit
            Code->>GPIO: SCL HIGH
            Code->>Code: delay(1ms)
            Code->>GPIO: SCL LOW
            Code->>Code: delay(1ms)
            alt ACK bit cycle
                Code->>GPIO: SDA INPUT (release for ACK)
                GPIO->>Code: Read SDA state
                Note over Code: nack = GPIO.read(SDA)
            else Data bit cycle
                Code->>GPIO: SDA = address bit
            end
        end
        Code->>GPIO: SDA HIGH (STOP condition)
    end
    
    Code->>Code: result = nack ? not_found : found
    alt result == found
        Code->>Code: _board = board_M5PowerHub
    end
```

**I2C Bit-Bang Detection Sequence**

The bit-bang I2C implementation manually toggles SCL and SDA pins to communicate without initializing the I2C peripheral. This is necessary during early boot when I2C may not be configured yet.

Key addresses probed:
- `0x50` (7-bit) → PowerHub
- `0x18` (7-bit) → AtomEchoS3R (ES8311 codec)
- `0x3C` (7-bit) → AtomS3RCam (OV3660 camera)
- `0x21` (7-bit) → AtomS3RCam (GC0308 camera)

Sources: [src/M5Unified.cpp:1194-1248]() (PowerHub), [src/M5Unified.cpp:1253-1305]() (AtomEchoS3R), [src/M5Unified.cpp:1307-1378]() (AtomS3RCam)

### Strategy 4: Touch Sensor Capacitance Testing

On ESP32 (original), the touch sensor peripheral can measure capacitance to distinguish boards with different physical layouts.

```mermaid
graph TB
    subgraph "Touch Sensor Detection Logic"
        init["touch_pad_init()"]
        config["Configure TOUCH_PAD_NUM4 (G13)<br/>Configure TOUCH_PAD_NUM7 (G27)"]
        read["Read capacitance values"]
        compare["diff = results[1]*3 - results[0]"]
        decide{"diff >= 0?"}
        
        init --> config
        config --> read
        read --> compare
        compare --> decide
        
        decide -->|"Yes (higher capacitance)"| LITE["AtomLite or AtomEcho"]
        decide -->|"No (lower capacitance)"| MATRIX["AtomMatrix"]
        
        LITE --> I2S_TEST["Test G19,G22,G33 pullup"]
        I2S_TEST --> ECHO_CHECK{"All pins pull low<br/>quickly?"}
        ECHO_CHECK -->|"Yes"| ECHO["AtomEcho<br/>(I2S speaker pins)"]
        ECHO_CHECK -->|"No"| LITE_FINAL["AtomLite"]
    end
    
    style decide fill:#f9f9f9,stroke:#333,stroke-width:2px
    style ECHO_CHECK fill:#f9f9f9,stroke:#333,stroke-width:2px
```

**Touch Sensor Detection for Atom Series**

The AtomMatrix has a 5×5 LED matrix (25 LEDs) connected to GPIO27, while AtomLite has only one LED. This difference in load capacitance is detectable through the ESP32's capacitive touch sensor peripheral. The code reads both GPIO13 (NC, reference) and GPIO27 (LED) to compute a differential measurement that's robust to environmental variations.

Sources: [src/M5Unified.cpp:827-883]() (touch reading function), [src/M5Unified.cpp:994-1061]() (AtomMatrix detection)

---

## Board Type Enumeration

The detected board type is stored as a `board_t` enum value, which is actually defined in the M5GFX library and aliased in M5Unified:

```cpp
// From M5Unified.hpp
namespace m5
{
  using board_t = m5gfx::board_t;
}
```

Common board_t values include:
- `board_M5Stack` - Original M5Stack Basic/Gray/Fire
- `board_M5StackCore2` - M5Stack Core2
- `board_M5StackCoreS3` - M5Stack Core S3
- `board_M5StickC` - M5StickC
- `board_M5StickCPlus` - M5StickC Plus
- `board_M5StickCPlus2` - M5StickC Plus 2
- `board_M5StickS3` - M5StickS3
- `board_M5AtomLite` - ATOM Lite
- `board_M5AtomMatrix` - ATOM Matrix
- `board_M5AtomS3` - ATOMS3
- `board_M5Paper` - M5Paper
- `board_M5Dial` - M5Dial
- `board_M5Cardputer` - M5Cardputer
- `board_M5Tab5` - M5Tab5 (ESP32-P4)
- `board_unknown` - Fallback/undetected

Sources: [src/M5Unified.hpp:23]()

---

## Arduino IDE Board Defines

If runtime detection fails (returns `board_unknown`), the system falls back to Arduino IDE board selection macros. This provides a manual override mechanism when auto-detection is insufficient.

| Arduino Define | Fallback Board |
|----------------|----------------|
| `ARDUINO_M5STACK_CORE_ESP32` | `board_M5Stack` |
| `ARDUINO_M5STACK_CORE2` | `board_M5StackCore2` |
| `ARDUINO_M5STICK_C` | `board_M5StickC` |
| `ARDUINO_M5STICK_C_PLUS` | `board_M5StickCPlus` |
| `ARDUINO_M5STACK_COREINK` | `board_M5StackCoreInk` |
| `ARDUINO_M5STACK_PAPER` | `board_M5Paper` |
| `ARDUINO_M5STACK_TOUGH` | `board_M5Tough` |
| `ARDUINO_M5STACK_ATOM` | `board_M5AtomLite` |
| `ARDUINO_M5STACK_TIMER_CAM` | `board_M5TimerCam` |

If no Arduino define matches and detection fails, the system uses `config.fallback_board` specified in the configuration passed to `M5.begin()`.

Sources: [src/M5Unified.cpp:1075-1112]()

---

## ESP32 Variant-Specific Detection Paths

The detection logic is heavily conditional on the ESP32 variant, controlled by `CONFIG_IDF_TARGET_*` macros from sdkconfig.

```mermaid
graph TB
    entry["_check_boardtype(board)"]
    check_build{"Check<br/>CONFIG_IDF_TARGET"}
    
    entry --> check_build
    
    check_build --> ESP32["CONFIG_IDF_TARGET_ESP32<br/>(Original ESP32)"]
    check_build --> ESP32S3["CONFIG_IDF_TARGET_ESP32S3"]
    check_build --> ESP32C3["CONFIG_IDF_TARGET_ESP32C3"]
    check_build --> ESP32C6["CONFIG_IDF_TARGET_ESP32C6"]
    check_build --> ESP32P4["CONFIG_IDF_TARGET_ESP32P4"]
    
    ESP32 --> PKG_VER["get_pkg_ver()<br/>Package version"]
    PKG_VER --> D0WDQ6_PATH["TimerCam path"]
    PKG_VER --> PICOD4_PATH["Atom/Stamp path<br/>(GPIO + Touch test)"]
    PKG_VER --> PICOV3_PATH["AtomPsram path"]
    
    ESP32S3 --> S3_PKG["get_pkg_ver()"]
    S3_PKG --> QFN56["0: QFN56<br/>(GPIO pattern)"]
    S3_PKG --> LGA56["1: LGA56<br/>(I2C probe for AtomEchoS3R)"]
    
    ESP32C3 --> C3_GPIO["GPIO20 pulldown test"]
    C3_GPIO --> STAMPC3["StampC3 vs StampC3U"]
    
    ESP32C6 --> C6_DEFAULT["board_M5NanoC6"]
    
    ESP32P4 --> P4_GPIO32["GPIO32 pulldown test"]
    P4_GPIO32 --> TAB5["M5Tab5 vs UnitPoEP4"]
    
    style check_build fill:#f9f9f9,stroke:#333,stroke-width:2px
```

**ESP32 Variant Detection Dispatch**

Each ESP32 variant has unique hardware characteristics that necessitate different detection approaches:

- **ESP32 (original)**: Rich package variants and mature ecosystem → Use package detection + GPIO tests
- **ESP32-S3**: Many M5Stack products → Complex GPIO patterns + I2C probing
- **ESP32-C3**: Minimal product line → Simple GPIO pullup test
- **ESP32-C6**: New variant → Simple default assignment
- **ESP32-P4**: Tab5-specific → Direct GPIO test

Sources: [src/M5Unified.cpp:974-1418]()

---

## Integration with Pin Mapping

After board detection completes, the detected board type is used to load the appropriate pin mapping table. This is done by `_setup_pinmap(board_t id)`.

```mermaid
graph LR
    subgraph "Pin Mapping Tables (Compile-Time)"
        I2C_TBL["_pin_table_i2c_ex_in<br/>(In_SCL, In_SDA, Ex_SCL, Ex_SDA)"]
        PORT_BC["_pin_table_port_bc<br/>(PortB P1/P2, PortC P1/P2)"]
        PORT_DE["_pin_table_port_de<br/>(PortD P1/P2, PortE P1/P2)"]
        SPI_SD["_pin_table_spi_sd<br/>(CLK, MOSI, MISO, CS)"]
        OTHER0["_pin_table_other0<br/>(RGB_LED)"]
        OTHER1["_pin_table_other1<br/>(POWER_HOLD)"]
        MBUS["_pin_table_mbus<br/>(MBUS pins 1-30)"]
    end
    
    board["Detected board_t"]
    lookup["Lookup row in each table<br/>matching board_t"]
    copy["memcpy to _get_pin_table"]
    api["getPin(pin_name_t) API"]
    
    board --> lookup
    
    I2C_TBL --> lookup
    PORT_BC --> lookup
    PORT_DE --> lookup
    SPI_SD --> lookup
    OTHER0 --> lookup
    OTHER1 --> lookup
    MBUS --> lookup
    
    lookup --> copy
    copy --> api
```

**Pin Mapping Table Structure**

Each pin table is a 2D array where:
- First column = `board_t` identifier
- Subsequent columns = GPIO numbers for that board
- Last row = `board_t::board_unknown` (fallback values)

The `_setup_pinmap()` function iterates through all seven pin tables, finds the row matching the detected board, and copies the pin assignments into the `_get_pin_table` array. This array is then accessed via the `getPin(pin_name_t)` API.

Sources: [src/M5Unified.cpp:73-327]() (pin tables), [src/M5Unified.cpp:328-348]() (_setup_pinmap)

---

## Key Detection Code Entities

### Core Functions

| Function | Location | Purpose |
|----------|----------|---------|
| `_check_boardtype(board_t)` | [src/M5Unified.cpp:971-1418]() | Main board detection logic |
| `_setup_pinmap(board_t)` | [src/M5Unified.cpp:328-348]() | Load pin mappings for detected board |
| `_setup_i2c(board_t)` | [src/M5Unified.cpp:1420-1495]() | Configure I2C buses based on board |
| `_read_touch_pad(...)` | [src/M5Unified.cpp:827-883]() | Read capacitive touch sensors (ESP32) |

### Member Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `M5Unified::_board` | `board_t` | Stores detected board type |
| `M5Unified::_get_pin_table` | `int8_t[pin_name_max]` | Pin mapping lookup table |

### Configuration

| Config Field | Type | Purpose |
|--------------|------|---------|
| `config_t::fallback_board` | `board_t` | Board type if detection fails |

Sources: [src/M5Unified.hpp:622](), [src/M5Unified.hpp:652](), [src/M5Unified.hpp:160-171]()

---

## Detection Call Flow in M5.begin()

```mermaid
sequenceDiagram
    participant App as Application
    participant M5 as M5Unified
    participant Display as M5GFX Display
    participant Detect as _check_boardtype()
    participant Pinmap as _setup_pinmap()
    participant I2C as _setup_i2c()
    
    App->>M5: M5.begin(config)
    activate M5
    
    Note over M5: _board == board_unknown initially
    
    M5->>Display: Display.init() or init_without_reset()
    Display->>Display: Detect display hardware
    Display-->>M5: Return detected board hint
    
    M5->>Detect: _check_boardtype(Display.getBoard())
    activate Detect
    
    alt ESP32 Original
        Detect->>Detect: get_pkg_ver() → package type
        alt Package indicates specific board
            Detect-->>M5: Return board type
        else Requires GPIO test
            Detect->>Detect: GPIO pullup/pulldown pattern
            alt Atom series
                Detect->>Detect: Touch sensor test on G27
                Detect->>Detect: I2S pin test
            end
            Detect-->>M5: Return board type
        end
    else ESP32-S3
        Detect->>Detect: GPIO pattern test (G4,G8,G10,G12,G38)
        alt Pattern matches known board
            Detect-->>M5: Return board type
        else Still unknown
            Detect->>Detect: I2C bit-bang probe (PowerHub)
            Detect-->>M5: Return board type or board_unknown
        end
    else ESP32-C3/C6/P4
        Detect->>Detect: Simple GPIO test or default
        Detect-->>M5: Return board type
    end
    
    deactivate Detect
    
    alt Detected board == board_unknown
        M5->>M5: _board = config.fallback_board
    else Detection succeeded
        M5->>M5: _board = detected board
    end
    
    M5->>Pinmap: _setup_pinmap(_board)
    activate Pinmap
    Pinmap->>Pinmap: Lookup pin tables by _board
    Pinmap->>Pinmap: Copy pins to _get_pin_table
    deactivate Pinmap
    
    M5->>I2C: _setup_i2c(_board)
    activate I2C
    I2C->>I2C: Get In_I2C pins via getPin()
    I2C->>I2C: Get Ex_I2C pins via getPin()
    I2C->>I2C: Initialize I2C peripherals
    deactivate I2C
    
    Note over M5: Continue with remaining init...
    
    deactivate M5
```

**Complete Board Detection Sequence**

Sources: [src/M5Unified.hpp:332-360]()

---

## Summary

The M5Unified board detection system provides automatic hardware identification through:

1. **ESP32 package version reading** - Coarse-grained board family identification
2. **GPIO pattern testing** - Fine-grained board differentiation using pullup/pulldown characteristics
3. **I2C device probing** - Active communication to detect specific peripherals
4. **Touch sensor capacitance** - Physical layout detection for Atom series

The detection result (`board_t`) drives all subsequent configuration including pin mapping, I2C bus setup, peripheral initialization, and feature availability. This architecture enables M5Unified to provide a truly unified API across the entire M5Stack product line while maintaining optimal performance through compile-time table lookups rather than runtime conditionals.