# Atom PWM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom PWM |
| SKU | K065 |
| 产品 ID | `atom-pwm-604957966ccb` |
| 源文档 | `zh_CN/atom/atom_pwm.md` |

## 概述

Atom PWM 以 U2 EG27324 栅极驱动器和 Q1 FDD8447L N 沟道 MOSFET 构成单通道低边 PWM 开关，Atom G22/PWM 经 U2 OUTA 与 R7 100Ω 驱动 Q1，R8/R9 提供输入与栅极下拉。外部 DC12~24V 输入形成 +VIN，U1 ME3116AM6G 将其转换为 +5VIN，并通过 Atom Header 4 的 5V 引脚供电；J1 将 MOSFET 漏极标为 LED-，并引出 LED+、12V+ 与 12V-。+MOSV 逻辑电源同时画有 R5 从 +5VIN 和 R6 从 +3.3V 的 0Ω 选择路径，但页面未标实际装配项。

## 检索关键词

`Atom PWM`、`K065`、`EG27324`、`FDD8447L`、`ME3116AM6G`、`PWM`、`G22`、`INA`、`OUTA`、`N-MOSFET`、`low-side switch`、`LED-`、`LED+`、`12V+`、`12V-`、`+VIN`、`+5VIN`、`+MOSV`、`+3.3V`、`DC12~24V`、`B5819W SL`、`SD24`、`R5 0Ω`、`R6 0Ω`、`R7 100Ω`、`R8 10KΩ`、`R9 10KΩ`、`Header 5`、`Header 4`、`HDR_4P_3.96`、`red LED 0603`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | EG27324 | PWM 栅极驱动器，INA 接 PWM，OUTA 驱动 Q1 栅极 | 图 9471fef4dad6 / 第 1 页 / 左下 U2 EG27324：NC/INA/GND/INB/OUTB/VDD/OUTA/SD pins 1~8 |
| Q1 | FDD8447L | 由 EG27324 驱动的低边功率 MOSFET，漏极连接 LED-，源极接地 | 图 9471fef4dad6 / 第 1 页 / 下部中央 Q1 FDD8447L：栅极 R7/R9、漏极 LED-、源极 GND |
| U1 | ME3116AM6G | +VIN 到 +5VIN 的降压转换器 | 图 9471fef4dad6 / 第 1 页 / 左上 U1 ME3116AM6G：VIN/EN/GND/FB/LX/BST 与 L1/D1/R1~R4/C1~C5 |
| J1 | HDR_4P_3.96 | PWM 负载与 DC 输入接线端子 | 图 9471fef4dad6 / 第 1 页 / 中下 J1 HDR_4P_3.96，端子依次为 LED-/LED+/12V+/12V- |
| P1 | Header 5 | Atom 5 Pin，G22 连接 PWM，其他 GPIO 未连接 | 图 9471fef4dad6 / 第 1 页 / 右下 P1 Header 5：3V3/G22/G19/G23/G33，G22 接 PWM，G19/G23/G33 标 no-connect |
| P2 | Header 4 | Atom 4 Pin，5V 接 +5VIN，G21/G25 未连接 | 图 9471fef4dad6 / 第 1 页 / 右下 P2 Header 4：G21/G25/5V/GND，5V 接 +5VIN，G21/G25 标 no-connect |
| D2 | SD24 | +VIN 输入到 GND 的保护二极管 | 图 9471fef4dad6 / 第 1 页 / 左上 +VIN-D2 SD24-GND，邻近 C2 100uF/35V 与 C3 100nF |
| D1 | B5819W SL | ME3116AM6G 开关节点到 GND 的肖特基二极管 | 图 9471fef4dad6 / 第 1 页 / 左上 U1 LX/C1/L1 共同开关节点-D1 B5819W SL-GND |
| D3 | 红灯 0603 | +5VIN 电源指示灯 | 图 9471fef4dad6 / 第 1 页 / 上部 +5VIN-R3 1KΩ-D3 红灯 0603-GND |
| R5/R6 | 0Ω | +MOSV 从 +5VIN 或 +3.3V 取电的选择电阻，实际装配待确认 | 图 9471fef4dad6 / 第 1 页 / 右上 R5 0Ω 从 +5VIN 到 +MOSV，R6 0Ω 从 +3.3V 到 +MOSV |

## 系统结构

### Atom PWM

Atom G22/PWM 驱动 U2 EG27324 INA，U2 OUTA 经 R7 控制 Q1 FDD8447L 低边开关；外部 +VIN 同时供给负载正端与 U1 ME3116AM6G，U1 生成 +5VIN 供 Atom 与指示电路使用。

- 参数与网络：`controller_signal=P1 G22 PWM`；`gate_driver=U2 EG27324`；`power_switch=Q1 FDD8447L`；`dc_dc=U1 ME3116AM6G`；`input=+VIN`；`logic_output=+5VIN`
- 证据：图 9471fef4dad6 / 第 1 页 / 整页 U1 DC-DC、U2/Q1 PWM 驱动、J1 负载端子与 P1/P2 Atom 接口

## 电源

### +VIN 输入

+VIN/DC12~24V 连接 U1 VIN pin 5，并由 D2 SD24、C2 100uF/35V 与 C3 100nF 接地；U1 EN pin 4 通过 R1 100KΩ 接 +VIN。

- 参数与网络：`rail=+VIN`；`label=DC12~24V`；`converter_input=U1 pin 5 VIN`；`protection=D2 SD24 to GND`；`bulk_cap=C2 100uF/35V`；`decoupling=C3 100nF`；`enable_pullup=R1 100KΩ`
- 证据：图 9471fef4dad6 / 第 1 页 / 左上 +VIN/DC12~24V-D2/C2/C3-U1 VIN/EN-R1

### U1 ME3116AM6G 降压输出

U1 LX pin 6 经 L1 10uH 输出 +5VIN，D1 B5819W SL 接在 LX 开关节点与 GND 之间，BST pin 1 通过 C1 100nF 接开关节点。

- 参数与网络：`converter=U1 ME3116AM6G`；`switch_pin=pin 6 LX`；`inductor=L1 10uH`；`catch_diode=D1 B5819W SL`；`bootstrap=C1 100nF`；`output=+5VIN`
- 证据：图 9471fef4dad6 / 第 1 页 / 左上 U1 LX/BST-C1-D1-L1-+5VIN

### ME3116AM6G 反馈与输出滤波

U1 FB pin 3 接 R2 56KΩ 与 R4 10KΩ 分压点，C4 100pF 跨接 R2；C5 22uF 从 +5VIN 接地，R3 1KΩ 与 D3 红灯 0603 构成 +5VIN 指示支路。

- 参数与网络：`feedback_top=R2 56KΩ`；`feedback_bottom=R4 10KΩ`；`feedforward_cap=C4 100pF`；`output_cap=C5 22uF`；`indicator=R3 1KΩ,D3 red LED 0603`
- 证据：图 9471fef4dad6 / 第 1 页 / 上部 U1 FB-R2/R4/C4-C5 与 +5VIN-R3-D3-GND

### EG27324 +MOSV 电源

U2 VDD pin 6 接 +MOSV，C6 100nF 与 C7 10uF 从 +MOSV 接 GND；U2 SD pin 8 与 GND pin 3 接地，NC pin 1 标为未连接。

- 参数与网络：`supply=U2 pin 6 VDD +MOSV`；`decoupling=C6 100nF,C7 10uF`；`shutdown=U2 pin 8 SD GND`；`ground=U2 pin 3 GND`；`unused=U2 pin 1 NC`
- 证据：图 9471fef4dad6 / 第 1 页 / 左下 U2 pins 1/3/6/8 与 +MOSV-C6/C7-GND

## 接口

### P1/P2 Atom 接口

P1 Header 5 的 3V3 接 +3.3V、G22 接 PWM，G19/G23/G33 标为未连接；P2 Header 4 的 5V 接 +5VIN、GND 接地，G21/G25 标为未连接。

- 参数与网络：`p1_pin_1=+3.3V`；`p1_pin_2=G22 PWM`；`p1_unused=G19,G23,G33`；`p2_unused=G21,G25`；`p2_power=5V +5VIN`；`p2_ground=GND`
- 证据：图 9471fef4dad6 / 第 1 页 / 右下 P1 Header 5 与 P2 Header 4 的所有网络及 no-connect 标记

### Q1 低边负载输出

Q1 FDD8447L 源极接 GND，漏极连接 J1 LED-；J1 LED+ 与 12V+ 连接 +VIN，J1 12V- 连接 GND。

- 参数与网络：`switch=Q1 FDD8447L`；`source=GND`；`drain=J1 LED-`；`load_positive=J1 LED+ +VIN`；`supply_positive=J1 12V+ +VIN`；`supply_negative=J1 12V- GND`
- 证据：图 9471fef4dad6 / 第 1 页 / 中下 Q1 drain/source 与 J1 LED-/LED+/12V+/12V-、+VIN/GND

## GPIO 与控制信号

### Atom G22 PWM 到 EG27324

Atom G22 直接连接 PWM 网络与 U2 INA pin 2，R8 10KΩ 将 PWM 下拉到 GND；U2 INB pin 4 标为未连接。

- 参数与网络：`atom_pin=P1 G22`；`network=PWM`；`driver_input=U2 pin 2 INA`；`pulldown=R8 10KΩ`；`unused_input=U2 pin 4 INB no-connect`
- 证据：图 9471fef4dad6 / 第 1 页 / 左下 PWM-R8-U2 INA pin 2、INB pin 4 no-connect 与右下 P1 G22

### EG27324 OUTA 到 FDD8447L

U2 OUTA pin 7 经 R7 100Ω 连接 Q1 栅极，R9 10KΩ 将栅极下拉到 GND；U2 OUTB pin 5 标为未连接。

- 参数与网络：`driver_output=U2 pin 7 OUTA`；`gate_resistor=R7 100Ω`；`mosfet=Q1 FDD8447L`；`gate_pulldown=R9 10KΩ`；`unused_output=U2 pin 5 OUTB no-connect`
- 证据：图 9471fef4dad6 / 第 1 页 / 下部 U2 OUTA pin 7-R7-Q1 gate-R9-GND 与 OUTB pin 5 no-connect

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom PWM | `controller_signal=P1 G22 PWM`；`gate_driver=U2 EG27324`；`power_switch=Q1 FDD8447L`；`dc_dc=U1 ME3116AM6G`；`input=+VIN`；`logic_output=+5VIN` |
| 电源 | +VIN 输入 | `rail=+VIN`；`label=DC12~24V`；`converter_input=U1 pin 5 VIN`；`protection=D2 SD24 to GND`；`bulk_cap=C2 100uF/35V`；`decoupling=C3 100nF`；`enable_pullup=R1 100KΩ` |
| 电源 | U1 ME3116AM6G 降压输出 | `converter=U1 ME3116AM6G`；`switch_pin=pin 6 LX`；`inductor=L1 10uH`；`catch_diode=D1 B5819W SL`；`bootstrap=C1 100nF`；`output=+5VIN` |
| 电源 | ME3116AM6G 反馈与输出滤波 | `feedback_top=R2 56KΩ`；`feedback_bottom=R4 10KΩ`；`feedforward_cap=C4 100pF`；`output_cap=C5 22uF`；`indicator=R3 1KΩ,D3 red LED 0603` |
| 电源 | +MOSV 栅极驱动电源选择 | `five_volt_option=R5 0Ω +5VIN to +MOSV`；`three_volt_option=R6 0Ω +3.3V to +MOSV`；`selected_source=null`；`explicit_population_mark=false` |
| 接口 | P1/P2 Atom 接口 | `p1_pin_1=+3.3V`；`p1_pin_2=G22 PWM`；`p1_unused=G19,G23,G33`；`p2_unused=G21,G25`；`p2_power=5V +5VIN`；`p2_ground=GND` |
| GPIO 与控制信号 | Atom G22 PWM 到 EG27324 | `atom_pin=P1 G22`；`network=PWM`；`driver_input=U2 pin 2 INA`；`pulldown=R8 10KΩ`；`unused_input=U2 pin 4 INB no-connect` |
| 电源 | EG27324 +MOSV 电源 | `supply=U2 pin 6 VDD +MOSV`；`decoupling=C6 100nF,C7 10uF`；`shutdown=U2 pin 8 SD GND`；`ground=U2 pin 3 GND`；`unused=U2 pin 1 NC` |
| GPIO 与控制信号 | EG27324 OUTA 到 FDD8447L | `driver_output=U2 pin 7 OUTA`；`gate_resistor=R7 100Ω`；`mosfet=Q1 FDD8447L`；`gate_pulldown=R9 10KΩ`；`unused_output=U2 pin 5 OUTB no-connect` |
| 接口 | Q1 低边负载输出 | `switch=Q1 FDD8447L`；`source=GND`；`drain=J1 LED-`；`load_positive=J1 LED+ +VIN`；`supply_positive=J1 12V+ +VIN`；`supply_negative=J1 12V- GND` |

## 待确认事项

- `power.mosv-source-selection`：R5 0Ω 将 +5VIN 连接到 +MOSV，R6 0Ω 将 +3.3V 连接到 +MOSV；页面没有 DNP、NC 或装配标记，无法确认实际版本选择哪一路供电。（证据：图 9471fef4dad6 / 第 1 页 / 右上 R5/R6 两只 0Ω 分别从 +5VIN/+3.3V 汇入 +MOSV，无装配状态标注）
- `review.mosv-source-selection`：请用 K065 的 BOM、PCB 或装配图确认 R5 与 R6 的实际装配状态，以及 +MOSV 采用 +5VIN 还是 +3.3V。；原因：两只 0Ω 电阻同时画在不同电源到 +MOSV 的路径上，但页面没有 DNP/NC 标记；不能据此认定两路同时连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9471fef4dad6c055ec8edaa92026eea7993fdb6e439005a10dc113fb887560ea` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_pwm.md`

源文档 SHA-256：`82cd1477dad67bc8fd9d8862938985638a669adcbe77494a334a791d1c354799`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
