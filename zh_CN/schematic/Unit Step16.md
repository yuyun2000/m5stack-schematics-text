# Unit Step16 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Step16 |
| SKU | U198 |
| 产品 ID | `unit-step16-f64c5daa39b8` |
| 源文档 | `zh_CN/unit/Unit_Step16.md` |

## 概述

Unit Step16 以 U1 STM32G031G8U6 为控制器，PA0-PA3 读取 SW1 GSMR-16 的 BCD_1/BCD_2/BCD_4/BCD_8，PA4-PA7、PB0/PB1、PA8、PC6 通过 RP2/RP3 驱动 FPC1 七段数码管的 A-G/DP。J1 Grove 提供 VCC_5V、GND、SDA、SCL，SDA/SCL 由 R4/R5 上拉到 3V3并连接 U1 PA12/PA11。U2 ME6206A33XG 把 VCC_5V 转换为 3V3；U3 WS2812C-2020 由 PB5 的 RGB 数据控制，PB4 的 RGB_VDD_EN 经 R1 0R 接其 RGB_VDD。NRST 具有 R2/C1 网络，J4 提供 SWD 调试，本页未显示外部晶振、独立存储、电池、充电、射频、音频或传感器。

## 检索关键词

`Unit Step16`、`U198`、`STM32G031G8U6`、`GSMR-16`、`ME6206A33XG`、`WS2812C-2020`、`I2C`、`0x48`、`SDA`、`SCL`、`BCD_1`、`BCD_2`、`BCD_4`、`BCD_8`、`8421 BCD`、`FPC1`、`7-segment`、`segment A`、`segment B`、`segment C`、`segment D`、`segment E`、`segment F`、`segment G`、`DP`、`RGB`、`RGB_VDD_EN`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`VCC_5V`、`3V3`、`GROVE`、`16 position`、`100ms`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控 MCU，采集 BCD 编码器、驱动七段数码管/RGB，并提供 I2C 与 SWD | 图 595b65317c2a / 第 1 页 / 第 1 页网格 B2-C3，U1 STM32G031G8U6 pins1-28 与 BCD/segments/I2C/RGB/SWD/NRST |
| SW1 | GSMR-16 MINI ROTARY DIP SWITCH | 输出 1/2/4/8 四位 BCD 编码，两个 C 公共端接 GND | 图 595b65317c2a / 第 1 页 / 第 1 页网格 B1-C2，SW1 GSMR-16，1/2/4/8/C/C 引脚 |
| FPC1 | FPC 10P 7-segment display | 七段数码管接口，提供 A-G、DP 与两个 3V3 COM 引脚 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 C2-D2，FPC1 pins1-10 与 A/B/COM/C/D/E/F/COM/G/DP |
| U2 | ME6206A33XG | 将 VCC_5V 转换为 3V3 的三引脚稳压器 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 A2，U2 ME6206A33XG VIN pin3、VOUT pin2、GND pin1 |
| U3 | WS2812C-2020 | PB5 RGB 数据控制的可编程 RGB LED，RGB_VDD 经 R1 连接 PB4 RGB_VDD_EN | 图 595b65317c2a / 第 1 页 / 第 1 页网格 C3-D3，U3 WS2812C-2020、RGB/RGB_VDD/RGB_VDD_EN/R1/C4 |
| J1 | GROVE | 四针 I2C 与 5V/GND 外部接口 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 A2，J1 GROVE IO2/SCL、IO1/SDA、5V/VCC_5V、GND |
| J4 | SWD_5P | 五针 SWD 调试和复位接口 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 C4-D4，J4 pin1 3V3、pin2 MCU_SWCLK、pin3 MCU_SWDIO、pin4 NRST、pin5 GND |
| RP1 | 4.7K ±5% resistor array | BCD_1/2/4/8 四路上拉到 3V3 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 B2，RP1 4.7K ±5% 与 BCD 四线 |
| RP2,RP3 | 470R ±5% resistor arrays | U1 到 FPC1 A-G/DP 八路段信号的串联限流电阻阵列 | 图 595b65317c2a / 第 1 页 / 第 1 页网格 C2-C3，RP2 A-D 与 RP3 E/F/G/DP |

## 系统结构

### Unit Step16 系统架构

U1 STM32G031G8U6 读取 SW1 的四位 BCD，直接驱动 FPC1 七段数码管与 U3 RGB LED，并通过 J1 I2C 与外部主机通信；U2 从 5V 生成 3V3，J4 提供 SWD。

- 参数与网络：`controller=U1 STM32G031G8U6`；`encoder=SW1 GSMR-16`；`display=FPC1 7-segment`；`rgb=U3 WS2812C-2020`；`host_bus=J1 I2C`；`power=VCC_5V -> U2 -> 3V3`；`debug=J4 SWD`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 本页未包含的子系统

本页未显示外部 Flash/EEPROM、UART/SPI/CAN/RS-485/USB/SDIO/I2S、射频、音频、环境传感器、电池或充电电路。

- 参数与网络：`external_storage=null`；`other_buses=null`；`rf=null`；`audio=null`；`sensor=null`；`battery_charger=null`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页完整原理图，仅含 MCU、编码器、显示、RGB、I2C、电源与调试

## 电源

### VCC_5V 至 3V3 稳压

U2 ME6206A33XG VIN pin3 接 VCC_5V、VOUT pin2 输出 3V3、GND pin1 接地；C5 10uF 位于输入侧，C7 100nF 与 C8/C9 各 10uF 位于输出侧。

- 参数与网络：`regulator=U2 ME6206A33XG`；`input=pin3 VIN=VCC_5V`；`output=pin2 VOUT=3V3`；`ground=pin1 GND`；`input_cap=C5 10uF`；`output_caps=C7 100nF,C8/C9 10uF`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 A2，U2/C5/C7-C9/VCC_5V/3V3

## 接口

### J1 Grove I2C 针脚映射

J1 IO2 接 SCL、IO1 接 SDA、5V 接 VCC_5V、GND 接地；SDA/SCL 为双向 I2C 信号，VCC_5V/GND 为供电输入与回路。

- 参数与网络：`connector=J1 GROVE`；`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`signal_direction=bidirectional`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 A2，J1 与 SCL/SDA/VCC_5V/GND

## 总线

### STM32 I2C 总线

SDA 连接 U1 PA12[PA10] pin19，SCL 连接 U1 PA11[PA9] pin18；R5/R4 各 4.7K 将 SDA/SCL 上拉到 3V3。原理图未打印从地址。

- 参数与网络：`device=U1 STM32G031G8U6`；`sda=J1 IO1 -> SDA -> U1 pin19 PA12[PA10]`；`scl=J1 IO2 -> SCL -> U1 pin18 PA11[PA9]`；`sda_pullup=R5 4.7K to 3V3`；`scl_pullup=R4 4.7K to 3V3`；`address_printed=null`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 A2-C3，J1/R4/R5/U1 SDA/SCL

## GPIO 与控制信号

### 旋转编码器 BCD 输入映射

SW1 的 1/2/4/8 输出分别形成 BCD_1/BCD_2/BCD_4/BCD_8，并连接 U1 PA0 pin6、PA1 pin7、PA2 pin8、PA3 pin9；RP1 四路 4.7K ±5% 上拉到 3V3，公共 C 引脚接 GND。

- 参数与网络：`bit1=SW1 1 -> BCD_1 -> U1 PA0 pin6`；`bit2=SW1 2 -> BCD_2 -> PA1 pin7`；`bit4=SW1 4 -> BCD_4 -> PA2 pin8`；`bit8=SW1 8 -> BCD_8 -> PA3 pin9`；`pullups=RP1 4.7K ±5% to 3V3`；`common=C,C=GND`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 B1-C2，SW1/RP1/BCD_1-8/U1 PA0-PA3

### 七段数码管段线映射

U1 PA4/PA5/PA6/PA7 经 RP2 470R ±5% 驱动 A/B/C/D，PB0/PB1/PA8/PC6 经 RP3 470R ±5% 驱动 E/F/G/DP；FPC1 两个 COM 引脚接 3V3。

- 参数与网络：`A=U1 PA4 pin10 -> RP2 -> FPC1 pin1`；`B=PA5 pin11 -> RP2 -> pin2`；`C=PA6 pin12 -> RP2 -> pin4`；`D=PA7 pin13 -> RP2 -> pin5`；`E=PB0 pin14 -> RP3 -> pin6`；`F=PB1 pin15 -> RP3 -> pin7`；`G=PA8 pin16 -> RP3 -> pin9`；`DP=PC6 pin17 -> RP3 -> pin10`；`common=FPC1 pins3/8=3V3`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 C2-D3，U1/RP2/RP3/FPC1 A-G/DP/COM

### WS2812C RGB 控制与供电

U1 PB5 pin25 的 RGB 网络连接 U3 DI pin3；U1 PB4 pin24 的 RGB_VDD_EN 经 R1 0R 形成 RGB_VDD，连接 U3 VDD pin4，C4 100nF 从 RGB_VDD 接 GND，U3 GND pin2 接地。

- 参数与网络：`data=U1 PB5 pin25 RGB -> U3 pin3 DI`；`power_control=U1 PB4 pin24 RGB_VDD_EN -> R1 0R -> RGB_VDD -> U3 pin4 VDD`；`decoupling=C4 100nF`；`ground=U3 pin2 GND`；`dout=U3 pin1 DO unconnected`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 B3-D3，U1 PB4/PB5 与 U3/R1/C4

## 时钟

### 外部时钟连接

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 在本页未连接外部晶振或负载电容，原理图没有其他晶振、谐振器或时钟输入器件。

- 参数与网络：`pc14=unconnected`；`pc15=unconnected`；`external_crystal=null`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页 U1 pins1/2 PC14/PC15 无外接线路

## 复位

### STM32 NRST 网络

U1 PF2-NRST pin5 连接 NRST，R2 10K 将 NRST 上拉到 3V3，C1 1uF 从 NRST 接 GND，NRST 同时引至 J4 pin4。

- 参数与网络：`controller_pin=U1 PF2-NRST pin5`；`pullup=R2 10K to 3V3`；`capacitor=C1 1uF to GND`；`debug_connector=J4 pin4`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 B1-D4，R2/C1/NRST/U1/J4

## 保护电路

### Grove 与外部接口保护

J1 SDA/SCL/VCC_5V 与 FPC1/J4 外部路径未显示 TVS、专用 ESD 阵列、保险丝、反接或过压保护器件。

- 参数与网络：`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页 J1/FPC1/J4 全路径，无专用保护符号

## 调试与烧录

### J4 SWD 接口

J4 pin1=3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；MCU_SWCLK 连接 U1 PA14-BOOT0 pin21，MCU_SWDIO 连接 PA13 pin20。

- 参数与网络：`pin1=3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 B3-D4，U1 SWD 与 J4

## 模拟电路

### BCD 输入滤波

BCD_1/BCD_2/BCD_4/BCD_8 各配置一颗 100nF 电容 C6/C10/C11/C12 对 GND，与 RP1 上拉共同构成四路输入滤波网络。

- 参数与网络：`BCD_1=C6 100nF to GND`；`BCD_2=C10 100nF to GND`；`BCD_4=C11 100nF to GND`；`BCD_8=C12 100nF to GND`；`pullups=RP1 4.7K ±5%`
- 证据：图 595b65317c2a / 第 1 页 / 第 1 页网格 C1-C2，C6/C10/C11/C12 与 BCD 四线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Step16 系统架构 | `controller=U1 STM32G031G8U6`；`encoder=SW1 GSMR-16`；`display=FPC1 7-segment`；`rgb=U3 WS2812C-2020`；`host_bus=J1 I2C`；`power=VCC_5V -> U2 -> 3V3`；`debug=J4 SWD` |
| 接口 | J1 Grove I2C 针脚映射 | `connector=J1 GROVE`；`io2=SCL`；`io1=SDA`；`power=VCC_5V`；`ground=GND`；`signal_direction=bidirectional` |
| 总线 | STM32 I2C 总线 | `device=U1 STM32G031G8U6`；`sda=J1 IO1 -> SDA -> U1 pin19 PA12[PA10]`；`scl=J1 IO2 -> SCL -> U1 pin18 PA11[PA9]`；`sda_pullup=R5 4.7K to 3V3`；`scl_pullup=R4 4.7K to 3V3`；`address_printed=null` |
| 电源 | VCC_5V 至 3V3 稳压 | `regulator=U2 ME6206A33XG`；`input=pin3 VIN=VCC_5V`；`output=pin2 VOUT=3V3`；`ground=pin1 GND`；`input_cap=C5 10uF`；`output_caps=C7 100nF,C8/C9 10uF` |
| GPIO 与控制信号 | 旋转编码器 BCD 输入映射 | `bit1=SW1 1 -> BCD_1 -> U1 PA0 pin6`；`bit2=SW1 2 -> BCD_2 -> PA1 pin7`；`bit4=SW1 4 -> BCD_4 -> PA2 pin8`；`bit8=SW1 8 -> BCD_8 -> PA3 pin9`；`pullups=RP1 4.7K ±5% to 3V3`；`common=C,C=GND` |
| 模拟电路 | BCD 输入滤波 | `BCD_1=C6 100nF to GND`；`BCD_2=C10 100nF to GND`；`BCD_4=C11 100nF to GND`；`BCD_8=C12 100nF to GND`；`pullups=RP1 4.7K ±5%` |
| GPIO 与控制信号 | 七段数码管段线映射 | `A=U1 PA4 pin10 -> RP2 -> FPC1 pin1`；`B=PA5 pin11 -> RP2 -> pin2`；`C=PA6 pin12 -> RP2 -> pin4`；`D=PA7 pin13 -> RP2 -> pin5`；`E=PB0 pin14 -> RP3 -> pin6`；`F=PB1 pin15 -> RP3 -> pin7`；`G=PA8 pin16 -> RP3 -> pin9`；`DP=PC6 pin17 -> RP3 -> pin10`；`common=FPC1 pins3/8=3V3` |
| GPIO 与控制信号 | WS2812C RGB 控制与供电 | `data=U1 PB5 pin25 RGB -> U3 pin3 DI`；`power_control=U1 PB4 pin24 RGB_VDD_EN -> R1 0R -> RGB_VDD -> U3 pin4 VDD`；`decoupling=C4 100nF`；`ground=U3 pin2 GND`；`dout=U3 pin1 DO unconnected` |
| 复位 | STM32 NRST 网络 | `controller_pin=U1 PF2-NRST pin5`；`pullup=R2 10K to 3V3`；`capacitor=C1 1uF to GND`；`debug_connector=J4 pin4` |
| 调试与烧录 | J4 SWD 接口 | `pin1=3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND` |
| 时钟 | 外部时钟连接 | `pc14=unconnected`；`pc15=unconnected`；`external_crystal=null` |
| 保护电路 | Grove 与外部接口保护 | `tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null` |
| 系统结构 | 本页未包含的子系统 | `external_storage=null`；`other_buses=null`；`rf=null`；`audio=null`；`sensor=null`；`battery_charger=null` |
| 总线地址 | 正文 I2C 默认地址与配置范围 | `documented_default=0x48`；`documented_range=0x08-0x77`；`documented_persistence=true`；`hardware_address_select=null`；`external_eeprom=null` |
| 内存与 Flash | 正文 STM32 内核与频率 | `mcu=U1 STM32G031G8U6`；`documented_core=ARM Cortex-M0+ 32-bit`；`documented_clock=64MHz`；`internal_flash=null`；`internal_sram=null` |
| 核心器件 | 正文 16 定位与方向配置 | `schematic_part=SW1 GSMR-16`；`schematic_outputs=1,2,4,8`；`documented_positions=16`；`documented_code=8421 BCD`；`direction_config=clockwise/counterclockwise`；`mechanical_order=null`；`lifetime=null` |
| 接口 | 正文数码管显示功能 | `connector=FPC1`；`documented_values=0-F`；`documented_controls=brightness,working mode`；`display_part=null`；`color=null`；`brightness_levels=null`；`refresh=null`；`glyph_table=null` |
| GPIO 与控制信号 | 正文 RGB 颜色与亮度配置 | `led=U3 WS2812C-2020`；`documented_controls=color,brightness`；`color_encoding=null`；`brightness_range=null`；`timing=null`；`default_state=null`；`max_current=null` |
| 其他事实 | 正文编码值更新周期 | `documented_update_period=100ms`；`sampling_period=null`；`debounce=null`；`i2c_publish_period=null`；`latency=null` |
| 电源 | 正文待机和显示/RGB 功耗 | `documented_standby=5V@5.85mA`；`documented_display_60=5V@14.76mA`；`documented_display_100=5V@24.13mA`；`documented_rgb_100=5V@18.9mA`；`documented_all_on=5V@29.91mA`；`test_conditions=null` |

## 待确认事项

- `address.documented-i2c-address`：正文称默认地址为 0x48、可配置范围 0x08-0x77 且掉电不丢失；原理图没有地址文字、地址选择引脚、电阻、配置存储器或固件寄存器。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 J1/U1 I2C 网络，无地址或配置存储）
- `memory.documented-mcu-spec`：正文称 STM32G031G8U6 为 32位 ARM Cortex-M0+、主频64MHz；原理图只确认 U1 型号，没有展开 CPU 内核、片内 Flash/SRAM 或运行频率。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 U1 型号与外部引脚）
- `component.documented-encoder-behavior`：原理图确认 SW1 型号 GSMR-16 及 1/2/4/8 BCD 接线；正文称为16定位、8421 BCD并可配置顺/逆时针递增方向，但本页没有定位数、机械顺序、旋转寿命或方向映射表。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 SW1 GSMR-16 与 BCD_1/2/4/8，无机械参数）
- `interface.documented-display-functions`：正文称七段数码管显示 0-F，并支持亮度和工作模式配置；原理图确认 A-G/DP 与两个 3V3 COM，但未标显示器型号、颜色、亮度等级、刷新方式、模式定义或 0-F 字形表。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 FPC1 A-G/DP/COM，无显示性能文字）
- `gpio.documented-rgb-functions`：正文称可配置 RGB LED 颜色和亮度；原理图确认 U3 WS2812C-2020 的 RGB 数据及可控供电，但未给颜色编码、亮度范围、刷新时序、默认状态或最大电流。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 U3 RGB/RGB_VDD 电路，无软件参数）
- `other.documented-update-period`：正文给出编码值更新周期 100ms；原理图没有固件采样定时器、去抖周期、I2C 发布周期或延迟定义。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 SW1/BCD/U1，无固件时序）
- `power.documented-consumption`：正文列出待机5.85mA、显示60% 14.76mA、显示100% 24.13mA、RGB100% 18.9mA、显示与RGB全开29.91mA；原理图未给测试条件、刷新率、显示内容、RGB颜色、温度或容差。（证据：图 595b65317c2a / 第 1 页 / 第 1 页 VCC_5V/U2/FPC1/U3 电源路径，无功耗数据）
- `review.i2c-address`：请用当前固件和协议确认默认 0x48、0x08-0x77 可配置范围、保留地址处理及掉电保存介质。；原因：原理图未显示地址或非易失存储实现。
- `review.mcu-spec`：请用 STM32G031G8U6 datasheet 和固件时钟配置确认 Cortex-M0+、64MHz 与可用 Flash/SRAM。；原因：板级原理图不展开 MCU 内部资源。
- `review.encoder-behavior`：请用 GSMR-16 datasheet 或实测确认16定位、8421码序列、顺/逆时针映射、触点抖动与寿命。；原因：原理图只显示位权接线。
- `review.display-functions`：请确认数码管型号/颜色、0-F 字形、亮度等级、刷新/复用方式和工作模式定义。；原因：原理图只显示段线与 COM。
- `review.rgb-functions`：请用固件协议确认 WS2812C 颜色编码、亮度范围、时序、默认状态和电流限制。；原因：原理图不含软件参数。
- `review.update-period`：请确认 100ms 指采样、去抖、显示刷新还是 I2C 数据更新时间，并给出最坏延迟。；原因：该时序由固件决定，原理图不可见。
- `review.power-consumption`：请确认各功耗值的显示内容/刷新、RGB颜色、亮度算法、I2C状态、温度和测量容差。；原因：原理图不能证明整机动态功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `595b65317c2a1505884b2396878327b7e6f83003a346bf858a3df57166fbb190` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/SCH_Unit_Step16.png` |

---

源文档：`zh_CN/unit/Unit_Step16.md`

源文档 SHA-256：`309ec141aa4b69d31e7cb07411b8605f05b9ce197df30ac2cf096e7de4cf7430`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
