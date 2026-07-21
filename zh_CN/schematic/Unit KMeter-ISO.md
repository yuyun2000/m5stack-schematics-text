# Unit KMeter-ISO 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit KMeter-ISO |
| SKU | U133-V11 |
| 产品 ID | `unit-kmeter-iso-446da9e20650` |
| 源文档 | `zh_CN/unit/KMeterISO Unit.md` |

## 概述

Unit KMeter-ISO 以 U2 STM32F030F4P6 作为 Grove I2C 控制器，通过 MCU_CS、MCU_SCK、MCU_MISO 三线只读 SPI 访问热电偶转换器。U3 CA-IS3641HW 将 SPI 隔离为 TC_CS、TC_SCK、TC_MISO，并由 VISO 经磁珠生成隔离侧 VCC_A3V3。U4 MAX31855KASA+T 连接 TC1 PCC-SMP-K-100-CE K 型热电偶接口，T+/T-/SH 路径配置磁珠和 10 nF 滤波；U1 MD5333 将 5 V 转为 MCU 侧 3.3 V。

## 检索关键词

`Unit KMeter-ISO`、`U133-V11`、`STM32F030F4P6`、`CA-IS3641HW`、`MAX31855KASA+T`、`MAX31855`、`MD5333`、`PCC-SMP-K-100-CE`、`K thermocouple`、`I2C`、`0x66`、`SPI`、`MCU_CS`、`MCU_SCK`、`MCU_MISO`、`TC_CS`、`TC_SCK`、`TC_MISO`、`T+`、`T-`、`SH`、`VISO`、`VCC_A3V3`、`VCC_3V3`、`VCC_5V`、`GND_ISO`、`SCL`、`SDA`、`SWD`、`NRST`、`BOOT0`、`TEMP_Read`、`14-bit`、`10Hz`、`5MHz`、`-200C to 1350C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | I2C 通信、SPI 采集与状态指示控制器 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 C1-C2 MCU 区域，U2 器件框下方标注 STM32F030F4P6 |
| U3 | CA-IS3641HW | SPI 数字隔离器与隔离侧电源源端 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 A3-B3 Isolated SPI 区域，U3 下方标注 CA-IS3641HW |
| U4 | MAX31855KASA+T | K 型热电偶到数字 SPI 转换器 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 C3 Thermocouple Converter 区域，U4 标注 MAX31855KASA+T |
| U1 | MD5333 | VCC_5V 至 VCC_3V3 MCU 侧 LDO | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 A1 MCU LDO 区域，U1 标注 MD5333，VIN/VOUT 接 VCC_5V/VCC_3V3 |
| TC1 | PCC-SMP-K-100-CE | K 型热电偶 T+/T-/SH 接口 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 C4 Thermocouple Connector 区域，TC1 下方标注 PCC-SMP-K-100-CE，端子为 T-、T+、SH |
| GROVE | Grove 4P | I2C 与 VCC_5V 主机接口 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 A2 Grove I2C 区域，四针标注 IO2、IO1、5V、GND 并连接 SCL、SDA、VCC_5V、GND |
| J2 | SWD_5P | 五针 MCU SWD 下载、调试与复位接口 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 D2 MCU DL CON 区域，J2 标注 SWD_5P |
| LED1 | red LED | TEMP_Read 温度读取状态指示灯 | 图 31dd2e5caffb / 第 1 页 / 页 1 网格 C2 Temp LED 区域，LED1 标注 red，连接 TEMP_Read 与 R1 |

## 系统结构

### Unit KMeter-ISO 采集架构

U2 STM32F030F4P6 通过 Grove I2C 与主机通信，通过 U3 隔离的三线 SPI 读取 U4 MAX31855KASA+T；U4 从 TC1 接收热电偶 T+/T- 信号。

- 参数与网络：`controller=U2 STM32F030F4P6`；`host_bus=I2C`；`isolator=U3 CA-IS3641HW`；`sensor_bus=3-wire read-only SPI`；`converter=U4 MAX31855KASA+T`；`thermocouple_connector=TC1 PCC-SMP-K-100-CE`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 Grove I2C、MCU、Isolated SPI、Thermocouple Converter 与 Connector 五个功能块

## 电源

### U1 MCU LDO

U1 MD5333 的 VIN 引脚 3 接 VCC_5V，VOUT 引脚 2 输出 VCC_3V3，GND 引脚 1 接地。

- 参数与网络：`reference=U1`；`part_number=MD5333`；`input=VIN/pin 3/VCC_5V`；`output=VOUT/pin 2/VCC_3V3`；`ground=GND/pin 1`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 A1 U1 引脚号与 VCC_5V/VCC_3V3/GND 网络

### U1 输入输出去耦

U1 输入侧 C1 4.7 uF 与 C2 100 nF 并联在 VCC_5V 与 GND 之间；输出侧 C3 4.7 uF 与 C4 100 nF 并联在 VCC_3V3 与 GND 之间。

- 参数与网络：`input_capacitors=C1 4.7uF,C2 100nF`；`output_capacitors=C3 4.7uF,C4 100nF`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 A1 U1 左右两侧 C1-C4 与电源网络

### MCU 与热电偶隔离域

U3 MCU 侧使用 VCC_5V、GND，隔离侧使用 VCC_A3V3、GND_ISO；GNDA 引脚 2/8 接 GND，GNDB 引脚 15/9 接 GND_ISO。

- 参数与网络：`mcu_domain=VCC_5V,GND`；`isolated_domain=VCC_A3V3,GND_ISO`；`gnda_pins=2,8`；`gndb_pins=15,9`；`galvanic_ground_connection=false`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U3 两侧 VDD/VISO、GNDA/GNDB 与 GND/GND_ISO 网络

### U3 VISO 输出

U3 VISO 引脚 16 经 330R/GZ1005D331TF 磁珠 FB3 输出 VCC_A3V3；VISO 侧使用 C6、C8 各 22 uF 对 GND_ISO，磁珠后 C16 100 nF 对 GND_ISO。

- 参数与网络：`source_pin=U3 VISO/pin 16`；`filter_bead=FB3 330R/GZ1005D331TF`；`output_rail=VCC_A3V3`；`bulk_capacitors=C6 22uF,C8 22uF`；`post_filter_capacitor=C16 100nF`；`return=GND_ISO`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 A3 U3 VISO 右侧 FB3、C6/C8/C16 与 VCC_A3V3/GND_ISO

### U4 供电

U4 VCC 引脚 4 连接 VCC_A3V3，GND 引脚 1 连接 GND_ISO；C12 100 nF 与 C13 10 uF 并联在供电与隔离地之间。

- 参数与网络：`supply=VCC/pin 4/VCC_A3V3`；`ground=GND/pin 1/GND_ISO`；`decoupling=C12 100nF,C13 10uF`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C3 U4 VCC/GND 与 C12/C13

### U2 供电

U2 VDD 引脚 16 与 VDDA 引脚 5 连接 VCC_3V3，VSS 引脚 15 接 GND；C15 100 nF 跨接 VCC_3V3 与 GND。

- 参数与网络：`supply_pins=VDD/pin 16,VDDA/pin 5`；`rail=VCC_3V3`；`ground_pin=VSS/pin 15`；`decoupling=C15 100nF`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U2 左下 VDD/VDDA/VSS 与 C15

## 接口

### GROVE I2C 接口

GROVE 的 IO2、IO1、5V、GND 四针分别连接 SCL、SDA、VCC_5V、GND。

- 参数与网络：`reference=GROVE`；`pinout=IO2:SCL,IO1:SDA,5V:VCC_5V,GND:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 A2 GROVE 四针文字与右侧 SCL/SDA/VCC_5V/GND 网络

### TC1 K 型热电偶接口

TC1 型号标注 PCC-SMP-K-100-CE，三个端子分别标注 T-、T+、SH；SH 连接经磁珠滤波的 GND_ISO。

- 参数与网络：`reference=TC1`；`part_number=PCC-SMP-K-100-CE`；`terminals=T-,T+,SH`；`shield_return=GND_ISO via ferrite bead`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C4 TC1 符号、T-/T+/SH 标签和 PCC-SMP-K-100-CE 型号

## 总线

### U2 与 GROVE 的 I2C

SCL、SDA 分别连接 U2 的 PA9 引脚 17、PA10 引脚 18；两条网络分别由 R2、R3 10 kΩ 上拉至 VCC_3V3。

- 参数与网络：`controller=U2`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R2 10k to VCC_3V3`；`sda_pullup=R3 10k to VCC_3V3`；`connector=GROVE`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U2 PA9/PA10 与 Grove 区域 SCL/SDA、R2/R3 上拉网络

### U2 MCU 侧 SPI

U2 的 PA4 引脚 10、PA5 引脚 11、PA6 引脚 12 分别连接 MCU_CS、MCU_SCK、MCU_MISO。

- 参数与网络：`chip_select=PA4/pin 10/MCU_CS`；`clock=PA5/pin 11/MCU_SCK`；`data_in=PA6/pin 12/MCU_MISO`；`mosi=null`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C1，U2 PA4-PA6 与 MCU_CS/MCU_SCK/MCU_MISO 网络

### U3 隔离 SPI 映射

U3 将 MCU_CS 从 VI1 引脚 3 隔离到 VO1 引脚 14 的 TC_CS，将 MCU_SCK 从 VI2 引脚 4 隔离到 VO2 引脚 13 的 TC_SCK；TC_MISO 从 VI4 引脚 11 隔离到 VO4 引脚 6 的 MCU_MISO。

- 参数与网络：`cs_path=MCU_CS -> U3 VI1/pin 3 -> VO1/pin 14 -> TC_CS`；`sck_path=MCU_SCK -> U3 VI2/pin 4 -> VO2/pin 13 -> TC_SCK`；`miso_path=TC_MISO -> U3 VI4/pin 11 -> VO4/pin 6 -> MCU_MISO`；`unused_channel=VI3/pin 5 and VO3/pin 12 unconnected`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 A3-B3 U3 两侧 MCU_CS/MCU_SCK/MCU_MISO 与 TC_CS/TC_SCK/TC_MISO 网络

### U4 MAX31855 SPI

U4 的 CS 引脚 6、SCK 引脚 5、MISO 引脚 7 分别连接 TC_CS、TC_SCK、TC_MISO；电路未使用 MOSI。

- 参数与网络：`converter=U4 MAX31855KASA+T`；`chip_select=CS/pin 6/TC_CS`；`clock=SCK/pin 5/TC_SCK`；`data_output=MISO/pin 7/TC_MISO`；`mosi=null`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C3 U4 左侧 TC_CS/TC_SCK/TC_MISO 与 CS/SCK/MISO 引脚

## GPIO 与控制信号

### U3 SEL

U3 SEL 引脚 10 通过 R6 10 kΩ 下拉至 GND_ISO。

- 参数与网络：`pin=SEL/pin 10`；`pulldown=R6 10k to GND_ISO`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U3 右下 SEL pin 10、R6 10K 与 GND_ISO

### TEMP_Read 与 LED1

U2 PB1 引脚 14 连接 TEMP_Read；TEMP_Read 驱动 LED1 red，并经 R1 10 kΩ 接 GND。

- 参数与网络：`mcu_pin=PB1/pin 14`；`network=TEMP_Read`；`indicator=LED1 red`；`series_resistor=R1 10k to GND`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C1-C2 U2 PB1/TEMP_Read 与 Temp LED 电路

### U2 BOOT0

U2 BOOT0 引脚 1 通过 R4 10 kΩ 下拉至 GND。

- 参数与网络：`mcu_pin=BOOT0/pin 1`；`pulldown=R4 10k to GND`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U2 右侧 BOOT0 pin 1、R4 10K 与 GND

## 时钟

### U2 外部时钟

U2 PF0-OSC_IN 引脚 2 与 PF1-OSC_OUT 引脚 3 在本页未连接外部晶振或时钟器件。

- 参数与网络：`osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U2 右上 PF0-OSC_IN/PF1-OSC_OUT 引脚短线无外接器件

## 复位

### U2 NRST

U2 NRST 引脚 4 连接 NRST；R5 10 kΩ 将其上拉至 VCC_3V3，C10 100 nF 将其连接至 GND，并引出到 J2。

- 参数与网络：`mcu_pin=NRST/pin 4`；`pullup=R5 10k to VCC_3V3`；`capacitor=C10 100nF to GND`；`debug_connector=J2`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C2-D2 U2 NRST、R5/C10 与 J2 NRST

## 传感器

### U4 热电偶输入

U4 的 T- 引脚 2 和 T+ 引脚 3 分别连接 TC1 的 T-、T+ 路径；U4 NC 引脚 8 未连接。

- 参数与网络：`negative_input=U4 T-/pin 2 -> TC1 T-`；`positive_input=U4 T+/pin 3 -> TC1 T+`；`unused_pin=U4 NC/pin 8`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C3-C4 U4 T-/T+ 与 TC1 对应端子路径

## 调试与烧录

### U2 与 J2 SWD

U2 PA13 引脚 19 的 MCU_SWDIO、PA14 引脚 20 的 MCU_SWCLK 连接 J2；J2 的 1 至 5 脚依次连接 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND。

- 参数与网络：`swdio=U2 PA13/pin 19`；`swclk=U2 PA14/pin 20`；`connector_pinout=J2 1:VCC_3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GND`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 U2 PA13/PA14 与网格 D2 J2 SWD_5P

## 模拟电路

### T+/T-/SH 输入滤波

TC1 的 T-、T+ 与 SH 路径各串联一只标注 330R/GZ1005D331TF 的磁珠；C9、C11、C14 均为 10 nF，构成热电偶差模/共模滤波网络。

- 参数与网络：`series_beads=three 330R/GZ1005D331TF beads on T-,T+,SH`；`filter_capacitors=C9 10nF,C11 10nF,C14 10nF`；`isolated_ground=GND_ISO`
- 证据：图 31dd2e5caffb / 第 1 页 / 页 1 网格 C3-C4 U4 至 TC1 三条路径上的磁珠和 C9/C11/C14

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit KMeter-ISO 采集架构 | `controller=U2 STM32F030F4P6`；`host_bus=I2C`；`isolator=U3 CA-IS3641HW`；`sensor_bus=3-wire read-only SPI`；`converter=U4 MAX31855KASA+T`；`thermocouple_connector=TC1 PCC-SMP-K-100-CE` |
| 接口 | GROVE I2C 接口 | `reference=GROVE`；`pinout=IO2:SCL,IO1:SDA,5V:VCC_5V,GND:GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | U2 与 GROVE 的 I2C | `controller=U2`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`scl_pullup=R2 10k to VCC_3V3`；`sda_pullup=R3 10k to VCC_3V3`；`connector=GROVE` |
| 总线地址 | Unit KMeter-ISO I2C 地址 | `documented_address=0x66`；`schematic_address=null`；`hardware_address_select=null` |
| 总线 | U2 MCU 侧 SPI | `chip_select=PA4/pin 10/MCU_CS`；`clock=PA5/pin 11/MCU_SCK`；`data_in=PA6/pin 12/MCU_MISO`；`mosi=null` |
| 总线 | U3 隔离 SPI 映射 | `cs_path=MCU_CS -> U3 VI1/pin 3 -> VO1/pin 14 -> TC_CS`；`sck_path=MCU_SCK -> U3 VI2/pin 4 -> VO2/pin 13 -> TC_SCK`；`miso_path=TC_MISO -> U3 VI4/pin 11 -> VO4/pin 6 -> MCU_MISO`；`unused_channel=VI3/pin 5 and VO3/pin 12 unconnected` |
| 总线 | U4 MAX31855 SPI | `converter=U4 MAX31855KASA+T`；`chip_select=CS/pin 6/TC_CS`；`clock=SCK/pin 5/TC_SCK`；`data_output=MISO/pin 7/TC_MISO`；`mosi=null` |
| 电源 | U1 MCU LDO | `reference=U1`；`part_number=MD5333`；`input=VIN/pin 3/VCC_5V`；`output=VOUT/pin 2/VCC_3V3`；`ground=GND/pin 1` |
| 电源 | U1 输入输出去耦 | `input_capacitors=C1 4.7uF,C2 100nF`；`output_capacitors=C3 4.7uF,C4 100nF` |
| 电源 | MCU 与热电偶隔离域 | `mcu_domain=VCC_5V,GND`；`isolated_domain=VCC_A3V3,GND_ISO`；`gnda_pins=2,8`；`gndb_pins=15,9`；`galvanic_ground_connection=false` |
| 电源 | U3 VISO 输出 | `source_pin=U3 VISO/pin 16`；`filter_bead=FB3 330R/GZ1005D331TF`；`output_rail=VCC_A3V3`；`bulk_capacitors=C6 22uF,C8 22uF`；`post_filter_capacitor=C16 100nF`；`return=GND_ISO` |
| GPIO 与控制信号 | U3 SEL | `pin=SEL/pin 10`；`pulldown=R6 10k to GND_ISO` |
| 电源 | U4 供电 | `supply=VCC/pin 4/VCC_A3V3`；`ground=GND/pin 1/GND_ISO`；`decoupling=C12 100nF,C13 10uF` |
| 传感器 | U4 热电偶输入 | `negative_input=U4 T-/pin 2 -> TC1 T-`；`positive_input=U4 T+/pin 3 -> TC1 T+`；`unused_pin=U4 NC/pin 8` |
| 接口 | TC1 K 型热电偶接口 | `reference=TC1`；`part_number=PCC-SMP-K-100-CE`；`terminals=T-,T+,SH`；`shield_return=GND_ISO via ferrite bead` |
| 模拟电路 | T+/T-/SH 输入滤波 | `series_beads=three 330R/GZ1005D331TF beads on T-,T+,SH`；`filter_capacitors=C9 10nF,C11 10nF,C14 10nF`；`isolated_ground=GND_ISO` |
| GPIO 与控制信号 | TEMP_Read 与 LED1 | `mcu_pin=PB1/pin 14`；`network=TEMP_Read`；`indicator=LED1 red`；`series_resistor=R1 10k to GND` |
| 电源 | U2 供电 | `supply_pins=VDD/pin 16,VDDA/pin 5`；`rail=VCC_3V3`；`ground_pin=VSS/pin 15`；`decoupling=C15 100nF` |
| 复位 | U2 NRST | `mcu_pin=NRST/pin 4`；`pullup=R5 10k to VCC_3V3`；`capacitor=C10 100nF to GND`；`debug_connector=J2` |
| GPIO 与控制信号 | U2 BOOT0 | `mcu_pin=BOOT0/pin 1`；`pulldown=R4 10k to GND` |
| 调试与烧录 | U2 与 J2 SWD | `swdio=U2 PA13/pin 19`；`swclk=U2 PA14/pin 20`；`connector_pinout=J2 1:VCC_3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GND` |
| 时钟 | U2 外部时钟 | `osc_in=PF0-OSC_IN/pin 2 unconnected`；`osc_out=PF1-OSC_OUT/pin 3 unconnected`；`external_crystal=false` |
| 传感器 | MAX31855 与热电偶性能 | `documented_resolution_bits=14`；`documented_resolution_c=0.25`；`documented_max_sample_rate_hz=10`；`documented_max_spi_hz=5000000`；`documented_range_c=-200 to 1350`；`documented_accuracy_c=2`；`schematic_performance=null` |
| 传感器 | 热电偶异常检测 | `documented_faults=open circuit,short circuit,thermocouple low voltage`；`schematic_fault_pin=null`；`schematic_thresholds=null` |

## 待确认事项

- `address.i2c`：产品正文标注 I2C 地址 0x66，但本页原理图没有地址值、地址选择引脚或拨码网络。（证据：图 31dd2e5caffb / 第 1 页 / 页 1 GROVE SCL/SDA 至 U2 的完整 I2C 链路未标注地址）
- `sensor.performance`：产品正文描述 14 位、0.25°C 分辨率、10 Hz 最大采样率、最高 5 MHz SPI、-200 至 1350°C 范围及 ±2°C 精度；这些性能参数未在本页原理图中标注。（证据：图 31dd2e5caffb / 第 1 页 / 页 1 U4 MAX31855KASA+T、SPI 与 TC1 电路未打印分辨率、速率、范围或精度）
- `sensor.fault_detection`：产品正文称支持开路、短路和热电偶低电压异常检测，但原理图未标注检测阈值或故障输出网络。（证据：图 31dd2e5caffb / 第 1 页 / 页 1 U4 与 TC1 之间只有 T+/T-、SPI 和电源连接，没有独立故障引脚或阈值标注）
- `review.i2c_address`：当前 STM32 固件的 7 位 I2C 地址是否为 0x66，是否可配置？；原因：原理图只有 I2C 物理连接，没有地址值或硬件地址选择网络。
- `review.sensor_performance`：14 位、0.25°C、10 Hz、5 MHz、-200 至 1350°C 与 ±2°C 参数分别适用于哪些转换和探头条件？；原因：原理图确认 MAX31855KASA+T 与 K 型接口，但未给出性能条件。
- `review.fault_detection`：开路、短路和低电压异常的检测定义、阈值与固件上报方式是什么？；原因：原理图没有故障阈值或独立故障网络，需查芯片和固件协议。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `31dd2e5caffbe002acca17887af7daae92ebeac9781721d4b9d52ed39980053c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/596/Sch_UNIT-KMeter_ISO_sch_01.png` |

---

源文档：`zh_CN/unit/KMeterISO Unit.md`

源文档 SHA-256：`77d192a6ff0ab5bf1001b979258caf138a2bb3e5efc9efa5de45368cd808708d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
