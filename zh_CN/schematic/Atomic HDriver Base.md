# Atomic HDriver Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic HDriver Base |
| SKU | A092 |
| 产品 ID | `atomic-hdriver-base-4810b53ccf76` |
| 源文档 | `zh_CN/atom/Atomic H-Driver Base.md` |

## 概述

Atomic HDriver Base 使用 U2 DRV8876PWP 驱动 OUT_N/OUT_P 电机输出，J3 同时接出 VIN、GND 和两路输出。外部 VIN 为驱动器 VM 供电，并由 U1 SY8303A 降压为 SYS_P050，再经 FU1 0.5A 输出 M5_P050 给 Atom。Atom 的 G19/G23 控制 IN_1/IN_2，G22 接收 FAULT，G33 通过 18KΩ/2KΩ 分压和 105/10V 电容监测 VIN。

## 检索关键词

`Atomic HDriver Base`、`A092`、`DRV8876PWP`、`SY8303A`、`H-bridge`、`motor driver`、`OUT_N`、`OUT_P`、`VIN`、`SYS_P050`、`M5_P050`、`IN_1`、`IN_2`、`FAULT`、`nFAULT`、`nSLEEP`、`PMODE`、`VREF`、`IPROPI`、`IMODE`、`GPIO19`、`GPIO22`、`GPIO23`、`GPIO33`、`FU1 0.5A`、`L1 4.7uH`、`J3 HT3.96_4P`、`voltage divider`、`output snubber`、`LED_GREEN`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SY8303A | 将外部 VIN 降压为 SYS_P050 的 DC-DC 转换器 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上 DC-DC 区，U1 SY8303A 的 VIN/EN、BS/LX、FB/FS 与 GND |
| U2 | DRV8876PWP | 接收 IN_1/IN_2 控制并驱动 OUT_N/OUT_P 的 H 桥电机驱动器 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下 Driver 区，U2 DRV8876PWP 全部控制、电源、输出和配置针脚 |
| FU1 | 0.5A | 串联保护 SYS_P050 到 M5_P050 的 Atom 5V 供电路径 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，FU1 0.5A 串联于 SYS_P050 与 M5_P050 之间 |
| J1,J2 | SIP4 / SIP5 | Atom 插座，连接 M5_P050、3V3、GND 和 G21/G25/G22/G19/G23/G33 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左下 ATOM SOCKET 区，J1 SIP4 与 J2 SIP5 的全部网络标注 |
| J3 | HT3.96_4P | 接出 OUT_N、OUT_P、GND 和 VIN 的四针电机与电源端子 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页右上，J3 HT3.96_4P，pin1 OUT_N、pin2 OUT_P、pin3 GND、pin4 VIN |
| L1 | 4.7uH | 连接 U1 LX 开关节点与 SYS_P050 输出的降压电感 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，L1 4.7uH 位于 U1 LX pin6 与 SYS_P050 之间 |
| LED1,R2 | LED_GREEN / 15KΩ 1% | SYS_P050 电源状态指示 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，SYS_P050 经 R2 15K/1% 和 LED1 LED_GREEN 接 GND |
| R7,R8,R9 | 15KΩ 1% / 2.2KΩ 1% / 200KΩ 1% | SY8303A 的反馈分压与 FS 设定网络 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，R7/R8 连接 SYS_P050、FB 与 GND，R9 连接 FS 与 GND |
| R3,R4,R5,R6,R10,C3 | 15KΩ / 2.2KΩ / 2.2KΩ / 18KΩ / 2KΩ / 105/10V | Atom 的 FAULT 上拉、IN_1/IN_2 串联电阻和 VIN 电压采样网络 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左下，J2 周围 R3-R6、R10、C3 与 FAULT/IN_1/IN_2/VIN/G33 |
| R11,R12,R13,R14,C11 | 15KΩ / 15KΩ / 1KΩ / 20KΩ / 104/50V | DRV8876PWP 的 VREF、IPROPI 和 IMODE 配置网络 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，R11/R12/C11 接 VREF，R13 接 IPROPI，R14 接 IMODE |
| C6,C7,C9,C10 | 104/50V / 104/50V / 104/50V / 100uF/35V | DRV8876PWP 电荷泵和 VIN 电机电源去耦 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，C6 从 VCP 到 VIN、C7 跨 CPH/CPL、C9/C10 从 VIN 到 GND |
| R15,C8 | 10Ω 1% / 102/50V | 跨接 OUT_N 与 OUT_P 的串联输出吸收网络 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，OUT_N 经 R15 10R/1% 与 C8 102/50V 串联后接 OUT_P |
| C1,C2,C4,C5 | 475/50V / 104/50V / 226/10V / 226/10V | SY8303A 的 VIN 输入、BS-LX 自举和 SYS_P050 输出电容 | 图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，C1 VIN-GND、C2 BS-LX、C4/C5 SYS_P050-GND |

## 系统结构

### Atomic HDriver Base 电源与电机控制架构

J3 VIN 为 U2 DRV8876PWP 的 VM 电机电源和 U1 SY8303A 的输入；U1 生成 SYS_P050 并经 FU1 输出 M5_P050 给 Atom，Atom 通过 IN_1/IN_2 控制 U2，U2 通过 OUT_N/OUT_P 驱动 J3 输出。

- 参数与网络：`motor_driver=U2 DRV8876PWP`；`dc_dc=U1 SY8303A`；`external_connector=J3 HT3.96_4P`；`logic_power_path=VIN -> U1 -> SYS_P050 -> FU1 -> M5_P050 -> J1 5V`；`control_path=Atom G19/G23 -> IN_1/IN_2 -> U2`；`motor_path=U2 OUT_N/OUT_P -> J3 pins 1/2`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页完整原理图，DC-DC、ATOM SOCKET、Driver 与 J3 四个功能区

## 电源

### SY8303A 输入、使能和降压输出

U1 VIN pin5 与 EN pin8 均接 VIN，GND pin3/pin4 接 GND；LX pin6 经 L1 4.7uH 输出 SYS_P050，BS pin7 通过 C2 104/50V 接 LX。

- 参数与网络：`VIN=pin5 VIN`；`EN=pin8 VIN`；`GND=pins 3 and 4 GND`；`LX=pin6 through L1 4.7uH to SYS_P050`；`bootstrap=C2 104/50V between BS pin7 and LX pin6`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，U1 SY8303A VIN/EN/GND/BS/LX 与 C2/L1/SYS_P050

### SY8303A 反馈、频率设定与去耦

R7 15KΩ/1% 从 SYS_P050 接 FB pin1，R8 2.2KΩ/1% 从 FB 接 GND，R9 200KΩ/1% 从 FS pin2 接 GND；C1 475/50V 位于 VIN-GND，C4/C5 226/10V 并联于 SYS_P050-GND。

- 参数与网络：`feedback_upper=R7 15K/1% SYS_P050 to FB`；`feedback_lower=R8 2.2K/1% FB to GND`；`frequency_set=R9 200K/1% FS to GND`；`input_capacitor=C1 475/50V`；`output_capacitors=C4 and C5 226/10V`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，U1 FB/FS 周围 R7-R9 与输入输出电容 C1/C4/C5

### DRV8876PWP 电机电源和接地

U2 VM pin11 接 VIN，GND pin15、PGND pin9 与 PAD pin0 接 GND；C9 104/50V 和 C10 100uF/35V 并联连接 VIN 与 GND。

- 参数与网络：`motor_supply=VM pin11 VIN`；`grounds=GND pin15, PGND pin9, PAD pin0`；`decoupling=C9 104/50V and C10 100uF/35V from VIN to GND`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，U2 VM/GND/PGND/PAD 与 VIN、GND、C9/C10

### DRV8876PWP 电荷泵电容

C6 104/50V 连接 U2 VCP pin12 与 VIN，C7 104/50V 连接 CPH pin13 与 CPL pin14。

- 参数与网络：`VCP_capacitor=C6 104/50V VCP to VIN`；`flying_capacitor=C7 104/50V CPH to CPL`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，U2 pin12-pin14 与 C6/C7

## 接口

### Atom 插座信号分配

J1 接出 G21、G25、5V/M5_P050 和 GND；J2 接出 3V3、G22、G19、G23 和 G33。G21/G25 在本页未连接其他电路，G22/G19/G23/G33 分别用于 FAULT、IN_1、IN_2 和 VIN 采样。

- 参数与网络：`J1=G21, G25, 5V=M5_P050, GND`；`J2=3V3, G22=FAULT, G19=IN_1, G23=IN_2, G33=VIN sense`；`unused_in_base=G21, G25`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左下 ATOM SOCKET，J1/J2 标签及 R3-R6、R10、C3 网络

### J3 电机与外部电源端子

J3 HT3.96_4P 的 pin1=OUT_N、pin2=OUT_P、pin3=GND、pin4=VIN。

- 参数与网络：`pin1=OUT_N`；`pin2=OUT_P`；`pin3=GND`；`pin4=VIN`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右上 J3 HT3.96_4P 的 pin1-pin4 与 OUT_N/OUT_P/GND/VIN

### SYS_P050 绿色指示灯

SYS_P050 经 R2 15KΩ/1% 和 LED1 LED_GREEN 串联连接到 GND。

- 参数与网络：`rail=SYS_P050`；`resistor=R2 15K/1%`；`indicator=LED1 LED_GREEN`；`return=GND`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上，SYS_P050-R2-LED1-GND 支路

## GPIO 与控制信号

### Atom 与 DRV8876PWP 控制和故障信号

G19 经 R4 2.2KΩ/1% 形成 IN_1 并接 U2 EN/IN1 pin1，G23 经 R5 2.2KΩ/1% 形成 IN_2 并接 U2 PH/IN2 pin2；U2 nFAULT pin4 通过 FAULT 接 G22，FAULT 由 R3 15KΩ/1% 上拉到 3V3。

- 参数与网络：`G19=R4 2.2K/1% -> IN_1 -> U2 pin1 EN/IN1`；`G23=R5 2.2K/1% -> IN_2 -> U2 pin2 PH/IN2`；`G22=FAULT <- U2 pin4 nFAULT`；`fault_pullup=R3 15K/1% to 3V3`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左下 J2/R3-R5 与右下 U2 pin1/pin2/pin4 的同名网络

## 保护电路

### Atom 5V 串联保护

SYS_P050 经过 FU1 0.5A 后成为 M5_P050，M5_P050 连接 J1 的 5V 触点。

- 参数与网络：`input_net=SYS_P050`；`protection=FU1 0.5A`；`output_net=M5_P050`；`destination=J1 5V`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左上 FU1 与左下 J1 5V 的 M5_P050 网络

### OUT_N/OUT_P 串联 RC 吸收网络

U2 OUT1 pin8 形成 OUT_N，OUT2 pin10 形成 OUT_P；R15 10Ω/1% 与 C8 102/50V 串联跨接 OUT_N 和 OUT_P。

- 参数与网络：`OUT_N=U2 OUT1 pin8`；`OUT_P=U2 OUT2 pin10`；`snubber=OUT_N -> R15 10R/1% -> C8 102/50V -> OUT_P`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，U2 OUT1/OUT2 与 R15/C8 串联跨接网络

## 关键网络

### DRV8876PWP 使能和模式网络

U2 nSLEEP pin3 与 PMODE pin16 均接 SYS_P050；IMODE pin7 通过 R14 20KΩ/1% 接 GND。

- 参数与网络：`nSLEEP=pin3 SYS_P050`；`PMODE=pin16 SYS_P050`；`IMODE=pin7 through R14 20K/1% to GND`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，SYS_P050 到 U2 nSLEEP/PMODE 与 R14 到 IMODE

## 模拟电路

### G33 的 VIN 电压采样网络

VIN 经 R6 18KΩ/1% 接 G33，G33 经 R10 2KΩ/1% 接 GND，C3 105/10V 从 G33 接 GND，构成 VIN 的 18KΩ/2KΩ 分压滤波网络。

- 参数与网络：`upper_resistor=R6 18K/1% VIN to G33`；`lower_resistor=R10 2K/1% G33 to GND`；`capacitor=C3 105/10V G33 to GND`；`divider_ratio=1/10`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页左下，VIN-R6-G33-R10-GND 与 C3 的完整连接

### DRV8876PWP VREF 与 IPROPI 配置

R11/R12 两个 15KΩ/1% 在 SYS_P050 与 GND 间分压，中点连接 U2 VREF pin5 并由 C11 104/50V 对地滤波；IPROPI pin6 通过 R13 1KΩ/1% 接 GND。

- 参数与网络：`VREF_upper=R11 15K/1% to SYS_P050`；`VREF_lower=R12 15K/1% to GND`；`VREF_filter=C11 104/50V to GND`；`IPROPI=pin6 through R13 1K/1% to GND`
- 证据：图 8ed610f2bdf4 / 第 1 页 / 第 1 页右下，R11/R12/C11 到 U2 VREF 与 R13 到 IPROPI

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic HDriver Base 电源与电机控制架构 | `motor_driver=U2 DRV8876PWP`；`dc_dc=U1 SY8303A`；`external_connector=J3 HT3.96_4P`；`logic_power_path=VIN -> U1 -> SYS_P050 -> FU1 -> M5_P050 -> J1 5V`；`control_path=Atom G19/G23 -> IN_1/IN_2 -> U2`；`motor_path=U2 OUT_N/OUT_P -> J3 pins 1/2` |
| 电源 | SY8303A 输入、使能和降压输出 | `VIN=pin5 VIN`；`EN=pin8 VIN`；`GND=pins 3 and 4 GND`；`LX=pin6 through L1 4.7uH to SYS_P050`；`bootstrap=C2 104/50V between BS pin7 and LX pin6` |
| 电源 | SY8303A 反馈、频率设定与去耦 | `feedback_upper=R7 15K/1% SYS_P050 to FB`；`feedback_lower=R8 2.2K/1% FB to GND`；`frequency_set=R9 200K/1% FS to GND`；`input_capacitor=C1 475/50V`；`output_capacitors=C4 and C5 226/10V` |
| 保护电路 | Atom 5V 串联保护 | `input_net=SYS_P050`；`protection=FU1 0.5A`；`output_net=M5_P050`；`destination=J1 5V` |
| 接口 | Atom 插座信号分配 | `J1=G21, G25, 5V=M5_P050, GND`；`J2=3V3, G22=FAULT, G19=IN_1, G23=IN_2, G33=VIN sense`；`unused_in_base=G21, G25` |
| GPIO 与控制信号 | Atom 与 DRV8876PWP 控制和故障信号 | `G19=R4 2.2K/1% -> IN_1 -> U2 pin1 EN/IN1`；`G23=R5 2.2K/1% -> IN_2 -> U2 pin2 PH/IN2`；`G22=FAULT <- U2 pin4 nFAULT`；`fault_pullup=R3 15K/1% to 3V3` |
| 模拟电路 | G33 的 VIN 电压采样网络 | `upper_resistor=R6 18K/1% VIN to G33`；`lower_resistor=R10 2K/1% G33 to GND`；`capacitor=C3 105/10V G33 to GND`；`divider_ratio=1/10` |
| 接口 | J3 电机与外部电源端子 | `pin1=OUT_N`；`pin2=OUT_P`；`pin3=GND`；`pin4=VIN` |
| 电源 | DRV8876PWP 电机电源和接地 | `motor_supply=VM pin11 VIN`；`grounds=GND pin15, PGND pin9, PAD pin0`；`decoupling=C9 104/50V and C10 100uF/35V from VIN to GND` |
| 电源 | DRV8876PWP 电荷泵电容 | `VCP_capacitor=C6 104/50V VCP to VIN`；`flying_capacitor=C7 104/50V CPH to CPL` |
| 关键网络 | DRV8876PWP 使能和模式网络 | `nSLEEP=pin3 SYS_P050`；`PMODE=pin16 SYS_P050`；`IMODE=pin7 through R14 20K/1% to GND` |
| 模拟电路 | DRV8876PWP VREF 与 IPROPI 配置 | `VREF_upper=R11 15K/1% to SYS_P050`；`VREF_lower=R12 15K/1% to GND`；`VREF_filter=C11 104/50V to GND`；`IPROPI=pin6 through R13 1K/1% to GND` |
| 保护电路 | OUT_N/OUT_P 串联 RC 吸收网络 | `OUT_N=U2 OUT1 pin8`；`OUT_P=U2 OUT2 pin10`；`snubber=OUT_N -> R15 10R/1% -> C8 102/50V -> OUT_P` |
| 接口 | SYS_P050 绿色指示灯 | `rail=SYS_P050`；`resistor=R2 15K/1%`；`indicator=LED1 LED_GREEN`；`return=GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8ed610f2bdf40a38141ae6af39eab849134f2f3ec26aded8602cf6dba69c171b` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-640b15c1-b24d-4e9a-b936-2ec3e5a0e8e6.png` |

---

源文档：`zh_CN/atom/Atomic H-Driver Base.md`

源文档 SHA-256：`d3b77a609a57997929ce97377503e395430469deb4dca86e389c588f03b2b345`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
