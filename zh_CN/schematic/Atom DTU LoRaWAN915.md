# Atom DTU LoRaWAN915 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU LoRaWAN915 |
| SKU | K061 |
| 产品 ID | `atom-dtu-lorawan915-a9d2804d7e36` |
| 源文档 | `zh_CN/atom/atom_dtu_lorawan915.md` |

## 概述

Atom DTU LoRaWAN915 以 M1 Ra-07/Ra-07H 无线模组为核心，Atom-5Pin 的 G22/G19 通过 UTXD/URXD UART 与模组通信，并引出 SWCLK、SWDIO、RESET 测试点及 E1 SMA 天线。P1 的 12V+ 输入形成 +VIN，U1 MP1584EN 经 F1、L1 与 SS54 二极管降压生成 +5V；Atom-5Pin 引入 +3.3V，为无线模组和 U2 SP3485EN-L/TR 供电。G23/G33 连接自动方向控制 RS485 电路，A/B 具有偏置、可选 120Ω 端接与 SP4021 保护，G21/G25 则连接 5V I2C 接口。

## 检索关键词

`Atom DTU LoRaWAN915`、`K061`、`US915`、`915MHz`、`ASR6501`、`Ra-07`、`Ra-07H`、`MP1584EN`、`SP3485EN-L/TR`、`SS8050 Y1`、`LoRaWAN`、`RS485`、`RS485_A`、`RS485_B`、`ANT_SMA-KWE`、`UTXD`、`URXD`、`TX`、`RX`、`SWC`、`SWD`、`RESET`、`G22`、`G19`、`G23`、`G33`、`G21`、`G25`、`IIC_SCL`、`IIC_SDA`、`+VIN`、`+5V`、`+3.3V`、`F1 1.5A/24V`、`R14 120Ω/NC`、`SP4021-01FTG-C`、`R3 0Ω 915`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | Ra-07/Ra-07H | 无线通信模组，连接 UART、SWD、复位、3.3V 电源与 SMA 天线 | 图 413dc7fd72ca / 第 1 页 / 页面中央 M1 Ra-07/Ra-07H，pins 1~18 的 GND/ADC/AUX/SETA/DIO3/SETB/SWCLK/SWDIO/VCC/URX/UTX/P00/P01/P06/P07/RES/GND/ANT |
| U1 | MP1584EN | +VIN 到 +5V 的降压转换器 | 图 413dc7fd72ca / 第 1 页 / 左上 U1 MP1584EN：VIN/SW/BST/FB/FREQ/COMP/GND 与 F1/L1/D1/D2/R4~R7 |
| U2 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 Atom TX/RX 与 RS485_A/RS485_B | 图 413dc7fd72ca / 第 1 页 / 左下 U2 SP3485EN-L/TR 的 RO/nRE/DE/DI/A/B/VCC/GND |
| Q1 | SS8050 Y1 | 由 TX 经 R15 驱动的 RS485 nRE/DE 自动方向控制晶体管 | 图 413dc7fd72ca / 第 1 页 / 左下 TX-R15 1KΩ-Q1 SS8050，集电极接 U2 pins 2/3，发射极接 GND |
| E1 | ANT_SMA-KWE | 无线模组外部 SMA 天线连接器 | 图 413dc7fd72ca / 第 1 页 / 中央 E1 ANT_SMA-KWE，经 R8 0Ω 接 M1 ANT pin 18，外壳接 GND |
| D3/D4/D5 | SP4021-01FTG-C | RS485 A/B 对地与线间瞬态保护器件 | 图 413dc7fd72ca / 第 1 页 / 下部 D3 从 RS485_B 到 GND、D4 跨 A/B、D5 从 RS485_A 到 GND |
| F1 | 1.5A/24V | +VIN 输入串联保险丝 | 图 413dc7fd72ca / 第 1 页 / 左上 +VIN-F1 1.5A/24V-U1 VIN 输入节点 |
| D1/D2 | SS54 | MP1584EN 输入与开关节点的肖特基二极管 | 图 413dc7fd72ca / 第 1 页 / 左上 D2 从 Vin 输入节点到 GND，D1 从 U1 SW 节点到 GND |
| P1 | HDR_4P | RS485_B、RS485_A、12V+ 与 12V- 接线端子 | 图 413dc7fd72ca / 第 1 页 / 右中 P1 HDR_4P 的 B/A/12V+/12V- 与 RS485_B/RS485_A/+VIN/GND |
| J1 | HY-2.0_IIC | G21/G25 对应 I2C SCL/SDA 的 5V Grove 接口 | 图 413dc7fd72ca / 第 1 页 / 右中 J1 HY-2.0_IIC，pins 1~4 为 IIC_SCL/IIC_SDA/VCC/GND |
| P2 | Atom-5Pin | Atom 主控到无线模组 UART、RS485 UART 与 3.3V 的连接器 | 图 413dc7fd72ca / 第 1 页 / 右下 P2 Atom-5Pin，pins 1~5 为 3V3/G22/G19/G23/G33 与 URXD/UTXD/TX/RX |
| P3 | Atom-4Pin | Atom 主控到 I2C Grove 的 G21/G25/5V/GND 连接器 | 图 413dc7fd72ca / 第 1 页 / 右下 P3 Atom-4Pin，pins 1~4 为 G21/G25/5V/GND |
| JP1~JP5 | Test pads | 3.3V、GND、SWCLK、SWDIO 与 RESET 测试/调试点 | 图 413dc7fd72ca / 第 1 页 / 左中 JP1 +3.3V、JP2 GND、JP3 SWC、JP4 SWD、JP5 RESET |
| R14 | 120Ω/NC | RS485_A 与 RS485_B 之间的可选终端电阻位 | 图 413dc7fd72ca / 第 1 页 / 下部 R14 120Ω/NC 跨接 RS485_B 与 RS485_A |
| R1/R2/R3 | 0Ω | 页面右上 470/868/915 配置表中的频段选择电阻位，连线与实装待确认 | 图 413dc7fd72ca / 第 1 页 / 右上 R1 0Ω-470、R2 0Ω-868、R3 0Ω-915 表格 |

## 系统结构

### Atom DTU LoRaWAN915

电路由 M1 Ra-07/Ra-07H 无线模组、U1 MP1584EN 5V 电源、U2 SP3485EN-L/TR RS485、Atom 4/5 Pin、I2C Grove、SMA 天线与调试测试点组成。

- 参数与网络：`radio=M1 Ra-07/Ra-07H`；`power=U1 MP1584EN`；`rs485=U2 SP3485EN-L/TR`；`host=P2 Atom-5Pin,P3 Atom-4Pin`；`antenna=E1 ANT_SMA-KWE`；`grove=J1 HY-2.0_IIC`
- 证据：图 413dc7fd72ca / 第 1 页 / 整页 U1/M1/U2/P1/P2/P3/J1/E1/JP1~JP5 功能块及同名网络

## 核心器件

### M1 Ra-07/Ra-07H 已用引脚

M1 VCC pin 9 接 +3.3V，URX pin 10 接 URXD，UTX pin 11 接 UTXD，RES pin 16 接 RESET，ANT pin 18 经 R8 0Ω 接 SMA，SWCLK/SWDIO pins 7/8 接 SWC/SWD，GND pins 1/17 接地。

- 参数与网络：`vcc=pin 9 +3.3V`；`uart_rx=pin 10 URX URXD`；`uart_tx=pin 11 UTX UTXD`；`reset=pin 16 RES RESET`；`antenna=pin 18 ANT`；`swclk=pin 7 SWCLK SWC`；`swdio=pin 8 SWDIO SWD`；`ground=pins 1,17`
- 证据：图 413dc7fd72ca / 第 1 页 / 页面中央 M1 Ra-07/Ra-07H pins 1~18 的已连接网络

## 电源

### +VIN 到 +5V

P1 12V+ 连接 +VIN，+VIN 经 F1 1.5A/24V 到 U1 VIN pin 7；输入节点由 D2 SS54 与 C2 10uF 接地，U1 SW pin 1 经 L1 10uH 输出 +5V，D1 SS54 接在 SW 节点与 GND 之间。

- 参数与网络：`terminal=P1 12V+`；`input=+VIN`；`fuse=F1 1.5A/24V`；`input_diode=D2 SS54 to GND`；`input_cap=C2 10uF`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`output=+5V`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 +VIN-F1-D2-C2-U1-D1-L1-C3/C4/C5-+5V

### MP1584EN 反馈与补偿

U1 FB pin 4 接 R4 51KΩ 与 R5 10KΩ 分压点，FREQ pin 6 经 R6 100KΩ 接地，COMP pin 3 经 C6 150pF 与 R7 100KΩ 串联接地，EN pin 2 标为未连接。

- 参数与网络：`feedback=R4 51KΩ,R5 10KΩ`；`frequency=R6 100KΩ`；`compensation=C6 150pF,R7 100KΩ`；`enable=U1 pin 2 no-connect`；`output_caps=C3/C4/C5 22uF`
- 证据：图 413dc7fd72ca / 第 1 页 / 左上 U1 FB/FREQ/COMP/EN 与 R4/R5/R6/C6/R7/C3~C5

### 无线模组 +3.3V 电源域

P2 Atom-5Pin pin 1 引入 +3.3V，连接 M1 VCC pin 9、U2 VCC pin 8、RS485 方向控制与偏置电阻；M1 电源去耦为 C7 100nF、C8 10uF、C9 33pF，另有 C12 100uF 接在 +3.3V 与 GND 之间。

- 参数与网络：`source=P2 pin 1 +3.3V`；`radio=M1 pin 9 VCC`；`rs485=U2 pin 8 VCC`；`radio_decoupling=C7 100nF,C8 10uF,C9 33pF`；`bulk_cap=C12 100uF`
- 证据：图 413dc7fd72ca / 第 1 页 / 中央 M1 pin 9 与 C7/C8/C9、左下 U2 pin 8、右下 P2 pin 1 与 C12 的 +3.3V 网络

## 接口

### P2 Atom-5Pin

P2 pins 1~5 依次为 +3.3V、G22/URXD、G19/UTXD、G23/TX、G33/RX。

- 参数与网络：`pin_1=+3.3V`；`pin_2=G22 URXD`；`pin_3=G19 UTXD`；`pin_4=G23 TX`；`pin_5=G33 RX`
- 证据：图 413dc7fd72ca / 第 1 页 / 右下 P2 Atom-5Pin pins 1~5 与 URXD/UTXD/TX/RX

### P3 Atom-4Pin 到 J1 I2C

P3 pins 1~4 的 G21、G25、+5V、GND 分别连接 J1 pins 1~4 的 IIC_SCL、IIC_SDA、VCC、GND；C10 100nF 接在 +5V 与 GND 之间。

- 参数与网络：`scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C10 100nF`
- 证据：图 413dc7fd72ca / 第 1 页 / 右中 J1 HY-2.0_IIC 与右下 P3 Atom-4Pin 的 G21/G25/+5V/GND

### SP3485EN RS485 A/B

U2 B pin 7 连接 RS485_B 并由 R11 4.7KΩ 接 GND，A pin 6 连接 RS485_A 并由 R16 4.7KΩ 接 +3.3V；R14 标为 120Ω/NC 并跨接 A/B。

- 参数与网络：`B=U2 pin 7-RS485_B-R11 4.7KΩ-GND`；`A=U2 pin 6-RS485_A-R16 4.7KΩ-+3.3V`；`termination=R14 120Ω/NC across A/B`
- 证据：图 413dc7fd72ca / 第 1 页 / 下部 U2 pins 7/6、R11/R16/R14 与 RS485_B/RS485_A

### P1 HDR_4P

P1 的 B、A、12V+、12V- 分别连接 RS485_B、RS485_A、+VIN 与 GND。

- 参数与网络：`B=RS485_B`；`A=RS485_A`；`12V_plus=+VIN`；`12V_minus=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 右中 P1 HDR_4P 的 B/A/12V+/12V- 与左侧网络

## 总线

### Atom 到 Ra-07/Ra-07H UART

Atom G22 的 URXD 经 R10 22Ω 连接 M1 URX pin 10，Atom G19 的 UTXD 经 R9 22Ω 连接 M1 UTX pin 11。

- 参数与网络：`module_rx=P2 pin 2 G22-URXD-R10 22Ω-M1 pin 10 URX`；`module_tx=P2 pin 3 G19-UTXD-R9 22Ω-M1 pin 11 UTX`
- 证据：图 413dc7fd72ca / 第 1 页 / M1 pins 10/11-R10/R9-URXD/UTXD 与右下 P2 G22/G19

### Atom 到 SP3485EN 自动方向控制

U2 RO pin 1 经 R12 1KΩ 到 RX；TX 经 R15 1KΩ 驱动 Q1 基极，Q1 集电极连接 U2 nRE/DE pins 2/3 并由 R13 4.7KΩ 上拉到 +3.3V，U2 DI pin 4 接 GND。

- 参数与网络：`receive=U2 pin 1 RO-R12 1KΩ-RX-P2 pin 5 G33`；`direction_drive=P2 pin 4 G23-TX-R15 1KΩ-Q1 base`；`direction_node=Q1 collector-U2 pins 2/3-R13 4.7KΩ to +3.3V`；`driver_input=U2 pin 4 DI to GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 左下 U2/R12/R13/R15/Q1 的 RX/TX/nRE/DE/DI 与右下 P2 G33/G23

## 保护电路

### RS485 A/B 保护

D3 SP4021-01FTG-C 连接 RS485_B 与 GND，D5 同型号连接 RS485_A 与 GND，D4 同型号跨接 RS485_B 与 RS485_A。

- 参数与网络：`B_to_ground=D3 SP4021-01FTG-C`；`A_to_ground=D5 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C`
- 证据：图 413dc7fd72ca / 第 1 页 / 下部 D3/D4/D5 围绕 RS485_B/RS485_A 的三器件保护网络

## 射频

### Ra-07/Ra-07H 到 SMA

M1 ANT pin 18 经 R8 0Ω 连接 E1 ANT_SMA-KWE 中心端，E1 的四个外壳端接 GND。

- 参数与网络：`radio_pin=M1 pin 18 ANT`；`series=R8 0Ω`；`connector=E1 ANT_SMA-KWE`；`shield=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 中央 M1 pin 18 ANT-R8 0Ω-E1 ANT_SMA-KWE 与外壳 GND

## 调试与烧录

### 无线模组调试测试点

JP1、JP2、JP3、JP4、JP5 分别引出 +3.3V、GND、SWC、SWD、RESET；SWC/SWD/RESET 分别连接 M1 SWCLK pin 7、SWDIO pin 8、RES pin 16。

- 参数与网络：`power=JP1 +3.3V`；`ground=JP2 GND`；`swclk=JP3 SWC-M1 pin 7`；`swdio=JP4 SWD-M1 pin 8`；`reset=JP5 RESET-M1 pin 16`
- 证据：图 413dc7fd72ca / 第 1 页 / 左中 JP1~JP5 与中央 M1 SWCLK/SWDIO/RES 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU LoRaWAN915 | `radio=M1 Ra-07/Ra-07H`；`power=U1 MP1584EN`；`rs485=U2 SP3485EN-L/TR`；`host=P2 Atom-5Pin,P3 Atom-4Pin`；`antenna=E1 ANT_SMA-KWE`；`grove=J1 HY-2.0_IIC` |
| 电源 | +VIN 到 +5V | `terminal=P1 12V+`；`input=+VIN`；`fuse=F1 1.5A/24V`；`input_diode=D2 SS54 to GND`；`input_cap=C2 10uF`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`output=+5V` |
| 电源 | MP1584EN 反馈与补偿 | `feedback=R4 51KΩ,R5 10KΩ`；`frequency=R6 100KΩ`；`compensation=C6 150pF,R7 100KΩ`；`enable=U1 pin 2 no-connect`；`output_caps=C3/C4/C5 22uF` |
| 电源 | 无线模组 +3.3V 电源域 | `source=P2 pin 1 +3.3V`；`radio=M1 pin 9 VCC`；`rs485=U2 pin 8 VCC`；`radio_decoupling=C7 100nF,C8 10uF,C9 33pF`；`bulk_cap=C12 100uF` |
| 核心器件 | M1 Ra-07/Ra-07H 已用引脚 | `vcc=pin 9 +3.3V`；`uart_rx=pin 10 URX URXD`；`uart_tx=pin 11 UTX UTXD`；`reset=pin 16 RES RESET`；`antenna=pin 18 ANT`；`swclk=pin 7 SWCLK SWC`；`swdio=pin 8 SWDIO SWD`；`ground=pins 1,17` |
| 接口 | P2 Atom-5Pin | `pin_1=+3.3V`；`pin_2=G22 URXD`；`pin_3=G19 UTXD`；`pin_4=G23 TX`；`pin_5=G33 RX` |
| 总线 | Atom 到 Ra-07/Ra-07H UART | `module_rx=P2 pin 2 G22-URXD-R10 22Ω-M1 pin 10 URX`；`module_tx=P2 pin 3 G19-UTXD-R9 22Ω-M1 pin 11 UTX` |
| 调试与烧录 | 无线模组调试测试点 | `power=JP1 +3.3V`；`ground=JP2 GND`；`swclk=JP3 SWC-M1 pin 7`；`swdio=JP4 SWD-M1 pin 8`；`reset=JP5 RESET-M1 pin 16` |
| 射频 | Ra-07/Ra-07H 到 SMA | `radio_pin=M1 pin 18 ANT`；`series=R8 0Ω`；`connector=E1 ANT_SMA-KWE`；`shield=GND` |
| 接口 | P3 Atom-4Pin 到 J1 I2C | `scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C10 100nF` |
| 总线 | Atom 到 SP3485EN 自动方向控制 | `receive=U2 pin 1 RO-R12 1KΩ-RX-P2 pin 5 G33`；`direction_drive=P2 pin 4 G23-TX-R15 1KΩ-Q1 base`；`direction_node=Q1 collector-U2 pins 2/3-R13 4.7KΩ to +3.3V`；`driver_input=U2 pin 4 DI to GND` |
| 接口 | SP3485EN RS485 A/B | `B=U2 pin 7-RS485_B-R11 4.7KΩ-GND`；`A=U2 pin 6-RS485_A-R16 4.7KΩ-+3.3V`；`termination=R14 120Ω/NC across A/B` |
| 保护电路 | RS485 A/B 保护 | `B_to_ground=D3 SP4021-01FTG-C`；`A_to_ground=D5 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C` |
| 接口 | P1 HDR_4P | `B=RS485_B`；`A=RS485_A`；`12V_plus=+VIN`；`12V_minus=GND` |
| 射频 | 470/868/915 配置表 | `470=R1 0Ω`；`868=R2 0Ω`；`915=R3 0Ω`；`selected_population=null`；`product_region=US915` |

## 待确认事项

- `rf.region-resistor-table`：页面右上表格将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915，但表格没有显示三个电阻的电气连接或实际装配状态，无法仅凭此页确认 LoRaWAN915 版本是否装配 R3。（证据：图 413dc7fd72ca / 第 1 页 / 右上 R1/R2/R3 0Ω 与 470/868/915 的独立表格，无外接网络）
- `review.us915-region-resistor`：请用 K061 的 BOM、PCB 或装配图确认 R3 0Ω 是否为 US915 版本的实际装配位，并确认 R1/R2/R3 所连接的频段配置网络。；原因：原理图只给出 R1/R2/R3 与 470/868/915 的对照表，没有绘制电气连接或装配标记，不能从表格单独证明 R3 已实装。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `413dc7fd72cad70452238a33b69a91afd73bdebe5f386c378c1ecc754444247f` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan915/atom_dtu_lorawan915_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_dtu_lorawan915.md`

源文档 SHA-256：`637935afdd2d5f449cd260ebc37caca6ed4cbe4398410cdae923548a12f6f4bc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
