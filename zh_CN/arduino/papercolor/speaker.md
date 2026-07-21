# PaperColor Speaker 扬声器

PaperColor 扬声器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include <M5Unified.h>

static void drawScreen()
{
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(RED);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(4);
    M5.Display.setTextSize(2);
    M5.Display.drawString("Speaker Tone Test", M5.Display.width() / 2, M5.Display.height() / 2);
}

void setup()
{
    M5.begin();
    M5.Display.setRotation(1);
    M5.Display.setEpdMode(epd_mode_t::epd_fast);

    drawScreen();
}

void loop()
{
    M5.Speaker.tone(4000, 200);
    delay(2000);
    M5.Speaker.tone(8000, 200);
    delay(2000);
}
```

设备上电后，会每隔 2 秒时间发出两次不同频率的声音:

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_spk_tone_demo_01.jpg" width="50%">

## API

PaperColor 扬声器部分驱动使用了 `M5Unified` 库中的`Speaker_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)
