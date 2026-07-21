# Unit NBIoT 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NBIoT |
| SKU | U111 |
| 产品 ID | `unit-nbiot-812620512877` |
| 源文档 | `zh_CN/unit/nbiot_global.md` |

## 概述

Unit NBIoT 的无线核心 M1 标注 SIM7020G/SIM7020C，连接 Nano SIM U2、E1 IPEX 天线、UART、RESET、NETLIGHT 和 STATUS。UART 通过 Q2/Q3 SS8050 Y1 在 1.8 V 模组域与 3.3 V 主机域之间转换，并连接第二页 J1 HCore。VIN 经 U3 JW5033H 转换为 +5.4V，再由 VR1 AMS1117-3.3 生成 +3.3V；SIM 信号具有 SMF05CT1G ESD、22 Ω 串联电阻和 33 pF 滤波。

## 检索关键词

`Unit NBIoT`、`U111`、`SIM7020G`、`SIM7020C`、`SIM7020G/SIM7020C`、`NB-IoT`、`Cat-NB`、`UART`、`115200bps`、`U1_TX`、`U1_RX`、`M_TXD`、`M_RXD`、`SS8050 Y1`、`1.8V`、`3.3V`、`JW5033H`、`AMS1117-3.3`、`+5.4V`、`VIN`、`Nano SIM`、`SIM_VCC`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SMF05CT1G`、`ANT_IPEX`、`NETLIGHT`、`STATUS`、`PWRKEY`、`RESET`、`HCore`、`TCP`、`UDP`、`MQTT`、`B1`、`B85`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7020G/SIM7020C | NB-IoT 蜂窝通信模组 | 图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 中部 M1 器件框下方标注 SIM7020G/SIM7020C |
| U2 | SIM | Nano SIM 卡座 | 图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 左下 U2 标注 SIM，针脚为 IO、CLK、RST、VCC、VPP、GND |
| U1 | SMF05CT1G | SIM 卡信号与电源 ESD 保护阵列 | 图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 左中 U1 标注 SMF05CT1G，连接 SIM_VCC 与 SIM 信号线 |
| E1 | ANT_IPEX | NB-IoT 外部射频天线连接器 | 图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 右中 E1 标注 ANT_IPEX，连接 M1 ANT pin 31 |
| U3 | JW5033H | VIN 至 +5.4V 开关稳压器 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 左上 U3 下方标注 JW5033H，输出经 L1 到 +5.4V |
| VR1 | AMS1117-3.3 | +5.4V 至 +3.3V 线性稳压器 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 上中 VR1 标注 AMS1117-3.3，Vin/Vout 接 +5.4V/+3.3V |
| J1 | HCore | 主机 UART、RESET、VIN 与地连接器 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 右下 J1 23 针连接器下方标注 HCore |
| Q2,Q3 | SS8050 Y1 | UART 1.8 V 与 3.3 V 电平转换晶体管 | 图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 右下 Q2/Q3 均标注 SS8050 Y1，位于 U1_RX/U1_TX 与 M_RXD/M_TXD 之间 |
| Q4 | SS8050 Y1 | 主机 RST 到模组 RESET 的复位驱动晶体管 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 右上 Q4 标注 SS8050 Y1，连接 RESET 与 RST |

## 系统结构

### Unit NBIoT 系统结构

M1 SIM7020G/SIM7020C 连接 Nano SIM、IPEX 天线和 1.8 V UART；UART 经 Q2/Q3 转换到 3.3 V 主机网络，并通过 J1 HCore 引出。

- 参数与网络：`modem=M1 SIM7020G/SIM7020C`；`sim_socket=U2 SIM`；`antenna=E1 ANT_IPEX`；`uart_level_shift=Q2,Q3 SS8050 Y1`；`host_connector=J1 HCore`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1、U2、E1 与 Q2/Q3 功能块; 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 J1 HCore 与 M_TXD/M_RXD/RST/VIN 网络

## 电源

### U3 +5.4V 电源

U3 JW5033H 的 VIN pin 3 接 VIN，EN pin 5 经 R15 100 kΩ 接 VIN，SW pin 2 经 L1 4.7 uH 输出 +5.4V；R16 115 kΩ 与 R18 20 kΩ 构成 FB pin 4 分压。

- 参数与网络：`reference=U3`；`part_number=JW5033H`；`input=VIN/pin 3`；`enable=EN/pin 5,R15 100k to VIN`；`switch_path=SW/pin 2,L1 4.7uH`；`output=+5.4V`；`feedback=R16 115k,R18 20k to FB/pin 4`；`bootstrap=C5 100nF between BST/pin 6 and SW`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 左上 U3、R15/R16/R18、C5、L1 与 +5.4V

### U3 输入输出电容

C6 10 uF 连接 VIN 与 GND；输出侧 C7 22 uF 和 C8 100 nF 并联在 +5.4V 与 GND 之间。

- 参数与网络：`input_capacitor=C6 10uF`；`output_capacitors=C7 22uF,C8 100nF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 U3 输入 C6 与 +5.4V 输出 C7/C8

### VR1 +3.3V 电源

VR1 AMS1117-3.3 的 Vin 接 +5.4V、Vout 输出 +3.3V、GND 接地；C9 22 uF 从 +3.3V 接地。

- 参数与网络：`reference=VR1`；`part_number=AMS1117-3.3`；`input_rail=+5.4V`；`output_rail=+3.3V`；`output_capacitor=C9 22uF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 上中 VR1 与 C9

### +3.3V 大容量电容

C11、C12 均为 100 uF，分别跨接 +3.3V 与 GND。

- 参数与网络：`capacitors=C11 100uF,C12 100uF`；`rail=+3.3V`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 中上 C11/C12 100uF 与 +3.3V/GND

## 接口

### J1 HCore 已连接针脚

J1 pin 6 TXD 连接 M_TXD，pin 7 RXD 连接 M_RXD，pin 10 RST 连接 RST，pin 11/12 接 GND，pin 13/14 接 VIN；其余针脚在本页未连接。

- 参数与网络：`reference=J1`；`connected_pinout=6:M_TXD/TXD,7:M_RXD/RXD,10:RST,11:GND,12:GND,13:VIN,14:VIN`；`other_pins=unconnected on this page`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 右下 J1 HCore 脚号与已连接网络

### U2 SIM 卡接口

U2 SIM 卡座的 VCC、RST、CLK、IO 分别连接 SIM_VCC、SIM_RST、SIM_CLK、SIM_DATA，GND 接地，VPP 未连接。

- 参数与网络：`reference=U2`；`pinout=VCC:SIM_VCC,RST:SIM_RST,CLK:SIM_CLK,IO:SIM_DATA,GND:GND,VPP:NC`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 左下 U2 SIM 卡座针脚与网络

## 总线

### M1 UART1

M1 UART1_TXD pin 1 连接 U1_TX，UART1_RXD pin 2 连接 U1_RX；UART1_RTS/CTS/DCD/DTR/RI pins 3-7 在本页标为未连接。

- 参数与网络：`tx=UART1_TXD/pin 1/U1_TX`；`rx=UART1_RXD/pin 2/U1_RX`；`unused_handshake=UART1_RTS/3,CTS/4,DCD/5,DTR/6,RI/7`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 左上 UART1 pins 1-7 与网络/未连接标记

### Q2/Q3 UART 电平转换

Q2/Q3 SS8050 Y1 与 R8-R13 4.7 kΩ 网络连接 U1_RX/U1_TX 的 +1.8V 域和 M_RXD/M_TXD 的 +3.3V 域。

- 参数与网络：`rx_converter=Q2 SS8050 Y1,R8-R10 4.7k`；`tx_converter=Q3 SS8050 Y1,R11-R13 4.7k`；`modem_domain=+1.8V`；`host_domain=+3.3V`；`host_nets=M_RXD,M_TXD`；`modem_nets=U1_RX,U1_TX`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 右下 Q2/Q3 与 R8-R13、+1.8V/+3.3V 网络

### M1 与 U2 SIM 信号

M1 SIM_DATA pin 15、SIM_CLK pin 16、SIM_RST pin 17 分别经 R5、R6、R7 22 Ω 连接 U2；SIM_VDD pin 18 连接 SIM_VCC。

- 参数与网络：`data=M1 SIM_DATA/15 -> R5 22ohm -> U2 IO`；`clock=M1 SIM_CLK/16 -> R6 22ohm -> U2 CLK`；`reset=M1 SIM_RST/17 -> R7 22ohm -> U2 RST`；`supply=M1 SIM_VDD/18 -> SIM_VCC -> U2 VCC`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 SIM pins 15-18、R5-R7 与 U2

## GPIO 与控制信号

### M1 PWRKEY

M1 PWRKEY pin 39 通过 R4 0 Ω 连接 GND。

- 参数与网络：`pin=PWRKEY/pin 39`；`strap=R4 0ohm to GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 PWRKEY pin 39 与 R4 0Ω/GND

### M1 NETLIGHT 指示

M1 NETLIGHT pin 41 经 R2 1 kΩ 驱动 Q1 SS8050 Y1，R3 10 kΩ 下拉；Q1 控制由 +3.3V、R1 1 kΩ、D1 0603 LED 构成的指示灯。

- 参数与网络：`source=M1 NETLIGHT/pin 41`；`base_resistor=R2 1k`；`base_pulldown=R3 10k`；`transistor=Q1 SS8050 Y1`；`led_path=+3.3V -> R1 1k -> D1 0603 -> Q1 -> GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 右上 NETLIGHT、Q1、D1 与 R1-R3 电路

## 复位

### M1 RESET 与主机 RST

M1 RESET pin 28 连接 RESET 网络；RESET 由 R14 10 kΩ 上拉至 +3.3V、C10 100 nF 接地，并通过 Q4 SS8050 Y1 和 R17 1 kΩ 连接主机 RST。

- 参数与网络：`modem_pin=RESET/pin 28`；`pullup=R14 10k to +3.3V`；`capacitor=C10 100nF to GND`；`driver=Q4 SS8050 Y1`；`host_series_resistor=R17 1k`；`host_net=RST`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 RESET pin 28 网络; 图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 右上 RESET、R14/C10、Q4/R17 与 RST

## 保护电路

### U1 SIM ESD 保护

U1 SMF05CT1G 连接 SIM_VCC、SIM_DATA、SIM_CLK、SIM_RST 与 GND，为 SIM 卡电源和信号提供多线瞬态保护。

- 参数与网络：`reference=U1`；`part_number=SMF05CT1G`；`protected_nets=SIM_VCC,SIM_DATA,SIM_CLK,SIM_RST`；`return=GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 U1 SMF05CT1G 与 SIM 电源/信号网络

## 射频

### M1 天线路径

M1 ANT pin 31 直接连接 E1 ANT_IPEX，E1 屏蔽端接 GND；图中未显示额外匹配网络。

- 参数与网络：`source=M1 ANT/pin 31`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=null`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 ANT pin 31 到 E1 ANT_IPEX 直连

## 模拟电路

### SIM 信号滤波

C2、C3、C4 均为 33 pF，分别从 SIM_DATA、SIM_CLK、SIM_RST 路径连接 GND；C13 1 uF 跨接 SIM_VCC 与 GND。

- 参数与网络：`signal_capacitors=C2 33pF,C3 33pF,C4 33pF`；`supply_capacitor=C13 1uF`；`return=GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 SIM 信号下方 C2-C4 与 U2 左侧 C13

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NBIoT 系统结构 | `modem=M1 SIM7020G/SIM7020C`；`sim_socket=U2 SIM`；`antenna=E1 ANT_IPEX`；`uart_level_shift=Q2,Q3 SS8050 Y1`；`host_connector=J1 HCore` |
| 核心器件 | M1 具体模组版本 | `schematic_part_number=SIM7020G/SIM7020C`；`documented_part_number=SIM7020G`；`assembled_variant=null` |
| 接口 | J1 HCore 已连接针脚 | `reference=J1`；`connected_pinout=6:M_TXD/TXD,7:M_RXD/RXD,10:RST,11:GND,12:GND,13:VIN,14:VIN`；`other_pins=unconnected on this page` |
| 接口 | 产品正文 Grove UART 接口 | `documented_grove_pinout=GND,5V,UART_RX,UART_TX`；`schematic_grove_connector=null`；`schematic_host_connector=J1 HCore` |
| 总线 | M1 UART1 | `tx=UART1_TXD/pin 1/U1_TX`；`rx=UART1_RXD/pin 2/U1_RX`；`unused_handshake=UART1_RTS/3,CTS/4,DCD/5,DTR/6,RI/7` |
| 总线 | Q2/Q3 UART 电平转换 | `rx_converter=Q2 SS8050 Y1,R8-R10 4.7k`；`tx_converter=Q3 SS8050 Y1,R11-R13 4.7k`；`modem_domain=+1.8V`；`host_domain=+3.3V`；`host_nets=M_RXD,M_TXD`；`modem_nets=U1_RX,U1_TX` |
| 总线 | UART 参数与 AT 指令 | `documented_baud=115200`；`documented_protocol=AT commands`；`schematic_baud=null`；`schematic_protocol=null` |
| 接口 | U2 SIM 卡接口 | `reference=U2`；`pinout=VCC:SIM_VCC,RST:SIM_RST,CLK:SIM_CLK,IO:SIM_DATA,GND:GND,VPP:NC` |
| 总线 | M1 与 U2 SIM 信号 | `data=M1 SIM_DATA/15 -> R5 22ohm -> U2 IO`；`clock=M1 SIM_CLK/16 -> R6 22ohm -> U2 CLK`；`reset=M1 SIM_RST/17 -> R7 22ohm -> U2 RST`；`supply=M1 SIM_VDD/18 -> SIM_VCC -> U2 VCC` |
| 保护电路 | U1 SIM ESD 保护 | `reference=U1`；`part_number=SMF05CT1G`；`protected_nets=SIM_VCC,SIM_DATA,SIM_CLK,SIM_RST`；`return=GND` |
| 模拟电路 | SIM 信号滤波 | `signal_capacitors=C2 33pF,C3 33pF,C4 33pF`；`supply_capacitor=C13 1uF`；`return=GND` |
| 射频 | M1 天线路径 | `source=M1 ANT/pin 31`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=null` |
| 电源 | U3 +5.4V 电源 | `reference=U3`；`part_number=JW5033H`；`input=VIN/pin 3`；`enable=EN/pin 5,R15 100k to VIN`；`switch_path=SW/pin 2,L1 4.7uH`；`output=+5.4V`；`feedback=R16 115k,R18 20k to FB/pin 4`；`bootstrap=C5 100nF between BST/pin 6 and SW` |
| 电源 | U3 输入输出电容 | `input_capacitor=C6 10uF`；`output_capacitors=C7 22uF,C8 100nF` |
| 电源 | VR1 +3.3V 电源 | `reference=VR1`；`part_number=AMS1117-3.3`；`input_rail=+5.4V`；`output_rail=+3.3V`；`output_capacitor=C9 22uF` |
| 电源 | +3.3V 大容量电容 | `capacitors=C11 100uF,C12 100uF`；`rail=+3.3V` |
| GPIO 与控制信号 | M1 PWRKEY | `pin=PWRKEY/pin 39`；`strap=R4 0ohm to GND` |
| GPIO 与控制信号 | M1 NETLIGHT 指示 | `source=M1 NETLIGHT/pin 41`；`base_resistor=R2 1k`；`base_pulldown=R3 10k`；`transistor=Q1 SS8050 Y1`；`led_path=+3.3V -> R1 1k -> D1 0603 -> Q1 -> GND` |
| 复位 | M1 RESET 与主机 RST | `modem_pin=RESET/pin 28`；`pullup=R14 10k to +3.3V`；`capacitor=C10 100nF to GND`；`driver=Q4 SS8050 Y1`；`host_series_resistor=R17 1k`；`host_net=RST` |
| 射频 | Cat-NB 频段与数据能力 | `documented_bands=B1,B2,B3,B4,B5,B8,B12,B13,B17,B18,B19,B20,B25,B26,B28,B66,B70,B71,B85`；`documented_downlink_kbps=126`；`documented_uplink_kbps=150`；`schematic_rf_capabilities=null` |
| 其他事实 | 网络协议支持 | `documented_protocols=TCP,UDP,HTTP,HTTPS,TLS,DTLS,DNS,NTP,PING,LWM2M,COAP,MQTT,MQTTS`；`schematic_protocols=null` |

## 待确认事项

- `component.modem_variant`：原理图将 M1 标为 SIM7020G/SIM7020C，产品正文称使用 SIM7020G；仅凭页面无法确认当前装配的是 G 还是 C 版本。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 下方复合型号 SIM7020G/SIM7020C）
- `interface.grove_mapping`：产品正文给出四针 Grove 的 GND、5V、UART_RX、UART_TX 映射，但两张原理图只显示 J1 HCore，没有 Grove 4P 连接器位号或针脚。（证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 页 1 主机接口仅标注 J1 HCore）
- `bus.uart_parameters`：产品正文标注 UART 115200 bps 和 AT 指令控制，但原理图只确认 UART 网络与电平转换，没有速率或命令协议标注。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 UART1 与 Q2/Q3 电路未标注速率或协议）
- `rf.capabilities`：产品正文列出 B1 至 B85 的多频段集合与 126 kbps 下行/150 kbps 上行能力，但原理图没有频段、速率或射频额定值。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 与 ANT_IPEX 路径未打印频段或数据速率）
- `other.network_protocols`：产品正文列出 TCP、UDP、HTTP(S)、TLS/DTLS、DNS、NTP、LWM2M、CoAP、MQTT(S) 等协议；原理图不包含固件协议栈信息。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 页 1 M1 外部电路没有固件协议标注）
- `review.modem_variant`：U111 当前装配的模组是否为 SIM7020G，SIM7020C 是否仅为兼容料位？；原因：原理图使用 SIM7020G/SIM7020C 复合型号。
- `review.grove_mapping`：产品实际 Grove 4P 与 J1 HCore 的 UART/VIN/GND 如何映射，Grove 连接器位号是什么？；原因：两张原理图没有显示 Grove 4P 连接器。
- `review.uart_parameters`：当前模组默认 UART 是否为 115200 bps，AT 指令集版本是什么？；原因：原理图只显示 UART 电气连接。
- `review.rf_capabilities`：列出的 Cat-NB 频段和 126/150 kbps 数据能力是否适用于当前 SIM7020G 固件与运营商配置？；原因：原理图没有频段、速率或认证配置。
- `review.network_protocols`：各网络协议由哪个固件版本提供，是否有运营商或内存限制？；原因：协议支持属于模组固件能力，不在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `674520ab1fc99396cd26a53d743d037424bb1d228dbbd4fe7aa78aacf62b7f9b` | `https://static-cdn.m5stack.com/resource/docs/products/unit/nbiot_global/nbiot_global_sch_01.webp` |
| 2 | 1 | `b53ff3ed62accdb8f8b109383f9d030b20b89e047e4514a76c7d475af61c2d42` | `https://static-cdn.m5stack.com/resource/docs/products/unit/nbiot_global/nbiot_global_sch_02.webp` |

---

源文档：`zh_CN/unit/nbiot_global.md`

源文档 SHA-256：`7dcbed93bb6caa02efbfd8253ee2e1573a30a833066534af3675fa314868c579`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
