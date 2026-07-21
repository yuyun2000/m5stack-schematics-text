# Module GSM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module GSM |
| SKU | M026 |
| 产品 ID | `module-gsm-0ac1e8c6b626` |
| 源文档 | `zh_CN/module/gsm.md` |

## 概述

Module GSM 以 U2 M6315 为 GSM 通信核心，通过 U5 TXS0104E 将 2.8 V 域的主 UART 和调试 UART 转换到 3.3 V 域，并由 0 Ω 路由位置连接 J1 M5Stack_BUS。模块从 J1 的 +5 V 经 U6 JW5033H 降压产生 +4 V/VBAT，同时利用 M6315 的 VDD_EXT 生成 +2.8 V；SIM、射频天线、麦克风、扬声器、状态灯、电源键和复位电路均在同页给出。SIM 信号带 SMF05CT1G 阵列、22 Ω 串联电阻和 22 pF 滤波，射频端同时画有 E1 Antenna 与 E2 ANT_IPEX 两条 0 Ω 支路。

## 检索关键词

`Module GSM`、`M026`、`M6315`、`JW5033H`、`TXS0104E`、`SMF05CT1G`、`M5Stack_BUS`、`GSM`、`GPRS`、`UART`、`URXD`、`UTXD`、`DBG_RXD`、`DBG_TXD`、`GPIO16`、`GPIO17`、`GPIO2`、`GPIO26`、`GPIO25`、`S_PWR`、`S_RST`、`PWR_KEY`、`RST`、`NETLight`、`RF_STA`、`SIM_VCC`、`SIM_RST`、`SIM_CLK`、`SIM_DATA`、`RF_ANT`、`ANT_IPEX`、`MIC_P`、`MIC_N`、`SPK2P`、`VBAT`、`+4V`、`+2.8V`、`+3.3V`、`+5V`、`Nano SIM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | M6315 | GSM 通信模组，提供主/辅助/调试串口、SIM、射频、音频、状态与电源控制接口 | 图 f4360d1b6539 / 第 1 页 / B2-C3 中央 U2 M6315 pins1-44 |
| U5 | TXS0104E | M6315 2.8 V UART/调试信号与 M5-Bus 3.3 V 信号之间的四通道电平转换器 | 图 f4360d1b6539 / 第 1 页 / C2-C3 U5 TXS0104E、C22/C23 |
| U6 | JW5033H | 从 +5 V 产生 +4 V/VBAT 的开关降压转换器 | 图 f4360d1b6539 / 第 1 页 / D1-D2 U6 JW5033H、L1、R24-R26、C24-C29 |
| U3 | SMF05CT1G | SIM_VCC、SIM_RST、SIM_CLK、SIM_DATA 接口的多通道保护阵列 | 图 f4360d1b6539 / 第 1 页 / B1 U3 SMF05CT1G pins1-6 |
| U4 | 未标注 | SIM 卡连接器，连接 SIM_VCC、SIM_RST、SIM_CLK、SIM_DATA 与 SIM_GND | 图 f4360d1b6539 / 第 1 页 / B1 U4 SIM connector pins1-7 |
| J1 | M5Stack_BUS | 30 针主机接口，承载 +5 V、+3.3 V、GND、UART、开机、复位与扬声器信号 | 图 f4360d1b6539 / 第 1 页 / C4 J1 M5Stack_BUS pins1-30 |
| E1/E2 | Antenna / ANT_IPEX | M6315 RF_ANT 的天线与 IPEX 天线接口支路 | 图 f4360d1b6539 / 第 1 页 / A3-B3 U2 RF_ANT pin35、R9/R10、E1 Antenna、E2 ANT_IPEX |
| U11 | MIC | 连接 M6315 MIC_P/MIC_N 差分输入的板载麦克风 | 图 f4360d1b6539 / 第 1 页 / A4 U11 MIC、MIC_P/MIC_N、C2-C13 |
| S1/Q4 | SW-PB / SS8050 Y1 | 3.3 V 按键和 NPN 反相器组成的 M6315 PWRKEY 低电平驱动 | 图 f4360d1b6539 / 第 1 页 / B1-C1 Q4/R14/R15/PWR_KEY 与 C4 S1/S_PWR |
| Q3 | SS8050 Y1 | S_RST 控制的复位下拉驱动器 | 图 f4360d1b6539 / 第 1 页 / A3 Q3/R5/R8/C1、S_RST/RST |
| Q1/D1 | SS8050 Y1 / 蓝灯 0603 | NETLight 控制的蓝色网络状态指示灯驱动 | 图 f4360d1b6539 / 第 1 页 / A1 Q1/D1/R1/R3/R6、NETLight |
| Q2/D2 | SS8050 Y1 / 绿灯 0603 | RF_STA 控制的绿色射频状态指示灯驱动 | 图 f4360d1b6539 / 第 1 页 / A2 Q2/D2/R2/R4/R7、RF_STA |
| R11-R13/C17-C19 | 22Ω / 22pF | SIM_RST、SIM_CLK、SIM_DATA 的串联阻尼和对地滤波网络 | 图 f4360d1b6539 / 第 1 页 / B1-C1 U4 至 U2 SIM 信号，R11-R13/C17-C19 |
| R16/R19-R23/R17/R18 | 0Ω | UART、SPK2P 与 S_RST 到 M5-Bus GPIO 的配置连接位置 | 图 f4360d1b6539 / 第 1 页 / C3-C4 R16-R23 与 J1 |

## 系统结构

### Module GSM 系统架构

U2 M6315 集成 GSM、SIM、RF 和音频功能；U6 从 M5-Bus +5 V 产生 VBAT，U5 完成 2.8 V/3.3 V 串口电平转换，J1 提供主机侧电源与控制信号。

- 参数与网络：`radio=U2 M6315`；`power=J1 +5V -> U6 JW5033H -> +4V/VBAT`；`level_shifter=U5 TXS0104E`；`host=J1 M5Stack_BUS`；`interfaces=UART, SIM, RF, microphone, speaker, power key, reset`
- 证据：图 f4360d1b6539 / 第 1 页 / 整页 U2/U5/U6/J1 及 SIM、RF、音频分区

## 核心器件

### M6315 主要引脚分组

U2 页面显示 DBG_TXD pin39、DBG_RXD pin38、RXD pin17、TXD pin18、SIM_GND/DATA/RST/CLK/VDD pins10-14、PWRKEY pin7、VDD_EXT pin24、RF_ANT pin35、NETLIGHT pin16、RFTXMON pin25、VBAT pins42/43 与音频 pins2-6。

- 参数与网络：`debug=DBG_TXD 39; DBG_RXD 38`；`uart=RXD 17; TXD 18`；`sim=SIM_GND 10; SIM_DATA 11; SIM_RST 12; SIM_CLK 13; SIM_VDD 14`；`power_control=PWRKEY 7; VDD_EXT 24`；`rf_status=RF_ANT 35; NETLIGHT 16; RFTXMON 25`；`vbat=pins42/43`；`audio=SPK2_P 2; MIC_P 3; MIC_N 4; SPK1_P 5; SPK1_N 6`
- 证据：图 f4360d1b6539 / 第 1 页 / B2-C3 U2 M6315 pin labels

## 电源

### +5 V 至 +4 V 降压路径

J1 pin28 的 +5 V 进入 U6 JW5033H VIN；U6 SW 经 L1 4.7 uH 输出 +4 V/VBAT，反馈网络为 R25 82 kΩ 与 R26 20 kΩ，输入和输出均配置去耦电容。

- 参数与网络：`input=+5V from J1 pin28`；`converter=U6 JW5033H`；`inductor=L1 4.7uH`；`output=+4V / VBAT`；`feedback=R25 82KΩ; R26 20KΩ`；`input_caps=C25 10uF; C26 10uF`；`output_caps=C27 22uF; C28 22uF; C29 100nF`；`bootstrap=C24 100nF`
- 证据：图 f4360d1b6539 / 第 1 页 / D1-D2 +5V/U6/L1/+4V/VBAT

### VBAT 供电分配

+4 V 与 VBAT 为同一输出节点，VBAT 连接 U2 pins42/43，并由 C31 100 uF、C32 100 nF、C33 33 pF、C34 10 pF 对地去耦；同一轨还供给状态灯支路。

- 参数与网络：`rail=VBAT`；`source=+4V`；`load=U2 pins42/43`；`bulk=C31 100uF`；`decoupling=C32 100nF; C33 33pF; C34 10pF`；`other_loads=D1/D2 indicator branches`
- 证据：图 f4360d1b6539 / 第 1 页 / B3 U2 VBAT pins42/43；D3 C31-C34；A1-A2 D1/D2 VBAT

### M6315 +2.8 V 输出

U2 VDD_EXT pin24 形成 +2.8 V 网络，经 C20 4.7 uF 与 C21 100 nF 去耦，并供给 U5 VCCA 与 OE；U5 VCCB 由 +3.3 V 供电。

- 参数与网络：`source=U2 VDD_EXT pin24`；`rail=+2.8V`；`decoupling=C20 4.7uF; C21 100nF`；`loads=U5 VCCA pin1; U5 OE pin8`；`b_side=+3.3V to U5 VCCB pin14`；`u5_caps=C22 100nF on +2.8V; C23 100nF on +3.3V`
- 证据：图 f4360d1b6539 / 第 1 页 / C2 U2 VDD_EXT/+2.8V/C20/C21；C2-C3 U5/C22/C23

## 接口

### SIM 卡接口网络

U4 pin1 接 SIM_VCC、pin2 经 R11 22 Ω 接 SIM_RST、pin3 经 R12 22 Ω 接 SIM_CLK、pin7 经 R13 22 Ω 接 SIM_DATA，pin5 接 SIM_GND；U2 侧对应 SIM_VDD/RST/CLK/DATA/GND pins14/12/13/11/10。

- 参数与网络：`connector=U4`；`vcc=U4 pin1 SIM_VCC -> U2 SIM_VDD pin14`；`reset=U4 pin2 -> R11 22Ω -> SIM_RST -> U2 pin12`；`clock=U4 pin3 -> R12 22Ω -> SIM_CLK -> U2 pin13`；`data=U4 pin7 -> R13 22Ω -> SIM_DATA -> U2 pin11`；`ground=U4 pin5 SIM_GND -> U2 pin10`；`vpp=U4 pin6 not connected`
- 证据：图 f4360d1b6539 / 第 1 页 / B1 U4/R11-R13；B2-C2 U2 SIM pins10-14

### 蓝色 NETLight 指示灯

U2 NETLIGHT pin16 的 NETLight 经 R3 1 kΩ 驱动 Q1，R6 10 kΩ 下拉；Q1 控制由 VBAT、R1 1 kΩ 与 D1 蓝灯 0603 组成的指示支路。

- 参数与网络：`source=U2 NETLIGHT pin16`；`base_resistor=R3 1KΩ`；`pulldown=R6 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 蓝灯 0603`；`led_resistor=R1 1KΩ`；`supply=VBAT`
- 证据：图 f4360d1b6539 / 第 1 页 / A1 NETLight/R3/R6/Q1/R1/D1/VBAT；B3 U2 NETLIGHT pin16

### 绿色 RF_STA 指示灯

U2 RFTXMON pin25 的 RF_STA 经 R4 1 kΩ 驱动 Q2，R7 10 kΩ 下拉；Q2 控制由 VBAT、R2 1 kΩ 与 D2 绿灯 0603 组成的指示支路。

- 参数与网络：`source=U2 RFTXMON pin25`；`net=RF_STA`；`base_resistor=R4 1KΩ`；`pulldown=R7 10KΩ`；`transistor=Q2 SS8050 Y1`；`led=D2 绿灯 0603`；`led_resistor=R2 1KΩ`；`supply=VBAT`
- 证据：图 f4360d1b6539 / 第 1 页 / A2 RF_STA/R4/R7/Q2/R2/D2/VBAT；A3 U2 RFTXMON pin25

### M5Stack_BUS 使用的针脚

J1 页面使用 pins1/3/5 GND、pin8 GPIO25/SPK2P、pin10 GPIO26/S_RST、pin12 +3.3 V、pins15/16 GPIO16/GPIO17、pin19 GPIO2/S_PWR、pins20/21/22/23 GPIO5/GPIO12/GPIO13/GPIO15 作为 UART 备选，以及 pin28 +5 V。

- 参数与网络：`ground=pins1/3/5`；`speaker=pin8 GPIO25 via R17 SPK2P`；`reset=pin10 GPIO26 via R18 S_RST`；`3v3=pin12`；`uart_primary_positions=pin15 GPIO16; pin16 GPIO17`；`power_key=pin19 GPIO2 S_PWR`；`uart_alternative_positions=pin20 GPIO5; pin21 GPIO12; pin22 GPIO13; pin23 GPIO15`；`5v=pin28`
- 证据：图 f4360d1b6539 / 第 1 页 / C4 J1 M5Stack_BUS pins1-30 与外部网络标签

## 总线

### 主 UART 电平转换

U2 TXD pin18 的 UTXD 接 U5 A1，并由 B1 输出 U1_T；U2 RXD pin17 的 URXD 接 U5 A2，并由 B2 接 U1_R，完成 2.8 V 与 3.3 V 域转换。

- 参数与网络：`module_tx=U2 TXD pin18 / UTXD -> U5 A1 -> B1 / U1_T`；`module_rx=U2 RXD pin17 / URXD -> U5 A2 -> B2 / U1_R`；`module_level=+2.8V`；`host_level=+3.3V`；`direction=UTXD module-to-host; URXD host-to-module`
- 证据：图 f4360d1b6539 / 第 1 页 / B2 U2 RXD/TXD；C2-C3 U5 A1/A2/B1/B2

## GPIO 与控制信号

### UART 到 M5-Bus 的 0 Ω 路由

U1_T 可经 R16/R19/R20 分别连接 GPIO16/J1 pin15、GPIO12/J1 pin21、GPIO15/J1 pin23；U1_R 可经 R21/R22/R23 分别连接 GPIO17/J1 pin16、GPIO5/J1 pin20、GPIO13/J1 pin22。

- 参数与网络：`tx_options=R16 0Ω -> GPIO16 pin15; R19 0Ω -> GPIO12 pin21; R20 0Ω -> GPIO15 pin23`；`rx_options=R21 0Ω -> GPIO17 pin16; R22 0Ω -> GPIO5 pin20; R23 0Ω -> GPIO13 pin22`；`selection=resistor population`
- 证据：图 f4360d1b6539 / 第 1 页 / C3-C4 U1_T/U1_R、R16/R19-R23、J1

### M6315 开关机控制

S_PWR 可由 S1 将 +3.3 V 接入，也直接连接 J1 pin19/GPIO2；S_PWR 经 R14 1 kΩ 驱动 Q4，Q4 将 U2 PWRKEY pin7 下拉，R15 10 kΩ 将 S_PWR 默认下拉。

- 参数与网络：`host=J1 pin19 GPIO2`；`button=S1 SW-PB to +3.3V`；`control_net=S_PWR`；`base_resistor=R14 1KΩ`；`pulldown=R15 10KΩ`；`transistor=Q4 SS8050 Y1`；`target=U2 PWRKEY pin7`；`polarity=S_PWR high -> PWR_KEY low`
- 证据：图 f4360d1b6539 / 第 1 页 / B1-C1 S_PWR/R14/R15/Q4/PWR_KEY；C4 S1；J1 pin19

## 复位

### 主机复位控制

J1 pin10/GPIO26 经 R18 0 Ω 连接 S_RST；S_RST 经 R5 1 kΩ 驱动 Q3，Q3 将 RST 下拉，R8 10 kΩ 为 S_RST 下拉，RST 配置 C1 100 nF 对地。

- 参数与网络：`host=J1 pin10 GPIO26`；`route=R18 0Ω`；`control=S_RST`；`base_resistor=R5 1KΩ`；`pulldown=R8 10KΩ`；`transistor=Q3 SS8050 Y1`；`target=RST`；`capacitor=C1 100nF`；`polarity=S_RST high -> RST low`
- 证据：图 f4360d1b6539 / 第 1 页 / A3 Q3/R5/R8/C1/RST；C4 R18/J1 pin10

## 保护电路

### SIM 接口保护与滤波

U3 SMF05CT1G 位于 SIM_VCC、SIM_RST、SIM_CLK、SIM_DATA 与 GND 之间；SIM_VCC 配置 C14 1 uF 和 C15 100 nF，三个信号分别配置 C17/C18/C19 22 pF 对地。

- 参数与网络：`protector=U3 SMF05CT1G`；`protected_nets=SIM_VCC, SIM_RST, SIM_CLK, SIM_DATA`；`supply_caps=C14 1uF; C15 100nF`；`signal_caps=C17/C18/C19 22pF`；`series_resistors=R11/R12/R13 22Ω`
- 证据：图 f4360d1b6539 / 第 1 页 / B1-C1 U3/C14/C15/R11-R13/C17-C19

## 音频

### 板载差分麦克风

U2 MIC_P pin3 与 MIC_N pin4 接 U11 MIC；MIC_P、MIC_N 分别有 10 pF/33 pF 对地电容，两线之间另有 10 pF/33 pF 跨线电容，并各经过串联滤波元件。

- 参数与网络：`positive=U2 pin3 MIC_P`；`negative=U2 pin4 MIC_N`；`microphone=U11 MIC`；`mic_p_to_ground=C2/C4 10pF; C3/C5 33pF`；`between_mic_p_mic_n=C6/C8 10pF; C7/C9 33pF`；`mic_n_to_ground=C10/C12 10pF; C11/C13 33pF`；`topology=symmetric differential filtering with series elements`
- 证据：图 f4360d1b6539 / 第 1 页 / A4 U11 MIC、MIC_P/MIC_N、C2-C13；B3 U2 pins3/4

### SPK2 输出到 M5-Bus

U2 SPK2_P pin2 经 C16 22 uF 串联形成 SPK2P，随后经 R17 0 Ω 接 J1 pin8/GPIO25。

- 参数与网络：`source=U2 SPK2_P pin2`；`coupling=C16 22uF`；`net=SPK2P`；`route=R17 0Ω`；`connector=J1 pin8 GPIO25`；`direction=output from M6315`
- 证据：图 f4360d1b6539 / 第 1 页 / B3 U2 SPK2_P/C16/SPK2P；C4 R17/J1 pin8

## 射频

### M6315 天线网络

U2 RF_ANT pin35 分成两路：经 R9 0 Ω 到 E1 Antenna，经 R10 0 Ω 到 E2 ANT_IPEX；E2 的另一端接 GND。

- 参数与网络：`source=U2 RF_ANT pin35`；`branch_1=R9 0Ω -> E1 Antenna`；`branch_2=R10 0Ω -> E2 ANT_IPEX`；`shield=E2 to GND`
- 证据：图 f4360d1b6539 / 第 1 页 / A3-B3 U2 RF_ANT/R9/R10/E1/E2

## 调试与烧录

### 调试 UART 电平转换

U2 DBG_RXD pin38 接 U5 A3 并转换为 DBG_R，U2 DBG_TXD pin39 接 U5 A4 并转换为 DBG_T；页面未把 DBG_R/DBG_T 继续连接到 J1。

- 参数与网络：`debug_rx=U2 DBG_RXD pin38 -> U5 A3 -> B3 DBG_R`；`debug_tx=U2 DBG_TXD pin39 -> U5 A4 -> B4 DBG_T`；`host_connector=not connected on this page`
- 证据：图 f4360d1b6539 / 第 1 页 / B2 DBG_TXD/DBG_RXD；C2-C3 U5 A3/A4/B3/B4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module GSM 系统架构 | `radio=U2 M6315`；`power=J1 +5V -> U6 JW5033H -> +4V/VBAT`；`level_shifter=U5 TXS0104E`；`host=J1 M5Stack_BUS`；`interfaces=UART, SIM, RF, microphone, speaker, power key, reset` |
| 核心器件 | M6315 主要引脚分组 | `debug=DBG_TXD 39; DBG_RXD 38`；`uart=RXD 17; TXD 18`；`sim=SIM_GND 10; SIM_DATA 11; SIM_RST 12; SIM_CLK 13; SIM_VDD 14`；`power_control=PWRKEY 7; VDD_EXT 24`；`rf_status=RF_ANT 35; NETLIGHT 16; RFTXMON 25`；`vbat=pins42/43`；`audio=SPK2_P 2; MIC_P 3; MIC_N 4; SPK1_P 5; SPK1_N 6` |
| 电源 | +5 V 至 +4 V 降压路径 | `input=+5V from J1 pin28`；`converter=U6 JW5033H`；`inductor=L1 4.7uH`；`output=+4V / VBAT`；`feedback=R25 82KΩ; R26 20KΩ`；`input_caps=C25 10uF; C26 10uF`；`output_caps=C27 22uF; C28 22uF; C29 100nF`；`bootstrap=C24 100nF` |
| 电源 | VBAT 供电分配 | `rail=VBAT`；`source=+4V`；`load=U2 pins42/43`；`bulk=C31 100uF`；`decoupling=C32 100nF; C33 33pF; C34 10pF`；`other_loads=D1/D2 indicator branches` |
| 电源 | M6315 +2.8 V 输出 | `source=U2 VDD_EXT pin24`；`rail=+2.8V`；`decoupling=C20 4.7uF; C21 100nF`；`loads=U5 VCCA pin1; U5 OE pin8`；`b_side=+3.3V to U5 VCCB pin14`；`u5_caps=C22 100nF on +2.8V; C23 100nF on +3.3V` |
| 总线 | 主 UART 电平转换 | `module_tx=U2 TXD pin18 / UTXD -> U5 A1 -> B1 / U1_T`；`module_rx=U2 RXD pin17 / URXD -> U5 A2 -> B2 / U1_R`；`module_level=+2.8V`；`host_level=+3.3V`；`direction=UTXD module-to-host; URXD host-to-module` |
| 调试与烧录 | 调试 UART 电平转换 | `debug_rx=U2 DBG_RXD pin38 -> U5 A3 -> B3 DBG_R`；`debug_tx=U2 DBG_TXD pin39 -> U5 A4 -> B4 DBG_T`；`host_connector=not connected on this page` |
| GPIO 与控制信号 | UART 到 M5-Bus 的 0 Ω 路由 | `tx_options=R16 0Ω -> GPIO16 pin15; R19 0Ω -> GPIO12 pin21; R20 0Ω -> GPIO15 pin23`；`rx_options=R21 0Ω -> GPIO17 pin16; R22 0Ω -> GPIO5 pin20; R23 0Ω -> GPIO13 pin22`；`selection=resistor population` |
| 接口 | SIM 卡接口网络 | `connector=U4`；`vcc=U4 pin1 SIM_VCC -> U2 SIM_VDD pin14`；`reset=U4 pin2 -> R11 22Ω -> SIM_RST -> U2 pin12`；`clock=U4 pin3 -> R12 22Ω -> SIM_CLK -> U2 pin13`；`data=U4 pin7 -> R13 22Ω -> SIM_DATA -> U2 pin11`；`ground=U4 pin5 SIM_GND -> U2 pin10`；`vpp=U4 pin6 not connected` |
| 保护电路 | SIM 接口保护与滤波 | `protector=U3 SMF05CT1G`；`protected_nets=SIM_VCC, SIM_RST, SIM_CLK, SIM_DATA`；`supply_caps=C14 1uF; C15 100nF`；`signal_caps=C17/C18/C19 22pF`；`series_resistors=R11/R12/R13 22Ω` |
| 射频 | M6315 天线网络 | `source=U2 RF_ANT pin35`；`branch_1=R9 0Ω -> E1 Antenna`；`branch_2=R10 0Ω -> E2 ANT_IPEX`；`shield=E2 to GND` |
| 音频 | 板载差分麦克风 | `positive=U2 pin3 MIC_P`；`negative=U2 pin4 MIC_N`；`microphone=U11 MIC`；`mic_p_to_ground=C2/C4 10pF; C3/C5 33pF`；`between_mic_p_mic_n=C6/C8 10pF; C7/C9 33pF`；`mic_n_to_ground=C10/C12 10pF; C11/C13 33pF`；`topology=symmetric differential filtering with series elements` |
| 音频 | SPK2 输出到 M5-Bus | `source=U2 SPK2_P pin2`；`coupling=C16 22uF`；`net=SPK2P`；`route=R17 0Ω`；`connector=J1 pin8 GPIO25`；`direction=output from M6315` |
| GPIO 与控制信号 | M6315 开关机控制 | `host=J1 pin19 GPIO2`；`button=S1 SW-PB to +3.3V`；`control_net=S_PWR`；`base_resistor=R14 1KΩ`；`pulldown=R15 10KΩ`；`transistor=Q4 SS8050 Y1`；`target=U2 PWRKEY pin7`；`polarity=S_PWR high -> PWR_KEY low` |
| 复位 | 主机复位控制 | `host=J1 pin10 GPIO26`；`route=R18 0Ω`；`control=S_RST`；`base_resistor=R5 1KΩ`；`pulldown=R8 10KΩ`；`transistor=Q3 SS8050 Y1`；`target=RST`；`capacitor=C1 100nF`；`polarity=S_RST high -> RST low` |
| 接口 | 蓝色 NETLight 指示灯 | `source=U2 NETLIGHT pin16`；`base_resistor=R3 1KΩ`；`pulldown=R6 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 蓝灯 0603`；`led_resistor=R1 1KΩ`；`supply=VBAT` |
| 接口 | 绿色 RF_STA 指示灯 | `source=U2 RFTXMON pin25`；`net=RF_STA`；`base_resistor=R4 1KΩ`；`pulldown=R7 10KΩ`；`transistor=Q2 SS8050 Y1`；`led=D2 绿灯 0603`；`led_resistor=R2 1KΩ`；`supply=VBAT` |
| 接口 | M5Stack_BUS 使用的针脚 | `ground=pins1/3/5`；`speaker=pin8 GPIO25 via R17 SPK2P`；`reset=pin10 GPIO26 via R18 S_RST`；`3v3=pin12`；`uart_primary_positions=pin15 GPIO16; pin16 GPIO17`；`power_key=pin19 GPIO2 S_PWR`；`uart_alternative_positions=pin20 GPIO5; pin21 GPIO12; pin22 GPIO13; pin23 GPIO15`；`5v=pin28` |
| GPIO 与控制信号 | 实际装配的 UART GPIO 路由 | `document_claim=UART2 GPIO16/GPIO17`；`schematic_positions=R16/R19/R20 and R21/R22/R23 all marked 0Ω`；`population=not marked` |
| 射频 | 天线支路实际装配选择 | `branch_1=R9 0Ω / E1 Antenna`；`branch_2=R10 0Ω / E2 ANT_IPEX`；`population=not specified` |
| 接口 | SIM 卡外形规格 | `document_claim=Nano SIM`；`schematic_reference=U4`；`connector_part_number=null` |
| 射频 | GSM/GPRS 频段与协议能力 | `document_bands=850/900/1800/1900MHz`；`document_gprs=Class12`；`document_protocols=SMS PDU/TEXT; IPv4/IPv6; TCP/UDP/PPP/HTTP/FTP/MQTT`；`schematic_marking=M6315` |

## 待确认事项

- `gpio.uart-installed-route`：产品正文称串口使用 UART2 GPIO16/GPIO17，但原理图同时给出六个均标 0 Ω 的路由位置，未用 DNP/装配标记明确实际装配组合。（证据：图 f4360d1b6539 / 第 1 页 / C3-C4 UART routing R16/R19-R23 lacks DNP marks）
- `rf.antenna-population`：原理图同时把 R9 与 R10 标为 0 Ω 并连接 E1 Antenna 与 E2 ANT_IPEX，未提供 BOM/DNP 信息确认成品实际装配或选择方式。（证据：图 f4360d1b6539 / 第 1 页 / A3-B3 RF_ANT/R9/R10/E1/E2 lacks DNP marks）
- `interface.sim-form-factor`：产品正文称 SIM 类型为 Nano，但原理图 U4 只画出 SIM 接口符号，未标连接器型号或 Nano 外形。（证据：图 f4360d1b6539 / 第 1 页 / B1 U4 connector symbol without part number/form factor）
- `rf.radio-capabilities`：产品正文列出 850/900/1800/1900 MHz、GPRS Class 12、SMS 与多种网络协议，但原理图仅标 U2 M6315，未印出这些射频和协议参数。（证据：图 f4360d1b6539 / 第 1 页 / B2-C3 U2 M6315 block lacks RF/protocol performance table）
- `review.uart-installed-route`：请用 BOM、贴装图或实板通断确认 R16/R21 是否为默认 UART2 装配，并确认其余 UART 路由电阻是否 DNP。；原因：原理图未标各 0 Ω 路由位置的装配状态。
- `review.antenna-population`：请用 BOM、PCB 或实板确认 E1 与 E2 天线支路的实际装配和选择方式。；原因：R9/R10 均标 0 Ω，页面没有 DNP 或互斥装配说明。
- `review.sim-form-factor`：请用 U4 BOM 型号或装配资料确认 SIM 卡座确为 Nano SIM。；原因：原理图符号未给出卡座型号和机械规格。
- `review.radio-capabilities`：请用该板实际 M6315 变体的数据手册或模组标签复核频段、GPRS 等级和协议支持。；原因：这些能力来自产品正文，未印在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f4360d1b653956aebcbc679e8bdcb5c42d4c45d27c475e4ad4f81192c2e83f6d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/954/M026-module_gsm_sch_page_01.png` |

---

源文档：`zh_CN/module/gsm.md`

源文档 SHA-256：`4f401a70756ab421e5d8a1a3c9f5435ae60ec2bfd805edffbb65277eace5f396`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
