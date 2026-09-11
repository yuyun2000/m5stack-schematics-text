# Chain PIR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain PIR |
| SKU | U225 |
| 产品 ID | `chain-pir-7fef392a5345` |
| 源文档 | `zh_CN/chain/Chain_PIR.md` |

## 概述

Chain PIR 以 STM32G031G8U6 为主控，读取 AS312 热释电红外传感器输出，并由 PA8 驱动一颗 WS2812C-2020 RGB LED。两组 GROVE_I/O 连接器分别连接两路 UART 网络，板上 ME6206A33XG 将 VCC_5V 转换为 VCC_3V3，为主控、PIR 和 RGB LED 供电。调试与复位由 5 针 SWD 接口、NRST 上拉及对地电容网络提供。

## 检索关键词

`Chain PIR`、`U225`、`STM32G031G8U6`、`STM32G031`、`PIR_AS312`、`AS312`、`WS2812C-2020`、`WS2812C`、`ME6206A33XG`、`GROVE_I/O`、`SWD_5P`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PIR_OUT`、`RGB`、`VCC_5V`、`VCC_3V3`、`NRST`、`MCU_SWCLK`、`MCU_SWDIO`、`SDA`、`SCL`、`PA8`、`PB0`、`PB6`、`PB7`、`PA2`、`PA3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控制器，连接两路 UART、PIR 输入、RGB LED 数据、NRST 和 SWD 调试信号 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C2-C3，U1 方框及下方型号 STM32G031G8U6 |
| U2 | ME6206A33XG | 将 VCC_5V 转换为 VCC_3V3 的三引脚稳压器 | 图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，U2 的 VIN/VOUT/GND 引脚与 ME6206A33XG 标注 |
| P1 | PIR_AS312 | 三引脚热释电红外传感器，输出经 R1 接入 PIR_OUT | 图 31d0afa37075 / 第 1 页 / 第1页网格 D2，P1 的 VCC/OUT/GND 引脚和 PIR_AS312 标注 |
| U3 | WS2812C-2020 | 单线数据输入的 RGB LED，DI 接 RGB 网络 | 图 31d0afa37075 / 第 1 页 / 第1页网格 D3，U3 的 VDD/DI/DO/GND 引脚和 WS2812C-2020 标注 |
| J1 | GROVE_I/O | 第一组四线外部接口，承载 TXD1、RXD1、VCC_5V 和 GND | 图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J1 GROVE_I/O 符号及 IO2/IO1/VCC/GND 网络 |
| J2 | GROVE_I/O | 第二组四线外部接口，承载 RXD2、TXD2、VCC_5V 和 GND | 图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J2 GROVE_I/O 符号及 IO2/IO1/VCC/GND 网络 |
| J4 | SWD_5P | 五针 SWD 调试与复位接口 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C3，J4 SWD_5P 及 1-5 针网络 |
| R1 | 10K | P1 OUT 与 PIR_OUT 之间的串联电阻 | 图 31d0afa37075 / 第 1 页 / 第1页网格 D2，P1 OUT 右侧 R1 10K |
| R2 | 10K | NRST 到 VCC_3V3 的上拉电阻 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C2，VCC_3V3 与 NRST 之间的 R2 10K |
| C1 | 1uF | NRST 到 GND 的复位电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C2，NRST 与 GND 之间的 C1 1uF |
| C2 | 100nF | U1 VDD/VDDA 的高频去耦电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 供电左侧 C2 100nF |
| C3 | 10uF | U1 VDD/VDDA 电源轨的储能电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 供电左侧 C3 10uF |
| C5 | 10uF | U2 VIN 侧 VCC_5V 储能电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，U2 VIN 左侧 C5 10uF |
| C6 | 100nF | U2 VIN 侧 VCC_5V 高频旁路电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，U2 VIN 左侧 C6 100nF |
| C7 | 100nF | U2 VOUT 侧 VCC_3V3 高频旁路电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 B3，U2 VOUT 右侧 C7 100nF |
| C8 | 10uF | U2 VOUT 侧 VCC_3V3 储能电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 B3，U2 VOUT 右侧 C8 10uF |
| C12 | 100nF | U3 VDD 到 GND 的去耦电容 | 图 31d0afa37075 / 第 1 页 / 第1页网格 D3，U3 左侧 VCC_3V3 与 GND 之间的 C12 100nF |

## 系统结构

### 整板信号架构

U1 STM32G031G8U6 连接 P1 PIR_AS312、U3 WS2812C-2020、J1/J2 两组串口接口以及 J4 SWD 接口。

- 参数与网络：`controller=U1 STM32G031G8U6`；`sensor=P1 PIR_AS312`；`indicator=U3 WS2812C-2020`；`external_interfaces=J1, J2, J4`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-D3，U1、U2、P1、U3、J1、J2、J4 及命名网络

## 电源

### VCC_5V 输入分布

J1 和 J2 的 VCC 端均接 VCC_5V，两个连接器的 GND 端均接公共 GND。

- 参数与网络：`connectors=J1, J2`；`supply_net=VCC_5V`；`return_net=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J1/J2 的 VCC 与 GND 引脚

### U2 稳压路径

U2 ME6206A33XG 的 VIN 引脚3接 VCC_5V，VOUT 引脚2输出 VCC_3V3，GND 引脚1接地。

- 参数与网络：`reference=U2`；`part_number=ME6206A33XG`；`input_pin=3 VIN`；`input_net=VCC_5V`；`output_pin=2 VOUT`；`output_net=VCC_3V3`；`ground_pin=1 GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，U2 引脚编号及 VCC_5V/VCC_3V3 网络

### U2 输入旁路

U2 的 VCC_5V 输入端并联 C6 100nF 和 C5 10uF 到 GND。

- 参数与网络：`rail=VCC_5V`；`capacitors=C6 100nF, C5 10uF`；`return_net=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，U2 VIN 左侧 C6/C5 并联网络

### U2 输出旁路

U2 的 VCC_3V3 输出端并联 C7 100nF 和 C8 10uF 到 GND。

- 参数与网络：`rail=VCC_3V3`；`capacitors=C7 100nF, C8 10uF`；`return_net=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B3，U2 VOUT 右侧 C7/C8 并联网络

### U1 供电与去耦

U1 的 VDD/VDDA 引脚3接 VCC_3V3，VSS/VSSA 引脚4接 GND，C2 100nF 与 C3 10uF 跨接该电源与地。

- 参数与网络：`supply_pin=3 VDD/VDDA`；`supply_net=VCC_3V3`；`ground_pin=4 VSS/VSSA`；`decoupling=C2 100nF, C3 10uF`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 引脚3/4 与 C2/C3

### U3 RGB LED 供电

U3 的 VDD 引脚4接 VCC_3V3，GND 引脚2接 GND，C12 100nF 并接在 VCC_3V3 与 GND 之间。

- 参数与网络：`vdd_pin=4`；`vdd_net=VCC_3V3`；`gnd_pin=2`；`decoupling=C12 100nF`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 D3，U3 引脚4/2 与 C12

## 接口

### J1 接口网络

J1 GROVE_I/O 的 IO2 接 TXD1，IO1 接 RXD1，VCC 接 VCC_5V，GND 接 GND。

- 参数与网络：`reference=J1`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J1 GROVE_I/O 四个端子及右侧网络名

### J2 接口网络

J2 GROVE_I/O 的 IO2 接 RXD2，IO1 接 TXD2，VCC 接 VCC_5V，GND 接 GND。

- 参数与网络：`reference=J2`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J2 GROVE_I/O 四个端子及右侧网络名

### U3 数据输出边界

U3 的 DO 引脚1在本页没有外接导线，RGB 数据链未从该引脚继续引出。

- 参数与网络：`reference=U3`；`pin=1 DO`；`external_net=null`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 D3，U3 右侧 DO 引脚1 端点

## 总线

### U1 UART1 网络映射

U1 的 PB6 引脚26连接 TXD1，PB7 引脚27连接 RXD1；两网络继续连接至 J1。

- 参数与网络：`tx_pin=PB6 pin 26`；`tx_net=TXD1`；`rx_pin=PB7 pin 27`；`rx_net=RXD1`；`connector=J1`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2 与 C3，J1 的 TXD1/RXD1 及 U1 PB6/PB7

### U1 UART2 网络映射

U1 的 PA2 引脚8连接 TXD2，PA3 引脚9连接 RXD2；两网络继续连接至 J2。

- 参数与网络：`tx_pin=PA2 pin 8`；`tx_net=TXD2`；`rx_pin=PA3 pin 9`；`rx_net=RXD2`；`connector=J2`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2 与 C2，J2 的 TXD2/RXD2 及 U1 PA2/PA3

### SDA/SCL 图面边界

U1 的 PA12[PA10] 引脚19旁标注 SDA，PA11[PA9] 引脚18旁标注 SCL；两条短线末端均带红色 X 未连接标记，且未连接外部器件或接口。

- 参数与网络：`sda_pin=U1 PA12[PA10] pin 19`；`scl_pin=U1 PA11[PA9] pin 18`；`external_i2c_device=null`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C3，U1 引脚18/19 右侧 SCL/SDA 标注及红色 X 端点

## GPIO 与控制信号

### PIR GPIO 映射

PIR_OUT 接入 U1 的 PB0 引脚14。

- 参数与网络：`net=PIR_OUT`；`mcu_port=PB0`；`mcu_pin=14`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 PB0 引脚14 左侧 PIR_OUT

### RGB LED 数据映射

U1 的 PA8 引脚16通过 RGB 网络连接 U3 的 DI 引脚3。

- 参数与网络：`mcu_pin=U1 PA8 pin 16`；`net=RGB`；`device_pin=U3 DI pin 3`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C3 与 D3，U1 PA8 的 RGB 网络及 U3 DI

## 时钟

### 外部低速晶振接口

U1 的 PC14-OSC32IN 引脚1和 PC15-OSC32OUT 引脚2只画出短引脚端，页面中没有连接外部晶体或其他时钟器件。

- 参数与网络：`osc_in=PC14-OSC32IN pin 1`；`osc_out=PC15-OSC32OUT pin 2`；`external_clock_component=null`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 左上方引脚1/2 的未布线端点

## 复位

### NRST 复位网络

NRST 连接 U1 的 PF2-NRST 引脚5，并由 R2 10K 上拉到 VCC_3V3、由 C1 1uF 接到 GND。

- 参数与网络：`mcu_pin=U1 PF2-NRST pin 5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`net=NRST`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2，U1 PF2-NRST 与 R2/C1 网络

## 保护电路

### UART 接口可见保护边界

TXD1、RXD1、TXD2、RXD2 在 U1 与 J1/J2 之间直接以同名网络连接，图中未画出电平转换、串联电阻或接口保护器件。

- 参数与网络：`nets=TXD1, RXD1, TXD2, RXD2`；`visible_intermediate_components=none`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-C3，J1/J2 与 U1 之间四条同名 UART 网络的完整可见路径

### 5V 输入保护可见边界

VCC_5V 从 J1/J2 直接进入 U2 VIN；本页未画出保险丝、反接保护或浪涌抑制器件。

- 参数与网络：`input_net=VCC_5V`；`destination=U2 VIN pin 3`；`visible_input_protection=none`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-B3，J1/J2 VCC_5V 与 U2 VIN 的完整可见供电路径

## 传感器

### P1 传感器供电

P1 PIR_AS312 的引脚1 VCC 接 VCC_3V3，引脚3 GND 接 GND。

- 参数与网络：`reference=P1`；`vcc_pin=1`；`vcc_net=VCC_3V3`；`gnd_pin=3`；`gnd_net=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 D2，P1 引脚1/3 及 VCC_3V3/GND 网络

### PIR 输出链路

P1 引脚2 OUT 经 R1 10K 串联后形成 PIR_OUT，PIR_OUT 连接 U1 的 PB0 引脚14。

- 参数与网络：`sensor_pin=P1 pin 2 OUT`；`series_resistor=R1 10K`；`net=PIR_OUT`；`mcu_pin=U1 PB0 pin 14`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2 与 D2，P1 OUT-R1-PIR_OUT 及 U1 PB0

## 调试与烧录

### J4 SWD 接口引脚

J4 引脚1接 VCC_3V3，引脚2接 MCU_SWCLK，引脚3接 MCU_SWDIO，引脚4接 NRST，引脚5接 GND。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C3，J4 SWD_5P 左侧五条网络和针号

### U1 SWD 信号映射

MCU_SWCLK 连接 U1 的 PA14-BOOT0 引脚21，MCU_SWDIO 连接 U1 的 PA13 引脚20，NRST 同时连接 U1 引脚5与 J4 引脚4。

- 参数与网络：`swclk=U1 PA14-BOOT0 pin 21`；`swdio=U1 PA13 pin 20`；`reset=U1 PF2-NRST pin 5 to J4 pin 4`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 C2-C3，U1 引脚20/21/5 与 J4 对应网络

## 模拟电路

### C4 装配标记

C4 画在 P1 OUT 侧节点与 GND 之间，其数值字段明确标为 NC。

- 参数与网络：`reference=C4`；`marking=NC`；`high_node=P1 OUT side of R1`；`low_node=GND`
- 证据：图 31d0afa37075 / 第 1 页 / 第1页网格 D2，P1 OUT 节点下方 C4 与 NC 标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板信号架构 | `controller=U1 STM32G031G8U6`；`sensor=P1 PIR_AS312`；`indicator=U3 WS2812C-2020`；`external_interfaces=J1, J2, J4` |
| 电源 | VCC_5V 输入分布 | `connectors=J1, J2`；`supply_net=VCC_5V`；`return_net=GND` |
| 电源 | U2 稳压路径 | `reference=U2`；`part_number=ME6206A33XG`；`input_pin=3 VIN`；`input_net=VCC_5V`；`output_pin=2 VOUT`；`output_net=VCC_3V3`；`ground_pin=1 GND` |
| 电源 | U2 输入旁路 | `rail=VCC_5V`；`capacitors=C6 100nF, C5 10uF`；`return_net=GND` |
| 电源 | U2 输出旁路 | `rail=VCC_3V3`；`capacitors=C7 100nF, C8 10uF`；`return_net=GND` |
| 电源 | U1 供电与去耦 | `supply_pin=3 VDD/VDDA`；`supply_net=VCC_3V3`；`ground_pin=4 VSS/VSSA`；`decoupling=C2 100nF, C3 10uF` |
| 接口 | J1 接口网络 | `reference=J1`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND` |
| 接口 | J2 接口网络 | `reference=J2`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND` |
| 总线 | U1 UART1 网络映射 | `tx_pin=PB6 pin 26`；`tx_net=TXD1`；`rx_pin=PB7 pin 27`；`rx_net=RXD1`；`connector=J1` |
| 总线 | U1 UART2 网络映射 | `tx_pin=PA2 pin 8`；`tx_net=TXD2`；`rx_pin=PA3 pin 9`；`rx_net=RXD2`；`connector=J2` |
| 保护电路 | UART 接口可见保护边界 | `nets=TXD1, RXD1, TXD2, RXD2`；`visible_intermediate_components=none` |
| 传感器 | P1 传感器供电 | `reference=P1`；`vcc_pin=1`；`vcc_net=VCC_3V3`；`gnd_pin=3`；`gnd_net=GND` |
| 传感器 | PIR 输出链路 | `sensor_pin=P1 pin 2 OUT`；`series_resistor=R1 10K`；`net=PIR_OUT`；`mcu_pin=U1 PB0 pin 14` |
| 模拟电路 | C4 装配标记 | `reference=C4`；`marking=NC`；`high_node=P1 OUT side of R1`；`low_node=GND` |
| GPIO 与控制信号 | PIR GPIO 映射 | `net=PIR_OUT`；`mcu_port=PB0`；`mcu_pin=14` |
| 电源 | U3 RGB LED 供电 | `vdd_pin=4`；`vdd_net=VCC_3V3`；`gnd_pin=2`；`decoupling=C12 100nF` |
| GPIO 与控制信号 | RGB LED 数据映射 | `mcu_pin=U1 PA8 pin 16`；`net=RGB`；`device_pin=U3 DI pin 3` |
| 接口 | U3 数据输出边界 | `reference=U3`；`pin=1 DO`；`external_net=null` |
| 复位 | NRST 复位网络 | `mcu_pin=U1 PF2-NRST pin 5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`net=NRST` |
| 调试与烧录 | J4 SWD 接口引脚 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND` |
| 调试与烧录 | U1 SWD 信号映射 | `swclk=U1 PA14-BOOT0 pin 21`；`swdio=U1 PA13 pin 20`；`reset=U1 PF2-NRST pin 5 to J4 pin 4` |
| 时钟 | 外部低速晶振接口 | `osc_in=PC14-OSC32IN pin 1`；`osc_out=PC15-OSC32OUT pin 2`；`external_clock_component=null` |
| 总线 | SDA/SCL 图面边界 | `sda_pin=U1 PA12[PA10] pin 19`；`scl_pin=U1 PA11[PA9] pin 18`；`external_i2c_device=null` |
| 保护电路 | 5V 输入保护可见边界 | `input_net=VCC_5V`；`destination=U2 VIN pin 3`；`visible_input_protection=none` |
| 接口 | J1/J2 物理连接器规格 | `source_document_claim=2 x HY2.0-4P`；`schematic_labels=J1/J2 GROVE_I/O`；`unconfirmed_fields=series, pitch, keying` |
| 总线 | UART 运行参数与应用协议 | `source_document_claim=115200bps@8N1; 自动上报模式; 查询模式`；`schematic_evidence_scope=TXD1/RXD1 and TXD2/RXD2 wiring only` |
| 传感器 | PIR 检测性能 | `source_document_claim=2.4m; ±60°; 2s`；`schematic_evidence_scope=P1 supply and OUT signal path only` |
| 电源 | 工作功耗 | `source_document_claim=5V@10.74mA`；`missing_context=test conditions and operating state` |

## 待确认事项

- `interface.connector-mechanics`：源文档将两个外部接口描述为 HY2.0-4P，但原理图仅将 J1/J2 标注为 GROVE_I/O，图面不能确认连接器系列、间距和键位方向。（证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2，J1/J2 仅标 GROVE_I/O 与信号角色，未标 HY2.0-4P 机械信息）
- `bus.uart-runtime-parameters`：源文档声明 UART 115200bps@8N1、自动上报模式和查询模式；原理图只确认两组 UART 网络及 MCU 引脚，无法证明波特率、帧格式、报文协议和固件工作模式。（证据：图 31d0afa37075 / 第 1 页 / 第1页网格 B2-C3，UART 网络与引脚未包含波特率、帧格式或协议时序）
- `sensor.pir-performance`：源文档声明最大检测距离 2.4m、检测角度 ±60°、检测间隔及触发维持时间 2s；这些性能和时序参数不能由 P1 连接图确认。（证据：图 31d0afa37075 / 第 1 页 / 第1页网格 D2，P1 仅标型号、供电和输出连接，未标检测距离、角度或时序）
- `power.operating-current`：源文档给出 5V@10.74mA 工作功耗；原理图未包含测试条件、负载状态或电流测量结果，不能据图确认该数值。（证据：图 31d0afa37075 / 第 1 页 / 第1页整页供电网络，未标电流测试值或工作状态条件）
- `review.connector-mechanics`：J1/J2 的实物连接器是否确为 HY2.0-4P，其间距、键位方向和料号分别是什么？；原因：源文档给出 HY2.0-4P，原理图符号仅标 GROVE_I/O，缺少机械规格和连接器料号。
- `review.uart-runtime-parameters`：量产固件的 UART 波特率、帧格式、报文协议以及自动上报/查询模式是否与源文档一致？；原因：这些属于固件运行参数和应用层行为，连接原理图只提供 TX/RX 网络映射。
- `review.pir-performance`：当前产品版本的 PIR 最大距离、检测角度、检测间隔和触发维持时间应采用哪些实测条件与数值？；原因：原理图只确认 AS312 型号和电气连接，不能证明环境相关性能与固件时序。
- `review.operating-current`：5V@10.74mA 对应哪种固件、PIR/RGB 状态和测试条件，当前硬件版本是否复现该值？；原因：原理图没有电流测量结果或运行状态定义，需要实测记录确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `31d0afa3707513cdf5a2639ebe5b58625477988d175c749dc5d0c62edfea956f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1261/ChainPIR_V01_2025_06_18_19_10_05.png` |

---

源文档：`zh_CN/chain/Chain_PIR.md`

源文档 SHA-256：`bf35cc1dd54e08480ccfa363746526622840c5ae8168cee2995c504bbfe19499`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
