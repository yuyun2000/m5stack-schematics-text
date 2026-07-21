# Atom DTU LoRaWAN-EU868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU LoRaWAN-EU868 |
| SKU | A152-EU868 |
| 产品 ID | `atom-dtu-lorawan-eu868-a2ca17869da8` |
| 源文档 | `zh_CN/atom/Atom DTU LoRaWAN-EU868.md` |

## 概述

Atom DTU LoRaWAN-EU868 以 M1 RAK3172 为无线通信模组，通过 Atom-5Pin 的 G22/G19 UART 连接模组，并经 R9 0Ω 与预留 C14/C15 匹配位连接 E1 SMA 天线座。P1 的 12V+ 进入 +VIN，经 F1 和 U1 MP1584EN 降压后通过 D7 形成 +5V；+3.3V 从 Atom-5Pin 引入，为 RAK3172、U2 SP3485EN-L/TR 与相关逻辑供电。Atom-5Pin 的 G23/G33 连接自动方向控制 RS485 电路，差分 A/B 具有偏置、可选 120Ω 端接和 SP4021 保护，并与 +VIN/GND 一同引到 4 Pin 端子。

## 检索关键词

`Atom DTU LoRaWAN-EU868`、`A152-EU868`、`EU868`、`863-870 MHz`、`RAK3172`、`STM32WLE5`、`MP1584EN`、`SP3485EN-L/TR`、`SS8050 Y1`、`LoRaWAN`、`LoRa P2P`、`RS485`、`RS485_A`、`RS485_B`、`ANT_SMA-KWE`、`R9 0Ω`、`C14 NC`、`C15 NC`、`Atom-5Pin`、`Atom-4Pin`、`HY-2.0_IIC`、`G19`、`G22`、`G23`、`G33`、`G21`、`G25`、`U2_RX`、`U2_TX`、`SWDIO`、`SWCLK`、`RST`、`BOOT`、`+VIN`、`+5V`、`+3.3V`、`F1 1.5A/24V`、`R14 120Ω/NC`、`SP4021-01FTG-C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MP1584EN | +VIN 到 +5V 路径中的降压转换器 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1A~2B：U1 MP1584EN，VIN/SW/BST/FB/FREQ/COMP/GND 与外围电感、电容、电阻 |
| M1 | RAK3172 | LoRaWAN 无线通信模组，连接 Atom UART、SWD、复位、启动与射频天线 | 图 70a4d5ed1c36 / 第 1 页 / 网格 2B~3C：M1 RAK3172 32 Pin 符号及 U2_RX/U2_TX/SWDIO/SWCLK/RF/RST/BOOT/VDD/GND |
| U2 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 Atom RX/TX 控制与 RS485_A/RS485_B | 图 70a4d5ed1c36 / 第 1 页 / 网格 1D~2D：U2 SP3485EN-L/TR 的 RO/nRE/DE/DI/A/B/VCC/GND 引脚 |
| Q1 | SS8050 Y1 | 由 TX 经 R15 驱动的 RS485 nRE/DE 自动方向控制晶体管 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1D：TX-R15 1KΩ-Q1 SS8050，集电极接 U2 pins 2/3，发射极接 GND |
| E1 | ANT_SMA-KWE | 外部 LoRa 天线 SMA 连接器 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1C~2C：E1 ANT_SMA-KWE 中心端 ANT 与外壳 GND |
| F1 | 1.5A/24V | +VIN 输入串联保险丝 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1A：+VIN-F1 1.5A/24V-U1 VIN 输入节点 |
| D1/D2/D7 | SS54 | MP1584EN 输入、开关节点与 +5V 输出路径中的肖特基二极管 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1A~3A：D2 从输入节点到 GND、D1 从 SW 节点到 GND、D7 从降压输出到 +5V |
| P1 | HDR_4P | RS485 A/B 与 12V+/12V- 电源接线端子接口 | 图 70a4d5ed1c36 / 第 1 页 / 网格 4C：P1 HDR_4P 的 B/A/12V+/12V- 与 RS485_B/RS485_A/+VIN/GND |
| J1 | HY-2.0_IIC | G21/G25 与 +5V/GND 的 4 Pin Grove/I2C 接口 | 图 70a4d5ed1c36 / 第 1 页 / 网格 4C：J1 HY-2.0_IIC，pins 1~4 为 IIC_SCL/IIC_SDA/VCC/GND |
| P2 | Atom-5Pin | Atom 主控的 3.3V、LoRa UART 与 RS485 UART 接口 | 图 70a4d5ed1c36 / 第 1 页 / 网格 4D：P2 Atom-5Pin，pins 1~5 为 3V3/G22/G19/G23/G33 |
| P3 | Atom-4Pin | Atom 主控到 Grove 的 G21/G25/+5V/GND 接口 | 图 70a4d5ed1c36 / 第 1 页 / 网格 3D~4D：P3 Atom-4Pin，pins 1~4 为 G21/G25/5V/GND |
| R14 | 120Ω/NC | RS485_A 与 RS485_B 之间的可选终端电阻位 | 图 70a4d5ed1c36 / 第 1 页 / 网格 2D：R14 120Ω/NC 跨接 RS485_B 与 RS485_A |
| D3/D4/D5 | SP4021-01FTG-C | RS485 A/B 对地及线间瞬态保护器件 | 图 70a4d5ed1c36 / 第 1 页 / 网格 2D：D3 从 RS485_B 到 GND、D4 跨 A/B、D5 从 RS485_A 到 GND |
| TVS1 | SMFJ5.0A | +5V 到 GND 的瞬态抑制器 | 图 70a4d5ed1c36 / 第 1 页 / 网格 3D：TVS1 SMFJ5.0A 连接 +5V 与 GND |
| JP1~JP6 | Test pads | 3.3V、GND、SWCLK、SWDIO、RST 与 BOOT 测试/调试点 | 图 70a4d5ed1c36 / 第 1 页 / 网格 1C：JP1 +3.3V、JP2 GND、JP3 SWCLK、JP4 SWDIO、JP5 RST、JP6 BOOT |
| R1/R2/R3 | 0Ω | 页面右上角 470/868/915 频段配置表中的三个电阻位，实际装配与连线待确认 | 图 70a4d5ed1c36 / 第 1 页 / 网格 4A：R1 0Ω-470、R2 0Ω-868、R3 0Ω-915 表格 |

## 系统结构

### Atom DTU LoRaWAN-EU868

电路由 RAK3172 无线模组、MP1584EN 5V 降压电源、SP3485EN-L/TR RS485 收发器、Atom 4/5 Pin 主控接口、SMA 天线接口与 Grove 接口组成。

- 参数与网络：`radio=M1 RAK3172`；`power=U1 MP1584EN`；`rs485=U2 SP3485EN-L/TR`；`host_interfaces=P2 Atom-5Pin,P3 Atom-4Pin`；`antenna=E1 ANT_SMA-KWE`；`grove=J1 HY-2.0_IIC`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 整页 U1/M1/U2/P1/P2/P3/J1/E1 功能块及同名网络

## 电源

### +VIN 输入

P1 的 12V+ 引脚连接 +VIN，+VIN 经 F1 1.5A/24V 后进入 U1 VIN；F1 后节点由 D2 SS54 与 C2 22uF/35V 接地。

- 参数与网络：`terminal=P1 12V+`；`net=+VIN`；`fuse=F1 1.5A/24V`；`clamp_diode=D2 SS54 to GND`；`input_capacitor=C2 22uF/35V`；`converter_input=U1 pin 7 VIN`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4C P1 12V+ 与网格 1A +VIN-F1-D2-C2-U1 VIN 路径

### U1 MP1584EN 降压输出

U1 SW 引脚 1 经 L1 22uH 到输出节点，D1 SS54 接在 SW 节点与 GND 之间；输出节点由 C3/C4/C5 各 22uF 滤波，经 D7 SS54 形成 +5V。

- 参数与网络：`controller=U1 MP1584EN`；`switch_pin=pin 1 SW`；`inductor=L1 22uH`；`catch_diode=D1 SS54`；`output_capacitors=C3/C4/C5 22uF`；`series_diode=D7 SS54`；`output=+5V`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 1A~3A：U1 SW-D1-L1-C3/C4/C5-D7-+5V

### MP1584EN 反馈与补偿

U1 FB 引脚 4 接 R4 56KΩ 与 R5 10KΩ 分压点；FREQ 引脚 6 经 R6 100KΩ 接地，COMP 引脚 3 经 C6 150pF 与 R7 100KΩ 串联接地，EN 引脚 2 标为未连接。

- 参数与网络：`feedback_top=R4 56KΩ`；`feedback_bottom=R5 10KΩ`；`frequency_resistor=R6 100KΩ`；`compensation=C6 150pF,R7 100KΩ`；`enable=U1 pin 2 EN no-connect`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 1A~2B：U1 FB/FREQ/COMP/EN 与 R4/R5/R6/C6/R7

### +3.3V 电源域

P2 Atom-5Pin 引脚 1 引入 +3.3V，连接 M1 VDD 引脚 24、U2 VCC 引脚 8、复位上拉 R8、UART 偏置 D6，以及 C8/C9/C13/C11/C12 和 D9 等支路。

- 参数与网络：`source=P2 pin 1 3V3`；`radio=M1 pin 24 VDD`；`rs485=U2 pin 8 VCC`；`radio_decoupling=C8 100nF,C9 22uF,C13 33pF`；`rs485_decoupling=C11 100nF`；`bulk_capacitor=C12 100uF`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4D P2 pin 1 与 M1/U2/R8/D6/C8/C9/C13/C11/C12/D9 的同名 +3.3V 网络

## 接口

### P1 HDR_4P

P1 四个端子自上而下为 B、A、12V+、12V-，分别连接 RS485_B、RS485_A、+VIN 与 GND。

- 参数与网络：`B=RS485_B`；`A=RS485_A`；`12V_plus=+VIN`；`12V_minus=GND`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4C：P1 HDR_4P 的 B/A/12V+/12V- 与左侧网络

### P2 Atom-5Pin

P2 引脚 1~5 依次为 +3.3V、G22、G19、G23、G33；G22/G19 连接 RAK3172 UART，G23/G33 分别标为 TX/RX 并连接 RS485 电路。

- 参数与网络：`pin_1=+3.3V`；`pin_2=G22 to U2_RX`；`pin_3=G19 to U2_TX`；`pin_4=G23 TX`；`pin_5=G33 RX`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4D：P2 Atom-5Pin pins 1~5、R18/R19/U2_RX/U2_TX 与 TX/RX 网络

### P3 Atom-4Pin 到 J1 HY-2.0_IIC

P3 引脚 1/2/3/4 的 G21/G25/+5V/GND 分别连接 J1 引脚 1/2/3/4 的 IIC_SCL/IIC_SDA/VCC/GND；C10 100nF 接在 +5V 与 GND 之间。

- 参数与网络：`scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C10 100nF`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 3D~4D：P3 Atom-4Pin、J1 HY-2.0_IIC 与 C10

### SP3485EN RS485 A/B

U2 B 引脚 7 连接 RS485_B 并由 R11 4.7KΩ 接 GND；U2 A 引脚 6 连接 RS485_A 并由 R16 4.7KΩ 接 +3.3V；R14 以 120Ω/NC 标注跨接 A/B。

- 参数与网络：`B=U2 pin 7-RS485_B-R11 4.7KΩ-GND`；`A=U2 pin 6-RS485_A-R16 4.7KΩ-+3.3V`；`termination=R14 120Ω/NC across A/B`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 2D：U2 pins 6/7、R11/R16/R14 与 RS485_A/RS485_B

## 总线

### Atom 与 RAK3172 UART

P2 G22 经 R18 22Ω 连接 U2_RX，并进入 M1 引脚 1；P2 G19 经 R19 22Ω 连接 U2_TX，并进入 M1 引脚 2。R10/R17 各 10KΩ 从两路信号接到 D6 后节点，D6 的另一端接 +3.3V。

- 参数与网络：`module_rx=P2 pin 2 G22-R18 22Ω-U2_RX-M1 pin 1`；`module_tx=P2 pin 3 G19-R19 22Ω-U2_TX-M1 pin 2`；`bias_rx=R10 10KΩ to D6 node`；`bias_tx=R17 10KΩ to D6 node`；`diode=D6 1N4148WS T4 to +3.3V`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4D P2/R10/R17/R18/R19/D6 与网格 2B M1 pins 1/2 的 U2_RX/U2_TX

### Atom 与 SP3485EN 控制

P2 G33 的 RX 网络经 R12 1KΩ 接 U2 RO 引脚 1；P2 G23 的 TX 网络经 R15 1KΩ 驱动 Q1 基极，Q1 集电极连接 U2 nRE/DE 引脚 2/3并由 R13 4.7KΩ 上拉到 +3.3V，U2 DI 引脚 4 接 GND。

- 参数与网络：`receive=U2 pin 1 RO-R12 1KΩ-RX-P2 pin 5 G33`；`direction_drive=P2 pin 4 G23-TX-R15 1KΩ-Q1 base`；`direction_node=Q1 collector-U2 pins 2 nRE and 3 DE-R13 4.7KΩ to +3.3V`；`driver_input=U2 pin 4 DI to GND`；`transistor=Q1 SS8050 Y1`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 1D U2/Q1/R12/R13/R15 的 RX/TX/nRE/DE/DI 与网格 4D P2 G23/G33

## 复位

### RAK3172 RST

M1 RST 引脚 22 连接 RST 网络与 JP5，R8 10KΩ 将 RST 上拉到 +3.3V，C7 1uF 将 RST 接到 GND。

- 参数与网络：`module_pin=M1 pin 22 RST`；`test_pad=JP5`；`pullup=R8 10KΩ to +3.3V`；`capacitor=C7 1uF to GND`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4B R8/RST/C7 与网格 2C M1 pin 22、网格 1C JP5

## 保护电路

### RS485 A/B 瞬态保护

D3 SP4021-01FTG-C 连接 RS485_B 与 GND，D5 同型号连接 RS485_A 与 GND，D4 同型号跨接 RS485_B 与 RS485_A。

- 参数与网络：`B_to_ground=D3 SP4021-01FTG-C`；`A_to_ground=D5 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 2D：D3/D4/D5 围绕 RS485_B/RS485_A 的三器件保护网络

### +5V 与 +3.3V 保护支路

TVS1 SMFJ5.0A 连接 +5V 与 GND，D9 LESD3Z5.0CMT1G 连接 +3.3V 与 GND，D10 LESD3Z5.0CMT1G 连接 MP1584EN 输出节点与 GND。

- 参数与网络：`five_volt=TVS1 SMFJ5.0A`；`three_volt_three=D9 LESD3Z5.0CMT1G`；`buck_output=D10 LESD3Z5.0CMT1G`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 3D TVS1/D9 与网格 3A D10 的电源轨到 GND 支路

## 关键网络

### RAK3172 BOOT

M1 BOOT 引脚 21 连接 BOOT 网络并引到 JP6，页面未绘制该网络的固定上拉或下拉电阻。

- 参数与网络：`module_pin=M1 pin 21 BOOT`；`test_pad=JP6`；`external_strap=not drawn`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 2C M1 pin 21 BOOT 与网格 1C JP6 BOOT，同页无该网络电阻支路

## 射频

### RAK3172 RF 到 SMA

M1 RF 引脚 12 经 R9 0Ω 到 ANT 网络并连接 E1 ANT_SMA-KWE 中心端；C15 与 C14 分别位于 R9 两侧并接地，两个电容位均标为 NC，E1 外壳引脚接 GND。

- 参数与网络：`radio_pin=M1 pin 12 RF`；`series=R9 0Ω`；`antenna_net=ANT`；`connector=E1 ANT_SMA-KWE`；`module_side_shunt=C15 NC to GND`；`antenna_side_shunt=C14 NC to GND`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 1C~2C：M1 pin 12 RF-C15 NC-R9 0Ω-C14 NC-ANT-E1 ANT_SMA-KWE

## 调试与烧录

### RAK3172 SWD 与测试点

M1 SWDIO 引脚 7 连接 JP4，SWCLK 引脚 8 连接 JP3；JP1、JP2、JP5、JP6 分别引出 +3.3V、GND、RST、BOOT。

- 参数与网络：`swdio=M1 pin 7-JP4`；`swclk=M1 pin 8-JP3`；`power=JP1 +3.3V`；`ground=JP2 GND`；`reset=JP5 RST`；`boot=JP6 BOOT`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 网格 1C JP1~JP6 与网格 2B M1 pins 7/8/22/21 的同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU LoRaWAN-EU868 | `radio=M1 RAK3172`；`power=U1 MP1584EN`；`rs485=U2 SP3485EN-L/TR`；`host_interfaces=P2 Atom-5Pin,P3 Atom-4Pin`；`antenna=E1 ANT_SMA-KWE`；`grove=J1 HY-2.0_IIC` |
| 电源 | +VIN 输入 | `terminal=P1 12V+`；`net=+VIN`；`fuse=F1 1.5A/24V`；`clamp_diode=D2 SS54 to GND`；`input_capacitor=C2 22uF/35V`；`converter_input=U1 pin 7 VIN` |
| 电源 | U1 MP1584EN 降压输出 | `controller=U1 MP1584EN`；`switch_pin=pin 1 SW`；`inductor=L1 22uH`；`catch_diode=D1 SS54`；`output_capacitors=C3/C4/C5 22uF`；`series_diode=D7 SS54`；`output=+5V` |
| 电源 | MP1584EN 反馈与补偿 | `feedback_top=R4 56KΩ`；`feedback_bottom=R5 10KΩ`；`frequency_resistor=R6 100KΩ`；`compensation=C6 150pF,R7 100KΩ`；`enable=U1 pin 2 EN no-connect` |
| 电源 | +3.3V 电源域 | `source=P2 pin 1 3V3`；`radio=M1 pin 24 VDD`；`rs485=U2 pin 8 VCC`；`radio_decoupling=C8 100nF,C9 22uF,C13 33pF`；`rs485_decoupling=C11 100nF`；`bulk_capacitor=C12 100uF` |
| 接口 | P1 HDR_4P | `B=RS485_B`；`A=RS485_A`；`12V_plus=+VIN`；`12V_minus=GND` |
| 接口 | P2 Atom-5Pin | `pin_1=+3.3V`；`pin_2=G22 to U2_RX`；`pin_3=G19 to U2_TX`；`pin_4=G23 TX`；`pin_5=G33 RX` |
| 接口 | P3 Atom-4Pin 到 J1 HY-2.0_IIC | `scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C10 100nF` |
| 总线 | Atom 与 RAK3172 UART | `module_rx=P2 pin 2 G22-R18 22Ω-U2_RX-M1 pin 1`；`module_tx=P2 pin 3 G19-R19 22Ω-U2_TX-M1 pin 2`；`bias_rx=R10 10KΩ to D6 node`；`bias_tx=R17 10KΩ to D6 node`；`diode=D6 1N4148WS T4 to +3.3V` |
| 总线 | Atom 与 SP3485EN 控制 | `receive=U2 pin 1 RO-R12 1KΩ-RX-P2 pin 5 G33`；`direction_drive=P2 pin 4 G23-TX-R15 1KΩ-Q1 base`；`direction_node=Q1 collector-U2 pins 2 nRE and 3 DE-R13 4.7KΩ to +3.3V`；`driver_input=U2 pin 4 DI to GND`；`transistor=Q1 SS8050 Y1` |
| 接口 | SP3485EN RS485 A/B | `B=U2 pin 7-RS485_B-R11 4.7KΩ-GND`；`A=U2 pin 6-RS485_A-R16 4.7KΩ-+3.3V`；`termination=R14 120Ω/NC across A/B` |
| 保护电路 | RS485 A/B 瞬态保护 | `B_to_ground=D3 SP4021-01FTG-C`；`A_to_ground=D5 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C` |
| 保护电路 | +5V 与 +3.3V 保护支路 | `five_volt=TVS1 SMFJ5.0A`；`three_volt_three=D9 LESD3Z5.0CMT1G`；`buck_output=D10 LESD3Z5.0CMT1G` |
| 射频 | RAK3172 RF 到 SMA | `radio_pin=M1 pin 12 RF`；`series=R9 0Ω`；`antenna_net=ANT`；`connector=E1 ANT_SMA-KWE`；`module_side_shunt=C15 NC to GND`；`antenna_side_shunt=C14 NC to GND` |
| 射频 | 470/868/915 频段配置表 | `470=R1 0Ω`；`868=R2 0Ω`；`915=R3 0Ω`；`selected_population=null`；`product_region=EU868` |
| 调试与烧录 | RAK3172 SWD 与测试点 | `swdio=M1 pin 7-JP4`；`swclk=M1 pin 8-JP3`；`power=JP1 +3.3V`；`ground=JP2 GND`；`reset=JP5 RST`；`boot=JP6 BOOT` |
| 复位 | RAK3172 RST | `module_pin=M1 pin 22 RST`；`test_pad=JP5`；`pullup=R8 10KΩ to +3.3V`；`capacitor=C7 1uF to GND` |
| 关键网络 | RAK3172 BOOT | `module_pin=M1 pin 21 BOOT`；`test_pad=JP6`；`external_strap=not drawn` |

## 待确认事项

- `rf.region-resistor-table`：页面右上表格将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915，但表格没有显示三个电阻的电气连接或实际装配状态，无法仅凭此页确认 EU868 版本是否装配 R2。（证据：图 70a4d5ed1c36 / 第 1 页 / 网格 4A：R1/R2/R3 0Ω 与 470/868/915 的独立表格，无外接网络）
- `review.eu868-region-resistor`：请用 A152-EU868 的 BOM、PCB 或装配图确认 R2 0Ω 是否为 EU868 版本的实际装配位，并确认 R1/R2/R3 所连接的配置网络。；原因：原理图只给出 R1/R2/R3 与 470/868/915 的对照表，没有绘制电气连接或装配标记，不能从表格单独证明 R2 已实装。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `70a4d5ed1c36f2e3667818970c8fb2db0e9d2b6af530d1a899ae3e0f768d03d3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1139/A152_EU868_Sch_page_01.png` |

---

源文档：`zh_CN/atom/Atom DTU LoRaWAN-EU868.md`

源文档 SHA-256：`d28d22d6f4f66a0d0f50603d87b2eef8955a29994f826bd2d0a1f44fa6f8800f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
