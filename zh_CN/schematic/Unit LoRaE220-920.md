# Unit LoRaE220-920 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaE220-920 |
| SKU | U170 |
| 产品 ID | `unit-lorae220-920-da0bbe16dcc2` |
| 源文档 | `zh_CN/unit/LoRaE220-JP Unit.md` |

## 概述

Unit LoRaE220-920 以 M1 E220-900T22S Module 为 LoRa/UART 模组，J1 Grove 的 IO2、IO1 分别连接 TXD、RXD。M1 VCC 直接连接 5V，J1 与模组附近各有一只 10 uF 电容。S1 两位拨码分别连接 M0、M1，开关闭合时将对应模式脚接地；M1 ANT 引脚 21 在本页没有画出外部天线连接器。

## 检索关键词

`Unit LoRaE220-920`、`U170`、`E220-900T22S`、`E220-900T22S JP`、`LLCC68`、`LoRa`、`920MHz`、`920.6-928.0MHz`、`UART`、`TXD`、`RXD`、`AUX`、`M0`、`M1`、`SW DIP-2`、`GROVE 4P`、`IO2`、`IO1`、`5V`、`ANT pin 21`、`13dBm`、`5km`、`Wake on Radio`、`WOR`、`carrier sense`、`configuration mode`、`point-to-point`、`broadcast`、`SMA antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | E220-900T22S Module | UART 接口 LoRa 无线通信模组 | 图 cdd9716ab202 / 第 1 页 / 页 1 网格 B2-C3，M1 器件框下方标注 E220-900T22S Module |
| J1 | GROVE 4P | UART 与 5V 主机接口 | 图 cdd9716ab202 / 第 1 页 / 页 1 网格 B2，J1 GROVE 4P，端子标注 IO2、IO1、5V、GND |
| S1 | SW DIP-2 | M0/M1 双位工作模式选择开关 | 图 cdd9716ab202 / 第 1 页 / 页 1 网格 C2，S1 标注 SW DIP-2，两位分别连接 M0、M1 与 GND |

## 系统结构

### M1 LoRa 模组

M1 的器件值为 E220-900T22S Module，通过 TXD/RXD 与 J1 通信，通过 M0/M1 选择工作状态，并具有 AUX 与 ANT 引脚。

- 参数与网络：`reference=M1`；`part_number=E220-900T22S Module`；`host_bus=UART`；`mode_pins=M0,M1`；`status_pin=AUX`；`rf_pin=ANT`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 型号及左侧 M0/M1/RXD/TXD/AUX、右侧 ANT 引脚

## 核心器件

### M1 未使用引脚

M1 引脚 12、14、15、16、17、18 标注 NC，未连接外部网络。

- 参数与网络：`nc_pins=12,14,15,16,17,18`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 右侧 NC 引脚 12、14-18

## 电源

### M1 供电

M1 VCC 引脚 10 连接 5V，GND 引脚 1、2、3、4、11、13、19、20、22 连接 GND。

- 参数与网络：`supply=VCC/pin 10/5V`；`ground_pins=1,2,3,4,11,13,19,20,22`；`rail=5V`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 VCC pin 10、所有 GND 引脚与 5V/GND 总线

### 5V 去耦

C1、C2 均为 10 uF，分别位于 J1 供电入口和 M1 VCC 附近，跨接 5V 与 GND。

- 参数与网络：`connector_capacitor=C1 10uF`；`module_capacitor=C2 10uF`；`rail=5V`；`return=GND`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 J1 下方 C1 10uF 与 M1 VCC 下方 C2 10uF

## 接口

### J1 Grove UART 接口

J1 的 IO2、IO1、5V、GND 四端分别连接 TXD、RXD、5V、GND。

- 参数与网络：`reference=J1`；`pinout=IO2:TXD,IO1:RXD,5V:5V,GND:GND`；`TXD_module_direction=output from M1`；`RXD_module_direction=input to M1`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 网格 B2 J1 四个端子与右侧 TXD/RXD/5V/GND 网络

## 总线

### J1 与 M1 UART

J1 IO2 的 TXD 网络连接 M1 TXD 引脚 8，J1 IO1 的 RXD 网络连接 M1 RXD 引脚 7。

- 参数与网络：`tx_path=M1 TXD/pin 8 -> J1 IO2`；`rx_path=J1 IO1 -> M1 RXD/pin 7`；`level_shifter=null`；`series_resistor=null`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 J1 TXD/RXD 网络与 M1 左侧 RXD pin 7、TXD pin 8

## GPIO 与控制信号

### S1 与 M0/M1

S1 的 pin 1 连接 M0、pin 2 连接 M1，pin 4 与 pin 3 均连接 GND；对应开关闭合时将 M0 或 M1 接地。

- 参数与网络：`switch_m0=S1 pin 1 M0 to pin 4 GND`；`switch_m1=S1 pin 2 M1 to pin 3 GND`；`closed_level=GND/logic low`；`external_pullups=null`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 网格 C2 S1 四个脚号、M0/M1 与 GND 连线

### M1 模式与状态引脚

M1 的 M0、M1、AUX 分别为引脚 5、6、9；M0/M1 连接 S1，AUX 在本页未连接其他器件或接口。

- 参数与网络：`M0=pin 5 -> S1`；`M1=pin 6 -> S1`；`AUX=pin 9 unconnected`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 左侧 M0 pin 5、M1 pin 6、AUX pin 9 及其外部线段

## 保护电路

### 接口与电源保护

本页未显示 TVS/ESD、保险丝、反接保护、负载开关或 UART 串联保护器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`uart_protection_visible=false`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 全图仅含 J1、C1、S1、M1、C2 与直接连线

## 射频

### M1 ANT

M1 ANT 引脚 21 在器件符号中标出，但本页没有画出 ANT 到 SMA、天线座或匹配网络的外部连接。

- 参数与网络：`rf_pin=M1 ANT/pin 21`；`external_connector=null`；`matching_network=null`
- 证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 右侧 ANT pin 21 的短线未连接外部器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M1 LoRa 模组 | `reference=M1`；`part_number=E220-900T22S Module`；`host_bus=UART`；`mode_pins=M0,M1`；`status_pin=AUX`；`rf_pin=ANT` |
| 接口 | J1 Grove UART 接口 | `reference=J1`；`pinout=IO2:TXD,IO1:RXD,5V:5V,GND:GND`；`TXD_module_direction=output from M1`；`RXD_module_direction=input to M1` |
| 总线 | J1 与 M1 UART | `tx_path=M1 TXD/pin 8 -> J1 IO2`；`rx_path=J1 IO1 -> M1 RXD/pin 7`；`level_shifter=null`；`series_resistor=null` |
| GPIO 与控制信号 | S1 与 M0/M1 | `switch_m0=S1 pin 1 M0 to pin 4 GND`；`switch_m1=S1 pin 2 M1 to pin 3 GND`；`closed_level=GND/logic low`；`external_pullups=null` |
| GPIO 与控制信号 | M1 模式与状态引脚 | `M0=pin 5 -> S1`；`M1=pin 6 -> S1`；`AUX=pin 9 unconnected` |
| 电源 | M1 供电 | `supply=VCC/pin 10/5V`；`ground_pins=1,2,3,4,11,13,19,20,22`；`rail=5V` |
| 电源 | 5V 去耦 | `connector_capacitor=C1 10uF`；`module_capacitor=C2 10uF`；`rail=5V`；`return=GND` |
| 射频 | M1 ANT | `rf_pin=M1 ANT/pin 21`；`external_connector=null`；`matching_network=null` |
| 核心器件 | M1 未使用引脚 | `nc_pins=12,14,15,16,17,18` |
| 保护电路 | 接口与电源保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`uart_protection_visible=false` |
| 射频 | LoRa 芯片与频段 | `documented_chip=LLCC68`；`documented_band_mhz=920.6-928.0`；`schematic_internal_chip=null`；`schematic_frequency=null` |
| 射频 | 发射功率与通信距离 | `documented_max_tx_dbm=13`；`documented_distance_km=5`；`schematic_tx_power=null`；`schematic_distance=null` |
| 其他事实 | M0/M1 工作模式 | `documented_modes=0 normal TX/RX,1 WOR TX,2 WOR RX,3 configuration`；`documented_on_level=0`；`documented_off_level=1`；`schematic_mode_table=null` |

## 待确认事项

- `rf.module_chip_band`：产品正文标注模组内部芯片 LLCC68、920.6 至 928.0 MHz 频段；本页原理图只显示 E220-900T22S 模组外部引脚，没有内部芯片或频段标注。（证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 仅标注 E220-900T22S Module，未出现 LLCC68 或频率数值）
- `rf.performance`：产品正文描述最大发射功率 13 dBm 和最大通信距离 5 km，但本页原理图未标注射频功率、天线增益或距离测试条件。（证据：图 cdd9716ab202 / 第 1 页 / 页 1 M1 与 ANT pin 21 区域未打印功率、增益或距离参数）
- `other.mode_semantics`：产品正文定义正常收发、WOR 发送、WOR 接收和参数配置四种 M0/M1 模式；原理图只确认两位开关接地方式，没有模式编号或行为说明。（证据：图 cdd9716ab202 / 第 1 页 / 页 1 S1 与 M0/M1 连接区没有模式表或 WOR 文字）
- `review.module_chip_band`：当前 E220-900T22S(JP) 模组内部是否为 LLCC68，认证版本的有效频段是否为 920.6-928.0 MHz？；原因：原理图只提供模组外部型号和引脚，没有内部芯片、认证版本或频率。
- `review.rf_performance`：13 dBm 和 5 km 参数适用于哪些信道、速率、天线、环境与法规条件？；原因：原理图没有射频测试配置或性能额定值。
- `review.mode_semantics`：S1 的 M0/M1 开关位置与四种工作模式的固件行为是否与正文模式表一致？；原因：原理图只确认开关闭合接地，没有模块内部上拉和模式语义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cdd9716ab2026d3bc54b574a19c173e482c28e5b8d6e402c3480621a9adc0fd2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/623/SCH_UNIT_LoraE220_sch_01.png` |

---

源文档：`zh_CN/unit/LoRaE220-JP Unit.md`

源文档 SHA-256：`0831c0e840929d7752f85455bdd72b03d865e55daef681b84ea9ed8b2c107c2b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
