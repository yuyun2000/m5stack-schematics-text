# Module COMX Cat1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX Cat1 |
| SKU | M031-H |
| 产品 ID | `module-comx-cat1-6bc022329978` |
| 源文档 | `zh_CN/module/comx_cat1.md` |

## 概述

当前唯一原理图资源展示 SIM-A7680C 核心小板电路：M1 蜂窝模组连接 SIM 卡座与 SMF05CT1G 防护、VBAT 与 1.8V 电源、ANT_IPEX 射频端、PWRKEY/RESET、NETLIGHT 指示，以及由 SS8050 构成的 1.8V/3.3V UART 电平转换。该页未画 COMX 底板的 M5-Bus、DC 5/12V、电源转换或拨码切换电路。

## 检索关键词

`Module COMX Cat1`、`M031-H`、`SIM-A7680C`、`LTE CAT1`、`USIM_DATA`、`USIM_CLK`、`USIM_RST`、`USIM_VDD`、`SIM_VCC`、`SMF05CT1G`、`U1_TX`、`U1_RX`、`M_TXD`、`M_RXD`、`SS8050 Y1`、`NETLIGHT`、`STATUS`、`PWRKEY`、`RESET`、`VBAT`、`VDD_EXT`、`+1.8V`、`+3.3V`、`ANT_MAIN`、`ANT_IPEX`、`SMA`、`Nano SIM`、`M5-Bus`、`DC 5/12V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM-A7680C | 蜂窝通信模组，提供 UART、USIM、USB、天线、状态、电源与控制引脚 | 图 8af2efaa697d / 第 1 页 / 中央 M1 SIM-A7680C pins1-42 |
| U2 | SIM | USIM 卡座，连接 IO/CLK/RST/VCC 与 GND | 图 8af2efaa697d / 第 1 页 / 左侧 U2 SIM 卡座 |
| U1 | SMF05CT1G | SIM_VCC、USIM_DATA/CLK/RST 多线 ESD 防护 | 图 8af2efaa697d / 第 1 页 / 左上 U1 SMF05CT1G，连接 SIM 接口信号与 GND |
| Q2,Q3 | SS8050 Y1 | M_RXD/M_TXD 与 U1_RX/U1_TX 之间的 3.3V/1.8V UART 电平转换 | 图 8af2efaa697d / 第 1 页 / 下中 Q2/Q3 SS8050 Y1 与 R8-R13 |
| Q1,D1 | SS8050 Y1 / LED 0603 | NETLIGHT 蜂窝网络状态指示灯驱动 | 图 8af2efaa697d / 第 1 页 / 右下 Q1 SS8050 Y1、D1 0603 与 NETLIGHT |
| E1 | ANT_IPEX | SIM-A7680C ANT_MAIN 射频天线接口 | 图 8af2efaa697d / 第 1 页 / 右上 M1 pin32 ANT_MAIN 到 E1 ANT_IPEX |

## 系统结构

### SIM-A7680C 核心小板架构

唯一资源以 M1 SIM-A7680C 为核心，连接 U2 SIM 卡座、U1 SMF05CT1G、E1 ANT_IPEX、Q2/Q3 UART 电平转换和 Q1/D1 NETLIGHT 指示；图中还引出 VBAT、VDD_EXT、PWRKEY、RESET、STATUS、USB 与备用 UART 引脚。

- 参数与网络：`schematic_page_count=1`；`cellular_module=SIM-A7680C`
- 证据：图 8af2efaa697d / 第 1 页 / 整页 SIM-A7680C、SIM、UART、NETLIGHT 与天线电路

## 电源

### VBAT、VDD_EXT 与逻辑电源

M1 pins34/35 VBAT 连接 VBAT 主电源，pin40 VDD_EXT 输出 +1.8V；+1.8V 为 UART 模组侧上拉和去耦供电，+3.3V 为主机侧 UART 上拉及 NETLIGHT LED 供电，C1 22uF 对 +1.8V 去耦。

- 参数与网络：`main_supply=VBAT`；`module_io_supply=+1.8V`；`host_io_supply=+3.3V`
- 证据：图 8af2efaa697d / 第 1 页 / M1 pins34/35/40 与 C1、Q2/Q3、D1 电源网络

## 接口

### SIM-A7680C 主 UART

M1 pin1 TXD 连接 U1_TX，pin2 RXD 连接 U1_RX；Q2/Q3 SS8050 Y1 与 R8-R13 在 U1_RX/U1_TX 和 M_RXD/M_TXD 之间实现 1.8V 与 3.3V 电平转换。RTS、CTS、DCD、DTR、RI 标为未连接。

- 参数与网络：`module_tx=U1_TX`；`module_rx=U1_RX`；`host_tx=M_TXD`；`host_rx=M_RXD`；`module_logic_v=1.8`；`host_logic_v=3.3`
- 证据：图 8af2efaa697d / 第 1 页 / M1 pins1-7 与下中 Q2/Q3/R8-R13 UART 电平转换

### USIM 卡接口

M1 USIM_DATA/USIM_CLK/USIM_RST/USIM_VDD 分别连接 U2 IO/CLK/RST/VCC；DATA/CLK/RST 各串联 R5/R6/R7 22Ω并配 C2/C3/C4 33pF 对地，USIM_DET 与 U2 VPP 标为未连接。

- 参数与网络：`data=USIM_DATA`；`clock=USIM_CLK`；`reset=USIM_RST`；`supply=SIM_VCC`；`series_resistor_ohm=22`；`shunt_capacitor_pf=33`
- 证据：图 8af2efaa697d / 第 1 页 / 左侧 U2/U1/R5-R7/C2-C4 与 M1 pins14-18

### STATUS 与 NETLIGHT

M1 pin42 引出 STATUS 但未接后级；pin41 NETLIGHT 经 R2 1K 驱动 Q1 SS8050 Y1，Q1 下拉 D1 LED，D1 由 +3.3V 经 R1 1K 供电，R3 10K 将 NETLIGHT 下拉。

- 参数与网络：`status=STATUS`；`network_led=NETLIGHT`；`led_reference=D1`
- 证据：图 8af2efaa697d / 第 1 页 / M1 pins41/42 与右下 Q1/D1/R1-R3

### 当前页未使用的语音、USB 与备用 UART

M1 MIC_P/MIC_N、SPK_P/SPK_N、USB_BOOT、USB_DN、USB_DP、USB_VBUS、U3_RXD、U3_TXD 在该页均未连接；RTS/CTS/DCD/DTR/RI 与 ADC 也标为未连接。

- 参数与网络：`usb_connected=false`；`audio_connected=false`；`secondary_uart_connected=false`
- 证据：图 8af2efaa697d / 第 1 页 / M1 pins3-7/9-12/22-26/28/37 的 NC 标记或无后级连线

## 复位

### PWRKEY 与 RESET

M1 pin39 PWRKEY 接 C16 10uF 对地，M1 pin29 引出 RESET 网络；图中没有额外按键或主控驱动器。

- 参数与网络：`power_key=PWRKEY`；`reset=RESET`；`powerkey_capacitor_uf=10`
- 证据：图 8af2efaa697d / 第 1 页 / M1 pins29/39 与 C16

## 保护电路

### USIM 多线 ESD 防护

U1 SMF05CT1G 将 SIM_VCC、USIM_DATA、USIM_CLK、USIM_RST 多条 SIM 线路钳位到 GND，位于卡座与 M1 之间。

- 参数与网络：`protector=SMF05CT1G`
- 证据：图 8af2efaa697d / 第 1 页 / 左上 U1 SMF05CT1G 与 SIM 线路

## 射频

### ANT_MAIN 到 ANT_IPEX

M1 pin32 ANT_MAIN 直接连接 E1 ANT_IPEX，E1 另一端接 GND；页面没有匹配网络、射频开关或天线 ESD 器件。

- 参数与网络：`module_net=ANT_MAIN`；`schematic_connector=ANT_IPEX`
- 证据：图 8af2efaa697d / 第 1 页 / 右上 M1 pin32 ANT_MAIN 与 E1 ANT_IPEX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | SIM-A7680C 核心小板架构 | `schematic_page_count=1`；`cellular_module=SIM-A7680C` |
| 系统结构 | 资源与 COMX 底板范围对应关系 | `documented_scope=COMX plug-in baseboard`；`visible_scope=SIM-A7680C core board` |
| 接口 | SIM-A7680C 主 UART | `module_tx=U1_TX`；`module_rx=U1_RX`；`host_tx=M_TXD`；`host_rx=M_RXD`；`module_logic_v=1.8`；`host_logic_v=3.3` |
| 接口 | USIM 卡接口 | `data=USIM_DATA`；`clock=USIM_CLK`；`reset=USIM_RST`；`supply=SIM_VCC`；`series_resistor_ohm=22`；`shunt_capacitor_pf=33` |
| 保护电路 | USIM 多线 ESD 防护 | `protector=SMF05CT1G` |
| 核心器件 | Nano SIM 卡槽规格 | `documented_form_factor=Nano SIM`；`schematic_label=SIM` |
| 电源 | VBAT、VDD_EXT 与逻辑电源 | `main_supply=VBAT`；`module_io_supply=+1.8V`；`host_io_supply=+3.3V` |
| 复位 | PWRKEY 与 RESET | `power_key=PWRKEY`；`reset=RESET`；`powerkey_capacitor_uf=10` |
| 接口 | STATUS 与 NETLIGHT | `status=STATUS`；`network_led=NETLIGHT`；`led_reference=D1` |
| 射频 | ANT_MAIN 到 ANT_IPEX | `module_net=ANT_MAIN`；`schematic_connector=ANT_IPEX` |
| 射频 | 外部天线接口规格 | `documented_connector=SMA`；`schematic_connector=ANT_IPEX` |
| 接口 | 当前页未使用的语音、USB 与备用 UART | `usb_connected=false`；`audio_connected=false`；`secondary_uart_connected=false` |
| 射频 | LTE Cat1 频段与吞吐能力 | `documented_tdd_bands=B34/B38/B39/B40/B41`；`documented_fdd_bands=B1/B3/B5/B8`；`documented_downlink_mbps=10`；`documented_uplink_mbps=5` |
| 接口 | UART 115200bps 8N1 | `documented_baud=115200`；`documented_format=8N1` |
| 接口 | COMX 底板 M5-Bus、DC 输入与拨码切换 | `documented_m5bus_supply_v=5`；`documented_dc_input_v=5/12`；`documented_uart_switch=true` |

## 待确认事项

- `system.resource-scope`：源文档把该图称为 Module COMX 模块插接底板原理图，但页面实际只显示 SIM-A7680C 核心小板功能，没有 M5-Bus、DC 输入、电源转换、堆叠接口或拨码开关，因此当前资源不能覆盖完整 COMX Cat1 底板。（证据：图 8af2efaa697d / 第 1 页 / 整页无 M5-Bus、DC 输入或拨码开关电路）
- `component.documented-sim-form-factor`：正文称卡槽规格为 Nano，原理图 U2 只标 SIM 并给出电气引脚，没有卡座料号、机械尺寸、插拔方向或 Nano 外形标注，实际卡槽规格需由 BOM 或结构资料确认。（证据：图 8af2efaa697d / 第 1 页 / 左侧 U2 仅标 SIM，无机械规格）
- `rf.documented-antenna-connector`：正文称产品集成 SMA 外部天线接口，原理图 E1 明确标 ANT_IPEX；当前资源没有画 IPEX 到 SMA 的转接、馈线或底板连接，因此量产外部接口及两者关系需确认。（证据：图 8af2efaa697d / 第 1 页 / 右上 E1 标注 ANT_IPEX）
- `rf.documented-cat1-capabilities`：正文称 SIM-A7680C 支持 LTE-TDD B34/B38/B39/B40/B41、LTE-FDD B1/B3/B5/B8，并给出最大下行 10Mbps、上行 5Mbps；原理图只确认 SIM-A7680C 型号和天线/SIM/UART 电气连接，没有频段、制式、吞吐或区域版本标注。（证据：图 8af2efaa697d / 第 1 页 / 中央 M1 仅标 SIM-A7680C，无频段/吞吐标注）
- `interface.documented-uart-format`：正文称主 UART 为 115200bps 8N1；原理图确认 UART 及电平转换，但没有波特率、数据位、校验位、停止位或 AT 固件版本标注。（证据：图 8af2efaa697d / 第 1 页 / M1 TXD/RXD 与 Q2/Q3 UART 电平转换，无串口格式标注）
- `interface.documented-comx-baseboard`：正文称底板支持 M5-Bus 5V、DC 5/12V、堆叠接口及拨码选择多组 UART 引脚；当前唯一原理图未画 M5-Bus、DC 插座、稳压器、拨码开关或底板插接连接器，无法验证其针脚与电源边界。（证据：图 8af2efaa697d / 第 1 页 / 整页无 M5-Bus、DC 输入、稳压或拨码切换电路）
- `review.resource-scope`：当前 comx_cat1_sch_01.webp 是 SIM-A7680C 核心小板图还是完整 COMX 插接底板图；原因：源文档称其为 COMX 底板原理图，但页面内容不含 M5-Bus、DC 输入与拨码电路。
- `review.sim-form-factor`：U2 量产 SIM 卡座是否为 Nano SIM 规格；原因：原理图只标 SIM 与电气引脚，没有机械规格或料号。
- `review.antenna-connector`：量产产品对外天线接口是 SMA、IPEX，还是由 IPEX 转接到 SMA；原因：正文称 SMA，原理图只画 E1 ANT_IPEX。
- `review.cat1-capabilities`：M031-H 量产 SIM-A7680C 的频段、区域版本和 10/5Mbps 吞吐条件是否与正文一致；原因：原理图未标 LTE 频段、制式、吞吐或模组区域后缀。
- `review.uart-format`：量产模组默认 UART 是否为 115200bps 8N1；原因：串口格式由固件配置决定，原理图仅能确认硬件 UART 电平路径。
- `review.comx-baseboard`：COMX Cat1 底板的 M5-Bus、DC 5/12V 和拨码 UART 路由应以哪份完整原理图为准；原因：当前资源不包含这些底板电路，无法验证正文针脚表与电源说明。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8af2efaa697de63a458c11b7f222e017c96c29cd8e330ca531168762867c726f` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_sch_01.webp` |

---

源文档：`zh_CN/module/comx_cat1.md`

源文档 SHA-256：`db09ed12b08708aecd7c24d77673079d25038bfb0bbc4863f5208ea030bb4f06`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
