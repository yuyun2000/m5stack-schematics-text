# Base M5GO Bottom2 v1.3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base M5GO Bottom2 v1.3 |
| SKU | A014-C-V13 |
| 产品 ID | `base-m5go-bottom2-v1-3-ccd29a0e34c3` |
| 源文档 | `zh_CN/base/m5go_bottom2_v1.3.md` |

## 概述

Base M5GO Bottom2 v1.3 原理图是一块由 Core2 通过 J4 M5Bus 控制的底座，包含 U1 BMI270 六轴 IMU、U2 LMD4020T261-OAC23 数字麦克风、LED1~LED10 SK6812 灯链和 U3 TP4057 电池充电器。G21/G22 I2C 同时连接 BMI270、未标型号的 U4 与 J3 磁吸电源/I2C 接口，BMI270 的 SDO 下拉使图示默认地址为 0x68。J1/J2 分别引出 UART 与 GPIO/ADC-DAC 网络；J3 VIN 经 TP4057 形成 BAT+ 并接到 M5Bus BATTERY，500mAh 容量与 U4 具体型号未在原理图中标出。

## 检索关键词

`Base M5GO Bottom2 v1.3`、`A014-C-V13`、`SCH Main V1.31`、`BMI270`、`0x68`、`0x69`、`LMD4020T261-OAC23`、`SPM1423`、`SK6812`、`TP4057`、`SS8550 Y2`、`M5Stack_BUS2`、`M5Bus`、`I2C_SDA`、`I2C_SCL`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO34`、`GPIO0`、`GPIO36`、`GPIO26`、`GPIO13`、`GPIO14`、`RGB`、`SK6812 data`、`DAT`、`CLK`、`U2_RXD`、`U2_TXD`、`VIN`、`BAT+`、`UART_Socket_4P`、`GPIO_Socket_4P`、`SOCKET_POWER_4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | BMI270 | 六轴 IMU，通过 I2C_SDA/I2C_SCL 连接 Core2，SDO 下拉选择默认地址 | 图 332b93b787b9 / 第 1 页 / 网格 B2-B3，U1 BMI270，SDX/SCX/SDO/CSB/VDD/VDDIO/GNDIO/GND |
| U2 | LMD4020T261-OAC23 | 数字麦克风，使用 DAT/CLK 接口，L/R 选择脚接地 | 图 332b93b787b9 / 第 1 页 / 网格 B1-C2，Microphone 分区 U2 LMD4020T261-OAC23，DATA/CLK/L/R/VDD/GND |
| LED1-LED10 | SK6812 | 十颗串行可编程 RGB LED，使用 +5V 供电，数据由 SK6812 网络依次级联 | 图 332b93b787b9 / 第 1 页 / 网格 A1-A4，LED1~LED10 SK6812，DIN/DOUT/VDD/VSS 串行链 |
| U3 | TP4057 | 单节锂电池充电管理器，VIN 输入、BAT+ 输出，并驱动 CHRG/STDBY 状态灯 | 图 332b93b787b9 / 第 1 页 / 网格 D1-D2，Power 分区 U3 TP4057，VCC/BAT/CHRG/STDBY/PROG/GND |
| U4 | 未标注 | 未标型号的 8-pin I2C 器件/预留位置，VCC=3.3V、SCL/SDA 接主 I2C，总计四个 NC 引脚 | 图 332b93b787b9 / 第 1 页 / 网格 D2-D3，U4 pins1-3/7 NC、pin4 GND、pin5 SDA、pin6 SCL、pin8 VCC |
| Q1 | SS8550 Y2 | RGB 到 SK6812 首灯数据网络的晶体管驱动/电平接口 | 图 332b93b787b9 / 第 1 页 / 网格 D2，Q1 SS8550 Y2，RGB 经 R8 到基极，SK6812 网络连接上端，另一端接 GND |
| D1 | 1615RG | TP4057 CHRG/STDBY 双色充电状态 LED | 图 332b93b787b9 / 第 1 页 / 网格 D1，D1 1615RG、R6 1K 与 U3 CHRG/STDBY |
| J1 | UART_Socket_4P | 四针 UART 扩展口，引出 U2_RXD、U2_TXD、+5V、GND | 图 332b93b787b9 / 第 1 页 / 网格 A4-B4，J1 UART_Socket_4P pins1-4 |
| J2 | GPIO_Socket_4P | 四针 GPIO 扩展口，引出 GPIO36、GPIO26、+5V、GND | 图 332b93b787b9 / 第 1 页 / 网格 B4，J2 GPIO_Socket_4P pins1-4 |
| J3 | SOCKET_POWER_4P | 磁吸电源/I2C 接口，引出 GND、VIN、I2C_SDA、I2C_SCL | 图 332b93b787b9 / 第 1 页 / 网格 B4，J3 SOCKET_POWER_4P pins1-4，GND/VIN/I2C_SDA/I2C_SCL |
| J4 | M5Stack_BUS2 | 30-pin M5Bus 主机接口，承载电源、电池、I2C、数字麦克风、RGB、UART 与 GPIO | 图 332b93b787b9 / 第 1 页 / 网格 C3-D4，J4 M5Stack_BUS2 pins1-30 |
| R2,R3 | 4.7KΩ | I2C_SDA/I2C_SCL 到 3.3V 的上拉电阻 | 图 332b93b787b9 / 第 1 页 / 网格 B3-B4 Socket 分区，R2 4.7K I2C_SDA、R3 4.7K I2C_SCL |
| R4,R5 | NC / 4.7KΩ | BMI270 SDO 地址选择网络，R4 为 3.3V 上拉预留，R5 为对地下拉 | 图 332b93b787b9 / 第 1 页 / 网格 B2，U1 SDO pin1，R4 NC 到 3.3V、R5 4.7K 到 GND |

## 系统结构

### Base M5GO Bottom2 v1.3 架构

底座通过 J4 M5Bus 连接外部 Core2，集成 BMI270、数字麦克风、十颗 SK6812、TP4057 充电器、未标型号 I2C 器件以及 UART/GPIO/磁吸电源-I2C 三组接口。

- 参数与网络：`host=J4 M5Stack_BUS2`；`imu=U1 BMI270`；`microphone=U2 LMD4020T261-OAC23`；`rgb=LED1-LED10 SK6812`；`charger=U3 TP4057`；`extra_i2c=U4 unmarked`；`sockets=J1,J2,J3`
- 证据：图 332b93b787b9 / 第 1 页 / 整页网格 A1-D4，各功能分区与 M5Bus

## 核心器件

### U4 未标型号 I2C 器件

U4 是 8-pin 符号：pin8 VCC 接 +3.3V、pin4 GND、pin5 SDA、pin6 SCL，pins1/2/3/7 均标 NC；图面没有器件型号、地址或功能名。

- 参数与网络：`reference=U4`；`part_number=null`；`vcc=pin8 +3.3V`；`ground=pin4`；`sda=pin5 I2C_SDA`；`scl=pin6 I2C_SCL`；`nc=pins1,2,3,7`；`address=null`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 D2-D3，U4 全部 pin 标注，无料号文字

## 电源

### 麦克风 3.3V 去耦

U2 VDD 使用 +3.3V，C1 10uF 与 C2 100nF 从 +3.3V 对地去耦。

- 参数与网络：`device=U2`；`rail=+3.3V`；`bulk_cap=C1 10uF`；`high_frequency_cap=C2 100nF`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 C1-C2，Microphone 分区 C1/C2 与 U2 VDD

### SK6812 供电

LED1~LED10 的 VDD pin4 均接 +5V，VSS pin2 均接 GND；R1 4.7K 从首灯数据输入 SK6812 网络上拉到 +5V。

- 参数与网络：`devices=LED1-LED10`；`supply=+5V`；`ground=VSS pin2`；`data_pullup=R1 4.7K to +5V`；`data_net=SK6812`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 A1-A4，十颗 SK6812 VDD/VSS 与 R1

### TP4057 充电路径

J3 pin2 的 VIN 连接 U3 TP4057 VCC pin4，U3 BAT pin3 输出 BAT+ 并连接 J4 pin30 BATTERY；C6/C7 各 10uF 分别对 VIN/BAT+ 去耦，PROG pin6 经 R9 2K 接地。

- 参数与网络：`charger=U3 TP4057`；`input=J3.2 VIN -> U3.4 VCC`；`output=U3.3 BAT -> BAT+ -> J4.30 BATTERY`；`input_cap=C6 10uF`；`battery_cap=C7 10uF`；`program_resistor=R9 2K`；`battery_capacity=null`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 D1-D4，J3 VIN、U3 TP4057、BAT+ 与 J4 pin30

### 5V、3.3V 与 BAT+ 电源轨

+5V 从 J4 pin28 分配到十颗 SK6812 和 J1/J2；+3.3V 从 J4 pin12 分配到 BMI270、麦克风、U4 与 I2C 上拉；BAT+ 由 TP4057 输出并接 J4 pin30。

- 参数与网络：`5v_source=J4 pin28`；`5v_loads=LED1-LED10,J1 pin3,J2 pin3`；`3v3_source=J4 pin12`；`3v3_loads=U1,U2,U4,R2,R3,R7`；`battery_rail=U3 BAT -> BAT+ -> J4 pin30`
- 证据：图 332b93b787b9 / 第 1 页 / 整页 +5V/+3.3V/BAT+ 网络追踪

## 接口

### J3 磁吸电源/I2C 接口

J3 SOCKET_POWER_4P pin1 为 GND、pin2 VIN、pin3 I2C_SDA、pin4 I2C_SCL；因此同一接口承载充电输入与 I2C 扩展。

- 参数与网络：`reference=J3`；`pin1=GND`；`pin2=VIN/charger input`；`pin3=I2C_SDA`；`pin4=I2C_SCL`；`power_direction=input to TP4057`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B4，J3 SOCKET_POWER_4P pins1-4 与黄色 SDA/SCL 标注

### J1 UART 四针接口

J1 UART_Socket_4P pin1 为 U2_RXD、pin2 U2_TXD、pin3 +5V、pin4 GND；U2_RXD/U2_TXD 分别延伸到 J4 pins15/16。

- 参数与网络：`reference=J1`；`pin1=U2_RXD -> J4.15 GPIO13`；`pin2=U2_TXD -> J4.16 GPIO14`；`pin3=+5V`；`pin4=GND`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 A4-C4，J1 U2_RXD/U2_TXD 到 J4 pins15/16

### J2 GPIO/ADC-DAC 四针接口

J2 GPIO_Socket_4P pin1 为 GPIO36、pin2 GPIO26、pin3 +5V、pin4 GND；GPIO36 与 GPIO26 分别连接 J4 pins4/10。

- 参数与网络：`reference=J2`；`pin1=GPIO36 -> J4.4`；`pin2=GPIO26 -> J4.10`；`pin3=+5V`；`pin4=GND`；`schematic_direction=not annotated`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B4-D4，J2 GPIO36/GPIO26 到 J4 pins4/10

### J4 M5Bus 关键引脚

J4 使用 pins1/3/5 GND、pin8 GPIO25/RGB、pin4 GPIO36、pin10 GPIO26、pin12 +3.3V、pins15/16 UART、pins17/18 I2C、pin24 GPIO0/CLK、pin26 GPIO34/DAT、pin28 +5V、pin30 BATTERY/BAT+。

- 参数与网络：`ground=pins1,3,5`；`rgb=pin8 GPIO25`；`gpio_socket=pin4 GPIO36,pin10 GPIO26`；`3v3=pin12`；`uart=pin15 GPIO13,pin16 GPIO14`；`i2c=pin17 GPIO21,pin18 GPIO22`；`microphone=pin24 GPIO0 CLK,pin26 GPIO34 DAT`；`5v=pin28`；`battery=pin30 BATTERY`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 C3-D4，J4 M5Stack_BUS2 pins1-30

## 总线

### 主 I2C 总线

J4 pin17 GPIO21 为 I2C_SDA、pin18 GPIO22 为 I2C_SCL；总线连接 U1 BMI270、U4 未标型号器件和 J3 pins3/4，并由 R2/R3 各 4.7K 上拉到 +3.3V。

- 参数与网络：`controller_connector=J4`；`sda=J4.17 GPIO21/I2C_SDA`；`scl=J4.18 GPIO22/I2C_SCL`；`devices=U1 BMI270,U4`；`external=J3 pins3,4`；`pullups=R2,R3 4.7K to +3.3V`；`level=3.3V`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B2-D4，I2C_SDA/I2C_SCL 从 J4 到 U1/U4/J3 与 R2/R3

### M5Bus 到数字麦克风 CLK/DAT

J4 pin24 GPIO0 连接 CLK 并驱动 U2 pin4，J4 pin26 GPIO34 连接 DAT 并接收 U2 pin3 数据。

- 参数与网络：`clock=J4.24 GPIO0 -> CLK -> U2.4`；`data=U2.3 -> DAT -> J4.26 GPIO34`；`device=U2 LMD4020T261-OAC23`；`supply_level=3.3V`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B1-C2 与 C4-D4，U2 DAT/CLK 到 J4 pins26/24

### Core2 UART2 扩展

J4 pin15 GPIO13 连接 U2_RXD 并到 J1 pin1 UART_RXD，J4 pin16 GPIO14 连接 U2_TXD 并到 J1 pin2 UART_TXD。

- 参数与网络：`host_rx=J4.15 GPIO13/U2_RXD`；`socket_rx=J1.1 UART_RXD`；`host_tx=J4.16 GPIO14/U2_TXD`；`socket_tx=J1.2 UART_TXD`；`power=+5V,GND`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 A4-D4，J1 与 J4 的 UART 网络

## 总线地址

### BMI270 I2C 地址

U1 SDO pin1 通过 R5 4.7K 下拉到 GND，R4 上拉位置标 NC；页内注记 SDO=0 时地址 0x68（default），SDO=1 时地址 0x69，因此图示装配地址为 0x68。

- 参数与网络：`device=U1 BMI270`；`sdo=pin1`；`pulldown=R5 4.7K`；`pullup_option=R4 NC`；`assembled_address=0x68`；`alternate_address=0x69`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B2，U1 SDO/R4/R5 与 SDO=0 add:0x68(default), SDO=1 add:0x69 注记

## GPIO 与控制信号

### BMI270 中断与辅助接口

BMI270 INT1 pin4、INT2 pin9、ASDX pin2、ASCX pin3、OSDO pin11 与 OCSB pin10 均以红色叉号标为未连接。

- 参数与网络：`interrupts=pin4 INT1 NC,pin9 INT2 NC`；`aux_i2c=pin2 ASDX NC,pin3 ASCX NC`；`ois_interface=pin11 OSDO NC,pin10 OCSB NC`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B2-B3，U1 右侧 INT/ASD/ASC/OSD/OCS 红色 NC 标记

### 十颗 SK6812 灯链

J4 pin8 GPIO25 的 RGB 网络经 R8 1K 与 Q1 SS8550 Y2 形成 SK6812 数据网络，进入 LED1 DIN；LED1 DOUT 依次连接 LED2~LED10 DIN，LED10 DOUT 未连接。

- 参数与网络：`host=J4 pin8 GPIO25`；`input_net=RGB`；`driver=R8 1K,Q1 SS8550 Y2`；`chain_input=SK6812 -> LED1 DIN`；`chain=LED1 DOUT through LED10 DIN`；`chain_output=LED10 DOUT NC`；`count=10`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 A1-A4/D2/C4，J4 RGB、Q1 与 LED1~LED10 数据链

### 充电状态指示

VIN 经 R6 1K 为 D1 1615RG 提供公共电源，D1 两路分别连接 U3 CHRG pin1 与 STDBY pin5，用于显示充电和待机状态。

- 参数与网络：`led=D1 1615RG`；`series_resistor=R6 1K`；`supply=VIN`；`charge_signal=U3 pin1 CHRG`；`standby_signal=U3 pin5 STDBY`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 D1，R6/D1 与 U3 CHRG/STDBY

## 时钟

### 板级时钟

本页未显示晶振或独立振荡器；麦克风 CLK 由 J4 GPIO0 提供，I2C SCL 由 J4 GPIO22 提供。

- 参数与网络：`crystal=null`；`oscillator=null`；`microphone_clock=J4.24 GPIO0/CLK`；`i2c_clock=J4.18 GPIO22/I2C_SCL`
- 证据：图 332b93b787b9 / 第 1 页 / 整页无 X/Y 器件；CLK 与 I2C_SCL 均来自 J4

## 复位

### 复位网络

本页没有连接到 BMI270、麦克风、SK6812、TP4057 或 U4 的外部复位网络；J4 EN pin6 以红色叉号标为未连接。

- 参数与网络：`board_reset=null`；`m5bus_en=J4 pin6 NC`；`imu_reset=null`；`u4_reset=null`
- 证据：图 332b93b787b9 / 第 1 页 / 整页器件无 RESET；网格 C4 J4 EN pin6 红色 NC

## 保护电路

### 外部接口保护

J1/J2/J3 与 M5Bus 信号在本页未显示专用 TVS/ESD、保险丝或反接保护器件；可见保护相关功能主要是 TP4057 充电管理本身。

- 参数与网络：`tvS_esd=null`；`fuse=null`；`reverse_protection=null`；`charger=U3 TP4057`
- 证据：图 332b93b787b9 / 第 1 页 / 整页 J1/J2/J3/J4 与电源区，无 TVS/ESD/Fuse 标注

## 关键网络

### 主机到功能模块关键映射

GPIO21/22 -> I2C -> BMI270/U4/J3；GPIO0/34 -> CLK/DAT -> 麦克风；GPIO25 -> RGB/Q1 -> SK6812 灯链；GPIO13/14 -> UART J1；GPIO36/26 -> J2。

- 参数与网络：`i2c=GPIO21/GPIO22 -> U1,U4,J3`；`microphone=GPIO0 CLK,GPIO34 DAT -> U2`；`rgb=GPIO25 -> RGB -> Q1 -> LED1-LED10`；`uart=GPIO13/GPIO14 -> J1`；`gpio=GPIO36/GPIO26 -> J2`
- 证据：图 332b93b787b9 / 第 1 页 / 整页 J4 与 U1/U2/Q1/LED/J1/J2/J3 网络追踪

## 存储

### 板级存储

本页没有明确标注的 Flash、EEPROM、eMMC 或存储卡接口；U4 型号未知，不能将其确定为存储器。

- 参数与网络：`flash=null`；`eeprom_confirmed=null`；`emmc=null`；`storage_card=null`；`u4_role=unknown`
- 证据：图 332b93b787b9 / 第 1 页 / 整页无存储器件型号；U4 仅有无型号 I2C 符号

## 内存与 Flash

### 外部内存

本页没有主控 SoC、RAM、PSRAM 或 DDR 器件。

- 参数与网络：`soc=null`；`ram=null`；`psram=null`；`ddr=null`
- 证据：图 332b93b787b9 / 第 1 页 / 整页为底座外设与连接器，无主控/内存

## 音频

### 数字麦克风接口

U2 LMD4020T261-OAC23 由 +3.3V 供电，DATA pin3 连接 DAT，CLK pin4 连接 CLK，L/R pin6 接 GND，pins2/5 GND 接地。

- 参数与网络：`reference=U2`；`part_number=LMD4020T261-OAC23`；`supply=pin1 +3.3V`；`data=pin3 DAT`；`clock=pin4 CLK`；`channel_select=pin6 L/R=GND`；`ground=pins2,5`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B1-C2，U2 数字麦克风 pins1-6

## 传感器

### BMI270 六轴 IMU

U1 明确标为 BMI270，VDD pin8、VDDIO pin5 与 CSB pin12 接 +3.3V，SDX pin14 接 I2C_SDA，SCX pin13 接 I2C_SCL，GNDIO pin6 与 GND pin7 接地。

- 参数与网络：`reference=U1`；`part_number=BMI270`；`vdd=pin8 +3.3V`；`vddio=pin5 +3.3V`；`mode_strap=pin12 CSB +3.3V`；`sda=pin14 SDX/I2C_SDA`；`scl=pin13 SCX/I2C_SCL`；`ground=pins6,7`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 B2-B3，U1 BMI270 pins1-14

## 射频

### 射频电路

本页未显示射频收发器、天线或射频匹配网络。

- 参数与网络：`rf_ic=null`；`antenna=null`；`matching=null`
- 证据：图 332b93b787b9 / 第 1 页 / 整页无 RF/ANT 分区或器件

## 调试与烧录

### 调试接口

本页未显示 SWD、JTAG、专用调试连接器或测试点；UART J1 是通用扩展口。

- 参数与网络：`swd=null`；`jtag=null`；`test_points=null`；`uart_extension=J1`
- 证据：图 332b93b787b9 / 第 1 页 / 整页无 Debug/TP/SWD/JTAG 标记

## 模拟电路

### TP4057 充电设定网络

U3 PROG pin6 经 R9 2K 接 GND，VIN/BAT+ 分别配置 C6/C7 10uF；原理图未给出由 R9 对应的数值充电电流。

- 参数与网络：`charger=U3 TP4057`；`program_pin=pin6 PROG`；`program_resistor=R9 2K to GND`；`input_cap=C6 10uF`；`battery_cap=C7 10uF`；`charge_current_mark=null`
- 证据：图 332b93b787b9 / 第 1 页 / 网格 D1-D2，U3 PROG/R9 与 C6/C7

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base M5GO Bottom2 v1.3 架构 | `host=J4 M5Stack_BUS2`；`imu=U1 BMI270`；`microphone=U2 LMD4020T261-OAC23`；`rgb=LED1-LED10 SK6812`；`charger=U3 TP4057`；`extra_i2c=U4 unmarked`；`sockets=J1,J2,J3` |
| 传感器 | BMI270 六轴 IMU | `reference=U1`；`part_number=BMI270`；`vdd=pin8 +3.3V`；`vddio=pin5 +3.3V`；`mode_strap=pin12 CSB +3.3V`；`sda=pin14 SDX/I2C_SDA`；`scl=pin13 SCX/I2C_SCL`；`ground=pins6,7` |
| 总线地址 | BMI270 I2C 地址 | `device=U1 BMI270`；`sdo=pin1`；`pulldown=R5 4.7K`；`pullup_option=R4 NC`；`assembled_address=0x68`；`alternate_address=0x69` |
| 总线 | 主 I2C 总线 | `controller_connector=J4`；`sda=J4.17 GPIO21/I2C_SDA`；`scl=J4.18 GPIO22/I2C_SCL`；`devices=U1 BMI270,U4`；`external=J3 pins3,4`；`pullups=R2,R3 4.7K to +3.3V`；`level=3.3V` |
| GPIO 与控制信号 | BMI270 中断与辅助接口 | `interrupts=pin4 INT1 NC,pin9 INT2 NC`；`aux_i2c=pin2 ASDX NC,pin3 ASCX NC`；`ois_interface=pin11 OSDO NC,pin10 OCSB NC` |
| 音频 | 数字麦克风接口 | `reference=U2`；`part_number=LMD4020T261-OAC23`；`supply=pin1 +3.3V`；`data=pin3 DAT`；`clock=pin4 CLK`；`channel_select=pin6 L/R=GND`；`ground=pins2,5` |
| 总线 | M5Bus 到数字麦克风 CLK/DAT | `clock=J4.24 GPIO0 -> CLK -> U2.4`；`data=U2.3 -> DAT -> J4.26 GPIO34`；`device=U2 LMD4020T261-OAC23`；`supply_level=3.3V` |
| 电源 | 麦克风 3.3V 去耦 | `device=U2`；`rail=+3.3V`；`bulk_cap=C1 10uF`；`high_frequency_cap=C2 100nF` |
| GPIO 与控制信号 | 十颗 SK6812 灯链 | `host=J4 pin8 GPIO25`；`input_net=RGB`；`driver=R8 1K,Q1 SS8550 Y2`；`chain_input=SK6812 -> LED1 DIN`；`chain=LED1 DOUT through LED10 DIN`；`chain_output=LED10 DOUT NC`；`count=10` |
| 电源 | SK6812 供电 | `devices=LED1-LED10`；`supply=+5V`；`ground=VSS pin2`；`data_pullup=R1 4.7K to +5V`；`data_net=SK6812` |
| 电源 | TP4057 充电路径 | `charger=U3 TP4057`；`input=J3.2 VIN -> U3.4 VCC`；`output=U3.3 BAT -> BAT+ -> J4.30 BATTERY`；`input_cap=C6 10uF`；`battery_cap=C7 10uF`；`program_resistor=R9 2K`；`battery_capacity=null` |
| GPIO 与控制信号 | 充电状态指示 | `led=D1 1615RG`；`series_resistor=R6 1K`；`supply=VIN`；`charge_signal=U3 pin1 CHRG`；`standby_signal=U3 pin5 STDBY` |
| 接口 | J3 磁吸电源/I2C 接口 | `reference=J3`；`pin1=GND`；`pin2=VIN/charger input`；`pin3=I2C_SDA`；`pin4=I2C_SCL`；`power_direction=input to TP4057` |
| 接口 | J1 UART 四针接口 | `reference=J1`；`pin1=U2_RXD -> J4.15 GPIO13`；`pin2=U2_TXD -> J4.16 GPIO14`；`pin3=+5V`；`pin4=GND` |
| 总线 | Core2 UART2 扩展 | `host_rx=J4.15 GPIO13/U2_RXD`；`socket_rx=J1.1 UART_RXD`；`host_tx=J4.16 GPIO14/U2_TXD`；`socket_tx=J1.2 UART_TXD`；`power=+5V,GND` |
| 接口 | J2 GPIO/ADC-DAC 四针接口 | `reference=J2`；`pin1=GPIO36 -> J4.4`；`pin2=GPIO26 -> J4.10`；`pin3=+5V`；`pin4=GND`；`schematic_direction=not annotated` |
| 接口 | J4 M5Bus 关键引脚 | `ground=pins1,3,5`；`rgb=pin8 GPIO25`；`gpio_socket=pin4 GPIO36,pin10 GPIO26`；`3v3=pin12`；`uart=pin15 GPIO13,pin16 GPIO14`；`i2c=pin17 GPIO21,pin18 GPIO22`；`microphone=pin24 GPIO0 CLK,pin26 GPIO34 DAT`；`5v=pin28`；`battery=pin30 BATTERY` |
| 核心器件 | U4 未标型号 I2C 器件 | `reference=U4`；`part_number=null`；`vcc=pin8 +3.3V`；`ground=pin4`；`sda=pin5 I2C_SDA`；`scl=pin6 I2C_SCL`；`nc=pins1,2,3,7`；`address=null` |
| 电源 | 5V、3.3V 与 BAT+ 电源轨 | `5v_source=J4 pin28`；`5v_loads=LED1-LED10,J1 pin3,J2 pin3`；`3v3_source=J4 pin12`；`3v3_loads=U1,U2,U4,R2,R3,R7`；`battery_rail=U3 BAT -> BAT+ -> J4 pin30` |
| 关键网络 | 主机到功能模块关键映射 | `i2c=GPIO21/GPIO22 -> U1,U4,J3`；`microphone=GPIO0 CLK,GPIO34 DAT -> U2`；`rgb=GPIO25 -> RGB -> Q1 -> LED1-LED10`；`uart=GPIO13/GPIO14 -> J1`；`gpio=GPIO36/GPIO26 -> J2` |
| 模拟电路 | TP4057 充电设定网络 | `charger=U3 TP4057`；`program_pin=pin6 PROG`；`program_resistor=R9 2K to GND`；`input_cap=C6 10uF`；`battery_cap=C7 10uF`；`charge_current_mark=null` |
| 时钟 | 板级时钟 | `crystal=null`；`oscillator=null`；`microphone_clock=J4.24 GPIO0/CLK`；`i2c_clock=J4.18 GPIO22/I2C_SCL` |
| 复位 | 复位网络 | `board_reset=null`；`m5bus_en=J4 pin6 NC`；`imu_reset=null`；`u4_reset=null` |
| 保护电路 | 外部接口保护 | `tvS_esd=null`；`fuse=null`；`reverse_protection=null`；`charger=U3 TP4057` |
| 调试与烧录 | 调试接口 | `swd=null`；`jtag=null`；`test_points=null`；`uart_extension=J1` |
| 存储 | 板级存储 | `flash=null`；`eeprom_confirmed=null`；`emmc=null`；`storage_card=null`；`u4_role=unknown` |
| 内存与 Flash | 外部内存 | `soc=null`；`ram=null`；`psram=null`；`ddr=null` |
| 射频 | 射频电路 | `rf_ic=null`；`antenna=null`；`matching=null` |
| 核心器件 | 数字麦克风型号冲突 | `reference=U2`；`schematic_model=LMD4020T261-OAC23`；`documented_model=SPM1423`；`assembled_model=null` |
| 核心器件 | U4 具体型号与用途 | `reference=U4`；`part_number=null`；`bus=I2C_SDA,I2C_SCL`；`supply=3.3V`；`address=null`；`role=null` |
| 电源 | 内置电池容量 | `documented_capacity=500mAh`；`charger=U3 TP4057`；`battery_net=BAT+`；`battery_connector=null`；`schematic_capacity=null` |

## 待确认事项

- `component.microphone-model-conflict`：产品正文称麦克风为 SPM1423，但当前原理图 U2 明确标为 LMD4020T261-OAC23；需要以量产 BOM 或丝印确认 v1.3 实际装配型号。（证据：图 332b93b787b9 / 第 1 页 / 网格 B1-C2，U2 器件文字 LMD4020T261-OAC23）
- `component.u4-identification`：U4 连接 3.3V、GND、I2C_SCL、I2C_SDA，其他四脚 NC，但原理图没有料号、功能名或地址，无法确定其器件类型。（证据：图 332b93b787b9 / 第 1 页 / 网格 D2-D3，U4 无器件型号/地址标注）
- `power.documented-battery-capacity`：正文称内置锂电池为 500mAh；原理图仅显示 TP4057、BAT+ 网络与 J4 BATTERY pin30，没有电池位号、型号或容量标注。（证据：图 332b93b787b9 / 第 1 页 / 网格 D1-D4，U3 BAT 输出到 BAT+/J4 pin30，无电池器件与容量）
- `review.microphone-model`：请用 v1.3 量产 BOM 或 U2 实物丝印确认数字麦克风是 LMD4020T261-OAC23 还是 SPM1423。；原因：当前正式原理图与产品正文的麦克风型号不一致。
- `review.u4`：请用 BOM、PCB 丝印或原始设计库确认 U4 的具体型号、功能和 I2C 地址。；原因：U4 符号只有引脚连接，没有料号、功能名与地址。
- `review.battery-capacity`：请用电池标签、BOM 或容量测试确认内置锂电池为 500mAh。；原因：原理图只显示 BAT+ 充电网络，不显示电池规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `332b93b787b976cf93080ec6799f34395781165be0dd2608f7108287c7a7221b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1227/SCH_M5GO_Bottom2_SCH_Main_V1.31_2026_03_16_10_32_04_page_01.png` |

---

源文档：`zh_CN/base/m5go_bottom2_v1.3.md`

源文档 SHA-256：`c66cd642f12c6cdb358093aa9e7941004abb36ef07f4a0eb3b50cae0ab091896`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
