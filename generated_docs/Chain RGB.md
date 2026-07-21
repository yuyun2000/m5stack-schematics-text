# Chain RGB 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain RGB |
| SKU | U218 |
| 产品 ID | `chain-rgb-0b295a8b03af` |
| 源文档 | `zh_CN/chain/Chain_RGB.md` |

## 概述

Chain RGB 以 U2 STM32G031G8U6 为主控，J1 连接 PB6/PB7 的 U1_TX/U1_RX，J2 连接 PA2/PA3 的 U2_TX/U2_RX，构成两个 Chain UART 端口。D1-D64 共 64 颗 WS2812E-1313 以单条数据链构成 8×8 点阵，PA8/RGB 经 R1 2.2KΩ进入 D1 DIN，LED 电源为 VDD。U1 TPAP7343D 从 VDD 生成 VCC_3V3，为 MCU 供电；TP1-TP5 引出 3.3V、SWDIO、SWCLK、RST 与 GND。页面标注点阵最大估算 800mA@5V，正文中的 UART 格式、RGB565/字符/旋转功能与实测功耗需固件和测试确认。

## 检索关键词

`Chain RGB`、`U218`、`STM32G031G8U6`、`TPAP7343D`、`WS2812E-1313`、`8x8 RGB matrix`、`D1-D64`、`RGB`、`PA8`、`R1 2.2K`、`VDD`、`VCC_3V3`、`U1_TX`、`U1_RX`、`U2_TX`、`U2_RX`、`PB6`、`PB7`、`PA2`、`PA3`、`UART1`、`UART2`、`GROVE_IO`、`SWDIO`、`SWCLK`、`RST`、`TP1`、`TP5`、`800mA@5V`、`12.5mA`、`RGB565`、`115200bps`、`8N1`、`64 pixels`、`SCH_Chain_RGB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32G031G8U6 | 双 UART Chain 通信与 64 点 RGB 数据输出主控 | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 B1-D2，U2 STM32G031G8U6 pins1-28 |
| U1 | TPAP7343D | VDD 到 VCC_3V3 的 LDO，EN 与 VIN 同接 VDD | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 B1，U1 TPAP7343D/C1/C2 |
| J1 | GROVE_IO | 第一 Chain UART/电源接口，提供 U1_TX、U1_RX、VDD、GND | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 A1，J1 GROVE_IO |
| J2 | GROVE_IO | 第二 Chain UART/电源接口，提供 U2_RX、U2_TX、VDD、GND | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 A1-A2，J2 GROVE_IO |
| D1-D64 | WS2812E-1313 | 串联形成 8×8 全彩 LED 点阵的 64 颗可寻址 RGB LED | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 A2-D4，D1-D64 WS2812E-1313 八行点阵 |
| R1 | 2.2KΩ | PA8/RGB 到首颗 D1 DIN 的串联数据电阻 | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 A2，RGB-R1 2.2K-D1 DIN |
| R2,C11 | 1KΩ / 1uF/25V | STM32 RST 上拉与复位电容 | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 D1-D2，RST/R2/C11 |
| TP1-TP5 | Test point | 3.3V、SWDIO、SWCLK、RST 与 GND 测试/调试点 | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 A1，TP1-TP5 标签 |
| C4-C10 | 1uF/25V | LED VDD 电源的分布式去耦电容组 | 图 fcfa8a1df34a / 第 1 页 / 第 1 页网格 D1-D2，VDD 上 C4-C10 |

## 系统结构

### Chain RGB 系统架构

U2 STM32G031G8U6 通过两组 UART 连接 J1/J2，并以 PA8/RGB 驱动 D1-D64 WS2812E-1313；U1 从 VDD 生成 MCU 的 VCC_3V3。

- 参数与网络：`mcu=U2 STM32G031G8U6`；`ports=J1/J2 GROVE_IO`；`matrix=D1-D64 WS2812E-1313`；`data=PA8 RGB`；`ldo=U1 TPAP7343D`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页完整 MCU/LDO/UART/64 LED 单页

## 核心器件

### 8×8 LED 点阵

D1-D64 按八行、每行八颗绘制，器件型号均为 WS2812E-1313，形成 8×8 物理点阵。

- 参数与网络：`rows=8`；`columns=8`；`count=64`；`part_number=WS2812E-1313`；`references=D1-D64`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 A2-D4 八行 D1-D64

## 电源

### VDD 到 3.3V 稳压

U1 TPAP7343D VIN pin4 与 EN pin3 同接 VDD，OUT pin1 输出 VCC_3V3，GND pin2/EP pin5 接 GND；C1/C2 各 1uF/25V。

- 参数与网络：`input=VDD`；`enable=EN=VDD`；`output=VCC_3V3`；`device=U1 TPAP7343D`；`capacitors=C1/C2 1uF/25V`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 B1 U1/C1/C2

### LED 与 MCU 电源域

J1/J2 的 VCC 网络为 VDD，直接供给 D1-D64；U1 从 VDD 生成 VCC_3V3，供 U2 与复位/调试网络。

- 参数与网络：`led_rail=VDD`；`mcu_rail=VCC_3V3`；`source=J1/J2 VCC`；`led_loads=D1-D64`；`mcu_load=U2`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页所有 VDD/VCC_3V3 网络

### 点阵电流估算标注

原理图在 LED 阵列上方明确标注 8*8*12.5mA=800mA@5V。

- 参数与网络：`pixels=64`；`per_pixel=12.5mA`；`total=800mA`；`voltage=5V`；`formula=8*8*12.5mA`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 A2 LED 阵列上方电流公式

## 接口

### J1 Chain 接口

J1 IO2=U1_TX、IO1=U1_RX、VCC=VDD、GND=GND。

- 参数与网络：`connector=J1`；`io2=U1_TX`；`io1=U1_RX`；`vcc=VDD`；`ground=GND`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 A1 J1

### J2 Chain 接口

J2 IO2=U2_RX、IO1=U2_TX、VCC=VDD、GND=GND。

- 参数与网络：`connector=J2`；`io2=U2_RX`；`io1=U2_TX`；`vcc=VDD`；`ground=GND`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 A1-A2 J2

## 总线

### 第一 UART 映射

U2 PB6 pin26 连接 U1_TX/J1 IO2，PB7 pin27 连接 U1_RX/J1 IO1。

- 参数与网络：`tx=PB6 pin26 -> U1_TX`；`rx=PB7 pin27 -> U1_RX`；`connector=J1`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 U2 PB6/PB7 与 J1

### 第二 UART 映射

U2 PA2 pin8 连接 U2_TX/J2 IO1，PA3 pin9 连接 U2_RX/J2 IO2。

- 参数与网络：`tx=PA2 pin8 -> U2_TX`；`rx=PA3 pin9 -> U2_RX`；`connector=J2`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 U2 PA2/PA3 与 J2

## GPIO 与控制信号

### 64 点 RGB 数据链

U2 PA8 pin16 的 RGB 经 R1 2.2KΩ进入 D1 DIN；D1-D64 的 DOUT 逐级连接下一颗 DIN，D64 DOUT 为链尾。

- 参数与网络：`mcu_pin=PA8 pin16`；`net=RGB`；`series=R1 2.2K`；`first=D1 DIN`；`last=D64`；`count=64`；`topology=daisy chain`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 PA8/RGB/R1 与 D1-D64 数据连线

## 时钟

### 无外部晶振

U2 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 未连接，页面未显示外部时钟器件。

- 参数与网络：`osc32in=NC`；`osc32out=NC`；`crystal=null`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 U2 pins1/2 与完整页面

## 复位

### STM32 RST

U2 PF2 RST pin5 接 RST，R2 1KΩ上拉至 VCC_3V3，C11 1uF/25V 接 GND，并引到 TP4。

- 参数与网络：`mcu_pin=PF2 RST pin5`；`pullup=R2 1K`；`capacitor=C11 1uF/25V`；`testpoint=TP4`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 D1-D2 RST/R2/C11/TP4

## 保护电路

### Chain 接口保护

J1/J2 的 UART、VDD 与 GND 路径未显示 TVS、保险丝、反接或过压保护器件。

- 参数与网络：`uart_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 J1/J2 外部路径

## 内存与 Flash

### 外部存储边界

完整单页未显示外部 Flash、EEPROM、RAM 或存储卡；显示缓冲由主控内部资源承担的具体大小未标。

- 参数与网络：`external_flash=null`；`eeprom=null`；`ram=null`；`memory_card=null`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页完整器件列表，无外部存储

## 调试与烧录

### SWD 与电源测试点

TP1=VCC_3V3、TP2=SWDIO、TP3=SWCLK、TP4=RST、TP5=GND；SWDIO/SWCLK 连接 U2 PA13/PA14。

- 参数与网络：`TP1=VCC_3V3`；`TP2=SWDIO/PA13`；`TP3=SWCLK/PA14`；`TP4=RST`；`TP5=GND`
- 证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 A1 TP1-TP5 与 U2 SWDIO/SWCLK

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain RGB 系统架构 | `mcu=U2 STM32G031G8U6`；`ports=J1/J2 GROVE_IO`；`matrix=D1-D64 WS2812E-1313`；`data=PA8 RGB`；`ldo=U1 TPAP7343D` |
| 电源 | VDD 到 3.3V 稳压 | `input=VDD`；`enable=EN=VDD`；`output=VCC_3V3`；`device=U1 TPAP7343D`；`capacitors=C1/C2 1uF/25V` |
| 电源 | LED 与 MCU 电源域 | `led_rail=VDD`；`mcu_rail=VCC_3V3`；`source=J1/J2 VCC`；`led_loads=D1-D64`；`mcu_load=U2` |
| 接口 | J1 Chain 接口 | `connector=J1`；`io2=U1_TX`；`io1=U1_RX`；`vcc=VDD`；`ground=GND` |
| 接口 | J2 Chain 接口 | `connector=J2`；`io2=U2_RX`；`io1=U2_TX`；`vcc=VDD`；`ground=GND` |
| 总线 | 第一 UART 映射 | `tx=PB6 pin26 -> U1_TX`；`rx=PB7 pin27 -> U1_RX`；`connector=J1` |
| 总线 | 第二 UART 映射 | `tx=PA2 pin8 -> U2_TX`；`rx=PA3 pin9 -> U2_RX`；`connector=J2` |
| GPIO 与控制信号 | 64 点 RGB 数据链 | `mcu_pin=PA8 pin16`；`net=RGB`；`series=R1 2.2K`；`first=D1 DIN`；`last=D64`；`count=64`；`topology=daisy chain` |
| 核心器件 | 8×8 LED 点阵 | `rows=8`；`columns=8`；`count=64`；`part_number=WS2812E-1313`；`references=D1-D64` |
| 电源 | 点阵电流估算标注 | `pixels=64`；`per_pixel=12.5mA`；`total=800mA`；`voltage=5V`；`formula=8*8*12.5mA` |
| 复位 | STM32 RST | `mcu_pin=PF2 RST pin5`；`pullup=R2 1K`；`capacitor=C11 1uF/25V`；`testpoint=TP4` |
| 调试与烧录 | SWD 与电源测试点 | `TP1=VCC_3V3`；`TP2=SWDIO/PA13`；`TP3=SWCLK/PA14`；`TP4=RST`；`TP5=GND` |
| 时钟 | 无外部晶振 | `osc32in=NC`；`osc32out=NC`；`crystal=null` |
| 内存与 Flash | 外部存储边界 | `external_flash=null`；`eeprom=null`；`ram=null`；`memory_card=null` |
| 保护电路 | Chain 接口保护 | `uart_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null` |
| 总线 | 正文 UART 参数 | `documented_baud=115200`；`documented_format=8N1`；`schematic_baud=null`；`schematic_format=null` |
| 其他事实 | 正文显示与字符功能 | `documented_format=RGB565`；`documented_framebuffer=64 pixels`；`documented_string_length=32`；`documented_rotation=0/90/180/270`；`font_storage=null`；`firmware_buffer=null`；`brightness_steps=null` |
| 电源 | 正文功耗参数 | `documented_standby=13.46mA@5V`；`documented_full_white=127.51mA@5V`；`schematic_estimate=800mA@5V`；`brightness_setting=null`；`refresh_conditions=null`；`measurement_boundary=null` |

## 待确认事项

- `bus.documented-uart-format`：正文称 UART 为 115200bps@8N1；原理图只显示 U1/U2 TX/RX 连接，没有速率或帧格式。（证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 J1/J2/U2 UART 网络）
- `other.documented-display-features`：正文称支持 RGB565、64 点显存、ASCII 字符、最大32字符滚动、彩色渐变、亮度调节和0/90/180/270度旋转；原理图仅确认64颗串联LED，没有像素格式、字库、缓存或算法证据。（证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 U2 与 D1-D64，未见固件功能文字）
- `power.documented-consumption`：正文列出待机 13.46mA、最大亮度白色全亮 127.51mA；原理图另标理论阵列 800mA@5V，但没有亮度设置、PWM/刷新条件、测量边界或峰值电流波形。（证据：图 fcfa8a1df34a / 第 1 页 / 第 1 页 LED 阵列与 800mA@5V 标注，无实测条件）
- `review.uart-format`：请用固件与协议确认两路 UART 的 115200bps 8N1 与级联转发时序。；原因：原理图无通信参数。
- `review.display-firmware`：请用内置固件确认 RGB565、显存、字库、滚动、渐变、亮度和旋转功能及资源占用。；原因：这些属于固件能力，原理图无法确认。
- `review.power-consumption`：请确认 13.46mA/127.51mA 的亮度、图案、刷新率和测量边界，并解释与 800mA 理论标注的差异。；原因：原理图只有理论估算，没有实测条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fcfa8a1df34aebbb1b49c3b312ea71876a863f40ec68ec75786e0f554ea8004a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/SCH_Chain_RGB_2026_04_02_10_35_51_page_01.png` |

---

源文档：`zh_CN/chain/Chain_RGB.md`

源文档 SHA-256：`c5a91cb25213e2358fc2ce976499fd26d9d6fe48babfb5a0b5b1e99a1340af86`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
