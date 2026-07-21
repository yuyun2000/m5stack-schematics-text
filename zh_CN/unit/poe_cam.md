# Unit PoE CAM

<span class="product-sku">SKU:U121</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_010.webp">
</PictureViewer>

## 描述

**Unit PoE CAM** 是一款集成 **PoE** (Power Over Ethernet) 功能的开源 **可编程网络摄像头**。硬件采用 **ESP32** 控制核心 + **W5500 嵌入式以太网控制器** + 2M 像素图像传感器 **OV2640** 方案，并搭配 **8MB PSRAM** + **16MB Flash** 的大内存组合。

该摄像头整机体积紧凑，供电方式灵活，仅需连接网线两步，即可实现稳定的图像传输，非常适用于仓储监控、定时图像采集等应用场景，其特点如下：

- **即插即用**：
  - 接入网线后可自动获取 IP，同一局域网内的任意设备都能获取摄像头图像。
  - 出厂软件集成图像传输固件，不仅提供图像数据获取功能，还设有图像参数（如白平衡、曝光、增益、尺寸等属性）调整的调用接口。
  - 配套 PC 端上位机 **CameraTool** 以及支持 UART 图像传输。
- **功能丰富**：
  - 内嵌 ESP32 并预留程序烧录接口，为二次开发提供支持。
  - W5500 嵌入式以太网控制器支持 **TCP、UDP、IPv4、ICMP、ARP、IGMP 和 PPPoE 协议**。
  - 支持输出多种格式的图像数据，且能对图像参数进行调节。
- **高灵活性**：
  - 支持 **PoE** 供电，实现网线与电源二合一，接线更为简洁；同时也支持 5V 供电。
  - 配备 GROVE 拓展接口。
  - 带有摄像头固定背夹，既支持壁挂，也支持吊装。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5poe_cam/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit PoE CAM 设备。 |

## 产品特性

- 丰富的图像处理 API 接口
- PoE IEEE802.3 AF 规范
- Ethernet 网络摄像头
- 内置 ESP32 MCU
- 开发平台:
  - UiFlow，Arduino，ESP-IDF
  - 软件代码 / 硬件开源

## 包装内容

- 1 x Unit PoE CAM
- 1 x 摄像头固定背夹
- 1 x LEGO 兼容背夹

## 应用场景

- 仓储监控
- 定时拍摄

## 规格参数

| 规格                        | 参数                                                                     |
| --------------------------- | ------------------------------------------------------------------------ |
| SoC                         | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                                  |
| DMIPS                       | 600                                                                      |
| SRAM                        | 520KB                                                                    |
| Flash                       | 16MB                                                                     |
| PSRAM                       | 8MB                                                                      |
| Wi-Fi                       | 2.4 GHz Wi-Fi                                                            |
| 图像传感器                  | OV2640                                                                   |
| 最大分辨率                  | 2MegaPixel                                                               |
| OV2640 支持最大图像传输速率 | YUV (422/420) /YCbCr422，8 位压缩数据，RGB565/555，8-/10 位 Raw RGB 数据 |
| DFOV                        | 65°                                                                      |
| PoE 规范                    | PoE IEEE802.3 AF 规范 / 最大功率 6W / 供电电压 DC 37-57V                 |
| 以太网控制器                | W5500，内置 32Kbytes 缓存区，SPI 接口                                    |
| 支持协议                    | TCP、UDP、IPv4、ICMP、ARP、IGMP 和 PPPoE 协议                            |
| 以太网接口规格              | RJ45                                                                     |
| 基础外设                    | 1x 可编程按键，2x 工作指示灯                                             |
| 产品尺寸                    | 64.0 x 24.0 x 18.0mm                                                     |
| 产品重量                    | 38.0g                                                                    |
| 包装尺寸                    | 80.0 x 37.0 x 32.0mm                                                     |
| 毛重                        | 45.0g                                                                    |

## 操作说明

?> 使用注意事项 | 摄像头长时间连续获取高分辨率的图像流，可能会导致设备过热，成像颜色异常。长时间工作情况，建议额外提供散热。

\#>**注意事项:**<br/>1. **PoECAM 下载程序需外接 ESP32 烧录器**，你可以[点击此处购买M5官方的ESP32-Downloader套件，内含转接小板，连接会更加的方便](https://shop.m5stack.com/products/esp32-downloader-kit)<br/>2. PoECAM 的出厂固件，在连接交换机后将会自动获取 IP，并启动 web 服务器。通过查看 PoECAM 的串口输出，可以获取到 IP 地址与图像流 URL，同一局域网下用浏览器的访问该 URL，既可以实时预览图像。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_04.webp" width="100%" height="30%">

## 原理图

- [Unit PoE CAM原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/poe_cam/M5PoECAM.pdf)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_sch_01.webp" width="80%">

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

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)
- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Unit PoE CAM Arduino 快速上手](/zh_CN/arduino/m5poe_cam/program)
- [Unit PoE CAM Arduino 驱动库](https://github.com/m5stack/PoE_CAM)
- [Unit PoE CAM Button Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/button)
- [Unit PoE CAM Capture Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/capture)
- [Unit PoE CAM HTTP POST Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/http_post)
- [Unit PoE CAM LED Control Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/led)
- [Unit PoE CAM RTSP Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/rtsp_stream)
- [Unit PoE CAM Web CAM Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/web_cam)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/PoECAM_VIDEO.mp4" type="video/mp4">
</video>
