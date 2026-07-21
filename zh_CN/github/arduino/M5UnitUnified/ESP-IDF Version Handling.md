M5UnitUnified ESP-IDF Version Handling

# ESP-IDF Version Handling

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/m5_unit_component/adapter_gpio.cpp](src/m5_unit_component/adapter_gpio.cpp)
- [src/m5_unit_component/adapter_gpio.hpp](src/m5_unit_component/adapter_gpio.hpp)
- [src/m5_unit_component/adapter_gpio_v1.cpp](src/m5_unit_component/adapter_gpio_v1.cpp)
- [src/m5_unit_component/adapter_gpio_v2.cpp](src/m5_unit_component/adapter_gpio_v2.cpp)
- [src/m5_unit_component/adapter_gpio_v2.hpp](src/m5_unit_component/adapter_gpio_v2.hpp)
- [src/m5_unit_component/identify_functions.hpp](src/m5_unit_component/identify_functions.hpp)
- [src/m5_unit_component/types.hpp](src/m5_unit_component/types.hpp)

</details>



## Purpose and Scope

This document describes how M5UnitUnified maintains compatibility across different ESP-IDF versions, focusing on conditional compilation strategies for hardware peripherals. The library supports ESP-IDF versions from 3.2.0 through 5.x, automatically selecting appropriate APIs for the RMT peripheral and ADC subsystem based on the detected ESP-IDF version.

For information about the GPIO adapter implementations themselves, see [GPIO and RMT](#4.2). For build configuration details, see [Build System](#6).

---

## Version Detection System

The library uses a centralized version detection mechanism in `identify_functions.hpp` to determine which ESP-IDF APIs are available at compile time.

### Detection Mechanism

The version detection logic checks for the presence of `esp_idf_version.h` and extracts the version number:

**Version Detection Flow:**

```mermaid
flowchart TD
    Start["Compilation Begins"]
    CheckHeader{"__has_include<br/>(esp_idf_version.h)?"}
    IncludeHeader["#include<br/>esp_idf_version.h<br/>ESP_IDF_VERSION defined"]
    DefineDefault["#define ESP_IDF_VERSION<br/>ESP_IDF_VERSION_VAL(3, 2, 0)"]
    CheckVersion{"ESP_IDF_VERSION<br/>>= 5.0.0?"}
    DefineV2["#define<br/>M5_UNIT_UNIFIED_USING_RMT_V2<br/>M5_UNIT_UNIFIED_USING_ADC_ONESHOT"]
    NoDefine["No version-specific<br/>macros defined<br/>(Use legacy APIs)"]
    Compile["Conditional compilation<br/>proceeds"]
    
    Start --> CheckHeader
    CheckHeader -->|Yes| IncludeHeader
    CheckHeader -->|No| DefineDefault
    IncludeHeader --> CheckVersion
    DefineDefault --> CheckVersion
    CheckVersion -->|Yes| DefineV2
    CheckVersion -->|No| NoDefine
    DefineV2 --> Compile
    NoDefine --> Compile
    
    style CheckVersion fill:#f9f9f9
    style DefineV2 fill:#f9f9f9
```

**Sources:** [src/m5_unit_component/identify_functions.hpp:13-26]()

### Version Macros

The library defines two primary feature detection macros:

| Macro | ESP-IDF Version | Purpose |
|-------|----------------|---------|
| `M5_UNIT_UNIFIED_USING_RMT_V2` | ≥ 5.0.0 | Enables RMT v2 API usage |
| `M5_UNIT_UNIFIED_USING_ADC_ONESHOT` | ≥ 5.0.0 | Enables ADC oneshot API |

These macros control conditional compilation throughout the GPIO adapter implementation, ensuring that the appropriate API is used for each ESP-IDF version.

**Sources:** [src/m5_unit_component/identify_functions.hpp:21-25]()

---

## RMT Peripheral Version Handling

The Remote Control Transceiver (RMT) peripheral underwent a major API redesign in ESP-IDF 5.0. M5UnitUnified supports both the legacy (v1) and modern (v2) APIs through dual implementations.

### API Differences

```mermaid
graph TB
    subgraph "ESP-IDF < 5.0 (RMT v1)"
        V1Header["#include soc/rmt_struct.h"]
        V1Type["rmt_item32_t"]
        V1Config["rmt_config_t<br/>channel, clk_div"]
        V1Init["rmt_config()<br/>rmt_driver_install()"]
        V1TX["rmt_write_items()"]
        V1RX["xRingbufferReceive()"]
    end
    
    subgraph "ESP-IDF >= 5.0 (RMT v2)"
        V2Header["#include driver/rmt_types.h<br/>driver/rmt_tx.h<br/>driver/rmt_rx.h"]
        V2Type["rmt_symbol_word_t"]
        V2Config["rmt_tx_channel_config_t<br/>resolution_hz, mem_block_symbols"]
        V2Init["rmt_new_tx_channel()<br/>rmt_enable()"]
        V2TX["rmt_transmit()"]
        V2RX["Callback-based<br/>on_recv_done"]
    end
    
    V1Header -.-> V1Type
    V1Type -.-> V1Config
    V1Config -.-> V1Init
    V1Init -.-> V1TX
    V1Init -.-> V1RX
    
    V2Header -.-> V2Type
    V2Type -.-> V2Config
    V2Config -.-> V2Init
    V2Init -.-> V2TX
    V2Init -.-> V2RX
```

**Sources:** [src/m5_unit_component/types.hpp:16-20](), [src/m5_unit_component/types.hpp:113-117]()

### Type Aliasing Strategy

The `m5_rmt_item_t` alias provides a unified interface across versions:

```mermaid
flowchart LR
    Code["Application Code<br/>Uses: m5_rmt_item_t"]
    Macro{"M5_UNIT_UNIFIED_<br/>USING_RMT_V2<br/>defined?"}
    V2Type["using m5_rmt_item_t =<br/>rmt_symbol_word_t"]
    V1Type["using m5_rmt_item_t =<br/>rmt_item32_t"]
    
    Code --> Macro
    Macro -->|Yes| V2Type
    Macro -->|No| V1Type
```

Both `rmt_symbol_word_t` and `rmt_item32_t` share the same memory layout with four fields: `duration0`, `level0`, `duration1`, `level1`. This structural compatibility allows the same high-level code to work with both versions through type aliasing.

**Sources:** [src/m5_unit_component/types.hpp:113-117]()

### Implementation Selection

The library maintains separate implementation files that are conditionally compiled:

**Compilation Units:**

```mermaid
graph TB
    Compile["Compilation"]
    CheckV2{"M5_UNIT_UNIFIED_<br/>USING_RMT_V2?"}
    
    subgraph V1["adapter_gpio_v1.cpp"]
        V1Guard["#if !defined(M5_UNIT_UNIFIED_USING_RMT_V2)"]
        V1Class["class GPIOImplV1"]
        V1Methods["rmt_config()<br/>rmt_write_items()<br/>xRingbufferReceive()"]
        V1Constructor["AdapterGPIO::AdapterGPIO()<br/>new GPIOImplV1()"]
        V1Error["#error if RMT_CHANNEL_0 defined"]
    end
    
    subgraph V2["adapter_gpio_v2.cpp"]
        V2Guard["#if defined(M5_UNIT_UNIFIED_USING_RMT_V2)"]
        V2Class["class GPIOImplV2"]
        V2Methods["rmt_new_tx_channel()<br/>rmt_transmit()<br/>callback-based RX"]
        V2Constructor["AdapterGPIO::AdapterGPIO()<br/>new GPIOImplV2()"]
        V2Error["#error if RMT_CHANNEL_0 defined"]
    end
    
    Compile --> CheckV2
    CheckV2 -->|No| V1Guard
    CheckV2 -->|Yes| V2Guard
    V1Guard --> V1Class
    V1Class --> V1Methods
    V1Methods --> V1Constructor
    V1Constructor --> V1Error
    V2Guard --> V2Class
    V2Class --> V2Methods
    V2Methods --> V2Constructor
    V2Constructor --> V2Error
```

The `AdapterGPIO` constructor is defined in exactly one compilation unit based on the version macro. Each implementation file includes error-checking preprocessor directives to detect accidental mixing of v1 and v2 APIs:

- **v1 check:** [src/m5_unit_component/adapter_gpio_v1.cpp:307-309]()
- **v2 check:** [src/m5_unit_component/adapter_gpio_v2.cpp:418-420]()

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:13](), [src/m5_unit_component/adapter_gpio_v2.cpp:12]()

### Configuration Translation

The library uses a unified `adapter_config_t` structure that works across both RMT versions. Internal translation functions convert this to version-specific configuration structures:

**Configuration Flow:**

```mermaid
flowchart TD
    UserConfig["gpio::adapter_config_t<br/>(Unified Configuration)"]
    
    subgraph Translation["Version-Specific Translation"]
        CheckRMT{"RMT Version?"}
        V1Func["to_rmt_config_tx/rx()<br/>Returns: rmt_config_t<br/>Fields: channel, clk_div"]
        V2Func["to_rmt_tx/rx_config()<br/>Returns: rmt_tx/rx_channel_config_t<br/>Fields: resolution_hz, mem_block_symbols"]
    end
    
    subgraph API["ESP-IDF API Calls"]
        V1API["rmt_config(&config)"]
        V2API["rmt_new_tx_channel(&config, &handle)"]
    end
    
    UserConfig --> CheckRMT
    CheckRMT -->|v1| V1Func
    CheckRMT -->|v2| V2Func
    V1Func --> V1API
    V2Func --> V2API
```

Key translation functions:
- **v1:** `to_rmt_config_tx()`, `to_rmt_config_rx()` [src/m5_unit_component/adapter_gpio_v1.cpp:49-74]()
- **v2:** `to_rmt_tx_config()`, `to_rmt_rx_config()` [src/m5_unit_component/adapter_gpio_v2.cpp:23-47]()

**Sources:** [src/m5_unit_component/types.hpp:80-110](), [src/m5_unit_component/adapter_gpio_v1.cpp:49-74](), [src/m5_unit_component/adapter_gpio_v2.cpp:23-47]()

---

## ADC API Handling

ESP-IDF 5.0 introduced the oneshot ADC API, replacing the legacy ADC1/ADC2 functions. The library conditionally compiles the appropriate ADC code path based on `M5_UNIT_UNIFIED_USING_ADC_ONESHOT`.

### ADC API Comparison

**Version-Specific Implementations:**

```mermaid
flowchart TB
    Start["read_analog(pin)"]
    CheckVersion{"M5_UNIT_UNIFIED_<br/>USING_ADC_ONESHOT<br/>defined?"}
    
    subgraph Legacy["ESP-IDF < 5.0 (Legacy ADC)"]
        L1["adc1_config_width(ADC_WIDTH_BIT_12)"]
        L2["adc1_config_channel_atten(channel, ADC_ATTEN_DB_12)"]
        L3["value = adc1_get_raw(channel)"]
        L4["OR: adc2_get_raw(channel, ADC_WIDTH_BIT_12, &value)"]
    end
    
    subgraph Oneshot["ESP-IDF >= 5.0 (Oneshot API)"]
        O1["adc_oneshot_unit_init_cfg_t<br/>unit_id, clk_src, ulp_mode"]
        O2["adc_oneshot_new_unit(&init_config, &handle)"]
        O3["adc_oneshot_chan_cfg_t<br/>atten=ADC_ATTEN_DB_12<br/>bitwidth=ADC_BITWIDTH_DEFAULT"]
        O4["adc_oneshot_config_channel(handle, channel, &cfg)"]
        O5["adc_oneshot_read(handle, channel, &raw)"]
        O6["adc_oneshot_del_unit(handle)"]
    end
    
    Start --> CheckVersion
    CheckVersion -->|No| L1
    L1 --> L2
    L2 --> L3
    L3 --> L4
    
    CheckVersion -->|Yes| O1
    O1 --> O2
    O2 --> O3
    O3 --> O4
    O4 --> O5
    O5 --> O6
```

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:391-461]()

### ADC Implementation Details

The legacy API uses global configuration:

```cpp
// ESP-IDF 4.x
adc1_config_width(ADC_WIDTH_BIT_12);
adc1_config_channel_atten(channel, ADC_ATTEN_DB_12);
value = adc1_get_raw(channel);
```

The oneshot API requires handle management and explicit cleanup:

```cpp
// ESP-IDF 5.x
adc_oneshot_unit_handle_t adc_handle{};
adc_oneshot_unit_init_cfg_t init_config = {
    .unit_id = unit,
    .clk_src = ADC_RTC_CLK_SRC_DEFAULT,  // or ADC_DIGI_CLK_SRC_DEFAULT for C6
    .ulp_mode = ADC_ULP_MODE_DISABLE
};
adc_oneshot_new_unit(&init_config, &adc_handle);
// ... configure channel, read value ...
adc_oneshot_del_unit(adc_handle);
```

The library handles clock source selection for ESP32-C6, which requires `ADC_DIGI_CLK_SRC_DEFAULT` instead of `ADC_RTC_CLK_SRC_DEFAULT`:

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:406-438](), [src/m5_unit_component/adapter_gpio.cpp:440-460]()

### GPIO-to-ADC Channel Mapping

The library maintains chip-specific lookup tables to map GPIO pin numbers to ADC channels:

| Target | GPIO Range | ADC Units | Table Size |
|--------|-----------|-----------|------------|
| ESP32 | 0-39 | ADC1 (0-9), ADC2 (10-19) | 40 entries |
| ESP32-S2/S3 | 0-20 | ADC1 (0-9), ADC2 (10-19) | 21 entries |
| ESP32-C3/C2 | 0-5 | ADC1 (0-4), ADC2 (10) | 6 entries |
| ESP32-C6/H2 | 0-6 | ADC1 (0-6) | 7 entries |
| ESP32-P4 | 16-23, 49-54 | ADC1 (0-7), ADC2 (10-15) | 55 entries |

The `gpio_to_adc_channel()` function uses these tables to translate pin numbers to ADC channel indices, with values ≥10 indicating ADC2 channels (ESP-IDF 4.x only).

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:147-305]()

---

## Compatibility Patterns

The library employs several patterns to maintain compatibility across ESP-IDF versions while keeping code maintainable.

### Preprocessor Pragma Messages

Compilation messages inform developers which version paths are being taken:

```mermaid
flowchart LR
    Compile["Compilation Start"]
    Check1{"RMT_V2<br/>defined?"}
    Check2{"DAC<br/>supported?"}
    Check3{"ADC<br/>supported?"}
    
    Msg1["#pragma message<br/>'Using RMT v2,Oneshot'"]
    Msg2["#pragma message<br/>'Using RMT v1'"]
    Msg3["#pragma message<br/>'DAC supported'"]
    Msg4["#pragma message<br/>'ADC supported'"]
    Msg5["#pragma message<br/>'ADC Not supported'"]
    
    Compile --> Check1
    Check1 -->|Yes| Msg1
    Check1 -->|No| Msg2
    Msg1 --> Check2
    Msg2 --> Check2
    Check2 -->|Yes| Msg3
    Check2 -->|No| Check3
    Msg3 --> Check3
    Check3 -->|Yes| Msg4
    Check3 -->|No| Msg5
```

**Example output during compilation:**
```
Using RMT v2,Oneshot
DAC supported
ADC supported
```

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:14-40]()

### Peripheral Capability Detection

The library uses SOC capability macros to detect hardware features:

| Macro | Purpose | Example |
|-------|---------|---------|
| `SOC_DAC_SUPPORTED` | DAC peripheral availability | ESP32 has DAC, ESP32-C6 does not |
| `SOC_ADC_SUPPORTED` | ADC peripheral availability | All targets support ADC |
| `SOC_ADC_PERIPH_NUM` | Number of ADC units | ESP32 has 2, ESP32-C6 has 1 |
| `SOC_RMT_MEM_WORDS_PER_CHANNEL` | RMT memory block size | Varies by chip |

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:22-40](), [src/m5_unit_component/adapter_gpio.cpp:399-404](), [src/m5_unit_component/adapter_gpio_v2.cpp:15]()

### Clock Source Selection

ESP-IDF version and target-specific clock source handling:

```mermaid
graph TB
    GetClock["esp_clk_apb_freq()"]
    
    subgraph V1["RMT v1"]
        V1Calc["calculate_rmt_clk_div()<br/>Returns: clk_div (1-255)"]
        V1Include["#include esp32/clk.h"]
    end
    
    subgraph V2["RMT v2"]
        V2Calc["calculate_rmt_resolution_hz()<br/>Returns: resolution_hz"]
        V2Include["#include esp_private/esp_clk.h"]
        V2ClkSrc["RMT_CLK_SRC_DEFAULT<br/>ESP32: APB<br/>ESP32-S3: APB<br/>ESP32-C6: PLL_F80M"]
    end
    
    GetClock -.-> V1Calc
    GetClock -.-> V2Calc
    V1Calc -.-> V1Include
    V2Calc -.-> V2Include
    V2Calc -.-> V2ClkSrc
```

The v1 implementation includes `<esp32/clk.h>` for `esp_clk_apb_freq()`, while v2 uses `<esp_private/esp_clk.h>`. Clock source defaults vary by chip but are abstracted through `RMT_CLK_SRC_DEFAULT`.

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:15-16](), [src/m5_unit_component/adapter_gpio_v2.cpp:14](), [src/m5_unit_component/adapter_gpio.cpp:324-345]()

### Error Detection Guards

Both v1 and v2 implementations include cross-contamination detection:

```cpp
#if defined(M5_UNIT_UNIFIED_USING_RMT_V2) && defined(RMT_CHANNEL_0)
#error "RMT v1 is mixed in with RMT v2 even though RMT v2 is used"
#endif
```

The `RMT_CHANNEL_0` macro is defined in RMT v1 headers (`soc/rmt_struct.h`) but not in v2 headers. This preprocessor check catches accidental inclusion of v1 headers when compiling v2 code, preventing subtle bugs from API mismatches.

**Sources:** [src/m5_unit_component/adapter_gpio_v1.cpp:307-309](), [src/m5_unit_component/adapter_gpio_v2.cpp:418-420]()

---

## Platform-Specific Considerations

### ESP32-C6 ADC Clock Source

ESP32-C6 requires special handling for ADC clock source selection:

```cpp
#if defined(CONFIG_IDF_TARGET_ESP32C6)
    adc_oneshot_unit_init_cfg_t init_config = {
        .unit_id = unit,
        .clk_src = ADC_DIGI_CLK_SRC_DEFAULT,  // Not ADC_RTC_CLK_SRC_DEFAULT
        .ulp_mode = ADC_ULP_MODE_DISABLE
    };
#else
    adc_oneshot_unit_init_cfg_t init_config = {
        .unit_id = unit,
        .clk_src = ADC_RTC_CLK_SRC_DEFAULT,
        .ulp_mode = ADC_ULP_MODE_DISABLE
    };
#endif
```

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:412-418]()

### ESP32-P4 Hysteresis Control

ESP32-P4 introduces additional GPIO configuration fields:

```cpp
#if defined(CONFIG_IDF_TARGET_ESP32P4)
    .hys_ctrl_mode = GPIO_HYS_SOFT_ENABLE,
#endif
```

These fields are conditionally included in all `gpio_config_t` structures to maintain compatibility with P4 targets.

**Sources:** [src/m5_unit_component/adapter_gpio.cpp:53-120]()

### RMT v2 Version-Gated Features

ESP-IDF 5.3.0 and 5.4.0 introduced additional configuration flags:

```cpp
#if ESP_IDF_VERSION >= ESP_IDF_VERSION_VAL(5, 3, 0)
    out.flags.en_partial_rx = 0;
#endif

#if ESP_IDF_VERSION >= ESP_IDF_VERSION_VAL(5, 4, 0)
    M5_LIB_LOGI("allow_pd : %u", cfg.flags.allow_pd);
#endif
```

The library gracefully handles these additions by conditionally accessing fields only when available.

**Sources:** [src/m5_unit_component/adapter_gpio_v2.cpp:67-69](), [src/m5_unit_component/adapter_gpio_v2.cpp:84-86](), [src/m5_unit_component/adapter_gpio_v2.cpp:100-102](), [src/m5_unit_component/adapter_gpio_v2.cpp:119-121]()

---

## Summary Table

| Feature | ESP-IDF < 5.0 | ESP-IDF ≥ 5.0 | Detection Macro |
|---------|--------------|---------------|-----------------|
| RMT API | v1 (channel-based) | v2 (handle-based) | `M5_UNIT_UNIFIED_USING_RMT_V2` |
| RMT Item Type | `rmt_item32_t` | `rmt_symbol_word_t` | Aliased as `m5_rmt_item_t` |
| RMT Configuration | `rmt_config_t` | `rmt_tx/rx_channel_config_t` | Version-specific translation |
| ADC API | `adc1_get_raw()` | `adc_oneshot_read()` | `M5_UNIT_UNIFIED_USING_ADC_ONESHOT` |
| Clock Access | `<esp32/clk.h>` | `<esp_private/esp_clk.h>` | Include path differs |
| Implementation File | `adapter_gpio_v1.cpp` | `adapter_gpio_v2.cpp` | One compiled per version |

**Sources:** All sections above