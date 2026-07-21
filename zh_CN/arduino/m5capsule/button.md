# Capsule Button 按键

M5Capsule按键输入相关API与案例程序。

#>注意事项: | 使用时需要在主循环中包含`M5Capsule.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

```cpp line-num
#include "M5Capsule.h"

void setup() {
    auto cfg = M5.config();
    M5Capsule.begin(cfg);
}

void loop() {
    M5Capsule.update();
    if (M5Capsule.BtnA.wasPressed()) {
        Serial.println("wasPressed");
    }
}
```

## API

M5Capsule库基于M5Unified库实现, 按键部分使用了M5Unified库中的`Button_Class`, 更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

