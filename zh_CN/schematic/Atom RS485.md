# Atom RS485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom RS485 |
| SKU | K045 |
| 产品 ID | `atom-rs485-ab98568a0c94` |
| 源文档 | `zh_CN/atom/atomic485.md` |

## 概述

Atom RS485 使用 U1 SP3485EN-L/TR 在 Atom 的 RX/TX 与 RS485_A/RS485_B 之间转换，TX 经 Q1 SS8050 Y1 控制并联的 /RE 与 DE，DI 固定接 GND。A/B 总线配置 4.7KΩ 偏置、可选 120Ω 终端和三颗 SMAJ6.5CA-E3 保护器件，并通过 J1 与 12V+/12V- 一起接出。J1 的 +12V 由 U2 AOZ1282CI 降压为 +5VIN，为 Atom P2 提供电源。

## 检索关键词

`Atom RS485`、`K045`、`SP3485EN-L/TR`、`AOZ1282CI`、`SS8050 Y1`、`RS-485`、`RS485_A`、`RS485_B`、`RX`、`TX`、`RO`、`DI`、`RE`、`DE`、`auto direction`、`120Ω termination`、`R4 120R NC`、`4.7K bias`、`SMAJ6.5CA-E3`、`HDR_4P_3.96`、`12V+`、`12V-`、`+12V`、`+5VIN`、`+3.3V`、`B5819W SL`、`P1 Header 5`、`P2 Header 4`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SP3485EN-L/TR | 3.3V UART 与 RS485_A/RS485_B 之间的半双工收发器 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上 U1 SP3485EN-L/TR，RO,/RE,DE,DI,VCC,GND,A,B |
| Q1 | SS8050 Y1 | 根据 TX 电平下拉 SP3485 的 /RE 与 DE 公共控制节点 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页左上，TX-R5-Q1 与 R3、U1 /RE/DE 公共节点 |
| J1 | HDR_4P_3.96 | 接出 RS485_B、RS485_A、12V+ 和 12V- 的四针端子 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页右上 J1 HDR_4P_3.96，B/A/12V+/12V- 四行网络 |
| U2 | AOZ1282CI | 将 J1 的 +12V 降压为 +5VIN 的 DC-DC 转换器 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页左下 U2 AOZ1282CI 的 VIN/EN/GND、BST/LX/FB 与 +12V/+5VIN |
| P1,P2 | Header 5 / Header 4 | Atom 侧 +3.3V、RX、TX、+5VIN 和 GND 接口 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页右中，P1 Header 5 与 P2 Header 4 的网络和 no-connect 标记 |
| R1,R6,R4 | 4.7KΩ / 4.7KΩ / 120Ω NC | RS485 B/A 偏置和可选总线终端网络 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上，R1 从 B 到 GND、R6 从 A 到 +3.3V、R4 120R/NC 跨 B/A |
| D1,D2,D3 | SMAJ6.5CA-E3 | RS485_B 对地、B-A 线间和 RS485_A 对地的 TVS 保护 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上 D1/D2/D3 SMAJ6.5CA-E3 与 GND/RS485_B/RS485_A |
| R2,R3,R5,C1 | 1KΩ / 4.7KΩ / 1KΩ / 100nF | SP3485 接收输出、方向控制和 3.3V 去耦网络 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页左上，RO-R2-RX、TX-R5-Q1、R3 上拉与 C1 VCC 去耦 |
| D4,L1 | B5819W SL / 4.7uH | AOZ1282CI LX 节点的续流二极管和输出电感 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页下方，D4 B5819W SL 从 LX 节点到 GND，L1 4.7uH 从 LX 到 +5VIN |
| R7,R8,R9 | 100KΩ / 51KΩ / 10KΩ | AOZ1282CI EN 上拉和 +5VIN 反馈分压网络 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页左下，R7 从 +12V 到 EN，R8 从 +5VIN 到 FB，R9 从 FB 到 GND |
| C2,C3,C4,C5,C6 | 100nF / 10uF / 10uF / 10uF / 100nF | AOZ1282CI BST、自举、输入和输出去耦 | 图 72fa3f8f2f70 / 第 1 页 / 第 1 页左下，C2 BST-LX、C3/C4 +12V-GND、C5/C6 +5VIN-GND |

## 系统结构

### Atom RS485 通信与供电架构

Atom 的 RX/TX 连接 U1 SP3485EN-L/TR，U1 将信号转换为 RS485_A/RS485_B 并通过 J1 接出；J1 同时输入 +12V/GND，U2 AOZ1282CI 将 +12V 转换为 +5VIN 给 Atom。

- 参数与网络：`transceiver=U1 SP3485EN-L/TR`；`host_signals=RX, TX`；`bus_signals=RS485_A, RS485_B`；`terminal=J1 HDR_4P_3.96`；`dc_dc=U2 AOZ1282CI`；`power_path=+12V -> U2 -> +5VIN -> P2`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页完整单页原理图，上方收发器/端子/Atom 与下方 +12V-to-+5VIN 电源

## 电源

### AOZ1282CI +12V 输入与使能

U2 VIN pin5 接 +12V，EN pin4 通过 R7 100KΩ 接 +12V，GND pin2 接 GND；C3/C4 两个 10uF (106) 10% 35V 电容并联连接 +12V 与 GND。

- 参数与网络：`VIN=pin5 +12V`；`EN=pin4 through R7 100K to +12V`；`GND=pin2 GND`；`input_capacitors=C3/C4 10uF (106) 10% 35V`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页左下 +12V、U2 VIN/EN/GND、R7 与 C3/C4

### AOZ1282CI +5VIN 降压输出

U2 LX pin6 经 L1 4.7uH 输出 +5VIN，D4 B5819W SL 从 LX 节点接 GND，C2 100nF 连接 BST pin1 与 LX；C5 10uF 和 C6 100nF 连接 +5VIN 与 GND。

- 参数与网络：`LX=pin6`；`inductor=L1 4.7uH to +5VIN`；`freewheel_diode=D4 B5819W SL LX to GND`；`bootstrap=C2 100nF BST pin1 to LX`；`output_caps=C5 10uF, C6 100nF`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页下方 U2 BST/LX、C2/D4/L1 与 +5VIN/C5/C6

### AOZ1282CI 输出反馈

R8 51KΩ 从 +5VIN 接 U2 FB pin3，R9 10KΩ 从 FB pin3 接 GND。

- 参数与网络：`upper_resistor=R8 51K +5VIN to FB`；`lower_resistor=R9 10K FB to GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页左下 U2 FB pin3 与 R8/R9/+5VIN/GND

## 接口

### Atom 连接器映射

P1 Header 5 的 pin1=+3.3V、pin2=RX、pin3=TX，pin4/pin5 未连接；P2 Header 4 的 pin1/pin2 未连接、pin3=+5VIN、pin4=GND。

- 参数与网络：`P1=pin1 +3.3V, pin2 RX, pin3 TX, pin4 NC, pin5 NC`；`P2=pin1 NC, pin2 NC, pin3 +5VIN, pin4 GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页右中 P1/P2 针脚编号、网络与红色 no-connect 标记

### J1 RS-485 与 12V 端子

J1 HDR_4P_3.96 从上到下接 RS485_B、RS485_A、+12V 和 GND/12V-。

- 参数与网络：`B=RS485_B`；`A=RS485_A`；`12V+=+12V`；`12V-=GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页右上 J1 B/A/12V+/12V- 标签与 RS485_B/RS485_A/+12V/GND 网络

## 总线

### SP3485EN-L/TR UART 与 RS-485 映射

U1 RO pin1 经 R2 1KΩ 连接 RX，DI pin4 固定接 GND，B pin7 连接 RS485_B，A pin6 连接 RS485_A；VCC pin8 接 +3.3V，GND pin5 接 GND。

- 参数与网络：`RO=pin1 -> R2 1K -> RX`；`DI=pin4 GND`；`B=pin7 RS485_B`；`A=pin6 RS485_A`；`VCC=pin8 +3.3V`；`GND=pin5 GND`；`decoupling=C1 100nF`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上 U1 RO/DI/B/A/VCC/GND 与 R2/C1/RX/RS485_A/RS485_B

## GPIO 与控制信号

### TX 自动方向控制网络

U1 /RE pin2 与 DE pin3 并联，公共节点由 R3 4.7KΩ 上拉到 +3.3V，并连接 Q1 集电极；TX 经 R5 1KΩ 驱动 Q1 SS8050 Y1 基极，Q1 发射极接 GND。

- 参数与网络：`control_pins=/RE pin2 tied to DE pin3`；`pullup=R3 4.7K to +3.3V`；`transistor=Q1 SS8050 Y1`；`base_drive=TX through R5 1K`；`emitter=GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页左上 TX-R5-Q1-R3 与 U1 /RE/DE 公共节点

## 保护电路

### RS485 三路 TVS 保护

D1 SMAJ6.5CA-E3 连接 RS485_B 与 GND，D2 SMAJ6.5CA-E3 跨接 RS485_B 与 RS485_A，D3 SMAJ6.5CA-E3 连接 RS485_A 与 GND。

- 参数与网络：`B_to_GND=D1 SMAJ6.5CA-E3`；`B_to_A=D2 SMAJ6.5CA-E3`；`A_to_GND=D3 SMAJ6.5CA-E3`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上 D1/D2/D3 的垂直网络及 RS485_B/RS485_A/GND 节点

## 关键网络

### RS485 A/B 偏置与可选终端

R1 4.7KΩ 从 RS485_B 接 GND，R6 4.7KΩ 从 RS485_A 接 +3.3V；R4 120Ω/NC 跨接 RS485_B 与 RS485_A，因此 120Ω 位置标记为不装配。

- 参数与网络：`B_bias=R1 4.7K RS485_B to GND`；`A_bias=R6 4.7K RS485_A to +3.3V`；`termination=R4 120R/NC across RS485_B and RS485_A`；`termination_populated=false`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 第 1 页中上 R1/R6/R4 与 RS485_B/RS485_A/GND/+3.3V

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom RS485 通信与供电架构 | `transceiver=U1 SP3485EN-L/TR`；`host_signals=RX, TX`；`bus_signals=RS485_A, RS485_B`；`terminal=J1 HDR_4P_3.96`；`dc_dc=U2 AOZ1282CI`；`power_path=+12V -> U2 -> +5VIN -> P2` |
| 接口 | Atom 连接器映射 | `P1=pin1 +3.3V, pin2 RX, pin3 TX, pin4 NC, pin5 NC`；`P2=pin1 NC, pin2 NC, pin3 +5VIN, pin4 GND` |
| 总线 | SP3485EN-L/TR UART 与 RS-485 映射 | `RO=pin1 -> R2 1K -> RX`；`DI=pin4 GND`；`B=pin7 RS485_B`；`A=pin6 RS485_A`；`VCC=pin8 +3.3V`；`GND=pin5 GND`；`decoupling=C1 100nF` |
| GPIO 与控制信号 | TX 自动方向控制网络 | `control_pins=/RE pin2 tied to DE pin3`；`pullup=R3 4.7K to +3.3V`；`transistor=Q1 SS8050 Y1`；`base_drive=TX through R5 1K`；`emitter=GND` |
| 关键网络 | RS485 A/B 偏置与可选终端 | `B_bias=R1 4.7K RS485_B to GND`；`A_bias=R6 4.7K RS485_A to +3.3V`；`termination=R4 120R/NC across RS485_B and RS485_A`；`termination_populated=false` |
| 保护电路 | RS485 三路 TVS 保护 | `B_to_GND=D1 SMAJ6.5CA-E3`；`B_to_A=D2 SMAJ6.5CA-E3`；`A_to_GND=D3 SMAJ6.5CA-E3` |
| 接口 | J1 RS-485 与 12V 端子 | `B=RS485_B`；`A=RS485_A`；`12V+=+12V`；`12V-=GND` |
| 电源 | AOZ1282CI +12V 输入与使能 | `VIN=pin5 +12V`；`EN=pin4 through R7 100K to +12V`；`GND=pin2 GND`；`input_capacitors=C3/C4 10uF (106) 10% 35V` |
| 电源 | AOZ1282CI +5VIN 降压输出 | `LX=pin6`；`inductor=L1 4.7uH to +5VIN`；`freewheel_diode=D4 B5819W SL LX to GND`；`bootstrap=C2 100nF BST pin1 to LX`；`output_caps=C5 10uF, C6 100nF` |
| 电源 | AOZ1282CI 输出反馈 | `upper_resistor=R8 51K +5VIN to FB`；`lower_resistor=R9 10K FB to GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `72fa3f8f2f70f0097edc759aa4941778e213c6dfa1130aabdcf80b0b8019cefa` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomic485/atomic485_sch_01.webp` |

---

源文档：`zh_CN/atom/atomic485.md`

源文档 SHA-256：`35ec6a9ebfcdf132deb82f8e39fecffa651e7db63d5efe911fd9828966f6e76c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
