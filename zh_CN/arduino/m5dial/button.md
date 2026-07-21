# Dial Button 按键

Dial 按键输入相关 API 与案例程序。

#> 按键位置 | 按键位于产品底部 M5 标志下方，可向下按压灰色边框触发。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Dial
- M5Dial 库版本 >= 1.0.3

#> 注意事项 | 使用时需要在主循环中包含`M5Dial.update()`函数用于读取状态更新，且尽可能减少阻塞情况，否则可能无法及时获取按键变化。

```cpp line-num
#include "M5Dial.h"

void setup() {
  auto cfg = M5.config();
  M5Dial.begin(cfg, false, false);  // encoder, RFID
  Serial.begin(115200);
}

void loop() {
  M5Dial.update();

  if (M5Dial.BtnA.wasPressed()) {
    Serial.println("Button A Pressed");
  }
  if (M5Dial.BtnA.wasReleased()) {
    Serial.println("Button A Released");
  }
}
```

## API

`M5Dial`库基于`M5Unified`库实现，Button 按键部分驱动使用了`M5Unified`库中的`Button_Class`，更多相关的 API 可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)