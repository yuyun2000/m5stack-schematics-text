# Atom PoE

<span class="product-sku">SKU:K052</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_06.webp">
</PictureViewer>

## 描述

**Atom PoE** 是一款适配 ATOM 主控的以太网控制器底座，支持 PoE (有源以太网) 技术，通过内置的 PoE 模块可以直接通过 PoE 集线器 / 交换机为设备整机供电而无需单独配备电源，有效降低线路搭建成本。内置 W5500 嵌入式以太网控制器，集成了 TCP/IP 协议栈，具备 8 路独立硬件 socket，10/100M 以太网数据链路层 (MAC) 及物理层 (PHY) 为嵌入式系统提供更加便捷的互联网连接方案。能够满足实际生产环境中的有线网络接入需求。

## 产品特性

- 支持 PoE IEEE802.3 AF
- 有线以太网接入
- 支持 8 路独立硬件 Socket 同时通信
- 支持 TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE 协议
- 集成 10BaseT / 100Base-T 以太网 PHY

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic PoE Base
- 1 x USB Type-C 连接线 (20cm)
- 1 x M2 六角扳手
- 1 x M2x8 螺丝

## 应用场景

- 远程控制
- 有线网络接入

## 规格参数

| 规格         | 参数                                                           |
| ------------ | -------------------------------------------------------------- |
| 以太网芯片   | W5500                                                          |
| 支持协议     | TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE                         |
| PoE 供电方式 | 空闲引脚供电（10M/100M Ethernet），J4\&J5（VC-）,J7\&J8（VC+） |
| PoE 规范     | IEEE802.3 AF                                                   |
| 工作温度     | 0 ~ 40°C                                                       |
| 产品尺寸     | 24.0 x 48.0 x 18.0mm                                                 |
| 产品重量     | 22.0g                                                            |
| 包装尺寸     | 54.0 x 54.0 x 20.0mm                                                 |
| 毛重         | 44.0g                                                            |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| 3V3      |      | 1     |     |
| SPI_CLK  | 2    | 3     |     |
| CS       | 4    | 5     | 5V  |
| SPI_MISO | 6    | 7     | GND |
| SPI_MOSI | 8    | 9     |     |
::

| Atom     | G22 | G19 | G23  | G33  |
| -------- | --- | --- | ---- | ---- |
| Atom PoE | CLK | CS  | MISO | MOSI |

## 数据手册

- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Atom PoE 测试程序](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_PoE)

### UiFlow1

- [Atom PoE UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/poe)

### EasyLoader

| Easyloader          | 下载链接                                                                                                      | 备注 |
| ------------------- | ------------------------------------------------------------------------------------------------------------- | ---- |
| Atom PoE Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_PoE.exe) | /    |

## 相关视频

- 连接以太网，访问通过 IP 访问控制页面，控制 RGB LED 改变颜色

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_PoE.mp4" type="video/mp4">
</video>
