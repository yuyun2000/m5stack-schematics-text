# PaperColor M5PM1 电源管理

## 1. 多级电源开关设计

PaperColor 内部集成 M5PM1，结合硬件电路实现了多级电源开关，不同的级别的电源开关对应控制了相关的外设与接口供电。用户可根据运行需求，切换不同级别的电源使能，关闭未使用的外设部分，实现整机低功耗。

### M5PM1 驱动库

使用 M5PM1 驱动库能够非常便捷地配置 M5PM1 的引脚功能，用于低功耗唤醒以及外设供电开关。

- [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/papercolor_m5pm1_level_01.png" width="70%" />

#> 注意事项 | PaperColor 的多级电源开关设计并非串联结构。L1 ~ L3B 开关的电源输入均来自于 L0 (SYS_VBUS) 级源头，而非上一级电源，因此支持独立控制不同级别的电源开关，以上分级根据外设供电与功耗进行区分。M5PM1 启动上电后 L1, L2, L3A 将自动开启 (默认打开 `DCDC3V3_EN_PP`, `LDO3V3_EN_PP`, `CHG_EN_PP`)。

### L0 / L1

此级电源条件下，电池保持对 M5PM1 以及 RTC 的供电。电池电量未耗尽的情况下，该层电源将一直保持，M5PM1 支持基础的按键开关机操作。

L0 层级表示 M5PM1 进入关机状态。

L1 层级时，M5PM1 处于待机状态。

### L2 / L3A

此级电源条件下，将启用 ESP32-S3 主控, SHT40I 温湿度传感器, 以及用户按键上拉的电阻的供电 (3V3_L2)。

当 ESP32-S3 处于休眠状态时，电源处于 L2 级。
当 ESP32-S3 处于工作状态时，电源处于 L3A 级。

ESP32-S3 可通过控制 M5PM1 进入休眠的方式，关断自身的供电 (L2->L1/L0)。

### L3B

该电源层级可通过 M5PM1 和 ESP32-S3 GPIO 进一步控制板载外设的供电。

| ESP32S3R8                             | G45          |
| ------------------------------------- | ------------ |
| ES8311 & ES7210 Power (CODEC_3V3_L3B) | AUDIO_PWR_EN |

| ESP32S3R8 | G46    |
| --------- | ------ |
| AW8737A   | SPK_EN |

- G46(SPK_EN): 扬声器功放使能
- G45(AUDIO_PWR_EN): 音频编解码芯片与麦克风供电

| M5PM1   | DCDC3V3_EN_PP | LDO3V3_EN_PP  | BOOST5V_EN_PP   |
| ------- | ------------- | ------------- | --------------- |
| 3V3_L2  | PY_MPWR_EN    |               |                 |
| RGB LED |               | PY_RGB_PWR_EN |                 |
| Grove   |               |               | PY_GROVE_OUT_EN |

- DCDC3V3_EN_PP(PY_MPWR_EN): 3V3_L2 层电源开关
- LDO3V3_EN_PP(PY_RGB_PWR_EN): RGB LED 供电开关
- BOOST5V_EN_PP(PY_GROVE_OUT_EN): Grove 拓展接口供电方向控制

| M5PM1   | PYG0      | PYG2    | PYG4         | PYG3         | PYG1     |
| ------- | --------- | ------- | ------------ | ------------ | -------- |
| E-Paper | PY_EPD_EN |         |              |              |          |
| RTC     |           | RTC_IRQ |              |              |          |
| microSD |           |         | PY_SD_DET_EN | PY_SD_PWR_EN | CARD_DEC |

- PYG0(PY_EPD_EN): 开启墨水屏供电
- PYG2(RTC_IRQ): RTC 中断信号
- PYG3(PY_SD_PWR_EN): microSD 模块供电
- PYG4(PY_SD_DET_EN): microSD 检测功能启用，使能上拉
- PYG1(CARD_DEC): microSD 插入检测

## 2. M5PM1 休眠

### 手动休眠

M5PM1 可通过程序手动控制进入休眠状态，来降低整机功耗。默认状态下，直接设置休眠将回退至 L0 级电源，此时仅 M5PM1 与 RTC 保持供电。

```cpp
pm1.shutdown();
```

在一些特殊的使用场景 (例如 ESP32-S3 SoC 休眠模式)，允许 M5PM1 进入休眠降低的同时，保持一些层级的外设供电，用于唤醒源或是状态保持。

该类应用需要在 M5PM1 进入休眠模式前，配置对应层级的电源开关引脚状态，并激活状态保持。

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

案例说明: 设备开机后，单击按键 A 配置 10 秒定时器触发开机事件，随后设备操作关机，等待唤醒。单击按键 B：配置 10 秒定时器触发 M5PM1 关机（可通过单击电源键重新开机）。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>
#include <Adafruit_NeoPixel.h>

static constexpr uint32_t POWERON_SECONDS = 10;
static constexpr uint32_t POWEROFF_SECONDS = 10;
static constexpr uint8_t LED_PIN = 21;
static constexpr uint8_t LED_COUNT = 2;

M5PM1 pm1;
M5Canvas canvas(&M5.Display);
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

static bool pm1_ready = false;

static void setAllLeds(uint32_t color)
{
    for (uint8_t i = 0; i < LED_COUNT; ++i) {
        pixels.setPixelColor(i, color);
    }
    pixels.show();
}

static void drawScreen(const char* status)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(top_center);
    canvas.setTextColor(BLACK);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.drawString("M5PM1 TIMER", w / 2, 34);

    canvas.setFont(&fonts::FreeSansBold12pt7b);
    canvas.setTextColor(BLUE);
    canvas.drawString("BtnA: Power ON in 10s", w / 2, 180);
    canvas.drawString("BtnB: Power OFF in 10s", w / 2, 248);

    canvas.setTextColor(pm1_ready ? GREEN : RED);
    canvas.drawString(status, w / 2, h - 110);

    canvas.pushSprite(0, 0);
}

void setup(void)
{
    auto cfg = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);

    Serial.begin(115200);
    M5.Display.setEpdMode(epd_mode_t::epd_quality);

    canvas.createSprite(M5.Display.width(), M5.Display.height());

    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);
    pm1_ready       = (err == M5PM1_OK);

    if (pm1_ready) {
        pm1.setLdoEnable(true);
    }

    pixels.begin();
    pixels.setBrightness(60);
    setAllLeds(0);

    if (pm1_ready) {
        Serial.println("PM1 init ok");
        drawScreen("PM1 ready");
        setAllLeds(pixels.Color(0, 255, 0));
    } else {
        Serial.printf("PM1 init failed: %d\n", (int)err);
        drawScreen("PM1 init failed");
        setAllLeds(pixels.Color(255, 0, 0));
    }
}

void loop(void)
{
    M5.update();

    if (!pm1_ready) {
        delay(20);
        return;
    }

    if (M5.BtnA.wasPressed()) {
        Serial.printf("BtnA: timer power on in %lu s\n", POWERON_SECONDS);
        setAllLeds(pixels.Color(255, 255, 0));
        m5pm1_err_t err = pm1.timerSet(POWERON_SECONDS, M5PM1_TIM_ACTION_POWERON);
        if (err != M5PM1_OK) {
            Serial.printf("timerSet POWERON failed: %d\n", (int)err);
            drawScreen("BtnA failed");
            setAllLeds(pixels.Color(255, 0, 0));
        }
        delay(1000);
        pm1.shutdown();
    }

    if (M5.BtnB.wasPressed()) {
        Serial.printf("BtnB: timer poweroff in %lu s\n", POWEROFF_SECONDS);
        setAllLeds(pixels.Color(0, 0, 255));
        m5pm1_err_t err = pm1.timerSet(POWEROFF_SECONDS, M5PM1_TIM_ACTION_POWEROFF);
        if (err != M5PM1_OK) {
            Serial.printf("timerSet POWEROFF failed: %d\n", (int)err);
            drawScreen("BtnB failed");
            setAllLeds(pixels.Color(255, 0, 0));
        }
    }

    delay(20);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_timer_onoff_pm1_demo_01.jpg" width="50%">

## 4. RTC M5PM1 唤醒

设备开机后，单击按键 A 配置 RTC 定时唤醒并配置 M5PM1 进入休眠，此时仅维持系统最低 L0 级别供电，用于维持 IMU 和 M5PM1 工作, 待 RTC 触发唤醒信号唤醒 M5PM1 重新启动。M5PM1 唤醒后将重新运行 L1, L2, L3A 上电流程，ESP32-S3 重新执行初始化。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>
#include <Adafruit_NeoPixel.h>

static constexpr int RTC_WAKE_AFTER_SECONDS = 20;

M5Canvas canvas(&M5.Display);
M5PM1 pm1;
Adafruit_NeoPixel pixels(2, 21, NEO_GRB + NEO_KHZ800);

static bool pm1_ready = false;

static void setAllLeds(uint32_t color)
{
    pixels.setPixelColor(0, color);
    pixels.setPixelColor(1, color);
    pixels.show();
}

static void drawScreen(const char* status, uint32_t status_color)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(top_center);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextColor(BLACK);
    canvas.drawString("RTC Wake PM1", w / 2, 40);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(RED);
    canvas.drawString("BtnA: Shutdown", w / 2, 160);

    canvas.setTextColor(BLUE);
    canvas.drawString("RTC Alarm", w / 2, 270);
    canvas.drawString("wakes PM1 after 10s", w / 2, 316);

    canvas.setTextColor(status_color);
    canvas.drawString(status, w / 2, 430);

    canvas.pushSprite(0, 0);
}

void setup(void)
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    Serial.begin(115200);

    M5.Display.setEpdMode(epd_mode_t::epd_quality);
    canvas.createSprite(M5.Display.width(), M5.Display.height());

    pixels.begin();
    pixels.setBrightness(80);
    setAllLeds(0);

    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);
    pm1_ready       = (err == M5PM1_OK);

    if (pm1_ready) {
        pm1.setLdoEnable(true);
        setAllLeds(pixels.Color(0, 255, 0));
        drawScreen("PM1 ready", GREEN);
        Serial.println("PM1 initialization successful");
        pm1.gpioSetWakeEnable(M5PM1_GPIO_NUM_2, true);
        pm1.gpioSetWakeEdge(M5PM1_GPIO_NUM_2, M5PM1_GPIO_WAKE_FALLING);  // Falling edge

    } else {
        setAllLeds(pixels.Color(255, 0, 0));
        drawScreen("PM1 init failed", RED);
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
}

void loop(void)
{
    M5.update();

    if (!pm1_ready) {
        delay(20);
        return;
    }

    if (M5.BtnA.wasPressed()) {
        M5.Rtc.disableIRQ();
        M5.Rtc.clearIRQ();
        M5.Rtc.setAlarmIRQ(RTC_WAKE_AFTER_SECONDS);

        for (int i = 0; i < 3; i++) {
            setAllLeds(pixels.Color(255, 0, 0));
            delay(200);
            setAllLeds(0);
            delay(200);
        }
        pm1.shutdown();
    }

    delay(20);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_rtc_wakeup_pm1_demo_01.jpg" width="50%" />
