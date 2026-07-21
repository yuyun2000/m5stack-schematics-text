# Stamp-S3Bat RGB LED 状态灯

Stamp-S3Bat 案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5StampS3Bat
- M5PM1 库版本 >= 1.0.7

### RGB LED

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

#define PIN_SCL 47
#define PIN_SDA 48

static const uint8_t LED_COUNT  = 1;
static const uint8_t BRIGHTNESS = 64;

static const m5pm1_rgb_t COLOR_RED   = {BRIGHTNESS, 0, 0};
static const m5pm1_rgb_t COLOR_GREEN = {0, BRIGHTNESS, 0};
static const m5pm1_rgb_t COLOR_BLUE  = {0, 0, BRIGHTNESS};

void setup()
{
    Serial.begin(115200);
    delay(2000);

    Wire.end();
    Wire.begin(PIN_SDA, PIN_SCL, 100000U);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, PIN_SDA, PIN_SCL, M5PM1_I2C_FREQ_400K);

    if (err != M5PM1_OK) {
        Serial.printf("[PM1][E] PM1 initialization failed: %d\r\n", err);
        while (true) {
            delay(1000);
        }
    }
    Serial.printf("[PM1][I] PM1 initialization successful\r\n");

    // 配置方案1
    pm1.gpioSetFunc(M5PM1_GPIO_NUM_0, M5PM1_GPIO_FUNC_OTHER);
    pm1.gpioSetDrive(M5PM1_GPIO_NUM_0, M5PM1_GPIO_DRIVE_PUSHPULL);
    pm1.gpioSetOutput(M5PM1_GPIO_NUM_0, true);
    // 配置方案2（等效，库内部会转换为方案1）
    pm1.pinMode(M5PM1_GPIO_NUM_0, M5PM1_OTHER);

    // 配置LED输出：使能输出 + 设置LED数量
    m5pm1_err_t err1 = pm1.setLedEnLevel(true);
    if (err1 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to enable LED output: %d\r\n", err1);
    } else {
        Serial.printf("[PM1][I] LED output enabled\r\n");
    }
    m5pm1_err_t err2 = pm1.setLedCount(LED_COUNT);
    if (err2 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to set LED count: %d\r\n", err2);
    } else {
        Serial.printf("[PM1][I] LED count set to %u\r\n", LED_COUNT);
        Serial.printf("[PM1][I] Fixed LED brightness set to %u/255\r\n", BRIGHTNESS);
    }
}

void loop()
{
    static uint8_t colorIndex = 0;

    m5pm1_rgb_t color = COLOR_RED;
    if (colorIndex == 1) {
        color = COLOR_GREEN;
    } else if (colorIndex == 2) {
        color = COLOR_BLUE;
    }

    m5pm1_err_t err3 = pm1.setLedColor(0, color);
    if (err3 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to set LED color: %d\r\n", err3);
    }

    pm1.refreshLeds();
    colorIndex = static_cast<uint8_t>((colorIndex + 1) % 3);
    delay(500);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_rgb_example_01.gif" width="50%" />
