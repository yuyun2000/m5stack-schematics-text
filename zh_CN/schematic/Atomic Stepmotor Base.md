# Atomic Stepmotor Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Stepmotor Base |
| SKU | A132 |
| 产品 ID | `atomic-stepmotor-base-0cceb8b75518` |
| 源文档 | `zh_CN/atom/Atomic Stepmotor Base.md` |

## 概述

Atomic Stepmotor Base 使用 U2 DRV8825 驱动两相步进电机，J3 接出 M_AP、M_AN、M_BP、M_BN、VIN 和 GND。Atom 的 G22/G19/G23 分别控制 EN/STP/DIR，G21 同时控制 RESET/SLEEP，G25 接收 FAULT；四位 S1 DIP 把 M2/M1/M0/DECAY 分别接到 3.3V。外部 VIN 为驱动器电机电源，并由 U1 JW5033S 降压生成 SYS_P050，经 D1 1N5819 形成 M5_P050 给 Atom 供电。

## 检索关键词

`Atomic Stepmotor Base`、`A132`、`DRV8825`、`JW5033S`、`stepper motor`、`STEP`、`STP`、`DIR`、`EN`、`ENBL`、`RESET`、`SLEEP`、`FAULT`、`M0`、`M1`、`M2`、`DECAY`、`M_AP`、`M_AN`、`M_BP`、`M_BN`、`AVREF`、`BVREF`、`ISENA`、`ISENB`、`0.2R 1/2W`、`S1 DSH-P04T`、`RW1 1K`、`VIN`、`SYS_P050`、`M5_P050`、`J3 CON6`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | JW5033S | 将 VIN 降压为 SYS_P050 的 DC-DC 转换器 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左上，U1 JW5033S 的 VIN/EN/GND、BST/SW/FB 与外围网络 |
| U2 | DRV8825 | 接收 EN/STP/DIR 和模式配置并驱动两相步进电机 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右侧，U2 DRV8825 的控制、模式、VREF、电源、电流采样与 A/B 相输出 |
| J1,J2 | SIP4 / SIP5 | Atom 插座，连接 M5_P050、3V3、GND、RST/FLT/EN/STP/DIR 和 VIN 采样 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左下，J1 SIP4 与 J2 SIP5 的 G21/G25/5V/GND 和 3V3/G22/G19/G23/G33 |
| J3 | CON6 | 接出两相电机四线、VIN 和 GND 的六针端子 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 J3 CON6，pin1-pin6 接 M_AP/M_AN/M_BP/M_BN/VIN/GND |
| S1 | DSH-P04T | 将 M2、M1、M0 和 DECAY 分别选择连接至 3.3V 的四位 DIP 开关 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右下 U2 左侧，S1 DSH-P04T top pins8/7/6/5 接 M2/M1/M0/DECAY，bottom pins1-4 共接 3.3V |
| RW1,R11,C9 | 1KΩ / 1.5KΩ 1% / 105/10V | 为 DRV8825 AVREF/BVREF 提供可调参考电压和滤波 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右下，3.3V-R11-RW1-GND 分压，RW1 滑端接 AVREF/BVREF，C9 对地 |
| R12,R13 | 0.2Ω (1/2W) | DRV8825 A/B 两路 ISENA/ISENB 电流采样电阻 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右侧，U2 ISENA pin6 经 R12 0.2R(1/2W) 到 GND，ISENB pin9 经 R13 到 GND |
| R4,R5,R10 | 7.5KΩ 1% | RST、FLT 和 EN 信号的 3.3V 上拉电阻 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左下 R4/R5 与右上 R10，分别从 RST/FLT/EN 接至 3.3V |
| R6,R9,C4 | 7.5KΩ 1% / 1.5KΩ 1% / 105/10V | VIN 到 Atom G33 的分压滤波网络 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左下，VIN-R6-G33-R9-GND 与 C4 从 G33 到 GND |
| D1 | 1N5819 | 串联连接 SYS_P050 与 M5_P050 的二极管 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左上，D1 1N5819 位于 SYS_P050 与 M5_P050 之间 |
| LED1,R2 | LED_GREEN / 7.5KΩ 1% | SYS_P050 电源状态指示 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左下，SYS_P050 经 R2 7.5K/1% 和 LED1 LED_GREEN 接 GND |
| L1,R7,R8 | 4.7uH / 7.5KΩ 1% / 1.5KΩ 1% | JW5033S 输出电感和反馈分压网络 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左上，L1 位于 SW 与 SYS_P050，R7/R8 连接 SYS_P050、FB 与 GND |
| C8,C10,C11,C12,C13 | 104/50V / 104/50V / 104/50V / 104/50V / 220uF/16V | DRV8825 电荷泵、V3P3OUT 和 VIN 电机电源去耦 | 图 8fc8696fa41f / 第 1 页 / 第 1 页右侧，C8 跨 CP1/CP2，C10 VCP-VIN，C11 V3P3OUT-GND，C12/C13 VIN-GND |
| R1,R3,C1,C2,C5,C6,C7 | 2.2Ω / 7.5KΩ / 226/16V / 104/50V / 226/6.3V / 226/6.3V / 107/6.3V | JW5033S 输入限流/使能、BST 和输出电源网络 | 图 8fc8696fa41f / 第 1 页 / 第 1 页左上，VIN 侧 R1/R3/C1、BST-SW C2、SYS_P050 C5/C6 与 M5_P050 C7 |

## 系统结构

### Atomic Stepmotor Base 控制与供电架构

外部 VIN 为 U2 DRV8825 的 VMA/VMB 电机电源和 U1 JW5033S 输入；U1 生成 SYS_P050，经 D1 形成 M5_P050 给 Atom。Atom 通过 EN/STP/DIR/RST 控制 U2并读取 FLT，U2 的 A/B 两相输出经 J3 接出。

- 参数与网络：`motor_driver=U2 DRV8825`；`dc_dc=U1 JW5033S`；`host=J1/J2 Atom socket`；`power_path=VIN -> U1 -> SYS_P050 -> D1 -> M5_P050`；`control=EN, STP, DIR, RST`；`status=FLT`；`motor_connector=J3 CON6`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页完整单页原理图，左侧 DC-DC/Atom 与右侧 DRV8825/J3

## 核心器件

### DRV8825 未使用针脚

U2 NC pin23 与 HOME pin27 在当前原理图中未连接到其他器件或连接器。

- 参数与网络：`NC=pin23 no external connection`；`HOME=pin27 no external connection`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 NC pin23 与 HOME pin27 的短悬空端点

## 电源

### JW5033S VIN 到 SYS_P050 转换

VIN 经 R1 2.2Ω/1% 接 U1 VIN pin3，EN pin5 通过 R3 7.5KΩ/1% 接同一输入节点，GND pin1 接 GND；SW pin2 经 L1 4.7uH 输出 SYS_P050，C2 104/50V 连接 BST pin6 与 SW。

- 参数与网络：`input=VIN -> R1 2.2R/1% -> VIN pin3`；`enable=EN pin5 through R3 7.5K/1% to input node`；`ground=pin1 GND`；`switch_output=SW pin2 -> L1 4.7uH -> SYS_P050`；`bootstrap=C2 104/50V BST pin6 to SW pin2`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左上 U1 JW5033S 与 R1/R3/C2/L1/VIN/SYS_P050

### JW5033S 反馈和 5V 电源轨

R7 7.5KΩ/1% 从 SYS_P050 接 FB pin4，R8 1.5KΩ/1% 从 FB 接 GND；C5/C6 226/6.3V 连接 SYS_P050 与 GND，SYS_P050 经 D1 1N5819 形成 M5_P050，C7 107/6.3V 连接 M5_P050 与 GND。

- 参数与网络：`feedback_upper=R7 7.5K/1% SYS_P050 to FB`；`feedback_lower=R8 1.5K/1% FB to GND`；`SYS_P050_caps=C5/C6 226/6.3V`；`series_diode=D1 1N5819`；`M5_P050_cap=C7 107/6.3V`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左上 U1 FB、R7/R8、C5/C6、D1 与 C7

### DRV8825 VIN 电机电源和接地

U2 VMA pin4 与 VMB pin11 接 VIN，GND pins14/28 和 PAD pin0 接 GND；C12 104/50V 与 C13 220uF/16V 并联连接 VIN 和 GND。

- 参数与网络：`VMA=pin4 VIN`；`VMB=pin11 VIN`；`grounds=pins14/28 and PAD pin0 GND`；`decoupling=C12 104/50V, C13 220uF/16V`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 VMA/VMB/GND/PAD 与 VIN-GND 电容 C12/C13

### DRV8825 电荷泵与 3.3V 输出

C8 104/50V 连接 U2 CP1 pin1 与 CP2 pin2，C10 104/50V 连接 VCP pin3 与 VIN；V3P3OUT pin15 连接 3.3V，并由 C11 104/50V 对地去耦。

- 参数与网络：`flying_capacitor=C8 104/50V CP1 to CP2`；`VCP_capacitor=C10 104/50V VCP to VIN`；`V3P3OUT=pin15 3.3V`；`V3P3OUT_capacitor=C11 104/50V to GND`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 CP1/CP2/VCP/V3P3OUT 与 C8/C10/C11

## 接口

### Atom 插座信号分配

J1 接出 G21=RST、G25=FLT、5V=M5_P050 和 GND；J2 接出 3V3、G22=EN、G19=STP、G23=DIR、G33=VIN 分压采样。

- 参数与网络：`J1=G21 RST, G25 FLT, 5V M5_P050, GND`；`J2=3V3, G22 EN, G19 STP, G23 DIR, G33 VIN sense`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左下 J1 SIP4/J2 SIP5 与 RST/FLT/EN/STP/DIR/M5_P050/VIN 分压网络

### J3 两相电机与电源端子

J3 CON6 的 pin1=M_AP/AOUT1 pin5、pin2=M_AN/AOUT2 pin7、pin3=M_BP/BOUT1 pin10、pin4=M_BN/BOUT2 pin8、pin5=VIN、pin6=GND。

- 参数与网络：`pin1=M_AP / AOUT1 pin5`；`pin2=M_AN / AOUT2 pin7`；`pin3=M_BP / BOUT1 pin10`；`pin4=M_BN / BOUT2 pin8`；`pin5=VIN`；`pin6=GND`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 AOUT1/AOUT2/BOUT1/BOUT2 线路交叉到 J3 pin1-pin4，以及 VIN/GND pin5/pin6

### SYS_P050 绿色电源指示

SYS_P050 经 R2 7.5KΩ/1% 和 LED1 LED_GREEN 串联连接到 GND。

- 参数与网络：`rail=SYS_P050`；`resistor=R2 7.5K/1%`；`indicator=LED1 LED_GREEN`；`return=GND`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左下 SYS_P050-R2-LED1-GND 支路

## GPIO 与控制信号

### DRV8825 控制与状态信号

U2 ENBL pin21 接 EN/G22 并由 R10 7.5KΩ/1% 上拉至 3.3V，STEP pin22 接 STP/G19，DIR pin20 接 DIR/G23；RESET pin16 与 SLEEP pin17 并联到 RST/G21，FAULT pin18 接 FLT/G25。

- 参数与网络：`EN=Atom G22 -> ENBL pin21, R10 7.5K/1% pull-up`；`STP=Atom G19 -> STEP pin22`；`DIR=Atom G23 -> DIR pin20`；`RST=Atom G21 -> RESET pin16 and SLEEP pin17`；`FLT=FAULT pin18 -> Atom G25`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 ENBL/STEP/DIR/RESET/SLEEP/FAULT 与左侧 Atom 同名网络

### M0/M1/M2 与 DECAY DIP 配置

S1 DSH-P04T 的 switch1 将 MODE2/M2 接 3.3V，switch2 将 MODE1/M1 接 3.3V，switch3 将 MODE0/M0 接 3.3V，switch4 将 DECAY 接 3.3V。

- 参数与网络：`switch1=M2 / MODE2 pin26 to 3.3V`；`switch2=M1 / MODE1 pin25 to 3.3V`；`switch3=M0 / MODE0 pin24 to 3.3V`；`switch4=DECAY pin19 to 3.3V`；`top_pins=8=M2, 7=M1, 6=M0, 5=DECAY`；`bottom_pins=1-4 common 3.3V`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右下 S1 DSH-P04T 与 U2 MODE0/MODE1/MODE2/DECAY 的交叉线路和 3.3V 公共端

## 关键网络

### RST 与 FLT 上拉网络

RST/G21 经 R4 7.5KΩ/1% 上拉到 3V3，FLT/G25 经 R5 7.5KΩ/1% 上拉到 3V3。

- 参数与网络：`RST=R4 7.5K/1% to 3V3`；`FLT=R5 7.5K/1% to 3V3`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左下 J1 G21/G25、R4/R5 与 J2 3V3 节点

## 模拟电路

### G33 VIN 分压滤波

VIN 经 R6 7.5KΩ/1% 接 G33，G33 经 R9 1.5KΩ/1% 接 GND，C4 105/10V 从 G33 接 GND，形成 1/6 分压滤波网络。

- 参数与网络：`upper_resistor=R6 7.5K/1% VIN to G33`；`lower_resistor=R9 1.5K/1% G33 to GND`；`filter_capacitor=C4 105/10V G33 to GND`；`divider_ratio=1/6`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页左下 VIN-R6-G33-R9-GND 与 C4

### DRV8825 AVREF/BVREF 可调参考

3.3V 经 R11 1.5KΩ/1% 和 RW1 1KΩ 串联到 GND，RW1 滑端连接 U2 AVREF pin12 与 BVREF pin13，C9 105/10V 从参考节点接 GND。

- 参数与网络：`source=3.3V`；`series_resistor=R11 1.5K/1%`；`potentiometer=RW1 1K`；`references=AVREF pin12 and BVREF pin13`；`filter=C9 105/10V to GND`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右下，R11/RW1/C9 与 U2 AVREF/BVREF

### A/B 相电流采样电阻

U2 ISENA pin6 通过 R12 0.2Ω (1/2W) 接 GND，ISENB pin9 通过 R13 0.2Ω (1/2W) 接 GND。

- 参数与网络：`phase_A=ISENA pin6 -> R12 0.2R(1/2W) -> GND`；`phase_B=ISENB pin9 -> R13 0.2R(1/2W) -> GND`
- 证据：图 8fc8696fa41f / 第 1 页 / 第 1 页右侧 U2 ISENA/ISENB 与 R12/R13 到底部 GND 轨

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Stepmotor Base 控制与供电架构 | `motor_driver=U2 DRV8825`；`dc_dc=U1 JW5033S`；`host=J1/J2 Atom socket`；`power_path=VIN -> U1 -> SYS_P050 -> D1 -> M5_P050`；`control=EN, STP, DIR, RST`；`status=FLT`；`motor_connector=J3 CON6` |
| 电源 | JW5033S VIN 到 SYS_P050 转换 | `input=VIN -> R1 2.2R/1% -> VIN pin3`；`enable=EN pin5 through R3 7.5K/1% to input node`；`ground=pin1 GND`；`switch_output=SW pin2 -> L1 4.7uH -> SYS_P050`；`bootstrap=C2 104/50V BST pin6 to SW pin2` |
| 电源 | JW5033S 反馈和 5V 电源轨 | `feedback_upper=R7 7.5K/1% SYS_P050 to FB`；`feedback_lower=R8 1.5K/1% FB to GND`；`SYS_P050_caps=C5/C6 226/6.3V`；`series_diode=D1 1N5819`；`M5_P050_cap=C7 107/6.3V` |
| 接口 | Atom 插座信号分配 | `J1=G21 RST, G25 FLT, 5V M5_P050, GND`；`J2=3V3, G22 EN, G19 STP, G23 DIR, G33 VIN sense` |
| GPIO 与控制信号 | DRV8825 控制与状态信号 | `EN=Atom G22 -> ENBL pin21, R10 7.5K/1% pull-up`；`STP=Atom G19 -> STEP pin22`；`DIR=Atom G23 -> DIR pin20`；`RST=Atom G21 -> RESET pin16 and SLEEP pin17`；`FLT=FAULT pin18 -> Atom G25` |
| 关键网络 | RST 与 FLT 上拉网络 | `RST=R4 7.5K/1% to 3V3`；`FLT=R5 7.5K/1% to 3V3` |
| 模拟电路 | G33 VIN 分压滤波 | `upper_resistor=R6 7.5K/1% VIN to G33`；`lower_resistor=R9 1.5K/1% G33 to GND`；`filter_capacitor=C4 105/10V G33 to GND`；`divider_ratio=1/6` |
| GPIO 与控制信号 | M0/M1/M2 与 DECAY DIP 配置 | `switch1=M2 / MODE2 pin26 to 3.3V`；`switch2=M1 / MODE1 pin25 to 3.3V`；`switch3=M0 / MODE0 pin24 to 3.3V`；`switch4=DECAY pin19 to 3.3V`；`top_pins=8=M2, 7=M1, 6=M0, 5=DECAY`；`bottom_pins=1-4 common 3.3V` |
| 模拟电路 | DRV8825 AVREF/BVREF 可调参考 | `source=3.3V`；`series_resistor=R11 1.5K/1%`；`potentiometer=RW1 1K`；`references=AVREF pin12 and BVREF pin13`；`filter=C9 105/10V to GND` |
| 模拟电路 | A/B 相电流采样电阻 | `phase_A=ISENA pin6 -> R12 0.2R(1/2W) -> GND`；`phase_B=ISENB pin9 -> R13 0.2R(1/2W) -> GND` |
| 电源 | DRV8825 VIN 电机电源和接地 | `VMA=pin4 VIN`；`VMB=pin11 VIN`；`grounds=pins14/28 and PAD pin0 GND`；`decoupling=C12 104/50V, C13 220uF/16V` |
| 电源 | DRV8825 电荷泵与 3.3V 输出 | `flying_capacitor=C8 104/50V CP1 to CP2`；`VCP_capacitor=C10 104/50V VCP to VIN`；`V3P3OUT=pin15 3.3V`；`V3P3OUT_capacitor=C11 104/50V to GND` |
| 接口 | J3 两相电机与电源端子 | `pin1=M_AP / AOUT1 pin5`；`pin2=M_AN / AOUT2 pin7`；`pin3=M_BP / BOUT1 pin10`；`pin4=M_BN / BOUT2 pin8`；`pin5=VIN`；`pin6=GND` |
| 核心器件 | DRV8825 未使用针脚 | `NC=pin23 no external connection`；`HOME=pin27 no external connection` |
| 接口 | SYS_P050 绿色电源指示 | `rail=SYS_P050`；`resistor=R2 7.5K/1%`；`indicator=LED1 LED_GREEN`；`return=GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8fc8696fa41f308ba79ac3319671ba63ba6cd5b7162c94a8e96358a7e4f8c7a0` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Stepmotor Base/img-16a88fcb-fc50-42f5-9b58-7c25c5f55cce.webp` |

---

源文档：`zh_CN/atom/Atomic Stepmotor Base.md`

源文档 SHA-256：`c3705ff46ffd84b1018b0a276edccc88974954c5819a5ebc5b2e7fdf75654615`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
