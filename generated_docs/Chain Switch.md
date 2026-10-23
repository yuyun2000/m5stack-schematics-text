# Chain Switch 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Switch |
| SKU | U227 |
| 产品 ID | `chain-switch-c421afa4f073` |
| 源文档 | `zh_CN/chain/Chain_Switch.md` |

## 概述

Chain Switch（U227）以 STM32G031G8U6 为主控，通过两个四针 GROVE_IO 接口形成有方向的 Chain 级联链路：J1 的 TXD1/RXD1 接 UART1，J2 的 TXD2/RXD2 接 UART2。10K 滑动电位器 PR1 的滑臂经 CH1_ADC 接 MCU PB0，PA8 的 RGB 网络驱动一颗 WS2812C-2020。J1/J2 的 VCC_5V 经 ME6206A33XG LDO 得到 VCC_3V3，并设置输入、输出、MCU 与 RGB 去耦；J4 引出 SWD 调试信号与 NRST。

## 检索关键词

`Chain Switch`、`U227`、`STM32G031G8U6`、`ME6206A33XG`、`WS2812C-2020`、`RPot-10K`、`PR1`、`CH1_ADC`、`PB0`、`PA8`、`RGB`、`Chain direction`、`Chain IN`、`Chain OUT`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PB6`、`PB7`、`PA2`、`PA3`、`GROVE_IO`、`HY2.0-4P`、`VCC_5V`、`VCC_3V3`、`SWD_5P`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`115200bps`、`8N1`、`12-bit ADC`、`U227 Main V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控 MCU，采样滑动电位器、驱动 RGB，并通过 UART1/UART2 连接 Chain 入口与出口 | 图 3200db2a8b53 / 第 1 页 / MCU 区：U1 符号、型号 STM32G031G8U6 与 pin1-28 |
| U2 | ME6206A33XG | VCC_5V 到 VCC_3V3 的 LDO | 图 3200db2a8b53 / 第 1 页 / LDO 区：U2 型号及 VIN/VOUT/GND pin3/2/1 |
| J1 | GROVE_IO | Chain IN 四针接口：IO2=TXD1、IO1=RXD1、VCC=VCC_5V、GND | 图 3200db2a8b53 / 第 1 页 / Chain direction 区左侧：J1/GROVE_IO、IN 箭头与四路网络 |
| J2 | GROVE_IO | Chain OUT 四针接口：IO2=RXD2、IO1=TXD2、VCC=VCC_5V、GND | 图 3200db2a8b53 / 第 1 页 / Chain direction 区右侧：J2/GROVE_IO、OUT 箭头与四路网络 |
| PR1 | RPot-10K | 10K 滑动电位器，滑臂输出 CH1_ADC | 图 3200db2a8b53 / 第 1 页 / Switch 区：PR1 RPot-10K 及 pin1/2/3 |
| U4 | WS2812C-2020 | 由 RGB 网络驱动的单颗可编程 RGB LED | 图 3200db2a8b53 / 第 1 页 / RGB 区：U4 WS2812C-2020 与 VDD/DO/DI/GND pin4/1/3/2 |
| J4 | SWD_5P | 五针 SWD 调试接口 | 图 3200db2a8b53 / 第 1 页 / MCU 区右侧：J4 SWD_5P 与 pin1-5 |
| R2 | 10K | NRST 上拉到 VCC_3V3 | 图 3200db2a8b53 / 第 1 页 / MCU 区左侧：R2 10K 连接 VCC_3V3 与 NRST |
| C1 | 1uF | NRST 对地复位电容 | 图 3200db2a8b53 / 第 1 页 / MCU 区左侧：C1 1uF 连接 NRST 与 GND |
| C2 | 100nF | MCU VDD/VDDA 的高频去耦电容 | 图 3200db2a8b53 / 第 1 页 / MCU 区左上：C2 100nF 跨接 VCC_3V3 与 GND |
| C3 | 10uF | MCU VDD/VDDA 的储能去耦电容 | 图 3200db2a8b53 / 第 1 页 / MCU 区左上：C3 10uF 跨接 VCC_3V3 与 GND |
| C5 / C6 | 10uF / 100nF | LDO 输入侧 VCC_5V 对地旁路 | 图 3200db2a8b53 / 第 1 页 / LDO 区左侧：C6 100nF、C5 10uF |
| C7 / C8 | 100nF / 10uF | LDO 输出侧 VCC_3V3 对地旁路 | 图 3200db2a8b53 / 第 1 页 / LDO 区右侧：C7 100nF、C8 10uF |
| C12 | 100nF | U4 WS2812C-2020 的 VCC_3V3 去耦 | 图 3200db2a8b53 / 第 1 页 / RGB 区左侧：C12 100nF 跨接 VCC_3V3 与 GND |
| C4 | NC | CH1_ADC 对地电容预留位，图中标记 NC | 图 3200db2a8b53 / 第 1 页 / Switch 区：C4 跨接 CH1_ADC 与 GND，并标注 NC |

## 系统结构

### Chain Switch 系统架构

U1 STM32G031G8U6 通过两个 UART 连接 Chain IN/OUT，PR1 滑臂经 CH1_ADC 接 PB0，PA8/RGB 驱动 U4；U2 将接口 VCC_5V 转换为 VCC_3V3。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`chain_in=J1`；`chain_out=J2`；`analog_input=PR1 -> CH1_ADC -> PB0`；`rgb=PA8 -> U4 WS2812C-2020`；`ldo=U2 ME6206A33XG`
- 证据：图 3200db2a8b53 / 第 1 页 / 整页：Chain direction、LDO、MCU、Switch 与 RGB 五个功能块

## 核心器件

### U1

U1 为 STM32G031G8U6；pin3 VDD/VDDA 接 VCC_3V3，pin4 VSS/VSSA 接地，pin5 PF2-NRST 接 NRST。

- 参数与网络：`part=STM32G031G8U6`；`vdd_vdda_pin=3`；`vss_vssa_pin=4`；`nrst_pin=5`；`package_pins=28`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区：U1 型号与 pin3/4/5

### U2

U2 为 ME6206A33XG，pin3 为 VIN、pin2 为 VOUT、pin1 为 GND。

- 参数与网络：`part=ME6206A33XG`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`
- 证据：图 3200db2a8b53 / 第 1 页 / LDO 区：U2 型号与三个引脚

### U4

U4 为 WS2812C-2020；pin4 VDD 接 VCC_3V3，pin3 DI 接 RGB，pin2 GND 接地，pin1 DO 未连接。

- 参数与网络：`part=WS2812C-2020`；`vdd_pin=4`；`data_in_pin=3`；`gnd_pin=2`；`data_out_pin=1`；`data_out_state=NC`
- 证据：图 3200db2a8b53 / 第 1 页 / RGB 区：U4 型号与 pin1-4

## 电源

### 5V 到 3.3V 稳压

U2 pin3 VIN 接 VCC_5V，pin2 VOUT 输出 VCC_3V3，pin1 接地。

- 参数与网络：`input_net=VCC_5V`；`output_net=VCC_3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`
- 证据：图 3200db2a8b53 / 第 1 页 / LDO 区：VCC_5V、U2、VCC_3V3 与 GND 连接

### LDO 输入去耦

C6 100nF 与 C5 10uF 均从 VCC_5V 接到 GND，位于 U2 VIN 侧。

- 参数与网络：`rail=VCC_5V`；`high_frequency_cap=C6 100nF`；`bulk_cap=C5 10uF`
- 证据：图 3200db2a8b53 / 第 1 页 / LDO 区左侧：C6/C5 与 VCC_5V/GND

### LDO 输出去耦

C7 100nF 与 C8 10uF 均从 VCC_3V3 接到 GND，位于 U2 VOUT 侧。

- 参数与网络：`rail=VCC_3V3`；`high_frequency_cap=C7 100nF`；`bulk_cap=C8 10uF`
- 证据：图 3200db2a8b53 / 第 1 页 / LDO 区右侧：C7/C8 与 VCC_3V3/GND

### MCU 电源去耦

C2 100nF 与 C3 10uF 从 VCC_3V3 接到 GND，并共同连接 U1 pin3 VDD/VDDA。

- 参数与网络：`rail=VCC_3V3`；`high_frequency_cap=C2 100nF`；`bulk_cap=C3 10uF`；`mcu_pin=U1 pin3 VDD/VDDA`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区左上：C2/C3、VCC_3V3、GND 与 U1 pin3

### RGB LED 去耦

C12 100nF 从 VCC_3V3 接到 GND，与 U4 pin4 VDD 同属 RGB 供电节点。

- 参数与网络：`rail=VCC_3V3`；`cap=C12 100nF`；`load_pin=U4 pin4 VDD`
- 证据：图 3200db2a8b53 / 第 1 页 / RGB 区左侧：C12、VCC_3V3、GND 与 U4 VDD

## 接口

### J1 Chain IN

J1 GROVE_IO 的 IO2=TXD1、IO1=RXD1，VCC=VCC_5V，GND=GND；页面箭头标为 IN。

- 参数与网络：`connector=J1 GROVE_IO`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND`；`direction=IN`
- 证据：图 3200db2a8b53 / 第 1 页 / Chain direction 区左侧：IN 箭头与 J1

### J2 Chain OUT

J2 GROVE_IO 的 IO2=RXD2、IO1=TXD2，VCC=VCC_5V，GND=GND；页面箭头标为 OUT。

- 参数与网络：`connector=J2 GROVE_IO`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND`；`direction=OUT`
- 证据：图 3200db2a8b53 / 第 1 页 / Chain direction 区右侧：OUT 箭头与 J2

## 总线

### UART1 Chain IN

U1 PB6 pin26 连接 TXD1，再由 J1 IO2 引出；PB7 pin27 连接 RXD1，再由 J1 IO1 引出。

- 参数与网络：`tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`controller=U1 UART1`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 pin26/27 与 Chain direction 区 J1

### UART2 Chain OUT

U1 PA2 pin8 连接 TXD2，再由 J2 IO1 引出；PA3 pin9 连接 RXD2，再由 J2 IO2 引出。

- 参数与网络：`tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`controller=U1 UART2`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 pin8/9 与 Chain direction 区 J2

### SDA/SCL 未连接

U1 pin19 PA12[PA10] 标 SDA、pin18 PA11[PA9] 标 SCL，两条短线均带未连接标记；页面没有 I2C 设备或地址。

- 参数与网络：`sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`i2c_devices=null`；`i2c_addresses=null`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 右侧 pin18/19 与红色未连接标记

## GPIO 与控制信号

### WS2812C RGB 控制

U1 PA8 pin16 的 RGB 网络连接 U4 pin3 DI；U4 pin4 VDD 接 VCC_3V3，pin2 接地，pin1 DO 未连接。

- 参数与网络：`mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`led_data_in=U4 pin3 DI`；`led_data_out=U4 pin1 DO NC`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 PA8 pin16 与 RGB 区 U4

## 时钟

### 外部时钟边界

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 未连接；完整单页未显示晶振、谐振器或有源振荡器。

- 参数与网络：`osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`crystal=null`；`oscillator=null`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 pin1/2

## 复位

### STM32 NRST

U1 PF2-NRST pin5 接 NRST，R2 10K 上拉到 VCC_3V3，C1 1uF 接 GND；NRST 同时引到 J4 pin4。

- 参数与网络：`mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10K`；`capacitor=C1 1uF`；`debug_pin=J4 pin4`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区左侧 R2/C1/NRST 与右侧 J4 pin4

## 保护电路

### 接口与滑动输入保护

完整单页未显示用于 J1/J2 UART 与电源、PR1 CH1_ADC 的 TVS、保险丝、串联限流、反接或过压保护器件。

- 参数与网络：`uart_tvs=null`；`power_fuse=null`；`adc_series_resistor=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 3200db2a8b53 / 第 1 页 / 完整单页：J1/J2、VCC_5V 与 PR1 CH1_ADC 通路

## 关键网络

### VCC_5V

VCC_5V 由 J1 VCC 与 J2 VCC 引入，并连接到 U2 pin3 VIN；该网络不直接连接 U1 或 U4 的供电脚。

- 参数与网络：`j1=VCC`；`j2=VCC`；`ldo_input=U2 pin3`；`mcu_supply=false`；`led_supply=false`
- 证据：图 3200db2a8b53 / 第 1 页 / Chain direction 区 J1/J2 VCC 与 LDO 区 VCC_5V

### VCC_3V3

VCC_3V3 由 U2 VOUT 产生，连接到 U1 pin3、PR1 pin1、U4 pin4、J4 pin1 以及各去耦电容。

- 参数与网络：`source=U2 pin2 VOUT`；`mcu=U1 pin3`；`slider=PR1 pin1`；`led=U4 pin4`；`debug=J4 pin1`
- 证据：图 3200db2a8b53 / 第 1 页 / 整页 VCC_3V3 电源符号与各负载连接

## 内存与 Flash

### 外部存储边界

完整单页未显示外部 Flash、EEPROM、RAM 或存储卡接口。

- 参数与网络：`external_flash=null`；`eeprom=null`；`ram=null`；`memory_card=null`
- 证据：图 3200db2a8b53 / 第 1 页 / 完整单页原理图

## 调试与烧录

### 五针 SWD

J4 pin1=VCC_3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；MCU_SWCLK 接 U1 PA14-BOOT0 pin21，MCU_SWDIO 接 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND`
- 证据：图 3200db2a8b53 / 第 1 页 / MCU 区 U1 pin20/21 与 J4 pin1-5

## 模拟电路

### 滑动电位器 ADC 输入

PR1 pin1 接 VCC_3V3，pin3 接 GND，pin2 滑臂输出 CH1_ADC 并连接 U1 PB0 pin14；PR1 标为 RPot-10K。

- 参数与网络：`component=PR1 RPot-10K`；`high=pin1 VCC_3V3`；`wiper=pin2 CH1_ADC -> U1 PB0 pin14`；`low=pin3 GND`
- 证据：图 3200db2a8b53 / 第 1 页 / Switch 区 PR1 三个引脚与 MCU 区 U1 PB0 pin14

### CH1_ADC 预留电容

C4 位于 CH1_ADC 与 GND 之间，图中标注 NC，表示该电容位不贴装。

- 参数与网络：`reference=C4`；`net=CH1_ADC`；`other_net=GND`；`population=NC`
- 证据：图 3200db2a8b53 / 第 1 页 / Switch 区 PR1 下方：C4、NC 标记与 CH1_ADC/GND 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Switch 系统架构 | `mcu=U1 STM32G031G8U6`；`chain_in=J1`；`chain_out=J2`；`analog_input=PR1 -> CH1_ADC -> PB0`；`rgb=PA8 -> U4 WS2812C-2020`；`ldo=U2 ME6206A33XG` |
| 核心器件 | U1 | `part=STM32G031G8U6`；`vdd_vdda_pin=3`；`vss_vssa_pin=4`；`nrst_pin=5`；`package_pins=28` |
| 核心器件 | U2 | `part=ME6206A33XG`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1` |
| 核心器件 | U4 | `part=WS2812C-2020`；`vdd_pin=4`；`data_in_pin=3`；`gnd_pin=2`；`data_out_pin=1`；`data_out_state=NC` |
| 电源 | 5V 到 3.3V 稳压 | `input_net=VCC_5V`；`output_net=VCC_3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1` |
| 电源 | LDO 输入去耦 | `rail=VCC_5V`；`high_frequency_cap=C6 100nF`；`bulk_cap=C5 10uF` |
| 电源 | LDO 输出去耦 | `rail=VCC_3V3`；`high_frequency_cap=C7 100nF`；`bulk_cap=C8 10uF` |
| 电源 | MCU 电源去耦 | `rail=VCC_3V3`；`high_frequency_cap=C2 100nF`；`bulk_cap=C3 10uF`；`mcu_pin=U1 pin3 VDD/VDDA` |
| 电源 | RGB LED 去耦 | `rail=VCC_3V3`；`cap=C12 100nF`；`load_pin=U4 pin4 VDD` |
| 关键网络 | VCC_5V | `j1=VCC`；`j2=VCC`；`ldo_input=U2 pin3`；`mcu_supply=false`；`led_supply=false` |
| 关键网络 | VCC_3V3 | `source=U2 pin2 VOUT`；`mcu=U1 pin3`；`slider=PR1 pin1`；`led=U4 pin4`；`debug=J4 pin1` |
| 接口 | J1 Chain IN | `connector=J1 GROVE_IO`；`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND`；`direction=IN` |
| 接口 | J2 Chain OUT | `connector=J2 GROVE_IO`；`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND`；`direction=OUT` |
| 总线 | UART1 Chain IN | `tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`controller=U1 UART1` |
| 总线 | UART2 Chain OUT | `tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`controller=U1 UART2` |
| 模拟电路 | 滑动电位器 ADC 输入 | `component=PR1 RPot-10K`；`high=pin1 VCC_3V3`；`wiper=pin2 CH1_ADC -> U1 PB0 pin14`；`low=pin3 GND` |
| 模拟电路 | CH1_ADC 预留电容 | `reference=C4`；`net=CH1_ADC`；`other_net=GND`；`population=NC` |
| GPIO 与控制信号 | WS2812C RGB 控制 | `mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`led_data_in=U4 pin3 DI`；`led_data_out=U4 pin1 DO NC` |
| 复位 | STM32 NRST | `mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10K`；`capacitor=C1 1uF`；`debug_pin=J4 pin4` |
| 调试与烧录 | 五针 SWD | `pin1=VCC_3V3`；`pin2=MCU_SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO -> U1 PA13 pin20`；`pin4=NRST`；`pin5=GND` |
| 总线 | SDA/SCL 未连接 | `sda=U1 pin19 NC`；`scl=U1 pin18 NC`；`i2c_devices=null`；`i2c_addresses=null` |
| 时钟 | 外部时钟边界 | `osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`crystal=null`；`oscillator=null` |
| 内存与 Flash | 外部存储边界 | `external_flash=null`；`eeprom=null`；`ram=null`；`memory_card=null` |
| 保护电路 | 接口与滑动输入保护 | `uart_tvs=null`；`power_fuse=null`；`adc_series_resistor=null`；`reverse_polarity=null`；`overvoltage=null` |
| 总线 | 正文 UART 参数 | `documented_baud=115200`；`documented_format=8N1`；`schematic_baud=null`；`schematic_format=null` |
| 模拟电路 | 正文 12-bit ADC | `documented_resolution=12-bit`；`documented_range=0-4095`；`mcu_input=U1 PB0 pin14`；`reference_voltage=null`；`sample_time=null`；`calibration=null` |
| 其他事实 | 正文滑动与开关模式 | `documented_modes=slider,switch`；`documented_slider_range=0-4095`；`documented_threshold_config=true`；`schematic_mode_control=null` |
| 电源 | 正文输入与功耗 | `documented_input=DC 5V`；`documented_typical_current=10.57mA`；`input_range=null`；`ldo_current_rating=null`；`rgb_state=null`；`measurement_conditions=null` |

## 待确认事项

- `bus.documented-uart-format`：产品正文列出 UART 为 115200bps@8N1；原理图只确认 TXD/RXD 与 GPIO 映射，没有速率、数据位、校验或停止位文字。（证据：图 3200db2a8b53 / 第 1 页 / MCU 区 UART1/UART2 网络与 Chain direction 区 J1/J2）
- `analog.documented-adc-resolution`：产品正文称滑动位置检测输出 0 到 4095、对应 12-bit ADC；原理图只确认 PR1 CH1_ADC 接 PB0，没有 ADC 位数、参考电压、采样时间或校准信息。（证据：图 3200db2a8b53 / 第 1 页 / Switch 区 PR1 CH1_ADC 与 MCU 区 U1 PB0 pin14）
- `other.documented-slider-modes`：产品正文列出滑动条模式与开关模式，并给开通、关断阈值行为；原理图只显示 PR1 电位器及 CH1_ADC 采样路径，不含模式切换或阈值实现。（证据：图 3200db2a8b53 / 第 1 页 / Switch 区 PR1 与 MCU 区 CH1_ADC/PB0 路径）
- `power.documented-consumption`：产品正文列出输入 DC 5V 与典型工作状态 5V@10.57mA；原理图只确认 VCC_5V 经 ME6206A33XG 转为 VCC_3V3，没有输入范围、LDO 电流裕量、RGB 状态或测量条件。（证据：图 3200db2a8b53 / 第 1 页 / LDO 区 VCC_5V、U2 与 VCC_3V3 电源路径）
- `review.uart-format`：请用内置固件与 U227 通信协议确认 UART1/UART2 是否固定为 115200bps 8N1，以及入口到出口的转发时序。；原因：原理图只确认 TXD/RXD 网络，不含通信参数或转发逻辑。
- `review.adc-resolution`：请确认固件 ADC 分辨率、参考电压、采样时间、滤波、校准与有效位数。；原因：原理图只确认 PR1 滑臂接 PB0，不包含 ADC 配置。
- `review.slider-modes`：请确认滑动条模式与开关模式的配置入口、阈值范围、默认值和持久化行为。；原因：原理图仅给出电位器采样硬件，模式与阈值由固件实现。
- `review.power-consumption`：请确认 5V 输入范围、ME6206A33XG 电流裕量、RGB 状态与 10.57mA 典型功耗的测量条件。；原因：原理图没有额定电流、允许输入范围或功耗测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3200db2a8b53e3d298c37ad07f16971cd7b149d7ff483ff0252e3905fa796862` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1283/U227_Chain_Switch_SCH_Main_V1.0_20260608_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Switch.md`

源文档 SHA-256：`014474e0347c2f50d57fce50ac78c5d8d56adf421737f5b2b65ed58091d72516`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
