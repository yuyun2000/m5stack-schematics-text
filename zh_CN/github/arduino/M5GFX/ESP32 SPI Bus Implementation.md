M5GFX ESP32 SPI Bus Implementation

# ESP32 SPI Bus Implementation

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp](src/lgfx/v1/platforms/esp32/Bus_SPI.cpp)
- [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp](src/lgfx/v1/platforms/esp32/Bus_SPI.hpp)
- [src/lgfx/v1/platforms/esp32/common.cpp](src/lgfx/v1/platforms/esp32/common.cpp)
- [src/lgfx/v1/platforms/esp32/common.hpp](src/lgfx/v1/platforms/esp32/common.hpp)

</details>



## Overview

The `Bus_SPI` class [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:65-205]() implements the `IBus` interface for ESP32 SPI communication. It uses direct register manipulation to achieve high throughput, bypassing ESP-IDF's `spi_master` driver during data transfers while using it only for initialization. The implementation supports:

- DMA-based transfers with descriptor chains (`lldesc_t`)
- Multiple SPI hosts: `HSPI_HOST`, `VSPI_HOST` (ESP32), `SPI2_HOST`, `SPI3_HOST` (S2/S3/C3/C6/P4)
- Quad-SPI (QSPI) mode via `SPI_FWRITE_QUAD` flag
- Clock frequencies up to 80MHz on compatible displays

This page focuses on ESP32-specific SPI implementation. For bus abstraction concepts, see page 5. For I2C implementation, see page 5.4. For DMA memory management, see page 5.5.

---

## Architecture and Hybrid Initialization Strategy

The `Bus_SPI` implementation uses ESP-IDF's `spi_bus_initialize()` and `spi_bus_add_device()` for peripheral setup [src/lgfx/v1/platforms/esp32/common.cpp:550-618](), then bypasses the driver for all transfers by writing directly to SPI peripheral registers. This hybrid approach provides reliable GPIO/DMA configuration while eliminating driver call overhead during rendering.

**Bus_SPI Hybrid Architecture**

```mermaid
graph TB
    BusSPI["Bus_SPI class"]
    ConfigT["config_t struct<br/>freq_write/freq_read<br/>pin_sclk/pin_mosi/pin_miso/pin_dc<br/>spi_host/dma_channel"]
    
    Init["init() method"]
    SPIInit["spi::init()<br/>common.cpp:550"]
    IDFBusInit["spi_bus_initialize()"]
    IDFDevAdd["spi_bus_add_device()"]
    
    RegCache["Register pointer caching<br/>_spi_w0_reg = SPI_W0_REG(port)<br/>_spi_cmd_reg = SPI_CMD_REG(port)<br/>_spi_user_reg = SPI_USER_REG(port)<br/>_spi_mosi_dlen_reg"]
    
    Transfers["Transfer methods<br/>writeCommand()<br/>writeData()<br/>writeBytes()<br/>writePixels()"]
    
    DirectReg["Direct register writes<br/>*_spi_w0_reg = data<br/>*_spi_cmd_reg = SPI_EXECUTE<br/>*_spi_user_reg = flags"]
    
    DMAPath["DMA path<br/>_setup_dma_desc_links()<br/>lldesc_t chains<br/>SPI_DMA_OUT_LINK_REG"]
    
    SPIHardware["SPI Peripheral<br/>HSPI/VSPI/SPI2/SPI3"]
    
    BusSPI --> ConfigT
    BusSPI --> Init
    Init --> SPIInit
    SPIInit --> IDFBusInit
    SPIInit --> IDFDevAdd
    Init --> RegCache
    
    BusSPI --> Transfers
    Transfers --> DirectReg
    Transfers --> DMAPath
    
    DirectReg --> SPIHardware
    DMAPath --> SPIHardware
    
    IDFBusInit -.->|"GPIO matrix routing<br/>DMA allocation"| SPIHardware
```

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:113-203](), [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:65-210](), [src/lgfx/v1/platforms/esp32/common.cpp:550-630]()
</old_str>

<old_str>
## Configuration Structure (config_t)

The `config_t` struct [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:75-97]() defines all SPI parameters. Application code calls `Bus_SPI::config(const config_t&)` before `init()`.

### config_t Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `freq_write` | `uint32_t` | 16000000 | Write clock frequency in Hz (max 80MHz for most panels) |
| `freq_read` | `uint32_t` | 8000000 | Read clock frequency in Hz |
| `pin_sclk` | `int16_t` | -1 | SPI clock pin (GPIO number) |
| `pin_miso` | `int16_t` | -1 | Master In Slave Out (MISO) pin |
| `pin_mosi` | `int16_t` | -1 | Master Out Slave In (MOSI) pin |
| `pin_dc` | `int16_t` | -1 | Data/Command pin (separate from SPI) |
| `pin_io0..io3` | `int16_t` | -1 | Quad-SPI data pins (QSPI mode only) |
| `spi_mode` | `uint8_t` | 0 | SPI mode: 0 (CPOL=0, CPHA=0), 1, 2, or 3 |
| `spi_3wire` | `bool` | true | 3-wire mode (bi-directional MOSI) |
| `use_lock` | `bool` | true | Enable `spi_device_acquire_bus()` locking |
| `dma_channel` | `uint8_t` | `LGFX_ESP32_SPI_DMA_CH` | DMA channel (0 for auto, 1-2 for ESP32, auto-assigned on GDMA chips) |
| `spi_host` | `spi_host_device_t` | `VSPI_HOST` (ESP32)<br/>`SPI2_HOST` (others) | Hardware SPI peripheral: `HSPI_HOST`, `VSPI_HOST`, `SPI2_HOST`, `SPI3_HOST` |

### SPI Mode Configuration

The `spi_mode` field sets CPOL (clock polarity) and CPHA (clock phase):
- Mode 0: CPOL=0, CPHA=0 (most common for displays)
- Mode 1: CPOL=0, CPHA=1
- Mode 2: CPOL=1, CPHA=0
- Mode 3: CPOL=1, CPHA=1

The implementation maps mode to register bits in `beginTransaction()` [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:256-276]():
```
_user_reg = (spi_mode == 1 || spi_mode == 2) ? SPI_CK_OUT_EDGE | SPI_USR_MOSI : SPI_USR_MOSI
pin_reg = (spi_mode & 2) ? SPI_CK_IDLE_EDGE : 0
```

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:75-97](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:113-155](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:256-276]()
</old_str>
<new_str>
## Class Structure and Key Members

The `Bus_SPI` class [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:65-205]() extends `IBus` and contains cached register pointers, DMA management structures, and configuration state.

### Critical Member Variables

| Category | Member Variables | Purpose |
|----------|------------------|---------|
| **Config** | `config_t _cfg` | Pin assignments, frequencies, SPI mode, DMA channel |
| **Register Cache** | `volatile uint32_t* _spi_w0_reg`<br/>`volatile uint32_t* _spi_cmd_reg`<br/>`volatile uint32_t* _spi_user_reg`<br/>`volatile uint32_t* _spi_mosi_dlen_reg` | Cached register addresses for zero-overhead access<br/>[Bus_SPI.cpp:119-122]() |
| **DMA Registers** | `volatile uint32_t* _spi_dma_out_link_reg`<br/>`volatile uint32_t* _spi_dma_outstatus_reg`<br/>`volatile uint32_t* _clear_dma_reg` | DMA descriptor list pointer, FIFO status, clear flag |
| **DC Pin** | `volatile uint32_t* _gpio_reg_dc[2]`<br/>`uint32_t _mask_reg_dc` | GPIO set/clear register pointers and bit mask<br/>[Bus_SPI.cpp:134-142]() |
| **Clock** | `uint32_t _clkdiv_write`<br/>`uint32_t _clkdiv_read`<br/>`uint32_t _last_freq_apb` | Pre-calculated SPI clock divisors, APB frequency cache |
| **DMA Descriptors** | `lldesc_t* _dmadesc`<br/>`uint32_t _dmadesc_size`<br/>`lldesc_t* _dma_queue`<br/>`uint32_t _dma_queue_capacity` | Active descriptor chain and queue for batched DMA |
| **Buffer** | `FlipBuffer _flip_buffer` | Reusable DMA-capable memory allocator |
| **State** | `uint8_t _spi_port`<br/>`uint8_t _dma_ch`<br/>`bool _inited`<br/>`bool _is_quad_spi` | SPI peripheral number (1-3), DMA channel, init status, QSPI mode |

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:181-204]()

---

## Bus_SPI Class Structure

The `Bus_SPI` class inherits from `IBus` and provides the complete SPI communication layer. Key member variables store configuration, register pointers for direct access, and DMA management structures.

### Class Members

| Member Category | Variables | Purpose |
|----------------|-----------|---------|
| **Configuration** | `_cfg` | Stores `config_t` with pins, frequencies, SPI mode |
| **Register Pointers** | `_spi_w0_reg`, `_spi_cmd_reg`, `_spi_user_reg`, `_spi_mosi_dlen_reg` | Direct access to SPI hardware registers |
| **DMA Registers** | `_spi_dma_out_link_reg`, `_spi_dma_outstatus_reg`, `_clear_dma_reg` | DMA control and status |
| **GPIO Control** | `_gpio_reg_dc[2]`, `_mask_reg_dc` | DC pin high/low register addresses and bit mask |
| **Clock Division** | `_clkdiv_write`, `_clkdiv_read`, `_last_freq_apb` | Pre-calculated clock divisors |
| **DMA Descriptors** | `_dmadesc`, `_dmadesc_size`, `_dma_queue`, `_dma_queue_capacity` | DMA descriptor chains for transfers |
| **Buffers** | `_flip_buffer` | FlipBuffer for DMA-capable memory allocation |
| **State** | `_spi_port`, `_dma_ch`, `_inited`, `_is_quad_spi` | Runtime state flags |

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:181-204]()

---

### Initialization Sequence

**init() Method Flow** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:157-203]()

1. **DC Pin Setup** [line 160-161]()
   ```
   dc_control(true);
   pinMode(_cfg.pin_dc, pin_mode_t::output);
   ```
   Sets DC pin LOW initially via `gpio_lo()` to prevent glitches during mode change.

2. **ESP-IDF SPI Initialization** [line 169-175]()
   - Calls `spi::init()` which invokes `spi_bus_initialize()` [common.cpp:604]()
   - GPIO matrix routes SCLK/MISO/MOSI to specified pins
   - For QSPI: calls `spi::initQuad()` with `pin_io0` through `pin_io3`
   - DMA channel assignment: auto on IDF 4.3+, manual on earlier versions

3. **Register Pointer Caching** [line 117-130]()
   ```
   _spi_port = spi_port;
   _spi_w0_reg = reg(SPI_W0_REG(spi_port));
   _spi_cmd_reg = reg(SPI_CMD_REG(spi_port));
   _spi_user_reg = reg(SPI_USER_REG(spi_port));
   _spi_mosi_dlen_reg = reg(SPI_MOSI_DLEN_REG(spi_port));
   ```
   The `reg()` macro [line 142]() converts register offset to uncached pointer: `(volatile uint32_t *)ETS_UNCACHED_ADDR(addr)`

4. **DMA Channel Detection** [line 177-200]()
   - **GDMA chips** (S3/C3/C6/P4): Call `search_dma_out_ch()` [common.cpp:270-294]() to find which GDMA channel is assigned to this SPI peripheral
   - **ESP32**: Read `DPORT_SPI_DMA_CHAN_SEL_REG` bits for selected channel [line 195]()
   - Calculate DMA register offsets based on detected channel

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:157-203](), [src/lgfx/v1/platforms/esp32/common.cpp:550-630](), [src/lgfx/v1/platforms/esp32/common.cpp:270-294]()

---

## Initialization Process

Initialization uses ESP-IDF's SPI driver for peripheral setup, then caches register addresses for direct access.

```mermaid
sequenceDiagram
    participant App as Application
    participant BusSPI as Bus_SPI
    participant SPIInit as spi::init()
    participant ESPIDF as ESP-IDF Driver
    participant HW as SPI Hardware
    
    App->>BusSPI: config(config_t)
    App->>BusSPI: init()
    
    BusSPI->>BusSPI: pinMode(pin_dc, OUTPUT)
    BusSPI->>SPIInit: spi::init(host, sclk, miso, mosi, dma_ch)
    
    SPIInit->>ESPIDF: spi_bus_initialize()
    ESPIDF->>HW: Configure GPIO matrix
    ESPIDF->>HW: Enable peripheral clock
    
    SPIInit->>ESPIDF: spi_bus_add_device()
    ESPIDF->>HW: Allocate DMA channel
    
    SPIInit-->>BusSPI: Success
    
    BusSPI->>BusSPI: Cache register addresses
    Note over BusSPI: _spi_w0_reg = SPI_W0_REG(port)
    Note over BusSPI: _spi_cmd_reg = SPI_CMD_REG(port)
    Note over BusSPI: _spi_user_reg = SPI_USER_REG(port)
    
    BusSPI->>BusSPI: Detect DMA channel
    Note over BusSPI: search_dma_out_ch() for GDMA
    
    BusSPI-->>App: Initialized
```

## Register-Level SPI Operations

All data transfer operations write directly to SPI peripheral registers, bypassing ESP-IDF driver API calls for performance.

### SPI Peripheral Register Map

**Core Data Transfer Registers**

```mermaid
graph TB
    W0Reg["SPI_W0_REG through SPI_W15_REG<br/>16 words = 64 bytes<br/>Data buffer at offset 0x80"]
    
    CMDReg["SPI_CMD_REG<br/>SPI_USR bit = transfer active<br/>SPI_UPDATE bit (C3/S3)"]
    
    USERReg["SPI_USER_REG<br/>SPI_USR_MOSI = enable TX<br/>SPI_USR_MISO = enable RX<br/>SPI_CK_OUT_EDGE = CPHA<br/>SPI_FWRITE_QUAD = QSPI"]
    
    DLENReg["SPI_MOSI_DLEN_REG<br/>SPI_MISO_DLEN_REG<br/>Transfer length - 1"]
    
    CLKReg["SPI_CLOCK_REG<br/>Clock divisor fields<br/>Calculated by FreqToClockDiv()"]
    
    PINReg["SPI_PIN_REG / SPI_MISC_REG<br/>SPI_CK_IDLE_EDGE = CPOL<br/>CS disable flags"]
    
    W0Reg --> TransferOp["Transfer Operation"]
    CMDReg --> TransferOp
    USERReg --> TransferOp
    DLENReg --> TransferOp
    CLKReg --> TransferOp
    PINReg --> TransferOp
```

**DMA Control Registers**

```mermaid
graph LR
    DMAConf["SPI_DMA_CONF_REG<br/>SPI_DMA_TX_ENA<br/>SPI_OUTDSCR_BURST_EN<br/>SPI_OUT_DATA_BURST_EN"]
    
    OutLink["SPI_DMA_OUT_LINK_REG<br/>Descriptor address bits [19:0]<br/>SPI_OUTLINK_START trigger"]
    
    OutStatus["SPI_DMA_OUTSTATUS_REG<br/>SPI_DMA_OUTFIFO_EMPTY<br/>Transfer completion status"]
    
    DMAConf --> DMAOp["DMA Transfer"]
    OutLink --> DMAOp
    OutStatus --> DMAOp
```

### Transfer Primitive Functions

**writeCommand() - Single Command Write** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:314-354]()

```
while (*_spi_cmd_reg & SPI_USR);        // Wait previous transfer
*_spi_mosi_dlen_reg = bit_length - 1;   // Set length
*_spi_w0_reg = data;                    // Write data to buffer
*_gpio_reg_dc[0] = _mask_reg_dc;        // DC LOW (command)
*_spi_cmd_reg = SPI_EXECUTE;            // Trigger transfer
```

**writeData() - Single Data Write** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:356-395]()

Same sequence but uses `_gpio_reg_dc[1]` for DC HIGH (data mode).

**writeBytes() with DMA** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:672-716]()

```
_setup_dma_desc_links(data, length);              // Build descriptor chain
*dma_conf_reg = SPI_AHBM_RST | SPI_AHBM_FIFO_RST | SPI_OUT_RST;  // Reset DMA
*dma_conf_reg = SPI_OUTDSCR_BURST_EN | ...;       // Enable burst
*_spi_dma_out_link_reg = SPI_OUTLINK_START | ((int)&_dmadesc[0] & 0xFFFFF);  // Start DMA
while (*_spi_dma_outstatus_reg & SPI_DMA_OUTFIFO_EMPTY);  // Wait ready
*_spi_mosi_dlen_reg = (length << 3) - 1;          // Set bit length
*_gpio_reg_dc[dc] = _mask_reg_dc;                 // Set DC pin
*_spi_cmd_reg = SPI_EXECUTE;                      // Start transfer
```

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:314-395](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:630-734]()

---

### Clock Divisor Calculation and Caching

The SPI clock frequency is derived from APB bus clock through a divisor. The `FreqToClockDiv()` function [src/lgfx/v1/platforms/esp32/common.cpp:202-209]() calculates the `SPI_CLOCK_REG` value:

**FreqToClockDiv() Algorithm**

```
Input: fapb (APB frequency), hz (target frequency)

if (fapb <= hz):
    return SPI_CLK_EQU_SYSCLK  // Special value for 1:1 ratio

div_num = fapb / (1 + hz)      // Integer division
pre = div_num / 64             // Pre-divider (0-8191)
div_num = div_num / (pre + 1)  // Adjust for pre-divider

// Pack into SPI_CLOCK_REG format:
clockdiv = (div_num << 12) | ((div_num-1)>>1 << 6) | div_num | (pre << 18)
```

The packed value contains:
- Bits [17:0]: `div_num` (clock divider)
- Bits [23:18]: `pre` (pre-scaler)
- Bits [11:6]: `(div_num-1)>>1` (duty cycle)

**APB Frequency Detection** [src/lgfx/v1/platforms/esp32/common.cpp:188-200]()

```
rtc_cpu_freq_config_t conf;
rtc_clk_cpu_freq_get_config(&conf);
if (conf.freq_mhz >= 80) return 80000000;
return (conf.source_freq_mhz * 1000000) / conf.div;
```

Typically returns 80MHz for ESP32/S2/S3/C3 when CPU runs at 160MHz or higher.

**Clock Caching in beginTransaction()** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:243-253]()

```cpp
uint32_t freq_apb = getApbFrequency();
if (_last_freq_apb != freq_apb) {
    _last_freq_apb = freq_apb;
    _clkdiv_read = FreqToClockDiv(freq_apb, _cfg.freq_read);
    _clkdiv_write = FreqToClockDiv(freq_apb, _cfg.freq_write);
}
```

Only recalculates when APB frequency changes (e.g., CPU frequency scaling event). Stores divisors in `_clkdiv_write` and `_clkdiv_read` for reuse.

**Sources:** [src/lgfx/v1/platforms/esp32/common.cpp:188-209](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:243-253]()

---

## Transaction Management

Transactions acquire the SPI bus (if locking enabled), configure clock speed and mode, and prepare registers for data transfer.

```mermaid
stateDiagram-v2
    [*] --> Idle
    
    Idle --> Locked: beginTransaction()
    note right of Locked
        spi::beginTransaction() if use_lock
        Configure clock divisor
        Set SPI_USER_REG, SPI_PIN_REG
        Set DC pin to HIGH (data mode)
    end note
    
    Locked --> Writing: writeCommand/writeData
    Locked --> Reading: beginRead()
    
    Writing --> Writing: Multiple writes
    Reading --> Reading: readData/readBytes
    
    Writing --> Locked: After write
    Reading --> Locked: endRead()
    
    Locked --> Idle: endTransaction()
    note right of Idle
        Restore SPI_USER_REG for SD card
        Release bus lock
        DMA workaround on ESP32
    end note
```

## DMA Transfers Using Descriptor Chains

DMA transfers use the `lldesc_t` linked list descriptor structure defined in ESP-IDF ROM headers [rom/lldesc.h](). Each descriptor points to a data buffer and the next descriptor, forming a chain.

### lldesc_t Structure

**Descriptor Layout**

```mermaid
graph LR
    Desc["lldesc_t"]
    
    Field1["uint32_t packed<br/>size: 12 bits<br/>length: 12 bits<br/>owner: 1 bit<br/>eof: 1 bit"]
    
    Field2["uint8_t* buf<br/>Buffer address"]
    
    Field3["lldesc_t* qe.stqe_next<br/>Next descriptor pointer"]
    
    Desc --> Field1
    Desc --> Field2
    Desc --> Field3
```

The first `uint32_t` packs multiple fields [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1195]():
```
*(uint32_t*)dmadesc = size | (length << 12) | 0x80000000;
                       │        │               │
                       │        │               └─ owner=1 (DMA owns)
                       │        └─ Valid data length (12 bits)
                       └─ Buffer size (12 bits, max 4095)
```

### _setup_dma_desc_links() Implementation

**Descriptor Chain Building** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1180-1202]()

```
Input: data pointer, length in bytes

1. Calculate required descriptors: (length / SPI_MAX_DMA_LEN) + 1
2. Allocate _dmadesc array if needed
3. Loop through data in SPI_MAX_DMA_LEN (4095) byte chunks:
   
   while (len > SPI_MAX_DMA_LEN):
       dmadesc->size = SPI_MAX_DMA_LEN
       dmadesc->length = SPI_MAX_DMA_LEN
       dmadesc->owner = 1
       dmadesc->buf = data
       dmadesc->qe.stqe_next = dmadesc + 1
       data += SPI_MAX_DMA_LEN
       len -= SPI_MAX_DMA_LEN
       dmadesc++
   
4. Final descriptor:
   dmadesc->size = (len + 3) & ~3     // Round up to 4-byte boundary
   dmadesc->length = len
   dmadesc->eof = 1                   // Mark end of frame
   dmadesc->qe.stqe_next = nullptr
```

### DMA Queue Batching

**addDMAQueue() and execDMAQueue()** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:824-939]()

The DMA queue allows batching multiple `writeBytes()` calls into a single DMA operation:

1. **addDMAQueue()** [line 824-860]():
   - Builds descriptors in `_dma_queue` array
   - Accumulates `_dma_queue_bytes` total
   - Does not trigger DMA transfer

2. **execDMAQueue()** [line 862-939]():
   - Links all queued descriptors
   - Sets EOF on last descriptor
   - Swaps `_dma_queue` with `_dmadesc` (flip-buffer pattern)
   - Writes descriptor address to `SPI_DMA_OUT_LINK_REG`
   - Triggers transfer with `SPI_OUTLINK_START` bit

### Platform-Specific DMA Implementation

| Chip Family | DMA Type | Channel Detection | Register Base |
|-------------|----------|-------------------|---------------|
| **ESP32** | SPI DMA (2 channels) | Read `DPORT_SPI_DMA_CHAN_SEL_REG` bits | `SPI_DMA_OUT_LINK_REG` |
| **ESP32-S2** | Per-peripheral SPI DMA | Static peripheral module | `SPI_DMA_OUT_LINK_REG` |
| **ESP32-C3/S3/C6/P4** | GDMA (unified) | `search_dma_out_ch(peri_sel)` finds channel | `GDMA_OUT_LINK_CH0_REG + (ch * sizeof(channel))` |

**GDMA Channel Search** [src/lgfx/v1/platforms/esp32/common.cpp:270-294]()

For GDMA chips, the DMA channel assigned to SPI2/SPI3 must be found at runtime:
```cpp
for (int i = 0; i < SOC_GDMA_PAIRS_PER_GROUP_MAX; ++i) {
    bool hit = (*reg(DMA_OUT_PERI_SEL_CH0_REG + i * sizeof(GDMA.channel[0])) 
                & DMA_PERI_OUT_SEL_CH0_M) == peripheral_select;
    if (hit) return i;
}
```

Then calculate register addresses [Bus_SPI.cpp:190-191]():
```cpp
_spi_dma_out_link_reg = reg(DMA_OUT_LINK_CH0_REG + assigned_dma_ch * SIZE_OF_DMA_OUT_CH);
_spi_dma_outstatus_reg = reg(DMA_OUTFIFO_STATUS_CH0_REG + assigned_dma_ch * SIZE_OF_DMA_OUT_CH);
```

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:824-939](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1180-1202](), [src/lgfx/v1/platforms/esp32/common.cpp:270-294]()

---

## Write Operations

The Bus_SPI implementation provides several write methods optimized for different data patterns.

### Write Method Selection

```mermaid
graph TD
    Start["Write Request"] --> CheckLen{Length?}
    
    CheckLen -->|"<= 32 bits"| Single["writeCommand()<br/>writeData()<br/>Single register write"]
    CheckLen -->|"> 32 bits"| CheckPattern{Repeating<br/>pattern?}
    
    CheckPattern -->|Yes| Repeat["writeDataRepeat()<br/>Optimized for fills<br/>Ring buffer technique"]
    CheckPattern -->|No| CheckDMA{DMA enabled<br/>and available?}
    
    CheckDMA -->|Yes| DMAWrite["writeBytes(use_dma=true)<br/>DMA descriptor chain<br/>Zero-copy transfer"]
    CheckDMA -->|No| Manual["writeBytes(use_dma=false)<br/>Manual chunking<br/>32/64 byte blocks"]
    
    Single --> HW["SPI Hardware"]
    Repeat --> HW
    DMAWrite --> HW
    Manual --> HW
```

### writeDataRepeat() Optimization

For repeated data patterns (e.g., filling with a solid color), `writeDataRepeat()` uses a clever ring buffer technique:

**12-Byte Pattern Buffer** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:397-513]():
1. Create 12-byte pattern (96 bits) in registers W0, W1, W2
2. Extend to full 64-byte buffer by repeating pattern
3. For 16-bit colors: Use 512-bit ring buffer capability on ESP32
4. For 24-bit colors: Use 504-bit limit to avoid overflow
5. Send first chunk, then repeatedly trigger with same buffer

This eliminates CPU overhead of copying data for fill operations.

### writePixels() for Pixel Data

`writePixels()` handles color format conversion and optimization for pixel data:

**DMA Path** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:529-544]():
- Uses `_flip_buffer` to get DMA-capable memory
- Calls `param->fp_copy()` for color conversion
- Transfers in chunks (32 pixels for RGB565, 24 for RGB888)
- Doubles chunk size progressively to reduce overhead

**Non-DMA Path** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:548-627]():
- Uses 32-byte (ESP32) or 64-byte (C3/S3) buffer
- Alternates between low/high parts of W0-W15 registers (HIGHPART)
- Overlaps color conversion with SPI transfer
- ESP32-C3/S3 don't support HIGHPART, use linear approach

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:313-628]()

---

## DC Pin Control (Command vs Data Mode)

SPI displays use a separate Data/Command (DC) pin to distinguish register commands from pixel data. The `Bus_SPI` class controls this pin via atomic GPIO register writes.

### DC Pin Initialization

**config() Method DC Pin Setup** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:131-142]()

```cpp
if (_cfg.pin_dc < 0) {
    // No DC pin: write to dummy location
    _mask_reg_dc = 0;
    _gpio_reg_dc[0] = &_mask_reg_dc;
    _gpio_reg_dc[1] = &_mask_reg_dc;
} else {
    // Calculate bit mask for pin
    _mask_reg_dc = (1ul << (_cfg.pin_dc & 31));
    
    // Get register addresses for set/clear
    _gpio_reg_dc[0] = get_gpio_lo_reg(_cfg.pin_dc);  // GPIO_OUT_W1TC
    _gpio_reg_dc[1] = get_gpio_hi_reg(_cfg.pin_dc);  // GPIO_OUT_W1TS
}
```

The helper functions `get_gpio_lo_reg()` and `get_gpio_hi_reg()` [src/lgfx/v1/platforms/esp32/common.hpp:143-158]() return pointers to:
- `GPIO_OUT_W1TC_REG` / `GPIO_OUT_W1TC`: Write 1 to **clear** output bit
- `GPIO_OUT_W1TS_REG` / `GPIO_OUT_W1TS`: Write 1 to **set** output bit

For GPIO pins 32-39 on ESP32/S2, use `GPIO_OUT1_W1TC` and `GPIO_OUT1_W1TS` registers.

### Atomic DC Pin Switching

**dc_control() Helper** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:148-175]()

```cpp
void dc_control(bool flg) {
    auto reg = _gpio_reg_dc[flg];  // Select set (1) or clear (0) register
    auto mask = _mask_reg_dc;
    
    while (*_spi_cmd_reg & SPI_USR);  // Wait for SPI idle
    
    // Clear DMA state on GDMA chips
    #if defined (SOC_GDMA_SUPPORTED)
        if (_clear_dma_reg) {
            _clear_dma_reg = nullptr;
            *_clear_dma_reg = 0;
        }
    #endif
    
    *reg = mask;  // Atomic write to GPIO register
}
```

**Usage in writeCommand() and writeData()** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:320-351, 363-364]()

```cpp
// In writeCommand():
*_gpio_reg_dc[0] = _mask_reg_dc;  // DC LOW = command mode

// In writeData():
*_gpio_reg_dc[1] = _mask_reg_dc;  // DC HIGH = data mode
```

This single instruction atomic write eliminates function call overhead and read-modify-write cycles. The `W1TS` and `W1TC` registers only affect the bit specified by the mask, leaving other GPIO pins unchanged.

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:131-142](), [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:148-175](), [src/lgfx/v1/platforms/esp32/common.hpp:143-158]()

---

## Read Operations

Read operations switch the SPI peripheral to receive mode, handle dummy clock cycles, and retrieve data from hardware registers.

### Read Configuration

```mermaid
sequenceDiagram
    participant App as Application
    participant BusSPI as Bus_SPI
    participant SPI as SPI Registers
    
    App->>BusSPI: beginRead(dummy_bits)
    
    BusSPI->>SPI: Set SPI_USER_REG
    Note over SPI: SPI_USR_MISO enabled<br/>SPI_SIO if 3-wire mode
    
    BusSPI->>SPI: Set SPI_CLOCK_REG
    Note over SPI: Switch to _clkdiv_read
    
    alt dummy_bits > 0
        BusSPI->>BusSPI: Send dummy clocks
        Note over BusSPI: ESP32-C3/S3: Toggle CPOL<br/>Others: readData(dummy_bits)
    end
    
    App->>BusSPI: readData(bit_length)
    BusSPI->>SPI: Set SPI_MISO_DLEN_REG
    BusSPI->>SPI: Write SPI_EXECUTE
    BusSPI->>BusSPI: Poll SPI_CMD_REG
    BusSPI->>SPI: Read SPI_W0_REG
    BusSPI-->>App: Return data
    
    App->>BusSPI: endRead()
    BusSPI->>SPI: Restore write configuration
```

### readBytes() Implementation

**Small Reads (≤32 bytes)** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1024-1055]():
- Read 32 bytes at a time into SPI_W0_REG..SPI_W7_REG
- Copy to destination buffer
- For C3/S3: Use linear buffer approach
- For ESP32: Use HIGHPART ping-pong buffering

**DMA Reads** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1005-1020]():
- Setup descriptor chain with `_setup_dma_desc_links()`
- Configure `SPI_DMA_IN_LINK_REG` (input, not output)
- Enable `SPI_INDSCR_BURST_EN`
- Trigger with `SPI_INLINK_START`

**HIGHPART Technique** (ESP32 only):
- SPI peripheral has 16 words (64 bytes) of buffer
- HIGHPART flag selects upper 8 words (W8-W15)
- While reading into low part, process high part (parallel operation)

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:941-1086]()

---

## DC Pin Control for Command/Data Mode

SPI displays distinguish between commands and data using a separate DC (Data/Command) pin. The Bus_SPI class controls this pin through direct GPIO register writes for minimal overhead.

### DC Pin Register Setup

```mermaid
graph TB
    subgraph "DC Pin Configuration"
        PinNum["pin_dc from config_t"] --> Mask["Calculate bit mask<br/>_mask_reg_dc = 1 << (pin & 31)"]
        
        PinNum --> RegCalc["Calculate register addresses"]
        
        RegCalc --> HiReg["_gpio_reg_dc[1]<br/>GPIO_OUT_W1TS_REG<br/>Set bit to 1"]
        RegCalc --> LoReg["_gpio_reg_dc[0]<br/>GPIO_OUT_W1TC_REG<br/>Set bit to 0"]
    end
    
    subgraph "Runtime Usage"
        Mask --> Write["*_gpio_reg_dc[dc] = _mask_reg_dc"]
        Write --> GPIO["Direct GPIO output<br/>No function call overhead"]
    end
    
    HiReg --> Write
    LoReg --> Write
```

### Command vs Data Write Pattern

**Command Write** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:314-353]():
```
*_gpio_reg_dc[0] = _mask_reg_dc  // DC LOW = Command
// Write to SPI registers
```

**Data Write** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:356-395]():
```
*_gpio_reg_dc[1] = _mask_reg_dc  // DC HIGH = Data
// Write to SPI registers
```

The GPIO registers `GPIO_OUT_W1TS_REG` (write 1 to set) and `GPIO_OUT_W1TC_REG` (write 1 to clear) allow atomic bit manipulation without read-modify-write cycles. Writing the bit mask directly toggles only the target pin.

**DC Control Function** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:148-175]():
- Waits for SPI idle (SPI_USR bit clear)
- Clears previous DMA state (ESP32-S3/C3/C6)
- Writes to GPIO register atomically
- Inlined for zero overhead

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:113-155](), [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:148-175]()

---

## Platform-Specific Implementations

The ESP32 family has variations across chip generations that require conditional compilation and different register handling.

### Register Naming Differences

```mermaid
graph TB
    subgraph "ESP32 / ESP32-S2"
        ESP32_CMD["SPI_CMD_REG<br/>SPI_USR triggers transfer"]
        ESP32_UPDATE["No SPI_UPDATE bit"]
        ESP32_EXEC["SPI_EXECUTE = SPI_USR"]
    end
    
    subgraph "ESP32-C3 / ESP32-S3 / ESP32-C6 / ESP32-P4"
        C3_CMD["SPI_CMD_REG<br/>SPI_USR + SPI_UPDATE"]
        C3_UPDATE["SPI_UPDATE required<br/>before transfer"]
        C3_EXEC["SPI_EXECUTE = SPI_USR | SPI_UPDATE"]
    end
    
    subgraph "Buffer Access"
        ESP32_BUF["HIGHPART support<br/>W0-W15 registers<br/>32-byte ping-pong"]
        C3_BUF["No HIGHPART<br/>Linear W0-W15<br/>64-byte single"]
    end
    
    ESP32_CMD --> Exec1["Transfer Execution"]
    C3_CMD --> Exec1
    C3_UPDATE --> Exec1
    
    ESP32_BUF --> Transfer["Data Transfer"]
    C3_BUF --> Transfer
```

### Conditional Compilation Patterns

**SPI_EXECUTE Macro** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:67-73]():
```cpp
#if defined ( SPI_UPDATE )  // C3/S3/C6/P4
  static constexpr uint32_t SPI_EXECUTE = SPI_USR | SPI_UPDATE;
#else  // ESP32/S2
  static constexpr uint32_t SPI_EXECUTE = SPI_USR;
#endif
```

**DMA Channel Detection** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:177-198]():
```cpp
#if defined ( SOC_GDMA_SUPPORTED )
  // C3/S3/C6/P4: Search GDMA channels
  int assigned_dma_ch = search_dma_out_ch(peri_sel);
  _spi_dma_out_link_reg = reg(DMA_OUT_LINK_CH0_REG + offset);
#elif defined ( CONFIG_IDF_TARGET_ESP32 )
  // ESP32: Read DPORT register
  dma_ch = (*reg(DPORT_SPI_DMA_CHAN_SEL_REG) >> (spi_host * 2)) & 3;
#endif
```

**Write Optimization** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:548-627]():
- ESP32: 32-byte limit with HIGHPART ping-pong (2×16 bytes)
- C3/S3: 64-byte limit, linear access (no HIGHPART)

### ESP32-P4 Special Handling

**Peripheral Register Access** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:649-656]():
```cpp
#if defined ( CONFIG_IDF_TARGET_ESP32P4 )
  // P4 peripherals don't support memcpy, must use loop
  for (int i = 0; i < aligned_len >> 2; ++i) {
    spi_w0_reg[i] = ((uint32_t*)data)[i];
  }
#else
  memcpy((void*)spi_w0_reg, data, aligned_len);
#endif
```

### QSPI Support

**Quad SPI Mode** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:84-87](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:149-154]():
- Requires `pin_io0`, `pin_io1`, `pin_io2`, `pin_io3` configured
- Uses `SPI_FWRITE_QUAD` flag in `SPI_USER_REG`
- Commands sent in 1-bit mode, data in 4-bit mode
- Only available with ESP-IDF 4.4.0+ (excluding ESP32-P4)

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:113-822](), [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:67-73]()

---

## Performance Optimizations

The Bus_SPI implementation includes several performance optimizations that distinguish it from standard ESP-IDF usage.

### Zero-Copy DMA Transfers

```mermaid
graph TB
    subgraph "Standard Approach"
        AppBuf1["Application Buffer<br/>(may be in PSRAM)"]
        Copy1["memcpy to<br/>DMA-capable buffer"]
        DMABuf1["DMA Buffer<br/>(internal RAM)"]
        DMA1["DMA Transfer"]
        
        AppBuf1 --> Copy1
        Copy1 --> DMABuf1
        DMABuf1 --> DMA1
    end
    
    subgraph "M5GFX Optimization"
        Check["heap_capable_dma()<br/>check pointer"]
        
        AppBuf2A["Buffer in internal RAM"] --> Direct["Direct DMA<br/>use_dma=true"]
        AppBuf2B["Buffer in PSRAM"] --> FlipBuf["FlipBuffer<br/>allocate & copy"]
        
        Check --> AppBuf2A
        Check --> AppBuf2B
        
        FlipBuf --> DMA2["DMA Transfer"]
        Direct --> DMA2
    end
```

**FlipBuffer Strategy** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:529-543]():
- Allocates DMA-capable buffer on first use
- Reuses buffer across multiple transfers
- Progressive size doubling (32→64→128... pixels)
- Only copies when source is not DMA-capable

### Inline Register Access

**Critical Path Functions** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:143-146]():
```cpp
__attribute__ ((always_inline)) inline void exec_spi(void) {
  *_spi_cmd_reg = SPI_EXECUTE;
}

__attribute__ ((always_inline)) inline void wait_spi(void) {
  while (*_spi_cmd_reg & SPI_USR);
}
```

Forces compiler to inline these functions, eliminating function call overhead in critical paths.

### Overlapped Operations

**Ping-Pong Buffering** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:586-624]():
```
Cycle 1: Write data to W0-W7  | SPI idle
Cycle 2: SPI sends W0-W7      | Write data to W8-W15
Cycle 3: SPI sends W8-W15     | Write data to W0-W7
...
```

While SPI hardware transmits one buffer half, CPU prepares the other half. Reduces CPU idle time by ~50%.

**Color Conversion Overlap** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:575-581]():
- Convert next chunk of pixels while SPI sends current chunk
- `param->fp_copy()` runs during `wait_spi()`
- Hides color format conversion latency

### Clock Divisor Caching

**Avoid Recalculation** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:243-253]():
```cpp
if (_last_freq_apb != freq_apb) {
  _last_freq_apb = freq_apb;
  _clkdiv_read = FreqToClockDiv(freq_apb, _cfg.freq_read);
  _clkdiv_write = FreqToClockDiv(freq_apb, _cfg.freq_write);
}
```

Only recalculates divisors when APB frequency changes (CPU frequency scaling event). Typical case: calculate once at startup, use throughout lifetime.

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:240-253](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:515-627]()

---

## Usage Example

```cpp
// Configuration
lgfx::Bus_SPI::config_t bus_cfg;
bus_cfg.spi_host = SPI2_HOST;
bus_cfg.freq_write = 40000000;  // 40 MHz write
bus_cfg.freq_read  = 16000000;  // 16 MHz read
bus_cfg.pin_sclk = 18;
bus_cfg.pin_mosi = 23;
bus_cfg.pin_miso = 19;
bus_cfg.pin_dc   = 27;
bus_cfg.spi_mode = 0;
bus_cfg.dma_channel = SPI_DMA_CH_AUTO;

// Instantiate and initialize
lgfx::Bus_SPI bus;
bus.config(bus_cfg);
if (!bus.init()) {
  // Handle initialization error
}

// Transaction
bus.beginTransaction();

// Write command (8-bit)
bus.writeCommand(0x2A, 8);  // CASET

// Write data (32-bit)
bus.writeData(0x00000000, 32);  // X start/end

// Write pixel data
uint8_t pixel_buffer[320*240*2];  // RGB565
bus.writeBytes(pixel_buffer, sizeof(pixel_buffer), true, true);

// End transaction
bus.endTransaction();

// Cleanup
bus.release();
```

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:75-105](), [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:157-203]()

---

## Summary

The ESP32 SPI Bus Implementation provides high-performance display communication through:

| Feature | Implementation | Performance Benefit |
|---------|----------------|---------------------|
| **Direct Register Access** | Bypass ESP-IDF after init | 3-5× faster than driver calls |
| **DMA Descriptor Chains** | Zero-copy for large transfers | Eliminates CPU bottleneck |
| **Clock Caching** | Pre-calculate divisors | No runtime division operations |
| **Ping-Pong Buffering** | Overlap data prep with transfer | ~50% reduction in idle time |
| **Inline Critical Path** | `always_inline` register access | Zero function call overhead |
| **DC Pin Direct Write** | Atomic GPIO register manipulation | Single instruction command/data switch |
| **FlipBuffer Management** | Reusable DMA-capable allocations | Reduces heap fragmentation |

The implementation handles all ESP32 family variations (ESP32, S2, S3, C3, C6, P4) with conditional compilation, providing consistent interface across platforms while exploiting hardware-specific optimizations.

**Sources:** [src/lgfx/v1/platforms/esp32/Bus_SPI.cpp:1-1209](), [src/lgfx/v1/platforms/esp32/Bus_SPI.hpp:1-210]()