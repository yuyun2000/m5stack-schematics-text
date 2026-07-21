# Chain Angle 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Angle |
| SKU | U208 |
| 产品 ID | `chain-angle-1f6d463f3b0d` |
| 源文档 | `zh_CN/chain/Chain_Angle.md` |

## 概述

Chain Angle 以 U1 STM32G031G8U6 为主控，J1 Chain IN 使用 UART1 的 PB6/PB7，J2 Chain OUT 使用 UART2 的 PA2/PA3，形成有方向的级联链路。J1/J2 的 VCC_5V 经 U2 ME6206A33XG 转换为 VCC_3V3，为 MCU、PR1 旋转电位器和 U4 WS2812C-2020 供电。PR1 滑臂 CH1_ADC 接 U1 PB0，RGB 数据由 PA8 输出；J4 提供 SWDIO、SWCLK、NRST、3.3V 与 GND。正文中的 12-bit ADC、115200bps@8N1、280°±10° 与功耗参数未在原理图中标注，保留待确认。

## 检索关键词

`Chain Angle`、`U208`、`STM32G031G8U6`、`ME6206A33XG`、`WS2812C-2020`、`RPot`、`CH1_ADC`、`PB0`、`PA8`、`RGB`、`Chain direction`、`Chain IN`、`Chain OUT`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PB6`、`PB7`、`PA2`、`PA3`、`GROVE_IO`、`VCC_5V`、`VCC_3V3`、`SWD_5P`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`115200bps`、`8N1`、`12-bit ADC`、`280 degree`、`U208 Main V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 采样电位器、驱动 RGB，并以 UART1/UART2 实现 Chain 入口/出口通信的主控 | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 B2-C3，U1 STM32G031G8U6 pins1-28 |
| U2 | ME6206A33XG | VCC_5V 到 VCC_3V3 的 LDO | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 A3，LDO 区 U2 ME6206A33XG |
| J1 | GROVE_IO | Chain IN 四针接口，承载 TXD1、RXD1、VCC_5V、GND | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 A1，J1 GROVE_IO 与 IN 箭头 |
| J2 | GROVE_IO | Chain OUT 四针接口，承载 RXD2、TXD2、VCC_5V、GND | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 A2，J2 GROVE_IO 与 OUT 箭头 |
| PR1 | RPot | 3.3V/GND 之间的旋转电位器，滑臂输出 CH1_ADC | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 C1-C2，PR1 RPot、CCW/CW、CH1_ADC |
| U4 | WS2812C-2020 | 由 MCU PA8/RGB 驱动的单颗可编程 RGB LED | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 C2-C3，U4 WS2812C-2020 与 C12 |
| J4 | SWD_5P | 引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 与 GND 的调试接口 | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 B3，J4 SWD_5P pins1-5 |
| R2,C1 | 10KΩ / 1uF | STM32 NRST 上拉和复位电容 | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 B1，NRST/R2/C1 |
| C2,C3 | 100nF / 10uF | STM32 VDD/VDDA 的 3.3V 去耦 | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 B1-B2，U1 VDD/VDDA 旁 C2/C3 |
| C5,C7,C8 | 10uF / 100nF / 10uF | ME6206A33XG 输入与输出旁路电容 | 图 762c9ebe13dd / 第 1 页 / 第 1 页网格 A3，U2 周围 C5/C7/C8 |

## 系统结构

### Chain Angle 系统架构

U1 STM32G031G8U6 通过两个 UART 连接 Chain IN/OUT，PB0 采样 PR1 电位器，PA8 驱动 U4 RGB；U2 将接口 5V 转换为全板 3.3V。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`input=J1 Chain IN`；`output=J2 Chain OUT`；`analog=PR1 RPot -> CH1_ADC/PB0`；`rgb=PA8 -> U4 WS2812C-2020`；`ldo=U2 ME6206A33XG`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页完整 Chain Angle 单页，Chain direction/LDO/MCU/Angle/RGB 分区

## 电源

### 5V 到 3.3V 稳压

U2 ME6206A33XG pin3 VIN 接 VCC_5V，pin2 VOUT 输出 VCC_3V3，pin1 GND；C5 10uF 位于输入，C7 100nF 与 C8 10uF 位于输出。

- 参数与网络：`input=U2 pin3 VCC_5V`；`output=U2 pin2 VCC_3V3`；`ground=U2 pin1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF,C8 10uF`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 A3 LDO 区 U2/C5/C7/C8

### 5V/3.3V 电源分配

J1/J2 均引出 VCC_5V；VCC_3V3 为 U1 VDD/VDDA、PR1、U4 VDD 和 J4 pin1 供电。

- 参数与网络：`five_volt=J1/J2 VCC -> U2 VIN`；`three_volt=U2 VOUT`；`loads=U1,PR1,U4,J4`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页全部 VCC_5V/VCC_3V3 网络

## 接口

### J1 Chain IN

J1 GROVE_IO 的 IO2=TXD1、IO1=RXD1，并提供 VCC_5V 与 GND；页面箭头标为 IN。

- 参数与网络：`connector=J1 GROVE_IO`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction=IN`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 A1 J1 与 IN 箭头

### J2 Chain OUT

J2 GROVE_IO 的 IO2=RXD2、IO1=TXD2，并提供 VCC_5V 与 GND；页面箭头标为 OUT。

- 参数与网络：`connector=J2 GROVE_IO`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction=OUT`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 A2 J2 与 OUT 箭头

## 总线

### UART1 Chain IN 映射

U1 PB6 pin26 连接 TXD1/J1 IO2，PB7 pin27 连接 RXD1/J1 IO1。

- 参数与网络：`tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`controller=U1 UART1`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 U1 PB6/PB7 与 J1 TXD1/RXD1

### UART2 Chain OUT 映射

U1 PA2 pin8 连接 TXD2/J2 IO1，PA3 pin9 连接 RXD2/J2 IO2。

- 参数与网络：`tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`controller=U1 UART2`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 U1 PA2/PA3 与 J2 TXD2/RXD2

### SDA/SCL 未连接

U1 pin19 PA12[PA10] 标 SDA、pin18 PA11[PA9] 标 SCL，两条短线均带未连接标记，页面没有 I2C 设备或地址。

- 参数与网络：`sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`i2c_devices=null`；`addresses=null`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 U1 右侧 SDA/SCL 红色未连接标记

## GPIO 与控制信号

### WS2812C RGB 控制

U1 PA8 pin16 的 RGB 网络连接 U4 DI pin3；U4 VDD pin4 接 VCC_3V3、GND pin2 接地、DO pin1 未连接，C12 100nF 去耦。

- 参数与网络：`mcu_pin=U1 PA8 pin16`；`data=RGB -> U4 pin3 DI`；`supply=U4 pin4 VCC_3V3`；`ground=U4 pin2 GND`；`data_out=U4 pin1 DO NC`；`decoupling=C12 100nF`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 B2 PA8/RGB 与 C2-C3 U4/C12

## 时钟

### 外部时钟未装

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 未连接，页面未显示晶振、谐振器或有源振荡器。

- 参数与网络：`osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`external_crystal=null`；`oscillator=null`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 U1 pins1/2 与完整页面无时钟器件

## 复位

### STM32 NRST

U1 PF2-NRST pin5 接 NRST，R2 10KΩ上拉到 VCC_3V3，C1 1uF 接 GND；NRST 同时引到 J4 pin4。

- 参数与网络：`mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug=J4 pin4`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 B1 NRST/R2/C1 与 B3 J4

## 保护电路

### Grove 与电位器保护

J1/J2 UART、VCC_5V 以及 PR1 CH1_ADC 路径未显示 TVS、保险丝、串联限流、反接或过压保护。

- 参数与网络：`uart_tvs=null`；`power_fuse=null`；`adc_protection=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 J1/J2/PR1 全部外部路径，无保护器件

## 内存与 Flash

### 外部存储器边界

完整单页未显示外部 Flash、EEPROM、RAM 或存储卡接口。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`memory_card=null`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页完整单页器件，无外部存储

## 调试与烧录

### 五针 SWD 接口

J4 pin1=VCC_3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；SWCLK 接 U1 PA14-BOOT0 pin21，SWDIO 接 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK/PA14 pin21`；`pin3=MCU_SWDIO/PA13 pin20`；`pin4=NRST`；`pin5=GND`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 B3 J4 与 U1 PA14/PA13

## 模拟电路

### 旋转电位器 ADC 输入

PR1 两端分别接 VCC_3V3 与 GND，pin2 滑臂输出 CH1_ADC，连接 U1 PB0 pin14；图中标出 CCW 与 CW 端方向。

- 参数与网络：`component=PR1 RPot`；`high=pin1 VCC_3V3`；`wiper=pin2 CH1_ADC -> U1 PB0 pin14`；`low=pin3 GND`；`orientation=CCW high,CW low`
- 证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 C1-C2 PR1 RPot 与 U1 PB0/CH1_ADC

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Angle 系统架构 | `mcu=U1 STM32G031G8U6`；`input=J1 Chain IN`；`output=J2 Chain OUT`；`analog=PR1 RPot -> CH1_ADC/PB0`；`rgb=PA8 -> U4 WS2812C-2020`；`ldo=U2 ME6206A33XG` |
| 电源 | 5V 到 3.3V 稳压 | `input=U2 pin3 VCC_5V`；`output=U2 pin2 VCC_3V3`；`ground=U2 pin1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF,C8 10uF` |
| 电源 | 5V/3.3V 电源分配 | `five_volt=J1/J2 VCC -> U2 VIN`；`three_volt=U2 VOUT`；`loads=U1,PR1,U4,J4` |
| 接口 | J1 Chain IN | `connector=J1 GROVE_IO`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction=IN` |
| 接口 | J2 Chain OUT | `connector=J2 GROVE_IO`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction=OUT` |
| 总线 | UART1 Chain IN 映射 | `tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`controller=U1 UART1` |
| 总线 | UART2 Chain OUT 映射 | `tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`controller=U1 UART2` |
| 模拟电路 | 旋转电位器 ADC 输入 | `component=PR1 RPot`；`high=pin1 VCC_3V3`；`wiper=pin2 CH1_ADC -> U1 PB0 pin14`；`low=pin3 GND`；`orientation=CCW high,CW low` |
| GPIO 与控制信号 | WS2812C RGB 控制 | `mcu_pin=U1 PA8 pin16`；`data=RGB -> U4 pin3 DI`；`supply=U4 pin4 VCC_3V3`；`ground=U4 pin2 GND`；`data_out=U4 pin1 DO NC`；`decoupling=C12 100nF` |
| 复位 | STM32 NRST | `mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug=J4 pin4` |
| 调试与烧录 | 五针 SWD 接口 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK/PA14 pin21`；`pin3=MCU_SWDIO/PA13 pin20`；`pin4=NRST`；`pin5=GND` |
| 总线 | SDA/SCL 未连接 | `sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`i2c_devices=null`；`addresses=null` |
| 时钟 | 外部时钟未装 | `osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`external_crystal=null`；`oscillator=null` |
| 内存与 Flash | 外部存储器边界 | `flash=null`；`eeprom=null`；`ram=null`；`memory_card=null` |
| 保护电路 | Grove 与电位器保护 | `uart_tvs=null`；`power_fuse=null`；`adc_protection=null`；`reverse_polarity=null`；`overvoltage=null` |
| 总线 | 正文 UART 参数 | `documented_baud=115200`；`documented_format=8N1`；`schematic_rate=null`；`schematic_format=null` |
| 模拟电路 | 正文 12-bit ADC | `documented_resolution=12-bit`；`input=PB0 CH1_ADC`；`reference_voltage=null`；`sample_time=null`；`calibration=null`；`noise=null`；`enob=null` |
| 传感器 | 正文旋转角度与电位器参数 | `documented_angle=280 degrees +/-10 degrees`；`resistance=null`；`taper=null`；`linearity=null`；`lifetime=null`；`output_range=null` |
| 电源 | 正文 5V 与 RGB 功耗 | `documented_input=DC 5V`；`documented_rgb_on=21.13mA`；`input_range=null`；`ldo_current=null`；`test_conditions=null`；`peak_current=null` |

## 待确认事项

- `bus.documented-uart-format`：正文规格称 UART 为 115200bps@8N1；原理图只确认 TXD/RXD 与 GPIO 映射，没有波特率、数据位、校验或停止位文字。（证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 J1/J2/U1 UART 网络，无速率/帧格式）
- `analog.documented-adc-resolution`：正文称对外输出最大 12-bit 分辨率；原理图确认 CH1_ADC 接 PB0，但没有 ADC 位数、参考电压、采样时间、校准、噪声或有效位数。（证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 PR1 CH1_ADC 到 U1 PB0，无 ADC 性能文字）
- `sensor.documented-angle-range`：正文规格列出旋转角度 280°±10°；原理图仅标 PR1 RPot 与 CCW/CW，没有阻值、锥度、机械角度、线性度、寿命或输出范围。（证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 PR1 RPot，仅电气连接和 CCW/CW）
- `power.documented-consumption`：正文称输入 DC 5V、RGB 开启功耗 21.13mA；原理图确认 VCC_5V 与 LDO 路径，但未标允许输入范围、LDO 额定电流、整机/LED 测试条件或峰值电流。（证据：图 762c9ebe13dd / 第 1 页 / 第 1 页 J1/J2 VCC_5V、U2 与 U4，无额定/功耗文字）
- `review.uart-format`：请用内置固件与通信协议确认 UART1/UART2 是否固定为 115200bps 8N1，以及级联转发时序。；原因：原理图不含通信参数。
- `review.adc-resolution`：请确认固件 ADC 分辨率、参考电压、采样时间、滤波、校准和有效位数。；原因：原理图只确认 PB0 模拟输入。
- `review.potentiometer`：请确认 PR1 料号、阻值、锥度、280°公差、线性度、寿命、端点死区和 ADC 电压范围。；原因：原理图没有电位器机械/性能规格。
- `review.power-consumption`：请确认 5V 输入范围、ME6206A33XG 电流裕量、RGB 亮度配置与 21.13mA 测试条件。；原因：原理图未标额定电流与功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `762c9ebe13dd49846df7826b3878a7c730feaa880fc976efdc61117d3c181975` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1197/U208_sche__Chain-Angle_SCH_Main_V1.0_20250704_2025_10_14_11_04_40_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Angle.md`

源文档 SHA-256：`1393a189187af7e195e9cd84bb4ab1acd3314a27d989945b81e11d24ff5010ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
