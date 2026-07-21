# Base26 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base26 |
| SKU | K026 |
| 产品 ID | `base26-5c79b1647571` |
| 源文档 | `zh_CN/base/base26.md` |

## 概述

Base26 主板原理图显示 TPS54360 降压电源把经 J1 和 F1 输入的 IN+ 转换为 +5V，并把 IN+、+5V、I2C 与多个电源或 GPIO 网络引到 J5 M5Stack_BUS。J4 是直接连接总线 SDA/SCL 的 Grove I2C 口；P1/J2 与 P2/J3 是两组彼此一一对应、但未固定接入 M5-Bus 的四针扩展接口。P3 只引出 B-、A+、12V+、12V-，本页没有 RS485 收发器或其到 UART 的固定连线。R2、R3 同时出现黑色与红色数值标注，输入范围文字也与源文档表述不同，均保留待确认。

## 检索关键词

`Base26`、`K026`、`TPS54360`、`IN12/24V`、`+5V`、`M5Stack_BUS`、`HPWR`、`Grove_IIC`、`Grove_UART`、`GPIO21`、`GPIO22`、`SDA`、`SCL`、`PWR3.5`、`PPTC-1812`、`B290B`、`8.2uH`、`B-`、`A+`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | PWR3.5 | 直流电源输入插座 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左上 IN12/24V 区域的 J1，器件值标注 PWR3.5 |
| F1 | PPTC-1812 | J1 与 IN+ 之间的串联自恢复保险丝 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左上 J1 右侧 F1，标注 PPTC-1812，串联到 IN+ |
| U1 | TPS54360 | IN+ 到 +5V 的开关降压控制器 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左上 U1 方框，下方器件型号标注 TPS54360 |
| D1 | B290B | TPS54360 开关节点与 GND 之间的续流二极管 | 图 c6a096991cf2 / 第 1 页 / 第 1 页上方中左 D1，标注 B290B，连接 SW 节点与 GND |
| L1 | 8.2uH | TPS54360 降压输出电感 | 图 c6a096991cf2 / 第 1 页 / 第 1 页上方 L1，连接 SW 节点与 +5V，数值标注 8.2uH |
| C1,C2,C3,C4,C5,C6 | 100nF / 10uF / 10uF / 6.8nF / 2.2uF / 2.2uF | TPS54360 的自举、输入输出滤波和补偿电容 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左上电源区，C1=100nF、C2/C3=10uF、C4=6.8nF、C5/C6=2.2uF |
| R1,R2,R3,R4 | 12KΩ / 51KΩ(红字 52.6K) / 160KΩ(红字 162K) / 10KΩ | TPS54360 的补偿、反馈和 RT/CLK 配置电阻 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左上 U1 周围 R1-R4；R2、R3 旁另有红色 52.6K、162K 标注 |
| D2,R5 | 红灯 0603 / 4.7KΩ | +5V 电源指示支路 | 图 c6a096991cf2 / 第 1 页 / 第 1 页右中部 D2 红灯 0603 与 R5 4.7KΩ，串联在 +5V 与 GND 之间 |
| P1,J2 | Header 4 / Grove_UART | RX、TX、VCC、GND 的一一对应扩展接口对 | 图 c6a096991cf2 / 第 1 页 / 第 1 页右上 P1 Header 4 与 J2 Grove_UART，四根导线一一对应 |
| P2,J3 | Header 4 / Grove_IIC | IIC_SCL、IIC_SDA、VCC、GND 的一一对应扩展接口对 | 图 c6a096991cf2 / 第 1 页 / 第 1 页右上 P2 Header 4 与 J3 Grove_IIC，四根导线一一对应 |
| P3 | HDR_4P | B-、A+、12V+、12V- 四线接口 | 图 c6a096991cf2 / 第 1 页 / 第 1 页左下 P3 HDR_4P，左侧网络自上而下标注 B-、A+、12V+、12V- |
| J4 | Grove_IIC | 直接连接 J5 SDA/SCL、+5V 和 GND 的 Grove I2C 接口 | 图 c6a096991cf2 / 第 1 页 / 第 1 页右中部 J4 Grove_IIC，pins1-4 接 SCL、SDA、+5V、GND |
| J5 | M5Stack_BUS | 30 针 M5Stack 堆叠总线接口 | 图 c6a096991cf2 / 第 1 页 / 第 1 页右下 J5 M5Stack_BUS，显示 pins1-30 的电源、GPIO、I2C、EN 与 BAT 标注 |

## 系统结构

### Base26 主板结构

本页由 TPS54360 降压电源、J5 M5Stack_BUS、J4 直连 I2C Grove、两组 Header/Grove 接口对、P3 四线接口和 +5V 指示灯组成。

- 参数与网络：`buck_controller=U1 TPS54360`；`stack_bus=J5 M5Stack_BUS`；`direct_i2c_grove=J4`；`optional_header_grove_pairs=P1/J2,P2/J3`；`four_wire_header=P3`；`power_indicator=D2,R5`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页全图：左上电源、左下 P3、右上 P1/J2 与 P2/J3、右中 J4/D2、右下 J5

## 电源

### J1 输入与 IN+ 网络

J1 PWR3.5 的正向输入路径经 F1 PPTC-1812 串联后形成 IN+；C5 和 C6 均为 2.2uF，并从 IN+ 接至 GND。

- 参数与网络：`input_connector=J1 PWR3.5`；`series_protection=F1 PPTC-1812`；`rail_after_fuse=IN+`；`input_capacitors=C5=2.2uF,C6=2.2uF`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左上 J1、F1、IN+、C5、C6 与 GND 连接区域

### TPS54360 降压主功率路径

U1 VIN pin2 接 IN+，SW pin8 经 L1 8.2uH 接 +5V；D1 B290B 接在 SW 节点与 GND 之间，C2 和 C3 各以 10uF 从 +5V 接至 GND。

- 参数与网络：`controller=U1 TPS54360`；`input=IN+`；`output=+5V`；`inductor=L1 8.2uH`；`diode=D1 B290B`；`output_capacitors=C2=10uF,C3=10uF`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左上 U1 pins2/8、D1、L1、C2、C3 与 +5V/GND 主功率回路

### TPS54360 自举、补偿与控制连接

C1 100nF 连接 U1 BOOT pin1 与 SW 节点；U1 COMP pin6 经 R1 12KΩ 接 C4 6.8nF 至 GND，FB pin5 位于 R2 与 R4 10KΩ 的分压节点，GND pin7 与 PWRPD pin9 接 GND，EN pin3 在图中标为未连接。

- 参数与网络：`bootstrap=C1=100nF between BOOT and SW`；`compensation=COMP -> R1 12KΩ -> C4 6.8nF -> GND`；`feedback_lower_resistor=R4 10KΩ`；`ground_pins=7,9`；`enable_pin=pin3 NC`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左上 U1 BOOT/COMP/FB/GND/PWRPD/EN 与 C1、R1、C4、R2、R4 连接区域

### +5V 指示灯

D2 标注为红灯 0603，并与 R5 4.7KΩ 串联在 +5V 和 GND 之间。

- 参数与网络：`led=D2 red 0603`；`series_resistor=R5 4.7KΩ`；`rail=+5V`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右中部 GND-R5-D2-+5V 串联支路

## 接口

### J5 GPIO 引脚标注

J5 左侧 pins7/9/11/13/15/19/21/23 依次标注 GPIO23/GPIO19/GPIO18/GPIO3/GPIO16/GPIO2/GPIO12/GPIO15；右侧 pins2/4/8/10/14/16/20/22/24/26 依次标注 GPIO35/GPIO36/GPIO25/GPIO26/GPIO1/GPIO17/GPIO5/GPIO13/GPIO0/GPIO34。

- 参数与网络：`odd_gpio_pins=7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,19:GPIO2,21:GPIO12,23:GPIO15`；`even_gpio_pins=2:GPIO35,4:GPIO36,8:GPIO25,10:GPIO26,14:GPIO1,16:GPIO17,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右下 J5 M5Stack_BUS 两侧的 GPIO 网络与 pin 编号

### P1 与 J2 Grove_UART

P1 Header 4 的 pins1-4 与 J2 Grove_UART 的 pins1-4 一一对应，J2 端依次标注 RX、TX、VCC、GND；这四条线在本页未连接到 J5 或其他命名网络。

- 参数与网络：`pinout=1:RX,2:TX,3:VCC,4:GND`；`m5_bus_connection_shown=false`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右上 P1 与 J2 Grove_UART 的四条短连线，区域外无延伸网络

### P2 与 J3 Grove_IIC

P2 Header 4 的 pins1-4 与 J3 Grove_IIC 的 pins1-4 一一对应，J3 端依次标注 IIC_SCL、IIC_SDA、VCC、GND；这四条线在本页未连接到 J5 或其他命名网络。

- 参数与网络：`pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND`；`m5_bus_connection_shown=false`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右上 P2 与 J3 Grove_IIC 的四条短连线，区域外无延伸网络

### P3 四线接口

P3 HDR_4P 自上而下的四条网络为 B-、A+、12V+、12V-；这些网络在本页没有连接到 U1、J5、P1/J2 或其他电路。

- 参数与网络：`pinout_top_to_bottom=B-,A+,12V+,12V-`；`other_connections_shown=false`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左下 P3 HDR_4P 及其四条独立网络标签

## 总线

### J5 电源与控制引脚

J5 pins1/3/5 接 GND，pins25/27/29 为 HPWR 并接 IN+，pin28 接 +5V，pin12 接 +3.3V，pin30 接 BAT，pin6 为 EN。

- 参数与网络：`ground=1,3,5`；`hpwr=25,27,29 -> IN+`；`five_volt=28 -> +5V`；`three_volt_three=12 -> +3.3V`；`battery=30 -> BAT`；`enable=6 -> EN`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右下 J5 pins1/3/5/6/12/25/27/28/29/30 及外部 IN+、+5V、+3.3V、BAT、GND 网络

### J5 到 J4 的 I2C Grove 连接

J5 pin17 的 GPIO21 接 SDA，pin18 的 GPIO22 接 SCL；J4 pins1-4 依次连接 IIC_SCL、IIC_SDA、+5V、GND。

- 参数与网络：`sda=J5 pin17 GPIO21 -> J4 pin2 IIC_SDA`；`scl=J5 pin18 GPIO22 -> J4 pin1 IIC_SCL`；`supply=J4 pin3 +5V`；`ground=J4 pin4 GND`
- 证据：图 c6a096991cf2 / 第 1 页 / 第 1 页右侧 J5 pins17/18 的 SDA/SCL 网络及 J4 Grove_IIC pins1-4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base26 主板结构 | `buck_controller=U1 TPS54360`；`stack_bus=J5 M5Stack_BUS`；`direct_i2c_grove=J4`；`optional_header_grove_pairs=P1/J2,P2/J3`；`four_wire_header=P3`；`power_indicator=D2,R5` |
| 电源 | J1 输入与 IN+ 网络 | `input_connector=J1 PWR3.5`；`series_protection=F1 PPTC-1812`；`rail_after_fuse=IN+`；`input_capacitors=C5=2.2uF,C6=2.2uF` |
| 电源 | TPS54360 降压主功率路径 | `controller=U1 TPS54360`；`input=IN+`；`output=+5V`；`inductor=L1 8.2uH`；`diode=D1 B290B`；`output_capacitors=C2=10uF,C3=10uF` |
| 电源 | TPS54360 自举、补偿与控制连接 | `bootstrap=C1=100nF between BOOT and SW`；`compensation=COMP -> R1 12KΩ -> C4 6.8nF -> GND`；`feedback_lower_resistor=R4 10KΩ`；`ground_pins=7,9`；`enable_pin=pin3 NC` |
| 电源 | R2 与 R3 数值标注 | `r2_black=51KΩ`；`r2_red=52.6K`；`r3_black=160KΩ`；`r3_red=162K`；`selected_values=null` |
| 电源 | 外部输入电压范围 | `schematic_label=IN12/24V`；`source_document_claim=9~24V`；`confirmed_range=null` |
| 电源 | +5V 指示灯 | `led=D2 red 0603`；`series_resistor=R5 4.7KΩ`；`rail=+5V` |
| 总线 | J5 电源与控制引脚 | `ground=1,3,5`；`hpwr=25,27,29 -> IN+`；`five_volt=28 -> +5V`；`three_volt_three=12 -> +3.3V`；`battery=30 -> BAT`；`enable=6 -> EN` |
| 总线 | J5 到 J4 的 I2C Grove 连接 | `sda=J5 pin17 GPIO21 -> J4 pin2 IIC_SDA`；`scl=J5 pin18 GPIO22 -> J4 pin1 IIC_SCL`；`supply=J4 pin3 +5V`；`ground=J4 pin4 GND` |
| 接口 | J5 GPIO 引脚标注 | `odd_gpio_pins=7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,19:GPIO2,21:GPIO12,23:GPIO15`；`even_gpio_pins=2:GPIO35,4:GPIO36,8:GPIO25,10:GPIO26,14:GPIO1,16:GPIO17,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34` |
| 接口 | P1 与 J2 Grove_UART | `pinout=1:RX,2:TX,3:VCC,4:GND`；`m5_bus_connection_shown=false` |
| 接口 | P2 与 J3 Grove_IIC | `pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND`；`m5_bus_connection_shown=false` |
| 接口 | P3 四线接口 | `pinout_top_to_bottom=B-,A+,12V+,12V-`；`other_connections_shown=false` |
| 接口 | RS485 转接实现 | `transceiver_shown=false`；`direction_control_shown=false`；`termination_shown=false`；`p3_to_uart_link_shown=false`；`external_board_wiring=null` |

## 待确认事项

- `power.r2_r3_values`：图中 R2 的黑色数值为 51KΩ、旁边红字为 52.6K；R3 的黑色数值为 160KΩ、旁边红字为 162K，单页未说明哪组数值对应最终装配版本。（证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左上 U1 下方 R2、R3 的黑色器件值及相邻红色修订文字）
- `power.input_range`：原理图标题只标注 IN12/24V，没有给出连续输入范围、容差或工作边界；仅据该页无法确认源文档所写的 9~24V 输入规格。（证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左上电源输入区域仅见 IN12/24V 文字）
- `interface.rs485_implementation`：源文档称套件提供 TTL/RS485 转接板，但当前主板原理图仅显示 P3 的 B-/A+/12V+/12V- 与独立 P1/J2 UART 接口对，没有显示 RS485 收发器、方向控制、端接网络或两者之间的固定连线。（证据：图 c6a096991cf2 / 第 1 页 / 第 1 页左下 P3、右上 P1/J2 及全页器件范围，未见 RS485 收发器或互连网络）
- `review.r2_r3_values`：Base26 当前量产版本的 R2 与 R3 应采用黑色标注值还是红色修订值？；原因：同一页同时显示 R2 51KΩ/红字 52.6K 和 R3 160KΩ/红字 162K，图框没有解释修订状态。
- `review.input_range`：Base26 当前硬件版本经验证的外部直流输入范围是否为 9~24V？；原因：源文档写 9~24V，原理图只写 IN12/24V；本页没有连续范围、容差或边界条件。
- `review.rs485_wiring`：套件所配 TTL/RS485 转接板的型号、供电与 P3/P1/J2 之间的实际接线方式是什么？；原因：当前主板原理图没有画出转接板内部电路，也没有给出 P3 到 UART 接口或 M5-Bus GPIO 的固定连线。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c6a096991cf2f5c50fd49cd288c2bbc034dcaaae4c0ae79c4d1457989a2f7f2a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1003/K026-BASE26_page_01.png` |

---

源文档：`zh_CN/base/base26.md`

源文档 SHA-256：`30fb23cff75fea66e4b254015d81cec4a2db3e1d094ef300a13928965d8813ed`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
