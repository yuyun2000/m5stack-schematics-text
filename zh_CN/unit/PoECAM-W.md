# Unit PoE CAM-W

<span class="product-sku">SKU:U121-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-0e65978b-b66f-41ea-a94f-e0be885ce076.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-35c1d0e2-7c00-45ab-809e-96c0bc0e0e1f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-ee21415b-f502-4588-b813-1b13d6c37e50.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-0e946d46-3d6a-45db-8754-1c7077152739.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-2753f4ab-f8dc-4117-b82a-e7ca59f3bafd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-c8a15ca9-1aec-4a65-b0e5-db4456c42b21.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-dc238aac-c353-455f-9bf8-65c9ec2a3550.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-0576a55d-fbda-4116-a613-22e66348fbcf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-763047bb-f767-465f-b8e8-90e569a02223.webp">
</PictureViewer>

## 描述

**Unit PoE CAM-W** 是一款基于 “ESP32 + W5500” 方案的可编程 PoE 摄像机。它集成了 PoE 以太网通信及网线供电功能，同时具备 Wi-Fi 功能，内置 2MP 图像传感器 OV2640。该产品适用于图像监控、远程采集以及设备按 PoE 布线的场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5poe_cam/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit PoE CAM-W 设备。 |

## 产品特性

- 内置 ESP32 MCU (支持 WiFi)
- 2MP 摄像头 0V2640
- 以太网芯片 W5500
- LAN 的速率可达 10M 或 100M (根据具体提供的线路而定)
- PoE IEEE802.3 AF 规范 (最大功率 6w)
- 内置提示 LED 灯
- 开发平台：Arduino、ESP-IDF
- 以太网标准接口 RJ45
- 标准 LEGO 接口和相机支架

## 包装内容

- 1 x Unit PoE CAM-W
- 1 x 相机安装夹
- 1 x LEGO 兼容夹

## 应用场景

- 仓库监控
- 定时拍摄
- 机器视觉
- 家庭智能监控

## 规格参数

| 规格                 | 参数                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| MCU                  | ESP32-D0WDQ6-V3                                                                                        |
| 摄像头模块           | OV2640                                                                                                 |
| 以太网芯片           | W5500                                                                                                  |
| Flash                | 16MB                                                                                                   |
| PSRAM                | 8MB                                                                                                    |
| 像素尺寸             | 2.2 µm x 2.2 µm                                                                                        |
| 输出格式 (8 位)      | YUV (422/420) /YCbCr422，RGB565/555，8-bit compressed data，8-/10-bit Raw RGB data                     |
| 自动图像控制功能     | 自动曝光控制 (AEC)，自动增益控制 (AGC)，自动白平衡 (AWB)，自动带带滤波器 (ABF) 和自动黑电平校准 (ABLC) |
| DFOV                 | 65°                                                                                                    |
| 支持连接 TCP/IP 协议 | TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE                                                                 |
| 以太网接口规格       | RJ45                                                                                                   |
| 最大功率             | 6W                                                                                                     |
| 产品尺寸             | 64 × 24 × 18mm                                                                                         |
| 包装尺寸             | 80 × 37 × 32mm                                                                                         |
| 产品重量             | 38g                                                                                                    |
| 毛重                 | 45g                                                                                                    |

### 操作说明

?> 使用注意事项 | 摄像头长时间连续获取高分辨率的图像流，可能会导致设备过热，成像颜色异常。长时间工作情况，建议额外提供散热。

\#> 备注: | `PoECAM 下载程序时，您需要连接外部 ESP32 烧录器`，您可以[点击这里购买 M5 官方的 ESP32-下载器套件，其中包括一个便于连接的传输板](https://shop.m5stack.com/products/esp32-downloader-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_04.webp" width="100%" height="30%">

## 原理图

- [Unit PoE CAM-W原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/PoECAM-W/Sch_M5PoECAM-W.pdf)

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-a9008619-1734-458f-81f1-8be6f4e68441.webp" width="100%" />

## 管脚映射

### OV2640

| 接口                 | Camera Pin | PoE CAM |
| -------------------- | ---------- | ------- |
| SCCB Clock           | SIOC       | G12     |
| SCCB Data            | SIOD       | G14     |
| System Clock         | XCLK       | G27     |
| Vertical Sync        | VSYNC      | G22     |
| Horizontal Reference | HREF       | G26     |
| Pixel Clock          | PCLK       | G21     |
| Pixel Data Bit 0     | D0         | G32     |
| Pixel Data Bit 1     | D1         | G35     |
| Pixel Data Bit 2     | D2         | G34     |
| Pixel Data Bit 3     | D3         | G5      |
| Pixel Data Bit 4     | D4         | G39     |
| Pixel Data Bit 5     | D5         | G18     |
| Pixel Data Bit 6     | D6         | G36     |
| Pixel Data Bit 7     | D7         | G19     |
| Camera Reset         | RESET      | G15     |
| Camera Power Down    | PWDN       | -1      |
| Power Supply 3.3V    | 3V3        | 3V3     |
| Ground               | GND        | GND     |

### W5500

| W5500 | PoE CAM |
| ----- | ------- |
| MOSI  | G13     |
| MISO  | G38     |
| SCLK  | G23     |
| CS    | G4      |

### EXT.PORT

| EXT.PORT | PoE CAM |
| -------- | ------- |
| RX       | G25     |
| TX       | G33     |
| 5V       | 5V      |
| GND      | GND     |

### 右侧按键

| Button | PoE CAM |
| ------ | ------- |
| Signal | G37     |

### 蓝色指示灯

| Blue LED | PoE CAM |
| -------- | ------- |
| Signal   | G0      |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/PoECAM-W/img-047019da-7c82-4641-8769-392f845222f4.png" width="100%" />

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)
- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)
- [Easyloader](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/PoECAM-W/PoECAM.exe)
- [PoECAM-W PinMap](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/PinMap/PoECAM-W%20PinMap.pdf)

## 软件开发

### Arduino

- [Unit PoE CAM-W Arduino 快速上手](/zh_CN/arduino/m5poe_cam/program)
- [Unit PoE CAM-W Arduino 驱动库](https://github.com/m5stack/PoE_CAM)
- [Unit PoE CAM-W Button Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/button)
- [Unit PoE CAM-W Capture Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/capture)
- [Unit PoE CAM-W HTTP POST Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/http_post)
- [Unit PoE CAM-W LED Control Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/led)
- [Unit PoE CAM-W RTSP Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/rtsp_stream)
- [Unit PoE CAM-W Web CAM Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/web_cam)

### EasyLoader

| Easyloader                     | 下载链接                                                                                                      | 备注 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---- |
| Unit PoE CAM-W Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/PoECAM-W/POE%20CAM-W.exe) | /    |

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/PoECAM_VIDEO.mp4" type="video/mp4">
</video>
