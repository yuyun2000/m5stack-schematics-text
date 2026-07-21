# Stamp-S3Bat Battery 电池状态

Stamp-S3Bat 电池，电源输入状态读取相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5StampS3Bat
- M5PM1 库版本 >= 1.0.7

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

static const uint8_t PIN_SCL            = 47;
static const uint8_t PIN_SDA            = 48;
static const uint8_t LED_COUNT          = 1;
static const uint8_t LED_BRIGHTNESS     = 64;
static const m5pm1_rgb_t LED_COLOR      = {0, LED_BRIGHTNESS, 0};
static const uint32_t PRINT_INTERVAL_MS = 2000;

static void printVoltages()
{
    uint16_t mv = 0;

    if (pm1.readVref(&mv) == M5PM1_OK) {
        Serial.printf("[PM1][I] Vref: %u mV (%.3f V)\r\n", mv, mv / 1000.0f);
    }
    if (pm1.readVbat(&mv) == M5PM1_OK) {
        Serial.printf("[PM1][I] VBAT: %u mV (%.3f V)\r\n", mv, mv / 1000.0f);
    }
    if (pm1.readVin(&mv) == M5PM1_OK) {
        Serial.printf("[PM1][I] VIN: %u mV (%.3f V)\r\n", mv, mv / 1000.0f);
    }
    if (pm1.read5VInOut(&mv) == M5PM1_OK) {
        Serial.printf("[PM1][I] 5V IN/OUT: %u mV (%.3f V)\r\n", mv, mv / 1000.0f);
    }
}

static bool setupLedDemo()
{
    pm1.gpioSetFunc(M5PM1_GPIO_NUM_0, M5PM1_GPIO_FUNC_OTHER);
    pm1.gpioSetDrive(M5PM1_GPIO_NUM_0, M5PM1_GPIO_DRIVE_PUSHPULL);
    pm1.gpioSetOutput(M5PM1_GPIO_NUM_0, true);
    pm1.pinMode(M5PM1_GPIO_NUM_0, M5PM1_OTHER);
    pm1.setLedEnLevel(true);
    pm1.setLedCount(LED_COUNT);
    pm1.setLedColor(0, LED_COLOR);
    pm1.refreshLeds();
    Serial.println("[DEMO] RGB on");
    delay(700);
    return true;
}

void setup()
{
    Serial.begin(115200);
    delay(300);
    Serial.println("[DEMO] Boot");

    Wire.end();
    Wire.begin(PIN_SDA, PIN_SCL, 100000U);
    if (pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, PIN_SDA, PIN_SCL, M5PM1_I2C_FREQ_400K) != M5PM1_OK) {
        Serial.println("[DEMO] PM1 init failed");
        return;
    }
    Serial.println("[DEMO] PM1 init ok");
    setupLedDemo();
}

void loop()
{
    static uint32_t lastMs = 0;
    if (millis() - lastMs >= PRINT_INTERVAL_MS) {
        lastMs = millis();
        printVoltages();
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_battery_example_01.jpg" width="50%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_battery_example_02.png" width="70%" />
