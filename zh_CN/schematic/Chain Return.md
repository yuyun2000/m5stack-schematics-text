# Chain Return 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Return |
| SKU | A154 |
| 产品 ID | `chain-return-0ee11469fa7b` |
| 源文档 | `zh_CN/accessory/converter/Chain_Return.md` |

## 概述

Chain Return 是由两个 GROVE_IO 四针接口 J1 和 J2 构成的无源直通连接器。两个接口的 pin1 至 pin4 分别共享 IO2、IO1、VCC_5V 和 GND 网络，其中 IO2 标注 SCL/RX 功能别名，IO1 标注 SDA/TX 功能别名。原理图未包含主动器件、电源转换或保护器件。

## 检索关键词

`Chain Return`、`A154`、`J1`、`J2`、`GROVE_IO`、`HY2.0-4P`、`IO1`、`IO2`、`SCL/RX`、`SDA/TX`、`VCC_5V`、`GND`、`Grove 直通`、`四针接口`、`无源转接`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 第一组 IO2、IO1、VCC_5V、GND 四针接口 | 图 45197a27e442 / 第 1 页 / 网格 B2，顶部 J1 GROVE_IO，左侧 pin1-pin4 连接 IO2、IO1、VCC_5V、GND |
| J2 | GROVE_IO | 第二组 IO2、IO1、VCC_5V、GND 四针接口 | 图 45197a27e442 / 第 1 页 / 网格 C2，底部 J2 GROVE_IO，左侧 pin1-pin4 连接 IO2、IO1、VCC_5V、GND |

## 系统结构

### Chain Return 无源直通结构

整页电路仅显示 J1 和 J2 两个 GROVE_IO 接口，两者通过 IO2、IO1、VCC_5V 和 GND 四个同名网络逐针贯通。

- 参数与网络：`connector_a=J1 GROVE_IO`；`connector_b=J2 GROVE_IO`；`shared_nets=IO2,IO1,VCC_5V,GND`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2-C2，J1 与 J2 的全部四条同名网络

## 电源

### VCC_5V 电源直通

J1 pin3 与 J2 pin3 共享 VCC_5V 网络。

- 参数与网络：`net=VCC_5V`；`endpoint_a=J1 pin3`；`endpoint_b=J2 pin3`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2-C2，J1/J2 pin3 的红色 VCC_5V 网络标注

### GND 直通

J1 pin4 与 J2 pin4 共享 GND 网络。

- 参数与网络：`net=GND`；`endpoint_a=J1 pin4`；`endpoint_b=J2 pin4`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2-C2，J1/J2 pin4 的 GND 符号与同名网络

## 接口

### J1 GROVE_IO 引脚

J1 pin1 连接 IO2，pin2 连接 IO1，pin3 连接 VCC_5V，pin4 连接 GND。

- 参数与网络：`reference=J1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2，J1 左侧 pin1-pin4 与右侧 IO2/IO1/VCC/GND 标注

### J2 GROVE_IO 引脚

J2 pin1 连接 IO2，pin2 连接 IO1，pin3 连接 VCC_5V，pin4 连接 GND。

- 参数与网络：`reference=J2`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND`
- 证据：图 45197a27e442 / 第 1 页 / 网格 C2，J2 左侧 pin1-pin4 与右侧 IO2/IO1/VCC/GND 标注

## 关键网络

### IO2 信号直通

J1 pin1 与 J2 pin1 共享 IO2 网络，IO2 左侧功能标注为 SCL/RX。

- 参数与网络：`net=IO2`；`alias=SCL/RX`；`endpoint_a=J1 pin1`；`endpoint_b=J2 pin1`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2-C2，J1/J2 pin1 的 IO2 网络及蓝色 SCL/RX 标注

### IO1 信号直通

J1 pin2 与 J2 pin2 共享 IO1 网络，IO1 左侧功能标注为 SDA/TX。

- 参数与网络：`net=IO1`；`alias=SDA/TX`；`endpoint_a=J1 pin2`；`endpoint_b=J2 pin2`
- 证据：图 45197a27e442 / 第 1 页 / 网格 B2-C2，J1/J2 pin2 的 IO1 网络及蓝色 SDA/TX 标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Return 无源直通结构 | `connector_a=J1 GROVE_IO`；`connector_b=J2 GROVE_IO`；`shared_nets=IO2,IO1,VCC_5V,GND` |
| 接口 | J1 GROVE_IO 引脚 | `reference=J1`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND` |
| 接口 | J2 GROVE_IO 引脚 | `reference=J2`；`pinout=1:IO2,2:IO1,3:VCC_5V,4:GND` |
| 关键网络 | IO2 信号直通 | `net=IO2`；`alias=SCL/RX`；`endpoint_a=J1 pin1`；`endpoint_b=J2 pin1` |
| 关键网络 | IO1 信号直通 | `net=IO1`；`alias=SDA/TX`；`endpoint_a=J1 pin2`；`endpoint_b=J2 pin2` |
| 电源 | VCC_5V 电源直通 | `net=VCC_5V`；`endpoint_a=J1 pin3`；`endpoint_b=J2 pin3` |
| 电源 | GND 直通 | `net=GND`；`endpoint_a=J1 pin4`；`endpoint_b=J2 pin4` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `45197a27e442451af9d8d05716e319755be7f9774af6a49e43d91bd584c6909a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1153/Chain_Return_Schematics.png` |

---

源文档：`zh_CN/accessory/converter/Chain_Return.md`

源文档 SHA-256：`24996ec5dab0541c596077e1a995635f12d8b099347dda3544074f08505768b6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
