# Base LAN PoE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base LAN PoE |
| SKU | K012-C |
| 产品 ID | `base-lan-poe-329c1d37f3fa` |
| 源文档 | `zh_CN/base/w5500PoE.md` |

## 概述

Base LAN PoE V1.0 以 U3 W5500 为以太网控制器，通过 M5Stack_BUS 的 GPIO23/19/18/26 使用 SPI，并以 GPIO13 复位、GPIO34 中断。U4 HJBJ-6308ANLF 集成 RJ45 磁性器件与链路/活动 LED，其 PoE 抽头通过 VC+/VC-/VC2+/VC2- 送入 P3；P3 VOUT 经 D3 SS54 与 J1 外部 IN12/24V 汇合为 INF+。INF+ 经 F1、U2 TPS54360 生成 +5V，再由 U1 SPX3819M5-L-3-3 生成 D3V3/A3V3；串口转 RS485/RS232 的收发器未画在当前页。

## 检索关键词

`Base LAN PoE`、`K012-C`、`LAN_W5500.PriPCB`、`V1.0`、`W5500`、`HJBJ-6308ANLF`、`TPS54360`、`SPX3819M5-L-3-3`、`P3 HDR_6P`、`PoE`、`VC+`、`VC-`、`VC2+`、`VC2-`、`INF+`、`IN12/24V`、`SS54`、`PPTC-1812`、`SPI`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO26`、`GPIO13`、`GPIO34`、`GPIO5`、`GPIO15`、`25MHz`、`TXP`、`TXN`、`RXP`、`RXN`、`LINKLED`、`ACTLED`、`D3V3`、`A3V3`、`M5Stack_BUS`、`RS485`、`RS232`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | W5500 | SPI 以太网控制器，连接主机总线、25MHz 时钟、PHY 差分线、复位、中断和 LED | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页中央 U3 W5500，48 脚方框及 TX/RX、SPI、时钟、RSTn、INTn、LED 引脚 |
| U4 | HJBJ-6308ANLF | 集成隔离磁性器件、PoE 抽头与 LINK/ACT LED 的 RJ45 连接器 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页左中 U4 HJBJ-6308ANLF，TD/RD、VC/VC2 和 Y/G LED 引脚 |
| P3 | HDR_6P | 接收 VA1/VA2/VB1/VB2 四路 PoE 网络并输出 GND/VOUT 的模块接口 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页左中上 P3 HDR_6P，VA1/VA2/VB1/VB2/GND/VOUT，外侧 VC2+/VC2-/VC+/VC- |
| D3 | SS54 | 串联在 P3 VOUT 与 INF+ 之间的 PoE 输出隔离二极管 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 P3 左下 VOUT-D3 SS54-INF+ 路径 |
| U2 | TPS54360 | 将 INF+/IN+ 降压为 +5V 的开关转换器 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页左上 U2 TPS54360 与 C1-C3、C8-C10、D1、L1、反馈网络 |
| J1 | PWR3.5 | IN12/24V 与 GND 外部直流电源输入连接器 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页最左上 J1 PWR3.5，正输入为 INF+，回路接 GND |
| F1 | PPTC-1812 | 串联在 INF+ 与 IN+ 之间的自恢复输入保护器件 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 J1/PoE 汇流节点 INF+ 与 U2 输入 IN+ 之间 F1 PPTC-1812 |
| D1,L1 | B290B / 8.2uH | TPS54360 降压级续流二极管和输出电感 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U2 右侧 D1 B290B 接 GND、L1 8.2uH 串向 +5V |
| U1 | SPX3819M5-L-3-3 | 由 +5V 生成 D3V3 的 3.3V LDO | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页上中 U1 SPX3819M5-L-3-3，IN/EN 接 +5V，OUT 接 D3V3 |
| R1,R3 | 120Ω/MB / 0Ω | 分别桥接 D3V3-A3V3 与 GND-AGND 电源域 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页上中 R1 120Ω/MB 位于 D3V3/A3V3，R3 0Ω 位于 GND/AGND |
| Y1,R20,C14,C17 | 25MHz 12PF 10PPM / 1MΩ / 18pF | W5500 XI/XO 外部晶振网络 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 右下 Y1 25MHz 12PF 10PPM、R20 1MΩ、C14/C17 18pF |
| R7 | 10KΩ (103) ±5% 4P | W5500 PMODE 配置引脚的四联电阻阵列 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 上方 R7 10KΩ (103) ±5% 四联阵列与 PMODE0/1/2 |
| R8,R13,R16 | 10KΩ | 分别为 W5500 RSTn、INTn 与 SCSn 提供 D3V3 上拉 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 RSTn-R8、INTn-R13、SCSn-R16，电阻另一端均接 D3V3 |
| R10,R11,R12,C11,C12,R17,R18,C15,C16 | 10Ω / 49.9Ω / 6.8nF / 22nF / 10nF network | W5500 与 U4 之间的 TX/RX 偏置、耦合和端接网络 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3/U4 之间 A3V3、TXP/TXN、RXP/RXN 周围 R10-R12/C11/C12/R17/R18/C15/C16 |
| R14,R15 | 1KΩ | U4 集成 LINK/ACT LED 的 D3V3 限流电阻 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U4 左侧 LINKLED/ACTLED 与 D3V3 之间 R14/R15 1KΩ |
| P2 | HDR_6P | 标为 I/O1-I/O6 的六针预留接口 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页右上 P2 HDR_6P，pin1-pin6 分别为 I/O1-I/O6，均无后续网络 |
| J2 | Header 4 | 引出 GPIO5、GPIO15、+5V 与 GND 的串口侧四针接口 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页右中 J2 Header 4，RX/GPIO5、TX/GPIO15、VCC/+5V、GND |
| J3,J4 | M5Stack_BUS | 同一 30 针 M5Stack 主机总线符号的分段位号，承载 SPI、控制、串口和电源 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页右下连接器上方标注 J3 J4、下方 M5Stack_BUS，1-30 脚 |
| D2,R9 | LED 0603 / 4.7KΩ | +5V 电源指示 LED 与限流电阻 | 图 03bbcb4a5f2c / 第 1 页 / 第 1 页右中上 +5V-D2 LED 0603-R9 4.7KΩ-GND |

## 系统结构

### Base LAN PoE 总体架构

M5Stack 主机经 SPI 控制 U3 W5500，U3 PHY 接 U4 PoE 磁性 RJ45；U4 的 PoE 网络进入 P3，P3 与外部 J1 电源共同形成 INF+，经 U2/U1 生成 +5V、D3V3 和 A3V3。

- 参数与网络：`host=J3/J4 M5Stack_BUS`；`ethernet=U3 W5500`；`magjack=U4 HJBJ-6308ANLF`；`poe_interface=P3 HDR_6P`；`dc_input=J1 PWR3.5`；`buck=U2 TPS54360`；`ldo=U1 SPX3819M5-L-3-3`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页完整单页原理图，PoE/外部输入、电源、W5500、U4 与 M5Stack_BUS

## 电源

### PoE 取电网络

U4 的 PoE 引脚将 VC2+、VC2-、VC+、VC- 分别送入 P3 的 VA1、VA2、VB1、VB2；U4 符号同时标出 VC+/TD、VC-/RD、VC+/J7&J8、VC-/J4&J5。

- 参数与网络：`va1=VC2+`；`va2=VC2-`；`vb1=VC+`；`vb2=VC-`；`magjack_labels=VC+/TD; VC-/RD; VC+/J7&J8; VC-/J4&J5`；`destination=P3`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页左中 U4 pins7-10 的 VC 网络与 P3 VA1/VA2/VB1/VB2

### PoE 输出与外部输入汇流

P3 VOUT 经 D3 SS54 形成 INF+，P3 GND 接 GND；J1 正输入也连接 INF+，因此 PoE 输出和外部 DC 输入在 F1 前汇合。

- 参数与网络：`poe_output=P3 VOUT -> D3 SS54 -> INF+`；`poe_return=P3 GND -> GND`；`external_input=J1 -> INF+`；`downstream=INF+ -> F1 -> IN+`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页左侧 P3 VOUT/D3/INF+ 与 J1 INF+/F1

### IN+ 到 +5V 降压

U2 TPS54360 的 SW 节点连接 D1 B290B 与 L1 8.2uH，L1 后形成 +5V，C2/C3 各 10uF 滤波；FB 使用 R4 51KΩ 与 R6 10KΩ 分压。

- 参数与网络：`input=IN+`；`output=+5V`；`diode=D1 B290B`；`inductor=L1 8.2uH`；`output_capacitors=C2/C3 10uF`；`feedback=R4 51KΩ; R6 10KΩ`；`enable=U2 pin3 EN shown NC`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页上方 U2/D1/L1/C2/C3/R4/R6，EN pin3 未连接

### +5V 到 D3V3 LDO

U1 SPX3819M5-L-3-3 的 IN/EN 接 +5V，OUT 输出 D3V3；C5/C7 各 100nF，BYP/ADJ 通过 C6 470pF 接 GND。

- 参数与网络：`input=+5V`；`enable=+5V`；`output=D3V3`；`input_capacitor=C5 100nF`；`output_capacitor=C7 100nF`；`bypass=C6 470pF`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页上中 U1 SPX3819M5-L-3-3 与 C5/C6/C7

### A3V3/D3V3 与 AGND/GND 分区

D3V3 经 R1 120Ω/MB 连接 A3V3，GND 经 R3 0Ω 连接 AGND；C4 100uF 位于 A3V3/AGND。

- 参数与网络：`supply_bridge=R1 120Ω/MB: D3V3 to A3V3`；`ground_bridge=R3 0Ω: GND to AGND`；`analog_bulk=C4 100uF`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页上中 U1 输出右侧 R1/R3/C4 与 D3V3/A3V3/GND/AGND

### W5500 电源去耦

A3V3 侧 C19-C24 各 100nF 接 AGND，D3V3 侧 C25 100nF 与 C26 10uF 接 GND；U3 下方还有 C27 4.7uF 与 C18 10nF 接 AGND。

- 参数与网络：`analog=C19-C24 100nF; C27 4.7uF; C18 10nF`；`digital=C25 100nF; C26 10uF`；`analog_ground=AGND`；`digital_ground=GND`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页底部 C19-C27/C18 去耦网络

### +5V 电源指示

D2 LED 0603 与 R9 4.7KΩ 串联在 +5V 和 GND 之间。

- 参数与网络：`rail=+5V`；`led=D2 LED 0603`；`resistor=R9 4.7KΩ`；`return=GND`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页右中上 +5V-D2-R9-GND

## 接口

### RJ45 链路和活动指示

U3 LINKLED pin25 接 U4 LINKLED，ACTLED pin27 接 U4 ACTLED；R14/R15 各 1KΩ 从 D3V3 接 U4 LED 端，DUPLED pin26 标为未连接。

- 参数与网络：`link=U3 pin25 -> U4 LINKLED`；`activity=U3 pin27 -> U4 ACTLED`；`resistors=R14/R15 1KΩ to D3V3`；`duplex_connected=false`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 LINKLED/ACTLED/DUPLED 与 U4 Y/G LED、R14/R15

### J2 串口侧接口

J2 Header 4 的 RX 接 GPIO5、TX 接 GPIO15、VCC 接 +5V、GND 接 GND；GPIO5/GPIO15 同时连接 M5Stack_BUS。

- 参数与网络：`rx=GPIO5`；`tx=GPIO15`；`vcc=+5V`；`ground=GND`；`host=M5Stack_BUS GPIO5/GPIO15`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页右中 J2 Header 4 与右下 M5Stack_BUS GPIO5/GPIO15

### M5Stack_BUS 关键映射

30 针 M5Stack_BUS 引出 GPIO23/19/18/26 给 W5500 SPI，GPIO13/GPIO34 给复位和中断，GPIO5/GPIO15 给 J2 串口；pin25 的 IN+ 对应 HPWR，pin28 为 +5V，pin30 为 BATTERY。

- 参数与网络：`spi=GPIO23, GPIO19, GPIO18, GPIO26`；`control=GPIO13, GPIO34`；`serial=GPIO5, GPIO15`；`power=pin25 IN+/HPWR; pin28 +5V; pin30 BATTERY`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页右下 M5Stack_BUS 1-30 脚与外侧 GPIO/IN+/+5V 网络

## 总线

### W5500 SPI 映射

U3 MOSI pin35=GPIO23、MISO pin34=GPIO19、SCLK pin33=GPIO18、SCSn pin32=GPIO26，四条网络进入 M5Stack_BUS；SCSn 由 R16 10KΩ 上拉 D3V3。

- 参数与网络：`controller=M5Stack host`；`device=U3 W5500`；`mosi=pin35 GPIO23`；`miso=pin34 GPIO19`；`sclk=pin33 GPIO18`；`cs=pin32 GPIO26`；`cs_pullup=R16 10KΩ to D3V3`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 右侧 35-32 脚 GPIO23/19/18/26 与右下 M5Stack_BUS

### W5500 PHY 差分对

U3 TXN pin1/TXP pin2 与 RXN pin5/RXP pin6 通过 TXN/TXP/RXN/RXP 网络及偏置耦合器件连接 U4 TD-/TD+/RD-/RD+。

- 参数与网络：`transmit=U3 pin1 TXN / pin2 TXP -> U4 pin3 TD- / pin1 TD+`；`receive=U3 pin5 RXN / pin6 RXP -> U4 pin6 RD- / pin4 RD+`；`rail=A3V3/AGND`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 左侧 TX/RX 1/2/5/6 脚到 U4 TD/RD 1/3/4/6 脚

## GPIO 与控制信号

### W5500 复位与中断

U3 RSTn pin37 接 GPIO13 并由 R8 10KΩ 上拉 D3V3；INTn pin36 接 GPIO34 并由 R13 10KΩ 上拉 D3V3。

- 参数与网络：`reset=U3 pin37 RSTn -> GPIO13; R8 10KΩ`；`interrupt=U3 pin36 INTn -> GPIO34; R13 10KΩ`；`rail=D3V3`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 RSTn/INTn 与 GPIO13/GPIO34、R8/R13

### W5500 PMODE 配置

U3 PMODE0/PMODE1/PMODE2 连接 R7 10KΩ (103) ±5% 四联电阻阵列，阵列上侧接 D3V3。

- 参数与网络：`signals=PMODE0, PMODE1, PMODE2`；`array=R7 10KΩ (103) ±5% 4P`；`rail=D3V3`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 顶部 PMODE 引脚与 R7/D3V3

## 时钟

### W5500 25MHz 时钟

U3 XO pin31 与 XI/CLKIN pin30 连接 Y1 25MHz 12PF 10PPM 晶振，R20 1MΩ 跨接两端，C14/C17 各 18pF 接 GND。

- 参数与网络：`frequency=25MHz`；`crystal=Y1 25MHz 12PF 10PPM`；`pins=XO pin31; XI/CLKIN pin30`；`feedback=R20 1MΩ`；`load=C14/C17 18pF`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 右下 XO/XI/Y1/R20/C14/C17

## 复位

### W5500 硬件复位路径

M5Stack_BUS 的 GPIO13 驱动 U3 RSTn，R8 10KΩ 保持上拉；页面未画出独立复位按钮。

- 参数与网络：`host_gpio=GPIO13`；`device_pin=U3 pin37 RSTn`；`pullup=R8 10KΩ to D3V3`；`reset_button_shown=false`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 RSTn/GPIO13/R8 及完整单页，无复位开关

## 保护电路

### 汇流输入保护

INF+ 经 F1 PPTC-1812 后成为 IN+，C9/C10 各 2.2uF 从 IN+ 接 GND，再进入 U2 VIN。

- 参数与网络：`path=INF+ -> F1 PPTC-1812 -> IN+ -> U2 VIN`；`input_capacitors=C9/C10 2.2uF`；`return=GND`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页左上 INF+/F1/IN+/C9/C10/U2 VIN

### RJ45 屏蔽耦合

U4 下方屏蔽/外壳节点通过 C13 1nF（102）10% 2000V 接 GND。

- 参数与网络：`capacitor=C13 1nF (102) 10% 2000V`；`return=GND`；`connector=U4 HJBJ-6308ANLF`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U4 左下垂直节点与 C13 1nF (102) 10% 2000V/GND

## 存储

### 板载存储

当前完整单页原理图未画出 Flash、PSRAM、EEPROM 或存储卡接口。

- 参数与网络：`flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页完整器件页，无存储器件或存储连接器

## 调试与烧录

### 专用调试接口

当前完整单页原理图未画出 JTAG、SWD、USB-UART 或专用调试连接器。

- 参数与网络：`jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`debug_connector_shown=false`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页完整单页连接器与网络，无调试接口标注

## 模拟电路

### W5500 EXRES1 外部电阻

U3 EXRES1 pin10 通过 R19 12KΩ（图中另标 12.4K）连接 AGND。

- 参数与网络：`pin=U3 pin10 EXRES1`；`reference=R19`；`visible_values=12KΩ / 12.4K`；`ground=AGND`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3 左下 EXRES1-R19-AGND，黑字 12KΩ、蓝字 12.4K

### PHY 偏置与耦合网络

U4 发送中心抽头通过 R10 10Ω 接 A3V3，TXP/TXN 通过 R11/R12 49.9Ω 偏置；RXP/RXN 使用 C11/C12 6.8nF 串联耦合及 R17/R18 49.9Ω、C15 22nF、C16 10nF 网络。

- 参数与网络：`tx_center=R10 10Ω to A3V3`；`tx_bias=R11/R12 49.9Ω`；`rx_series=C11/C12 6.8nF`；`rx_resistors=R17/R18 49.9Ω`；`rx_capacitors=C15 22nF; C16 10nF`
- 证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 U3/U4 之间 R10-R12/C11/C12/R17/R18/C15/C16

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base LAN PoE 总体架构 | `host=J3/J4 M5Stack_BUS`；`ethernet=U3 W5500`；`magjack=U4 HJBJ-6308ANLF`；`poe_interface=P3 HDR_6P`；`dc_input=J1 PWR3.5`；`buck=U2 TPS54360`；`ldo=U1 SPX3819M5-L-3-3` |
| 电源 | PoE 取电网络 | `va1=VC2+`；`va2=VC2-`；`vb1=VC+`；`vb2=VC-`；`magjack_labels=VC+/TD; VC-/RD; VC+/J7&J8; VC-/J4&J5`；`destination=P3` |
| 电源 | PoE 输出与外部输入汇流 | `poe_output=P3 VOUT -> D3 SS54 -> INF+`；`poe_return=P3 GND -> GND`；`external_input=J1 -> INF+`；`downstream=INF+ -> F1 -> IN+` |
| 核心器件 | P3 PoE 模块身份 | `reference=P3`；`visible_part_number=HDR_6P`；`manufacturer_shown=false`；`module_model_shown=false`；`ratings_shown=false` |
| 保护电路 | 汇流输入保护 | `path=INF+ -> F1 PPTC-1812 -> IN+ -> U2 VIN`；`input_capacitors=C9/C10 2.2uF`；`return=GND` |
| 电源 | IN+ 到 +5V 降压 | `input=IN+`；`output=+5V`；`diode=D1 B290B`；`inductor=L1 8.2uH`；`output_capacitors=C2/C3 10uF`；`feedback=R4 51KΩ; R6 10KΩ`；`enable=U2 pin3 EN shown NC` |
| 电源 | +5V 到 D3V3 LDO | `input=+5V`；`enable=+5V`；`output=D3V3`；`input_capacitor=C5 100nF`；`output_capacitor=C7 100nF`；`bypass=C6 470pF` |
| 电源 | A3V3/D3V3 与 AGND/GND 分区 | `supply_bridge=R1 120Ω/MB: D3V3 to A3V3`；`ground_bridge=R3 0Ω: GND to AGND`；`analog_bulk=C4 100uF` |
| 电源 | W5500 电源去耦 | `analog=C19-C24 100nF; C27 4.7uF; C18 10nF`；`digital=C25 100nF; C26 10uF`；`analog_ground=AGND`；`digital_ground=GND` |
| 总线 | W5500 SPI 映射 | `controller=M5Stack host`；`device=U3 W5500`；`mosi=pin35 GPIO23`；`miso=pin34 GPIO19`；`sclk=pin33 GPIO18`；`cs=pin32 GPIO26`；`cs_pullup=R16 10KΩ to D3V3` |
| GPIO 与控制信号 | W5500 复位与中断 | `reset=U3 pin37 RSTn -> GPIO13; R8 10KΩ`；`interrupt=U3 pin36 INTn -> GPIO34; R13 10KΩ`；`rail=D3V3` |
| 复位 | W5500 硬件复位路径 | `host_gpio=GPIO13`；`device_pin=U3 pin37 RSTn`；`pullup=R8 10KΩ to D3V3`；`reset_button_shown=false` |
| GPIO 与控制信号 | W5500 PMODE 配置 | `signals=PMODE0, PMODE1, PMODE2`；`array=R7 10KΩ (103) ±5% 4P`；`rail=D3V3` |
| 时钟 | W5500 25MHz 时钟 | `frequency=25MHz`；`crystal=Y1 25MHz 12PF 10PPM`；`pins=XO pin31; XI/CLKIN pin30`；`feedback=R20 1MΩ`；`load=C14/C17 18pF` |
| 模拟电路 | W5500 EXRES1 外部电阻 | `pin=U3 pin10 EXRES1`；`reference=R19`；`visible_values=12KΩ / 12.4K`；`ground=AGND` |
| 总线 | W5500 PHY 差分对 | `transmit=U3 pin1 TXN / pin2 TXP -> U4 pin3 TD- / pin1 TD+`；`receive=U3 pin5 RXN / pin6 RXP -> U4 pin6 RD- / pin4 RD+`；`rail=A3V3/AGND` |
| 模拟电路 | PHY 偏置与耦合网络 | `tx_center=R10 10Ω to A3V3`；`tx_bias=R11/R12 49.9Ω`；`rx_series=C11/C12 6.8nF`；`rx_resistors=R17/R18 49.9Ω`；`rx_capacitors=C15 22nF; C16 10nF` |
| 接口 | RJ45 链路和活动指示 | `link=U3 pin25 -> U4 LINKLED`；`activity=U3 pin27 -> U4 ACTLED`；`resistors=R14/R15 1KΩ to D3V3`；`duplex_connected=false` |
| 接口 | J2 串口侧接口 | `rx=GPIO5`；`tx=GPIO15`；`vcc=+5V`；`ground=GND`；`host=M5Stack_BUS GPIO5/GPIO15` |
| 总线 | 可选 RS485/RS232 转接板 | `documented_rs485=SP3485EE`；`documented_rs232=MAX232`；`ttl_header=J2 GPIO5/GPIO15/+5V/GND`；`terminal_header=P2 I/O1-I/O6`；`transceivers_shown=false`；`routing_shown=false` |
| 接口 | M5Stack_BUS 关键映射 | `spi=GPIO23, GPIO19, GPIO18, GPIO26`；`control=GPIO13, GPIO34`；`serial=GPIO5, GPIO15`；`power=pin25 IN+/HPWR; pin28 +5V; pin30 BATTERY` |
| 电源 | +5V 电源指示 | `rail=+5V`；`led=D2 LED 0603`；`resistor=R9 4.7KΩ`；`return=GND` |
| 保护电路 | RJ45 屏蔽耦合 | `capacitor=C13 1nF (102) 10% 2000V`；`return=GND`；`connector=U4 HJBJ-6308ANLF` |
| 存储 | 板载存储 | `flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false` |
| 调试与烧录 | 专用调试接口 | `jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`debug_connector_shown=false` |

## 待确认事项

- `component.poe-module-identity`：P3 在当前页面只标为 HDR_6P，并显示 VA1/VA2/VB1/VB2/GND/VOUT，没有制造商、模块料号、输入范围、隔离等级或输出额定值。（证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页左中上 P3，仅见 HDR_6P 和六个信号名）
- `bus.optional-serial-transceivers`：产品正文列出 SP3485EE 与 MAX232 转接功能，但当前原理图只显示 J2 的 GPIO5/GPIO15 TTL 串口和 P2 I/O1-I/O6，未画出两种收发器、P2 路由、方向控制或总线保护。（证据：图 03bbcb4a5f2c / 第 1 页 / 第 1 页 J2/P2 与完整单页器件，未见 SP3485EE、MAX232、A/B 或 RS232 电平网络）
- `review.poe-module-identity`：P3 PoE 模块的具体料号、IEEE 802.3af 兼容范围、隔离等级与输出额定值是什么？；原因：当前原理图只将 P3 标为 HDR_6P 并给出六个引脚，无法验证模块选型和额定参数。
- `review.serial-adapter-circuits`：K012-C 配套 RS485/RS232 转接板的确切料号、J2/P2 针脚对应、方向控制、终端和保护电路是什么？；原因：当前主板原理图未包含 SP3485EE/MAX232 转接板电路，也没有 J2 到 P2 的连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `03bbcb4a5f2caeaf4235f2f6c90753231605d32d9cd7fd070fe655517f6a556b` | `https://static-cdn.m5stack.com/resource/docs/products/base/w5500PoE/w5500PoE_sch_01.webp` |

---

源文档：`zh_CN/base/w5500PoE.md`

源文档 SHA-256：`57aa096bd9fdcc625e4e05ba693be2e3de8d42091bfe40a38d054ad2424dea8d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
