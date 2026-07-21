# Module13.2 AIN4-20mA 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 AIN4-20mA |
| SKU | M133 |
| 产品 ID | `module13-2-ain4-20ma-27da563bb743` |
| 源文档 | `zh_CN/module/AIN4-20mA Module 13.2.md` |

## 概述

Module13.2 AIN4-20mA 以 STM32G030F6P6（U14）采集 VOUT1~VOUT4，并通过 M5-Bus 的 SCL/SDA 与主机通信。四路 4-20mA 输入各使用 24R 采样、HCNR200-000E 光耦、SGM321YC5/TR 运放、BC807 晶体管与 BZT52C5V1S 钳位构成隔离调理链，原理图标注输出范围 0.593~2.9686V。HPWR 经 ME3116AM6G 生成 BUS_5V，再由 SX1308 生成 HPWR_24V 并经 F2424S-2WR3 隔离为 ISO_24V；HX6306P332MR 从 BUS_5V 生成 VCC_3V3。

## 检索关键词

`Module13.2 AIN4-20mA`、`M133`、`STM32G030F6P6`、`HCNR200-000E`、`F2424S-2WR3`、`SGM321YC5/TR`、`ME3116AM6G`、`SX1308`、`HX6306P332MR`、`BC807-40W,115`、`BZT52C5V1S`、`4-20mA`、`0.593-2.9686V`、`VOUT1`、`VOUT2`、`VOUT3`、`VOUT4`、`ISO_24V`、`ISO_GND`、`HPWR_24V`、`BUS_5V`、`VCC_3V3`、`I2C`、`0x55`、`M5_BUS`、`IN1+`、`IN1-`、`M1+`、`M1-`、`24R`、`SWD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U14 | STM32G030F6P6 | 主控 MCU，采集 VOUT1~VOUT4、处理 I2C 并提供 SWD | 图 fb1bb2b0fc7c / 第 1 页 / B6-C7 区域 U14 STM32G030F6P6：SCL/SDA、VOUT1~4、SWDIO/SWCLK、NRST 与 VCC_3V3 |
| U1/U2/U3/U4 | HCNR200-000E | 四路模拟信号隔离光耦，每颗以 A/B/C 单元分布在输入反馈和隔离输出侧 | 图 fb1bb2b0fc7c / 第 1 页 / B3-D5 四路通道中的 U1A/B/C、U2A/B/C、U3A/B/C、U4A/B/C HCNR200-000E |
| U6/U7/U8/U9 | SGM321YC5/TR | 四路隔离输入侧运放，驱动 Q1~Q4 与 HCNR200 输入 LED 反馈环 | 图 fb1bb2b0fc7c / 第 1 页 / B3-D4 每路左侧 U6~U9 SGM321YC5/TR 与 HCNR200/Q1~Q4 网络 |
| U10/U11/U12/U13 | SGM321YC5/TR | 四路非隔离输出侧跨阻/放大运放，产生 VOUT1~VOUT4 | 图 fb1bb2b0fc7c / 第 1 页 / B5-D6 每路右侧 U10~U13 SGM321YC5/TR、62K/1nF 反馈与 VOUT1~4 |
| Q1/Q2/Q3/Q4 | BC807-40W,115 | 四路隔离发送端的 PNP 晶体管驱动器 | 图 fb1bb2b0fc7c / 第 1 页 / B4-D4 Q1~Q4 BC807-40W,115，连接运放输出、ISO_24V 和光耦驱动支路 |
| D3/D4/D5/D6 | BZT52C5V1S | 四路隔离发送端的 5.1V 钳位器件 | 图 fb1bb2b0fc7c / 第 1 页 / B4-D4 每路 Q1~Q4 右侧 D3~D6 BZT52C5V1S 与 C11~C14 100nF |
| U5 | F2424S-2WR3 | 将 HPWR_24V/GND 隔离转换为 ISO_24V/ISO_GND 的电源隔离模块 | 图 fb1bb2b0fc7c / 第 1 页 / A5 区域 U5 F2424S-2WR3：VIN/GND 输入与 +VO/0V 输出 |
| U16 | ME3116AM6G | 从 HPWR 生成 BUS_5V 的降压转换器 | 图 fb1bb2b0fc7c / 第 1 页 / A2-A3 区域 U16 ME3116AM6G 与 L2/D10/R15/R14 电源网络 |
| U17 | SX1308 | 从 BUS_5V 升压生成 HPWR_24V 的转换器 | 图 fb1bb2b0fc7c / 第 1 页 / A3-A4 区域 U17 SX1308 与 L1/D1/R21/R26 电源网络 |
| U15 | HX6306P332MR | 从 BUS_5V 生成 VCC_3V3 的稳压器 | 图 fb1bb2b0fc7c / 第 1 页 / B6-B7 区域 U15 HX6306P332MR：VIN/BUS_5V、VOUT/FB1、VCC_3V3、GND |
| P3/P4/P5/P6 | Header 2 | 四路 4-20mA 现场输入端，分别引出 IN1+/IN1- 至 IN4+/IN4- | 图 fb1bb2b0fc7c / 第 1 页 / B1-D1 左侧 P3~P6 Header 2，均标注 DC:4-20mA 和 INx+/INx- |
| P7/P8/P9/P10 | Jumper 2 | 四路输入到 Mx+/Mx- 模拟前端的串联跳线 | 图 fb1bb2b0fc7c / 第 1 页 / B2-D2 P7~P10 Jumper 2，左侧 INx+/INx-，右侧 Mx+/Mx- |
| P11/P12/P13/P14 | Jumper 4 | 四路 ISO_24V/ISO_GND 与 INx+/Mx- 的 2 线/4 线传感器供电模式跳线 | 图 fb1bb2b0fc7c / 第 1 页 / B2-D2 P11~P14 Jumper 4：ISO_24V、INx+、Mx-、ISO_GND 四行网络 |
| J1 | M5_BUS | 30 针主机接口，使用 GND、SDA、SCL、HPWR、BUS_5V 和 BAT_OUT | 图 fb1bb2b0fc7c / 第 1 页 / D7-D8 区域 J1 M5_BUS 1~30 脚及 SDA/SCL/HPWR/BUS_5V/BAT_OUT 网络 |
| P15 | SWD_5P | MCU 调试接口，引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND | 图 fb1bb2b0fc7c / 第 1 页 / C7 区域 P15 SWD_5P 五针网络 |
| D9 | SMF30CA | HPWR 输入对 GND 的瞬态保护器 | 图 fb1bb2b0fc7c / 第 1 页 / A1-A2 P1/U16 输入旁 D9 SMF30CA 跨接 HPWR 与 GND |

## 系统结构

### Module13.2 AIN4-20mA

四路 4-20mA 输入分别经 HCNR200 隔离与双运放调理生成 VOUT1~VOUT4，由 U14 STM32G030F6P6 的 PA0~PA3 采集；主机通过 M5-Bus I2C 通信。

- 参数与网络：`channels=4`；`controller=U14 STM32G030F6P6`；`isolators=U1-U4 HCNR200-000E`；`opamps=U6-U13 SGM321YC5/TR`；`adc_inputs=PA0-PA3`；`host_bus=I2C via J1 M5_BUS`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B1-D8 四路通道、U14、J1 和全部 VOUT/SCL/SDA 网络

## 核心器件

### U14 STM32G030F6P6

U14.8~U14.11 PA0~PA3 分别连接 VOUT1~VOUT4；U14.1 接 SCL，U14.2 接 SDA，U14.18/19 接 MCU_SWDIO/MCU_SWCLK，U14.6 接 NRST。

- 参数与网络：`pin_8=PA0 VOUT1`；`pin_9=PA1 VOUT2`；`pin_10=PA2 VOUT3`；`pin_11=PA3 VOUT4`；`pin_1=SCL`；`pin_2=SDA`；`pin_18=MCU_SWDIO`；`pin_19=MCU_SWCLK`；`pin_6=NRST`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B6-C7 U14 左右引脚编号、复用名与 VOUT/SCL/SDA/SWD/NRST 网络

## 电源

### U16 HPWR 降压级

U16 VIN 接 HPWR，EN 经 R9 100K 接 HPWR；LX 经 L2 6.8uH 输出 BUS_5V，D10 DSS34 连接 LX 与 GND，R15 210K/R14 39K 构成反馈。

- 参数与网络：`input=HPWR`；`converter=U16 ME3116AM6G`；`enable=R9 100K`；`inductor=L2 6.8uH`；`diode=D10 DSS34`；`output=BUS_5V`；`feedback=R15 210K / R14 39K`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / A1-A3 P1/D9/U16/L2/D10 与 BUS_5V 网络

### U17 24V 升压级

BUS_5V 经 L1 4.7uH 与 U17 SX1308、D1 DSS34 生成 HPWR_24V，R21 390K/R26 10K 构成反馈。

- 参数与网络：`input=BUS_5V`；`converter=U17 SX1308`；`inductor=L1 4.7uH`；`diode=D1 DSS34`；`output=HPWR_24V`；`feedback=R21 390K / R26 10K`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / A3-A4 BUS_5V/L1/U17/D1/HPWR_24V 与反馈网络

### U5 隔离电源

U5 F2424S-2WR3 的 VIN/GND 接 HPWR_24V/GND，+VO/0V 输出 ISO_24V/ISO_GND，两侧各有 10uF/100nF 去耦。

- 参数与网络：`input=HPWR_24V/GND`；`module=U5 F2424S-2WR3`；`output=ISO_24V/ISO_GND`；`input_caps=C24 10uF; C25 100nF`；`output_caps=C26 10uF; C27 100nF`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / A4-A5 HPWR_24V/U5/ISO_24V 与 C24~C27

### U15 VCC_3V3 稳压

U15 HX6306P332MR 以 BUS_5V 为输入，VOUT 经 FB1 330R/GZ1005D331TF 形成 VCC_3V3，为 U14 与 SWD 供电。

- 参数与网络：`input=BUS_5V`；`regulator=U15 HX6306P332MR`；`filter=FB1 330R/GZ1005D331TF`；`output=VCC_3V3`；`loads=U14; P15`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B6-B7 U15/FB1/BUS_5V/VCC_3V3 与 U14/P15 网络

## 接口

### J1 M5_BUS

J1.2/4/6 接 GND，J1.18 接 SDA，J1.17 接 SCL，J1.26/28/30 接 HPWR，J1.27 接 BUS_5V，J1.29 接 BAT_OUT；其余图示信号未连接。

- 参数与网络：`ground=pins 2,4,6`；`sda=pin 18`；`scl=pin 17`；`hpwr=pins 26,28,30`；`bus_5v=pin 27`；`bat_out=pin 29`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / D7-D8 J1 M5_BUS 1~30 脚与实际连线

### P3~P6 四路电流输入

P3、P4、P5、P6 分别引出 IN1+/IN1-、IN2+/IN2-、IN3+/IN3-、IN4+/IN4-，每路旁标注 DC:4-20mA。

- 参数与网络：`P3=IN1+, IN1-`；`P4=IN2+, IN2-`；`P5=IN3+, IN3-`；`P6=IN4+, IN4-`；`range_label=DC:4-20mA`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B1-D1 P3~P6 Header 2 及蓝色 DC:4-20mA 标签

### 2线/4线传感器跳线

每路 P7~P10 将 INx+/INx- 串接到 Mx+/Mx-；P11~P14 进一步引出 ISO_24V、INx+、Mx-、ISO_GND，用于内部/外部传感器供电模式配置。

- 参数与网络：`channel_1=P7 and P11`；`channel_2=P8 and P12`；`channel_3=P9 and P13`；`channel_4=P10 and P14`；`isolated_supply=ISO_24V/ISO_GND`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B2-D2 P7~P14 的 INx/Mx/ISO_24V/ISO_GND 网络

## 总线

### SCL/SDA

J1.17 SCL 连接 U14.1，J1.18 SDA 连接 U14.2；页面未显示 I2C 上拉或电平转换。

- 参数与网络：`scl=J1.17 to U14.1`；`sda=J1.18 to U14.2`；`pullups=not shown`；`level_shifter=not shown`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B6-D8 U14 与 J1 的 SCL/SDA 同名网络

## 时钟

### U14 时钟

U14 的 PC14-OSC32_IN 与 PC15-OSC32_OUT 未连接，页面未显示外部晶振或谐振器。

- 参数与网络：`osc32_in=NC`；`osc32_out=NC`；`external_crystal=not shown`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B6-B7 U14 顶部 PC14-OSC32_IN/PC15-OSC32_OUT 短线无连接

## 保护电路

### HPWR 输入保护

D9 SMF30CA 跨接 HPWR 与 GND，位于 P1/U16 输入侧。

- 参数与网络：`protector=D9 SMF30CA`；`protected_net=HPWR`；`reference=GND`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / A1-A2 D9 SMF30CA 的 HPWR-GND 跨接

## 调试与烧录

### P15 SWD 与 NRST

P15 引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND；NRST 由 R27 10K 上拉至 VCC_3V3，并有对地电容。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`；`reset_pullup=R27 10K`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / C7 P15 与 B7-C7 U14 NRST/R27/电容网络

## 模拟电路

### 四路 24R 电流采样

M1-、M2-、M3-、M4- 分别通过 R2、R4、R6、R8 24R 接到各通道隔离输入参考节点。

- 参数与网络：`channel_1=R2 24R`；`channel_2=R4 24R`；`channel_3=R6 24R`；`channel_4=R8 24R`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B3-D3 每路 Mx- 水平线上 R2/R4/R6/R8 24R

### HCNR200 隔离发送端

每路由 HCNR200 的 A/B 单元、10K 反馈电阻、SGM321 输入侧运放、BC807 晶体管和 BZT52C5V1S/100nF 钳位网络构成 ISO_24V 侧闭环发送级。

- 参数与网络：`channel_1=U1A/U1B, U6, Q1, D3`；`channel_2=U2A/U2B, U7, Q2, D4`；`channel_3=U3A/U3B, U8, Q3, D5`；`channel_4=U4A/U4B, U9, Q4, D6`；`isolated_rail=ISO_24V/ISO_GND`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B3-D5 四组 HCNR A/B、U6~U9、Q1~Q4、D3~D6 对称电路

### VOUT1~VOUT4 输出调理

HCNR200 的 C 单元分别驱动 U10~U13，R22~R25 62K 与 C15~C18 1nF 构成反馈，产生 VOUT1~VOUT4。

- 参数与网络：`VOUT1=U1C-U10-R22 62K-C15 1nF`；`VOUT2=U2C-U11-R23 62K-C16 1nF`；`VOUT3=U3C-U12-R24 62K-C17 1nF`；`VOUT4=U4C-U13-R25 62K-C18 1nF`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B5-D6 四组 HCNR C 单元、U10~U13、62K/1nF 反馈和 VOUT 标签

### 4-20mA 到电压转换

原理图文字框明确标注 INPUT:4-20mA、OUTPUT:0.593-2.9686V。

- 参数与网络：`input_range=4-20mA`；`output_range=0.593-2.9686V`
- 证据：图 fb1bb2b0fc7c / 第 1 页 / B1 左侧 P3 下方红色文字框 INPUT:4-20mA / OUTPUT:0.593-2.9686V

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 AIN4-20mA | `channels=4`；`controller=U14 STM32G030F6P6`；`isolators=U1-U4 HCNR200-000E`；`opamps=U6-U13 SGM321YC5/TR`；`adc_inputs=PA0-PA3`；`host_bus=I2C via J1 M5_BUS` |
| 核心器件 | U14 STM32G030F6P6 | `pin_8=PA0 VOUT1`；`pin_9=PA1 VOUT2`；`pin_10=PA2 VOUT3`；`pin_11=PA3 VOUT4`；`pin_1=SCL`；`pin_2=SDA`；`pin_18=MCU_SWDIO`；`pin_19=MCU_SWCLK`；`pin_6=NRST` |
| 接口 | J1 M5_BUS | `ground=pins 2,4,6`；`sda=pin 18`；`scl=pin 17`；`hpwr=pins 26,28,30`；`bus_5v=pin 27`；`bat_out=pin 29` |
| 总线 | SCL/SDA | `scl=J1.17 to U14.1`；`sda=J1.18 to U14.2`；`pullups=not shown`；`level_shifter=not shown` |
| 总线地址 | 模块 I2C 地址 | `documented_address=0x55`；`schematic_address_label=not shown`；`address_straps=not shown`；`firmware_evidence=not shown` |
| 接口 | P3~P6 四路电流输入 | `P3=IN1+, IN1-`；`P4=IN2+, IN2-`；`P5=IN3+, IN3-`；`P6=IN4+, IN4-`；`range_label=DC:4-20mA` |
| 接口 | 2线/4线传感器跳线 | `channel_1=P7 and P11`；`channel_2=P8 and P12`；`channel_3=P9 and P13`；`channel_4=P10 and P14`；`isolated_supply=ISO_24V/ISO_GND` |
| 模拟电路 | 四路 24R 电流采样 | `channel_1=R2 24R`；`channel_2=R4 24R`；`channel_3=R6 24R`；`channel_4=R8 24R` |
| 模拟电路 | HCNR200 隔离发送端 | `channel_1=U1A/U1B, U6, Q1, D3`；`channel_2=U2A/U2B, U7, Q2, D4`；`channel_3=U3A/U3B, U8, Q3, D5`；`channel_4=U4A/U4B, U9, Q4, D6`；`isolated_rail=ISO_24V/ISO_GND` |
| 模拟电路 | VOUT1~VOUT4 输出调理 | `VOUT1=U1C-U10-R22 62K-C15 1nF`；`VOUT2=U2C-U11-R23 62K-C16 1nF`；`VOUT3=U3C-U12-R24 62K-C17 1nF`；`VOUT4=U4C-U13-R25 62K-C18 1nF` |
| 模拟电路 | 4-20mA 到电压转换 | `input_range=4-20mA`；`output_range=0.593-2.9686V` |
| 模拟电路 | IN+ 与 IN- 输入阻抗 | `documented_typical_impedance=200Ω`；`schematic_shunt=24R per channel`；`equivalent_impedance_label=not shown` |
| 电源 | U16 HPWR 降压级 | `input=HPWR`；`converter=U16 ME3116AM6G`；`enable=R9 100K`；`inductor=L2 6.8uH`；`diode=D10 DSS34`；`output=BUS_5V`；`feedback=R15 210K / R14 39K` |
| 电源 | U17 24V 升压级 | `input=BUS_5V`；`converter=U17 SX1308`；`inductor=L1 4.7uH`；`diode=D1 DSS34`；`output=HPWR_24V`；`feedback=R21 390K / R26 10K` |
| 电源 | U5 隔离电源 | `input=HPWR_24V/GND`；`module=U5 F2424S-2WR3`；`output=ISO_24V/ISO_GND`；`input_caps=C24 10uF; C25 100nF`；`output_caps=C26 10uF; C27 100nF` |
| 电源 | U15 VCC_3V3 稳压 | `input=BUS_5V`；`regulator=U15 HX6306P332MR`；`filter=FB1 330R/GZ1005D331TF`；`output=VCC_3V3`；`loads=U14; P15` |
| 电源 | 外部 DC 电源范围 | `documented_range=DC 9-24V`；`schematic_label=Power:0-24V`；`confirmed_range=not resolved` |
| 保护电路 | HPWR 输入保护 | `protector=D9 SMF30CA`；`protected_net=HPWR`；`reference=GND` |
| 调试与烧录 | P15 SWD 与 NRST | `pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`；`reset_pullup=R27 10K` |
| 时钟 | U14 时钟 | `osc32_in=NC`；`osc32_out=NC`；`external_crystal=not shown` |

## 待确认事项

- `address.i2c-0x55`：产品正文标注 I2C 地址为 0x55，但原理图未标注地址、地址选择网络或固件版本，无法仅由该页确认。（证据：图 fb1bb2b0fc7c / 第 1 页 / 全页 U14 与 SCL/SDA 网络，未见 0x55 或地址配置）
- `analog.input-impedance-200r`：产品正文声明输入阻抗典型值 200Ω，但原理图只明确标出每路 24R 采样及有源隔离网络，没有 200Ω 等效输入阻抗标注。（证据：图 fb1bb2b0fc7c / 第 1 页 / B3-D3 各通道 24R 输入电阻与隔离有源电路，未见 200Ω 标注）
- `power.external-input-range`：产品正文声明外部 DC 9~24V，原理图 P2 旁却标注 Power:0-24V；两者下限不一致，无法确认正式工作输入范围。（证据：图 fb1bb2b0fc7c / 第 1 页 / A1-B1 P2 Header 2 左侧蓝色 Power:0-24V 标注）
- `review.i2c-address-0x55`：模块 I2C 地址 0x55 是否由 STM32 固件固定实现？；原因：原理图仅显示 SCL/SDA，不含地址或固件信息。
- `review.input-impedance`：IN+ 与 IN- 的 200Ω 典型输入阻抗如何由 24R 采样和有源隔离网络定义？；原因：原理图未直接标注 200Ω 等效阻抗。
- `review.external-input-range`：外部 DC 输入的正式工作范围下限是 0V 还是 9V？；原因：产品正文写 9~24V，原理图 P2 标注 0~24V。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fb1bb2b0fc7c857666c46afd637a63f034cb7d77e0141da5fec8df81d8e6f548` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/560/SCH_Module13.2_AIN4-20mA_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/AIN4-20mA Module 13.2.md`

源文档 SHA-256：`bcf1726837c837c2c58f6fd6cc8f38295f1e8d91c67fcb4157369542b8dcefc7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
