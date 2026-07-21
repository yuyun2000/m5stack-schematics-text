M5Cardputer Supported Hardware

# Supported Hardware

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [library.properties](library.properties)
- [src/utility/Keyboard/KeyboardReader/TCA8418.cpp](src/utility/Keyboard/KeyboardReader/TCA8418.cpp)
- [src/utility/common.h](src/utility/common.h)

</details>



## Purpose and Scope

This document describes the two hardware variants supported by the M5Cardputer library: the **M5Cardputer** (standard) and **M5Cardputer-ADV** boards. It details their hardware differences, particularly in keyboard implementation, and explains how the library provides automatic hardware detection and variant-specific initialization while maintaining a unified API.

For information about the library's external dependencies, see [Library Dependencies](#1.1). For initialization procedures and runtime board detection algorithms, see [Hardware Variant Detection](#11.2).

**Sources:** [library.properties:5]()

---

## Hardware Variants Overview

The library supports two distinct hardware variants of the M5Cardputer board, which differ primarily in their keyboard hardware implementation:

| Feature | M5Cardputer (Standard) | M5Cardputer-ADV |
|---------|------------------------|-----------------|
| **Board Identifier** | `board_M5Cardputer` | `board_M5CardputerADV` |
| **Keyboard Technology** | Direct GPIO matrix scanning | TCA8418 I2C keyboard controller |
| **Keyboard Matrix Size** | 8×7 (remapped from 3×7 GPIO) | 7×8 (TCA8418 native) |
| **Interrupt Support** | Polling-based | Hardware interrupt on GPIO 11 |
| **I2C Address** | N/A | 0x34 (TCA8418) |
| **GPIO Pin Usage** | 3 output + 7 input pins | 1 interrupt pin |
| **KeyboardReader Implementation** | `IOMatrixKeyboardReader` | `TCA8418KeyboardReader` |

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:12-13](), high-level diagrams

---

## M5Cardputer (Standard Board)

### Hardware Architecture

The standard M5Cardputer board uses direct GPIO matrix scanning for keyboard input. The physical keyboard is wired as a matrix that requires dedicated GPIO pins for scanning.

```mermaid
graph TB
    subgraph "M5Cardputer Standard Hardware"
        KB["Physical Keyboard<br/>56 keys"]
        
        subgraph "GPIO Matrix Configuration"
            OUT["3 Output Pins<br/>Drive rows"]
            IN["7 Input Pins<br/>Read columns"]
        end
        
        subgraph "Matrix Layout"
            MAT["8×7 Logical Matrix<br/>(with coordinate remapping)"]
        end
        
        READER["IOMatrixKeyboardReader"]
    end
    
    KB -->|"physical wiring"| OUT
    KB -->|"physical wiring"| IN
    OUT --> MAT
    IN --> MAT
    MAT --> READER
    
    READER -->|"polling scan"| OUT
    READER -->|"read state"| IN
```

**Diagram: M5Cardputer Standard Keyboard Hardware Architecture**

### Keyboard Implementation

The `IOMatrixKeyboardReader` class implements keyboard scanning by:
1. Driving output pins high/low in sequence
2. Reading input pin states for each output configuration
3. Detecting key presses based on continuity through the matrix
4. Applying coordinate remapping to translate physical matrix positions to logical key positions

The implementation uses polling rather than interrupts, requiring periodic `update()` calls.

**Sources:** High-level diagrams, inferred from keyboard architecture description

---

## M5Cardputer-ADV

### Hardware Architecture

The M5Cardputer-ADV board uses the TCA8418 I2C keyboard controller IC, which handles matrix scanning in hardware and provides interrupt-driven event notification.

```mermaid
graph TB
    subgraph "M5Cardputer-ADV Hardware"
        KB["Physical Keyboard<br/>56 keys"]
        
        subgraph "TCA8418 Controller"
            TCA["TCA8418 IC<br/>I2C Address: 0x34"]
            MATRIX["7×8 Matrix Scanner<br/>Hardware scan engine"]
            FIFO["Event FIFO<br/>10-event buffer"]
            INT_CTRL["Interrupt Controller"]
        end
        
        subgraph "ESP32 Interface"
            I2C_BUS["Internal I2C Bus"]
            INT_PIN["GPIO 11<br/>Interrupt Pin"]
        end
        
        READER["TCA8418KeyboardReader"]
    end
    
    KB --> MATRIX
    MATRIX --> FIFO
    FIFO --> INT_CTRL
    INT_CTRL --> INT_PIN
    
    TCA --> I2C_BUS
    I2C_BUS --> READER
    INT_PIN --> READER
```

**Diagram: M5Cardputer-ADV Keyboard Hardware Architecture**

### TCA8418 Controller Details

The TCA8418 is a dedicated keyboard controller that:
- Performs hardware matrix scanning autonomously
- Stores up to 10 key events in an internal FIFO
- Generates interrupts when events are available
- Operates on the internal I2C bus at address `0x34`
- Uses GPIO 11 as the interrupt notification pin (default, configurable)

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:12-13]()

### Interrupt Configuration

The interrupt pin configuration occurs during initialization:

[src/utility/Keyboard/KeyboardReader/TCA8418.cpp:42-46]()

The interrupt service routine sets a flag that triggers event processing in the next `update()` call:

[src/utility/Keyboard/KeyboardReader/TCA8418.cpp:22-26]()

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:15-49]()

---

## Hardware Detection and Automatic Reader Selection

### Board Detection Flow

The library automatically detects the hardware variant at runtime and instantiates the appropriate keyboard reader implementation. This process follows the Factory pattern.

```mermaid
graph TB
    BOOT["System Boot"]
    INIT["M5.begin()<br/>M5Unified Initialization"]
    
    DETECT["M5.getBoard()<br/>Returns board type enum"]
    
    subgraph "Board Type Values"
        CARD["board_M5Cardputer"]
        ADV["board_M5CardputerADV"]
    end
    
    KB_BEGIN["Keyboard_Class::begin()"]
    
    subgraph "Factory Logic"
        CHECK{"Board Type?"}
        CREATE_IO["Create IOMatrixKeyboardReader<br/>GPIO-based scanning"]
        CREATE_TCA["Create TCA8418KeyboardReader<br/>I2C controller + interrupt"]
    end
    
    subgraph "Reader Instances"
        IO_INST["IOMatrixKeyboardReader instance"]
        TCA_INST["TCA8418KeyboardReader instance"]
    end
    
    BOOT --> INIT
    INIT --> DETECT
    DETECT --> CARD
    DETECT --> ADV
    
    CARD --> KB_BEGIN
    ADV --> KB_BEGIN
    
    KB_BEGIN --> CHECK
    CHECK -->|"board_M5Cardputer"| CREATE_IO
    CHECK -->|"board_M5CardputerADV"| CREATE_TCA
    
    CREATE_IO --> IO_INST
    CREATE_TCA --> TCA_INST
```

**Diagram: Hardware Detection and Keyboard Reader Factory Pattern**

### TCA8418KeyboardReader Initialization

The constructor accepts an optional interrupt pin parameter, defaulting to GPIO 11 for the M5Cardputer-ADV:

[src/utility/Keyboard/KeyboardReader/TCA8418.cpp:15-20]()

The `begin()` method initializes the TCA8418 controller and configures the interrupt:

[src/utility/Keyboard/KeyboardReader/TCA8418.cpp:28-50]()

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:15-50]()

---

## Coordinate Remapping

Both hardware variants use different physical matrix layouts but map to the same logical keyboard layout. Each reader implementation includes coordinate remapping logic.

### M5Cardputer-ADV Remapping

The TCA8418 reports events in its native 7×8 matrix coordinates, which are remapped to match the standard M5Cardputer layout:

[src/utility/Keyboard/KeyboardReader/TCA8418.cpp:87-101]()

This remapping algorithm transforms:
- **Column calculation:** `col = (row * 2) + (col > 3 ? 1 : 0)`
- **Row calculation:** `row = (col + 4) % 4`

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:87-101]()

---

## Unified Keyboard API

Despite the hardware differences, both implementations satisfy the `KeyboardReader` abstract interface, providing identical functionality to applications:

```mermaid
graph TB
    subgraph "Application Layer"
        APP["Application Code"]
    end
    
    subgraph "Unified API"
        KB_CLASS["Keyboard_Class<br/>Public API"]
    end
    
    subgraph "Abstract Interface"
        INTERFACE["KeyboardReader<br/>Abstract Base Class"]
    end
    
    subgraph "Hardware Implementations"
        IO_IMPL["IOMatrixKeyboardReader<br/>Standard Board"]
        TCA_IMPL["TCA8418KeyboardReader<br/>ADV Board"]
    end
    
    subgraph "Hardware"
        IO_HW["GPIO Matrix<br/>3×7 pins"]
        TCA_HW["TCA8418 IC<br/>I2C + Interrupt"]
    end
    
    APP -->|"isKeyPressed()<br/>getKeysState()"| KB_CLASS
    KB_CLASS -->|"owns pointer to"| INTERFACE
    INTERFACE <-.->|"implements"| IO_IMPL
    INTERFACE <-.->|"implements"| TCA_IMPL
    
    IO_IMPL --> IO_HW
    TCA_IMPL --> TCA_HW
```

**Diagram: Hardware Abstraction Through Polymorphism**

Applications interact exclusively with `Keyboard_Class` methods such as:
- `isKeyPressed(char key)` - Check if a specific key is pressed
- `getKeysState()` - Retrieve complete keyboard state
- `isChange()` - Detect state changes
- `update()` - Process hardware events

The keyboard reader implementation is entirely transparent to application code, enabling the same application to run on both hardware variants without modification.

**Sources:** High-level diagrams, architectural descriptions

---

## Hardware Specification Summary

### Pin Assignments

| Signal | M5Cardputer | M5Cardputer-ADV |
|--------|-------------|-----------------|
| **Keyboard Output** | GPIO (3 pins) | N/A |
| **Keyboard Input** | GPIO (7 pins) | N/A |
| **I2C SDA** | N/A | Internal I2C Bus |
| **I2C SCL** | N/A | Internal I2C Bus |
| **Interrupt** | N/A | GPIO 11 (default) |

### Communication Parameters

| Parameter | M5Cardputer | M5Cardputer-ADV |
|-----------|-------------|-----------------|
| **Scan Method** | GPIO polling | Hardware scan + I2C read |
| **Update Frequency** | Application-controlled | Interrupt-driven |
| **I2C Address** | N/A | 0x34 |
| **I2C Clock** | N/A | Standard (100 kHz) or Fast (400 kHz) |
| **Event Buffer** | Immediate processing | 10-event FIFO in TCA8418 |

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:12-13](), high-level diagrams

---

## Compatibility Matrix

The library maintains full API compatibility across both hardware variants:

| Feature | M5Cardputer | M5Cardputer-ADV | Notes |
|---------|-------------|-----------------|-------|
| **All Keyboard_Class methods** | ✓ | ✓ | Identical API |
| **Character mapping** | ✓ | ✓ | Same key map |
| **Modifier keys** | ✓ | ✓ | Shift, Ctrl, Alt, Fn, Opt |
| **HID key codes** | ✓ | ✓ | USB HID standard |
| **Multi-key press** | ✓ | ✓ | Full N-key rollover |
| **Interrupt support** | — | ✓ | ADV only |
| **Power efficiency** | Standard | Improved | ADV uses hardware scanning |

**Sources:** High-level diagrams, architectural descriptions

---

## Development Considerations

When developing applications for the M5Cardputer library:

1. **Hardware Agnostic Code:** Write applications using the `Keyboard_Class` API without hardware-specific logic
2. **No Manual Detection:** Never manually detect board type; the library handles this automatically
3. **Update Call Required:** Both implementations require periodic `update()` calls, though ADV uses interrupts internally
4. **Initialization Order:** Always call `M5Cardputer.begin()` before accessing keyboard functionality

For detailed keyboard API documentation, see [Keyboard_Class API](#4.1). For information on implementing custom keyboard readers for new hardware, see [Creating Custom Keyboard Readers](#11.1).

**Sources:** High-level diagrams, architectural descriptions