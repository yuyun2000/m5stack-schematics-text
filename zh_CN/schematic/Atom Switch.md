# Atom Switch 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Switch |
| SKU | K042 |
| 产品 ID | `atom-switch-1c4ab8c0f218` |
| 源文档 | `zh_CN/atom/atomhub_switch.md` |

## 概述

Atom Switch 通过 BUS1 连接 Atom，G22/G19 分别控制 Relay_1/Relay_2，G23/G33 连接 SP3485EN-L/TR 的 Uart_Tx/Uart_Rx，G21/G25 引出 Grove I2C。板上两颗 JQX-115F-005-2ZS4 继电器各提供一组外部 COM/双转换端子，线圈由 S8050 低边驱动。系统支持两种 5V 来源：AC_L/AC_N 经 MD1 AC-DC 5V1A，或 RS485 端子的 VCC_12V 经 MP1584 降压；RS485 A/B 配置偏置、可选 120Ω 终端和三颗 SMAJ6.5CA 保护器件。

## 检索关键词

`Atom Switch`、`K042`、`SP3485EN-L/TR`、`MP1584`、`JQX-115F-005-2ZS4`、`AC-DC 5V1A`、`RS485`、`RS485_A`、`RS485_B`、`Uart_Tx`、`Uart_Rx`、`Relay_1`、`Relay_2`、`RelayCOM_1`、`RelayCOM_2`、`IIC_SCL`、`IIC_SDA`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`、`VCC_12V`、`VCC_5V`、`VCC_3V3`、`AC_L`、`AC_N`、`SMAJ6.5CA`、`120R DNP`、`Modbus`、`9-24V`、`250V 10A`、`16A surge`、`Grove I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SP3485EN-L/TR | Atom Uart_Tx/Uart_Rx 与 RS485_A/RS485_B 之间的半双工收发器 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左上 RS485_3V3_Atom 区，U2 SP3485EN-L/TR 的 RO/RE/DE/DI、A/B、VCC/GND |
| U1 | MP1584 | 将 RS485 端子输入的 VCC_12V 降压为 VCC_5V | 图 734dd77e85d1 / 第 1 页 / 第 1 页上中 RS485_DC-DC 区，U1 MP1584、VCC_12V、L1 10uH 和 VCC_5V |
| MD1 | AC-DC 5V1A | 将 AC_L/AC_N 转换为 VCC_5V/GND 的交流输入电源模块 | 图 734dd77e85d1 / 第 1 页 / 第 1 页中下 AC-DC 区，MD1 AC-DC 5V1A 的 AC_1/AC_0/+5V/GND |
| JK1A,JK2A | JQX-115F-005-2ZS4 | 两路 5V 线圈继电器，由 Q2/Q3 低边驱动 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左下 RELAY 区，JK1A/JK2A JQX-115F-005-2ZS4 线圈、VCC_5V、Q2/Q3 与 D3/D4 |
| JK1B,JK1C,JK2B,JK2C | 未标注 | 两颗继电器的双转换触点，分别汇总到 RelayCOM_1/RelayCOM_2 和两路转换端 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左下 JK1B/JK1C 与 JK2B/JK2C 触点、RelayCOM_1/2 和 RelayCON 网络 |
| Q2,Q3 | S8050 | Relay_1/Relay_2 控制的继电器线圈低边驱动晶体管 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左下 Q2/Q3 S8050、R15/R16 4.7K、Relay_1/Relay_2 与线圈 |
| Q1 | S8050 | 由 Uart_Tx 经 R11 驱动的 RS485 RE/DE 方向控制晶体管 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左上 Q1 S8050、R11 4.7K、Uart_Tx 与 U2 RE/DE |
| JP1 | 未标注 | GND、VCC_12V、RS485_A 和 RS485_B 四针接口 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右上 RS485_CON 区，JP1 pin1 GND、pin2 经 D2 到 VCC_12V、pin3 RS485_A、pin4 RS485_B |
| JP2 | 未标注 | 可选 GND、AC_N 和经 F1 输入的 AC_L 三针交流电源接口 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右中 AC_IN 区，JP2 pin1 经 R14M/DNP 可选接 GND、pin2 AC_N、pin3 经 F1 到 AC_L |
| JP3,JP4 | 未标注 | 两路继电器的三针外部 COM/转换触点端子 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右中 RELAY_OUT_CON 区，JP3 RelayCON_1_1/RelayCOM_1/RelayCON_1_2 与 JP4 对应第二路 |
| GROVE | GROVE | IIC_SCL、IIC_SDA、VCC_5V 和 GND 扩展接口 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右上 GROVE 区，IO2 IIC_SCL、IO1 IIC_SDA、5V VCC_5V、GND |
| BUS1 | ATOM | Atom 主控的 I2C、继电器、RS485 UART 和电源接口 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右下 Atom_IO 区，BUS1 G21/G25/G22/G19/G23/G33/3V3/5V/GND |
| DZ1-DZ3 | SMAJ6.5CA | RS485_B、RS485_A 线对地及线间浪涌保护器件 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左上 DZ1/DZ2/DZ3 SMAJ6.5CA 与 RS485_B/RS485_A/GND |
| R5 | 120R/DNP | 跨接 RS485_A/RS485_B 的可选终端电阻 | 图 734dd77e85d1 / 第 1 页 / 第 1 页左上 R5 120R/DNP，跨接 U2 B/A 输出网络 |
| F1,D2 | 250V 1A / SS24 | AC_L 输入保险和 VCC_12V 输入串联二极管保护 | 图 734dd77e85d1 / 第 1 页 / 第 1 页右侧 JP2 AC_L 经 F1 250V1A，以及 JP1 VCC_12V 经 D2 SS24 |

## 系统结构

### Atom Switch 系统架构

Atom Switch 通过 Atom GPIO 控制两路继电器并提供 RS485 和 Grove I2C；系统可由 AC-DC 模块或 RS485 端子 DC-DC 生成 VCC_5V，为 Atom、继电器线圈和接口供电。

- 参数与网络：`host=BUS1 ATOM`；`relay_channels=2`；`relay_parts=JK1A/JK2A JQX-115F-005-2ZS4`；`rs485=U2 SP3485EN-L/TR`；`i2c=GROVE IIC_SCL/IIC_SDA`；`ac_supply=MD1 AC-DC 5V1A`；`dc_supply=U1 MP1584`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页完整原理图，RS485、DC-DC、Grove、Relay、AC-DC、接口和 Atom_IO 功能区

## 电源

### AC 输入到 VCC_5V

JP2 pin3 的 AC_L 经 F1 250V/1A 连接 MD1 AC_1，pin2 AC_N 连接 MD1 AC_0；MD1 +5V/GND 输出形成 VCC_5V/GND，并由 C11 0.1uF/25V 去耦。

- 参数与网络：`connector=JP2`；`line=pin3 -> F1 -> AC_L -> MD1 AC_1`；`neutral=pin2 AC_N -> MD1 AC_0`；`module=MD1 AC-DC 5V1A`；`output=VCC_5V, GND`；`decoupling=C11 0.1uF/25V`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页右中 AC_IN 与中下 AC-DC 区，JP2/F1/AC_L/AC_N/MD1/C11

### RS485 端子 DC 输入到 VCC_5V

JP1 pin2 经 D2 SS24 形成 VCC_12V，U1 MP1584 以 VCC_12V 为输入，通过 L1 10uH 和反馈/补偿网络生成 VCC_5V。

- 参数与网络：`connector=JP1 pin2`；`input_diode=D2 SS24`；`input_rail=VCC_12V`；`converter=U1 MP1584`；`inductor=L1 10uH`；`output=VCC_5V`；`enable_pull=R7 100K to VCC_12V`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页右上 JP1/D2 与上中 U1 MP1584/VCC_12V/L1/VCC_5V

### VCC_5V 负载分配

AC-DC 与 MP1584 两个电源模块都连接 VCC_5V；该电源轨连接 BUS1 Atom 5V、Grove 5V、JK1A/JK2A 线圈和相关去耦电容。

- 参数与网络：`sources=MD1 AC-DC output, U1 MP1584 output`；`loads=BUS1 5V, GROVE 5V, JK1A/JK2A coils`；`rail=VCC_5V`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页 AC-DC、RS485_DC-DC、RELAY、GROVE 和 Atom_IO 区的 VCC_5V 网络

## 接口

### Atom 主控引脚映射

BUS1 G21=IIC_SCL、G25=IIC_SDA、G22=Relay_1、G19=Relay_2、G23=Uart_Tx、G33=Uart_Rx，并连接 VCC_3V3、VCC_5V 和 GND。

- 参数与网络：`G21=IIC_SCL`；`G25=IIC_SDA`；`G22=Relay_1`；`G19=Relay_2`；`G23=Uart_Tx`；`G33=Uart_Rx`；`power=VCC_3V3, VCC_5V, GND`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页右下 BUS1 ATOM 逐针网络

### 两路继电器外部触点端子

JP3 依次引出 RelayCON_1_1、RelayCOM_1、RelayCON_1_2，JP4 依次引出 RelayCON_2_1、RelayCOM_2、RelayCON_2_2；每组对应一颗继电器的公共端和两路转换端。

- 参数与网络：`JP3=RelayCON_1_1, RelayCOM_1, RelayCON_1_2`；`JP4=RelayCON_2_1, RelayCOM_2, RelayCON_2_2`；`relay_1_contacts=JK1B/JK1C`；`relay_2_contacts=JK2B/JK2C`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页左下继电器触点与右中 JP3/JP4 RELAY_OUT_CON

### Atom 到 RS485 收发器 UART

BUS1 G23 连接 Uart_Tx，G33 连接 Uart_Rx；U2 RO 输出 Uart_Rx，Uart_Tx 经 R11 4.7kΩ 驱动 Q1 以控制 RE/DE，U2 A/B 连接 RS485_A/RS485_B。

- 参数与网络：`host_tx=G23 Uart_Tx`；`host_rx=G33 Uart_Rx`；`transceiver=U2 SP3485EN-L/TR`；`direction_control=Uart_Tx -> R11 -> Q1 -> RE/DE`；`bus=RS485_A, RS485_B`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页左上 U2/Q1/Uart_Tx/Uart_Rx 与右下 BUS1 G23/G33

### JP1 RS485 与 DC 电源端子

JP1 pin1=GND、pin2 经 D2 连接 VCC_12V、pin3=RS485_A、pin4=RS485_B。

- 参数与网络：`pin1=GND`；`pin2=DC input via D2 to VCC_12V`；`pin3=RS485_A`；`pin4=RS485_B`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页右上 RS485_CON JP1

### Grove I2C 接口

Grove IO2=IIC_SCL/G21、IO1=IIC_SDA/G25、5V=VCC_5V、GND=GND；SCL/SDA 各由 10kΩ 电阻上拉到 VCC_3V3。

- 参数与网络：`io2=IIC_SCL G21`；`io1=IIC_SDA G25`；`power=VCC_5V`；`ground=GND`；`pullups=10K each to VCC_3V3`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页右上 GROVE 区与右下 BUS1 G21/G25

## GPIO 与控制信号

### 两路继电器驱动

Relay_1 经 R15 4.7kΩ 驱动 Q2 S8050，Relay_2 经 R16 4.7kΩ 驱动 Q3 S8050；Q2/Q3 分别低边控制 JK1A/JK2A 的 5V 线圈，D3/D4 1N4148 跨接线圈。

- 参数与网络：`channel_1=G22 Relay_1 -> R15 -> Q2 -> JK1A`；`channel_2=G19 Relay_2 -> R16 -> Q3 -> JK2A`；`coil_supply=VCC_5V`；`flyback=D3/D4 1N4148`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页左下 RELAY 区与右下 BUS1 Relay_1/Relay_2

## 保护电路

### RS485 偏置与可选终端

RS485_B 由 R6 4.7kΩ 下拉到 GND，RS485_A 由 R13 4.7kΩ 上拉到 VCC_3V3，R5 120R/DNP 跨接 A/B 作为可选终端。

- 参数与网络：`B_bias=R6 4.7K to GND`；`A_bias=R13 4.7K to VCC_3V3`；`termination=R5 120R/DNP across A/B`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页左上 U2 A/B、R5/R6/R13 与 RS485_A/RS485_B

### RS485 浪涌保护

DZ1/DZ2/DZ3 三颗 SMAJ6.5CA 配置在 RS485_B、RS485_A 与 GND 周围，形成线对地及线间保护网络。

- 参数与网络：`devices=DZ1, DZ2, DZ3 SMAJ6.5CA`；`protected_nets=RS485_A, RS485_B`；`reference=GND`
- 证据：图 734dd77e85d1 / 第 1 页 / 第 1 页左上 DZ1-DZ3 与 RS485_B/RS485_A/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom Switch 系统架构 | `host=BUS1 ATOM`；`relay_channels=2`；`relay_parts=JK1A/JK2A JQX-115F-005-2ZS4`；`rs485=U2 SP3485EN-L/TR`；`i2c=GROVE IIC_SCL/IIC_SDA`；`ac_supply=MD1 AC-DC 5V1A`；`dc_supply=U1 MP1584` |
| 电源 | AC 输入到 VCC_5V | `connector=JP2`；`line=pin3 -> F1 -> AC_L -> MD1 AC_1`；`neutral=pin2 AC_N -> MD1 AC_0`；`module=MD1 AC-DC 5V1A`；`output=VCC_5V, GND`；`decoupling=C11 0.1uF/25V` |
| 电源 | RS485 端子 DC 输入到 VCC_5V | `connector=JP1 pin2`；`input_diode=D2 SS24`；`input_rail=VCC_12V`；`converter=U1 MP1584`；`inductor=L1 10uH`；`output=VCC_5V`；`enable_pull=R7 100K to VCC_12V` |
| 电源 | VCC_5V 负载分配 | `sources=MD1 AC-DC output, U1 MP1584 output`；`loads=BUS1 5V, GROVE 5V, JK1A/JK2A coils`；`rail=VCC_5V` |
| 接口 | Atom 主控引脚映射 | `G21=IIC_SCL`；`G25=IIC_SDA`；`G22=Relay_1`；`G19=Relay_2`；`G23=Uart_Tx`；`G33=Uart_Rx`；`power=VCC_3V3, VCC_5V, GND` |
| GPIO 与控制信号 | 两路继电器驱动 | `channel_1=G22 Relay_1 -> R15 -> Q2 -> JK1A`；`channel_2=G19 Relay_2 -> R16 -> Q3 -> JK2A`；`coil_supply=VCC_5V`；`flyback=D3/D4 1N4148` |
| 接口 | 两路继电器外部触点端子 | `JP3=RelayCON_1_1, RelayCOM_1, RelayCON_1_2`；`JP4=RelayCON_2_1, RelayCOM_2, RelayCON_2_2`；`relay_1_contacts=JK1B/JK1C`；`relay_2_contacts=JK2B/JK2C` |
| 接口 | Atom 到 RS485 收发器 UART | `host_tx=G23 Uart_Tx`；`host_rx=G33 Uart_Rx`；`transceiver=U2 SP3485EN-L/TR`；`direction_control=Uart_Tx -> R11 -> Q1 -> RE/DE`；`bus=RS485_A, RS485_B` |
| 接口 | JP1 RS485 与 DC 电源端子 | `pin1=GND`；`pin2=DC input via D2 to VCC_12V`；`pin3=RS485_A`；`pin4=RS485_B` |
| 保护电路 | RS485 偏置与可选终端 | `B_bias=R6 4.7K to GND`；`A_bias=R13 4.7K to VCC_3V3`；`termination=R5 120R/DNP across A/B` |
| 保护电路 | RS485 浪涌保护 | `devices=DZ1, DZ2, DZ3 SMAJ6.5CA`；`protected_nets=RS485_A, RS485_B`；`reference=GND` |
| 接口 | Grove I2C 接口 | `io2=IIC_SCL G21`；`io1=IIC_SDA G25`；`power=VCC_5V`；`ground=GND`；`pullups=10K each to VCC_3V3` |
| 电源 | 产品正文中的 AC/DC 输入范围 | `documented_ac=AC 250V`；`documented_dc=DC 9-24V`；`schematic_ac=MD1 AC-DC 5V1A with F1 250V/1A`；`schematic_dc=VCC_12V to MP1584` |
| 电源 | 产品正文中的继电器额定值 | `documented_ac_rating=250V 10A`；`documented_inrush=16A`；`schematic_relay=JQX-115F-005-2ZS4` |
| 总线 | 产品正文中的 Modbus 支持 | `documented_protocol=Modbus`；`physical_layer=SP3485EN-L/TR RS485`；`firmware_parameters=null` |

## 待确认事项

- `power.documented-input-ranges`：产品正文给出 AC 250V 输入和 RS485 DC 9-24V 供电范围，但原理图只标 MD1 AC-DC 5V1A、F1 250V/1A、VCC_12V 与 MP1584，未给出完整输入范围和降额条件。（证据：图 734dd77e85d1 / 第 1 页 / 第 1 页 AC_IN/AC-DC 与 RS485_CON/RS485_DC-DC，图中无输入范围表）
- `power.documented-relay-rating`：产品正文给出 AC 250V@10A 和瞬时 16A，但原理图只给出 JQX-115F-005-2ZS4 料号、线圈和触点连接，无法确认 PCB、端子、温升和安全规范下的整机额定能力。（证据：图 734dd77e85d1 / 第 1 页 / 第 1 页 RELAY 与 RELAY_OUT_CON 区，图中无整机额定值）
- `bus.documented-modbus`：产品正文称 RS485 支持 Modbus，但原理图只定义 Uart_Tx/Uart_Rx 到 SP3485EN 的物理层，未定义波特率、帧格式、地址或 Modbus 固件行为。（证据：图 734dd77e85d1 / 第 1 页 / 第 1 页 RS485_3V3_Atom 与 Atom_IO，只显示 UART/RS485 物理网络）
- `review.input-ranges`：Atom Switch 的 AC 输入额定范围和 RS485 DC 9-24V 范围在温升、负载和安全认证条件下如何定义？；原因：原理图只给电源模块、保险和网络名，无法验证完整工作范围与降额曲线。
- `review.relay-rating`：250V@10A 和瞬时 16A 是否已按继电器、JP3/JP4 端子、PCB 铜厚、温升和绝缘距离完成整机验证？；原因：继电器料号本身不足以证明整机端到端额定能力。
- `review.modbus-firmware`：当前 Atom Switch 配套固件的 Modbus 角色、地址、波特率、校验和寄存器映射是什么？；原因：Modbus 是固件协议，当前原理图只能确认 RS485 物理层。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `734dd77e85d119827f782fd459601062865d05d694e975cda7ce67dadbd9fba7` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_sch_01.webp` |

---

源文档：`zh_CN/atom/atomhub_switch.md`

源文档 SHA-256：`89fb1abc451e711f889023635192b702e4a432d140db8f0b243f3f8777989248`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
