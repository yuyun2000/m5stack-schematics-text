M5Stack Hardware Testing and Validation

# Hardware Testing and Validation

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Basics/FactoryTest/FactoryTest.ino](examples/Basics/FactoryTest/FactoryTest.ino)

</details>



This document covers the comprehensive hardware testing and validation procedures for M5Stack Basic and Gray devices. The factory test suite provides systematic validation of all major hardware components including display, sensors, communication modules, storage, and input devices.

For basic usage examples without hardware validation focus, see [Basic Examples and Tutorials](#3.1). For power management implementation details, see [Power Management](#2.3).

## Purpose and Scope

The M5Stack factory test suite serves as both a manufacturing quality control tool and a diagnostic utility for developers. It provides:

- **Component Validation**: Systematic testing of display, IMU, WiFi, SD card, buttons, and power management
- **Performance Benchmarking**: Graphics performance measurement and sensor calibration verification  
- **Integration Testing**: Verification that all hardware subsystems work together correctly
- **Diagnostic Tool**: Identification of faulty components or connection issues

## Factory Test Architecture

The factory test system follows a sequential validation approach, testing each hardware subsystem independently before proceeding to integration tests.

### Test Execution Flow

```mermaid
flowchart TD
    A["setup()"] --> B["M5.begin()"]
    B --> C["Power.begin()"]
    C --> D["startupLogo()"]
    D --> E["Display Tests"]
    E --> F["Graphics Performance Tests"]
    F --> G["IMU Tests"]
    G --> H["WiFi Scan Test"]
    H --> I["SD Card Tests"]
    I --> J["loop()"]
    J --> K["Button Tests"]
    K --> L["M5.update()"]
    L --> J
    
    E --> E1["Color Fill Tests"]
    E --> E2["Brightness Control"]
    
    F --> F1["testLines()"]
    F --> F2["testFastLines()"]
    F --> F3["testRects()"]
    F --> F4["testFilledRects()"]
    F --> F5["testCircles()"]
    F --> F6["testTriangles()"]
    
    G --> G1["MPU9250 Detection"]
    G --> G2["AK8963 Detection"]
    G --> G3["IMU Initialization"]
    
    I --> I1["listDir()"]
    I --> I2["writeFile()"]
    I --> I3["readFile()"]
```

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:467-686]()

### Hardware Component Test Mapping

```mermaid
graph LR
    subgraph "M5Stack Hardware"
        ESP32["ESP32 MCU"]
        LCD["320x240 LCD Display"]
        IMU["MPU9250 + AK8963"]
        WIFI["WiFi Module"]
        SD["SD Card Slot"]
        BTN["Buttons A/B/C"]
        PWR["IP5306 Power IC"]
        SPK["Speaker/DAC"]
    end
    
    subgraph "Test Functions"
        StartupTest["startupLogo()"]
        DisplayTest["Display Tests"]
        GraphicsTest["Graphics Performance"]
        IMUTest["IMU Detection"]
        WiFiTest["wifi_test()"]
        SDTest["SD Card Tests"]
        ButtonTest["buttons_test()"]
        PowerTest["Power.begin()"]
    end
    
    LCD --> StartupTest
    SPK --> StartupTest
    LCD --> DisplayTest
    LCD --> GraphicsTest
    IMU --> IMUTest
    WIFI --> WiFiTest
    SD --> SDTest
    BTN --> ButtonTest
    PWR --> PowerTest
    ESP32 --> StartupTest
    ESP32 --> DisplayTest
    ESP32 --> IMUTest
    ESP32 --> WiFiTest
    ESP32 --> SDTest
    ESP32 --> ButtonTest
```

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:1-686]()

## Component Testing Procedures

### Display and Graphics Validation

The display testing sequence validates both basic functionality and performance characteristics:

| Test Phase | Function | Purpose | Expected Result |
|------------|----------|---------|-----------------|
| Basic Display | Color fills | Pixel functionality | Full screen colors (WHITE, RED, GREEN, BLUE, BLACK) |
| Brightness Control | `setBrightness()` | Backlight control | Smooth brightness transitions |
| Graphics Performance | `testLines()` | Line drawing speed | Performance benchmarks in microseconds |
| Shape Rendering | `testRects()`, `testCircles()`, `testTriangles()` | Geometry accuracy | Correct shape rendering |

The graphics performance tests measure rendering speed for different primitives:

```mermaid
graph TD
    A["Graphics Performance Tests"] --> B["testLines()"]
    A --> C["testFastLines()"]
    A --> D["testRects()"]
    A --> E["testFilledRects()"]
    A --> F["testCircles()"]
    A --> G["testFilledCircles()"]
    A --> H["testTriangles()"]
    A --> I["testFilledTriangles()"]
    A --> J["testRoundRects()"]
    A --> K["testFilledRoundRects()"]
    
    B --> L["Line Drawing Performance"]
    C --> M["Horizontal/Vertical Line Speed"]
    D --> N["Rectangle Outline Speed"]
    E --> O["Filled Rectangle Speed"]
    F --> P["Circle Outline Speed"]
```

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:265-455](), [examples/Basics/FactoryTest/FactoryTest.ino:517-589]()

### IMU and Motion Sensor Testing

The IMU validation tests both the accelerometer/gyroscope (MPU9250) and magnetometer (AK8963):

```mermaid
sequenceDiagram
    participant Test as "Factory Test"
    participant Wire as "I2C Bus"
    participant MPU as "MPU9250"
    participant AK as "AK8963"
    
    Test->>Wire: Wire.begin()
    Test->>MPU: readByte(WHO_AM_I_MPU9250)
    MPU->>Test: 0x71 (expected)
    Test->>MPU: initMPU9250()
    MPU->>Test: Initialization complete
    Test->>AK: readByte(WHO_AM_I_AK8963)
    AK->>Test: 0x48 (expected)
    Test->>Test: Display results on LCD
```

The test validates sensor presence and communication:
- **MPU9250 Detection**: Reads WHO_AM_I register, expects `0x71`
- **AK8963 Detection**: Reads WHO_AM_I register, expects `0x48`
- **Initialization**: Configures sensors for active data mode

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:613-658]()

### WiFi Connectivity Testing

The WiFi test performs a network scan to validate radio functionality:

```mermaid
flowchart TD
    A["wifi_test()"] --> B["WiFi.mode(WIFI_STA)"]
    B --> C["WiFi.disconnect()"]
    C --> D["WiFi.scanNetworks()"]
    D --> E{"Networks Found?"}
    E -->|Yes| F["Display Network List"]
    E -->|No| G["Display 'no networks found'"]
    F --> H["For each network"]
    H --> I["Display SSID, RSSI, Security"]
    I --> J["utf8ascii() conversion"]
    J --> K["Output to LCD and Serial"]
```

The scan results include:
- Network count
- SSID names (with UTF-8 to ASCII conversion)
- Signal strength (RSSI)
- Security status (open/encrypted)

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:182-225](), [examples/Basics/FactoryTest/FactoryTest.ino:605-664]()

### SD Card Storage Testing

The SD card validation performs file system operations to verify storage functionality:

| Operation | Function | Test Purpose |
|-----------|----------|--------------|
| Directory Listing | `listDir()` | File system access |
| File Writing | `writeFile()` | Write capability |
| File Reading | `readFile()` | Read capability |

```mermaid
graph LR
    A["SD Card Test"] --> B["listDir(SD, '/', 0)"]
    A --> C["writeFile(SD, '/hello.txt', 'Hello world')"]
    A --> D["readFile(SD, '/hello.txt')"]
    
    B --> E["Display directory contents"]
    C --> F["Verify write success"]
    D --> G["Display file contents"]
    
    E --> H["Output to LCD and Serial"]
    F --> H
    G --> H
```

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:50-127](), [examples/Basics/FactoryTest/FactoryTest.ino:666-673]()

### Button Input Testing

Button testing runs continuously in the main loop, detecting both quick presses and long holds:

```mermaid
graph TD
    A["buttons_test()"] --> B{"BtnA.wasReleased()"}
    A --> C{"BtnB.wasReleased()"}
    A --> D{"BtnC.wasReleased()"}
    
    B -->|True| E["Display 'A'"]
    C -->|True| F["Display 'B'"]
    D -->|True| G["Display 'C'"]
    
    A --> H{"BtnA.pressedFor(1000, 200)"}
    A --> I{"BtnB.pressedFor(1000, 200)"}
    A --> J{"BtnC.pressedFor(1000, 200)"}
    
    H -->|True| E
    I -->|True| F
    J -->|True| G
    
    E --> K["Output to LCD and Serial"]
    F --> K
    G --> K
```

The button test detects:
- Single button releases (`wasReleased()`)
- Long press events (`pressedFor(1000, 200)`)
- Outputs button identifier to both LCD and Serial

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:129-142](), [examples/Basics/FactoryTest/FactoryTest.ino:684-685]()

## Power Management Validation

Power system initialization validates the IP5306 power management IC:

```mermaid
sequenceDiagram
    participant Test as "Factory Test"
    participant M5 as "M5 Stack"
    participant Power as "IP5306 PMIC"
    
    Test->>M5: M5.begin()
    Test->>Power: M5.Power.begin()
    Note over Power: Initialize battery charging<br/>voltage and current settings
    Power->>Test: Power management ready
```

The power management test:
- Initializes the IP5306 power management IC
- Configures battery charging parameters
- Validates I2C communication with power chip (GPIO21, GPIO22)

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:478-486]()

## Startup Sequence and Audio Testing

The startup sequence tests both audio output and display synchronization:

```mermaid
flowchart TD
    A["startupLogo()"] --> B["setBrightness(0)"]
    B --> C["pushImage(M5 Logo)"]
    C --> D["Audio Playback Loop"]
    D --> E["dacWrite(SPEAKER_PIN, audio_data)"]
    E --> F["Brightness Fade In"]
    F --> G["Brightness Fade Out"]
    G --> H["Clear Screen"]
    
    D --> I["40μs delay per sample"]
    F --> J["Brightness = sample_index / 157"]
    G --> K["dacWrite for audio fade"]
```

The startup test validates:
- DAC audio output through speaker
- LCD brightness control synchronization
- Image display capabilities
- Timing accuracy for audio playback

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:22-47](), [examples/Basics/FactoryTest/FactoryTest.ino:493]()

## Test Results and Validation Criteria

### Expected Outcomes

| Component | Pass Criteria | Failure Indicators |
|-----------|---------------|-------------------|
| Display | All colors display correctly, graphics tests complete | Black screen, color distortion, test timeouts |
| IMU | MPU9250 returns 0x71, AK8963 returns 0x48 | Wrong device IDs, I2C communication failure |
| WiFi | Network scan returns available networks | Scan failure, no networks detected |
| SD Card | File operations succeed | Mount failure, read/write errors |
| Buttons | All three buttons respond to input | No response, stuck buttons |
| Audio | Startup sound plays correctly | No audio output, distorted sound |
| Power | Power IC initializes successfully | I2C communication failure |

### Diagnostic Output

The factory test provides dual output streams:
- **Serial Console**: Detailed technical information and timing data
- **LCD Display**: Visual confirmation and user-friendly status messages

Both outputs use UTF-8 to ASCII conversion for proper character display using the `utf8ascii()` function.

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:146-180]()

## Usage Instructions

1. **Flash the Factory Test**: Upload `FactoryTest.ino` to the M5Stack device
2. **Monitor Output**: Connect serial monitor at 115200 baud for detailed logs
3. **Observe LCD**: Watch the display for visual test confirmation
4. **Test Buttons**: Press buttons A, B, and C during the button test phase
5. **Verify Components**: Check that all expected hardware responses occur

The test runs automatically through all hardware components, then enters an interactive button testing loop. The comprehensive validation ensures all M5Stack hardware subsystems are functioning correctly.

Sources: [examples/Basics/FactoryTest/FactoryTest.ino:467-686]()