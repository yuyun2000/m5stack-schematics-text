# Atomic CAN Base

<span class="product-sku">SKU:A103</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-8c8eb3c4-9657-4330-9e1a-a0f5f3290197.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-bf76f9ef-f775-4a04-8b4e-8f0526933f9b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-9e16346a-fcbf-40ff-b10d-941c92a2d0e2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-3abf1fa4-e4ed-4538-84bd-73162e2d7366.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-b000ce07-7e0a-4bfe-bd06-66423829e090.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-33b20de7-6f6e-42ee-bc7d-7ad25f95b919.webp">
</PictureViewer>

## 描述

**Atomic CAN Base** 是一款 CAN 总线通信单元，采用 CA-IS3050G 收发器方案 (内置的 DC-DC 隔离电源芯片能够有效隔离干扰，防止损坏敏感电路) 。通信总线可支持多达 110 个节点，信号传输速率可达 1Mbps 且具备多种电气线路保护功能。非常适合于车载运输与安防系统等应用场景。

## 产品特性

- CAN 总线多点通讯
- 内置隔离 DC-DC
- 信号速率高达 1Mbps
- 共模电压范围为–12V 至 12V
- 信号保护功能

## 包装内容

- 1 x Atomic CAN Base
- 1 x HT3.96-4P 端子

## 应用场景

- CAN 总线通信
- 车载设备控制
- 工业现场控制

## 规格参数

| 规格           | 参数            |
| -------------- | --------------- |
| 外接端口       | HT3.96-4P       |
| CAN 收发器型号 | CA-IS3050G      |
| 最高速率       | 1Mbps           |
| 支持节点数     | 110             |
| 低环路延迟     | 150ns           |
| 共模电压       | -12V ~ 12V      |
| 工作温度       | 0 ~ 40°C        |
| 外壳材质       | Plastic (PC)    |
| 产品尺寸       | 24 x 48 x 18mm  |
| 包装尺寸       | 136 x 92 x 20mm |
| 产品重量       | 11.1g           |
| 毛重           | 15.6g           |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-fa481a72-f110-4866-9266-b67369f6ff2a.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN     |
| --- | ---- | ----- | ------- |
|     |      | 1     | 3V3     |
|     | 2    | 3     | UART_TX |
|     | 4    | 5     | UART_RX |
| 5V  | 6    | 7     |         |
| GND | 8    | 9     |         |
::

## 尺寸图

- [Atomic CAN Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm_page_01.png" width="100%">

## 数据手册

- [CA-IS3050G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3050G.pdf)

## 软件开发

### Arduino

- [Atomic CAN Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_can_base)

### UiFlow1

- [Atomic CAN Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/can)

### UiFlow2

- [Atomic CAN Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/atom_can.html)

### EasyLoader

| Easyloader                  | 下载链接                                                                                                              | 备注 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom CAN Sender Easyloader  | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_CAN_SENDER.exe)  | /    |
| Atom CAN Receive Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_CAN_RECEIVE.exe) | /    |

## 相关视频

- CAN 总线交互例子

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_CAN_VIDEO.mp4" type="video/mp4"></video>

- CAN 总线交互例子 (3 个 ATOMOIC CAN BASE 进行通讯的例子)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_can/85ce623f3ada31ee9b4d05d45174542d.mp4" type="video/mp4"></video>
