# StickC-Plus2 Battery 电池状态

M5StickC Plus2电池状态读取相关API与案例程序。

## 案例程序


```cpp line-num
#include "M5StickCPlus2.h"

void setup() {
    auto cfg = M5.config();
    StickCP2.begin(cfg);
    StickCP2.Display.setRotation(1);
    StickCP2.Display.setTextColor(GREEN);
    StickCP2.Display.setTextDatum(middle_center);
    StickCP2.Display.setTextFont(&fonts::Orbitron_Light_24);
    StickCP2.Display.setTextSize(1);
}

void loop() {
    StickCP2.Display.clear();
    int vol = StickCP2.Power.getBatteryVoltage();
    StickCP2.Display.setCursor(10, 30);
    StickCP2.Display.printf("BAT: %dmv", vol);
    delay(1000);
}
```

## API

M5StickCPlus2库基于M5Unified库实现, 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
