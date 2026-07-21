# Module COMX Zigbee 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX Zigbee |
| SKU | M031-Z |
| 产品 ID | `module-comx-zigbee-02106baaddac` |
| 源文档 | `zh_CN/module/comx_zigbee.md` |

## 概述

Module COMX Zigbee 的射频子板以 M1 DRF1609H 为核心，提供 G_TXD/G_RXD UART、RESET_N、KEY、LED_DAT 和 LED_STA 信号，并由 +3.3V 供电。COMX 底板使用 U1 JW5033H 将 VIN 转换为 +5.4V，再由 VR1 AMS1117-3.3 生成 +3.3V；J1 HCore 引出 M_TXD、M_RXD、RST、VIN 和 GND。RST 经 Q1 SS8050 转换为低有效 RESET，子板另带按键、蓝/绿状态灯和电源去耦。

## 检索关键词

`Module COMX Zigbee`、`M031-Z`、`DRF1609H`、`CC2630F128`、`Zigbee`、`JW5033H`、`AMS1117-3.3`、`UART`、`G_TXD`、`G_RXD`、`M_TXD`、`M_RXD`、`TXD`、`RXD`、`RESET_N`、`RESET`、`RST`、`KEY`、`LED_DAT`、`LED_STA`、`HCore`、`VIN`、`+5.4V`、`+3.3V`、`SS8050`、`SW-PB`、`TMS`、`TCK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | DRF1609H | Zigbee 通信模块，提供 UART、复位、按键和状态 LED 信号 | 图 7150a2e3a342 / 第 1 页 / 第 1 资源页中央 M1 方框，器件值 DRF1609H，标注 TX、RX、LED_DAT、LED_STA、KEY、RESET_N、VCC、GND、TMS、TCK |
| S1 | SW-PB | M1 KEY 信号对地按键 | 图 7150a2e3a342 / 第 1 页 / 第 1 资源页右上 S1 SW-PB，连接 M1 KEY pin 4 与 GND |
| D1,R6 | 蓝灯 0603; 1KΩ | M1 LED_DAT 状态指示支路 | 图 7150a2e3a342 / 第 1 页 / 第 1 资源页左上 D1 蓝灯 0603 与 R6 1KΩ，串联连接 M1 LED_DAT pin 7 与 GND |
| D2,R7 | 绿灯 0603; 1KΩ | M1 LED_STA 状态指示支路 | 图 7150a2e3a342 / 第 1 页 / 第 1 资源页左下 D2 绿灯 0603 与 R7 1KΩ，串联连接 M1 LED_STA pin 8 与 GND |
| C7,C8 | 100nF; 10uF | M1 +3.3V 电源去耦和储能电容 | 图 7150a2e3a342 / 第 1 页 / 第 1 资源页右侧 C7 100nF、C8 10uF，并联在 M1 VCC/+3.3V 与 GND 之间 |
| U1 | JW5033H | VIN 至 +5.4V 的降压转换器 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页左上 U1 JW5033H，标注 VIN、EN、SW、BST、FB、GND 引脚 |
| VR1 | AMS1117-3.3 | +5.4V 至 +3.3V 的线性稳压器 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页上方中部 VR1 AMS1117-3.3，Vin 接 +5.4V，Vout 接 +3.3V，GND 接地 |
| L1 | 4.7uH | JW5033H 降压输出电感 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页 U1 右侧 L1 4.7uH，串联在 SW 节点与 +5.4V 之间 |
| R2,R3,R5,C1 | 100KΩ; 115KΩ; 20KΩ; 100nF | JW5033H 使能、反馈和自举网络 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页左上 U1 周围 R2 100KΩ、R3 115KΩ、R5 20KΩ、C1 100nF 与 EN/FB/BST/SW 连接 |
| C2,C3,C4,C5 | 10uF; 22uF; 100nF; 22uF | VIN、+5.4V 与 +3.3V 电源滤波电容 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页上方 C2 10uF 接 VIN，C3 22uF/C4 100nF 接 +5.4V，C5 22uF 接 +3.3V，均回到 GND |
| Q1,R1,R4,C6 | SS8050; 10KΩ; 1KΩ; 100nF | HCore RST 到 M1 RESET 的低侧复位驱动与偏置网络 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页右上 RESET/RST 区：Q1 SS8050 Y1、R1 10KΩ、R4 1KΩ、C6 100nF |
| J1 | HCore | COMX 底板到模块/主机的 23 针电源、UART、复位和辅助信号接口 | 图 6043df7de5ad / 第 1 页 / 第 2 资源页右下 J1 HCore，pin 1-23 标注 SC、SD、SR、SV、STA、TXD、RXD、RTS、PEN、RST、GND、VIN、NET、VBAT、RXD2、TXD2、DTR、RI、CTS、VTTL、VEXT |

## 系统结构

### Module COMX Zigbee 架构

第 1 资源页显示 M1 DRF1609H Zigbee 子板及 UART、复位、按键、LED 和 +3.3V 去耦；第 2 资源页显示 COMX 底板的 VIN 至 +5.4V/+3.3V 电源链、RST 复位驱动和 J1 HCore 接口。

- 参数与网络：`radio_module=M1 DRF1609H`；`module_uart=G_TXD,G_RXD`；`buck_converter=U1 JW5033H`；`ldo=VR1 AMS1117-3.3`；`rails=VIN,+5.4V,+3.3V`；`base_connector=J1 HCore`；`reset_driver=Q1 SS8050`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页完整子板电路：M1、S1、D1/D2、C7/C8; 图 6043df7de5ad / 第 1 页 / 第 2 资源页完整底板电路：U1、VR1、Q1、J1

## 电源

### U1 VIN 至 +5.4V 降压转换

U1 VIN/pin 3 接 VIN，EN/pin 5 由 R2 100KΩ 上拉至 VIN，SW/pin 2 经 L1 4.7uH 输出 +5.4V，BST/pin 6 经 C1 100nF 连接 SW 节点。

- 参数与网络：`converter=U1 JW5033H`；`input=pin 3/VIN`；`enable=pin 5/EN via R2 100KΩ to VIN`；`switch=pin 2/SW`；`inductor=L1 4.7uH`；`output=+5.4V`；`bootstrap=C1 100nF between BST pin 6 and SW`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页左上 VIN、U1 JW5033H、R2、C1、L1 与 +5.4V 路径

### U1 +5.4V 反馈网络

R3 115KΩ 从 +5.4V 连接 U1 FB/pin 4，R5 20KΩ 从 FB 连接 GND。

- 参数与网络：`upper_resistor=R3 115KΩ`；`lower_resistor=R5 20KΩ`；`feedback_pin=U1 pin 4/FB`；`sensed_rail=+5.4V`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页 U1 FB、R3 115KΩ、R5 20KΩ 与 +5.4V/GND 连接

### VR1 +3.3V 稳压

VR1 AMS1117-3.3 的 Vin 接 +5.4V，Vout 输出 +3.3V，GND 接地；C5 22uF 连接在 +3.3V 与 GND 之间。

- 参数与网络：`regulator=VR1 AMS1117-3.3`；`input_rail=+5.4V`；`output_rail=+3.3V`；`output_capacitor=C5 22uF`；`return=GND`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页上方 VR1 AMS1117-3.3、+5.4V、+3.3V、C5 与 GND

### VIN、+5.4V 与 +3.3V 滤波

C2 10uF 连接 VIN 至 GND；C3 22uF 与 C4 100nF 并联连接 +5.4V 至 GND；C5 22uF 连接 +3.3V 至 GND；子板的 C7 100nF 与 C8 10uF 并联在 +3.3V 与 GND 之间。

- 参数与网络：`vin_filter=C2 10uF`；`five4_filter=C3 22uF,C4 100nF`；`base_3v3_filter=C5 22uF`；`module_3v3_filter=C7 100nF,C8 10uF`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页上方 C2-C5 与 VIN/+5.4V/+3.3V 电源轨; 图 7150a2e3a342 / 第 1 页 / 第 1 资源页右侧 C7/C8 与 M1 +3.3V/GND

## 接口

### J1 HCore 已用针脚

J1 pin 6 TXD 连接 M_TXD，pin 7 RXD 连接 M_RXD，pin 10 RST 连接 RST，pin 11、12 连接 GND，pin 13、14 VIN 连接 VIN；其余针脚在本页无外部连线。

- 参数与网络：`reference=J1 HCore`；`used_pinout=6:TXD/M_TXD,7:RXD/M_RXD,10:RST,11:GND,12:GND,13:VIN,14:VIN`；`unused_pinout=1:SC,2:SD,3:SR,4:SV,5:STA,8:RTS,9:PEN,15:NET,16:VBAT,17:RXD2,18:TXD2,19:DTR,20:RI,21:CTS,22:VTTL,23:VEXT`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页右下 J1 HCore pin 1-23，外部蓝色连线仅见 M_TXD、M_RXD、RST、GND、VIN

## 总线

### M1 UART

M1 TX/pin 5 引出 G_TXD，RX/pin 6 引出 G_RXD；该页未标注 UART 波特率、数据位、校验位或停止位。

- 参数与网络：`controller=M1 DRF1609H`；`tx=pin 5/TX -> G_TXD`；`rx=pin 6/RX -> G_RXD`；`electrical_rail=+3.3V`；`baud_visible=false`；`frame_format_visible=false`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 左上 TX/G_TXD 与 RX/G_RXD 网络

## GPIO 与控制信号

### M1 KEY 按键

M1 KEY/pin 4 连接 S1 SW-PB，按键另一端连接 GND。

- 参数与网络：`module_pin=M1 pin 4/KEY`；`switch=S1 SW-PB`；`active_connection=GND`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页右上 M1 KEY pin 4、S1 SW-PB 与 GND

### M1 状态 LED

M1 LED_DAT/pin 7 经 R6 1KΩ 和 D1 蓝灯 0603 接 GND；LED_STA/pin 8 经 R7 1KΩ 和 D2 绿灯 0603 接 GND。

- 参数与网络：`data_led=M1 pin 7/LED_DAT -> R6 1KΩ -> D1 blue 0603 -> GND`；`status_led=M1 pin 8/LED_STA -> R7 1KΩ -> D2 green 0603 -> GND`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 LED_DAT/LED_STA 与 R6/D1、R7/D2 两条支路

## 时钟

### 外部时钟可见性

两张原理图均未绘出独立晶体、谐振器或外部振荡器；DRF1609H 内部时钟电路未展开。

- 参数与网络：`external_clock_visible=false`；`module_internal_clock_expanded=false`；`assets_checked=2`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页完整 M1 外围，无 Y/X 晶体或振荡器位号; 图 6043df7de5ad / 第 1 页 / 第 2 资源页完整底板电路，无晶体或振荡器

## 复位

### J1 RST 到 M1 RESET_N 的复位链

J1 pin 10 RST 经 R4 1KΩ 连接 Q1 SS8050 基极，Q1 发射极接 GND、集电极接 RESET；R1 10KΩ 将 RESET 上拉至 +3.3V，C6 100nF 将 RESET 接地，RESET 对应 M1 RESET_N/pin 3。

- 参数与网络：`host_reset=J1 pin 10/RST`；`base_resistor=R4 1KΩ`；`transistor=Q1 SS8050`；`module_reset_net=RESET`；`module_reset_pin=M1 pin 3/RESET_N`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C6 100nF to GND`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页右上 RST-R4-Q1-RESET-R1/C6 复位电路与右下 J1 pin 10; 图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 RESET_N pin 3 连接 RESET

## 保护电路

### VIN 与外部接口保护可见性

两张原理图未绘出 VIN 保险丝、TVS、ESD 或反接保护器件；UART、RESET 和 HCore 外部信号也未显示专用保护器件。

- 参数与网络：`vin_fuse_visible=false`；`vin_tvs_visible=false`；`reverse_protection_visible=false`；`signal_esd_visible=false`
- 证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页 VIN 输入、J1 HCore、UART 与 RST 全部外围器件区域

## 射频

### M1 DRF1609H

M1 的器件型号标注为 DRF1609H；其 VCC/pin 1 接 +3.3V，GND/pin 2 接 GND，TX/pin 5 接 G_TXD，RX/pin 6 接 G_RXD，RESET_N/pin 3 接 RESET，KEY/pin 4 接按键支路。

- 参数与网络：`reference=M1`；`part_number=DRF1609H`；`supply=pin 1/VCC -> +3.3V`；`ground=pin 2/GND`；`uart_tx=pin 5/TX -> G_TXD`；`uart_rx=pin 6/RX -> G_RXD`；`reset=pin 3/RESET_N -> RESET`；`key=pin 4/KEY`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页中央 M1 DRF1609H 全部已连接引脚与网络标注

### 天线与射频匹配网络可见性

两张原理图均未绘出天线连接器、射频匹配网络或射频走线，射频部分封装在 M1 DRF1609H 模块表示中。

- 参数与网络：`antenna_connector_visible=false`；`rf_matching_visible=false`；`rf_module=M1 DRF1609H`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 所有引脚与外围，无 RF/ANT 网络或天线位号

## 调试与烧录

### M1 TMS/TCK

M1 TMS/pin 9 与 TCK/pin 10 在第 1 资源页标为未连接，未绘出 JTAG 或其他专用调试连接器。

- 参数与网络：`tms=M1 pin 9 unconnected`；`tck=M1 pin 10 unconnected`；`debug_connector_visible=false`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 左下 TMS pin 9、TCK pin 10 旁未连接叉号

## 其他事实

### 其他功能分区可见性

两张原理图未绘出独立外部存储器、音频器件、传感器或模拟采样链路；DRF1609H 内部存储和处理器结构未展开。

- 参数与网络：`external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`；`module_internal_memory_expanded=false`
- 证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 外围仅含按键、LED 和去耦; 图 6043df7de5ad / 第 1 页 / 第 2 资源页底板仅含电源、复位与 HCore 接口

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module COMX Zigbee 架构 | `radio_module=M1 DRF1609H`；`module_uart=G_TXD,G_RXD`；`buck_converter=U1 JW5033H`；`ldo=VR1 AMS1117-3.3`；`rails=VIN,+5.4V,+3.3V`；`base_connector=J1 HCore`；`reset_driver=Q1 SS8050` |
| 射频 | M1 DRF1609H | `reference=M1`；`part_number=DRF1609H`；`supply=pin 1/VCC -> +3.3V`；`ground=pin 2/GND`；`uart_tx=pin 5/TX -> G_TXD`；`uart_rx=pin 6/RX -> G_RXD`；`reset=pin 3/RESET_N -> RESET`；`key=pin 4/KEY` |
| 核心器件 | DRF1609H 内部主芯片 | `documented_chip=CC2630F128`；`schematic_module=M1 DRF1609H`；`internal_chip_visible=false` |
| 总线 | M1 UART | `controller=M1 DRF1609H`；`tx=pin 5/TX -> G_TXD`；`rx=pin 6/RX -> G_RXD`；`electrical_rail=+3.3V`；`baud_visible=false`；`frame_format_visible=false` |
| 接口 | J1 HCore 已用针脚 | `reference=J1 HCore`；`used_pinout=6:TXD/M_TXD,7:RXD/M_RXD,10:RST,11:GND,12:GND,13:VIN,14:VIN`；`unused_pinout=1:SC,2:SD,3:SR,4:SV,5:STA,8:RTS,9:PEN,15:NET,16:VBAT,17:RXD2,18:TXD2,19:DTR,20:RI,21:CTS,22:VTTL,23:VEXT` |
| 接口 | M5-Bus 到 Zigbee UART 的选择路由 | `module_uart_nets=G_TXD,G_RXD`；`hcore_uart_nets=M_TXD,M_RXD`；`m5bus_connector_visible=false`；`selector_switch_visible=false`；`cross_connection_visible=false` |
| 电源 | U1 VIN 至 +5.4V 降压转换 | `converter=U1 JW5033H`；`input=pin 3/VIN`；`enable=pin 5/EN via R2 100KΩ to VIN`；`switch=pin 2/SW`；`inductor=L1 4.7uH`；`output=+5.4V`；`bootstrap=C1 100nF between BST pin 6 and SW` |
| 电源 | U1 +5.4V 反馈网络 | `upper_resistor=R3 115KΩ`；`lower_resistor=R5 20KΩ`；`feedback_pin=U1 pin 4/FB`；`sensed_rail=+5.4V` |
| 电源 | VR1 +3.3V 稳压 | `regulator=VR1 AMS1117-3.3`；`input_rail=+5.4V`；`output_rail=+3.3V`；`output_capacitor=C5 22uF`；`return=GND` |
| 电源 | VIN、+5.4V 与 +3.3V 滤波 | `vin_filter=C2 10uF`；`five4_filter=C3 22uF,C4 100nF`；`base_3v3_filter=C5 22uF`；`module_3v3_filter=C7 100nF,C8 10uF` |
| 电源 | VIN 输入电压范围 | `documented_range=5-12V`；`schematic_range_visible=false`；`confirmed_range=null` |
| 复位 | J1 RST 到 M1 RESET_N 的复位链 | `host_reset=J1 pin 10/RST`；`base_resistor=R4 1KΩ`；`transistor=Q1 SS8050`；`module_reset_net=RESET`；`module_reset_pin=M1 pin 3/RESET_N`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C6 100nF to GND` |
| GPIO 与控制信号 | M1 KEY 按键 | `module_pin=M1 pin 4/KEY`；`switch=S1 SW-PB`；`active_connection=GND` |
| GPIO 与控制信号 | M1 状态 LED | `data_led=M1 pin 7/LED_DAT -> R6 1KΩ -> D1 blue 0603 -> GND`；`status_led=M1 pin 8/LED_STA -> R7 1KΩ -> D2 green 0603 -> GND` |
| 调试与烧录 | M1 TMS/TCK | `tms=M1 pin 9 unconnected`；`tck=M1 pin 10 unconnected`；`debug_connector_visible=false` |
| 时钟 | 外部时钟可见性 | `external_clock_visible=false`；`module_internal_clock_expanded=false`；`assets_checked=2` |
| 射频 | 天线与射频匹配网络可见性 | `antenna_connector_visible=false`；`rf_matching_visible=false`；`rf_module=M1 DRF1609H` |
| 保护电路 | VIN 与外部接口保护可见性 | `vin_fuse_visible=false`；`vin_tvs_visible=false`；`reverse_protection_visible=false`；`signal_esd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`；`module_internal_memory_expanded=false` |

## 待确认事项

- `component.internal-radio-chip`：产品正文记载 CC2630F128 方案，但两张原理图只把射频单元画为 M1 DRF1609H，未展开或打印内部芯片位号。（证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 方框仅标 DRF1609H，未显示 CC2630F128 位号或内部连接）
- `interface.host-uart-routing`：产品正文列出多组可切换 M5-Bus TXD/RXD 针脚，但两张原理图未绘出 30 针 M5-Bus 或拨码开关，也未显示 G_TXD/G_RXD 与 M_TXD/M_RXD 之间的固定连线。（证据：图 7150a2e3a342 / 第 1 页 / 第 1 资源页 M1 仅引出 G_TXD/G_RXD，未画 M5-Bus 或拨码开关; 图 6043df7de5ad / 第 1 页 / 第 2 资源页 J1 HCore 仅标 M_TXD/M_RXD，未画 30 针 M5-Bus 或选择开关）
- `power.vin-input-range`：两张原理图只标出 VIN 网络，未打印允许输入范围；产品正文记载 5-12V，但无法由本地原理图确认端点和容差。（证据：图 6043df7de5ad / 第 1 页 / 第 2 资源页 U1 输入与 J1 pin 13/14 仅标 VIN，未附电压范围）
- `review.internal-radio-chip`：M1 DRF1609H 内部采用的主芯片是否确认为产品正文记载的 CC2630F128？；原因：本地原理图只显示完整模块型号 DRF1609H，没有展开内部芯片位号或料号。
- `review.host-uart-routing`：30 针 M5-Bus 的可切换 TXD/RXD 针脚如何通过底板拨码开关映射到 J1 HCore 和 M1 UART？；原因：本地两张原理图未包含 30 针 M5-Bus、拨码开关或 G_TXD/G_RXD 与 M_TXD/M_RXD 的跨板连线。
- `review.vin-input-range`：Module COMX Zigbee 的正式 VIN 输入范围是否确认为产品正文记载的 5-12V？；原因：本地原理图仅标 VIN 网络，没有标注最小、最大或绝对额定电压。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7150a2e3a3421a54155a785a54c1f80e01d62b7dca0c3855cfaed4bc194f3921` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_sch_01.webp` |
| 2 | 1 | `6043df7de5ada771d83775ce1efa1cdee9a2f52c074826e55cbebd7963d81084` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_sch_02.webp` |

---

源文档：`zh_CN/module/comx_zigbee.md`

源文档 SHA-256：`78afb7283e3f333934001af92eddeea37e8eb22c3934b006c39a253cdfe4f74d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
