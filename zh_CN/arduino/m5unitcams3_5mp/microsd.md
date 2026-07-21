# Unit CamS3-5MP microSD 卡

使用 Unit CamS3-5MP 拍摄照片并保存至 microSD 卡的案例程序。

## 案例程序

### 编译要求

?> 编译版本要求 | Unit CamS3-5MP 存在两种内置固件版本，使用前请参考 [Unit CamS3-5MP 快速上手](/zh_CN/arduino/m5unitcams3_5mp/program)，读取版本信息，并根据实际使用的版本，配置相应的编译环境。

设备上电前请插入 microSD 卡， 设备启动后将定时进行拍摄并保存至 microSD 卡，拍摄照片的命名将使用系统上电后的运行时间 (IMG\_{millis}.jpg)。设备重新上电后，同名图片将被覆盖。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/unit_cams3_5mp_microsd_demo_01.jpg" width="70%">

```cpp line-num
#include <WiFi.h>
#include "esp_camera.h"
#include "FS.h"
#include "SD.h"
#include "SPI.h"

#define SD_SPI_CS_PIN    9
#define SD_SPI_MOSI_PIN 38
#define SD_SPI_SCK_PIN  39
#define SD_SPI_MISO_PIN 40

#define CAPTURE_INTERVAL 15000

#define PWDN_GPIO_NUM  -1
#define RESET_GPIO_NUM 21
#define XCLK_GPIO_NUM  11
#define SIOD_GPIO_NUM  17
#define SIOC_GPIO_NUM  41

#define Y9_GPIO_NUM    13
#define Y8_GPIO_NUM    4
#define Y7_GPIO_NUM    10
#define Y6_GPIO_NUM    5
#define Y5_GPIO_NUM    7
#define Y4_GPIO_NUM    16
#define Y3_GPIO_NUM    15
#define Y2_GPIO_NUM    6
#define VSYNC_GPIO_NUM 42
#define HREF_GPIO_NUM  18
#define PCLK_GPIO_NUM  12
#define LED_GPIO_NUM   14

unsigned long lastCaptureTime = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Camera + SD Card Capture Demo");

  SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
  if (!SD.begin(SD_SPI_CS_PIN, SPI, 40000000)) {
    Serial.println("SD Card Mount Failed");
    return;
  }

  uint8_t cardType = SD.cardType();
  if (cardType == CARD_NONE) {
    Serial.println("No SD card attached");
    return;
  }
  Serial.println("SD Card initialized.");

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer   = LEDC_TIMER_0;
  config.pin_d0       = Y2_GPIO_NUM;
  config.pin_d1       = Y3_GPIO_NUM;
  config.pin_d2       = Y4_GPIO_NUM;
  config.pin_d3       = Y5_GPIO_NUM;
  config.pin_d4       = Y6_GPIO_NUM;
  config.pin_d5       = Y7_GPIO_NUM;
  config.pin_d6       = Y8_GPIO_NUM;
  config.pin_d7       = Y9_GPIO_NUM;
  config.pin_xclk     = XCLK_GPIO_NUM;
  config.pin_pclk     = PCLK_GPIO_NUM;
  config.pin_vsync    = VSYNC_GPIO_NUM;
  config.pin_href     = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn     = PWDN_GPIO_NUM;
  config.pin_reset    = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size   = FRAMESIZE_5MP;
  config.fb_location  = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 63;
  config.fb_count     = 1;
  config.grab_mode    = CAMERA_GRAB_WHEN_EMPTY;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x\n", err);
    return;
  }

  Serial.println("Camera initialized.");
}

void loop() {
  unsigned long now = millis();
  if (now - lastCaptureTime >= CAPTURE_INTERVAL) {
    lastCaptureTime = now;

    camera_fb_t* fb = esp_camera_fb_get();
    if (!fb) {
      Serial.println("Camera capture failed");
      return;
    }

    String path = "/IMG_" + String(millis()) + ".jpg";
    File file = SD.open(path.c_str(), FILE_WRITE);
    if (!file) {
      Serial.println("Failed to open file for writing");
    } else {
      file.write(fb->buf, fb->len);
      file.close();
      Serial.printf("Saved file: %s, size: %d bytes\n", path.c_str(), fb->len);
    }

    esp_camera_fb_return(fb);
  }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/unit_cams3_5mp_microsd_demo_02.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/unit_cams3_5mp_microsd_demo_03.png" width="70%">

## API

Unit CamS3-5MP microSD 卡部分使用了 Arduino 自带的 `SD`，更多相关的 API 可以参考下方文档：

- [SD | Arduino Doc](https://docs.arduino.cc/libraries/sd/)
- [Guide to SD Storage | Arduino Doc](https://docs.arduino.cc/learn/programming/sd-guide/)
