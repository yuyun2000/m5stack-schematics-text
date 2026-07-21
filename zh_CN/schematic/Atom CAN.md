# Atom CAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom CAN |
| SKU | K057 |
| 产品 ID | `atom-can-8022ccbcf601` |
| 源文档 | `zh_CN/atom/atom_can.md` |

## 概述

Atom CAN 通过 U4 CA-IS3050G 将 Atom 主控侧 CAN_TX/CAN_RX 与隔离侧 CANH/CANL 连接，U2 B0505S-1W 同时把 +5VIN/GND 隔离为 +S5V/SGND。CANH/CANL 输出经过串联保险、P0080TA、PESD5V0L1BA 和 SMD4532-075 多级保护后到达 J1，隔离地 SGND 通过 R4/C10 耦合到 SHIELD。主控侧由 P1/P2 引入 +3.3V、+5VIN、CAN_TX/CAN_RX 和 GND，当前原理图未画出 120Ω CAN 终端电阻。

## 检索关键词

`Atom CAN`、`K057`、`CA-IS3050G`、`B0505S-1W`、`CAN`、`CANH`、`CANL`、`CAN_H`、`CAN_L`、`CAN_TX`、`CAN_RX`、`+3.3V`、`+5VIN`、`+S5V`、`GND`、`SGND`、`SHIELD`、`galvanic isolation`、`P0080TA`、`PESD5V0L1BA`、`SMD4532-075`、`J/K-NSMD0010`、`ZMM5V1`、`HDR_4P_3.96`、`1Mbps`、`110 nodes`、`common mode -12V to 12V`、`CAN protection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | CA-IS3050G | 3.3V 主控侧与 +S5V CAN 总线侧之间的隔离 CAN 收发器 | 图 14471ad2d57d / 第 1 页 / 第 1 页左中 U4 CA-IS3050G，VCC1/RXD/TXD/GND1 与 VCC2/CANH/CANL/GND2 |
| U2 | B0505S-1W | 将主控侧 +5VIN/GND 转换为隔离侧 +S5V/SGND 的 5V-5V 隔离电源模块 | 图 14471ad2d57d / 第 1 页 / 第 1 页左上 U2 B0505S-1W，+Vin/-Vin 与 +Vout/-Vout、+5VIN/GND/+S5V/SGND |
| J1 | HDR_4P_3.96 | CAN_H、CAN_L、NC 和 SHIELD/GND 四针外部总线端子 | 图 14471ad2d57d / 第 1 页 / 第 1 页右中 J1 HDR_4P_3.96，CANH/CANL/NC/GND 与 CAN_H/CAN_L/SHIELD |
| P1 | Header 5 | Atom 侧 +3.3V、CAN_TX 和 CAN_RX 接口，另有两针未连接 | 图 14471ad2d57d / 第 1 页 / 第 1 页右下 P1 Header 5，pin1 +3.3V、pin2 CAN_TX、pin3 CAN_RX、pin4/pin5 未接 |
| P2 | Header 4 | Atom 侧 +5VIN 和 GND 电源接口，另有两针未连接 | 图 14471ad2d57d / 第 1 页 / 第 1 页右下 P2 Header 4，pin3 +5VIN、pin4 GND，pin1/pin2 未接 |
| F1,F2 | 60V 100mA / J/K-NSMD0010 | 分别串联在 CANH/CANL 到 CAN_H/CAN_L 的线路保护器件 | 图 14471ad2d57d / 第 1 页 / 第 1 页中右 F1/F2 60V 100mA J/K-NSMD0010，串联 CANH/CANL 与 CAN_H/CAN_L |
| TSS1,TSS2,TSS3 | P0080TA | CANH/CANL 与 SGND/SHIELD 周围的浪涌钳位器件 | 图 14471ad2d57d / 第 1 页 / 第 1 页中央保护区，TSS1/TSS2/TSS3 P0080TA 与 CANH/CANL、SGND、SHIELD |
| DZ1,DZ2 | PESD5V0L1BA | CANH/CANL 到 SGND 的 ESD 保护二极管 | 图 14471ad2d57d / 第 1 页 / 第 1 页中央左侧 DZ1/DZ2 PESD5V0L1BA，分别位于 CANH/CANL 与 SGND |
| GDT1,GDT2 | SMD4532-075 | CAN_H/CAN_L 到 SHIELD 的气体放电浪涌保护器件 | 图 14471ad2d57d / 第 1 页 / 第 1 页中右 GDT1/GDT2 SMD4532-075，CAN_H/CAN_L 到 SHIELD |
| R4,C10 | 1MΩ / 1nF 2000V | SGND 与 SHIELD 之间的并联泄放和高频耦合网络 | 图 14471ad2d57d / 第 1 页 / 第 1 页中央 R4 1MΩ 与 C10 1nF/2000V，并联连接 SGND 与 SHIELD |
| D2 | ZMM5V1 | +S5V 隔离电源轨对 SGND 的钳位器件 | 图 14471ad2d57d / 第 1 页 / 第 1 页左下 D2 ZMM5V1，+S5V 到 SGND |
| C6,C7,C12,C13 | 4.7uF / 10uF / 100nF / 100nF | 隔离电源输入输出及 CAN 收发器两侧电源去耦 | 图 14471ad2d57d / 第 1 页 / 第 1 页 C6 +5VIN/GND、C7 +S5V/SGND、C12 +3.3V/GND、C13 +S5V/SGND |

## 系统结构

### Atom CAN 隔离通信架构

Atom 主控通过 P1 的 CAN_TX/CAN_RX 连接 U4 CA-IS3050G 逻辑侧，U4 总线侧输出 CANH/CANL；U2 B0505S-1W 为总线侧提供隔离 +S5V/SGND，保护网络后经 J1 接出。

- 参数与网络：`transceiver=U4 CA-IS3050G`；`isolated_power=U2 B0505S-1W`；`logic_side=+3.3V, GND, CAN_TX, CAN_RX`；`bus_side=+S5V, SGND, CANH, CANL`；`external_connector=J1 HDR_4P_3.96`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页完整单页原理图，U2/U4、P1/P2、CAN 保护与 J1

## 电源

### +5VIN 到 +S5V 隔离电源

U2 B0505S-1W 的 +Vin pin2 接 +5VIN、-Vin pin1 接 GND，+Vout pin4 输出 +S5V、-Vout pin3 接 SGND，实现两侧电源和地隔离。

- 参数与网络：`input_positive=+5VIN`；`input_return=GND`；`output_positive=+S5V`；`output_return=SGND`；`input_capacitor=C6 4.7uF`；`output_capacitor=C7 10uF`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页左上 U2 B0505S-1W 与 C6/C7

### CA-IS3050G 双侧供电域

U4 VCC1 pin1 使用 +3.3V、GND1 pin4 接 GND；VCC2 pin8 使用 +S5V、GND2 pin5 接 SGND，C12/C13 分别为两侧 100nF 去耦。

- 参数与网络：`logic_supply=VCC1 +3.3V`；`logic_ground=GND1 GND`；`bus_supply=VCC2 +S5V`；`bus_ground=GND2 SGND`；`logic_decoupling=C12 100nF`；`bus_decoupling=C13 100nF`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页左中 U4 VCC1/GND1/VCC2/GND2 与 C12/C13

## 接口

### Atom 主控连接器映射

P1 Header 5 的 pin1=+3.3V、pin2=CAN_TX、pin3=CAN_RX，pin4/pin5 未接；P2 Header 4 的 pin3=+5VIN、pin4=GND，pin1/pin2 未接。

- 参数与网络：`P1=pin1 +3.3V, pin2 CAN_TX, pin3 CAN_RX, pin4 NC, pin5 NC`；`P2=pin1 NC, pin2 NC, pin3 +5VIN, pin4 GND`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页右下 P1 Header 5 与 P2 Header 4

### CA-IS3050G 逻辑与总线信号

U4 RXD pin2 连接 CAN_RX，TXD pin3 连接 CAN_TX；隔离侧 CANH pin7 与 CANL pin6 进入后级保护网络。

- 参数与网络：`RXD=pin2 CAN_RX`；`TXD=pin3 CAN_TX`；`CANH=pin7 CANH`；`CANL=pin6 CANL`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页左中 U4 RXD/TXD/CANH/CANL 与同名网络

### J1 外部 CAN 端子

J1 pin1 CANH 接保护后的 CAN_H，pin2 CANL 接 CAN_L，pin3 为 NC，pin4 GND 连接 SHIELD。

- 参数与网络：`pin1=CAN_H / CANH`；`pin2=CAN_L / CANL`；`pin3=NC`；`pin4=SHIELD / GND`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页右中 J1 HDR_4P_3.96 与 CAN_H/CAN_L/SHIELD

### CAN 终端电阻

当前完整单页原理图未画出跨接 CANH/CANL 或 CAN_H/CAN_L 的 120Ω 终端电阻；R4 1MΩ 与 C10 1nF 连接的是 SGND 和 SHIELD，不是 CAN 终端。

- 参数与网络：`onboard_120ohm=false`；`shield_network=R4 1MΩ parallel C10 1nF between SGND and SHIELD`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页完整 CANH/CANL 到 J1 路径，未见 120Ω 跨线电阻

## 保护电路

### CANH/CANL 串联线路保护

CANH 与 CANL 分别经过 F1/F2 60V 100mA J/K-NSMD0010 后成为外部网络 CAN_H/CAN_L。

- 参数与网络：`high_line=CANH -> F1 -> CAN_H`；`low_line=CANL -> F2 -> CAN_L`；`rating=60V 100mA`；`part=J/K-NSMD0010`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页中右 F1/F2 与 CANH/CANL/CAN_H/CAN_L

### CAN 低压 ESD 与 TSS 保护

DZ1/DZ2 PESD5V0L1BA 分别将 CANH/CANL 钳位到 SGND；TSS2 P0080TA 跨接 CANH/CANL，TSS1/TSS3 P0080TA 位于 CANH/CANL 与 SHIELD 参考节点之间。

- 参数与网络：`esd_devices=DZ1/DZ2 PESD5V0L1BA`；`line_to_line_tss=TSS2 P0080TA`；`line_to_shield_tss=TSS1/TSS3 P0080TA`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页中央 DZ1/DZ2 与 TSS1/TSS2/TSS3 保护拓扑

### CAN 线对 SHIELD 气体放电保护

GDT1/GDT2 SMD4532-075 分别连接 CAN_H/CAN_L 与 SHIELD，为外部总线提供线对屏蔽层保护。

- 参数与网络：`CAN_H=GDT1 SMD4532-075 to SHIELD`；`CAN_L=GDT2 SMD4532-075 to SHIELD`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页中右 GDT1/GDT2 与 CAN_H/CAN_L/SHIELD

### +S5V 隔离电源钳位

D2 ZMM5V1 从 +S5V 接到 SGND，对 CA-IS3050G 总线侧电源轨提供钳位。

- 参数与网络：`device=D2 ZMM5V1`；`rail=+S5V`；`return=SGND`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页左下 D2 ZMM5V1 与 +S5V/SGND

## 关键网络

### GND、SGND 与 SHIELD 隔离边界

主控侧使用 GND，CAN 收发器隔离侧使用 SGND，外部端子和浪涌器件参考 SHIELD；SGND 与 SHIELD 只通过 R4 1MΩ 和 C10 1nF/2000V 并联网络耦合。

- 参数与网络：`logic_ground=GND`；`isolated_ground=SGND`；`chassis_reference=SHIELD`；`dc_coupling=R4 1MΩ`；`ac_coupling=C10 1nF 2000V`
- 证据：图 14471ad2d57d / 第 1 页 / 第 1 页 U2/U4 地域与中央 R4/C10 到 SHIELD

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom CAN 隔离通信架构 | `transceiver=U4 CA-IS3050G`；`isolated_power=U2 B0505S-1W`；`logic_side=+3.3V, GND, CAN_TX, CAN_RX`；`bus_side=+S5V, SGND, CANH, CANL`；`external_connector=J1 HDR_4P_3.96` |
| 电源 | +5VIN 到 +S5V 隔离电源 | `input_positive=+5VIN`；`input_return=GND`；`output_positive=+S5V`；`output_return=SGND`；`input_capacitor=C6 4.7uF`；`output_capacitor=C7 10uF` |
| 电源 | CA-IS3050G 双侧供电域 | `logic_supply=VCC1 +3.3V`；`logic_ground=GND1 GND`；`bus_supply=VCC2 +S5V`；`bus_ground=GND2 SGND`；`logic_decoupling=C12 100nF`；`bus_decoupling=C13 100nF` |
| 接口 | Atom 主控连接器映射 | `P1=pin1 +3.3V, pin2 CAN_TX, pin3 CAN_RX, pin4 NC, pin5 NC`；`P2=pin1 NC, pin2 NC, pin3 +5VIN, pin4 GND` |
| 接口 | CA-IS3050G 逻辑与总线信号 | `RXD=pin2 CAN_RX`；`TXD=pin3 CAN_TX`；`CANH=pin7 CANH`；`CANL=pin6 CANL` |
| 接口 | J1 外部 CAN 端子 | `pin1=CAN_H / CANH`；`pin2=CAN_L / CANL`；`pin3=NC`；`pin4=SHIELD / GND` |
| 关键网络 | GND、SGND 与 SHIELD 隔离边界 | `logic_ground=GND`；`isolated_ground=SGND`；`chassis_reference=SHIELD`；`dc_coupling=R4 1MΩ`；`ac_coupling=C10 1nF 2000V` |
| 保护电路 | CANH/CANL 串联线路保护 | `high_line=CANH -> F1 -> CAN_H`；`low_line=CANL -> F2 -> CAN_L`；`rating=60V 100mA`；`part=J/K-NSMD0010` |
| 保护电路 | CAN 低压 ESD 与 TSS 保护 | `esd_devices=DZ1/DZ2 PESD5V0L1BA`；`line_to_line_tss=TSS2 P0080TA`；`line_to_shield_tss=TSS1/TSS3 P0080TA` |
| 保护电路 | CAN 线对 SHIELD 气体放电保护 | `CAN_H=GDT1 SMD4532-075 to SHIELD`；`CAN_L=GDT2 SMD4532-075 to SHIELD` |
| 保护电路 | +S5V 隔离电源钳位 | `device=D2 ZMM5V1`；`rail=+S5V`；`return=SGND` |
| 接口 | CAN 终端电阻 | `onboard_120ohm=false`；`shield_network=R4 1MΩ parallel C10 1nF between SGND and SHIELD` |
| 其他事实 | 产品正文中的 CAN 性能参数 | `documented_max_rate=1Mbps`；`documented_nodes=110`；`documented_loop_delay=150ns`；`documented_common_mode=-12V to 12V` |

## 待确认事项

- `other.documented-can-limits`：产品正文给出最高 1Mbps、最多 110 节点、150ns 环路延迟和 -12V 至 12V 共模范围，但这些性能指标没有在原理图中标注，需由 CA-IS3050G 数据手册和具体网络条件确认。（证据：图 14471ad2d57d / 第 1 页 / 第 1 页 U4 CA-IS3050G 型号与 CANH/CANL 电路，图中无速率、节点数、延迟或共模参数标注）
- `review.can-performance-limits`：Atom CAN 当前硬件版本的 1Mbps、110 节点、150ns 和 -12V 至 12V 参数是否均由 CA-IS3050G 数据手册及整机测试确认？；原因：这些数值来自产品正文，当前原理图只给出器件型号和连接，无法验证条件、容差与系统级上限。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `14471ad2d57d0bc57c1868501d55da2d06db7566782d6b0f7592247c5fe7cb19` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_can/atom_can_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_can.md`

源文档 SHA-256：`df4d74a6a9bab9a7537ce049d4f46e773458234b1eabf5fe944344abd6bbc96f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
