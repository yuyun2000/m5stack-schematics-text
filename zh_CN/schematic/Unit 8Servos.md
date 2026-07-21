# Unit 8Servos 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 8Servos |
| SKU | U165 |
| 产品 ID | `unit-8servos-206387ff33ed` |
| 源文档 | `zh_CN/unit/8Servos Unit.md` |

## 概述

Unit 8Servos 以 U3 STM32F030F4P6 产生 IO0~IO7 八路舵机控制信号，通过 Grove I2C 与主机通信，P1~P4 每个连接两路信号及公共 VM/GND。HPWR 经 U1 SY8303AIC 降压为 VCC_5V，Grove BUS_5V 还通过 Q1/Q3 AO3401A 电源路径与 VCC_5V 侧关联；VCC_5V 经 F1 12V/3A 和 R5 10mΩ 形成舵机电源 VM。U4 INA199A1DCKR 跨 R5 测量总电流并输出 ADC_OUT 到 U3 PB1，U2 HX6306P332MR 从 BUS_5V 生成 3V3。正文给出的 0x25、PWM/舵机协议、9-24V 与 5V@3A 系统额定及电源切换优先级需结合固件、器件资料和测试确认。

## 检索关键词

`Unit 8Servos`、`U165`、`STM32F030F4P6`、`INA199A1DCKR`、`SY8303AIC`、`HX6306P332MR`、`AO3401A`、`TL432`、`I2C`、`0x25`、`IO0`、`IO1`、`IO2`、`IO3`、`IO4`、`IO5`、`IO6`、`IO7`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA5`、`PA6`、`PA7`、`ADC_OUT`、`PB1`、`R5 10mR/1206`、`VM`、`VCC_5V`、`BUS_5V`、`HPWR`、`3V3`、`HT3.96 4P`、`Grove`、`PWM`、`servo`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 舵机控制 MCU，输出八路 IO 并采集 ADC_OUT | 图 85031f66807e / 第 1 页 / 第 1 页 C1-D2 U3 STM32F030F4P6 |
| U4 | INA199A1DCKR | 跨 R5 采集舵机总电流并输出 ADC_OUT | 图 85031f66807e / 第 1 页 / 第 1 页 C3-D3 U4 INA199A1DCKR |
| U1 | SY8303AIC | HPWR 到 VCC_5V 的降压转换器 | 图 85031f66807e / 第 1 页 / 第 1 页 A1-A2 U1 SY8303AIC |
| U2 | HX6306P332MR | BUS_5V 到 3V3 的稳压器 | 图 85031f66807e / 第 1 页 / 第 1 页 B1-B2 U2 |
| Q1/Q3 | AO3401A | BUS_5V 与 VCC_5V 之间受 HPWR 检测网络控制的背靠背 MOS 电源路径 | 图 85031f66807e / 第 1 页 / 第 1 页 B3 Q1/Q3 AO3401A |
| U5 | TL432 | VCC_5V/电流监测辅助参考或钳位网络器件 | 图 85031f66807e / 第 1 页 / 第 1 页 D3 U5 TL432 |
| P1/P2/P3/P4 | Header 3X2H | 八路舵机信号、VM 和 GND 输出端子，每个连接两路舵机 | 图 85031f66807e / 第 1 页 / 第 1 页 C4-D4 P1-P4 |
| P5 | HT3.96 4P | HPWR、GND、VCC_5V 外部电源端子 | 图 85031f66807e / 第 1 页 / 第 1 页 A1 P5 |
| J1 | GROVE 4P | SCL、SDA、BUS_5V、GND I2C/电源接口 | 图 85031f66807e / 第 1 页 / 第 1 页 B1-C1 J1 GROVE |
| J2 | SWD_5P | 3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND 调试接口 | 图 85031f66807e / 第 1 页 / 第 1 页 D2 J2 SWD_5P |
| F1/R5 | 12V/3A / 10mR/1206 | VCC_5V 到 VM 的串联保险与总电流分流电阻 | 图 85031f66807e / 第 1 页 / 第 1 页 C3 F1/R5 |
| D1/D2/D3 | SMF30CA / TVS 5V / TVS 5V | HPWR 输入及 VCC_5V 输出的瞬态保护器件 | 图 85031f66807e / 第 1 页 / 第 1 页 A1-A2 D1/D2/D3 |

## 系统结构

### Unit 8Servos

U3 通过 I2C 接收主机命令并输出 IO0~IO7，P1~P4 提供八路舵机接口；U1/U2/Q1/Q3 管理电源，U4/R5 监测总电流。

- 参数与网络：`mcu=U3 STM32F030F4P6`；`channels=IO0-IO7`；`connectors=P1-P4`；`current_monitor=U4 INA199A1DCKR,R5`；`power=U1,U2,Q1,Q3`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页完整功能分区

## 电源

### U1 SY8303AIC

P5.4 HPWR 经 D2 图示 TVS 5V 网络进入 U1，D1 SMF30CA 对地保护；U1 配合 L1 6.8uH 生成 VCC_5V，D3 TVS 5V 跨接输出。

- 参数与网络：`input=P5.4 HPWR`；`input_protection=D1 SMF30CA,D2 TVS 5V`；`converter=U1 SY8303AIC`；`inductor=L1 6.8uH`；`output=VCC_5V`；`output_protection=D3 TVS 5V`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 A1-A2 DCDC

### U2 HX6306P332MR

U2 VIN 接 BUS_5V、VOUT 输出 3V3、GND 接地，C5 100nF 为输入去耦并配置图示输出电容。

- 参数与网络：`input=BUS_5V`；`output=3V3`；`input_cap=C5 100nF`；`regulator=HX6306P332MR`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 B1-B2 U2

### VCC_5V 到 VM

VCC_5V 经 F1 12V/3A 和 R5 10mR/1206 串联形成 VM，VM 连接 P1~P4 舵机电源针和多颗去耦电容。

- 参数与网络：`source=VCC_5V`；`fuse=F1 12V/3A`；`shunt=R5 10mR/1206`；`output=VM`；`loads=P1-P4`；`decoupling=C11-C15 shown on VM`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 C3-D4 F1/R5/VM/P1-P4

## 接口

### P1~P4 Header 3X2H

P1:1=IO0,2=IO1,3/4=VM,5/6=GND；P2 对应 IO2/IO3，P3 对应 IO4/IO5，P4 对应 IO6/IO7，其余 VM/GND 针序相同。

- 参数与网络：`P1=1 IO0,2 IO1,3/4 VM,5/6 GND`；`P2=1 IO2,2 IO3,3/4 VM,5/6 GND`；`P3=1 IO4,2 IO5,3/4 VM,5/6 GND`；`P4=1 IO6,2 IO7,3/4 VM,5/6 GND`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 C4-D4 P1-P4

### J1 GROVE 4P

J1 针脚为 SCL、SDA、BUS_5V、GND，BUS_5V 同时为 U2 3.3V 稳压器和电源选择电路提供输入。

- 参数与网络：`signals=SCL,SDA`；`power=BUS_5V`；`ground=GND`；`downstream=U2,Q1/Q3`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 B1-B3 J1/BUS_5V

### P5 HT3.96 4P

P5.4=HPWR、P5.3=GND、P5.1=VCC_5V，P5.2 未连接；端子支持高压降压输入或直接 5V 电源网接入。

- 参数与网络：`pin_4=HPWR`；`pin_3=GND`；`pin_2=NC`；`pin_1=VCC_5V`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 A1 P5

## 总线

### U3 I2C

J1 SCL/SDA 分别连接 U3 PA9/PA10，R2/R3 各 4.7K 上拉到 3V3。

- 参数与网络：`scl=J1 SCL -> U3 PA9`；`sda=J1 SDA -> U3 PA10`；`pullups=R2/R3 4.7K`；`rail=3V3`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 B1-C2 J1/R2/R3/U3

## GPIO 与控制信号

### IO0~IO7 舵机信号

U3 PA0/PA1/PA2/PA3/PA4/PA5/PA6/PA7 分别直接连接 IO0/IO1/IO2/IO3/IO4/IO5/IO6/IO7。

- 参数与网络：`IO0=U3 PA0`；`IO1=U3 PA1`；`IO2=U3 PA2`；`IO3=U3 PA3`；`IO4=U3 PA4`；`IO5=U3 PA5`；`IO6=U3 PA6`；`IO7=U3 PA7`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 C1-D2 U3 PA0-PA7

## 时钟

### U3 时钟

U3 PF0/PF1 未连接，完整页面未显示外部晶振或振荡器。

- 参数与网络：`PF0=NC`；`PF1=NC`；`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 U3 PF0/PF1

## 保护电路

### 电源保护

HPWR 侧有 D1 SMF30CA 和 D2，VCC_5V 输出有 D3 TVS 5V，VM 前串 F1 12V/3A；P1~P4 信号线上未画 TVS/ESD 或串联保护。

- 参数与网络：`hpwr_tvs=D1 SMF30CA,D2`；`vcc5_tvs=D3 TVS 5V`；`vm_fuse=F1 12V/3A`；`servo_signal_tvs_shown=false`；`servo_signal_series_shown=false`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 A1-A2 电源保护与 C4-D4 舵机接口

## 内存与 Flash

### 外部存储器

完整原理图未展示 U3 之外的 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页完整图无外部存储器

## 调试与烧录

### U3 BOOT/NRST/SWD

U3 BOOT0 经 R7 10K 下拉 GND，NRST 由 R6 10K 上拉 3V3并配 100nF 对地；J2.1~5 为 3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND。

- 参数与网络：`boot0=R7 10K to GND`；`reset=R6 10K to 3V3,100nF to GND`；`swd=J2 1:3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 C1-D2 U3/J2 reset/SWD

## 模拟电路

### ADC_OUT 总电流采样

U4 INA199A1DCKR 跨接 R5 10mR 分流电阻，V+ 接 VCC_5V、GND 接地，OUT 形成 ADC_OUT 并连接 U3 PB1；C16 10nF 对输出滤波。

- 参数与网络：`amplifier=U4 INA199A1DCKR`；`shunt=R5 10mR/1206`；`supply=VCC_5V`；`output=ADC_OUT`；`mcu=U3 PB1`；`filter=C16 10nF`
- 证据：图 85031f66807e / 第 1 页 / 第 1 页 C3-D3 U4/R5/U3 PB1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit 8Servos | `mcu=U3 STM32F030F4P6`；`channels=IO0-IO7`；`connectors=P1-P4`；`current_monitor=U4 INA199A1DCKR,R5`；`power=U1,U2,Q1,Q3` |
| GPIO 与控制信号 | IO0~IO7 舵机信号 | `IO0=U3 PA0`；`IO1=U3 PA1`；`IO2=U3 PA2`；`IO3=U3 PA3`；`IO4=U3 PA4`；`IO5=U3 PA5`；`IO6=U3 PA6`；`IO7=U3 PA7` |
| 接口 | P1~P4 Header 3X2H | `P1=1 IO0,2 IO1,3/4 VM,5/6 GND`；`P2=1 IO2,2 IO3,3/4 VM,5/6 GND`；`P3=1 IO4,2 IO5,3/4 VM,5/6 GND`；`P4=1 IO6,2 IO7,3/4 VM,5/6 GND` |
| 总线 | U3 I2C | `scl=J1 SCL -> U3 PA9`；`sda=J1 SDA -> U3 PA10`；`pullups=R2/R3 4.7K`；`rail=3V3` |
| 总线地址 | Unit 8Servos I2C 地址 | `documented_address=0x25`；`address_hardware_shown=false`；`firmware_controlled=true` |
| 接口 | J1 GROVE 4P | `signals=SCL,SDA`；`power=BUS_5V`；`ground=GND`；`downstream=U2,Q1/Q3` |
| 电源 | U1 SY8303AIC | `input=P5.4 HPWR`；`input_protection=D1 SMF30CA,D2 TVS 5V`；`converter=U1 SY8303AIC`；`inductor=L1 6.8uH`；`output=VCC_5V`；`output_protection=D3 TVS 5V` |
| 电源 | U2 HX6306P332MR | `input=BUS_5V`；`output=3V3`；`input_cap=C5 100nF`；`regulator=HX6306P332MR` |
| 电源 | VCC_5V 到 VM | `source=VCC_5V`；`fuse=F1 12V/3A`；`shunt=R5 10mR/1206`；`output=VM`；`loads=P1-P4`；`decoupling=C11-C15 shown on VM` |
| 模拟电路 | ADC_OUT 总电流采样 | `amplifier=U4 INA199A1DCKR`；`shunt=R5 10mR/1206`；`supply=VCC_5V`；`output=ADC_OUT`；`mcu=U3 PB1`；`filter=C16 10nF` |
| 电源 | Q1/Q3 AO3401A 电源路径 | `mosfets=Q1/Q3 AO3401A`；`rails=BUS_5V,VCC_5V`；`sense=HPWR via R8 100K`；`pulldown=R4 200K`；`priority=null`；`threshold=null` |
| 接口 | P5 HT3.96 4P | `pin_4=HPWR`；`pin_3=GND`；`pin_2=NC`；`pin_1=VCC_5V` |
| 调试与烧录 | U3 BOOT/NRST/SWD | `boot0=R7 10K to GND`；`reset=R6 10K to 3V3,100nF to GND`；`swd=J2 1:3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND` |
| 保护电路 | 电源保护 | `hpwr_tvs=D1 SMF30CA,D2`；`vcc5_tvs=D3 TVS 5V`；`vm_fuse=F1 12V/3A`；`servo_signal_tvs_shown=false`；`servo_signal_series_shown=false` |
| 其他事实 | 正文舵机控制协议 | `documented_channels=8`；`documented_control=PWM servo and motor release/lock`；`frequency=null`；`pulse_range=null`；`resolution=null`；`registers=null` |
| 其他事实 | 正文电源和负载额定 | `documented_inputs=9-24V or 5V`；`documented_load=DC 5V@3A total`；`fuse_marking=12V/3A`；`test_conditions=null` |
| 时钟 | U3 时钟 | `PF0=NC`；`PF1=NC`；`crystal_shown=false`；`oscillator_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x25`：正文列出 I2C 地址 0x25，原理图没有地址选择硬件或地址标注，地址由 U3 固件决定。（证据：图 85031f66807e / 第 1 页 / 第 1 页 U3/J1 I2C 无地址标注）
- `power.source-switch`：Q1/Q3 以背靠背 AO3401A 连接 BUS_5V 与 VCC_5V，栅极控制节点由 HPWR 经 R8 100K 和 R4 200K 下拉网络驱动；具体电源优先级和切换阈值未在图中注释。（证据：图 85031f66807e / 第 1 页 / 第 1 页 B3 Q1/Q3/R8/R4）
- `other.documented-servo-protocol`：正文称 U3 产生八路 PWM 并支持编程电机释放/锁定；原理图只显示 IO0~IO7 和电源硬件，未标 PWM 频率、脉宽范围、分辨率或释放/锁定寄存器。（证据：图 85031f66807e / 第 1 页 / 第 1 页 U3 IO0-IO7 与电源选择硬件无协议参数）
- `other.documented-ratings`：正文列出 9-24V/5V 双输入和八路总负载 DC 5V@3A；图中有 SY8303AIC、F1 12V/3A 和 VM 网络，但未标完整输入范围、温升、连接器电流或同时负载测试条件。（证据：图 85031f66807e / 第 1 页 / 第 1 页 P5/U1/F1/VM 无系统额定条件）
- `review.i2c-address`：请通过内置固件或 I2C 扫描确认默认地址 0x25。；原因：原理图没有地址配置硬件。
- `review.power-switch`：请依据 Q1/Q3 电路仿真或实测确认 HPWR 与 BUS_5V 的电源优先级、切换阈值和反灌行为。；原因：原理图未注释该背靠背 MOS 电源路径的工作状态。
- `review.servo-protocol`：请依据 U165 内置固件协议确认 PWM 频率、脉宽、分辨率和电机电源释放/锁定寄存器。；原因：这些参数不能从 IO 和电源原理图推导。
- `review.power-ratings`：请依据电源器件、连接器、PCB 温升和八路同时负载测试确认 9-24V 输入及 5V@3A 总负载能力。；原因：保险丝标值不能单独证明整机持续额定。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `85031f66807ed2c90a7f8c3bbebde9790cf74d10fa9705e41b8160a852ed283d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/620/SCH_UNIT_8Servos_V1.01_sch_01.png` |

---

源文档：`zh_CN/unit/8Servos Unit.md`

源文档 SHA-256：`0e9155e83a904d13dc4aeecadb9b6d505a3a02ad6c464a9bdfdb7b3224cbdc25`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
