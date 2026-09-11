# Chain PIR

<span class="product-sku">SKU:U225</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_main_pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_weight.png">
</PictureViewer>

## 描述

Chain PIR 是 M5Stack Chain 系列中的一款热释电人体红外感应节点。内置热释电红外传感器，并集成可编程 RGB LED。适用于人体活动检测、智能家居自动化及安防报警等应用场景。

Chain PIR 集成 STM32G031G8U6 数据处理器，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 拓展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- 热释电人体红外感应
- STM32G031G8U6 核心主控
- 采用 UART 串口级联通信协议
- 1x RGB LED
- 2x HY2.0-4P 拓展接口，可拓展 Chain 系列设备
- 两种工作模式：
  - 自动上报模式：PIR 状态变化时，自动发送数据至主机
  - 查询模式：由主机主动发起查询，从机响应当前 PIR 状态

## 包装内容

- 1 x Chain PIR
- 1 x Chain Bridge

## 应用场景

- 人体活动检测
- 智能家居自动化
- 安防报警

## 规格参数

| 规格         | 参数                   |
| ------------ | ---------------------- |
| MCU          | STM32G031G8U6          |
| 输入电源     | DC 5V                  |
| 通信方式     | UART 115200bps@8N1     |
| 接口规格     | 2 x HY2.0-4P           |
| RGB LED      | 1 x WS2812C            |
| 传感器       | AS312 热释电红外传感器 |
| 最大检测距离 | 2.4m                   |
| 检测角度     | ±60°                   |
| 检测间隔     | 2s                     |
| 工作功耗     | 5V@10.74mA             |
| 产品尺寸     | 23.9 x 23.9 x 22.3mm   |
| 产品重量     | 6.8g                   |
| 包装尺寸     | 138.0 x 93.0 x 21.0mm  |
| 毛重         | 10.0g                  |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain PIR 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/ChainPIR_V01_2025_06_18_19_10_05.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/ChainPIR_V01_2025_06_18_19_10_05.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031 | PA8 |
| --------- | --- |
| WS2812C   | RGB |

### PIR

| STM32G031  | PB0   |
| ---------- | ----- |
| PIR Sensor | Input |

PIR Sensor 的检测触发维持时间为 2 秒；重复触发时，维持时间从最后一次有效脉冲重新计时。

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain PIR 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225-Chain_PIR_Model_Size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225-Chain_PIR_Model_Size.png" width="100%">

## 软件开发

### Arduino

- [Chain PIR Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_pir)
- [Chain 系列产品 驱动库](https://github.com/m5stack/M5Chain)
- [Chain PIR 测试程序](https://github.com/m5stack/M5Chain/tree/main/examples/PIR_Example)

### UiFlow2

- [Chain PIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/pir.html)

### 内置固件

- [Chain PIR 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-PIR)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/U225/UART" title="查看通信协议" />

- [Chain PIR 通信协议 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/M5Stack-Chain-PIR-Protocol-V1_CN.pdf)

## 相关视频

- Chain PIR 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_video_CN.mp4" type="video/mp4"></video>

<!--英文视频链接：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/U225_Chain_PIR_video_EN.mp4>-->
