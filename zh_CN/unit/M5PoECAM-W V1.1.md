# Unit PoE CAM-W v1.1

<span class="product-sku">SKU:U121-B-V11</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/7.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/U121-B-V11-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/10.webp">
</PictureViewer>

## 描述

**Unit PoE CAM-W v1.1** 是一款基于 “ESP32+W5500” 方案的可编程 PoE 摄像机，内置 3MP 的 OV3660 图像传感器，具有 66.5° 视场角，集成 PoE (通过以太网供电，最大功耗 6W) 和 Wi-Fi 功能。配备 16MB Flash 和 8MB PSRAM，预留程序下载接口。该摄像机配有丰富的接口和功能模块，包括按键 (G37) 、LED 提示灯 (G0) 、Grove 接口 (EXT_PORT)，和扩展 IO 引脚，并配有相机安装夹和乐高兼容夹。适用于图像监控、远程采集、智能家居、工业自动化等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5poe_cam/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit PoE CAM 设备。 |

learn>| ![M5PoECAM-W V1.1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20v1.1/1.png) | [Quick Start](/zh_CN/guide/eth_camera/poe_cam/web_cam) | 本教程将向你介绍，M5PoECAM-W V1.1 设备教程 & 快速上手 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/camera/unit_poe_cam_w_v1.1) | 本教程介绍如何将 PoE Camera 添加至 Home Assistant |

## 产品特性

- 内置 ESP32-D0WDQ6-V3 (支持 2.4G Wi-Fi)
- 3MP 摄像头 OV3660
- 以太网芯片 W5500
- LAN 的速率可达 10M 或 100M (根据具体提供的线路而定)
- PoE IEEE802.3 AF 规范 (最大功率 6w)
- 内置提示 LED 灯
- 以太网标准接口 RJ45
- 兼容标准 LEGO 接口和配备相机支架
- 开发平台：Arduino、ESP-IDF

## 包装内容

- 1 x Unit PoE CAM-W v1.1
- 1 x 相机安装夹
- 1 x LEGO 兼容夹

## 应用场景

- 仓库监控
- 定时拍摄
- 机器视觉
- 家庭智能监控

## 规格参数

| 规格                 | 参数                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| SoC                  | ESP32-D0WDQ6-V3                                                                                                    |
| 摄像头模块           | OV3660@3Megapixel                                                                                                  |
| DFOV                 | 66.5°                                                                                                              |
| 以太网芯片           | W5500                                                                                                              |
| Flash                | 16MB                                                                                                               |
| PSRAM                | 8MB                                                                                                                |
| Wi-Fi                | 802.11 b/g/n                                                                                                       |
| 像素尺寸             | 1.75µm x 1.75µm                                                                                                    |
| 输出格式             | RAW<br/>RGB565/555/444 <br/>YUV422/420<br/>YCbCr422<br/>JPEG                                                       |
| 自动图像控制功能     | 自动曝光控制 (AEC) <br/>自动增益控制 (AGC) <br/>自动白平衡 (AWB) <br/>自动带带滤波器 (ABF) 和自动黑电平校准 (ABLC) |
| 支持连接 TCP/IP 协议 | TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE                                                                             |
| 以太网接口规格       | RJ45                                                                                                               |
| PoE                  | PoE IEEE802.3 AF 规范 (最大功率 6w)                                                                                |
| 产品尺寸             | 64.0 x 24.0 x 18.0mm                                                                                               |
| 产品重量             | 20.6g                                                                                                              |
| 包装尺寸             | 80.0 x 38.0 x 33.0mm                                                                                               |
| 毛重                 | 44.6g                                                                                                              |

## 操作说明

?> 使用注意事项 | 摄像头长时间连续获取高分辨率的图像流，可能会导致设备过热，成像颜色异常。长时间工作情况，建议额外提供散热。

\#> 下载程序示意图 | <img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20v1.1/%E4%B8%8B%E8%BD%BD%E5%9B%BE.png" width="50%" />

## 原理图

- [Unit PoE CAM-W v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/595/Sch_M5PoECAM-W.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/595/Sch_M5PoECAM-W_sch_01.png">
</SchViewer>

## 管脚映射

- Grove 接口 & 按键 & Led 提示灯

| ESP32-D0WDQ6-V3 | G33 | G25 | 5V  | GND | G37    | G0  |
| --------------- | --- | --- | --- | --- | ------ | --- |
| Grove           | SCL | SDA | VCC | GND |        |     |
| Button          |     |     |     |     | Button |     |
| LED (Blue)      |     |     |     |     |        | LED |

- 拓展引脚 (下载引脚)

| ESP32-D0WDQ6-V3 | CHIP_UP | G0  | GND | VCC  | G1  | G3  |
| --------------- | ------- | --- | --- | ---- | --- | --- |
| Expansion pin   | EN      | G0  | G   | 3.3V | G1  | G3  |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/M5PoECAM-W V1.1/img-40419f43-5f2d-40e8-92e9-bceec6908475.png" width="100%" />

## 数据手册

- [ESP32-D0WDQ6-V3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV3660](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)
- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Unit PoE CAM-W v1.1 Arduino 快速上手](/zh_CN/arduino/m5poe_cam/program)
- [Unit PoE CAM-W v1.1 Arduino 驱动库](https://github.com/m5stack/PoE_CAM)
- [Unit PoE CAM-W v1.1 Button Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/button)
- [Unit PoE CAM-W v1.1 Capture Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/capture)
- [Unit PoE CAM-W v1.1 HTTP POST Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/http_post)
- [Unit PoE CAM-W v1.1 LED Control Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/led)
- [Unit PoE CAM-W v1.1 RTSP Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/rtsp_stream)
- [Unit PoE CAM-W v1.1 Web CAM Example](https://github.com/m5stack/M5PoECAM/tree/master/examples/web_cam)

### Home Assistant

- [Unit PoE CAM-W v1.1 Home Assistant 集成](/zh_CN/homeassistant/camera/unit_poe_cam_w_v1.1)

### EasyLoader

| Easyloader                              | 下载链接                                                                                                                              | 备注 |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit PoE CAM-W v1.1 Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/PoECAM-W%20V1.1%20Firmware.exe) | /    |

## 相关视频

- Unit PoE CAM-W V1.1 HTTP STREAM

<video class="video-container" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/M5PoECAM-W%20V1.1/U121-B-V11%20M5PoECAM-W%20V1.1%20%E8%A7%86%E9%A2%911.mp4" playsinline controls></video>
