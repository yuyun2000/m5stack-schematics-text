# CoreS3 microSD 卡

CoreS3 microSD 卡相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include <SPI.h>
#include <SD.h>
#include <M5Unified.h>

// ========== CoreS3 SD 卡正确引脚定义 ==========
#define SD_SPI_CS_PIN    4
#define SD_SPI_SCK_PIN  36
#define SD_SPI_MISO_PIN 35
#define SD_SPI_MOSI_PIN 37

void setup() {
  M5.begin();

  M5.Display.setFont(&fonts::FreeMono12pt7b);
  M5.Display.clear();

  // ========== SD 卡初始化（使用正确引脚）==========
  SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);

  if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {
    M5.Display.println("SD card not detected");
    while (1);
  } else {
    M5.Display.println("SD card detected");
  }
  delay(1000);

  // ========== 写入测试 ==========
  M5.Display.println("SD card write test...");
  auto file = SD.open("/WriteTest.txt", FILE_WRITE, true);
  if (file) {
    file.print("Hello, world! \nSD card write success! \n");
    file.close();
    M5.Display.println("SD card write success");
  } else {
    M5.Display.println("Failed to create TXT file");
  }
  delay(1000);

  // ========== 读取测试 ==========
  M5.Display.println("SD card read test...");

  if (SD.exists("/cores3_test_picture01.png")) {
    M5.Display.println("PNG file 01 detected");
  } else {
    M5.Display.println("PNG file 01 not detected");
  }

  if (SD.exists("/cores3_test_picture02.png")) {
    M5.Display.println("PNG file 02 detected");
  } else {
    M5.Display.println("PNG file 02 not detected");
  }
  delay(1000);
}

void loop() {
  M5.Display.drawPngFile(SD, "/cores3_test_picture01.png");
  delay(500);
  M5.Display.drawPngFile(SD, "/cores3_test_picture02.png");
  delay(500);
}
```

准备一张 microSD 卡，格式化为 FAT32 格式，在其根目录放入两张 320 \* 240 分辨率的 PNG 图片并命名为 cores3_test_picture01.png、cores3_test_picture02.png。你也可以直接下载 [cores3_test_picture01.png](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_test_picture01.png)、[cores3_test_picture02.png](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_test_picture02.png)。如果图片的分辨率不是 320\*240，则程序会根据预设来决定显示方式，可能会有显示异常。

将这张 SD 卡插入 CoreS3，注意 SD 卡的触点与 CoreS3 的屏幕朝同一方向。复制上面的代码到 Arduino IDE 中，编译并上传到 CoreS3。

该程序会在 SD 卡中创建文本文件 WriteTest.txt 并写入一段文本，然后循环播放 SD 卡中的两张 PNG 图片。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/arduino_cores3_sd_display_text.jpg" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/arduino_cores3_sd_display_picture1.jpg" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/arduino_cores3_sd_display_picture2.jpg" width="60%">

## API

CoreS3 microSD 卡部分使用了 Arduino 自带的 SD 库以及 M5GFX 库中的 drawPngFile，更多相关的 API 可以参考下方文档：

- [Arduino SD Doc](https://docs.arduino.cc/libraries/sd/)
- [Guide to Arduino & Secure Digital (SD) Storage](https://docs.arduino.cc/learn/programming/sd-guide/)
- [M5GFX API - drawPngFile](/zh_CN/arduino/m5gfx/m5gfx_image#drawpngfile)
