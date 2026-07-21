# Chain DualKey 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain DualKey |
| SKU | C147 |
| 产品 ID | `chain-dualkey-38acc9b60721` |
| 源文档 | `zh_CN/chain/Chain_DualKey.md` |

## 概述

Chain DualKey 以 U6 ESP32-S3FN8 为主控，使用 40MHz 主晶振和 32.768kHz RTC 晶振，GPIO19/GPIO20 直连 USB-C D-/D+，GPIO47/GPIO48 与 GPIO6/GPIO5 分别形成两路 Chain UART。电源由 USB VBUS 和电池经 AO3401A 路径汇入 VIN，U29 WL9005S5-33 生成 MCU_3V3；U5 TP4057 负责 VBAT 充电，U20 SY7088DGC 将 VBAT 升压到 VOUT。SW3/SW4 是两路低有效按键，Q27 驱动两颗 WS2812B-2020 的电源和数据，SW5 与分压网络提供 SWITCH_1/SWITCH_2 状态。原理图框图写 3.7V 200mAh，而正文写 350mAh，电池容量必须按版本/BOM 复核。

## 检索关键词

`Chain DualKey`、`C147`、`ESP32-S3FN8`、`TP4057`、`WL9005S5-33`、`SY7088DGC`、`WS2812B-2020`、`AO3401A`、`BSS84DW-7-F`、`CJ3439KDW`、`USB-C`、`USB_DN`、`USB_DP`、`GPIO19`、`GPIO20`、`KEY_1`、`KEY_2`、`GPIO0`、`GPIO17`、`SWITCH_1`、`SWITCH_2`、`GPIO8`、`GPIO7`、`ADC_BAT`、`ADC_VBUS`、`ADC_CHRG`、`GPIO10`、`GPIO2`、`GPIO9`、`WS2812_IN`、`PWR_2812`、`GPIO21`、`GPIO40`、`UART1_TX`、`UART1_RX`、`UART2_TX`、`UART2_RX`、`VOUT`、`VBAT`、`MCU_3V3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | ESP32-S3FN8 | 主控制器，连接 USB、按键、开关 ADC、RGB LED、两路 UART、调试、时钟和射频网络 | 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页中央 U6 ESP32-S3FN8，GPIO0-GPIO48、USB、UART、时钟、SPI/射频和电源引脚 |
| U25 | USB Type-C receptacle | VBUS 电源与 USB_DN/USB_DP 数据接口，CC1/CC2 配置为受电设备 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页上中 Type-C 区域 U25，A/B 排 VBUS、DP/DN、CC1/CC2、GND/EP |
| U29 | WL9005S5-33 | 由 VIN 生成 MCU_3V3 的 3.3V LDO，EN 由 PWR_EN 控制 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页左中 LDO 区 U29 WL9005S5-33，VIN/GND/EN/VOUT |
| U5 | TP4057 | VBUS 输入的单节电池充电器，连接 VBAT、CHRG#、STDBY# 和 PROG | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页左下 Charge 区 U5 TP4057，CHRG#/BAT/PROG/STDBY#/VCC/GND |
| U20 | SY7088DGC | 将 VBAT 升压为 VOUT 的开关转换器 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页右下 Boost 区 U20 SY7088DGC，LX/EN/IN/OUT/FB 与 U21 1.5uH |
| Q1,Q25 | AO3401A | VBAT/VBUS/VIN/VOUT 电源路径的 P 沟道 MOSFET | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 LDO 区 Q1 与右上电源切换区 Q25，均标 AO3401A |
| Q26 | BSS84DW-7-F | 与 S1/D1/D2/G1/G2 网络连接的双 P 沟道开关器件 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页右上 Q26 BSS84DW-7-F 双 MOSFET，S1/D1/D2/G1/G2 |
| Q27 | CJ3439KDW | 分别控制 PWR_2812 电源和 WS2812_IN 数据电平的双 MOSFET | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页右中 LED 区 Q27.1/Q27.2 CJ3439KDW |
| LED1,LED2 | WS2812B-2020 | 两颗串联数据链的可编程 RGB LED | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页右中 LED1/LED2 WS2812B-2020，LED1 DO 接 LED2 DI |
| SW3,SW4 | CPG151101S13 | KEY_2 与 KEY_1 的两颗按键开关 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页中部 Key 区 SW3/SW4 CPG151101S13 与 KEY_2/KEY_1 |
| SW5 | K3-1311S-F1 | 生成 SWITCH_1/SWITCH_2 和 PWR_EN 状态的三挡滑动开关 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页左下 Switch 区 SW5 K3-1311S-F1、D2/D3、SWITCH_1/SWITCH_2/PWR_EN |
| H2 | PZ254V-11-02P | VBAT/GND 两针电池连接器 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页左上 Battery 区 H2 PZ254V-11-02P pin2 VBAT、pin1 GND |
| U27,U28 | WAFER-PH2.0-4PZZ | 两组 Chain UART 扩展接口，分别引出 UART1 与 UART2、VOUT 和 GND | 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页左下 U27/U28 WAFER-PH2.0-4PZZ |
| H1 | PZ254V-11-06P | GND、GPIO0、CHIP_PU、U0RXD/U0TXD、MCU_3V3 调试接口 | 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页左中 DEBUG 区 H1 PZ254V-11-06P pin1-pin6 |
| X1 | 40MHz | ESP32-S3 XTAL_P/XTAL_N 主晶振 | 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页右上 X1 40MHz、C17/C18 12pF 与 L6 10nH |
| X3 | 32.768kHz | ESP32-S3 XTAL_32K_P/XTAL_32K_N 低速晶振 | 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页中央 X3 32.768kHz、C29/C90 与 R114 |
| D1,D2,D3 | 1N5819WS | USB/VIN 和三挡开关 PWR_EN 路径的肖特基二极管 | 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页右上 D1 及左下 Switch 区 D2/D3，均标 1N5819WS |

## 系统结构

### Chain DualKey 系统架构

USB-C 提供 VBUS 和 D+/D-，电池与 USB 电源经切换后由 U29 生成 MCU_3V3；U6 ESP32-S3FN8 连接双按键、双 WS2812B、三挡开关 ADC、两路 Chain UART、调试和射频/时钟网络。U5 TP4057 连接 VBUS/VBAT，U20 SY7088DGC 将 VBAT 升压为 VOUT。

- 参数与网络：`mcu=U6 ESP32-S3FN8`；`usb=U25 USB-C`；`ldo=U29 WL9005S5-33`；`charger=U5 TP4057`；`boost=U20 SY7088DGC`；`keys=SW3/SW4`；`rgb=LED1/LED2`；`chain_ports=U27/U28`
- 证据：图 33f2d99c40de / 第 1 页 / 第 1 张第 1 页 Overview 系统框图; 图 602669f0d683 / 第 1 页 / 第 2 张第 1 页完整 Power 页; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页完整 MCU 页

## 核心器件

### U6 ESP32-S3FN8 已使用 GPIO

U6 使用 GPIO0/GPIO17 作为 KEY_1/KEY_2，GPIO8/GPIO7 作为 SWITCH_1/SWITCH_2，GPIO10/GPIO2/GPIO9 作为 ADC_BAT/ADC_VBUS/ADC_CHRG，GPIO21/GPIO40 作为 WS2812_IN/PWR_2812，GPIO19/GPIO20 作为 USB_DN/USB_DP。

- 参数与网络：`keys=GPIO0 KEY_1, GPIO17 KEY_2`；`switch=GPIO8 SWITCH_1, GPIO7 SWITCH_2`；`adc=GPIO10 ADC_BAT, GPIO2 ADC_VBUS, GPIO9 ADC_CHRG`；`rgb=GPIO21 WS2812_IN, GPIO40 PWR_2812`；`usb=GPIO19 USB_DN, GPIO20 USB_DP`
- 证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页左侧 KEY/ADC/USB 网络与中央 U6 同名 GPIO

## 电源

### USB 与电池到 VIN 的电源汇入

VBUS 直接连接 VIN 节点并通过 R4 1MΩ 控制 Q1 AO3401A；VBAT 经 Q1 接入 VIN。VIN 通过 D1 1N5819WS 连接 VBUS，并参与 Q25/Q26/S1 的 VOUT/G1/G2 电源切换网络。

- 参数与网络：`battery_path=VBAT -> Q1 AO3401A -> VIN`；`usb_path=VBUS -> VIN node`；`gate_bias=VBUS -> R4 1MΩ -> Q1 gate`；`diode=VIN -> D1 1N5819WS -> VBUS`；`switch_network=Q25/Q26/S1/G1/G2`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 LDO 区 Q1/VBAT/VBUS/VIN 与右上 D1/Q25/Q26

### VIN 到 MCU_3V3

U29 WL9005S5-33 的 VIN pin1 接 VIN，VOUT pin5 输出 MCU_3V3，EN pin3 接 PWR_EN 并由 R5 1MΩ 下拉；C4 1uF/C5 10uF 为输入电容，C6 10uF/C7 1uF 为输出电容。

- 参数与网络：`input=VIN`；`regulator=U29 WL9005S5-33`；`output=MCU_3V3`；`enable=PWR_EN`；`enable_pulldown=R5 1MΩ`；`input_caps=C4 1uF,C5 10uF`；`output_caps=C6 10uF,C7 1uF`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 LDO 区 U29、C4-C7、PWR_EN/MCU_3V3

### TP4057 充电路径

U5 TP4057 VCC pin4 接 VBUS、BAT pin3 接 VBAT、GND pin2 接 GND；PROG pin6 经 R6 5.1KΩ 接 GND，CHRG# pin1 输出 CHRG，STDBY# pin5 输出 STDBY，C8/C9 各 10uF 对地。

- 参数与网络：`input=VBUS`；`battery=VBAT`；`program_resistor=R6 5.1KΩ`；`status=CHRG#,STDBY#`；`caps=C8/C9 10uF`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Charge 区 U5 TP4057、R6、C8/C9

### VBAT 到 VOUT 升压

VBAT 经 U21 1.5uH 接 U20 SY7088DGC LX，U20 OUT pins7/8 输出 VOUT；FB pin5 使用 R87 220KΩ 与 R88 68KΩ，C85 100nF/C86 22uF 对地，VOUT_EN 控制 EN pin3。

- 参数与网络：`input=VBAT`；`inductor=U21 1.5uH`；`converter=U20 SY7088DGC`；`output=VOUT`；`feedback=R87 220KΩ,R88 68KΩ`；`output_caps=C85 100nF,C86 22uF`；`enable=VOUT_EN`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Boost 区 VBAT/U21/U20/R87/R88/C85/C86/VOUT

## 总线

### ESP32-S3 原生 USB

U25 的 A6/B6 DP1/DP2 汇合为 USB_DP 并连接 U6 GPIO20，A7/B7 DN1/DN2 汇合为 USB_DN 并连接 U6 GPIO19；VBUS 独立进入电源与检测网络。

- 参数与网络：`controller=U6 ESP32-S3FN8`；`dp=U25 A6/B6 -> USB_DP -> GPIO20`；`dn=U25 A7/B7 -> USB_DN -> GPIO19`；`power=VBUS`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Type-C 区 U25 DP1/DP2/DN1/DN2; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 USB 区 GPIO19/GPIO20

### 两路 Chain UART

UART1_TX 由 GPIO47 输出到 U27 pin1，UART1_RX 由 U27 pin2 经 R63 499Ω 到 GPIO48；UART2_TX 由 GPIO6 经 R64 499Ω 到 U28 pin2，UART2_RX 由 U28 pin1 接 GPIO5。U27/U28 pin3 均为 VOUT、pin4 均为 GND。

- 参数与网络：`uart1=GPIO47 TX -> U27 pin1; U27 pin2 RX -> R63 499Ω -> GPIO48`；`uart2=GPIO6 -> R64 499Ω -> U28 pin2 TX; U28 pin1 RX -> GPIO5`；`power=pin3 VOUT, pin4 GND`；`logic_level=MCU GPIO domain`
- 证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页左侧 UART 网络、R63/R64 与 U27/U28

## GPIO 与控制信号

### 双按键输入

SW4 KEY_1 连接 GPIO0，SW3 KEY_2 连接 GPIO17；两路均由 R118/R117 10KΩ 上拉到 MCU_3V3，按下开关时接 GND。

- 参数与网络：`key1=SW4 KEY_1 -> GPIO0`；`key2=SW3 KEY_2 -> GPIO17`；`pullups=R118/R117 10KΩ to MCU_3V3`；`active_level=low`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Key 区 SW3/SW4 与 R117/R118; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 KEY 区 GPIO0/GPIO17

### SW5 三挡开关与关断控制

SW5 K3-1311S-F1 通过 D2/D3 1N5819WS 连接 VIN/PWR_EN，并通过 R59/R60、R57/R58 各 510KΩ/1MΩ 分压输出 SWITCH_1 和 SWITCH_2，分别进入 GPIO8/GPIO7。

- 参数与网络：`switch=SW5 K3-1311S-F1`；`power_control=VIN,PWR_EN through D2/D3`；`switch1=R59 510KΩ/R60 1MΩ -> GPIO8`；`switch2=R57 510KΩ/R58 1MΩ -> GPIO7`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Switch 区 SW5、D2/D3、R57-R60; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 ADC 区 GPIO8/GPIO7

### 双 WS2812 电源与数据控制

GPIO40 的 PWR_2812 经 R8 10KΩ 控制 Q27.2，为 LED1/LED2 的 VDD 电源链路开关；GPIO21 的 WS2812_IN 经 Q27.1 电平网络送入 LED1 DI，LED1 DO 接 LED2 DI，LED2 DO 未继续连接。

- 参数与网络：`power_enable=GPIO40 PWR_2812 -> R8 -> Q27.2`；`data=GPIO21 WS2812_IN -> Q27.1 -> LED1 DI`；`chain=LED1 DO -> LED2 DI`；`last_output=LED2 DO NC`；`led_part=WS2812B-2020`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 LED 区 Q27.1/Q27.2、LED1/LED2; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 GPIO21 WS2812_IN 与 GPIO40 PWR_2812

## 时钟

### ESP32-S3 主时钟与 RTC 时钟

U6 XTAL_P/XTAL_N 连接 X1 40MHz，配合 L6 10nH 与 C17/C18 各 12pF；XTAL_32K_P/XTAL_32K_N 连接 X3 32.768kHz，C29/C90 标 22pF，其中 R114 标 NC。

- 参数与网络：`main=X1 40MHz, L6 10nH, C17/C18 12pF`；`rtc=X3 32.768kHz, C29/C90 22pF`；`rtc_resistor=R114 NC`
- 证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 U6 上方 X1 主晶振和左侧 X3 RTC 晶振

## 保护电路

### USB-C 配置与保护

U25 CC1/CC2 分别通过 R56/R55 5.1KΩ 接 GND；D7/D8/D5 连接相关 USB-C 侧网络到 GND，构成接口钳位保护。

- 参数与网络：`cc1=R56 5.1KΩ to GND`；`cc2=R55 5.1KΩ to GND`；`protectors=D7,D8,D5 to GND`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Type-C 区 U25 CC1/CC2、R56/R55 与 D7/D8/D5

## 射频

### ESP32-S3 射频匹配网络

U6 LNA_IN 通过 L7 2nH 接 MCU_3V3 去耦侧，并通过页底 L4 2.4nH、L5 2nH、C23 1.8pF、C24 2pF 及 C26/C27 NC 构成射频网络；资源未给出天线位号或天线接口。

- 参数与网络：`mcu_pin=LNA_IN`；`series_inductors=L4 2.4nH,L5 2nH`；`shunt_caps=C23 1.8pF,C24 2pF`；`optional_caps=C26/C27 NC`；`antenna_reference=null`
- 证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 U6 LNA_IN 与页底 L4/L5/C23/C24/C26/C27

## 调试与烧录

### H1 调试下载接口

H1 PZ254V-11-06P 的 pin1=GND、pin2=GPIO0、pin3=CHIP_PU、pin4=U0RXD、pin5=U0TXD、pin6=MCU_3V3；CHIP_PU 由 R15 10KΩ 上拉并由 C25 1uF 对地。

- 参数与网络：`header=H1`；`pinout=1 GND,2 GPIO0,3 CHIP_PU,4 U0RXD,5 U0TXD,6 MCU_3V3`；`chip_pu=R15 10KΩ,C25 1uF`
- 证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 DEBUG 区 H1 与中央 CHIP_PU R15/C25

## 模拟电路

### ADC_CHRG 状态采样

ADC_CHRG 节点通过 R9 100KΩ 接 MCU_3V3、R10 200KΩ 接 STDBY、R11 100KΩ 接 CHRG，并由 C10 100nF 对地；图中注释标出无充电约 3.3V、有线充电约 1.65V、无线充电约 2.2V。

- 参数与网络：`host_gpio=GPIO9 ADC_CHRG`；`pullup=R9 100KΩ MCU_3V3`；`standby=R10 200KΩ STDBY`；`charge=R11 100KΩ CHRG`；`filter=C10 100nF`；`schematic_notes=no charge 3.3V, wired charge 1.65V, wireless charge 2.2V`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 Charge 区 ADC_CHRG、R9-R11/C10 与三行电压注释

### 电池与 VBUS ADC

VBAT 经 R61 510KΩ/R62 1MΩ 分压形成 ADC_BAT，并由 C28 100nF 对地；图中给出 Vadv_bat=Vbat*0.662、Vbat=Vadv_bat*1.51。ADC_VBUS 由 VBUS 经 R119 51KΩ/R120 100KΩ 分压。

- 参数与网络：`adc_bat_gpio=GPIO10`；`battery_divider=R61 510KΩ,R62 1MΩ,C28 100nF`；`battery_formula=Vadv_bat=Vbat*0.662; Vbat=Vadv_bat*1.51`；`adc_vbus_gpio=GPIO2`；`vbus_divider=R119 51KΩ,R120 100KΩ`
- 证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页左上 Battery ADC 与右上 ADC_VBUS 分压

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain DualKey 系统架构 | `mcu=U6 ESP32-S3FN8`；`usb=U25 USB-C`；`ldo=U29 WL9005S5-33`；`charger=U5 TP4057`；`boost=U20 SY7088DGC`；`keys=SW3/SW4`；`rgb=LED1/LED2`；`chain_ports=U27/U28` |
| 核心器件 | U6 ESP32-S3FN8 已使用 GPIO | `keys=GPIO0 KEY_1, GPIO17 KEY_2`；`switch=GPIO8 SWITCH_1, GPIO7 SWITCH_2`；`adc=GPIO10 ADC_BAT, GPIO2 ADC_VBUS, GPIO9 ADC_CHRG`；`rgb=GPIO21 WS2812_IN, GPIO40 PWR_2812`；`usb=GPIO19 USB_DN, GPIO20 USB_DP` |
| 总线 | ESP32-S3 原生 USB | `controller=U6 ESP32-S3FN8`；`dp=U25 A6/B6 -> USB_DP -> GPIO20`；`dn=U25 A7/B7 -> USB_DN -> GPIO19`；`power=VBUS` |
| 保护电路 | USB-C 配置与保护 | `cc1=R56 5.1KΩ to GND`；`cc2=R55 5.1KΩ to GND`；`protectors=D7,D8,D5 to GND` |
| 电源 | USB 与电池到 VIN 的电源汇入 | `battery_path=VBAT -> Q1 AO3401A -> VIN`；`usb_path=VBUS -> VIN node`；`gate_bias=VBUS -> R4 1MΩ -> Q1 gate`；`diode=VIN -> D1 1N5819WS -> VBUS`；`switch_network=Q25/Q26/S1/G1/G2` |
| 电源 | VIN 到 MCU_3V3 | `input=VIN`；`regulator=U29 WL9005S5-33`；`output=MCU_3V3`；`enable=PWR_EN`；`enable_pulldown=R5 1MΩ`；`input_caps=C4 1uF,C5 10uF`；`output_caps=C6 10uF,C7 1uF` |
| 电源 | TP4057 充电路径 | `input=VBUS`；`battery=VBAT`；`program_resistor=R6 5.1KΩ`；`status=CHRG#,STDBY#`；`caps=C8/C9 10uF` |
| 模拟电路 | ADC_CHRG 状态采样 | `host_gpio=GPIO9 ADC_CHRG`；`pullup=R9 100KΩ MCU_3V3`；`standby=R10 200KΩ STDBY`；`charge=R11 100KΩ CHRG`；`filter=C10 100nF`；`schematic_notes=no charge 3.3V, wired charge 1.65V, wireless charge 2.2V` |
| 电源 | VBAT 到 VOUT 升压 | `input=VBAT`；`inductor=U21 1.5uH`；`converter=U20 SY7088DGC`；`output=VOUT`；`feedback=R87 220KΩ,R88 68KΩ`；`output_caps=C85 100nF,C86 22uF`；`enable=VOUT_EN` |
| 模拟电路 | 电池与 VBUS ADC | `adc_bat_gpio=GPIO10`；`battery_divider=R61 510KΩ,R62 1MΩ,C28 100nF`；`battery_formula=Vadv_bat=Vbat*0.662; Vbat=Vadv_bat*1.51`；`adc_vbus_gpio=GPIO2`；`vbus_divider=R119 51KΩ,R120 100KΩ` |
| GPIO 与控制信号 | 双按键输入 | `key1=SW4 KEY_1 -> GPIO0`；`key2=SW3 KEY_2 -> GPIO17`；`pullups=R118/R117 10KΩ to MCU_3V3`；`active_level=low` |
| GPIO 与控制信号 | SW5 三挡开关与关断控制 | `switch=SW5 K3-1311S-F1`；`power_control=VIN,PWR_EN through D2/D3`；`switch1=R59 510KΩ/R60 1MΩ -> GPIO8`；`switch2=R57 510KΩ/R58 1MΩ -> GPIO7` |
| GPIO 与控制信号 | 双 WS2812 电源与数据控制 | `power_enable=GPIO40 PWR_2812 -> R8 -> Q27.2`；`data=GPIO21 WS2812_IN -> Q27.1 -> LED1 DI`；`chain=LED1 DO -> LED2 DI`；`last_output=LED2 DO NC`；`led_part=WS2812B-2020` |
| 总线 | 两路 Chain UART | `uart1=GPIO47 TX -> U27 pin1; U27 pin2 RX -> R63 499Ω -> GPIO48`；`uart2=GPIO6 -> R64 499Ω -> U28 pin2 TX; U28 pin1 RX -> GPIO5`；`power=pin3 VOUT, pin4 GND`；`logic_level=MCU GPIO domain` |
| 调试与烧录 | H1 调试下载接口 | `header=H1`；`pinout=1 GND,2 GPIO0,3 CHIP_PU,4 U0RXD,5 U0TXD,6 MCU_3V3`；`chip_pu=R15 10KΩ,C25 1uF` |
| 时钟 | ESP32-S3 主时钟与 RTC 时钟 | `main=X1 40MHz, L6 10nH, C17/C18 12pF`；`rtc=X3 32.768kHz, C29/C90 22pF`；`rtc_resistor=R114 NC` |
| 射频 | ESP32-S3 射频匹配网络 | `mcu_pin=LNA_IN`；`series_inductors=L4 2.4nH,L5 2nH`；`shunt_caps=C23 1.8pF,C24 2pF`；`optional_caps=C26/C27 NC`；`antenna_reference=null` |
| 内存与 Flash | ESP32-S3FN8 集成 Flash 容量 | `mcu=ESP32-S3FN8`；`documented_flash=8MB`；`external_flash=null`；`schematic_note=SPICS1 and IO33-IO37 connect to OSPI PSRAM and are not available for other use` |
| 电源 | 电池容量版本冲突 | `schematic_overview=3.7V 200mAh`；`product_document=350mAh`；`battery_connector=H2`；`resolved_capacity=null` |
| 电源 | 充电、升压与低功耗性能 | `charger=TP4057 with R6 5.1KΩ`；`boost=SY7088DGC with R87/R88`；`charge_current=null`；`termination_voltage=null`；`vout_current=null`；`efficiency=null`；`measured_currents=null` |
| 射频 | Wi-Fi/BLE 天线实现与性能 | `radio=ESP32-S3FN8`；`matching=L4/L5/C23/C24`；`antenna=null`；`connector=null`；`test_point=null`；`rf_performance=null` |
| 其他事实 | 正文中的 USB/BLE HID 与 Web 配置功能 | `documented_features=USB HID,BLE HID,AP,Web configuration,macro keyboard`；`firmware_version=null`；`usb_stack=null`；`ble_profile=null` |

## 待确认事项

- `memory.documented-integrated-flash`：原理图明确标 U6 为 ESP32-S3FN8，正文写 8MB Flash；图中没有独立 Flash 器件或容量字段，且仅注释 SPICS1/IO33-IO37 连接 OSPI PSRAM 并不可作其他用途。（证据：图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 U6 型号与下方 OSPI PSRAM 注释）
- `power.battery-capacity-conflict`：第 1 页 Overview 框图标注 Battery 3.7V 200mAh，而产品正文标注 350mAh 锂电池；两处容量不一致，当前量产电池容量无法确定。（证据：图 33f2d99c40de / 第 1 页 / 第 1 张第 1 页 Overview 中 Battery 3.7V 200mAh 方框）
- `power.electrical-performance`：原理图给出 TP4057、SY7088DGC、反馈/设定电阻和电源路径，但未标注量产充电电流、终止电压、VOUT 额定电流、转换效率、温升或正文所列待机/深睡/USB 电流的测试条件。（证据：图 602669f0d683 / 第 1 页 / 第 2 张第 1 页 TP4057 Charge 与 SY7088DGC Boost 电路）
- `rf.antenna-implementation`：Overview 以 Wi-Fi 图标表示无线连接，MCU 页只画出 LNA_IN 匹配网络，没有天线位号、PCB 天线形状、连接器、射频测试点或 2.4GHz 性能参数，因此天线实现与认证状态无法确认。（证据：图 33f2d99c40de / 第 1 页 / 第 1 张第 1 页 Overview ESP32-S3FN8 上方 Wi-Fi 图标; 图 68d899624de7 / 第 1 页 / 第 3 张第 1 页 LNA_IN 匹配网络，图中无天线位号）
- `other.documented-firmware-features`：正文描述 USB/BLE HID、AP 热点、Web 配置和宏键盘固件；原理图只确认 ESP32-S3、USB、按键、RGB 和无线射频硬件连接，不能证明具体固件版本、协议行为或功能映射。（证据：图 33f2d99c40de / 第 1 页 / 第 1 张第 1 页 Overview 仅显示 USB/Wi-Fi/KEY/WS2812/UART 功能框）
- `review.flash-capacity`：请用 ESP32-S3FN8 料号定义或实机读取确认 C147 的集成 Flash 容量是否为 8MB，并澄清图中 OSPI PSRAM 注释。；原因：容量来自正文和型号后缀，原理图没有独立容量字段，且 PSRAM 注释需结合芯片版本解释。
- `review.battery-capacity`：C147 当前量产 BOM 的电池是 3.7V 200mAh 还是 350mAh？；原因：Overview 原理图与产品正文容量直接冲突。
- `review.power-performance`：TP4057 充电电流/终止条件、SY7088DGC VOUT 电压与额定电流、转换效率和各低功耗电流的测试条件是什么？；原因：原理图连接不足以证明整机性能与热边界。
- `review.rf-antenna`：C147 使用何种 PCB 天线或外部天线，匹配值、辐射性能和认证测试结果是什么？；原因：资源只有 LNA_IN 匹配网络，没有天线本体或射频指标。
- `review.firmware-features`：C147 当前出厂固件版本实际支持哪些 USB/BLE HID、AP/Web 配置和宏键盘功能？；原因：软件功能不能由原理图独立验证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `33f2d99c40de8917f12e3c22e454daaf079fc76ed91f7eb3ef5e613cb61bcb1e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_01.png` |
| 2 | 1 | `602669f0d68313d37ad6de060fc6b1dafb9a35dfc885114668f1bf5c2c3f7255` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_02.png` |
| 3 | 1 | `68d899624de7431af7fb9a7cfe0fd50e4dd530000de8c8e146f6d70e54f6294a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_03.png` |

---

源文档：`zh_CN/chain/Chain_DualKey.md`

源文档 SHA-256：`d813d86181395d7b2ed5392395f106dafdd0eff59f14f80a13d4a51ec4a26279`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
