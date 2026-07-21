StackChan WebSocket Protocol

# WebSocket Protocol

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [app/StackChan/AppState.swift](app/StackChan/AppState.swift)
- [app/StackChan/Model/MessageModel.swift](app/StackChan/Model/MessageModel.swift)

</details>



This page documents the WebSocket protocol used for real-time bidirectional communication between StackChan components (iOS app, robot firmware, and backend server). The protocol defines the binary message format, message types, and communication patterns that enable live video streaming, audio transmission, motion control, and status updates.

For information about the initial device configuration over Bluetooth, see [Bluetooth LE (Blufi Protocol)](#7.1). For HTTP-based device management endpoints, see [HTTP REST API](#7.3). For a complete reference of all message types and their purposes, see [Message Types Reference](#7.4).

## Connection Establishment

WebSocket connections are initiated by both the iOS app and the robot firmware to the backend server. The server acts as a central relay hub, forwarding messages between connected clients based on their device MAC addresses.

### Connection URL Format

The WebSocket endpoint uses query parameters to identify the connecting client:

```
ws://<server-address>/ws?mac=<device-mac>&deviceType=<client-type>&deviceId=<unique-id>
```

**Parameters:**
- `mac`: The MAC address of the StackChan robot device
- `deviceType`: Either `"App"` for iOS clients or `"Device"` for robot firmware
- `deviceId`: A unique identifier for the connecting client (iOS uses `UIDevice.current.identifierForVendor`)

**Connection Flow:**

```mermaid
sequenceDiagram
    participant App as "iOS App<br/>(AppState)"
    participant WS as "WebSocketUtil"
    participant Server as "Go Server<br/>/ws endpoint"
    participant Robot as "Robot Firmware<br/>(WebSocket Client)"
    
    Note over App,Robot: Connection Establishment
    
    App->>App: "deviceMac = stored MAC"
    App->>App: "deviceId = UIDevice UUID"
    App->>App: "Build URL with parameters"
    App->>WS: "connect(urlString)"
    WS->>Server: "WebSocket handshake<br/>ws://server/ws?mac=XX&deviceType=App"
    Server->>Server: "Register connection<br/>by MAC and deviceType"
    
    Robot->>Server: "WebSocket handshake<br/>ws://server/ws?mac=XX&deviceType=Device"
    Server->>Server: "Register device connection<br/>by MAC"
    
    Note over App,Robot: Bidirectional Communication Active
    
    App->>Server: "Binary message (controlMotion)"
    Server->>Robot: "Forward to device with MAC"
    Robot->>Server: "Binary message (jpeg frame)"
    Server->>App: "Forward to app for MAC"
```

**Sources:** [app/StackChan/AppState.swift:93-96]()

### iOS Implementation

The iOS app establishes the WebSocket connection through the `AppState` class:

```swift
func connectWebSocket() {
    let webSocketUrl = Urls.getWebSocketUrl() + "?mac=" + deviceMac + 
                       "&deviceType=App&deviceId=" + AppState.deviceId
    WebSocketUtil.shared.connect(urlString: webSocketUrl)
}
```

**Sources:** [app/StackChan/AppState.swift:93-96]()

## Binary Protocol Structure

All messages transmitted over the WebSocket connection use a binary protocol format consisting of a type byte, length field, and payload.

### Message Format

```
+--------+--------+--------+--------+--------+----------------+
| Type   | Length (4 bytes, big-endian)       | Payload        |
| 1 byte | byte1  | byte2  | byte3  | byte4  | N bytes        |
+--------+--------+--------+--------+--------+----------------+
```

**Field Descriptions:**

| Field | Size | Type | Description |
|-------|------|------|-------------|
| Type | 1 byte | UInt8 | Message type identifier (see `MsgType` enum) |
| Length | 4 bytes | UInt32 | Payload size in bytes (big-endian) |
| Payload | Variable | Data | Message-specific data |

### Encoding Messages

The iOS app constructs messages using the `sendWebSocketMessage` function:

```mermaid
flowchart LR
    Input["MsgType + Data"] --> Buffer["Create Data buffer"]
    Buffer --> TypeByte["Append type byte"]
    TypeByte --> Length["Calculate payload length"]
    Length --> LengthBytes["Append 4 length bytes<br/>(big-endian)"]
    LengthBytes --> Payload["Append payload data"]
    Payload --> Send["WebSocketUtil.send()"]
```

**Encoding Process:**
1. Create a `Data` buffer starting with the message type byte
2. Calculate payload length as `UInt32`
3. Append 4 bytes representing length in big-endian order:
   - Byte 1: `(length >> 24) & 0xFF`
   - Byte 2: `(length >> 16) & 0xFF`
   - Byte 3: `(length >> 8) & 0xFF`
   - Byte 4: `length & 0xFF`
4. Append the payload data
5. Send via WebSocket

**Sources:** [app/StackChan/AppState.swift:98-114]()

### Decoding Messages

The iOS app parses received messages using the `parseMessage` function:

```mermaid
flowchart TD
    Start["Receive Data"] --> Check["Check length >= 5 bytes"]
    Check -->|"< 5"| Invalid["Return (nil, nil)"]
    Check -->|">= 5"| Extract["Extract type byte at [0]"]
    Extract --> ValidateType["Validate MsgType enum"]
    ValidateType -->|"Invalid"| Invalid
    ValidateType -->|"Valid"| ReadLength["Read length from [1...4]<br/>Combine bytes to UInt32"]
    ReadLength --> ValidatePayload["Check total length<br/>5 + payload length"]
    ValidatePayload -->|"Insufficient"| Invalid
    ValidatePayload -->|"Valid"| ExtractPayload["Extract payload<br/>from [5..<5+length]"]
    ExtractPayload --> Return["Return (MsgType, Data)"]
```

**Decoding Process:**
1. Verify minimum message length (5 bytes for header)
2. Read type byte at position 0
3. Validate against `MsgType` enum
4. Reconstruct length from 4 bytes: `(b1 << 24) | (b2 << 16) | (b3 << 8) | b4`
5. Verify total message length matches header + payload
6. Extract payload data from position 5 onwards
7. Return tuple of `(MsgType?, Data?)`

**Sources:** [app/StackChan/AppState.swift:117-139]()

## Message Types

The `MsgType` enum defines all supported message types with their hexadecimal identifiers:

```mermaid
classDiagram
    class MsgType {
        <<enum UInt8>>
        +opus: 0x01
        +jpeg: 0x02
        +controlAvatar: 0x03
        +controlMotion: 0x04
        +onCamera: 0x05
        +offCamera: 0x06
        +textMessage: 0x07
        +requestCall: 0x09
        +refuseCall: 0x0A
        +agreeCall: 0x0B
        +hangupCall: 0x0C
        +updateDeviceName: 0x0D
        +getDeviceName: 0x0E
        +ping: 0x10
        +pong: 0x11
        +onPhoneScreen: 0x12
        +offPhoneScreen: 0x13
        +dance: 0x14
        +getAvatarPosture: 0x15
        +deviceOffline: 0x16
        +deviceOnline: 0x17
    }
```

### Message Type Categories

| Category | Message Types | Direction | Description |
|----------|---------------|-----------|-------------|
| **Media Streaming** | `opus` (0x01), `jpeg` (0x02) | Robot → App | Audio frames (Opus codec) and video frames (JPEG images) |
| **Control Commands** | `controlAvatar` (0x03), `controlMotion` (0x04) | App → Robot | Facial expression control and servo motion commands |
| **Camera Control** | `onCamera` (0x05), `offCamera` (0x06) | App → Robot | Enable/disable camera streaming |
| **Text Communication** | `textMessage` (0x07) | Bidirectional | Text message exchange |
| **Call Management** | `requestCall` (0x09), `refuseCall` (0x0A), `agreeCall` (0x0B), `hangupCall` (0x0C) | Bidirectional | Video call session lifecycle |
| **Device Management** | `updateDeviceName` (0x0D), `getDeviceName` (0x0E) | Bidirectional | Device name synchronization |
| **Connection Health** | `ping` (0x10), `pong` (0x11) | Bidirectional | Keep-alive and latency measurement |
| **Screen State** | `onPhoneScreen` (0x12), `offPhoneScreen` (0x13) | App → Robot | Mobile app foreground/background state |
| **Entertainment** | `dance` (0x14), `getAvatarPosture` (0x15) | App → Robot | Dance sequence playback and posture queries |
| **Status Events** | `deviceOffline` (0x16), `deviceOnline` (0x17) | Server → App | Device connectivity status notifications |

**Sources:** [app/StackChan/Model/MessageModel.swift:9-39]()

## Communication Patterns

### Server-Mediated Relay

The Go backend server acts as a WebSocket relay, maintaining separate connections to both the iOS app and the robot, and forwarding messages based on MAC address routing:

```mermaid
sequenceDiagram
    participant App as "iOS App<br/>(WebSocketUtil)"
    participant Server as "Go Server<br/>(/ws handler)"
    participant Robot as "Robot Firmware"
    
    Note over App,Robot: Control Command Flow
    
    App->>App: "User triggers action"
    App->>App: "sendWebSocketMessage(controlMotion)"
    App->>Server: "Binary: [0x04][len][motion data]"
    Server->>Server: "Parse message header"
    Server->>Server: "Lookup device by MAC"
    Server->>Robot: "Forward: [0x04][len][motion data]"
    Robot->>Robot: "Execute servo movement"
    
    Note over App,Robot: Media Streaming Flow
    
    Robot->>Robot: "Capture camera frame"
    Robot->>Robot: "Encode as JPEG"
    Robot->>Server: "Binary: [0x02][len][jpeg data]"
    Server->>Server: "Lookup app by MAC"
    Server->>App: "Forward: [0x02][len][jpeg data]"
    App->>App: "parseMessage() extracts payload"
    App->>App: "Display frame"
```

### Message Monitoring and Handling

The iOS app implements a message observation pattern to handle incoming WebSocket messages:

```mermaid
flowchart TD
    Start["WebSocketUtil receives message"] --> Observer["Notify registered observers"]
    Observer --> AppState["AppState.webSocketMessageMonitoring"]
    AppState --> Switch["Switch on message type"]
    Switch --> Data["case .data(let data)"]
    Data --> Parse["parseMessage(message: data)"]
    Parse --> ExtractType["Extract MsgType"]
    ExtractType --> HandleType["Switch on msgType"]
    
    HandleType --> Online["deviceOnline:<br/>set deviceIsOnline = false"]
    HandleType --> Offline["deviceOffline:<br/>set deviceIsOnline = true"]
    HandleType --> Other["Other types:<br/>handled by specific views"]
    
    Switch --> String["case .string(let text):<br/>Log text message"]
```

The `AppState` class registers observers for WebSocket messages and processes status updates:

```swift
func webSocketMessageMonitoring() {
    WebSocketUtil.shared.addObserver(for: "App") { (message) in
        switch message {
        case .data(let data):
            let result = self.parseMessage(message: data)
            if let msgType = result.0 {
                switch msgType {
                case MsgType.deviceOnline:
                    self.deviceIsOnline = false
                case MsgType.deviceOffline:
                    self.deviceIsOnline = true
                default:
                    break
                }
            }
        case .string(let text):
            print("Received a regular message: \(text)")
        }
    }
}
```

**Sources:** [app/StackChan/AppState.swift:246-267]()

## Protocol Extension Points

### Custom Message Types

To add new message types to the protocol:

1. **Define enum case** in `MsgType` enum with unique hexadecimal identifier
2. **Implement encoding** logic in message sender (if payload structure differs)
3. **Implement decoding** logic in message receiver
4. **Update server relay** logic to handle routing (if special behavior needed)
5. **Document payload format** in [Message Types Reference](#7.4)

### Payload Structures

The binary protocol does not enforce payload structure beyond the header. Each message type defines its own payload format, which may be:
- **Raw binary data**: JPEG images, Opus audio frames
- **JSON-encoded data**: Control commands with parameters
- **Empty payload**: Simple flag messages (camera on/off)
- **Custom binary structures**: Optimized formats for performance

Specific payload formats for each message type are documented in [Message Types Reference](#7.4).

**Sources:** [app/StackChan/Model/MessageModel.swift:9-39](), [app/StackChan/AppState.swift:98-139]()

## Implementation References

### Key Code Entities

| Entity | Location | Purpose |
|--------|----------|---------|
| `MsgType` | [app/StackChan/Model/MessageModel.swift:9-39]() | Enum defining all message type identifiers |
| `AppState.connectWebSocket()` | [app/StackChan/AppState.swift:93-96]() | Establishes WebSocket connection with URL parameters |
| `AppState.sendWebSocketMessage()` | [app/StackChan/AppState.swift:98-114]() | Encodes and sends binary messages |
| `AppState.parseMessage()` | [app/StackChan/AppState.swift:117-139]() | Decodes received binary messages |
| `AppState.webSocketMessageMonitoring()` | [app/StackChan/AppState.swift:246-267]() | Registers observer and handles status messages |
| `WebSocketUtil.shared` | Referenced in AppState | Singleton managing WebSocket connection lifecycle |

### Message Flow Architecture

```mermaid
graph TB
    subgraph iOS["iOS App Layer"]
        UI["UI Views<br/>(Camera, Dance, Control)"]
        AppState["AppState<br/>Message coordination"]
        WSUtil["WebSocketUtil<br/>Connection management"]
    end
    
    subgraph Protocol["WebSocket Protocol Layer"]
        Encode["sendWebSocketMessage()<br/>Type + Length + Payload"]
        Decode["parseMessage()<br/>Extract MsgType & Data"]
    end
    
    subgraph Network["Network Transport"]
        WS["WebSocket Connection<br/>ws://server/ws?mac=XXX"]
    end
    
    subgraph Server["Go Server"]
        Handler["/ws endpoint handler"]
        Router["Message Router<br/>MAC-based forwarding"]
        Connections["Connection Pool<br/>App & Device sockets"]
    end
    
    subgraph Robot["Robot Firmware"]
        FWProtocol["Binary Protocol Handler"]
        FWLogic["Application Logic<br/>Motion, Camera, Audio"]
    end
    
    UI -->|"User actions"| AppState
    AppState -->|"MsgType + Data"| Encode
    Encode --> WSUtil
    WSUtil --> WS
    WS --> Handler
    Handler --> Router
    Router --> Connections
    Connections --> FWProtocol
    FWProtocol --> FWLogic
    
    FWLogic -->|"Status/Media"| FWProtocol
    FWProtocol --> Connections
    Connections --> Router
    Router --> Handler
    Handler --> WS
    WS --> WSUtil
    WSUtil --> Decode
    Decode --> AppState
    AppState -->|"Update state"| UI
```

**Sources:** [app/StackChan/AppState.swift:93-267](), [app/StackChan/Model/MessageModel.swift:9-39]()