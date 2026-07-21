# Atom DTU LoRaWAN470 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU LoRaWAN470 |
| SKU | K062 |
| 产品 ID | `atom-dtu-lorawan470-8e943f8cb5b9` |
| 源文档 | `zh_CN/atom/atom_dtu_lorawan470.md` |

## 概述

Atom DTU LoRaWAN470 原理图以 P1 四针端子的 +VIN 为电源入口，经过 F1、SS54 防护和 U1 MP1584EN 降压生成 +5V；板上 +3.3V 为 M1 Ra-07/Ra-07H 无线模块和 U2 SP3485EN-L/TR 供电。M1 通过 UTX/URX 串口连接 Atom-5Pin，并经 R8 0Ω 接到 E1 SMA 天线座，同时引出 SWC、SWD 与 RESET 测试点。RS485 由 TX 驱动 Q1 自动控制 /RE 与 DE，A/B 侧配置偏置、120Ω/NC 可选终端和三只 SP4021-01FTG-C 防护器件，最终与 +VIN/GND 一起接到 P1。

## 检索关键词

`Atom DTU LoRaWAN470`、`K062`、`Ra-07`、`Ra-07H`、`MP1584EN`、`SP3485EN-L/TR`、`SS8050 Y1`、`SP4021-01FTG-C`、`ANT_SMA-KWE`、`RS485_A`、`RS485_B`、`UTXD`、`URXD`、`SWC`、`SWD`、`RESET`、`+VIN`、`+5V`、`+3.3V`、`Atom-4Pin`、`Atom-5Pin`、`HY-2.0_IIC`、`IIC_SCL`、`IIC_SDA`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`、`120Ω/NC`、`470`、`868`、`915`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| F1 | 1.5A/24V | +VIN 输入串联保护器件 | 图 413dc7fd72ca / 第 1 页 / 左上电源区：+VIN 后串联 F1，标注 1.5A/24V |
| U1 | MP1584EN | 将受保护的 +VIN 降压为 +5V 的开关稳压器 | 图 413dc7fd72ca / 第 1 页 / 左上电源区黄色 U1 MP1584EN，VIN/SW/FB/BST/COMP/FREQ 引脚及外围 |
| D1-D2 | SS54 | MP1584EN 开关节点续流与 +VIN 输入对地防护 | 图 413dc7fd72ca / 第 1 页 / 左上电源区：D1 SS54 位于 SW 节点与 GND，D2 SS54 位于 F1 后输入节点与 GND |
| L1 | 10uH | MP1584EN SW 输出到 +5V 的降压电感 | 图 413dc7fd72ca / 第 1 页 / 左上电源区 U1 SW 引脚右侧 L1 10uH，后接 +5V |
| M1 | Ra-07/Ra-07H | 无线通信模块，连接 UART、SWC/SWD、RESET、+3.3V 和 SMA 天线 | 图 413dc7fd72ca / 第 1 页 / 页面中央 M1 Ra-07/Ra-07H，18 针方框及 UTX/URX/ANT/SWCLK/SWDIO/RES/VCC |
| E1 | ANT_SMA-KWE | 经 R8 0Ω 连接 M1 ANT 的外部天线座 | 图 413dc7fd72ca / 第 1 页 / 页面中央偏右 E1 ANT_SMA-KWE；中心端经 R8 0Ω 接 M1 ANT，外壳多点接 GND |
| U2 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 RX/TX 控制逻辑与 RS485_A/RS485_B | 图 413dc7fd72ca / 第 1 页 / 左下黄色 U2 SP3485EN-L/TR，RO-/RE/DE/DI、A/B、VCC/GND 引脚 |
| Q1 | SS8050 Y1 | 由 TX 经 R15 驱动，控制 U2 的 /RE 与 DE 共节点 | 图 413dc7fd72ca / 第 1 页 / 左下 Q1 SS8050 Y1；基极经 R15 1KΩ 接 TX，发射极接 GND，集电极接 /RE/DE |
| D3-D5 | SP4021-01FTG-C | RS485_B 对地、A/B 之间和 RS485_A 对地的三级防护 | 图 413dc7fd72ca / 第 1 页 / 页面下中右 D3、D4、D5 SP4021-01FTG-C，分别跨 GND-B、B-A、A-GND |
| R14 | 120Ω/NC | 跨接 RS485_B 与 RS485_A 的可选终端电阻 | 图 413dc7fd72ca / 第 1 页 / 页面下中 R14 120Ω/NC，竖直跨接 RS485_B 与 RS485_A |
| P1 | HDR_4P | 引出 RS485_B、RS485_A、+VIN 与 GND 的四针端子 | 图 413dc7fd72ca / 第 1 页 / 页面右中 P1 HDR_4P，端子标注 B、A、12V+、12V- |
| J1 | HY-2.0_IIC | 引出 IIC_SCL、IIC_SDA、+5V 与 GND 的四针接口 | 图 413dc7fd72ca / 第 1 页 / 页面右中下 J1 HY-2.0_IIC，1-4 脚依次 IIC_SCL、IIC_SDA、VCC、GND |
| P2 | Atom-5Pin | 连接 Atom 的 3V3、G22/G19 UART 和 G23/G33 RS485 控制信号 | 图 413dc7fd72ca / 第 1 页 / 页面右下 P2 Atom-5Pin，G22/G19/G23/G33 分别接 URXD/UTXD/TX/RX |
| P3 | Atom-4Pin | 连接 Atom 的 G21、G25、+5V 和 GND | 图 413dc7fd72ca / 第 1 页 / 页面右下 P3 Atom-4Pin，1-4 脚为 G21、G25、5V、GND |
| JP1-JP5 | 未标注 | 引出 +3.3V、GND、SWC、SWD 与 RESET 的调试/测试连接点 | 图 413dc7fd72ca / 第 1 页 / 页面左中竖排 JP1-JP5，对应网络 +3.3V、GND、SWC、SWD、RESET |

## 系统结构

### 系统功能分区

原理图由 +VIN 到 +5V 的 MP1584EN 电源、+3.3V 供电的 Ra-07/Ra-07H 无线模块、SP3485EN-L/TR RS485 接口、SMA 天线、Atom 插针、I2C 接口和四针电源/总线端子组成。

- 参数与网络：`radio_module=M1 Ra-07/Ra-07H`；`buck_converter=U1 MP1584EN`；`rs485_transceiver=U2 SP3485EN-L/TR`；`antenna_connector=E1 ANT_SMA-KWE`
- 证据：图 413dc7fd72ca / 第 1 页 / 整页原理图：左上电源、中央 M1、左下 RS485、右侧连接器

## 电源

### +VIN 输入路径

P1 的 12V+ 端连接 +VIN，+VIN 先串联 F1 1.5A/24V，再进入 U1 MP1584EN 的 VIN 引脚；P1 的 12V- 端接 GND。

- 参数与网络：`connector=P1`；`positive_terminal=12V+`；`negative_terminal=12V-`；`input_net=+VIN`；`series_protection=F1 1.5A/24V`
- 证据：图 413dc7fd72ca / 第 1 页 / 右中 P1 +VIN/GND 端子与左上 +VIN-F1-U1 VIN 电源链

### MP1584EN +5V 输出

U1 MP1584EN 的 SW 引脚经 L1 10uH 到 +5V，+5V 输出端由 C3、C4、C5 三只 22uF 电容对地滤波。

- 参数与网络：`converter=U1 MP1584EN`；`switch_pin=1`；`inductor=L1 10uH`；`output_net=+5V`；`output_capacitors=C3/C4/C5 22uF`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 U1 SW-L1-+5V 路径及 C3/C4/C5 对地电容

### MP1584EN 反馈分压

U1 FB 引脚连接 R4 51KΩ 与 R5 10KΩ 的分压节点，R4 上端接 +5V，R5 下端接 GND。

- 参数与网络：`feedback_pin=4`；`upper_resistor=R4 51KΩ`；`lower_resistor=R5 10KΩ`；`sense_net=+5V`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 U1 FB 引脚至 R4/R5 分压网络

### MP1584EN 支持网络

U1 BST 通过 C1 100nF 接 SW 节点，D1 SS54 跨接 SW 节点与 GND；FREQ 经 R6 100KΩ 接地，COMP 经 C6 150pF 与 R7 100KΩ 串联接地，EN 标为未连接。

- 参数与网络：`bootstrap_capacitor=C1 100nF`；`freewheel_diode=D1 SS54`；`frequency_resistor=R6 100KΩ`；`compensation=C6 150pF + R7 100KΩ`；`enable_connected=false`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 U1 的 BST、SW、FREQ、COMP、EN 周边；EN 引脚旁为 no-connect 标记

### M1 3.3V 供电

M1 VCC 9 脚连接 +3.3V，并由 C7 100nF、C8 10uF、C9 33pF 对地去耦。

- 参数与网络：`component=M1`；`vcc_pin=9`；`rail=+3.3V`；`decoupling=C7 100nF; C8 10uF; C9 33pF`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面中央 M1 VCC 9 脚及左侧 +3.3V、C7/C8/C9

### U2 3.3V 供电

U2 SP3485EN-L/TR 的 VCC 8 脚连接 +3.3V，GND 5 脚接地，C11 100nF 跨接 +3.3V 与 GND。

- 参数与网络：`vcc_pin=8`；`gnd_pin=5`；`rail=+3.3V`；`decoupling=C11 100nF`
- 证据：图 413dc7fd72ca / 第 1 页 / 左下 U2 VCC/GND 与 C11 100nF

### +3.3V 储能电容

C12 100uF 跨接 +3.3V 与 GND。

- 参数与网络：`component=C12`；`value=100uF`；`rail=+3.3V`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右下 C12 100uF，连接 +3.3V 与 GND

## 接口

### J1 I2C 接口

J1 HY-2.0_IIC 的 1-4 脚依次为 IIC_SCL、IIC_SDA、VCC、GND；IIC_SCL 接 G21，IIC_SDA 接 G25，VCC 接 +5V。

- 参数与网络：`pin1=IIC_SCL / G21`；`pin2=IIC_SDA / G25`；`pin3=VCC / +5V`；`pin4=GND`；`local_decoupling=C10 100nF from +5V to GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右中下 J1 HY-2.0_IIC、G21/G25/+5V/GND 与 C10 100nF

### P1 四针端子

P1 HDR_4P 从上到下标注 B、A、12V+、12V-，分别连接 RS485_B、RS485_A、+VIN 与 GND。

- 参数与网络：`terminal_b=RS485_B`；`terminal_a=RS485_A`；`terminal_12v_plus=+VIN`；`terminal_12v_minus=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右中 P1 HDR_4P 及左侧四条网络

## 总线

### M1 UART 串口

M1 UTX 11 脚经 R9 22Ω 输出到 UTXD，M1 URX 10 脚经 R10 22Ω 连接 URXD。

- 参数与网络：`transmit=M1 pin 11 UTX -> R9 22Ω -> UTXD`；`receive=URXD -> R10 22Ω -> M1 pin 10 URX`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面中央 M1 UTX/URX 右侧 R9/R10 22Ω 与 UTXD/URXD 网络

### RS485 A/B 差分网络

U2 B 7 脚连接 RS485_B，U2 A 6 脚连接 RS485_A，两条网络均引到 P1 的 B、A 端子。

- 参数与网络：`b_path=U2 pin 7 -> RS485_B -> P1 B`；`a_path=U2 pin 6 -> RS485_A -> P1 A`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面下中 U2 A/B 到 RS485_A/RS485_B，以及右中 P1 B/A

### RS485 偏置

RS485_B 通过 R11 4.7KΩ 接 GND，RS485_A 通过 R16 4.7KΩ 接 +3.3V。

- 参数与网络：`b_bias=R11 4.7KΩ to GND`；`a_bias=R16 4.7KΩ to +3.3V`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面下中 R11 从 RS485_B 接 GND，R16 从 RS485_A 接 +3.3V

### RS485 可选终端

R14 标注 120Ω/NC，并跨接 RS485_B 与 RS485_A。

- 参数与网络：`component=R14`；`value=120Ω/NC`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面下中 R14 120Ω/NC 竖跨 A/B 网络

## GPIO 与控制信号

### Atom-5Pin 映射

P2 Atom-5Pin 的 1-5 脚依次为 3V3、G22、G19、G23、G33；G22 接 URXD，G19 接 UTXD，G23 接 TX，G33 接 RX。

- 参数与网络：`pin1=3V3`；`pin2=G22 -> URXD`；`pin3=G19 -> UTXD`；`pin4=G23 -> TX`；`pin5=G33 -> RX`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右下 P2 Atom-5Pin 与右侧 URXD/UTXD/TX/RX 网络

### Atom-4Pin 映射

P3 Atom-4Pin 的 1-4 脚依次为 G21、G25、5V、GND。

- 参数与网络：`pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右下 P3 Atom-4Pin，方框内外均标注 G21/G25/5V/GND

## 保护电路

### +VIN 输入防护

F1 后的输入节点通过 D2 SS54 和 C2 10uF 分别接 GND。

- 参数与网络：`node=F1 output / U1 VIN`；`diode=D2 SS54`；`capacitor=C2 10uF`；`reference=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 F1 后节点：D2 SS54 对地、C2 10uF 对地

### RS485 防护网络

D3、D4、D5 均标注 SP4021-01FTG-C；D3 跨 GND 与 RS485_B，D4 跨 RS485_B 与 RS485_A，D5 跨 RS485_A 与 GND。

- 参数与网络：`d3=GND to RS485_B`；`d4=RS485_B to RS485_A`；`d5=RS485_A to GND`；`part_number=SP4021-01FTG-C`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面下中右 D3-D5 与 RS485_B/RS485_A/GND 三节点

## 关键网络

### RS485 方向控制

TX 经 R15 1KΩ 驱动 Q1 SS8050 Y1 基极；Q1 发射极接 GND，集电极连接 U2 的 /RE 2 脚和 DE 3 脚共节点，该节点由 R13 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`control_net=TX`；`base_resistor=R15 1KΩ`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U2 /RE pin 2 and DE pin 3`；`pullup=R13 4.7KΩ to +3.3V`
- 证据：图 413dc7fd72ca / 第 1 页 / 左下 TX-R15-Q1 与 U2 /RE/DE 共节点、R13 上拉

### U2 驱动输入

U2 的 DI 4 脚直接连接 GND。

- 参数与网络：`component=U2 SP3485EN-L/TR`；`pin=4`；`signal=DI`；`connection=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 左下 U2 DI 4 脚向左再向下连接 GND

### U2 接收输出

U2 的 RO 1 脚经 R12 1KΩ 连接 RX 网络，RX 再连接 P2 Atom-5Pin 的 G33。

- 参数与网络：`source=U2 RO pin 1`；`series_resistor=R12 1KΩ`；`net=RX`；`atom_gpio=G33`
- 证据：图 413dc7fd72ca / 第 1 页 / 左下 U2 RO-R12-RX 与右下 P2 G33-RX

## 射频

### M1 天线通路

M1 ANT 18 脚经 R8 0Ω 连接 E1 ANT_SMA-KWE 中心端，E1 的外壳端多点接 GND；M1 GND 17 脚也接地。

- 参数与网络：`source=M1 ANT pin 18`；`series_resistor=R8 0Ω`；`connector=E1 ANT_SMA-KWE`；`module_ground_pin=17`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面中央 M1 18/17 脚、R8 0Ω 与 E1 ANT_SMA-KWE

## 调试与烧录

### 无线模块调试测试点

M1 SWCLK 7 脚连接 SWC，SWDIO 8 脚连接 SWD，RES 16 脚连接 RESET；JP3、JP4、JP5 分别引出 SWC、SWD、RESET，JP1 和 JP2 引出 +3.3V 与 GND。

- 参数与网络：`swclk=M1 pin 7 -> SWC -> JP3`；`swdio=M1 pin 8 -> SWD -> JP4`；`reset=M1 pin 16 -> RESET -> JP5`；`power_test=JP1 +3.3V; JP2 GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面中央 M1 SWCLK/SWDIO/RES 网络与左中 JP1-JP5 引出

## 其他事实

### 频段装配标注表

页面右上独立表格显示 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915；该表格未画出与主电路的连线。

- 参数与网络：`r1=0Ω -> 470`；`r2=0Ω -> 868`；`r3=0Ω -> 915`；`connected_in_page=false`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面右上 R1/R2/R3 与 470/868/915 三行独立表格

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统功能分区 | `radio_module=M1 Ra-07/Ra-07H`；`buck_converter=U1 MP1584EN`；`rs485_transceiver=U2 SP3485EN-L/TR`；`antenna_connector=E1 ANT_SMA-KWE` |
| 电源 | +VIN 输入路径 | `connector=P1`；`positive_terminal=12V+`；`negative_terminal=12V-`；`input_net=+VIN`；`series_protection=F1 1.5A/24V` |
| 保护电路 | +VIN 输入防护 | `node=F1 output / U1 VIN`；`diode=D2 SS54`；`capacitor=C2 10uF`；`reference=GND` |
| 电源 | MP1584EN +5V 输出 | `converter=U1 MP1584EN`；`switch_pin=1`；`inductor=L1 10uH`；`output_net=+5V`；`output_capacitors=C3/C4/C5 22uF` |
| 电源 | MP1584EN 反馈分压 | `feedback_pin=4`；`upper_resistor=R4 51KΩ`；`lower_resistor=R5 10KΩ`；`sense_net=+5V` |
| 电源 | MP1584EN 支持网络 | `bootstrap_capacitor=C1 100nF`；`freewheel_diode=D1 SS54`；`frequency_resistor=R6 100KΩ`；`compensation=C6 150pF + R7 100KΩ`；`enable_connected=false` |
| 电源 | M1 3.3V 供电 | `component=M1`；`vcc_pin=9`；`rail=+3.3V`；`decoupling=C7 100nF; C8 10uF; C9 33pF` |
| 调试与烧录 | 无线模块调试测试点 | `swclk=M1 pin 7 -> SWC -> JP3`；`swdio=M1 pin 8 -> SWD -> JP4`；`reset=M1 pin 16 -> RESET -> JP5`；`power_test=JP1 +3.3V; JP2 GND` |
| 射频 | M1 天线通路 | `source=M1 ANT pin 18`；`series_resistor=R8 0Ω`；`connector=E1 ANT_SMA-KWE`；`module_ground_pin=17` |
| 总线 | M1 UART 串口 | `transmit=M1 pin 11 UTX -> R9 22Ω -> UTXD`；`receive=URXD -> R10 22Ω -> M1 pin 10 URX` |
| GPIO 与控制信号 | Atom-5Pin 映射 | `pin1=3V3`；`pin2=G22 -> URXD`；`pin3=G19 -> UTXD`；`pin4=G23 -> TX`；`pin5=G33 -> RX` |
| GPIO 与控制信号 | Atom-4Pin 映射 | `pin1=G21`；`pin2=G25`；`pin3=5V`；`pin4=GND` |
| 接口 | J1 I2C 接口 | `pin1=IIC_SCL / G21`；`pin2=IIC_SDA / G25`；`pin3=VCC / +5V`；`pin4=GND`；`local_decoupling=C10 100nF from +5V to GND` |
| 电源 | U2 3.3V 供电 | `vcc_pin=8`；`gnd_pin=5`；`rail=+3.3V`；`decoupling=C11 100nF` |
| 关键网络 | RS485 方向控制 | `control_net=TX`；`base_resistor=R15 1KΩ`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U2 /RE pin 2 and DE pin 3`；`pullup=R13 4.7KΩ to +3.3V` |
| 关键网络 | U2 驱动输入 | `component=U2 SP3485EN-L/TR`；`pin=4`；`signal=DI`；`connection=GND` |
| 关键网络 | U2 接收输出 | `source=U2 RO pin 1`；`series_resistor=R12 1KΩ`；`net=RX`；`atom_gpio=G33` |
| 总线 | RS485 A/B 差分网络 | `b_path=U2 pin 7 -> RS485_B -> P1 B`；`a_path=U2 pin 6 -> RS485_A -> P1 A` |
| 总线 | RS485 偏置 | `b_bias=R11 4.7KΩ to GND`；`a_bias=R16 4.7KΩ to +3.3V` |
| 总线 | RS485 可选终端 | `component=R14`；`value=120Ω/NC`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A` |
| 保护电路 | RS485 防护网络 | `d3=GND to RS485_B`；`d4=RS485_B to RS485_A`；`d5=RS485_A to GND`；`part_number=SP4021-01FTG-C` |
| 接口 | P1 四针端子 | `terminal_b=RS485_B`；`terminal_a=RS485_A`；`terminal_12v_plus=+VIN`；`terminal_12v_minus=GND` |
| 电源 | +3.3V 储能电容 | `component=C12`；`value=100uF`；`rail=+3.3V` |
| 其他事实 | 频段装配标注表 | `r1=0Ω -> 470`；`r2=0Ω -> 868`；`r3=0Ω -> 915`；`connected_in_page=false` |

## 待确认事项

- `review.radio_module_variant`：K062 当前硬件版本实际装配的是 Ra-07 还是 Ra-07H，且其内部通信芯片型号是什么？；原因：M1 在原理图中并列标为 Ra-07/Ra-07H，页面未显示内部芯片型号。
- `review.band_resistor_population`：470 MHz 版本的 R1/R2/R3 实际装配状态和对应配置网络是什么？；原因：页面仅给出 R1/R2/R3 与 470/868/915 的独立装配表，没有画出它们与 M1 的连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `413dc7fd72cad70452238a33b69a91afd73bdebe5f386c378c1ecc754444247f` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_dtu_lorawan470.md`

源文档 SHA-256：`df68d6652531ee17ea8a06db05e0518a9d75b2db55a41f34a5bfbabb2f6cadeb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
