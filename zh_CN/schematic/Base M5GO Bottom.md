# Base M5GO Bottom 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base M5GO Bottom |
| SKU | A014 |
| 产品 ID | `base-m5go-bottom-94b45fc18195` |
| 源文档 | `zh_CN/base/m5go_bottom.md` |

## 概述

Base M5GO Bottom 通过 J4 M5Stack_BUS 与 Core 主机连接，板上包含 10 颗串联 SK6812 RGB LED、U1 SPQ2410 麦克风与 U2 MAX4466 模拟放大器，以及由 Q1 AO3400A_N 驱动的红外 LED。U3 TP4057 从 J3 pogo 接口的 VIN 为 BAT+ 充电，BAT+ 回到 M5Bus；J1/J2 另行引出 UART 和 GPIO36/GPIO26，并均提供 +5V。I2C_SDA/I2C_SCL 从 M5Bus GPIO21/GPIO22 接到 J3，使用 R3/R4 4.7KΩ 上拉到 +3.3V。

## 检索关键词

`Base M5GO Bottom`、`A014`、`M5Stack_BUS`、`SK6812`、`RGB LED`、`GPIO15`、`SPQ2410`、`MAX4466`、`GPIO34`、`E3.3V`、`AGND`、`TP4057`、`BAT+`、`VIN`、`CHRG`、`STDBY`、`IR12-21C`、`AO3400A_N`、`IR_S`、`GPIO13`、`UART_RXD`、`UART_TXD`、`GPIO16`、`GPIO17`、`GPIO36`、`GPIO26`、`I2C_SDA`、`I2C_SCL`、`GPIO21`、`GPIO22`、`SOCKET_POWER_4P`、`UART_Socket_4P`、`GPIO_Socket_4P`、`+5V`、`+3.3V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED10 | SK6812 | 十颗串行 RGB LED，数据从 LED1 DIN 依次级联到 LED10 | 图 257641dd1a48 / 第 1 页 / 第 1 页 A 区 LED1-LED10 SK6812，VSS/GND、VDD/+5V 与 DOUT-DIN 级联 |
| R1 | 4.7KΩ | SK6812 数据输入网络到 +5V 的上拉电阻 | 图 257641dd1a48 / 第 1 页 / 第 1 页 A1 区 LED1 DIN/SK6812 网络下方 R1 4.7KΩ 到 +5V |
| U1 | SPQ2410 | 3.3V 供电的模拟麦克风，输出经 C6 耦合到 MAX4466 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B1 区 U1 SPQ2410，Vdd/OUT/GND 与 E3.3V、AGND、C6 |
| U2 | MAX4466 | 将 SPQ2410 信号放大后输出到 GPIO34 的运算放大器 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B2 区 U2 max4466，IN+/IN-/OUT/VCC/GND 与 GPIO34 |
| R2,R5,C6 | 1MΩ / 1MΩ / 10nF | 麦克风交流耦合和 E3.3V/AGND 中点偏置网络 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B1-B2 区 U1 OUT-C6 10nF 节点，R2 1MΩ 到 E3.3V、R5 1MΩ 到 AGND |
| R7,C8,R9,C10 | 100KΩ / 100pF / 1KΩ / 10uF | MAX4466 反相输入反馈与低频增益设定网络 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B2-C2 区 U2 OUT/IN- 周围 R7 100KΩ、C8 100pF、R9 1KΩ、C10 10uF |
| R6,R8 | 0Ω | 分别桥接 +3.3V 到 E3.3V、GND 到 AGND 的麦克风电源域连接器件 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B3 区 R6 0Ω 位于 E3.3V/+3.3V，R8 0Ω 位于 AGND/GND |
| C1-C5,C7 | 10uF / 1.0uF / 100nF / 10nF / 1nF / 10uF | MAX4466 E3.3V/AGND 电源域的宽频去耦电容组 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B2-B3 区 C1-C5 从 E3.3V 接 AGND，C7 从 +3.3V 接 GND |
| U3 | TP4057 | 从 VIN 为 BAT+ 单节电池网络充电，并提供 CHRG/STDBY 状态输出 | 图 257641dd1a48 / 第 1 页 / 第 1 页 D1-D2 区 U3 TP4057，VCC/VIN、BAT/BAT+、PROG、CHRG、STDBY、GND |
| D1,R11 | 1615RG / 1KΩ | 由 TP4057 CHRG 与 STDBY 驱动的双色充电状态指示灯和公共限流电阻 | 图 257641dd1a48 / 第 1 页 / 第 1 页 D1 区 D1 1615RG 两路接 U3 CHRG/STDBY，公共端经 R11 1KΩ 接 VIN |
| R12,C11,C12 | 2KΩ / 10uF / 10uF | TP4057 充电编程电阻和 VIN/BAT+ 输入输出旁路 | 图 257641dd1a48 / 第 1 页 / 第 1 页 C1-D2 区 U3 PROG-R12 2KΩ，VIN-C11 10uF，BAT+-C12 10uF |
| LED11 | IR12-21C | 由 +5V 供电并经 Q1 低端开关驱动的红外发射 LED | 图 257641dd1a48 / 第 1 页 / 第 1 页 C3-D3 区 LED11 IR12-21C，+5V 到 R10/Q1 路径 |
| Q1 | AO3400A_N | 受 IR_S 控制的 N 沟道 MOSFET，作为红外 LED 低端开关 | 图 257641dd1a48 / 第 1 页 / 第 1 页 D3 区 Q1 AO3400A_N，漏极接 R10/LED11，源极接 GND，栅极接 IR_S |
| R10,R13,R14 | 49.9Ω / 1KΩ / 10KΩ | 红外 LED 限流、MOSFET 栅极串联和栅极下拉网络 | 图 257641dd1a48 / 第 1 页 / 第 1 页 C3-D3 区 LED11-R10 49.9Ω-Q1 与 IR_S-R13 1KΩ、R14 10KΩ-GND |
| J1 | UART_Socket_4P | 引出 U2_RXD、U2_TXD、+5V 与 GND 的四针 UART 接口 | 图 257641dd1a48 / 第 1 页 / 第 1 页 A4 区 J1 UART_Socket_4P，pin1 U2_RXD、pin2 U2_TXD、pin3 +5V、pin4 GND |
| J2 | GPIO_Socket_4P | 引出 GPIO36、GPIO26、+5V 与 GND 的四针 GPIO 接口 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B4 区 J2 GPIO_Socket_4P，pin1 GPIO36、pin2 GPIO26、pin3 +5V、pin4 GND |
| J3 | SOCKET_POWER_4P | pogo 电源/I2C 接口，连接 GND、VIN、I2C_SDA 与 I2C_SCL | 图 257641dd1a48 / 第 1 页 / 第 1 页 B4 区 J3 SOCKET_POWER_4P，pin1 GND、pin2 +5V 标识/外部网 VIN、pin3 SDA、pin4 SCL |
| R3,R4 | 4.7KΩ | I2C_SDA 与 I2C_SCL 到 +3.3V 的上拉电阻 | 图 257641dd1a48 / 第 1 页 / 第 1 页 B3-B4 区 R3 4.7KΩ 从 I2C_SDA 到 +3.3V，R4 4.7KΩ 从 I2C_SCL 到 +3.3V |
| J4 | M5Stack_BUS | 30 针主机总线，承载 UART、I2C、RGB、红外、麦克风、电源和未使用 GPIO | 图 257641dd1a48 / 第 1 页 / 第 1 页 C4-D4 区 J4 M5Stack_BUS，1-30 脚及网络标注 |
| C9 | 1.0uF | J4 EN 网络到 GND 的电容 | 图 257641dd1a48 / 第 1 页 / 第 1 页 C4 区 J4 pin6 EN 向上经 C9 1.0uF 接 GND |

## 系统结构

### Base M5GO Bottom 系统架构

J4 M5Stack_BUS 将 Core 主机的 GPIO 与 RGB、麦克风、红外、UART、GPIO 和 I2C/充电接口相连；板上没有独立主控，功能由 J4 上的主机 GPIO 驱动。

- 参数与网络：`host_connector=J4 M5Stack_BUS`；`rgb=LED1-LED10 SK6812`；`microphone=U1 SPQ2410 + U2 MAX4466`；`charger=U3 TP4057`；`infrared=LED11 IR12-21C + Q1 AO3400A_N`；`onboard_mcu_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页完整单页四个功能分区与 J4，未见主控 MCU

## 核心器件

### 红外 LED 低端驱动

+5V 依次经过 LED11 IR12-21C 与 R10 49.9Ω 到 Q1 AO3400A_N 漏极，Q1 源极接 GND，构成由 IR_S 控制的低端开关。

- 参数与网络：`power_path=+5V -> LED11 IR12-21C -> R10 49.9Ω -> Q1 drain`；`switch=Q1 AO3400A_N`；`source=GND`；`control=IR_S`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 C3-D3 区 +5V、LED11、R10、Q1 与 GND

## 电源

### SK6812 灯链供电

LED1-LED10 的 VDD pin4 均接 +5V，VSS pin2 均接 GND。

- 参数与网络：`supply=+5V`；`ground=GND`；`vdd_pin=4`；`vss_pin=2`；`devices=LED1-LED10`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 A 区十颗 SK6812 的 pin4 +5V 与 pin2 GND

### 麦克风模拟电源域

+3.3V 经 R6 0Ω 形成 E3.3V，GND 经 R8 0Ω 形成 AGND；C1-C5 从 E3.3V 到 AGND 提供 10uF、1.0uF、100nF、10nF、1nF 多级去耦。

- 参数与网络：`supply_bridge=R6 0Ω: +3.3V to E3.3V`；`ground_bridge=R8 0Ω: GND to AGND`；`decoupling=C1 10uF, C2 1.0uF, C3 100nF, C4 10nF, C5 1nF`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B2-B3 区 R6/R8 与 C1-C5

### TP4057 充电路径

J3 pin2 的外部网络 VIN 连接 U3 TP4057 VCC pin4，U3 BAT pin3 输出 BAT+；BAT+ 连接 J4 pin30 BATTERY，C11/C12 各 10uF 分别旁路 VIN 与 BAT+。

- 参数与网络：`input_connector=J3 pin2`；`input_net=VIN`；`charger=U3 TP4057`；`battery_net=BAT+`；`host_battery_pin=J4 pin30 BATTERY`；`input_capacitor=C11 10uF`；`battery_capacitor=C12 10uF`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B4 J3 VIN、C1-D2 U3/C11/C12/BAT+、D4 J4 pin30 BATTERY

### TP4057 充电编程

U3 TP4057 PROG pin6 通过 R12 2KΩ 接 GND；原理图仅给出该电阻，不直接标注充电电流数值。

- 参数与网络：`program_pin=U3 pin6 PROG`；`program_resistor=R12 2KΩ to GND`；`charge_current_label_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 D2 区 U3 PROG pin6-R12 2KΩ-GND

## 接口

### J1 UART 接口

J1 UART_Socket_4P pin1=U2_RXD、pin2=U2_TXD、pin3=VCC/+5V、pin4=GND；U2_RXD 来自 J4 pin15 GPIO16，U2_TXD 来自 J4 pin16 GPIO17。

- 参数与网络：`pin1=U2_RXD / J4 pin15 GPIO16`；`pin2=U2_TXD / J4 pin16 GPIO17`；`pin3=+5V`；`pin4=GND`；`rx_direction=socket RX toward host GPIO16`；`tx_direction=host GPIO17 toward socket TX`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 A4 J1 UART_Socket_4P 与 C4 J4 pin15/pin16 U2_RXD/U2_TXD

### J2 GPIO 接口

J2 GPIO_Socket_4P pin1=GPIO36、pin2=GPIO26、pin3=VCC/+5V、pin4=GND；GPIO36 与 GPIO26 分别连接 J4 pin4 和 pin10。

- 参数与网络：`pin1=GPIO36 / J4 pin4`；`pin2=GPIO26 / J4 pin10`；`pin3=+5V`；`pin4=GND`；`gpio36_direction=host GPIO input capability not specified on schematic`；`gpio26_direction=bidirectional GPIO net`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B4 J2 GPIO_Socket_4P 与 C4 J4 pin4 GPIO36/pin10 GPIO26

### J3 pogo 电源与 I2C 接口

J3 SOCKET_POWER_4P pin1=GND、pin2 的连接器标识为 +5V 且板内网络名为 VIN、pin3=SDA/I2C_SDA、pin4=SCL/I2C_SCL。

- 参数与网络：`pin1=GND`；`pin2=+5V contact / VIN net`；`pin3=SDA / I2C_SDA`；`pin4=SCL / I2C_SCL`；`power_destination=U3 TP4057 VCC`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B4 J3 SOCKET_POWER_4P 的引脚字段和左侧 GND/VIN/I2C_SDA/I2C_SCL 网络

### J4 M5Stack_BUS 已用引脚

J4 已用功能网络为 pin4 GPIO36、pin10 GPIO26、pin15 GPIO16/U2_RXD、pin16 GPIO17/U2_TXD、pin17 GPIO21/I2C_SDA、pin18 GPIO22/I2C_SCL、pin22 GPIO13/IR_S、pin23 GPIO15/SK6812、pin26 GPIO34、pin28 +5V、pin30 BATTERY/BAT+；pin1/3/5 为 GND，pin6 为 EN，pin12 为 +3.3V。

- 参数与网络：`uart=pin15 GPIO16 RXD; pin16 GPIO17 TXD`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`rgb=pin23 GPIO15`；`infrared=pin22 GPIO13`；`microphone=pin26 GPIO34`；`gpio_socket=pin4 GPIO36; pin10 GPIO26`；`power=pin1/3/5 GND; pin12 +3.3V; pin28 +5V; pin30 BATTERY/BAT+`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 C4-D4 J4 M5Stack_BUS 1-30 脚与外侧功能网络

## 总线

### 十颗 SK6812 串行灯链

LED1 DOUT 依次连接 LED2 DIN，随后逐颗级联到 LED10 DIN；LED10 DOUT 在本页标记未连接。

- 参数与网络：`devices=LED1-LED10`；`part_number=SK6812`；`count=10`；`data_order=LED1 -> LED2 -> LED3 -> LED4 -> LED5 -> LED6 -> LED7 -> LED8 -> LED9 -> LED10`；`last_dout_connected=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 A1-A4 区 LED1-LED10 DOUT/DIN 蓝色级联线，LED10 DOUT 端有未连接标记

### 主机 UART 路由

J4 GPIO16/pin15 通过 U2_RXD 接 J1 pin1，J4 GPIO17/pin16 通过 U2_TXD 接 J1 pin2；接口电源为 +5V，逻辑信号电平未在原理图标注。

- 参数与网络：`receive=J1 pin1 U2_RXD <-> J4 pin15 GPIO16`；`transmit=J1 pin2 U2_TXD <-> J4 pin16 GPIO17`；`connector_supply=+5V`；`logic_voltage_label_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 J1 U2_RXD/U2_TXD 与 J4 pin15/pin16 同名网络

### pogo I2C 路由

J4 pin17 GPIO21 通过 I2C_SDA 接 J3 pin3，J4 pin18 GPIO22 通过 I2C_SCL 接 J3 pin4；R3/R4 各 4.7KΩ 将 SDA/SCL 上拉到 +3.3V，页面未显示板载 I2C 地址。

- 参数与网络：`controller=M5Stack host`；`sda=J4 pin17 GPIO21 -> I2C_SDA -> J3 pin3`；`scl=J4 pin18 GPIO22 -> I2C_SCL -> J3 pin4`；`pullups=R3/R4 4.7KΩ to +3.3V`；`address_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B3-B4 R3/R4/J3 与 C4 J4 pin17/pin18 I2C_SDA/I2C_SCL

## GPIO 与控制信号

### SK6812 数据输入映射

J4 pin23 的 GPIO15 连接 SK6812 网络并进入 LED1 DIN pin3，R1 4.7KΩ 将该输入网络上拉到 +5V。

- 参数与网络：`host=J4 pin23 GPIO15`；`net=SK6812`；`destination=LED1 DIN pin3`；`pullup=R1 4.7KΩ to +5V`；`direction=host output to LED chain`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 A1 LED1 DIN/SK6812/R1 与 C4 区 J4 pin23 SK6812/GPIO15

### 麦克风模拟输出映射

U2 MAX4466 OUT pin4 的 GPIO34 网络连接 J4 M5Stack_BUS pin26。

- 参数与网络：`source=U2 pin4 OUT`；`net=GPIO34`；`host_connector=J4 pin26`；`direction=analog output to host input`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B2 U2 OUT GPIO34 与 D4 J4 pin26 GPIO34

### 充电状态 LED

U3 CHRG pin1 与 STDBY pin5 分别连接 D1 1615RG 的两路发光单元，D1 公共端经 R11 1KΩ 接 VIN。

- 参数与网络：`charge_output=U3 pin1 CHRG`；`standby_output=U3 pin5 STDBY`；`indicator=D1 1615RG`；`common_resistor=R11 1KΩ to VIN`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 D1 区 U3 CHRG/STDBY、D1 1615RG、R11/VIN

### 红外发射控制映射

J4 pin22 的 GPIO13 连接 IR_S，IR_S 经 R13 1KΩ 驱动 Q1 栅极，并由 R14 10KΩ 下拉到 GND。

- 参数与网络：`host=J4 pin22 GPIO13`；`net=IR_S`；`gate_resistor=R13 1KΩ`；`gate_pulldown=R14 10KΩ`；`destination=Q1 gate`；`direction=host output`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 D3 IR_S/R13/R14/Q1 与 C4-D4 J4 pin22 IR_S/GPIO13

## 时钟

### 板载时钟

当前完整单页原理图未画出晶振、振荡器或独立时钟输入。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页完整单页所有功能分区，未见 Y/X 晶振位号或 CLK 网络

## 复位

### M5Bus EN 电容

J4 pin6 EN 通过 C9 1.0uF 接 GND；本页未显示 EN 的其他驱动或复位开关。

- 参数与网络：`host_pin=J4 pin6 EN`；`capacitor=C9 1.0uF to GND`；`other_driver_shown=false`；`reset_switch_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 C4 区 J4 pin6 EN 向上到 C9 1.0uF/GND

## 关键网络

### 板上电源网络分配

J4 pin28 提供 +5V 给 SK6812、红外 LED、J1 和 J2；J4 pin12 提供 +3.3V 并经 R6 形成 E3.3V；J3 的 VIN 进入 U3 充电器，U3 的 BAT+ 回到 J4 pin30。

- 参数与网络：`five_volt_consumers=LED1-LED10, LED11, J1 pin3, J2 pin3`；`three_volt_source=J4 pin12 +3.3V`；`analog_rail=E3.3V via R6 0Ω`；`charge_input=J3 pin2 VIN`；`battery_return=U3 BAT+ -> J4 pin30`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页各 +5V/+3.3V/E3.3V/VIN/BAT+ 网络与 J4 pin12/pin28/pin30

## 存储

### 板载存储

当前完整单页原理图未画出 Flash、PSRAM、EEPROM 或存储卡接口。

- 参数与网络：`flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页完整器件页，U1-U3 为麦克风、放大器和充电器，未见存储器件

## 音频

### SPQ2410 麦克风前端

U1 SPQ2410 Vdd pin1 接 E3.3V，GND pin2/pin3 接 AGND，OUT pin4 经 C6 10nF 交流耦合到由 R2/R5 各 1MΩ 形成的中点偏置，再进入 U2 MAX4466 IN+ pin1。

- 参数与网络：`microphone=U1 SPQ2410`；`supply=E3.3V`；`ground=AGND`；`output=U1 pin4 OUT`；`coupling=C6 10nF`；`bias=R2 1MΩ to E3.3V; R5 1MΩ to AGND`；`amplifier_input=U2 pin1 IN+`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B1-B2 区 U1、C6、R2/R5 与 U2 IN+

## 调试与烧录

### 专用调试接口

当前完整单页原理图未画出 JTAG、SWD、USB-UART 或专用编程调试连接器。

- 参数与网络：`jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`dedicated_debug_connector_shown=false`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页完整连接器 J1-J4，仅为 UART/GPIO/I2C/主机总线，无调试标注

## 模拟电路

### MAX4466 放大与反馈

U2 MAX4466 VCC pin5 接 E3.3V、GND pin2 接 AGND，OUT pin4 输出 GPIO34；OUT 到 IN- pin3 的反馈为 R7 100KΩ 与 C8 100pF 并联，IN- 再经 R9 1KΩ、C10 10uF 串联到 AGND。

- 参数与网络：`amplifier=U2 MAX4466`；`supply=E3.3V/AGND`；`output=U2 pin4 GPIO34`；`feedback=R7 100KΩ parallel C8 100pF`；`gain_leg=R9 1KΩ series C10 10uF to AGND`
- 证据：图 257641dd1a48 / 第 1 页 / 第 1 页 B2-C2 区 U2 OUT/IN- 与 R7/C8/R9/C10

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base M5GO Bottom 系统架构 | `host_connector=J4 M5Stack_BUS`；`rgb=LED1-LED10 SK6812`；`microphone=U1 SPQ2410 + U2 MAX4466`；`charger=U3 TP4057`；`infrared=LED11 IR12-21C + Q1 AO3400A_N`；`onboard_mcu_shown=false` |
| GPIO 与控制信号 | SK6812 数据输入映射 | `host=J4 pin23 GPIO15`；`net=SK6812`；`destination=LED1 DIN pin3`；`pullup=R1 4.7KΩ to +5V`；`direction=host output to LED chain` |
| 总线 | 十颗 SK6812 串行灯链 | `devices=LED1-LED10`；`part_number=SK6812`；`count=10`；`data_order=LED1 -> LED2 -> LED3 -> LED4 -> LED5 -> LED6 -> LED7 -> LED8 -> LED9 -> LED10`；`last_dout_connected=false` |
| 电源 | SK6812 灯链供电 | `supply=+5V`；`ground=GND`；`vdd_pin=4`；`vss_pin=2`；`devices=LED1-LED10` |
| 音频 | SPQ2410 麦克风前端 | `microphone=U1 SPQ2410`；`supply=E3.3V`；`ground=AGND`；`output=U1 pin4 OUT`；`coupling=C6 10nF`；`bias=R2 1MΩ to E3.3V; R5 1MΩ to AGND`；`amplifier_input=U2 pin1 IN+` |
| 模拟电路 | MAX4466 放大与反馈 | `amplifier=U2 MAX4466`；`supply=E3.3V/AGND`；`output=U2 pin4 GPIO34`；`feedback=R7 100KΩ parallel C8 100pF`；`gain_leg=R9 1KΩ series C10 10uF to AGND` |
| GPIO 与控制信号 | 麦克风模拟输出映射 | `source=U2 pin4 OUT`；`net=GPIO34`；`host_connector=J4 pin26`；`direction=analog output to host input` |
| 电源 | 麦克风模拟电源域 | `supply_bridge=R6 0Ω: +3.3V to E3.3V`；`ground_bridge=R8 0Ω: GND to AGND`；`decoupling=C1 10uF, C2 1.0uF, C3 100nF, C4 10nF, C5 1nF` |
| 电源 | TP4057 充电路径 | `input_connector=J3 pin2`；`input_net=VIN`；`charger=U3 TP4057`；`battery_net=BAT+`；`host_battery_pin=J4 pin30 BATTERY`；`input_capacitor=C11 10uF`；`battery_capacitor=C12 10uF` |
| 电源 | TP4057 充电编程 | `program_pin=U3 pin6 PROG`；`program_resistor=R12 2KΩ to GND`；`charge_current_label_shown=false` |
| GPIO 与控制信号 | 充电状态 LED | `charge_output=U3 pin1 CHRG`；`standby_output=U3 pin5 STDBY`；`indicator=D1 1615RG`；`common_resistor=R11 1KΩ to VIN` |
| 其他事实 | 电池容量 | `documented_capacity=500mAh`；`schematic_battery_net=BAT+`；`battery_reference_shown=false`；`capacity_shown_on_schematic=false` |
| GPIO 与控制信号 | 红外发射控制映射 | `host=J4 pin22 GPIO13`；`net=IR_S`；`gate_resistor=R13 1KΩ`；`gate_pulldown=R14 10KΩ`；`destination=Q1 gate`；`direction=host output` |
| 核心器件 | 红外 LED 低端驱动 | `power_path=+5V -> LED11 IR12-21C -> R10 49.9Ω -> Q1 drain`；`switch=Q1 AO3400A_N`；`source=GND`；`control=IR_S` |
| 接口 | J1 UART 接口 | `pin1=U2_RXD / J4 pin15 GPIO16`；`pin2=U2_TXD / J4 pin16 GPIO17`；`pin3=+5V`；`pin4=GND`；`rx_direction=socket RX toward host GPIO16`；`tx_direction=host GPIO17 toward socket TX` |
| 总线 | 主机 UART 路由 | `receive=J1 pin1 U2_RXD <-> J4 pin15 GPIO16`；`transmit=J1 pin2 U2_TXD <-> J4 pin16 GPIO17`；`connector_supply=+5V`；`logic_voltage_label_shown=false` |
| 接口 | J2 GPIO 接口 | `pin1=GPIO36 / J4 pin4`；`pin2=GPIO26 / J4 pin10`；`pin3=+5V`；`pin4=GND`；`gpio36_direction=host GPIO input capability not specified on schematic`；`gpio26_direction=bidirectional GPIO net` |
| 接口 | J3 pogo 电源与 I2C 接口 | `pin1=GND`；`pin2=+5V contact / VIN net`；`pin3=SDA / I2C_SDA`；`pin4=SCL / I2C_SCL`；`power_destination=U3 TP4057 VCC` |
| 总线 | pogo I2C 路由 | `controller=M5Stack host`；`sda=J4 pin17 GPIO21 -> I2C_SDA -> J3 pin3`；`scl=J4 pin18 GPIO22 -> I2C_SCL -> J3 pin4`；`pullups=R3/R4 4.7KΩ to +3.3V`；`address_shown=false` |
| 接口 | J4 M5Stack_BUS 已用引脚 | `uart=pin15 GPIO16 RXD; pin16 GPIO17 TXD`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`rgb=pin23 GPIO15`；`infrared=pin22 GPIO13`；`microphone=pin26 GPIO34`；`gpio_socket=pin4 GPIO36; pin10 GPIO26`；`power=pin1/3/5 GND; pin12 +3.3V; pin28 +5V; pin30 BATTERY/BAT+` |
| 复位 | M5Bus EN 电容 | `host_pin=J4 pin6 EN`；`capacitor=C9 1.0uF to GND`；`other_driver_shown=false`；`reset_switch_shown=false` |
| 关键网络 | 板上电源网络分配 | `five_volt_consumers=LED1-LED10, LED11, J1 pin3, J2 pin3`；`three_volt_source=J4 pin12 +3.3V`；`analog_rail=E3.3V via R6 0Ω`；`charge_input=J3 pin2 VIN`；`battery_return=U3 BAT+ -> J4 pin30` |
| 存储 | 板载存储 | `flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false` |
| 时钟 | 板载时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 调试与烧录 | 专用调试接口 | `jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`dedicated_debug_connector_shown=false` |

## 待确认事项

- `other.documented-battery-capacity`：产品正文标注内置电池为 500mAh，但当前原理图只显示 BAT+ 网络和 TP4057 充电电路，没有电池位号、型号或容量标注。（证据：图 257641dd1a48 / 第 1 页 / 第 1 页 Power 区 U3 TP4057/BAT+ 与 J4 pin30，完整页面未见电池器件或容量）
- `review.battery-capacity`：A014 当前硬件所装电池的料号、额定容量和保护板规格是否确认为 500mAh？；原因：500mAh 来自产品正文，当前原理图只显示 BAT+ 和 TP4057，无法从图中验证电池容量与保护配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `257641dd1a48c91b73085574de27e2e06ebfcde06599fa0ed865fe3c733da01e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1006/A014_Sch_M5GO_page_01.png` |

---

源文档：`zh_CN/base/m5go_bottom.md`

源文档 SHA-256：`dca69ab37bf0518ed635a12212b477e64e496e6bfd528cc2b44356769d34b788`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
