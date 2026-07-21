# Base LAN PoE v1.2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base LAN PoE v1.2 |
| SKU | K012-C-V12 |
| 产品 ID | `base-lan-poe-v1-2-0c51709f4a9c` |
| 源文档 | `zh_CN/base/lan_poe_v12.md` |

## 概述

Base LAN PoE v1.2 主板以 U3 W5500 为以太网控制器，通过 M5Stack_BUS 的 GPIO23/GPIO19/GPIO18/GPIO26 使用 SPI，并由 GPIO13 复位、GPIO34 接收中断；25MHz 晶振和 U4 HBJ-6308ANLF 磁性 RJ45 构成 PHY 接口。J1 外部输入或 P3 的 PoE 子板输出经 F1、U2 MP1584EN 生成 +5V，再由 U1 SPX3819M5-L-3-3 生成 D3V3/A3V3。其余三页分别给出 CA-IS3050G 隔离 CAN、MAX232ESE RS232 和 SP485EEN-L/TR RS485 转接板，其中 CAN 与 RS485 带明确的多级保护。资源未展示 PoE 高压受电前端，且不能确认三种转接板的实际装配组合和正文所列协议性能。

## 检索关键词

`Base LAN PoE v1.2`、`K012-C-V12`、`W5500`、`MP1584EN`、`SPX3819M5-L-3-3`、`HBJ-6308ANLF`、`M5Stack_BUS`、`SPI`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO26`、`GPIO13`、`GPIO34`、`25MHz`、`TXP`、`TXN`、`RXP`、`RXN`、`LINKLED`、`ACTLED`、`IN12/24V`、`IN+`、`+5V`、`D3V3`、`A3V3`、`PPTC-1812`、`PoE`、`P3 HDR_6P`、`CA-IS3050G`、`B0505S-1W`、`CAN_H`、`CAN_L`、`MAX232ESE`、`RS232_T`、`RS232_R`、`SP485EEN-L/TR`、`RS485_A`、`RS485_B`、`P6SMB6.8CA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 (主板) | W5500 | SPI 以太网控制器，连接 M5-Bus、PHY 差分线、25MHz 时钟、复位、中断和状态 LED | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页中央 U3 W5500，48 脚符号及 TX/RX、SPI、XI/XO、RSTn、INTn、LED 引脚 |
| U4 (主板) | HBJ-6308ANLF | 带隔离磁性器件和 LINK/ACT LED 的 RJ45 以太网连接器 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左中 U4 HBJ-6308ANLF，TD+/TD-/RD+/RD-、VC/VC2 中心抽头和 Y/G LED 引脚 |
| U2 (主板) | MP1584EN | 将 IN+ 降压为 +5V 的开关降压转换器 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左上 U2 MP1584EN，VIN/BST/SW/FB/FREQ/COMP 与 D1/L1 |
| U1 (主板) | SPX3819M5-L-3-3 | 由 +5V 生成 D3V3 的 3.3V LDO | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页上中 U1 SPX3819M5-L-3-3，IN/EN 接 +5V、OUT 接 D3V3 |
| J1,F1 | PWR3.5 / PPTC-1812 | 外部 IN12/24V 输入连接器及串联自恢复保护器件 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左上 J1 PWR3.5、INF+、F1 PPTC-1812、IN+ 与 GND |
| P3,D3 | HDR_6P / SS54 | 接收 RJ45 中心抽头网络及外部 PoE 子板 VOUT/GND，并经 D3 汇入 INF+ | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左中 P3 HDR_6P，VC2+/VC2-/VC+/VC-/GND/VOUT 与 D3 SS54、INF+ |
| D1,L1 | SS54 / 10uH | MP1584EN 降压级的续流二极管与输出电感 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U2 右侧 D1 SS54、L1 10uH 与 +5V |
| Y1,R20,C14,C17 | 25MHz 12PF 10PPM / 1MΩ / 18pF | W5500 外部晶振、反馈电阻和负载电容网络 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 右下 XO/XI：Y1 25MHz 12PF 10PPM、R20 1MΩ、C14/C17 18pF |
| J3,J4 | M5Stack_BUS | 30 针主控堆叠总线，承载 W5500 SPI/控制、扩展 UART 和电源网络 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右下 J3/J4 M5Stack_BUS，pin1-pin30 |
| J2 (主板) | Header 4 | 引出 GPIO5 RX、GPIO15 TX、+5V 与 GND 的转接板接口 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右中 J2 Header 4，RX/TX/VCC/GND 对应 GPIO5/GPIO15/+5V/GND |
| P2 (主板) | HDR_6P | I/O_01 至 I/O_06 的六针预留焊盘 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右上 P2 HDR_6P，pin1-pin6 标 I/O_01-I/O_06 |
| D2,R9 (主板) | 红灯 0603 / 4.7KΩ | +5V 电源指示灯与限流电阻 | 图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右上 D2 红灯 0603、R9 4.7KΩ，跨接 +5V 与 GND |
| U2 (CAN板) | CA-IS3050G | 3.3V 逻辑侧至隔离 CANH/CANL 总线侧的收发器 | 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页左下 U2 CA-IS3050G，VCC1/RXD/TXD/GND1 与 VCC2/CANH/CANL/GND2 |
| U1 (CAN板) | B0505S-1W | 把 +5VIN/GND 隔离转换为 +S5V/SGND | 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页左中 U1 B0505S-1W，+Vin/-Vin/+Vout/-Vout |
| U3 (CAN板) | HT7533 | 由 +5VIN 生成 +3.3V 的逻辑侧稳压器 | 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页左中 U3 HT7533，VIN +5VIN、VOUT +3.3V、GND |
| DZ1,DZ2,TSS1,TSS2,TSS3,F1,F2,GDT1,GDT2 | PESD5V0L1BA / P0080TA / JK-NSMD010 / SMD4532-075 | CANH/CANL 的 ESD、浪涌、串联保险与气体放电保护网络 | 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页中右 CANH/CANL 至 CAN_H/CAN_L 的完整保护链 |
| P1,P2 (CAN板) | Header 5 / Header 4 | CAN_H/CAN_L/SHIELD 外部端与 RXD/TXD/+5VIN/GND 逻辑端连接器 | 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页右上 P1 Header 5 与左上 P2 Header 4 |
| U1 (RS232板) | MAX232ESE | TXD/RXD 逻辑电平与 RS232_R/RS232_T 电平转换器 | 图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页中央 U1 MAX232ESE，电荷泵和 T1/R1 通道 |
| P1,P2 (RS232板) | Header 9 / Header 3 | RS232_T/RS232_R/VIN+/+5V/GND 与 TXD/RXD/V+ 接口 | 图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页右侧 P1 Header 9 与左侧 P2 Header 3 |
| U1 (RS485板) | SP485EEN-L/TR | U0_TXD/U0_RXD 与 RS485_A/RS485_B 之间的半双工收发器 | 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页中央 U1 SP485EEN-L/TR，RO/RE/DE/DI/A/B/VCC/GND |
| Q1 (RS485板) | SS8050 Y1 | 由 U0_TXD 控制 SP485EEN 的 RE/DE 自动方向节点 | 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页左中 Q1 SS8050 Y1、R3/R4 与 U1 RE/DE |
| D1,D2,D3 (RS485板) | P6SMB6.8CA | RS485_B/RS485_A 线间及对地 TVS 保护 | 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页中右 D1/D2/D3 P6SMB6.8CA 跨接 GND、RS485_B、RS485_A |
| P1,P2 (RS485板) | Header 9 / Header 3 | RS485_B/RS485_A/VIN+/+5V/GND 与 U0_RXD/U0_TXD/V+ 接口 | 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页右侧 P1 Header 9 与左侧 P2 Header 3 |

## 系统结构

### Base LAN PoE v1.2 系统架构

主板通过 J3/J4 M5Stack_BUS 的 SPI 和控制 GPIO 驱动 U3 W5500，W5500 连接 25MHz 晶振与 U4 HBJ-6308ANLF RJ45；J1 或 P3 汇入的输入经 U2/U1 生成 +5V、D3V3 和 A3V3。另三张资源分别描述隔离 CAN、RS232 和 RS485 转接板。

- 参数与网络：`ethernet=U3 W5500 -> U4 HBJ-6308ANLF`；`host=J3/J4 M5Stack_BUS`；`power=J1 or P3 -> INF+ -> F1 -> IN+ -> U2 MP1584EN -> +5V -> U1 SPX3819M5-L-3-3 -> D3V3/A3V3`；`expansions=CA-IS3050G CAN, MAX232ESE RS232, SP485EEN-L/TR RS485`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页完整主板电源、W5500、RJ45、M5Stack_BUS; 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页隔离 CAN 转接板; 图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页 RS232 转接板; 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页 RS485 转接板

### 隔离 CAN 转接板架构

P2 的 RXD/TXD 接 U2 CA-IS3050G 的 CAN_RX/CAN_TX 逻辑侧；U3 HT7533 由 +5VIN 生成 +3.3V，U1 B0505S-1W 生成隔离 +S5V/SGND，U2 总线侧 CANH/CANL 经保护链到 CAN_H/CAN_L 和 P1。

- 参数与网络：`transceiver=U2 CA-IS3050G`；`logic_power=+5VIN -> U3 HT7533 -> +3.3V/GND`；`isolated_power=+5VIN/GND -> U1 B0505S-1W -> +S5V/SGND`；`signal_path=CAN_TX/CAN_RX <-> U2 <-> CANH/CANL -> protection -> CAN_H/CAN_L`
- 证据：图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页完整 CAN 转接板的 P2、U1/U2/U3、保护网络与 P1

## 电源

### P3 PoE 子板接口到主电源输入

U4 的 VC2+/VC2-/VC+/VC- 中心抽头网络分别进入 P3 的 VA1/VA2/VB1/VB2；P3 GND 接 GND，P3 VOUT 经 D3 SS54 接到 INF+，再与 J1 路径共同进入 F1。

- 参数与网络：`rj45_center_taps=VC2+,VC2-,VC+,VC-`；`header=P3 VA1,VA2,VB1,VB2,GND,VOUT`；`output_diode=D3 SS54`；`destination=INF+ -> F1`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U4 中心抽头至 P3，以及 P3 VOUT-D3-INF+ 连线

### IN+ 到 +5V 降压

U2 MP1584EN 的 VIN pin7 接 IN+，SW pin1 经 L1 10uH 输出 +5V，D1 SS54 从 SW 节点接地；C2/C3 各 22uF 对地，FB pin4 使用 R2 51KΩ 与 R4 10KΩ 反馈网络，EN pin2 标为未连接。

- 参数与网络：`input=IN+`；`converter=U2 MP1584EN`；`output=+5V`；`inductor=L1 10uH`；`diode=D1 SS54`；`output_capacitors=C2/C3 22uF`；`feedback=R2 51KΩ, R4 10KΩ`；`enable=pin2 NC`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左上 U2 MP1584EN、D1、L1、C2/C3、R2/R4 与 +5V

### +5V 到 D3V3/A3V3

U1 SPX3819M5-L-3-3 的 IN pin1 与 EN pin3 接 +5V，OUT pin5 输出 D3V3；D3V3 通过 R1 120Ω/MB 连接 A3V3，D3V3 使用 GND，A3V3 使用 AGND。

- 参数与网络：`ldo=U1 SPX3819M5-L-3-3`；`input=+5V`；`enable=+5V`；`digital_rail=D3V3/GND`；`analog_rail=A3V3/AGND`；`rail_bridge=R1 120Ω/MB`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页上中 U1、D3V3、R1、A3V3、GND 与 AGND

### CAN 板双电源域

U3 HT7533 的 VIN 接 +5VIN、VOUT 接 +3.3V、GND 接 GND；U1 B0505S-1W 的 +Vin/-Vin 接 +5VIN/GND，+Vout/-Vout 接 +S5V/SGND。U2 VCC1/GND1 使用 +3.3V/GND，VCC2/GND2 使用 +S5V/SGND。

- 参数与网络：`logic_domain=+3.3V/GND`；`bus_domain=+S5V/SGND`；`logic_regulator=U3 HT7533`；`isolated_converter=U1 B0505S-1W`；`transceiver=U2 CA-IS3050G`
- 证据：图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页左侧 U1/U3 与左下 U2 双侧电源引脚

### MAX232ESE 电荷泵

U1 VCC pin16 与 VDD pin2 接 +5V，GND pin15 接 GND；C1/C2/C3/C4/C5 均为 470nF，分别连接电荷泵 C1+/C1-/C2+/C2-、VDD/+5V 与 VEE/GND 节点。

- 参数与网络：`supply=+5V`；`ground=pin15 GND`；`capacitors=C1-C5 470nF`；`pump_pins=C1+ pin1, C1- pin3, C2+ pin4, C2- pin5, VDD pin2, VEE pin6`
- 证据：图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页 U1 上下电源与 C1-C5 470nF

## 接口

### U4 以太网 RJ45

U4 HBJ-6308ANLF 将 W5500 的 TXP/TXN 和 RXP/RXN 接入内部磁性器件并引出以太网端；其 Y-/Y+ 和 G-/G+ LED 分别连接 LINKLED、ACTLED 与 D3V3 限流网络。

- 参数与网络：`connector=U4 HBJ-6308ANLF`；`tx_pair=TD+/TD-`；`rx_pair=RD+/RD-`；`link_led=LINKLED via R14 1KΩ to D3V3`；`activity_led=ACTLED via R15 1KΩ to D3V3`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左中 U4 HBJ-6308ANLF 与 LINKLED/ACTLED、R14/R15

### J3/J4 M5Stack_BUS 关键针脚

M5Stack_BUS 的 pin7/9/11/10 分别为 GPIO23/GPIO19/GPIO18/GPIO26，pin22 为 GPIO13，pin26 为 GPIO34，pin23 为 GPIO15，pin20 为 GPIO5；pin1/3/5 为 GND，pin12 为 +3.3V，pin25 为 IN+，pin27/29 为 HPWR，pin28/30 为 +5V。

- 参数与网络：`spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18, pin10 GPIO26`；`control=pin22 GPIO13, pin26 GPIO34`；`expansion_uart=pin23 GPIO15 TX, pin20 GPIO5 RX`；`ground=pins1,3,5`；`power=pin12 +3.3V, pin25 IN+, pins27/29 HPWR, pins28/30 +5V`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右下 J3/J4 M5Stack_BUS pin1-pin30

### 主板 J2 转接板接口

J2 Header 4 的 RX 接 GPIO5、TX 接 GPIO15、VCC 接 +5V、GND 接 GND；RX/TX 网络分别对应 M5Stack_BUS pin20 与 pin23。

- 参数与网络：`rx=GPIO5, M5Stack_BUS pin20`；`tx=GPIO15, M5Stack_BUS pin23`；`supply=+5V`；`ground=GND`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页右中 J2 Header 4 与右下 M5Stack_BUS GPIO5/GPIO15

### CAN 板 P1/P2 针脚

P2 Header 4 的 pin1=RXD、pin2=TXD、pin3=+5VIN、pin4=GND；P1 Header 5 的 pin2=CAN_H、pin3=CAN_L、pin4 未连接、pin5=SHIELD，pin1 在本页无外接网络。

- 参数与网络：`P2=pin1 RXD, pin2 TXD, pin3 +5VIN, pin4 GND`；`P1=pin1 unconnected, pin2 CAN_H, pin3 CAN_L, pin4 NC, pin5 SHIELD`
- 证据：图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页左上 P2 Header 4 与右上 P1 Header 5

### RS232 板 P1/P2 针脚

P2 Header 3 的 pin1=RXD、pin2=TXD、pin3=V+；P1 Header 9 的 pin1/pin4=VIN+、pin2=RS232_T、pin3=RS232_R、pin5/pin9=GND、pin6/pin7 未连接、pin8=+5V。

- 参数与网络：`P2=pin1 RXD, pin2 TXD, pin3 V+`；`P1=pin1 VIN+, pin2 RS232_T, pin3 RS232_R, pin4 VIN+, pin5 GND, pins6/7 NC, pin8 +5V, pin9 GND`
- 证据：图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页左侧 P2 Header 3 与右侧 P1 Header 9

### RS485 板 P1/P2 针脚

P2 Header 3 的 pin1=U0_RXD、pin2=U0_TXD、pin3=V+；P1 Header 9 的 pin1/pin4=VIN+、pin2=RS485_B、pin3=RS485_A、pin5/pin9=GND、pin6/pin7 未连接、pin8=+5V。

- 参数与网络：`P2=pin1 U0_RXD, pin2 U0_TXD, pin3 V+`；`P1=pin1 VIN+, pin2 RS485_B, pin3 RS485_A, pin4 VIN+, pin5 GND, pins6/7 NC, pin8 +5V, pin9 GND`；`bus_direction=RS485_A/RS485_B bidirectional`
- 证据：图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页左侧 P2 Header 3 与右侧 P1 Header 9

## 总线

### W5500 SPI 主控映射

U3 MOSI pin35 接 GPIO23，MISO pin34 接 GPIO19，SCLK pin33 接 GPIO18，SCSn pin32 接 GPIO26；四条网络均进入 J3/J4 M5Stack_BUS，R16 10KΩ 将 SCSn 上拉到 D3V3。

- 参数与网络：`controller=M5Stack host`；`device=U3 W5500`；`mosi=pin35 GPIO23`；`miso=pin34 GPIO19`；`sclk=pin33 GPIO18`；`chip_select=pin32 GPIO26`；`cs_pullup=R16 10KΩ to D3V3`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 右侧 MOSI/MISO/SCLK/SCSn 与 J3/J4 同名 GPIO

### CAN 逻辑与差分总线映射

U2 CA-IS3050G 的 RXD pin2 接 CAN_RX，TXD pin3 接 CAN_TX，CANH pin7 接 CANH，CANL pin6 接 CANL；P2 pin1/pin2 分别为 RXD/TXD，P1 pin2/pin3 分别为 CAN_H/CAN_L。

- 参数与网络：`controller_side=P2 pin1 RXD/CAN_RX, pin2 TXD/CAN_TX`；`transceiver=U2 CA-IS3050G`；`bus_side=pin7 CANH, pin6 CANL`；`terminal=P1 pin2 CAN_H, pin3 CAN_L`；`direction=CAN_TX controller-to-bus; CAN_RX bus-to-controller`
- 证据：图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页 P2、U2 和 P1 的 RXD/TXD/CANH/CANL/CAN_H/CAN_L

### RS232 转接板信号路径

U1 MAX232ESE 的 T1IN pin11 接 TXD，T1OUT pin14 输出 RS232_R；R1IN pin13 接 RS232_T，R1OUT pin12 输出 RXD。T2IN/T2OUT 与 R2IN/R2OUT 在本页未使用。

- 参数与网络：`logic_to_rs232=TXD -> T1IN pin11 -> T1OUT pin14 -> RS232_R`；`rs232_to_logic=RS232_T -> R1IN pin13 -> R1OUT pin12 -> RXD`；`unused_channel=T2IN/T2OUT/R2IN/R2OUT NC`；`supply=+5V`
- 证据：图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页中央 U1 MAX232ESE 的 T1/R1 通道与未连接第二通道

### RS485 转接板自动方向

P2 pin1 的 U0_RXD 经 R2 1KΩ 接 U1 RO pin1；P2 pin2 的 U0_TXD 直接接 DI pin4，并经 R4 1KΩ 驱动 Q1 SS8050 Y1。Q1 控制相连的 RE pin2/DE pin3 节点，R3 4.7KΩ 将该节点上拉到 +5V。

- 参数与网络：`receive=U1 RO pin1 -> R2 1KΩ -> U0_RXD/P2 pin1`；`transmit=U0_TXD/P2 pin2 -> U1 DI pin4`；`direction_control=U0_TXD -> R4 1KΩ -> Q1; Q1 collector -> RE/DE`；`direction_pullup=R3 4.7KΩ to +5V`；`transceiver=U1 SP485EEN-L/TR`
- 证据：图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页 P2、R2/R3/R4、Q1 与 U1 RO/RE/DE/DI

## GPIO 与控制信号

### W5500 复位与中断

U3 RSTn pin37 接 GPIO13，INTn pin36 接 GPIO34；R8 与 R13 各 10KΩ 将对应网络上拉到 D3V3。

- 参数与网络：`reset=U3 pin37 RSTn -> GPIO13`；`interrupt=U3 pin36 INTn -> GPIO34`；`pullups=R8/R13 10KΩ to D3V3`；`polarity=RSTn and INTn active-low naming`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 RSTn/INTn 与 GPIO13/GPIO34、R8/R13

### W5500 PMODE 配置

U3 PMODE2、PMODE1、PMODE0 通过 R7 标为 10KΩ (103) ±5% 的电阻阵列连接 D3V3。

- 参数与网络：`signals=PMODE2,PMODE1,PMODE0`；`array=R7 10KΩ (103) ±5%`；`rail=D3V3`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 上边 PMODE2/PMODE1/PMODE0 与 R7

## 时钟

### W5500 外部时钟

U3 XO pin31 与 XI/CLKIN pin30 连接 Y1 25MHz 12PF 10PPM 晶振，R20 1MΩ 跨接两端，C14/C17 各 18pF 接 GND。

- 参数与网络：`frequency=25MHz`；`pins=XO pin31, XI/CLKIN pin30`；`crystal=Y1 25MHz 12PF 10PPM`；`feedback=R20 1MΩ`；`load_capacitors=C14/C17 18pF`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 右下 XO/XI 与 Y1/R20/C14/C17

## 复位

### W5500 硬件复位路径

W5500 RSTn 由 M5Stack_BUS 的 GPIO13 驱动并由 R8 10KΩ 上拉到 D3V3；四页资源均未展示独立复位开关。

- 参数与网络：`device_pin=U3 pin37 RSTn`；`host_gpio=GPIO13`；`pullup=R8 10KΩ to D3V3`；`reset_switch_shown=false`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 RSTn 37 脚到 GPIO13/R8，主板页无复位开关

## 保护电路

### 主板外部输入保护

J1 的正端形成 INF+，经 F1 PPTC-1812 串联后成为 IN+；C9/C10 各 2.2uF 从 IN+ 接 GND，再进入 U2 VIN pin7。

- 参数与网络：`connector=J1 PWR3.5`；`positive_path=J1 -> INF+ -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C9/C10 2.2uF`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页左上 J1、INF+、F1、IN+、C9/C10 与 U2 VIN

### CAN 多级保护

DZ1/DZ2 PESD5V0L1BA 将 CANH/CANL 钳位到 SGND，TSS2 P0080TA 跨接 CANH/CANL；TSS1/TSS3 P0080TA 接 SHIELD，F1/F2 60V 100mA JK-NSMD010 串联后，GDT1/GDT2 SMD4532-075 将 CAN_H/CAN_L 接 SHIELD。

- 参数与网络：`esd=DZ1/DZ2 PESD5V0L1BA to SGND`；`differential_tss=TSS2 P0080TA`；`shield_tss=TSS1/TSS3 P0080TA`；`series_fuses=F1/F2 60V 100mA JK-NSMD010`；`gdt=GDT1/GDT2 SMD4532-075 to SHIELD`；`shield_coupling=R3 1MΩ and C3 1nF 2000V between SGND/SHIELD`
- 证据：图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页中右 CANH/CANL、SGND、SHIELD、F1/F2 与全部浪涌器件

### RS485 偏置与 TVS

U1 B pin7 接 RS485_B 并由 R1 4.7KΩ 下拉到 GND，A pin6 接 RS485_A 并由 R5 4.7KΩ 上拉到 +5V；D1/D2/D3 均为 P6SMB6.8CA，分别构成 RS485_B 对地、B/A 线间和 RS485_A 对地保护。

- 参数与网络：`b_bias=R1 4.7KΩ to GND`；`a_bias=R5 4.7KΩ to +5V`；`tvs=D1/D2/D3 P6SMB6.8CA`；`termination_resistor_shown=false`
- 证据：图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页 U1 A/B、R1/R5 与 D1/D2/D3

## 模拟电路

### W5500 PHY 模拟网络

U3 TXN pin1、TXP pin2、RXN pin5、RXP pin6 通过 TX/RX 差分网络连接 U4 的 TD-/TD+/RD-/RD+；网络包含 R10/R11/R12/R17/R18 49.9Ω、两只 6.8nF 串联电容以及 C15 22nF、C16 10nF。

- 参数与网络：`tx=U3 TXN/TXP -> U4 TD-/TD+`；`rx=U3 RXN/RXP -> U4 RD-/RD+`；`resistors=R10/R11/R12/R17/R18 49.9Ω`；`rx_series_capacitors=2 x 6.8nF`；`shunt_capacitors=C15 22nF, C16 10nF`
- 证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 与 U4 间 TXP/TXN/RXP/RXN、R10-R12/R17/R18、C15/C16

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base LAN PoE v1.2 系统架构 | `ethernet=U3 W5500 -> U4 HBJ-6308ANLF`；`host=J3/J4 M5Stack_BUS`；`power=J1 or P3 -> INF+ -> F1 -> IN+ -> U2 MP1584EN -> +5V -> U1 SPX3819M5-L-3-3 -> D3V3/A3V3`；`expansions=CA-IS3050G CAN, MAX232ESE RS232, SP485EEN-L/TR RS485` |
| 保护电路 | 主板外部输入保护 | `connector=J1 PWR3.5`；`positive_path=J1 -> INF+ -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C9/C10 2.2uF` |
| 电源 | P3 PoE 子板接口到主电源输入 | `rj45_center_taps=VC2+,VC2-,VC+,VC-`；`header=P3 VA1,VA2,VB1,VB2,GND,VOUT`；`output_diode=D3 SS54`；`destination=INF+ -> F1` |
| 电源 | IN+ 到 +5V 降压 | `input=IN+`；`converter=U2 MP1584EN`；`output=+5V`；`inductor=L1 10uH`；`diode=D1 SS54`；`output_capacitors=C2/C3 22uF`；`feedback=R2 51KΩ, R4 10KΩ`；`enable=pin2 NC` |
| 电源 | +5V 到 D3V3/A3V3 | `ldo=U1 SPX3819M5-L-3-3`；`input=+5V`；`enable=+5V`；`digital_rail=D3V3/GND`；`analog_rail=A3V3/AGND`；`rail_bridge=R1 120Ω/MB` |
| 总线 | W5500 SPI 主控映射 | `controller=M5Stack host`；`device=U3 W5500`；`mosi=pin35 GPIO23`；`miso=pin34 GPIO19`；`sclk=pin33 GPIO18`；`chip_select=pin32 GPIO26`；`cs_pullup=R16 10KΩ to D3V3` |
| GPIO 与控制信号 | W5500 复位与中断 | `reset=U3 pin37 RSTn -> GPIO13`；`interrupt=U3 pin36 INTn -> GPIO34`；`pullups=R8/R13 10KΩ to D3V3`；`polarity=RSTn and INTn active-low naming` |
| 复位 | W5500 硬件复位路径 | `device_pin=U3 pin37 RSTn`；`host_gpio=GPIO13`；`pullup=R8 10KΩ to D3V3`；`reset_switch_shown=false` |
| GPIO 与控制信号 | W5500 PMODE 配置 | `signals=PMODE2,PMODE1,PMODE0`；`array=R7 10KΩ (103) ±5%`；`rail=D3V3` |
| 时钟 | W5500 外部时钟 | `frequency=25MHz`；`pins=XO pin31, XI/CLKIN pin30`；`crystal=Y1 25MHz 12PF 10PPM`；`feedback=R20 1MΩ`；`load_capacitors=C14/C17 18pF` |
| 模拟电路 | W5500 PHY 模拟网络 | `tx=U3 TXN/TXP -> U4 TD-/TD+`；`rx=U3 RXN/RXP -> U4 RD-/RD+`；`resistors=R10/R11/R12/R17/R18 49.9Ω`；`rx_series_capacitors=2 x 6.8nF`；`shunt_capacitors=C15 22nF, C16 10nF` |
| 接口 | U4 以太网 RJ45 | `connector=U4 HBJ-6308ANLF`；`tx_pair=TD+/TD-`；`rx_pair=RD+/RD-`；`link_led=LINKLED via R14 1KΩ to D3V3`；`activity_led=ACTLED via R15 1KΩ to D3V3` |
| 接口 | J3/J4 M5Stack_BUS 关键针脚 | `spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18, pin10 GPIO26`；`control=pin22 GPIO13, pin26 GPIO34`；`expansion_uart=pin23 GPIO15 TX, pin20 GPIO5 RX`；`ground=pins1,3,5`；`power=pin12 +3.3V, pin25 IN+, pins27/29 HPWR, pins28/30 +5V` |
| 接口 | 主板 J2 转接板接口 | `rx=GPIO5, M5Stack_BUS pin20`；`tx=GPIO15, M5Stack_BUS pin23`；`supply=+5V`；`ground=GND` |
| 系统结构 | 隔离 CAN 转接板架构 | `transceiver=U2 CA-IS3050G`；`logic_power=+5VIN -> U3 HT7533 -> +3.3V/GND`；`isolated_power=+5VIN/GND -> U1 B0505S-1W -> +S5V/SGND`；`signal_path=CAN_TX/CAN_RX <-> U2 <-> CANH/CANL -> protection -> CAN_H/CAN_L` |
| 电源 | CAN 板双电源域 | `logic_domain=+3.3V/GND`；`bus_domain=+S5V/SGND`；`logic_regulator=U3 HT7533`；`isolated_converter=U1 B0505S-1W`；`transceiver=U2 CA-IS3050G` |
| 总线 | CAN 逻辑与差分总线映射 | `controller_side=P2 pin1 RXD/CAN_RX, pin2 TXD/CAN_TX`；`transceiver=U2 CA-IS3050G`；`bus_side=pin7 CANH, pin6 CANL`；`terminal=P1 pin2 CAN_H, pin3 CAN_L`；`direction=CAN_TX controller-to-bus; CAN_RX bus-to-controller` |
| 保护电路 | CAN 多级保护 | `esd=DZ1/DZ2 PESD5V0L1BA to SGND`；`differential_tss=TSS2 P0080TA`；`shield_tss=TSS1/TSS3 P0080TA`；`series_fuses=F1/F2 60V 100mA JK-NSMD010`；`gdt=GDT1/GDT2 SMD4532-075 to SHIELD`；`shield_coupling=R3 1MΩ and C3 1nF 2000V between SGND/SHIELD` |
| 接口 | CAN 板 P1/P2 针脚 | `P2=pin1 RXD, pin2 TXD, pin3 +5VIN, pin4 GND`；`P1=pin1 unconnected, pin2 CAN_H, pin3 CAN_L, pin4 NC, pin5 SHIELD` |
| 总线 | RS232 转接板信号路径 | `logic_to_rs232=TXD -> T1IN pin11 -> T1OUT pin14 -> RS232_R`；`rs232_to_logic=RS232_T -> R1IN pin13 -> R1OUT pin12 -> RXD`；`unused_channel=T2IN/T2OUT/R2IN/R2OUT NC`；`supply=+5V` |
| 电源 | MAX232ESE 电荷泵 | `supply=+5V`；`ground=pin15 GND`；`capacitors=C1-C5 470nF`；`pump_pins=C1+ pin1, C1- pin3, C2+ pin4, C2- pin5, VDD pin2, VEE pin6` |
| 接口 | RS232 板 P1/P2 针脚 | `P2=pin1 RXD, pin2 TXD, pin3 V+`；`P1=pin1 VIN+, pin2 RS232_T, pin3 RS232_R, pin4 VIN+, pin5 GND, pins6/7 NC, pin8 +5V, pin9 GND` |
| 总线 | RS485 转接板自动方向 | `receive=U1 RO pin1 -> R2 1KΩ -> U0_RXD/P2 pin1`；`transmit=U0_TXD/P2 pin2 -> U1 DI pin4`；`direction_control=U0_TXD -> R4 1KΩ -> Q1; Q1 collector -> RE/DE`；`direction_pullup=R3 4.7KΩ to +5V`；`transceiver=U1 SP485EEN-L/TR` |
| 保护电路 | RS485 偏置与 TVS | `b_bias=R1 4.7KΩ to GND`；`a_bias=R5 4.7KΩ to +5V`；`tvs=D1/D2/D3 P6SMB6.8CA`；`termination_resistor_shown=false` |
| 接口 | RS485 板 P1/P2 针脚 | `P2=pin1 U0_RXD, pin2 U0_TXD, pin3 V+`；`P1=pin1 VIN+, pin2 RS485_B, pin3 RS485_A, pin4 VIN+, pin5 GND, pins6/7 NC, pin8 +5V, pin9 GND`；`bus_direction=RS485_A/RS485_B bidirectional` |
| 电源 | PoE 高压受电前端 | `visible_interface=U4 center taps -> P3; P3 VOUT -> D3 -> INF+`；`poe_controller=null`；`bridge_rectifier=null`；`isolation_converter=null`；`documented_standard=IEEE 802.3af`；`documented_input=DC 37-57V` |
| 核心器件 | 正文中的 W5500 协议与缓存能力 | `part_number=W5500`；`documented_protocols=TCP,UDP,IPv4,ICMP,ARP,IGMP,PPPoE`；`documented_sockets=8`；`documented_buffer=32Kbytes TX/RX Buffers`；`schematic_confirmation=model and external connections only` |
| 系统结构 | CAN/RS232/RS485 转接板装配组合 | `available_schematics=CAN,RS232,RS485`；`main_header=J2 GPIO5 RX/GPIO15 TX/+5V/GND`；`assembly_variant=null`；`simultaneous_installation=null`；`can_gpio_map=null` |

## 待确认事项

- `power.poe-front-end-boundary`：主板页只显示 RJ45 中心抽头到 P3 以及 P3 VOUT 经 D3 汇入 INF+；资源未展示 PoE 检测/分类、整流、高压隔离 DC-DC、控制器料号或 37-57V 输入范围的器件级实现。（证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U4-P3-D3-INF+，页面无 PoE 高压前端器件）
- `component.documented-w5500-capabilities`：正文列出 TCP/UDP/IPv4/ICMP/ARP/IGMP/PPPoE、8 路硬件 Socket 和 32Kbytes TX/RX Buffers；原理图仅确认 W5500 型号和外部电路，未标注协议、Socket 数量或缓存容量。（证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页 U3 W5500 符号与外部连接，图中无协议/Socket/缓存参数）
- `system.expansion-assembly`：资源分别提供 CAN、RS232 和 RS485 三张完整转接板原理图，但未给出量产时的焊接组合、互斥规则、P1/P2 与主板 J2/P2 的机械对应关系或 CAN_TX/CAN_RX 到主机 GPIO 的最终映射。（证据：图 2bf48b663891 / 第 1 页 / 第 1 张第 1 页主板 J2 Header 4 与 P2 HDR_6P; 图 c35be3c28b88 / 第 1 页 / 第 2 张第 1 页 CAN 板 P1/P2; 图 7f2698f2e729 / 第 1 页 / 第 3 张第 1 页 RS232 板 P1/P2; 图 8a0c0e7232ea / 第 1 页 / 第 4 张第 1 页 RS485 板 P1/P2）
- `review.poe-front-end`：K012-C-V12 配套 PoE 子板的控制器、整流桥、隔离 DC-DC、检测/分类电阻和完整 37-57V/IEEE 802.3af 设计是什么？；原因：四张资源只显示主板 P3 接口和低压输出汇入路径，没有 PoE 高压受电前端。
- `review.w5500-capabilities`：请以当前 W5500 datasheet 与固件验证正文列出的协议、8 路 Socket、32Kbytes 缓存和 SPI 模式。；原因：这些是芯片/固件能力，不是当前原理图页可独立证明的连接事实。
- `review.expansion-assembly`：K012-C-V12 出货时 CAN、RS232、RS485 转接板如何选择或焊接，P1/P2 与主板焊盘如何对应，CAN_TX/CAN_RX 最终映射哪些主机 GPIO？；原因：资源给出三套独立板级原理图，但没有总装互连图或装配配置表。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2bf48b66389147b67403c8990af46aa562d601de576f5c84cc387e1ff89deae2` | `https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_01.webp` |
| 2 | 1 | `c35be3c28b88cf0629d335352b254edb61e6ffcaf7b5977aff1cc076dedefe0c` | `https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_02.webp` |
| 3 | 1 | `7f2698f2e729af8dd9e04733815df6a67a0d1ab70917bf47cc072f7e51c8acbe` | `https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_03.webp` |
| 4 | 1 | `8a0c0e7232eab35b87ff671420f99a19299d52db1933fd57419770373220515d` | `https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_04.webp` |

---

源文档：`zh_CN/base/lan_poe_v12.md`

源文档 SHA-256：`2d5f64ffb0426fab5b362be739f618a8f70af8604bd646e14058d07c55e31c61`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
