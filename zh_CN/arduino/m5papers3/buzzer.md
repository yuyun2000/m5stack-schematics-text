# PaperS3 Buzzer 蜂鸣器

PaperS3 蜂鸣器相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5PaperS3
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

### 播放音阶

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::DejaVu40);

  M5.Display.print("\nStart playing\nmusical scale");

  M5.Speaker.setVolume(200);  // 0~255, bigger is louder
}

void loop() {
  M5.update();

  M5.Speaker.tone(880, 500);  // frequency (Hz), duration (ms)
  delay(500);
  M5.Speaker.tone(990, 500);
  delay(500);
  M5.Speaker.tone(1120, 500);
  delay(500);
  M5.Speaker.tone(1180, 500);
  delay(500);
  M5.Speaker.tone(1320, 500);
  delay(500);
  M5.Speaker.tone(1480, 500);
  delay(500);
  M5.Speaker.tone(1650, 500);
  delay(500);
  M5.Speaker.tone(1760, 500);
  delay(1000);

  M5.Speaker.tone(1760, 500);
  delay(500);
  M5.Speaker.tone(1650, 500);
  delay(500);
  M5.Speaker.tone(1480, 500);
  delay(500);
  M5.Speaker.tone(1320, 500);
  delay(500);
  M5.Speaker.tone(1180, 500);
  delay(500);
  M5.Speaker.tone(1120, 500);
  delay(500);
  M5.Speaker.tone(990, 500);
  delay(500);
  M5.Speaker.tone(880, 500);
  delay(1000);
}
```

该程序将会播放 12345671、17654321 的音阶。

### 生日快乐歌

```cpp line-num
// Happy birthday song

#include <M5Unified.h>
#include <M5GFX.h>

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::FreeMonoBold24pt7b);

  M5.Display.print("\n\n   Happy birthday\n   to\n   you\n\n\n");
  M5.Display.print("      i  i  i\n     |:|:|:|:|\n    |||||||||||\n   {~~~~~~~~~~~}\n  [#############]\n  |#############|\n  |#############|\n  \\_____________/\n");

  M5.Speaker.setVolume(200);  // 0~255, bigger is louder
}

void loop() {
  M5.update();

  playHappyBirthday();
}

void playHappyBirthday() {
  int notes[] = {
    1320, 1320, 1480, 1320, 0, 1760, 1650, 0,
    1320, 1320, 1480, 1320, 0, 1980, 1760, 0,
    1320, 1320, 2600, 2200, 0, 1760, 1650, 1480, 0,
    2350, 2350, 2200, 1760, 0, 1980, 1760, 0
  };

  int durations[] = {
    300, 300, 600, 400, 200, 600, 600, 300,
    300, 300, 600, 400, 200, 600, 600, 300,
    300, 300, 600, 400, 200, 600, 600, 600, 300,
    300, 300, 600, 400, 200, 600, 600, 300
  };

  int count = sizeof(notes) / sizeof(int);
  for (int i = 0; i < count; i++) {
    if (notes[i] == 0) {
      delay(durations[i]);
    } else {
      M5.Speaker.tone(notes[i], durations[i]);
      delay(durations[i] + 30);
    }
  }
}
```

该程序将会播放生日快乐歌，并在屏幕上显示一个蛋糕。

## API

PaperS3 蜂鸣器部分使用了 `M5Unified` 库中的 `Speaker_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)