# Chain Mount 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Mount |
| SKU | U211 |
| 产品 ID | `chain-mount-15c29cf8cbdc` |
| 源文档 | `zh_CN/chain/Chain_Mount.md` |

## 概述

Chain Mount 是无源四线直通节点，J1 与 J2 两个 GROVE_IO 接口的 IO2、IO1、VCC_5V 和 GND 分别直接相连。原理图未配置主控、收发器、电源转换、保护或信号调理器件，因此不会改变链路协议、电平或信号方向。

## 检索关键词

`Chain Mount`、`U211`、`J1`、`J2`、`GROVE_IO`、`HY2.0-4P`、`IO1`、`IO2`、`VCC_5V`、`GND`、`4-wire pass-through`、`直通`、`Chain series`、`无源节点`、`V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 四线 Chain/Grove 接口，接点依次标注 IO2、IO1、VCC、GND | 图 f5cebbb547bc / 第 1 页 / B2 区域：J1 GROVE_IO 符号及 IO2/IO1/VCC/GND 四个接点 |
| J2 | GROVE_IO | 四线 Chain/Grove 接口，接点依次标注 IO2、IO1、VCC、GND | 图 f5cebbb547bc / 第 1 页 / B3 区域：J2 GROVE_IO 符号及 IO2/IO1/VCC/GND 四个接点 |

## 系统结构

### Chain Mount

整页电路仅包含 J1、J2 两个 GROVE_IO 接口及四条直连网络，是无源 Chain 直通节点。

- 参数与网络：`connectors=J1,J2`；`active_components=none shown`；`nets=IO2,IO1,VCC_5V,GND`
- 证据：图 f5cebbb547bc / 第 1 页 / B2-C3：Chain Mount 框内仅 J1/J2 与四条连接线

## 核心器件

### 主动器件

原理图未绘制主控、协处理器、收发器、存储器或其他 IC。

- 参数与网络：`mcu=none shown`；`coprocessor=none shown`；`transceiver=none shown`；`ic=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / 全页器件检查：仅 J1/J2 连接器

## 电源

### VCC_5V

VCC_5V 在 J1 与 J2 之间直接贯通，图中没有稳压器、负载开关、保险丝或去耦电容。

- 参数与网络：`rail=VCC_5V`；`source=external through either connector`；`conversion=none shown`；`switch=none shown`；`fuse=none shown`；`decoupling=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / B2-B3：J1.VCC 到 J2.VCC 的 VCC_5V 直线，无串并联器件

## 接口

### J1 GROVE_IO

J1 的四个接点从上到下标注 IO2、IO1、VCC、GND；VCC 接点使用网络名 VCC_5V。

- 参数与网络：`contact_1_label=IO2`；`contact_2_label=IO1`；`contact_3_label=VCC / VCC_5V`；`contact_4_label=GND`；`pin_numbers=not printed`
- 证据：图 f5cebbb547bc / 第 1 页 / B2：J1 符号自上而下 IO2、IO1、VCC、GND

### J2 GROVE_IO

J2 的四个接点从上到下标注 IO2、IO1、VCC、GND；VCC 接点使用网络名 VCC_5V。

- 参数与网络：`contact_1_label=IO2`；`contact_2_label=IO1`；`contact_3_label=VCC / VCC_5V`；`contact_4_label=GND`；`pin_numbers=not printed`
- 证据：图 f5cebbb547bc / 第 1 页 / B3：J2 符号自上而下 IO2、IO1、VCC、GND

## 总线

### IO1/IO2 总线能力

原理图仅定义 IO1/IO2 网络名，没有指定 I2C、UART、SPI 或其他协议；由于两线直通，协议由链路两端设备决定。

- 参数与网络：`signal_names=IO1,IO2`；`protocol=not specified on schematic`；`electrical_path=transparent pass-through`
- 证据：图 f5cebbb547bc / 第 1 页 / B2-B3：信号仅标 IO1/IO2，无协议或方向标注

## GPIO 与控制信号

### IO1/IO2

IO1 与 IO2 均为端到端铜线直通，图中没有缓冲、反相、电平转换、上拉或下拉器件。

- 参数与网络：`io1=direct`；`io2=direct`；`buffer=none shown`；`level_shifter=none shown`；`pull_resistors=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / B2-B3：IO1/IO2 水平连线中无器件

## 时钟

### 时钟与复位

原理图没有晶振、时钟网络、复位网络、BOOT 或使能信号。

- 参数与网络：`clock=none shown`；`crystal=none shown`；`reset=none shown`；`boot=none shown`；`enable=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / 全页网络检查：仅 IO1/IO2/VCC_5V/GND

## 保护电路

### 接口保护

J1/J2 的 IO1、IO2、VCC_5V 与 GND 上均未绘制 ESD、TVS、限流或反接保护器件。

- 参数与网络：`esd=none shown`；`tvs=none shown`；`current_limit=none shown`；`reverse_protection=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / Chain Mount 框内全部电路，无保护器件符号

## 关键网络

### J1-J2 直通网络

J1.IO2 直连 J2.IO2，J1.IO1 直连 J2.IO1，两个 VCC 接点同接 VCC_5V，两个 GND 接点同接 GND。

- 参数与网络：`io2=J1.IO2-J2.IO2`；`io1=J1.IO1-J2.IO1`；`power=J1.VCC-J2.VCC=VCC_5V`；`ground=J1.GND-J2.GND=GND`
- 证据：图 f5cebbb547bc / 第 1 页 / B2-B3：两连接器之间 IO2、IO1、VCC_5V、GND 四条水平直连线

## 存储

### 存储与内存

原理图未绘制 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash=none shown`；`eeprom=none shown`；`ram=none shown`；`sd=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / 全页器件检查：无存储器

## 其他事实

### 音频/传感器/射频/调试

原理图未绘制音频、传感器、模拟采样、射频或专用调试功能块。

- 参数与网络：`audio=none shown`；`sensor=none shown`；`analog=none shown`；`rf=none shown`；`debug=none shown`
- 证据：图 f5cebbb547bc / 第 1 页 / 全页器件与网络检查：仅无源四线直通

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Mount | `connectors=J1,J2`；`active_components=none shown`；`nets=IO2,IO1,VCC_5V,GND` |
| 接口 | J1 GROVE_IO | `contact_1_label=IO2`；`contact_2_label=IO1`；`contact_3_label=VCC / VCC_5V`；`contact_4_label=GND`；`pin_numbers=not printed` |
| 接口 | J2 GROVE_IO | `contact_1_label=IO2`；`contact_2_label=IO1`；`contact_3_label=VCC / VCC_5V`；`contact_4_label=GND`；`pin_numbers=not printed` |
| 关键网络 | J1-J2 直通网络 | `io2=J1.IO2-J2.IO2`；`io1=J1.IO1-J2.IO1`；`power=J1.VCC-J2.VCC=VCC_5V`；`ground=J1.GND-J2.GND=GND` |
| 电源 | VCC_5V | `rail=VCC_5V`；`source=external through either connector`；`conversion=none shown`；`switch=none shown`；`fuse=none shown`；`decoupling=none shown` |
| GPIO 与控制信号 | IO1/IO2 | `io1=direct`；`io2=direct`；`buffer=none shown`；`level_shifter=none shown`；`pull_resistors=none shown` |
| 总线 | IO1/IO2 总线能力 | `signal_names=IO1,IO2`；`protocol=not specified on schematic`；`electrical_path=transparent pass-through` |
| 保护电路 | 接口保护 | `esd=none shown`；`tvs=none shown`；`current_limit=none shown`；`reverse_protection=none shown` |
| 核心器件 | 主动器件 | `mcu=none shown`；`coprocessor=none shown`；`transceiver=none shown`；`ic=none shown` |
| 时钟 | 时钟与复位 | `clock=none shown`；`crystal=none shown`；`reset=none shown`；`boot=none shown`；`enable=none shown` |
| 存储 | 存储与内存 | `flash=none shown`；`eeprom=none shown`；`ram=none shown`；`sd=none shown` |
| 其他事实 | 音频/传感器/射频/调试 | `audio=none shown`；`sensor=none shown`；`analog=none shown`；`rf=none shown`；`debug=none shown` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f5cebbb547bcfcb576941a2113a076dddf5d8b5b2e2460abd353f8e3ea9a6e18` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1203/U211_Chain-Mount_SCH_Main_V1.0_20241122_2025_11_11_19_03_01_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Mount.md`

源文档 SHA-256：`84fa2df1139cb4225f35f0095348f2d96dac59afffa40c0f124d1b3ef78b24e0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
