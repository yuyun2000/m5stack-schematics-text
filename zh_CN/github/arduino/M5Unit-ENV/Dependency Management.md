M5Unit-ENV Dependency Management

# Dependency Management

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [library.json](library.json)
- [library.properties](library.properties)
- [src/unit/unit_BME688.cpp](src/unit/unit_BME688.cpp)
- [src/unit/unit_BME688.hpp](src/unit/unit_BME688.hpp)

</details>



This document details all external dependencies required by the M5Unit-ENV library, their version requirements, platform-specific exclusions, and how they integrate with different build systems. It covers both the conventional and unified interface dependency paths.

For information about the architectural differences between interfaces, see [Conventional vs Unified Interface](#3.1). For build system configuration details, see [PlatformIO Configuration](#6.1) and [Arduino IDE Integration](#6.3).

## Dependency Architecture

The M5Unit-ENV library has two distinct dependency paths depending on which interface is used. The conventional interface (`M5UnitENV.h`) relies primarily on third-party vendor libraries (Adafruit, Sensirion), while the unified interface (`M5UnitUnifiedENV.h`) builds on the M5Stack ecosystem framework.

**Dual-Path Dependency Architecture**

```mermaid
graph TB
    subgraph "Entry Points"
        CONV["M5UnitENV.h<br/>(Conventional)"]
        UNIFIED["M5UnitUnifiedENV.h<br/>(Unified)"]
    end
    
    subgraph "M5Stack Ecosystem<br/>Unified Path Only"
        M5UU["M5UnitUnified<br/>>=0.1.0"]
        M5UTIL["M5Utility<br/>CRC-8, mmh3 hash"]
        M5HAL["M5HAL<br/>I2C/GPIO abstraction"]
    end
    
    subgraph "Bosch Ecosystem<br/>Both Paths"
        BME68X["BME68x Sensor library<br/>>=1.3.40408<br/>Low-level driver"]
        BSEC2["bsec2<br/>>=1.10.2610<br/>IAQ algorithms<br/>⚠ Excluded: NanoC6"]
    end
    
    subgraph "Adafruit Ecosystem<br/>Conventional Path"
        ADA_BMP["Adafruit_BMP280_Library<br/>BMP280 driver"]
        ADA_SENS["Adafruit_Sensor<br/>Unified sensor API"]
    end
    
    subgraph "Sensirion Ecosystem<br/>Conventional Path"
        SENS_SCD["Sensirion I2C SCD4x<br/>CO2 sensors"]
        SENS_SHT["Sensirion I2C SHT4x<br/>Temp/Humidity"]
        SENS_CORE["Sensirion Core<br/>Common I2C functions"]
    end
    
    CONV --> ADA_BMP
    CONV --> SENS_SCD
    CONV --> SENS_SHT
    CONV --> BME68X
    CONV --> BSEC2
    
    UNIFIED --> M5UU
    UNIFIED --> BME68X
    UNIFIED --> BSEC2
    
    M5UU --> M5UTIL
    M5UU --> M5HAL
    
    ADA_BMP --> ADA_SENS
    SENS_SCD --> SENS_CORE
    SENS_SHT --> SENS_CORE
```

Sources: [library.properties:11](), [library.json:13-16](), [README.md:29-35](), [README.md:78-85]()

## Core M5Stack Dependencies

The unified interface requires the M5Stack ecosystem libraries, which provide framework services, hardware abstraction, and utility functions. These dependencies are **only required when using `M5UnitUnifiedENV.h`**.

| Library | Minimum Version | Purpose | Key Components |
|---------|----------------|---------|----------------|
| **M5UnitUnified** | >=0.1.0 | Unit management framework | Multi-unit discovery, lifecycle management, adapter patterns |
| **M5Utility** | (latest) | Common utilities | CRC-8 calculation, MurmurHash3 (mmh3) |
| **M5HAL** | (latest) | Hardware abstraction layer | I2C bus adapter, GPIO management |

The `M5Utility` library is specifically used for hash calculation in unit identification and CRC validation, as seen in [src/unit/unit_BME688.cpp:21]() where `m5::utility::mmh3` is imported for the unit UID generation [src/unit/unit_BME688.cpp:132]().

Sources: [library.json:13-16](), [README.md:78-82](), [src/unit/unit_BME688.cpp:17](), [src/unit/unit_BME688.cpp:21]()

## Bosch Sensortec Dependencies

The BME688 sensor (ENVPro unit) requires two Bosch libraries. These are **required for both conventional and unified interfaces** when using the BME688/ENVPro sensor.

**BME688 Dependency Stack**

```mermaid
graph TB
    BME688_UNIT["UnitBME688<br/>src/unit/unit_BME688.cpp"]
    
    subgraph "Conditional Compilation"
        BSEC2_CHECK{"UNIT_BME688_USING_BSEC2<br/>defined?"}
        BSEC2_PATH["BSEC2 Library Path<br/>IAQ calculations enabled"]
        RAW_PATH["Raw Data Only Path<br/>No IAQ calculations"]
    end
    
    BME68X_LIB["BME68x Sensor library<br/>bme68xLibrary.h (Arduino)<br/>bme68x/bme68x.h (ESP-IDF)"]
    BSEC2_LIB["bsec2<br/>bsec2.h (Arduino)<br/>inc/bsec_datatypes.h (ESP-IDF)"]
    
    BME688_UNIT --> BSEC2_CHECK
    BSEC2_CHECK -->|"ESP32/S3/C3"| BSEC2_PATH
    BSEC2_CHECK -->|"NanoC6 or<br/>not defined"| RAW_PATH
    
    BSEC2_PATH --> BSEC2_LIB
    BSEC2_PATH --> BME68X_LIB
    RAW_PATH --> BME68X_LIB
    
    BSEC2_LIB -.->|"Provides"| IAQ["IAQ<br/>CO2eq<br/>VOC<br/>bsec_do_steps()"]
    BME68X_LIB -.->|"Provides"| RAW["bme68x_init()<br/>bme68x_get_data()<br/>bme68x_set_conf()"]
```

Sources: [src/unit/unit_BME688.hpp:22-31](), [src/unit/unit_BME688.cpp:11-16]()

### BME68x Sensor Library

**Version Requirement:** `>=1.3.40408`

This library provides low-level sensor communication functions:
- Sensor initialization: `bme68x_init()` [src/unit/unit_BME688.cpp:182]()
- Configuration management: `bme68x_set_conf()`, `bme68x_get_conf()` [src/unit/unit_BME688.cpp:222]()
- Data retrieval: `bme68x_get_data()` [src/unit/unit_BME688.cpp:783]()
- Mode control: `bme68x_set_op_mode()`, `bme68x_get_op_mode()` [src/unit/unit_BME688.cpp:678](), [src/unit/unit_BME688.cpp:688]()
- Heater configuration: `bme68x_set_heatr_conf()` [src/unit/unit_BME688.cpp:669]()

The library is conditionally included based on the build environment [src/unit/unit_BME688.hpp:16-20]():
- Arduino: `#include <bme68xLibrary.h>`
- ESP-IDF: `#include <bme68x/bme68x.h>`

Sources: [library.json:15](), [src/unit/unit_BME688.hpp:16-20](), [src/unit/unit_BME688.cpp:182-225]()

### BSEC2 (Bosch Sensortec Environmental Cluster 2)

**Version Requirement:** `>=1.10.2610`

**Platform Exclusion:** Not available on ESP32-C6 (NanoC6)

BSEC2 is Bosch's proprietary air quality algorithm library that provides advanced metrics:
- **IAQ (Indoor Air Quality):** `BSEC_OUTPUT_IAQ`, `BSEC_OUTPUT_STATIC_IAQ`
- **CO2 Equivalent:** `BSEC_OUTPUT_CO2_EQUIVALENT`
- **VOC (Breath VOC):** `BSEC_OUTPUT_BREATH_VOC_EQUIVALENT`
- **Heat-Compensated Values:** Temperature and humidity with heater compensation
- **Gas Estimates:** Four-class gas classification

The library is conditionally compiled based on the target platform [src/unit/unit_BME688.hpp:22-31]():

```cpp
#if defined(CONFIG_IDF_TARGET_ESP32) || defined(CONFIG_IDF_TARGET_ESP32S3) || 
    defined(CONFIG_IDF_TARGET_ESP32C3)
#define UNIT_BME688_USING_BSEC2
#endif
```

When BSEC2 is available, it provides the `bsec_do_steps()` function [src/unit/unit_BME688.cpp:1012]() to process raw sensor data into high-level air quality metrics. The default configuration is loaded from `config/bme688/bme688_sel_33v_3s_4d/bsec_selectivity.txt` [src/unit/unit_BME688.cpp:76]().

**BSEC2 Integration Functions:**

| Function | Purpose | Line Reference |
|----------|---------|----------------|
| `bsec_init()` | Initialize BSEC2 library | [src/unit/unit_BME688.cpp:188]() |
| `bsec_set_configuration()` | Load algorithm config | [src/unit/unit_BME688.cpp:808]() |
| `bsec_update_subscription()` | Subscribe to virtual sensors | [src/unit/unit_BME688.cpp:848]() |
| `bsec_sensor_control()` | Get next measurement settings | [src/unit/unit_BME688.cpp:295]() |
| `bsec_do_steps()` | Process raw data to outputs | [src/unit/unit_BME688.cpp:1012]() |
| `bsec_get_state()` / `bsec_set_state()` | State persistence | [src/unit/unit_BME688.cpp:815-823]() |

Sources: [library.json:16](), [README.md:85](), [src/unit/unit_BME688.hpp:22-31](), [src/unit/unit_BME688.cpp:11-16](), [src/unit/unit_BME688.cpp:187-200](), [src/unit/unit_BME688.cpp:786-1019]()

## Adafruit Dependencies

The conventional interface uses Adafruit libraries for the BMP280 pressure sensor (used in ENVIV and BPS units). These are **only required when using `M5UnitENV.h`**.

| Library | Purpose | Key Classes/Functions |
|---------|---------|----------------------|
| **Adafruit_BMP280_Library** | BMP280 sensor driver | Temperature, pressure measurement |
| **Adafruit_Sensor** | Unified sensor interface | Common sensor API abstraction |

The BMP280 driver depends on the unified sensor library, which provides a common interface pattern used across Adafruit's sensor ecosystem.

Sources: [README.md:31-32](), [library.properties:11]()

## Sensirion Dependencies

The conventional interface uses Sensirion libraries for CO2 sensors (SCD40, SCD41) and advanced temperature/humidity sensors (SHT40). These are **only required when using `M5UnitENV.h`**.

**Sensirion Dependency Hierarchy**

```mermaid
graph TB
    subgraph "Application Layer"
        SCD40_APP["UnitCO2<br/>SCD40"]
        SCD41_APP["UnitCO2L<br/>SCD41"]
        SHT40_APP["UnitSHT40"]
    end
    
    subgraph "Sensirion Driver Layer"
        SCD4X["Sensirion I2C SCD4x<br/>scd4x_i2c.h"]
        SHT4X["Sensirion I2C SHT4x<br/>sht4x_i2c.h"]
    end
    
    subgraph "Sensirion Core Layer"
        CORE["Sensirion Core<br/>sensirion_common.h<br/>sensirion_i2c.h"]
    end
    
    SCD40_APP --> SCD4X
    SCD41_APP --> SCD4X
    SHT40_APP --> SHT4X
    
    SCD4X --> CORE
    SHT4X --> CORE
    
    CORE -.->|"Provides"| FUNCS["CRC calculation<br/>I2C communication<br/>Delay functions<br/>Error handling"]
```

Sources: [README.md:33-35]()

### Sensirion I2C SCD4x

Provides driver functions for SCD40 and SCD41 CO2 sensors:
- Periodic measurement control
- Single-shot measurement (SCD41 only)
- Automatic self-calibration (ASC)
- Forced recalibration (FRC)
- Temperature offset adjustment
- Altitude compensation
- Ambient pressure compensation

Sources: [README.md:33]()

### Sensirion I2C SHT4x

Provides driver functions for SHT40 temperature and humidity sensor:
- High/medium/low precision measurements
- Heater activation for condensation removal
- Serial number reading
- Soft reset functionality

Sources: [README.md:34]()

### Sensirion Core

Common utilities shared across Sensirion sensor libraries:
- I2C communication primitives
- CRC-8 validation
- Delay and timing functions
- Error code definitions

Both SCD4x and SHT4x libraries depend on this core library for basic I2C operations and data validation.

Sources: [README.md:35]()

## Dependency Version Matrix

The following table summarizes all dependencies with their version requirements and applicability:

| Library | Min Version | Interface | Platforms | Notes |
|---------|------------|-----------|-----------|-------|
| **M5UnitUnified** | >=0.1.0 | Unified only | All ESP32 | Core framework |
| **M5Utility** | (latest) | Unified only | All ESP32 | CRC, hashing |
| **M5HAL** | (latest) | Unified only | All ESP32 | Hardware abstraction |
| **BME68x Sensor library** | >=1.3.40408 | Both | All ESP32 | BME688 low-level |
| **bsec2** | >=1.10.2610 | Both | ESP32, S3, C3 | **Excluded: C6** |
| **Adafruit_BMP280_Library** | (latest) | Conventional | All ESP32 | BMP280 driver |
| **Adafruit_Sensor** | (latest) | Conventional | All ESP32 | Unified API |
| **Sensirion I2C SCD4x** | (latest) | Conventional | All ESP32 | CO2 sensors |
| **Sensirion I2C SHT4x** | (latest) | Conventional | All ESP32 | Temp/Humidity |
| **Sensirion Core** | (latest) | Conventional | All ESP32 | Common functions |

Sources: [library.properties:11](), [library.json:13-16](), [README.md:29-35](), [README.md:78-86]()

## Platform-Specific Exclusions

### BSEC2 Exclusion on ESP32-C6

The BSEC2 library is **not available** on the ESP32-C6 (NanoC6) platform due to resource constraints. This is enforced through conditional compilation:

**Platform Detection Logic:**

```mermaid
graph TD
    START["Build System"]
    CHECK_ESP32{"CONFIG_IDF_TARGET_ESP32<br/>defined?"}
    CHECK_S3{"CONFIG_IDF_TARGET_ESP32S3<br/>defined?"}
    CHECK_C3{"CONFIG_IDF_TARGET_ESP32C3<br/>defined?"}
    
    DEFINE["#define<br/>UNIT_BME688_USING_BSEC2"]
    NO_DEFINE["BSEC2 disabled<br/>Raw data only"]
    
    START --> CHECK_ESP32
    CHECK_ESP32 -->|Yes| DEFINE
    CHECK_ESP32 -->|No| CHECK_S3
    CHECK_S3 -->|Yes| DEFINE
    CHECK_S3 -->|No| CHECK_C3
    CHECK_C3 -->|Yes| DEFINE
    CHECK_C3 -->|No| NO_DEFINE
    
    DEFINE -.->|"Enables"| FEATURES["IAQ calculations<br/>CO2eq estimation<br/>VOC estimation<br/>Advanced algorithms"]
    NO_DEFINE -.->|"Limited to"| RAW["Raw temperature<br/>Raw pressure<br/>Raw humidity<br/>Raw gas resistance"]
```

Sources: [src/unit/unit_BME688.hpp:22-31]()

When BSEC2 is excluded, the BME688 sensor can still be used, but only raw sensor data is available:
- Temperature (compensated)
- Pressure (compensated)
- Humidity (compensated)
- Gas resistance (raw)

The high-level metrics (IAQ, CO2eq, VOC) require BSEC2 and are unavailable on NanoC6.

Sources: [README.md:85](), [src/unit/unit_BME688.hpp:22-31](), [src/unit/unit_BME688.cpp:11-16]()

## Build System Integration

### Arduino Library Manager

Dependencies are declared in `library.properties` using the `depends` field [library.properties:11]():

```
depends=M5UnitUnified,M5Utility,M5HAL,bsec2,BME68x Sensor library
```

The Arduino Library Manager automatically resolves and installs these dependencies when the M5Unit-ENV library is installed. Library names must match the exact names published in the Arduino Library Registry.

**Limitations:**
- Cannot specify version ranges (all dependencies install latest)
- Cannot conditionally exclude dependencies based on platform
- Both conventional and unified dependencies are always installed

Sources: [library.properties:1-11]()

### PlatformIO

Dependencies are declared in `library.json` with semantic versioning support [library.json:13-16]():

```json
"dependencies": {
    "m5stack/M5UnitUnified": ">=0.1.0",
    "boschsensortec/BME68x Sensor library": ">=1.3.40408",
    "boschsensortec/bsec2": ">=1.10.2610"
}
```

**PlatformIO Dependency Resolution:**

```mermaid
graph LR
    JSON["library.json<br/>dependencies"]
    
    subgraph "Registry Resolution"
        REG["PlatformIO Registry<br/>registry.platformio.org"]
        SEM["Semantic Version<br/>Resolver"]
    end
    
    subgraph "Installation"
        CACHE["Local Cache<br/>.pio/libdeps"]
        PROJECT["Project lib_deps"]
    end
    
    JSON --> REG
    REG --> SEM
    SEM -->|">= constraint"| CACHE
    CACHE --> PROJECT
    
    SEM -.->|"Satisfies"| VER["Latest compatible<br/>version installed"]
```

Sources: [library.json:13-16]()

**Platform-Specific Configuration:**

PlatformIO allows platform-specific dependency management in `platformio.ini` through build flags and library filtering. For BSEC2 exclusion on NanoC6, the build system relies on the conditional compilation in the source code rather than dependency exclusion.

Sources: [library.json:1-33]()

## Dependency Resolution Process

The following diagram illustrates how dependencies are resolved during the build process:

**Build-Time Dependency Resolution**

```mermaid
graph TB
    START["Build Initiated"]
    
    subgraph "Dependency Declaration"
        PROPS["library.properties<br/>(Arduino)"]
        JSON["library.json<br/>(PlatformIO)"]
    end
    
    subgraph "Platform Detection"
        DETECT["Platform Flags<br/>CONFIG_IDF_TARGET_xxx"]
        DEFINES["Preprocessor Defines<br/>UNIT_BME688_USING_BSEC2"]
    end
    
    subgraph "Conditional Compilation"
        BSEC_CHECK{"#if defined<br/>(UNIT_BME688_USING_BSEC2)"}
        INCLUDE_BSEC["#include <bsec2.h><br/>BSEC functions available"]
        EXCLUDE_BSEC["BSEC2 code excluded<br/>Raw data only"]
    end
    
    subgraph "Linking"
        LINK_ALL["Link all dependencies"]
        LINK_SUBSET["Link subset<br/>(no BSEC2)"]
    end
    
    START --> PROPS
    START --> JSON
    PROPS --> DETECT
    JSON --> DETECT
    
    DETECT --> DEFINES
    DEFINES --> BSEC_CHECK
    
    BSEC_CHECK -->|"ESP32/S3/C3"| INCLUDE_BSEC
    BSEC_CHECK -->|"C6 or undefined"| EXCLUDE_BSEC
    
    INCLUDE_BSEC --> LINK_ALL
    EXCLUDE_BSEC --> LINK_SUBSET
```

Sources: [library.properties:11](), [library.json:13-16](), [src/unit/unit_BME688.hpp:22-31](), [src/unit/unit_BME688.cpp:11-16]()

### Dependency Order

Dependencies must be resolved in the correct order due to transitive dependencies:

1. **M5HAL** (no dependencies)
2. **M5Utility** (no dependencies)
3. **M5UnitUnified** (depends on M5HAL, M5Utility)
4. **Sensirion Core** (no dependencies)
5. **Sensirion I2C SCD4x** (depends on Sensirion Core)
6. **Sensirion I2C SHT4x** (depends on Sensirion Core)
7. **Adafruit_Sensor** (no dependencies)
8. **Adafruit_BMP280_Library** (depends on Adafruit_Sensor)
9. **BME68x Sensor library** (no dependencies)
10. **bsec2** (depends on BME68x Sensor library)

Both Arduino and PlatformIO automatically handle transitive dependencies, but understanding the order helps diagnose build issues.

Sources: [library.properties:11](), [library.json:13-16](), [README.md:29-35](), [README.md:78-86]()