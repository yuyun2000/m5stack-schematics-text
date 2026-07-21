M5Stack M5Stack Modules

# M5Stack Modules

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Modules/Base_PoE/RS_485/RS_485.ino](examples/Modules/Base_PoE/RS_485/RS_485.ino)
- [examples/Modules/COM_GPS/COM_GPS.ino](examples/Modules/COM_GPS/COM_GPS.ino)
- [examples/Modules/COM_GSM/COM_GSM.ino](examples/Modules/COM_GSM/COM_GSM.ino)
- [examples/Modules/COM_LTE-DATA/COM_LTE-DATA.ino](examples/Modules/COM_LTE-DATA/COM_LTE-DATA.ino)
- [examples/Modules/COM_LTE/COM_LTE.ino](examples/Modules/COM_LTE/COM_LTE.ino)
- [examples/Modules/LORA868_SX1276/LoRa868Duplex/LoRa868Duplex.ino](examples/Modules/LORA868_SX1276/LoRa868Duplex/LoRa868Duplex.ino)
- [examples/Modules/PLUS/PLUS.ino](examples/Modules/PLUS/PLUS.ino)
- [examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino](examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino)
- [examples/Modules/SERVO/SERVO.ino](examples/Modules/SERVO/SERVO.ino)
- [examples/Modules/SERVO2_PCA9685/SERVO2_PCA9685.ino](examples/Modules/SERVO2_PCA9685/SERVO2_PCA9685.ino)

</details>



M5Stack Modules are complex, multi-functional hardware expansion boards that extend M5Stack Core capabilities through sophisticated integrated circuits and communication protocols. Unlike the simpler M5Stack Units documented in page [4](#4), modules typically integrate multiple subsystems, require complex initialization sequences, and often implement real-time processing using FreeRTOS tasks.

This page provides an overview of M5Stack Modules architecture and integration patterns. Detailed documentation for specific module categories can be found in:
- **Communication Modules** ([5.1](#5.1)): Wireless and cellular modules with AT command processing
- **Motor Control and Robotics** ([5.2](#5.2)): Servo control and balancing robot systems  
- **Network and IoT Modules** ([5.3](#5.3)): Ethernet, GPS, and environmental sensor modules

## Module Architecture Overview

M5Stack Modules follow a layered architecture pattern that abstracts complex hardware functionality through standardized communication interfaces. The modules integrate with the M5Stack Core through UART, I2C, or SPI protocols and often implement internal state machines for autonomous operation.

```mermaid
graph TB
    subgraph "M5Stack Core"
        M5Core["M5Stack Core<br/>ESP32 Controller"]
        Serial2["Serial2 UART<br/>Pins 5,13"]
        I2C["I2C Bus<br/>Pins 21,22"]
        GPIO["GPIO Control<br/>Reset/Enable"]
    end
    
    subgraph "Communication Modules"
        LTE["COM_LTE Module<br/>Cellular Voice"]
        LTEData["COM_LTE-DATA<br/>Cellular Data"]
        GSM["COM_GSM Module<br/>2G/3G Cellular"]
        GPS["COM_GPS Module<br/>GNSS Receiver"]
        LoRa["LORA868 Module<br/>Long Range Radio"]
    end
    
    subgraph "Motor Control Modules"
        Servo12["SERVO Module<br/>12-Channel Control"]
        Servo16["SERVO2 Module<br/>16-Channel PCA9685"]
    end
    
    subgraph "Environmental Modules"
        PM25["PM2.5 Module<br/>PMSA003 Sensor"]
    end
    
    subgraph "Interface Modules"
        Plus["PLUS Module<br/>Encoder Interface"]
        PoE["Base PoE<br/>RS-485 Network"]
    end
    
    M5Core --> Serial2
    M5Core --> I2C
    M5Core --> GPIO
    
    Serial2 --> LTE
    Serial2 --> LTEData
    Serial2 --> GSM
    Serial2 --> GPS
    Serial2 --> PM25
    Serial2 --> PoE
    
    I2C --> Servo12
    I2C --> Servo16
    I2C --> Plus
    
    GPIO --> LTE
    GPIO --> LTEData
    GPIO --> GSM
```

**Sources:** [examples/Modules/COM_LTE/COM_LTE.ino:286](), [examples/Modules/SERVO/SERVO.ino:30](), [examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino:42]()

## FreeRTOS Task-Based Module Architecture

M5Stack Modules frequently implement asynchronous processing using FreeRTOS tasks to handle time-sensitive operations without blocking the main application loop. This architectural pattern is essential for communication modules that must process incoming data streams and manage command timeouts.

### Task-Based Processing Pattern

The following pattern is used across multiple module types, particularly communication modules:

```mermaid
graph TB
    subgraph "Main Loop Context"
        Application["Application Code<br/>M5.update() loop"]
        CommandAPI["Module API Functions<br/>AddMsg(), ReadStatus()"]
    end
    
    subgraph "Synchronization Layer"
        Semaphore["SemaphoreHandle_t<br/>command_list_samap"]
        CommandQueue["vector<ATCommand><br/>serial_at"]
    end
    
    subgraph "Background Task Context"
        ModuleTask["xTaskCreate()<br/>LTEModuleTask/SIM800Task"]
        StateMachine["State Machine<br/>kSendReady->kSending->kWaitforMsg"]
        HardwareIO["Serial2/I2C<br/>Hardware Communication"]
    end
    
    Application --> CommandAPI
    CommandAPI --> Semaphore
    Semaphore --> CommandQueue
    CommandQueue --> ModuleTask
    ModuleTask --> StateMachine
    StateMachine --> HardwareIO
    HardwareIO --> Semaphore
```

This architecture separates application logic from hardware communication timing, enabling non-blocking operation while maintaining deterministic response handling. Communication modules use this pattern extensively (detailed in [5.1](#5.1)), while motor control modules implement simpler synchronous patterns.

**Sources:** [examples/Modules/COM_LTE/COM_LTE.ino:68-151](), [examples/Modules/COM_LTE/COM_LTE.ino:314-316](), [examples/Modules/COM_GSM/COM_GSM.ino:67-150]()

## Module Categories and Communication Interfaces

M5Stack Modules utilize different communication protocols based on their functional requirements. The following table summarizes the primary module categories:

| Category | Example Modules | Interface | Key Features |
|----------|----------------|-----------|--------------|
| Communication | COM_LTE, COM_GSM, LoRa868 | UART (Serial2) | AT command processing, FreeRTOS tasks |
| Motor Control | SERVO, SERVO2, BALA2 | I2C, GPIO | PWM generation, multi-channel control |
| Network/IoT | Base PoE, COM_GPS, PM2.5 | UART, I2C | RS-485, NMEA parsing, sensor integration |
| Interface | PLUS Module | I2C | Rotary encoder, digital input |

Detailed documentation for each category:
- Communication module architecture and AT command processing: See [5.1](#5.1)
- Motor control systems and robotics modules: See [5.2](#5.2)  
- Network connectivity and environmental sensors: See [5.3](#5.3)

**Sources:** [examples/Modules/SERVO/SERVO.ino:20](), [examples/Modules/COM_LTE/COM_LTE.ino:286](), [examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino:42](), [examples/Modules/PLUS/PLUS.ino:19]()

## Hardware Communication Patterns

M5Stack Modules interface with the M5Stack Core through standardized communication protocols. Understanding these patterns is essential for module integration.

### UART-Based Module Communication

UART-based modules use `Serial2` with configurable TX/RX pins to accommodate different module configurations:

```mermaid
graph LR
    subgraph "M5Stack Core"
        ESP32["ESP32"]
        Serial2["Serial2 UART"]
        GPIO_Ctrl["GPIO Control Pins"]
    end
    
    subgraph "Configuration Options"
        Config1["RX:5, TX:13<br/>COM_LTE, COM_GSM"]
        Config2["RX:16, TX:17<br/>PM2.5, COM_GPS"]
        Config3["RX:5, TX:15<br/>Base PoE RS-485"]
    end
    
    subgraph "Module Hardware"
        ModemIC["Cellular Modem IC"]
        SensorIC["Sensor Interface IC"]
        RS485IC["RS-485 Transceiver"]
    end
    
    ESP32 --> Serial2
    ESP32 --> GPIO_Ctrl
    
    Serial2 --> Config1
    Serial2 --> Config2
    Serial2 --> Config3
    
    Config1 --> ModemIC
    Config2 --> SensorIC
    Config3 --> RS485IC
    
    GPIO_Ctrl --> ModemIC
```

**Sources:** [examples/Modules/COM_LTE/COM_LTE.ino:286](), [examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino:42](), [examples/Modules/Base_PoE/RS_485/RS_485.ino:23](), [examples/Modules/COM_GPS/COM_GPS.ino:31]()

### I2C-Based Module Communication

I2C modules share the standard I2C bus (SDA:21, SCL:22) and use unique addresses for device selection:

| Module | I2C Address | Data Type | Access Pattern |
|--------|-------------|-----------|----------------|
| SERVO | 0x53 | Command registers | `Wire.beginTransmission()` |
| SERVO2 (PCA9685) | 0x40 | PWM control | `Adafruit_PWMServoDriver` |
| PLUS | 0x62 | Encoder state | `Wire.requestFrom()` |

**Sources:** [examples/Modules/SERVO/SERVO.ino:20](), [examples/Modules/SERVO2_PCA9685/SERVO2_PCA9685.ino:21](), [examples/Modules/PLUS/PLUS.ino:19]()

## Module Integration Patterns

M5Stack Modules follow consistent integration patterns that enable reliable communication and error handling:

1. **Hardware Initialization**: Reset sequences using GPIO control pins
2. **Communication Setup**: Protocol-specific initialization (UART baud rates, I2C addresses)
3. **Task Management**: FreeRTOS task creation for asynchronous processing
4. **State Synchronization**: Semaphore-based resource protection
5. **Error Recovery**: Timeout handling and retry mechanisms

These patterns ensure robust operation in embedded environments while maintaining compatibility with the M5Stack ecosystem.

**Sources:** [examples/Modules/COM_LTE/COM_LTE.ino:314-316](), [examples/Modules/SERVO/SERVO.ino:24-30](), [examples/Modules/PM2.5_PMSA003/PM2.5_PMSA003.ino:39-55]()