# StickS3 Mic 麦克风

StickS3 Mic 相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include "M5Unified.h"

static constexpr const size_t record_number     = 256;
static constexpr const size_t record_length     = 256;
static constexpr const size_t record_size       = record_number * record_length;
static constexpr const size_t record_samplerate = 18000;
static size_t rec_record_idx  = 2;
static size_t draw_record_idx = 0;
static int16_t *rec_data;
static int32_t w;

static bool indicator_visible = true;
static uint32_t indicator_timer = 0;
static constexpr uint32_t indicator_interval = 500;//ms
static uint16_t indicator_color = RED;

static void updateIndicator(void) {
    uint32_t now = millis();
    if (now - indicator_timer >= indicator_interval) {
        indicator_timer = now;
        indicator_visible = !indicator_visible;
    }
    if (indicator_visible) {
        M5.Lcd.fillCircle(85, 10, 8, indicator_color);
    } else {
        M5.Lcd.fillCircle(85, 10, 8, BLACK);
    }
}

void setup(void) {
    M5.begin();
    M5.Lcd.setRotation(1);
    M5.Lcd.setTextDatum(middle_center);
    M5.Lcd.setTextColor(WHITE);
    M5.Lcd.setFont(&fonts::FreeMonoBold9pt7b);
    w = M5.Lcd.width();
    rec_data = (typeof(rec_data))heap_caps_malloc(record_size *sizeof(int16_t), MALLOC_CAP_8BIT);
    memset(rec_data, 0, record_size * sizeof(int16_t));
    M5.Speaker.setVolume(200);
    // Since the microphone and speaker cannot be used at the same time,
    // turn off the speaker here.
    M5.Speaker.end();
    M5.Mic.begin();
    indicator_color = RED;
    updateIndicator();
    M5.Lcd.drawString("REC", w / 2, 12);
    M5.Lcd.drawString("BtnA to play record", w / 2, 80);
}

void loop(void) {
    M5.update();
    if (M5.Mic.isEnabled()) {
        static constexpr int shift = 6;
        auto data = &rec_data[rec_record_idx * record_length];
        updateIndicator();
        if (M5.Mic.record(data, record_length, record_samplerate)) {
            data = &rec_data[draw_record_idx * record_length];
            M5.Lcd.display();
            updateIndicator();
            M5.Lcd.drawString("REC", w / 2, 12);
            M5.Lcd.drawString("BtnA to play record", w / 2, 80);
            if (++draw_record_idx >= record_number) {
                draw_record_idx = 0;
            }
            if (++rec_record_idx >= record_number) {
                rec_record_idx = 0;
            }
        }
    }
    if (M5.BtnA.wasPressed()) {
        if (M5.Speaker.isEnabled()) {
            while (M5.Mic.isRecording()) {
                delay(1);
            }
            M5.Lcd.clear();
            indicator_color = GREEN;
            indicator_visible = true;
            indicator_timer = millis();
            updateIndicator();
            M5.Lcd.drawString("PLAY", w / 2, 12);
            // Since the microphone and speaker cannot be used at the same time, 
            // turn off the microphone here.
            M5.Mic.end();
            M5.Speaker.begin();
            int start_pos = rec_record_idx * record_length;
            if (start_pos < record_size) {
                M5.Speaker.playRaw(&rec_data[start_pos],
                                       record_size - start_pos,
                                       record_samplerate, false, 1, 0);
            }
            if (start_pos > 0) {
                M5.Speaker.playRaw(rec_data, start_pos, record_samplerate,
                                       false, 1, 0);
            }
            do {
                delay(1);
                M5.update();
                updateIndicator();
            } while (M5.Speaker.isPlaying());
            // Since the microphone and speaker cannot be used at the same time, 
            // turn off the speaker here.
            M5.Speaker.end();
            M5.Mic.begin();
            M5.Lcd.clear();
            indicator_color = RED;
            indicator_visible = true;
            indicator_timer = millis();
            updateIndicator();
            M5.Lcd.drawString("REC", w / 2, 12);
        }
    }
}
```

该程序的功能是，屏幕上会显示麦克风录音状态，并在按下按键 A 时播放录音，录音播放完毕后会自动返回录音状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_mic_rec.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_mic_play.jpg" width="30%">

## API

StickS3 Mic 部分使用了 `M5Unified` 库中的 `Mic_Class` 及 `Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Mic Class](/zh_CN/arduino/m5unified/mic_class)
- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

