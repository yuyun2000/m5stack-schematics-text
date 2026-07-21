# Atomic PoE Base

<span class="product-sku">SKU:A091</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-dbec41f6-7d53-477d-89a0-1a889888bd62.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-ae81daf4-976a-433b-b35a-507e0989ad5d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-83593788-27dd-4c97-a392-7d932ba7d799.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-a5c3a43b-e616-45c1-b55b-0becf537fd37.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-c6372274-ca2b-4e75-906d-d7c1282fa1cf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-6e127478-40e4-405d-8553-d56e9682b9ba.webp">
</PictureViewer>

## 描述

**Atomic PoE Base** 是一款适配 ATOM 系列主控的以太网控制器底座，支持 PoE (有源以太网) 技术，通过内置的 PoE 模块可以直接通过 PoE 集线器 / 交换机为设备整机供电而无需单独配备电源，有效降低线路搭建成本。内置 W5500 嵌入式以太网控制器，集成了 TCP/IP 协议栈，具备 8 路独立硬件 socket，10/100M 以太网数据链路层 (MAC) 及物理层 (PHY) ，为嵌入式系统提供更加便捷的互联网连接方案。能够满足实际生产环境中的有线网络接入需求。

## 产品特性

- 适用于 Atom-Lite/Atom-Matrix/AtomS3/AtomS3-Lite
- 支持 PoE IEEE802.3 AF
- 有线以太网接入
- 支持 8 路独立硬件 Socket 同时通信
- 支持 TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE 协议
- 集成 10BaseT / 100Base-T 以太网 PHY

## 包装内容

- 1 x Atomic PoE Base

## 应用场景

- 远程控制
- 有线网络接入

## 规格参数

| 规格         | 参数                                                        |
| ------------ | ----------------------------------------------------------- |
| 以太网芯片   | W5500                                                       |
| 支持协议     | TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE                      |
| PoE 供电方式 | 空闲引脚供电 (10M/100M Ethernet)，J4\&J5 (VC-),J7\&J8 (VC+) |
| PoE 规范     | IEEE802.3 AF                                                |
| 工作温度     | 0 ~ 40°C                                                    |
| 产品尺寸     | 64.0 x 24.0 x 17.5mm                                        |
| 产品重量     | 17g                                                         |
| 包装尺寸     | 136 x 92 x 20mm                                             |
| 毛重         | 20.5g                                                       |

## 原理图

- [Atomic PoE Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/465/Sch_AtomicPoE_v1.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/465/Sch_AtomicPoE_v1.2_sch_01.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
|     | 2    | 3     | SPI_CLK  |
|     | 4    | 5     | CS       |
| 5V  | 6    | 7     | SPI_MISO |
| GND | 8    | 9     | SPI_MOSI |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PoE Base/img-942113e5-3854-45c4-9f45-3ce6a582c57f.jpg" width="100%" />

## 数据手册

- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Atomic PoE Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_poe_base)
- [Atomic PoE Base Remote LED Control - with Atom-Lite](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_PoE)
- [Atomic PoE Base HTTP Client - with AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/AtomicBase/AtomicPoE/HTTP)
- [Atomic PoE Base LinkStatus - with AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/AtomicBase/AtomicPoE/LinkStatus)
- [Atomic PoE Base MQTT Client - with AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/AtomicBase/AtomicPoE/MQTT)
- [Atomic PoE Base WebServer - with AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/AtomicBase/AtomicPoE/WebServer)

### UiFlow1

- [Atomic PoE Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/poe)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                                     | 备注 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic PoE Base Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20PoE%20Base/ezLoader-aa92d2a6-fb14-4c06-8a38-a7b59e0417ee.exe) | /    |

## 相关视频

- 连接以太网，通过 IP 访问控制页面，控制 RGB LED 改变颜色

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_PoE.mp4" type="video/mp4"></video>
