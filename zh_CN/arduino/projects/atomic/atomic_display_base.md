# Atomic Display Base Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置：参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库：

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 3\. 使用到的硬件产品：
  - [AtomS3R](https://shop.m5stack.com/products/atoms3r-dev-kit)
  - [Atomic Display Base](https://shop.m5stack.com/products/atomic-display-base-gw1nr)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/3.webp" width="20%">

## 2. 案例程序

参考[M5Unified库](https://github.com/m5stack/M5Unified)中的[`Displays`示例程序](https://github.com/m5stack/M5Unified/blob/master/examples/Basic/Displays/Displays.ino)，根据本教程实际使用的设备修改了示例程序中相应的配置选项。你可以根据要使用的外接显示器分辨率修改程序中的 13、14 行。

\#> 显示器兼容性 | Atomic Display Base 需搭配具备自适应分辨率缩放功能的显示器，在一些不支持自适应分辨率的显示器上可能会出现显示异常现象。

```cpp line-num
#include <Arduino.h>
#include <M5AtomDisplay.h>
#include <M5Unified.h>

void setup() {
  auto cfg = M5.config();

  // external display setting. (Pre-include required)
  cfg.external_display.atom_display = true;  // default=true. use AtomDisplay

  // Set individual parameters for external displays.
  // (※ Use only the items you wish to change. Basically, it can be omitted.)
  cfg.atom_display.logical_width = 1920;
  cfg.atom_display.logical_height = 1200;
  // cfg.atom_display.output_width   = 1920;
  // cfg.atom_display.output_height  = 1080;
  // cfg.atom_display.refresh_rate   = 60;
  // cfg.atom_display.scale_w        = 2;
  // cfg.atom_display.scale_h        = 2;
  // cfg.atom_display.pixel_clock    = 74250000;

  // begin M5Unified.
  M5.begin(cfg);

  // Get the number of available displays
  int display_count = M5.getDisplayCount();

  for (int i = 0; i < display_count; ++i) {
    // All displays are available in M5.Displays.
    // ※ Note that the order of which displays are numbered is the order in which they are detected, so the order may change.

    M5.Displays(i).clear();
    int textsize = M5.Displays(i).height() / 120;
    if (textsize < 5) { textsize = 3; }
    M5.Displays(i).setTextSize(textsize);
    M5.Displays(i).printf("\n\nNo.%d\n\n", i);
  }

  // If an external display is to be used as the main display, it can be listed in order of priority.
  M5.setPrimaryDisplayType({
    m5::board_t::board_M5AtomDisplay,
    // m5::board_t::board_M5ModuleDisplay,
  });

  // The primary display can be used with M5.Display.
  M5.Display.print("primary display\n\n");

  // Examine the indexes of a given type of display
  int index_atom_display = M5.getDisplayIndex(m5::board_t::board_M5AtomDisplay);

  if (index_atom_display >= 0) {
    M5.Displays(index_atom_display).print("This is Atom Display\n");
  }

  M5.delay(2500);
}

void loop() {
  M5.delay(100);

  int x = rand() % M5.Displays(0).width();
  int y = rand() % M5.Displays(0).height();
  int r = (M5.Displays(0).width() >> 2) + 2;
  uint16_t c = rand();
  M5.Displays(0).fillCircle(x, y, r, c);

  draw_function(&M5.Displays(1));
}

// When creating a function for drawing, it can be used universally by accepting a LovyanGFX type as an argument.
void draw_function(LovyanGFX* gfx) {
  int x = rand() % gfx->width();
  int y = rand() % gfx->height();
  int r = (gfx->width() >> 6) + 2;
  uint16_t c = rand();
  gfx->fillRect(x - r, y - r, r * 2, r * 2, c);
}
```

## 3. 编译上传

- 1\. 下载模式：主控设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- AtomS3R 长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角的编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/AtomicDisplayBase_Arduino_01.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/AtomicDisplayBase_Arduino_02.png" width="70%">

## 4. 开始运行

将 AtomS3R、Atomic Display Base 组合起来，并通过高清视频扩展接口连接至显示器后，短按一次复位按钮。AtomS3R 自带屏幕上会出现许多彩色圆圈，而外接屏幕上会出现许多彩色方块。效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/AtomicDisplayBase_Arduino_2.gif" width="100%">

<!--
<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/AtomicDisplayBase_Arduino_2.mp4" type="video/mp4"></video>
-->
