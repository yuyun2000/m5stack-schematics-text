# Unit CAM

<span class="product-sku">SKU:U109</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_07.webp">
</PictureViewer>

## 描述

**Unit CAM** 是 M5 推出的一款极具性价比的 WiFi 摄像头，硬件上使用 ESP32-WROOM-32E 控制核心 + 2 MegaPixel 图像传感器 (OV2640) 方案，采用最精简化设计，无多余外设。出厂软件集成图像传输固件，提供图像数据获取，图像参数 ( 白平衡，曝光，增益，尺寸等属性 ) 调整等调用接口，用户可以通过 UART 或是 WiFi 的形式直接获取图像数据，与摄像头进行交互。支持 UiFlow 图形化编程调用，实现零开发，开箱即用的用户体验。紧凑的设计与性价比适用于各种无线摄像头应用场景。

## 产品特性

- 精简化设计
- ESP32 控制核心
- 2MP 摄像头 (OV2640)
- UART 通信 (支持图像数据获取，图像参数调整等接口)
- WIFI 图像传输
- 可编程 LED 指示灯 (blue)
- 编程平台：ESP-IDF/Arduino/UiFlow

## 包装内容

- 1 x Unit CAM

## 应用场景

- WiFi 摄像头
- 远程监控

## 规格参数

| 规格                          | 参数                                                                     |
| ----------------------------- | ------------------------------------------------------------------------ |
| Flash                         | 4M                                                                       |
| 固件默认通信方式              | UART: 115200bps 8N1                                                      |
| 图像传感器                    | OV2640                                                                   |
| 最大分辨率                    | 2MP                                                                      |
| Unit CAM 固件默认图片传输速率 | 12fps                                                                    |
| OV2640 支持输出格式           | YUV (422/420) / YCbCr422，8 位压缩数据，RGB565/555，8/10 位 Raw RGB 数据 |
| DFOV                          | 66.5°                                                                    |
| 产品重量                      | 4.7g                                                                     |
| 毛重                          | 5.3g                                                                     |
| 产品尺寸                      | 45 x 20 x 12mm                                                           |
| 包装尺寸                      | 60 x 60 x 15mm                                                           |

## 操作说明

> Unit CAM 并不包含程序下载电路，用户需要下载为 ESP32 更新程序时，可以通过外部连接 USB-TTL 下载器进行程序烧录。[点击此处购买ESP32下载板](https://shop.m5stack.com/products/esp32-downloader-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_04.webp">

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_08.webp" width="70%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_sch_01.webp" width="80%">

## 管脚映射

### Camera

| 接口                 | Camera Pin | Unit CAM |
| -------------------- | ---------- | -------- |
| SCCB Clock           | SIOC       | G23      |
| SCCB Data            | SIOD       | G25      |
| System Clock         | XCLK       | G27      |
| Vertical Sync        | VSYNC      | G22      |
| Horizontal Reference | HREF       | G26      |
| Pixel Clock          | PCLK       | G21      |
| Pixel Data Bit 0     | D0         | G32      |
| Pixel Data Bit 1     | D1         | G35      |
| Pixel Data Bit 2     | D2         | G34      |
| Pixel Data Bit 3     | D3         | G5       |
| Pixel Data Bit 4     | D4         | G39      |
| Pixel Data Bit 5     | D5         | G18      |
| Pixel Data Bit 6     | D6         | G36      |
| Pixel Data Bit 7     | D7         | G19      |
| Camera Reset         | RESET      | G15      |
| Camera Power Down    | PWDN       | -1       |
| Power Supply 3.3V    | 3V3        | 3V3      |
| Ground               | GND        | GND      |

### HY2.0-4P 接口

| HY2.0-4P | Unit CAM |
| -------- | -------- |
| RX       | G16      |
| TX       | G17      |
| 5V       | 5V       |
| GND      | GND      |

### LED (blue)

| LED | Unit CAM |
| --- | -------- |
| D1  | G4       |

## 数据手册

- [ESP32-WROOM-32E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/unit_cam/ESP32-WROOM-32E-EN.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)

## 软件开发

### 快速上手

- [Camera-Tool](/zh_CN/guide/wifi_camera/timer_cam/cameratool)
- [UART 传输 / Timer 定时拍摄](/zh_CN/guide/wifi_camera/timer_cam/uiflow)

### Arduino

?> 使用说明:| 该案例程序适用于 M5Core，用于通过 UART 接收来自 Unit Camera 的图像，请勿烧录至 Unit Camera。

- [Camera UART to Core](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/UNIT_CAM/CAM2CORE)

### ESP IDF

- [AWS-S3-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/AWS-S3-PUT)
- [Ali-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Ali-OSS)
- [SMB-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/SMB-PUT)
- [Timer Wakeup](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Wake-up)
- [HTTP Stream](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/http-stream)
- [Wireless-send](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/wireless-send)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UnitCAM.mp4" type="video/mp4">
</video>

## 产品对比

如需对比 Unit CAM 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unit_cam_compare?select=U109)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
