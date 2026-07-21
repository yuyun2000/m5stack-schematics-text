# BugC2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | BugC2 |
| SKU | K033-C |
| 产品 ID | `bugc2-9d763b1973a6` |
| 源文档 | `zh_CN/app/BUGC2.md` |

## 概述

BugC2 以 STM32F030F4P6 为控制核心，四颗 L9110S 分别驱动四个两针电机接口，控制信号占用 PA1-PA7 和 PB1。主机通过 STICKIO 提供 SCL/SDA、IR_R、+3.3V 和 +5VIN，板上另有 SWD 调试接口、SL0038GD 红外接收器以及两颗级联 WS2812C-2020 RGB LED。PA0 上的 BAT_ADC/RGB 网络同时连接 RGB 数据输入和电池分压采样支路。电源部分包含仅供电的 USB Type-C、TP4057 充电器、充电状态 LED、16340 电池座、2A 保险丝、反接保护和由 +3.3V 控制的 BAT 输出开关。

## 检索关键词

`BugC2`、`K033-C`、`STM32F030F4P6`、`L9110S`、`TP4057`、`SL0038GD`、`WS2812C-2020`、`AO3401A`、`AO3400A`、`STICKIO`、`USB Type-C`、`SWD`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`SCL PA9`、`SDA PA10`、`IR_R`、`BAT_ADC/RGB`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA5`、`PA6`、`PA7`、`PB1`、`16340_B+`、`BAT`、`+3.3V`、`+5VIN`、`four motor drivers`、`battery reverse protection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | 主控制器，管理四路电机、I2C、RGB/电池采样和 SWD 调试 | 图 d38ba3ddf050 / 第 1 页 / 网格 2B，U3 STM32F030F4P6 及 PA0-PA14、PB1、NRST、BOOT0、电源引脚 |
| U1 | L9110S | 由 PA3/PA4 控制并驱动 P1 的第一路双向电机驱动器 | 图 d38ba3ddf050 / 第 1 页 / 网格 1A-2A，U1 L9110S、P1、PA3/PA4、BAT 和 C5 |
| U2 | L9110S | 由 PA2/PB1 控制并驱动 P2 的第二路双向电机驱动器 | 图 d38ba3ddf050 / 第 1 页 / 网格 3A-4A，U2 L9110S、P2、PA2/PB1、BAT 和 C6 |
| U4 | L9110S | 由 PA1/PA7 控制并驱动 P3 的第三路双向电机驱动器 | 图 d38ba3ddf050 / 第 1 页 / 网格 1A-2B，U4 L9110S、P3、PA1/PA7、BAT 和 C10 |
| U5 | L9110S | 由 PA5/PA6 控制并驱动 P4 的第四路双向电机驱动器 | 图 d38ba3ddf050 / 第 1 页 / 网格 3A-4B，U5 L9110S、P4、PA5/PA6、BAT 和 C11 |
| P1, P2, P3, P4 | Header 2 | 四个两针电机输出接口，分别连接 U1、U2、U4、U5 的 OA/OB | 图 d38ba3ddf050 / 第 1 页 / 网格 1A-4B，P1-P4 Header 2 与各 L9110S 输出 |
| P5 | SWD_5p | STM32 的五针 SWD 调试与复位接口 | 图 d38ba3ddf050 / 第 1 页 / 网格 3B，P5 SWD_5p 的 VCC/SWCLK/SWDIO/RST/GND |
| P6 | STICKIO | 与 M5StickC 主机连接的八针板间接口 | 图 d38ba3ddf050 / 第 1 页 / 网格 4C，P6 STICKIO 的 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN |
| IR1 | SL0038GD | 3.3V 红外接收器，输出 IR_R 到 STICKIO G36 | 图 d38ba3ddf050 / 第 1 页 / 网格 4B，IR1 SL0038GD、IR_R、R3 10kΩ 和 C9 100nF |
| LED1, LED2 | WS2812C-2020 | 两颗由 BAT_ADC/RGB 网络驱动的级联可编程 RGB LED | 图 d38ba3ddf050 / 第 1 页 / 网格 2C-3C，LED1/LED2 WS2812C-2020、BAT_ADC/RGB、DO/DI 和 +3.3V |
| USB1 | TYPE-C 6P | 仅提供 +5VIN 的 USB Type-C 电源输入连接器 | 图 d38ba3ddf050 / 第 1 页 / 网格 1D-2D，USB1 TYPE-C 6P、VBUS、CC1/CC2、R9/R16 和 GND |
| U7 | TP4057 | +5VIN 到 16340_B+ 的单节锂电池充电控制器 | 图 d38ba3ddf050 / 第 1 页 / 网格 2D-3D，U7 TP4057、+5VIN、16340_B+、R17 2.7kΩ 与状态 LED |
| BT1 | Battery | 16340 电池座，正端经 Q3 和 F1 接入 16340_B+ | 图 d38ba3ddf050 / 第 1 页 / 网格 3D-4D，BT1 Battery、Q3、F1 和 GND |
| Q3 | AO3401A | 电池座正端的反接保护 P 沟道 MOSFET | 图 d38ba3ddf050 / 第 1 页 / 网格 3D，BT1 正端与 F1 之间的 Q3 AO3401A，门极接 GND |
| Q1 | AO3401A | 16340_B+ 到 BAT 的高边输出开关 | 图 d38ba3ddf050 / 第 1 页 / 网格 4D，Q1 AO3401A 位于 16340_B+ 与 BAT 之间，门极接 R5/Q2 节点 |
| Q2 | AO3400A | 由 +3.3V 控制并下拉 Q1 门极的 N 沟道 MOSFET | 图 d38ba3ddf050 / 第 1 页 / 网格 4D，Q2 AO3400A、+3.3V、R8 10kΩ、GND 与 Q1 门极节点 |
| F1 | Fuse 0805 2A/6V | 电池正极路径串联保险丝 | 图 d38ba3ddf050 / 第 1 页 / 网格 3D-4D，Q3 与 16340_B+ 之间的 F1 Fuse 0805 2A/6V |

## 系统结构

### BugC2 控制与执行架构

U3 STM32F030F4P6 通过八个 GPIO 控制四颗 L9110S，四颗驱动器分别连接 P1-P4 两针电机接口；同一控制器还连接 I2C、SWD 和 BAT_ADC/RGB 网络。

- 参数与网络：`controller=U3 STM32F030F4P6`；`motor_drivers=U1, U2, U4, U5 L9110S`；`motor_outputs=P1, P2, P3, P4`；`host_interface=P6 STICKIO`；`debug=P5 SWD_5p`
- 证据：图 d38ba3ddf050 / 第 1 页 / 全图 U3 主控、U1/U2/U4/U5 电机驱动、P1-P6 接口及 RGB/红外/电源模块

## 核心器件

### U1 第一电机驱动通道

U1 L9110S 的 IA 接 PA4、IB 接 PA3，OA 接 P1 pin2、OB 接 P1 pin1，两个 VCC 引脚接 BAT，两个 GND 引脚接地。

- 参数与网络：`driver=U1 L9110S`；`ia=PA4`；`ib=PA3`；`oa=P1 pin2`；`ob=P1 pin1`；`supply=BAT`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1A-2A，U1 的 IA/IB/OA/OB/VCC/GND 与 P1

### U2 第二电机驱动通道

U2 L9110S 的 IA 接 PA2、IB 接 PB1，OA 接 P2 pin2、OB 接 P2 pin1，两个 VCC 引脚接 BAT，两个 GND 引脚接地。

- 参数与网络：`driver=U2 L9110S`；`ia=PA2`；`ib=PB1`；`oa=P2 pin2`；`ob=P2 pin1`；`supply=BAT`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 3A-4A，U2 的 IA/IB/OA/OB/VCC/GND 与 P2

### U4 第三电机驱动通道

U4 L9110S 的 IA 接 PA7、IB 接 PA1，OA 接 P3 pin2、OB 接 P3 pin1，两个 VCC 引脚接 BAT，两个 GND 引脚接地。

- 参数与网络：`driver=U4 L9110S`；`ia=PA7`；`ib=PA1`；`oa=P3 pin2`；`ob=P3 pin1`；`supply=BAT`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1A-2B，U4 的 IA/IB/OA/OB/VCC/GND 与 P3

### U5 第四电机驱动通道

U5 L9110S 的 IA 接 PA5、IB 接 PA6，OA 接 P4 pin2、OB 接 P4 pin1，两个 VCC 引脚接 BAT，两个 GND 引脚接地。

- 参数与网络：`driver=U5 L9110S`；`ia=PA5`；`ib=PA6`；`oa=P4 pin2`；`ob=P4 pin1`；`supply=BAT`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 3A-4B，U5 的 IA/IB/OA/OB/VCC/GND 与 P4

## 电源

### TP4057 充电路径

U7 TP4057 的 VCC 接 +5VIN，BAT 输出 16340_B+，PROG 经 R17 2.7kΩ 接地；输入配置 C16 10uF，输出配置 C17 100nF 与 C18 10uF。

- 参数与网络：`charger=U7 TP4057`；`input=+5VIN`；`battery_output=16340_B+`；`program_resistor=R17 2.7kΩ`；`input_capacitor=C16 10uF`；`output_capacitors=C17 100nF, C18 10uF`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2D-3D，U7 VCC/BAT/PROG、+5VIN、16340_B+、R17、C16-C18

### 充电状态指示

U7 CHRG 连接红色 D1 指示支路，U7 STDBY 连接绿色 D2 指示支路；D1 经 R15 2kΩ 接 +5VIN，D2 经 R4 10kΩ 接 +5VIN。

- 参数与网络：`charge_pin=U7 CHRG`；`charge_led=D1 red with R15 2kΩ`；`standby_pin=U7 STDBY`；`standby_led=D2 green with R4 10kΩ`；`supply=+5VIN`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2D，U7 CHRG/STDBY、D1/D2 与 R15/R4

### 电池正极保护路径

BT1 正端经 Q3 AO3401A 和 F1 0805 2A/6V 串联到 16340_B+；Q3 门极接 GND。

- 参数与网络：`path=BT1 positive-Q3-F1-16340_B+`；`reverse_protection=Q3 AO3401A`；`fuse=F1 0805 2A/6V`；`q3_gate=GND`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 3D-4D，BT1、Q3、F1 与 16340_B+ 串联路径

### 16340_B+ 到 BAT 的受控开关

Q1 AO3401A 串联在 16340_B+ 与 BAT 之间，其门极由 R5 100kΩ 上拉到 16340_B+，并由 Q2 AO3400A 下拉；Q2 门极接 +3.3V，R8 10kΩ 将其门极下拉到 GND。

- 参数与网络：`high_side_switch=Q1 AO3401A`；`input=16340_B+`；`output=BAT`；`gate_pullup=R5 100kΩ`；`gate_pulldown_switch=Q2 AO3400A`；`q2_control=+3.3V with R8 10kΩ to GND`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 4D，Q1/Q2、R5/R8、16340_B+、BAT、+3.3V 和 GND

### 主电源域

+5VIN 来自 USB1 或 P6 pin8 并供给 TP4057；+3.3V 来自 P6 pin7 并供给 STM32、红外、RGB 和电池输出控制；BAT 经受控电池路径供给四颗 L9110S。

- 参数与网络：`five_volt_input=+5VIN from USB1 and P6 pin8`；`logic_supply=+3.3V from P6 pin7`；`motor_supply=BAT`；`charger_input=+5VIN`；`battery_switch_control=+3.3V`
- 证据：图 d38ba3ddf050 / 第 1 页 / 全图 +5VIN、+3.3V、BAT、USB1、P6、U7 与四颗 L9110S 电源连接

## 接口

### P6 STICKIO 引脚

P6 pin1=GND、pin2=5VOUT 且外部 +5V 支路标记未连接、pin3=G26/SCL、pin4=G36/IR_R、pin5=G0/SDA、pin6=BAT 且未接线、pin7=+3.3V、pin8=+5VIN。

- 参数与网络：`connector=P6 STICKIO`；`pin1=GND`；`pin2=5VOUT, external +5V branch NC`；`pin3=G26 / SCL`；`pin4=G36 / IR_R`；`pin5=G0 / SDA`；`pin6=BAT, no wire`；`pin7=+3.3V`；`pin8=+5VIN`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 4C，P6 STICKIO 1-8 脚、SCL/IR_R/SDA/+3.3V/+5VIN 及 NC 标记

### USB Type-C 供电输入

USB1 TYPE-C 6P 仅画出 VBUS、CC1、CC2、GND 和 SHELL；两个 VBUS 引脚接 +5VIN，CC1/CC2 分别通过 R9/R16 5.1kΩ 接地。

- 参数与网络：`connector=USB1 TYPE-C 6P`；`output=+5VIN`；`cc1_pulldown=R9 5.1kΩ`；`cc2_pulldown=R16 5.1kΩ`；`data_pins=not shown`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1D-2D，USB1 的全部六针符号、+5VIN、R9/R16 和 GND

## 总线

### STICKIO 到 STM32 的 I2C 总线

P6 pin3 的 SCL 连接 U3 PA9，P6 pin5 的 SDA 连接 U3 PA10；SCL 和 SDA 分别由 R6/R7 10kΩ 上拉到 +3.3V。

- 参数与网络：`connector=P6 STICKIO`；`scl_path=P6 pin3 G26-SCL-U3 PA9`；`sda_path=P6 pin5 G0-SDA-U3 PA10`；`scl_pullup=R6 10kΩ`；`sda_pullup=R7 10kΩ`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2B-4C，U3 PA9/PA10 的 SCL/SDA 与 P6、R6/R7

## GPIO 与控制信号

### 红外输出到主机

IR_R 从 IR1 OUT 直接连接 P6 pin4，对应 STICKIO G36。

- 参数与网络：`source=IR1 OUT`；`net=IR_R`；`host_connector=P6 pin4 G36`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 4B-C，IR1 OUT 的 IR_R 与 P6 pin4 G36 同名网络

### 两颗 WS2812C-2020 级联

BAT_ADC/RGB 接 LED1 DI，LED1 DO 接 LED2 DI，LED2 DO 未继续连接；两颗 LED 均由 +3.3V 供电并接 GND。

- 参数与网络：`first_led=LED1 WS2812C-2020`；`second_led=LED2 WS2812C-2020`；`data_input=BAT_ADC/RGB`；`chain=LED1 DO to LED2 DI`；`supply=+3.3V`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2C-3C，LED1/LED2 的 DI/DO/VDD/GND 与 BAT_ADC/RGB

## 复位

### STM32 复位网络

U3 NRST 由 R2 10kΩ 上拉到 +3.3V，并由 C8 100nF 对地；NRST 同时引出到 P5 pin4。

- 参数与网络：`controller_pin=U3 pin4 NRST`；`pullup=R2 10kΩ`；`capacitor=C8 100nF`；`debug_pin=P5 pin4`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1B-3B，R2/C8/NRST、U3 pin4 与 P5 pin4

### STM32 BOOT0 配置

U3 BOOT0 通过 R1 10kΩ 接 GND。

- 参数与网络：`controller_pin=U3 pin1 BOOT0`；`resistor=R1 10kΩ`；`default_level=GND`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2B，U3 BOOT0、R1 10kΩ 与 GND

## 保护电路

### 电机驱动去耦

四颗 L9110S 的 BAT 电源分别配置 C1-C4 100nF 对地，四个电机输出端 P1-P4 分别跨接 C5、C6、C10、C11 100nF。

- 参数与网络：`bat_decoupling=C1, C2, C3, C4 each 100nF`；`p1_output_capacitor=C5 100nF`；`p2_output_capacitor=C6 100nF`；`p3_output_capacitor=C10 100nF`；`p4_output_capacitor=C11 100nF`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1A-4B，C1-C4 的 BAT 去耦与 P1-P4 两端的 C5/C6/C10/C11

## 关键网络

### PA0 的 BAT_ADC/RGB 复用网络

U3 PA0 与 BAT_ADC/RGB 同网，该网络同时连接电池分压支路和 LED1 DI。

- 参数与网络：`controller_pin=U3 PA0`；`net=BAT_ADC/RGB`；`analog_branch=BAT divider via R11`；`digital_branch=LED1 DI`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2B-4C，U3 PA0、LED1 DI 和 R11 输出均标注 BAT_ADC/RGB

### 四路电机 GPIO 映射

电机控制映射为 U1/P1 使用 PA4 与 PA3，U2/P2 使用 PA2 与 PB1，U4/P3 使用 PA7 与 PA1，U5/P4 使用 PA5 与 PA6。

- 参数与网络：`P1=PA4 IA, PA3 IB`；`P2=PA2 IA, PB1 IB`；`P3=PA7 IA, PA1 IB`；`P4=PA5 IA, PA6 IB`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 1A-4B，U1/U2/U4/U5 的 IA/IB 网络名及 P1-P4 输出

## 传感器

### SL0038GD 红外接收器

IR1 SL0038GD 的 VCC 接 +3.3V、GND 接地、OUT 输出 IR_R；IR_R 由 R3 10kΩ 上拉到 +3.3V，电源配置 C9 100nF 去耦。

- 参数与网络：`reference=IR1`；`part_number=SL0038GD`；`output=IR_R`；`pullup=R3 10kΩ`；`supply=+3.3V`；`decoupling=C9 100nF`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 4B，IR1 的 VCC/OUT/GND、IR_R、R3 和 C9

## 调试与烧录

### SWD 调试接口

P5 pin1=+3.3V、pin2=SWCLK、pin3=SWDIO、pin4=NRST、pin5=GND；SWCLK/SWDIO 分别连接 U3 PA14/PA13。

- 参数与网络：`connector=P5 SWD_5p`；`pin1=+3.3V`；`pin2=SWCLK to U3 PA14`；`pin3=SWDIO to U3 PA13`；`pin4=NRST`；`pin5=GND`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 2B-3B，U3 PA14/PA13/NRST 与 P5 五针引脚

## 模拟电路

### BAT 电压分压采样

BAT 经 R10 100kΩ 与 R12 51kΩ 分压，分压中点再经 R11 330Ω 接 BAT_ADC/RGB，BAT_ADC/RGB 连接 U3 PA0。

- 参数与网络：`source=BAT`；`upper_resistor=R10 100kΩ`；`lower_resistor=R12 51kΩ`；`series_resistor=R11 330Ω`；`controller_pin=U3 PA0`；`net=BAT_ADC/RGB`
- 证据：图 d38ba3ddf050 / 第 1 页 / 网格 3C-4C，BAT、R10/R12/R11、BAT_ADC/RGB 与 U3 PA0

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | BugC2 控制与执行架构 | `controller=U3 STM32F030F4P6`；`motor_drivers=U1, U2, U4, U5 L9110S`；`motor_outputs=P1, P2, P3, P4`；`host_interface=P6 STICKIO`；`debug=P5 SWD_5p` |
| 核心器件 | U1 第一电机驱动通道 | `driver=U1 L9110S`；`ia=PA4`；`ib=PA3`；`oa=P1 pin2`；`ob=P1 pin1`；`supply=BAT` |
| 核心器件 | U2 第二电机驱动通道 | `driver=U2 L9110S`；`ia=PA2`；`ib=PB1`；`oa=P2 pin2`；`ob=P2 pin1`；`supply=BAT` |
| 核心器件 | U4 第三电机驱动通道 | `driver=U4 L9110S`；`ia=PA7`；`ib=PA1`；`oa=P3 pin2`；`ob=P3 pin1`；`supply=BAT` |
| 核心器件 | U5 第四电机驱动通道 | `driver=U5 L9110S`；`ia=PA5`；`ib=PA6`；`oa=P4 pin2`；`ob=P4 pin1`；`supply=BAT` |
| 总线 | STICKIO 到 STM32 的 I2C 总线 | `connector=P6 STICKIO`；`scl_path=P6 pin3 G26-SCL-U3 PA9`；`sda_path=P6 pin5 G0-SDA-U3 PA10`；`scl_pullup=R6 10kΩ`；`sda_pullup=R7 10kΩ` |
| 调试与烧录 | SWD 调试接口 | `connector=P5 SWD_5p`；`pin1=+3.3V`；`pin2=SWCLK to U3 PA14`；`pin3=SWDIO to U3 PA13`；`pin4=NRST`；`pin5=GND` |
| 复位 | STM32 复位网络 | `controller_pin=U3 pin4 NRST`；`pullup=R2 10kΩ`；`capacitor=C8 100nF`；`debug_pin=P5 pin4` |
| 复位 | STM32 BOOT0 配置 | `controller_pin=U3 pin1 BOOT0`；`resistor=R1 10kΩ`；`default_level=GND` |
| 接口 | P6 STICKIO 引脚 | `connector=P6 STICKIO`；`pin1=GND`；`pin2=5VOUT, external +5V branch NC`；`pin3=G26 / SCL`；`pin4=G36 / IR_R`；`pin5=G0 / SDA`；`pin6=BAT, no wire`；`pin7=+3.3V`；`pin8=+5VIN` |
| 传感器 | SL0038GD 红外接收器 | `reference=IR1`；`part_number=SL0038GD`；`output=IR_R`；`pullup=R3 10kΩ`；`supply=+3.3V`；`decoupling=C9 100nF` |
| GPIO 与控制信号 | 红外输出到主机 | `source=IR1 OUT`；`net=IR_R`；`host_connector=P6 pin4 G36` |
| GPIO 与控制信号 | 两颗 WS2812C-2020 级联 | `first_led=LED1 WS2812C-2020`；`second_led=LED2 WS2812C-2020`；`data_input=BAT_ADC/RGB`；`chain=LED1 DO to LED2 DI`；`supply=+3.3V` |
| 模拟电路 | BAT 电压分压采样 | `source=BAT`；`upper_resistor=R10 100kΩ`；`lower_resistor=R12 51kΩ`；`series_resistor=R11 330Ω`；`controller_pin=U3 PA0`；`net=BAT_ADC/RGB` |
| 关键网络 | PA0 的 BAT_ADC/RGB 复用网络 | `controller_pin=U3 PA0`；`net=BAT_ADC/RGB`；`analog_branch=BAT divider via R11`；`digital_branch=LED1 DI` |
| 接口 | USB Type-C 供电输入 | `connector=USB1 TYPE-C 6P`；`output=+5VIN`；`cc1_pulldown=R9 5.1kΩ`；`cc2_pulldown=R16 5.1kΩ`；`data_pins=not shown` |
| 电源 | TP4057 充电路径 | `charger=U7 TP4057`；`input=+5VIN`；`battery_output=16340_B+`；`program_resistor=R17 2.7kΩ`；`input_capacitor=C16 10uF`；`output_capacitors=C17 100nF, C18 10uF` |
| 电源 | 充电状态指示 | `charge_pin=U7 CHRG`；`charge_led=D1 red with R15 2kΩ`；`standby_pin=U7 STDBY`；`standby_led=D2 green with R4 10kΩ`；`supply=+5VIN` |
| 电源 | 电池正极保护路径 | `path=BT1 positive-Q3-F1-16340_B+`；`reverse_protection=Q3 AO3401A`；`fuse=F1 0805 2A/6V`；`q3_gate=GND` |
| 电源 | 16340_B+ 到 BAT 的受控开关 | `high_side_switch=Q1 AO3401A`；`input=16340_B+`；`output=BAT`；`gate_pullup=R5 100kΩ`；`gate_pulldown_switch=Q2 AO3400A`；`q2_control=+3.3V with R8 10kΩ to GND` |
| 电源 | 主电源域 | `five_volt_input=+5VIN from USB1 and P6 pin8`；`logic_supply=+3.3V from P6 pin7`；`motor_supply=BAT`；`charger_input=+5VIN`；`battery_switch_control=+3.3V` |
| 保护电路 | 电机驱动去耦 | `bat_decoupling=C1, C2, C3, C4 each 100nF`；`p1_output_capacitor=C5 100nF`；`p2_output_capacitor=C6 100nF`；`p3_output_capacitor=C10 100nF`；`p4_output_capacitor=C11 100nF` |
| 关键网络 | 四路电机 GPIO 映射 | `P1=PA4 IA, PA3 IB`；`P2=PA2 IA, PB1 IB`；`P3=PA7 IA, PA1 IB`；`P4=PA5 IA, PA6 IB` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d38ba3ddf0500bde295da2fabc0651b10f55d70fb23bcfe0fbb365b939921aaf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/SCH_BugC2_V1.0_sch_01.png` |

---

源文档：`zh_CN/app/BUGC2.md`

源文档 SHA-256：`4fce496285880f264b204d4e9d4065267ea27417205ef941532baedd261da7f2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
