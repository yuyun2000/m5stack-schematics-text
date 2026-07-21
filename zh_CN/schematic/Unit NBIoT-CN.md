# Unit NBIoT-CN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NBIoT-CN |
| SKU | U112 |
| 产品 ID | `unit-nbiot-cn-bff1068848bb` |
| 源文档 | `zh_CN/unit/nbiot_cn.md` |

## 概述

Unit NBIoT-CN 的两张原理图由 M1 SIM7020G/SIM7020C 模组页与电源/HCore 接口页组成。M1 连接 U2 SIM 卡座、E1 ANT_IPEX、NETLIGHT LED、RESET 及两路 SS8050 UART 电平转换；J1 HCore 的 TXD/RXD/RST/VIN 跨页连接这些网络。VIN 经 U3 JW5033H 生成 +5.4V，再由 VR1 AMS1117-3.3 生成 +3.3V，模组还输出 +1.8V；实际 SIM7020C/G 变体、Grove/SMA/Nano SIM 结构、频段、协议与性能需结合 U112 BOM、模组资料或实测确认。

## 检索关键词

`Unit NBIoT-CN`、`U112`、`SIM7020C`、`SIM7020G`、`NB-IoT`、`Cat-NB`、`JW5033H`、`AMS1117-3.3`、`HCore`、`UART1_TXD`、`UART1_RXD`、`U1_TX`、`U1_RX`、`M_TXD`、`M_RXD`、`NB_TX`、`NB_RX`、`RESET`、`RST`、`NETLIGHT`、`SIM_VCC`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SMF05CT1G`、`ANT_IPEX`、`E1`、`VIN`、`+5.4V`、`+3.3V`、`+1.8V`、`Nano SIM`、`SMA antenna`、`B1`、`B3`、`B5`、`B8`、`115200bps`、`AT command`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7020G/SIM7020C | NB-IoT 通信模组，连接 UART、SIM、复位、NETLIGHT、VBAT、1.8V 输出和 IPEX 天线 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页中央：M1 SIM7020G/SIM7020C pins1-42 |
| U2 | SIM | 连接 SIM_VCC、IO、CLK、RST 与 GND 的 SIM 卡座 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页左中：U2 SIM pins1/2/3/5/6/7 |
| U1 | SMF05CT1G | SIM_DATA/SIM_CLK/SIM_RST/SIM_VCC 接口的多通道 ESD 保护阵列 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页左中：U1 SMF05CT1G 位于 SIM 卡与 M1 之间 |
| E1 | ANT_IPEX | 连接 M1 ANT pin32 的蜂窝射频天线接口 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页中右：M1 ANT pin32 至 E1 ANT_IPEX |
| Q1,D1 | SS8050 Y1 / 0603 LED | 由 M1 NETLIGHT 控制的网络状态 LED 低侧驱动 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页右上：NETLIGHT-R2/Q1 与 +3.3V-R1-D1 |
| Q2,Q3 | SS8050 Y1 | M_RXD/M_TXD 与 U1_RX/U1_TX 之间的双路 3.3V/1.8V UART 晶体管转换网络 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页右下：Q2/Q3 与 R8-R13、NB_RX/NB_TX/U1_RX/U1_TX |
| U3 | JW5033H | 由 VIN 生成 +5.4V 的开关转换器 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页左上：U3 JW5033H、L1、R15/R16/R18 与 VIN/+5.4V |
| VR1 | AMS1117-3.3 | 将 +5.4V 线性稳压为 +3.3V | 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页上中：VR1 AMS1117-3.3 与 +5.4V/+3.3V |
| J1 | HCore | 23 针主机接口；本页实际连接 TXD、RXD、RST、VIN 与 GND | 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页右下：J1 HCore pins1-23 |
| Q4 | SS8050 Y1 | J1 RST 到 M1 RESET 的晶体管复位转换器 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页右上：RST-R17-Q4-RESET 与 R14/C10 |
| R5,R6,R7 | 22Ω / 22Ω / 22Ω | SIM IO、CLK、RST 三条信号的串联电阻 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 U2 至 M1 SIM_DATA/SIM_CLK/SIM_RST 的 R5/R6/R7 |
| R4 | 0Ω | M1 PWRKEY pin39 到 GND 的 0Ω 绑带 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 PWRKEY pin39 经 R4 0Ω 接 GND |
| C11,C12 | 100uF / 100uF | +3.3V 模组电源的大容量并联储能电容 | 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页中部：C11/C12 各 100uF 从 +3.3V 到 GND |
| C2,C3,C4,C13 | 33pF / 33pF / 33pF / 1uF | SIM 信号 EMI 滤波与 SIM_VCC 去耦 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 U2 附近 C2/C3/C4 33pF 与 C13 1uF |
| C1 | 22uF | M1 VDD_EXT 输出的 +1.8V 去耦电容 | 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页右中：M1 VDD_EXT pin40、+1.8V 与 C1 22uF |

## 系统结构

### Unit NBIoT-CN 系统结构

资源 1 展示 M1 蜂窝模组、SIM、IPEX 天线、NETLIGHT 和 UART 转换；资源 2 展示 VIN->+5.4V->+3.3V 电源、RESET 转换和 HCore 主机接口。跨页网络 M_TXD/M_RXD/RST/VIN 将两部分连接。

- 参数与网络：`module=M1 SIM7020G/SIM7020C`；`sim=U2`；`antenna=E1 ANT_IPEX`；`host=J1 HCore`；`uart=Q2/Q3 level translation`；`power=VIN -> U3 +5.4V -> VR1 +3.3V`；`reset=J1 RST -> Q4 -> RESET`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页完整模组/SIM/UART/RF; 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页完整电源/RESET/HCore

## 电源

### VIN 至 +5.4V 转换

VIN 接 U3 JW5033H VIN pin3，EN pin5 经 R15 100KΩ 接 VIN；SW pin2 经 L1 4.7uH 输出 +5.4V，FB pin4 使用 R16 115KΩ/R18 20KΩ，C6 10uF 为输入电容、C7 22uF 为输出电容。

- 参数与网络：`input=VIN`；`converter=U3 JW5033H`；`enable=R15 100KΩ to VIN`；`inductor=L1 4.7uH`；`output=+5.4V`；`feedback=R16 115KΩ,R18 20KΩ`；`caps=C6 10uF,C7 22uF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页左上 U3/L1/R15/R16/R18/C6/C7

### +5.4V 至 +3.3V

+5.4V 接 VR1 AMS1117-3.3 Vin，Vout 输出 +3.3V；C8 100nF 位于输入，C9 22uF 与 C11/C12 各 100uF 位于 3.3V 侧。

- 参数与网络：`input=+5.4V`；`regulator=VR1 AMS1117-3.3`；`output=+3.3V`；`input_cap=C8 100nF`；`output_caps=C9 22uF,C11/C12 100uF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页上中 VR1/C8/C9 与中部 C11/C12

### M1 VBAT 与 1.8V 输出

M1 VBAT pins34/35 连接 +3.3V，VDD_EXT pin40 输出 +1.8V 并由 C1 22uF 去耦；PWRKEY pin39 经 R4 0Ω 接 GND。

- 参数与网络：`vbat=M1 pins34/35 +3.3V`；`vdd_ext=M1 pin40 +1.8V`；`vdd_ext_cap=C1 22uF`；`pwrkey=M1 pin39 via R4 0Ω to GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 pins34/35/39/40 与 +3.3V/+1.8V/R4/C1

## 接口

### J1 HCore 已连接引脚

J1 pin6 TXD 接 M_TXD、pin7 RXD 接 M_RXD、pin10 RST 接 RST、pins11/12 接 GND、pins13/14 接 VIN；其余符号引脚在本页无外部连线。

- 参数与网络：`pin6=TXD M_TXD`；`pin7=RXD M_RXD`；`pin10=RST`；`pins11_12=GND`；`pins13_14=VIN`；`connector=HCore`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页右下 J1 HCore pins1-23

### U2 SIM 卡接口

U2 pin1 VCC 接 SIM_VCC，pin2 RST 经 R7 22Ω 接 SIM_RST，pin3 CLK 经 R6 22Ω 接 SIM_CLK，pin7 IO 经 R5 22Ω 接 SIM_DATA，pin5 GND 接地，pin6 VPP 未接功能网络。

- 参数与网络：`pin1=SIM_VCC`；`pin2=SIM_RST via R7 22Ω`；`pin3=SIM_CLK via R6 22Ω`；`pin7=SIM_DATA via R5 22Ω`；`pin5=GND`；`pin6=VPP`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 U2 SIM 与 R5-R7

## 总线

### 主机与模组 UART 转换

M_RXD/NB_RX 与 U1_RX 之间使用 Q2 SS8050 及 R8/R9/R10 各 4.7KΩ，M_TXD/NB_TX 与 U1_TX 之间使用 Q3 及 R11/R12/R13 各 4.7KΩ；左侧网络上拉 +3.3V，右侧网络上拉 +1.8V。

- 参数与网络：`channel_rx=M_RXD/NB_RX <-> Q2 <-> U1_RX`；`channel_tx=M_TXD/NB_TX <-> Q3 <-> U1_TX`；`host_rail=+3.3V via R9/R12`；`module_rail=+1.8V via R8/R10/R11/R13`；`transistors=Q2,Q3 SS8050 Y1`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页右下两组 UART 电平转换; 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页 J1 M_TXD/M_RXD

### M1 UART1 映射

M1 UART1_TXD pin1 连接 U1_TX，UART1_RXD pin2 连接 U1_RX；UART1_RTS/CTS/DCD/DTR/RI pins3-7 未接外部网络，UART2_RXD/TXD pins23/22 也未接。

- 参数与网络：`tx=M1 pin1 U1_TX`；`rx=M1 pin2 U1_RX`；`uart1_flow_control=pins3-7 NC`；`uart2=pins22/23 NC`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 UART1/UART2 pins1-7/22/23

## GPIO 与控制信号

### NETLIGHT 状态灯

M1 NETLIGHT pin41 经 R2 1KΩ 驱动 Q1 SS8050，R3 10KΩ 下拉控制节点；Q1 低侧控制 +3.3V-R1 1KΩ-D1 0603 LED 支路。

- 参数与网络：`module_pin=M1 NETLIGHT pin41`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=+3.3V -> R1 1KΩ -> D1 -> Q1 -> GND`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页右上 NETLIGHT/R1-R3/D1/Q1

### M1 未使用外部接口

M1 ADC、GPIO0、RTC_GPIO、RTC_EINT、SIM_DET、GPIO1、USB_DM/DP/VBUS、UART2_RXD/TXD 以及 UART1 流控脚在本页标为未连接；STATUS pin42 也未接外部电路。

- 参数与网络：`unused=ADC,GPIO0,RTC_GPIO,RTC_EINT,SIM_DET,GPIO1,USB_DM,USB_DP,USB_VBUS,UART2_RXD,UART2_TXD,UART1 flow-control,STATUS`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 全部红色 NC 标记

## 复位

### 主机 RST 到模组 RESET

J1 RST pin10 经 R17 1KΩ 驱动 Q4 SS8050，Q4 控制 RESET 网络；RESET 由 R14 10KΩ 上拉到 +3.3V、C10 100nF 对地，并连接 M1 RESET pin28。

- 参数与网络：`host=J1 pin10 RST`；`series=R17 1KΩ`；`transistor=Q4 SS8050 Y1`；`module_net=RESET -> M1 pin28`；`pullup=R14 10KΩ`；`cap=C10 100nF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页右上 RESET/Q4/R14/R17/C10 与 J1 RST; 图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 RESET pin28

## 保护电路

### SIM ESD 与滤波

U1 SMF05CT1G 位于 SIM 卡与 M1 之间，为 SIM_DATA/SIM_CLK/SIM_RST/SIM_VCC 提供保护；C2/C3/C4 各 33pF 将三条 SIM 信号对地滤波，C13 1uF 为 SIM_VCC 去耦。

- 参数与网络：`esd_array=U1 SMF05CT1G`；`protected_nets=SIM_DATA,SIM_CLK,SIM_RST,SIM_VCC`；`signal_caps=C2,C3,C4 33pF`；`supply_cap=C13 1uF`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 U1/U2/C2-C4/C13 SIM 区

## 内存与 Flash

### 模组内部时钟与存储

两张板级原理图只显示 M1 模组外部引脚，没有展开内部基带、Flash/RAM、晶振或时钟网络，因此无法从图中确认存储容量、时钟频率或固件存储结构。

- 参数与网络：`module=M1 SIM7020G/SIM7020C`；`internal_baseband=null`；`flash=null`；`ram=null`；`crystal=null`；`clock_frequency=null`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 仅为模块级符号

## 射频

### 蜂窝天线路径

M1 ANT pin32 直接连接 E1 ANT_IPEX 中心端，E1 地端接 GND；本页未显示外部 LC 匹配、射频开关、功放或天线检测网络。

- 参数与网络：`source=M1 ANT pin32`；`connector=E1 ANT_IPEX`；`ground=GND`；`external_matching_shown=false`；`rf_switch_shown=false`；`external_pa_shown=false`
- 证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 pin32 ANT 至 E1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NBIoT-CN 系统结构 | `module=M1 SIM7020G/SIM7020C`；`sim=U2`；`antenna=E1 ANT_IPEX`；`host=J1 HCore`；`uart=Q2/Q3 level translation`；`power=VIN -> U3 +5.4V -> VR1 +3.3V`；`reset=J1 RST -> Q4 -> RESET` |
| 电源 | VIN 至 +5.4V 转换 | `input=VIN`；`converter=U3 JW5033H`；`enable=R15 100KΩ to VIN`；`inductor=L1 4.7uH`；`output=+5.4V`；`feedback=R16 115KΩ,R18 20KΩ`；`caps=C6 10uF,C7 22uF` |
| 电源 | +5.4V 至 +3.3V | `input=+5.4V`；`regulator=VR1 AMS1117-3.3`；`output=+3.3V`；`input_cap=C8 100nF`；`output_caps=C9 22uF,C11/C12 100uF` |
| 电源 | M1 VBAT 与 1.8V 输出 | `vbat=M1 pins34/35 +3.3V`；`vdd_ext=M1 pin40 +1.8V`；`vdd_ext_cap=C1 22uF`；`pwrkey=M1 pin39 via R4 0Ω to GND` |
| 接口 | J1 HCore 已连接引脚 | `pin6=TXD M_TXD`；`pin7=RXD M_RXD`；`pin10=RST`；`pins11_12=GND`；`pins13_14=VIN`；`connector=HCore` |
| 总线 | 主机与模组 UART 转换 | `channel_rx=M_RXD/NB_RX <-> Q2 <-> U1_RX`；`channel_tx=M_TXD/NB_TX <-> Q3 <-> U1_TX`；`host_rail=+3.3V via R9/R12`；`module_rail=+1.8V via R8/R10/R11/R13`；`transistors=Q2,Q3 SS8050 Y1` |
| 总线 | M1 UART1 映射 | `tx=M1 pin1 U1_TX`；`rx=M1 pin2 U1_RX`；`uart1_flow_control=pins3-7 NC`；`uart2=pins22/23 NC` |
| 复位 | 主机 RST 到模组 RESET | `host=J1 pin10 RST`；`series=R17 1KΩ`；`transistor=Q4 SS8050 Y1`；`module_net=RESET -> M1 pin28`；`pullup=R14 10KΩ`；`cap=C10 100nF` |
| 接口 | U2 SIM 卡接口 | `pin1=SIM_VCC`；`pin2=SIM_RST via R7 22Ω`；`pin3=SIM_CLK via R6 22Ω`；`pin7=SIM_DATA via R5 22Ω`；`pin5=GND`；`pin6=VPP` |
| 保护电路 | SIM ESD 与滤波 | `esd_array=U1 SMF05CT1G`；`protected_nets=SIM_DATA,SIM_CLK,SIM_RST,SIM_VCC`；`signal_caps=C2,C3,C4 33pF`；`supply_cap=C13 1uF` |
| 射频 | 蜂窝天线路径 | `source=M1 ANT pin32`；`connector=E1 ANT_IPEX`；`ground=GND`；`external_matching_shown=false`；`rf_switch_shown=false`；`external_pa_shown=false` |
| GPIO 与控制信号 | NETLIGHT 状态灯 | `module_pin=M1 NETLIGHT pin41`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=+3.3V -> R1 1KΩ -> D1 -> Q1 -> GND` |
| GPIO 与控制信号 | M1 未使用外部接口 | `unused=ADC,GPIO0,RTC_GPIO,RTC_EINT,SIM_DET,GPIO1,USB_DM,USB_DP,USB_VBUS,UART2_RXD,UART2_TXD,UART1 flow-control,STATUS` |
| 内存与 Flash | 模组内部时钟与存储 | `module=M1 SIM7020G/SIM7020C`；`internal_baseband=null`；`flash=null`；`ram=null`；`crystal=null`；`clock_frequency=null` |
| 核心器件 | SIM7020C/G 实际装配 | `documented_module=SIM7020C`；`schematic_label=SIM7020G/SIM7020C`；`asset_path_variant=nbiot_global`；`assembled_variant=null` |
| 接口 | 正文 Grove UART 与图中 HCore | `documented_connector=HY2.0-4P Grove`；`documented_pins=GND,5V,UART_RX,UART_TX`；`schematic_connector=J1 HCore`；`grove_on_page=null`；`schematic_input=VIN` |
| 接口 | Nano SIM 结构 | `documented_form_factor=Nano SIM`；`schematic_part=U2 SIM`；`socket_part_number=null`；`card_detect=null`；`orientation=null` |
| 接口 | SMA 外部天线 | `documented_connector=SMA`；`schematic_connector=E1 ANT_IPEX`；`pigtail=null`；`sma_polarity=null`；`antenna_part=null`；`gain=null` |
| 射频 | Cat-NB 频段与吞吐性能 | `documented_bands=B1,B3,B5,B8`；`documented_downlink=26.15kbps`；`documented_uplink=62.5kbps`；`schematic_bands=null`；`tx_power=null`；`sensitivity=null`；`carrier_certification=null` |
| 总线 | UART 115200 与 AT/网络协议 | `documented_baud=115200bps`；`documented_control=AT commands`；`documented_protocols=TCP,UDP,LWM2M,CoAP,MQTT,HTTP,HTTPS,TLS,DTLS,DNS,NTP,PING`；`frame_format=null`；`firmware_version=null` |
| 其他事实 | 正文认证与运营商适配 | `documented_certifications=RoHS,REACH,CCC,CTA,SRRC,Mobile,Unicom,Telecom,ATEX`；`documented_carriers=China Telecom,China Unicom,China Mobile`；`certificate_numbers=null`；`tested_revision=null` |

## 待确认事项

- `component.module-variant`：产品正文称通信模组为 SIM7020C，但原理图 M1 同时标注 SIM7020G/SIM7020C，两个资源 URL 也位于 nbiot_global 路径；本页没有 BOM 装配标记可确定 U112 实际变体。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1 下方 SIM7020G/SIM7020C）
- `interface.documented-grove`：正文将外部接口描述为四针 Grove：GND/5V/UART_RX/UART_TX；两张原理图只显示 J1 HCore 23 针接口及 VIN/M_TXD/M_RXD/RST，没有 Grove 连接器或明确 5V 输入标签。（证据：图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页唯一主机接口为 J1 HCore）
- `interface.documented-nano-sim`：正文称 SIM 卡类型为 Nano；原理图 U2 仅标 SIM 并给出电气引脚，没有卡座型号、尺寸、检测开关、插卡方向或热插拔额定信息。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 U2 仅标 SIM）
- `interface.documented-sma`：正文称集成 SMA 外部天线接口；原理图只显示 E1 ANT_IPEX，没有 SMA 连接器、IPEX-to-SMA 馈线、天线型号、极性或增益。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页唯一射频接口 E1 ANT_IPEX）
- `rf.documented-bands-performance`：正文列出中国地区 B1/B3/B5/B8，以及 26.15kbps 下行、62.5kbps 上行；原理图只确认模组和天线连接，没有频段、功率、灵敏度、吞吐、运营商或区域认证参数。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 M1/E1，无射频性能表）
- `bus.documented-at-protocols`：正文称 UART 115200bps、AT 指令，并列出 TCP/UDP/LWM2M/CoAP/MQTT/HTTP/HTTPS/TLS/DTLS/DNS/NTP/PING 等；原理图只显示 UART 电气连接，没有波特率、帧格式、固件版本或协议栈配置。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页 UART1_TXD/RXD 与转换电路，无协议文字）
- `other.documented-certifications`：正文列出 RoHS/REACH/CCC/CTA/SRRC/Mobile/Unicom/Telecom/ATEX 及中国三大运营商；原理图没有证书编号、测试版本、模组变体或认证标识，无法从电路图确认当前 U112 的认证状态。（证据：图 674520ab1fc9 / 第 1 页 / 资源 1 第 1 页无认证标识; 图 b53ff3ed62ac / 第 1 页 / 资源 2 第 1 页无认证标识）
- `review.module-variant`：请用 U112 BOM/丝印确认量产模组是 SIM7020C 还是 SIM7020G，并确认两张 global 图纸与 CN 产品的版本对应。；原因：正文与原理图变体标注不唯一。
- `review.grove-interface`：请提供 Unit 底板/HCore 转 Grove 的当前原理图或网表，确认 Grove 5V、UART_RX、UART_TX 与 J1 HCore 的映射。；原因：当前资源只显示 HCore，不显示 Grove。
- `review.nano-sim`：请用卡座 BOM/机械图确认 U2 为 Nano SIM，并确认插卡方向、检测与热插拔边界。；原因：原理图只标 SIM。
- `review.sma-assembly`：请确认 E1 IPEX 到外部 SMA 的转接结构、SMA 极性、馈线和天线型号/增益。；原因：原理图没有 SMA。
- `review.rf-bands`：请用实际 SIM7020 变体 datasheet、射频测试与运营商认证确认 B1/B3/B5/B8、上下行速率、功率和灵敏度。；原因：原理图不包含频段或性能参数。
- `review.at-protocols`：请用当前模组固件确认 UART 帧格式、115200bps、AT 版本与实际网络协议支持。；原因：硬件图只有 UART 电气连接。
- `review.certifications`：请提供与 U112 当前硬件/模组变体对应的证书编号、测试版本和运营商入网状态。；原因：原理图不能证明法规或运营商认证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `674520ab1fc99396cd26a53d743d037424bb1d228dbbd4fe7aa78aacf62b7f9b` | `https://static-cdn.m5stack.com/resource/docs/products/unit/nbiot_global/nbiot_global_sch_01.webp` |
| 2 | 1 | `b53ff3ed62accdb8f8b109383f9d030b20b89e047e4514a76c7d475af61c2d42` | `https://static-cdn.m5stack.com/resource/docs/products/unit/nbiot_global/nbiot_global_sch_02.webp` |

---

源文档：`zh_CN/unit/nbiot_cn.md`

源文档 SHA-256：`5f33963081c2aa39359ad4830f0775c3bc63b24954fb18eee52e9888906540d2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
