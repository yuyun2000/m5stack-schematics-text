# Module COMX LoRaWAN868 v2.0 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX LoRaWAN868 v2.0 |
| SKU | M031-C4 |
| 产品 ID | `module-comx-lorawan868-v2-0-f51e2213e53b` |
| 源文档 | `zh_CN/module/comx_lorawan868_2.0.md` |

## 概述

Module COMX LoRaWAN868 v2.0 当前唯一原理图资源展示 COMX 通用插接底板：J1 DC 输入经 U7 JW5033H 生成 +5.4V，S1 选择 +12V 或 +5.4V 送往 P1；J2 M5Stack_BUS 通过 S2 为 RXD/TXD 选择 GPIO，通过 S3、U1 MIC 与 Q1 连接核心板控制和音频端子。页面没有展开 ASR6501 LoRaWAN 核心小板、868MHz 射频链路或 SMA 天线，因此 v2.0 的芯片、协议版本、灵敏度与发射功率仍需核心板资料确认。

## 检索关键词

`Module COMX LoRaWAN868 v2.0`、`M031-C4`、`COMX LoRaWAN868 2.0`、`COMX baseboard`、`ASR6501`、`LoRaWAN`、`LoRaWAN v1.0.1`、`868MHz`、`-137dBm`、`+21dBm`、`SMA antenna`、`UART 115200bps`、`AT commands`、`JW5033H`、`+12V`、`+5.4V`、`+3.3V`、`M5Stack_BUS`、`PWR2.5`、`SW-SPDT`、`SW DIP-6`、`RXD`、`TXD`、`G17`、`G0`、`G13`、`G16`、`G5`、`G15`、`G25`、`G26`、`MIC`、`O+`、`IN+`、`SS8550 Y2`、`SS54`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | JW5033H | +12V 至 +5.4V 的降压转换器 | 图 d7f894f440e4 / 第 1 页 / 左上 U7 JW5033H pins 1-6，连接 +12V、C1、L1、R1-R3 与 +5.4V |
| J1/S1 | PWR2.5 / SW-SPDT | DC 电源入口及 +12V/+5.4V 到 P1 的电源选择 | 图 d7f894f440e4 / 第 1 页 / 左中 J1 PWR2.5、S1 SW-SPDT、+12V、+5.4V 与 P1 |
| J2 | M5Stack_BUS | 30 针主机总线，提供 GND、3.3V、5V、EN、GPIO 与 UART 候选网络 | 图 d7f894f440e4 / 第 1 页 / 右下 J2 M5Stack_BUS pins 1-30 |
| S2 | SW DIP-6 | 从三组 M5-Bus GPIO 对中选择 RXD/TXD | 图 d7f894f440e4 / 第 1 页 / 右下 S2 SW DIP-6，G17/G0/G13 到 RXD，G16/G5/G15 到 TXD |
| S3 | SW DIP-6 | EN、MIC、G25、G26 与核心板控制/音频网络的选择路由 | 图 d7f894f440e4 / 第 1 页 / 下中 S3 SW DIP-6 pins 1-12，连接 EN、MIC、G25、G26、O+、IN+ 与 Q1 偏置节点 |
| Q1 | SS8550 Y2 | 由 S3/EN 控制 P3 pin3 的 3.3V 高侧驱动 | 图 d7f894f440e4 / 第 1 页 / 下中 Q1 SS8550 Y2、R4 4.7KΩ、R5 1KΩ、R6 4.7KΩ 与 P3/S3 |
| U1 | MIC | 板载麦克风，正端连接 MIC 选择网络，负端接地 | 图 d7f894f440e4 / 第 1 页 / 下中 U1 MIC，正端到 S3 pin2/MIC，负端到 GND |
| P1-P5 | 2p / 2p / 3p / 2p / 4p | 连接核心小板的电源、控制、UART 与音频端子组 | 图 d7f894f440e4 / 第 1 页 / 左中至左下 P1 2p、P2 2p、P3 3p、P4 2p、P5 4p |
| D1/D2 | SS54 | 以相反方向连接 M5-Bus +5V 与底板 +5.4V 电源轨 | 图 d7f894f440e4 / 第 1 页 / 右下 D1/D2 SS54，位于 J2 pin28 +5V 与 +5.4V 之间 |

## 系统结构

### COMX LoRaWAN868 v2.0 插接底板架构

本页由 DC 输入与 +5.4V 降压、P1-P5 核心板端子、J2 M5Stack_BUS、S2 UART 选择、S3 控制/音频选择、U1 MIC 和 Q1 控制驱动组成。

- 参数与网络：`dc_input=J1 PWR2.5`；`buck=U7 JW5033H`；`module_connectors=P1-P5`；`host_bus=J2 M5Stack_BUS`；`uart_selector=S2`；`control_audio_selector=S3`；`microphone=U1 MIC`
- 证据：图 d7f894f440e4 / 第 1 页 / 整页：U7/J1/S1/P1-P5/Q1/U1/S2/S3/J2/D1/D2

### 原理图资源覆盖范围

当前唯一资源覆盖 COMX 通用插接底板，不包含 ASR6501 LoRaWAN 核心小板内部电路；页面未画 ASR6501、868MHz 射频链路或天线接口。

- 参数与网络：`visible_scope=COMX plug-in baseboard`；`core_module_visible=false`；`asr6501_visible=false`；`rf_visible=false`；`antenna_connector_visible=false`
- 证据：图 d7f894f440e4 / 第 1 页 / 整页仅底板电源、接口、拨码、MIC 与 M5Stack_BUS，无 LoRaWAN 核心电路

## 电源

### U7 +12V 至 +5.4V 降压

U7 JW5033H 的 VIN/pin3 接 +12V，EN/pin5 经 R1 100KΩ 接 +12V，SW/pin2 经 L1 4.7uH 输出 +5.4V，BST/pin6 经 C1 100nF 连接 SW 节点，GND/pin1 接地。

- 参数与网络：`converter=U7 JW5033H`；`input=+12V`；`enable=R1 100KΩ to +12V`；`inductor=L1 4.7uH`；`output=+5.4V`；`bootstrap=C1 100nF between BST and SW`
- 证据：图 d7f894f440e4 / 第 1 页 / 左上 +12V、U7 JW5033H、R1、C1、L1 与 +5.4V

### U7 反馈与电源滤波

R2 115KΩ 从 +5.4V 接到 U7 FB/pin4，R3 20KΩ 从 FB 接地；C2/C3 各 10uF 接在 +12V 与 GND 之间，C32/C33 各 22uF、C4 100nF、C5 33pF 接在 +5.4V 与 GND 之间，C6 220uF 接在 +12V 与 GND 之间。

- 参数与网络：`feedback_upper=R2 115KΩ`；`feedback_lower=R3 20KΩ`；`input_filter=C2 10uF; C3 10uF; C6 220uF`；`output_filter=C32 22uF; C33 22uF; C4 100nF; C5 33pF`
- 证据：图 d7f894f440e4 / 第 1 页 / 左上 U7 FB/R2/R3 与 C2/C3/C32/C33/C4/C5；左中 C6 220uF

### J1、S1 与 P1 电源选择

J1 PWR2.5 建立 +12V 与 GND；S1 SW-SPDT 的 pin3 接 +12V、pin1 接 +5.4V、公共 pin2 同时连接 P1 pins1/2，因此 P1 两针接收 S1 选中的电源轨。P2 两针均标为未连接。

- 参数与网络：`input_connector=J1 PWR2.5`；`selector=S1 SW-SPDT`；`source_a=pin3 +12V`；`source_b=pin1 +5.4V`；`common=pin2 -> P1 pins1/2`；`unused_connector=P2 pins1/2 NC`
- 证据：图 d7f894f440e4 / 第 1 页 / 左中 J1、S1、P1、P2 与 +12V/+5.4V/GND

### M5-Bus +5V 与 +5.4V 连接

J2 pin28 的 +5V 与底板 +5.4V 之间并联 D1、D2 两只 SS54，两个二极管方向相反。

- 参数与网络：`m5bus_pin=J2 pin28/+5V`；`baseboard_rail=+5.4V`；`diodes=D1 SS54; D2 SS54`；`orientation=opposite directions`
- 证据：图 d7f894f440e4 / 第 1 页 / 右下 J2 pin28 +5V、D1/D2 SS54 与 +5.4V

### 底板 +3.3V 来源

J2 pin12 连接 +3.3V，Q1 发射极与 R4 上端使用该 +3.3V；本页未画从 +12V 或 +5.4V 生成 +3.3V 的本地稳压器。

- 参数与网络：`m5bus_pin=J2 pin12/+3.3V`；`consumers=Q1 emitter; R4`；`local_3v3_regulator_visible=false`
- 证据：图 d7f894f440e4 / 第 1 页 / J2 pin12 +3.3V 与 Q1/R4 +3.3V 网络；整页无 3.3V 稳压器

## 接口

### J2 M5Stack_BUS 已连接针脚

J2 pins1/3/5 接 GND，pin6 接 EN，pin8 接 G25，pin10 接 G26，pin12 接 +3.3V，pin15 接 G16，pin16 接 G17，pin20 接 G5，pin22 接 G13，pin23 接 G15，pin24 接 G0，pin28 接 +5V；其余针脚在本页无外部连线。

- 参数与网络：`ground=pins1/3/5`；`enable=pin6 EN`；`gpio=pin8 G25; pin10 G26; pin15 G16; pin16 G17; pin20 G5; pin22 G13; pin23 G15; pin24 G0`；`power=pin12 +3.3V; pin28 +5V`
- 证据：图 d7f894f440e4 / 第 1 页 / 右下 J2 M5Stack_BUS pins1-30 与外部网络连线

### S2 UART GPIO 选择

S2 的前三路分别把 G17、G0、G13 连接到 RXD 公共网络，后三路分别把 G16、G5、G15 连接到 TXD 公共网络。

- 参数与网络：`rx_options=switch1 G17; switch2 G0; switch3 G13`；`tx_options=switch4 G16; switch5 G5; switch6 G15`；`rx_net=RXD`；`tx_net=TXD`
- 证据：图 d7f894f440e4 / 第 1 页 / 右下 S2 pins7-12 为 G17/G0/G13/G16/G5/G15，pins6-4 汇入 RXD，pins3-1 汇入 TXD

### P1-P5 底板端子映射

P1 pins1/2 同接 S1 公共电源；P2 pins1/2 未连接；P3 pin1 未连接、pin2 接 GND、pin3 接 Q1/R6 控制节点；P4 pin1 接 RXD、pin2 接 TXD；P5 pin1 接 O+、pin2 未连接、pin3 接 IN+、pin4 接 GND。

- 参数与网络：`P1=pins1/2 selected supply`；`P2=pins1/2 NC`；`P3=pin1 NC; pin2 GND; pin3 control`；`P4=pin1 RXD; pin2 TXD`；`P5=pin1 O+; pin2 NC; pin3 IN+; pin4 GND`
- 证据：图 d7f894f440e4 / 第 1 页 / 左中至左下 P1-P5 各针脚与网络/未连接标记

### M5-Bus 到 P4 UART 路径

S2 选择后的 RXD 与 TXD 公共网络分别连接 P4 pin1 与 pin2，构成 J2 候选 GPIO 到核心板 UART 端子的底板路径。

- 参数与网络：`host_side=J2 GPIO via S2`；`rx_destination=P4 pin1/RXD`；`tx_destination=P4 pin2/TXD`
- 证据：图 d7f894f440e4 / 第 1 页 / S2 RXD/TXD 网络标签与左下 P4 pin1 RXD、pin2 TXD

## GPIO 与控制信号

### EN 到 P3 控制驱动

Q1 SS8550 Y2 发射极接 +3.3V，基极经 R5 1KΩ 接到由 R4 4.7KΩ 上拉的 S3 pin12 节点，集电极连接 P3 pin3，并由 R6 4.7KΩ 下拉到 GND；S3 第一路可把 J2 EN 接到该基极偏置节点。

- 参数与网络：`transistor=Q1 SS8550 Y2`；`emitter=+3.3V`；`base=R5 1KΩ to R4 4.7KΩ/S3 pin12`；`collector=P3 pin3 with R6 4.7KΩ to GND`；`control=J2 pin6 EN via S3 switch1`
- 证据：图 d7f894f440e4 / 第 1 页 / 下中 Q1/R4/R5/R6/P3 与 S3 pins1/12、EN

## 保护电路

### 底板输入与接口保护可见性

本页未绘制 J1 输入保险丝、TVS、反接保护或浪涌抑制器，P1-P5 与 UART/音频信号也未显示专用 ESD 器件。

- 参数与网络：`input_fuse_visible=false`；`input_tvs_visible=false`；`reverse_protection_visible=false`；`signal_esd_visible=false`
- 证据：图 d7f894f440e4 / 第 1 页 / J1、P1-P5、S2/S3 与 J2 外围；未见保险丝、TVS、反接或 ESD 位号

## 音频

### U1 MIC 与 S3 音频/GPIO 路由

U1 MIC 正端连接 MIC 并进入 S3 pin2，负端接 GND；S3 switch2 将 MIC 接到 IN+，switch3/4 分别将 G25 接到 O+/IN+，switch5/6 分别将 G26 接到 O+/IN+；O+ 与 IN+ 分别到 P5 pin1 与 pin3。

- 参数与网络：`microphone=U1 MIC`；`microphone_route=MIC -> S3 switch2 -> IN+`；`gpio25_routes=S3 switch3 -> O+; switch4 -> IN+`；`gpio26_routes=S3 switch5 -> O+; switch6 -> IN+`；`module_audio_connector=P5 pin1 O+; pin3 IN+; pin4 GND`
- 证据：图 d7f894f440e4 / 第 1 页 / 下中 U1 MIC、S3 pins2-11、G25/G26、O+/IN+ 与左下 P5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | COMX LoRaWAN868 v2.0 插接底板架构 | `dc_input=J1 PWR2.5`；`buck=U7 JW5033H`；`module_connectors=P1-P5`；`host_bus=J2 M5Stack_BUS`；`uart_selector=S2`；`control_audio_selector=S3`；`microphone=U1 MIC` |
| 系统结构 | 原理图资源覆盖范围 | `visible_scope=COMX plug-in baseboard`；`core_module_visible=false`；`asr6501_visible=false`；`rf_visible=false`；`antenna_connector_visible=false` |
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
| 系统结构 | 底板到 ASR6501 核心小板的完整互连 | `baseboard_connectors=P1-P5`；`core_mating_connectors_visible=false`；`asr6501_pin_mapping_visible=false` |
| 核心器件 | ASR6501 通信方案 | `documented_chip=ASR6501`；`schematic_reference=null`；`core_board_visible=false` |
| 电源 | DC 输入范围 | `documented_input_range=5-12V`；`schematic_input_label=+12V`；`absolute_max_visible=false` |
| 接口 | UART 115200bps 与 AT 指令 | `documented_baud=115200`；`documented_protocol=AT commands`；`frame_format=null`；`uart_logic_level=null`；`firmware_version=null` |
| 射频 | 868MHz LoRaWAN 性能 | `documented_frequency=868MHz`；`documented_lorawan_version=v1.0.1`；`documented_sensitivity=-137dBm at SF=12/BW=125KHz`；`documented_max_tx_power=+21dBm`；`rf_path_visible=false` |
| 射频 | SMA 外置天线 | `documented_antenna=SMA`；`antenna_connector_visible=false`；`matching_network_visible=false`；`rf_esd_visible=false` |
| 其他事实 | 868MHz 国家与地区适用性 | `documented_region=868MHz countries and regions list`；`regional_configuration_visible=false`；`certification_visible=false` |
| 其他事实 | v2.0 尺寸与重量 | `documented_product_size=54.2 x 54.2 x 13.2mm`；`documented_product_weight=27.4g`；`documented_gross_weight=70.4g`；`documented_package_size=165 x 60 x 36mm` |
| 其他事实 | M031-C4 v2.0 图纸适用范围 | `product_sku=M031-C4`；`product_version=v2.0`；`sku_printed_on_schematic=false`；`pcb_revision_visible=false`；`bom_revision_visible=false` |

## 待确认事项

- `system.complete-core-interconnect`：底板页只给出 P1-P5 的底板侧网络，未提供 v2.0 核心小板配对端、连接器定义或 ASR6501 引脚，因此不能确认选定电源、P3 控制、RXD/TXD、O+ 和 IN+ 在核心小板上的最终去向。（证据：图 d7f894f440e4 / 第 1 页 / P1-P5 仅显示底板侧网络，页面无配对核心板或 ASR6501）
- `component.documented-asr6501`：v2.0 产品正文记载通信芯片/方案为 ASR6501，但当前底板原理图未出现 ASR6501 位号、封装、引脚、供电、时钟、复位或内部射频连接。（证据：图 d7f894f440e4 / 第 1 页 / 整页无 ASR6501 器件方框、位号或引脚）
- `power.documented-dc-range`：v2.0 产品正文给出外部 DC 输入 5-12V，但原理图将 J1 输入网络标为 +12V，没有标注允许的最小值、最大值、容差或降额条件。（证据：图 d7f894f440e4 / 第 1 页 / J1 PWR2.5 与 U7 输入只标 +12V）
- `interface.documented-uart-at`：v2.0 产品正文给出 UART 115200bps 并使用 AT 指令集控制；原理图确认底板 RXD/TXD 选择路径，但未标波特率、帧格式、逻辑电平、流控方式或核心板固件版本。（证据：图 d7f894f440e4 / 第 1 页 / S2/P4 RXD/TXD 路径未标速率、格式、电平或固件）
- `rf.documented-lorawan-performance`：v2.0 产品正文记载 868MHz、LoRaWAN v1.0.1、最小接收灵敏度 -137dBm（SF=12、BW=125KHz）和最大发射功率 +21dBm；底板页没有 ASR6501、射频匹配、滤波、功放、收发切换或测试条件。（证据：图 d7f894f440e4 / 第 1 页 / 整页无 ASR6501、868MHz RF 网络或性能参数）
- `rf.documented-sma-antenna`：v2.0 产品正文和包装内容记载 SMA 天线，但底板原理图未显示 SMA、IPEX、天线匹配、射频馈线或射频 ESD 器件。（证据：图 d7f894f440e4 / 第 1 页 / 整页无 SMA/IPEX/ANT 网络、匹配或射频 ESD）
- `other.documented-region-support`：v2.0 产品正文列出一组 868MHz 支持国家和地区，但底板原理图没有区域配置、认证编号、发射参数限制或法规证据，不能据此确认当前量产硬件在各地区的合规适用性。（证据：图 d7f894f440e4 / 第 1 页 / 底板页无区域配置、认证编号或法规参数）
- `other.documented-mechanics`：v2.0 产品正文列出产品尺寸 54.2 x 54.2 x 13.2mm、产品重量 27.4g、毛重 70.4g 和包装尺寸 165 x 60 x 36mm；当前电气原理图未包含这些机械参数。（证据：图 d7f894f440e4 / 第 1 页 / 电气原理图整页未标机械尺寸或重量）
- `other.revision-applicability`：当前资源页没有打印 M031-C4、v2.0、PCB 版本、BOM 版本或 ASR6501 核心板标识，因此该通用底板页与 v2.0 量产底板/核心板版本的对应关系仍需版本化设计资料确认。（证据：图 d7f894f440e4 / 第 1 页 / 整页通用底板电路，无 M031-C4/v2.0/PCB/BOM 版本标识）
- `review.complete-core-interconnect`：请提供 M031-C4 v2.0 核心小板原理图或配对连接器定义，确认 P1-P5 到 ASR6501 电源、控制、UART 与辅助端子的完整映射。；原因：当前资源只覆盖 COMX 通用底板，核心小板配对端与 ASR6501 引脚均未显示。
- `review.asr6501`：请用 M031-C4 量产 BOM、核心小板原理图和器件标识确认 ASR6501 的完整料号、封装与外围连接。；原因：底板原理图没有 ASR6501 位号或核心小板电路。
- `review.dc-input-range`：请用 JW5033H 设计计算、输入器件额定值和量产测试确认 M031-C4 J1 的正式 5-12V 输入范围及容差。；原因：原理图网络只标 +12V，没有给出范围或保护边界。
- `review.uart-at`：请用 v2.0 核心板电平电路、固件和 AT 手册确认 UART 115200bps、帧格式、逻辑电平与流控配置。；原因：底板原理图只确认 RXD/TXD 的 GPIO 选择和端子路径。
- `review.lorawan-performance`：请用 M031-C4 核心板原理图、ASR6501 资料和量产射频测试确认 868MHz、LoRaWAN v1.0.1、-137dBm 与 +21dBm 的适用条件。；原因：底板页没有 LoRaWAN 核心芯片、射频链路或性能测试条件。
- `review.sma-antenna`：请用 v2.0 核心板射频原理图、BOM 和天线规格书确认 SMA 接口、匹配、阻抗与 ESD 保护。；原因：当前底板页没有任何天线或射频网络。
- `review.region-support`：请用最新 LoRaWAN 区域参数、当地法规和 M031-C4 认证资料复核正文国家/地区列表。；原因：电气原理图不能证明区域法规适用性或认证状态。
- `review.mechanics`：请用 v2.0 正式尺寸图、称重记录和包装规范复核 M031-C4 的尺寸与重量。；原因：当前证据为电气原理图，不包含机械规格。
- `review.revision-applicability`：请用版本化原理图、PCB 文件、BOM 或工程变更记录确认当前通用底板页对应的 M031-C4 v2.0 硬件版本。；原因：资源页没有 SKU、v2.0、PCB 或 BOM 版本标识，不能与旧版 868 产品混用。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d7f894f440e4225d10edda7b5421551a1d31e44e388ebd935600b3839b780753` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_sch_01.webp` |

---

源文档：`zh_CN/module/comx_lorawan868_2.0.md`

源文档 SHA-256：`be7dccfcb8d21ba901a76b0512f4030b170a5f48314bf6f6db15b5229cbeb51e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
