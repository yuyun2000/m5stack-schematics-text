# Atomic Motion Base v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Motion Base v1.1 |
| SKU | A090-V11 |
| 产品 ID | `atomic-motion-base-v1-1-5a63ca566c77` |
| 源文档 | `zh_CN/atom/Atomic Motion Base v1.1.md` |

## 概述

Atomic Motion Base v1.1 以 U3 STM32F030F4P6 为控制器，通过 ATOM G21/G25 的 SCL/SDA 与主机通信，并输出四路舵机和两组 RZ7899 电机控制信号。U1 ETA9740 从 BAT+ 生成 5V；BT1、S1、5A 保险、Q1、R3 20mΩ 和 U5 INA226AIDGSR 构成电池开关、采样与监测路径。两组 Grove 分别引出 G23/G33 和 G22/G19。正文中的 0x38 固件地址、寄存器、18350@900mAh 与系统级电流额定值无法仅由原理图确认，其中电池位与图中 BT1 16340 标注不一致。

## 检索关键词

`Atomic Motion Base v1.1`、`A090-V11`、`STM32F030F4P6`、`ETA9740`、`RZ7899`、`INA226AIDGSR`、`LP3218DT1G`、`I2C`、`0x38`、`SCL`、`SDA`、`G21`、`G25`、`M1F`、`M1R`、`M2F`、`M2R`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA6`、`PA7`、`PB1`、`BAT+`、`IN_P`、`5V`、`3V3`、`16340`、`18350`、`SWDIO`、`SWCLK`、`NRST`、`Grove`、`DC motor`、`servo`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 运动控制器，输出四路舵机和两路电机控制信号，并连接 SWD 与复位 | 图 42f23cce107e / 第 1 页 / 第 1 页 B2-B3 区 U3 STM32F030F4P6，PA/PB、SCL/SDA、SWDIO/SWCLK、NRST、BOOT0 和电源地 |
| U1 | ETA9740 | BAT+ 到 5V 的开关电源转换器，并连接充电状态 LED | 图 42f23cce107e / 第 1 页 / 第 1 页 A1-A2 区 U1 ETA9740，BAT/SW/OUT/ISET/LED1-3、L1 与 BAT+/5V |
| U2,U4 | RZ7899 | 两路直流电机驱动器，分别连接 M2F/M2R 与 M1F/M1R | 图 42f23cce107e / 第 1 页 / 第 1 页 B1 区 U2/U4 RZ7899，OUTF/OUTR、INF/INR、BAT+/GND 与 JP1/JP2 |
| U5 | INA226AIDGSR | 跨 IN_P 与 BAT+ 的电流、电压监测器，共用 SCL/SDA 总线 | 图 42f23cce107e / 第 1 页 / 第 1 页 B3-B4 区 U5 INA226AIDGSR，SCL/SDA、VBUS/IN+/IN-、VS、A1/A0、ALERT 与 GND |
| BT1 | 16340 | 原理图标注的可拆卸电池位，正端连接 Q1，负端连接电源开关与保险路径 | 图 42f23cce107e / 第 1 页 / 第 1 页 A2-A3 区 BT1 16340、S1、Fuse、Q1、IN_P、R3 与 BAT+ |
| Q1 | LP3218DT1G | BT1 正端到 IN_P 电源路径中的开关器件 | 图 42f23cce107e / 第 1 页 / 第 1 页 A2 区 Q1 LP3218DT1G 位于 BT1 正端与 IN_P 之间，控制端接电池负端/Fuse 节点 |
| S1,Fuse | SS-12F23 / 5A | 电池负端到 GND 的滑动开关与串联保险路径 | 图 42f23cce107e / 第 1 页 / 第 1 页 A2 区 S1 SS-12F23 pin2 接 GND，pin3 经 Fuse 5A 接 BT1 负端 |
| JP1,JP2 | 未标注 | U2/U4 两路 RZ7899 的两针直流电机输出接口 | 图 42f23cce107e / 第 1 页 / 第 1 页 B1 区 JP1/JP2 两针接口与 U2/U4 OUTF/OUTR |
| JP3-JP6 | 未标注 | 四组三针舵机接口，每组包含 MCU 控制信号、BAT+ 和 GND | 图 42f23cce107e / 第 1 页 / 第 1 页 B1-C2 区 JP3-JP6 三针接口与 PA0-PA3、BAT+、GND |
| ATOM | ATOM | 连接 Atom 主控的 3V3、I2C、5V、GND 和 G22/G19/G23/G33 信号 | 图 42f23cce107e / 第 1 页 / 第 1 页 C2 区 ATOM 9 针连接器，G21/G25/5V/GND/3V3/G22/G19/G23/G33 |
| J1,J2 | GROVE | 两组 5V Grove 扩展接口，分别引出 G23/G33 与 G22/G19 | 图 42f23cce107e / 第 1 页 / 第 1 页 C2-C3 区 J1/J2 GROVE，IO2/IO1/5V/GND 与 ATOM 网络 |
| J3 | SWD | STM32 的 NRST、SWCLK、SWDIO、3V3 和 GND 调试接口 | 图 42f23cce107e / 第 1 页 / 第 1 页 B3 区 J3 SWD，RST/CLK/DIO/VCC/GND 与 NRST/SWCLK/SWDIO/3V3 |
| D1 | DSS34 | BAT+ 到 GND 的二极管 | 图 42f23cce107e / 第 1 页 / 第 1 页 A4 区 D1 DSS34 从 BAT+ 接到 GND |

## 系统结构

### Atomic Motion Base v1.1 系统架构

U3 STM32F030F4P6 通过 SCL/SDA 连接 Atom 主机和 U5 INA226，直接输出四路舵机控制，并以 M1F/M1R/M2F/M2R 驱动 U4/U2 两颗 RZ7899；U1 ETA9740 从 BAT+ 生成 5V。

- 参数与网络：`controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`power_monitor=U5 INA226AIDGSR`；`motor_drivers=U4/U2 RZ7899`；`motor_channels=2`；`servo_channels=4`；`battery_rail=BAT+`；`five_volt_converter=U1 ETA9740`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页完整单页：电源、U2/U4 电机、U3 MCU、U5 INA226、JP3-JP6 舵机、ATOM/Grove/SWD

## 核心器件

### STM32F030F4P6 运动控制器

U3 由 3V3 供电，连接 PA0-PA3 舵机信号、M1F/M1R/M2F/M2R 电机控制、SCL/SDA、SWDIO/SWCLK 和 NRST；BOOT0 与 VSS 接 GND，PF0/PF1 未连接。

- 参数与网络：`reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA pin5 and VDD pin16 to 3V3; VSS pin15 to GND`；`servo_gpio=PA0,PA1,PA2,PA3`；`motor_nets=M1F,M1R,M2F,M2R`；`i2c=PA9 SCL, PA10 SDA`；`debug=PA13 SWDIO, PA14 SWCLK, NRST`；`boot0=GND`；`oscillator_pins=PF0/PF1 NC`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B2-B3 区 U3 STM32F030F4P6 全部已连接网络与 NC 标记

## 电源

### BT1 到 BAT+ 的开关与采样路径

BT1 正端经 Q1 LP3218DT1G 到 IN_P，再经 R3 20mΩ/1206 到 BAT+；BT1 负端经 Fuse 5A 接 S1 pin3，S1 pin2 接 GND，Q1 控制端接 BT1 负端/Fuse 节点。

- 参数与网络：`cell=BT1 16340`；`positive_path=BT1+ -> Q1 -> IN_P -> R3 20mR/1206 -> BAT+`；`negative_path=BT1- -> Fuse 5A -> S1 pin3; S1 pin2 -> GND`；`switch=S1 SS-12F23`；`path_device=Q1 LP3218DT1G`；`sense_resistor=R3 20mR/1206`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 A2-A3 区 S1/Fuse/BT1/Q1/IN_P/R3/BAT+ 连线

### BAT+ 到 5V 转换

U1 ETA9740 的 BAT/SW 侧连接 BAT+ 和 L1 3.3uH，OUT pin7 形成 5V；ISET pin5 经 R2 150K 接 GND，LED1 pin2 经 R1 1K 和 LED1 接到 LED3 pin4。

- 参数与网络：`converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 106, C2 475`；`output_caps=C3/C4/C5 106, C11 104`；`iset=R2 150K`；`indicator=R1 1K, LED1 between LED1/LED3 pins`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 A1-A2 区 U1 ETA9740、L1、R1/R2、LED1、C1-C5/C11 与 BAT+/5V

### 5V、3V3 与 BAT+ 负载分配

5V 连接 ATOM pin3、J1/J2 Grove pin2 和 C7；3V3 连接 ATOM pin9、U3 VDDA/VDD、U5 VS、J3 VCC 及相关去耦；BAT+ 连接 U2/U4 VCC、JP3-JP6 舵机电源和 D1。

- 参数与网络：`5V=ATOM pin3, J1/J2 pin2, C7`；`3V3=ATOM pin9, U3 VDDA/VDD, U5 VS, J3 VCC, C8/C9/C10/C13`；`BAT+=U2/U4 VCC, JP3-JP6 power, D1`；`battery_decoupling=C1 106, C2 475`；`five_volt_decoupling=C7 475`；`three_volt_decoupling=C8 475, C9/C10 104`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页各区域的 5V、3V3、BAT+ 同名网络及 A4 区 C7-C10/D1

## 接口

### JP1/JP2 直流电机输出

U4 RZ7899 的并联 OUTF pins5/6 与 OUTR pins7/8 连接 JP2 两针接口，U2 的同类输出连接 JP1；两颗驱动器 VCC pin4 接 BAT+、GND pin3 接地。

- 参数与网络：`M1_control=U4 M1F/M1R -> JP2`；`M2_control=U2 M2F/M2R -> JP1`；`output_forward=OUTF pins5/6`；`output_reverse=OUTR pins7/8`；`supply=BAT+`；`ground=GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B1 区 U2/U4 RZ7899 与 JP1/JP2、BAT+/GND

### JP3-JP6 舵机接口

JP3/JP4 的 pin3 为控制、pin2 为 BAT+、pin1 为 GND；JP5/JP6 的 pin1 为控制、pin2 为 BAT+、pin3 为 GND。

- 参数与网络：`JP3=pin3 signal PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 signal PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 signal PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 signal PA3, pin2 BAT+, pin3 GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B1-C2 区 JP3-JP6 的 pin1-pin3 标号、BAT+/GND 与控制线

### ATOM 9 针主机接口

ATOM 左侧 pins7/5/3/1 分别为 G21 SCL、G25 SDA、5V、GND；右侧 pins9/8/6/4/2 分别为 3V3、G22、G19、G23、G33。

- 参数与网络：`pin1=GND`；`pin2=G33`；`pin3=5V`；`pin4=G23`；`pin5=G25 SDA`；`pin6=G19`；`pin7=G21 SCL`；`pin8=G22`；`pin9=3V3`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 C2 区 ATOM 连接器的 pin1-pin9 与网络标签

### J1 Grove PortB

J1 pin4 IO2 连接 ATOM G23，pin3 IO1 连接 G33，pin2 接 5V，pin1 接 GND。

- 参数与网络：`pin4_io2=G23`；`pin3_io1=G33`；`pin2=5V`；`pin1=GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 C2 区 J1 GROVE PortB 与 ATOM G23/G33/5V/GND

### J2 Grove PortC

J2 pin4 IO2 连接 ATOM G22，pin3 IO1 连接 G19，pin2 接 5V，pin1 接 GND。

- 参数与网络：`pin4_io2=G22`；`pin3_io1=G19`；`pin2=5V`；`pin1=GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 C2-C3 区 J2 GROVE PortC 与 ATOM G22/G19/5V/GND

## 总线

### Atom、STM32 与 INA226 共用 I2C

ATOM pin7 G21 连接 SCL 到 U3 PA9 pin17 和 U5 SCL pin5；ATOM pin5 G25 连接 SDA 到 U3 PA10 pin18 和 U5 SDA pin4；R5/R4 各 4.7K 将 SCL/SDA 上拉到 3V3。

- 参数与网络：`host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`monitor_scl=U5 pin5`；`scl_pullup=R5 4.7K to 3V3`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18`；`monitor_sda=U5 pin4`；`sda_pullup=R4 4.7K to 3V3`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 U3 PA9/PA10、ATOM G21/G25、U5 pins5/4 与 R5/R4 的 SCL/SDA 同名网络

## 总线地址

### INA226 A1/A0 地址绑带

U5 A1 pin1 直接接 GND；A0 pin2 经 R10 10K 接 GND，并预留 R11 NC 到 3V3。原理图未直接标注由该绑带对应的 I2C 地址。

- 参数与网络：`A1_pin1=GND`；`A0_pin2_default=R10 10K to GND`；`A0_option=R11 NC to 3V3`；`address_label_on_schematic=null`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B3 区 U5 A1/A0、R10 10K、R11 NC 与 GND/3V3

## GPIO 与控制信号

### 四路舵机 GPIO 映射

U3 PA0 pin6、PA1 pin7、PA2 pin8、PA3 pin9 分别连接 Servo3 JP3、Servo1 JP4、Servo4 JP5、Servo2 JP6 的控制信号；四个接口另外连接 BAT+ 和 GND。

- 参数与网络：`PA0_pin6=JP3 Servo3 signal pin3`；`PA1_pin7=JP4 Servo1 signal pin3`；`PA2_pin8=JP5 Servo4 signal pin1`；`PA3_pin9=JP6 Servo2 signal pin1`；`servo_power=BAT+`；`servo_ground=GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B1-C2 区 U3 PA0-PA3 到 JP3-JP6 的长连线与各接口 pin1-pin3

### 两路电机 GPIO 映射

U3 PA4 pin10 连接 M1F，PB1 pin14 连接 M1R，驱动 U4 INF/INR；PA6 pin12 连接 M2F，PA7 pin13 连接 M2R，驱动 U2 INF/INR；PA5 pin11 标为未连接。

- 参数与网络：`PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1`；`PA5_pin11=NC`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B1-B2 区 U3 PA4/PB1/PA6/PA7 与 U4/U2 的 M1F/M1R/M2F/M2R

## 传感器

### U5 INA226 电源监测路径

U5 VBUS pin8 与 IN+ pin10 同接一节点并经 R6 10R 到 IN_P；IN- pin9 经 R7 10R 到 BAT+，C12 104 跨接 IN+ 与 IN-；VS pin6 接 3V3，GND pin7 接地。

- 参数与网络：`part_number=INA226AIDGSR`；`vbus=pin8 tied to IN+ node`；`in_plus=pin10 -> R6 10R -> IN_P`；`in_minus=pin9 -> R7 10R -> BAT+`；`input_filter=C12 104 across IN+/IN-`；`external_shunt=R3 20mR/1206 between IN_P and BAT+`；`supply=VS pin6 3V3 with C13 106`；`ground=pin7 GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B3-B4 区 U5 pins8/10/9、R6/R7/C12 与 A2-A3 区 R3 IN_P/BAT+

## 调试与烧录

### STM32 SWD 与复位

J3 引出 NRST、SWCLK、SWDIO、3V3 和 GND；U3 PA13/SWDIO、PA14/SWCLK 和 NRST 分别连接这些网络，R9 10K 将 NRST 上拉到 3V3，C6 104 从 NRST 接地。

- 参数与网络：`connector=J3 SWD`；`signals=NRST,SWCLK,SWDIO,3V3,GND`；`debug_pins=PA13/SWDIO pin19, PA14/SWCLK pin20`；`reset_pin=NRST pin4`；`reset_pullup=R9 10K to 3V3`；`reset_capacitor=C6 104 to GND`
- 证据：图 42f23cce107e / 第 1 页 / 第 1 页 B2-B3 区 U3 SWDIO/SWCLK/NRST、R9/C6 与 J3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Motion Base v1.1 系统架构 | `controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`power_monitor=U5 INA226AIDGSR`；`motor_drivers=U4/U2 RZ7899`；`motor_channels=2`；`servo_channels=4`；`battery_rail=BAT+`；`five_volt_converter=U1 ETA9740` |
| 电源 | BT1 到 BAT+ 的开关与采样路径 | `cell=BT1 16340`；`positive_path=BT1+ -> Q1 -> IN_P -> R3 20mR/1206 -> BAT+`；`negative_path=BT1- -> Fuse 5A -> S1 pin3; S1 pin2 -> GND`；`switch=S1 SS-12F23`；`path_device=Q1 LP3218DT1G`；`sense_resistor=R3 20mR/1206` |
| 电源 | BAT+ 到 5V 转换 | `converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 106, C2 475`；`output_caps=C3/C4/C5 106, C11 104`；`iset=R2 150K`；`indicator=R1 1K, LED1 between LED1/LED3 pins` |
| 电源 | 5V、3V3 与 BAT+ 负载分配 | `5V=ATOM pin3, J1/J2 pin2, C7`；`3V3=ATOM pin9, U3 VDDA/VDD, U5 VS, J3 VCC, C8/C9/C10/C13`；`BAT+=U2/U4 VCC, JP3-JP6 power, D1`；`battery_decoupling=C1 106, C2 475`；`five_volt_decoupling=C7 475`；`three_volt_decoupling=C8 475, C9/C10 104` |
| 核心器件 | STM32F030F4P6 运动控制器 | `reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA pin5 and VDD pin16 to 3V3; VSS pin15 to GND`；`servo_gpio=PA0,PA1,PA2,PA3`；`motor_nets=M1F,M1R,M2F,M2R`；`i2c=PA9 SCL, PA10 SDA`；`debug=PA13 SWDIO, PA14 SWCLK, NRST`；`boot0=GND`；`oscillator_pins=PF0/PF1 NC` |
| 总线 | Atom、STM32 与 INA226 共用 I2C | `host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`monitor_scl=U5 pin5`；`scl_pullup=R5 4.7K to 3V3`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18`；`monitor_sda=U5 pin4`；`sda_pullup=R4 4.7K to 3V3` |
| 总线 | 正文中的 STM32 I2C 地址与寄存器 | `documented_address=0x38`；`servo_angle_registers=0x00-0x03`；`servo_pulse_registers=0x10,0x12,0x14,0x16`；`motor_registers=0x20-0x21`；`schematic_setting=null` |
| GPIO 与控制信号 | 四路舵机 GPIO 映射 | `PA0_pin6=JP3 Servo3 signal pin3`；`PA1_pin7=JP4 Servo1 signal pin3`；`PA2_pin8=JP5 Servo4 signal pin1`；`PA3_pin9=JP6 Servo2 signal pin1`；`servo_power=BAT+`；`servo_ground=GND` |
| GPIO 与控制信号 | 两路电机 GPIO 映射 | `PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1`；`PA5_pin11=NC` |
| 接口 | JP1/JP2 直流电机输出 | `M1_control=U4 M1F/M1R -> JP2`；`M2_control=U2 M2F/M2R -> JP1`；`output_forward=OUTF pins5/6`；`output_reverse=OUTR pins7/8`；`supply=BAT+`；`ground=GND` |
| 接口 | JP3-JP6 舵机接口 | `JP3=pin3 signal PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 signal PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 signal PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 signal PA3, pin2 BAT+, pin3 GND` |
| 接口 | ATOM 9 针主机接口 | `pin1=GND`；`pin2=G33`；`pin3=5V`；`pin4=G23`；`pin5=G25 SDA`；`pin6=G19`；`pin7=G21 SCL`；`pin8=G22`；`pin9=3V3` |
| 接口 | J1 Grove PortB | `pin4_io2=G23`；`pin3_io1=G33`；`pin2=5V`；`pin1=GND` |
| 接口 | J2 Grove PortC | `pin4_io2=G22`；`pin3_io1=G19`；`pin2=5V`；`pin1=GND` |
| 传感器 | U5 INA226 电源监测路径 | `part_number=INA226AIDGSR`；`vbus=pin8 tied to IN+ node`；`in_plus=pin10 -> R6 10R -> IN_P`；`in_minus=pin9 -> R7 10R -> BAT+`；`input_filter=C12 104 across IN+/IN-`；`external_shunt=R3 20mR/1206 between IN_P and BAT+`；`supply=VS pin6 3V3 with C13 106`；`ground=pin7 GND` |
| 总线地址 | INA226 A1/A0 地址绑带 | `A1_pin1=GND`；`A0_pin2_default=R10 10K to GND`；`A0_option=R11 NC to 3V3`；`address_label_on_schematic=null` |
| 调试与烧录 | STM32 SWD 与复位 | `connector=J3 SWD`；`signals=NRST,SWCLK,SWDIO,3V3,GND`；`debug_pins=PA13/SWDIO pin19, PA14/SWCLK pin20`；`reset_pin=NRST pin4`；`reset_pullup=R9 10K to 3V3`；`reset_capacitor=C6 104 to GND` |
| 电源 | 正文电池规格与原理图标注冲突 | `schematic_cell=BT1 16340`；`schematic_capacity=null`；`documented_cell=18350`；`documented_capacity=900mAh`；`conflict=true` |
| 电源 | 正文中的过载与通道电流额定值 | `documented_overload=5V@5A`；`documented_full_load=3A`；`documented_motor_peak=1A per channel`；`documented_servo_peak=0.4A per channel`；`documented_charge_current=1.152A at 5V`；`schematic_fuse=5A`；`schematic_shunt=R3 20mR/1206` |

## 待确认事项

- `bus.documented-i2c-protocol`：产品正文给出 I2C 地址 0x38，以及舵机 0x00-0x03/0x10-0x16 和电机 0x20-0x21 寄存器；原理图只显示 STM32 的 SCL/SDA 物理连接，无法验证固件地址和寄存器语义。（证据：图 42f23cce107e / 第 1 页 / 第 1 页 U3 SCL/SDA 与 ATOM G21/G25，图中无 STM32 地址或固件寄存器设定）
- `power.documented-battery-spec`：产品正文和包装内容称电池为 18350@900mAh，但原理图 BT1 标注 16340 且未标容量；电池规格和当前硬件版本的对应关系无法由现有图纸确认。（证据：图 42f23cce107e / 第 1 页 / 第 1 页 A2 区 BT1 明确标注 16340，图中无 18350 或 900mAh）
- `power.documented-current-ratings`：正文给出 5V@5A 过载保护、3A 满负荷、单电机峰值 1A、单舵机峰值 0.4A 和 1.152A 充电电流；原理图仅标 Fuse 5A、R3 20mΩ、RZ7899 与舵机连接，无法验证这些系统级额定值和测试条件。（证据：图 42f23cce107e / 第 1 页 / 第 1 页 S1/Fuse 5A、R3 20mR、U2/U4 RZ7899 与 JP3-JP6，图中无系统测试条件或通道电流额定值）
- `review.i2c-firmware-protocol`：A090-V11 当前 STM32 固件是否确认为 I2C 地址 0x38，并实现正文所列舵机与电机寄存器映射？；原因：地址与寄存器由固件决定，原理图只确认 SCL/SDA 物理连接；U5 INA226 还与 STM32 共用该总线，不能把正文的 0x38 误归给监测芯片。
- `review.battery-spec-conflict`：A090-V11 量产 BOM 和结构件使用 16340 还是 18350 电池，配套容量是否为 900mAh？；原因：产品正文称 18350@900mAh，原理图 BT1 却标 16340；需要当前版本 BOM、结构图或实物确认。
- `review.current-ratings`：5V@5A 过载、3A 满负荷、1A 单电机、0.4A 单舵机和 1.152A 充电电流的持续/峰值定义及测试条件是什么？；原因：原理图连接与保险标称不能单独证明系统级额定能力，需要器件规格、BOM 和整机测试记录。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `42f23cce107e7b34fcdecd3632d91c34580bdbf2575f5ef2c2db231ca37ab2c2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_schematic_sch_01.png` |

---

源文档：`zh_CN/atom/Atomic Motion Base v1.1.md`

源文档 SHA-256：`d418e8c0af38b69e55f311ea0bef4e31e26c94fcaa18391b5e5fccd67790b71c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
