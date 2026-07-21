# USB Downloader 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | USB Downloader |
| SKU | A012 |
| 产品 ID | `usb-downloader-d0bdffc696b7` |
| 源文档 | `zh_CN/tool/usb_downloader.md` |

## 概述

USB Downloader 的本地原理图采用 CP2104-F03-GM（U1）完成 USB 到 UART 转换，Type-C 的 USB_P/USB_N 经 22Ω 串联电阻和 SRV05-4-P-T7 防护网络连接 U1。VBUS 同时为 U1 和 AMS1117-3.3（VR1）供电，VR1 输出 +3.3V 至外部排针与板上电路。DTR、RTS 通过 Q1/Q2 两只 SS8050 及 10KΩ 基极电阻形成 EN/BOOT 自动下载控制，P1 集中引出 3.3V、RXD、TXD、EN、BOOT 和 GND。

## 检索关键词

`USB Downloader`、`A012`、`CP2104-F03-GM`、`CP2104`、`USB-TTL`、`Type-C`、`USB_P`、`USB_N`、`TXD`、`RXD`、`DTR`、`RTS`、`EN`、`BOOT`、`AMS1117-3.3`、`SS8050 Y1`、`SRV05-4-P-T7`、`VBUS`、`+3.3V`、`VCC_3.3V`、`Header 6`、`22Ω`、`10KΩ`、`UART`、`auto download`、`RST`、`JP1`、`JP2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | CP2104-F03-GM | USB 到 UART 转换器，提供 TXD/RXD 与 DTR/RTS 握手信号 | 图 4d9e2adb14cf / 第 1 页 / 页面中央 U1：CP2104-F03-GM，D+/D-、VBUS/REGIN/VDD/VIO、TXD/RXD/DTR/RTS 等引脚 |
| J1 | Type-C | USB Type-C 输入接口，引出 VBUS、USB_P、USB_N 和 GND | 图 4d9e2adb14cf / 第 1 页 / 页面左侧 J1 Type-C USB Port：VCC/GND、DP/DN 与 VBUS/USB_P/USB_N 网络 |
| J2 | SRV05-4-P-T7 | USB 数据线与电源相关网络的多通道瞬态保护阵列 | 图 4d9e2adb14cf / 第 1 页 / 页面左下部 J1 与 U1 之间：J2 标注 SRV05-4-P-T7，连接 USB_P/USB_N、VBUS/VCC_3.3V 与 GND |
| VR1 | AMS1117-3.3 | 将 VBUS 转换为 +3.3V 的线性稳压器 | 图 4d9e2adb14cf / 第 1 页 / 页面下部中央 VR1：AMS1117-3.3，Vin 接 VBUS，Vout 接 +3.3V，GND 接地 |
| Q1 | SS8050 Y1 | DTR/RTS 自动下载控制网络中的 EN 驱动晶体管 | 图 4d9e2adb14cf / 第 1 页 / 页面右中部 Q1：SS8050 Y1，输出网络标注 EN，基极路径含 R4 10KΩ |
| Q2 | SS8050 Y1 | DTR/RTS 自动下载控制网络中的 BOOT 驱动晶体管 | 图 4d9e2adb14cf / 第 1 页 / 页面右中部 Q2：SS8050 Y1，输出网络标注 BOOT，基极路径含 R7 10KΩ |
| P1 | Header 6 | 下载与串口调试排针，引出 +3.3V、RXD、TXD、EN、BOOT、GND | 图 4d9e2adb14cf / 第 1 页 / 页面右侧 P1 Header 6：1~6 脚依次连接 +3.3V、RXD、TXD、EN、BOOT、GND |
| R5/R6 | 22Ω | USB_P/USB_N 到 U1 D+/D- 的串联电阻 | 图 4d9e2adb14cf / 第 1 页 / 页面左中部 J1 与 U1 之间：USB_P、USB_N 两线上各有一只标注 22Ω 的 R5/R6 |
| R4/R7 | 10KΩ | Q1/Q2 自动下载控制的基极串联电阻 | 图 4d9e2adb14cf / 第 1 页 / 页面右中部：DTR 经 R4 10KΩ、RTS 经 R7 10KΩ 进入交叉晶体管网络 |
| D1/R1 | YELT 0603 / 1KΩ | VBUS 到 TXD 的发送活动指示支路 | 图 4d9e2adb14cf / 第 1 页 / 页面上部：VBUS-D1(YELT 0603)-R1(1KΩ)-TXD 串联支路 |
| D2/R2 | YELT 0603 / 1KΩ | VBUS 到 RXD 的接收活动指示支路 | 图 4d9e2adb14cf / 第 1 页 / 页面上部：VBUS-D2(YELT 0603)-R2(1KΩ)-RXD 串联支路 |
| D3/R3 | YELT 0603 / 1KΩ | +3.3V 对 GND 的电源指示支路 | 图 4d9e2adb14cf / 第 1 页 / 页面上部右侧：+3.3V-D3(YELT 0603)-R3(1KΩ)-GND 串联支路 |
| C3/C4/C5 | 100uF / 1.0uF / 100nF | AMS1117-3.3 输入输出滤波与去耦电容 | 图 4d9e2adb14cf / 第 1 页 / 页面下部 VR1 周围：C4 1.0uF 接 VBUS/GND，C3 100uF 与 C5 100nF 接 +3.3V/GND |
| C6 | 10uF | EN 对 GND 的自动复位/下载时序电容 | 图 4d9e2adb14cf / 第 1 页 / 页面右上部 Q1 输出：C6 10uF 跨接 EN 与 GND |
| C1/C2/R8 | 100nF / 10uF / 10KΩ | CP2104 的 VCC_3.3V 去耦以及 RST 上拉网络 | 图 4d9e2adb14cf / 第 1 页 / 页面中央 U1 下侧：C1 100nF、C2 10uF 接 VCC_3.3V/GND，R8 10KΩ 位于 U1 RST 与 VCC_3.3V 之间 |
| JP1/JP2 | 未标注 | DTR/TXD 与 RXD/RTS 信号对旁的两组跳线 | 图 4d9e2adb14cf / 第 1 页 / 页面中央上方 U1 的 DTR/TXD/RXD/RTS 四条网络右端：JP1 位于 DTR/TXD 对，JP2 位于 RXD/RTS 对 |

## 系统结构

### USB Downloader

J1 的 USB 数据经保护和 22Ω 串联电阻进入 U1 CP2104-F03-GM，U1 输出 UART TXD/RXD，并用 DTR/RTS 驱动 Q1/Q2 生成 EN/BOOT 自动下载控制；P1 汇总全部目标侧信号。

- 参数与网络：`usb_uart=U1 CP2104-F03-GM`；`usb_port=J1 Type-C`；`target_header=P1 Header 6`；`auto_download=DTR/RTS,Q1/Q2,EN/BOOT`；`regulator=VR1 AMS1117-3.3`
- 证据：图 4d9e2adb14cf / 第 1 页 / 整页：J1/J2/U1/VR1/Q1/Q2/P1 及 USB、UART、EN、BOOT、电源网络

## 核心器件

### U1 CP2104-F03-GM USB/电源侧

U1 的 D+、D- 接 USB_P、USB_N；VBUS/REGIN 接 VBUS，VIO/VDD 使用 VCC_3.3V，多个 GND/EPAD 引脚接地。

- 参数与网络：`usb=D+ USB_P,D- USB_N`；`input_power=VBUS,REGIN to VBUS`；`logic_power=VIO,VDD to VCC_3.3V`；`ground=GND,EPAD`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面中央 U1 左侧和下侧：D+/D-、VBUS/REGIN、VIO/VDD、GND/EPAD 引脚与网络

### U1 USB-TTL 芯片版本

该本地原理图页面的 U1 明确标注为 CP2104-F03-GM。

- 参数与网络：`reference=U1`；`part_number=CP2104-F03-GM`；`schematic_asset=page 1`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面中央 U1 元件下方型号文字 CP2104-F03-GM

## 电源

### VR1 AMS1117-3.3

VR1 的 Vin 接 VBUS，Vout 输出 +3.3V，GND 接地；C4 1.0uF 位于输入侧，C3 100uF 和 C5 100nF 位于输出侧。

- 参数与网络：`input=VBUS`；`output=+3.3V`；`input_capacitor=C4 1.0uF`；`output_capacitors=C3 100uF,C5 100nF`；`ground=GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面下部中央 VR1 与 C3/C4/C5：VBUS、+3.3V、GND 连接

### +3.3V 指示支路

+3.3V 经 D3 YELT 0603 和 R3 1KΩ 串联到 GND。

- 参数与网络：`supply=+3.3V`；`led=D3 YELT 0603`；`resistor=R3 1KΩ`；`return=GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面上部右侧：+3.3V-D3-R3-GND 竖直串联支路

## 接口

### J1 Type-C USB Port

J1 引出 VBUS、USB_P、USB_N 和 GND；USB_P、USB_N 分别经 22Ω 串联电阻连接 U1 的 D+、D-。

- 参数与网络：`power=VBUS`；`data_positive=USB_P via 22Ω to U1 D+`；`data_negative=USB_N via 22Ω to U1 D-`；`return=GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面左侧 J1 至 U1：VBUS/GND、USB_P/USB_N、R5/R6 22Ω 与 U1 D+/D-

### P1 Header 6

P1 的 1 脚接 +3.3V，2 脚接 RXD，3 脚接 TXD，4 脚接 EN，5 脚接 BOOT，6 脚接 GND。

- 参数与网络：`pin_1=+3.3V`；`pin_2=RXD`；`pin_3=TXD`；`pin_4=EN`；`pin_5=BOOT`；`pin_6=GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面右侧 P1 Header 6：1~6 脚数字与 +3.3V/RXD/TXD/EN/BOOT/GND 网络

## 总线

### U1 UART/握手信号

U1 引出 TXD、RXD、DTR 和 RTS 网络；TXD/RXD 连接 P1，DTR/RTS 进入 Q1/Q2 自动下载控制网络。

- 参数与网络：`uart_tx=TXD`；`uart_rx=RXD`；`handshake_1=DTR`；`handshake_2=RTS`；`target=P1 and auto-download circuit`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面中央 U1 上侧 DTR/TXD/RXD/RTS 网络及右侧 Q1/Q2、P1 同名连接

## 复位

### EN/BOOT 自动下载控制

DTR 经 R4 10KΩ、RTS 经 R7 10KΩ 驱动 Q1/Q2 交叉晶体管网络，输出 EN 和 BOOT；C6 10uF 从 EN 接 GND。

- 参数与网络：`control_inputs=DTR,RTS`；`base_resistors=R4 10KΩ,R7 10KΩ`；`transistors=Q1/Q2 SS8050 Y1`；`outputs=EN,BOOT`；`en_capacitor=C6 10uF to GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面右中部：DTR-R4-Q1/Q2、RTS-R7-Q1/Q2 的交叉连线及 EN/BOOT/C6

### U1 RST

U1 的 RST 引脚通过 R8 10KΩ 连接 VCC_3.3V。

- 参数与网络：`reference=U1`；`reset_pin=RST`；`pullup=R8 10KΩ`；`rail=VCC_3.3V`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面中央 U1 下侧 RST 引脚、R8 10KΩ 与 VCC_3.3V 网络

## 保护电路

### J2 SRV05-4-P-T7

J2 SRV05-4-P-T7 连接 USB_P、USB_N、VBUS/VCC_3.3V 与 GND，位于 Type-C 接口和 U1 之间。

- 参数与网络：`device=SRV05-4-P-T7`；`protected_signals=USB_P,USB_N`；`power_references=VBUS,VCC_3.3V`；`ground=GND`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面左下部 J2：SRV05-4-P-T7 的 I/O、电源和 GND 引脚连接

## 关键网络

### 目标侧下载信号

目标侧 P1 同时提供 UART 数据通道 RXD/TXD、下载控制 EN/BOOT、+3.3V 与 GND，所有网络均直接来自 U1、自动下载电路或 VR1。

- 参数与网络：`data=RXD,TXD`；`control=EN,BOOT`；`power=+3.3V,GND`；`connector=P1 Header 6`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面右侧 P1 与页面中央/下部 U1、Q1/Q2、VR1 的同名网络

## 调试与烧录

### TXD/RXD 活动指示

VBUS 经 D1 与 R1 1KΩ 接 TXD，另一路经 D2 与 R2 1KΩ 接 RXD；D1、D2 均标注 YELT 0603。

- 参数与网络：`tx_indicator=VBUS-D1 YELT 0603-R1 1KΩ-TXD`；`rx_indicator=VBUS-D2 YELT 0603-R2 1KΩ-RXD`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面上部 D1/R1 与 D2/R2 两条 VBUS 至 TXD/RXD 指示支路

### JP1/JP2 跳线

原理图在 U1 的 DTR/TXD 与 RXD/RTS 信号对右侧分别绘出 JP1 和 JP2。

- 参数与网络：`jp1_signal_pair=DTR,TXD`；`jp2_signal_pair=RXD,RTS`；`references=JP1,JP2`
- 证据：图 4d9e2adb14cf / 第 1 页 / 页面中央上方：DTR/TXD/RXD/RTS 四条网络右端的 JP1、JP2 标号与跳线符号

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | USB Downloader | `usb_uart=U1 CP2104-F03-GM`；`usb_port=J1 Type-C`；`target_header=P1 Header 6`；`auto_download=DTR/RTS,Q1/Q2,EN/BOOT`；`regulator=VR1 AMS1117-3.3` |
| 接口 | J1 Type-C USB Port | `power=VBUS`；`data_positive=USB_P via 22Ω to U1 D+`；`data_negative=USB_N via 22Ω to U1 D-`；`return=GND` |
| 保护电路 | J2 SRV05-4-P-T7 | `device=SRV05-4-P-T7`；`protected_signals=USB_P,USB_N`；`power_references=VBUS,VCC_3.3V`；`ground=GND` |
| 核心器件 | U1 CP2104-F03-GM USB/电源侧 | `usb=D+ USB_P,D- USB_N`；`input_power=VBUS,REGIN to VBUS`；`logic_power=VIO,VDD to VCC_3.3V`；`ground=GND,EPAD` |
| 总线 | U1 UART/握手信号 | `uart_tx=TXD`；`uart_rx=RXD`；`handshake_1=DTR`；`handshake_2=RTS`；`target=P1 and auto-download circuit` |
| 接口 | P1 Header 6 | `pin_1=+3.3V`；`pin_2=RXD`；`pin_3=TXD`；`pin_4=EN`；`pin_5=BOOT`；`pin_6=GND` |
| 电源 | VR1 AMS1117-3.3 | `input=VBUS`；`output=+3.3V`；`input_capacitor=C4 1.0uF`；`output_capacitors=C3 100uF,C5 100nF`；`ground=GND` |
| 复位 | EN/BOOT 自动下载控制 | `control_inputs=DTR,RTS`；`base_resistors=R4 10KΩ,R7 10KΩ`；`transistors=Q1/Q2 SS8050 Y1`；`outputs=EN,BOOT`；`en_capacitor=C6 10uF to GND` |
| 调试与烧录 | TXD/RXD 活动指示 | `tx_indicator=VBUS-D1 YELT 0603-R1 1KΩ-TXD`；`rx_indicator=VBUS-D2 YELT 0603-R2 1KΩ-RXD` |
| 电源 | +3.3V 指示支路 | `supply=+3.3V`；`led=D3 YELT 0603`；`resistor=R3 1KΩ`；`return=GND` |
| 关键网络 | 目标侧下载信号 | `data=RXD,TXD`；`control=EN,BOOT`；`power=+3.3V,GND`；`connector=P1 Header 6` |
| 核心器件 | U1 USB-TTL 芯片版本 | `reference=U1`；`part_number=CP2104-F03-GM`；`schematic_asset=page 1` |
| 复位 | U1 RST | `reference=U1`；`reset_pin=RST`；`pullup=R8 10KΩ`；`rail=VCC_3.3V` |
| 调试与烧录 | JP1/JP2 跳线 | `jp1_signal_pair=DTR,TXD`；`jp2_signal_pair=RXD,RTS`；`references=JP1,JP2` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4d9e2adb14cf3115311f98b79d3790b0b0ad45efb6a2ed62f0a1730ba6247932` | `https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_sch_01.webp` |

---

源文档：`zh_CN/tool/usb_downloader.md`

源文档 SHA-256：`ed4f8f73c6c30ac316f3097e6560578564f2fa85cd665a31851960d928adb72e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
