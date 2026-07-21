# Base LAN v1.2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base LAN v1.2 |
| SKU | K012-B-V12 |
| 产品 ID | `base-lan-v1-2-1fe11278dc70` |
| 源文档 | `zh_CN/base/lan_v12.md` |

## 概述

Base LAN v1.2 的本地单页原理图以 U3 W5500 为以太网控制器，通过 M5Stack_BUS 的 GPIO23、GPIO19、GPIO18、GPIO26 构成 SPI，并使用 GPIO13 复位和 GPIO34 中断。W5500 使用 25MHz 晶振，TX/RX 差分线连接 U4 HR911105A 集成磁性器件 RJ45，LINKLED/ACTLED 同样接入该连接器。外部 IN12/24V 经 F1 PPTC 和 U2 TPS54360 降压为 +5V，再由 U1 SPX3819M5-L-3-3 生成 D3V3，并通过 R1/R3 分隔 A3V3/AGND；P2 扩展和配套 RS232/RS485 子板连接未在本页展开。

## 检索关键词

`Base LAN v1.2`、`K012-B-V12`、`W5500`、`TPS54360`、`SPX3819M5-L-3-3`、`HR911105A`、`M5Stack_BUS`、`SPI`、`MOSI GPIO23`、`MISO GPIO19`、`SCLK GPIO18`、`SCSn GPIO26`、`RSTn GPIO13`、`INTn GPIO34`、`25MHz`、`TXP`、`TXN`、`RXP`、`RXN`、`LINKLED`、`ACTLED`、`IN12/24V`、`+5V`、`D3V3`、`A3V3`、`GND`、`AGND`、`PPTC-1812`、`B290B`、`IIC_socket_4P`、`HDR_6P`、`HPWR`、`BATTERY`、`RS485`、`RS232`、`RJ45`、`PWR3.5`、`PMODE`、`EXRES1`、`LAN_W5500`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | W5500 | SPI 以太网控制器，连接 M5-Bus、PHY 差分线、25MHz 时钟、复位、中断和状态 LED | 图 c7e3400b1b74 / 第 1 页 / 网格 B2-D3：U3 W5500 48 脚方框及 TX/RX、SPI、XI/XO、RSTn、INTn、LED 引脚 |
| U4 | HR911105A | 带隔离磁性器件和 LINK/ACT LED 的 RJ45 以太网连接器 | 图 c7e3400b1b74 / 第 1 页 / 网格 C1：U4 HR911105A，TD+/TD-/RD+/RD-、VADD 和 Y/G LED 引脚 |
| U2 | TPS54360 | 将 IN12/24V 降压为 +5V 的开关降压转换器 | 图 c7e3400b1b74 / 第 1 页 / 网格 A1-A3：U2 TPS54360，VIN/BOOT/SW/COMP/FB 与 D1、L1、C1-C3、C8-C10 |
| U1 | SPX3819M5-L-3-3 | 由 +5V 生成 D3V3 的 3.3V LDO | 图 c7e3400b1b74 / 第 1 页 / 网格 A3：U1 SPX3819M5-L-3-3，IN/EN 接 +5V，OUT 接 D3V3 |
| J1 | PWR3.5 | IN12/24V 与 GND 外部直流电源输入连接器 | 图 c7e3400b1b74 / 第 1 页 / 网格 A1：J1 PWR3.5，正输入经 F1 形成 IN+，回路接 GND |
| F1 | PPTC-1812 | 串联在 J1 正电源输入与 IN+ 之间的自恢复保护器件 | 图 c7e3400b1b74 / 第 1 页 / 网格 A1：J1 与 U2 之间 F1 PPTC-1812 |
| D1,L1 | B290B / 8.2uH | TPS54360 降压级的续流二极管与输出电感 | 图 c7e3400b1b74 / 第 1 页 / 网格 A2：U2 SW 节点的 D1 B290B 与串向 +5V 的 L1 8.2uH |
| R1,R3 | 120Ω/MB / 0Ω | 分别连接 D3V3-A3V3 和 GND-AGND 的电源与地分区桥接器件 | 图 c7e3400b1b74 / 第 1 页 / 网格 A3-A4：D3V3-R1 120Ω/MB-A3V3，以及 GND-R3 0Ω-AGND |
| Y1,R20,C14,C17 | 25MHz 12PF 10PPM / 1MΩ / 18pF | W5500 XI/CLKIN 与 XO 的外部晶振、反馈电阻和负载电容网络 | 图 c7e3400b1b74 / 第 1 页 / 网格 C3-D3：XO/XI、Y1 25MHz 12PF 10PPM、R20 1MΩ、C14/C17 18pF |
| R7 | 10KΩ (103) 4P | 配置 W5500 PMODE3-PMODE0 启动模式的四联电阻阵列 | 图 c7e3400b1b74 / 第 1 页 / 网格 B2：U3 上方 R7 四联电阻阵列、D3V3/AGND 与 PMODE3-PMODE0 |
| R8,R13,R16 | 10KΩ | 分别为 W5500 RSTn、INTn 与 SCSn 信号提供 D3V3 上拉 | 图 c7e3400b1b74 / 第 1 页 / 网格 B2-C3：R8 接 RSTn，R13/R16 接 INTn/SCSn，另一端均为 D3V3 |
| R19 | 12.4KΩ | W5500 EXRES1 引脚到 AGND 的外部参考电阻 | 图 c7e3400b1b74 / 第 1 页 / 网格 C2-D2：U3 EXRES1 经 R19 12.4KΩ 接 AGND |
| R10,R11,R12,R17,R18,C11,C14,C15,C16 | 49.9Ω / 6.8nF / 22nF network | W5500 TX/RX 差分线与 HR911105A 之间的偏置、耦合和端接网络 | 图 c7e3400b1b74 / 第 1 页 / 网格 B1-D2：TXP/TXN/RXP/RXN 周围 49.9Ω、6.8nF、22nF 网络 |
| R14,R15 | 1KΩ | HR911105A 集成 LINK/ACT LED 的 D3V3 限流电阻 | 图 c7e3400b1b74 / 第 1 页 / 网格 B1-C1：LINKLED/ACTLED 与 D3V3 之间 R14/R15 1KΩ |
| C13 | 1nF (102) 10% 2000V | HR911105A 屏蔽/机壳相关节点到 GND 的高压电容耦合 | 图 c7e3400b1b74 / 第 1 页 / 网格 C1-D1：U4 pins13/14 区域经 C13 1nF 2000V 接 GND |
| D2,R9 | 红灯 0603 / 4.7KΩ | +5V 电源指示灯及限流电阻 | 图 c7e3400b1b74 / 第 1 页 / 网格 B4：D2 红灯 0603 与 R9 4.7KΩ 串接在 +5V 与 GND 之间 |
| J2 | IIC_Socket_4P | 引出 SCL、SDA、+5V 与 GND 的四针接口 | 图 c7e3400b1b74 / 第 1 页 / 网格 B4-C4：J2 IIC_Socket_4P，pin1 SCL、pin2 SDA、pin3 +5V、pin4 GND |
| J3 | M5Stack_BUS | 30 针主控堆叠总线，承载 W5500 SPI/控制信号和 GND、3.3V、+5V、HPWR、BATTERY 等电源 | 图 c7e3400b1b74 / 第 1 页 / 网格 C4-D4：J3 M5Stack_BUS，1-30 脚及 GPIO、电源网络标注 |
| P2 | HDR_6P | 标为 I/O_01 至 I/O_06 的六针预留接口 | 图 c7e3400b1b74 / 第 1 页 / 网格 A4-B4：P2 HDR_6P，pin1-pin6 分别标 I/O_01-I/O_06，页面未画后续网络 |

## 系统结构

### Base LAN v1.2 系统架构

J1 的 IN12/24V 经 U2 TPS54360 产生 +5V，U1 再产生 D3V3/A3V3；外部 M5 主控通过 J3 的 SPI 和控制 GPIO 驱动 U3 W5500，W5500 的 PHY 差分线最终接入 U4 HR911105A RJ45。

- 参数与网络：`input=J1 IN12/24V`；`buck=U2 TPS54360`；`ldo=U1 SPX3819M5-L-3-3`；`ethernet_controller=U3 W5500`；`ethernet_connector=U4 HR911105A`；`host_connector=J3 M5Stack_BUS`
- 证据：图 c7e3400b1b74 / 第 1 页 / 第 1 页完整单页：上方电源、中央 W5500、左侧 HR911105A、右下 M5Stack_BUS

## 核心器件

### RS-485 与 RS-232 转接板可见性

当前完整单页主板原理图未画出 RS-485 收发器、RS-232 收发器、A/B 差分网络、RS-232 电平转换、终端电阻或方向控制信号；不能从本页确认配套转接板器件和连接。

- 参数与网络：`rs485_transceiver_shown=false`；`rs232_transceiver_shown=false`；`rs485_ab_nets_shown=false`；`termination_shown=false`；`direction_control_shown=false`；`reserved_connector=P2 HDR_6P I/O_01-I/O_06`
- 证据：图 c7e3400b1b74 / 第 1 页 / 第 1 页完整单页器件与网络；仅见 P2 I/O_01-I/O_06，未见 RS485、RS232、A/B、DE/RE

## 电源

### IN12/24V 到 +5V 降压

U2 TPS54360 以 IN+ 为输入，其 SW pin8 连接 D1 B290B 和 L1 8.2uH；L1 后的 +5V 由 C2/C3 各 10uF 滤波，FB pin5 使用 R4 51KΩ 与 R6 10KΩ 分压。

- 参数与网络：`input_net=IN+`；`output_net=+5V`；`switch_pin=U2 pin8 SW`；`freewheel_diode=D1 B290B`；`inductor=L1 8.2uH`；`output_capacitors=C2/C3 10uF`；`feedback=R4 51KΩ; R6 10KΩ`；`enable_pin=U2 pin3 EN shown NC`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 A1-A3：U2、D1/L1/C2/C3/R4/R6，EN pin3 处未连接标记

### TPS54360 自举、补偿与频率网络

U2 BOOT pin1 与 SW pin8 之间连接 C1 100nF；COMP pin6 连接 R2 12KΩ 与 C8 6.8nF 网络，RT/CLK pin4 通过 R5 160KΩ 接 GND。

- 参数与网络：`bootstrap=C1 100nF between BOOT and SW`；`compensation=R2 12KΩ and C8 6.8nF`；`timing=R5 160KΩ from RT/CLK to GND`；`annotation_values=R5 red 162K; R4 red 52.6K`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 A1-A3：U2 周围 C1、R2/C8、R5 及黑色/红色数值标注

### +5V 到 D3V3 LDO

U1 SPX3819M5-L-3-3 的 IN pin1 与 EN pin3 均接 +5V，OUT pin5 输出 D3V3，GND pin2 接 GND，BYP/ADJ pin4 通过 C6 470pF 接 GND；C5/C7 各 100nF 为输入和输出旁路。

- 参数与网络：`input=+5V`；`enable=+5V`；`output=D3V3`；`bypass=C6 470pF`；`input_capacitor=C5 100nF`；`output_capacitors=C7 100nF; C4 100uF`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 A3-A4：U1 SPX3819M5-L-3-3 与 C4-C7

### W5500 A3V3/D3V3 电源分区

U1 输出形成 D3V3，D3V3 经 R1 120Ω/MB 连接 A3V3；数字地 GND 经 R3 0Ω 连接模拟地 AGND。

- 参数与网络：`digital_rail=D3V3/GND`；`analog_rail=A3V3/AGND`；`rail_bridge=R1 120Ω/MB`；`ground_bridge=R3 0Ω`；`bulk_capacitor=C4 100uF`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 A3-A4：D3V3-R1-A3V3、GND-R3-AGND 与 C4

### W5500 去耦

A3V3 侧 C19-C24 均标 100nF 并接 AGND；D3V3 侧 C25 100nF 与 C26 10uF 接 GND，U3 下方 C27 4.7uF 与 C18 10nF 接 AGND。

- 参数与网络：`analog_decoupling=C19-C24 100nF to AGND`；`digital_decoupling=C25 100nF and C26 10uF to GND`；`local_analog=C27 4.7uF and C18 10nF to AGND`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 D1-D3：C19-C27/C18 去耦网络

### +5V 电源指示

D2 红灯 0603 与 R9 4.7KΩ 串联在 +5V 和 GND 之间，用于指示 +5V 电源轨。

- 参数与网络：`rail=+5V`；`led=D2 red 0603`；`resistor=R9 4.7KΩ`；`return=GND`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B4：+5V-D2-R9-GND 串联支路

## 接口

### HR911105A 以太网接口

U4 HR911105A 将 W5500 的 TXP/TXN 与 RXP/RXN 接到其内部发送和接收磁性器件，并集成 LINK 与 ACT 两组 LED；该页没有显示 PoE 取电路径。

- 参数与网络：`connector=U4 HR911105A`；`tx_pair=TD+/TD-`；`rx_pair=RD+/RD-`；`led_signals=LINKLED, ACTLED`；`shield_coupling=C13 1nF 2000V to GND`；`poe_path_shown=false`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B1-D1：U4 HR911105A 完整符号、C13；完整页无 PoE 取电网络

### J2 IIC 四针接口

J2 IIC_Socket_4P 的 pin1=SCL、pin2=SDA、pin3=+5V、pin4=GND；当前页面未画出 SCL/SDA 上拉电阻。

- 参数与网络：`pin1=SCL -> J3 pin18`；`pin2=SDA -> J3 pin17`；`pin3=+5V`；`pin4=GND`；`pullups_shown=false`；`signal_direction=bidirectional bus lines`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B4-C4：J2 pins1-4 与 J3 SDA/SCL 同名网络

### J3 M5Stack_BUS 针脚映射

J3 pin1/3/5 接 GND，pin7/9/11/10 分别为 GPIO23/19/18/26，pin22 GPIO13，pin26 GPIO34，pin17 SDA，pin18 SCL，pin12/14 为 +3.3V/GPIO1，pin25/27/29 为 IN+/HPWR，pin28 +5V，pin30 BATTERY。

- 参数与网络：`ground=pins1,3,5`；`spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18, pin10 GPIO26`；`control=pin22 GPIO13, pin26 GPIO34`；`i2c=pin17 SDA, pin18 SCL`；`power=pin12 +3.3V, pin25 IN+, pins27/29 HPWR, pin28 +5V, pin30 BATTERY`；`other_gpio=pin2 GPIO35,pin4 GPIO36,pin6 EN,pin8 GPIO25,pin13 GPIO3,pin14 GPIO1,pin15 GPIO16,pin16 GPIO17,pin19 GPIO2,pin20 GPIO5,pin21 GPIO12,pin23 GPIO15,pin24 GPIO0`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 C4-D4：J3 M5Stack_BUS pins1-30 及左右网络名

## 总线

### W5500 SPI 主控映射

U3 MOSI pin35 接 GPIO23，MISO pin34 接 GPIO19，SCLK pin33 接 GPIO18，SCSn pin32 接 GPIO26；这些网络均进入 J3 M5Stack_BUS。

- 参数与网络：`controller=external M5Stack host`；`device=U3 W5500`；`mosi=U3 pin35 -> GPIO23 -> J3 pin7`；`miso=U3 pin34 -> GPIO19 -> J3 pin9`；`sclk=U3 pin33 -> GPIO18 -> J3 pin11`；`chip_select=U3 pin32 SCSn -> GPIO26 -> J3 pin10`；`logic_rail=D3V3`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 C3-C4：U3 MOSI/MISO/SCLK/SCSn pins35-32 与 J3 GPIO23/19/18/26

### W5500 PHY 差分对

U3 TXN pin1、TXP pin2、RXN pin5、RXP pin6 分别使用 TXN、TXP、RXN、RXP 网络连接 U4 HR911105A 的 TD-/TD+/RD-/RD+。

- 参数与网络：`transmit=U3 TXN pin1/TXP pin2 -> U4 TD-/TD+`；`receive=U3 RXN pin5/RXP pin6 -> U4 RD-/RD+`；`analog_supply=A3V3/AGND`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B1-C2：U3 TXN/TXP/RXN/RXP pins1/2/5/6 到 U4 TD/RD 引脚

### J2 I2C 总线

J2 引出 J3 的 SCL 与 SDA 两条总线网络并提供 +5V/GND；原理图未显示板载 I2C 从设备或可见地址。

- 参数与网络：`controller=external M5Stack host`；`clock=SCL / J3 pin18`；`data=SDA / J3 pin17`；`connector_supply=+5V`；`onboard_device_shown=false`；`onboard_address_shown=false`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B4-C4：J2 SCL/SDA/+5V/GND 与完整单页，无 I2C 从设备

## GPIO 与控制信号

### W5500 复位、中断和片选映射

U3 RSTn pin37 接 GPIO13，INTn pin36 接 GPIO34，SCSn pin32 接 GPIO26；R8、R13、R16 各 10KΩ 将三条信号上拉到 D3V3。

- 参数与网络：`reset=U3 pin37 RSTn -> GPIO13 -> J3 pin22`；`interrupt=U3 pin36 INTn -> GPIO34 -> J3 pin26`；`chip_select=U3 pin32 SCSn -> GPIO26 -> J3 pin10`；`pullups=R8/R13/R16 10KΩ to D3V3`；`active_low=RSTn, INTn, SCSn`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B2-C4：U3 RSTn/INTn/SCSn、GPIO13/34/26、R8/R13/R16 与 J3

### W5500 PMODE 配置

U3 PMODE2、PMODE1、PMODE0 通过 R7 的 10KΩ 支路上拉到 D3V3，PMODE3 侧连接到 AGND。

- 参数与网络：`high_straps=PMODE2, PMODE1, PMODE0 via R7 10KΩ to D3V3`；`low_strap=PMODE3 to AGND`；`array=R7 10KΩ (103) 4P`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B2：U3 PMODE3-PMODE0 与 R7、D3V3、AGND 连线

### 以太网链路和活动指示

U3 LINKLED pin25 接 U4 LINKLED，ACTLED pin27 接 U4 ACTLED；U4 LED 另一侧通过 R14/R15 1KΩ 接 D3V3，DUPLED pin26 标记未连接。

- 参数与网络：`link=U3 pin25 LINKLED -> U4 pin11`；`activity=U3 pin27 ACTLED -> U4 pin10`；`led_resistors=R14/R15 1KΩ to D3V3`；`duplex_led=U3 pin26 DUPLED shown NC`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B1-C3：U3 LINKLED/ACTLED/DUPLED 与 U4 LED、R14/R15

## 时钟

### W5500 外部时钟

U3 XO pin31 与 XI/CLKIN pin30 连接 Y1 25MHz 12PF 10PPM 晶振，R20 1MΩ 跨接两端，C14/C17 各 18pF 接 GND。

- 参数与网络：`frequency=25MHz`；`crystal=Y1 25MHz 12PF 10PPM`；`pins=XO pin31; XI/CLKIN pin30`；`feedback_resistor=R20 1MΩ`；`load_capacitors=C14/C17 18pF`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 C3-D3：U3 XO/XI 与 Y1/R20/C14/C17

## 复位

### W5500 硬件复位路径

W5500 RSTn 由 J3 pin22 的 GPIO13 驱动，并由 R8 10KΩ 保持 D3V3 上拉；当前页面未画出独立复位按钮。

- 参数与网络：`device_pin=U3 pin37 RSTn`；`host_gpio=GPIO13 / J3 pin22`；`pullup=R8 10KΩ to D3V3`；`reset_switch_shown=false`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B2-C4：U3 RSTn 到 GPIO13/R8/J3 pin22，完整页无复位开关

## 保护电路

### 外部直流输入保护

J1 正输入先串联 F1 PPTC-1812 后形成 IN+，C9/C10 各 2.2uF 从 IN+ 接 GND，再进入 U2 VIN。

- 参数与网络：`connector=J1 PWR3.5`；`positive_path=J1 -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C9/C10 2.2uF`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 A1：J1、F1、IN+、C9/C10 与 U2 VIN

## 存储

### 板载存储

当前完整单页原理图未画出 Flash、PSRAM、EEPROM、SD 卡或其他板载存储器件。

- 参数与网络：`flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`sd_card_shown=false`
- 证据：图 c7e3400b1b74 / 第 1 页 / 第 1 页完整单页：U1-U4 为电源、W5500 和 HR911105A，未见存储器件

## 调试与烧录

### 调试接口

当前完整单页原理图未画出 JTAG、SWD、USB-UART 或专用编程调试连接器。

- 参数与网络：`jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`dedicated_debug_connector_shown=false`
- 证据：图 c7e3400b1b74 / 第 1 页 / 第 1 页完整单页连接器 J1/J2/J3/P2，未见 JTAG、SWD、USB-UART

## 模拟电路

### W5500 EXRES1 外部电阻

U3 EXRES1 pin10 通过 R19 12.4KΩ 连接 AGND。

- 参数与网络：`pin=U3 pin10 EXRES1`；`resistor=R19 12.4KΩ`；`reference_ground=AGND`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 C2-D2：U3 EXRES1 pin10 经 R19 12.4KΩ 到 AGND

### W5500 与 HR911105A 模拟接口

TXP/TXN 使用 A3V3 侧 49.9Ω 偏置网络连接 U4 发送绕组；RXP/RXN 通过 C11/C14 6.8nF 串联电容及 R17/R18 49.9Ω、C15 22nF/C16 10nF 网络连接 U4 接收绕组。

- 参数与网络：`tx_bias=R10 10Ω and R11/R12 49.9Ω to A3V3`；`rx_series_capacitors=C11/C14 6.8nF`；`rx_resistors=R17/R18 49.9Ω`；`rx_capacitors=C15 22nF; C16 10nF`
- 证据：图 c7e3400b1b74 / 第 1 页 / 网格 B1-D2：U3/U4 之间 R10-R12、C11/C14、R17/R18、C15/C16

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base LAN v1.2 系统架构 | `input=J1 IN12/24V`；`buck=U2 TPS54360`；`ldo=U1 SPX3819M5-L-3-3`；`ethernet_controller=U3 W5500`；`ethernet_connector=U4 HR911105A`；`host_connector=J3 M5Stack_BUS` |
| 保护电路 | 外部直流输入保护 | `connector=J1 PWR3.5`；`positive_path=J1 -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C9/C10 2.2uF` |
| 电源 | IN12/24V 到 +5V 降压 | `input_net=IN+`；`output_net=+5V`；`switch_pin=U2 pin8 SW`；`freewheel_diode=D1 B290B`；`inductor=L1 8.2uH`；`output_capacitors=C2/C3 10uF`；`feedback=R4 51KΩ; R6 10KΩ`；`enable_pin=U2 pin3 EN shown NC` |
| 电源 | TPS54360 自举、补偿与频率网络 | `bootstrap=C1 100nF between BOOT and SW`；`compensation=R2 12KΩ and C8 6.8nF`；`timing=R5 160KΩ from RT/CLK to GND`；`annotation_values=R5 red 162K; R4 red 52.6K` |
| 电源 | +5V 到 D3V3 LDO | `input=+5V`；`enable=+5V`；`output=D3V3`；`bypass=C6 470pF`；`input_capacitor=C5 100nF`；`output_capacitors=C7 100nF; C4 100uF` |
| 电源 | W5500 A3V3/D3V3 电源分区 | `digital_rail=D3V3/GND`；`analog_rail=A3V3/AGND`；`rail_bridge=R1 120Ω/MB`；`ground_bridge=R3 0Ω`；`bulk_capacitor=C4 100uF` |
| 电源 | W5500 去耦 | `analog_decoupling=C19-C24 100nF to AGND`；`digital_decoupling=C25 100nF and C26 10uF to GND`；`local_analog=C27 4.7uF and C18 10nF to AGND` |
| 总线 | W5500 SPI 主控映射 | `controller=external M5Stack host`；`device=U3 W5500`；`mosi=U3 pin35 -> GPIO23 -> J3 pin7`；`miso=U3 pin34 -> GPIO19 -> J3 pin9`；`sclk=U3 pin33 -> GPIO18 -> J3 pin11`；`chip_select=U3 pin32 SCSn -> GPIO26 -> J3 pin10`；`logic_rail=D3V3` |
| GPIO 与控制信号 | W5500 复位、中断和片选映射 | `reset=U3 pin37 RSTn -> GPIO13 -> J3 pin22`；`interrupt=U3 pin36 INTn -> GPIO34 -> J3 pin26`；`chip_select=U3 pin32 SCSn -> GPIO26 -> J3 pin10`；`pullups=R8/R13/R16 10KΩ to D3V3`；`active_low=RSTn, INTn, SCSn` |
| 复位 | W5500 硬件复位路径 | `device_pin=U3 pin37 RSTn`；`host_gpio=GPIO13 / J3 pin22`；`pullup=R8 10KΩ to D3V3`；`reset_switch_shown=false` |
| GPIO 与控制信号 | W5500 PMODE 配置 | `high_straps=PMODE2, PMODE1, PMODE0 via R7 10KΩ to D3V3`；`low_strap=PMODE3 to AGND`；`array=R7 10KΩ (103) 4P` |
| 时钟 | W5500 外部时钟 | `frequency=25MHz`；`crystal=Y1 25MHz 12PF 10PPM`；`pins=XO pin31; XI/CLKIN pin30`；`feedback_resistor=R20 1MΩ`；`load_capacitors=C14/C17 18pF` |
| 模拟电路 | W5500 EXRES1 外部电阻 | `pin=U3 pin10 EXRES1`；`resistor=R19 12.4KΩ`；`reference_ground=AGND` |
| 总线 | W5500 PHY 差分对 | `transmit=U3 TXN pin1/TXP pin2 -> U4 TD-/TD+`；`receive=U3 RXN pin5/RXP pin6 -> U4 RD-/RD+`；`analog_supply=A3V3/AGND` |
| 模拟电路 | W5500 与 HR911105A 模拟接口 | `tx_bias=R10 10Ω and R11/R12 49.9Ω to A3V3`；`rx_series_capacitors=C11/C14 6.8nF`；`rx_resistors=R17/R18 49.9Ω`；`rx_capacitors=C15 22nF; C16 10nF` |
| 接口 | HR911105A 以太网接口 | `connector=U4 HR911105A`；`tx_pair=TD+/TD-`；`rx_pair=RD+/RD-`；`led_signals=LINKLED, ACTLED`；`shield_coupling=C13 1nF 2000V to GND`；`poe_path_shown=false` |
| GPIO 与控制信号 | 以太网链路和活动指示 | `link=U3 pin25 LINKLED -> U4 pin11`；`activity=U3 pin27 ACTLED -> U4 pin10`；`led_resistors=R14/R15 1KΩ to D3V3`；`duplex_led=U3 pin26 DUPLED shown NC` |
| 接口 | J2 IIC 四针接口 | `pin1=SCL -> J3 pin18`；`pin2=SDA -> J3 pin17`；`pin3=+5V`；`pin4=GND`；`pullups_shown=false`；`signal_direction=bidirectional bus lines` |
| 总线 | J2 I2C 总线 | `controller=external M5Stack host`；`clock=SCL / J3 pin18`；`data=SDA / J3 pin17`；`connector_supply=+5V`；`onboard_device_shown=false`；`onboard_address_shown=false` |
| 接口 | J3 M5Stack_BUS 针脚映射 | `ground=pins1,3,5`；`spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18, pin10 GPIO26`；`control=pin22 GPIO13, pin26 GPIO34`；`i2c=pin17 SDA, pin18 SCL`；`power=pin12 +3.3V, pin25 IN+, pins27/29 HPWR, pin28 +5V, pin30 BATTERY`；`other_gpio=pin2 GPIO35,pin4 GPIO36,pin6 EN,pin8 GPIO25,pin13 GPIO3,pin14 GPIO1,pin15 GPIO16,pin16 GPIO17,pin19 GPIO2,pin20 GPIO5,pin21 GPIO12,pin23 GPIO15,pin24 GPIO0` |
| 接口 | P2 六针 I/O 接口 | `pin1=I/O_01`；`pin2=I/O_02`；`pin3=I/O_03`；`pin4=I/O_04`；`pin5=I/O_05`；`pin6=I/O_06`；`destination_shown=false` |
| 核心器件 | RS-485 与 RS-232 转接板可见性 | `rs485_transceiver_shown=false`；`rs232_transceiver_shown=false`；`rs485_ab_nets_shown=false`；`termination_shown=false`；`direction_control_shown=false`；`reserved_connector=P2 HDR_6P I/O_01-I/O_06` |
| 电源 | HPWR 与外部输入关系 | `j3_pin25=IN+`；`j3_pins27_29=HPWR`；`external_input=J1 -> F1 -> IN+`；`explicit_hpwr_bridge_shown=false` |
| 电源 | +5V 电源指示 | `rail=+5V`；`led=D2 red 0603`；`resistor=R9 4.7KΩ`；`return=GND` |
| 存储 | 板载存储 | `flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`sd_card_shown=false` |
| 调试与烧录 | 调试接口 | `jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`dedicated_debug_connector_shown=false` |
| 其他事实 | v1.2 产品与 V1.0 图纸修订对应关系 | `product_name=Base LAN v1.2`；`sku=K012-B-V12`；`schematic_project=LAN_W5500`；`schematic_revision=V1.0`；`schematic_date=07/30/2018`；`v12_alignment_confirmed=false` |
| 电源 | 外部输入电压范围 | `documented_range=9-24V`；`schematic_label=IN12/24V`；`minimum_input_confirmed=false`；`reverse_polarity_protection_shown=false`；`continuous_power=null` |
| 其他事实 | 以太网速率与协议能力 | `documented_port=RJ45 adaptive 10/100M`；`documented_protocols=TCP,UDP,IPv4,ICMP,ARP,IGMP,PPPoE`；`schematic_controller=U3 W5500`；`firmware_version=null`；`measured_throughput=null` |

## 待确认事项

- `interface.io-header-unresolved-routing`：P2 HDR_6P 的 pin1-pin6 仅标为 I/O_01-I/O_06，当前原理图页面没有显示它们连接到 J3 GPIO、RS-485/RS-232 子板或其他网络。（证据：图 c7e3400b1b74 / 第 1 页 / 网格 A4-B4：P2 HDR_6P，I/O_01-I/O_06 均为短引线，未连接命名网络）
- `power.hpwr-input-relationship`：J3 pin25 明确接 IN+，pins27/29 标为 HPWR；当前页面未显示 HPWR 与 IN+ 之间的同名网络连接或桥接器件。（证据：图 c7e3400b1b74 / 第 1 页 / 网格 A1 与 D4：J1/IN+ 及 J3 pins25/27/29 IN+/HPWR）
- `other.schematic-revision-alignment`：产品清单名称为 Base LAN v1.2、SKU 为 K012-B-V12，但本地原理图标题栏标注 Project LAN_W5500、Revised V1.0、Date 07/30/2018；该页是否精确对应 v1.2 量产硬件无法由页面本身确认。（证据：图 c7e3400b1b74 / 第 1 页 / 网格 D3-D4 标题栏：Project Title LAN_W5500.PrjPCB、Revised V1.0、Date 07/30/2018）
- `power.documented-input-range`：产品正文写支持 9-24V 输入，原理图页面只标 IN12/24V，且 F1 与 TPS54360 电路未给出整机最低输入、容差、反接保护和持续功率边界。（证据：图 c7e3400b1b74 / 第 1 页 / 网格 A1-A3：IN12/24V、J1/F1、TPS54360 电源级，图中无 9V 或整机功率说明）
- `other.documented-network-capabilities`：产品正文列出 RJ45 自适应 10/100M 以及 TCP、UDP、IPv4、ICMP、ARP、IGMP、PPPoE 等协议；原理图只确认 W5500 与物理接口，无法验证固件配置、吞吐量、缓存使用和整机协议行为。（证据：图 c7e3400b1b74 / 第 1 页 / 第 1 页 U3 W5500、U4 HR911105A 与 SPI，图中无协议、速率或吞吐参数表）
- `review.io-header-routing`：P2 的 I/O_01-I/O_06 在 PCB 或配套 TTL-RS485/TTL-RS232 转接板上分别连接哪些 M5-Bus GPIO、供电和串行信号？；原因：当前原理图只显示 P2 引脚标签，没有网络去向或转接板原理图。
- `review.hpwr-input-relationship`：J3 pins27/29 的 HPWR 是否在 PCB 上连接 J1/F1 后的 IN+，或通过未画出的电源选择路径连接？；原因：J3 pin25 明确为 IN+，pins27/29 另标 HPWR，页面没有桥接关系。
- `review.schematic-revision`：标题栏 Revised V1.0 的 LAN_W5500 图纸是否就是 K012-B-V12 的正式 v1.2 量产原理图？；原因：产品版本和图纸修订号不一致，需要正式版本记录、BOM 或 PCB 文件闭环。
- `review.input-voltage-range`：K012-B-V12 的认证输入范围究竟是 9-24V 还是图纸标注的 12/24V，最低启动电压、容差和持续功率是多少？；原因：正文与图纸标注不同，且原理图不能证明整机工作边界。
- `review.network-capabilities`：v1.2 当前固件和整机测试确认的端口速率、协议集、缓存配置与持续吞吐量分别是什么？；原因：这些是控制器配置和系统性能，单页连接原理图无法验证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c7e3400b1b74c358c88209600540088198a85d7b08c653547a017b5bff3cf603` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/lan_base_page_01.png` |

---

源文档：`zh_CN/base/lan_v12.md`

源文档 SHA-256：`e8476c171530aea70414961fe526a99eb2edbd3f1e495829e8a544ecdf95634c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
