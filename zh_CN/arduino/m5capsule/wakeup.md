# Capsule Wakeup 休眠唤醒

M5Capsule休眠唤醒相关API与案例程序。

#>注意事项: | 在USB供电状态下, 无法关闭电源进入休眠。需在电池供电条件下该功能才生效。

```cpp line-num
#include <M5Capsule.h>

void setup(void) {
    auto cfg = M5.config();
    M5Capsule.begin(cfg);

    Serial.println("Press Btn to sleep");
    Serial.println("After 5s Wakeup");
}

void loop(void) {
    M5Capsule.update();

    if (M5Capsule.BtnA.wasPressed()) {
        M5Capsule.Power.timerSleep(5);
        // M5Capsule.Power.timerSleep(const rtc_time_t& time);
        // M5Capsule.Power.timerSleep(const rtc_date_t& date, const rtc_time_t&
        // time);
        // M5Capsule.Power.powerOff(); shutdown
    }
}
```

## API

M5Capsule库基于M5Unified库实现, 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

