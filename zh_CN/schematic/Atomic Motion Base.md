# Atomic Motion Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Motion Base |
| SKU | A090 |
| 产品 ID | `atomic-motion-base-910a44802a78` |
| 源文档 | `zh_CN/atom/Atomic Motion Base.md` |

## 概述

Atomic Motion Base 由 BT1 16340 电池形成 BAT+，U1 ETA9740 将 BAT+ 转换为 5V，两颗 RZ7899 分别驱动 JP2/JP1 两路直流电机，四个 JP3-JP6 三针接口由 BAT+ 供电。U3 STM32F030F4P6 通过 M1F/M1R 和 M2F/M2R 控制两颗电机驱动器，并以 PA0-PA3 控制四路三针接口。Atom 的 G21/G25 通过 SCL/SDA 连接 STM32，G22/G19 和 G23/G33 分别接到两组 Grove 接口。

## 检索关键词

`Atomic Motion Base`、`A090`、`STM32F030F4P6`、`ETA9740`、`RZ7899`、`16340`、`BAT+`、`5V boost`、`M1F`、`M1R`、`M2F`、`M2R`、`PA0`、`PA1`、`PA2`、`PA3`、`SCL`、`SDA`、`SWDIO`、`SWCLK`、`NRST`、`JP1 motor`、`JP2 motor`、`JP3 JP4 JP5 JP6`、`GROVE`、`GPIO21`、`GPIO25`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO33`、`Fuse 5A`、`SS-12F23`、`DSS34`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ETA9740 | 以 BAT+ 为输入并产生 5V 的升压电源芯片 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左上，U1 ETA9740 的 SW/BAT/ISET/PGND/AGND、OUT 与 LED1-LED3 |
| U2,U4 | RZ7899 | 分别接收 M2F/M2R 与 M1F/M1R 并驱动 JP1/JP2 的双向电机驱动器 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左中，U2/U4 RZ7899 的 OUTF/OUTR、VCC/GND 与 INF/INR |
| U3 | STM32F030F4P6 | 协调两路电机、四路三针输出、Atom I2C 和 SWD 调试的控制器 | 图 cacac3d1e29e / 第 1 页 / 第 1 页中央，U3 STM32F030F4P6 的 PA0-PA14、PB1、电源、NRST 与 SWD 网络 |
| BT1 | 16340 | 为 BAT+ 电源域提供电池连接 | 图 cacac3d1e29e / 第 1 页 / 第 1 页上方中右，BT1 16340 上端接 BAT+，下端经 Fuse 5A 接开关 |
| S? | SS-12F23 | 通过电池回路与 GND 的接通或断开控制电源 | 图 cacac3d1e29e / 第 1 页 / 第 1 页上方中央，S? SS-12F23，pin2 接 GND、pin3 经 Fuse 5A 接 BT1 下端、pin1 未接外部网络 |
| Fuse | FUSE 5A | 串联在 BT1 下端与开关 pin3 之间的电池回路保护器件 | 图 cacac3d1e29e / 第 1 页 / 第 1 页上方中央，Fuse/FUSE 5A 位于 S? pin3 与 BT1 下端之间 |
| JP1,JP2 | 2-pin connector | 分别引出 U2 与 U4 的 OUTF/OUTR 电机输出 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左中，JP1/JP2 两针接口与 U2/U4 OUTF/OUTR 并联输出脚 |
| JP3,JP4,JP5,JP6 | 3-pin connector | 四路 BAT+ 供电、GND 回路和 STM32 PA0-PA3 控制信号接口 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左下，JP3-JP6 的 BAT+/GND 与四条连到 U3 PA0-PA3 的信号线 |
| ATOM | Atom 9-pin socket | 提供 3V3、5V、GND、I2C 和两组 Grove GPIO | 图 cacac3d1e29e / 第 1 页 / 第 1 页中下 ATOM，pin1-pin9 与 G21/G25/G22/G19/G23/G33、5V、3V3、GND |
| J1,J2 | GROVE | 两组 IO2/IO1/5V/GND 四针扩展接口 | 图 cacac3d1e29e / 第 1 页 / 第 1 页右下，J1/J2 GROVE 的 pin4 IO2、pin3 IO1、pin2 5V、pin1 GND |
| J3 | SWD | 接出 NRST、SWCLK、SWDIO、3V3 和 GND 的调试接口 | 图 cacac3d1e29e / 第 1 页 / 第 1 页右中，J3 SWD，RST/CLK/DIO/VCC/GND 分别接 NRST/SWCLK/SWDIO/3V3/GND |
| D1 | DSS34 | 跨接 BAT+ 与 GND 的二极管 | 图 cacac3d1e29e / 第 1 页 / 第 1 页右上，D1 DSS34 连接 BAT+ 与 GND |
| L1,R2 | 3.3uH 4012 / 150KΩ | ETA9740 的开关电感和 ISET 设定网络 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左上，L1 3.3uH 4012 位于 BAT+ 与 U1 SW，R2 150K 从 ISET pin6 接 GND |
| C1-C11 | 106 / 475 / 104 | BAT+、5V、3V3 和 STM32 电源去耦电容组 | 图 cacac3d1e29e / 第 1 页 / 第 1 页顶部 C1-C5/C7-C11 与中央 C6，分别连接 BAT+、5V、3V3 和 GND |

## 系统结构

### Atomic Motion Base 运动控制架构

BT1 建立 BAT+ 电源域，U1 ETA9740 产生 5V；U3 STM32F030F4P6 控制两颗 RZ7899 的两路电机输出和 JP3-JP6 四路三针接口，并通过 SCL/SDA 与 Atom 连接，Atom 另行直连两组 Grove。

- 参数与网络：`battery=BT1 16340`；`boost_converter=U1 ETA9740`；`controller=U3 STM32F030F4P6`；`motor_drivers=U4/U2 RZ7899`；`motor_outputs=JP2/JP1`；`three_pin_outputs=JP3-JP6`；`host_bus=Atom G21/G25 SCL/SDA`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页完整单页原理图，顶部电源、左侧驱动/接口、中央 STM32、右下 Atom/Grove

## 核心器件

### RZ7899 双路电机驱动连接

U4 VCC pin4 接 BAT+、GND pin3 接 GND，INF pin2=M1F、INR pin1=M1R，OUTF pins5/6 与 OUTR pins7/8 接 JP2；U2 采用同一供电，INF pin2=M2F、INR pin1=M2R，输出接 JP1。

- 参数与网络：`U4_supply=pin4 BAT+, pin3 GND`；`U4_inputs=pin2 M1F, pin1 M1R`；`U4_outputs=pins5/6 OUTF, pins7/8 OUTR -> JP2`；`U2_supply=pin4 BAT+, pin3 GND`；`U2_inputs=pin2 M2F, pin1 M2R`；`U2_outputs=pins5/6 OUTF, pins7/8 OUTR -> JP1`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左中，U4/U2 RZ7899 与 JP2/JP1、BAT+/GND、M1F/M1R/M2F/M2R

## 电源

### BT1 电池回路、开关和保险丝

BT1 16340 上端接 BAT+，下端经 FUSE 5A 接 S? SS-12F23 pin3；开关 pin2 接 GND，pin1 未接外部网络。

- 参数与网络：`battery_positive=BT1 upper terminal BAT+`；`battery_return=BT1 lower terminal -> FUSE 5A -> switch pin3`；`switch_common=pin2 GND`；`unused_contact=pin1 no external net`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页上方中央，BT1/Fuse/S? 到 BAT+ 和 GND 的完整回路

### ETA9740 BAT+ 到 5V 转换

U1 ETA9740 的 BAT 输入接 BAT+，SW 通过 L1 3.3uH 4012 接 BAT+，OUT pin7 输出 5V；ISET pin6 通过 R2 150KΩ 接 GND，PGND pin8 与 AGND 接 GND。

- 参数与网络：`input=BAT+`；`switch_inductor=L1 3.3uH 4012`；`output=OUT pin7 5V`；`current_set=ISET pin6 through R2 150K to GND`；`grounds=PGND pin8 and AGND GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左上，BAT+/L1/U1 ETA9740/R2 与 5V 输出

### BAT+、5V 与 3V3 去耦

C1 106 与 C2 475 连接 BAT+ 到 GND；C3/C4/C5 106 和 C11 104 连接 U1 输出 5V 到 GND；C7 475 连接 5V 到 GND；C8 475 与 C9/C10 104 连接 3V3 到 GND；C6 104 位于 STM32 的 3V3-GND。

- 参数与网络：`BAT+=C1 106, C2 475`；`U1_5V_output=C3/C4/C5 106, C11 104`；`5V_distribution=C7 475`；`3V3_distribution=C8 475, C9/C10 104`；`MCU_3V3=C6 104`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页顶部 C1-C5/C7-C11 与 U3/J3 附近 C6

### STM32F030F4P6 电源与去耦

U3 VDDA pin5 与 VDD pin16 接 3V3，VSS pin15 接 GND，C6 104 连接 3V3 与 GND。

- 参数与网络：`VDDA=pin5 3V3`；`VDD=pin16 3V3`；`VSS=pin15 GND`；`decoupling=C6 104 from 3V3 to GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 VDDA/VDD/VSS 与右侧 C6 104 的 3V3-GND 连接

## 接口

### JP1/JP2 电机输出

JP2 pin2 接 U4 OUTF pins5/6，pin1 接 U4 OUTR pins7/8；JP1 pin2 接 U2 OUTF pins5/6，pin1 接 U2 OUTR pins7/8。

- 参数与网络：`JP2=pin2 U4 OUTF, pin1 U4 OUTR`；`JP1=pin2 U2 OUTF, pin1 U2 OUTR`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左中，JP2/JP1 两针编号到 U4/U2 OUTF/OUTR 的线路

### JP3-JP6 三针接口映射

JP3 pin3=U3 PA0、pin2=BAT+、pin1=GND；JP4 pin3=PA1、pin2=BAT+、pin1=GND；JP5 pin1=PA2、pin2=BAT+、pin3=GND；JP6 pin1=PA3、pin2=BAT+、pin3=GND。

- 参数与网络：`JP3=pin3 PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 PA3, pin2 BAT+, pin3 GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左下 JP3-JP6 针脚编号、BAT+/GND 与连到 U3 PA0-PA3 的四条信号线

### Atom 电源与 GPIO 针脚

Atom pin9=3V3、pin8=G22、pin7=G21/SCL、pin6=G19、pin5=G25/SDA、pin4=G23、pin3=5V、pin2=G33、pin1=GND。

- 参数与网络：`pin9=3V3`；`pin8=G22`；`pin7=G21 SCL`；`pin6=G19`；`pin5=G25 SDA`；`pin4=G23`；`pin3=5V`；`pin2=G33`；`pin1=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中下 ATOM 符号的 pin1-pin9、G21/G25/G22/G19/G23/G33 与电源标注

### J1/J2 Grove GPIO 映射

J1 GROVE 的 pin4 IO2 接 Atom G23 pin4，pin3 IO1 接 G33 pin2，pin2=5V、pin1=GND；J2 的 pin4 IO2 接 G22 pin8，pin3 IO1 接 G19 pin6，pin2=5V、pin1=GND。

- 参数与网络：`J1=pin4 G23, pin3 G33, pin2 5V, pin1 GND`；`J2=pin4 G22, pin3 G19, pin2 5V, pin1 GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页右下，ATOM 右侧 G22/G19/G23/G33 到 J2/J1 IO2/IO1 的线路

## 总线

### Atom 与 STM32 的 SCL/SDA 总线

Atom G21 pin7 通过 SCL 连接 U3 PA9 pin17，Atom G25 pin5 通过 SDA 连接 U3 PA10 pin18。

- 参数与网络：`SCL=Atom G21 pin7 <-> U3 PA9 pin17`；`SDA=Atom G25 pin5 <-> U3 PA10 pin18`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央，ATOM G21/G25 的 SCL/SDA 网络到 U3 PA9/PA10

## GPIO 与控制信号

### STM32 电机控制 GPIO

U3 PA4 pin10 输出 M1F，PB1 pin14 输出 M1R，PA6 pin12 输出 M2F，PA7 pin13 输出 M2R，并分别连接 U4/U2 的 INF/INR。

- 参数与网络：`PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 的 PA4/PB1/PA6/PA7 与左侧 U4/U2 同名 M1F/M1R/M2F/M2R 网络

### STM32 四路三针接口控制

U3 PA0 pin6、PA1 pin7、PA2 pin8、PA3 pin9 分别连接 JP3、JP4、JP5、JP6 的信号针。

- 参数与网络：`PA0_pin6=JP3 pin3`；`PA1_pin7=JP4 pin3`；`PA2_pin8=JP5 pin1`；`PA3_pin9=JP6 pin1`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 PA0-PA3 到左下 JP3-JP6 的四条独立线路

## 保护电路

### BAT+ 对地二极管

D1 DSS34 连接在 BAT+ 与 GND 之间。

- 参数与网络：`device=D1 DSS34`；`rail=BAT+`；`return=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页右上，D1 DSS34 的 BAT+-GND 连接

## 调试与烧录

### STM32 SWD 调试接口

U3 NRST pin4、PA14/DCK pin20 的 SWCLK、PA13/DIO pin19 的 SWDIO 与 3V3/GND 一同接至 J3 SWD 的 RST/CLK/DIO/VCC/GND。

- 参数与网络：`RST=U3 NRST pin4`；`CLK=U3 PA14/DCK pin20 SWCLK`；`DIO=U3 PA13/DIO pin19 SWDIO`；`VCC=3V3`；`GND=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 NRST/SWCLK/SWDIO 与右中 J3 SWD

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Motion Base 运动控制架构 | `battery=BT1 16340`；`boost_converter=U1 ETA9740`；`controller=U3 STM32F030F4P6`；`motor_drivers=U4/U2 RZ7899`；`motor_outputs=JP2/JP1`；`three_pin_outputs=JP3-JP6`；`host_bus=Atom G21/G25 SCL/SDA` |
| 电源 | BT1 电池回路、开关和保险丝 | `battery_positive=BT1 upper terminal BAT+`；`battery_return=BT1 lower terminal -> FUSE 5A -> switch pin3`；`switch_common=pin2 GND`；`unused_contact=pin1 no external net` |
| 电源 | ETA9740 BAT+ 到 5V 转换 | `input=BAT+`；`switch_inductor=L1 3.3uH 4012`；`output=OUT pin7 5V`；`current_set=ISET pin6 through R2 150K to GND`；`grounds=PGND pin8 and AGND GND` |
| 电源 | BAT+、5V 与 3V3 去耦 | `BAT+=C1 106, C2 475`；`U1_5V_output=C3/C4/C5 106, C11 104`；`5V_distribution=C7 475`；`3V3_distribution=C8 475, C9/C10 104`；`MCU_3V3=C6 104` |
| 保护电路 | BAT+ 对地二极管 | `device=D1 DSS34`；`rail=BAT+`；`return=GND` |
| 核心器件 | RZ7899 双路电机驱动连接 | `U4_supply=pin4 BAT+, pin3 GND`；`U4_inputs=pin2 M1F, pin1 M1R`；`U4_outputs=pins5/6 OUTF, pins7/8 OUTR -> JP2`；`U2_supply=pin4 BAT+, pin3 GND`；`U2_inputs=pin2 M2F, pin1 M2R`；`U2_outputs=pins5/6 OUTF, pins7/8 OUTR -> JP1` |
| 接口 | JP1/JP2 电机输出 | `JP2=pin2 U4 OUTF, pin1 U4 OUTR`；`JP1=pin2 U2 OUTF, pin1 U2 OUTR` |
| GPIO 与控制信号 | STM32 电机控制 GPIO | `PA4_pin10=M1F -> U4 INF pin2`；`PB1_pin14=M1R -> U4 INR pin1`；`PA6_pin12=M2F -> U2 INF pin2`；`PA7_pin13=M2R -> U2 INR pin1` |
| 接口 | JP3-JP6 三针接口映射 | `JP3=pin3 PA0, pin2 BAT+, pin1 GND`；`JP4=pin3 PA1, pin2 BAT+, pin1 GND`；`JP5=pin1 PA2, pin2 BAT+, pin3 GND`；`JP6=pin1 PA3, pin2 BAT+, pin3 GND` |
| GPIO 与控制信号 | STM32 四路三针接口控制 | `PA0_pin6=JP3 pin3`；`PA1_pin7=JP4 pin3`；`PA2_pin8=JP5 pin1`；`PA3_pin9=JP6 pin1` |
| 总线 | Atom 与 STM32 的 SCL/SDA 总线 | `SCL=Atom G21 pin7 <-> U3 PA9 pin17`；`SDA=Atom G25 pin5 <-> U3 PA10 pin18` |
| 接口 | Atom 电源与 GPIO 针脚 | `pin9=3V3`；`pin8=G22`；`pin7=G21 SCL`；`pin6=G19`；`pin5=G25 SDA`；`pin4=G23`；`pin3=5V`；`pin2=G33`；`pin1=GND` |
| 接口 | J1/J2 Grove GPIO 映射 | `J1=pin4 G23, pin3 G33, pin2 5V, pin1 GND`；`J2=pin4 G22, pin3 G19, pin2 5V, pin1 GND` |
| 电源 | STM32F030F4P6 电源与去耦 | `VDDA=pin5 3V3`；`VDD=pin16 3V3`；`VSS=pin15 GND`；`decoupling=C6 104 from 3V3 to GND` |
| 调试与烧录 | STM32 SWD 调试接口 | `RST=U3 NRST pin4`；`CLK=U3 PA14/DCK pin20 SWCLK`；`DIO=U3 PA13/DIO pin19 SWDIO`；`VCC=3V3`；`GND=GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cacac3d1e29ea7035c746de97a331103b07bb0ab32a5b1c7d70c35724b57b915` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-e3e37376-655b-4193-aa31-b44c116df5ff.webp` |

---

源文档：`zh_CN/atom/Atomic Motion Base.md`

源文档 SHA-256：`102ca413bbdea9890e4acd3e4b498d7d270b321602f5a0f83ff53916b553c289`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
