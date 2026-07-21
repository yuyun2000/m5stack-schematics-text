# Atom-Lite/Atom-Matrix Button 按键

Atom-Lite/Atom-Matrix 按键输入相关 API 与案例程序。

#> 注意事项 | 使用时需要在主循环中包含 `M5.update()` 函数用于读取状态更新，且尽可能减少阻塞，否则可能无法及时获取按键变化。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5Atom
- M5Unified 库版本 >= 0.2.13

```cpp line-num
#include "M5Unified.h"

void setup() {
    M5.begin();
    Serial.begin(115200);
}

void loop() {
    M5.update();

    if (M5.BtnA.wasPressed()) {
        Serial.println("BtnA was pressed");
    }
    if (M5.BtnA.wasReleased()) {
        Serial.println("BtnA was released");
    }
    if (M5.BtnA.wasSingleClicked()) {
        Serial.println("BtnA was single clicked");
    }
    if (M5.BtnA.wasDoubleClicked()) {
        Serial.println("BtnA was double clicked");
    }
    if (M5.BtnA.wasHold()) {
        Serial.println("BtnA was held");
    }
}
```

该程序将检测设备正面按键的状态（按下、松开、短按一次、短按两次、长按），并在串口监视器打印消息（例如）：

```
BtnA was pressed
BtnA was released
BtnA was single clicked
BtnA was pressed
BtnA was held
BtnA was released
```

## API

Atom-Lite/Atom-Matrix 按键部分使用了 `M5Unified` 库中的`Button_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)