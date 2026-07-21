# CoreS3 输出图片

CoreS3 输出 microSD 卡图片文件的案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11
- M5GFX 库版本 >= 0.2.14

```cpp line-num
#include <Arduino.h>
#include <SPI.h>
#include <SD.h>
#include <M5Unified.h>
#include <M5GFX.h>

#define SD_SPI_CS_PIN   4
#define SD_SPI_SCK_PIN  36
#define SD_SPI_MISO_PIN 35
#define SD_SPI_MOSI_PIN 37

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
}

void loop() {
  // Read PNG file and draw picture
  M5.Display.drawPngFile(SD, "/TestPicture01.png");
  delay(1000);
  M5.Display.drawPngFile(SD, "/TestPicture02.png");
  delay(1000);
}
```
