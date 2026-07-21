# Atomic Motion Base v1.2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Motion Base v1.2 |
| SKU | A090-V12 |
| 产品 ID | `atomic-motion-base-v1-2-f5b15b53f382` |
| 源文档 | `zh_CN/atom/Atomic_Motion_Base_v1.2.md` |

## 概述

Atomic Motion Base v1.2 以 U3 STM32F030F4P6 为运动控制器，通过 SCL/SDA 连接 Atom 主机和 U5 INA226，并控制四路舵机及两颗 RZ7899 直流电机驱动器。U1 ETA9740 从 BAT+ 生成 5V，电池正端经 Q1、R3 20mΩ采样电阻形成 BAT+，负端经 6V/5A 保险、S1 和 U6 DW01-A 控制的 Q2/Q3 保护链接入 GND。两组 Grove 分别引出 G23/G33 和 G22/G19，STM32 另提供独立 SWD 接口。产品正文的 0x38 固件协议、18350@900mAh、电气额定值和保护阈值无法仅由原理图确认，且电机区块标题与 M1/M2 控制网络编号需要核对。

## 检索关键词

`Atomic Motion Base v1.2`、`A090-V12`、`STM32F030F4P6`、`ETA9740`、`RZ7899`、`INA226AIDGSR`、`DW01-A`、`LP3218DT1G`、`LN2324DT2AG`、`I2C`、`0x38`、`SCL`、`SDA`、`G21`、`G25`、`M1F`、`M1R`、`M2F`、`M2R`、`PA0`、`PA1`、`PA2`、`PA3`、`BAT+`、`IN_P`、`B-`、`5V`、`3V3`、`20mR shunt`、`16340`、`18350`、`SWDIO`、`SWCLK`、`NRST`、`Grove PortB`、`Grove PortC`、`DC motor`、`servo`、`battery protection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 运动控制器，输出四路舵机和两组电机控制信号，并连接 SWD 与复位 | 图 b19d83f11321 / 第 1 页 / 第 1 页 B2-B3 区 U3 STM32F030F4P6，PA/PB、SCL/SDA、SWDIO/SWCLK、NRST、BOOT0 和电源地 |
| U1 | ETA9740 | BAT+ 到 5V 的充电与升压电源电路核心，并连接充电状态 LED | 图 b19d83f11321 / 第 1 页 / 第 1 页 A1-A2 区 Charger&Boost，U1 ETA9740、L1、BAT+/5V 与 LED1 |
| U2,U4 | RZ7899 | 两路直流电机驱动器，分别受 M2F/M2R 和 M1F/M1R 网络控制 | 图 b19d83f11321 / 第 1 页 / 第 1 页 B1 区 U2/U4 RZ7899，OUTF/OUTR、INF/INR、BAT+/GND 与 JP1/JP2 |
| U5 | INA226AIDGSR | 跨 IN_P 与 BAT+ 采样路径的电流、电压监测器，并连接共享 SCL/SDA 总线 | 图 b19d83f11321 / 第 1 页 / 第 1 页 C3-D4 区 U5 INA226AIDGSR，SCL/SDA、VBUS/IN+/IN-、VS、A1/A0、ALERT 与 GND |
| U6 | DW01-A | 监测 IN_P 与 B- 并通过 OD/OC 控制负端保护 MOSFET | 图 b19d83f11321 / 第 1 页 / 第 1 页 A3-A4 区 Battery protection，U6 DW01-A 的 VDD/VSS/VM/OD/OC 与外围 |
| Q1 | LP3218DT1G | 位于 BT1 正端与 IN_P 之间的受控电源路径器件 | 图 b19d83f11321 / 第 1 页 / 第 1 页 A2-A3 区 Q1 LP3218DT1G，串联在 BT1 正端与 IN_P 之间 |
| Q2,Q3 | LN2324DT2AG | 受 U6 OD/OC 控制、串联在 B- 与 GND 之间的背靠背保护 MOSFET | 图 b19d83f11321 / 第 1 页 / 第 1 页 A3-A4 区 Q2/Q3 LN2324DT2AG，从 B- 串联到 GND，栅极分别接 U6 OD/OC |
| R3 | 20mR/1206 | IN_P 与 BAT+ 之间的电流采样分流电阻 | 图 b19d83f11321 / 第 1 页 / 第 1 页 A2-A3 区 R3 20mR/1206 Shunt Resistor，连接 IN_P 与 BAT+ |
| BT1 | 16340 | 原理图标注的可拆卸单节电池位 | 图 b19d83f11321 / 第 1 页 / 第 1 页 A2-A3 区 BT1，电池符号下明确标注 16340 |
| S1,Fuse | 6V/5A (Fuse) | BT1 负端到 B- 的电源开关与串联保险路径 | 图 b19d83f11321 / 第 1 页 / 第 1 页 A2 区 S1 与 Fuse 6V/5A，连接 BT1 负端和 B- |
| JP1,JP2 | 未标注 | U2/U4 两路 RZ7899 的两针直流电机输出接口 | 图 b19d83f11321 / 第 1 页 / 第 1 页 B1 区 JP1/JP2 两针接口与 U2/U4 OUTF/OUTR |
| JP3-JP6 | 未标注 | 四组三针舵机接口，每组包含 MCU 控制信号、BAT+ 和 GND | 图 b19d83f11321 / 第 1 页 / 第 1 页 B1-C2 区 JP3-JP6 三针接口与 PA0-PA3、BAT+、GND |
| ATOM | ATOM | 连接 Atom 主控的 3V3、I2C、5V、GND 和 G22/G19/G23/G33 信号 | 图 b19d83f11321 / 第 1 页 / 第 1 页 C2 区 ATOM 9 针连接器，G21/G25/5V/GND/3V3/G22/G19/G23/G33 |
| J1,J2 | GROVE-B / GROVE-C | 两组 5V Grove 扩展接口，分别引出 G23/G33 与 G22/G19 | 图 b19d83f11321 / 第 1 页 / 第 1 页 C2-C3 区 J1/J2 GROVE-B/GROVE-C，IO2/IO1/5V/GND |
| J3 | SWD | STM32 的 NRST、SWCLK、SWDIO、3V3 和 GND 调试接口 | 图 b19d83f11321 / 第 1 页 / 第 1 页 B3 区 J3 SWD，RST/CLK/DIO/VCC/GND 与 NRST/SWCLK/SWDIO/3V3 |
| D1 | DSS34 | BAT+ 到 GND 的二极管 | 图 b19d83f11321 / 第 1 页 / 第 1 页 C4 区 D1 DSS34，从 BAT+ 接到 GND |

## 系统结构

### Atomic Motion Base v1.2 系统架构

U3 STM32F030F4P6 通过 SCL/SDA 连接 Atom 主机和 U5 INA226，输出四路舵机控制，并以 M1F/M1R/M2F/M2R 驱动 U4/U2 两颗 RZ7899；U1 ETA9740 从 BAT+ 生成 5V，U6 DW01-A 控制电池负端保护链。

- 参数与网络：`controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`power_monitor=U5 INA226AIDGSR`；`battery_protection=U6 DW01-A with Q2/Q3`；`motor_drivers=U4/U2 RZ7899`；`motor_channels=2`；`servo_channels=4`；`five_volt_converter=U1 ETA9740`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页完整单页：Charger&Boost、Battery、Battery protection、Motor/Servo、U3、ATOM/Grove、U5/SWD

## 核心器件

### STM32F030F4P6 运动控制器

U3 由 3V3 供电，连接 PA0-PA3 舵机信号、M1F/M1R/M2F/M2R 电机控制、SCL/SDA、SWDIO/SWCLK 和 NRST；BOOT0 与 VSS 接 GND，PF0/PF1 未连接。

- 参数与网络：`reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA pin5 and VDD pin16 to 3V3; VSS pin15 to GND`；`servo_gpio=PA0,PA1,PA2,PA3`；`motor_nets=M1F,M1R,M2F,M2R`；`i2c=PA9 SCL, PA10 SDA`；`debug=PA13 SWDIO, PA14 SWCLK, NRST`；`boot0=GND`；`oscillator_pins=PF0/PF1 unconnected`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B2-B3 区 U3 STM32F030F4P6 全部已连接网络和未连接引脚

## 电源

### BT1 到 BAT+ 与 B- 的开关采样路径

BT1 正端经 Q1 LP3218DT1G 到 IN_P，再经 R3 20mΩ/1206 到 BAT+；BT1 负端经 Fuse 6V/5A 到 S1 pin2，S1 pin1 接 B-，Q1 控制端接 BT1 负端/Fuse 节点。

- 参数与网络：`cell=BT1 16340`；`positive_path=BT1+ -> Q1 -> IN_P -> R3 20mR/1206 -> BAT+`；`negative_path=BT1- -> Fuse 6V/5A -> S1 pin2; S1 pin1 -> B-`；`switch=S1`；`path_device=Q1 LP3218DT1G`；`sense_resistor=R3 20mR/1206`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 A2-A3 区 S1/Fuse/BT1/Q1/IN_P/R3/BAT+ 连线

### BAT+ 到 5V 转换

U1 ETA9740 的 BAT/SW 侧连接 BAT+ 和 L1 3.3uH/4012，OUT pin7 形成 5V；ISET pin5 经 R2 150K 接 GND，LED1 pin2 经 R1 1K 和 LED1 接到 LED3 pin4。

- 参数与网络：`converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 106, C2 475`；`output_caps=C3/C4/C5 106, C11 104`；`iset=R2 150K`；`indicator=R1 1K and LED1 between LED1/LED3 pins`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 A1-A2 区 U1 ETA9740、L1、R1/R2、LED1、C1-C5/C11 与 BAT+/5V

### 5V、3V3 与 BAT+ 负载分配

5V 连接 ATOM pin3、J1/J2 Grove pin2 和 C7；3V3 连接 ATOM pin9、U3 VDDA/VDD、U5 VS、J3 VCC 及相关去耦；BAT+ 连接 U1 输入、U2/U4 VCC、JP3-JP6 舵机电源和 D1。

- 参数与网络：`5V=ATOM pin3, J1/J2 pin2, C7`；`3V3=ATOM pin9, U3 VDDA/VDD, U5 VS, J3 VCC, C8/C9/C10/C13`；`BAT+=U1 BAT/SW, U2/U4 VCC, JP3-JP6 power, D1`；`five_volt_decoupling=C7 475`；`three_volt_decoupling=C8 475, C9/C10 104`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页各区域的 5V、3V3、BAT+ 同名网络及 C3-C4 区 C7-C10/D1

## 接口

### JP1/JP2 直流电机输出

U4 RZ7899 的并联 OUTF pins5/6 与 OUTR pins7/8 连接 JP2，两颗输入分别为 M1F/M1R；U2 的同类输出连接 JP1，输入分别为 M2F/M2R；两颗驱动器 VCC pin4 接 BAT+、GND pin3 接地。

- 参数与网络：`M1_control=U4 M1F/M1R -> JP2`；`M2_control=U2 M2F/M2R -> JP1`；`output_forward=OUTF pins5/6`；`output_reverse=OUTR pins7/8`；`supply=BAT+`；`ground=GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B1 区 U2/U4 RZ7899 与 JP1/JP2、BAT+/GND、M1F/M1R/M2F/M2R

### JP3-JP6 舵机接口

JP3/JP4 的 pin3 为控制、pin2 为 BAT+、pin1 为 GND；JP5/JP6 的 pin1 为控制、pin2 为 BAT+、pin3 为 GND。

- 参数与网络：`JP3=pin3 signal PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 signal PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 signal PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 signal PA3, pin2 BAT+, pin3 GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B1-C2 区 JP3-JP6 的 pin1-pin3 标号、BAT+/GND 与控制线

### ATOM 9 针主机接口

ATOM 左侧 pins7/5/3/1 分别为 G21 SCL、G25 SDA、5V、GND；右侧 pins9/8/6/4/2 分别为 3V3、G22、G19、G23、G33。

- 参数与网络：`pin1=GND`；`pin2=G33`；`pin3=5V`；`pin4=G23`；`pin5=G25 SDA`；`pin6=G19`；`pin7=G21 SCL`；`pin8=G22`；`pin9=3V3`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 C2 区 ATOM 连接器的 pin1-pin9 与网络标签

### J1 Grove PortB

J1 pin4 IO2 连接 ATOM G23，pin3 IO1 连接 G33，pin2 接 5V，pin1 接 GND。

- 参数与网络：`pin4_io2=G23`；`pin3_io1=G33`；`pin2=5V`；`pin1=GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 C2 区 J1 GROVE-B PortB 与 ATOM G23/G33/5V/GND

### J2 Grove PortC

J2 pin4 IO2 连接 ATOM G22，pin3 IO1 连接 G19，pin2 接 5V，pin1 接 GND。

- 参数与网络：`pin4_io2=G22`；`pin3_io1=G19`；`pin2=5V`；`pin1=GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 C2-C3 区 J2 GROVE-C PortC 与 ATOM G22/G19/5V/GND

## 总线

### Atom、STM32 与 INA226 共用 I2C

ATOM pin7 G21 连接 SCL 到 U3 PA9 pin17 和 U5 SCL pin5；ATOM pin5 G25 连接 SDA 到 U3 PA10 pin18 和 U5 SDA pin4；R5/R4 各 4.7K 将 SCL/SDA 上拉到 3V3。

- 参数与网络：`host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`monitor_scl=U5 pin5`；`scl_pullup=R5 4.7K to 3V3`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18`；`monitor_sda=U5 pin4`；`sda_pullup=R4 4.7K to 3V3`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 U3 PA9/PA10、ATOM G21/G25、U5 pins5/4 与 R5/R4 的 SCL/SDA 同名网络

## 总线地址

### INA226 地址绑带

U5 A1 pin1 直接接 GND，A0 pin2 经 R10 10K 接 GND；原理图未直接标注该绑带对应的 I2C 地址。

- 参数与网络：`A1_pin1=GND`；`A0_pin2=R10 10K to GND`；`address_label_on_schematic=null`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 D3 区 U5 A1/A0 与 GND、R10 10K

## GPIO 与控制信号

### 四路舵机 GPIO 映射

U3 PA0 pin6、PA1 pin7、PA2 pin8、PA3 pin9 分别连接 Servo3 JP3、Servo1 JP4、Servo4 JP5、Servo2 JP6 的控制信号；四个接口另外连接 BAT+ 和 GND。

- 参数与网络：`PA0_pin6=JP3 Servo3 signal pin3`；`PA1_pin7=JP4 Servo1 signal pin3`；`PA2_pin8=JP5 Servo4 signal pin1`；`PA3_pin9=JP6 Servo2 signal pin1`；`servo_power=BAT+`；`servo_ground=GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B1-C2 区 U3 PA0-PA3 到 JP3-JP6 的长连线与各接口 pin1-pin3

### 两路电机 GPIO 映射

U3 PA4 pin10 连接 M1F，PB1 pin14 连接 M1R，驱动 U4 INF/INR；PA6 pin12 连接 M2F，PA7 pin13 连接 M2R，驱动 U2 INF/INR；PA5 pin11 标为未连接。

- 参数与网络：`PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1`；`PA5_pin11=NC`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B1-B2 区 U3 PA4/PB1/PA6/PA7 与 U4/U2 的 M1F/M1R/M2F/M2R

## 保护电路

### DW01-A 电池负端保护拓扑

U6 VDD pin5 经 R11 330Ω接 IN_P，VSS pin6 接 B-，C14 104 跨 VDD 与 B-；VM pin2 经 R12 2.2K 接 GND，OD pin1 与 OC pin3 分别控制 Q2/Q3，Q2/Q3 串联在 B- 与 GND 之间。

- 参数与网络：`controller=U6 DW01-A`；`supply=IN_P -> R11 330R -> VDD pin5`；`reference=VSS pin6 -> B-`；`filter=C14 104 between VDD and B-`；`vm=pin2 -> R12 2.2K -> GND`；`od=pin1 -> Q2 gate`；`oc=pin3 -> Q3 gate`；`switch_path=B- -> Q2/Q3 LN2324DT2AG -> GND`；`nc=pin4 unconnected`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 A3-A4 区 U6、R11/R12、C14、Q2/Q3 与 IN_P/B-/GND

## 传感器

### U5 INA226 电源监测路径

U5 VBUS pin8 与 IN+ pin10 同接一节点并经 R6 10R 到 IN_P；IN- pin9 经 R7 10R 到 BAT+，C12 104 跨接 IN+ 与 IN-；VS pin6 接 3V3，GND pin7 接地。

- 参数与网络：`part_number=INA226AIDGSR`；`vbus=pin8 tied to IN+ node`；`in_plus=pin10 -> R6 10R -> IN_P`；`in_minus=pin9 -> R7 10R -> BAT+`；`input_filter=C12 104 across IN+/IN-`；`external_shunt=R3 20mR/1206 between IN_P and BAT+`；`supply=VS pin6 3V3 with C13 106`；`ground=pin7 GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 C3-D4 区 U5 VBUS/IN+/IN-、R6/R7、C12、R3 与 IN_P/BAT+

## 调试与烧录

### STM32 SWD 与复位

J3 引出 NRST、SWCLK、SWDIO、3V3 和 GND；U3 PA13/SWDIO、PA14/SWCLK 和 NRST 分别连接这些网络，R9 10K 将 NRST 上拉到 3V3，C6 104 从 NRST 接地。

- 参数与网络：`connector=J3 SWD`；`signals=NRST,SWCLK,SWDIO,3V3,GND`；`debug_pins=PA13/SWDIO pin19, PA14/SWCLK pin20`；`reset_pin=NRST pin4`；`reset_pullup=R9 10K to 3V3`；`reset_capacitor=C6 104 to GND`
- 证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B2-B3 区 U3 SWDIO/SWCLK/NRST 与 J3/R9/C6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Motion Base v1.2 系统架构 | `controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`power_monitor=U5 INA226AIDGSR`；`battery_protection=U6 DW01-A with Q2/Q3`；`motor_drivers=U4/U2 RZ7899`；`motor_channels=2`；`servo_channels=4`；`five_volt_converter=U1 ETA9740` |
| 电源 | BT1 到 BAT+ 与 B- 的开关采样路径 | `cell=BT1 16340`；`positive_path=BT1+ -> Q1 -> IN_P -> R3 20mR/1206 -> BAT+`；`negative_path=BT1- -> Fuse 6V/5A -> S1 pin2; S1 pin1 -> B-`；`switch=S1`；`path_device=Q1 LP3218DT1G`；`sense_resistor=R3 20mR/1206` |
| 保护电路 | DW01-A 电池负端保护拓扑 | `controller=U6 DW01-A`；`supply=IN_P -> R11 330R -> VDD pin5`；`reference=VSS pin6 -> B-`；`filter=C14 104 between VDD and B-`；`vm=pin2 -> R12 2.2K -> GND`；`od=pin1 -> Q2 gate`；`oc=pin3 -> Q3 gate`；`switch_path=B- -> Q2/Q3 LN2324DT2AG -> GND`；`nc=pin4 unconnected` |
| 电源 | BAT+ 到 5V 转换 | `converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 106, C2 475`；`output_caps=C3/C4/C5 106, C11 104`；`iset=R2 150K`；`indicator=R1 1K and LED1 between LED1/LED3 pins` |
| 电源 | 5V、3V3 与 BAT+ 负载分配 | `5V=ATOM pin3, J1/J2 pin2, C7`；`3V3=ATOM pin9, U3 VDDA/VDD, U5 VS, J3 VCC, C8/C9/C10/C13`；`BAT+=U1 BAT/SW, U2/U4 VCC, JP3-JP6 power, D1`；`five_volt_decoupling=C7 475`；`three_volt_decoupling=C8 475, C9/C10 104` |
| 核心器件 | STM32F030F4P6 运动控制器 | `reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA pin5 and VDD pin16 to 3V3; VSS pin15 to GND`；`servo_gpio=PA0,PA1,PA2,PA3`；`motor_nets=M1F,M1R,M2F,M2R`；`i2c=PA9 SCL, PA10 SDA`；`debug=PA13 SWDIO, PA14 SWCLK, NRST`；`boot0=GND`；`oscillator_pins=PF0/PF1 unconnected` |
| 总线 | Atom、STM32 与 INA226 共用 I2C | `host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`monitor_scl=U5 pin5`；`scl_pullup=R5 4.7K to 3V3`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18`；`monitor_sda=U5 pin4`；`sda_pullup=R4 4.7K to 3V3` |
| 总线 | 正文中的 STM32 I2C 地址与寄存器 | `documented_address=0x38`；`servo_angle_registers=0x00-0x03`；`servo_pulse_registers=0x10,0x12,0x14,0x16`；`motor_registers=0x20-0x21`；`schematic_setting=null` |
| GPIO 与控制信号 | 四路舵机 GPIO 映射 | `PA0_pin6=JP3 Servo3 signal pin3`；`PA1_pin7=JP4 Servo1 signal pin3`；`PA2_pin8=JP5 Servo4 signal pin1`；`PA3_pin9=JP6 Servo2 signal pin1`；`servo_power=BAT+`；`servo_ground=GND` |
| GPIO 与控制信号 | 两路电机 GPIO 映射 | `PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1`；`PA5_pin11=NC` |
| 接口 | JP1/JP2 直流电机输出 | `M1_control=U4 M1F/M1R -> JP2`；`M2_control=U2 M2F/M2R -> JP1`；`output_forward=OUTF pins5/6`；`output_reverse=OUTR pins7/8`；`supply=BAT+`；`ground=GND` |
| 接口 | 电机区块标题与控制网络编号 | `block_motor2=U4/JP2 with M1F/M1R`；`block_motor1=U2/JP1 with M2F/M2R`；`resolved_external_channel=null` |
| 接口 | JP3-JP6 舵机接口 | `JP3=pin3 signal PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 signal PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 signal PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 signal PA3, pin2 BAT+, pin3 GND` |
| 接口 | ATOM 9 针主机接口 | `pin1=GND`；`pin2=G33`；`pin3=5V`；`pin4=G23`；`pin5=G25 SDA`；`pin6=G19`；`pin7=G21 SCL`；`pin8=G22`；`pin9=3V3` |
| 接口 | J1 Grove PortB | `pin4_io2=G23`；`pin3_io1=G33`；`pin2=5V`；`pin1=GND` |
| 接口 | J2 Grove PortC | `pin4_io2=G22`；`pin3_io1=G19`；`pin2=5V`；`pin1=GND` |
| 传感器 | U5 INA226 电源监测路径 | `part_number=INA226AIDGSR`；`vbus=pin8 tied to IN+ node`；`in_plus=pin10 -> R6 10R -> IN_P`；`in_minus=pin9 -> R7 10R -> BAT+`；`input_filter=C12 104 across IN+/IN-`；`external_shunt=R3 20mR/1206 between IN_P and BAT+`；`supply=VS pin6 3V3 with C13 106`；`ground=pin7 GND` |
| 总线地址 | INA226 地址绑带 | `A1_pin1=GND`；`A0_pin2=R10 10K to GND`；`address_label_on_schematic=null` |
| 调试与烧录 | STM32 SWD 与复位 | `connector=J3 SWD`；`signals=NRST,SWCLK,SWDIO,3V3,GND`；`debug_pins=PA13/SWDIO pin19, PA14/SWCLK pin20`；`reset_pin=NRST pin4`；`reset_pullup=R9 10K to 3V3`；`reset_capacitor=C6 104 to GND` |
| 电源 | 产品正文中的电池规格 | `schematic_cell=BT1 16340`；`schematic_capacity=null`；`documented_cell=18350`；`documented_capacity=900mAh`；`conflict=true` |
| 电源 | 产品正文中的电气额定值 | `documented_overload=5V@5A`；`documented_full_load=3A`；`documented_motor_peak=1A per channel`；`documented_servo_peak=0.4A per channel`；`documented_charge_current=1.18A at 5V`；`documented_standby_current=40.97uA at 4.04V`；`schematic_fuse=6V/5A`；`schematic_shunt=R3 20mR/1206` |
| 保护电路 | 产品正文中的电池保护阈值与功能 | `documented_charge_cutoff=4.14V`；`documented_discharge_cutoff=2.5V`；`documented_functions=overcharge, overdischarge, short-circuit protection`；`schematic_thresholds=null` |

## 待确认事项

- `bus.documented-i2c-protocol`：产品正文给出 I2C 地址 0x38，以及舵机 0x00-0x03/0x10-0x16 和电机 0x20-0x21 寄存器；原理图只显示 STM32 的 SCL/SDA 物理连接，无法验证固件地址和寄存器语义。（证据：图 b19d83f11321 / 第 1 页 / 第 1 页 U3 SCL/SDA 与 ATOM G21/G25，图中无 STM32 地址或固件寄存器设定）
- `interface.motor-label-conflict`：原理图将 U4/JP2 区块标题写为 Motor2，但输入网络为 M1F/M1R；将 U2/JP1 区块标题写为 Motor1，但输入网络为 M2F/M2R，因此外部通道编号应以固件和板端丝印进一步确认。（证据：图 b19d83f11321 / 第 1 页 / 第 1 页 B1 区蓝色 Motor2/Motor1 标题、U4/U2、JP2/JP1 与 M1F/M1R/M2F/M2R）
- `power.documented-battery-spec`：产品正文和包装内容称电池为 18350@900mAh，但原理图 BT1 标注 16340 且未标容量；电池规格和当前硬件版本的对应关系无法由现有图纸确认。（证据：图 b19d83f11321 / 第 1 页 / 第 1 页 A2-A3 区 BT1 仅标注 16340，未标容量）
- `power.documented-current-ratings`：正文给出 5V@5A 过载保护、3A 满负荷、单电机峰值 1A、单舵机峰值 0.4A、5V@1.18A 充电电流和 4.04V@40.97uA 待机电流；原理图仅标 Fuse 6V/5A、R3 20mΩ和负载连接，无法验证这些系统级额定值及测试条件。（证据：图 b19d83f11321 / 第 1 页 / 第 1 页 Fuse 6V/5A、R3 20mR、U1、RZ7899 和 JP3-JP6，图中无整机测试条件）
- `protection.documented-cutoffs`：正文称 DW01-A 提供过充、过放和短路保护，并给出 4.14V 充电截止与 2.5V 放电截止；原理图确认 U6/Q2/Q3 保护拓扑，但未标注阈值或具体保护动作条件。（证据：图 b19d83f11321 / 第 1 页 / 第 1 页 A3-A4 区 U6 DW01-A、Q2/Q3 与 R11/R12/C14，图中无保护阈值）
- `review.i2c-firmware-protocol`：A090-V12 当前 STM32 固件是否确认为 I2C 地址 0x38，并实现正文所列舵机与电机寄存器映射？；原因：地址与寄存器由固件决定，原理图只确认 SCL/SDA 物理连接；U5 INA226 还与 STM32 共用该总线。
- `review.motor-channel-labels`：A090-V12 的 JP1/JP2 板端丝印和固件 Motor1/Motor2 定义，究竟按区块标题还是按 M1F/M1R、M2F/M2R 网络编号？；原因：原理图区块标题与控制网络编号交叉，不能仅凭图中一个标签确定对外通道编号。
- `review.battery-spec-conflict`：A090-V12 量产 BOM 和结构件使用 16340 还是 18350 电池，配套容量是否为 900mAh？；原因：产品正文称 18350@900mAh，原理图 BT1 却标 16340；需要当前版本 BOM、结构图或实物确认。
- `review.current-ratings`：5V@5A 过载、3A 满负荷、1A 单电机、0.4A 单舵机、1.18A 充电和 40.97uA 待机的持续/峰值定义及测试条件是什么？；原因：原理图连接、保险和采样电阻标称不能单独证明整机额定能力，需要器件规格、BOM 和测试记录。
- `review.battery-protection-thresholds`：A090-V12 的 DW01-A 具体料号后缀、保护阈值以及 4.14V/2.5V 截止参数是否与当前 BOM 和实测一致？；原因：原理图只给出 DW01-A 名称与外围拓扑，没有阈值、延时、短路判定或温度条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b19d83f1132169505fa2d0c4a30ba7e0547cb565731786f6b2a49c605fb11f46` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_schematic_page_01.png` |

---

源文档：`zh_CN/atom/Atomic_Motion_Base_v1.2.md`

源文档 SHA-256：`f81e6438d06a5e1e807e91c0dc5ad906d776eb726f7f051c42eff9a81d3c38fc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
