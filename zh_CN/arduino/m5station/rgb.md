# Station RGB LED

Station RGB LED案例程序。本案例基于[Adafruit NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)库实现, 使用前请通过库管理安装[Adafruit NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)依赖库。

## 案例程序

```cpp line-num
#include <M5Unified.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN    4
#define NUM_LEDS   7

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
    //红色
    for(char i = 0; i <= NUM_LEDS; i++)
    {strip.setPixelColor(i, strip.Color(255, 0, 0)); }    
    strip.show();
    delay(1000);
  
    //绿色
    for(char i = 0; i <= NUM_LEDS; i++)
    {strip.setPixelColor(i, strip.Color(0, 255, 0)); }
    strip.show();
    delay(1000);
  
    //蓝色
    for(char i = 0; i <= NUM_LEDS; i++)
    {strip.setPixelColor(i, strip.Color(0, 0, 255)); }
    strip.show();
    delay(1000);
} 
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/station_arduino_rgb.jpg" width="50%">

