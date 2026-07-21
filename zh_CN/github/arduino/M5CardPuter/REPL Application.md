M5Cardputer REPL Application

# REPL Application

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/UI/REPL/REPL.ino](examples/UI/REPL/REPL.ino)
- [examples/UI/REPL/ReplView.cpp](examples/UI/REPL/ReplView.cpp)
- [examples/UI/REPL/ReplView.h](examples/UI/REPL/ReplView.h)

</details>



## Purpose and Scope

The REPL (Read-Eval-Print Loop) application demonstrates how to build an interactive command-line interface on the M5Cardputer using the `ReplView` class. This example implements a number-guessing game to showcase text input handling, cursor management, message display, and callback-based application architecture. The REPL pattern is widely applicable for debugging tools, configuration interfaces, and interactive applications requiring text-based command entry.

For general keyboard input patterns beyond REPL interfaces, see [Keyboard Input Examples](#9.2). For display system fundamentals, see [Display System](#5). For keyboard API reference, see [Keyboard_Class API](#4.1).

**Sources:** [examples/UI/REPL/REPL.ino:1-88](), [examples/UI/REPL/ReplView.h:1-52]()

---

## Architecture Overview

The REPL application follows a Model-View-Controller pattern with clear separation between UI rendering (`ReplView`) and application logic (in `REPL.ino`). The architecture uses callback functions to decouple the view from game-specific behavior.

```mermaid
graph TB
    subgraph "Application Layer (REPL.ino)"
        MAIN["loop() / setup()"]
        STATE["Game State<br/>the_number<br/>is_player_win"]
        HANDLER["handle_command()"]
        VALIDATOR["string_to_number()"]
        TIP_CB["onRenderTips callback"]
    end
    
    subgraph "View Layer (ReplView)"
        VIEW["ReplView instance"]
        CANVAS["LGFX_Sprite* _canvas"]
        UPDATE["update()"]
        RENDER["render_prompt()<br/>render_interface()"]
        KB_INPUT["update_keyboard_input()"]
        CURSOR["update_cursor()"]
    end
    
    subgraph "M5Cardputer Hardware"
        KB["M5Cardputer.Keyboard"]
        DISP["M5Cardputer.Display"]
    end
    
    MAIN -->|"M5Cardputer.update()"| KB
    MAIN -->|"repl_view.update()"| UPDATE
    
    UPDATE --> KB_INPUT
    UPDATE --> CURSOR
    
    KB_INPUT -->|"isChange()<br/>isPressed()<br/>keysState()"| KB
    KB_INPUT -->|"on enter"| HANDLER
    
    HANDLER --> VALIDATOR
    HANDLER --> STATE
    HANDLER -->|"showMessage()"| VIEW
    
    VIEW -->|onCommand| HANDLER
    VIEW -->|onRenderTips| TIP_CB
    
    RENDER --> CANVAS
    CANVAS -->|"pushSprite()"| DISP
    
    CURSOR --> RENDER
    KB_INPUT --> RENDER
```

**Component Responsibilities:**

| Component | File | Responsibility |
|-----------|------|----------------|
| `ReplView` | [ReplView.h:15-51]() | UI rendering, keyboard input processing, cursor animation |
| `LGFX_Sprite* canvas` | [REPL.ino:9]() | Double-buffered rendering surface for flicker-free display |
| `handle_command()` | [REPL.ino:35-59]() | Game logic: input validation, number comparison, win condition |
| `string_to_number()` | [REPL.ino:14-33]() | Input validation and range checking (-999 to 999) |
| `onRenderTips` callback | [REPL.ino:71-75]() | Renders application-specific instructions at startup |
| `onCommand` callback | [REPL.ino:70]() | Invoked when user presses Enter with non-empty input |

**Sources:** [examples/UI/REPL/REPL.ino:1-88](), [examples/UI/REPL/ReplView.h:15-51](), [examples/UI/REPL/ReplView.cpp:8-167]()

---

## ReplView Class Design

The `ReplView` class provides a reusable REPL interface with configurable behavior through callbacks. It manages the complete input-display lifecycle without imposing specific command handling logic.

### Class Interface

```mermaid
classDiagram
    class ReplView {
        +function~void()~ onRenderTips
        +function~void(string)~ onCommand
        +bool autoClearPrompt
        
        +init(LGFX_Sprite* canvas)
        +update()
        +clearScreen()
        +showMessage(string message, uint16_t color)
        +showPrompt(string prompt_text)
        +setPromptText(string prompt)
        +setInputBuffer(string text)
        +getInputBuffer() string
        +clearInputBuffer()
        
        -LGFX_Sprite* _canvas
        -uint32_t _cursor_update_time
        -bool _cursor_state
        -string _input_buffer
        -string _prompt_text
        -int _key_event_slot_id
        
        -render_interface()
        -render_prompt()
        -handle_enter_key()
        -handle_backspace()
        -update_cursor()
        -update_keyboard_input()
    }
```

### Public Configuration

| Member | Type | Default | Purpose |
|--------|------|---------|---------|
| `onRenderTips` | `std::function<void()>` | nullptr | Called during `render_interface()` to display application-specific instructions |
| `onCommand` | `std::function<void(const std::string&)>` | nullptr | Called when Enter is pressed with non-empty input buffer |
| `autoClearPrompt` | `bool` | true | If true, clears `_input_buffer` after Enter; if false, preserves input for inspection |

**Sources:** [examples/UI/REPL/ReplView.h:17-19]()

### Initialization Sequence

```mermaid
sequenceDiagram
    participant App as REPL.ino::setup()
    participant M5 as M5Cardputer
    participant Canvas as LGFX_Sprite
    participant View as ReplView
    
    App->>M5: begin()
    App->>Canvas: new LGFX_Sprite(&Display)
    App->>Canvas: createSprite(width, height)
    App->>View: onCommand = handle_command
    App->>View: onRenderTips = lambda
    App->>View: init(canvas)
    View->>View: render_interface()
    View->>Canvas: fillScreen(TFT_BLACK)
    View->>Canvas: setFont(&fonts::efontCN_16)
    View->>Canvas: setTextScroll(true)
    View->>View: onRenderTips()
    View->>View: render_prompt()
    View->>Canvas: pushSprite(0, 0)
```

**Sources:** [examples/UI/REPL/REPL.ino:61-80](), [examples/UI/REPL/ReplView.cpp:8-73]()

---

## Update Loop Architecture

The REPL application uses a polling-based update loop that processes keyboard events and manages cursor animation on every iteration.

```mermaid
graph LR
    subgraph "Arduino loop()"
        LOOP_START["loop() entry"]
        M5_UPDATE["M5Cardputer.update()"]
        REPL_UPDATE["repl_view.update()"]
        LOOP_END["loop() exit"]
    end
    
    subgraph "ReplView::update()"
        UPDATE_KB["update_keyboard_input()"]
        UPDATE_CURSOR["update_cursor()"]
    end
    
    subgraph "Input Processing"
        CHECK_CHANGE["Keyboard.isChange()"]
        CHECK_PRESSED["Keyboard.isPressed()"]
        GET_STATE["keysState()"]
        HANDLE_ENTER["handle_enter_key()"]
        HANDLE_BACK["handle_backspace()"]
        APPEND_CHARS["append to _input_buffer"]
    end
    
    subgraph "Cursor Animation"
        CHECK_TIME["millis() - _cursor_update_time > 500"]
        TOGGLE_STATE["_cursor_state = !_cursor_state"]
        RENDER["render_prompt()"]
    end
    
    LOOP_START --> M5_UPDATE
    M5_UPDATE --> REPL_UPDATE
    REPL_UPDATE --> UPDATE_KB
    REPL_UPDATE --> UPDATE_CURSOR
    UPDATE_KB --> CHECK_CHANGE
    CHECK_CHANGE -->|true| CHECK_PRESSED
    CHECK_PRESSED -->|true| GET_STATE
    GET_STATE -->|enter| HANDLE_ENTER
    GET_STATE -->|del| HANDLE_BACK
    GET_STATE -->|word| APPEND_CHARS
    APPEND_CHARS --> RENDER
    
    UPDATE_CURSOR --> CHECK_TIME
    CHECK_TIME -->|true| TOGGLE_STATE
    TOGGLE_STATE --> RENDER
    
    RENDER --> LOOP_END
```

### Update Timing

- **Keyboard polling:** Every call to `M5Cardputer.update()` refreshes keyboard state
- **Cursor blink:** Toggles every `CURSOR_BLINK_PERIOD` (500ms) based on `millis()` comparison
- **Rendering:** Only occurs when input changes or cursor state toggles, minimizing unnecessary redraws

**Sources:** [examples/UI/REPL/REPL.ino:82-87](), [examples/UI/REPL/ReplView.cpp:14-18](), [examples/UI/REPL/ReplView.cpp:136-143]()

---

## Keyboard Input Processing

The `update_keyboard_input()` method implements a state-machine approach to keyboard event handling, processing special keys first, then collecting character input.

```mermaid
graph TB
    START["update_keyboard_input()"]
    CHECK_CHANGE{"Keyboard.isChange()"}
    CHECK_PRESSED{"Keyboard.isPressed()"}
    GET_STATUS["status = Keyboard.keysState()"]
    
    CHECK_ENTER{"status.enter?"}
    HANDLE_ENTER["handle_enter_key()"]
    ENTER_RETURN["return"]
    
    CHECK_DEL{"status.del?"}
    HANDLE_DEL["handle_backspace()"]
    DEL_RETURN["return"]
    
    ITERATE["for (auto& c : status.word)"]
    APPEND["_input_buffer += c"]
    RENDER["render_prompt()"]
    END["return"]
    
    START --> CHECK_CHANGE
    CHECK_CHANGE -->|false| END
    CHECK_CHANGE -->|true| CHECK_PRESSED
    CHECK_PRESSED -->|false| END
    CHECK_PRESSED -->|true| GET_STATUS
    
    GET_STATUS --> CHECK_ENTER
    CHECK_ENTER -->|true| HANDLE_ENTER
    HANDLE_ENTER --> ENTER_RETURN
    ENTER_RETURN --> END
    
    CHECK_ENTER -->|false| CHECK_DEL
    CHECK_DEL -->|true| HANDLE_DEL
    HANDLE_DEL --> DEL_RETURN
    DEL_RETURN --> END
    
    CHECK_DEL -->|false| ITERATE
    ITERATE --> APPEND
    APPEND --> RENDER
    RENDER --> END
```

### Key Event Handling

| Key | Field | Handler | Behavior |
|-----|-------|---------|----------|
| Enter | `status.enter` | `handle_enter_key()` | Finalizes input, invokes `onCommand` callback, clears buffer if `autoClearPrompt` |
| Backspace/Delete | `status.del` | `handle_backspace()` | Removes last character from `_input_buffer`, re-renders prompt |
| Printable characters | `status.word` | Direct append | Iterates through `word` vector, appends each character to `_input_buffer` |

### Enter Key Processing

When Enter is pressed, `handle_enter_key()` performs these steps:

1. **Finalize current line:** Clears cursor area with `fillRect()`, re-renders prompt + input without cursor
2. **Move to next line:** Calls `_canvas->println()` to advance cursor position
3. **Invoke command callback:** Calls `onCommand(_input_buffer)` if callback is set and buffer is non-empty
4. **Reset for next input:** Clears `_input_buffer` if `autoClearPrompt` is true, renders new prompt line

**Sources:** [examples/UI/REPL/ReplView.cpp:145-167](), [examples/UI/REPL/ReplView.cpp:99-120](), [examples/UI/REPL/ReplView.cpp:122-134]()

---

## Display Rendering Pipeline

The REPL application uses sprite-based double buffering to prevent screen flicker. All rendering operations target the `LGFX_Sprite` canvas, which is then pushed to the display as a complete frame.

```mermaid
graph TB
    subgraph "Canvas Configuration (render_interface)"
        FILL["fillScreen(TFT_BLACK)"]
        FONT["setFont(&fonts::efontCN_16)"]
        SCROLL["setTextScroll(true)"]
        CURSOR_POS["setCursor(0, 0)"]
        TEXT_SIZE["setTextSize(1)"]
        COLORS["setBaseColor(TFT_BLACK)<br/>setTextColor(TFT_WHITE, TFT_BLACK)"]
    end
    
    subgraph "Prompt Rendering (render_prompt)"
        GET_Y["cursor_y = getCursorY()"]
        CLEAR_LINE["fillRect(0, cursor_y, width, 15, TFT_BLACK)"]
        BUILD_TEXT["display_text = _prompt_text + _input_buffer"]
        ADD_CURSOR{"_cursor_state?"}
        CURSOR_CHAR["display_text += '_'"]
        SPACE_CHAR["display_text += ' '"]
        SET_CURSOR["setCursor(0, cursor_y)"]
        PRINT["print(display_text)"]
        PUSH["pushSprite(0, 0)"]
    end
    
    subgraph "Message Display (showMessage)"
        SET_COLOR["setTextColor(color, TFT_BLACK)"]
        PRINTLN["println(message)"]
        RESET_COLOR["setTextColor(TFT_WHITE, TFT_BLACK)"]
        PUSH_MSG["pushSprite(0, 0)"]
    end
    
    FILL --> FONT
    FONT --> SCROLL
    SCROLL --> CURSOR_POS
    CURSOR_POS --> TEXT_SIZE
    TEXT_SIZE --> COLORS
    
    GET_Y --> CLEAR_LINE
    CLEAR_LINE --> BUILD_TEXT
    BUILD_TEXT --> ADD_CURSOR
    ADD_CURSOR -->|true| CURSOR_CHAR
    ADD_CURSOR -->|false| SPACE_CHAR
    CURSOR_CHAR --> SET_CURSOR
    SPACE_CHAR --> SET_CURSOR
    SET_CURSOR --> PRINT
    PRINT --> PUSH
    
    SET_COLOR --> PRINTLN
    PRINTLN --> RESET_COLOR
    RESET_COLOR --> PUSH_MSG
```

### Critical Rendering Techniques

**Cursor Flicker Prevention:**
The cursor is rendered as part of the prompt text string rather than as a separate shape. This ensures atomic rendering—the entire line is drawn in one operation, preventing the cursor from appearing separate from the text.

**Line Clearing:**
Before re-rendering the prompt, `fillRect(0, cursor_y, _canvas->width(), 15, TFT_BLACK)` clears the entire line. The height of 15 pixels matches the font height to ensure complete erasure of previous characters and cursor states.

**Text Scrolling:**
`setTextScroll(true)` enables automatic vertical scrolling when `println()` operations exceed canvas height. New lines push older content upward, maintaining a scrolling terminal effect.

**Sources:** [examples/UI/REPL/ReplView.cpp:58-97](), [examples/UI/REPL/ReplView.cpp:27-33]()

---

## Application-Specific Implementation

The number-guessing game in `REPL.ino` demonstrates how to use `ReplView` to implement application logic through callbacks.

### Game State Management

```mermaid
stateDiagram-v2
    [*] --> Playing: setup() generates random number
    
    state Playing {
        [*] --> WaitingInput: showPrompt()
        WaitingInput --> ValidatingInput: Enter pressed
        ValidatingInput --> ShowingFeedback: string_to_number()
        ShowingFeedback --> WaitingInput: showMessage()
    }
    
    Playing --> Won: number == the_number
    
    state Won {
        [*] --> DisplayingMessages: is_player_win = true
        DisplayingMessages --> DisplayingMessages: Any input shows as cyan message
    }
```

### Input Validation Flow

The `string_to_number()` function implements strict input validation:

```mermaid
graph TB
    INPUT["const char* str"]
    CHECK_NULL{"str == NULL || *str == '\\0'?"}
    STRTOL["value = strtol(str, &end, 10)"]
    CHECK_TRAILING{"*end != '\\0'?"}
    CHECK_RANGE{"value < -999 || value > 999?"}
    SUCCESS["*out = value<br/>return true"]
    FAIL["return false"]
    
    INPUT --> CHECK_NULL
    CHECK_NULL -->|true| FAIL
    CHECK_NULL -->|false| STRTOL
    STRTOL --> CHECK_TRAILING
    CHECK_TRAILING -->|true| FAIL
    CHECK_TRAILING -->|false| CHECK_RANGE
    CHECK_RANGE -->|true| FAIL
    CHECK_RANGE -->|false| SUCCESS
```

**Validation Rules:**
- Input must be non-null and non-empty
- Must parse completely as base-10 integer (no trailing characters)
- Must be within range [-999, 999]

**Sources:** [examples/UI/REPL/REPL.ino:14-33]()

### Command Handler Implementation

```mermaid
graph TB
    COMMAND["handle_command(const string& command)"]
    CHECK_WIN{"is_player_win?"}
    SHOW_WIN["showMessage(command, TFT_CYAN)<br/>return"]
    
    PARSE["string_to_number(command, &number)"]
    CHECK_VALID{"Valid?"}
    SHOW_INVALID["showMessage('Invalid input :(', TFT_RED)<br/>return"]
    
    COMPARE{"number == the_number?"}
    TOO_HIGH{"number > the_number?"}
    
    WIN["showMessage('Correct! :)', TFT_GREENYELLOW)<br/>is_player_win = true"]
    HIGH["showMessage('Too high!', TFT_CYAN)"]
    LOW["showMessage('Too low!', TFT_CYAN)"]
    
    COMMAND --> CHECK_WIN
    CHECK_WIN -->|true| SHOW_WIN
    CHECK_WIN -->|false| PARSE
    
    PARSE --> CHECK_VALID
    CHECK_VALID -->|false| SHOW_INVALID
    CHECK_VALID -->|true| COMPARE
    
    COMPARE -->|true| WIN
    COMPARE -->|false| TOO_HIGH
    TOO_HIGH -->|true| HIGH
    TOO_HIGH -->|false| LOW
```

### Color Coding Scheme

| Message Type | Color Constant | RGB | Usage |
|--------------|---------------|-----|-------|
| Success | `TFT_GREENYELLOW` | Green-Yellow | Correct guess |
| Information | `TFT_CYAN` | Cyan | Hints, post-win messages |
| Error | `TFT_RED` | Red | Invalid input |
| Default | `TFT_WHITE` | White | Prompt text |

**Sources:** [examples/UI/REPL/REPL.ino:35-59]()

---

## Usage Patterns

### Basic REPL Setup

```
setup():
  1. Initialize M5Cardputer
  2. Create LGFX_Sprite covering full display
  3. Set ReplView callbacks (onRenderTips, onCommand)
  4. Call ReplView::init()
  
loop():
  1. Call M5Cardputer.update() to refresh hardware state
  2. Call ReplView::update() to process input and animate cursor
```

### Customizing the Interface

**Changing Prompt Text:**
```cpp
repl_view.setPromptText("custom> ");
```

**Pre-filling Input:**
```cpp
repl_view.setInputBuffer("default text");
```

**Preserving Input After Enter:**
```cpp
repl_view.autoClearPrompt = false;
```

**Displaying Colored Messages:**
```cpp
repl_view.showMessage("Error occurred", TFT_RED);
repl_view.showMessage("Processing...", TFT_YELLOW);
```

**Clearing Screen:**
```cpp
repl_view.clearScreen();
```

**Sources:** [examples/UI/REPL/ReplView.h:19-34](), [examples/UI/REPL/ReplView.cpp:35-56]()

---

## Memory and Performance Considerations

### Sprite Memory Allocation

The full-screen sprite requires approximately 38,400 bytes (240×135×16bpp÷8) for the M5Cardputer's 240×135 display. This memory is allocated on the heap via `createSprite()`.

**Memory Layout:**
- `LGFX_Sprite` object: ~100 bytes (stack or heap depending on allocation)
- Frame buffer: 38,400 bytes (heap)
- Total: ~38.5 KB

### Rendering Performance

| Operation | Frequency | Cost |
|-----------|-----------|------|
| `render_prompt()` | On input change + cursor blink (every 500ms) | ~5ms (fillRect + print + pushSprite) |
| `update_keyboard_input()` | Every loop iteration | <1ms (no-op when no keys pressed) |
| `update_cursor()` | Every loop iteration | <1ms (time comparison only) |
| `showMessage()` | Per command execution | ~3ms (println + pushSprite) |

### Optimization Notes

- **Cursor rendering:** Only re-renders when state changes or input is modified
- **Keyboard polling:** Early returns from `update_keyboard_input()` when `isChange()` is false
- **Line clearing:** Uses `fillRect()` instead of clearing entire canvas, minimizing pixel writes
- **Text scrolling:** Handled natively by M5GFX, no application-level buffer management needed

**Sources:** [examples/UI/REPL/ReplView.cpp:75-97](), [examples/UI/REPL/ReplView.cpp:136-167]()

---

## Extension Opportunities

### Adding Command History

Implement up/down arrow navigation through previous commands by:
1. Storing commands in `std::vector<std::string>`
2. Tracking current history index
3. Processing `status.fn` modifier with keyboard navigation
4. Calling `setInputBuffer()` to display historical command

### Implementing Tab Completion

Add auto-completion by:
1. Maintaining a list of valid commands
2. Detecting Tab key in `update_keyboard_input()`
3. Matching `_input_buffer` prefix against command list
4. Completing partial match or cycling through options

### Multi-line Input Support

Enable multi-line editing by:
1. Treating Enter as line break instead of command submission
2. Using Ctrl+Enter for command submission
3. Tracking cursor position within multi-line buffer
4. Implementing vertical cursor navigation

### Custom Syntax Highlighting

Add color-coded text by:
1. Parsing `_input_buffer` for keywords/syntax
2. Rendering different segments with `setTextColor()` before each `print()`
3. Maintaining color state during character-by-character rendering

**Sources:** [examples/UI/REPL/ReplView.h:15-51](), [examples/UI/REPL/ReplView.cpp:145-167]()