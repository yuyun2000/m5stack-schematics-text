M5Unit-ENV Supported Boards and Platforms

# Supported Boards and Platforms

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [.github/workflows/arduino-esp-v2-build-check.yml](.github/workflows/arduino-esp-v2-build-check.yml)
- [.github/workflows/arduino-esp-v3-build-check.yml](.github/workflows/arduino-esp-v3-build-check.yml)
- [.github/workflows/arduino-m5-build-check.yml](.github/workflows/arduino-m5-build-check.yml)
- [platformio.ini](platformio.ini)
- [src/M5UnitUnifiedENV.hpp](src/M5UnitUnifiedENV.hpp)
- [unit_co2_env.ini](unit_co2_env.ini)

</details>



This page documents the comprehensive list of M5Stack boards and ESP32 platform versions supported by the M5Unit-ENV library. It covers board configurations in both PlatformIO and Arduino ecosystems, platform version compatibility, and platform-specific limitations (particularly BSEC2 exclusion from NanoC6).

For detailed PlatformIO environment configuration, see [PlatformIO Configuration](#6.1). For Arduino-specific setup, see [Arduino IDE Integration](#6.3).

## Overview

The library supports **14 distinct M5Stack board configurations** across multiple product lines (Core, Atom, Stick, Stamp series) and validates builds against **three major platform variants**:

- **ESP32 v3** (arduino-esp32:esp32@3.0.4): 18 boards
- **ESP32 v2** (arduino-esp32:esp32@2.0.17): 7 boards  
- **M5Stack** (m5stack:esp32@3.2.1): 19 boards (includes AtomS3R, DinMeter)

The library also supports PlatformIO with ESP32 platform versions ranging from 4.4.0 to 6.8.1, providing broad compatibility across hardware generations and framework versions.

## Board Categories and Configurations

### Core Series Boards

The flagship M5Stack devices with full-featured ESP32 modules and integrated displays.

```mermaid
graph TB
    subgraph CoreFamily["Core Series Boards"]
        Core["Core<br/>[Core]<br/>board: m5stack-grey"]
        Core2["Core2<br/>[Core2]<br/>board: m5stack-core2"]
        CoreS3["CoreS3<br/>[CoreS3]<br/>board: m5stack-cores3"]
        Fire["Fire<br/>[Fire]<br/>board: m5stack-fire"]
    end
    
    subgraph BaseConfig["Base Configuration [m5base]"]
        MonSpeed["monitor_speed: 115200"]
        UpSpeed["upload_speed: 1500000"]
        TestIgnore["test_ignore: native/*"]
    end
    
    subgraph Deps["Dependencies"]
        M5U["M5Unified"]
        M5UU["M5UnitUnified"]
        BME68X["BME68x Sensor library"]
        BSEC2["bsec2"]
    end
    
    Core -.->|extends| BaseConfig
    Core2 -.->|extends| BaseConfig
    CoreS3 -.->|extends| BaseConfig
    Fire -.->|extends| BaseConfig
    
    Core --> M5U
    Core --> M5UU
    Core --> BME68X
    Core --> BSEC2
    
    Core2 --> M5U
    Core2 --> M5UU
    Core2 --> BME68X
    Core2 --> BSEC2
    
    CoreS3 --> M5U
    CoreS3 --> M5UU
    CoreS3 --> BME68X
    CoreS3 --> BSEC2
    
    Fire --> M5U
    Fire --> M5UU
    Fire --> BME68X
    Fire --> BSEC2
```

**Board Configurations:**

| Board Name | PlatformIO Section | Board ID | BSEC2 Support |
|------------|-------------------|----------|---------------|
| Core | `[Core]` | `m5stack-grey` | ✓ |
| Core2 | `[Core2]` | `m5stack-core2` | ✓ |
| CoreS3 | `[CoreS3]` | `m5stack-cores3` | ✓ |
| Fire | `[Fire]` | `m5stack-fire` | ✓ |

**Sources:** [platformio.ini:28-53]()

### Atom Series Boards

Compact ESP32 modules designed for space-constrained applications.

```mermaid
graph TB
    subgraph AtomFamily["Atom Series Boards"]
        AtomMatrix["AtomMatrix<br/>[AtomMatrix]<br/>board: m5stack-atom"]
        AtomS3["AtomS3<br/>[AtomS3]<br/>board: m5stack-atoms3"]
        AtomS3R["AtomS3R<br/>[AtomS3R]<br/>board: m5stack-atoms3r<br/>Uses custom JSON"]
    end
    
    subgraph AtomBoards["Custom Board Definitions"]
        BoardJSON["./boards/m5stack-atoms3r.json"]
    end
    
    AtomS3R -.->|requires| BoardJSON
```

**Board Configurations:**

| Board Name | PlatformIO Section | Board ID | BSEC2 Support | Notes |
|------------|-------------------|----------|---------------|-------|
| AtomMatrix | `[AtomMatrix]` | `m5stack-atom` | ✓ | |
| AtomS3 | `[AtomS3]` | `m5stack-atoms3` | ✓ | |
| AtomS3R | `[AtomS3R]` | `m5stack-atoms3r` | ✓ | Custom board JSON |

**Sources:** [platformio.ini:69-86]()

### Stick Series Boards

Portable handheld devices with integrated batteries.

| Board Name | PlatformIO Section | Board ID | BSEC2 Support |
|------------|-------------------|----------|---------------|
| StickCPlus | `[StickCPlus]` | `m5stick-c` | ✓ |
| StickCPlus2 | `[StickCPlus2]` | `m5stick-cplus2` | ✓ |

**Sources:** [platformio.ini:99-110]()

### Stamp Series Boards

Low-profile ESP32 modules for embedded integration, including specialized display variants.

```mermaid
graph TB
    subgraph StampFamily["Stamp Series Boards"]
        StampS3["StampS3<br/>[StampS3]<br/>board: m5stack-stamps3<br/>Includes: M5Capsule, M5DinMeter"]
        Dial["Dial<br/>[Dial]<br/>board: m5stack-stamps3<br/>+ M5Dial library"]
    end
    
    subgraph DialSpecific["Dial-Specific Dependencies"]
        M5DialLib["m5stack/M5Dial"]
    end
    
    Dial --> M5DialLib
```

**Board Configurations:**

| Board Name | PlatformIO Section | Board ID | BSEC2 Support | Additional Dependencies |
|------------|-------------------|----------|---------------|------------------------|
| StampS3 | `[StampS3]` | `m5stack-stamps3` | ✓ | Includes Capsule, DinMeter |
| Dial | `[Dial]` | `m5stack-stamps3` | ✓ | `m5stack/M5Dial` |

**Sources:** [platformio.ini:55-67]()

### E-Paper Display Boards

Specialized boards with e-paper displays for low-power applications.

| Board Name | PlatformIO Section | Board ID | BSEC2 Support |
|------------|-------------------|----------|---------------|
| Paper | `[Paper]` | `m5stack-fire` | ✓ |
| CoreInk | `[CoreInk]` | `m5stack-coreink` | ✓ |

**Sources:** [platformio.ini:112-122]()

### ESP32-C6 Board (NanoC6)

The NanoC6 represents a special case with platform-specific limitations.

```mermaid
graph TB
    subgraph NanoC6Config["NanoC6 Configuration [NanoC6]"]
        Board["board: m5stack-nanoc6"]
        Platform["platform: GitHub ESP32"]
        FW["framework-arduinoespressif32"]
        Libs["framework-arduinoespressif32-libs"]
        Part["partitions: default.csv"]
    end
    
    subgraph Exclusions["Library Exclusions"]
        NoBSEC2["❌ BSEC2 Not Included"]
        Reason["Reason: Resource constraints"]
    end
    
    subgraph GitDeps["GitHub Dependencies"]
        ESPPlatform["platformio/platform-espressif32.git"]
        Arduino["espressif/arduino-esp32.git#3.0.7"]
        ArduinoLibs["espressif/esp32-arduino-libs.git#idf-release/v5.1"]
    end
    
    NanoC6Config --> Exclusions
    Platform -.->|uses| ESPPlatform
    FW -.->|uses| Arduino
    Libs -.->|uses| ArduinoLibs
```

**NanoC6 Configuration:**

| Property | Value |
|----------|-------|
| PlatformIO Section | `[NanoC6]` |
| Board ID | `m5stack-nanoc6` |
| Platform Source | GitHub: `platformio/platform-espressif32.git` |
| Framework | GitHub: `espressif/arduino-esp32.git#3.0.7` |
| Framework Libs | GitHub: `espressif/esp32-arduino-libs.git#idf-release/v5.1` |
| Partitions | `default.csv` |
| BSEC2 Support | ❌ **Not Supported** |
| Base Dependencies | M5Unified, M5UnitUnified, BME68x Sensor library |

**Important:** NanoC6 explicitly excludes the BSEC2 library due to resource constraints on the ESP32-C6 chip. This means **UnitENVPro (BME688) IAQ features are not available** on this platform. Basic sensor readings (temperature, humidity, pressure, raw gas resistance) remain functional.

**Sources:** [platformio.ini:88-97]()

## Platform Version Matrix

### PlatformIO Platform Versions

The library defines multiple platform version configurations for testing and compatibility validation.

```mermaid
graph LR
    subgraph Versions["Platform Version Configurations"]
        Latest["arduino_latest<br/>espressif32@6.8.1"]
        V6_6["arduino_6_6_0<br/>espressif32@6.6.0"]
        V6_0["arduino_6_0_1<br/>espressif32@6.0.1"]
        V5_4["arduino_5_4_0<br/>espressif32@5.4.0"]
        V4_4["arduino_4_4_0<br/>espressif32@4.4.0"]
        IDF["esp-idf<br/>espressif32@6.8.1<br/>framework: espidf"]
    end
    
    subgraph Framework["Framework Selection"]
        Arduino["framework: arduino"]
        ESPIDF["framework: espidf"]
    end
    
    Latest --> Arduino
    V6_6 --> Arduino
    V6_0 --> Arduino
    V5_4 --> Arduino
    V4_4 --> Arduino
    IDF --> ESPIDF
```

**Platform Version Reference:**

| Configuration Name | Platform Version | Framework | Usage |
|-------------------|------------------|-----------|-------|
| `[arduino_latest]` | `espressif32@6.8.1` | arduino | Latest stable release |
| `[arduino_6_6_0]` | `espressif32@6.6.0` | arduino | Specific version testing |
| `[arduino_6_0_1]` | `espressif32@6.0.1` | arduino | Compatibility testing |
| `[arduino_5_4_0]` | `espressif32@5.4.0` | arduino | Legacy support |
| `[arduino_4_4_0]` | `espressif32@4.4.0` | arduino | Minimum version |
| `[esp-idf]` | `espressif32@6.8.1` | espidf | ESP-IDF native framework |

**Sources:** [platformio.ini:137-164]()

### Arduino CI Platform Matrix

The CI/CD pipeline validates builds across three Arduino platform variants with different board sets.

```mermaid
graph TB
    subgraph ESP32v3["ESP32 v3.0.4 Platform"]
        V3Boards["18 Boards<br/>m5stack_atom<br/>m5stack_atoms3<br/>m5stack_capsule<br/>m5stack_core<br/>m5stack_core2<br/>m5stack_coreink<br/>m5stack_cores3<br/>m5stack_dial<br/>m5stack_fire<br/>m5stack_nanoc6<br/>m5stack_paper<br/>m5stack_stamp_s3<br/>m5stack_stickc_plus<br/>m5stack_stickc_plus2"]
    end
    
    subgraph ESP32v2["ESP32 v2.0.17 Platform"]
        V2Boards["7 Boards<br/>m5stack-atom<br/>m5stack-atoms3<br/>m5stack-core-esp32<br/>m5stack-core2<br/>m5stack-coreink<br/>m5stack-cores3<br/>m5stack-fire"]
    end
    
    subgraph M5Stack["M5Stack v3.2.1 Platform"]
        M5Boards["19 Boards<br/>m5stack_atom<br/>m5stack_atoms3<br/>m5stack_atoms3r<br/>m5stack_capsule<br/>m5stack_core<br/>m5stack_core2<br/>m5stack_coreink<br/>m5stack_cores3<br/>m5stack_dial<br/>m5stack_dinmeter<br/>m5stack_fire<br/>m5stack_paper<br/>m5stack_stamp_s3<br/>m5stack_stickc_plus<br/>m5stack_stickc_plus2"]
    end
```

**Arduino Platform Comparison:**

| Platform Variant | Version | Board Count | Unique Boards | Board ID Format |
|-----------------|---------|-------------|---------------|-----------------|
| ESP32 v3 | 3.0.4 | 18 | nanoc6 | `m5stack_*` (underscore) |
| ESP32 v2 | 2.0.17 | 7 | Legacy naming | `m5stack-*` (hyphen) |
| M5Stack | 3.2.1 | 19 | atoms3r, dinmeter | `m5stack_*` (underscore) |

**Note:** Board ID naming conventions differ between platforms:
- **ESP32 v3 and M5Stack:** Use underscores (`m5stack_atom`)
- **ESP32 v2:** Use hyphens (`m5stack-atom`)

**Sources:** [.github/workflows/arduino-esp-v3-build-check.yml:71-95](), [.github/workflows/arduino-esp-v2-build-check.yml:71-78](), [.github/workflows/arduino-m5-build-check.yml:71-96]()

## Board Configuration Details

### Base Configuration Inheritance

All boards inherit from the `[m5base]` configuration, which defines common serial and upload parameters.

```mermaid
graph TB
    subgraph BaseConfig["[m5base] Configuration"]
        MS["monitor_speed = 115200"]
        MF["monitor_filters = esp32_exception_decoder, time"]
        US["upload_speed = 1500000"]
        TS["test_speed = 115200"]
        TI["test_ignore = native/*"]
    end
    
    subgraph BoardExtends["Board Extends [m5base]"]
        Core["[Core]"]
        Core2["[Core2]"]
        CoreS3["[CoreS3]"]
        Fire["[Fire]"]
        StampS3["[StampS3]"]
        Dial["[Dial]"]
        AtomMatrix["[AtomMatrix]"]
        AtomS3["[AtomS3]"]
        AtomS3R["[AtomS3R]"]
        NanoC6["[NanoC6]"]
        StickCPlus["[StickCPlus]"]
        StickCPlus2["[StickCPlus2]"]
        Paper["[Paper]"]
        CoreInk["[CoreInk]"]
    end
    
    BaseConfig -.->|extends| Core
    BaseConfig -.->|extends| Core2
    BaseConfig -.->|extends| CoreS3
    BaseConfig -.->|extends| Fire
    BaseConfig -.->|extends| StampS3
    BaseConfig -.->|extends| Dial
    BaseConfig -.->|extends| AtomMatrix
    BaseConfig -.->|extends| AtomS3
    BaseConfig -.->|extends| AtomS3R
    BaseConfig -.->|extends| NanoC6
    BaseConfig -.->|extends| StickCPlus
    BaseConfig -.->|extends| StickCPlus2
    BaseConfig -.->|extends| Paper
    BaseConfig -.->|extends| CoreInk
```

**Sources:** [platformio.ini:21-26]()

### Library Dependencies by Board

Most boards share identical library dependencies, with NanoC6 as the notable exception.

```mermaid
graph TB
    subgraph StandardBoards["Standard Boards<br/>13 boards"]
        StdDeps["lib_deps:<br/>M5Unified<br/>M5UnitUnified<br/>BME68x Sensor library<br/>bsec2"]
    end
    
    subgraph NanoC6Board["NanoC6 Board"]
        NanoDeps["lib_deps:<br/>M5Unified<br/>M5UnitUnified<br/>BME68x Sensor library<br/>❌ NO bsec2"]
    end
    
    subgraph BSEC2Config["[bsec2] Configuration"]
        BSEC2Lib["boschsensortec/bsec2@>=1.10.2610"]
    end
    
    StdDeps --> BSEC2Config
    NanoDeps -.->|excluded| BSEC2Config
```

**Sources:** [platformio.ini:8-19](), [platformio.ini:97]()

## Build Options and Test Configuration

### Build Type Options

The library provides three build option configurations for different development needs.

| Option Name | Build Type | Debug Levels | Defines | Use Case |
|-------------|-----------|--------------|---------|----------|
| `[option_release]` | release | 3 | `CORE_DEBUG_LEVEL=3`<br/>`LOG_LOCAL_LEVEL=3`<br/>`APP_LOG_LEVEL=3`<br/>`M5_LOG_LEVEL=3` | Production builds |
| `[option_log]` | release | 5 | `CORE_DEBUG_LEVEL=5`<br/>`LOG_LOCAL_LEVEL=5`<br/>`APP_LOG_LEVEL=5` | Debugging with optimizations |
| `[option_debug]` | debug | 5 | `CORE_DEBUG_LEVEL=5`<br/>`LOG_LOCAL_LEVEL=5`<br/>`APP_LOG_LEVEL=5`<br/>`DEBUG` | Full debugging |

**Sources:** [platformio.ini:167-189]()

### Test Framework Configuration

Embedded tests use GoogleTest framework with specific version requirements.

```mermaid
graph TB
    subgraph TestConfig["Test Configuration"]
        TF["test_framework = googletest"]
        TBS["test_build_src = true"]
        TFW["google/googletest@1.12.1"]
    end
    
    subgraph TestEnvs["Test Environments"]
        SCD40["test_scd40"]
        SCD41["test_scd41"]
        BMP280["test_bmp280"]
    end
    
    TestConfig --> TestEnvs
```

**Test Environment Pattern:**
- Environment name format: `test_{SENSOR}_{BOARD}`
- Example: `[env:test_SCD40_Core]`
- All 14 boards tested for SCD40 and SCD41 sensors
- Uses `arduino_latest` platform (espressif32@6.8.1)

**Sources:** [platformio.ini:11-12](), [platformio.ini:201-202](), [unit_co2_env.ini:5-88]()

## Platform-Specific Considerations

### BSEC2 Library Exclusion

The Bosch BSEC2 library for advanced air quality metrics (IAQ, CO2eq, VOC) is excluded from the NanoC6 platform due to resource constraints of the ESP32-C6 chip.

**Impact:**
- **UnitENVPro (BME688)** functionality limited to basic readings on NanoC6
- Temperature, humidity, pressure, and raw gas resistance remain available
- IAQ algorithm, CO2 equivalent, and VOC index calculations unavailable

**Configuration Mapping:**

```mermaid
graph TB
    subgraph AllBoards["All Boards"]
        Standard13["13 Standard Boards"]
        NanoC6Board["NanoC6"]
    end
    
    subgraph LibraryInclusion["Library Dependencies"]
        BSEC2["bsec2@>=1.10.2610"]
        BME68X["BME68x Sensor library@>=1.3.40408"]
    end
    
    subgraph Features["Feature Availability"]
        BasicENVPro["BME688 Basic Features:<br/>Temperature<br/>Humidity<br/>Pressure<br/>Raw Gas Resistance"]
        AdvENVPro["BME688 Advanced Features:<br/>IAQ Index<br/>CO2 Equivalent<br/>VOC Index<br/>Air Quality Classification"]
    end
    
    Standard13 --> BSEC2
    Standard13 --> BME68X
    NanoC6Board --> BME68X
    NanoC6Board -.->|excluded| BSEC2
    
    BSEC2 --> AdvENVPro
    BME68X --> BasicENVPro
```

**Sources:** [platformio.ini:89-97](), [platformio.ini:18-19]()

### Custom Board JSON Definitions

Some boards require custom JSON definitions stored in the `./boards/` directory.

| Board | Custom JSON File | Reason |
|-------|-----------------|--------|
| AtomS3R | `./boards/m5stack-atoms3r.json` | Board variant not in standard platform |
| NanoC6 | `./boards/m5stack-nanoc6.json` | ESP32-C6 support, custom configuration |
| StickCPlus2 | `./boards/m5stick-cplus2.json` | New board variant |

**Sources:** [platformio.ini:82-86](), [platformio.ini:88-97](), [platformio.ini:106-110]()

## Board Selection Guide

### By Sensor Unit Support

All boards support all sensor units **except** NanoC6's limitation with BME688 advanced features.

| Sensor Unit | All Boards | NanoC6 Special Case |
|-------------|-----------|---------------------|
| UnitCO2 (SCD40) | ✓ Full support | ✓ Full support |
| UnitCO2L (SCD41) | ✓ Full support | ✓ Full support |
| UnitENVIII (ENV3) | ✓ Full support | ✓ Full support |
| UnitENVIV (ENV4) | ✓ Full support | ✓ Full support |
| UnitTVOC (SGP30) | ✓ Full support | ✓ Full support |
| UnitENVPro (BME688) | ✓ Full support | ⚠️ Basic only (no IAQ) |

### By CI Validation Coverage

```mermaid
graph TB
    subgraph CIMatrix["CI Build Validation Matrix"]
        Units["6 Sensor Units:<br/>UnitCO2, UnitCO2L<br/>UnitENVIII, UnitENVIV<br/>UnitTVOC, UnitENVPro"]
        
        ESP32v3["ESP32 v3.0.4<br/>18 boards"]
        ESP32v2["ESP32 v2.0.17<br/>7 boards"]
        M5Stack["M5Stack v3.2.1<br/>19 boards"]
        
        Combos["Total Combinations:<br/>ESP32v3: 6×18 = 108<br/>ESP32v2: 6×7 = 42<br/>M5Stack: 6×19 = 114<br/>Grand Total: 264"]
    end
    
    Units --> ESP32v3
    Units --> ESP32v2
    Units --> M5Stack
    
    ESP32v3 --> Combos
    ESP32v2 --> Combos
    M5Stack --> Combos
```

**Highest Coverage Boards (validated across all 3 platforms):**
- m5stack_atom / m5stack-atom
- m5stack_atoms3 / m5stack-atoms3
- m5stack_core / m5stack-core-esp32
- m5stack_core2
- m5stack_coreink
- m5stack_cores3
- m5stack_fire

**Platform-Exclusive Boards:**
- **AtomS3R, DinMeter:** Only on M5Stack platform
- **NanoC6:** Only on ESP32 v3 platform

**Sources:** [.github/workflows/arduino-esp-v3-build-check.yml:63-69](), [.github/workflows/arduino-esp-v2-build-check.yml:63-69](), [.github/workflows/arduino-m5-build-check.yml:63-69]()