M5GFX Architecture Overview

# Architecture Overview

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5GFX.cpp](src/M5GFX.cpp)
- [src/M5GFX.h](src/M5GFX.h)
- [src/lgfx/boards.hpp](src/lgfx/boards.hpp)
- [src/lgfx/v1/LGFXBase.cpp](src/lgfx/v1/LGFXBase.cpp)
- [src/lgfx/v1/LGFXBase.hpp](src/lgfx/v1/LGFXBase.hpp)
- [src/lgfx/v1/misc/colortype.hpp](src/lgfx/v1/misc/colortype.hpp)

</details>



## Purpose and Scope

This document describes the high-level architecture of the M5GFX library, explaining how the system is organized into distinct layers and how these layers interact. M5GFX is a graphics library specifically designed for M5Stack hardware that wraps the LovyanGFX graphics engine with device-specific initialization and configuration logic.

For information about specific M5Stack devices and their hardware configurations, see [Supported Devices and Displays](#1.3). For details on the M5GFX device wrapper classes, see [M5GFX Device Classes](#2). For LovyanGFX core functionality, see [LovyanGFX Graphics Core](#3).

---

## System Layering

M5GFX employs a five-layer architecture that separates hardware abstraction, graphics operations, and platform-specific implementations:

```mermaid
graph TB
    subgraph Layer1["Application Layer"]
        UserApp["User Application<br/>setup() / loop()"]
    end
    
    subgraph Layer2["M5GFX Device Wrapper Layer"]
        M5GFX_Class["M5GFX class<br/>src/M5GFX.cpp<br/>src/M5GFX.h"]
        AutoDetect["autodetect()<br/>Board identification"]
        DeviceInit["init_impl()<br/>Device configuration"]
    end
    
    subgraph Layer3["LovyanGFX Core Graphics Layer"]
        LGFX_Device["LGFX_Device<br/>Panel management"]
        LGFXBase["LGFXBase<br/>src/lgfx/v1/LGFXBase.hpp<br/>Drawing primitives"]
        LGFX_Sprite["LGFX_Sprite<br/>Off-screen buffers"]
        PixelCopy["pixelcopy_t<br/>Format conversion"]
    end
    
    subgraph Layer4["Panel Driver Layer"]
        Panel_Device["Panel_Device<br/>Base interface"]
        Panel_ILI9342["Panel_ILI9342<br/>320x240 TFT"]
        Panel_ST7789["Panel_ST7789<br/>240x320 TFT"]
        Panel_EPD["Panel_EPD<br/>E-paper displays"]
        Panel_M5HDMI["Panel_M5HDMI<br/>HDMI output"]
    end
    
    subgraph Layer5["Platform Abstraction Layer"]
        Bus_SPI["Bus_SPI<br/>SPI communication"]
        Bus_I2C["Bus_I2C<br/>I2C communication"]
        ESP32_Platform["ESP32 Platform<br/>GPIO, DMA, PSRAM"]
        SDL_Platform["SDL Platform<br/>Desktop simulation"]
    end
    
    subgraph Layer6["Hardware Layer"]
        ESP32_HW["ESP32/S3/C3/P4<br/>Physical hardware"]
        Desktop_OS["Windows/Linux/macOS<br/>SDL2 library"]
    end
    
    UserApp --> M5GFX_Class
    M5GFX_Class --> AutoDetect
    M5GFX_Class --> DeviceInit
    M5GFX_Class -.inherits.-> LGFX_Device
    
    LGFX_Device --> LGFXBase
    LGFX_Device --> LGFX_Sprite
    LGFXBase --> PixelCopy
    
    LGFX_Device --> Panel_Device
    Panel_Device --> Panel_ILI9342
    Panel_Device --> Panel_ST7789
    Panel_Device --> Panel_EPD
    Panel_Device --> Panel_M5HDMI
    
    Panel_ILI9342 --> Bus_SPI
    Panel_ST7789 --> Bus_SPI
    Panel_EPD --> ESP32_Platform
    Panel_M5HDMI --> Bus_SPI
    
    Bus_SPI --> ESP32_Platform
    Bus_I2C --> ESP32_Platform
    ESP32_Platform --> ESP32_HW
    
    Panel_Device -.SDL mode.-> SDL_Platform
    SDL_Platform --> Desktop_OS
```

**Sources:** [src/M5GFX.cpp:1-2800](), [src/M5GFX.h:1-300](), [src/lgfx/v1/LGFXBase.hpp:1-1500]()

---

## M5GFX Device Wrapper Layer

The `M5GFX` class serves as the primary entry point and hardware abstraction layer. It inherits from `LGFX_Device` and adds M5Stack-specific device detection and initialization.

### Class Hierarchy

```mermaid
graph TB
    LGFXBase["LGFXBase<br/>Core graphics API<br/>Drawing primitives"]
    LGFX_Device["LGFX_Device<br/>Panel management<br/>Transaction control"]
    M5GFX_Class["M5GFX<br/>Device auto-detection<br/>M5Stack initialization"]
    
    Print["Print<br/>Arduino Print class<br/>Text output"]
    
    Print -.-> LGFXBase
    LGFXBase -.inherits.-> LGFX_Device
    LGFX_Device -.inherits.-> M5GFX_Class
    
    Panel_Device["Panel_Device*<br/>_panel"]
    ITouch["ITouch*<br/>_touch_last"]
    IBus["IBus*<br/>_bus_last"]
    ILight["ILight*<br/>_light_last"]
    
    M5GFX_Class --> Panel_Device
    M5GFX_Class --> ITouch
    M5GFX_Class --> IBus
    M5GFX_Class --> ILight
```

**Sources:** [src/M5GFX.h:174-274](), [src/M5GFX.cpp:60-63](), [src/lgfx/v1/LGFXBase.hpp:56-63]()

### Board Auto-Detection

The `M5GFX::autodetect()` method implements a multi-stage detection algorithm that identifies the connected M5Stack hardware:

```mermaid
graph TD
    Start["init_impl()"] --> CheckNVS["Load board_t from NVS"]
    CheckNVS --> CheckDefine["Check #define M5GFX_BOARD<br/>or ARDUINO_* macros"]
    CheckDefine --> AutoDetect["autodetect(use_reset, board)"]
    
    AutoDetect --> CheckPKG["Read chip package version<br/>get_pkg_ver()"]
    
    CheckPKG --> PICOD4{"EFUSE_RD_CHIP_VER_PKG_ESP32PICOD4?"}
    CheckPKG --> PICOV3{"Package version 6?"}
    CheckPKG --> D0WDQ6{"EFUSE_RD_CHIP_VER_PKG_ESP32D0WDQ6?"}
    
    PICOD4 -->|Yes| DetectStick["Detect M5StickC/Plus<br/>Panel_ST7735/ST7789<br/>GPIO checks"]
    PICOD4 -->|Yes| DetectInk["Detect M5StackCoreInk<br/>Panel_EPD<br/>GDEW0154M09"]
    
    PICOV3 -->|Yes| DetectPlus2["Detect M5StickCPlus2<br/>Panel_ST7789<br/>GPIO_NUM_5"]
    
    D0WDQ6 -->|Yes| CheckAXP["Check AXP192/AXP2101<br/>I2C addr 0x34"]
    CheckAXP --> DetectCore2["Detect Core2/Tough<br/>Panel_ILI9342<br/>Touch controllers"]
    CheckAXP --> DetectStack["Detect M5Stack Basic<br/>Panel_ILI9342<br/>GPIO_NUM_14"]
    
    DetectStick --> SetPanel["Set _panel_last<br/>Set _bus_last<br/>Set _light_last"]
    DetectInk --> SetPanel
    DetectPlus2 --> SetPanel
    DetectCore2 --> SetPanel
    DetectStack --> SetPanel
    
    SetPanel --> SaveNVS["Save board_t to NVS"]
    SaveNVS --> InitPanel["LGFX_Device::init_impl()"]
    InitPanel --> Return["return true"]
```

**Sources:** [src/M5GFX.cpp:620-709](), [src/M5GFX.cpp:712-1695]()

### Key Detection Components

| Component | Purpose | Code Reference |
|-----------|---------|----------------|
| `get_pkg_ver()` | Reads ESP32 chip package version from eFuse | [src/M5GFX.cpp:733]() |
| `_read_panel_id()` | Reads LCD panel ID via SPI command 0x04 | [src/M5GFX.cpp:583-598]() |
| `i2c::readRegister8()` | Checks for I2C devices (AXP power ICs, GPIO expanders) | [src/M5GFX.cpp:893]() |
| `board_t` enumeration | Identifies specific M5Stack hardware models | [src/lgfx/boards.hpp:8-72]() |

**Sources:** [src/M5GFX.cpp:583-709](), [src/lgfx/boards.hpp:1-78]()

---

## LovyanGFX Core Graphics Layer

LovyanGFX provides the underlying graphics engine with hardware-agnostic drawing operations. M5GFX builds on this foundation without modifying core graphics behavior.

### Core Classes

```mermaid
graph LR
    subgraph "Graphics API"
        LGFXBase_Draw["LGFXBase<br/>drawPixel()<br/>drawLine()<br/>fillRect()<br/>drawCircle()"]
    end
    
    subgraph "Color Management"
        ColorConv["color_conv_t<br/>RGB888→RGB565→RGB332<br/>Palette mapping"]
        ColorTypes["color_depth_t<br/>rgb332_t, rgb565_t<br/>rgb888_t, argb8888_t"]
    end
    
    subgraph "Format Conversion"
        PixelCopy_Struct["pixelcopy_t<br/>Format conversion<br/>Affine transforms<br/>Transparency"]
    end
    
    subgraph "Text Rendering"
        FontEngine["IFont interface<br/>UTF-8 decode<br/>Glyph rendering"]
        FontTypes["BaseFont, BMPfont<br/>RLEfont, VLWfont<br/>U8g2font"]
    end
    
    subgraph "Sprite System"
        LGFX_Sprite_Class["LGFX_Sprite<br/>Off-screen buffer<br/>createSprite()<br/>pushSprite()"]
        Panel_Sprite["Panel_Sprite<br/>Internal panel impl"]
    end
    
    LGFXBase_Draw --> ColorConv
    LGFXBase_Draw --> PixelCopy_Struct
    LGFXBase_Draw --> FontEngine
    
    ColorConv --> ColorTypes
    FontEngine --> FontTypes
    
    LGFX_Sprite_Class -.uses.-> Panel_Sprite
    LGFX_Sprite_Class -.inherits.-> LGFXBase_Draw
```

**Sources:** [src/lgfx/v1/LGFXBase.hpp:56-1500](), [src/lgfx/v1/LGFXBase.cpp:1-8000]()

### Graphics Pipeline Flow

```mermaid
flowchart TD
    Start["User calls drawing function<br/>fillRect(x, y, w, h)"]
    
    Start --> Clip["Clipping<br/>_clipping(x, y, w, h)<br/>Check against _clip_l/r/t/b"]
    
    Clip -->|Inside| StartWrite["startWrite()<br/>Acquire bus transaction"]
    Clip -->|Outside| End["Return"]
    
    StartWrite --> ColorConv["Color Conversion<br/>_write_conv.convert(color)<br/>RGB888 → panel depth"]
    
    ColorConv --> Panel["Panel Interface<br/>_panel->writeFillRectPreclipped()"]
    
    Panel --> SetWindow["setWindow(xs, ys, xe, ye)<br/>Send CASET/RASET commands"]
    
    SetWindow --> Transfer["Data Transfer<br/>writePixels() or writeBlock()<br/>DMA or direct write"]
    
    Transfer --> EndWrite["endWrite()<br/>Release bus transaction"]
    
    EndWrite --> End
```

**Sources:** [src/lgfx/v1/LGFXBase.cpp:198-213](), [src/lgfx/v1/LGFXBase.hpp:145-156]()

---

## Panel Driver Layer

Panel drivers implement the `IPanel` interface and provide hardware-specific initialization and communication protocols.

### Panel Driver Hierarchy

```mermaid
graph TB
    IPanel["IPanel<br/>Interface"]
    Panel_Device["Panel_Device<br/>Base implementation<br/>src/lgfx/v1/panel/Panel_Device.hpp"]
    
    IPanel -.interface.-> Panel_Device
    
    subgraph "TFT LCD Drivers"
        Panel_LCD["Panel_LCD<br/>SPI TFT base class<br/>CASET/RASET protocol"]
        Panel_ILI9342_Class["Panel_ILI9342<br/>320x240 displays<br/>M5Stack/Core2"]
        Panel_ST7789_Class["Panel_ST7789<br/>240x320 displays<br/>M5StickCPlus"]
        Panel_GC9A01["Panel_GC9A01<br/>240x240 round<br/>M5Dial"]
    end
    
    subgraph "E-Paper Drivers"
        Panel_EPD_Class["Panel_EPD<br/>E-ink displays<br/>LUT waveforms"]
        Panel_GDEW0154M09["Panel_GDEW0154M09<br/>200x200 1.54in<br/>M5CoreInk"]
        Panel_IT8951["Panel_IT8951<br/>960x540 10.3in<br/>M5Paper"]
    end
    
    subgraph "Special Output"
        Panel_M5HDMI_Class["Panel_M5HDMI<br/>FPGA + HDMI TX<br/>1280x720 capable"]
        Panel_CVBS["Panel_CVBS<br/>I2S DAC<br/>NTSC/PAL composite"]
        Panel_M5UnitLCD["Panel_M5UnitLCD<br/>I2C with RLE<br/>135x240"]
    end
    
    Panel_Device --> Panel_LCD
    Panel_LCD --> Panel_ILI9342_Class
    Panel_LCD --> Panel_ST7789_Class
    Panel_LCD --> Panel_GC9A01
    
    Panel_Device --> Panel_EPD_Class
    Panel_EPD_Class --> Panel_GDEW0154M09
    Panel_EPD_Class --> Panel_IT8951
    
    Panel_Device --> Panel_M5HDMI_Class
    Panel_Device --> Panel_CVBS
    Panel_Device --> Panel_M5UnitLCD
```

**Sources:** [src/M5GFX.cpp:16-32](), [src/M5GFX.cpp:85-530]()

### Panel Configuration Pattern

Each panel driver uses a configuration structure to define hardware parameters:

| Configuration Parameter | Purpose | Example Values |
|------------------------|---------|----------------|
| `pin_cs` | Chip select GPIO | `GPIO_NUM_14`, `GPIO_NUM_5` |
| `pin_rst` | Hardware reset GPIO | `GPIO_NUM_33`, `GPIO_NUM_18` |
| `panel_width` | Physical width in pixels | `320`, `240`, `135` |
| `panel_height` | Physical height in pixels | `240`, `320`, `240` |
| `offset_x` / `offset_y` | Display RAM offset | `0`, `26`, `52` |
| `offset_rotation` | Default rotation offset | `0-3` |
| `invert` | Color inversion flag | `true`, `false` |
| `rgb_order` | RGB vs BGR pixel order | `true`, `false` |
| `freq_write` | SPI write frequency (Hz) | `40000000`, `27000000` |

**Sources:** [src/M5GFX.cpp:85-343](), [src/M5GFX.cpp:355-502]()

---

## Platform Abstraction Layer

The platform abstraction layer provides unified interfaces for bus communication and hardware control across different ESP32 variants and SDL simulation.

### Bus Abstraction

```mermaid
graph TB
    subgraph "Bus Interfaces"
        IBus["IBus<br/>Base interface"]
        Bus_SPI_Class["Bus_SPI<br/>SPI communication<br/>DMA support"]
        Bus_I2C_Class["Bus_I2C<br/>I2C communication<br/>Multi-master"]
        Bus_EPD["Bus_EPD<br/>Parallel I80 8/16-bit"]
    end
    
    subgraph "ESP32 Implementation"
        ESP32_SPI["ESP32 SPI<br/>Direct register access<br/>GDMA descriptors"]
        ESP32_I2C["ESP32 I2C<br/>State machine<br/>Bus recovery"]
        ESP32_GPIO["ESP32 GPIO<br/>pinMode()<br/>gpio_hi()/gpio_lo()"]
    end
    
    subgraph "SDL Implementation"
        SDL_Bus["SDL Bus Emulation<br/>Simulated timing<br/>No actual transfer"]
        SDL_GPIO["SDL GPIO Emulation<br/>Keyboard mapping<br/>Mouse mapping"]
    end
    
    IBus -.interface.-> Bus_SPI_Class
    IBus -.interface.-> Bus_I2C_Class
    IBus -.interface.-> Bus_EPD
    
    Bus_SPI_Class -->|ESP_PLATFORM| ESP32_SPI
    Bus_I2C_Class -->|ESP_PLATFORM| ESP32_I2C
    
    Bus_SPI_Class -->|SDL_h_| SDL_Bus
    Bus_I2C_Class -->|SDL_h_| SDL_Bus
    
    ESP32_SPI --> ESP32_GPIO
    ESP32_I2C --> ESP32_GPIO
    
    SDL_Bus --> SDL_GPIO
```

**Sources:** [src/M5GFX.cpp:6-52]()

### Platform Detection Pattern

Conditional compilation directives select platform-specific implementations:

```cpp
#if defined ( ESP_PLATFORM )
  // ESP32 hardware implementation
  #include <driver/i2c.h>
  #include <driver/spi_master.h>
  
  #if defined ( CONFIG_IDF_TARGET_ESP32P4 )
    // ESP32-P4 specific (DSI interface)
  #elif defined ( CONFIG_IDF_TARGET_ESP32S3 )
    // ESP32-S3 specific
  #elif defined ( CONFIG_IDF_TARGET_ESP32C6 )
    // ESP32-C6 specific
  #endif
  
#else
  // SDL simulation for desktop
  #include "lgfx/v1/platforms/sdl/Panel_sdl.hpp"
#endif
```

**Sources:** [src/M5GFX.cpp:6-52]()

---

## Component Communication

### Initialization Sequence

```mermaid
sequenceDiagram
    participant App as "Application"
    participant M5GFX as "M5GFX::init()"
    participant AutoDetect as "autodetect()"
    participant Panel as "Panel_Device"
    participant Bus as "Bus_SPI"
    participant HW as "Hardware"
    
    App->>M5GFX: init()
    M5GFX->>M5GFX: init_impl()
    M5GFX->>AutoDetect: autodetect()
    
    AutoDetect->>HW: Read eFuse (chip package)
    HW-->>AutoDetect: Package version
    
    AutoDetect->>Bus: Create Bus_SPI instance
    AutoDetect->>Bus: config() / init()
    Bus->>HW: Configure SPI peripheral
    
    AutoDetect->>Bus: _read_panel_id()
    Bus->>HW: Send 0x04 command
    HW-->>Bus: Panel ID bytes
    Bus-->>AutoDetect: Panel ID
    
    AutoDetect->>Panel: Create Panel_ILI9342 instance
    AutoDetect->>M5GFX: Set _panel_last
    AutoDetect->>M5GFX: Set _bus_last
    AutoDetect-->>M5GFX: board_t
    
    M5GFX->>Panel: init(use_reset=false)
    Panel->>Bus: Reset sequence
    Panel->>Bus: Init commands
    
    M5GFX-->>App: true (success)
```

**Sources:** [src/M5GFX.cpp:620-709](), [src/M5GFX.cpp:712-1695]()

### Drawing Operation Flow

```mermaid
sequenceDiagram
    participant App as "Application"
    participant LGFX as "LGFXBase"
    participant Panel as "Panel_ILI9342"
    participant Bus as "Bus_SPI"
    participant DMA as "DMA Engine"
    participant HW as "Display"
    
    App->>LGFX: fillRect(x, y, w, h)
    LGFX->>LGFX: _clipping(x, y, w, h)
    LGFX->>Panel: startWrite()
    Panel->>Bus: beginTransaction()
    
    LGFX->>Panel: writeFillRectPreclipped()
    Panel->>Panel: setWindow(x, y, x+w-1, y+h-1)
    Panel->>Bus: writeCommand(CASET)
    Bus->>HW: 0x2A + coordinates
    Panel->>Bus: writeCommand(RASET)
    Bus->>HW: 0x2B + coordinates
    Panel->>Bus: writeCommand(RAMWR)
    Bus->>HW: 0x2C
    
    Panel->>Bus: writeBlock(color, w*h)
    Bus->>DMA: Setup DMA descriptor chain
    DMA->>HW: Transfer pixel data
    
    Panel->>Bus: endTransaction()
    LGFX->>Panel: endWrite()
```

**Sources:** [src/lgfx/v1/LGFXBase.cpp:198-213]()

---

## Memory Management

### Resource Ownership

The `M5GFX` class uses `std::shared_ptr` to manage dynamically allocated resources:

| Resource | Type | Purpose |
|----------|------|---------|
| `_panel_last` | `std::shared_ptr<Panel_Device>` | Current panel driver instance |
| `_touch_last` | `std::shared_ptr<ITouch>` | Touch controller instance |
| `_bus_last` | `std::shared_ptr<IBus>` | Bus communication instance |
| `_light_last` | `std::shared_ptr<ILight>` | Backlight control instance |

**Sources:** [src/M5GFX.h:187-192]()

### Buffer Allocation Strategy

| Buffer Type | Allocation | Purpose |
|-------------|------------|---------|
| Panel framebuffer | DMA-capable RAM | Direct hardware access via DMA |
| Sprite buffer | PSRAM or heap | Off-screen rendering (`LGFX_Sprite`) |
| Font glyph cache | Heap | Temporary storage for rendered glyphs |
| DMA descriptor chain | DMA-capable RAM | SPI burst transfer control |

**Sources:** [src/M5GFX.cpp:714-1695]()

---

## Conditional Compilation

The codebase uses extensive conditional compilation to support different platforms and chip variants:

### Platform Selection

```
#if defined ( ESP_PLATFORM )
  → ESP32 hardware implementation
  #if defined ( CONFIG_IDF_TARGET_ESP32P4 )
    → ESP32-P4 specific features (DSI, MIPI)
  #elif defined ( CONFIG_IDF_TARGET_ESP32S3 )
    → ESP32-S3 specific features (Octal PSRAM, EPD)
  #elif defined ( CONFIG_IDF_TARGET_ESP32C6 )
    → ESP32-C6 specific features
  #endif
#else
  → SDL desktop simulation
#endif
```

**Sources:** [src/M5GFX.cpp:6-52]()

### Board-Specific Code

The `autodetect()` function contains board-specific detection and initialization code organized by chip package:

- **PICO-D4 (lines 736-834)**: M5StickC, M5StickCPlus, M5StackCoreInk
- **PICO-V3_02 (lines 835-878)**: M5StickCPlus2, M5AtomPsram
- **D0WDQ6 (lines 881-1695)**: M5Stack Basic, M5StackCore2, M5Tough
- **ESP32-S3 (lines 345-502)**: M5StackCoreS3, M5AtomS3, M5Dial

**Sources:** [src/M5GFX.cpp:712-1695]()

---

## Summary

The M5GFX architecture demonstrates clean separation of concerns through five distinct layers:

1. **M5GFX Device Wrapper**: Hardware detection, board-specific initialization
2. **LovyanGFX Core**: Unified graphics API, color management, text rendering
3. **Panel Drivers**: Display-specific protocols and initialization
4. **Platform Abstraction**: Bus communication, GPIO control, DMA operations
5. **Hardware/OS**: Physical ESP32 peripherals or SDL simulation

This layered approach enables:
- Support for 30+ M5Stack hardware variants through runtime detection
- Cross-platform development via SDL simulation
- Consistent graphics API regardless of underlying display technology
- Efficient hardware access through direct register manipulation and DMA

**Sources:** [src/M5GFX.cpp:1-2800](), [src/M5GFX.h:1-300](), [src/lgfx/v1/LGFXBase.hpp:1-1500](), [src/lgfx/boards.hpp:1-78]()