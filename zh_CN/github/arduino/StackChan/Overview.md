StackChan Overview

# Overview

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [README.md](README.md)

</details>



## Purpose and Scope

This document provides a high-level introduction to the StackChan system, an open-source AI desktop robot platform. It describes the system's purpose, major components, communication architecture, and key capabilities. This overview is intended for developers, contributors, and users seeking to understand how StackChan works as a complete system.

For detailed information about specific subsystems, refer to:
- Hardware specifications: [Hardware & Robot](#3)
- Firmware development: [Firmware Development](#4)
- iOS application details: [iOS Application](#5)
- Backend server implementation: [Backend Server](#6)
- Communication protocols: [Communication Protocols](#7)

**Sources:** [README.md:1-22]()

## What is StackChan

StackChan is a distributed AI desktop robot system comprising three interconnected components: an embedded ESP32-S3 robot, an iOS mobile application, and a Go backend server. The system enables real-time interaction with a physical robot through multiple communication channels, supporting features like facial expressions, motion control, video streaming, voice interaction, and social networking.

The robot uses the M5Stack CoreS3 as its main controller, powered by an ESP32-S3 SoC with a 240 MHz dual-core processor, 16MB Flash, and 8MB PSRAM. The hardware supports Wi-Fi and Bluetooth LE for connectivity.

**Sources:** [README.md:11-15]()

## System Components

### Three-Tier Architecture

```mermaid
graph TB
    subgraph "Tier 1: Embedded Robot"
        CoreS3["CoreS3 Hardware<br/>ESP32-S3 SoC<br/>Sensors & Actuators"]
        Firmware["Embedded Firmware<br/>ESP-IDF v5.5.1<br/>C/C++ Application"]
        FactoryFW["Factory Features<br/>• Expressions<br/>• XiaoZhi AI Agent<br/>• Device Discovery"]
    end
    
    subgraph "Tier 2: Mobile Client"
        iOSApp["iOS App: StackChan World<br/>Swift/SwiftUI"]
        AppState["AppState.swift<br/>Global State Manager"]
        Models["Data Models<br/>• Device.swift<br/>• ExpressionData.swift<br/>• MessageModel.swift"]
        Views["SwiftUI Views<br/>Device Control UI"]
    end
    
    subgraph "Tier 3: Backend Server"
        GoServer["Go HTTP Server<br/>main.go"]
        WebSocketHub["WebSocket Hub<br/>Message Relay"]
        DeviceAPI["Device Management<br/>REST Endpoints"]
        SocialAPI["Social Features<br/>Posts & Comments"]
        Database["Relational Database<br/>Device & Social Data"]
    end
    
    CoreS3 --> Firmware
    Firmware --> FactoryFW
    
    iOSApp --> AppState
    iOSApp --> Models
    iOSApp --> Views
    
    GoServer --> WebSocketHub
    GoServer --> DeviceAPI
    GoServer --> SocialAPI
    GoServer --> Database
    
    Firmware -.->|"BLE: Blufi Protocol"| AppState
    Firmware -.->|"WebSocket Messages"| WebSocketHub
    AppState -.->|"WebSocket Messages"| WebSocketHub
    AppState -.->|"HTTP REST"| DeviceAPI
    iOSApp -.->|"HTTP REST"| SocialAPI
    
    style CoreS3 fill:#f9f9f9
    style iOSApp fill:#f9f9f9
    style GoServer fill:#f9f9f9
```

**Sources:** [README.md:11-15]()

### Hardware Layer

The CoreS3 controller integrates:
- **Display:** 2.0-inch capacitive touch display with glass cover
- **Camera:** 0.3 MP camera for video streaming
- **Sensors:** Proximity sensor, 9-axis IMU (accelerometer, gyroscope, magnetometer)
- **Audio:** 1W speaker and dual microphones
- **Storage:** microSD card slot
- **Controls:** Power and reset buttons

The robot body includes:
- **Power:** USB-C interface, 700 mAh battery
- **Actuators:** Two feedback servos (360° horizontal rotation, 90° vertical movement)
- **Lighting:** 12 RGB LEDs arranged in two rows
- **Communication:** IR transmitter/receiver, NFC module
- **Input:** Three-zone touch panel

**Sources:** [README.md:11-13]()

### Firmware Layer

The factory firmware runs on ESP-IDF v5.5.1 and provides:
- Vivid facial expressions and motion sequences
- XiaoZhi AI agent integration
- iOS app video call support
- Device discovery for nearby StackChan robots
- Remote avatar control

The firmware supports alternative programming via Arduino IDE and UiFlow2 for custom functionality development.

**Sources:** [README.md:14-15]()

### iOS Application Layer

The StackChan World iOS app (available on the App Store) provides:
- Bluetooth LE device discovery and pairing
- Wi-Fi network configuration via Blufi protocol
- Real-time robot control (expressions, motion)
- Video and audio streaming
- Social features (posts, comments, device feed)
- AR-based distance detection

**Sources:** [README.md:19]()

### Backend Server Layer

The Go backend server implements:
- Device registration and information management
- Online/offline status tracking
- WebSocket message relay between robots and apps
- Social platform features (posts, comments, feeds)
- Dance data storage and playback control

**Sources:** High-level architecture diagrams

## Communication Architecture

The system uses three communication protocols operating over different network layers:

```mermaid
graph TB
    subgraph "Protocol Stack"
        BLE["Bluetooth LE<br/>Blufi Protocol<br/>• Device Discovery<br/>• Wi-Fi Configuration"]
        
        WebSocket["WebSocket Protocol<br/>Binary Message Format<br/>• controlMotion<br/>• controlExpression<br/>• opusAudio<br/>• jpegImage<br/>• callControl"]
        
        HTTP["HTTP REST API<br/>JSON Payloads<br/>• GET /deviceInfo<br/>• POST /deviceInfo<br/>• POST /device-post<br/>• POST /comment"]
    end
    
    subgraph "iOS Implementation"
        BluetoothUtility["BluetoothUtility.swift<br/>Blufi Client"]
        WebSocketManager["WebSocketManager in AppState<br/>WebSocket Client"]
        NetworkUtility["NetworkUtility.swift<br/>HTTP Client"]
    end
    
    subgraph "Server Implementation"
        WSHandler["WebSocket Handler<br/>go-server/main.go<br/>HandleWebSocket()"]
        HTTPHandlers["HTTP Handlers<br/>• GetDeviceInfo()<br/>• PostDeviceInfo()<br/>• CreatePost()<br/>• AddComment()"]
    end
    
    subgraph "Firmware Implementation"
        BlufiServer["Blufi Server<br/>ESP-IDF Component"]
        WSClient["WebSocket Client<br/>ESP HTTP Client"]
        HTTPClient["HTTP Client<br/>ESP HTTP Client"]
    end
    
    BLE --> BluetoothUtility
    BLE --> BlufiServer
    BluetoothUtility -.->|"Pairing & Config"| BlufiServer
    
    WebSocket --> WebSocketManager
    WebSocket --> WSHandler
    WebSocket --> WSClient
    WebSocketManager -.->|"Real-time Data"| WSHandler
    WSClient -.->|"Status Updates"| WSHandler
    
    HTTP --> NetworkUtility
    HTTP --> HTTPHandlers
    HTTP --> HTTPClient
    NetworkUtility -.->|"Device Mgmt"| HTTPHandlers
    HTTPClient -.->|"API Calls"| HTTPHandlers
    
    style BLE fill:#f9f9f9
    style WebSocket fill:#f9f9f9
    style HTTP fill:#f9f9f9
```

**Sources:** High-level architecture diagrams

### Protocol Usage Patterns

| Protocol | Purpose | Direction | Typical Message Types |
|----------|---------|-----------|----------------------|
| Bluetooth LE (Blufi) | Initial setup, Wi-Fi provisioning | iOS ↔ Robot | Device discovery, SSID/password exchange |
| WebSocket | Real-time bidirectional communication | iOS ↔ Server ↔ Robot | Motion control, video frames, audio streams, expressions |
| HTTP REST | Device and social data management | iOS → Server, Robot → Server | Device info updates, post creation, comment submission |

**Sources:** High-level architecture diagrams

## Communication Flow

```mermaid
sequenceDiagram
    participant iOS as "iOS App<br/>AppState.swift"
    participant BLE as "Bluetooth<br/>BluetoothUtility"
    participant Robot as "Robot Firmware<br/>ESP-IDF"
    participant WS as "WebSocket<br/>go-server"
    participant API as "REST API<br/>go-server"
    
    Note over iOS,Robot: Phase 1: Discovery & Configuration
    iOS->>BLE: scanForDevices()
    BLE->>Robot: BLE Scan
    Robot-->>BLE: Advertise (MAC address)
    iOS->>BLE: connectToDevice()
    iOS->>BLE: sendWiFiCredentials()
    BLE->>Robot: Blufi: SSID + Password
    Robot->>Robot: Connect to Wi-Fi
    
    Note over iOS,WS: Phase 2: Device Registration
    iOS->>API: GET /deviceInfo?mac=XXX
    API-->>iOS: Device info or 404
    iOS->>API: POST /deviceInfo (name, online)
    
    Note over iOS,Robot: Phase 3: Real-time Interaction
    iOS->>WS: WebSocket Connect<br/>ws://server/ws?mac=XXX&id=YYY
    Robot->>WS: WebSocket Connect
    
    iOS->>WS: Binary Message: controlMotion
    WS->>Robot: Forward motion command
    Robot-->>WS: Status update
    WS-->>iOS: Status feedback
    
    Robot->>WS: Binary Message: jpegImage
    WS->>iOS: Video frame
    
    Note over iOS,API: Phase 4: Social Features
    iOS->>API: POST /device-post (title, content)
    iOS->>API: POST /comment (postID, content)
    iOS->>API: GET /device-posts (feed)
```

**Sources:** High-level architecture diagrams

## Key Features and Capabilities

### Factory Firmware Features

The pre-installed firmware provides production-ready functionality:

| Feature | Description | Implementation |
|---------|-------------|----------------|
| Facial Expressions | Multiple pre-programmed expressions | Expression engine in firmware |
| XiaoZhi AI Agent | AI-powered interaction | Integrated AI agent component |
| Video Calling | iOS app video call support | Camera streaming via WebSocket |
| Device Discovery | Find nearby StackChan devices | Bluetooth LE advertising |
| Motion Control | Servo-based head movements | Servo control system with feedback |

**Sources:** [README.md:14-15]()

### iOS App Features

The StackChan World app enables:
- Device discovery and Bluetooth pairing
- Wi-Fi network configuration
- Real-time expression and motion control
- Live camera viewing
- Audio streaming and recording
- Post creation and commenting
- Device feed browsing
- AR distance detection and face switching

**Sources:** High-level architecture diagrams

### Server Features

The backend provides:
- Device registration and management
- Online/offline status tracking
- WebSocket message relay and routing
- Social platform (posts, comments, feeds)
- Dance data storage and playback
- Binary protocol handling for efficient data transfer

**Sources:** High-level architecture diagrams

## Development Approaches

StackChan supports multiple development paths:

```mermaid
graph LR
    subgraph "Firmware Development"
        ESPIDF["ESP-IDF<br/>C/C++<br/>idf.py build/flash"]
        Arduino["Arduino IDE<br/>C/C++<br/>Arduino framework"]
        UiFlow["UiFlow2<br/>Visual Programming<br/>Block-based"]
    end
    
    subgraph "iOS Development"
        Xcode["Xcode<br/>Swift/SwiftUI<br/>Standard iOS workflow"]
    end
    
    subgraph "Server Development"
        GoSDK["Go SDK 1.24+<br/>go build<br/>Standard Go tooling"]
    end
    
    ESPIDF --> FirmwareBin["Firmware Binary<br/>.bin file"]
    Arduino --> FirmwareBin
    UiFlow --> FirmwareBin
    
    Xcode --> iOSApp["StackChan.app<br/>iOS Bundle"]
    
    GoSDK --> ServerBin["Server Executable<br/>Binary"]
    
    FirmwareBin -->|"idf.py flash<br/>USB-C"| Robot["StackChan Robot"]
    iOSApp -->|"Xcode/TestFlight"| iPhone["iPhone/iPad"]
    ServerBin -->|"Deploy"| Server["Server Host"]
    
    style ESPIDF fill:#f9f9f9
    style Xcode fill:#f9f9f9
    style GoSDK fill:#f9f9f9
```

**Sources:** [README.md:15](), High-level architecture diagrams

## Safety Considerations

**Important:** Do not forcibly rotate movable parts connected to motors by hand when unsure whether motors are powered and under control. Manual rotation can cause hardware damage to the feedback servos.

**Sources:** [README.md:17]()

## External Resources

- **iOS App:** [StackChan World on App Store](https://apps.apple.com/app/stackchan-world/id6756086326)
- **Website:** [stackchan.world](https://stackchan.world/home)
- **Product Page:** [m5stack.com/stackchan](https://m5stack.com/stackchan)
- **CoreS3 Documentation:** [M5Stack CoreS3 Docs](https://docs.m5stack.com/en/core/CoreS3)

**Sources:** [README.md:19-21]()

## Repository Structure

The StackChan repository contains:
- Firmware source code and build configuration for ESP-IDF
- iOS application source code in Swift/SwiftUI
- Go server implementation
- Documentation and development guides
- Build scripts and tooling configuration

For detailed information on repository organization, see [Version Control and Project Organization](#8.4).

**Sources:** High-level architecture diagrams