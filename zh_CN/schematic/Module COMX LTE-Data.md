# Module COMX LTE-Data 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX LTE-Data |
| SKU | M031-E |
| 产品 ID | `module-comx-lte-data-5df34570f62f` |
| 源文档 | `zh_CN/module/comx_lte-data.md` |

## 概述

当前唯一原理图资源展示 COMX 通用插接底板：J1 DC 输入的 +12V 经 U7 JW5033H 降压为 +5.4V，S1 在 +12V/+5.4V 之间选择模块供电，J2 M5Stack_BUS 通过 D1/D2 接收 +5.4V，并由 S2 六位拨码把多组 M5-Bus GPIO 路由到 RXD/TXD。页面还包含模块插座 P1-P5、S3 配置拨码、Q1 控制级和板载 MIC，但没有 A7600C1、MicroSIM、状态 LED、SMA 天线或蜂窝射频电路。

## 检索关键词

`Module COMX LTE-Data`、`M031-E`、`COMX baseboard`、`A7600C1`、`LTE Cat 1`、`LTE CAT4`、`LTE-TDD`、`LTE-FDD`、`GSM`、`GPRS`、`EDGE`、`MicroSIM`、`SMA`、`JW5033H`、`PWR2.5`、`+12V`、`+5.4V`、`SW-SPDT`、`SW DIP-6`、`M5Stack_BUS`、`SS54`、`RXD`、`TXD`、`G17`、`G0`、`G13`、`G16`、`G5`、`G15`、`G25`、`G26`、`EN`、`MIC`、`O+`、`IN+`、`SS8550 Y2`、`UART`、`115200bps`、`AT command`、`RNDIS`、`PPP`、`ECM`、`IPv4`、`IPv6`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | JW5033H | +12V 到 +5.4V 的降压转换器 | 图 7ac95076a5be / 第 1 页 / 左上 U7 JW5033H、L1 与 +12V/+5.4V |
| J1 | PWR2.5 | 外部 DC 电源输入插座 | 图 7ac95076a5be / 第 1 页 / 左中 J1 PWR2.5，连接 +12V 与 GND |
| S1 | SW-SPDT | 在 +12V 与 +5.4V 之间选择 P1 模块供电 | 图 7ac95076a5be / 第 1 页 / 左中 S1 SW-SPDT、+12V/+5.4V 与 P1 |
| J2 | M5Stack_BUS | 30-pin M5-Bus 堆叠连接器 | 图 7ac95076a5be / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30 |
| S2,S3 | SW DIP-6 | UART GPIO 路由与插接模块功能配置拨码开关 | 图 7ac95076a5be / 第 1 页 / 中下 S2/S3 SW DIP-6 |
| D1,D2 | SS54 | +5.4V 到 M5-Bus +5V 的并联肖特基二极管 | 图 7ac95076a5be / 第 1 页 / 右下 J2 pin28 与 +5.4V 之间 D1/D2 SS54 |
| P1,P2,P3,P4,P5 | 2p/3p/4p module headers | COMX 插接模块的电源、UART、控制和音频信号连接器 | 图 7ac95076a5be / 第 1 页 / 左中至左下 P1-P5，2p/3p/4p 接口 |
| Q1,U1 | SS8550 Y2 / MIC | S3 配置网络中的晶体管控制级与板载麦克风 | 图 7ac95076a5be / 第 1 页 / 左下 Q1 SS8550 Y2、U1 MIC、R4-R6 与 S3 |

## 系统结构

### COMX 通用插接底板架构

页面显示 COMX 底板而非 LTE 核心小板：包含 J1 DC 输入、U7 5.4V 降压、S1 电源选择、J2 M5Stack_BUS、S2/S3 拨码、P1-P5 模块插座、Q1 控制级与 U1 MIC。

- 参数与网络：`schematic_page_count=1`；`visible_scope=COMX baseboard`
- 证据：图 7ac95076a5be / 第 1 页 / 整页 COMX 底板电源、M5-Bus、拨码与模块插座

## 电源

### +12V 到 +5.4V 降压

J1 PWR2.5 输入 +12V；U7 JW5033H 以 R1 100K 上拉 EN，经 L1 4.7uH 和 R2/R3 115K/20K 反馈输出 +5.4V，输入端 C2/C3 各 10uF，输出端 C32/C33 各 22uF并配 C4 100nF。

- 参数与网络：`input=+12V`；`output=+5.4V`；`inductor_uh=4.7`；`converter=JW5033H`
- 证据：图 7ac95076a5be / 第 1 页 / 左上 J1/U7/L1/R1-R3/C2-C5/C32-C33

### P1 模块供电电压选择

S1 SW-SPDT 的两路输入分别为 +12V 与 +5.4V，公共端连接 P1 2-pin 接口，允许插接模块在两种底板电源之间选择；P2 2-pin 在该页标为未连接。

- 参数与网络：`option_a=+12V`；`option_b=+5.4V`；`output_connector=P1`
- 证据：图 7ac95076a5be / 第 1 页 / 左中 S1/P1/P2

### +5.4V 到 M5-Bus +5V

+5.4V 通过 D1/D2 两颗 SS54 并联送到 J2 pin28 +5V；J2 pins25/27/29 为 HPWR，pin30 为 BATTERY，pin12 为 +3.3V。

- 参数与网络：`source=+5.4V`；`bus_5v_pin=28`；`diodes=D1,D2 SS54`
- 证据：图 7ac95076a5be / 第 1 页 / 右侧 J2 pins12/25/27-30 与 D1/D2

## 接口

### 30-pin M5Stack_BUS

J2 pins1/3/5 为 GND；pins2/4/6 为 GPIO35/GPIO36/EN；pins7-24 依次引出 GPIO23/GPIO25、GPIO19/GPIO26、GPIO18/+3.3V、GPIO3/GPIO1、GPIO16/GPIO17、GPIO21/GPIO22、GPIO2/GPIO5、GPIO12/GPIO13、GPIO15/GPIO0；pins25-30 为 HPWR/GPIO34/HPWR/+5V/HPWR/BATTERY。

- 参数与网络：`connector_pins=30`；`connector=M5Stack_BUS`
- 证据：图 7ac95076a5be / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30

### M5-Bus UART 拨码路由

S2 六位拨码把 G17/G0/G13 三路候选接到 RXD 公共网络，把 G16/G5/G15 三路候选接到 TXD 公共网络；P4 2-pin 连接 RXD/TXD，可通过拨码适配不同 M5 主机的 UART 引脚。

- 参数与网络：`rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4`
- 证据：图 7ac95076a5be / 第 1 页 / 中下 S2 SW DIP-6、G17/G0/G13/G16/G5/G15 与 RXD/TXD；左下 P4

### P1-P5 插接模块接口

P1 为 S1 选择后的两针电源，P2 两针未连接，P3 三针含 GND 与控制网络，P4 两针为 RXD/TXD，P5 四针含 O+、IN+ 与两脚 GND；S3 六位拨码连接 EN、MIC、G25、G26、O+、IN+ 等适配网络。

- 参数与网络：`power=P1`；`uart=P4`；`audio=P5`；`configuration_switch=S3`
- 证据：图 7ac95076a5be / 第 1 页 / 左中/左下 P1-P5、S3、EN/MIC/G25/G26/O+/IN+

## 音频

### 底板 MIC 与通用音频脚

U1 MIC 一端接 GND，信号 MIC 接 S3；P5 引出 O+、IN+ 与 GND，用于插接模块的通用音频连接。当前页没有 LTE-Data 核心小板的音频接口或用途说明。

- 参数与网络：`microphone_net=MIC`；`output_net=O+`；`input_net=IN+`
- 证据：图 7ac95076a5be / 第 1 页 / 左下 U1 MIC、P5 与 S3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | COMX 通用插接底板架构 | `schematic_page_count=1`；`visible_scope=COMX baseboard` |
| 系统结构 | LTE-Data 核心小板未覆盖 | `documented_module=A7600C1`；`visible_module=null` |
| 电源 | +12V 到 +5.4V 降压 | `input=+12V`；`output=+5.4V`；`inductor_uh=4.7`；`converter=JW5033H` |
| 电源 | P1 模块供电电压选择 | `option_a=+12V`；`option_b=+5.4V`；`output_connector=P1` |
| 电源 | +5.4V 到 M5-Bus +5V | `source=+5.4V`；`bus_5v_pin=28`；`diodes=D1,D2 SS54` |
| 接口 | 30-pin M5Stack_BUS | `connector_pins=30`；`connector=M5Stack_BUS` |
| 接口 | M5-Bus UART 拨码路由 | `rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4` |
| 接口 | P1-P5 插接模块接口 | `power=P1`；`uart=P4`；`audio=P5`；`configuration_switch=S3` |
| 音频 | 底板 MIC 与通用音频脚 | `microphone_net=MIC`；`output_net=O+`；`input_net=IN+` |
| 电源 | DC 5-12V 输入范围 | `documented_input_v=5-12`；`schematic_input_label=+12V` |
| 核心器件 | A7600C1 LTE 通讯模组 | `documented_module=A7600C1` |
| 接口 | MicroSIM 与两路状态 LED | `documented_sim=MicroSIM`；`documented_status_leds=2` |
| 射频 | LTE-TDD、LTE-FDD 与 900/1800MHz 蜂窝频段 | `documented_lte_tdd=B34,B38,B39,B40,B41`；`documented_lte_fdd=B1,B3,B5,B8`；`documented_2g_mhz=900,1800` |
| 接口 | LTE Cat 1 与 LTE CAT4 描述冲突 | `description_category=LTE CAT4`；`feature_category=LTE Cat 1`；`documented_uplink_mbps=5`；`documented_downlink_mbps=10` |
| 接口 | EDGE 与 GPRS 数据速率 | `documented_edge_kbps=236.8`；`documented_gprs_kbps=85.6` |
| 接口 | IP、应用层与主机侧协议 | `documented_protocols=TCP/IP,IPv4,IPv6,MultiPDP,FTP,FTPS,HTTP,HTTPS,DNS,RNDIS,PPP,ECM,SSL,UDP,MQTT` |
| 射频 | 外置 SMA 天线与射频链路 | `documented_connector=SMA`；`documented_antenna=external antenna` |
| 接口 | UART 115200bps 与 AT 指令协议 | `documented_baud=115200`；`documented_protocol=AT command` |
| 接口 | Fire 主控兼容拨码方向 | `documented_tx=G0,G13`；`documented_rx=G5,G15`；`schematic_rxd_candidates=G17,G0,G13`；`schematic_txd_candidates=G16,G5,G15` |

## 待确认事项

- `system.lte-core-not-shown`：正文称产品包含 A7600C1 LTE 通讯模组，但当前资源没有 A7600C1、MicroSIM、状态 LED、蜂窝射频、SMA 天线或数据接口电路，因此不能用该页验证 LTE-Data 核心小板硬件。（证据：图 7ac95076a5be / 第 1 页 / 整页无 A7600C1、MicroSIM、状态 LED 或蜂窝射频链路）
- `power.documented-dc-range`：正文称 DC 接口允许 5-12V 输入；原理图把 J1 输入网络直接命名为 +12V，并按 +12V 设计 JW5033H 到 +5.4V 的降压路径，没有标最小 5V、输入容差、欠压锁定或完整允许范围。（证据：图 7ac95076a5be / 第 1 页 / 左侧 J1/U7 输入仅标 +12V）
- `component.documented-a7600c1`：正文称 LTE 核心小板采用 A7600C1；当前底板图没有 A7600C1 器件、引脚、供电、时钟、复位、USB、UART、SIM 或射频连接，量产模组型号、硬件版本及配套 AT 手册需由核心小板原理图和 BOM 确认。（证据：图 7ac95076a5be / 第 1 页 / 整页无 A7600C1 器件）
- `interface.documented-sim-led`：正文称产品使用 MicroSIM 并有两路 LED 状态指示；当前底板图没有 SIM 卡座、SIM 电源与 ESD、卡检测、LED 位号或驱动网络，无法验证接口规格和指示含义。（证据：图 7ac95076a5be / 第 1 页 / 整页无 SIM 卡座或状态 LED）
- `rf.documented-cellular-bands`：正文列出 LTE-TDD B34/B38/B39/B40/B41、LTE-FDD B1/B3/B5/B8，以及 GSM/GPRS/EDGE 900/1800MHz；当前底板图没有蜂窝基带、射频前端、匹配、滤波或天线电路，无法验证频段组合和区域版本。（证据：图 7ac95076a5be / 第 1 页 / 整页无蜂窝射频器件或网络）
- `network.documented-lte-category`：同一正文的描述段称传输速率为 LTE.CAT4 标准，产品特性段却写 LTE Cat 1 并列出上行 5Mbps、下行 10Mbps；当前底板图没有 LTE 模组或高速数据接口，无法判定量产产品类别和速率。（证据：图 7ac95076a5be / 第 1 页 / 整页无 LTE 模组、类别或数据速率标注）
- `network.documented-2g-rates`：正文称 EDGE 上下行最大 236.8Kbps、GPRS 上下行最大 85.6Kbps；当前底板图没有 A7600C1、蜂窝协议栈、数据接口或测试条件，无法验证这些速率及其网络配置。（证据：图 7ac95076a5be / 第 1 页 / 整页无蜂窝数据路径或速率标注）
- `network.documented-protocols`：正文列出 TCP/IP、IPv4、IPv6、MultiPDP、FTP、FTPS、HTTP、HTTPS、DNS、RNDIS、PPP、ECM、SSL，并在规格表另列 UDP 与 MQTT；底板图不包含模组固件、USB 或网络协议栈，具体协议支持和固件版本无法从原理图确认。（证据：图 7ac95076a5be / 第 1 页 / 整页无网络协议栈或 USB 数据接口）
- `rf.documented-sma-antenna`：正文和包装内容称产品搭配外置 SMA 天线；底板图没有 SMA、IPEX、天线匹配、射频馈线或 ESD 器件，外部天线连接、阻抗和保护方式需由 LTE 核心小板与结构资料确认。（证据：图 7ac95076a5be / 第 1 页 / 整页无 SMA、天线匹配或射频保护电路）
- `interface.documented-uart-at`：正文称模块采用 UART 115200bps 和 AT 指令控制；底板图只确认 RXD/TXD 路由与拨码候选，不包含串口电平、波特率、帧格式、流控或固件协议。（证据：图 7ac95076a5be / 第 1 页 / S2/P4 仅显示 RXD/TXD 硬件路由）
- `interface.documented-fire-routing`：正文因 Fire 的 G16/G17 PSRAM 冲突，建议使用 TX G0/G13 与 RX G5/G15；但原理图把 G0/G13 接到名为 RXD 的公共网络，把 G5/G15 接到名为 TXD 的公共网络。主机侧与模组侧方向命名可能相反，实际拨码方向需结合核心小板接口定义确认。（证据：图 7ac95076a5be / 第 1 页 / S2 将 G17/G0/G13 标到 RXD，将 G16/G5/G15 标到 TXD）
- `review.lte-core-scope`：Module COMX LTE-Data 的 A7600C1 核心小板应使用哪份完整原理图；原因：当前资源只覆盖 COMX 通用底板，不含 LTE 核心、SIM 与射频电路。
- `review.dc-input-range`：J1 与 U7 的量产 DC 输入允许范围是否完整覆盖 5-12V；原因：图面只把输入标为 +12V，没有范围或欠压条件。
- `review.a7600c1-module`：M031-E 量产核心小板的蜂窝模组是否为 A7600C1及哪个硬件版本和 AT 手册版本；原因：底板原理图没有 LTE 模组器件或 BOM 信息。
- `review.sim-led`：核心小板的 MicroSIM 接口、热插拔保护和两路 LED 指示含义如何实现；原因：当前底板图没有 SIM 或 LED 电路。
- `review.cellular-bands`：M031-E 量产版本实际支持哪些 LTE-TDD、LTE-FDD 和 2G 频段及区域认证；原因：底板资源不包含蜂窝射频核心、前端或区域版本信息。
- `review.lte-category`：M031-E 应标为 LTE Cat 1 还是 LTE CAT4，量产上下行峰值速率是多少；原因：同一源文档的描述段与产品特性段互相冲突，底板图无法裁决。
- `review.2g-rates`：EDGE 236.8Kbps 与 GPRS 85.6Kbps 指标适用哪些网络类别和测试条件；原因：当前资源没有蜂窝数据路径或性能测试边界。
- `review.network-protocols`：A7600C1 量产固件实际启用哪些 IP、应用层和主机侧协议；原因：协议能力属于模组固件，且产品特性与规格表列出的协议集合不同。
- `review.sma-antenna`：LTE 核心小板的 SMA 天线接口、匹配、阻抗和保护电路如何实现；原因：当前底板图没有任何蜂窝天线或射频匹配电路。
- `review.uart-at`：量产固件默认 UART 是否为 115200bps，帧格式、流控及 AT 指令集版本是什么；原因：底板图只画 UART 拨码路由，串口配置和协议取决于 LTE 模组固件。
- `review.fire-routing`：Fire 主控与 LTE 核心小板之间 TX/RX 的方向命名和正确拨码组合是什么；原因：正文的 TX/RX GPIO 分组与底板原理图上的 RXD/TXD 网络标签相反。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7ac95076a5be6f11c33d7a67e2f609c3571bb469f4ff2de9bad10749f482a9da` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_sch_01.webp` |

---

源文档：`zh_CN/module/comx_lte-data.md`

源文档 SHA-256：`7e532ef3e111abb8d7e8a905d5229828c78102eb163b83a8944373e413c122ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
