M5Unified Battery Monitoring and Charging Control

# Battery Monitoring and Charging Control

<details>
<summary>Relevant source files</summary>

The following files were used as context for generating this wiki page:

- [src/utility/Power_Class.cpp](src/utility/Power_Class.cpp)
- [src/utility/Power_Class.hpp](src/utility/Power_Class.hpp)

</details>



## Purpose and Scope

This document covers the battery monitoring and charging control functionality provided by the `Power_Class`. It explains how M5Unified abstracts battery voltage/current measurement, battery level calculation, and charge control across multiple hardware implementations including dedicated PMICs (Power Management ICs) and ADC-based monitoring systems. For general power management including sleep modes and power states, see [Sleep Modes and Power States](#3.3). For PMIC detection and initialization, see [PMIC Detection and Initialization](#3.1).

---

## Battery Monitoring Architecture

M5Unified supports two distinct battery monitoring strategies depending on the available hardware:

1. **PMIC-based monitoring**: Dedicated power management ICs (AXP192, AXP2101, IP5306, M5PM1, AW32001) provide built-in voltage, current, and charging status measurements via I2C registers
2. **ADC-based monitoring**: For boards without PMICs, the ESP32's ADC peripheral directly measures battery voltage through a voltage divider circuit

The `Power_Class` abstracts these differences through a unified API, with runtime selection based on the detected `pmic_t` type stored in `_pmic`.

```mermaid
graph TB
    subgraph "Power_Class API Layer"
        API_Voltage["getBatteryVoltage()"]
        API_Current["getBatteryCurrent()"]
        API_Level["getBatteryLevel()"]
        API_Charging["isCharging()"]
    end
    
    subgraph "PMIC Implementations"
        AXP192["AXP192_Class<br/>Core2/StickC/Tough"]
        AXP2101["AXP2101_Class<br/>CoreS3/Core2v1.1"]
        IP5306["IP5306_Class<br/>Original M5Stack"]
        M5PM1["M5PM1 Protocol<br/>StickS3"]
        AW32001["AW32001_Class<br/>NessoN1"]
    end
    
    subgraph "ADC Monitoring"
        ADC_Raw["_getBatteryAdcRaw()<br/>ESP32 ADC peripheral"]
        ADC_Ratio["_adc_ratio<br/>Voltage divider scaling"]
        ADC_Channels["_batAdcCh / _batAdcUnit<br/>ADC channel configuration"]
    end
    
    subgraph "Specialized Monitors"
        INA226["INA226_Class<br/>Tab5/StampPLC<br/>High-precision current"]
        INA3221["INA3221_Class<br/>Core2v1.1<br/>Multi-channel"]
        BQ27220["BQ27220_Class<br/>NessoN1<br/>Fuel gauge"]
    end
    
    API_Voltage --> AXP192
    API_Voltage --> AXP2101
    API_Voltage --> IP5306
    API_Voltage --> M5PM1
    API_Voltage --> AW32001
    API_Voltage --> ADC_Raw
    
    API_Current --> AXP192
    API_Current --> AXP2101
    API_Current --> INA226
    API_Current --> INA3221
    
    API_Level --> AXP192
    API_Level --> AXP2101
    API_Level --> IP5306
    API_Level --> ADC_Raw
    API_Level --> BQ27220
    
    API_Charging --> AXP192
    API_Charging --> AXP2101
    API_Charging --> IP5306
    API_Charging --> M5PM1
    API_Charging --> AW32001
    
    ADC_Raw --> ADC_Ratio
    ADC_Raw --> ADC_Channels
    
    style API_Voltage fill:#f9f9f9
    style API_Current fill:#f9f9f9
    style API_Level fill:#f9f9f9
    style API_Charging fill:#f9f9f9
```

**Sources**: [src/utility/Power_Class.cpp:1227-1309](), [src/utility/Power_Class.cpp:1360-1421](), [src/utility/Power_Class.cpp:1423-1500](), [src/utility/Power_Class.cpp:1633-1685](), [src/utility/Power_Class.cpp:1725-1779]()

---

## Voltage Measurement

### PMIC-Based Voltage Reading

Each PMIC provides battery voltage through dedicated ADC channels accessible via I2C registers. The `getBatteryVoltage()` method returns voltage in millivolts (mV).

| PMIC Type | Implementation | Board Examples | Return Format |
|-----------|---------------|----------------|---------------|
| `pmic_axp192` | `Axp192.getBatteryVoltage()` | M5Stack Core2, StickC, Tough | Volts * 1000 |
| `pmic_axp2101` | `Axp2101.getBatteryVoltage()` | CoreS3, Core2 v1.1 | Volts * 1000 |
| `pmic_ip5306` | Not supported | Original M5Stack | 0 |
| `pmic_m5pm1` | I2C registers 0x22-0x23 | StickS3 | Direct mV |
| `pmic_aw32001` | `Bq27220.getVoltage_mV()` | NessoN1 | Direct mV |

```mermaid
graph LR
    subgraph "getBatteryVoltage() Switch"
        Entry["getBatteryVoltage()"]
    end
    
    subgraph "PMIC Drivers"
        AXP192_Read["Axp192.getBatteryVoltage()"]
        AXP2101_Read["Axp2101.getBatteryVoltage()"]
        M5PM1_Read["M5.In_I2C.readRegister<br/>addr=0x6E reg=0x22-0x23"]
        BQ27220_Read["Bq27220.getVoltage_mV()"]
    end
    
    subgraph "ADC Path"
        ADC_Path["_getBatteryAdcRaw()"]
        Ratio["_adc_ratio scaling"]
    end
    
    subgraph "Specialized"
        INA226_Read["Ina226.getBusVoltage() * 1000<br/>Tab5"]
        PowerHub_Read["I2C 0x50 reg=0x30-0x31<br/>PowerHub"]
    end
    
    Entry -->|"pmic_axp192"| AXP192_Read
    Entry -->|"pmic_axp2101"| AXP2101_Read
    Entry -->|"pmic_m5pm1"| M5PM1_Read
    Entry -->|"pmic_aw32001"| BQ27220_Read
    Entry -->|"pmic_adc"| ADC_Path
    Entry -->|"board=Tab5"| INA226_Read
    Entry -->|"board=PowerHub"| PowerHub_Read
    
    ADC_Path --> Ratio
```

**Sources**: [src/utility/Power_Class.cpp:1360-1421]()

### ADC-Based Voltage Reading

Boards without PMICs use the ESP32's internal ADC to measure battery voltage through a voltage divider. The `_getBatteryAdcRaw()` method handles ADC configuration and reading, with board-specific initialization setting `_batAdcCh`, `_batAdcUnit`, and `_adc_ratio`.

#### ADC Configuration Per Board

| Board | ADC Channel | ADC Unit | `_adc_ratio` | Notes |
|-------|-------------|----------|--------------|-------|
| M5Paper | `ADC1_GPIO35_CHANNEL` | 1 | 2.0 | [src/utility/Power_Class.cpp:279-282]() |
| M5PaperS3 | `ADC1_GPIO3_CHANNEL` | 1 | 2.0 | [src/utility/Power_Class.cpp:198-204]() |
| M5Capsule | `ADC1_GPIO6_CHANNEL` | 1 | 2.0 | [src/utility/Power_Class.cpp:206-211]() |
| M5Cardputer | `ADC1_GPIO10_CHANNEL` | 1 | 2.0 | [src/utility/Power_Class.cpp:221-227]() |
| CoreInk | `ADC1_GPIO35_CHANNEL` | 1 | 4.922 | [src/utility/Power_Class.cpp:268-274]() |
| TimerCam | `ADC1_GPIO38_CHANNEL` | 1 | 1.513 | [src/utility/Power_Class.cpp:261-265]() |
| StickCPlus2 | `ADC1_GPIO38_CHANNEL` | 1 | 2.0 | [src/utility/Power_Class.cpp:303-309]() |

#### ADC Reading Implementation

The `_getBatteryAdcRaw()` method provides abstraction for ESP-IDF version differences:

- **ESP-IDF v5.x**: Uses `adc_oneshot` API with calibration schemes (curve fitting or line fitting)
- **ESP-IDF v4.x**: Uses legacy `adc1_get_raw()` with `esp_adc_cal_characterize()`

Both paths return calibrated voltage in millivolts, which is then multiplied by `_adc_ratio` to compensate for the voltage divider:

```
Battery Voltage (mV) = _getBatteryAdcRaw() * _adc_ratio
```

**Sources**: [src/utility/Power_Class.cpp:1227-1309](), [src/utility/Power_Class.cpp:53-513]()

---

## Current Measurement

Battery current measurement is only available on boards with PMICs or dedicated current sense ICs. Current is reported in milliamps (mA), with positive values indicating charging and negative values indicating discharge.

### Current Measurement Implementations

```mermaid
graph TB
    subgraph "getBatteryCurrent() Method"
        Entry["getBatteryCurrent()"]
    end
    
    subgraph "AXP192 Implementation"
        AXP192_Charge["Axp192.getBatteryChargeCurrent()"]
        AXP192_Discharge["Axp192.getBatteryDischargeCurrent()"]
        AXP192_Compare["Compare and return<br/>max magnitude with sign"]
    end
    
    subgraph "AXP2101 Implementations"
        AXP2101_CoreS3["CoreS3: return 0<br/>No current sensing"]
        AXP2101_Core2["Core2 v1.1:<br/>Ina3221[0].getCurrent(0)<br/>CH1 = BAT"]
    end
    
    subgraph "Board-Specific"
        Tab5_Current["Tab5:<br/>Ina226.getShuntCurrent() * 1000"]
        PowerHub_Current["PowerHub:<br/>I2C 0x50 reg=0x32-0x33<br/>signed int16"]
    end
    
    Entry -->|"pmic_axp192"| AXP192_Charge
    AXP192_Charge --> AXP192_Discharge
    AXP192_Discharge --> AXP192_Compare
    
    Entry -->|"pmic_axp2101 + CoreS3"| AXP2101_CoreS3
    Entry -->|"pmic_axp2101 + Core2"| AXP2101_Core2
    
    Entry -->|"board_M5Tab5"| Tab5_Current
    Entry -->|"board_M5PowerHub"| PowerHub_Current
    
    Entry -->|"Other boards"| Return0["return 0"]
```

**Key Implementation Details**:

1. **AXP192**: Reads both charge and discharge currents separately, returns the larger magnitude with appropriate sign [src/utility/Power_Class.cpp:1643-1649]()

2. **AXP2101 on CoreS3**: Returns 0 as the CoreS3 lacks current sensing hardware [src/utility/Power_Class.cpp:1655-1656]()

3. **AXP2101 on Core2 v1.1**: Uses external INA3221 chip, reads channel 0 (battery current) and converts to mA [src/utility/Power_Class.cpp:1660-1661]()

4. **M5Tab5**: Uses INA226 high-precision current shunt monitor [src/utility/Power_Class.cpp:1670-1671]()

5. **M5PowerHub**: Reads signed 16-bit current from custom I2C protocol, negates for correct sign [src/utility/Power_Class.cpp:1676-1678]()

**Sources**: [src/utility/Power_Class.cpp:1633-1685]()

---

## Battery Level Calculation

The `getBatteryLevel()` method converts battery voltage to a percentage (0-100%) using either PMIC-reported levels or voltage-based estimation.

### Level Calculation Algorithm

For boards without native battery level reporting, voltage is linearly mapped:

```
level = (voltage_mV - 3300) * 100 / (4150 - 3350)
Clamped to [0, 100]
```

This assumes:
- **Minimum voltage**: 3300 mV (0% battery)
- **Maximum voltage**: 4150 mV (100% battery)
- **Linear discharge curve** between these points

```mermaid
graph TB
    subgraph "getBatteryLevel() Flow"
        Entry["getBatteryLevel()"]
    end
    
    subgraph "Native Level Reporting"
        IP5306_Level["IP5306:<br/>Ip5306.getBatteryLevel()"]
        AXP2101_Level["AXP2101:<br/>Axp2101.getBatteryLevel()"]
    end
    
    subgraph "Voltage-Based Calculation"
        Get_Voltage["Get voltage in mV"]
        Tab5_Scale["Tab5: divide by 2<br/>2S Li-Po adjustment"]
        PowerHub_Scale["PowerHub: divide by 2"]
        ADC_Read["ADC boards:<br/>_getBatteryAdcRaw() * _adc_ratio"]
        AXP192_Read["AXP192:<br/>Axp192.getBatteryVoltage() * 1000"]
        M5PM1_Read["M5PM1:<br/>getBatteryVoltage()"]
        BQ27220_Read["BQ27220:<br/>Bq27220.getVoltage_F() * 1000"]
        
        Calculate["level = (mv - 3300) * 100 / 850"]
        Clamp["Clamp to [0, 100]"]
    end
    
    Entry -->|"pmic_ip5306"| IP5306_Level
    Entry -->|"pmic_axp2101"| AXP2101_Level
    
    Entry -->|"pmic_axp192"| AXP192_Read
    Entry -->|"pmic_m5pm1"| M5PM1_Read
    Entry -->|"pmic_aw32001"| BQ27220_Read
    Entry -->|"pmic_adc"| ADC_Read
    Entry -->|"board_M5Tab5"| Get_Voltage
    Entry -->|"board_M5PowerHub"| Get_Voltage
    
    AXP192_Read --> Get_Voltage
    M5PM1_Read --> Get_Voltage
    BQ27220_Read --> Get_Voltage
    ADC_Read --> Get_Voltage
    Get_Voltage -->|"Tab5"| Tab5_Scale
    Get_Voltage -->|"PowerHub"| PowerHub_Scale
    Tab5_Scale --> Calculate
    PowerHub_Scale --> Calculate
    Get_Voltage --> Calculate
    Calculate --> Clamp
    
    IP5306_Level --> Return
    AXP2101_Level --> Return
    Clamp --> Return["Return level"]
```

**Special Cases**:

- **M5Tab5**: Uses 2S Li-Po battery (7.4V nominal), so voltage is divided by 2 before calculation [src/utility/Power_Class.cpp:1479-1481]()
- **M5PowerHub**: Also uses 2S configuration [src/utility/Power_Class.cpp:1485-1487]()
- **NessoN1 (BQ27220)**: Returns NaN on error, which is converted to -1 [src/utility/Power_Class.cpp:1434-1439]()

**Sources**: [src/utility/Power_Class.cpp:1423-1500]()

---

## Charging Control

### Charge Enable/Disable

The `setBatteryCharge(bool enable)` method controls whether the battery charging circuit is active. Implementation varies by PMIC:

| PMIC Type | Implementation | Register/Pin |
|-----------|---------------|--------------|
| `pmic_ip5306` | `Ip5306.setBatteryCharge(enable)` | I2C register control |
| `pmic_axp192` | `Axp192.setBatteryCharge(enable)` | I2C register control |
| `pmic_axp2101` | `Axp2101.setBatteryCharge(enable)` | I2C register control |
| `pmic_m5pm1` | I2C register 0x06 bit 0 | Direct bit manipulation |
| `pmic_aw32001` | `Aw32001.setBatteryCharge(enable)` | Dedicated charger IC |
| M5Tab5 | IO Expander 1 pin 7 (CHG_EN) | GPIO control |
| M5PowerHub | I2C 0x50 register 0x06 | Custom protocol |

**M5PM1 Implementation Example** [src/utility/Power_Class.cpp:1529-1540]():
```
Register 0x06 bit 0: 1=enable charging, 0=disable charging
Read-modify-write pattern to preserve other bits
```

**Sources**: [src/utility/Power_Class.cpp:1502-1563]()

### Charge Current Limiting

The `setChargeCurrent(uint16_t max_mA)` method sets the maximum charging current in milliamps. Each PMIC implements current limiting differently:

```mermaid
graph TB
    subgraph "setChargeCurrent(max_mA)"
        Entry["setChargeCurrent(max_mA)"]
    end
    
    subgraph "PMIC Implementations"
        IP5306_Current["IP5306:<br/>Ip5306.setChargeCurrent(max_mA)"]
        AXP192_Current["AXP192:<br/>Axp192.setChargeCurrent(max_mA)"]
        AXP2101_Current["AXP2101:<br/>Axp2101.setChargeCurrent(max_mA)"]
        AW32001_Current["AW32001:<br/>Aw32001.setChargeCurrent(max_mA)"]
    end
    
    subgraph "Tab5 Special Logic"
        Tab5_0mA["max_mA == 0:<br/>CHG_EN=LOW, QC_EN=HIGH<br/>Disable charging"]
        Tab5_500mA["max_mA == 500:<br/>CHG_EN=HIGH, QC_EN=HIGH<br/>Standard USB charging"]
        Tab5_1000mA["max_mA == 1000:<br/>CHG_EN=HIGH, QC_EN=LOW<br/>Quick Charge enabled"]
    end
    
    Entry -->|"pmic_ip5306"| IP5306_Current
    Entry -->|"pmic_axp192"| AXP192_Current
    Entry -->|"pmic_axp2101"| AXP2101_Current
    Entry -->|"pmic_aw32001"| AW32001_Current
    
    Entry -->|"board_M5Tab5"| Tab5_Logic
    Tab5_Logic -->|"0"| Tab5_0mA
    Tab5_Logic -->|"500"| Tab5_500mA
    Tab5_Logic -->|"1000"| Tab5_1000mA
```

**M5Tab5 Current Control** [src/utility/Power_Class.cpp:1596-1622]():
- Uses IO Expander to control CHG_EN (pin 7) and QC_EN (pin 5)
- Supports discrete levels: 0mA (disabled), 500mA (standard), 1000mA (Quick Charge)
- Quick Charge mode enables higher current draw from USB-C PD sources

**Sources**: [src/utility/Power_Class.cpp:1565-1631]()

### Charge Voltage Limiting

The `setChargeVoltage(uint16_t max_mV)` method sets the maximum battery charge voltage in millivolts. This protects the battery from overcharging.

| PMIC | Method | Typical Values |
|------|--------|----------------|
| IP5306 | `Ip5306.setChargeVoltage(max_mV)` | 4100-4360 mV |
| AXP192 | `Axp192.setChargeVoltage(max_mV)` | 4100-4360 mV |
| AXP2101 | `Axp2101.setChargeVoltage(max_mV)` | 4100-4360 mV |

**Note**: This function is not implemented for ADC-based boards (M5Paper, CoreInk, etc.) as they lack charging control hardware.

**Sources**: [src/utility/Power_Class.cpp:1687-1723]()

### Charging Status Detection

The `isCharging()` method returns an `is_charging_t` enum indicating the current charging state:

```cpp
enum is_charging_t {
    is_discharging = 0,  // Battery is discharging
    is_charging = 1,      // Battery is charging
    charge_unknown = 2    // Status cannot be determined
}
```

#### Charging Detection Methods

```mermaid
graph TB
    subgraph "isCharging() Detection Methods"
        Entry["isCharging()"]
    end
    
    subgraph "PMIC Status Register"
        IP5306_Status["IP5306:<br/>Ip5306.isCharging()"]
        AXP192_Status["AXP192:<br/>Axp192.isCharging()"]
        AXP2101_Status["AXP2101:<br/>Axp2101.isCharging()"]
        AW32001_Status["AW32001:<br/>Aw32001.isCharging()"]
    end
    
    subgraph "GPIO Pin Sensing"
        StickS3_GPIO["StickS3:<br/>M5PM1 reg 0x12 bit 0<br/>PM1_G0 input pin<br/>LOW=charging"]
        PaperS3_GPIO["PaperS3:<br/>GPIO4 CHG_STAT<br/>LOW=charging"]
        Tab5_GPIO["Tab5:<br/>IO Expander pin 6<br/>HIGH=charging"]
    end
    
    subgraph "Current-Based Detection"
        PowerHub_Current["PowerHub:<br/>getBatteryCurrent() < -10mA<br/>Negative current = charging"]
    end
    
    Entry -->|"pmic_ip5306"| IP5306_Status
    Entry -->|"pmic_axp192"| AXP192_Status
    Entry -->|"pmic_axp2101"| AXP2101_Status
    Entry -->|"pmic_aw32001"| AW32001_Status
    
    Entry -->|"board_M5StickS3"| StickS3_GPIO
    Entry -->|"board_M5PaperS3"| PaperS3_GPIO
    Entry -->|"board_M5Tab5"| Tab5_GPIO
    Entry -->|"board_M5PowerHub"| PowerHub_Current
    
    Entry -->|"Other boards"| Unknown["return charge_unknown"]
```

**Implementation Details**:

1. **PMIC-based detection** [src/utility/Power_Class.cpp:1739-1749](): PMICs provide dedicated status registers indicating charge state

2. **M5StickS3** [src/utility/Power_Class.cpp:1756-1761](): Uses M5PM1 GPIO0 as input pin for charge status (configured during `begin()` at [src/utility/Power_Class.cpp:186-193]())

3. **M5PaperS3** [src/utility/Power_Class.cpp:1764-1765](): Reads GPIO4 pin configured as input [src/utility/Power_Class.cpp:198]()

4. **M5Tab5** [src/utility/Power_Class.cpp:1771-1773](): Reads IO Expander 1 pin 6 (CHG_STAT), HIGH indicates charging

5. **M5PowerHub** [src/utility/Power_Class.cpp:1767-1768](): Infers charging from battery current (< -10mA threshold)

**Sources**: [src/utility/Power_Class.cpp:1725-1779]()

---

## Board-Specific Implementation Matrix

| Board | Voltage Source | Current Source | Level Method | Charge Control |
|-------|---------------|----------------|--------------|----------------|
| M5Stack Core2 | AXP192 | AXP192 | Voltage-based | AXP192 registers |
| M5Stack Core2 v1.1 | AXP2101 | INA3221 CH0 | AXP2101 native | AXP2101 registers |
| M5Stack CoreS3 | AXP2101 | None (returns 0) | AXP2101 native | AXP2101 registers |
| M5Stack CoreS3 SE | AXP2101 | None (returns 0) | AXP2101 native | AXP2101 registers |
| M5Stack Tough | AXP192 | AXP192 | Voltage-based | AXP192 registers |
| M5Stack | IP5306 | None | IP5306 native | IP5306 registers |
| M5StickC | AXP192 | AXP192 | Voltage-based | AXP192 registers |
| M5StickC Plus | AXP192 | AXP192 | Voltage-based | AXP192 registers |
| M5StickC Plus2 | ADC GPIO38 | None | Voltage-based | None |
| M5StickS3 | M5PM1 I2C | None | Voltage-based | M5PM1 reg 0x06 |
| M5Paper | ADC GPIO35 | None | Voltage-based | None |
| M5PaperS3 | ADC GPIO3 | None | Voltage-based | GPIO4 status |
| CoreInk | ADC GPIO35 | None | Voltage-based | None |
| M5Capsule | ADC GPIO6 | None | Voltage-based | None |
| M5Cardputer | ADC GPIO10 | None | Voltage-based | None |
| M5Tab5 | INA226 bus | INA226 shunt | Voltage (2S) | IO Expander |
| M5PowerHub | I2C 0x50 | I2C 0x50 | Voltage (2S) | I2C 0x50 |
| M5StampPLC | INA226 bus | INA226 shunt | None | None |
| Arduino NessoN1 | BQ27220 | None | BQ27220 fuel gauge | AW32001 |
| M5TimerCam | ADC GPIO38 | None | Voltage-based | None |

**Sources**: [src/utility/Power_Class.cpp:53-513](), [src/utility/Power_Class.cpp:1360-1421](), [src/utility/Power_Class.cpp:1423-1500](), [src/utility/Power_Class.cpp:1633-1685](), [src/utility/Power_Class.cpp:1725-1779]()

---

## API Usage Examples

### Reading Battery Status

```cpp
// Read battery voltage
int16_t voltage_mV = M5.Power.getBatteryVoltage();
if (voltage_mV > 0) {
    M5.Display.printf("Battery: %d mV\n", voltage_mV);
}

// Read battery level percentage
int32_t level = M5.Power.getBatteryLevel();
if (level >= 0) {
    M5.Display.printf("Level: %d%%\n", level);
} else {
    M5.Display.println("Level not available");
}

// Check charging status
auto charging = M5.Power.isCharging();
if (charging == Power_Class::is_charging_t::is_charging) {
    M5.Display.println("Charging...");
} else if (charging == Power_Class::is_charging_t::is_discharging) {
    M5.Display.println("Discharging");
}

// Read battery current (if supported)
int32_t current_mA = M5.Power.getBatteryCurrent();
if (current_mA != 0) {
    M5.Display.printf("Current: %d mA\n", current_mA);
}
```

### Controlling Charging

```cpp
// Set charge current to 390mA (for Core2 battery)
M5.Power.setChargeCurrent(390);

// Set charge voltage to 4.2V
M5.Power.setChargeVoltage(4200);

// Enable battery charging
M5.Power.setBatteryCharge(true);

// Disable charging (for testing or specific use cases)
M5.Power.setBatteryCharge(false);
```

### VBUS Voltage Monitoring

For boards with PMICs, USB input voltage can be monitored:

```cpp
// Read VBUS voltage (USB input)
int16_t vbus_mV = M5.Power.getVBUSVoltage();
if (vbus_mV > 0) {
    M5.Display.printf("USB: %d mV\n", vbus_mV);
} else {
    M5.Display.println("VBUS not supported or not connected");
}
```

**Sources**: [src/utility/Power_Class.hpp:148-181]()