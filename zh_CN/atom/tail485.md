# Tail RS485

<span class="product-sku">SKU:T002</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/901/T002_Tail_RS485_weight.jpg">
</PictureViewer>

## 描述

**Tail RS485** 是一款为 ATOM 设计的 TTL-RS485 转换器，用于 TTL 电平与 RS485 电平转换。RS485 是一种通信协议标准，用于定义串行通信系统的驱动器和接收器的电气特性，支持多点系统，适用于工业领域。当项目设备需要通过 RS485 进行通信控制时，使用 Tail485 进行接口类型转接会是一个不错的选择。在 Tail485 的内部集成有 DC/DC 降压稳压芯片，可以直接将 RS485 的 12V 电压转为 5V 为 Type-C 接口供电，免去了单独供电的烦恼。

## 产品特性

- 内置 DC/DC
- SP485EEN-L

## 包装内容

- 1 x Tail RS485
- 1 x HT3.96-4P 端子
- 1 x I/O 贴纸

## 应用场景

- RS485 多点通讯

## 规格参数

| 规格        | 参数                  |
| ----------- | --------------------- |
| 外接端口    | VH-3.96 4P            |
| 转换电平    | 9 ~ 24V -> 5V         |
| 电平转换 IC | SP485EEN-L            |
| 稳压降压 IC | AOZ1282CI             |
| 外壳材质    | Plastic（ PC ）       |
| 产品尺寸    | 54.0 x 96.0 x 10.0mm  |
| 产品重量    | 9.0g                  |
| 包装尺寸    | 136.0 x 92.0 x 10.0mm |
| 毛重        | 11.3g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_sch_01.webp" width="80%">

## 管脚映射

| Atom Lite | G26 | G32 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| Tail485   | TX  | RX  | 5V  | GND |

## 尺寸图

- [Tail RS485 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/901/T002-tail-rs485.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/901/T002-tail-rs485_page_01.png" width="100%">

## 数据手册

- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)
- [AOZ1282CI](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/tail485/AOZ1282CI-datasheet.pdf)

## 软件开发

### Arduino

- [Tail RS485 TX/RX Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/Tail485/Tail485)

### UiFlow1

- [Tail RS485 TX/RX Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/Tail485/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_uiflow_01.webp" width = "50%">

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/Tail485.mp4" type="video/mp4">
</video>
