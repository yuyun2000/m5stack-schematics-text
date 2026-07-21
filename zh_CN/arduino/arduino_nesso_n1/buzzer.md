# Arduino Nesso N1 Buzzer 蜂鸣器

Arduino Nesso N1 Buzzer 蜂鸣器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setRotation(1);
    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);
    M5.Display.drawString("Buzzer Test", M5.Display.width() / 2,
                                M5.Display.height() / 2);
}

void loop() {
    M5.Speaker.tone(10000, 100);
    delay(1000);
    M5.Speaker.tone(4000, 20);
    delay(1000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_buzzer_example_01.jpg" width="50%" />

## API

Arduino Nesso N1 的 Buzzer 驱动部分使用了 M5Unified 库中的`Speaker_Class`, 更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)
