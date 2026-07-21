# Atomic PWM Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic PWM Base |
| SKU | A114 |
| 产品 ID | `atomic-pwm-base-0d888c312525` |
| 源文档 | `zh_CN/atom/Atomic PWM Base.md` |

## 概述

Atomic PWM Base 以 +VIN/DC12~24V 为输入，U1 ME3116AM6G 经 L1 与肖特基二极管降压生成 +5VIN，并以 D3 红色 LED 指示电源。ATOM Header 5 的 G22 输出 PWM，PWM 经下拉后进入 U2 EG27324 INA，OUTA 通过 R7 驱动 Q1 FDD8447L 栅极；Q1 作为低侧开关控制 J1 LED-，J1 LED+ 与 12V+ 共接 +VIN，12V- 接 GND。U2 的 +MOSV 供电节点通过 R5/R6 两只 0Ω 分别连接 +5VIN 和 +3.3V，当前页面没有标注两只电阻的实际装配选项。

## 检索关键词

`Atomic PWM Base`、`A114`、`ME3116AM6G`、`EG27324`、`FDD8447L`、`PWM`、`G22`、`+VIN`、`DC12~24V`、`+5VIN`、`+MOSV`、`+3.3V`、`LED-`、`LED+`、`12V+`、`12V-`、`B5819W SL`、`SD24`、`L1 10uH`、`OUTA`、`INA`、`R5 0Ω`、`R6 0Ω`、`HDR_4P_3.96`、`P1 Header 5`、`P2 Header 4`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME3116AM6G | 将 +VIN/DC12~24V 降压为 +5VIN 的开关稳压器 | 图 9471fef4dad6 / 第 1 页 / 页面左上 U1 ME3116AM6G，VIN/EN/GND/BST/LX/FB 六脚及外围 |
| D2 | SD24 | +VIN 输入节点到 GND 的防护二极管 | 图 9471fef4dad6 / 第 1 页 / 页面左上 +VIN 输入节点下方 D2 SD24 对地 |
| D1/L1 | B5819W SL / 10uH | ME3116AM6G 降压转换的肖特基续流二极管与输出电感 | 图 9471fef4dad6 / 第 1 页 / U1 右侧 LX 开关节点、D1 B5819W SL 与 L1 10uH |
| D3 | 红灯 0603 | 由 +5VIN 经 R3 驱动的电源指示灯 | 图 9471fef4dad6 / 第 1 页 / 页面上中 +5VIN-R3 1KΩ-D3 红灯 0603-GND |
| U2 | EG27324 | 接收 PWM 并由 OUTA 驱动功率 MOSFET 的双通道栅极驱动器，本设计只使用 A 通道 | 图 9471fef4dad6 / 第 1 页 / 页面左下 U2 EG27324，INA/OUTA/VDD/GND 与未连接的 NC/INB/OUTB |
| Q1 | FDD8447L | 由 U2 OUTA 驱动的低侧功率 MOSFET，开关 J1 LED- | 图 9471fef4dad6 / 第 1 页 / 页面中下 Q1 FDD8447L，栅极接 R7/R9，源极 GND，漏极接 J1 LED- |
| J1 | HDR_4P_3.96 | 引出 LED-、LED+、12V+ 和 12V- 的负载/电源端子 | 图 9471fef4dad6 / 第 1 页 / 页面中右 J1 HDR_4P_3.96，四行标注 LED-/LED+/12V+/12V- |
| P1 | Header 5 | Atom 五针接口，引出 +3.3V 与 G22 PWM，其余三脚未连接 | 图 9471fef4dad6 / 第 1 页 / 页面右下 P1 Header 5，3V3/G22/G19/G23/G33 |
| P2 | Header 4 | Atom 四针接口，引出 +5VIN 与 GND，G21/G25 未连接 | 图 9471fef4dad6 / 第 1 页 / 页面右下 P2 Header 4，G21/G25/5V/GND |
| R5/R6 | 0Ω | 分别把 +5VIN 与 +3.3V 连接到 +MOSV 的供电选择位置 | 图 9471fef4dad6 / 第 1 页 / 页面右上 R5 0Ω 从 +5VIN 到 +MOSV，R6 0Ω 从 +3.3V 到 +MOSV |

## 系统结构

### PWM 功率路径

+VIN/DC12~24V 同时供给 ME3116AM6G 降压电路和 J1 LED+/12V+；Atom G22 的 PWM 经 EG27324 A 通道驱动 FDD8447L，MOSFET 在低侧开关 J1 LED-。

- 参数与网络：`input=+VIN / DC12~24V`；`controller_signal=P1 G22 -> PWM`；`driver=U2 EG27324 channel A`；`switch=Q1 FDD8447L`；`switched_output=J1 LED-`；`positive_output=J1 LED+/12V+ -> +VIN`
- 证据：图 9471fef4dad6 / 第 1 页 / 整页 +VIN/U1、P1 PWM、U2/Q1 与 J1 负载链路

## 核心器件

### Grove 接口可见性

当前页面没有显示独立 Grove 连接器，P2 的 G21/G25 两脚也标为未连接。

- 参数与网络：`grove_connector_shown=false`；`g21_connected=false`；`g25_connected=false`
- 证据：图 9471fef4dad6 / 第 1 页 / 整页无 Grove 方框；右下 P2 G21/G25 为 no-connect

### 负载额定与保护可见性

原理图给出 FDD8447L 和 DC12~24V 输入，但没有在页面标注允许的连续电流、功率、散热条件、保险丝、过流检测或负载续流器件。

- 参数与网络：`mosfet=FDD8447L`；`input_range=DC12~24V`；`current_rating_shown=false`；`thermal_limit_shown=false`；`fuse_shown=false`；`current_sense_shown=false`；`load_flyback_shown=false`
- 证据：图 9471fef4dad6 / 第 1 页 / 整页 Q1/J1 功率路径，未见电流检测、保险丝或负载续流器件

## 电源

### +VIN 输入防护与滤波

+VIN 网络标注 DC12~24V，D2 SD24 从 +VIN 接 GND，C2 100uF 35V 与 C3 100nF 从 +VIN 接 GND。

- 参数与网络：`input_label=DC12~24V`；`protection=D2 SD24 to GND`；`bulk_capacitor=C2 100uF 35V`；`high_frequency_capacitor=C3 100nF`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面左上 +VIN/DC12~24V 与 D2/C2/C3

### ME3116AM6G 输入与使能

U1 VIN 5 脚连接 +VIN，EN 4 脚经 R1 100KΩ 连接 +VIN，GND 2 脚接地。

- 参数与网络：`vin=pin 5 -> +VIN`；`enable=pin 4 -> R1 100KΩ -> +VIN`；`ground=pin 2 -> GND`
- 证据：图 9471fef4dad6 / 第 1 页 / U1 左侧 VIN/EN/GND 与 R1

### ME3116AM6G +5VIN 输出

U1 LX 6 脚经 L1 10uH 形成 +5VIN，D1 B5819W SL 从开关节点接 GND，C1 100nF 跨接 BST 1 脚与开关节点，C5 22uF 从 +5VIN 接 GND。

- 参数与网络：`switch=LX pin 6`；`inductor=L1 10uH`；`output=+5VIN`；`catch_diode=D1 B5819W SL`；`bootstrap=C1 100nF`；`output_capacitor=C5 22uF`
- 证据：图 9471fef4dad6 / 第 1 页 / U1 右侧 BST/LX、C1/D1/L1/+5VIN/C5

### ME3116AM6G 反馈网络

U1 FB 3 脚连接 R2 56KΩ 与 R4 10KΩ 的 +5VIN 对地分压节点，C4 100pF 与 R2 并联。

- 参数与网络：`upper_resistor=R2 56KΩ to +5VIN`；`lower_resistor=R4 10KΩ to GND`；`feedforward_capacitor=C4 100pF parallel to R2`；`feedback_pin=3`
- 证据：图 9471fef4dad6 / 第 1 页 / U1 FB 3 脚与 R2/R4/C4

### EG27324 驱动电源

U2 VDD 6 脚连接 +MOSV，GND 3 脚与 SD 8 脚接 GND，C6 100nF 与 C7 10uF 从 +MOSV 接 GND。

- 参数与网络：`vdd=pin 6 -> +MOSV`；`ground=pin 3 -> GND`；`shutdown_pin=pin 8 SD -> GND`；`decoupling=C6 100nF; C7 10uF`
- 证据：图 9471fef4dad6 / 第 1 页 / U2 VDD/GND/SD 与 +MOSV、C6/C7

### +MOSV 供电选择

R5 0Ω 从 +5VIN 连接 +MOSV，R6 0Ω 从 +3.3V 连接 +MOSV；当前页面没有用 DNP 或装配选项标识区分两只电阻。

- 参数与网络：`r5=+5VIN -> 0Ω -> +MOSV`；`r6=+3.3V -> 0Ω -> +MOSV`；`assembly_option_marked=false`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面右上 R5/R6 两只 0Ω 汇到 +MOSV

## 接口

### P2 四针电源接口

P2 Header 4 的 G21/G25 两脚在当前页面标为未连接，5V 脚接 +5VIN，GND 脚接地。

- 参数与网络：`g21=not connected`；`g25=not connected`；`5v=+5VIN`；`ground=GND`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面右下 P2 Header 4 与 no-connect/+5VIN/GND

### J1 四针输出端子

J1 HDR_4P_3.96 四行从上到下标注 LED-、LED+、12V+、12V-。

- 参数与网络：`line1=LED-`；`line2=LED+`；`line3=12V+`；`line4=12V-`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面中右 J1 HDR_4P_3.96 四行标签

## GPIO 与控制信号

### +5VIN 电源指示

+5VIN 经 R3 1KΩ 和 D3 红灯 0603 接 GND。

- 参数与网络：`source=+5VIN`；`resistor=R3 1KΩ`；`indicator=D3 red LED 0603`；`return=GND`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面上中 +5VIN-R3-D3-GND

### Atom PWM 映射

P1 Header 5 的 1 脚 3V3 接 +3.3V，2 脚 G22 接 PWM，3/4/5 脚 G19/G23/G33 在当前页面标为未连接。

- 参数与网络：`pin1=3V3 -> +3.3V`；`pin2=G22 -> PWM`；`pin3=G19 not connected`；`pin4=G23 not connected`；`pin5=G33 not connected`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面右下 P1 Header 5 与 +3.3V/PWM/no-connect 标记

### EG27324 PWM 输入

PWM 网络连接 U2 INA 2 脚，并由 R8 10KΩ 下拉到 GND；INB 4 脚与 NC 1 脚标为未连接。

- 参数与网络：`input=PWM -> INA pin 2`；`pulldown=R8 10KΩ to GND`；`inb_connected=false`；`pin1_connected=false`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面左下 PWM-R8-U2 INA 与 pin1/INB no-connect

## 关键网络

### FDD8447L 栅极驱动

U2 OUTA 7 脚经 R7 10Ω 连接 Q1 FDD8447L 栅极，R9 10KΩ 将栅极下拉到 GND；OUTB 5 脚标为未连接。

- 参数与网络：`driver_output=U2 OUTA pin 7`；`series_resistor=R7 10Ω`；`mosfet=Q1 FDD8447L`；`gate_pulldown=R9 10KΩ`；`outb_connected=false`
- 证据：图 9471fef4dad6 / 第 1 页 / 页面中下 U2 OUTA-R7-Q1 gate-R9 与 OUTB no-connect

### 负载低侧开关

Q1 FDD8447L 源极接 GND，漏极连接 J1 LED-；J1 LED+ 与 12V+ 并接 +VIN，12V- 接 GND。

- 参数与网络：`source=Q1 source -> GND`；`drain=Q1 drain -> J1 LED-`；`positive_load=J1 LED+ and 12V+ -> +VIN`；`negative_supply=J1 12V- -> GND`
- 证据：图 9471fef4dad6 / 第 1 页 / Q1 源/漏极与 J1 LED-/LED+/12V+/12V-

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | PWM 功率路径 | `input=+VIN / DC12~24V`；`controller_signal=P1 G22 -> PWM`；`driver=U2 EG27324 channel A`；`switch=Q1 FDD8447L`；`switched_output=J1 LED-`；`positive_output=J1 LED+/12V+ -> +VIN` |
| 电源 | +VIN 输入防护与滤波 | `input_label=DC12~24V`；`protection=D2 SD24 to GND`；`bulk_capacitor=C2 100uF 35V`；`high_frequency_capacitor=C3 100nF` |
| 电源 | ME3116AM6G 输入与使能 | `vin=pin 5 -> +VIN`；`enable=pin 4 -> R1 100KΩ -> +VIN`；`ground=pin 2 -> GND` |
| 电源 | ME3116AM6G +5VIN 输出 | `switch=LX pin 6`；`inductor=L1 10uH`；`output=+5VIN`；`catch_diode=D1 B5819W SL`；`bootstrap=C1 100nF`；`output_capacitor=C5 22uF` |
| 电源 | ME3116AM6G 反馈网络 | `upper_resistor=R2 56KΩ to +5VIN`；`lower_resistor=R4 10KΩ to GND`；`feedforward_capacitor=C4 100pF parallel to R2`；`feedback_pin=3` |
| GPIO 与控制信号 | +5VIN 电源指示 | `source=+5VIN`；`resistor=R3 1KΩ`；`indicator=D3 red LED 0603`；`return=GND` |
| GPIO 与控制信号 | Atom PWM 映射 | `pin1=3V3 -> +3.3V`；`pin2=G22 -> PWM`；`pin3=G19 not connected`；`pin4=G23 not connected`；`pin5=G33 not connected` |
| 接口 | P2 四针电源接口 | `g21=not connected`；`g25=not connected`；`5v=+5VIN`；`ground=GND` |
| GPIO 与控制信号 | EG27324 PWM 输入 | `input=PWM -> INA pin 2`；`pulldown=R8 10KΩ to GND`；`inb_connected=false`；`pin1_connected=false` |
| 电源 | EG27324 驱动电源 | `vdd=pin 6 -> +MOSV`；`ground=pin 3 -> GND`；`shutdown_pin=pin 8 SD -> GND`；`decoupling=C6 100nF; C7 10uF` |
| 关键网络 | FDD8447L 栅极驱动 | `driver_output=U2 OUTA pin 7`；`series_resistor=R7 10Ω`；`mosfet=Q1 FDD8447L`；`gate_pulldown=R9 10KΩ`；`outb_connected=false` |
| 关键网络 | 负载低侧开关 | `source=Q1 source -> GND`；`drain=Q1 drain -> J1 LED-`；`positive_load=J1 LED+ and 12V+ -> +VIN`；`negative_supply=J1 12V- -> GND` |
| 接口 | J1 四针输出端子 | `line1=LED-`；`line2=LED+`；`line3=12V+`；`line4=12V-` |
| 电源 | +MOSV 供电选择 | `r5=+5VIN -> 0Ω -> +MOSV`；`r6=+3.3V -> 0Ω -> +MOSV`；`assembly_option_marked=false` |
| 核心器件 | Grove 接口可见性 | `grove_connector_shown=false`；`g21_connected=false`；`g25_connected=false` |
| 核心器件 | 负载额定与保护可见性 | `mosfet=FDD8447L`；`input_range=DC12~24V`；`current_rating_shown=false`；`thermal_limit_shown=false`；`fuse_shown=false`；`current_sense_shown=false`；`load_flyback_shown=false` |

## 待确认事项

- `review.mosv_resistor_population`：R5 与 R6 的实际装配状态是什么，+MOSV 应由 +5VIN 还是 +3.3V 供电？；原因：原理图把两只电阻都标为 0Ω 且未标 DNP，同时装配会把 +5VIN 与 +3.3V 直接连接。
- `review.grove_and_load_limits`：当前 A114 硬件的 Grove 接口位于何处，并请确认 J1 负载的连续电流、功率、散热和感性负载保护限制。；原因：当前原理图没有 Grove 连接器，也没有给出功率回路的额定值与负载保护边界。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9471fef4dad6c055ec8edaa92026eea7993fdb6e439005a10dc113fb887560ea` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-2d6a7113-0f87-4c13-be7a-4a9eecf72550.webp` |

---

源文档：`zh_CN/atom/Atomic PWM Base.md`

源文档 SHA-256：`8af3db83d499d94ada45581b602b73071a28a21dc9cd4711b1733cb49a8e871c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
