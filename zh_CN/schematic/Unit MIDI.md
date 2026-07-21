# Unit MIDI 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit MIDI |
| SKU | U187 |
| 产品 ID | `unit-midi-8013566d6639` |
| 源文档 | `zh_CN/unit/Unit-MIDI.md` |

## 概述

Unit MIDI 以 U2 SAM2695 合成器为核心，UART_MIDI_OUT_EXT 经 R2 进入 MIDI_IN，AOUTL/AOUTR 经隔直电容和输出网络连接 J4 立体声音频插座。J2/J9 的 MIDI 输入通过 PC1 TLP2361 光耦隔离后形成 UART_MIDI_IN；SYS_MIDI_OUT 经 Q1 2N7002 驱动 J3/J10 的 MIDI 输出。J1 Grove 引出 UART_MIDI_OUT/UART_MIDI_IN 和 SYS_5V，S1 与 J5/J7 承载 EXT/系统 MIDI 路由。SYS_5V 经 U1 SE8533X2-H 生成 MCU_VDD，VDD_EXT 通过 J8 输入并为 SAM2695 供电；正文中的模式连通表、MIDI 参数、复音数和功耗未在原理图中直接标注。

## 检索关键词

`Unit MIDI`、`U187`、`SAM2695`、`TLP2361`、`2N7002`、`SE8533X2-H`、`MIDI IN`、`MIDI OUT`、`MIDI THRU`、`Bypass`、`Separate`、`UART_MIDI_IN`、`UART_MIDI_OUT`、`UART_MIDI_IN_EXT`、`UART_MIDI_OUT_EXT`、`SYS_MIDI_OUT`、`SYS_MIDI_OUT_EXT`、`MIDI_IN_REF`、`MIDI_IN_DAT`、`MIDI_OUT_REF`、`MIDI_OUT_DAT`、`AOUT_L`、`AOUT_R`、`SYN_L`、`SYN_R`、`PJ-342`、`DIN 5-pin`、`HY2.0-4P`、`31520bps`、`MIDI 1.0`、`16 channel`、`64 polyphony`、`38 polyphony`、`X1 12MHz`、`MCU_VDD`、`VDD_EXT`、`SYS_5V`、`LED_GREEN`、`optocoupler isolation`、`stereo audio output`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SAM2695 | MIDI 音频合成器，接收 UART MIDI 数据并输出左右模拟音频 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A2-B3，U2 SAM2695，MIDI_IN/AOUTL/AOUTR/晶振/数字与模拟电源 pins1-48 |
| U1 | SE8533X2-H | 将 SYS_5V 转换为 MCU_VDD 的稳压器 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A1，U1 SE8533X2-H，VIN/OUT/GND 与 C1/C2 |
| PC1 | TLP2361 | MIDI 输入电流环到 UART_MIDI_IN 逻辑域的光耦隔离器 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-A4，PC1 TLP2361，MCU_VDD/GND、UART_MIDI_IN 与 MIDI_IN_REF/DAT |
| Q1 | 2N7002 | 由 SYS_MIDI_OUT 控制的 MIDI 输出低侧开关 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-A4，Q1 2N7002 与 SYS_MIDI_OUT、MCU_VDD/R5、R10/MIDI_OUT_DAT |
| J1 | CON_HY2.0_4P_DIP_HOR_BLUE | Grove UART 与 SYS_5V/GND 接口 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 B1，J1 pin1 GND、pin2 SYS_5V、pin3 UART_MIDI_OUT、pin4 UART_MIDI_IN |
| J2,J3,J4 | PJ-342 | 3.5mm MIDI 输入、MIDI 输出和立体声音频输出插座 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A4-B4，J2 MIDI_IN_REF/DAT、J3 MIDI_OUT_REF/DAT、J4 AOUT_R/AOUT_L |
| J9,J10 | 1.25MM_7P | MIDI DIN 接口子板连接器，分别引出 MIDI IN 与 MIDI OUT 参考/数据线 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A4-B4，J9/J10 1.25MM_7P 的 pins4/5 接 MIDI_IN_REF/DAT 与 MIDI_OUT_REF/DAT |
| S1 | MS-22D16G3-B | UART_MIDI_IN_EXT、SYS_MIDI_OUT_EXT、UART_MIDI_OUT_EXT 三路模式切换开关 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 B3，S1 MS-22D16G3-B 双排 pins1-6，右侧 pins3/2/1 标注三路 EXT 网络 |
| X1,C3,C4 | TXM12M0004521BEC... / 20pF/50V / 20pF/50V | SAM2695 X1/X2 的 12MHz 晶振与负载电容网络 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 B2，X1 标注 TXM12M0004521BEC...，连接 U2 X1 pin39/X2 pin40，C3/C4 各 20pF/50V |
| LED1,R1 | LED_GREEN / 1K/1% | MCU_VDD 电源绿色指示灯 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 B1，MCU_VDD-R1 1K/1%-LED1 LED_GREEN-GND |
| D1,R8 | 1N4148WS / 220R/1% | MIDI 输入光耦 LED 的反向钳位与串联限流网络 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A4，J2 MIDI_IN_REF/DAT、R8 220R/1%、D1 1N4148WS 与 PC1 输入侧 |
| R9,R10,R11 | 220R/1% | SYS_5V/Q1 到 MIDI_OUT_REF/MIDI_OUT_DAT 的输出电流限制网络 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-B4，R9/R10/R11 220R/1% 位于 SYS_5V、Q1 与 J3/J10 MIDI OUT 路径 |
| J5,J7 | CON4 | 内部/EXT MIDI 信号互连连接器 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 C3，J5 UART_MIDI_OUT/SYS_MIDI_OUT/UART_MIDI_IN/GND 与 J7 对应 EXT 网络/GND |
| J6,J8 | CON2 | MCU_VDD 与 VDD_EXT 两路板间电源连接器 | 图 73356ab7e30b / 第 1 页 / 第 1 页网格 C3，J6 CON2 pin1 MCU_VDD，J8 CON2 pin1 VDD_EXT |

## 系统结构

### Unit MIDI 系统架构

U2 SAM2695 接收 UART_MIDI_OUT_EXT 并输出左右模拟音频；MIDI 输入由 J2/J9 经 PC1 TLP2361 隔离成 UART_MIDI_IN，MIDI 输出由 SYS_MIDI_OUT 经 Q1 驱动 J3/J10。S1 和 J5/J7 承载内部/EXT 信号切换，J1 提供 Grove UART 与 5V 电源。

- 参数与网络：`synth=U2 SAM2695`；`midi_input=J2/J9 -> PC1 -> UART_MIDI_IN`；`midi_output=SYS_MIDI_OUT -> Q1 -> J3/J10`；`audio=U2 AOUTL/AOUTR -> J4`；`selector=S1`；`host=J1 Grove UART`；`power=SYS_5V -> U1 -> MCU_VDD; J8 -> VDD_EXT`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页完整 A1-C4，U1/U2/PC1/Q1/J1-J10/S1 功能区

## 电源

### SYS_5V 至 MCU_VDD

J1 pin2 引入 SYS_5V，连接 U1 SE8533X2-H VIN；U1 OUT 输出 MCU_VDD，GND 接地。C1 10uF/10V 位于 SYS_5V 输入侧，C2 10uF/10V 位于 MCU_VDD 输出侧。

- 参数与网络：`input=J1 pin2 SYS_5V`；`regulator=U1 SE8533X2-H`；`output=MCU_VDD`；`input_cap=C1 10uF/10V`；`output_cap=C2 10uF/10V`；`ground=GND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A1 U1/C1/C2/SYS_5V/MCU_VDD 与 B1 J1

### SAM2695 数字与模拟电源域

U2 多个 VDD33 引脚（46/41/35/31/20/11/8）及 XDIV pin47 接 VDD_EXT，C5 47uF/10V、C10 10uF/10V、C11-C13 100nF/50V 对地去耦；VA33/VCM 使用 C8/C9 各 4.7uF/10V 对 AGND，R3 0Ω连接 GND 与 AGND。

- 参数与网络：`digital_rail=VDD_EXT`；`vdd_pins=46,41,35,31,20,11,8`；`xdiv=pin47 VDD_EXT`；`digital_caps=C5 47uF,C10 10uF,C11-C13 100nF`；`analog_caps=C8/C9 4.7uF to AGND`；`ground_bridge=R3 0R between GND and AGND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A2-B3，U2 VDD33/VA33/VCM/GND/AGND、C5/C8-C13/R3

## 接口

### J1 Grove UART 引脚

J1 CON_HY2.0_4P_DIP_HOR_BLUE pin1=GND、pin2=SYS_5V、pin3=UART_MIDI_OUT、pin4=UART_MIDI_IN。

- 参数与网络：`connector=J1`；`pin1=GND`；`pin2=SYS_5V`；`pin3=UART_MIDI_OUT`；`pin4=UART_MIDI_IN`；`signal_type=UART`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B1，J1 pins1-4 与四个网络标签

### MIDI IN 光耦隔离

J2/J9 的 MIDI_IN_REF 与 MIDI_IN_DAT 进入 PC1 TLP2361 输入侧，R8 220R/1% 串联限流，D1 1N4148WS 跨输入侧反向钳位；PC1 逻辑侧由 MCU_VDD 供电并经 R4 100R/1% 输出 UART_MIDI_IN。

- 参数与网络：`connectors=J2 PJ-342,J9 1.25MM_7P`；`input_nets=MIDI_IN_REF,MIDI_IN_DAT`；`opto=PC1 TLP2361`；`series=R8 220R/1%`；`reverse_diode=D1 1N4148WS`；`logic_supply=MCU_VDD`；`logic_output=PC1 -> R4 100R/1% -> UART_MIDI_IN`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-A4，J2/J9/R8/D1/PC1/R4/UART_MIDI_IN

### MIDI OUT 晶体管驱动

SYS_MIDI_OUT 控制 Q1 2N7002；MIDI_OUT_REF 由 SYS_5V 经 220R/1% 电阻网络驱动，Q1 开关节点经 R10 220R/1% 形成 MIDI_OUT_DAT，两个网络同时引到 J3 PJ-342 与 J10 1.25MM_7P。

- 参数与网络：`control=SYS_MIDI_OUT`；`transistor=Q1 2N7002`；`reference=SYS_5V via R9/R11 220R/1% -> MIDI_OUT_REF`；`data=Q1 via R10 220R/1% -> MIDI_OUT_DAT`；`connectors=J3,J10`；`bias=R5 100K/1% to MCU_VDD`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-B4，SYS_MIDI_OUT/Q1/R5/R9-R11/J3/J10

## 总线

### SAM2695 MIDI_IN 数据路径

UART_MIDI_OUT_EXT 经 R2 1K/1% 进入 U2 MIDI_IN pin16；U2 CS# pin14、RD# pin15 和 A0 pin10 接 GND，WR# pin12 接 VDD_EXT，D0-D7 并行数据引脚未外接。

- 参数与网络：`serial_input=UART_MIDI_OUT_EXT -> R2 1K/1% -> U2 pin16 MIDI_IN`；`cs=pin14 CS# -> GND`；`rd=pin15 RD# -> GND`；`wr=pin12 WR# -> VDD_EXT`；`a0=pin10 A0 -> GND`；`parallel_data=D0-D7 unconnected`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A2-B2，U2 MIDI_IN/CS#/RD#/WR#/A0/D0-D7 与 R2

## GPIO 与控制信号

### MCU_VDD 绿色指示灯

MCU_VDD 经 R1 1K/1% 和 LED1 LED_GREEN 串联到 GND，构成电源存在指示。

- 参数与网络：`rail=MCU_VDD`；`resistor=R1 1K/1%`；`led=LED1 LED_GREEN`；`return=GND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B1，MCU_VDD/R1/LED1/GND

## 时钟

### SAM2695 外部晶振

U2 X1 pin39 与 X2 pin40 连接 X1 晶振，器件文字以 TXM12M... 开头；C3/C4 各 20pF/50V 接 GND，晶振外壳/接地脚接 GND。

- 参数与网络：`synth=U2 SAM2695`；`pins=pin39 X1,pin40 X2`；`crystal=X1 TXM12M0004521BEC...`；`frequency_marking=12M in part marking`；`load_caps=C3/C4 20pF/50V`；`ground=GND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B2，U2 pins39/40、X1 TXM12M... 与 C3/C4

## 复位

### SAM2695 RST#/PD# 网络

U2 RST#/PD# pin38 由 R11 22K/1% 上拉到 VDD_EXT，并由 C14 1uF/10V 接 GND，形成上电复位/掉电控制网络。

- 参数与网络：`pin=U2 pin38 RST#/PD#`；`pullup=R11 22K/1% to VDD_EXT`；`capacitor=C14 1uF/10V to GND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B2，U2 pin38 RST#/PD#、R11、C14、VDD_EXT/GND

## 保护电路

### MIDI 输入隔离与反向保护

PC1 TLP2361 在 MIDI_IN_REF/DAT 电流环与 MCU_VDD/UART_MIDI_IN 逻辑域之间提供光电隔离；R8 220R/1% 限制输入电流，D1 1N4148WS 与光耦输入反向并联。

- 参数与网络：`isolation=PC1 TLP2361`；`field_side=MIDI_IN_REF,MIDI_IN_DAT`；`logic_side=MCU_VDD,GND,UART_MIDI_IN`；`series_resistor=R8 220R/1%`；`reverse_clamp=D1 1N4148WS`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A3-A4，PC1/R8/D1 与两侧网络

## 关键网络

### J5-J8 板间网络

J5 CON4 依次引出 UART_MIDI_OUT、SYS_MIDI_OUT、UART_MIDI_IN、GND；J7 CON4 依次引出 UART_MIDI_OUT_EXT、SYS_MIDI_OUT_EXT、UART_MIDI_IN_EXT、GND；J6/J8 分别引出 MCU_VDD 与 VDD_EXT。

- 参数与网络：`J5=pin1 UART_MIDI_OUT,pin2 SYS_MIDI_OUT,pin3 UART_MIDI_IN,pin4 GND`；`J7=pin1 UART_MIDI_OUT_EXT,pin2 SYS_MIDI_OUT_EXT,pin3 UART_MIDI_IN_EXT,pin4 GND`；`J6=pin1 MCU_VDD`；`J8=pin1 VDD_EXT`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 C3，J5/J7 CON4 与 J6/J8 CON2 网络标签

## 音频

### SAM2695 立体声音频输出

U2 AOUTL pin1 经 C6 10uF/10V 形成 SYN_L，再经 R7 10R/1% 到 J4 AOUT_L；AOUTR pin2 经 C7 10uF/10V 形成 SYN_R，再经 R6 10R/1% 到 J4 AOUT_R。R12/R13 各 1K/1% 将左右输出接至 AGND。

- 参数与网络：`left=U2 pin1 AOUTL -> C6 10uF -> SYN_L -> R7 10R -> J4 AOUT_L`；`right=U2 pin2 AOUTR -> C7 10uF -> SYN_R -> R6 10R -> J4 AOUT_R`；`loads=R12/R13 1K/1% to AGND`；`connector=J4 PJ-342`；`ground=AGND`
- 证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 A2-B4，U2 AOUTL/AOUTR/C6/C7/SYN_L/SYN_R/R6/R7/R12/R13/J4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit MIDI 系统架构 | `synth=U2 SAM2695`；`midi_input=J2/J9 -> PC1 -> UART_MIDI_IN`；`midi_output=SYS_MIDI_OUT -> Q1 -> J3/J10`；`audio=U2 AOUTL/AOUTR -> J4`；`selector=S1`；`host=J1 Grove UART`；`power=SYS_5V -> U1 -> MCU_VDD; J8 -> VDD_EXT` |
| 电源 | SYS_5V 至 MCU_VDD | `input=J1 pin2 SYS_5V`；`regulator=U1 SE8533X2-H`；`output=MCU_VDD`；`input_cap=C1 10uF/10V`；`output_cap=C2 10uF/10V`；`ground=GND` |
| 电源 | SAM2695 数字与模拟电源域 | `digital_rail=VDD_EXT`；`vdd_pins=46,41,35,31,20,11,8`；`xdiv=pin47 VDD_EXT`；`digital_caps=C5 47uF,C10 10uF,C11-C13 100nF`；`analog_caps=C8/C9 4.7uF to AGND`；`ground_bridge=R3 0R between GND and AGND` |
| 接口 | J1 Grove UART 引脚 | `connector=J1`；`pin1=GND`；`pin2=SYS_5V`；`pin3=UART_MIDI_OUT`；`pin4=UART_MIDI_IN`；`signal_type=UART` |
| 总线 | SAM2695 MIDI_IN 数据路径 | `serial_input=UART_MIDI_OUT_EXT -> R2 1K/1% -> U2 pin16 MIDI_IN`；`cs=pin14 CS# -> GND`；`rd=pin15 RD# -> GND`；`wr=pin12 WR# -> VDD_EXT`；`a0=pin10 A0 -> GND`；`parallel_data=D0-D7 unconnected` |
| 接口 | MIDI IN 光耦隔离 | `connectors=J2 PJ-342,J9 1.25MM_7P`；`input_nets=MIDI_IN_REF,MIDI_IN_DAT`；`opto=PC1 TLP2361`；`series=R8 220R/1%`；`reverse_diode=D1 1N4148WS`；`logic_supply=MCU_VDD`；`logic_output=PC1 -> R4 100R/1% -> UART_MIDI_IN` |
| 接口 | MIDI OUT 晶体管驱动 | `control=SYS_MIDI_OUT`；`transistor=Q1 2N7002`；`reference=SYS_5V via R9/R11 220R/1% -> MIDI_OUT_REF`；`data=Q1 via R10 220R/1% -> MIDI_OUT_DAT`；`connectors=J3,J10`；`bias=R5 100K/1% to MCU_VDD` |
| 音频 | SAM2695 立体声音频输出 | `left=U2 pin1 AOUTL -> C6 10uF -> SYN_L -> R7 10R -> J4 AOUT_L`；`right=U2 pin2 AOUTR -> C7 10uF -> SYN_R -> R6 10R -> J4 AOUT_R`；`loads=R12/R13 1K/1% to AGND`；`connector=J4 PJ-342`；`ground=AGND` |
| 时钟 | SAM2695 外部晶振 | `synth=U2 SAM2695`；`pins=pin39 X1,pin40 X2`；`crystal=X1 TXM12M0004521BEC...`；`frequency_marking=12M in part marking`；`load_caps=C3/C4 20pF/50V`；`ground=GND` |
| 复位 | SAM2695 RST#/PD# 网络 | `pin=U2 pin38 RST#/PD#`；`pullup=R11 22K/1% to VDD_EXT`；`capacitor=C14 1uF/10V to GND` |
| GPIO 与控制信号 | MCU_VDD 绿色指示灯 | `rail=MCU_VDD`；`resistor=R1 1K/1%`；`led=LED1 LED_GREEN`；`return=GND` |
| 关键网络 | J5-J8 板间网络 | `J5=pin1 UART_MIDI_OUT,pin2 SYS_MIDI_OUT,pin3 UART_MIDI_IN,pin4 GND`；`J7=pin1 UART_MIDI_OUT_EXT,pin2 SYS_MIDI_OUT_EXT,pin3 UART_MIDI_IN_EXT,pin4 GND`；`J6=pin1 MCU_VDD`；`J8=pin1 VDD_EXT` |
| 保护电路 | MIDI 输入隔离与反向保护 | `isolation=PC1 TLP2361`；`field_side=MIDI_IN_REF,MIDI_IN_DAT`；`logic_side=MCU_VDD,GND,UART_MIDI_IN`；`series_resistor=R8 220R/1%`；`reverse_clamp=D1 1N4148WS` |
| 接口 | 正文中的 Bypass/Separate 路由 | `switch=S1 MS-22D16G3-B`；`nets=UART_MIDI_IN_EXT,SYS_MIDI_OUT_EXT,UART_MIDI_OUT_EXT`；`documented_modes=Bypass,Separate`；`schematic_position_labels=null`；`contact_truth_table=null` |
| 总线 | 正文中的 MIDI/UART 参数 | `documented_protocol=MIDI 1.0`；`documented_channels=16`；`documented_baud=31520bps`；`schematic_baud=null`；`frame_format=null`；`serial_input=U2 pin16 MIDI_IN` |
| 音频 | 正文中的 SAM2695 复音数 | `synth=U2 SAM2695`；`documented_polyphony_dry=64`；`documented_polyphony_effects=38`；`schematic_polyphony=null`；`effects_configuration=null` |
| 电源 | 正文中的待机电流 | `documented_standby=DC 5V@18.59mA`；`schematic_current=null`；`mode_condition=null`；`tolerance=null` |
| 其他事实 | R11 重复位号 | `reference=R11`；`reset_value=22K/1%`；`reset_role=VDD_EXT to U2 pin38 RST#/PD#`；`midi_out_value=220R/1%`；`midi_out_role=SYS_5V/MIDI_OUT_REF network`；`bom_resolution=null` |

## 待确认事项

- `interface.documented-mode-routing`：正文描述 Bypass/Separate 两种模式下 INPUT、OUTPUT、Grove UART 与 SAM2695 的不同连通关系；原理图显示 S1 和 internal/EXT 网络，但未标开关位置名称、触点状态表或 Bypass/Separate 文字，无法仅凭本页确认每个物理档位对应关系。（证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B3 S1 与 J5/J7，图中无 Bypass/Separate 档位文字）
- `bus.documented-midi-protocol`：正文标称 MIDI 1.0、16 通道和 UART 31520bps；原理图只显示 UART/MIDI 电气网络与 SAM2695 MIDI_IN，没有协议版本、通道数、波特率或帧格式文字。（证据：图 73356ab7e30b / 第 1 页 / 第 1 页 U2 MIDI_IN 与 UART_MIDI_* 网络，无协议/波特率文字）
- `audio.documented-polyphony`：正文称 SAM2695 支持无效果 64 复音、带效果 38 复音；原理图只确认 U2 型号与音频输出，没有音色库、效果配置、复音数或输出性能参数。（证据：图 73356ab7e30b / 第 1 页 / 第 1 页 U2 SAM2695 与 AOUTL/AOUTR，图中无复音参数）
- `power.documented-standby-current`：正文标称待机电流 DC 5V@18.59mA；原理图显示稳压器、SAM2695、光耦、LED 和输出支路，但没有整机电流、模式条件或容差标注。（证据：图 73356ab7e30b / 第 1 页 / 第 1 页完整电源与负载电路，未标整机电流）
- `other.duplicate-r11-reference`：本页在 U2 RST#/PD# 上拉处标出 R11 22K/1%，同时在 MIDI OUT/SYS_5V 电阻网络处又标出 R11 220R/1%；同一位号对应两个不同阻值和功能，无法由本页确定正确 BOM 编号。（证据：图 73356ab7e30b / 第 1 页 / 第 1 页网格 B2 的 R11 22K/1% 与网格 A4 的 R11 220R/1%）
- `review.mode-routing`：请结合 S1 实物档位、PCB 网表或导通实测确认 Bypass/Separate 各档的 INPUT、OUTPUT、Grove 与 SAM2695 路由。；原因：原理图未标开关档位名称或完整触点真值表。
- `review.midi-protocol`：请用当前固件/协议资料或串口实测确认 MIDI 1.0、16 通道以及正文所写 31520bps 是否准确。；原因：板级原理图没有通信参数，且需要独立确认波特率文本。
- `review.polyphony`：请用 SAM2695 资料和当前配置确认 64/38 复音条件、效果模式及音色库版本。；原因：原理图不能证明合成器的固件/音色与复音性能。
- `review.standby-current`：请用量产规格或实测确认 5V@18.59mA 待机电流对应的模式、音量、MIDI 活动和输出负载条件。；原因：原理图没有整机电流或测试状态标注。
- `review.duplicate-r11`：请用 PCB/BOM 确认 RST#/PD# 的 22K 上拉和 MIDI OUT 的 220Ω 电阻各自正确位号。；原因：原理图重复使用 R11 且阻值不同。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `73356ab7e30bd47c3853896f0c348b44360af07b32e4db80151fef9addd31100` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/774/SCH_UnitMIDI_B04_sch_2024_07_08_15_41_29_page_01.png` |

---

源文档：`zh_CN/unit/Unit-MIDI.md`

源文档 SHA-256：`8f14e73d002f536fbc4ef9ca37b7ee76a8de2ebc9e33d6f40670d39b13ac9c1a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
