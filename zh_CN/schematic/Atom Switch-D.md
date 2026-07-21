# Atom Switch-D 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Switch-D |
| SKU | K042-D |
| 产品 ID | `atom-switch-d-7c3e8ae886fb` |
| 源文档 | `zh_CN/atom/atomhub_switch_d.md` |

## 概述

Atom Switch-D 原理图分为 RS485、12V 降压、Grove/端子、双继电器、AC-DC 和 Atom IO 六个功能区。BUS1 将 G22/G19 用于 Relay_1/Relay_2，G23/G33 用于 Uart_Tx/Uart_Rx，G21/G25 用于 I2C；SP3485EN-L/TR 通过 Q1 自动控制 /RE/DE，并在 A/B 端配置偏置、可选 120Ω 终端和 SMAJ6.5CA 防护。AC_L 经 F1 后同时送到两只 JQX-115F-005-2ZS4 的并联双刀公共端，NO 端分别形成 AC_L1/AC_L2；VCC_5V 既可由 MD1 AC-DC 5V1A 产生，也由外部 VCC_12V 经 MP1584 降压产生。

## 检索关键词

`Atom Switch-D`、`K042-D`、`SP3485EN-L/TR`、`MP1584`、`JQX-115F-005-2ZS4`、`SMAJ6.5CA`、`RS485_A`、`RS485_B`、`Uart_Tx`、`Uart_Rx`、`Relay_1`、`Relay_2`、`IIC_SCL`、`IIC_SDA`、`VCC_12V`、`VCC_5V`、`VCC_3V3`、`AC_L`、`AC_N`、`F1_2`、`AC_L1`、`AC_L2`、`AC-DC 5V1A`、`RS485_CON`、`RELAY_OUT_CON`、`GROVE`、`BUS1`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO33`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 Atom UART 控制逻辑与 RS485_A/RS485_B | 图 1adcf4e5fc2b / 第 1 页 / 左上 RS485_3V3_Atom 区黄色 U2 SP3485EN-L/TR |
| Q1 | S8050 | 由 Uart_Tx 驱动并控制 U2 /RE 与 DE 共节点 | 图 1adcf4e5fc2b / 第 1 页 / 左上 Uart_Tx-R11-Q1 S8050 与 U2 /RE/DE |
| DZ1-DZ3 | SMAJ6.5CA | RS485_B 对地、A/B 之间及 RS485_A 对地的三级浪涌/瞬态防护 | 图 1adcf4e5fc2b / 第 1 页 / 左上 RS485 A/B 右侧 DZ1-DZ3 SMAJ6.5CA |
| U1 | MP1584 | 将 VCC_12V 降压为 VCC_5V 的开关稳压器 | 图 1adcf4e5fc2b / 第 1 页 / 上中 RS485_DC-DC 区 U1 MP1584 与 L1、D1、反馈网络 |
| JP1 | 未标注 | 引出 GND、VCC_12V、RS485_A 与 RS485_B 的四针端子 | 图 1adcf4e5fc2b / 第 1 页 / 右上 RS485_CON 区 JP1 1-4 脚 |
| GROVE | 未标注 | 引出 IIC_SCL、IIC_SDA、VCC_5V 与 GND 的四针接口 | 图 1adcf4e5fc2b / 第 1 页 / 右上 GROVE 区 IO2/IO1/5V/GND 方框与 I2C 上拉 |
| JK1/JK2 | JQX-115F-005-2ZS4 | 两路 5V 双刀继电器，分别切换 AC_L1 与 AC_L2 | 图 1adcf4e5fc2b / 第 1 页 / 左下 RELAY 区 JK1/JK2，均标注 JQX-115F-005-2ZS4 |
| Q2/Q3 | S8050 | 由 Relay_1/Relay_2 通过 4.7K 电阻驱动的低侧继电器线圈开关 | 图 1adcf4e5fc2b / 第 1 页 / 左下 Q2/Q3 S8050、R15/R16 与 JK1A/JK2A 线圈 |
| D3/D4 | 1N4148 | 分别跨接 JK1/JK2 线圈的续流二极管 | 图 1adcf4e5fc2b / 第 1 页 / 左下 JK1A/JK2A 线圈左侧 D3/D4 1N4148 |
| MD1 | AC-DC 5V1A | 从 AC_L/AC_N 生成 VCC_5V 与 GND 的板载 AC-DC 模块 | 图 1adcf4e5fc2b / 第 1 页 / 下中 AC-DC 区 MD1，AC_1/AC_0/+5V/GND，底部标注 AC-DC 5V1A |
| BUS1 | ATOM | Atom 九针接口，连接双继电器、UART、I2C 和 3.3V/5V/GND | 图 1adcf4e5fc2b / 第 1 页 / 右下 Atom_IO 区 BUS1 ATOM 1-9 脚 |
| JP2 | 未标注 | AC_N/AC_L 市电输入三针端子，2 脚未连接，火线串联 F1 | 图 1adcf4e5fc2b / 第 1 页 / 右中 AC_IN 区 JP2，1 AC_N、2 no-connect、3 保险后火线 |
| JP3/JP4 | 未标注 | 分别引出 AC_N 与 AC_L1/AC_L2 的两路继电器输出端子 | 图 1adcf4e5fc2b / 第 1 页 / 右中下 RELAY_OUT_CON 区 JP3/JP4 |

## 系统结构

### 系统功能分区

原理图分为 RS485_3V3_Atom、RS485_DC-DC、GROVE、RS485_CON、AC_IN、RELAY、AC-DC、RELAY_OUT_CON 和 Atom_IO 功能区。

- 参数与网络：`sections=RS485_3V3_Atom; RS485_DC-DC; GROVE; RS485_CON; AC_IN; RELAY; AC-DC; RELAY_OUT_CON; Atom_IO`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 整页红色分区边框与各分区标题

## 核心器件

### 继电器触点额定值可见性

原理图给出 JK1/JK2 型号 JQX-115F-005-2ZS4 和 5V 线圈连接，但没有在页面上标注触点的电压、电流、负载类别或双刀并联降额。

- 参数与网络：`part_number=JQX-115F-005-2ZS4`；`coil_rail=VCC_5V`；`contact_rating_shown=false`；`parallel_derating_shown=false`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左下 JK1/JK2 型号和触点连接，未见额定值文字

### MD1 具体型号可见性

MD1 只标注 AC-DC 5V1A 和四个功能引脚，没有显示制造商、具体料号、输入范围、隔离等级或保护参数。

- 参数与网络：`reference=MD1`；`visible_marking=AC-DC 5V1A`；`part_number_shown=false`；`input_range_shown=false`；`isolation_rating_shown=false`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 下中 MD1 方框，仅见 AC_1/AC_0/+5V/GND 与 AC-DC 5V1A

## 电源

### U2 3.3V 供电

U2 SP3485EN-L/TR 的 VCC 8 脚接 VCC_3V3，GND 5 脚接 GND，C10 0.1uF/25V 跨接 VCC_3V3 与 GND。

- 参数与网络：`vcc=pin 8 -> VCC_3V3`；`ground=pin 5 -> GND`；`decoupling=C10 0.1uF/25V`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 U2 VCC/GND 与 C10

### MP1584 输入与使能

VCC_12V 连接 U1 MP1584 VIN 7 脚，C7 0.1uF/25V 与 C8 10uF/25V 对地滤波，EN 2 脚经 R7 100K 连接 VCC_12V。

- 参数与网络：`input=VCC_12V -> VIN pin 7`；`input_capacitors=C7 0.1uF/25V; C8 10uF/25V`；`enable=R7 100K from VCC_12V to EN pin 2`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 上中 VCC_12V、C7/C8、R7 与 U1 VIN/EN

### MP1584 5V 输出

U1 SW 1 脚经 L1 10uH 输出 VCC_5V，D1 SS24 从开关节点接 GND，C1 0.1uF/25V 跨 BST 与开关节点；VCC_5V 由 C4 22uF/6.3V、C5/C6 0.1uF/25V 对地滤波。

- 参数与网络：`switch_pin=1`；`inductor=L1 10uH`；`output=VCC_5V`；`catch_diode=D1 SS24`；`bootstrap=C1 0.1uF/25V`；`output_capacitors=C4 22uF/6.3V; C5/C6 0.1uF/25V`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 上中 U1 SW-C1-D1-L1-VCC_5V 与 C4-C6

### MP1584 反馈与补偿

U1 FB 4 脚连接 R4 27K 与 R8 5.1K 的 VCC_5V 对地分压节点；COMP 3 脚经 R10 12K 与 C9 1nF 串联接地，FREQ 6 脚经 R12 100K 接地。

- 参数与网络：`feedback=R4 27K to VCC_5V; R8 5.1K to GND`；`compensation=R10 12K + C9 1nF to GND`；`frequency=R12 100K to GND`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 上中 U1 FB/COMP/FREQ 外围 R4/R8/R10/C9/R12

### 继电器火线公共输入

AC_L 从 JP2 侧经过 F1 250V 1A 形成 F1_2，F1_2 同时连接 JK1 和 JK2 两组触点的公共端 3/6。

- 参数与网络：`input=AC_L`；`fuse=F1 250V 1A`；`protected_net=F1_2`；`relay1_commons=JK1 pins 3 and 6`；`relay2_commons=JK2 pins 3 and 6`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右中 AC_IN 区 AC_L-F1-F1_2 与左下 F1_2 到 JK1/JK2 3/6 脚

### MD1 AC-DC 5V 电源

MD1 的 4 脚 AC_1 接 AC_L，3 脚 AC_0 接 AC_N，2 脚 +5V 输出 VCC_5V，1 脚接 GND；C11 0.1uF/25V 跨接 VCC_5V 与 GND。

- 参数与网络：`pin4=AC_1 -> AC_L`；`pin3=AC_0 -> AC_N`；`pin2=+5V -> VCC_5V`；`pin1=GND`；`decoupling=C11 0.1uF/25V`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 下中 AC-DC 区 MD1 1-4 脚与 C11

### VCC_5V 双电源来源

图中 VCC_5V 同时出现在 U1 MP1584 的 12V 降压输出和 MD1 AC-DC 5V1A 的 +5V 输出，当前页面没有显示两路电源之间的隔离、优先级或防回灌器件。

- 参数与网络：`dc_source=VCC_12V -> U1 MP1584 -> VCC_5V`；`ac_source=AC_L/AC_N -> MD1 -> VCC_5V`；`source_selection_shown=false`；`reverse_current_blocking_shown=false`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 上中 U1 VCC_5V 输出与下中 MD1 VCC_5V 输出，未见两区之间 ORing 器件

## 接口

### JP1 RS485 端子

JP1 的 1 脚接 GND，2 脚经 D2 SS24 连接 VCC_12V，3 脚接 RS485_A，4 脚接 RS485_B。

- 参数与网络：`pin1=GND`；`pin2=VCC_12V through D2 SS24`；`pin3=RS485_A`；`pin4=RS485_B`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右上 RS485_CON 区 D2 与 JP1 1-4 脚

### Grove I2C 接口

GROVE 的 IO2 接 IIC_SCL，IO1 接 IIC_SDA，5V 接 VCC_5V，GND 接地；R1/R2 各 10K 将 IIC_SCL/IIC_SDA 上拉到 VCC_3V3。

- 参数与网络：`io2=IIC_SCL`；`io1=IIC_SDA`；`power=VCC_5V`；`ground=GND`；`pullups=R1/R2 10K to VCC_3V3`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右上 GROVE 区 R1/R2 与 IO2/IO1/5V/GND

### 两路继电器输出端子

JP3 的 1 脚接 AC_N、2 脚未连接、3 脚接 AC_L1；JP4 的 1 脚接 AC_N、2 脚未连接、3 脚接 AC_L2。

- 参数与网络：`jp3=pin1 AC_N; pin2 NC; pin3 AC_L1`；`jp4=pin1 AC_N; pin2 NC; pin3 AC_L2`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右中下 RELAY_OUT_CON 区 JP3/JP4

### JP2 AC 输入端子

JP2 的 1 脚接 AC_N，2 脚标为未连接，3 脚连接 F1 后火线；F1 左侧网络为 AC_L。

- 参数与网络：`pin1=AC_N`；`pin2=not connected`；`pin3=fused AC_L / F1_2`；`pre_fuse_net=AC_L`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右中 AC_IN 区 JP2 与 AC_N、AC_L、F1

## 总线

### RS485 A/B 与偏置

U2 B 7 脚连接 RS485_B，A 6 脚连接 RS485_A；RS485_B 经 R6 4.7K 接 GND，RS485_A 经 R13 4.7K 接 VCC_3V3。

- 参数与网络：`b=U2 pin 7 -> RS485_B; R6 4.7K to GND`；`a=U2 pin 6 -> RS485_A; R13 4.7K to VCC_3V3`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 U2 A/B 与 R6/R13 偏置

### RS485 可选终端

R5 标注 120R/DNP，并跨接 RS485_B 与 RS485_A。

- 参数与网络：`component=R5`；`value=120R/DNP`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 A/B 之间 R5 120R/DNP

## GPIO 与控制信号

### ATOM 九针映射

BUS1 的 9 脚 3V3 接 VCC_3V3，8 脚 G22 接 Relay_1，6 脚 G19 接 Relay_2，4 脚 G23 接 Uart_Tx，2 脚 G33 接 Uart_Rx，7 脚 G21 接 IIC_SCL，5 脚 G25 接 IIC_SDA，3 脚 5V 接 VCC_5V，1 脚接 GND。

- 参数与网络：`pin9=3V3 -> VCC_3V3`；`pin8=G22 -> Relay_1`；`pin6=G19 -> Relay_2`；`pin4=G23 -> Uart_Tx`；`pin2=G33 -> Uart_Rx`；`pin7=G21 -> IIC_SCL`；`pin5=G25 -> IIC_SDA`；`pin3=5V -> VCC_5V`；`pin1=GND`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 右下 BUS1 ATOM 方框的 1-9 脚网络

## 保护电路

### RS485 瞬态防护

DZ1、DZ2、DZ3 均标注 SMAJ6.5CA；DZ1 跨 GND 与 RS485_B，DZ2 跨 RS485_B 与 RS485_A，DZ3 跨 RS485_A 与 GND。

- 参数与网络：`dz1=GND to RS485_B`；`dz2=RS485_B to RS485_A`；`dz3=RS485_A to GND`；`part_number=SMAJ6.5CA`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 RS485 A/B 右侧 DZ1-DZ3

## 关键网络

### RS485 自动方向控制

Uart_Tx 经 R11 4.7K 驱动 Q1 S8050 基极，Q1 发射极接 GND，集电极连接 U2 /RE 2 脚和 DE 3 脚共节点，该节点经 R9 4.7K 上拉到 VCC_3V3。

- 参数与网络：`control=Uart_Tx`；`base_resistor=R11 4.7K`；`transistor=Q1 S8050`；`controlled_pins=U2 /RE pin 2 and DE pin 3`；`pullup=R9 4.7K to VCC_3V3`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 Uart_Tx-R11-Q1 与 U2 /RE/DE、R9

### RS485 UART 数据

U2 RO 1 脚连接 Uart_Rx，并由 R3 4.7K 上拉到 VCC_3V3；U2 DI 4 脚直接接 GND。

- 参数与网络：`receiver=U2 RO pin 1 -> Uart_Rx; R3 4.7K to VCC_3V3`；`driver_input=U2 DI pin 4 -> GND`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左上 U2 RO/Uart_Rx/R3 与 DI-GND

### 继电器 1 线圈驱动

Relay_1 经 R15 4.7K 驱动 Q2 S8050 基极，Q2 发射极接 GND，集电极连接 JK1A 线圈 1 脚；线圈 8 脚接 VCC_5V，D3 1N4148 跨接线圈。

- 参数与网络：`control=Relay_1`；`base_resistor=R15 4.7K`；`transistor=Q2 S8050`；`coil=JK1A pins 8 VCC_5V and 1 Q2 collector`；`flyback=D3 1N4148`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左下上半 Relay_1-R15-Q2-JK1A-D3

### 继电器 2 线圈驱动

Relay_2 经 R16 4.7K 驱动 Q3 S8050 基极，Q3 发射极接 GND，集电极连接 JK2A 线圈 1 脚；线圈 8 脚接 VCC_5V，D4 1N4148 跨接线圈。

- 参数与网络：`control=Relay_2`；`base_resistor=R16 4.7K`；`transistor=Q3 S8050`；`coil=JK2A pins 8 VCC_5V and 1 Q3 collector`；`flyback=D4 1N4148`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左下下半 Relay_2-R16-Q3-JK2A-D4

### 双刀触点并联输出

JK1 的公共端 3/6 并联接 F1_2，NO 端 4/5 并联形成 AC_L1，NC 端 2/7 未连接；JK2 同样以 3/6 接 F1_2、4/5 形成 AC_L2、2/7 未连接。

- 参数与网络：`relay1=3/6 common F1_2; 4/5 output AC_L1; 2/7 NC unused`；`relay2=3/6 common F1_2; 4/5 output AC_L2; 2/7 NC unused`
- 证据：图 1adcf4e5fc2b / 第 1 页 / 左下 JK1B/JK1C 与 JK2B/JK2C 触点编号、F1_2、AC_L1/AC_L2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统功能分区 | `sections=RS485_3V3_Atom; RS485_DC-DC; GROVE; RS485_CON; AC_IN; RELAY; AC-DC; RELAY_OUT_CON; Atom_IO` |
| GPIO 与控制信号 | ATOM 九针映射 | `pin9=3V3 -> VCC_3V3`；`pin8=G22 -> Relay_1`；`pin6=G19 -> Relay_2`；`pin4=G23 -> Uart_Tx`；`pin2=G33 -> Uart_Rx`；`pin7=G21 -> IIC_SCL`；`pin5=G25 -> IIC_SDA`；`pin3=5V -> VCC_5V`；`pin1=GND` |
| 电源 | U2 3.3V 供电 | `vcc=pin 8 -> VCC_3V3`；`ground=pin 5 -> GND`；`decoupling=C10 0.1uF/25V` |
| 关键网络 | RS485 自动方向控制 | `control=Uart_Tx`；`base_resistor=R11 4.7K`；`transistor=Q1 S8050`；`controlled_pins=U2 /RE pin 2 and DE pin 3`；`pullup=R9 4.7K to VCC_3V3` |
| 关键网络 | RS485 UART 数据 | `receiver=U2 RO pin 1 -> Uart_Rx; R3 4.7K to VCC_3V3`；`driver_input=U2 DI pin 4 -> GND` |
| 总线 | RS485 A/B 与偏置 | `b=U2 pin 7 -> RS485_B; R6 4.7K to GND`；`a=U2 pin 6 -> RS485_A; R13 4.7K to VCC_3V3` |
| 总线 | RS485 可选终端 | `component=R5`；`value=120R/DNP`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A` |
| 保护电路 | RS485 瞬态防护 | `dz1=GND to RS485_B`；`dz2=RS485_B to RS485_A`；`dz3=RS485_A to GND`；`part_number=SMAJ6.5CA` |
| 接口 | JP1 RS485 端子 | `pin1=GND`；`pin2=VCC_12V through D2 SS24`；`pin3=RS485_A`；`pin4=RS485_B` |
| 电源 | MP1584 输入与使能 | `input=VCC_12V -> VIN pin 7`；`input_capacitors=C7 0.1uF/25V; C8 10uF/25V`；`enable=R7 100K from VCC_12V to EN pin 2` |
| 电源 | MP1584 5V 输出 | `switch_pin=1`；`inductor=L1 10uH`；`output=VCC_5V`；`catch_diode=D1 SS24`；`bootstrap=C1 0.1uF/25V`；`output_capacitors=C4 22uF/6.3V; C5/C6 0.1uF/25V` |
| 电源 | MP1584 反馈与补偿 | `feedback=R4 27K to VCC_5V; R8 5.1K to GND`；`compensation=R10 12K + C9 1nF to GND`；`frequency=R12 100K to GND` |
| 接口 | Grove I2C 接口 | `io2=IIC_SCL`；`io1=IIC_SDA`；`power=VCC_5V`；`ground=GND`；`pullups=R1/R2 10K to VCC_3V3` |
| 关键网络 | 继电器 1 线圈驱动 | `control=Relay_1`；`base_resistor=R15 4.7K`；`transistor=Q2 S8050`；`coil=JK1A pins 8 VCC_5V and 1 Q2 collector`；`flyback=D3 1N4148` |
| 关键网络 | 继电器 2 线圈驱动 | `control=Relay_2`；`base_resistor=R16 4.7K`；`transistor=Q3 S8050`；`coil=JK2A pins 8 VCC_5V and 1 Q3 collector`；`flyback=D4 1N4148` |
| 电源 | 继电器火线公共输入 | `input=AC_L`；`fuse=F1 250V 1A`；`protected_net=F1_2`；`relay1_commons=JK1 pins 3 and 6`；`relay2_commons=JK2 pins 3 and 6` |
| 关键网络 | 双刀触点并联输出 | `relay1=3/6 common F1_2; 4/5 output AC_L1; 2/7 NC unused`；`relay2=3/6 common F1_2; 4/5 output AC_L2; 2/7 NC unused` |
| 接口 | 两路继电器输出端子 | `jp3=pin1 AC_N; pin2 NC; pin3 AC_L1`；`jp4=pin1 AC_N; pin2 NC; pin3 AC_L2` |
| 接口 | JP2 AC 输入端子 | `pin1=AC_N`；`pin2=not connected`；`pin3=fused AC_L / F1_2`；`pre_fuse_net=AC_L` |
| 电源 | MD1 AC-DC 5V 电源 | `pin4=AC_1 -> AC_L`；`pin3=AC_0 -> AC_N`；`pin2=+5V -> VCC_5V`；`pin1=GND`；`decoupling=C11 0.1uF/25V` |
| 电源 | VCC_5V 双电源来源 | `dc_source=VCC_12V -> U1 MP1584 -> VCC_5V`；`ac_source=AC_L/AC_N -> MD1 -> VCC_5V`；`source_selection_shown=false`；`reverse_current_blocking_shown=false` |
| 核心器件 | 继电器触点额定值可见性 | `part_number=JQX-115F-005-2ZS4`；`coil_rail=VCC_5V`；`contact_rating_shown=false`；`parallel_derating_shown=false` |
| 核心器件 | MD1 具体型号可见性 | `reference=MD1`；`visible_marking=AC-DC 5V1A`；`part_number_shown=false`；`input_range_shown=false`；`isolation_rating_shown=false` |

## 待确认事项

- `review.dual_5v_power_policy`：AC-DC 与 12V DC-DC 两路 VCC_5V 是否允许同时接入，实际硬件如何防止互相回灌？；原因：原理图显示两路电源同名并网，但未显示电源选择或理想二极管/串联隔离。
- `review.relay_and_acdc_ratings`：请确认 JK1/JK2 实装继电器的触点额定值、并联触点降额，以及 MD1 的具体料号与安全认证参数。；原因：这些参数关系到市电负载和隔离安全，当前原理图只给出继电器与 MD1 的有限标识。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1adcf4e5fc2b372c63bf209b857b360a65f0e88a1113681a3a9463a8356b7558` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_sch_01.webp` |

---

源文档：`zh_CN/atom/atomhub_switch_d.md`

源文档 SHA-256：`5f371d81649a10b522e4ad0c8ca48b9020319b3ee3dd0ef7afb329379ca490d9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
