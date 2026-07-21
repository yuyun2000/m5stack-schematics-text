# Unit BLDC Driver 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit BLDC Driver |
| SKU | U181 |
| 产品 ID | `unit-bldc-driver-fe1397986f4b` |
| 源文档 | `zh_CN/unit/Unit-BLDC Driver.md` |

## 概述

Unit BLDC Driver 以 U1 STM32G030F6P6 为主控，通过 J1 Grove 的 I2C_SCL/I2C_SDA 接受外部命令，并以 DRV_PWM、DRV_FR、DRV_FS、DRV_FG、DRV_RD 五条控制/状态线连接 U3 DRV11873PWPR。U3 直接由 VIN 供电，驱动 PHU/PHV/PHW 三相并通过 PCOM 接到 J2 HT3.96_4P，配有电荷泵电容、相线二极管和相位公共点电阻网络。VIN 经 R9/R10 与 BZT52C3V3S 钳位网络形成 MCU_VDD，为 MCU、I2C 上拉和 SYS_LED 供电；J3 提供 SWD 下载与复位。原理图未标 I2C 地址、最大带载电流、待机/工作电流或 DRV11873 内部堵转保护参数。

## 检索关键词

`Unit BLDC Driver`、`U181`、`STM32G030F6P6`、`DRV11873PWPR`、`BLDC`、`I2C`、`0x65`、`I2C_SCL`、`I2C_SDA`、`DRV_PWM`、`DRV_FR`、`DRV_FS`、`DRV_FG`、`DRV_RD`、`PHU`、`PHV`、`PHW`、`PCOM`、`PWM_IN`、`FR`、`FG`、`FS`、`RD`、`VIN`、`MCU_VDD`、`BZT52C3V3S`、`SS16-A`、`HT3.96_4P`、`HY2.0_4P`、`SWCLK`、`SWDIO`、`SYS_RST`、`SYS_LED`、`R9 150R`、`R10 10R`、`R5 R6 R7 1K`、`C9 100nF`、`C11 100nF`、`three phase motor`、`sensorless motor driver`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G030F6P6 | 主控 MCU，连接 I2C、DRV11873 控制/状态、SYS_LED、SWD 和复位 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B2，U1 STM32G030F6P6，pins1-20 与 SYS_LED/SWCLK/SWDIO/I2C/DRV_* 网络 |
| U3 | DRV11873PWPR | 三相电机驱动器，接收 PWM/方向控制并输出 PHU/PHV/PHW/PCOM | 图 a778bea573af / 第 1 页 / 第 1 页网格 B3，U3 DRV11873PWPR，PWM_IN/FR/FG/FS/RD、U/V/W/COM、VCP/VCC/GND/CS/CPP/CPN |
| J1 | CON_HY2.0_4P_DIP_HOR_RED | Grove I2C 与 VIN/GND 接口 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B1，J1 pins4/3/2/1 对应 I2C_SCL/I2C_SDA/VIN/GND |
| J2 | HT3.96_4P | 四针三相电机接口，输出 PHU、PHV、PHW 和 PCOM | 图 a778bea573af / 第 1 页 / 第 1 页网格 B4，J2 HT3.96_4P，pin4 PHU、pin3 PHV、pin2 PHW、pin1 PCOM |
| J3 | CON5 | MCU_VDD、SWCLK、SWDIO、SYS_RST、GND 下载调试接口 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B1，J3 CON5 pins1-5 标注 MCU_VDD/SWCLK/SWDIO/SYS_RST/GND |
| R9,R10,D2,C8 | 150R/1% / 10R/1% / BZT52C3V3S / 10uF/16V | VIN 至 MCU_VDD 的串联限流、3.3V 齐纳钳位与滤波网络 | 图 a778bea573af / 第 1 页 / 第 1 页网格 A2，VIN-R9-R10-MCU_VDD，D2 BZT52C3V3S 与 C8 对 GND |
| R2,R3 | 3.6K/1% | I2C_SCL 与 I2C_SDA 到 MCU_VDD 的上拉电阻 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B1，R2/R3 3.6K/1% 从 I2C_SCL/I2C_SDA 接 MCU_VDD |
| D1,R1 | 绿色 LED / 3.6K/1% | 由 SYS_LED 经 R1 驱动并对 GND 回路的绿色状态指示灯 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B1-C1，SYS_LED-R1 3.6K/1%-D1 绿色-GND |
| D3,D4,D5 | SS16-A | PHU、PHV、PHW 三相输出到 GND 的钳位二极管 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B3-B4，D3/D4/D5 SS16-A 分别从 PHU/PHV/PHW 接 GND |
| R5,R6,R7 | 1K/1% | 三相 PHU/PHV/PHW 到 PCOM 的公共点电阻网络 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B3，R5/R6/R7 1K/1% 位于 PHU/PHV/PHW 与 PCOM 星形网络 |
| C9,C11 | 100nF/50V | DRV11873 CPP/CPN 与 VCP/VCC 的电荷泵电容 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B3，C9 100nF/50V 跨 CPP/CPN，C11 100nF/50V 位于 VCP/VCC 支路 |
| R4,R8 | 2K/1% / 3.6K/1% | DRV11873 CS 设置电阻与 DRV_PWM 下拉电阻 | 图 a778bea573af / 第 1 页 / 第 1 页网格 B2-B3，R4 2K/1% 从 U3 CS pin14 接 GND，R8 3.6K/1% 从 DRV_PWM 接 GND |

## 系统结构

### Unit BLDC Driver 系统架构

U1 STM32G030F6P6 通过 I2C 与外部主机通信，并通过 DRV_PWM/DRV_FR 控制 U3 DRV11873PWPR、通过 DRV_FS/DRV_FG/DRV_RD 读取状态；U3 产生 PHU/PHV/PHW 三相输出和 PCOM。VIN 同时给 U3 供电，并经齐纳钳位网络生成 MCU_VDD。

- 参数与网络：`controller=U1 STM32G030F6P6`；`driver=U3 DRV11873PWPR`；`host_bus=I2C via J1`；`control=DRV_PWM,DRV_FR`；`status=DRV_FS,DRV_FG,DRV_RD`；`motor_output=J2 PHU,PHV,PHW,PCOM`；`power=VIN and MCU_VDD`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页完整 A1-C4，J1/J3/U1/MCU_VDD/U3/J2 功能区

## 核心器件

### STM32G030F6P6 关键引脚映射

U1 pin20 复用组 PB3/PB4/PB5/PB6 接 SYS_LED，pin19 PA15/PA14/BOOT0 接 SWCLK，pin18 PA13 接 SWDIO，pin17 PA12/PA10 接 I2C_SDA，pin16 PA11/PA9 接 I2C_SCL，pin15 PB0/PB1/PB2/PA8 接 DRV_RD，pin14 PA7 接 DRV_FG，pin13 PA6 接 DRV_FS，pin12 PA5 接 DRV_FR，pin11 PA4 接 DRV_PWM。

- 参数与网络：`sys_led=pin20 PB3/PB4/PB5/PB6`；`swclk=pin19 PA15/PA14/BOOT0`；`swdio=pin18 PA13`；`i2c_sda=pin17 PA12/PA10`；`i2c_scl=pin16 PA11/PA9`；`drv_rd=pin15 PB0/PB1/PB2/PA8`；`drv_fg=pin14 PA7`；`drv_fs=pin13 PA6`；`drv_fr=pin12 PA5`；`drv_pwm=pin11 PA4`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B2，U1 右侧 pins11-20 的复用引脚与网络标签

## 电源

### VIN 至 MCU_VDD

VIN 经 R9 150R/1% 与 R10 10R/1% 串联形成 MCU_VDD；D2 BZT52C3V3S 从 R9/R10 中间节点接 GND，C8 10uF/16V 从 MCU_VDD 接 GND。

- 参数与网络：`input=VIN`；`series_resistors=R9 150R/1%,R10 10R/1%`；`zener=D2 BZT52C3V3S to GND`；`output=MCU_VDD`；`capacitor=C8 10uF/16V`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 A2，VIN/R9/R10/D2/C8/MCU_VDD

### DRV11873 VIN 供电与去耦

VIN 直接连接 U3 VCC pin11；C12 22uF/16V 位于 U3 VCC/VIN 对地支路，C1/C2/C3 各 22uF/16V 组成另一组 VIN 对地储能，U3 V5 pin12 使用 C7 2.2uF/10V 对地。

- 参数与网络：`driver=U3 DRV11873PWPR`；`vcc=pin11 -> VIN`；`local_bulk=C12 22uF/16V`；`input_bulk=C1/C2/C3 22uF/16V`；`v5=pin12 with C7 2.2uF/10V`；`ground=GND`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3-C3，U3 VCC/V5、C12/C7 与下方 VIN/C1/C2/C3

### DRV11873 电荷泵

C9 100nF/50V 跨接 U3 CPP pin5 与 CPN pin6；C11 100nF/50V 位于 U3 VCP pin4 与 VCC/VIN 节点之间。

- 参数与网络：`flying_cap=C9 100nF/50V between CPP pin5 and CPN pin6`；`pump_cap=C11 100nF/50V between VCP pin4 and VCC/VIN`；`driver=U3 DRV11873PWPR`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3，U3 CPP/CPN/VCP/VCC 与 C9/C11

## 接口

### J1 Grove I2C 与电源接口

J1 pin4=I2C_SCL、pin3=I2C_SDA、pin2=VIN、pin1=GND；R2/R3 各 3.6K/1% 将 SCL/SDA 上拉到 MCU_VDD。

- 参数与网络：`connector=J1 CON_HY2.0_4P_DIP_HOR_RED`；`pin4=I2C_SCL`；`pin3=I2C_SDA`；`pin2=VIN`；`pin1=GND`；`pullups=R2/R3 3.6K/1% to MCU_VDD`；`direction=bidirectional I2C`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1，J1 pins1-4、R2/R3 与 MCU_VDD

### J2 三相电机接口

J2 HT3.96_4P pin4=PHU、pin3=PHV、pin2=PHW、pin1=PCOM；PHU/PHV/PHW 分别来自 U3 U pin10、V pin9、W pin7，PCOM 来自 U3 COM pin13。

- 参数与网络：`connector=J2 HT3.96_4P`；`pin4=PHU <- U3 pin10 U`；`pin3=PHV <- U3 pin9 V`；`pin2=PHW <- U3 pin7 W`；`pin1=PCOM <- U3 pin13 COM`；`phases=U,V,W`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3-B4，U3 U/V/W/COM 与 J2 pins4/3/2/1

## 总线

### 外部主机到 U1 I2C

J1 I2C_SDA 同名网络连接 U1 pin17 PA12/PA10，J1 I2C_SCL 同名网络连接 U1 pin16 PA11/PA9；U1 是板上 I2C 从设备逻辑的控制器。

- 参数与网络：`external_connector=J1`；`sda=I2C_SDA -> U1 pin17 PA12/PA10`；`scl=I2C_SCL -> U1 pin16 PA11/PA9`；`pullups=3.6K/1% to MCU_VDD`；`board_controller=U1 STM32G030F6P6`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1-B2，J1/R2/R3 与 U1 I2C_SDA/I2C_SCL 同名网络

## GPIO 与控制信号

### U1 与 DRV11873 控制/状态映射

U1 PA4 输出 DRV_PWM 到 U3 PWM_IN pin16，PA5 输出 DRV_FR 到 FR pin15；U3 FS pin1、FG pin2、RD pin3 分别经 DRV_FS、DRV_FG、DRV_RD 返回 U1 PA6、PA7 和 pin15 复用 GPIO。

- 参数与网络：`pwm=U1 PA4 pin11 -> DRV_PWM -> U3 pin16 PWM_IN`；`direction=U1 PA5 pin12 -> DRV_FR -> U3 pin15 FR`；`fs=U3 pin1 FS -> U1 PA6 pin13`；`fg=U3 pin2 FG -> U1 PA7 pin14`；`rd=U3 pin3 RD -> U1 pin15 PB0/PB1/PB2/PA8`；`pwm_pulldown=R8 3.6K/1%`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B2-B3，U1 pins11-15、DRV_* 同名网络、R8 与 U3 pins1-3/15/16

### SYS_LED 绿色指示灯

U1 pin20 的 SYS_LED 网络经 R1 3.6K/1% 和 D1 绿色 LED 接到 GND，构成高电平驱动的状态指示支路。

- 参数与网络：`mcu_pin=U1 pin20 PB3/PB4/PB5/PB6`；`net=SYS_LED`；`resistor=R1 3.6K/1%`；`led=D1 绿色`；`return=GND`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1-B2，U1 SYS_LED 与 R1/D1/GND

## 时钟

### U1 外部时钟

U1 左侧 PC14_OSC32I 与 PC15_OSC32O 复用引脚在本页没有连接晶振、谐振器或负载电容，原理图未显示独立时钟器件。

- 参数与网络：`osc_in=PC14_OSC32I unconnected`；`osc_out=PC15_OSC32O unconnected`；`external_crystal=null`；`load_capacitors=null`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B2，U1 左上 OSC32I/OSC32O 复用引脚无外接线路

## 复位

### U1 SYS_RST 复位网络

U1 NRST pin6 连接 SYS_RST，并引到 J3 pin4；C6 2.2uF/10V 从 SYS_RST 接到 GND，原理图没有显示外部复位上拉电阻或复位按键。

- 参数与网络：`mcu_pin=U1 pin6 NRST`；`net=SYS_RST`；`capacitor=C6 2.2uF/10V to GND`；`debug_pin=J3 pin4`；`external_pullup=null`；`reset_button=null`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1-B2，J3 SYS_RST、U1 NRST 与 C6/GND

## 保护电路

### 三相输出钳位

D3、D4、D5 均标 SS16-A，分别从 PHU、PHV、PHW 接到公共 GND，对三相输出形成对地钳位支路。

- 参数与网络：`phase_u=D3 SS16-A to GND`；`phase_v=D4 SS16-A to GND`；`phase_w=D5 SS16-A to GND`；`protected_connector=J2`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3-B4，PHU/PHV/PHW 上的 D3/D4/D5 SS16-A 与 GND

## 调试与烧录

### J3 SWD 下载接口

J3 CON5 pin1=MCU_VDD、pin2=SWCLK、pin3=SWDIO、pin4=SYS_RST、pin5=GND；SWCLK/SWDIO 连接 U1 pins19/18，SYS_RST 连接 U1 NRST pin6。

- 参数与网络：`pin1=MCU_VDD`；`pin2=SWCLK -> U1 pin19`；`pin3=SWDIO -> U1 pin18`；`pin4=SYS_RST -> U1 pin6 NRST`；`pin5=GND`；`interface=SWD`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1-B2，J3 CON5 与 U1 SWCLK/SWDIO/NRST 同名网络

## 模拟电路

### PHU/PHV/PHW 到 PCOM 网络

R5、R6、R7 均为 1K/1%，分别从三相 PHU、PHV、PHW 汇入 PCOM；PCOM 同时连接 U3 COM pin13 和 J2 pin1。

- 参数与网络：`phase_u=PHU via R5 1K/1%`；`phase_v=PHV via R6 1K/1%`；`phase_w=PHW via R7 1K/1%`；`common=PCOM -> U3 pin13 COM -> J2 pin1`
- 证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3-B4，R5/R6/R7、PHU/PHV/PHW、PCOM、U3 COM 与 J2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit BLDC Driver 系统架构 | `controller=U1 STM32G030F6P6`；`driver=U3 DRV11873PWPR`；`host_bus=I2C via J1`；`control=DRV_PWM,DRV_FR`；`status=DRV_FS,DRV_FG,DRV_RD`；`motor_output=J2 PHU,PHV,PHW,PCOM`；`power=VIN and MCU_VDD` |
| 核心器件 | STM32G030F6P6 关键引脚映射 | `sys_led=pin20 PB3/PB4/PB5/PB6`；`swclk=pin19 PA15/PA14/BOOT0`；`swdio=pin18 PA13`；`i2c_sda=pin17 PA12/PA10`；`i2c_scl=pin16 PA11/PA9`；`drv_rd=pin15 PB0/PB1/PB2/PA8`；`drv_fg=pin14 PA7`；`drv_fs=pin13 PA6`；`drv_fr=pin12 PA5`；`drv_pwm=pin11 PA4` |
| 接口 | J1 Grove I2C 与电源接口 | `connector=J1 CON_HY2.0_4P_DIP_HOR_RED`；`pin4=I2C_SCL`；`pin3=I2C_SDA`；`pin2=VIN`；`pin1=GND`；`pullups=R2/R3 3.6K/1% to MCU_VDD`；`direction=bidirectional I2C` |
| 总线 | 外部主机到 U1 I2C | `external_connector=J1`；`sda=I2C_SDA -> U1 pin17 PA12/PA10`；`scl=I2C_SCL -> U1 pin16 PA11/PA9`；`pullups=3.6K/1% to MCU_VDD`；`board_controller=U1 STM32G030F6P6` |
| GPIO 与控制信号 | U1 与 DRV11873 控制/状态映射 | `pwm=U1 PA4 pin11 -> DRV_PWM -> U3 pin16 PWM_IN`；`direction=U1 PA5 pin12 -> DRV_FR -> U3 pin15 FR`；`fs=U3 pin1 FS -> U1 PA6 pin13`；`fg=U3 pin2 FG -> U1 PA7 pin14`；`rd=U3 pin3 RD -> U1 pin15 PB0/PB1/PB2/PA8`；`pwm_pulldown=R8 3.6K/1%` |
| 接口 | J2 三相电机接口 | `connector=J2 HT3.96_4P`；`pin4=PHU <- U3 pin10 U`；`pin3=PHV <- U3 pin9 V`；`pin2=PHW <- U3 pin7 W`；`pin1=PCOM <- U3 pin13 COM`；`phases=U,V,W` |
| 电源 | VIN 至 MCU_VDD | `input=VIN`；`series_resistors=R9 150R/1%,R10 10R/1%`；`zener=D2 BZT52C3V3S to GND`；`output=MCU_VDD`；`capacitor=C8 10uF/16V` |
| 电源 | DRV11873 VIN 供电与去耦 | `driver=U3 DRV11873PWPR`；`vcc=pin11 -> VIN`；`local_bulk=C12 22uF/16V`；`input_bulk=C1/C2/C3 22uF/16V`；`v5=pin12 with C7 2.2uF/10V`；`ground=GND` |
| 电源 | DRV11873 电荷泵 | `flying_cap=C9 100nF/50V between CPP pin5 and CPN pin6`；`pump_cap=C11 100nF/50V between VCP pin4 and VCC/VIN`；`driver=U3 DRV11873PWPR` |
| 模拟电路 | PHU/PHV/PHW 到 PCOM 网络 | `phase_u=PHU via R5 1K/1%`；`phase_v=PHV via R6 1K/1%`；`phase_w=PHW via R7 1K/1%`；`common=PCOM -> U3 pin13 COM -> J2 pin1` |
| 保护电路 | 三相输出钳位 | `phase_u=D3 SS16-A to GND`；`phase_v=D4 SS16-A to GND`；`phase_w=D5 SS16-A to GND`；`protected_connector=J2` |
| GPIO 与控制信号 | SYS_LED 绿色指示灯 | `mcu_pin=U1 pin20 PB3/PB4/PB5/PB6`；`net=SYS_LED`；`resistor=R1 3.6K/1%`；`led=D1 绿色`；`return=GND` |
| 调试与烧录 | J3 SWD 下载接口 | `pin1=MCU_VDD`；`pin2=SWCLK -> U1 pin19`；`pin3=SWDIO -> U1 pin18`；`pin4=SYS_RST -> U1 pin6 NRST`；`pin5=GND`；`interface=SWD` |
| 复位 | U1 SYS_RST 复位网络 | `mcu_pin=U1 pin6 NRST`；`net=SYS_RST`；`capacitor=C6 2.2uF/10V to GND`；`debug_pin=J3 pin4`；`external_pullup=null`；`reset_button=null` |
| 时钟 | U1 外部时钟 | `osc_in=PC14_OSC32I unconnected`；`osc_out=PC15_OSC32O unconnected`；`external_crystal=null`；`load_capacitors=null` |
| 总线地址 | 正文中的 I2C 地址 0x65 | `documented_address=0x65`；`controller=U1 STM32G030F6P6`；`scl=I2C_SCL`；`sda=I2C_SDA`；`schematic_address=null`；`hardware_selector=null` |
| 核心器件 | 正文中的无传感器驱动与堵转保护 | `driver=U3 DRV11873PWPR`；`documented_motor=三相无传感器 BLDC`；`documented_functions=堵转保护,PWM 转速控制,方向切换`；`schematic_control=PWM_IN,FR,FG,FS,RD`；`stall_threshold=null`；`protection_timing=null` |
| 电源 | 正文中的带载与整机电流 | `documented_motor_voltage=5V`；`documented_load=DC 5V@508mA`；`documented_standby=DC 5V@10.62mA`；`documented_operating=DC 5V@13.20mA`；`current_set=U3 CS pin14,R4 2K/1%`；`schematic_rating=null`；`test_condition=null` |

## 待确认事项

- `address.documented-i2c-address`：产品正文标称默认 I2C 地址为 0x65；本页原理图只显示 J1、R2/R3 和 U1 的 I2C_SCL/I2C_SDA 网络，没有地址电阻、拨码选择、地址文字或固件寄存器。（证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B1-B2，J1/R2/R3/U1 I2C 网络，图中无 0x65）
- `component.documented-driver-functions`：产品正文称 DRV11873PWPR 驱动三相无传感器 BLDC，并集成堵转保护、PWM 转速控制和方向切换；原理图确认 U3 型号、PWM_IN/FR/FG/FS/RD 与三相输出，但没有展开内部换相、堵转阈值、保护时序或适用电机参数。（证据：图 a778bea573af / 第 1 页 / 第 1 页网格 B3，U3 DRV11873PWPR 外部引脚与 PHU/PHV/PHW/PCOM）
- `power.documented-current-ratings`：产品正文标称电机驱动 5V、输出带载 DC 5V@508mA、待机 DC 5V@10.62mA、工作 DC 5V@13.20mA；原理图只显示 VIN 电源路径、CS 设置电阻和去耦，没有标注这些额定值、测试条件或容差。（证据：图 a778bea573af / 第 1 页 / 第 1 页 VIN/U3/J2/R4/C1-C3/C12 电源与输出电路，未标额定电流）
- `review.i2c-address`：请用 U181 当前固件、I2C 协议或总线扫描确认默认地址 0x65 及修改/持久化规则。；原因：原理图没有地址文字或硬件地址配置。
- `review.driver-functions`：请用 DRV11873 资料和 U181 固件确认无传感器换相、堵转检测阈值/恢复行为、PWM 范围、方向切换约束及 FG/FS/RD 语义。；原因：板级原理图仅显示驱动器外部连接，未展开内部功能参数。
- `review.current-ratings`：请用量产规格或实测确认 5V@508mA 带载能力、10.62mA 待机、13.20mA 工作电流及温升/电机条件。；原因：原理图未标整机电流额定值、测试负载或热边界。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a778bea573af57d753554f3029fddaefd4d1a1486507b24400603c2fd8fe619e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/633/Sch_bldc_driver_V1.3_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-BLDC Driver.md`

源文档 SHA-256：`676467488d7d494e9197825656fbefc9ae8e151694a7bc7ba5a3fd67168e0c97`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
