# IoT Base NBIoT-CN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | IoT Base NBIoT-CN |
| SKU | K064 |
| 产品 ID | `iot-base-nbiot-cn-fbca1fe6128f` |
| 源文档 | `zh_CN/base/iot_base_nb_cn.md` |

## 概述

IoT Base NBIoT-CN 以 U1 SIM7020C 为蜂窝通信核心，CORE G0/G35 经 Q2/Q4 S8050 电平转换连接模组 UART1，CORE G12 经 Q3 控制 PWRKEY，ANT pin32 接 ANT1 IPEX。VIN_P240 经 FU2、U3 SY8205FCC 和 U4 SY8089AAAC 依次形成 CORE_P050 与 NB_P033，另有 J5/J6 经 FU1、D1 接入 CORE_BAT 的独立电池路径。U2 组成带自动方向控制、偏置、DNP 终端位和三只 TVS 的 RS485 通道；J1/J2/J3 引出三组 Grove 网络，J4/J7 提供直流与 RS485/电源输入，J8 连接 SIM 卡。U2 完整料号、无线固件能力、电源轨负载能力、电池边界和 SIM 卡座机械规格未由本页确认。

## 检索关键词

`IoT Base NBIoT-CN`、`K064`、`SIM7020C`、`NB-IoT`、`SY8205FCC`、`SY8089AAAC`、`VIN_P240`、`CORE_P050`、`NB_P033`、`NB_P018`、`CORE_BAT`、`CORE_TXD`、`CORE_RXD`、`NB_TXD`、`NB_RXD`、`MOD_PWR`、`NB_KEY`、`NB_STAT`、`RS_TXD`、`RS_RXD`、`RS_A`、`RS_B`、`S8050`、`P6S05C-LF`、`M5_BUS`、`G0`、`G35`、`G12`、`G15`、`G13`、`G21`、`G22`、`G36`、`G26`、`G17`、`G16`、`MicroSIM`、`IPEX`、`RS485`、`Grove`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SIM7020C | NB-IoT 通信模组，连接 UART、电源控制、状态 LED、IPEX 天线和 SIM 卡座 | 图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 SIM7020C，UART1、PWRKEY、STATUS、ANT、VBAT/VDD_EXT、SIM 与 GND 引脚 |
| U2 | 未标注 | NB_P033 供电的 RS485 收发器，连接 RS_TXD/RS_RXD、自动方向网络和 RS_A/RS_B | 图 b50bad176689 / 第 1 页 / 第 1 页中央 U2，RO/RE/DE/DI/A/B/VCC/GND 八脚与 Q1、偏置和保护网络 |
| U3 | SY8205FCC | 将 VIN_P240 降压为 CORE_P050 的第一级开关稳压器 | 图 b50bad176689 / 第 1 页 / 第 1 页右上 U3 SY8205FCC，VIN/EN/BS/LX/FB/SS、FU2、L1 与 CORE_P050 |
| U4 | SY8089AAAC | 将 CORE_P050 降压为 NB_P033 的第二级开关稳压器 | 图 b50bad176689 / 第 1 页 / 第 1 页右上 U4 SY8089AAAC，IN/EN/SW/FB/GND、L2 10uH 与 NB_P033 |
| Q1,Q2,Q3,Q4 | S8050 | 分别完成 RS485 自动方向控制、CORE/NB UART 电平转换和 SIM7020C PWRKEY 下拉控制 | 图 b50bad176689 / 第 1 页 / 第 1 页中央 Q1/Q2/Q3/Q4 S8050，位于 U2、UART 电平转换和 NB_KEY 网络 |
| BUS1 | M5_BUS | 连接主机 GPIO、UART、RS485、模组电源控制、5V 和电池网络 | 图 b50bad176689 / 第 1 页 / 第 1 页左上 BUS1 M5_BUS，pin1-pin30 与外部网络 |
| J1,J2,J3 | GROVE 4P | 三组 CORE_P050 供电的 Grove 接口，分别引出 G21/G22、G36/G26 和 G17/G16 | 图 b50bad176689 / 第 1 页 / 第 1 页左侧 J1/J2/J3 GROVE，IO2/IO1/5V/GND 与 G22/G21、G36/G26、G16/G17 |
| J4 | DC5.5 | VIN_P240 直流输入接口 | 图 b50bad176689 / 第 1 页 / 第 1 页左下 J4 DC5.5，PWR+ 接 VIN_P240、PWR- 接 GND |
| J5,J6 | MX1.25_2P / HT3.96_2P | BAT_IN 与 GND 电池输入接口 | 图 b50bad176689 / 第 1 页 / 第 1 页左下 J5 MX1.25_2P 和 J6 HT3.96_2P，与 BAT_IN/GND、FU1/D1/CORE_BAT |
| J7 | HT3.96_4P | 引出 RS_B、RS_A、VIN_P240 和 GND 的 RS485/电源接口 | 图 b50bad176689 / 第 1 页 / 第 1 页左下 J7 HT3.96_4P，pin4 RS_B、pin3 RS_A、pin2 VIN_P240、pin1 GND |
| J8 | CARD_SOCKET_SIM | 连接 SIM7020C 的 SIM_VDD、SIM_DATA、SIM_CLK、SIM_RST、GND 和卡检测相关线路 | 图 b50bad176689 / 第 1 页 / 第 1 页右下 J8 CARD_SOCKET_SIM，C1/C2/C3/C5/C6/C7 与 SIM 信号 |
| ANT1 | IPEX | SIM7020C ANT pin32 的外部射频天线接口 | 图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 ANT pin32 到 ANT1 IPEX，接口外壳接 GND |
| FU1,D1,FU2 | SL0805200 / SOD4007 / BSMD0805-050-24V | CORE_BAT 与 VIN_P240 输入路径的保险和二极管保护器件 | 图 b50bad176689 / 第 1 页 / 第 1 页左下 FU1/D1 的 BAT_IN/CORE_BAT 路径及右上 FU2 的 VIN_P240 路径 |
| LED1 | RED | 由 SIM7020C STATUS 信号驱动的红色状态指示灯 | 图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 STATUS pin42 经 NB_STAT、R13 5.1K/1% 到 LED1 RED 和 GND |

## 系统结构

### IoT Base NBIoT-CN 系统架构

BUS1 提供主机 GPIO、UART、RS485 和电源网络；VIN_P240 经 U3/U4 生成 CORE_P050 与 NB_P033，U1 SIM7020C 通过电平转换 UART、PWRKEY、状态 LED、IPEX 天线和 J8 SIM 卡座工作，U2 提供 RS485 收发。

- 参数与网络：`modem=U1 SIM7020C`；`power=VIN_P240 -> U3 SY8205FCC -> CORE_P050 -> U4 SY8089AAAC -> NB_P033`；`modem_uart=CORE_TXD/CORE_RXD <-> Q2/Q4 <-> NB_RXD/NB_TXD`；`rs485=BUS1 RS_RXD/RS_TXD <-> U2 <-> RS_A/RS_B`；`sim=J8 CARD_SOCKET_SIM`；`antenna=ANT1 IPEX`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页完整单页的 BUS1、电源、RS485、UART 转换、SIM7020C、SIM 和接口

## 电源

### VIN_P240 到 CORE_P050

VIN_P240 经 FU2 BSMD0805-050-24V 到 U3 VIN pins8/7，EN pin3 同接输入；U3 LX pin2 经 L1 2.2uH 生成 CORE_P050，BS pin1 通过 C6 104/50V 接 LX，FB pin5 使用 R15 36K/1% 与 R16 5.1K/1% 反馈网络。

- 参数与网络：`input=VIN_P240`；`input_fuse=FU2 BSMD0805-050-24V`；`converter=U3 SY8205FCC`；`inductor=L1 2.2uH`；`output=CORE_P050`；`feedback=R15 36K/1%, R16 5.1K/1%`；`bootstrap=C6 104/50V`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页右上 VIN_P240/FU2/U3/C6/L1/R15/R16/CORE_P050

### CORE_P050 到 NB_P033

CORE_P050 连接 U4 IN pin4 与 EN pin1，U4 SW pin3 经 L2 10uH 形成 NB_P033，FB pin5 使用 R18 22K/1% 与 R19 8.2K/1% 分压，C11 226/16V 从 NB_P033 接 GND。

- 参数与网络：`input=CORE_P050`；`converter=U4 SY8089AAAC`；`inductor=L2 10uH`；`output=NB_P033`；`feedback=R18 22K/1%, R19 8.2K/1%`；`output_capacitor=C11 226/16V`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页右上 CORE_P050/U4/L2/R18/R19/C11/NB_P033

### BAT_IN 到 CORE_BAT

J5 pin1 和 J6 pin2 接 BAT_IN，J5 pin2/SH 与 J6 pin1 接 GND；BAT_IN 经 FU1 SL0805200 到 CORE_BAT，D1 SOD4007 连接 CORE_BAT 与 GND，CORE_BAT 再连接 BUS1 pin1。

- 参数与网络：`battery_inputs=J5 pin1 BAT_IN; J6 pin2 BAT_IN`；`ground=J5 pin2/SH; J6 pin1`；`series_fuse=FU1 SL0805200`；`diode=D1 SOD4007 between CORE_BAT and GND`；`output=CORE_BAT -> BUS1 pin1`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页左下 J5/J6、BAT_IN、FU1、D1、CORE_BAT 与 BUS1 同名网络

### SIM7020C 电源连接

U1 VBAT pins34/35 接 NB_P033，并由 C1/C2 两只 106/10V 电容对地去耦；VDD_EXT pin40 输出 NB_P018；U1 多个 GND 引脚接 GND。

- 参数与网络：`vbat=pins34,35 -> NB_P033`；`vbat_caps=C1/C2 106/10V`；`logic_output=pin40 VDD_EXT -> NB_P018`；`ground_net=U1 GND pins -> GND`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 VBAT/VDD_EXT/GND 与 NB_P033/NB_P018/C1/C2

## 接口

### BUS1 M5_BUS 已连接针脚

BUS1 已连接 pin30/28/26 GND、pin29 CORE_RXD、pin27 G36、pin21 G26、pin16 G16、pin15 G17、pin14 G21、pin13 G22、pin10 MOD_PWR、pin9 RS_TXD、pin8 RS_RXD、pin7 CORE_TXD、pin3 CORE_P050 和 pin1 CORE_BAT。

- 参数与网络：`ground=pins30,28,26`；`modem_uart=pin29 CORE_RXD (G35/ADC), pin7 CORE_TXD (G0/IIS_MK)`；`rs485=pin9 RS_TXD (G13/IIS_WS), pin8 RS_RXD (G15/IIS_OUT)`；`modem_power_control=pin10 MOD_PWR (G12/IIS_SK)`；`grove_gpio=pin27 G36, pin21 G26, pin16 G16, pin15 G17, pin14 G21, pin13 G22`；`power=pin3 CORE_P050, pin1 CORE_BAT`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页左上 BUS1 M5_BUS 所有带外部网络名的针脚

### J1/J2/J3 Grove 接口

J1 IO2/IO1/5V/GND 依次连接 G22/G21/CORE_P050/GND；J2 连接 G36/G26/CORE_P050/GND；J3 连接 G16/G17/CORE_P050/GND。

- 参数与网络：`J1=pin4 G22, pin3 G21, pin2 CORE_P050, pin1 GND`；`J2=pin4 G36, pin3 G26, pin2 CORE_P050, pin1 GND`；`J3=pin4 G16, pin3 G17, pin2 CORE_P050, pin1 GND`；`signal_direction=由外接主机 GPIO 配置，原理图未固定`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页左侧 J1/J2/J3 GROVE 的 pin1-pin4 网络

### J4 DC 输入

J4 DC5.5 的 PWR+ 接 VIN_P240，PWR- 接 GND。

- 参数与网络：`positive=VIN_P240`；`negative=GND`；`direction=power input`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页左下 J4 DC5.5 PWR+/PWR-

### J7 RS485 与电源接口

J7 HT3.96_4P 的 pin4 接 RS_B、pin3 接 RS_A、pin2 接 VIN_P240、pin1 接 GND。

- 参数与网络：`pin4=RS_B bidirectional`；`pin3=RS_A bidirectional`；`pin2=VIN_P240 power input`；`pin1=GND`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页左下 J7 HT3.96_4P 的 pin1-pin4 标签

### SIM7020C 状态指示灯

U1 STATUS pin42 输出 NB_STAT，经 R13 5.1K/1% 和 LED1 RED 接 GND；U1 NETLIGHT pin41 在本页未连接。

- 参数与网络：`status_pin=U1 pin42 STATUS -> NB_STAT`；`resistor=R13 5.1K/1%`；`led=LED1 RED to GND`；`netlight=U1 pin41 unconnected`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 STATUS/NETLIGHT、NB_STAT、R13 与 LED1

### SIM7020C 与 J8 SIM 卡座

U1 SIM_VDD pin18、SIM_DATA pin15、SIM_CLK pin16 和 SIM_RST pin17 连接 J8 CARD_SOCKET_SIM 的 VCC、IO、CLK 和 RST；J8 GND 与 SHELL 接地，U1 SIM_DET pin14 连接卡座检测相关线路。

- 参数与网络：`supply=U1 pin18 SIM_VDD -> J8 VCC`；`data=U1 pin15 SIM_DATA <-> J8 IO`；`clock=U1 pin16 SIM_CLK -> J8 CLK`；`reset=U1 pin17 SIM_RST -> J8 RST`；`detect=U1 pin14 SIM_DET -> J8 detect-related line`；`ground=J8 GND/SHELL -> GND`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页右下 U1 SIM_VDD/SIM_DET/SIM_DATA/SIM_CLK/SIM_RST 与 J8 C1/C2/C3/C5/C6/C7

## 总线

### U2 RS485 收发与自动方向

U2 RO pin1 连接 RS_TXD，A pin6/B pin7 连接 RS_A/RS_B，VCC pin8 接 NB_P033、GND pin5 接地；RE pin2 与 DE pin3 相连并由 Q1 S8050 控制，RS_RXD 经 R2 2.2K 驱动 Q1，R7 2.2K 将 RE/DE 节点上拉到 NB_P033，DI pin4 在图中接 GND。

- 参数与网络：`receiver_output=RO pin1 -> RS_TXD`；`bus=A pin6 -> RS_A; B pin7 -> RS_B`；`supply=VCC pin8 NB_P033; GND pin5`；`direction=RE pin2 tied DE pin3; Q1 S8050 control`；`direction_input=RS_RXD through R2 2.2K`；`direction_pullup=R7 2.2K to NB_P033`；`driver_input=DI pin4 -> GND`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页中央 U2、Q1、R1/R2/R7、RS_TXD/RS_RXD、RS_A/RS_B

### CORE 与 SIM7020C UART 电平转换

BUS1 pin7 的 CORE_TXD 经 Q2 S8050 电平转换到 NB_RXD，并接 U1 UART1_RXD pin2；U1 UART1_TXD pin1 的 NB_TXD 经 Q4 S8050 转换到 CORE_RXD，再接 BUS1 pin29。该网络使用 NB_P018、NB_P033 与 R3-R6/R11/R12 的 5.1K/1% 电阻。

- 参数与网络：`controller=外接 CORE via BUS1`；`device=U1 SIM7020C UART1`；`core_to_modem=BUS1 pin7 CORE_TXD -> Q2 -> NB_RXD -> U1 pin2 UART1_RXD`；`modem_to_core=U1 pin1 UART1_TXD -> NB_TXD -> Q4 -> CORE_RXD -> BUS1 pin29`；`transistors=Q2,Q4 S8050`；`logic_rails=NB_P018, NB_P033`；`resistors=R3/R4/R5/R6/R11/R12 5.1K/1%`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页中央 Q2/Q4 UART 电平转换与下中 U1 UART1_TXD/UART1_RXD

## GPIO 与控制信号

### SIM7020C PWRKEY 控制

BUS1 pin10 的 MOD_PWR 经 R9 5.1K/1% 驱动 Q3 S8050，R10 5.1K/1% 将控制节点接地；Q3 将 U1 PWRKEY pin39 的 NB_KEY 网络拉向 GND。

- 参数与网络：`host=BUS1 pin10 MOD_PWR (G12/IIS_SK)`；`base_resistor=R9 5.1K/1%`；`pulldown=R10 5.1K/1%`；`transistor=Q3 S8050`；`modem_pin=U1 pin39 PWRKEY -> NB_KEY`；`action=Q3 low-side pull-down`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页中央 MOD_PWR/R9/R10/Q3/NB_KEY 与 U1 PWRKEY pin39

## 复位

### SIM7020C RESET 引脚

U1 RESET pin28 在本页未连接；模组的上电控制由 PWRKEY pin39 的 NB_KEY 网络实现。

- 参数与网络：`reset_pin=U1 pin28 RESET`；`reset_connection=unconnected on this page`；`power_key=U1 pin39 PWRKEY -> NB_KEY`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 左侧 RESET pin28 无外部连线，右侧 PWRKEY pin39 接 NB_KEY

## 保护电路

### RS485 偏置、终端位与 TVS

R14 5.1K/1% 将 RS_A 拉向 NB_P033，R17 5.1K/1% 将 RS_B 拉向 GND；RX1 标为 DNP 并跨接 RS_A/RS_B。TVS1/TVS2/TVS3 均标 P6S05C-LF，构成 A/B 线间及对地保护网络。

- 参数与网络：`a_bias=R14 5.1K/1% to NB_P033`；`b_bias=R17 5.1K/1% to GND`；`termination=RX1 DNP across RS_A/RS_B`；`tvs=TVS1/TVS2/TVS3 P6S05C-LF`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页中央 RS_A/RS_B 周围 R14/R17/RX1 和 TVS1/TVS2/TVS3

## 射频

### SIM7020C 外部天线

U1 ANT pin32 直接连接 ANT1 IPEX，IPEX 外壳接 GND；图中未显示射频匹配元件或天线切换器。

- 参数与网络：`modem_pin=U1 pin32 ANT`；`connector=ANT1 IPEX`；`shield=GND`；`signal_direction=bidirectional RF`；`matching_network_shown=false`；`rf_switch_shown=false`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 ANT pin32 到 ANT1 IPEX

## 调试与烧录

### SIM7020C 未引出的接口

U1 UART1_RTS/CTS/DCD/DTR/RI、USB_VBUS/USB_DM/USB_DP、UART2_RXD/UART2_TXD、ADC、GPIO1、GPIO0 和 RTC_GPIO0 在本页均未连接到外部网络。

- 参数与网络：`uart1_control=pins3-7 unconnected`；`usb=pins24/28/25 unconnected`；`uart2=pins23/22 unconnected`；`other=ADC pin38, GPIO1 pin29, GPIO0 pin10, RTC_GPIO0 pin11 unconnected`
- 证据：图 b50bad176689 / 第 1 页 / 第 1 页下中 U1 两侧无外接线的 UART1 控制、USB、UART2、ADC、GPIO 与 RTC_GPIO0 引脚

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | IoT Base NBIoT-CN 系统架构 | `modem=U1 SIM7020C`；`power=VIN_P240 -> U3 SY8205FCC -> CORE_P050 -> U4 SY8089AAAC -> NB_P033`；`modem_uart=CORE_TXD/CORE_RXD <-> Q2/Q4 <-> NB_RXD/NB_TXD`；`rs485=BUS1 RS_RXD/RS_TXD <-> U2 <-> RS_A/RS_B`；`sim=J8 CARD_SOCKET_SIM`；`antenna=ANT1 IPEX` |
| 接口 | BUS1 M5_BUS 已连接针脚 | `ground=pins30,28,26`；`modem_uart=pin29 CORE_RXD (G35/ADC), pin7 CORE_TXD (G0/IIS_MK)`；`rs485=pin9 RS_TXD (G13/IIS_WS), pin8 RS_RXD (G15/IIS_OUT)`；`modem_power_control=pin10 MOD_PWR (G12/IIS_SK)`；`grove_gpio=pin27 G36, pin21 G26, pin16 G16, pin15 G17, pin14 G21, pin13 G22`；`power=pin3 CORE_P050, pin1 CORE_BAT` |
| 电源 | VIN_P240 到 CORE_P050 | `input=VIN_P240`；`input_fuse=FU2 BSMD0805-050-24V`；`converter=U3 SY8205FCC`；`inductor=L1 2.2uH`；`output=CORE_P050`；`feedback=R15 36K/1%, R16 5.1K/1%`；`bootstrap=C6 104/50V` |
| 电源 | CORE_P050 到 NB_P033 | `input=CORE_P050`；`converter=U4 SY8089AAAC`；`inductor=L2 10uH`；`output=NB_P033`；`feedback=R18 22K/1%, R19 8.2K/1%`；`output_capacitor=C11 226/16V` |
| 电源 | BAT_IN 到 CORE_BAT | `battery_inputs=J5 pin1 BAT_IN; J6 pin2 BAT_IN`；`ground=J5 pin2/SH; J6 pin1`；`series_fuse=FU1 SL0805200`；`diode=D1 SOD4007 between CORE_BAT and GND`；`output=CORE_BAT -> BUS1 pin1` |
| 接口 | J1/J2/J3 Grove 接口 | `J1=pin4 G22, pin3 G21, pin2 CORE_P050, pin1 GND`；`J2=pin4 G36, pin3 G26, pin2 CORE_P050, pin1 GND`；`J3=pin4 G16, pin3 G17, pin2 CORE_P050, pin1 GND`；`signal_direction=由外接主机 GPIO 配置，原理图未固定` |
| 接口 | J4 DC 输入 | `positive=VIN_P240`；`negative=GND`；`direction=power input` |
| 接口 | J7 RS485 与电源接口 | `pin4=RS_B bidirectional`；`pin3=RS_A bidirectional`；`pin2=VIN_P240 power input`；`pin1=GND` |
| 总线 | U2 RS485 收发与自动方向 | `receiver_output=RO pin1 -> RS_TXD`；`bus=A pin6 -> RS_A; B pin7 -> RS_B`；`supply=VCC pin8 NB_P033; GND pin5`；`direction=RE pin2 tied DE pin3; Q1 S8050 control`；`direction_input=RS_RXD through R2 2.2K`；`direction_pullup=R7 2.2K to NB_P033`；`driver_input=DI pin4 -> GND` |
| 保护电路 | RS485 偏置、终端位与 TVS | `a_bias=R14 5.1K/1% to NB_P033`；`b_bias=R17 5.1K/1% to GND`；`termination=RX1 DNP across RS_A/RS_B`；`tvs=TVS1/TVS2/TVS3 P6S05C-LF` |
| 总线 | CORE 与 SIM7020C UART 电平转换 | `controller=外接 CORE via BUS1`；`device=U1 SIM7020C UART1`；`core_to_modem=BUS1 pin7 CORE_TXD -> Q2 -> NB_RXD -> U1 pin2 UART1_RXD`；`modem_to_core=U1 pin1 UART1_TXD -> NB_TXD -> Q4 -> CORE_RXD -> BUS1 pin29`；`transistors=Q2,Q4 S8050`；`logic_rails=NB_P018, NB_P033`；`resistors=R3/R4/R5/R6/R11/R12 5.1K/1%` |
| GPIO 与控制信号 | SIM7020C PWRKEY 控制 | `host=BUS1 pin10 MOD_PWR (G12/IIS_SK)`；`base_resistor=R9 5.1K/1%`；`pulldown=R10 5.1K/1%`；`transistor=Q3 S8050`；`modem_pin=U1 pin39 PWRKEY -> NB_KEY`；`action=Q3 low-side pull-down` |
| 接口 | SIM7020C 状态指示灯 | `status_pin=U1 pin42 STATUS -> NB_STAT`；`resistor=R13 5.1K/1%`；`led=LED1 RED to GND`；`netlight=U1 pin41 unconnected` |
| 射频 | SIM7020C 外部天线 | `modem_pin=U1 pin32 ANT`；`connector=ANT1 IPEX`；`shield=GND`；`signal_direction=bidirectional RF`；`matching_network_shown=false`；`rf_switch_shown=false` |
| 接口 | SIM7020C 与 J8 SIM 卡座 | `supply=U1 pin18 SIM_VDD -> J8 VCC`；`data=U1 pin15 SIM_DATA <-> J8 IO`；`clock=U1 pin16 SIM_CLK -> J8 CLK`；`reset=U1 pin17 SIM_RST -> J8 RST`；`detect=U1 pin14 SIM_DET -> J8 detect-related line`；`ground=J8 GND/SHELL -> GND` |
| 电源 | SIM7020C 电源连接 | `vbat=pins34,35 -> NB_P033`；`vbat_caps=C1/C2 106/10V`；`logic_output=pin40 VDD_EXT -> NB_P018`；`ground_net=U1 GND pins -> GND` |
| 复位 | SIM7020C RESET 引脚 | `reset_pin=U1 pin28 RESET`；`reset_connection=unconnected on this page`；`power_key=U1 pin39 PWRKEY -> NB_KEY` |
| 调试与烧录 | SIM7020C 未引出的接口 | `uart1_control=pins3-7 unconnected`；`usb=pins24/28/25 unconnected`；`uart2=pins23/22 unconnected`；`other=ADC pin38, GPIO1 pin29, GPIO0 pin10, RTC_GPIO0 pin11 unconnected` |
| 核心器件 | U2 RS485 收发器型号 | `reference=U2`；`part_number=null`；`supply=NB_P033`；`pins=RO,RE,DE,DI,A,B,VCC,GND`；`package=null`；`common_mode_range=null` |
| 射频 | 正文中的频段、速率、协议和 UART 参数 | `documented_bands=B1,B3,B5,B8`；`documented_uart=115200bps`；`documented_protocols=TCP,UDP,LWM2M,COAP,MQTT,HTTP,HTTPS,TLS,DTLS,DNS,NTP,PING`；`schematic_module=SIM7020C`；`firmware_version=null`；`measured_throughput=null` |
| 电源 | CORE_P050 与 NB_P033 供电能力 | `first_rail=CORE_P050`；`second_rail=NB_P033`；`first_converter=SY8205FCC`；`second_converter=SY8089AAAC`；`tolerance=null`；`continuous_current=null`；`peak_current=null`；`startup_sequence=null` |
| 保护电路 | J5/J6 电池输入边界 | `connectors=J5 MX1.25_2P, J6 HT3.96_2P`；`input_net=BAT_IN`；`output_net=CORE_BAT`；`fuse=FU1 SL0805200`；`diode=D1 SOD4007`；`voltage_range=null`；`chemistry=null`；`charge_path_shown=false` |
| 接口 | SIM 卡座规格与检测 | `documented_size=MicroSIM`；`schematic_designator=J8 CARD_SOCKET_SIM`；`mechanical_dimensions=null`；`orientation=null`；`hotplug_support=null`；`sim_det_default=null` |

## 待确认事项

- `component.rs485-transceiver-model`：原理图完整显示 U2 的八脚 RS485 收发器连接，但没有标注器件型号；实际料号、封装、共模范围和失效保护特性无法由本页确认。（证据：图 b50bad176689 / 第 1 页 / 第 1 页中央 U2 只有位号和引脚名，无底部料号文字）
- `rf.documented-radio-capabilities`：正文给出 Cat-NB B1/B3/B5/B8、上下行速率、协议栈、认证和 UART 115200bps；原理图只确认 SIM7020C 型号及物理连接，无法验证固件版本、运营商配置、认证状态和通信性能。（证据：图 b50bad176689 / 第 1 页 / 第 1 页 U1 SIM7020C、UART1 和 ANT/IPEX，图中无频段、速率、协议或认证表）
- `power.rail-capability`：原理图网络名表明两级输出为 CORE_P050 和 NB_P033，并给出稳压器、反馈和电容连接，但没有输出容差、持续/峰值电流、启动时序、热设计或 SIM7020C 发射条件下的压降数据。（证据：图 b50bad176689 / 第 1 页 / 第 1 页右上 U3/U4 两级电源与下中 U1 VBAT 负载）
- `protection.battery-input-limits`：原理图显示 BAT_IN 经 FU1 到 CORE_BAT，并有 D1 SOD4007 对地支路，但未标注允许电池电压、化学体系、极性、充电路径、FU1 额定值含义或 D1 的具体保护动作。（证据：图 b50bad176689 / 第 1 页 / 第 1 页左下 J5/J6、BAT_IN、FU1、D1、CORE_BAT）
- `interface.sim-socket-mechanics`：正文称卡槽为 MicroSIM；原理图只标 J8 CARD_SOCKET_SIM 并展示电气端子，未给出机械尺寸、插卡方向、热插拔限制或 SIM_DET 开关的默认状态。（证据：图 b50bad176689 / 第 1 页 / 第 1 页右下 J8 仅显示 CARD_SOCKET_SIM 电气符号和 C1-C7 端子）
- `review.rs485-transceiver-bom`：K064 当前 BOM 中 U2 的完整 RS485 收发器型号、封装、供电范围和失效保护特性是什么？；原因：原理图未标 U2 料号，不能仅凭八脚符号推导器件特性。
- `review.radio-firmware-region`：K064 量产 SIM7020C 的固件版本、启用频段、UART 参数、协议栈和当前有效认证清单是什么？；原因：这些能力依赖模组固件、运营商和测试条件，原理图只能确认型号与连接。
- `review.power-rail-capability`：CORE_P050 与 NB_P033 的目标电压、容差、持续/峰值电流、启动时序和 SIM7020C 发射压降指标是什么？；原因：网络名与反馈阻值不足以证明整机供电能力，需要 BOM、datasheet、布局和负载测试。
- `review.battery-input-safety`：J5/J6 允许连接何种电池、电压与极性，FU1/D1 的额定和保护目的是什么，板上是否具备充电功能？；原因：原理图没有电池规格、充电器或明确保护说明，错误接入存在硬件风险。
- `review.sim-socket-bom`：J8 当前 BOM 是否确为 MicroSIM 卡座，插卡方向、SIM_DET 默认状态和热插拔限制是什么？；原因：CARD_SOCKET_SIM 电气符号不能证明机械规格和检测开关行为。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b50bad1766895d00ef8789178d41347fc2a23924cca289562b89c654990c0efc` | `https://static-cdn.m5stack.com/resource/docs/products/base/iot_base_nb_cn/iot_base_nb_sch_01.webp` |

---

源文档：`zh_CN/base/iot_base_nb_cn.md`

源文档 SHA-256：`4be423fd9cda4eabe00bf4c45a14b3258f5bc7259490fb0bcb4c6a67392e254f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
