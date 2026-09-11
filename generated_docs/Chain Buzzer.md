# Chain Buzzer 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Buzzer |
| SKU | U224 |
| 产品 ID | `chain-buzzer-1fc7e7a7a6b2` |
| 源文档 | `zh_CN/chain/Chain_Buzzer.md` |

## 概述

Chain Buzzer 以 STM32G031G8U6 为核心，J1 与 J2 分别承载独立的 TXD1/RXD1 和 TXD2/RXD2 UART 信号，并共同接入 VCC_5V 与 GND。ME6206A33XG 将 VCC_5V 转换为 VCC_3V3，为 MCU、WS2812C-2020 RGB LED 和 SWD 接口供电。PA0 的 BEEP 信号经 SS8050 Y1 低边驱动 MLT-5020 蜂鸣器，支路带串联电阻、基极偏置和 1N4148WS 钳位二极管；PA8 则通过 RGB 网络驱动 LED 数据输入。NRST 带 10K/1uF 复位网络，J4 完整引出 3.3V、SWCLK、SWDIO、NRST 和 GND。

## 检索关键词

`Chain Buzzer`、`U224`、`STM32G031G8U6`、`STM32G031`、`GROVE_I/O`、`HY2.0-4P`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`VCC_5V`、`VCC_3V3`、`ME6206A33XG`、`SWD_5P`、`MCU_SWCLK`、`MCU_SWDIO`、`PF2-NRST`、`PA14-BOOT0`、`PA13`、`BEEP`、`PA0`、`PB6`、`PB7`、`MLT-5020`、`1N4148WS`、`RGB`、`PA8`、`WS2812C-2020`、`100nF`、`10uF`、`1uF`、`10K`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控 MCU | 图 82cda5fe4939 / 第 1 页 / B2 U1 |
| U2 | ME6206A33XG | 3.3V 稳压器 | 图 82cda5fe4939 / 第 1 页 / A2 U2 |
| J1 | GROVE_I/O | UART1 接口 | 图 82cda5fe4939 / 第 1 页 / A1 J1 |
| J2 | GROVE_I/O | UART2 接口 | 图 82cda5fe4939 / 第 1 页 / A1 J2 |
| J4 | SWD_5P | SWD 调试接口 | 图 82cda5fe4939 / 第 1 页 / B3 J4 |
| LS1 | MLT-5020 | 蜂鸣器 | 图 82cda5fe4939 / 第 1 页 / C2 LS1 |
| U3 | WS2812C-2020 | RGB LED | 图 82cda5fe4939 / 第 1 页 / C3 U3 |
| Q1 | SS8050 Y1 | 蜂鸣器开关晶体管 | 图 82cda5fe4939 / 第 1 页 / D2 Q1 |
| D1 | 1N4148WS | 跨接蜂鸣器两端节点的感性关断钳位二极管 | 图 82cda5fe4939 / 第 1 页 / C1-D2，D1 位于 LS1 左侧并跨接其上下节点 |
| R1 | 10R | VCC_5V 至蜂鸣器上端节点的串联供电电阻 | 图 82cda5fe4939 / 第 1 页 / C2，R1=10R 位于 VCC_5V 与 LS1 上端节点之间 |
| R3 | 1K | BEEP 至 Q1 基极的串联电阻 | 图 82cda5fe4939 / 第 1 页 / D1-D2，BEEP-R3-Q1 基极链路 |
| R4 | 10K | Q1 基极节点至 GND 的下拉电阻 | 图 82cda5fe4939 / 第 1 页 / D2，R4=10K 跨接 Q1 基极节点与 GND |
| R2/C1 | 10K / 1uF | NRST 上拉与对地电容组成的复位网络 | 图 82cda5fe4939 / 第 1 页 / B1-B2，VCC_3V3-R2-NRST-C1-GND |
| C2/C3 | 100nF / 10uF | U1 VDD/VDDA 的并联电源去耦 | 图 82cda5fe4939 / 第 1 页 / B2，U1 左上方 C2=100nF、C3=10uF 跨接 VCC_3V3 与 GND |
| C5/C6 | 10uF / 100nF | U2 VIN 侧的 VCC_5V 输入去耦 | 图 82cda5fe4939 / 第 1 页 / A2，U2 VIN 左侧 C5=10uF、C6=100nF |
| C7/C8 | 100nF / 10uF | U2 VOUT 侧的 VCC_3V3 输出去耦 | 图 82cda5fe4939 / 第 1 页 / A2，U2 VOUT 右侧 C7=100nF、C8=10uF |
| C12 | 100nF | U3 VDD 的本地电源去耦 | 图 82cda5fe4939 / 第 1 页 / C2-C3，U3 左侧 C12=100nF 跨接 VCC_3V3 与 GND |

## 系统结构

### Chain Buzzer

单页原理图由两组 UART/Grove 接口、5V 转 3.3V 电源、STM32G031G8U6 主控、SWD/复位、晶体管驱动蜂鸣器和单颗可编程 RGB LED 六个主要功能块组成。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`uart_connectors=J1,J2`；`regulator=U2 ME6206A33XG`；`debug_connector=J4 SWD_5P`；`buzzer=LS1 MLT-5020`；`rgb_led=U3 WS2812C-2020`
- 证据：图 82cda5fe4939 / 第 1 页 / 整页网格 A1-D3，J1/J2、U2、U1/J4、LS1/Q1 与 U3 功能块

## 核心器件

### U1

U1 的器件标注为 STM32G031G8U6，原理图符号为 28 引脚。

- 参数与网络：`reference=U1`；`part_number=STM32G031G8U6`；`pin_count_shown=28`
- 证据：图 82cda5fe4939 / 第 1 页 / B2，U1 符号底部型号与两侧 pin 1-28

### U3

U3 WS2812C-2020 的 VDD pin 4 接 VCC_3V3、DI pin 3 接 RGB、GND pin 2 接地，DO pin 1 未接到其他网络。

- 参数与网络：`part_number=WS2812C-2020`；`vdd_pin=pin 4 / VCC_3V3`；`di_pin=pin 3 / RGB`；`gnd_pin=pin 2 / GND`；`do_pin=pin 1 / no external net shown`
- 证据：图 82cda5fe4939 / 第 1 页 / C3，U3 pins 1-4 与 DO/GND/DI/VDD 网络

## 电源

### U2

U2 ME6206A33XG 的 VIN pin 3 接 VCC_5V、VOUT pin 2 输出 VCC_3V3、GND pin 1 接地。

- 参数与网络：`part_number=ME6206A33XG`；`vin_pin=3`；`input=VCC_5V`；`vout_pin=2`；`output=VCC_3V3`；`gnd_pin=1`
- 证据：图 82cda5fe4939 / 第 1 页 / A2，U2 VIN pin 3、VOUT pin 2、GND pin 1 与两侧电源轨

### U1

U1 VDD/VDDA pin 3 接 VCC_3V3，VSS/VSSA pin 4 接 GND。

- 参数与网络：`supply_pin=VDD/VDDA pin 3`；`supply_net=VCC_3V3`；`ground_pin=VSS/VSSA pin 4`；`ground_net=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / B2，U1 左侧 pins 3-4 与 VCC_3V3/GND

### VCC_5V

VCC_5V 同时连接 J1/J2 的 VCC、U2 VIN 输入去耦节点，并通过 R1=10R 向蜂鸣器支路供电。

- 参数与网络：`connector_loads=J1 VCC,J2 VCC`；`regulator_load=U2 VIN pin 3`；`buzzer_path=VCC_5V-R1-LS1`
- 证据：图 82cda5fe4939 / 第 1 页 / A1-A2 与 C2，VCC_5V 网络在 J1/J2、U2 和 R1 处的标注

### VCC_3V3

VCC_3V3 为 U1 VDD/VDDA、U3 VDD、J4 pin 1 和 NRST 上拉电阻 R2 供电。

- 参数与网络：`mcu=U1 VDD/VDDA pin 3`；`rgb_led=U3 VDD pin 4`；`debug=J4 pin 1`；`reset_pullup=R2 10K`
- 证据：图 82cda5fe4939 / 第 1 页 / A2-C3，VCC_3V3 在 U2 输出、U1、R2、J4 与 U3 处的标注

## 接口

### J1

J1 GROVE_I/O 的 IO2 接 TXD1、IO1 接 RXD1、VCC 接 VCC_5V、GND 接 GND。

- 参数与网络：`connector=J1 GROVE_I/O`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / A1，J1 右侧 IO2/IO1/VCC/GND 四行网络

### J2

J2 GROVE_I/O 的 IO2 接 RXD2、IO1 接 TXD2、VCC 接 VCC_5V、GND 接 GND。

- 参数与网络：`connector=J2 GROVE_I/O`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / A1，J2 右侧 IO2/IO1/VCC/GND 四行网络

## 总线

### UART1

U1 的 PB6 pin 26 连接 TXD1，PB7 pin 27 连接 RXD1，两条网络均到达 J1。

- 参数与网络：`tx_pin=PB6 pin 26`；`tx_net=TXD1`；`rx_pin=PB7 pin 27`；`rx_net=RXD1`；`connector=J1`
- 证据：图 82cda5fe4939 / 第 1 页 / A1-B2，J1 TXD1/RXD1 与 U1 PB6 pin 26、PB7 pin 27

### UART2

U1 的 PA2 pin 8 连接 TXD2，PA3 pin 9 连接 RXD2，两条网络均到达 J2。

- 参数与网络：`tx_pin=PA2 pin 8`；`tx_net=TXD2`；`rx_pin=PA3 pin 9`；`rx_net=RXD2`；`connector=J2`
- 证据：图 82cda5fe4939 / 第 1 页 / A1-B2，J2 TXD2/RXD2 与 U1 PA2 pin 8、PA3 pin 9

### U1 SDA/SCL

U1 PA12[PA10] pin 19 标注 SDA、PA11[PA9] pin 18 标注 SCL，但两条短线均在图中以未连接标记终止，未连接到外部器件或接口。

- 参数与网络：`sda=PA12[PA10] pin 19`；`scl=PA11[PA9] pin 18`；`drawing_state=terminated with no-connect markers`
- 证据：图 82cda5fe4939 / 第 1 页 / B2，U1 pins 19/18 的 SDA/SCL 短线及红色未连接标记

## GPIO 与控制信号

### U3

U1 PA8 pin 16 连接 RGB 网络并驱动 U3 WS2812C-2020 的 DI pin 3。

- 参数与网络：`gpio=PA8 pin 16`；`net=RGB`；`device_pin=U3 DI pin 3`
- 证据：图 82cda5fe4939 / 第 1 页 / B2-C3，U1 PA8 pin 16、RGB 网络与 U3 DI pin 3

### Q1 base

BEEP 经 R3=1K 串联到 Q1 基极，R4=10K 从该基极节点下拉到 GND。

- 参数与网络：`control_net=BEEP`；`series_resistor=R3 1K`；`pulldown_resistor=R4 10K`；`transistor=Q1 SS8050 Y1`
- 证据：图 82cda5fe4939 / 第 1 页 / D1-D2，BEEP、R3、R4 与 Q1 基极节点

## 时钟

### U1 PC14/PC15

U1 PC14-OSC32IN pin 1 与 PC15-OSC32OUT pin 2 在该页未连接外部晶体或其他时钟器件。

- 参数与网络：`osc_in=PC14-OSC32IN pin 1`；`osc_out=PC15-OSC32OUT pin 2`；`external_clock_device=null`
- 证据：图 82cda5fe4939 / 第 1 页 / B2，U1 左上 pins 1-2 无外接连线

## 复位

### NRST

U1 PF2-NRST pin 5 接 NRST；该网络由 R2=10K 上拉至 VCC_3V3，并由 C1=1uF 接 GND。

- 参数与网络：`mcu_pin=PF2-NRST pin 5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`
- 证据：图 82cda5fe4939 / 第 1 页 / B1-B2，U1 PF2-NRST pin 5 与 VCC_3V3-R2-NRST-C1-GND 网络

## 保护电路

### U1 VCC_3V3

C2=100nF 与 C3=10uF 并联在 U1 的 VCC_3V3 供电节点和 GND 之间。

- 参数与网络：`capacitor_1=C2 100nF`；`capacitor_2=C3 10uF`；`rail=VCC_3V3`；`return=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / B2，U1 左上方 C2/C3 并联去耦支路

### U2 VIN

U2 输入侧 C6=100nF 与 C5=10uF 并联在 VCC_5V 和 GND 之间。

- 参数与网络：`rail=VCC_5V`；`capacitor_1=C6 100nF`；`capacitor_2=C5 10uF`；`return=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / A2，U2 VIN 左侧 C6/C5 至公共 GND

### U2 VOUT

U2 输出侧 C7=100nF 与 C8=10uF 并联在 VCC_3V3 和 GND 之间。

- 参数与网络：`rail=VCC_3V3`；`capacitor_1=C7 100nF`；`capacitor_2=C8 10uF`；`return=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / A2，U2 VOUT 右侧 C7/C8 至公共 GND

### D1

D1 1N4148WS 与 LS1 跨接在 R1 后供电节点和 Q1 集电极节点之间，为蜂鸣器感性关断提供钳位路径。

- 参数与网络：`diode=D1 1N4148WS`；`upper_node=R1 output / LS1 upper node`；`lower_node=LS1 lower node / Q1 collector`；`protected_load=LS1 MLT-5020`
- 证据：图 82cda5fe4939 / 第 1 页 / C1-D2，D1 跨接 LS1 上下两个节点

### U3 VDD

C12=100nF 跨接在 U3 的 VCC_3V3 供电节点与 GND 之间。

- 参数与网络：`capacitor=C12 100nF`；`rail=VCC_3V3`；`device_pin=U3 VDD pin 4`；`return=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / C2-C3，U3 左侧 C12=100nF 去耦支路

## 关键网络

### J1/J2

J1 与 J2 的 VCC 引脚均接 VCC_5V，GND 引脚均接公共 GND；两接口的 UART 信号网络彼此分为 TXD1/RXD1 与 TXD2/RXD2。

- 参数与网络：`supply=VCC_5V`；`ground=GND`；`j1_signals=TXD1,RXD1`；`j2_signals=TXD2,RXD2`
- 证据：图 82cda5fe4939 / 第 1 页 / A1，J1 与 J2 的四线网络标注

## 音频

### LS1

U1 PA0 pin 6 输出 BEEP，经 R3=1K 到 Q1 SS8050 Y1 基极，Q1 以低边方式控制 LS1 MLT-5020。

- 参数与网络：`gpio=PA0 pin 6`；`net=BEEP`；`r3=1K`；`transistor=Q1 SS8050 Y1`；`load=LS1 MLT-5020`
- 证据：图 82cda5fe4939 / 第 1 页 / B2-D2，U1 PA0 pin 6 的 BEEP 网络至 R3、Q1 和 LS1

### Q1/LS1

Q1 SS8050 Y1 的集电极接 LS1 下端节点，发射极接 GND，形成蜂鸣器低边开关。

- 参数与网络：`transistor=Q1 SS8050 Y1`；`collector=LS1 lower node`；`emitter=GND`；`load=LS1 MLT-5020`
- 证据：图 82cda5fe4939 / 第 1 页 / C2-D2，LS1 下端、Q1 集电极和 Q1 发射极至 GND

### LS1

蜂鸣器供电路径为 VCC_5V 经 R1=10R 到 LS1 MLT-5020 上端，LS1 下端由 Q1 开关至 GND。

- 参数与网络：`supply=VCC_5V`；`series_resistor=R1 10R`；`buzzer=LS1 MLT-5020`；`switch=Q1 SS8050 Y1`；`return=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / C2-D2，VCC_5V-R1-LS1-Q1-GND 完整纵向支路

## 调试与烧录

### J4

J4 SWD_5P 的 pin 1 至 pin 5 依次连接 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 82cda5fe4939 / 第 1 页 / B3，J4 SWD_5P pins 1-5 的网络标注

### U1

U1 PA14-BOOT0 pin 21 连接 MCU_SWCLK，PA13 pin 20 连接 MCU_SWDIO。

- 参数与网络：`swclk=PA14-BOOT0 pin 21 / MCU_SWCLK`；`swdio=PA13 pin 20 / MCU_SWDIO`；`connector=J4`
- 证据：图 82cda5fe4939 / 第 1 页 / B2-B3，U1 pins 21/20 至 J4 MCU_SWCLK/MCU_SWDIO

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 电源 | U2 | `part_number=ME6206A33XG`；`vin_pin=3`；`input=VCC_5V`；`vout_pin=2`；`output=VCC_3V3`；`gnd_pin=1` |
| 总线 | UART1 | `tx_pin=PB6 pin 26`；`tx_net=TXD1`；`rx_pin=PB7 pin 27`；`rx_net=RXD1`；`connector=J1` |
| 总线 | UART2 | `tx_pin=PA2 pin 8`；`tx_net=TXD2`；`rx_pin=PA3 pin 9`；`rx_net=RXD2`；`connector=J2` |
| 音频 | LS1 | `gpio=PA0 pin 6`；`net=BEEP`；`r3=1K`；`transistor=Q1 SS8050 Y1`；`load=LS1 MLT-5020` |
| GPIO 与控制信号 | U3 | `gpio=PA8 pin 16`；`net=RGB`；`device_pin=U3 DI pin 3` |
| 调试与烧录 | J4 | `pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND` |
| 复位 | NRST | `mcu_pin=PF2-NRST pin 5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND` |
| 系统结构 | Chain Buzzer | `mcu=U1 STM32G031G8U6`；`uart_connectors=J1,J2`；`regulator=U2 ME6206A33XG`；`debug_connector=J4 SWD_5P`；`buzzer=LS1 MLT-5020`；`rgb_led=U3 WS2812C-2020` |
| 核心器件 | U1 | `reference=U1`；`part_number=STM32G031G8U6`；`pin_count_shown=28` |
| 电源 | U1 | `supply_pin=VDD/VDDA pin 3`；`supply_net=VCC_3V3`；`ground_pin=VSS/VSSA pin 4`；`ground_net=GND` |
| 保护电路 | U1 VCC_3V3 | `capacitor_1=C2 100nF`；`capacitor_2=C3 10uF`；`rail=VCC_3V3`；`return=GND` |
| 接口 | J1 | `connector=J1 GROVE_I/O`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND` |
| 接口 | J2 | `connector=J2 GROVE_I/O`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND` |
| 关键网络 | J1/J2 | `supply=VCC_5V`；`ground=GND`；`j1_signals=TXD1,RXD1`；`j2_signals=TXD2,RXD2` |
| 保护电路 | U2 VIN | `rail=VCC_5V`；`capacitor_1=C6 100nF`；`capacitor_2=C5 10uF`；`return=GND` |
| 保护电路 | U2 VOUT | `rail=VCC_3V3`；`capacitor_1=C7 100nF`；`capacitor_2=C8 10uF`；`return=GND` |
| 电源 | VCC_5V | `connector_loads=J1 VCC,J2 VCC`；`regulator_load=U2 VIN pin 3`；`buzzer_path=VCC_5V-R1-LS1` |
| 电源 | VCC_3V3 | `mcu=U1 VDD/VDDA pin 3`；`rgb_led=U3 VDD pin 4`；`debug=J4 pin 1`；`reset_pullup=R2 10K` |
| 调试与烧录 | U1 | `swclk=PA14-BOOT0 pin 21 / MCU_SWCLK`；`swdio=PA13 pin 20 / MCU_SWDIO`；`connector=J4` |
| GPIO 与控制信号 | Q1 base | `control_net=BEEP`；`series_resistor=R3 1K`；`pulldown_resistor=R4 10K`；`transistor=Q1 SS8050 Y1` |
| 音频 | Q1/LS1 | `transistor=Q1 SS8050 Y1`；`collector=LS1 lower node`；`emitter=GND`；`load=LS1 MLT-5020` |
| 音频 | LS1 | `supply=VCC_5V`；`series_resistor=R1 10R`；`buzzer=LS1 MLT-5020`；`switch=Q1 SS8050 Y1`；`return=GND` |
| 保护电路 | D1 | `diode=D1 1N4148WS`；`upper_node=R1 output / LS1 upper node`；`lower_node=LS1 lower node / Q1 collector`；`protected_load=LS1 MLT-5020` |
| 核心器件 | U3 | `part_number=WS2812C-2020`；`vdd_pin=pin 4 / VCC_3V3`；`di_pin=pin 3 / RGB`；`gnd_pin=pin 2 / GND`；`do_pin=pin 1 / no external net shown` |
| 保护电路 | U3 VDD | `capacitor=C12 100nF`；`rail=VCC_3V3`；`device_pin=U3 VDD pin 4`；`return=GND` |
| 总线 | U1 SDA/SCL | `sda=PA12[PA10] pin 19`；`scl=PA11[PA9] pin 18`；`drawing_state=terminated with no-connect markers` |
| 时钟 | U1 PC14/PC15 | `osc_in=PC14-OSC32IN pin 1`；`osc_out=PC15-OSC32OUT pin 2`；`external_clock_device=null` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `82cda5fe4939f456e5b95edd536a334689d264ee052b5cdee34f743dcd814db9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1260/ChainBuzzer_SCH_V02_20250829_2025_08_29_16_56_12_2.png` |

---

源文档：`zh_CN/chain/Chain_Buzzer.md`

源文档 SHA-256：`aa758a84b50839a2e858fbd25bc386c2db49b66ea2445d582aa1a8423d60d754`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
