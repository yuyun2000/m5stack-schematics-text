M5UnitUnified API Reference

# API Reference

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [library.json](library.json)
- [library.properties](library.properties)
- [src/M5UnitComponent.cpp](src/M5UnitComponent.cpp)
- [src/M5UnitComponent.hpp](src/M5UnitComponent.hpp)
- [src/M5UnitUnified.cpp](src/M5UnitUnified.cpp)
- [src/M5UnitUnified.hpp](src/M5UnitUnified.hpp)
- [src/m5_unit_component/adapter_base.hpp](src/m5_unit_component/adapter_base.hpp)
- [src/m5_unit_component/adapter_gpio_v1.hpp](src/m5_unit_component/adapter_gpio_v1.hpp)
- [src/m5_unit_component/adapter_i2c.cpp](src/m5_unit_component/adapter_i2c.cpp)
- [src/m5_unit_component/adapter_i2c.hpp](src/m5_unit_component/adapter_i2c.hpp)

</details>



This page provides a comprehensive overview of the M5UnitUnified library's public API. It documents the core classes, their relationships, and common usage patterns for integrating M5Stack sensor units into your applications.

For detailed method-level documentation, see:
- Component base class methods: [Component API](#9.1)
- UnitUnified manager methods: [UnitUnified API](#9.2)
- Communication adapter interfaces: [Adapter APIs](#9.3)

For implementation examples, see [Usage Patterns](#5).

---

## Namespace Organization

The M5UnitUnified library uses a hierarchical namespace structure to organize its classes and types:

```mermaid
graph TB
    m5["m5<br/>(Top-level namespace)"]
    unit["unit<br/>(Unit components)"]
    types["types<br/>(Type definitions)"]
    gpio["gpio<br/>(GPIO-specific types)"]
    hal["hal<br/>(Hardware abstraction)"]
    
    m5 --> unit
    unit --> types
    unit --> gpio
    m5 --> hal
    
    Component["Component<br/>(Base class)"]
    UnitUnified["UnitUnified<br/>(Manager)"]
    Adapter["Adapter<br/>(Communication base)"]
    PeriodicMeasurementAdapter["PeriodicMeasurementAdapter<br/>(CRTP interface)"]
    
    unit --> Component
    unit --> UnitUnified
    unit --> Adapter
    unit --> PeriodicMeasurementAdapter
    
    uid_t["uid_t<br/>(Unique identifier)"]
    attr_t["attr_t<br/>(Attributes bitmask)"]
    category_t["category_t<br/>(Unit category)"]
    elapsed_time_t["elapsed_time_t<br/>(Millisecond timestamp)"]
    
    types --> uid_t
    types --> attr_t
    types --> category_t
    types --> elapsed_time_t
    
    Mode["Mode<br/>(Pin mode enum)"]
    pin_backup_t["pin_backup_t<br/>(GPIO register backup)"]
    
    gpio --> Mode
    gpio --> pin_backup_t
```

**Primary namespaces:**
- `m5::unit` - Contains all component and manager classes
- `m5::unit::types` - Type aliases and enumerations
- `m5::unit::gpio` - GPIO-specific functionality
- `m5::hal` - Hardware abstraction layer (from M5HAL dependency)

Sources: [src/M5UnitComponent.hpp:25-27](), [src/M5UnitUnified.hpp:32-40]()

---

## Core Class Hierarchy

The library's architecture centers on three primary class hierarchies:

```mermaid
classDiagram
    class Component {
        <<abstract>>
        +begin() bool
        +update(force) void
        +assign(wire) bool
        +assign(rx_pin, tx_pin) bool
        +adapter() Adapter*
        +address() uint8_t
        +identifier() uid_t
        +attribute() attr_t
        +deviceName() const char*
        +updated() bool
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len) error_t
        -_adapter shared_ptr~Adapter~
        -_manager UnitUnified*
        -_parent Component*
        -_child Component*
        -_next Component*
        -_prev Component*
    }
    
    class UnitUnified {
        +add(Component, TwoWire) bool
        +add(Component, rx_pin, tx_pin) bool
        +add(Component, HardwareSerial) bool
        +add(Component, Bus*) bool
        +begin() bool
        +update(force) void
        +debugInfo() string
        -_units vector~Component*~
        -_registerCount uint32_t
    }
    
    class Adapter {
        <<abstract>>
        +type() Type
        +duplicate(addr) Adapter*
        +readWithTransaction(data, len) error_t
        +writeWithTransaction(data, len) error_t
        #_impl unique_ptr~Impl~
        #_type Type
    }
    
    class AdapterI2C {
        +AdapterI2C(TwoWire, addr, clock)
        +AdapterI2C(Bus*, addr, clock)
        +address() uint8_t
        +setAddress(addr) void
        +clock() uint32_t
        +setClock(clock) void
        +scl() int16_t
        +sda() int16_t
        -I2CImpl* impl()
    }
    
    class AdapterGPIO {
        +AdapterGPIO(rx_pin, tx_pin)
        +rx_pin() int8_t
        +tx_pin() int8_t
        +pinModeRX(Mode) error_t
        +writeDigitalRX(high) error_t
        +readAnalogRX(value) error_t
        -GPIOImpl* impl()
    }
    
    class AdapterUART {
        +AdapterUART(HardwareSerial)
        +available() size_t
        +read() int
        +write(data, len) size_t
        -SerialImpl* impl()
    }
    
    class PeriodicMeasurementAdapter~Derived, MD~ {
        <<CRTP interface>>
        +startPeriodicMeasurement(args) bool
        +stopPeriodicMeasurement() bool
        +available() size_t
        +oldest() MD
        +latest() MD
        +discard() void
        +flush() void
    }
    
    Adapter <|-- AdapterI2C
    Adapter <|-- AdapterGPIO
    Adapter <|-- AdapterUART
    Component o-- Adapter : uses
    Component --o UnitUnified : managed by
    Component o-- Component : parent-child
    PeriodicMeasurementAdapter <.. Component : optional interface
```

**Key relationships:**
- `Component` is the abstract base class for all sensor units
- `UnitUnified` manages multiple `Component` instances
- `Component` uses `Adapter` for protocol-agnostic communication
- Components can form parent-child hierarchies (hub topologies)
- `PeriodicMeasurementAdapter` is a CRTP interface for time-series data

Sources: [src/M5UnitComponent.hpp:35-588](), [src/M5UnitUnified.hpp:47-117](), [src/m5_unit_component/adapter_base.hpp:25-229](), [src/m5_unit_component/adapter_i2c.hpp:25-243]()

---

## Type System

The library defines specialized types for improved type safety and code clarity:

| Type | Definition | Purpose |
|------|-----------|---------|
| `types::uid_t` | `uint32_t` | Unique identifier for each unit type (e.g., `0x12345678`) |
| `types::attr_t` | `uint32_t` | Bitmask of unit capabilities (I2C/GPIO/UART access) |
| `types::category_t` | `enum` | Unit category classification (ENV, METER, SENSOR, etc.) |
| `types::elapsed_time_t` | `uint32_t` | Millisecond timestamps from system start |
| `gpio::Mode` | `enum` | GPIO pin mode (Input, Output, InputPullup, etc.) |

**Attribute bitmask flags:**
```cpp
namespace m5::unit::types::attribute {
    constexpr attr_t AccessI2C   = (1 << 0);  // Can communicate via I2C
    constexpr attr_t AccessGPIO  = (1 << 1);  // Can communicate via GPIO
    constexpr attr_t AccessUART  = (1 << 2);  // Can communicate via UART
    // Additional flags defined in types.hpp
}
```

**Usage example:**
```cpp
// Check if unit supports I2C communication
if (component.canAccessI2C()) {
    // Unit has AccessI2C attribute set
}
```

Sources: [src/m5_unit_component/types.hpp]()

---

## Component Configuration

Each `Component` instance can be configured through the `component_config_t` structure:

```mermaid
graph LR
    cfg["component_config_t"]
    
    clock["clock<br/>uint32_t<br/>default: 100000"]
    stored["stored_size<br/>uint32_t<br/>default: 1"]
    self["self_update<br/>bool<br/>default: false"]
    children["max_children<br/>uint8_t<br/>default: 0"]
    
    cfg --> clock
    cfg --> stored
    cfg --> self
    cfg --> children
    
    clock_desc["I2C clock frequency<br/>in Hz"]
    stored_desc["Circular buffer size<br/>for periodic data"]
    self_desc["Enable async updates<br/>via FreeRTOS task"]
    children_desc["Maximum connected<br/>child units (hub)"]
    
    clock -.-> clock_desc
    stored -.-> stored_desc
    self -.-> self_desc
    children -.-> children_desc
```

**Configuration pattern:**
```cpp
auto unit = UnitCO2();
auto cfg = unit.component_config();
cfg.clock = 400000;              // 400kHz I2C
cfg.stored_size = 10;            // Store 10 measurements
cfg.self_update = false;         // Manager calls update()
unit.component_config(cfg);
```

Sources: [src/M5UnitComponent.hpp:41-50](), [src/M5UnitComponent.hpp:83-92]()

---

## Error Handling

All communication operations return `m5::hal::error::error_t` enum values:

```mermaid
graph TD
    op["Communication Operation"]
    check{"Check<br/>error_t"}
    
    op --> check
    
    OK["error_t::OK<br/>Operation succeeded"]
    I2C_ERR["error_t::I2C_BUS_ERROR<br/>I2C transaction failed"]
    INVALID["error_t::INVALID_ARGUMENT<br/>Invalid parameters"]
    UNKNOWN["error_t::UNKNOWN_ERROR<br/>Unspecified failure"]
    
    check -->|Success| OK
    check -->|I2C failure| I2C_ERR
    check -->|Bad input| INVALID
    check -->|Other| UNKNOWN
    
    retry["Retry logic"]
    error_log["Error logging"]
    
    I2C_ERR --> retry
    UNKNOWN --> error_log
```

**Error handling pattern:**
```cpp
// Direct error check
auto err = component.writeWithTransaction(data, len);
if (err != m5::hal::error::error_t::OK) {
    M5_LIB_LOGE("Write failed: %d", (int)err);
}

// Boolean convenience methods
if (!component.writeRegister8(reg, value)) {
    // Operation failed
}
```

**Common error codes:**
- `OK` - Operation completed successfully
- `I2C_BUS_ERROR` - I2C NACK or timeout
- `INVALID_ARGUMENT` - Null pointer or invalid parameter
- `UNKNOWN_ERROR` - Default failure state

Sources: [src/M5UnitComponent.cpp:166-177](), [src/M5UnitComponent.cpp:192-202]()

---

## Static Member Pattern

Unit classes define three static members for identification and capabilities:

```mermaid
graph TB
    subgraph "Every Unit Class"
        uid["static const uid_t uid<br/>Unique 32-bit identifier"]
        attr["static const attr_t attr<br/>Capability bitmask"]
        name["static const char name[]<br/>Device name string"]
    end
    
    subgraph "Component Base"
        v_uid["virtual uid_t unit_identifier()"]
        v_attr["virtual attr_t unit_attribute()"]
        v_name["virtual const char* unit_device_name()"]
    end
    
    subgraph "Public Access"
        p_uid["uid_t identifier()"]
        p_attr["attr_t attribute()"]
        p_name["const char* deviceName()"]
    end
    
    uid --> v_uid
    attr --> v_attr
    name --> v_name
    
    v_uid --> p_uid
    v_attr --> p_attr
    v_name --> p_name
    
    builder["M5_UNIT_COMPONENT_HPP_BUILDER<br/>macro generates boilerplate"]
    builder -.-> uid
    builder -.-> attr
    builder -.-> name
```

**Implementation via builder macro:**
```cpp
// In derived unit class header
class UnitCO2 : public Component {
    M5_UNIT_COMPONENT_HPP_BUILDER(UnitCO2, 0x62);
    // Expands to:
    // static constexpr uint8_t DEFAULT_ADDRESS{0x62};
    // static const types::uid_t uid;
    // static const types::attr_t attr;
    // static const char name[];
    // ... and virtual function overrides
};

// In derived unit class implementation
const types::uid_t UnitCO2::uid{0x87654321};
const types::attr_t UnitCO2::attr{types::attribute::AccessI2C};
const char UnitCO2::name[] = "UnitCO2";
```

Sources: [src/M5UnitComponent.hpp:52-58](), [src/M5UnitComponent.hpp:694-721]()

---

## Communication API Pattern

All three communication protocols follow a consistent transaction-based API:

```mermaid
sequenceDiagram
    participant App as "Application"
    participant Comp as "Component"
    participant Adapt as "Adapter"
    participant Impl as "Adapter::Impl"
    participant HW as "Hardware<br/>(Wire/GPIO/Serial)"
    
    App->>Comp: writeRegister8(reg, value)
    Note over Comp: Template method<br/>accepts uint8_t or uint16_t reg
    
    Comp->>Comp: selectChannel(channel)
    Note over Comp: Recursive parent traversal<br/>for hub topologies
    
    Comp->>Adapt: writeWithTransaction(reg, &value, 1)
    Adapt->>Impl: writeWithTransaction(reg, &value, 1)
    
    alt I2C
        Impl->>HW: beginTransmission(addr)
        Impl->>HW: write(reg)
        Impl->>HW: write(value)
        Impl->>HW: endTransmission()
    else GPIO
        Impl->>HW: digitalWrite(pin, value)
    else UART
        Impl->>HW: Serial.write(&value, 1)
    end
    
    HW-->>Impl: return status
    Impl-->>Adapt: error_t
    Adapt-->>Comp: error_t
    Comp-->>App: bool (success)
```

**Common I2C operations:**
- `readWithTransaction(data, len)` - Read raw bytes
- `writeWithTransaction(data, len)` - Write raw bytes
- `readRegister8(reg, result, delay)` - Read 8-bit register
- `writeRegister8(reg, value)` - Write 8-bit register
- `readRegister16BE/LE(reg, result, delay)` - Read 16-bit register (big/little endian)
- `writeRegister16BE/LE(reg, value)` - Write 16-bit register

**Register templates:**
```cpp
// Supports both 8-bit and 16-bit register addresses
template <typename Reg>
bool readRegister(const Reg reg, uint8_t* rbuf, const size_t len, 
                  const uint32_t delayMillis, const bool stop = true);
```

Sources: [src/M5UnitComponent.hpp:348-440](), [src/M5UnitComponent.cpp:179-280]()

---

## Lifecycle Methods

Components follow a standard lifecycle managed by `UnitUnified`:

```mermaid
stateDiagram-v2
    [*] --> Constructed : new UnitXXX()
    
    Constructed --> Configured : component_config(cfg)
    Configured --> Assigned : UnitUnified::add()
    
    note right of Assigned
        Adapter created
        Parent/children linked
        _manager pointer set
    end note
    
    Assigned --> Initialized : UnitUnified::begin()
    
    note right of Initialized
        begin() called
        Hardware initialized
        _begun flag set
    end note
    
    Initialized --> Updating : UnitUnified::update()
    Updating --> Updating : update() loop
    
    note right of Updating
        Periodic: update() called by manager
        Self-update: update() called by FreeRTOS task
    end note
    
    Updating --> [*] : Destruction
```

**Required overrides:**
```cpp
class MyUnit : public Component {
public:
    // Initialize hardware, start measurements
    virtual bool begin() override {
        // Return true if successful
    }
    
    // Read sensor data, update internal state
    virtual void update(const bool force = false) override {
        // Set _updated flag when new data available
    }
};
```

**Lifecycle guarantees:**
- `begin()` called exactly once after assignment
- `update()` called repeatedly only if `begin()` returned true
- `update()` skipped for units with `self_update=true`

Sources: [src/M5UnitComponent.hpp:96-112](), [src/M5UnitUnified.cpp:124-144]()

---

## Parent-Child Relationships

Components support hierarchical topologies for hub-based configurations:

```mermaid
graph TB
    subgraph "Parent Unit (Hub)"
        hub["UnitPaHub2<br/>_child pointer"]
        hub_adapter["shared_ptr&lt;Adapter&gt;<br/>Reference count: 4"]
    end
    
    subgraph "Child Units (Sensors)"
        child0["UnitCO2<br/>_channel = 0<br/>_parent = hub"]
        child1["UnitVmeter<br/>_channel = 1<br/>_parent = hub"]
        child2["UnitHEART<br/>_channel = 2<br/>_parent = hub"]
    end
    
    hub --> child0
    child0 --> child1
    child1 --> child2
    
    hub_adapter -.shares.-> child0
    hub_adapter -.shares.-> child1
    hub_adapter -.shares.-> child2
    
    child0_prev["_prev = nullptr"]
    child0_next["_next = child1"]
    
    child1_prev["_prev = child0"]
    child1_next["_next = child2"]
    
    child2_prev["_prev = child1"]
    child2_next["_next = nullptr"]
    
    child0 --> child0_prev
    child0 --> child0_next
    child1 --> child1_prev
    child1 --> child1_next
    child2 --> child2_prev
    child2 --> child2_next
```

**API methods:**
- `add(Component& child, channel)` - Connect child to specific channel
- `hasParent()` - Check if unit has a parent
- `hasSiblings()` - Check if other units share the same parent
- `hasChildren()` - Check if unit has connected children
- `childrenSize()` - Count of connected children
- `existsChild(channel)` - Check if channel is occupied
- `child(channel)` - Get child at specific channel
- `selectChannel(channel)` - Recursively configure hub chain

**Usage pattern:**
```cpp
// Create hub and sensors
auto hub = UnitPaHub2();
auto co2 = UnitCO2();
auto vmeter = UnitVmeter();

// Connect sensors to hub channels
hub.add(co2, 0);
hub.add(vmeter, 1);

// Register only the hub - children registered automatically
Units.add(hub, Wire);
```

Sources: [src/M5UnitComponent.hpp:234-272](), [src/M5UnitComponent.cpp:62-123]()

---

## Periodic Measurement Interface

Units with time-series data inherit from `PeriodicMeasurementAdapter` (CRTP pattern):

```mermaid
graph TB
    subgraph "User Code"
        app["Application"]
    end
    
    subgraph "CRTP Interface"
        crtp["PeriodicMeasurementAdapter&lt;UnitHEART, Data&gt;"]
        start["startPeriodicMeasurement(interval)"]
        stop["stopPeriodicMeasurement()"]
        avail["available() -> size_t"]
        oldest["oldest() -> Data"]
        latest["latest() -> Data"]
    end
    
    subgraph "Derived Implementation"
        unit["UnitHEART : public Component,<br/>public PeriodicMeasurementAdapter"]
        impl_start["start_periodic_measurement()"]
        impl_stop["stop_periodic_measurement()"]
        impl_data["oldest/latest_periodic_data()"]
        buffer["unique_ptr&lt;CircularBuffer&lt;Data&gt;&gt; _data"]
    end
    
    subgraph "Component Base"
        comp["Component"]
        updated["_updated flag"]
        interval["_interval timestamp"]
        periodic["_periodic flag"]
    end
    
    app --> start
    app --> avail
    app --> latest
    
    crtp --> unit
    start --> impl_start
    oldest --> impl_data
    
    impl_start --> buffer
    impl_data --> buffer
    
    unit -.inherits.-> comp
    impl_start -.sets.-> periodic
    impl_start -.configures.-> interval
```

**Required implementation:**
```cpp
class UnitHEART : public Component, 
                  public PeriodicMeasurementAdapter<UnitHEART, Data> {
    // Macro generates interface implementations
    M5_UNIT_COMPONENT_PERIODIC_MEASUREMENT_ADAPTER_HPP_BUILDER(UnitHEART, Data);
    
protected:
    // User implements these
    bool start_periodic_measurement();
    bool stop_periodic_measurement();
    Data oldest_periodic_data() const;
    Data latest_periodic_data() const;
    
    // Required data member
    std::unique_ptr<m5::container::CircularBuffer<Data>> _data{};
};
```

**Usage pattern:**
```cpp
unit.startPeriodicMeasurement();  // Begin collecting data

if (unit.updated()) {
    auto data = unit.latest();    // Get most recent reading
    // Process data...
}

size_t count = unit.available();  // Check buffer occupancy
```

Sources: [src/M5UnitComponent.hpp:590-687](), [src/M5UnitComponent.hpp:724-755]()

---

## Detailed API Documentation

For complete method signatures, parameters, and usage examples:

- **[Component API](#9.1)** - Full Component class reference including:
  - Lifecycle methods (`begin()`, `update()`)
  - Communication methods (I2C, GPIO, UART)
  - Property accessors
  - Parent-child management
  - Iterator interface

- **[UnitUnified API](#9.2)** - UnitUnified manager reference including:
  - Unit registration methods
  - Batch operations (`begin()`, `update()`)
  - Debugging utilities

- **[Adapter APIs](#9.3)** - Communication adapter reference including:
  - AdapterI2C (TwoWire and M5HAL implementations)
  - AdapterGPIO (RMT v1/v2 support)
  - AdapterUART (HardwareSerial interface)

Sources: [src/M5UnitComponent.hpp](), [src/M5UnitUnified.hpp](), [src/m5_unit_component/adapter_base.hpp](), [src/m5_unit_component/adapter_i2c.hpp]()