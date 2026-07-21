M5GFX Composite Video Panel Driver

# Composite Video Panel Driver

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5AtomDisplay.h](src/M5AtomDisplay.h)
- [src/M5ModuleDisplay.h](src/M5ModuleDisplay.h)
- [src/M5ModuleRCA.h](src/M5ModuleRCA.h)
- [src/M5UnitRCA.h](src/M5UnitRCA.h)

</details>



## Purpose and Scope

This document describes the `Panel_CVBS` driver implementation for generating composite video signals (NTSC/PAL) via DAC output on ESP32 hardware. The panel driver enables M5Stack devices to output analog video signals through RCA connectors, supporting standard television video formats.

The `Panel_CVBS` driver is used by two M5Stack device classes: `M5ModuleRCA` and `M5UnitRCA`. For HDMI digital video output, see [HDMI Panel Driver](#4.3). For general panel architecture concepts, see [Panel Driver Architecture](#4).

**Sources:** [src/M5ModuleRCA.h:1-297](), [src/M5UnitRCA.h:1-297]()

---

## Panel_CVBS Architecture

The `Panel_CVBS` driver is a platform-specific panel implementation that generates composite video baseband signals (CVBS - Composite Video Baseband Signal) using the ESP32's built-in DAC peripheral. Unlike LCD panel drivers that communicate via SPI/I2C, this driver directly outputs analog voltage levels representing luminance and chrominance information encoded according to NTSC or PAL standards.

```mermaid
graph TB
    subgraph "M5Stack Device Classes"
        M5ModuleRCA["M5ModuleRCA<br/>board_t::board_M5ModuleRCA"]
        M5UnitRCA["M5UnitRCA<br/>board_t::board_M5UnitRCA"]
    end
    
    subgraph "Panel Driver Layer"
        Panel_CVBS["Panel_CVBS<br/>lgfx/v1/platforms/esp32/Panel_CVBS.hpp"]
        config_t["config_t<br/>panel_width, panel_height<br/>memory_width, memory_height<br/>offset_x, offset_y"]
        config_detail_t["config_detail_t<br/>signal_type<br/>use_psram<br/>pin_dac<br/>output_level"]
    end
    
    subgraph "Platform Implementation"
        ESP32_DAC["ESP32 DAC Peripheral<br/>8-bit Digital-to-Analog<br/>GPIO25/26 (ESP32)"]
        PSRAM["PSRAM Buffer<br/>Frame Storage<br/>Scanline Buffering"]
        DMA["I2S/DMA System<br/>Continuous Signal Output"]
    end
    
    subgraph "Video Signal Standards"
        NTSC["NTSC<br/>525 lines, 60Hz<br/>black=7.5 IRE"]
        NTSC_J["NTSC_J<br/>525 lines, 60Hz<br/>black=0 IRE (Japan)"]
        PAL["PAL<br/>625 lines, 50Hz"]
        PAL_M["PAL_M<br/>525 lines, 60Hz"]
        PAL_N["PAL_N<br/>625 lines, 50Hz"]
    end
    
    M5ModuleRCA --> Panel_CVBS
    M5UnitRCA --> Panel_CVBS
    
    Panel_CVBS --> config_t
    Panel_CVBS --> config_detail_t
    
    config_detail_t --> ESP32_DAC
    config_detail_t --> PSRAM
    config_detail_t -.->|signal_type| NTSC
    config_detail_t -.->|signal_type| NTSC_J
    config_detail_t -.->|signal_type| PAL
    config_detail_t -.->|signal_type| PAL_M
    config_detail_t -.->|signal_type| PAL_N
    
    Panel_CVBS --> ESP32_DAC
    Panel_CVBS --> PSRAM
    Panel_CVBS --> DMA
```

**Sources:** [src/M5ModuleRCA.h:10-11](), [src/M5UnitRCA.h:10-11](), [src/M5ModuleRCA.h:53-54](), [src/M5UnitRCA.h:53-54]()

---

## Signal Type Configuration

The `Panel_CVBS` driver supports five composite video standards through the `signal_type_t` enumeration. Each standard defines specific timing, line count, field rate, and pedestal levels.

| Signal Type | Lines | Field Rate | Pedestal Level | Region |
|-------------|-------|-----------|----------------|---------|
| `NTSC` | 525 | 60Hz | 7.5 IRE | North America |
| `NTSC_J` | 525 | 60Hz | 0 IRE | Japan |
| `PAL` | 625 | 50Hz | 0 IRE | Europe/Asia |
| `PAL_M` | 525 | 60Hz | 0 IRE | Brazil |
| `PAL_N` | 625 | 50Hz | 0 IRE | Argentina |

The signal type is configured via `config_detail_t::signal_type` and can be changed at runtime using the `setSignalType()` method.

**Sources:** [src/M5ModuleRCA.h:35-36](), [src/M5ModuleRCA.h:58](), [src/M5ModuleRCA.h:258-270](), [src/M5UnitRCA.h:35-36](), [src/M5UnitRCA.h:258-270]()

---

## Configuration System

The composite video panel uses a two-tier configuration structure separating display geometry from signal generation parameters.

```mermaid
graph TB
    subgraph "M5ModuleRCA / M5UnitRCA"
        DeviceConfig["config_t Structure<br/>logical_width: 216<br/>logical_height: 144<br/>output_width: 0 (auto)<br/>output_height: 0 (auto)<br/>signal_type: PAL<br/>use_psram: psram_half_use<br/>pin_dac: GPIO_NUM_26<br/>output_level: 0 (auto)"]
        setup["setup() Method<br/>Calculates offsets<br/>Maps to Panel_CVBS configs"]
    end
    
    subgraph "Panel_CVBS Configuration"
        PanelConfig["config_t<br/>(inherited from IPanel)<br/>panel_width<br/>panel_height<br/>memory_width<br/>memory_height<br/>offset_x<br/>offset_y<br/>offset_rotation"]
        DetailConfig["config_detail_t<br/>(CVBS-specific)<br/>signal_type<br/>use_psram<br/>pin_dac<br/>output_level"]
    end
    
    subgraph "Runtime Methods"
        setSignalType["setSignalType()<br/>Change NTSC/PAL"]
        setPsram["setPsram()<br/>Change memory mode"]
        setOutputPin["setOutputPin()<br/>Change DAC GPIO"]
        setOutputLevel["setOutputLevel()<br/>Adjust voltage"]
        setOutputBoost["setOutputBoost()<br/>Core2 preset"]
    end
    
    DeviceConfig --> setup
    setup --> PanelConfig
    setup --> DetailConfig
    
    PanelConfig --> Panel_CVBS
    DetailConfig --> Panel_CVBS
    
    setSignalType --> DetailConfig
    setPsram --> DetailConfig
    setOutputPin --> DetailConfig
    setOutputLevel --> DetailConfig
    setOutputBoost --> setOutputLevel
```

### Panel Geometry Configuration

The `config_t` structure (inherited from `IPanel`) defines display dimensions:

- **`panel_width` / `panel_height`**: Logical drawing resolution (default 216×144)
- **`memory_width` / `memory_height`**: Physical buffer resolution (auto-calculated or specified)
- **`offset_x` / `offset_y`**: Centering offsets when logical < memory dimensions
- **`offset_rotation`**: Fixed at 3 for proper orientation

**Sources:** [src/M5ModuleRCA.h:65-75](), [src/M5ModuleRCA.h:114-138](), [src/M5UnitRCA.h:65-75](), [src/M5UnitRCA.h:114-138]()

### Signal Generation Configuration

The `config_detail_t` structure contains CVBS-specific parameters:

- **`signal_type`**: Video standard (NTSC, NTSC_J, PAL, PAL_M, PAL_N)
- **`use_psram`**: Memory allocation strategy (see Memory Management section)
- **`pin_dac`**: DAC output GPIO pin (GPIO_NUM_26 on ESP32)
- **`output_level`**: Voltage adjustment value (0-255, default 128)

**Sources:** [src/M5ModuleRCA.h:134-137](), [src/M5UnitRCA.h:134-137]()

---

## Memory Management and PSRAM Usage

Composite video generation requires continuous frame buffer access. The `use_psram` parameter controls memory allocation strategy through three modes:

```mermaid
graph LR
    subgraph "use_psram_t Enumeration"
        psram_no_use["psram_no_use = 0<br/>Use only internal SRAM<br/>Limited resolution"]
        psram_half_use["psram_half_use = 1<br/>Split SRAM + PSRAM<br/>Default mode<br/>Balance performance/size"]
        psram_use["psram_use = 2<br/>Use PSRAM exclusively<br/>Maximum resolution<br/>Slower access"]
    end
    
    psram_no_use --> FrameBuffer["Frame Buffer<br/>Scanline buffers<br/>DMA-compatible memory"]
    psram_half_use --> FrameBuffer
    psram_use --> FrameBuffer
```

| Mode | Value | Memory Source | Use Case |
|------|-------|---------------|----------|
| `psram_no_use` | 0 | Internal SRAM only | Small resolutions, faster access |
| `psram_half_use` | 1 | SRAM + PSRAM split | Default, balanced performance |
| `psram_use` | 2 | PSRAM only | Maximum resolution, lower speed |

The PSRAM mode can be changed at runtime using `setPsram()`:

```cpp
void setPsram(use_psram_t use_psram);  // Typed enum
void setPsram(uint8_t use_psram);      // Numeric value 0-2
```

**Sources:** [src/M5ModuleRCA.h:44-46](), [src/M5ModuleRCA.h:59-63](), [src/M5ModuleRCA.h:273-292](), [src/M5UnitRCA.h:44-46](), [src/M5UnitRCA.h:273-292]()

---

## Output Signal Control

### DAC Pin Configuration

The composite video signal is output through an ESP32 DAC-capable GPIO pin. The default configuration is `GPIO_NUM_26` on ESP32, which is compatible with M5Stack Module/Unit RCA hardware.

```mermaid
graph TB
    subgraph "ESP32 GPIO Routing"
        GPIO26["GPIO_NUM_26<br/>DAC Channel 1<br/>Default RCA output"]
        GPIO25["GPIO_NUM_25<br/>DAC Channel 2<br/>Alternative pin"]
    end
    
    subgraph "Pin Configuration Flow"
        DefaultPin["M5MODULERCA_PIN_DAC<br/>M5UNITRCA_PIN_DAC<br/>Compile-time default"]
        config_detail["config_detail_t.pin_dac<br/>Runtime configuration"]
        setOutputPin["setOutputPin(uint8_t)<br/>Dynamic reconfiguration"]
    end
    
    DefaultPin --> config_detail
    config_detail --> Panel_CVBS
    setOutputPin --> config_detail
    
    Panel_CVBS --> GPIO26
    Panel_CVBS -.->|alternative| GPIO25
```

**Sources:** [src/M5ModuleRCA.h:15-20](), [src/M5ModuleRCA.h:249-256](), [src/M5UnitRCA.h:15-20](), [src/M5UnitRCA.h:249-256]()

### Output Level Adjustment

The `output_level` parameter (0-255) adjusts the DAC output voltage to compensate for protection resistors in the signal path. Different M5Stack hardware requires different levels due to varying resistor values:

```mermaid
graph TB
    subgraph "Hardware Detection and Auto-Configuration"
        AutoDetect["output_level == 0<br/>Auto-detect mode"]
        ProbeI2C["Probe I2C addr 0x34<br/>Register 0x03"]
        
        CheckAXP{AXP ID?}
        
        Core2["AXP192 (ID=0x03)<br/>M5Stack Core2/Tough<br/>output_level = 200"]
        Basic["Other<br/>M5Stack Basic/Fire/Go<br/>output_level = 128"]
    end
    
    subgraph "Manual Configuration"
        setOutputLevel["setOutputLevel(uint8_t)<br/>Manual override<br/>0-255 range"]
        setOutputBoost["setOutputBoost(bool)<br/>Core2 helper<br/>200 (boost) or 128"]
    end
    
    AutoDetect --> ProbeI2C
    ProbeI2C --> CheckAXP
    CheckAXP -->|0x03| Core2
    CheckAXP -->|other| Basic
    
    setOutputBoost --> setOutputLevel
```

The output level is auto-detected on ESP32 by probing for the AXP192 PMIC (present on Core2/Tough). If detected, level is set to 200; otherwise defaults to 128 for Basic/Fire/Go.

**Sources:** [src/M5ModuleRCA.h:196-211](), [src/M5ModuleRCA.h:232-247](), [src/M5UnitRCA.h:196-211](), [src/M5UnitRCA.h:232-247]()

---

## Platform-Specific Implementation

### ESP32 Platform

On ESP32 hardware, the `Panel_CVBS` driver uses the DAC peripheral with I2S/DMA for continuous signal generation. The initialization process includes:

1. Allocate frame buffer (SRAM/PSRAM based on `use_psram`)
2. Configure DAC output on specified GPIO pin
3. Setup I2S peripheral for timed DAC updates
4. Configure DMA descriptors for scanline streaming
5. Generate sync pulses and video data according to `signal_type`

```mermaid
graph TB
    init_impl["init_impl()<br/>Device class initialization"]
    
    CreatePanel["new Panel_CVBS()"]
    
    AutoConfig["Auto-detect output_level<br/>Probe AXP192 PMIC"]
    
    ConfigPanel["config(_cfg)<br/>Set panel geometry"]
    
    ConfigDetail["config_detail(_cfg_detail)<br/>Set signal parameters"]
    
    SetRotation["setRotation(1)<br/>Landscape orientation"]
    
    BaseInit["LGFX_Device::init_impl()<br/>Panel initialization"]
    
    DACSetup["DAC GPIO configuration<br/>I2S peripheral setup<br/>DMA descriptor chain"]
    
    SignalGen["Video signal generation<br/>Continuous output"]
    
    init_impl --> CreatePanel
    CreatePanel --> AutoConfig
    AutoConfig --> ConfigPanel
    ConfigPanel --> ConfigDetail
    ConfigDetail --> SetRotation
    SetRotation --> BaseInit
    BaseInit --> DACSetup
    DACSetup --> SignalGen
```

**Sources:** [src/M5ModuleRCA.h:183-230](), [src/M5UnitRCA.h:183-230]()

### SDL Simulation Platform

When compiled with SDL support, the device classes instantiate `Panel_sdl` instead of `Panel_CVBS`, rendering to a desktop window with appropriate scaling for composite video aspect ratios.

```mermaid
graph TB
    SDL_Init["init_impl() with SDL_h_ defined"]
    
    CreateSDL["new Panel_sdl()"]
    
    SetDimensions["memory_width/height<br/>panel_width/height<br/>from config"]
    
    SetTitle["setWindowTitle()<br/>'ModuleRCA' or 'UnitRCA'"]
    
    SetScaling["setScaling(864/width, 576/height)<br/>CRT aspect ratio scaling"]
    
    SetRotation["setRotation(1)<br/>Landscape mode"]
    
    StubMethods["Stub methods:<br/>setOutputLevel()<br/>setSignalType()<br/>setPsram()<br/>etc."]
    
    SDL_Init --> CreateSDL
    CreateSDL --> SetDimensions
    SetDimensions --> SetTitle
    SetTitle --> SetScaling
    SetScaling --> SetRotation
    SetRotation --> StubMethods
```

The SDL implementation provides no-op stubs for all CVBS-specific methods (signal type, output level, PSRAM control) since they have no meaning in desktop simulation.

**Sources:** [src/M5ModuleRCA.h:140-180](), [src/M5UnitRCA.h:140-180]()

---

## M5ModuleRCA Device Class

The `M5ModuleRCA` class provides a pre-configured composite video display for the M5Stack Module RCA hardware, which connects to the M5Stack Core/Core2 via the M-Bus connector.

### Default Configuration

| Parameter | Default Value | Macro Override |
|-----------|---------------|----------------|
| Logical Width | 216 | `M5MODULERCA_LOGICAL_WIDTH` |
| Logical Height | 144 | `M5MODULERCA_LOGICAL_HEIGHT` |
| Signal Type | PAL | `M5MODULERCA_SIGNAL_TYPE` |
| Output Width | 0 (auto) | `M5MODULERCA_OUTPUT_WIDTH` |
| Output Height | 0 (auto) | `M5MODULERCA_OUTPUT_HEIGHT` |
| PSRAM Mode | `psram_half_use` | `M5MODULERCA_USE_PSRAM` |
| DAC Pin | GPIO_NUM_26 | `M5MODULERCA_PIN_DAC` |
| Output Level | 0 (auto) | `M5MODULERCA_OUTPUT_LEVEL` |

### Initialization Example

```cpp
// Default configuration
M5ModuleRCA display;
display.init();

// Custom resolution and signal type
M5ModuleRCA display(320, 240, 0, 0, 
                    M5ModuleRCA::signal_type_t::NTSC);
display.init();

// Using config_t structure
M5ModuleRCA::config_t cfg;
cfg.logical_width = 256;
cfg.logical_height = 192;
cfg.signal_type = M5ModuleRCA::signal_type_t::NTSC_J;
cfg.use_psram = M5ModuleRCA::psram_use;
M5ModuleRCA display(cfg);
display.init();
```

**Sources:** [src/M5ModuleRCA.h:29-49](), [src/M5ModuleRCA.h:65-75](), [src/M5ModuleRCA.h:79-97]()

---

## M5UnitRCA Device Class

The `M5UnitRCA` class provides identical functionality to `M5ModuleRCA` but is designated for the M5Stack Unit RCA hardware, which connects via PortA/PortB Grove connectors.

The class implementation is nearly identical to `M5ModuleRCA`, differing only in:
- Board type identifier: `board_t::board_M5UnitRCA`
- SDL window title: "UnitRCA" vs "ModuleRCA"

All configuration parameters, macros, and methods are the same.

**Sources:** [src/M5UnitRCA.h:29-49](), [src/M5UnitRCA.h:65-75](), [src/M5UnitRCA.h:79-97]()

---

## Runtime Configuration Methods

Both device classes expose methods to reconfigure the composite video output after initialization:

| Method | Parameters | Purpose |
|--------|------------|---------|
| `setSignalType()` | `signal_type_t` | Switch between NTSC/PAL variants |
| `setOutputLevel()` | `uint8_t (0-255)` | Adjust DAC output voltage |
| `setOutputBoost()` | `bool` | Preset for Core2 (200) or Basic (128) |
| `setOutputPin()` | `uint8_t` | Change DAC GPIO pin |
| `setPsram()` | `use_psram_t` or `uint8_t` | Change memory allocation mode |

All methods retrieve the current `Panel_CVBS` instance via `_panel_last.get()`, read the existing configuration, modify the specified parameter, and write the updated configuration back to the panel.

**Example Usage:**

```cpp
M5ModuleRCA display;
display.init();

// Switch from default PAL to NTSC
display.setSignalType(M5ModuleRCA::signal_type_t::NTSC);

// Boost output for Core2 hardware
display.setOutputBoost(true);

// Use PSRAM exclusively for higher resolution
display.setPsram(M5ModuleRCA::psram_use);
```

**Sources:** [src/M5ModuleRCA.h:232-292](), [src/M5UnitRCA.h:232-292]()