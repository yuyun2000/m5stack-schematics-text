# Unit AC Measure 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit AC Measure |
| SKU | U164 |
| 产品 ID | `unit-ac-measure-661899298cfe` |
| 源文档 | `zh_CN/unit/AC Measure Unit.md` |

## 概述

Unit AC Measure 由交流计量侧和低压逻辑侧构成：HLW8032（IC2）通过零线分流电阻与火线高阻分压链采集交流信号，STM32G030F6（U4）负责 I2C 通信和数据处理。B0505ST16-W5（U2）从 VCC_5V 产生隔离的 VCC_8032/GND_8032，EL357N(C)(TA)-G（IC1）将 HLW8032 的 TX 单向隔离到逻辑侧 RX。逻辑侧 Grove 接口提供 VCC_5V、SCL、SDA 和 GND，HX6306P332MR（U3）生成 VCC_3V3，板上另有 SWD、NRST 和红色状态 LED。交流端 P1 引出 AC_L_IN/OUT 与 AC_N_IN/OUT，FUSE1 串接火线；原理图没有印出 I2C 地址或完整测量范围。

## 检索关键词

`Unit AC Measure`、`U164`、`STM32G030F6`、`HLW8032`、`B0505ST16-W5`、`EL357N(C)(TA)-G`、`HX6306P332MR`、`HT3.96 4P`、`GROVE 4P`、`SWD_5P`、`I2C`、`0x42`、`SCL`、`SDA`、`RX`、`TX`、`AC_L_IN`、`AC_L_OUT`、`AC_N_IN`、`AC_N_OUT`、`VCC_5V`、`VCC_3V3`、`VCC_8032`、`GND_8032`、`FUSE1`、`TBT10A250V`、`MA251230R00MZ`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`PA3`、`PB7/PB8`、`PB9/PC14-OSC32_IN`、`470K/1%`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | STM32G030F6 | 逻辑侧主控，连接 I2C、隔离后的 RX、状态 LED、NRST 和 SWD | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 C1-D2：U4 STM32G030F6 及 SCL/SDA/RX/MCU_SWDIO/MCU_SWCLK/NRST 引脚 |
| IC2 | HLW8032 | 隔离计量侧交流电压与电流采集芯片，通过 TX 输出测量数据 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A3：IC2 HLW8032，VDD/I_P/I_N/V_P/GND/TX/PF/RX 引脚 |
| U2 | B0505ST16-W5 | 从逻辑侧 VCC_5V 产生隔离的 VCC_8032 电源域 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B3-C4：U2 B0505ST16-W5，虚线隔离边界两侧为 VCC_5V/GND 与 VCC_8032/GND_8032 |
| IC1 | EL357N(C)(TA)-G | 将 HLW8032 TX 信号光耦隔离后送到逻辑侧 RX | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A4：IC1 EL357N(C)(TA)-G，输入侧接 VCC_8032/TX，输出侧接 RX/VCC_3V3/GND |
| U3 | HX6306P332MR | 将 VCC_5V 转换为逻辑侧 VCC_3V3 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B2-C2：U3 HX6306P332MR，VIN pin 3 接 VCC_5V、VOUT pin 2 经 FB1 到 VCC_3V3、GND pin 1 接地 |
| P1 | HT3.96 4P | 交流输入/输出端子，引出火线与零线的 IN/OUT 网络 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A1：P1 HT3.96 4P，pin 4~1 标为 AC_L_OUT、AC_N_OUT、AC_L_IN、AC_N_IN |
| J2 | GROVE 4P | 逻辑侧 VCC_5V 供电与 I2C 接口 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1-C1：J2 GROVE 4P，SCL、SDA、VCC_5V、GND |
| J1 | SWD_5P | 主控烧录和调试接口 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 D3：J1 SWD_5P，1~5 脚连接 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND |
| FUSE1 | TBT10A250V | 串联在 AC_L_IN 与 AC_L_OUT 之间的火线保险丝 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1：AC_L_IN-FUSE1(TBT10A250V)-AC_L_OUT 串联路径 |
| R5 | MA251230R00MZ | 位于 AC_N_OUT 与 AC_N_IN/GND_8032 路径上的电流分流电阻 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A2：R5 标注 MA251230R00MZ，跨接 AC_N_OUT 与 AC_N_IN/GND_8032 节点 |
| R1/R6/C1/C3 | 1K/1% / 33nF/16V/10% | HLW8032 I_P/I_N 差分电流输入的串联与对地滤波网络 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A2-A3：R1/R6 各 1K/1%，C1/C3 各 33nF/16V/10%，连接 IC2 I_P/I_N 与 GND_8032 |
| R9-R12/R8/C5 | 470K/1% / 1K/1% / 100nF/50V/10% | AC_L_OUT 到 HLW8032 V_P 的高阻分压和滤波网络 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B2-B3：AC_L_OUT 经 R9~R12 四只 470K/1% 到 IC2 V_P，R8 1K/1% 与 C5 100nF/50V/10% 接 GND_8032 |
| R2/R3/R4 | 470R/1% / 1.6K/1% / 3.3K/1% | IC1 光耦输入限流、RX 上拉和输出侧回路电阻 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 A4：R2 从 VCC_8032 到 IC1 pin 1，R3 从 VCC_3V3 到 RX，R4 从 IC1 pin 3 到 GND |
| FB1 | 330R/GZ1005D331TF | U3 输出到 VCC_3V3 之间的电源磁珠 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B2-C2：U3 VOUT 与 VCC_3V3 之间 FB1 标注 330R/GZ1005D331TF |
| R14/R15 | 4.7KΩ | SCL/SDA 到 VCC_3V3 的 I2C 上拉电阻 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1-C1：R14/R15 均为 4.7K，上端接 VCC_3V3，下端接 SCL/SDA |
| R7/C8 | 10K/1% / 100nF/50V/10% | U4 NRST 上拉与对地复位电容 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 C2-D2：NRST 经 R7 10K/1% 接 VCC_3V3，并经 C8 100nF/50V/10% 接 GND |
| D1/R13 | Red 0603 / 1K/1% | 由 U4 PA4 驱动的红色状态指示支路 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 C1：U4 PA4 pin 11 经 D1 Red 0603、R13 1K/1% 接 GND |
| C10/C11/C12 | 100nF/50V/10% | U2 隔离电源输入侧和输出侧去耦电容 | 图 f41ba93e6497 / 第 1 页 / 页 1 网格 B3-C4：C10/C11 跨 VCC_5V-GND，C12 跨 VCC_8032-GND_8032 |

## 系统结构

### Unit AC Measure

P1 的交流线路经分流与高阻分压网络进入 IC2 HLW8032，IC2 TX 经 IC1 光耦单向送到 U4 STM32G030F6；U2 为计量侧提供隔离电源，U4 通过 J2 的 SCL/SDA 对外通信。

- 参数与网络：`metering_ic=IC2 HLW8032`；`controller=U4 STM32G030F6`；`power_isolation=U2 B0505ST16-W5`；`signal_isolation=IC1 EL357N(C)(TA)-G`；`external_bus=J2 SCL/SDA`；`ac_connector=P1 HT3.96 4P`
- 证据：图 f41ba93e6497 / 第 1 页 / 整页：P1/FUSE1/HLW8032 测量链、IC1 光耦、U2 隔离电源、U4/J2 逻辑侧

## 核心器件

### IC2 HLW8032

IC2 VDD pin 1 接 VCC_8032，I_P pin 2 和 I_N pin 3 接分流采样网络，V_P pin 4 接电压分压网络，GND pin 5 接 GND_8032，TX pin 6 连接光耦输入；PF pin 7 与 RX pin 8 未接。

- 参数与网络：`pin_1=VDD,VCC_8032`；`pin_2=I_P`；`pin_3=I_N`；`pin_4=V_P`；`pin_5=GND,GND_8032`；`pin_6=TX to IC1`；`pin_7=PF no-connect`；`pin_8=RX no-connect`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A3：IC2 周围 1~8 脚名称、网络和未连接端点

## 电源

### U2 B0505ST16-W5

U2 的 CTRL pin 1 与 VIN pin 3 接 VCC_5V，输入 GND pin 2 接逻辑 GND；VO pin 14 输出 VCC_8032，0V pins 9/15/16 接 GND_8032，构成隔离计量电源域。

- 参数与网络：`input_rail=VCC_5V`；`input_ground=GND`；`control_pin=pin 1 CTRL to VCC_5V`；`input_pin=pin 3 VIN`；`output_pin=pin 14 VO`；`output_rail=VCC_8032`；`output_ground=pins 9,15,16 to GND_8032`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B3-C4：U2 左右两侧引脚和虚线隔离边界

### U2 输入/输出去耦

C10 与 C11 均为 100nF/50V/10%，跨接 VCC_5V 与 GND；C12 100nF/50V/10% 跨接 VCC_8032 与 GND_8032。

- 参数与网络：`input_capacitors=C10,C11; 100nF/50V/10%`；`input_domains=VCC_5V,GND`；`output_capacitor=C12 100nF/50V/10%`；`output_domains=VCC_8032,GND_8032`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B3-C4：U2 周围 C10/C11/C12 与两侧电源域

### U3 HX6306P332MR

U3 VIN pin 3 接 VCC_5V，VOUT pin 2 经 FB1 330R/GZ1005D331TF 输出 VCC_3V3，GND pin 1 接地；C4 位于输入侧，C6/C7 位于输出滤波路径。

- 参数与网络：`input=VCC_5V at VIN pin 3`；`output=VOUT pin 2 via FB1 to VCC_3V3`；`ground=GND pin 1`；`ferrite=FB1 330R/GZ1005D331TF`；`input_capacitor=C4 100nF/50V/10%`；`output_capacitors=C6,C7`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B2-C2：U3、C4/C6/C7、FB1 与 VCC_5V/VCC_3V3/GND

### GND 与 GND_8032

逻辑侧使用 GND/VCC_5V/VCC_3V3，计量侧使用 GND_8032/VCC_8032；两侧通过 U2 的隔离电源和 IC1 光耦跨越图示虚线隔离边界。

- 参数与网络：`logic_ground=GND`；`logic_rails=VCC_5V,VCC_3V3`；`meter_ground=GND_8032`；`meter_rail=VCC_8032`；`power_barrier=U2`；`signal_barrier=IC1`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B3-D3：U2 内部虚线及贯穿下半页的蓝色虚线，两侧 GND/GND_8032 与电源网络

### U4 电源

U4 VDDA/DDA pin 4 接 VCC_3V3，VSSA/SSA pin 5 接 GND，C9 100nF/50V/10% 跨接 VCC_3V3 与 GND。

- 参数与网络：`supply_pin=VDDA/DDA pin 4 to VCC_3V3`；`ground_pin=VSSA/SSA pin 5 to GND`；`decoupling=C9 100nF/50V/10%`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 D1-D2：U4 pins 4/5、VCC_3V3/GND 和 C9

## 接口

### P1 HT3.96 4P

P1 pin 4 接 AC_L_OUT，pin 3 接 AC_N_OUT，pin 2 接 AC_L_IN，pin 1 接 AC_N_IN。

- 参数与网络：`pin_4=AC_L_OUT`；`pin_3=AC_N_OUT`；`pin_2=AC_L_IN`；`pin_1=AC_N_IN`；`connector=HT3.96 4P`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A1：P1 pin 4~1 与四条 AC_L_OUT/AC_N_OUT/AC_L_IN/AC_N_IN 网络

### J2 GROVE 4P

J2 的 SCL 与 SDA 为 I2C 信号，5V 端接 VCC_5V，GND 端接逻辑 GND。

- 参数与网络：`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`connector=GROVE 4P`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1-C1：J2 端子与 SCL/SDA/VCC_5V/GND 网络

## 总线

### HLW8032 到 STM32 的串行数据

IC2 TX pin 6 驱动 IC1 输入侧，IC1 输出侧形成 RX 网络，RX 连接 U4 PA3 pin 10；原理图仅显示计量侧到主控侧的单向数据路径。

- 参数与网络：`source=IC2 TX pin 6`；`isolation=IC1 EL357N(C)(TA)-G`；`logic_net=RX`；`destination=U4 PA3 pin 10`；`direction=IC2 to U4`；`reverse_path=null`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A3-A4 与 C1：IC2 TX→IC1→RX 同名网络→U4 PA3 pin 10

### U4 I2C

SCL 从 J2 连接 U4 pin 1（PB7/PB8），SDA 从 J2 连接 U4 pin 2（PB9/PC14-OSC32_IN）；R14/R15 各 4.7KΩ 将两线拉至 VCC_3V3。

- 参数与网络：`controller=U4 STM32G030F6`；`scl=U4 pin 1 PB7/PB8`；`sda=U4 pin 2 PB9/PC14-OSC32_IN`；`pullups=R14,R15 4.7K to VCC_3V3`；`connector=J2`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1-D2：J2/R14/R15 的 SCL/SDA 同名网络及 U4 pins 1/2

## GPIO 与控制信号

### U4 关键 GPIO

U4 pin 1（PB7/PB8）接 SCL，pin 2（PB9/PC14-OSC32_IN）接 SDA，PA3 pin 10 接 RX，PA4 pin 11 驱动 D1，PA13(SWDIO) pin 18 接 MCU_SWDIO，PA15/PA14-BOOT0(SWCLK) pin 19 接 MCU_SWCLK。

- 参数与网络：`pin_1=PB7/PB8,SCL`；`pin_2=PB9/PC14-OSC32_IN,SDA`；`pin_10=PA3,RX`；`pin_11=PA4,D1`；`pin_18=PA13(SWDIO),MCU_SWDIO`；`pin_19=PA15/PA14-BOOT0(SWCLK),MCU_SWCLK`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 C1-D2：U4 周围信号名、GPIO 复用名和 pin 编号

## 时钟

### U4 振荡器引脚

U4 pin 2 的复用标注包含 PC14-OSC32_IN，但该脚用于 SDA；PC15-OSC32_OUT pin 3 未连接，页面未绘出外部晶振或振荡器。

- 参数与网络：`osc_in_mux=pin 2 PB9/PC14-OSC32_IN used as SDA`；`osc_out=pin 3 PC15-OSC32_OUT no-connect`；`external_clock_component=null`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 C1-C2：U4 pins 2/3 的 PB9/PC14-OSC32_IN 与 PC15-OSC32_OUT 标注及未连接端点

## 复位

### U4 NRST

U4 NRST pin 6 接 NRST 网络，R7 10K/1% 将其上拉至 VCC_3V3，C8 100nF/50V/10% 接 GND，NRST 同时引至 J1 pin 4。

- 参数与网络：`mcu_pin=NRST pin 6`；`pullup=R7 10K/1% to VCC_3V3`；`capacitor=C8 100nF/50V/10% to GND`；`debug_header=J1 pin 4`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 C2-D3：U4 NRST pin 6、R7/C8 和 J1 pin 4 同名 NRST 网络

## 保护电路

### FUSE1

FUSE1 TBT10A250V 串联在 AC_L_IN 与 AC_L_OUT 之间。

- 参数与网络：`reference=FUSE1`；`part_number=TBT10A250V`；`input_net=AC_L_IN`；`output_net=AC_L_OUT`；`path=line conductor`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1：AC_L_IN-FUSE1-AC_L_OUT 横向串联连接

### IC1 光耦隔离

IC1 输入侧由 VCC_8032 经 R2 470R/1% 接 pin 1，IC2 TX 接 pin 2；输出侧 pin 4 为 RX 并经 R3 1.6K/1% 上拉至 VCC_3V3，pin 3 经 R4 3.3K/1% 接 GND。

- 参数与网络：`input_supply=VCC_8032 via R2 470R/1%`；`input_signal=TX at pin 2`；`output_signal=RX at pin 4`；`output_pullup=R3 1.6K/1% to VCC_3V3`；`output_return=pin 3 via R4 3.3K/1% to GND`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A4：IC1 pins 1~4、R2/R3/R4、VCC_8032/TX/RX/VCC_3V3/GND

## 关键网络

### 电源域索引

VCC_5V/GND 为 Grove 输入和逻辑侧原始电源，U3 生成 VCC_3V3；U2 隔离输出 VCC_8032/GND_8032，为 HLW8032、其采样网络和光耦输入侧供电。

- 参数与网络：`input_domain=VCC_5V,GND`；`logic_domain=VCC_3V3,GND`；`meter_domain=VCC_8032,GND_8032`；`logic_regulator=U3`；`isolated_converter=U2`；`meter_loads=IC2,IC1 input,R1/R6/C1/C3,R8/C5`
- 证据：图 f41ba93e6497 / 第 1 页 / 整页同名电源网络：J2/U3/U4 的 VCC_5V/VCC_3V3/GND 与 U2/IC2/IC1 的 VCC_8032/GND_8032

## 调试与烧录

### D1 红色 LED

U4 PA4 pin 11 经 D1 Red 0603 和 R13 1K/1% 连接到 GND，形成主控驱动的状态指示支路。

- 参数与网络：`controller_pin=U4 PA4 pin 11`；`led=D1 Red 0603`；`resistor=R13 1K/1%`；`return=GND`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 C1：U4 pin 11-PA4 至 D1/R13/GND 的横向支路

### J1 SWD_5P

J1 pin 1 接 VCC_3V3，pin 2 接 MCU_SWCLK，pin 3 接 MCU_SWDIO，pin 4 接 NRST，pin 5 接 GND。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 D3：J1 SWD_5P 的 1~5 脚和五条网络

## 模拟电路

### R5 电流分流路径

R5 MA251230R00MZ 位于 AC_N_OUT 与 AC_N_IN/GND_8032 节点之间，R5 两端分别通过 R1 和 R6 送往 HLW8032 的 I_P 与 I_N。

- 参数与网络：`shunt=R5 MA251230R00MZ`；`high_side_net=AC_N_OUT`；`low_side_net=AC_N_IN,GND_8032`；`positive_path=R1 1K/1% to I_P`；`negative_path=R6 1K/1% to I_N`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A2-A3：AC_N_OUT/R5/AC_N_IN、R1/R6 与 IC2 I_P/I_N

### HLW8032 I_P/I_N

R1 与 R6 均为 1K/1%，串接到 IC2 I_P pin 2 和 I_N pin 3；C1 与 C3 均为 33nF/16V/10%，从两条输入支路接到 GND_8032。

- 参数与网络：`i_p=IC2 pin 2 via R1 1K/1%`；`i_n=IC2 pin 3 via R6 1K/1%`；`i_p_capacitor=C1 33nF/16V/10% to GND_8032`；`i_n_capacitor=C3 33nF/16V/10% to GND_8032`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 A2-A3：R1/C1 与 R6/C3 进入 IC2 I_P/I_N 的对称网络

### HLW8032 V_P

AC_L_OUT 经 R9、R10、R11、R12 四只 470K/1% 串联电阻送到 IC2 V_P pin 4，V_P 节点由 R8 1K/1% 和 C5 100nF/50V/10% 接至 GND_8032。

- 参数与网络：`source=AC_L_OUT`；`series_chain=R9,R10,R11,R12; each 470K/1%`；`meter_pin=IC2 V_P pin 4`；`low_resistor=R8 1K/1% to GND_8032`；`filter_capacitor=C5 100nF/50V/10% to GND_8032`
- 证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B2-B3：AC_L_OUT、R9~R12、R8/C5 与 IC2 V_P pin 4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit AC Measure | `metering_ic=IC2 HLW8032`；`controller=U4 STM32G030F6`；`power_isolation=U2 B0505ST16-W5`；`signal_isolation=IC1 EL357N(C)(TA)-G`；`external_bus=J2 SCL/SDA`；`ac_connector=P1 HT3.96 4P` |
| 接口 | P1 HT3.96 4P | `pin_4=AC_L_OUT`；`pin_3=AC_N_OUT`；`pin_2=AC_L_IN`；`pin_1=AC_N_IN`；`connector=HT3.96 4P` |
| 保护电路 | FUSE1 | `reference=FUSE1`；`part_number=TBT10A250V`；`input_net=AC_L_IN`；`output_net=AC_L_OUT`；`path=line conductor` |
| 模拟电路 | R5 电流分流路径 | `shunt=R5 MA251230R00MZ`；`high_side_net=AC_N_OUT`；`low_side_net=AC_N_IN,GND_8032`；`positive_path=R1 1K/1% to I_P`；`negative_path=R6 1K/1% to I_N` |
| 模拟电路 | HLW8032 I_P/I_N | `i_p=IC2 pin 2 via R1 1K/1%`；`i_n=IC2 pin 3 via R6 1K/1%`；`i_p_capacitor=C1 33nF/16V/10% to GND_8032`；`i_n_capacitor=C3 33nF/16V/10% to GND_8032` |
| 模拟电路 | HLW8032 V_P | `source=AC_L_OUT`；`series_chain=R9,R10,R11,R12; each 470K/1%`；`meter_pin=IC2 V_P pin 4`；`low_resistor=R8 1K/1% to GND_8032`；`filter_capacitor=C5 100nF/50V/10% to GND_8032` |
| 核心器件 | IC2 HLW8032 | `pin_1=VDD,VCC_8032`；`pin_2=I_P`；`pin_3=I_N`；`pin_4=V_P`；`pin_5=GND,GND_8032`；`pin_6=TX to IC1`；`pin_7=PF no-connect`；`pin_8=RX no-connect` |
| 总线 | HLW8032 到 STM32 的串行数据 | `source=IC2 TX pin 6`；`isolation=IC1 EL357N(C)(TA)-G`；`logic_net=RX`；`destination=U4 PA3 pin 10`；`direction=IC2 to U4`；`reverse_path=null` |
| 保护电路 | IC1 光耦隔离 | `input_supply=VCC_8032 via R2 470R/1%`；`input_signal=TX at pin 2`；`output_signal=RX at pin 4`；`output_pullup=R3 1.6K/1% to VCC_3V3`；`output_return=pin 3 via R4 3.3K/1% to GND` |
| 电源 | U2 B0505ST16-W5 | `input_rail=VCC_5V`；`input_ground=GND`；`control_pin=pin 1 CTRL to VCC_5V`；`input_pin=pin 3 VIN`；`output_pin=pin 14 VO`；`output_rail=VCC_8032`；`output_ground=pins 9,15,16 to GND_8032` |
| 电源 | U2 输入/输出去耦 | `input_capacitors=C10,C11; 100nF/50V/10%`；`input_domains=VCC_5V,GND`；`output_capacitor=C12 100nF/50V/10%`；`output_domains=VCC_8032,GND_8032` |
| 电源 | U3 HX6306P332MR | `input=VCC_5V at VIN pin 3`；`output=VOUT pin 2 via FB1 to VCC_3V3`；`ground=GND pin 1`；`ferrite=FB1 330R/GZ1005D331TF`；`input_capacitor=C4 100nF/50V/10%`；`output_capacitors=C6,C7` |
| 电源 | GND 与 GND_8032 | `logic_ground=GND`；`logic_rails=VCC_5V,VCC_3V3`；`meter_ground=GND_8032`；`meter_rail=VCC_8032`；`power_barrier=U2`；`signal_barrier=IC1` |
| 接口 | J2 GROVE 4P | `io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`connector=GROVE 4P` |
| 总线 | U4 I2C | `controller=U4 STM32G030F6`；`scl=U4 pin 1 PB7/PB8`；`sda=U4 pin 2 PB9/PC14-OSC32_IN`；`pullups=R14,R15 4.7K to VCC_3V3`；`connector=J2` |
| 总线地址 | Unit AC Measure I2C 地址 | `bus=I2C`；`schematic_address=null`；`controller=U4 STM32G030F6`；`address_source_needed=firmware or protocol documentation` |
| GPIO 与控制信号 | U4 关键 GPIO | `pin_1=PB7/PB8,SCL`；`pin_2=PB9/PC14-OSC32_IN,SDA`；`pin_10=PA3,RX`；`pin_11=PA4,D1`；`pin_18=PA13(SWDIO),MCU_SWDIO`；`pin_19=PA15/PA14-BOOT0(SWCLK),MCU_SWCLK` |
| 调试与烧录 | D1 红色 LED | `controller_pin=U4 PA4 pin 11`；`led=D1 Red 0603`；`resistor=R13 1K/1%`；`return=GND` |
| 复位 | U4 NRST | `mcu_pin=NRST pin 6`；`pullup=R7 10K/1% to VCC_3V3`；`capacitor=C8 100nF/50V/10% to GND`；`debug_header=J1 pin 4` |
| 调试与烧录 | J1 SWD_5P | `pin_1=VCC_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND` |
| 时钟 | U4 振荡器引脚 | `osc_in_mux=pin 2 PB9/PC14-OSC32_IN used as SDA`；`osc_out=pin 3 PC15-OSC32_OUT no-connect`；`external_clock_component=null` |
| 电源 | U4 电源 | `supply_pin=VDDA/DDA pin 4 to VCC_3V3`；`ground_pin=VSSA/SSA pin 5 to GND`；`decoupling=C9 100nF/50V/10%` |
| 模拟电路 | 交流测量范围 | `schematic_voltage_range=null`；`schematic_accuracy=null`；`fuse_marking=TBT10A250V`；`measurement_ic=HLW8032`；`specification_source_needed=rated product specification and calibration data` |
| 关键网络 | 电源域索引 | `input_domain=VCC_5V,GND`；`logic_domain=VCC_3V3,GND`；`meter_domain=VCC_8032,GND_8032`；`logic_regulator=U3`；`isolated_converter=U2`；`meter_loads=IC2,IC1 input,R1/R6/C1/C3,R8/C5` |

## 待确认事项

- `address.i2c-not-shown`：原理图显示 SCL/SDA 硬件连接和上拉，但未印出 I2C 从机地址，无法仅凭该页确认地址值。（证据：图 f41ba93e6497 / 第 1 页 / 页 1 网格 B1-D2：J2、R14/R15 和 U4 的 SCL/SDA 网络，整页无十六进制地址标注）
- `analog.measurement-range-not-shown`：原理图给出 FUSE1 型号和电压/电流采样元件值，但没有印出允许的交流输入电压范围或计量精度，无法仅凭该页确认完整测量规格。（证据：图 f41ba93e6497 / 第 1 页 / 页 1 上半部：P1/FUSE1、R5、R9~R12 与 HLW8032，页面无 AC 电压范围或精度文字）
- `review.i2c-address`：Unit AC Measure 当前固件使用的 I2C 从机地址是否为 0x42？；原因：原理图只显示 SCL/SDA 与上拉电路，没有地址选择脚或地址文字，需要固件或通信协议资料确认。
- `review.measurement-range`：该硬件版本允许的交流输入范围、最大持续电流和计量精度分别是多少？；原因：原理图仅显示 TBT10A250V、采样阻容和 HLW8032，未给出整机额定范围、温升降额、校准参数或精度。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f41ba93e6497cf0c3f068f596468005443e5ae8bd7a7b0b544472146d961f40d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/619/SCH_UNIT_AC_Measure_V1.01_sch_01.png` |

---

源文档：`zh_CN/unit/AC Measure Unit.md`

源文档 SHA-256：`398c56a766366d1d8862a5b4f3683a3cd9e7d799e8f19965a5f318b7b279bd8f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
