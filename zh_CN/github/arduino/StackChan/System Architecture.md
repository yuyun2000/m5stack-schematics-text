StackChan System Architecture

# System Architecture

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)
- [app/README.md](app/README.md)
- [firmware/README.md](firmware/README.md)
- [server/README.md](server/README.md)

</details>



## Purpose and Scope

This document describes the overall architecture of the StackChan system, including the relationships and communication pathways between the four major components: the CoreS3 hardware platform, the ESP-IDF firmware, the iOS mobile application, and the Go backend server. This page provides a structural overview of how these components interact to create the complete StackChan robot experience.

For detailed information about specific components, see:
- Hardware specifications: [Hardware & Robot](#3)
- Firmware development: [Firmware Development](#4)
- iOS application implementation: [iOS Application](#5)
- Backend server APIs: [Backend Server](#6)
- Communication protocol details: [Communication Protocols](#7)

## Component Overview

The StackChan system is a distributed architecture consisting of four primary components operating across three physical deployment targets:

| Component | Technology | Deployment Target | Primary Responsibilities |
|-----------|-----------|-------------------|-------------------------|
| **CoreS3 Hardware** | ESP32-S3 SoC | StackChan Robot | Physical sensors, actuators, processing |
| **Firmware** | ESP-IDF v5.5.1 (C/C++) | ESP32-S3 Flash Memory | Real-time control, expression engine, communication |
| **iOS App** | Swift/SwiftUI | iPhone/iPad (iOS 16.6+) | User interface, device control, social features |
| **Backend Server** | Go 1.24+ | Server Host | WebSocket relay, device management, persistence |

```mermaid
graph TB
    subgraph Physical["Physical Robot Hardware"]
        CoreS3["CoreS3 Module<br/>ESP32-S3 Dual-Core 240MHz<br/>16MB Flash + 8MB PSRAM"]
        Sensors["Sensors<br/>• 0.3MP Camera<br/>• 9-axis IMU<br/>• Proximity<br/>• Dual Mics"]
        Actuators["Actuators<br/>• 2 Servos<br/>• 12 RGB LEDs<br/>• 1W Speaker<br/>• IR TX/RX"]
        IO["I/O Devices<br/>• Touch Display<br/>• Touch Panel<br/>• Buttons<br/>• NFC"]
    end
    
    subgraph FW["Embedded Firmware Layer"]
        ESPIDF["ESP-IDF v5.5.1<br/>FreeRTOS"]
        Drivers["Hardware Drivers<br/>Servo/Audio/Camera/Network"]
        AppLogic["Application Logic<br/>Expression Engine<br/>XiaoZhi AI Agent<br/>Motion Control"]
    end
    
    subgraph Mobile["iOS Application"]
        AppState["AppState.swift<br/>Global State Management"]
        Models["Models/<br/>Device/Expression/Post/Message"]
        Views["Views/<br/>SwiftUI Components"]
        Network["Network/<br/>WebSocket/HTTP/Bluetooth"]
    end
    
    subgraph Backend["Go Backend Server"]
        Main["main.go<br/>HTTP Server Setup"]
        DeviceAPI["Device Management<br/>Registration/Status/Info"]
        SocialAPI["Social Features<br/>Posts/Comments/Feed"]
        WSRelay["WebSocket Hub<br/>Message Routing"]
    end
    
    CoreS3 --> Sensors
    CoreS3 --> Actuators
    CoreS3 --> IO
    
    Sensors --> Drivers
    Actuators --> Drivers
    IO --> Drivers
    Drivers --> ESPIDF
    ESPIDF --> AppLogic
    
    AppLogic -.->|"Blufi Protocol<br/>BLE Pairing"| Network
    AppLogic -.->|"WebSocket<br/>Real-time Control"| WSRelay
    
    Network --> AppState
    AppState --> Views
    Views --> Models
    
    Network -.->|"HTTP REST<br/>Device Info"| DeviceAPI
    Network -.->|"WebSocket<br/>Video/Audio/Control"| WSRelay
    
    WSRelay --> DeviceAPI
    WSRelay --> SocialAPI
```

**Sources:** [README.md:1-22](), [firmware/README.md:1-26](), [app/README.md:1-63](), [server/README.md:1-45]()

## System Topology

The StackChan system operates in a hub-and-spoke topology where the Go backend server acts as the central communication hub. All real-time interactions between iOS clients and robot hardware are mediated through WebSocket connections to the server.

```mermaid
graph LR
    subgraph Clients["Mobile Clients"]
        iOS1["iPhone 1<br/>StackChan.app"]
        iOS2["iPhone 2<br/>StackChan.app"]
        iOS3["iPhone N<br/>StackChan.app"]
    end
    
    subgraph Hub["Central Server"]
        Server["Go Server<br/>main.go<br/>Port 12800"]
        WSHub["WebSocket Hub<br/>Connection Pool"]
        DB[("Database<br/>Device/Post/Comment<br/>Persistent Storage")]
    end
    
    subgraph Robots["StackChan Robots"]
        Robot1["StackChan 1<br/>CoreS3<br/>MAC: XX:XX:XX"]
        Robot2["StackChan 2<br/>CoreS3<br/>MAC: YY:YY:YY"]
        Robot3["StackChan N<br/>CoreS3<br/>MAC: ZZ:ZZ:ZZ"]
    end
    
    iOS1 -->|"WebSocket<br/>ws://IP:12800/ws"| WSHub
    iOS2 -->|"WebSocket"| WSHub
    iOS3 -->|"WebSocket"| WSHub
    
    Robot1 -->|"WebSocket"| WSHub
    Robot2 -->|"WebSocket"| WSHub
    Robot3 -->|"WebSocket"| WSHub
    
    WSHub --> Server
    Server --> DB
    
    iOS1 -.->|"BLE Direct<br/>Initial Config Only"| Robot1
    iOS2 -.->|"BLE Direct"| Robot2
```

**Sources:** [app/README.md:42-52](), [server/README.md:8-14]()

## Hardware Layer Architecture

The hardware layer is built on the M5Stack CoreS3 module, which integrates the ESP32-S3 SoC with comprehensive sensor and actuator arrays.

```mermaid
graph TB
    subgraph ESP32["ESP32-S3 SoC"]
        Core0["Core 0<br/>240 MHz"]
        Core1["Core 1<br/>240 MHz"]
        Flash["16MB Flash<br/>Program Storage"]
        PSRAM["8MB PSRAM<br/>Runtime Memory"]
        WiFi["Wi-Fi Radio<br/>802.11 b/g/n"]
        BLE["BLE Radio<br/>Bluetooth 5.0"]
    end
    
    subgraph Peripherals["Integrated Peripherals"]
        Display["2.0\" Touch Display<br/>Capacitive"]
        Camera["0.3MP Camera<br/>Image Capture"]
        IMU["9-axis IMU<br/>Accel/Gyro/Mag"]
        Audio["Audio Subsystem<br/>1W Speaker<br/>Dual Mics"]
        Prox["Proximity Sensor"]
        SD["microSD Slot"]
    end
    
    subgraph RobotBody["Robot Body Components"]
        Servo1["Servo 1<br/>Horizontal 360°"]
        Servo2["Servo 2<br/>Vertical 90°"]
        LEDs["12 RGB LEDs<br/>2 Rows"]
        IR["IR TX/RX"]
        Touch["3-Zone Touch Panel"]
        NFC["NFC Module"]
        Battery["700mAh Battery"]
        USBC["USB-C Interface<br/>Power + Data"]
    end
    
    Core0 --> WiFi
    Core0 --> BLE
    Core1 --> Camera
    Core1 --> Audio
    
    Flash --> Core0
    PSRAM --> Core0
    
    WiFi -.-> Display
    BLE -.-> Display
    
    Core0 --> Servo1
    Core0 --> Servo2
    Core1 --> LEDs
    Core1 --> IR
    
    USBC --> Battery
    Battery --> Core0
```

**Sources:** [README.md:11-13]()

## Firmware Layer Architecture

The firmware runs on ESP-IDF v5.5.1, a FreeRTOS-based framework that provides hardware abstraction and networking capabilities.

### Firmware Build System

```mermaid
graph LR
    Source["Firmware Source<br/>C/C++ Code"]
    FetchDeps["fetch_repos.py<br/>Dependency Fetcher"]
    ESPIDF["ESP-IDF v5.5.1<br/>Build Toolchain"]
    Binary["Firmware Binary<br/>.bin Files"]
    Flash["idf.py flash<br/>USB-C Upload"]
    Hardware["CoreS3 Flash<br/>16MB Storage"]
    
    FetchDeps --> Source
    Source --> ESPIDF
    ESPIDF -->|"idf.py build"| Binary
    Binary --> Flash
    Flash --> Hardware
```

The firmware includes factory-installed features:
- Facial expression rendering and animation
- XiaoZhi AI agent integration
- Video call support via iOS app
- Device discovery for nearby StackChan robots
- Blufi protocol implementation for Wi-Fi configuration
- WebSocket client for server communication

**Sources:** [firmware/README.md:1-26](), [README.md:15-17]()

## iOS Application Layer Architecture

The iOS application is built with Swift and SwiftUI, targeting iOS 16.6 and later. It follows a centralized state management pattern.

### Application Architecture

```mermaid
graph TB
    subgraph AppCore["Application Core"]
        AppDelegate["App Entry Point<br/>SwiftUI App"]
        AppState["AppState.swift<br/>@Observable Singleton<br/>Global State Manager"]
    end
    
    subgraph DataLayer["Data Models"]
        Device["Device.swift<br/>Robot Device Info"]
        Expression["ExpressionData.swift<br/>Facial Expressions"]
        Motion["MotionData.swift<br/>Servo Control"]
        Post["Post.swift<br/>Social Posts"]
        Message["MessageModel.swift<br/>WebSocket Messages"]
    end
    
    subgraph NetworkLayer["Network Layer"]
        WSManager["WebSocketManager<br/>Real-time Comms"]
        HTTPClient["HTTP Client<br/>REST API Calls"]
        BLEManager["Bluetooth Manager<br/>Blufi Protocol"]
        Urls["Urls.swift<br/>Server Configuration"]
    end
    
    subgraph ViewLayer["View Layer"]
        MainView["ContentView<br/>Primary Interface"]
        DeviceView["Device Control Views<br/>Expression/Motion"]
        SocialView["Social Views<br/>Posts/Comments"]
        ARView["AR Views<br/>Distance Detection"]
    end
    
    AppDelegate --> AppState
    AppState --> Device
    AppState --> Expression
    AppState --> Motion
    
    AppState --> WSManager
    AppState --> HTTPClient
    AppState --> BLEManager
    
    Urls --> WSManager
    Urls --> HTTPClient
    
    Message --> WSManager
    
    MainView --> AppState
    DeviceView --> AppState
    SocialView --> AppState
    ARView --> AppState
```

### Network Configuration

The iOS app requires server IP configuration in `Network/Urls.swift`. The base URL defines the WebSocket and HTTP endpoints:

```swift
static let url = "192.168.51.24:12800/"
```

**Sources:** [app/README.md:42-52]()

## Backend Server Layer Architecture

The Go backend server provides device management, WebSocket message relay, and social features with persistent storage.

### Server Components

```mermaid
graph TB
    subgraph Entry["Server Entry Point"]
        MainGo["main.go<br/>HTTP Server Setup<br/>Port 12800"]
    end
    
    subgraph DeviceServices["Device Services"]
        DeviceReg["Device Registration<br/>POST /device"]
        DeviceInfo["Device Info Query<br/>GET /deviceInfo"]
        DeviceUpdate["Device Update<br/>POST /updateDeviceName"]
        DeviceStatus["Online/Offline Status<br/>Tracking"]
    end
    
    subgraph Communication["Communication Hub"]
        WSEndpoint["WebSocket Endpoint<br/>GET /ws?mac=XXX&id=YYY"]
        WSHub["Connection Pool<br/>Active WebSocket Map"]
        MessageRouter["Message Router<br/>Binary Protocol Handler"]
    end
    
    subgraph Social["Social Features"]
        PostCreate["Create Post<br/>POST /device-post"]
        PostList["List Posts<br/>GET /post-list"]
        CommentCreate["Create Comment<br/>POST /comment"]
        CommentList["List Comments<br/>GET /comment"]
    end
    
    subgraph Dance["Dance System"]
        DanceData["Dance Data Storage"]
        DanceControl["Dance Playback Control"]
    end
    
    subgraph Persistence["Data Persistence"]
        DB[("Relational Database<br/>Device/Post/Comment")]
    end
    
    MainGo --> WSEndpoint
    MainGo --> DeviceReg
    MainGo --> PostCreate
    
    WSEndpoint --> WSHub
    WSHub --> MessageRouter
    
    DeviceReg --> DB
    DeviceInfo --> DB
    PostCreate --> DB
    CommentCreate --> DB
    
    MessageRouter -.->|"Relay to Device"| WSHub
    MessageRouter -.->|"Relay to App"| WSHub
```

**Sources:** [server/README.md:1-45]()

## Communication Architecture

The system employs three distinct communication protocols for different interaction phases and requirements.

### Protocol Overview

| Protocol | Transport | Use Case | Connection Timing | Data Types |
|----------|-----------|----------|-------------------|------------|
| **Blufi** | Bluetooth LE | Initial device pairing, Wi-Fi credentials | Setup phase only | Configuration data |
| **WebSocket** | TCP over Wi-Fi | Real-time bidirectional control | Active session | Binary messages (video, audio, control) |
| **HTTP REST** | TCP over Wi-Fi | Device management, social features | As needed | JSON payloads |

### Communication Flow

```mermaid
sequenceDiagram
    participant User
    participant iOS as "iOS App<br/>StackChan.app"
    participant BLE as "Bluetooth LE<br/>Blufi Protocol"
    participant Robot as "StackChan Robot<br/>CoreS3 Firmware"
    participant WiFi as "Wi-Fi Network"
    participant Server as "Go Server<br/>main.go:12800"
    participant DB as "Database"
    
    Note over User,DB: Phase 1: Initial Setup
    User->>iOS: Launch app
    iOS->>BLE: Scan for devices
    BLE->>Robot: Discover via advertisement
    Robot-->>iOS: Device MAC address
    iOS->>BLE: Pair and connect
    iOS->>BLE: Send Wi-Fi credentials
    BLE->>Robot: Configure network
    Robot->>WiFi: Connect to network
    
    Note over User,DB: Phase 2: Device Registration
    Robot->>Server: HTTP POST /device
    Server->>DB: Store device info
    iOS->>Server: HTTP GET /deviceInfo?mac=XX
    Server->>DB: Query device
    DB-->>Server: Device record
    Server-->>iOS: Device details
    
    Note over User,DB: Phase 3: Real-time Session
    iOS->>Server: WebSocket /ws?mac=XX&id=YY
    Note over iOS,Server: Connection established
    Robot->>Server: WebSocket /ws?mac=XX&id=YY
    Note over Robot,Server: Connection established
    
    User->>iOS: Control expression
    iOS->>Server: WS: controlMotion message
    Server->>Robot: WS: Forward command
    Robot->>Robot: Execute servo movement
    
    Robot->>Server: WS: JPEG frame
    Server->>iOS: WS: Stream video
    iOS->>User: Display camera view
    
    Note over User,DB: Phase 4: Social Interaction
    User->>iOS: Create post
    iOS->>Server: HTTP POST /device-post
    Server->>DB: Store post
    iOS->>Server: HTTP POST /comment
    Server->>DB: Store comment
```

**Sources:** [app/README.md:42-52](), [server/README.md:8-14]()

## Data Flow Patterns

### Control Data Flow

Control commands flow from the iOS app through the server to the robot hardware:

```
User Input → iOS AppState → WebSocketManager → Server WebSocket Hub → Robot Firmware → Servo Drivers → Physical Movement
```

### Video Streaming Flow

Video data flows from the robot's camera through the server to the iOS app:

```
Camera Sensor → Firmware Image Capture → JPEG Encoding → WebSocket Binary Message → Server Relay → iOS Decoder → SwiftUI Display
```

### Device State Synchronization

Device information is synchronized through HTTP REST APIs:

```
Robot Status Update → HTTP POST /updateDeviceName → Server Database → HTTP GET /deviceInfo → iOS AppState → UI Update
```

**Sources:** [app/README.md:1-63](), [server/README.md:1-45]()

## Development and Deployment Architecture

The system supports multiple development paths and toolchains for each component.

### Build and Deployment Workflow

```mermaid
graph TB
    subgraph Dev["Development Tools"]
        Xcode["Xcode IDE<br/>Swift/SwiftUI"]
        ESPIDF_Tools["ESP-IDF v5.5.1<br/>idf.py Toolchain"]
        GoSDK["Go SDK 1.24+<br/>go build"]
        Arduino["Arduino IDE<br/>Alternative Firmware"]
        UiFlow["UiFlow2<br/>Visual Programming"]
    end
    
    subgraph Source["Source Code"]
        AppSource["app/<br/>Swift Project"]
        FirmwareSource["firmware/<br/>C/C++ Code"]
        ServerSource["server/<br/>Go Code"]
    end
    
    subgraph Build["Build Artifacts"]
        AppBinary["StackChan.app<br/>iOS Bundle"]
        FirmwareBin["firmware.bin<br/>ESP32 Binary"]
        ServerBin["StackChan<br/>Executable"]
    end
    
    subgraph Deploy["Deployment Targets"]
        iPhone["iPhone/iPad<br/>iOS 16.6+"]
        CoreS3["CoreS3 Hardware<br/>ESP32-S3 Flash"]
        ServerHost["Server Host<br/>Linux/macOS/Windows"]
    end
    
    Xcode -->|"Build & Sign"| AppSource
    ESPIDF_Tools -->|"idf.py build"| FirmwareSource
    GoSDK -->|"go build"| ServerSource
    Arduino -->|"Alternative"| FirmwareSource
    UiFlow -->|"Alternative"| FirmwareSource
    
    AppSource --> AppBinary
    FirmwareSource --> FirmwareBin
    ServerSource --> ServerBin
    
    AppBinary -->|"Xcode Install"| iPhone
    FirmwareBin -->|"idf.py flash<br/>USB-C"| CoreS3
    ServerBin -->|"Direct Execution"| ServerHost
```

### Component Dependencies

The firmware requires dependency fetching before building:

```bash
python3 ./fetch_repos.py
```

The iOS app requires server URL configuration in `Network/Urls.swift` before deployment.

The Go server requires Go 1.24+ and depends on modules managed by `go mod`.

**Sources:** [firmware/README.md:1-26](), [app/README.md:1-63](), [server/README.md:18-45]()

## Network Configuration Requirements

All three network-connected components must be configured to communicate with each other:

| Component | Configuration Location | Parameter | Default Value |
|-----------|----------------------|-----------|---------------|
| iOS App | `Network/Urls.swift` | `Urls.url` | `"192.168.51.24:12800/"` |
| Firmware | Blufi configuration | Wi-Fi SSID/Password | User-provided via BLE |
| Server | Command line | Port binding | `:12800` |

The iOS app and firmware must both point to the same server IP address and port. The firmware receives this configuration during the initial Blufi pairing process.

**Sources:** [app/README.md:42-52]()

## Security and Safety Considerations

### Motor Safety

The system includes safety warnings regarding servo operation:

> Do not forcibly rotate any movable parts connected to the motors by hand when you are unsure whether the motors are powered and under control, as this may cause hardware damage.

### Network Security

The system currently operates on local networks. The Blufi protocol handles initial Wi-Fi credential exchange over Bluetooth LE, which provides pairing-based security. WebSocket and HTTP connections operate over standard TCP without explicit encryption in the documented configuration.

### Code Signing

The iOS app requires proper code signing configuration in Xcode under "Signing & Capabilities" for deployment to physical devices. A free Apple ID is sufficient for personal development and testing.

**Sources:** [README.md:17](), [app/README.md:28-40]()