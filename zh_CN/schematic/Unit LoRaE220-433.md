# Unit LoRaE220-433 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaE220-433 |
| SKU | U170-433 |
| 产品 ID | `unit-lorae220-433-fd8862b01edf` |
| 源文档 | `zh_CN/unit/Unit LoRaE220-433.md` |

## 概述

Unit LoRaE220-433 以 M1 E220-400T22S Module 为无线通信模组，J1 Grove 的 IO2、IO1 分别连接模组 TXD、RXD。M1 VCC 直接使用 5V，J1 电源入口与模组供电端各有一颗 10uF 电容。S1 两位拨码分别控制 M0、M1，开关闭合时将对应模式脚接地；M1 ANT pin 21 在本页未画出外部天线连接器或匹配网络。

## 检索关键词

`Unit LoRaE220-433`、`U170-433`、`E220-400T22S`、`E220-400T22S Module`、`LLCC68`、`LoRa`、`433MHz`、`410.125-493.125MHz`、`UART`、`115200`、`TXD`、`RXD`、`AUX`、`M0`、`M1`、`SW DIP-2`、`GROVE 4P`、`IO2`、`IO1`、`5V`、`ANT pin 21`、`22dBm`、`-129dBm`、`Wake on Radio`、`WOR`、`configuration mode`、`point-to-point`、`broadcast`、`SMA antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | E220-400T22S Module | UART 接口的 LoRa 无线通信模组，提供 M0/M1 模式控制、AUX 状态和 ANT 射频引脚 | 图 830596faf5c4 / 第 1 页 / 页 1 网格 B2-C3，M1 器件框下方标注 E220-400T22S Module |
| J1 | GROVE 4P | UART、5V 和 GND 主机接口 | 图 830596faf5c4 / 第 1 页 / 页 1 网格 B2，J1 GROVE 4P，触点标注 IO2、IO1、5V、GND |
| S1 | SW DIP-2 | M0/M1 双位工作模式选择开关 | 图 830596faf5c4 / 第 1 页 / 页 1 网格 C2，S1 标注 SW DIP-2，两位分别连接 M0、M1 与 GND |
| C1,C2 | 10uF | J1 供电入口和 M1 VCC 的 5V 对地储能/去耦电容 | 图 830596faf5c4 / 第 1 页 / 页 1 网格 B2 的 C1 10uF 与网格 C2-C3 的 C2 10uF |

## 系统结构

### M1 LoRa 模组

M1 的器件值为 E220-400T22S Module，通过 TXD/RXD 与 J1 通信，通过 M0/M1 选择工作状态，并具有 AUX 与 ANT 引脚。

- 参数与网络：`reference=M1`；`part_number=E220-400T22S Module`；`host_bus=UART`；`mode_pins=M0,M1`；`status_pin=AUX`；`rf_pin=ANT`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 型号及左侧 M0/M1/RXD/TXD/AUX、右侧 ANT 引脚

### 其他功能分区

本页未绘制独立主控或协处理器、外部存储器、充电器、电池、音频器件、传感器、晶振、复位或调试接口；无线协议处理位于未展开内部电路的 M1 模组中。

- 参数与网络：`separate_controller=false`；`coprocessor=false`；`external_memory=false`；`battery=false`；`charger=false`；`audio=false`；`sensor=false`；`external_clock=false`；`reset_interface=false`；`debug_interface=false`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 网格 B2-C3 的全部器件与连接

## 核心器件

### M1 未使用引脚

M1 pin 12、14、15、16、17、18 标注 NC，未连接外部网络。

- 参数与网络：`nc_pins=12,14,15,16,17,18`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 右侧 NC 引脚 12、14-18

## 电源

### M1 供电

M1 VCC pin 10 直接连接 5V，GND pin 1、2、3、4、11、13、19、20、22 连接 GND。

- 参数与网络：`supply=VCC/pin 10/5V`；`ground_pins=1,2,3,4,11,13,19,20,22`；`rail=5V`；`regulator_visible=false`；`load_switch_visible=false`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 VCC pin 10、所有 GND 引脚与 5V/GND 总线

### 5V 去耦

C1、C2 均为 10uF，分别位于 J1 供电入口和 M1 VCC 附近，跨接 5V 与 GND。

- 参数与网络：`connector_capacitor=C1 10uF`；`module_capacitor=C2 10uF`；`rail=5V`；`return=GND`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 J1 下方 C1 10uF 与 M1 VCC 下方 C2 10uF

## 接口

### J1 Grove UART 接口

J1 的 IO2、IO1、5V、GND 四个触点分别连接 TXD、RXD、5V、GND。

- 参数与网络：`reference=J1`；`pinout=IO2:TXD,IO1:RXD,5V:5V,GND:GND`；`txd_module_direction=output from M1`；`rxd_module_direction=input to M1`；`interface_supply=5V`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 网格 B2，J1 四个触点与右侧 TXD/RXD/5V/GND 网络

## 总线

### J1 与 M1 UART

J1 IO2 的 TXD 网络连接 M1 TXD pin 8，J1 IO1 的 RXD 网络连接 M1 RXD pin 7；两条信号均为直接连接。

- 参数与网络：`controller_device=external host via J1`；`device=M1`；`tx_path=M1 TXD/pin 8 -> J1 IO2`；`rx_path=J1 IO1 -> M1 RXD/pin 7`；`level_shifter=null`；`series_resistor=null`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 J1 TXD/RXD 网络与 M1 左侧 RXD pin 7、TXD pin 8

## GPIO 与控制信号

### S1 与 M0/M1

S1 pin 1 连接 M0、pin 2 连接 M1，pin 4 与 pin 3 均连接 GND；对应开关闭合时将 M0 或 M1 接地。

- 参数与网络：`switch_m0=S1 pin 1 M0 to pin 4 GND`；`switch_m1=S1 pin 2 M1 to pin 3 GND`；`closed_level=GND/logic low`；`external_pullups=null`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 网格 C2，S1 四个脚号、M0/M1 与 GND 连线

### M1 模式与状态引脚

M1 的 M0、M1、AUX 分别为 pin 5、pin 6、pin 9；M0/M1 连接 S1，AUX 在本页未连接其他器件或接口。

- 参数与网络：`m0=pin 5 -> S1`；`m1=pin 6 -> S1`；`aux=pin 9 unconnected`；`aux_external_direction=null`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 左侧 M0 pin 5、M1 pin 6、AUX pin 9 及其外部线段

## 保护电路

### 接口与电源保护

本页未显示 TVS/ESD、保险丝、反接保护、负载开关、电平转换器或 UART 串联保护器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`level_shifter_visible=false`；`uart_protection_visible=false`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 全图仅含 J1、C1、S1、M1、C2 与直接连线

## 射频

### M1 ANT

M1 ANT pin 21 在器件符号中标出，但本页没有画出 ANT 到 SMA、天线座或匹配网络的外部连接。

- 参数与网络：`rf_pin=M1 ANT/pin 21`；`external_connector=null`；`matching_network=null`
- 证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 右侧 ANT pin 21 的短线未连接外部器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M1 LoRa 模组 | `reference=M1`；`part_number=E220-400T22S Module`；`host_bus=UART`；`mode_pins=M0,M1`；`status_pin=AUX`；`rf_pin=ANT` |
| 接口 | J1 Grove UART 接口 | `reference=J1`；`pinout=IO2:TXD,IO1:RXD,5V:5V,GND:GND`；`txd_module_direction=output from M1`；`rxd_module_direction=input to M1`；`interface_supply=5V` |
| 总线 | J1 与 M1 UART | `controller_device=external host via J1`；`device=M1`；`tx_path=M1 TXD/pin 8 -> J1 IO2`；`rx_path=J1 IO1 -> M1 RXD/pin 7`；`level_shifter=null`；`series_resistor=null` |
| GPIO 与控制信号 | S1 与 M0/M1 | `switch_m0=S1 pin 1 M0 to pin 4 GND`；`switch_m1=S1 pin 2 M1 to pin 3 GND`；`closed_level=GND/logic low`；`external_pullups=null` |
| GPIO 与控制信号 | M1 模式与状态引脚 | `m0=pin 5 -> S1`；`m1=pin 6 -> S1`；`aux=pin 9 unconnected`；`aux_external_direction=null` |
| 电源 | M1 供电 | `supply=VCC/pin 10/5V`；`ground_pins=1,2,3,4,11,13,19,20,22`；`rail=5V`；`regulator_visible=false`；`load_switch_visible=false` |
| 电源 | 5V 去耦 | `connector_capacitor=C1 10uF`；`module_capacitor=C2 10uF`；`rail=5V`；`return=GND` |
| 射频 | M1 ANT | `rf_pin=M1 ANT/pin 21`；`external_connector=null`；`matching_network=null` |
| 核心器件 | M1 未使用引脚 | `nc_pins=12,14,15,16,17,18` |
| 保护电路 | 接口与电源保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`level_shifter_visible=false`；`uart_protection_visible=false` |
| 系统结构 | 其他功能分区 | `separate_controller=false`；`coprocessor=false`；`external_memory=false`；`battery=false`；`charger=false`；`audio=false`；`sensor=false`；`external_clock=false`；`reset_interface=false`；`debug_interface=false` |
| 射频 | LoRa 芯片与频段 | `documented_chip=LLCC68`；`documented_default_frequency_mhz=433`；`documented_band_mhz=410.125-493.125`；`schematic_internal_chip=null`；`schematic_frequency=null` |
| 射频 | 发射功率、接收灵敏度与通信距离 | `documented_max_tx_dbm=22`；`documented_rx_sensitivity_dbm=-129`；`documented_distance_km=5`；`schematic_tx_power=null`；`schematic_rx_sensitivity=null`；`schematic_distance=null` |
| 总线 | UART 波特率 | `documented_baud=115200`；`schematic_baud=null`；`frame_format=null` |
| 其他事实 | M0/M1 工作模式 | `documented_modes=0 normal TX/RX,1 WOR TX,2 WOR RX,3 configuration`；`documented_on_level=0`；`documented_off_level=1`；`schematic_mode_table=null` |
| 射频 | 外接天线规格 | `documented_antenna=rubber rod antenna`；`documented_gain_dbi=2.5`；`documented_length_mm=110`；`documented_connector=SMA male pin`；`schematic_connector=null` |
| 电源 | 最大供电电压 | `schematic_nominal_voltage_v=5`；`documented_max_voltage_v=5.5`；`overvoltage_protection_visible=false` |

## 待确认事项

- `rf.module_chip_band`：产品正文标注模组内部芯片为 LLCC68、默认频段为 433MHz 且支持 410.125 至 493.125MHz；本页原理图只显示 E220-400T22S 模组外部引脚，没有内部芯片或频率标注。（证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 仅标注 E220-400T22S Module，未出现 LLCC68 或频率数值）
- `rf.performance`：产品正文描述最大发射功率 22dBm、接收灵敏度 -129dBm，并在产品比较表列出理论通信距离 5km；本页原理图未标注射频性能或测试条件。（证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 与 ANT pin 21 区域未打印功率、灵敏度、增益或距离参数）
- `bus.documented_uart_baud`：产品正文列出串口通信速率 115200，但本页原理图仅标注 TXD/RXD 物理网络，没有波特率或帧格式。（证据：图 830596faf5c4 / 第 1 页 / 页 1 J1 TXD/RXD 与 M1 pin 7/8 路径，无速率或串口格式注释）
- `other.mode_semantics`：产品正文定义正常收发、WOR 发送、WOR 接收和参数配置四种 M0/M1 模式，并说明开关 ON 对应逻辑 0；原理图只确认两位开关闭合接地，没有模式编号或行为说明。（证据：图 830596faf5c4 / 第 1 页 / 页 1 S1 与 M0/M1 连接区没有模式表、WOR 或 ON/OFF 逻辑文字）
- `rf.documented_antenna`：产品正文包装信息描述 2.5dBi、总长 110mm、SMA 内针胶棒天线，但本页未绘制天线连接器，无法从原理图确认接口形式、增益或长度。（证据：图 830596faf5c4 / 第 1 页 / 页 1 M1 ANT pin 21 未连接外部连接器或天线符号）
- `power.documented_max_input`：产品正文警告供电不要超过 5.5V，但本页原理图只标称 5V 电源轨，没有绝对最大额定值或过压保护。（证据：图 830596faf5c4 / 第 1 页 / 页 1 J1 5V、M1 VCC pin 10 与直接供电路径，无最大电压或过压保护标注）
- `review.module_chip_band`：当前 E220-400T22S 模组内部是否为 LLCC68，默认 433MHz 和 410.125-493.125MHz 范围是否适用于该硬件版本？；原因：原理图只提供模组外部型号和引脚，没有内部芯片、射频频段或认证版本。
- `review.rf_performance`：22dBm、-129dBm 和 5km 参数分别适用于哪些信道、速率、天线、环境与法规条件？；原因：原理图没有射频测试配置或性能额定值。
- `review.uart_baud`：当前出厂配置的 UART 波特率是否为 115200，帧格式是什么？；原因：原理图只能确认 TXD/RXD 连线，串口参数由模组配置决定。
- `review.mode_semantics`：S1 的 M0/M1 开关位置与四种工作模式的行为是否与正文模式表一致？；原因：原理图只确认开关闭合接地，没有模块内部上拉和模式语义。
- `review.antenna_spec`：量产板的 ANT 路径和随附天线是否确为 SMA 内针、2.5dBi、110mm？；原因：原理图没有绘制天线座、匹配网络或天线规格。
- `review.max_input_voltage`：5.5V 是否为 M1 或整板输入的绝对最大供电电压？；原因：原理图仅显示 5V 标称网络，没有额定值说明和过压保护。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `830596faf5c40741d4b4a2d87cd92e55bad2d96ae7e3fc238df176620c98e951` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/624/SCH_UNIT_LoraE220_433MHz_sch_01.png` |

---

源文档：`zh_CN/unit/Unit LoRaE220-433.md`

源文档 SHA-256：`32471bcd722d70de92fe99d89d72cb511f44eaf143f39aa1f286d913c87da340`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
