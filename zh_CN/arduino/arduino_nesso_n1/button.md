# Arduino Nesso N1 Button 按键

Arduino Nesso N1 按键输入相关 API 与案例程序。

\#> 注意事项: | 使用时需要在主循环中包含`M5.update()`函数，用于读取状态更新且尽可能减少阻塞情况，否则可能无法及时获取的按键变化状态。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    cfg.serial_baudrate = 115200;
    M5.begin(cfg);
}

void loop()
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        Serial.println("A Btn Pressed");
    }
    if (M5.BtnA.wasReleased()) {
        Serial.println("A Btn Released");
    }
    if (M5.BtnB.wasPressed()) {
        Serial.println("B Btn Pressed");
    }
    if (M5.BtnB.wasReleased()) {
        Serial.println("B Btn Released");
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_button_example_01.jpg" width="50%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_button_example_02.png" width="70%" />

## API

Arduino Nesso N1 的按键驱动部分使用了 M5Unified 库中的`Button_Class`, 更多按键相关的 API 可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)
