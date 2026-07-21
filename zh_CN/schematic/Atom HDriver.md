# Atom HDriver 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom HDriver |
| SKU | K050 |
| 产品 ID | `atom-hdriver-e289df887408` |
| 源文档 | `zh_CN/atom/atom_hdriver.md` |

## 概述

Atom HDriver 以 U2 DRV8876PWP 驱动 OUT_N/OUT_P 双向负载，电机电源 VM 直接连接 VIN，IN_1/IN_2 分别由 Atom G19/G23 控制，nFAULT 连接 G22。U1 SY8303A 将 VIN 转换为 SYS_P050，SYS_P050 经 FU1 0.5A 形成 M5_P050，为 Atom 4 Pin 的 5V 供电；同一 SYS_P050 还连接 DRV8876 的 nSLEEP、PMODE 与 VREF 分压。Atom G33 通过 R6 18KΩ、R10 2KΩ 和 C3 105/10V 监测 VIN，J3 同时引出 OUT_N、OUT_P、GND 和 VIN。

## 检索关键词

`Atom HDriver`、`K050`、`DRV8876PWP`、`SY8303A`、`H-bridge`、`DC motor`、`OUT_N`、`OUT_P`、`IN_1`、`IN_2`、`FAULT`、`nFAULT`、`nSLEEP`、`PMODE`、`VREF`、`IPROPI`、`IMODE`、`VM`、`VCP`、`CPH`、`CPL`、`SYS_P050`、`M5_P050`、`VIN`、`VIN-1/10`、`G19`、`G23`、`G22`、`G33`、`Atom SIP5`、`Atom SIP4`、`HT3.96_4P`、`FU1 0.5A`、`R15 10Ω`、`C8 102/50V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | DRV8876PWP | H 桥电机驱动器，连接 Atom 控制、VIN 电机电源与 OUT_N/OUT_P 输出 | 图 39f8ddd46052 / 第 1 页 / 右下 Driver 区域 U2 DRV8876PWP：EN/IN1、PH/IN2、nSLEEP、nFAULT、PMODE、VREF、IPROPI、IMODE、OUT1/OUT2、VM/VCP/CPH/CPL/PAD/GND |
| U1 | SY8303A | VIN 到 SYS_P050 的降压转换器 | 图 39f8ddd46052 / 第 1 页 / 左上 DC-DC 区域 U1 SY8303A：VIN/EN/BS/LX/FB/FS/GND、L1 与 R7/R8/R9 |
| FU1 | 0.5A | SYS_P050 到 M5_P050 的串联保险丝 | 图 39f8ddd46052 / 第 1 页 / 左上 SYS_P050-FU1 0.5A-M5_P050 |
| J3 | HT3.96_4P | 电机输出与 VIN 电源接线端子 | 图 39f8ddd46052 / 第 1 页 / 右上 J3 HT3.96_4P，pins 1~4 为 OUT_N/OUT_P/GND/VIN |
| J2 | SIP5 | Atom 5 Pin 的 3.3V、FAULT、IN_1、IN_2 与 VIN 检测接口 | 图 39f8ddd46052 / 第 1 页 / 左下 J2 SIP5：3V3/G22/G19/G23/G33 与 R3/R4/R5/R6/R10/C3 |
| J1 | SIP4 | Atom 4 Pin 的 G21/G25/5V/GND 接口，其中 5V 接 M5_P050 | 图 39f8ddd46052 / 第 1 页 / 左下 J1 SIP4：G21/G25/5V/GND，5V 网络标 M5_P050 |
| LED1 | LED_GREEN | SYS_P050 电源指示灯 | 图 39f8ddd46052 / 第 1 页 / 左上 SYS_P050-R2 15K/1%-LED1 LED_GREEN-GND |
| L1 | 4.7uH | SY8303A LX 到 SYS_P050 的降压电感 | 图 39f8ddd46052 / 第 1 页 / 左上 U1 LX pin 6-L1 4.7uH-SYS_P050 |
| R15/C8 | 10Ω/1% / 102/50V | OUT_N 与 OUT_P 之间的并联阻容输出网络 | 图 39f8ddd46052 / 第 1 页 / 右下 U2 OUT1/OUT2 之间的 R15 10Ω/1% 与 C8 102/50V |

## 系统结构

### Atom HDriver

电路由 U2 DRV8876PWP H 桥、U1 SY8303A 5V 电源、Atom SIP4/SIP5 接口和 J3 电机/电源端子组成；VIN 同时供给驱动器 VM 与 DC-DC 输入。

- 参数与网络：`motor_driver=U2 DRV8876PWP`；`dc_dc=U1 SY8303A`；`atom=J1 SIP4,J2 SIP5`；`terminal=J3 HT3.96_4P`；`motor_supply=VIN`
- 证据：图 39f8ddd46052 / 第 1 页 / 整页 DC-DC、ATOM SOCKET、Driver 与 J3 四个功能分区

## 电源

### U1 SY8303A 降压

VIN 连接 U1 VIN pin 5 与 EN pin 8，LX pin 6 经 L1 4.7uH 输出 SYS_P050；BS pin 7 通过 C2 104/50V 接 LX，FB pin 1 使用 R7 15K/1% 与 R8 2.2K/1% 分压，FS pin 2 经 R9 200K/1% 接地。

- 参数与网络：`input=VIN`；`converter=U1 SY8303A`；`enable=U1 pin 8 tied to VIN`；`inductor=L1 4.7uH`；`output=SYS_P050`；`bootstrap=C2 104/50V`；`feedback=R7 15K/1%,R8 2.2K/1%`；`frequency=R9 200K/1%`
- 证据：图 39f8ddd46052 / 第 1 页 / 左上 VIN-U1-C2-L1-R7/R8/R9-SYS_P050

### SYS_P050 到 M5_P050

SYS_P050 经 FU1 0.5A 串联后形成 M5_P050，M5_P050 连接 J1 SIP4 的 5V 引脚；SYS_P050 另经 R2 15K/1% 与 LED1 接地。

- 参数与网络：`source=SYS_P050`；`fuse=FU1 0.5A`；`atom_rail=M5_P050`；`atom_connector=J1 5V`；`indicator=R2 15K/1%,LED1 LED_GREEN`
- 证据：图 39f8ddd46052 / 第 1 页 / 左上 SYS_P050-FU1-M5_P050 与 R2-LED1-GND，左下 J1 M5_P050

### DRV8876 VIN 电源

U2 VM pin 11 连接 VIN，C9 104/50V 与 C10 100uF/35V 从 VIN 接 GND；VCP pin 12 通过 C6 104/50V 接 VM/VIN，CPH/CPL pins 13/14 之间接 C7 104/50V。

- 参数与网络：`motor_supply=U2 pin 11 VM VIN`；`supply_caps=C9 104/50V,C10 100uF/35V`；`vcp_cap=C6 104/50V between VCP and VM`；`charge_pump_cap=C7 104/50V between CPH and CPL`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 U2 pins 11~14、C6/C7/C9/C10 与 VIN/GND

### DRV8876 接地

U2 PGND pin 9、GND pin 15 与 PAD pin 0 均连接 GND。

- 参数与网络：`power_ground=pin 9 PGND`；`ground=pin 15 GND`；`thermal_pad=pin 0 PAD`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 U2 pins 9/15/0 到公共 GND

## 接口

### J3 HT3.96_4P

J3 pins 1~4 依次连接 OUT_N、OUT_P、GND、VIN。

- 参数与网络：`pin_1=OUT_N`；`pin_2=OUT_P`；`pin_3=GND`；`pin_4=VIN`
- 证据：图 39f8ddd46052 / 第 1 页 / 右上 J3 HT3.96_4P pins 1~4 与左侧网络

### J1/J2 Atom 插座

J1 SIP4 引出 G21、G25、M5_P050 和 GND；J2 SIP5 引出 3V3、G22/FAULT、G19/IN_1、G23/IN_2、G33/VIN 检测。

- 参数与网络：`sip4=G21,G25,M5_P050,GND`；`sip5_pin_1=3V3`；`sip5_pin_2=G22 FAULT`；`sip5_pin_3=G19 IN_1`；`sip5_pin_4=G23 IN_2`；`sip5_pin_5=G33 VIN monitor`
- 证据：图 39f8ddd46052 / 第 1 页 / 左下 J1 SIP4 与 J2 SIP5 的网络标签及 R3/R4/R5/R6/R10/C3

### DRV8876 OUT_N/OUT_P

U2 OUT1 pin 8 连接 OUT_N 并到 J3 pin 1，OUT2 pin 10 连接 OUT_P 并到 J3 pin 2；R15 10Ω/1% 与 C8 102/50V 均跨接 OUT_N 和 OUT_P。

- 参数与网络：`output_1=U2 pin 8 OUT1-OUT_N-J3 pin 1`；`output_2=U2 pin 10 OUT2-OUT_P-J3 pin 2`；`parallel_resistor=R15 10Ω/1%`；`parallel_capacitor=C8 102/50V`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 U2 pins 8/10 OUT_N/OUT_P-R15/C8 与右上 J3 pins 1/2

## GPIO 与控制信号

### DRV8876 IN_1/IN_2

Atom G19 经 R4 2.2K/1% 连接 IN_1 并到 U2 EN/IN1 pin 1，Atom G23 经 R5 2.2K/1% 连接 IN_2 并到 U2 PH/IN2 pin 2。

- 参数与网络：`input_1=J2 G19-R4 2.2K/1%-IN_1-U2 pin 1`；`input_2=J2 G23-R5 2.2K/1%-IN_2-U2 pin 2`
- 证据：图 39f8ddd46052 / 第 1 页 / 左下 J2 G19/G23-R4/R5-IN_1/IN_2 与右下 U2 pins 1/2

### DRV8876 nFAULT

U2 nFAULT pin 4 连接 FAULT，FAULT 经 R3 15K/1% 连接 Atom G22。

- 参数与网络：`driver_pin=U2 pin 4 nFAULT`；`network=FAULT`；`series_resistor=R3 15K/1%`；`atom_pin=J2 G22`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 U2 pin 4 nFAULT-FAULT 与左下 R3-J2 G22

## 关键网络

### DRV8876 nSLEEP 与 PMODE

U2 nSLEEP pin 3 与 PMODE pin 16 均直接连接 SYS_P050。

- 参数与网络：`sleep=U2 pin 3 nSLEEP SYS_P050`；`phase_mode=U2 pin 16 PMODE SYS_P050`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 SYS_P050 垂直网络连接 U2 pins 3/16

## 模拟电路

### G33 VIN 分压检测

VIN 经 R6 18K/1% 到 G33 检测节点，R10 2K/1% 与 C3 105/10V 从该节点接 GND；电阻比使 G33 节点为 VIN 的 1/10。

- 参数与网络：`input=VIN`；`top_resistor=R6 18K/1%`；`bottom_resistor=R10 2K/1%`；`filter_capacitor=C3 105/10V`；`output=J2 G33`；`ratio=1/10`
- 证据：图 39f8ddd46052 / 第 1 页 / 左下 VIN-R6 18K-G33-R10 2K/C3 105-GND 分压滤波网络

### DRV8876 VREF/IPROPI/IMODE

U2 VREF pin 5 连接 R1 15K/1% 与 R12 15K/1% 的 SYS_P050-GND 分压点，并由 C11 104/50V 接地；IPROPI pin 6 经 R13 1K/1% 接地，IMODE pin 7 经 R14 20K/1% 接地。

- 参数与网络：`vref_top=R1 15K/1% to SYS_P050`；`vref_bottom=R12 15K/1% to GND`；`vref_cap=C11 104/50V to GND`；`ipropi=U2 pin 6-R13 1K/1%-GND`；`imode=U2 pin 7-R14 20K/1%-GND`
- 证据：图 39f8ddd46052 / 第 1 页 / 右下 U2 pins 5/6/7 与 R1/R12/C11/R13/R14/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom HDriver | `motor_driver=U2 DRV8876PWP`；`dc_dc=U1 SY8303A`；`atom=J1 SIP4,J2 SIP5`；`terminal=J3 HT3.96_4P`；`motor_supply=VIN` |
| 电源 | U1 SY8303A 降压 | `input=VIN`；`converter=U1 SY8303A`；`enable=U1 pin 8 tied to VIN`；`inductor=L1 4.7uH`；`output=SYS_P050`；`bootstrap=C2 104/50V`；`feedback=R7 15K/1%,R8 2.2K/1%`；`frequency=R9 200K/1%` |
| 电源 | SYS_P050 到 M5_P050 | `source=SYS_P050`；`fuse=FU1 0.5A`；`atom_rail=M5_P050`；`atom_connector=J1 5V`；`indicator=R2 15K/1%,LED1 LED_GREEN` |
| 接口 | J3 HT3.96_4P | `pin_1=OUT_N`；`pin_2=OUT_P`；`pin_3=GND`；`pin_4=VIN` |
| 接口 | J1/J2 Atom 插座 | `sip4=G21,G25,M5_P050,GND`；`sip5_pin_1=3V3`；`sip5_pin_2=G22 FAULT`；`sip5_pin_3=G19 IN_1`；`sip5_pin_4=G23 IN_2`；`sip5_pin_5=G33 VIN monitor` |
| 模拟电路 | G33 VIN 分压检测 | `input=VIN`；`top_resistor=R6 18K/1%`；`bottom_resistor=R10 2K/1%`；`filter_capacitor=C3 105/10V`；`output=J2 G33`；`ratio=1/10` |
| GPIO 与控制信号 | DRV8876 IN_1/IN_2 | `input_1=J2 G19-R4 2.2K/1%-IN_1-U2 pin 1`；`input_2=J2 G23-R5 2.2K/1%-IN_2-U2 pin 2` |
| GPIO 与控制信号 | DRV8876 nFAULT | `driver_pin=U2 pin 4 nFAULT`；`network=FAULT`；`series_resistor=R3 15K/1%`；`atom_pin=J2 G22` |
| 电源 | DRV8876 VIN 电源 | `motor_supply=U2 pin 11 VM VIN`；`supply_caps=C9 104/50V,C10 100uF/35V`；`vcp_cap=C6 104/50V between VCP and VM`；`charge_pump_cap=C7 104/50V between CPH and CPL` |
| 关键网络 | DRV8876 nSLEEP 与 PMODE | `sleep=U2 pin 3 nSLEEP SYS_P050`；`phase_mode=U2 pin 16 PMODE SYS_P050` |
| 模拟电路 | DRV8876 VREF/IPROPI/IMODE | `vref_top=R1 15K/1% to SYS_P050`；`vref_bottom=R12 15K/1% to GND`；`vref_cap=C11 104/50V to GND`；`ipropi=U2 pin 6-R13 1K/1%-GND`；`imode=U2 pin 7-R14 20K/1%-GND` |
| 接口 | DRV8876 OUT_N/OUT_P | `output_1=U2 pin 8 OUT1-OUT_N-J3 pin 1`；`output_2=U2 pin 10 OUT2-OUT_P-J3 pin 2`；`parallel_resistor=R15 10Ω/1%`；`parallel_capacitor=C8 102/50V` |
| 电源 | DRV8876 接地 | `power_ground=pin 9 PGND`；`ground=pin 15 GND`；`thermal_pad=pin 0 PAD` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `39f8ddd46052a3fd7e9cddc15f16f8d9cc5c8ea368dd23ee06bdd02cd7ae125e` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_hdriver/atom_hdriver_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_hdriver.md`

源文档 SHA-256：`6df146f3904895c90418a693ed5fcee0710e0b0db9c22be818f8ba014f907b2b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
