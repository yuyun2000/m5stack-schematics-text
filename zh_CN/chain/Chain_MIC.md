# Chain MIC

<span class="product-sku">SKU:U226</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_weight.jpg">
</PictureViewer>

## 描述

Chain MIC 是 M5Stack Chain 系列中的一款声音采集节点。内置 GMI4015P-2C 麦克风、SGM321YC5/TR 运算放大器与可编程 RGB LED，支持声音信号 **12 位 ADC** 采样及阈值触发，适用于环境声音检测、声控交互和设备状态提示等应用场景。内部集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 扩展接口，可扩展更多 Chain 系列设备，构建更加丰富的声音感知与交互应用。

## 产品特性

- M5Stack Chain 系列
- GMI4015P-2C 麦克风声音采集
- 支持声音信号 **12 位 ADC** 采样与阈值触发
- STM32G031G8U6 核心主控
- 1x RGB LED
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 扩展接口，可扩展 Chain 系列设备

## 包装内容

- 1 x Chain MIC
- 1 x Chain Bridge

## 应用场景

- 环境声音检测
- 声音阈值触发
- 声控交互设备
- 智能家居声音感知

## 规格参数

| 规格       | 参数                            |
| ---------- | ------------------------------- |
| MCU        | STM32G031G8U6                   |
| 输入电源   | DC 5V                           |
| 通信方式   | UART 115200bps@8N1              |
| 接口规格   | 2x HY2.0-4P                     |
| 麦克风     | GMI4015P-2C                     |
| 运算放大器 | SGM321YC5/TR                    |
| RGB LED    | 1x WS2812C-2020                 |
| 声音信号   | 12 位 ADC 采样值、阈值触发状态  |
| 工作功耗   | 5V@35.54mA (MIC 工作、白灯常亮) |
| 产品尺寸   | 24.0 x 24.0 x 16.0mm            |
| 产品重量   | 5.7g                            |
| 包装尺寸   | 138.0 x 93.0 x 17.0mm           |
| 毛重       | 9.0g                            |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain MIC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/Chain_MIC_SCH_Main_V1.0_20250626_2026_07_10_13_59_52.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/Chain_MIC_SCH_Main_V1.0_20250626_2026_07_10_13_59_52.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### MIC

| STM32G031 | PA7 | PB0 |
| --------- | --- | --- |
| MIC       | AIN | DIN |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain MIC 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain MIC Arduino 快速上手](/zh_CN/arduino/projects/chain/chain_mic)
- [Chain MIC Arduino 驱动库](https://github.com/m5stack/M5Chain)

### UiFlow2

- [Chain MIC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/mic.html)

### 内置固件

- [Chain MIC 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-MIC)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/U226/UART" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="Chain MIC 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/U226_Chain_MIC_video_CN.mp4" />
</VideoGallery>
