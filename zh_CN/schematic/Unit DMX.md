# Unit DMX 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DMX |
| SKU | U183 |
| 产品 ID | `unit-dmx-012418845602` |
| 源文档 | `zh_CN/unit/Unit-DMX.md` |

## 概述

Unit DMX 以 U3 CA-IS3092W 隔离式差分收发器为核心，J1 Grove 提供 RXD、TXD、+5V 和 GND。U2 ME6206A33XG 将 5V 转换为 3V3，U3 内部隔离电源形成 ISO_3V3/ISO_GND，A/B 侧与逻辑地分离。TXD 经 Q2 2N7002W 控制共接的 /RE、DE 节点，DI 固定为低电平；A/B 由 4.7K 偏置并通过 D1-D3 防护后连接 P1 XLR-328P。SW1 可将 R4 120R 跨接到 A/B，总线终端可按需接入。

## 检索关键词

`Unit DMX`、`U183`、`CA-IS3092W`、`ME6206A33XG`、`2N7002W`、`XLR-328P`、`SS-1260`、`DMX512`、`RS-485`、`half duplex`、`RXD`、`TXD`、`A`、`B`、`VDDA`、`VISO`、`3V3`、`ISO_3V3`、`ISO_GND`、`120R`、`termination`、`5kVrms`、`250Kbps`、`500Kbps`、`HY2.0-4P Grove`、`XLR-3`、`R5 4.7K`、`R7 4.7K`、`D1-D3`、`RED LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | CA-IS3092W | 逻辑侧与 A/B 总线侧隔离的差分收发器，集成 VISO 隔离电源域 | 图 c9affd32e389 / 第 1 页 / 第 1 页中央 U3 CA-IS3092W，VDDA/GNDA、RO/RE#/DE/DI 与 VISO/GNDB/A/B/SEL 引脚 |
| U2 | ME6206A33XG | 5V 至 3V3 稳压器 | 图 c9affd32e389 / 第 1 页 / 第 1 页上方 U2，VIN pin 3、VOUT pin 2、GND pin 1 及 ME6206A33XG 标注 |
| J1 | GROVE 4P | 主机 UART 与 5V 电源接口 | 图 c9affd32e389 / 第 1 页 / 第 1 页左上 J1 GROVE，IO2/IO1/5V/GND 与 RXD/TXD/5V/GND |
| P1 | XLR-328P | 隔离侧 DMX/差分总线三针 XLR 接口 | 图 c9affd32e389 / 第 1 页 / 第 1 页右侧 P1 XLR-328P，pin 1 ISO_GND、pin 2 B、pin 3 A |
| Q1,Q2 | 2N7002W | RXD 逻辑整形与 TXD 驱动/方向控制 MOSFET | 图 c9affd32e389 / 第 1 页 / 第 1 页左中 Q1/Q2 均标 2N7002W，连接 RXD/TXD 与 U3 RO/RE#/DE |
| SW1,R4 | SS-1260 / 120R | 可开关接入的 A/B 总线 120Ω 终端 | 图 c9affd32e389 / 第 1 页 / 第 1 页右中 R4 120R 与 SW1 SS-1260 串联跨接 A/B |
| D1,D2,D3 | 未标注 | 隔离侧 B 对地、B-A 跨线、A 对地的三器件保护网络 | 图 c9affd32e389 / 第 1 页 / 第 1 页右中 D1-D3 竖直保护链，连接 ISO_GND、B、A、ISO_GND |
| D4,R8 | RED LED / 2K | 3V3 电源指示灯支路 | 图 c9affd32e389 / 第 1 页 / 第 1 页上中 3V3、R8 2K、D4 RED LED 与 GND |
| C1,C7,C8,C9 | 10uF / 100nF / 100nF / 10uF | U3 逻辑侧 3V3 与隔离侧 ISO_3V3 的电源去耦 | 图 c9affd32e389 / 第 1 页 / 第 1 页 U3 上方 C1/C7 跨 3V3-GND，C8/C9 跨 ISO_3V3-ISO_GND |

## 系统结构

### Unit DMX 系统架构

单页电路由 J1 Grove、U2 3V3 稳压器、U3 CA-IS3092W 隔离收发器、Q1/Q2 逻辑网络、A/B 偏置与保护、SW1/R4 终端及 P1 XLR 接口构成。

- 参数与网络：`host_interface=J1 Grove RXD/TXD`；`regulator=U2 ME6206A33XG`；`isolated_transceiver=U3 CA-IS3092W`；`bus=A/B`；`termination=SW1 + R4 120R`；`output_connector=P1 XLR-328P`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页完整单页电路，J1/U2/U3/Q1/Q2/SW1/P1 功能区

### 其他功能分区

本页未绘制独立 MCU、协处理器、存储器、晶振、复位/BOOT、调试口、音频、传感器、射频、电池或充电器；控制器位于 J1 外部主机。

- 参数与网络：`onboard_controller=false`；`coprocessor=false`；`memory=false`；`storage=false`；`clock=false`；`reset=false`；`debug=false`；`audio=false`；`sensor=false`；`rf=false`；`battery=false`；`charger=false`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页全部器件与网络，仅含接口、电源、隔离收发、保护和终端

## 电源

### 5V 至 3V3 稳压

J1 5V 网络连接 U2 ME6206A33XG VIN pin 3，VOUT pin 2 输出 3V3，GND pin 1 接地；输入 C4 10uF，输出 C5 100nF 与 C6 10uF 均对地。

- 参数与网络：`input=5V -> U2 pin 3 VIN`；`output=U2 pin 2 VOUT -> 3V3`；`ground=U2 pin 1`；`input_capacitor=C4 10uF`；`output_capacitors=C5 100nF,C6 10uF`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页上方 J1 5V、U2、C4-C6、3V3 与 GND

### U3 双电源域

U3 逻辑侧 VDDA pin 1 接 3V3，GNDA pins 2、7、8 接 GND；隔离侧 VISO pin 16 输出 ISO_3V3，GNDB pins 15、9 接 ISO_GND，SEL pin 10 也接 ISO_GND。

- 参数与网络：`logic_supply=VDDA pin 1 -> 3V3`；`logic_ground=GNDA pins 2,7,8 -> GND`；`isolated_supply=VISO pin 16 -> ISO_3V3`；`isolated_ground=GNDB pins 15,9 -> ISO_GND`；`select=SEL pin 10 -> ISO_GND`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页中央 U3 两侧 VDDA/GNDA/VISO/GNDB/SEL 网络

### U3 双域去耦

逻辑侧 C1 10uF 与 C7 100nF 跨接 3V3/GND；隔离侧 C8 100nF 与 C9 10uF 跨接 ISO_3V3/ISO_GND。

- 参数与网络：`logic_caps=C1 10uF,C7 100nF`；`logic_rails=3V3/GND`；`isolated_caps=C8 100nF,C9 10uF`；`isolated_rails=ISO_3V3/ISO_GND`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页 U3 上方 C1/C7 和 C8/C9 两组去耦

### 3V3 指示灯

3V3 经 R8 2K 和 D4 RED LED 串联到 GND，形成常接电源指示支路。

- 参数与网络：`rail=3V3`；`resistor=R8 2K`；`led=D4 RED LED`；`return=GND`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页上中 R8/D4 电源 LED 支路

## 接口

### J1 Grove 主机接口

J1 的 IO2、IO1、5V、GND 四触点分别连接 RXD、TXD、5V、GND。

- 参数与网络：`connector=J1 GROVE 4P`；`pinout=IO2:RXD,IO1:TXD,5V:5V,GND:GND`；`signal_level=3V3 logic network`；`direction=RXD to host,TXD from host`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页左上 J1 GROVE 的 IO2/IO1/5V/GND 行与 RXD/TXD/5V/GND

### P1 XLR-328P

P1 pin 1 连接 ISO_GND，pin 2 连接 B，pin 3 连接 A。

- 参数与网络：`connector=P1 XLR-328P`；`pinout=1:ISO_GND,2:B,3:A`；`isolation_domain=ISO_3V3/ISO_GND side`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页右侧 P1 XLR-328P pins 1-3 与 ISO_GND/B/A

## 总线

### TXD 与 U3 驱动控制

TXD 经 R6 1KΩ 驱动 Q2 2N7002W；Q2 源极接 GND，漏极连接 U3 RE# pin 4 与 DE pin 5 的共节点，该节点由 R3 4.7KΩ 上拉到 3V3。U3 DI pin 6 固定接 GND。

- 参数与网络：`input=TXD`；`gate_resistor=R6 1K`；`transistor=Q2 2N7002W`；`controlled_pins=U3 pin 4 RE# and pin 5 DE tied`；`pullup=R3 4.7K to 3V3`；`driver_input=U3 pin 6 DI -> GND`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页左中 TXD/R6/Q2/R3 与 U3 RE#/DE/DI pins 4-6

### RXD 与 U3 RO 逻辑网络

RXD 与 U3 RO pin 3 之间配置 Q1 2N7002W 及 R1、R2 各 100KΩ 的 3V3 偏置/整形网络。

- 参数与网络：`host_net=RXD`；`receiver_output=U3 pin 3 RO`；`transistor=Q1 2N7002W`；`resistors=R1 100K,R2 100K`；`rail=3V3`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页左中 RXD、R1/R2、Q1 与 U3 RO pin 3

### U3 A/B 差分总线

U3 A pin 12 连接 A 网络，B pin 13 连接 B 网络；A 通过 R7 4.7KΩ 偏置到 ISO_3V3，B 通过 R5 4.7KΩ 偏置到 ISO_GND。

- 参数与网络：`a_pin=U3 pin 12 A`；`b_pin=U3 pin 13 B`；`a_bias=R7 4.7K to ISO_3V3`；`b_bias=R5 4.7K to ISO_GND`；`topology=two-wire differential bus`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页中央右侧 U3 A/B pins 12/13、R7/R5 与 ISO_3V3/ISO_GND

### A/B 120Ω 终端

R4 120R 与 SW1 SS-1260 串联跨接 B 和 A；SW1 闭合时将 120Ω 电阻接入差分总线。

- 参数与网络：`resistor=R4 120R`；`switch=SW1 SS-1260`；`between=B-A`；`closed_state=termination connected`；`open_state=termination disconnected`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页右中 B-R4 120R-SW1-A 支路

## 保护电路

### A/B 总线保护

D1 连接 ISO_GND 与 B，D2 跨接 B 与 A，D3 连接 A 与 ISO_GND，形成 B 对地、线间和 A 对地三支路保护；本页未标注 D1-D3 的具体型号。

- 参数与网络：`b_to_ground=D1`；`line_to_line=D2`；`a_to_ground=D3`；`return=ISO_GND`；`part_number=null`
- 证据：图 c9affd32e389 / 第 1 页 / 第 1 页右中 D1-D3 保护链与 ISO_GND/B/A 节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit DMX 系统架构 | `host_interface=J1 Grove RXD/TXD`；`regulator=U2 ME6206A33XG`；`isolated_transceiver=U3 CA-IS3092W`；`bus=A/B`；`termination=SW1 + R4 120R`；`output_connector=P1 XLR-328P` |
| 电源 | 5V 至 3V3 稳压 | `input=5V -> U2 pin 3 VIN`；`output=U2 pin 2 VOUT -> 3V3`；`ground=U2 pin 1`；`input_capacitor=C4 10uF`；`output_capacitors=C5 100nF,C6 10uF` |
| 电源 | U3 双电源域 | `logic_supply=VDDA pin 1 -> 3V3`；`logic_ground=GNDA pins 2,7,8 -> GND`；`isolated_supply=VISO pin 16 -> ISO_3V3`；`isolated_ground=GNDB pins 15,9 -> ISO_GND`；`select=SEL pin 10 -> ISO_GND` |
| 电源 | U3 双域去耦 | `logic_caps=C1 10uF,C7 100nF`；`logic_rails=3V3/GND`；`isolated_caps=C8 100nF,C9 10uF`；`isolated_rails=ISO_3V3/ISO_GND` |
| 电源 | 3V3 指示灯 | `rail=3V3`；`resistor=R8 2K`；`led=D4 RED LED`；`return=GND` |
| 接口 | J1 Grove 主机接口 | `connector=J1 GROVE 4P`；`pinout=IO2:RXD,IO1:TXD,5V:5V,GND:GND`；`signal_level=3V3 logic network`；`direction=RXD to host,TXD from host` |
| 总线 | TXD 与 U3 驱动控制 | `input=TXD`；`gate_resistor=R6 1K`；`transistor=Q2 2N7002W`；`controlled_pins=U3 pin 4 RE# and pin 5 DE tied`；`pullup=R3 4.7K to 3V3`；`driver_input=U3 pin 6 DI -> GND` |
| 总线 | RXD 与 U3 RO 逻辑网络 | `host_net=RXD`；`receiver_output=U3 pin 3 RO`；`transistor=Q1 2N7002W`；`resistors=R1 100K,R2 100K`；`rail=3V3` |
| 总线 | U3 A/B 差分总线 | `a_pin=U3 pin 12 A`；`b_pin=U3 pin 13 B`；`a_bias=R7 4.7K to ISO_3V3`；`b_bias=R5 4.7K to ISO_GND`；`topology=two-wire differential bus` |
| 接口 | P1 XLR-328P | `connector=P1 XLR-328P`；`pinout=1:ISO_GND,2:B,3:A`；`isolation_domain=ISO_3V3/ISO_GND side` |
| 保护电路 | A/B 总线保护 | `b_to_ground=D1`；`line_to_line=D2`；`a_to_ground=D3`；`return=ISO_GND`；`part_number=null` |
| 总线 | A/B 120Ω 终端 | `resistor=R4 120R`；`switch=SW1 SS-1260`；`between=B-A`；`closed_state=termination connected`；`open_state=termination disconnected` |
| 系统结构 | 其他功能分区 | `onboard_controller=false`；`coprocessor=false`；`memory=false`；`storage=false`；`clock=false`；`reset=false`；`debug=false`；`audio=false`；`sensor=false`；`rf=false`；`battery=false`；`charger=false` |
| 总线 | DMX512 协议与速率 | `documented_protocol=DMX512`；`documented_dmx_bitrate_bps=250000`；`documented_max_transceiver_bps=500000`；`documented_physical_layer=RS-485 half duplex`；`schematic_bitrate=null`；`frame_format=null` |
| 保护电路 | 隔离耐压 | `documented_isolation_vrms=5000`；`schematic_isolation_barrier=true`；`schematic_rating=null` |
| 接口 | XLR 接口机械属性 | `schematic_part_number=XLR-328P`；`documented_connector=XLR-3 female`；`schematic_gender=null` |

## 待确认事项

- `bus.documented-dmx-protocol`：产品正文称协议为 DMX512，固定速率 250Kbps，收发器最高数据速率 500Kbps，并描述为 RS-485 半双工；原理图只确认两线 A/B 收发拓扑，没有协议名称、波特率或帧格式。（证据：图 c9affd32e389 / 第 1 页 / 第 1 页 U3、A/B 与 P1 区域，无 DMX512、250Kbps 或 500Kbps 文字）
- `protection.documented-isolation-rating`：产品正文称 CA-IS3092W 提供 5kVrms 电气隔离；原理图绘制了 U3 隔离栅和独立地，但未标注耐压值或测试条件。（证据：图 c9affd32e389 / 第 1 页 / 第 1 页 U3 CA-IS3092W 内部隔离符号及 GND/ISO_GND 分域，无数值标注）
- `interface.documented-xlr-gender`：产品正文称 DMX 接口为 XLR-3 母头；原理图只标 P1 XLR-328P 和三针电气映射，未写公母、面板方向或机械规格。（证据：图 c9affd32e389 / 第 1 页 / 第 1 页右侧 P1 仅标 XLR-328P）
- `review.dmx-protocol`：请用当前固件、CA-IS3092W 规格或 DMX 测试确认 DMX512、250Kbps、500Kbps 上限和半双工行为。；原因：原理图只能确认 A/B 电气拓扑，不能证明上层协议与速率。
- `review.isolation-rating`：当前 CA-IS3092W 料号与 PCB 隔离设计是否满足正文所列 5kVrms？；原因：原理图显示隔离分域，但没有额定耐压、爬电距离或测试标准。
- `review.xlr-gender`：P1 XLR-328P 的量产机械版本是否为正文所述 XLR-3 母头？；原因：原理图器件值未直接标注接口性别和机械方向。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c9affd32e389d590c5a2feb74fcaeeb2bc663e8907885084fa007dcde39f334c` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DMX/img-a9577c01-030e-414c-a485-a37d14fa26b1.png` |

---

源文档：`zh_CN/unit/Unit-DMX.md`

源文档 SHA-256：`679cd85ea0f1bc2878a8f8cfba98b8e0271c60be39d40d84c41ce4b0d88a19db`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
