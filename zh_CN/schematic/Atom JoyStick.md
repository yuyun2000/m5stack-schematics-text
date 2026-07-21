# Atom JoyStick 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom JoyStick |
| SKU | K137 |
| 产品 ID | `atom-joystick-edbf9d8d61f7` |
| 源文档 | `zh_CN/app/Atom JoyStick.md` |

## 概述

Atom JoyStick 以 STM32F030F4P6（U1）为协处理器，采集 J1/J2 两只 JH16 摇杆、S2/S3 功能按键和两路电池分压，并通过 SCL/SDA 与外部 Atom 主控连接。LED1/LED2 两颗 WS2812C 构成串行 RGB 链，P1 还引出 BEEP 控制到独立蜂鸣器驱动。USB Type-C 输入分别供给 U3/U4 两颗 TP4067-4.35V 充电器，BAT_IN1/BAT_IN2 经 B5819W 肖特基或接后由 SY7088（U2）升压生成 +5VIN。

## 检索关键词

`Atom JoyStick`、`K137`、`STM32F030F4P6`、`TP4067-4.35V`、`SY7088`、`JH16`、`WS2812C`、`SCL`、`SDA`、`SWCLK`、`SWDIO`、`NRST`、`LEFT-SW-X`、`LEFT-SW-Y`、`LEFT-SW-B`、`RIGHT-SW-X`、`RIGHT-SW-Y`、`RIGHT-SW-B`、`LEFT-BTN`、`RIGHT-BTN`、`BAT-ADC1`、`BAT-ADC2`、`BAT_IN1`、`BAT_IN2`、`+5VIN`、`+3.3V`、`BEEP`、`RGB`、`0x59`、`SWD_5p`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 摇杆、按键和电池采样协处理器，并提供 I2C 与 SWD 接口 | 图 aa6ea9724768 / 第 1 页 / 页面下部左中 U1：STM32F030F4P6，PA0~PA14、PF0/PF1、BOOT0、NRST、SCL/SDA、SWD 引脚 |
| USB1 | TYPEC-304S-ACR16 | 5V 充电输入 Type-C 接口，CC1/CC2 通过 5.1KΩ 下拉 | 图 aa6ea9724768 / 第 1 页 / 页面左上 USB1：TYPEC-304S-ACR16，VBUS/GND 与 CC1/CC2、R10/R11 5.1KΩ |
| U2 | SY7088 | BAT_IN1/BAT_IN2 或接电源到 +5VIN 的升压转换器 | 图 aa6ea9724768 / 第 1 页 / 页面右上 U2：SY7088，D1/D4 或接输入、L1、LX/OUT/EN/FB/GND 与 D6-+5VIN 输出 |
| U3 | TP4067-4.35V | 第一路 BAT_IN1 高压锂电池充电器 | 图 aa6ea9724768 / 第 1 页 / 页面上部左中 U3：TP4067-4.35V，VCC/BAT/CHRG/STDBY/PROG/GND，BAT 输出 VBAT_IN1 |
| U4 | TP4067-4.35V | 第二路 BAT_IN2 高压锂电池充电器 | 图 aa6ea9724768 / 第 1 页 / 页面上部中央 U4：TP4067-4.35V，VCC/BAT/CHRG/STDBY/PROG/GND，BAT 输出 VBAT_IN2 |
| J1 | JH16 | 左侧三轴输出摇杆，提供 LEFT-SW-X/Y/B | 图 aa6ea9724768 / 第 1 页 / 页面中左 J1 JH16：VCC/X/Y/SW/GND 与 LEFT-SW-X/LEFT-SW-Y/LEFT-SW-B |
| J2 | JH16 | 右侧三轴输出摇杆，提供 RIGHT-SW-X/Y/B | 图 aa6ea9724768 / 第 1 页 / 页面中部 J2 JH16：VCC/X/Y/SW/GND 与 RIGHT-SW-X/RIGHT-SW-Y/RIGHT-SW-B |
| LED1 | WS2812C | RGB 串行链第一颗灯，DIN 接 RGB，DOUT 连接 LED2 DIN | 图 aa6ea9724768 / 第 1 页 / 页面中上 LED1 WS2812C：DI 接 RGB，DO 接 LED2 DI，+3.3V/GND 供电 |
| LED2 | WS2812C | RGB 串行链第二颗灯，DIN 接 LED1 DOUT | 图 aa6ea9724768 / 第 1 页 / 页面中上 LED2 WS2812C：DI 接 LED1 DO，+3.3V/GND 供电 |
| S2 | SW-PB | LEFT-BTN 功能按键 | 图 aa6ea9724768 / 第 1 页 / 页面中上 S2：SW-PB 从 LEFT-BTN 接 GND，R15 10KΩ 上拉，C10 100nF 对地 |
| S3 | SW-PB | RIGHT-BTN 功能按键 | 图 aa6ea9724768 / 第 1 页 / 页面中上 S3：SW-PB 从 RIGHT-BTN 接 GND，R16 10KΩ 上拉，C11 100nF 对地 |
| LS1/Q3 | Buzzer / SS8050 Y1 | BEEP 控制的蜂鸣器低侧驱动链路 | 图 aa6ea9724768 / 第 1 页 / 页面右中 LS1 Buzzer 与 Q3 SS8050 Y1：+3.3V-R14-LS1-Q3-GND，BEEP 经 R18/C12/D7 控制 |
| P3 | SWD_5p | STM32 调试与烧录接口，引出 VCC、SWCLK、SWDIO、NRST、GND | 图 aa6ea9724768 / 第 1 页 / 页面中部 P3 SWD_5p：1~5 脚为 VCC/SWCLK/SWDIO/RST/GND |
| P2 | Header 4 | 外部 Atom 主控 I2C 与电源接口 | 图 aa6ea9724768 / 第 1 页 / 页面右下 P2 Header 4：1~4 脚对应 SCL/SDA/+5VIN/GND，R1/R2 4.7KΩ 上拉 |
| P1 | Header 5 | 外部 Atom 主控蜂鸣器与 RGB 控制接口 | 图 aa6ea9724768 / 第 1 页 / 页面右下 P1 Header 5：1 脚 +3.3V、2 脚 BEEP、3 脚 RGB、4/5 脚 NC |
| P4/S1 | Header 4 / SK22D07 | 双电池连接与 BAT_IN1/BAT_IN2 开关路径 | 图 aa6ea9724768 / 第 1 页 / 页面中左 P4 Header 4 与 S1 SK22D07：VBAT_IN1/VBAT_IN2、BAT_IN1/BAT_IN2 和 GND |

## 系统结构

### Atom JoyStick

U1 STM32F030F4P6 采集两只 JH16 摇杆、LEFT-BTN/RIGHT-BTN 和 BAT-ADC1/BAT-ADC2，并通过 SCL/SDA 与 P2 外部接口连接；RGB 与 BEEP 由 P1 外部信号直接驱动对应链路。

- 参数与网络：`coprocessor=U1 STM32F030F4P6`；`left_joystick=J1 JH16`；`right_joystick=J2 JH16`；`buttons=S2 LEFT-BTN,S3 RIGHT-BTN`；`battery_adc=BAT-ADC1,BAT-ADC2`；`host_bus=SCL,SDA`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中下 U1 与 J1/J2/S2/S3/P1/P2/BAT-ADC 网络

## 电源

### U3/U4 双路充电

U3、U4 均标注 TP4067-4.35V；U3 BAT 输出 VBAT_IN1，U4 BAT 输出 VBAT_IN2，各自使用 2.4KΩ PROG 电阻和 10uF 电池端电容，并分别配置 CHRG/STDBY 指示 LED。

- 参数与网络：`charger_1=U3 TP4067-4.35V to VBAT_IN1`；`charger_2=U4 TP4067-4.35V to VBAT_IN2`；`program_resistors=R12 2.4KΩ,R13 2.4KΩ`；`battery_caps=C7 10uF,C8 10uF`；`status=CHRG,STDBY LEDs`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面上部 U3/U4：VCC/BAT/CHRG/STDBY/PROG、VBAT_IN1/VBAT_IN2、R12/R13、C7/C8

### BAT_IN1/BAT_IN2 到 +5VIN

BAT_IN1 经 D1 B5819W SL、BAT_IN2 经 D4 B5819W SL 汇合到 U2/L1 输入节点；U2 SY7088 经 L1 3015 1.5uH 升压，输出再经 D6 B5819W SL 形成 +5VIN。

- 参数与网络：`battery_1_or=D1 B5819W SL`；`battery_2_or=D4 B5819W SL`；`boost=U2 SY7088`；`inductor=L1 3015 1.5uH`；`output_diode=D6 B5819W SL`；`output=+5VIN`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面右上 BAT_IN1-D1、BAT_IN2-D4、L1/U2/D6-+5VIN 电源链

## 接口

### USB1 Type-C

USB1 的 VBUS 为双路充电电路提供输入电源，CC1 与 CC2 分别经 R10、R11 5.1KΩ 接 GND；数据引脚在本页无外接功能网络。

- 参数与网络：`power=VBUS`；`cc1=R10 5.1KΩ to GND`；`cc2=R11 5.1KΩ to GND`；`usb_data=unconnected on page`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面左上 USB1：VBUS/GND、CC1-R10、CC2-R11 及悬空 DP/DN/SBU

### P2 Header 4

P2 的 1 脚接 SCL，2 脚接 SDA，3 脚接 +5VIN，4 脚接 GND；SCL/SDA 分别经 R1/R2 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VIN`；`pin_4=GND`；`pullups=R1/R2 4.7KΩ to +3.3V`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面右下 P2、R1/R2、C1：SCL/SDA/+5VIN/GND

### P1 Header 5

P1 的 1 脚接 +3.3V，2 脚接 BEEP，3 脚接 RGB，4 脚和 5 脚标记不连接。

- 参数与网络：`pin_1=+3.3V`；`pin_2=BEEP`；`pin_3=RGB`；`pin_4=NC`；`pin_5=NC`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面右下 P1 Header 5：+3.3V/BEEP/RGB 与 4/5 脚红色 NC 标记

## 总线

### U1 SCL/SDA

U1 的 PA9 接 SCL，PA10 接 SDA，两条网络连接 P2。

- 参数与网络：`SCL=U1 PA9 to P2.1`；`SDA=U1 PA10 to P2.2`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面下部 U1 右侧 PA9/PA10 与右下 P2 的 SCL/SDA 同名网络

## GPIO 与控制信号

### J1 左摇杆

J1 的 X、Y、SW 分别形成 LEFT-SW-X、LEFT-SW-Y、LEFT-SW-B，并连接 U1 PA2、PA3、PA4。

- 参数与网络：`X=LEFT-SW-X to PA2`；`Y=LEFT-SW-Y to PA3`；`button=LEFT-SW-B to PA4`；`supply=+3.3V`；`ground=GND`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中左 J1 与下部 U1：LEFT-SW-X/Y/B 同名网络和 PA2/PA3/PA4

### J2 右摇杆

J2 的 X、Y、SW 分别形成 RIGHT-SW-X、RIGHT-SW-Y、RIGHT-SW-B，并连接 U1 PA6、PA5、PA7。

- 参数与网络：`X=RIGHT-SW-X to PA6`；`Y=RIGHT-SW-Y to PA5`；`button=RIGHT-SW-B to PA7`；`supply=+3.3V`；`ground=GND`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中部 J2 与下部 U1：RIGHT-SW-X/Y/B 同名网络和 PA6/PA5/PA7

### LEFT-BTN/RIGHT-BTN

LEFT-BTN 连接 U1 PF0/OSC_IN，RIGHT-BTN 连接 U1 PF1/OSC_OUT；两者分别由 R15/R16 10KΩ 上拉到 +3.3V，并由 S2/S3 按下接 GND。

- 参数与网络：`left=S2 LEFT-BTN to U1 PF0`；`right=S3 RIGHT-BTN to U1 PF1`；`pullups=R15/R16 10KΩ`；`filters=C10/C11 100nF`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中上 S2/S3 与下部 U1 PF0/PF1：LEFT-BTN/RIGHT-BTN 网络

### LED1/LED2 WS2812C

RGB 网络连接 LED1 DIN，LED1 DOUT 连接 LED2 DIN；两颗 WS2812C 均由 +3.3V/GND 供电并各配置 100nF 去耦。

- 参数与网络：`input=RGB to LED1 DIN`；`chain=LED1 DOUT to LED2 DIN`；`supply=+3.3V`；`decoupling=C9 100nF,C14 100nF`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中上 LED1/LED2 WS2812C：RGB-DI、DO-DI、+3.3V/GND 与 C9/C14

## 音频

### LS1 Buzzer

+3.3V 经 R14 10Ω 和 LS1 后由 Q3 SS8050 Y1 低侧开关到 GND，BEEP 经 R18 470Ω 进入 Q3 控制节点。

- 参数与网络：`supply=+3.3V`；`series_resistor=R14 10Ω`；`buzzer=LS1`；`driver=Q3 SS8050 Y1`；`control=BEEP via R18 470Ω`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面右中 +3.3V-R14-LS1-Q3-GND 与 BEEP-R18 控制支路

## 调试与烧录

### P3 SWD_5p

P3 的 1 脚接 +3.3V/VCC，2 脚接 SWCLK，3 脚接 SWDIO，4 脚接 NRST，5 脚接 GND；SWCLK/SWDIO 分别连接 U1 PA14/PA13。

- 参数与网络：`pin_1=VCC +3.3V`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面中部 P3 SWD_5p 与页面下部 U1 PA14/PA13/NRST 同名网络

## 模拟电路

### BAT_IN1 电量检测

BAT_IN1 经 R23 1MΩ 到 BAT-ADC1，BAT-ADC1 经 R25 1MΩ 和 C27 100nF 接 GND，并连接 U1 PA0。

- 参数与网络：`upper_resistor=R23 1MΩ`；`lower_resistor=R25 1MΩ`；`capacitor=C27 100nF`；`adc_net=BAT-ADC1`；`mcu_pin=U1 PA0`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面下部中右 BAT_IN1-R23-BAT-ADC1-R25/C27-GND 与 U1 PA0

### BAT_IN2 电量检测

BAT_IN2 经 R24 1MΩ 到 BAT-ADC2，BAT-ADC2 经 R26 1MΩ 和 C28 100nF 接 GND，并连接 U1 PA1。

- 参数与网络：`upper_resistor=R24 1MΩ`；`lower_resistor=R26 1MΩ`；`capacitor=C28 100nF`；`adc_net=BAT-ADC2`；`mcu_pin=U1 PA1`
- 证据：图 aa6ea9724768 / 第 1 页 / 页面下部中右 BAT_IN2-R24-BAT-ADC2-R26/C28-GND 与 U1 PA1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom JoyStick | `coprocessor=U1 STM32F030F4P6`；`left_joystick=J1 JH16`；`right_joystick=J2 JH16`；`buttons=S2 LEFT-BTN,S3 RIGHT-BTN`；`battery_adc=BAT-ADC1,BAT-ADC2`；`host_bus=SCL,SDA` |
| 接口 | USB1 Type-C | `power=VBUS`；`cc1=R10 5.1KΩ to GND`；`cc2=R11 5.1KΩ to GND`；`usb_data=unconnected on page` |
| 电源 | U3/U4 双路充电 | `charger_1=U3 TP4067-4.35V to VBAT_IN1`；`charger_2=U4 TP4067-4.35V to VBAT_IN2`；`program_resistors=R12 2.4KΩ,R13 2.4KΩ`；`battery_caps=C7 10uF,C8 10uF`；`status=CHRG,STDBY LEDs` |
| 电源 | BAT_IN1/BAT_IN2 到 +5VIN | `battery_1_or=D1 B5819W SL`；`battery_2_or=D4 B5819W SL`；`boost=U2 SY7088`；`inductor=L1 3015 1.5uH`；`output_diode=D6 B5819W SL`；`output=+5VIN` |
| 接口 | P2 Header 4 | `pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VIN`；`pin_4=GND`；`pullups=R1/R2 4.7KΩ to +3.3V` |
| 接口 | P1 Header 5 | `pin_1=+3.3V`；`pin_2=BEEP`；`pin_3=RGB`；`pin_4=NC`；`pin_5=NC` |
| 总线 | U1 SCL/SDA | `SCL=U1 PA9 to P2.1`；`SDA=U1 PA10 to P2.2` |
| GPIO 与控制信号 | J1 左摇杆 | `X=LEFT-SW-X to PA2`；`Y=LEFT-SW-Y to PA3`；`button=LEFT-SW-B to PA4`；`supply=+3.3V`；`ground=GND` |
| GPIO 与控制信号 | J2 右摇杆 | `X=RIGHT-SW-X to PA6`；`Y=RIGHT-SW-Y to PA5`；`button=RIGHT-SW-B to PA7`；`supply=+3.3V`；`ground=GND` |
| GPIO 与控制信号 | LEFT-BTN/RIGHT-BTN | `left=S2 LEFT-BTN to U1 PF0`；`right=S3 RIGHT-BTN to U1 PF1`；`pullups=R15/R16 10KΩ`；`filters=C10/C11 100nF` |
| 模拟电路 | BAT_IN1 电量检测 | `upper_resistor=R23 1MΩ`；`lower_resistor=R25 1MΩ`；`capacitor=C27 100nF`；`adc_net=BAT-ADC1`；`mcu_pin=U1 PA0` |
| 模拟电路 | BAT_IN2 电量检测 | `upper_resistor=R24 1MΩ`；`lower_resistor=R26 1MΩ`；`capacitor=C28 100nF`；`adc_net=BAT-ADC2`；`mcu_pin=U1 PA1` |
| GPIO 与控制信号 | LED1/LED2 WS2812C | `input=RGB to LED1 DIN`；`chain=LED1 DOUT to LED2 DIN`；`supply=+3.3V`；`decoupling=C9 100nF,C14 100nF` |
| 音频 | LS1 Buzzer | `supply=+3.3V`；`series_resistor=R14 10Ω`；`buzzer=LS1`；`driver=Q3 SS8050 Y1`；`control=BEEP via R18 470Ω` |
| 调试与烧录 | P3 SWD_5p | `pin_1=VCC +3.3V`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=NRST`；`pin_5=GND` |
| 总线地址 | U1 STM32F030F4P6 I2C 从机地址 | `documented_address=0x59`；`schematic_address_label=null`；`address_source=firmware-controlled` |

## 待确认事项

- `address.stm32-i2c`：原理图显示 U1 通过 SCL/SDA 通信，但页面没有标注从机地址或硬件地址选择网络，因此仅凭原理图无法确认 0x59 地址。（证据：图 aa6ea9724768 / 第 1 页 / 页面下部 U1 PA9/PA10 与 P2 SCL/SDA；整页无 0x59 或地址绑定位标注）
- `review.stm32-i2c-address`：请用 STM32 固件源码或通信协议确认 Atom JoyStick 协处理器的 I2C 地址是否固定为 0x59。；原因：STM32 的 I2C 从机地址由固件定义，原理图只显示 SCL/SDA 物理连接，不能证明 0x59。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `aa6ea9724768216e0cb39132ef2effd40d57501cf9e3ef1d690d9ce8c75013f8` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/c0a25d850ef9122df3669baeab813e5.png` |

---

源文档：`zh_CN/app/Atom JoyStick.md`

源文档 SHA-256：`077eea4882a938ec5a3d104c06f9248c9f8f097121cdbf0940ff04494f860acb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
