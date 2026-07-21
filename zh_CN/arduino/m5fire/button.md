# Fire Button 按键

Fire 按键输入相关 API 与案例程序。

#> 注意事项 | 使用时需要在主循环中包含`M5.update()`函数用于读取状态更新，且尽可能减少阻塞，否则可能无法及时获取按键变化。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Fire
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();
  Serial.begin(115200);
}

void loop() {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    Serial.println("BtnA Pressed");
  }
  if (M5.BtnB.wasPressed()) {
    Serial.println("BtnB Pressed");
  }
  if (M5.BtnC.wasPressed()) {
    Serial.println("BtnC Pressed");
  }
}
```

该程序将检测三个按钮是否被按下，并在串口监视器打印消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Arduino_button.png" width="90%">

## API

Fire 按键部分使用了`M5Unified`库中的`Button_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)