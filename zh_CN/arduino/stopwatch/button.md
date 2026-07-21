# StopWatch Button 按键

StopWatch 按键输入相关 API 与案例程序。

#>注意事项: | 使用时需要在主循环中包含`M5.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

### 编译要求

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5StopWatch
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    Serial.begin(115200);
}

void loop()
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        Serial.println("BtnA Pressed");
    }
    if (M5.BtnB.wasPressed()) {
        Serial.println("BtnB Pressed");
    }
}
```
具体实现效果请下载例程后，按动按键，打开串口监视窗口查看。

## API

StopWatch 按键部分使用了 M5Unified 库中的 `Button_Class`, 更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

