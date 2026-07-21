M5Cardputer TCA8418 Implementation (M5Cardputer-ADV)

# TCA8418 Implementation (M5Cardputer-ADV)

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/utility/Keyboard/KeyboardReader/TCA8418.cpp](src/utility/Keyboard/KeyboardReader/TCA8418.cpp)
- [src/utility/Keyboard/KeyboardReader/TCA8418.h](src/utility/Keyboard/KeyboardReader/TCA8418.h)
- [src/utility/common.h](src/utility/common.h)

</details>



## Purpose and Scope

This document provides a detailed technical reference for the `TCA8418KeyboardReader` class, which implements keyboard input handling for the M5Cardputer-ADV hardware variant. The TCA8418KeyboardReader communicates with the TCA8418 I2C keyboard controller chip to scan a 7x8 key matrix, process interrupt-driven key events, and provide key state information through the unified `KeyboardReader` interface.

For the abstract keyboard interface and polymorphic hardware support, see [Hardware Abstraction Layer](#4.4). For the standard M5Cardputer GPIO-based implementation, see [IOMatrix Implementation (M5Cardputer)](#4.5). For high-level keyboard API usage, see [Keyboard_Class API](#4.1).

---

## Architecture Overview

The `TCA8418KeyboardReader` class provides an interrupt-driven implementation of the `KeyboardReader` interface, delegating physical key scanning to the TCA8418 I2C controller. This design offloads matrix scanning from the ESP32, reducing CPU load and enabling reliable key event detection.

### Class Structure

```mermaid
graph TB
    subgraph "TCA8418KeyboardReader Class"
        READER["TCA8418KeyboardReader<br/>KeyboardReader Implementation"]
        
        subgraph "Private Members"
            TCA["_tca8418<br/>unique_ptr&lt;Adafruit_TCA8418&gt;"]
            ISR_FLAG["_isr_flag<br/>volatile bool"]
            INT_PIN["_interrupt_pin<br/>int"]
            RAW_BUF["_key_event_raw_buffer<br/>KeyEventRaw_t"]
        end
        
        subgraph "Public Interface"
            CTOR["TCA8418KeyboardReader(int interrupt_pin)"]
            BEGIN["begin()"]
            UPDATE["update()"]
        end
        
        subgraph "Private Methods"
            ISR["gpio_isr_handler(void* arg)<br/>static IRAM_ATTR"]
            GET_RAW["get_key_event_raw(uint8_t eventRaw)<br/>KeyEventRaw_t"]
            REMAP["remap(KeyEventRaw_t& key)<br/>void"]
            UPDATE_LIST["update_key_list(KeyEventRaw_t& event)<br/>void"]
        end
    end
    
    subgraph "Dependencies"
        TCA_DRIVER["Adafruit_TCA8418<br/>I2C Driver"]
        BASE["KeyboardReader<br/>Abstract Interface"]
    end
    
    subgraph "Hardware"
        TCA_CHIP["TCA8418 Chip<br/>I2C Address 0x34"]
        INT_GPIO["GPIO 11<br/>Interrupt Pin"]
        MATRIX["7x8 Key Matrix"]
    end
    
    READER -->|inherits from| BASE
    READER -->|owns| TCA
    READER -->|owns| ISR_FLAG
    READER -->|owns| INT_PIN
    READER -->|owns| RAW_BUF
    
    BEGIN -->|creates| TCA
    TCA -->|wraps| TCA_DRIVER
    TCA_DRIVER -->|communicates via I2C| TCA_CHIP
    
    ISR -->|sets| ISR_FLAG
    INT_GPIO -->|triggers| ISR
    TCA_CHIP -->|asserts| INT_GPIO
    
    UPDATE -->|reads| ISR_FLAG
    UPDATE -->|calls| GET_RAW
    UPDATE -->|calls| REMAP
    UPDATE -->|calls| UPDATE_LIST
    
    TCA_CHIP -->|scans| MATRIX
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.h:1-41](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:1-122]()

---

## Initialization Process

The `begin()` method initializes the TCA8418 controller and configures interrupt handling. This method is called once during keyboard subsystem initialization.

### Initialization Sequence

```mermaid
sequenceDiagram
    participant APP as "Keyboard_Class"
    participant READER as "TCA8418KeyboardReader"
    participant TCA as "Adafruit_TCA8418"
    participant HW as "TCA8418 Hardware"
    participant GPIO as "ESP32 GPIO"
    
    APP->>READER: begin()
    READER->>READER: Create unique_ptr<Adafruit_TCA8418>
    READER->>TCA: begin()
    TCA->>HW: Initialize I2C communication
    HW-->>TCA: ACK (or NACK on failure)
    
    alt Initialization Failed
        TCA-->>READER: return false
        READER->>READER: Print error message
        READER-->>APP: return (no further action)
    end
    
    READER->>TCA: matrix(7, 8)
    TCA->>HW: Configure as 7 rows, 8 columns
    
    READER->>TCA: flush()
    TCA->>HW: Clear event FIFO
    
    READER->>GPIO: pinMode(_interrupt_pin, INPUT)
    READER->>GPIO: attachInterruptArg(..., gpio_isr_handler, this, CHANGE)
    GPIO-->>READER: Interrupt handler registered
    
    READER->>TCA: enableInterrupts()
    TCA->>HW: Set interrupt enable registers
    
    READER-->>APP: Initialization complete
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:28-50]()

### Initialization Steps

| Step | Method Call | Purpose |
|------|-------------|---------|
| 1 | `_tca8418 = std::make_unique<Adafruit_TCA8418>()` | Create driver instance using C++11-compatible make_unique |
| 2 | `_tca8418->begin()` | Initialize I2C communication at default address 0x34 |
| 3 | `_tca8418->matrix(7, 8)` | Configure TCA8418 for 7-row, 8-column matrix |
| 4 | `_tca8418->flush()` | Clear any stale events from FIFO |
| 5 | `pinMode(_interrupt_pin, INPUT)` | Configure GPIO 11 as input (default) |
| 6 | `attachInterruptArg(...)` | Attach ISR to detect interrupt pin changes |
| 7 | `_tca8418->enableInterrupts()` | Enable TCA8418 interrupt generation |

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:28-50](), [src/utility/common.h:15-19]()

### Default Hardware Configuration

The TCA8418KeyboardReader uses the following default configuration:

| Parameter | Value | Location |
|-----------|-------|----------|
| I2C Address | 0x34 | Adafruit_TCA8418 default |
| Interrupt Pin | GPIO 11 | [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:13]() |
| Matrix Size | 7 rows × 8 columns | [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:39]() |
| Interrupt Mode | CHANGE (both edges) | [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:45]() |

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:13-50]()

---

## Interrupt-Driven Event Handling

The TCA8418 controller uses hardware interrupts to signal key events, minimizing polling overhead and ensuring responsive key detection.

### Interrupt Service Routine

The `gpio_isr_handler` is a static method marked with `IRAM_ATTR` for fast execution from IRAM. It sets the `_isr_flag` volatile boolean to indicate a pending event.

```mermaid
graph LR
    subgraph "Hardware Layer"
        KEY["Key Press/Release"]
        TCA["TCA8418 Chip"]
        INT_PIN["GPIO 11"]
    end
    
    subgraph "ISR (IRAM)"
        ISR["gpio_isr_handler<br/>static void IRAM_ATTR"]
        FLAG["_isr_flag = true"]
    end
    
    subgraph "Main Loop"
        UPDATE["update() method"]
        CHECK["if (!_isr_flag) return"]
        PROCESS["Process event"]
    end
    
    KEY -->|"Detected by"| TCA
    TCA -->|"Asserts"| INT_PIN
    INT_PIN -->|"Triggers"| ISR
    ISR -->|"Sets"| FLAG
    UPDATE -->|"Checks"| CHECK
    CHECK -->|"If set"| PROCESS
    PROCESS -->|"Clears"| FLAG
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:22-26](), [src/utility/Keyboard/KeyboardReader/TCA8418.h:32-36]()

### Update Method Flow

The `update()` method processes pending key events when called from the main loop. It checks the interrupt flag, reads events, clears the interrupt, and updates the key list.

```mermaid
flowchart TD
    START["update() called"]
    CHECK_FLAG{"_isr_flag == true?"}
    RETURN_EARLY["return (no event)"]
    
    GET_EVENT["eventRaw = _tca8418->getEvent()"]
    PARSE["_key_event_raw_buffer = get_key_event_raw(eventRaw)"]
    
    CLEAR_INT["writeRegister8(TCA8418_REG_INT_STAT, 1)"]
    READ_INT["intstat = readRegister8(TCA8418_REG_INT_STAT)"]
    
    CHECK_CLEARED{"(intstat & 0x01) == 0?"}
    CLEAR_FLAG["_isr_flag = false"]
    KEEP_FLAG["Keep _isr_flag = true<br/>(more events pending)"]
    
    REMAP_COORDS["remap(_key_event_raw_buffer)"]
    UPDATE_LIST["update_key_list(_key_event_raw_buffer)"]
    
    END["return"]
    
    START --> CHECK_FLAG
    CHECK_FLAG -->|"false"| RETURN_EARLY
    CHECK_FLAG -->|"true"| GET_EVENT
    
    GET_EVENT --> PARSE
    PARSE --> CLEAR_INT
    CLEAR_INT --> READ_INT
    
    READ_INT --> CHECK_CLEARED
    CHECK_CLEARED -->|"yes, cleared"| CLEAR_FLAG
    CHECK_CLEARED -->|"no, still set"| KEEP_FLAG
    
    CLEAR_FLAG --> REMAP_COORDS
    KEEP_FLAG --> REMAP_COORDS
    
    REMAP_COORDS --> UPDATE_LIST
    UPDATE_LIST --> END
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:52-73]()

### Interrupt Flag Clearing Logic

The TCA8418 hardware maintains an interrupt status register (TCA8418_REG_INT_STAT). Writing 1 to this register attempts to clear the interrupt. However, if additional events remain in the FIFO, the interrupt bit remains set. This mechanism ensures no events are lost:

- If interrupt clears: `_isr_flag = false`, no more events to process
- If interrupt remains set: `_isr_flag = true`, more events pending, `update()` will be called again

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:60-66]()

---

## Raw Event Decoding

The TCA8418 controller reports key events as 8-bit values encoding the key state and matrix position.

### Event Format

The TCA8418 event byte format:

| Bit 7 | Bits 6-0 |
|-------|----------|
| State (1=press, 0=release) | Key code (1-based index into matrix) |

### Decoding Algorithm

The `get_key_event_raw()` method converts the raw byte into a `KeyEventRaw_t` structure:

```mermaid
graph LR
    subgraph "Input"
        RAW["eventRaw<br/>uint8_t"]
    end
    
    subgraph "Extraction"
        STATE["state = eventRaw & 0x80<br/>(bit 7)"]
        KEYCODE["buffer = eventRaw & 0x7F<br/>(bits 0-6)"]
        SUBTRACT["buffer = buffer - 1<br/>(convert to 0-based)"]
    end
    
    subgraph "Position Calculation"
        ROW_CALC["row = buffer / 10"]
        COL_CALC["col = buffer % 10"]
    end
    
    subgraph "Output"
        OUT["KeyEventRaw_t{<br/>state, row, col<br/>}"]
    end
    
    RAW --> STATE
    RAW --> KEYCODE
    KEYCODE --> SUBTRACT
    SUBTRACT --> ROW_CALC
    SUBTRACT --> COL_CALC
    
    STATE --> OUT
    ROW_CALC --> OUT
    COL_CALC --> OUT
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:75-85]()

### Example Decode

For a key press at TCA8418 matrix position (3, 5):

```
TCA8418 Key Code = (3 * 10) + 5 + 1 = 36
Event Byte = 0x80 | 36 = 0xA4 (164 decimal)

Decoding:
  state = 0xA4 & 0x80 = 0x80 (true, pressed)
  buffer = 0xA4 & 0x7F = 0x24 (36)
  buffer = 36 - 1 = 35
  row = 35 / 10 = 3
  col = 35 % 10 = 5
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:75-85]()

---

## Coordinate Remapping

The TCA8418 chip's 7×8 matrix layout differs from the standard M5Cardputer's 4×14 logical layout. The `remap()` method transforms TCA8418 coordinates to match the standard layout, ensuring consistent key mapping across hardware variants.

### Remapping Algorithm

```mermaid
graph TB
    subgraph "Input: TCA8418 Coordinates"
        IN_ROW["key.row (0-6)"]
        IN_COL["key.col (0-7)"]
    end
    
    subgraph "Column Transformation"
        COL_CALC1["col = key.row * 2"]
        COL_CALC2{"key.col > 3?"}
        COL_INC["col++"]
        COL_FINAL["new col"]
    end
    
    subgraph "Row Transformation"
        ROW_CALC["row = (key.col + 4) % 4"]
        ROW_FINAL["new row"]
    end
    
    subgraph "Output: Standard Coordinates"
        OUT_ROW["key.row (remapped)"]
        OUT_COL["key.col (remapped)"]
    end
    
    IN_ROW --> COL_CALC1
    COL_CALC1 --> COL_CALC2
    COL_CALC2 -->|"yes"| COL_INC
    COL_CALC2 -->|"no"| COL_FINAL
    COL_INC --> COL_FINAL
    
    IN_COL --> ROW_CALC
    ROW_CALC --> ROW_FINAL
    
    COL_FINAL --> OUT_COL
    ROW_FINAL --> OUT_ROW
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:88-101]()

### Transformation Rules

The remapping logic implements two transformations:

**Column Mapping:**
```
new_col = old_row * 2 + (old_col > 3 ? 1 : 0)
```

This effectively splits the 7 TCA rows into 14 columns by doubling the row index and adding an offset based on the original column position.

**Row Mapping:**
```
new_row = (old_col + 4) % 4
```

This wraps the 8 TCA columns into 4 rows using modulo arithmetic with a 4-position offset.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:88-101]()

### Mapping Table Example

Sample coordinate transformations:

| TCA Row | TCA Col | New Row | New Col | Formula Verification |
|---------|---------|---------|---------|---------------------|
| 0 | 0 | 0 | 0 | col = 0*2 + 0 = 0, row = (0+4)%4 = 0 |
| 0 | 4 | 0 | 1 | col = 0*2 + 1 = 1, row = (4+4)%4 = 0 |
| 1 | 0 | 0 | 2 | col = 1*2 + 0 = 2, row = (0+4)%4 = 0 |
| 2 | 3 | 3 | 4 | col = 2*2 + 0 = 4, row = (3+4)%4 = 3 |
| 6 | 7 | 3 | 13 | col = 6*2 + 1 = 13, row = (7+4)%4 = 3 |

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:88-101]()

---

## Key List Management

The `update_key_list()` method maintains `_key_list`, a vector of currently pressed keys inherited from the `KeyboardReader` base class. This list is used by `Keyboard_Class` to determine active keys.

### Key List Update Logic

```mermaid
flowchart TD
    START["update_key_list(eventRaw)"]
    
    CONVERT["point.x = eventRaw.col<br/>point.y = eventRaw.row"]
    
    CHECK_STATE{"eventRaw.state?"}
    
    subgraph "Press Event"
        FIND_PRESS["it = find(_key_list, point)"]
        CHECK_EXIST_PRESS{"it == end()?"}
        ADD["_key_list.push_back(point)"]
    end
    
    subgraph "Release Event"
        FIND_RELEASE["it = find(_key_list, point)"]
        CHECK_EXIST_RELEASE{"it != end()?"}
        REMOVE["_key_list.erase(it)"]
    end
    
    END["return"]
    
    START --> CONVERT
    CONVERT --> CHECK_STATE
    
    CHECK_STATE -->|"true (press)"| FIND_PRESS
    FIND_PRESS --> CHECK_EXIST_PRESS
    CHECK_EXIST_PRESS -->|"yes, not in list"| ADD
    CHECK_EXIST_PRESS -->|"no, already present"| END
    ADD --> END
    
    CHECK_STATE -->|"false (release)"| FIND_RELEASE
    FIND_RELEASE --> CHECK_EXIST_RELEASE
    CHECK_EXIST_RELEASE -->|"yes, in list"| REMOVE
    CHECK_EXIST_RELEASE -->|"no, not present"| END
    REMOVE --> END
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:103-121]()

### Duplicate Key Handling

The method uses `std::find` to check for duplicate entries before adding or removing keys:

- **On press:** Only add the key if it's not already in the list (prevents duplicates from repeated events)
- **On release:** Only remove the key if it's present in the list (prevents errors from spurious release events)

This defensive approach ensures `_key_list` accurately reflects the current pressed keys without corruption from event anomalies.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:103-121]()

---

## Data Structures

### KeyEventRaw_t Structure

The `KeyEventRaw_t` private structure encapsulates a single key event:

```cpp
struct KeyEventRaw_t {
    bool state;      // true = pressed, false = released
    uint8_t row;     // Row coordinate (after decoding, before remapping)
    uint8_t col;     // Column coordinate (after decoding, before remapping)
};
```

This structure is used internally as an intermediate representation between the TCA8418's raw byte format and the final `Point2D_t` coordinates stored in `_key_list`.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.h:25-29]()

---

## Interrupt Pin Configuration

### Constructor Behavior

The `TCA8418KeyboardReader` constructor accepts an optional `interrupt_pin` parameter:

```cpp
TCA8418KeyboardReader(int interrupt_pin = -1)
```

- If `interrupt_pin` is negative (default -1), the constructor sets `_interrupt_pin` to `DEFAULT_TCA8418_INT_PIN` (GPIO 11)
- If a non-negative pin is provided, that pin is used instead

This allows hardware flexibility while providing a sensible default for the M5Cardputer-ADV board.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:15-20](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:13]()

### Interrupt Edge Detection

The interrupt is configured to trigger on `CHANGE` (both rising and falling edges):

```cpp
attachInterruptArg(digitalPinToInterrupt(_interrupt_pin), gpio_isr_handler, this, CHANGE);
```

This ensures the ISR captures both the assertion and de-assertion of the TCA8418 interrupt signal, providing maximum responsiveness.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:45]()

---

## Complete Event Processing Pipeline

The following diagram shows the complete flow from hardware key press to application-accessible key state:

```mermaid
sequenceDiagram
    participant User as "Physical Key"
    participant TCA as "TCA8418 Chip"
    participant GPIO as "GPIO 11"
    participant ISR as "gpio_isr_handler"
    participant Update as "update()"
    participant Parse as "get_key_event_raw()"
    participant Remap as "remap()"
    participant List as "update_key_list()"
    participant App as "Keyboard_Class"
    
    User->>TCA: Key press detected
    TCA->>TCA: Store event in FIFO
    TCA->>GPIO: Assert interrupt
    GPIO->>ISR: Trigger interrupt
    ISR->>ISR: Set _isr_flag = true
    
    Note over Update: Main loop calls update()
    
    Update->>Update: Check _isr_flag
    Update->>TCA: getEvent()
    TCA-->>Update: eventRaw (uint8_t)
    
    Update->>Parse: get_key_event_raw(eventRaw)
    Parse->>Parse: Extract state bit
    Parse->>Parse: Extract key code
    Parse->>Parse: Calculate row/col
    Parse-->>Update: KeyEventRaw_t
    
    Update->>TCA: Clear INT_STAT register
    Update->>TCA: Read INT_STAT register
    TCA-->>Update: intstat value
    Update->>Update: Clear _isr_flag if no more events
    
    Update->>Remap: remap(KeyEventRaw_t)
    Remap->>Remap: Transform col = row*2 + offset
    Remap->>Remap: Transform row = (col+4)%4
    Remap-->>Update: Remapped coordinates
    
    Update->>List: update_key_list(KeyEventRaw_t)
    List->>List: Convert to Point2D_t
    List->>List: Add to or remove from _key_list
    
    Note over App: Later, application queries state
    App->>List: Access _key_list
    List-->>App: Vector of pressed keys
```

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:52-73](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:75-85](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:88-101](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:103-121]()

---

## Comparison with IOMatrix Implementation

The `TCA8418KeyboardReader` differs significantly from the GPIO-based `IOMatrixKeyboardReader`:

| Aspect | TCA8418KeyboardReader | IOMatrixKeyboardReader |
|--------|----------------------|------------------------|
| **Hardware Interface** | I2C communication with TCA8418 chip | Direct GPIO matrix scanning |
| **Matrix Size** | 7 rows × 8 columns (hardware) | 3 output pins × 7 input pins (8×7 logical) |
| **Event Detection** | Interrupt-driven (hardware FIFO) | Polling-based (manual scanning) |
| **CPU Overhead** | Low (only processes on interrupt) | Higher (continuous polling in update()) |
| **Pin Requirements** | 2 pins (SDA, SCL) + 1 interrupt pin | 10 pins (3 output + 7 input) |
| **Event Buffering** | Hardware FIFO in TCA8418 | None (immediate processing) |
| **Coordinate Remapping** | Complex (7×8 → 4×14) | Simpler (8×7 → 4×14) |
| **Initialization** | Requires I2C device init | Direct GPIO configuration |

The TCA8418 implementation trades hardware complexity for reduced CPU load and pin count, making it suitable for advanced variants where GPIO pins are scarce or other processing demands require efficient keyboard handling.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:1-122](), [src/utility/Keyboard/KeyboardReader/TCA8418.h:1-41]()

---

## Key Implementation Details

### C++11 Compatibility

The code uses `std::make_unique` for smart pointer creation, with a custom implementation for C++11 compatibility defined in [src/utility/common.h:15-19](). This ensures the code works with older toolchains while using modern C++ idioms.

**Sources:** [src/utility/common.h:1-34](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:31]()

### IRAM Attribute

The ISR is marked with `IRAM_ATTR`, which places the function in IRAM (instruction RAM) rather than flash memory. This ensures fast interrupt response times without flash access latency.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:22](), [src/utility/Keyboard/KeyboardReader/TCA8418.h:36]()

### Volatile Flag

The `_isr_flag` member is marked `volatile` to prevent compiler optimization issues. This ensures the main loop always reads the current value set by the ISR, preventing race conditions.

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.h:32]()

---

## Error Handling

The implementation includes minimal error handling:

- **Initialization failure:** If `_tca8418->begin()` returns false, an error message is printed to serial, and the method returns early
- **No exception handling:** The code follows Arduino/embedded conventions, avoiding exceptions
- **Silent failures:** After initialization failure, subsequent `update()` calls will do nothing (null pointer check not shown but implicitly handled by early return)

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:33-35]()

---

## Usage Example

While application code typically uses the high-level `Keyboard_Class` API, the `TCA8418KeyboardReader` is instantiated and used like this:

```cpp
// During Keyboard_Class initialization
if (M5.getBoard() == board_M5CardputerADV) {
    _reader = new TCA8418KeyboardReader();  // Uses default GPIO 11
    _reader->begin();
}

// In main loop (called by Keyboard_Class::update())
_reader->update();  // Processes interrupt-driven events

// Key list is available via _reader->_key_list (protected member)
```

For complete keyboard API usage, see [Keyboard_Class API](#4.1).

**Sources:** [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:15-50](), [src/utility/Keyboard/KeyboardReader/TCA8418.cpp:52-73]()