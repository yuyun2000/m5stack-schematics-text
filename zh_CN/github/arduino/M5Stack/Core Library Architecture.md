M5Stack Core Library Architecture

# Core Library Architecture

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [.clang-format](.clang-format)
- [.github/ISSUE_TEMPLATE/bug-report.yml](.github/ISSUE_TEMPLATE/bug-report.yml)
- [.github/workflows/Arduino-Lint-Check.yml](.github/workflows/Arduino-Lint-Check.yml)
- [.github/workflows/clang-format-check.yml](.github/workflows/clang-format-check.yml)
- [README.md](README.md)
- [docs/getting_started_cn.md](docs/getting_started_cn.md)
- [docs/getting_started_ja.md](docs/getting_started_ja.md)
- [library.json](library.json)
- [library.properties](library.properties)
- [src/M5Stack.cpp](src/M5Stack.cpp)
- [src/M5Stack.h](src/M5Stack.h)
- [src/gitTagVersion.h](src/gitTagVersion.h)
- [src/utility/Power.cpp](src/utility/Power.cpp)
- [src/utility/Power.h](src/utility/Power.h)

</details>



**⚠️ DEPRECATION NOTICE**: This library (version 0.4.6) is officially deprecated. For new projects, use [M5GFX](https://github.com/m5stack/M5GFX) for graphics and [M5Unified](https://github.com/m5stack/M5Unified) for device control. See page 1 (Overview) for migration information.

This document provides a high-level architectural overview of the M5Stack Core Library, covering the primary system components and their interactions. The library serves as a hardware abstraction layer for M5Stack Basic and Gray devices, built on the ESP32 platform.

For detailed information about specific subsystems, see: [M5Stack Class and Initialization](#2.1), [Display and Graphics System](#2.2), [Power Management](#2.3), [Audio System](#2.4), [IMU and Motion Sensing](#2.5), and [I2C Communication Utilities](#2.6).

Sources: [README.md:1-11](), [library.properties:1-11]()

## System Overview

The M5Stack library implements a **facade pattern** with the `M5Stack` class as the central coordinator. A global instance `M5` provides unified access to all hardware subsystems. The architecture is layered in three tiers: application code interacts with the `M5` object, which delegates to hardware abstraction modules (`M5Display`, `POWER`, `Button`, `SPEAKER`, `IMU`), which in turn use low-level drivers and ESP32 peripherals.

### Three-Tier Architecture Diagram

```mermaid
graph TB
    subgraph Tier1["Application Tier"]
        UserSketch["User Sketch<br/>setup() + loop()"]
        BasicExamples["Basic Examples"]
        UnitExamples["Unit Examples"]
    end
    
    subgraph Tier2["Facade API Tier"]
        M5Object["M5Stack M5<br/>(Global Instance)"]
        M5Begin["M5.begin()"]
        M5Update["M5.update()"]
    end
    
    subgraph Tier3["Hardware Abstraction Tier"]
        LcdObj["M5Display<br/>M5.Lcd"]
        PowerObj["POWER<br/>M5.Power"]
        BtnAObj["Button<br/>M5.BtnA"]
        BtnBObj["Button<br/>M5.BtnB"]
        BtnCObj["Button<br/>M5.BtnC"]
        SpeakerObj["SPEAKER<br/>M5.Speaker"]
        ImuObj["IMU<br/>M5.Imu"]
        Mpu6886Obj["MPU6886<br/>M5.Mpu6886"]
        Sh200qObj["SH200Q<br/>M5.Sh200Q"]
        CommObj["CommUtil<br/>M5.I2C"]
    end
    
    subgraph Tier4["Driver & Peripheral Tier"]
        TFTDriver["TFT_eSPI"]
        WireLib["Wire (I2C)"]
        SPILib["SPI"]
        DACPeripheral["DAC/LEDC PWM"]
        GPIOPeripheral["GPIO"]
    end
    
    UserSketch --> M5Object
    BasicExamples --> M5Object
    UnitExamples --> M5Object
    
    M5Object --> M5Begin
    M5Object --> M5Update
    M5Object --> LcdObj
    M5Object --> PowerObj
    M5Object --> BtnAObj
    M5Object --> BtnBObj
    M5Object --> BtnCObj
    M5Object --> SpeakerObj
    M5Object --> ImuObj
    M5Object --> Mpu6886Obj
    M5Object --> Sh200qObj
    M5Object --> CommObj
    
    LcdObj --> TFTDriver
    PowerObj --> WireLib
    ImuObj --> WireLib
    Mpu6886Obj --> WireLib
    Sh200qObj --> WireLib
    CommObj --> WireLib
    TFTDriver --> SPILib
    SpeakerObj --> DACPeripheral
    BtnAObj --> GPIOPeripheral
    BtnBObj --> GPIOPeripheral
    BtnCObj --> GPIOPeripheral
```

Sources: [src/M5Stack.h:118-170](), [src/M5Stack.cpp:7-15](), [src/M5Stack.cpp:62-70]()

## M5Stack Class Structure

The `M5Stack` class (defined in [src/M5Stack.h:118-170]()) serves as the primary facade and aggregates all hardware subsystems. A global instance `extern M5Stack M5` ([src/M5Stack.cpp:94]()) provides the main entry point. The class contains public member objects for each subsystem, following a composition pattern.

### M5Stack Class Member Objects and Methods

| Member Object | Type | GPIO/Address | Description |
|---------------|------|--------------|-------------|
| `Lcd` | `M5Display` | SPI (CS:14, DC:27, RST:33) | Display interface extending TFT_eSPI |
| `Power` | `POWER` | I2C 0x75 | IP5306 power management |
| `BtnA` | `Button` | GPIO 39 | Left hardware button |
| `BtnB` | `Button` | GPIO 38 | Middle hardware button |
| `BtnC` | `Button` | GPIO 37 | Right hardware button |
| `Speaker` | `SPEAKER` | GPIO 25 (DAC) | Audio output via DAC/PWM |
| `Imu` | `IMU` | I2C 0x68 | Generic IMU interface |
| `Mpu6886` | `MPU6886` | I2C 0x68 | MPU6886 IMU driver |
| `Sh200Q` | `SH200Q` | I2C 0x6C | SH200Q IMU driver |
| `I2C` | `CommUtil` | I2C (SDA:21, SCL:22) | I2C helper utilities |

**Core Methods:**
- `void begin(bool LCDEnable, bool SDEnable, bool SerialEnable, bool I2CEnable)` - Initialize all subsystems ([src/M5Stack.cpp:10-60]())
- `void update()` - Poll buttons and update speaker state, called in `loop()` ([src/M5Stack.cpp:62-70]())

**Deprecated Methods:** `setPowerBoostKeepOn()`, `setWakeupButton()`, `powerOFF()` redirect to `M5.Power.*` equivalents for backward compatibility ([src/M5Stack.cpp:76-92]())

**Global Aliases:** The library provides lowercase macros for convenience: `m5`, `lcd`, `imu`, etc. ([src/M5Stack.h:173-180]())

### M5Stack Class Composition Diagram

```mermaid
graph LR
    subgraph M5StackClass["M5Stack Class Definition"]
        Constructor["M5Stack()"]
        BeginMethod["begin(LCDEnable, SDEnable,<br/>SerialEnable, I2CEnable)"]
        UpdateMethod["update()"]
        IsInitedFlag["private: bool isInited"]
    end
    
    subgraph PublicMembers["Public Member Objects"]
        LcdMember["M5Display Lcd"]
        PowerMember["POWER Power"]
        BtnAMember["Button BtnA<br/>(BUTTON_A_PIN=39)"]
        BtnBMember["Button BtnB<br/>(BUTTON_B_PIN=38)"]
        BtnCMember["Button BtnC<br/>(BUTTON_C_PIN=37)"]
        SpeakerMember["SPEAKER Speaker"]
        ImuMember["IMU Imu"]
        I2CMember["CommUtil I2C"]
        Mpu6886Member["MPU6886 Mpu6886"]
        Sh200QMember["SH200Q Sh200Q"]
    end
    
    subgraph GlobalInstance["Global Singleton"]
        ExternM5["extern M5Stack M5"]
    end
    
    M5StackClass --> PublicMembers
    ExternM5 --> M5StackClass
```

Sources: [src/M5Stack.h:118-170](), [src/M5Stack.h:172-184](), [src/M5Stack.cpp:7-15](), [src/M5Stack.cpp:94]()

## Hardware Abstraction Layers

The M5Stack library implements a clear separation between high-level APIs and low-level hardware drivers. Each major subsystem provides its own abstraction layer that handles hardware-specific details.

### Hardware Abstraction Stack

| Layer | Components | Purpose |
|-------|------------|---------|
| **Application API** | `M5.Lcd`, `M5.Power`, `M5.BtnA/B/C` | User-friendly interface methods |
| **Subsystem Classes** | `M5Display`, `POWER`, `Button`, `SPEAKER` | Hardware abstraction and state management |
| **Driver Layer** | `TFT_eSPI`, `IP5306`, `MPU6886`, `SH200Q` | Hardware-specific communication protocols |
| **Communication** | `I2C`, `SPI`, `GPIO` | Low-level protocol implementation |
| **Hardware** | ESP32, ILI9341 LCD, IP5306 PMIC, IMU sensors | Physical devices |

Sources: [src/M5Stack.h:101-117](), [src/utility/Power.h:18-76]()

## Initialization and Startup Sequence

The `M5.begin()` method ([src/M5Stack.cpp:10-60]()) initializes hardware subsystems in a specific order. It uses a flag `isInited` to prevent double initialization. The method accepts four boolean parameters to selectively enable subsystems.

### begin() Method Signature and Defaults

```cpp
void M5Stack::begin(bool LCDEnable = true, 
                    bool SDEnable = true, 
                    bool SerialEnable = true, 
                    bool I2CEnable = false)
```

**Default Behavior:** LCD, SD card, and Serial are enabled by default. I2C must be explicitly enabled (typically required for IMU and power management features).

### Initialization Sequence Diagram

```mermaid
graph TD
    AppSetup["setup() function"]
    
    subgraph InitProcess["M5.begin() - src/M5Stack.cpp:10-60"]
        CheckInit["Check isInited flag<br/>(line 12-15)"]
        SetFlag["Set isInited = true"]
        SPIPins["Configure SPI pins 18,19,23<br/>Set FUN_DRV_M, pullup<br/>(lines 18-22)"]
        SerialSetup["if (SerialEnable)<br/>Serial.begin(115200)<br/>(lines 25-30)"]
        SDSetup["if (SDEnable)<br/>SD.begin(TFCARD_CS_PIN, SPI, 40MHz)<br/>(lines 33-35)"]
        LCDSetup["if (LCDEnable)<br/>Lcd.begin()<br/>(lines 38-40)"]
        WakeupBtn["Power.setWakeupButton(BUTTON_A_PIN)<br/>(line 46)"]
        I2CSetup["if (I2CEnable)<br/>Wire.begin(21, 22)<br/>(lines 49-51)"]
        GPIO15["pinMode(15, OUTPUT_OPEN_DRAIN)<br/>M5GO WiFi compatibility<br/>(line 59)"]
    end
    
    subgraph LoopProcess["loop() function"]
        UpdateCall["M5.update()"]
        BtnARead["BtnA.read() - line 64"]
        BtnBRead["BtnB.read() - line 65"]
        BtnCRead["BtnC.read() - line 66"]
        SpeakerUpd["Speaker.update() - line 69"]
    end
    
    AppSetup --> CheckInit
    CheckInit -->|"not initialized"| SetFlag
    CheckInit -->|"already initialized"| Return["return (skip init)"]
    SetFlag --> SPIPins
    SPIPins --> SerialSetup
    SerialSetup --> SDSetup
    SDSetup --> LCDSetup
    LCDSetup --> WakeupBtn
    WakeupBtn --> I2CSetup
    I2CSetup --> GPIO15
    
    GPIO15 --> LoopProcess
    UpdateCall --> BtnARead
    BtnARead --> BtnBRead
    BtnBRead --> BtnCRead
    BtnCRead --> SpeakerUpd
    SpeakerUpd --> UpdateCall
```

**Key Initialization Steps:**
1. **SPI GPIO Configuration** ([src/M5Stack.cpp:18-22]()): Pins 18, 19, 23 set to high drive strength with pullups for reliable SPI communication
2. **Serial Port** ([src/M5Stack.cpp:25-30]()): 115200 baud UART0 for debugging
3. **SD Card** ([src/M5Stack.cpp:33-35]()): TFCARD_CS_PIN chip select, 40MHz SPI clock
4. **LCD Display** ([src/M5Stack.cpp:38-40]()): Initializes M5Display and underlying TFT_eSPI driver
5. **Power Wakeup** ([src/M5Stack.cpp:46]()): Sets Button A (GPIO 39) as deep sleep wakeup source
6. **I2C Bus** ([src/M5Stack.cpp:49-51]()): SDA=21, SCL=22 for IMU and IP5306 communication
7. **GPIO 15 Open-Drain** ([src/M5Stack.cpp:59]()): Prevents interference with M5GO accessories

Sources: [src/M5Stack.cpp:10-60](), [src/M5Stack.cpp:62-70]()

## Power Management Integration

The power management system is built around the IP5306 Power Management IC (PMIC), which provides battery charging, power boost control, and low-power sleep modes. The `POWER` class abstracts all IP5306 operations through I2C communication.

### Power System Architecture

```mermaid
graph LR
    subgraph "Power API"
        PowerClass["POWER Class"]
        PowerMethods["setPowerBoostKeepOn()<br/>setCharge()<br/>getBatteryLevel()<br/>isCharging()<br/>deepSleep()<br/>lightSleep()<br/>powerOFF()"]
    end
    
    subgraph "IP5306 PMIC Registers"
        SysCtl0["IP5306_REG_SYS_CTL0<br/>Boost Control"]
        SysCtl1["IP5306_REG_SYS_CTL1<br/>Power Settings"]
        SysCtl2["IP5306_REG_SYS_CTL2<br/>Shutdown Timer"]
        ReadRegs["IP5306_REG_READ0/1/3<br/>Status Registers"]
        ChgRegs["IP5306_REG_CHG_CTL0/1<br/>Charge Control"]
    end
    
    subgraph "I2C Communication"
        I2CAddr["IP5306_ADDR (0x75)"]
        CommUtil["CommUtil M5.I2C<br/>readByte()<br/>writeByte()"]
    end
    
    PowerClass --> PowerMethods
    PowerMethods --> SysCtl0
    PowerMethods --> SysCtl1
    PowerMethods --> SysCtl2
    PowerMethods --> ReadRegs
    PowerMethods --> ChgRegs
    
    SysCtl0 --> I2CAddr
    SysCtl1 --> I2CAddr
    SysCtl2 --> I2CAddr
    ReadRegs --> I2CAddr
    ChgRegs --> I2CAddr
    
    I2CAddr --> CommUtil
```

Sources: [src/utility/Power.h:18-76](), [src/utility/Power.cpp:27-82]()

## Compatibility and Legacy Support

The M5Stack library maintains backward compatibility through deprecated method stubs and global aliases. Legacy power management methods in the main `M5Stack` class redirect to the newer `POWER` class implementation.

### Backward Compatibility Methods

| Deprecated Method | New Implementation | Location |
|-------------------|-------------------|----------|
| `M5.setPowerBoostKeepOn()` | `M5.Power.setPowerBoostKeepOn()` | [src/M5Stack.cpp:76-78]() |
| `M5.setWakeupButton()` | `M5.Power.setWakeupButton()` | [src/M5Stack.cpp:83-85]() |
| `M5.powerOFF()` | `M5.Power.deepSleep()` | [src/M5Stack.cpp:90-92]() |

The library also provides lowercase aliases for convenience: `m5`, `lcd`, `imu`, etc. are all mapped to their respective capitalized versions through preprocessor definitions.

Sources: [src/M5Stack.h:164-184](), [src/M5Stack.cpp:72-93]()