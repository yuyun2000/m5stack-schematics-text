# Stamp-S3Bat Wakeup 休眠唤醒

Stamp-S3Bat 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5StampS3Bat
- M5PM1 库版本 >= 1.0.7

### M5PM1 Timer 定时器唤醒

Stamp‑S3Bat 启动后可配置 M5PM1 定时器，关机后实现定时唤醒功能。

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

static const uint8_t PIN_SDA = 48;
static const uint8_t PIN_SCL = 47;

static const uint8_t LED_COUNT      = 1;
static const uint8_t LED_BRIGHTNESS = 64;
static const uint32_t WAKEUP_SEC    = 10;
static const uint32_t GREEN_HOLD_MS = 2000;

static const m5pm1_rgb_t COLOR_RED   = {LED_BRIGHTNESS, 0, 0};
static const m5pm1_rgb_t COLOR_GREEN = {0, LED_BRIGHTNESS, 0};
static const m5pm1_rgb_t COLOR_OFF   = {0, 0, 0};

static bool setSingleLedColor(m5pm1_rgb_t color)
{
    if (pm1.setLedColor(0, color) != M5PM1_OK) {
        return false;
    }
    return pm1.refreshLeds() == M5PM1_OK;
}

void setup()
{
    Serial.begin(115200);
    delay(300);

    Wire.end();
    Wire.begin(PIN_SDA, PIN_SCL, 100000U);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, PIN_SDA, PIN_SCL, M5PM1_I2C_FREQ_100K);

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
    m5pm1_err_t err2 = pm1.setLedCount(LED_COUNT);
    if (err1 != M5PM1_OK || err2 != M5PM1_OK) {
        Serial.printf("[PM1][E] LED init failed, en:%d count:%d\r\n", err1, err2);
    }

    if (!setSingleLedColor(COLOR_GREEN)) {
        Serial.printf("[PM1][E] Failed to set boot GREEN LED\r\n");
    }
    delay(GREEN_HOLD_MS);

    if (!setSingleLedColor(COLOR_RED)) {
        Serial.printf("[PM1][E] Failed to set pre-sleep RED LED\r\n");
    }
    delay(200);
    setSingleLedColor(COLOR_OFF);
    delay(120);

    m5pm1_err_t err_timer = pm1.timerSet(WAKEUP_SEC, M5PM1_TIM_ACTION_POWERON);
    if (err_timer != M5PM1_OK) {
        Serial.printf("[PM1][E] timerSet failed: %d\r\n", err_timer);
        while (true) {
            delay(1000);
        }
    }
    Serial.printf("[PM1][I] Shutdown now, wake up in %lu s\r\n", static_cast<unsigned long>(WAKEUP_SEC));

    m5pm1_err_t err_shutdown = pm1.shutdown();
    if (err_shutdown != M5PM1_OK) {
        Serial.printf("[PM1][E] shutdown failed: %d\r\n", err_shutdown);
    }
}

void loop()
{
    delay(1000);
}
```

### M5PM1 IO 唤醒

Stamp‑S3Bat 启动后会将 M5PM1 的 G4（WAKE）配置为唤醒 IO，关机后，拉低 WAKE 引脚产生下降沿，即可唤醒设备。

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

static const uint8_t PIN_SDA = 48;
static const uint8_t PIN_SCL = 47;

static const uint8_t LED_COUNT      = 1;
static const uint8_t LED_BRIGHTNESS = 64;
static const uint32_t GREEN_HOLD_MS = 2000;

static const m5pm1_rgb_t COLOR_RED   = {LED_BRIGHTNESS, 0, 0};
static const m5pm1_rgb_t COLOR_GREEN = {0, LED_BRIGHTNESS, 0};
static const m5pm1_rgb_t COLOR_OFF   = {0, 0, 0};

static bool setSingleLedColor(m5pm1_rgb_t color)
{
    if (pm1.setLedColor(0, color) != M5PM1_OK) {
        return false;
    }
    return pm1.refreshLeds() == M5PM1_OK;
}

void setup()
{
    Serial.begin(115200);
    delay(300);

    Wire.end();
    Wire.begin(PIN_SDA, PIN_SCL, 100000U);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, PIN_SDA, PIN_SCL, M5PM1_I2C_FREQ_100K);

    if (err != M5PM1_OK) {
        Serial.printf("[PM1][E] PM1 initialization failed: %d\r\n", err);
        while (true) {
            delay(1000);
        }
    }
    Serial.printf("[PM1][I] PM1 initialization successful\r\n");

    pm1.irqClearGpioAll();
    pm1.irqClearSysAll();
    pm1.irqClearBtnAll();

    pm1.irqSetGpioMaskAll(M5PM1_IRQ_MASK_ENABLE);
    pm1.irqSetSysMaskAll(M5PM1_IRQ_MASK_ENABLE);
    pm1.irqSetBtnMaskAll(M5PM1_IRQ_MASK_ENABLE);

    pm1.irqSetGpioMask(M5PM1_IRQ_GPIO4, M5PM1_IRQ_MASK_DISABLE);
    pm1.gpioSetMode(M5PM1_GPIO_NUM_4, M5PM1_GPIO_MODE_INPUT);
    pm1.gpioSetPull(M5PM1_GPIO_NUM_4, M5PM1_GPIO_PULL_UP);

    pm1.gpioSetFunc(M5PM1_GPIO_NUM_0, M5PM1_GPIO_FUNC_OTHER);
    pm1.gpioSetDrive(M5PM1_GPIO_NUM_0, M5PM1_GPIO_DRIVE_PUSHPULL);
    pm1.gpioSetOutput(M5PM1_GPIO_NUM_0, true);
    pm1.pinMode(M5PM1_GPIO_NUM_0, M5PM1_OTHER);

    m5pm1_err_t err1 = pm1.setLedEnLevel(true);
    m5pm1_err_t err2 = pm1.setLedCount(LED_COUNT);
    if (err1 != M5PM1_OK || err2 != M5PM1_OK) {
        Serial.printf("[PM1][E] LED init failed, en:%d count:%d\r\n", err1, err2);
    }

    if (!setSingleLedColor(COLOR_GREEN)) {
        Serial.printf("[PM1][E] Failed to set boot GREEN LED\r\n");
    }
    delay(GREEN_HOLD_MS);

    // Configure G4 as IO wake source: low-level trigger (falling edge)
    m5pm1_err_t err_wake_en = pm1.gpioSetWakeEnable(M5PM1_GPIO_NUM_4, true);
    m5pm1_err_t err_wake_ed = pm1.gpioSetWakeEdge(M5PM1_GPIO_NUM_4, M5PM1_GPIO_WAKE_FALLING);
    if (err_wake_en != M5PM1_OK || err_wake_ed != M5PM1_OK) {
        Serial.printf("[PM1][E] GPIO wake config failed, en:%d edge:%d\r\n", err_wake_en, err_wake_ed);
        while (true) {
            delay(1000);
        }
    }

    // Blink red LED, then enter sleep and wait for wakeup
    for (int i = 0; i < 4; ++i) {
        if (!setSingleLedColor(COLOR_RED)) {
            Serial.printf("[PM1][E] Failed to blink RED LED\r\n");
            break;
        }
        delay(150);
        setSingleLedColor(COLOR_OFF);
        delay(150);
    }

    Serial.printf("[PM1][I] Shutdown now, wait GPIO4 low level to wake\r\n");

    m5pm1_err_t err_shutdown = pm1.shutdown();
    if (err_shutdown != M5PM1_OK) {
        Serial.printf("[PM1][E] shutdown failed: %d\r\n", err_shutdown);
    }
}

void loop()
{
    delay(1000);
}
```
