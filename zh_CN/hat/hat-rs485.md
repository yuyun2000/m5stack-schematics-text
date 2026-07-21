# Hat RS485

<span class="product-sku">SKU:U067</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_06.webp">
</PictureViewer>

## 描述

**Hat RS485** 是一款兼容 M5SticKC 的 RS485 转换器。内部集成 SP485EEN，主要部分由一个 485 自动收发器电路和一个 DC-DC 降压电路组成（可以将输入电压降至 5V）。RS485 是一种标准，用于定义串行通信系统的驱动器和接收器的电气特性，广泛用于工业领域，支持多点系统。 该产品用于将 TTL 标准转换为 RS485 标准。 如果外部串行设备是 RS485 标准，可以通过该模块实现 TTL 转换 RS485 协议的实现设备之间的通信。

## 产品特性

- 内置 SP485EEN
- 内置自动收发电路
- 内置 DC-DC 降压电路
- AOZ1282CI
- 输入电压: DC 12V
- 波特率：115200
- 开发平台: Arduino, UiFlow (Blockly, Python)

## 包装内容

- 1 x Hat RS485
- 1 x HT3.96-4P 端子
- 1 x I/O 贴纸
- 1 x 双面胶

## 应用场景

- RS485 多点系统
- 工业领域的串行通信

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量 | 7g                   |
| 毛重     | 17g                  |
| 产品尺寸 | 34.9 x 24.0 x 13.7mm |
| 包装尺寸 | 40 x 42 x 30mm       |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_sch_01.webp" width="80%" height="80%">

## 管脚映射

| M5StickC  | G0  | G26 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| Hat RS485 | TX  | RX  | 5V  | GND |

## 尺寸图

- [Hat RS485模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/864/HATRS485.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/864/HATRS485_page_01.png" width="100%">

## 数据手册

- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)

## 软件开发

### Arduino

- [Hat RS485 Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/RS485)

### UiFlow1

- [Hat RS485 UiFlow1 文档](/zh_CN/uiflow/blockly/hat/rs485)

### Easyloader

| Easyloader           | 下载链接                                                                                               | 备注 |
| -------------------- | ------------------------------------------------------------------------------------------------------ | ---- |
| Hat RS485 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/RS485/EasyLoader_RS485_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/RS485_HAT.mp4" type="video/mp4" >
</video>
