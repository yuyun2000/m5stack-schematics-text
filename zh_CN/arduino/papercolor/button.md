# PaperColor Button 按键

PaperColor 按键输入相关 API 与案例程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_button_demo_01.jpg" width="50%">

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include <M5Unified.h>

static void showMessage(const char* msg)
{
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(4);
    M5.Display.setTextSize(1);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString(msg, M5.Display.width() / 2, M5.Display.height() / 2);
}

void setup()
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    Serial.begin(115200);
    M5.Display.setEpdMode(epd_mode_t::epd_fast);

    showMessage("Ready: press A / B / C");
}

void loop()
{
    M5.update();

    if (M5.BtnA.wasPressed()) Serial.println("A was Pressed");
    if (M5.BtnB.wasPressed()) Serial.println("B was Pressed");
    if (M5.BtnC.wasPressed()) Serial.println("C was Pressed");

    delay(100);
}
```

完成程序烧录后，通过串口监视器可以查看按键状态日志

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_button_demo_02.png" width="70%">

## API

PaperColor 按键部分使用了 M5Unified 库中的`Button_Class`, 更多按键相关的 API 可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)
