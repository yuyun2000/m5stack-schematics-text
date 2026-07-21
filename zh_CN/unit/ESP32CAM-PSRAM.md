# ESP32-CAM PSRAM

<span class="product-sku">SKU:U017-PCBA</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_01.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_02.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_03.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_04.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_05.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_06.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_07.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_08.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/ESP32CAM-PSRAM_09.webp">
</PictureViewer>

## 描述

**ESP32CAM-PSRAM**是一款鱼眼广角图像识别开发板，视场角为 150°，集成 ESP32 (4MB Flash + 520KB RAM + 4MB PSRAM) 芯片和 2MP 的摄像头 (OV2640) . 支持 WiFi 图像传输和 USB 端口调试.

硬件上预装固件，通过 ESP-IDF 编程开发，运行 WiFi 相机应用程序。默认程序输出图像尺寸为**600 x 800**，你可以通过优化程序输出更大尺寸.

使用流程：

- 打开手机 Wi-Fi，扫描并连接名称以 "m5stack-" 开头的 AP 热点.
- 打开手机浏览器，访问<mark>192.168.4.1</mark>，进入监控页面实时获取拍摄视频.
- 视频帧率大约在每秒 5-6 帧.

因为开发板可以生成 WIFI 热点 AP，所以可以用手机、PC 或其他设备通过 WIFI 无线获取摄像头图片，也可以通过开发板的 HY2.0-4P 接口有线获取摄像头图片。

## 产品特性

- 基于 ESP32 设计
- WIFI 图像传输
- CP2104 USB TTL
- 广角镜头 150°
- OV2640 视觉传感器

## 包装内容

- 1 x ESP32-CAM PSRAM
- 1 x 摄像头 (OV2640)

## 应用

- DIY 制作
- 延时摄影
- 物联网监控

## 规格参数

| 规格       | 参数                                                                     |
| ---------- | ------------------------------------------------------------------------ |
| Flash/RAM  | 4MB/500KB                                                                |
| PSRAM      | 4MB PSRAM                                                                |
| 图像传感器 | OV2640                                                                   |
| 最大分辨率 | 2MP                                                                      |
| 输出格式   | YUV (422/420) /YCbCr422，8 位压缩数据，RGB565/555，8-/10 位 Raw RGB 数据 |
| 视角       | 150°                                                                     |
| CCD 尺寸   | 1/4 inch                                                                 |
| 产品尺寸   | 47 x 20 x 10mm                                                           |
| 包装尺寸   | 136 x 92 x 13mm                                                          |
| 产品重量   | 9.4g                                                                     |
| 毛重       | 11.8g                                                                    |

## 原理图

### 电源电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp" width="80%">

### 芯片外围电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp" width="80%">

### USB 转串口电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp">

## 管脚映射

### Camera

| 接口                 | Camera Pin | ESP32CAM-PSRAM |
| -------------------- | ---------- | -------------- |
| SCCB Clock           | SIOC       | G23            |
| SCCB Data            | SIOD       | G22            |
| System Clock         | XCLK       | G27            |
| Vertical Sync        | VSYNC      | G25            |
| Horizontal Reference | HREF       | G26            |
| Pixel Clock          | PCLK       | G21            |
| Pixel Data Bit 0     | D2         | G32            |
| Pixel Data Bit 1     | D3         | G35            |
| Pixel Data Bit 2     | D4         | G34            |
| Pixel Data Bit 3     | D5         | G5             |
| Pixel Data Bit 4     | D6         | G39            |
| Pixel Data Bit 5     | D7         | G18            |
| Pixel Data Bit 6     | D8         | G36            |
| Pixel Data Bit 7     | D9         | G19            |
| Camera Reset         | RESET      | G15            |
| Camera Power Down    | PWDN       | see Note 1     |
| Power Supply 3.3V    | 3V3        | 3V3            |
| Ground               | GND        | GND            |

### HY2.0-4P 接口

| HY2.0-4P | ESP32CAM-PSRAM |
| -------- | -------------- |
| SCL      | G13            |
| SDA      | G4             |
| 5V       | 5V             |
| GND      | GND            |

### LED

| LED     | ESP32CAM-PSRAM |
| ------- | -------------- |
| LED_Pin | G14            |

\#>OV2640 芯片的 **PIN8 (PDWN)**引脚为使能引脚，在该主板中通过 12KΩ 下拉电阻接地使能，进入工作模式。当 PIN8 (PDWN) 引脚上拉高电平时，将进入**Camera Power Down**模式.

## 尺寸图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ESP32CAM-PSRAM/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)

## 软件开发

### ESP-IDF

- [M5Stack-Camera](https://github.com/m5stack/M5Stack-Camera/tree/master/wifi/wifi_ap/firmware/M5CameraF)

### Arduino

- [ESP32-CAM PSRAM Camera WebServer Example](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                        | 备注 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---- |
| ESP32-CAM PSRAM Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/M5-Camera-F/wifi_ap/EasyLoader_M5-Camera-F_wifi_ap.exe) | /    |

## 产品对比

<a href="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/Product_compared.pdf">查看 M5 摄像头系列 / 产品区别</a>
