# Chain Encoder

<span class="product-sku">SKU:U207</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder-main-pictuers_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207-weight.jpg">
</PictureViewer>

## 描述

Chain Encoder 是 M5Stack Chain 系列中的一款旋转编码器输入节点。内部集成 AB 旋转编码器，支持检测旋转方向与脉冲计数，旋钮中心支持按键输入。同时集成可编程 RGB LED 用于状态指示和交互显示。编码器帽带有 LEGO 兼容孔结构，能够实现更多创意结构连接。适用于人机交互、智能家居控制等应用场景。

Chain Encoder 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 扩展接口，可扩展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- AB 旋转编码器
- 按键输入
- STM32G031G8U6 核心主控
- 1x RGB LED
- LEGO 兼容孔结构
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 扩展接口，可扩展 Chain 系列设备

## 包装内容

- 1 x Chain Encoder
- 1 x Chain Bridge

## 应用场景

- 智能家居控制
- 人机交互

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32G031G8U6         |
| 输入电源 | DC 5V                 |
| 通信方式 | UART 115200bps@8N1    |
| 接口规格 | 2x HY2.0-4P           |
| RGB LED  | 1x WS2812C            |
| 待机功耗 | 22.51mA               |
| 工作温度 | 0 ~ 40°C              |
| 产品尺寸 | 23.9 x 23.9 x 29.8mm  |
| 产品重量 | 10.0g                 |
| 包装尺寸 | 138.0 x 93.0 x 26.0mm |
| 毛重     | 13.7g                 |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Encoder 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder_SCH_Main_V1.0_20250704_2025_10_16_10_44_19.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder_SCH_Main_V1.0_20250704_2025_10_16_10_44_19_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### Encoder

| STM32G031 | PA6 | PA7 | PB0  |
| --------- | --- | --- | ---- |
| Encoder   | A1  | B1  | BTN1 |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Encoder 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207-chain-encoder.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207-chain-encoder_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Encoder Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_encoder)
- [Chain 系列产品 驱动库](https://github.com/m5stack/M5Chain)

### UiFlow2

- [Chain Encoder UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/encoder.html)

### 内置固件

- [Chain Encoder 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Encder)

### 通信协议

- [Chain Encoder 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/M5Stack-Chain-Encoder-Protocol-CN.pdf)

<!-- 英文版链接： https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/M5Stack-Chain-Encoder-Protocol-EN.pdf -->

## 相关视频

- Chain Encoder 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207-Chain-Encoder-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115745660862776&bvid=BV1h4qZB6EKW&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/WMVrNFR839Q?si=lCyTffGsxprtgIlQ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
