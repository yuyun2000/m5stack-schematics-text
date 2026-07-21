# Grove to USBC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Grove to USBC |
| SKU | A140 |
| 产品 ID | `grove-to-usbc-a6f4ed3b21ac` |
| 源文档 | `zh_CN/accessory/Grove2USB-C.md` |

## 概述

Grove to USBC 是一块无源 USB Type-C 到 Grove 四针转接板。J2 的 USB D+、D-、VBUS 和 GND 分别直接映射到 J1 的 IO1、IO2、5V 和 GND，CC1 与 CC2 各通过 5.1kΩ 电阻下拉到地。原理图未配置 USB 数据线串联器件、ESD 防护、保险丝、电平转换器或主动控制芯片。

## 检索关键词

`Grove to USBC`、`Grove2USB-C`、`A140`、`USB Type-C`、`TYPE-C 16P`、`Grove`、`USB_DP`、`USB_DM`、`D+`、`D-`、`IO1`、`IO2`、`VCC`、`5V`、`CC1`、`CC2`、`5.1K`、`R1`、`R2`、`无源转接板`、`USB CDC`、`USB 下载`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE | 四针 Grove 接口，引出 IO2、IO1、5V 和 GND | 图 212dad2adaa0 / 第 1 页 / 网格 2B-3C，J1 GROVE 的 IO2=USB_DM、IO1=USB_DP、5V=VCC、GND=GND |
| J2 | TYPE-C 16P | USB Type-C 设备侧连接器 | 图 212dad2adaa0 / 第 1 页 / 网格 2B，J2 TYPE-C 16P，VCC、CC1、CC2、DP1、DP2、DN1、DN2、GND 和 SHELL |
| R1 | 5.1K | USB Type-C CC1 下拉电阻 | 图 212dad2adaa0 / 第 1 页 / 网格 1B-2C，J2 CC1 pin A5 经 R1 5.1K 接 GND |
| R2 | 5.1K | USB Type-C CC2 下拉电阻 | 图 212dad2adaa0 / 第 1 页 / 网格 1B-2C，J2 CC2 pin B5 经 R2 5.1K 接 GND |

## 系统结构

### Grove 到 USB-C 无源转接架构

电路只包含 J1 Grove、J2 USB Type-C 和两只 CC 下拉电阻，USB 数据、电源和地线在两个连接器之间直接映射。

- 参数与网络：`active_components=0`；`connectors=J1 GROVE, J2 TYPE-C 16P`；`resistors=R1 5.1K, R2 5.1K`；`topology=passive_direct_mapping`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 1B-3C，完整原理图仅有 J1、J2、R1、R2

## 电源

### USB VBUS 到 Grove 5V

J2 VCC 通过 VCC 网络直接连接 J1 5V，引线上未配置保险丝、二极管、负载开关或稳压器。

- 参数与网络：`source=J2 VCC`；`destination=J1 5V`；`net=VCC`；`fuse=null`；`switch=null`；`regulator=null`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 2B-3C，J2 VCC 与 J1 5V 均标注 VCC 且无中间器件

## 接口

### J1 Grove 引脚映射

J1 IO2 连接 USB_DM，IO1 连接 USB_DP，5V 连接 VCC，GND 连接公共 GND。

- 参数与网络：`connector=J1 GROVE`；`io2=USB_DM`；`io1=USB_DP`；`power=VCC`；`ground=GND`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 2B-3C，J1 GROVE 四个引脚右侧网络名

### J2 USB Type-C 引脚并联

J2 DP1 pin A6 与 DP2 pin B6 并接 USB_DP，DN1 pin A7 与 DN2 pin B7 并接 USB_DM；VCC 接 VCC，GND 与 SHELL 均接 GND。

- 参数与网络：`connector=J2 TYPE-C 16P`；`dp_pins=A6,B6`；`dp_net=USB_DP`；`dm_pins=A7,B7`；`dm_net=USB_DM`；`power_net=VCC`；`grounded=GND,SHELL`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 2B，J2 DP1/DP2、DN1/DN2、VCC、GND、SHELL 连接

### USB Type-C CC 下拉配置

J2 CC1 pin A5 通过 R1 5.1K 接 GND，CC2 pin B5 通过 R2 5.1K 接 GND。

- 参数与网络：`cc1=A5 -> R1 5.1K -> GND`；`cc2=B5 -> R2 5.1K -> GND`；`resistance_ohm=5100`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 1B-2C，J2 CC1/CC2、R1/R2 5.1K 与 GND

## 总线

### USB D+/D- 直连路径

USB_DP 从 J2 DP1/DP2 直接连接 J1 IO1，USB_DM 从 J2 DN1/DN2 直接连接 J1 IO2，中间没有串联电阻、共模扼流圈或收发器。

- 参数与网络：`positive_path=J2 DP1/DP2 -> USB_DP -> J1 IO1`；`negative_path=J2 DN1/DN2 -> USB_DM -> J1 IO2`；`series_components=null`；`transceiver=null`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 2B-3C，USB_DP/USB_DM 网络在 J2 与 J1 之间无其他器件

## 保护电路

### 接口保护与信号调理

完整原理图未显示 USB_DP、USB_DM、VCC 或 Grove 引脚上的 ESD/TVS、过流保护、滤波、缓冲或电平转换器件。

- 参数与网络：`esd_protection=null`；`overcurrent_protection=null`；`data_filter=null`；`level_shifter=null`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 1A-4D，完整单页原理图除 J1、J2、R1、R2 外无其他器件

## 关键网络

### 公共地与 USB 外壳

J2 GND、J2 SHELL、R1/R2 下端和 J1 GND 共用同一 GND 网络。

- 参数与网络：`net=GND`；`members=J2 GND, J2 SHELL, R1 low side, R2 low side, J1 GND`
- 证据：图 212dad2adaa0 / 第 1 页 / 网格 1B-3C，各地符号与 J1/J2/R1/R2 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Grove 到 USB-C 无源转接架构 | `active_components=0`；`connectors=J1 GROVE, J2 TYPE-C 16P`；`resistors=R1 5.1K, R2 5.1K`；`topology=passive_direct_mapping` |
| 接口 | J1 Grove 引脚映射 | `connector=J1 GROVE`；`io2=USB_DM`；`io1=USB_DP`；`power=VCC`；`ground=GND` |
| 接口 | J2 USB Type-C 引脚并联 | `connector=J2 TYPE-C 16P`；`dp_pins=A6,B6`；`dp_net=USB_DP`；`dm_pins=A7,B7`；`dm_net=USB_DM`；`power_net=VCC`；`grounded=GND,SHELL` |
| 总线 | USB D+/D- 直连路径 | `positive_path=J2 DP1/DP2 -> USB_DP -> J1 IO1`；`negative_path=J2 DN1/DN2 -> USB_DM -> J1 IO2`；`series_components=null`；`transceiver=null` |
| 电源 | USB VBUS 到 Grove 5V | `source=J2 VCC`；`destination=J1 5V`；`net=VCC`；`fuse=null`；`switch=null`；`regulator=null` |
| 接口 | USB Type-C CC 下拉配置 | `cc1=A5 -> R1 5.1K -> GND`；`cc2=B5 -> R2 5.1K -> GND`；`resistance_ohm=5100` |
| 关键网络 | 公共地与 USB 外壳 | `net=GND`；`members=J2 GND, J2 SHELL, R1 low side, R2 low side, J1 GND` |
| 保护电路 | 接口保护与信号调理 | `esd_protection=null`；`overcurrent_protection=null`；`data_filter=null`；`level_shifter=null` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `212dad2adaa0d7ed4f370fc58e7d8e0d3228ef6f32b78e1b9faa71e1f74a78fb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/537/SCH_Grove2USB-C_V1.0_sch_01.png` |

---

源文档：`zh_CN/accessory/Grove2USB-C.md`

源文档 SHA-256：`5888417129a92e3cb95a4d138df16a145fb8f3f29160fe8dcbf84d380f6be499`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
