# Module COMX LTE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX LTE |
| SKU | M031-A |
| 产品 ID | `module-comx-lte-20b73553b7c9` |
| 源文档 | `zh_CN/module/comx_lte.md` |

## 概述

当前唯一原理图资源展示带 J3 Phonejack 的 COMX 通用插接底板：J1 DC 输入的 +12V 经 U7 JW5033H 降压为 +5.4V，S1 在 +12V/+5.4V 之间选择模块供电，J2 M5Stack_BUS 通过 D1/D2 接收 +5.4V，S2 六位拨码把多组 M5-Bus GPIO 路由到 RXD/TXD；U1 MIC、P5 和 J3 提供通用音频连接。页面没有 SIM7600G、MicroSIM、状态 LED、SMA、蜂窝射频或核心 USB 电路，因此 LTE Cat4、频段、速率、语音/SMS、协议和固件能力均列为待确认。

## 检索关键词

`Module COMX LTE`、`M031-A`、`COMX baseboard`、`SIM7600G`、`LTE Cat4`、`LTE-TDD`、`LTE-FDD`、`WCDMA`、`GSM`、`GPRS`、`EDGE`、`MicroSIM`、`SMA`、`Phonejack`、`3.5mm headset`、`JW5033H`、`PWR2.5`、`+12V`、`+5.4V`、`SW-SPDT`、`SW DIP-6`、`M5Stack_BUS`、`SS54`、`RXD`、`TXD`、`G17`、`G0`、`G13`、`G16`、`G5`、`G15`、`G25`、`G26`、`EN`、`MIC`、`O+`、`IN+`、`SS8550 Y2`、`UART 115200bps`、`AT command`、`RNDIS`、`ECM`、`IPv4`、`IPv6`、`FOTA`、`5-12V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | JW5033H | +12V 到 +5.4V 的底板降压转换器 | 图 2af2c8cc6c57 / 第 1 页 / 左上 U7 JW5033H、L1 与 +12V/+5.4V |
| J1 | PWR2.5 | COMX 底板外部 DC 电源输入插座 | 图 2af2c8cc6c57 / 第 1 页 / 左中 J1 PWR2.5，连接 +12V 与 GND |
| S1 | SW-SPDT | 在 +12V 与 +5.4V 之间选择 P1 插接模块供电 | 图 2af2c8cc6c57 / 第 1 页 / 左中 S1 SW-SPDT、+12V/+5.4V 与 P1 |
| J2 | M5Stack_BUS | 30-pin M5-Bus 堆叠连接器 | 图 2af2c8cc6c57 / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30 |
| S2,S3 | SW DIP-6 | M5-Bus UART GPIO 路由与插接模块音频/控制配置拨码开关 | 图 2af2c8cc6c57 / 第 1 页 / 中下 S2/S3 SW DIP-6 |
| D1,D2 | SS54 | +5.4V 到 M5-Bus +5V/BATTERY 电源脚的肖特基隔离 | 图 2af2c8cc6c57 / 第 1 页 / 右下 J2 pins28/30 与 +5.4V 之间 D1/D2 SS54 |
| P1,P2,P3,P4,P5 | 2p/3p/4p module headers | COMX 插接核心的电源、UART、控制和音频连接器 | 图 2af2c8cc6c57 / 第 1 页 / 左中至左下 P1-P5，2p/3p/4p 接口 |
| Q1,U1 | SS8550 Y2 / MIC | S3 配置网络中的晶体管控制级与底板麦克风 | 图 2af2c8cc6c57 / 第 1 页 / 左下 Q1 SS8550 Y2、U1 MIC、R4-R6 与 S3 |
| J3 | Phonejack | 连接 O+、IN+ 与 GND 的底板耳机插座 | 图 2af2c8cc6c57 / 第 1 页 / 页面中上 J3 Phonejack，O+/IN+/GND |

## 系统结构

### COMX LTE 通用插接底板架构

页面明确显示 COMX 底板：包含 J1 DC 输入、U7 5.4V 降压、S1 电源选择、J2 M5Stack_BUS、S2/S3 拨码、P1-P5 模块插座、Q1 控制级、U1 MIC 与 J3 Phonejack。

- 参数与网络：`schematic_page_count=1`；`visible_scope=COMX baseboard`；`audio=U1 MIC+P5+J3 Phonejack`；`core_scope=null`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 整页 COMX 底板电源、M5-Bus、拨码、插座与 Phonejack

## 电源

### +12V 到 +5.4V 降压

J1 PWR2.5 输入网络标为 +12V；U7 JW5033H 以 R1 100 kΩ 偏置 EN，经 L1 4.7 uH 和 R2/R3 115 kΩ/20 kΩ 反馈输出 +5.4V，输入端 C2/C3 各 10 uF，输出端 C32/C33 各 22 uF并配 C4 100 nF。

- 参数与网络：`input=+12V`；`output=+5.4V`；`converter=U7 JW5033H`；`inductor=L1 4.7uH`；`feedback=R2 115k,R3 20k`；`input_caps=C2 10uF,C3 10uF`；`output_caps=C32 22uF,C33 22uF,C4 100nF`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 左上 J1/U7/L1/R1-R3/C2-C5/C32-C33

### P1 插接核心供电电压选择

S1 SW-SPDT 的两路输入分别为 +12V 与 +5.4V，公共端连接 P1 2-pin 接口；P2 2-pin 的两脚在该页均标为未连接。

- 参数与网络：`option_a=+12V`；`option_b=+5.4V`；`output_connector=P1`；`unused_connector=P2`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 左中 S1/P1/P2

### +5.4V 与 M5-Bus 电源脚

+5.4V 通过 D1/D2 两颗 SS54 分别连接 J2 的 +5V 与 BATTERY 电源脚；J2 pins25/27/29 为 HPWR，pin12 为 +3.3V，pin28 为 +5V，pin30 为 BATTERY。

- 参数与网络：`source=+5.4V`；`diodes=D1,D2 SS54`；`logic_rail=pin12 +3.3V`；`power_pins=pin25 HPWR,pin27 HPWR,pin28 +5V,pin29 HPWR,pin30 BATTERY`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 右侧 J2 pins12/25/27-30 与 D1/D2/+5.4V

## 接口

### 30-pin M5Stack_BUS

J2 pins1/3/5 为 GND；pins2/4/6 为 GPIO35/GPIO36/EN；pins7-24 依次引出 GPIO23/GPIO25、GPIO19/GPIO26、GPIO18/+3.3V、GPIO3/GPIO1、GPIO16/GPIO17、GPIO21/GPIO22、GPIO2/GPIO5、GPIO12/GPIO13、GPIO15/GPIO0；pins25-30 为 HPWR/GPIO34/HPWR/+5V/HPWR/BATTERY。

- 参数与网络：`connector=J2 M5Stack_BUS`；`pins=30`；`ground=1,3,5`；`uart_candidates=GPIO16,GPIO17,GPIO5,GPIO13,GPIO15,GPIO0`；`rails=pin12 +3.3V,pin28 +5V,pin30 BATTERY`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 右侧 J2 M5Stack_BUS pins1-30

### M5-Bus UART 拨码路由

S2 六位拨码把 G17/G0/G13 三路候选连接到 RXD 公共网络，把 G16/G5/G15 三路候选连接到 TXD 公共网络；P4 2-pin 引出 RXD/TXD。

- 参数与网络：`rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4`；`switch=S2 SW DIP-6`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 中下 S2 SW DIP-6、G17/G0/G13/G16/G5/G15 与 RXD/TXD；左下 P4

### P1-P5 插接核心接口

P1 为 S1 选择后的两针电源，P2 两针未连接，P3 三针包含 GND 与控制网络，P4 两针为 RXD/TXD，P5 四针包含 O+、IN+ 与两脚 GND；S3 六位拨码连接 EN、MIC、G25、G26、O+、IN+ 等适配网络。

- 参数与网络：`power=P1`；`unused=P2`；`control=P3`；`uart=P4 RXD/TXD`；`audio=P5 O+/IN+/GND/GND`；`configuration_switch=S3`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 左中/左下 P1-P5、S3、EN/MIC/G25/G26/O+/IN+

## 音频

### 底板麦克风与音频选择

U1 MIC 一端接 GND，信号 MIC 接 S3；S3 还连接 EN、G25、G26、O+ 和 IN+，Q1 SS8550 Y2 与 R4-R6 组成该选择网络的控制级。

- 参数与网络：`microphone=U1 MIC`；`microphone_net=MIC`；`switch=S3`；`audio_nets=O+,IN+`；`control=Q1 SS8550 Y2,R4-R6`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 左下 U1 MIC、Q1、R4-R6 与 S3

### J3 Phonejack 音频接口

J3 标为 Phonejack，其触点网络包括 O+、IN+ 与 GND；O+/IN+ 同时由 P5 引出并连接 S3 配置网络。

- 参数与网络：`connector=J3 Phonejack`；`output=O+`；`input=IN+`；`ground=GND`；`module_header=P5`；`switch=S3`
- 证据：图 2af2c8cc6c57 / 第 1 页 / 页面中上 J3 Phonejack 与左下 P5/S3 的 O+/IN+ 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | COMX LTE 通用插接底板架构 | `schematic_page_count=1`；`visible_scope=COMX baseboard`；`audio=U1 MIC+P5+J3 Phonejack`；`core_scope=null` |
| 电源 | +12V 到 +5.4V 降压 | `input=+12V`；`output=+5.4V`；`converter=U7 JW5033H`；`inductor=L1 4.7uH`；`feedback=R2 115k,R3 20k`；`input_caps=C2 10uF,C3 10uF`；`output_caps=C32 22uF,C33 22uF,C4 100nF` |
| 电源 | P1 插接核心供电电压选择 | `option_a=+12V`；`option_b=+5.4V`；`output_connector=P1`；`unused_connector=P2` |
| 电源 | +5.4V 与 M5-Bus 电源脚 | `source=+5.4V`；`diodes=D1,D2 SS54`；`logic_rail=pin12 +3.3V`；`power_pins=pin25 HPWR,pin27 HPWR,pin28 +5V,pin29 HPWR,pin30 BATTERY` |
| 接口 | 30-pin M5Stack_BUS | `connector=J2 M5Stack_BUS`；`pins=30`；`ground=1,3,5`；`uart_candidates=GPIO16,GPIO17,GPIO5,GPIO13,GPIO15,GPIO0`；`rails=pin12 +3.3V,pin28 +5V,pin30 BATTERY` |
| 接口 | M5-Bus UART 拨码路由 | `rx_candidates=G17,G0,G13`；`tx_candidates=G16,G5,G15`；`module_uart_connector=P4`；`switch=S2 SW DIP-6` |
| 接口 | P1-P5 插接核心接口 | `power=P1`；`unused=P2`；`control=P3`；`uart=P4 RXD/TXD`；`audio=P5 O+/IN+/GND/GND`；`configuration_switch=S3` |
| 音频 | 底板麦克风与音频选择 | `microphone=U1 MIC`；`microphone_net=MIC`；`switch=S3`；`audio_nets=O+,IN+`；`control=Q1 SS8550 Y2,R4-R6` |
| 音频 | J3 Phonejack 音频接口 | `connector=J3 Phonejack`；`output=O+`；`input=IN+`；`ground=GND`；`module_header=P5`；`switch=S3` |
| 系统结构 | SIM7600G LTE 核心小板未覆盖 | `documented_module=SIM7600G`；`visible_scope=COMX baseboard`；`visible_module=null` |
| 核心器件 | SIM7600G LTE 通讯模组 | `documented_module=SIM7600G`；`reference=null`；`exact_variant=null`；`supply=null`；`clock=null`；`reset=null`；`usb=null` |
| 接口 | MicroSIM 与两路状态 LED | `documented_sim=MicroSIM`；`documented_status_leds=2`；`sim_connector=null`；`sim_protection=null`；`led_drivers=null` |
| 射频 | SIM7600G 蜂窝频段集合 | `documented_lte_tdd=B34,B38,B39,B40,B41`；`documented_lte_fdd=B1,B2,B3,B4,B5,B7,B8,B12,B13,B18,B19,B20,B25,B26,B28,B66`；`documented_wcdma=B1,B2,B4,B5,B6,B8,B19`；`documented_2g_mhz=850,900,1800,1900`；`hardware_variant=null` |
| 接口 | LTE Cat4 峰值速率 | `documented_category=LTE Cat4`；`documented_uplink_mbps=50`；`documented_downlink_mbps=150`；`test_conditions=null` |
| 接口 | HSPA+、WCDMA、EDGE/GPRS 速率 | `documented_hspa_uplink_mbps=5.76`；`documented_hspa_downlink_mbps=42`；`documented_wcdma_kbps=384`；`documented_edge_gprs_kbps=236.8`；`test_conditions=null` |
| 接口 | IP、应用层与主机侧协议 | `documented_protocols=TCP/IP,IPv4,IPv6,Multi-PDP,FTP,FTPS,HTTP,HTTPS,DNS,TLS,RNDIS,ECM,FOTA`；`firmware_version=null`；`usb_data_path=null` |
| 接口 | 语音、SMS 与蜂窝数据能力 | `documented_voice=true`；`documented_sms=true`；`documented_cellular_data=true`；`baseboard_audio=U1 MIC,J3 Phonejack,P5 O+/IN+`；`core_audio=null`；`core_data=null` |
| 射频 | 外置 SMA 蜂窝天线 | `documented_connector=SMA`；`documented_antenna=external cellular antenna`；`impedance=null`；`matching=null`；`protection=null` |
| 接口 | UART 115200bps 与 AT 指令 | `documented_baud=115200`；`documented_protocol=AT command`；`frame_format=null`；`flow_control=null`；`at_version=null` |
| 音频 | 3.5mm 耳机与 17mm 插头适配 | `documented_jack=3.5mm`；`documented_plug_length=17mm`；`documented_headset_microphone=true`；`schematic_connector=J3 Phonejack`；`contact_standard=null`；`insert_detect=null` |
| 电源 | DC 5-12V 输入范围 | `documented_input=5-12V`；`schematic_input_label=+12V`；`undervoltage_lockout=null`；`tolerance=null` |
| 接口 | Fire 主机 UART 拨码说明 | `documented_avoid=G16,G17`；`documented_tx=G0,G13`；`documented_rx=G5,G15`；`schematic_rxd_candidates=G17,G0,G13`；`schematic_txd_candidates=G16,G5,G15`；`direction_perspective=null` |

## 待确认事项

- `system.lte-core-not-shown`：源文档称产品内置 SIM7600G；当前资源没有 SIM7600G、MicroSIM、状态 LED、蜂窝射频、SMA 天线或核心 USB 电路，因此该页不能验证 LTE 核心小板硬件。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无 SIM7600G、MicroSIM、状态 LED、SMA 或蜂窝核心电路）
- `component.documented-sim7600g`：源文档把 SIM7600G 列为 LTE 核心模组；当前底板图没有该器件的位号、完整子型号、引脚、供电、时钟、复位、USB、UART、SIM 或射频连接。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页未出现 SIM7600G）
- `interface.documented-sim-led`：源文档称产品使用 MicroSIM 并带两路 LED 状态信号；当前底板图没有 SIM 卡座、SIM 电源与 ESD、卡检测、LED 位号或驱动网络。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无 SIM 卡座或状态 LED）
- `rf.documented-cellular-bands`：源文档列出 LTE-TDD B34/B38/B39/B40/B41，LTE-FDD B1/B2/B3/B4/B5/B7/B8/B12/B13/B18/B19/B20/B25/B26/B28/B66，WCDMA B1/B2/B4/B5/B6/B8/B19，以及 GSM/GPRS/EDGE 850/900/1800/1900MHz；当前底板图没有蜂窝基带、射频前端、匹配、滤波或天线电路。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无蜂窝射频器件、滤波或频段标识）
- `interface.documented-lte-cat4`：源文档明确称 LTE Cat4 上行最大 50Mbps、下行最大 150Mbps；当前底板图没有 SIM7600G、高速数据接口、天线或性能测试边界。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无 LTE 核心、类别或速率标注）
- `interface.documented-legacy-rates`：源文档列出 HSPA+ 上行 5.76Mbps/下行 42Mbps、WCDMA 上下行 384Kbps、EDGE/GPRS 上下行 236.8Kbps；当前底板图没有蜂窝协议栈、数据路径或测试条件。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无蜂窝核心或数据速率标注）
- `interface.documented-network-protocols`：源文档列出 TCP/IP、IPv4、IPv6、Multi-PDP、FTP、FTPS、HTTP、HTTPS、DNS、TLS、RNDIS、ECM 和 FOTA；底板图不包含 SIM7600G 固件、USB 数据线路或网络协议栈。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无网络协议栈或核心 USB 数据接口）
- `interface.documented-voice-sms-data`：源文档称产品支持语音通话、SMS 短信和蜂窝数据传输；图面确认底板存在 MIC、Phonejack 和 O+/IN+ 网络，但没有 SIM7600G 音频引脚、编解码、SIM、协议栈或数据接口，不能从该页证明端到端能力。（证据：图 2af2c8cc6c57 / 第 1 页 / U1/J3/P5 仅为底板音频网络，整页无 SIM7600G 核心接口）
- `rf.documented-sma-antenna`：源文档和包装内容称产品搭配 SMA 天线；底板图没有 SMA、IPEX、天线匹配、射频馈线或 ESD 器件。（证据：图 2af2c8cc6c57 / 第 1 页 / 整页无 SMA、天线匹配或射频保护电路）
- `interface.documented-uart-at`：源文档称模块采用 UART 115200bps 和 AT 指令控制；底板图只确认 RXD/TXD 路由与拨码候选，不包含串口电平、波特率、帧格式、流控或固件协议。（证据：图 2af2c8cc6c57 / 第 1 页 / S2/P4 仅显示 RXD/TXD 硬件路由）
- `audio.documented-headset`：源文档称 J3 为 3.5mm 耳机孔，需使用 17mm 长的带麦克风插头，并可通过 S3 启用板载麦克风；图面确认 Phonejack、MIC 和选择网络，但没有机械尺寸、触点标准、插入检测或插头兼容表。（证据：图 2af2c8cc6c57 / 第 1 页 / J3 仅标 Phonejack，U1/S3 为 MIC 选择，无机械尺寸或插头标准）
- `power.documented-dc-range`：源文档称 DC 接口允许 5-12V 输入；原理图把 J1 输入网络直接命名为 +12V，并按 +12V 设计 JW5033H 到 +5.4V 的降压路径，没有标最小 5V、输入容差、欠压锁定或完整允许范围。（证据：图 2af2c8cc6c57 / 第 1 页 / 左侧 J1/U7 输入仅标 +12V）
- `interface.fire-routing-perspective`：源文档为避免 Fire 的 G16/G17 PSRAM 冲突，要求选择 TX(G0/G13)、RX(G5/G15)；图面网络名则把 G0/G13 归入 RXD 候选、G5/G15 归入 TXD 候选，需确认文档采用主机视角还是模块视角。（证据：图 2af2c8cc6c57 / 第 1 页 / 中下 S2：G17/G0/G13 接 RXD，G16/G5/G15 接 TXD）
- `review.lte-core-scope`：Module COMX LTE 的 SIM7600G 核心小板应使用哪份完整原理图？；原因：当前资源只覆盖 COMX 通用底板，不含 LTE 核心、SIM、射频与核心 USB 电路。
- `review.sim7600g-module`：M031-A 量产核心的完整 SIM7600G 子型号、硬件版本、电源、时钟、复位和接口定义是什么？；原因：底板原理图没有 LTE 模组器件或 BOM 信息。
- `review.sim-led`：核心小板的 MicroSIM 接口、热插拔保护和两路 LED 指示含义如何实现？；原因：当前底板图没有 SIM 或 LED 电路。
- `review.cellular-bands`：M031-A 量产版本实际支持哪些 LTE-TDD、LTE-FDD、WCDMA 和 2G 频段及区域认证？；原因：底板资源不包含蜂窝射频核心、前端或区域版本信息。
- `review.lte-cat4`：LTE Cat4 上行 50Mbps、下行 150Mbps 指标适用于哪个 SIM7600G 子型号、网络和测试条件？；原因：当前底板图没有 LTE 核心或性能测试边界。
- `review.legacy-rates`：HSPA+、WCDMA、EDGE/GPRS 的峰值速率适用哪些网络类别和测试条件？；原因：当前资源没有蜂窝数据路径或性能测试证据。
- `review.network-protocols`：SIM7600G 量产固件实际启用哪些 IP、应用层、USB 网络和 FOTA 能力？；原因：协议能力属于核心固件，底板图没有 USB 数据链或协议栈。
- `review.voice-sms-data`：SIM7600G 核心如何连接底板 O+/IN+，语音、SMS 与数据能力对应哪些固件和运营商条件？；原因：当前页面只显示底板音频，未显示核心音频、SIM 与数据接口。
- `review.sma-antenna`：LTE 核心小板的 SMA 天线接口、匹配、阻抗和保护电路如何实现？；原因：当前底板图没有蜂窝天线或射频匹配电路。
- `review.uart-at`：量产固件默认 UART 是否为 115200bps，帧格式、流控及 AT 指令集版本是什么？；原因：底板图只画 UART 拨码路由，串口配置取决于 LTE 核心固件。
- `review.headset`：J3 的 3.5mm 触点标准、17mm 插头机械要求、插入检测和板载/耳机麦克风切换真值是什么？；原因：图面只标 Phonejack 和音频网络，未给机械与触点规格。
- `review.dc-input-range`：J1 与 U7 的量产 DC 输入允许范围是否完整覆盖 5-12V？；原因：图面只把输入标为 +12V，没有范围、容差或欠压条件。
- `review.fire-uart-perspective`：Fire 兼容说明中的 TX/RX 是主机视角还是 LTE 核心视角，实际拨码应如何标注？；原因：源文档的 TX(G0/G13)、RX(G5/G15) 与图面 RXD/TXD 网络名方向相反。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2af2c8cc6c5778a3cd6142f2eec8bb229a9448b56cbe1de6f73b3a8c1d11364b` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_sch_01.webp` |

---

源文档：`zh_CN/module/comx_lte.md`

源文档 SHA-256：`421e1a72bf2ce08b11bceff9637e562d6a3fe3c025c8e5e783e49d280ca20376`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
