# Chain Angle

<span class="product-sku">SKU:U208</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-weight.jpg">
</PictureViewer>

## 描述

Chain Angle 是 M5Stack Chain 系列中的一款电位器旋钮输入节点。随着电位器旋钮旋转，采样端的电压值将在固定的范围内变化。在内置 MCU 进行 ADC 转换后，对外输出最大 12-bit 分辨率的信号值。同时集成可编程 RGB LED 用于状态指示和交互显示。适用于人机交互、智能家居和电机调速控制等应用场景。

Chain Angle 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 扩展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- 电位器旋钮输入
- STM32G031G8U6 核心主控
- 1x RGB LED
- 采用 UART 串口级联通信协议
- 2x HY2.0-4P 扩展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain Angle
- 1 x Chain Bridge

## 应用场景

- 智能家居控制
- 人机交互
- 音量旋钮
- 电机调速

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| MCU          | STM32G031G8U6         |
| 输入电源     | DC 5V                 |
| 通信方式     | UART 115200bps@8N1    |
| 接口规格     | 2x HY2.0-4P           |
| RGB LED      | 1x WS2812C            |
| RGB 开启功耗 | 21.13mA               |
| 旋转角度     | 280° ±10°             |
| 工作温度     | 0 ~ 40°C              |
| 产品尺寸     | 23.9 x 23.9 x 28.2mm  |
| 产品重量     | 8.4g                  |
| 包装尺寸     | 138.0 x 93.0 x 26.0mm |
| 毛重         | 11.7g                 |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Angle 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208_sche__Chain-Angle_SCH_Main_V1.0_20250704_2025_10_14_11_04_40.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208_sche__Chain-Angle_SCH_Main_V1.0_20250704_2025_10_14_11_04_40_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### Angle

| STM32G031 | PB0       |
| --------- | --------- |
| Angle     | ADC_Input |

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Angle 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-chain-angle.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-chain-angle_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Angle Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_angle)
- [Chain 系列产品 驱动库](https://github.com/m5stack/M5Chain)

### UiFlow2

- [Chain Angle UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/angle.html)

### 内置固件

- [Chain Angle 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Angle)

### 通信协议

- [Chain Angle 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/M5Stack-Chain-Angle-Protocol-CN.pdf)

<!-- 英文版链接： https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/M5Stack-Chain-Angle-Protocol-EN.pdf -->

## 相关视频

- Chain Angle 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208-Chain-Angle-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115745543423605&bvid=BV1jdqZBDEGm&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ozx0QhRZhew?si=DNV7PZhbkylxQQsC" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
