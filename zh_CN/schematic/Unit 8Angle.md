# Unit 8Angle 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 8Angle |
| SKU | U154 |
| 产品 ID | `unit-8angle-e52c04131be5` |
| 源文档 | `zh_CN/unit/8Angle.md` |

## 概述

Unit 8Angle 以 STM32F030F4P6（U10）为采集与通信主控，读取 8 路电位器 ad0~ad7 和拨动开关 ad_Key，并通过 Grove 接口的 SCL/SDA 与外部主机连接。U10 的 RGB 网络驱动 9 颗 SK6812-3535 组成的串行级联链。Grove 输入的 VCC_5V 经 ME6210A33M3G（U11）稳压为 3V3，为主控、电位器、LED 和 I2C 上拉供电。板上还提供 NRST、BOOT0 管理电路和 5 针 SWD 调试接口；原理图未标注 I2C 地址。

## 检索关键词

`Unit 8Angle`、`U154`、`STM32F030F4P6`、`ME6210A33M3G`、`SK6812-3535`、`SS12D07L4B`、`GROVE 4P`、`I2C`、`SCL`、`SDA`、`PA9`、`PA10`、`ad0`、`ad1`、`ad2`、`ad3`、`ad4`、`ad5`、`ad6`、`ad7`、`ad_Key`、`RGB`、`SWD`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`BOOT0`、`VCC_5V`、`3V3`、`4.7K`、`0x43`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U10 | STM32F030F4P6 | 采集 8 路电位器与拨动开关、驱动 RGB 链并连接 I2C/SWD 的主控 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-C1：U10 STM32F030F4P6，标有 PA0~PA14、PB1、PF0/PF1、BOOT0、NRST、VDD/VDDA/VSS |
| U11 | ME6210A33M3G | 将 Grove 输入的 VCC_5V 稳压为 3V3 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 A1-A2：U11 ME6210A33M3G，Vin 接 VCC_5V、Vout 接 3V3、GND 接地 |
| J1 | GROVE 4P | 外部 5V 供电和 I2C SCL/SDA 接口 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 A1：J1 GROVE 4P，IO2=SCL、IO1=SDA、5V=VCC_5V、GND=GND |
| J2 | SWD 5P | 主控烧录与调试接口，引出 3V3、SWCLK、SWDIO、NRST 和 GND | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B2-C2：J2 SWD，1~5 脚依次接 3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND |
| R1-R8 | RPot | 8 路模拟电位器，滑动端分别输出 ad0~ad7 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 A3-A4：R1~R8 均标 RPot，1 脚接 3V3、3 脚接 GND、2 脚依次为 ad0~ad7 |
| SW1 | SS12D07L4B | 生成 ad_Key 状态的物理拨动开关 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B4：SW1 SS12D07L4B，右侧触点连接 ad_Key，底部触点连接 GND |
| U1-U9 | SK6812-3535 | 9 颗可寻址 RGB LED，按 U1 到 U9 串行级联 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 C1-D4：U1~U9 均标 SK6812-3535，DI/DO 逐级连接，VDD 接 3V3、GND 接地 |
| R12/R13 | 4.7KΩ | SCL 与 SDA 到 3V3 的 I2C 上拉电阻 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 A1：R12、R13 均标 4.7K，上端并接 3V3，下端分别进入 SCL/SDA |
| R11 | 10KΩ | ad_Key 到 3V3 的上拉电阻 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B4：R11 10K 连接 3V3 与 ad_Key |
| R9/C10 | 10KΩ / 100nF | NRST 上拉及对地复位电容 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-C2：NRST 经 R9 10K 接 3V3，并经 C10 100nF 接 GND |
| R10 | 10KΩ | BOOT0 到 GND 的下拉电阻 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-B2：U10 BOOT0 pin 1 经 R10 10K 接 GND |
| C1/C2 | 1uF/50V | U11 的 VCC_5V 输入与 3V3 输出滤波电容 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 A1-A2：C1、C2 均标 1uF/50V，分别跨接 VCC_5V/GND 与 3V3/GND |
| C11 | 100nF | U10 VDD/VDDA 的 3V3 去耦电容 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 C1：U10 VDD pin 16 与 VDDA pin 5 接 3V3，旁路 C11 100nF 到 GND |
| C3-C9/C13/C14 | 100nF | 9 颗 SK6812-3535 所在 3V3 电源轨的去耦电容组 | 图 09ccb8692112 / 第 1 页 / 页 1 网格 D3-D4：C3、C4、C5、C6、C7、C8、C9、C13、C14 均为 100nF 并联在 3V3 与 GND 之间 |

## 系统结构

### Unit 8Angle

U10 STM32F030F4P6 读取 R1~R8 的 ad0~ad7 与 SW1 的 ad_Key，通过 J1 的 SCL/SDA 通信，并由 RGB 网络驱动 U1~U9 的 SK6812-3535 级联链；U11 从 VCC_5V 生成全板 3V3。

- 参数与网络：`controller=U10 STM32F030F4P6`；`analog_inputs=R1-R8,ad0-ad7`；`switch_input=SW1,ad_Key`；`communication=J1,SCL,SDA`；`rgb_chain=U1-U9 SK6812-3535`；`power_conversion=U11 VCC_5V to 3V3`
- 证据：图 09ccb8692112 / 第 1 页 / 整页：J1/U11 电源与 I2C、U10 主控、R1~R8/SW1 输入、U1~U9 RGB 链

## 核心器件

### SW1 SS12D07L4B

SW1 的公共状态网络标为 ad_Key，R11 将该网络上拉至 3V3，开关下侧触点接 GND。

- 参数与网络：`reference=SW1`；`part_number=SS12D07L4B`；`signal=ad_Key`；`pullup=R11 10KΩ`；`rail=3V3`；`ground=GND`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B4：SW1、R11、ad_Key、3V3 与 GND 标注

## 电源

### U11 ME6210A33M3G

U11 的 Vin pin 3 接 VCC_5V，Vout pin 2 输出 3V3，GND pin 1 接地；C1/C2 各 1uF/50V 分别位于输入和输出侧。

- 参数与网络：`input_pin=pin 3 Vin`；`input_rail=VCC_5V`；`output_pin=pin 2 Vout`；`output_rail=3V3`；`ground_pin=pin 1 GND`；`input_capacitor=C1 1uF/50V`；`output_capacitor=C2 1uF/50V`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A1-A2：U11、C1、C2 与 VCC_5V/3V3/GND 网络

### SCL/SDA 上拉

R12 和 R13 均为 4.7KΩ，将 SCL 与 SDA 上拉到 3V3。

- 参数与网络：`resistors=R12,R13`；`resistance=4.7KΩ`；`signals=SCL,SDA`；`rail=3V3`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A1：3V3 至 R12/R13 4.7K，再到 SCL/SDA 的两条支路

### U1~U9 LED 供电

U1~U9 的 VDD pin 4 全部连接 3V3，GND pin 2 全部接地；C3~C9、C13、C14 九只 100nF 电容并联在 3V3 与 GND 之间。

- 参数与网络：`devices=U1-U9 SK6812-3535`；`vdd=pin 4 to 3V3`；`ground=pin 2 to GND`；`decoupling=C3,C4,C5,C6,C7,C8,C9,C13,C14; 100nF`；`rail=3V3`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 C1-D4：U1~U9 VDD/GND 引脚和下方九只 100nF 的 3V3-GND 电容组

### U10 电源

U10 VDD pin 16 和 VDDA pin 5 接 3V3，VSS pin 15 接 GND，C11 100nF 跨接 3V3 与 GND。

- 参数与网络：`vdd=pin 16 to 3V3`；`vdda=pin 5 to 3V3`；`vss=pin 15 to GND`；`decoupling=C11 100nF`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-C1：U10 VDD/VDDA/VSS 引脚、3V3/GND 与 C11 100nF

## 接口

### J1 GROVE 4P

J1 的 IO2 接 SCL，IO1 接 SDA，5V 接 VCC_5V，GND 接系统地。

- 参数与网络：`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`signal_level_reference=3V3 pull-ups on SCL/SDA`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A1：J1 端子文字 IO2/IO1/5V/GND 及 SCL/SDA/VCC_5V/GND 网络

## 总线

### U10 I2C

SCL 从 J1 连接 U10 PA9 pin 17，SDA 从 J1 连接 U10 PA10 pin 18。

- 参数与网络：`controller=U10 STM32F030F4P6`；`scl_net=SCL`；`scl_pin=PA9 pin 17`；`sda_net=SDA`；`sda_pin=PA10 pin 18`；`connector=J1 GROVE 4P`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A1 与 B1：J1 SCL/SDA 同名网络连接 U10 PA9 pin 17、PA10 pin 18

### U1~U9 RGB 串行链

数据从 RGB 进入 U1 DI，随后按 U1 DO→U2 DI、U2 DO→U3 DI，依次级联至 U9 DI；各器件 DO 为 pin 1、DI 为 pin 3。

- 参数与网络：`devices=U1,U2,U3,U4,U5,U6,U7,U8,U9`；`part_number=SK6812-3535`；`input=RGB to U1 DI pin 3`；`chain_order=U1->U2->U3->U4->U5->U6->U7->U8->U9`；`data_out_pin=pin 1 DO`；`data_in_pin=pin 3 DI`；`device_count=9`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 C1-D4：从右侧 U1 的 RGB/DI 开始，经相邻 DO-DI 连线逐级到左侧 U9

## GPIO 与控制信号

### U10 模拟输入映射

ad0~ad7 分别连接 U10 PA0 pin 6、PA1 pin 7、PA2 pin 8、PA3 pin 9、PA4 pin 10、PA5 pin 11、PA7 pin 13、PB1 pin 14。

- 参数与网络：`ad0=PA0 pin 6`；`ad1=PA1 pin 7`；`ad2=PA2 pin 8`；`ad3=PA3 pin 9`；`ad4=PA4 pin 10`；`ad5=PA5 pin 11`；`ad6=PA7 pin 13`；`ad7=PB1 pin 14`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1：U10 左侧 ad0~ad6 与 PA0~PA7，右上 ad7 与 PB1 pin 14

### ad_Key

ad_Key 连接 U10 PF0-OSC_IN(PF0) pin 2，并由 R11 10KΩ 上拉到 3V3；SW1 提供到 GND 的开关路径。

- 参数与网络：`net=ad_Key`；`mcu_pin=PF0-OSC_IN(PF0) pin 2`；`pullup=R11 10KΩ to 3V3`；`switch=SW1 SS12D07L4B`；`switch_return=GND`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1 与 B4：U10 PF0 pin 2 的 ad_Key 同名网络，以及 R11/SW1/GND 支路

### U10 RGB 输出

U10 PA6 pin 12 连接 RGB 网络，RGB 进入 U1 SK6812-3535 的 DI pin 3。

- 参数与网络：`controller_pin=PA6 pin 12`；`net=RGB`；`first_device=U1 SK6812-3535`；`first_device_pin=DI pin 3`；`direction=U10 to U1`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1 与 C4：U10 PA6 pin 12 的 RGB 网络及 U1 DI pin 3 的 RGB 网络

## 时钟

### U10 PF0/PF1 时钟引脚

U10 的 PF0-OSC_IN(PF0) pin 2 被连接为 ad_Key 输入，PF1-OSC_OUT(PF1) pin 3 在原理图中未连接，页面未绘出外部晶振或振荡器。

- 参数与网络：`osc_in=PF0 pin 2 used as ad_Key`；`osc_out=PF1 pin 3 no connection`；`external_clock_component=null`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-B2：U10 右上 PF0-OSC_IN pin 2 接 ad_Key、PF1-OSC_OUT pin 3 端点未接，整页无晶振位号

## 复位

### U10 NRST

U10 NRST pin 4 接 NRST 网络，R9 10KΩ 将其上拉至 3V3，C10 100nF 将其连接到 GND；NRST 同时引至 J2 pin 4。

- 参数与网络：`mcu_pin=NRST pin 4`；`net=NRST`；`pullup=R9 10KΩ to 3V3`；`capacitor=C10 100nF to GND`；`debug_header=J2 pin 4`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-C2：U10 NRST pin 4、R9、C10 与 J2 pin 4 的 NRST 网络

### U10 BOOT0

U10 BOOT0 pin 1 通过 R10 10KΩ 下拉到 GND。

- 参数与网络：`mcu_pin=BOOT0 pin 1`；`resistor=R10 10KΩ`；`strap=GND`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-B2：BOOT0 pin 1、R10 10K 与 GND

## 关键网络

### U10 关键网络索引

U10 的关键映射为 PA0~PA5→ad0~ad5、PA6→RGB、PA7→ad6、PB1→ad7、PF0→ad_Key、PA9→SCL、PA10→SDA、PA13→MCU_SWDIO、PA14→MCU_SWCLK。

- 参数与网络：`PA0-PA5=ad0-ad5`；`PA6=RGB`；`PA7=ad6`；`PB1=ad7`；`PF0=ad_Key`；`PA9=SCL`；`PA10=SDA`；`PA13=MCU_SWDIO`；`PA14=MCU_SWCLK`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1：U10 四周全部网络名、GPIO 名称和 pin 编号

## 调试与烧录

### J2 SWD

J2 pin 1 接 3V3，pin 2 接 MCU_SWCLK，pin 3 接 MCU_SWDIO，pin 4 接 NRST，pin 5 接 GND；U10 的 PA14 pin 20 和 PA13 pin 19 分别连接 MCU_SWCLK 与 MCU_SWDIO。

- 参数与网络：`pin_1=3V3`；`pin_2=MCU_SWCLK; U10 PA14 pin 20`；`pin_3=MCU_SWDIO; U10 PA13 pin 19`；`pin_4=NRST; U10 pin 4`；`pin_5=GND`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 B1-C2：U10 PA13/PA14 与 J2 1~5 脚的同名 SWD/NRST/电源网络

## 模拟电路

### R1~R8 电位器阵列

R1~R8 的 pin 1 均接 3V3、pin 3 均接 GND，pin 2 滑动端依次输出 ad0、ad1、ad2、ad3、ad4、ad5、ad6、ad7。

- 参数与网络：`references=R1,R2,R3,R4,R5,R6,R7,R8`；`part=RPot`；`high_terminal=pin 1 to 3V3`；`wiper=pin 2 to ad0-ad7`；`low_terminal=pin 3 to GND`；`channels=8`
- 证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A3-A4：R1~R8 的 1/2/3 脚、3V3/GND 端点及 ad0~ad7 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit 8Angle | `controller=U10 STM32F030F4P6`；`analog_inputs=R1-R8,ad0-ad7`；`switch_input=SW1,ad_Key`；`communication=J1,SCL,SDA`；`rgb_chain=U1-U9 SK6812-3535`；`power_conversion=U11 VCC_5V to 3V3` |
| 电源 | U11 ME6210A33M3G | `input_pin=pin 3 Vin`；`input_rail=VCC_5V`；`output_pin=pin 2 Vout`；`output_rail=3V3`；`ground_pin=pin 1 GND`；`input_capacitor=C1 1uF/50V`；`output_capacitor=C2 1uF/50V` |
| 接口 | J1 GROVE 4P | `io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`signal_level_reference=3V3 pull-ups on SCL/SDA` |
| 总线 | U10 I2C | `controller=U10 STM32F030F4P6`；`scl_net=SCL`；`scl_pin=PA9 pin 17`；`sda_net=SDA`；`sda_pin=PA10 pin 18`；`connector=J1 GROVE 4P` |
| 电源 | SCL/SDA 上拉 | `resistors=R12,R13`；`resistance=4.7KΩ`；`signals=SCL,SDA`；`rail=3V3` |
| 总线地址 | Unit 8Angle I2C 地址 | `bus=I2C`；`schematic_address=null`；`controller=U10 STM32F030F4P6`；`address_source_needed=firmware or protocol documentation` |
| 模拟电路 | R1~R8 电位器阵列 | `references=R1,R2,R3,R4,R5,R6,R7,R8`；`part=RPot`；`high_terminal=pin 1 to 3V3`；`wiper=pin 2 to ad0-ad7`；`low_terminal=pin 3 to GND`；`channels=8` |
| GPIO 与控制信号 | U10 模拟输入映射 | `ad0=PA0 pin 6`；`ad1=PA1 pin 7`；`ad2=PA2 pin 8`；`ad3=PA3 pin 9`；`ad4=PA4 pin 10`；`ad5=PA5 pin 11`；`ad6=PA7 pin 13`；`ad7=PB1 pin 14` |
| GPIO 与控制信号 | ad_Key | `net=ad_Key`；`mcu_pin=PF0-OSC_IN(PF0) pin 2`；`pullup=R11 10KΩ to 3V3`；`switch=SW1 SS12D07L4B`；`switch_return=GND` |
| 核心器件 | SW1 SS12D07L4B | `reference=SW1`；`part_number=SS12D07L4B`；`signal=ad_Key`；`pullup=R11 10KΩ`；`rail=3V3`；`ground=GND` |
| GPIO 与控制信号 | U10 RGB 输出 | `controller_pin=PA6 pin 12`；`net=RGB`；`first_device=U1 SK6812-3535`；`first_device_pin=DI pin 3`；`direction=U10 to U1` |
| 总线 | U1~U9 RGB 串行链 | `devices=U1,U2,U3,U4,U5,U6,U7,U8,U9`；`part_number=SK6812-3535`；`input=RGB to U1 DI pin 3`；`chain_order=U1->U2->U3->U4->U5->U6->U7->U8->U9`；`data_out_pin=pin 1 DO`；`data_in_pin=pin 3 DI`；`device_count=9` |
| 电源 | U1~U9 LED 供电 | `devices=U1-U9 SK6812-3535`；`vdd=pin 4 to 3V3`；`ground=pin 2 to GND`；`decoupling=C3,C4,C5,C6,C7,C8,C9,C13,C14; 100nF`；`rail=3V3` |
| 复位 | U10 NRST | `mcu_pin=NRST pin 4`；`net=NRST`；`pullup=R9 10KΩ to 3V3`；`capacitor=C10 100nF to GND`；`debug_header=J2 pin 4` |
| 复位 | U10 BOOT0 | `mcu_pin=BOOT0 pin 1`；`resistor=R10 10KΩ`；`strap=GND` |
| 调试与烧录 | J2 SWD | `pin_1=3V3`；`pin_2=MCU_SWCLK; U10 PA14 pin 20`；`pin_3=MCU_SWDIO; U10 PA13 pin 19`；`pin_4=NRST; U10 pin 4`；`pin_5=GND` |
| 时钟 | U10 PF0/PF1 时钟引脚 | `osc_in=PF0 pin 2 used as ad_Key`；`osc_out=PF1 pin 3 no connection`；`external_clock_component=null` |
| 电源 | U10 电源 | `vdd=pin 16 to 3V3`；`vdda=pin 5 to 3V3`；`vss=pin 15 to GND`；`decoupling=C11 100nF` |
| 关键网络 | U10 关键网络索引 | `PA0-PA5=ad0-ad5`；`PA6=RGB`；`PA7=ad6`；`PB1=ad7`；`PF0=ad_Key`；`PA9=SCL`；`PA10=SDA`；`PA13=MCU_SWDIO`；`PA14=MCU_SWCLK` |

## 待确认事项

- `address.i2c-not-shown`：本页原理图显示 SCL/SDA 硬件连接，但没有印出 I2C 从机地址，无法仅凭该原理图确认地址值。（证据：图 09ccb8692112 / 第 1 页 / 页 1 网格 A1-B1：J1 与 U10 的 SCL/SDA 网络，页面未见十六进制 I2C 地址标注）
- `review.i2c-address`：Unit 8Angle 当前固件使用的 I2C 从机地址是否为 0x43？；原因：本页原理图只显示 SCL/SDA 与上拉电路，没有地址选择脚、地址标注或固件版本信息；需要用对应固件或通信协议资料确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `09ccb86921121c350877d12758370e78e8d14ce4bcec58e1028e02add00885ed` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/608/SCH_UNIT_8Angle_V1.01_sch_01.png` |

---

源文档：`zh_CN/unit/8Angle.md`

源文档 SHA-256：`6320330a2dd4b061f7008ef2898c3ce8555652b18fbd76d2a9e197f59347ba91`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
