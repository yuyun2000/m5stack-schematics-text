# Unit NCIR2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NCIR2 |
| SKU | U150 |
| 产品 ID | `unit-ncir2-f812153e5668` |
| 源文档 | `zh_CN/unit/NCIR2.md` |

## 概述

Unit NCIR2 以 U2 STM32F030F4P6 为数据处理 MCU，通过内部 SCL1/SDA1 总线连接 U3 MLX90614，并通过另一组 SCL/SDA 连接 J2 Grove，因此传感器与主机总线由 MCU 隔开。U2 还驱动 LED1 SK6812、Q1/LS1 蜂鸣器并读取 key1 按键，P2 提供 SWD，S1 提供复位。+5V 经 U1 SY8089 生成 +3.3V；正文中的 0x5A、MLX90614ESF-BAA 后缀、测温性能及告警/独立运行固件行为未在原理图中直接标注。

## 检索关键词

`Unit NCIR2`、`U150`、`STM32F030F4P6`、`MLX90614`、`MLX90614ESF-BAA`、`SY8089`、`SK6812`、`I2C`、`0x5A`、`SCL`、`SDA`、`SCL1`、`SDA1`、`PA9`、`PA10`、`PA3`、`PA4`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`key1`、`BEEP`、`LS1 Buzzer`、`Q1 SS8050`、`+5V`、`+3.3V`、`HY-2.0_IIC`、`SWD_5p`、`OUT3`、`OUT4`、`non-contact IR temperature`、`非接触测温`、`高低温告警`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | 读取 MLX90614、处理温度数据、提供外部 I2C 并控制 RGB、蜂鸣器与按键的 MCU | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B2-C3：U2 STM32F030F4P6 全部 pins1-20 |
| U3 | MLX90614 | 通过 SCL1/SDA1 连接 MCU 的非接触式红外测温传感器 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 D2-D3：U3 MLX90614，SCL/SDA/VDD/GND |
| U1 | SY8089 | 将 +5V 降压生成 +3.3V | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 A1-A2：U1 SY8089、L1、R1/R2 与 +5V/+3.3V |
| J2 | HY-2.0_IIC | 外部主机的 SCL、SDA、+5V、GND Grove 接口 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B4：J2 HY-2.0_IIC pin1-pin4 |
| P2 | SWD_5p | MCU 的 +3.3V、SWCLK、SWDIO、NRST、GND 调试接口 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 A4：P2 SWD_5p pin1-pin5 |
| LED1 | SK6812 | 由 U2 PA0 的 SK6812 网络控制的 RGB 指示灯 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 D1-D2：LED1 SK6812、DIN/DOUT/VDD/VSS |
| LS1,Q1 | Buzzer / SS8050 Y1 | 由 BEEP 网络控制的蜂鸣器与低侧驱动晶体管 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 C4-D4：LS1、Q1、BEEP、R9/R11/R13、D7 |
| S2 | SMT_SW_PTS_820 | 将 key1 按下接 GND 的功能按键 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B1：S2/OS2 SMT_SW_PTS_820、key1、R4、D1 |
| S1 | SW-PB | 将 NRST 按下接 GND 的复位按键 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B2：S1 SW-PB、NRST、R3/C6/D2 |
| R5,R6 | 4.7KΩ / 4.7KΩ | 外部 SCL/SDA 总线到 +3.3V 的上拉电阻 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B3-B4：R5/R6 4.7KΩ 从 +3.3V 到 SCL/SDA |
| R8,R10 | 4.7KΩ / 4.7KΩ | MLX90614 SCL1/SDA1 内部 I2C 到 +3.3V 的上拉电阻 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 D2-D3：R8/R10 4.7KΩ 从 SCL1/SDA1 到 +3.3V |
| D1,D2,D3,D4,D5,D6 | RLSD52A031V / LESD3Z5.0CMT1G | 按键、复位、Grove 信号/电源和传感器电源节点的对地 ESD/瞬态保护 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页 D1-D6 各对地保护支路 |
| L1,R1,R2 | 3015 4.7uH / 68KΩ / 15KΩ | SY8089 输出电感与反馈网络 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 A1-A2：L1 3015 4.7uH、R1 68KΩ、R2 15KΩ |
| D7 | 1N4007WS | 跨接 LS1 蜂鸣器两端的钳位/续流二极管 | 图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 C4-D4：D7 1N4007WS 与 LS1 并联 |

## 系统结构

### Unit NCIR2 系统结构

U2 STM32F030F4P6 通过 SCL1/SDA1 读取 U3 MLX90614，并通过独立的 SCL/SDA 与 J2 主机通信；U2 还连接 SK6812、key1、BEEP、SWD 与 NRST。+5V 经 U1 生成 +3.3V。

- 参数与网络：`controller=U2 STM32F030F4P6`；`sensor=U3 MLX90614`；`internal_bus=SCL1/SDA1`；`host_bus=SCL/SDA`；`rgb=LED1 SK6812`；`button=key1`；`buzzer=BEEP -> Q1/LS1`；`power=+5V -> U1 SY8089 -> +3.3V`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 电源

### +5V 至 +3.3V

+5V 接 U1 SY8089 VIN pin4 与 EN pin1，SW pin3 经 L1 4.7uH 输出 +3.3V；FB pin5 使用 R1 68KΩ/R2 15KΩ，C4 22uF/C5 100nF 为输入电容，C2 100nF/C3 22uF 为输出电容。

- 参数与网络：`input=+5V`；`converter=U1 SY8089`；`enable=pin1 tied +5V`；`inductor=L1 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ,R2 15KΩ`；`input_caps=C4 22uF,C5 100nF`；`output_caps=C2 100nF,C3 22uF`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 A1-A2 U1/L1/R1/R2/C2-C5

### MCU 3.3V 供电与去耦

U2 VDDA pin5 与 VDD pin16 接 +3.3V，VSS pin15 接 GND；C10 22uF 与 C11 100nF 跨接 +3.3V/GND。

- 参数与网络：`vdda=U2 pin5 +3.3V`；`vdd=U2 pin16 +3.3V`；`vss=U2 pin15 GND`；`caps=C10 22uF,C11 100nF`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 电源脚与 C10/C11

## 接口

### J2 Grove I2C

J2 pin1=IIC_SCL/SCL、pin2=IIC_SDA/SDA、pin3=+5V、pin4=GND；SCL/SDA 分别经 R5/R6 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND`；`pullups=R5/R6 4.7KΩ to +3.3V`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B3-B4 J2/R5/R6

## 总线

### STM32 外部 I2C

U2 PA10 pin18 连接 SDA，PA9 pin17 连接 SCL；这组网络经 R5/R6 上拉后连接 J2，与 MLX90614 的 SCL1/SDA1 不同名。

- 参数与网络：`controller=U2 STM32F030F4P6`；`sda=PA10 pin18 SDA`；`scl=PA9 pin17 SCL`；`connector=J2`；`sensor_directly_shared=false`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 PA9/PA10 与 J2 SCL/SDA

### STM32 至 MLX90614 I2C

U2 PA3 pin9 连接 SCL1，PA4 pin10 连接 SDA1；U3 MLX90614 pin1 SCL 接 SCL1、pin2 SDA 接 SDA1，R8/R10 各 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`controller_scl=U2 PA3 pin9 SCL1`；`controller_sda=U2 PA4 pin10 SDA1`；`sensor_scl=U3 pin1`；`sensor_sda=U3 pin2`；`pullups=R8/R10 4.7KΩ`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 PA3/PA4 至 U3 SCL/SDA 与 R8/R10

## GPIO 与控制信号

### STM32 主要 GPIO 映射

U2 PA0 pin6=SK6812、PA1 pin7=key1、PA3 pin9=SCL1、PA4 pin10=SDA1、PB1 pin14=BEEP、PA9 pin17=SCL、PA10 pin18=SDA、PA13 pin19=SWDIO、PA14 pin20=SWCLK。

- 参数与网络：`pa0=pin6 SK6812`；`pa1=pin7 key1`；`pa3=pin9 SCL1`；`pa4=pin10 SDA1`；`pb1=pin14 BEEP`；`pa9=pin17 SCL`；`pa10=pin18 SDA`；`pa13=pin19 SWDIO`；`pa14=pin20 SWCLK`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 全部已连接 GPIO 网络

### key1 功能按键

U2 PA1 pin7 的 key1 节点经 R4 10KΩ 上拉至 +3.3V，S2 按下接 GND，D1 RLSD52A031V 对地保护。

- 参数与网络：`mcu_pin=U2 PA1 pin7`；`net=key1`；`pullup=R4 10KΩ`；`button=S2 to GND`；`esd=D1`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B1 key1/R4/S2/D1 与 U2 PA1

### SK6812 RGB 指示灯

U2 PA0 pin6 的 SK6812 网络连接 LED1 DIN pin3；LED1 VDD pin4 接 +3.3V、VSS pin2 接 GND、DOUT pin1 未连接，R12 4.7KΩ 将数据节点上拉到 +3.3V，C14 100nF 去耦。

- 参数与网络：`control=U2 PA0 pin6`；`din=LED1 pin3`；`vdd=pin4 +3.3V`；`vss=pin2 GND`；`dout=pin1 NC`；`pullup=R12 4.7KΩ`；`cap=C14 100nF`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 D1-D2 LED1/R12/C14 与 U2 PA0

## 时钟

### STM32 时钟引脚

U2 PF0-OSC_IN pin2 与 PF1-OSC_OUT pin3 分别连接 OUT3、OUT4 网络，没有外接晶振或负载电容；原理图未标 MCU 工作频率。

- 参数与网络：`osc_in=PF0 pin2 OUT3`；`osc_out=PF1 pin3 OUT4`；`external_crystal=false`；`frequency=null`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 PF0/PF1 的 OUT3/OUT4 网络

## 复位

### NRST 复位网络

U2 NRST pin4 经 R3 10KΩ 上拉到 +3.3V、C6 100nF 接 GND，S1 按下接 GND，D2 RLSD52A031V 对地保护；NRST 同时引至 P2 pin4。

- 参数与网络：`mcu=U2 pin4 NRST`；`pullup=R3 10KΩ`；`cap=C6 100nF`；`button=S1 to GND`；`esd=D2`；`debug=P2 pin4`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 B2 NRST/R3/C6/S1/D2 与 A4 P2

### BOOT0 配置

U2 BOOT0 pin1 经 R7 10KΩ 下拉至 GND；本页没有 BOOT0 按键或跳线。

- 参数与网络：`boot0=U2 pin1`；`pulldown=R7 10KΩ to GND`；`button=null`；`jumper=null`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2 BOOT0 pin1 与 R7

## 保护电路

### Grove 与控制节点保护

J2 SCL、SDA、+5V 分别通过 D4、D5、D3 对地保护；key1/NRST 通过 D1/D2 保护，MLX90614 3.3V 侧配置 D6。图中未显示保险丝或反接保护。

- 参数与网络：`scl=D4 RLSD52A031V`；`sda=D5 RLSD52A031V`；`vcc5=D3 LESD3Z5.0CMT1G`；`key=D1`；`reset=D2`；`sensor_3v3=D6`；`fuse=null`；`reverse_protection=null`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 D1-D6 与对应网络

## 内存与 Flash

### 存储器

完整单页没有外部 Flash、EEPROM、RAM 或存储卡；原理图也未标 STM32 内部 Flash/RAM 容量。

- 参数与网络：`external_flash=null`；`external_eeprom=null`；`external_ram=null`；`storage_card=null`；`internal_flash_capacity=null`；`internal_ram_capacity=null`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页完整原理图，无独立存储器件

## 音频

### 蜂鸣器驱动

U2 PB1 pin14 的 BEEP 经 R11 1KΩ 驱动 Q1 SS8050，R13 4.7KΩ 下拉基极；+3.3V 经 R9 10Ω 和 LS1 到 Q1 集电极，D7 1N4007WS 跨接 LS1。

- 参数与网络：`control=U2 PB1 pin14 BEEP`；`base_resistor=R11 1KΩ`；`base_pulldown=R13 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`load=+3.3V -> R9 10Ω -> LS1 -> Q1 -> GND`；`diode=D7 1N4007WS`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 C4-D4 BEEP/R9/R11/R13/Q1/LS1/D7

## 传感器

### MLX90614 电源与连接

U3 MLX90614 pin3 VDD 接 +3.3V、pin4 GND 接地，C7 22uF 与 C8 100nF 跨接传感器电源；D6 RLSD52A031V 从 +3.3V 接 GND。

- 参数与网络：`vdd=pin3 +3.3V`；`ground=pin4 GND`；`decoupling=C7 22uF,C8 100nF`；`protection=D6 RLSD52A031V`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 D2-D3 U3/C7/C8/D6

## 调试与烧录

### P2 SWD 调试接口

P2 pin1=+3.3V、pin2=SWCLK、pin3=SWDIO、pin4=NRST、pin5=GND；C1 100nF 跨接 +3.3V 与 GND。

- 参数与网络：`pin1=+3.3V`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=NRST`；`pin5=GND`；`cap=C1 100nF`
- 证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页网格 A4 P2 SWD_5p 与 C1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NCIR2 系统结构 | `controller=U2 STM32F030F4P6`；`sensor=U3 MLX90614`；`internal_bus=SCL1/SDA1`；`host_bus=SCL/SDA`；`rgb=LED1 SK6812`；`button=key1`；`buzzer=BEEP -> Q1/LS1`；`power=+5V -> U1 SY8089 -> +3.3V` |
| 电源 | +5V 至 +3.3V | `input=+5V`；`converter=U1 SY8089`；`enable=pin1 tied +5V`；`inductor=L1 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ,R2 15KΩ`；`input_caps=C4 22uF,C5 100nF`；`output_caps=C2 100nF,C3 22uF` |
| 接口 | J2 Grove I2C | `pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND`；`pullups=R5/R6 4.7KΩ to +3.3V` |
| 总线 | STM32 外部 I2C | `controller=U2 STM32F030F4P6`；`sda=PA10 pin18 SDA`；`scl=PA9 pin17 SCL`；`connector=J2`；`sensor_directly_shared=false` |
| 总线 | STM32 至 MLX90614 I2C | `controller_scl=U2 PA3 pin9 SCL1`；`controller_sda=U2 PA4 pin10 SDA1`；`sensor_scl=U3 pin1`；`sensor_sda=U3 pin2`；`pullups=R8/R10 4.7KΩ` |
| 传感器 | MLX90614 电源与连接 | `vdd=pin3 +3.3V`；`ground=pin4 GND`；`decoupling=C7 22uF,C8 100nF`；`protection=D6 RLSD52A031V` |
| GPIO 与控制信号 | STM32 主要 GPIO 映射 | `pa0=pin6 SK6812`；`pa1=pin7 key1`；`pa3=pin9 SCL1`；`pa4=pin10 SDA1`；`pb1=pin14 BEEP`；`pa9=pin17 SCL`；`pa10=pin18 SDA`；`pa13=pin19 SWDIO`；`pa14=pin20 SWCLK` |
| 复位 | NRST 复位网络 | `mcu=U2 pin4 NRST`；`pullup=R3 10KΩ`；`cap=C6 100nF`；`button=S1 to GND`；`esd=D2`；`debug=P2 pin4` |
| 调试与烧录 | P2 SWD 调试接口 | `pin1=+3.3V`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=NRST`；`pin5=GND`；`cap=C1 100nF` |
| 复位 | BOOT0 配置 | `boot0=U2 pin1`；`pulldown=R7 10KΩ to GND`；`button=null`；`jumper=null` |
| 时钟 | STM32 时钟引脚 | `osc_in=PF0 pin2 OUT3`；`osc_out=PF1 pin3 OUT4`；`external_crystal=false`；`frequency=null` |
| GPIO 与控制信号 | key1 功能按键 | `mcu_pin=U2 PA1 pin7`；`net=key1`；`pullup=R4 10KΩ`；`button=S2 to GND`；`esd=D1` |
| GPIO 与控制信号 | SK6812 RGB 指示灯 | `control=U2 PA0 pin6`；`din=LED1 pin3`；`vdd=pin4 +3.3V`；`vss=pin2 GND`；`dout=pin1 NC`；`pullup=R12 4.7KΩ`；`cap=C14 100nF` |
| 音频 | 蜂鸣器驱动 | `control=U2 PB1 pin14 BEEP`；`base_resistor=R11 1KΩ`；`base_pulldown=R13 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`load=+3.3V -> R9 10Ω -> LS1 -> Q1 -> GND`；`diode=D7 1N4007WS` |
| 保护电路 | Grove 与控制节点保护 | `scl=D4 RLSD52A031V`；`sda=D5 RLSD52A031V`；`vcc5=D3 LESD3Z5.0CMT1G`；`key=D1`；`reset=D2`；`sensor_3v3=D6`；`fuse=null`；`reverse_protection=null` |
| 电源 | MCU 3.3V 供电与去耦 | `vdda=U2 pin5 +3.3V`；`vdd=U2 pin16 +3.3V`；`vss=U2 pin15 GND`；`caps=C10 22uF,C11 100nF` |
| 内存与 Flash | 存储器 | `external_flash=null`；`external_eeprom=null`；`external_ram=null`；`storage_card=null`；`internal_flash_capacity=null`；`internal_ram_capacity=null` |
| 总线地址 | 外部 I2C 地址 0x5A | `documented_unit_address=0x5A`；`host_device=U2 STM32F030F4P6 firmware`；`sensor_bus=SCL1/SDA1`；`schematic_address=null`；`address_straps=null` |
| 核心器件 | MLX90614ESF-BAA 完整型号 | `documented_part=MLX90614ESF-BAA`；`schematic_part=MLX90614`；`suffix_confirmed=false` |
| 传感器 | 红外测温范围与精度 | `documented_object_range=-70C to 380C`；`documented_sensor_range=-40C to 125C`；`documented_unit_range=0C to 40C`；`documented_accuracy=+/-0.5C`；`fov=null`；`response_time=null`；`emissivity=null`；`calibration=null` |
| 其他事实 | 高低温告警与独立运行 | `documented_alarm=high/low temperature`；`documented_modes=host-connected and standalone`；`threshold_storage=null`；`alarm_truth_table=null`；`power_on_defaults=null`；`firmware_version=null` |

## 待确认事项

- `address.documented-0x5a`：正文称 Unit NCIR2 的 I2C 地址为 0x5A；原理图显示 Grove SCL/SDA 进入 STM32，而 MLX90614 位于独立 SCL1/SDA1 总线，图中没有任何十六进制地址、地址绑带或固件地址表。（证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页两组独立 I2C，总图无 0x5A）
- `component.documented-sensor-suffix`：正文规格表称传感器为 MLX90614ESF-BAA；原理图 U3 只打印 MLX90614，没有封装/温区/光学后缀。（证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U3 仅标 MLX90614）
- `sensor.documented-performance`：正文列出对象温度 -70°C~380°C、传感器工作温度 -40°C~125°C、Unit 工作温度 0°C~40°C、精度 ±0.5°C；原理图只确认 MLX90614 型号与电气连接，没有量程、精度、视场角、响应时间、发射率或校准条件。（证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U3 MLX90614，整页无性能参数）
- `other.documented-alarm-standalone`：正文称 MCU 数据处理可实现高/低温告警，并可与主机或单独使用；原理图确认 MCU、按键、RGB 与蜂鸣器硬件，但没有寄存器协议、阈值存储、告警真值表、上电默认值或离线固件流程。（证据：图 1eadfd123eb9 / 第 1 页 / 第 1 页 U2/U3/key1/LED1/LS1，无固件协议）
- `review.i2c-address`：请用当前 STM32 内置固件或上电扫描确认 Grove 侧 7 位地址 0x5A，并区分其与内部 MLX90614 地址。；原因：原理图不含地址文字，且主机与传感器位于两组不同 I2C。
- `review.sensor-part`：请用 U150 当前 BOM/丝印确认传感器完整料号是否为 MLX90614ESF-BAA。；原因：原理图省略 ESF-BAA 后缀。
- `review.sensor-performance`：请用当前传感器 datasheet 与整机校准测试确认温度范围、±0.5°C 条件、视场角、响应时间、发射率和环境边界。；原因：板级图不能证明定量测温性能。
- `review.alarm-firmware`：请用内置固件协议确认高低温阈值、保存方式、RGB/蜂鸣器告警语义、按键操作和独立运行流程。；原因：硬件图只确认执行器与输入，未描述固件行为。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1eadfd123eb931de64ab11a5a30685216be6e2881429ab8774d34936b8b1a294` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/604/Sch_UNIT-NCIR2_sch_01.png` |

---

源文档：`zh_CN/unit/NCIR2.md`

源文档 SHA-256：`1af15fa497e390e4e7552f8ed1618176e004c43b592898fab16f9ce3d36b05a5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
