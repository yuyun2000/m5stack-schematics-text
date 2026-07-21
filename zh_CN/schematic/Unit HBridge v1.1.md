# Unit HBridge v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit HBridge v1.1 |
| SKU | U160-V11 |
| 产品 ID | `unit-hbridge-v1-1-13c2bfb2a9d9` |
| 源文档 | `zh_CN/unit/HBridge v1.1 Unit.md` |

## 概述

Unit HBridge v1.1 以 U3 STM32F030F4P6 为 I2C 从控制器，通过 MF/MR 驱动 U4 RZ7899 H 桥，并由 U5 INA199A1DCKR 对电机总电流进行采样。HPWR 经 D1 和 U1 SY8303AIC 生成 VCC_5V，Grove 的 BUS_5V 又经 U2 HX6306P332MR 生成 3V3，另有 Q1/Q2/D5 构成 BUS_5V 到 VCC_5V 的受控备用路径。J1 提供 Grove I2C，P5 引出 OUT_P、OUT_N、GND 和 HPWR，S1 在 HPWR 与 VCC_5V 间选择电机电源；默认地址、整机额定边界及固件控制语义未由本页原理图确认。

## 检索关键词

`Unit HBridge v1.1`、`U160-V11`、`STM32F030F4P6`、`RZ7899`、`INA199A1DCKR`、`SY8303AIC`、`HX6306P332MR`、`TL432`、`AO3401A`、`DTC143ZCA`、`Grove I2C`、`SCL`、`SDA`、`BUS_5V`、`VCC_5V`、`VCC_12V`、`3V3`、`HPWR`、`VM`、`ADC_OUT`、`MF`、`MR`、`OUT_P`、`OUT_N`、`SWDIO`、`SWCLK`、`BOOT0`、`NRST`、`SW1`、`S1`、`F1 3A`、`R4 10mR`、`DSS34`、`SMF30CA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 从控制器，读取地址开关、电流与 VM 检测信号并输出 MF/MR 电机控制信号 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C1-D2：U3 STM32F030F4P6 及全部引脚网络 |
| U4 | RZ7899 | 由 MF/MR 控制、以 VM 供电的双向电机 H 桥驱动器 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D3-D4：U4 RZ7899、INR/INF、OUTR/OUTF 与 VM |
| U5 | INA199A1DCKR | 跨 R4 10mR 分流电阻测量电机供电电流并输出 ADC_OUT | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C3-C4：U5 INA199A1DCKR、R4、ADC_OUT、3V3 与 REF |
| U1 | SY8303AIC | 将 VCC_12V 降压生成 VCC_5V 的开关稳压器 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A2：U1 SY8303AIC、L1 6.8uH、反馈网络与 VCC_5V |
| U2 | HX6306P332MR | 由 BUS_5V 生成 3V3 的线性稳压器 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A3：U2 HX6306P332MR，VIN=BUS_5V、VOUT=3V3 |
| U6,R5 | TL432 / 330R | 为 INA199 REF 引脚形成参考偏置支路 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C4：U6 TL432、R5 330R、3V3、GND 与 U5 REF |
| J1 | GROVE 4P | 外部 I2C 与 BUS_5V/GND 接口 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A3：J1 GROVE 4P，SCL/SDA/5V/GND 网络标注 |
| P5 | HT3.96 4P | 电机输出与外部电源端子，引出 OUT_P、OUT_N、GND、HPWR | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D4：P5 HT3.96 4P 的 1~4 脚 |
| J2 | SWD | STM32 的 3V3、SWCLK、SWDIO、NRST、GND 调试接口 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D2：J2 SWD pin1-pin5 |
| SW1 | 4-position DIP switch | 将 PA0~PA3 各自选择接地，用于四位 I2C 地址配置 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C2：SW1 四联开关、PA0~PA3 与 GND |
| S1 | TA-3539S-A1 | 在 HPWR 与 VCC_5V 之间选择电机供电来源 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C3：S1 TA-3539S-A1，HPWR/VCC_5V 输入及并联公共输出 |
| Q1,Q2,D5 | AO3401A / DTC143ZCA / DSS34 | 由 HPWR 检测网络控制的 BUS_5V 至 VCC_5V 备用供电路径 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 B3：BUS_5V-Q1-D5-VCC_5V 与 Q2/R17/R18/R19 |
| D1 | DSS34 | HPWR 至 VCC_12V 输入串联肖特基二极管 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A1-A2：HPWR-D1(DSS34)-VCC_12V |
| D3 | SMF30CA | HPWR 输入侧对地瞬态抑制器件 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A1：D3 SMF30CA 跨接 HPWR 与 GND |
| D2 | TVS 5V | VCC_5V 电源轨对地瞬态抑制器件 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A2：D2 TVS 5V 跨接 VCC_5V 与 GND |
| F1,R4 | 3A / 10mR 1206 | 电机电源串联保险与电流采样分流器 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C3：S1 输出-F1(3A)-R4(10mR/1206)-VM |
| R14,C15 | 10R / 1nF | 串联跨接 OUT_N 与 OUT_P 的电机输出吸收网络 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D3：OUT_N-R14(10R)-C15(1nF)-OUT_P |
| C10,C11,C12 | 220uF/25V | VM 电机电源轨的并联储能/滤波电容 | 图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D3：VM 至 GND 的 C10/C11/C12，均标注 220uF/25V |

## 系统结构

### Unit HBridge v1.1 系统架构

U3 STM32F030F4P6 通过 SCL/SDA 接 Grove I2C，以 MF/MR 控制 U4 RZ7899；电机电源经 S1、F1、R4 形成 VM，U5 INA199A1DCKR 将分流电压转换为 ADC_OUT。HPWR 经 U1 生成 VCC_5V，BUS_5V 经 U2 生成 3V3。

- 参数与网络：`controller=U3 STM32F030F4P6`；`motor_driver=U4 RZ7899`；`current_monitor=U5 INA199A1DCKR`；`host_bus=SCL/SDA`；`motor_control=MF/MR`；`rails=HPWR,VCC_12V,VCC_5V,BUS_5V,3V3,VM`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 核心器件

### RZ7899 电机输出

U4 以 VM 连接 VCC pin4、GND pin3；OUTR pins8/7 并联形成 OUT_N，OUTF pins6/5 并联形成 OUT_P。

- 参数与网络：`supply=U4 pin4 VCC=VM`；`ground=U4 pin3 GND`；`out_n=U4 OUTR pins8,7`；`out_p=U4 OUTF pins6,5`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D3：U4 RZ7899 pins3-8 与 VM/OUT_N/OUT_P

## 电源

### HPWR 至 VCC_5V 降压路径

HPWR 经 D1 DSS34 串联形成 VCC_12V，VCC_12V 连接 U1 SY8303AIC 的 VIN pin5 与 EN pin8；U1 LX pin6 经 L1 6.8uH 输出 VCC_5V，FB pin1 接含 R1 200K 的反馈网络。

- 参数与网络：`input=HPWR`；`series_diode=D1 DSS34`；`intermediate_rail=VCC_12V`；`converter=U1 SY8303AIC`；`vin=pin5`；`enable=pin8 tied to VCC_12V`；`switch_node=pin6 LX`；`inductor=L1 6.8uH`；`output=VCC_5V`；`feedback=pin1 FB,R1 200K`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A1-A2：D1、U1、L1、R1 与 HPWR/VCC_12V/VCC_5V

### BUS_5V 至 3V3 稳压

J1 的 5V 网络标为 BUS_5V；BUS_5V 接 U2 HX6306P332MR VIN pin3，U2 VOUT pin2 输出 3V3，GND pin1 接地，C5 100nF 位于输入侧。

- 参数与网络：`input=BUS_5V`；`regulator=U2 HX6306P332MR`；`vin=pin3`；`vout=pin2 3V3`；`ground=pin1 GND`；`input_cap=C5 100nF`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A3：J1 BUS_5V、C5、U2 与 3V3

### BUS_5V 至 VCC_5V 备用路径

BUS_5V 经过 Q1 AO3401A 和 D5 DSS34 接至 VCC_5V；Q1 栅极节点由 R17 100K 下拉并连接 Q2 DTC143ZCA，Q2 输入由 HPWR 经 R18 20K/R19 100K 分压节点驱动。

- 参数与网络：`path=BUS_5V -> Q1 AO3401A -> D5 DSS34 -> VCC_5V`；`gate_pulldown=R17 100K`；`control_transistor=Q2 DTC143ZCA`；`hpwr_divider=R18 20K,R19 100K`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 B3：HPWR/R18/R19/Q2/R17 与 BUS_5V/Q1/D5/VCC_5V

### STM32 3V3 供电

U3 VDD pin16 与 VDDA pin5 连接 3V3，VSS pin15 接 GND，C4 100nF 跨接 3V3 与 GND 作为去耦。

- 参数与网络：`vdd=pin16 3V3`；`vdda=pin5 3V3`；`vss=pin15 GND`；`decoupling=C4 100nF`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D2：U3 VDD/VDDA/VSS 与 C4

### S1 电机电源选择

S1 TA-3539S-A1 的输入侧连接 HPWR 与 VCC_5V，两个公共触点 pin2/pin5 并联后依次经过 F1 3A 和 R4 10mR/1206，形成 VM 电机电源轨。

- 参数与网络：`selector=S1 TA-3539S-A1`；`sources=HPWR,VCC_5V`；`common_contacts=pin2,pin5 tied`；`series_path=S1 -> F1 3A -> R4 10mR/1206 -> VM`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C3：VM select 框内 S1、F1、R4 与 HPWR/VCC_5V/VM

## 接口

### J1 Grove 接口

J1 GROVE 4P 从上到下标注 SCL、SDA、5V、GND；其中 5V 引脚连接 BUS_5V，GND 引脚接地，SCL/SDA 为 3V3 域信号。

- 参数与网络：`connector=J1 GROVE 4P`；`order_top_to_bottom=SCL,SDA,5V,GND`；`supply_net=BUS_5V`；`logic_rail=3V3`；`direction=SCL/SDA bidirectional open-drain`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A3：J1 四条网络及 SCL/SDA 上拉支路

### P5 电机与电源端子

P5 HT3.96 4P 的 pin1=OUT_P、pin2=OUT_N、pin3=GND、pin4=HPWR；OUT_P/OUT_N 为 U4 输出，HPWR 为外部输入电源网络。

- 参数与网络：`pin1=OUT_P, bidirectional motor output`；`pin2=OUT_N, bidirectional motor output`；`pin3=GND`；`pin4=HPWR, power input`；`connector=HT3.96 4P`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 D4：P5 pin1-pin4 与 OUT_P/OUT_N/GND/HPWR

## 总线

### STM32 与 Grove I2C 总线

U3 PA9 pin17 连接 SCL，PA10 pin18 连接 SDA；SCL 经 R15 10K、SDA 经 R16 10K 上拉至 3V3，并连接 J1。

- 参数与网络：`controller=U3 STM32F030F4P6`；`scl=PA9 pin17 -> SCL`；`sda=PA10 pin18 -> SDA`；`scl_pullup=R15 10K to 3V3`；`sda_pullup=R16 10K to 3V3`；`external_port=J1`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A3 与 C2：R15/R16、J1 SCL/SDA、U3 PA9/PA10

## GPIO 与控制信号

### MF/MR 电机控制映射

U3 PA6 pin12 输出 MF，PA7 pin13 输出 MR；MF 连接 U4 INF pin2，MR 连接 U4 INR pin1。

- 参数与网络：`forward_net=U3 PA6 pin12 MF -> U4 INF pin2`；`reverse_net=U3 PA7 pin13 MR -> U4 INR pin1`；`direction=U3 output to U4 input`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C2 与 D3：U3 PA6/PA7 的 MF/MR 同名网络到 U4 INR/INF

## 时钟

### STM32 时钟连接

U3 PF0-OSC_IN pin2 与 PF1-OSC_OUT pin3 在本页未连接外部晶振、谐振器或时钟网络；原理图未标出 MCU 工作频率。

- 参数与网络：`osc_in=PF0 pin2 no external connection`；`osc_out=PF1 pin3 no external connection`；`external_crystal=false`；`frequency=null`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C1：U3 PF0-OSC_IN/PF1-OSC_OUT 引脚无外接连线

## 复位

### STM32 BOOT0 与 NRST

U3 BOOT0 pin1 经 R7 10K 下拉至 GND；NRST pin4 经 R6 10K 上拉至 3V3，并由 C9 100nF 对地滤波，同时引至 J2 pin4。

- 参数与网络：`boot0=pin1 via R7 10K to GND`；`reset=pin4 NRST`；`reset_pullup=R6 10K to 3V3`；`reset_cap=C9 100nF to GND`；`debug_reset=J2 pin4`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C1-D2：U3 BOOT0/NRST、R6/R7/C9 与 J2 NRST

## 保护电路

### 输入与 5V 电源保护

D3 SMF30CA 跨接 HPWR 与 GND，D1 DSS34 串联在 HPWR 至 VCC_12V 路径；D2 标注 TVS 5V，跨接 VCC_5V 与 GND。

- 参数与网络：`hpwr_tvs=D3 SMF30CA to GND`；`series_diode=D1 DSS34`；`vcc5v_tvs=D2 TVS 5V to GND`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 A1-A2：D1/D3 输入支路与 D2 VCC_5V 支路

### 电机供电与输出抑制网络

F1 标注 3A 并串联在 S1 输出与 R4 之间；C10/C11/C12 各 220uF/25V 并联在 VM 与 GND 之间；R14 10R 与 C15 1nF 串联后跨接 OUT_N 和 OUT_P。

- 参数与网络：`fuse=F1 3A`；`bulk_caps=C10,C11,C12 220uF/25V`；`snubber=OUT_N -> R14 10R -> C15 1nF -> OUT_P`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C3-D3：F1/R4、VM 的 C10-C12、OUT_N/OUT_P 的 R14/C15

## 调试与烧录

### J2 SWD 调试接口

J2 pin1=3V3、pin2=SWCLK、pin3=SWDIO、pin4=NRST、pin5=GND；SWDIO 连接 U3 PA13 pin19，SWCLK 连接 U3 PA14 pin20。

- 参数与网络：`pin1=3V3`；`pin2=SWCLK -> U3 PA14 pin20`；`pin3=SWDIO -> U3 PA13 pin19`；`pin4=NRST`；`pin5=GND`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C2-D2：U3 PA13/PA14 与 J2 SWD pin1-pin5

## 模拟电路

### INA199 电流采样链路

F1 后、R4 上游节点接 U5 IN+ pin4，R4 下游 VM 接 U5 IN- pin5；U5 OUT pin6 输出 ADC_OUT 到 U3 PB1 pin14，U5 V+ pin3 接 3V3、GND pin2 接地、REF pin1 接 U6/R5 偏置节点。

- 参数与网络：`shunt=R4 10mR/1206`；`in_plus=U5 pin4, R4 upstream`；`in_minus=U5 pin5, VM/R4 downstream`；`output=U5 pin6 ADC_OUT -> U3 PB1 pin14`；`supply=U5 pin3 3V3`；`ground=U5 pin2 GND`；`reference=U5 pin1 -> U6 TL432/R5 330R`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C1-C4：R4/U5/U6/R5、ADC_OUT 与 U3 PB1

### VM 电压分压检测

VM 经 R12 200K 接至 U3 PA4 pin10，PA4 节点再经 R13 20K 接 GND，构成 VM 的 200K/20K 分压检测网络。

- 参数与网络：`input=VM`；`upper_resistor=R12 200K`；`lower_resistor=R13 20K`；`adc_input=U3 PA4 pin10`；`nominal_divider_ratio=1/11`
- 证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C2：U3 PA4 至 R12/R13 与 VM/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit HBridge v1.1 系统架构 | `controller=U3 STM32F030F4P6`；`motor_driver=U4 RZ7899`；`current_monitor=U5 INA199A1DCKR`；`host_bus=SCL/SDA`；`motor_control=MF/MR`；`rails=HPWR,VCC_12V,VCC_5V,BUS_5V,3V3,VM` |
| 电源 | HPWR 至 VCC_5V 降压路径 | `input=HPWR`；`series_diode=D1 DSS34`；`intermediate_rail=VCC_12V`；`converter=U1 SY8303AIC`；`vin=pin5`；`enable=pin8 tied to VCC_12V`；`switch_node=pin6 LX`；`inductor=L1 6.8uH`；`output=VCC_5V`；`feedback=pin1 FB,R1 200K` |
| 电源 | BUS_5V 至 3V3 稳压 | `input=BUS_5V`；`regulator=U2 HX6306P332MR`；`vin=pin3`；`vout=pin2 3V3`；`ground=pin1 GND`；`input_cap=C5 100nF` |
| 电源 | BUS_5V 至 VCC_5V 备用路径 | `path=BUS_5V -> Q1 AO3401A -> D5 DSS34 -> VCC_5V`；`gate_pulldown=R17 100K`；`control_transistor=Q2 DTC143ZCA`；`hpwr_divider=R18 20K,R19 100K` |
| 接口 | J1 Grove 接口 | `connector=J1 GROVE 4P`；`order_top_to_bottom=SCL,SDA,5V,GND`；`supply_net=BUS_5V`；`logic_rail=3V3`；`direction=SCL/SDA bidirectional open-drain` |
| 总线 | STM32 与 Grove I2C 总线 | `controller=U3 STM32F030F4P6`；`scl=PA9 pin17 -> SCL`；`sda=PA10 pin18 -> SDA`；`scl_pullup=R15 10K to 3V3`；`sda_pullup=R16 10K to 3V3`；`external_port=J1` |
| 总线地址 | SW1 I2C 地址配置 | `bit_inputs=PA0 pin6,PA1 pin7,PA2 pin8,PA3 pin9`；`pullups=R8,R9,R10,R11 10K to 3V3`；`switch=SW1 closes inputs to GND`；`documented_default=0x20`；`address_mapping=null` |
| GPIO 与控制信号 | MF/MR 电机控制映射 | `forward_net=U3 PA6 pin12 MF -> U4 INF pin2`；`reverse_net=U3 PA7 pin13 MR -> U4 INR pin1`；`direction=U3 output to U4 input` |
| 复位 | STM32 BOOT0 与 NRST | `boot0=pin1 via R7 10K to GND`；`reset=pin4 NRST`；`reset_pullup=R6 10K to 3V3`；`reset_cap=C9 100nF to GND`；`debug_reset=J2 pin4` |
| 调试与烧录 | J2 SWD 调试接口 | `pin1=3V3`；`pin2=SWCLK -> U3 PA14 pin20`；`pin3=SWDIO -> U3 PA13 pin19`；`pin4=NRST`；`pin5=GND` |
| 时钟 | STM32 时钟连接 | `osc_in=PF0 pin2 no external connection`；`osc_out=PF1 pin3 no external connection`；`external_crystal=false`；`frequency=null` |
| 电源 | STM32 3V3 供电 | `vdd=pin16 3V3`；`vdda=pin5 3V3`；`vss=pin15 GND`；`decoupling=C4 100nF` |
| 电源 | S1 电机电源选择 | `selector=S1 TA-3539S-A1`；`sources=HPWR,VCC_5V`；`common_contacts=pin2,pin5 tied`；`series_path=S1 -> F1 3A -> R4 10mR/1206 -> VM` |
| 模拟电路 | INA199 电流采样链路 | `shunt=R4 10mR/1206`；`in_plus=U5 pin4, R4 upstream`；`in_minus=U5 pin5, VM/R4 downstream`；`output=U5 pin6 ADC_OUT -> U3 PB1 pin14`；`supply=U5 pin3 3V3`；`ground=U5 pin2 GND`；`reference=U5 pin1 -> U6 TL432/R5 330R` |
| 模拟电路 | VM 电压分压检测 | `input=VM`；`upper_resistor=R12 200K`；`lower_resistor=R13 20K`；`adc_input=U3 PA4 pin10`；`nominal_divider_ratio=1/11` |
| 核心器件 | RZ7899 电机输出 | `supply=U4 pin4 VCC=VM`；`ground=U4 pin3 GND`；`out_n=U4 OUTR pins8,7`；`out_p=U4 OUTF pins6,5` |
| 接口 | P5 电机与电源端子 | `pin1=OUT_P, bidirectional motor output`；`pin2=OUT_N, bidirectional motor output`；`pin3=GND`；`pin4=HPWR, power input`；`connector=HT3.96 4P` |
| 保护电路 | 输入与 5V 电源保护 | `hpwr_tvs=D3 SMF30CA to GND`；`series_diode=D1 DSS34`；`vcc5v_tvs=D2 TVS 5V to GND` |
| 保护电路 | 电机供电与输出抑制网络 | `fuse=F1 3A`；`bulk_caps=C10,C11,C12 220uF/25V`；`snubber=OUT_N -> R14 10R -> C15 1nF -> OUT_P` |
| 电源 | 正文电压与负载额定值 | `documented_external_voltage=MAX 12V`；`documented_external_range=6-12V`；`documented_load_current=3A`；`schematic_fuse=F1 3A`；`continuous_rating=null`；`peak_rating=null`；`thermal_derating=null` |
| 其他事实 | 正文固件控制与保护语义 | `documented_pwm=up to 16-bit`；`documented_functions=speed,forward,reverse,brake`；`documented_protection=over-current,over-voltage,over-temperature`；`register_protocol=null`；`pwm_frequency=null`；`brake_truth_table=null`；`fault_thresholds=null` |
| 保护电路 | 包装所含 470uF 外接电容 | `documented_capacitance=470uF`；`documented_type=aluminum electrolytic`；`schematic_reference=null`；`voltage_rating=null`；`connection_points=null` |

## 待确认事项

- `address.dip-switch`：U3 PA0 pin6、PA1 pin7、PA2 pin8、PA3 pin9 分别接 SW1 的 1、2、3、4 位并各经 R8/R9/R10/R11 10K 上拉至 3V3；开关闭合时相应输入接 GND。原理图未给出四位数值权重、有效极性对应的地址算法或默认 0x20。（证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页网格 C2：for I2C address config、R8-R11、SW1 与 PA0-PA3；图中无地址数值）
- `power.documented-operating-limits`：正文称外部直流电压最大 12V、可在 6-12V 与 5V 电机电源间切换、最大负载电流 3A；原理图确认 HPWR/VCC_5V 选择和 F1=3A，但没有给出整机连续电流、峰值电流、热降额、输入工作范围或绝对最大额定值。（证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页 S1/F1/HPWR/VCC_5V 电源路径；图中无额定值或温升表）
- `other.documented-firmware-functions`：正文描述最高 16 位 PWM、转速、正转、反转、制动以及过流、过压、过热保护；原理图只确认 I2C、MF/MR、ADC_OUT、VM 检测及保护器件连接，没有寄存器协议、PWM 位宽/频率、制动真值表、故障阈值或温度检测网络说明。（证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页 U3/U4/U5、MF/MR/ADC_OUT/VM 与保护器件；图中无固件协议或阈值）
- `protection.documented-external-capacitor`：正文要求将包装中的 470uF 铝电解电容接到电源输入正负极并注意极性；本页板级原理图没有该外接电容的位号、端子接法、额定电压或所对应的 HPWR/GND 安装位置。（证据：图 1f7a6d1f3b71 / 第 1 页 / 第 1 页 P5/HPWR/GND 与板载 C10-C12；未出现 470uF 外接电容位号）
- `review.i2c-address-map`：请用内部固件、通信协议或实机扫描确认默认 I2C 地址 0x20，以及 SW1 四位开关对应的地址权重和有效电平。；原因：原理图只显示 PA0-PA3 的上拉与接地开关，没有地址算法或地址数值。
- `review.operating-limits`：请依据 RZ7899、SY8303AIC、连接器、PCB 铜厚与热测试确认 6-12V 输入范围、12V 上限及 3A 连续/峰值负载边界。；原因：F1=3A 与器件标称不能单独证明整机连续负载能力和热降额。
- `review.firmware-protection`：请结合当前内置固件与器件资料确认 PWM 位宽/频率、方向/制动真值表，以及过流、过压、过热检测方式和阈值。；原因：板级原理图没有固件寄存器协议、PWM 参数、故障阈值或明确温度传感器。
- `review.external-capacitor`：请确认随附 470uF 电解电容的额定电压、极性标识和应接入的 P5/电源端子位置。；原因：该电容未作为板级器件出现在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1f7a6d1f3b7110efa75dc0ecb9a0110af988662da474c7c96b5cbe3cb0576418` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/615/SCH_UNIT_HBridge_V1.1_sch_01.png` |

---

源文档：`zh_CN/unit/HBridge v1.1 Unit.md`

源文档 SHA-256：`0b8dd92966354b151869c3069841d0c072f2bd2d3640634f4b65b5cb575eeb7e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
