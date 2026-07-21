# Module13.2 LAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 LAN |
| SKU | M136 |
| 产品 ID | `module13-2-lan-55693d26da93` |
| 源文档 | `zh_CN/module/LAN Module 13.2.md` |

## 概述

Module13.2 LAN 以 U3 W5500 通过 GPIO23/GPIO19/GPIO18 的 SPI 接入 M5-Bus，P3/P4/P5 三组跳线分别选择 CSN、RSTN 和 INTN 的主机 GPIO。W5500 的 TXP/TXN、RXP/RXN 经 T1 11FB-05NL 隔离变压器连接 J5 HC-RJ45-053-5，并配置差分端接、Bob Smith 终端和链路/活动 LED。外部 12/24V 经 F1/D4 保护和 U2 MP1584EN 降至 +5V，U1 BL8075CB5TR33 再产生 D3V3，FB1/R3 将 D3V3/GND 与 A3V3/AGND 相连；协议、缓存容量和 10/100M 自适应能力需结合 W5500 资料确认。

## 检索关键词

`Module13.2 LAN`、`M136`、`W5500`、`MP1584EN`、`BL8075CB5TR33`、`11FB-05NL`、`HC-RJ45-053-5`、`SPI`、`GPIO23 MOSI`、`GPIO19 MISO`、`GPIO18 SCLK`、`CSN`、`RSTN`、`INTN`、`P3`、`P4`、`P5`、`25MHz`、`Y1`、`TXP`、`TXN`、`RXP`、`RXN`、`ACTLED`、`LINKLED`、`IN12/24V`、`IN+`、`+5V`、`D3V3`、`A3V3`、`AGND`、`PPTC-1812`、`SD24`、`LESD3Z5.0CMT1G`、`RJ45`、`M5Stack_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | W5500 | SPI 接口硬件以太网控制器，连接主机 SPI/控制信号、25MHz 时钟与以太网差分前端 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 B2-D3 U3 W5500，TX/RX、SPI、INT/RST、时钟、电源和 LED 引脚 |
| Y1 | 25MHZ 12PF 10PPM | W5500 XI/XO 外部晶振 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 D3 Y1 25MHZ 12PF 10PPM，连接 XI/XO，C14/C17 各 18pF |
| T1 | 11FB-05NL | W5500 差分侧与 RJ45 线缆侧之间的以太网隔离变压器 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 C1-C2 T1 11FB-05NL，TX/RX 两组绕组与中心抽头 |
| J5 | HC-RJ45-053-5 | RJ45 以太网接口，连接 ETX+/ETX-/ERX+/ERX- 并集成 ACT/LINK LED 引脚 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 B1-C1 J5 HC-RJ45-053-5，1~12 脚 |
| U2 | MP1584EN | 将受保护的 IN+ 输入降压为 +5V | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1-B2 U2 MP1584EN，VIN/SW/FB/BST/FREQ/COMP 与 L1 |
| U1 | BL8075CB5TR33 | 将 +5V 稳压为 D3V3 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A3-A4 U1 BL8075CB5TR33，VIN +5V、VOUT D3V3 |
| J1 | PWR3.5 | 12/24V 外部直流输入插座 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1 J1 PWR3.5 与 INF+/GND |
| F1 | PPTC-1812 | INF+ 到 IN+ 的可恢复保险器件 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1 F1 PPTC-1812 串联 INF+ 与 IN+ |
| D4 | SD24 | INF+ 对 GND 的输入瞬态保护器件 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1 D4 SD24 跨接 INF+ 与 GND |
| D3 | LESD3Z5.0CMT1G | +5V 电源轨对 GND 的瞬态/ESD 保护器件 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A2 D3 LESD3Z5.0CMT1G 跨接 +5V 与 GND |
| FB1/R3 | 120Ω/MB / 0Ω | 连接 D3V3-A3V3 与 GND-AGND 的模拟电源/地桥接器件 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A4-B4 FB1 120Ω/MB 与 R3 0Ω |
| P3/P4/P5 | Header 3 | CSN、RSTN、INTN 三组 GPIO 选择跳线 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A3-A4 P3/P4/P5 Header 3 与 GPIO/CSN/RSTN/INTN 标签 |
| J3/J4 | M5Stack_BUS | 30 针堆叠总线，引出 SPI、GPIO、电源、电池与高功率输入 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 C4-D4 J3/J4 M5Stack_BUS，1~30 脚 |
| R7 | 10KΩ(103)±5% resistor array | W5500 PMODE0/1/2 配置上拉电阻阵列 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 B2 U3 上方 R7，D3V3 到 PMODE0/1/2 |
| P1/P2 | Header 4 | 原理图中预留但未连接任何网络的两组四针接口 | 图 56aa59f6cd71 / 第 1 页 / 第 1 页 A4-B4 P1/P2 Header 4，1~4 脚均无连线 |

## 系统结构

### Module13.2 LAN

U3 W5500 通过主机 SPI 与可选 CSN/RSTN/INTN 连接 M5-Bus，TX/RX 差分对经 T1 隔离后到 J5；J1 输入经 U2 生成 +5V，再由 U1 生成 D3V3/A3V3。

- 参数与网络：`ethernet_controller=U3 W5500`；`host_bus=SPI`；`magnetics=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5`；`power=J1 -> U2 +5V -> U1 D3V3/A3V3`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页全图电源、W5500、变压器、RJ45 与 M5Stack_BUS

## 核心器件

### U3

以太网控制器位号 U3，型号标为 W5500。

- 参数与网络：`reference=U3`；`part_number=W5500`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C2-D3 U3 W5500

## 电源

### 12/24V 输入保护

J1 的 INF+ 经 F1 PPTC-1812 串联形成 IN+，D4 SD24 从 INF+ 接 GND，C9/C10 各 2.2uF 从 IN+ 接地。

- 参数与网络：`connector=J1 PWR3.5`；`input=INF+`；`resettable_fuse=F1 PPTC-1812`；`protected_net=IN+`；`tvs=D4 SD24`；`input_caps=C9,C10 2.2uF`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1 J1/F1/D4/C9/C10

### U2 MP1584EN

U2.7 VIN 接 IN+，U2.1 SW 经 L1 10uH 输出 +5V；R2 82K/R4 15K 构成 FB 分压，C2/C3 各 22uF 滤波，D3 LESD3Z5.0CMT1G 保护 +5V。

- 参数与网络：`input=U2.7 IN+`；`switch=U2.1 SW`；`inductor=L1 10uH`；`output=+5V`；`feedback=R2 82K,R4 15K`；`output_caps=C2,C3 22uF`；`protection=D3 LESD3Z5.0CMT1G`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A1-B2 U2、L1、反馈与 +5V 输出

### U1 BL8075CB5TR33

U1.1 VIN 接 +5V，U1.5 VOUT 输出 D3V3，U1.2/.3 GND 接地；C5/C6 各 10uF 位于输入/输出侧。

- 参数与网络：`input=+5V`；`output=D3V3`；`ground=GND`；`input_cap=C5 10uF`；`output_cap=C6 10uF`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A3-A4 U1/C5/C6

### D3V3/A3V3 与 GND/AGND

FB1 标注 120Ω/MB，连接 D3V3 与 A3V3；R3 0Ω 连接 GND 与 AGND。W5500 的数字电源使用 D3V3，模拟电源引脚使用 A3V3/AGND。

- 参数与网络：`power_bridge=FB1 120Ω/MB D3V3-A3V3`；`ground_bridge=R3 0R GND-AGND`；`digital_rail=D3V3`；`analog_rail=A3V3`；`analog_ground=AGND`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A4-B4 FB1/R3 与 U3 周围 D3V3/A3V3/GND/AGND

## 接口

### T1 到 J5 RJ45

T1 线缆侧 TX+/TX- 连接 J5 ETX+/ETX-，RX+/RX- 连接 J5 ERX+/ERX-；T1 在 W5500 与 RJ45 之间提供磁性隔离。

- 参数与网络：`tx_path=T1 TX+/TX- -> J5 ETX+/ETX-`；`rx_path=T1 RX+/RX- -> J5 ERX+/ERX-`；`transformer=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C1 J5 与 T1 的 ETX/ERX 差分连线

### RJ45 活动/链路 LED

U3.27 ACTLED 连接 J5 ACTLED，U3.25 LINKLED 连接 J5 LINKLED；两路分别通过 R15/R14 1K 上拉至 D3V3。

- 参数与网络：`activity=U3.27 ACTLED -> J5.9/10 via R15 1K to D3V3`；`link=U3.25 LINKLED -> J5.11/12 via R14 1K to D3V3`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 B1 J5 ACTLED/LINKLED 与 C3 U3.27/U3.25

### J3/J4 M5Stack_BUS

总线 1/3/5 脚接 GND，7/9/11 脚为 GPIO23/19/18 SPI，2/26 为 GPIO35/GPIO34，20/23 为 GPIO5/GPIO15，22/24 为 GPIO13/GPIO0，12 为 +3.3V，28 为 +5V，25 为 IN+，27/29 为 HPWR。

- 参数与网络：`ground=pins 1,3,5`；`spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18`；`int_options=pin2 GPIO35,pin26 GPIO34`；`cs_options=pin20 GPIO5,pin23 GPIO15`；`reset_options=pin22 GPIO13,pin24 GPIO0`；`3v3=pin12`；`5v=pin28`；`external_input=pin25 IN+`；`hpwr=pins27,29`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C4-D4 M5Stack_BUS 1~30 脚与外部网络

## 总线

### W5500 SPI

U3.35 MOSI 接 GPIO23，U3.34 MISO 接 GPIO19，U3.33 SCLK 接 GPIO18，U3.32 SCSn 接 CSN；GPIO23/19/18 分别连接 M5Stack_BUS.7/.9/.11。

- 参数与网络：`mosi=U3.35 GPIO23 -> bus pin 7`；`miso=U3.34 GPIO19 -> bus pin 9`；`sclk=U3.33 GPIO18 -> bus pin 11`；`chip_select=U3.32 CSN selectable by P3`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C3 U3 SPI 32~35 脚与 C4-D4 M5Stack_BUS GPIO23/19/18

## GPIO 与控制信号

### P3 CSN 选择

P3.2 为 CSN，P3.1 为 GPIO5，P3.3 为 GPIO15，可用跳线将 W5500 CSN 连接至 GPIO5 或 GPIO15。

- 参数与网络：`center=P3.2 CSN`；`option_1=P3.1 GPIO5 / bus pin 20`；`option_2=P3.3 GPIO15 / bus pin 23`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A3 P3 GPIO5/CSN/GPIO15 与总线同名 GPIO

### P5 INTN 选择

P5.2 为 INTN，P5.1 为 GPIO35，P5.3 为 GPIO34；INTN 来自 U3.36，并由 R13 10K 上拉至 D3V3。

- 参数与网络：`interrupt_pin=U3.36 INTn`；`pullup=R13 10K to D3V3`；`option_1=P5.1 GPIO35 / bus pin 2`；`option_2=P5.3 GPIO34 / bus pin 26`；`direction=U3 to host`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A4 P5 与 C3 U3.36 INTn/R13

### W5500 PMODE 配置

R7 四联 10KΩ 阵列由 D3V3 上拉 U3 的 PMODE0/PMODE1/PMODE2 配置脚；具体模式编码需结合 W5500 datasheet。

- 参数与网络：`resistor_array=R7 10KΩ(103)±5%`；`signals=PMODE0,PMODE1,PMODE2`；`rail=D3V3`；`mode_value=requires datasheet decoding`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 B2 U3 上方 R7 与 PMODE0/1/2

## 时钟

### W5500 时钟

Y1 标注 25MHZ 12PF 10PPM，跨接 U3.31 XO 与 U3.30 XI/CLKIN；C14/C17 各 18pF 从 XO/XI 接 GND。

- 参数与网络：`crystal=Y1`；`frequency=25MHz`；`load_spec=12pF`；`tolerance=10PPM`；`xo=U3.31`；`xi=U3.30`；`caps=C14,C17 18pF`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 D3 Y1、XO/XI、C14/C17

## 复位

### P4 RSTN 选择

P4.2 为 RSTN，P4.1 为 GPIO0，P4.3 为 GPIO13；RSTN 连接 U3.37，并由 R8 10K 上拉至 D3V3。

- 参数与网络：`reset_pin=U3.37 RSTn`；`pullup=R8 10K to D3V3`；`option_1=P4.1 GPIO0 / bus pin 24`；`option_2=P4.3 GPIO13 / bus pin 22`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A3 P4 与 B3 U3.37 RSTn/R8

## 保护电路

### RJ45 线侧端接

J5 四条线侧网络各经 C7/C8/C15/C29 22nF 与 R22/R23/R24/R25 75Ω 汇合，公共点经 C13 1nF 2000V 接 GND。

- 参数与网络：`series_caps=C7,C8,C15,C29 22nF`；`termination_resistors=R22,R23,R24,R25 75R`；`common_cap=C13 1nF 2000V`；`reference=GND`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C1-D1 J5 下方四路 22nF/75R 与 C13 高压电容

## 射频

### W5500 MDI 差分线

U3.1/.2 的 TXN/TXP 连接 T1 的 TX_N/TX_P，U3.5/.6 的 RXN/RXP 连接 T1 的 RX_N/RX_P；TX 侧串有 R10 10R 及 R11/R12 49.9R 网络，RX 侧配置 C11/C12 6.8nF、R17/R18 49.9R 等网络。

- 参数与网络：`tx=U3 TXN/TXP -> TX_N/TX_P -> T1`；`rx=T1 -> RX_N/RX_P -> U3 RXN/RXP`；`tx_network=R10 10R,R11/R12 49.9R`；`rx_network=C11/C12 6.8nF,R17/R18 49.9R`
- 证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 C1-C3 T1 与 U3 之间 TX/RX 差分匹配网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 LAN | `ethernet_controller=U3 W5500`；`host_bus=SPI`；`magnetics=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5`；`power=J1 -> U2 +5V -> U1 D3V3/A3V3` |
| 核心器件 | U3 | `reference=U3`；`part_number=W5500` |
| 总线 | W5500 SPI | `mosi=U3.35 GPIO23 -> bus pin 7`；`miso=U3.34 GPIO19 -> bus pin 9`；`sclk=U3.33 GPIO18 -> bus pin 11`；`chip_select=U3.32 CSN selectable by P3` |
| GPIO 与控制信号 | P3 CSN 选择 | `center=P3.2 CSN`；`option_1=P3.1 GPIO5 / bus pin 20`；`option_2=P3.3 GPIO15 / bus pin 23` |
| 复位 | P4 RSTN 选择 | `reset_pin=U3.37 RSTn`；`pullup=R8 10K to D3V3`；`option_1=P4.1 GPIO0 / bus pin 24`；`option_2=P4.3 GPIO13 / bus pin 22` |
| GPIO 与控制信号 | P5 INTN 选择 | `interrupt_pin=U3.36 INTn`；`pullup=R13 10K to D3V3`；`option_1=P5.1 GPIO35 / bus pin 2`；`option_2=P5.3 GPIO34 / bus pin 26`；`direction=U3 to host` |
| 时钟 | W5500 时钟 | `crystal=Y1`；`frequency=25MHz`；`load_spec=12pF`；`tolerance=10PPM`；`xo=U3.31`；`xi=U3.30`；`caps=C14,C17 18pF` |
| 射频 | W5500 MDI 差分线 | `tx=U3 TXN/TXP -> TX_N/TX_P -> T1`；`rx=T1 -> RX_N/RX_P -> U3 RXN/RXP`；`tx_network=R10 10R,R11/R12 49.9R`；`rx_network=C11/C12 6.8nF,R17/R18 49.9R` |
| 接口 | T1 到 J5 RJ45 | `tx_path=T1 TX+/TX- -> J5 ETX+/ETX-`；`rx_path=T1 RX+/RX- -> J5 ERX+/ERX-`；`transformer=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5` |
| 保护电路 | RJ45 线侧端接 | `series_caps=C7,C8,C15,C29 22nF`；`termination_resistors=R22,R23,R24,R25 75R`；`common_cap=C13 1nF 2000V`；`reference=GND` |
| 接口 | RJ45 活动/链路 LED | `activity=U3.27 ACTLED -> J5.9/10 via R15 1K to D3V3`；`link=U3.25 LINKLED -> J5.11/12 via R14 1K to D3V3` |
| 电源 | 12/24V 输入保护 | `connector=J1 PWR3.5`；`input=INF+`；`resettable_fuse=F1 PPTC-1812`；`protected_net=IN+`；`tvs=D4 SD24`；`input_caps=C9,C10 2.2uF` |
| 电源 | U2 MP1584EN | `input=U2.7 IN+`；`switch=U2.1 SW`；`inductor=L1 10uH`；`output=+5V`；`feedback=R2 82K,R4 15K`；`output_caps=C2,C3 22uF`；`protection=D3 LESD3Z5.0CMT1G` |
| 电源 | U1 BL8075CB5TR33 | `input=+5V`；`output=D3V3`；`ground=GND`；`input_cap=C5 10uF`；`output_cap=C6 10uF` |
| 电源 | D3V3/A3V3 与 GND/AGND | `power_bridge=FB1 120Ω/MB D3V3-A3V3`；`ground_bridge=R3 0R GND-AGND`；`digital_rail=D3V3`；`analog_rail=A3V3`；`analog_ground=AGND` |
| GPIO 与控制信号 | W5500 PMODE 配置 | `resistor_array=R7 10KΩ(103)±5%`；`signals=PMODE0,PMODE1,PMODE2`；`rail=D3V3`；`mode_value=requires datasheet decoding` |
| 接口 | J3/J4 M5Stack_BUS | `ground=pins 1,3,5`；`spi=pin7 GPIO23, pin9 GPIO19, pin11 GPIO18`；`int_options=pin2 GPIO35,pin26 GPIO34`；`cs_options=pin20 GPIO5,pin23 GPIO15`；`reset_options=pin22 GPIO13,pin24 GPIO0`；`3v3=pin12`；`5v=pin28`；`external_input=pin25 IN+`；`hpwr=pins27,29` |
| 接口 | P1/P2 Header 4 | `P1_pin_count=4`；`P2_pin_count=4`；`connections_shown=false`；`purpose=null`；`pinout=null` |
| 内存与 Flash | 正文中的 W5500 缓存 | `controller=W5500`；`buffer_present_documented=true`；`buffer_size_on_schematic=null`；`external_memory_shown=false` |
| 总线 | 正文中的网络协议与速率 | `documented_protocols=TCP,UDP,IPv4,ICMP,ARP,IGMP,PPPoE`；`documented_link=10/100M auto-negotiation`；`protocols_on_schematic=null`；`speed_on_schematic=null` |
| 保护电路 | 接口 ESD 可见性 | `power_tvs=D4 SD24,D3 LESD3Z5.0CMT1G`；`resettable_fuse=F1 PPTC-1812`；`magnetic_isolation=T1`；`spi_esd_shown=false`；`rj45_line_esd_array_shown=false` |

## 待确认事项

- `interface.unconnected-headers`：P1 和 P2 均画为四针接口，但本页四个针脚均无网络连接或功能标注，无法确认其扩展用途与针序。（证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 A4-B4 P1/P2 Header 4 无连线）
- `memory.documented-w5500-buffer`：产品正文称 W5500 集成数据包缓存区，但原理图只确认 W5500 型号，未标缓存容量、分配或外部存储器；具体缓存参数需查芯片 datasheet。（证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 U3 W5500，无缓存容量或外部存储器）
- `bus.documented-protocols-speed`：产品正文列出 TCP、UDP、IPv4、ICMP、ARP、IGMP、PPPoE 及 10/100M 自适应；原理图未标协议栈或链路速率，因此这些能力需由 W5500 与磁性器件/RJ45 datasheet 确认。（证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页 U3/T1/J5 电路无协议或 10/100M 字样）
- `protection.spi-rj45-esd-not-visible`：页面显示电源 TVS/PPTC 与 RJ45 端接隔离网络，但未显示 SPI/跳线 GPIO 或 RJ45 差分线专用 ESD 阵列，额外端口 ESD 保护需确认。（证据：图 56aa59f6cd71 / 第 1 页 / 第 1 页全图保护器件与 J5/P3-P5/M5Stack_BUS 区）
- `review.extension-headers`：请确认 P1/P2 的实际扩展用途、针脚定义和是否装配。；原因：本页只画无连线 Header 4，无法从图中恢复功能。
- `review.w5500-buffer`：请以本版本 W5500 datasheet 确认片上缓存容量及 TX/RX 分配能力。；原因：原理图仅给出料号，不含内部存储参数。
- `review.protocol-speed`：请确认 M136 的实际协议支持、10/100M 自协商能力及 T1/J5 组合的速率等级。；原因：协议与速率未直接标在原理图。
- `review.interface-esd`：请确认 RJ45 差分线及 SPI/跳线 GPIO 是否在 PCB 或其他资料中配置专用 ESD 保护。；原因：当前单页未画这些 ESD 阵列。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `56aa59f6cd713084b144932eaf682b42ea94fc006a295ef67f620dbbfe65b475` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/562/Sch_Module13.2_LAN_sch_01.png` |

---

源文档：`zh_CN/module/LAN Module 13.2.md`

源文档 SHA-256：`034929a75637a7934ca3f858664bdaa6fea03cdac9a206269c724b123b5f4c11`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
