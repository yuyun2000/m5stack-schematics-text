# AtomS3R Button 按键

AtomS3R 按键输入相关 API 与案例程序。

#>注意事项: | 使用时需要在主循环中包含`M5.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5AtomS3R
- M5Unified 库版本 >= 0.2.17
- M5GFX 库版本 >= 0.2.22

```cpp line-num
#include "M5Unified.h"

void setup() {
    M5.begin();
    Serial.begin(115200);
}

void loop() {
    M5.update();
    if (M5.BtnA.wasPressed()) {
        Serial.println("Pressed");
    }
    if (M5.BtnA.wasReleased()) {
        Serial.println("Released");
    }
}
```

烧录上述程序到 AtomS3R 后，打开串口监视器，按下按键（屏幕）时会输出 "Pressed"，松开按键（屏幕）时会输出 "Released"。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/C126_AtomS3R_Arduino_pictures_01.png" width="40%">

## API

AtomS3R 按键部分使用了 M5Unified 库中的 `Button_Class`，更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

