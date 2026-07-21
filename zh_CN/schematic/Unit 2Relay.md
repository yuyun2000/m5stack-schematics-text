# Unit 2Relay 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 2Relay |
| SKU | U131 |
| 产品 ID | `unit-2relay-082cac04e142` |
| 源文档 | `zh_CN/unit/2relay.md` |

## 概述

Unit 2Relay 由两个对称的离散晶体管继电器驱动通道构成，没有板载主控、协处理器、存储器或通信 IC。J1 将 Relay A、Relay B、+5VIN 和 GND 引入，两路控制分别经 1KΩ 基极电阻驱动 Q1/Q2（SS8050 Y1），低侧控制 K1/K2（Relay-DPDT）线圈。每路具有 10KΩ 输入下拉、蓝色 0603 LED 指示支路和线圈并联二极管，负载触点通过 P1/P2 的 C/A/B/C 四端引出。

## 检索关键词

`Unit 2Relay`、`U131`、`2Relay`、`J1`、`HY-2.0_IO`、`Relay A`、`Relay B`、`+5VIN`、`GND`、`K1`、`K2`、`Relay-DPDT`、`Q1`、`Q2`、`SS8050 Y1`、`D1`、`D2`、`D3`、`D4`、`蓝灯 0603`、`R1`、`R2`、`R3`、`R4`、`R5`、`R6`、`1KΩ`、`10KΩ`、`P1`、`P2`、`HDR_4P_relay`、`C/A/B/C`、`low-side drive`、`flyback diode`、`GPIO relay control`、`relay indicator LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | HY-2.0_IO | 四针控制与供电接口，引入 Relay A、Relay B、+5VIN 和 GND。 | 图 d2fa75fa6126 / 第 1 页 / 页面左侧 J1（HY-2.0_IO），1-4 脚及 Relay A/Relay B/+5VIN/GND 标注 |
| K1 | Relay-DPDT | A 通道继电器，线圈由 +5VIN 与 Q1 低侧节点驱动，触点连接 P1。 | 图 d2fa75fa6126 / 第 1 页 / 页面右上 K1（Relay-DPDT）、线圈与 P1 连接 |
| K2 | Relay-DPDT | B 通道继电器，线圈由 +5VIN 与 Q2 低侧节点驱动，触点连接 P2。 | 图 d2fa75fa6126 / 第 1 页 / 页面右下 K2（Relay-DPDT）、线圈与 P2 连接 |
| P1 | HDR_4P_relay | K1 负载触点四端连接器，图中从上到下标注 C、A、B、C。 | 图 d2fa75fa6126 / 第 1 页 / 页面右上 P1（HDR_4P_relay），端子文字 C/A/B/C |
| P2 | HDR_4P_relay | K2 负载触点四端连接器，图中从上到下标注 C、A、B、C。 | 图 d2fa75fa6126 / 第 1 页 / 页面右下 P2（HDR_4P_relay），端子文字 C/A/B/C |
| Q1 | SS8050 Y1 | A 通道低侧继电器线圈驱动晶体管，发射极接 GND。 | 图 d2fa75fa6126 / 第 1 页 / 页面上半部 Q1（SS8050 Y1），基极 R2、集电极 K1、发射极 GND |
| Q2 | SS8050 Y1 | B 通道低侧继电器线圈驱动晶体管，发射极接 GND。 | 图 d2fa75fa6126 / 第 1 页 / 页面下半部 Q2（SS8050 Y1），基极 R5、集电极 K2、发射极 GND |
| D1,D3 | 蓝灯 0603 | A、B 两路继电器动作指示 LED，分别通过 R1、R4 连接到低侧驱动节点。 | 图 d2fa75fa6126 / 第 1 页 / 页面上半部 D1 蓝灯 0603/R1 与下半部 D3 蓝灯 0603/R4 |
| D2,D4 | 未标注 | 分别反向并联在 K1、K2 线圈两端的续流保护二极管。 | 图 d2fa75fa6126 / 第 1 页 / 页面上半部 D2 跨接 +5VIN/K1 低侧节点；下半部 D4 跨接 +5VIN/K2 低侧节点 |
| R1,R2,R4,R5 | 1KΩ | R1/R4 为 LED 串联限流电阻，R2/R5 为 Q1/Q2 基极串联电阻。 | 图 d2fa75fa6126 / 第 1 页 / D1-R1、Relay A-R2-Q1、D3-R4、Relay B-R5-Q2 支路，均标注 1KΩ |
| R3,R6 | 10KΩ | Relay A 与 Relay B 输入到 GND 的下拉电阻。 | 图 d2fa75fa6126 / 第 1 页 / 页面中部 Relay A-R3-GND 与下部 Relay B-R6-GND，均标注 10KΩ |

## 系统结构

### 双路继电器架构

整板由 A、B 两个相互镜像的离散继电器驱动通道组成：J1 提供控制与供电，Q1/Q2 低侧驱动 K1/K2，P1/P2 引出负载触点；原理图未显示板载主控、存储器、时钟或数字通信 IC。

- 参数与网络：`channels=2`；`channel_a=Relay A,Q1,K1,P1`；`channel_b=Relay B,Q2,K2,P2`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示`
- 证据：图 d2fa75fa6126 / 第 1 页 / 第 1 页全图，J1、上方 K1/Q1/P1 与下方 K2/Q2/P2 镜像电路

## 核心器件

### Q1/K1 驱动

Q1（SS8050 Y1）发射极接 GND、集电极接 K1 线圈低端，K1 线圈高端接 +5VIN，形成 A 通道低侧线圈驱动。

- 参数与网络：`transistor=Q1 SS8050 Y1`；`relay=K1 Relay-DPDT`；`base_path=Relay A -> R2 1KΩ -> Q1`；`collector=K1 coil low side`；`emitter=GND`；`coil_high_side=+5VIN`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面上半部 R2-Q1-K1 线圈与 +5VIN/GND 连接

### Q2/K2 驱动

Q2（SS8050 Y1）发射极接 GND、集电极接 K2 线圈低端，K2 线圈高端接 +5VIN，形成 B 通道低侧线圈驱动。

- 参数与网络：`transistor=Q2 SS8050 Y1`；`relay=K2 Relay-DPDT`；`base_path=Relay B -> R5 1KΩ -> Q2`；`collector=K2 coil low side`；`emitter=GND`；`coil_high_side=+5VIN`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面下半部 R5-Q2-K2 线圈与 +5VIN/GND 连接

### A 通道指示灯

D1（蓝灯 0603）与 R1（1KΩ）串联在 +5VIN 和 Q1/K1 低侧节点之间，作为与 K1 线圈低侧节点同步的指示支路。

- 参数与网络：`led=D1 蓝灯 0603`；`resistor=R1 1KΩ`；`high_side=+5VIN`；`low_side=Q1 collector/K1 coil low side`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面上半部 +5VIN-D1-R1-Q1 集电极支路

### B 通道指示灯

D3（蓝灯 0603）与 R4（1KΩ）串联在 +5VIN 和 Q2/K2 低侧节点之间，作为与 K2 线圈低侧节点同步的指示支路。

- 参数与网络：`led=D3 蓝灯 0603`；`resistor=R4 1KΩ`；`high_side=+5VIN`；`low_side=Q2 collector/K2 coil low side`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面下半部 +5VIN-D3-R4-Q2 集电极支路

## 电源

### +5VIN 电源路径

+5VIN 从 J1.3 直接供给 K1/K2 线圈高端、D1/D3 指示支路高端以及 D2/D4 续流二极管高端；原理图未显示稳压器、LDO、负载开关、去耦电容或输入保护器件。

- 参数与网络：`rail=+5VIN`；`input=J1.3`；`relay_coils=K1,K2`；`indicator_leds=D1,D3`；`flyback_diodes=D2,D4`；`conversion=原理图未显示`；`decoupling=原理图未显示`
- 证据：图 d2fa75fa6126 / 第 1 页 / J1.3 的 +5VIN 网络以及 K1/K2 线圈、D1/D2/D3/D4 顶部 +5VIN 母线

### GND 回路

J1.4 为 GND；Q1/Q2 发射极与 R3/R6 下端均连接 GND，构成两路驱动和输入下拉的回路。

- 参数与网络：`input_ground=J1.4`；`transistor_emitters=Q1,Q2`；`pulldown_resistors=R3,R6`；`net=GND`
- 证据：图 d2fa75fa6126 / 第 1 页 / J1.4、Q1/Q2 发射极、R3/R6 下端的 GND 符号

## 接口

### J1 HY-2.0_IO

J1 的 1-4 脚分别为 A、B、VCC、GND，并连接 Relay A、Relay B、+5VIN、GND 网络。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IO`；`pin_1_function=A`；`pin_1_net=Relay A`；`pin_2_function=B`；`pin_2_net=Relay B`；`pin_3_function=VCC`；`pin_3_net=+5VIN`；`pin_4_function=GND`；`pin_4_net=GND`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面左侧 J1，针脚 1-4 与 A/B/VCC/GND、Relay A/Relay B/+5VIN/GND 标注

### P1 负载端子

P1（HDR_4P_relay）连接 K1 触点，四个端子在符号内从上到下标注 C、A、B、C。

- 参数与网络：`reference=P1`；`part_number=HDR_4P_relay`；`relay=K1`；`top_to_bottom=C,A,B,C`；`terminal_count=4`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面右上 K1 触点至 P1，P1 内部从上到下 C/A/B/C 标注

### P2 负载端子

P2（HDR_4P_relay）连接 K2 触点，四个端子在符号内从上到下标注 C、A、B、C。

- 参数与网络：`reference=P2`；`part_number=HDR_4P_relay`；`relay=K2`；`top_to_bottom=C,A,B,C`；`terminal_count=4`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面右下 K2 触点至 P2，P2 内部从上到下 C/A/B/C 标注

## GPIO 与控制信号

### Relay A 控制输入

Relay A 从 J1.1 引入，经 R2（1KΩ）连接 Q1 基极，并由 R3（10KΩ）下拉到 GND。

- 参数与网络：`connector_pin=J1.1`；`net=Relay A`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`driver=Q1 SS8050 Y1`；`direction=J1 到 Q1`
- 证据：图 d2fa75fa6126 / 第 1 页 / J1.1 Relay A；页面中上 Relay A-R2-Q1 与 Relay A-R3-GND

### Relay B 控制输入

Relay B 从 J1.2 引入，经 R5（1KΩ）连接 Q2 基极，并由 R6（10KΩ）下拉到 GND。

- 参数与网络：`connector_pin=J1.2`；`net=Relay B`；`base_resistor=R5 1KΩ`；`pulldown=R6 10KΩ`；`driver=Q2 SS8050 Y1`；`direction=J1 到 Q2`
- 证据：图 d2fa75fa6126 / 第 1 页 / J1.2 Relay B；页面下半部 Relay B-R5-Q2 与 Relay B-R6-GND

## 保护电路

### K1/K2 线圈续流保护

D2、D4 分别反向并联在 K1、K2 线圈的 +5VIN 高端与晶体管低侧节点之间，用于继电器线圈断电时的续流钳位；原理图未标注二极管具体型号。

- 参数与网络：`channel_a_diode=D2`；`channel_a_coil=K1`；`channel_b_diode=D4`；`channel_b_coil=K2`；`high_side=+5VIN`；`part_number=未标注`
- 证据：图 d2fa75fa6126 / 第 1 页 / D2 跨接 K1 线圈两端，D4 跨接 K2 线圈两端，二极管阴极侧接 +5VIN

## 关键网络

### K1 线圈低侧节点

K1 线圈低侧、Q1 集电极、D2 阳极以及 R1 指示支路低端连接在同一节点。

- 参数与网络：`connections=K1 coil low,Q1 collector,D2 anode,R1 low`；`channel=A`；`high_side=+5VIN`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面上半部 K1 线圈下端、Q1 集电极、D2 下端、R1 右端的连接点

### K2 线圈低侧节点

K2 线圈低侧、Q2 集电极、D4 阳极以及 R4 指示支路低端连接在同一节点。

- 参数与网络：`connections=K2 coil low,Q2 collector,D4 anode,R4 low`；`channel=B`；`high_side=+5VIN`
- 证据：图 d2fa75fa6126 / 第 1 页 / 页面下半部 K2 线圈下端、Q2 集电极、D4 下端、R4 右端的连接点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 双路继电器架构 | `channels=2`；`channel_a=Relay A,Q1,K1,P1`；`channel_b=Relay B,Q2,K2,P2`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示` |
| 接口 | J1 HY-2.0_IO | `reference=J1`；`part_number=HY-2.0_IO`；`pin_1_function=A`；`pin_1_net=Relay A`；`pin_2_function=B`；`pin_2_net=Relay B`；`pin_3_function=VCC`；`pin_3_net=+5VIN`；`pin_4_function=GND`；`pin_4_net=GND` |
| 电源 | +5VIN 电源路径 | `rail=+5VIN`；`input=J1.3`；`relay_coils=K1,K2`；`indicator_leds=D1,D3`；`flyback_diodes=D2,D4`；`conversion=原理图未显示`；`decoupling=原理图未显示` |
| 电源 | GND 回路 | `input_ground=J1.4`；`transistor_emitters=Q1,Q2`；`pulldown_resistors=R3,R6`；`net=GND` |
| GPIO 与控制信号 | Relay A 控制输入 | `connector_pin=J1.1`；`net=Relay A`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`driver=Q1 SS8050 Y1`；`direction=J1 到 Q1` |
| GPIO 与控制信号 | Relay B 控制输入 | `connector_pin=J1.2`；`net=Relay B`；`base_resistor=R5 1KΩ`；`pulldown=R6 10KΩ`；`driver=Q2 SS8050 Y1`；`direction=J1 到 Q2` |
| 核心器件 | Q1/K1 驱动 | `transistor=Q1 SS8050 Y1`；`relay=K1 Relay-DPDT`；`base_path=Relay A -> R2 1KΩ -> Q1`；`collector=K1 coil low side`；`emitter=GND`；`coil_high_side=+5VIN` |
| 核心器件 | Q2/K2 驱动 | `transistor=Q2 SS8050 Y1`；`relay=K2 Relay-DPDT`；`base_path=Relay B -> R5 1KΩ -> Q2`；`collector=K2 coil low side`；`emitter=GND`；`coil_high_side=+5VIN` |
| 核心器件 | A 通道指示灯 | `led=D1 蓝灯 0603`；`resistor=R1 1KΩ`；`high_side=+5VIN`；`low_side=Q1 collector/K1 coil low side` |
| 核心器件 | B 通道指示灯 | `led=D3 蓝灯 0603`；`resistor=R4 1KΩ`；`high_side=+5VIN`；`low_side=Q2 collector/K2 coil low side` |
| 保护电路 | K1/K2 线圈续流保护 | `channel_a_diode=D2`；`channel_a_coil=K1`；`channel_b_diode=D4`；`channel_b_coil=K2`；`high_side=+5VIN`；`part_number=未标注` |
| 接口 | P1 负载端子 | `reference=P1`；`part_number=HDR_4P_relay`；`relay=K1`；`top_to_bottom=C,A,B,C`；`terminal_count=4` |
| 接口 | P2 负载端子 | `reference=P2`；`part_number=HDR_4P_relay`；`relay=K2`；`top_to_bottom=C,A,B,C`；`terminal_count=4` |
| 关键网络 | K1 线圈低侧节点 | `connections=K1 coil low,Q1 collector,D2 anode,R1 low`；`channel=A`；`high_side=+5VIN` |
| 关键网络 | K2 线圈低侧节点 | `connections=K2 coil low,Q2 collector,D4 anode,R4 low`；`channel=B`；`high_side=+5VIN` |
| 接口 | P1/P2 触点定义与额定值 | `connectors=P1,P2`；`visible_labels=C,A,B,C`；`no_mapping=未标注`；`nc_mapping=未标注`；`com_mapping=未标注`；`contact_rating=未标注` |
| GPIO 与控制信号 | Relay A/Relay B 输入电气阈值 | `inputs=Relay A,Relay B`；`series_resistors=R2 1KΩ,R5 1KΩ`；`pulldowns=R3 10KΩ,R6 10KΩ`；`logic_threshold=未标注`；`input_voltage_range=未标注`；`required_drive_current=未标注` |

## 待确认事项

- `interface.contact-functions-ratings-undetermined`：原理图将 P1/P2 四个负载端标为 C/A/B/C，但未给出这些字母与 NO、NC、COM 的逐端对应，也未标注触点额定电压、电流或端子编号。（证据：图 d2fa75fa6126 / 第 1 页 / 页面右侧 K1/P1 与 K2/P2，继电器标注 Relay-DPDT，端子仅标 C/A/B/C）
- `gpio.input-threshold-undetermined`：原理图显示 Relay A/Relay B 通过 1KΩ 电阻驱动 SS8050 Y1 基极并由 10KΩ 下拉，但未给出逻辑高低阈值、允许输入电压范围或所需 GPIO 驱动电流。（证据：图 d2fa75fa6126 / 第 1 页 / Relay A-R2/R3-Q1 与 Relay B-R5/R6-Q2 输入网络，页面无阈值或电压范围文字）
- `review.contact-functions-ratings`：P1/P2 的 C/A/B/C 四端分别对应哪些 NO、NC、COM 触点，且触点额定电压和电流是多少？；原因：当前原理图没有端子编号、NO/NC/COM 文字或触点额定参数，不能仅凭符号和产品正文补全。
- `review.input-threshold`：Relay A/Relay B 的保证吸合/释放逻辑阈值、允许输入电压和 GPIO 驱动电流是多少？；原因：原理图只给出 SS8050 Y1、1KΩ 基极电阻和 10KΩ 下拉，未给出继电器线圈参数或逻辑电气规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d2fa75fa6126915d7c2b7a26248b08e4416ce2a801a1771add49b94bef524b73` | `https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_sch_01.webp` |

---

源文档：`zh_CN/unit/2relay.md`

源文档 SHA-256：`d39146dbdf01c11b4ef84b61525a303d344d9d2438faa6c6688be3de21b3cc1e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
