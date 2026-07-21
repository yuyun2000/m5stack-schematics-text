# Grove Converter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Grove Converter |
| SKU | A162 |
| 产品 ID | `grove-converter-2257c4feeecf` |
| 源文档 | `zh_CN/accessory/Grove_Converter.md` |

## 概述

Grove Converter 将 M1、M2 和 Grove1 三个四针接口的 IO2、IO1、VCC_5V 与 GND 网络并联，形成无源三路扩展。USB1 Type-C 的 VBUS 经 F1 6V/2A 接入 VCC_5V，CC1 与 CC2 分别通过 5.1 kΩ 电阻下拉至 GND。USB D− 与 D+ 分别预留经 R3、R4 接入 IO2、IO1，但两个电阻均在图中标注 NC。

## 检索关键词

`Grove Converter`、`A162`、`M1`、`M2`、`Grove1`、`USB1`、`USB-C-SMD_TYPEC-303-ACP16`、`USB Type-C`、`VBUS`、`CC1`、`CC2`、`DN1`、`DN2`、`DP1`、`DP2`、`IO1`、`IO2`、`VCC_5V`、`GND`、`F1 6V/2A`、`R1 5.1K`、`R2 5.1K`、`R3 NC`、`R4 NC`、`Grove 三路扩展`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | 1x4P | 第一组 IO2、IO1、VCC_5V、GND 四针接口 | 图 1d93e8a4a8fd / 第 1 页 / 网格 B2，左侧 M1 1x4P，pin1-pin4 分别连接 IO2、IO1、VCC_5V、GND |
| M2 | 1x4P | 第二组 IO2、IO1、VCC_5V、GND 四针接口 | 图 1d93e8a4a8fd / 第 1 页 / 网格 B2，M1 右侧 M2 1x4P，pin1-pin4 分别连接 IO2、IO1、VCC_5V、GND |
| Grove1 | Grove | 第三组 IO2、IO1、VCC_5V、GND 四针 GROVE 接口 | 图 1d93e8a4a8fd / 第 1 页 / 网格 C2，Grove1 Grove，pin1-pin4 分别连接 IO2、IO1、VCC_5V、GND |
| USB1 | USB-C-SMD_TYPEC-303-ACP16 | 向 VCC_5V 注入 VBUS 并预留 D−/D+ 到 IO2/IO1 的 USB Type-C 接口 | 图 1d93e8a4a8fd / 第 1 页 / 网格 B2-B3，USB1 方框下方标注 USB-C-SMD_TYPEC-303-ACP16，含 VBUS、CC、SBU、DN、DP、GND |
| F1 | 6V/2A | USB1 VBUS 与 VCC_5V 之间的串联过流保护器件 | 图 1d93e8a4a8fd / 第 1 页 / 网格 B2-B3，USB1 VBUS 上方 F1，标注 6V/2A，另一端为 VCC_5V |

## 系统结构

### Grove Converter 连接架构

M1、M2、Grove1 三个四针接口共享 IO2、IO1、VCC_5V 和 GND；USB1 通过 F1 向 VCC_5V 提供 VBUS，并预留数据线到 IO2/IO1。

- 参数与网络：`parallel_connectors=M1,M2,Grove1`；`shared_nets=IO2,IO1,VCC_5V,GND`；`usb_connector=USB1`；`usb_power_path=USB1 VBUS -> F1 -> VCC_5V`；`optional_usb_data=D- -> R3 NC -> IO2,D+ -> R4 NC -> IO1`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 整页 B2-C3，M1/M2/Grove1 并联网与 USB1/F1/R3/R4 网络

## 电源

### USB VBUS 到 VCC_5V

USB1 VBUS 经 F1 串联后连接 VCC_5V，F1 标注 6V/2A。

- 参数与网络：`source=USB1 VBUS`；`protection=F1 6V/2A`；`destination=VCC_5V`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-B3，USB1 VBUS 上方至 F1 6V/2A 和 VCC_5V 的连线

### VCC_5V 三路分配

VCC_5V 网络同时连接 M1 pin3、M2 pin3、Grove1 pin3 和 F1。

- 参数与网络：`rail=VCC_5V`；`endpoints=M1 pin3,M2 pin3,Grove1 pin3,F1`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-C2，M1/M2/Grove1 pin3 与 F1 端使用的 VCC_5V 同名网络

### GND 公共网络

GND 网络同时连接 M1 pin4、M2 pin4、Grove1 pin4、USB1 GND 以及 R1/R2 下端。

- 参数与网络：`rail=GND`；`endpoints=M1 pin4,M2 pin4,Grove1 pin4,USB1 GND,R1,R2`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-C3，所有 GND 符号及 M1/M2/Grove1/USB1/R1/R2 连接

## 接口

### M1 四针接口

M1 pin1 连接 IO2，pin2 连接 IO1，pin3 连接 VCC_5V，pin4 连接 GND。

- 参数与网络：`reference=M1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2，M1 pin1-pin4 与四条网络标注

### M2 四针接口

M2 pin1 连接 IO2，pin2 连接 IO1，pin3 连接 VCC_5V，pin4 连接 GND。

- 参数与网络：`reference=M2`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2，M2 pin1-pin4 与四条网络标注

### Grove1 四针接口

Grove1 pin1 连接 IO2，pin2 连接 IO1，pin3 连接 VCC_5V，pin4 连接 GND。

- 参数与网络：`reference=Grove1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 C2，Grove1 pin1-pin4 与 IO2/IO1/VCC/GND 标注

### USB1 Type-C 引脚用途

USB1 使用 VBUS、CC1、CC2、DN1、DN2、DP1、DP2 和 GND；SBU1 与 SBU2 在图中未连接。

- 参数与网络：`reference=USB1`；`part_number=USB-C-SMD_TYPEC-303-ACP16`；`used_pins=VBUS,CC1,CC2,DN1,DN2,DP1,DP2,GND`；`unconnected_pins=SBU1,SBU2`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-B3，USB1 符号各引脚连线，B8/A8 SBU2/SBU1 无外部连线

### USB Type-C CC 下拉

USB1 CC2 的 B5 引脚通过 R1 5.1 kΩ 连接 GND，CC1 的 A5 引脚通过 R2 5.1 kΩ 连接 GND。

- 参数与网络：`cc2_path=USB1 B5/CC2 -> R1 5.1kΩ -> GND`；`cc1_path=USB1 A5/CC1 -> R2 5.1kΩ -> GND`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-C2，USB1 B5 CC2/A5 CC1 左侧 R1/R2 5.1K 到 GND

### USB D− 到 IO2 预留连接

USB1 DN2 pin B7 与 DN1 pin A7 并联后通过 R3 连接 IO2，R3 的器件值标注 NC。

- 参数与网络：`usb_pins=B7 DN2,A7 DN1`；`series_option=R3 NC`；`destination=IO2`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B3，USB1 B7/A7 DN2/DN1 汇合节点、R3 NC 与 IO2

### USB D+ 到 IO1 预留连接

USB1 DP1 pin A6 与 DP2 pin B6 并联后通过 R4 连接 IO1，R4 的器件值标注 NC。

- 参数与网络：`usb_pins=A6 DP1,B6 DP2`；`series_option=R4 NC`；`destination=IO1`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B3，USB1 A6/B6 DP1/DP2 汇合节点、R4 NC 与 IO1

## 保护电路

### F1 VBUS 过流保护

F1 串联在 USB1 VBUS 与 VCC_5V 之间，器件标注为 6V/2A。

- 参数与网络：`reference=F1`；`rating=6V/2A`；`protected_path=USB1 VBUS -> VCC_5V`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2，F1 6V/2A 垂直串接 VCC_5V 与 USB1 VBUS

## 关键网络

### 三组 Grove 网络并联

M1、M2、Grove1 的同号引脚分别共享 IO2、IO1、VCC_5V 和 GND 网络。

- 参数与网络：`pin1_net=IO2`；`pin2_net=IO1`；`pin3_net=VCC_5V`；`pin4_net=GND`；`connectors=M1,M2,Grove1`
- 证据：图 1d93e8a4a8fd / 第 1 页 / 网格 B2-C2，三组接口重复使用的 IO2、IO1、VCC_5V、GND 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Grove Converter 连接架构 | `parallel_connectors=M1,M2,Grove1`；`shared_nets=IO2,IO1,VCC_5V,GND`；`usb_connector=USB1`；`usb_power_path=USB1 VBUS -> F1 -> VCC_5V`；`optional_usb_data=D- -> R3 NC -> IO2,D+ -> R4 NC -> IO1` |
| 接口 | M1 四针接口 | `reference=M1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND` |
| 接口 | M2 四针接口 | `reference=M2`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND` |
| 接口 | Grove1 四针接口 | `reference=Grove1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND` |
| 关键网络 | 三组 Grove 网络并联 | `pin1_net=IO2`；`pin2_net=IO1`；`pin3_net=VCC_5V`；`pin4_net=GND`；`connectors=M1,M2,Grove1` |
| 接口 | USB1 Type-C 引脚用途 | `reference=USB1`；`part_number=USB-C-SMD_TYPEC-303-ACP16`；`used_pins=VBUS,CC1,CC2,DN1,DN2,DP1,DP2,GND`；`unconnected_pins=SBU1,SBU2` |
| 电源 | USB VBUS 到 VCC_5V | `source=USB1 VBUS`；`protection=F1 6V/2A`；`destination=VCC_5V` |
| 保护电路 | F1 VBUS 过流保护 | `reference=F1`；`rating=6V/2A`；`protected_path=USB1 VBUS -> VCC_5V` |
| 接口 | USB Type-C CC 下拉 | `cc2_path=USB1 B5/CC2 -> R1 5.1kΩ -> GND`；`cc1_path=USB1 A5/CC1 -> R2 5.1kΩ -> GND` |
| 接口 | USB D− 到 IO2 预留连接 | `usb_pins=B7 DN2,A7 DN1`；`series_option=R3 NC`；`destination=IO2` |
| 接口 | USB D+ 到 IO1 预留连接 | `usb_pins=A6 DP1,B6 DP2`；`series_option=R4 NC`；`destination=IO1` |
| 电源 | VCC_5V 三路分配 | `rail=VCC_5V`；`endpoints=M1 pin3,M2 pin3,Grove1 pin3,F1` |
| 电源 | GND 公共网络 | `rail=GND`；`endpoints=M1 pin4,M2 pin4,Grove1 pin4,USB1 GND,R1,R2` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1d93e8a4a8fd0a7adeeb266cbe628daa992a21bcf7bbc3cb771f5b02a72564f4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1194/A162_Grove-Converter_SCH_V1.0_20250805_2025_11_19_12_22_36_page_01.png` |

---

源文档：`zh_CN/accessory/Grove_Converter.md`

源文档 SHA-256：`f557d589a4033f9d5eb86dcba2f68d869fa63c7c415657c7a490ce5e70bf01c2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
