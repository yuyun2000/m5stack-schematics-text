# Module COMX LoRaWAN470 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX LoRaWAN470 |
| SKU | M031-C2 |
| 产品 ID | `module-comx-lorawan470-0079a37aa09d` |
| 源文档 | `zh_CN/module/comx_lorawan470.md` |

## 概述

当前唯一原理图资源展示 COMX 通用插接底板而非 LoRaWAN470 核心小板：J1 DC 输入的 +12V 经 U7 JW5033H 降压为 +5.4V，S1 在 +12V/+5.4V 之间选择模块供电，J2 M5Stack_BUS 通过 D1/D2 接收 +5.4V，S2 六位拨码把多组 M5-Bus GPIO 路由到 RXD/TXD。页面还包含 P1-P5 模块插座、S3 功能拨码、Q1 控制级和 U1 MIC，但没有 ASR6501、470MHz 射频前端、SMA 天线或 LoRaWAN 核心电路；这些产品级声明均列为待确认。

## 检索关键词

`Module COMX LoRaWAN470`、`M031-C2`、`COMX baseboard`、`ASR6501`、`LoRaWAN`、`CN470`、`470MHz`、`SMA`、`AT command`、`115200`、`8N1`、`JW5033H`、`PWR2.5`、`+12V`、`+5.4V`、`SW-SPDT`、`SW DIP-6`、`M5Stack_BUS`、`SS54`、`RXD`、`TXD`、`G17`、`G0`、`G13`、`G16`、`G5`、`G15`、`G25`、`G26`、`EN`、`MIC`、`O+`、`IN+`、`SS8550 Y2`、`5-12V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | JW5033H | +12V 到 +5.4V 的底板降压转换器 | 图 7ac95076a5be / 第 1 页 / 左上 U7 JW5033H、L1 与 +12V/+5.4V |
| J1 | PWR2.5 | COMX 底板外部 DC 电源输入插座 | 图 7ac95076a5be / 第 1 页 / 左中 J1 PWR2.5，连接 +12V 与 GND |
| S1 | SW-SPDT | 在 +12V 与 +5.4V 之间选择 P1 插接模块供电 | 图 7ac95076a5be / 第 1 页 / 左中 S1 SW-SPDT、+12V/+5.4V 与 P1 |
| J2 | M5Stack_BUS | 30-pin M5-Bus 堆叠连接器 | 图 7ac95076a5be / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30 |
| S2,S3 | SW DIP-6 | M5-Bus UART GPIO 路由与插接模块功能配置拨码开关 | 图 7ac95076a5be / 第 1 页 / 中下 S2/S3 SW DIP-6 |
| D1,D2 | SS54 | +5.4V 到 M5-Bus +5V/BATTERY 电源脚的肖特基隔离 | 图 7ac95076a5be / 第 1 页 / 右下 J2 pins28/30 与 +5.4V 之间 D1/D2 SS54 |
| P1,P2,P3,P4,P5 | 2p/3p/4p module headers | COMX 插接核心的电源、UART、控制和通用音频连接器 | 图 7ac95076a5be / 第 1 页 / 左中至左下 P1-P5，2p/3p/4p 接口 |
| Q1,U1 | SS8550 Y2 / MIC | S3 配置网络中的晶体管控制级与底板麦克风 | 图 7ac95076a5be / 第 1 页 / 左下 Q1 SS8550 Y2、U1 MIC、R4-R6 与 S3 |

## 系统结构

### COMX 通用插接底板架构

页面明确显示 COMX 底板：包含 J1 DC 输入、U7 5.4V 降压、S1 电源选择、J2 M5Stack_BUS、S2/S3 拨码、P1-P5 模块插座、Q1 控制级与 U1 MIC。

- 参数与网络：`schematic_page_count=1`；`visible_scope=COMX baseboard`；`core_scope=null`
- 证据：图 7ac95076a5be / 第 1 页 / 整页 COMX 底板电源、M5-Bus、拨码与模块插座

## 电源

### +12V 到 +5.4V 降压

J1 PWR2.5 输入网络标为 +12V；U7 JW5033H 以 R1 100 kΩ 偏置 EN，经 L1 4.7 uH 和 R2/R3 115 kΩ/20 kΩ 反馈输出 +5.4V，输入端 C2/C3 各 10 uF，输出端 C32/C33 各 22 uF并配 C4 100 nF。

- 参数与网络：`input=+12V`；`output=+5.4V`；`converter=U7 JW5033H`；`inductor=L1 4.7uH`；`feedback=R2 115k,R3 20k`；`input_caps=C2 10uF,C3 10uF`；`output_caps=C32 22uF,C33 22uF,C4 100nF`
- 证据：图 7ac95076a5be / 第 1 页 / 左上 J1/U7/L1/R1-R3/C2-C5/C32-C33

### P1 插接核心供电电压选择

S1 SW-SPDT 的两路输入分别为 +12V 与 +5.4V，公共端连接 P1 2-pin 接口；P2 2-pin 的两脚在该页均标为未连接。

- 参数与网络：`option_a=+12V`；`option_b=+5.4V`；`output_connector=P1`；`unused_connector=P2`
- 证据：图 7ac95076a5be / 第 1 页 / 左中 S1/P1/P2

### +5.4V 与 M5-Bus 电源脚

+5.4V 通过 D1/D2 两颗 SS54 分别连接 J2 的 +5V 与 BATTERY 电源脚；J2 pins25/27/29 为 HPWR，pin12 为 +3.3V，pin28 为 +5V，pin30 为 BATTERY。

- 参数与网络：`source=+5.4V`；`diodes=D1,D2 SS54`；`logic_rail=pin12 +3.3V`；`power_pins=pin25 HPWR,pin27 HPWR,pin28 +5V,pin29 HPWR,pin30 BATTERY`
- 证据：图 7ac95076a5be / 第 1 页 / 右侧 J2 pins12/25/27-30 与 D1/D2/+5.4V

## 接口

### 30-pin M5Stack_BUS

J2 pins1/3/5 为 GND；pins2/4/6 为 GPIO35/GPIO36/EN；pins7-24 依次引出 GPIO23/GPIO25、GPIO19/GPIO26、GPIO18/+3.3V、GPIO3/GPIO1、GPIO16/GPIO17、GPIO21/GPIO22、GPIO2/GPIO5、GPIO12/GPIO13、GPIO15/GPIO0；pins25-30 为 HPWR/GPIO34/HPWR/+5V/HPWR/BATTERY。

- 参数与网络：`connector=J2 M5Stack_BUS`；`pins=30`；`ground=1,3,5`；`uart_candidates=GPIO16,GPIO17,GPIO5,GPIO13,GPIO15,GPIO0`；`rails=pin12 +3.3V,pin28 +5V,pin30 BATTERY`
- 证据：图 7ac95076a5be / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30

### M5-Bus UART 拨码路由

S2 六位拨码把 G17/G0/G13 三路候选连接到 RXD 公共网络，把 G16/G5/G15 三路候选连接到 TXD 公共网络；P4 2-pin 引出 RXD/TXD。

- 参数与网络：`rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4`；`switch=S2 SW DIP-6`
- 证据：图 7ac95076a5be / 第 1 页 / 中下 S2 SW DIP-6、G17/G0/G13/G16/G5/G15 与 RXD/TXD；左下 P4

### P1-P5 插接核心接口

P1 为 S1 选择后的两针电源，P2 两针未连接，P3 三针包含 GND 与控制网络，P4 两针为 RXD/TXD，P5 四针包含 O+、IN+ 与两脚 GND；S3 六位拨码连接 EN、MIC、G25、G26、O+、IN+ 等适配网络。

- 参数与网络：`power=P1`；`unused=P2`；`control=P3`；`uart=P4 RXD/TXD`；`audio=P5 O+/IN+/GND/GND`；`configuration_switch=S3`
- 证据：图 7ac95076a5be / 第 1 页 / 左中/左下 P1-P5、S3、EN/MIC/G25/G26/O+/IN+

## 音频

### 底板 MIC 与通用音频脚

U1 MIC 一端接 GND，信号 MIC 接 S3；P5 引出 O+、IN+ 与两脚 GND，Q1 SS8550 Y2、R4-R6 组成 S3 周边控制网络。

- 参数与网络：`microphone=U1 MIC`；`microphone_net=MIC`；`output_net=O+`；`input_net=IN+`；`control=Q1 SS8550 Y2,R4-R6,S3`
- 证据：图 7ac95076a5be / 第 1 页 / 左下 U1 MIC、Q1、R4-R6、P5 与 S3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | COMX 通用插接底板架构 | `schematic_page_count=1`；`visible_scope=COMX baseboard`；`core_scope=null` |
| 电源 | +12V 到 +5.4V 降压 | `input=+12V`；`output=+5.4V`；`converter=U7 JW5033H`；`inductor=L1 4.7uH`；`feedback=R2 115k,R3 20k`；`input_caps=C2 10uF,C3 10uF`；`output_caps=C32 22uF,C33 22uF,C4 100nF` |
| 电源 | P1 插接核心供电电压选择 | `option_a=+12V`；`option_b=+5.4V`；`output_connector=P1`；`unused_connector=P2` |
| 电源 | +5.4V 与 M5-Bus 电源脚 | `source=+5.4V`；`diodes=D1,D2 SS54`；`logic_rail=pin12 +3.3V`；`power_pins=pin25 HPWR,pin27 HPWR,pin28 +5V,pin29 HPWR,pin30 BATTERY` |
| 接口 | 30-pin M5Stack_BUS | `connector=J2 M5Stack_BUS`；`pins=30`；`ground=1,3,5`；`uart_candidates=GPIO16,GPIO17,GPIO5,GPIO13,GPIO15,GPIO0`；`rails=pin12 +3.3V,pin28 +5V,pin30 BATTERY` |
| 接口 | M5-Bus UART 拨码路由 | `rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4`；`switch=S2 SW DIP-6` |
| 接口 | P1-P5 插接核心接口 | `power=P1`；`unused=P2`；`control=P3`；`uart=P4 RXD/TXD`；`audio=P5 O+/IN+/GND/GND`；`configuration_switch=S3` |
| 音频 | 底板 MIC 与通用音频脚 | `microphone=U1 MIC`；`microphone_net=MIC`；`output_net=O+`；`input_net=IN+`；`control=Q1 SS8550 Y2,R4-R6,S3` |
| 系统结构 | LoRaWAN470 核心小板未覆盖 | `documented_core=ASR6501`；`documented_stack=LoRaWAN`；`visible_scope=COMX baseboard`；`visible_core=null` |
| 核心器件 | ASR6501 核心方案 | `documented_component=ASR6501`；`reference=null`；`part_number_suffix=null`；`supply=null`；`clock=null`；`reset=null` |
| 射频 | 470MHz、CN470 与 SMA 天线 | `documented_frequency=470MHz`；`documented_region=CN470`；`documented_antenna=SMA antenna`；`rf_connector=null`；`matching_network=null`；`rf_protection=null` |
| 接口 | LoRaWAN 核心 UART 默认参数 | `documented_protocol=AT command`；`documented_baud=115200`；`documented_data_bits=8`；`documented_stop_bits=1`；`documented_parity=none`；`documented_terminator=none`；`schematic_uart=S2/P4 RXD/TXD` |
| 其他事实 | LoRaWAN 协议栈与通信能力 | `documented_stack=LoRaWAN`；`documented_role=collection node`；`documented_claims=long range,ultra-low power,high sensitivity`；`tx_power=null`；`sensitivity=null`；`sleep_current=null`；`firmware_version=null` |
| 电源 | DC 5-12V 输入范围 | `documented_input=5-12V`；`schematic_input_label=+12V`；`undervoltage_lockout=null`；`tolerance=null` |
| 接口 | Fire 主机 UART 拨码说明 | `documented_avoid=G16,G17`；`documented_tx=G0,G13`；`documented_rx=G5,G15`；`schematic_rxd_candidates=G17,G0,G13`；`schematic_txd_candidates=G16,G5,G15`；`direction_perspective=null` |

## 待确认事项

- `system.lorawan-core-not-shown`：源文档称产品采用 ASR6501 方案并集成 LoRaWAN 协议栈；当前资源没有 ASR6501、LoRa 收发链、射频匹配、晶振、非易失存储或核心小板电源电路，因此该页不能验证 LoRaWAN470 核心硬件。（证据：图 7ac95076a5be / 第 1 页 / 整页无 ASR6501 或 LoRaWAN 核心小板电路）
- `component.documented-asr6501`：源文档将 ASR6501 列为产品核心方案；底板图没有该器件的位号、完整料号、引脚、供电、时钟、复位、存储或 UART 电平信息。（证据：图 7ac95076a5be / 第 1 页 / 整页仅含 COMX 底板，未出现 ASR6501）
- `rf.documented-cn470`：源文档称工作频率为 470MHz、区域为 CN470 并随附 SMA 天线；底板图没有 ASR6501、射频前端、匹配网络、SMA/IPEX 连接器、天线馈电或射频保护器件。（证据：图 7ac95076a5be / 第 1 页 / 整页无 LoRa 射频、SMA/IPEX 或匹配电路）
- `interface.documented-uart`：源文档称核心通过 UART 使用 AT 指令，默认 115200 波特、8 数据位、1 停止位、无校验且无结束符；底板图只确认 S2/P4 的 RXD/TXD 硬件路由，不包含核心 UART 电平、波特率、帧格式或固件配置。（证据：图 7ac95076a5be / 第 1 页 / S2/P4 仅显示 RXD/TXD 路由，无串口参数或协议文字）
- `other.documented-lorawan-behavior`：源文档称模组集成 LoRaWAN 协议栈，具备远距离、低功耗和高灵敏度特性并可作为采集节点接入网关；底板图不含核心芯片、固件、区域参数、发射功率、接收灵敏度、休眠电流或入网状态机。（证据：图 7ac95076a5be / 第 1 页 / 整页无 LoRaWAN 核心、协议或性能测试电路）
- `power.documented-dc-range`：源文档称 DC 接口允许 5-12V 输入；原理图把 J1 输入网络直接命名为 +12V，并按 +12V 设计 JW5033H 到 +5.4V 的降压路径，没有标最小 5V、输入容差、欠压锁定或完整允许范围。（证据：图 7ac95076a5be / 第 1 页 / 左侧 J1/U7 输入仅标 +12V）
- `interface.fire-routing-perspective`：源文档为避免 Fire 的 G16/G17 PSRAM 冲突，要求选择 TX(G0/G13)、RX(G5/G15)；图面网络名则把 G0/G13 归入 RXD 候选、G5/G15 归入 TXD 候选，需确认文档采用主机视角还是模块视角。（证据：图 7ac95076a5be / 第 1 页 / 中下 S2：G17/G0/G13 接 RXD，G16/G5/G15 接 TXD）
- `review.lorawan-core-scope`：Module COMX LoRaWAN470 的 ASR6501 核心小板应使用哪份完整原理图？；原因：当前资源只覆盖 COMX 通用底板，不含 LoRa 收发、射频与核心电源电路。
- `review.asr6501`：M031-C2 量产核心的完整 ASR6501 料号、硬件版本、供电、时钟和复位连接是什么？；原因：底板原理图没有 ASR6501 器件或 BOM 信息。
- `review.cn470-rf`：核心小板的 CN470 频段、SMA 天线接口、匹配网络、发射功率和射频认证边界是什么？；原因：当前底板图没有任何 LoRa 射频或天线电路。
- `review.uart-defaults`：量产固件默认 UART 是否固定为 115200、8 数据位、1 停止位、无校验且无结束符，AT 指令版本是什么？；原因：底板图只画 RXD/TXD 路由，串口参数由核心固件决定。
- `review.lorawan-behavior`：LoRaWAN 协议栈版本、区域参数、入网模式、发射功率、接收灵敏度和各电源状态电流是什么？；原因：当前资源不含核心硬件、固件和性能测试证据。
- `review.dc-input-range`：J1 与 U7 的量产 DC 输入允许范围是否完整覆盖 5-12V？；原因：图面只把输入标为 +12V，没有范围、容差或欠压条件。
- `review.fire-uart-perspective`：Fire 兼容说明中的 TX/RX 是主机视角还是 LoRaWAN 核心视角，实际拨码应如何标注？；原因：源文档的 TX(G0/G13)、RX(G5/G15) 与图面 RXD/TXD 网络名方向相反。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7ac95076a5be6f11c33d7a67e2f609c3571bb469f4ff2de9bad10749f482a9da` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_sch_01.webp` |

---

源文档：`zh_CN/module/comx_lorawan470.md`

源文档 SHA-256：`c5132b77a3275fc37a6f5e90cd4e27993b3b21045a588375408ff681f3d4d3a4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
