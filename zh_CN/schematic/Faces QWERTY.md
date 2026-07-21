# Faces QWERTY 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces QWERTY |
| SKU | A003 |
| 产品 ID | `faces-qwerty-59a1a6d60299` |
| 源文档 | `zh_CN/module/faces_keyboard.md` |

## 概述

Faces QWERTY 以 U1 ATmega328P-AU 扫描 30 键的 A-J/O1-O3 矩阵，并直接采集 S31-S35 五个功能键，共 35 键。PC4/SDA 与 PC5/SCL 接到 BUS1 面板总线，PB2 经 G5 与 10K 上拉接 BUS1 pin22；U1 由 3V3 供电，PC0 驱动方向相反的 LED1/LED2。原理图未打印 I2C 地址和固件行为，正文中的 0x08、按键复用、指示灯状态及 MCU 命名差异需要结合固件和 BOM 确认。

## 检索关键词

`Faces QWERTY`、`A003`、`FACE_BOTTOM`、`ATmega328P-AU`、`MEGA328`、`MEGA838P`、`QWERTY keyboard`、`35 keys`、`I2C`、`0x08`、`SDA`、`SCL`、`G5`、`INT`、`M5_BUS`、`Faces Panel Bus`、`O1`、`O2`、`O3`、`A-J`、`SPACE`、`BACK SPACE`、`ENTER`、`sym`、`alt`、`aA`、`LED1`、`LED2`、`RESET`、`Header 6`、`ISP`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ATmega328P-AU | 扫描按键矩阵和功能键、驱动状态 LED，并通过 I2C 接入面板总线 | 图 242fa73ce807 / 第 1 页 / 左下 U1，器件标注 ATmega328P-AU，pins1-32 |
| BUS1 | M5_BUS | 22 针 Faces 面板接口，提供 3V3、GND、SDA、SCL、G5/INT 等信号 | 图 242fa73ce807 / 第 1 页 / 左上 BUS1 M5_BUS pins1-22，SDA/SCL/G5 外引 |
| P1 | Header 6 | 连接 GND、U1 PB3/PB4/PB5 和 RESET 的六针接口 | 图 242fa73ce807 / 第 1 页 / 下中 P1 Header 6 pins1-6 与 GND/PB3/PB4/PB5/RESET |
| S1/S4/S7/S10/S13/S16/S19/S22/S25/S28 | 未标注 | O1 列的十个主键，覆盖 SPACE、$、M、N、B、V、C、X、Z、0 | 图 242fa73ce807 / 第 1 页 / 右侧 O1 竖列，A-J 十行按键 |
| S2/S5/S8/S11/S14/S17/S20/S23/S26/S29 | 未标注 | O2 列的十个主键，覆盖 BACK SPACE、L、K、J、H、G、F、D、S、A | 图 242fa73ce807 / 第 1 页 / 右侧 O2 竖列，A-J 十行按键 |
| S3/S6/S9/S12/S15/S18/S21/S24/S27/S30 | 未标注 | O3 列的十个主键，覆盖 P、O、I、U、Y、T、R、E、W、Q | 图 242fa73ce807 / 第 1 页 / 右侧 O3 竖列，A-J 十行按键 |
| S31-S35 | 未标注 | 五个 MCU 直连功能键，其中 S32/S33/S34/S35 标为 alt/aA/ENTER/sym，S31 未标键名 | 图 242fa73ce807 / 第 1 页 / 下部 S31-S35，分别连接 PB3-PB7 与 GND |
| LED1/LED2,R1/R2 | LED / 10KΩ | 由 U1 PC0 驱动的两路反向状态指示支路 | 图 242fa73ce807 / 第 1 页 / U1 PC0/pin23 右侧 R1 10K/LED1/GND 与 LED2/R2 10K/3V3 |
| R3 | 10KΩ | 将 U1 PB2/G5 网络上拉到 3V3 | 图 242fa73ce807 / 第 1 页 / U1 PB2/pin14 的 G5 节点与 R3 10K 到 3V3 |

## 系统结构

### Faces QWERTY 硬件架构

U1 ATmega328P-AU 扫描由 O1/O2/O3 与 A-J 构成的 30 键矩阵，并直接采集 S31-S35 五个功能键；U1 通过 SDA/SCL 接入 BUS1，同时以 PC0 驱动 LED1/LED2。

- 参数与网络：`controller=U1 ATmega328P-AU`；`matrix=3 columns x 10 rows`；`matrix_keys=30`；`direct_keys=5`；`total_keys=35`；`host_bus=I2C SDA/SCL`；`indicators=LED1; LED2`
- 证据：图 242fa73ce807 / 第 1 页 / 整页：U1、BUS1、S1-S35、LED1/LED2

## 核心器件

### U1 微控制器

主控制器位号为 U1，原理图器件值明确标为 ATmega328P-AU。

- 参数与网络：`reference=U1`；`part_number=ATmega328P-AU`；`package_suffix=AU`；`pin_count=32`
- 证据：图 242fa73ce807 / 第 1 页 / U1 符号底部 ATmega328P-AU 标注

## 电源

### U1 3V3 供电

U1 pins4/6 VCC 与 pin18 AVCC 接 3V3，pins3/5/21 GND 接地；pin20 AREF 在本页无外部连接。

- 参数与网络：`vcc_pins=4; 6`；`avcc_pin=18`；`supply=3V3`；`ground_pins=3; 5; 21`；`aref_pin=20 no external connection`
- 证据：图 242fa73ce807 / 第 1 页 / U1 左侧 VCC/AVCC/AREF 与底部 GND 引脚

### BUS1 电源

BUS1 pin1 标为 GND、pin2 标为 5V、pin4 标为 3V3；U1 使用 3V3 电源，页面未显示 5V 到 U1 或其他负载的连接，也未绘制本地稳压器。

- 参数与网络：`bus_ground=BUS1 pin1 GND`；`bus_5v=BUS1 pin2 5V`；`bus_3v3=BUS1 pin4 3V3`；`u1_supply=3V3`；`local_regulator_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / BUS1 pins1/2/4 与 U1 3V3/GND 电源网络

## 接口

### Faces 面板总线已用信号

该页使用 BUS1 的 GND、3V3、SDA/pin16、SCL/pin18 与 G5/pin22；BUS1 符号还列出 5V、AD35、AD36、DA25、DA26、SK、WS、OUT、MK、IN、HPR、MOSI、MISO、SCK、R2/16、T2/17、G2，但未显示这些信号连接到 U1 外围。

- 参数与网络：`used_signals=GND; 3V3; SDA/pin16; SCL/pin18; G5/pin22`；`other_bus_labels=5V; AD35; AD36; DA25; DA26; SK; WS; OUT; MK; IN; HPR; MOSI; MISO; SCK; R2/16; T2/17; G2`
- 证据：图 242fa73ce807 / 第 1 页 / BUS1 M5_BUS pins1-22 与 U1 连接网络

### 3×10 主键盘矩阵

S1-S30 构成 O1/O2/O3 三列与 A-J 十行的 3×10 矩阵，共 30 个按键；页面未绘制逐键二极管。

- 参数与网络：`columns=3`；`rows=10`；`matrix_keys=30`；`column_nets=O1; O2; O3`；`row_nets=A; B; C; D; E; F; G; H; I; J`；`per_key_diodes_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / 右侧 S1-S30 三列十行矩阵

### O1 列按键

O1 列从 A 到 J 依次为 S1 SPACE、S4 $、S7 M、S10 N、S13 B、S16 V、S19 C、S22 X、S25 Z、S28 0。

- 参数与网络：`A=S1 SPACE`；`B=S4 $`；`C=S7 M`；`D=S10 N`；`E=S13 B`；`F=S16 V`；`G=S19 C`；`H=S22 X`；`I=S25 Z`；`J=S28 0`
- 证据：图 242fa73ce807 / 第 1 页 / 右侧 O1 竖列 S1/S4/S7/S10/S13/S16/S19/S22/S25/S28 与 A-J

### O2 列按键

O2 列从 A 到 J 依次为 S2 BACK SPACE、S5 L、S8 K、S11 J、S14 H、S17 G、S20 F、S23 D、S26 S、S29 A。

- 参数与网络：`A=S2 BACK SPACE`；`B=S5 L`；`C=S8 K`；`D=S11 J`；`E=S14 H`；`F=S17 G`；`G=S20 F`；`H=S23 D`；`I=S26 S`；`J=S29 A`
- 证据：图 242fa73ce807 / 第 1 页 / 右侧 O2 竖列 S2/S5/S8/S11/S14/S17/S20/S23/S26/S29 与 A-J

### O3 列按键

O3 列从 A 到 J 依次为 S3 P、S6 O、S9 I、S12 U、S15 Y、S18 T、S21 R、S24 E、S27 W、S30 Q。

- 参数与网络：`A=S3 P`；`B=S6 O`；`C=S9 I`；`D=S12 U`；`E=S15 Y`；`F=S18 T`；`G=S21 R`；`H=S24 E`；`I=S27 W`；`J=S30 Q`
- 证据：图 242fa73ce807 / 第 1 页 / 右侧 O3 竖列 S3/S6/S9/S12/S15/S18/S21/S24/S27/S30 与 A-J

### S31-S35 直连功能键

S31 将 U1 pin15/PB3 接地且键名未标；S32 将 pin16/PB4 接地并标 alt；S33 将 pin17/PB5 接地并标 aA；S34 将 pin7/PB6 接地并标 ENTER；S35 将 pin8/PB7 接地并标 sym。

- 参数与网络：`S31=PB3/pin15 -> GND; unlabeled`；`S32=PB4/pin16 -> GND; alt`；`S33=PB5/pin17 -> GND; aA`；`S34=PB6/pin7 -> GND; ENTER`；`S35=PB7/pin8 -> GND; sym`
- 证据：图 242fa73ce807 / 第 1 页 / 下部 U1 PB3-PB7 与 S31-S35/GND

## 总线

### U1 到 BUS1 的 I2C

U1 pin27 PC4/SDA 通过 SDA 网络连接 BUS1 pin16，U1 pin28 PC5/SCL 通过 SCL 网络连接 BUS1 pin18；本页未绘制 SDA/SCL 上拉电阻。

- 参数与网络：`sda=U1 pin27 PC4 -> BUS1 pin16`；`scl=U1 pin28 PC5 -> BUS1 pin18`；`local_pullups_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PC4/PC5 的 SDA/SCL 标签与 BUS1 pins16/18

## GPIO 与控制信号

### G5 网络与上拉

U1 pin14 PB2 连接 G5，G5 同时连接 BUS1 pin22，并由 R3 10KΩ 上拉到 3V3。

- 参数与网络：`mcu_pin=U1 pin14 PB2`；`net=G5`；`bus_pin=BUS1 pin22`；`pullup=R3 10KΩ to 3V3`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PB2/pin14、G5、R3 10K/3V3 与 BUS1 pin22

### 按键矩阵 O1/O2/O3 映射

U1 pin24 PC1 连接 O1，pin25 PC2 连接 O3，pin26 PC3 连接 O2；U1 pin23 PC0 不属于按键矩阵列，而是连接 LED1/LED2。

- 参数与网络：`O1=U1 pin24 PC1`；`O2=U1 pin26 PC3`；`O3=U1 pin25 PC2`；`PC0=U1 pin23 LED driver node`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PC0-PC3 pins23-26 与 LED/O1/O3/O2 网络

### 按键矩阵 A-J 映射

矩阵行线映射为 A=U1 pin30/PD0、B=pin31/PD1、C=pin32/PD2、D=pin1/PD3、E=pin2/PD4、F=pin11/PD7、G=pin10/PD6、H=pin9/PD5、I=pin12/PB0、J=pin13/PB1。

- 参数与网络：`A=pin30 PD0`；`B=pin31 PD1`；`C=pin32 PD2`；`D=pin1 PD3`；`E=pin2 PD4`；`F=pin11 PD7`；`G=pin10 PD6`；`H=pin9 PD5`；`I=pin12 PB0`；`J=pin13 PB1`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PD0-PD7/PB0/PB1 与 A-J 网络标签

### LED1/LED2 指示电路

U1 pin23/PC0 同时连接两条方向相反的 LED 支路：一条经 R1 10KΩ、LED1 到 GND，另一条经 LED2、R2 10KΩ 到 3V3。

- 参数与网络：`driver_pin=U1 pin23 PC0`；`branch_1=PC0 -> R1 10KΩ -> LED1 -> GND`；`branch_2=PC0 -> LED2 -> R2 10KΩ -> 3V3`；`orientation=opposite`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PC0/pin23 与 R1/LED1/GND、LED2/R2/3V3

## 时钟

### U1 时钟源可见性

U1 pin7/PB6(XTAL1) 与 pin8/PB7(XTAL2) 分别用于 S34 ENTER 和 S35 sym，页面未绘制外部晶体、谐振器或振荡器，也未标注 MCU 工作频率。

- 参数与网络：`xtal1_pin_usage=pin7 PB6 -> S34 ENTER`；`xtal2_pin_usage=pin8 PB7 -> S35 sym`；`external_clock_visible=false`；`frequency_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / U1 PB6/PB7 pins7/8 到 S34/S35；整页无晶体或振荡器

## 复位

### U1 RESET

U1 pin29 PC6/RESET 连接 RESET 网络并到 P1 pin5；页面未显示 RESET 外部上拉电阻、复位按钮或复位电容。

- 参数与网络：`mcu_pin=U1 pin29 PC6/RESET`；`header_pin=P1 pin5`；`external_pullup_visible=false`；`reset_switch_visible=false`；`reset_capacitor_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / U1 pin29 RESET 与 P1 pin5；整页无复位外围

## 内存与 Flash

### 外部存储器可见性

页面未显示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器件与存储总线。

- 参数与网络：`external_flash_visible=false`；`external_eeprom_visible=false`；`external_ram_visible=false`；`sd_interface_visible=false`
- 证据：图 242fa73ce807 / 第 1 页 / 完整原理图器件范围，无独立存储器或存储连接器

## 调试与烧录

### P1 Header 6 逐针连接

P1 pin1 接 GND，pin2 接 U1 pin15/PB3，pin3 接 U1 pin16/PB4，pin4 接 U1 pin17/PB5，pin5 接 RESET，pin6 在本页无外部网络连接。

- 参数与网络：`pin1=GND`；`pin2=U1 pin15 PB3`；`pin3=U1 pin16 PB4`；`pin4=U1 pin17 PB5`；`pin5=RESET`；`pin6=no external connection shown`
- 证据：图 242fa73ce807 / 第 1 页 / 下中 P1 Header 6 pins1-6 与 GND/PB3/PB4/PB5/RESET

## 模拟电路

### 未使用模拟引脚

U1 pin19 ADC6 与 pin22 ADC7 标为未连接，pin20 AREF 也未显示外部连接；PC0-PC5 的复用模拟引脚在本页用于 LED、矩阵与 I2C。

- 参数与网络：`ADC6=pin19 NC`；`ADC7=pin22 NC`；`AREF=pin20 no external connection`；`PC0_PC5_usage=LED; matrix; I2C`
- 证据：图 242fa73ce807 / 第 1 页 / U1 ADC6/ADC7/AREF 与 PC0-PC5 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces QWERTY 硬件架构 | `controller=U1 ATmega328P-AU`；`matrix=3 columns x 10 rows`；`matrix_keys=30`；`direct_keys=5`；`total_keys=35`；`host_bus=I2C SDA/SCL`；`indicators=LED1; LED2` |
| 核心器件 | U1 微控制器 | `reference=U1`；`part_number=ATmega328P-AU`；`package_suffix=AU`；`pin_count=32` |
| 电源 | U1 3V3 供电 | `vcc_pins=4; 6`；`avcc_pin=18`；`supply=3V3`；`ground_pins=3; 5; 21`；`aref_pin=20 no external connection` |
| 电源 | BUS1 电源 | `bus_ground=BUS1 pin1 GND`；`bus_5v=BUS1 pin2 5V`；`bus_3v3=BUS1 pin4 3V3`；`u1_supply=3V3`；`local_regulator_visible=false` |
| 总线 | U1 到 BUS1 的 I2C | `sda=U1 pin27 PC4 -> BUS1 pin16`；`scl=U1 pin28 PC5 -> BUS1 pin18`；`local_pullups_visible=false` |
| GPIO 与控制信号 | G5 网络与上拉 | `mcu_pin=U1 pin14 PB2`；`net=G5`；`bus_pin=BUS1 pin22`；`pullup=R3 10KΩ to 3V3` |
| 接口 | Faces 面板总线已用信号 | `used_signals=GND; 3V3; SDA/pin16; SCL/pin18; G5/pin22`；`other_bus_labels=5V; AD35; AD36; DA25; DA26; SK; WS; OUT; MK; IN; HPR; MOSI; MISO; SCK; R2/16; T2/17; G2` |
| GPIO 与控制信号 | 按键矩阵 O1/O2/O3 映射 | `O1=U1 pin24 PC1`；`O2=U1 pin26 PC3`；`O3=U1 pin25 PC2`；`PC0=U1 pin23 LED driver node` |
| GPIO 与控制信号 | 按键矩阵 A-J 映射 | `A=pin30 PD0`；`B=pin31 PD1`；`C=pin32 PD2`；`D=pin1 PD3`；`E=pin2 PD4`；`F=pin11 PD7`；`G=pin10 PD6`；`H=pin9 PD5`；`I=pin12 PB0`；`J=pin13 PB1` |
| 接口 | 3×10 主键盘矩阵 | `columns=3`；`rows=10`；`matrix_keys=30`；`column_nets=O1; O2; O3`；`row_nets=A; B; C; D; E; F; G; H; I; J`；`per_key_diodes_visible=false` |
| 接口 | O1 列按键 | `A=S1 SPACE`；`B=S4 $`；`C=S7 M`；`D=S10 N`；`E=S13 B`；`F=S16 V`；`G=S19 C`；`H=S22 X`；`I=S25 Z`；`J=S28 0` |
| 接口 | O2 列按键 | `A=S2 BACK SPACE`；`B=S5 L`；`C=S8 K`；`D=S11 J`；`E=S14 H`；`F=S17 G`；`G=S20 F`；`H=S23 D`；`I=S26 S`；`J=S29 A` |
| 接口 | O3 列按键 | `A=S3 P`；`B=S6 O`；`C=S9 I`；`D=S12 U`；`E=S15 Y`；`F=S18 T`；`G=S21 R`；`H=S24 E`；`I=S27 W`；`J=S30 Q` |
| 接口 | S31-S35 直连功能键 | `S31=PB3/pin15 -> GND; unlabeled`；`S32=PB4/pin16 -> GND; alt`；`S33=PB5/pin17 -> GND; aA`；`S34=PB6/pin7 -> GND; ENTER`；`S35=PB7/pin8 -> GND; sym` |
| 调试与烧录 | P1 Header 6 逐针连接 | `pin1=GND`；`pin2=U1 pin15 PB3`；`pin3=U1 pin16 PB4`；`pin4=U1 pin17 PB5`；`pin5=RESET`；`pin6=no external connection shown` |
| GPIO 与控制信号 | LED1/LED2 指示电路 | `driver_pin=U1 pin23 PC0`；`branch_1=PC0 -> R1 10KΩ -> LED1 -> GND`；`branch_2=PC0 -> LED2 -> R2 10KΩ -> 3V3`；`orientation=opposite` |
| 复位 | U1 RESET | `mcu_pin=U1 pin29 PC6/RESET`；`header_pin=P1 pin5`；`external_pullup_visible=false`；`reset_switch_visible=false`；`reset_capacitor_visible=false` |
| 时钟 | U1 时钟源可见性 | `xtal1_pin_usage=pin7 PB6 -> S34 ENTER`；`xtal2_pin_usage=pin8 PB7 -> S35 sym`；`external_clock_visible=false`；`frequency_visible=false` |
| 模拟电路 | 未使用模拟引脚 | `ADC6=pin19 NC`；`ADC7=pin22 NC`；`AREF=pin20 no external connection`；`PC0_PC5_usage=LED; matrix; I2C` |
| 内存与 Flash | 外部存储器可见性 | `external_flash_visible=false`；`external_eeprom_visible=false`；`external_ram_visible=false`；`sd_interface_visible=false` |
| 总线地址 | I2C 从机地址 | `documented_address_7bit=0x08`；`address_printed_on_schematic=false`；`address_straps_visible=false` |
| 核心器件 | MCU 型号命名冲突 | `schematic_part_number=ATmega328P-AU`；`description_name=MEGA328`；`spec_table_name=MEGA838P` |
| 接口 | BUS1 pin22 的 INT 语义 | `documented_name=INT`；`schematic_name=G5`；`mcu_pin=U1 pin14 PB2`；`pullup=R3 10KΩ to 3V3`；`direction=null`；`active_level=null` |
| 接口 | 功能键标签与单击/双击行为 | `documented_shift_keys=sym; Fn`；`schematic_labels=S31 unlabeled; S32 alt; S33 aA; S34 ENTER; S35 sym`；`single_click_behavior=documented single-character mode`；`double_click_behavior=documented continuous mode`；`firmware_state_machine_visible=false` |
| GPIO 与控制信号 | 蓝色输入状态 LED | `documented_color=blue`；`documented_count=2`；`schematic_references=LED1; LED2`；`color_printed_on_schematic=false`；`firmware_behavior_visible=false` |
| 调试与烧录 | P1 ISP 下载接口角色 | `documented_role=Mega328 ISP download interface`；`schematic_label=P1 Header 6`；`isp_text_on_schematic=false`；`orientation_visible=false` |
| 保护电路 | 保护、去耦与按键滤波 | `decoupling_visible=false`；`i2c_esd_visible=false`；`int_esd_visible=false`；`key_debounce_visible=false`；`power_protection_visible=false` |
| 系统结构 | FACE_BOTTOM 兼容性 | `documented_host=FACE_BOTTOM`；`schematic_connector=BUS1 M5_BUS`；`mechanical_stack_visible=false`；`host_revision_visible=false` |
| 其他事实 | 外壳、尺寸与重量 | `documented_material=Plastic (PC)`；`documented_product_size=58.2 x 54.2 x 10.4mm`；`documented_product_weight=21.0g`；`documented_package_size=95.0 x 65.0 x 25.0mm`；`documented_gross_weight=41.0g` |

## 待确认事项

- `address.documented-i2c-0x08`：产品正文给出 I2C 从机地址 0x08，但原理图只显示 SDA/SCL 连线，没有 0x08 文本、地址跳线或地址电阻。（证据：图 242fa73ce807 / 第 1 页 / U1 PC4/PC5 与 BUS1 SDA/SCL，页面无地址配置）
- `component.documented-mcu-naming`：原理图明确标注 ATmega328P-AU，产品描述写 MEGA328，规格表写 MEGA838P；后两种文档写法与原理图完整料号不一致。（证据：图 242fa73ce807 / 第 1 页 / U1 符号底部只标 ATmega328P-AU）
- `interface.documented-int-semantics`：产品管脚表把 pin22 称为 INT，而原理图将 BUS1 pin22 与 U1 PB2 网络标为 G5 并通过 R3 上拉；中断方向、有效电平与触发条件未在原理图中说明。（证据：图 242fa73ce807 / 第 1 页 / BUS1 pin22 G5、U1 PB2/G5 与 R3；页面无 INT 极性文本）
- `interface.documented-function-behavior`：产品正文称 sym 与 Fn 用于上档、aA 用于大小写，并描述单击/双击的单字符与连续输入行为；原理图只确认 S31 未标名、S32 标 alt、S33 标 aA、S34 标 ENTER、S35 标 sym 的电气连接，未包含 Fn 标签或按键状态机。（证据：图 242fa73ce807 / 第 1 页 / S31-S35 标签与直连 U1/GND 电路，无 Fn 或状态机文本）
- `gpio.documented-indicators`：规格表称有两只蓝色输入状态 LED，正文描述常亮与闪烁模式；原理图确认 LED1/LED2 及 PC0 驱动电路，但未标颜色、亮灭逻辑、闪烁周期或模式含义。（证据：图 242fa73ce807 / 第 1 页 / PC0、R1/R2 与 LED1/LED2，仅标 LED 无颜色或状态含义）
- `debug.documented-isp-role`：产品正文将相关接口描述为 Mega328 ISP 下载接口，但当前原理图只把 P1 标为 Header 6 并显示 GND、PB3、PB4、PB5、RESET 与一个未连接针脚，没有 ISP 名称、观察方向或标准针序标注。（证据：图 242fa73ce807 / 第 1 页 / P1 Header 6 pins1-6 与 U1 PB3/PB4/PB5/RESET/GND）
- `protection.filtering-visibility`：当前页未绘制 VCC/AVCC 去耦电容、I2C/INT ESD 器件、按键去抖器件或电源过流/反接保护，无法由该页判断量产板是否另有未展示器件。（证据：图 242fa73ce807 / 第 1 页 / 完整原理图器件范围，无电容、ESD、去抖或电源保护器件）
- `system.documented-face-bottom-compatibility`：产品正文称 Faces QWERTY 适配 FACE_BOTTOM；原理图只显示 BUS1 M5_BUS 的电气接口，没有 FACE_BOTTOM 型号、机械堆叠、版本边界或完整互连说明。（证据：图 242fa73ce807 / 第 1 页 / BUS1 M5_BUS 与整页电路，无 FACE_BOTTOM 型号或机械信息）
- `other.documented-mechanics`：产品正文列出 PC 塑料外壳、58.2 x 54.2 x 10.4mm、21.0g、包装 95.0 x 65.0 x 25.0mm 和毛重 41.0g；当前电气原理图未包含材料、尺寸或重量信息。（证据：图 242fa73ce807 / 第 1 页 / 电气原理图整页未标材料、机械尺寸或重量）
- `review.i2c-address`：请通过 A003 当前固件或协议资料确认 I2C 7-bit 从机地址是否固定为 0x08，以及是否可配置。；原因：地址属于固件行为，原理图只有 SDA/SCL 连线，没有地址标注或硬件配置。
- `review.mcu-naming`：请用 A003 量产 BOM 确认 MCU 正式料号，并修正文档中的 MEGA328/MEGA838P 命名差异。；原因：原理图明确为 ATmega328P-AU，描述和规格表使用两个不同名称。
- `review.int-semantics`：BUS1 pin22 的 G5 是否由固件作为 INT 使用，其方向、有效电平和触发条件是什么？；原因：原理图只确认 PB2-G5-BUS1 pin22 与 10K 上拉，INT 名称来自产品管脚表。
- `review.function-key-behavior`：请用键帽图和 A003 固件确认 S31/S32 对应 Fn/alt 的实际标签，以及 sym/Fn/aA 单击、双击和连续输入状态机。；原因：原理图 S31 未标名、S32 标 alt，与正文 Fn 描述不能直接对应，且状态机未在硬件图中表示。
- `review.indicators`：请用 BOM、键盘面板照片和固件确认 LED1/LED2 的蓝色规格、亮灭极性、闪烁周期及状态含义。；原因：原理图只给出两条反向 LED 支路，没有颜色或固件行为。
- `review.isp-role`：请用 ISP 针脚定义图或 PCB 丝印确认 P1 的观察方向、逐针定义及是否为量产 Mega328 ISP 下载接口。；原因：当前主原理图仅标 P1 Header 6，没有 ISP 名称或方向。
- `review.protection-filtering`：请确认 A003 量产板是否包含本页未展示的 MCU 去耦、I2C/INT ESD、按键去抖或电源保护器件。；原因：当前单页没有这些器件，无法区分设计省略与实际不存在。
- `review.face-bottom-compatibility`：请用 FACE_BOTTOM 与 A003 的版本化接口/机械图确认电气、机械和版本兼容范围。；原因：原理图只显示通用 BUS1 M5_BUS，不含 FACE_BOTTOM 版本和机械堆叠信息。
- `review.mechanics`：请用正式尺寸图、材料规范、称重记录和包装规范复核 A003 的外壳、尺寸与重量。；原因：当前证据为电气原理图，不包含材料或机械规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `242fa73ce807a3f7e0f7920b3af8fe9ba427b36f03c6370666ca57375ce21fe8` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_sch_01.webp` |

---

源文档：`zh_CN/module/faces_keyboard.md`

源文档 SHA-256：`e5b8dc72e810081eaede2acce7d613a4716e7623f12c92f358b03d8b635ab725`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
