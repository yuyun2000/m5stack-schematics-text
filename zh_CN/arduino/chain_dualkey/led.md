# Chain DualKey RGB LED

Chain DualKey RGB LED 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.4
- 开发板选项 = M5ChainDualKey
- Adafruit NeoPixel 库版本 >= 1.15.2

```cpp line-num
#define LED_PWR_PIN 40
#define LED_SIG_PIN 21
#define NUM_LEDS 2

#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel LED(NUM_LEDS, LED_SIG_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(LED_PWR_PIN, OUTPUT);
  digitalWrite(LED_PWR_PIN, HIGH);

  LED.begin();
  LED.show();
}

void loop() {
  // White (all on)
  for (int i = 0; i <= NUM_LEDS; i++) { LED.setPixelColor(i, LED.Color(255, 255, 255)); }
  LED.show();
  delay(500);

  // Black (all off)
  for (int i = 0; i <= NUM_LEDS; i++) { LED.setPixelColor(i, LED.Color(0, 0, 0)); }
  LED.show();
  delay(500);

  // Red & Green
  LED.setPixelColor(0, LED.Color(255, 0, 0));
  LED.setPixelColor(1, LED.Color(0, 255, 0));
  LED.show();
  delay(500);

  // Blue & Yellow
  LED.setPixelColor(0, LED.Color(0, 0, 255));
  LED.setPixelColor(1, LED.Color(255, 255, 0));
  LED.show();
  delay(500);

  // Magenta & Cyan
  LED.setPixelColor(0, LED.Color(255, 0, 255));
  LED.setPixelColor(1, LED.Color(0, 255, 255));
  LED.show();
  delay(500);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/rgb.gif" width="50%">

## API

Chain DualKey RGB LED 部分使用了`Adafruit NeoPixel`库，更多相关的 API 可以参考下方文档：

- [Adafruit NeoPixel - GitHub](https://github.com/adafruit/Adafruit_NeoPixel)
- [Adafruit NeoPixel Docs 1](https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use)
- [Adafruit NeoPixel Docs 2](https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html)