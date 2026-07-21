# Tab5 Wakeup 休眠唤醒

Tab5 休眠唤醒相关 API 与案例程序。

## 案例程序

### 秒级定时唤醒

#> 说明 | 秒级唤醒使用的是 ESP32 内部 RTC 定时器，唤醒时间精度为秒级，唤醒后会重新启动程序。

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    if(M5.Rtc.isEnabled()){
        M5.Display.drawString("OK", M5.Display.width() / 2,
                              M5.Display.height() / 2 - 60);
        delay(2000);
    }

    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::FreeMonoBold18pt7b);
    M5.Display.setRotation(1);

    M5.Display.clear();

    M5.Display.drawString("Touch to sleep", M5.Display.width() / 2, M5.Display.height() / 2 - 20);
    M5.Display.drawString("After 5s wakeup", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
}

void loop(void) {
    M5.update();

    if (M5.Touch.getDetail(0).wasClicked()) {
        M5.Power.deepSleep(5000000ULL, false);
    }
}
```

成功运行后，触摸屏幕，Tab5 将进入休眠状态，并在约 5 秒后唤醒。屏幕显示如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Tab5_Arduino_wakeup_01.jpg" width="50%">

### 指定时间唤醒

#> 说明 | 指定时间唤醒使用的是 RX8130 RTC 定时器，唤醒时间精度为分钟级，唤醒后会重新启动程序。

```cpp line-num
#include <M5Unified.h>

m5::rtc_time_t wakeTime = {};

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);

    if (M5.Rtc.isEnabled()) {
        // Set an initial RTC time for testing.
        // Format: {{year, month, date, weekDay}, {hour, minute, second}}
        m5::rtc_datetime_t initialDateTime = {{2026, 1, 1, 4}, {12, 0, 0}};
        M5.Rtc.setDateTime(&initialDateTime.date, &initialDateTime.time);
    }

    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::FreeMonoBold18pt7b);
    M5.Display.setRotation(1);

    M5.Display.clear();

    M5.Display.drawString("Touch to sleep", M5.Display.width() / 2, M5.Display.height() / 2 - 20);
    M5.Display.drawString("After about 1min wakeup", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
}

void loop(void) {
    M5.update();

    if (M5.Touch.getDetail(0).wasClicked()) {
        m5::rtc_time_t now;

        if (M5.Rtc.getTime(&now)) {
            int wakeHour = now.hours;
            int wakeMinute = now.minutes + 1;

            if (wakeMinute >= 60) {
                wakeMinute -= 60;
                wakeHour += 1;
                if (wakeHour >= 24) {
                    wakeHour = 0;
                }
            }

            wakeTime.hours = wakeHour;
            wakeTime.minutes = wakeMinute;
            wakeTime.seconds = -1;  // RX8130 alarm ignores seconds in this library.

            M5.Power.timerSleep(wakeTime);
        } else {
            M5.Display.clear();
            M5.Display.drawString("RTC Error", M5.Display.width() / 2, M5.Display.height() / 2);
        }
    }
    delay(10);
}
```

成功运行后，触摸屏幕，Tab5 将进入休眠状态，并在约 1 分钟后唤醒。屏幕显示如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Tab5_Arduino_wakeup_02.jpg" width="50%">

## API

Tab5 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

