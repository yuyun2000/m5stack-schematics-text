M5GFX Introduction

# Introduction

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [idf_component.yml](idf_component.yml)
- [library.json](library.json)
- [library.properties](library.properties)
- [src/M5GFX.cpp](src/M5GFX.cpp)
- [src/M5GFX.h](src/M5GFX.h)
- [src/lgfx/boards.hpp](src/lgfx/boards.hpp)
- [src/lgfx/v1/gitTagVersion.h](src/lgfx/v1/gitTagVersion.h)

</details>



M5GFX is a graphics library for the M5Stack hardware ecosystem built on the LovyanGFX graphics engine. It provides automatic hardware detection and board-specific initialization for 25+ M5Stack devices while exposing a unified graphics API. The library supports diverse display technologies including LCD, E-Paper, HDMI, and composite video, and compiles for both ESP32 embedded targets and desktop simulation via SDL2.

**Key Capabilities**:
- **Hardware Autodetection**: Identifies M5Stack boards using eFuse reading, I2C probing, and SPI panel ID detection
- **Unified Graphics API**: Single codebase works across different display controllers and communication buses
- **Multi-Platform**: Compiles for ESP32/S2/S3/C3/C6/P4 and SDL desktop simulation
- **LovyanGFX Core**: Inherits optimized graphics primitives, font rendering, and image decoding from LovyanGFX v1.2.19

**Navigation**: For installation and basic usage, see page 1.1 (Getting Started). For architecture details, see page 1.2 (Architecture Overview). For the complete device list, see page 1.3 (Supported Devices and Displays).

---

## What is M5GFX?

M5GFX extends the LovyanGFX graphics engine to provide M5Stack-specific hardware support. The library manages 25+ M5Stack board variants with different display controllers (ILI9342, ST7789, GC9A01, IT8951), communication buses (SPI, I2C, I80 parallel, HDMI), touch interfaces (FT5x06, GT911, CST816S), and power management ICs (AXP192, AXP2101, AW9523).

**Primary Goals**:
1. **Zero-Configuration Initialization**: Call `M5GFX::init()` to automatically detect and configure hardware
2. **Portable Graphics Code**: Write once, run on any supported M5Stack device
3. **Desktop Development**: Test graphics code on PC using SDL2 before deploying to hardware
4. **Performance**: DMA-accelerated transfers, hardware-specific optimizations, PSRAM sprite support

**Core Class**: The `M5GFX` class ([src/M5GFX.h:174]()) inherits from `lgfx::LGFX_Device` and adds board auto-detection ([src/M5GFX.cpp:712-1591]()).

Sources: [src/M5GFX.h:1-296](), [src/M5GFX.cpp:1-1591](), [README.md:1-56]()

---

## Supported Hardware

M5GFX supports a comprehensive range of M5Stack products organized into categories:

### Main Display Units

```mermaid
graph TB
    subgraph "Core Series - ESP32"
        M5Stack["board_M5Stack<br/>320x240 ILI9342<br/>VSPI, GPIO_NUM_14 CS"]
        M5StackCore2["board_M5StackCore2<br/>320x240 ILI9342C<br/>AXP192/AXP2101 Power<br/>FT5x06 Touch"]
        M5Tough["board_M5Tough<br/>320x240 ILI9342C<br/>AXP192 Power<br/>Custom Touch"]
        M5Station["board_M5Station<br/>240x135 ST7789<br/>AXP192 Power"]
    end
    
    subgraph "Core Series - ESP32-S3"
        M5StackCoreS3["board_M5StackCoreS3<br/>320x240 ILI9342<br/>AW9523 I/O Expander<br/>AXP2101 Power<br/>FT5x06 Touch"]
        M5StackCoreS3SE["board_M5StackCoreS3SE"]
    end
    
    subgraph "Stick Series"
        M5StickC["board_M5StickC<br/>80x160 ST7735S<br/>AXP192 Power"]
        M5StickCPlus["board_M5StickCPlus<br/>135x240 ST7789<br/>AXP192 Power"]
        M5StickCPlus2["board_M5StickCPlus2<br/>135x240 ST7789<br/>PWM Backlight GPIO_NUM_27"]
    end
    
    subgraph "E-Paper Series"
        M5Paper["board_M5Paper<br/>540x960 IT8951<br/>E-Ink Controller"]
        M5PaperS3["board_M5PaperS3<br/>ESP32-S3 PSRAM<br/>EPD Panel"]
        M5StackCoreInk["board_M5StackCoreInk<br/>200x200 GDEW0154*<br/>E-Paper"]
    end
    
    subgraph "Specialized Units"
        M5Dial["board_M5Dial<br/>240x240 GC9A01"]
        M5Cardputer["board_M5Cardputer<br/>240x135 ST7789"]
        M5Tab5["board_M5Tab5<br/>Large Display"]
        M5DinMeter["board_M5DinMeter"]
        M5VAMeter["board_M5VAMeter"]
        M5AirQ["board_M5AirQ"]
    end
    
    subgraph "Atom Series - ESP32-S3"
        M5AtomS3["board_M5AtomS3<br/>128x128 GC9107"]
        M5AtomS3R["board_M5AtomS3R<br/>Custom Backlight I2C"]
    end
    
    subgraph "External Displays"
        M5AtomDisplay["board_M5AtomDisplay<br/>HDMI via FPGA<br/>Up to 720p"]
        M5ModuleDisplay["board_M5ModuleDisplay<br/>HDMI via FPGA"]
        M5UnitLCD["board_M5UnitLCD<br/>I2C Display"]
        M5UnitOLED["board_M5UnitOLED<br/>SH110x I2C<br/>Addr 0x3C-0x3E"]
        M5UnitGLASS["board_M5UnitGLASS<br/>I2C Display"]
        M5UnitRCA["board_M5UnitRCA<br/>NTSC/PAL Composite<br/>I2S-DAC GPIO 25/26"]
        M5ModuleRCA["board_M5ModuleRCA<br/>Composite Video"]
    end
```

**Board Enumeration**: All board types are defined in [src/lgfx/boards.hpp:8-72]() as the `board_t` enum. The library distinguishes between display boards (0-127), non-display boards (128-191), and external displays (192+).

Sources: [src/lgfx/boards.hpp:1-78](), [README.md:11-39](), [library.json:4]()

---

## Core Architecture Components

The following diagram maps M5GFX's conceptual architecture to actual code entities:

```mermaid
graph TB
    subgraph "Application Interface"
        UserCode["User Application"]
        M5GFXClass["M5GFX Class<br/>src/M5GFX.h:174<br/>src/M5GFX.cpp:60"]
    end
    
    subgraph "Device Detection System"
        InitImpl["init_impl()<br/>src/M5GFX.cpp:620-710"]
        Autodetect["autodetect()<br/>src/M5GFX.cpp:712-1591"]
        NVSCache["NVS Storage<br/>Key: 'AUTODETECT'<br/>src/M5GFX.cpp:627-634"]
        EfuseRead["get_pkg_ver()<br/>Read EFUSE_RD_CHIP_VER_PKG<br/>src/M5GFX.cpp:733"]
        I2CProbe["I2C Probe<br/>AXP192: 0x34<br/>AW9523: 0x58<br/>src/M5GFX.cpp:890-903"]
        PanelIDRead["_read_panel_id()<br/>SPI Command 0x04<br/>src/M5GFX.cpp:583-598"]
    end
    
    subgraph "Graphics Engine Layer"
        LGFXDevice["lgfx::LGFX_Device<br/>Base class"]
        LGFXBase["lgfx::LGFXBase<br/>Drawing primitives<br/>Text rendering"]
        LGFXSprite["lgfx::LGFX_Sprite<br/>Off-screen buffers"]
    end
    
    subgraph "Panel Abstraction"
        PanelDevice["lgfx::Panel_Device<br/>Panel interface"]
        PanelLCD["Panel_ILI9342<br/>Panel_ST7789<br/>Panel_GC9A01<br/>src/lgfx/v1/panel/"]
        PanelEPD["Panel_EPD<br/>Panel_IT8951<br/>Panel_GDEW*"]
        PanelHDMI["Panel_M5HDMI<br/>FPGA control"]
    end
    
    subgraph "Bus Layer"
        BusSPI["Bus_SPI<br/>DMA transfers<br/>lldesc_t chains"]
        BusI2C["Bus_I2C<br/>i2c_context_t"]
        BusEPD["Bus_EPD<br/>I80 parallel"]
    end
    
    subgraph "Peripheral Interfaces"
        ITouch["lgfx::ITouch<br/>Touch_FT5x06<br/>Touch_GT911<br/>Touch_CST816S"]
        ILight["lgfx::ILight<br/>Light_PWM<br/>Light_M5StackCore2"]
    end
    
    UserCode --> M5GFXClass
    M5GFXClass --> InitImpl
    InitImpl --> NVSCache
    InitImpl --> Autodetect
    Autodetect --> EfuseRead
    Autodetect --> I2CProbe
    Autodetect --> PanelIDRead
    
    M5GFXClass -.inherits.-> LGFXDevice
    LGFXDevice --> LGFXBase
    M5GFXClass --> LGFXSprite
    
    LGFXBase --> PanelDevice
    PanelDevice --> PanelLCD
    PanelDevice --> PanelEPD
    PanelDevice --> PanelHDMI
    
    PanelLCD --> BusSPI
    PanelEPD --> BusEPD
    PanelHDMI --> BusSPI
    
    M5GFXClass --> ITouch
    M5GFXClass --> ILight
    BusSPI --> BusI2C
```

**Component Relationships**:

| Component | File Location | Purpose |
|-----------|---------------|---------|
| `M5GFX` | [src/M5GFX.h:174]() | Main API class with board detection |
| `init_impl()` | [src/M5GFX.cpp:620-710]() | Initialization with NVS cache check |
| `autodetect()` | [src/M5GFX.cpp:712-1591]() | Hardware probing and identification |
| `lgfx::LGFX_Device` | Inherited base | Device configuration container |
| `lgfx::LGFXBase` | Include chain | Drawing primitives implementation |
| `lgfx::Panel_Device` | Panel headers | Display controller interface |
| `Bus_SPI` / `Bus_I2C` | Platform layer | Hardware communication |
| `ITouch` / `ILight` | Interfaces | Touch and backlight control |

Sources: [src/M5GFX.h:174-274](), [src/M5GFX.cpp:60-63,620-710,712-1591]()

---

## Library Dependencies and Version

M5GFX builds upon several open-source libraries:

```mermaid
graph LR
    M5GFX["M5GFX v0.2.17<br/>MIT License<br/>M5Stack + lovyan03"]
    LovyanGFX["LovyanGFX v1.2.17<br/>FreeBSD License<br/>Core graphics engine"]
    TJpgDec["TJpgDec<br/>Original License<br/>JPEG decoder"]
    Pngle["Pngle<br/>MIT License<br/>PNG decoder"]
    QRCode["QRCode<br/>MIT License<br/>QR generation"]
    Fonts["Font Libraries:<br/>Adafruit GFX (BSD-2)<br/>TFT_eSPI (FreeBSD)<br/>IPA Font (IPA License)<br/>efont (BSD-3)"]
    
    M5GFX --> LovyanGFX
    M5GFX --> TJpgDec
    M5GFX --> Pngle
    M5GFX --> QRCode
    M5GFX --> Fonts
```

**Version Information**:
- **M5GFX**: v0.2.19 ([library.json:13](), [library.properties:2]())
- **LovyanGFX Core**: v1.2.19 ([src/lgfx/v1/gitTagVersion.h:1-4]())
- **License**: M5GFX uses MIT license; LovyanGFX core uses FreeBSD license

**Supported Frameworks**:
- ESP-IDF (native ESP32 framework)
- Arduino for ESP32
- Native desktop (via SDL2 for simulation)

Declared in [library.json:14](): `"frameworks": ["arduino", "espidf", "*"]`

Sources: [library.json:1-17](), [library.properties:1-11](), [src/lgfx/v1/gitTagVersion.h:1-5](), [README.md:41-54]()

---

## Hardware Autodetection System

**Autodetection Algorithm**: The `M5GFX::init()` method ([src/M5GFX.cpp:620-710]()) performs multi-stage hardware identification:

1. **NVS Cache Check** ([src/M5GFX.cpp:627-635]()): Reads previously detected `board_t` from non-volatile storage using key `"AUTODETECT"` to optimize subsequent boots.

2. **ESP32 Package Detection** ([src/M5GFX.cpp:733]()): Reads `EFUSE_RD_CHIP_VER_PKG` to determine chip variant:
   - `EFUSE_RD_CHIP_VER_PKG_ESP32PICOD4`: M5StickC/CPlus/CoreInk (lines 736-834)
   - `pkg_ver == 6`: M5StickCPlus2 (lines 835-879)
   - `EFUSE_RD_CHIP_VER_PKG_ESP32D0WDQ6`: M5Stack/Core2/Tough (lines 880-1101)

3. **I2C Power Management Probing** ([src/M5GFX.cpp:890-903]()): Detects power ICs:
   - `0x34` address → Read register `0x03`:
     - `0x03` = AXP192 (Core2 1st gen)
     - `0x4A` = AXP2101 (Core2 v1.1)
   - `0x58` address → AW9523B (CoreS3)

4. **SPI Panel ID Reading** ([src/M5GFX.cpp:583-598]()): Sends command `0x04` (RDDID) to identify display controller:
   - `0xE3`: ILI9342C (M5Stack Basic/Core2)
   - `0x81/0x85`: ST7789 (M5StickCPlus)
   - `0x7C`: ST7735S (M5StickC)
   - `0x019A00`: GC9A01 (M5Dial)

5. **Board-Specific Configuration**: Instantiates panel, bus, touch, and backlight drivers. Example: M5StackCore2 setup at [src/M5GFX.cpp:1025-1091]() creates `Panel_M5StackCore2`, `Touch_FT5x06`, and `Light_M5StackCore2`.

6. **NVS Persistence** ([src/M5GFX.cpp:699-705]()): Saves detected `board_t` value to NVS for faster future boots.

**Detection Flow Diagram**:

```mermaid
flowchart TD
    Start["M5GFX::init()"] --> CheckNVS["nvs_get_u32('AUTODETECT')<br/>src/M5GFX.cpp:632"]
    CheckNVS -->|"nvs_board != 0"| UseCached["Use cached board_t"]
    CheckNVS -->|"nvs_board == 0"| ReadEfuse["get_pkg_ver()<br/>EFUSE_RD_CHIP_VER_PKG<br/>line 733"]
    
    ReadEfuse --> ChipCheck{Chip Package?}
    ChipCheck -->|"PICOD4"| StickProbe["GPIO_NUM_18 RST<br/>SPI ID @ GPIO_NUM_5<br/>lines 740-782"]
    ChipCheck -->|"pkg_ver==6"| Plus2Probe["GPIO_NUM_12 RST<br/>SPI ID @ GPIO_NUM_5<br/>lines 839-872"]
    ChipCheck -->|"D0WDQ6"| I2CProbe["I2C probe 0x34<br/>readRegister8(0x03)<br/>line 892"]
    
    StickProbe --> StickID{Panel ID}
    StickID -->|"0x81/0x85"| StickCPlus["board_M5StickCPlus<br/>Panel_ST7789"]
    StickID -->|"0x7C"| StickC["board_M5StickC<br/>Panel_ST7735S"]
    
    I2CProbe --> AXPCheck{AXP Type}
    AXPCheck -->|"0x03"| AXP192["AXP192 detected"]
    AXPCheck -->|"0x4A"| AXP2101["AXP2101 detected"]
    AXPCheck -->|"No response"| StackProbe["GPIO_NUM_33 RST<br/>SPI ID @ GPIO_NUM_14<br/>line 1118"]
    
    AXP192 --> Core2ID["SPI ID @ GPIO_NUM_5<br/>line 1020"]
    AXP2101 --> Core2ID
    Core2ID -->|"0xE3"| Core2Touch["Check Touch 0x2E<br/>line 1036"]
    Core2Touch -->|"No touch"| Core2["board_M5StackCore2<br/>Panel_ILI9342C<br/>Touch_FT5x06"]
    Core2Touch -->|"Touch present"| Tough["board_M5Tough<br/>Panel_ILI9342C<br/>Touch_M5Tough"]
    
    StackProbe -->|"0xE3"| Stack["board_M5Stack<br/>Panel_M5Stack"]
    
    UseCached --> Ready["Ready"]
    StickCPlus --> SaveNVS["nvs_set_u32('AUTODETECT')<br/>line 702"]
    StickC --> SaveNVS
    Core2 --> SaveNVS
    Tough --> SaveNVS
    Stack --> SaveNVS
    SaveNVS --> Ready
```

Sources: [src/M5GFX.cpp:620-710,712-1591,583-598]()

---

## Platform and Build Target Support

M5GFX compiles for multiple platforms with conditional compilation:

```mermaid
graph TB
    subgraph "Build Targets"
        ArduinoIDE["Arduino IDE"]
        PlatformIO["PlatformIO"]
        ESPIDF["ESP-IDF Native"]
    end
    
    subgraph "Embedded Platforms"
        ESP32["ESP32<br/>CONFIG_IDF_TARGET_ESP32<br/>VSPI/HSPI"]
        ESP32S3["ESP32-S3<br/>CONFIG_IDF_TARGET_ESP32S3<br/>SPI2/SPI3"]
        ESP32P4["ESP32-P4<br/>CONFIG_IDF_TARGET_ESP32P4<br/>MIPI DSI Support<br/>src/M5GFX.cpp:28-34"]
        ESP32C3["ESP32-C3/C6<br/>RISC-V Core"]
    end
    
    subgraph "Desktop Simulation"
        SDL["SDL Platform<br/>defined(SDL_h_)<br/>src/M5GFX.cpp:49-51"]
        PanelSDL["Panel_sdl<br/>Window simulation<br/>Keyboard→GPIO<br/>Mouse→Touch"]
    end
    
    subgraph "Conditional Features"
        PSRAM["PSRAM Support<br/>CONFIG_SPIRAM_MODE_OCT<br/>For EPD buffering<br/>src/M5GFX.cpp:40-44"]
        DSI["DSI Bus<br/>Bus_DSI<br/>Panel_ILI9881C<br/>Panel_ST7123<br/>src/M5GFX.cpp:30-33"]
    end
    
    ArduinoIDE --> ESP32
    ArduinoIDE --> ESP32S3
    PlatformIO --> ESP32
    PlatformIO --> ESP32S3
    PlatformIO --> ESP32P4
    PlatformIO --> SDL
    ESPIDF --> ESP32
    ESPIDF --> ESP32S3
    ESPIDF --> ESP32P4
    
    ESP32S3 --> PSRAM
    ESP32P4 --> DSI
    SDL --> PanelSDL
```

**Platform Detection** ([src/M5GFX.cpp:6-52]()): 

| Define | Purpose | Lines |
|--------|---------|-------|
| `ESP_PLATFORM` | ESP32 family targets | 6 |
| `CONFIG_IDF_TARGET_ESP32P4` | ESP32-P4 with DSI support | 28 |
| `CONFIG_IDF_TARGET_ESP32S3` | ESP32-S3 variant | 37 |
| `CONFIG_SPIRAM_MODE_OCT` | Octal PSRAM for M5PaperS3 | 40 |
| `SDL_h_` | SDL2 desktop simulation | 49 |

**Platform-Specific Includes**:
- ESP32-P4 DSI: [src/M5GFX.cpp:30-33]() includes `Bus_DSI.hpp`, `Panel_ILI9881C.hpp`, `Panel_ST7123.hpp`
- ESP32-S3 EPD: [src/M5GFX.cpp:42]() includes `Panel_EPD.hpp` for M5PaperS3 with octal PSRAM
- SDL Simulation: [src/M5GFX.cpp:49-50]() includes `Panel_sdl.hpp` and `picture_frame.h`

Sources: [src/M5GFX.cpp:6-52](), [library.json:14-15]()

---

## Key Features Summary

| Feature | Implementation | Code Reference |
|---------|----------------|----------------|
| **Auto-Detection** | NVS caching + eFuse + I2C + SPI probing | [src/M5GFX.cpp:620-1591]() |
| **40+ Board Support** | Enum in `board_t` | [src/lgfx/boards.hpp:8-72]() |
| **Unified API** | `M5GFX` inherits `LGFX_Device` | [src/M5GFX.h:174]() |
| **Multiple Displays** | Panel_LCD, Panel_EPD, Panel_HDMI, Panel_DSI, Panel_CVBS | Various panel headers |
| **Touch Support** | `ITouch` interface with FT5x06, GT911, CST816S | [src/M5GFX.cpp:24-26]() |
| **Backlight Control** | `ILight` interface with PWM and I2C | [src/M5GFX.cpp:600-618]() |
| **Power Management** | AXP192/AXP2101 integration | [src/M5GFX.cpp:79-80,349]() |
| **Desktop Simulation** | SDL2 platform support | [src/M5GFX.cpp:49-51]() |
| **Sprite/Canvas** | `M5Canvas` class | [src/M5GFX.h:277-284]() |
| **Image Formats** | JPEG, PNG, BMP decoding | LovyanGFX dependencies |
| **Font Support** | Multiple font libraries | README.md fonts section |

**API Entry Point**: Users instantiate `M5GFX` and call `init()` ([src/M5GFX.h:174,267-273]()). All graphics operations inherit from `lgfx::LGFXBase`.

Sources: [src/M5GFX.h:1-296](), [src/M5GFX.cpp:1-1591](), [README.md:1-56]()

---

## Next Steps

- **[Getting Started](#1.1)**: Installation, basic examples, and first program
- **[Architecture Overview](#1.2)**: Detailed layer-by-layer architecture explanation
- **[M5GFX Core System](#2)**: Complete API documentation for graphics operations
- **[Display Device Classes](#3)**: Device-specific wrapper classes (M5AtomDisplay, M5UnitRCA, etc.)
- **[Panel Drivers](#4)**: Low-level panel implementations for different display technologies