# Tab5 Speaker 扬声器

Tab5 Speaker扬声器相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.0
- 开发板选项 = M5Tab5
- M5Unified 库版本 >= 0.2.17
- M5GFX 库版本 >= 0.2.22

```cpp line-num
##include "M5Unified.h"

void setup()
{
    M5.begin();
    M5.Display.clear(WHITE);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::FreeMonoBold24pt7b);
    M5.Display.setTextSize(1);
    M5.Display.drawString("Speaker Test", M5.Display.width() / 2, M5.Display.height() / 2);
}

void loop()
{
    M5.Speaker.tone(10000, 60);
    delay(1000);
    M5.Speaker.tone(8000, 60);
    delay(1000);
    M5.Speaker.tone(6000, 60);
    delay(1000);
    M5.Speaker.tone(4000, 60);
    delay(1000);
    M5.Speaker.tone(2000, 60);
    delay(1000);
}  
```

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Arduino_speaker.mp4" type="video/mp4"></video>

## API

Tab5 Speaker部分驱动使用了M5Unified库中的`Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

