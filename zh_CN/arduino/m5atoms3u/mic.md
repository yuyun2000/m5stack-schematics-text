# AtomS3U Mic 麦克风

AtomS3U Mic 麦克风案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5AtomS3
- M5Unified 库版本 >= 0.2.13
- [FastLED](https://github.com/FastLED/FastLED) 库版本 >= 3.5.0

#> 说明 | 请根据实际环境调整 `NOISE_FLOOR` 和 `MAX_LEVEL` 数值，以获得更好的音频响应效果。

```cpp line-num
#include <M5Unified.h>
#include <FastLED.h>

#define PIN_LED     35          // Onboard RGB LED pin
#define NUM_LEDS    1           // Number of LEDs (onboard = 1)

static constexpr size_t record_length     = 320;   // Number of samples per audio frame

CRGB leds[NUM_LEDS] = {CRGB::Green};  // LED array, initialized to green

static int16_t rec_data[record_length]; // Audio sample buffer

// ================= Tunable parameters =================
#define NOISE_FLOOR   300    // Noise floor threshold (environment-dependent)
#define MAX_LEVEL     5000   // Maximum expected audio level

uint8_t hue = 0;             // Current HSV hue (0–255, wraps automatically)

void setup() {
    auto cfg = M5.config();
    cfg.internal_mic = true;     // Enable onboard microphone
    M5.begin(cfg);

    Serial.begin(115200);
    Serial.println("AtomS3U Sound Reactive RGB LED");

    // Start microphone
    M5.Mic.begin();

    // ================= LED initialization =================
    FastLED.addLeds<SK6812, PIN_LED, GRB>(leds, NUM_LEDS); 
    FastLED.setBrightness(255);                            
    FastLED.show();                                  
    delay(500); 
}

void loop() {
    M5.update();
;
    
    if (!M5.Mic.isEnabled()) {
        leds[0] = CRGB::Red;// Show red LED as error/status indicator
        FastLED.show();
        return;
    }

    // Record one frame of audio samples
    if (M5.Mic.record(rec_data, record_length)) {

        // ================= Audio level calculation =================
        uint32_t sum = 0;
        for (size_t i = 0; i < record_length; i++) {
            sum += abs(rec_data[i]); // Accumulate absolute sample values
        }

        // Calculate average audio amplitude
        uint32_t level = sum / record_length;

        // Apply noise floor (prevent very low values)
        if (level < NOISE_FLOOR) level = NOISE_FLOOR;

        // ================= Audio-to-LED mapping =================
        // Map audio level to LED brightness (1–255)
        uint8_t brightness = map(level, NOISE_FLOOR, MAX_LEVEL, 1, 255);
        brightness = constrain(brightness, 1, 255);

        // Increase hue based on audio level (louder sound = faster color change)
        hue += map(level, NOISE_FLOOR, MAX_LEVEL, 1, 5);

        // Set LED color using HSV model
        leds[0] = CHSV(hue, 255, brightness);

        // Update LED output
        FastLED.show();

        // Debug output
        Serial.printf("Level:%d Bright:%d Hue:%d\n", level, brightness, hue);
    }
}
```

设备上电后，RGB LED 将根据环境声音的强弱变化颜色和亮度。较大的声音会使 LED 变得更亮并快速变色，而较小的声音则会使 LED 显得较暗且颜色变化较慢。请确保在一个有适当音量的环境中测试，以观察效果。

## 驱动库

- [FastLED](https://github.com/FastLED/FastLED)