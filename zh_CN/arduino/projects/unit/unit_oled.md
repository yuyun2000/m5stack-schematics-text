# Unit OLED Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit OLED](https://shop.m5stack.com/products/oled-unit-1-3-128-64-display)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_cover_01.webp" width="20%">


## 2.案例程序

#>案例说明|Unit OLED 是一款 1.3 英寸的 OLED 拓展屏幕单元。本案例将使用CoreS3主控通过 PORT.A 拓展接口控制，实现文字滚动显示。其他款的M5Stack主控可以通过修改创建`M5UnitOLED display(2, 1, 400000);`实例时的`SDA`, `SCL`引脚配置完成适配。


```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <M5UnitOLED.h>

M5UnitOLED display(2, 1, 400000);  // SDA, SCL, FREQ

M5Canvas canvas(&display);

static constexpr char text[]    = "Hello world ! Hello Unit OLED ! ";
static constexpr size_t textlen = sizeof(text) / sizeof(text[0]);
int textpos                     = 0;
int scrollstep                  = 2;

void setup(void)
{
    M5.begin();
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_32);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString("Unit OLED Test", M5.Display.width() / 2, M5.Display.height() / 2);

    display.init();
    display.setRotation(1);
    canvas.setColorDepth(1);  // mono color
    canvas.setFont(&fonts::lgfxJapanMinchoP_28);
    canvas.setTextWrap(false);
    canvas.setTextSize(2);
    canvas.createSprite(display.width() + 64, 72);
}

void loop(void)
{
    int32_t cursor_x = canvas.getCursorX() - scrollstep;
    if (cursor_x <= 0) {
        textpos  = 0;
        cursor_x = display.width();
    }

    canvas.setCursor(cursor_x, 0);
    canvas.scroll(-scrollstep, 0);
    while (textpos < textlen && cursor_x <= display.width()) {
        canvas.print(text[textpos++]);
        cursor_x = canvas.getCursorX();
    }
    display.waitDisplay();
    canvas.pushSprite(&display, 0, (display.height() - canvas.height()) >> 1);
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/752/unit_oled_example_01.png" width="70%">


## 4.Hello World

使用 CoreS3 的 PORT.A 控制 Unit OLED 进行文字滚动显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/752/unit_oled_example_02.jpg" width="70%">
