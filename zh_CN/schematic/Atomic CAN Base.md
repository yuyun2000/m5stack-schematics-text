# Atomic CAN Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic CAN Base |
| SKU | A103 |
| 产品 ID | `atomic-can-base-4d4cc1e22580` |
| 源文档 | `zh_CN/atom/Atomic CAN Base.md` |

## 概述

Atomic CAN Base 以 CA-IS3050G（U4）连接 3.3V 逻辑侧的 CAN_TX/CAN_RX 与隔离侧的 CANH/CANL。B0505S-1W（U2）把 +5VIN/GND 转换为独立的 +S5V/SGND，为 U4 总线侧供电。CANH/CANL 经 ESD/浪涌器件、串联保险丝、气体放电管和 SGND-SHIELD 的 RC 耦合网络后，以 CAN_H、CAN_L 和 SHIELD 引出到 J1。

## 检索关键词

`Atomic CAN Base`、`A103`、`CA-IS3050G`、`B0505S-1W`、`CAN`、`CAN_TX`、`CAN_RX`、`CANH`、`CANL`、`CAN_H`、`CAN_L`、`+3.3V`、`+5VIN`、`+S5V`、`GND`、`SGND`、`SHIELD`、`HDR_4P_3.96`、`PESD5V0L1BA`、`P0080TA`、`SMD4532-075`、`JK-NSMD010`、`ZMM5V1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | B0505S-1W | +5VIN/GND 至 +S5V/SGND 的隔离 DC-DC 电源模块 | 图 14471ad2d57d / 第 1 页 / 左上角 U2：B0505S-1W，1/2 脚为 -Vin/+Vin，3/4 脚为 -Vout/+Vout |
| U4 | CA-IS3050G | 隔离 CAN 收发器，连接 CAN_TX/CAN_RX 与 CANH/CANL | 图 14471ad2d57d / 第 1 页 / 左中部 U4：CA-IS3050G，VCC1/RXD/TXD/GND1 与 VCC2/CANH/CANL/GND2 引脚 |
| J1 | HDR_4P_3.96 | 外部 CAN 端子，提供 CANH、CANL、NC 和 GND/SHIELD | 图 14471ad2d57d / 第 1 页 / 右上部 J1：HDR_4P_3.96，端子文字 CANH、CANL、NC、GND |
| P1 | Header 5 | ATOM 逻辑侧 5 Pin 排针，引出 +3.3V、CAN_TX 和 CAN_RX | 图 14471ad2d57d / 第 1 页 / 右下角 P1 Header 5：1 脚 +3.3V、2 脚 CAN_TX、3 脚 CAN_RX，4/5 脚无外接连线 |
| P2 | Header 4 | ATOM 电源侧 4 Pin 排针，引入 +5VIN 和 GND | 图 14471ad2d57d / 第 1 页 / 右下角 P2 Header 4：1/2 脚 NC 标记，3 脚 +5VIN，4 脚 GND |
| C6 | 4.7uF | U2 +5VIN 输入侧滤波电容 | 图 14471ad2d57d / 第 1 页 / 左上角 U2 输入侧：C6 4.7uF 接在 +5VIN 与 GND 之间 |
| C7 | 10uF | U2 +S5V 输出侧滤波电容 | 图 14471ad2d57d / 第 1 页 / 左上角 U2 输出侧：C7 10uF 接在 +S5V 与 SGND 之间 |
| C9 | 22uF | +3.3V 逻辑电源滤波电容 | 图 14471ad2d57d / 第 1 页 / 右下部 P1/P2 左侧：C9 22uF 接在 +3.3V 与 GND 之间 |
| C12 | 100nF | U4 VCC1 的 +3.3V 去耦电容 | 图 14471ad2d57d / 第 1 页 / 左下部 U4 下方：C12 100nF 接在 +3.3V 与 GND 之间 |
| C13 | 100nF | U4 VCC2 的 +S5V 去耦电容 | 图 14471ad2d57d / 第 1 页 / 左下部 U4 下方：C13 100nF 接在 +S5V 与 SGND 之间 |
| D2 | ZMM5V1 | +S5V 对 SGND 的稳压/钳位器件 | 图 14471ad2d57d / 第 1 页 / 左下部 C13 右侧：D2 ZMM5V1 接在 +S5V 与 SGND 之间 |
| DZ1 | PESD5V0L1BA | CANH 到 SGND 的 ESD 钳位器件 | 图 14471ad2d57d / 第 1 页 / 中部保护网络左侧：DZ1 PESD5V0L1BA 位于 CANH 与 SGND 中点之间 |
| DZ2 | PESD5V0L1BA | CANL 到 SGND 的 ESD 钳位器件 | 图 14471ad2d57d / 第 1 页 / 中部保护网络左侧：DZ2 PESD5V0L1BA 位于 SGND 中点与 CANL 之间 |
| TSS1 | P0080TA | 保险丝前 CANH 到 SHIELD 的浪涌保护器件 | 图 14471ad2d57d / 第 1 页 / 中部保护网络：TSS1 P0080TA 竖接在 CANH 与 SHIELD 中点之间，位于 F1 左侧 |
| TSS2 | P0080TA | CANH 与 CANL 之间的差模浪涌保护器件 | 图 14471ad2d57d / 第 1 页 / 中部保护网络最左侧：TSS2 P0080TA 直接跨接 CANH 与 CANL |
| TSS3 | P0080TA | 保险丝前 CANL 到 SHIELD 的浪涌保护器件 | 图 14471ad2d57d / 第 1 页 / 中部保护网络：TSS3 P0080TA 竖接在 SHIELD 中点与 CANL 之间，位于 F2 左侧 |
| F1 | 60V 100mA/JK-NSMD010 | CANH 至 CAN_H 路径上的串联保护器件 | 图 14471ad2d57d / 第 1 页 / 中上部 CANH 线上：F1 标注 60V 100mA/JK-NSMD010，输出网络为 CAN_H |
| F2 | 60V 100mA/JK-NSMD010 | CANL 至 CAN_L 路径上的串联保护器件 | 图 14471ad2d57d / 第 1 页 / 中下部 CANL 线上：F2 标注 60V 100mA/JK-NSMD010，输出网络为 CAN_L |
| GDT1 | SMD4532-075 | 保险丝后 CAN_H 到 SHIELD 的气体放电保护器件 | 图 14471ad2d57d / 第 1 页 / 中右部：GDT1 SMD4532-075 竖接在 CAN_H 与 SHIELD 之间，位于 F1 右侧 |
| GDT2 | SMD4532-075 | 保险丝后 CAN_L 到 SHIELD 的气体放电保护器件 | 图 14471ad2d57d / 第 1 页 / 中右部：GDT2 SMD4532-075 竖接在 SHIELD 与 CAN_L 之间，位于 F2 右侧 |
| R4 | 1MΩ (1004) ±1% | SGND 与 SHIELD 之间的高阻泄放/参考连接 | 图 14471ad2d57d / 第 1 页 / 中部 SGND-SHIELD 桥接网络：R4 标注 1MΩ (1004) ±1% |
| C10 | 1nF (102) 10% 2000V | SGND 与 SHIELD 之间的高压电容耦合器件 | 图 14471ad2d57d / 第 1 页 / 中部 SGND-SHIELD 桥接网络：C10 标注 1nF (102) 10% 2000V，与 R4 并联 |

## 系统结构

### Atomic CAN Base

U4 将 GND 域的 +3.3V、CAN_TX、CAN_RX 与 SGND 域的 +S5V、CANH、CANL 分隔；U2 为 SGND 域生成独立的 +S5V。

- 参数与网络：`logic_transceiver=U4 CA-IS3050G`；`isolated_power=U2 B0505S-1W`；`logic_ground=GND`；`bus_ground=SGND`
- 证据：图 14471ad2d57d / 第 1 页 / 左侧 U2/U4：U2 输入 GND、输出 SGND；U4 的 GND1 接 GND、GND2 接 SGND

## 电源

### U2 B0505S-1W

U2 的 2 脚 +Vin 接 +5VIN、1 脚 -Vin 接 GND；4 脚 +Vout 输出 +S5V、3 脚 -Vout 接 SGND。

- 参数与网络：`input_positive=U2.2 +5VIN`；`input_return=U2.1 GND`；`output_positive=U2.4 +S5V`；`output_return=U2.3 SGND`
- 证据：图 14471ad2d57d / 第 1 页 / 左上角 U2：+Vin/-Vin/+Vout/-Vout 引脚和 +5VIN、GND、+S5V、SGND 网络

### U2 输入输出滤波

C6 4.7uF 跨接 +5VIN 与 GND；C7 10uF 跨接 +S5V 与 SGND。

- 参数与网络：`input_capacitor=C6 4.7uF`；`output_capacitor=C7 10uF`
- 证据：图 14471ad2d57d / 第 1 页 / 左上角 U2 两侧：C6 位于 +5VIN/GND，C7 位于 +S5V/SGND

### +3.3V 电源轨

C9 22uF 跨接 +3.3V 与 GND；C12 100nF 跨接 +3.3V 与 GND，并为 U4 的 VCC1 侧提供去耦。

- 参数与网络：`bulk_capacitor=C9 22uF`；`decoupling_capacitor=C12 100nF`；`transceiver_supply_pin=U4.1 VCC1`
- 证据：图 14471ad2d57d / 第 1 页 / 左中下部 C12 与右下部 C9：两者均接 +3.3V/GND；U4.1 标注 VCC1

### +S5V 电源轨

C13 100nF 跨接 +S5V 与 SGND，为 U4 的 VCC2 侧去耦；D2 ZMM5V1 同样跨接 +S5V 与 SGND。

- 参数与网络：`decoupling_capacitor=C13 100nF`；`clamp=D2 ZMM5V1`；`transceiver_supply_pin=U4.8 VCC2`
- 证据：图 14471ad2d57d / 第 1 页 / 左中下部：C13 与 D2 均接 +S5V/SGND；U4.8 标注 VCC2

## 接口

### P1 Header 5

P1 的 1 脚接 +3.3V，2 脚接 CAN_TX，3 脚接 CAN_RX；4 脚和 5 脚在本页无外接连线。

- 参数与网络：`pin_1=+3.3V`；`pin_2=CAN_TX`；`pin_3=CAN_RX`；`pin_4=unconnected`；`pin_5=unconnected`
- 证据：图 14471ad2d57d / 第 1 页 / 右下角 P1 Header 5：1~5 脚及 +3.3V、CAN_TX、CAN_RX 连线

### P2 Header 4

P2 的 1 脚和 2 脚标记为不连接，3 脚接 +5VIN，4 脚接 GND。

- 参数与网络：`pin_1=NC`；`pin_2=NC`；`pin_3=+5VIN`；`pin_4=GND`
- 证据：图 14471ad2d57d / 第 1 页 / 右下角 P2 Header 4：1/2 脚红色 NC 标记，3 脚 +5VIN，4 脚 GND

### J1 HDR_4P_3.96

J1 的四个端子功能依次标为 CANH、CANL、NC、GND；CANH 接 CAN_H，CANL 接 CAN_L，GND 端接 SHIELD。

- 参数与网络：`terminal_can_high=CANH to CAN_H`；`terminal_can_low=CANL to CAN_L`；`terminal_unused=NC`；`terminal_ground=GND to SHIELD`
- 证据：图 14471ad2d57d / 第 1 页 / 右上部 J1：符号内 CANH/CANL/NC/GND 标注，左侧网络为 CAN_H/CAN_L/SHIELD

## 总线

### U4 逻辑侧

U4 的 1 脚 VCC1 接 +3.3V，2 脚 RXD 接 CAN_RX，3 脚 TXD 接 CAN_TX，4 脚 GND1 接 GND。

- 参数与网络：`pin_1=VCC1 +3.3V`；`pin_2=RXD CAN_RX`；`pin_3=TXD CAN_TX`；`pin_4=GND1 GND`
- 证据：图 14471ad2d57d / 第 1 页 / 左中部 U4 左侧 1~4 脚：VCC1/RXD/TXD/GND1 与 +3.3V/CAN_RX/CAN_TX/GND

### U4 CAN 侧

U4 的 8 脚 VCC2 接 +S5V，7 脚 CANH 接 CANH，6 脚 CANL 接 CANL，5 脚 GND2 接 SGND。

- 参数与网络：`pin_8=VCC2 +S5V`；`pin_7=CANH CANH`；`pin_6=CANL CANL`；`pin_5=GND2 SGND`
- 证据：图 14471ad2d57d / 第 1 页 / 左中部 U4 右侧 5~8 脚：GND2/CANL/CANH/VCC2 与 SGND/CANL/CANH/+S5V

## 保护电路

### F1/F2 CAN 串联保护

F1 串联在 CANH/CAN_H 路径，F2 串联在 CANL/CAN_L 路径；两者均标注 60V 100mA/JK-NSMD010。

- 参数与网络：`high_line=F1 60V 100mA/JK-NSMD010`；`low_line=F2 60V 100mA/JK-NSMD010`
- 证据：图 14471ad2d57d / 第 1 页 / 中部 CANH/CANL 水平线上：F1 和 F2 的位号、额定标注及串联连接

### DZ1/DZ2 ESD 网络

DZ1 PESD5V0L1BA 连接 CANH 与 SGND，DZ2 PESD5V0L1BA 连接 CANL 与 SGND。

- 参数与网络：`canh_protector=DZ1 PESD5V0L1BA`；`canl_protector=DZ2 PESD5V0L1BA`；`reference_ground=SGND`
- 证据：图 14471ad2d57d / 第 1 页 / 中部保护网络左侧：DZ1 位于 CANH-SGND，DZ2 位于 SGND-CANL

### TSS2 差模保护

TSS2 P0080TA 直接跨接在 CANH 与 CANL 之间。

- 参数与网络：`device=TSS2 P0080TA`；`terminal_1=CANH`；`terminal_2=CANL`
- 证据：图 14471ad2d57d / 第 1 页 / 中部保护网络最左侧：TSS2 竖直跨接 CANH 与 CANL

### TSS1/TSS3 对 SHIELD 保护

TSS1 P0080TA 在 F1 前连接 CANH 与 SHIELD；TSS3 P0080TA 在 F2 前连接 CANL 与 SHIELD。

- 参数与网络：`high_line_protector=TSS1 P0080TA`；`low_line_protector=TSS3 P0080TA`；`reference=SHIELD`
- 证据：图 14471ad2d57d / 第 1 页 / 中部保护网络 F1/F2 左侧：TSS1 连接 CANH-SHIELD，TSS3 连接 SHIELD-CANL

### GDT1/GDT2 对 SHIELD 保护

GDT1 SMD4532-075 在 F1 后连接 CAN_H 与 SHIELD；GDT2 SMD4532-075 在 F2 后连接 CAN_L 与 SHIELD。

- 参数与网络：`high_line_protector=GDT1 SMD4532-075`；`low_line_protector=GDT2 SMD4532-075`；`reference=SHIELD`
- 证据：图 14471ad2d57d / 第 1 页 / 中右部 F1/F2 右侧：GDT1 连接 CAN_H-SHIELD，GDT2 连接 SHIELD-CAN_L

### SGND 与 SHIELD 耦合网络

R4 1MΩ (1004) ±1% 与 C10 1nF (102) 10% 2000V 并联，跨接 SGND 和 SHIELD。

- 参数与网络：`resistor=R4 1MΩ (1004) ±1%`；`capacitor=C10 1nF (102) 10% 2000V`；`connection=SGND-SHIELD parallel RC`
- 证据：图 14471ad2d57d / 第 1 页 / 中部 SGND-SHIELD 桥接：R4 与 C10 上下并联，左端 SGND、右端 SHIELD

## 关键网络

### CANH/CANL 至 CAN_H/CAN_L

U4 侧网络 CANH 和 CANL 分别经过串联器件 F1 和 F2 后改名为端子侧网络 CAN_H 和 CAN_L。

- 参数与网络：`high_side_path=CANH-F1-CAN_H`；`low_side_path=CANL-F2-CAN_L`
- 证据：图 14471ad2d57d / 第 1 页 / 中部两条总线：F1 左侧 CANH/右侧 CAN_H，F2 左侧 CANL/右侧 CAN_L

### CAN_TX/CAN_RX

P1.2 的 CAN_TX 连接 U4.3 TXD；P1.3 的 CAN_RX 连接 U4.2 RXD。

- 参数与网络：`transmit_path=P1.2 CAN_TX to U4.3 TXD`；`receive_path=P1.3 CAN_RX to U4.2 RXD`
- 证据：图 14471ad2d57d / 第 1 页 / 左中部 U4 与右下角 P1：同名网络 CAN_TX、CAN_RX 分别标注于对应引脚

### SHIELD

SHIELD 网络连接 J1 的 GND 端子，并作为 TSS1、TSS3、GDT1、GDT2 以及 R4/C10 耦合网络的公共参考节点。

- 参数与网络：`external_terminal=J1 GND`；`pre_fuse_protection=TSS1,TSS3`；`post_fuse_protection=GDT1,GDT2`；`sgnd_coupling=R4,C10`
- 证据：图 14471ad2d57d / 第 1 页 / 中部至右上部 SHIELD 水平网络：连接保护器件中点、R4/C10 右端和 J1 GND 端

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic CAN Base | `logic_transceiver=U4 CA-IS3050G`；`isolated_power=U2 B0505S-1W`；`logic_ground=GND`；`bus_ground=SGND` |
| 电源 | U2 B0505S-1W | `input_positive=U2.2 +5VIN`；`input_return=U2.1 GND`；`output_positive=U2.4 +S5V`；`output_return=U2.3 SGND` |
| 电源 | U2 输入输出滤波 | `input_capacitor=C6 4.7uF`；`output_capacitor=C7 10uF` |
| 电源 | +3.3V 电源轨 | `bulk_capacitor=C9 22uF`；`decoupling_capacitor=C12 100nF`；`transceiver_supply_pin=U4.1 VCC1` |
| 电源 | +S5V 电源轨 | `decoupling_capacitor=C13 100nF`；`clamp=D2 ZMM5V1`；`transceiver_supply_pin=U4.8 VCC2` |
| 总线 | U4 逻辑侧 | `pin_1=VCC1 +3.3V`；`pin_2=RXD CAN_RX`；`pin_3=TXD CAN_TX`；`pin_4=GND1 GND` |
| 总线 | U4 CAN 侧 | `pin_8=VCC2 +S5V`；`pin_7=CANH CANH`；`pin_6=CANL CANL`；`pin_5=GND2 SGND` |
| 接口 | P1 Header 5 | `pin_1=+3.3V`；`pin_2=CAN_TX`；`pin_3=CAN_RX`；`pin_4=unconnected`；`pin_5=unconnected` |
| 接口 | P2 Header 4 | `pin_1=NC`；`pin_2=NC`；`pin_3=+5VIN`；`pin_4=GND` |
| 接口 | J1 HDR_4P_3.96 | `terminal_can_high=CANH to CAN_H`；`terminal_can_low=CANL to CAN_L`；`terminal_unused=NC`；`terminal_ground=GND to SHIELD` |
| 关键网络 | CANH/CANL 至 CAN_H/CAN_L | `high_side_path=CANH-F1-CAN_H`；`low_side_path=CANL-F2-CAN_L` |
| 保护电路 | F1/F2 CAN 串联保护 | `high_line=F1 60V 100mA/JK-NSMD010`；`low_line=F2 60V 100mA/JK-NSMD010` |
| 保护电路 | DZ1/DZ2 ESD 网络 | `canh_protector=DZ1 PESD5V0L1BA`；`canl_protector=DZ2 PESD5V0L1BA`；`reference_ground=SGND` |
| 保护电路 | TSS2 差模保护 | `device=TSS2 P0080TA`；`terminal_1=CANH`；`terminal_2=CANL` |
| 保护电路 | TSS1/TSS3 对 SHIELD 保护 | `high_line_protector=TSS1 P0080TA`；`low_line_protector=TSS3 P0080TA`；`reference=SHIELD` |
| 保护电路 | GDT1/GDT2 对 SHIELD 保护 | `high_line_protector=GDT1 SMD4532-075`；`low_line_protector=GDT2 SMD4532-075`；`reference=SHIELD` |
| 保护电路 | SGND 与 SHIELD 耦合网络 | `resistor=R4 1MΩ (1004) ±1%`；`capacitor=C10 1nF (102) 10% 2000V`；`connection=SGND-SHIELD parallel RC` |
| 关键网络 | CAN_TX/CAN_RX | `transmit_path=P1.2 CAN_TX to U4.3 TXD`；`receive_path=P1.3 CAN_RX to U4.2 RXD` |
| 关键网络 | SHIELD | `external_terminal=J1 GND`；`pre_fuse_protection=TSS1,TSS3`；`post_fuse_protection=GDT1,GDT2`；`sgnd_coupling=R4,C10` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `14471ad2d57d0bc57c1868501d55da2d06db7566782d6b0f7592247c5fe7cb19` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic CAN Base/img-fa481a72-f110-4866-9266-b67369f6ff2a.webp` |

---

源文档：`zh_CN/atom/Atomic CAN Base.md`

源文档 SHA-256：`23aa02332032c6481629e8b7d291ce676f489f3c8eb720f2fd4bc19f6d8119c9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
