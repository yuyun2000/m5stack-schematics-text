# Unit ExtEncoder 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ExtEncoder |
| SKU | U161 |
| 产品 ID | `unit-extencoder-afea3e9f9b59` |
| 源文档 | `zh_CN/unit/ExtEncoder Unit.md` |

## 概述

Unit ExtEncoder 以 U1 STM32F030F4P6 为控制器，从 P6 接收 A1、B1、Z1 三路编码器信号，并通过 J1 Grove 接口的 SCL、SDA 与主机通信。VCC_5V 经 U2 HX6306 转换为 3V3，分别为控制器和输入上拉网络供电。板上还提供 J2 五针 SWD 调试接口、NRST 复位网络、BOOT0 下拉以及 P6 电源入口的 5 V TVS 保护。

## 检索关键词

`Unit ExtEncoder`、`U161`、`STM32F030F4P6`、`HX6306`、`GROVE 4P`、`I2C`、`0x59`、`SCL`、`SDA`、`A1`、`B1`、`Z1`、`ABZ encoder`、`P6`、`J1`、`J2`、`SWD_5P`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`BOOT0`、`VCC_5V`、`3V3`、`TVS 5V`、`PA4`、`PA6`、`PA7`、`PA9`、`PA10`、`PA13`、`PA14`、`12-bit`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 编码器信号采集与 I2C 通信控制器 | 图 db8136665eae / 第 1 页 / 页 1 网格 C1-C2，U1 器件框下方标注 STM32F030F4P6 |
| U2 | HX6306 | VCC_5V 至 3V3 电源转换器 | 图 db8136665eae / 第 1 页 / 页 1 网格 B2，U2 标注 HX6306，VIN/VOUT 分别连接 VCC_5V/3V3 |
| J1 | GROVE 4P | 主机侧 I2C 与 5 V 电源接口 | 图 db8136665eae / 第 1 页 / 页 1 网格 B1，J1 GROVE 4P，端子标注 SCL、SDA、5V、GND |
| P6 | Header 5 | A/B/Z 编码器信号与 5 V 电源输入接口 | 图 db8136665eae / 第 1 页 / 页 1 网格 B3，P6 Header 5，1 至 5 脚连接 A1、B1、Z1、VCC_5V、GND |
| J2 | SWD_5P | 五针 SWD 调试与复位接口 | 图 db8136665eae / 第 1 页 / 页 1 网格 C3，J2 SWD_5P，端子标注 VCC、SWCLK、SWDIO、NRST、GND |
| D1 | TVS 5V | P6 的 VCC_5V 对地瞬态保护器件 | 图 db8136665eae / 第 1 页 / 页 1 网格 B3，D1 标注 TVS 5V，跨接 VCC_5V 与 GND |

## 系统结构

### U1

U1 的器件型号为 STM32F030F4P6，连接三路编码器输入、I2C 和 SWD 网络。

- 参数与网络：`reference=U1`；`part_number=STM32F030F4P6`；`encoder_inputs=A1,B1,Z1`；`host_bus=I2C`；`debug_bus=SWD`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C1-C2，U1 型号及左右两侧网络标注

## 电源

### U2 电源转换

U2 HX6306 的 VIN 引脚 3 接 VCC_5V，VOUT 引脚 2 输出 3V3，GND 引脚 1 接地。

- 参数与网络：`reference=U2`；`part_number=HX6306`；`vin_pin=3`；`input_rail=VCC_5V`；`vout_pin=2`；`output_rail=3V3`；`gnd_pin=1`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B2，U2 VIN/VOUT/GND 引脚号及 VCC_5V、3V3、GND 网络

### U2 输入输出去耦

U2 输入侧 C5 为 100 nF，跨接 VCC_5V 与 GND；输出侧 C7 100 nF 和 C8 10 uF 并联在 3V3 与 GND 之间。

- 参数与网络：`input_capacitor=C5 100nF`；`output_capacitors=C7 100nF,C8 10uF`；`input_rail=VCC_5V`；`output_rail=3V3`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B2，U2 左右两侧 C5、C7、C8 及电源网络

### U1 供电

U1 的 VDD 引脚 16 和 VDDA 引脚 5 连接 3V3，VSS 引脚 15 连接 GND。

- 参数与网络：`supply_pins=VDD/pin 16,VDDA/pin 5`；`supply_rail=3V3`；`ground_pin=VSS/pin 15`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C1-C2，U1 VDD/VDDA/VSS 引脚及 3V3/GND 网络

### U1 电源去耦

C10 100 nF 与 C11 10 uF 并联在 U1 的 3V3 供电节点和 GND 之间。

- 参数与网络：`capacitors=C10 100nF,C11 10uF`；`rail=3V3`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C1，U1 VDD/VDDA 左侧 C10、C11 与 GND

## 接口

### P6 编码器接口

P6 的 1 至 5 脚依次连接 A1、B1、Z1、VCC_5V 和 GND；A1、B1、Z1 为流向 U1 的输入网络。

- 参数与网络：`reference=P6`；`pinout=1:A1,2:B1,3:Z1,4:VCC_5V,5:GND`；`signal_direction=A1/B1/Z1: input to U1`；`signal_level_rail=3V3 pull-up`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B3，P6 脚号、A1/B1/Z1/VCC_5V 网络及第 5 脚接地连线

### J1 Grove 接口

J1 的四个端子依次标注 SCL、SDA、5V 和 GND，对应网络为 SCL、SDA、VCC_5V 和 GND。

- 参数与网络：`reference=J1`；`terminals=SCL,SDA,5V,GND`；`networks=SCL,SDA,VCC_5V,GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B1，J1 GROVE 4P 端子文字与右侧网络

## 总线

### U1 与 J1 的 I2C 总线

J1 的 SCL、SDA 网络分别连接 U1 的 PA9 引脚 17、PA10 引脚 18；R15、R16 均为 10 kΩ，并将 SCL、SDA 上拉至 3V3。

- 参数与网络：`controller=U1`；`connector=J1`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R15 10k to 3V3`；`sda_pullup=R16 10k to 3V3`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B1 与 C1，J1 SCL/SDA、R15/R16 及 U1 PA9/PA10 网络标注

## GPIO 与控制信号

### U1 编码器输入映射

Z1、A1、B1 分别连接 U1 的 PA4 引脚 10、PA6 引脚 12、PA7 引脚 13。

- 参数与网络：`Z1=PA4/pin 10`；`A1=PA6/pin 12`；`B1=PA7/pin 13`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C1，U1 左侧 Z1/A1/B1 网络与 PA4/PA6/PA7 引脚号

### U1 BOOT0

U1 BOOT0 引脚 1 通过 R6 10 kΩ 下拉至 GND。

- 参数与网络：`mcu_pin=BOOT0/pin 1`；`pulldown=R6 10k to GND`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C2，U1 BOOT0 引脚 1、R6 10K 与 GND

## 时钟

### U1 时钟连接

U1 的 PF0-OSC_IN 引脚 2 和 PF1-OSC_OUT 引脚 3 在本页未连接外部晶振或时钟器件。

- 参数与网络：`osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C2，U1 PF0-OSC_IN 与 PF1-OSC_OUT 引脚短线无外接器件

## 复位

### U1 NRST

U1 NRST 引脚 4 连接 NRST 网络；R7 10 kΩ 将其上拉至 3V3，C9 100 nF 将其连接至 GND，并引出到 J2。

- 参数与网络：`mcu_pin=NRST/pin 4`；`pullup=R7 10k to 3V3`；`capacitor=C9 100nF to GND`；`debug_connector=J2`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C2-C3，U1 NRST、R7、C9 与 J2 NRST 网络

## 保护电路

### P6 VCC_5V 保护

D1 标注为 TVS 5V，跨接 P6 的 VCC_5V 网络与 GND。

- 参数与网络：`reference=D1`；`part_number=TVS 5V`；`protected_net=VCC_5V`；`return_net=GND`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B3，P6 下方 D1 与 VCC_5V/GND 连线

## 调试与烧录

### U1 与 J2 的 SWD 接口

U1 PA13 引脚 19 的 MCU_SWDIO 和 PA14 引脚 20 的 MCU_SWCLK 引出到 J2；J2 还引出 3V3、NRST 和 GND。

- 参数与网络：`swdio=U1 PA13/pin 19 -> J2 MCU_SWDIO`；`swclk=U1 PA14/pin 20 -> J2 MCU_SWCLK`；`connector_signals=3V3,MCU_SWCLK,MCU_SWDIO,NRST,GND`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 C1 与 C3，U1 PA13/PA14 网络及 J2 SWD_5P 端子

## 模拟电路

### A1/B1/Z1 输入整形

A1、B1、Z1 各由一只 10 kΩ 电阻上拉至 3V3，并各由一只 100 nF 电容连接 GND：对应关系为 A1-R1/C4、B1-R2/C6、Z1-R8/C12。

- 参数与网络：`A1_network=R1 10k pull-up,C4 100nF to GND`；`B1_network=R2 10k pull-up,C6 100nF to GND`；`Z1_network=R8 10k pull-up,C12 100nF to GND`；`pullup_rail=3V3`
- 证据：图 db8136665eae / 第 1 页 / 页 1 网格 B3，R1/R2/R8、C4/C6/C12 与 A1/B1/Z1 的连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | U1 | `reference=U1`；`part_number=STM32F030F4P6`；`encoder_inputs=A1,B1,Z1`；`host_bus=I2C`；`debug_bus=SWD` |
| GPIO 与控制信号 | U1 编码器输入映射 | `Z1=PA4/pin 10`；`A1=PA6/pin 12`；`B1=PA7/pin 13` |
| 接口 | P6 编码器接口 | `reference=P6`；`pinout=1:A1,2:B1,3:Z1,4:VCC_5V,5:GND`；`signal_direction=A1/B1/Z1: input to U1`；`signal_level_rail=3V3 pull-up` |
| 模拟电路 | A1/B1/Z1 输入整形 | `A1_network=R1 10k pull-up,C4 100nF to GND`；`B1_network=R2 10k pull-up,C6 100nF to GND`；`Z1_network=R8 10k pull-up,C12 100nF to GND`；`pullup_rail=3V3` |
| 接口 | J1 Grove 接口 | `reference=J1`；`terminals=SCL,SDA,5V,GND`；`networks=SCL,SDA,VCC_5V,GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | U1 与 J1 的 I2C 总线 | `controller=U1`；`connector=J1`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R15 10k to 3V3`；`sda_pullup=R16 10k to 3V3` |
| 总线地址 | Unit ExtEncoder I2C 地址 | `documented_address=0x59`；`schematic_address=null` |
| 电源 | U2 电源转换 | `reference=U2`；`part_number=HX6306`；`vin_pin=3`；`input_rail=VCC_5V`；`vout_pin=2`；`output_rail=3V3`；`gnd_pin=1` |
| 电源 | U2 输入输出去耦 | `input_capacitor=C5 100nF`；`output_capacitors=C7 100nF,C8 10uF`；`input_rail=VCC_5V`；`output_rail=3V3` |
| 电源 | U1 供电 | `supply_pins=VDD/pin 16,VDDA/pin 5`；`supply_rail=3V3`；`ground_pin=VSS/pin 15` |
| 电源 | U1 电源去耦 | `capacitors=C10 100nF,C11 10uF`；`rail=3V3` |
| 保护电路 | P6 VCC_5V 保护 | `reference=D1`；`part_number=TVS 5V`；`protected_net=VCC_5V`；`return_net=GND` |
| 复位 | U1 NRST | `mcu_pin=NRST/pin 4`；`pullup=R7 10k to 3V3`；`capacitor=C9 100nF to GND`；`debug_connector=J2` |
| GPIO 与控制信号 | U1 BOOT0 | `mcu_pin=BOOT0/pin 1`；`pulldown=R6 10k to GND` |
| 调试与烧录 | U1 与 J2 的 SWD 接口 | `swdio=U1 PA13/pin 19 -> J2 MCU_SWDIO`；`swclk=U1 PA14/pin 20 -> J2 MCU_SWCLK`；`connector_signals=3V3,MCU_SWCLK,MCU_SWDIO,NRST,GND` |
| 时钟 | U1 时钟连接 | `osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false` |
| 系统结构 | 编码器采样精度 | `documented_resolution_bits=12`；`schematic_resolution_bits=null` |

## 待确认事项

- `address.i2c`：产品正文给出 I2C 地址 0x59，但本页原理图没有地址标注或地址选择网络，无法仅由原理图确认。（证据：图 db8136665eae / 第 1 页 / 页 1 网格 B1-C1，完整 SCL/SDA 链路仅显示上拉与 U1 引脚，未显示地址值或地址选择网络）
- `system.sampling_resolution`：产品正文描述 12 位采样精度，但本页原理图未标注采样位数或相应配置，无法仅由原理图确认。（证据：图 db8136665eae / 第 1 页 / 页 1 网格 B3-C2，A1/B1/Z1 输入链路与 U1 连接未标注采样位数）
- `review.i2c_address`：固件定义的 Unit ExtEncoder I2C 从机地址是否为产品正文所列 0x59？；原因：原理图仅显示 I2C 物理连接，没有地址值、地址选择引脚或固件定义。
- `review.sampling_resolution`：产品正文所述 12 位采样精度具体由固件计数范围还是其他处理逻辑实现？；原因：原理图只显示数字输入的 RC 网络及 MCU 引脚，未给出采样分辨率定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `db8136665eae5ac861966fedc84e74452ef569efff09eeb7c0abdb0ed28184f9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/616/SCH_UNIT_EXTEncoder_sch_01.png` |

---

源文档：`zh_CN/unit/ExtEncoder Unit.md`

源文档 SHA-256：`ad0eb4f1c5b0c86d45c34a55eeec410da5395785a4f70b907998250cdde7f3b9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
