# Module NBIoT 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module NBIoT |
| SKU | M028 |
| 产品 ID | `module-nbiot-96c9ad4f52eb` |
| 源文档 | `zh_CN/module/nb-iot.md` |

## 概述

Module NBIoT 以 U1 M5311 为 NB-IoT 通信核心，通过 U4 TXS0104E 在模块侧 1.8V 与 M5-Bus 侧 3.3V 之间转换主 UART 和调试 UART。Nano-SIM 卡座 U3 连接 M5311 的 SIM_VCC、SIM_RST、SIM_CLK、SIM_DATA，并配置 22Ω 串阻、33pF 滤波电容和 U2 SMF05CT1G 保护。M5-Bus J1 引出 GPIO2 开关机控制、GPIO26 复位控制及三组可选 UART 0Ω 路径；板上还包含状态/唤醒 LED、弹簧天线和 IPEX 天线支路。原理图没有稳压器，M5311 VBAT 与板上 3.3V 电源网相连；UART 跳线、射频 0Ω 电阻的实际装配状态及正文所列无线能力和控制时序需结合 BOM、PCB 或固件确认。

## 检索关键词

`Module NBIoT`、`M028`、`M5311`、`TXS0104E`、`SMF05CT1G`、`Nano-SIM`、`M5Stack_BUS`、`NB-IoT`、`UART1_TXD`、`UART1_RXD`、`DBG_TXD`、`DBG_RXD`、`U1_T`、`U1_R`、`GPIO16`、`GPIO17`、`GPIO12`、`GPIO13`、`GPIO15`、`GPIO5`、`GPIO2`、`GPIO26`、`S_PWR`、`S_RST`、`PWR_KEY`、`RST`、`WUP_OUT`、`STALED`、`SIM_VCC`、`SIM_RST`、`SIM_CLK`、`SIM_DATA`、`+1.8V`、`+3.3V`、`VBAT`、`ANT_IPEX`、`E1 Antenna`、`R11 0Ω`、`R13 0Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | M5311 | NB-IoT 通信模组，提供主 UART、调试 UART、SIM、射频、复位、开关机、唤醒和状态信号 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B2-C3 U1 M5311 |
| U4 | TXS0104E | U1 侧 +1.8V 与 M5-Bus 侧 +3.3V 之间的四通道 UART/调试信号电平转换器 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C2-C3 U4 TXS0104E |
| U3 | 未标注 | Nano-SIM 卡座，连接 SIM_VCC、RST、CLK、IO 和 GND | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B1-B2 U3 SIM 卡座 |
| U2 | SMF05CT1G | SIM 接口多通道瞬态保护阵列 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B1-B2 U2 SMF05CT1G |
| J1 | M5Stack_BUS | 主机堆叠接口，承载 GND、+3.3V、GPIO2 开关机、GPIO26 复位和可选 UART GPIO 路径 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C3-C4 J1 M5Stack_BUS |
| S1 | SW-PB | 将 +3.3V 接到 S_PWR 的本地开关机按键 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3 S1 SW-PB |
| Q1/Q4 | SS8050 Y1 | 分别把 S_RST、S_PWR 高电平转换为 M5311 RST、PWR_KEY 的低电平下拉控制 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 A4-B4 Q1 RESET 与 Q4 PWR_KEY |
| Q2/Q3 | SS8050 Y1 | STALED 与 WUP_OUT 控制的低侧 LED 驱动晶体管 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 A1-A2 Q2/Q3 LED 驱动 |
| D1/D2 | LED 0603 | 由 STALED 驱动的蓝色状态灯和由 WUP_OUT 驱动的绿色唤醒灯 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 A1-A2 D1 蓝灯 0603、D2 绿灯 0603 |
| E1 | Antenna | 经 R11 0Ω 连接 M5311 RF 的板载天线支路 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3 E1 Antenna 与 R11 |
| E2 | ANT_IPEX | 经 R13 0Ω 连接 M5311 RF 的 IPEX 外接天线支路 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3 E2 ANT_IPEX 与 R13 |
| R16/R18/R19/R20/R21/R22 | 0Ω | 把 U1_T/U1_R 路由到三组 M5-Bus UART GPIO 对的配置电阻 | 图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C3 J1 左侧 UART 0Ω 跳线矩阵 |

## 系统结构

### Module NBIoT

U1 M5311 集成无线通信功能，连接 U3 SIM 卡、E1/E2 射频支路、U4 电平转换器、板载按键和两路 LED，并通过 J1 M5Stack_BUS 与主机交互。

- 参数与网络：`modem=U1 M5311`；`sim=U3`；`level_shifter=U4 TXS0104E`；`host=J1 M5Stack_BUS`；`rf=E1/E2`；`indicators=D1/D2`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页完整功能分区

## 核心器件

### D1/D2 指示灯

U1.21 STATE/STALED 经 R4 1K 驱动 Q2，点亮 VBAT-R1 1K-D1 蓝灯支路；U1.16 WAKEUP_OUT/WUP_OUT 经 R5 1K 驱动 Q3，点亮 VBAT-R2 1K-D2 绿灯支路，R7/R8 均为 10K 下拉。

- 参数与网络：`blue=U1.21 STATE -> R4/Q2 -> D1, R1 1K`；`green=U1.16 WAKEUP_OUT -> R5/Q3 -> D2, R2 1K`；`base_pulldowns=R7,R8 10K`；`transistors=Q2,Q3 SS8050 Y1`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 A1-A2 D1/D2、Q2/Q3 与 U1.16/U1.21

## 电源

### M5311 VBAT 电源

U1 的 VBAT 引脚 31/32 接 VBAT；底部去耦网络把 VBAT 与 +3.3V 标在同一节点，C10 100uF、C11 100nF、C12 33pF 和 C13 10pF 对地。

- 参数与网络：`u1_pins=31,32`；`rail=VBAT/+3.3V`；`bulk=C10 100uF`；`decoupling=C11 100nF,C12 33pF,C13 10pF`；`regulator_shown=false`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 U1.31/U1.32 VBAT 与 D1-D2 底部 VBAT/+3.3V 去耦

### M5311 VDD_EXT

U1 引脚 20 VDD_EXT 生成 +1.8V，供 U4 VCCA 和 OE，并由 C6 4.7uF、C7/C9 100nF 对地去耦；U4 VCCB 接 +3.3V 并由 C8 100nF 去耦。

- 参数与网络：`source=U1.20 VDD_EXT`；`rail=+1.8V`；`u4_vcca=+1.8V`；`u4_oe=+1.8V`；`u4_vccb=+3.3V`；`capacitors=C6 4.7uF,C7/C8/C9 100nF`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C1-C3 U1.20、U4 与 C6-C9

## 接口

### J1 M5Stack_BUS

图中实际连接的 J1 引脚包括 1/3/5=GND、10=GPIO26/S_RST、12=+3.3V、15=GPIO16、16=GPIO17、19=GPIO2/S_PWR、20=GPIO5、21=GPIO12、22=GPIO13、23=GPIO15。

- 参数与网络：`ground=1,3,5`；`reset=10 GPIO26`；`supply=12 +3.3V`；`power_control=19 GPIO2`；`uart_pairs=15/16 GPIO16/GPIO17;21/22 GPIO12/GPIO13;23/20 GPIO15/GPIO5`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C3-C4 J1 外部连线

### U3 Nano-SIM

U3.1=SIM_VCC、U3.2=RST、U3.3=CLK、U3.5=GND、U3.7=IO；RST/CLK/IO 分别经 R12/R14/R15 22Ω 连接 U1.12/U1.13/U1.14，U1.15 提供 SIM_VCC。

- 参数与网络：`U3_1=SIM_VCC`；`U3_2=RST via R12 22Ω to U1.12 SIM_RST`；`U3_3=CLK via R14 22Ω to U1.13 SIM_CLK`；`U3_5=GND`；`U3_7=IO via R15 22Ω to U1.14 SIM_DATA`；`supply_source=U1.15 SIM_VCC`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B1-B2 U3、R12/R14/R15 与 U1.12-U1.15

## 总线

### M5311 主 UART

U1 UART1_TXD/UART1_RXD 引脚 9/10 分别经 U4 A1/A2 转换到 3.3V 侧 U1_T/U1_R；模块 TXD 路径指向主机，模块 RXD 路径接收主机信号。

- 参数与网络：`module_tx=U1.9 UART1_TXD -> U4.A1 -> U4.B1 U1_T`；`module_rx=U1.10 UART1_RXD -> U4.A2 <- U4.B2 U1_R`；`module_level=1.8V`；`host_level=3.3V`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B2-C3 U1 UART1 与 U4 A1/A2/B1/B2

### M5311 未接外设总线

U1 SPI_SS/SPI_MISO/SPI_MOSI/SPI_SCLK 引脚 3-6 均标未连接；IIC_SCL/IIC_SDA 引脚 36/37 以及 GPIO0/GPIO1、ADC、SIM_DET 也未在本页连接外部器件。

- 参数与网络：`spi=U1.3-U1.6 NC`；`i2c=U1.36/U1.37 NC`；`gpio=U1.34/U1.35 NC`；`adc=U1.38 NC`；`sim_det=U1.11 NC`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B2-C3 U1 未连接引脚叉号

## GPIO 与控制信号

### U1_T/U1_R UART 选择

U1_T 可经 R16/R18/R19 三个 0Ω 电阻到 GPIO16/GPIO12/GPIO15，U1_R 可经 R20/R21/R22 三个 0Ω 电阻到 GPIO17/GPIO5/GPIO13。

- 参数与网络：`U1_T=R16->GPIO16,R18->GPIO12,R19->GPIO15`；`U1_R=R20->GPIO17,R21->GPIO5,R22->GPIO13`；`resistance=0Ω`；`pairs=GPIO16/17,GPIO12/13,GPIO15/5`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C3 R16/R18/R19/R20/R21/R22

### S_PWR/PWR_KEY

J1.19 GPIO2 与 S1 输出共同连接 S_PWR；S_PWR 经 R9 1K 驱动 Q4，Q4 导通时把 U1.19 PWR_KEY 拉低，R10 10K 将 S_PWR 下拉。

- 参数与网络：`host_pin=J1.19 GPIO2`；`button=S1 +3.3V -> S_PWR`；`base_resistor=R9 1K`；`pulldown=R10 10K`；`transistor=Q4 SS8050 Y1`；`module_pin=U1.19 PWR_ON/OFF PWR_KEY`；`active_host_level=high`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3-B4 S1、Q4 与 J1.19

## 时钟

### 外部时钟

完整原理图页未显示晶振、振荡器或外部时钟连接，时钟位于 M5311 模组内部的具体实现不在该页展开。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`external_clock_net_shown=false`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页完整图无 Y/X 晶振或 CLK 网络

## 复位

### S_RST/RST

J1.10 GPIO26 经 R17 0Ω 形成 S_RST；S_RST 经 R3 1K 驱动 Q1，Q1 导通时把 U1.17 RESET/RST 拉低，R6 10K 下拉 S_RST，C1 100nF 对 RST 滤波。

- 参数与网络：`host_pin=J1.10 GPIO26`；`jumper=R17 0Ω`；`base_resistor=R3 1K`；`pulldown=R6 10K`；`transistor=Q1 SS8050 Y1`；`module_pin=U1.17 RESET`；`capacitor=C1 100nF`；`active_host_level=high`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 A4-C4 Q1、R17 与 J1.10

## 保护电路

### SIM 信号保护与滤波

U2 SMF05CT1G 跨接在 SIM 接口网络；SIM_VCC 由 C2 100nF 去耦，SIM_DATA/SIM_CLK/SIM_RST 路径配置 C3/C4/C5 各 33pF 对地，并有 R15/R14/R12 各 22Ω 串阻。

- 参数与网络：`tvs=U2 SMF05CT1G`；`supply_decoupling=C2 100nF`；`signal_capacitors=C3,C4,C5 33pF`；`series_resistors=R12,R14,R15 22Ω`；`protected_interface=SIM`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B1-B2 U2/U3 SIM 网络

## 内存与 Flash

### 外部存储器

完整原理图页未展示独立 Flash、EEPROM、RAM、SD 卡或其他存储器器件。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页完整图无外部存储器

## 射频

### M5311 RF 输出

U1.27 RF 节点分为两路：经 R11 0Ω 到 E1 Antenna，经 R13 0Ω 到 E2 ANT_IPEX。

- 参数与网络：`module_pin=U1.27 RF`；`onboard_path=R11 0Ω -> E1 Antenna`；`external_path=R13 0Ω -> E2 ANT_IPEX`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3 U1.27、R11/R13、E1/E2

## 调试与烧录

### M5311 调试 UART

U1.1 DBG_TXD 与 U1.2 DBG_RXD 经 U4 A4/A3 转换为 3.3V 侧 DBG_T/DBG_R；当前页没有画出 DBG_T/DBG_R 的外部连接器。

- 参数与网络：`debug_tx=U1.1 DBG_TXD -> U4.A4 -> U4.B4 DBG_T`；`debug_rx=U1.2 DBG_RXD -> U4.A3 <- U4.B3 DBG_R`；`external_connector_shown=false`
- 证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B2-C3 DBG_TXD/DBG_RXD 与 U4 A3/A4/B3/B4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module NBIoT | `modem=U1 M5311`；`sim=U3`；`level_shifter=U4 TXS0104E`；`host=J1 M5Stack_BUS`；`rf=E1/E2`；`indicators=D1/D2` |
| 电源 | M5311 VBAT 电源 | `u1_pins=31,32`；`rail=VBAT/+3.3V`；`bulk=C10 100uF`；`decoupling=C11 100nF,C12 33pF,C13 10pF`；`regulator_shown=false` |
| 电源 | M5311 VDD_EXT | `source=U1.20 VDD_EXT`；`rail=+1.8V`；`u4_vcca=+1.8V`；`u4_oe=+1.8V`；`u4_vccb=+3.3V`；`capacitors=C6 4.7uF,C7/C8/C9 100nF` |
| 总线 | M5311 主 UART | `module_tx=U1.9 UART1_TXD -> U4.A1 -> U4.B1 U1_T`；`module_rx=U1.10 UART1_RXD -> U4.A2 <- U4.B2 U1_R`；`module_level=1.8V`；`host_level=3.3V` |
| 接口 | J1 M5Stack_BUS | `ground=1,3,5`；`reset=10 GPIO26`；`supply=12 +3.3V`；`power_control=19 GPIO2`；`uart_pairs=15/16 GPIO16/GPIO17;21/22 GPIO12/GPIO13;23/20 GPIO15/GPIO5` |
| GPIO 与控制信号 | U1_T/U1_R UART 选择 | `U1_T=R16->GPIO16,R18->GPIO12,R19->GPIO15`；`U1_R=R20->GPIO17,R21->GPIO5,R22->GPIO13`；`resistance=0Ω`；`pairs=GPIO16/17,GPIO12/13,GPIO15/5` |
| 其他事实 | UART 0Ω 装配状态 | `documented_default=GPIO16/GPIO17`；`schematic_options=GPIO16/17,GPIO12/13,GPIO15/5`；`bom_population=null`；`dnp_marking_shown=false` |
| GPIO 与控制信号 | S_PWR/PWR_KEY | `host_pin=J1.19 GPIO2`；`button=S1 +3.3V -> S_PWR`；`base_resistor=R9 1K`；`pulldown=R10 10K`；`transistor=Q4 SS8050 Y1`；`module_pin=U1.19 PWR_ON/OFF PWR_KEY`；`active_host_level=high` |
| 复位 | S_RST/RST | `host_pin=J1.10 GPIO26`；`jumper=R17 0Ω`；`base_resistor=R3 1K`；`pulldown=R6 10K`；`transistor=Q1 SS8050 Y1`；`module_pin=U1.17 RESET`；`capacitor=C1 100nF`；`active_host_level=high` |
| 接口 | U3 Nano-SIM | `U3_1=SIM_VCC`；`U3_2=RST via R12 22Ω to U1.12 SIM_RST`；`U3_3=CLK via R14 22Ω to U1.13 SIM_CLK`；`U3_5=GND`；`U3_7=IO via R15 22Ω to U1.14 SIM_DATA`；`supply_source=U1.15 SIM_VCC` |
| 保护电路 | SIM 信号保护与滤波 | `tvs=U2 SMF05CT1G`；`supply_decoupling=C2 100nF`；`signal_capacitors=C3,C4,C5 33pF`；`series_resistors=R12,R14,R15 22Ω`；`protected_interface=SIM` |
| 射频 | M5311 RF 输出 | `module_pin=U1.27 RF`；`onboard_path=R11 0Ω -> E1 Antenna`；`external_path=R13 0Ω -> E2 ANT_IPEX` |
| 射频 | 射频支路装配选择 | `documented_default=E1 onboard antenna`；`alternate=E2 ANT_IPEX`；`R11=0Ω`；`R13=0Ω`；`bom_population=null` |
| 核心器件 | D1/D2 指示灯 | `blue=U1.21 STATE -> R4/Q2 -> D1, R1 1K`；`green=U1.16 WAKEUP_OUT -> R5/Q3 -> D2, R2 1K`；`base_pulldowns=R7,R8 10K`；`transistors=Q2,Q3 SS8050 Y1` |
| 调试与烧录 | M5311 调试 UART | `debug_tx=U1.1 DBG_TXD -> U4.A4 -> U4.B4 DBG_T`；`debug_rx=U1.2 DBG_RXD -> U4.A3 <- U4.B3 DBG_R`；`external_connector_shown=false` |
| 总线 | M5311 未接外设总线 | `spi=U1.3-U1.6 NC`；`i2c=U1.36/U1.37 NC`；`gpio=U1.34/U1.35 NC`；`adc=U1.38 NC`；`sim_det=U1.11 NC` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`external_clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |
| 其他事实 | 正文无线能力与控制时序 | `documented_category=LTE Cat NB2`；`documented_bands=B3,B5,B8`；`documented_power_on=GPIO2 high 2s`；`documented_power_off=GPIO2 high 8s`；`documented_reset=GPIO26 high`；`schematic_confirms_timing=false` |

## 待确认事项

- `other.uart-population`：原理图把六个 UART 配置电阻都标为 0Ω，无法仅凭该页确认量产板默认装配哪一组，以及未选通路径是否为 DNP；正文把 GPIO16/GPIO17 描述为默认 UART。（证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 C3 UART 0Ω 跳线矩阵均无 DNP 标记）
- `rf.antenna-population`：R11 与 R13 在原理图上均标 0Ω，正文说明默认板载天线并可跳线切换 IPEX；该页无法确认实际 BOM 是否只装其中一路。（证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 B3 两个 RF 0Ω 支路均无 DNP 标记）
- `other.documented-radio-timing`：正文列出 LTE Cat NB2、B3/B5/B8、GPIO2 高电平 2s 开机/8s 关机和 GPIO26 高电平复位；原理图只确认对应控制电路，不能确认协议能力、频段和固件时序。（证据：图 1a5aa1ebaba6 / 第 1 页 / 第 1 页 S_PWR/S_RST 控制电路无频段、协议或时序标注）
- `review.uart-population`：请依据 v1.0/V1.0 量产 BOM 或 PCB 确认 R16/R18/R19/R20/R21/R22 的默认装配组合。；原因：原理图六个电阻均标 0Ω 且无 DNP 状态，无法唯一确定默认 UART GPIO 对。
- `review.antenna-population`：请依据量产 BOM 或 PCB 确认 R11/R13 的互斥装配状态及默认天线路径。；原因：原理图两条 RF 支路均标 0Ω，但正文描述为可选天线。
- `review.radio-timing`：请通过 M5311 具体料号资料和固件确认 LTE 类别、B3/B5/B8 频段以及 GPIO2/GPIO26 控制时序。；原因：这些参数来自产品正文，原理图只显示电气控制路径。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1a5aa1ebaba6496c03f1896b3c46f9cafb7f3934fe9be5784e4988c3cf9d3207` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/955/M028-module_nb_iot_sch_page_01.png` |

---

源文档：`zh_CN/module/nb-iot.md`

源文档 SHA-256：`a331414a83ca6c9b5a88675b19d82fcfd115cd836195ab235123bff8972892ba`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
