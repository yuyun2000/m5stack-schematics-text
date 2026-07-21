# Stamp-S3Bat M5PM1 电源管理

## 1. 多级电源开关设计

Stamp-S3Bat 内部集成 M5PM1，结合硬件电路实现了多级电源开关，不同的级别的电源开关对应控制了相关的外设与接口供电。用户可根据运行需求，切换不同级别的电源使能，关闭未使用的外设部分，实现整机低功耗。

### M5PM1 驱动库

使用 M5PM1 驱动库能够非常便捷地配置 M5PM1 的引脚功能，用于低功耗唤醒以及外设供电开关。

- [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/stamp_s3bat_m5pm1_level_01.png" width="70%" />

\#> 注意事项 | Stamp-S3Bat 的多级电源开关设计并非串联结构。L1 ~ L3B 开关的电源输入均来自于 L1 (SYS_VBUS) 级源头，而非上一级电源，因此支持独立控制不同级别的电源开关，以上分级根据外设供电与功耗进行区分。

M5PM1 启动上电后 L1, L2，L3A 将自动开启 (默认打开 `DCDC3V3_EN_PP`, `CHG_EN_PP`)，此时设备上的 ESP32-S3 上电完成初始化，EXT_5V_OUT 不启用输出，RGB LED 灯供电未开启。

### L1

此级电源条件下，电池保持对 M5PM1 供电。电池电量未耗尽的情况下，该层电源将一直保持，M5PM1 支持基础的按键开关机操作。

### L2 / L3A

此级电源条件下，将启用 ESP32-S3 主控的供电。 当 ESP32-S3 处于休眠状态时，电源处于 L2 级。当 ESP32-S3 处于工作状态时，电源处于 L3A 级。

ESP32-S3 可通过控制 M5PM1 进入休眠的方式，关断自身的供电 (L2->L1/L0)。

### L3B

该电源层级可通过 M5PM1 进一步打开 EXT_5V_OUT 输出接口与 RGB LED 的供电。可通过以下 API 实现开关控制。

- 打开 `EXT_5V_OUT` 输出：通过 PY_G1 (5VOUT_EN) 控制。

```cpp
pm1.gpioSetFunc(M5PM1_GPIO_NUM_1, M5PM1_GPIO_FUNC_GPIO);
pm1.gpioSetMode(M5PM1_GPIO_NUM_1, M5PM1_GPIO_MODE_OUTPUT);
pm1.gpioSetDrive(M5PM1_GPIO_NUM_1, M5PM1_GPIO_DRIVE_PUSHPULL);
pm1.gpioSetOutput(M5PM1_GPIO_NUM_1, true);
```

- 打开 `RGB LED` 供电：通过 PY_LED_EN 控制。

```cpp
pm1.setLedEnLevel(true)
```

## 2. M5PM1 休眠

### 手动休眠

M5PM1 可通过程序手动控制进入休眠状态，来降低整机功耗。默认状态下，直接设置休眠将回退至 L1 级电源，此时仅 M5PM1 保持供电，无其他唤醒源的情况下，需单击 `PWR` 按键进行唤醒。

休眠前可配置外部唤醒 IO 或者其他唤醒源 (如定时器等)，待设备进入休眠状态后，可通过唤醒源触发 M5PM1 唤醒，恢复 ESP32-S3 供电。

```cpp
pm1.shutdown();
```

### IO 唤醒

Stamp‑S3Bat 运行本案例程序启动后会将 M5PM1 的 G4（WAKE）配置为唤醒 IO，关机后，拉低 WAKE 引脚产生下降沿，即可唤醒设备。

```cpp
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

static const uint8_t PIN_SDA = 48;
static const uint8_t PIN_SCL = 47;

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

    // Configure G4 as IO wake source: low-level trigger (falling edge)
    m5pm1_err_t err_wake_en = pm1.gpioSetWakeEnable(M5PM1_GPIO_NUM_4, true);
    m5pm1_err_t err_wake_ed = pm1.gpioSetWakeEdge(M5PM1_GPIO_NUM_4, M5PM1_GPIO_WAKE_FALLING);
    if (err_wake_en != M5PM1_OK || err_wake_ed != M5PM1_OK) {
        Serial.printf("[PM1][E] GPIO wake config failed, en:%d edge:%d\r\n", err_wake_en, err_wake_ed);
        while (true) {
            delay(1000);
        }
    }
    Serial.printf("[PM1][I] Shutdown now, wait GPIO4 low level to wake\r\n");
    delay(1000);
    m5pm1_err_t err_shutdown = pm1.shutdown();
    if (err_shutdown != M5PM1_OK) {
        Serial.printf("[PM1][E] shutdown failed: %d\r\n", err_shutdown);
    }
}

void loop()
{
}
```

### 休眠保持

在一些特殊的使用场景，允许 M5PM1 进入休眠降低的同时，且可维持芯片 GPIO 引脚的当前状态。 实现该功能时，需在 M5PM1 进入休眠前完成对应引脚状态配置，并启用 GPIO 状态保持机制。

- M5PM1 休眠，并保持 `M5PM1_GPIO_NUM_1` (EXT_5V_OUT) 电源输出。

```cpp
pm1.gpioSetMode(M5PM1_GPIO_NUM_1, M5PM1_GPIO_MODE_OUTPUT);
pm1.gpioSetDrive(M5PM1_GPIO_NUM_1, M5PM1_GPIO_DRIVE_PUSHPULL);
pm1.gpioSetOutput(M5PM1_GPIO_NUM_1, true);
pm1.gpioSetPowerHold(M5PM1_GPIO_NUM_1, true);

Serial.println("[DEMO] GPIO1 HIGH + HOLD");
delay(1000);
Serial.println("[DEMO] Shutdown now");
delay(300);
pm1.shutdown();
```

- M5PM1 休眠，并保持 `M5PM1_GPIO_NUM_4` (WAKE) 输出高电平。

```cpp
pm1.gpioSetMode(M5PM1_GPIO_NUM_4, M5PM1_GPIO_MODE_OUTPUT);
pm1.gpioSetDrive(M5PM1_GPIO_NUM_4, M5PM1_GPIO_DRIVE_PUSHPULL);
pm1.gpioSetOutput(M5PM1_GPIO_NUM_4, true);
pm1.gpioSetPowerHold(M5PM1_GPIO_NUM_4, true);

Serial.println("[DEMO] GPIO4 HIGH + HOLD");
delay(1000);
Serial.println("[DEMO] Shutdown now");
delay(300);
pm1.shutdown();
```

### I2C 空闲休眠

M5PM1 支持配置 I2C 空闲通信自动休眠状态，来降低整机功耗。进入休眠状态后，ESP32-S3 与 M5PM1 的首次通信将用于 M5PM1 唤醒，因为将通信失败，有效的通信将与唤醒后的下一次通信。

```cpp
m5pm1_err_t setI2cSleepTime(uint8_t seconds);
```

## 3. M5PM1 Timer 定时器

M5PM1 支持配置定时器功能，当计时结束后，执行相应的操作，如开机，关机，复位等。

```cpp
m5pm1_err_t timerSet(uint32_t seconds, m5pm1_tim_action_t action);
```

```cpp
typedef enum {
    M5PM1_TIM_ACTION_STOP = 0b000,     // 停止，无动作
                                       // Stop, no action
    M5PM1_TIM_ACTION_FLAG = 0b001,     // 仅设置标志
                                       // Set flag only
    M5PM1_TIM_ACTION_REBOOT = 0b010,   // 系统复位
                                       // System reboot
    M5PM1_TIM_ACTION_POWERON = 0b011,  // 开机
                                       // Power on
    M5PM1_TIM_ACTION_POWEROFF = 0b100  // 关机
                                       // Power off
} m5pm1_tim_action_t;
```

### 定时开机 / 关机案例

设备上电运行这段程序后，会在 10 秒后自动关机。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    auto sda = M5.getPin(m5::pin_name_t::in_i2c_sda);
    auto scl = M5.getPin(m5::pin_name_t::in_i2c_scl);

    Wire.end();
    Wire.begin(sda, scl, 100000U);

    if (pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, sda, scl, M5PM1_I2C_FREQ_100K) != M5PM1_OK) {
        Serial.println("PM1 init failed");
        return;
    }

    Serial.println("Set timer: power off after 10s");
    pm1.timerSet(10, M5PM1_TIM_ACTION_POWEROFF);
}

void loop(void) {

}
```

设备执行这段程序后会立刻关机，10 秒后自动重新开机。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

void setup(void)
{
    M5.begin();
    Serial.begin(115200);

    auto sda = M5.getPin(m5::pin_name_t::in_i2c_sda);
    auto scl = M5.getPin(m5::pin_name_t::in_i2c_scl);

    Wire.end();
    Wire.begin(sda, scl, 100000U);

    if (pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, sda, scl, M5PM1_I2C_FREQ_100K) != M5PM1_OK) {
        Serial.println("PM1 init failed");
        return;
    }

    Serial.println("Set timer: power on after 10s");
    pm1.timerSet(10, M5PM1_TIM_ACTION_POWERON);
    pm1.shutdown();  // Must enter shutdown first, then PM1 can wake it up by timer.
}

void loop(void) {

}
```

## 4. RGB LED 控制

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

#define PIN_SCL 47
#define PIN_SDA 48

static const uint8_t LED_COUNT  = 1;
static const uint8_t BRIGHTNESS = 64;

static const m5pm1_rgb_t COLOR_GREEN = {0, BRIGHTNESS, 0};

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

    // Configure PM1 GPIO0 for LED output path.
    pm1.gpioSetFunc(M5PM1_GPIO_NUM_0, M5PM1_GPIO_FUNC_OTHER);
    pm1.gpioSetDrive(M5PM1_GPIO_NUM_0, M5PM1_GPIO_DRIVE_PUSHPULL);
    pm1.gpioSetOutput(M5PM1_GPIO_NUM_0, true);
    pm1.pinMode(M5PM1_GPIO_NUM_0, M5PM1_OTHER);

    // Enable LED output and set LED count.
    m5pm1_err_t err1 = pm1.setLedEnLevel(true);
    if (err1 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to enable LED output: %d\r\n", err1);
    }

    m5pm1_err_t err2 = pm1.setLedCount(LED_COUNT);
    if (err2 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to set LED count: %d\r\n", err2);
    }

    // Keep LED solid green.
    m5pm1_err_t err3 = pm1.setLedColor(0, COLOR_GREEN);
    m5pm1_err_t err4 = pm1.refreshLeds();
    if (err3 != M5PM1_OK || err4 != M5PM1_OK) {
        Serial.printf("[PM1][E] Failed to set GREEN LED, color:%d refresh:%d\r\n", err3, err4);
    }
}

void loop()
{
    delay(1000);
}
```

## 5. 充电控制

通过 `PY_G3_CHG_PROG` 切换充电 IC 对电池的充电电流 (低电平: 650mA / 浮空: 200mA)

将宏定义 CHARGE_CURRENT_650MA_ENABLED 置 1，即可启用 650mA 大电流充电模式。

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

#define PIN_SCL 47
#define PIN_SDA 48
#define CHARGE_CURRENT_650MA_ENABLED 1
static const uint8_t LED_COUNT = 1;
static const uint8_t LED_BRIGHTNESS = 64;

static const m5pm1_gpio_num_t PY_G3_CHG_PROG = M5PM1_GPIO_NUM_3;

#if CHARGE_CURRENT_650MA_ENABLED
static const m5pm1_rgb_t LED_COLOR = {0, LED_BRIGHTNESS, 0};
#else
static const m5pm1_rgb_t LED_COLOR = {0, 0, LED_BRIGHTNESS};
#endif

static bool applyChargeCurrentConfig()
{
#if CHARGE_CURRENT_650MA_ENABLED
    return pm1.gpioSetMode(PY_G3_CHG_PROG, M5PM1_GPIO_MODE_OUTPUT) == M5PM1_OK &&
           pm1.gpioSetPull(PY_G3_CHG_PROG, M5PM1_GPIO_PULL_NONE) == M5PM1_OK &&
           pm1.gpioSetOutput(PY_G3_CHG_PROG, false) == M5PM1_OK;
#else
    return pm1.gpioSetMode(PY_G3_CHG_PROG, M5PM1_GPIO_MODE_INPUT) == M5PM1_OK &&
           pm1.gpioSetPull(PY_G3_CHG_PROG, M5PM1_GPIO_PULL_NONE) == M5PM1_OK;
#endif
}

static bool applyRgbLedConfig()
{
    bool ok = pm1.gpioSetFunc(M5PM1_GPIO_NUM_0, M5PM1_GPIO_FUNC_OTHER) == M5PM1_OK &&
              pm1.gpioSetDrive(M5PM1_GPIO_NUM_0, M5PM1_GPIO_DRIVE_PUSHPULL) == M5PM1_OK &&
              pm1.gpioSetOutput(M5PM1_GPIO_NUM_0, true) == M5PM1_OK;
    pm1.pinMode(M5PM1_GPIO_NUM_0, M5PM1_OTHER);
    return ok && pm1.setLedEnLevel(true) == M5PM1_OK && pm1.setLedCount(LED_COUNT) == M5PM1_OK &&
           pm1.setLedColor(0, LED_COLOR) == M5PM1_OK && pm1.refreshLeds() == M5PM1_OK;
}

void setup()
{
    delay(200);

    Wire.end();
    Wire.begin(PIN_SDA, PIN_SCL, 100000U);

    m5pm1_err_t err = pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, PIN_SDA, PIN_SCL, M5PM1_I2C_FREQ_400K);

    pm1.setChargeEnable(true);

    if (err != M5PM1_OK) {
        while (true) {
            delay(1000);
        }
    }

    if (!applyChargeCurrentConfig()) {
        while (true) {
            delay(1000);
        }
    }

    if (!applyRgbLedConfig()) {
        while (true) {
            delay(1000);
        }
    }
}

void loop()
{
    delay(1000);
}
```

## 6. 电源状态

读取 Stamp-S3Bat 当前电源状态。

```cpp line-num
#include <Arduino.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

static const uint8_t PIN_SCL            = 47;
static const uint8_t PIN_SDA            = 48;
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
