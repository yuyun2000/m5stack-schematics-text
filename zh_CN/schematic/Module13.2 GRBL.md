# Module13.2 GRBL 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 GRBL |
| SKU | M035 |
| 产品 ID | `module13-2-grbl-372f1e1be2cc` |
| 源文档 | `zh_CN/module/grbl13.2.md` |

## 概述

Module13.2 GRBL 以 U2 ATMEGA328P-AU 为控制器，输出 STP_X/Y/Z、DIR_X/Y/Z 和 DRV_EN，控制 U3、U4、U5 三颗 DRV8825，并由 J4、J5、J6 分别连接三轴双极步进电机。J3 引出 END_X/Y/Z 三路限位输入，SH1041 四位拨码提供 M0/M1/M2 微步模式与 ADDR 地址配置，M5-Bus 通过 CORE_SCL/SDA、CORE_RXD/TXD 和 CORE_RST 与板内控制域连接。VIN 同时供给三颗电机驱动和 U1 SY8205FCC 降压电源，后者经 FU1、D1 形成系统与 MCU 5V 电源。

## 检索关键词

`Module13.2 GRBL`、`M035`、`ATMEGA328P-AU`、`DRV8825`、`SY8205FCC`、`I2C`、`0x70`、`0x71`、`STP_X`、`STP_Y`、`STP_Z`、`DIR_X`、`DIR_Y`、`DIR_Z`、`DRV_EN`、`END_X`、`END_Y`、`END_Z`、`M0`、`M1`、`M2`、`ADDR`、`D_RST`、`VIN`、`MCU_5V`、`SYS_P050`、`M5_BUS`、`XH-4AW`、`SH1041`、`12MHz`、`2N7002DW`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATMEGA328P-AU | 三轴 GRBL 控制、I2C/UART 通信、限位采集和驱动配置主控制器 | 图 5dd266361415 / 第 1 页 / 网格 A2-C3 的 U2 ATMEGA328P-AU，标注 DRV_EN、ADDR、END_X/Y/Z、STP_X/Y/Z、DIR_X/Y/Z、MCU_SDA/SCL/RXD/TXD |
| U3,U4,U5 | DRV8825 | X、Y、Z 三轴双极步进电机驱动器 | 图 5dd266361415 / 第 1 页 / 网格 A4、B4、C4-D4 的 U3/U4/U5 DRV8825，分别连接 STP_X/Y/Z、DIR_X/Y/Z 与 J4/J5/J6 |
| J4,J5,J6 | XH-4AW | 三轴四线步进电机输出连接器 | 图 5dd266361415 / 第 1 页 / 页面右侧 J4/J5/J6 XH-4AW，各自 pin 1-4 连接对应 DRV8825 AOUT1/AOUT2/BOUT2/BOUT1 |
| J3 | XH-4AW | END_X、END_Y、END_Z 与 GND 三轴限位接口 | 图 5dd266361415 / 第 1 页 / 网格 C3 的 J3 XH-4AW，pin 1-3 经 D4/D5/D6 连接 END_X/Y/Z，pin 4 接 GND |
| SH1041 | 四位拨码开关 | DRV8825 M0/M1/M2 微步模式和 MCU ADDR 地址输入配置 | 图 5dd266361415 / 第 1 页 / 网格 A3 的 SH1041 四位拨码，四条网络标注 M0、M1、M2、ADDR |
| U1 | SY8205FCC | VIN 至系统 5V 电源的降压转换器 | 图 5dd266361415 / 第 1 页 / 网格 B1 的 U1 SY8205FCC，连接 VIN、L1 10uH、反馈网络、FU1 与 SYS_P050 |
| J1 | DC5.5 | VIN/PWR- 外部直流电源输入接口 | 图 5dd266361415 / 第 1 页 / 网格 B1 左侧 J1 DC5.5，PWR+ 接 VIN，PWR- 接 GND，旁有 C3/C5 高压电容 |
| FU1,D1 | 1A/PTC; 1N5819WS | 降压输出串联保护和 MCU_5V 隔离二极管 | 图 5dd266361415 / 第 1 页 / 网格 B1-B2 的 U1 输出经 FU1 1A/PTC 形成 SYS_P050，再经 D1 1N5819WS 到 MCU_5V |
| BUS1 | M5_BUS 30 PIN | 主机电源、I2C、UART 和复位接口 | 图 5dd266361415 / 第 1 页 / 网格 A1 的 BUS1 M5_BUS 30 PIN，板内使用 SYS_P050、CORE_SCL/SDA、CORE_3V3、CORE_RST、CORE_RXD/TXD 和 GND |
| J2 | CON6 | MCU_5V、MCU_RST、MCU_SCK、MCU_MISO、MCU_MOSI 和 GND 调试/下载接口 | 图 5dd266361415 / 第 1 页 / 网格 A2 的 J2 CON6，pin 6-1 依次连接 MCU_5V、MCU_RST、MCU_SCK、MCU_MISO、MCU_MOSI、GND |
| X1,C10,C11 | 12M_12PF; 12pF/50V; 12pF/50V | ATmega328P 12MHz 时钟晶体与负载电容 | 图 5dd266361415 / 第 1 页 / 网格 C2 的 X1 12M_12PF 与 C10/C11 12pF/50V，连接 MCU_X1/MCU_X2 |
| 未标位号 2N7002DW x2 | 2N7002DW | CORE 与 MCU 信号域之间的双 MOSFET 电平转换器 | 图 5dd266361415 / 第 1 页 / 网格 B2 左侧两组标注 2N7002DW 的双 MOSFET 符号，周围有 CORE_SCL/SDA/RST、MCU_SCL/SDA/RST 与 CORE_3V3 |

## 系统结构

### Module13.2 GRBL 系统架构

U2 ATMEGA328P-AU 通过 STP_X/Y/Z、DIR_X/Y/Z 和 DRV_EN 控制 U3/U4/U5 三颗 DRV8825，三轴电机分别连接 J4/J5/J6；J3 提供三路限位输入，BUS1 提供主机通信与电源。

- 参数与网络：`controller=U2 ATMEGA328P-AU`；`drivers=U3,U4,U5 DRV8825`；`motor_ports=J4,J5,J6`；`limit_port=J3`；`mode_switch=SH1041`；`host=BUS1 M5_BUS`；`power_converter=U1 SY8205FCC`
- 证据：图 5dd266361415 / 第 1 页 / 完整单页网格 A1-D4 的 M5-Bus、电源、MCU、限位和三轴驱动功能区

## 核心器件

### U2 运动控制引脚

U2 PD2/pin 32、PD3/pin 1、PD4/pin 2 分别连接 STP_X、STP_Y、STP_Z；PD5/pin 9、PD6/pin 10、PD7/pin 11 分别连接 DIR_X、DIR_Y、DIR_Z；PB0/pin 12 连接 DRV_EN。

- 参数与网络：`STP_X=PD2/pin 32`；`STP_Y=PD3/pin 1`；`STP_Z=PD4/pin 2`；`DIR_X=PD5/pin 9`；`DIR_Y=PD6/pin 10`；`DIR_Z=PD7/pin 11`；`DRV_EN=PB0/pin 12`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B2-C3 U2 PB0/PD2-PD7 与 DRV_EN/STP_X-Y-Z/DIR_X-Y-Z 标注

### DRV8825 电流检测与参考网络

每颗 DRV8825 的 ISENA、ISENB 分别通过两只 0.2R(1/2W) 电阻连接 GND，并各自配置 1K 电位器、1.5K/1% 电阻与 1uF/10V 电容的参考/DECAY 网络。

- 参数与网络：`x_sense=R17,R18 0.2R(1/2W)`；`y_sense=R19,R20 0.2R(1/2W)`；`z_sense=R21,R22 0.2R(1/2W)`；`potentiometers=RV1,RV2,RV3 1K`；`reference_resistors=R14,R15,R16 1.5K/1%`；`reference_capacitors=1uF/10V per axis`
- 证据：图 5dd266361415 / 第 1 页 / 页面右侧 U3/U4/U5 ISENA/ISENB 电阻与 RV1/RV2/RV3、R14/R15/R16、1uF 电容网络

## 电源

### VIN 电机电源域

J1 PWR+ 连接 VIN、PWR- 连接 GND；VIN 由 C3 100uF/35V 与 C5 220uF/35V 滤波，并直接连接 U3/U4/U5 的 VCP/VMA/VMB 电机电源网络及各轴 100uF/50V、10uF/35V、100nF/50V 去耦。

- 参数与网络：`input=J1 DC5.5 PWR+/PWR-`；`rail=VIN`；`input_bulk=C3 100uF/35V,C5 220uF/35V`；`drivers=U3,U4,U5 VCP/VMA/VMB`；`per_axis_filter=100uF/50V,10uF/35V,100nF/50V`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B1 J1/C3/C5/VIN 与页面右侧 U3/U4/U5 VIN 电源和去耦

### U1 系统与 MCU 5V

U1 SY8205FCC 从 VIN 经 L1 10uH 和输出滤波产生电源，经 FU1 1A/PTC 形成 SYS_P050 并送到 BUS1 pin 3；SYS_P050 经 D1 1N5819WS 形成 MCU_5V，R3 10KΩ与 LED1 LED_GREEN 构成 MCU_5V 指示支路。

- 参数与网络：`converter=U1 SY8205FCC`；`inductor=L1 10uH`；`fuse=FU1 1A/PTC`；`bus_rail=SYS_P050/BUS1 pin 3`；`isolation_diode=D1 1N5819WS`；`mcu_rail=MCU_5V`；`indicator=R3 10KΩ,LED1 LED_GREEN`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B1-B2 U1/L1/FU1/SYS_P050/D1/MCU_5V/R3/LED1 与 BUS1 pin 3

### U2 MCU_5V 供电

U2 AVCC/pin 18 与 VCC pin 4、pin 6 接 MCU_5V，GND pin 3、pin 5、pin 21 接 GND；C12 22uF/10V 与 C13 1uF/10V 连接 MCU_5V 至 GND。

- 参数与网络：`rail=MCU_5V`；`supply_pins=U2 AVCC pin 18,VCC pin 4,6`；`ground_pins=U2 pin 3,5,21`；`decoupling=C12 22uF/10V,C13 1uF/10V`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B3-C3 U2 AVCC/VCC/GND 与 C12/C13

## 接口

### J4/J5/J6 三轴电机接口

J4、J5、J6 均为 XH-4AW，pin 1-4 分别连接对应 DRV8825 的 AOUT1、AOUT2、BOUT2、BOUT1。

- 参数与网络：`x_axis=J4 <- U3`；`y_axis=J5 <- U4`；`z_axis=J6 <- U5`；`pinout=1:AOUT1,2:AOUT2,3:BOUT2,4:BOUT1`
- 证据：图 5dd266361415 / 第 1 页 / 页面右侧 U3/J4、U4/J5、U5/J6 的 AOUT/BOUT 逐线连接

### BUS1 M5_BUS 已用针脚

BUS1 pin 3 连接 SYS_P050，pin 13 连接 CORE_SCL，pin 14 连接 CORE_SDA，pin 19 连接 CORE_3V3，pin 25 连接 CORE_RST，pin 27 连接 CORE_RXD，pin 29 连接 CORE_TXD，pin 26、28、30 连接 GND。

- 参数与网络：`used_pinout=3:SYS_P050/5V,13:CORE_SCL/G22,14:CORE_SDA/G21,19:CORE_3V3,25:CORE_RST/EN,26:GND,27:CORE_RXD/G36,28:GND,29:CORE_TXD/G35,30:GND`；`reference=BUS1 M5_BUS`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A1 BUS1 的板内外部网络标注

## 总线

### CORE 与 MCU I2C

BUS1 pin 13 CORE_SCL 与 pin 14 CORE_SDA 经标注 2N7002DW 的双 MOSFET电平转换电路连接 MCU_SCL、MCU_SDA；CORE 侧 R12/R25 10KΩ上拉至 CORE_3V3，MCU 侧 R10/R9 10KΩ上拉至 MCU_5V，MCU_SCL/SDA 分别连接 U2 PC5/pin 28、PC4/pin 27。

- 参数与网络：`host_scl=BUS1 pin 13/CORE_SCL`；`host_sda=BUS1 pin 14/CORE_SDA`；`host_pullups=R12 10KΩ,R25 10KΩ to CORE_3V3`；`level_shifter=2N7002DW`；`mcu_pullups=R10 10KΩ,R9 10KΩ to MCU_5V`；`mcu_scl=U2 PC5/pin 28`；`mcu_sda=U2 PC4/pin 27`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A1-B2 BUS1 CORE_SCL/SDA、R12/R25、2N7002DW、R9/R10 与 U2 MCU_SCL/SDA

### MCU UART 与 M5-Bus

U2 PD0/RXD/pin 30 与 PD1/TXD/pin 31 引出 MCU_RXD、MCU_TXD；BUS1 pin 27、pin 29 分别引出 CORE_RXD、CORE_TXD。本页未像 I2C 网络那样完整画出两组 UART 网络之间的逐线连接。

- 参数与网络：`mcu_rx=U2 PD0/pin 30/MCU_RXD`；`mcu_tx=U2 PD1/pin 31/MCU_TXD`；`host_rx=BUS1 pin 27/CORE_RXD`；`host_tx=BUS1 pin 29/CORE_TXD`；`cross_connection_fully_visible=false`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A1 的 BUS1 CORE_RXD/TXD 与网格 B2-C2 的 U2 MCU_RXD/TXD 网络标注

## GPIO 与控制信号

### 三轴 DRV8825 控制扇出

DRV_EN 共同连接 U3/U4/U5 ENBL/pin 21；STP_X/Y/Z 分别连接 U3/U4/U5 STEP/pin 22，DIR_X/Y/Z 分别连接对应 DIR/pin 20；D_RST 共同连接三颗驱动器 RESET/pin 16。

- 参数与网络：`enable=DRV_EN -> U3/U4/U5 pin 21`；`x_axis=STP_X/DIR_X -> U3 pin 22/20`；`y_axis=STP_Y/DIR_Y -> U4 pin 22/20`；`z_axis=STP_Z/DIR_Z -> U5 pin 22/20`；`driver_reset=D_RST -> U3/U4/U5 pin 16`
- 证据：图 5dd266361415 / 第 1 页 / U2 运动网络与页面右侧 U3/U4/U5 ENBL/STEP/DIR/RESET 引脚

### 三轴限位输入

U2 PC0/pin 23、PC1/pin 24、PC2/pin 25 分别连接 END_X、END_Y、END_Z，并由 R5/R6/R7 各 10KΩ上拉至 MCU_5V；三路经 D4/D5/D6 1N4148 连接 J3 pin 1/2/3，J3 pin 4 接 GND。

- 参数与网络：`END_X=U2 PC0/pin 23,R5 10KΩ,D4 1N4148,J3 pin 1`；`END_Y=U2 PC1/pin 24,R6 10KΩ,D5 1N4148,J3 pin 2`；`END_Z=U2 PC2/pin 25,R7 10KΩ,D6 1N4148,J3 pin 3`；`return=J3 pin 4/GND`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B2 U2 END_X/Y/Z 与 R5-R7、网格 C3 D4-D6/J3

### M0/M1/M2 微步配置硬件

SH1041 的三位开关连接 M0、M1、M2，三条网络共同连接 U3/U4/U5 的 MODE0/pin 24、MODE1/pin 25、MODE2/pin 26。

- 参数与网络：`switch=SH1041`；`mode0=M0 -> U3/U4/U5 pin 24`；`mode1=M1 -> U3/U4/U5 pin 25`；`mode2=M2 -> U3/U4/U5 pin 26`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A3 SH1041 的 M0/M1/M2 与 U3/U4/U5 MODE0/1/2 引脚

## 时钟

### U2 12MHz 时钟

X1 标注 12M_12PF，连接 MCU_X1/MCU_X2 与 U2 PB6/XTAL1 pin 7、PB7/XTAL2 pin 8；C10、C11 均为 12pF/50V并接 GND。

- 参数与网络：`crystal=X1 12M_12PF`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C10 12pF/50V,C11 12pF/50V`
- 证据：图 5dd266361415 / 第 1 页 / 网格 C2 X1/C10/C11 与 MCU_X1/MCU_X2/U2 XTAL1/XTAL2

## 复位

### MCU_RST、CORE_RST 与 D_RST

MCU_RST 由 R4 20K/1% 上拉至 MCU_5V并由 C9 22uF/10V接 GND，连接 U2 PC6/RESET pin 29 与 J2 pin 5；CORE_RST 从 BUS1 pin 25 引入并通过 2N7002DW 相关电路连接控制域，D_RST 共同复位三颗 DRV8825。

- 参数与网络：`mcu_reset=U2 PC6/pin 29/MCU_RST`；`pullup=R4 20K/1% to MCU_5V`；`capacitor=C9 22uF/10V`；`host_reset=BUS1 pin 25/CORE_RST`；`driver_reset=D_RST -> U3/U4/U5 pin 16`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A1-B3 BUS1 CORE_RST、2N7002DW、R4/C9/MCU_RST、U2 RESET 与三颗驱动器 D_RST

## 保护电路

### 电源与限位保护

FU1 1A/PTC 串联在降压输出，D1 1N5819WS 位于 SYS_P050 与 MCU_5V 之间，D4-D6 1N4148 串联在三路限位输入；本页未绘出电机端口 TVS 或独立反接保护器件。

- 参数与网络：`output_ptc=FU1 1A/PTC`；`mcu_diode=D1 1N5819WS`；`limit_diodes=D4,D5,D6 1N4148`；`motor_tvs_visible=false`；`reverse_protection_visible=false`
- 证据：图 5dd266361415 / 第 1 页 / 网格 B1-B2 FU1/D1 与网格 C3 D4-D6/J3，及电机端口外围

## 调试与烧录

### J2 MCU 下载接口

J2 pin 6 至 pin 1 依次连接 MCU_5V、MCU_RST、MCU_SCK、MCU_MISO、MCU_MOSI、GND；MCU_SCK/MISO/MOSI 对应 U2 PB5/pin 17、PB4/pin 16、PB3/pin 15。

- 参数与网络：`pinout=6:MCU_5V,5:MCU_RST,4:MCU_SCK,3:MCU_MISO,2:MCU_MOSI,1:GND`；`mcu_mapping=SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15`
- 证据：图 5dd266361415 / 第 1 页 / 网格 A2 J2 CON6 与 U2 MCU_MOSI/MISO/SCK 网络

## 其他事实

### 其他功能分区可见性

该页未绘出独立存储器、外部存储、音频器件、传感器或射频器件；运动位置输入仅见 END_X/Y/Z 限位开关接口。

- 参数与网络：`external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`position_inputs=END_X,END_Y,END_Z`
- 证据：图 5dd266361415 / 第 1 页 / 完整单页全部功能区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 GRBL 系统架构 | `controller=U2 ATMEGA328P-AU`；`drivers=U3,U4,U5 DRV8825`；`motor_ports=J4,J5,J6`；`limit_port=J3`；`mode_switch=SH1041`；`host=BUS1 M5_BUS`；`power_converter=U1 SY8205FCC` |
| 核心器件 | U2 运动控制引脚 | `STP_X=PD2/pin 32`；`STP_Y=PD3/pin 1`；`STP_Z=PD4/pin 2`；`DIR_X=PD5/pin 9`；`DIR_Y=PD6/pin 10`；`DIR_Z=PD7/pin 11`；`DRV_EN=PB0/pin 12` |
| GPIO 与控制信号 | 三轴 DRV8825 控制扇出 | `enable=DRV_EN -> U3/U4/U5 pin 21`；`x_axis=STP_X/DIR_X -> U3 pin 22/20`；`y_axis=STP_Y/DIR_Y -> U4 pin 22/20`；`z_axis=STP_Z/DIR_Z -> U5 pin 22/20`；`driver_reset=D_RST -> U3/U4/U5 pin 16` |
| GPIO 与控制信号 | 三轴限位输入 | `END_X=U2 PC0/pin 23,R5 10KΩ,D4 1N4148,J3 pin 1`；`END_Y=U2 PC1/pin 24,R6 10KΩ,D5 1N4148,J3 pin 2`；`END_Z=U2 PC2/pin 25,R7 10KΩ,D6 1N4148,J3 pin 3`；`return=J3 pin 4/GND` |
| 接口 | J4/J5/J6 三轴电机接口 | `x_axis=J4 <- U3`；`y_axis=J5 <- U4`；`z_axis=J6 <- U5`；`pinout=1:AOUT1,2:AOUT2,3:BOUT2,4:BOUT1` |
| GPIO 与控制信号 | M0/M1/M2 微步配置硬件 | `switch=SH1041`；`mode0=M0 -> U3/U4/U5 pin 24`；`mode1=M1 -> U3/U4/U5 pin 25`；`mode2=M2 -> U3/U4/U5 pin 26` |
| 其他事实 | 微步拨码真值表 | `mode_inputs=M0,M1,M2`；`documented_max=1/32`；`schematic_truth_table_visible=false` |
| 总线 | CORE 与 MCU I2C | `host_scl=BUS1 pin 13/CORE_SCL`；`host_sda=BUS1 pin 14/CORE_SDA`；`host_pullups=R12 10KΩ,R25 10KΩ to CORE_3V3`；`level_shifter=2N7002DW`；`mcu_pullups=R10 10KΩ,R9 10KΩ to MCU_5V`；`mcu_scl=U2 PC5/pin 28`；`mcu_sda=U2 PC4/pin 27` |
| 总线地址 | I2C ADDR 拨码 | `switch_input=SH1041 ADDR`；`mcu_pin=U2 PB1/pin 13`；`documented_addresses=0x70,0x71`；`schematic_mapping_visible=false` |
| 总线 | MCU UART 与 M5-Bus | `mcu_rx=U2 PD0/pin 30/MCU_RXD`；`mcu_tx=U2 PD1/pin 31/MCU_TXD`；`host_rx=BUS1 pin 27/CORE_RXD`；`host_tx=BUS1 pin 29/CORE_TXD`；`cross_connection_fully_visible=false` |
| 电源 | VIN 电机电源域 | `input=J1 DC5.5 PWR+/PWR-`；`rail=VIN`；`input_bulk=C3 100uF/35V,C5 220uF/35V`；`drivers=U3,U4,U5 VCP/VMA/VMB`；`per_axis_filter=100uF/50V,10uF/35V,100nF/50V` |
| 电源 | U1 系统与 MCU 5V | `converter=U1 SY8205FCC`；`inductor=L1 10uH`；`fuse=FU1 1A/PTC`；`bus_rail=SYS_P050/BUS1 pin 3`；`isolation_diode=D1 1N5819WS`；`mcu_rail=MCU_5V`；`indicator=R3 10KΩ,LED1 LED_GREEN` |
| 电源 | U2 MCU_5V 供电 | `rail=MCU_5V`；`supply_pins=U2 AVCC pin 18,VCC pin 4,6`；`ground_pins=U2 pin 3,5,21`；`decoupling=C12 22uF/10V,C13 1uF/10V` |
| 核心器件 | DRV8825 电流检测与参考网络 | `x_sense=R17,R18 0.2R(1/2W)`；`y_sense=R19,R20 0.2R(1/2W)`；`z_sense=R21,R22 0.2R(1/2W)`；`potentiometers=RV1,RV2,RV3 1K`；`reference_resistors=R14,R15,R16 1.5K/1%`；`reference_capacitors=1uF/10V per axis` |
| 调试与烧录 | J2 MCU 下载接口 | `pinout=6:MCU_5V,5:MCU_RST,4:MCU_SCK,3:MCU_MISO,2:MCU_MOSI,1:GND`；`mcu_mapping=SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15` |
| 时钟 | U2 12MHz 时钟 | `crystal=X1 12M_12PF`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C10 12pF/50V,C11 12pF/50V` |
| 复位 | MCU_RST、CORE_RST 与 D_RST | `mcu_reset=U2 PC6/pin 29/MCU_RST`；`pullup=R4 20K/1% to MCU_5V`；`capacitor=C9 22uF/10V`；`host_reset=BUS1 pin 25/CORE_RST`；`driver_reset=D_RST -> U3/U4/U5 pin 16` |
| 接口 | BUS1 M5_BUS 已用针脚 | `used_pinout=3:SYS_P050/5V,13:CORE_SCL/G22,14:CORE_SDA/G21,19:CORE_3V3,25:CORE_RST/EN,26:GND,27:CORE_RXD/G36,28:GND,29:CORE_TXD/G35,30:GND`；`reference=BUS1 M5_BUS` |
| 保护电路 | 电源与限位保护 | `output_ptc=FU1 1A/PTC`；`mcu_diode=D1 1N5819WS`；`limit_diodes=D4,D5,D6 1N4148`；`motor_tvs_visible=false`；`reverse_protection_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`position_inputs=END_X,END_Y,END_Z` |

## 待确认事项

- `other.microstep-truth-table`：产品正文给出 Full、1/2、1/4、1/8、1/16、1/32 微步组合，但原理图仅显示 M0/M1/M2 物理连接，未打印组合与微步倍率的对应表。（证据：图 5dd266361415 / 第 1 页 / 网格 A3 SH1041 至三颗 DRV8825 MODE0/1/2 的连接区域）
- `address.dip-switch`：SH1041 第四位连接 ADDR，并接 U2 PB1/pin 13；产品正文记载地址 0x70/0x71，但原理图未打印开关状态与地址的对应关系。（证据：图 5dd266361415 / 第 1 页 / 网格 A2-A3 U2 PB1/ADDR、R23/D_RST 网络与 SH1041 ADDR 开关）
- `review.microstep-truth-table`：SH1041 的 M0/M1/M2 各组合与 Full 至 1/32 微步倍率是否按产品正文表执行？；原因：原理图只给出 M0/M1/M2 物理连接，没有微步真值表。
- `review.i2c-address-map`：SH1041 ADDR 开关的两个状态是否分别对应产品正文记载的 0x70 与 0x71？；原因：原理图只显示 ADDR 到 U2 PB1 的硬件连接，没有打印地址映射。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5dd266361415f5c5144a04d7056b6448dc1d3997e29c2018ad06a5bdb7999300` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/546/Sch_M5GRBL_V1.1_sch_01.png` |

---

源文档：`zh_CN/module/grbl13.2.md`

源文档 SHA-256：`6846a37f2514f46b1efe414de278757e749e8d6809eccc4c72c4680eab08649d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
