# PaperColor Arduino 示例程序编译与烧录

## 1. 准备工作

- 1. Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2. 板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板 `M5PaperColor`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_select_board_01.png" width="70%" />

- 3. 驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成 `PaperColor`驱动库安装，并根据提示安装全部依赖库。

<!-- todo: 补下载库的截图，对应最新版本 -->

## 2.端口选择

将设备通过 USB-C 数据线连接至电脑，长按侧面的电源按键，待设备进入下载模式后，可在 Arduino IDE 中选择对应的主控和设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/C151-power-operate_02.gif" width="35%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_select_port_01.png" width="70%" />

## 3.程序编译&烧录

复制下方案例程序至 Arduino IDE，点击上传按钮，程序将编译并上传至 PaperColor。

```cpp line-num
#include <M5Unified.h>

M5Canvas Canvas(&M5.Display);

static void drawBoldText(M5Canvas& canvas, const String& text, int x, int y, uint16_t color)
{
    // Draw the text in small offsets to emulate a bold weight on EPD.
    canvas.setTextColor(color);
    canvas.drawString(text, x, y);
    canvas.drawString(text, x + 1, y);
    canvas.drawString(text, x, y + 1);
    canvas.drawString(text, x + 1, y + 1);
}

void setup()
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    M5.Display.setEpdMode(epd_mode_t::epd_quality);

    const int screen_w = M5.Display.width();
    const int screen_h = M5.Display.height();

    Canvas.createSprite(screen_w, screen_h);
    Canvas.fillSprite(WHITE);

    const uint16_t band_colors[6] = {YELLOW, RED, GREEN, BLUE, BLACK, WHITE};
    const int band_h             = screen_h / 6;

    for (int i = 0; i < 6; ++i)
    {
        const int y = i * band_h;
        const int h = (i == 5) ? (screen_h - y) : band_h;
        Canvas.fillRect(0, y, screen_w, h, band_colors[i]);
    }

    const int white_band_y = 5 * band_h;
    const int white_band_h = screen_h - white_band_y;

    Canvas.setTextFont(4);
    Canvas.setTextSize(2);
    Canvas.setTextDatum(middle_left);
    Canvas.setTextColor(BLACK);

    const String text_paper = "PAPER";
    const String text_color = "COLOR";
    const int gap_w         = Canvas.textWidth("   ");
    const int total_w       = Canvas.textWidth(text_paper) + gap_w + Canvas.textWidth(text_color);
    const int start_x       = (screen_w - total_w) / 2;
    const int text_y        = white_band_y + (white_band_h / 2);

    drawBoldText(Canvas, text_paper, start_x, text_y, BLACK);

    int x = start_x + Canvas.textWidth(text_paper) + gap_w;
    const uint16_t color_text_colors[5] = {RED, YELLOW, GREEN, YELLOW, BLUE};
    for (int i = 0; i < text_color.length(); ++i)
    {
        const String ch = text_color.substring(i, i + 1);
        drawBoldText(Canvas, ch, x, text_y, color_text_colors[i]);
        x += Canvas.textWidth(ch);
    }

    Canvas.pushSprite(0, 0);
}

void loop()
{
    M5.update();
    delay(100);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_demo_01.png" width="70%">

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_demo_02.jpg" width="50%">

## 4.相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- Arduino API & Examples
  - [Button](/zh_CN/arduino/papercolor/button)
  - [Battery](/zh_CN/arduino/papercolor/battery)
  - [Display](/zh_CN/arduino/papercolor/display)
  - [IR NEC](/zh_CN/arduino/papercolor/ir_nec)
  - [RGB LED](/zh_CN/arduino/papercolor/rgb_led)
  - [MIC](/zh_CN/arduino/papercolor/mic)
  - [Speaker](/zh_CN/arduino/papercolor/speaker)
  - [microSD](/zh_CN/arduino/papercolor/microsd)
  - [RTC](/zh_CN/arduino/papercolor/rtc)
  - [SHT40](/zh_CN/arduino/papercolor/sht40)
  - [Wakeup](/zh_CN/arduino/papercolor/wakeup)
  - [M5PM1](/zh_CN/arduino/papercolor/m5pm1)
