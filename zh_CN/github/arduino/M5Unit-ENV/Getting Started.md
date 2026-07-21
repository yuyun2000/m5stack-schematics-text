M5Unit-ENV Getting Started

# Getting Started

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [examples/UnitUnified/UnitENVIII/PlotToSerial/PlotToSerial.ino](examples/UnitUnified/UnitENVIII/PlotToSerial/PlotToSerial.ino)
- [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp](examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp)
- [examples/UnitUnified/UnitENVPro/PlotToSerial/PlotToSerial.ino](examples/UnitUnified/UnitENVPro/PlotToSerial/PlotToSerial.ino)
- [examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp](examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp)
- [examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp](examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp)
- [library.json](library.json)
- [library.properties](library.properties)

</details>



This page guides you through initial setup, installation, dependency management, and first steps with the M5Unit-ENV library. You will learn how to install the library via Arduino Library Manager or PlatformIO, configure dependencies, select between conventional and unified interfaces, and run your first environmental sensor program.

For architectural details about the dual-interface design, see [Architecture Overview](#3). For detailed sensor configuration and usage patterns, see [Usage Patterns and Examples](#5). For troubleshooting installation or initialization issues, see [Troubleshooting and FAQ](#9).

## Installation Methods

The M5Unit-ENV library can be installed through two primary methods, depending on your development environment.

### Installation Decision Tree

```mermaid
flowchart TD
    START["Choose Installation Method"]
    IDE_CHECK{"Using Arduino IDE?"}
    ALM["Arduino Library Manager"]
    PIO["PlatformIO Library Manager"]
    MANUAL["Manual Installation"]
    
    START --> IDE_CHECK
    IDE_CHECK -->|Yes| ALM
    IDE_CHECK -->|No, using PlatformIO| PIO
    IDE_CHECK -->|No, manual setup| MANUAL
    
    ALM --> ALM_STEPS["1. Open Library Manager<br/>2. Search 'M5Unit-ENV'<br/>3. Install version 1.3.1+<br/>4. Install dependencies"]
    PIO --> PIO_STEPS["1. Add to platformio.ini<br/>2. lib_deps = m5stack/M5Unit-ENV<br/>3. Dependencies auto-install"]
    MANUAL --> MANUAL_STEPS["1. Clone repository<br/>2. Copy to libraries folder<br/>3. Manually install dependencies"]
    
    ALM_STEPS --> VERIFY["Verify Installation"]
    PIO_STEPS --> VERIFY
    MANUAL_STEPS --> VERIFY
```

**Sources:** [README.md:1-106](), [library.properties:1-12](), [library.json:1-33]()

### Arduino Library Manager Installation

The library is registered in the Arduino Library Registry and can be installed directly from the Arduino IDE or Arduino CLI.

**Arduino IDE Steps:**
1. Open Arduino IDE
2. Navigate to **Sketch → Include Library → Manage Libraries**
3. Search for `M5Unit-ENV`
4. Select version `1.3.1` or higher
5. Click **Install** (dependencies will prompt for installation)

**Arduino CLI:**
```bash
arduino-cli lib install "M5Unit-ENV@1.3.1"
```

**Sources:** [library.properties:1-12](), [README.md:1-28]()

### PlatformIO Installation

Add the library to your `platformio.ini` configuration file:

```ini
[env:your_board]
platform = espressif32
framework = arduino
lib_deps = 
    m5stack/M5Unit-ENV@^1.3.1
```

PlatformIO will automatically resolve and install dependencies specified in [library.json:13-17]().

**Sources:** [library.json:1-33](), [README.md:29-88]()

## Dependency Management

The library requires different dependencies depending on which interface and sensor units you use.

### Core Dependencies by Interface

| Dependency | Conventional Interface | Unified Interface | Version Requirement | Notes |
|------------|----------------------|-------------------|---------------------|-------|
| `M5UnitUnified` | ❌ | ✅ Required | `>=0.1.0` | Framework for unified handling |
| `M5Utility` | ❌ | ✅ Required | Latest | CRC-8, MurmurHash3 utilities |
| `M5HAL` | ❌ | ✅ Required | Latest | Hardware abstraction layer |
| `Adafruit_BMP280_Library` | ✅ For BMP280 | ❌ | Latest | Conventional BMP280 driver |
| `Adafruit_Sensor` | ✅ For BMP280 | ❌ | Latest | Unified sensor API base |
| `Sensirion I2C SCD4x` | ✅ For SCD40 | ❌ | Latest | Conventional CO2 driver |
| `Sensirion I2C SHT4x` | ✅ For SHT40 | ❌ | Latest | Conventional temp/humidity |
| `Sensirion Core` | ✅ For Sensirion | ❌ | Latest | I2C common functions |
| `BME68x Sensor library` | ✅ For BME688 | ✅ For BME688 | `>=1.3.40408` | Low-level BME688 driver |
| `bsec2` | ✅ For BME688 IAQ | ✅ For BME688 IAQ | `>=1.10.2610` | Air quality algorithm |

**Sources:** [library.properties:11](), [library.json:13-17](), [README.md:29-36](), [README.md:78-85]()

### Dependency Resolution Flow

```mermaid
flowchart TB
    APP["Application Code"]
    INTERFACE{"Interface Choice"}
    
    APP --> INTERFACE
    
    INTERFACE -->|"#include <M5UnitENV.h>"| CONV["Conventional Interface"]
    INTERFACE -->|"#include <M5UnitUnifiedENV.h>"| UNIFIED["Unified Interface"]
    
    subgraph "Conventional Dependencies"
        ADA_BMP["Adafruit_BMP280_Library"]
        ADA_SENS["Adafruit_Sensor"]
        SENS_SCD["Sensirion I2C SCD4x"]
        SENS_SHT["Sensirion I2C SHT4x"]
        SENS_CORE["Sensirion Core"]
    end
    
    subgraph "Unified Dependencies"
        M5UU["M5UnitUnified >=0.1.0"]
        M5UTIL["M5Utility"]
        M5HAL["M5HAL"]
    end
    
    subgraph "Shared Dependencies"
        BME68X["BME68x Sensor library >=1.3.40408"]
        BSEC2["bsec2 >=1.10.2610<br/>⚠️ Excluded: NanoC6"]
    end
    
    CONV --> ADA_BMP
    CONV --> ADA_SENS
    CONV --> SENS_SCD
    CONV --> SENS_SHT
    CONV --> SENS_CORE
    
    UNIFIED --> M5UU
    UNIFIED --> M5UTIL
    UNIFIED --> M5HAL
    
    CONV -.->|"If using ENVPro"| BME68X
    CONV -.->|"If using ENVPro with IAQ"| BSEC2
    UNIFIED -.->|"If using ENVPro"| BME68X
    UNIFIED -.->|"If using ENVPro with IAQ"| BSEC2
    
    ADA_BMP --> ADA_SENS
    SENS_SCD --> SENS_CORE
    SENS_SHT --> SENS_CORE
```

**Sources:** [library.properties:11](), [library.json:13-17](), [README.md:78-86]()

### Platform-Specific Considerations

The **BSEC2** library (required for BME688 IAQ calculations) has platform exclusions:

- **Excluded:** ESP32-C6 (NanoC6) due to resource constraints
- **Supported:** ESP32, ESP32-S3, ESP32-C3

This is enforced in the build system configuration.

**Sources:** [README.md:85]()

## Interface Selection

The library provides two mutually exclusive interfaces. You must choose one at compile time by including the appropriate header.

### Interface Comparison

```mermaid
flowchart LR
    subgraph "Code Entry Points"
        CONV_H["M5UnitENV.h"]
        UNIFIED_H["M5UnitUnifiedENV.h"]
    end
    
    subgraph "Usage Patterns"
        STANDALONE["Standalone Sensor Usage<br/>Direct hardware control<br/>Adafruit/Sensirion APIs"]
        FRAMEWORK["Framework Integration<br/>Multi-unit management<br/>M5Stack HAL abstraction"]
    end
    
    subgraph "Typical Use Cases"
        SIMPLE["Simple single-sensor projects<br/>Learning/prototyping<br/>Existing Adafruit code"]
        COMPLEX["Multi-sensor applications<br/>M5Stack ecosystem integration<br/>Advanced lifecycle management"]
    end
    
    CONV_H -->|"Provides"| STANDALONE
    UNIFIED_H -->|"Provides"| FRAMEWORK
    
    STANDALONE -->|"Best for"| SIMPLE
    FRAMEWORK -->|"Best for"| COMPLEX
    
    CONV_H -.->|"⚠️ Do not mix"| UNIFIED_H
```

**Key Decision Factors:**

| Factor | Conventional Interface | Unified Interface |
|--------|----------------------|-------------------|
| **Header Include** | `#include <M5UnitENV.h>` | `#include <M5UnitUnifiedENV.h>` |
| **Supported Units** | ENV3, ENV4, BMP280, SHT30, QMP6988, SGP30 | ENVPro, CO2, CO2L, ENVIII, ENVIV, TVOC |
| **Initialization Pattern** | Direct sensor `begin()` calls | `UnitUnified::add()` + `begin()` |
| **I2C Management** | Arduino `Wire` library | `Wire` or `M5HAL::bus::i2c` |
| **Discovery** | Manual addressing | Automatic via `M5UnitUnified` |
| **Learning Curve** | Lower (standard Arduino) | Higher (M5Stack framework) |

**Sources:** [library.properties:10](), [library.json:22-25](), [README.md:71-75](), [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:9-11]()

### Mutual Exclusion Warning

**Do not include both headers simultaneously.** The interfaces are mutually exclusive and will cause compilation conflicts:

```cpp
// ❌ WRONG - Will cause conflicts
#include <M5UnitENV.h>
#include <M5UnitUnifiedENV.h>

// ✅ CORRECT - Choose one
#include <M5UnitUnifiedENV.h>  // For unified interface
```

**Sources:** [README.md:72-75]()

## Basic Setup Pattern (Unified Interface)

This section demonstrates the standard initialization pattern using the unified interface. For conventional interface examples, see the sensor-specific documentation pages under [Sensor Units Reference](#4).

### Unified Interface Setup Flow

```mermaid
flowchart TD
    START["Application Startup"]
    
    M5_BEGIN["M5.begin()<br/>Initialize M5Stack core"]
    GET_PINS["M5.getPin()<br/>Get SDA/SCL pins"]
    
    I2C_CHOICE{"I2C Bus Configuration"}
    WIRE_INIT["Wire.begin(sda, scl, 400kHz)"]
    HAL_INIT["m5::hal::bus::i2c::getBus(config)"]
    
    UNIT_CREATE["Create UnitUnified manager<br/>Create sensor unit objects"]
    UNIT_ADD["Units.add(unit, bus)"]
    UNIT_BEGIN["Units.begin()"]
    
    CHECK_SUCCESS{"begin() success?"}
    ERROR["Display error<br/>Halt execution"]
    SUCCESS["Ready for measurements"]
    
    START --> M5_BEGIN
    M5_BEGIN --> GET_PINS
    GET_PINS --> I2C_CHOICE
    
    I2C_CHOICE -->|"Using Wire"| WIRE_INIT
    I2C_CHOICE -->|"Using M5HAL"| HAL_INIT
    
    WIRE_INIT --> UNIT_CREATE
    HAL_INIT --> UNIT_CREATE
    
    UNIT_CREATE --> UNIT_ADD
    UNIT_ADD --> UNIT_BEGIN
    UNIT_BEGIN --> CHECK_SUCCESS
    
    CHECK_SUCCESS -->|"false"| ERROR
    CHECK_SUCCESS -->|"true"| SUCCESS
```

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:43-127]()

### Minimal Setup Example (Wire Interface)

The following pattern appears in [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:43-127]():

**Global Declarations:**
```cpp
#include <M5Unified.h>
#include <M5UnitUnified.h>
#include <M5UnitUnifiedENV.h>

m5::unit::UnitUnified Units;  // Manager for multiple units
m5::unit::UnitENV3 unitENV3;  // Example: ENV3 composite unit
```

**Setup Function:**
```cpp
void setup() {
    M5.begin();  // Initialize M5Stack core
    
    // Get I2C pins for PortA
    auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
    
    // Initialize Wire at 400kHz
    Wire.end();
    Wire.begin(pin_num_sda, pin_num_scl, 400000U);
    
    // Add unit to manager and initialize
    if (!Units.add(unitENV3, Wire) || !Units.begin()) {
        M5_LOGE("Failed to begin");
        while (true) { delay(10000); }
    }
}
```

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:43-89]()

### I2C Bus Configuration Options

The library supports two I2C bus abstraction methods:

#### Option 1: Arduino Wire Library

```cpp
// Standard Arduino approach
Wire.end();
Wire.begin(pin_num_sda, pin_num_scl, 400000U);
Units.add(unit, Wire);
```

**Characteristics:**
- Uses Arduino's standard `TwoWire` class
- Widely compatible with existing Arduino code
- Manual pin configuration required
- Enabled when `USING_M5HAL` is not defined

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:79-89]()

#### Option 2: M5HAL Bus Abstraction

```cpp
// M5HAL approach
#define USING_M5HAL  // Enable M5HAL mode

m5::hal::bus::I2CBusConfig i2c_cfg;
i2c_cfg.pin_sda = m5::hal::gpio::getPin(pin_num_sda);
i2c_cfg.pin_scl = m5::hal::gpio::getPin(pin_num_scl);
auto i2c_bus = m5::hal::bus::i2c::getBus(i2c_cfg);
Units.add(unit, i2c_bus ? i2c_bus.value() : nullptr);
```

**Characteristics:**
- Uses M5Stack's hardware abstraction layer
- Provides advanced bus management
- Consistent API across M5Stack products
- Enabled by defining `USING_M5HAL` before includes

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:13](), [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:65-77]()

### Code Entity Mapping

```mermaid
classDiagram
    class M5 {
        +begin() void
        +update() void
        +getPin(pin_name_t) uint8_t
        +Display lcd
        +Log logger
    }
    
    class UnitUnified {
        +add(Unit&, Wire&) bool
        +add(Unit&, I2CBus*) bool
        +begin() bool
        +update() void
        +debugInfo() String
    }
    
    class UnitENV3 {
        +config(Config&) void
        +sht30 UnitSHT30
        +qmp6988 UnitQMP6988
    }
    
    class UnitENVPro {
        +temperature() float
        +pressure() float
        +humidity() float
        +gas() float
        +iaq() float
    }
    
    class UnitTVOC {
        +co2eq() uint16_t
        +tvoc() uint16_t
        +updated() bool
    }
    
    class Wire {
        +begin(sda, scl, freq) void
        +end() void
    }
    
    M5 --> Wire : "configures"
    UnitUnified --> UnitENV3 : "manages"
    UnitUnified --> UnitENVPro : "manages"
    UnitUnified --> UnitTVOC : "manages"
    UnitUnified --> Wire : "uses"
```

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:1-154](), [examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp:1-57](), [examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp:1-57]()

## First Steps

### Running Example Sketches

The library includes example sketches in the `examples/UnitUnified/` directory for each supported sensor unit.

#### Example Location Structure

```mermaid
graph TB
    ROOT["examples/UnitUnified/"]
    
    ENV3["UnitENVIII/<br/>PlotToSerial/"]
    ENV4["UnitENVIV/<br/>PlotToSerial/"]
    ENVPRO["UnitENVPro/<br/>PlotToSerial/"]
    CO2["UnitCO2/<br/>PlotToSerial/"]
    CO2L["UnitCO2L/<br/>PlotToSerial/"]
    TVOC["UnitTVOC/<br/>PlotToSerial/"]
    
    INO["*.ino<br/>Arduino entry point"]
    MAIN["main/*.cpp<br/>Implementation"]
    
    ROOT --> ENV3
    ROOT --> ENV4
    ROOT --> ENVPRO
    ROOT --> CO2
    ROOT --> CO2L
    ROOT --> TVOC
    
    ENV3 --> INO
    ENV3 --> MAIN
    
    INO -.->|"#include"| MAIN
```

**Example Structure:**
- Each unit has a dedicated directory (e.g., `UnitENVIII/`)
- Contains a `PlotToSerial/` subdirectory
- `.ino` file includes the `.cpp` implementation from `main/`

**Sources:** [README.md:88](), [examples/UnitUnified/UnitENVIII/PlotToSerial/PlotToSerial.ino:1-12]()

#### Opening Examples in Arduino IDE

1. **File → Examples → M5Unit-ENV → UnitUnified → [UnitName] → PlotToSerial**
2. Select your M5Stack board from **Tools → Board**
3. Configure Port from **Tools → Port**
4. Click **Upload**

#### Opening Examples in PlatformIO

Examples can be used as project templates:

```bash
# Copy example to your project
cp -r examples/UnitUnified/UnitENVIII/PlotToSerial/ my_project/
cd my_project
pio run -t upload
```

**Sources:** [README.md:88]()

### Basic Measurement Loop Pattern

All unified interface examples follow a consistent `setup()` / `loop()` pattern:

```mermaid
sequenceDiagram
    participant App
    participant M5
    participant Units
    participant Sensor
    
    Note over App,Sensor: setup() phase
    App->>M5: M5.begin()
    App->>M5: M5.getPin(port_a_sda/scl)
    App->>Units: Units.add(unit, Wire)
    App->>Units: Units.begin()
    Units->>Sensor: initialize hardware
    
    Note over App,Sensor: loop() phase (repeating)
    loop Every Iteration
        App->>M5: M5.update()
        App->>Units: Units.update()
        Units->>Sensor: trigger measurement cycle
        
        alt Sensor has new data
            Sensor-->>Units: update complete
            App->>Sensor: unit.updated() == true
            App->>Sensor: read data (temperature(), etc.)
            App->>M5: M5.Log.printf(values)
        end
    end
```

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:129-153]()

### Example: ENV3 Periodic Measurement

This example from [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:129-153]() demonstrates the standard periodic measurement pattern:

```cpp
void loop() {
    M5.update();      // Update M5Stack state
    Units.update();   // Trigger sensor update cycle
    
    // Check if SHT30 has new data
    if (sht30.updated()) {
        M5.Log.printf(">SHT30Temp:%2.2f\n>Humidity:%2.2f\n", 
                      sht30.temperature(), sht30.humidity());
    }
    
    // Check if QMP6988 has new data
    if (qmp6988.updated()) {
        M5.Log.printf(">QMP6988Temp:%2.2f\n>Pressure:%.2f\n", 
                      qmp6988.temperature(), qmp6988.pressure() * 0.01f);
    }
}
```

**Key Methods:**
- `Units.update()`: Triggers measurement cycle for all registered units
- `unit.updated()`: Returns `true` when new data is available
- `unit.temperature()`, `unit.humidity()`, etc.: Access latest readings

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:129-153]()

### Example: ENVPro with BSEC2

For advanced air quality measurements with the BME688 sensor ([examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp:42-56]()):

```cpp
void loop() {
    M5.update();
    Units.update();
    
    if (unit.updated()) {
#if defined(UNIT_BME688_USING_BSEC2)
        // With BSEC2: IAQ available
        M5.Log.printf(">IAQ:%.2f\n>Temperature:%.2f\n>Pressure:%.2f\n", 
                      unit.iaq(), unit.temperature(), unit.pressure());
#else
        // Without BSEC2: basic environmental only
        M5.Log.printf(">Temperature:%.2f\n>Pressure:%.2f\n", 
                      unit.temperature(), unit.pressure());
#endif
    }
}
```

**BSEC2 Note:** The `UNIT_BME688_USING_BSEC2` define is set automatically when BSEC2 library is available and platform is supported.

**Sources:** [examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp:42-56]()

### Example: TVOC with Initialization Delay

The SGP30 sensor requires a 15-second initialization period ([examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp:46-56]()):

```cpp
void loop() {
    M5.update();
    Units.update();
    
    // SGP30 measurement starts 15 seconds after begin
    if (unit.updated()) {
        M5.Log.printf("\n>CO2eq:%u\n>TVOC:%u", unit.co2eq(), unit.tvoc());
    }
}
```

**Important:** The first valid readings appear 15 seconds after `Units.begin()` completes. The `unit.updated()` method returns `false` during initialization.

**Sources:** [examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp:41-56]()

## Verification and Next Steps

After successfully running an example, you should see:

1. **Serial Output:** Sensor data formatted for Arduino Serial Plotter (`>Label:Value` format)
2. **LCD Feedback:** Display clears to dark green on success, red on failure
3. **Debug Info:** `Units.debugInfo()` prints detected units and their I2C addresses

### Verification Checklist

| Step | Expected Behavior | Failure Action |
|------|------------------|----------------|
| Compilation | No errors, all dependencies resolved | Check [Dependency Management](#dependency-management) |
| Upload | Sketch uploads successfully | Verify board selection and port |
| Serial Output | Debug messages appear at 115200 baud | Check serial monitor configuration |
| Sensor Detection | `Units.debugInfo()` shows discovered units | Check I2C connections, addresses |
| Data Updates | `unit.updated()` returns `true` periodically | Check sensor power, initialization delay |
| Valid Readings | Data values within expected ranges | See [Troubleshooting and FAQ](#9) |

### Next Steps

Once basic examples work:

1. **Explore Measurement Modes:** See [Usage Patterns and Examples](#5) for periodic vs single-shot patterns
2. **Configure Sensors:** See individual sensor pages under [Sensor Units Reference](#4)
3. **Multi-Sensor Applications:** See [Multi-Sensor Applications](#5.2)
4. **Calibration:** See [Calibration and Configuration](#5.3) for CO2 calibration, baseline persistence
5. **Custom Applications:** Adapt examples to your specific use case

**Sources:** [examples/UnitUnified/UnitENVIII/PlotToSerial/main/PlotToSerial.cpp:1-154](), [examples/UnitUnified/UnitENVPro/PlotToSerial/main/PlotToSerial.cpp:1-57](), [examples/UnitUnified/UnitTVOC/PlotToSerial/main/PlotToSerial.cpp:1-57]()