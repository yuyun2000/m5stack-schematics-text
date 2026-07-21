# Atomic Display Base

<span class="product-sku">SKU:A115</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/11.webp">
</PictureViewer>

## 描述

**Atomic Display Base** 是一款高清显示器驱动单元，使用 FPGA 模拟传统 SPI TFT-LCD 数据输出，支持最大 720P (1280 x 720) 图像输出，并通过专用 RGB 转高清多媒体信号芯片实现广泛兼容的显示输出。用户可搭配 Atom 系列主机，以满足不同内存和应用需求。Atomic Display Base 能够替代传统显示面板的 PC 控制方案，提供更具性价比的选择，适用于工业控制显示、智能家居信息屏、教育与会议演示、远程监控显示等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/atomic/atomic_display_base) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Atomic Display Base 设备 |

## 产品特性

- 采用 FPGA (Gowin GW1NR-9C)
- 内置 LT8618SX RGB 转高清多媒体信号芯片 (支持 24bit 色深)
- SPI 接口 (FPGA) + I2C 接口 (LT8618SX)
- 最大 720P (1280x720) 的图像输出
- 多种输出模式，优化帧率可达 12 ~ 16FPS
- 开发平台：Arduino, ESP32-IDF, UiFlow

## 包装内容

- 1 x Atomic Display Base

## 应用场景

- 显示器输入信号源
- 高清数据看板

## 规格参数

| 规格             | 参数                                      |
| ---------------- | ----------------------------------------- |
| FPGA             | Gowin GW1NR-9C                            |
| LT8618SX         | RGB 转高清多媒体信号芯片，支持 24bit 色深 |
| 最大图像输出尺寸 | 720P (1280x720)                           |
| 输出帧率         | 1280x720 60Hz                             |
| 产品尺寸         | 64.0 x 24.0 x 29.0mm                      |
| 包装尺寸         | 136.0 x 92.0 x 30.0mm                     |
| 产品重量         | 15.2g                                     |
| 毛重             | 17.3g                                     |

## 操作说明

\#> 显示器兼容性 | Atomic Display Base 需搭配具备自适应分辨率缩放功能的显示器，在一些不支持自适应分辨率的显示器上可能会出现显示异常现象。

## 原理图

- [Atomic Display Base原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_display/Sch_AtomDisplay.pdf)

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Display Base/img-3f5ac8bb-5276-4d1d-9edb-2921f8aab2f2.jpg" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
|     | 2    | 3     | SPI_CLK  |
|     | 4    | 5     | CS       |
| 5V  | 6    | 7     | SPI_MISO |
| GND | 8    | 9     | SPI_MOSI |
::

### LT8618SX

| Atomic Display Base | G25     | G21     |
| ------------------- | ------- | ------- |
| LT8618SX            | LT_CSDA | LT_CSCL |

## 尺寸图

- [Atomic Display Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/A115-atom-display.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/933/A115-atom-display_page_01.png" width="100%">

## 数据手册

- [LT8618SX](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/LT8618SX.pdf)
- [GW1NR-9C Data Sheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/GW1NR%20Serial%20data%20sheet.pdf)
- [GW1NR-9C Design Manual](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/GW1N(R)%20Serial%20FPGA%20SCH%20Design.pdf>)

## 软件开发

### Arduino

- [M5GFX Library](https://github.com/m5stack/M5GFX)

### UiFlow2

- [Atomic Display Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/display.html)

## 视频

- Atomic Display Base 产品示例介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Display%20Base/atomic%20display%20base%20video.mp4" type="video/mp4" type="video/mp4"></video>
