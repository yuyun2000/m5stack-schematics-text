# StopWatch Speaker 扬声器

StopWatch Speaker 扬声器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5StopWatch
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include "M5Unified.h"

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::FreeMonoBold18pt7b);
    M5.Display.setTextSize(1);
    M5.Display.drawString("Speaker Test", M5.Display.width() / 2,
                                M5.Display.height() / 2);
}

void loop() {
    M5.Speaker.tone(10000, 100);
    delay(1000);
    M5.Speaker.tone(4000, 20);
    delay(1000);
}
```

烧录成功后，您将听到 StackChan 扬声器发出不同频率的声音，分别是 10kHz 和 4kHz。

## API

StopWatch Speaker部分驱动使用了 M5Unified 库中的 `Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

