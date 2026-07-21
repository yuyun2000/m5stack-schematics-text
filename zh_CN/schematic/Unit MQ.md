# Unit MQ 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit MQ |
| SKU | U199 |
| 产品 ID | `unit-mq-2a13ac26d1ac` |
| 源文档 | `zh_CN/unit/Unit_MQ.md` |

## 概述

Unit MQ 以 U2 STM32G030F6P6 为主控，通过 J1 Grove 的 I2C_SCL/I2C_SDA 与外部主机通信，并通过 P1 提供 SWD 调试。+5V 经 U3 XC6228D332VR-G 生成 3V3；J2 六针 MQ 接口的加热端由 PA7/TIM3_CH2 经 Q1 AO3400 低侧控制，敏感电阻端经 R10、D2/D3、R1/R8、U4 LMV321 和 R11/C7 调理后形成 STM_AD。R18 KNTC0603/10KF3950 与 R14 构成 NTC_AD 温度采样，D1 为 LED_OUT 状态灯，L1 将 GND 与 AGND 通过 120R@100MHz 磁珠连接。J3/J4 形成 MQ 系列传感器插座适配结构；原理图未直接标传感器具体型号、气体性能或 I2C 数字地址。

## 检索关键词

`Unit MQ`、`U199`、`STM32G030F6P6`、`XC6228D332VR-G`、`LMV321M5/NOPB`、`AO3400`、`MQ sensor socket`、`MQ-5`、`GROVE`、`I2C`、`0x11`、`I2C_SCL`、`I2C_SDA`、`SLAVE_A`、`SLAVE_B`、`PWM_Ctrl`、`TIM3_CH2`、`STM_AD`、`ADC1_IN4`、`NTC_AD`、`ADC1_IN1`、`KNTC0603/10KF3950`、`+5`、`3V3`、`AGND`、`GND`、`SWDIO`、`SWCLK`、`RST`、`LED_OUT`、`TP1`、`TP2`、`TP3`、`TP4`、`J2 2x3`、`J3 MQ`、`D2`、`D3`、`R10 1KΩ`、`L1 120R@100MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32G030F6P6 | 主控 MCU，处理 Grove I2C、MQ 模拟采样、NTC 采样、加热 PWM、状态 LED 和 SWD | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C2-D3，U2 STM32G030F6P6 pin1-pin20 |
| U3 | XC6228D332VR-G | 将 +5V 转换为 3V3 的稳压器 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B1-C1，U3 XC6228D332VR-G、C2-C5 |
| U4 | LMV321M5/NOPB | 传感器模拟信号的电压跟随缓冲运放，输出 STM_AD | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A3-B3，U4 LMV321M5/NOPB 与 R1/R8/R11/C7 |
| Q1 | AO3400 | PWM_Ctrl 驱动的 MQ 加热器低侧 MOSFET | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B2-C2，Q1 AO3400、R2/R12/R13 与 PWM_Ctrl |
| J1 | GROVE | 四针外部接口，提供 SCL/SDA、+5V 和 GND | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B1，J1 GROVE pin1 SCL、pin2 SDA、pin3 +5V、pin4 GND |
| P1 | SWD_5p | 五针 MCU 调试接口，提供 3V3、SWCLK、SWDIO、RST、GND | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B1，P1 SWD_5p pin1-pin5 |
| J2 | 2*3P 2.54贴片排针 | 主板 MQ 六针接口，连接 A0/A1、B0/B1 与两端 H 加热器 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A2-B2，J2 A0/H/A1/B0/H/B1 |
| J3,J4 | MQ系列传感器插座 / 2*3p 2.54排母 | MQ 传感器与六针排母之间的插座适配结构 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B4-C4，J3 MQ系列传感器插座与 J4 2*3p 2.54排母 |
| D2,D3 | 1N4148WS | STM_AD 原始传感器节点至 3V3/AGND 的上下钳位二极管 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A3-B3，TP3 节点的 D2/D3 1N4148WS |
| R18 | KNTC0603/10KF3950 | 与 R14 2KΩ组成 NTC_AD 温度分压的 10K B3950 热敏电阻 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C1-D2，R18 KNTC0603/10KF3950、R14 与 NTC_AD |
| D1 | GREEN 0603 | 由 LED_OUT 驱动的绿色状态 LED，串联 R5 2KΩ | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C1-D1，LED_OUT、R5 2KΩ、D1 GREEN 0603 |
| L1 | 120R@100Mhz | 连接数字 GND 与模拟 AGND 的磁珠/阻抗器件 | 图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C2-C3，GND 与 AGND 之间的 L1 120R@100Mhz |

## 系统结构

### Unit MQ 系统架构

U2 STM32G030F6P6 通过 J1 I2C 对外通信，通过 PA7/PWM_Ctrl 控制 Q1 加热开关，通过 PA4/STM_AD 与 PA5/NTC_AD 采集气敏和温度信号，并通过 P1 SWD 调试。+5V 为 MQ 传感器、加热器和 U4 供电，U3 生成 MCU 使用的 3V3。

- 参数与网络：`controller=U2 STM32G030F6P6`；`host=J1 I2C`；`gas_adc=PA4 STM_AD`；`temperature_adc=PA5 NTC_AD`；`heater=PA7 PWM_Ctrl -> Q1`；`power=+5V -> U3 -> 3V3`；`debug=P1 SWD`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 独立存储、射频、音频与外部时钟

唯一原理图页面未画独立存储器、协处理器、射频、音频、USB、UART、CAN、RS-485 或外部晶振；PC15-OSC32 OUT pin3 未连接，复用 PC14-OSC32 IN 的 pin2 用作 I2C_SDA。

- 参数与网络：`storage=null`；`coprocessor=null`；`rf=null`；`audio=null`；`usb=null`；`uart=null`；`can=null`；`rs485=null`；`external_crystal=null`；`pc14_use=I2C_SDA`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页完整原理图，U2 pin2/pin3 与唯一页面

## 电源

### +5V 至 3V3 稳压

+5V 同时连接 U3 XC6228D332VR-G IN pin1 与 EN pin3，OUT pin5 输出 3V3，GND pin2 接地，NC pin4 未连接；C2 4.7uF/C3 100nF 位于输入端，C4 100nF/C5 4.7uF 位于输出端。

- 参数与网络：`input=+5V`；`regulator=U3 XC6228D332VR-G`；`enable=EN pin3 tied to +5V`；`output=3V3`；`ground=pin2 GND`；`caps=C2 4.7uF,C3 100nF,C4 100nF,C5 4.7uF`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B1-C1，U3/C2-C5 与 +5/3V3

### STM32 3V3 供电

U2 VDD/VDDA pin4 接 3V3，VSS/VSSA pin5 接 GND；C8 10uF 与 C1 100nF 从 3V3 接 GND。数字 GND 通过 L1 120R@100Mhz 与模拟 AGND 连接。

- 参数与网络：`device=U2 STM32G030F6P6`；`supply=VDD/VDDA pin4 3V3`；`ground=VSS/VSSA pin5 GND`；`decoupling=C8 10uF,C1 100nF`；`analog_ground_link=L1 120R@100Mhz GND-AGND`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C2-D3，U2/C8/C1 与网格 C2-C3 L1

## 接口

### J1 Grove I2C 接口

J1 pin1=SCL/SLAVE_B、pin2=SDA/SLAVE_A、pin3=+5V、pin4=GND；SCL/SDA 为双向 I2C，+5V 为板上电源输入。R9/R7 各 0Ω分别连接 SLAVE_B/SLAVE_A 至 I2C_SCL/I2C_SDA。

- 参数与网络：`connector=J1 GROVE`；`pin1=SCL SLAVE_B`；`pin2=SDA SLAVE_A`；`pin3=+5V input`；`pin4=GND`；`links=R9 0Ω SCL,R7 0Ω SDA`；`direction=I2C bidirectional`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A1-B1，J1、R7/R9、SLAVE_A/SLAVE_B、I2C_SDA/I2C_SCL

### J2 MQ 六针主板接口

J2 以 A0 pin1、H pin2、A1 pin3、B1 pin4、H pin5、B0 pin6 标识。A0/A1 与一端 H 接 +5V，B0/B1 并接传感器模拟节点，另一端 H 经 R2 10Ω与 Q1 接 AGND。

- 参数与网络：`connector=J2 2*3P 2.54`；`pin1=A0 +5V`；`pin2=H +5V`；`pin3=A1 +5V`；`pin4=B1 sensor node`；`pin5=H via R2/Q1`；`pin6=B0 sensor node`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A2-B2，J2 pins1-6 与 +5、R2、TP3/R10 节点

### J3/J4 MQ 传感器插座适配

J3 标为 MQ系列传感器插座，六脚为 A0/H/A1/B0/H/B1；J4 为 2*3p 2.54排母，J3 六脚通过板上走线连接 J4 六脚，未包含额外有源器件。

- 参数与网络：`sensor_socket=J3 A0/H/A1/B0/H/B1`；`board_header=J4 2*3p 2.54 female`；`active_components=null`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B4-C4，J3/J4 六脚连接

## 总线

### STM32 Grove I2C 总线

I2C_SCL 连接 U2 pin1（符号标 PB7/PB8），I2C_SDA 连接 U2 pin2（符号标 PB9/PC14-OSC32 IN）；R16/R17 各 4.7KΩ将 SCL/SDA 上拉到 3V3。

- 参数与网络：`controller=U2 STM32G030F6P6`；`scl=U2 pin1 PB7/PB8 -> I2C_SCL`；`sda=U2 pin2 PB9/PC14-OSC32 IN -> I2C_SDA`；`pullups=R16/R17 4.7KΩ to 3V3`；`logic_level=3V3`；`connector=J1`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C2-D2，U2 pins1/2、R16/R17 与 I2C_SCL/I2C_SDA

## GPIO 与控制信号

### MQ 加热器 PWM 控制

U2 PA7 pin14/TIM3_CH2 输出 PWM_Ctrl，经 R12 10Ω连接 Q1 AO3400 栅极；R13 4.7KΩ将栅极下拉至 AGND。Q1 源极接 AGND，漏极经 R2 10Ω连接 J2 H pin5，另一 H pin2 接 +5V。

- 参数与网络：`mcu=U2 PA7 pin14 TIM3_CH2`；`network=PWM_Ctrl`；`gate_resistor=R12 10Ω`；`gate_pulldown=R13 4.7KΩ`；`mosfet=Q1 AO3400`；`heater_path=+5V -> J2 H -> heater -> J2 H -> R2 10Ω -> Q1 -> AGND`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B2-C3，U2 PA7/PWM_Ctrl、R12/R13、Q1、R2 与 J2 H

### LED_OUT 状态灯

U2 pin15（符号复用标注 PB0/PB1/PB2/PA8）输出 LED_OUT，LED_OUT 经 R5 2KΩ与 D1 GREEN 0603 串联至 GND，因此 LED 为高电平点亮路径。

- 参数与网络：`mcu_pin=U2 pin15 PB0/PB1/PB2/PA8`；`network=LED_OUT`；`resistor=R5 2KΩ`；`led=D1 GREEN 0603`；`active_level=high`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C1-D2，U2 pin15/LED_OUT、R5、D1

## 复位

### STM32 RST 网络

U2 RST pin6 接 RST；R6 10KΩ将 RST 上拉到 3V3，C6 1uF 将 RST 接 GND，TP4 位于 RST 节点；P1 pin4 同时引出 RST。

- 参数与网络：`mcu_pin=U2 RST pin6`；`pullup=R6 10KΩ to 3V3`；`capacitor=C6 1uF to GND`；`test_point=TP4`；`debug_header=P1 pin4`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C1-D2，R6/C6/TP4/RST、U2 pin6 与 P1

## 保护电路

### 模拟输入保护与地隔离

D2/D3 对原始气敏节点提供 3V3/AGND 钳位，R1/R11 分别提供 1KΩ与 100Ω串联限流/隔离，C7 100nF 对 STM_AD 滤波，L1 将 GND 与 AGND 通过 120R@100Mhz 连接。图中未画 Grove 输入保险丝、ESD 或反接保护。

- 参数与网络：`clamps=D2/D3 1N4148WS`；`input_series=R1 1KΩ/0.1%`；`adc_series=R11 100Ω`；`adc_cap=C7 100nF`；`ground_bead=L1 120R@100Mhz`；`fuse=null`；`esd=null`；`reverse_protection=null`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页 D2/D3/R1/U4/R11/C7/L1 与 J1 +5V 输入路径

## 传感器

### 板载 NTC 温度采样

R18 KNTC0603/10KF3950 从 3V3 接 NTC_AD，R14 2KΩ从 NTC_AD 接 AGND，构成热敏电阻分压；NTC_AD 连接 U2 PA5 pin12/ADC1_IN1。

- 参数与网络：`thermistor=R18 KNTC0603/10KF3950`；`top=3V3`；`bottom=R14 2KΩ to AGND`；`network=NTC_AD`；`mcu_adc=U2 PA5 pin12 ADC1_IN1`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 C1-D2，R18/R14/NTC_AD 与 U2 PA5

## 调试与烧录

### P1 SWD 调试接口

P1 pin1=3V3 VCC、pin2=SWCLK、pin3=SWDIO、pin4=RST、pin5=GND。U2 PA13 pin18 经 R3 27Ω连接 SWDIO，PA14-BOOT0 pin19 经 R4 27Ω连接 SWCLK。

- 参数与网络：`connector=P1 SWD_5p`；`pin1=3V3`；`pin2=SWCLK via R4 27Ω to U2 pin19 PA14-BOOT0`；`pin3=SWDIO via R3 27Ω to U2 pin18 PA13`；`pin4=RST`；`pin5=GND`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 B1 P1 与网格 C3-D4 U2 PA13/PA14、R3/R4

## 模拟电路

### MQ 原始传感器节点与钳位

J2 B0/B1 并接原始传感器节点，R10 1KΩ/0.1% 将该节点接 AGND；TP3 位于此节点，D2 1N4148WS 将节点钳位到 3V3，D3 1N4148WS 将节点钳位到 AGND。

- 参数与网络：`sensor_electrodes=J2 B0/B1`；`load=R10 1KΩ/0.1% to AGND`；`test_point=TP3`；`upper_clamp=D2 1N4148WS to 3V3`；`lower_clamp=D3 1N4148WS to AGND`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A2-B3，J2 B0/B1、R10、TP3、D2/D3

### MQ 模拟分压与运放缓冲

TP3 原始节点经 R1 1KΩ/0.1% 接 U4 同相输入 pin1，R8 1KΩ/0.1% 从同相输入接 AGND；U4 输出 pin4 回接反相输入 pin3形成电压跟随器。U4 V+ pin5 接 +5V，V- pin2 接 AGND。

- 参数与网络：`series=R1 1KΩ/0.1%`；`shunt=R8 1KΩ/0.1% to AGND`；`op_amp=U4 LMV321M5/NOPB`；`configuration=voltage follower, output pin4 to inverting pin3`；`supply=+5V/AGND`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A3-B3，R1/R8 与 U4 pins1-5

### STM_AD 输出滤波与 ADC 映射

U4 输出经 R11 100Ω形成 STM_AD，C7 100nF 从 STM_AD 接 AGND，TP2 位于 STM_AD；该网络连接 U2 PA4 pin11/ADC1_IN4。

- 参数与网络：`source=U4 output pin4`；`series=R11 100Ω`；`network=STM_AD`；`capacitor=C7 100nF to AGND`；`test_point=TP2`；`mcu_adc=U2 PA4 pin11 ADC1_IN4`
- 证据：图 1bf5734172b2 / 第 1 页 / 第 1 页网格 A3-B4 的 U4/R11/C7/TP2 与网格 C3-D3 U2 PA4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit MQ 系统架构 | `controller=U2 STM32G030F6P6`；`host=J1 I2C`；`gas_adc=PA4 STM_AD`；`temperature_adc=PA5 NTC_AD`；`heater=PA7 PWM_Ctrl -> Q1`；`power=+5V -> U3 -> 3V3`；`debug=P1 SWD` |
| 系统结构 | 独立存储、射频、音频与外部时钟 | `storage=null`；`coprocessor=null`；`rf=null`；`audio=null`；`usb=null`；`uart=null`；`can=null`；`rs485=null`；`external_crystal=null`；`pc14_use=I2C_SDA` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 GROVE`；`pin1=SCL SLAVE_B`；`pin2=SDA SLAVE_A`；`pin3=+5V input`；`pin4=GND`；`links=R9 0Ω SCL,R7 0Ω SDA`；`direction=I2C bidirectional` |
| 总线 | STM32 Grove I2C 总线 | `controller=U2 STM32G030F6P6`；`scl=U2 pin1 PB7/PB8 -> I2C_SCL`；`sda=U2 pin2 PB9/PC14-OSC32 IN -> I2C_SDA`；`pullups=R16/R17 4.7KΩ to 3V3`；`logic_level=3V3`；`connector=J1` |
| 电源 | +5V 至 3V3 稳压 | `input=+5V`；`regulator=U3 XC6228D332VR-G`；`enable=EN pin3 tied to +5V`；`output=3V3`；`ground=pin2 GND`；`caps=C2 4.7uF,C3 100nF,C4 100nF,C5 4.7uF` |
| 电源 | STM32 3V3 供电 | `device=U2 STM32G030F6P6`；`supply=VDD/VDDA pin4 3V3`；`ground=VSS/VSSA pin5 GND`；`decoupling=C8 10uF,C1 100nF`；`analog_ground_link=L1 120R@100Mhz GND-AGND` |
| 接口 | J2 MQ 六针主板接口 | `connector=J2 2*3P 2.54`；`pin1=A0 +5V`；`pin2=H +5V`；`pin3=A1 +5V`；`pin4=B1 sensor node`；`pin5=H via R2/Q1`；`pin6=B0 sensor node` |
| 接口 | J3/J4 MQ 传感器插座适配 | `sensor_socket=J3 A0/H/A1/B0/H/B1`；`board_header=J4 2*3p 2.54 female`；`active_components=null` |
| GPIO 与控制信号 | MQ 加热器 PWM 控制 | `mcu=U2 PA7 pin14 TIM3_CH2`；`network=PWM_Ctrl`；`gate_resistor=R12 10Ω`；`gate_pulldown=R13 4.7KΩ`；`mosfet=Q1 AO3400`；`heater_path=+5V -> J2 H -> heater -> J2 H -> R2 10Ω -> Q1 -> AGND` |
| 模拟电路 | MQ 原始传感器节点与钳位 | `sensor_electrodes=J2 B0/B1`；`load=R10 1KΩ/0.1% to AGND`；`test_point=TP3`；`upper_clamp=D2 1N4148WS to 3V3`；`lower_clamp=D3 1N4148WS to AGND` |
| 模拟电路 | MQ 模拟分压与运放缓冲 | `series=R1 1KΩ/0.1%`；`shunt=R8 1KΩ/0.1% to AGND`；`op_amp=U4 LMV321M5/NOPB`；`configuration=voltage follower, output pin4 to inverting pin3`；`supply=+5V/AGND` |
| 模拟电路 | STM_AD 输出滤波与 ADC 映射 | `source=U4 output pin4`；`series=R11 100Ω`；`network=STM_AD`；`capacitor=C7 100nF to AGND`；`test_point=TP2`；`mcu_adc=U2 PA4 pin11 ADC1_IN4` |
| 传感器 | 板载 NTC 温度采样 | `thermistor=R18 KNTC0603/10KF3950`；`top=3V3`；`bottom=R14 2KΩ to AGND`；`network=NTC_AD`；`mcu_adc=U2 PA5 pin12 ADC1_IN1` |
| GPIO 与控制信号 | LED_OUT 状态灯 | `mcu_pin=U2 pin15 PB0/PB1/PB2/PA8`；`network=LED_OUT`；`resistor=R5 2KΩ`；`led=D1 GREEN 0603`；`active_level=high` |
| 复位 | STM32 RST 网络 | `mcu_pin=U2 RST pin6`；`pullup=R6 10KΩ to 3V3`；`capacitor=C6 1uF to GND`；`test_point=TP4`；`debug_header=P1 pin4` |
| 调试与烧录 | P1 SWD 调试接口 | `connector=P1 SWD_5p`；`pin1=3V3`；`pin2=SWCLK via R4 27Ω to U2 pin19 PA14-BOOT0`；`pin3=SWDIO via R3 27Ω to U2 pin18 PA13`；`pin4=RST`；`pin5=GND` |
| 保护电路 | 模拟输入保护与地隔离 | `clamps=D2/D3 1N4148WS`；`input_series=R1 1KΩ/0.1%`；`adc_series=R11 100Ω`；`adc_cap=C7 100nF`；`ground_bead=L1 120R@100Mhz`；`fuse=null`；`esd=null`；`reverse_protection=null` |
| 总线地址 | Unit MQ I2C 地址 | `documented_default=0x11`；`documented_configurable=true`；`controller=U2 STM32G030F6P6`；`hardware_strap=null`；`schematic_address=null` |
| 传感器 | MQ-5 型号与气体检测性能 | `documented_sensor=MQ-5`；`documented_gases=LPG,methane`；`documented_range=300~10000ppm`；`schematic_socket=J3 MQ series`；`sensitivity=null`；`calibration=null` |
| 模拟电路 | ADC 输出分辨率与电压换算 | `documented_raw=12-bit and 8-bit`；`gas_adc=PA4 ADC1_IN4`；`ntc_adc=PA5 ADC1_IN1`；`reference=null`；`sample_time=null`；`accuracy=null`；`conversion_formula=null` |
| 电源 | 工作电流与加热模式 | `documented_off=5.02V@6.88mA`；`documented_continuous=5.05V@188.89mA`；`documented_preheat=20s`；`control=PA7 TIM3_CH2 PWM_Ctrl`；`heater_path=J2 H/Q1`；`pwm_period=null`；`duty_cycle=null`；`thermal_limit=null` |

## 待确认事项

- `address.documented-i2c`：产品正文给出默认 I2C 地址 0x11 且地址可设置；原理图只确认 J1 至 U2 的 SCL/SDA 连接，没有 0x11 地址文字、硬件地址拨码或地址选择引脚。（证据：图 1bf5734172b2 / 第 1 页 / 第 1 页 J1/R7/R9/I2C_SCL/I2C_SDA 与 U2，图中无数字地址）
- `sensor.documented-mq5`：产品正文称标配 MQ-5，可检测液化气/甲烷，范围 300~10000ppm，并兼容多种 MQ 传感器；原理图只标 J3 为 MQ系列传感器插座，没有具体传感器型号、气体类型、浓度范围、灵敏度或校准曲线。（证据：图 1bf5734172b2 / 第 1 页 / 第 1 页 J3 仅标 MQ系列传感器插座）
- `analog.documented-adc`：产品正文称可读取参考电压、传感器电压以及 12 位和 8 位 ADC 原始值；原理图确认 STM_AD/NTC_AD 分别进入 ADC1_IN4/ADC1_IN1，但没有 ADC 分辨率、参考源、采样时间、量程、精度或固件换算公式。（证据：图 1bf5734172b2 / 第 1 页 / 第 1 页 U2 PA4/PA5 与 STM_AD/NTC_AD，图中无 ADC 性能参数）
- `power.documented-heater-modes`：产品正文称支持关闭、连续加热和可设周期的间歇加热，并列出约 5V@6.88mA 与 5V@188.89mA 工作点和 20s 推荐预热；原理图只确认 PA7/TIM3_CH2、Q1 与加热器电源路径，没有电流、PWM 周期、占空比、预热时间或热安全边界。（证据：图 1bf5734172b2 / 第 1 页 / 第 1 页 J2 H、R2/Q1、PWM_Ctrl 与 U2 PA7，图中无模式参数）
- `review.i2c-address`：请通过当前固件协议或总线扫描确认默认地址 0x11 及可配置地址范围、持久化方式和冲突处理。；原因：原理图没有硬件地址选择或数字地址。
- `review.mq-sensor`：请用量产 BOM、传感器标签与 datasheet 确认标配 MQ-5、兼容型号、300~10000ppm 范围及校准要求。；原因：原理图只显示通用 MQ 插座。
- `review.adc-spec`：请依据 STM32 配置和固件协议确认 12/8 位 ADC 数据、参考电压来源、采样参数及电压换算公式。；原因：原理图只显示 ADC 引脚和模拟调理链。
- `review.heater-modes`：请通过固件和实测确认关闭/连续/间歇加热的电流、PWM 周期与占空比、20s 数据有效条件和热安全限制。；原因：电路仅给出加热器 MOSFET 路径，没有运行参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1bf5734172b2d1e70f85c8a16064516bafcf685ca59a7f04a9dffa4c9a84a520` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/UnitMQ_SCH_MAIN_V1.0_20250716_2025_07_16_11_13_24_page_01.png` |

---

源文档：`zh_CN/unit/Unit_MQ.md`

源文档 SHA-256：`59dc010ca92f17545c05e7171bd59dd9ea20ea38dd9677a1304dcdab38829e0d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
