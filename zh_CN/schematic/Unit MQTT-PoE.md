# Unit MQTT-PoE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit MQTT-PoE |
| SKU | U129-B |
| 产品 ID | `unit-mqtt-poe-9ff834605eee` |
| 源文档 | `zh_CN/unit/mqtt_poe.md` |

## 概述

Unit MQTT-PoE（U129-B）原理图由 M1 MQTT_TCP03 以太网/UART 模组、U1 HBJ-6308ANLF 磁性 RJ45、M2 WC-PD06H050A PoE 电源模组和 J1 HY-2.0_UART 组成。RJ45 的差分对通过端接网络连接 M1，PoE 中心抽头经 P1/P2 板间接口送入 M2，M2 的 +5V 输出经 F1 后为系统和 J1 供电，再由 VR1 AMS1117-3.3 生成 3V3。M1 的 TXD/RXD、RST、CFG 通过 P1/P2 引出，其中 TXD_1/RXD_1 接 J1 RX/TX。原理图未展开 M1 内部芯片，也未标注 PoE 输入额定范围、UART/MQTT 参数或以太网速率。

## 检索关键词

`Unit MQTT-PoE`、`U129-B`、`MQTT-PoE`、`MQTT_TCP03`、`M1`、`HBJ-6308ANLF`、`U1`、`WC-PD06H050A`、`M2`、`AMS1117-3.3`、`VR1`、`HY-2.0_UART`、`J1`、`Header 5X2`、`P1`、`P2`、`PoE`、`Ethernet`、`RJ45`、`TXP`、`TXN`、`RXP`、`RXN`、`LINKLED`、`ACTLED`、`TXD`、`RXD`、`RST`、`CFG`、`VC+`、`VC-`、`VC2+`、`VC2-`、`+5V`、`3V3`、`F1 Fuse`、`R1 10Ω`、`49.9Ω PHY termination`、`C1 C2 6.8nF`、`C3 1nF 2000V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | MQTT_TCP03 | 以太网到 UART 功能模组，连接 PHY 差分对、链路/活动 LED、RST、TXD、RXD 和 CFG | 图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 MQTT_TCP03，pins 1~12 标注 TX-N/TX-P/RX-N/RX-P/LED_LINK/LED_ACT/CFG/RXD/TXD/RST/GND/3.3V |
| U1 | HBJ-6308ANLF | 带磁性器件与 LINK/ACT LED 的 RJ45 以太网连接器，并引出四路 PoE 中心抽头 | 图 c6b5d0bf3819 / 第 1 页 / 页面左中 U1 HBJ-6308ANLF，TD+/TD-/RD+/RD-、VC+/VC-/VC2+/VC2-、Y+/Y-/G+/G- |
| M2 | WC-PD06H050A | PoE 受电电源模组，从 VA1/VA2/VB1/VB2 输入侧产生 +5V 与 GND | 图 c6b5d0bf3819 / 第 1 页 / 页面下中 M2 WC-PD06H050A，pins 1~4 VA1/VA2/VB1/VB2，pin 5 GND，pin 6 +5V |
| VR1 | AMS1117-3.3 | 把 +5V 稳压为 3V3，供 M1 与以太网端接/LED 网络使用 | 图 c6b5d0bf3819 / 第 1 页 / 页面左上 VR1 AMS1117-3.3，Vin +5V、Vout 3V3、GND |
| J1 | HY-2.0_UART | 四针 UART 与 +5V 电源接口 | 图 c6b5d0bf3819 / 第 1 页 / 页面右下 J1 HY-2.0_UART，pin 1 RX/TXD_1、pin 2 TX/RXD_1、pin 3 VCC/+5V、pin 4 GND |
| P1 | Header 5X2 排针 | M1/RJ45 子板的十针板间接口，承载 PoE 抽头、+5V、CFG/RXD/TXD/RST 和 GND | 图 c6b5d0bf3819 / 第 1 页 / 页面右上 P1 Header 5X2 排针，odd pins VC-/VC+/VC2-/VC2+/+5V，even pins CFG/RXD/TXD/RST/GND |
| P2 | Header 5X2 排母 | PoE/J1 子板的十针板间接口，承载 +5V、PoE 抽头与带 _1 后缀的 UART/控制网络 | 图 c6b5d0bf3819 / 第 1 页 / 页面右中 P2 Header 5X2 排母，odd pins +5V/VC2+/VC2-/VC+/VC-，even pins GND/RST_1/TXD_1/RXD_1/CFG_1 |
| F1 | Fuse | 串联在 M2 pin 6 与系统 +5V 电源轨之间的保险丝 | 图 c6b5d0bf3819 / 第 1 页 / 页面下中 M2 pin 6 +5V-F1 Fuse-+5V |
| R1 | 10Ω | 从 3V3 向 TX 差分端接公共节点供电的串联电阻 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 上方 3V3-R1 10Ω-R2/R3 公共节点 |
| R2/R3 | 49.9Ω | TXP/TXN 差分线的偏置/端接电阻 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 与 M1 之间 R2/R3 49.9Ω 分别连接 TXP/TXN |
| R4/R5 | 1KΩ | U1 LINK/ACT LED 从 3V3 供电的限流电阻 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 左侧 R4/R5 1KΩ 从 3V3 接 U1 Y+/G+，Y-/G- 接 LINKLED/ACTLED |
| R6/R7 | 49.9Ω | RXP/RXN 差分线到 C5 公共节点的端接电阻 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 右下 R6/R7 49.9Ω 分别从 RXP/RXN 接到 C5 10nF 公共节点 |
| C1/C2 | 6.8nF | U1 RD+/RD- 与 M1 RXP/RXN 之间的串联电容 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 右侧 C1/C2 6.8nF 串联在 RD+/RD- 到 RXP/RXN 路径 |
| C3 | 1nF (102) 10% 2000V | U1 pins 15/16 公共节点到 GND 的高压额定电容 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 左下 pins 15/16 公共节点-C3 1nF (102) 10% 2000V-GND |
| C4/C5 | 22nF/10nF | PHY 模拟网络的接地电容 | 图 c6b5d0bf3819 / 第 1 页 / 页面 U1 下方 C4 22nF 与 R6/R7 公共节点下方 C5 10nF，均接 GND |
| C6/C7/C8/C9 | 100nF/22uF/22uF/100nF | AMS1117-3.3 输入 +5V 与输出 3V3 的去耦/储能电容组 | 图 c6b5d0bf3819 / 第 1 页 / 页面左上 +5V 侧 C6 100nF/C7 22uF，3V3 侧 C8 22uF/C9 100nF |

## 系统结构

### Unit MQTT-PoE 系统架构

M1 MQTT_TCP03 通过 TXP/TXN/RXP/RXN 连接 U1 HBJ-6308ANLF RJ45，并通过 TXD/RXD 连接 J1 UART；U1 的 VC+/VC-/VC2+/VC2- 经 P1/P2 接入 M2 WC-PD06H050A，M2 输出 +5V，经 VR1 生成 3V3。

- 参数与网络：`ethernet_module=M1 MQTT_TCP03`；`rj45=U1 HBJ-6308ANLF`；`poe_module=M2 WC-PD06H050A`；`uart=J1 HY-2.0_UART`；`power=M2 +5V -> F1 -> +5V -> VR1 -> 3V3`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 整页 U1/M1/M2/VR1/P1/P2/J1 与同名网络

## 核心器件

### M1 MQTT_TCP03 引脚

M1 pins 1~6 依次为 TX-N、TX-P、RX-N、RX-P、LED_LINK、LED_ACT；pins 7~12 依次为 CFG、RXD、TXD、RST、GND、3.3V。

- 参数与网络：`pin_1=TX-N TXN`；`pin_2=TX-P TXP`；`pin_3=RX-N RXN`；`pin_4=RX-P RXP`；`pin_5=LED_LINK LINKLED`；`pin_6=LED_ACT ACTLED`；`pin_7=CFG`；`pin_8=RXD`；`pin_9=TXD`；`pin_10=RST`；`pin_11=GND`；`pin_12=3V3`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 MQTT_TCP03 pins 1~12 与网络文字

## 电源

### PoE 中心抽头输入

U1 的 VC-、VC+、VC2-、VC2+ 网络引到 P1；M2 的 VA1、VA2、VB1、VB2 分别连接 P2 侧的 VC-_1、VC+_1、VC2-_1、VC2+_1。

- 参数与网络：`rj45_taps=VC-,VC+,VC2-,VC2+`；`p1=pins 1,3,5,7`；`m2_inputs=pin1 VA1 VC-_1,pin2 VA2 VC+_1,pin3 VB1 VC2-_1,pin4 VB2 VC2+_1`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面 U1 VC/VC2 网络、右上 P1 与下中 M2/P2 对应网络

### M2 +5V 输出与保险丝

M2 pin 5 接 GND，pin 6 的 +5V 输出经 F1 Fuse 串联后进入系统 +5V 电源轨。

- 参数与网络：`module=M2 WC-PD06H050A`；`ground=pin 5 GND`；`output=pin 6 +5V`；`series_protection=F1 Fuse`；`rail=+5V`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面下中 M2 pins 5/6、F1 与 +5V 网络

### +5V 到 3V3 稳压

VR1 AMS1117-3.3 的 Vin 接 +5V、Vout 输出 3V3、GND 接地；M1 pin 12 由 3V3 供电。

- 参数与网络：`input=+5V`；`regulator=VR1 AMS1117-3.3`；`output=3V3`；`load=M1 pin 12`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面左上 VR1 +5V/3V3 与中央 M1 pin 12 3.3V

### VR1 输入输出电容

+5V 输入侧 C6 100nF 与 C7 22uF 对地，3V3 输出侧 C8 22uF 与 C9 100nF 对地。

- 参数与网络：`input_caps=C6 100nF,C7 22uF`；`output_caps=C8 22uF,C9 100nF`；`return=GND`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面左上 VR1 两侧 C6/C7/C8/C9

## 接口

### U1 RJ45 以太网接口

U1 HBJ-6308ANLF 引出 TD+/TD-、RD+/RD- 差分端、VC+/VC-/VC2+/VC2- PoE 中心抽头，以及 Y+/Y-/G+/G- 两组状态 LED 端。

- 参数与网络：`tx_pair=TD+ pin 1,TD- pin 3`；`rx_pair=RD+ pin 4,RD- pin 6`；`poe_taps=VC+ pin 9,VC- pin 10,VC2+ pin 7,VC2- pin 8`；`led_pins=Y- pin12,Y+ pin11,G- pin14,G+ pin13`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面左中 U1 HBJ-6308ANLF 全部标注引脚

### 以太网 LINK/ACT LED

M1 LINKLED 连接 U1 Y- pin 12，M1 ACTLED 连接 U1 G- pin 14；U1 Y+ pin 11 和 G+ pin 13 分别经 R4/R5 1KΩ 接 3V3。

- 参数与网络：`link=M1 pin 5 LINKLED -> U1 pin 12 Y-, U1 pin 11 Y+ -> R4 1KΩ -> 3V3`；`activity=M1 pin 6 ACTLED -> U1 pin 14 G-, U1 pin 13 G+ -> R5 1KΩ -> 3V3`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面 U1 左侧 Y-/Y+/G-/G+、LINKLED/ACTLED、R4/R5 1KΩ

### J1 HY-2.0_UART 针脚

J1 pins 1~4 依次为 RX、TX、VCC、GND，对应网络为 TXD_1、RXD_1、+5V、GND。

- 参数与网络：`pin_1=RX-TXD_1，模块到主机`；`pin_2=TX-RXD_1，主机到模块`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面右下 J1 HY-2.0_UART pins 1~4 与 TXD_1/RXD_1/+5V/GND

### P1 Header 5X2 排针

P1 odd pins 1/3/5/7/9 依次为 VC-/VC+/VC2-/VC2+/+5V，even pins 2/4/6/8/10 依次为 CFG/RXD/TXD/RST/GND。

- 参数与网络：`pin_1=VC-`；`pin_2=CFG`；`pin_3=VC+`；`pin_4=RXD`；`pin_5=VC2-`；`pin_6=TXD`；`pin_7=VC2+`；`pin_8=RST`；`pin_9=+5V`；`pin_10=GND`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面右上 P1 Header 5X2 排针 pins 1~10 与网络标签

### P2 Header 5X2 排母

P2 odd pins 1/3/5/7/9 依次为 +5V/VC2+_1/VC2-_1/VC+_1/VC-_1，even pins 2/4/6/8/10 依次为 GND/RST_1/TXD_1/RXD_1/CFG_1。

- 参数与网络：`pin_1=+5V`；`pin_2=GND`；`pin_3=VC2+_1`；`pin_4=RST_1`；`pin_5=VC2-_1`；`pin_6=TXD_1`；`pin_7=VC+_1`；`pin_8=RXD_1`；`pin_9=VC-_1`；`pin_10=CFG_1`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面右中 P2 Header 5X2 排母 pins 1~10 与网络标签

## 总线

### M1 UART

M1 pin 9 TXD 与 pin 8 RXD 引到 P1；P2 侧 TXD_1/RXD_1 分别连接 J1 pin 1 RX 与 pin 2 TX，原理图未显示电平转换器。

- 参数与网络：`module_tx=M1 pin 9 TXD -> P1 pin 6`；`module_rx=M1 pin 8 RXD -> P1 pin 4`；`external_tx_path=P2 pin 6 TXD_1 -> J1 pin 1 RX`；`external_rx_path=P2 pin 8 RXD_1 -> J1 pin 2 TX`；`level_shifter=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 TXD/RXD、右侧 P1/P2 TXD/RXD 网络及 J1

### 其他总线

本页对外控制接口仅显示 UART、RST 和 CFG，未显示 I2C、SPI、CAN、RS-485、USB、SDIO、MIPI 或 I2S 控制总线。

- 参数与网络：`uart=TXD/RXD`；`control=RST,CFG`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 整页 M1/P1/P2/J1 控制网络仅 TXD/RXD/RST/CFG

## GPIO 与控制信号

### M1 CFG 配置网络

M1 pin 7 CFG 连接 P1 pin 2；P2 pin 10 引出 CFG_1。本页未显示 CFG 的上拉、下拉、开关或有效电平。

- 参数与网络：`module_pin=M1 pin 7 CFG`；`p1=pin 2 CFG`；`p2=pin 10 CFG_1`；`pull=null`；`switch=null`；`active_level=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 CFG、右上 P1 CFG、右中 P2 CFG_1，整页无 CFG 外围器件

## 时钟

### 时钟连接

本页未显示独立晶振、谐振器或外部 CLK 网络，M1 内部时钟实现未在模块符号中展开。

- 参数与网络：`external_crystal=null`；`external_clock=null`；`module_internal_clock=not expanded`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 整页 M1 模块符号及外围网络，无 XTAL/CLK 器件或网络

## 复位

### M1 RST 网络

M1 pin 10 RST 连接 P1 pin 8；P2 pin 4 引出 RST_1。本页未显示 RST 上拉、RC 延时、按钮或复位监控器。

- 参数与网络：`module_pin=M1 pin 10 RST`；`p1=pin 8 RST`；`p2=pin 4 RST_1`；`pull=null`；`rc=null`；`switch=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 RST、右上 P1 RST、右中 P2 RST_1，整页无 RST 外围器件

## 保护电路

### +5V 保险丝保护

F1 Fuse 是原理图中明确显示的串联保护器件，位于 M2 +5V 输出与系统 +5V 轨之间；页面未标注其型号、额定电流或可恢复类型。

- 参数与网络：`reference=F1`；`path=M2 pin 6 +5V -> F1 -> +5V rail`；`part_number=null`；`current_rating=null`；`resettable=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面下中 F1 标注 Fuse，串联在 M2 pin 6 与 +5V 标签之间

### 接口保护覆盖

除 F1 外，本页未显示 UART 或以太网差分线上独立的 TVS/ESD 器件，也未显示 +5V 反接或过压钳位器件。

- 参数与网络：`fuse=F1`；`uart_tvs=null`；`ethernet_tvs=null`；`reverse_polarity=null`；`overvoltage_clamp=null`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 整页 J1、U1-M1 差分路径与 +5V 路径，无 TVS/ESD/反接器件符号

## 存储

### 外部存储器

本页未显示独立 Flash、EEPROM、SD 卡或其他存储器，M1 内部存储实现未展开。

- 参数与网络：`flash=null`；`eeprom=null`；`sd=null`；`module_internal_storage=not expanded`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 整页元件清单无独立存储器件，M1 仅以模块符号表示

## 模拟电路

### M1 到 U1 的 PHY 差分网络

M1 TXP/TXN 连接 U1 TD+/TD-，并由 R2/R3 49.9Ω 接至经 R1 10Ω 供电的 3V3 公共节点；U1 RD+/RD- 经 C1/C2 6.8nF 串联到 M1 RXP/RXN，R6/R7 49.9Ω 接至 C5 10nF 对地公共节点。

- 参数与网络：`tx=M1 TXP/TXN -> U1 TD+/TD-`；`tx_termination=R2/R3 49.9Ω, R1 10Ω to 3V3`；`rx=U1 RD+/RD- -> C1/C2 6.8nF -> M1 RXP/RXN`；`rx_termination=R6/R7 49.9Ω -> C5 10nF -> GND`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面 U1 与 M1 间 TXP/TXN/RXP/RXN、R1-R3/R6-R7、C1/C2/C5

### U1 pins 15/16 对地电容

U1 pins 15 和 16 共节点通过 C3 1nF（102）、10%、2000V 电容接 GND。

- 参数与网络：`connector_pins=U1 pins 15,16`；`capacitor=C3 1nF (102) 10% 2000V`；`return=GND`
- 证据：图 c6b5d0bf3819 / 第 1 页 / 页面 U1 左下 pins 15/16-C3-GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit MQTT-PoE 系统架构 | `ethernet_module=M1 MQTT_TCP03`；`rj45=U1 HBJ-6308ANLF`；`poe_module=M2 WC-PD06H050A`；`uart=J1 HY-2.0_UART`；`power=M2 +5V -> F1 -> +5V -> VR1 -> 3V3` |
| 核心器件 | M1 MQTT_TCP03 引脚 | `pin_1=TX-N TXN`；`pin_2=TX-P TXP`；`pin_3=RX-N RXN`；`pin_4=RX-P RXP`；`pin_5=LED_LINK LINKLED`；`pin_6=LED_ACT ACTLED`；`pin_7=CFG`；`pin_8=RXD`；`pin_9=TXD`；`pin_10=RST`；`pin_11=GND`；`pin_12=3V3` |
| 接口 | U1 RJ45 以太网接口 | `tx_pair=TD+ pin 1,TD- pin 3`；`rx_pair=RD+ pin 4,RD- pin 6`；`poe_taps=VC+ pin 9,VC- pin 10,VC2+ pin 7,VC2- pin 8`；`led_pins=Y- pin12,Y+ pin11,G- pin14,G+ pin13` |
| 模拟电路 | M1 到 U1 的 PHY 差分网络 | `tx=M1 TXP/TXN -> U1 TD+/TD-`；`tx_termination=R2/R3 49.9Ω, R1 10Ω to 3V3`；`rx=U1 RD+/RD- -> C1/C2 6.8nF -> M1 RXP/RXN`；`rx_termination=R6/R7 49.9Ω -> C5 10nF -> GND` |
| 接口 | 以太网 LINK/ACT LED | `link=M1 pin 5 LINKLED -> U1 pin 12 Y-, U1 pin 11 Y+ -> R4 1KΩ -> 3V3`；`activity=M1 pin 6 ACTLED -> U1 pin 14 G-, U1 pin 13 G+ -> R5 1KΩ -> 3V3` |
| 电源 | PoE 中心抽头输入 | `rj45_taps=VC-,VC+,VC2-,VC2+`；`p1=pins 1,3,5,7`；`m2_inputs=pin1 VA1 VC-_1,pin2 VA2 VC+_1,pin3 VB1 VC2-_1,pin4 VB2 VC2+_1` |
| 电源 | M2 +5V 输出与保险丝 | `module=M2 WC-PD06H050A`；`ground=pin 5 GND`；`output=pin 6 +5V`；`series_protection=F1 Fuse`；`rail=+5V` |
| 电源 | +5V 到 3V3 稳压 | `input=+5V`；`regulator=VR1 AMS1117-3.3`；`output=3V3`；`load=M1 pin 12` |
| 电源 | VR1 输入输出电容 | `input_caps=C6 100nF,C7 22uF`；`output_caps=C8 22uF,C9 100nF`；`return=GND` |
| 接口 | J1 HY-2.0_UART 针脚 | `pin_1=RX-TXD_1，模块到主机`；`pin_2=TX-RXD_1，主机到模块`；`pin_3=VCC +5V`；`pin_4=GND` |
| 总线 | M1 UART | `module_tx=M1 pin 9 TXD -> P1 pin 6`；`module_rx=M1 pin 8 RXD -> P1 pin 4`；`external_tx_path=P2 pin 6 TXD_1 -> J1 pin 1 RX`；`external_rx_path=P2 pin 8 RXD_1 -> J1 pin 2 TX`；`level_shifter=null` |
| 接口 | P1 Header 5X2 排针 | `pin_1=VC-`；`pin_2=CFG`；`pin_3=VC+`；`pin_4=RXD`；`pin_5=VC2-`；`pin_6=TXD`；`pin_7=VC2+`；`pin_8=RST`；`pin_9=+5V`；`pin_10=GND` |
| 接口 | P2 Header 5X2 排母 | `pin_1=+5V`；`pin_2=GND`；`pin_3=VC2+_1`；`pin_4=RST_1`；`pin_5=VC2-_1`；`pin_6=TXD_1`；`pin_7=VC+_1`；`pin_8=RXD_1`；`pin_9=VC-_1`；`pin_10=CFG_1` |
| 复位 | M1 RST 网络 | `module_pin=M1 pin 10 RST`；`p1=pin 8 RST`；`p2=pin 4 RST_1`；`pull=null`；`rc=null`；`switch=null` |
| GPIO 与控制信号 | M1 CFG 配置网络 | `module_pin=M1 pin 7 CFG`；`p1=pin 2 CFG`；`p2=pin 10 CFG_1`；`pull=null`；`switch=null`；`active_level=null` |
| 保护电路 | +5V 保险丝保护 | `reference=F1`；`path=M2 pin 6 +5V -> F1 -> +5V rail`；`part_number=null`；`current_rating=null`；`resettable=null` |
| 保护电路 | 接口保护覆盖 | `fuse=F1`；`uart_tvs=null`；`ethernet_tvs=null`；`reverse_polarity=null`；`overvoltage_clamp=null` |
| 模拟电路 | U1 pins 15/16 对地电容 | `connector_pins=U1 pins 15,16`；`capacitor=C3 1nF (102) 10% 2000V`；`return=GND` |
| 时钟 | 时钟连接 | `external_crystal=null`；`external_clock=null`；`module_internal_clock=not expanded` |
| 存储 | 外部存储器 | `flash=null`；`eeprom=null`；`sd=null`；`module_internal_storage=not expanded` |
| 总线 | 其他总线 | `uart=TXD/RXD`；`control=RST,CFG`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 接口 | P1/P2 板间配接 | `proposed_pairs=P1 1-10 <-> P2 9,10,7,8,5,6,3,4,1,2 by matching net function`；`direct_schematic_connection=false`；`mechanical_orientation=null` |
| 核心器件 | M1 内部控制器与以太网芯片 | `module=MQTT_TCP03`；`mcu=null`；`ethernet_controller=null`；`memory=null` |
| 电源 | PoE 电气额定参数 | `module=WC-PD06H050A`；`output_label=+5V`；`input_voltage_range=null`；`output_current=null`；`output_power=null`；`efficiency=null`；`isolation_rating=null` |
| 总线 | UART、MQTT 与以太网参数 | `uart_baud=null`；`uart_format=null`；`at_version=null`；`mqtt_topics=null`；`mqtts=null`；`ethernet_speed=null` |

## 待确认事项

- `interface.board-mating-map`：P1 与 P2 的同功能网络呈反向针号排列，例如 +5V 为 P1 pin 9/P2 pin 1、VC- 为 P1 pin 1/P2 pin 9、CFG 为 P1 pin 2/P2 pin 10；但本页没有直接画出 P1 与 P2 的机械配接线，实际针脚配对需结构或 PCB 资料确认。（证据：图 c6b5d0bf3819 / 第 1 页 / 页面右侧 P1 排针与 P2 排母的反向网络排列，二者之间无绘制连线）
- `component.m1-internal-silicon`：原理图只标注 M1 为 MQTT_TCP03，未展开其内部 MCU、以太网控制器或存储器，因此无法仅凭本页确认 W5500、ARM Cortex-M3 或具体存储型号。（证据：图 c6b5d0bf3819 / 第 1 页 / 页面中央 M1 MQTT_TCP03 仅显示模块级 pins 1~12，无内部芯片展开）
- `power.poe-ratings`：M2 原理图符号确认输出网络为 +5V，但未标注 PoE 输入电压范围、+5V 输出电流/功率、效率或输入输出隔离等级。（证据：图 c6b5d0bf3819 / 第 1 页 / 页面下中 M2 WC-PD06H050A 仅标 VA/VB、GND、+5V 引脚，无额定参数文字）
- `bus.protocol-parameters`：原理图未标注 UART 波特率/帧格式、AT 指令版本、MQTT 功能或以太网 10/100M 速率；这些固件和协议参数不能由本页确定。（证据：图 c6b5d0bf3819 / 第 1 页 / 整页仅有 M1 型号、PHY/UART 网络和电源连接，无通信速率或协议参数）
- `review.board-mating-map`：P1 排针与 P2 排母的实际机械配接方向及逐针对应关系是什么？；原因：网络功能呈反向针号排列，但原理图没有画出两个连接器之间的直接连接或机械方向。
- `review.m1-internal-silicon`：MQTT_TCP03 模组内部 MCU、以太网控制器和存储器的准确型号是什么？；原因：本页仅给模块级符号，需 BOM、模组原理图或 datasheet 确认内部器件。
- `review.poe-ratings`：M2 的 PoE 输入范围、+5V 输出额定电流/功率和隔离等级分别是多少？；原因：原理图只显示 M2 型号和 +5V 输出网络，没有电气额定参数。
- `review.protocol-parameters`：该硬件/固件版本的 UART、AT、MQTT 和以太网速率参数是什么？；原因：这些参数属于固件/模组能力，当前原理图页未标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c6b5d0bf3819231167828c952b2d0f54cf5d31af185c6138bdf9a11a9dab5cc1` | `https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_sch_01.webp` |

---

源文档：`zh_CN/unit/mqtt_poe.md`

源文档 SHA-256：`90554c92edfc9395b9f509ca1de07ff908274e7e20150d7dd9e5d376503bb20b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
