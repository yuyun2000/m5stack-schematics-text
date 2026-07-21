# Base M5GO Bottom3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base M5GO Bottom3 |
| SKU | A014-D |
| 产品 ID | `base-m5go-bottom3-e6363d570f6f` |
| 源文档 | `zh_CN/module/M5GO3 Bottom.md` |

## 概述

Base M5GO Bottom3 通过 J4 M5Stack_BUS 引出电源和 GPIO，并提供 J1 UART、J2 GPIO 与 J3 I2C/电源三组 4 针接口。LED1-LED10 为 10 颗串联的 WS2812C，由 GPIO5/RGB 驱动；GPIO7 通过 Q1 SI2302 驱动 +5 V 红外发射支路。U1 TP4057 从 VIN 为 BAT+ 充电，BAT+ 同时连接 J5 电池座和 M5-Bus BATTERY pin30，J3 I2C 总线配置 4.7 kΩ 上拉到 3.3 V。

## 检索关键词

`Base M5GO Bottom3`、`A014-D`、`M5GO3`、`TP4057`、`WS2812C`、`LED1`、`LED10`、`RGB`、`GPIO5`、`IR1`、`SI2302`、`GPIO7`、`49.9Ω`、`BAT+`、`VIN`、`CHRG`、`STDBY`、`RPROG`、`R6 2KΩ`、`M5Stack_BUS_S3`、`UART_Socket_4P`、`GPIO_Socket_4P`、`SOCKET_POWER_4P`、`GPIO18`、`GPIO17`、`GPIO8`、`GPIO9`、`I2C_SDA`、`I2C_SCL`、`GPIO12`、`GPIO11`、`4.7KΩ`、`+3.3V`、`+5V`、`500mAh`、`pogo pin`、`CoreS3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TP4057 | 单节电池充电控制器，连接 VIN、BAT+、CHRG、STDBY 与 PROG | 图 9a19e47f4e25 / 第 1 页 / C1-D2 Power 分区 U1 TP4057 pins1-6 |
| LED1-LED10 | WS2812C | 十颗 3.3 V 可编程 RGB LED，使用 DI/DO 级联数据链 | 图 9a19e47f4e25 / 第 1 页 / A1-B3 RGB LED * 10 分区 LED1-LED10 |
| C3-C12 | 100nF | 分别对应十颗 WS2812C 的 3.3 V 对地去耦电容 | 图 9a19e47f4e25 / 第 1 页 / A1-A3 +3.3V 上方 C3-C12 100nF |
| IR1/Q1 | IR LED / SI2302 | +5 V 红外发射 LED 与 GPIO7 控制的 N 沟道 MOSFET 低侧驱动 | 图 9a19e47f4e25 / 第 1 页 / C2-D3 IR 分区 IR1/R4/Q1/R5/R7 |
| D1 | 1615RG | 连接 TP4057 CHRG/STDBY 的双色充电状态指示灯 | 图 9a19e47f4e25 / 第 1 页 / C1-D1 D1 1615RG、R3、CHRG/STDBY |
| J5 | Header 2 | BAT+ 与 GND 两针电池连接器 | 图 9a19e47f4e25 / 第 1 页 / D2 J5 Header 2 pins1/2 |
| J1 | UART_Socket_4P | GPIO18/UART_RXD、GPIO17/UART_TXD、+5 V 与 GND 的四针接口 | 图 9a19e47f4e25 / 第 1 页 / A4 Socket 分区 J1 UART_Socket_4P |
| J2 | GPIO_Socket_4P | GPIO8、GPIO9、+5 V 与 GND 的四针接口 | 图 9a19e47f4e25 / 第 1 页 / A4-B4 Socket 分区 J2 GPIO_Socket_4P |
| J3 | SOCKET_POWER_4P | GND、VIN/+5 V、I2C_SDA 与 I2C_SCL 的四针电源/I2C 接口 | 图 9a19e47f4e25 / 第 1 页 / B4 Socket 分区 J3 SOCKET_POWER_4P |
| J4 | M5Stack_BUS_S3 | 30 针 CoreS3 系列主机接口，承载电源、BAT+、RGB、IR、UART、GPIO 与 I2C | 图 9a19e47f4e25 / 第 1 页 / C4-D4 J4 M5Stack_BUS_S3 pins1-30 |
| R1/R2 | 4.7KΩ | I2C_SDA 与 I2C_SCL 到 +3.3 V 的上拉电阻 | 图 9a19e47f4e25 / 第 1 页 / B3-B4 R1/R2 4.7KΩ、I2C_SDA/I2C_SCL |
| R3/R6/C1/C2 | 1KΩ / 2KΩ / 10uF / 10uF | TP4057 状态灯限流、充电编程及 VIN/BAT+ 去耦网络 | 图 9a19e47f4e25 / 第 1 页 / C1-D2 Power 分区 R3/R6/C1/C2 |

## 系统结构

### Base M5GO Bottom3 系统架构

J4 M5Stack_BUS_S3 将主机 GPIO、电源和电池网络分配到十颗 WS2812C、红外驱动、三组四针接口与 TP4057 电池充电电路；页面未画独立主控、存储器或传感器。

- 参数与网络：`host=J4 M5Stack_BUS_S3`；`rgb=LED1-LED10 WS2812C`；`infrared=IR1/Q1 SI2302`；`charging=U1 TP4057`；`external_ports=J1 UART; J2 GPIO; J3 I2C/power`；`controller=host via J4`；`storage=not shown`；`sensor=not shown`
- 证据：图 9a19e47f4e25 / 第 1 页 / 整页 RGB LED/Socket/Power/IR/M5Bus 五个分区

## 核心器件

### 十颗 WS2812C 级联

RGB 网络进入 LED1 DI，LED1 DO 依次级联到 LED2-LED5，再折返到 LED6-LED10；LED10 DO 在页面末端未连接。

- 参数与网络：`count=10`；`part_number=WS2812C`；`input=RGB -> LED1 DI pin3`；`chain=LED1 DO -> LED2 DI -> LED3 DI -> LED4 DI -> LED5 DI -> LED6 DI -> LED7 DI -> LED8 DI -> LED9 DI -> LED10 DI`；`last_output=LED10 DO pin1 unconnected`
- 证据：图 9a19e47f4e25 / 第 1 页 / A1-B3 LED1-LED10 DI/DO 连线

## 电源

### RGB LED 供电与去耦

LED1-LED10 的 VDD pin4 全部接 +3.3 V、GND pin2 全部接地，每颗 LED 分别配置 C3-C12 中的一颗 100 nF 对地去耦电容。

- 参数与网络：`rail=+3.3V`；`ground=LED1-LED10 pin2`；`vdd=LED1-LED10 pin4`；`decoupling=C3-C12 100nF, one per LED`
- 证据：图 9a19e47f4e25 / 第 1 页 / A1-B3 LED1-LED10 VDD/GND 与 C3-C12

### TP4057 充电路径

VIN 连接 U1 TP4057 VCC pin4 并由 C1 10 uF 对地去耦；U1 BAT pin3 输出 BAT+，由 C2 10 uF 去耦并连接 J5 pin2 与 J4 BATTERY pin30。

- 参数与网络：`input=VIN -> U1 VCC pin4`；`input_cap=C1 10uF`；`charger=U1 TP4057`；`battery_output=U1 BAT pin3 -> BAT+`；`output_cap=C2 10uF`；`battery_connector=J5 pin2 BAT+; J5 pin1 GND`；`host_battery=J4 pin30 BATTERY/BAT+`
- 证据：图 9a19e47f4e25 / 第 1 页 / C1-D2 U1/C1/C2/J5/VIN/BAT+；D4 J4 pin30

### TP4057 PROG 配置

U1 PROG pin6 通过 R6 2 kΩ 接 GND；原理图仅给出编程电阻值，没有在页面标注对应充电电流。

- 参数与网络：`pin=U1 PROG pin6`；`resistor=R6 2KΩ`；`destination=GND`；`charge_current_label=not shown`
- 证据：图 9a19e47f4e25 / 第 1 页 / D1-D2 U1 PROG pin6/R6 2KΩ

## 接口

### 红外发射驱动

+5 V 经 IR1 和 R4 49.9 Ω ±1% 串联后接 Q1 SI2302 漏极，Q1 源极接地；GPIO7 经 R5 1 kΩ 驱动栅极，R7 10 kΩ 将栅极下拉。

- 参数与网络：`supply=+5V`；`emitter=IR1`；`series_resistor=R4 49.9Ω (49R9) ±1%`；`switch=Q1 SI2302`；`gate=GPIO7 via R5 1KΩ`；`gate_pulldown=R7 10KΩ`；`topology=N-MOSFET low-side switch`
- 证据：图 9a19e47f4e25 / 第 1 页 / C2-D3 IR 分区 +5V/IR1/R4/Q1/R5/R7

### 充电状态指示

U1 CHRG pin1 与 STDBY pin5 分别连接 D1 1615RG 的两个发光通道，D1 公共供电路径经 R3 1 kΩ 接 VIN。

- 参数与网络：`indicator=D1 1615RG`；`charging=U1 CHRG pin1`；`standby=U1 STDBY pin5`；`supply=VIN via R3 1KΩ`
- 证据：图 9a19e47f4e25 / 第 1 页 / C1-D1 D1/R3/U1 CHRG/STDBY

### J1 UART 四针接口

J1 UART_Socket_4P pin1 为 GPIO18/UART_RXD、pin2 为 GPIO17/UART_TXD、pin3 为 +5 V/VCC、pin4 为 GND。

- 参数与网络：`connector=J1 UART_Socket_4P`；`pin1=GPIO18 / UART_RXD`；`pin2=GPIO17 / UART_TXD`；`pin3=+5V / VCC`；`pin4=GND`；`host_routes=GPIO18 J4 pin15; GPIO17 J4 pin16`
- 证据：图 9a19e47f4e25 / 第 1 页 / A4 J1 UART_Socket_4P pins1-4；C4 J4 GPIO18/GPIO17

### J2 GPIO 四针接口

J2 GPIO_Socket_4P pin1 为 GPIO8、pin2 为 GPIO9、pin3 为 +5 V/VCC、pin4 为 GND；GPIO8/9 分别来自 J4 pins4/10。

- 参数与网络：`connector=J2 GPIO_Socket_4P`；`pin1=GPIO8`；`pin2=GPIO9`；`pin3=+5V / VCC`；`pin4=GND`；`host_routes=GPIO8 J4 pin4; GPIO9 J4 pin10`
- 证据：图 9a19e47f4e25 / 第 1 页 / A4-B4 J2 GPIO_Socket_4P；C4 J4 GPIO8/GPIO9

### M5Stack_BUS_S3 已用针脚

J4 使用 pins1/3/5 GND、pin4 GPIO8、pin8 GPIO5/RGB、pin10 GPIO9、pin12 +3.3 V、pin15 GPIO18、pin16 GPIO17、pin17 GPIO12/I2C_SDA、pin18 GPIO11/I2C_SCL、pin22 GPIO7、pin28 +5 V 与 pin30 BATTERY/BAT+。

- 参数与网络：`ground=pins1/3/5`；`gpio_socket=pin4 GPIO8; pin10 GPIO9`；`rgb=pin8 GPIO5`；`3v3=pin12`；`uart=pin15 GPIO18; pin16 GPIO17`；`i2c=pin17 GPIO12 SDA; pin18 GPIO11 SCL`；`ir=pin22 GPIO7`；`5v=pin28`；`battery=pin30 BAT+`
- 证据：图 9a19e47f4e25 / 第 1 页 / C4-D4 J4 M5Stack_BUS_S3 pins1-30

## 总线

### J3 I2C/电源接口

J3 SOCKET_POWER_4P pin1 为 GND、pin2 为 VIN（接口内标 +5 V）、pin3 为 SDA/I2C_SDA、pin4 为 SCL/I2C_SCL；SDA/SCL 分别连接 J4 GPIO12/pin17 与 GPIO11/pin18。

- 参数与网络：`connector=J3 SOCKET_POWER_4P`；`pin1=GND`；`pin2=VIN / +5V label`；`pin3=SDA / I2C_SDA`；`pin4=SCL / I2C_SCL`；`sda_host=J4 pin17 GPIO12`；`scl_host=J4 pin18 GPIO11`；`direction=bidirectional data; host clock`
- 证据：图 9a19e47f4e25 / 第 1 页 / B3-B4 J3/I2C_SDA/I2C_SCL；C4 J4 pins17/18

### I2C 上拉

I2C_SDA 与 I2C_SCL 分别通过 R1 与 R2 4.7 kΩ 上拉到 +3.3 V；页面没有连接固定地址的 I2C 从设备。

- 参数与网络：`sda_pullup=R1 4.7KΩ to +3.3V`；`scl_pullup=R2 4.7KΩ to +3.3V`；`bus_level=+3.3V`；`i2c_device=none shown`；`address=none shown`
- 证据：图 9a19e47f4e25 / 第 1 页 / B3-B4 R1/R2/I2C_SDA/I2C_SCL/J3

## GPIO 与控制信号

### RGB 数据 GPIO

J4 pin8/GPIO5 通过 RGB 网络直接连接 LED1 DI pin3，方向为主机向 WS2812C 链输出。

- 参数与网络：`host_gpio=GPIO5`；`connector_pin=J4 pin8`；`net=RGB`；`target=LED1 DI pin3`；`direction=host-to-LED-chain`
- 证据：图 9a19e47f4e25 / 第 1 页 / B1 RGB/LED1 DI；C4 J4 pin8 GPIO5/RGB

### 红外控制 GPIO

J4 pin22/GPIO7 连接红外驱动网络 GPIO7，经 R5 控制 Q1 栅极。

- 参数与网络：`host_gpio=GPIO7`；`connector_pin=J4 pin22`；`net=GPIO7`；`target=Q1 gate via R5 1KΩ`；`direction=host-to-IR-driver`
- 证据：图 9a19e47f4e25 / 第 1 页 / D2 GPIO7/R5/Q1；C4 J4 pin22 GPIO7

## 保护电路

### 电池路径保护器件

页面在 U1、J5 与 J4 BAT+ 之间没有画出电池保护 IC、保险丝、反接保护或负载开关。

- 参数与网络：`battery_protection_ic=not shown`；`fuse=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`visible_path=U1 BAT -> BAT+ -> J5/J4 pin30`
- 证据：图 9a19e47f4e25 / 第 1 页 / D1-D4 BAT+ direct path from U1 to J5 and J4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base M5GO Bottom3 系统架构 | `host=J4 M5Stack_BUS_S3`；`rgb=LED1-LED10 WS2812C`；`infrared=IR1/Q1 SI2302`；`charging=U1 TP4057`；`external_ports=J1 UART; J2 GPIO; J3 I2C/power`；`controller=host via J4`；`storage=not shown`；`sensor=not shown` |
| 核心器件 | 十颗 WS2812C 级联 | `count=10`；`part_number=WS2812C`；`input=RGB -> LED1 DI pin3`；`chain=LED1 DO -> LED2 DI -> LED3 DI -> LED4 DI -> LED5 DI -> LED6 DI -> LED7 DI -> LED8 DI -> LED9 DI -> LED10 DI`；`last_output=LED10 DO pin1 unconnected` |
| 电源 | RGB LED 供电与去耦 | `rail=+3.3V`；`ground=LED1-LED10 pin2`；`vdd=LED1-LED10 pin4`；`decoupling=C3-C12 100nF, one per LED` |
| GPIO 与控制信号 | RGB 数据 GPIO | `host_gpio=GPIO5`；`connector_pin=J4 pin8`；`net=RGB`；`target=LED1 DI pin3`；`direction=host-to-LED-chain` |
| 接口 | 红外发射驱动 | `supply=+5V`；`emitter=IR1`；`series_resistor=R4 49.9Ω (49R9) ±1%`；`switch=Q1 SI2302`；`gate=GPIO7 via R5 1KΩ`；`gate_pulldown=R7 10KΩ`；`topology=N-MOSFET low-side switch` |
| GPIO 与控制信号 | 红外控制 GPIO | `host_gpio=GPIO7`；`connector_pin=J4 pin22`；`net=GPIO7`；`target=Q1 gate via R5 1KΩ`；`direction=host-to-IR-driver` |
| 电源 | TP4057 充电路径 | `input=VIN -> U1 VCC pin4`；`input_cap=C1 10uF`；`charger=U1 TP4057`；`battery_output=U1 BAT pin3 -> BAT+`；`output_cap=C2 10uF`；`battery_connector=J5 pin2 BAT+; J5 pin1 GND`；`host_battery=J4 pin30 BATTERY/BAT+` |
| 电源 | TP4057 PROG 配置 | `pin=U1 PROG pin6`；`resistor=R6 2KΩ`；`destination=GND`；`charge_current_label=not shown` |
| 接口 | 充电状态指示 | `indicator=D1 1615RG`；`charging=U1 CHRG pin1`；`standby=U1 STDBY pin5`；`supply=VIN via R3 1KΩ` |
| 接口 | J1 UART 四针接口 | `connector=J1 UART_Socket_4P`；`pin1=GPIO18 / UART_RXD`；`pin2=GPIO17 / UART_TXD`；`pin3=+5V / VCC`；`pin4=GND`；`host_routes=GPIO18 J4 pin15; GPIO17 J4 pin16` |
| 接口 | J2 GPIO 四针接口 | `connector=J2 GPIO_Socket_4P`；`pin1=GPIO8`；`pin2=GPIO9`；`pin3=+5V / VCC`；`pin4=GND`；`host_routes=GPIO8 J4 pin4; GPIO9 J4 pin10` |
| 总线 | J3 I2C/电源接口 | `connector=J3 SOCKET_POWER_4P`；`pin1=GND`；`pin2=VIN / +5V label`；`pin3=SDA / I2C_SDA`；`pin4=SCL / I2C_SCL`；`sda_host=J4 pin17 GPIO12`；`scl_host=J4 pin18 GPIO11`；`direction=bidirectional data; host clock` |
| 总线 | I2C 上拉 | `sda_pullup=R1 4.7KΩ to +3.3V`；`scl_pullup=R2 4.7KΩ to +3.3V`；`bus_level=+3.3V`；`i2c_device=none shown`；`address=none shown` |
| 接口 | M5Stack_BUS_S3 已用针脚 | `ground=pins1/3/5`；`gpio_socket=pin4 GPIO8; pin10 GPIO9`；`rgb=pin8 GPIO5`；`3v3=pin12`；`uart=pin15 GPIO18; pin16 GPIO17`；`i2c=pin17 GPIO12 SDA; pin18 GPIO11 SCL`；`ir=pin22 GPIO7`；`5v=pin28`；`battery=pin30 BAT+` |
| 保护电路 | 电池路径保护器件 | `battery_protection_ic=not shown`；`fuse=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`visible_path=U1 BAT -> BAT+ -> J5/J4 pin30` |
| 电源 | 内置电池容量 | `document_voltage=3.7V`；`document_capacity=500mAh`；`schematic_connector=J5 Header 2`；`schematic_capacity=null` |
| 电源 | 充电电流设定 | `charger=U1 TP4057`；`program_resistor=R6 2KΩ`；`charge_current=null`；`datasheet_formula=not present on schematic` |
| 接口 | 磁吸 pogo 接口形态 | `document_claim=magnetic pogo pin charging and I2C`；`schematic_reference=J3`；`schematic_part=SOCKET_POWER_4P`；`mechanical_type=not shown` |
| 系统结构 | CoreS3 系列兼容性 | `document_claim=CoreS3 series`；`schematic_connector=J4 M5Stack_BUS_S3`；`mechanical_compatibility=not shown`；`host_list=not shown` |

## 待确认事项

- `power.battery-capacity`：产品正文称内置电池为 3.7 V、500 mAh，但原理图只显示 J5 与 BAT+，没有电芯型号、电压或容量标注。（证据：图 9a19e47f4e25 / 第 1 页 / D2 J5/BAT+ without battery cell specification）
- `power.charge-current`：原理图确认 R6 为 2 kΩ，但页面未给 TP4057 的 PROG 公式或充电电流数值，不能仅由该页确认实际充电电流。（证据：图 9a19e47f4e25 / 第 1 页 / D1-D2 U1 PROG/R6 2KΩ）
- `interface.magnetic-pogo`：产品正文把充电与 I2C 接口描述为磁吸 pogo pin，但原理图仅将 J3 标为 SOCKET_POWER_4P，未给连接器型号、pogo 结构或磁吸极性。（证据：图 9a19e47f4e25 / 第 1 页 / B4 J3 SOCKET_POWER_4P symbol）
- `system.cores3-compatibility`：产品正文称底座适用于 CoreS3 系列；原理图把 J4 命名为 M5Stack_BUS_S3 并给出 GPIO 映射，但没有机械尺寸、堆叠高度或完整主机兼容清单。（证据：图 9a19e47f4e25 / 第 1 页 / C4-D4 J4 M5Stack_BUS_S3 electrical symbol only）
- `review.battery-capacity`：请用电芯标签、BOM 或装配资料确认内置电池为 3.7 V、500 mAh。；原因：原理图只显示 BAT+ 和两针电池连接器。
- `review.charge-current`：请按该硬件使用的 TP4057 具体版本 datasheet 与 R6=2 kΩ 复核充电电流。；原因：充电电流换算关系未出现在原理图页面。
- `review.magnetic-pogo`：请用 J3 BOM、PCB 与结构件确认其磁吸 pogo pin 型号、针脚方向和机械极性。；原因：原理图只给通用四针接口符号。
- `review.cores3-compatibility`：请用结构图和产品兼容矩阵确认适配的 CoreS3 型号及机械兼容边界。；原因：原理图只能确认 M5Stack_BUS_S3 电气网络，不能确认机械适配。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9a19e47f4e253aa2ab354b1757c0bee9b12bafb673fcc426eaaeca74d042f353` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/M5GO3_sch_01.png` |

---

源文档：`zh_CN/module/M5GO3 Bottom.md`

源文档 SHA-256：`1603aeea8ce06d86f224ed96a8fff108227703319d99be329c33b13d8c3a3def`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
