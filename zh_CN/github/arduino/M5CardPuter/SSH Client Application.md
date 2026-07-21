M5Cardputer SSH Client Application

# SSH Client Application

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Advanced/SSHClient/SSHClient.ino](examples/Advanced/SSHClient/SSHClient.ino)

</details>



## Purpose and Scope

This page documents the SSH Client example application included with the M5Cardputer library. The application demonstrates how to build a terminal emulator that connects to remote SSH servers, providing interactive command-line access through the M5Cardputer's keyboard and display. It covers WiFi initialization, LibSSH-ESP32 session management, PTY (pseudo-terminal) configuration, keyboard input processing, display scrolling, and ANSI escape sequence filtering.

For general networking overview and IR communication features, see [Networking and Communication](#8). For keyboard input processing details, see [Keyboard_Class API](#4.1). For display text handling patterns, see [Text Input and Display Patterns](#5.1).

## Application Architecture

The SSH Client application integrates several subsystems to create a functional terminal emulator on the M5Cardputer device.

```mermaid
graph TB
    subgraph "Application Layer"
        MAIN["SSHClient.ino::loop()<br/>Main Event Loop"]
        SETUP["SSHClient.ino::setup()<br/>Initialization"]
        WAIT["SSHClient.ino::waitForInput()<br/>Credential Input Handler"]
    end
    
    subgraph "M5Cardputer Hardware API"
        KB["M5Cardputer.Keyboard<br/>Keyboard_Class"]
        DISP["M5Cardputer.Display<br/>M5GFX Display"]
        UPDATE["M5Cardputer.update()<br/>State Update"]
    end
    
    subgraph "LibSSH-ESP32 API"
        SESSION["ssh_session<br/>Connection Handle"]
        CHANNEL["ssh_channel<br/>Communication Channel"]
        AUTH["ssh_userauth_password()<br/>Authentication"]
        READ["ssh_channel_read_nonblocking()<br/>Server Output"]
        WRITE["ssh_channel_write()<br/>Command Input"]
        PTY["ssh_channel_request_pty()<br/>Terminal Emulation"]
    end
    
    subgraph "WiFi Stack"
        WIFI["WiFi.begin()<br/>Network Connection"]
    end
    
    subgraph "Application State"
        CMDBUF["commandBuffer<br/>Input Line Buffer"]
        CURSORY["cursorY<br/>Vertical Position"]
        CREDENTIALS["ssh_host, ssh_user, ssh_password<br/>Connection Details"]
        FILTER["filterAnsiSequences<br/>Display Mode Flag"]
    end
    
    SETUP --> WIFI
    SETUP --> WAIT
    WAIT --> KB
    WAIT --> DISP
    WAIT --> CREDENTIALS
    
    SETUP --> SESSION
    SESSION --> AUTH
    AUTH --> CHANNEL
    CHANNEL --> PTY
    
    MAIN --> UPDATE
    MAIN --> KB
    KB --> CMDBUF
    
    MAIN --> WRITE
    CMDBUF --> WRITE
    WRITE --> CHANNEL
    
    MAIN --> READ
    READ --> CHANNEL
    READ --> FILTER
    
    MAIN --> DISP
    FILTER --> DISP
    CMDBUF --> DISP
    CURSORY --> DISP
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:1-272]()

## Key Components

### Global State Variables

| Variable | Type | Purpose | Initial Value |
|----------|------|---------|---------------|
| `ssh_host` | `String` | SSH server hostname/IP | Empty string |
| `ssh_user` | `String` | SSH username | Empty string |
| `ssh_password` | `String` | SSH password | Empty string |
| `my_ssh_session` | `ssh_session` | LibSSH session handle | Created by `ssh_new()` |
| `channel` | `ssh_channel` | LibSSH channel handle | Created by `ssh_channel_new()` |
| `commandBuffer` | `String` | Current input line | `"> "` (prompt) |
| `cursorY` | `int` | Vertical cursor position | 0 |
| `filterAnsiSequences` | `bool` | ANSI filtering toggle | `true` |
| `lastKeyPressMillis` | `unsigned long` | Debounce timestamp | 0 |

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:26-44]()

### Configuration Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| `lineHeight` | 32 | Vertical scroll increment in pixels |
| `debounceDelay` | 200 ms | Minimum time between key events |

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:34-36]()

## Initialization Sequence

The application follows a multi-stage initialization process to establish a fully functional SSH terminal session.

```mermaid
sequenceDiagram
    participant SETUP as "setup() Function"
    participant WIFI as "WiFi Stack"
    participant DISPLAY as "M5Cardputer.Display"
    participant USER as "User Input"
    participant LIBSSH as "LibSSH-ESP32"
    
    SETUP->>DISPLAY: Initialize with rotation=1, textSize=1
    SETUP->>WIFI: WiFi.begin(ssid, password)
    WIFI-->>SETUP: WL_CONNECTED
    
    SETUP->>DISPLAY: Print "SSH Host: "
    SETUP->>USER: waitForInput(ssh_host)
    USER-->>SETUP: Host entered
    
    SETUP->>DISPLAY: Print "SSH Username: "
    SETUP->>USER: waitForInput(ssh_user)
    USER-->>SETUP: Username entered
    
    SETUP->>DISPLAY: Print "SSH Password: "
    SETUP->>USER: waitForInput(ssh_password)
    USER-->>SETUP: Password entered
    
    SETUP->>LIBSSH: ssh_new()
    LIBSSH-->>SETUP: my_ssh_session
    
    SETUP->>LIBSSH: ssh_options_set(HOST, USER)
    SETUP->>LIBSSH: ssh_connect(my_ssh_session)
    LIBSSH-->>SETUP: SSH_OK
    
    SETUP->>LIBSSH: ssh_userauth_password()
    LIBSSH-->>SETUP: SSH_AUTH_SUCCESS
    
    SETUP->>LIBSSH: ssh_channel_new()
    LIBSSH-->>SETUP: channel
    
    SETUP->>LIBSSH: ssh_channel_open_session()
    SETUP->>LIBSSH: ssh_channel_request_pty()
    SETUP->>LIBSSH: ssh_channel_request_shell()
    LIBSSH-->>SETUP: Ready for commands
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:46-124]()

### WiFi Connection

The application connects to WiFi during setup using blocking calls:

```
WiFi.begin(ssid, password);
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
}
```

The WiFi SSID and password must be hardcoded in the sketch at compile time ([examples/Advanced/SSHClient/SSHClient.ino:22-23]()).

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:56-61]()

### Credential Input with `waitForInput()`

The `waitForInput()` function implements a blocking input routine for collecting SSH credentials. It uses the keyboard subsystem to capture characters and display them in real-time.

```mermaid
graph TB
    START["waitForInput(String& input)"]
    UPDATE["M5Cardputer.update()"]
    CHECK["Keyboard.isChange()"]
    GET["keysState()"]
    
    subgraph "Key Handling"
        DEL["status.del?<br/>Backspace"]
        WORD["status.word<br/>Character Input"]
        ENTER["status.enter?<br/>Submit"]
    end
    
    subgraph "Display Updates"
        ERASE["Erase last character<br/>setCursor, print space"]
        PRINT["Print character"]
        NEWLINE["println()"]
    end
    
    TIMEOUT["Timeout Check<br/>180 seconds"]
    REBOOT["ESP.restart()"]
    RETURN["Return to caller"]
    
    START --> UPDATE
    UPDATE --> CHECK
    CHECK -->|Yes| GET
    GET --> DEL
    GET --> WORD
    GET --> ENTER
    
    DEL --> ERASE
    WORD --> PRINT
    ENTER --> NEWLINE
    NEWLINE --> RETURN
    
    CHECK -->|No| TIMEOUT
    TIMEOUT -->|Exceeded| REBOOT
    TIMEOUT -->|Not exceeded| UPDATE
```

**Key features:**
- **Debouncing**: 200ms delay between key presses ([examples/Advanced/SSHClient/SSHClient.ino:227]())
- **Backspace handling**: Removes characters from input buffer and display ([examples/Advanced/SSHClient/SSHClient.ino:235-247]())
- **Character accumulation**: Appends `status.word` characters to `currentInput` ([examples/Advanced/SSHClient/SSHClient.ino:249-256]())
- **Timeout protection**: Reboots after 180 seconds (3 minutes) of inactivity ([examples/Advanced/SSHClient/SSHClient.ino:265-270]())

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:224-272]()

### SSH Session Establishment

The LibSSH-ESP32 library requires a specific sequence of calls to establish an interactive shell session:

1. **Create session**: `ssh_session my_ssh_session = ssh_new()` ([examples/Advanced/SSHClient/SSHClient.ino:75]())
2. **Set options**: `ssh_options_set()` for host and user ([examples/Advanced/SSHClient/SSHClient.ino:80-81]())
3. **Connect**: `ssh_connect(my_ssh_session)` ([examples/Advanced/SSHClient/SSHClient.ino:83]())
4. **Authenticate**: `ssh_userauth_password()` with password ([examples/Advanced/SSHClient/SSHClient.ino:89-90]())
5. **Create channel**: `ssh_channel channel = ssh_channel_new(my_ssh_session)` ([examples/Advanced/SSHClient/SSHClient.ino:97]())
6. **Open session**: `ssh_channel_open_session(channel)` ([examples/Advanced/SSHClient/SSHClient.ino:98]())
7. **Request PTY**: `ssh_channel_request_pty(channel)` for terminal emulation ([examples/Advanced/SSHClient/SSHClient.ino:105]())
8. **Request shell**: `ssh_channel_request_shell(channel)` to start interactive shell ([examples/Advanced/SSHClient/SSHClient.ino:114]())

Each step includes error checking with early return on failure. The PTY request is critical for interactive terminal behavior, enabling proper line editing, cursor control, and command echoing on the remote server.

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:75-121]()

## Main Loop Operation

The `loop()` function implements the core terminal emulator logic, handling bidirectional communication between the keyboard and SSH server.

```mermaid
graph TB
    LOOP_START["loop() Entry"]
    UPDATE["M5Cardputer.update()"]
    
    subgraph "Keyboard Input Path"
        KB_CHECK["Keyboard.isChange() &&<br/>Keyboard.isPressed()"]
        DEBOUNCE["Check debounceDelay"]
        GET_STATE["keysState()"]
        
        subgraph "Character Processing"
            WORD_LOOP["For each char in status.word"]
            APPEND_BUF["commandBuffer += char"]
            DISPLAY_CHAR["Display.print(char)"]
        end
        
        DEL_CHECK["status.del?"]
        DEL_HANDLE["Remove from buffer<br/>Erase from display"]
        
        ENTER_CHECK["status.enter?"]
        EXTRACT_CMD["Extract command<br/>(substring after '> ')"]
        SEND_CMD["ssh_channel_write(command)"]
        SEND_CR["ssh_channel_write('\\r')"]
        RESET_BUF["commandBuffer = '> '"]
    end
    
    subgraph "Display Scrolling"
        SCROLL_CHECK["cursorY > height - lineHeight?"]
        SCROLL_UP["Display.scroll(0, -lineHeight)"]
        ADJUST_Y["cursorY -= lineHeight"]
    end
    
    subgraph "Server Output Path"
        READ_SSH["ssh_channel_read_nonblocking()"]
        CHECK_BYTES["nbytes > 0?"]
        
        subgraph "ANSI Filtering"
            CHAR_LOOP["For each byte in buffer"]
            ESC_CHECK["byte == '\\033'?"]
            ANSI_MODE["isAnsiSequence = true"]
            ALPHA_CHECK["isalpha()?"]
            EXIT_ANSI["isAnsiSequence = false"]
            DISPLAY_BYTE["Display.write(byte)"]
        end
    end
    
    CLOSED_CHECK["Channel closed?"]
    CLEANUP["Close channel, disconnect,<br/>free session"]
    
    LOOP_START --> UPDATE
    UPDATE --> KB_CHECK
    KB_CHECK -->|Yes| DEBOUNCE
    DEBOUNCE --> GET_STATE
    GET_STATE --> WORD_LOOP
    WORD_LOOP --> APPEND_BUF
    APPEND_BUF --> DISPLAY_CHAR
    GET_STATE --> DEL_CHECK
    DEL_CHECK -->|Yes| DEL_HANDLE
    GET_STATE --> ENTER_CHECK
    ENTER_CHECK -->|Yes| EXTRACT_CMD
    EXTRACT_CMD --> SEND_CMD
    SEND_CMD --> SEND_CR
    SEND_CR --> RESET_BUF
    
    KB_CHECK -->|No| SCROLL_CHECK
    RESET_BUF --> SCROLL_CHECK
    DEL_HANDLE --> SCROLL_CHECK
    DISPLAY_CHAR --> SCROLL_CHECK
    
    SCROLL_CHECK -->|Yes| SCROLL_UP
    SCROLL_UP --> ADJUST_Y
    SCROLL_CHECK -->|No| READ_SSH
    ADJUST_Y --> READ_SSH
    
    READ_SSH --> CHECK_BYTES
    CHECK_BYTES -->|Yes| CHAR_LOOP
    CHAR_LOOP --> ESC_CHECK
    ESC_CHECK -->|Yes| ANSI_MODE
    ESC_CHECK -->|No| ALPHA_CHECK
    ALPHA_CHECK -->|Yes, in ANSI mode| EXIT_ANSI
    ALPHA_CHECK -->|No| DISPLAY_BYTE
    
    CHECK_BYTES -->|No| CLOSED_CHECK
    DISPLAY_BYTE --> CLOSED_CHECK
    EXIT_ANSI --> CLOSED_CHECK
    CLOSED_CHECK -->|Yes| CLEANUP
    CLOSED_CHECK -->|No| LOOP_START
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:126-222]()

## Keyboard Input Processing

The application uses the M5Cardputer keyboard subsystem to capture user input with debouncing.

### Input Event Handling

The keyboard state is checked on each loop iteration:

```
if (M5Cardputer.Keyboard.isChange() && M5Cardputer.Keyboard.isPressed()) {
    unsigned long currentMillis = millis();
    if (currentMillis - lastKeyPressMillis >= debounceDelay) {
        lastKeyPressMillis = currentMillis;
        Keyboard_Class::KeysState status = M5Cardputer.Keyboard.keysState();
        // Process keys...
    }
}
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:130-134]()

### Character Accumulation

Characters from `status.word` are appended to `commandBuffer` and immediately displayed:

```
for (auto i : status.word) {
    commandBuffer += i;
    M5Cardputer.Display.print(i);
    cursorY = M5Cardputer.Display.getCursorY();
}
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:136-140]()

### Backspace Handling

The delete key removes the last character from both the buffer and display. The implementation protects the prompt (`"> "`) from deletion:

```
if (status.del && commandBuffer.length() > 2) {
    commandBuffer.remove(commandBuffer.length() - 1);
    M5Cardputer.Display.setCursor(
        M5Cardputer.Display.getCursorX() - 6,
        M5Cardputer.Display.getCursorY());
    M5Cardputer.Display.print(" ");
    M5Cardputer.Display.setCursor(
        M5Cardputer.Display.getCursorX() - 6,
        M5Cardputer.Display.getCursorY());
    cursorY = M5Cardputer.Display.getCursorY();
}
```

The cursor is moved back 6 pixels (character width), a space is printed to erase the character, and the cursor is moved back again to position for the next character.

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:142-152]()

### Command Submission

When Enter is pressed, the command is extracted (excluding the `"> "` prompt), sent to the SSH server, and the buffer is reset:

```
if (status.enter) {
    commandBuffer.trim();
    String message = commandBuffer.substring(2);  // Exclude "> "
    ssh_channel_write(channel, message.c_str(), message.length());
    ssh_channel_write(channel, "\r", 1);  // Send carriage return
    
    commandBuffer = "> ";  // Reset to prompt
    M5Cardputer.Display.print('\n');
    cursorY = M5Cardputer.Display.getCursorY();
}
```

Note that only a single carriage return (`"\r"`) is sent. Different servers may require `"\n"` or `"\r\n"` as noted in the code comments.

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:154-170]()

## Display Management

### Automatic Scrolling

When the cursor reaches the bottom of the display, the content scrolls upward by one line:

```
if (cursorY > M5Cardputer.Display.height() - lineHeight) {
    M5Cardputer.Display.scroll(0, -lineHeight);
    cursorY -= lineHeight;
    M5Cardputer.Display.setCursor(M5Cardputer.Display.getCursorX(), cursorY);
}
```

The `lineHeight` constant (32 pixels) determines the scroll increment. The cursor position is adjusted to remain on-screen after scrolling.

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:174-180]()

### Display Configuration

The display is configured during setup with:
- **Rotation**: 1 (landscape orientation) ([examples/Advanced/SSHClient/SSHClient.ino:52]())
- **Text size**: 1 (default font size) ([examples/Advanced/SSHClient/SSHClient.ino:53]())

## Server Output Processing

The application reads data from the SSH channel and processes it for display.

```mermaid
graph TB
    READ["ssh_channel_read_nonblocking(channel, buffer, 128, 0)"]
    CHECK["nbytes > 0?"]
    
    subgraph "Character Loop"
        ITER["For i = 0 to nbytes-1"]
        GETCHAR["c = buffer[i]"]
        
        subgraph "ANSI Filter Path (if enabled)"
            ESC["c == '\\033'?"]
            SET_ANSI["isAnsiSequence = true"]
            IN_ANSI["isAnsiSequence?"]
            ALPHA["isalpha(c)?"]
            CLEAR_ANSI["isAnsiSequence = false"]
            SKIP["Skip character"]
        end
        
        subgraph "Display Path"
            CR["c == '\\r'?"]
            WRITE["Display.write(c)"]
            UPDATE_Y["cursorY = getCursorY()"]
        end
    end
    
    CHANNEL_CHECK["Channel closed or error?"]
    CLEANUP["Close and cleanup"]
    
    READ --> CHECK
    CHECK -->|Yes| ITER
    ITER --> GETCHAR
    GETCHAR --> ESC
    ESC -->|Yes| SET_ANSI
    ESC -->|No| IN_ANSI
    IN_ANSI -->|Yes| ALPHA
    ALPHA -->|Yes| CLEAR_ANSI
    ALPHA -->|No| SKIP
    CLEAR_ANSI --> SKIP
    IN_ANSI -->|No| CR
    CR -->|No| WRITE
    CR -->|Yes| SKIP
    WRITE --> UPDATE_Y
    UPDATE_Y --> ITER
    SKIP --> ITER
    
    CHECK -->|No| CHANNEL_CHECK
    ITER -->|Complete| CHANNEL_CHECK
    CHANNEL_CHECK -->|Yes| CLEANUP
```

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:183-221]()

### Non-Blocking Read

The application uses `ssh_channel_read_nonblocking()` with a 128-byte buffer to avoid blocking the main loop:

```
char buffer[128];
int nbytes = ssh_channel_read_nonblocking(channel, buffer, sizeof(buffer), 0);
```

This allows the application to continue processing keyboard input even when no server output is available.

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:183-185]()

### ANSI Escape Sequence Filtering

The `filterAnsiSequences` flag controls whether ANSI escape codes are removed from the output. When enabled, the filter operates as follows:

1. When `'\033'` (ESC) is encountered, set `isAnsiSequence = true` ([examples/Advanced/SSHClient/SSHClient.ino:193-194]())
2. While in ANSI sequence mode, skip all characters ([examples/Advanced/SSHClient/SSHClient.ino:195-199]())
3. When an alphabetic character is found (the terminating character of ANSI sequences), set `isAnsiSequence = false` ([examples/Advanced/SSHClient/SSHClient.ino:196-198]())
4. Only display characters when not in ANSI sequence mode ([examples/Advanced/SSHClient/SSHClient.ino:200-204]())

This simple state machine filters most common ANSI escape sequences including:
- Cursor positioning codes (e.g., `\033[H`)
- Text formatting codes (e.g., `\033[1m` for bold)
- Color codes (e.g., `\033[31m` for red text)

Carriage return characters (`'\r'`) are always filtered to prevent display issues ([examples/Advanced/SSHClient/SSHClient.ino:201]()).

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:189-211]()

## Session Cleanup

When the channel is closed or an error occurs, the application performs orderly cleanup:

```
if (nbytes < 0 || ssh_channel_is_closed(channel)) {
    ssh_channel_close(channel);
    ssh_channel_free(channel);
    ssh_disconnect(my_ssh_session);
    ssh_free(my_ssh_session);
    M5Cardputer.Display.println("\nSSH session closed.");
    return;
}
```

The cleanup sequence follows LibSSH-ESP32 best practices:
1. Close the channel
2. Free the channel handle
3. Disconnect the session
4. Free the session handle

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:214-221]()

## Configuration and Customization

### Required Changes

Before compiling, users must modify the following constants:

| Constant | Location | Purpose |
|----------|----------|---------|
| `ssid` | [Line 22]() | WiFi network SSID |
| `password` | [Line 23]() | WiFi network password |

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:22-23]()

### Optional Configuration

| Variable | Default | Purpose | Modification Impact |
|----------|---------|---------|---------------------|
| `filterAnsiSequences` | `true` | Enable ANSI filtering | Set to `false` to display raw ANSI codes |
| `debounceDelay` | 200 ms | Key debounce time | Reduce for faster input, increase if keys repeat |
| `lineHeight` | 32 pixels | Scroll increment | Adjust based on font size |

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:43-44](), [examples/Advanced/SSHClient/SSHClient.ino:34-36]()

## Limitations and Considerations

### Terminal Emulation Limitations

- **No cursor control**: The application does not interpret ANSI cursor positioning codes beyond filtering them
- **No line editing**: Server-side line editing (arrow keys, home/end) is not supported
- **Single-line input**: Commands must fit on one line; multi-line editing is not implemented
- **No scrollback**: Previous output cannot be scrolled back once it moves off-screen

### Security Considerations

- **Plaintext credentials**: SSH credentials are hardcoded in the sketch or entered at runtime but stored in plaintext in memory
- **No host key verification**: The application does not verify SSH host keys, making it vulnerable to man-in-the-middle attacks
- **Password authentication only**: Public key authentication is not implemented

### Performance Considerations

- **Small buffer size**: The 128-byte read buffer may cause display lag with high-volume server output
- **Synchronous keyboard handling**: The 200ms debounce delay adds perceptible latency to keyboard input
- **No output buffering**: Each character is individually written to the display, which may be slow for bulk output

## Integration with M5Cardputer Systems

The SSH Client example demonstrates integration of multiple M5Cardputer subsystems:

| Subsystem | Integration Point | Purpose |
|-----------|-------------------|---------|
| Keyboard | `M5Cardputer.Keyboard.keysState()` | Capture user input |
| Display | `M5Cardputer.Display` (M5GFX) | Render terminal output |
| WiFi | ESP32 WiFi stack | Network connectivity |
| LibSSH-ESP32 | `ssh_*` function calls | SSH protocol implementation |

The application follows the standard M5Cardputer event loop pattern:
1. Call `M5Cardputer.update()` to refresh peripheral states
2. Check for keyboard changes
3. Process any pending events
4. Update display as needed

This pattern is consistent with other M5Cardputer examples like the REPL application (see [REPL Application](#9.1)).

**Sources:** [examples/Advanced/SSHClient/SSHClient.ino:126-172]()