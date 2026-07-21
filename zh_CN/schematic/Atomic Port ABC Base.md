# Atomic Port ABC Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Port ABC Base |
| SKU | A130 |
| 产品 ID | `atomic-port-abc-base-f732530bbecb` |
| 源文档 | `zh_CN/atom/AtomPortABC.md` |

## 概述

Atomic Port ABC Base 将 Atom 的 G21、G25、G22、G19、G23、G33、5V、3V3 和 GND 复制到两组 Atom 插座，并通过 J3 汇总六个 GPIO、两路 5V 和四路 GND。第二张原理图把这些信号分配成三组 Grove：I2C 使用 G21/G25，GPIO 使用 G33/G23，UART 使用 G19/G22，三组均使用 5V/GND。六个 GPIO 使用 SD03 对地保护，5V 使用 SD05 对地保护，5V 和 3V3 另有电容去耦。

## 检索关键词

`Atomic Port ABC Base`、`A130`、`AtomPortABC`、`Grove I2C`、`Grove GPIO`、`Grove UART`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`、`5V`、`3V3`、`GND`、`J3 Grove_3`、`J1 J4 Atom_J`、`J2 J5 Atom_J1`、`SD03`、`SD05`、`ESD protection`、`Grove1`、`Grove2`、`Grove3`、`12-pin interconnect`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | Atomic | Atom 九针核心接口，将六个 GPIO 和三路电源/地接入底板 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，U1 Atomic，left pins1-4 G21/G25/5V/GND，right pins5-9 G33/G23/G19/G22/3V3 |
| J1,J4 | Atom_J | 两组并联的 3V3、G22、G19、G23、G33 五针 Atom 插座 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B3-B4，J1/J4 Atom_J 的 pin1 3V3、pin2 G22、pin3 G19、pin4 G23、pin5 G33 |
| J2,J5 | Atom_J1 | 两组并联的 G21、G25、5V、GND 四针 Atom 插座 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B1-B2，J2/J5 Atom_J1 的 pin1 G21、pin2 G25、pin3 5V、pin4 GND |
| J3 | Grove_3 | 把六个 GPIO、四路 GND 和两路 5V 汇总到 12 针板间接口 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 C3，J3 Grove_3 pin1-pin12 的 G25/G21/G33/G23/G19/G22/GNDx4/5Vx2 |
| Grove2 | I2C | G21、G25、5V、GND 四针 Grove 接口 | 图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 B2，Grove2 I2C，pin1 G21、pin2 G25、pin3 VCC/5V、pin4 GND |
| Grove3 | GPIO | G33、G23、5V、GND 四针 Grove 接口 | 图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 C2，Grove3 GPIO，pin1 G33、pin2 G23、pin3 VCC/5V、pin4 GND |
| Grove1 | UART | G19、G22、5V、GND 四针 Grove 接口 | 图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 C2，Grove1 UART，pin1 G19、pin2 G22、pin3 VCC/5V、pin4 GND |
| D1,D2,D4,D5,D6,D7 | SD03 | 六个 GPIO 到 GND 的单线保护器件 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，D1/D2 接 G21/G25，D4-D7 接 G22/G19/G23/G33，另一端共接 GND |
| D3 | SD05 | 5V 到 GND 的电源保护器件 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2，D3 SD05 连接 5V 与 GND |
| C1,C2,C3,C4 | 10uF / 0.1uF / 0.1uF / 0.1uF | 5V 与 3V3 电源去耦 | 图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，C1 10uF/C2-C3 0.1uF 连接 5V-GND，C4 0.1uF 连接 3V3-GND |

## 系统结构

### Atomic Port ABC Base 信号分配架构

U1 Atomic 的六个 GPIO 与 5V/GND/3V3 并联到双组 Atom 插座；六个 GPIO、5V 和 GND 再经 J3 12 针接口连接第二页的三组 Grove，分别标记为 I2C、GPIO 和 UART。

- 参数与网络：`atom_core=U1 Atomic`；`duplicate_headers=J1/J4 and J2/J5`；`interconnect=J3 Grove_3`；`I2C_port=Grove2 G21/G25`；`GPIO_port=Grove3 G33/G23`；`UART_port=Grove1 G19/G22`；`port_power=5V and GND`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 U1、J1/J2/J4/J5 与 J3 的完整信号汇总; 图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 Grove2/Grove3/Grove1 的 I2C/GPIO/UART 分配

## 电源

### 5V 与 3V3 去耦

C1 10uF、C2 0.1uF 和 C3 0.1uF 并联连接 5V 与 GND；C4 0.1uF 连接 3V3 与 GND。

- 参数与网络：`5V=C1 10uF, C2 0.1uF, C3 0.1uF`；`3V3=C4 0.1uF`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，C1-C3 的 5V-GND 与 C4 的 3V3-GND

## 接口

### U1 Atomic 九针映射

U1 left pin1=G21、pin2=G25、pin3=5V、pin4=GND；right pin5=G33、pin6=G23、pin7=G19、pin8=G22、pin9=3V3。

- 参数与网络：`pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND`；`pin5=G33`；`pin6=G23`；`pin7=G19`；`pin8=G22`；`pin9=3V3`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，U1 Atomic pin1-pin9 的编号与网络名

### 双组 Atom 插座并联映射

J2 与 J5 具有相同映射：pin1=G21、pin2=G25、pin3=5V、pin4=GND；J1 与 J4 具有相同映射：pin1=3V3、pin2=G22、pin3=G19、pin4=G23、pin5=G33。

- 参数与网络：`J2_J5=pin1 G21, pin2 G25, pin3 5V, pin4 GND`；`J1_J4=pin1 3V3, pin2 G22, pin3 G19, pin4 G23, pin5 G33`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B1-B4，J2/J5 与 J1/J4 到 U1 的并联线路

### J3 12 针板间接口

J3 pin1=G25、pin2=G21、pin3=G33、pin4=G23、pin5=G19、pin6=G22、pin7-pin10=GND、pin11-pin12=5V。

- 参数与网络：`pin1=G25`；`pin2=G21`；`pin3=G33`；`pin4=G23`；`pin5=G19`；`pin6=G22`；`pins7_10=GND`；`pins11_12=5V`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 C3，J3 Grove_3 pin1-pin12 标签

### Grove3 GPIO 接口

Grove3 标记为 GPIO，pin1=G33、pin2=G23、pin3=VCC/5V、pin4=GND。

- 参数与网络：`pin1=G33`；`pin2=G23`；`pin3=5V`；`pin4=GND`
- 证据：图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 C2，Grove3/GPIO 的 G33/G23/VCC/GND

## 总线

### Grove2 I2C 接口

Grove2 标记为 I2C，pin1=G21、pin2=G25、pin3=VCC/5V、pin4=GND。

- 参数与网络：`pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND`
- 证据：图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 B2，Grove2/I2C 的 G21/G25/VCC/GND

### Grove1 UART 接口

Grove1 标记为 UART，pin1=G19、pin2=G22、pin3=VCC/5V、pin4=GND。

- 参数与网络：`pin1=G19`；`pin2=G22`；`pin3=5V`；`pin4=GND`
- 证据：图 ffc6485b6688 / 第 1 页 / 资源 2 第 1 页 C2，Grove1/UART 的 G19/G22/VCC/GND

## 保护电路

### 六路 GPIO SD03 对地保护

D1/D2/D4/D5/D6/D7 均为 SD03，分别连接 G21、G25、G22、G19、G23、G33 与公共 GND。

- 参数与网络：`G21=D1 SD03 to GND`；`G25=D2 SD03 to GND`；`G22=D4 SD03 to GND`；`G19=D5 SD03 to GND`；`G23=D6 SD03 to GND`；`G33=D7 SD03 to GND`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2-B3，D1/D2/D4-D7 的上端信号线路和下端 GND 总线

### 5V SD05 对地保护

D3 SD05 连接在 5V 与 GND 之间。

- 参数与网络：`device=D3 SD05`；`rail=5V`；`return=GND`
- 证据：图 817fd06803d4 / 第 1 页 / 资源 1 第 1 页 B2，D3 SD05 的 5V-GND 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Port ABC Base 信号分配架构 | `atom_core=U1 Atomic`；`duplicate_headers=J1/J4 and J2/J5`；`interconnect=J3 Grove_3`；`I2C_port=Grove2 G21/G25`；`GPIO_port=Grove3 G33/G23`；`UART_port=Grove1 G19/G22`；`port_power=5V and GND` |
| 接口 | U1 Atomic 九针映射 | `pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND`；`pin5=G33`；`pin6=G23`；`pin7=G19`；`pin8=G22`；`pin9=3V3` |
| 接口 | 双组 Atom 插座并联映射 | `J2_J5=pin1 G21, pin2 G25, pin3 5V, pin4 GND`；`J1_J4=pin1 3V3, pin2 G22, pin3 G19, pin4 G23, pin5 G33` |
| 接口 | J3 12 针板间接口 | `pin1=G25`；`pin2=G21`；`pin3=G33`；`pin4=G23`；`pin5=G19`；`pin6=G22`；`pins7_10=GND`；`pins11_12=5V` |
| 保护电路 | 六路 GPIO SD03 对地保护 | `G21=D1 SD03 to GND`；`G25=D2 SD03 to GND`；`G22=D4 SD03 to GND`；`G19=D5 SD03 to GND`；`G23=D6 SD03 to GND`；`G33=D7 SD03 to GND` |
| 保护电路 | 5V SD05 对地保护 | `device=D3 SD05`；`rail=5V`；`return=GND` |
| 电源 | 5V 与 3V3 去耦 | `5V=C1 10uF, C2 0.1uF, C3 0.1uF`；`3V3=C4 0.1uF` |
| 总线 | Grove2 I2C 接口 | `pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND` |
| 接口 | Grove3 GPIO 接口 | `pin1=G33`；`pin2=G23`；`pin3=5V`；`pin4=GND` |
| 总线 | Grove1 UART 接口 | `pin1=G19`；`pin2=G22`；`pin3=5V`；`pin4=GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `817fd06803d49d5fb0b78b76d269b11d1f50639e1e2fc7e4dd5abd54e3689a5f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/535/Sch_AtomPortABC_01.png` |
| 2 | 1 | `ffc6485b6688396b15ae9f1c9989e05c78d75cf4cf4df4f1c3dcca515e0ca4af` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/535/Sch_AtomPortABC_02.png` |

---

源文档：`zh_CN/atom/AtomPortABC.md`

源文档 SHA-256：`d8c9e17b12770c1312992cd6b40bb181bfe8f44a0628da4386d468c56c3c8aec`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
