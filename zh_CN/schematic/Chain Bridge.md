# Chain Bridge 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Bridge |
| SKU | A155 |
| 产品 ID | `chain-bridge-989d2a56d4ae` |
| 源文档 | `zh_CN/accessory/converter/Chain_Bridge.md` |

## 概述

Chain Bridge 是由 J1 和 J2 两只 GROVE_IO 4 Pin 连接器组成的无源直通转接电路。两端的 1~4 脚分别通过同名网络 IO2、IO1、VCC_5V、GND 直接相连。IO2 同时标注 SCL/RX，IO1 同时标注 SDA/TX，表明相同物理通道可承载相应的 I2C 或串行信号名称。

## 检索关键词

`Chain Bridge`、`A155`、`GROVE_IO`、`HY2.0-4P`、`J1`、`J2`、`IO1`、`IO2`、`SCL`、`SDA`、`RX`、`TX`、`VCC_5V`、`GND`、`I2C`、`UART`、`4 Pin`、`pass-through`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 第一只 4 Pin Grove/Chain 连接器，引出 IO2、IO1、VCC_5V、GND | 图 2a94bdfb31a9 / 第 1 页 / B2 区域 J1：GROVE_IO 符号，1~4 脚对应 IO2、IO1、VCC、GND |
| J2 | GROVE_IO | 第二只 4 Pin Grove/Chain 连接器，引出 IO2、IO1、VCC_5V、GND | 图 2a94bdfb31a9 / 第 1 页 / C2 区域 J2：GROVE_IO 符号，1~4 脚对应 IO2、IO1、VCC、GND |

## 系统结构

### Chain Bridge

原理图只绘制 J1 和 J2 两只 GROVE_IO 连接器，四个通道均通过同名网络直接桥接。

- 参数与网络：`connector_1=J1 GROVE_IO`；`connector_2=J2 GROVE_IO`；`channels=IO2,IO1,VCC_5V,GND`；`active_component=null`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2-C2 区域：整页仅有 J1、J2 及 IO2/IO1/VCC_5V/GND 同名网络

## 电源

### VCC_5V

J1.3 与 J2.3 通过 VCC_5V 同名网络直接相连。

- 参数与网络：`endpoint_1=J1.3 VCC`；`endpoint_2=J2.3 VCC`；`network=VCC_5V`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2 与 C2 区域：J1.3/J2.3 左侧均标注 VCC_5V

### GND

J1.4 与 J2.4 通过 GND 同名网络直接相连。

- 参数与网络：`endpoint_1=J1.4 GND`；`endpoint_2=J2.4 GND`；`network=GND`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2 与 C2 区域：J1.4/J2.4 均连接 GND 符号

## 接口

### J1 GROVE_IO

J1 的 1 脚连接 IO2，2 脚连接 IO1，3 脚连接 VCC_5V，4 脚连接 GND。

- 参数与网络：`pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2 区域 J1：1/2/3/4 脚数字与 IO2/IO1/VCC/GND 字段及左侧网络

### J2 GROVE_IO

J2 的 1 脚连接 IO2，2 脚连接 IO1，3 脚连接 VCC_5V，4 脚连接 GND。

- 参数与网络：`pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND`
- 证据：图 2a94bdfb31a9 / 第 1 页 / C2 区域 J2：1/2/3/4 脚数字与 IO2/IO1/VCC/GND 字段及左侧网络

## 总线

### IO1/IO2 信号别名

原理图将 IO2 标注为 SCL/RX，将 IO1 标注为 SDA/TX；连接器之间没有中间方向控制器件。

- 参数与网络：`IO2=SCL/RX`；`IO1=SDA/TX`；`direction_control=null`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2-C2 区域 J1/J2 左侧：SCL/RX、SDA/TX 与 IO2/IO1 成对标注，整页无其他器件

## 关键网络

### IO2

J1.1 与 J2.1 通过 IO2 同名网络直接相连，该网络旁同时标注 SCL/RX。

- 参数与网络：`endpoint_1=J1.1`；`endpoint_2=J2.1`；`network=IO2`；`aliases=SCL/RX`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2 与 C2 区域：J1.1/J2.1 均标注 IO2，左侧均标注 SCL/RX

### IO1

J1.2 与 J2.2 通过 IO1 同名网络直接相连，该网络旁同时标注 SDA/TX。

- 参数与网络：`endpoint_1=J1.2`；`endpoint_2=J2.2`；`network=IO1`；`aliases=SDA/TX`
- 证据：图 2a94bdfb31a9 / 第 1 页 / B2 与 C2 区域：J1.2/J2.2 均标注 IO1，左侧均标注 SDA/TX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Bridge | `connector_1=J1 GROVE_IO`；`connector_2=J2 GROVE_IO`；`channels=IO2,IO1,VCC_5V,GND`；`active_component=null` |
| 接口 | J1 GROVE_IO | `pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND` |
| 接口 | J2 GROVE_IO | `pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND` |
| 关键网络 | IO2 | `endpoint_1=J1.1`；`endpoint_2=J2.1`；`network=IO2`；`aliases=SCL/RX` |
| 关键网络 | IO1 | `endpoint_1=J1.2`；`endpoint_2=J2.2`；`network=IO1`；`aliases=SDA/TX` |
| 电源 | VCC_5V | `endpoint_1=J1.3 VCC`；`endpoint_2=J2.3 VCC`；`network=VCC_5V` |
| 电源 | GND | `endpoint_1=J1.4 GND`；`endpoint_2=J2.4 GND`；`network=GND` |
| 总线 | IO1/IO2 信号别名 | `IO2=SCL/RX`；`IO1=SDA/TX`；`direction_control=null` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2a94bdfb31a9a78bbe6e2889b6b10078fb0bf1d1998d5911c080d2ed2f64c66f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1154/Chain_Bridge_Schematics.png` |

---

源文档：`zh_CN/accessory/converter/Chain_Bridge.md`

源文档 SHA-256：`3b9c7eb695c70f47952a1c7481ed96a2a7b40c952bf13c1c1d741af779dff912`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
