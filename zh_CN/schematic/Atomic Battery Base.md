# Atomic Battery Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Battery Base |
| SKU | A151 |
| 产品 ID | `atomic-battery-base-cdc6e6b48c99` |
| 源文档 | `zh_CN/atom/Atomic Battery Base.md` |

## 概述

Atomic Battery Base 通过 P3 连接电池，SW1 将 BAT 在 BAT_IN 升压路径和 VBAT_OUT 充电路径之间切换。U1 ETA9085E10 以电池为输入生成 5V，并驱动 D1-D4 四个红色电量指示灯；U2 LGS4056HDA 通过 Q1/Q2 控制的 Charg_5V 路径为电池充电，图中给出的充电电流为 0.0989A。P1/P2 接出 Atom 的 5V、3V3 和 GPIO，GPIO33 还连接 BAT 的 1MΩ/1MΩ 分压中点。

## 检索关键词

`Atomic Battery Base`、`A151`、`ETA9085E10`、`LGS4056HDA`、`AP40P05`、`battery charger`、`5V Boost`、`Charger`、`BAT`、`BAT_IN`、`VBAT_OUT`、`Charg_5V`、`SW1`、`SW-PWR`、`GPIO33`、`battery voltage divider`、`1MΩ`、`2.2uH`、`98.9mA`、`CHRG`、`DONE`、`D1 D2 D3 D4`、`battery level indicator`、`D5 Blue 0603`、`D6 Green 0603`、`P1 Header 4`、`P2 Header 5`、`P3 Battery Pad`、`5V`、`3V3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ETA9085E10 | 将 BAT_IN 电池电源升压为 5V，并驱动四个电量指示灯 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2-A3，U1 ETA9085E10 的 BAT/SW/ENBST、OUT、LED1/LED2/LED3 与 EP |
| U2 | LGS4056HDA | 由 Charg_5V 供电并通过 VBAT_OUT 为电池充电的线性充电器 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2-C3，U2 LGS4056HDA 的 TEMP/PROG/GND/VCC/CE/CHRG/DONE/BAT/PAD |
| SW1 | SW-PWR | 在 BAT_IN 升压模式与 VBAT_OUT 充电模式之间切换电池正极 BAT | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B3，SW1 pin2 接 BAT、pin3 接 BAT_IN、pin1 接 VBAT_OUT，旁注 5V Boost/Charger |
| P1,P2 | Header 4 / Header 5 | 连接 Atom 的 5V、3V3、GND 与 GPIO21/GPIO25/GPIO22/GPIO19/GPIO23/GPIO33 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B1-B2，P1 Header 4 与 P2 Header 5 的完整针脚网络标注 |
| P3 | Battery Pad | 电池连接焊盘，pin2 为 BAT 正极、pin1 为 GND | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B3，P3 Battery Pad，pin2 标有正号并接 BAT，pin1 接 GND |
| L1 | 2.2uH/2520 | ETA9085E10 BAT_IN 与 SW pin5 之间的升压电感 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2，L1 2.2uH/2520 连接 BAT_IN 与 U1 SW pin5 |
| Q1,Q2 | AP40P05 | 根据 BAT_IN 控制 5V 到 Charg_5V 的充电输入开关网络 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C1-C2，Q1/Q2 AP40P05、R9/R12/R13 与 5V、Charg_5V、BAT_IN、GND |
| D1,D2,D3,D4 | RED | ETA9085E10 驱动的四级电池电量指示灯 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A3-A4，D1-D4 RED、R1/R3 330R 及 Battery Voltage Level Indicator 表 |
| D5,D6 | Blue 0603 / Green 0603 | 分别由 U2 CHRG 和 DONE 状态输出控制的充电状态指示灯 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C3，D5 Blue 0603 与 R11 330R、D6 Green 0603 与 R10 330R |
| R14,R6,R5 | 1MΩ / 1MΩ / NC | BAT 到 GPIO33 的 1:1 分压和可选 BAT_IN 接入网络 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B2，R14 1M 从 BAT 到 GPIO33、R6 1M 从 GPIO33 到 GND、R5 NC 从 BAT_IN 到 GPIO33 |
| R8 | 9.1KΩ | LGS4056HDA PROG pin2 的充电电流设定电阻 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2，R8 9.1K 连接 U2 PROG pin2 与 GND，旁注 IBAT=900/RPROG |
| C1,C2,C3,C6 | 22uF / 22uF / 100nF / 4.7uF | ETA9085E10 的 5V 输出和 BAT_IN 输入去耦 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2-A3，C1/C2 22uF 从 5V 到 GND，C3 100nF 与 C6 4.7uF 从 BAT_IN 到 GND |
| C4,R7,C5 | 10uF / 1.2Ω / 100nF NC | LGS4056HDA 输入 RC 支路及可选电池端电容 | 图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2-C3，Charg_5V 经 R7 1.2Ω 与 C4 10uF 到 GND，VBAT_OUT 经 C5 100nF/NC 到 GND |

## 系统结构

### Atomic Battery Base 双模式电源架构

P3 的电池正极形成 BAT，SW1 将 BAT 切换到 BAT_IN 时由 U1 ETA9085E10 升压产生 5V，切换到 VBAT_OUT 时由 U2 LGS4056HDA 连接充电路径；P1/P2 将电源和 GPIO 接至 Atom。

- 参数与网络：`battery_connector=P3 Battery Pad`；`mode_switch=SW1 SW-PWR`；`boost_path=BAT -> BAT_IN -> U1 ETA9085E10 -> 5V`；`charge_path=5V -> Q1/Q2 -> Charg_5V -> U2 LGS4056HDA -> VBAT_OUT -> BAT`；`atom_connectors=P1 Header 4, P2 Header 5`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页完整单页原理图，A2-A4 升压、B1-B3 接口与开关、C1-C3 充电

## 核心器件

### 原理图明确标注的 NC 项

U1 VIN pin1 与 ISET pin3 带 no-connect 标记；R4 标为 NC 并位于 U1 NTC pin7 与 GND 之间；R5 标为 NC 并位于 BAT_IN 与 GPIO33 之间；C5 标为 100nF/NC。

- 参数与网络：`U1_VIN=pin1 no-connect`；`U1_ISET=pin3 no-connect`；`R4=NC, U1 NTC pin7 to GND`；`R5=NC, BAT_IN to GPIO33`；`C5=100nF/NC, VBAT_OUT to GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2 的 U1 VIN/ISET 与 R4 NC、B2 的 R5 NC、C3 的 C5 100nF/NC

## 电源

### SW1 升压与充电模式选择

SW1 pin2 为 BAT 公共端，pin3 接 BAT_IN，图注为开关向右选择 5V Boost；pin1 接 VBAT_OUT，图注为开关向左选择 Charger。

- 参数与网络：`common=pin2 BAT`；`boost_position=pin2 BAT to pin3 BAT_IN, switch to the right`；`charge_position=pin2 BAT to pin1 VBAT_OUT, switch to the left`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B3，SW1 pin1/pin2/pin3 与 5V Boost (switch to the right)/Charger (switch to the left) 注释

### ETA9085E10 5V 升压路径

U1 BAT pin2 和 ENBST pin4 接 BAT_IN，SW pin5 通过 L1 2.2uH/2520 接 BAT_IN，OUT pin6 输出 5V，EP pin11 接 GND。

- 参数与网络：`battery_input=pin2 BAT = BAT_IN`；`enable=pin4 ENBST = BAT_IN`；`switching_node=pin5 SW through L1 2.2uH/2520 to BAT_IN`；`output=pin6 OUT = 5V`；`exposed_pad=pin11 EP = GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2-A3，U1 BAT/SW/ENBST/OUT/EP 与 BAT_IN、L1、5V、GND

### 升压输入输出去耦

C3 100nF 与 C6 4.7uF 并联连接 BAT_IN 和 GND；C1/C2 两个 22uF 电容并联连接 5V 和 GND。

- 参数与网络：`input_decoupling=C3 100nF, C6 4.7uF`；`output_decoupling=C1 22uF, C2 22uF`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A2-A3，BAT_IN 侧 C3/C6 与 5V 侧 C1/C2

### 5V 到 Charg_5V 控制网络

Q1/Q2 均标注 AP40P05；Q1 位于 5V 与 Charg_5V 之间，R9 10K 从 5V 接 Q1/Q2 控制节点，BAT_IN 经 R12 1K 接 Q2 控制端，R13 1M 将该控制端下拉到 GND。

- 参数与网络：`series_switch=Q1 AP40P05 between 5V and Charg_5V`；`control_device=Q2 AP40P05`；`gate_bias=R9 10K to 5V`；`BAT_IN_drive=R12 1K`；`pulldown=R13 1M to GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C1-C2，Q1/Q2 AP40P05 与 R9/R12/R13、5V、Charg_5V、BAT_IN、GND

### LGS4056HDA 充电器连接

U2 VCC pin4 与 CE pin8 接 Charg_5V，BAT pin5 接 VBAT_OUT，TEMP pin1、GND pin3 和 PAD pin9 接 GND；PROG pin2 通过 R8 9.1KΩ 接 GND。

- 参数与网络：`VCC=pin4 Charg_5V`；`CE=pin8 Charg_5V`；`BAT=pin5 VBAT_OUT`；`TEMP=pin1 GND`；`GND=pin3 GND`；`PAD=pin9 GND`；`PROG=pin2 through R8 9.1KΩ to GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2-C3，U2 LGS4056HDA 全部电源、控制和电池针脚连接

### 充电电流设定

原理图按 IBAT=900/RPROG 计算，R8 为 9.1KΩ，对应标注的 900/9100=0.0989A 充电电流。

- 参数与网络：`formula=IBAT=900/RPROG`；`RPROG=R8 9.1KΩ`；`annotated_current=0.0989A`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2，U2 下方 Charging Current: IBAT=900/RPROG, 900/9100=0.0989A 注释

### 充电器输入与电池端无源网络

Charg_5V 经 R7 1.2Ω 和 C4 10uF 串联支路接 GND；U2 BAT/VBAT_OUT 端的 C5 标注为 100nF/NC，因此该位置不装配。

- 参数与网络：`input_branch=Charg_5V -> R7 1.2Ω -> C4 10uF -> GND`；`battery_capacitor=C5 100nF/NC from VBAT_OUT to GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C2-C3，C4/R7 的 Charg_5V-GND 支路与 C5 100nF/NC 的 VBAT_OUT-GND 位置

## 接口

### Atom 连接器针脚映射

P1 Header 4 的 pin1=GND、pin2=5V、pin3=GPIO25、pin4=GPIO21；P2 Header 5 的 pin1=GPIO33、pin2=GPIO23、pin3=GPIO19、pin4=GPIO22、pin5=3V3。图中 GPIO21、GPIO25、GPIO22、GPIO19、GPIO23 的网络端以 no-connect 标记结束。

- 参数与网络：`P1=pin1 GND, pin2 5V, pin3 GPIO25, pin4 GPIO21`；`P2=pin1 GPIO33, pin2 GPIO23, pin3 GPIO19, pin4 GPIO22, pin5 3V3`；`unused_in_base=GPIO21, GPIO25, GPIO22, GPIO19, GPIO23`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B1-B2，P1/P2 针脚编号、网络名与红色 no-connect 标记

### P3 电池焊盘

P3 Battery Pad 的 pin2 为电池正极 BAT，pin1 为 GND。

- 参数与网络：`pin2=BAT (+)`；`pin1=GND`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B3，P3 Battery Pad 的 + 标记、BAT 网络和 GND

### D1-D4 电池电量显示规则

放电时，75%<C≤100% 点亮 D1-D4；50%<C≤75% 点亮 D1-D3；25%<C≤50% 点亮 D1-D2；3%<C≤25% 仅点亮 D1；C≤3% 时 D1 以 1Hz 闪烁，其余熄灭。

- 参数与网络：`75_to_100_percent=D1 on, D2 on, D3 on, D4 on`；`50_to_75_percent=D1 on, D2 on, D3 on, D4 off`；`25_to_50_percent=D1 on, D2 on, D3 off, D4 off`；`3_to_25_percent=D1 on, D2 off, D3 off, D4 off`；`at_or_below_3_percent=D1 1Hz flash, D2 off, D3 off, D4 off`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A3-A4，Table 1 D1, D2, D3, D4 Battery Voltage Level Indicator

### 充电与完成状态指示灯

U2 CHRG pin7 连接 D5 Blue 0603，U2 DONE pin6 连接 D6 Green 0603；D5/D6 分别通过 R11/R10 330R 接 Charg_5V。

- 参数与网络：`charging=pin7 CHRG -> D5 Blue 0603 -> R11 330R -> Charg_5V`；`done=pin6 DONE -> D6 Green 0603 -> R10 330R -> Charg_5V`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 C3，U2 CHRG/DONE 与 D5/D6、R11/R10 和 Charg_5V

## 关键网络

### ETA9085E10 电量灯驱动网络

U1 LED1 pin8 通过 R1 330R 接 D1/D2 上侧节点，LED3 pin10 接 D1/D2 与 D3/D4 的中间节点，LED2 pin9 通过 R3 330R 接 D3/D4 下侧节点。

- 参数与网络：`LED1=pin8 through R1 330R`；`LED3=pin10 to middle LED node`；`LED2=pin9 through R3 330R`；`indicators=D1-D4 RED`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 A3，U1 LED1/LED3/LED2、R1/R3 330R 与 D1-D4 RED

## 模拟电路

### GPIO33 电池电压分压

R14 1MΩ 从 BAT 接 GPIO33，R6 1MΩ 从 GPIO33 接 GND，构成等值分压；R5 标为 NC，位于 BAT_IN 与 GPIO33 之间。

- 参数与网络：`upper_resistor=R14 1MΩ BAT to GPIO33`；`lower_resistor=R6 1MΩ GPIO33 to GND`；`divider_ratio=1/2`；`optional_input=R5 NC BAT_IN to GPIO33`
- 证据：图 621a3d6ea2a7 / 第 1 页 / 第 1 页 B2，BAT-R14-GPIO33-R6-GND 分压链与 R5 NC

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Battery Base 双模式电源架构 | `battery_connector=P3 Battery Pad`；`mode_switch=SW1 SW-PWR`；`boost_path=BAT -> BAT_IN -> U1 ETA9085E10 -> 5V`；`charge_path=5V -> Q1/Q2 -> Charg_5V -> U2 LGS4056HDA -> VBAT_OUT -> BAT`；`atom_connectors=P1 Header 4, P2 Header 5` |
| 接口 | Atom 连接器针脚映射 | `P1=pin1 GND, pin2 5V, pin3 GPIO25, pin4 GPIO21`；`P2=pin1 GPIO33, pin2 GPIO23, pin3 GPIO19, pin4 GPIO22, pin5 3V3`；`unused_in_base=GPIO21, GPIO25, GPIO22, GPIO19, GPIO23` |
| 接口 | P3 电池焊盘 | `pin2=BAT (+)`；`pin1=GND` |
| 电源 | SW1 升压与充电模式选择 | `common=pin2 BAT`；`boost_position=pin2 BAT to pin3 BAT_IN, switch to the right`；`charge_position=pin2 BAT to pin1 VBAT_OUT, switch to the left` |
| 电源 | ETA9085E10 5V 升压路径 | `battery_input=pin2 BAT = BAT_IN`；`enable=pin4 ENBST = BAT_IN`；`switching_node=pin5 SW through L1 2.2uH/2520 to BAT_IN`；`output=pin6 OUT = 5V`；`exposed_pad=pin11 EP = GND` |
| 电源 | 升压输入输出去耦 | `input_decoupling=C3 100nF, C6 4.7uF`；`output_decoupling=C1 22uF, C2 22uF` |
| 接口 | D1-D4 电池电量显示规则 | `75_to_100_percent=D1 on, D2 on, D3 on, D4 on`；`50_to_75_percent=D1 on, D2 on, D3 on, D4 off`；`25_to_50_percent=D1 on, D2 on, D3 off, D4 off`；`3_to_25_percent=D1 on, D2 off, D3 off, D4 off`；`at_or_below_3_percent=D1 1Hz flash, D2 off, D3 off, D4 off` |
| 关键网络 | ETA9085E10 电量灯驱动网络 | `LED1=pin8 through R1 330R`；`LED3=pin10 to middle LED node`；`LED2=pin9 through R3 330R`；`indicators=D1-D4 RED` |
| 模拟电路 | GPIO33 电池电压分压 | `upper_resistor=R14 1MΩ BAT to GPIO33`；`lower_resistor=R6 1MΩ GPIO33 to GND`；`divider_ratio=1/2`；`optional_input=R5 NC BAT_IN to GPIO33` |
| 电源 | 5V 到 Charg_5V 控制网络 | `series_switch=Q1 AP40P05 between 5V and Charg_5V`；`control_device=Q2 AP40P05`；`gate_bias=R9 10K to 5V`；`BAT_IN_drive=R12 1K`；`pulldown=R13 1M to GND` |
| 电源 | LGS4056HDA 充电器连接 | `VCC=pin4 Charg_5V`；`CE=pin8 Charg_5V`；`BAT=pin5 VBAT_OUT`；`TEMP=pin1 GND`；`GND=pin3 GND`；`PAD=pin9 GND`；`PROG=pin2 through R8 9.1KΩ to GND` |
| 电源 | 充电电流设定 | `formula=IBAT=900/RPROG`；`RPROG=R8 9.1KΩ`；`annotated_current=0.0989A` |
| 接口 | 充电与完成状态指示灯 | `charging=pin7 CHRG -> D5 Blue 0603 -> R11 330R -> Charg_5V`；`done=pin6 DONE -> D6 Green 0603 -> R10 330R -> Charg_5V` |
| 电源 | 充电器输入与电池端无源网络 | `input_branch=Charg_5V -> R7 1.2Ω -> C4 10uF -> GND`；`battery_capacitor=C5 100nF/NC from VBAT_OUT to GND` |
| 核心器件 | 原理图明确标注的 NC 项 | `U1_VIN=pin1 no-connect`；`U1_ISET=pin3 no-connect`；`R4=NC, U1 NTC pin7 to GND`；`R5=NC, BAT_IN to GPIO33`；`C5=100nF/NC, VBAT_OUT to GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `621a3d6ea2a72e89209ba3eef435cddb790788e9e56a3d11469665d6e6eb9a2f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1130/A151_SCH_Atomic_Battery_Base_V1.1_2025_03_11_10_49_15_page_01.png` |

---

源文档：`zh_CN/atom/Atomic Battery Base.md`

源文档 SHA-256：`e8c7cc327453c657ac0b9600ddc76596321a8c1fe059216931b25f24348ef3fe`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
