# PowerHub RGB LED

PowerHub RGB LED 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

void setup() {
  M5.begin();
  M5.Led.setBrightness(255);  // 0 ~ 255
}

void loop() {
  M5.update();

  // color enums, see: https://docs.m5stack.com/en/arduino/m5gfx/m5gfx_appendix#color%20encoding
  M5.Led.setAllColor(TFT_WHITE);
  M5.Led.display();
  delay(500);

  // r, g, b
  M5.Led.setAllColor(0, 0, 0);  // Black (off)
  M5.Led.display();
  delay(500);

  // index, r, g, b
  M5.Led.setColor(0, 255, 255, 255);  // White
  M5.Led.setColor(1,   0,   0,   0);  // Black (off)
  M5.Led.setColor(2, 255,   0,   0);  // Red
  M5.Led.setColor(3,   0, 255,   0);  // Green
  M5.Led.setColor(4,   0,   0, 255);  // Blue
  M5.Led.setColor(5, 255, 255,   0);  // Yellow
  M5.Led.setColor(6, 255,   0, 255);  // Magenta
  M5.Led.setColor(7,   0, 255, 255);  // Cyan
  M5.Led.display();
  delay(1000);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_RGB.jpeg" width="50%">

## API

PowerHub RGB LED 部分驱动使用了`M5Unified`库中的`LED_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - LED Class](/zh_CN/arduino/m5unified/led_class)