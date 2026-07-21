M5GFX ESP32 I2C Bus Implementation

# ESP32 I2C Bus Implementation

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp](src/lgfx/v1/platforms/esp32/Bus_SPI.cpp)
- [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp](src/lgfx/v1/platforms/esp32/Bus_SPI.hpp)
- [src/lgfx/v1/platforms/esp32/common.cpp](src/lgfx/v1/platforms/esp32/common.cpp)
- [src/lgfx/v1/platforms/esp32/common.hpp](src/lgfx/v1/platforms/esp32/common.hpp)

</details>



This document describes the I2C bus implementation for ESP32 platforms in M5GFX. This implementation provides direct hardware register control with state machine management, bus recovery logic, and multi-threading support for I2C communication with display panels and other peripherals.

For SPI bus implementation details, see [5.3](#5.3). For general ESP32 platform features, see [5.1](#5.1).

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:840-1436](), [src/lgfx/v1/platforms/esp32/common.hpp:321-341]()

---

## Overview and Architecture

The I2C implementation resides in the `lgfx::v1::i2c` namespace and provides low-level control of ESP32's I2C peripherals. Unlike the SPI implementation which bypasses ESP-IDF drivers for performance, the I2C implementation integrates with ESP-IDF's I2C driver infrastructure while adding sophisticated state management and error recovery.

### Core Components

```mermaid
graph TB
    subgraph "Public API"
        Init["init(i2c_port)"]
        SetPins["setPins(i2c_port, sda, scl)"]
        Release["release(i2c_port)"]
        BeginWrite["beginWrite(addr, freq)"]
        WriteBytes["writeBytes(data, len)"]
        ReadBytes["readBytes(buf, len)"]
        EndTransaction["endTransaction()"]
    end
    
    subgraph "State Management"
        Context["i2c_context_t"]
        StateMachine["State Machine<br/>disconnect/write/read"]
        Mutex["FreeRTOS Semaphore"]
    end
    
    subgraph "Hardware Interface"
        DevStruct["i2c_dev_t*<br/>I2C0, I2C1"]
        FIFOReg["FIFO Registers"]
        CmdReg["Command Registers"]
        IntReg["Interrupt Registers"]
    end
    
    subgraph "Error Recovery"
        WaitAck["i2c_wait()<br/>ACK Detection"]
        BusRecovery["i2c_stop()<br/>Manual SCL/SDA<br/>Pulsing"]
        ResetPeriph["Peripheral Reset"]
    end
    
    Init --> Context
    SetPins --> Context
    Context --> StateMachine
    Context --> Mutex
    StateMachine --> DevStruct
    BeginWrite --> WaitAck
    WriteBytes --> CmdReg
    ReadBytes --> FIFOReg
    WaitAck --> BusRecovery
    EndTransaction --> WaitAck
    
    style Context fill:#f9f9f9
    style StateMachine fill:#f9f9f9
    style BusRecovery fill:#f9f9f9
```

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:971-1066](), [src/lgfx/v1/platforms/esp32/common.cpp:840-927]()

---

## Context Structure and State Management

### i2c_context_t Structure

The `i2c_context_t` structure maintains per-port state for I2C communication:

```mermaid
classDiagram
    class i2c_context_t {
        +state_t state
        +SemaphoreHandle_t mtx
        +gpio_num_t pin_scl
        +gpio_num_t pin_sda
        +uint8_t wait_ack_stage
        +bool initialized
        +uint32_t freq
        +lock(msec)
        +unlock()
        +save_reg(dev)
        +load_reg(dev)
        +setPins(dev, scl, sda)
    }
    
    class state_t {
        <<enumeration>>
        state_disconnect
        state_write
        state_read
    }
    
    i2c_context_t --> state_t : uses
    
    note for i2c_context_t "Global array: i2c_context[I2C_NUM_MAX]"
    note for state_t "Result type wraps state with error_t"
```

| Field | Type | Purpose |
|-------|------|---------|
| `state` | `cpp::result<state_t, error_t>` | Current transaction state with error tracking |
| `mtx` | `SemaphoreHandle_t` | FreeRTOS mutex for thread safety |
| `pin_scl`, `pin_sda` | `gpio_num_t` | GPIO pin assignments |
| `wait_ack_stage` | `uint8_t` | ACK wait state: 0=none, 1=after address, 2=during data |
| `initialized` | `bool` | Whether port has been initialized |
| `freq` | `uint32_t` | Current operating frequency |

The global array `i2c_context[I2C_NUM_MAX]` stores one context per I2C port (typically 2 ports on ESP32, 1 port on ESP32-C3/C6).

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:971-1066](), [src/lgfx/v1/platforms/esp32/common.cpp:1067]()

### State Transitions

```mermaid
stateDiagram-v2
    [*] --> state_disconnect
    
    state_disconnect --> state_write : beginWrite()
    state_disconnect --> state_read : beginRead()
    
    state_write --> state_write : writeBytes()
    state_write --> state_read : restart()
    state_write --> state_disconnect : endTransaction()
    state_write --> state_disconnect : error
    
    state_read --> state_disconnect : endTransaction()
    state_read --> state_disconnect : error
    
    note right of state_disconnect
        No active transaction
        Bus is idle
    end note
    
    note right of state_write
        ACK expected after each byte
        wait_ack_stage tracks position
    end note
    
    note right of state_read
        NACK sent on last byte
        No ACK checking
    end note
```

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:973-978](), [src/lgfx/v1/platforms/esp32/common.cpp:1172-1262]()

---

## Initialization and Configuration

### Pin Configuration Flow

```mermaid
sequenceDiagram
    participant User
    participant setPins
    participant release
    participant init
    participant set_pin
    participant Arduino_Wire as Arduino Wire
    participant ESPIDF as ESP-IDF I2C
    
    User->>setPins: setPins(port, sda, scl)
    setPins->>release: if pins changed
    release->>Arduino_Wire: Wire.end() [Arduino]
    release->>ESPIDF: i2c_periph_disable() [IDF]
    
    User->>init: init(port)
    init->>init: i2c_stop() - bus recovery
    
    alt Arduino Framework
        init->>Arduino_Wire: Wire.begin()
        Arduino_Wire->>ESPIDF: configures I2C peripheral
    else ESP-IDF 5.x+
        init->>ESPIDF: i2c_new_master_bus()
        init->>init: store bus_handle
    else ESP-IDF < 5.x
        init->>init: i2c_periph_enable()
    end
    
    init->>set_pin: configure GPIO matrix
    init->>init: save_reg() - backup registers
```

**Key Functions:**

- **`setPins(i2c_port, pin_sda, pin_scl)`** [common.cpp:1305-1342](): Sets GPIO pins and releases previous configuration if changed
- **`init(i2c_port)`** [common.cpp:1354-1407](): Initializes I2C peripheral, performs bus recovery
- **`set_pin(i2c_port, pin_sda, pin_scl)`** [common.cpp:1069-1091](): Configures GPIO matrix routing

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1305-1407](), [src/lgfx/v1/platforms/esp32/common.cpp:1069-1091]()

### Framework-Specific Initialization

The implementation adapts to three environments:

| Environment | Detection | Initialization Path |
|-------------|-----------|---------------------|
| **Arduino** | `#if defined(ARDUINO) && __has_include(<Wire.h>)` | Uses `Wire.begin()` / `Wire1.begin()` |
| **ESP-IDF 5.x+** | `__has_include(<driver/i2c_master.h>)` | Uses new `i2c_new_master_bus()` API |
| **ESP-IDF < 5.x** | fallback | Uses `i2c_periph_enable()` direct control |

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1372-1399]()

---

## Command Structure and Hardware Interface

### I2C Command Encoding

ESP32's I2C peripheral uses a command queue system. Commands are encoded differently across chip variants:

```mermaid
graph LR
    subgraph "ESP32 / ESP32-S2"
        CMD0_Old["i2c_cmd_start = 0<br/>i2c_cmd_write = 1<br/>i2c_cmd_read = 2<br/>i2c_cmd_stop = 3<br/>i2c_cmd_end = 4"]
    end
    
    subgraph "ESP32-S3 / C3 / C6 / P4"
        CMD0_New["i2c_cmd_start = 6<br/>i2c_cmd_write = 1<br/>i2c_cmd_read = 3<br/>i2c_cmd_stop = 2<br/>i2c_cmd_end = 4"]
    end
    
    SetCmd["i2c_set_cmd(dev, idx, opcode, byte_num, nack)"]
    
    SetCmd --> CMD0_Old
    SetCmd --> CMD0_New
```

**Command Encoding in `i2c_set_cmd()`** [common.cpp:1104-1133]():

```
Command Value = byte_num 
              | (ack_enable ? 0x100 : 0)
              | (opcode << 11)
              | (nack_flag << 10)
```

| Field | Bits | Purpose |
|-------|------|---------|
| `byte_num` | [7:0] | Number of bytes to transfer |
| `ack_en` | [8] | Enable ACK checking (for write/stop) |
| `ack_value` | [10] | NACK flag for read operations |
| `op_code` | [13:11] | Command type (start/write/read/stop/end) |

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:929-965](), [src/lgfx/v1/platforms/esp32/common.cpp:1104-1133]()

### Hardware Register Access

```mermaid
graph TB
    subgraph "Register Access Helper Functions"
        GetDev["getDev(i2c_num)<br/>returns i2c_dev_t*"]
        GetFifo["getFifoAddr(i2c_num)<br/>returns FIFO register"]
        GetRxCount["getRxFifoCount(dev)<br/>platform-specific"]
    end
    
    subgraph "i2c_dev_t Structure"
        IntRaw["int_raw<br/>Interrupt status"]
        SR["sr / status_reg<br/>FIFO counts"]
        CmdRegs["command[16]<br/>Command queue"]
        Data["data / fifo_data<br/>FIFO register"]
        Ctr["ctr<br/>Control register"]
    end
    
    GetDev --> IntRaw
    GetDev --> SR
    GetDev --> CmdRegs
    GetFifo --> Data
    GetRxCount --> SR
    
    note right of GetRxCount
        ESP32-C3: sr.rx_fifo_cnt
        ESP32-S3/C6/P4: sr.rxfifo_cnt
        Others: status_reg.rx_fifo_cnt
    end note
```

**Platform-Specific Differences:**

The implementation handles multiple chip-specific register layouts:

- **Command Register Array:** On ESP32-S3 IDF 5.x+, accessed via `dev->comd[idx].val` instead of `dev->command[idx].val` [common.cpp:1122-1132]()
- **FIFO Address:** Varies by chip - uses `getFifoAddr()` to abstract [common.cpp:934-958]()
- **Update Mechanism:** ESP32-S3+ requires `dev->ctr.conf_upgate = 1` after register changes [common.cpp:947-950]()

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:860-867](), [src/lgfx/v1/platforms/esp32/common.cpp:934-966](), [src/lgfx/v1/platforms/esp32/common.cpp:1093-1102]()

---

## Transaction Flow and ACK Detection

### Write Transaction

```mermaid
sequenceDiagram
    participant Panel as Panel Driver
    participant API as I2C API
    participant Wait as i2c_wait()
    participant Hardware as I2C Peripheral
    participant Device as I2C Device
    
    Panel->>API: beginWrite(addr, freq)
    API->>API: lock mutex
    API->>API: configure clock divider
    API->>Hardware: set START + address + W
    API->>Hardware: set trans_start = 1
    API->>API: wait_ack_stage = 1
    
    Panel->>API: writeBytes(data, len)
    API->>Wait: i2c_wait(false)
    Wait->>Hardware: check int_raw flags
    
    alt ACK received
        Hardware-->>Wait: end_detect = 1
        Wait->>Wait: wait_ack_stage = 0
        Wait-->>API: success
    else NACK or timeout
        Hardware-->>Wait: ack_err / timeout
        Wait->>Wait: i2c_stop() - force STOP
        Wait-->>API: error_t::connection_lost
    end
    
    API->>Hardware: write data to FIFO
    API->>Hardware: set WRITE command
    API->>API: wait_ack_stage = 2
    
    Panel->>API: endTransaction()
    API->>Wait: i2c_wait(true)
    Wait->>Hardware: send STOP command
    Wait->>API: unlock mutex
```

**ACK Wait Logic** [common.cpp:1172-1220]():

The `wait_ack_stage` field tracks where ACK is expected:
- **0:** Not waiting for ACK
- **1:** Waiting after address byte (initial connection)
- **2:** Waiting during data transmission

Timeout calculation adapts based on stage:
```cpp
uint32_t us_limit = (scl_period) * (1 + tx_fifo_count);
us_limit += 512 << wait_ack_stage;  // Longer timeout after address
```

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1172-1262](), [src/lgfx/v1/platforms/esp32/common.cpp:1182-1203]()

### Interrupt Flag Detection

The implementation monitors multiple interrupt flags:

| Flag | Condition | Meaning |
|------|-----------|---------|
| `I2C_ACK_ERR_INT_RAW_M` / `I2C_NACK_INT_RAW_M` | Set when NACK received | Device did not acknowledge |
| `I2C_END_DETECT_INT_RAW_M` | Set on successful completion | Transaction completed normally |
| `I2C_ARBITRATION_LOST_INT_RAW_M` | Set when bus arbitration lost | Multi-master conflict |

**Platform Variation:** ESP32 classic additionally checks SDA line directly for NACK [common.cpp:1206-1207]():
```cpp
bool flg_nack = (gpio_in(pin_sda) == 1);
```

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1179](), [src/lgfx/v1/platforms/esp32/common.cpp:1206-1213]()

---

## Bus Recovery and Error Handling

### i2c_stop() - Manual Bus Recovery

When communication errors occur, the `i2c_stop()` function [common.cpp:1135-1170]() performs manual bus recovery by bit-banging STOP conditions:

```mermaid
sequenceDiagram
    participant API as I2C API
    participant GPIO as GPIO Bit-Bang
    participant Peripheral as I2C Peripheral
    participant Bus as Physical Bus
    
    API->>GPIO: Set SDA/SCL to GPIO mode
    API->>GPIO: Set SCL output, SDA input
    
    loop Until SDA = HIGH (max 9 cycles)
        GPIO->>Bus: SCL = LOW
        GPIO->>Bus: SDA = LOW
        GPIO->>Bus: SCL = HIGH
        GPIO->>Bus: SDA = HIGH (STOP)
        GPIO->>GPIO: Check if SDA = HIGH
    end
    
    alt ESP32 (not C3)
        API->>Peripheral: periph_module_reset()
    end
    
    API->>GPIO: Restore pin configuration
```

**Recovery Process:**

1. **Switch to GPIO mode:** Configure SCL/SDA as GPIO open-drain outputs
2. **Generate clock pulses:** Send up to 9 SCL pulses to allow device to complete byte
3. **Send STOP condition:** Generate START→STOP sequence to reset bus
4. **Reset peripheral:** Call `periph_module_reset()` (except on ESP32-C3 where it causes issues)
5. **Restore configuration:** Restore original pin settings from backup

**Special Case for ESP32-C3:** The peripheral reset is skipped [common.cpp:1165-1167]() due to a bug where it causes permanent communication failure.

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1135-1170]()

### Error States and Recovery

```mermaid
graph TB
    Start["Transaction Start"]
    WriteAddr["Write Address"]
    CheckAck1["Check ACK 1"]
    WriteData["Write Data Bytes"]
    CheckAck2["Check ACK 2"]
    SendStop["Send STOP"]
    Success["Success"]
    
    Error1["NACK after Address"]
    Error2["NACK during Data"]
    Error3["Timeout"]
    
    Recovery["i2c_stop()<br/>Force STOP + Reset"]
    
    Start --> WriteAddr
    WriteAddr --> CheckAck1
    
    CheckAck1 -->|ACK| WriteData
    CheckAck1 -->|NACK| Error1
    CheckAck1 -->|Timeout| Error3
    
    WriteData --> CheckAck2
    CheckAck2 -->|ACK| SendStop
    CheckAck2 -->|NACK| Error2
    CheckAck2 -->|Timeout| Error3
    
    SendStop --> Success
    
    Error1 --> Recovery
    Error2 --> Recovery
    Error3 --> Recovery
    
    Recovery --> Start
    
    style Error1 fill:#ffcccc
    style Error2 fill:#ffcccc
    style Error3 fill:#ffcccc
    style Recovery fill:#ffffcc
```

When errors occur, the state is set to `cpp::fail(error_t::connection_lost)` and subsequent operations return this error until `endTransaction()` performs recovery.

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1215-1216](), [src/lgfx/v1/platforms/esp32/common.cpp:1222-1253]()

---

## Multi-Threading and Locking

### Mutex-Based Synchronization

Each I2C port has a FreeRTOS semaphore for thread-safe access:

```mermaid
graph TB
    subgraph "Thread A"
        A1["beginWrite()"]
        A2["writeBytes()"]
        A3["endTransaction()"]
    end
    
    subgraph "Thread B"
        B1["beginWrite()"]
        B2["writeBytes()"]
        B3["endTransaction()"]
    end
    
    subgraph "i2c_context_t"
        MTX["SemaphoreHandle_t mtx"]
        Lock["lock(portMAX_DELAY)"]
        Unlock["unlock()"]
    end
    
    A1 --> Lock
    Lock --> MTX
    A2 --> A2
    A3 --> Unlock
    Unlock --> MTX
    
    B1 -.blocked.-> Lock
    Lock -.->|after unlock| B1
    
    style MTX fill:#f9f9f9
```

**Lock Methods** [common.cpp:983-992]():

```cpp
void lock(uint32_t msec = portMAX_DELAY) {
    if (mtx == nullptr) {
        mtx = xSemaphoreCreateMutex();
    }
    xSemaphoreTake(mtx, msec);
}

void unlock(void) {
    xSemaphoreGive(mtx);
}
```

**Lock Acquisition Points:**
- Locked during `beginWrite()` / `beginRead()`
- Unlocked during `endTransaction()` or on error
- Timeout parameter allows non-blocking acquisition

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:981-992]()

### Register Backup and Restoration

The `i2c_context_t` includes register backup functionality to support temporary pin switching:

```mermaid
sequenceDiagram
    participant User
    participant Switcher as i2c_temporary_switcher_t
    participant Context as i2c_context_t
    
    User->>Switcher: construct(port, new_sda, new_scl)
    Switcher->>Context: save_reg(dev)
    Switcher->>User: [configure new pins]
    
    Note over User,Context: User code operates with new pins
    
    User->>Switcher: restore() or destruct
    Switcher->>Context: load_reg(dev)
    Switcher->>User: [restore original pins]
```

**`save_reg()` / `load_reg()`** [common.cpp:1000-1029]():

These methods backup and restore all I2C peripheral registers except the FIFO data register, enabling temporary configuration changes without losing the original setup. This is used by `i2c_temporary_switcher_t` for temporary device access.

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1000-1029](), [src/lgfx/v1/platforms/esp32/common.hpp:328-340]()

---

## Framework Integration Patterns

### Conditional Compilation Strategy

The implementation uses extensive conditional compilation to support multiple frameworks:

```mermaid
graph TB
    subgraph "Compilation Paths"
        Check1{Arduino +<br/>Wire.h?}
        Check2{ESP-IDF 5.x<br/>i2c_master.h?}
        Check3{Default<br/>ESP-IDF}
    end
    
    subgraph "Arduino Path"
        WireInit["Wire.begin()"]
        WireEnd["Wire.end()"]
        WireSetPins["Wire.setPins()"]
    end
    
    subgraph "ESP-IDF 5.x+ Path"
        NewMaster["i2c_new_master_bus()"]
        DelMaster["i2c_del_master_bus()"]
        BusHandle["i2c_master_bus_handle_t"]
    end
    
    subgraph "ESP-IDF Legacy Path"
        PeriphEnable["i2c_periph_enable()"]
        PeriphDisable["i2c_periph_disable()"]
        PeriphReset["i2c_periph_reset()"]
    end
    
    Check1 -->|Yes| WireInit
    Check1 -->|No| Check2
    Check2 -->|Yes| NewMaster
    Check2 -->|No| Check3
    Check3 --> PeriphEnable
```

**Key Compilation Guards:**

| Guard | Purpose |
|-------|---------|
| `#if defined(ARDUINO) && __has_include(<Wire.h>)` | Arduino framework support |
| `#if __has_include(<driver/i2c_master.h>)` | ESP-IDF 5.x new I2C driver |
| `#if defined(I2C_CLOCK_SRC_ATOMIC)` | ESP-IDF 5.3+ peripheral control macros |

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1035-1057](), [src/lgfx/v1/platforms/esp32/common.cpp:1372-1399](), [src/lgfx/v1/platforms/esp32/common.cpp:869-927]()

### Pin Configuration Integration

Different frameworks require different approaches to pin configuration:

```mermaid
graph LR
    SetPins["setPins(port, sda, scl)"]
    
    subgraph "Arduino"
        SetPins1["Wire.setPins(sda, scl)"]
        Begin1["Wire.begin()"]
    end
    
    subgraph "ESP-IDF 5.x+"
        SetPins2["gpio_set_level()"]
        SetPins2a["gpio_iomux_out()"]
        SetPins2b["esp_rom_gpio_connect_*()"]
    end
    
    subgraph "ESP-IDF Legacy"
        SetPins3["i2c_set_pin()"]
    end
    
    SetPins --> SetPins1
    SetPins --> SetPins2
    SetPins --> SetPins3
    
    SetPins2 --> SetPins2a
    SetPins2a --> SetPins2b
```

**Arduino Integration** [common.cpp:1035-1057]():
- Uses `Wire.setPins()` if available (ESP-IDF 4.x+)
- Falls back to `Wire.begin(sda, scl)` on older versions
- Distinguishes between `Wire` (I2C port 0) and `Wire1` (I2C port 1)

**ESP-IDF 5.x+ Integration** [common.cpp:1071-1087]():
- Direct GPIO matrix configuration via `esp_rom_gpio_connect_out_signal()` and `esp_rom_gpio_connect_in_signal()`
- Sets pull-up mode and open-drain configuration manually
- Uses `i2c_periph_signal` lookup table for signal routing

**ESP-IDF Legacy Integration** [common.cpp:1089]():
- Uses `i2c_set_pin()` convenience function
- Automatically configures pull-ups and master mode

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1069-1091](), [src/lgfx/v1/platforms/esp32/common.cpp:1035-1057]()

---

## Usage Patterns

### Basic I2C Transaction

```mermaid
sequenceDiagram
    participant Panel as Panel_M5UnitLCD
    participant I2C as i2c namespace
    participant Context as i2c_context
    participant HW as Hardware
    
    Panel->>I2C: setPins(0, 21, 22)
    I2C->>Context: store pin config
    
    Panel->>I2C: init(0)
    I2C->>Context: initialize + bus recovery
    
    Panel->>I2C: beginWrite(0x3E, 400000)
    I2C->>Context: lock()
    I2C->>HW: configure clock
    I2C->>HW: send START + address
    
    Panel->>I2C: writeBytes(data, 32)
    I2C->>HW: wait for ACK
    I2C->>HW: write to FIFO
    
    Panel->>I2C: endTransaction()
    I2C->>HW: send STOP
    I2C->>Context: unlock()
```

**Typical Usage in Panel Drivers:**

Panel drivers that use I2C (e.g., `Panel_M5UnitLCD`, `Panel_SH110x`) follow this pattern:
1. Call `i2c::init()` during initialization
2. Begin write transaction with device address and frequency
3. Write command/data bytes
4. End transaction to release the bus

**Sources:** Referenced implementation patterns from panel drivers

---

## Performance Characteristics

### Timing Constraints

The I2C implementation enforces timing based on clock divider and FIFO depth:

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| **Bus Speed** | 100kHz - 400kHz | Configurable per transaction |
| **ACK Timeout** | Dynamic | Calculated from SCL period and FIFO count |
| **Initial ACK Timeout** | `us_limit + 512` μs | After address byte |
| **Data ACK Timeout** | `us_limit + 1024` μs | During data transmission |
| **Clock Period Calculation** | `scl_high_period + scl_low_period + 16` | Hardware-specific |

**Timeout Scaling** [common.cpp:1189-1195]():
```cpp
uint32_t us_limit = (scl_period) * (1 + tx_fifo_cnt);
us_limit += 512 << wait_ack_stage;  // 512μs after address, 1024μs during data
```

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1189-1195]()

### FIFO Management

ESP32's I2C FIFO is 32 bytes deep. The implementation monitors FIFO count to determine when to wait:

```mermaid
graph LR
    Write["Write Request"]
    CheckFIFO{"FIFO Full?"}
    WaitTx["Wait for TX"]
    WriteFIFO["Write to FIFO"]
    Done["Continue"]
    
    Write --> CheckFIFO
    CheckFIFO -->|Yes| WaitTx
    CheckFIFO -->|No| WriteFIFO
    WaitTx --> WriteFIFO
    WriteFIFO --> Done
```

The `getRxFifoCount()` function [common.cpp:1093-1102]() provides platform-independent FIFO level access, abstracting register name differences across chip variants.

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:1093-1102](), [src/lgfx/v1/platforms/esp32/common.cpp:1189]()