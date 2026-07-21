# PaperColor RGB LED

PaperColor RGB LED 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21
- Adafruit_NeoPixel 库版本 >= 1.15.4
- M5PM1 库版本 >= 1.0.1

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Adafruit_NeoPixel.h>

static constexpr uint8_t LED_PIN   = 21;
static constexpr uint8_t LED_COUNT = 2;

M5PM1 pm1;
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
static bool pm1_ready = false;

static void setSingleLed(uint8_t index, uint32_t color)
{
    if (index >= LED_COUNT) return;
    pixels.setPixelColor(index, color);
    pixels.show();
}

static void setAllLeds(uint32_t color)
{
    for (uint8_t i = 0; i < LED_COUNT; ++i)
    {
        pixels.setPixelColor(i, color);
    }
    pixels.show();
}

static void showMessage(const char* msg)
{
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(4);
    M5.Display.setTextSize(1);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString(msg, M5.Display.width() / 2, M5.Display.height() / 2);
}

void setup()
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    M5.Display.setEpdMode(epd_mode_t::epd_fast);

    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);
    pm1_ready       = (err == M5PM1_OK);

    if (pm1_ready)
    {
        pm1.setLdoEnable(true);
    }

    pixels.begin();
    pixels.setBrightness(80);
    setAllLeds(pixels.Color(255, 0, 0));

    showMessage("RGB LED TEST");
}

void loop()
{
    setAllLeds(0);
    setSingleLed(0, pixels.Color(255, 255, 255));
    delay(500);
    setAllLeds(0);
    setSingleLed(1, pixels.Color(255, 255, 255));
    delay(500);

    pixels.setPixelColor(0, pixels.Color(255, 0, 0));
    pixels.setPixelColor(1, pixels.Color(0, 0, 255));
    pixels.show();
    delay(500);
    pixels.setPixelColor(0, pixels.Color(0, 0, 255));
    pixels.setPixelColor(1, pixels.Color(255, 0, 0));
    pixels.show();
    delay(500);

    setAllLeds(pixels.Color(255, 0, 0));
    delay(500);
    setAllLeds(pixels.Color(0, 255, 0));
    delay(500);
    setAllLeds(pixels.Color(0, 0, 255));
    delay(500);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_rgb_led_demo_01.jpg" width="50%">
