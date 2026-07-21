# Base DIN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base DIN |
| SKU | M132 |
| 产品 ID | `base-din-9b4ada6f179d` |
| 源文档 | `zh_CN/base/DIN BASE.md` |

## 概述

Base DIN 原理图把 DC1 经 D3 和双刀开关 S1 接入 HPWR 与 BUS_BAT，UE1 SY8303AIC 将 HPWR 降压为 BUS_5V；U2 TP4057 以 VCC_5V 为输入并连接 BUS_BAT，Q1/Q2 组成 BUS_5V 到 VCC_5V 的受 PWR 控制通路。J3 M5_BUS 引出电源与 GPIO，J1/J2 Grove 分别使用 GPIO36/GPIO26 与 RXD/TXD。P2/P3 当前页未标出电气连接。

## 检索关键词

`Base DIN`、`M132`、`SY8303AIC`、`TP4057`、`DC-044`、`DSS34`、`SMF30CA`、`SI2301`、`DTC114YUA`、`HPWR`、`BUS_5V`、`VCC_5V`、`BUS_BAT`、`M5_BUS`、`Grove`、`GPIO36`、`GPIO26`、`RXD`、`TXD`、`HT3.96 4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| DC1,D3,S1 | DC-044 / DSS34 / Switch | 直流输入、串联二极管以及 HPWR/BUS_BAT 双刀切换 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A1-A2 Power 区，DC1、D3 与 S1 pins1-6 |
| UE1 | SY8303AIC | 将 HPWR 转换为 BUS_5V 的降压转换器 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，UE1 SY8303AIC 的 VIN/EN/GND/BS/LX/FB/FS |
| D4,C2 | SMF30CA / 10uF | HPWR 对地浪涌抑制与输入去耦 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A2 Power 区，HPWR-D4/C2-GND 并联支路 |
| C1,L1 | 100nF / 10uH | UE1 自举网络与 BUS_5V 输出电感 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，C1 连接 BS/LX，L1 连接 LX/BUS_5V |
| R1,R2,R3,C9 | 120K / 200K / 16K / 22pF | UE1 FB 反馈与 FS 设定网络 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，FB-R1/C9-R3 与 FS-R2 支路 |
| C3,C5,D1 | 10uF / 10uF / TVS 5V | BUS_5V 输出滤波与对地 TVS 保护 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A3 Power 区，BUS_5V-C3/C5/D1-GND 并联支路 |
| U2 | TP4057 | VCC_5V 输入、BUS_BAT 输出的电池充电控制器 | 图 c1548d89f72e / 第 1 页 / 第 1 页 C1-C2 Charge 区，U2 TP4057 的 VCC/CHRG/STDBY/GND/BAT/PROG |
| R6,R8,C6,C7,C8 | 100K / 2K / 100nF / 10uF / 10uF | TP4057 的 PROG、输入和 BUS_BAT 周边网络 | 图 c1548d89f72e / 第 1 页 / 第 1 页 C1-C2 Charge 区，R6/R8/C6/C7/C8 与 U2 周边连接 |
| D2,R7,R11 | 1615RG / 4.7K / 2K | 连接 TP4057 CHRG/STDBY 的红绿状态指示网络 | 图 c1548d89f72e / 第 1 页 / 第 1 页 C1 Charge 区，VCC_5V 经 R7/R11 和 D2 连接 CHRG/STDBY |
| Q1,Q2,R9,R12 | SI2301 / DTC114YUA / 100K / 100K | 受 PWR 控制的 BUS_5V 到 VCC_5V 电源通路 | 图 c1548d89f72e / 第 1 页 / 第 1 页 C2-C3 Charge 区，BUS_5V-Q1-VCC_5V 与 PWR-R9-Q2-R12 门极控制 |
| P1 | SMT_HDR_2x1.25mm | BAT+ 与 GND 的四针电池连接器 | 图 c1548d89f72e / 第 1 页 / 第 1 页 D2 Charge 区，P1 pin1=BAT+，pins2/3/4=GND |
| J1,J2 | GROVE | BUS_5V 供电的 GPIO 与串口 Grove 接口 | 图 c1548d89f72e / 第 1 页 / 第 1 页 A4 Socket 区，J1/J2 IO2/IO1/5V/GND 的网络标签 |
| P2,P3 | HT3.96 4P | 当前原理图页未标出电气网络的四针插座 | 图 c1548d89f72e / 第 1 页 / 第 1 页 B4 Socket 区，P2/P3 pins1-4 均仅画出未接网络的短线 |
| J3 | M5_BUS | 引出 30 针 M5 总线的电源、地与 GPIO 信号 | 图 c1548d89f72e / 第 1 页 / 第 1 页 C3-D4 M5BUS 区，J3 pins1-30 的全部名称与外部网络 |

## 系统结构

### Base DIN 电源与接口架构

DC1 经 D3 和 S1 分配到 HPWR/BUS_BAT，UE1 把 HPWR 降压为 BUS_5V；U2 连接 VCC_5V 与 BUS_BAT，Q1/Q2 构成 BUS_5V 到 VCC_5V 的受控通路。J3 提供 M5_BUS，J1/J2 引出 GPIO 与 RXD/TXD Grove 接口。

- 参数与网络：`dc_input=DC1 DC-044`；`selector=S1`；`buck=UE1 SY8303AIC`；`charger=U2 TP4057`；`bus=J3 M5_BUS`；`grove=J1 GPIO36/GPIO26; J2 RXD/TXD`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页完整单页，Power、Charge、Socket 与 M5BUS 四个功能分区

## 电源

### DC1、D3 与 S1 输入切换

DC1 pin1 形成 PWR 并经 D3 DSS34 到 S1 pin5，DC1 pin2 接 GND，pin3 未画出外部连接。S1 上组由 pin5 在 pin4=HPWR 与 pin6=BUS_BAT 间切换，下组由 pin2=BAT+ 在 pin1=BUS_BAT 与未接网络的 pin3 间切换。

- 参数与网络：`DC1_pin1=PWR -> D3 -> S1 pin5`；`DC1_pin2=GND`；`DC1_pin3=no external connection shown`；`S1_pole_a=pin5 selects pin4 HPWR or pin6 BUS_BAT`；`S1_pole_b=pin2 BAT+ selects pin1 BUS_BAT or pin3 unconnected`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A1-A2 Power 区，DC1/D3/S1 与 PWR/HPWR/BUS_BAT/BAT+ 标签

### SY8303AIC 输入、使能与接地

UE1 VIN pin5 与 EN pin8 均接 HPWR，GND pins3/4 接 GND。

- 参数与网络：`VIN_pin5=HPWR`；`EN_pin8=HPWR`；`GND_pins3_4=GND`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A2 Power 区，UE1 left-side pins5/8/3/4

### SY8303AIC BUS_5V 降压输出

UE1 LX pin6 经 L1 10uH 连接 BUS_5V，C1 100nF 连接 BS pin7 与 LX 节点。

- 参数与网络：`LX_pin6=L1 10uH -> BUS_5V`；`bootstrap=C1 100nF between BS pin7 and LX`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，UE1 BS/LX、C1、L1 与 BUS_5V

### SY8303AIC 反馈与 FS 网络

FB pin1 通过并联的 R1 120K 与 C9 22pF 连接 BUS_5V，并通过 R3 16K 接 GND；FS pin2 通过 R2 200K 接 GND。

- 参数与网络：`FB_upper=R1 120K parallel C9 22pF to BUS_5V`；`FB_lower=R3 16K to GND`；`FS=R2 200K to GND`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，UE1 FB/FS 和 R1/R2/R3/C9

### TP4057 充电网络

U2 VCC pin4 接 VCC_5V，BAT pin3 接 BUS_BAT，GND pin2 接 GND，PROG pin6 经 R8 2K 接 GND；C8 10uF 从 VCC_5V 接 GND，C6 100nF 与 C7 10uF 从 BUS_BAT 接 GND，R6 100K 连接 VCC_5V 与 BUS_BAT。

- 参数与网络：`VCC_pin4=VCC_5V`；`BAT_pin3=BUS_BAT`；`GND_pin2=GND`；`PROG_pin6=R8 2K -> GND`；`input_cap=C8 10uF`；`battery_caps=C6 100nF; C7 10uF`；`VCC_to_BAT=R6 100K`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C1-C2 Charge 区，U2 与 R6/R8/C6/C7/C8

### BUS_5V 到 VCC_5V 控制通路

Q1 SI2301 位于 BUS_5V 与 VCC_5V 之间；其门极通过 R12 100K 上拉到 BUS_5V，并连接 Q2 DTC114YUA，Q2 发射极接 GND，PWR 经 R9 100K 接入 Q2 输入。

- 参数与网络：`pass_device=Q1 SI2301 BUS_5V to VCC_5V`；`gate_pullup=R12 100K to BUS_5V`；`gate_control=Q2 DTC114YUA to GND`；`control_input=PWR through R9 100K`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C2-C3 Charge 区，Q1/Q2/R9/R12 与 PWR/BUS_5V/VCC_5V/GND

## 接口

### TP4057 红绿状态指示

D2 1615RG 的绿色支路由 VCC_5V 经 R7 4.7K 连接 CHRG pin1，红色支路由 VCC_5V 经 R11 2K 连接 STDBY pin5。

- 参数与网络：`green=VCC_5V -> R7 4.7K -> D2 green -> CHRG pin1`；`red=VCC_5V -> R11 2K -> D2 red -> STDBY pin5`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C1 Charge 区，D2 两色 LED 到 U2 CHRG/STDBY 的连线

### P1 电池连接器

P1 SMT_HDR_2x1.25mm 的 pin1 接 BAT+，pins2/3/4 均接 GND。

- 参数与网络：`pin1=BAT+`；`pin2=GND`；`pin3=GND`；`pin4=GND`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 D2 Charge 区，P1 pins1-4 与 BAT+/GND

### J1 GPIO Grove 接口

J1 Grove 的 IO2 接 GPIO36、IO1 接 GPIO26、5V 接 BUS_5V、GND 接 GND。

- 参数与网络：`IO2=GPIO36`；`IO1=GPIO26`；`5V=BUS_5V`；`GND=GND`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A4 Socket 区，J1 IO2/IO1/5V/GND

### J2 串口 Grove 接口

J2 Grove 的 IO2 接 RXD、IO1 接 TXD、5V 接 BUS_5V、GND 接 GND。

- 参数与网络：`IO2=RXD`；`IO1=TXD`；`5V=BUS_5V`；`GND=GND`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A4 Socket 区，J2 IO2/IO1/5V/GND

### P2/P3 HT3.96 四针插座

P2 与 P3 均标注 HT3.96 4P；当前原理图页仅画出 pins1-4 的悬空短线，没有标出网络名或到其他电路的连接。

- 参数与网络：`P2=pins1-4 no electrical network shown`；`P3=pins1-4 no electrical network shown`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 B4 Socket 区，P2/P3 HT3.96 4P 与四条未接网络短线

## 总线

### J3 M5_BUS 电源与地针脚

J3 pins2/4/6 接 GND，pin11=VDD_3V3，pins26/28/30=HPWR，pin27=5V 并接 BUS_5V，pin29=VBAT 并接 BUS_BAT。

- 参数与网络：`GND=pins2,4,6`；`VDD_3V3=pin11`；`HPWR=pins26,28,30`；`BUS_5V=pin27`；`BUS_BAT=pin29`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C3-D4 M5BUS 区，J3 GND/VDD_3V3/HPWR/5V/VBAT 针脚

### J3 M5_BUS pins1-16 信号

J3 pin1=G35、pin3=G36/ADC、pin5=EN/RST、pin7=G25/DAC、pin8=G23/MOSI、pin9=G26/DAC、pin10=G19/MISO、pin12=G18/SCK、pin13=G1/TXD0、pin14=G3/RXD0、pin15=G17/TXD2、pin16=G16/RXD2。

- 参数与网络：`pin1=G35`；`pin3=G36/ADC`；`pin5=EN/RST`；`pin7=G25/DAC`；`pin8=G23/MOSI`；`pin9=G26/DAC`；`pin10=G19/MISO`；`pin12=G18/SCK`；`pin13=G1/TXD0`；`pin14=G3/RXD0`；`pin15=G17/TXD2`；`pin16=G16/RXD2`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C3-D4 M5BUS 区，J3 pins1-16 内部标签

### J3 M5_BUS pins17-25 信号

J3 pin17=G22/IIC_SCL、pin18=G21/IIS_SDA、pin19=G5、pin20=G2、pin21=G13/IIS_WS、pin22=G12/IIS_SK、pin23=G0/IIS_MK、pin24=G15/IIS_OUT、pin25=G34/IIS_IN。

- 参数与网络：`pin17=G22/IIC_SCL`；`pin18=G21/IIS_SDA`；`pin19=G5`；`pin20=G2`；`pin21=G13/IIS_WS`；`pin22=G12/IIS_SK`；`pin23=G0/IIS_MK`；`pin24=G15/IIS_OUT`；`pin25=G34/IIS_IN`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 C3-D4 M5BUS 区，J3 pins17-25 内部标签

### Grove 网络到 M5_BUS 的映射

GPIO36 从 J1 IO2 对应到 J3 pin3，GPIO26 从 J1 IO1 对应到 J3 pin9；RXD 从 J2 IO2 对应到 J3 pin16，TXD 从 J2 IO1 对应到 J3 pin15；J1/J2 的 BUS_5V 对应 J3 pin27。

- 参数与网络：`J1_IO2=GPIO36 -> J3 pin3`；`J1_IO1=GPIO26 -> J3 pin9`；`J2_IO2=RXD -> J3 pin16`；`J2_IO1=TXD -> J3 pin15`；`power=BUS_5V -> J3 pin27`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A4 Socket 区与 C3-D4 M5BUS 区的同名网络标签

## 保护电路

### HPWR 与 BUS_5V 保护和去耦

HPWR 通过 D4 SMF30CA 与 C2 10uF 并联到 GND；BUS_5V 通过 C3/C5 两个 10uF 电容和 D1 TVS 5V 并联到 GND。

- 参数与网络：`HPWR_TVS=D4 SMF30CA`；`HPWR_cap=C2 10uF`；`BUS_5V_caps=C3/C5 10uF`；`BUS_5V_TVS=D1 TVS 5V`
- 证据：图 c1548d89f72e / 第 1 页 / 第 1 页 A2-A3 Power 区，HPWR 与 BUS_5V 两侧的对地器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base DIN 电源与接口架构 | `dc_input=DC1 DC-044`；`selector=S1`；`buck=UE1 SY8303AIC`；`charger=U2 TP4057`；`bus=J3 M5_BUS`；`grove=J1 GPIO36/GPIO26; J2 RXD/TXD` |
| 电源 | DC1、D3 与 S1 输入切换 | `DC1_pin1=PWR -> D3 -> S1 pin5`；`DC1_pin2=GND`；`DC1_pin3=no external connection shown`；`S1_pole_a=pin5 selects pin4 HPWR or pin6 BUS_BAT`；`S1_pole_b=pin2 BAT+ selects pin1 BUS_BAT or pin3 unconnected` |
| 保护电路 | HPWR 与 BUS_5V 保护和去耦 | `HPWR_TVS=D4 SMF30CA`；`HPWR_cap=C2 10uF`；`BUS_5V_caps=C3/C5 10uF`；`BUS_5V_TVS=D1 TVS 5V` |
| 电源 | SY8303AIC 输入、使能与接地 | `VIN_pin5=HPWR`；`EN_pin8=HPWR`；`GND_pins3_4=GND` |
| 电源 | SY8303AIC BUS_5V 降压输出 | `LX_pin6=L1 10uH -> BUS_5V`；`bootstrap=C1 100nF between BS pin7 and LX` |
| 电源 | SY8303AIC 反馈与 FS 网络 | `FB_upper=R1 120K parallel C9 22pF to BUS_5V`；`FB_lower=R3 16K to GND`；`FS=R2 200K to GND` |
| 电源 | TP4057 充电网络 | `VCC_pin4=VCC_5V`；`BAT_pin3=BUS_BAT`；`GND_pin2=GND`；`PROG_pin6=R8 2K -> GND`；`input_cap=C8 10uF`；`battery_caps=C6 100nF; C7 10uF`；`VCC_to_BAT=R6 100K` |
| 接口 | TP4057 红绿状态指示 | `green=VCC_5V -> R7 4.7K -> D2 green -> CHRG pin1`；`red=VCC_5V -> R11 2K -> D2 red -> STDBY pin5` |
| 电源 | BUS_5V 到 VCC_5V 控制通路 | `pass_device=Q1 SI2301 BUS_5V to VCC_5V`；`gate_pullup=R12 100K to BUS_5V`；`gate_control=Q2 DTC114YUA to GND`；`control_input=PWR through R9 100K` |
| 接口 | P1 电池连接器 | `pin1=BAT+`；`pin2=GND`；`pin3=GND`；`pin4=GND` |
| 接口 | J1 GPIO Grove 接口 | `IO2=GPIO36`；`IO1=GPIO26`；`5V=BUS_5V`；`GND=GND` |
| 接口 | J2 串口 Grove 接口 | `IO2=RXD`；`IO1=TXD`；`5V=BUS_5V`；`GND=GND` |
| 接口 | P2/P3 HT3.96 四针插座 | `P2=pins1-4 no electrical network shown`；`P3=pins1-4 no electrical network shown` |
| 总线 | J3 M5_BUS 电源与地针脚 | `GND=pins2,4,6`；`VDD_3V3=pin11`；`HPWR=pins26,28,30`；`BUS_5V=pin27`；`BUS_BAT=pin29` |
| 总线 | J3 M5_BUS pins1-16 信号 | `pin1=G35`；`pin3=G36/ADC`；`pin5=EN/RST`；`pin7=G25/DAC`；`pin8=G23/MOSI`；`pin9=G26/DAC`；`pin10=G19/MISO`；`pin12=G18/SCK`；`pin13=G1/TXD0`；`pin14=G3/RXD0`；`pin15=G17/TXD2`；`pin16=G16/RXD2` |
| 总线 | J3 M5_BUS pins17-25 信号 | `pin17=G22/IIC_SCL`；`pin18=G21/IIS_SDA`；`pin19=G5`；`pin20=G2`；`pin21=G13/IIS_WS`；`pin22=G12/IIS_SK`；`pin23=G0/IIS_MK`；`pin24=G15/IIS_OUT`；`pin25=G34/IIS_IN` |
| 总线 | Grove 网络到 M5_BUS 的映射 | `J1_IO2=GPIO36 -> J3 pin3`；`J1_IO1=GPIO26 -> J3 pin9`；`J2_IO2=RXD -> J3 pin16`；`J2_IO1=TXD -> J3 pin15`；`power=BUS_5V -> J3 pin27` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c1548d89f72e6124d5633f0cd14460607633bdc235e5b0e2d6d1ecaa0721891a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1_sch_01.png` |

---

源文档：`zh_CN/base/DIN BASE.md`

源文档 SHA-256：`6b8ca9067e9c3066d743c8b4e7d829e6fbcd49b194cbc7fb567b6d2780724e47`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
