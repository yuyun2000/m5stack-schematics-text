# Unit ByteButton 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ByteButton |
| SKU | U192 |
| 产品 ID | `unit-bytebutton-afe4979eef29` |
| 源文档 | `zh_CN/unit/Unit ByteButton.md` |

## 概述

Unit ByteButton（U192）以 U10 STM32G031G8U6 为主控，通过 J1/J2 双 Grove I2C 接口通信，并由 U11 ME6206A33XG 将 5V 转换为 3.3V。S1~S8 八个轻触按键分别连接 SW_K0~SW_K7，每路具有 10KΩ 上拉、100nF 滤波和 PESD3V3S1UB ESD；GPIO 映射覆盖 PA0/PA1/PA5/PA6/PA7/PA15/PB3/PA8。U1~U9 九颗 WS2812C-2020 从 PB5/RGB 串行级联，由 3.3V 供电并配置九只 100nF 去耦。Sel_A0/Sel_A1 使用默认 10KΩ 下拉与预留未装上拉，但原理图未给地址真值表、I2C 协议、LED 完整版本或整机功耗。

## 检索关键词

`Unit ByteButton`、`U192`、`STM32G031G8U6`、`STM32G031`、`ME6206A33XG`、`WS2812C-2020`、`9 RGB LED`、`8 buttons`、`S1-S8`、`SW_K0`、`SW_K1`、`SW_K2`、`SW_K3`、`SW_K4`、`SW_K5`、`SW_K6`、`SW_K7`、`PB5 RGB`、`PA0`、`PA1`、`PA5`、`PA6`、`PA7`、`PA15`、`PB3`、`PA8`、`I2C`、`SCL`、`SDA`、`0x47`、`Sel_A0`、`Sel_A1`、`SWD`、`SWCLK`、`SWDIO`、`PESD3V3S1UB`、`Grove cascade`、`VCC_5V`、`VCC_3V3`、`NRST`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U10 | STM32G031G8U6 | 按键扫描、I2C 从设备、RGB 驱动和 SWD 调试主控 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A3:B3 U10 STM32G031G8U6，pins 1~28 与 SW_K0~7/RGB/SDA/SCL/SWD/NRST |
| U11 | ME6206A33XG | 将 VCC_5V 稳压为 VCC_3V3 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A2 U11 ME6206A33XG，pin3 Vin 5V、pin2 Vout 3.3V、pin1 GND |
| J1/J2 | GROVE 4P | 两组并联 I2C/5V/GND 输入与级联接口 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A1:B1 J1/J2 GROVE，IO2/IO1/5V/GND 与 IN/OUT 网络 |
| J3 | SWD_5P | 3.3V、SWCLK、SWDIO、NRST 与 GND 调试接口 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A4 J3 SWD_5P pins 1~5 |
| S1-S8 | 3*4*2.5/1.6N | 八个独立轻触按键，按下时将 SW_K0~SW_K7 接地 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 B1:B4 S1~S8，每路 SW_Kn 到 GND |
| R1-R8 | 10KΩ | 八路按键 SW_K0~SW_K7 到 VCC_3V3 的上拉电阻 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 B1:B4 R1~R8 10KΩ 从 VCC_3V3 到各 SW_Kn |
| C17-C24 | 100nF | 八路按键节点到 GND 的去抖/滤波电容 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 B1:B4 C17~C24 100nF 从 SW_K0~7 到 GND |
| D1-D8 | PESD3V3S1UB | 八路按键节点的 ESD 保护二极管 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 C1 D1~D8 PESD3V3S1UB，分别从 SW_K0~7 到 GND |
| U1-U9 | WS2812C-2020 | 九颗串行级联 RGB LED，由 PB5/RGB 驱动 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 D1:D4 U1~U9 WS2812C-2020，VDD/DO/DI/GND 串行链 |
| C3-C9/C13/C14 | 100nF | 九颗 RGB LED 的 3.3V 去耦电容组 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 C3:C4 C3~C9/C13/C14 共九只 100nF 并联 VCC_3V3-GND |
| R11/R14 | 4.7KΩ | SCL/SDA 到 VCC_3V3 的 I2C 上拉电阻 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A2 R11 4.7KΩ-SCL、R14 4.7KΩ-SDA |
| R20-R23 | NC/NC/10KΩ/10KΩ | Sel_A0/Sel_A1 地址选择预留上拉与默认下拉网络 | 图 ad4eb9cad9d3 / 第 1 页 / 页面 A4 Reserve 框，R20/R21 NC 到 3V3，R22/R23 10KΩ 到 GND |

## 系统结构

### Unit ByteButton 系统架构

U10 STM32G031G8U6 通过双 Grove I2C 提供八键扫描和九颗 WS2812C-2020 RGB 控制，U11 从 5V 生成 3.3V，并提供 SWD 与地址选择。

- 参数与网络：`mcu=U10 STM32G031G8U6`；`buttons=S1-S8`；`rgb=U1-U9 WS2812C-2020`；`i2c=J1/J2`；`power=U11 ME6206A33XG`；`debug=J3 SWD_5P`；`address_straps=Sel_A0/Sel_A1`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 整页 MCU/I2C/按键/RGB/电源/SWD/地址分区

## 电源

### 5V 到 3.3V

U11 ME6206A33XG pin3 Vin 接 VCC_5V、pin2 Vout 输出 VCC_3V3、pin1 GND；输入 C16 10uF/C1 10uF，输出 C2 10uF/C15 100nF。

- 参数与网络：`input=VCC_5V`；`output=VCC_3V3`；`regulator=ME6206A33XG`；`input_caps=C16,C1 10uF`；`output_caps=C2 10uF,C15 100nF`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A2 U11 与输入输出电容

### RGB 电源与去耦

U1~U9 VDD 接 VCC_3V3、GND 接地，C3~C9/C13/C14 共九只 100nF 并联去耦。

- 参数与网络：`rail=VCC_3V3`；`leds=U1-U9`；`capacitors=C3-C9,C13,C14 100nF`；`count=9`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 C3:C4 去耦组与 D 行 LED 电源

## 接口

### J1/J2 公共针脚

J1/J2 的 IO2 接 SCL、IO1 接 SDA、5V 接 VCC_5V、GND 接地。

- 参数与网络：`IO2=SCL`；`IO1=SDA`；`5V=VCC_5V`；`GND=GND`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面左侧 J1/J2 GROVE 4P

## 总线

### 双 Grove I2C

J1 IO2/IO1 通过 R9/R10 0Ω 接 SCL/SDA，J2 IO2/IO1 通过 R16/R18 0Ω 接相同 SCL/SDA；两接口并联用于级联。

- 参数与网络：`J1=IO2-IN_2-R9-SCL,IO1-IN_1-R10-SDA`；`J2=IO2-OUT_2-R16-SCL,IO1-OUT_1-R18-SDA`；`series=all 0Ω`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A1:B2 J1/J2/R9/R10/R16/R18/SCL/SDA

### MCU I2C 引脚

SDA 连接 U10 PA12[PA10] pin19，SCL 连接 PA11[PA9] pin18，R14/R11 4.7KΩ 上拉到 3.3V。

- 参数与网络：`sda=U10 pin19 PA12[PA10]`；`scl=U10 pin18 PA11[PA9]`；`pullups=R14/R11 4.7KΩ`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A2:A3 U10 SDA/SCL 与 R11/R14

### 九颗 RGB 串行链

U10 PB5 pin25 的 RGB 网络接 U1 DI，U1 DO 逐级连接到 U9 DI；U9 DO 未显示外部连接。

- 参数与网络：`controller=U10 PB5 pin25`；`input=RGB -> U1 DI`；`chain=U1 DO -> U2 DI -> ... -> U9 DI`；`final_output=U9 DO no visible connection`；`count=9`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A3 PB5 RGB 与 D1:D4 U1~U9 链

## GPIO 与控制信号

### 八路按键 MCU 映射

SW_K0~SW_K7 分别连接 U10 PA0、PA1、PA5、PA6、PA7、PA15、PB3、PA8。

- 参数与网络：`SW_K0=PA0 pin6`；`SW_K1=PA1 pin7`；`SW_K2=PA5 pin11`；`SW_K3=PA6 pin12`；`SW_K4=PA7 pin13`；`SW_K5=PA15 pin22`；`SW_K6=PB3 pin23`；`SW_K7=PA8 pin16`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 U10 SW_K0~7 与按键区域同名网络

### I2C 地址选择

U10 PB0/PB1 连接 Sel_A0/Sel_A1；R22/R23 10KΩ 默认下拉，R20/R21 到 3.3V 标 NC 作为预留上拉。

- 参数与网络：`a0=PB0 pin14,R22 10KΩ GND,R20 NC 3V3`；`a1=PB1 pin15,R23 10KΩ GND,R21 NC 3V3`；`default_bits=0,0`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A4 Reserve 框与 U10 Sel_A0/Sel_A1

## 时钟

### 外部时钟

U10 PC14-OSC32IN/PC15-OSC32OUT 未显示外接晶振，页面无其他时钟器件。

- 参数与网络：`pc14=no visible connection`；`pc15=no visible connection`；`external_crystal=null`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 U10 pins1/2 与整页无晶振

## 复位

### MCU NRST

U10 PF2-NRST pin5 连接 NRST，R13 10KΩ 上拉到 3.3V，C12 1uF 接地并引到 J3 pin4。

- 参数与网络：`mcu=U10 pin5 PF2-NRST`；`pullup=R13 10KΩ`；`capacitor=C12 1uF`；`debug=J3 pin4`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A3 U10 NRST 与 R13/C12/J3

## 保护电路

### 按键 ESD

SW_K0~SW_K7 各通过一只 PESD3V3S1UB D1~D8 接地保护。

- 参数与网络：`devices=D1-D8 PESD3V3S1UB`；`protected_nets=SW_K0-SW_K7`；`return=GND`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 C1 D1~D8 ESD 阵列

## 存储

### 外部存储器

本页未显示独立 Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 整页器件无外部存储芯片

## 调试与烧录

### J3 SWD 接口

J3 pins 1~5 为 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND；SWCLK/SWDIO 分别连接 U10 PA14 pin21/PA13 pin20。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=SWCLK PA14`；`pin_3=SWDIO PA13`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 A4 J3 与 U10 PA14/PA13

## 模拟电路

### 按键上拉与去抖

每个 SW_Kn 由 10KΩ 上拉到 3.3V、100nF 接地，按键按下接 GND。

- 参数与网络：`pullups=R1-R8 10KΩ`；`capacitors=C17-C24 100nF`；`switches=S1-S8 to GND`；`active_level=low`
- 证据：图 ad4eb9cad9d3 / 第 1 页 / 页面 B1:B4 八路重复按键电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ByteButton 系统架构 | `mcu=U10 STM32G031G8U6`；`buttons=S1-S8`；`rgb=U1-U9 WS2812C-2020`；`i2c=J1/J2`；`power=U11 ME6206A33XG`；`debug=J3 SWD_5P`；`address_straps=Sel_A0/Sel_A1` |
| 总线 | 双 Grove I2C | `J1=IO2-IN_2-R9-SCL,IO1-IN_1-R10-SDA`；`J2=IO2-OUT_2-R16-SCL,IO1-OUT_1-R18-SDA`；`series=all 0Ω` |
| 总线 | MCU I2C 引脚 | `sda=U10 pin19 PA12[PA10]`；`scl=U10 pin18 PA11[PA9]`；`pullups=R14/R11 4.7KΩ` |
| 接口 | J1/J2 公共针脚 | `IO2=SCL`；`IO1=SDA`；`5V=VCC_5V`；`GND=GND` |
| 电源 | 5V 到 3.3V | `input=VCC_5V`；`output=VCC_3V3`；`regulator=ME6206A33XG`；`input_caps=C16,C1 10uF`；`output_caps=C2 10uF,C15 100nF` |
| GPIO 与控制信号 | 八路按键 MCU 映射 | `SW_K0=PA0 pin6`；`SW_K1=PA1 pin7`；`SW_K2=PA5 pin11`；`SW_K3=PA6 pin12`；`SW_K4=PA7 pin13`；`SW_K5=PA15 pin22`；`SW_K6=PB3 pin23`；`SW_K7=PA8 pin16` |
| 模拟电路 | 按键上拉与去抖 | `pullups=R1-R8 10KΩ`；`capacitors=C17-C24 100nF`；`switches=S1-S8 to GND`；`active_level=low` |
| 保护电路 | 按键 ESD | `devices=D1-D8 PESD3V3S1UB`；`protected_nets=SW_K0-SW_K7`；`return=GND` |
| 总线 | 九颗 RGB 串行链 | `controller=U10 PB5 pin25`；`input=RGB -> U1 DI`；`chain=U1 DO -> U2 DI -> ... -> U9 DI`；`final_output=U9 DO no visible connection`；`count=9` |
| 电源 | RGB 电源与去耦 | `rail=VCC_3V3`；`leds=U1-U9`；`capacitors=C3-C9,C13,C14 100nF`；`count=9` |
| 调试与烧录 | J3 SWD 接口 | `pin_1=VCC_3V3`；`pin_2=SWCLK PA14`；`pin_3=SWDIO PA13`；`pin_4=NRST`；`pin_5=GND` |
| 复位 | MCU NRST | `mcu=U10 pin5 PF2-NRST`；`pullup=R13 10KΩ`；`capacitor=C12 1uF`；`debug=J3 pin4` |
| GPIO 与控制信号 | I2C 地址选择 | `a0=PB0 pin14,R22 10KΩ GND,R20 NC 3V3`；`a1=PB1 pin15,R23 10KΩ GND,R21 NC 3V3`；`default_bits=0,0` |
| 时钟 | 外部时钟 | `pc14=no visible connection`；`pc15=no visible connection`；`external_crystal=null` |
| 存储 | 外部存储器 | `flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线地址 | I2C 地址映射 | `bits=Sel_A0,Sel_A1`；`default=0,0`；`address=null`；`candidate_from_product_doc=0x47` |
| 核心器件 | RGB 完整型号 | `schematic=WS2812C-2020`；`version=null`；`full_ordering_code=null` |
| 其他事实 | I2C 固件协议与行为 | `registers=null`；`commands=null`；`debounce_time=null`；`rgb_timing=null`；`brightness=null`；`i2c_speed=null`；`firmware_version=null` |
| 电源 | 功耗与温度性能 | `standby_current=null`；`operating_current=null`；`power=null`；`temperature_range=null` |

## 待确认事项

- `address.i2c-map`：原理图确认 Sel_A0/Sel_A1 硬件位，但没有给出位组合到地址的映射，不能仅凭本页确认默认 0x47。（证据：图 ad4eb9cad9d3 / 第 1 页 / Sel_A0/Sel_A1 网络，无十六进制地址表）
- `component.rgb-full-model`：原理图标 WS2812C-2020，未显示版本后缀或完整订货型号。（证据：图 ad4eb9cad9d3 / 第 1 页 / U1~U9 型号文字 WS2812C-2020）
- `other.firmware-protocol`：原理图未标注寄存器/命令、按键去抖时间、RGB 时序、亮度/颜色能力、I2C 速率或固件版本。（证据：图 ad4eb9cad9d3 / 第 1 页 / 整页硬件连接，无协议/时序参数）
- `power.performance`：原理图未标注待机/工作电流、DC 5V@8.94mA 或工作温度范围。（证据：图 ad4eb9cad9d3 / 第 1 页 / 整页 5V/3.3V 电路，无功耗或温度注释）
- `review.i2c-address`：Sel_A0/Sel_A1 各组合对应什么 I2C 地址，默认是否为 0x47？；原因：原理图只有配置位，没有地址表。
- `review.rgb-full-model`：九颗 RGB 的完整订货型号和版本是什么？；原因：图纸只标 WS2812C-2020。
- `review.firmware-protocol`：I2C 命令/寄存器、按键去抖、RGB 时序与固件版本是什么？；原因：这些由固件定义，原理图未提供。
- `review.power-performance`：待机/工作功耗与工作温度范围是什么？；原因：原理图无整机性能参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ad4eb9cad9d36ddcde7bd924d7fcdd17de4e3a92136571e8d6f4366f1a1eda2c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/819/U192_SCH_Unit-ByteButton_V1.0_2024_11_20_16_18_15_page_01.png` |

---

源文档：`zh_CN/unit/Unit ByteButton.md`

源文档 SHA-256：`1f66db9e2ef5ef925cdffe8793e8fae314c8f285cb35c35e0fc4d7a4fee397b7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
