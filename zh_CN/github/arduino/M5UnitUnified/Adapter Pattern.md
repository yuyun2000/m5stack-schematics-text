M5UnitUnified Adapter Pattern

# Adapter Pattern

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [library.json](library.json)
- [library.properties](library.properties)
- [src/googletest/test_helper.hpp](src/googletest/test_helper.hpp)
- [src/googletest/test_template.hpp](src/googletest/test_template.hpp)
- [src/m5_unit_component/adapter.cpp](src/m5_unit_component/adapter.cpp)
- [src/m5_unit_component/adapter.hpp](src/m5_unit_component/adapter.hpp)
- [src/m5_unit_component/adapter_i2c.hpp](src/m5_unit_component/adapter_i2c.hpp)
- [src/m5_unit_component/adapter_uart.cpp](src/m5_unit_component/adapter_uart.cpp)

</details>



## Purpose and Scope

This document explains the adapter pattern implementation in M5UnitUnified, which provides a unified interface for three communication protocols (I2C, GPIO/RMT, UART) while abstracting differences between Arduino and M5HAL APIs. The adapter layer enables components to communicate with hardware without knowing which underlying library (Arduino Wire, M5HAL Bus, HardwareSerial) is being used.

For information about how components use adapters, see [Component System](#3.1). For information about adapter sharing in hub topologies, see [Parent-Child Hierarchies](#3.4). For protocol-specific details, see [Communication Protocols](#4).

## Adapter Architecture Overview

The adapter pattern in M5UnitUnified uses a **pointer-to-implementation (pimpl)** idiom with runtime polymorphism. Each `Adapter` object contains a `std::shared_ptr<Adapter::Impl>` that points to a concrete implementation. This design allows:

1. **Runtime selection** between Arduino and M5HAL implementations
2. **Zero-cost abstraction** - no virtual calls in component code
3. **Adapter sharing** via `std::shared_ptr` among multiple components
4. **Implementation switching** without recompiling component code

### Adapter Class Hierarchy

```mermaid
classDiagram
    class Adapter {
        +Type type
        #shared_ptr~Impl~ _impl
        +Adapter(Type, Impl*)
        +duplicate(address) Adapter*
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class AdapterBase_Impl {
        <<abstract>>
        +readWithTransaction(data, len)* error_t
        +writeWithTransaction(data, len, stop)* error_t
    }
    
    class AdapterI2C {
        +address() uint8_t
        +setAddress(addr)
        +clock() uint32_t
        +setClock(clock)
        +scl() int16_t
        +sda() int16_t
        +duplicate(addr) Adapter*
    }
    
    class I2CImpl {
        <<abstract>>
        #_addr uint8_t
        #_clock uint32_t
        +address() uint8_t
        +setAddress(addr)
        +clock() uint32_t
        +setClock(clock)
        +duplicate(addr)* I2CImpl*
    }
    
    class WireImpl {
        -_wire* TwoWire
        -_sda int16_t
        -_scl int16_t
        +WireImpl(wire, addr, clock)
        +getWire() TwoWire*
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class BusImpl {
        -_bus* Bus
        -_access_cfg I2CMasterAccessConfig
        +BusImpl(bus, addr, clock)
        +getBus() Bus*
        +setClock(clock)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class AdapterGPIO {
        +in() int16_t
        +out() int16_t
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class GPIOImpl {
        <<abstract>>
        #_in int16_t
        #_out int16_t
    }
    
    class GPIOImplV1 {
        +GPIOImplV1(in, out)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class GPIOImplV2 {
        +GPIOImplV2(in, out)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class AdapterUART {
        +flush()
        +flushRX()
        +setTimeout(ms)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class SerialImpl {
        -_serial* HardwareSerial
        +SerialImpl(serial)
        +flush()
        +flushRX()
        +setTimeout(ms)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    Adapter o-- AdapterBase_Impl : "_impl"
    AdapterI2C --|> Adapter
    AdapterGPIO --|> Adapter
    AdapterUART --|> Adapter
    
    I2CImpl --|> AdapterBase_Impl
    WireImpl --|> I2CImpl
    BusImpl --|> I2CImpl
    AdapterI2C o-- I2CImpl : "impl()"
    
    GPIOImpl --|> AdapterBase_Impl
    GPIOImplV1 --|> GPIOImpl
    GPIOImplV2 --|> GPIOImpl
    AdapterGPIO o-- GPIOImpl
    
    SerialImpl --|> AdapterBase_Impl
    AdapterUART o-- SerialImpl
```

**Sources:** [src/m5_unit_component/adapter_base.hpp](), [src/m5_unit_component/adapter_i2c.hpp:25-247](), [src/m5_unit_component/adapter_uart.hpp](), [src/m5_unit_component/adapter_gpio_v1.hpp](), [src/m5_unit_component/adapter_gpio_v2.hpp]()

## Adapter Type System

The `Adapter` base class defines three communication types via an enumeration:

| Type | Protocol | Use Case |
|------|----------|----------|
| `Adapter::Type::I2C` | I2C bus communication | Sensors with I2C interface (SCD40, SHT30, ADS1115, etc.) |
| `Adapter::Type::GPIO` | GPIO with RMT peripheral | Units requiring pulse timing (WS2812, DHT11/22, etc.) |
| `Adapter::Type::UART` | Serial UART communication | Units with serial interface (GPS, fingerprint readers, etc.) |

The type is stored in each `Adapter` instance and can be queried via the `type()` method. This allows components to verify they received the correct adapter type during initialization.

**Sources:** [src/m5_unit_component/adapter_base.hpp]()

## I2C Adapter Implementation Selection

The `AdapterI2C` class provides dual implementation paths that are selected at construction time based on the parameter type passed by the application.

### I2C Implementation Selection Logic

```mermaid
graph TB
    UserCode["User Code"]
    
    UnitUnified["UnitUnified::add()"]
    
    CheckParam{"Parameter<br/>Type?"}
    
    CreateWire["new AdapterI2C(Wire, addr, clock)<br/>↓<br/>new WireImpl(wire, addr, clock)"]
    
    CreateBus["new AdapterI2C(bus, addr, clock)<br/>↓<br/>new BusImpl(bus, addr, clock)"]
    
    WireImpl["WireImpl"]
    WireAPI["Arduino TwoWire API<br/>wire->beginTransmission(addr)<br/>wire->write(data, len)<br/>wire->endTransmission(stop)<br/>wire->requestFrom(addr, len)<br/>wire->read()"]
    
    BusImpl["BusImpl"]
    BusAPI["M5HAL Bus API<br/>bus->readWithTransaction(cfg, data, len)<br/>bus->writeWithTransaction(cfg, data, len, stop)"]
    
    I2CHardware["I2C Hardware<br/>Peripheral"]
    
    UserCode -->|"Units.add(unit, Wire)"| UnitUnified
    UserCode -->|"Units.add(unit, bus)"| UnitUnified
    
    UnitUnified --> CheckParam
    
    CheckParam -->|"TwoWire&"| CreateWire
    CheckParam -->|"Bus*"| CreateBus
    
    CreateWire --> WireImpl
    CreateBus --> BusImpl
    
    WireImpl --> WireAPI
    BusImpl --> BusAPI
    
    WireAPI --> I2CHardware
    BusAPI --> I2CHardware
```

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:101-136](), [src/m5_unit_component/adapter_i2c.hpp:139-171](), [src/m5_unit_component/adapter_i2c.hpp:174-179]()

### WireImpl: Arduino TwoWire Implementation

The `WireImpl` class wraps Arduino's `TwoWire` interface. It stores a pointer to the `TwoWire` instance and captures the SDA/SCL pin numbers during construction.

**Key Methods:**
- `WireImpl(TwoWire& wire, uint8_t addr, uint32_t clock)` - Constructor captures wire reference and pin numbers
- `readWithTransaction(uint8_t* data, size_t len)` - Performs `requestFrom()` and `read()` operations
- `writeWithTransaction(const uint8_t* data, size_t len, uint32_t stop)` - Performs `beginTransmission()`, `write()`, and `endTransmission()`
- `writeWithTransaction(uint8_t reg, ...)` - Overloads for register-based writes
- `duplicate(uint8_t addr)` - Creates new `WireImpl` with different address but same wire instance

**Implementation Details:**
The `writeWithTransaction()` methods use a helper function `write_with_transaction()` that handles the Arduino I2C transaction sequence. The `stop` parameter controls whether a STOP condition is sent, enabling repeated-start sequences.

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:101-136](), [src/m5_unit_component/adapter_i2c.cpp]()

### BusImpl: M5HAL Bus Implementation

The `BusImpl` class wraps M5HAL's `Bus` interface, storing a pointer to the `Bus` and maintaining an `I2CMasterAccessConfig` structure for each transaction.

**Key Methods:**
- `BusImpl(m5::hal::bus::Bus* bus, uint8_t addr, uint32_t clock)` - Constructor initializes access configuration
- `setClock(uint32_t clock)` - Updates both `_clock` and `_access_cfg.freq`
- `readWithTransaction(uint8_t* data, size_t len)` - Calls `bus->readWithTransaction(cfg, data, len)`
- `writeWithTransaction(const uint8_t* data, size_t len, uint32_t stop)` - Calls `bus->writeWithTransaction(cfg, data, len, stop)`
- `duplicate(uint8_t addr)` - Creates new `BusImpl` with different address but same bus instance

**Implementation Details:**
The `_access_cfg` structure is populated with the device address and clock frequency during construction. Each transaction method passes this configuration to the underlying M5HAL Bus methods.

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:139-171](), [src/m5_unit_component/adapter_i2c.cpp]()

### I2C Adapter Duplication Mechanism

Both implementations support the `duplicate(uint8_t addr)` method, which creates a new adapter instance sharing the same underlying hardware (Wire or Bus) but with a different I2C address. This is essential for components that need to communicate with multiple devices on the same bus or for hub devices that manage child components.

```mermaid
sequenceDiagram
    participant Component as "Component"
    participant Adapter as "AdapterI2C"
    participant Impl as "WireImpl/BusImpl"
    participant NewImpl as "New WireImpl/BusImpl"
    
    Component->>Adapter: duplicate(newAddr)
    Adapter->>Impl: duplicate(newAddr)
    
    alt WireImpl
        Impl->>NewImpl: new WireImpl(same wire, newAddr, same clock)
    else BusImpl
        Impl->>NewImpl: new BusImpl(same bus, newAddr, same clock)
    end
    
    NewImpl-->>Impl: return new impl
    Impl-->>Adapter: return new impl
    Adapter->>Adapter: Create new AdapterI2C with new impl
    Adapter-->>Component: return new adapter
    
    Note over Component,NewImpl: Both adapters share same Wire/Bus hardware
```

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:80-83](), [src/m5_unit_component/adapter_i2c.cpp]()

## GPIO Adapter Implementation Selection

The `AdapterGPIO` class provides dual implementation paths selected at **compile time** based on the ESP-IDF version. The selection is controlled by conditional compilation directives in [src/m5_unit_component/adapter.hpp:17-21]().

### GPIO Version Detection and Selection

```mermaid
graph LR
    CompileTime["Compile Time"]
    
    VersionCheck{"M5_UNIT_UNIFIED_USING_RMT_V2<br/>defined?"}
    
    IncludeV2["#include adapter_gpio_v2.hpp"]
    IncludeV1["#include adapter_gpio_v1.hpp"]
    
    GPIOImplV2["GPIOImplV2<br/>ESP-IDF 5.x RMT API<br/>rmt_new_tx_channel()<br/>rmt_new_rx_channel()<br/>rmt_transmit()<br/>rmt_receive()"]
    
    GPIOImplV1["GPIOImplV1<br/>ESP-IDF 4.x RMT API<br/>rmt_config()<br/>rmt_driver_install()<br/>rmt_write_items()<br/>rmt_read_items()"]
    
    RMTHardware["RMT Peripheral<br/>Pulse Timing"]
    
    CompileTime --> VersionCheck
    
    VersionCheck -->|"Yes"| IncludeV2
    VersionCheck -->|"No"| IncludeV1
    
    IncludeV2 --> GPIOImplV2
    IncludeV1 --> GPIOImplV1
    
    GPIOImplV2 --> RMTHardware
    GPIOImplV1 --> RMTHardware
```

**Sources:** [src/m5_unit_component/adapter.hpp:17-21](), [src/m5_unit_component/adapter_gpio_v1.hpp](), [src/m5_unit_component/adapter_gpio_v2.hpp]()

### GPIO Implementation Characteristics

| Implementation | ESP-IDF Version | RMT API Style | Channel Management |
|----------------|-----------------|---------------|-------------------|
| `GPIOImplV1` | 4.x and earlier | Legacy driver API | Static channel allocation |
| `GPIOImplV2` | 5.x and later | New driver API | Dynamic handle-based allocation |

Both implementations provide the same interface to components:
- `readWithTransaction(uint8_t* data, size_t len)` - Read pulse timing data via RMT
- `writeWithTransaction(const uint8_t* data, size_t len, uint32_t stop)` - Write pulse timing data via RMT
- `in()` - Return input GPIO pin number
- `out()` - Return output GPIO pin number

For detailed information about RMT version handling, see [ESP-IDF Version Handling](#10.2).

**Sources:** [src/m5_unit_component/adapter_gpio_v1.hpp](), [src/m5_unit_component/adapter_gpio_v2.hpp]()

## UART Adapter Implementation

The `AdapterUART` class provides a single implementation path using Arduino's `HardwareSerial` interface through the `SerialImpl` class.

### SerialImpl: HardwareSerial Wrapper

```mermaid
classDiagram
    class AdapterUART {
        +AdapterUART(serial)
        +flush()
        +flushRX()
        +setTimeout(ms)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class SerialImpl {
        -_serial* HardwareSerial
        +SerialImpl(serial)
        +flush()
        +flushRX()
        +setTimeout(ms)
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len, stop) error_t
    }
    
    class HardwareSerial {
        <<Arduino>>
        +write(data, len) size_t
        +readBytes(data, len) size_t
        +flush()
        +setTimeout(ms)
        +available() int
        +read() int
    }
    
    AdapterUART o-- SerialImpl : "_impl"
    SerialImpl --> HardwareSerial : "_serial"
```

**Key Methods:**
- `SerialImpl(HardwareSerial& serial)` - Constructor stores reference to serial instance
- `readWithTransaction(uint8_t* data, size_t len)` - Calls `serial->readBytes(data, len)` with timeout
- `writeWithTransaction(const uint8_t* data, size_t len, uint32_t stop)` - Calls `serial->write(data, len)` (stop parameter unused)
- `flush()` - Waits for transmission to complete via `serial->flush()`
- `flushRX()` - Discards all pending received data
- `setTimeout(uint32_t ms)` - Sets read timeout for blocking operations

**Implementation Details:**
The `readWithTransaction()` method returns `error_t::OK` if the expected number of bytes was read, or `error_t::TIMEOUT_ERROR` if fewer bytes were received. The `stop` parameter in `writeWithTransaction()` is ignored since UART has no equivalent to I2C STOP conditions.

**Sources:** [src/m5_unit_component/adapter_uart.hpp](), [src/m5_unit_component/adapter_uart.cpp:25-62]()

## Transaction-Based Communication Pattern

All adapter implementations follow a **transaction-based pattern** where read and write operations are atomic, self-contained operations. This design simplifies error handling and enables protocol-level abstractions.

### Transaction Method Signatures

```mermaid
graph TB
    subgraph "Read Transaction"
        ReadMethod["error_t readWithTransaction(uint8_t* data, size_t len)"]
        ReadDesc["Reads len bytes into data buffer<br/>Returns OK or error code"]
    end
    
    subgraph "Write Transaction"
        WriteMethod1["error_t writeWithTransaction(const uint8_t* data, size_t len, uint32_t stop)"]
        WriteMethod2["error_t writeWithTransaction(uint8_t reg, const uint8_t* data, size_t len, uint32_t stop)"]
        WriteMethod3["error_t writeWithTransaction(uint16_t reg, const uint8_t* data, size_t len, uint32_t stop)"]
        WriteDesc["Writes len bytes from data buffer<br/>Optional register address prefix<br/>stop controls I2C STOP condition<br/>Returns OK or error code"]
    end
    
    subgraph "Special Transactions"
        GeneralCall["error_t generalCall(const uint8_t* data, size_t len)"]
        Wakeup["error_t wakeup()"]
        SpecialDesc["generalCall: I2C broadcast to address 0x00<br/>wakeup: Sends wakeup pulse"]
    end
    
    ReadMethod --> ReadDesc
    WriteMethod1 --> WriteDesc
    WriteMethod2 --> WriteDesc
    WriteMethod3 --> WriteDesc
    GeneralCall --> SpecialDesc
    Wakeup --> SpecialDesc
```

**Sources:** [src/m5_unit_component/adapter_base.hpp](), [src/m5_unit_component/adapter_i2c.hpp:118-127]()

### Error Handling

All transaction methods return `m5::hal::error::error_t` values:

| Error Code | Meaning | Common Causes |
|------------|---------|---------------|
| `OK` | Transaction completed successfully | - |
| `TIMEOUT_ERROR` | Transaction timed out | Device not responding, incorrect address, bus conflict |
| `NACK_ERROR` | Device sent NACK | Invalid register address, device busy |
| `BUS_ERROR` | Bus error condition | SDA/SCL line stuck, electrical issue |
| `UNKNOWN_ERROR` | Unspecified error | Implementation-specific failure |

Components check the return value of transaction methods and handle errors appropriately, typically by setting their `_updated` flag to false and returning early from `update()`.

**Sources:** [src/m5_unit_component/adapter_base.hpp](), M5HAL library

## Adapter Lifecycle and Ownership

Adapters are managed through `std::shared_ptr<Adapter>` to enable sharing among multiple components, particularly in hub topologies where child components share their parent's adapter.

### Adapter Creation and Assignment Flow

```mermaid
sequenceDiagram
    participant App as "Application"
    participant Units as "UnitUnified"
    participant Component as "Component"
    participant Adapter as "Adapter"
    
    App->>Units: add(component, Wire/Bus/Serial)
    
    alt Component has no adapter yet
        Units->>Adapter: Create new Adapter(Wire/Bus/Serial)
        Adapter-->>Units: shared_ptr<Adapter>
        Units->>Component: assign(shared_ptr)
        Component->>Component: _adapter = shared_ptr
    else Component already has adapter
        Note over Units,Component: Skip adapter assignment
    end
    
    App->>Units: begin()
    Units->>Component: begin()
    Component->>Adapter: readWithTransaction() / writeWithTransaction()
    
    Note over Component,Adapter: shared_ptr enables multiple components<br/>to share same adapter instance
```

**Sources:** [src/m5_unit_component/component.hpp](), [src/m5_unit_component/unit_unified.hpp]()

### Adapter Sharing in Parent-Child Relationships

When components form parent-child hierarchies (e.g., hub with attached sensors), all children receive a copy of the parent's `shared_ptr<Adapter>`. This ensures:

1. All components use the same underlying hardware interface
2. Reference counting prevents premature adapter destruction
3. Children can perform independent transactions without interfering with each other (assuming proper channel selection)

For details on how channel selection coordinates access, see [Parent-Child Hierarchies](#3.4).

**Sources:** [src/m5_unit_component/component.hpp](), [src/m5_unit_component/component.cpp]()

## Testing Adapter Implementations

The GoogleTest framework provides specialized base classes for testing components with different adapter types: `ComponentTestBase` for I2C, `GPIOComponentTestBase` for GPIO, and `UARTComponentTestBase` for UART.

### Parameterized Adapter Testing

```mermaid
graph TB
    TestSuite["Test Suite"]
    
    TestParam{"Test<br/>Parameter"}
    
    UseWire["Create component with Wire<br/>ComponentTestBase creates<br/>AdapterI2C(Wire)"]
    
    UseHAL["Create component with Bus<br/>ComponentTestBase creates<br/>AdapterI2C(Bus)"]
    
    RunTest1["Run test with WireImpl"]
    RunTest2["Run test with BusImpl"]
    
    Verify["Verify identical behavior<br/>across implementations"]
    
    TestSuite --> TestParam
    TestParam -->|"Wire"| UseWire
    TestParam -->|"HAL"| UseHAL
    
    UseWire --> RunTest1
    UseHAL --> RunTest2
    
    RunTest1 --> Verify
    RunTest2 --> Verify
```

The `ComponentTestBase::begin()` method checks the test parameter to determine whether to use `Wire` (Arduino) or `Bus` (M5HAL), enabling the same test to validate both implementation paths.

**Sources:** [src/googletest/test_template.hpp:86-100](), [src/googletest/test_template.hpp:142-161](), [src/googletest/test_template.hpp:203-213]()