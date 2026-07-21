# Atom RS485

<span class="product-sku">SKU:K045</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_06.webp">
</PictureViewer>

## 描述

**Atom RS485** 是一款基于 Atomic 设计的 TTL-RS485 转换器，用于 TTL 电平与 RS485 电平转换。RS485 是一种通信协议标准，用于定义串行通信系统的驱动器和接收器的电气特性，它支持多点系统，广泛应用于工业领域。其内部集成有 DC/DC 降压稳压芯片，可以直接将 RS485 的 12V 电压转为 5V 为 ATOM 供电，免去了单独供电的烦恼，当多台设备需要通信控制时，使用 Atom RS485 进行接口类型转接会是一个不错的选择。

## 产品特性

- 多点通讯
- SP3485EE
- 内置 DC/DC

## 包装内容

- 1 x Atom-Lite
- 1 × Atomic RS485 Base
- 1 x M2 内六角扳手
- 1 x M2\*8mm 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- RS485 多点通讯
- 工业控制节点
- RS485 转 WiFi

## 规格参数

| 规格        | 参数             |
| ----------- | ---------------- |
| 外接端口    | VH-3.96 4P       |
| 转换电平    | 5V12V            |
| 电平转换 IC | SP3485EE         |
| DC-DC       | A0Z1282CI        |
| 外壳材质    | Plastic （ PC ） |
| 产品尺寸    | 24 x 48 x 18mm   |
| 产品重量    | 28g              |
| 包装尺寸    | 54 x 54 x 20mm   |
| 毛重        | 38g              |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| 3V3      |      | 1     |     |
| RS485_RX | 2    | 3     |     |
| RS485_TX | 4    | 5     | 5V  |
|          | 6    | 7     | GND |
|          | 8    | 9     |     |
::

## 数据手册

- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)
- [AOZ1282CI](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/tail485/AOZ1282CI-datasheet.pdf)

## 软件开发

### Arduino

- [Atom RS485 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS485/Arduino/AtomicRS485)

### UiFlow1

- [Atom RS485 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS485/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_uiflow_01.webp" width="70%" height="70%">

### EasyLoader

| Easyloader            | 下载链接                                                                                                        | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| Atom RS485 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_RS485.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomicRS485.mp4" type="video/mp4">
</video>
