# StickC-Plus2 Buzzer 蜂鸣器

M5StickCPlus2 Buzzer蜂鸣器相关API与案例程序。

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
    StickCP2.Display.drawString("Buzzer Test", StickCP2.Display.width() / 2,
                                StickCP2.Display.height() / 2);
}

void loop() {
    StickCP2.Speaker.tone(10000, 100);
    delay(1000);
    StickCP2.Speaker.tone(4000, 20);
    delay(1000);
}
```

## API

M5StickCPlus2库基于M5Unified库实现, Buzzer部分驱动使用了M5Unified库中的`Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

