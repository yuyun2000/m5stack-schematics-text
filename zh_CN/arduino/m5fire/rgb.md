# Fire RGB LED

Fire RGB LED 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Fire
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.11
- Adafruit NeoPixel 库版本 >= 1.15.1

```cpp line-num
#include <M5Unified.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN 15
#define NUM_LEDS 10

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);
  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextFont(&fonts::Orbitron_Light_24);
  M5.Display.setTextSize(1);
  M5.Display.drawString("RGB LED Test", M5.Display.width() / 2, M5.Display.height() / 2);
  strip.begin();
  strip.show();
}

void loop() {
  // Red
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(255, 0, 0)); }
  strip.show();
  delay(500);

  // Green
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(0, 255, 0)); }
  strip.show();
  delay(500);

  // Blue
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(0, 0, 255)); }
  strip.show();
  delay(500);

  // Yellow
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(255, 255, 0)); }
  strip.show();
  delay(500);

  // Magenta
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(255, 0, 255)); }
  strip.show();
  delay(500);

  // Cyan
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(0, 255, 255)); }
  strip.show();
  delay(500);

  // White (all on)
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(255, 255, 255)); }
  strip.show();
  delay(500);

  // Black (all off)
  for (char i = 0; i <= NUM_LEDS; i++) { strip.setPixelColor(i, strip.Color(0, 0, 0)); }
  strip.show();
  delay(500);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Arduino_RGB.gif" width="50%">

## API

Fire RGB LED 部分使用了`Adafruit NeoPixel`库，更多相关的 API 可以参考下方文档：

- [Adafruit NeoPixel - GitHub](https://github.com/adafruit/Adafruit_NeoPixel)
- [Adafruit NeoPixel Docs 1](https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use)
- [Adafruit NeoPixel Docs 2](https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html)