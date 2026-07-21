# Module13.2 GoPlus2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 GoPlus2 |
| SKU | M025-B |
| 产品 ID | `module13-2-goplus2-5e9f31ba4cb3` |
| 源文档 | `zh_CN/module/goplus2.md` |

## 概述

Module13.2 GoPlus2 以 U1 STM32F030C8 通过 I2C 接入 M5-Bus，并控制 U4 DRV8833PWP 双 H 桥、四路 Servo、三组 Grove 和红外收发。外部 VIN_6_12V 分别经 U3 SY8368AQCC 生成 VCC_P5V、经 U5 TPS54335ADRCR 生成 VCC_5V；电池 VBAT 经 Q2/Q3 放电控制形成 VBAT_IN，再由 U2 TPS61088RHLR 升压到 VCC_P5V。原理图还包含 SWD、两组电机输出、四路舵机接口、DC 输入与电池接口；I2C 地址 0x38、500mAh 容量和充电实现未在页面中直接给出。

## 检索关键词

`Module13.2 GoPlus2`、`M025-B`、`STM32F030C8`、`DRV8833PWP`、`TPS61088RHLR`、`SY8368AQCC`、`TPS54335ADRCR`、`I2C`、`0x38`、`IIC_SCL`、`IIC_SDA`、`DRV_EN`、`DRV_FLT`、`MotorA1`、`MotorA2`、`MotorB1`、`MotorB2`、`MotorOUT_A1`、`MotorOUT_A2`、`MotorOUT_B1`、`MotorOUT_B2`、`Servo1`、`Servo2`、`Servo3`、`Servo4`、`PortB1_IN`、`PortB1_OUT`、`PortB2_IN`、`PortB2_OUT`、`PortB3_IN`、`PortB3_OUT`、`IR_IN`、`IR_OUT`、`VIN_6_12V`、`VBAT`、`VBAT_IN`、`VCC_P5V`、`VCC_5V`、`VCC_3V3`、`DCDC_EN`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030C8 | 模块主控制器，处理 I2C、Grove、舵机、电机、IR、SWD 与驱动使能/故障信号 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1-B1 STM32 MCU 区 U1，底部标 STM32F030C8 |
| U2 | TPS61088RHLR | 将 VBAT_IN 升压为 VCC_P5V 的电池升压转换器 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A2-B2 BAT Boost DC-DC 区 U2 TPS61088RHLR，VIN/BOOT/SW/VOUT/FB 与 L1 |
| U3 | SY8368AQCC | 将 VIN_6_12V 降压为 VCC_P5V 的外部输入电源转换器 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 B1-C2 IN Power Buck DC-DC 区 U3 SY8368AQCC，VIN/LX/FB/EN 与 L2 |
| U4 | DRV8833PWP | 双 H 桥电机驱动器，连接 MotorA/B 控制信号与 MotorOUT_A/B 输出 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 B2-C3 Motor Driver 区 U4 DRV8833PWP，AIN/BIN、AOUT/BOUT、nSLEEP/nFAULT、VM/VCP |
| U5 | TPS54335ADRCR | 将 VIN_6_12V 降压为系统 VCC_5V 的降压转换器 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 C1-D2 Sys Buck DC-DC 区 U5 TPS54335ADRCR，VIN/EN/PH/VSENSE 与 L3 |
| BUS1 | M5BUS | 30 针主机堆叠接口，引出电池、高功率输入、5V/3.3V、I2C、IR、RST 与 GND | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 B4-C4 M5 BUS 区 BUS1 M5BUS，1~30 脚 |
| J1 | STM32_SWD | 五针 SWD 调试接口，引出 VCC_3V3、RST、SWD_DIO、SWD_CLK 和 GND | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4 SWD 区 J1 STM32_SWD 1~5 脚 |
| J2 | DC_5.5MM | 外部 VIN_6_12V 直流电源输入插座，并带 LowP 开关触点 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4 Power IN 区 J2 DC_5.5MM，VIN_6_12V/LowP/GND |
| JP4 | BAT_CONN | 四针电池接口，引出 VBAT 与 GND | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4-B4 BAT CONN 区 JP4，VBAT/GND 与 1~4 脚 |
| JP1/JP2 | 未标注 | 两组双舵机六针接口，共引出 Servo1~Servo4、VCC_P5V 与 GND | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3-A4 Server CONN 区 JP1/JP2，Servo1~4、VCC_P5V、GND |
| JP3/JP5 | 未标注 | 两组双针电机输出接口，分别引出 MotorOUT_A1/A2 与 MotorOUT_B1/B2 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4-B4 Motor CONN 区 JP3/JP5 |
| J3 (3x GROVE) | GROVE | 三组 PortB 扩展接口，各引出 IO2 输入、IO1 输出、VCC_5V 和 GND | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 C4 GROVE 区三组 J3/GROVE，PortB1~3 IN/OUT |
| HR1 | SL0038GD | 红外接收器，输出 IR_IN | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 IR IN/OUT 区 HR1 SL0038GD，VCC_3V3/GND/IR_IN |
| LED1/Q1 | IR / SI2302 | 由 IR_OUT 控制的红外发射支路 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 IR IN/OUT 区 LED1 IR、R7 49.9R、Q1 SI2302、R9/R11 |
| Q2/Q3 | SIW15P02 / SI2302 | VBAT 到 VBAT_IN 的高边放电控制与栅极驱动网络 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 B3 BAT DisC 区 Q2 SIW15P02、Q3 SI2302、VBAT/VBAT_IN |
| Q4/Q5 | SI2301 / S8050 | 由 LowP 与 VIN_6_12V 形成 DCDC_EN 的欠压/使能控制网络 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 B3-C3 UVLO 区 Q4 SI2301、Q5 S8050、LowP、DCDC_EN |
| LED2 | GREEN | VCC_P5V 电源指示灯，经 R38 2.2K 接地 | 图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 上部 R38 2.2K 与 LED2 GREEN 串联在 VCC_P5V 和 GND 间 |

## 系统结构

### Module13.2 GoPlus2

U1 STM32F030C8 经 IIC_SCL/IIC_SDA 接入 BUS1，控制 U4 双路电机、Servo1~4、PortB1~3 与 IR 输入输出；U2/U3/U5 和电池/外部输入网络提供 VCC_P5V、VCC_5V、VCC_3V3 电源域。

- 参数与网络：`mcu=U1 STM32F030C8`；`motor_driver=U4 DRV8833PWP`；`battery_boost=U2 TPS61088RHLR`；`power_buck=U3 SY8368AQCC`；`system_buck=U5 TPS54335ADRCR`；`interfaces=2 motor,4 servo,3 Grove,IR,SWD,M5BUS`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页全图各功能分区与同名网络

## 核心器件

### U1

模块主控位号 U1，原理图型号标为 STM32F030C8。

- 参数与网络：`reference=U1`；`part_number=STM32F030C8`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1-B1 U1 符号底部 STM32F030C8

## 电源

### U1 电源与启动

U1 的 VDDA.9、VDD.1/.24/.48 接 VCC_3V3，VSS.23/.47/.8 与 VSSA 接 GND；NRST.7 由 R14 4.7K 上拉到 VCC_3V3 并由 C10 100nF/50V 对地，BOOT0.44 接 GND。

- 参数与网络：`supply=VCC_3V3`；`ground_pins=VSS 23,47,8 and VSSA`；`reset=NRST.7, R14 4.7K pull-up, C10 100nF/50V to GND`；`boot0=U1.44 GND`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 B1 U1 电源、NRST/BOOT0 与 R14/C10

### J2 外部电源输入

J2 DC_5.5MM 的电源端连接 VIN_6_12V，回路端接 GND，开关触点引出 LowP；VIN_6_12V 同时送入 U3 与 U5，并进入 UVLO 网络。

- 参数与网络：`connector=J2 DC_5.5MM`；`input_net=VIN_6_12V`；`ground=GND`；`switch_contact=LowP`；`loads=U3,U5,UVLO`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4 J2 与 B1/C1 U3/U5 VIN_6_12V、B3 LowP

### U3 外部输入降压

U3 SY8368AQCC 从 VIN_6_12V 经 LX 与 L2 2.2uH 生成 VCC_P5V，EN 由 DCDC_EN 控制；输出侧含 R21 36K、R25 4.7K 反馈与 C17/C19/C20 滤波。

- 参数与网络：`input=VIN_6_12V`；`converter=U3 SY8368AQCC`；`enable=DCDC_EN`；`inductor=L2 2.2uH`；`output=VCC_P5V`；`feedback=R21 36K,R25 4.7K`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 B1-C2 U3、L2、VCC_P5V、R21/R25 与输出电容

### U5 系统 5V 降压

U5 TPS54335ADRCR 从 VIN_6_12V 经 PH 与 L3 3.3uH 生成 VCC_5V，EN 由 DCDC_EN 控制；R32 330K 与 R34 62K 构成反馈分压。

- 参数与网络：`input=VIN_6_12V`；`converter=U5 TPS54335ADRCR`；`enable=DCDC_EN`；`inductor=L3 3.3uH`；`output=VCC_5V`；`feedback=R32 330K,R34 62K`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 C1-D2 U5、L3、VCC_5V、R32/R34

### VBAT 放电路径

VBAT 经 Q2 SIW15P02 高边器件形成 VBAT_IN，Q2 栅极由 Q3 SI2302 与 R15/R16/R17 网络控制；VBAT 同时连接 BUS1.1 与 JP4 电池接口。

- 参数与网络：`source=VBAT`；`high_side_switch=Q2 SIW15P02`；`gate_driver=Q3 SI2302`；`output=VBAT_IN`；`bus_pin=BUS1.1`；`battery_connector=JP4`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 B3 BAT DisC Q2/Q3 与 A4 JP4、B4 BUS1.1 VBAT

### U2 电池升压

U2 TPS61088RHLR 以 VBAT_IN 和 L1 2.2uH 为输入开关级，在 VOUT.14/.15/.16 输出 VCC_P5V；R12 6.8K 与 R13 2.2K 构成 FB 分压。

- 参数与网络：`input=VBAT_IN`；`converter=U2 TPS61088RHLR`；`inductor=L1 2.2uH`；`output=VCC_P5V`；`feedback=R12 6.8K,R13 2.2K`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A2-B2 U2、L1、VBAT_IN、VCC_P5V、R12/R13

### DCDC_EN/LowP 欠压控制

Q4 SI2301、Q5 S8050 与 R22/R23/R24/R26/R27 构成 VIN_6_12V/LowP 到 DCDC_EN 的控制网络，图中在 DCDC_EN 旁标注 MAX 6V。

- 参数与网络：`input=VIN_6_12V and LowP`；`output=DCDC_EN`；`mosfet=Q4 SI2301`；`transistor=Q5 S8050`；`note=DCDC_EN MAX 6V`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 B3-C3 UVLO 区 Q4/Q5、电阻网络、LowP 与 DCDC_EN MAX 6V

### VCC_P5V 指示

R38 2.2K 与 LED2 GREEN 串联在 VCC_P5V 与 GND 之间，作为该电源轨指示支路。

- 参数与网络：`rail=VCC_P5V`；`resistor=R38 2.2K`；`led=LED2 GREEN`；`return=GND`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 上方 VCC_P5V-R38-LED2-GND

## 接口

### 三组 J3 GROVE

三组 Grove 针脚定义相同：IO2 经 4.7K 串联电阻连接对应 PortBx_IN，IO1 经 4.7K 串联电阻连接 PortBx_OUT，另两脚为 VCC_5V 与 GND。

- 参数与网络：`port1=IO2-R28 4.7K-PortB1_IN; IO1-R29 4.7K-PortB1_OUT`；`port2=IO2-R30 4.7K-PortB2_IN; IO1-R31 4.7K-PortB2_OUT`；`port3=IO2-R33 4.7K-PortB3_IN; IO1-R35 4.7K-PortB3_OUT`；`power=VCC_5V`；`ground=GND`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 C4 GROVE 区三组 IO2/IO1/5V/GND 与 R28~R35

### JP1/JP2 舵机接口

JP1 同组引出 Servo2 与 Servo1，JP2 同组引出 Servo4 与 Servo3；每组还分配 GND 与 VCC_P5V 电源行。

- 参数与网络：`JP1_signals=Servo2,Servo1,GND,VCC_P5V`；`JP2_signals=Servo4,Servo3,GND,VCC_P5V`；`servo_supply=VCC_P5V`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3-A4 JP1/JP2 Server CONN 网络标签

### JP3/JP5 电机接口

JP3.1/JP3.2 分别为 MotorOUT_A1/MotorOUT_A2，JP5.1/JP5.2 分别为 MotorOUT_B1/MotorOUT_B2。

- 参数与网络：`JP3_pin_1=MotorOUT_A1`；`JP3_pin_2=MotorOUT_A2`；`JP5_pin_1=MotorOUT_B1`；`JP5_pin_2=MotorOUT_B2`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4-B4 JP3/JP5 Motor CONN

### BUS1 M5BUS 已用针脚

BUS1.1=VBAT，2/4/6=HPWR 并接 VIN_6_12V，3=VCC_5V，9=IR_OUT，13=IIC_SCL，14=IIC_SDA，19=VCC_3V3，25=RST，29=IR_IN，26/28/30=GND。

- 参数与网络：`pin_1=VBAT`；`pins_2_4_6=VIN_6_12V / HPWR`；`pin_3=VCC_5V`；`pin_9=IR_OUT`；`pin_13=IIC_SCL`；`pin_14=IIC_SDA`；`pin_19=VCC_3V3`；`pin_25=RST`；`pin_29=IR_IN`；`pins_26_28_30=GND`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 B4 BUS1 1~30 脚及外部网络标签

## 总线

### I2C 总线

U1 PB6/PB7 分别连接 IIC_SCL/IIC_SDA，并通过 R5/R6 各 4.7K 上拉到 VCC_3V3；IIC_SCL/IIC_SDA 分别连接 BUS1.13/BUS1.14。

- 参数与网络：`controller=U1`；`scl=U1 PB6 -> IIC_SCL -> BUS1.13`；`sda=U1 PB7 -> IIC_SDA -> BUS1.14`；`scl_pullup=R5 4.7K to VCC_3V3`；`sda_pullup=R6 4.7K to VCC_3V3`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1 U1 PB6/PB7 与 R5/R6；B4 BUS1.13/14

### U4 电机输出

U4 的 AOUT1/AOUT2 输出 MotorOUT_B2/MotorOUT_B1，BOUT1/BOUT2 输出 MotorOUT_A2/MotorOUT_A1；U4 VM 接 VCC_P5V。

- 参数与网络：`AOUT1=MotorOUT_B2`；`AOUT2=MotorOUT_B1`；`BOUT1=MotorOUT_A2`；`BOUT2=MotorOUT_A1`；`motor_supply=VCC_P5V`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 U4 右侧 AOUT/BOUT 网络与左下 VM VCC_P5V

## GPIO 与控制信号

### 三组 PortB GPIO

U1 PA0/PA1/PA2 分别接 PortB1_IN/PortB2_IN/PortB3_IN，U1 PB12/PB11/PB10 分别接 PortB1_OUT/PortB2_OUT/PortB3_OUT。

- 参数与网络：`PortB1_IN=U1 PA0`；`PortB2_IN=U1 PA1`；`PortB3_IN=U1 PA2`；`PortB1_OUT=U1 PB12`；`PortB2_OUT=U1 PB11`；`PortB3_OUT=U1 PB10`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1 U1 左上 PA0~PA2 与右侧 PB10~PB12 网络

### 四路舵机控制

Servo1/Servo2 分别由 U1 PA6/PA7 引出，Servo3/Servo4 分别由 U1 PB1/PB0 引出；各控制线串有 22R 电阻。

- 参数与网络：`Servo1=U1 PA6 via 22R`；`Servo2=U1 PA7 via 22R`；`Servo3=U1 PB1 via 22R`；`Servo4=U1 PB0 via R2 22R`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1 U1 PA6/PA7、PB0/PB1 的 Servo1~4 与 22R 串联电阻

### U1 到 U4 电机控制

U1 的 MotorB2/MotorB1/MotorA2/MotorA1 网络进入 U4 AIN1/AIN2/BIN1/BIN2；U1 还以 DRV_EN 控制 U4 nSLEEP，并接收 U4 nFAULT 的 DRV_FLT。

- 参数与网络：`AIN1=MotorB2`；`AIN2=MotorB1`；`BIN1=MotorA2`；`BIN2=MotorA1`；`sleep_enable=DRV_EN -> U4 nSLEEP`；`fault=U4 nFAULT -> DRV_FLT`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1 U1 电机/DRV 网络与 B2-C3 U4 左侧同名网络

## 内存与 Flash

### 外部存储器

页面未展示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器件和总线。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页完整原理图无独立存储器或存储连接器

## 射频

### 红外接收

HR1 SL0038GD 由 VCC_3V3/GND 供电，输出 IR_IN，并由 R3 4.7K 上拉；IR_IN 同名网络连接 BUS1.29。

- 参数与网络：`receiver=HR1 SL0038GD`；`supply=VCC_3V3`；`output=IR_IN`；`pullup=R3 4.7K`；`bus_pin=BUS1.29`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 HR1/R3 IR_IN 与 B4 BUS1.29

### 红外发射

LED1 IR 从 VCC_5V 经 R7 49.9R 接 Q1 SI2302，Q1 栅极由 IR_OUT 经 R9 1K 驱动并由 R11 10K 下拉；IR_OUT 同名网络连接 BUS1.9。

- 参数与网络：`emitter=LED1 IR`；`supply=VCC_5V`；`series_resistor=R7 49.9R`；`switch=Q1 SI2302`；`gate_resistor=R9 1K`；`gate_pulldown=R11 10K`；`bus_pin=BUS1.9`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A3 LED1/Q1/R7/R9/R11 IR_OUT 与 B4 BUS1.9

## 调试与烧录

### J1 STM32_SWD

J1.1 为 VCC_3V3，J1.2 为 RST，J1.3 为 SWD_DIO，J1.4 为 SWD_CLK，J1.5 为 GND；SWD_DIO/CLK 分别连接 U1 PA13/PA14。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=RST`；`pin_3=SWD_DIO / U1 PA13`；`pin_4=SWD_CLK / U1 PA14`；`pin_5=GND`
- 证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A4 J1 1~5 脚与 A1 U1 PA13/PA14 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 GoPlus2 | `mcu=U1 STM32F030C8`；`motor_driver=U4 DRV8833PWP`；`battery_boost=U2 TPS61088RHLR`；`power_buck=U3 SY8368AQCC`；`system_buck=U5 TPS54335ADRCR`；`interfaces=2 motor,4 servo,3 Grove,IR,SWD,M5BUS` |
| 核心器件 | U1 | `reference=U1`；`part_number=STM32F030C8` |
| 电源 | U1 电源与启动 | `supply=VCC_3V3`；`ground_pins=VSS 23,47,8 and VSSA`；`reset=NRST.7, R14 4.7K pull-up, C10 100nF/50V to GND`；`boot0=U1.44 GND` |
| 调试与烧录 | J1 STM32_SWD | `pin_1=VCC_3V3`；`pin_2=RST`；`pin_3=SWD_DIO / U1 PA13`；`pin_4=SWD_CLK / U1 PA14`；`pin_5=GND` |
| 总线 | I2C 总线 | `controller=U1`；`scl=U1 PB6 -> IIC_SCL -> BUS1.13`；`sda=U1 PB7 -> IIC_SDA -> BUS1.14`；`scl_pullup=R5 4.7K to VCC_3V3`；`sda_pullup=R6 4.7K to VCC_3V3` |
| 总线地址 | 正文中的 I2C 地址 | `documented_address=0x38`；`address_on_schematic=null`；`address_straps_shown=false` |
| GPIO 与控制信号 | 三组 PortB GPIO | `PortB1_IN=U1 PA0`；`PortB2_IN=U1 PA1`；`PortB3_IN=U1 PA2`；`PortB1_OUT=U1 PB12`；`PortB2_OUT=U1 PB11`；`PortB3_OUT=U1 PB10` |
| 接口 | 三组 J3 GROVE | `port1=IO2-R28 4.7K-PortB1_IN; IO1-R29 4.7K-PortB1_OUT`；`port2=IO2-R30 4.7K-PortB2_IN; IO1-R31 4.7K-PortB2_OUT`；`port3=IO2-R33 4.7K-PortB3_IN; IO1-R35 4.7K-PortB3_OUT`；`power=VCC_5V`；`ground=GND` |
| GPIO 与控制信号 | 四路舵机控制 | `Servo1=U1 PA6 via 22R`；`Servo2=U1 PA7 via 22R`；`Servo3=U1 PB1 via 22R`；`Servo4=U1 PB0 via R2 22R` |
| 接口 | JP1/JP2 舵机接口 | `JP1_signals=Servo2,Servo1,GND,VCC_P5V`；`JP2_signals=Servo4,Servo3,GND,VCC_P5V`；`servo_supply=VCC_P5V` |
| GPIO 与控制信号 | U1 到 U4 电机控制 | `AIN1=MotorB2`；`AIN2=MotorB1`；`BIN1=MotorA2`；`BIN2=MotorA1`；`sleep_enable=DRV_EN -> U4 nSLEEP`；`fault=U4 nFAULT -> DRV_FLT` |
| 总线 | U4 电机输出 | `AOUT1=MotorOUT_B2`；`AOUT2=MotorOUT_B1`；`BOUT1=MotorOUT_A2`；`BOUT2=MotorOUT_A1`；`motor_supply=VCC_P5V` |
| 接口 | JP3/JP5 电机接口 | `JP3_pin_1=MotorOUT_A1`；`JP3_pin_2=MotorOUT_A2`；`JP5_pin_1=MotorOUT_B1`；`JP5_pin_2=MotorOUT_B2` |
| 射频 | 红外接收 | `receiver=HR1 SL0038GD`；`supply=VCC_3V3`；`output=IR_IN`；`pullup=R3 4.7K`；`bus_pin=BUS1.29` |
| 射频 | 红外发射 | `emitter=LED1 IR`；`supply=VCC_5V`；`series_resistor=R7 49.9R`；`switch=Q1 SI2302`；`gate_resistor=R9 1K`；`gate_pulldown=R11 10K`；`bus_pin=BUS1.9` |
| 接口 | BUS1 M5BUS 已用针脚 | `pin_1=VBAT`；`pins_2_4_6=VIN_6_12V / HPWR`；`pin_3=VCC_5V`；`pin_9=IR_OUT`；`pin_13=IIC_SCL`；`pin_14=IIC_SDA`；`pin_19=VCC_3V3`；`pin_25=RST`；`pin_29=IR_IN`；`pins_26_28_30=GND` |
| 电源 | J2 外部电源输入 | `connector=J2 DC_5.5MM`；`input_net=VIN_6_12V`；`ground=GND`；`switch_contact=LowP`；`loads=U3,U5,UVLO` |
| 电源 | U3 外部输入降压 | `input=VIN_6_12V`；`converter=U3 SY8368AQCC`；`enable=DCDC_EN`；`inductor=L2 2.2uH`；`output=VCC_P5V`；`feedback=R21 36K,R25 4.7K` |
| 电源 | U5 系统 5V 降压 | `input=VIN_6_12V`；`converter=U5 TPS54335ADRCR`；`enable=DCDC_EN`；`inductor=L3 3.3uH`；`output=VCC_5V`；`feedback=R32 330K,R34 62K` |
| 电源 | VBAT 放电路径 | `source=VBAT`；`high_side_switch=Q2 SIW15P02`；`gate_driver=Q3 SI2302`；`output=VBAT_IN`；`bus_pin=BUS1.1`；`battery_connector=JP4` |
| 电源 | U2 电池升压 | `input=VBAT_IN`；`converter=U2 TPS61088RHLR`；`inductor=L1 2.2uH`；`output=VCC_P5V`；`feedback=R12 6.8K,R13 2.2K` |
| 电源 | DCDC_EN/LowP 欠压控制 | `input=VIN_6_12V and LowP`；`output=DCDC_EN`；`mosfet=Q4 SI2301`；`transistor=Q5 S8050`；`note=DCDC_EN MAX 6V` |
| 电源 | VCC_P5V 指示 | `rail=VCC_P5V`；`resistor=R38 2.2K`；`led=LED2 GREEN`；`return=GND` |
| 电源 | 正文中的 500mAh 与充电 | `documented_capacity=500mAh`；`documented_charging=via M5Core`；`capacity_on_schematic=null`；`charger_ic_shown=false`；`visible_battery_path=JP4/BUS1.1 VBAT -> Q2/Q3 -> VBAT_IN -> U2` |
| 时钟 | U1 时钟 | `external_crystal_shown=false`；`oscillator_shown=false`；`clock_frequency=null` |
| 保护电路 | 输入与输出保护可见性 | `uvlo_shown=true`；`input_fuse_shown=false`；`reverse_protection_diode_shown=false`；`tvs_shown=false`；`grove_esd_shown=false`；`motor_tvs_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x38`：产品正文给出 I2C 地址 0x38，但原理图未显示该地址、地址选择电阻或固件配置，因此 0x38 需由固件/协议确认。（证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 U1 与 BUS1 IIC_SCL/IIC_SDA 范围，无 0x38 标注）
- `power.documented-battery-capacity-charge`：产品正文称内置 500mAh 电池并可由 M5Core 充电；原理图只显示 VBAT、JP4、BUS1.1、Q2/Q3 放电与 U2 升压路径，没有容量标注或独立充电 IC，因此容量和充电实现无法由本页确认。（证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 JP4/BUS1 VBAT、BAT DisC 与 BAT Boost 区，无 500mAh 或充电器件）
- `clock.mcu-clock-not-shown`：页面未显示连接 U1 的外部晶振、谐振器或时钟网络，具体 MCU 时钟源与频率无法确认。（证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 A1-B1 U1 周围无晶振或时钟网络）
- `protection.power-interface-limits`：原理图显示 LowP/UVLO 使能网络与电源滤波，但未显示 J2/JP4/Motor/Grove 端口的保险丝、反接二极管、TVS 或 ESD 阵列，实际端口保护能力需进一步确认。（证据：图 f87a7d5dae17 / 第 1 页 / 第 1 页 J2/JP4/JP3/JP5/J3 与 UVLO、电源区；无保险丝或 TVS 符号）
- `review.i2c-address`：请通过 M025-B 当前固件或 I2C 协议确认 7-bit 地址是否固定为 0x38。；原因：地址属于固件行为，原理图未显示 0x38 或地址配置。
- `review.battery-charge`：请确认内置电池实际容量、JP4 针脚定义、M5Core 充电路径与充电保护规格。；原因：本页无容量标注和充电器件，只能看到 VBAT 放电/升压路径。
- `review.mcu-clock`：请确认 STM32F030C8 使用的时钟源与频率，以及是否完全依赖内部振荡器。；原因：原理图没有外部时钟器件，不能据此推导固件时钟配置。
- `review.port-protection`：请确认 DC、电池、电机、舵机和 Grove 接口的反接、过流、浪涌与 ESD 保护是否在其他页面或 PCB 中实现。；原因：当前单页未画保险丝、TVS 或 ESD 阵列。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f87a7d5dae17a0bdcab9075cd7589bab04075aa11049a2d8fec4c3ae5b8dab87` | `https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_sch_01.webp` |

---

源文档：`zh_CN/module/goplus2.md`

源文档 SHA-256：`dd0fbc564d7828cd64088c9937717448ae2672a5dd2978305aae121103321650`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
