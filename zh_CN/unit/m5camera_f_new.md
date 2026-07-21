# M5Camera-F New

<span class="product-sku">SKU:U037</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/m5camera_f_new/m5camera_f_new_06.webp">
</PictureViewer>

## 描述

**M5Camera-F New** 是一款鱼眼广角图像识别开发板，视场角为 150°。集成 ESP32 (4M Flash + 520K RAM + 4M PSRAM) 芯片和 2MP 的摄像头 ( OV2640 )。支持 WiFi 图像传输和 USB 端口调试。

硬件上预装固件，通过 ESP-IDF 编程开发，运行 WiFi - 相机应用程序。默认程序输出图像尺寸为 **600 x 800**，你可以通过优化程序输出更大尺寸。

这个程序是如何使用的？

- 打开手机 Wi-Fi，扫描并连接名称以 "m5stack-" 开头的 AP 热点.
- 打开手机浏览器，访问<mark>192.168.4.1</mark>，进入监控页面实时获取拍摄视频.
- 视频帧率大约在每秒 5-6 帧.

因为模块可以生成 WIFI 热点 AP，所以可以用手机、PC 或其他设备通过 WIFI 无线获取摄像头图片，也可以通过模块的 HY2.0-4P 接口有线获取摄像头图片。

## 产品特性

- 基于 ESP32 设计
- WIFI 图像传输
- CP2104 USB TTL
- 广角镜头 150°
- OV2640 视觉传感器

## 包装内容

- 1 x M5Camera-F New
- 1 x LEGO 适配背夹
- 1 x Wall/1515
- 1 x USB Type-C 连接线 (20cm)

## 规格参数

| 规格       | 参数                                                                     |
| ---------- | ------------------------------------------------------------------------ |
| Flash      | 4M                                                                       |
| RAM        | 4MB                                                                      |
| 图像传感器 | OV2640                                                                   |
| 最大分辨率 | 2MP                                                                      |
| 输出格式   | YUV (422/420) /YCbCr422，8 位压缩数据，RGB565/555，8-/10 位 Raw RGB 数据 |
| 视角       | 150°                                                                     |
| CCD 尺寸   | 1/4 inch                                                                 |
| 产品重量   | 17g                                                                      |
| 毛重       | 41g                                                                      |
| 产品尺寸   | 24 x 48 x 19mm                                                           |
| 包装尺寸   | 75 x 45 x 30mm                                                           |

## 原理图

### 电源电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp" width="80%">

### 芯片外围电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp" width="80%">

### USB 转串口电路

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp">

## 管脚映射

### Camera

| 接口                 | Camera Pin | M5CameraF  |
| -------------------- | ---------- | ---------- |
| SCCB Clock           | SIOC       | IO23       |
| SCCB Data            | SIOD       | IO22       |
| System Clock         | XCLK       | IO27       |
| Vertical Sync        | VSYNC      | IO25       |
| Horizontal Reference | HREF       | IO26       |
| Pixel Clock          | PCLK       | IO21       |
| Pixel Data Bit 0     | D2         | IO32       |
| Pixel Data Bit 1     | D3         | IO35       |
| Pixel Data Bit 2     | D4         | IO34       |
| Pixel Data Bit 3     | D5         | IO5        |
| Pixel Data Bit 4     | D6         | IO39       |
| Pixel Data Bit 5     | D7         | IO18       |
| Pixel Data Bit 6     | D8         | IO36       |
| Pixel Data Bit 7     | D9         | IO19       |
| Camera Reset         | RESET      | IO15       |
| Camera Power Down    | PWDN       | see Note 1 |
| Power Supply 3.3V    | 3V3        | 3V3        |
| Ground               | GND        | GND        |

### HY2.0-4P 接口

| HY2.0-4P | M5CameraF |
| -------- | --------- |
| SCL      | G4        |
| SDA      | G13       |
| 5V       | 5V        |
| GND      | GND       |

### LED

| LED     | M5Camera |
| ------- | -------- |
| LED_Pin | IO14     |

\#>OV2640 芯片的 **PIN8 (PDWN)**引脚为使能引脚，在该主板中通过 12KΩ 下拉电阻接地使能，进入工作模式。当 PIN8 (PDWN) 引脚上拉高电平时，将进入**Camera Power Down**模式。

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)

## 软件开发

### Arduino

- [M5Camera-Arduino](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/Camera/CameraWebServer)

### ESP-IDF

- [M5Stack-Camera](https://github.com/m5stack/M5Stack-Camera)
- [M5CameraF 固件](https://github.com/m5stack/M5Stack-Camera/tree/master/wifi/wifi_ap/firmware/M5CameraF)
- [串口通信-M5CameraF](https://github.com/m5stack/M5Stack-Camera/tree/master/uart/firmware/M5CameraF)\*\*
- [串口通信-M5Core](https://github.com/m5stack/M5Stack-Camera/tree/master/uart/arduino)
- [QRcode识别](https://github.com/m5stack/M5Stack-Camera/tree/master/qr/firmware/M5CameraF)
- [MPU6050](https://github.com/m5stack/M5Stack-Camera/tree/master/mpu6050/firmware/M5CameraF)

### EasyLoader

| Easyloader                            | 下载链接                                                                                                                        | 备注 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---- |
| M5Camera-F New AP Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/M5-Camera-F/wifi_ap/EasyLoader_M5-Camera-F_wifi_ap.exe) | /    |

## 产品对比

- [查看M5摄像头系列/产品区别](https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/Product_compared.pdf)
