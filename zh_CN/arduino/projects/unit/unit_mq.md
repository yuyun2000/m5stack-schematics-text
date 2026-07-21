# Unit MQ Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-MQ](https://github.com/m5stack/M5Unit-MQ)

- 使用到的硬件产品：
  - [Core2 v1.1](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)
  - [Unit MQ](https://shop.m5stack.com/products/ina226-10a-current-voltage-power-monitor-unit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2%20v1.1/img-9eb726ec-5729-42c3-9cce-e06140856095.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_04.webp" width="20%">

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，为了让用户更方便地使用，M5Stack 官方提供了引脚兼容性表，方便用户查看，请根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U199" type="UNIT"></ProductCompatible>

## 3. 案例程序

本教程中使用的主控设备为 Core2 v1.1 ，搭配 Unit MQ。本电流电压检测单元采用 I2C 的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的 I2C 引脚为 `G33 (SCL)`，`G32 (SDA)`。

?> 说明 | 1.加热控制引脚**高电平持续 20s** 后，传感器获取数据有效，一旦切换为低电平数据有效标志即刻为 0，数据有效标志与加热控制引脚高低电平关系请见[示意图](/zh_CN/unit/Unit_MQ#数据有效标志与各模式下控制引脚电平状态关系图示)。  
2.检测到的可燃气体`浓度越大`，Unit MQ 反馈的`电压越高`，有关电压与浓度 ppm 信息，可参考[MQ-5数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Gas_Sensor_MQ-5_datasheet.pdf)。

- Unit MQ 可配置两种加热模式：连续加热模式（`HEAT_MODE_CONTINUOUS`）和间歇加热模式（`HEAT_MODE_PIN_SWITCH`），能够获取的数据有传感器电压、ADC 参考电压、设备温度等，可根据需要选用。  
- 数据获取 API 如下：

``` cpp
getValidTags()                            // Data Valid Tag
getReferenceVoltage()                     // Reference Voltage
getNTCADC12bit()                          // NTC ADC
getNTCVoltage()                           // NTC Voltage
getNTCResistance()                        // NTC Resistance
getNTCTemperature(uint16_t ntcResistance) // NTC Temperature
getMQADC12bit()                           // Sensor ADC 
getMQVoltage()                            // Sensor Voltage 
```

### 连续加热模式

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include "m5_unit_mq.hpp"

#define I2C_SDA   (32)     /**< I2C SDA pin number */
#define I2C_SCL   (33)     /**< I2C SCL pin number */
#define I2C_SPEED (400000) /**< I2C bus speed in Hz */

M5UnitMQ unitMQ; /**< Instance of the Unit MQ gas sensor */

/* Sensor status and data variables */
static led_status_t ledStatus        = LED_WORK_STATUS_OFF;  /**< Current LED state */
static heat_mode_t heatMode          = HEAT_MODE_CONTINUOUS; /**< Current heating mode */
static mq_adc_valid_tags_t validTags = VALID_TAG_INVALID;    /**< MQ ADC data validity flag */
static uint8_t highLevelTime         = 0;                    /**< High-level heating time (not used here) */
static uint8_t lowLevelTime          = 0;                    /**< Low-level heating time (not used here) */
static uint16_t mqADC12bit           = 0;                    /**< MQ sensor raw ADC value (12-bit) */
static uint16_t ntcADC12bit          = 0;                    /**< NTC sensor raw ADC value (12-bit) */
static uint16_t ntcResistance        = 0;                    /**< Calculated NTC resistance in Ohms */
static uint16_t referenceVoltage     = 0;                    /**< Reference voltage in millivolts */
static uint16_t mqVoltage            = 0;                    /**< Calculated MQ sensor voltage in millivolts */
static uint16_t ntcVoltage           = 0;                    /**< Calculated NTC sensor voltage in millivolts */
float temperature                    = 0.0f;                 /**< Calculated temperature in degrees Celsius */
static uint8_t firmwareVersion       = 0;                    /**< Sensor firmware version */

/**
 * @brief Arduino setup function, runs once at startup.
 *
 * Initializes the M5 hardware and Unit MQ sensor with I2C configuration.
 * Retries sensor initialization until successful.
 * Sets sensor heating mode and turns on the sensor LED.
 */
void setup()
{
    M5.begin();
    M5.Display.setRotation(1);
    M5.Display.clear(TFT_WHITE);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setTextColor(TFT_BLACK);
    Serial.begin(115200);

    Serial.println("========== Unit MQ Initialization ==========");

    // Initialize Unit MQ sensor on I2C bus, retry until success
    while (!unitMQ.begin(&Wire, UNIT_MQ_I2C_BASE_ADDR, I2C_SDA, I2C_SCL, I2C_SPEED)) {
        Serial.println("[ERROR] Unit MQ initialization failed! Retrying...");
        delay(1000);
    }
    Serial.println("[INFO] Unit MQ initialization succeeded.");

    // Set the heating mode to continuous heating
    unitMQ.setHeatMode(HEAT_MODE_CONTINUOUS);
    Serial.println("[INFO] Heating mode set to CONTINUOUS.");

    // Turn on the sensor's LED indicator
    unitMQ.setLEDState(LED_WORK_STATUS_ON);
    Serial.println("[INFO] LED status set to ON.");
}

/**
 * @brief Arduino main loop function, runs repeatedly.
 *
 * Reads sensor data including LED status, valid tags, firmware version,
 * NTC sensor ADC and temperature, and MQ sensor ADC and voltage if valid.
 * Prints all the relevant data to Serial for monitoring.
 */
void loop()
{
    // Get the current heating mode
    heatMode = unitMQ.getHeatMode();

    // Retrieve current LED state
    ledStatus = unitMQ.getLEDState();

    // Retrieve validity tag for MQ sensor data
    validTags = unitMQ.getValidTags();

    // Retrieve sensor firmware version
    firmwareVersion = unitMQ.getFirmwareVersion();

    // Always read NTC sensor data and calculate temperature
    ntcADC12bit      = unitMQ.getNTCADC12bit();
    referenceVoltage = unitMQ.getReferenceVoltage();
    ntcVoltage       = unitMQ.getNTCVoltage();
    ntcResistance    = unitMQ.getNTCResistance();
    temperature      = unitMQ.getNTCTemperature(ntcResistance);

    // Print sensor status and readings
    Serial.println("======== Unit MQ Status ========");
    Serial.printf("Firmware Version   : %d\n", firmwareVersion);
    Serial.printf("Heating Mode       : %s\n", heatMode == HEAT_MODE_CONTINUOUS ? "CONTINUOUS" : "SWITCH");
    Serial.printf("LED Status         : %s\n", ledStatus == LED_WORK_STATUS_ON ? "ON" : "OFF");
    Serial.printf("NTC ADC (12-bit)   : %u\n", ntcADC12bit);
    Serial.printf("Reference Voltage  : %u mV\n", referenceVoltage);
    Serial.printf("NTC Voltage        : %u mV\n", ntcVoltage);
    Serial.printf("NTC Resistance     : %u Ohm\n", ntcResistance);
    Serial.printf("Temperature        : %.2f °C\n", temperature);

    M5.Display.clear(TFT_WHITE);
    M5.Display.drawCenterString("Unit MQ Status", M5.Display.width()/2, 0);
    M5.Display.setCursor(0, 20);
    M5.Display.printf("Firmware Version : %d\n", firmwareVersion);
    M5.Display.printf("Heating Mode     : %s\n", heatMode == HEAT_MODE_CONTINUOUS ? "CONTINUOUS" : "SWITCH");
    M5.Display.printf("LED Status       : %s\n", ledStatus == LED_WORK_STATUS_ON ? "ON" : "OFF");
    M5.Display.printf("NTC ADC (12-bit) : %u\n", ntcADC12bit);
    M5.Display.printf("Reference Voltage: %u mV\n", referenceVoltage);
    M5.Display.printf("NTC Voltage      : %u mV\n", ntcVoltage);
    M5.Display.printf("NTC Resistance   : %u Ohm\n", ntcResistance);
    M5.Display.printf("Temperature      : %.2f C\n", temperature);

    // Print MQ sensor readings only if data is valid
    if (validTags == VALID_TAG_VALID) {
        mqADC12bit = unitMQ.getMQADC12bit();
        mqVoltage  = unitMQ.getMQVoltage();

        Serial.printf("Valid Tags         : 0x%02X (MQ data valid)\n", validTags);
        Serial.printf("MQ ADC (12-bit)    : %u\n", mqADC12bit);
        Serial.printf("MQ Voltage         : %u mV\n", mqVoltage);

        M5.Display.printf("Valid Tags : 0x%02X (valid)\n", validTags);
        M5.Display.printf("MQ ADC (12-bit)  : %u\n", mqADC12bit);
        M5.Display.printf("MQ Voltage       : %u mV\n", mqVoltage);
    } else {
        Serial.printf("Valid Tags         : 0x%02X (MQ data invalid)\n", validTags);
        Serial.println("[WARNING] MQ data invalid. Skipping MQ readings.");

        M5.Display.printf("Valid Tags : 0x%02X (invalid)\n", validTags);
        M5.Display.println("[WARNING] MQ data invalid. Skipping MQ readings.");
    }

    Serial.println("================================\n");

    delay(1000);  // Delay 1 second before next reading
}
```

### 间歇加热模式

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.H>
#include "m5_unit_mq.hpp"

#define I2C_SDA   (32)     /**< I2C SDA pin number */
#define I2C_SCL   (33)     /**< I2C SCL pin number */
#define I2C_SPEED (400000) /**< I2C bus speed in Hz */

#define HIGH_LEVEL_TIME (30) /**< High level duration for pin switch mode in seconds */
#define LOW_LEVEL_TIME  (10)  /**< Low level duration for pin switch mode in seconds */

M5UnitMQ unitMQ; /**< Instance of the Unit MQ gas sensor class */

/* Sensor and system state variables */
static led_status_t ledStatus        = LED_WORK_STATUS_OFF;  /**< Current LED status */
static heat_mode_t heatMode          = HEAT_MODE_PIN_SWITCH; /**< Heating mode of the sensor */
static mq_adc_valid_tags_t validTags = VALID_TAG_INVALID;    /**< Validity tag for MQ sensor ADC data */
static uint8_t highLevelTime         = 0;                    /**< High-level time setting for pin switch heating */
static uint8_t lowLevelTime          = 0;                    /**< Low-level time setting for pin switch heating */
static uint16_t mqAdc12bit           = 0;                    /**< Raw 12-bit ADC reading from MQ sensor */
static uint16_t ntcAdc12bit          = 0;                    /**< Raw 12-bit ADC reading from NTC temperature sensor */
static uint16_t ntcResistance        = 0;                    /**< Calculated resistance of NTC sensor (Ohms) */
static uint16_t referenceVoltage     = 0;                    /**< Reference voltage value (mV) */
static uint16_t mqVoltage            = 0;                    /**< Calculated voltage of MQ sensor output (mV) */
static uint16_t ntcVoltage           = 0;                    /**< Calculated voltage of NTC sensor output (mV) */
float temperature                    = 0.0f;                 /**< Calculated temperature in Celsius */
static uint8_t firmwareVersion       = 0;                    /**< Firmware version of the Unit MQ sensor */

void setup()
{
    M5.begin();
    M5.Display.setRotation(1);
    M5.Display.clear(TFT_WHITE);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setTextColor(TFT_BLACK);
    Serial.begin(115200);

    Serial.println("========== Unit MQ Initialization ==========");

    // Initialize the Unit MQ sensor with I2C settings.
    // Retry initialization until successful.
    while (!unitMQ.begin(&Wire, UNIT_MQ_I2C_BASE_ADDR, I2C_SDA, I2C_SCL, I2C_SPEED)) {
        Serial.println("[ERROR] Unit MQ initialization failed! Retrying...");
        delay(1000);
    }
    Serial.println("[INFO] Unit MQ initialization succeeded.");

    // Set heating mode to PIN SWITCH mode, which alternates heating between HIGH and LOW levels.
    unitMQ.setHeatMode(HEAT_MODE_PIN_SWITCH);
    Serial.println("[INFO] Heating mode set to PIN SWITCH mode.");

    // Configure the durations for high and low heating levels in PIN SWITCH mode.
    unitMQ.setPulseTime(HIGH_LEVEL_TIME, LOW_LEVEL_TIME);
    Serial.println("[INFO] Pin level switch time set to 30s HIGH and 5s LOW.");

    // Turn on the sensor LED indicator.
    unitMQ.setLEDState(LED_WORK_STATUS_ON);
    Serial.println("[INFO] LED status set to ON.");
}

void loop()
{
    // Get the current heating mode
    heatMode = unitMQ.getHeatMode();

    // Read the current LED status from the sensor.
    ledStatus = unitMQ.getLEDState();

    // Retrieve validity tag indicating whether MQ sensor data is reliable.
    validTags = unitMQ.getValidTags();

    // Get the firmware version from the sensor.
    firmwareVersion = unitMQ.getFirmwareVersion();

    // Always read NTC-related sensor data regardless of MQ data validity.
    ntcAdc12bit      = unitMQ.getNTCADC12bit();                  // Raw ADC for NTC sensor
    referenceVoltage = unitMQ.getReferenceVoltage();             // Reference voltage for ADC
    ntcVoltage       = unitMQ.getNTCVoltage();                   // Calculated voltage across NTC
    ntcResistance    = unitMQ.getNTCResistance();                // Calculated resistance of NTC thermistor
    temperature      = unitMQ.getNTCTemperature(ntcResistance);  // Convert resistance to temperature

    Serial.println("======== Unit MQ Status ========");
    Serial.printf("Firmware Version   : %d\n", firmwareVersion);
    Serial.printf("Heating Mode       : %s\n", heatMode == HEAT_MODE_CONTINUOUS ? "CONTINUOUS" : "SWITCH");
    Serial.printf("LED Status         : %s\n", ledStatus == LED_WORK_STATUS_ON ? "ON" : "OFF");

    // Print detailed NTC sensor parameters
    Serial.printf("NTC ADC (12-bit)   : %u\n", ntcAdc12bit);
    Serial.printf("Reference Voltage  : %u mV\n", referenceVoltage);
    Serial.printf("NTC Voltage        : %u mV\n", ntcVoltage);
    Serial.printf("NTC Resistance     : %u Ohm\n", ntcResistance);
    Serial.printf("Temperature        : %.2f °C\n", temperature);

    M5.Display.clear(TFT_WHITE);
    M5.Display.drawCenterString("Unit MQ Status", M5.Display.width()/2, 0);
    M5.Display.setCursor(0, 20);
    M5.Display.printf("Firmware Version : %d\n", firmwareVersion);
    M5.Display.printf("Heating Mode     : %s\n", heatMode == HEAT_MODE_CONTINUOUS ? "CONTINUOUS" : "SWITCH");
    M5.Display.printf("LED Status       : %s\n", ledStatus == LED_WORK_STATUS_ON ? "ON" : "OFF");
    M5.Display.printf("NTC ADC (12-bit) : %u\n", ntcAdc12bit);
    M5.Display.printf("Reference Voltage: %u mV\n", referenceVoltage);
    M5.Display.printf("NTC Voltage      : %u mV\n", ntcVoltage);
    M5.Display.printf("NTC Resistance   : %u Ohm\n", ntcResistance);
    M5.Display.printf("Temperature      : %.2f C\n", temperature);

    // If MQ sensor data is valid, read and print MQ ADC and voltage values.
    if (validTags == VALID_TAG_VALID) {
        mqAdc12bit = unitMQ.getMQADC12bit();
        mqVoltage  = unitMQ.getMQVoltage();

        Serial.printf("Valid Tags         : 0x%02X (MQ data valid)\n", validTags);
        Serial.printf("MQ ADC (12-bit)    : %u\n", mqAdc12bit);
        Serial.printf("MQ Voltage         : %u mV\n", mqVoltage);

        M5.Display.printf("Valid Tags : 0x%02X (valid)\n", validTags);
        M5.Display.printf("MQ ADC (12-bit)  : %u\n", mqAdc12bit);
        M5.Display.printf("MQ Voltage       : %u mV\n", mqVoltage);
    } else {
        // If MQ data is invalid, log a warning and skip readings.
        Serial.printf("Valid Tags         : 0x%02X (MQ data invalid)\n", validTags);
        Serial.println("[WARNING] MQ data invalid. Skipping MQ readings.");

        M5.Display.printf("Valid Tags : 0x%02X (invalid)\n", validTags);
        M5.Display.println("[WARNING] MQ data invalid.\nSkipping MQ readings.");
    }

    Serial.println("================================\n");

    delay(1000);  // Wait for 1 second before next update
}
```

## 4. 编译上传

- 选中设备端口（详情请参考 [程序编译与烧录](/zh_CN/arduino/m5core2/program)），点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ__arduino_example.png" width="70%">

## 5. 测量结果

Unit MQ 两种模式效果如下所示：

- 连续加热模式

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_continuous_mode.jpg" width="35%">

- 间歇加热模式

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_pin_switch_mode.jpg" width="35%">
