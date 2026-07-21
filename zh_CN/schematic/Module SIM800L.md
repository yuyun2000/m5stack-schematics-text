# Module SIM800L 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module SIM800L |
| SKU | M004 |
| 产品 ID | `module-sim800l-899e03111377` |
| 源文档 | `zh_CN/module/sim800.md` |

## 概述

Module SIM800L 原理图以 U1（图中标为 SIM800）为蜂窝通信核心，UART TX/RX、RESET 和 SPK+ 分别经 0Ω 电阻连接 M5Stack_BUS 的 GPIO16、GPIO17、GPIO5 和 GPIO25。J1 提供 +5V，电源经 D1 M7 串联后送入 U1 VCC，并由 C1（图示 477）对地储能/滤波。音频部分连接 MK1 麦克风、J2 3.5mm 插孔以及 U1 的 MIC+/MIC-/SPK+/SPK-，射频只显示 E1 ANT。产品正文中的 SIM800L 精确型号、microSIM/IPX/状态 LED、UART 2.8V 电平边界和麦克风使能电阻实际装配状态未由本页完整确认。

## 检索关键词

`Module SIM800L`、`M004`、`SIM800`、`SIM800L`、`GSM`、`GPRS`、`M5Stack_BUS`、`UART`、`GPIO16`、`GPIO17`、`GPIO5`、`GPIO25`、`TX`、`RX`、`RST`、`SPK+`、`SPK-`、`MIC+`、`MIC-`、`3.5mm_jack`、`MK1 Mic2`、`R1 0Ω`、`R2 0Ω`、`R3 0Ω`、`R4 0Ω`、`R5 0Ω`、`D1 M7`、`C1 477`、`+5V`、`E1 ANT`、`AGND`、`microSIM`、`IPX`、`2.8V UART`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SIM800 | 蜂窝通信模块，提供 UART、RESET、ANT、MIC、SPK、RING、DTR 和电源接口 | 图 a60e773da081 / 第 1 页 / 第 1 页左中 U1 SIM800 |
| J1 | M5Stack_BUS | 主机堆叠接口，连接 GND、+5V、UART、RESET 和 SPK+ | 图 a60e773da081 / 第 1 页 / 第 1 页右侧 J1 M5Stack_BUS |
| J2 | 3.5mm_jack | 连接 U1 MIC+/MIC- 和 SPK+/SPK- 的四针音频插孔 | 图 a60e773da081 / 第 1 页 / 第 1 页左侧 J2 3.5mm_jack |
| MK1 | Mic2 | 连接 U1 麦克风差分输入的板载麦克风 | 图 a60e773da081 / 第 1 页 / 第 1 页左上 MK1 Mic2 |
| E1 | ANT | 连接 U1 ANT 引脚的板载天线节点 | 图 a60e773da081 / 第 1 页 / 第 1 页上方 E1 ANT |
| D1 | M7 | +5V 到 U1 VCC 的串联二极管 | 图 a60e773da081 / 第 1 页 / 第 1 页 U1 右上 D1 M7 |
| R1/R2/R3/R4 | 0Ω | TX、SPK+、RX、RST 到 M5Stack_BUS GPIO 的串联配置电阻 | 图 a60e773da081 / 第 1 页 / 第 1 页中部 R1-R4 0Ω |
| R5 | 0Ω | MK1 麦克风支路中的使能/配置电阻 | 图 a60e773da081 / 第 1 页 / 第 1 页左上 MK1 与 R5 0Ω |
| C1 | 477 | D1 后 U1 VCC 电源网到 GND 的储能/滤波电容 | 图 a60e773da081 / 第 1 页 / 第 1 页 U1 右侧 C1 477 |

## 系统结构

### Module SIM800L

U1 集成蜂窝通信、UART、射频和模拟音频接口；J1 M5Stack_BUS 提供电源与主机信号，J2/MK1 提供音频连接，E1 为天线节点。

- 参数与网络：`cellular_module=U1 SIM800`；`host=J1 M5Stack_BUS`；`audio_jack=J2`；`microphone=MK1`；`antenna=E1`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页完整功能分区

## 核心器件

### U1 RING/DTR

U1.12 RING 和 U1.11 DTR 在当前页未连接外部网络。

- 参数与网络：`ring=U1.12 NC`；`dtr=U1.11 NC`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1 左上 RING/DTR 短线无网络

## 电源

### U1 VCC 电源

J1 的 +5V 网络经串联 D1 M7 后连接 U1.2 VCC，C1（图示值 477）从 D1 后电源节点接 GND；图中没有 DC/DC、LDO、充电器或负载开关。

- 参数与网络：`input=+5V`；`series_diode=D1 M7`；`module_pin=U1.2 VCC`；`capacitor=C1 477`；`converter_shown=false`；`ldo_shown=false`；`charger_shown=false`；`load_switch_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1.2、D1、C1 与 J1 +5V

## 接口

### J1 M5Stack_BUS

本板使用 J1.1/.3/.5=GND、J1.8=GPIO25/SPK+、J1.15=GPIO16/TX、J1.16=GPIO17/RX、J1.20=GPIO5/RST、J1.28=+5V；其余主机引脚未连接板上网络。

- 参数与网络：`ground=1,3,5`；`speaker=8 GPIO25`；`uart=15 GPIO16 TX,16 GPIO17 RX`；`reset=20 GPIO5`；`power=28 +5V`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页右侧 J1 外部网络

### J2 3.5mm_jack

J2 四个触点分别接入 U1 的麦克风差分对和扬声器差分对，图中未标 CTIA/OMTP 或具体插头触点标准。

- 参数与网络：`connector=J2 3.5mm_jack`；`signals=MIC+,MIC-,SPK+,SPK-`；`headset_standard_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页左侧 J2 四针音频连接

## 总线

### SIM800 UART

U1.5 TXD 的 TX 网络经 R1 0Ω 到 J1.15 GPIO16；J1.16 GPIO17 的 RX 网络经 R3 0Ω 到 U1.4 RXD。

- 参数与网络：`module_tx=U1.5 TXD -> TX -> R1 0Ω -> J1.15 GPIO16`；`module_rx=J1.16 GPIO17 -> R3 0Ω -> RX -> U1.4 RXD`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1 TX/RX、R1/R3 与 J1.15/.16

## 时钟

### 外部时钟

完整原理图页未显示晶振、振荡器或外部时钟网络。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页完整图无时钟器件

## 复位

### U1 RESET

U1.3 RESET 的 RST 网络经 R4 0Ω 直接连接 J1.20 GPIO5；本页未画复位上拉、下拉、RC 或缓冲。

- 参数与网络：`module_pin=U1.3 RESET`；`net=RST`；`series=R4 0Ω`；`host_pin=J1.20 GPIO5`；`conditioning_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1.3 RST、R4、J1 GPIO5

## 保护电路

### 电源与外部接口保护

图中只显示 +5V 串联 D1 M7；J1、J2、E1 及 UART/音频/射频网络未画 TVS、ESD 阵列、保险丝或过流保护。

- 参数与网络：`series_power_diode=D1 M7`；`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`overcurrent_protection_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页完整外部接口网络

## 内存与 Flash

### 外部存储器

完整原理图页未展示独立 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页完整图无存储器

## 音频

### SPK+/SPK-

U1.8 SPK+ 连接 J2 扬声器触点，并经 R2 0Ω 引到 J1.8 GPIO25；U1.7 SPK- 连接 J2 返回触点和 AGND 网络。

- 参数与网络：`positive=U1.8 SPK+ -> J2 -> R2 0Ω -> J1.8 GPIO25`；`negative=U1.7 SPK- -> J2 -> AGND`；`m5bus_gpio=GPIO25`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页左侧 U1.7/.8、J2 与 R2

### MIC+/MIC- 与 MK1

U1.9 MIC+ 和 U1.10 MIC- 连接 J2 麦克风触点与 MK1，MK1 其中一路串联 R5 0Ω。

- 参数与网络：`module_pins=U1.9 MIC+,U1.10 MIC-`；`microphone=MK1 Mic2`；`jack=J2`；`configuration_resistor=R5 0Ω`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页左侧 MK1/R5/J2 与 U1.9/.10

## 射频

### E1 ANT

U1.1 ANT 直接连接 E1 ANT，当前页没有射频匹配网络、天线选择开关或其他射频连接器位号。

- 参数与网络：`module_pin=U1.1 ANT`；`antenna=E1 ANT`；`matching_network_shown=false`；`selector_shown=false`；`second_connector_shown=false`
- 证据：图 a60e773da081 / 第 1 页 / 第 1 页上方 U1.1 与 E1 ANT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module SIM800L | `cellular_module=U1 SIM800`；`host=J1 M5Stack_BUS`；`audio_jack=J2`；`microphone=MK1`；`antenna=E1` |
| 核心器件 | U1 型号标注 | `schematic_marking=SIM800`；`product_name=SIM800L`；`confirmed_assembly_part=null` |
| 电源 | U1 VCC 电源 | `input=+5V`；`series_diode=D1 M7`；`module_pin=U1.2 VCC`；`capacitor=C1 477`；`converter_shown=false`；`ldo_shown=false`；`charger_shown=false`；`load_switch_shown=false` |
| 总线 | SIM800 UART | `module_tx=U1.5 TXD -> TX -> R1 0Ω -> J1.15 GPIO16`；`module_rx=J1.16 GPIO17 -> R3 0Ω -> RX -> U1.4 RXD`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16` |
| 复位 | U1 RESET | `module_pin=U1.3 RESET`；`net=RST`；`series=R4 0Ω`；`host_pin=J1.20 GPIO5`；`conditioning_shown=false` |
| 接口 | J1 M5Stack_BUS | `ground=1,3,5`；`speaker=8 GPIO25`；`uart=15 GPIO16 TX,16 GPIO17 RX`；`reset=20 GPIO5`；`power=28 +5V` |
| 音频 | SPK+/SPK- | `positive=U1.8 SPK+ -> J2 -> R2 0Ω -> J1.8 GPIO25`；`negative=U1.7 SPK- -> J2 -> AGND`；`m5bus_gpio=GPIO25` |
| 音频 | MIC+/MIC- 与 MK1 | `module_pins=U1.9 MIC+,U1.10 MIC-`；`microphone=MK1 Mic2`；`jack=J2`；`configuration_resistor=R5 0Ω` |
| 音频 | R5 麦克风使能 | `reference=R5`；`schematic_value=0Ω`；`dnp_marking_shown=false`；`documented_default=not populated / microphone disabled`；`assembly_state=null` |
| 接口 | J2 3.5mm_jack | `connector=J2 3.5mm_jack`；`signals=MIC+,MIC-,SPK+,SPK-`；`headset_standard_shown=false` |
| 射频 | E1 ANT | `module_pin=U1.1 ANT`；`antenna=E1 ANT`；`matching_network_shown=false`；`selector_shown=false`；`second_connector_shown=false` |
| 射频 | 正文中的 IPX 天线连接器 | `documented_connectors=IPX and onboard spring antenna`；`schematic_visible=E1 ANT only`；`ipx_reference=null`；`selection_network=null` |
| 接口 | UART 逻辑电平 | `documented_uart_max=2.8V`；`level_shifter_shown=false`；`series=R1/R3 0Ω`；`host_gpio=GPIO16/GPIO17`；`confirmed_compatible_level=null` |
| 接口 | microSIM 与状态 LED | `documented_sim=microSIM`；`documented_indicator=status LED`；`sim_connector_shown=false`；`sim_nets_shown=false`；`led_reference=null` |
| 核心器件 | U1 RING/DTR | `ring=U1.12 NC`；`dtr=U1.11 NC` |
| 保护电路 | 电源与外部接口保护 | `series_power_diode=D1 M7`；`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`overcurrent_protection_shown=false` |
| 其他事实 | 正文无线与功耗参数 | `documented_network=2G GSM/GPRS`；`documented_bands=850/950/1800/1900MHz`；`documented_supply=3.8-4.2V, recommended 4V`；`documented_peak_current=2000mA`；`ratings_on_schematic=null` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `component.module-marking`：当前原理图 U1 器件值明确写为 SIM800，而产品名称和正文写为 SIM800L；仅凭本页无法确认量产器件的精确后缀型号。（证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1 标注 SIM800）
- `audio.mic-enable-population`：R5 在原理图中标为 0Ω，但没有 DNP/NC 装配标记；正文说明麦克风默认停用并需焊接 0Ω 电阻，实际出厂 R5 状态需由 BOM 或实板确认。（证据：图 a60e773da081 / 第 1 页 / 第 1 页 MK1 支路 R5 0Ω 无 DNP 标记）
- `rf.documented-ipx`：正文列出 IPX 天线连接器和板载弹簧天线，但当前页只显示 E1 ANT，未显示 IPX/IPEX 连接器位号或选择网络。（证据：图 a60e773da081 / 第 1 页 / 第 1 页 RF 区仅 E1 ANT）
- `interface.uart-level`：TX/RX 通过 0Ω 电阻直接连接 M5Stack_BUS，图中没有电平转换；正文写 UART 最大 2.8V，但本页没有标出 GPIO16/GPIO17 与 U1 RXD/TXD 的允许电平范围。（证据：图 a60e773da081 / 第 1 页 / 第 1 页 TX/RX 0Ω 直连且无电压标注）
- `interface.documented-sim-led`：正文列出底部 microSIM 卡座和状态 LED，但当前原理图页没有 SIM 卡座、SIM_VCC/SIM_DATA/SIM_CLK/SIM_RST 网络或 LED 位号，无法从本页确认其具体连接。（证据：图 a60e773da081 / 第 1 页 / 第 1 页完整图无 SIM 卡座或 LED）
- `other.documented-radio-ratings`：正文列出 2G GSM/GPRS、850/950/1800/1900MHz、3.8-4.2V 建议 4V 以及峰值 2000mA 等参数；当前页只显示模块符号和供电连接，未标这些额定条件。（证据：图 a60e773da081 / 第 1 页 / 第 1 页 U1/D1/C1 无频段或额定参数标注）
- `review.module-marking`：请依据 M004 BOM 或实物模组丝印确认量产器件是 SIM800、SIM800L 或其他具体变体。；原因：原理图 U1 标 SIM800，产品名称与正文标 SIM800L。
- `review.mic-enable`：请依据 BOM 或实板确认 R5 默认是否未装，以及焊接后对应的麦克风使能行为。；原因：原理图标 0Ω 但无 DNP，正文说明默认停用。
- `review.ipx-antenna`：请依据 PCB/BOM 确认 IPX/IPEX 连接器位号、板载天线形式及天线选择方式。；原因：当前页只显示 E1 ANT。
- `review.uart-level`：请依据实际 U1 变体 datasheet 和主机 GPIO 规格确认 TX/RX 直连的安全逻辑电平。；原因：正文写 UART 最大 2.8V，原理图却通过 0Ω 直接连接 M5-Bus。
- `review.sim-led`：请依据完整原理图、PCB 或 BOM 确认 microSIM 卡座与状态 LED 的位号和连接。；原因：正文列出这些器件，但当前唯一页面未画出。
- `review.radio-ratings`：请依据确认后的蜂窝模组 datasheet 验证频段、供电和峰值电流参数。；原因：这些额定值未在当前原理图页标注，且 U1 型号后缀存在差异。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a60e773da081fbfaef684b077cc7bb4078439bf2034b564e87ef6000523c0e6a` | `https://static-cdn.m5stack.com/resource/docs/products/module/sim800/sim800_sch_01.webp` |

---

源文档：`zh_CN/module/sim800.md`

源文档 SHA-256：`9119f535ab167da37b1fdc509d6dc6fd9bc030eb858b2e93716e11467087d653`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
