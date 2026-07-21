# Unit DigiClock 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DigiClock |
| SKU | U146 |
| 产品 ID | `unit-digiclock-63cf25e6b4eb` |
| 源文档 | `zh_CN/unit/digi_clock.md` |

## 概述

Unit DigiClock（U146）以 U2 STM32F030F4P6 作为外部 I2C 从设备控制器，通过 PA9/PA10 连接并联的 J1/J2 Grove SCL/SDA，并由 ADDR1-ADDR4 四位拨码网络读取地址配置。U2 使用 PA0/PA1 的 DIO/CLK 控制 U1 TM1637，TM1637 再以 A-G、DP 与 D1-D5 驱动 DS1 Dpy Amber-CA 四位数码显示器及冒号/小数点。J1/J2 输入 +5V，U3 HT7533 生成 +3.3V 供 MCU 和逻辑上拉；TM1637 VDD 则由 +5V 经 D1 B5819W SL 供电。板上还提供 P1 五针 SWD、NRST RC 和 BOOT0 下拉；正文中的默认地址 0x30、拨码地址映射、红色/2.1 英寸、8 级亮度及功耗数据未直接印在原理图上。

## 检索关键词

`Unit DigiClock`、`U146`、`STM32F030F4P6`、`TM1637`、`Dpy Amber-CA`、`HT7533`、`B5819W SL`、`SW DIP-4`、`HY-2.0_IIC`、`SWD_5p`、`I2C`、`0x30`、`SCL`、`SDA`、`PA9`、`PA10`、`DIO`、`CLK`、`PA0`、`PA1`、`ADDR1`、`ADDR2`、`ADDR3`、`ADDR4`、`BOOT0`、`NRST`、`SWCLK`、`SWDIO`、`+5V`、`+3.3V`、`D1-D5`、`A-G`、`DP`、`四位数码管`、`冒号`、`小数点`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | I2C 从设备控制器，读取地址拨码并以 DIO/CLK 控制 TM1637，同时提供 SWD/复位/BOOT 接口 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 C1-C2，U2 STM32F030F4P6 pin1-pin20 与 BOOT0/NRST/DIO/CLK/ADDR1-4/SCL/SDA/SWDIO/SWCLK |
| U1 | TM1637 | 由 MCU DIO/CLK 控制的数码管驱动器，输出 SEG1-SEG8 与 GRID1-GRID5 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 A2-B2，U1 TM1637 pin1-pin20，A-G/DP、D1-D5、CLK/DIO/VDD/GND |
| DS1 | Dpy Amber-CA | 四位七段显示器，带小数点和中间冒号，由 A-G/DP 与 D1-D5 网络复用驱动 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 A3-B4，DS1 Dpy Amber-CA 图形与 pin1-pin14 的 E/D/DP/C/G/D4/D5/D1/A/F/D2/D3/B/DP |
| U3 | HT7533 | 将 +5V 稳压为 MCU、地址网络和逻辑上拉使用的 +3.3V | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 A1，U3 HT7533，VIN pin2 +5V、VOUT pin3 +3.3V、GND pin1 |
| D1 | B5819W SL | 串联在 +5V 与 U1 TM1637 VDD 电源节点之间的肖特基二极管 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 A2，器件 D1 B5819W SL 位于 +5V 与 U1 VDD/C1/C2 节点之间 |
| S1 | SW DIP-4 | 四位地址配置开关，分别将 ADDR1-ADDR4 闭合接地 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 D1-D2，S1 SW DIP-4，pins1-4 接 ADDR1-ADDR4、pins8-5 共接 GND |
| J1,J2 | HY-2.0_IIC | 两只并联的四针 Grove I2C 连接器，提供 SCL、SDA、+5V 和 GND，可用于总线串接 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 C4，J1/J2 HY-2.0_IIC 均为 pin1 SCL、pin2 SDA、pin3 +5V、pin4 GND |
| P1 | SWD_5p | STM32 五针 SWD 调试与复位接口 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 C3，P1 SWD_5p pin1 VCC、pin2 SWCLK、pin3 SWDIO、pin4 RST、pin5 GND |
| Rp1,Rp2,R1,R2 | 10KΩ(103)±5% / 10KΩ | I2C、复位、BOOT、地址拨码与 TM1637 DIO/CLK 的上拉/下拉网络 | 图 462b70c98a00 / 第 1 页 / 第 1 页网格 A2/C2/D1，R1/R2 10KΩ；Rp1/Rp2 均标 10KΩ(103)±5% |
| C1,C2,C3,C4,C5,C6,C7 | 100nF / 22uF | TM1637、STM32、HT7533 输入输出及 NRST 的去耦、储能和复位电容 | 图 462b70c98a00 / 第 1 页 / 第 1 页：C1/C3/C4/C5 100nF，C2/C6/C7 22uF，分别位于 U1/U2/U3 电源与 NRST 网络 |

## 系统结构

### Unit DigiClock 系统架构

U2 STM32F030F4P6 通过 J1/J2 的 SCL/SDA 接入外部 I2C 主机，读取 S1 的 ADDR1-ADDR4 地址状态，并通过 DIO/CLK 控制 U1 TM1637；TM1637 以 A-G、DP、D1-D5 驱动 DS1。U3 从 +5V 生成 +3.3V，P1 提供 SWD。完整单页未显示外部存储器、协处理器、射频、音频、传感器、电池或充电电路。

- 参数与网络：`controller=U2 STM32F030F4P6`；`display_driver=U1 TM1637`；`display=DS1 Dpy Amber-CA`；`host_bus=I2C SCL/SDA via J1/J2`；`address_switch=S1 ADDR1-ADDR4`；`debug=P1 SWD_5p`；`regulator=U3 HT7533`；`external_storage=null`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页完整网格 A1-D4，U1/U2/U3/DS1/S1/P1/J1/J2 及所有网络

## 核心器件

### STM32F030F4P6 关键引脚映射

U2 pin1 BOOT0 接 BOOT0，pin4 NRST 接 NRST，pin5/pin16 VDD 接 +3.3V，pin15 VSS 接 GND；PA0 pin6 接 DIO、PA1 pin7 接 CLK，PA4 pin10 至 PA7 pin13 依次接 ADDR1-ADDR4，PA9 pin17 接 SCL、PA10 pin18 接 SDA，PA13 pin19 接 SWDIO、PA14 pin20 接 SWCLK。

- 参数与网络：`boot=pin1 BOOT0`；`reset=pin4 NRST`；`power=pins5/16 +3.3V,pin15 GND`；`display_bus=pin6 PA0 DIO,pin7 PA1 CLK`；`address_gpio=pin10 PA4 ADDR1,pin11 PA5 ADDR2,pin12 PA6 ADDR3,pin13 PA7 ADDR4`；`i2c=pin17 PA9 SCL,pin18 PA10 SDA`；`swd=pin19 PA13 SWDIO,pin20 PA14 SWCLK`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C1-C2，U2 STM32F030F4P6 pin1-pin20 标注和同名网络

### TM1637 到 DS1 段线与位选

U1 SEG1/KS1 至 SEG8/KS8（pins2-9）依次连接 A、B、C、D、E、F、G、DP；GRID1 至 GRID5（pins15-11）依次连接 D1、D2、D3、D4、D5。DS1 用这些网络连接四个七段数字、各小数点和中间冒号；U1 GRID6 pin10、K1 pin19、K2 pin20 未连接。

- 参数与网络：`segments=U1 pins2-9 -> A,B,C,D,E,F,G,DP`；`grids=U1 pins15-11 -> D1,D2,D3,D4,D5`；`display=DS1 Dpy Amber-CA`；`grid6=U1 pin10 NC`；`key_scan=U1 pins19/20 K1/K2 NC`；`visible_format=4 digits,decimal points,colon`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 A2-B4，U1 A-G/DP/D1-D5 输出与 DS1 pin1-pin14/显示图形

## 电源

### +5V 至 +3.3V 稳压

J1/J2 pin3 将 +5V 输入引到 U3 HT7533 VIN pin2，U3 VOUT pin3 输出 +3.3V，GND pin1 接地。C7 22uF 位于 +5V 输入侧，C5 100nF 与 C6 22uF 位于 +3.3V 输出侧；+3.3V 为 U2、P1 和各逻辑上拉网络供电。

- 参数与网络：`input=J1/J2 pin3 +5V`；`regulator=U3 HT7533`；`vin=pin2 +5V`；`vout=pin3 +3.3V`；`input_cap=C7 22uF`；`output_caps=C5 100nF,C6 22uF`；`loads=U2 VDD,P1 VCC,R1/R2,Rp1/Rp2`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 A1 U3/C5/C6/C7 与网格 C4 J1/J2 +5V

### TM1637 显示驱动电源

+5V 经 D1 B5819W SL 串联后连接 U1 TM1637 VDD pin16 及 C1 100nF/C2 22uF 去耦节点，U1 GND pin1 接地。CLK/DIO 则分别经 R1/R2 10KΩ 上拉到 +3.3V，与 VDD 供电路径分开。

- 参数与网络：`driver=U1 TM1637`；`supply_path=+5V -> D1 B5819W SL -> U1 pin16 VDD`；`ground=U1 pin1 GND`；`decoupling=C1 100nF,C2 22uF`；`clock_pullup=R1 10KΩ to +3.3V`；`data_pullup=R2 10KΩ to +3.3V`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 A2，U1 VDD/GND、D1 B5819W SL、C1/C2 与 R1/R2

## 接口

### J1/J2 双 Grove I2C 接口

J1 与 J2 均为 HY-2.0_IIC，且四针同名网络并联：pin1=SCL，pin2=SDA，pin3=+5V，pin4=GND。两只接口没有独立使能或隔离，可作为同一 I2C/供电网络的两个物理连接点。

- 参数与网络：`connectors=J1,J2 HY-2.0_IIC`；`pin1=SCL bidirectional I2C clock`；`pin2=SDA bidirectional I2C data`；`pin3=+5V power`；`pin4=GND`；`electrical_relationship=parallel same nets`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C4，J1/J2 pin1-pin4 的 SCL/SDA/+5V/GND

## 总线

### 外部主机 I2C 总线

J1/J2 SCL 连接 U2 PA9 pin17，SDA 连接 U2 PA10 pin18；Rp1 中两只 10KΩ 电阻分别将 SCL、SDA 上拉至 +3.3V。原理图未显示 I2C 电平转换、复用器或其他 I2C 从设备。

- 参数与网络：`external_controller=via J1/J2`；`device=U2 STM32F030F4P6`；`scl=J1/J2 pin1 -> PA9 pin17`；`sda=J1/J2 pin2 -> PA10 pin18`；`pullups=Rp1 10KΩ SCL/SDA to +3.3V`；`level_shifter=null`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C1-C4，Rp1 SCL/SDA、U2 PA9/PA10 与 J1/J2 同名网络

### STM32 到 TM1637 的 DIO/CLK 控制总线

U2 PA0 pin6 的 DIO 连接 U1 DIO pin17，U2 PA1 pin7 的 CLK 连接 U1 CLK pin18；R2/R1 各 10KΩ 分别将 DIO/CLK 上拉到 +3.3V。该两线控制总线与外部 SCL/SDA I2C 网络名称和引脚均独立。

- 参数与网络：`controller=U2 STM32F030F4P6`；`device=U1 TM1637`；`data=PA0 pin6 DIO -> U1 pin17`；`clock=PA1 pin7 CLK -> U1 pin18`；`pullups=R2 DIO,R1 CLK,10KΩ to +3.3V`；`external_i2c=separate SCL/SDA`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页 U2 PA0/PA1 的 DIO/CLK 与 U1 pin17/pin18、R1/R2

## GPIO 与控制信号

### ADDR1-ADDR4 四位拨码输入

U2 PA4 pin10、PA5 pin11、PA6 pin12、PA7 pin13 依次连接 ADDR1、ADDR2、ADDR3、ADDR4。Rp2 四只 10KΩ 将每个地址位上拉到 +3.3V，S1 四个开关闭合时分别将对应地址位接 GND，因此每位形成上拉默认高、闭合为低的输入。

- 参数与网络：`ADDR1=PA4 pin10,Rp2 10KΩ pull-up,S1 switch1 to GND`；`ADDR2=PA5 pin11,Rp2 10KΩ pull-up,S1 switch2 to GND`；`ADDR3=PA6 pin12,Rp2 10KΩ pull-up,S1 switch3 to GND`；`ADDR4=PA7 pin13,Rp2 10KΩ pull-up,S1 switch4 to GND`；`open_state=high`；`closed_state=low`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C2-D2，U2 ADDR1-4、Rp2 10KΩ、S1 SW DIP-4 与 GND

## 时钟

### MCU 时钟连接

U2 PF0/OSC_IN pin2 与 PF1/OSC_OUT pin3 仅显示未连接短线，完整单页没有晶振、谐振器或外部振荡器连接到 MCU；TM1637 的 CLK 是由 U2 PA1 驱动的控制信号，不是板级晶振。

- 参数与网络：`osc_in=U2 pin2 NC`；`osc_out=U2 pin3 NC`；`external_crystal=null`；`tm1637_clock=PA1 CLK control signal`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C1-C2，U2 pin2 PF0/OSC_IN、pin3 PF1/OSC_OUT 未连接；整页无晶振

## 复位

### NRST 与 BOOT0 配置

U2 NRST pin4 由 Rp1 10KΩ 上拉到 +3.3V，并由 C3 100nF 接 GND，同时引到 P1 pin4 RST。U2 BOOT0 pin1 由 Rp1 10KΩ 下拉到 GND；图中没有 BOOT 按键或跳线。

- 参数与网络：`reset_pin=U2 pin4 NRST`；`reset_pullup=Rp1 10KΩ to +3.3V`；`reset_cap=C3 100nF to GND`；`debug_reset=P1 pin4 RST`；`boot_pin=U2 pin1 BOOT0`；`boot_pulldown=Rp1 10KΩ to GND`；`boot_switch=null`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C1-C3，Rp1 NRST/BOOT0、C3、U2 pin1/pin4 与 P1 RST

## 保护电路

### Grove 接口保护配置

完整单页在 J1/J2 的 +5V、SCL、SDA 和 GND 路径上未显示 TVS/ESD 阵列、保险丝、反接保护或串联信号限流器件；D1 B5819W SL 位于 TM1637 供电支路，不在 Grove 输入总路径上。

- 参数与网络：`connectors=J1,J2`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`tm1637_series_diode=D1 B5819W SL`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页完整 J1/J2 到 U2/U3 的 +5V/SCL/SDA/GND 路径

## 关键网络

### 关键电源与信号网络索引

+5V 连接 J1/J2 pin3、U3 VIN 与 D1；+3.3V 连接 U3 VOUT、U2 VDD、P1 VCC、Rp1/Rp2 和 R1/R2。SCL/SDA 从 J1/J2 到 U2 PA9/PA10；DIO/CLK 从 U2 PA0/PA1 到 U1；ADDR1-ADDR4 从 U2 PA4-PA7 到 Rp2/S1；A-G/DP 与 D1-D5 从 U1 到 DS1。

- 参数与网络：`+5V=J1/J2 pin3,U3 VIN,D1`；`+3.3V=U3 VOUT,U2 VDD,P1 VCC,Rp1/Rp2,R1/R2`；`I2C=SCL PA9,SDA PA10`；`display_control=DIO PA0,CLK PA1`；`address=ADDR1-ADDR4 PA4-PA7`；`display_matrix=A-G,DP,D1-D5`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页全部 +5V/+3.3V/SCL/SDA/DIO/CLK/ADDR1-4/A-G/DP/D1-D5 同名网络

## 调试与烧录

### P1 SWD 调试接口

P1 SWD_5p pin1 VCC 接 +3.3V，pin2 SWCLK 接 U2 PA14 pin20，pin3 SWDIO 接 U2 PA13 pin19，pin4 RST 接 NRST，pin5 接 GND。

- 参数与网络：`pin1=VCC +3.3V`；`pin2=SWCLK -> PA14 pin20`；`pin3=SWDIO -> PA13 pin19`；`pin4=RST -> NRST pin4`；`pin5=GND`
- 证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C3，P1 SWD_5p 与 U2 SWCLK/SWDIO/NRST 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit DigiClock 系统架构 | `controller=U2 STM32F030F4P6`；`display_driver=U1 TM1637`；`display=DS1 Dpy Amber-CA`；`host_bus=I2C SCL/SDA via J1/J2`；`address_switch=S1 ADDR1-ADDR4`；`debug=P1 SWD_5p`；`regulator=U3 HT7533`；`external_storage=null` |
| 核心器件 | STM32F030F4P6 关键引脚映射 | `boot=pin1 BOOT0`；`reset=pin4 NRST`；`power=pins5/16 +3.3V,pin15 GND`；`display_bus=pin6 PA0 DIO,pin7 PA1 CLK`；`address_gpio=pin10 PA4 ADDR1,pin11 PA5 ADDR2,pin12 PA6 ADDR3,pin13 PA7 ADDR4`；`i2c=pin17 PA9 SCL,pin18 PA10 SDA`；`swd=pin19 PA13 SWDIO,pin20 PA14 SWCLK` |
| 电源 | +5V 至 +3.3V 稳压 | `input=J1/J2 pin3 +5V`；`regulator=U3 HT7533`；`vin=pin2 +5V`；`vout=pin3 +3.3V`；`input_cap=C7 22uF`；`output_caps=C5 100nF,C6 22uF`；`loads=U2 VDD,P1 VCC,R1/R2,Rp1/Rp2` |
| 电源 | TM1637 显示驱动电源 | `driver=U1 TM1637`；`supply_path=+5V -> D1 B5819W SL -> U1 pin16 VDD`；`ground=U1 pin1 GND`；`decoupling=C1 100nF,C2 22uF`；`clock_pullup=R1 10KΩ to +3.3V`；`data_pullup=R2 10KΩ to +3.3V` |
| 接口 | J1/J2 双 Grove I2C 接口 | `connectors=J1,J2 HY-2.0_IIC`；`pin1=SCL bidirectional I2C clock`；`pin2=SDA bidirectional I2C data`；`pin3=+5V power`；`pin4=GND`；`electrical_relationship=parallel same nets` |
| 总线 | 外部主机 I2C 总线 | `external_controller=via J1/J2`；`device=U2 STM32F030F4P6`；`scl=J1/J2 pin1 -> PA9 pin17`；`sda=J1/J2 pin2 -> PA10 pin18`；`pullups=Rp1 10KΩ SCL/SDA to +3.3V`；`level_shifter=null` |
| 总线 | STM32 到 TM1637 的 DIO/CLK 控制总线 | `controller=U2 STM32F030F4P6`；`device=U1 TM1637`；`data=PA0 pin6 DIO -> U1 pin17`；`clock=PA1 pin7 CLK -> U1 pin18`；`pullups=R2 DIO,R1 CLK,10KΩ to +3.3V`；`external_i2c=separate SCL/SDA` |
| GPIO 与控制信号 | ADDR1-ADDR4 四位拨码输入 | `ADDR1=PA4 pin10,Rp2 10KΩ pull-up,S1 switch1 to GND`；`ADDR2=PA5 pin11,Rp2 10KΩ pull-up,S1 switch2 to GND`；`ADDR3=PA6 pin12,Rp2 10KΩ pull-up,S1 switch3 to GND`；`ADDR4=PA7 pin13,Rp2 10KΩ pull-up,S1 switch4 to GND`；`open_state=high`；`closed_state=low` |
| 复位 | NRST 与 BOOT0 配置 | `reset_pin=U2 pin4 NRST`；`reset_pullup=Rp1 10KΩ to +3.3V`；`reset_cap=C3 100nF to GND`；`debug_reset=P1 pin4 RST`；`boot_pin=U2 pin1 BOOT0`；`boot_pulldown=Rp1 10KΩ to GND`；`boot_switch=null` |
| 调试与烧录 | P1 SWD 调试接口 | `pin1=VCC +3.3V`；`pin2=SWCLK -> PA14 pin20`；`pin3=SWDIO -> PA13 pin19`；`pin4=RST -> NRST pin4`；`pin5=GND` |
| 时钟 | MCU 时钟连接 | `osc_in=U2 pin2 NC`；`osc_out=U2 pin3 NC`；`external_crystal=null`；`tm1637_clock=PA1 CLK control signal` |
| 核心器件 | TM1637 到 DS1 段线与位选 | `segments=U1 pins2-9 -> A,B,C,D,E,F,G,DP`；`grids=U1 pins15-11 -> D1,D2,D3,D4,D5`；`display=DS1 Dpy Amber-CA`；`grid6=U1 pin10 NC`；`key_scan=U1 pins19/20 K1/K2 NC`；`visible_format=4 digits,decimal points,colon` |
| 关键网络 | 关键电源与信号网络索引 | `+5V=J1/J2 pin3,U3 VIN,D1`；`+3.3V=U3 VOUT,U2 VDD,P1 VCC,Rp1/Rp2,R1/R2`；`I2C=SCL PA9,SDA PA10`；`display_control=DIO PA0,CLK PA1`；`address=ADDR1-ADDR4 PA4-PA7`；`display_matrix=A-G,DP,D1-D5` |
| 保护电路 | Grove 接口保护配置 | `connectors=J1,J2`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`tm1637_series_diode=D1 B5819W SL` |
| 总线地址 | I2C 默认地址与拨码映射 | `documented_default_address=0x30`；`address_inputs=ADDR1-ADDR4`；`open_level=high`；`closed_level=low`；`switch_to_address_map=null`；`schematic_default_switch_position=null` |
| 其他事实 | 正文中的显示颜色、尺寸与亮度级数 | `documented_size=2.1 inch`；`documented_color=red`；`schematic_part_text=Dpy Amber-CA`；`documented_brightness_levels=8`；`schematic_format=4 digits,decimal points,colon`；`wavelength=null` |
| 电源 | 正文中的 5V 功耗数据 | `supply=DC 5V`；`standby=2.5mA`；`SG1=6.6mA`；`SG2=10.3mA`；`SG3=17.5mA`；`SG4=38.7mA`；`SG5=42.0mA`；`SG6=45.7mA`；`SG7=49.2mA`；`SG8=52.5mA`；`schematic_measurement_conditions=null` |

## 待确认事项

- `address.documented-default-and-map`：产品正文列出 I2C 通信地址 0x30，并称四位拨码可修改地址；原理图确认 ADDR1-ADDR4 的高/低硬件输入拓扑，但没有列出开关组合到 7 位 I2C 地址的映射，也未标默认拨码位置。（证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 C2-D2，U2 ADDR1-4、Rp2 与 S1；整页无 0x30 或地址表）
- `other.documented-display-spec`：产品正文称显示器为 2.1 英寸、四位红色数字并支持 8 级亮度；原理图确认四位数字、小数点和冒号，但 DS1 型号文字为 Dpy Amber-CA，且页面未给出 2.1 英寸尺寸、发光波长/颜色验证或亮度级数。（证据：图 462b70c98a00 / 第 1 页 / 第 1 页网格 A3-B4，DS1 Dpy Amber-CA 图形与引脚；无尺寸或亮度表）
- `power.documented-current-levels`：产品正文列出 DC 5V 下待机 2.5mA、SG1 6.6mA、SG2 10.3mA、SG3 17.5mA、SG4 38.7mA、SG5 42.0mA、SG6 45.7mA、SG7 49.2mA、SG8 52.5mA；原理图只显示供电和负载拓扑，没有电流测量条件、显示内容、刷新状态或器件容差。（证据：图 462b70c98a00 / 第 1 页 / 第 1 页 +5V/U3/U2/U1/DS1 供电与负载网络，图中无电流数据）
- `review.i2c-address-map`：请用 U146 固件/寄存器协议或总线扫描确认默认地址 0x30，以及 S1 四位开关各组合对应的 7 位 I2C 地址。；原因：原理图只显示 ADDR1-ADDR4 电平拓扑，没有地址算法、默认位置或地址表。
- `review.display-spec`：请用当前 DS1 BOM、结构图或实物确认 2.1 英寸、红色/Amber 标识关系、发光参数及 8 级亮度实现。；原因：原理图 DS1 标为 Dpy Amber-CA，与正文红色描述需核对，且图中无尺寸和亮度级数。
- `review.power-current-test`：请按明确显示内容、亮度命令、刷新状态、输入电压和环境条件复测待机及 SG1-SG8 电流。；原因：原理图不能证明整机各亮度状态的实测电流。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `462b70c98a003824482648ef3997a0ee6882ab78a89a924b39bdcd09f3613e9e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/601/Sch_UNIT_Digi-Clock_sch_01.png` |

---

源文档：`zh_CN/unit/digi_clock.md`

源文档 SHA-256：`c850f3902679a32b35f901396da0aaa6b1a548b26f99e00a277da27d242838c7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
