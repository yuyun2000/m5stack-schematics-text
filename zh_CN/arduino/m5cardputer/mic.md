# Cardputer Mic 麦克风

Cardputer Mic 麦克风相关 API 与案例程序，适用于 Cardputer 和 Cardputer-Adv。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.0
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.10

```cpp line-num
#include <M5Cardputer.h>

static constexpr const size_t record_number = 256;
static constexpr const size_t record_length = 240;
static constexpr const size_t record_size = record_number * record_length;
static constexpr const size_t record_samplerate = 17000;
static int16_t prev_y[record_length];
static int16_t prev_h[record_length];
static size_t rec_record_idx = 2;
static size_t draw_record_idx = 0;
static int16_t *rec_data;

void setup(void) {
  auto cfg = M5.config();
  M5Cardputer.begin(cfg);

  M5Cardputer.Display.startWrite();
  M5Cardputer.Display.setRotation(1);
  M5Cardputer.Display.setTextDatum(top_center);
  M5Cardputer.Display.setTextColor(WHITE);
  M5Cardputer.Display.setFont(&fonts::FreeSansBoldOblique12pt7b);

  rec_data = (typeof(rec_data))heap_caps_malloc(record_size * sizeof(int16_t), MALLOC_CAP_8BIT);
  memset(rec_data, 0, record_size * sizeof(int16_t));
  M5Cardputer.Speaker.setVolume(255);

  // Turn off the speaker, because the microphone and speaker cannot be used at the same time.
  M5Cardputer.Speaker.end();
  M5Cardputer.Mic.begin();
  M5Cardputer.Display.fillCircle(70, 15, 8, RED);
  M5Cardputer.Display.drawString("REC", 120, 3);
}

void loop(void) {
  M5Cardputer.update();

  if (M5Cardputer.Mic.isEnabled()) {
    static constexpr int shift = 6;
    auto data = &rec_data[rec_record_idx * record_length];
    if (M5Cardputer.Mic.record(data, record_length, record_samplerate)) {
      data = &rec_data[draw_record_idx * record_length];

      int32_t w = M5Cardputer.Display.width();
      if (w > record_length - 1) {
        w = record_length - 1;
      }
      for (int32_t x = 0; x < w; ++x) {
        M5Cardputer.Display.writeFastVLine(x, prev_y[x], prev_h[x], TFT_BLACK);
        int32_t y1 = (data[x] >> shift);
        int32_t y2 = (data[x + 1] >> shift);
        if (y1 > y2) {
          int32_t tmp = y1;
          y1 = y2;
          y2 = tmp;
        }
        int32_t y = ((M5Cardputer.Display.height()) >> 1) + y1;
        int32_t h = ((M5Cardputer.Display.height()) >> 1) + y2 + 1 - y;
        prev_y[x] = y;
        prev_h[x] = h;
        M5Cardputer.Display.writeFastVLine(x, prev_y[x], prev_h[x], WHITE);
      }

      M5Cardputer.Display.display();
      M5Cardputer.Display.fillCircle(70, 15, 8, RED);
      M5Cardputer.Display.drawString("REC", 120, 3);
      if (++draw_record_idx >= record_number) {
        draw_record_idx = 0;
      }
      if (++rec_record_idx >= record_number) {
        rec_record_idx = 0;
      }
    }
  }

  if (M5Cardputer.BtnA.wasHold()) {
    auto cfg = M5Cardputer.Mic.config();
    cfg.noise_filter_level = (cfg.noise_filter_level + 8) & 255;
    M5Cardputer.Mic.config(cfg);
    M5Cardputer.Display.clear();
    M5Cardputer.Display.fillCircle(70, 15, 8, GREEN);
    M5Cardputer.Display.drawString("NF:" + String(cfg.noise_filter_level), 120, 3);

  } else if (M5Cardputer.BtnA.wasClicked()) {
    if (M5Cardputer.Speaker.isEnabled()) {
      M5Cardputer.Display.clear();
      while (M5Cardputer.Mic.isRecording()) {
        delay(1);
      }
      // Turn off the microphone, because the microphone and speaker cannot be used at the same time.
      M5Cardputer.Mic.end();
      M5Cardputer.Speaker.begin();

      M5Cardputer.Display.fillTriangle(70 - 8, 15 - 8, 70 - 8, 15 + 8, 70 + 8, 15, 0x1c9f);
      M5Cardputer.Display.drawString("PLAY", 120, 3);
      int start_pos = rec_record_idx * record_length;
      if (start_pos < record_size) {
        M5Cardputer.Speaker.playRaw(&rec_data[start_pos], record_size - start_pos, record_samplerate, false, 1, 0);
      }
      if (start_pos > 0) {
        M5Cardputer.Speaker.playRaw(rec_data, start_pos, record_samplerate, false, 1, 0);
      }
      do {
        delay(1);
        M5Cardputer.update();
      } while (M5Cardputer.Speaker.isPlaying());

      // Turn off the speaker, because the microphone and speaker cannot be used at the same time.
      M5Cardputer.Speaker.end();
      M5Cardputer.Mic.begin();

      M5Cardputer.Display.clear();
      M5Cardputer.Display.fillCircle(70, 15, 8, RED);
      M5Cardputer.Display.drawString("REC", 120, 3);
    }
  }
}
```

这段程序会在设备屏幕上显示麦克风采集到的声音波形，并缓存最近几秒的录音，按上侧面的 G0 按键（即 BtnA）回放最近几秒的录音（回放音量会比真实音量小）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_mic.jpg" width="70%">

## API

`M5Cardputer`库基于`M5Unified`库实现，Mic 麦克风部分驱动使用了`M5Unified`库中的`Mic_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Mic Class](/zh_CN/arduino/m5unified/mic_class)