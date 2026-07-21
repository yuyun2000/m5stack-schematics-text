# StickC-Plus2 Button 按键

StickC-Plus2 按键输入相关API与案例程序。

#>注意事项: | 使用时需要在主循环中包含`StickCP2.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序


```cpp line-num
#include "M5StickCPlus2.h"

void setup() {
    auto cfg = M5.config();
    StickCP2.begin(cfg);
}

void loop() {
    StickCP2.update();
    if (StickCP2.BtnA.wasPressed()) {
        Serial.println("A Btn Pressed");
    }
    if (StickCP2.BtnA.wasReleased()) {

        Serial.println("A Btn Released");
    }
    if (StickCP2.BtnB.wasPressed()) {
        Serial.println("B Btn Pressed");
    }
    if (StickCP2.BtnB.wasReleased()) {
        Serial.println("B Btn Released");
    }
    if (StickCP2.BtnPWR.wasClicked()) {
        Serial.println("PWR Btn Clicked");
    }
    if (StickCP2.BtnPWR.wasHold()) {
        Serial.println("PWR Btn Hold");
    }
}
```

## API

M5StickCPlus2库基于M5Unified库实现, 按键部分使用了M5Unified库中的`Button_Class`, 更多按键相关的API可以参考下方文档:

StickC-Plus2 的实体按键(BtnPWR)状态读取依赖于电源管理芯片， 目前仅`wasClicked"，"wasHold"可正常使用。

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

