# Hat SPK Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品:
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat SPK](https://shop.m5stack.com/products/m5stickc-speaker-hat)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-spk/hat-spk_cover_01.webp" width="20%">

## 2. 案例程序

### Play Tone

\#> 案例说明 | Hat SPK 是一款兼容 SticKC 的扬声器，内置 PAM8303 功放 IC（3W 单通道 D 类音频功率放大器）。本案例将使用 StickC-Plus2 通过 GPIO 26 引脚输出 PWM 信号来控制 Hat SPK 来播放音频。

```cpp line-num
#include <M5Unified.h>

const int SPEAKER_PIN = 26;
const int SD_PIN = 0;
const int PWM_CHANNEL = 0;
const int PWM_RESOLUTION = 10;  // 10-bit resolution (0-1023)
const int PWM_FREQ = 40000;     // 40kHz carrier frequency

void setup() {
    M5.begin();

    // Enable speaker
    pinMode(SD_PIN, OUTPUT);
    digitalWrite(SD_PIN, HIGH);

    // Configure LEDC PWM
    ledcAttach(SPEAKER_PIN, PWM_FREQ, PWM_RESOLUTION);
    M5.Display.setRotation(1);  // Depends on the direction of M5StickC-Plus2 be held
    M5.Display.setCursor(40, 60, 2);
    M5.Display.print("Press BtnA to play Audio");
}

void playTone(int frequency, int duration) {
    // Calculate duty cycle for 50% square wave
    int dutyCycle = (1 << (PWM_RESOLUTION - 1));  // 512 for 10-bit

    // Set PWM frequency to audio frequency
    ledcChangeFrequency(SPEAKER_PIN, frequency, PWM_RESOLUTION);
    ledcWrite(SPEAKER_PIN, dutyCycle);

    delay(duration);

    // Stop tone
    ledcWrite(SPEAKER_PIN, 0);
}

void loop() {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    // Play musical notes
    playTone(262, 500);  // C4
    delay(100);
    playTone(294, 500);  // D4
    delay(100);
    playTone(330, 500);  // E4
    delay(100);
    playTone(349, 500);  // F4
    delay(100);
    playTone(392, 500);  // G4
    delay(1000);
  }
}
```

### Play Raw RCM

\#> 案例说明 | 以下链接可以获取源码工程和 m5stack_startup_music.c 文件

- [arduino_hat_spk_raw_pcm_example.zip](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/861/arduino_hat_spk_raw_pcm_example.zip)

```cpp line-num
#include <M5Unified.h>

extern const unsigned char m5stack_startup_music[];
extern const unsigned int m5stack_startup_music_len;

const int HAT_SPK_ENABLE_PIN = 0;
const int HAT_SPK_AUDIO_PIN = 26;

void setup() {
    auto cfg = M5.config();
    cfg.external_speaker.hat_spk = true;
    M5.begin(cfg);

    // Enable speaker
    pinMode(HAT_SPK_ENABLE_PIN, OUTPUT);
    digitalWrite(HAT_SPK_ENABLE_PIN, HIGH);

    // Configure Speaker to use GPIO26（Hat SPK）
    auto spk_cfg = M5.Speaker.config();
    spk_cfg.pin_data_out = HAT_SPK_AUDIO_PIN;
    spk_cfg.sample_rate = 8000;
    spk_cfg.task_pinned_core = APP_CPU_NUM;
    M5.Speaker.config(spk_cfg);
    M5.Speaker.begin();

    M5.Display.setRotation(1);
    M5.Display.setCursor(40, 60, 2);
    M5.Display.print("Press BtnA to play");
}

void playMusic() {
    M5.Display.clear();
    M5.Display.setCursor(40, 60, 2);
    M5.Display.print("Playing...");

    // Use Hat SPK to play audio
    M5.Speaker.playRaw(
        m5stack_startup_music,
        m5stack_startup_music_len,
        8000,
        false,
        1,
        0
    );

    while (M5.Speaker.isPlaying()) {
        M5.update();
        if (M5.BtnA.wasPressed()) {
            M5.Speaker.stop();
            break;
        }
        delay(10);
    }

    M5.Display.clear();
    M5.Display.setCursor(40, 60, 2);
    M5.Display.print("Press BtnA to play");
}

void loop() {
    M5.update();
    if (M5.BtnA.wasPressed()) {
        playMusic();
    }
    delay(10);
}
```

## 3. 编译上传

1. 进入下载模式：不同的 Stick 设备进行程序烧录前需要安装对应的驱动程序，不同的主控设备使用的驱动与安装步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体设备对应的操作方式。

2. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/861/arduino_hat_spk_example_01.png" width="70%">

## 4. 点按 Button A 按键控制 Hat SPK 播放音频显示

该程序在检测到 Button A 按键被按下后，将控制 Hat SPK 播放音频。程序完成编译并上传至设备后，StickC-Plus2 的屏幕上显示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/861/arduino_hat_spk_example_02.jpg" width="70%">
