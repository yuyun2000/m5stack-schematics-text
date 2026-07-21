M5Stack Basic Examples and Tutorials

# Basic Examples and Tutorials

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [examples/Basics/Button/Button.ino](examples/Basics/Button/Button.ino)
- [examples/Basics/Display/Display.ino](examples/Basics/Display/Display.ino)
- [examples/Basics/HelloWorld/HelloWorld.ino](examples/Basics/HelloWorld/HelloWorld.ino)
- [examples/Basics/IMU/IMU.ino](examples/Basics/IMU/IMU.ino)
- [examples/Basics/PowerOFF/PowerOFF.ino](examples/Basics/PowerOFF/PowerOFF.ino)
- [examples/Basics/Sleep/Sleep.ino](examples/Basics/Sleep/Sleep.ino)
- [examples/Basics/Speaker/Speaker.ino](examples/Basics/Speaker/Speaker.ino)
- [examples/Basics/bmm150/bmm150.ino](examples/Basics/bmm150/bmm150.ino)

</details>



This page provides a comprehensive guide to the basic examples included in the M5Stack library, covering fundamental operations like display control, button input, speaker output, power management, and sensor integration. These examples serve as the foundation for understanding M5Stack hardware interaction and establishing development patterns.

For hardware testing and validation procedures, see [Hardware Testing and Validation](#3.2). For detailed API reference, see [API Reference and Keywords](#7.1).

## Purpose and Scope

The basic examples demonstrate core M5Stack functionality through progressively complex tutorials. They establish common patterns for hardware initialization, main loop structure, and peripheral control that are essential for all M5Stack development.

## Example Structure and Common Patterns

All M5Stack examples follow a consistent structure built around the global `M5` object and standard Arduino framework patterns.

### Core Example Architecture

```mermaid
flowchart TD
    Setup["setup() Function"] --> M5Begin["M5.begin()"]
    M5Begin --> PowerInit["M5.Power.begin()"]
    PowerInit --> HardwareInit["Hardware Initialization"]
    HardwareInit --> DisplaySetup["Display Configuration"]
    
    Loop["loop() Function"] --> M5Update["M5.update()"]
    M5Update --> ButtonCheck["Button State Checking"]
    ButtonCheck --> HardwareAction["Hardware Actions"]
    HardwareAction --> DisplayUpdate["Display Updates"]
    DisplayUpdate --> Loop
    
    subgraph "Global M5 Object"
        M5Class["M5Stack Class Instance"]
        Lcd["M5.Lcd"]
        Power["M5.Power"]
        BtnABC["M5.BtnA/B/C"]
        Speaker["M5.Speaker"]
        IMU["M5.IMU"]
    end
    
    M5Begin --> M5Class
    PowerInit --> Power
    ButtonCheck --> BtnABC
    HardwareAction --> Lcd
    HardwareAction --> Speaker
    HardwareAction --> IMU
```

Sources: [examples/Basics/HelloWorld/HelloWorld.ino:19-27](), [examples/Basics/PowerOFF/PowerOFF.ino:19-21](), [examples/Basics/Speaker/Speaker.ino:46-48]()

### Standard Initialization Pattern

Every M5Stack example begins with the same initialization sequence:

| Step | Function Call | Purpose |
|------|---------------|---------|
| 1 | `M5.begin()` | Initialize core M5Stack hardware |
| 2 | `M5.Power.begin()` | Initialize power management system |
| 3 | Display setup | Configure LCD properties |
| 4 | Hardware-specific init | Initialize sensors, peripherals |

Sources: [examples/Basics/HelloWorld/HelloWorld.ino:20-21](), [examples/Basics/Button/Button.ino:21-22](), [examples/Basics/IMU/IMU.ino:35-38]()

## Fundamental Hardware Control Examples

### Hello World - Basic Display Output

The simplest example demonstrates basic initialization and text display using the `M5.Lcd` interface.

```mermaid
flowchart LR
    HelloWorld["HelloWorld.ino"] --> M5Begin["M5.begin()"]
    M5Begin --> PowerBegin["M5.Power.begin()"]
    PowerBegin --> LcdPrint["M5.Lcd.print()"]
    
    subgraph "M5.Lcd Methods"
        Print["print()"]
        SetTextSize["setTextSize()"]
        SetCursor["setCursor()"]
        FillScreen["fillScreen()"]
    end
    
    LcdPrint --> Print
```

Sources: [examples/Basics/HelloWorld/HelloWorld.ino:25]()

### Button Input Handling

The button example demonstrates the M5Stack button API with different press detection methods.

```mermaid
flowchart TD
    ButtonExample["Button.ino"] --> M5Update["M5.update()"]
    M5Update --> ButtonCheck{"Button State Check"}
    
    ButtonCheck --> BtnACheck["M5.BtnA.wasReleased()"]
    ButtonCheck --> BtnBCheck["M5.BtnB.wasReleased()"]
    ButtonCheck --> BtnCCheck["M5.BtnC.wasReleased()"]
    ButtonCheck --> BtnBLong["M5.BtnB.wasReleasefor(700)"]
    
    BtnACheck --> PrintA["M5.Lcd.print('A')"]
    BtnBCheck --> PrintB["M5.Lcd.print('B')"]
    BtnCCheck --> PrintC["M5.Lcd.print('C')"]
    BtnBLong --> ClearScreen["M5.Lcd.clear(WHITE)"]
    
    subgraph "Button API Methods"
        WasReleased["wasReleased()"]
        WasPressed["wasPressed()"]
        PressedFor["pressedFor(ms, repeat)"]
        WasReleaseFor["wasReleasefor(ms)"]
    end
```

Sources: [examples/Basics/Button/Button.ino:42-54]()

### Speaker Audio Output

The speaker example shows audio generation using frequency-based tone control.

```mermaid
flowchart LR
    SpeakerExample["Speaker.ino"] --> FrequencyDefs["Frequency Definitions"]
    FrequencyDefs --> ButtonInput["Button Input Handling"]
    ButtonInput --> SpeakerControl["Speaker Control"]
    
    subgraph "Note Frequencies"
        NoteDH2["NOTE_DH2 = 661"]
        NoteDH7["NOTE_DH7 = 112"]
        NoteD0["NOTE_D0 = -1"]
    end
    
    subgraph "M5.Speaker Methods"
        Tone["tone(frequency, duration)"]
        ToneContinuous["tone(frequency)"]
        End["end()"]
    end
    
    SpeakerControl --> Tone
    SpeakerControl --> ToneContinuous
    SpeakerControl --> End
```

Sources: [examples/Basics/Speaker/Speaker.ino:15-41](), [examples/Basics/Speaker/Speaker.ino:63-72]()

### Display Graphics and Colors

The display example demonstrates comprehensive LCD control including colors, shapes, and text formatting.

```mermaid
flowchart TD
    DisplayExample["Display.ino"] --> ColorSequence["Color Fill Sequence"]
    ColorSequence --> TextDisplay["Text Display"]
    TextDisplay --> ShapeDrawing["Shape Drawing"]
    ShapeDrawing --> RandomLoop["Random Animation Loop"]
    
    subgraph "M5.Lcd Color Methods"
        FillScreen["fillScreen(color)"]
        SetTextColor["setTextColor(color)"]
        SetBgColor["Background Color"]
    end
    
    subgraph "M5.Lcd Shape Methods"
        DrawRect["drawRect(x,y,w,h,color)"]
        FillRect["fillRect(x,y,w,h,color)"]
        DrawCircle["drawCircle(x,y,r,color)"]
        FillCircle["fillCircle(x,y,r,color)"]
        DrawTriangle["drawTriangle(x1,y1,x2,y2,x3,y3,color)"]
        FillTriangle["fillTriangle(x1,y1,x2,y2,x3,y3,color)"]
    end
    
    ColorSequence --> FillScreen
    TextDisplay --> SetTextColor
    ShapeDrawing --> DrawRect
    ShapeDrawing --> FillRect
    ShapeDrawing --> DrawCircle
    ShapeDrawing --> FillCircle
    ShapeDrawing --> DrawTriangle
    ShapeDrawing --> FillTriangle
```

Sources: [examples/Basics/Display/Display.ino:22-61](), [examples/Basics/Display/Display.ino:68-74]()

## Power Management Examples

### Basic Power Control

The PowerOFF example demonstrates essential power management features including sleep modes and shutdown.

```mermaid
flowchart TD
    PowerExample["PowerOFF.ino"] --> LightSleep["Light Sleep Demo"]
    LightSleep --> ShutdownDemo["Shutdown Demo"]
    
    subgraph "M5.Power Methods"
        LightSleepFunc["lightSleep(SLEEP_SEC(5))"]
        PowerOFFFunc["powerOFF()"]
        BeginFunc["begin()"]
    end
    
    subgraph "Sleep Macros"
        SleepSec["SLEEP_SEC(seconds)"]
        SleepMs["SLEEP_MS(milliseconds)"]
    end
    
    LightSleep --> LightSleepFunc
    LightSleep --> SleepSec
    ShutdownDemo --> PowerOFFFunc
```

Sources: [examples/Basics/PowerOFF/PowerOFF.ino:29-31](), [examples/Basics/PowerOFF/PowerOFF.ino:45-47]()

### Advanced Sleep Management

The Sleep example shows comprehensive power state management with wake-up detection.

```mermaid
flowchart TD
    SleepExample["Sleep.ino"] --> WakeupSetup["Wakeup Button Setup"]
    WakeupSetup --> PowerStateCheck["Power State Detection"]
    PowerStateCheck --> SleepModes["Sleep Mode Demonstration"]
    
    subgraph "Power State Methods"
        IsResetPower["isResetbyPowerSW()"]
        IsResetSleep["isResetbyDeepsleep()"]
        SetWakeupBtn["setWakeupButton(BUTTON_A_PIN)"]
    end
    
    subgraph "Sleep Functions"
        LightSleepTimed["lightSleep(SLEEP_SEC(10))"]
        LightSleepBtn["lightSleep(0)"]
        DeepSleep["deepSleep(0)"]
    end
    
    PowerStateCheck --> IsResetPower
    PowerStateCheck --> IsResetSleep
    WakeupSetup --> SetWakeupBtn
    SleepModes --> LightSleepTimed
    SleepModes --> LightSleepBtn
    SleepModes --> DeepSleep
```

Sources: [examples/Basics/Sleep/Sleep.ino:22-23](), [examples/Basics/Sleep/Sleep.ino:35-41](), [examples/Basics/Sleep/Sleep.ino:57-71]()

## Advanced Sensor Integration

### IMU Sensor Data Reading

The IMU example demonstrates reading and displaying motion sensor data from the built-in IMU.

```mermaid
flowchart TD
    IMUExample["IMU.ino"] --> IMUInit["M5.IMU.Init()"]
    IMUInit --> DataReading["Sensor Data Reading"]
    DataReading --> DataDisplay["Data Display"]
    
    subgraph "M5.IMU Methods"
        GetGyroData["getGyroData(&gyroX, &gyroY, &gyroZ)"]
        GetAccelData["getAccelData(&accX, &accY, &accZ)"]
        GetAhrsData["getAhrsData(&pitch, &roll, &yaw)"]
        GetTempData["getTempData(&temp)"]
    end
    
    subgraph "Data Variables"
        GyroVars["gyroX, gyroY, gyroZ"]
        AccelVars["accX, accY, accZ"]
        AhrsVars["pitch, roll, yaw"]
        TempVar["temp"]
    end
    
    DataReading --> GetGyroData
    DataReading --> GetAccelData
    DataReading --> GetAhrsData
    DataReading --> GetTempData
    
    GetGyroData --> GyroVars
    GetAccelData --> AccelVars
    GetAhrsData --> AhrsVars
    GetTempData --> TempVar
```

Sources: [examples/Basics/IMU/IMU.ino:38](), [examples/Basics/IMU/IMU.ino:55-63]()

### Magnetometer with Calibration

The BMM150 example shows advanced sensor integration with calibration procedures and data persistence.

```mermaid
flowchart TD
    BMM150Example["bmm150.ino"] --> I2CSetup["I2C Interface Setup"]
    I2CSetup --> BMM150Init["bmm150_initialization()"]
    BMM150Init --> CalibrationSystem["Calibration System"]
    CalibrationSystem --> DataReading["Magnetometer Reading"]
    
    subgraph "BMM150 Driver Functions"
        I2CRead["i2c_read()"]
        I2CWrite["i2c_write()"]
        BMM150InitFunc["bmm150_init(&dev)"]
        BMM150ReadMag["bmm150_read_mag_data(&dev)"]
    end
    
    subgraph "Calibration Functions"
        CalibrateFn["bmm150_calibrate(time)"]
        OffsetSave["bmm150_offset_save()"]
        OffsetLoad["bmm150_offset_load()"]
    end
    
    subgraph "Data Structures"
        MagOffset["mag_offset"]
        MagMax["mag_max"]
        MagMin["mag_min"]
        DevStruct["bmm150_dev dev"]
    end
    
    BMM150Init --> BMM150InitFunc
    BMM150Init --> I2CRead
    BMM150Init --> I2CWrite
    CalibrationSystem --> CalibrateFn
    CalibrationSystem --> OffsetSave
    CalibrationSystem --> OffsetLoad
    DataReading --> BMM150ReadMag
```

Sources: [examples/Basics/bmm150/bmm150.ino:53-82](), [examples/Basics/bmm150/bmm150.ino:135-172](), [examples/Basics/bmm150/bmm150.ino:84-99]()

## Example Progression Path

The examples are designed to build upon each other in complexity and demonstrate different aspects of M5Stack development:

| Example | Complexity | Key Concepts | Prerequisites |
|---------|------------|--------------|---------------|
| HelloWorld | Beginner | Basic initialization, text display | None |
| Button | Beginner | Input handling, button states | HelloWorld |
| Display | Beginner | Graphics, colors, shapes | HelloWorld |
| Speaker | Beginner | Audio output, frequency control | Button |
| PowerOFF | Intermediate | Power management, sleep modes | Button |
| Sleep | Intermediate | Advanced power states, wake detection | PowerOFF |
| IMU | Intermediate | Sensor data, real-time display | Display |
| BMM150 | Advanced | I2C communication, calibration, persistence | IMU |

### Learning Path Recommendations

```mermaid
flowchart TD
    Start["Start Here"] --> HelloWorld["HelloWorld.ino"]
    HelloWorld --> BasicIO{"Choose Path"}
    
    BasicIO --> ButtonPath["Button Input"]
    BasicIO --> DisplayPath["Display Graphics"]
    
    ButtonPath --> ButtonExample["Button.ino"]
    DisplayPath --> DisplayExample["Display.ino"]
    
    ButtonExample --> SpeakerExample["Speaker.ino"]
    DisplayExample --> SpeakerExample
    
    SpeakerExample --> PowerManagement["Power Management"]
    PowerManagement --> PowerOFFExample["PowerOFF.ino"]
    PowerOFFExample --> SleepExample["Sleep.ino"]
    
    SleepExample --> SensorPath["Sensor Integration"]
    SensorPath --> IMUExample["IMU.ino"]
    IMUExample --> BMM150Example["bmm150.ino"]
    
    BMM150Example --> Advanced["Ready for Advanced Projects"]
```

Sources: [examples/Basics/HelloWorld/HelloWorld.ino](), [examples/Basics/Button/Button.ino](), [examples/Basics/Display/Display.ino](), [examples/Basics/Speaker/Speaker.ino](), [examples/Basics/PowerOFF/PowerOFF.ino](), [examples/Basics/Sleep/Sleep.ino](), [examples/Basics/IMU/IMU.ino](), [examples/Basics/bmm150/bmm150.ino]()