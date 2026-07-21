# Base M5GO Bottom2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base M5GO Bottom2 |
| SKU | A014-C |
| 产品 ID | `base-m5go-bottom2-fc60f6c5b664` |
| 源文档 | `zh_CN/base/m5go_bottom2.md` |

## 概述

Base M5GO Bottom2 通过 J4 M5Stack_BUS2 连接外部 M5 主机，板载 U1 MPU-6886 I2C 惯性传感器、U2 SPM1423HM4H-B 数字麦克风和 LED1-LED10 十颗级联 SK6812。GPIO25 的 RGB 网络经 Q1 SS8550 Y2 驱动 SK6812 数据链，GPIO0/GPIO34 连接麦克风 CLK/DAT，GPIO21/GPIO22 构成 MPU-6886 与 Pogo 接口共用的 I2C 总线。J3 Pogo 的 VIN 进入 U3 TP4057，输出 BAT+ 到 M5_BUS 电池针脚；J1/J2 另引出 UART 和 GPIO 扩展。

## 检索关键词

`Base M5GO Bottom2`、`A014-C`、`MPU-6886`、`SPM1423HM4H-B`、`TP4057`、`SK6812`、`SK6812 x10`、`SS8550 Y2`、`1615RG`、`M5Stack_BUS2`、`RGB GPIO25`、`DAT GPIO34`、`CLK GPIO0`、`I2C_SDA GPIO21`、`I2C_SCL GPIO22`、`U2_RXD GPIO13`、`U2_TXD GPIO14`、`GPIO36`、`GPIO26`、`J1 UART_Socket_4P`、`J2 GPIO_Socket_4P`、`J3 SOCKET_POWER_4P`、`J4 M5Stack_BUS`、`VIN`、`BAT+`、`+5V`、`+3.3V`、`CHRG`、`STDBY`、`PROG`、`AD0/SDO`、`I2C`、`I2S`、`Pogo Pin`、`HY2.0-4P`、`RGB LED`、`digital microphone`、`IMU`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED10 | SK6812 | 十颗串联可编程 RGB LED，统一由 +5V/GND 供电 | 图 476163941d62 / 第 1 页 / 网格 A1-A4：LED1 至 LED10，均标 SK6812，DIN/DOUT 串接且 VDD=+5V、VSS=GND |
| U1 | MPU-6886 | I2C 惯性传感器，连接 I2C_SCL/I2C_SDA、地址选择和 3.3V 电源 | 图 476163941d62 / 第 1 页 / 网格 B2-C3：U1 MPU-6886，SCL/SCLK、SDA/SDI、AD0/SDO、CS、INT、VDD/VDDIO |
| U2 | SPM1423HM4H-B | 3.3V 数字麦克风，DAT/CLK 连接 M5_BUS，SELECT 接地 | 图 476163941d62 / 第 1 页 / 网格 B1-C2：U2 SPM1423HM4H-B，GND/SELECT/DAT/CLK/3V3 六脚 |
| U3 | TP4057 | 由 VIN 为 BAT+ 充电的单节电池充电控制器，连接双状态 LED 和 PROG 电阻 | 图 476163941d62 / 第 1 页 / 网格 C1-D2 Power 区：U3 TP4057 的 VCC/BAT/CHRG/STDBY/PROG/GND |
| Q1 | SS8550 Y2 | 连接 RGB 控制网络与 SK6812 数据输入网络的晶体管 | 图 476163941d62 / 第 1 页 / 网格 D2：Q1 SS8550 Y2，基极经 R8 接 RGB，上端接 SK6812、下端接 GND |
| D1,R6 | 1615RG / 1KΩ | TP4057 CHRG/STDBY 双颜色充电状态指示器及 VIN 侧限流电阻 | 图 476163941d62 / 第 1 页 / 网格 C1-D1：D1 1615RG、R6 1KΩ、VIN 与 U3 CHRG/STDBY |
| R1,R7,R8 | 4.7KΩ / 4.7KΩ / 1KΩ | SK6812 数据输入上拉及 RGB 到 Q1 的驱动网络 | 图 476163941d62 / 第 1 页 / 网格 A1 的 SK6812-R1-+5V，以及网格 D2 的 +3.3V-R7-RGB-R8-Q1 |
| R2,R3 | 4.7KΩ | I2C_SDA 与 I2C_SCL 到 +3.3V 的上拉电阻 | 图 476163941d62 / 第 1 页 / 网格 B3：R2/R3 4.7KΩ 分别从 I2C_SDA/I2C_SCL 上拉至 +3.3V |
| R4,R5 | NC / 4.7KΩ | MPU-6886 AD0/SDO 地址选择网络，默认通过 R5 下拉到 GND | 图 476163941d62 / 第 1 页 / 网格 B2-C2：+3.3V-R4(NC)-AD0/SDO 与 R5 4.7KΩ-GND |
| R9,C6,C7 | 2KΩ / 10uF / 10uF | TP4057 PROG 设置和 VIN/BAT+ 输入输出旁路网络 | 图 476163941d62 / 第 1 页 / 网格 C1-D2：U3 PROG-R9 2KΩ-GND、VIN-C6 10uF、BAT+-C7 10uF |
| J1 | UART_Socket_4P | 引出 U2_RXD、U2_TXD、+5V 和 GND 的四针 UART 接口 | 图 476163941d62 / 第 1 页 / 网格 A4-B4 Socket 区：J1 UART_Socket_4P pins1-4 |
| J2 | GPIO_Socket_4P | 引出 GPIO36、GPIO26、+5V 和 GND 的四针 GPIO 接口 | 图 476163941d62 / 第 1 页 / 网格 B4：J2 GPIO_Socket_4P pins1-4 |
| J3 | SOCKET_POWER_4P | Pogo/磁吸接口，引出 GND、VIN、I2C_SDA 和 I2C_SCL | 图 476163941d62 / 第 1 页 / 网格 B4-C4：J3 SOCKET_POWER_4P，外部网络 GND/VIN/I2C_SDA/I2C_SCL |
| J4 | M5Stack_BUS2 | 30 针 Core2 堆叠总线，连接 RGB、UART、I2C、麦克风、电源和电池网络 | 图 476163941d62 / 第 1 页 / 网格 C4-D4：J4 M5Stack_BUS2 pins1-30 与网络标注 |

## 系统结构

### Base M5GO Bottom2 系统架构

J4 连接外部 M5 主机；板载 U1 MPU-6886、U2 SPM1423HM4H-B、十颗 SK6812 与 U3 TP4057，J1/J2/J3 分别引出 UART、GPIO 和 Pogo 电源/I2C。

- 参数与网络：`host=external M5 host via J4 M5Stack_BUS2`；`imu=U1 MPU-6886`；`microphone=U2 SPM1423HM4H-B`；`rgb=LED1-LED10 SK6812`；`charger=U3 TP4057`；`interfaces=J1 UART, J2 GPIO, J3 Pogo power/I2C`
- 证据：图 476163941d62 / 第 1 页 / 第 1 页完整单页：RGB、Microphone、Power、Socket 与 M5Bus 功能区

### 本页未集成的系统功能

当前完整单页未画出通用主控、协处理器、Flash/PSRAM/SD 存储、晶振、射频或专用调试接口；控制由 J4 外部 M5 主机提供。

- 参数与网络：`general_mcu_shown=false`；`coprocessor_shown=false`；`storage_shown=false`；`crystal_shown=false`；`rf_shown=false`；`debug_connector_shown=false`；`external_host=M5 host via J4`
- 证据：图 476163941d62 / 第 1 页 / 第 1 页完整单页器件与连接器范围

## 核心器件

### RGB 到 SK6812 驱动网络

+3.3V 经 R7 4.7KΩ 接 RGB 节点，RGB 经 R8 1KΩ 驱动 Q1 SS8550 Y2；Q1 连接 SK6812 数据网络与 GND。

- 参数与网络：`input=RGB / GPIO25`；`pullup=R7 4.7KΩ to +3.3V`；`base_resistor=R8 1KΩ`；`transistor=Q1 SS8550 Y2`；`output=SK6812`；`return=GND`
- 证据：图 476163941d62 / 第 1 页 / 网格 D2：+3.3V-R7-RGB-R8-Q1-SK6812/GND

## 电源

### SK6812 电源连接

LED1-LED10 的 VDD pin4 均接 +5V，VSS pin2 均接 GND；首颗数据网络 SK6812 通过 R1 4.7KΩ 上拉到 +5V。

- 参数与网络：`devices=LED1-LED10 SK6812`；`supply=+5V`；`ground=GND`；`data_pullup=R1 4.7KΩ from SK6812 to +5V`
- 证据：图 476163941d62 / 第 1 页 / 网格 A1-A4：十颗 LED 的 VDD/VSS 与左侧 R1

### TP4057 充电路径

J3 pin2 的 VIN 接 U3 VCC pin4，U3 BAT pin3 输出 BAT+，PROG pin6 经 R9 2KΩ 接 GND；C6/C7 各 10uF 分别从 VIN/BAT+ 接地。

- 参数与网络：`input=J3 pin2 VIN -> U3 pin4 VCC`；`charger=U3 TP4057`；`battery_net=U3 pin3 BAT -> BAT+`；`program_resistor=R9 2KΩ to GND`；`input_capacitor=C6 10uF`；`battery_capacitor=C7 10uF`
- 证据：图 476163941d62 / 第 1 页 / 网格 C1-D2 Power：VIN/U3/BAT+/R9/C6/C7

### TP4057 充电状态指示

VIN 经 R6 1KΩ 为 D1 1615RG 双颜色 LED 公共节点供电，D1 两路分别连接 U3 CHRG pin1 与 STDBY pin5。

- 参数与网络：`indicator=D1 1615RG`；`series_resistor=R6 1KΩ from VIN`；`charge_output=U3 pin1 CHRG`；`standby_output=U3 pin5 STDBY`
- 证据：图 476163941d62 / 第 1 页 / 网格 C1-D1：VIN/R6/D1 与 U3 CHRG/STDBY

### BAT+ 到 M5_BUS

U3 BAT pin3 的 BAT+ 网络连接 J4 pin30 BATTERY；当前页面没有画出独立电池连接器、电芯、保护板或 BAT+ 到其他负载的支路。

- 参数与网络：`charger_output=U3 pin3 BAT`；`net=BAT+`；`host_bus=J4 pin30 BATTERY`；`cell_symbol_shown=false`；`battery_connector_shown=false`；`protection_ic_shown=false`
- 证据：图 476163941d62 / 第 1 页 / 网格 C1-D4：U3 BAT+ 与 J4 pin30 同名网络，完整页无电芯或保护 IC

## 接口

### J4 M5Stack_BUS2 已连接针脚

J4 pins1/3/5 接 GND，pin8 RGB/GPIO25，pin10 GPIO26，pin12 +3.3V，pin15 U2_RXD/GPIO13，pin16 U2_TXD/GPIO14，pin17 I2C_SDA/GPIO21，pin18 I2C_SCL/GPIO22，pin24 CLK/GPIO0，pin26 DAT/GPIO34，pin28 +5V，pin30 BAT+。

- 参数与网络：`ground=pins1,3,5`；`rgb=pin8 RGB / GPIO25`；`gpio_port=pin4 GPIO36; pin10 GPIO26`；`uart=pin15 U2_RXD/GPIO13; pin16 U2_TXD/GPIO14`；`i2c=pin17 I2C_SDA/GPIO21; pin18 I2C_SCL/GPIO22`；`microphone=pin24 CLK/GPIO0; pin26 DAT/GPIO34`；`power=pin12 +3.3V; pin28 +5V; pin30 BAT+`
- 证据：图 476163941d62 / 第 1 页 / 网格 C4-D4：J4 M5Stack_BUS2 pins1-30 与外部网络

### J1 UART 四针接口

J1 pin1=U2_RXD、pin2=U2_TXD、pin3=+5V、pin4=GND；U2_RXD 连接 J4 pin15 GPIO13，U2_TXD 连接 J4 pin16 GPIO14。

- 参数与网络：`pin1=U2_RXD -> GPIO13 / J4 pin15`；`pin2=U2_TXD -> GPIO14 / J4 pin16`；`pin3=+5V`；`pin4=GND`；`rx_direction=socket to host`；`tx_direction=host to socket`
- 证据：图 476163941d62 / 第 1 页 / 网格 A4-B4 与 C4-D4：J1 pins1-4、U2_RXD/U2_TXD 与 J4 pins15/16

### J2 GPIO 四针接口

J2 pin1=GPIO36、pin2=GPIO26、pin3=+5V、pin4=GND；GPIO36 与 GPIO26 分别连接 J4 pins4/10。

- 参数与网络：`pin1=GPIO36 / J4 pin4`；`pin2=GPIO26 / J4 pin10`；`pin3=+5V`；`pin4=GND`；`gpio36_function_label=null`；`gpio26_function_label=null`
- 证据：图 476163941d62 / 第 1 页 / 网格 B4-D4：J2 pins1-4 与 J4 GPIO36/GPIO26

### J3 Pogo 电源与 I2C 接口

J3 SOCKET_POWER_4P 的 pin1=GND、pin2=VIN、pin3=I2C_SDA、pin4=I2C_SCL；符号内 pin2 功能标 +5V，VIN 同名网络进入 TP4057 VCC。

- 参数与网络：`pin1=GND`；`pin2=VIN / symbol +5V -> U3 VCC`；`pin3=I2C_SDA / GPIO21`；`pin4=I2C_SCL / GPIO22`；`power_direction=external VIN into charger`；`bus_direction=bidirectional I2C`
- 证据：图 476163941d62 / 第 1 页 / 网格 B4-C4 与 C1-D2：J3 pins1-4、VIN/I2C 网络及 U3 VCC

## 总线

### 数字麦克风时钟与数据总线

外部 Core2 通过 GPIO0 输出 CLK 到 U2，U2 通过 GPIO34 的 DAT 向主机输出数字音频数据；页面未画出独立 WS/LRCK 网络。

- 参数与网络：`controller=external Core2`；`clock_direction=GPIO0/J4 pin24 -> U2 CLK pin4`；`data_direction=U2 DAT pin5 -> GPIO34/J4 pin26`；`word_select_shown=false`；`select_pin=U2 SELECT tied GND`
- 证据：图 476163941d62 / 第 1 页 / 网格 B1-D4：U2 CLK/DAT 与 J4 pins24/26；完整页无 WS/LRCK 网络

### MPU-6886 与 Pogo 共用 I2C

I2C_SDA/I2C_SCL 分别连接 J4 pins17/18、U1 pins24/23 和 J3 pins3/4，并通过 R2/R3 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`controller=external Core2`；`sda=GPIO21 / J4 pin17 / U1 pin24 / J3 pin3`；`scl=GPIO22 / J4 pin18 / U1 pin23 / J3 pin4`；`pullups=R2/R3 4.7KΩ to +3.3V`；`onboard_device=U1 MPU-6886`；`external_extension=J3 Pogo`
- 证据：图 476163941d62 / 第 1 页 / 网格 B2-D4：U1、R2/R3、J3 与 J4 的 I2C_SDA/I2C_SCL 同名网络

## GPIO 与控制信号

### 十颗 SK6812 数据链

J4 pin8 的 RGB/GPIO25 经 Q1 驱动形成 SK6812 网络并进入 LED1 DIN；LED1 DOUT 依次连接 LED2 DIN，直至 LED10，LED10 DOUT 未连接。

- 参数与网络：`host_gpio=GPIO25 / J4 pin8 RGB`；`driver=Q1 SS8550 Y2 with R7/R8`；`input_net=SK6812`；`chain=LED1 -> LED2 -> LED3 -> LED4 -> LED5 -> LED6 -> LED7 -> LED8 -> LED9 -> LED10`；`last_dout=LED10 DOUT NC`
- 证据：图 476163941d62 / 第 1 页 / 网格 A1-A4 与 D2：Q1/SK6812 输入、LED1-LED10 DIN/DOUT 连线、LED10 DOUT NC

### MPU-6886 中断和同步信号

U1 INT pin12、REGOUT pin10 和 FSYNC pin11 在当前页面标为未连接。

- 参数与网络：`interrupt=pin12 INT NC`；`regout=pin10 REGOUT NC`；`fsync=pin11 FSYNC NC`
- 证据：图 476163941d62 / 第 1 页 / 网格 B2：U1 INT/REGOUT/FSYNC 引脚旁红色 NC 标记

## 关键网络

### 主要电源网络

+5V 从 J4 pin28 供给十颗 SK6812 及 J1/J2；+3.3V 从 J4 pin12 供给 MPU-6886、SPM1423、I2C 上拉和 RGB 驱动；VIN 来自 J3 充电接口，BAT+ 连接 U3 与 J4 pin30。

- 参数与网络：`five_volt=J4 pin28 -> LED1-LED10, J1 pin3, J2 pin3`；`three_volt=J4 pin12 -> U1, U2, R2/R3/R7`；`charger_input=J3 pin2 VIN`；`battery=U3 BAT -> BAT+ -> J4 pin30`
- 证据：图 476163941d62 / 第 1 页 / 第 1 页 +5V/+3.3V/VIN/BAT+ 同名网络与 J1-J4/U1-U3/LED1-10

## 音频

### SPM1423HM4H-B 数字麦克风

U2 pin6 接 +3.3V，pins1/3 GND 与 pin2 SELECT 均接 GND，pin5 DAT 接 J4 pin26 GPIO34，pin4 CLK 接 J4 pin24 GPIO0。

- 参数与网络：`part=U2 SPM1423HM4H-B`；`supply=pin6 +3.3V`；`ground=pins1,3 GND`；`select=pin2 SELECT -> GND`；`data=pin5 DAT -> GPIO34 / J4 pin26`；`clock=pin4 CLK -> GPIO0 / J4 pin24`；`decoupling=C1 10uF; C2 100nF`
- 证据：图 476163941d62 / 第 1 页 / 网格 B1-C2：U2 SPM1423HM4H-B、DAT/CLK/SELECT、C1/C2 与 J4 DAT/CLK

## 传感器

### MPU-6886 I2C 连接

U1 SCL/SCLK pin23 接 I2C_SCL，SDA/SDI pin24 接 I2C_SDA，CS pin22 接 +3.3V，AD0/SDO pin9 通过 R5 4.7KΩ 下拉到 GND且到 +3.3V 的 R4 标为 NC；VDD pin13 和 VDDIO pin8 接 +3.3V。

- 参数与网络：`device=U1 MPU-6886`；`scl=pin23 I2C_SCL`；`sda=pin24 I2C_SDA`；`cs=pin22 +3.3V`；`address_select=pin9 AD0/SDO -> R5 4.7KΩ -> GND; R4 to +3.3V is NC`；`supply=VDD pin13 and VDDIO pin8 -> +3.3V`；`decoupling=C3 10uF; C4/C5 100nF`
- 证据：图 476163941d62 / 第 1 页 / 网格 B2-C3：U1 MPU-6886、R4/R5、I2C 和 C3-C5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base M5GO Bottom2 系统架构 | `host=external M5 host via J4 M5Stack_BUS2`；`imu=U1 MPU-6886`；`microphone=U2 SPM1423HM4H-B`；`rgb=LED1-LED10 SK6812`；`charger=U3 TP4057`；`interfaces=J1 UART, J2 GPIO, J3 Pogo power/I2C` |
| 接口 | J4 M5Stack_BUS2 已连接针脚 | `ground=pins1,3,5`；`rgb=pin8 RGB / GPIO25`；`gpio_port=pin4 GPIO36; pin10 GPIO26`；`uart=pin15 U2_RXD/GPIO13; pin16 U2_TXD/GPIO14`；`i2c=pin17 I2C_SDA/GPIO21; pin18 I2C_SCL/GPIO22`；`microphone=pin24 CLK/GPIO0; pin26 DAT/GPIO34`；`power=pin12 +3.3V; pin28 +5V; pin30 BAT+` |
| GPIO 与控制信号 | 十颗 SK6812 数据链 | `host_gpio=GPIO25 / J4 pin8 RGB`；`driver=Q1 SS8550 Y2 with R7/R8`；`input_net=SK6812`；`chain=LED1 -> LED2 -> LED3 -> LED4 -> LED5 -> LED6 -> LED7 -> LED8 -> LED9 -> LED10`；`last_dout=LED10 DOUT NC` |
| 电源 | SK6812 电源连接 | `devices=LED1-LED10 SK6812`；`supply=+5V`；`ground=GND`；`data_pullup=R1 4.7KΩ from SK6812 to +5V` |
| 核心器件 | RGB 到 SK6812 驱动网络 | `input=RGB / GPIO25`；`pullup=R7 4.7KΩ to +3.3V`；`base_resistor=R8 1KΩ`；`transistor=Q1 SS8550 Y2`；`output=SK6812`；`return=GND` |
| 音频 | SPM1423HM4H-B 数字麦克风 | `part=U2 SPM1423HM4H-B`；`supply=pin6 +3.3V`；`ground=pins1,3 GND`；`select=pin2 SELECT -> GND`；`data=pin5 DAT -> GPIO34 / J4 pin26`；`clock=pin4 CLK -> GPIO0 / J4 pin24`；`decoupling=C1 10uF; C2 100nF` |
| 总线 | 数字麦克风时钟与数据总线 | `controller=external Core2`；`clock_direction=GPIO0/J4 pin24 -> U2 CLK pin4`；`data_direction=U2 DAT pin5 -> GPIO34/J4 pin26`；`word_select_shown=false`；`select_pin=U2 SELECT tied GND` |
| 传感器 | MPU-6886 I2C 连接 | `device=U1 MPU-6886`；`scl=pin23 I2C_SCL`；`sda=pin24 I2C_SDA`；`cs=pin22 +3.3V`；`address_select=pin9 AD0/SDO -> R5 4.7KΩ -> GND; R4 to +3.3V is NC`；`supply=VDD pin13 and VDDIO pin8 -> +3.3V`；`decoupling=C3 10uF; C4/C5 100nF` |
| 总线 | MPU-6886 与 Pogo 共用 I2C | `controller=external Core2`；`sda=GPIO21 / J4 pin17 / U1 pin24 / J3 pin3`；`scl=GPIO22 / J4 pin18 / U1 pin23 / J3 pin4`；`pullups=R2/R3 4.7KΩ to +3.3V`；`onboard_device=U1 MPU-6886`；`external_extension=J3 Pogo` |
| 总线地址 | MPU-6886 I2C 地址 | `device=U1 MPU-6886`；`address_pin=AD0/SDO pin9 low via R5 4.7KΩ`；`seven_bit_address=null`；`address_text_shown=false` |
| GPIO 与控制信号 | MPU-6886 中断和同步信号 | `interrupt=pin12 INT NC`；`regout=pin10 REGOUT NC`；`fsync=pin11 FSYNC NC` |
| 接口 | J1 UART 四针接口 | `pin1=U2_RXD -> GPIO13 / J4 pin15`；`pin2=U2_TXD -> GPIO14 / J4 pin16`；`pin3=+5V`；`pin4=GND`；`rx_direction=socket to host`；`tx_direction=host to socket` |
| 接口 | J2 GPIO 四针接口 | `pin1=GPIO36 / J4 pin4`；`pin2=GPIO26 / J4 pin10`；`pin3=+5V`；`pin4=GND`；`gpio36_function_label=null`；`gpio26_function_label=null` |
| 接口 | J3 Pogo 电源与 I2C 接口 | `pin1=GND`；`pin2=VIN / symbol +5V -> U3 VCC`；`pin3=I2C_SDA / GPIO21`；`pin4=I2C_SCL / GPIO22`；`power_direction=external VIN into charger`；`bus_direction=bidirectional I2C` |
| 电源 | TP4057 充电路径 | `input=J3 pin2 VIN -> U3 pin4 VCC`；`charger=U3 TP4057`；`battery_net=U3 pin3 BAT -> BAT+`；`program_resistor=R9 2KΩ to GND`；`input_capacitor=C6 10uF`；`battery_capacitor=C7 10uF` |
| 电源 | TP4057 充电状态指示 | `indicator=D1 1615RG`；`series_resistor=R6 1KΩ from VIN`；`charge_output=U3 pin1 CHRG`；`standby_output=U3 pin5 STDBY` |
| 电源 | BAT+ 到 M5_BUS | `charger_output=U3 pin3 BAT`；`net=BAT+`；`host_bus=J4 pin30 BATTERY`；`cell_symbol_shown=false`；`battery_connector_shown=false`；`protection_ic_shown=false` |
| 电源 | 电池容量与充电电流 | `documented_capacity=500mAh`；`cell_part_number=null`；`cell_capacity_shown=false`；`charger=U3 TP4057`；`program_resistor=R9 2KΩ`；`charge_current_shown=null`；`temperature_monitor_shown=false` |
| 关键网络 | 主要电源网络 | `five_volt=J4 pin28 -> LED1-LED10, J1 pin3, J2 pin3`；`three_volt=J4 pin12 -> U1, U2, R2/R3/R7`；`charger_input=J3 pin2 VIN`；`battery=U3 BAT -> BAT+ -> J4 pin30` |
| 系统结构 | 本页未集成的系统功能 | `general_mcu_shown=false`；`coprocessor_shown=false`；`storage_shown=false`；`crystal_shown=false`；`rf_shown=false`；`debug_connector_shown=false`；`external_host=M5 host via J4` |

## 待确认事项

- `address.mpu6886-address`：原理图确认 U1 AD0/SDO 默认下拉到 GND，但页面没有直接标注其 7-bit I2C 地址数值。（证据：图 476163941d62 / 第 1 页 / 网格 B2-C2：U1 AD0/SDO 与 R4 NC/R5 4.7KΩ，页面无 0x 地址标注）
- `power.battery-capacity-and-charge-current`：产品正文写内置 500mAh 锂电池，原理图只显示 BAT+ 网络和 TP4057/R9 2KΩ，未显示电芯型号、容量标注、保护板、充电电流数值或温度监测。（证据：图 476163941d62 / 第 1 页 / 网格 C1-D4：U3 TP4057、BAT+、R9 与 J4 BATTERY，页面无电芯/容量/电流标注）
- `review.mpu6886-i2c-address`：A014-C 当前 MPU-6886 在 AD0/SDO 下拉配置下的正式 7-bit I2C 地址是多少？；原因：当前原理图只显示地址选择脚电平，没有直接标注地址数值；需由对应 MPU-6886 datasheet 或已确认软件定义闭环。
- `review.battery-and-charge-spec`：内置电芯的完整型号、额定容量、保护板规格，以及 R9=2KΩ 对应的正式充电电流和热设计边界是什么？；原因：产品正文只有 500mAh，原理图没有电芯、保护和电流数值，不能从阻值经验推导充电规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `476163941d62ad77661f0c12867ffe3776c42839f60f5f11ceeba94bc1d3d854` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1007/A014-C_Sch_M5GO2_page_01.png` |

---

源文档：`zh_CN/base/m5go_bottom2.md`

源文档 SHA-256：`05b10228f9da949348e5213be639e31fb240a08bb93aacc3ad4efaa071e8a72f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
