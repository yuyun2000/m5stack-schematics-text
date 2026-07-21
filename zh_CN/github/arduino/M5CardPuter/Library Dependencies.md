M5Cardputer Library Dependencies

# Library Dependencies

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [library.json](library.json)
- [library.properties](library.properties)

</details>



## Purpose and Scope

This document details the external library dependencies required by M5Cardputer v1.1.1. Each dependency is explained in terms of its role within the library architecture, the functionality it provides, and how it integrates with the M5Cardputer API. For information about the hardware variants that these dependencies support, see [Supported Hardware](#1.2). For details on how to initialize the library with these dependencies, see [Initialization and Configuration](#3.1).

---

## Dependency Overview

The M5Cardputer library declares four external dependencies that provide core functionality across display, device management, infrared communication, and secure networking capabilities.

| Dependency | Category | Purpose | Declared In |
|------------|----------|---------|-------------|
| **M5Unified** | Device Abstraction | Unified API for M5Stack hardware components including power, I2C, buttons, speaker, and microphone | [library.properties:11]() |
| **M5GFX** | Graphics Framework | High-performance graphics rendering, text display, and sprite management | [library.properties:11]() |
| **IRremote** | Communication | Infrared signal transmission and reception | [library.properties:11]() |
| **LibSSH-ESP32** | Networking | SSH client implementation for secure remote terminal access | [library.properties:11]() |

**Sources:** [library.properties:1-11](), [library.json:22-26]()

---

## Dependency Declaration Files

The M5Cardputer library declares its dependencies in two metadata files using different formats for Arduino Library Manager and PlatformIO compatibility.

### Dependency Declaration in Library Metadata

```mermaid
graph TB
    subgraph "Library Metadata Files"
        PROP["library.properties<br/>(Arduino Format)"]
        JSON["library.json<br/>(PlatformIO Format)"]
    end
    
    subgraph "Declared Dependencies"
        M5U["M5Unified<br/>Device Abstraction Layer"]
        M5G["M5GFX<br/>Graphics Framework"]
        IR["IRremote<br/>Infrared Communication"]
        SSH["LibSSH-ESP32<br/>SSH Client"]
    end
    
    PROP -->|"depends field"| M5U
    PROP -->|"depends field"| M5G
    PROP -->|"depends field"| IR
    PROP -->|"depends field"| SSH
    
    JSON -->|"dependencies object"| M5U
    JSON -->|"dependencies object"| M5G
    JSON -->|"dependencies object"| IR
    JSON -.->|"omitted"| SSH
    
    style PROP fill:#f9f9f9
    style JSON fill:#f9f9f9
```

**Note:** `LibSSH-ESP32` is declared in [library.properties:11]() but omitted from [library.json:22-26](), likely due to PlatformIO repository availability constraints. Applications requiring SSH functionality must manually include this dependency.

**Sources:** [library.properties:11](), [library.json:22-26]()

---

## Dependency Architecture

The following diagram shows how dependencies integrate with the M5Cardputer library structure and which components they provide.

### M5Cardputer Dependency Integration

```mermaid
graph TB
    subgraph "User Application Layer"
        APP["Application Code"]
    end
    
    subgraph "M5Cardputer Library"
        M5C["M5_CARDPUTER class<br/>Main API Interface"]
        KB["Keyboard_Class<br/>Device-Specific Input"]
    end
    
    subgraph "External Dependencies"
        M5U_LIB["M5Unified Library"]
        M5G_LIB["M5GFX Library"]
        IR_LIB["IRremote Library"]
        SSH_LIB["LibSSH-ESP32 Library"]
    end
    
    subgraph "Component References from M5Unified"
        DISPLAY["Display & Lcd<br/>M5GFX instances"]
        POWER["Power_Class"]
        SPEAKER["Speaker_Class"]
        MIC["Mic_Class"]
        BUTTON["Button_Class"]
        I2C["I2C Buses<br/>In_I2C & Ex_I2C"]
    end
    
    APP -->|"uses M5Cardputer global"| M5C
    
    M5C -.->|"references M5.Display"| DISPLAY
    M5C -.->|"references M5.Power"| POWER
    M5C -.->|"references M5.Speaker"| SPEAKER
    M5C -.->|"references M5.Mic"| MIC
    M5C -.->|"references M5.BtnA"| BUTTON
    M5C -.->|"references M5.In_I2C/Ex_I2C"| I2C
    M5C -->|"owns instance"| KB
    
    M5U_LIB --> POWER
    M5U_LIB --> SPEAKER
    M5U_LIB --> MIC
    M5U_LIB --> BUTTON
    M5U_LIB --> I2C
    
    M5G_LIB --> DISPLAY
    
    KB -.->|"uses for coordinate detection"| I2C
    
    APP -.->|"direct use in examples"| IR_LIB
    APP -.->|"direct use in SSH example"| SSH_LIB
```

**Sources:** [library.properties:11](), [library.json:22-26]()

---

## Dependency Details

### M5Unified

**Purpose:** M5Unified provides a unified device abstraction layer for all M5Stack products, including the M5Cardputer. It manages hardware initialization, power control, I2C buses, buttons, audio input/output, and board variant detection.

**Integration Pattern:** M5Cardputer uses a reference-based architecture where most hardware components (Display, Power, Speaker, Mic, BtnA, I2C buses) are accessed through the `M5` global singleton rather than being duplicated. This ensures unified state management and zero-copy access.

**Key Components Exposed:**
- `M5.Power` - Battery status, power management
- `M5.Speaker` - Audio output and tone generation
- `M5.Mic` - Microphone input and recording
- `M5.BtnA` - Physical button state
- `M5.In_I2C` - Internal I2C bus for onboard components
- `M5.Ex_I2C` - External I2C bus (Port.A expansion)
- `M5.getBoard()` - Hardware variant detection (distinguishes M5Cardputer vs M5Cardputer-ADV)

**Critical for:** Hardware initialization sequence, board detection for keyboard implementation selection, power management, audio I/O, and I2C communication with keyboard controllers.

**Sources:** [library.properties:11](), [library.json:23]()

---

### M5GFX

**Purpose:** M5GFX is a high-performance graphics library optimized for M5Stack displays. It provides hardware-accelerated drawing primitives, text rendering with multiple fonts, sprite management, and display rotation.

**Integration Pattern:** M5Cardputer exposes the `M5.Display` and `M5.Lcd` references which are `M5GFX` instances. Applications use this for all display operations.

**Key Features Used:**
- Text rendering with built-in and custom fonts
- Graphics primitives (lines, rectangles, circles, fill operations)
- Display rotation and coordinate transformation
- Sprite system for efficient graphics composition
- High-speed display updates via DMA

**Critical for:** All visual output including keyboard input display, REPL interfaces, graphics demonstrations, and text-based applications.

**Sources:** [library.properties:11](), [library.json:24]()

---

### IRremote

**Purpose:** IRremote provides infrared signal transmission and reception capabilities using the ESP32's RMT (Remote Control) peripheral.

**Integration Pattern:** IRremote is not wrapped by M5Cardputer but is declared as a dependency because IR functionality is hardware-supported and commonly used in M5Cardputer applications. Applications must directly initialize and use the IRremote library.

**Typical Usage:**
- IR remote control transmission
- IR signal reception and decoding
- Custom IR protocol implementation

**Critical for:** Applications requiring infrared communication such as remote controls, IR-based data exchange, or appliance control.

**Sources:** [library.properties:11](), [library.json:25]()

---

### LibSSH-ESP32

**Purpose:** LibSSH-ESP32 is an ESP32 port of the libssh library, providing SSH client functionality for secure remote terminal access.

**Integration Pattern:** LibSSH-ESP32 is not wrapped by M5Cardputer. It is declared as a dependency in `library.properties` to support SSH client examples but must be directly initialized and used by applications. This dependency is **omitted from library.json**, requiring manual installation in PlatformIO environments.

**Key Features:**
- SSH client connection establishment
- Password and key-based authentication
- Remote command execution
- Interactive shell sessions
- Secure channel management

**Critical for:** SSH terminal applications, remote server management tools, and secure IoT device communication.

**Sources:** [library.properties:11]()

---

## Version Constraints

### Wildcard Version Policy

```mermaid
graph LR
    subgraph "Version Specification"
        JSON_DEPS["library.json dependencies object"]
        VER_SPEC["Version: '*' (wildcard)"]
    end
    
    subgraph "Resolution Strategy"
        LATEST["Use latest compatible version<br/>from package manager"]
    end
    
    subgraph "Dependencies with Wildcards"
        M5U_V["M5Unified: *"]
        M5G_V["M5GFX: *"]
        IR_V["IRremote: *"]
    end
    
    JSON_DEPS --> VER_SPEC
    VER_SPEC --> LATEST
    
    LATEST --> M5U_V
    LATEST --> M5G_V
    LATEST --> IR_V
```

All dependencies in [library.json:22-26]() use wildcard version specifiers (`"*"`), meaning the library manager will install the latest available version compatible with the ESP32 platform. This approach:

- **Advantages:** Automatically benefits from bug fixes and performance improvements in dependencies
- **Risks:** Potential breaking changes if dependencies introduce incompatible API changes
- **Mitigation:** M5Stack maintains M5Unified and M5GFX, ensuring coordinated releases

**Sources:** [library.json:22-26]()

---

## Dependency Installation

### Arduino IDE

When installing M5Cardputer via Arduino Library Manager, the following dependencies are automatically resolved and installed:
- M5Unified
- M5GFX
- IRremote
- LibSSH-ESP32

### PlatformIO

Add to `platformio.ini`:
```ini
lib_deps = 
    M5Cardputer
    LibSSH-ESP32  ; Required for SSH examples, not auto-resolved
```

The M5Unified, M5GFX, and IRremote dependencies are automatically resolved. LibSSH-ESP32 must be manually added due to its omission from [library.json:22-26]().

**Sources:** [library.properties:11](), [library.json:22-26]()

---

## Dependency Graph

### Complete Dependency Tree

```mermaid
graph TB
    subgraph "Application"
        APP["User Application"]
    end
    
    subgraph "M5Cardputer v1.1.1"
        CARD["M5Cardputer Library<br/>ESP32 Platform<br/>Display Category"]
    end
    
    subgraph "Required Dependencies"
        M5U["M5Unified<br/>(wildcard version)"]
        M5G["M5GFX<br/>(wildcard version)"]
        IR["IRremote<br/>(wildcard version)"]
        SSH["LibSSH-ESP32<br/>(no version constraint)"]
    end
    
    subgraph "Transitive Dependencies"
        M5U_DEPS["M5Unified Dependencies<br/>(ESP32-specific libraries)"]
        M5G_DEPS["M5GFX Dependencies<br/>(TFT/LCD drivers)"]
    end
    
    APP -->|"includes M5Cardputer.h"| CARD
    
    CARD -->|"required"| M5U
    CARD -->|"required"| M5G
    CARD -->|"required"| IR
    CARD -->|"optional (examples)"| SSH
    
    M5U --> M5U_DEPS
    M5G --> M5G_DEPS
    
    style CARD fill:#f9f9f9
    style SSH stroke-dasharray: 5 5
```

**Legend:** Dashed border indicates optional/example-only dependency (LibSSH-ESP32)

**Sources:** [library.properties:1-11](), [library.json:1-26]()

---

## Summary Table

| Library | Version | Provided By | Used For | Auto-Installed |
|---------|---------|-------------|----------|----------------|
| **M5Unified** | Latest (wildcard) | M5Stack | Device abstraction, power, audio, I2C, board detection | Yes (all platforms) |
| **M5GFX** | Latest (wildcard) | M5Stack | Graphics rendering, text display, sprites | Yes (all platforms) |
| **IRremote** | Latest (wildcard) | Third-party | Infrared communication | Yes (all platforms) |
| **LibSSH-ESP32** | Unspecified | Third-party | SSH client functionality | Yes (Arduino), Manual (PlatformIO) |

**Sources:** [library.properties:1-11](), [library.json:1-26]()