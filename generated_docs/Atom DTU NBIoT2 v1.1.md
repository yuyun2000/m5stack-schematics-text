# Atom DTU NBIoT2 v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU NBIoT2 v1.1 |
| SKU | A106-V21 |
| 产品 ID | `atom-dtu-nbiot2-v1-1-7cc35e7fc6dc` |
| 源文档 | `zh_CN/atom/Atom_DTU_NBIoT2_v1.1.md` |

## 概述

Atom DTU NBIoT2 v1.1 原理图以 M1 SIM7028 NB-IoT 模组为核心，连接 U3 Micro-SIM、E1 SMA 天线、STATUS/NETLIGHT 指示和 Atom-5Pin UART。P1 的 +VIN 经 F1、U20 SY8303AIC 降压及 U2 串联器件形成 +5V，U6 TPS7A2033PDBVR 生成 +3.3V，U1 SY8089AAAC 在 SIM_PWR_EN 控制下生成 SIM_VBAT。U4 IO_EXP 通过 G21/G25 I2C 控制 SIM_PWR_EN、IO1_SIM_RESET 并采集 VIN_ADC；U5 SP3485EN-L/TR 提供带自动方向控制、偏置、可选端接和 SP4021 防护的 RS485_A/RS485_B。

## 检索关键词

`Atom DTU NBIoT2 v1.1`、`A106-V21`、`SIM7028`、`IO_EXP`、`M5IOE1`、`SP3485EN-L/TR`、`SY8303AIC`、`SY8089AAAC`、`TPS7A2033PDBVR`、`CH213K`、`Micro-SIM`、`ANT_SMA-KWE`、`NB_RX`、`NB_TX`、`SIM_PWR_EN`、`IO1_SIM_RESET`、`VIN_ADC`、`RS485_A`、`RS485_B`、`G21`、`G25`、`G23`、`G33`、`Atom-4Pin`、`Atom-5Pin`、`HY-2.0_IIC`、`+VIN`、`+5V`、`+3.3V`、`SIM_VBAT`、`SIM_VCC`、`STATUS`、`NETLIGHT`、`SP4021-01FTG-C`、`BOOT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7028 | NB-IoT 通信模组，连接 Atom UART、Micro-SIM、SMA 天线、电源、复位和状态指示 | 图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C4，M1 SIM7028，UART1/SIM/ANT/VBAT/RESET/STATUS/NETLIGHT 引脚 |
| U4 | IO_EXP | I2C IO 扩展器，采集 VIN_ADC，并控制 SIM_PWR_EN 与 IO1_SIM_RESET | 图 e9a55ccf03f2 / 第 1 页 / 网格 D3，U4 IO_EXP，I2C_SCL/SDA、IO2/ADC1、IO9、IO11、ADDR_SEL |
| U20 | SY8303AIC | +VIN 至约 5.21V 的主降压转换器 | 图 e9a55ccf03f2 / 第 1 页 / 网格 A1-A2，U20 SY8303AIC、功率电感、R6/R9 反馈，Vout=5.21V |
| U2 | CH213K | 位于主 Buck 输出与 +5V 之间的 IN/OUT/GND 串联器件 | 图 e9a55ccf03f2 / 第 1 页 / 网格 A2，U2 CH213K，IN+、OUT、GND，输出接 +5V 与 D4 |
| U1 | SY8089AAAC | +5V 至 SIM_VBAT 的 3.3V/600mA 降压转换器，由 SIM_PWR_EN 控制 | 图 e9a55ccf03f2 / 第 1 页 / 网格 B1-B2，U1 SY8089AAAC、L2、SIM_PWR_EN、SIM_VBAT，DCDC:3.3V_600mA |
| U6 | TPS7A2033PDBVR | +5V 至 +3.3V 的 LDO，为 IO 扩展、RS485 与逻辑电路供电 | 图 e9a55ccf03f2 / 第 1 页 / 网格 C1-D1，U6 TPS7A2033PDBVR，IN/EN=+5V、OUT=+3.3V |
| U5 | SP3485EN-L/TR | 3.3V RS-485 半双工收发器，将 Atom TX/RX 转换为 RS485_A/RS485_B | 图 e9a55ccf03f2 / 第 1 页 / 网格 D1-D2，U5 SP3485EN-L/TR，RO/nRE/DE/DI/A/B/VCC/GND |
| U3 | SIM socket | Micro-SIM 卡座，连接 SIM_DATA、SIM_CLK、SIM_RST、SIM_VCC 和 GND | 图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C2，U3 SIM，IO/CLK/RST/VCC/GND，VPP 未连接 |
| E1 | ANT_SMA-KWE | SIM7028 外置蜂窝天线 SMA 连接器 | 图 e9a55ccf03f2 / 第 1 页 / 网格 B4，M1 ANT 经 C24/L3/C25 到 E1 ANT_SMA-KWE |
| P1 | HDR_4P | 四针电源与 RS-485 端子，提供 RS485_B、RS485_A、+VIN 和 GND | 图 e9a55ccf03f2 / 第 1 页 / 网格 C4-D4，P1 HDR_4P，B/A/12V+/12V- |
| P2,P3 | Atom-5Pin / Atom-4Pin | 与 Atom 主控连接的电源、UART、RS485 控制和 I2C 排针 | 图 e9a55ccf03f2 / 第 1 页 / 网格 C1，P2 Atom-5Pin 与 P3 Atom-4Pin 的 G21/G25/G22/G19/G23/G33/电源网络 |
| J1 | HY-2.0_IIC | 四针 I2C 扩展接口，提供 IIC_SCL、IIC_SDA、+5V 和 GND；信号串联位默认 NC | 图 e9a55ccf03f2 / 第 1 页 / 网格 D4，J1 HY-2.0_IIC 与 R14/R15 NC |
| Q1,Q2 | SS8050 Y1 | STATUS 与 NETLIGHT LED 的低端驱动晶体管 | 图 e9a55ccf03f2 / 第 1 页 / 网格 A3，Q1/Q2 SS8050 Y1 与 D1 RED/D2 BLUE |
| Q3 | SS8050 Y1 | 由 TX 驱动的 RS-485 nRE/DE 自动方向控制晶体管 | 图 e9a55ccf03f2 / 第 1 页 / 网格 D1，TX-R21-Q3 与 R19 上拉、U5 nRE/DE 公共节点 |
| D5,D6,D7 | SP4021-01FTG-C | RS485_A/RS485_B 到地及线间的浪涌/ESD 保护阵列 | 图 e9a55ccf03f2 / 第 1 页 / 网格 C2-D2，D5/D6/D7 SP4021-01FTG-C 跨 GND、RS485_B、RS485_A |
| D1,D2 | RED / BLUE LED | 分别显示 SIM7028 STATUS 与 NETLIGHT | 图 e9a55ccf03f2 / 第 1 页 / 网格 A3，D1 RED STATUS、D2 BLUE NETLIGHT |
| F1 | 1.5A/24V | +VIN 输入串联保护器件 | 图 e9a55ccf03f2 / 第 1 页 / 网格 A1，+VIN 后串联 F1 1.5A/24V |
| D3,D4 | SS54 / TVS 5V | 输入 Schottky 钳位与 +5V 瞬态保护 | 图 e9a55ccf03f2 / 第 1 页 / 网格 A1-A2，D3 SS54 接输入节点至 GND，D4 TVS 5V 接 +5V 至 GND |

## 系统结构

### Atom DTU NBIoT2 v1.1 架构

电路由 SIM7028 蜂窝模组、Micro-SIM、SMA 天线、IO_EXP 管理器、Atom 4/5Pin 接口、SP3485EN RS485、电源转换、VIN_ADC 和状态指示组成。

- 参数与网络：`radio=M1 SIM7028`；`io_expander=U4 IO_EXP`；`sim=U3`；`antenna=E1`；`rs485=U5 SP3485EN-L/TR`；`host=P2/P3 Atom connectors`；`power=U20/U2/U6/U1`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 整页网格 A1-D4，各功能分区

## 核心器件

### SIM7028 通信模组

M1 明确标为 SIM7028，使用 UART1_TXD/RXD、SIM_DATA/CLK/RST/VDD、ANT、VBAT、RESET、BOOT、STATUS 与 NETLIGHT 等引脚。

- 参数与网络：`reference=M1`；`part_number=SIM7028`；`host_uart=UART1_TXD pin1,UART1_RXD pin2`；`sim_pins=15 SIM_DATA,16 SIM_CLK,17 SIM_RST,18 SIM_VDD`；`antenna_pin=32 ANT`；`power_pins=34,35 VBAT`；`reset_pin=28 RESET`；`boot_pin=10 BOOT`；`status_pins=42 STATUS,41 NETLIGHT`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C4，M1 SIM7028 全部引脚标注

### U4 IO 扩展控制映射

U4 IO_EXP 使用 G21/G25 作为 I2C_SCL/SDA，IO2/ADC1 pin11 接 VIN_ADC，IO9 pin13 输出 SIM_PWR_EN，IO11 pin10 输出 IO1_SIM_RESET。

- 参数与网络：`reference=U4`；`symbol=IO_EXP`；`scl=pin9 G21`；`sda=pin8 G25`；`adc=pin11 VIN_ADC`；`sim_power=pin13 SIM_PWR_EN`；`sim_reset=pin10 IO1_SIM_RESET`；`supply=+3.3V`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 D3，U4 IO_EXP pin8/9/10/11/13

## 电源

### +VIN 至 +5V 主电源

P1 的 12V+ 引脚连接 +VIN；+VIN 经 F1 1.5A/24V 后进入 U20 SY8303AIC Buck，反馈标注 Vfb=0.6V、Vout=5.21V，再经 U2 CH213K 输出 +5V。

- 参数与网络：`connector=P1 12V+`；`input_net=+VIN`；`fuse=F1 1.5A/24V`；`buck=U20 SY8303AIC`；`vfb_mark=0.6V`；`vout_mark=5.21V`；`series_device=U2 CH213K`；`output=+5V`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 A1-A2 与 C4-D4，P1 +VIN、F1、U20、U2、+5V

### U20 5V Buck 反馈与滤波

U20 输出级使用 FTC252012S4R7MBCA 电感，R6 100K/1% 与 R9 13K/1% 构成反馈；C2/C3 各 22uF/10V，输入侧 C19/C1/C20/C4 各 10uF/50V。

- 参数与网络：`converter=U20 SY8303AIC`；`inductor=FTC252012S4R7MBCA`；`feedback_upper=R6 100K/1%`；`feedback_lower=R9 13K/1%`；`output_caps=C2,C3 22uF/10V`；`input_caps=C19,C1,C20,C4 10uF/50V`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 A1-A2，U20 周边电感、R6/R9、C19/C1/C20/C4/C2/C3

### +3.3V 逻辑电源

U6 TPS7A2033PDBVR 的 IN pin1 与 EN pin3 接 +5V，OUT pin5 生成 +3.3V；C26 1uF/16V 为输入电容，C15 1uF/16V 为输出电容，C27 标 NC。

- 参数与网络：`regulator=U6 TPS7A2033PDBVR`；`input=+5V`；`enable=+5V`；`output=+3.3V`；`input_cap=C26 1uF/16V`；`output_cap=C15 1uF/16V`；`nc_cap=C27 NC`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C1-D1，U6 与 C26/C27/C15

### SIM7028 可控 VBAT 电源

U1 SY8089AAAC 以 +5V 为输入、SIM_PWR_EN 驱动 EN，通过 L2 FTC201610S2R2MBCA 输出 SIM_VBAT；图面标注 DCDC:3.3V_600mA，SIM_VBAT 接 M1 pins34/35 并由 C14 100uF 储能。

- 参数与网络：`converter=U1 SY8089AAAC`；`input=+5V`；`enable=SIM_PWR_EN`；`inductor=L2 FTC201610S2R2MBCA`；`output=SIM_VBAT`；`output_mark=3.3V 600mA`；`module_pins=M1 pins34,35`；`bulk_cap=C14 100uF`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B1-B4，U1/L2/SIM_PWR_EN/SIM_VBAT/C14 到 M1 VBAT

### SIM_VBAT Buck 反馈与去耦

U1 的反馈网络为 R26 100K/1% 与 R27 22K/1%；输入 C16/C23 与输出 C21/C22 均标 10uF/6.3V。

- 参数与网络：`converter=U1`；`feedback_upper=R26 100K/1%`；`feedback_lower=R27 22K/1%`；`input_caps=C16,C23 10uF/6.3V`；`output_caps=C21,C22 10uF/6.3V`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B1-B2，U1 周边 R26/R27/C16/C23/C21/C22

## 接口

### Atom 4Pin/5Pin 映射

P3 Atom-4Pin 为 pin1 G21、pin2 G25、pin3 +5V、pin4 GND；P2 Atom-5Pin 为 pin1 3V3、pin2 G22/NB_RX、pin3 G19/NB_TX、pin4 G23/TX、pin5 G33/RX。

- 参数与网络：`p3=1 G21,2 G25,3 +5V,4 GND`；`p2=1 3V3,2 G22/NB_RX,3 G19/NB_TX,4 G23/TX,5 G33/RX`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C1，P3 Atom-4Pin 与 P2 Atom-5Pin

### J1 I2C 扩展接口

J1 HY-2.0_IIC pin1 为 IIC_SCL、pin2 为 IIC_SDA、pin3 为 +5V、pin4 为 GND；G21/G25 到 IIC_SCL/IIC_SDA 的 R14/R15 均标 NC，因此默认装配下信号支路断开。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=+5V`；`pin4=GND`；`scl_link=R14 NC to G21`；`sda_link=R15 NC to G25`；`assembled_signal_state=open`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 D4，J1 与 R14/R15 NC

### P1 RS-485 与电源端子

P1 HDR_4P 从上至下标为 B、A、12V+、12V-，分别连接 RS485_B、RS485_A、+VIN、GND。

- 参数与网络：`connector=P1 HDR_4P`；`pin_b=RS485_B`；`pin_a=RS485_A`；`pin_12v_plus=+VIN`；`pin_12v_minus=GND`；`signal_direction=RS485_A/B bidirectional`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C4-D4，P1 B/A/12V+/12V- 与网络标签

### Micro-SIM 信号接口

M1 SIM_DATA/CLK/RST 分别经 R11/R12/R13 22R 到 U3 IO/CLK/RST；SIM_VDD 形成 SIM_VCC 接 U3 VCC，U3 VPP 未连接。

- 参数与网络：`socket=U3`；`data=M1 pin15 SIM_DATA -> R11 22R -> U3 IO`；`clock=M1 pin16 SIM_CLK -> R12 22R -> U3 CLK`；`reset=M1 pin17 SIM_RST -> R13 22R -> U3 RST`；`power=M1 pin18 SIM_VDD -> SIM_VCC -> U3 VCC`；`vpp=NC`；`ground=U3 GND`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C3，M1 pins15-18、R11-R13、U3 SIM

## 总线

### Atom 与 SIM7028 UART

M1 pin1 UART1_TXD 形成 NB_TX，并接 P2 pin3/G19；M1 pin2 UART1_RXD 形成 NB_RX，并接 P2 pin2/G22。TP1 位于 NB_TX，TP2 位于 NB_RX。

- 参数与网络：`device_tx=M1 pin1 UART1_TXD`；`tx_net=NB_TX`；`host_rx=P2 pin3 G19`；`device_rx=M1 pin2 UART1_RXD`；`rx_net=NB_RX`；`host_tx=P2 pin2 G22`；`test_points=TP1 NB_TX,TP2 NB_RX`；`level=+3.3V host connector shown; module UART supply level not annotated`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C3，M1 UART1_TXD/RXD、NB_TX/NB_RX、TP1/TP2 与 P2 G19/G22

### Atom 到 IO_EXP I2C

P3 的 G21/G25 分别直接连接 U4 I2C_SCL pin9 与 I2C_SDA pin8；同一网络预留经 R14/R15 接往 J1 IIC_SCL/IIC_SDA。

- 参数与网络：`controller_connector=P3 Atom-4Pin`；`scl=G21 -> U4 pin9 I2C_SCL`；`sda=G25 -> U4 pin8 I2C_SDA`；`external_branch=G21/G25 via R14/R15 NC to J1`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C1-D4，P3 G21/G25、U4 I2C 和 J1 支路

### Atom UART 到 RS-485

P2 pin4/G23 的 TX 驱动 U5 DI 并经 R21/Q3 自动控制并联的 nRE/DE；U5 RO 经 R18 1K 输出 RX 到 P2 pin5/G33；U5 A/B 连接 RS485_A/RS485_B。

- 参数与网络：`host_tx=P2 pin4 G23/TX`；`driver_input=U5 pin4 DI`；`direction_control=TX -> R21 1K -> Q3; R19 4.7K pull-up; U5 pins2/3`；`receiver_output=U5 pin1 RO -> R18 1K -> RX -> P2 pin5 G33`；`bus=U5 pin6 A=RS485_A,pin7 B=RS485_B`；`supply=+3.3V`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C1-D2，P2 TX/RX 与 U5/Q3/R18/R19/R21/A/B

## 总线地址

### IO_EXP 地址选择

U4 ADDR_SEL pin19 经 R23 10K/1% 下拉至 GND；原理图未在该器件旁标出由此对应的数值 I2C 地址。

- 参数与网络：`device=U4 IO_EXP`；`address_pin=ADDR_SEL pin19`；`strap=R23 10K/1% to GND`；`numeric_address=null`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 D3，U4 ADDR_SEL pin19 与 R23 10K/1% 接 GND

## GPIO 与控制信号

### 通信模组电源与复位 GPIO

U4 IO9 pin13 驱动 SIM_PWR_EN 并连接 U1 EN；U4 IO11 pin10 驱动 IO1_SIM_RESET 并连接 M1 RESET pin28。

- 参数与网络：`power_gpio=U4 IO9 pin13`；`power_net=SIM_PWR_EN`；`power_target=U1 EN`；`reset_gpio=U4 IO11 pin10`；`reset_net=IO1_SIM_RESET`；`reset_target=M1 pin28 RESET`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B1-B4 与 D3，U4 IO9/IO11 到 U1/M1

### STATUS 与 NETLIGHT 指示

M1 STATUS pin42 经 R3 1K 驱动 Q1，控制 +5V-R1 1K-D1 RED；M1 NETLIGHT pin41 经 R4 1K 驱动 Q2，控制 +5V-R2 1K-D2 BLUE；R7/R8 各 100K 下拉。

- 参数与网络：`status=M1 pin42 STATUS,R3 1K,Q1,D1 RED,R1 1K,R7 100K`；`netlight=M1 pin41 NETLIGHT,R4 1K,Q2,D2 BLUE,R2 1K,R8 100K`；`led_supply=+5V`；`drivers=Q1,Q2 SS8050 Y1`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 A3-B3，D1/Q1 STATUS 与 D2/Q2 NETLIGHT 到 M1 pins42/41

## 时钟

### 板级时钟

本页未显示独立晶振、振荡器或外部时钟网络；SIM7028 与 IO_EXP 的内部时钟未在符号外展开。

- 参数与网络：`external_crystal=null`；`oscillator=null`；`clock_net=null`；`scope=single-page board schematic`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 整页网格 A1-D4，无 X/Y 晶振或 CLK 网络

## 复位

### IO_EXP 复位

U4 NRST pin1 使用 PY_NRST 网络，R16 10K/1% 上拉到 +3.3V，C12 1uF/16V 下拉至 GND，形成上电复位 RC。

- 参数与网络：`device=U4`；`reset_pin=pin1 NRST`；`net=PY_NRST`；`pullup=R16 10K/1% to +3.3V`；`capacitor=C12 1uF/16V to GND`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 D3，U4 NRST/PY_NRST 与 R16/C12

### SIM7028 软件复位控制

U4 IO11 pin10 的 IO1_SIM_RESET 网络连接 M1 RESET pin28；该复位与 M1 SIM_RST pin17 到 SIM 卡 RST 的网络相互独立。

- 参数与网络：`controller=U4 IO11 pin10`；`net=IO1_SIM_RESET`；`module_reset=M1 pin28 RESET`；`sim_card_reset=M1 pin17 SIM_RST -> R13 -> U3 RST`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-D3，U4 IO11/IO1_SIM_RESET 到 M1 pin28，M1 pin17 SIM_RST 到 U3

## 保护电路

### RS-485 偏置、端接与浪涌保护

RS485_B 经 R17 4.7K 下拉，RS485_A 经 R22 4.7K 上拉到 +3.3V；R20 为跨 A/B 的 NC 端接位；D5/D6/D7 SP4021-01FTG-C 形成 B-地、B-A、A-地保护。

- 参数与网络：`b_bias=R17 4.7K to GND`；`a_bias=R22 4.7K to +3.3V`；`termination=R20 NC across A/B`；`protectors=D5,D6,D7 SP4021-01FTG-C`；`protected_nets=RS485_A,RS485_B,GND`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 C2-D2，R17/R20/R22 与 D5/D6/D7

### SIM 卡接口保护与滤波

SIM_DATA/CLK/RST 配置 TVS1/TVS3/TVS4/TVS5 防护和 C7/C8/C9 33pF 对地滤波；SIM_VCC 配 C6 100nF 与 TVS2。

- 参数与网络：`signal_tvs=TVS1,TVS3,TVS4,TVS5`；`signal_caps=C7,C8,C9 33pF`；`supply_cap=C6 100nF`；`supply_tvs=TVS2`；`nets=SIM_DATA,SIM_CLK,SIM_RST,SIM_VCC`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C2，U3 下方 TVS1-5、C6-C9

## 关键网络

### 管理与通信关键网络

Atom G21/G25 -> U4 I2C；U4 IO9 -> SIM_PWR_EN -> U1 -> SIM_VBAT；U4 IO11 -> IO1_SIM_RESET -> M1 RESET；Atom G22/G19 <-> NB_RX/NB_TX <-> M1 UART1；Atom G23/G33 <-> U5 <-> RS485_A/B。

- 参数与网络：`management=G21/G25 -> U4`；`power_control=U4.IO9 -> SIM_PWR_EN -> U1 -> SIM_VBAT`；`reset_control=U4.IO11 -> IO1_SIM_RESET -> M1.RESET`；`modem_uart=G22/G19 <-> NB_RX/NB_TX <-> M1`；`industrial_bus=G23/G33 <-> U5 <-> RS485_A/B`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 整页网络追踪：P2/P3、U4、U1、M1、U5、P1

## 存储

### 板级存储

本页未显示 Flash、EEPROM、eMMC 或存储卡器件；U3 是通信 SIM 卡座，不是数据存储卡接口。

- 参数与网络：`flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`sim_socket=U3`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 整页网格 A1-D4，仅 U3 SIM，无存储器器件

## 内存与 Flash

### SIM7028 内部存储器

SIM7028 在本页作为封装模组 M1 表示，内部 RAM/Flash 未展开，原理图未给出容量或总线。

- 参数与网络：`module=M1 SIM7028`；`ram=null`；`flash=null`；`internal_bus=null`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C4，M1 单一 SIM7028 模组符号，无内部 memory block

## 音频

### 音频电路

本页未显示音频编解码器、麦克风、扬声器或 I2S/PCM 音频网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s_pcm=null`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 整页网格 A1-D4，无 Audio/I2S/PCM 器件或网络

## 射频

### SIM7028 SMA 天线路径

M1 ANT pin32 通过预留 C24 对地、L3 0R 串联和预留 C25 对地的 pi 型匹配位置连接 E1 ANT_SMA-KWE，C24/C25 均标 NC。

- 参数与网络：`source=M1 pin32 ANT`；`shunt_in=C24 NC`；`series=L3 0R`；`shunt_out=C25 NC`；`connector=E1 ANT_SMA-KWE`；`return=multiple GND pins`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B3-B4，M1 ANT、C24/L3/C25、E1

## 调试与烧录

### 测试点与启动信号

TP1/TP2 分别位于 NB_TX/NB_RX，TP3 连接 M1 BOOT pin10，TP4 接 GND，TP5 接 SIM_VBAT，TP6 接 GND；本页未显示 SWD 或 JTAG 调试口。

- 参数与网络：`uart=TP1 NB_TX,TP2 NB_RX`；`boot=TP3 BOOT/M1 pin10`；`ground=TP4,TP6`；`power=TP5 SIM_VBAT`；`swd_jtag=null`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-C4，TP1-TP6 标注

## 模拟电路

### +VIN 电压监测分压

F1 后输入节点经 R5 10K/0.1% 与 R24 1K/0.1% 分压形成 VIN_ADC，C18 10nF 从 VIN_ADC 接地；VIN_ADC 接 U4 IO2/ADC1 pin11。

- 参数与网络：`source=+VIN after F1`；`upper_resistor=R5 10K/0.1%`；`lower_resistor=R24 1K/0.1%`；`filter=C18 10nF`；`adc_net=VIN_ADC`；`adc_input=U4 IO2/ADC1 pin11`；`divider_ratio=1/11`
- 证据：图 e9a55ccf03f2 / 第 1 页 / 网格 A1 与 D3-D4，R5/R24/C18 VIN_ADC 到 U4 pin11

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU NBIoT2 v1.1 架构 | `radio=M1 SIM7028`；`io_expander=U4 IO_EXP`；`sim=U3`；`antenna=E1`；`rs485=U5 SP3485EN-L/TR`；`host=P2/P3 Atom connectors`；`power=U20/U2/U6/U1` |
| 核心器件 | SIM7028 通信模组 | `reference=M1`；`part_number=SIM7028`；`host_uart=UART1_TXD pin1,UART1_RXD pin2`；`sim_pins=15 SIM_DATA,16 SIM_CLK,17 SIM_RST,18 SIM_VDD`；`antenna_pin=32 ANT`；`power_pins=34,35 VBAT`；`reset_pin=28 RESET`；`boot_pin=10 BOOT`；`status_pins=42 STATUS,41 NETLIGHT` |
| 电源 | +VIN 至 +5V 主电源 | `connector=P1 12V+`；`input_net=+VIN`；`fuse=F1 1.5A/24V`；`buck=U20 SY8303AIC`；`vfb_mark=0.6V`；`vout_mark=5.21V`；`series_device=U2 CH213K`；`output=+5V` |
| 电源 | U20 5V Buck 反馈与滤波 | `converter=U20 SY8303AIC`；`inductor=FTC252012S4R7MBCA`；`feedback_upper=R6 100K/1%`；`feedback_lower=R9 13K/1%`；`output_caps=C2,C3 22uF/10V`；`input_caps=C19,C1,C20,C4 10uF/50V` |
| 模拟电路 | +VIN 电压监测分压 | `source=+VIN after F1`；`upper_resistor=R5 10K/0.1%`；`lower_resistor=R24 1K/0.1%`；`filter=C18 10nF`；`adc_net=VIN_ADC`；`adc_input=U4 IO2/ADC1 pin11`；`divider_ratio=1/11` |
| 电源 | +3.3V 逻辑电源 | `regulator=U6 TPS7A2033PDBVR`；`input=+5V`；`enable=+5V`；`output=+3.3V`；`input_cap=C26 1uF/16V`；`output_cap=C15 1uF/16V`；`nc_cap=C27 NC` |
| 电源 | SIM7028 可控 VBAT 电源 | `converter=U1 SY8089AAAC`；`input=+5V`；`enable=SIM_PWR_EN`；`inductor=L2 FTC201610S2R2MBCA`；`output=SIM_VBAT`；`output_mark=3.3V 600mA`；`module_pins=M1 pins34,35`；`bulk_cap=C14 100uF` |
| 电源 | SIM_VBAT Buck 反馈与去耦 | `converter=U1`；`feedback_upper=R26 100K/1%`；`feedback_lower=R27 22K/1%`；`input_caps=C16,C23 10uF/6.3V`；`output_caps=C21,C22 10uF/6.3V` |
| 总线 | Atom 与 SIM7028 UART | `device_tx=M1 pin1 UART1_TXD`；`tx_net=NB_TX`；`host_rx=P2 pin3 G19`；`device_rx=M1 pin2 UART1_RXD`；`rx_net=NB_RX`；`host_tx=P2 pin2 G22`；`test_points=TP1 NB_TX,TP2 NB_RX`；`level=+3.3V host connector shown; module UART supply level not annotated` |
| 接口 | Atom 4Pin/5Pin 映射 | `p3=1 G21,2 G25,3 +5V,4 GND`；`p2=1 3V3,2 G22/NB_RX,3 G19/NB_TX,4 G23/TX,5 G33/RX` |
| 核心器件 | U4 IO 扩展控制映射 | `reference=U4`；`symbol=IO_EXP`；`scl=pin9 G21`；`sda=pin8 G25`；`adc=pin11 VIN_ADC`；`sim_power=pin13 SIM_PWR_EN`；`sim_reset=pin10 IO1_SIM_RESET`；`supply=+3.3V` |
| 总线 | Atom 到 IO_EXP I2C | `controller_connector=P3 Atom-4Pin`；`scl=G21 -> U4 pin9 I2C_SCL`；`sda=G25 -> U4 pin8 I2C_SDA`；`external_branch=G21/G25 via R14/R15 NC to J1` |
| 总线地址 | IO_EXP 地址选择 | `device=U4 IO_EXP`；`address_pin=ADDR_SEL pin19`；`strap=R23 10K/1% to GND`；`numeric_address=null` |
| 复位 | IO_EXP 复位 | `device=U4`；`reset_pin=pin1 NRST`；`net=PY_NRST`；`pullup=R16 10K/1% to +3.3V`；`capacitor=C12 1uF/16V to GND` |
| 复位 | SIM7028 软件复位控制 | `controller=U4 IO11 pin10`；`net=IO1_SIM_RESET`；`module_reset=M1 pin28 RESET`；`sim_card_reset=M1 pin17 SIM_RST -> R13 -> U3 RST` |
| GPIO 与控制信号 | 通信模组电源与复位 GPIO | `power_gpio=U4 IO9 pin13`；`power_net=SIM_PWR_EN`；`power_target=U1 EN`；`reset_gpio=U4 IO11 pin10`；`reset_net=IO1_SIM_RESET`；`reset_target=M1 pin28 RESET` |
| 接口 | J1 I2C 扩展接口 | `connector=J1 HY-2.0_IIC`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=+5V`；`pin4=GND`；`scl_link=R14 NC to G21`；`sda_link=R15 NC to G25`；`assembled_signal_state=open` |
| 接口 | P1 RS-485 与电源端子 | `connector=P1 HDR_4P`；`pin_b=RS485_B`；`pin_a=RS485_A`；`pin_12v_plus=+VIN`；`pin_12v_minus=GND`；`signal_direction=RS485_A/B bidirectional` |
| 总线 | Atom UART 到 RS-485 | `host_tx=P2 pin4 G23/TX`；`driver_input=U5 pin4 DI`；`direction_control=TX -> R21 1K -> Q3; R19 4.7K pull-up; U5 pins2/3`；`receiver_output=U5 pin1 RO -> R18 1K -> RX -> P2 pin5 G33`；`bus=U5 pin6 A=RS485_A,pin7 B=RS485_B`；`supply=+3.3V` |
| 保护电路 | RS-485 偏置、端接与浪涌保护 | `b_bias=R17 4.7K to GND`；`a_bias=R22 4.7K to +3.3V`；`termination=R20 NC across A/B`；`protectors=D5,D6,D7 SP4021-01FTG-C`；`protected_nets=RS485_A,RS485_B,GND` |
| 接口 | Micro-SIM 信号接口 | `socket=U3`；`data=M1 pin15 SIM_DATA -> R11 22R -> U3 IO`；`clock=M1 pin16 SIM_CLK -> R12 22R -> U3 CLK`；`reset=M1 pin17 SIM_RST -> R13 22R -> U3 RST`；`power=M1 pin18 SIM_VDD -> SIM_VCC -> U3 VCC`；`vpp=NC`；`ground=U3 GND` |
| 保护电路 | SIM 卡接口保护与滤波 | `signal_tvs=TVS1,TVS3,TVS4,TVS5`；`signal_caps=C7,C8,C9 33pF`；`supply_cap=C6 100nF`；`supply_tvs=TVS2`；`nets=SIM_DATA,SIM_CLK,SIM_RST,SIM_VCC` |
| 射频 | SIM7028 SMA 天线路径 | `source=M1 pin32 ANT`；`shunt_in=C24 NC`；`series=L3 0R`；`shunt_out=C25 NC`；`connector=E1 ANT_SMA-KWE`；`return=multiple GND pins` |
| GPIO 与控制信号 | STATUS 与 NETLIGHT 指示 | `status=M1 pin42 STATUS,R3 1K,Q1,D1 RED,R1 1K,R7 100K`；`netlight=M1 pin41 NETLIGHT,R4 1K,Q2,D2 BLUE,R2 1K,R8 100K`；`led_supply=+5V`；`drivers=Q1,Q2 SS8050 Y1` |
| 调试与烧录 | 测试点与启动信号 | `uart=TP1 NB_TX,TP2 NB_RX`；`boot=TP3 BOOT/M1 pin10`；`ground=TP4,TP6`；`power=TP5 SIM_VBAT`；`swd_jtag=null` |
| 关键网络 | 管理与通信关键网络 | `management=G21/G25 -> U4`；`power_control=U4.IO9 -> SIM_PWR_EN -> U1 -> SIM_VBAT`；`reset_control=U4.IO11 -> IO1_SIM_RESET -> M1.RESET`；`modem_uart=G22/G19 <-> NB_RX/NB_TX <-> M1`；`industrial_bus=G23/G33 <-> U5 <-> RS485_A/B` |
| 时钟 | 板级时钟 | `external_crystal=null`；`oscillator=null`；`clock_net=null`；`scope=single-page board schematic` |
| 存储 | 板级存储 | `flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`sim_socket=U3` |
| 内存与 Flash | SIM7028 内部存储器 | `module=M1 SIM7028`；`ram=null`；`flash=null`；`internal_bus=null` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s_pcm=null` |
| 核心器件 | IO 扩展器具体型号 | `reference=U4`；`schematic_mark=IO_EXP`；`documented_model=M5IOE1`；`schematic_part_number=null`；`numeric_i2c_address=null` |
| 电源 | 输入范围与 Grove 带载能力 | `documented_input=9~24V`；`documented_grove_load=5V@1.3A`；`schematic_connector_mark=12V+`；`fuse_mark=1.5A/24V`；`verified_input_range=null`；`verified_continuous_5v_load=null` |
| 射频 | Cat-NB 频段与吞吐率 | `documented_module=SIM7028`；`documented_bands=B1/B2/B3/B4/B5/B8/B12/B13/B14/B17/B18/B19/B20/B25/B26/B28/B66/B70/B85`；`documented_downlink=127kbps`；`documented_uplink=159kbps`；`schematic_band_data=null`；`schematic_throughput_data=null` |

## 待确认事项

- `component.io-expander-model`：产品正文称 IO 扩展管理芯片为 M5IOE1，但当前原理图 U4 只标 IO_EXP，未在器件符号旁给出 M5IOE1 料号或数值 I2C 地址。（证据：图 e9a55ccf03f2 / 第 1 页 / 网格 D3，U4 仅标 IO_EXP，ADDR_SEL 下拉）
- `power.documented-ratings`：正文称 P1 输入 9~24V 且 RS485 供电时 Grove +5V 可带载 1.3A；原理图仅标 P1 12V+、F1 1.5A/24V、U20 输出设定和 +5V 网络，未给出完整输入范围与持续输出额定测试条件。（证据：图 e9a55ccf03f2 / 第 1 页 / 网格 A1-A2 与 D4，P1 12V+、F1 1.5A/24V、U20/U2 +5V，无 9~24V/1.3A 额定表）
- `rf.documented-bands-performance`：正文列出多组 Cat-NB 频段及 127kbps 下行/159kbps 上行；原理图只确认 M1 SIM7028 与 SMA 天线路径，没有频段表、射频认证配置或吞吐性能参数。（证据：图 e9a55ccf03f2 / 第 1 页 / 网格 B2-B4，M1 SIM7028 与 E1 天线路径，无 band/throughput 表）
- `review.io-expander-model`：请用 v1.1 量产 BOM、U4 丝印或 M5IOE1 设计资料确认 U4 的具体型号及 ADDR_SEL 接地时的 7-bit I2C 地址。；原因：原理图符号仅标 IO_EXP，未标 M5IOE1 型号和数值地址。
- `review.power-ratings`：请用 U20/U2 datasheet、量产 BOM、热设计与负载测试确认 9~24V 输入范围及 +5V Grove 1.3A 持续带载能力。；原因：F1 与电源反馈值不能单独证明完整工作范围和持续输出额定。
- `review.rf-bands-performance`：请依据 SIM7028 具体硬件版本、固件、认证资料和网络测试确认支持频段与上下行吞吐率。；原因：原理图仅给出 SIM7028 型号及天线连接，不含频段和性能数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e9a55ccf03f23cb1805dbbdfc30a2694ec23d7a02d2f9c43deb85f53f66802e8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/SCH_Atom_DTU_NBIoT_v1.1_2025_11_06_19_20_28_page_01.png` |

---

源文档：`zh_CN/atom/Atom_DTU_NBIoT2_v1.1.md`

源文档 SHA-256：`8744fdd0a8c631725ef6983b83b18cfe68446fc79a444093d51568357c811726`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
