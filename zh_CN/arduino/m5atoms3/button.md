# AtomS3 Button 按键

M5AtomS3按键输入相关API与案例程序。

#>注意事项: | 使用时需要在主循环中包含`AtomS3.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

```cpp line-num
#include "M5AtomS3.h"

void setup() {
    AtomS3.begin();
}

void loop() {
    AtomS3.update();
    if (AtomS3.BtnA.wasPressed()) {

        Serial.println("Pressed");
    }
    if (AtomS3.BtnA.wasReleased()) {

        Serial.println("Released");
    }
}
```

## API

M5AtomS3库基于M5Unified库实现, 按键部分使用了M5Unified库中的`Button_Class`, 更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

