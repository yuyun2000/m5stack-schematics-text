# Atom CAN

<span class="product-sku">SKU:K057</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_06.webp">
</PictureViewer>

## 描述

**Atom CAN** 是一款 CAN 总线通信单元，采用 CA-IS3050G 收发器方案 (内置的 DC-DC 隔离电源芯片能够有效隔离干扰，防止损坏敏感电路) 。通信总线可支持多达 110 个节点，信号传输速率可达 1Mbps 且具备多种电气线路保护功能。非常适合于车载运输与安防系统等应用场景。

## 产品特性

- CAN 总线多点通讯
- 内置隔离 DC-DC
- 信号速率高达 1Mbps
- 共模电压范围为–12V 至 12V
- 保护功能:
  - 信号隔离
  - 限流
  - 过压保护
  - 热关断
  - 接地损耗保护 (-40V～40V)

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic CAN Base
- 1 x HT3.96-4P 端子

## 应用场景

- CAN 总线通信
- 车载设备控制
- 工业现场控制

## 规格参数

| 规格           | 参数                           |
| -------------- | ------------------------------ |
| 外接端口       | HT3.96-4P                      |
| CAN 收发器型号 | CA-IS3050G                     |
| 最高速率       | 1Mbps                          |
| 支持节点数     | 110                            |
| 低环路延迟     | 150ns                          |
| 共模电压       | -12V ~ 12V                     |
| 保护功能       | 限流，过压，主动态超时，热关断 |
| 工作温度       | 0 ~ 40°C                       |
| 外壳材质       | Plastic （ PC ）               |
| 产品尺寸       | 24 x 48 x 18mm                 |
| 产品重量       | 14.0g                          |
| 包装尺寸       | 54 x 54 x 20mm                 |
| 毛重           | 33.0g                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_sch_01.webp" width="80%">

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

- [CA-IS3050G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3050G.pdf)

## 软件开发

### Arduino

- [Atom CAN Sender/Receive Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_CAN)

### UiFlow1

- [Atom CAN UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/can)

### EasyLoader

| Easyloader                  | 下载链接                                                                                                              | 备注 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom CAN Sender Easyloader  | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_CAN_SENDER.exe)  | /    |
| Atom CAN Receive Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ATOM_CAN_RECEIVE.exe) | /    |

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20CAN%20Base/1000x1000%2025%E5%B8%A7.mp4" type="video/mp4">
</video>
