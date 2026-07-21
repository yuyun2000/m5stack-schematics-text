# Atom VoiceS3R Mic 麦克风

Atom VoiceS3R 麦克风相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5AtomS3R
- M5Unified 库版本 >= 0.2.8

```cpp line-num
#include <M5Unified.h>

static constexpr const size_t record_number = 256;
static constexpr const size_t record_length = 200;
static constexpr const size_t record_size = record_number * record_length;
static constexpr const size_t record_samplerate = 16000;
static size_t rec_record_idx = 2;
static int16_t *rec_data;

void setup() {
  M5.begin();
  M5.Speaker.setVolume(255);
  auto cfg = M5.Mic.config();
  cfg.noise_filter_level = (cfg.noise_filter_level + 8) & 255;
  M5.Mic.config(cfg);

  rec_data = (typeof(rec_data))heap_caps_malloc(record_size * sizeof(int16_t), MALLOC_CAP_8BIT);
  memset(rec_data, 0, record_size * sizeof(int16_t));

  // Since the microphone and speaker cannot be used at the same time, turn off the speaker here.
  M5.Speaker.end();
  M5.Mic.begin();
}

void loop() {
  M5.update();

  if (M5.Mic.isEnabled()) {
    auto data = &rec_data[rec_record_idx * record_length];
    if (M5.Mic.record(data, record_length, record_samplerate)) {
      if (++rec_record_idx >= record_number) {
        rec_record_idx = 0;
      }
    }
  }

  if (M5.BtnA.wasClicked()) {
    if (M5.Speaker.isEnabled()) {
      while (M5.Mic.isRecording()) {
        M5.delay(1);
      }

      // Since the microphone and speaker cannot be used at the same time, turn off the microphone here.
      M5.Mic.end();
      M5.Speaker.begin();

      int start_pos = rec_record_idx * record_length;
      if (start_pos < record_size) {
        M5.Speaker.playRaw(&rec_data[start_pos], record_size - start_pos, record_samplerate, false, 1, 0);
      }
      if (start_pos > 0) {
        M5.Speaker.playRaw(rec_data, start_pos, record_samplerate, false, 1, 0);
      }

      do {
        M5.delay(1);
        M5.update();
      } while (M5.Speaker.isPlaying());

      // Since the microphone and speaker cannot be used at the same time, turn off the speaker here.
      M5.Speaker.end();
      M5.Mic.begin();
    }
  }
}
```

将以上程序编译并上传至 Atom VoiceS3R，该程序会使用麦克风采集声音并循环缓存，短按设备正面的按键播放最近几秒的缓存录音。

## API

Atom VoiceS3R 麦克风部分使用了`M5Unified`库中的`Mic_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Mic Class](/zh_CN/arduino/m5unified/mic_class)
