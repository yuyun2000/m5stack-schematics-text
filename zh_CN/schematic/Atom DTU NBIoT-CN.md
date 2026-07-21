# Atom DTU NBIoT-CN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU NBIoT-CN |
| SKU | K060 |
| 产品 ID | `atom-dtu-nbiot-cn-761b536e6b99` |
| 源文档 | `zh_CN/atom/atom_dtu_nb_cn.md` |

## 概述

Atom DTU NBIoT-CN 以 M1 SIM7020G/SIM7020C 蜂窝模组为核心，包含 Micro-SIM 接口、SMF05CT1G SIM 信号防护、SMA 天线、STATUS/NETLIGHT 指示以及 Atom UART 的 3.3V/1.8V 电平转换。P1 的 12V 输入经 MP1584EN 生成 +5V，SP3485EN-L/TR 将 Atom G23/G33 的 TX/RX 转换为带偏置、可选终端和 SP4021 保护的 RS485_A/RS485_B。Grove I2C 与 Atom 4Pin/5Pin 同时引出；原理图给出 SIM7020G/C 共用设计，未单独确认 K060 装配后缀和固件网络参数。

## 检索关键词

`Atom DTU NBIoT-CN`、`K060`、`SIM7020C`、`SIM7020G`、`NB-IoT`、`Cat-NB`、`MP1584EN`、`SP3485EN-L/TR`、`SMF05CT1G`、`MicroSIM`、`SIM_VCC`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`STATUS`、`NETLIGHT`、`U1_TX`、`U1_RX`、`NB_TX`、`NB_RX`、`RS485_A`、`RS485_B`、`ANT_SMA-KWE`、`+VIN`、`+5V`、`+3.3V`、`+1.8V`、`G19`、`G22`、`G23`、`G33`、`G21`、`G25`、`Atom-5Pin`、`Atom-4Pin`、`HY-2.0_IIC`、`SP4021-01FTG-C`、`115200bps`、`B1/B3/B5/B8`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7020G/SIM7020C | NB-IoT 蜂窝通信模组，连接 UART、SIM、天线、状态指示和多组电源/GPIO | 图 5b62a55c7039 / 第 1 页 / 第 1 页中央 M1 SIM7020G/SIM7020C，UART1、SIM、STATUS/NETLIGHT、VDD_EXT、VBAT、USB 和 UART2 引脚 |
| U1 | MP1584EN | 从 +VIN 生成 +5V 的降压转换器 | 图 5b62a55c7039 / 第 1 页 / 第 1 页左上 U1 MP1584EN、F1、L1 10uH、R7/R8 与 +VIN/+5V |
| U2 | SMF05CT1G | SIM_VCC、SIM_DATA、SIM_CLK、SIM_RST 周围的多通道 ESD 防护器件 | 图 5b62a55c7039 / 第 1 页 / 第 1 页中左 U2 SMF05CT1G，连接 SIM_VCC/SIM_DATA/SIM_CLK/SIM_RST 与 GND |
| U3 | SIM | SIM 卡连接器，连接 IO、CLK、RST、VCC 和 GND | 图 5b62a55c7039 / 第 1 页 / 第 1 页中左 U3 SIM，IO/CLK/RST/VCC/GND/VPP |
| U4 | SP3485EN-L/TR | 3.3V 逻辑侧 TX/RX 与 RS485_A/RS485_B 的半双工收发器 | 图 5b62a55c7039 / 第 1 页 / 第 1 页左下 U4 SP3485EN-L/TR，RO/RE/DE/DI、A/B、VCC/GND |
| Q1,Q2 | SS8050 Y1 | 由 STATUS/NETLIGHT 控制的 D1/D2 低边 LED 驱动晶体管 | 图 5b62a55c7039 / 第 1 页 / 第 1 页右上 Q1/Q2 SS8050 Y1、D1/D2、R1-R6 与 STATUS/NETLIGHT |
| Q3,Q5 | SS8050 Y1 | NB_RX/NB_TX 与 U1_RX/U1_TX 之间的 3.3V/1.8V UART 电平转换器件 | 图 5b62a55c7039 / 第 1 页 / 第 1 页下中右 Q3/Q5 SS8050 Y1、R16-R18/R23/R26/R27 与 NB_RX/NB_TX/U1_RX/U1_TX |
| Q4 | SS8050 Y1 | 由 TX 经 R24 驱动的 RS485 RE/DE 方向控制晶体管 | 图 5b62a55c7039 / 第 1 页 / 第 1 页左下 Q4 SS8050 Y1、R24 1KΩ 与 U4 RE/DE |
| E1 | ANT_SMA-KWE | SIM7020G/C 外部 SMA 天线接口 | 图 5b62a55c7039 / 第 1 页 / 第 1 页中右 E1 ANT_SMA-KWE 与 M1 射频接口、GND 屏蔽端 |
| P1 | HDR_4P | RS485 B/A 与 12V+/12V- 电源端子 | 图 5b62a55c7039 / 第 1 页 / 第 1 页右中 P1 HDR_4P，RS485_B/RS485_A/+VIN/GND 与 B/A/12V+/12V- |
| J1 | HY-2.0_IIC | G21/G25 I2C 与 +5V/GND Grove 接口 | 图 5b62a55c7039 / 第 1 页 / 第 1 页右中 J1 HY-2.0_IIC，G21/IIC_SCL、G25/IIC_SDA、+5V、GND |
| P2,P3 | Atom-5Pin / Atom-4Pin | Atom 主控的 3.3V、蜂窝 UART、RS485 UART、I2C、5V 与 GND 接口 | 图 5b62a55c7039 / 第 1 页 / 第 1 页右下 P2 Atom-5Pin 与 P3 Atom-4Pin 的逐针网络 |
| D6,D7,D8 | SP4021-01FTG-C | RS485_A/RS485_B 线对地及线间浪涌保护网络 | 图 5b62a55c7039 / 第 1 页 / 第 1 页下中 D6/D7/D8 SP4021-01FTG-C 与 RS485_B/RS485_A/GND |
| R22 | 120Ω/NC | 跨接 RS485_A/RS485_B 的可选终端电阻 | 图 5b62a55c7039 / 第 1 页 / 第 1 页下中 R22 120Ω/NC，跨接 RS485_B 与 RS485_A |
| F1 | 1.5A/24V | +VIN 输入保险丝 | 图 5b62a55c7039 / 第 1 页 / 第 1 页左上 +VIN 串联 F1 1.5A/24V 到 U1 VIN |

## 系统结构

### Atom DTU NBIoT-CN 系统架构

电路由 SIM7020G/SIM7020C 模组、SIM 卡与防护、SMA 天线、双向 UART 电平转换、状态指示、MP1584EN 5V 电源、SP3485EN RS485 和 Grove I2C 组成。

- 参数与网络：`cellular_module=M1 SIM7020G/SIM7020C`；`sim=U3 SIM with U2 SMF05CT1G`；`antenna=E1 ANT_SMA-KWE`；`cellular_uart=NB_RX/NB_TX <-> U1_RX/U1_TX`；`rs485=U4 SP3485EN-L/TR`；`power_converter=U1 MP1584EN`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页完整原理图，电源、M1、SIM、LED、天线、RS485、Atom 与 Grove 区

## 核心器件

### SIM7020G/SIM7020C 蜂窝模组

M1 型号字段明确为 SIM7020G/SIM7020C，原理图引出两组 UART、SIM、STATUS/NETLIGHT、VDD_EXT、PWRKEY、ADC、USB、RESET、GPIO 和多组电源地。

- 参数与网络：`reference=M1`；`part_number=SIM7020G/SIM7020C`；`uart1=pin1 UART1_TXD, pin2 UART1_RXD`；`sim=pin14 SIM_DET, pin15 SIM_DATA, pin16 SIM_CLK, pin17 SIM_RST, pin18 SIM_VDD`；`status=pin42 STATUS, pin41 NETLIGHT`；`aux_supply=pin40 VDD_EXT`；`reset=pin28 RESET`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页中央 M1 SIM7020G/SIM7020C 全部引脚标签

## 电源

### 12V 输入到 +5V 降压

P1 12V+ 连接 +VIN，+VIN 经 F1 1.5A/24V 进入 U1 MP1584EN；SW 经 L1 10uH 和 D3 SS54 形成降压输出，R7 51kΩ/R8 10kΩ 反馈，输出网络为 +5V。

- 参数与网络：`terminal=P1 12V+ / 12V-`；`input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D3 SS54`；`feedback=R7 51K, R8 10K`；`output=+5V`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页左上 U1 电源区与右中 P1，+VIN/F1/MP1584EN/L1/R7/R8/+5V

### SIM7020G/C 3.3V 与 1.8V 电源

P2 pin1 引入 +3.3V，连接 M1 VBAT pin34/pin35 和逻辑供电节点；M1 VDD_EXT pin40 输出 +1.8V，并由 C7 22uF 去耦到 GND，+1.8V 同时用于 UART 电平转换上拉。

- 参数与网络：`host_supply=+3.3V from P2 pin1`；`module_vbat=M1 pin34/pin35`；`module_aux_output=M1 pin40 VDD_EXT -> +1.8V`；`aux_decoupling=C7 22uF`；`level_shift_rail=+1.8V`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页 M1 VBAT/+3.3V、VDD_EXT/+1.8V/C7 与右下 P2 pin1

## 接口

### SIM 卡连接与信号

M1 SIM_DATA/SIM_CLK/SIM_RST 经三颗 22Ω 串联电阻连接 U3 IO/CLK/RST，M1 SIM_VDD 形成 SIM_VCC 并连接 U3 VCC；U3 GND 接系统 GND。

- 参数与网络：`data=M1 pin15 SIM_DATA -> 22R -> U3 IO`；`clock=M1 pin16 SIM_CLK -> 22R -> U3 CLK`；`reset=M1 pin17 SIM_RST -> 22R -> U3 RST`；`supply=M1 pin18 SIM_VDD -> SIM_VCC -> U3 VCC`；`ground=U3 GND -> GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页中左 M1 SIM_DATA/CLK/RST/VDD、22Ω 电阻、U3 SIM 与 SIM_VCC

### Atom 与 SIM7020 UART 电平转换

P2 pin2 G22 连接 NB_RX，P2 pin3 G19 连接 NB_TX；Q3 与 R16/R17/R18 在 NB_RX 和 U1_RX 之间转换，Q5 与 R23/R26/R27 在 NB_TX 和 U1_TX 之间转换，电平参考为 +3.3V 与 +1.8V。

- 参数与网络：`host_to_module=P2 pin2 G22 NB_RX <-> Q3 network <-> U1_RX/M1 UART1_RXD pin2`；`module_to_host=M1 UART1_TXD pin1/U1_TX <-> Q5 network <-> NB_TX/P2 pin3 G19`；`logic_rails=+3.3V and +1.8V`；`devices=Q3/Q5 SS8050 Y1`；`resistors=R16/R17/R18/R23/R26/R27 4.7K`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页 M1 UART1_TXD/RXD、下中右 Q3/Q5 电平转换与右下 P2 G22/G19

### Atom 与 RS485 UART 映射

P2 pin4 G23 连接 TX，pin5 G33 连接 RX；RX 经 R20 1kΩ 接 U4 RO 并由 R21 4.7kΩ 上拉，TX 经 R24 1kΩ 驱动 Q4 以控制 U4 RE/DE。

- 参数与网络：`host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U4 RO via R20 1K to RX`；`rx_pullup=R21 4.7K to +3.3V`；`direction_control=TX via R24 1K and Q4 SS8050 Y1`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页右下 P2 G23/G33/TX/RX 与左下 U4/R20/R21/Q4/R24

### P1 RS485 与电源端子

P1 HDR_4P 依次引出 RS485_B、RS485_A、+VIN 和 GND，端子功能标注为 B、A、12V+、12V-。

- 参数与网络：`B=RS485_B`；`A=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页右中 P1 HDR_4P 的 RS485_B/RS485_A/+VIN/GND

### J1 Grove I2C 接口

J1 HY-2.0_IIC 的 pin1 IIC_SCL=G21、pin2 IIC_SDA=G25、pin3 VCC=+5V、pin4 GND=GND；同名网络连接 P3 Atom-4Pin。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页右中 J1 与右下 P3 的 G21/G25/+5V/GND

## GPIO 与控制信号

### STATUS 与 NETLIGHT 指示灯

M1 STATUS pin42 经 R3 1kΩ 驱动 Q1，控制 +5V-R1-D1 指示支路；NETLIGHT pin41 经 R4 1kΩ 驱动 Q2，控制 +5V-R2-D2 指示支路，R5/R6 各 10kΩ 下拉。

- 参数与网络：`status=M1 pin42 STATUS -> R3 -> Q1 -> D1`；`netlight=M1 pin41 NETLIGHT -> R4 -> Q2 -> D2`；`led_supply=+5V`；`led_resistors=R1/R2 1K`；`base_pulldowns=R5/R6 10K`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页右上 D1/D2、Q1/Q2、R1-R6 与中央 M1 STATUS/NETLIGHT

## 保护电路

### +VIN 输入保护与滤波

+VIN 经 F1 串联保护，D5 SS54 和 C2 10uF 从保险后输入节点接到 GND，U1 EN pin2 标为未连接。

- 参数与网络：`fuse=F1 1.5A/24V`；`shunt_diode=D5 SS54`；`input_capacitor=C2 10uF`；`enable_pin=U1 EN pin2 NC`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页左上 +VIN/F1/D5/C2/U1 EN

### SIM 接口 ESD 与滤波

U2 SMF05CT1G 连接 SIM_VCC 和三条 SIM 信号并参考 GND；C8 100nF 为 SIM_VCC 去耦，C9/C10/C11 各 33pF 对 SIM 信号提供对地滤波。

- 参数与网络：`esd_array=U2 SMF05CT1G`；`protected_nets=SIM_VCC, SIM_DATA, SIM_CLK, SIM_RST`；`supply_decoupling=C8 100nF`；`signal_capacitors=C9/C10/C11 33pF`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页中左 U2 SMF05CT1G、C8-C11 与 SIM 信号

### RS485 偏置与可选终端

RS485_B 由 R19 4.7kΩ 下拉到 GND，RS485_A 由 R25 4.7kΩ 上拉到 +3.3V；R22 120Ω/NC 跨接 A/B 作为可选终端。

- 参数与网络：`B_bias=R19 4.7K to GND`；`A_bias=R25 4.7K to +3.3V`；`termination=R22 120R/NC across A/B`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页下中 U4 A/B、R19/R25 与 R22 120Ω/NC

### RS485 浪涌保护

D6/D7/D8 三颗 SP4021-01FTG-C 配置在 RS485_B、RS485_A 与 GND 周围，形成线对地及线间保护网络。

- 参数与网络：`devices=D6, D7, D8 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页下中 D6/D7/D8 与 RS485_B/RS485_A/GND

## 射频

### SIM7020G/C 外部天线接口

M1 的射频端连接 E1 ANT_SMA-KWE，E1 屏蔽端接 GND。

- 参数与网络：`module=M1 SIM7020G/SIM7020C`；`connector=E1 ANT_SMA-KWE`；`shield=GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 第 1 页中右 M1 射频端到 E1 ANT_SMA-KWE 与 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU NBIoT-CN 系统架构 | `cellular_module=M1 SIM7020G/SIM7020C`；`sim=U3 SIM with U2 SMF05CT1G`；`antenna=E1 ANT_SMA-KWE`；`cellular_uart=NB_RX/NB_TX <-> U1_RX/U1_TX`；`rs485=U4 SP3485EN-L/TR`；`power_converter=U1 MP1584EN` |
| 电源 | 12V 输入到 +5V 降压 | `terminal=P1 12V+ / 12V-`；`input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D3 SS54`；`feedback=R7 51K, R8 10K`；`output=+5V` |
| 保护电路 | +VIN 输入保护与滤波 | `fuse=F1 1.5A/24V`；`shunt_diode=D5 SS54`；`input_capacitor=C2 10uF`；`enable_pin=U1 EN pin2 NC` |
| 电源 | SIM7020G/C 3.3V 与 1.8V 电源 | `host_supply=+3.3V from P2 pin1`；`module_vbat=M1 pin34/pin35`；`module_aux_output=M1 pin40 VDD_EXT -> +1.8V`；`aux_decoupling=C7 22uF`；`level_shift_rail=+1.8V` |
| 核心器件 | SIM7020G/SIM7020C 蜂窝模组 | `reference=M1`；`part_number=SIM7020G/SIM7020C`；`uart1=pin1 UART1_TXD, pin2 UART1_RXD`；`sim=pin14 SIM_DET, pin15 SIM_DATA, pin16 SIM_CLK, pin17 SIM_RST, pin18 SIM_VDD`；`status=pin42 STATUS, pin41 NETLIGHT`；`aux_supply=pin40 VDD_EXT`；`reset=pin28 RESET` |
| 核心器件 | K060 实际装配的 SIM7020 后缀 | `documented_variant=SIM7020C`；`schematic_variants=SIM7020G/SIM7020C`；`assembly_confirmed=false` |
| 接口 | SIM 卡连接与信号 | `data=M1 pin15 SIM_DATA -> 22R -> U3 IO`；`clock=M1 pin16 SIM_CLK -> 22R -> U3 CLK`；`reset=M1 pin17 SIM_RST -> 22R -> U3 RST`；`supply=M1 pin18 SIM_VDD -> SIM_VCC -> U3 VCC`；`ground=U3 GND -> GND` |
| 保护电路 | SIM 接口 ESD 与滤波 | `esd_array=U2 SMF05CT1G`；`protected_nets=SIM_VCC, SIM_DATA, SIM_CLK, SIM_RST`；`supply_decoupling=C8 100nF`；`signal_capacitors=C9/C10/C11 33pF` |
| 射频 | SIM7020G/C 外部天线接口 | `module=M1 SIM7020G/SIM7020C`；`connector=E1 ANT_SMA-KWE`；`shield=GND` |
| GPIO 与控制信号 | STATUS 与 NETLIGHT 指示灯 | `status=M1 pin42 STATUS -> R3 -> Q1 -> D1`；`netlight=M1 pin41 NETLIGHT -> R4 -> Q2 -> D2`；`led_supply=+5V`；`led_resistors=R1/R2 1K`；`base_pulldowns=R5/R6 10K` |
| 接口 | Atom 与 SIM7020 UART 电平转换 | `host_to_module=P2 pin2 G22 NB_RX <-> Q3 network <-> U1_RX/M1 UART1_RXD pin2`；`module_to_host=M1 UART1_TXD pin1/U1_TX <-> Q5 network <-> NB_TX/P2 pin3 G19`；`logic_rails=+3.3V and +1.8V`；`devices=Q3/Q5 SS8050 Y1`；`resistors=R16/R17/R18/R23/R26/R27 4.7K` |
| 接口 | Atom 与 RS485 UART 映射 | `host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U4 RO via R20 1K to RX`；`rx_pullup=R21 4.7K to +3.3V`；`direction_control=TX via R24 1K and Q4 SS8050 Y1` |
| 接口 | P1 RS485 与电源端子 | `B=RS485_B`；`A=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-` |
| 保护电路 | RS485 偏置与可选终端 | `B_bias=R19 4.7K to GND`；`A_bias=R25 4.7K to +3.3V`；`termination=R22 120R/NC across A/B` |
| 保护电路 | RS485 浪涌保护 | `devices=D6, D7, D8 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin` |
| 总线 | 产品正文中的蜂窝频段与协议参数 | `documented_bands=B1/B3/B5/B8`；`documented_baud=115200bps`；`documented_protocols=TCP, UDP, LWM2M, CoAP, MQTT, HTTP, HTTPS, TLS, DTLS, DNS, NTP`；`schematic_module=SIM7020G/SIM7020C` |

## 待确认事项

- `component.cellular-variant`：产品正文指定 SIM7020C，但当前原理图的 M1 型号字段为 SIM7020G/SIM7020C 共用设计，无法仅凭原理图确认 K060 实际装配的是 C 还是 G 后缀。（证据：图 5b62a55c7039 / 第 1 页 / 第 1 页中央 M1 型号字段标为 SIM7020G/SIM7020C）
- `bus.documented-cellular-capabilities`：产品正文给出 Cat-NB B1/B3/B5/B8、UART 115200bps 以及 TCP/UDP/LWM2M/CoAP/MQTT/HTTP 等协议，但当前原理图只显示 SIM7020G/C 和物理接口，未标注这些频段、波特率或协议栈。（证据：图 5b62a55c7039 / 第 1 页 / 第 1 页 M1 SIM7020G/SIM7020C 与 UART/SIM/天线连接，图中无频段、波特率或协议列表）
- `review.cellular-variant`：K060 当前出货硬件的 M1 是否固定装配 SIM7020C，而不是共用原理图中允许的 SIM7020G？；原因：产品正文指定 SIM7020C，但原理图型号字段同时列出 SIM7020G/SIM7020C，需要 BOM 或模组丝印确认。
- `review.cellular-capabilities`：当前 SIM7020C 固件和运营商版本是否完整支持正文所列 B1/B3/B5/B8、115200bps 和全部网络协议？；原因：这些是模组和固件能力，当前原理图无法验证具体区域版本、固件配置和协议支持范围。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5b62a55c7039274af90a41bc3cd61c1b1b7b6d24ea41ea1b133f40f4c95c647c` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb/atom_dtu_nb_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_dtu_nb_cn.md`

源文档 SHA-256：`9543ee9d9141865ba104b558e20ff769e98c3974f2cac2fdeaac07ecf520e08a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
