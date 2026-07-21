# Tough microSD 卡

Tough microSD 卡相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Tough
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <Arduino.h>
#include <SPI.h>
#include <SD.h>
#include <M5Unified.h>
#include <M5GFX.h>

#define SD_SPI_CS_PIN    4
#define SD_SPI_SCK_PIN  18
#define SD_SPI_MOSI_PIN 23
#define SD_SPI_MISO_PIN 38

void setup() {
  M5.begin();

  M5.Display.setRotation(1);
  M5.Display.setFont(&fonts::FreeMono12pt7b);

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

  // Write TXT file
  M5.Display.print("\n SD card write test...\n");
  auto file = SD.open("/WriteTest.txt", FILE_WRITE, true);
  if (file) {
    file.print("Hello, world! \nSD card write success! \n");
    file.close();
    M5.Display.print(" SD card write success\n");
  } else {
    M5.Display.print(" Failed to create TXT file\n");
  }
  delay(1000);

  M5.Display.print("\n SD card read test...\n");
  if (SD.open("/TestPicture01.png", FILE_READ, false)) {
    M5.Display.print(" PNG file 01 detected\n");
  } else {
    M5.Display.print(" PNG file 01 not detected\n");
  }
  if (SD.open("/TestPicture02.png", FILE_READ, false)) {
    M5.Display.print(" PNG file 02 detected\n");
  } else {
    M5.Display.print(" PNG file 02 not detected\n");
  }
  delay(1000);
}

void loop() {
  // Read PNG file and draw picture
  M5.Display.drawPngFile(SD, "/TestPicture01.png");
  delay(500);
  M5.Display.drawPngFile(SD, "/TestPicture02.png");
  delay(500);
}
```

准备一张 microSD 卡，格式化为 FAT32 格式，在其根目录放入两张 `320*240` 分辨率的 `PNG` 图片并命名为 `TestPicture01.png`、`TestPicture02.png`。（你也可以直接下载 [示例图片1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/TestPicture01.png)、[示例图片2](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/TestPicture02.png)。如果图片的分辨率不是 `320*240`，则程序会根据预设来决定显示方式，可能会有显示异常。）

如下图所示，用产品随附的 2.5mm 六角扳手松开背后的四个螺丝，打开盖子，右侧箭头所指即为 Tough 的 microSD 卡槽。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Insert_sd_card.png" width="90%">

将上述 SD 卡插入 Tough，注意 SD 卡的触点与 Tough 的屏幕朝同一方向。复制上面的代码到 Arduino IDE 中，编译并上传到 Tough。

该程序会在 SD 卡中创建文本文件 `WriteTest.txt` 并写入一段文本，然后循环播放 SD 卡中的两张 PNG 图片。

<!--
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_sdcard.gif" width="30%">
-->

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_sdcard.mp4" type="video/mp4"></video>

## API

Tough microSD 卡部分使用了 Arduino 自带的 `SD` 以及 `M5GFX` 库中的 `drawPngFile`，更多相关的API可以参考下方文档：

- [SD | Arduino Doc](https://docs.arduino.cc/libraries/sd/)
- [Guide to SD Storage | Arduino Doc](https://docs.arduino.cc/learn/programming/sd-guide/)
- [M5GFX API - drawPngFile](/zh_CN/arduino/m5gfx/m5gfx_functions#drawpngfile)