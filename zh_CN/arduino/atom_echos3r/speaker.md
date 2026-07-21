# Atom VoiceS3R Speaker 扬声器

Atom VoiceS3R 扬声器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5AtomS3R
- M5Unified 库版本 >= 0.2.8

```cpp line-num
#include "M5Unified.h"
#include "test_audio.h"

// 8bit unsigned 44.1kHz mono (exclude wav header)
extern const uint8_t test_audio[46000];

void setup() {
  M5.begin();
  M5.Speaker.setVolume(64);

  M5.Speaker.tone(7000, 500);  // frequency, duration
  delay(500);
  M5.Speaker.tone(4000, 100);
  delay(500);
}

void loop() {
  M5.Speaker.playRaw(test_audio, sizeof(test_audio) / sizeof(test_audio[0]));
  while (M5.Speaker.isPlaying()) {
    delay(1);
  }
  delay(100);
}
```

点击下载 [test_audio.zip](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/test_audio.zip)，解压后得到`test_audio.h`文件。将上方代码复制到 Arduino IDE 并保存，然后将`test_audio.h`文件放入同一目录，与`.ino`文件并列。点击上传按钮，程序将编译并上传至 Atom VoiceS3R。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Arduino_speaker.png" width="90%">

上传完成后程序开始运行，通过扬声器先播放蜂鸣声然后播放`test_audio.h`文件中的 wav 音频数组。

## API

Atom VoiceS3R 扬声器部分使用了`M5Unified`库中的`Speaker_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)
