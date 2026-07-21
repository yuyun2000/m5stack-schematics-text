# Atom PoE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom PoE |
| SKU | K052 |
| 产品 ID | `atom-poe-2ad697f37267` |
| 源文档 | `zh_CN/atom/atom_poe.md` |

## 概述

Atom PoE 原理图以 U1 W5500 为以太网控制器，通过 GPIO22、GPIO19、GPIO23、GPIO33 与 ATOM 插座形成 SCLK、SCSn、MISO、MOSI 四线 SPI，并使用 25MHz 晶振。W5500 的 TX/RX 差分线经过 TVS1/TVS2、R5 0Ω 阵列、发送/接收端接网络和 T1 Net Trans 后连接 RJ45。T1 中心抽头 VA1/VA2 与 RJ45 空闲对 VB1/VB2 进入 P1 5V PoE 模块，VOUT 经 D1 SS54 形成 INF+ 并送到 ATOM 5V；A3V3/D3V3 与 AGND/GND 分别通过 120Ω/MB 器件连接。

## 检索关键词

`Atom PoE`、`K052`、`W5500`、`SPI`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO33`、`SCLK`、`SCSn`、`MISO`、`MOSI`、`25MHz`、`TX_P`、`TX_N`、`RX_P`、`RX_N`、`T1 Net Trans`、`RJ45`、`VA1`、`VA2`、`VB1`、`VB2`、`P1 5V`、`INF+`、`A3V3`、`D3V3`、`AGND`、`GND`、`ACTLED`、`LINKLED`、`PMODE0`、`PMODE1`、`PMODE2`、`ESD3.3V52D-C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | W5500 | SPI 以太网控制器，连接 ATOM、25MHz 时钟、PHY 差分线和状态指示 | 图 4c5ce75fd7c2 / 第 1 页 / 页面左中黄色 U1 W5500，48 脚方框及 TX/RX、SPI、时钟、电源和 LED 引脚 |
| R4 | 4.7KΩ resistor array | 将 W5500 PMODE0/PMODE1/PMODE2 与 RSTn 上拉到 D3V3 | 图 4c5ce75fd7c2 / 第 1 页 / U1 上方 R4 4.7KΩ 四联电阻阵列，顶部接 D3V3，底部接 PMODE0/1/2 与 RSTn |
| 25MHz crystal network | 25MHZ 12PF 10PPM | 为 W5500 XI/CLKIN 与 XO 提供 25MHz 时钟 | 图 4c5ce75fd7c2 / 第 1 页 / U1 右下 XI/XO 网络：25MHZ 12PF 10PPM 晶振、R17 1MΩ、R19 0Ω、C10/C11 12pF |
| TVS1/TVS2 | ESD3.3V52D-C | W5500 TX/RX 差分线的双路 ESD 防护 | 图 4c5ce75fd7c2 / 第 1 页 / 页面中上 TX_P/TX_N 旁 TVS1、RX_P/RX_N 旁 TVS2，均标注 ESD3.3V52D-C |
| R5 | 4-channel 0R array | 串联在四条 W5500 PHY 差分线与变压器端接网络之间 | 图 4c5ce75fd7c2 / 第 1 页 / TVS1/TVS2 右侧 R5 四联阵列，底部标注 0R |
| T1 | Net Trans | 隔离 W5500 PHY 差分线与 RJ45，并引出 VA1/VA2 中心抽头供 PoE 模块 | 图 4c5ce75fd7c2 / 第 1 页 / 页面右上 T1 Net Trans，TD+/CT/TD-、RD+/CT/RD- 与 TX+/CT/TX-、RX+/CT/RX- |
| RJ45 | 未标注 | 以太网连接器，引出 TX/RX 数据对、VB1/VB2 空闲对和屏蔽端 | 图 4c5ce75fd7c2 / 第 1 页 / 页面最右 RJ45 1-9 脚，TX1_P/TX1_N/RX1_P/RX1_N、VB1、VB2 |
| P1 | 5V | 接收 VA1/VA2/VB1/VB2 的 PoE 电源模块，输出 VOUT 与 GND | 图 4c5ce75fd7c2 / 第 1 页 / 页面右中 P1 方框，输入 VA1/VA2/VB1/VB2，输出 GND/VOUT，方框下标注 5V |
| D1 | SS54 | 串联在 P1 VOUT 与 INF+ 之间的电源二极管 | 图 4c5ce75fd7c2 / 第 1 页 / P1 左侧 VOUT-D1 SS54-INF+ 串联路径 |
| R15/R18 | 120Ω/MB | 分别连接 A3V3-D3V3 和 AGND-GND 的电源域桥接器件 | 图 4c5ce75fd7c2 / 第 1 页 / 页面中央 R15 120Ω/MB 位于 A3V3-D3V3，R18 120Ω/MB 位于 AGND-GND |
| ACT/LINK LEDs | LED2 GREEN / LED_ORANGE | 由 W5500 ACTLED 与 LINKLED 引脚驱动的活动和链路状态指示 | 图 4c5ce75fd7c2 / 第 1 页 / U1 右侧 ACTLED 27 脚到绿色 LED/R20 100R，LINKLED 25 脚到橙色 LED/R21 100R |
| ATOM | 未标注 | 连接 D3V3、INF+、GND、W5500 SPI 与 G21/G25 扩展信号的九针 Atom 插座 | 图 4c5ce75fd7c2 / 第 1 页 / 页面右下蓝色 ATOM 1-9 脚方框，标注 GND/5V/G25/G21 与 G33/G23/G19/G22/3V3 |
| I2C | 未标注 | 引出 G21、G25 和 GND 的四针扩展连接器，其中 2 脚未连接 | 图 4c5ce75fd7c2 / 第 1 页 / ATOM 左侧黄色 I2C 4-1 脚方框；4 接 G21，3 接 G25，2 为短线无网络，1 接 GND |

## 系统结构

### 以太网与 PoE 总体链路

ATOM 通过 SPI 控制 W5500；W5500 PHY 差分线经过 ESD、0Ω 阵列和 T1 隔离后到 RJ45，同时 T1 中心抽头与 RJ45 空闲对把 PoE 输入送入 P1 5V 模块，P1 输出经 D1 接回 ATOM 5V。

- 参数与网络：`controller=ATOM`；`ethernet_ic=U1 W5500`；`magnetics=T1 Net Trans`；`connector=RJ45`；`poe_module=P1 5V`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 整页原理图：左侧 W5500、中上 PHY/T1/RJ45、右中 P1、右下 ATOM

## 核心器件

### P1 具体型号可见性

P1 在当前页面只标注输入/输出引脚和 5V，没有显示制造商、具体料号、输入范围或功率额定值。

- 参数与网络：`reference=P1`；`visible_marking=5V`；`manufacturer_shown=false`；`part_number_shown=false`；`ratings_shown=false`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面右中 P1 方框，仅见 VA1/VA2/VB1/VB2/GND/VOUT 和下方 5V

## 电源

### A3V3/D3V3 与地分区

R15 标注 120Ω/MB 并连接 A3V3 与 D3V3；R18 标注 120Ω/MB 并连接 AGND 与 GND。

- 参数与网络：`supply_bridge=R15 120Ω/MB: A3V3 to D3V3`；`ground_bridge=R18 120Ω/MB: AGND to GND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面中央 R15 A3V3-D3V3 与 R18 AGND-GND

### W5500 电源去耦

A3V3 侧 C14-C19 各 100nF 接 AGND，并有 C13 4.7uF 与 C12 10nF；D3V3 侧 C20 100nF 与 C21 10uF 接 GND。

- 参数与网络：`analog_decoupling=C14-C19 100nF; C13 4.7uF; C12 10nF`；`digital_decoupling=C20 100nF; C21 10uF`；`analog_rail=A3V3/AGND`；`digital_rail=D3V3/GND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面下方 C14-C21 去耦排，以及 U1 下侧 C12/C13

### PoE 取电输入

T1 发送侧中心抽头 15 脚标为 VA1，接收侧中心抽头 10 脚标为 VA2；RJ45 4/5 脚并为 VB1，7/8 脚并为 VB2，VA1/VA2/VB1/VB2 均进入 P1。

- 参数与网络：`va1=T1 CT pin 15`；`va2=T1 CT pin 10`；`vb1=RJ45 pins 4 and 5`；`vb2=RJ45 pins 7 and 8`；`destination=P1`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / T1 CT 15/10 的 VA1/VA2、RJ45 4/5 与 7/8 的 VB1/VB2，以及 P1 四路输入

### P1 5V 输出

P1 方框标注 5V，GND 输出接板级 GND，VOUT 经 D1 SS54 形成 INF+；INF+ 连接 ATOM 的 5V 3 脚。

- 参数与网络：`module=P1 5V`；`ground_output=GND`；`power_output=VOUT -> D1 SS54 -> INF+`；`atom_destination=ATOM pin 3 5V`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面右中 P1 GND/VOUT-D1-INF+ 与右下 ATOM 5V 3 脚

## 接口

### T1 到 RJ45 数据对映射

T1 TX+ 16 脚经 TX1_P 接 RJ45 1 脚，TX- 14 脚经 TX1_N 接 2 脚，RX+ 11 脚经 RX1_P 接 3 脚，RX- 9 脚经 RX1_N 接 6 脚。

- 参数与网络：`rj45_pin1=TX1_P from T1 TX+ pin 16`；`rj45_pin2=TX1_N from T1 TX- pin 14`；`rj45_pin3=RX1_P from T1 RX+ pin 11`；`rj45_pin6=RX1_N from T1 RX- pin 9`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / T1 右侧 TX+/TX-/RX+/RX- 到 RJ45 1/2/3/6

### ATOM 九针连接

ATOM 1/3/5/7 脚分别为 GND、5V、G25、G21，2/4/6/8/9 脚分别为 G33、G23、G19、G22、3V3；5V 接 INF+，3V3 接 D3V3。

- 参数与网络：`odd_pins=1 GND; 3 5V/INF+; 5 G25; 7 G21`；`even_and_power=2 G33; 4 G23; 6 G19; 8 G22; 9 3V3/D3V3`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面右下蓝色 ATOM 方框及 1-9 脚网络

### I2C 四针接口

I2C 方框的 4 脚接 ATOM G21，3 脚接 G25，2 脚在当前页面未连接，1 脚接 GND。

- 参数与网络：`pin4=G21`；`pin3=G25`；`pin2=not connected`；`pin1=GND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / ATOM 左侧黄色 I2C 4-1 脚方框与四条引线

## 总线

### W5500 SPI 映射

U1 W5500 的 SCLK 33 脚接 GPIO22，SCSn 32 脚接 GPIO19，MISO 34 脚接 GPIO23，MOSI 35 脚接 GPIO33；四个 GPIO 分别连接 ATOM 的 G22、G19、G23、G33。

- 参数与网络：`sclk=U1 pin 33 -> GPIO22 -> ATOM G22 pin 8`；`chip_select=U1 pin 32 SCSn -> GPIO19 -> ATOM G19 pin 6`；`miso=U1 pin 34 -> GPIO23 -> ATOM G23 pin 4`；`mosi=U1 pin 35 -> GPIO33 -> ATOM G33 pin 2`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 右侧 MOSI/MISO/SCLK/SCSn 到 GPIO33/23/22/19，以及 ATOM 右侧对应 GPIO

### W5500 PHY 差分对

U1 TXN 1 脚和 TXP 2 脚连接 TX_N/TX_P，RXN 5 脚和 RXP 6 脚连接 RX_N/RX_P，四条网络进入 TVS1/TVS2 与 R5 0Ω 阵列。

- 参数与网络：`transmit=TXN pin 1 -> TX_N; TXP pin 2 -> TX_P`；`receive=RXN pin 5 -> RX_N; RXP pin 6 -> RX_P`；`protection=TVS1/TVS2`；`series_array=R5 0R`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 左上 TXN/TXP/RXN/RXP 网络与页面中上 TVS1/TVS2、R5

## GPIO 与控制信号

### W5500 中断引脚

U1 INTn 36 脚在当前页面只有短引线，没有连接到命名网络或 ATOM 引脚。

- 参数与网络：`pin=36`；`signal=INTn`；`connected=false`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 右上 INTn 36 脚短线，未见网络名或后续连接

### W5500 模式配置

U1 PMODE0 44 脚、PMODE1 43 脚、PMODE2 42 脚分别通过 R4 的三路 4.7KΩ 电阻上拉到 D3V3。

- 参数与网络：`pmode0=pin 44 pull-up 4.7KΩ`；`pmode1=pin 43 pull-up 4.7KΩ`；`pmode2=pin 42 pull-up 4.7KΩ`；`rail=D3V3`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 上方 PMODE0/1/2 42-44 脚到 R4 三路上拉

### 以太网状态指示

U1 ACTLED 27 脚连接绿色 LED，LED 另一端经 R20 100R 接 D3V3；U1 LINKLED 25 脚连接橙色 LED，另一端经 R21 100R 接 D3V3；DUPLED 26 脚和 SPDLED 24 脚标为未连接。

- 参数与网络：`activity=ACTLED pin 27 -> green LED -> R20 100R -> D3V3`；`link=LINKLED pin 25 -> orange LED -> R21 100R -> D3V3`；`duplex_connected=false`；`speed_connected=false`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 右侧 ACTLED/DUPLED/LINKLED 与下方 SPDLED，以及绿色/橙色 LED、R20/R21

## 时钟

### W5500 25MHz 时钟

U1 XI/CLKIN 30 脚和 XO 31 脚连接标注 25MHZ 12PF 10PPM 的晶振网络，R17 1MΩ 跨接 XI/XO，R19 0Ω 串在 XO 侧，C10/C11 各 12pF 接 AGND。

- 参数与网络：`frequency_mhz=25`；`pins=XI/CLKIN pin 30; XO pin 31`；`feedback_resistor=R17 1MΩ`；`series_resistor=R19 0Ω`；`load_capacitors=C10/C11 12pF`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 右下 XI/XO 与 25MHZ 12PF 10PPM、R17/R19、C10/C11

## 复位

### W5500 复位上拉

U1 RSTn 37 脚通过 R4 四联 4.7KΩ 电阻阵列的一路上拉到 D3V3，当前页面没有显示外部复位驱动。

- 参数与网络：`pin=37`；`signal=RSTn`；`pullup=R4 4.7KΩ to D3V3`；`external_driver_shown=false`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 RSTn 37 脚向上连接 R4 第四路，R4 顶部公共接 D3V3

## 保护电路

### PHY 差分线 ESD 防护

TVS1 跨接 TX_P/TX_N，TVS2 跨接 RX_P/RX_N，二者均在图中标注 ESD3.3V52D-C。

- 参数与网络：`transmit_tvs=TVS1 on TX_P/TX_N`；`receive_tvs=TVS2 on RX_P/RX_N`；`visible_part_number=ESD3.3V52D-C`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / 页面中上 TVS1 位于 TX 对，TVS2 位于 RX 对

## 模拟电路

### W5500 外部电阻

U1 EXRES1 10 脚通过 R16 12.4KΩ 连接 AGND。

- 参数与网络：`pin=10`；`signal=EXRES1`；`resistor=R16 12.4KΩ`；`reference=AGND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / U1 左下 EXRES1 10 脚经 R16 12.4KΩ 接 AGND

### 发送侧端接

R5 后的发送差分线形成 TX2_P/TX2_N 并连接 T1 的 TD+ 1 脚与 TD- 3 脚；R1/R2 各 49.9R 1% 从 A3V3 接两条发送线，T1 CT 2 脚通过 R3 10R 1% 接 A3V3，并通过 C1 223 接 AGND。

- 参数与网络：`transformer_pins=TD+ pin 1; CT pin 2; TD- pin 3`；`pair_resistors=R1/R2 49.9R 1%`；`center_tap_resistor=R3 10R 1%`；`center_tap_capacitor=C1 223 to AGND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / T1 左上 TD+/CT/TD- 与 R1/R2/R3、C1 网络

### 接收侧端接

R5 后的 RX3_P/RX3_N 经标注 682 的串联电容形成 RX2_P/RX2_N，连接 T1 RD+ 6 脚与 RD- 8 脚；R6/R7 各 82R 1% 连接接收线与 CT 7 脚，CT 通过 C3 103 接 AGND。

- 参数与网络：`transformer_pins=RD+ pin 6; CT pin 7; RD- pin 8`；`series_capacitors=C2/C4 visible value 682`；`termination_resistors=R6/R7 82R 1%`；`center_tap_capacitor=C3 103 to AGND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / T1 左下 RD+/CT/RD- 与 RX3/RX2、C2/C4、R6/R7、C3 网络

### RJ45 共模泄放网络

VA1、VA2、VB1、VB2 分别经 C5/C6/C7/C8 223 100V 与 R9/R10/R12/R13 75R 串联到公共节点，公共节点再经 C9 102 2kV 接 GND。

- 参数与网络：`va1_branch=C5 223 100V + R9 75R`；`va2_branch=C6 223 100V + R10 75R`；`vb1_branch=C7 223 100V + R12 75R`；`vb2_branch=C8 223 100V + R13 75R`；`common_capacitor=C9 102 2kV to GND`
- 证据：图 4c5ce75fd7c2 / 第 1 页 / RJ45 下方 VA1/VA2/VB1/VB2 的 C5-C8、R9/R10/R12/R13 与公共 C9

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 以太网与 PoE 总体链路 | `controller=ATOM`；`ethernet_ic=U1 W5500`；`magnetics=T1 Net Trans`；`connector=RJ45`；`poe_module=P1 5V` |
| 总线 | W5500 SPI 映射 | `sclk=U1 pin 33 -> GPIO22 -> ATOM G22 pin 8`；`chip_select=U1 pin 32 SCSn -> GPIO19 -> ATOM G19 pin 6`；`miso=U1 pin 34 -> GPIO23 -> ATOM G23 pin 4`；`mosi=U1 pin 35 -> GPIO33 -> ATOM G33 pin 2` |
| GPIO 与控制信号 | W5500 中断引脚 | `pin=36`；`signal=INTn`；`connected=false` |
| 复位 | W5500 复位上拉 | `pin=37`；`signal=RSTn`；`pullup=R4 4.7KΩ to D3V3`；`external_driver_shown=false` |
| GPIO 与控制信号 | W5500 模式配置 | `pmode0=pin 44 pull-up 4.7KΩ`；`pmode1=pin 43 pull-up 4.7KΩ`；`pmode2=pin 42 pull-up 4.7KΩ`；`rail=D3V3` |
| 模拟电路 | W5500 外部电阻 | `pin=10`；`signal=EXRES1`；`resistor=R16 12.4KΩ`；`reference=AGND` |
| 时钟 | W5500 25MHz 时钟 | `frequency_mhz=25`；`pins=XI/CLKIN pin 30; XO pin 31`；`feedback_resistor=R17 1MΩ`；`series_resistor=R19 0Ω`；`load_capacitors=C10/C11 12pF` |
| GPIO 与控制信号 | 以太网状态指示 | `activity=ACTLED pin 27 -> green LED -> R20 100R -> D3V3`；`link=LINKLED pin 25 -> orange LED -> R21 100R -> D3V3`；`duplex_connected=false`；`speed_connected=false` |
| 电源 | A3V3/D3V3 与地分区 | `supply_bridge=R15 120Ω/MB: A3V3 to D3V3`；`ground_bridge=R18 120Ω/MB: AGND to GND` |
| 电源 | W5500 电源去耦 | `analog_decoupling=C14-C19 100nF; C13 4.7uF; C12 10nF`；`digital_decoupling=C20 100nF; C21 10uF`；`analog_rail=A3V3/AGND`；`digital_rail=D3V3/GND` |
| 总线 | W5500 PHY 差分对 | `transmit=TXN pin 1 -> TX_N; TXP pin 2 -> TX_P`；`receive=RXN pin 5 -> RX_N; RXP pin 6 -> RX_P`；`protection=TVS1/TVS2`；`series_array=R5 0R` |
| 保护电路 | PHY 差分线 ESD 防护 | `transmit_tvs=TVS1 on TX_P/TX_N`；`receive_tvs=TVS2 on RX_P/RX_N`；`visible_part_number=ESD3.3V52D-C` |
| 模拟电路 | 发送侧端接 | `transformer_pins=TD+ pin 1; CT pin 2; TD- pin 3`；`pair_resistors=R1/R2 49.9R 1%`；`center_tap_resistor=R3 10R 1%`；`center_tap_capacitor=C1 223 to AGND` |
| 模拟电路 | 接收侧端接 | `transformer_pins=RD+ pin 6; CT pin 7; RD- pin 8`；`series_capacitors=C2/C4 visible value 682`；`termination_resistors=R6/R7 82R 1%`；`center_tap_capacitor=C3 103 to AGND` |
| 接口 | T1 到 RJ45 数据对映射 | `rj45_pin1=TX1_P from T1 TX+ pin 16`；`rj45_pin2=TX1_N from T1 TX- pin 14`；`rj45_pin3=RX1_P from T1 RX+ pin 11`；`rj45_pin6=RX1_N from T1 RX- pin 9` |
| 电源 | PoE 取电输入 | `va1=T1 CT pin 15`；`va2=T1 CT pin 10`；`vb1=RJ45 pins 4 and 5`；`vb2=RJ45 pins 7 and 8`；`destination=P1` |
| 电源 | P1 5V 输出 | `module=P1 5V`；`ground_output=GND`；`power_output=VOUT -> D1 SS54 -> INF+`；`atom_destination=ATOM pin 3 5V` |
| 模拟电路 | RJ45 共模泄放网络 | `va1_branch=C5 223 100V + R9 75R`；`va2_branch=C6 223 100V + R10 75R`；`vb1_branch=C7 223 100V + R12 75R`；`vb2_branch=C8 223 100V + R13 75R`；`common_capacitor=C9 102 2kV to GND` |
| 接口 | ATOM 九针连接 | `odd_pins=1 GND; 3 5V/INF+; 5 G25; 7 G21`；`even_and_power=2 G33; 4 G23; 6 G19; 8 G22; 9 3V3/D3V3` |
| 接口 | I2C 四针接口 | `pin4=G21`；`pin3=G25`；`pin2=not connected`；`pin1=GND` |
| 核心器件 | P1 具体型号可见性 | `reference=P1`；`visible_marking=5V`；`manufacturer_shown=false`；`part_number_shown=false`；`ratings_shown=false` |

## 待确认事项

- `review.poe_module_identity`：P1 PoE 模块的具体料号、输入范围、隔离等级和额定输出功率是什么？；原因：当前原理图只标注 P1 输出为 5V，无法从该页确认模块选型与额定参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4c5ce75fd7c2ce7344ce8d2f66ccfdacfe076b686d83f0e5e213775a530f8d22` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_poe/atom_poe_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_poe.md`

源文档 SHA-256：`01f753b19a50ac95be5f627299ff7a15a131b56f92e4f1571dc127c80ea72915`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
