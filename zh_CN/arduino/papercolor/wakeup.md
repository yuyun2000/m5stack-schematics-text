# PaperColor Wakeup 休眠唤醒

PaperColor 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21
- M5PM1 库版本 >= 1.0.1

### RTC 唤醒 ESP32-S3

使用 RTC 中断信号唤醒 ESP32-S3，此过程中 M5PM1 电源管理芯片保持待机状态。

```cpp line-num
#include <M5Unified.h>

M5Canvas canvas(&M5.Display);

static void drawEpdSleepScreen()
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(middle_center);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(RED);
    canvas.drawString("Press Top BtnA", w / 2, h / 2 - 20);

    canvas.setTextColor(GREEN);
    canvas.drawString("Sleep 5s, then wakeup", w / 2, h / 2 + 20);

    canvas.pushSprite(0, 0);
}

void setup(void)
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);

    M5.Display.setEpdMode(epd_mode_t::epd_quality);

    canvas.createSprite(M5.Display.width(), M5.Display.height());
    drawEpdSleepScreen();
}

void loop(void)
{
    M5.update();

    if (M5.BtnA.wasPressed()) {
        M5.Power.timerSleep(5);
    }

    delay(10);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_rtc_esp32s3_sleep_demo_01.jpg" width="50%">

该案例中 PaperColor 休眠唤醒部分使用 `M5Unified` 库中的 `Power_Class`，更多相关 API 可参考：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

### M5PM1 Timer 定时器唤醒

设备开机后，单击按键 A 配置 10 秒定时器触发开机事件，随后设备操作关机，等待唤醒。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>

static constexpr uint32_t POWERON_SECONDS = 10;
static constexpr uint32_t POWEROFF_SECONDS = 10;

M5PM1 pm1;
M5Canvas canvas(&M5.Display);

static bool pm1_ready = false;

static void drawScreen(const char* status)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(top_left);
    canvas.setTextColor(BLACK);

    canvas.setFont(&fonts::FreeSansBold12pt7b);
    canvas.drawString("M5PM1 TIMER", 16, 24);

    canvas.setFont(&fonts::FreeSansBold9pt7b);
    canvas.setTextColor(BLUE);
    canvas.drawString("BtnA: power on after 10s", 16, 86);

    canvas.setTextColor(pm1_ready ? GREEN : RED);
    canvas.drawString(status, 16, h - 40);

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

    if (pm1_ready) {
        Serial.println("PM1 init ok");
        drawScreen("PM1 ready");
    } else {
        Serial.printf("PM1 init failed: %d\n", (int)err);
        drawScreen("PM1 init failed");
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
        m5pm1_err_t err = pm1.timerSet(POWERON_SECONDS, M5PM1_TIM_ACTION_POWERON);
        if (err != M5PM1_OK) {
            Serial.printf("timerSet POWERON failed: %d\n", (int)err);
            drawScreen("BtnA failed");
        }
        delay(1000);
        pm1.shutdown();
    }
    delay(20);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_timer_wakeup_pm1_demo_01.jpg" width="70%">

更多相关 PaperColor - M5PM1 说明可参考：

- [PaperColor M5PM1 电源管理](/zh_CN/arduino/papercolor/m5pm1)
