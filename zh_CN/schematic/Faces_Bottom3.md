# Faces_Bottom3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces_Bottom3 |
| SKU | A168 |
| 产品 ID | `faces-bottom3-f33b429808b8` |
| 源文档 | `zh_CN/faces/Faces_Bottom3.md` |

## 概述

该原理图资源由两张电路页组成：第 1 页包含 10 颗 SK6812 串行灯链、Faces_Core 30 针连接、30P FPC、两个 HY-2.0 接口以及 BAT 到 BAT_ON 的受控电源路径。第 2 页包含另一组 30P FPC 与 2x11P 接口映射、SYS_5V 经 DSK34 到 BUS_5V 的路径，以及 TP4057 从 SYS_5V 向 BAT 连接的充电网络。原理图明确给出了主要 GPIO、电源网络、阻容值和连接器针脚；未标注的物理接口用途、方向语义和开关档位均保留为待确认。

## 检索关键词

`Faces_Bottom3`、`A168`、`Faces_Core`、`SK6812`、`LED1-LED10`、`LEDnet`、`S1`、`G15`、`G25`、`HY-2.0_UART`、`HY-2.0_IO`、`FPC-30P`、`2x11P`、`TP4057`、`ME1502CM5G`、`DSK34`、`BAT`、`BAT_ON`、`BAT_EN`、`HPWR`、`5V`、`3V3`、`SYS_5V`、`BUS_5V`、`G16`、`G17`、`G21`、`G22`、`G26`、`G36`、`SW-DPDT`、`SW-SPDT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED10 | SK6812 | 第 1 页的 10 颗串行 RGB LED，LEDnet 进入 LED1，数据依次传递到 LED10。 | 图 1a63a5979cc1 / 第 1 页 / 网格 A1-A4，LED1 至 LED10，标注 SK6812、DIN、DOUT、VDD、VSS |
| J3 | Faces_Core | 第 1 页的 30 针 Core 总线符号，分配 GPIO、3V3、5V、HPWR、BAT_ON 与 GND。 | 图 1a63a5979cc1 / 第 1 页 / 网格 B1-C2，J3 Faces_Core，针脚 1-30 |
| FPC1 | FPC-30P | 第 1 页的 30 针 FPC 连接器，承载 GPIO、5V、3V3、HPWR、BAT 与 GND。 | 图 1a63a5979cc1 / 第 1 页 / 网格 C4-D4，FPC1 FPC-30P，针脚 1-30 |
| J1 | HY-2.0_UART | 第 1 页的 4 针 UART 标注接口，连接 G16、G17、5V 与 GND。 | 图 1a63a5979cc1 / 第 1 页 / 网格 B4，J1 HY-2.0_UART，针脚 1-4 |
| J2 | HY-2.0_IO | 第 1 页的 4 针 I/O 标注接口，连接 G36、G26、5V 与 GND。 | 图 1a63a5979cc1 / 第 1 页 / 网格 B4，J2 HY-2.0_IO，针脚 1-4 |
| S1 | SW-SPDT | 在 G15 与 G25 之间选择 LEDnet 控制来源。 | 图 1a63a5979cc1 / 第 1 页 / 网格 B3，S1 SW-SPDT，共用端 LEDnet，选择端 G15/G25 |
| U21 | ME1502CM5G | 第 1 页 BAT 到 BAT_ON 路径中的五引脚器件，使用 VIN、OUT、EN、SET 与 GND 引脚。 | 图 1a63a5979cc1 / 第 1 页 / 网格 C2，U21 ME1502CM5G，VIN/OUT/EN/SET/GND 网络 |
| SW1 | SW-DPDT | 第 1 页与 BAT_EN 和 GND 相连的机械联动双刀双掷开关。 | 图 1a63a5979cc1 / 第 1 页 / 网格 C2-C3，SW1 SW-DPDT，已标注网络 BAT_EN 与 GND |
| J4 | SMT_HDR_2x1.25mm | 第 1 页的 BAT/GND 四引脚表贴连接器。 | 图 1a63a5979cc1 / 第 1 页 / 网格 B3-C3，J4 SMT_HDR_2x1.25mm，针脚 1-4 |
| FPC1 | FPC-30P | 第 2 页的 30 针 FPC 连接器，承载 GPIO、BUS_5V、3V3、HPWR、BAT 与 GND。 | 图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，FPC1 FPC-30P，针脚 1-30 |
| J2 | 2x11P | 第 2 页的 22 针连接器，分配 GPIO、HPWR、3V3、BUS_5V 与 GND。 | 图 fd3b1a620966 / 第 1 页 / 网格 B2-C3，J2 2x11P，针脚 1-22 |
| J3 | 未标注 | 第 2 页的 4 针连接器，针脚网络为 G22、G21、SYS_5V 与 GND。 | 图 fd3b1a620966 / 第 1 页 / 网格 B3，J3，针脚 1-4 与网络 G22/G21/SYS_5V/GND |
| D1 | DSK34 | 第 2 页串接在 SYS_5V 与 BUS_5V 之间的二极管。 | 图 fd3b1a620966 / 第 1 页 / 网格 B3-B4，D1 DSK34，左侧 SYS_5V、右侧 BUS_5V |
| U1 | TP4057 | 第 2 页的电池充电器件，VCC 接 SYS_5V，BAT 接 BAT，PROG 经电阻接地。 | 图 fd3b1a620966 / 第 1 页 / 网格 C2-C3，U1 TP4057，VCC/CHRG/GND/BAT/STDBY/PROG |
| J4 | SMT_HDR_2x1.25mm | 第 2 页的 BAT/GND 四引脚表贴连接器。 | 图 fd3b1a620966 / 第 1 页 / 网格 C3-C4，J4 SMT_HDR_2x1.25mm，针脚 1-4 |

## 系统结构

### 两页原理图功能分布

第 1 页集中显示 LED、Core/FPC 接口和 BAT_ON 使能路径；第 2 页集中显示 30P/22P 接口、SYS_5V 到 BUS_5V 路径及 TP4057 充电网络。

- 参数与网络：`page_1_blocks=LED1-LED10; J1/J2/J3/FPC1/J4; U21; S1; SW1`；`page_2_blocks=FPC1; J2/J3/J4; D1; U1`
- 证据：图 1a63a5979cc1 / 第 1 页 / 第 1 页全图，网格 A1-D4; 图 fd3b1a620966 / 第 1 页 / 第 2 页全图，网格 B1-C4

## 电源

### LED1-LED10 供电

10 颗 SK6812 的 VDD pin 4 均接 5V，VSS pin 2 均接 GND。

- 参数与网络：`references=LED1-LED10`；`vdd_pin=4`；`vdd_net=5V`；`vss_pin=2`；`vss_net=GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 A1-A4，每个 LED 符号的 VDD/VSS 与 5V/GND 标注

### SK6812 去耦

C1 至 C10 均为 100nF，并分别跨接在 5V 与 GND 之间。

- 参数与网络：`references=C1-C10`；`value=100nF`；`between=5V-GND`；`quantity=10`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 D1-D2，C1-C10，每颗标注 100nF、上接 5V、下接 GND

### J3 Faces_Core 电源映射

J3 的 pins 2/4/6 接 GND，pin 11 接 3V3，pin 27 接 5V，pins 26/28/30 共接 HPWR，pin 29 的 BATTERY 引脚接 BAT_ON。

- 参数与网络：`gnd_pins=2,4,6`；`3v3_pin=11`；`5v_pin=27`；`hpwr_pins=26,28,30`；`battery_pin=29=BAT_ON`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B1-C2，J3 Faces_Core，pins 2/4/6/11/26-30

### 第 1 页 FPC1 电源映射

第 1 页 FPC1 的 pins 1-3 接 GND，pins 4-5 接 5V，pins 6-7 接 3V3，pins 26-27 接 HPWR，pins 28-30 接 BAT。

- 参数与网络：`gnd_pins=1,2,3`；`5v_pins=4,5`；`3v3_pins=6,7`；`hpwr_pins=26,27`；`bat_pins=28,29,30`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C4-D4，FPC1 pins 1-7 与 26-30

### U21 BAT 到 BAT_ON 路径

U21 pin 5 VIN 接 BAT，pin 1 OUT 接 BAT_ON，pin 4 EN 接 BAT_EN，pin 2 接 GND。

- 参数与网络：`reference=U21`；`part_number=ME1502CM5G`；`vin=pin 5=BAT`；`out=pin 1=BAT_ON`；`enable=pin 4=BAT_EN`；`ground=pin 2=GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C2，U21 pins 1/2/4/5 及 BAT、BAT_ON、BAT_EN、GND

### BAT_EN 偏置

R1 为 100K/1%，连接在 BAT 与 BAT_EN 之间。

- 参数与网络：`reference=R1`；`value=100K/1%`；`between=BAT-BAT_EN`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C1-C2，R1 100K/1%，左接 BAT、右接 BAT_EN

### BAT 与 BAT_ON 电容

C11 为 10u/10V 并接 BAT 到 GND，C12 为 10u/10V 并接 BAT_ON 到 GND。

- 参数与网络：`input_capacitor=C11=10u/10V BAT-GND`；`output_capacitor=C12=10u/10V BAT_ON-GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C1-C2，C11/C12 及 BAT/BAT_ON/GND

### SW1 与 BAT_EN

SW1 的已用开关段在一个触点侧接 GND、公共侧接 BAT_EN，另一选择触点未标网络；其余机械联动触点未接网络。

- 参数与网络：`reference=SW1`；`part=SW-DPDT`；`labeled_nets=GND,BAT_EN`；`unused_contacts=unlabeled`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C2-C3，SW1 的 GND/BAT_EN 连线、虚线机械联动和无网络触点

### 第 2 页 FPC1 电源映射

第 2 页 FPC1 的 pins 1-3 接 GND，pins 4-5 接 BUS_5V，pins 6-7 接 3V3，pins 26-27 接 HPWR，pins 28-30 接 BAT。

- 参数与网络：`gnd_pins=1,2,3`；`bus_5v_pins=4,5`；`3v3_pins=6,7`；`hpwr_pins=26,27`；`bat_pins=28,29,30`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，第 2 页 FPC1 pins 1-7 与 26-30

### SYS_5V 到 BUS_5V

D1（DSK34）串接在 SYS_5V 与 BUS_5V 之间，SYS_5V 位于符号左侧，BUS_5V 位于右侧。

- 参数与网络：`reference=D1`；`part_number=DSK34`；`left_net=SYS_5V`；`right_net=BUS_5V`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 B3-B4，J3 pin 2 的 SYS_5V 经 D1 DSK34 到 BUS_5V

### TP4057 主连接

U1 TP4057 的 pin 4 VCC 接 SYS_5V，pin 2 GND 接 GND，pin 3 BAT 接 BAT。

- 参数与网络：`vcc=pin 4=SYS_5V`；`ground=pin 2=GND`；`battery=pin 3=BAT`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 C2-C3，U1 TP4057 pins 2/3/4 与 SYS_5V/BAT/GND

### TP4057 电源电容

C1 为 2.2uF 并接 SYS_5V 到 GND，C2 为 0.1uF_0603 并接 BAT 到 GND。

- 参数与网络：`input_capacitor=C1=2.2uF SYS_5V-GND`；`battery_capacitor=C2=0.1uF_0603 BAT-GND`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 C2-C3，C1/C2 与 SYS_5V/BAT/GND

## 接口

### J3 未连接引脚

J3 的 EN pin 5、GPIO1 pin 13 和 GPIO3 pin 14 在该页符号外没有继续连线。

- 参数与网络：`unconnected=pin 5=EN; pin 13=GPIO1; pin 14=GPIO3`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B1-C2，J3 pins 5、13、14 的短线末端

### 第 1 页 FPC1 GPIO 映射

第 1 页 FPC1 的 pins 8-25 依次映射为 G35、G23、G36、G19、G25、G18、G26、G16、G12、G17、G13、G21、G15、G22、G0、G2、G34、G5。

- 参数与网络：`pin_map=8=G35;9=G23;10=G36;11=G19;12=G25;13=G18;14=G26;15=G16;16=G12;17=G17;18=G13;19=G21;20=G15;21=G22;22=G0;23=G2;24=G34;25=G5`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C4-D4，FPC1 pins 8-25 与左侧网络名

### J1 HY-2.0_UART

J1 pin 1 标为 RX 并接 G16，pin 2 标为 TX 并接 G17，pin 3 为 VCC 并接 5V，pin 4 为 GND。

- 参数与网络：`pin_1=RX=G16`；`pin_2=TX=G17`；`pin_3=VCC=5V`；`pin_4=GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B4，J1 HY-2.0_UART，pins 1-4

### J2 HY-2.0_IO

J2 pin 1 标为 I 并接 G36，pin 2 标为 O 并接 G26，pin 3 为 VCC 并接 5V，pin 4 为 GND。

- 参数与网络：`pin_1=I=G36`；`pin_2=O=G26`；`pin_3=VCC=5V`；`pin_4=GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B4，J2 HY-2.0_IO，pins 1-4

### 第 1 页 J4 电池端子

第 1 页 J4 pin 1 接 BAT，pins 2、3、4 通过连线汇接到 GND。

- 参数与网络：`pin_1=BAT`；`ground_pins=2,3,4`；`part=SMT_HDR_2x1.25mm`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B3-C3，J4 pins 1-4、BAT 标签与 GND 汇接点

### 第 2 页 FPC1 GPIO 映射

第 2 页 FPC1 的 pins 8-25 依次映射为 G35、G23、G36、G19、G25、G18、G26、G16、G12、G17、G13、G21、G15、G22、G0、G2、G34、G5。

- 参数与网络：`pin_map=8=G35;9=G23;10=G36;11=G19;12=G25;13=G18;14=G26;15=G16;16=G12;17=G17;18=G13;19=G21;20=G15;21=G22;22=G0;23=G2;24=G34;25=G5`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，第 2 页 FPC1 pins 8-25

### 第 2 页 J2 2x11P 映射

J2 pins 1-11 为 HPWR、G34、G0、G15、G13、G12、G26、G25、G36、G35、GND；pins 12-22 为 BUS_5V、3V3、G23、G19、G18、G16、G17、G21、G22、G2、G5。

- 参数与网络：`pins_1_11=1=HPWR;2=G34;3=G0;4=G15;5=G13;6=G12;7=G26;8=G25;9=G36;10=G35;11=GND`；`pins_12_22=12=BUS_5V;13=3V3;14=G23;15=G19;16=G18;17=G16;18=G17;19=G21;20=G22;21=G2;22=G5`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 B2-C3，J2 2x11P 的上下两排 pins 1-22

### 第 2 页 J3 针脚

第 2 页 J3 pin 4 接 G22，pin 3 接 G21，pin 2 接 SYS_5V，pin 1 接 GND。

- 参数与网络：`pin_4=G22`；`pin_3=G21`；`pin_2=SYS_5V`；`pin_1=GND`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 B3，J3 pins 1-4 及 G22/G21/SYS_5V/GND

### 第 2 页 J4 电池端子

第 2 页 J4 pin 1 接 BAT，pins 2、3、4 通过连线汇接到 GND。

- 参数与网络：`pin_1=BAT`；`ground_pins=2,3,4`；`part=SMT_HDR_2x1.25mm`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 C3-C4，J4 pins 1-4、BAT 标签与 GND 汇接点

## 总线

### SK6812 数据链

LEDnet 连接 LED1 的 DIN；LED1 至 LED10 按 DOUT 到下一颗 DIN 的顺序串接，LED10 的 DOUT 未继续连接。

- 参数与网络：`input_net=LEDnet`；`order=LED1->LED2->LED3->LED4->LED5->LED6->LED7->LED8->LED9->LED10`；`din_pin=3`；`dout_pin=1`；`last_dout=LED10 pin 1 unconnected`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 A1-A4，LEDnet、LED1-LED10 的 DIN pin 3 与 DOUT pin 1 连线

### 两页 FPC1 可见针脚一致性

两页 FPC1 的 GPIO、3V3、HPWR、BAT 与 GND 针脚号一致；5V 电源在第 1 页标为 5V，在第 2 页对应 pins 4-5 标为 BUS_5V。

- 参数与网络：`common_gpio_range=pins 8-25`；`common_3v3=pins 6-7`；`common_hpwr=pins 26-27`；`common_bat=pins 28-30`；`common_gnd=pins 1-3`；`power_label_difference=page 1 pins 4-5=5V; page 2 pins 4-5=BUS_5V`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C4-D4，第 1 页 FPC1 pins 1-30; 图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，第 2 页 FPC1 pins 1-30

## GPIO 与控制信号

### LEDnet 控制源选择

S1 的公共端 pin 2 接 LEDnet，两个选择端分别为 pin 3 的 G15 和 pin 1 的 G25。

- 参数与网络：`reference=S1`；`common=pin 2=LEDnet`；`throw_a=pin 3=G15`；`throw_b=pin 1=G25`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B3，S1 SW-SPDT，pin 1/2/3 网络标注

### J3 Faces_Core GPIO 映射

J3 将可见 GPIO 引脚映射到同编号 G 网络：GPIO35/36/25/26/17/22/5/13/0/34/23/19/18/16/21/2/12/15 分别接 G35/G36/G25/G26/G17/G22/G5/G13/G0/G34/G23/G19/G18/G16/G21/G2/G12/G15。

- 参数与网络：`pin_map=1=G35;3=G36;7=G25;9=G26;15=G17;17=G22;19=G5;21=G13;23=G0;25=G34;8=G23;10=G19;12=G18;16=G16;18=G21;20=G2;22=G12;24=G15`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B1-C2，J3 Faces_Core 的 GPIO 引脚及两侧 G 网络标注

### TP4057 状态引脚

U1 pin 1 CHRG 与 pin 5 STDBY 在该页没有继续连线。

- 参数与网络：`unconnected=pin 1=CHRG; pin 5=STDBY`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 C2-C3，U1 CHRG pin 1 与 STDBY pin 5 的短线末端

## 关键网络

### HPWR 与 BAT 多针分配

两页 FPC1 均将 HPWR 并接到 pins 26-27、BAT 并接到 pins 28-30；第 1 页 J3 Faces_Core 另将 HPWR 并接到 pins 26/28/30，并把其 BATTERY pin 29 接到 BAT_ON。

- 参数与网络：`fpc_hpwr=pins 26,27`；`fpc_bat=pins 28,29,30`；`faces_core_hpwr=pins 26,28,30`；`faces_core_battery=pin 29=BAT_ON`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 B1-C2 的 J3 pins 26-30；网格 C4-D4 的 FPC1 pins 26-30; 图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，第 2 页 FPC1 pins 26-30

## 模拟电路

### U21 SET 电阻

U21 pin 3 SET 经 R2 30K/1% 接 GND。

- 参数与网络：`reference=R2`；`value=30K/1%`；`path=U21 pin 3 SET-R2-GND`
- 证据：图 1a63a5979cc1 / 第 1 页 / 网格 C2，U21 SET pin 3 与 R2 30K/1%

### TP4057 PROG 电阻

U1 pin 6 PROG 经 R1 3K_0603 接 GND。

- 参数与网络：`reference=R1`；`value=3K_0603`；`path=U1 pin 6 PROG-R1-GND`
- 证据：图 fd3b1a620966 / 第 1 页 / 网格 C2-C3，U1 PROG pin 6、R1 3K_0603 与 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 两页原理图功能分布 | `page_1_blocks=LED1-LED10; J1/J2/J3/FPC1/J4; U21; S1; SW1`；`page_2_blocks=FPC1; J2/J3/J4; D1; U1` |
| 总线 | SK6812 数据链 | `input_net=LEDnet`；`order=LED1->LED2->LED3->LED4->LED5->LED6->LED7->LED8->LED9->LED10`；`din_pin=3`；`dout_pin=1`；`last_dout=LED10 pin 1 unconnected` |
| 电源 | LED1-LED10 供电 | `references=LED1-LED10`；`vdd_pin=4`；`vdd_net=5V`；`vss_pin=2`；`vss_net=GND` |
| 电源 | SK6812 去耦 | `references=C1-C10`；`value=100nF`；`between=5V-GND`；`quantity=10` |
| GPIO 与控制信号 | LEDnet 控制源选择 | `reference=S1`；`common=pin 2=LEDnet`；`throw_a=pin 3=G15`；`throw_b=pin 1=G25` |
| GPIO 与控制信号 | J3 Faces_Core GPIO 映射 | `pin_map=1=G35;3=G36;7=G25;9=G26;15=G17;17=G22;19=G5;21=G13;23=G0;25=G34;8=G23;10=G19;12=G18;16=G16;18=G21;20=G2;22=G12;24=G15` |
| 电源 | J3 Faces_Core 电源映射 | `gnd_pins=2,4,6`；`3v3_pin=11`；`5v_pin=27`；`hpwr_pins=26,28,30`；`battery_pin=29=BAT_ON` |
| 接口 | J3 未连接引脚 | `unconnected=pin 5=EN; pin 13=GPIO1; pin 14=GPIO3` |
| 接口 | 第 1 页 FPC1 GPIO 映射 | `pin_map=8=G35;9=G23;10=G36;11=G19;12=G25;13=G18;14=G26;15=G16;16=G12;17=G17;18=G13;19=G21;20=G15;21=G22;22=G0;23=G2;24=G34;25=G5` |
| 电源 | 第 1 页 FPC1 电源映射 | `gnd_pins=1,2,3`；`5v_pins=4,5`；`3v3_pins=6,7`；`hpwr_pins=26,27`；`bat_pins=28,29,30` |
| 接口 | J1 HY-2.0_UART | `pin_1=RX=G16`；`pin_2=TX=G17`；`pin_3=VCC=5V`；`pin_4=GND` |
| 接口 | J2 HY-2.0_IO | `pin_1=I=G36`；`pin_2=O=G26`；`pin_3=VCC=5V`；`pin_4=GND` |
| GPIO 与控制信号 | J2 I/O 方向定义 | `input_labeled_net=G36`；`output_labeled_net=G26`；`missing_definition=direction reference` |
| 接口 | 第 1 页 J4 电池端子 | `pin_1=BAT`；`ground_pins=2,3,4`；`part=SMT_HDR_2x1.25mm` |
| 电源 | U21 BAT 到 BAT_ON 路径 | `reference=U21`；`part_number=ME1502CM5G`；`vin=pin 5=BAT`；`out=pin 1=BAT_ON`；`enable=pin 4=BAT_EN`；`ground=pin 2=GND` |
| 电源 | BAT_EN 偏置 | `reference=R1`；`value=100K/1%`；`between=BAT-BAT_EN` |
| 模拟电路 | U21 SET 电阻 | `reference=R2`；`value=30K/1%`；`path=U21 pin 3 SET-R2-GND` |
| 电源 | BAT 与 BAT_ON 电容 | `input_capacitor=C11=10u/10V BAT-GND`；`output_capacitor=C12=10u/10V BAT_ON-GND` |
| 电源 | SW1 与 BAT_EN | `reference=SW1`；`part=SW-DPDT`；`labeled_nets=GND,BAT_EN`；`unused_contacts=unlabeled` |
| 电源 | SW1 物理档位 | `known_nets=GND,BAT_EN`；`missing=physical position to electrical state mapping` |
| 接口 | 第 2 页 FPC1 GPIO 映射 | `pin_map=8=G35;9=G23;10=G36;11=G19;12=G25;13=G18;14=G26;15=G16;16=G12;17=G17;18=G13;19=G21;20=G15;21=G22;22=G0;23=G2;24=G34;25=G5` |
| 电源 | 第 2 页 FPC1 电源映射 | `gnd_pins=1,2,3`；`bus_5v_pins=4,5`；`3v3_pins=6,7`；`hpwr_pins=26,27`；`bat_pins=28,29,30` |
| 接口 | 第 2 页 J2 2x11P 映射 | `pins_1_11=1=HPWR;2=G34;3=G0;4=G15;5=G13;6=G12;7=G26;8=G25;9=G36;10=G35;11=GND`；`pins_12_22=12=BUS_5V;13=3V3;14=G23;15=G19;16=G18;17=G16;18=G17;19=G21;20=G22;21=G2;22=G5` |
| 接口 | 第 2 页 J3 针脚 | `pin_4=G22`；`pin_3=G21`；`pin_2=SYS_5V`；`pin_1=GND` |
| 接口 | 第 2 页 J3 物理用途 | `reference=J3`；`known_nets=G22,G21,SYS_5V,GND`；`missing=connector type and physical role` |
| 电源 | SYS_5V 到 BUS_5V | `reference=D1`；`part_number=DSK34`；`left_net=SYS_5V`；`right_net=BUS_5V` |
| 电源 | TP4057 主连接 | `vcc=pin 4=SYS_5V`；`ground=pin 2=GND`；`battery=pin 3=BAT` |
| 模拟电路 | TP4057 PROG 电阻 | `reference=R1`；`value=3K_0603`；`path=U1 pin 6 PROG-R1-GND` |
| 电源 | TP4057 电源电容 | `input_capacitor=C1=2.2uF SYS_5V-GND`；`battery_capacitor=C2=0.1uF_0603 BAT-GND` |
| GPIO 与控制信号 | TP4057 状态引脚 | `unconnected=pin 1=CHRG; pin 5=STDBY` |
| 接口 | 第 2 页 J4 电池端子 | `pin_1=BAT`；`ground_pins=2,3,4`；`part=SMT_HDR_2x1.25mm` |
| 总线 | 两页 FPC1 可见针脚一致性 | `common_gpio_range=pins 8-25`；`common_3v3=pins 6-7`；`common_hpwr=pins 26-27`；`common_bat=pins 28-30`；`common_gnd=pins 1-3`；`power_label_difference=page 1 pins 4-5=5V; page 2 pins 4-5=BUS_5V` |
| 系统结构 | 两页 FPC1 实体关系 | `reference=FPC1`；`known=matching pin numbers and signals`；`missing=sheet-to-board and mating relationship` |
| 关键网络 | HPWR 与 BAT 多针分配 | `fpc_hpwr=pins 26,27`；`fpc_bat=pins 28,29,30`；`faces_core_hpwr=pins 26,28,30`；`faces_core_battery=pin 29=BAT_ON` |

## 待确认事项

- `io-port.direction-semantics`：J2 符号只标出 pin 1 为 I、pin 2 为 O；原理图未说明方向是相对 Faces Bottom3、主机还是外部设备定义。（证据：图 1a63a5979cc1 / 第 1 页 / 网格 B4，J2 内部仅见 I/O 标签，无方向参照说明）
- `battery.switch-position`：原理图没有标注 SW1 的外部拨动方向、ON/OFF 文本或各物理档位对应的 BAT_EN 状态。（证据：图 1a63a5979cc1 / 第 1 页 / 网格 C2-C3，SW1 符号周围无 ON/OFF 或方向标注）
- `page2.j3-physical-role`：原理图没有为第 2 页 J3 标出连接器型号或物理接口名称，因此仅凭该页不能确认它是否对应磁吸触点或其他外部接口。（证据：图 fd3b1a620966 / 第 1 页 / 网格 B3，J3 仅有位号、针脚号和网络名，无型号/用途文字）
- `fpc1.cross-page-physical-relation`：虽然两页 FPC1 的大多数针脚映射一致，但原理图未给出页间连接标记、板名或装配关系，不能仅凭图纸确认两个 FPC1 符号是否为直接配对的两个实体连接器。（证据：图 1a63a5979cc1 / 第 1 页 / 网格 C4-D4，第 1 页 FPC1；页面无板名或跨页连接说明; 图 fd3b1a620966 / 第 1 页 / 网格 B1-C2，第 2 页 FPC1；页面无板名或跨页连接说明）
- `review.io-port-direction`：J2 的 I/O 方向是以主机、Faces Bottom3 还是外部设备为参照？；原因：原理图仅在 J2 符号内部标注 I 和 O，没有给出方向参照。
- `review.sw1-position`：SW1 哪个物理拨动方向对应 BAT_EN 接地，哪个方向对应释放？；原因：图中有电气触点和机械联动，但没有外壳方向或 ON/OFF 档位标识。
- `review.page2-j3-role`：第 2 页 J3 的连接器型号和实际物理接口是什么？；原因：原理图仅给出位号、四个针脚和网络，没有型号或用途标签。
- `review.fpc1-mating`：两页的 FPC1 是否分别位于两个 PCB 并直接互连或配对？；原因：针脚映射高度一致，但图中没有板名、页间引用或装配连接说明。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1a63a5979cc1ee659ed2bd10e825c85d317019547c520e0d8efd56f3ad3809fd` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1273/A168_Faces_Bottom3_Sche_page_01.png` |
| 2 | 1 | `fd3b1a6209661da45ce10468a69b204d52b9e04e2c941fcf5d9deedff205634c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1273/A168_Faces_Bottom3_Sche_page_02.png` |

---

源文档：`zh_CN/faces/Faces_Bottom3.md`

源文档 SHA-256：`bd1f85fd23f369ffc56346b78af27a37b5b007aefe0aa851f125a7b769b12862`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
