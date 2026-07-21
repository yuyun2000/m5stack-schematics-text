M5UnitUnified Communication Protocols

# Communication Protocols

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [library.json](library.json)
- [library.properties](library.properties)
- [src/googletest/test_helper.hpp](src/googletest/test_helper.hpp)
- [src/googletest/test_template.hpp](src/googletest/test_template.hpp)
- [src/m5_unit_component/adapter.cpp](src/m5_unit_component/adapter.cpp)
- [src/m5_unit_component/adapter.hpp](src/m5_unit_component/adapter.hpp)
- [src/m5_unit_component/adapter_gpio.cpp](src/m5_unit_component/adapter_gpio.cpp)
- [src/m5_unit_component/adapter_gpio.hpp](src/m5_unit_component/adapter_gpio.hpp)
- [src/m5_unit_component/adapter_gpio_v1.cpp](src/m5_unit_component/adapter_gpio_v1.cpp)
- [src/m5_unit_component/adapter_gpio_v2.cpp](src/m5_unit_component/adapter_gpio_v2.cpp)
- [src/m5_unit_component/adapter_gpio_v2.hpp](src/m5_unit_component/adapter_gpio_v2.hpp)
- [src/m5_unit_component/adapter_i2c.hpp](src/m5_unit_component/adapter_i2c.hpp)
- [src/m5_unit_component/adapter_uart.cpp](src/m5_unit_component/adapter_uart.cpp)
- [src/m5_unit_component/identify_functions.hpp](src/m5_unit_component/identify_functions.hpp)
- [src/m5_unit_component/types.hpp](src/m5_unit_component/types.hpp)

</details>



## Purpose and Scope

This page provides an overview of the three communication protocols supported by M5UnitUnified: I2C, GPIO/RMT, and UART. It explains the adapter abstraction layer that unifies these protocols, how components declare protocol support through attributes, and guidance on selecting the appropriate protocol for different sensors.

For detailed implementation specifics of each protocol, see:
- [I2C Communication](#4.1) for address management, clock configuration, and transaction patterns
- [GPIO and RMT](#4.2) for digital/analog operations and pulse timing
- [UART Communication](#4.3) for serial interface details

For information about the adapter pattern design, see [Adapter Pattern](#3.3).

---

## Protocol Overview

M5UnitUnified abstracts three hardware communication protocols through a unified adapter interface. Each protocol serves different sensor types and use cases:

| Protocol | Typical Use Cases | M5Stack Ports | Key Characteristics |
|----------|------------------|---------------|---------------------|
| **I2C** | Environmental sensors, ADCs, IMUs, displays | Port A (Grove) | Multi-device bus, address-based, 100-400kHz |
| **GPIO/RMT** | IR transmitters/receivers, pulse sensors, digital I/O | Port B, GPIO pins | Single/dual wire, precise timing control |
| **UART** | GPS modules, fingerprint sensors, serial devices | Port C (HY2.0) | Full-duplex, configurable baud rate |

Components declare protocol support using attribute bits defined in [src/m5_unit_component/types.hpp:44-50]():

```cpp
namespace attribute {
    constexpr attr_t AccessI2C  = 0x00000001;  // I2C Accessible Unit
    constexpr attr_t AccessGPIO = 0x00000002;  // GPIO Accessible Unit
    constexpr attr_t AccessUART = 0x00000004;  // UART Accessible Unit
}
```

**Sources:** [src/m5_unit_component/types.hpp:44-50](), [library.json:1-31]()

---

## Adapter Type System

### Adapter Hierarchy

The adapter system uses runtime polymorphism to support multiple implementations per protocol. The `Adapter` base class defines a common interface, while protocol-specific adapters extend it with specialized functionality.

```mermaid
classDiagram
    class Adapter {
        <<abstract>>
        +Type _type
        +unique_ptr~Impl~ _impl
        +readWithTransaction()
        +writeWithTransaction()
    }
    
    class AdapterI2C {
        +I2CImpl* impl()
        +address() uint8_t
        +clock() uint32_t
        +duplicate(addr) Adapter*
    }
    
    class AdapterGPIOBase {
        +GPIOImpl* impl()
        +rx_pin() gpio_num_t
        +tx_pin() gpio_num_t
        +begin(config)
    }
    
    class AdapterUART {
        +UARTImpl* impl()
        +flush()
        +setTimeout(ms)
    }
    
    class I2CImpl {
        <<interface>>
        +address() uint8_t
        +clock() uint32_t
        +readWithTransaction()
        +writeWithTransaction()
    }
    
    class WireImpl {
        -TwoWire* _wire
        +getWire() TwoWire*
        +scl() int16_t
        +sda() int16_t
    }
    
    class BusImpl {
        -Bus* _bus
        +getBus() Bus*
        -I2CMasterAccessConfig _access_cfg
    }
    
    class GPIOImpl {
        <<interface>>
        -gpio_num_t _rx_pin
        -gpio_num_t _tx_pin
        -adapter_config_t _adapter_cfg
        +pin_mode()
        +write_digital()
        +read_analog()
    }
    
    class GPIOImplV1 {
        -rmt_config_t _rx_config
        -rmt_config_t _tx_config
        +begin()
    }
    
    class GPIOImplV2 {
        -rmt_channel_handle_t _rx_handle
        -rmt_channel_handle_t _tx_handle
        +begin()
    }
    
    class SerialImpl {
        -HardwareSerial* _serial
        +flush()
        +flushRX()
    }
    
    Adapter <|-- AdapterI2C
    Adapter <|-- AdapterGPIOBase
    Adapter <|-- AdapterUART
    
    AdapterI2C o-- I2CImpl
    I2CImpl <|-- WireImpl
    I2CImpl <|-- BusImpl
    
    AdapterGPIOBase o-- GPIOImpl
    GPIOImpl <|-- GPIOImplV1
    GPIOImpl <|-- GPIOImplV2
    
    AdapterUART o-- SerialImpl
```

**Diagram: Adapter class hierarchy showing protocol implementations**

**Sources:** [src/m5_unit_component/adapter_base.hpp](), [src/m5_unit_component/adapter_i2c.hpp:25-243](), [src/m5_unit_component/adapter_gpio.hpp:40-158](), [src/m5_unit_component/adapter_uart.hpp]()

---

## Implementation Selection

### Compile-Time Protocol Variant Selection

The library automatically selects implementation variants based on compile-time detection of ESP-IDF version and available features:

```mermaid
graph TB
    DETECT["identify_functions.hpp<br/>Version Detection"]
    
    IDF_VER{"ESP-IDF Version?"}
    
    RMT_V1["RMT v1<br/>adapter_gpio_v1.cpp"]
    RMT_V2["RMT v2<br/>adapter_gpio_v2.cpp"]
    
    ADC_OLD["ADC Legacy API<br/>adc1_get_raw()"]
    ADC_NEW["ADC Oneshot API<br/>adc_oneshot_read()"]
    
    ADAPTER_HPP["adapter.hpp<br/>Conditional Include"]
    
    GPIO_V1["adapter_gpio_v1.hpp"]
    GPIO_V2["adapter_gpio_v2.hpp"]
    
    DETECT --> IDF_VER
    
    IDF_VER -->|"< 5.0.0"| RMT_V1
    IDF_VER -->|">= 5.0.0"| RMT_V2
    
    IDF_VER -->|"< 5.0.0"| ADC_OLD
    IDF_VER -->|">= 5.0.0"| ADC_NEW
    
    RMT_V1 --> GPIO_V1
    RMT_V2 --> GPIO_V2
    
    GPIO_V1 --> ADAPTER_HPP
    GPIO_V2 --> ADAPTER_HPP
```

**Diagram: Conditional compilation for protocol implementations**

The version detection in [src/m5_unit_component/identify_functions.hpp:14-26]() defines preprocessor macros:

```cpp
#if ESP_IDF_VERSION >= ESP_IDF_VERSION_VAL(5, 0, 0)
#define M5_UNIT_UNIFIED_USING_RMT_V2
#define M5_UNIT_UNIFIED_USING_ADC_ONESHOT
#endif
```

These macros control conditional includes in [src/m5_unit_component/adapter.hpp:14-23]():

```cpp
#if defined(M5_UNIT_UNIFIED_USING_RMT_V2)
#include "adapter_gpio_v2.hpp"
#else
#include "adapter_gpio_v1.hpp"
#endif
```

**Sources:** [src/m5_unit_component/identify_functions.hpp:14-26](), [src/m5_unit_component/adapter.hpp:14-23](), [src/m5_unit_component/adapter_gpio_v1.cpp:13-18](), [src/m5_unit_component/adapter_gpio_v2.cpp:12-18]()

---

## Runtime Protocol Selection

### I2C Implementation Variants

Components using I2C can be assigned either Arduino's `TwoWire` or M5HAL's `Bus` interface at runtime:

```mermaid
graph LR
    subgraph "User Code"
        UNIT["Component Instance"]
    end
    
    subgraph "Adapter Selection"
        WIRE_PATH["Wire Path"]
        BUS_PATH["Bus Path"]
    end
    
    subgraph "Implementation"
        WIRE_IMPL["WireImpl"]
        BUS_IMPL["BusImpl"]
    end
    
    subgraph "Hardware Layer"
        TWOWIRE["TwoWire<br/>Arduino API"]
        HALBUS["m5::hal::bus::Bus<br/>M5HAL API"]
    end
    
    UNIT -->|"add(unit, Wire)"| WIRE_PATH
    UNIT -->|"add(unit, bus)"| BUS_PATH
    
    WIRE_PATH --> WIRE_IMPL
    BUS_PATH --> BUS_IMPL
    
    WIRE_IMPL --> TWOWIRE
    BUS_IMPL --> HALBUS
    
    TWOWIRE --> I2C_HW["I2C Hardware"]
    HALBUS --> I2C_HW
```

**Diagram: Runtime selection between TwoWire and M5HAL Bus implementations**

The selection occurs in `UnitUnified::add()` calls:

```cpp
// Using Arduino TwoWire
Units.add(unit, Wire);  // Creates AdapterI2C with WireImpl

// Using M5HAL Bus
auto bus = m5::hal::bus::i2c::getBus(i2c_cfg);
Units.add(unit, bus.value());  // Creates AdapterI2C with BusImpl
```

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:101-136](), [src/m5_unit_component/adapter_i2c.hpp:139-171](), [src/googletest/test_template.hpp:86-100]()

### GPIO Implementation Variants

GPIO adapters support both basic digital/analog operations and RMT peripheral access for precise pulse timing:

| Mode | Enum Value | RMT Usage | Typical Applications |
|------|------------|-----------|---------------------|
| `Input` | 0 | No | Button reading, sensor flags |
| `Output` | 1 | No | LED control, relay switching |
| `Analog` | 8 | No | ADC reading (temperature, light) |
| `RmtRX` | 0x80 | Yes | IR receiver, pulse counting |
| `RmtTX` | 0x81 | Yes | IR transmitter, WS2812 LEDs |
| `RmtRXTX` | 0x82 | Yes | DHT sensors, bidirectional pulse |

Mode definitions from [src/m5_unit_component/types.hpp:60-74]():

```cpp
enum class Mode : uint8_t {
    Input, Output, Pullup, InputPullup, Pulldown, InputPulldown,
    OpenDrain, OutputOpenDrain, Analog,
    RmtRX = 0x80, RmtTX, RmtRXTX,
};
```

**Sources:** [src/m5_unit_component/types.hpp:60-74](), [src/m5_unit_component/adapter_gpio.cpp:45-145]()

### UART Implementation

UART adapters wrap Arduino's `HardwareSerial` interface, providing transaction-based read/write methods:

```mermaid
sequenceDiagram
    participant User as "User Code"
    participant Adapter as "AdapterUART"
    participant Impl as "SerialImpl"
    participant HW as "HardwareSerial"
    
    User->>Adapter: add(unit, Serial2)
    Adapter->>Impl: Create SerialImpl(Serial2)
    
    User->>Adapter: writeWithTransaction(data, len)
    Adapter->>Impl: writeWithTransaction(data, len)
    Impl->>HW: write(data, len)
    HW-->>Impl: bytes_written
    Impl-->>Adapter: OK/TIMEOUT_ERROR
    
    User->>Adapter: readWithTransaction(buffer, len)
    Adapter->>Impl: readWithTransaction(buffer, len)
    Impl->>HW: readBytes(buffer, len)
    HW-->>Impl: bytes_read
    Impl-->>Adapter: OK/TIMEOUT_ERROR
```

**Diagram: UART transaction flow through adapter layers**

**Sources:** [src/m5_unit_component/adapter_uart.cpp:25-62](), [src/googletest/test_template.hpp:203-213]()

---

## Protocol Configuration

### I2C Configuration Parameters

I2C adapters store address and clock frequency, modifiable at runtime:

```cpp
// Construction
AdapterI2C adapter(Wire, 0x5C, 400000);  // addr=0x5C, clock=400kHz

// Runtime modification
adapter.setAddress(0x5D);     // Change target address
adapter.setClock(100000);     // Reduce to 100kHz
```

[src/m5_unit_component/adapter_i2c.hpp:36-53]() defines the parameters stored in `I2CImpl`:

```cpp
uint8_t _addr{};                    // I2C device address
uint32_t _clock{100 * 1000U};       // Clock frequency (default 100kHz)
```

**Sources:** [src/m5_unit_component/adapter_i2c.hpp:36-53](), [src/m5_unit_component/adapter_i2c.hpp:190-207]()

### GPIO/RMT Configuration Structure

GPIO adapters accept a unified configuration structure supporting both RMT v1 and v2:

```mermaid
classDiagram
    class adapter_config_t {
        +Mode mode
        +rx_config_t rx
        +tx_config_t tx
    }
    
    class config_t {
        <<base>>
        +uint32_t tick_ns
        +gpio_num_t gpio_num
        +uint8_t mem_blocks
        +bool invert_signal
        +bool with_dma
    }
    
    class tx_config_t {
        +uint16_t loop_count
        +bool idle_output_enabled
        +bool idle_level_high
        +bool loop_enabled
    }
    
    class rx_config_t {
        +uint16_t ring_buffer_size
        +uint16_t filter_ticks_threshold
        +uint16_t idle_ticks_threshold
        +bool filter_enabled
    }
    
    adapter_config_t *-- tx_config_t
    adapter_config_t *-- rx_config_t
    config_t <|-- tx_config_t
    config_t <|-- rx_config_t
```

**Diagram: GPIO/RMT configuration structure hierarchy**

From [src/m5_unit_component/types.hpp:80-110]():

```cpp
struct adapter_config_t {
    Mode mode{};        // RmtRX, RmtTX, or RmtRXTX
    rx_config_t rx{};   // RX-specific parameters
    tx_config_t tx{};   // TX-specific parameters
};
```

Key configuration fields:
- `tick_ns`: RMT tick resolution in nanoseconds (determines timing precision)
- `mem_blocks`: RMT memory allocation (v1: 1-8 blocks, v2: symbol buffer size)
- `filter_ticks_threshold`: Minimum valid pulse duration (noise filtering)
- `idle_ticks_threshold`: Timeout for end-of-transmission detection

**Sources:** [src/m5_unit_component/types.hpp:80-110](), [src/m5_unit_component/adapter_gpio.cpp:49-74]()

---

## Testing Infrastructure Protocol Support

The GoogleTest framework provides specialized base classes for each protocol:

```mermaid
graph TB
    GLOBAL["GlobalFixture<br/>M5.begin(), Wire.begin()"]
    
    subgraph "Test Base Classes"
        I2C_BASE["ComponentTestBase<br/>I2C Units"]
        GPIO_BASE["GPIOComponentTestBase<br/>GPIO Units"]
        UART_BASE["UARTComponentTestBase<br/>UART Units"]
    end
    
    subgraph "Test Methods"
        I2C_METHOD["begin(): Wire or Bus"]
        GPIO_METHOD["begin(): GPIO pins"]
        UART_METHOD["begin(): HardwareSerial"]
    end
    
    GLOBAL -.initializes.-> I2C_BASE
    GLOBAL -.initializes.-> GPIO_BASE
    GLOBAL -.initializes.-> UART_BASE
    
    I2C_BASE --> I2C_METHOD
    GPIO_BASE --> GPIO_METHOD
    UART_BASE --> UART_METHOD
    
    I2C_METHOD --> TEST_I2C["Parameterized Tests<br/>Wire vs M5HAL"]
    GPIO_METHOD --> TEST_GPIO["RMT TX/RX Tests"]
    UART_METHOD --> TEST_UART["Serial Transaction Tests"]
```

**Diagram: Test infrastructure protocol support hierarchy**

From [src/googletest/test_template.hpp:33-54](), the global fixture initializes I2C:

```cpp
template <uint32_t FREQ, uint32_t WNUM = 0>
class GlobalFixture : public ::testing::Environment {
    void SetUp() override {
        auto pin_num_sda = M5.getPin(m5::pin_name_t::port_a_sda);
        auto pin_num_scl = M5.getPin(m5::pin_name_t::port_a_scl);
        w[WNUM]->begin(pin_num_sda, pin_num_scl, FREQ);
    }
};
```

Test base classes handle protocol-specific setup:

| Test Base Class | Protocol | Setup Method | Hardware Used |
|----------------|----------|--------------|---------------|
| `ComponentTestBase` | I2C | Wire.begin() or m5::hal::bus::i2c::getBus() | Port A (SDA/SCL) |
| `GPIOComponentTestBase` | GPIO/RMT | Units.add(unit, rx_pin, tx_pin) | Port B or Port A pins |
| `UARTComponentTestBase` | UART | Units.add(unit, Serial) | HardwareSerial instance |

**Sources:** [src/googletest/test_template.hpp:33-54](), [src/googletest/test_template.hpp:62-110](), [src/googletest/test_template.hpp:118-171](), [src/googletest/test_template.hpp:179-226]()

---

## Protocol Selection Guidelines

### Choosing the Appropriate Protocol

Decision matrix for protocol selection:

```mermaid
flowchart TD
    START["Select Protocol"]
    
    MULTI{"Multiple devices<br/>on shared bus?"}
    TIMING{"Precise timing<br/>required?"}
    BIDIRECTIONAL{"Full-duplex<br/>communication?"}
    
    I2C_PROTO["Use I2C<br/>AdapterI2C"]
    GPIO_PROTO["Use GPIO/RMT<br/>AdapterGPIO"]
    UART_PROTO["Use UART<br/>AdapterUART"]
    
    START --> MULTI
    MULTI -->|Yes| I2C_PROTO
    MULTI -->|No| TIMING
    
    TIMING -->|Yes<br/>microsecond| GPIO_PROTO
    TIMING -->|No| BIDIRECTIONAL
    
    BIDIRECTIONAL -->|Yes| UART_PROTO
    BIDIRECTIONAL -->|No| GPIO_PROTO
```

**Diagram: Protocol selection decision tree**

### Attribute-Based Protocol Identification

Components declare supported protocols using attribute bits. Applications can query these at runtime:

```cpp
// Check protocol support
if (unit.attribute() & types::attribute::AccessI2C) {
    // I2C protocol supported
}

if (unit.attribute() & types::attribute::AccessGPIO) {
    // GPIO/RMT protocol supported
}

if (unit.attribute() & types::attribute::AccessUART) {
    // UART protocol supported
}
```

Protocol attributes from [src/m5_unit_component/types.hpp:44-50]():

| Attribute Constant | Hex Value | Usage |
|-------------------|-----------|-------|
| `attribute::AccessI2C` | 0x00000001 | I2C-compatible units (most sensors) |
| `attribute::AccessGPIO` | 0x00000002 | GPIO/RMT units (IR, pulse sensors) |
| `attribute::AccessUART` | 0x00000004 | Serial units (GPS, fingerprint) |

**Sources:** [src/m5_unit_component/types.hpp:44-50](), [src/m5_unit_component/types.hpp:36-42]()