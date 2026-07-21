M5Unit-ENV Architecture Overview

# Architecture Overview

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [library.json](library.json)
- [library.properties](library.properties)
- [platformio.ini](platformio.ini)
- [src/M5UnitUnifiedENV.hpp](src/M5UnitUnifiedENV.hpp)
- [unit_co2_env.ini](unit_co2_env.ini)

</details>



This document explains the internal structure of the M5Unit-ENV library, including the dual-interface design philosophy, component hierarchy, dependency integration, and data flow patterns. This overview provides a foundation for understanding how the library organizes sensor drivers, manages external dependencies, and supports both standalone and framework-integrated usage.

For details on the differences between the two interfaces, see [Conventional vs Unified Interface](#3.1). For dependency requirements and version constraints, see [Dependency Management](#3.2). For usage patterns and code examples, see [Usage Patterns and Examples](#5).

## Library Entry Points

The M5Unit-ENV library provides two mutually exclusive top-level headers that define the library's interface paradigm:

| Header File | Interface Type | Primary Use Case | Framework Dependency |
|------------|----------------|------------------|---------------------|
| `M5UnitENV.h` | Conventional | Standalone sensor usage | Arduino Wire library |
| `M5UnitUnifiedENV.h` | Unified | Multi-sensor integration | M5UnitUnified framework |

The mutual exclusion is enforced at compile time through preprocessor guards in [src/M5UnitUnifiedENV.hpp:13-15]():

```cpp
#if defined(_M5_UNIT_ENV_H_)
#error "DO NOT USE it at the same time as conventional libraries"
#endif
```

Both headers declare themselves in [library.properties:10]() and [library.json:22-25]() as the primary includes for the library.

**Unified Interface Include Structure**

```mermaid
graph TD
    APP["Application Code"]
    MAIN["M5UnitUnifiedENV.hpp<br/>(Main Header)"]
    
    CO2_SCD40["unit_SCD40.hpp"]
    CO2_SCD41["unit_SCD41.hpp"]
    
    ENV3_PARENT["unit_ENV3.hpp"]
    ENV3_SHT30["unit_SHT30.hpp"]
    ENV3_QMP["unit_QMP6988.hpp"]
    
    ENV4_PARENT["unit_ENV4.hpp"]
    ENV4_SHT40["unit_SHT40.hpp"]
    ENV4_BMP["unit_BMP280.hpp"]
    
    ENVPRO["unit_BME688.hpp"]
    TVOC["unit_SGP30.hpp"]
    
    ALIAS_CO2["UnitCO2<br/>(alias)"]
    ALIAS_CO2L["UnitCO2L<br/>(alias)"]
    ALIAS_PRO["UnitENVPro<br/>(alias)"]
    ALIAS_TVOC["UnitTVOC<br/>(alias)"]
    
    APP -->|"includes"| MAIN
    
    MAIN -->|"line 21"| CO2_SCD40
    MAIN -->|"line 22"| CO2_SCD41
    MAIN -->|"line 26"| ENV3_PARENT
    MAIN -->|"line 24"| ENV3_SHT30
    MAIN -->|"line 25"| ENV3_QMP
    MAIN -->|"line 28"| ENVPRO
    MAIN -->|"line 30"| TVOC
    MAIN -->|"line 34"| ENV4_PARENT
    MAIN -->|"line 32"| ENV4_SHT40
    MAIN -->|"line 33"| ENV4_BMP
    
    MAIN -->|"line 48"| ALIAS_CO2
    MAIN -->|"line 49"| ALIAS_CO2L
    MAIN -->|"line 50"| ALIAS_PRO
    MAIN -->|"line 51"| ALIAS_TVOC
    
    ALIAS_CO2 -.->|"typedef"| CO2_SCD40
    ALIAS_CO2L -.->|"typedef"| CO2_SCD41
    ALIAS_PRO -.->|"typedef"| ENVPRO
    ALIAS_TVOC -.->|"typedef"| TVOC
    
    ENV3_PARENT -.->|"aggregates"| ENV3_SHT30
    ENV3_PARENT -.->|"aggregates"| ENV3_QMP
    ENV4_PARENT -.->|"aggregates"| ENV4_SHT40
    ENV4_PARENT -.->|"aggregates"| ENV4_BMP
```

Sources: [src/M5UnitUnifiedENV.hpp:1-55](), [library.properties:10](), [library.json:22-25]()

## Component Hierarchy

The library organizes sensors into three architectural tiers:

### Basic Sensor Units

Individual sensor drivers that provide direct hardware access:

| Unit Class | Physical Sensor | SKU | Capabilities |
|-----------|----------------|-----|--------------|
| `UnitSHT30` | SHT30 | U001-C | Temperature, Humidity, Periodic/Single-shot |
| `UnitSHT40` | SHT40 | U001-D | Temperature, Humidity, Heater, Periodic/Single-shot |
| `UnitQMP6988` | QMP6988 | U001-C | Pressure, Temperature, IIR Filter |
| `UnitBMP280` | BMP280 | U001-D | Pressure, Temperature, 6 Use Cases |
| `UnitSCD40` | SCD40 | U103 | CO2, Temperature, Humidity, ASC |
| `UnitSCD41` | SCD41 | U104 | CO2, Temperature, Humidity, Low Power |
| `UnitSGP30` | SGP30 | U088 | TVOC, eCO2, Baseline Management |
| `UnitBME688` | BME688 | U169 | Temperature, Humidity, Pressure, Gas, IAQ |

### Composite Units

Aggregated multi-sensor units that combine multiple physical sensors:

| Composite Class | Component Sensors | SKU | Architecture Pattern |
|----------------|-------------------|-----|---------------------|
| `UnitENV3` | `UnitSHT30` + `UnitQMP6988` | U001-C | Parent-child with I2C adapter |
| `UnitENV4` | `UnitSHT40` + `UnitBMP280` | U001-D | Parent-child with I2C adapter |

### Type Aliases

Product-friendly naming defined in [src/M5UnitUnifiedENV.hpp:48-51]():

```cpp
using UnitCO2    = m5::unit::UnitSCD40;
using UnitCO2L   = m5::unit::UnitSCD41;
using UnitENVPro = m5::unit::UnitBME688;
using UnitTVOC   = m5::unit::UnitSGP30;
```

**Component Class Hierarchy**

```mermaid
graph TB
    subgraph "m5::unit namespace"
        BASE["Component<br/>(M5UnitUnified base)"]
        
        SHT30["UnitSHT30"]
        QMP["UnitQMP6988"]
        ENV3["UnitENV3<br/>(ENVIII)"]
        
        SHT40["UnitSHT40"]
        BMP280["UnitBMP280"]
        ENV4["UnitENV4<br/>(ENVIV)"]
        
        SCD40["UnitSCD40<br/>(UnitCO2)"]
        SCD41["UnitSCD41<br/>(UnitCO2L)"]
        
        BME688["UnitBME688<br/>(UnitENVPro)"]
        SGP30["UnitSGP30<br/>(UnitTVOC)"]
        
        BASE -->|"inherits"| SHT30
        BASE -->|"inherits"| QMP
        BASE -->|"inherits"| ENV3
        BASE -->|"inherits"| SHT40
        BASE -->|"inherits"| BMP280
        BASE -->|"inherits"| ENV4
        BASE -->|"inherits"| SCD40
        BASE -->|"inherits"| SCD41
        BASE -->|"inherits"| BME688
        BASE -->|"inherits"| SGP30
        
        ENV3 -->|"component()"| SHT30
        ENV3 -->|"component()"| QMP
        
        ENV4 -->|"component()"| SHT40
        ENV4 -->|"component()"| BMP280
    end
```

Sources: [src/M5UnitUnifiedENV.hpp:20-34](), [src/M5UnitUnifiedENV.hpp:48-51]()

## Dependency Architecture

The library integrates with three primary dependency ecosystems: M5Stack, Bosch Sensortec, and third-party vendor libraries.

### M5Stack Ecosystem Dependencies

These dependencies are required for the unified interface and are declared in [library.properties:11]() and [library.json:13-16]():

| Library | Minimum Version | Purpose | Configuration Source |
|---------|----------------|---------|---------------------|
| `M5UnitUnified` | >=0.1.0 | Unit lifecycle management, discovery | [library.json:14]() |
| `M5Utility` | (implicit) | CRC-8, MurmurHash3 utilities | [library.properties:11]() |
| `M5HAL` | (implicit) | Hardware abstraction layer | [library.properties:11]() |
| `M5Unified` | (implicit) | Core M5Stack framework | [platformio.ini:13]() |

### Bosch Sensortec Dependencies

Required specifically for the BME688/ENVPro unit:

| Library | Minimum Version | Purpose | Platform Exclusions |
|---------|----------------|---------|-------------------|
| `BME68x Sensor library` | >=1.3.40408 | Low-level BME688 driver | None |
| `bsec2` | >=1.10.2610 | IAQ, CO2eq, VOC algorithms | NanoC6 (excluded) |

The BSEC2 exclusion for NanoC6 is handled in [platformio.ini:89-97](), where the `NanoC6` environment does not include `${bsec2.lib_deps}`.

### Third-Party Vendor Dependencies

Used by the conventional interface, documented in [README.md:29-35]():

| Library | Vendor | Sensor Support | Interface Type |
|---------|--------|----------------|----------------|
| `Adafruit_BMP280_Library` | Adafruit | BMP280 | Conventional only |
| `Adafruit_Sensor` | Adafruit | Unified sensor API | Conventional only |
| `Sensirion I2C SCD4x` | Sensirion | SCD40/SCD41 | Conventional only |
| `Sensirion I2C SHT4x` | Sensirion | SHT40 | Conventional only |
| `Sensirion Core` | Sensirion | I2C common functions | Conventional only |

**Dependency Integration Map**

```mermaid
graph TB
    subgraph "M5Unit-ENV Library"
        UNIFIED["M5UnitUnifiedENV.hpp"]
        CONV["M5UnitENV.h"]
        
        BME688_UNIT["unit_BME688.hpp"]
        SCD_UNITS["unit_SCD40.hpp<br/>unit_SCD41.hpp"]
        BMP_UNIT["unit_BMP280.hpp"]
        SHT_UNITS["unit_SHT30.hpp<br/>unit_SHT40.hpp"]
    end
    
    subgraph "M5Stack Ecosystem"
        M5U["M5Unified"]
        M5UU["M5UnitUnified<br/>Component base class"]
        M5HAL["M5HAL<br/>I2C, GPIO abstraction"]
        M5UTIL["M5Utility<br/>CRC-8, mmh3"]
    end
    
    subgraph "Bosch Sensortec"
        BME68X["BME68x Sensor library<br/>v1.3.40408+"]
        BSEC2["bsec2<br/>v1.10.2610+<br/>(excludes NanoC6)"]
    end
    
    subgraph "Third-Party Libraries"
        ADA_BMP["Adafruit_BMP280_Library"]
        ADA_SENS["Adafruit_Sensor"]
        SENS_SCD["Sensirion I2C SCD4x"]
        SENS_SHT["Sensirion I2C SHT4x"]
        SENS_CORE["Sensirion Core"]
    end
    
    UNIFIED --> M5UU
    UNIFIED --> M5HAL
    UNIFIED --> M5UTIL
    M5UU --> M5U
    
    BME688_UNIT --> BME68X
    BME688_UNIT --> BSEC2
    
    CONV --> ADA_BMP
    CONV --> ADA_SENS
    CONV --> SENS_SCD
    CONV --> SENS_SHT
    CONV --> SENS_CORE
    
    UNIFIED --> BME688_UNIT
    UNIFIED --> SCD_UNITS
    UNIFIED --> BMP_UNIT
    UNIFIED --> SHT_UNITS
```

Sources: [library.properties:11](), [library.json:13-16](), [platformio.ini:13-19](), [platformio.ini:89-97](), [README.md:29-35]()

## Build Configuration Architecture

The library supports both PlatformIO and Arduino IDE through parallel configuration systems.

### PlatformIO Configuration Structure

The build system uses a modular INI structure defined in [platformio.ini:1-204]():

| Configuration File | Purpose | Line Reference |
|-------------------|---------|----------------|
| `platformio.ini` | Base environments and framework selection | [platformio.ini:8-203]() |
| `unit_co2_env.ini` | CO2 unit test/example configurations | [platformio.ini:6]() |
| `unit_env3_env.ini` | ENV3 unit test/example configurations | [platformio.ini:6]() |
| `unit_env4_env.ini` | ENV4 unit test/example configurations | [platformio.ini:6]() |
| `unit_envpro_env.ini` | ENVPro unit test/example configurations | [platformio.ini:6]() |
| `unit_tvoc_env.ini` | TVOC unit test/example configurations | [platformio.ini:6]() |

**Base Environment Structure**

The base environment is defined in [platformio.ini:8-15]():

```
[env]
build_flags = -Wall -Wextra -Wreturn-local-addr -Werror=format -Werror=return-local-addr
lib_ldf_mode = deep
test_framework = googletest
test_build_src = true
lib_deps = m5stack/M5Unified
           m5stack/M5UnitUnified
           boschsensortec/BME68x Sensor library@>=1.3.40408
```

**Board Environment Inheritance Pattern**

Each M5Stack board extends from `m5base` with specific dependencies:

| Environment | Board Identifier | BSEC2 Support | Line Reference |
|------------|-----------------|---------------|----------------|
| `Core` | `m5stack-grey` | Yes | [platformio.ini:28-35]() |
| `Core2` | `m5stack-core2` | Yes | [platformio.ini:37-41]() |
| `CoreS3` | `m5stack-cores3` | Yes | [platformio.ini:43-47]() |
| `Fire` | `m5stack-fire` | Yes | [platformio.ini:49-53]() |
| `StampS3` | `m5stack-stamps3` | Yes | [platformio.ini:55-60]() |
| `AtomMatrix` | `m5stack-atom` | Yes | [platformio.ini:69-73]() |
| `AtomS3` | `m5stack-atoms3` | Yes | [platformio.ini:75-79]() |
| `AtomS3R` | `m5stack-atoms3r` | Yes | [platformio.ini:82-86]() |
| `NanoC6` | `m5stack-nanoc6` | **No** | [platformio.ini:89-97]() |

**Framework Version Selection**

Multiple Espressif32 platform versions are supported through configuration sections:

```
[arduino_latest]   platform = espressif32 @ 6.8.1
[arduino_6_6_0]    platform = espressif32 @ 6.6.0
[arduino_6_0_1]    platform = espressif32 @ 6.0.1
[arduino_5_4_0]    platform = espressif32 @ 5.4.0
[arduino_4_4_0]    platform = espressif32 @ 4.4.0
```

Defined in [platformio.ini:138-156]().

### Arduino IDE Configuration

Arduino IDE integration is configured through [library.properties:1-11]():

```
name=M5Unit-ENV
version=1.3.1
architectures=esp32
includes=M5UnitENV.h, M5UnitUnifiedENV.h
depends=M5UnitUnified,M5Utility,M5HAL,bsec2,BME68x Sensor library
```

**Build System Configuration Matrix**

```mermaid
graph TB
    subgraph "Configuration Files"
        PROPS["library.properties<br/>Arduino metadata"]
        JSON["library.json<br/>PlatformIO metadata"]
        INI_MAIN["platformio.ini<br/>Base config"]
        INI_UNITS["unit_*_env.ini<br/>Unit-specific configs"]
    end
    
    subgraph "Build Systems"
        ARDUINO["Arduino IDE/CLI"]
        PIO["PlatformIO"]
    end
    
    subgraph "Environment Inheritance"
        BASE["[env]<br/>Base dependencies"]
        M5BASE["[m5base]<br/>Monitor/upload config"]
        BOARDS["[Core], [Core2], [CoreS3]<br/>[Fire], [AtomS3], etc."]
        BSEC2_FLAG["[bsec2]<br/>lib_deps flag"]
    end
    
    subgraph "Framework Selection"
        FW_LATEST["[arduino_latest]<br/>ESP32 6.8.1"]
        FW_6_6["[arduino_6_6_0]<br/>ESP32 6.6.0"]
        FW_5_4["[arduino_5_4_0]<br/>ESP32 5.4.0"]
        FW_4_4["[arduino_4_4_0]<br/>ESP32 4.4.0"]
    end
    
    subgraph "Build Options"
        OPT_RELEASE["[option_release]<br/>LOG_LEVEL=3"]
        OPT_LOG["[option_log]<br/>LOG_LEVEL=5"]
        OPT_DEBUG["[option_debug]<br/>DEBUG flag"]
    end
    
    PROPS --> ARDUINO
    JSON --> PIO
    INI_MAIN --> PIO
    INI_UNITS --> PIO
    
    BASE --> M5BASE
    M5BASE --> BOARDS
    BSEC2_FLAG -.->|"optional"| BOARDS
    
    BOARDS -->|"extends"| FW_LATEST
    BOARDS -->|"extends"| FW_6_6
    BOARDS -->|"extends"| FW_5_4
    BOARDS -->|"extends"| FW_4_4
    
    FW_LATEST -->|"extends"| OPT_RELEASE
    FW_LATEST -->|"extends"| OPT_LOG
    FW_LATEST -->|"extends"| OPT_DEBUG
```

Sources: [platformio.ini:1-204](), [library.properties:1-11](), [library.json:1-33]()

## File Organization

The library follows a structured directory layout:

```
M5Unit-ENV/
├── src/
│   ├── M5UnitENV.h                    # Conventional interface header
│   ├── M5UnitUnifiedENV.hpp           # Unified interface header
│   └── unit/
│       ├── unit_BME688.hpp/cpp        # ENVPro sensor driver
│       ├── unit_SCD40.hpp/cpp         # CO2 sensor driver
│       ├── unit_SCD41.hpp/cpp         # CO2L sensor driver
│       ├── unit_SHT30.hpp/cpp         # Temperature/humidity driver
│       ├── unit_SHT40.hpp/cpp         # Advanced temp/humidity driver
│       ├── unit_QMP6988.hpp/cpp       # Pressure sensor driver
│       ├── unit_BMP280.hpp/cpp        # Pressure/temp driver
│       ├── unit_SGP30.hpp/cpp         # TVOC sensor driver
│       ├── unit_ENV3.hpp/cpp          # ENVIII composite unit
│       └── unit_ENV4.hpp/cpp          # ENVIV composite unit
├── examples/
│   └── UnitUnified/
│       ├── UnitCO2/PlotToSerial/      # SCD40 example
│       ├── UnitCO2L/PlotToSerial/     # SCD41 example
│       ├── UnitENV3/PlotToSerial/     # ENV3 composite example
│       ├── UnitENV4/PlotToSerial/     # ENV4 composite example
│       ├── UnitENVPro/PlotToSerial/   # BME688 example
│       └── UnitTVOC/PlotToSerial/     # SGP30 example
├── test/
│   └── embedded/
│       ├── test_scd40/                # SCD40 unit tests
│       ├── test_scd41/                # SCD41 unit tests
│       └── test_bmp280/               # BMP280 unit tests
├── platformio.ini                      # PlatformIO configuration
├── unit_co2_env.ini                    # CO2 test environments
├── unit_env3_env.ini                   # ENV3 test environments
├── unit_env4_env.ini                   # ENV4 test environments
├── unit_envpro_env.ini                 # ENVPro test environments
├── unit_tvoc_env.ini                   # TVOC test environments
├── library.properties                  # Arduino library metadata
└── library.json                        # PlatformIO library metadata
```

**File-to-Component Mapping**

| Product Name | SKU | Unit Class | Header File | Namespace |
|-------------|-----|-----------|-------------|-----------|
| Unit CO2 | U103 | `UnitSCD40` / `UnitCO2` | `unit_SCD40.hpp` | `m5::unit` |
| Unit CO2L | U104 | `UnitSCD41` / `UnitCO2L` | `unit_SCD41.hpp` | `m5::unit` |
| Unit ENVIII | U001-C | `UnitENV3` | `unit_ENV3.hpp` | `m5::unit` |
| Unit ENVIV | U001-D | `UnitENV4` | `unit_ENV4.hpp` | `m5::unit` |
| Unit ENVPro | U169 | `UnitBME688` / `UnitENVPro` | `unit_BME688.hpp` | `m5::unit` |
| Unit TVOC | U088 | `UnitSGP30` / `UnitTVOC` | `unit_SGP30.hpp` | `m5::unit` |

Sources: [src/M5UnitUnifiedENV.hpp:20-34](), [README.md:47-53]()

## Data Flow and Update Cycle

The unified interface implements a periodic update pattern managed by the M5UnitUnified framework:

**Sensor Update Flow**

```mermaid
sequenceDiagram
    participant APP as "Application<br/>loop()"
    participant MGR as "M5UnitUnified<br/>Manager"
    participant UNIT as "UnitSCD40<br/>(example)"
    participant I2C as "I2C Bus<br/>(Wire or M5HAL)"
    participant HW as "Physical Sensor"
    
    APP->>MGR: update()
    MGR->>UNIT: update()
    
    alt "Periodic measurement mode"
        UNIT->>UNIT: Check interval elapsed
        alt "Interval elapsed"
            UNIT->>I2C: Read measurement command
            I2C->>HW: I2C transaction
            HW-->>I2C: Raw sensor data
            I2C-->>UNIT: Register values
            UNIT->>UNIT: Apply calibration
            UNIT->>UNIT: Store in CircularBuffer
        else "Interval not elapsed"
            UNIT->>UNIT: Return cached data
        end
    else "Single-shot mode"
        UNIT->>I2C: Trigger measurement
        I2C->>HW: Measurement command
        UNIT->>UNIT: Wait for ready
        UNIT->>I2C: Read result
        I2C->>HW: Read registers
        HW-->>I2C: Measurement data
        I2C-->>UNIT: Raw values
        UNIT->>UNIT: Compensate and store
    end
    
    UNIT-->>MGR: Update status
    MGR-->>APP: Update complete
    
    APP->>UNIT: co2() accessor
    UNIT-->>APP: Latest CO2 value
```

**Composite Unit Data Aggregation**

For composite units like `UnitENV3` and `UnitENV4`, the parent unit coordinates child sensor updates:

```mermaid
graph LR
    APP["Application"]
    ENV3["UnitENV3<br/>parent"]
    SHT30["UnitSHT30<br/>component"]
    QMP["UnitQMP6988<br/>component"]
    ADAPTER["I2CAdapter"]
    BUS["I2C Bus"]
    
    APP -->|"update()"| ENV3
    ENV3 -->|"component().update()"| SHT30
    ENV3 -->|"component().update()"| QMP
    
    SHT30 -->|"via adapter"| ADAPTER
    QMP -->|"via adapter"| ADAPTER
    ADAPTER --> BUS
    
    APP -->|"temperature()"| ENV3
    APP -->|"humidity()"| ENV3
    APP -->|"pressure()"| ENV3
    
    ENV3 -.->|"delegates to"| SHT30
    ENV3 -.->|"delegates to"| QMP
```

Sources: [src/M5UnitUnifiedENV.hpp:26](), Example structure inferred from composite unit patterns

## Testing Infrastructure

The library includes embedded unit tests using GoogleTest, configured in [platformio.ini:11]():

```
test_framework = googletest
test_build_src = true
```

**Test Coverage by Sensor**

| Sensor Unit | Test Directory | Test Environments | Configuration File |
|------------|----------------|-------------------|-------------------|
| SCD40 | `test/embedded/test_scd40` | 14 boards × 1 test | [unit_co2_env.ini:5-88]() |
| SCD41 | `test/embedded/test_scd41` | 14 boards × 1 test | [unit_co2_env.ini:91-174]() |
| BMP280 | `test/embedded/test_bmp280` | Multiple boards | Unit-specific config |

Test environments inherit from board configurations and add `${test_fw.lib_deps}` which is defined in [platformio.ini:201-202]():

```
[test_fw]
lib_deps = google/googletest@1.12.1
```

Sources: [platformio.ini:11-12](), [platformio.ini:201-202](), [unit_co2_env.ini:5-174]()

## Platform-Specific Considerations

### NanoC6 BSEC2 Exclusion

The NanoC6 board environment excludes the BSEC2 library due to resource constraints. This is implemented in [platformio.ini:89-97]():

```ini
[NanoC6]
extends = m5base
board = m5stack-nanoc6
platform = https://github.com/platformio/platform-espressif32.git
platform_packages =
	platformio/framework-arduinoespressif32 @ https://github.com/espressif/arduino-esp32.git#3.0.7
	platformio/framework-arduinoespressif32-libs @ https://github.com/espressif/esp32-arduino-libs.git#idf-release/v5.1
board_build.partitions = default.csv
lib_deps = ${env.lib_deps}
```

Note the absence of `${bsec2.lib_deps}` which is present in all other board configurations. This means the BME688/ENVPro unit will not have IAQ calculation capabilities on NanoC6.

### ESP32 Platform Version Matrix

The library supports a wide range of ESP32 platform versions to maintain compatibility:

| Platform Version | Espressif32 Package | Arduino Core Version | Status |
|-----------------|-------------------|---------------------|---------|
| 6.8.1 | `espressif32 @ 6.8.1` | Latest | Primary |
| 6.6.0 | `espressif32 @ 6.6.0` | Stable | Supported |
| 6.0.1 | `espressif32 @ 6.0.1` | Stable | Supported |
| 5.4.0 | `espressif32 @ 5.4.0` | Stable | Supported |
| 4.4.0 | `espressif32 @ 4.4.0` | Legacy | Supported |

Sources: [platformio.ini:89-97](), [platformio.ini:138-156](), [README.md:85]()