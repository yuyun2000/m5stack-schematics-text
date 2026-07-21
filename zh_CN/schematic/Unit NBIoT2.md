# Unit NBIoT2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NBIoT2 |
| SKU | U111-B |
| 产品 ID | `unit-nbiot2-1c4bde8307d2` |
| 源文档 | `zh_CN/unit/Unit NB-IoT2(SIM7028).md` |

## 概述

Unit NBIoT2 以 M1 SIM7028 蜂窝通信模组为核心，J1 HY-2.0_UART 通过 NB_TX/NB_RX 提供主机 UART 和 +5V 供电。U1 SY8003ADFC 与 L1 构成 +5V 至 +3.3V 降压电源，为 SIM7028 VBAT 供电。U3 SIM 卡座通过 22Ω 串联电阻、33pF 滤波电容和 U2 SMF05CT1G 防护连接模组，M1 ANT pin 32 直接连接 E1 ANT_IPEX。板上还提供 NETLIGHT 晶体管 LED、BOOT 和 UART0 测试点，但未显示独立 MCU、存储、晶振、复位电路、电池或充电器。

## 检索关键词

`Unit NBIoT2`、`U111-B`、`SIM7028`、`SY8003ADFC`、`WPN3012H2R2MT`、`SMF05CT1G`、`ANT_IPEX`、`HY-2.0_UART`、`NB_TX`、`NB_RX`、`U1_TX`、`U1_RX`、`UART1_TXD`、`UART1_RXD`、`UART0_TXD`、`UART0_RXD`、`U0T`、`U0R`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SIM_VCC`、`NETLIGHT`、`BOOT`、`+5V`、`+3.3V`、`VBAT`、`VDD_EXT`、`Nano SIM`、`NB-IoT`、`Cat-NB`、`115200bps`、`AT command`、`SMA antenna`、`R7 22Ω`、`R8 22Ω`、`R9 22Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7028 | NB-IoT 蜂窝通信模组，提供双 UART、SIM 卡、天线、状态和控制引脚 | 图 8b5fe2f09400 / 第 1 页 / 网格 B2-C3，M1 SIM7028 及 pins 1-42 的功能标注 |
| U1 | SY8003ADFC | +5V 至 +3.3V 同步降压转换器 | 图 8b5fe2f09400 / 第 1 页 / 网格 A1-A2，U1 SY8003ADFC 的 IN/EN/LX/FB/PG/VSS/PGND 引脚 |
| L1 | WPN3012H2R2MT | U1 LX 至 +3.3V 输出的降压电感 | 图 8b5fe2f09400 / 第 1 页 / 网格 A2，U1 LX pin 6 与 +3.3V 之间 L1 WPN3012H2R2MT |
| J1 | HY-2.0_UART | 四针 Grove UART 与 +5V 电源接口 | 图 8b5fe2f09400 / 第 1 页 / 网格 C4，J1 HY-2.0_UART，pin 1 RX、pin 2 TX、pin 3 VCC、pin 4 GND |
| U3 | SIM | SIM 卡座，连接 SIM_DATA、SIM_CLK、SIM_RST 和 SIM_VCC | 图 8b5fe2f09400 / 第 1 页 / 网格 C1，U3 SIM 卡座的 IO/CLK/RST/VCC/GND/VPP 引脚 |
| U2 | SMF05CT1G | SIM 卡接口多路 ESD/瞬态防护阵列 | 图 8b5fe2f09400 / 第 1 页 / 网格 B1-C2，U2 SMF05CT1G 与 SIM_VCC/SIM_DATA/SIM_CLK/SIM_RST/GND |
| E1 | ANT_IPEX | SIM7028 ANT 引脚的 IPEX 天线连接器 | 图 8b5fe2f09400 / 第 1 页 / 网格 C3，M1 ANT pin 32 到 E1 ANT_IPEX 与 GND |
| Q1,D1,R1,R2,R3 | SS8050 Y1 / 0603 / 1KΩ / 1KΩ / 10KΩ | 由 NETLIGHT 控制的 +5V LED 指示电路 | 图 8b5fe2f09400 / 第 1 页 / 网格 A4-B4，NETLIGHT、R2/R3、Q1 SS8050 Y1、D1 0603、R1 与 +5V |
| R7,R8,R9,C6,C7,C8 | 22Ω / 33pF | SIM_DATA、SIM_CLK、SIM_RST 的串联阻尼与对地滤波网络 | 图 8b5fe2f09400 / 第 1 页 / 网格 C1-C2，R7-R9 各 22Ω、C6-C8 各 33pF 与三条 SIM 信号 |

## 系统结构

### Unit NBIoT2 系统架构

单页电路由 M1 SIM7028、U1/L1 3.3V 降压电源、J1 UART Grove、U3 SIM 卡接口、E1 IPEX 天线接口、SIM 防护和 NETLIGHT 指示电路构成。

- 参数与网络：`cellular_module=M1 SIM7028`；`host_interface=J1 HY-2.0_UART`；`power=+5V -> U1 SY8003ADFC/L1 -> +3.3V`；`sim_holder=U3 SIM`；`antenna=E1 ANT_IPEX`；`status_indicator=NETLIGHT -> Q1/D1`
- 证据：图 8b5fe2f09400 / 第 1 页 / 第 1 页完整原理图，电源、M1、SIM、天线、指示和 J1 功能区

### 其他功能分区

本页未绘制独立主控或协处理器、外部存储器、晶振、音频器件、传感器、模拟采样前端、电池、充电器或负载开关；蜂窝协议、存储和时钟位于未展开内部电路的 SIM7028 模组中。

- 参数与网络：`separate_controller=false`；`coprocessor=false`；`external_memory=false`；`external_clock=false`；`audio=false`；`sensor=false`；`analog_frontend=false`；`battery=false`；`charger=false`；`load_switch=false`
- 证据：图 8b5fe2f09400 / 第 1 页 / 第 1 页网格 A1-C4 的全部器件与功能分区

## 核心器件

### M1 SIM7028 外部引脚

M1 pin 1/2 为 UART1_TXD/UART1_RXD，pins 3-7 为 UART1_RTS/CTS/DCD/DTR/RI，pin 10 为 BOOT，pins 15-18 为 SIM_DATA/SIM_CLK/SIM_RST/SIM_VDD，pins 22/23 为 UART0_TXD/UART0_RXD，pin 32 为 ANT，pins 34/35 为 VBAT，pin 40 为 VDD_EXT，pins 41/42 为 NETLIGHT/STATUS。

- 参数与网络：`uart1=1 UART1_TXD;2 UART1_RXD;3 RTS;4 CTS;5 DCD;6 DTR;7 RI`；`control=10 BOOT;11 AON_GPIO;12 WAKEUP;28 RESET;39 WAKEUP`；`sim=15 SIM_DATA;16 SIM_CLK;17 SIM_RST;18 SIM_VDD`；`uart0=22 UART0_TXD;23 UART0_RXD`；`rf=32 ANT`；`power=34/35 VBAT;40 VDD_EXT`；`status=41 NETLIGHT;42 STATUS`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B2-C3，M1 SIM7028 左右两侧 pins 1-42 名称

### M1 未连接控制与 GPIO 引脚

M1 UART1_RTS/CTS/DCD/DTR/RI pins 3-7、RESERVED pin 9、AON_GPIO pin 11、WAKEUP pin 12、GPIO1 pin 14、RESET pin 28、GPIO2 pin 29、ADC pin 38、WAKEUP pin 39 均绘有未连接标记；STATUS pin 42 未画出外部连接。

- 参数与网络：`nc_marked_pins=3,4,5,6,7,9,11,12,14,28,29,38,39`；`status_pin=42 no external connection shown`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B2-C3，M1 两侧未连接叉号及 STATUS pin 42 短线

## 电源

### +5V 至 +3.3V 降压

+5V 连接 U1 SY8003ADFC 的 IN pin 3 与 EN pin 7，LX pin 6 经 L1 WPN3012H2R2MT 输出 +3.3V；R4 68KΩ 与 R5 15KΩ 构成 FB pin 1 分压，PG pin 2 标记未连接。

- 参数与网络：`converter=U1 SY8003ADFC`；`input=+5V -> IN pin 3`；`enable=+5V -> EN pin 7`；`switch_node=LX pin 6 -> L1 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R4 68K,R5 15K -> FB pin 1`；`power_good=PG pin 2 NC`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 A1-A3，+5V、U1、L1、R4/R5、+3.3V 与 PG 未连接标记

### 降压输入输出滤波

U1 输入 +5V 由 C1 22uF 对地；输出 +3.3V 由 C3、C4 各 22uF 对地，C2 22pF 跨接在反馈上支路两端。U1 VSS/PGND pins 4、8、9 接 GND。

- 参数与网络：`input_capacitor=C1 22uF`；`output_capacitors=C3 22uF,C4 22uF`；`feedback_capacitor=C2 22pF`；`ground_pins=U1 pins 4,8,9`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 A1-A3，C1-C4、U1 接地引脚和反馈网络

### SIM7028 电源

M1 VBAT pins 34、35 连接 +3.3V；VDD_EXT pin 40 配置 C5 22uF 对地；SIM_VDD pin 18 形成 SIM_VCC 并供给 U3 卡座。

- 参数与网络：`module_vbat=+3.3V at pins 34,35`；`vdd_ext=pin 40 with C5 22uF to GND`；`sim_supply=SIM_VCC from pin 18 SIM_VDD`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B3-C3，M1 VDD_EXT/VBAT/SIM_VDD、C5、+3.3V 与 SIM_VCC

## 接口

### J1 HY-2.0_UART

J1 pin 1 标 RX 并连接 NB_TX，pin 2 标 TX 并连接 NB_RX，pin 3 VCC 连接 +5V，pin 4 GND 接地。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pinout=1:RX/NB_TX,2:TX/NB_RX,3:VCC/+5V,4:GND`；`signal_level=null`；`protection_visible=false`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 C4，J1 pins 1-4 与 NB_TX/NB_RX/+5V/GND

### U3 SIM 卡接口

M1 SIM_DATA pin 15、SIM_CLK pin 16、SIM_RST pin 17 分别经 R7、R8、R9 各 22Ω 连接 U3 IO pin 7、CLK pin 3、RST pin 2；SIM_VCC 连接 U3 VCC pin 1，U3 GND pin 5 接地，VPP pin 6 未连接。

- 参数与网络：`holder=U3 SIM`；`data=M1 pin 15 -> R7 22R -> U3 pin 7 IO`；`clock=M1 pin 16 -> R8 22R -> U3 pin 3 CLK`；`reset=M1 pin 17 -> R9 22R -> U3 pin 2 RST`；`supply=SIM_VCC -> U3 pin 1 VCC`；`ground=U3 pin 5`；`vpp=U3 pin 6 NC`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 C1-C2，U3、R7-R9 与 M1 SIM_DATA/SIM_CLK/SIM_RST/SIM_VDD

## 总线

### J1 与 SIM7028 主 UART

M1 UART1_TXD pin 1 通过 U1_TX/NB_TX 直接连接 J1 pin 1 RX；J1 pin 2 TX 通过 NB_RX/U1_RX 直接连接 M1 UART1_RXD pin 2。UART1_RTS、CTS、DCD、DTR、RI pins 3-7 均绘有未连接标记。

- 参数与网络：`module_tx=M1 pin 1 UART1_TXD/U1_TX/NB_TX -> J1 pin 1 RX`；`module_rx=J1 pin 2 TX -> NB_RX/U1_RX -> M1 pin 2 UART1_RXD`；`unused_flow_control=pins 3-7 RTS,CTS,DCD,DTR,RI NC`；`series_resistor=null`；`level_shifter=null`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B2-C4，M1 UART1 pins 1-7、NB_TX/NB_RX 与 J1 RX/TX

## GPIO 与控制信号

### NETLIGHT 指示灯

M1 NETLIGHT pin 41 经 R2 1KΩ 驱动 Q1 SS8050 Y1，R3 10KΩ 将基极网络下拉；Q1 低边控制由 +5V、R1 1KΩ 和 D1 0603 构成的 LED 支路。

- 参数与网络：`module_output=M1 pin 41 NETLIGHT`；`base_resistor=R2 1K`；`base_pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`led=D1 0603 with R1 1K`；`supply=+5V`；`topology=low-side switch`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 A4-B4，M1 NETLIGHT、R2/R3、Q1、D1、R1 和 +5V

## 复位

### M1 RESET

M1 RESET pin 28 绘有未连接标记，本页没有外部复位按键、上拉或 RC 复位网络。

- 参数与网络：`module_pin=M1 pin 28 RESET`；`external_connection=null`；`reset_button=false`；`reset_rc=false`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 C3，M1 RESET pin 28 的未连接标记

## 保护电路

### SIM 卡接口防护与滤波

U2 SMF05CT1G 连接 SIM_VCC、SIM_DATA、SIM_CLK、SIM_RST 与 GND，形成多路接口防护；SIM_DATA、SIM_CLK、SIM_RST 分别配置 C6、C7、C8 33pF 对地。

- 参数与网络：`array=U2 SMF05CT1G`；`protected_nets=SIM_VCC,SIM_DATA,SIM_CLK,SIM_RST`；`return=GND`；`signal_capacitors=C6,C7,C8 each 33pF`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B1-C2，U2 SMF05CT1G、C6-C8 与四条 SIM 网络

## 射频

### SIM7028 IPEX 天线路径

M1 ANT pin 32 直接连接 E1 ANT_IPEX 的射频端，E1 接地端连接 GND；本页未绘制外部匹配网络。

- 参数与网络：`module_pin=M1 pin 32 ANT`；`connector=E1 ANT_IPEX`；`shield=GND`；`external_matching_network=null`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 C3，M1 pin 32 ANT、E1 ANT_IPEX 与 GND

## 调试与烧录

### BOOT 与 UART0 测试点

M1 BOOT pin 10 引出到 JP4；UART0_RXD pin 23 通过 U0R 引出到 JP1，UART0_TXD pin 22 通过 U0T 引出到 JP2，JP3 接 GND。

- 参数与网络：`boot=M1 pin 10 -> JP4`；`uart0_rx=M1 pin 23 U0R -> JP1`；`uart0_tx=M1 pin 22 U0T -> JP2`；`ground=JP3`
- 证据：图 8b5fe2f09400 / 第 1 页 / 网格 B1-C3，M1 BOOT/UART0_RXD/UART0_TXD 与 JP1-JP4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NBIoT2 系统架构 | `cellular_module=M1 SIM7028`；`host_interface=J1 HY-2.0_UART`；`power=+5V -> U1 SY8003ADFC/L1 -> +3.3V`；`sim_holder=U3 SIM`；`antenna=E1 ANT_IPEX`；`status_indicator=NETLIGHT -> Q1/D1` |
| 核心器件 | M1 SIM7028 外部引脚 | `uart1=1 UART1_TXD;2 UART1_RXD;3 RTS;4 CTS;5 DCD;6 DTR;7 RI`；`control=10 BOOT;11 AON_GPIO;12 WAKEUP;28 RESET;39 WAKEUP`；`sim=15 SIM_DATA;16 SIM_CLK;17 SIM_RST;18 SIM_VDD`；`uart0=22 UART0_TXD;23 UART0_RXD`；`rf=32 ANT`；`power=34/35 VBAT;40 VDD_EXT`；`status=41 NETLIGHT;42 STATUS` |
| 电源 | +5V 至 +3.3V 降压 | `converter=U1 SY8003ADFC`；`input=+5V -> IN pin 3`；`enable=+5V -> EN pin 7`；`switch_node=LX pin 6 -> L1 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R4 68K,R5 15K -> FB pin 1`；`power_good=PG pin 2 NC` |
| 电源 | 降压输入输出滤波 | `input_capacitor=C1 22uF`；`output_capacitors=C3 22uF,C4 22uF`；`feedback_capacitor=C2 22pF`；`ground_pins=U1 pins 4,8,9` |
| 电源 | SIM7028 电源 | `module_vbat=+3.3V at pins 34,35`；`vdd_ext=pin 40 with C5 22uF to GND`；`sim_supply=SIM_VCC from pin 18 SIM_VDD` |
| 接口 | J1 HY-2.0_UART | `connector=J1 HY-2.0_UART`；`pinout=1:RX/NB_TX,2:TX/NB_RX,3:VCC/+5V,4:GND`；`signal_level=null`；`protection_visible=false` |
| 总线 | J1 与 SIM7028 主 UART | `module_tx=M1 pin 1 UART1_TXD/U1_TX/NB_TX -> J1 pin 1 RX`；`module_rx=J1 pin 2 TX -> NB_RX/U1_RX -> M1 pin 2 UART1_RXD`；`unused_flow_control=pins 3-7 RTS,CTS,DCD,DTR,RI NC`；`series_resistor=null`；`level_shifter=null` |
| 接口 | U3 SIM 卡接口 | `holder=U3 SIM`；`data=M1 pin 15 -> R7 22R -> U3 pin 7 IO`；`clock=M1 pin 16 -> R8 22R -> U3 pin 3 CLK`；`reset=M1 pin 17 -> R9 22R -> U3 pin 2 RST`；`supply=SIM_VCC -> U3 pin 1 VCC`；`ground=U3 pin 5`；`vpp=U3 pin 6 NC` |
| 保护电路 | SIM 卡接口防护与滤波 | `array=U2 SMF05CT1G`；`protected_nets=SIM_VCC,SIM_DATA,SIM_CLK,SIM_RST`；`return=GND`；`signal_capacitors=C6,C7,C8 each 33pF` |
| 射频 | SIM7028 IPEX 天线路径 | `module_pin=M1 pin 32 ANT`；`connector=E1 ANT_IPEX`；`shield=GND`；`external_matching_network=null` |
| GPIO 与控制信号 | NETLIGHT 指示灯 | `module_output=M1 pin 41 NETLIGHT`；`base_resistor=R2 1K`；`base_pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`led=D1 0603 with R1 1K`；`supply=+5V`；`topology=low-side switch` |
| 调试与烧录 | BOOT 与 UART0 测试点 | `boot=M1 pin 10 -> JP4`；`uart0_rx=M1 pin 23 U0R -> JP1`；`uart0_tx=M1 pin 22 U0T -> JP2`；`ground=JP3` |
| 复位 | M1 RESET | `module_pin=M1 pin 28 RESET`；`external_connection=null`；`reset_button=false`；`reset_rc=false` |
| 核心器件 | M1 未连接控制与 GPIO 引脚 | `nc_marked_pins=3,4,5,6,7,9,11,12,14,28,29,38,39`；`status_pin=42 no external connection shown` |
| 系统结构 | 其他功能分区 | `separate_controller=false`；`coprocessor=false`；`external_memory=false`；`external_clock=false`；`audio=false`；`sensor=false`；`analog_frontend=false`；`battery=false`；`charger=false`；`load_switch=false` |
| 接口 | SIM 卡尺寸 | `documented_sim_type=Nano SIM`；`schematic_holder=U3 SIM`；`holder_part_number=null` |
| 射频 | Cat-NB 频段、协议与数据速率 | `documented_bands=B1/B2/B3/B4/B5/B8/B12/B13/B14/B17/B18/B19/B20/B25/B26/B28/B66/B70/B85`；`documented_protocols=TCP,UDP,HTTP,TLS,DTLS,DNS,NTP,PING,LWM2M,COAP,MQTT,MQTTS,SSL`；`documented_downlink_kbps=127`；`documented_uplink_kbps=159`；`schematic_radio_specification=null` |
| 总线 | UART 参数与 AT 控制 | `documented_baud=115200`；`documented_control=AT command`；`schematic_baud=null`；`frame_format=null` |
| 射频 | 外部 SMA 天线 | `schematic_connector=E1 ANT_IPEX`；`documented_external_connector=SMA`；`adapter_or_pigtail=null` |
| 电源 | 待机与驻网电流 | `documented_supply_voltage_v=5`；`documented_standby_current_ma=3.1`；`documented_registered_current_ma=36`；`schematic_current_budget=null`；`test_conditions=null` |

## 待确认事项

- `interface.documented-sim-size`：产品正文称 SIM 卡类型为 Nano，但原理图只将 U3 标为 SIM，未标注 Nano、Micro 或卡座具体型号。（证据：图 8b5fe2f09400 / 第 1 页 / 网格 C1，U3 器件值仅标 SIM）
- `rf.documented-bands-protocols`：产品正文列出全球 Cat-NB 频段、TCP/UDP/HTTP/TLS/DTLS/DNS/NTP/PING/LWM2M/COAP/MQTT/MQTTS/SSL 协议及 127kbps 下行、159kbps 上行；原理图只确认 SIM7028 型号与外部连接，没有频段、协议栈或吞吐率标注。（证据：图 8b5fe2f09400 / 第 1 页 / 网格 B2-C3，M1 仅标 SIM7028 与外部引脚，无频段、协议或数据率文字）
- `bus.documented-uart-control`：产品正文称主 UART 使用 115200bps 并通过 AT 指令集控制；原理图只确认 UART1_TXD/UART1_RXD 物理路径，没有波特率、帧格式或 AT 指令版本。（证据：图 8b5fe2f09400 / 第 1 页 / 网格 B2-C4，M1 UART1 与 J1 RX/TX 路径，无通信参数文字）
- `rf.documented-sma-antenna`：产品正文称集成 SMA 外部天线接口并随附 SMA 天线，但原理图上的板端器件 E1 标为 ANT_IPEX，未画出 SMA 连接器或 IPEX-to-SMA 转接结构。（证据：图 8b5fe2f09400 / 第 1 页 / 网格 C3，M1 ANT pin 32 直接连接 E1 ANT_IPEX）
- `power.documented-current`：产品正文给出 DC 5V 下待机电流 3.1mA、驻网电流 36mA；原理图没有电流预算、测量点、网络状态或固件测试条件，无法由电路图独立复核。（证据：图 8b5fe2f09400 / 第 1 页 / 第 1 页 +5V、U1、+3.3V、M1 与 J1 电源路径，无电流注释）
- `review.sim-size`：当前量产 U3 卡座是否为 Nano-SIM，具体料号是什么？；原因：原理图只标 SIM，无法确定机械尺寸和卡座型号。
- `review.radio-capabilities`：请用当前 SIM7028 模组规格、固件和认证资料确认全部 Cat-NB 频段、网络协议及 127/159kbps 速率。；原因：板级原理图只显示模组型号和引脚，不包含内部协议栈、射频版本或吞吐率。
- `review.uart-control`：请用当前模组固件或 AT 手册确认默认 UART 波特率、帧格式和 AT 指令集版本。；原因：原理图只能确认 UART 电气连接，不能确认软件通信参数。
- `review.sma-antenna`：量产板如何从 E1 IPEX 连接到正文所述 SMA 接口，是否使用转接线或外壳安装座？；原因：原理图只显示 ANT_IPEX，没有 SMA 或转接结构。
- `review.power-current`：3.1mA 待机与 36mA 驻网值分别对应何种网络、信号、固件和测量条件？；原因：原理图没有电流预算或蜂窝工作状态，不能从连接关系推导实测电流。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8b5fe2f09400cd887deb74ef15b6496aa5d868abe787fe3563ff4e69b860595e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/593/Sch_UNIT-NB-IoT2_sch_01.png` |

---

源文档：`zh_CN/unit/Unit NB-IoT2(SIM7028).md`

源文档 SHA-256：`3bc8d8a09002f5382e19584bc2c6c8a7c4d9896b6985ba5b0dfb33e8aaf25ee3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
