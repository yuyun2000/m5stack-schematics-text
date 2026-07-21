# Unit HBridge 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit HBridge |
| SKU | U160 |
| 产品 ID | `unit-hbridge-be6746009602` |
| 源文档 | `zh_CN/unit/Hbridge Unit.md` |

## 概述

Unit HBridge 以 U3 STM32F030F4P6 作为 I2C 控制器，通过 MF、MR 控制 U4 RZ7899 H 桥并从 P5 输出 OUT_P、OUT_N。HPWR 经 U1 MP1584EN-LF-Z 降压形成 VCC_5V，S1 在 HPWR 与 VCC_5V 之间选择电机 VM；BUS_5V 还通过 Q1/Q2 自动供电路径接入 VCC_5V。U2 HX6306P332MR 从 BUS_5V 生成 3V3，SW1 四位拨码用于地址配置，J2 提供 SWD 调试。

## 检索关键词

`Unit HBridge`、`U160`、`STM32F030F4P6`、`RZ7899`、`MP1584EN-LF-Z`、`HX6306P332MR`、`I2C`、`0x20`、`SCL`、`SDA`、`MF`、`MR`、`OUT_P`、`OUT_N`、`HPWR`、`VCC_12V`、`VCC_5V`、`BUS_5V`、`3V3`、`VM`、`SW1`、`S1 VM select`、`TA-3539S-A1`、`AO3401A`、`DTC143ZCA`、`HT3.96 4P`、`GROVE 4P`、`SWD`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`PWM`、`3A`、`SS54`、`TVS5V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 从机、电机控制与地址配置控制器 | 图 1c0a851512f2 / 第 1 页 / 页 1 左中控制器区，U3 器件框下方标注 STM32F030F4P6 |
| U4 | RZ7899 | 双向直流电机 H 桥驱动器 | 图 1c0a851512f2 / 第 1 页 / 页 1 右中电机驱动区，U4 连接 MF/MR、VM、OUT_P、OUT_N，型号标注 RZ7899 |
| U1 | MP1584EN-LF-Z | HPWR/VCC_12V 至 VCC_5V 降压转换器 | 图 1c0a851512f2 / 第 1 页 / 页 1 左上电源区，U1 标注 MP1584EN-LF-Z，输出电感连接 VCC_5V |
| U2 | HX6306P332MR | BUS_5V 至 3V3 稳压器 | 图 1c0a851512f2 / 第 1 页 / 页 1 右上 U2，标注 HX6306P332MR，VIN 接 BUS_5V、VOUT 接 3V3 |
| J1 | GROVE 4P | I2C 与 BUS_5V 主机接口 | 图 1c0a851512f2 / 第 1 页 / 页 1 上中部 J1 GROVE 4P，端子标注 SCL、SDA、5V、GND |
| P5 | HT3.96 4P | 电机输出与外部 HPWR 电源端子 | 图 1c0a851512f2 / 第 1 页 / 页 1 右中部 P5 HT3.96 4P，1 至 4 脚连接 OUT_P、OUT_N、GND、HPWR |
| SW1 | 4-position DIP switch | 四位 I2C 地址配置开关 | 图 1c0a851512f2 / 第 1 页 / 页 1 中部 for I2C address config 区域，SW1 四组触点连接 U3 PA0-PA3 与 GND |
| S1 | TA-3539S-A1 | 电机 VM 电源选择开关 | 图 1c0a851512f2 / 第 1 页 / 页 1 右中上 VM select 区域，S1 标注 TA-3539S-A1，连接 HPWR、VCC_5V 与 VM |
| Q1 | AO3401A | BUS_5V 至 VCC_5V 自动供电路径的高侧 MOSFET | 图 1c0a851512f2 / 第 1 页 / 页 1 中上电源切换区，Q1 标注 AO3401A，位于 BUS_5V 与 D5/VCC_5V 之间 |
| Q2 | DTC143ZCA | 根据 HPWR 检测网络控制 Q1 栅极 | 图 1c0a851512f2 / 第 1 页 / 页 1 中上电源切换区，Q2 标注 DTC143ZCA，连接 R18/R19 检测节点与 Q1 栅极 |
| J2 | SWD 5P | 五针 SWD 下载、调试与复位接口 | 图 1c0a851512f2 / 第 1 页 / 页 1 下中部 J2 SWD，1 至 5 脚连接 3V3、SWCLK、SWDIO、NRST、GND |

## 系统结构

### Unit HBridge 控制架构

U3 STM32F030F4P6 通过 I2C 与 J1 相连，并以 MF、MR 控制 U4 RZ7899；U4 从 VM 取电并驱动 OUT_P、OUT_N。

- 参数与网络：`controller=U3 STM32F030F4P6`；`motor_driver=U4 RZ7899`；`host_bus=I2C`；`control_nets=MF,MR`；`motor_supply=VM`；`motor_outputs=OUT_P,OUT_N`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 中部 U3 与右中 U4、J1 之间的 SCL/SDA、MF/MR、VM、OUT_P/OUT_N 网络

## 核心器件

### U4 RZ7899

U4 RZ7899 的 VCC 连接 VM，INF/INR 接 MF/MR，两个输出网络为 OUT_P、OUT_N，GND 接地。

- 参数与网络：`reference=U4`；`part_number=RZ7899`；`supply=VM`；`inputs=INF:MF,INR:MR`；`outputs=OUT_P,OUT_N`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 右中 U4 器件框、引脚名和 VM/MF/MR/OUT_P/OUT_N 网络

## 电源

### U1 VCC_5V 降压电源

HPWR 经串联 D1 到 VCC_12V，U1 MP1584EN-LF-Z 从 VCC_12V 降压并通过输出电感 L1 形成 VCC_5V。

- 参数与网络：`input_path=HPWR -> D1 -> VCC_12V`；`converter=U1 MP1584EN-LF-Z`；`output_inductor=L1`；`output_rail=VCC_5V`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 左上电源区，HPWR、D1、VCC_12V、U1、L1 与 VCC_5V 连续路径

### U2 3V3 电源

U2 HX6306P332MR 的 VIN 引脚 3 接 BUS_5V，VOUT 引脚 2 输出 3V3，GND 引脚 1 接地。

- 参数与网络：`reference=U2`；`part_number=HX6306P332MR`；`input=VIN/pin 3/BUS_5V`；`output=VOUT/pin 2/3V3`；`ground=GND/pin 1`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 右上 U2 引脚号、BUS_5V/3V3/GND 网络

### BUS_5V 至 VCC_5V 自动供电路径

Q1 AO3401A 位于 BUS_5V 与 D5/VCC_5V 之间，其栅极由 Q2 DTC143ZCA 及 HPWR 检测分压网络控制；R17 100 kΩ 将控制节点下拉至 GND。

- 参数与网络：`high_side_switch=Q1 AO3401A`；`control_transistor=Q2 DTC143ZCA`；`source_rail=BUS_5V`；`destination_path=D5 -> VCC_5V`；`sense_network=R18/R19 from HPWR to GND`；`gate_pulldown=R17 100k`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 中上 Q1/Q2、R17-R19、BUS_5V、HPWR 与 D5/VCC_5V 电路块

### S1 电机电源选择

S1 TA-3539S-A1 标注 VM select，连接 HPWR、VCC_5V 与经 D7 引出的 VM 网络，用于选择电机驱动供电来源。

- 参数与网络：`reference=S1`；`part_number=TA-3539S-A1`；`sources=HPWR,VCC_5V`；`selected_rail=VM`；`series_diode=D7`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 右中上 VM select 区域，S1、D7 与 HPWR/VCC_5V/VM 网络

### U3 供电

U3 的 VDD 引脚 16 和 VDDA 引脚 5 连接 3V3，VSS 引脚 15 连接 GND；C4 100 nF 跨接 3V3 与 GND。

- 参数与网络：`supply_pins=VDD/pin 16,VDDA/pin 5`；`rail=3V3`；`ground_pin=VSS/pin 15`；`decoupling=C4 100nF`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 下方 VSS/VDD/VDDA 与 C4 100nF 网络

## 接口

### J1 Grove 接口

J1 的四个端子标注 SCL、SDA、5V、GND，对应网络为 SCL、SDA、BUS_5V、GND。

- 参数与网络：`reference=J1`；`terminals=SCL,SDA,5V,GND`；`networks=SCL,SDA,BUS_5V,GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 上中部 J1 GROVE 4P 端子与网络文字

### P5 电机与外部电源端子

P5 的 1 至 4 脚依次连接 OUT_P、OUT_N、GND、HPWR。

- 参数与网络：`reference=P5`；`pinout=1:OUT_P,2:OUT_N,3:GND,4:HPWR`；`motor_outputs=pins 1-2`；`power_input=pins 4-3`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 右中 P5 HT3.96 4P 的脚号与左侧网络标注

## 总线

### U3 I2C 总线

SCL、SDA 分别连接 U3 的 PA9 引脚 17、PA10 引脚 18，并连接 J1；R15、R16 均为 10 kΩ，将两条总线上拉至 3V3。

- 参数与网络：`controller=U3`；`connector=J1`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R15 10k to 3V3`；`sda_pullup=R16 10k to 3V3`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 PA9/PA10、J1 SCL/SDA 与上方 R15/R16 上拉网络

## GPIO 与控制信号

### U3 与 SW1 地址配置

U3 的 PA0、PA1、PA2、PA3 引脚 6、7、8、9 分别连接 SW1 的四位开关；每路由一只 10 kΩ 电阻上拉至 3V3，开关闭合时接 GND。

- 参数与网络：`switch_1=PA0/pin 6`；`switch_2=PA1/pin 7`；`switch_3=PA2/pin 8`；`switch_4=PA3/pin 9`；`pullups=R8,R9,R10,R11 10k to 3V3`；`switch_common=GND`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 中部 for I2C address config，U3 PA0-PA3、R8-R11 与 SW1 四位触点

### U3 电机控制输出

U3 的 PA6 引脚 12 连接 MF，PA7 引脚 13 连接 MR；MF、MR 分别进入 U4 的 INF、INR 控制输入。

- 参数与网络：`MF=U3 PA6/pin 12 -> U4 INF`；`MR=U3 PA7/pin 13 -> U4 INR`；`direction=U3 output to motor driver`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 右侧 PA6/PA7 的 MF/MR 与右中 U4 INF/INR 网络

### U3 BOOT0

U3 BOOT0 引脚 1 通过 R7 10 kΩ 下拉至 GND。

- 参数与网络：`mcu_pin=BOOT0/pin 1`；`pulldown=R7 10k to GND`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 左侧 BOOT0 引脚 1、R7 10K 与 GND

## 时钟

### U3 外部时钟

U3 的 PF0-OSC_IN 引脚 2 与 PF1-OSC_OUT 引脚 3 在本页未连接外部晶振或时钟器件。

- 参数与网络：`osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 左上 PF0-OSC_IN/PF1-OSC_OUT 引脚短线无外接器件

## 复位

### U3 NRST

U3 NRST 引脚 4 连接 NRST 网络，该网络由 10 kΩ 电阻上拉至 3V3、由 100 nF 电容连接 GND，并引出到 J2。

- 参数与网络：`mcu_pin=NRST/pin 4`；`pullup_ohm=10000`；`capacitance_nf=100`；`debug_connector=J2`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 左侧 NRST 上拉/电容网络及下方 J2 NRST

## 保护电路

### VCC_5V 输出保护

U1 输出侧包含对地续流二极管 D2，以及跨接 VCC_5V 与 GND、标注 TVS5V 的 D3。

- 参数与网络：`freewheel_diode=D2`；`tvs_reference=D3`；`tvs_marking=TVS5V`；`protected_rail=VCC_5V`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 左上 U1 输出电感附近 D2 及 VCC_5V 旁 D3 TVS5V

## 调试与烧录

### U3 与 J2 SWD

U3 PA13 引脚 19 的 SWDIO、PA14 引脚 20 的 SWCLK 连接 J2；J2 的 1 至 5 脚依次连接 3V3、SWCLK、SWDIO、NRST、GND。

- 参数与网络：`swdio=U3 PA13/pin 19`；`swclk=U3 PA14/pin 20`；`connector_pinout=J2 1:3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND`
- 证据：图 1c0a851512f2 / 第 1 页 / 页 1 U3 PA13/PA14 网络与下方 J2 SWD 五针接口

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit HBridge 控制架构 | `controller=U3 STM32F030F4P6`；`motor_driver=U4 RZ7899`；`host_bus=I2C`；`control_nets=MF,MR`；`motor_supply=VM`；`motor_outputs=OUT_P,OUT_N` |
| 接口 | J1 Grove 接口 | `reference=J1`；`terminals=SCL,SDA,5V,GND`；`networks=SCL,SDA,BUS_5V,GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | U3 I2C 总线 | `controller=U3`；`connector=J1`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R15 10k to 3V3`；`sda_pullup=R16 10k to 3V3` |
| GPIO 与控制信号 | U3 与 SW1 地址配置 | `switch_1=PA0/pin 6`；`switch_2=PA1/pin 7`；`switch_3=PA2/pin 8`；`switch_4=PA3/pin 9`；`pullups=R8,R9,R10,R11 10k to 3V3`；`switch_common=GND` |
| 总线地址 | Unit HBridge I2C 地址 | `documented_default_address=0x20`；`address_switch=SW1 4-position`；`address_gpio=PA0,PA1,PA2,PA3`；`schematic_address_formula=null` |
| GPIO 与控制信号 | U3 电机控制输出 | `MF=U3 PA6/pin 12 -> U4 INF`；`MR=U3 PA7/pin 13 -> U4 INR`；`direction=U3 output to motor driver` |
| 核心器件 | U4 RZ7899 | `reference=U4`；`part_number=RZ7899`；`supply=VM`；`inputs=INF:MF,INR:MR`；`outputs=OUT_P,OUT_N` |
| 接口 | P5 电机与外部电源端子 | `reference=P5`；`pinout=1:OUT_P,2:OUT_N,3:GND,4:HPWR`；`motor_outputs=pins 1-2`；`power_input=pins 4-3` |
| 电源 | U1 VCC_5V 降压电源 | `input_path=HPWR -> D1 -> VCC_12V`；`converter=U1 MP1584EN-LF-Z`；`output_inductor=L1`；`output_rail=VCC_5V` |
| 保护电路 | VCC_5V 输出保护 | `freewheel_diode=D2`；`tvs_reference=D3`；`tvs_marking=TVS5V`；`protected_rail=VCC_5V` |
| 电源 | U2 3V3 电源 | `reference=U2`；`part_number=HX6306P332MR`；`input=VIN/pin 3/BUS_5V`；`output=VOUT/pin 2/3V3`；`ground=GND/pin 1` |
| 电源 | BUS_5V 至 VCC_5V 自动供电路径 | `high_side_switch=Q1 AO3401A`；`control_transistor=Q2 DTC143ZCA`；`source_rail=BUS_5V`；`destination_path=D5 -> VCC_5V`；`sense_network=R18/R19 from HPWR to GND`；`gate_pulldown=R17 100k` |
| 电源 | S1 电机电源选择 | `reference=S1`；`part_number=TA-3539S-A1`；`sources=HPWR,VCC_5V`；`selected_rail=VM`；`series_diode=D7` |
| 电源 | U3 供电 | `supply_pins=VDD/pin 16,VDDA/pin 5`；`rail=3V3`；`ground_pin=VSS/pin 15`；`decoupling=C4 100nF` |
| 复位 | U3 NRST | `mcu_pin=NRST/pin 4`；`pullup_ohm=10000`；`capacitance_nf=100`；`debug_connector=J2` |
| GPIO 与控制信号 | U3 BOOT0 | `mcu_pin=BOOT0/pin 1`；`pulldown=R7 10k to GND` |
| 调试与烧录 | U3 与 J2 SWD | `swdio=U3 PA13/pin 19`；`swclk=U3 PA14/pin 20`；`connector_pinout=J2 1:3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND` |
| 时钟 | U3 外部时钟 | `osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false` |
| 核心器件 | 电机驱动额定值与保护 | `documented_max_current_a=3`；`documented_protections=overcurrent,overvoltage,overtemperature`；`schematic_current_rating=null`；`schematic_internal_protection=null` |

## 待确认事项

- `address.i2c`：产品正文给出默认 I2C 地址 0x20 并称可通过 SW1 修改；原理图确认四位地址输入硬件，但未标出拨码到最终地址的计算关系。（证据：图 1c0a851512f2 / 第 1 页 / 页 1 SW1 地址配置区只标注 for I2C address config，未出现 0x20 或位权公式）
- `component.motor_limits`：产品正文称最大电流 3 A，并具备过流、过压、过热保护；本页原理图未标注 3 A 额定值或 U4 内部保护条件。（证据：图 1c0a851512f2 / 第 1 页 / 页 1 U4 RZ7899 与 OUT_P/OUT_N 功率路径未标注电流额定值或内部保护阈值）
- `review.i2c_address`：SW1 四位拨码与固件 I2C 地址的位权关系及默认 0x20 配置是什么？；原因：原理图只确认 PA0-PA3 拨码输入，没有地址公式或默认地址文字。
- `review.motor_limits`：3 A 最大电流与过流、过压、过热保护分别适用哪些电压、温度和散热条件？；原因：原理图未给出 U4 内部保护阈值、热设计或板级电流额定值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1c0a851512f226d2d480ad8ad76998f65c63059d80dd66aca1f79d4f055432b7` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-f4f40b0f-e9ef-47f0-9b5d-6378e00d3c0f.png` |

---

源文档：`zh_CN/unit/Hbridge Unit.md`

源文档 SHA-256：`36739215f9ba8175458bf8f23339804ff9ba8f6cf178f07ec971a55fcc52acc0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
