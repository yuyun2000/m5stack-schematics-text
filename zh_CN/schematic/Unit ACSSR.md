# Unit ACSSR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ACSSR |
| SKU | U139 |
| 产品 ID | `unit-acssr-856e468edd0e` |
| 源文档 | `zh_CN/unit/acssr.md` |

## 概述

Unit ACSSR 控制板以 U4 ESP32-C3FH4 为主控，通过 J2 提供 I2C、通过 U3 SP3485EN-L/TR 提供 RS-485，并以 Q2 AO3400A 低侧驱动 P3 上的外接 SSR 控制端。VIN 经 F1、TVS D3 和 U1 ME3116AM6G 转换到 +5V，U2 HM8089 再生成 +3.3V；J2 的 5V 还可经 F2 接入 +5V。板上另有 SK6812 RGB、S1 按键、J1 下载口、X1 晶振、E1 ANT_IPEX 射频接口和 P1/P2 并联 RS485PWR 端子。

## 检索关键词

`Unit ACSSR`、`U139`、`ESP32-C3FH4`、`SP3485EN-L/TR`、`ME3116AM6G`、`HM8089`、`AO3400A`、`SS8050 Y1`、`SK6812`、`ANT_IPEX`、`HY-2.0_IIC`、`DownloadSocket`、`RS485_A`、`RS485_B`、`RS-485`、`Modbus`、`I2C`、`SCL`、`SDA`、`TXD`、`RXD`、`Ctl`、`Btn`、`RGB`、`CHIP_EN`、`GPIO9`、`U0TXD`、`U0RXD`、`VIN`、`+5V`、`+3.3V`、`P1`、`P2`、`P3`、`F1 24V@1.5A`、`F2 6V@1A`、`SP4021-01FTG-C`、`RLSD52A031V`、`0x50`、`SSR control`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | ESP32-C3FH4 | 系统主控，连接 I2C、RGB、按键、SSR 控制、RS-485 UART、下载与射频网络。 | 图 6b599219293d / 第 1 页 / source_004 网格 A2-C2，U4 ESP32-C3FH4 全部引脚网络 |
| U3 | SP3485EN-L/TR | 3.3V RS-485 收发器，B/A 连接 RS485_B/RS485_A，RO 接 RXD。 | 图 c6405b791c31 / 第 1 页 / source_003 网格 B2-B3，U3 SP3485EN-L/TR 及 RO/RE/DE/DI/B/A |
| U1 | ME3116AM6G | VIN 至 5V 中间轨的降压转换器，配合 L1、D1 和反馈网络。 | 图 043324c72c13 / 第 1 页 / source_002 网格 B2-B3，U1 ME3116AM6G、L1、D1、R2/R4 |
| U2 | HM8089 | +5V 至 +3.3V 的降压转换器，配合 L2、R5/R6 和输入输出电容。 | 图 043324c72c13 / 第 1 页 / source_002 网格 C2-D3，U2 HM8089、L2、R5/R6、C7-C10 |
| Q2 | AO3400A | P3 外接 SSR 控制回路的 N 沟道低侧 MOSFET。 | 图 ef8998d30ae1 / 第 1 页 / source_001 网格 B3，Q2 AO3400A、Ctl、R19/R21/R22、P3 |
| Q1 | SS8050 Y1 | 由 TXD 经 R12 驱动的 RS-485 RE/DE 控制晶体管。 | 图 c6405b791c31 / 第 1 页 / source_003 网格 B1-B2，TXD-R12-Q1 与 U3 RE/DE 节点 |
| LED1 | SK6812 | 由 RGB 网络驱动的可编程全彩 LED，工作于 +3.3V。 | 图 6b599219293d / 第 1 页 / source_004 网格 C3，LED1 SK6812、DIN RGB、VDD +3.3V |
| S1 | SW-PB | Btn 瞬时按键，按下时将 Btn 接 GND，R18 提供 10K 上拉。 | 图 6b599219293d / 第 1 页 / source_004 网格 D1，S1 SW-PB、Btn、R18、D12 |
| J1 | DownloadSocket | 六针下载接口，引出 +3.3V、U0TXD、U0RXD、CHIP_EN、GPIO9 和 GND。 | 图 6b599219293d / 第 1 页 / source_004 网格 A4，J1 DownloadSocket 1-6 脚 |
| J2 | HY-2.0_IIC | 四针 I2C 与 5V 供电接口，带 SCL/SDA/VCC 保护器件。 | 图 6b599219293d / 第 1 页 / source_004 网格 B4，J2 HY-2.0_IIC、F2、D9-D11 |
| P1,P2 | HDR_4P | 两组并联 RS485PWR 端子，均引出 RS485_B、RS485_A、VIN/12V+ 和 GND/12V-。 | 图 6b599219293d / 第 1 页 / source_004 网格 C4-D4，P1/P2 HDR_4P 的 B/A/12V+/12V- |
| P3 | Header 2 | 外接 SSR 控制端，两针分别为 +5V 与经 Q2/R22 低侧开关的回路端。 | 图 ef8998d30ae1 / 第 1 页 / source_001 网格 B3，P3 Header 2、+5V、R22/Q2 |
| E1 | ANT_IPEX | ESP32-C3 射频天线接口，通过 L3/C12/C13 匹配网络连接 U4 LAN_IN。 | 图 6b599219293d / 第 1 页 / source_004 网格 A2-A3，U4 LAN_IN-L3-C12/C13-E1 ANT_IPEX |
| X1 | TXC/8Z4000017 | U4 XTAL_P/XTAL_N 外部晶振，配合 L5 与 C23/C24。 | 图 6b599219293d / 第 1 页 / source_004 网格 C1-C2，X1 TXC/8Z4000017、L5 27nH、C23/C24 18pF |
| F1,F2 | 24V@1.5A / 6V@1A | VIN 输入与 J2 5V 输入的串联保险器件。 | 图 043324c72c13 / 第 1 页 / source_002 网格 B1，VIN-F1 24V@1.5A; 图 6b599219293d / 第 1 页 / source_004 网格 B4，+5V-F2 6V@1A-J2 VCC |
| D3,D5,D9,D10,D12 | SD24 / RLSD52A031V | VIN、+3.3V、SCL、SDA 和 Btn 网络的对地瞬态保护器件。 | 图 043324c72c13 / 第 1 页 / source_002 D3 SD24 位于 VIN 对地，D5 RLSD52A031V 位于 +3.3V 对地; 图 6b599219293d / 第 1 页 / source_004 D9/D10 位于 SCL/SDA 对地，D12 位于 Btn 对地 |
| D6,D7,D8 | SP4021-01FTG-C | RS485_B/RS485_A 的共模与差模浪涌/ESD 保护网络。 | 图 c6405b791c31 / 第 1 页 / source_003 网格 B3，D6-D8 SP4021-01FTG-C 位于 RS485_B/A 与 GND/线间 |
| D11 | LESD3Z5.0CMT1G | J2 VCC 5V 网络的对地保护器件。 | 图 6b599219293d / 第 1 页 / source_004 网格 B4-C4，J2 VCC 节点至 D11 LESD3Z5.0CMT1G/GND |

## 系统结构

### 系统架构

U4 ESP32-C3FH4 是控制核心，连接 J2 I2C、U3 RS-485、LED1 RGB、S1 Btn、Q2/P3 SSR 控制、J1 下载、X1 时钟和 E1 射频接口。

- 参数与网络：`controller=U4 ESP32-C3FH4`；`i2c=J2`；`rs485=U3 SP3485EN-L/TR`；`ssr_output=Q2/P3`；`rgb=LED1 SK6812`；`button=S1`；`debug=J1`；`rf=E1 ANT_IPEX`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 及 J1/J2/LED1/S1/E1/X1 网络; 图 c6405b791c31 / 第 1 页 / source_003 U3 RS-485 电路; 图 ef8998d30ae1 / 第 1 页 / source_001 Q2/P3 SSR 控制电路

## 核心器件

### U4 ESP32-C3FH4 关键 GPIO

U4 将 SCL/SDA 接 4/5 脚，RGB 接 GPIO2/6 脚，Btn 接 GPIO3/8 脚，Ctl 接 MTMS/9 脚，TXD/RXD 接 MTDI/10 脚与 MTCK/12 脚，U0RXD/U0TXD 接 27/28 脚。

- 参数与网络：`scl=pin4 XTAL_32K_P`；`sda=pin5 XTAL_32K_N`；`rgb=pin6 GPIO2`；`button=pin8 GPIO3`；`ctl=pin9 MTMS`；`txd=pin10 MTDI`；`rxd=pin12 MTCK`；`uart0_rx=pin27 U0RXD`；`uart0_tx=pin28 U0TXD`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 A1-B2，U4 左侧 SCL/SDA/RGB/Btn/Ctl/TXD/RXD 与 U0RXD/U0TXD

### LED1 SK6812

LED1 SK6812 的 DIN（3 脚）接 RGB，RGB 来自 U4 GPIO2/6 脚；VDD（4 脚）接 +3.3V、VSS（2 脚）接 GND，C22 100nF 跨接电源。

- 参数与网络：`device=LED1 SK6812`；`data_in=RGB/U4 GPIO2 pin6`；`vdd=+3.3V`；`ground=GND`；`decoupling=C22 100nF`；`data_out=LED1 pin1, no visible connection`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 A1 U4 RGB/GPIO2 与网格 C3 LED1/C22

## 电源

### VIN 输入路径

P1/P2 的 VIN/12V+ 网络经 F1（24V@1.5A）串联后进入 U1 电源级，D3 SD24 与 C2 100nF 从该输入节点接 GND。

- 参数与网络：`input_connectors=P1,P2`；`net=VIN`；`fuse=F1 24V@1.5A`；`tvs=D3 SD24`；`input_capacitor=C2 100nF`；`converter=U1 ME3116AM6G`
- 证据：图 6b599219293d / 第 1 页 / source_004 P1/P2 VIN/12V+; 图 043324c72c13 / 第 1 页 / source_002 VIN-F1-D3-C2-U1 输入路径

### U1 5V 降压级

U1 ME3116AM6G 通过 L1 10uH、D1 B5819W SL、R2 56K、R4 10K 和 C3 100pF 构成降压级；输出侧 C4-C6 各 22uF，并经 D2 B5819W SL 串联到 +5V。

- 参数与网络：`converter=U1 ME3116AM6G`；`inductor=L1 10uH`；`catch_diode=D1 B5819W SL`；`feedback_top=R2 56K`；`feedback_bottom=R4 10K`；`feedforward=C3 100pF`；`output_caps=C4,C5,C6 22uF`；`series_diode=D2 B5819W SL`；`output_rail=+5V`
- 证据：图 043324c72c13 / 第 1 页 / source_002 网格 B2-C4，U1-L1-D1-R2/R4-C3-C6-D2 电源链

### U2 3.3V 降压级

U2 HM8089 的 VIN 与 EN 接 +5V，SW 经 L2（3015 4.7uH）输出 +3.3V，反馈分压为 R5 68K/R6 15K；C7/C8 为输出电容，C9/C10 为输入电容。

- 参数与网络：`converter=U2 HM8089`；`input=+5V`；`enable=+5V`；`output=+3.3V`；`inductor=L2 3015 4.7uH`；`feedback=R5 68K,R6 15K`；`output_caps=C7 100nF,C8 22uF`；`input_caps=C9 22uF,C10 100nF`；`output_protection=D5 RLSD52A031V`
- 证据：图 043324c72c13 / 第 1 页 / source_002 网格 C2-D3，+5V-U2-L2-+3.3V 及 R5/R6/C7-C10/D5

### J2 5V 供电路径

J2.3 VCC 通过 F2（6V@1A）连接 +5V，VCC 节点由 D11 LESD3Z5.0CMT1G 对地保护；J2.4 为 GND。

- 参数与网络：`connector=J2`；`vcc_pin=3`；`ground_pin=4`；`rail=+5V`；`fuse=F2 6V@1A`；`protection=D11 LESD3Z5.0CMT1G`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 B4，+5V-F2-J2.3/D11 与 J2.4 GND

## 接口

### J2 HY-2.0_IIC

J2.1-J2.4 分别为 IIC_SCL/SCL、IIC_SDA/SDA、VCC/+5V、GND；SCL 与 SDA 各由 D9/D10 RLSD52A031V 对地保护。

- 参数与网络：`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND`；`scl_protection=D9 RLSD52A031V`；`sda_protection=D10 RLSD52A031V`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 B4，J2 1-4 脚与 D9-D11/F2

### P1/P2 RS485PWR

P1 与 P2 均为四针 HDR_4P，四个位置从上到下标注 B、A、12V+、12V-，分别连接 RS485_B、RS485_A、VIN、GND；两连接器网络并联。

- 参数与网络：`connectors=P1,P2`；`position_1=B/RS485_B`；`position_2=A/RS485_A`；`position_3=12V+/VIN`；`position_4=12V-/GND`；`topology=parallel`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 C4-D4，P1/P2 B/A/12V+/12V- 与 RS485_B/A/VIN/GND

### P3 外接 SSR 控制

P3.1 直接接 +5V；P3.2 经 R22 10Ω 连接 Q2 漏极，Q2 源极接 GND，形成受 Ctl 控制的低侧开关回路。

- 参数与网络：`connector=P3 Header 2`；`pin_1=+5V`；`pin_2=R22 10Ω to Q2 drain`；`switch=Q2 AO3400A`；`source=GND`；`control=Ctl`
- 证据：图 ef8998d30ae1 / 第 1 页 / source_001 网格 B3，P3.1/+5V、P3.2/R22/Q2/GND

## 总线

### I2C 总线

J2 的 SCL 与 SDA 直接连接 U4 的 4 脚 XTAL_32K_P 和 5 脚 XTAL_32K_N；原理图未显示外部 I2C 上拉电阻。

- 参数与网络：`controller=U4 ESP32-C3FH4`；`scl=J2.1 to U4 pin4 XTAL_32K_P`；`sda=J2.2 to U4 pin5 XTAL_32K_N`；`pullups=原理图未显示`；`protection=D9,D10`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 SCL/SDA 网络至 J2.1/J2.2

### RS-485 收发器连接

U3 SP3485EN-L/TR 以 +3.3V 供电，B/A 分别连接 RS485_B/RS485_A；RO 经 R8 1K 接 RXD，RE 与 DE 并联后由 R9 4.7K 上拉并由 Q1 下拉。

- 参数与网络：`transceiver=U3 SP3485EN-L/TR`；`supply=+3.3V`；`b_net=RS485_B`；`a_net=RS485_A`；`receiver_output=RO -> R8 1K -> RXD`；`direction_pins=RE pin2 tied DE pin3`；`direction_pullup=R9 4.7K`；`direction_driver=Q1 SS8050 Y1`
- 证据：图 c6405b791c31 / 第 1 页 / source_003 网格 B1-B3，U3、R8/R9、Q1、RS485_B/A

## GPIO 与控制信号

### TXD 与 RE/DE 自动方向节点

U4 的 TXD 网络来自 MTDI/10 脚，经 R12 4.7K 驱动 Q1 SS8050 Y1；Q1 集电极连接 U3 的 RE/DE 公共节点，发射极接 GND。

- 参数与网络：`mcu_pin=U4 MTDI pin10`；`net=TXD`；`base_resistor=R12 4.7K`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U3 RE pin2,DE pin3`；`default_pull=R9 4.7K to +3.3V`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 MTDI/10 脚 TXD; 图 c6405b791c31 / 第 1 页 / source_003 TXD-R12-Q1-RE/DE 电路

### GPIO9 下载控制

U4 GPIO9（15 脚）连接 GPIO9 网络，由 R15 10K 上拉到 +3.3V，并引出到 J1.5 G0。

- 参数与网络：`mcu_pin=U4 GPIO9 pin15`；`pullup=R15 10K to +3.3V`；`debug_pin=J1.5 G0`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 GPIO9/R15 与 J1.5 GPIO9/G0

### S1 Btn 按键

Btn 连接 U4 GPIO3/8 脚，由 R18 10K 上拉到 +3.3V；S1 按下把 Btn 接 GND，D12 RLSD52A031V 从 Btn 接 GND。

- 参数与网络：`mcu_pin=U4 GPIO3 pin8`；`net=Btn`；`switch=S1 SW-PB`；`active_connection=GND`；`pullup=R18 10K`；`protection=D12 RLSD52A031V`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 Btn/GPIO3 与网格 D1 S1/R18/D12

### Ctl 到 Q2

Ctl 来自 U4 MTMS/9 脚，经 R21 10Ω 连接 Q2 AO3400A 栅极，R19 51K 将 Ctl 下拉到 GND。

- 参数与网络：`mcu_pin=U4 MTMS pin9`；`net=Ctl`；`gate_resistor=R21 10Ω`；`pulldown=R19 51K`；`mosfet=Q2 AO3400A`
- 证据：图 6b599219293d / 第 1 页 / source_004 U4 Ctl/MTMS pin9; 图 ef8998d30ae1 / 第 1 页 / source_001 Ctl-R19/R21-Q2 电路

## 时钟

### U4 外部晶振

U4 XTAL_P（30 脚）经 L5 27nH 接 X1.1，U4 XTAL_N（29 脚）接 X1.3；C23/C24 各 18pF 对地，X1.2/X1.4 接 GND。

- 参数与网络：`crystal=X1 TXC/8Z4000017`；`xtal_p=U4 pin30 -> L5 27nH -> X1.1`；`xtal_n=U4 pin29 -> X1.3`；`load_caps=C23 18pF,C24 18pF`；`ground_pins=X1.2,X1.4`；`frequency=原理图未明确标注`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 C1-C2，XTAL_P/L5/X1/XTAL_N/C23/C24

## 复位

### CHIP_EN

U4 CHIP_EN（7 脚）由 R14 10K 上拉到 +3.3V，并由 C16 1.0uF 接 GND，同时引出到 J1.4 EN。

- 参数与网络：`mcu_pin=U4 CHIP_EN pin7`；`pullup=R14 10K to +3.3V`；`capacitor=C16 1.0uF to GND`；`debug_pin=J1.4 EN`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 A2-B3，U4 CHIP_EN、R14/C16 与 J1.4

## 保护电路

### RS-485 偏置、终端与浪涌保护

RS485_B 经 R7 4.7K 接 GND，RS485_A 经 R11 4.7K 接 +3.3V；R10 标注 120Ω/NC 并接 A/B，D6-D8 SP4021-01FTG-C 分别提供线对地与线间保护。

- 参数与网络：`b_bias=R7 4.7K to GND`；`a_bias=R11 4.7K to +3.3V`；`termination=R10 120Ω/NC between A and B`；`b_to_ground=D6 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C`；`a_to_ground=D8 SP4021-01FTG-C`
- 证据：图 c6405b791c31 / 第 1 页 / source_003 网格 B3，R7/R10/R11 与 D6-D8 的 RS485_B/A 网络

## 存储

### 外部存储

四页原理图未显示独立 Flash、EEPROM、SD 卡或其他外部存储器件。

- 参数与网络：`controller=U4 ESP32-C3FH4`；`external_flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`
- 证据：图 6b599219293d / 第 1 页 / source_004 全页主控及外围，无外部存储器位号或存储接口

## 射频

### E1 射频路径

U4 LAN_IN（1 脚）经 C12 2.7pF 对地、L3 2.7nH 串联和 C13 2.4pF 对地的匹配网络连接 E1 ANT_IPEX。

- 参数与网络：`controller_pin=U4 LAN_IN pin1`；`shunt_input=C12 2.7pF`；`series_inductor=L3 2.7nH`；`shunt_output=C13 2.4pF`；`connector=E1 ANT_IPEX`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 A2-A3，U4 LAN_IN-C12-L3-C13-E1

## 调试与烧录

### J1 DownloadSocket

J1.1-J1.6 依次为 +3.3V、TXD/U0TXD、RXD/U0RXD、EN/CHIP_EN、G0/GPIO9、GND；U0TXD 路径含 R17 510Ω。

- 参数与网络：`pin_1=+3.3V`；`pin_2=TXD/U0TXD`；`pin_3=RXD/U0RXD`；`pin_4=EN/CHIP_EN`；`pin_5=G0/GPIO9`；`pin_6=GND`；`tx_series=R17 510Ω`
- 证据：图 6b599219293d / 第 1 页 / source_004 网格 A4，J1 1-6 脚；网格 B1-B2 U4 U0RXD/U0TXD/R17

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统架构 | `controller=U4 ESP32-C3FH4`；`i2c=J2`；`rs485=U3 SP3485EN-L/TR`；`ssr_output=Q2/P3`；`rgb=LED1 SK6812`；`button=S1`；`debug=J1`；`rf=E1 ANT_IPEX` |
| 核心器件 | U4 ESP32-C3FH4 关键 GPIO | `scl=pin4 XTAL_32K_P`；`sda=pin5 XTAL_32K_N`；`rgb=pin6 GPIO2`；`button=pin8 GPIO3`；`ctl=pin9 MTMS`；`txd=pin10 MTDI`；`rxd=pin12 MTCK`；`uart0_rx=pin27 U0RXD`；`uart0_tx=pin28 U0TXD` |
| 电源 | VIN 输入路径 | `input_connectors=P1,P2`；`net=VIN`；`fuse=F1 24V@1.5A`；`tvs=D3 SD24`；`input_capacitor=C2 100nF`；`converter=U1 ME3116AM6G` |
| 电源 | U1 5V 降压级 | `converter=U1 ME3116AM6G`；`inductor=L1 10uH`；`catch_diode=D1 B5819W SL`；`feedback_top=R2 56K`；`feedback_bottom=R4 10K`；`feedforward=C3 100pF`；`output_caps=C4,C5,C6 22uF`；`series_diode=D2 B5819W SL`；`output_rail=+5V` |
| 电源 | U2 3.3V 降压级 | `converter=U2 HM8089`；`input=+5V`；`enable=+5V`；`output=+3.3V`；`inductor=L2 3015 4.7uH`；`feedback=R5 68K,R6 15K`；`output_caps=C7 100nF,C8 22uF`；`input_caps=C9 22uF,C10 100nF`；`output_protection=D5 RLSD52A031V` |
| 电源 | J2 5V 供电路径 | `connector=J2`；`vcc_pin=3`；`ground_pin=4`；`rail=+5V`；`fuse=F2 6V@1A`；`protection=D11 LESD3Z5.0CMT1G` |
| 接口 | J2 HY-2.0_IIC | `pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND`；`scl_protection=D9 RLSD52A031V`；`sda_protection=D10 RLSD52A031V` |
| 总线 | I2C 总线 | `controller=U4 ESP32-C3FH4`；`scl=J2.1 to U4 pin4 XTAL_32K_P`；`sda=J2.2 to U4 pin5 XTAL_32K_N`；`pullups=原理图未显示`；`protection=D9,D10` |
| 总线地址 | I2C 地址 | `documented_candidate=0x50`；`schematic_address=未标注`；`address_straps=未显示`；`firmware_defined=需确认` |
| 总线 | RS-485 收发器连接 | `transceiver=U3 SP3485EN-L/TR`；`supply=+3.3V`；`b_net=RS485_B`；`a_net=RS485_A`；`receiver_output=RO -> R8 1K -> RXD`；`direction_pins=RE pin2 tied DE pin3`；`direction_pullup=R9 4.7K`；`direction_driver=Q1 SS8050 Y1` |
| GPIO 与控制信号 | TXD 与 RE/DE 自动方向节点 | `mcu_pin=U4 MTDI pin10`；`net=TXD`；`base_resistor=R12 4.7K`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U3 RE pin2,DE pin3`；`default_pull=R9 4.7K to +3.3V` |
| 总线 | U3 DI 发送数据路径 | `transceiver_pin=U3 DI pin4`；`visible_connection=未显示`；`txd_visible_path=TXD -> R12 -> Q1 base`；`impact=发送数据路径无法闭环` |
| 保护电路 | RS-485 偏置、终端与浪涌保护 | `b_bias=R7 4.7K to GND`；`a_bias=R11 4.7K to +3.3V`；`termination=R10 120Ω/NC between A and B`；`b_to_ground=D6 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C`；`a_to_ground=D8 SP4021-01FTG-C` |
| 接口 | P1/P2 RS485PWR | `connectors=P1,P2`；`position_1=B/RS485_B`；`position_2=A/RS485_A`；`position_3=12V+/VIN`；`position_4=12V-/GND`；`topology=parallel` |
| 调试与烧录 | J1 DownloadSocket | `pin_1=+3.3V`；`pin_2=TXD/U0TXD`；`pin_3=RXD/U0RXD`；`pin_4=EN/CHIP_EN`；`pin_5=G0/GPIO9`；`pin_6=GND`；`tx_series=R17 510Ω` |
| 复位 | CHIP_EN | `mcu_pin=U4 CHIP_EN pin7`；`pullup=R14 10K to +3.3V`；`capacitor=C16 1.0uF to GND`；`debug_pin=J1.4 EN` |
| GPIO 与控制信号 | GPIO9 下载控制 | `mcu_pin=U4 GPIO9 pin15`；`pullup=R15 10K to +3.3V`；`debug_pin=J1.5 G0` |
| GPIO 与控制信号 | S1 Btn 按键 | `mcu_pin=U4 GPIO3 pin8`；`net=Btn`；`switch=S1 SW-PB`；`active_connection=GND`；`pullup=R18 10K`；`protection=D12 RLSD52A031V` |
| GPIO 与控制信号 | Ctl 到 Q2 | `mcu_pin=U4 MTMS pin9`；`net=Ctl`；`gate_resistor=R21 10Ω`；`pulldown=R19 51K`；`mosfet=Q2 AO3400A` |
| 接口 | P3 外接 SSR 控制 | `connector=P3 Header 2`；`pin_1=+5V`；`pin_2=R22 10Ω to Q2 drain`；`switch=Q2 AO3400A`；`source=GND`；`control=Ctl` |
| 核心器件 | LED1 SK6812 | `device=LED1 SK6812`；`data_in=RGB/U4 GPIO2 pin6`；`vdd=+3.3V`；`ground=GND`；`decoupling=C22 100nF`；`data_out=LED1 pin1, no visible connection` |
| 射频 | E1 射频路径 | `controller_pin=U4 LAN_IN pin1`；`shunt_input=C12 2.7pF`；`series_inductor=L3 2.7nH`；`shunt_output=C13 2.4pF`；`connector=E1 ANT_IPEX` |
| 时钟 | U4 外部晶振 | `crystal=X1 TXC/8Z4000017`；`xtal_p=U4 pin30 -> L5 27nH -> X1.1`；`xtal_n=U4 pin29 -> X1.3`；`load_caps=C23 18pF,C24 18pF`；`ground_pins=X1.2,X1.4`；`frequency=原理图未明确标注` |
| 存储 | 外部存储 | `controller=U4 ESP32-C3FH4`；`external_flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示` |
| 总线 | Modbus 参数 | `physical_bus=RS-485`；`baud_candidate=115200`；`format_candidate=8N1`；`id_candidate=0x0004`；`schematic_protocol_parameters=未标注` |
| 接口 | 外接 SSR 与交流负载额定值 | `control_connector=P3`；`control_voltage_net=+5V`；`external_ssr_model=未标注`；`ac_load_path=未显示`；`voltage_candidate=AC 24-480V`；`current_candidate=10A` |

## 待确认事项

- `address.i2c-address-undetermined`：四页原理图均未打印 I2C 地址或硬件地址选择网络，因此无法仅由原理图确认产品正文中的 0x50 或地址可配置范围。（证据：图 6b599219293d / 第 1 页 / source_004 SCL/SDA 从 J2 到 U4，页面无地址文字或配置电阻）
- `bus.rs485-di-connection-undetermined`：source_003 中 U3 的 DI（4 脚）没有可见网络连接，而 TXD 只画到 R12/Q1 方向控制支路；无法从现有图确认 RS-485 发送数据如何进入 DI。（证据：图 c6405b791c31 / 第 1 页 / source_003 网格 B2，U3 DI/4 脚左侧无连线，TXD 位于独立 Q1 支路）
- `bus.modbus-parameters-undetermined`：原理图只确认 UART TXD/RXD 与 RS-485 收发器网络，没有标注波特率、数据格式、Modbus 设备 ID 或寄存器协议，无法由图纸确认正文中的 115200 8N1 与默认 ID 0x0004。（证据：图 c6405b791c31 / 第 1 页 / source_003 U3 RS-485 电路无协议参数; 图 6b599219293d / 第 1 页 / source_004 U4 TXD/RXD 与 P1/P2，无波特率或 ID 标注）
- `interface.external-ssr-ratings-undetermined`：控制板原理图只画出 P3 的 +5V/低侧控制端，没有画出外接固态继电器内部功率器件、交流负载端子或电气额定值，因此不能由图纸确认 AC 24-480V、10A 等参数。（证据：图 ef8998d30ae1 / 第 1 页 / source_001 仅显示 P3/Q2 控制回路，无交流功率触点或 SSR 型号）
- `review.i2c-address`：当前固件默认 I2C 地址是否为 0x50，可配置范围与保存方式是什么？；原因：I2C 地址属于固件行为，四页原理图没有地址文字或硬件地址选择网络。
- `review.rs485-di-path`：U3 DI（4 脚）实际连接哪个 ESP32-C3 UART 发送网络，source_003 是否漏画 TXD 到 DI 的连线？；原因：当前图中 TXD 只驱动 Q1 方向控制，而 U3 DI 无可见连接，RS-485 发送路径无法闭环。
- `review.modbus-parameters`：当前固件的 RS-485 波特率、帧格式、Modbus 默认 ID 和寄存器协议是什么？；原因：原理图只能确认物理层连接，不能证明 115200 8N1、0x0004 或寄存器定义。
- `review.external-ssr-ratings`：套件所配外接 SSR 的准确型号、控制输入范围、交流负载电压与额定电流是多少？；原因：控制板图只显示 P3 低侧驱动，没有外接 SSR 型号、内部电路或交流负载额定参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ef8998d30ae1302d50d1adc8f1a2ff29a8b815401f2ae78115803d091c26a505` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_01.png` |
| 2 | 1 | `043324c72c139c10e4bf364df191877d58be8c4483b4df1e17ebcfa11d50beec` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_02.png` |
| 3 | 1 | `c6405b791c311288649e85bcb9e35ef0d8b711339de5f82422cc0023486e58b9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_03.png` |
| 4 | 1 | `6b599219293decd42df297a3f2ad88ef20a8ad19d621ff7eec2b4247f35772c1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_04.png` |

---

源文档：`zh_CN/unit/acssr.md`

源文档 SHA-256：`63f17f22db1ba8f2d2d61c0d15d7f31e0adbc05677b51391fc17b2a9e0815682`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
