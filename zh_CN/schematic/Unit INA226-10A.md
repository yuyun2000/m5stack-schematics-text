# Unit INA226-10A 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit INA226-10A |
| SKU | U200 |
| 产品 ID | `unit-ina226-10a-aa1797f184e5` |
| 源文档 | `zh_CN/unit/Unit_INA226-10A.md` |

## 概述

Unit INA226-10A 的原理图以隔离边界分为 HOST 主控侧与 INA226 测量侧：M1 B0505ST16-W5 传递隔离 5V 电源，U1 在 HOST_I2C_SDA/SCL 与 IIC_SDA/SCL 之间提供信号隔离。测量侧使用 U2 INA226AIDGSR，借助 R3 5mΩ 分流电阻与 INA_P/INA_N Kelvin 网络测量 VCC_IN 到 VCC_OUT 的电流，并以 I2C 地址 0x41 通信。HOST_5V 和隔离侧 VCC_5V 分别由 U4、U3 XC6228D332VR-G 转换为两侧独立 3.3V 电源，J2 同时引出高电流通道和 PGND。

## 检索关键词

`Unit INA226-10A`、`U200`、`INA226`、`INA226AIDGSR`、`IIC:0x41`、`0x41`、`CA-IS3020`、`ISO1540`、`ADuM1250`、`B0505ST16-W5`、`XC6228D332VR-G`、`BSMD1206C-2120T`、`LESD3Z5.0CMT1G`、`5mR`、`INA_P`、`INA_N`、`VCC_IN`、`VCC_OUT`、`VCC_5V`、`VCC_3V3`、`HOST_5V`、`HOST_VCC_3V3`、`HOST_I2C_SCL`、`HOST_I2C_SDA`、`IIC_SCL`、`IIC_SDA`、`PGND`、`HOST_GND`、`I2C 隔离`、`5mΩ 分流电阻`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | INA226AIDGSR | 分流电压、总线电压与功率监测器 | 图 9f0f4b7d428d / 第 1 页 / 网格 C3-C4，U2 方框下方标注 INA226AIDGSR，含 VIN-/VIN+/VBUS/SCL/SDA/A0/A1/ALERT |
| U1 | CA-IS3020/ISO1540/ADuM1250 | HOST 与测量侧之间的双通道 I2C 信号隔离器 | 图 9f0f4b7d428d / 第 1 页 / 网格 D2，U1 跨越蓝黑隔离虚线，器件值标注 CA-IS3020/ISO1540/ADuM1250 |
| M1 | B0505ST16-W5 | HOST_5V 到隔离侧 VCC_5V 的隔离 DC-DC 模块 | 图 9f0f4b7d428d / 第 1 页 / 网格 C2，M1 跨越蓝黑隔离虚线，器件值标注 B0505ST16-W5 |
| U3 | XC6228D332VR-G | 测量侧 VCC_5V 到 VCC_3V3 的 LDO | 图 9f0f4b7d428d / 第 1 页 / 网格 B3-B4，U3 XC6228D332VR-G，IN/EN 接 VCC_5V，OUT 接 VCC_3V3 |
| U4 | XC6228D332VR-G | HOST_5V 到 HOST_VCC_3V3 的主控侧 LDO | 图 9f0f4b7d428d / 第 1 页 / 网格 A1-A2，U4 XC6228D332VR-G，IN/EN 接 HOST_5V，OUT 接 HOST_VCC_3V3 |
| FUSE1 | BSMD1206C-2120T | J2 pin1 与 VCC_IN 之间的串联过流保护器件 | 图 9f0f4b7d428d / 第 1 页 / 网格 C3-C4，FUSE1 标注 BSMD1206C-2120T，串联在 J2 pin1 与 VCC_IN 之间 |
| R3 | 5mR | VCC_IN 与 VCC_OUT 之间的电流检测分流电阻 | 图 9f0f4b7d428d / 第 1 页 / 网格 C3，R3 垂直跨接 VCC_IN 与 VCC_OUT，阻值标注 5mR |
| J1 | IIC_Socket_4P | HOST 侧 Grove/I2C 与 5V 电源接口 | 图 9f0f4b7d428d / 第 1 页 / 网格 C1，J1 IIC_Socket_4P，四脚连接 HOST_I2C_SCL、HOST_I2C_SDA、HOST_5V、HOST_GND |
| J2 | THT_Male_P_1x4 | VCC_IN、VCC_OUT 与双 PGND 的四位高电流端子 | 图 9f0f4b7d428d / 第 1 页 / 网格 C4，J2 THT_Male_P_1x4，pin1 接保险丝、pin2/3 接 PGND、pin4 接 VCC_OUT |
| D1 | LESD3Z5.0CMT1G | 隔离侧 VCC_5V 对 GND 的瞬态保护器件 | 图 9f0f4b7d428d / 第 1 页 / 网格 C2，D1 标注 LESD3Z5.0CMT1G，跨接 VCC_5V 与 GND |
| D2 | BLUE 0603 | HOST_5V 电源指示 LED | 图 9f0f4b7d428d / 第 1 页 / 网格 B1-B2，D2 标注 BLUE 0603，与 R13 4.7KΩ 串联在 HOST_5V 与 HOST_GND 之间 |
| L1 | 120R@100MHz | PGND 与测量侧 GND 之间的高频阻抗器件 | 图 9f0f4b7d428d / 第 1 页 / 网格 A3-A4，L1 标注 120R@100MHz，连接 PGND 与 GND |
| L2 | 6.8uH | M1 隔离电源输入滤波电感 | 图 9f0f4b7d428d / 第 1 页 / 网格 C1-C2，L2 标注 6.8uH，串联在 HOST_5V 与 M1 VIN 之间 |

## 系统结构

### HOST 与测量侧隔离架构

蓝黑竖向虚线将电路分为 HOST_5V/HOST_GND/HOST_VCC_3V3 域与 VCC_5V/GND/VCC_3V3 测量域；M1 跨域传递电源，U1 跨域传递两路 I2C 信号。

- 参数与网络：`host_power=HOST_5V,HOST_VCC_3V3,HOST_GND`；`measurement_power=VCC_5V,VCC_3V3,GND`；`power_isolator=M1 B0505ST16-W5`；`signal_isolator=U1 CA-IS3020/ISO1540/ADuM1250`
- 证据：图 9f0f4b7d428d / 第 1 页 / 整页中央蓝黑隔离虚线，以及跨线的 M1 与 U1

## 电源

### U4 HOST 侧 3.3V LDO

U4 XC6228D332VR-G 的 IN pin1 与 EN pin3 连接 HOST_5V，OUT pin5 输出 HOST_VCC_3V3，GND pin2 连接 HOST_GND，NC pin4 未连接。

- 参数与网络：`reference=U4`；`input=HOST_5V`；`output=HOST_VCC_3V3`；`pinout=1:IN,2:GND,3:EN,4:NC,5:OUT`；`input_capacitor=C12 4.7uF/16V`；`output_capacitor=C7 4.7uF/16V`；`test_point=TP2`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 A1-A2，U4、C12、C7、HOST_5V、HOST_VCC_3V3 与 TP2

### M1 HOST_5V 输入滤波

HOST_5V 经 L2 6.8 uH 串联后连接 M1 VIN pin3；C1 10 uF/16V 位于 L2 输入侧，C2 10 uF/16V 位于 L2 输出侧，两者均连接 HOST_GND。

- 参数与网络：`input_rail=HOST_5V`；`series_inductor=L2 6.8uH`；`pre_filter_capacitor=C1 10uF/16V`；`post_filter_capacitor=C2 10uF/16V`；`module_input=M1 pin3 VIN`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C1-C2，HOST_5V、C1、L2、C2 与 M1 VIN pin3

### M1 隔离 5V 输出

M1 的 VO pin14 连接 VCC_5V，0V pin9、pin15、pin16 连接测量侧 GND；C5 10 uF/16V 跨接 VCC_5V 与 GND，TP3 位于 VCC_5V。

- 参数与网络：`reference=M1`；`part_number=B0505ST16-W5`；`output_pin=14:VO`；`output_rail=VCC_5V`；`return_pins=9,15,16:0V`；`output_capacitor=C5 10uF/16V`；`test_point=TP3`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C2，M1 pin9/pin14/pin15/pin16、C5、VCC_5V、GND 与 TP3

### M1 TRIM 网络

M1 TRIM pin13 通过 R1 0Ω (0R0) ±1% 连接 VCC_5V；R2 标注 NC，位于 TRIM 与 pin9 的 GND 网络之间。

- 参数与网络：`trim_pin=M1 pin13 TRIM`；`output_link=R1 0Ω (0R0) ±1%`；`ground_option=R2 NC`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C2，M1 pin13 TRIM、R1 0Ω、R2 NC 与 VCC_5V/GND

### U1 两侧隔离供电

U1 pin1 连接 HOST_VCC_3V3、pin4 连接 HOST_GND，C4 4.7 uF/16V 跨接该侧电源；pin8 连接 VCC_3V3、pin5 连接 GND，C6 4.7 uF/16V 跨接测量侧电源。

- 参数与网络：`host_supply=pin1 HOST_VCC_3V3,pin4 HOST_GND,C4 4.7uF/16V`；`measurement_supply=pin8 VCC_3V3,pin5 GND,C6 4.7uF/16V`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D2，U1 pin1/pin4/C4 与 pin8/pin5/C6 两侧供电网络

### U3 测量侧 3.3V LDO

U3 XC6228D332VR-G 的 IN pin1 与 EN pin3 连接 VCC_5V，OUT pin5 输出 VCC_3V3，GND pin2 连接 GND，NC pin4 未连接。

- 参数与网络：`reference=U3`；`input=VCC_5V`；`output=VCC_3V3`；`pinout=1:IN,2:GND,3:EN,4:NC,5:OUT`；`input_capacitors=C10 10uF/16V,C11 100nF/16V`；`output_capacitors=C8 100nF/16V,C9 10uF/16V`；`test_point=TP1`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 B3-B4，U3、C10、C11、C8、C9、VCC_5V、VCC_3V3 与 TP1

### INA226 供电与去耦

U2 VS+ pin6 连接 VCC_3V3，GND pin7 连接 GND；C13 4.7 uF/16V 跨接 VCC_3V3 与 GND。

- 参数与网络：`supply_pin=U2 pin6 VS+`；`supply_rail=VCC_3V3`；`ground_pin=U2 pin7 GND`；`decoupling_capacitor=C13 4.7uF/16V`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D3，U2 pin6/pin7、VCC_3V3、GND 与 C13

## 接口

### J1 HOST 侧接口

J1 的 pin1 至 pin4 依次连接 HOST_I2C_SCL、HOST_I2C_SDA、HOST_5V 和 HOST_GND。

- 参数与网络：`reference=J1`；`part_number=IIC_Socket_4P`；`pinout=1:HOST_I2C_SCL,2:HOST_I2C_SDA,3:HOST_5V,4:HOST_GND`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C1，J1 四个脚号及右侧 HOST_I2C_SCL/HOST_I2C_SDA/HOST_5V/HOST_GND 标注

### J2 高电流端子

J2 pin1 通过 FUSE1 连接 VCC_IN，pin2 与 pin3 并联连接 PGND，pin4 连接 VCC_OUT。

- 参数与网络：`reference=J2`；`part_number=THT_Male_P_1x4`；`pinout=1:FUSE1/VCC_IN,2:PGND,3:PGND,4:VCC_OUT`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C4，J2 pin1-pin4 与左侧 FUSE1、PGND、VCC_OUT 连线

## 总线

### U1 隔离 I2C 信号映射

HOST_I2C_SDA 连接 U1 pin2 ViA，并由 pin7 VoA 输出为 IIC_SDA；HOST_I2C_SCL 连接 pin3 ViB，并由 pin6 VoB 输出为 IIC_SCL。

- 参数与网络：`sda_path=HOST_I2C_SDA -> U1 pin2 ViA -> U1 pin7 VoA -> IIC_SDA`；`scl_path=HOST_I2C_SCL -> U1 pin3 ViB -> U1 pin6 VoB -> IIC_SCL`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D2，U1 左侧 HOST_I2C_SDA/SCL 与右侧 IIC_SDA/SCL 引脚标注

### HOST 侧 I2C 上拉

R4 4.7 kΩ 将 HOST_I2C_SCL 上拉到 HOST_VCC_3V3，R12 4.7 kΩ 将 HOST_I2C_SDA 上拉到 HOST_VCC_3V3。

- 参数与网络：`scl_pullup=R4 4.7kΩ (4701) ±1%`；`sda_pullup=R12 4.7kΩ (4701) ±1%`；`rail=HOST_VCC_3V3`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D1，HOST_VCC_3V3 至 R4/HOST_I2C_SCL 与 R12/HOST_I2C_SDA

### INA226 I2C 总线

U2 SCL pin5 连接 IIC_SCL，SDA pin4 连接 IIC_SDA；R9 4.7 kΩ 将 IIC_SCL 上拉到 VCC_3V3，R8 4.7 kΩ 将 IIC_SDA 上拉到 VCC_3V3。

- 参数与网络：`scl=U2 pin5 IIC_SCL,R9 4.7kΩ to VCC_3V3`；`sda=U2 pin4 IIC_SDA,R8 4.7kΩ to VCC_3V3`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D3-D4，U2 SCL/SDA 至 IIC_SCL/IIC_SDA 及 R9/R8 上拉网络

## 总线地址

### INA226 I2C 地址配置

U2 A1 pin1 通过 R6 4.7 kΩ 连接 GND，A0 pin2 通过 R7 4.7 kΩ 连接 VCC_3V3；原理图明确标注 IIC:0x41。

- 参数与网络：`address=0x41`；`a1_configuration=U2 pin1 -> R6 4.7kΩ -> GND`；`a0_configuration=U2 pin2 -> R7 4.7kΩ -> VCC_3V3`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D3-D4，U2 A1/A0、R6/R7 与器件下方 IIC:0x41 标注

## GPIO 与控制信号

### INA226 ALERT 网络

U2 ALERT pin3 通过 R5 4.7 kΩ 连接 GND，且该 ALERT 网络未引出到 J1 或 J2。

- 参数与网络：`alert_pin=U2 pin3 ALERT`；`resistor=R5 4.7kΩ to GND`；`external_connector=null`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D3-D4，U2 ALERT pin3 到 R5 4.7kΩ/GND 的封闭支路

## 保护电路

### 隔离侧 VCC_5V 瞬态保护

D1 LESD3Z5.0CMT1G 跨接 VCC_5V 与测量侧 GND。

- 参数与网络：`reference=D1`；`part_number=LESD3Z5.0CMT1G`；`protected_rail=VCC_5V`；`return=GND`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C2，TP3 下方 D1 LESD3Z5.0CMT1G 至 GND 支路

### FUSE1 输入过流保护

FUSE1 BSMD1206C-2120T 串联在 J2 pin1 与 VCC_IN 网络之间。

- 参数与网络：`reference=FUSE1`；`part_number=BSMD1206C-2120T`；`upstream=J2 pin1`；`downstream=VCC_IN`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C3-C4，VCC_IN 与 J2 pin1 之间的 FUSE1 BSMD1206C-2120T

## 关键网络

### PGND 与 GND 连接

L1 标注 120R@100MHz，串联连接端子侧 PGND 与测量电路 GND。

- 参数与网络：`reference=L1`；`impedance=120R@100MHz`；`net_a=PGND`；`net_b=GND`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 A3-A4，PGND-L1 120R@100MHz-GND 单独连接

### 板上电源测试点

TP1 连接 VCC_3V3，TP2 连接 HOST_VCC_3V3，TP3 连接 VCC_5V。

- 参数与网络：`TP1=VCC_3V3`；`TP2=HOST_VCC_3V3`；`TP3=VCC_5V`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 A1-A2 的 TP2、B3-B4 的 TP1、C2 的 TP3

## 传感器

### U2 INA226AIDGSR 引脚映射

U2 的 pin10 VIN+ 接 INA_P、pin9 VIN- 接 INA_N、pin8 VBUS 接 VCC_OUT、pin6 VS+ 接 VCC_3V3、pin7 GND 接 GND、pin5 SCL 接 IIC_SCL、pin4 SDA 接 IIC_SDA、pin3 ALERT、pin2 A0、pin1 A1。

- 参数与网络：`reference=U2`；`part_number=INA226AIDGSR`；`pinout=1:A1,2:A0,3:ALERT,4:SDA,5:SCL,6:VS+,7:GND,8:VBUS,9:VIN-,10:VIN+`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 D3-D4，U2 符号四周的全部脚号、引脚名与网络名

## 模拟电路

### 5mΩ 主电流分流路径

R3 5mR 连接在 VCC_IN 与 VCC_OUT 之间，构成 J2 pin1 经 FUSE1、R3 到 J2 pin4 的主电流路径。

- 参数与网络：`shunt_reference=R3`；`shunt_resistance_ohm=0.005`；`path=J2 pin1 -> FUSE1 -> VCC_IN -> R3 -> VCC_OUT -> J2 pin4`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C3-C4，VCC_IN-R3 5mR-VCC_OUT 与 J2/FUSE1 连接

### INA226 分流检测网络

R10 0R 将 INA_P 连接 VCC_IN，R11 0R 将 INA_N 连接 VCC_OUT；INA_P 连接 U2 VIN+ pin10，INA_N 连接 U2 VIN- pin9。

- 参数与网络：`positive_sense=VCC_IN -> R10 0R -> INA_P -> U2 pin10 VIN+`；`negative_sense=VCC_OUT -> R11 0R -> INA_N -> U2 pin9 VIN-`；`filter_capacitor=C3 NC across INA_P/INA_N`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C3-D3，R10/R11、INA_P/INA_N、C3 NC 与 U2 VIN+/VIN-

### INA_P/INA_N 差分滤波焊位

C3 跨接 INA_P 与 INA_N，器件值标注 NC，原理图未给出装配电容值。

- 参数与网络：`reference=C3`；`net_a=INA_P`；`net_b=INA_N`；`schematic_value=NC`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 C3，INA_P 与 INA_N 之间的 C3，左侧标注 NC

## 其他事实

### HOST_5V 指示灯

HOST_5V 通过 R13 4.7 kΩ 串联 D2 BLUE 0603 后连接 HOST_GND。

- 参数与网络：`resistor=R13 4.7kΩ (4701) ±1%`；`led=D2 BLUE 0603`；`rail=HOST_5V`
- 证据：图 9f0f4b7d428d / 第 1 页 / 网格 B1-B2，HOST_5V-R13-D2-HOST_GND 串联支路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | HOST 与测量侧隔离架构 | `host_power=HOST_5V,HOST_VCC_3V3,HOST_GND`；`measurement_power=VCC_5V,VCC_3V3,GND`；`power_isolator=M1 B0505ST16-W5`；`signal_isolator=U1 CA-IS3020/ISO1540/ADuM1250` |
| 接口 | J1 HOST 侧接口 | `reference=J1`；`part_number=IIC_Socket_4P`；`pinout=1:HOST_I2C_SCL,2:HOST_I2C_SDA,3:HOST_5V,4:HOST_GND` |
| 电源 | U4 HOST 侧 3.3V LDO | `reference=U4`；`input=HOST_5V`；`output=HOST_VCC_3V3`；`pinout=1:IN,2:GND,3:EN,4:NC,5:OUT`；`input_capacitor=C12 4.7uF/16V`；`output_capacitor=C7 4.7uF/16V`；`test_point=TP2` |
| 其他事实 | HOST_5V 指示灯 | `resistor=R13 4.7kΩ (4701) ±1%`；`led=D2 BLUE 0603`；`rail=HOST_5V` |
| 电源 | M1 HOST_5V 输入滤波 | `input_rail=HOST_5V`；`series_inductor=L2 6.8uH`；`pre_filter_capacitor=C1 10uF/16V`；`post_filter_capacitor=C2 10uF/16V`；`module_input=M1 pin3 VIN` |
| 电源 | M1 隔离 5V 输出 | `reference=M1`；`part_number=B0505ST16-W5`；`output_pin=14:VO`；`output_rail=VCC_5V`；`return_pins=9,15,16:0V`；`output_capacitor=C5 10uF/16V`；`test_point=TP3` |
| 电源 | M1 TRIM 网络 | `trim_pin=M1 pin13 TRIM`；`output_link=R1 0Ω (0R0) ±1%`；`ground_option=R2 NC` |
| 保护电路 | 隔离侧 VCC_5V 瞬态保护 | `reference=D1`；`part_number=LESD3Z5.0CMT1G`；`protected_rail=VCC_5V`；`return=GND` |
| 核心器件 | U1 I2C 隔离器装配型号 | `reference=U1`；`schematic_value=CA-IS3020/ISO1540/ADuM1250`；`populated_part_number=null` |
| 总线 | U1 隔离 I2C 信号映射 | `sda_path=HOST_I2C_SDA -> U1 pin2 ViA -> U1 pin7 VoA -> IIC_SDA`；`scl_path=HOST_I2C_SCL -> U1 pin3 ViB -> U1 pin6 VoB -> IIC_SCL` |
| 电源 | U1 两侧隔离供电 | `host_supply=pin1 HOST_VCC_3V3,pin4 HOST_GND,C4 4.7uF/16V`；`measurement_supply=pin8 VCC_3V3,pin5 GND,C6 4.7uF/16V` |
| 总线 | HOST 侧 I2C 上拉 | `scl_pullup=R4 4.7kΩ (4701) ±1%`；`sda_pullup=R12 4.7kΩ (4701) ±1%`；`rail=HOST_VCC_3V3` |
| 电源 | U3 测量侧 3.3V LDO | `reference=U3`；`input=VCC_5V`；`output=VCC_3V3`；`pinout=1:IN,2:GND,3:EN,4:NC,5:OUT`；`input_capacitors=C10 10uF/16V,C11 100nF/16V`；`output_capacitors=C8 100nF/16V,C9 10uF/16V`；`test_point=TP1` |
| 关键网络 | PGND 与 GND 连接 | `reference=L1`；`impedance=120R@100MHz`；`net_a=PGND`；`net_b=GND` |
| 接口 | J2 高电流端子 | `reference=J2`；`part_number=THT_Male_P_1x4`；`pinout=1:FUSE1/VCC_IN,2:PGND,3:PGND,4:VCC_OUT` |
| 保护电路 | FUSE1 输入过流保护 | `reference=FUSE1`；`part_number=BSMD1206C-2120T`；`upstream=J2 pin1`；`downstream=VCC_IN` |
| 模拟电路 | 5mΩ 主电流分流路径 | `shunt_reference=R3`；`shunt_resistance_ohm=0.005`；`path=J2 pin1 -> FUSE1 -> VCC_IN -> R3 -> VCC_OUT -> J2 pin4` |
| 模拟电路 | INA226 分流检测网络 | `positive_sense=VCC_IN -> R10 0R -> INA_P -> U2 pin10 VIN+`；`negative_sense=VCC_OUT -> R11 0R -> INA_N -> U2 pin9 VIN-`；`filter_capacitor=C3 NC across INA_P/INA_N` |
| 模拟电路 | INA_P/INA_N 差分滤波焊位 | `reference=C3`；`net_a=INA_P`；`net_b=INA_N`；`schematic_value=NC` |
| 传感器 | U2 INA226AIDGSR 引脚映射 | `reference=U2`；`part_number=INA226AIDGSR`；`pinout=1:A1,2:A0,3:ALERT,4:SDA,5:SCL,6:VS+,7:GND,8:VBUS,9:VIN-,10:VIN+` |
| 电源 | INA226 供电与去耦 | `supply_pin=U2 pin6 VS+`；`supply_rail=VCC_3V3`；`ground_pin=U2 pin7 GND`；`decoupling_capacitor=C13 4.7uF/16V` |
| 总线 | INA226 I2C 总线 | `scl=U2 pin5 IIC_SCL,R9 4.7kΩ to VCC_3V3`；`sda=U2 pin4 IIC_SDA,R8 4.7kΩ to VCC_3V3` |
| 总线地址 | INA226 I2C 地址配置 | `address=0x41`；`a1_configuration=U2 pin1 -> R6 4.7kΩ -> GND`；`a0_configuration=U2 pin2 -> R7 4.7kΩ -> VCC_3V3` |
| GPIO 与控制信号 | INA226 ALERT 网络 | `alert_pin=U2 pin3 ALERT`；`resistor=R5 4.7kΩ to GND`；`external_connector=null` |
| 关键网络 | 板上电源测试点 | `TP1=VCC_3V3`；`TP2=HOST_VCC_3V3`；`TP3=VCC_5V` |

## 待确认事项

- `component.u1_variant`：U1 的器件值同时列出 CA-IS3020、ISO1540 和 ADuM1250，无法仅凭该原理图确定实际装配型号。（证据：图 9f0f4b7d428d / 第 1 页 / 网格 D2，U1 下方器件值 CA-IS3020/ISO1540/ADuM1250）
- `review.u1_populated_variant`：U1 在当前量产版本中实际装配 CA-IS3020、ISO1540 还是 ADuM1250？；原因：原理图器件值同时列出三个兼容型号，需用 BOM、贴片资料或实物丝印确定当前装配型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9f0f4b7d428ddce47924456fb544bbb274fdbc79d8b2cfa093a36ae273ee8eed` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/SCH_Unit_ina226-10A_SCH_Main_V0.3_20250625_2025_08_11_11_28_32_page_01.png` |

---

源文档：`zh_CN/unit/Unit_INA226-10A.md`

源文档 SHA-256：`1aa8e173413558cc0b64de952372c38ed06e7e0619c215f163b9fe16aba29251`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
