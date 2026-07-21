# StickC-Plus2 Wakeup 休眠唤醒

M5StickC Plus2休眠唤醒相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5StickCPlus2.h>

void setup(void) {
    auto cfg = M5.config();
    StickCP2.begin(cfg);

    StickCP2.Display.setRotation(1);
    StickCP2.Display.setTextColor(GREEN);
    StickCP2.Display.setTextDatum(middle_center);
    StickCP2.Display.setTextFont(&fonts::Orbitron_Light_24);
    StickCP2.Display.setTextSize(1);

    Serial.println("Press Btn to sleep");
    Serial.println("After 5s Wakeup");

    StickCP2.Display.drawString("BtnA Sleep 5s", StickCP2.Display.width() / 2,
                                StickCP2.Display.height() / 2);
}

void loop(void) {
    StickCP2.update();

    if (StickCP2.BtnA.wasPressed()) {
        StickCP2.Power.timerSleep(5);
        // StickCP2.Power.timerSleep(const rtc_time_t& time);
        // StickCP2.Power.timerSleep(const rtc_date_t& date, const rtc_time_t&
        // time);
        // StickCP2.Power.powerOff(); shutdown
    }
}
```


## API

M5StickCPlus2库基于M5Unified库实现, 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

