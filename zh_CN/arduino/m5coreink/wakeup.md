# CoreInk Wakeup 休眠唤醒

CoreInk 休眠唤醒相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>

void setup(void)
{
    auto cfg = M5.config();
    M5.begin(cfg);

    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::FreeSerifBold9pt7b);
    M5.Display.setTextSize(1);

    Serial.println("Press BtnPWR to sleep");
    Serial.println("After 5s Wakeup");

    M5.Display.drawString("Press BtnPWR", M5.Display.width() / 2, M5.Display.height() / 2 - 20);
    M5.Display.drawString("to Sleep 5s", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
}

void loop(void)
{
    M5.update();

    if (M5.BtnPWR.wasPressed()) {
        M5.Display.clear();
        M5.Display.drawString("Sleep 5s", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
        M5.Power.timerSleep(5);
        // M5.Power.timerSleep(const rtc_time_t& time);
        // M5.Power.timerSleep(const rtc_date_t& date, const rtc_time_t&
        // time);
        // M5.Power.powerOff(); shutdown
    }
}
```


## API

CoreInk 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

