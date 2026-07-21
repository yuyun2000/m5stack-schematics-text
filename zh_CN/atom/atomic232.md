# Atom RS232

<span class="product-sku">SKU:K046</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_06.webp">
</PictureViewer>

## 描述

**Atom RS232** 是一款基于 Atomic 设计的 TTL-RS232 电平转换器。RS232 是一种全双工通信协议标准，定义了串行通信系统的电气特性，在工业控制领域是一种应用广泛的通讯协议。模块采用 MAX232 芯片，支持 TTL 电平与 RS232 电平的双向转换，同时内置 DC-DC 降压稳压芯片，可以直接通过 RS232 的 12V 电平为 ATOM 供电。

## 产品特性

- 全双工通讯
- 内置 DC-DC

## 包装内容

- 1 x Atom-Lite
- 1 × Atomic RS232 Base
- 1 x M2 内六角扳手
- 1 x M2\*8mm 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- RS232 通讯
- 工业控制节点

## 规格参数

| 规格         | 参数             |
| ------------ | ---------------- |
| 外接端口     | VH-3.96 4P       |
| 电平转换芯片 | MAX232           |
| DC-DC        | A0Z1282CI        |
| 外壳材质     | Plastic （ PC ） |
| 产品尺寸     | 24 x 48 x 18mm   |
| 产品重量     | 26g              |
| 包装尺寸     | 54 x 54 x 20mm   |
| 毛重         | 36g              |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN |
| ------- | ---- | ----- | --- |
| 3V3     |      | 1     |     |
| UART_TX | 2    | 3     |     |
| UART_RX | 4    | 5     | 5V  |
|         | 6    | 7     | GND |
|         | 8    | 9     |     |
::

## 数据手册

- [MAX232](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicRS232/MAX232.pdf)
- [AOZ1282CI](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/tail485/AOZ1282CI-datasheet.pdf)

## 软件开发

### Arduino

- [Atom RS232 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS232/Arduino/AtomicRS232)

### UiFlow1

- [Atom RS232 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS232/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_uiflow_01.webp" width="70%" height="70%">

### EasyLoader

| Easyloader            | 下载链接                                                                                                        | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| Atom RS232 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_RS232.exe) | /    |

## 相关视频

- 通过 RS485 收发到消息 LED 亮起，按下按键发送消息

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomicRS232.mp4" type="video/mp4">
</video>
