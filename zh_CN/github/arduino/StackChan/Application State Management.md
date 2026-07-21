StackChan Application State Management

# Application State Management

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [app/StackChan/AppState.swift](app/StackChan/AppState.swift)

</details>



## Purpose and Scope

This document describes how the iOS application manages global state through the `AppState` singleton class. It covers the centralized management of device connectivity, WebSocket and Bluetooth communication, navigation state, alert presentation, AR-based distance detection, and message protocol implementation.

For information about the data structures used by AppState, see [Data Models](#5.4). For details about the overall iOS project structure, see [Project Structure](#5.2).

---

## Overview

The StackChan iOS application uses a centralized state management pattern implemented through the `AppState` class [app/StackChan/AppState.swift:19-268](). This singleton class serves as the single source of truth for application-wide state and coordinates communication between the UI layer, network services, and hardware interfaces.

The `AppState` class conforms to `ObservableObject`, allowing SwiftUI views to automatically update when published properties change. It manages five primary categories of state:

| Category | Responsibilities |
|----------|------------------|
| Device State | MAC address storage, device info, online/offline status |
| Navigation State | Navigation paths for different tabs (StackChan, Nearby, Settings) |
| Communication State | WebSocket and Bluetooth connection management |
| Alert State | Global alert presentation and user notifications |
| AR Features | Distance detection and face switching triggers |

**Sources:** [app/StackChan/AppState.swift:19-268]()

---

## AppState Singleton Architecture

The `AppState` class implements the singleton pattern to ensure a single instance manages all global state throughout the application lifecycle.

```mermaid
classDiagram
    class AppState {
        +static shared: AppState
        +static deviceId: String
        +static isRelease: Bool
        -init()
        +deviceMac: String
        +deviceInfo: Device
        +deviceIsOnline: Bool
        +blufDeviceList: [BlufiDeviceInfo]
        +showAlert: Bool
        +alertTitle: String
        +stackChanPath: [PageType]
        +nearbyPath: [PageType]
        +settingsPath: [PageType]
        +detector: DistanceDetector
        +connectWebSocket()
        +sendWebSocketMessage()
        +parseMessage() MessageModel
        +connectBulDevice()
        +startDistanceDetection()
        +getDeviceInfo()
        +updateDeviceInfo()
    }
    
    class ObservableObject {
        <<protocol>>
    }
    
    class WebSocketUtil {
        +shared: WebSocketUtil
        +connect()
        +send()
        +addObserver()
    }
    
    class BlufiUtil {
        +shared: BlufiUtil
        +startScan()
        +blufDevicesMonitoring
        +characteristicCallback
    }
    
    class DistanceDetector {
        +startDistanceDetection()
        +stopDistanceDetection()
    }
    
    class Networking {
        +shared: Networking
        +get()
        +put()
    }
    
    AppState ..|> ObservableObject
    AppState --> WebSocketUtil : "uses"
    AppState --> BlufiUtil : "uses"
    AppState --> DistanceDetector : "owns"
    AppState --> Networking : "uses"
```

### Singleton Implementation

The singleton is initialized with a private initializer and accessed through the static `shared` property [app/StackChan/AppState.swift:20-21]():

```swift
static let shared = AppState()
private init() {}
```

Additionally, a static `deviceId` property provides a unique identifier for the iOS device [app/StackChan/AppState.swift:23]():

```swift
static let deviceId = UIDevice.current.identifierForVendor?.uuidString ?? UUID().uuidString
```

**Sources:** [app/StackChan/AppState.swift:19-23]()

---

## State Categories

### Device State Management

Device state tracks the currently bound StackChan robot and its connection status.

| Property | Type | Purpose | Storage |
|----------|------|---------|---------|
| `deviceMac` | `String` | MAC address of bound device | `@AppStorage` (persistent) |
| `deviceInfo` | `Device` | Full device information | `@Published` (memory) |
| `deviceIsOnline` | `Bool` | Real-time online status | `@Published` (memory) |
| `showBindingDevice` | `Bool` | Show device binding UI | `@Published` (memory) |
| `forcedDisplayBindingDevice` | `Bool` | Force binding UI display | `@Published` (memory) |

The `deviceMac` property uses `@AppStorage` [app/StackChan/AppState.swift:36]() to persist the MAC address across app launches, ensuring the binding survives app restarts.

**Sources:** [app/StackChan/AppState.swift:36-63]()

### Navigation State Management

Navigation state is managed through three separate path arrays, one for each main tab in the application:

```mermaid
graph LR
    AppState["AppState"]
    
    StackChanTab["StackChan Tab"]
    NearbyTab["Nearby Tab"]
    SettingsTab["Settings Tab"]
    
    stackChanPath["stackChanPath: [PageType]"]
    nearbyPath["nearbyPath: [PageType]"]
    settingsPath["settingsPath: [PageType]"]
    
    PageType["PageType enum<br/>• minicryEmotion<br/>• cameraPage<br/>• dance"]
    
    AppState --> stackChanPath
    AppState --> nearbyPath
    AppState --> settingsPath
    
    StackChanTab -.-> stackChanPath
    NearbyTab -.-> nearbyPath
    SettingsTab -.-> settingsPath
    
    stackChanPath --> PageType
    nearbyPath --> PageType
    settingsPath --> PageType
```

The `PageType` enum [app/StackChan/AppState.swift:13-17]() defines the navigable page types, and each tab maintains its own navigation stack as a `@Published` array [app/StackChan/AppState.swift:38-40]().

**Sources:** [app/StackChan/AppState.swift:13-17](), [app/StackChan/AppState.swift:38-40]()

### Alert State Management

Global alert presentation is managed through three properties that work together:

```mermaid
stateDiagram-v2
    [*] --> Idle: showAlert = false
    Idle --> Presenting: presentAlert() called
    Presenting --> Idle: User dismisses
    
    note right of Presenting
        showAlert = true
        alertTitle = "..."
        alertAction = closure
    end note
```

The `presentAlert()` method [app/StackChan/AppState.swift:30-34]() provides a unified interface for triggering alerts from anywhere in the application:

```swift
func presentAlert(title: String, action: (() -> Void)? = nil)
```

**Sources:** [app/StackChan/AppState.swift:26-34](), [app/StackChan/AppState.swift:45](), [app/StackChan/AppState.swift:47]()

### Bluetooth State Management

Bluetooth device discovery state is tracked through two properties:

- `blufDeviceList`: Array of discovered Blufi devices [app/StackChan/AppState.swift:55]()
- `showDeviceWifiSet`: Controls Wi-Fi configuration UI visibility [app/StackChan/AppState.swift:58]()

A `manualShutdownTime` property [app/StackChan/AppState.swift:61]() prevents the Wi-Fi configuration popup from appearing within 5 seconds of a manual dismissal.

**Sources:** [app/StackChan/AppState.swift:55-61]()

---

## WebSocket Communication Management

### Connection Establishment

The `connectWebSocket()` method [app/StackChan/AppState.swift:93-96]() establishes a WebSocket connection to the backend server:

```mermaid
sequenceDiagram
    participant App as "AppState"
    participant WS as "WebSocketUtil.shared"
    participant Server as "Backend Server"
    
    App->>App: "connectWebSocket()"
    App->>App: "Build URL with<br/>mac, deviceType, deviceId"
    App->>WS: "connect(urlString)"
    WS->>Server: "WebSocket Handshake"
    Server-->>WS: "Connection Established"
    
    Note over App,Server: URL format:<br/>ws://server/ws?mac=XXX&deviceType=App&deviceId=YYY
```

The URL is constructed using the `Urls.getWebSocketUrl()` helper and includes:
- `mac`: The bound device's MAC address
- `deviceType`: Set to "App" to identify as mobile client
- `deviceId`: The iOS device's unique identifier

**Sources:** [app/StackChan/AppState.swift:93-96]()

### Message Sending Protocol

The `sendWebSocketMessage()` method [app/StackChan/AppState.swift:98-114]() implements the binary message protocol:

```mermaid
graph LR
    Input["Input<br/>msgType: MsgType<br/>data: Data?"]
    
    Byte1["Byte 0<br/>Message Type"]
    Bytes2_5["Bytes 1-4<br/>Payload Length<br/>(Big Endian)"]
    BytesN["Bytes 5+<br/>Payload Data"]
    
    Output["Binary Message<br/>sent via WebSocket"]
    
    Input --> Byte1
    Input --> Bytes2_5
    Input --> BytesN
    
    Byte1 --> Output
    Bytes2_5 --> Output
    BytesN --> Output
```

The message structure consists of:
1. **Byte 0**: Message type (from `MsgType` enum)
2. **Bytes 1-4**: Payload length as 32-bit big-endian integer
3. **Bytes 5+**: Optional payload data

**Sources:** [app/StackChan/AppState.swift:98-114]()

### Message Parsing

The `parseMessage()` method [app/StackChan/AppState.swift:117-139]() reverses the encoding process:

| Validation Step | Check | Action |
|----------------|-------|--------|
| Minimum Length | `message.count >= 5` | Return `(nil, nil)` if failed |
| Type Validity | `MsgType(rawValue: typeByte)` | Return `(nil, nil)` if invalid |
| Length Validity | `message.count >= 5 + dataLength` | Return `(nil, nil)` if insufficient |
| Success | All checks pass | Return `(msgType, payload)` |

The method extracts the 32-bit length by reducing bytes 1-4 [app/StackChan/AppState.swift:127-130]():

```swift
let dataLength = lengthData.reduce(0) { (result, byte) -> UInt32 in
    return (result << 8) | UInt32(byte)
}
```

**Sources:** [app/StackChan/AppState.swift:117-139]()

### Message Monitoring

The `webSocketMessageMonitoring()` method [app/StackChan/AppState.swift:246-267]() sets up an observer for incoming WebSocket messages:

```mermaid
sequenceDiagram
    participant App as "AppState"
    participant WS as "WebSocketUtil.shared"
    participant Handler as "Message Handler"
    
    App->>WS: "addObserver(for: 'App')"
    
    loop "Message Received"
        WS->>Handler: "URLSessionWebSocketTask.Message"
        
        alt "Message Type: .data"
            Handler->>App: "parseMessage(message)"
            App->>App: "Extract (MsgType, Data)"
            
            alt "MsgType.deviceOnline"
                App->>App: "deviceIsOnline = false"
            else "MsgType.deviceOffline"
                App->>App: "deviceIsOnline = true"
            end
        else "Message Type: .string"
            Handler->>Handler: "Log text message"
        end
    end
```

Note: The online/offline logic appears inverted in the implementation [app/StackChan/AppState.swift:253-257]() - when `deviceOnline` message is received, `deviceIsOnline` is set to `false`, and vice versa.

**Sources:** [app/StackChan/AppState.swift:246-267]()

---

## Bluetooth Communication Management

### Blufi Device Discovery

The `openBlufi()` method [app/StackChan/AppState.swift:226-243]() initializes Bluetooth device monitoring:

```mermaid
flowchart TD
    Start["openBlufi() called"]
    Monitor["Set blufDevicesMonitoring callback"]
    Callback["Callback triggered with<br/>discovered devices"]
    Update["Update blufDeviceList"]
    
    CheckShutdown{"manualShutdownTime<br/>exists and < 5 sec?"}
    CheckWifiSet{"showDeviceWifiSet<br/>already true?"}
    CheckEmpty{"blufDeviceList<br/>empty?"}
    ShowPopup["Set showDeviceWifiSet = true"]
    Skip["Skip popup"]
    
    Start --> Monitor
    Monitor --> Callback
    Callback --> Update
    Update --> CheckShutdown
    CheckShutdown -->|Yes| Skip
    CheckShutdown -->|No| CheckWifiSet
    CheckWifiSet -->|Yes| Skip
    CheckWifiSet -->|No| CheckEmpty
    CheckEmpty -->|No| ShowPopup
    CheckEmpty -->|Yes| Skip
```

The 5-second cooldown period [app/StackChan/AppState.swift:231-236]() prevents the Wi-Fi configuration popup from reappearing immediately after manual dismissal, improving user experience.

**Sources:** [app/StackChan/AppState.swift:226-243]()

### Blufi Device Connection

The `connectBulDevice()` method [app/StackChan/AppState.swift:65-91]() establishes a connection to a specific device by MAC address:

```mermaid
sequenceDiagram
    participant App as "AppState"
    participant Blufi as "BlufiUtil.shared"
    participant BLE as "Bluetooth Hardware"
    
    App->>App: "connectBulDevice(macAddress)"
    
    alt "Bluetooth already powered on"
        App->>Blufi: "startScan()"
    else "Bluetooth not ready"
        App->>Blufi: "Set centralManagerDidUpdateState callback"
        Note over Blufi: "Wait for .poweredOn state"
        Blufi->>Blufi: "startScan() when powered on"
    end
    
    App->>Blufi: "Set characteristicCallback"
    
    loop "For each discovered characteristic"
        Blufi->>App: "characteristicCallback(characteristic)"
        
        alt "UUID: E2E5E5E2-...-DEF0"
            App->>Blufi: "writeExpressionCharacteristic = characteristic"
            Note over App: "Expression control channel"
        else "UUID: E2E5E5E1-...-DEF0"
            App->>Blufi: "writeHeadCharacteristic = characteristic"
            Note over App: "Head motion control channel"
        end
    end
```

The method identifies and assigns two critical characteristics:
- **Expression Characteristic** (UUID ending in DEF0): Controls facial expressions [app/StackChan/AppState.swift:80-83]()
- **Head Characteristic** (UUID ending in DEF0): Controls head/servo movements [app/StackChan/AppState.swift:85-88]()

**Sources:** [app/StackChan/AppState.swift:65-91]()

---

## Distance Detection and AR Features

### DistanceDetector Integration

The `AppState` owns a `DistanceDetector` instance [app/StackChan/AppState.swift:52]() that uses ARKit for face proximity detection:

```mermaid
graph TB
    AppState["AppState"]
    Detector["detector: DistanceDetector"]
    ARKit["ARKit Framework"]
    
    Start["startDistanceDetection()"]
    Stop["stopDistanceDetection()"]
    
    DistanceUpdate["distanceUpdate callback"]
    BelowThreshold["belowThreshold callback"]
    
    ShowFace["showSwitchFace = true"]
    
    AppState --> Detector
    Detector --> ARKit
    
    AppState --> Start
    AppState --> Stop
    
    Start --> DistanceUpdate
    Start --> BelowThreshold
    
    DistanceUpdate -.->|"distance < 5cm"| ShowFace
```

### Distance Detection Lifecycle

The `startDistanceDetection()` method [app/StackChan/AppState.swift:164-179]() initiates AR-based distance monitoring:

```mermaid
stateDiagram-v2
    [*] --> Inactive
    Inactive --> Active: startDistanceDetection()
    Active --> Inactive: stopDistanceDetection()
    
    state Active {
        [*] --> Monitoring
        Monitoring --> FaceDetected: Face within 5cm
        FaceDetected --> ShowUI: Set showSwitchFace = true
        ShowUI --> Monitoring: Continue monitoring
    }
```

The distance is converted to centimeters [app/StackChan/AppState.swift:167]() and compared against a 5cm threshold [app/StackChan/AppState.swift:168]() to trigger the face switching UI.

**Sources:** [app/StackChan/AppState.swift:52](), [app/StackChan/AppState.swift:53](), [app/StackChan/AppState.swift:164-183]()

---

## Device Information Management

### Fetching Device Information

The `getDeviceInfo()` method [app/StackChan/AppState.swift:198-223]() retrieves device details from the backend server:

```mermaid
sequenceDiagram
    participant App as "AppState"
    participant Net as "Networking.shared"
    participant Server as "Backend API"
    
    App->>App: "getDeviceInfo()"
    App->>Net: "get(Urls.deviceInfo, [mac: deviceMac])"
    Net->>Server: "GET /deviceInfo?mac=XXX"
    Server-->>Net: "Response<Device>"
    Net-->>App: "Success or Failure"
    
    alt "Success with data"
        App->>App: "Decode Response<Device>"
        App->>App: "deviceInfo = response.data"
        App->>App: "newName = deviceInfo.name"
        
        alt "Device name is empty"
            App->>App: "showCjamgeNameAlert = true"
            Note over App: "Prompt user to set name"
        end
    else "Failure or parse error"
        App->>App: "Log error"
    end
```

**Sources:** [app/StackChan/AppState.swift:198-223]()

### Updating Device Information

The `updateDeviceInfo()` method [app/StackChan/AppState.swift:141-161]() persists changes to the device name:

| Step | Action | Code Reference |
|------|--------|----------------|
| 1 | Build parameter map with MAC and name | [app/StackChan/AppState.swift:142-145]() |
| 2 | Send PUT request to `/deviceInfo` | [app/StackChan/AppState.swift:146]() |
| 3 | Parse `Response<String>` | [app/StackChan/AppState.swift:150]() |
| 4 | Check `isSuccess` flag | [app/StackChan/AppState.swift:151]() |
| 5 | Log result | [app/StackChan/AppState.swift:152-158]() |

**Sources:** [app/StackChan/AppState.swift:141-161]()

---

## Message Protocol Implementation

### Message Type Enumeration

The binary protocol uses a `MsgType` enum to identify message purposes. Common message types handled by AppState include:

- `deviceOnline`: Robot came online [app/StackChan/AppState.swift:253]()
- `deviceOffline`: Robot went offline [app/StackChan/AppState.swift:255]()

For complete details on all message types, see [Message Types Reference](#7.4).

### Binary Protocol Structure

The message format implemented in `sendWebSocketMessage()` and `parseMessage()` follows this structure:

```mermaid
graph LR
    subgraph "Binary Message Format"
        B0["Byte 0<br/>MsgType.rawValue<br/>(UInt8)"]
        B1["Bytes 1-4<br/>Payload Length<br/>(UInt32 Big Endian)"]
        B2["Bytes 5+<br/>Payload<br/>(Data)"]
    end
    
    B0 --> B1
    B1 --> B2
    
    Example["Example: Control Motion<br/>0x05 0x00 0x00 0x00 0x10 [16 bytes of motion data]"]
```

This protocol ensures:
- **Type Safety**: The first byte identifies the message purpose
- **Length Prefix**: Bytes 1-4 specify payload size for proper buffering
- **Variable Payload**: Arbitrary binary data starting at byte 5

**Sources:** [app/StackChan/AppState.swift:98-114](), [app/StackChan/AppState.swift:117-139]()

---

## Summary

The `AppState` singleton provides centralized state management for the StackChan iOS application through:

1. **ObservableObject Pattern**: SwiftUI views automatically react to state changes via `@Published` properties
2. **Persistent Storage**: Device MAC address persists across app launches using `@AppStorage`
3. **WebSocket Communication**: Binary protocol implementation for real-time robot control
4. **Bluetooth Management**: Blufi protocol handling for device discovery and pairing
5. **AR Integration**: Distance detection using ARKit for proximity-based features
6. **REST API Integration**: Device information synchronization with backend server

The class acts as the primary coordination point between UI components, network services, and hardware communication layers, ensuring consistent state across the application.

**Sources:** [app/StackChan/AppState.swift:1-268]()