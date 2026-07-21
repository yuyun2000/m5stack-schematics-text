# Unit C6L RGB LED

Unit C6L RGB LED 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5UnitC6L
- M5Unified 库版本 >= 0.2.10
- Adafruit NeoPixel 库版本 >= 1.15.1

```cpp line-num
#define LED_PIN  2
#define NUM_LEDS 1

#include <M5Unified.h>
#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel led(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  M5.begin();

  led.begin();
  led.show();
}

void loop() {
  // Red
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(255, 0, 0)); }
  led.show();
  delay(500);

  // Green
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(0, 255, 0)); }
  led.show();
  delay(500);

  // Blue
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(0, 0, 255)); }
  led.show();
  delay(500);

  // Yellow
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(255, 255, 0)); }
  led.show();
  delay(500);

  // Magenta
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(255, 0, 255)); }
  led.show();
  delay(500);

  // Cyan
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(0, 255, 255)); }
  led.show();
  delay(500);

  // White (all on)
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(255, 255, 255)); }
  led.show();
  delay(500);

  // Black (all off)
  for (char i = 0; i <= NUM_LEDS; i++) { led.setPixelColor(i, led.Color(0, 0, 0)); }
  led.show();
  delay(500);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/RGB.gif" width="50%">

## API

Unit C6L RGB LED 部分使用了`Adafruit NeoPixel`库，更多相关的 API 可以参考下方文档：

- [Adafruit NeoPixel - GitHub](https://github.com/adafruit/Adafruit_NeoPixel)
- [Adafruit NeoPixel Docs 1](https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use)
- [Adafruit NeoPixel Docs 2](https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html)