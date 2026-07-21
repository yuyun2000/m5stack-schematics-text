# Atomic PoE Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic PoE Base |
| SKU | A091 |
| 产品 ID | `atomic-poe-base-3b5470e5815f` |
| 源文档 | `zh_CN/atom/Atomic PoE Base.md` |

## 概述

Atomic PoE Base 使用 U1 W5500，以 GPIO33/GPIO23/GPIO22/GPIO19 构成 SPI 接口，并由 Y1 25MHz 有源时钟驱动。W5500 的 TX/RX 差分信号经 R5、T1 网络变压器连接 P9 RJ45；变压器中心抽头 VA1/VA2 与 RJ45 空闲对 VB1/VB2 接入 P1，P1 输出 5V。INF+ 还经 D1 SS54 接入 5V，并由 U2 BL8075CB5TR33 生成 D3V3，再通过 FB1 分为 A3V3。P2/P3 连接 Atom 主机，另有可选供电的 I2C 接口。P1 未标型号，W5500 协议、socket 数量和以太网速率也未写在图纸上，因此正文中的 IEEE 802.3af 与芯片能力需要数据手册或 BOM 复核。

## 检索关键词

`Atomic PoE Base`、`A091`、`W5500`、`SPI`、`GPIO33`、`GPIO23`、`GPIO22`、`GPIO19`、`25MHz`、`R5 33R`、`T1 Net Trans`、`RJ45`、`P9`、`PoE`、`IEEE 802.3af`、`VA1`、`VA2`、`VB1`、`VB2`、`INF+`、`5V`、`D3V3`、`A3V3`、`BL8075CB5TR33`、`SS54`、`G21`、`G25`、`ACTLED`、`LINKLED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | W5500 | SPI 以太网控制器，连接外部 25MHz 时钟、差分收发网络和状态 LED | 图 f6c81577b11d / 第 1 页 / 第 1 页 A1-C2 区 U1 W5500，TX/RX、SPI、XI/XO、LED、PMODE、RSTn 与电源地引脚 |
| Y1 | 25MHz | W5500 XI/CLKIN 的 25MHz 有源时钟源 | 图 f6c81577b11d / 第 1 页 / 第 1 页 C2 区 Y1 25MHz，VCC/STBY/GND/OUT、R11、R14、C10/C11 与 XI |
| T1 | Net Trans | W5500 PHY 与 RJ45 数据对之间的双通道网络变压器 | 图 f6c81577b11d / 第 1 页 / 第 1 页 A2-B4 区 T1 Net Trans，TD+/TD-/RD+/RD-、TX+/TX-/RX+/RX- 与 CT |
| P9 | RJ45 | 以太网数据与 VB1/VB2 PoE 空闲对接口 | 图 f6c81577b11d / 第 1 页 / 第 1 页 A4-B4 区 P9 RJ45 pins1-9，RX1/TX1、VB1/VB2 与屏蔽终端网络 |
| P1 | 未标注 | 接收 VA1/VA2/VB1/VB2 并输出 5V 的 PoE 模块 | 图 f6c81577b11d / 第 1 页 / 第 1 页 B2-B3 区 P1，VA1/VA2/VB1/VB2/GND/VOUT，引脚外仅标输出 5V，未标模块型号 |
| U2 | BL8075CB5TR33 | INF+ 到 D3V3 的 3.3V 稳压器 | 图 f6c81577b11d / 第 1 页 / 第 1 页 C3-D4 区 U2 BL8075CB5TR33，VIN/EN/GND/VOUT/NC 与 C23/C24 |
| D1 | SS54 | INF+ 与 P1 5V 输出之间的串联二极管 | 图 f6c81577b11d / 第 1 页 / 第 1 页 B2-B3 区 INF+-D1 SS54-P1 VOUT/5V |
| P2,P3 | Header 5 / Header 4 | Atom 主机的 3.3V、SPI、I2C、INF+ 和 GND 连接器 | 图 f6c81577b11d / 第 1 页 / 第 1 页 C3-C4 区 P3 Header4 与 P2 Header5，G21/G25/INF+/GND/+3.3V/GPIO22/19/23/33 |
| I2C | Header 4 | G21/G25 与可选 INF+ 或 +3.3V 供电的四针扩展接口 | 图 f6c81577b11d / 第 1 页 / 第 1 页 C2 区 I2C pins1-4 与 R17/R18 0Ω/NC、G21/G25/INF+/+3.3V/GND |
| R5 | 4 x 33R | W5500 TX/RX 四线到 T1 的串联电阻阵列 | 图 f6c81577b11d / 第 1 页 / 第 1 页 A2-B2 区 R5 33R 四联阵列，连接 RX_N/RX_P/TX_N/TX_P 与 T1 |
| R4 | 4 x 4.7KΩ | W5500 PMODE0/1/2 与 RSTn 到 D3V3 的上拉电阻阵列 | 图 f6c81577b11d / 第 1 页 / 第 1 页 A1 区 R4 4.7KΩ 四联阵列，上端接 D3V3，下端接 U1 PMODE0/1/2 与 RSTn |
| LED1,LED2 | GREEN / ORANGE | W5500 ACTLED 与 LINKLED 状态指示灯 | 图 f6c81577b11d / 第 1 页 / 第 1 页 B2 区 U1 ACTLED/LINKLED、LED1 GREEN、LED2 ORANGE、R20/R21 100R 到 D3V3 |
| FB1,R15 | 120Ω/MB / 0Ω | D3V3/A3V3 与 GND/AGND 的电源域连接件 | 图 f6c81577b11d / 第 1 页 / 第 1 页 D3-D4 区 D3V3-FB1-A3V3 与 GND-R15-AGND，C25 100uF |

## 系统结构

### Atomic PoE Base 系统架构

U1 W5500 经 Atom SPI 与主机通信，TX/RX 差分信号经 R5 和 T1 到 P9 RJ45；P1 从 VA1/VA2/VB1/VB2 取电并输出 5V，INF+ 通过 D1 连接该 5V 节点，U2 从 INF+ 生成 D3V3。

- 参数与网络：`ethernet_controller=U1 W5500`；`host_bus=SPI`；`clock=Y1 25MHz`；`magnetics=T1 Net Trans`；`network_connector=P9 RJ45`；`poe_module=P1 unmarked`；`poe_output=5V`；`external_input=INF+`；`logic_regulator=U2 BL8075CB5TR33`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页完整单页：U1/R5/T1/P9/P1/D1/U2/P2/P3 的信号与电源连接

## 核心器件

### U1 W5500 已连接功能

U1 的 TXN/TXP/RXN/RXP 接四组差分网络，MOSI/MISO/SCLK/SCSn 接 Atom SPI，XI/CLKIN 接外部时钟，ACTLED/LINKLED 接状态灯；INTn、DUPLED 和 SPDLED 未连接。

- 参数与网络：`phy=TXN pin1, TXP pin2, RXN pin5, RXP pin6`；`spi=MOSI pin35, MISO pin34, SCLK pin33, SCSn pin32`；`clock_input=XI/CLKIN pin30`；`clock_output=XO pin31`；`led_outputs=ACTLED pin27, LINKLED pin25`；`unconnected=INTn pin36, DUPLED pin26, SPDLED pin24`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 A1-C2 区 U1 各引脚、网络标签与 NC 标记

## 电源

### RJ45 PoE 节点到 P1 5V 输出

P9 pins4/5 同接 VB1，pins7/8 同接 VB2；T1 中心抽头形成 VA1/VA2。P1 的四个输入连接这些 VA/VB 节点，GND 接地，VOUT 网络标为 5V。

- 参数与网络：`rj45_spare_pair_1=P9 pins4/5 VB1`；`rj45_spare_pair_2=P9 pins7/8 VB2`；`data_center_taps=VA1,VA2`；`module_inputs=P1 VA1/VA2/VB1/VB2`；`module_ground=GND`；`module_output=5V`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 A3-B4 区 P9 VB1/VB2、T1 VA1/VA2 与 B2-B3 区 P1 输入/GND/VOUT

### INF+ 与 PoE 5V 电源节点

P3 pin3 输出 INF+；INF+ 一路连接 U2 VIN/EN，另一路经 D1 SS54 连接 P1 VOUT 所在的 5V 节点。

- 参数与网络：`atom_power=P3 pin3 INF+`；`logic_regulator_input=INF+ -> U2 VIN/EN`；`diode_link=INF+ -> D1 SS54 -> P1 VOUT/5V`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 B2-B3 区 D1/P1 与 C3-D3 区 P3/U2 的 INF+ 同名网络

### U2 3.3V 数字电源

U2 BL8075CB5TR33 的 VIN pin1 和 EN pin3 接 INF+，GND pin2 接地，VOUT pin5 输出 D3V3，NC pin4 未连接；C23/C24 各 10uF 位于输入与输出。

- 参数与网络：`input=INF+`；`vin=pin1`；`enable=pin3 tied to INF+`；`ground=pin2 GND`；`output=pin5 D3V3`；`unconnected=pin4 NC`；`input_capacitor=C23 10uF`；`output_capacitor=C24 10uF`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 D3 区 U2 BL8075CB5TR33、C23/C24 与 INF+/D3V3

### D3V3 与 A3V3 电源域

D3V3 经 FB1 120Ω/MB 连接 A3V3；C25 100uF 从 D3V3 接 GND，R15 0Ω 连接 GND 与 AGND。U1 数字电源使用 D3V3，模拟电源使用 A3V3，并配置 C14-C22 去耦。

- 参数与网络：`digital_rail=D3V3`；`analog_rail=A3V3`；`rail_link=FB1 120Ω/MB`；`ground_link=R15 0Ω between GND and AGND`；`bulk_capacitor=C25 100uF/6.3V`；`analog_decoupling=C14-C19 100nF, C22 10uF`；`digital_decoupling=C20 100nF, C21 10uF`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 C1-D4 区 U1 A3V3/D3V3、C14-C22 与 FB1/C25/R15

## 接口

### W5500 到 T1 网络变压器

U1 的 RX_N/RX_P/TX_N/TX_P 四线先经过 R5 四联 33Ω 串联阵列，再连接 T1 的 TD+/TD-/RD+/RD- 侧；TX 侧含 R6/R7 49.9Ω、C2/C4 682 和中心抽头 C3 103，RX 侧含 R1/R2/R3 与 C1 223 偏置网络。

- 参数与网络：`series_array=R5 4 x 33R`；`transformer=T1 Net Trans`；`primary_pairs=TD+/TD-, RD+/RD-`；`tx_termination=R6/R7 49.9R 1%, C2/C4 682, C3 103 to AGND`；`rx_termination=R1/R2/R3 and C1 223 to AGND/A3V3`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 A2-B3 区 R5、R1-R7、C1-C4 与 T1 pins1-8

### T1 到 P9 RJ45 数据对

T1 次级 TX+ pin16、TX- pin14、RX+ pin11、RX- pin9 分别形成 RX1_N、RX1_P、TX1_N、TX1_P，并连接 P9 的数据 pins6、3、2、1；中心抽头 pins15/10 分别为 VA1/VA2。

- 参数与网络：`pin16_tx_plus=RX1_N -> P9 pin6`；`pin14_tx_minus=RX1_P -> P9 pin3`；`pin11_rx_plus=TX1_N -> P9 pin2`；`pin9_rx_minus=TX1_P -> P9 pin1`；`tx_center_tap=T1 pin15 VA1`；`rx_center_tap=T1 pin10 VA2`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 A3-B4 区 T1 secondary pins9-16、RX1/TX1、VA1/VA2 与 P9 pins1/2/3/6

### P2/P3 Atom 主机接口

P3 pins1-4 依次连接 G21、G25、INF+、GND；P2 pins1-5 依次连接 +3.3V、GPIO22、GPIO19、GPIO23、GPIO33。

- 参数与网络：`P3_pin1=G21`；`P3_pin2=G25`；`P3_pin3=INF+`；`P3_pin4=GND`；`P2_pin1=+3.3V`；`P2_pin2=GPIO22`；`P2_pin3=GPIO19`；`P2_pin4=GPIO23`；`P2_pin5=GPIO33`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 C3-C4 区 P3 Header4 和 P2 Header5 的 pin1-pin5 网络标签

### 可选供电 I2C 四针接口

I2C 接口 pin4 为 G21，pin3 为 G25，pin1 为 GND；pin2 可通过 R17 0Ω/NC 接 INF+，或通过 R18 0Ω/NC 接 +3.3V，当前两电阻均标 NC。

- 参数与网络：`pin4=G21`；`pin3=G25`；`pin2_default=unpowered`；`pin2_option_1=R17 0Ω/NC to INF+`；`pin2_option_2=R18 0Ω/NC to +3.3V`；`pin1=GND`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 C2-C3 区 I2C Header4、R17/R18 与 G21/G25/INF+/+3.3V/GND

## 总线

### Atom 到 W5500 的 SPI 映射

U1 MOSI pin35 连接 GPIO33，MISO pin34 连接 GPIO23，SCLK pin33 经 R8 33Ω 连接 GPIO22，SCSn pin32 连接 GPIO19。

- 参数与网络：`MOSI=U1 pin35 -> GPIO33`；`MISO=U1 pin34 -> GPIO23`；`SCLK=U1 pin33 -> R8 33R -> GPIO22`；`SCSn=U1 pin32 -> GPIO19`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 B1-B2 区 U1 pins35-32、R8 与 GPIO33/23/22/19

## GPIO 与控制信号

### W5500 状态 LED

U1 ACTLED pin27 连接 LED1 GREEN 并经 R20 100R 到 D3V3；LINKLED pin25 连接 LED2 ORANGE 并经 R21 100R 到 D3V3；DUPLED pin26 未连接。

- 参数与网络：`activity=ACTLED pin27 -> LED1 GREEN -> R20 100R -> D3V3`；`link=LINKLED pin25 -> LED2 ORANGE -> R21 100R -> D3V3`；`duplex=DUPLED pin26 NC`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 B2 区 U1 pins27/26/25、LED1/LED2 与 R20/R21

## 时钟

### W5500 外部 25MHz 时钟

Y1 标注 25MHz，VCC pin4 接 D3V3，GND pin2 接地，STBY pin1 经 R14 100K 接 GND，OUT pin3 经 R11 33Ω 到 XI，并以 C11 15pF 接地；C10 100nF 跨接 Y1 供电。

- 参数与网络：`oscillator=Y1 25MHz`；`supply=pin4 D3V3`；`ground=pin2 GND`；`standby=pin1 R14 100K to GND`；`output=pin3 -> R11 33R -> XI`；`output_capacitor=C11 15pF to GND`；`decoupling=C10 100nF`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 C2 区 Y1/R11/R14/C10/C11 与 U1 XI 网络

## 复位

### W5500 RSTn 与 PMODE 上拉

R4 四联 4.7KΩ 阵列上端共接 D3V3，下端分别连接 U1 PMODE0 pin45、PMODE1 pin44、PMODE2 pin43 和 RSTn pin37。

- 参数与网络：`resistor_array=R4 4 x 4.7KΩ`；`common=D3V3`；`mode0=U1 pin45`；`mode1=U1 pin44`；`mode2=U1 pin43`；`reset=U1 RSTn pin37`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 A1 区 R4 与 U1 top-side PMODE0/1/2、RSTn 连线

## 保护电路

### RJ45 侧共模终端网络

RX1_N/RX1_P/TX1_N/TX1_P 四线分别经 C6/C5/C8/C7 223 100V 与 R10/R9/R13/R12 75R 汇合到 P9 屏蔽节点，该节点再经 C9 102 2kV 接 GND。

- 参数与网络：`signal_capacitors=C5-C8 223 100V`；`termination_resistors=R9/R10/R12/R13 75R`；`common_node=P9 shield`；`ground_capacitor=C9 102 2kV to GND`
- 证据：图 f6c81577b11d / 第 1 页 / 第 1 页 B3-B4 区 C5-C9、R9/R10/R12/R13 与 P9/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic PoE Base 系统架构 | `ethernet_controller=U1 W5500`；`host_bus=SPI`；`clock=Y1 25MHz`；`magnetics=T1 Net Trans`；`network_connector=P9 RJ45`；`poe_module=P1 unmarked`；`poe_output=5V`；`external_input=INF+`；`logic_regulator=U2 BL8075CB5TR33` |
| 核心器件 | U1 W5500 已连接功能 | `phy=TXN pin1, TXP pin2, RXN pin5, RXP pin6`；`spi=MOSI pin35, MISO pin34, SCLK pin33, SCSn pin32`；`clock_input=XI/CLKIN pin30`；`clock_output=XO pin31`；`led_outputs=ACTLED pin27, LINKLED pin25`；`unconnected=INTn pin36, DUPLED pin26, SPDLED pin24` |
| 总线 | Atom 到 W5500 的 SPI 映射 | `MOSI=U1 pin35 -> GPIO33`；`MISO=U1 pin34 -> GPIO23`；`SCLK=U1 pin33 -> R8 33R -> GPIO22`；`SCSn=U1 pin32 -> GPIO19` |
| 时钟 | W5500 外部 25MHz 时钟 | `oscillator=Y1 25MHz`；`supply=pin4 D3V3`；`ground=pin2 GND`；`standby=pin1 R14 100K to GND`；`output=pin3 -> R11 33R -> XI`；`output_capacitor=C11 15pF to GND`；`decoupling=C10 100nF` |
| 复位 | W5500 RSTn 与 PMODE 上拉 | `resistor_array=R4 4 x 4.7KΩ`；`common=D3V3`；`mode0=U1 pin45`；`mode1=U1 pin44`；`mode2=U1 pin43`；`reset=U1 RSTn pin37` |
| 接口 | W5500 到 T1 网络变压器 | `series_array=R5 4 x 33R`；`transformer=T1 Net Trans`；`primary_pairs=TD+/TD-, RD+/RD-`；`tx_termination=R6/R7 49.9R 1%, C2/C4 682, C3 103 to AGND`；`rx_termination=R1/R2/R3 and C1 223 to AGND/A3V3` |
| 接口 | T1 到 P9 RJ45 数据对 | `pin16_tx_plus=RX1_N -> P9 pin6`；`pin14_tx_minus=RX1_P -> P9 pin3`；`pin11_rx_plus=TX1_N -> P9 pin2`；`pin9_rx_minus=TX1_P -> P9 pin1`；`tx_center_tap=T1 pin15 VA1`；`rx_center_tap=T1 pin10 VA2` |
| 电源 | RJ45 PoE 节点到 P1 5V 输出 | `rj45_spare_pair_1=P9 pins4/5 VB1`；`rj45_spare_pair_2=P9 pins7/8 VB2`；`data_center_taps=VA1,VA2`；`module_inputs=P1 VA1/VA2/VB1/VB2`；`module_ground=GND`；`module_output=5V` |
| 电源 | INF+ 与 PoE 5V 电源节点 | `atom_power=P3 pin3 INF+`；`logic_regulator_input=INF+ -> U2 VIN/EN`；`diode_link=INF+ -> D1 SS54 -> P1 VOUT/5V` |
| 电源 | U2 3.3V 数字电源 | `input=INF+`；`vin=pin1`；`enable=pin3 tied to INF+`；`ground=pin2 GND`；`output=pin5 D3V3`；`unconnected=pin4 NC`；`input_capacitor=C23 10uF`；`output_capacitor=C24 10uF` |
| 电源 | D3V3 与 A3V3 电源域 | `digital_rail=D3V3`；`analog_rail=A3V3`；`rail_link=FB1 120Ω/MB`；`ground_link=R15 0Ω between GND and AGND`；`bulk_capacitor=C25 100uF/6.3V`；`analog_decoupling=C14-C19 100nF, C22 10uF`；`digital_decoupling=C20 100nF, C21 10uF` |
| 接口 | P2/P3 Atom 主机接口 | `P3_pin1=G21`；`P3_pin2=G25`；`P3_pin3=INF+`；`P3_pin4=GND`；`P2_pin1=+3.3V`；`P2_pin2=GPIO22`；`P2_pin3=GPIO19`；`P2_pin4=GPIO23`；`P2_pin5=GPIO33` |
| 接口 | 可选供电 I2C 四针接口 | `pin4=G21`；`pin3=G25`；`pin2_default=unpowered`；`pin2_option_1=R17 0Ω/NC to INF+`；`pin2_option_2=R18 0Ω/NC to +3.3V`；`pin1=GND` |
| GPIO 与控制信号 | W5500 状态 LED | `activity=ACTLED pin27 -> LED1 GREEN -> R20 100R -> D3V3`；`link=LINKLED pin25 -> LED2 ORANGE -> R21 100R -> D3V3`；`duplex=DUPLED pin26 NC` |
| 保护电路 | RJ45 侧共模终端网络 | `signal_capacitors=C5-C8 223 100V`；`termination_resistors=R9/R10/R12/R13 75R`；`common_node=P9 shield`；`ground_capacitor=C9 102 2kV to GND` |
| 核心器件 | 正文中的 W5500 网络能力 | `documented_protocols=TCP,UDP,ICMP,IPv4,ARP,IGMP,PPPoE`；`documented_sockets=8`；`documented_link=10BaseT/100Base-T`；`schematic_part=U1 W5500` |
| 电源 | 正文中的 IEEE 802.3af PoE 规格 | `documented_standard=IEEE 802.3af`；`documented_method=spare-pair power for 10M/100M Ethernet`；`schematic_module=P1 unmarked`；`schematic_inputs=VA1,VA2,VB1,VB2`；`schematic_output=5V` |

## 待确认事项

- `component.documented-w5500-capabilities`：正文称 W5500 集成 TCP/UDP/ICMP/IPv4/ARP/IGMP/PPPoE、8 路硬件 socket 和 10/100M MAC/PHY；当前原理图只确认器件型号及电气连接，不能单独证明这些数据手册能力。（证据：图 f6c81577b11d / 第 1 页 / 第 1 页 U1 仅标 W5500 与引脚连接，图中无协议、socket 数量或速率文字）
- `power.documented-poe-compliance`：正文声明支持 IEEE 802.3af，并描述空闲引脚供电；原理图显示 VA1/VA2、VB1/VB2 到 P1 及 5V 输出，但 P1 未标型号或标准，无法仅由该页确认 IEEE 802.3af 合规性和完整输入范围。（证据：图 f6c81577b11d / 第 1 页 / 第 1 页 T1/P9/P1 区显示 VA/VB 与 5V 连接，但 P1 没有 part number、IEEE 标记或输入电压范围）
- `review.w5500-datasheet-capabilities`：当前 W5500 datasheet 版本是否确认正文所列协议、8 路硬件 socket 和 10/100M 能力？；原因：这些是芯片数据手册能力，不是原理图连线能够证明的事实；发布前应绑定官方 datasheet 版本。
- `review.poe-module-and-standard`：P1 的量产型号、输入范围和认证资料是否确认 Atomic PoE Base 符合 IEEE 802.3af？；原因：原理图 P1 未标 part number，只能确认 VA/VB 输入与 5V 输出，无法追溯 PoE 标准合规和功率范围。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f6c81577b11df0af044685af7d53a82e4fa60befc17a830862e93c0c8e163f1c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/465/Sch_AtomicPoE_v1.2_sch_01.png` |

---

源文档：`zh_CN/atom/Atomic PoE Base.md`

源文档 SHA-256：`c31b018687565f2aef5ef0fb762291f04c1f0b91fb3ebc49ba22f94fef636085`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
