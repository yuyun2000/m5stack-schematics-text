# Unit 8Encoder 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 8Encoder |
| SKU | U153 |
| 产品 ID | `unit-8encoder-02e2f84d6fb0` |
| 源文档 | `zh_CN/unit/8Encoder.md` |

## 概述

Unit 8Encoder 以 U10 STM32F030C8T6 为采集与通信主控，直接读取八个 EC11A 旋转编码器的 A/B 与按压网络以及 SW9 拨动开关。J1 通过 SCL、SDA、VCC_5V 和 GND 接入，U11 BL8075CB5TR33 产生 3V3，I2C 分别连接 MCU 的 PB10/PB11。U1-U9 共九颗 WS2812C-2020 由 PB0 的 RGB 网络串行驱动；板上还提供 J2 SWD 调试口、NRST RC 网络和 BOOT0 下拉。

## 检索关键词

`Unit 8Encoder`、`U153`、`STM32F030C8T6`、`U10`、`BL8075CB5TR33`、`U11`、`WS2812C-2020`、`U1-U9`、`EC11A EH`、`SW1-SW8`、`SS12D07L4B`、`SW9`、`J1`、`GROVE_4P`、`J2`、`SWD`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`BOOT0`、`I2C`、`SCL`、`SDA`、`PB10`、`PB11`、`RGB`、`PB0`、`SW_K1-SW_K9`、`EN S1 A`、`EN S8 B`、`VCC_5V`、`3V3`、`4.7K`、`10K`、`100nF`、`0x41`、`rotary encoder`、`RGB daisy chain`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U10 | STM32F030C8T6 | 主控 MCU，采集八路编码器和 SW9，控制 RGB 串行链，并提供 I2C 与 SWD。 | 图 75d0558295a7 / 第 1 页 / 网格 B1-B2，U10 STM32F030C8T6 及 PA/PB/SWD/电源引脚网络 |
| U11 | BL8075CB5TR33 | VCC_5V 到 3V3 的五引脚稳压器，输入/输出分别配置 C1/C2。 | 图 75d0558295a7 / 第 1 页 / 网格 D2，U11 BL8075CB5TR33，VCC_5V 输入、3V3 输出、C1/C2 |
| U1-U9 | WS2812C-2020 | 九颗 3V3 RGB LED，U1.DI 接 RGB，按 U1 到 U9 方向串行级联。 | 图 75d0558295a7 / 第 1 页 / 网格 A1-A4，U1-U9 WS2812C-2020 的 DI/DO、3V3、GND 链 |
| SW1-SW8 | EC11A EH | 八个旋转编码器，每个具有 A/B 正交输出和 SW_K1-SW_K8 按压输出。 | 图 75d0558295a7 / 第 1 页 / 网格 B3-C4，SW1-SW8 EC11A EH，EN Sx A/B 与 SW_Kx 网络 |
| SW9 | SS12D07L4B | 拨动开关，输出网络为 SW_K9，并由 R11 上拉至 3V3。 | 图 75d0558295a7 / 第 1 页 / 网格 D4，SW9 SS12D07L4B、SW_K9、R11 10K 与 GND |
| J1 | GROVE_4P | 四针 Grove 接口，针脚 IO2/IO1/5V/GND 分别连接 SCL/SDA/VCC_5V/GND。 | 图 75d0558295a7 / 第 1 页 / 网格 D1，J1 GROVE_4P 的 IO2/IO1/5V/GND 与 SCL/SDA/VCC_5V/GND |
| J2 | SWD | 五针 MCU 调试连接器，引出 3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND。 | 图 75d0558295a7 / 第 1 页 / 网格 C2，J2 SWD 1-5 脚网络 |
| RP1,RP2 | 10K | SW_K1-SW_K8 八路编码器按压输入的 3V3 上拉电阻阵列。 | 图 75d0558295a7 / 第 1 页 / 网格 C3-C4，RP1/RP2 标注 10K，输出 SW_K1-SW_K8 |
| RP3-RP6 | 10K | EN S1 A/B 至 EN S8 A/B 十六路编码器相位输入的 3V3 上拉电阻阵列。 | 图 75d0558295a7 / 第 1 页 / 网格 C3-D4，RP3-RP6 标注 10K，输出 EN S1 A/B 至 EN S8 A/B |
| R3,R4 | 4.7K | SCL 与 SDA 到 3V3 的 I2C 上拉电阻。 | 图 75d0558295a7 / 第 1 页 / 网格 D1，R3/R4 4.7K 从 SCL/SDA 上拉到 3V3 |
| R1,C14 | 10K / 100nF | NRST 的 3V3 上拉与对地电容复位网络。 | 图 75d0558295a7 / 第 1 页 / 网格 C1-C2，U10 NRST、R1 10K 到 3V3、C14 100nF 到 GND |
| R2 | 10K | U10 BOOT0 到 GND 的下拉电阻。 | 图 75d0558295a7 / 第 1 页 / 网格 C2，U10 BOOT0 44 脚经 R2 10K 接 GND |
| R11 | 10K | SW_K9 到 3V3 的上拉电阻。 | 图 75d0558295a7 / 第 1 页 / 网格 D4，R11 10K 连接 3V3 与 SW_K9 |
| C1,C2 | 1uF/25V | U11 的 VCC_5V 输入与 3V3 输出对地电容。 | 图 75d0558295a7 / 第 1 页 / 网格 D2，U11 两侧 C1/C2，均标注 1uF/25V |
| C15-C30 | 100nF | 八个编码器 A/B 相位网络各自到 GND 的滤波电容。 | 图 75d0558295a7 / 第 1 页 / 网格 B3-C4，SW1-SW8 两侧 C15-C30，均标注 100nF |

## 系统结构

### 整板架构

U10 STM32F030C8T6 连接八个 EC11A 编码器、SW9、九颗 WS2812C-2020、J1 I2C/Grove 和 J2 SWD；U11 从 VCC_5V 生成 3V3。

- 参数与网络：`controller=U10 STM32F030C8T6`；`encoders=SW1-SW8 EC11A EH`；`slide_switch=SW9 SS12D07L4B`；`rgb_leds=U1-U9 WS2812C-2020`；`host_interface=J1 I2C`；`debug=J2 SWD`；`regulator=U11 BL8075CB5TR33`
- 证据：图 75d0558295a7 / 第 1 页 / 第 1 页全图，U10、U11、U1-U9、SW1-SW9、J1、J2 功能分区

## 核心器件

### U10 STM32F030C8T6

U10 的 PA0-PA11 与 PB12-PB15 接编码器相位，PB2-PB9 接八个编码器按压，PB1 接 SW_K9，PB0 接 RGB，PB10/PB11 接 SCL/SDA，PA13/PA14 接 SWD。

- 参数与网络：`reference=U10`；`part_number=STM32F030C8T6`；`encoder_phase_ports=PA0-PA11,PB12-PB15`；`encoder_key_ports=PB2-PB9`；`slide_switch_port=PB1`；`rgb_port=PB0`；`i2c_ports=PB10 SCL,PB11 SDA`；`debug_ports=PA13/SWDIO,PA14/SWCLK`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B1-B2，U10 左右两侧全部网络与引脚号

### U1-U9 RGB 链

U10 PB0（18 脚）的 RGB 网络连接 U1.DI，随后 U1.DO→U2.DI→U3.DI→U4.DI→U5.DI→U6.DI→U7.DI→U8.DI→U9.DI；各器件 VDD 接 3V3、GND 接地。

- 参数与网络：`driver_pin=U10 PB0 pin18`；`input_net=RGB`；`first_device=U1 DI pin3`；`chain_order=U1,U2,U3,U4,U5,U6,U7,U8,U9`；`last_output=U9 DO pin1`；`supply=3V3`；`ground=GND`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 A1-A4 U1-U9 DI/DO 串链及网格 B2 U10 PB0 RGB

## 电源

### U11 供电转换

J1 的 5V/VCC_5V 网络进入 U11 BL8075CB5TR33，U11 输出 3V3；C1 与 C2 均为 1uF/25V，分别跨接输入/输出到 GND，U11 EN 接输入侧。

- 参数与网络：`input_rail=VCC_5V`；`output_rail=3V3`；`regulator=U11 BL8075CB5TR33`；`input_capacitor=C1 1uF/25V`；`output_capacitor=C2 1uF/25V`；`enable=EN tied to VCC_5V`；`ground_pin=U11.2`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 D2，VCC_5V-C1-U11-C2-3V3 电源链

### 3V3 电源轨

3V3 为 U10 的 VDDA/VDD/PF7-VDD 引脚、U1-U9 VDD、I2C 上拉、按键/编码器上拉阵列、NRST 上拉和 J2.1 供电。

- 参数与网络：`mcu_pins=U10.1,U10.9,U10.24,U10.36,U10.48`；`rgb_vdd=U1-U9 pin 4`；`i2c_pullups=R3,R4`；`input_pullups=RP1-RP6,R11`；`reset_pullup=R1`；`debug_pin=J2.1`
- 证据：图 75d0558295a7 / 第 1 页 / U10 电源脚、U1-U9 VDD、R1/R3/R4/RP1-RP6/R11 与 J2.1 的 3V3 标注

### 3V3 去耦

C10-C12 各为 100nF，跨接 U10 的 3V3 与 GND；C3-C9 和 C13 各为 100nF，跨接 RGB 区域的 3V3 与 GND。

- 参数与网络：`mcu_decoupling=C10,C11,C12 100nF`；`rgb_decoupling=C3,C4,C5,C6,C7,C8,C9,C13 100nF`；`rail=3V3`；`return=GND`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 A3 C3-C9/C13 与网格 B1-C1 C10-C12，均标注 100nF

## 接口

### J1 GROVE_4P

J1 的 IO2、IO1、5V、GND 四个位置分别连接 SCL、SDA、VCC_5V、GND。

- 参数与网络：`reference=J1`；`part_number=GROVE_4P`；`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`direction=SCL/SDA 双向总线`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 D1，J1 GROVE_4P 左右功能与网络标注

## 总线

### I2C 总线

SCL 从 J1.IO2 连接 U10 PB10（21 脚），SDA 从 J1.IO1 连接 U10 PB11（22 脚）；R3/R4 各以 4.7K 上拉到 3V3。

- 参数与网络：`bus=I2C`；`device=U10 STM32F030C8T6`；`scl_connector=J1 IO2`；`scl_mcu_pin=U10 PB10 pin 21`；`sda_connector=J1 IO1`；`sda_mcu_pin=U10 PB11 pin 22`；`scl_pullup=R3 4.7K to 3V3`；`sda_pullup=R4 4.7K to 3V3`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B2 的 U10 PB10/PB11 与网格 D1 的 J1 SCL/SDA、R3/R4

## GPIO 与控制信号

### U10 BOOT0

U10 BOOT0（44 脚）通过 R2（10K）下拉到 GND。

- 参数与网络：`mcu_pin=U10 BOOT0 pin 44`；`resistor=R2 10K`；`default_connection=GND`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 C2，U10 BOOT0 44 脚、R2 10K 与 GND

### SW1-SW4 编码器相位映射

SW1 A/B 接 PA10/PA11，SW2 A/B 接 PA8/PA9，SW3 A/B 接 PB14/PB15，SW4 A/B 接 PB12/PB13。

- 参数与网络：`sw1=EN S1 A=PA10 pin31; EN S1 B=PA11 pin32`；`sw2=EN S2 A=PA8 pin29; EN S2 B=PA9 pin30`；`sw3=EN S3 A=PB14 pin27; EN S3 B=PB15 pin28`；`sw4=EN S4 A=PB12 pin25; EN S4 B=PB13 pin26`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B1-B2 U10 EN S1-S4 A/B 网络；网格 B3-B4 SW1-SW4 A/B

### SW5-SW8 编码器相位映射

SW5 A/B 接 PA6/PA7，SW6 A/B 接 PA4/PA5，SW7 A/B 接 PA2/PA3，SW8 A/B 接 PA0/PA1。

- 参数与网络：`sw5=EN S5 A=PA6 pin16; EN S5 B=PA7 pin17`；`sw6=EN S6 A=PA4 pin14; EN S6 B=PA5 pin15`；`sw7=EN S7 A=PA2 pin12; EN S7 B=PA3 pin13`；`sw8=EN S8 A=PA0 pin10; EN S8 B=PA1 pin11`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B1 U10 EN S5-S8 A/B 网络；网格 C3-C4 SW5-SW8 A/B

### SW1-SW8 按压映射

SW_K1-SW_K8 分别连接 U10 PB2、PB3、PB4、PB5、PB6、PB7、PB8、PB9。

- 参数与网络：`sw_k1=PB2 pin20`；`sw_k2=PB3 pin39`；`sw_k3=PB4 pin40`；`sw_k4=PB5 pin41`；`sw_k5=PB6 pin42`；`sw_k6=PB7 pin43`；`sw_k7=PB8 pin45`；`sw_k8=PB9 pin46`；`pullups=RP1,RP2 10K to 3V3`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B2 U10 PB2-PB9 SW_K1-SW_K8；SW1-SW8 D 端；RP1/RP2

## 时钟

### U10 时钟连接

U10 的 PF0-OSCIN、PF1-OSCOUT、PC14-OSC32IN 和 PC15-OSC32OUT 在原理图中未连接，页面未显示外部晶振或谐振器。

- 参数与网络：`high_speed_clock_pins=PF0-OSCIN pin5,PF1-OSCOUT pin6`；`low_speed_clock_pins=PC14-OSC32IN pin3,PC15-OSC32OUT pin4`；`external_crystal=原理图未显示`；`clock_source=本页未标注`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B2，U10 PC14/PC15/PF0/PF1 时钟脚无外部连接；第 1 页无晶振位号

## 复位

### U10 NRST

U10 NRST（7 脚）由 R1（10K）上拉到 3V3，并由 C14（100nF）接 GND，同时引出到 J2.4。

- 参数与网络：`mcu_pin=U10 NRST pin 7`；`pullup=R1 10K to 3V3`；`capacitor=C14 100nF to GND`；`debug_connector=J2.4`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 C1-C2，U10 NRST-R1-C14 网络及 J2.4 NRST

## 保护电路

### J1 外部接口保护

J1 的 SCL、SDA、VCC_5V 和 GND 直接进入上拉/稳压与地网络，本页未显示 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`connector=J1`；`signals=SCL,SDA,VCC_5V,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_polarity=原理图未显示`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 D1-D2，J1 到 R3/R4/U11 的直接路径

## 存储

### 外部存储器

第 1 页未显示外部 Flash、EEPROM、SD 卡或其他存储器件，所有板级控制均围绕 U10 展开。

- 参数与网络：`external_flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`controller=U10 STM32F030C8T6`
- 证据：图 75d0558295a7 / 第 1 页 / 第 1 页全图，未出现外部存储器位号或存储总线

## 调试与烧录

### J2 SWD 调试接口

J2.1-J2.5 依次连接 3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND；MCU_SWCLK 接 U10 PA14/SWCLK（37 脚），MCU_SWDIO 接 PA13/SWDIO（34 脚）。

- 参数与网络：`reference=J2`；`pin_1=3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`；`swclk_mcu=PA14/SWCLK pin 37`；`swdio_mcu=PA13/SWDIO pin 34`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B1 的 U10 PA13/PA14 与网格 C2 的 J2 1-5 脚

## 模拟电路

### 编码器 A/B 滤波与上拉

EN S1 A/B 至 EN S8 A/B 均由 RP3-RP6 的 10K 电阻上拉到 3V3，并分别由 C15-C30 的 100nF 电容接 GND。

- 参数与网络：`phase_inputs=16`；`pullups=RP3-RP6 10K to 3V3`；`filter_capacitors=C15-C30 100nF to GND`；`encoder_common=SW1-SW8 C pins to GND`
- 证据：图 75d0558295a7 / 第 1 页 / 网格 B3-D4，SW1-SW8 A/B、C15-C30 与 RP3-RP6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `controller=U10 STM32F030C8T6`；`encoders=SW1-SW8 EC11A EH`；`slide_switch=SW9 SS12D07L4B`；`rgb_leds=U1-U9 WS2812C-2020`；`host_interface=J1 I2C`；`debug=J2 SWD`；`regulator=U11 BL8075CB5TR33` |
| 核心器件 | U10 STM32F030C8T6 | `reference=U10`；`part_number=STM32F030C8T6`；`encoder_phase_ports=PA0-PA11,PB12-PB15`；`encoder_key_ports=PB2-PB9`；`slide_switch_port=PB1`；`rgb_port=PB0`；`i2c_ports=PB10 SCL,PB11 SDA`；`debug_ports=PA13/SWDIO,PA14/SWCLK` |
| 电源 | U11 供电转换 | `input_rail=VCC_5V`；`output_rail=3V3`；`regulator=U11 BL8075CB5TR33`；`input_capacitor=C1 1uF/25V`；`output_capacitor=C2 1uF/25V`；`enable=EN tied to VCC_5V`；`ground_pin=U11.2` |
| 电源 | 3V3 电源轨 | `mcu_pins=U10.1,U10.9,U10.24,U10.36,U10.48`；`rgb_vdd=U1-U9 pin 4`；`i2c_pullups=R3,R4`；`input_pullups=RP1-RP6,R11`；`reset_pullup=R1`；`debug_pin=J2.1` |
| 接口 | J1 GROVE_4P | `reference=J1`；`part_number=GROVE_4P`；`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`direction=SCL/SDA 双向总线` |
| 总线 | I2C 总线 | `bus=I2C`；`device=U10 STM32F030C8T6`；`scl_connector=J1 IO2`；`scl_mcu_pin=U10 PB10 pin 21`；`sda_connector=J1 IO1`；`sda_mcu_pin=U10 PB11 pin 22`；`scl_pullup=R3 4.7K to 3V3`；`sda_pullup=R4 4.7K to 3V3` |
| 总线地址 | Unit 8Encoder I2C 地址 | `bus=I2C`；`documented_candidate=0x41`；`schematic_visible_address=未标注`；`address_straps=未显示`；`firmware_defined=需确认` |
| 调试与烧录 | J2 SWD 调试接口 | `reference=J2`；`pin_1=3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=NRST`；`pin_5=GND`；`swclk_mcu=PA14/SWCLK pin 37`；`swdio_mcu=PA13/SWDIO pin 34` |
| 复位 | U10 NRST | `mcu_pin=U10 NRST pin 7`；`pullup=R1 10K to 3V3`；`capacitor=C14 100nF to GND`；`debug_connector=J2.4` |
| GPIO 与控制信号 | U10 BOOT0 | `mcu_pin=U10 BOOT0 pin 44`；`resistor=R2 10K`；`default_connection=GND` |
| GPIO 与控制信号 | SW1-SW4 编码器相位映射 | `sw1=EN S1 A=PA10 pin31; EN S1 B=PA11 pin32`；`sw2=EN S2 A=PA8 pin29; EN S2 B=PA9 pin30`；`sw3=EN S3 A=PB14 pin27; EN S3 B=PB15 pin28`；`sw4=EN S4 A=PB12 pin25; EN S4 B=PB13 pin26` |
| GPIO 与控制信号 | SW5-SW8 编码器相位映射 | `sw5=EN S5 A=PA6 pin16; EN S5 B=PA7 pin17`；`sw6=EN S6 A=PA4 pin14; EN S6 B=PA5 pin15`；`sw7=EN S7 A=PA2 pin12; EN S7 B=PA3 pin13`；`sw8=EN S8 A=PA0 pin10; EN S8 B=PA1 pin11` |
| GPIO 与控制信号 | SW1-SW8 按压映射 | `sw_k1=PB2 pin20`；`sw_k2=PB3 pin39`；`sw_k3=PB4 pin40`；`sw_k4=PB5 pin41`；`sw_k5=PB6 pin42`；`sw_k6=PB7 pin43`；`sw_k7=PB8 pin45`；`sw_k8=PB9 pin46`；`pullups=RP1,RP2 10K to 3V3` |
| 模拟电路 | 编码器 A/B 滤波与上拉 | `phase_inputs=16`；`pullups=RP3-RP6 10K to 3V3`；`filter_capacitors=C15-C30 100nF to GND`；`encoder_common=SW1-SW8 C pins to GND` |
| 核心器件 | U1-U9 RGB 链 | `driver_pin=U10 PB0 pin18`；`input_net=RGB`；`first_device=U1 DI pin3`；`chain_order=U1,U2,U3,U4,U5,U6,U7,U8,U9`；`last_output=U9 DO pin1`；`supply=3V3`；`ground=GND` |
| 电源 | 3V3 去耦 | `mcu_decoupling=C10,C11,C12 100nF`；`rgb_decoupling=C3,C4,C5,C6,C7,C8,C9,C13 100nF`；`rail=3V3`；`return=GND` |
| 时钟 | U10 时钟连接 | `high_speed_clock_pins=PF0-OSCIN pin5,PF1-OSCOUT pin6`；`low_speed_clock_pins=PC14-OSC32IN pin3,PC15-OSC32OUT pin4`；`external_crystal=原理图未显示`；`clock_source=本页未标注` |
| 存储 | 外部存储器 | `external_flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`controller=U10 STM32F030C8T6` |
| 保护电路 | J1 外部接口保护 | `connector=J1`；`signals=SCL,SDA,VCC_5V,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_polarity=原理图未显示` |
| GPIO 与控制信号 | SW9 拨动开关状态 | `switch=SW9 SS12D07L4B`；`signal=SW_K9`；`mcu_pin=U10 PB1 pin19`；`pullup=R11 10K to 3V3`；`ground=GND`；`position_truth_table=未标注` |
| 核心器件 | RGB 与控件物理对应 | `rgb_devices=U1-U9`；`electrical_order=U1,U2,U3,U4,U5,U6,U7,U8,U9`；`controls=SW1-SW9`；`physical_mapping=未标注` |

## 待确认事项

- `address.i2c-address-undetermined`：原理图没有打印 I2C 从设备地址，也没有显示硬件地址配置电阻或地址选择引脚；仅凭本页不能确认产品正文所列的 0x41。（证据：图 75d0558295a7 / 第 1 页 / 第 1 页 J1 SCL/SDA 至 U10 PB10/PB11 路径，页面无 0x41 或地址选择标注）
- `gpio.sw9-state-map-undetermined`：SW_K9 连接 U10 PB1（19 脚）并由 R11（10K）上拉到 3V3；SW9 符号显示接地端，但本页没有给出各机械档位对应的 SW_K9 高低电平真值表。（证据：图 75d0558295a7 / 第 1 页 / 网格 D4，SW9、SW_K9、R11 10K、3V3 与 GND；网格 B2 U10 PB1）
- `component.rgb-control-association-undetermined`：原理图确认 U1-U9 的串行电气顺序，但未标注每颗 RGB 分别对应 SW1-SW8 中哪个编码器或 SW9 拨动开关。（证据：图 75d0558295a7 / 第 1 页 / 网格 A1-A4 的 U1-U9 仅显示串链；SW1-SW9 区域无 RGB 对应编号）
- `review.i2c-address`：当前固件的 I2C 从设备地址是否固定为 0x41，是否存在可配置地址方式？；原因：地址属于 MCU 固件行为，原理图没有打印 0x41 或地址选择硬件。
- `review.sw9-truth-table`：SW9 各机械档位分别使 SW_K9 读取高电平还是低电平？；原因：原理图显示上拉与接地连接，但没有档位名称或真值表。
- `review.rgb-control-mapping`：U1-U9 在 PCB 上分别对应 SW1-SW8 和 SW9 中的哪个实体控件？；原因：原理图只给出 RGB 串行顺序，没有给出物理位置或控件对应表。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `75d0558295a7325c0499d532af4081b0cf764bf37f0287085b962283fccbb332` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/607/SCH_UNIT_8Encoder_V1.01_sch_01.png` |

---

源文档：`zh_CN/unit/8Encoder.md`

源文档 SHA-256：`1a1fe3c044e0e1e8d9688b3446490040d5907ace014a4ffc4f28c574473084f8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
