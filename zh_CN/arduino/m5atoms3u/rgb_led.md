# AtomS3U RGB LED

AtomS3U RGB LED 案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5AtomS3
- [FastLED](https://github.com/FastLED/FastLED) 库版本 >= 3.5.0

```cpp line-num
#include <Arduino.h>
#include <FastLED.h>

#define PIN_BUTTON 41
#define PIN_LED    35
#define NUM_LEDS   1

CRGB leds[NUM_LEDS];
uint8_t led_ih             = 0;
uint8_t led_status         = 0;
String led_status_string[] = {"Rainbow", "Red", "Green", "Blue"};

void setup() {
    Serial.begin(115200);
    Serial.println("AtomS3U demo!");

    pinMode(PIN_BUTTON, INPUT);

    FastLED.addLeds<SK6812, PIN_LED, GRB>(leds, NUM_LEDS);
}

void loop() {
    switch (led_status) {
        case 0:
            leds[0] = CHSV(led_ih, 255, 255);
            break;
        case 1:
            leds[0] = CRGB::Red;
            break;
        case 2:
            leds[0] = CRGB::Green;
            break;
        case 3:
            leds[0] = CRGB::Blue;
            break;
        default:
            break;
    }
    FastLED.show();
    led_ih++;
    delay(15);

    if (!digitalRead(PIN_BUTTON)) {
        delay(5);
        if (!digitalRead(PIN_BUTTON)) {
            led_status++;
            if (led_status > 3) led_status = 0;
            while (!digitalRead(PIN_BUTTON))
                ;
            Serial.print("LED status updated: ");
            Serial.println(led_status_string[led_status]);
        }
    }
}
```

设备上电后，RGB LED 将显示彩虹色。按下设备上的按钮将切换 LED 显示红色、绿色、蓝色和回到彩虹色。每次切换都会在串口监视器中输出当前的 LED 状态。

## 驱动库

- [FastLED](https://github.com/FastLED/FastLED)