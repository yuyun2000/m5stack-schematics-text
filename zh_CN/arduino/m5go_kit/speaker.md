# M5GO Speaker 扬声器

M5GO Speaker扬声器相关API与案例程序。

## 案例程序

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);
    M5.Display.drawString("Speaker Test", M5.Display.width() / 2, M5.Display.height() / 2);
}

void loop()
{
    M5.Speaker.tone(10000, 100);
    delay(1000);
    M5.Speaker.tone(4000, 20);
    delay(1000);
}
```

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/659/Core_Arduino_speaker.mp4" type="video/mp4"></video>

## API

M5GO Speaker部分驱动使用了M5Unified库中的`Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

