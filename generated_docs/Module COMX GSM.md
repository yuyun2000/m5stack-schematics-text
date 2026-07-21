# Module COMX GSM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX GSM |
| SKU | M031-D |
| 产品 ID | `module-comx-gsm-e81b91d4b9ec` |
| 源文档 | `zh_CN/module/comx_gsm.md` |

## 概述

当前唯一原理图资源展示 Module COMX GSM 插接底板：J1 DC 输入经 U7 JW5033H 生成 +5.4V，S1 选择 +12V 或 +5.4V 送往 P1；J2 M5Stack_BUS 通过 S2 为 RXD/TXD 选择 GPIO，通过 S3、U1 MIC 与 Q1 连接核心板控制和音频端子。页面没有展开 SIM800C 核心小板、SIM 卡、射频、天线或状态 LED 电路，因此蜂窝频段、模组供电、功耗和协议能力均不能由该底板页直接确认。

## 检索关键词

`Module COMX GSM`、`M031-D`、`COMX GSM`、`COMX baseboard`、`SIM800C`、`GSM`、`GPRS`、`JW5033H`、`+12V`、`+5.4V`、`+3.3V`、`M5Stack_BUS`、`PWR2.5`、`SW-SPDT`、`SW DIP-6`、`RXD`、`TXD`、`G17`、`G0`、`G13`、`G16`、`G5`、`G15`、`G25`、`G26`、`MIC`、`O+`、`IN+`、`SS8550 Y2`、`SS54`、`MicroSIM`、`SMA antenna`、`850/900/1800/1900MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | JW5033H | +12V 至 +5.4V 的降压转换器 | 图 7ac95076a5be / 第 1 页 / 左上 U7 JW5033H pins 1-6，连接 +12V、C1、L1、R1-R3 与 +5.4V |
| J1/S1 | PWR2.5 / SW-SPDT | DC 电源入口及 +12V/+5.4V 到 P1 的电源选择 | 图 7ac95076a5be / 第 1 页 / 左中 J1 PWR2.5、S1 SW-SPDT、+12V、+5.4V 与 P1 |
| J2 | M5Stack_BUS | 30 针主机总线，提供 GND、3.3V、5V、EN、GPIO 与 UART 候选网络 | 图 7ac95076a5be / 第 1 页 / 右下 J2 M5Stack_BUS pins 1-30 |
| S2 | SW DIP-6 | 从三组 M5-Bus GPIO 对中选择 RXD/TXD | 图 7ac95076a5be / 第 1 页 / 右下 S2 SW DIP-6，G17/G0/G13 到 RXD，G16/G5/G15 到 TXD |
| S3 | SW DIP-6 | EN、MIC、G25、G26 与核心板控制/音频网络的选择路由 | 图 7ac95076a5be / 第 1 页 / 下中 S3 SW DIP-6 pins 1-12，连接 EN、MIC、G25、G26、O+、IN+ 与 Q1 偏置节点 |
| Q1 | SS8550 Y2 | 由 S3/EN 控制 P3 pin3 的 3.3V 高侧驱动 | 图 7ac95076a5be / 第 1 页 / 下中 Q1 SS8550 Y2、R4 4.7KΩ、R5 1KΩ、R6 4.7KΩ 与 P3/S3 |
| U1 | MIC | 板载麦克风，正端连接 MIC 选择网络，负端接地 | 图 7ac95076a5be / 第 1 页 / 下中 U1 MIC，正端到 S3 pin2/MIC，负端到 GND |
| P1-P5 | 2p / 2p / 3p / 2p / 4p | 连接核心小板的电源、控制、UART 与音频端子组 | 图 7ac95076a5be / 第 1 页 / 左中至左下 P1 2p、P2 2p、P3 3p、P4 2p、P5 4p |
| D1/D2 | SS54 | 以相反方向连接 M5-Bus +5V 与底板 +5.4V 电源轨 | 图 7ac95076a5be / 第 1 页 / 右下 D1/D2 SS54，位于 J2 pin28 +5V 与 +5.4V 之间 |

## 系统结构

### COMX GSM 插接底板架构

本页由 DC 输入与 +5.4V 降压、P1-P5 核心板端子、J2 M5Stack_BUS、S2 UART 选择、S3 控制/音频选择、U1 MIC 和 Q1 控制驱动组成。

- 参数与网络：`dc_input=J1 PWR2.5`；`buck=U7 JW5033H`；`module_connectors=P1-P5`；`host_bus=J2 M5Stack_BUS`；`uart_selector=S2`；`control_audio_selector=S3`；`microphone=U1 MIC`
- 证据：图 7ac95076a5be / 第 1 页 / 整页：U7/J1/S1/P1-P5/Q1/U1/S2/S3/J2/D1/D2

### 原理图资源覆盖范围

当前唯一资源覆盖 COMX 插接底板，不包含 SIM800C 核心小板内部电路；页面未画 SIM800C、SIM 卡座、射频天线接口或网络状态 LED。

- 参数与网络：`visible_scope=COMX plug-in baseboard`；`core_module_visible=false`；`sim_socket_visible=false`；`rf_visible=false`；`status_led_visible=false`
- 证据：图 7ac95076a5be / 第 1 页 / 整页仅底板电源、接口、拨码、MIC 与 M5Stack_BUS，无 SIM800C 核心电路

## 电源

### U7 +12V 至 +5.4V 降压

U7 JW5033H 的 VIN/pin3 接 +12V，EN/pin5 经 R1 100KΩ 接 +12V，SW/pin2 经 L1 4.7uH 输出 +5.4V，BST/pin6 经 C1 100nF 连接 SW 节点，GND/pin1 接地。

- 参数与网络：`converter=U7 JW5033H`；`input=+12V`；`enable=R1 100KΩ to +12V`；`inductor=L1 4.7uH`；`output=+5.4V`；`bootstrap=C1 100nF between BST and SW`
- 证据：图 7ac95076a5be / 第 1 页 / 左上 +12V、U7 JW5033H、R1、C1、L1 与 +5.4V

### U7 反馈与电源滤波

R2 115KΩ 从 +5.4V 接到 U7 FB/pin4，R3 20KΩ 从 FB 接地；C2/C3 各 10uF 接在 +12V 与 GND 之间，C32/C33 各 22uF、C4 100nF、C5 33pF 接在 +5.4V 与 GND 之间，C6 220uF 接在 +12V 与 GND 之间。

- 参数与网络：`feedback_upper=R2 115KΩ`；`feedback_lower=R3 20KΩ`；`input_filter=C2 10uF; C3 10uF; C6 220uF`；`output_filter=C32 22uF; C33 22uF; C4 100nF; C5 33pF`
- 证据：图 7ac95076a5be / 第 1 页 / 左上 U7 FB/R2/R3 与 C2/C3/C32/C33/C4/C5；左中 C6 220uF

### J1、S1 与 P1 电源选择

J1 PWR2.5 建立 +12V 与 GND；S1 SW-SPDT 的 pin3 接 +12V、pin1 接 +5.4V、公共 pin2 同时连接 P1 pins1/2，因此 P1 两针接收 S1 选中的电源轨。P2 两针均标为未连接。

- 参数与网络：`input_connector=J1 PWR2.5`；`selector=S1 SW-SPDT`；`source_a=pin3 +12V`；`source_b=pin1 +5.4V`；`common=pin2 -> P1 pins1/2`；`unused_connector=P2 pins1/2 NC`
- 证据：图 7ac95076a5be / 第 1 页 / 左中 J1、S1、P1、P2 与 +12V/+5.4V/GND

### M5-Bus +5V 与 +5.4V 连接

J2 pin28 的 +5V 与底板 +5.4V 之间并联 D1、D2 两只 SS54，两个二极管方向相反。

- 参数与网络：`m5bus_pin=J2 pin28/+5V`；`baseboard_rail=+5.4V`；`diodes=D1 SS54; D2 SS54`；`orientation=opposite directions`
- 证据：图 7ac95076a5be / 第 1 页 / 右下 J2 pin28 +5V、D1/D2 SS54 与 +5.4V

### 底板 +3.3V 来源

J2 pin12 连接 +3.3V，Q1 发射极与 R4 上端使用该 +3.3V；本页未画从 +12V 或 +5.4V 生成 +3.3V 的本地稳压器。

- 参数与网络：`m5bus_pin=J2 pin12/+3.3V`；`consumers=Q1 emitter; R4`；`local_3v3_regulator_visible=false`
- 证据：图 7ac95076a5be / 第 1 页 / J2 pin12 +3.3V 与 Q1/R4 +3.3V 网络；整页无 3.3V 稳压器

## 接口

### J2 M5Stack_BUS 已连接针脚

J2 pins1/3/5 接 GND，pin6 接 EN，pin8 接 G25，pin10 接 G26，pin12 接 +3.3V，pin15 接 G16，pin16 接 G17，pin20 接 G5，pin22 接 G13，pin23 接 G15，pin24 接 G0，pin28 接 +5V；其余针脚在本页无外部连线。

- 参数与网络：`ground=pins1/3/5`；`enable=pin6 EN`；`gpio=pin8 G25; pin10 G26; pin15 G16; pin16 G17; pin20 G5; pin22 G13; pin23 G15; pin24 G0`；`power=pin12 +3.3V; pin28 +5V`
- 证据：图 7ac95076a5be / 第 1 页 / 右下 J2 M5Stack_BUS pins1-30 与外部网络连线

### S2 UART GPIO 选择

S2 的前三路分别把 G17、G0、G13 连接到 RXD 公共网络，后三路分别把 G16、G5、G15 连接到 TXD 公共网络。

- 参数与网络：`rx_options=switch1 G17; switch2 G0; switch3 G13`；`tx_options=switch4 G16; switch5 G5; switch6 G15`；`rx_net=RXD`；`tx_net=TXD`
- 证据：图 7ac95076a5be / 第 1 页 / 右下 S2 pins7-12 为 G17/G0/G13/G16/G5/G15，pins6-4 汇入 RXD，pins3-1 汇入 TXD

### P1-P5 底板端子映射

P1 pins1/2 同接 S1 公共电源；P2 pins1/2 未连接；P3 pin1 未连接、pin2 接 GND、pin3 接 Q1/R6 控制节点；P4 pin1 接 RXD、pin2 接 TXD；P5 pin1 接 O+、pin2 未连接、pin3 接 IN+、pin4 接 GND。

- 参数与网络：`P1=pins1/2 selected supply`；`P2=pins1/2 NC`；`P3=pin1 NC; pin2 GND; pin3 control`；`P4=pin1 RXD; pin2 TXD`；`P5=pin1 O+; pin2 NC; pin3 IN+; pin4 GND`
- 证据：图 7ac95076a5be / 第 1 页 / 左中至左下 P1-P5 各针脚与网络/未连接标记

### M5-Bus 到 P4 UART 路径

S2 选择后的 RXD 与 TXD 公共网络分别连接 P4 pin1 与 pin2，构成 J2 候选 GPIO 到核心板 UART 端子的底板路径。

- 参数与网络：`host_side=J2 GPIO via S2`；`rx_destination=P4 pin1/RXD`；`tx_destination=P4 pin2/TXD`
- 证据：图 7ac95076a5be / 第 1 页 / S2 RXD/TXD 网络标签与左下 P4 pin1 RXD、pin2 TXD

## GPIO 与控制信号

### EN 到 P3 控制驱动

Q1 SS8550 Y2 发射极接 +3.3V，基极经 R5 1KΩ 接到由 R4 4.7KΩ 上拉的 S3 pin12 节点，集电极连接 P3 pin3，并由 R6 4.7KΩ 下拉到 GND；S3 第一路可把 J2 EN 接到该基极偏置节点。

- 参数与网络：`transistor=Q1 SS8550 Y2`；`emitter=+3.3V`；`base=R5 1KΩ to R4 4.7KΩ/S3 pin12`；`collector=P3 pin3 with R6 4.7KΩ to GND`；`control=J2 pin6 EN via S3 switch1`
- 证据：图 7ac95076a5be / 第 1 页 / 下中 Q1/R4/R5/R6/P3 与 S3 pins1/12、EN

## 保护电路

### 底板输入与接口保护可见性

本页未绘制 J1 输入保险丝、TVS、反接保护或浪涌抑制器，P1-P5 与 UART/音频信号也未显示专用 ESD 器件。

- 参数与网络：`input_fuse_visible=false`；`input_tvs_visible=false`；`reverse_protection_visible=false`；`signal_esd_visible=false`
- 证据：图 7ac95076a5be / 第 1 页 / J1、P1-P5、S2/S3 与 J2 外围；未见保险丝、TVS、反接或 ESD 位号

## 音频

### U1 MIC 与 S3 音频/GPIO 路由

U1 MIC 正端连接 MIC 并进入 S3 pin2，负端接 GND；S3 switch2 将 MIC 接到 IN+，switch3/4 分别将 G25 接到 O+/IN+，switch5/6 分别将 G26 接到 O+/IN+；O+ 与 IN+ 分别到 P5 pin1 与 pin3。

- 参数与网络：`microphone=U1 MIC`；`microphone_route=MIC -> S3 switch2 -> IN+`；`gpio25_routes=S3 switch3 -> O+; switch4 -> IN+`；`gpio26_routes=S3 switch5 -> O+; switch6 -> IN+`；`module_audio_connector=P5 pin1 O+; pin3 IN+; pin4 GND`
- 证据：图 7ac95076a5be / 第 1 页 / 下中 U1 MIC、S3 pins2-11、G25/G26、O+/IN+ 与左下 P5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | COMX GSM 插接底板架构 | `dc_input=J1 PWR2.5`；`buck=U7 JW5033H`；`module_connectors=P1-P5`；`host_bus=J2 M5Stack_BUS`；`uart_selector=S2`；`control_audio_selector=S3`；`microphone=U1 MIC` |
| 系统结构 | 原理图资源覆盖范围 | `visible_scope=COMX plug-in baseboard`；`core_module_visible=false`；`sim_socket_visible=false`；`rf_visible=false`；`status_led_visible=false` |
| 电源 | U7 +12V 至 +5.4V 降压 | `converter=U7 JW5033H`；`input=+12V`；`enable=R1 100KΩ to +12V`；`inductor=L1 4.7uH`；`output=+5.4V`；`bootstrap=C1 100nF between BST and SW` |
| 电源 | U7 反馈与电源滤波 | `feedback_upper=R2 115KΩ`；`feedback_lower=R3 20KΩ`；`input_filter=C2 10uF; C3 10uF; C6 220uF`；`output_filter=C32 22uF; C33 22uF; C4 100nF; C5 33pF` |
| 电源 | J1、S1 与 P1 电源选择 | `input_connector=J1 PWR2.5`；`selector=S1 SW-SPDT`；`source_a=pin3 +12V`；`source_b=pin1 +5.4V`；`common=pin2 -> P1 pins1/2`；`unused_connector=P2 pins1/2 NC` |
| 电源 | M5-Bus +5V 与 +5.4V 连接 | `m5bus_pin=J2 pin28/+5V`；`baseboard_rail=+5.4V`；`diodes=D1 SS54; D2 SS54`；`orientation=opposite directions` |
| 电源 | 底板 +3.3V 来源 | `m5bus_pin=J2 pin12/+3.3V`；`consumers=Q1 emitter; R4`；`local_3v3_regulator_visible=false` |
| 接口 | J2 M5Stack_BUS 已连接针脚 | `ground=pins1/3/5`；`enable=pin6 EN`；`gpio=pin8 G25; pin10 G26; pin15 G16; pin16 G17; pin20 G5; pin22 G13; pin23 G15; pin24 G0`；`power=pin12 +3.3V; pin28 +5V` |
| 接口 | S2 UART GPIO 选择 | `rx_options=switch1 G17; switch2 G0; switch3 G13`；`tx_options=switch4 G16; switch5 G5; switch6 G15`；`rx_net=RXD`；`tx_net=TXD` |
| 接口 | P1-P5 底板端子映射 | `P1=pins1/2 selected supply`；`P2=pins1/2 NC`；`P3=pin1 NC; pin2 GND; pin3 control`；`P4=pin1 RXD; pin2 TXD`；`P5=pin1 O+; pin2 NC; pin3 IN+; pin4 GND` |
| 接口 | M5-Bus 到 P4 UART 路径 | `host_side=J2 GPIO via S2`；`rx_destination=P4 pin1/RXD`；`tx_destination=P4 pin2/TXD` |
| GPIO 与控制信号 | EN 到 P3 控制驱动 | `transistor=Q1 SS8550 Y2`；`emitter=+3.3V`；`base=R5 1KΩ to R4 4.7KΩ/S3 pin12`；`collector=P3 pin3 with R6 4.7KΩ to GND`；`control=J2 pin6 EN via S3 switch1` |
| 音频 | U1 MIC 与 S3 音频/GPIO 路由 | `microphone=U1 MIC`；`microphone_route=MIC -> S3 switch2 -> IN+`；`gpio25_routes=S3 switch3 -> O+; switch4 -> IN+`；`gpio26_routes=S3 switch5 -> O+; switch6 -> IN+`；`module_audio_connector=P5 pin1 O+; pin3 IN+; pin4 GND` |
| 保护电路 | 底板输入与接口保护可见性 | `input_fuse_visible=false`；`input_tvs_visible=false`；`reverse_protection_visible=false`；`signal_esd_visible=false` |
| 系统结构 | 底板到 SIM800C 核心小板的完整互连 | `baseboard_connectors=P1-P5`；`core_mating_connectors_visible=false`；`sim800c_pin_mapping_visible=false` |
| 核心器件 | SIM800C 通信模组 | `documented_module=SIM800C`；`schematic_reference=null`；`variant_suffix=null`；`core_board_visible=false` |
| 电源 | DC 输入范围 | `documented_input_range=5-12V`；`schematic_input_label=+12V`；`absolute_max_visible=false` |
| 电源 | SIM800C 供电与休眠功耗 | `documented_module_supply=3.4-4.4V`；`documented_sleep_current=0.88mA typical`；`visible_baseboard_rails=+12V; +5.4V; +5V; +3.3V`；`core_regulator_visible=false` |
| 接口 | UART 速率与 AT 控制 | `documented_baud=115200`；`documented_control=AT commands`；`frame_format=null`；`uart_logic_level=null`；`firmware_version=null` |
| 接口 | MicroSIM 与状态 LED | `documented_sim_form_factor=MicroSIM`；`documented_leds=power; network status`；`sim_socket_visible=false`；`status_leds_visible=false` |
| 射频 | GSM 频段与外部天线 | `documented_bands=850/900/1800/1900MHz`；`documented_antenna=2.5dB SMA`；`documented_antenna_ranges=1880-1900MHz; 2320-2370MHz; 2575-2635MHz`；`rf_path_visible=false` |
| 射频 | GPRS 与数据协议能力 | `documented_multislot=class 12/10`；`documented_mobile_station=class B`；`documented_max_rate=85.6kbps`；`documented_coding=CS1; CS2; CS3; CS4`；`documented_protocols=TCP/IP; UDP; HTTP; FTP; PBCCH; USSD` |
| 其他事实 | 温度、尺寸、重量与 DC 接口规格 | `documented_temperature=-40°C to +85°C`；`documented_dc_jack=5.5mm`；`documented_module_size=54 x 54 x 13.2mm`；`documented_product_weight=40g`；`documented_gross_weight=75g`；`documented_package_size=165 x 60 x 36mm` |

## 待确认事项

- `system.complete-core-interconnect`：底板页只给出 P1-P5 的底板侧网络，未提供核心小板配对端、连接器定义或 SIM800C 引脚，因此不能确认选定电源、P3 控制、RXD/TXD、O+ 和 IN+ 在核心小板上的最终去向。（证据：图 7ac95076a5be / 第 1 页 / P1-P5 仅显示底板侧网络，页面无配对核心板或 SIM800C）
- `component.documented-sim800c`：产品正文记载内置通信模组为 SIM800C，但当前底板原理图未出现 SIM800C 位号、料号后缀、引脚或核心小板电路。（证据：图 7ac95076a5be / 第 1 页 / 整页无 SIM800C 器件方框、位号或引脚）
- `power.documented-dc-range`：产品正文给出外部 DC 输入 5-12V，但原理图将 J1 输入网络标为 +12V，没有标注允许的最小值、最大值、容差或降额条件。（证据：图 7ac95076a5be / 第 1 页 / J1 PWR2.5 与 U7 输入只标 +12V）
- `power.documented-module-supply`：产品正文给出 3.4-4.4V 供电和休眠模式典型 0.88mA，但底板页只显示 +12V、+5.4V、+5V 与 +3.3V，未显示 SIM800C 电源引脚、3.4-4.4V 电源轨、核心板稳压器或电流测量条件。（证据：图 7ac95076a5be / 第 1 页 / 底板电源网络与 P1；无 3.4-4.4V 标注或 SIM800C 电源电路）
- `interface.documented-uart-settings`：产品正文给出 UART 115200bps 并宣称 AT 指令控制；原理图确认底板 RXD/TXD 选择路径，但未标波特率、数据格式、逻辑电平、流控方式或 SIM800C 固件版本。（证据：图 7ac95076a5be / 第 1 页 / S2/P4 RXD/TXD 路径未标速率、格式、电平或固件）
- `interface.documented-sim-leds`：产品正文记载 MicroSIM 卡和电源/网络状态两路 LED，但底板原理图未显示 SIM 卡座、卡座料号、SIM 信号、LED 位号或 LED 驱动网络。（证据：图 7ac95076a5be / 第 1 页 / 整页无 SIM 卡座、SIM 信号、LED 或 LED 驱动器件）
- `rf.documented-bands-antenna`：产品正文给出 GSM/GPRS 850/900/1800/1900MHz、外置 2.5dB SMA 天线及天线频率范围，但底板页没有射频模组、ANT 网络、匹配器件、IPEX/SMA 连接器或天线走线。（证据：图 7ac95076a5be / 第 1 页 / 整页无 RF/ANT/SMA/IPEX 网络或射频匹配器件）
- `rf.documented-gprs-capabilities`：产品正文宣称 GPRS multi-slot class 12/10、mobile station class B、最高 85.6kbps、PBCCH、CS1-4、USSD 以及 TCP/IP、UDP、HTTP、FTP；底板原理图不包含蜂窝基带或固件信息，无法确认这些制式与协议能力。（证据：图 7ac95076a5be / 第 1 页 / 底板页无 SIM800C 基带、制式、吞吐或协议文本）
- `other.documented-environment-mechanics`：产品正文列出 -40°C 至 +85°C、DC 接口 5.5mm、模块尺寸 54 x 54 x 13.2mm、产品重量 40g、毛重 75g 和包装尺寸 165 x 60 x 36mm；当前电气原理图未包含这些环境与机械参数。（证据：图 7ac95076a5be / 第 1 页 / 电气原理图整页未标工作温度、机械尺寸、重量或 J1 机械口径）
- `review.complete-core-interconnect`：请提供 SIM800C 核心小板原理图或配对连接器定义，确认 P1-P5 到 SIM800C 电源、控制、UART 与音频引脚的完整映射。；原因：当前资源只覆盖 COMX 底板，核心小板配对端与 SIM800C 引脚均未显示。
- `review.sim800c-module`：请用量产 BOM、核心小板原理图或模组标签确认 M031-D 的通信模组完整料号和 SIM800C 版本后缀。；原因：底板原理图没有 SIM800C 位号、完整料号或核心板电路。
- `review.dc-input-range`：请用 JW5033H 设计计算、输入器件额定值和量产测试确认 J1 的正式 5-12V 输入范围及容差。；原因：原理图网络只标 +12V，没有给出范围或保护边界。
- `review.module-supply`：请用核心小板原理图和 SIM800C datasheet 确认 3.4-4.4V 供电轨的生成方式，以及 0.88mA 休眠电流的测试条件。；原因：底板只显示 +12V/+5.4V/+5V/+3.3V，未显示 SIM800C 供电链。
- `review.uart-settings`：请用 SIM800C 固件/AT 手册和核心板电平电路确认默认 115200bps、帧格式、逻辑电平与流控配置。；原因：底板原理图只确认 RXD/TXD 的 GPIO 选择和端子路径。
- `review.sim-leds`：请用核心小板原理图、BOM 与机械图确认 SIM 卡座为 MicroSIM，并确认电源/网络状态 LED 的位号与驱动连接。；原因：当前底板页没有 SIM 卡座或状态 LED 电路。
- `review.bands-antenna`：请用 SIM800C 完整版本 datasheet、射频原理图和天线规格书确认四频支持、SMA 接口、2.5dB 增益及所列频率范围。；原因：底板页没有蜂窝模组、射频链路或天线连接器。
- `review.gprs-capabilities`：请用量产 SIM800C 固件版本和官方 AT 手册复核 GPRS class、85.6kbps、编码方案及 TCP/IP/UDP/HTTP/FTP/PBCCH/USSD 支持范围。；原因：这些能力属于模组与固件，当前底板电气原理图不包含相关证据。
- `review.environment-mechanics`：请用正式尺寸图、环境规格、称重记录和 J1 料号复核温度、尺寸、重量、包装与 DC 接口口径。；原因：当前证据为电气原理图，不包含环境和机械规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7ac95076a5be6f11c33d7a67e2f609c3571bb469f4ff2de9bad10749f482a9da` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_sch_01.webp` |

---

源文档：`zh_CN/module/comx_gsm.md`

源文档 SHA-256：`0d46b96ff7ecf9a51dab0418b1321991481b8ecd1fae7506918ed62fa852270b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
