# ESP32-CAM

<span class="product-sku">SKU:U007</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/esp32cam/esp32cam_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/esp32cam/esp32cam_02.webp">
</PictureViewer>

## 描述

**ESP32CAM** 是一款图像识别开发板，集成 ESP32 (4M Flash + 520K RAM) 芯片和 2MP 的摄像头 (OV2640) . 支持 WiFi - 图像传输和 USB 端口调试.

硬件上预装固件，通过 ESP-IDF 编程开发，运行 WiFi - 相机应用程序。默认程序输出图像尺寸为**600 x 800**，你可以通过优化程序输出更大尺寸.

这个程序是如何使用的？

- 打开手机 Wi-Fi，扫描并连接名称以 "m5stack-" 开头的 AP 热点.
- 打开手机浏览器，访问<mark>192.168.4.1</mark>，进入监控页面实时获取拍摄视频.
- 视频帧率大约在每秒 5-6 帧.

因为模块可以生成 WIFI 热点 AP，所以可以用手机、PC 或其他设备通过 WIFI 无线获取摄像头图片，也可以通过模块的 HY2.0-4P 接口有线获取摄像头图片。

## 产品特性

- 基于 ESP32 设计
- CP2104 USB TTL
- 2MP 像素图像传感器
- 65° 视角

## 包装内容

- 1 x ESP32-CAM

## 规格参数

| 规格       | 参数                                                       |
| ---------- | ---------------------------------------------------------- |
| Flash      | 4MB                                                        |
| RAM        | 520KB                                                      |
| 图像传感器 | OV2640                                                     |
| 最大分辨率 | 2MP                                                        |
| 输出格式   | YUV (422/420) /YCbCr422，RGB565/555，8-bit compressed data |
| 产品尺寸   | 54.0 x 54.0 x 26.6mm                                       |
| 产品重量   | 5.0g                                                       |
| 包装尺寸   | 62.0 x 57.0 x 17.0mm                                       |
| 毛重       | 17.0g                                                      |

## 原理图

- [ESP32-CAM原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/esp32-cam/M5CAM-ESP32-A1-POWER.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_04.png">
</SchViewer>

## 管脚映射

### Camera

| 接口                 | OV2640 Pin | ESP32Cam   |
| -------------------- | ---------- | ---------- |
| SCCB Clock           | SIOC       | G23        |
| SCCB Data            | SIOD       | G25        |
| System Clock         | XCLK       | G27        |
| Vertical Sync        | VSYNC      | G22        |
| Horizontal Reference | HREF       | G26        |
| Pixel Clock          | PCLK       | G21        |
| Pixel Data Bit 0     | D2         | G17        |
| Pixel Data Bit 1     | D3         | G35        |
| Pixel Data Bit 2     | D4         | G34        |
| Pixel Data Bit 3     | D5         | G5         |
| Pixel Data Bit 4     | D6         | G39        |
| Pixel Data Bit 5     | D7         | G18        |
| Pixel Data Bit 6     | D8         | G36        |
| Pixel Data Bit 7     | D9         | G19        |
| Camera Reset         | RESET      | G15        |
| Camera Power Down    | PWDN       | see Note 1 |
| Power Supply 3.3V    | 3V3        | 3V3        |
| Ground               | GND        | GND        |

### HY2.0-4P 接口

| HY2.0-4P | ESP32Cam |
| -------- | -------- |
| SCL      | G4       |
| SDA      | G13      |
| 5V       | 5V       |
| GND      | GND      |

### LED

| LED     | ESP32Cam |
| ------- | -------- |
| LED_Pin | G16      |

### 预留芯片接口接口

| BME280 | ESP32Cam |
| ------ | -------- |
| SCL    | G4       |
| SDA    | G13      |

| MPU6050 | ESP32Cam |
| ------- | -------- |
| SCL     | G4       |
| SDA     | G13      |

| SPQ2410 | ESP32Cam |
| ------- | -------- |
| OUT     | G32      |

\#>OV2640 芯片的 **PIN8 (PDWN)**引脚为使能引脚，在该主板中通过 12KΩ 下拉电阻接地使能，进入工作模式。当 PIN8 (PDWN) 引脚上拉高电平时，将进入**Camera Power Down**模式.

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)

## 软件开发

### ESP-IDF

- [M5Stack-Camera](https://github.com/m5stack/M5Stack-Camera/tree/master/wifi/wifi_ap/firmware/ESP32-Camera)

### Arduino

- [ESP32-CAM Camera WebServer Exampler](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer)

### EasyLoader

| Easyloader                | 下载链接                                                                                                                   | 备注 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---- |
| ESP32-CAM Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/ESP32CAM/wifi_ap/EasyLoader__ESP32CAM_wifi_ap.exe) | /    |

## 相关视频

**ESP32CAM case-01**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201903/esp32cam_webcam_01.mp4" type="video/mp4">
</video>

**M5Camera 的应用 - 02**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/The%20M5Camera%20works.mp4" type="video/mp4">
</video>
