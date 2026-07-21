# Unit LoRaWAN470 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaWAN470 |
| SKU | U116 |
| 产品 ID | `unit-lorawan470-9d0faaf6a4e5` |
| 源文档 | `zh_CN/unit/lorawan470.md` |

## 概述

Unit LoRaWAN470 的板级核心为 M1 Ra-07/Ra-07H 模组，UTX/URX 经 R5/R6 22Ω 连接 J1 Grove UART，SWCLK/SWDIO/RES 分别引至 SWC、SWD、RESET 测试点。+5V 经 VR1 AMS1117-3.3 生成 +3.3V 为模组供电，ANT 经 R4 0Ω 接 E1 ANT_IPEX。原理图还给出 470/868/915 的 R1/R2/R3 0Ω 变体表，但没有标明实际装配；ASR6501、470MHz、LoRaWAN/AT/UART 参数、射频功率/灵敏度和 SMA 外部结构需结合 BOM、模组资料或实测确认。

## 检索关键词

`Unit LoRaWAN470`、`U116`、`Ra-07`、`Ra-07H`、`ASR6501`、`LoRaWAN470`、`470MHz`、`868MHz`、`915MHz`、`AMS1117-3.3`、`+5V`、`+3.3V`、`UART`、`UTX`、`URX`、`UTXD`、`URXD`、`115200bps`、`AT command`、`J1 HY-2.0_UART`、`SWCLK`、`SWDIO`、`SWC`、`SWD`、`RESET`、`P00`、`ANT`、`ANT_IPEX`、`E1`、`R4 0Ω`、`R5 22Ω`、`R6 22Ω`、`SMA antenna`、`LoRaWAN v1.0.1`、`+21dBm`、`-137dBm`、`SF12`、`BW125KHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | Ra-07/Ra-07H | 提供 UART、SWD、复位和 ANT 射频端口的无线通信模组 | 图 900b529b827b / 第 1 页 / 第 1 页中央：M1 Ra-07/Ra-07H，pins1-18 与 GND/VCC/SWD/RESET/UART/ANT |
| VR1 | AMS1117-3.3 | 将 +5V 转换为模组使用的 +3.3V | 图 900b529b827b / 第 1 页 / 第 1 页左上：VR1 AMS1117-3.3，Vin=+5V、Vout=+3.3V、GND |
| J1 | HY-2.0_UART | 外部 UART 与 +5V/GND Grove 接口 | 图 900b529b827b / 第 1 页 / 第 1 页右中：J1 HY-2.0_UART pin1 RX、pin2 TX、pin3 VCC、pin4 GND |
| E1 | ANT_IPEX | 由 M1 ANT 经 R4 连接的 IPEX 射频天线接口 | 图 900b529b827b / 第 1 页 / 第 1 页中右：M1 ANT pin18-R4-E1 ANT_IPEX 与 GND |
| R4 | 0Ω | M1 ANT 与 E1 ANT_IPEX 之间的串联射频跳线 | 图 900b529b827b / 第 1 页 / 第 1 页中右：R4 0Ω 位于 ANT pin18 与 E1 之间 |
| R5,R6 | 22Ω / 22Ω | M1 UTX/URX 至外部 UTXD/URXD 的 UART 串联电阻 | 图 900b529b827b / 第 1 页 / 第 1 页中央：M1 UTX pin11-R5 22Ω-UTXD；URX pin10-R6 22Ω-URXD |
| JP1,JP2,JP3,JP4,JP5 | test pads/jumpers | 分别引出 +3.3V、GND、SWC、SWD、RESET 的测试与调试节点 | 图 900b529b827b / 第 1 页 / 第 1 页左中：JP1 +3.3V、JP2 GND、JP3 SWC、JP4 SWD、JP5 RESET |
| R1,R2,R3 | 0Ω / 0Ω / 0Ω | 图中独立 470/868/915 变体识别表的三颗 0Ω 配置电阻 | 图 900b529b827b / 第 1 页 / 第 1 页上中：R1 0Ω-470、R2 0Ω-868、R3 0Ω-915 表格 |
| C1,C2 | 22uF / 22uF | AMS1117 的 +5V 输入与 +3.3V 输出电容 | 图 900b529b827b / 第 1 页 / 第 1 页左上：C1 22uF 从 +5V 到 GND，C2 22uF 从 +3.3V 到 GND |
| C3,C4,C5,C6 | 100nF / 100nF / 10uF / 33pF | +5V 接口去耦及 M1 +3.3V 电源去耦/滤波 | 图 900b529b827b / 第 1 页 / 第 1 页：J1 附近 C3 100nF；M1 VCC 附近 C4 100nF/C5 10uF/C6 33pF |

## 系统结构

### Unit LoRaWAN470 系统结构

J1 提供 +5V 和交叉映射 UART，VR1 生成 +3.3V 供 M1 Ra-07/Ra-07H；M1 通过 SWD/RESET 测试点调试，并通过 ANT-R4-E1 连接外部天线。板上没有独立 MCU、外部存储器、电池或充电器。

- 参数与网络：`module=M1 Ra-07/Ra-07H`；`host_interface=J1 UART`；`power=+5V -> VR1 AMS1117-3.3 -> +3.3V`；`debug=JP3 SWC,JP4 SWD,JP5 RESET`；`rf=M1 ANT -> R4 -> E1 ANT_IPEX`；`external_mcu=null`；`external_storage=null`；`battery=null`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页完整原理图

## 电源

### +5V 至 +3.3V 稳压

+5V 连接 VR1 AMS1117-3.3 Vin，VR1 Vout 输出 +3.3V；C1 22uF 位于 +5V 输入，C2 22uF 位于 +3.3V 输出，VR1 GND 接地。

- 参数与网络：`input=+5V`；`regulator=VR1 AMS1117-3.3`；`output=+3.3V`；`input_cap=C1 22uF`；`output_cap=C2 22uF`；`ground=GND`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页左上 VR1/C1/C2 与 +5V/+3.3V

### M1 3.3V 供电

M1 VCC pin9 接 +3.3V，GND pin1 接 GND；C4 100nF、C5 10uF、C6 33pF 从 +3.3V 接 GND，位于模组电源附近。

- 参数与网络：`vcc=M1 pin9 +3.3V`；`ground=M1 pin1 GND`；`decoupling=C4 100nF,C5 10uF,C6 33pF`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页中央 M1 pin1/pin9 与 C4/C5/C6

## 接口

### J1 HY-2.0_UART

J1 pin1 标为 RX 并连接 UTXD，pin2 标为 TX 并连接 URXD，pin3=+5V，pin4=GND；C3 100nF 跨接 +5V 与 GND。

- 参数与网络：`pin1=RX <- UTXD`；`pin2=TX -> URXD`；`pin3=+5V`；`pin4=GND`；`connector=HY-2.0_UART`；`decoupling=C3 100nF`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页右中 J1 pin1-pin4、UTXD/URXD/+5V/GND 与 C3

## 总线

### M1 至 Grove UART

M1 UTX pin11 经 R5 22Ω 形成 UTXD 并连接 J1 RX pin1；M1 URX pin10 经 R6 22Ω 形成 URXD 并连接 J1 TX pin2。页面未显示 UART 电平转换器、握手线或反相器。

- 参数与网络：`module_tx=M1 UTX pin11 -> R5 22Ω -> UTXD -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> URXD -> R6 22Ω -> M1 URX pin10`；`level_shifter=null`；`flow_control=null`；`inverter=null`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页中央至右侧 M1 UTX/URX、R5/R6 与 J1

## GPIO 与控制信号

### M1 配置与未用引脚

M1 P00 pin12 接 GND；ADC pin2、AUX pin3、SETA pin4、DIO3 pin5、SETB pin6 标为未连接，P01 pin13、P06 pin14、P07 pin15 也未接外部网络。

- 参数与网络：`p00=pin12 GND`；`left_unconnected=ADC pin2,AUX pin3,SETA pin4,DIO3 pin5,SETB pin6`；`right_unconnected=P01 pin13,P06 pin14,P07 pin15`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 pins2-6 与 pins12-15 的连线/未连接标记

## 复位

### M1 RESET

M1 RES pin16 连接 RESET 网络并引至 JP5；本页未显示 RESET 的外部上拉、下拉、电容或按键。

- 参数与网络：`module_pin=M1 RES pin16`；`net=RESET`；`testpoint=JP5`；`external_pullup_shown=false`；`external_pulldown_shown=false`；`reset_cap_shown=false`；`reset_button_shown=false`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 RES pin16、RESET 同名网络与 JP5

## 保护电路

### 电源、UART 与射频保护拓扑

+5V 直接进入 AMS1117，UART 仅有 R5/R6 22Ω 串联，ANT 仅有 R4 0Ω；完整单页未显示保险丝、反接保护、TVS/ESD 二极管、UART 电平转换或射频浪涌保护器件。

- 参数与网络：`power_series_protection=null`；`uart_series=R5/R6 22Ω`；`rf_series=R4 0Ω`；`fuse_shown=false`；`reverse_protection_shown=false`；`tvs_esd_shown=false`；`uart_level_shifter_shown=false`；`rf_surge_protection_shown=false`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页完整 +5V/UART/ANT 路径

## 内存与 Flash

### 模组内部时钟与存储

本页只显示 M1 Ra-07/Ra-07H 外部引脚，没有展开模组内部 MCU、Flash/RAM、射频芯片、晶振或时钟网络，因此无法从本页确认存储容量与时钟频率。

- 参数与网络：`module=M1 Ra-07/Ra-07H`；`internal_mcu_schematic=null`；`flash_capacity=null`；`ram_capacity=null`；`external_crystal_on_page=null`；`clock_frequency=null`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 仅为模块级符号，无内部框图

## 射频

### M1 至 IPEX 天线路径

M1 ANT pin18 通过 R4 0Ω 串联连接 E1 ANT_IPEX 中心端，E1 地端接 GND；页面未显示额外 LC 匹配、射频开关、功放或低噪声放大器。

- 参数与网络：`source=M1 ANT pin18`；`series=R4 0Ω`；`connector=E1 ANT_IPEX`；`ground=E1 GND`；`matching_network_shown=false`；`rf_switch_shown=false`；`external_pa_shown=false`；`external_lna_shown=false`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页中右 M1 ANT-R4-E1 ANT_IPEX-GND

## 调试与烧录

### SWD 调试连接

M1 SWCLK pin7 连接 SWC 并引至 JP3，M1 SWDIO pin8 连接 SWD 并引至 JP4；JP1 提供 +3.3V、JP2 提供 GND。

- 参数与网络：`clock=M1 SWCLK pin7 -> SWC -> JP3`；`data=M1 SWDIO pin8 -> SWD -> JP4`；`reference_power=JP1 +3.3V`；`reference_ground=JP2 GND`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页左中 JP1-JP4 与 M1 SWCLK/SWDIO

## 其他事实

### 其他功能分区

完整单页没有显示 LED、按键、传感器、音频、显示、USB、I2C、SPI、CAN、RS-485、电池或充电路径；外部可见功能集中于 UART、SWD/RESET、供电和天线。

- 参数与网络：`led=null`；`button=null`；`sensor=null`；`audio=null`；`display=null`；`usb=null`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`battery=null`
- 证据：图 900b529b827b / 第 1 页 / 第 1 页完整原理图

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit LoRaWAN470 系统结构 | `module=M1 Ra-07/Ra-07H`；`host_interface=J1 UART`；`power=+5V -> VR1 AMS1117-3.3 -> +3.3V`；`debug=JP3 SWC,JP4 SWD,JP5 RESET`；`rf=M1 ANT -> R4 -> E1 ANT_IPEX`；`external_mcu=null`；`external_storage=null`；`battery=null` |
| 电源 | +5V 至 +3.3V 稳压 | `input=+5V`；`regulator=VR1 AMS1117-3.3`；`output=+3.3V`；`input_cap=C1 22uF`；`output_cap=C2 22uF`；`ground=GND` |
| 电源 | M1 3.3V 供电 | `vcc=M1 pin9 +3.3V`；`ground=M1 pin1 GND`；`decoupling=C4 100nF,C5 10uF,C6 33pF` |
| 接口 | J1 HY-2.0_UART | `pin1=RX <- UTXD`；`pin2=TX -> URXD`；`pin3=+5V`；`pin4=GND`；`connector=HY-2.0_UART`；`decoupling=C3 100nF` |
| 总线 | M1 至 Grove UART | `module_tx=M1 UTX pin11 -> R5 22Ω -> UTXD -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> URXD -> R6 22Ω -> M1 URX pin10`；`level_shifter=null`；`flow_control=null`；`inverter=null` |
| 调试与烧录 | SWD 调试连接 | `clock=M1 SWCLK pin7 -> SWC -> JP3`；`data=M1 SWDIO pin8 -> SWD -> JP4`；`reference_power=JP1 +3.3V`；`reference_ground=JP2 GND` |
| 复位 | M1 RESET | `module_pin=M1 RES pin16`；`net=RESET`；`testpoint=JP5`；`external_pullup_shown=false`；`external_pulldown_shown=false`；`reset_cap_shown=false`；`reset_button_shown=false` |
| GPIO 与控制信号 | M1 配置与未用引脚 | `p00=pin12 GND`；`left_unconnected=ADC pin2,AUX pin3,SETA pin4,DIO3 pin5,SETB pin6`；`right_unconnected=P01 pin13,P06 pin14,P07 pin15` |
| 射频 | M1 至 IPEX 天线路径 | `source=M1 ANT pin18`；`series=R4 0Ω`；`connector=E1 ANT_IPEX`；`ground=E1 GND`；`matching_network_shown=false`；`rf_switch_shown=false`；`external_pa_shown=false`；`external_lna_shown=false` |
| 射频 | 470/868/915 变体电阻表 | `r1=0Ω, label 470`；`r2=0Ω, label 868`；`r3=0Ω, label 915`；`electrical_nets=null`；`assembled_option=null` |
| 保护电路 | 电源、UART 与射频保护拓扑 | `power_series_protection=null`；`uart_series=R5/R6 22Ω`；`rf_series=R4 0Ω`；`fuse_shown=false`；`reverse_protection_shown=false`；`tvs_esd_shown=false`；`uart_level_shifter_shown=false`；`rf_surge_protection_shown=false` |
| 内存与 Flash | 模组内部时钟与存储 | `module=M1 Ra-07/Ra-07H`；`internal_mcu_schematic=null`；`flash_capacity=null`；`ram_capacity=null`；`external_crystal_on_page=null`；`clock_frequency=null` |
| 核心器件 | 正文 ASR6501 方案 | `documented_chip=ASR6501`；`schematic_module=M1 Ra-07/Ra-07H`；`internal_chip_label=null` |
| 总线 | 正文 UART 与 AT 协议 | `documented_baud=115200bps`；`documented_control=AT commands`；`documented_lorawan=v1.0.1`；`data_bits=null`；`parity=null`；`stop_bits=null`；`firmware_version=null` |
| 射频 | 正文 470MHz 射频性能 | `documented_frequency=470MHz`；`documented_sensitivity=-137dBm`；`documented_sensitivity_condition=SF12/BW125kHz`；`documented_tx_power=+21dBm`；`schematic_frequency=null`；`impedance=null`；`certification=null`；`antenna_gain=null` |
| 接口 | 正文 SMA 天线结构 | `documented_antenna=SMA antenna`；`schematic_connector=E1 ANT_IPEX`；`sma_connector_on_page=null`；`pigtail=null`；`antenna_part_number=null` |
| 其他事实 | 其他功能分区 | `led=null`；`button=null`；`sensor=null`；`audio=null`；`display=null`；`usb=null`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`battery=null` |

## 待确认事项

- `rf.variant-table`：原理图上方独立表格将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915；这些符号没有在本页连接到任何网络，图中也没有装配标记，无法仅凭本页确认 U116 实际装配哪一颗。（证据：图 900b529b827b / 第 1 页 / 第 1 页上中 R1/R2/R3 与 470/868/915 独立表格）
- `component.documented-asr6501`：正文称产品采用 ASR6501；板级原理图只将 M1 标为 Ra-07/Ra-07H，没有在模组符号中打印 ASR6501 型号或内部连接。（证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 标注 Ra-07/Ra-07H，无 ASR6501 文字）
- `bus.documented-at-uart`：正文称通过 UART 115200bps 使用 AT 指令，并集成 LoRaWAN v1.0.1 协议栈；原理图只确认 UTX/URX 两线，没有波特率、数据位、校验、停止位、AT 固件版本或 LoRaWAN 协议版本。（证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 UTX/URX 至 J1，整页无协议或速率文字）
- `rf.documented-470-performance`：正文列出 470MHz、最小接收灵敏度 -137dBm（SF12/BW125kHz）和最大发射功率 +21dBm；原理图只确认 ANT 到 IPEX 的路径，没有频段、匹配阻抗、功率、灵敏度、带宽、扩频因子、认证或天线性能参数。（证据：图 900b529b827b / 第 1 页 / 第 1 页 M1 ANT-R4-E1；无射频性能表）
- `interface.documented-sma`：正文称产品配有 SMA 天线；板级原理图只显示 E1 ANT_IPEX，没有 SMA 连接器、IPEX-to-SMA 馈线、天线型号或机械接口细节。（证据：图 900b529b827b / 第 1 页 / 第 1 页唯一射频接口为 E1 ANT_IPEX）
- `review.frequency-option`：请用 U116 当前 BOM/装配图确认 R1/R2/R3 的实际贴装状态，以及 470/868/915 标记如何决定模组频段。；原因：原理图只给出孤立变体表，没有网络或装配状态。
- `review.module-internals`：请用当前 Ra-07/Ra-07H 模组 BOM 或模组原理图确认内部主芯片是否为 ASR6501，以及内部存储、时钟与射频实现。；原因：板级原理图没有展开模组内部，也没有 ASR6501 文字。
- `review.uart-lorawan-protocol`：请以当前模组固件确认 UART 115200bps 的完整帧格式、AT 指令版本和 LoRaWAN v1.0.1 协议栈版本。；原因：硬件图只显示 UTX/URX 两线。
- `review.rf-performance`：请用模组 datasheet、射频测试报告和区域认证确认 470MHz、+21dBm、-137dBm（SF12/BW125kHz）、匹配阻抗与适用地区。；原因：板级原理图只有 ANT/IPEX 连接，不能证明射频性能或法规边界。
- `review.sma-assembly`：请确认量产板 E1 IPEX 到外部 SMA 的馈线/转接结构、SMA 极性、天线型号和增益。；原因：原理图没有 SMA 或外部馈线结构。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `900b529b827b45c2a11b2863953929fb1378fe8c54f9c34000712ddf9bc5e9d7` | `https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan470/lorawan470_sch_01.webp` |

---

源文档：`zh_CN/unit/lorawan470.md`

源文档 SHA-256：`86b0f14220a4ad1d1282c3b037336bc5d1ddacccc488fb6799524b4b12590b3f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
