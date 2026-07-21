M5Cardputer M5Cardputer Core API

# M5Cardputer Core API

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5Cardputer.cpp](src/M5Cardputer.cpp)
- [src/M5Cardputer.h](src/M5Cardputer.h)

</details>



## Purpose and Scope

This document provides comprehensive reference documentation for the `M5_CARDPUTER` class, the primary interface for interacting with M5Cardputer hardware. The `M5_CARDPUTER` class aggregates hardware components, manages initialization, and provides the main update loop for applications.

This page covers the class structure, component ownership model, and initialization patterns. For detailed information on specific subsystems, see:
- Initialization methods and configuration options: [Initialization and Configuration](#3.1)
- Accessing Display, Speaker, Mic, Power, and Button: [Hardware Component Access](#3.2)
- Internal and external I2C bus management: [I2C Bus Management](#3.3)
- Keyboard-specific APIs: [Keyboard_Class API](#4.1)

---

## The M5_CARDPUTER Class

The `M5_CARDPUTER` class [src/M5Cardputer.h:14-39]() serves as the unified entry point for all M5Cardputer functionality. It follows a hybrid ownership model: most hardware peripherals are **referenced** from the M5Unified singleton, while device-specific components like the keyboard are **directly owned**.

### Global Instance

The library provides a pre-instantiated global object:

```cpp
extern m5::M5_CARDPUTER M5Cardputer;
```

Applications interact with the hardware exclusively through this global `M5Cardputer` instance [src/M5Cardputer.cpp:10]().

**Sources:** [src/M5Cardputer.h:43](), [src/M5Cardputer.cpp:10]()

---

## Class Structure

The following diagram maps the `M5_CARDPUTER` class members to their code entities:

```mermaid
classDiagram
    class M5_CARDPUTER {
        +begin(bool enableKeyboard)
        +begin(M5Unified::config_t cfg, bool enableKeyboard)
        +update()
        +M5GFX& Display
        +M5GFX& Lcd
        +Power_Class& Power
        +Speaker_Class& Speaker
        +Mic_Class& Mic
        +Button_Class& BtnA
        +Keyboard_Class Keyboard
        +I2C_Class& In_I2C
        +I2C_Class& Ex_I2C
        -bool _enableKeyboard
    }
    
    class M5Unified_Singleton["M5 (M5Unified singleton)"] {
        +M5GFX Display
        +Power_Class Power
        +Speaker_Class Speaker
        +Mic_Class Mic
        +Button_Class getButton(int)
        +begin()
        +update()
    }
    
    class Keyboard_Class {
        +begin()
        +updateKeyList()
        +updateKeysState()
    }
    
    class I2C_Class_Internal["m5::In_I2C"] {
        <<internal bus>>
    }
    
    class I2C_Class_External["m5::Ex_I2C"] {
        <<external bus>>
    }
    
    M5_CARDPUTER "references" --> M5Unified_Singleton : "Display, Lcd, Power,\nSpeaker, Mic, BtnA"
    M5_CARDPUTER "owns" --> Keyboard_Class : "Keyboard"
    M5_CARDPUTER "references" --> I2C_Class_Internal : "In_I2C"
    M5_CARDPUTER "references" --> I2C_Class_External : "Ex_I2C"
```

**Key Observations:**
- **Referenced Components**: `Display`, `Lcd`, `Power`, `Speaker`, `Mic`, and `BtnA` are reference members [src/M5Cardputer.h:19-24]() pointing to the corresponding components in the M5Unified singleton
- **Owned Component**: `Keyboard` is a directly owned instance [src/M5Cardputer.h:26]()
- **I2C Bus References**: `In_I2C` and `Ex_I2C` reference global I2C bus objects [src/M5Cardputer.h:29,32]()

**Sources:** [src/M5Cardputer.h:14-39]()

---

## Component Ownership Model

The following diagram illustrates the ownership and reference relationships:

```mermaid
graph TB
    subgraph "Application Code"
        APP["Application"]
    end
    
    subgraph "M5Cardputer Global Instance"
        M5C["M5Cardputer"]
        
        subgraph "Direct Members (References)"
            REF_DISP["Display &"]
            REF_LCD["Lcd &"]
            REF_PWR["Power &"]
            REF_SPK["Speaker &"]
            REF_MIC["Mic &"]
            REF_BTN["BtnA &"]
            REF_IN_I2C["In_I2C &"]
            REF_EX_I2C["Ex_I2C &"]
        end
        
        subgraph "Direct Members (Owned)"
            OWN_KB["Keyboard"]
        end
    end
    
    subgraph "M5Unified Singleton"
        M5["M5"]
        M5_DISP["M5.Display"]
        M5_PWR["M5.Power"]
        M5_SPK["M5.Speaker"]
        M5_MIC["M5.Mic"]
        M5_BTN["M5.getButton(0)"]
    end
    
    subgraph "Global I2C Buses"
        IN_I2C["m5::In_I2C"]
        EX_I2C["m5::Ex_I2C"]
    end
    
    APP -->|uses| M5C
    
    M5C --> OWN_KB
    
    REF_DISP -.->|references| M5_DISP
    REF_LCD -.->|references| M5_DISP
    REF_PWR -.->|references| M5_PWR
    REF_SPK -.->|references| M5_SPK
    REF_MIC -.->|references| M5_MIC
    REF_BTN -.->|references| M5_BTN
    REF_IN_I2C -.->|references| IN_I2C
    REF_EX_I2C -.->|references| EX_I2C
    
    M5_DISP --> M5
    M5_PWR --> M5
    M5_SPK --> M5
    M5_MIC --> M5
    M5_BTN --> M5
```

**Design Rationale:**

| Component Type | Ownership | Rationale |
|---------------|-----------|-----------|
| Display, Power, Speaker, Mic, BtnA | Reference to M5 singleton | These are standard M5Stack peripherals shared across all M5 devices. Referencing prevents duplication and ensures unified state management. |
| Keyboard | Direct ownership | Device-specific to M5Cardputer. Not provided by M5Unified, so `M5_CARDPUTER` owns and manages it directly. |
| I2C Buses | Reference to globals | Global bus objects allow sharing across modules. References provide convenient access. |

**Sources:** [src/M5Cardputer.h:19-32]()

---

## Initialization Methods

The `M5_CARDPUTER` class provides two initialization methods:

### Method 1: Simple Initialization

```cpp
void begin(bool enableKeyboard = true);
```

[src/M5Cardputer.h:16](), [src/M5Cardputer.cpp:12-19]()

Initializes the M5Cardputer with default M5Unified configuration. The `enableKeyboard` parameter controls whether the keyboard subsystem is initialized.

**Behavior:**
1. Calls `M5.begin()` [src/M5Cardputer.cpp:14]()
2. Stores `enableKeyboard` flag [src/M5Cardputer.cpp:15]()
3. If `enableKeyboard` is true, calls `Keyboard.begin()` [src/M5Cardputer.cpp:16-18]()

### Method 2: Custom Configuration

```cpp
void begin(m5::M5Unified::config_t cfg, bool enableKeyboard = true);
```

[src/M5Cardputer.h:17](), [src/M5Cardputer.cpp:21-28]()

Initializes the M5Cardputer with custom M5Unified configuration. Allows fine-grained control over internal I2C, external I2C, display, LED, and power management settings.

**Behavior:**
1. Calls `M5.begin(cfg)` with custom configuration [src/M5Cardputer.cpp:23]()
2. Stores `enableKeyboard` flag [src/M5Cardputer.cpp:24]()
3. If `enableKeyboard` is true, calls `Keyboard.begin()` [src/M5Cardputer.cpp:25-27]()

For detailed configuration options and initialization lifecycle, see [Initialization and Configuration](#3.1).

**Sources:** [src/M5Cardputer.h:16-17](), [src/M5Cardputer.cpp:12-28]()

---

## Update Method

The `update()` method must be called regularly in the application main loop:

```cpp
void update(void);
```

[src/M5Cardputer.h:34](), [src/M5Cardputer.cpp:30-37]()

### Initialization Sequence

```mermaid
sequenceDiagram
    participant App as "Application"
    participant M5C as "M5Cardputer"
    participant M5U as "M5 Singleton"
    participant KB as "Keyboard"
    
    App->>M5C: "begin()"
    M5C->>M5U: "M5.begin()"
    M5U-->>M5C: "initialized"
    M5C->>M5C: "store _enableKeyboard"
    alt enableKeyboard == true
        M5C->>KB: "Keyboard.begin()"
        KB-->>M5C: "initialized"
    end
    M5C-->>App: "ready"
    
    loop "Main Loop"
        App->>M5C: "update()"
        M5C->>M5U: "M5.update()"
        alt _enableKeyboard == true
            M5C->>KB: "Keyboard.updateKeyList()"
            M5C->>KB: "Keyboard.updateKeysState()"
        end
        M5C-->>App: "state updated"
    end
```

**Update Cycle:**
1. Calls `M5.update()` to refresh M5Unified state (buttons, power, etc.) [src/M5Cardputer.cpp:32]()
2. If keyboard is enabled:
   - Calls `Keyboard.updateKeyList()` to scan for pressed keys [src/M5Cardputer.cpp:34]()
   - Calls `Keyboard.updateKeysState()` to process key states and generate events [src/M5Cardputer.cpp:35]()

**Sources:** [src/M5Cardputer.cpp:30-37]()

---

## Basic Usage Pattern

The following example demonstrates the standard initialization and update pattern:

```cpp
#include <M5Cardputer.h>

void setup() {
    // Initialize M5Cardputer with keyboard enabled
    M5Cardputer.begin();
    
    // Access display
    M5Cardputer.Display.setTextSize(2);
    M5Cardputer.Display.println("Ready");
}

void loop() {
    // Update all subsystems
    M5Cardputer.update();
    
    // Check keyboard input
    if (M5Cardputer.Keyboard.isChange()) {
        // Process keyboard events
    }
    
    // Check button
    if (M5Cardputer.BtnA.wasPressed()) {
        // Handle button press
    }
}
```

This pattern ensures:
- All hardware is properly initialized during `setup()`
- Component states are refreshed every loop iteration via `update()`
- Applications can query component states after each update

**Sources:** [src/M5Cardputer.h:16,34](), [src/M5Cardputer.cpp:12-37]()

---

## Member Summary Table

| Member | Type | Access | Purpose |
|--------|------|--------|---------|
| `Display` | `M5GFX&` | Reference | Primary display interface for graphics operations |
| `Lcd` | `M5GFX&` | Reference | Alias for `Display` (backward compatibility) |
| `Power` | `Power_Class&` | Reference | Battery and power management |
| `Speaker` | `Speaker_Class&` | Reference | Audio output (tones and WAV playback) |
| `Mic` | `Mic_Class&` | Reference | Microphone input and recording |
| `BtnA` | `Button_Class&` | Reference | Physical button on the device |
| `Keyboard` | `Keyboard_Class` | Owned | Full keyboard input processing |
| `In_I2C` | `I2C_Class&` | Reference | Internal I2C bus for onboard devices |
| `Ex_I2C` | `I2C_Class&` | Reference | External I2C bus (Port.A connector) |

**Sources:** [src/M5Cardputer.h:19-32]()

---

## Implementation Details

### Namespace

The `M5_CARDPUTER` class is defined in the `m5` namespace [src/M5Cardputer.h:12]():

```cpp
namespace m5 {
    class M5_CARDPUTER { /* ... */ };
}
```

The global instance is in the global namespace for convenience:

```cpp
extern m5::M5_CARDPUTER M5Cardputer;
```

### Private Members

The class maintains a single private member [src/M5Cardputer.h:38]():

```cpp
bool _enableKeyboard;
```

This flag stores whether the keyboard subsystem is active, controlling whether keyboard update methods are called in `update()` [src/M5Cardputer.cpp:33-36]().

**Sources:** [src/M5Cardputer.h:12,38,43](), [src/M5Cardputer.cpp:33-36]()

---

## Relationship to M5Unified

```mermaid
graph LR
    subgraph "Application Layer"
        APP["Application Code"]
    end
    
    subgraph "M5Cardputer Library"
        M5C["M5Cardputer<br/>(M5_CARDPUTER instance)"]
        KB["Keyboard_Class"]
    end
    
    subgraph "M5Unified Library"
        M5["M5<br/>(M5Unified singleton)"]
        DISP["Display"]
        PWR["Power"]
        SPK["Speaker"]
        MIC["Mic"]
        BTN["Button"]
    end
    
    subgraph "Hardware Abstraction"
        M5GFX["M5GFX"]
        ESP32["ESP32 Platform"]
    end
    
    APP -->|uses| M5C
    M5C -->|owns| KB
    M5C -.->|references| M5
    M5 --> DISP
    M5 --> PWR
    M5 --> SPK
    M5 --> MIC
    M5 --> BTN
    M5 --> M5GFX
    M5GFX --> ESP32
    KB --> ESP32
```

The `M5_CARDPUTER` class acts as a **facade** that:
1. Wraps M5Unified functionality for standard peripherals
2. Extends M5Unified with device-specific features (Keyboard)
3. Provides a unified, simplified interface for applications
4. Manages the initialization and update lifecycle for both M5Unified and device-specific components

This design allows applications to use a single consistent interface (`M5Cardputer`) while leveraging the full M5Stack ecosystem underneath.

**Sources:** [src/M5Cardputer.h:9-10,14-39](), [src/M5Cardputer.cpp:10-37]()