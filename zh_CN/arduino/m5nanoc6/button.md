# NanoC6 Button 按键

NanoC6 Button 按键相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5NanoC6
- M5NanoC6 库版本 = 1.0.0

```cpp line-num
#include <M5NanoC6.h>

void setup() {
    NanoC6.begin();
}

void loop() {
    NanoC6.update();
    if (NanoC6.BtnA.wasPressed()) {
        Serial.println("Button A was pressed");
    }
    if (NanoC6.BtnA.wasHold()) {
        Serial.println("Button A was hold");
    }
    if (NanoC6.BtnA.wasReleased()) {
        Serial.println("Button A was released");
    }
}
```

该程序将检测 NanoC6 正面的输入按键的状态，并在串口监视器打印按键事件：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/NanoC6_Arduino_tutorial_button_part_01.png" width="90%" >

## API

NanoC6 按键部分参考了 M5Unified 库中的`Button_Class`, 更多按键相关的 API 可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)
