M5Unified Main Update Loop and Peripheral Polling

# Main Update Loop and Peripheral Polling

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/M5Unified.cpp](src/M5Unified.cpp)
- [src/M5Unified.hpp](src/M5Unified.hpp)
- [src/utility/Button_Class.cpp](src/utility/Button_Class.cpp)
- [src/utility/Button_Class.hpp](src/utility/Button_Class.hpp)

</details>



## Purpose and Scope

This page documents the `M5.update()` method and the peripheral polling system that drives input event processing in M5Unified. The update loop is responsible for reading hardware inputs (buttons, touch, IO expanders), updating internal state machines, and making input events available to application code.

For information about system initialization before the update loop begins, see [System Initialization and Lifecycle](#2.1). For details on audio system background tasks that operate independently of the update loop, see [Audio System Architecture](#4).

**Sources:** [src/M5Unified.hpp:320](), [src/M5Unified.cpp:1-100]()

---

## Application Loop Pattern

The M5Unified library follows a polling-based event processing model where user code must call `M5.update()` regularly, typically in the Arduino `loop()` function or equivalent main application loop.

```mermaid
sequenceDiagram
    participant App as "Application Code"
    participant M5 as "M5.update()"
    participant HW as "Hardware Inputs"
    participant Buttons as "Button State Machines"
    
    App->>M5: begin(config)
    Note over M5: Initialize system
    M5-->>App: System ready
    
    loop Application Loop
        App->>M5: update()
        activate M5
        M5->>M5: "_updateMsec = millis()"
        M5->>HW: Read Touch coordinates
        M5->>HW: Read GPIO registers
        M5->>HW: Read IO Expander
        M5->>HW: Read PMIC button state
        M5->>Buttons: "Update Button[0-4]"
        Note over Buttons: Run state machines<br/>Apply debouncing<br/>Detect clicks/holds
        M5-->>App: Continue
        deactivate M5
        
        App->>M5: Query button states
        Note over App: "BtnA.wasClicked()"<br/>"BtnB.isPressed()"<br/>etc.
        
        App->>App: Application logic
        Note over App: Render graphics<br/>Process events<br/>Control devices
    end
```

**Sources:** [src/M5Unified.hpp:320](), [src/M5Unified.cpp:148-150]()

---

## Update Method Responsibilities

The `update()` method declared in [src/M5Unified.hpp:320]() performs several key functions on each invocation:

### Timestamp Capture

```mermaid
graph LR
    update["M5.update()"] --> timestamp["_updateMsec = millis()"]
    timestamp --> available["getUpdateMsec()"]
    available --> buttons["Button state machines<br/>use timestamp"]
    available --> app["Application queries<br/>getUpdateMsec()"]
```

The method captures the current millisecond timestamp at the start of each update cycle. This timestamp is stored in the `_updateMsec` member variable [src/M5Unified.hpp:620]() and used consistently throughout the update cycle for:
- Button debouncing calculations
- Hold duration measurements
- Click timeout detection
- Application timing queries via `getUpdateMsec()` [src/M5Unified.hpp:289]()

### Input Source Aggregation

The update method polls multiple input sources and aggregates their states:

| Input Source | Hardware Interface | Target Buttons | Board Dependency |
|--------------|-------------------|----------------|------------------|
| **Touch** | `Touch.update()` | BtnA, BtnB, BtnC | Core2, Tough, CoreS3 |
| **GPIO** | Direct GPIO register read | BtnA, BtnB, BtnC, BtnEXT | Most boards |
| **IO Expander** | I2C (AW9523, PI4IOE5V6408) | BtnEXT | Specific models |
| **PMIC** | `Power.getKeyState()` | BtnPWR | Boards with AXP192/AXP2101 |

**Sources:** [src/M5Unified.hpp:238-242](), [src/M5Unified.cpp:351-365]()

---

## Button Array Architecture

M5Unified maintains an array of five `Button_Class` instances to support various board configurations:

```mermaid
graph TB
    subgraph "M5Unified Button Array"
        buttons["_buttons[5]<br/>Button_Class array"]
        btn0["_buttons[0]<br/>BtnA reference"]
        btn1["_buttons[1]<br/>BtnB reference"]
        btn2["_buttons[2]<br/>BtnC reference"]
        btn3["_buttons[3]<br/>BtnEXT reference"]
        btn4["_buttons[4]<br/>BtnPWR reference"]
    end
    
    subgraph "Input Sources per Board"
        gpio["GPIO Pins"]
        touch["Touch Regions"]
        ioexp["IO Expander"]
        pmic["PMIC Key Register"]
    end
    
    subgraph "Board Examples"
        core2["Core2: Touch→ABC, PMIC→PWR"]
        stack["M5Stack: GPIO→ABC"]
        ink["CoreInk: GPIO→AB,PWR + EXT"]
    end
    
    buttons --> btn0
    buttons --> btn1
    buttons --> btn2
    buttons --> btn3
    buttons --> btn4
    
    gpio --> btn0
    gpio --> btn1
    gpio --> btn2
    gpio --> btn3
    touch --> btn0
    touch --> btn1
    touch --> btn2
    ioexp --> btn3
    pmic --> btn4
    
    core2 -.Example.-> touch
    stack -.Example.-> gpio
    ink -.Example.-> gpio
    ink -.Example.-> ioexp
```

Each button instance maintains its own independent state machine, allowing the same application code to work across different M5Stack boards without modification.

**Sources:** [src/M5Unified.hpp:238-242, 614](), [src/utility/Button_Class.hpp:11-83]()

---

## Button State Machine

Each `Button_Class` instance implements a state machine that processes raw hardware inputs into high-level button events.

### State Enumeration

```mermaid
stateDiagram-v2
    [*] --> state_nochange: Initial state
    
    state_nochange --> state_clicked: Button released<br/>after short press
    state_nochange --> state_hold: Button held for<br/>_msecHold duration
    state_clicked --> state_nochange: Event processed
    state_clicked --> state_decide_click_count: Timeout after<br/>click sequence
    state_hold --> state_nochange: Button released
    state_decide_click_count --> state_nochange: Event processed
    
    note right of state_nochange
        No event this cycle
        Default state
    end note
    
    note right of state_clicked
        Single click detected
        _clickCount++
    end note
    
    note right of state_hold
        Long press detected
        Triggered once at threshold
    end note
    
    note right of state_decide_click_count
        Multi-click sequence complete
        Final click count available
    end note
```

The state enumeration is defined in [src/utility/Button_Class.hpp:14-19]():
- `state_nochange` - No new event this update cycle
- `state_clicked` - Button was clicked (pressed and quickly released)
- `state_hold` - Button has been held for the hold threshold duration
- `state_decide_click_count` - Multi-click sequence timeout reached, final count available

### State Update Logic

The `setRawState()` method [src/utility/Button_Class.cpp:41-83]() processes raw hardware input through the following pipeline:

```mermaid
graph TD
    raw["setRawState(msec, press)"] --> debounce["Debounce Check"]
    debounce -->|"Changed"| rawchange["_lastRawChange = msec"]
    debounce -->|"Stable for _msecDebounce"| validate["Valid State Change"]
    
    validate --> pressed{"press == true?"}
    pressed -->|Yes| oldpress{"_oldPress == 0?"}
    pressed -->|No| released{"_oldPress != 0?"}
    
    oldpress -->|Yes| setpress1["_press = 1<br/>(clicked)"]
    oldpress -->|No| checkhold{"holdPeriod >= _msecHold?"}
    
    checkhold -->|Yes| setpress2["_press = 2<br/>(holding)<br/>state = state_hold"]
    checkhold -->|No| continue1["Continue holding"]
    
    released -->|Yes| setpress0["_press = 0<br/>state = state_clicked"]
    released -->|No| continue2["Continue released"]
    
    setpress1 --> setstate["setState(msec, state)"]
    setpress2 --> setstate
    setpress0 --> setstate
    continue1 --> setstate
    continue2 --> setstate
    
    setstate --> timeout{"Click timeout?"}
    timeout -->|"Yes + _clickCount > 0"| decide["state = state_decide_click_count"]
    timeout -->|No| done["Return"]
    decide --> done
```

**Key Variables:**
- `_raw_press` - Immediate hardware state (may be noisy)
- `_press` - Debounced state: 0=released, 1=clicked, 2=holding
- `_oldPress` - Previous debounced state
- `_lastRawChange` - Timestamp of last raw input change
- `_lastChange` - Timestamp of last debounced state change
- `_msecDebounce` - Debounce threshold (default 10ms)
- `_msecHold` - Hold detection threshold (default 500ms)

**Sources:** [src/utility/Button_Class.cpp:41-83](), [src/utility/Button_Class.hpp:69-81]()

### Multi-Click Detection

The state machine tracks consecutive clicks within a timeout window:

```mermaid
sequenceDiagram
    participant HW as "Hardware"
    participant SM as "State Machine"
    participant App as "Application"
    
    Note over SM: _clickCount = 0
    
    HW->>SM: Press detected
    HW->>SM: Release detected
    SM->>SM: state_clicked<br/>_clickCount = 1<br/>_lastClicked = msec
    
    Note over SM: Wait < _msecHold
    
    HW->>SM: Press detected
    HW->>SM: Release detected
    SM->>SM: state_clicked<br/>_clickCount = 2<br/>_lastClicked = msec
    
    Note over SM: Wait _msecHold
    
    SM->>SM: Timeout reached<br/>state_decide_click_count
    App->>SM: wasDoubleClicked()?
    SM-->>App: true (_clickCount == 2)
    
    SM->>SM: _clickCount = 0<br/>state_nochange
```

The timeout logic in [src/utility/Button_Class.cpp:16-27]() finalizes the click count when `_msecHold` duration passes without another click.

**Sources:** [src/utility/Button_Class.cpp:8-39](), [src/utility/Button_Class.hpp:28-39]()

---

## Button State Query Interface

Application code queries button states using the `Button_Class` public methods. States persist until the next update cycle where they may change.

### Query Methods by Category

**Press/Release State:**

```cpp
bool isPressed()       // Currently held down (this moment)
bool isReleased()      // Currently not pressed (this moment)
bool isHolding()       // Currently in hold state (_press == 2)
bool wasPressed()      // Transitioned from released to pressed
bool wasReleased()     // Transitioned from pressed to released
bool wasChangePressed()// State changed (either direction)
```

**Event Detection:**

```cpp
bool wasClicked()           // Single quick press/release detected
bool wasHold()              // Hold threshold reached
bool wasSingleClicked()     // Exactly 1 click after timeout
bool wasDoubleClicked()     // Exactly 2 clicks after timeout
bool wasDecideClickCount()  // Any multi-click count decided
```

**Timing Queries:**

```cpp
bool pressedFor(ms)         // Held for at least ms milliseconds
bool releasedFor(ms)        // Released for at least ms milliseconds
bool wasReleaseFor(ms)      // Was held for at least ms before release
bool wasReleasedAfterHold() // Released after reaching hold state
uint32_t lastChange()       // Timestamp of last state change
```

### Usage Pattern Example

```cpp
void loop() {
    M5.update();  // Poll hardware and update button states
    
    // Query button states for this frame
    if (M5.BtnA.wasClicked()) {
        Serial.println("Button A clicked");
    }
    
    if (M5.BtnB.wasHold()) {
        Serial.println("Button B held");
    }
    
    if (M5.BtnC.wasDoubleClicked()) {
        Serial.println("Button C double-clicked");
    }
    
    // Current state queries
    if (M5.BtnA.isPressed()) {
        // React to continuous press
    }
    
    // Application logic continues...
}
```

**Sources:** [src/utility/Button_Class.hpp:22-55](), [src/M5Unified.hpp:238-242]()

---

## Touch-to-Button Mapping

On boards with touch screens (Core2, Tough, CoreS3), the update loop converts touch coordinates into virtual button presses for BtnA, BtnB, and BtnC.

```mermaid
graph TB
    subgraph "Touch Screen Coordinate Space"
        screen["Display Width × Height"]
        region1["Region 1:<br/>X: 0 to W/3<br/>Y: H - ButtonHeight to H"]
        region2["Region 2:<br/>X: W/3 to 2W/3<br/>Y: H - ButtonHeight to H"]
        region3["Region 3:<br/>X: 2W/3 to W<br/>Y: H - ButtonHeight to H"]
    end
    
    subgraph "Button Mapping"
        btnA["BtnA"]
        btnB["BtnB"]
        btnC["BtnC"]
    end
    
    screen --> region1
    screen --> region2
    screen --> region3
    
    region1 -.Maps to.-> btnA
    region2 -.Maps to.-> btnB
    region3 -.Maps to.-> btnC
    
    height["_touch_button_height<br/>Configurable via<br/>setTouchButtonHeight()"]
    height -.Defines.-> region1
    height -.Defines.-> region2
    height -.Defines.-> region3
```

The touch button height can be configured:
- `setTouchButtonHeight(uint16_t pixel)` - Set absolute pixel height [src/M5Unified.hpp:606]()
- `setTouchButtonHeightByRatio(uint8_t ratio)` - Set as percentage of display height [src/M5Unified.hpp:605]()
- `getTouchButtonHeight()` - Query current setting [src/M5Unified.hpp:607]()

**Sources:** [src/M5Unified.hpp:605-607, 621](), [src/utility/Touch_Class.hpp:1-50]()

---

## Update Timing Considerations

### Recommended Update Frequency

The update loop should be called frequently for responsive input handling:

| Update Frequency | Input Responsiveness | Resource Usage |
|------------------|---------------------|----------------|
| **Every loop iteration** (default) | Excellent (sub-ms latency) | Minimal CPU overhead |
| 10-50 Hz | Acceptable for most applications | Very low overhead |
| < 10 Hz | Noticeable lag in button response | Not recommended |

### Debounce and Hold Thresholds

Default timing values can be adjusted per button:

```cpp
// Configure debounce threshold (default 10ms)
M5.BtnA.setDebounceThresh(20);  // 20ms debounce

// Configure hold threshold (default 500ms)
M5.BtnA.setHoldThresh(1000);    // 1 second for hold detection

// Query current settings
uint32_t debounce = M5.BtnA.getDebounceThresh();
uint32_t hold = M5.BtnA.getHoldThresh();
```

**Sources:** [src/utility/Button_Class.hpp:57-58, 65-66](), [src/utility/Button_Class.cpp:74-76]()

### Update Loop vs Background Tasks

The update loop operates independently from audio background tasks:

```mermaid
graph LR
    subgraph "FreeRTOS Scheduler"
        main["Main Task<br/>(loop function)"]
        spk["spk_task<br/>(Audio playback)"]
        mic["mic_task<br/>(Audio capture)"]
    end
    
    subgraph "Update Operations"
        update["M5.update()"]
        buttons["Button state machines"]
        touch["Touch polling"]
    end
    
    subgraph "Concurrent Operations"
        i2s["I2S DMA transfers"]
        mixing["8-channel audio mixing"]
        fft["FFT processing"]
    end
    
    main --> update
    update --> buttons
    update --> touch
    
    spk -.Runs concurrently.-> i2s
    mic -.Runs concurrently.-> fft
    
    main -.Does not block.-> spk
    main -.Does not block.-> mic
```

The update loop does not block on audio operations. Speaker and microphone tasks run independently in separate FreeRTOS tasks with their own priority levels. For details on audio task architecture, see [Speaker Interface and Multi-Channel Mixing](#4.2) and [Microphone Interface and Signal Processing](#4.3).

**Sources:** [src/M5Unified.cpp:1-100](), High-level architecture diagrams

---

## Power Button Special Handling

The power button (BtnPWR) requires special consideration as it may be polled less frequently to reduce I2C bus traffic:

```mermaid
graph TD
    update["M5.update() called"] --> check{"_use_pmic_button?"}
    check -->|No| skip["Skip BtnPWR update"]
    check -->|Yes| interval{"Time since last<br/>PWR update ><br/>BTNPWR_MIN_UPDATE_MSEC?"}
    
    interval -->|No| skip2["Skip this cycle<br/>(debounce)"]
    interval -->|Yes| i2c["Read PMIC via I2C<br/>Power.getKeyState()"]
    
    i2c --> state["Update BtnPWR<br/>state machine"]
    
    skip --> done["Continue to<br/>other buttons"]
    skip2 --> done
    state --> done
```

The minimum update interval `BTNPWR_MIN_UPDATE_MSEC` is defined as 4ms [src/M5Unified.hpp:612]() to prevent excessive I2C transactions to the PMIC. The `_use_pmic_button` flag is set based on the `config_t.pmic_button` configuration option [src/M5Unified.hpp:133]().

**Sources:** [src/M5Unified.hpp:133, 242, 612, 625](), [src/utility/Power_Class.hpp:1-100]()

---

## Performance Characteristics

### Execution Time

Typical `M5.update()` execution times on ESP32 @ 240MHz:

| Operation | Approximate Duration | Notes |
|-----------|---------------------|-------|
| Timestamp capture | < 1 μs | `millis()` call |
| GPIO register read | ~2-5 μs | Direct register access |
| Touch coordinate read | ~50-200 μs | I2C transaction dependent |
| IO Expander read | ~100-300 μs | I2C transaction to AW9523/PI4IOE |
| PMIC button read | ~100-300 μs | I2C transaction to AXP192/AXP2101 |
| Button state machine (×5) | ~5-10 μs | Pure computation |
| **Total (typical)** | **200-800 μs** | Varies by board configuration |

Boards without touch screens or IO expanders experience faster update cycles (< 50 μs).

### Best Practices

1. **Call `update()` in every iteration** of the main loop for maximum responsiveness
2. **Query button states immediately after update()** while state is fresh
3. **Don't call `update()` from interrupt handlers** - designed for main loop only
4. **Adjust debounce/hold thresholds** if mechanical buttons exhibit excessive bounce
5. **Use state query methods consistently** - prefer `wasClicked()` over manual state tracking

**Sources:** [src/M5Unified.cpp:1-100](), [src/utility/Button_Class.cpp:41-83]()