# StickS3 Speaker 扬声器

StickS3 扬声器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include "M5Unified.h"

void setup() {
    M5.begin();
    M5.Lcd.setRotation(1);
    M5.Lcd.setTextDatum(middle_center);
    M5.Lcd.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Lcd.clear();
    M5.Lcd.drawString("Speaker", M5.Lcd.width() / 2, M5.Lcd.height() / 2);
    delay(100);
}

void loop() {
    M5.Speaker.tone(7000, 100);  // frequency, duration
    delay(1000);
    M5.Speaker.tone(4000, 200);  // frequency, duration
    delay(1000);
}
```

设备上电后，会每隔一秒时间发出两次不同频率的声音。

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_speaker.mp4" type="video/mp4"></video>

## API

StickS3 扬声器部分驱动使用了 `M5Unified` 库中的`Speaker_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)