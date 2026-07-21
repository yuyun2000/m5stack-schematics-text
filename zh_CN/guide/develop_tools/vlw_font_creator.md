# vlw Font Creator

vlw Font Creator 是一款在线 vlw 字体生成器，用于生成自定义像素大小和字库范围的 vlw 字体文件，方便开发者拓展显示字体样式和节约字体内存占用。

## 1. 创建 vlw 字体

访问<https://vlw-font-creator.m5stack.com/>, 根据下图提示完成 vlw 字体创建。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/develop_tools/vlw_font_creator/vlw_font_creator_cn_01.jpg" width="100%">

## 2. 使用 vlw 字体

参考以下案例程序，引用 vlw 字体文件到你的项目中。

1. `采用芯片内存存储vlw字体文件`

- [Arduino - M5GFX vlw Font](https://github.com/m5stack/M5GFX/tree/master/examples/Basic/VlwFont)

2. `采用microSD存储vlw字体文件`

```cpp line-num
#include <Arduino.h>
#include <SPI.h>
#include <SD.h>
#include <M5Unified.h>
#include <M5GFX.h>

#define SD_SPI_CS_PIN   4
#define SD_SPI_SCK_PIN  18
#define SD_SPI_MISO_PIN 19
#define SD_SPI_MOSI_PIN 23

void setup() {
  M5.begin();

  M5.Display.setTextFont(&fonts::Orbitron_Light_24);
  M5.Display.setTextSize(1);

  // SD Card Initialization
  SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
  if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {
    // Print a message if SD card initialization failed or if the SD card does not exist.
    M5.Display.print("\n SD card not detected\n");
    while (1)
      ;
  } else {
    M5.Display.print("\n SD card detected\n");
  }
  delay(1000);
  delay(1000);

  M5.Display.print("\n SD card read test...\n");
  if (SD.open("/Test.vlw", FILE_READ, false)) {
    M5.Display.print(" vlw detected\n");
  } else {
    M5.Display.print(" vlw not detected\n");
  }

  if (M5.Display.loadFont(SD, "/Test.vlw")) {
    M5.Display.print("\n↑↓←→☺\n");// Display some characters to test the font
  } else {
    M5.Display.print(" vlw not loaded\n");
  }
}

void loop() {
}
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/659/vlw_font_creator.jpg" width="50%">
