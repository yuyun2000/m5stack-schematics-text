# Chain Encoder 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Encoder |
| SKU | U207 |
| 产品 ID | `chain-encoder-89e7cf7197fa` |
| 源文档 | `zh_CN/chain/Chain_Encoder.md` |

## 概述

Chain Encoder 以 U1 STM32G031G8U6 为主控，J1 Chain IN 使用 UART1 的 PB6/PB7，J2 Chain OUT 使用 UART2 的 PA2/PA3，形成有方向的级联链路。EC1 编码器 A/B 信号分别连接 PA6/PA7并带 10KΩ 上拉和 47pF 滤波，按键 BTN1 连接 PB0并带 10KΩ 上拉、100nF 滤波及 PESD3V3S1UB 防护。U2 ME6206A33XG 将接口 5V 转为 3.3V，PA8 驱动单颗 WS2812C-2020，J4 提供 SWD。正文中的 115200bps@8N1、编码器脉冲/机械规格和 22.51mA 待机功耗未在原理图中标注。

## 检索关键词

`Chain Encoder`、`U207`、`STM32G031G8U6`、`ME6206A33XG`、`WS2812C-2020`、`EC1`、`rotary encoder`、`A1`、`B1`、`BTN1`、`PA6`、`PA7`、`PB0`、`PA8`、`RGB`、`PESD3V3S1UB`、`Chain direction`、`Chain IN`、`Chain OUT`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PB6`、`PB7`、`PA2`、`PA3`、`GROVE_IO`、`VCC_5V`、`VCC_3V3`、`SWD_5P`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`115200bps`、`8N1`、`U207 Main V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 读取编码器 A/B/按键、驱动 RGB，并以两个 UART 实现 Chain 入口/出口通信的主控 | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 B2-C3，U1 STM32G031G8U6 pins1-28 |
| U2 | ME6206A33XG | VCC_5V 到 VCC_3V3 的 LDO | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 A3，U2 ME6206A33XG |
| J1 | GROVE_IO | Chain IN，承载 TXD1、RXD1、VCC_5V、GND | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 A1，J1 与 IN 箭头 |
| J2 | GROVE_IO | Chain OUT，承载 RXD2、TXD2、VCC_5V、GND | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 A2，J2 与 OUT 箭头 |
| EC1 | 未标注 | 带按键的 AB 增量式旋转编码器，输出 A1、B1、BTN1 | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 C1-C2，Encoder 区 EC1/EC11 与 A/B/BTN1 |
| R1,R5,C4,C6 | 10KΩ / 10KΩ / 47pF / 47pF | 编码器 A1/B1 上拉和对地滤波 | 图 3302b11a6b7c / 第 1 页 / 第 1 页 Encoder 区 A1/B1 的 R1/R5/C4/C6 |
| R6,C9,D1 | 10KΩ / 100nF / PESD3V3S1UB | BTN1 上拉、去抖/滤波与 ESD 钳位 | 图 3302b11a6b7c / 第 1 页 / 第 1 页 Encoder 区 BTN1/R6/C9/D1 |
| U4 | WS2812C-2020 | 由 PA8/RGB 驱动的单颗可编程 RGB LED | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 C2-C3，U4 WS2812C-2020/C12 |
| J4 | SWD_5P | VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND 调试接口 | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 B3，J4 SWD_5P |
| R2,C1 | 10KΩ / 1uF | STM32 NRST 上拉与复位电容 | 图 3302b11a6b7c / 第 1 页 / 第 1 页网格 B1，R2/C1/NRST |
| C5,C7,C8 | 10uF / 100nF / 10uF | ME6206A33XG 输入与输出旁路 | 图 3302b11a6b7c / 第 1 页 / 第 1 页 LDO 区 C5/C7/C8 |

## 系统结构

### Chain Encoder 系统架构

U1 STM32G031G8U6 通过两个 UART 连接 Chain IN/OUT，采集 EC1 的 A1/B1/BTN1 并驱动 U4 RGB；U2 将接口 5V 转换为 3.3V。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`input=J1`；`output=J2`；`encoder=EC1 A1/B1/BTN1`；`rgb=U4 WS2812C-2020`；`ldo=U2 ME6206A33XG`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页完整 Chain direction/LDO/MCU/Encoder/RGB 分区

## 电源

### 5V 到 3.3V 稳压

U2 pin3 VIN 接 VCC_5V，pin2 VOUT 输出 VCC_3V3，pin1 GND；C5 10uF 为输入旁路，C7 100nF 与 C8 10uF 为输出旁路。

- 参数与网络：`input=VCC_5V`；`output=VCC_3V3`；`device=U2 ME6206A33XG`；`capacitors=C5 10uF,C7 100nF,C8 10uF`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 A3 U2/C5/C7/C8

## 接口

### J1 Chain IN

J1 IO2=TXD1、IO1=RXD1，并提供 VCC_5V/GND；页面标为 IN。

- 参数与网络：`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction=IN`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 A1 J1 与 IN

### J2 Chain OUT

J2 IO2=RXD2、IO1=TXD2，并提供 VCC_5V/GND；页面标为 OUT。

- 参数与网络：`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction=OUT`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 A2 J2 与 OUT

## 总线

### UART1 Chain IN

U1 PB6 pin26 连接 TXD1/J1 IO2，PB7 pin27 连接 RXD1/J1 IO1。

- 参数与网络：`tx=PB6 pin26 -> TXD1`；`rx=PB7 pin27 -> RXD1`；`connector=J1`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 U1 PB6/PB7 与 J1

### UART2 Chain OUT

U1 PA2 pin8 连接 TXD2/J2 IO1，PA3 pin9 连接 RXD2/J2 IO2。

- 参数与网络：`tx=PA2 pin8 -> TXD2`；`rx=PA3 pin9 -> RXD2`；`connector=J2`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 U1 PA2/PA3 与 J2

### SDA/SCL 未连接

U1 pin19 SDA 与 pin18 SCL 均带未连接标记，页面没有 I2C 设备或地址。

- 参数与网络：`sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`devices=null`；`addresses=null`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 U1 SDA/SCL 红色未连接标记

## GPIO 与控制信号

### 编码器 A/B 输入

EC1 A 输出 A1 接 U1 PA6 pin12，B 输出 B1 接 PA7 pin13；A1/B1 分别由 R1/R5 10KΩ上拉到 VCC_3V3并由 C4/C6 47pF 接地。

- 参数与网络：`phase_a=EC1 A -> A1 -> PA6 pin12`；`phase_b=EC1 B -> B1 -> PA7 pin13`；`pullups=R1/R5 10K`；`filters=C4/C6 47pF`；`common=EC1 C=GND`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 Encoder 区 A/B/A1/B1/R1/R5/C4/C6 与 U1 PA6/PA7

### 编码器按键输入

EC1 按键 D/E 在按下时把 BTN1 接 GND；BTN1 连接 U1 PB0 pin14，R6 10KΩ上拉，C9 100nF 与 D1 PESD3V3S1UB 接 GND。

- 参数与网络：`net=BTN1`；`mcu_pin=PB0 pin14`；`active_level=low`；`pullup=R6 10K`；`filter=C9 100nF`；`protection=D1 PESD3V3S1UB`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 Encoder 区 D/E/BTN1/R6/C9/D1 与 U1 PB0

### WS2812C 控制

U1 PA8 pin16 的 RGB 网络连接 U4 DI pin3；U4 VDD 接 VCC_3V3、GND 接地、DO 未连接，C12 100nF 去耦。

- 参数与网络：`mcu_pin=PA8 pin16`；`data=RGB`；`led=U4 WS2812C-2020`；`supply=VCC_3V3`；`data_out=NC`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 U1 PA8 与 RGB 区 U4/C12

## 时钟

### 无外部晶振

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 未连接，页面无晶振或振荡器。

- 参数与网络：`osc32in=NC`；`osc32out=NC`；`crystal=null`；`oscillator=null`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 U1 pins1/2 与完整页

## 复位

### STM32 NRST

U1 PF2-NRST pin5 接 NRST，R2 10KΩ上拉到 VCC_3V3，C1 1uF 接 GND；NRST 同时到 J4 pin4。

- 参数与网络：`mcu_pin=PF2-NRST pin5`；`pullup=R2 10K`；`capacitor=C1 1uF`；`debug=J4 pin4`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 NRST/R2/C1/J4

## 保护电路

### BTN1 ESD 防护

D1 PESD3V3S1UB 从 BTN1 接 GND，对编码器按键信号提供钳位；J1/J2 UART 与电源路径未显示专用保护。

- 参数与网络：`device=D1 PESD3V3S1UB`；`protected_net=BTN1`；`uart_protection=null`；`power_fuse=null`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 BTN1 D1 及 J1/J2 外部路径

## 内存与 Flash

### 外部存储边界

完整单页未显示外部 Flash、EEPROM、RAM 或存储卡。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`card=null`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页完整单页，无外部存储

## 调试与烧录

### 五针 SWD

J4 pin1=VCC_3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；SWCLK 接 PA14 pin21，SWDIO 接 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=SWCLK/PA14`；`pin3=SWDIO/PA13`；`pin4=NRST`；`pin5=GND`
- 证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 B3 J4 与 U1 PA14/PA13

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Encoder 系统架构 | `mcu=U1 STM32G031G8U6`；`input=J1`；`output=J2`；`encoder=EC1 A1/B1/BTN1`；`rgb=U4 WS2812C-2020`；`ldo=U2 ME6206A33XG` |
| 电源 | 5V 到 3.3V 稳压 | `input=VCC_5V`；`output=VCC_3V3`；`device=U2 ME6206A33XG`；`capacitors=C5 10uF,C7 100nF,C8 10uF` |
| 接口 | J1 Chain IN | `io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction=IN` |
| 接口 | J2 Chain OUT | `io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction=OUT` |
| 总线 | UART1 Chain IN | `tx=PB6 pin26 -> TXD1`；`rx=PB7 pin27 -> RXD1`；`connector=J1` |
| 总线 | UART2 Chain OUT | `tx=PA2 pin8 -> TXD2`；`rx=PA3 pin9 -> RXD2`；`connector=J2` |
| GPIO 与控制信号 | 编码器 A/B 输入 | `phase_a=EC1 A -> A1 -> PA6 pin12`；`phase_b=EC1 B -> B1 -> PA7 pin13`；`pullups=R1/R5 10K`；`filters=C4/C6 47pF`；`common=EC1 C=GND` |
| GPIO 与控制信号 | 编码器按键输入 | `net=BTN1`；`mcu_pin=PB0 pin14`；`active_level=low`；`pullup=R6 10K`；`filter=C9 100nF`；`protection=D1 PESD3V3S1UB` |
| 保护电路 | BTN1 ESD 防护 | `device=D1 PESD3V3S1UB`；`protected_net=BTN1`；`uart_protection=null`；`power_fuse=null` |
| GPIO 与控制信号 | WS2812C 控制 | `mcu_pin=PA8 pin16`；`data=RGB`；`led=U4 WS2812C-2020`；`supply=VCC_3V3`；`data_out=NC` |
| 复位 | STM32 NRST | `mcu_pin=PF2-NRST pin5`；`pullup=R2 10K`；`capacitor=C1 1uF`；`debug=J4 pin4` |
| 调试与烧录 | 五针 SWD | `pin1=VCC_3V3`；`pin2=SWCLK/PA14`；`pin3=SWDIO/PA13`；`pin4=NRST`；`pin5=GND` |
| 总线 | SDA/SCL 未连接 | `sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`devices=null`；`addresses=null` |
| 时钟 | 无外部晶振 | `osc32in=NC`；`osc32out=NC`；`crystal=null`；`oscillator=null` |
| 内存与 Flash | 外部存储边界 | `flash=null`；`eeprom=null`；`ram=null`；`card=null` |
| 总线 | 正文 UART 参数 | `documented_baud=115200`；`documented_format=8N1`；`schematic_baud=null`；`schematic_format=null` |
| 传感器 | 编码器机械与脉冲参数 | `part_number=null`；`pulses_per_revolution=null`；`phase_timing=null`；`debounce=null`；`lifetime=null`；`torque=null`；`mechanical_dimensions=null` |
| 电源 | 正文输入与待机功耗 | `documented_input=DC 5V`；`documented_standby=22.51mA`；`input_range=null`；`ldo_current=null`；`rgb_state=null`；`measurement_conditions=null` |

## 待确认事项

- `bus.documented-uart-format`：正文称 UART 为 115200bps@8N1；原理图只有 TXD/RXD 映射，没有速率或帧格式。（证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 UART1/UART2，无参数文字）
- `sensor.encoder-characteristics`：原理图确认机械 AB 编码器与按键接线，但没有编码器料号、每转脉冲数、触点时序、去抖要求、寿命、旋转扭矩或 LEGO 帽机械尺寸。（证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 Encoder 区 EC1，仅接线和外围）
- `power.documented-consumption`：正文称输入 DC 5V、待机功耗 22.51mA；原理图确认 VCC_5V/LDO 路径，但未标输入范围、LDO 电流裕量、RGB 状态或测量条件。（证据：图 3302b11a6b7c / 第 1 页 / 第 1 页 VCC_5V/U2/U4，无功耗文字）
- `review.uart-format`：请用固件与协议确认 UART1/UART2 的 115200bps 8N1 和级联转发时序。；原因：原理图无通信参数。
- `review.encoder`：请确认 EC1 料号、PPR、相位、去抖、寿命、扭矩和机械尺寸。；原因：原理图只显示通用编码器符号。
- `review.power`：请确认 5V 输入范围、LDO 电流裕量与 22.51mA 待机功耗测量条件。；原因：原理图未给额定与功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3302b11a6b7c7b24f0110e3cdaad33b8c93e6944eec39f62d5750c0cbbaf0e12` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1200/U207_Chain-Encoder_SCH_Main_V1.0_20250704_2025_10_16_10_44_19_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Encoder.md`

源文档 SHA-256：`39a5e85389c56ecae340b31b69e4426fa9069fdcfe0a1bfd93f10860dc20377f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
