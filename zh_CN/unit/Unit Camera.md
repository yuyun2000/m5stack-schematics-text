# Unit Camera

<span class="product-sku">SKU:U109-B</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/10.webp">
</PictureViewer>

## 描述

**Unit Camera** 是 M5Stack 推出的一款高性价比 WiFi 摄像头，采用 ESP32-WROOM-32E 控制核心和 2 百万像素图像传感器 (OV2640) 方案，设计简洁，无多余外设。出厂软件集成了图像传输固件，提供图像数据获取和图像参数 ( 如白平衡、曝光、增益、尺寸等 ) 调整接口。用户可通过 UART 或 WiFi 直接获取图像数据并与摄像头交互。支持 UiFlow 图形化编程，用户无需开发即可实现开箱即用。此外，预留的程序下载接口使用户能够轻松更新或自定义固件，提升功能和性能。摄像头还配备了安装夹，方便用户将其固定在所需位置。其紧凑设计和高性价比适用于各种无线摄像头应用场景。

## 产品特性

- ESP32 控制核心
- 精简化设计
- 2MP 摄像头 (OV2640)
- UART 通信 (支持图像数据获取，图像参数调整等接口)
- WIFI 图像传输
- 可编程 LED 指示灯 (blue)
- 编程平台：ESP-IDF/Arduino/UiFlow

## 包装内容

- 1 x Unit Camera
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 摄像头背夹 (兼容乐高)

## 应用场景

- 家庭安防
- 智能家居
- 工业监控
- 农业监测
- 教育和研究
- 宠物监控

## 规格参数

| 规格            | 参数                                                                                                        |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| ESP32-WROOM-32E | 240MHz dual core，600 DMIPS，520KB SRAM，Wi-Fi                                                              |
| Flash           | 4MB                                                                                                         |
| 摄像头          | 焦距 4.8±5% mm<br/>光圈 2.4±5%<br/>镜头类型 1/4inch<br/>视场角 65°<br/>2MP<br/>畸变 <1%<br/>感光芯片 OV2640 |
| 支持输出格式    | YUV (422/420) / YCbCr422，8 位压缩数据，RGB565/555，8/10 位 Raw RGB 数据                                    |
| DFOV            | 65°                                                                                                         |
| 产品尺寸        | 40 x 24 x 11m                                                                                               |
| 包装尺寸        | 136 x 92 x 13mm                                                                                             |
| 产品重量        | 10.6g                                                                                                       |
| 毛重            | 15.7g                                                                                                       |

## 操作说明

> Unit Camera 并不包含程序下载电路，用户需要下载为 ESP32 更新程序时，可以通过外部连接 USB-TTL 下载器进行程序烧录。[点击此处购买ESP32下载板](https://shop.m5stack.com/products/esp32-downloader-kit)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/%E4%B8%8B%E8%BD%BD%E5%9B%BE.png" width="80%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_sch_01.webp" width="100%">

## 管脚映射

### OV2640

| 接口                 | Camera Pin | Unit Camera |
| -------------------- | ---------- | ----------- |
| SCCB Clock           | SIOC       | G23         |
| SCCB Data            | SIOD       | G25         |
| System Clock         | XCLK       | G27         |
| Vertical Sync        | VSYNC      | G22         |
| Horizontal Reference | HREF       | G26         |
| Pixel Clock          | PCLK       | G21         |
| Pixel Data Bit 0     | D0         | G32         |
| Pixel Data Bit 1     | D1         | G35         |
| Pixel Data Bit 2     | D2         | G34         |
| Pixel Data Bit 3     | D3         | G5          |
| Pixel Data Bit 4     | D4         | G39         |
| Pixel Data Bit 5     | D5         | G18         |
| Pixel Data Bit 6     | D6         | G36         |
| Pixel Data Bit 7     | D7         | G19         |
| Camera Reset         | RESET      | G15         |
| Camera Power Down    | PWDN       | -1          |
| Power Supply 3.3V    | 3V3        | 3V3         |
| Ground               | GND        | GND         |

### HY2.0-4P 接口

| HY2.0-4P | Unit Camera |
| -------- | ----------- |
| RX       | G16         |
| TX       | G17         |
| 5V       | 5V          |
| GND      | GND         |

### LED (blue)

| LED | Unit Camera |
| --- | ----------- |
| D1  | G4          |

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20Camera/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="80%">

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

## 产品对比

| 产品                | SKU    | 摄像头                                                 | 外壳                   |
| ------------------- | ------ | ------------------------------------------------------ | ---------------------- |
| Unit Camera         | U109-B | 常规视角 FOV:65°<br/>OV2640                            | 包含外壳以及摄像头背夹 |
| Unit CAM            | U109   | 常规视角 FOV:65°<br/>OV2640                            | 不包含外壳             |
| Unit Camera DIY KIT | U109-X | 常规视角 FOV:65°，OV2640<br/>广角鱼眼 FOV:160°，OV2640 | 包含外壳以及摄像头背夹 |

如需对比 Unit CAM 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unit_cam_compare?select=U109-B)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
