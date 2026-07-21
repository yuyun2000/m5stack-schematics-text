# Chain Key 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Key |
| SKU | U206 |
| 产品 ID | `chain-key-663f4af06229` |
| 源文档 | `zh_CN/chain/Chain_Key.md` |

## 概述

Chain Key 以 U1 STM32G031G8U6 为主控，J1/J2 按 IN/OUT 方向分别连接 USART1 的 PB6/PB7 和 USART2 的 PA2/PA3，从而形成双 UART 级联节点。VCC_5V 经 U2 ME6206A33XG LDO 生成 VCC_3V3，为 MCU、按键上拉、SWD 和两颗 WS2812C-2020 供电。PB0 连接带 10KΩ 上拉、100nF 滤波和 PESD3V3S1UB 防护的按键，PA8 驱动 RGB 网络，J4 提供 SWDIO/SWCLK/NRST 调试与复位。

## 检索关键词

`Chain Key`、`U206`、`STM32G031G8U6`、`ME6206A33XG`、`WS2812C-2020`、`WS2812B`、`PESD3V3S1UB`、`UART1`、`UART2`、`PB6 TXD1`、`PB7 RXD1`、`PA2 TXD2`、`PA3 RXD2`、`PB0 BTN1`、`PA8 RGB`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`SWD_5P`、`GROVE_IO`、`Chain direction`、`IN`、`OUT`、`VCC_5V`、`VCC_3V3`、`J1`、`J2`、`J4`、`S1 SW-PB`、`TP1`、`TP2`、`115200bps`、`HY2.0-4P`、`RGB LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | Chain 节点主控，连接两组 UART、按键、RGB、SWD 和复位 | 图 7fdf0b2fb16e / 第 1 页 / 网格 B2-C3 MCU 区：U1 STM32G031G8U6 28 脚与所有网络 |
| U2 | ME6206A33XG | 把 VCC_5V 转换为 VCC_3V3 的 LDO | 图 7fdf0b2fb16e / 第 1 页 / 网格 A3：U2 ME6206A33XG、VIN/VOUT/GND 与 C5-C8 |
| J1 | GROVE_IO | Chain IN 四针接口，引出 TXD1、RXD1、VCC_5V、GND | 图 7fdf0b2fb16e / 第 1 页 / 网格 A1-A2：J1 GROVE_IO、IN 箭头及 TXD1/RXD1/VCC_5V/GND |
| J2 | GROVE_IO | Chain OUT 四针接口，引出 RXD2、TXD2、VCC_5V、GND | 图 7fdf0b2fb16e / 第 1 页 / 网格 A2：J2 GROVE_IO、OUT 箭头及 RXD2/TXD2/VCC_5V/GND |
| J4 | SWD_5P | VCC_3V3、SWCLK、SWDIO、NRST 与 GND 调试接口 | 图 7fdf0b2fb16e / 第 1 页 / 网格 B3：J4 SWD_5P pins1-5 |
| S1 | SW-PB | BTN1 到 GND 的用户按键 | 图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D2：S1 SW-PB、BTN1、TP1/TP2 与 GND |
| D1 | PESD3V3S1UB | BTN1 对 GND 的 ESD 保护二极管 | 图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D1：D1 PESD3V3S1UB 从 BTN1 接 GND |
| U4,U5 | WS2812C-2020 | 两颗 3.3V 可编程 RGB LED | 图 7fdf0b2fb16e / 第 1 页 / 网格 C3-D3 RGB 区：U4/U5 均标 WS2812C-2020 |
| R1,C4 | 10KΩ / 100nF | BTN1 的 VCC_3V3 上拉与对地滤波网络 | 图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D1：VCC_3V3-R1-BTN1-C4-GND |
| R2,C1 | 10KΩ / 1uF | NRST 的 VCC_3V3 上拉与对地复位电容 | 图 7fdf0b2fb16e / 第 1 页 / 网格 B1-C1：VCC_3V3-R2-NRST-C1-GND |

## 系统结构

### Chain Key 系统架构

U1 STM32G031G8U6 使用两组 UART 连接 J1 IN 与 J2 OUT，PB0 读取按键，PA8 控制两颗 RGB，U2 从 5V 生成 3.3V，J4 提供 SWD 调试。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`chain_in=J1 via USART1`；`chain_out=J2 via USART2`；`button=PB0 BTN1`；`rgb=PA8 RGB -> U4/U5`；`power=U2 ME6206A33XG`；`debug=J4 SWD_5P`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 第 1 页完整单页的接口、LDO、MCU、Button 与 RGB 分区

## 电源

### VCC_5V 到 VCC_3V3

U2 ME6206A33XG VIN pin3 接 VCC_5V，VOUT pin2 输出 VCC_3V3，GND pin1 接地；输入 C6 100nF/C5 10uF，输出 C7 100nF/C8 10uF。

- 参数与网络：`input=VCC_5V`；`regulator=U2 ME6206A33XG`；`output=VCC_3V3`；`input_caps=C6 100nF; C5 10uF`；`output_caps=C7 100nF; C8 10uF`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 A3：U2 与 C5-C8/VCC_5V/VCC_3V3

## 接口

### J1 Chain IN

J1 IO2=TXD1、IO1=RXD1、VCC=VCC_5V、GND=GND；TXD1/RXD1 分别连接 U1 PB6 pin26/PB7 pin27。

- 参数与网络：`io2=TXD1 <- U1 PB6 pin26`；`io1=RXD1 -> U1 PB7 pin27`；`vcc=VCC_5V`；`ground=GND`；`chain_role=IN`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 A1-B3：J1 TXD1/RXD1 与 U1 PB6/PB7

### J2 Chain OUT

J2 IO2=RXD2、IO1=TXD2、VCC=VCC_5V、GND=GND；TXD2/RXD2 分别连接 U1 PA2 pin8/PA3 pin9。

- 参数与网络：`io2=RXD2 -> U1 PA3 pin9`；`io1=TXD2 <- U1 PA2 pin8`；`vcc=VCC_5V`；`ground=GND`；`chain_role=OUT`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 A2-B2：J2 RXD2/TXD2 与 U1 PA3/PA2

## 总线

### 双 UART 级联

USART1 使用 PB6 TXD1/PB7 RXD1 连接 IN 端，USART2 使用 PA2 TXD2/PA3 RXD2 连接 OUT 端；两个接口共享 VCC_5V 和 GND。

- 参数与网络：`uart1=PB6 TXD1, PB7 RXD1 -> J1 IN`；`uart2=PA2 TXD2, PA3 RXD2 -> J2 OUT`；`supply=VCC_5V`；`baud_rate_shown=null`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 A1-C3：J1/J2 与 U1 UART 引脚、Chain direction 箭头

## GPIO 与控制信号

### PB0 按键输入

U1 PB0 pin14 形成 BTN1，R1 10KΩ 上拉到 VCC_3V3，S1 按下时将 BTN1 接 GND，C4 100nF 与 D1 PESD3V3S1UB 均从 BTN1 接 GND。

- 参数与网络：`mcu_pin=U1 PB0 pin14`；`net=BTN1`；`pullup=R1 10KΩ to VCC_3V3`；`switch=S1 SW-PB to GND`；`filter=C4 100nF to GND`；`esd=D1 PESD3V3S1UB to GND`；`test_points=TP1 BTN1 side; TP2 GND side`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D2：U1 PB0/BTN1 与 R1/S1/C4/D1/TP1/TP2

### RGB LED 控制

U1 PA8 pin16 连接 RGB 网络并进入 U4 DI pin3；U4/U5 均由 VCC_3V3 供电且各有 C12/C13 100nF 去耦。

- 参数与网络：`mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`first_led=U4 DI pin3`；`leds=U4/U5 WS2812C-2020`；`supply=VCC_3V3`；`decoupling=C12/C13 100nF`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 B2-D3：U1 PA8/RGB 与 U4/U5/C12/C13

## 时钟

### 外部时钟器件

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 在本页未连接，完整页面未画出晶振或有源时钟器件。

- 参数与网络：`osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`external_crystal_shown=false`；`active_clock_shown=false`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 B2-C2：U1 PC14/PC15 无外接线；完整页无时钟器件

## 复位

### STM32 NRST

U1 PF2-NRST pin5 连接 NRST，R2 10KΩ 上拉至 VCC_3V3，C1 1uF 接 GND；NRST 同时引到 J4 pin4。

- 参数与网络：`mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10KΩ`；`capacitor=C1 1uF`；`debug_header=J4 pin4 NRST`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 B1-C3：R2/C1/NRST/U1 pin5/J4 pin4

## 保护电路

### 按键输入保护

D1 PESD3V3S1UB 把 BTN1 钳位到 GND，C4 100nF 同节点滤波，保护网络位于 S1 与 MCU PB0 之间。

- 参数与网络：`protected_net=BTN1`；`device=D1 PESD3V3S1UB`；`return=GND`；`filter=C4 100nF`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D1：BTN1/D1/C4/GND

## 内存与 Flash

### 外部存储器

当前完整单页未画出外接 Flash、EEPROM、PSRAM、SD 卡或其他独立存储器件。

- 参数与网络：`external_flash_shown=false`；`eeprom_shown=false`；`psram_shown=false`；`sd_card_shown=false`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 第 1 页完整单页器件范围

## 调试与烧录

### J4 SWD 调试接口

J4 pin1=VCC_3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；SWCLK/SWDIO 分别连接 U1 PA14-BOOT0 pin21 和 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND`
- 证据：图 7fdf0b2fb16e / 第 1 页 / 网格 B2-C3：U1 PA13/PA14 与 J4 SWD_5P

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Key 系统架构 | `mcu=U1 STM32G031G8U6`；`chain_in=J1 via USART1`；`chain_out=J2 via USART2`；`button=PB0 BTN1`；`rgb=PA8 RGB -> U4/U5`；`power=U2 ME6206A33XG`；`debug=J4 SWD_5P` |
| 电源 | VCC_5V 到 VCC_3V3 | `input=VCC_5V`；`regulator=U2 ME6206A33XG`；`output=VCC_3V3`；`input_caps=C6 100nF; C5 10uF`；`output_caps=C7 100nF; C8 10uF` |
| 接口 | J1 Chain IN | `io2=TXD1 <- U1 PB6 pin26`；`io1=RXD1 -> U1 PB7 pin27`；`vcc=VCC_5V`；`ground=GND`；`chain_role=IN` |
| 接口 | J2 Chain OUT | `io2=RXD2 -> U1 PA3 pin9`；`io1=TXD2 <- U1 PA2 pin8`；`vcc=VCC_5V`；`ground=GND`；`chain_role=OUT` |
| 总线 | 双 UART 级联 | `uart1=PB6 TXD1, PB7 RXD1 -> J1 IN`；`uart2=PA2 TXD2, PA3 RXD2 -> J2 OUT`；`supply=VCC_5V`；`baud_rate_shown=null` |
| GPIO 与控制信号 | PB0 按键输入 | `mcu_pin=U1 PB0 pin14`；`net=BTN1`；`pullup=R1 10KΩ to VCC_3V3`；`switch=S1 SW-PB to GND`；`filter=C4 100nF to GND`；`esd=D1 PESD3V3S1UB to GND`；`test_points=TP1 BTN1 side; TP2 GND side` |
| 保护电路 | 按键输入保护 | `protected_net=BTN1`；`device=D1 PESD3V3S1UB`；`return=GND`；`filter=C4 100nF` |
| GPIO 与控制信号 | RGB LED 控制 | `mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`first_led=U4 DI pin3`；`leds=U4/U5 WS2812C-2020`；`supply=VCC_3V3`；`decoupling=C12/C13 100nF` |
| 复位 | STM32 NRST | `mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10KΩ`；`capacitor=C1 1uF`；`debug_header=J4 pin4 NRST` |
| 调试与烧录 | J4 SWD 调试接口 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND` |
| 时钟 | 外部时钟器件 | `osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`external_crystal_shown=false`；`active_clock_shown=false` |
| 核心器件 | RGB LED 型号差异 | `schematic_part=WS2812C-2020`；`documented_part=WS2812B`；`references=U4,U5`；`assembled_part=null` |
| 总线 | UART 波特率与 Chain 协议 | `documented_uart=115200bps 8N1`；`physical_uart1=PB6/PB7`；`physical_uart2=PA2/PA3`；`protocol_fields_shown=false`；`firmware_version=null` |
| 其他事实 | 热插拔青轴按键机械规格 | `documented_switch=hot-swappable blue mechanical switch`；`schematic_switch=S1 SW-PB`；`socket_reference=null`；`switch_part_number=null`；`contact_life=null` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`eeprom_shown=false`；`psram_shown=false`；`sd_card_shown=false` |

## 待确认事项

- `component.rgb-part-variant`：原理图 U4/U5 均标 WS2812C-2020，产品正文规格写 WS2812B；当前量产 U206 的准确 RGB 型号无法由这两种不同标注唯一确认。（证据：图 7fdf0b2fb16e / 第 1 页 / 网格 C3-D3：U4/U5 器件值 WS2812C-2020）
- `bus.documented-uart-protocol`：产品正文给出 UART 115200bps@8N1 和 Chain 级联协议，但原理图只定义双 UART 电气连接，未标注波特率、帧格式、地址、命令或转发行为。（证据：图 7fdf0b2fb16e / 第 1 页 / 第 1 页 J1/J2 与 U1 双 UART，图中无协议或波特率文字）
- `other.documented-mechanical-switch`：产品正文描述热插拔青轴机械键盘按键，原理图只把 S1 标为 SW-PB，没有轴体型号、热插拔座位号、触点寿命或机械装配规格。（证据：图 7fdf0b2fb16e / 第 1 页 / 网格 C1-D2：S1 仅标 SW-PB）
- `review.rgb-part-variant`：U206 当前量产 U4/U5 使用 WS2812C-2020 还是产品正文所写 WS2812B？；原因：图纸与正文型号不同，需要 BOM 或实物丝印确认。
- `review.uart-protocol`：U206 当前固件的 UART 波特率、帧格式、节点寻址和级联转发规则是什么？；原因：这些是固件协议行为，原理图只能确认物理 UART 映射。
- `review.mechanical-switch`：S1 的量产轴体、热插拔座型号、触点寿命和装配规格是什么？；原因：原理图只有通用 SW-PB 符号，不能证明产品机械配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7fdf0b2fb16ecec916eab0a9b9c2bad7ad50f57a588492c04b3adac6ba1545ff` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1192/U206-SCH_Chain-Key_SCH_Main_V1.0_20250823_2025_09_30_21_04_28_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Key.md`

源文档 SHA-256：`b47ddef87bfae5a5f5657ab7a5ffd941792b4f29cbb6e651dfa8508aa5a5350c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
