# Chain Switch

<span class="product-sku">SKU:U227</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_weight.jpg">
</PictureViewer>

## 描述

Chain Switch 是 M5Stack Chain 系列中的一款滑动开关输入节点，支持滑动条模式与开关模式。设备可输出 12 位滑动位置数据，并配有可编程 RGB LED，用于提供直观的状态反馈。内部集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 扩展接口，可连接更多 Chain 系列设备，适用于控制面板、状态切换和交互装置等应用。

## 产品特性

- M5Stack Chain 系列
- 支持滑动条模式与开关模式：
  - 滑动条模式：读取滑动位置，输出范围为 0 ~ 4095
  - 开关模式：根据设定的开、关阈值输出开关状态
- 12 位 ADC 滑动位置检测
- STM32G031G8U6 核心主控
- 1x RGB LED
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 扩展接口，可扩展 Chain 系列设备

## 包装内容

- 1 x Chain Switch
- 1 x Chain Bridge

## 应用场景

- 控制面板输入
- 智能家居状态切换
- 交互装置控制

## 规格参数

| 规格         | 参数                         |
| ------------ | ---------------------------- |
| MCU          | STM32G031G8U6                |
| 输入电源     | DC 5V                        |
| 通信方式     | UART 115200bps@8N1           |
| 接口规格     | 2x HY2.0-4P                  |
| 滑动位置检测 | 12 位 ADC，输出范围 0 ~ 4095 |
| RGB LED      | 1x WS2812C                   |
| 工作功耗     | 5V@10.57mA (典型工作状态)    |
| 产品尺寸     | 24.0 x 24.0 x 18.5mm         |
| 产品重量     | 5.9g                         |
| 包装尺寸     | 138.0 x 93.0 x 21.0mm        |
| 毛重         | 9.2g                         |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Switch 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_SCH_Main_V1.0_20260608.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_SCH_Main_V1.0_20260608_page_01.png">
</SchViewer>

## 管脚映射

### Slider

| STM32G031 | PB0    |
| --------- | ------ |
| Slider    | ADC_IN |

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Switch 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Switch Arduino 快速上手](/zh_CN/arduino/projects/chain/chain_switch)
- [Chain Switch Arduino 驱动库](https://github.com/m5stack/M5Chain)

### 内置固件

- [Chain Switch 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Switch)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/U227/UART" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="Chain Switch 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_video_CN.mp4" />
</VideoGallery>
