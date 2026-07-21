# CoreInk LED 状态灯

CoreInk 状态灯相关API与案例程序。


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
    M5.Display.drawString("LED Test", M5.Display.width() / 2, M5.Display.height() / 2);
}

void loop()
{
    // inside green led control
    M5.Power.setLed(255);
    delay(1000);
    M5.Power.setLed(0);
    delay(1000);
}
```

## API

CoreInk 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

