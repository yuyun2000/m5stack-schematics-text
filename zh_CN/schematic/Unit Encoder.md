# Unit Encoder 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Encoder |
| SKU | U135 |
| 产品 ID | `unit-encoder-20eb287ba027` |
| 源文档 | `zh_CN/unit/encoder.md` |

## 概述

Unit Encoder 以 STM32F030F4P6（U2）为主控，采集 J2 旋转编码器的 IN_A、IN_B 与 BTN，并通过 J1 的 SCL/SDA 连接外部 I2C 主机。U2 PA0 的 SK6812 网络驱动 LED1、LED2 两颗串行级联 SK6812，LED 由 +5V 供电、数据网由 R1 10KΩ 上拉到 +3.3V。HT7533（U1）将 J1 输入的 +5V 稳压为 +3.3V，为主控、编码器输入上拉和 I2C 上拉供电。板上提供 BOOT0 下拉、NRST RC 网络和 5 针 SWD；原理图未打印 I2C 地址或编码器每圈脉冲数。

## 检索关键词

`Unit Encoder`、`U135`、`STM32F030F4P6`、`HT7533`、`SK6812`、`Rotary encoder`、`IN_A`、`IN_B`、`BTN`、`SCL`、`SDA`、`I2C`、`0x40`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`PA0`、`PA5`、`PA6`、`PA7`、`PA9`、`PA10`、`+5V`、`+3.3V`、`30 pulses`、`R4 10KΩ`、`R8 10KΩ`、`R9 10KΩ`、`100nF`、`HY-2.0_IIC`、`SWD_5p`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | 采集编码器与按键、驱动 SK6812 并提供 I2C/SWD 的主控 | 图 49167f49ddc2 / 第 1 页 / 页 1 左中 U2 STM32F030F4P6，pins 1~20 与 SK6812/BTN/IN_A/IN_B/SCL/SDA/SWD/NRST 网络 |
| U1 | HT7533 | 将 +5V 稳压为 +3.3V | 图 49167f49ddc2 / 第 1 页 / 页 1 左上 U1 HT7533，VIN pin 2 接 +5V、VOUT pin 3 接 +3.3V、GND pin 1 接地 |
| J2 | Rotary encode | A/B 相旋转编码器与按压按键组件 | 图 49167f49ddc2 / 第 1 页 / 页 1 中部 J2 Rotary encode：button pins 1/2 b1/b2 与 rotary pins 3/4/5 A/COM/B |
| LED1/LED2 | SK6812 | 由 U2 PA0 驱动的两颗串行级联 RGB LED | 图 49167f49ddc2 / 第 1 页 / 页 1 上部 LED1/LED2 SK6812：DIN pin 3、DOUT pin 1、VDD pin 4、VSS pin 2 及级联线 |
| J1 | HY-2.0_IIC | 外部 I2C、+5V 与 GND 接口 | 图 49167f49ddc2 / 第 1 页 / 页 1 右下 J1 HY-2.0_IIC：pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC/+5V、pin 4 GND |
| P1 | SWD_5p | 主控烧录与调试接口 | 图 49167f49ddc2 / 第 1 页 / 页 1 右中 P1 SWD_5p：pins 1~5 为 +3.3V、SWCLK、SWDIO、NRST、GND |
| R4/C1 | 10KΩ / 100nF | BTN 的 +3.3V 上拉与对地滤波网络 | 图 49167f49ddc2 / 第 1 页 / 页 1 中部 J2 左侧：BTN 节点经 R4 10KΩ 接 +3.3V、经 C1 100nF 接 GND |
| R8/C6 | 10KΩ / 100nF | IN_A 的 +3.3V 上拉与对地滤波网络 | 图 49167f49ddc2 / 第 1 页 / 页 1 中下 J2 A pin 3/IN_A：R8 10KΩ 到 +3.3V、C6 100nF 到 GND |
| R9/C7 | 10KΩ / 100nF | IN_B 的 +3.3V 上拉与对地滤波网络 | 图 49167f49ddc2 / 第 1 页 / 页 1 中下 J2 B pin 5/IN_B：R9 10KΩ 到 +3.3V、C7 100nF 到 GND |
| R6/R7 | 10KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 49167f49ddc2 / 第 1 页 / 页 1 右下：R6/R7 均 10KΩ，上端 +3.3V，下端分别接 SCL/SDA |
| R3 | 10KΩ | U2 BOOT0 到 GND 的下拉电阻 | 图 49167f49ddc2 / 第 1 页 / 页 1 左中 U2 BOOT0 pin 1 经 R3 10KΩ 接 GND |
| R5/C5 | 10KΩ / 100nF | U2 NRST 的 +3.3V 上拉和对地复位电容 | 图 49167f49ddc2 / 第 1 页 / 页 1 左中 U2 NRST pin 4：R5 10KΩ 到 +3.3V、C5 100nF 到 GND |
| R1 | 10KΩ | SK6812 数据输入网络到 +3.3V 的上拉电阻 | 图 49167f49ddc2 / 第 1 页 / 页 1 上部：U2 PA0/SK6812/LED1 DIN 共网经 R1 10KΩ 接 +3.3V |
| C2/C3/C4 | 100nF / 22uF / 22uF | 主控 +3.3V 去耦及 HT7533 输入输出滤波 | 图 49167f49ddc2 / 第 1 页 / 页 1 左侧：C2 100nF 跨 +3.3V/GND，C3 22uF 跨 +5V/GND，C4 22uF 跨 +3.3V/GND |

## 系统结构

### Unit Encoder

U2 STM32F030F4P6 采集 J2 的 BTN、IN_A、IN_B，驱动 LED1/LED2 SK6812，并通过 J1 SCL/SDA 与外部主机通信；U1 从 +5V 产生 +3.3V。

- 参数与网络：`controller=U2 STM32F030F4P6`；`encoder=J2 Rotary encode`；`inputs=BTN,IN_A,IN_B`；`rgb=LED1,LED2 SK6812`；`communication=J1 SCL,SDA`；`power=+5V->U1 HT7533->+3.3V`
- 证据：图 49167f49ddc2 / 第 1 页 / 整页：U1/U2/J2/LED1/LED2/J1/P1 与所有同名信号

## 核心器件

### J2 Rotary encode

J2 button pin 1（b1）接 BTN、pin 2（b2）接 GND；rotary pin 3（A）接 IN_A、pin 4（COM）接 GND、pin 5（B）接 IN_B。

- 参数与网络：`pin_1=b1,BTN`；`pin_2=b2,GND`；`pin_3=A,IN_A`；`pin_4=COM,GND`；`pin_5=B,IN_B`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 中部 J2 pins 1~5、b1/b2/A/COM/B 与 BTN/IN_A/IN_B/GND

## 电源

### U1 HT7533

U1 VIN pin 2 接 +5V，VOUT pin 3 输出 +3.3V，GND pin 1 接地；C3/C4 各 22uF 分别位于输入和输出侧。

- 参数与网络：`input=VIN pin 2,+5V`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C3 22uF`；`output_capacitor=C4 22uF`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 左上 U1/C3/C4/+5V/+3.3V/GND

### U2 电源

U2 VDDA pin 5 与 VDD pin 16 接 +3.3V，VSS pin 15 接 GND；C2 100nF 跨接 +3.3V 与 GND。

- 参数与网络：`vdda=pin 5,+3.3V`；`vdd=pin 16,+3.3V`；`vss=pin 15,GND`；`decoupling=C2 100nF`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 左中 U2 pins 5/15/16 与左侧 C2

### LED1/LED2 供电

LED1 与 LED2 的 VDD pin 4 均接 +5V，VSS pin 2 均接 GND；SK6812 数据网络由 R1 10KΩ上拉到 +3.3V。

- 参数与网络：`devices=LED1,LED2 SK6812`；`vdd=pin 4,+5V`；`vss=pin 2,GND`；`data_pullup=R1 10KΩ to +3.3V`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 上部 LED1/LED2 VDD/VSS 与 R1/SK6812/+3.3V

## 接口

### J1 HY-2.0_IIC

J1 pin 1 标 IIC_SCL 并接 SCL，pin 2 标 IIC_SDA 并接 SDA，pin 3 标 VCC 并接 +5V，pin 4 标 GND 并接地。

- 参数与网络：`pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC,+5V`；`pin_4=GND`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 右下 J1 pins 1~4 与 SCL/SDA/+5V/GND

### 未使用的 U2 GPIO

U2 PA1 pin 7、PA2 pin 8、PA3 pin 9、PA4 pin 10 与 PB1 pin 14 在页面标记未连接。

- 参数与网络：`unused_pins=PA1.7,PA2.8,PA3.9,PA4.10,PB1.14`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 U2 左侧 pins 7~10 与右侧 pin14 的未连接标记

## 总线

### U2 I2C

SCL 从 J1 连接 U2 PA9 pin 17，SDA 从 J1 连接 U2 PA10 pin 18；R6/R7 各 10KΩ将两线拉至 +3.3V。

- 参数与网络：`controller=U2 STM32F030F4P6`；`scl=PA9 pin 17`；`sda=PA10 pin 18`；`pullups=R6/R7 10KΩ to +3.3V`；`connector=J1`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 U2 PA9/PA10 与 J1/R6/R7 的 SCL/SDA 同名网络

### LED1/LED2 SK6812 级联

U2 PA0 pin 6 的 SK6812 网络进入 LED1 DIN pin 3，LED1 DOUT pin 1 连接 LED2 DIN pin 3，LED2 DOUT pin 1 在页面未继续连接。

- 参数与网络：`controller_pin=U2 PA0 pin 6`；`input_net=SK6812`；`first_led=LED1 DIN pin3`；`cascade=LED1 DOUT pin1->LED2 DIN pin3`；`chain_end=LED2 DOUT pin1 no-connect`；`count=2`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 上部 U2 SK6812 网络与 LED1/LED2 DIN/DOUT 连线

## GPIO 与控制信号

### U2 关键 GPIO

U2 PA0 pin 6 接 SK6812，PA5 pin 11 接 BTN，PA6 pin 12 接 IN_A，PA7 pin 13 接 IN_B，PA9 pin 17 接 SCL，PA10 pin 18 接 SDA，PA13 pin 19 接 SWDIO，PA14 pin 20 接 SWCLK。

- 参数与网络：`PA0_pin6=SK6812`；`PA5_pin11=BTN`；`PA6_pin12=IN_A`；`PA7_pin13=IN_B`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 U2 左右两侧 GPIO 名、pin 编号和网络

### BTN 按键输入

BTN 由 R4 10KΩ上拉到 +3.3V、C1 100nF 接 GND；J2 按下时 b1 pin 1 与 b2 pin 2 闭合，将 BTN 接 GND，因此按键为低有效。

- 参数与网络：`mcu_pin=U2 PA5 pin 11`；`pullup=R4 10KΩ to +3.3V`；`capacitor=C1 100nF to GND`；`button_contacts=J2 pins 1/2`；`pressed_logic=low`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 中部 BTN/R4/C1/J2 b1-b2 与 U2 PA5

### IN_A/IN_B 编码输入

J2 A pin 3 的 IN_A 连接 U2 PA6 pin 12，并由 R8 10KΩ上拉、C6 100nF 对地；J2 B pin 5 的 IN_B 连接 U2 PA7 pin 13，并由 R9 10KΩ上拉、C7 100nF 对地，COM pin 4 接 GND。

- 参数与网络：`phase_a=J2.3 IN_A->U2 PA6 pin12`；`phase_a_pullup=R8 10KΩ`；`phase_a_cap=C6 100nF`；`phase_b=J2.5 IN_B->U2 PA7 pin13`；`phase_b_pullup=R9 10KΩ`；`phase_b_cap=C7 100nF`；`common=J2.4 GND`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 中部/中下 J2 A/COM/B、IN_A/IN_B、R8/R9/C6/C7 与 U2 PA6/PA7

## 时钟

### U2 PF0/PF1 时钟引脚

U2 PF0/OSC_IN pin 2 与 PF1/OSC_OUT pin 3 在页面未连接，整页未绘出外部晶振或振荡器。

- 参数与网络：`osc_in=PF0 pin 2 no-connect`；`osc_out=PF1 pin 3 no-connect`；`external_clock_component=null`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 U2 pins 2/3 未连接端点，整页无晶振位号

## 复位

### U2 NRST

U2 NRST pin 4 由 R5 10KΩ上拉到 +3.3V，并由 C5 100nF 接 GND；NRST 同时引至 P1 pin 4。

- 参数与网络：`mcu_pin=NRST pin 4`；`pullup=R5 10KΩ to +3.3V`；`capacitor=C5 100nF to GND`；`debug_header=P1 pin 4`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 左中 NRST/R5/C5/U2 pin4 与右中 P1 NRST

### U2 BOOT0

U2 BOOT0 pin 1 通过 R3 10KΩ下拉到 GND。

- 参数与网络：`mcu_pin=BOOT0 pin 1`；`resistor=R3 10KΩ`；`strap=GND`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 左中 U2 BOOT0 pin1-R3 10KΩ-GND

## 保护电路

### Grove 与编码器接口保护

本页没有绘出 TVS、ESD 阵列、保险丝或反接保护器件。

- 参数与网络：`grove_esd=null`；`encoder_esd=null`；`fuse=null`；`reverse_polarity=null`
- 证据：图 49167f49ddc2 / 第 1 页 / 整页所有位号，无 TVS/ESD/FUSE/反接保护元件

## 关键网络

### Unit Encoder 关键网络索引

关键路径为 J2 BTN/A/B→BTN/IN_A/IN_B→U2 PA5/PA6/PA7，U2 PA0→SK6812→LED1→LED2，J1 SCL/SDA→U2 PA9/PA10，以及 +5V→U1→+3.3V。

- 参数与网络：`encoder_inputs=J2.1/3/5-U2 PA5/PA6/PA7`；`rgb_path=U2 PA0-LED1-LED2`；`i2c_path=J1.1/2-U2 PA9/PA10`；`power_path=J1.3 +5V-U1-+3.3V`；`debug=P1 SWD`
- 证据：图 49167f49ddc2 / 第 1 页 / 整页 BTN/IN_A/IN_B/SK6812/SCL/SDA/+5V/+3.3V 同名网络

## 调试与烧录

### P1 SWD_5p

P1 pin 1 接 +3.3V，pin 2 接 SWCLK/U2 PA14 pin 20，pin 3 接 SWDIO/U2 PA13 pin 19，pin 4 接 NRST，pin 5 接 GND。

- 参数与网络：`pin_1=+3.3V`；`pin_2=SWCLK,U2 PA14 pin20`；`pin_3=SWDIO,U2 PA13 pin19`；`pin_4=NRST,U2 pin4`；`pin_5=GND`
- 证据：图 49167f49ddc2 / 第 1 页 / 页 1 右中 P1 pins 1~5 与 U2 SWCLK/SWDIO/NRST 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Encoder | `controller=U2 STM32F030F4P6`；`encoder=J2 Rotary encode`；`inputs=BTN,IN_A,IN_B`；`rgb=LED1,LED2 SK6812`；`communication=J1 SCL,SDA`；`power=+5V->U1 HT7533->+3.3V` |
| 电源 | U1 HT7533 | `input=VIN pin 2,+5V`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C3 22uF`；`output_capacitor=C4 22uF` |
| 电源 | U2 电源 | `vdda=pin 5,+3.3V`；`vdd=pin 16,+3.3V`；`vss=pin 15,GND`；`decoupling=C2 100nF` |
| 接口 | J1 HY-2.0_IIC | `pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC,+5V`；`pin_4=GND` |
| 总线 | U2 I2C | `controller=U2 STM32F030F4P6`；`scl=PA9 pin 17`；`sda=PA10 pin 18`；`pullups=R6/R7 10KΩ to +3.3V`；`connector=J1` |
| 总线地址 | Unit Encoder I2C 地址 | `controller=U2 STM32F030F4P6`；`schematic_address=null`；`address_selector=null`；`address_source_needed=internal firmware and protocol documentation` |
| GPIO 与控制信号 | U2 关键 GPIO | `PA0_pin6=SK6812`；`PA5_pin11=BTN`；`PA6_pin12=IN_A`；`PA7_pin13=IN_B`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK` |
| 核心器件 | J2 Rotary encode | `pin_1=b1,BTN`；`pin_2=b2,GND`；`pin_3=A,IN_A`；`pin_4=COM,GND`；`pin_5=B,IN_B` |
| GPIO 与控制信号 | BTN 按键输入 | `mcu_pin=U2 PA5 pin 11`；`pullup=R4 10KΩ to +3.3V`；`capacitor=C1 100nF to GND`；`button_contacts=J2 pins 1/2`；`pressed_logic=low` |
| GPIO 与控制信号 | IN_A/IN_B 编码输入 | `phase_a=J2.3 IN_A->U2 PA6 pin12`；`phase_a_pullup=R8 10KΩ`；`phase_a_cap=C6 100nF`；`phase_b=J2.5 IN_B->U2 PA7 pin13`；`phase_b_pullup=R9 10KΩ`；`phase_b_cap=C7 100nF`；`common=J2.4 GND` |
| 核心器件 | 旋转编码器每圈脉冲数 | `component=J2 Rotary encode`；`schematic_pulses_per_revolution=null`；`schematic_detents=null`；`schematic_phase_timing=null`；`specification_source_needed=encoder part specification or mechanical BOM` |
| 总线 | LED1/LED2 SK6812 级联 | `controller_pin=U2 PA0 pin 6`；`input_net=SK6812`；`first_led=LED1 DIN pin3`；`cascade=LED1 DOUT pin1->LED2 DIN pin3`；`chain_end=LED2 DOUT pin1 no-connect`；`count=2` |
| 电源 | LED1/LED2 供电 | `devices=LED1,LED2 SK6812`；`vdd=pin 4,+5V`；`vss=pin 2,GND`；`data_pullup=R1 10KΩ to +3.3V` |
| 复位 | U2 NRST | `mcu_pin=NRST pin 4`；`pullup=R5 10KΩ to +3.3V`；`capacitor=C5 100nF to GND`；`debug_header=P1 pin 4` |
| 复位 | U2 BOOT0 | `mcu_pin=BOOT0 pin 1`；`resistor=R3 10KΩ`；`strap=GND` |
| 调试与烧录 | P1 SWD_5p | `pin_1=+3.3V`；`pin_2=SWCLK,U2 PA14 pin20`；`pin_3=SWDIO,U2 PA13 pin19`；`pin_4=NRST,U2 pin4`；`pin_5=GND` |
| 时钟 | U2 PF0/PF1 时钟引脚 | `osc_in=PF0 pin 2 no-connect`；`osc_out=PF1 pin 3 no-connect`；`external_clock_component=null` |
| 接口 | 未使用的 U2 GPIO | `unused_pins=PA1.7,PA2.8,PA3.9,PA4.10,PB1.14` |
| 保护电路 | Grove 与编码器接口保护 | `grove_esd=null`；`encoder_esd=null`；`fuse=null`；`reverse_polarity=null` |
| 关键网络 | Unit Encoder 关键网络索引 | `encoder_inputs=J2.1/3/5-U2 PA5/PA6/PA7`；`rgb_path=U2 PA0-LED1-LED2`；`i2c_path=J1.1/2-U2 PA9/PA10`；`power_path=J1.3 +5V-U1-+3.3V`；`debug=P1 SWD` |

## 待确认事项

- `address.i2c-not-shown`：原理图显示 STM32 的 SCL/SDA 连接，但页面未打印 I2C 从机地址，且没有硬件地址选择网络。（证据：图 49167f49ddc2 / 第 1 页 / 页 1 U2/J1 SCL/SDA 区域，整页无 0x 地址或 ADDR 引脚）
- `component.encoder-resolution-not-shown`：原理图只显示 J2 的 A/B/COM 和按键触点，没有打印每圈脉冲数、机械定位数或相位时序。（证据：图 49167f49ddc2 / 第 1 页 / 页 1 J2 符号仅标 Rotary encode 与 A/COM/B/b1/b2，无脉冲数文字）
- `review.i2c-address`：Unit Encoder 当前固件使用的 I2C 从机地址是否为 0x40？；原因：地址由 STM32 固件实现，原理图未打印地址值或硬件选择电路。
- `review.encoder-resolution`：J2 编码器每圈脉冲数、机械定位数和 A/B 相时序是什么？；原因：原理图只给出通用 Rotary encode 符号与电气连接，没有器件型号或机械参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `49167f49ddc25e9dd166220d9c814e821b605754808cd1f851ce7d034e816c49` | `https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_sch_01.webp` |

---

源文档：`zh_CN/unit/encoder.md`

源文档 SHA-256：`57b284a05d6a388215cb20ca149dc983fe5f5796319bd5519e0d2f115de2537c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
