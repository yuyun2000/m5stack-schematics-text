# CoreInk Battery 电池

CoreInk 电池状态读取相关API与案例程序。

## 案例程序


```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);
}

void loop()
{
    M5.Display.clear();
    int vol = M5.Power.getBatteryVoltage();
    M5.Display.setCursor(0, 30);
    M5.Display.printf("BAT: %dmv", vol);
    delay(5000);
}
```

## API

CoreInk 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
