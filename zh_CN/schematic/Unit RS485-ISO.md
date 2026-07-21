# Unit RS485-ISO 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RS485-ISO |
| SKU | U094 |
| 产品 ID | `unit-rs485-iso-a1adae831e85` |
| 源文档 | `zh_CN/unit/iso485.md` |

## 概述

Unit RS485-ISO 以 U1 CA-IS3082W 将 Grove 侧 UART_Tx/UART_Rx 转换为隔离的半双工 485_A/485_B，Q1/Q2 BSS138 周边电路完成自动方向控制。M1 B0505ST16-W5 从 HOST_5V 生成隔离 VCC_5V，U2 MST5333 则生成 Grove 逻辑侧 HOST_3V3，HOST_GND 与隔离侧 GND 分开。RS-485 侧通过 TVS、P0080TA、SMD4532-075 和 F1/F2 自恢复保险丝形成多级保护，最终由 JP1 引出 485_OUT_A、485_OUT_B 与 SHIELD。

## 检索关键词

`Unit RS485-ISO`、`U094`、`CA-IS3082W`、`B0505ST16-W5`、`MST5333`、`RS-485`、`RS485`、`half-duplex`、`UART_Tx`、`UART_Rx`、`485_A`、`485_B`、`485_OUT_A`、`485_OUT_B`、`HOST_5V`、`HOST_3V3`、`HOST_GND`、`VCC_5V`、`SHIELD`、`BSS138`、`PSDV05-4`、`PESD5V0L1BA`、`P0080TA`、`SMD4532-075`、`60V 100mA`、`JK-NSMD010`、`JP1`、`GROVE`、`automatic direction`、`fail-safe bias`、`120Ω termination`、`500Kbps`、`1000VRMS`、`256 nodes`、`15kV ESD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | CA-IS3082W | 隔离式半双工 RS-485 收发器 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A2，U1 器件框下方标注 CA-IS3082W，左右分别为 UART 逻辑侧与 A/B 总线侧 |
| M1 | B0505ST16-W5 | HOST_5V 至隔离 VCC_5V 的隔离 DC-DC 模块 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 B1-B2 Isolated 5V Power 区域，M1 标注 B0505ST16-W5 |
| U2 | MST5333 | HOST_5V 至 HOST_3V3 Grove 侧 LDO | 图 ed7400bc012b / 第 1 页 / 页 1 网格 B3 Grove LDO 区域，U2 标注 MST5333，VIN/VOUT 接 HOST_5V/HOST_3V3 |
| Q1,Q2 | BSS138 | UART 半双工自动方向控制 MOSFET | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A1-A2 Isolated RS-485 区域，Q1/Q2 均标注 BSS138，连接 UART_Tx/UART_Rx 与 U1 RO/RE/DE/DI |
| D2 | PSDV05-4 | Grove UART 与 HOST_5V 侧多线 ESD 保护器件 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A1，D2 标注 PSDV05-4，连接 UART_Tx、UART_Rx、HOST_5V 与 HOST_GND |
| GROVE | Grove 4P | UART 与 HOST_5V 主机接口 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A4 Grove 区域，四针标注 IO2、IO1、5V、GND 并连接 UART_Tx、UART_Rx、HOST_5V、HOST_GND |
| JP1 | RS-485 Out Con 4P | 保护后的 RS-485 A/B 与屏蔽端输出接口 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A4 RS-485 Out Con 区域，JP1 四针连接 485_OUT_B、485_OUT_A、NC、SHIELD |
| F1,F2 | 60V 100mA / JK-NSMD010 | RS-485 B/A 串联自恢复保险丝 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A3 I/O Protector 区域，F1/F2 标注 60V 100mA/JK-NSMD010，串联在 B/A 输出路径 |
| DZ1,DZ2 | PESD5V0L1BA | 485_B 与 485_A 线对地 ESD/瞬态保护 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A2-A3 I/O Protector 左侧，DZ1/DZ2 标注 PESD5V0L1BA，分别连接 485_B/485_A |
| TS1,TS2,TS3 | P0080TA | RS-485 总线浪涌保护器件 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A3 I/O Protector 中部，TS1/TS2/TS3 均标注 P0080TA |
| GDT1,GDT2 | SMD4532-075 | RS-485 B/A 至 SHIELD 的气体放电保护器 | 图 ed7400bc012b / 第 1 页 / 页 1 网格 A3 I/O Protector 右侧，GDT1/GDT2 标注 SMD4532-075 |

## 系统结构

### Unit RS485-ISO 隔离架构

Grove 侧 UART_Tx/UART_Rx 经自动方向控制连接 U1 CA-IS3082W，隔离侧输出 485_A/485_B，再经过 I/O Protector 到 JP1；M1 为隔离侧提供独立 VCC_5V。

- 参数与网络：`host_interface=UART_Tx,UART_Rx`；`isolated_transceiver=U1 CA-IS3082W`；`bus_nets=485_A,485_B`；`protected_outputs=485_OUT_A,485_OUT_B`；`isolated_power=M1 B0505ST16-W5`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 上半部 Grove、Isolated RS-485、I/O Protector、JP1 与下方 Isolated 5V Power 功能块

## 电源

### 主机侧与隔离侧电源域

主机侧使用 HOST_5V、HOST_3V3、HOST_GND，RS-485 隔离侧使用 VCC_5V、GND；原理图以不同网络名保持两侧地与电源分离。

- 参数与网络：`host_domain=HOST_5V,HOST_3V3,HOST_GND`；`isolated_domain=VCC_5V,GND`；`galvanic_ground_connection=false`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 U1 两侧 VCC1/GND1 与 VCC2/GND2 及 M1 输入输出网络名称

### M1 隔离 5V 电源

HOST_5V 经 L1 6.8 uH 输入 M1 B0505ST16-W5，M1 输出 VCC_5V 与隔离 GND；C5、C6、C7 均为 10 uF/16V，D1 LESD3Z5.0CMT1G 跨接 VCC_5V 与 GND。

- 参数与网络：`module=M1 B0505ST16-W5`；`input_filter=L1 6.8uH,C5 10uF/16V,C6 10uF/16V`；`output_capacitor=C7 10uF/16V`；`output_rail=VCC_5V`；`output_ground=GND`；`output_protection=D1 LESD3Z5.0CMT1G`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 B1-B2 Isolated 5V Power 区域，L1、M1、C5-C7、D1 与两侧电源域

### U2 HOST_3V3 LDO

U2 MST5333 的 VIN 引脚 3 接 HOST_5V，VOUT 引脚 2 输出 HOST_3V3，GND 引脚 1 接 HOST_GND；输入输出各配置 4.7 uF/6.3V 电容。

- 参数与网络：`reference=U2`；`part_number=MST5333`；`input=VIN/pin 3/HOST_5V`；`output=VOUT/pin 2/HOST_3V3`；`ground=GND/pin 1/HOST_GND`；`capacitors=C3 4.7uF/6.3V,C4 4.7uF/6.3V`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 B3 Grove LDO 区域，U2、C3/C4 与 HOST_5V/HOST_3V3/HOST_GND

### LED1

HOST_3V3 输出侧连接 LED1 SMT_LED，并通过 1 kΩ 电阻回到 HOST_GND，作为主机侧 3.3V 状态指示。

- 参数与网络：`reference=LED1`；`part_number=SMT_LED`；`rail=HOST_3V3`；`series_resistance_ohm=1000`；`return=HOST_GND`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 B3 U2 输出旁 LED1 SMT_LED 与 1K 电阻

## 接口

### GROVE UART 接口

GROVE 的 IO2、IO1、5V、GND 四针分别连接 UART_Tx、UART_Rx、HOST_5V、HOST_GND。

- 参数与网络：`reference=GROVE`；`pinout=IO2:UART_Tx,IO1:UART_Rx,5V:HOST_5V,GND:HOST_GND`；`uart_tx_direction=input to unit`；`uart_rx_direction=output from unit`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A4 GROVE 四针文字与右侧 UART_Tx/UART_Rx、HOST_5V/HOST_GND 网络

### JP1 RS-485 输出接口

JP1 的 4、3、2、1 脚分别连接 485_OUT_B、485_OUT_A、未连接、SHIELD。

- 参数与网络：`reference=JP1`；`pinout=4:485_OUT_B,3:485_OUT_A,2:NC,1:SHIELD`；`bus_direction=bidirectional half-duplex`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A4 JP1 的脚号与 485_OUT_B、485_OUT_A、SHIELD 网络

## 总线

### UART 逻辑侧

UART_Tx 与 UART_Rx 连接到 Q1/Q2 BSS138 和 U1 的 RO、RE、DE、DI 周边逻辑，Grove 侧不另提供方向控制引脚。

- 参数与网络：`tx_network=UART_Tx`；`rx_network=UART_Rx`；`direction_control_components=Q1,Q2 BSS138`；`external_direction_pin=null`；`transceiver_logic_pins=RO,RE,DE,DI`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A1-A2，UART_Tx/UART_Rx、Q1/Q2 与 U1 RO/RE/DE/DI 电路

### U1 RS-485 总线侧

U1 的 B 引脚 13 连接 485_B，A 引脚 12 连接 485_A；两条网络经保护电路分别变为 485_OUT_B、485_OUT_A。

- 参数与网络：`transceiver=U1 CA-IS3082W`；`b_pin=pin 13/485_B`；`a_pin=pin 12/485_A`；`protected_outputs=485_OUT_B,485_OUT_A`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 U1 右侧 B/A 引脚 13/12 与 I/O Protector 两条总线路径

### 485_A/485_B 偏置

R8、R10 均为 4.7 kΩ；R8 将 485_B 偏置到隔离侧 GND，R10 将 485_A 偏置到 VCC_5V。

- 参数与网络：`b_bias=R8 4.7k to GND`；`a_bias=R10 4.7k to VCC_5V`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A2，U1 B/A 引脚旁 R8/R10 4.7KΩ 与 GND/VCC_5V

## 保护电路

### Grove UART 侧保护

D2 PSDV05-4 连接 UART_Tx、UART_Rx、HOST_5V 与 HOST_GND，为 Grove 侧信号和电源提供多线瞬态保护。

- 参数与网络：`reference=D2`；`part_number=PSDV05-4`；`protected_nets=UART_Tx,UART_Rx,HOST_5V`；`return_net=HOST_GND`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A1 D2 PSDV05-4 的 IO1-IO4、VCC、GND 连接

### 485_A/485_B TVS 保护

DZ1、DZ2 均为 PESD5V0L1BA，分别连接 485_B、485_A 与隔离 GND；R6 1 nF/2000V 电容性连接隔离 GND 与 SHIELD。

- 参数与网络：`b_tvs=DZ1 PESD5V0L1BA`；`a_tvs=DZ2 PESD5V0L1BA`；`return_net=GND`；`shield_coupling=R6 1nF/2000V between GND and SHIELD`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A2-A3 I/O Protector 左侧 DZ1/DZ2 与 R6 1nF/2000V

### RS-485 浪涌保护级

I/O Protector 中 TS1、TS2、TS3 标注 P0080TA，GDT1、GDT2 标注 SMD4532-075，连接于 A/B、SHIELD 保护网络。

- 参数与网络：`thyristor_devices=TS1,TS2,TS3 P0080TA`；`gas_discharge_devices=GDT1,GDT2 SMD4532-075`；`protected_nets=485_A,485_B`；`shield_net=SHIELD`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A3 I/O Protector 中央 TS1-TS3 与右侧 GDT1/GDT2

### F1/F2 串联保护

F1、F2 均标注 60V 100mA/JK-NSMD010，分别串联在 485_B 至 485_OUT_B、485_A 至 485_OUT_A 路径。

- 参数与网络：`b_fuse=F1 60V 100mA/JK-NSMD010`；`a_fuse=F2 60V 100mA/JK-NSMD010`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 网格 A3 I/O Protector 上下两条输出线上 F1/F2 标注

## 关键网络

### RS-485 终端电阻

本页未显示跨接 485_OUT_A 与 485_OUT_B 的板载 120 Ω 终端电阻；产品包装正文另列一只外置 120 Ω 电阻。

- 参数与网络：`onboard_termination_visible=false`；`documented_external_resistor_ohm=120`；`termination_nets=485_OUT_A,485_OUT_B`
- 证据：图 ed7400bc012b / 第 1 页 / 页 1 I/O Protector 至 JP1 的完整 A/B 输出路径没有跨线 120Ω 电阻

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RS485-ISO 隔离架构 | `host_interface=UART_Tx,UART_Rx`；`isolated_transceiver=U1 CA-IS3082W`；`bus_nets=485_A,485_B`；`protected_outputs=485_OUT_A,485_OUT_B`；`isolated_power=M1 B0505ST16-W5` |
| 接口 | GROVE UART 接口 | `reference=GROVE`；`pinout=IO2:UART_Tx,IO1:UART_Rx,5V:HOST_5V,GND:HOST_GND`；`uart_tx_direction=input to unit`；`uart_rx_direction=output from unit` |
| 接口 | JP1 RS-485 输出接口 | `reference=JP1`；`pinout=4:485_OUT_B,3:485_OUT_A,2:NC,1:SHIELD`；`bus_direction=bidirectional half-duplex` |
| 总线 | UART 逻辑侧 | `tx_network=UART_Tx`；`rx_network=UART_Rx`；`direction_control_components=Q1,Q2 BSS138`；`external_direction_pin=null`；`transceiver_logic_pins=RO,RE,DE,DI` |
| 总线 | U1 RS-485 总线侧 | `transceiver=U1 CA-IS3082W`；`b_pin=pin 13/485_B`；`a_pin=pin 12/485_A`；`protected_outputs=485_OUT_B,485_OUT_A` |
| 总线 | 485_A/485_B 偏置 | `b_bias=R8 4.7k to GND`；`a_bias=R10 4.7k to VCC_5V` |
| 电源 | 主机侧与隔离侧电源域 | `host_domain=HOST_5V,HOST_3V3,HOST_GND`；`isolated_domain=VCC_5V,GND`；`galvanic_ground_connection=false` |
| 电源 | M1 隔离 5V 电源 | `module=M1 B0505ST16-W5`；`input_filter=L1 6.8uH,C5 10uF/16V,C6 10uF/16V`；`output_capacitor=C7 10uF/16V`；`output_rail=VCC_5V`；`output_ground=GND`；`output_protection=D1 LESD3Z5.0CMT1G` |
| 电源 | U2 HOST_3V3 LDO | `reference=U2`；`part_number=MST5333`；`input=VIN/pin 3/HOST_5V`；`output=VOUT/pin 2/HOST_3V3`；`ground=GND/pin 1/HOST_GND`；`capacitors=C3 4.7uF/6.3V,C4 4.7uF/6.3V` |
| 电源 | LED1 | `reference=LED1`；`part_number=SMT_LED`；`rail=HOST_3V3`；`series_resistance_ohm=1000`；`return=HOST_GND` |
| 保护电路 | Grove UART 侧保护 | `reference=D2`；`part_number=PSDV05-4`；`protected_nets=UART_Tx,UART_Rx,HOST_5V`；`return_net=HOST_GND` |
| 保护电路 | 485_A/485_B TVS 保护 | `b_tvs=DZ1 PESD5V0L1BA`；`a_tvs=DZ2 PESD5V0L1BA`；`return_net=GND`；`shield_coupling=R6 1nF/2000V between GND and SHIELD` |
| 保护电路 | RS-485 浪涌保护级 | `thyristor_devices=TS1,TS2,TS3 P0080TA`；`gas_discharge_devices=GDT1,GDT2 SMD4532-075`；`protected_nets=485_A,485_B`；`shield_net=SHIELD` |
| 保护电路 | F1/F2 串联保护 | `b_fuse=F1 60V 100mA/JK-NSMD010`；`a_fuse=F2 60V 100mA/JK-NSMD010` |
| 关键网络 | RS-485 终端电阻 | `onboard_termination_visible=false`；`documented_external_resistor_ohm=120`；`termination_nets=485_OUT_A,485_OUT_B` |
| 核心器件 | 通信与隔离额定值 | `documented_max_bitrate_kbps=500`；`documented_max_nodes=256`；`documented_isolation_vrms=1000`；`documented_esd_kv=15`；`documented_protections=fail-safe,overcurrent,thermal shutdown`；`schematic_ratings=null` |

## 待确认事项

- `component.ratings`：产品正文声称最高 500 kbps、256 节点、1000 VRMS 隔离耐压、±15 kV ESD 及失效保护/过流/热关断；这些系统额定值和阈值未在本页原理图中标注。（证据：图 ed7400bc012b / 第 1 页 / 页 1 U1、M1 与 I/O Protector 电路未打印速率、节点数、隔离耐压或 ESD 系统额定值）
- `review.ratings`：500 kbps、256 节点、1000 VRMS、±15 kV 和各保护功能分别适用哪些测试标准、布线与工作条件？；原因：原理图确认器件和保护拓扑，但未给出系统级额定值、测试条件或保护阈值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ed7400bc012b37cada211c8d4264b53d98a5e6b6b85c0c3645e1066b500d0f1a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/588/SCH_UNIT_ISO485_v1.1_sch_01.png` |

---

源文档：`zh_CN/unit/iso485.md`

源文档 SHA-256：`c2a381bb4d0fbdbe8f0525f774023fb1a9e3377180a28b226a3f9aa46c600669`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
