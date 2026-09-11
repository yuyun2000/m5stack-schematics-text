# Faces_Keyboard3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces_Keyboard3 |
| SKU | A003-V3 |
| 产品 ID | `faces-keyboard3-d38f8dd92d25` |
| 源文档 | `zh_CN/faces/Faces_Keyboard3.md` |

## 概述

Faces_Keyboard3 以 STM32F030C8T6 为主控，扫描由 PA0-PA9 与 PB0-PB2 构成的 10 列 3 行键矩阵，并读取 5 个独立接地按键，共覆盖 S1-S35。面板经 J1 的 3V3、GND、SDA、SCL 和 G35 网络连接主机，PB4/PB5 分别驱动两路串联 2k 电阻的 LED。P1 提供 3V3、SWCLK、SWDIO、NRST 和 GND 调试连接，主控还包含 3V3 去耦、BOOT0 下拉和 NRST 上拉加电容复位网络。

## 检索关键词

`Faces_Keyboard3`、`Faces Keyboard3`、`A003-V3`、`STM32F030C8T6`、`U1`、`35-key keyboard`、`QWERTY`、`10x3 key matrix`、`PA0-PA9`、`PB0-PB2`、`PC13-PC15`、`PF0-PF1`、`M5_BUS_22P`、`J1`、`I2C`、`SDA`、`SCL`、`G35`、`AD35`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`LED1`、`LED2`、`PB4`、`PB5`、`3V3`、`NC_0603`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030C8T6 | 键盘扫描、主机 I2C/G35 接口和双 LED 控制主控 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2-D2，U1 器件框及其 STM32F030C8T6 型号标注 |
| J1 | M5_BUS_22P | 连接主机侧 GND、3V3、G35、SDA 和 SCL 的 22 针接口 | 图 532f534f75ac / 第 1 页 / 页 1 网格 A4，J1 M5_BUS_22P 符号及针脚网络 |
| P1 | Header 5 | 3V3、SWCLK、SWDIO、NRST、GND 五针调试接口 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C3，P1 Header 5 针脚 1-5 |
| S1-S20, S22-S29, S32-S33 | 未标注 | PA0-PA9 列与 PB0-PB2 行之间的 30 键矩阵开关 | 图 532f534f75ac / 第 1 页 / 页 1 网格 A1-B3，三行十列按键阵列及 S1-S20、S22-S29、S32-S33 位号 |
| S21, S30-S31, S34-S35 | 未标注 | 分别连接 PC14、PC15、PC13、PF0、PF1 到 GND 的五个独立功能键 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C1-D2，S31 aA、S21 alt、S30 ok、S34 sym、S35 Fn 与 GND 总线 |
| LED1 | 未标注 | 由 PB4 经 R1 驱动的状态指示 LED | 图 532f534f75ac / 第 1 页 / 页 1 网格 B3，PB4-R1-LED1-GND 支路 |
| LED2 | 未标注 | 由 PB5 经 R2 驱动的状态指示 LED | 图 532f534f75ac / 第 1 页 / 页 1 网格 B3，PB5-R2-LED2-GND 支路 |
| R1-R2 | 2k_0603 | LED1 与 LED2 的串联限流电阻 | 图 532f534f75ac / 第 1 页 / 页 1 网格 B3，R1、R2 均标注 2k_0603 |
| R3 | 10k_0603 | G35 网络到 3V3 的上拉电阻 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C1-C2，3V3-R3-G35 网络 |
| R4 | 10k_0603 | U1 BOOT0 到 GND 的下拉电阻 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2，U1 pin 44 BOOT0-R4-GND |
| R5 | 10k_0603 | U1 NRST 到 3V3 的上拉电阻 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2-D2，NRST-R5-3V3 支路 |
| R6-R7 | NC_0603 | SCL 与 SDA 到 3V3 的未装配可选上拉电阻位 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2，SCL-R6-3V3 与 SDA-R7-3V3，二者均标注 NC_0603 |
| C1-C3 | 100nF | U1 3V3 供电轨到 GND 的三只去耦电容 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2，C1、C2、C3 并联于 3V3 与 GND，均标注 100nF |
| C4 | 100nF | NRST 到 GND 的复位电容 | 图 532f534f75ac / 第 1 页 / 页 1 网格 C2-D2，NRST-C4-GND 支路 |

## 系统结构

### 键盘面板架构

单页原理图显示 U1 连接 30 键矩阵、5 个独立接地按键、J1 主机接口、LED1/LED2 和 P1 调试接口。

- 参数与网络：`mcu=STM32F030C8T6`；`matrix_keys=30`；`direct_keys=5`；`total_switches=35`；`host_connector=J1 M5_BUS_22P`；`debug_connector=P1 Header 5`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 全页，键矩阵、U1、J1、LED1/LED2 与 P1 功能分区

## 核心器件

### U1 主控

U1 的图面型号完整标注为 STM32F030C8T6。

- 参数与网络：`reference=U1`；`part_number=STM32F030C8T6`；`package_pin_count=48`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2-D2，U1 下方型号与 1-48 引脚编号

### 按键开关数量

原理图包含连续位号 S1 至 S35，共 35 个按键开关符号。

- 参数与网络：`reference_range=S1-S35`；`count=35`；`matrix_switches=30`；`direct_switches=5`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A1-B3 的矩阵开关与 C1-D2 的五个独立开关

## 电源

### J1 面板供电

J1 pin 3 的 3V3 网络连接面板电源轨，J1 pin 2 连接 GND；J1 pin 1 标注 5V 但图中没有接入面板网络。

- 参数与网络：`supply_pin=J1 pin 3`；`supply_net=3V3`；`ground_pin=J1 pin 2`；`five_volt_pin=J1 pin 1, no connected net shown`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A4，J1 pin 1-3 的 5V、GND、3V3 引脚线段

### U1 电源引脚

U1 的 VDD pin 1、24、48 和 VDDA pin 9 接 3V3，VSS pin 23、47 与 VSSA pin 8 接 GND。

- 参数与网络：`positive_pins=VDD 1, VDD 24, VDD 48, VDDA 9`；`positive_net=3V3`；`ground_pins=VSS 23, VSS 47, VSSA 8`；`ground_net=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2，U1 右下 VDD/VDDA/VSS/VSSA 引脚及 3V3/GND 电源总线

### U1 电源去耦

C1、C2、C3 均为 100nF，并联连接在 U1 的 3V3 供电总线与 GND 总线之间。

- 参数与网络：`capacitors=C1, C2, C3`；`value_each=100nF`；`rail=3V3`；`return=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2，C1-C3 与 U1 电源引脚旁的 3V3/GND 总线

## 接口

### J1 已连接信号

J1 除供电外还连接 pin 4 AD35 上的 G35、pin 15 SDA 和 pin 17 SCL。

- 参数与网络：`J1_pin_4=symbol label AD35, net G35`；`J1_pin_15=SDA`；`J1_pin_17=SCL`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A4，J1 pin 4、15、17 的外接网络标签

### J1 未接入面板的针脚

J1 的 pin 1、5-14、16、18-22 在本页均以短引脚线结束，未显示连接到面板网络。

- 参数与网络：`pins=1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22`；`symbol_labels=5V, MOSI, AD36, MISO, DA25, SCK, DA26, R2/16, SK, T2/17, WS, OUT, MK, G2, IN, G5, HRR`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A4，J1 各针脚；仅 2、3、4、15、17 画有外接网络

## 总线

### U1 I2C 网络

U1 PB10 pin 21 接 SCL，PB11 pin 22 接 SDA，两条网络连接到 J1。

- 参数与网络：`SCL=U1 PB10 pin 21 to J1 pin 17`；`SDA=U1 PB11 pin 22 to J1 pin 15`；`connector=J1 M5_BUS_22P`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2 的 U1 PB10/PB11 与网格 A4 的 J1 SDA/SCL

### I2C 可选上拉位

SCL 经 R6、SDA 经 R7 接向 3V3，但 R6 与 R7 的图面值均为 NC_0603，因此原理图未声明这两只上拉电阻已装配。

- 参数与网络：`SCL_pullup=R6 NC_0603 to 3V3`；`SDA_pullup=R7 NC_0603 to 3V3`；`assembly_mark=NC`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2，U1 PB10/PB11 右侧 R6/R7 及 NC_0603 标注

## GPIO 与控制信号

### 30 键矩阵拓扑

30 个矩阵按键位于 U1 的十个列网络 PA0-PA9 与三个行网络 PB0-PB2 之间，构成 10 列 3 行矩阵。

- 参数与网络：`columns=PA0, PA1, PA2, PA3, PA4, PA5, PA6, PA7, PA8, PA9`；`rows=PB0, PB1, PB2`；`column_count=10`；`row_count=3`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A1-B3，PA9 至 PA0 竖向列与 PB0 至 PB2 横向行

### PB0 矩阵行

PB0 行依次连接 S1 Q、S2 W、S3 E、S4 R、S5 T、S6 Y、S7 U、S8 I、S9 O 和 S10 P。

- 参数与网络：`mcu_net=PB0`；`mcu_pin=18`；`switches=S1, S2, S3, S4, S5, S6, S7, S8, S9, S10`；`legends=Q, W, E, R, T, Y, U, I, O, P`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A1-A3，上方十键与右端 PB0；U1 PB0 为 pin 18

### PB1 矩阵行

PB1 行依次连接 S11 A、S12 S、S13 D、S14 F、S15 G、S16 H、S17 J、S18 K、S19 L 和 S20 del。

- 参数与网络：`mcu_net=PB1`；`mcu_pin=19`；`switches=S11, S12, S13, S14, S15, S16, S17, S18, S19, S20`；`legends=A, S, D, F, G, H, J, K, L, del`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A1-B3，中间十键与右端 PB1；U1 PB1 为 pin 19

### PB2 矩阵行

PB2 行依次连接 S32 0、S22 Z、S23 X、S24 C、S25 V、S26 B、S27 N、S28 M、S29 $ 和 S33 SPACE。

- 参数与网络：`mcu_net=PB2`；`mcu_pin=20`；`switches=S32, S22, S23, S24, S25, S26, S27, S28, S29, S33`；`legends=0, Z, X, C, V, B, N, M, $, SPACE`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 B1-B3，下方十键与右端 PB2；U1 PB2 为 pin 20

### 矩阵列与开关位号映射

矩阵列从左到右为 PA9、PA8、PA7、PA6、PA5、PA4、PA3、PA2、PA1、PA0，每列各连接三只开关。

- 参数与网络：`PA9=S1, S11, S32`；`PA8=S2, S12, S22`；`PA7=S3, S13, S23`；`PA6=S4, S14, S24`；`PA5=S5, S15, S25`；`PA4=S6, S16, S26`；`PA3=S7, S17, S27`；`PA2=S8, S18, S28`；`PA1=S9, S19, S29`；`PA0=S10, S20, S33`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A1-B3，十条竖向 PA 列网络与每列三只开关

### 五个独立功能键

S31 aA、S21 alt、S30 ok、S34 sym、S35 Fn 闭合时分别把 PC13、PC14、PC15、PF0、PF1 接到公共 GND。

- 参数与网络：`S31_aA=PC13, U1 pin 2`；`S21_alt=PC14, U1 pin 3`；`S30_ok=PC15, U1 pin 4`；`S34_sym=PF0, U1 pin 5`；`S35_Fn=PF1, U1 pin 6`；`common=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C1-D2，五个功能键、U1 pin 2-6 与左侧 GND 总线

### LED1 驱动

U1 PB4 pin 40 经 R1 2k_0603 连接 LED1 的 0 号正端，LED1 的 1 号负端接 GND。

- 参数与网络：`mcu_net=PB4`；`mcu_pin=40`；`series_resistor=R1 2k_0603`；`led_positive_terminal=0`；`led_negative_terminal=1`；`return=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 B3，PB4-R1-LED1-GND；U1 PB4 标为 pin 40

### LED2 驱动

U1 PB5 pin 41 经 R2 2k_0603 连接 LED2 的 0 号正端，LED2 的 1 号负端接 GND。

- 参数与网络：`mcu_net=PB5`；`mcu_pin=41`；`series_resistor=R2 2k_0603`；`led_positive_terminal=0`；`led_negative_terminal=1`；`return=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 B3，PB5-R2-LED2-GND；U1 PB5 标为 pin 41

### U1 未连接引脚

PA10 pin 31、PA11 pin 32、PA12 pin 33 带显式无连接标记；PB3、PB6-PB9、PB12-PB15、PF6、PF7 在本页未显示外接网络。

- 参数与网络：`explicit_no_connect=PA10 pin 31, PA11 pin 32, PA12 pin 33`；`no_external_net_shown=PB3 pin 39, PB6 pin 42, PB7 pin 43, PB8 pin 45, PB9 pin 46, PB12 pin 25, PB13 pin 26, PB14 pin 27, PB15 pin 28, PF6 pin 35, PF7 pin 36`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C1-C2，U1 左侧 PA10-PA12 红色无连接标记及其余短引脚线

## 时钟

### 振荡器复用引脚

U1 的 PC14-OSC32_IN、PC15-OSC32_OUT、PF0-OSC_IN、PF1-OSC_OUT 在图中分别作为 alt、ok、sym、Fn 按键输入，页面未画外部晶振。

- 参数与网络：`PC14_OSC32_IN=S21 alt`；`PC15_OSC32_OUT=S30 ok`；`PF0_OSC_IN=S34 sym`；`PF1_OSC_OUT=S35 Fn`；`external_crystal_shown=false`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C1-D2，U1 振荡器复用引脚名称及四个直连按键

## 复位

### NRST 复位网络

U1 NRST pin 7 接 NRST 网络，R5 10k_0603 将其上拉到 3V3，C4 100nF 将其连接到 GND，NRST 还引到 P1 pin 4。

- 参数与网络：`mcu_pin=U1 NRST pin 7`；`pullup=R5 10k_0603 to 3V3`；`capacitor=C4 100nF to GND`；`debug_pin=P1 pin 4`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2-D2 的 U1 NRST/R5/C4 与网格 C3 的 P1 NRST

### BOOT0 配置

U1 BOOT0 pin 44 通过 R4 10k_0603 下拉到 GND。

- 参数与网络：`mcu_pin=U1 BOOT0 pin 44`；`pulldown=R4 10k_0603`；`net=GND`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C2，U1 BOOT0 pin 44-R4-GND

## 关键网络

### G35 网络

U1 PA15 pin 38 连接 G35；G35 同时连接 J1 pin 4 的 AD35 引脚，并通过 R3 10k_0603 上拉到 3V3。

- 参数与网络：`mcu_pin=U1 PA15 pin 38`；`connector_pin=J1 pin 4 AD35`；`pullup=R3 10k_0603 to 3V3`；`net=G35`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C1-C2 的 U1 PA15/G35/R3 与网格 A4 的 J1 AD35/G35

## 调试与烧录

### P1 SWD 调试接口

P1 pin 1-5 依次为 3V3、SWCLK、SWDIO、NRST、GND；SWCLK 连接 U1 PA14 pin 37，SWDIO 连接 U1 PA13 pin 34。

- 参数与网络：`pin_1=3V3`；`pin_2=SWCLK`；`pin_3=SWDIO`；`pin_4=NRST`；`pin_5=GND`；`SWCLK_mcu=U1 PA14 pin 37`；`SWDIO_mcu=U1 PA13 pin 34`
- 证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C3 的 P1 pin 1-5 与网格 C1-C2 的 U1 SWCLK/SWDIO 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 键盘面板架构 | `mcu=STM32F030C8T6`；`matrix_keys=30`；`direct_keys=5`；`total_switches=35`；`host_connector=J1 M5_BUS_22P`；`debug_connector=P1 Header 5` |
| 核心器件 | U1 主控 | `reference=U1`；`part_number=STM32F030C8T6`；`package_pin_count=48` |
| 核心器件 | 按键开关数量 | `reference_range=S1-S35`；`count=35`；`matrix_switches=30`；`direct_switches=5` |
| GPIO 与控制信号 | 30 键矩阵拓扑 | `columns=PA0, PA1, PA2, PA3, PA4, PA5, PA6, PA7, PA8, PA9`；`rows=PB0, PB1, PB2`；`column_count=10`；`row_count=3` |
| GPIO 与控制信号 | PB0 矩阵行 | `mcu_net=PB0`；`mcu_pin=18`；`switches=S1, S2, S3, S4, S5, S6, S7, S8, S9, S10`；`legends=Q, W, E, R, T, Y, U, I, O, P` |
| GPIO 与控制信号 | PB1 矩阵行 | `mcu_net=PB1`；`mcu_pin=19`；`switches=S11, S12, S13, S14, S15, S16, S17, S18, S19, S20`；`legends=A, S, D, F, G, H, J, K, L, del` |
| GPIO 与控制信号 | PB2 矩阵行 | `mcu_net=PB2`；`mcu_pin=20`；`switches=S32, S22, S23, S24, S25, S26, S27, S28, S29, S33`；`legends=0, Z, X, C, V, B, N, M, $, SPACE` |
| GPIO 与控制信号 | 矩阵列与开关位号映射 | `PA9=S1, S11, S32`；`PA8=S2, S12, S22`；`PA7=S3, S13, S23`；`PA6=S4, S14, S24`；`PA5=S5, S15, S25`；`PA4=S6, S16, S26`；`PA3=S7, S17, S27`；`PA2=S8, S18, S28`；`PA1=S9, S19, S29`；`PA0=S10, S20, S33` |
| GPIO 与控制信号 | 五个独立功能键 | `S31_aA=PC13, U1 pin 2`；`S21_alt=PC14, U1 pin 3`；`S30_ok=PC15, U1 pin 4`；`S34_sym=PF0, U1 pin 5`；`S35_Fn=PF1, U1 pin 6`；`common=GND` |
| 时钟 | 振荡器复用引脚 | `PC14_OSC32_IN=S21 alt`；`PC15_OSC32_OUT=S30 ok`；`PF0_OSC_IN=S34 sym`；`PF1_OSC_OUT=S35 Fn`；`external_crystal_shown=false` |
| GPIO 与控制信号 | LED1 驱动 | `mcu_net=PB4`；`mcu_pin=40`；`series_resistor=R1 2k_0603`；`led_positive_terminal=0`；`led_negative_terminal=1`；`return=GND` |
| GPIO 与控制信号 | LED2 驱动 | `mcu_net=PB5`；`mcu_pin=41`；`series_resistor=R2 2k_0603`；`led_positive_terminal=0`；`led_negative_terminal=1`；`return=GND` |
| 总线 | U1 I2C 网络 | `SCL=U1 PB10 pin 21 to J1 pin 17`；`SDA=U1 PB11 pin 22 to J1 pin 15`；`connector=J1 M5_BUS_22P` |
| 电源 | J1 面板供电 | `supply_pin=J1 pin 3`；`supply_net=3V3`；`ground_pin=J1 pin 2`；`five_volt_pin=J1 pin 1, no connected net shown` |
| 接口 | J1 已连接信号 | `J1_pin_4=symbol label AD35, net G35`；`J1_pin_15=SDA`；`J1_pin_17=SCL` |
| 接口 | J1 未接入面板的针脚 | `pins=1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22`；`symbol_labels=5V, MOSI, AD36, MISO, DA25, SCK, DA26, R2/16, SK, T2/17, WS, OUT, MK, G2, IN, G5, HRR` |
| 关键网络 | G35 网络 | `mcu_pin=U1 PA15 pin 38`；`connector_pin=J1 pin 4 AD35`；`pullup=R3 10k_0603 to 3V3`；`net=G35` |
| 总线 | I2C 可选上拉位 | `SCL_pullup=R6 NC_0603 to 3V3`；`SDA_pullup=R7 NC_0603 to 3V3`；`assembly_mark=NC` |
| 调试与烧录 | P1 SWD 调试接口 | `pin_1=3V3`；`pin_2=SWCLK`；`pin_3=SWDIO`；`pin_4=NRST`；`pin_5=GND`；`SWCLK_mcu=U1 PA14 pin 37`；`SWDIO_mcu=U1 PA13 pin 34` |
| 电源 | U1 电源引脚 | `positive_pins=VDD 1, VDD 24, VDD 48, VDDA 9`；`positive_net=3V3`；`ground_pins=VSS 23, VSS 47, VSSA 8`；`ground_net=GND` |
| 电源 | U1 电源去耦 | `capacitors=C1, C2, C3`；`value_each=100nF`；`rail=3V3`；`return=GND` |
| 复位 | NRST 复位网络 | `mcu_pin=U1 NRST pin 7`；`pullup=R5 10k_0603 to 3V3`；`capacitor=C4 100nF to GND`；`debug_pin=P1 pin 4` |
| 复位 | BOOT0 配置 | `mcu_pin=U1 BOOT0 pin 44`；`pulldown=R4 10k_0603`；`net=GND` |
| GPIO 与控制信号 | U1 未连接引脚 | `explicit_no_connect=PA10 pin 31, PA11 pin 32, PA12 pin 33`；`no_external_net_shown=PB3 pin 39, PB6 pin 42, PB7 pin 43, PB8 pin 45, PB9 pin 46, PB12 pin 25, PB13 pin 26, PB14 pin 27, PB15 pin 28, PF6 pin 35, PF7 pin 36` |
| 总线地址 | I2C 从地址 0x08 | `claimed_address=0x08`；`claim_source=zh_CN/faces/Faces_Keyboard3.md 规格参数`；`schematic_address_label=null` |
| 接口 | G35 主机中断语义 | `claimed_role=host interrupt`；`schematic_net=G35`；`mcu_endpoint=U1 PA15 pin 38`；`host_endpoint=J1 pin 4 AD35` |
| 接口 | 源文档与 J1 针脚编号视角 | `source_table=GND at 1, INT at 3, 3V3 at 4`；`schematic_j1=GND pin 2, G35/AD35 pin 4, 3V3 pin 3`；`review_scope=connector orientation and numbering convention` |
| 核心器件 | LED1 与 LED2 的颜色 | `claimed_color=blue`；`references=LED1, LED2`；`schematic_part_number=null` |
| 电源 | 面板待机功耗 | `claimed_voltage=3.3V`；`claimed_current=5.51mA`；`claim_source=zh_CN/faces/Faces_Keyboard3.md 规格参数` |

## 待确认事项

- `address.i2c-0x08`：源文档规格表声明 I2C 通信地址为 0x08，但当前原理图页只标出 SDA、SCL 网络，未标注从地址或地址配置电路。（证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A4/C2，仅可见 J1 与 U1 的 SDA/SCL 连接，无 0x08 标注）
- `interface.g35-interrupt-role`：源文档描述面板通过中断引脚与主机交互；原理图仅确认 G35 从 U1 PA15 连接到 J1 AD35 并经 R3 上拉，没有把该网络直接标为 INT。（证据：图 532f534f75ac / 第 1 页 / 页 1 网格 C1-C2/A4，G35 网络标注为 G35 与 AD35，未出现 INT 网络名）
- `interface.source-pin-map-numbering`：源文档 Faces Panel Bus 表把 GND、INT、3V3 放在表中 1、3、4 位置，而原理图 J1 显示 GND=pin 2、G35/AD35=pin 4、3V3=pin 3；两者的编号视角或映射关系尚未由当前页面解释。（证据：图 532f534f75ac / 第 1 页 / 页 1 网格 A4，J1 M5_BUS_22P 的 pin 2 GND、pin 3 3V3、pin 4 AD35/G35）
- `component.led-color`：源文档把两路输入状态指示灯声明为蓝色，原理图只标注 LED1、LED2 及极性，没有颜色或具体料号。（证据：图 532f534f75ac / 第 1 页 / 页 1 网格 B3，LED1 与 LED2 符号仅显示正负端和位号）
- `power.standby-current`：源文档规格表声明面板待机功耗为 3.3V@5.51mA，原理图没有测量条件、电流标注或功耗测试电路，无法由图面确认该数值。（证据：图 532f534f75ac / 第 1 页 / 页 1 全页，只有 3V3 电源网络与负载电路，没有 5.51mA 或测量条件标注）
- `review.i2c-address`：请用当前固件协议、网表或地址配置资料确认 7-bit I2C 地址是否为 0x08。；原因：0x08 只出现在源文档规格表，原理图没有地址标注或硬件地址配置。
- `review.g35-interrupt-role`：请用固件或接口协议确认 G35 是否为主机中断，以及有效电平和时序。；原因：原理图确认物理连接和上拉，但没有 INT 标签或方向、极性、时序说明。
- `review.source-pin-map-numbering`：请核对 Faces Panel Bus 表的观察方向与 J1 原理图针脚编号，确认文档中的 GND、INT、3V3 映射。；原因：源文档表格与 J1 符号显示的编号不一致，当前资料未说明连接器视角转换。
- `review.led-color`：请用 BOM、装配图或当前物料确认 LED1、LED2 的颜色和具体料号。；原因：蓝色来自源文档，原理图没有颜色代码或 LED 料号。
- `review.standby-current`：请提供测试条件或当前硬件测量结果以确认 3.3V@5.51mA 待机功耗。；原因：原理图不能证明工作模式、固件状态和实测电流。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `532f534f75ac1880cbf3c92234036971e884e1ed2682c0765916c09138897d86` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_page_01.png` |

---

源文档：`zh_CN/faces/Faces_Keyboard3.md`

源文档 SHA-256：`a6d425243d2616503f9946873ca2f8e7e600509497f3cf3b53c906b16b2bf380`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
