# Tough Speaker 扬声器

Tough 扬声器相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Tough
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

void setup() {
  M5.begin();
  M5.Display.setRotation(1);
  M5.Display.setFont(&fonts::DejaVu40);

  M5.Display.print("\nStart playing\nmusical scale");

  M5.Speaker.setVolume(128);  // 0~255, bigger is louder
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

## API

Tough 扬声器部分使用了 `M5Unified` 库中的 `Speaker_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)