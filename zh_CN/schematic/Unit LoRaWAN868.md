# Unit LoRaWAN868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaWAN868 |
| SKU | U117 |
| 产品 ID | `unit-lorawan868-9340b4ba3b1b` |
| 源文档 | `zh_CN/unit/lorawan868.md` |

## 概述

Unit LoRaWAN868 以 M1 Ra-07/Ra-07H 无线模组为核心，通过 UTX/URX UART 与 J1 HY-2.0_UART 通信。VR1 AMS1117-3.3 将 J1 的 +5V 转换为 +3.3V，供 M1 使用；SWCLK、SWDIO、RESET 和电源地分别引出到 JP1-JP5。M1 ANT 引脚 18 经 R4 0 Ω 连接 E1 ANT_IPEX，页面另列 R1/R2/R3 0 Ω 对应 470/868/915 的频段版本选型表。

## 检索关键词

`Unit LoRaWAN868`、`U117`、`Ra-07`、`Ra-07H`、`ASR6501`、`AMS1117-3.3`、`LoRaWAN`、`868MHz`、`UART`、`115200bps`、`UTX`、`URX`、`UTXD`、`URXD`、`R5 22Ω`、`R6 22Ω`、`ANT`、`ANT_IPEX`、`IPEX`、`R4 0Ω`、`SWCLK`、`SWDIO`、`RESET`、`JP1`、`JP2`、`JP3`、`JP4`、`JP5`、`+5V`、`+3.3V`、`470`、`868`、`915`、`R1`、`R2`、`R3`、`LoRaWAN v1.0.1`、`+21dBm`、`-137dBm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | Ra-07/Ra-07H | UART 接口 LoRaWAN 无线模组 | 图 900b529b827b / 第 1 页 / 页 1 中部 M1 器件框下方标注 Ra-07/Ra-07H |
| VR1 | AMS1117-3.3 | +5V 至 +3.3V 线性稳压器 | 图 900b529b827b / 第 1 页 / 页 1 左上 VR1 标注 AMS1117-3.3，Vin/Vout 接 +5V/+3.3V |
| J1 | HY-2.0_UART | UART 与 +5V 主机接口 | 图 900b529b827b / 第 1 页 / 页 1 右侧 J1 标注 HY-2.0_UART，针脚为 RX、TX、VCC、GND |
| E1 | ANT_IPEX | LoRaWAN 射频天线连接器 | 图 900b529b827b / 第 1 页 / 页 1 中右 E1 标注 ANT_IPEX，经 R4 连接 M1 ANT |
| JP1-JP5 | test/jumper pads | 3.3V、GND、SWCLK、SWDIO、RESET 调试引出点 | 图 900b529b827b / 第 1 页 / 页 1 左中 JP1-JP5，依次连接 +3.3V、GND、SWC、SWD、RESET |

## 系统结构

### M1 LoRaWAN 模组

M1 的器件值为 Ra-07/Ra-07H，具有 UART、SWD、RESET、AUX、ADC、模式/通用 IO 和 ANT 引脚。

- 参数与网络：`reference=M1`；`part_number=Ra-07/Ra-07H`；`host_bus=UART`；`debug=SWCLK,SWDIO`；`reset=RESET`；`rf_pin=ANT`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 型号及左右两侧完整引脚列表

## 核心器件

### M1 其他 IO

M1 还标出 ADC pin 2、AUX pin 3、SETA pin 4、DIO3 pin 5、SETB pin 6、P07 pin 15、P06 pin 14、P01 pin 13、P00 pin 12；这些网络未引出到 J1。

- 参数与网络：`other_pins=ADC/2,AUX/3,SETA/4,DIO3/5,SETB/6,P07/15,P06/14,P01/13,P00/12`；`host_connector=J1 UART only`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 左右两侧除 UART/SWD/RESET/ANT 外的 IO 引脚列表

## 电源

### VR1 3.3V 稳压

VR1 AMS1117-3.3 的 Vin 接 +5V、Vout 输出 +3.3V、GND 接地。

- 参数与网络：`reference=VR1`；`part_number=AMS1117-3.3`；`input_rail=+5V`；`output_rail=+3.3V`；`ground=GND`
- 证据：图 900b529b827b / 第 1 页 / 页 1 左上 VR1 Vin/Vout/GND 与 +5V/+3.3V 网络

### VR1 输入输出电容

C1、C2 均为 22 uF，分别连接在 VR1 的 +5V 输入、+3.3V 输出与 GND 之间。

- 参数与网络：`input_capacitor=C1 22uF`；`output_capacitor=C2 22uF`
- 证据：图 900b529b827b / 第 1 页 / 页 1 左上 VR1 两侧 C1/C2 22uF

### M1 供电

M1 VCC 引脚 9 连接 +3.3V，GND 引脚 1 与 17 接地；C4 100 nF、C5 10 uF、C6 33 pF 并联在 +3.3V 与 GND 之间。

- 参数与网络：`supply=VCC/pin 9/+3.3V`；`ground_pins=1,17`；`decoupling=C4 100nF,C5 10uF,C6 33pF`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 VCC/GND 引脚与左下 C4/C5/C6 去耦网络

## 接口

### J1 UART 接口

J1 的 1 至 4 脚依次为 RX、TX、VCC、GND；外部网络分别为 UTXD、URXD、+5V、GND。

- 参数与网络：`reference=J1`；`pinout=1:UTXD/RX,2:URXD/TX,3:+5V/VCC,4:GND`；`module_tx_direction=M1 to J1 pin 1`；`module_rx_direction=J1 pin 2 to M1`
- 证据：图 900b529b827b / 第 1 页 / 页 1 右侧 J1 脚号、内部 RX/TX/VCC/GND 与外部 UTXD/URXD/+5V/GND

## 总线

### M1 与 J1 UART

M1 UTX 引脚 11 经 R5 22 Ω 连接 UTXD 和 J1 pin 1；M1 URX 引脚 10 经 R6 22 Ω 连接 URXD 和 J1 pin 2。

- 参数与网络：`tx_path=M1 UTX/pin 11 -> R5 22ohm -> UTXD -> J1 pin 1`；`rx_path=J1 pin 2 -> URXD -> R6 22ohm -> M1 URX/pin 10`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 UTX/URX pin 11/10、R5/R6 22Ω 与 J1 UTXD/URXD 网络

## 复位

### M1 RESET

M1 RES 引脚 16 连接 RESET 网络，并引出到 JP5。

- 参数与网络：`reset_pin=M1 RES/pin 16`；`network=RESET`；`test_pad=JP5`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 右侧 RES pin 16 的 RESET 网络与左侧 JP5

## 保护电路

### 接口与电源保护

本页未显示 TVS/ESD、保险丝、反接保护、负载开关或天线浪涌保护器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`rf_surge_protection_visible=false`
- 证据：图 900b529b827b / 第 1 页 / 页 1 全图仅含稳压、模组、UART、调试与 R4 天线连接

## 射频

### M1 至 E1 天线路径

M1 ANT 引脚 18 经 R4 0 Ω 串联连接 E1 ANT_IPEX，E1 屏蔽端接 GND。

- 参数与网络：`rf_source=M1 ANT/pin 18`；`series_link=R4 0ohm`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=R4 only`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 ANT pin 18、R4 0Ω 与 E1 ANT_IPEX 连线

## 调试与烧录

### JP1-JP5 调试引出

JP1 连接 +3.3V，JP2 连接 GND，JP3 连接 SWC，JP4 连接 SWD，JP5 连接 RESET。

- 参数与网络：`JP1=+3.3V`；`JP2=GND`；`JP3=SWC`；`JP4=SWD`；`JP5=RESET`
- 证据：图 900b529b827b / 第 1 页 / 页 1 左中 JP1-JP5 与各自右侧网络标签

### M1 SWD

M1 SWCLK 引脚 7 连接 SWC/JP3，SWDIO 引脚 8 连接 SWD/JP4。

- 参数与网络：`swclk=M1 SWCLK/pin 7 -> SWC -> JP3`；`swdio=M1 SWDIO/pin 8 -> SWD -> JP4`
- 证据：图 900b529b827b / 第 1 页 / 页 1 M1 左侧 SWCLK/SWDIO pins 7/8 与 JP3/JP4 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M1 LoRaWAN 模组 | `reference=M1`；`part_number=Ra-07/Ra-07H`；`host_bus=UART`；`debug=SWCLK,SWDIO`；`reset=RESET`；`rf_pin=ANT` |
| 接口 | J1 UART 接口 | `reference=J1`；`pinout=1:UTXD/RX,2:URXD/TX,3:+5V/VCC,4:GND`；`module_tx_direction=M1 to J1 pin 1`；`module_rx_direction=J1 pin 2 to M1` |
| 总线 | M1 与 J1 UART | `tx_path=M1 UTX/pin 11 -> R5 22ohm -> UTXD -> J1 pin 1`；`rx_path=J1 pin 2 -> URXD -> R6 22ohm -> M1 URX/pin 10` |
| 电源 | VR1 3.3V 稳压 | `reference=VR1`；`part_number=AMS1117-3.3`；`input_rail=+5V`；`output_rail=+3.3V`；`ground=GND` |
| 电源 | VR1 输入输出电容 | `input_capacitor=C1 22uF`；`output_capacitor=C2 22uF` |
| 电源 | M1 供电 | `supply=VCC/pin 9/+3.3V`；`ground_pins=1,17`；`decoupling=C4 100nF,C5 10uF,C6 33pF` |
| 射频 | M1 至 E1 天线路径 | `rf_source=M1 ANT/pin 18`；`series_link=R4 0ohm`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=R4 only` |
| 调试与烧录 | JP1-JP5 调试引出 | `JP1=+3.3V`；`JP2=GND`；`JP3=SWC`；`JP4=SWD`；`JP5=RESET` |
| 调试与烧录 | M1 SWD | `swclk=M1 SWCLK/pin 7 -> SWC -> JP3`；`swdio=M1 SWDIO/pin 8 -> SWD -> JP4` |
| 复位 | M1 RESET | `reset_pin=M1 RES/pin 16`；`network=RESET`；`test_pad=JP5` |
| 核心器件 | M1 其他 IO | `other_pins=ADC/2,AUX/3,SETA/4,DIO3/5,SETB/6,P07/15,P06/14,P01/13,P00/12`；`host_connector=J1 UART only` |
| 其他事实 | 470/868/915 版本选型表 | `R1=0ohm -> 470`；`R2=0ohm -> 868`；`R3=0ohm -> 915`；`current_population=null`；`circuit_connection=null` |
| 射频 | 内部芯片与 LoRaWAN 协议 | `documented_chip=ASR6501`；`documented_lorawan_version=v1.0.1`；`schematic_internal_chip=null`；`schematic_protocol_version=null` |
| 总线 | UART 参数与 AT 指令 | `documented_baud=115200`；`documented_protocol=AT commands`；`schematic_baud=null`；`schematic_command_protocol=null` |
| 射频 | 868 MHz 射频性能 | `documented_frequency_mhz=868`；`documented_rx_sensitivity_dbm=-137`；`documented_rx_condition=SF12/BW125kHz`；`documented_max_tx_dbm=21`；`schematic_rf_ratings=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`rf_surge_protection_visible=false` |

## 待确认事项

- `other.frequency_selection_table`：页面右上表格将 R1 0 Ω 对应 470、R2 0 Ω 对应 868、R3 0 Ω 对应 915，但未在主电路中画出 R1-R3 的连接或当前装配标记。（证据：图 900b529b827b / 第 1 页 / 页 1 右上 R1/R2/R3 与 470/868/915 对照表）
- `rf.internal_chip_protocol`：产品正文描述 ASR6501 和 LoRaWAN v1.0.1 协议栈，但原理图只显示 Ra-07/Ra-07H 模组外部连接，没有内部芯片或协议版本标注。（证据：图 900b529b827b / 第 1 页 / 页 1 M1 仅标注 Ra-07/Ra-07H，未出现 ASR6501 或 LoRaWAN 版本）
- `bus.uart_parameters`：产品正文标注 UART 115200 bps 并通过 AT 指令控制；原理图仅确认 UTX/URX 物理连接，没有波特率或命令协议标注。（证据：图 900b529b827b / 第 1 页 / 页 1 M1 UTX/URX 至 J1 的 UART 路径未标注速率或协议）
- `rf.performance`：产品正文标注 868 MHz、-137 dBm 最小接收灵敏度和 +21 dBm 最大发射功率；本页原理图没有这些射频额定值或测试条件。（证据：图 900b529b827b / 第 1 页 / 页 1 M1、R4 与 E1 天线路径未标注频率、灵敏度或发射功率）
- `review.frequency_selection`：U117 868 MHz 版本是否实际装配 R2 0 Ω，R1/R3 是否不装？；原因：页面仅给出版本对照表，没有在主电路显示 R1-R3 连接和装配状态。
- `review.internal_chip_protocol`：当前 Ra-07/Ra-07H 模组内部是否为 ASR6501，固件 LoRaWAN 协议栈版本是否为 v1.0.1？；原因：原理图没有模组内部芯片和固件版本信息。
- `review.uart_parameters`：当前模组固件默认 UART 是否为 115200 bps，AT 指令集版本是什么？；原因：原理图只显示 UART 物理连接。
- `review.rf_performance`：868 MHz、-137 dBm 与 +21 dBm 参数适用于哪些区域配置、扩频因子、带宽、天线和法规条件？；原因：原理图没有射频额定值或测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `900b529b827b45c2a11b2863953929fb1378fe8c54f9c34000712ddf9bc5e9d7` | `https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_sch_01.webp` |

---

源文档：`zh_CN/unit/lorawan868.md`

源文档 SHA-256：`f03105ff97079928680894deefe8da50339d535dcc49278c023a18a49f1f9df1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
