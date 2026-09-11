# Faces_Gamepad3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces_Gamepad3 |
| SKU | A004-V3 |
| 产品 ID | `faces-gamepad3-674f9085ab88` |
| 源文档 | `zh_CN/faces/Faces_Gamepad3.md` |

## 概述

Faces_Gamepad3 是一块以 STM32F030F4P6 为核心的八按键输入板，S1-S8 分别连接 PA0-PA7，并由两组 4.7KΩ 电阻阵列上拉到 +3.3V。J2 M5_BUS_22P 引出 +5V、+3.3V、GND、SDA、SCL、G35 及 UART2_RX/UART2_TX 标号网络，I2C 线另有 10KΩ 上拉。板上提供 5 针 SWD 接口、独立调试焊盘、BOOT0 下拉与 NRST RC 网络；PF0/PF1 未画外部时钟电路。

## 检索关键词

`Faces_Gamepad3`、`Faces Gamepad3`、`A004-V3`、`STM32F030F4P6`、`U1`、`S1-S8`、`SW-PB`、`PA0-PA7`、`RP1`、`RP2`、`4.7KΩ`、`M5_BUS_22P`、`J2`、`SDA`、`SCL`、`I2C`、`PA10`、`PA9`、`G35`、`PB1`、`UART2_RX`、`UART2_TX`、`U1_TX`、`U1_RX`、`SWD`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`+3.3V`、`+5V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 连接八路按键、I2C、G35、SWD、复位及串口测试网络的主控制器 | 图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 器件框及其 1-20 脚网络标注 |
| S1-S8 | SW-PB | 八个常开按键，分别在闭合时将 PA0-PA7 接到 GND | 图 938d340dd3b4 / 第 1 页 / 网格 A2-B4，S1-S8 的 PA0-PA7 与 GND 连接 |
| RP1, RP2 | 4.7KΩ (472) ±5% | 将 PA0-PA7 分组上拉到 +3.3V 的四联电阻阵列 | 图 938d340dd3b4 / 第 1 页 / 网格 A1-B1，RP1/RP2 数值及 PA0-PA7 网络标注 |
| J2 | M5_BUS_22P | 承载电源、I2C、G35 和 UART2 标号网络的 22 针主机接口 | 图 938d340dd3b4 / 第 1 页 / 网格 D3-D4，J2 M5_BUS_22P 引脚与外接网络 |
| P1 | SWD_5p | 提供 +3.3V、SWCLK、SWDIO、NRST 和 GND 的 5 针调试接口 | 图 938d340dd3b4 / 第 1 页 / 网格 D2，P1 SWD_5p 的 1-5 脚标注 |
| R1 | 10KΩ | 把 G35 网络上拉到 +3.3V | 图 938d340dd3b4 / 第 1 页 / 网格 D3，J2 左上方 R1 与 G35、+3.3V 连接 |
| R3 | 10KΩ | 把 U1 BOOT0 下拉到 GND | 图 938d340dd3b4 / 第 1 页 / 网格 C1-C2，R3 位于 U1 BOOT0 与 GND 之间 |
| R4 | 10KΩ | 把 NRST 上拉到 +3.3V | 图 938d340dd3b4 / 第 1 页 / 网格 C1，R4 位于 +3.3V 与 NRST 之间 |
| C5 | 100nF | +3.3V 与 GND 之间的旁路电容 | 图 938d340dd3b4 / 第 1 页 / 网格 C1，C5 连接 +3.3V 与 GND |
| C6 | 100nF | NRST 与 GND 之间的复位电容 | 图 938d340dd3b4 / 第 1 页 / 网格 C1，C6 连接 NRST 与 GND |
| R5, R6 | 10KΩ | 分别把 SDA 和 SCL 上拉到 +3.3V | 图 938d340dd3b4 / 第 1 页 / 网格 D4，J2 的 SDA/SCL 右侧 R5/R6 |
| JP1-JP3, JP9-JP10 | 未标注 | 引出 SWCLK、SWDIO、NRST、U1_TX 和 U1_RX 的单点焊盘或测试点 | 图 938d340dd3b4 / 第 1 页 / 网格 D1，JP1-JP3 与 JP9-JP10 网络标签 |
| JP4-JP8 | 未标注 | 引出 +5V、两路 +3.3V 和两路 GND 的电源焊盘或测试点 | 图 938d340dd3b4 / 第 1 页 / 网格 D1，JP4-JP8 下方电源与地标注 |

## 系统结构

### 整板架构

该原理图页由 U1 STM32F030F4P6、八个按键、M5_BUS_22P 接口、SWD 调试口以及启动和复位网络构成。

- 参数与网络：`mcu=U1 STM32F030F4P6`；`button_count=8`；`host_connector=J2 M5_BUS_22P`；`debug_connector=P1 SWD_5p`
- 证据：图 938d340dd3b4 / 第 1 页 / 整页，网格 A1-D4 的主要功能分区

## 核心器件

### U1

U1 的器件标注为 STM32F030F4P6，封装符号给出 20 个引脚。

- 参数与网络：`reference=U1`；`part_number=STM32F030F4P6`；`pin_count_shown=20`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 器件框底部型号及 1-20 脚编号

### RP1 与 RP2

RP1 和 RP2 均标注为四联 4.7KΩ (472) ±5% 电阻阵列。

- 参数与网络：`references=RP1, RP2`；`resistance=4.7KΩ`；`code=472`；`tolerance=±5%`；`resistors_per_array=4`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 A1-B1，RP1/RP2 符号与数值标注

## 电源

### 按键上拉供电

RP1 的公共侧连接 +3.3V，分别上拉 PA0-PA3；RP2 的公共侧连接同一 +3.3V 网络，分别上拉 PA4-PA7。

- 参数与网络：`rail=+3.3V`；`rp1_nets=PA0, PA1, PA2, PA3`；`rp2_nets=PA4, PA5, PA6, PA7`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 A1-B1，+3.3V 公共母线及 RP1/RP2 两侧网络

### SDA/SCL 上拉

R5 与 R6 均为 10KΩ，分别把 SDA 和 SCL 上拉到 +3.3V。

- 参数与网络：`sda_pullup=R5 10KΩ to +3.3V`；`scl_pullup=R6 10KΩ to +3.3V`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D4，J2 15/17 脚右侧 R5/R6 与 +3.3V

### G35 上拉

R1 为 10KΩ，并连接在 +3.3V 与 G35 之间；GND 到 J2 2 脚的导线以跨线桥越过 R1/G35 支路，不与其相连。

- 参数与网络：`reference=R1`；`resistance=10KΩ`；`rail=+3.3V`；`net=G35`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D3，R1/G35 支路与 J2 2 脚 GND 跨线桥

### U1 供电脚

U1 的 VDDA/5 脚和 VDD/16 脚连接 +3.3V，VSS/15 脚连接 GND。

- 参数与网络：`analog_supply=VDDA pin 5 = +3.3V`；`digital_supply=VDD pin 16 = +3.3V`；`ground=VSS pin 15 = GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 VDDA/VDD/VSS 引脚连接

### +3.3V 旁路

C5 为 100nF，直接连接在 +3.3V 与 GND 之间。

- 参数与网络：`reference=C5`；`capacitance=100nF`；`between=+3.3V and GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C1，C5 与上下电源符号

### JP4-JP8 电源焊盘

JP4 引出 +5V，JP5 和 JP6 引出 +3.3V，JP7 和 JP8 引出 GND。

- 参数与网络：`mapping=JP4=+5V; JP5=+3.3V; JP6=+3.3V; JP7=GND; JP8=GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D1，JP4-JP8 下方电源标签

## 接口

### J2 I2C 引脚

J2 的 15 脚标为 SDA，17 脚标为 SCL，并通过同名网络连接到 U1。

- 参数与网络：`connector=J2 M5_BUS_22P`；`sda_pin=15`；`scl_pin=17`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D3-D4，J2 15/17 脚及 SDA/SCL 网络

### J2 电源引脚

J2 的 1 脚连接 +5V，3 脚连接 +3.3V，2 脚连接 GND。

- 参数与网络：`pin_1=+5V`；`pin_2=GND`；`pin_3=+3.3V`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D3-D4，J2 顶部 1-3 脚电源网络

### J2 UART2 标号网络

J2 的 R2/16 对应 11 脚接 UART2_RX，T2/17 对应 13 脚接 UART2_TX。

- 参数与网络：`uart2_rx=J2 R2/16, pin 11`；`uart2_tx=J2 T2/17, pin 13`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D4，J2 11/13 脚右侧 UART2_RX/UART2_TX 网络标签

### J2 未外接引脚

本页未画出 J2 的 5、6、7、8、9、10、12、14、16、18、19、20、21、22 脚到板内其他网络的连接。

- 参数与网络：`pins_without_drawn_board_net=5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 19, 20, 21, 22`；`connector_labels=MOSI, AD36, MISO, DA25, SCK, DA26, SK, WS, OUT, MK, G2, IN, G5, HRR`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D3-D4，J2 对应引脚仅有短引线且无板内网络标签

### U1_TX/U1_RX 测试网络

U1 的 PA2/8 脚标为 U1_TX 并引到 JP9，PA3/9 脚标为 U1_RX 并引到 JP10。

- 参数与网络：`tx=U1 PA2, pin 8 -> U1_TX -> JP9`；`rx=U1 PA3, pin 9 -> U1_RX -> JP10`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2 的 U1 PA2/PA3 网络与网格 D1 的 JP9/JP10

## 总线

### U1 I2C 网络

U1 的 PA10/18 脚连接 SDA，PA9/17 脚连接 SCL。

- 参数与网络：`sda=U1 PA10, pin 18`；`scl=U1 PA9, pin 17`；`nets=SDA, SCL`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 右侧 PA10/18=SDA 与 PA9/17=SCL

## GPIO 与控制信号

### S1-S8 按键网络

S1-S8 依次连接 PA0、PA1、PA2、PA3、PA4、PA5、PA6、PA7，每个按键另一端接 GND。

- 参数与网络：`mapping=S1=PA0; S2=PA1; S3=PA2; S4=PA3; S5=PA4; S6=PA5; S7=PA6; S8=PA7`；`common_terminal=GND`；`switch_type=SW-PB`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 A2-B4，S1-S8 两端网络标签

### G35 网络

U1 的 PB1/14 脚连接 G35，同名网络到达 J2 的 AD35/4 脚。

- 参数与网络：`mcu_pin=U1 PB1, pin 14`；`connector_pin=J2 AD35, pin 4`；`net=G35`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2 的 U1 PB1/14=G35 与网格 D3 的 J2 AD35/4=G35

### BOOT0

U1 的 BOOT0/1 脚通过 R3 10KΩ 下拉到 GND。

- 参数与网络：`mcu_pin=U1 BOOT0, pin 1`；`pulldown=R3 10KΩ to GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C1-C2，GND-R3-U1 BOOT0 连线

## 时钟

### U1 PF0/PF1 时钟脚

U1 的 PF0/OSC_IN/2 脚和 PF1/OSC_OUT/3 脚在本页未画外部连接，原理图中也未出现外部晶振或谐振器件。

- 参数与网络：`osc_in=U1 PF0/OSC_IN, pin 2, no drawn connection`；`osc_out=U1 PF1/OSC_OUT, pin 3, no drawn connection`；`external_oscillator_shown=false`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 2/3 脚短引线及整页器件检查

## 复位

### NRST 偏置与滤波

NRST 通过 R4 10KΩ 上拉到 +3.3V，并通过 C6 100nF 接到 GND；该网络连接 U1 的 NRST/4 脚。

- 参数与网络：`mcu_pin=U1 NRST, pin 4`；`pullup=R4 10KΩ to +3.3V`；`capacitor=C6 100nF to GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C1-C2，R4/C6/NRST 与 U1 4 脚

### NRST 外部访问

NRST 同时引到 P1 的 4 脚和 JP3。

- 参数与网络：`swd_header=P1 pin 4`；`breakout=JP3`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D1-D2，JP3 与 P1 4 脚的 NRST 标签

## 关键网络

### PA0-PA7 按键电平

PA0-PA7 分别由 4.7KΩ 电阻上拉到 +3.3V，按键闭合时对应网络接地，因此图面电路形成低有效按键输入。

- 参数与网络：`idle_bias=+3.3V through 4.7KΩ`；`pressed_level=GND`；`logic=active-low`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 A1-B4，RP1/RP2 上拉与 S1-S8 接地支路

## 调试与烧录

### U1 SWD 信号

U1 的 PA14/20 脚连接 SWCLK，PA13/19 脚连接 SWDIO。

- 参数与网络：`swclk=U1 PA14, pin 20`；`swdio=U1 PA13, pin 19`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 C2，U1 右上角 PA14/20=SWCLK 与 PA13/19=SWDIO

### P1 SWD_5p

P1 的 1-5 脚依次为 +3.3V、SWCLK、SWDIO、NRST 和 GND。

- 参数与网络：`pin_map=1=+3.3V; 2=SWCLK; 3=SWDIO; 4=NRST; 5=GND`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D2，P1 SWD_5p 连接器引脚表

### 调试信号焊盘

JP1、JP2、JP3 分别引出 SWCLK、SWDIO、NRST。

- 参数与网络：`mapping=JP1=SWCLK; JP2=SWDIO; JP3=NRST`
- 证据：图 938d340dd3b4 / 第 1 页 / 网格 D1，JP1-JP3 及其网络标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `mcu=U1 STM32F030F4P6`；`button_count=8`；`host_connector=J2 M5_BUS_22P`；`debug_connector=P1 SWD_5p` |
| 核心器件 | U1 | `reference=U1`；`part_number=STM32F030F4P6`；`pin_count_shown=20` |
| GPIO 与控制信号 | S1-S8 按键网络 | `mapping=S1=PA0; S2=PA1; S3=PA2; S4=PA3; S5=PA4; S6=PA5; S7=PA6; S8=PA7`；`common_terminal=GND`；`switch_type=SW-PB` |
| 关键网络 | PA0-PA7 按键电平 | `idle_bias=+3.3V through 4.7KΩ`；`pressed_level=GND`；`logic=active-low` |
| 核心器件 | RP1 与 RP2 | `references=RP1, RP2`；`resistance=4.7KΩ`；`code=472`；`tolerance=±5%`；`resistors_per_array=4` |
| 电源 | 按键上拉供电 | `rail=+3.3V`；`rp1_nets=PA0, PA1, PA2, PA3`；`rp2_nets=PA4, PA5, PA6, PA7` |
| 总线 | U1 I2C 网络 | `sda=U1 PA10, pin 18`；`scl=U1 PA9, pin 17`；`nets=SDA, SCL` |
| 接口 | J2 I2C 引脚 | `connector=J2 M5_BUS_22P`；`sda_pin=15`；`scl_pin=17` |
| 电源 | SDA/SCL 上拉 | `sda_pullup=R5 10KΩ to +3.3V`；`scl_pullup=R6 10KΩ to +3.3V` |
| GPIO 与控制信号 | G35 网络 | `mcu_pin=U1 PB1, pin 14`；`connector_pin=J2 AD35, pin 4`；`net=G35` |
| 电源 | G35 上拉 | `reference=R1`；`resistance=10KΩ`；`rail=+3.3V`；`net=G35` |
| 接口 | J2 电源引脚 | `pin_1=+5V`；`pin_2=GND`；`pin_3=+3.3V` |
| 接口 | J2 UART2 标号网络 | `uart2_rx=J2 R2/16, pin 11`；`uart2_tx=J2 T2/17, pin 13` |
| 接口 | J2 未外接引脚 | `pins_without_drawn_board_net=5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 19, 20, 21, 22`；`connector_labels=MOSI, AD36, MISO, DA25, SCK, DA26, SK, WS, OUT, MK, G2, IN, G5, HRR` |
| 调试与烧录 | U1 SWD 信号 | `swclk=U1 PA14, pin 20`；`swdio=U1 PA13, pin 19` |
| 调试与烧录 | P1 SWD_5p | `pin_map=1=+3.3V; 2=SWCLK; 3=SWDIO; 4=NRST; 5=GND` |
| 调试与烧录 | 调试信号焊盘 | `mapping=JP1=SWCLK; JP2=SWDIO; JP3=NRST` |
| 接口 | U1_TX/U1_RX 测试网络 | `tx=U1 PA2, pin 8 -> U1_TX -> JP9`；`rx=U1 PA3, pin 9 -> U1_RX -> JP10` |
| 复位 | NRST 偏置与滤波 | `mcu_pin=U1 NRST, pin 4`；`pullup=R4 10KΩ to +3.3V`；`capacitor=C6 100nF to GND` |
| 复位 | NRST 外部访问 | `swd_header=P1 pin 4`；`breakout=JP3` |
| GPIO 与控制信号 | BOOT0 | `mcu_pin=U1 BOOT0, pin 1`；`pulldown=R3 10KΩ to GND` |
| 时钟 | U1 PF0/PF1 时钟脚 | `osc_in=U1 PF0/OSC_IN, pin 2, no drawn connection`；`osc_out=U1 PF1/OSC_OUT, pin 3, no drawn connection`；`external_oscillator_shown=false` |
| 电源 | U1 供电脚 | `analog_supply=VDDA pin 5 = +3.3V`；`digital_supply=VDD pin 16 = +3.3V`；`ground=VSS pin 15 = GND` |
| 电源 | +3.3V 旁路 | `reference=C5`；`capacitance=100nF`；`between=+3.3V and GND` |
| 电源 | JP4-JP8 电源焊盘 | `mapping=JP4=+5V; JP5=+3.3V; JP6=+3.3V; JP7=GND; JP8=GND` |
| 总线地址 | I2C 地址 0x08 | `document_claim=I2C @ 0x08`；`schematic_address_label=null`；`verification_needed=firmware protocol or authoritative specification` |
| GPIO 与控制信号 | 八个按键的物理功能 | `schematic_labels=S1-S8`；`gpio_labels=PA0-PA7`；`document_layout=方向键、A/B、开始/选择`；`missing_mapping=physical key name to S1-S8` |
| GPIO 与控制信号 | G35 的 INT 语义 | `schematic_net=G35`；`schematic_path=U1 PB1/14 -> J2 AD35/4`；`document_label=INT` |
| 接口 | U1 串口与 J2 UART2 网络关系 | `u1_nets=U1_TX, U1_RX`；`j2_nets=UART2_RX, UART2_TX`；`drawn_connection=false` |

## 待确认事项

- `address.i2c-0x08`：源文档声明 I2C 通信地址为 0x08，但原理图页只显示 SDA/SCL 电气连接，没有地址标注或可推导该地址的硬件配置。（证据：图 938d340dd3b4 / 第 1 页 / 网格 C2 与 D4，U1/J2 的 SDA、SCL 连接；整页无数值地址标注）
- `gpio.button-semantic-map`：源文档把八键描述为方向键、A/B、开始/选择，但原理图仅标 S1-S8 与 PA0-PA7，未给出每个位号对应的面板按键名称。（证据：图 938d340dd3b4 / 第 1 页 / 网格 A2-B4，按键仅标 S1-S8、SW-PB 和 PA0-PA7）
- `gpio.g35-interrupt-role`：源文档管脚表列出 INT，但原理图把 U1 PB1 到 J2 AD35/4 脚的网络标为 G35，未直接标注 INT，因此该网络的中断用途需结合接口定义确认。（证据：图 938d340dd3b4 / 第 1 页 / 网格 C2 与 D3，PB1/14、G35、J2 AD35/4 标注）
- `interface.uart-network-relationship`：U1 侧网络名为 U1_TX/U1_RX，J2 侧网络名为 UART2_RX/UART2_TX；本页没有画出两组网络之间的连接，不能据此确认 J2 UART2 与 U1 串口相连。（证据：图 938d340dd3b4 / 第 1 页 / 网格 C2/D1 的 U1_TX/U1_RX 与网格 D4 的 UART2_RX/UART2_TX 标签对照）
- `review.i2c-0x08`：当前固件使用的 7-bit I2C 地址是否确定为 0x08？；原因：0x08 只出现在源文档规格表，原理图没有地址标注或硬件地址配置。
- `review.button-semantic-map`：S1-S8 分别对应哪一个方向键、A/B、开始和选择按键？；原因：原理图只给出位号与 PA0-PA7 映射，没有面板丝印或物理键名。
- `review.g35-interrupt-role`：G35/PB1 到 J2 AD35/4 的网络是否就是源文档所称的 INT 信号？；原因：图面网络名为 G35，没有 INT 标签，需由接口定义或固件确认语义。
- `review.uart-network-relationship`：J2 的 UART2_RX/UART2_TX 是否应与 U1_TX/U1_RX 相连，或仅是总线贯通信号？；原因：两组网络标签不同，当前原理图没有绘制它们之间的连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `938d340dd3b412fd3241291ead1adea5dfd984a721c03a9cd3ec1e8168a5221d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_Sche_page_01.png` |

---

源文档：`zh_CN/faces/Faces_Gamepad3.md`

源文档 SHA-256：`2fa18ce68dc2a570baccb201a4ae476e836959d06c3a1197112162a67e6a557e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
