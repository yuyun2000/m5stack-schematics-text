# AtomS3R 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R |
| SKU | C126 |
| 产品 ID | `atoms3r-494d86750895` |
| 源文档 | `zh_CN/core/AtomS3R.md` |

## 概述

AtomS3R 以 U1 ESP32-S3-PICO-1-N8R8 为核心，U2 JW5712 将 VIN_5V 转为 VDD_3V3，并集成原生 USB-C、ESP-H0920-PIFA 天线、红外驱动、用户按键和扩展 GPIO。U6 BMI270 通过 SYS_SCL/SYS_SDA 连接主控，U9 BMM150 挂接 BMI270 的 A_SCL/A_SDA 辅助总线，U4 LP5562 同样使用 SYS I2C 并控制 RGB 与显示背光。J1 以 SPI_MOSI/SPI_SCK、DISP_CS、DISP_RS、DISP_RST 和 LED_BL 连接显示模组。原理图未标显示驱动 IC/分辨率、I2C 地址、SiP 存储容量、射频/红外性能或休眠电流。

## 检索关键词

`AtomS3R`、`C126`、`ESP32-S3-PICO-1-N8R8`、`JW5712`、`LP5562`、`BMI270`、`BMM150`、`PMS150G-U6`、`ESP-H0920-PIFA`、`HDGC/0.5K-HX-8PWB`、`ST7735`、`GC9107`、`USB-C`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`SPI_MOSI`、`SPI_SCK`、`DISP_CS`、`DISP_RS`、`DISP_RST`、`LED_BL`、`LED_BL_DRV`、`USER_BUT`、`GPIO41`、`IR_LED_DRV`、`GPIO47`、`GPIO1`、`GPIO2`、`GPIO5-GPIO8`、`GPIO38`、`GPIO39`、`8MB Flash`、`8MB PSRAM`、`128x128`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3-PICO-1-N8R8 | 主控 SiP，连接显示、IMU、USB、IR、RGB、按键、GPIO 和射频 | 图 f6814e0cd0e8 / 第 1 页 / 网格 A3-B4，U1 ESP32-S3-PICO-1-N8R8 全部信号与电源引脚 |
| U2 | JW5712 | VIN_5V 到 VDD_3V3 的开关稳压器 | 图 f6814e0cd0e8 / 第 1 页 / 网格 C1-C3，U2 JW5712、L1 与输入/输出电容 |
| U4 | LP5562 | SYS I2C RGB LED 控制器，输出 LED_R/G/B 与 LED_BL_DRV | 图 f6814e0cd0e8 / 第 1 页 / 网格 C1-D3，U4 LP5562、SYS_SDA/SYS_SCL、LED_R/G/B、LED_BL_DRV |
| U6 | BMI270 | 连接 SYS I2C 并提供 A_SCL/A_SDA 辅助总线的六轴惯性传感器 | 图 f6814e0cd0e8 / 第 1 页 / 网格 C6-D6，U6 BMI270 的 SCx/SDx、ASCx/ASDx 与中断引脚 |
| U9 | BMM150 | 连接 BMI270 辅助 I2C 的三轴磁力计 | 图 f6814e0cd0e8 / 第 1 页 / 网格 C5，U9 BMM150 与 A_SCL/A_SDA |
| U7 | PMS150G-U6 | 连接 SYS_SCL/GPIO_LED/ESP_EN 的辅助控制器及绿色状态灯控制 | 图 f6814e0cd0e8 / 第 1 页 / 网格 D2-D3，U7 PMS150G-U6、D1 GREEN、GPIO_LED 与 ESP_EN |
| ANT1 | ESP-H0920-PIFA | U1 ESP_LNA 射频端的 PIFA 天线 | 图 f6814e0cd0e8 / 第 1 页 / 网格 A1-A3，ANT1、R1、C1、C2 与 ESP_LNA |
| J1 | HDGC/0.5K-HX-8PWB | 显示模组背光、电源、复位、命令/数据与 SPI 接口 | 图 f6814e0cd0e8 / 第 1 页 / 网格 A5，J1 pin1-pin8 的 LED_BL/GND/DISP_RST/DISP_RS/SPI_MOSI/SPI_SCK/VDD_3V3/DISP_CS |
| J2 | USB-TYPEC | VIN_5V 输入与 USB_D_P/USB_D_N 原生 USB 接口 | 图 f6814e0cd0e8 / 第 1 页 / 网格 A6-A7，J2 USB-TYPEC、F1、R4/R5、R19/R20、D3/D4 |
| J5,J6 | THT_Male_P_1x5 / THT_Male_P_1x4 | 底部 3.3V/5V/GND 与六路 GPIO 扩展排针 | 图 f6814e0cd0e8 / 第 1 页 / 网格 B6，J5/J6 各针脚网络 |
| J7 | GH2.0-4P | GPIO1、GPIO2、VIN_5V、GND Grove/HY2.0-4P 接口 | 图 f6814e0cd0e8 / 第 1 页 / 网格 B5-C6，J7、R17/R18、D5/D6 |
| FET1 | CJ1339K | 由 LP5562 LED_BL_DRV 控制 LED_BL 的显示背光开关 | 图 f6814e0cd0e8 / 第 1 页 / 网格 C2-D3，FET1 CJ1339K、R7/R8、LED_BL_DRV 与 LED_BL |
| FET2,D2 | CJ3134K KF / XMEIHUA/MHS153IRCT | GPIO47 IR_LED_DRV 控制的红外 LED 低侧驱动 | 图 f6814e0cd0e8 / 第 1 页 / 网格 B7-C8，D2、R2、FET2、R3 与 IR_LED_DRV |
| S1,S2 | SMT_SW_PTS_820 / SMT_SW_TS_015 | USER_BUT 用户按键与 ESP_EN 复位按键 | 图 f6814e0cd0e8 / 第 1 页 / 网格 C4-D4，S1 USER_BUT 与 S2 ESP_EN |
| F1,D3-D6 | 6V/2A/PPTC / ESD5Z3V3 | USB 电源过流保护及 USB/Grove 信号 ESD 保护 | 图 f6814e0cd0e8 / 第 1 页 / 网格 A6-A7 的 F1/D3/D4 与网格 B5-C6 的 D5/D6 |

## 系统结构

### AtomS3R 系统架构

U1 ESP32-S3-PICO-1-N8R8 连接 J1 SPI 显示、U4 LP5562、U6 BMI270/U9 BMM150、J2 原生 USB、ANT1 PIFA、FET2 红外驱动、S1 用户按键以及 J5/J6/J7 扩展接口；U2 JW5712 为全板生成 VDD_3V3。

- 参数与网络：`controller=U1 ESP32-S3-PICO-1-N8R8`；`display=J1 SPI display interface`；`rgb_backlight=U4 LP5562,FET1`；`imu=U6 BMI270 + U9 BMM150`；`usb=J2 native USB`；`rf=ANT1 ESP-H0920-PIFA`；`power=U2 JW5712`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 完整单页，U1 主控及所有功能分区

## 核心器件

### LP5562 RGB 与背光控制

U4 LP5562 由 VDD_3V3 供电并经 SYS_SDA/SYS_SCL 控制，R/G/B 输出形成 LED_R/LED_G/LED_B；W 输出为 LED_BL_DRV，经 R8 10KΩ、FET1 CJ1339K 与 R7 15Ω 控制 J1 的 LED_BL。

- 参数与网络：`driver=U4 LP5562`；`bus=SYS_SCL/SYS_SDA`；`rgb_outputs=LED_R,LED_G,LED_B`；`white_output=LED_BL_DRV`；`switch=FET1 CJ1339K`；`backlight=R7 15Ω -> LED_BL`；`enable=VDD_3V3`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C1-D3，U4 LP5562、FET1、R7/R8 与 LED_BL

## 电源

### VIN_5V 到 VDD_3V3

U2 JW5712 的 VIN/EN 接 VIN_5V，SW 经 L1 MWTC201608S2R2 输出 VDD_3V3；输入 C15 10uF/C16 100nF，输出 C7 100nF/C13 10uF，C12 1nF 连接 VOS。

- 参数与网络：`converter=U2 JW5712`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF`；`vos_cap=C12 1nF`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C1-C3，U2/L1/VIN_5V/VDD_3V3

## 接口

### J7 Grove/HY2.0-4P 接口

J7 GH2.0-4P pin1=GPIO1、pin2=GPIO2、pin3=VIN_5V、pin4=GND；GPIO1/GPIO2 各经 R17/R18 串联器件并带 D5/D6 ESD5Z3V3 对地保护。

- 参数与网络：`pin1=GPIO1, bidirectional VDD_3V3 domain`；`pin2=GPIO2, bidirectional VDD_3V3 domain`；`pin3=VIN_5V power`；`pin4=GND`；`series=R17/R18 PRG15BC330MM1RC`；`protection=D5/D6 ESD5Z3V3`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 B5-C6，J7 pin1-pin4、R17/R18、D5/D6

### 底部 GPIO 与电源接口

J5 pin1=VDD_3V3、pin2=GPIO6、pin3=GPIO5、pin4=GPIO7、pin5=GPIO8；J6 pin1=GPIO39、pin2=GPIO38、pin3=VIN_5V、pin4=GND。

- 参数与网络：`J5=pin1 VDD_3V3,pin2 GPIO6,pin3 GPIO5,pin4 GPIO7,pin5 GPIO8`；`J6=pin1 GPIO39,pin2 GPIO38,pin3 VIN_5V,pin4 GND`；`gpio_direction=bidirectional`；`gpio_level=VDD_3V3 domain`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 B6，J5/J6 各针脚网络

## 总线

### USB-C 原生 USB

J2 DP1/DN1 经 R19/R20 各 22Ω 形成 USB_D_P/USB_D_N，并分别连接 U1 GPIO20/GPIO19；CC1/CC2 经 R4/R5 各 5.1KΩ 接 GND，J2 VCC 经 F1 6V/2A PPTC 形成 VIN_5V。

- 参数与网络：`controller=U1 ESP32-S3-PICO-1-N8R8`；`dp=J2 DP1 -> R19 22Ω -> USB_D_P -> GPIO20`；`dn=J2 DN1 -> R20 22Ω -> USB_D_N -> GPIO19`；`cc=R4/R5 5.1KΩ to GND`；`power=J2 VCC -> F1 -> VIN_5V`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A6-A7，J2/R19/R20/R4/R5/F1 与 U1 USB_D_P/USB_D_N

### SYS_SCL/SYS_SDA 系统 I2C

U1 GPIO0 形成 SYS_SCL，GPIO45 形成 SYS_SDA；R10/R11 各 2.2KΩ 上拉到 VDD_3V3，总线连接 U4 LP5562 的 SCL/SDA 与 U6 BMI270 的 SCx/SDx。

- 参数与网络：`controller=U1 ESP32-S3-PICO-1-N8R8`；`scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`devices=U4 LP5562,U6 BMI270`
- 证据：图 f6814e0cd0e8 / 第 1 页 / U1 SYS_SCL/SYS_SDA；网格 C1-D3 U4；网格 C6-D6 U6；R10/R11

### BMI270 辅助 I2C 与 BMM150

U6 BMI270 ASDx/ASCx 形成 A_SDA/A_SCL 并连接 U9 BMM150 SDx/SCK；R12 2.2KΩ 将 A_SDA 上拉到 VDD_3V3，U9 CSB 接 GND。

- 参数与网络：`hub=U6 BMI270`；`device=U9 BMM150`；`sda=ASDx/A_SDA`；`scl=ASCx/A_SCL`；`pullup=R12 2.2KΩ on A_SDA`；`bmm150_csb=GND`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C5-D6，U6/U9/A_SDA/A_SCL/R12

### 显示 SPI 与控制映射

J1 pin1=LED_BL、pin2=GND、pin3=DISP_RST/GPIO48、pin4=DISP_RS/GPIO42、pin5=SPI_MOSI/GPIO21、pin6=SPI_SCK/GPIO15、pin7=VDD_3V3、pin8=DISP_CS/GPIO14。

- 参数与网络：`connector=J1 HDGC/0.5K-HX-8PWB`；`pin1=LED_BL, power input`；`pin2=GND`；`pin3=DISP_RST / GPIO48, output`；`pin4=DISP_RS / GPIO42, output`；`pin5=SPI_MOSI / GPIO21, output`；`pin6=SPI_SCK / GPIO15, output`；`pin7=VDD_3V3`；`pin8=DISP_CS / GPIO14, output`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A3-A5，U1 GPIO14/15/21/42/48 网络与 J1 pin1-pin8

## GPIO 与控制信号

### USER_BUT 用户按键

U1 GPIO41 连接 USER_BUT；R6 10KΩ 将 USER_BUT 上拉到 VDD_3V3，S1 SMT_SW_PTS_820 按下接 GND，C11 1nF 对地。

- 参数与网络：`gpio=GPIO41`；`net=USER_BUT`；`button=S1 SMT_SW_PTS_820`；`active_level=low`；`pullup=R6 10KΩ to VDD_3V3`；`capacitor=C11 1nF to GND`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 B4-C4，U1 GPIO41/USER_BUT、R6、C11、S1

### 红外 LED 驱动

U1 GPIO47 输出 IR_LED_DRV，经 R3 100KΩ 控制 FET2 CJ3134K KF；FET2 低侧驱动 D2 XMEIHUA/MHS153IRCT，D2 经 R2 15Ω 接 VDD_3V3。

- 参数与网络：`gpio=GPIO47`；`net=IR_LED_DRV`；`gate_resistor=R3 100KΩ`；`fet=FET2 CJ3134K KF`；`led=D2 XMEIHUA/MHS153IRCT`；`series_resistor=R2 15Ω`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 B7-C8，U1 GPIO47、IR_LED_DRV、R3、FET2、D2、R2

## 时钟

### 主控外部晶振引脚

U1 XTAL_P、XTAL_N、XTAL_32K_P 和 XTAL_32K_N 在本页均以未连接标记结束，板级原理图未画出外部主晶振或 32.768kHz 晶振网络。

- 参数与网络：`main_xtal=U1 XTAL_P/XTAL_N not connected`；`rtc_xtal=U1 XTAL_32K_P/XTAL_32K_N not connected`；`external_crystal=false`；`internal_clock_frequency=null`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A3-B4，U1 pins21-24 与 pin53 的 XTAL 标记及未连接叉号

## 复位

### ESP_EN 复位与辅助控制

S2 SMT_SW_TS_015 按下将 ESP_EN 接 GND，C17 1nF 对地；R14 10KΩ 将 ESP_EN 上拉到 VDD_3V3，C24 1uF 对地；U7 PMS150G-U6 也连接 ESP_EN、GPIO_LED 与 SYS_SCL。

- 参数与网络：`reset_button=S2 SMT_SW_TS_015`；`net=ESP_EN`；`active_level=low`；`pullup=R14 10KΩ`；`caps=C17 1nF,C24 1uF`；`aux_controller=U7 PMS150G-U6`；`aux_signals=SYS_SCL,GPIO_LED,ESP_EN`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C4-D3，S2/C17/R14/C24/U7/D1

## 保护电路

### USB 与 Grove 保护

D3/D4 ESD5Z3V3 分别从 USB_D_P/USB_D_N 对地钳位，D5/D6 ESD5Z3V3 分别从 GPIO1/GPIO2 对地钳位；F1 6V/2A PPTC 串接 USB VCC 与 VIN_5V。

- 参数与网络：`usb_esd=D3 USB_D_P,D4 USB_D_N`；`grove_esd=D5 GPIO1,D6 GPIO2`；`device=ESD5Z3V3`；`overcurrent=F1 6V/2A PPTC`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A6-A7 的 D3/D4/F1 与网格 B5-C6 的 D5/D6

## 射频

### PIFA 天线与匹配

U1 LNA_IN 通过 ESP_LNA 网络连接 ANT1 ESP-H0920-PIFA；串联 R1 2.4nH，C1 2.7pF 与 C2 2.0pF 对地形成匹配网络。

- 参数与网络：`antenna=ANT1 ESP-H0920-PIFA`；`mcu_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A1-A3，ANT1/R1/C1/C2/ESP_LNA/LNA_IN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3R 系统架构 | `controller=U1 ESP32-S3-PICO-1-N8R8`；`display=J1 SPI display interface`；`rgb_backlight=U4 LP5562,FET1`；`imu=U6 BMI270 + U9 BMM150`；`usb=J2 native USB`；`rf=ANT1 ESP-H0920-PIFA`；`power=U2 JW5712` |
| 电源 | VIN_5V 到 VDD_3V3 | `converter=U2 JW5712`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF`；`vos_cap=C12 1nF` |
| 总线 | USB-C 原生 USB | `controller=U1 ESP32-S3-PICO-1-N8R8`；`dp=J2 DP1 -> R19 22Ω -> USB_D_P -> GPIO20`；`dn=J2 DN1 -> R20 22Ω -> USB_D_N -> GPIO19`；`cc=R4/R5 5.1KΩ to GND`；`power=J2 VCC -> F1 -> VIN_5V` |
| 保护电路 | USB 与 Grove 保护 | `usb_esd=D3 USB_D_P,D4 USB_D_N`；`grove_esd=D5 GPIO1,D6 GPIO2`；`device=ESD5Z3V3`；`overcurrent=F1 6V/2A PPTC` |
| 射频 | PIFA 天线与匹配 | `antenna=ANT1 ESP-H0920-PIFA`；`mcu_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF` |
| 总线 | SYS_SCL/SYS_SDA 系统 I2C | `controller=U1 ESP32-S3-PICO-1-N8R8`；`scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`devices=U4 LP5562,U6 BMI270` |
| 总线 | BMI270 辅助 I2C 与 BMM150 | `hub=U6 BMI270`；`device=U9 BMM150`；`sda=ASDx/A_SDA`；`scl=ASCx/A_SCL`；`pullup=R12 2.2KΩ on A_SDA`；`bmm150_csb=GND` |
| 核心器件 | LP5562 RGB 与背光控制 | `driver=U4 LP5562`；`bus=SYS_SCL/SYS_SDA`；`rgb_outputs=LED_R,LED_G,LED_B`；`white_output=LED_BL_DRV`；`switch=FET1 CJ1339K`；`backlight=R7 15Ω -> LED_BL`；`enable=VDD_3V3` |
| 总线 | 显示 SPI 与控制映射 | `connector=J1 HDGC/0.5K-HX-8PWB`；`pin1=LED_BL, power input`；`pin2=GND`；`pin3=DISP_RST / GPIO48, output`；`pin4=DISP_RS / GPIO42, output`；`pin5=SPI_MOSI / GPIO21, output`；`pin6=SPI_SCK / GPIO15, output`；`pin7=VDD_3V3`；`pin8=DISP_CS / GPIO14, output` |
| GPIO 与控制信号 | USER_BUT 用户按键 | `gpio=GPIO41`；`net=USER_BUT`；`button=S1 SMT_SW_PTS_820`；`active_level=low`；`pullup=R6 10KΩ to VDD_3V3`；`capacitor=C11 1nF to GND` |
| 复位 | ESP_EN 复位与辅助控制 | `reset_button=S2 SMT_SW_TS_015`；`net=ESP_EN`；`active_level=low`；`pullup=R14 10KΩ`；`caps=C17 1nF,C24 1uF`；`aux_controller=U7 PMS150G-U6`；`aux_signals=SYS_SCL,GPIO_LED,ESP_EN` |
| GPIO 与控制信号 | 红外 LED 驱动 | `gpio=GPIO47`；`net=IR_LED_DRV`；`gate_resistor=R3 100KΩ`；`fet=FET2 CJ3134K KF`；`led=D2 XMEIHUA/MHS153IRCT`；`series_resistor=R2 15Ω` |
| 接口 | J7 Grove/HY2.0-4P 接口 | `pin1=GPIO1, bidirectional VDD_3V3 domain`；`pin2=GPIO2, bidirectional VDD_3V3 domain`；`pin3=VIN_5V power`；`pin4=GND`；`series=R17/R18 PRG15BC330MM1RC`；`protection=D5/D6 ESD5Z3V3` |
| 接口 | 底部 GPIO 与电源接口 | `J5=pin1 VDD_3V3,pin2 GPIO6,pin3 GPIO5,pin4 GPIO7,pin5 GPIO8`；`J6=pin1 GPIO39,pin2 GPIO38,pin3 VIN_5V,pin4 GND`；`gpio_direction=bidirectional`；`gpio_level=VDD_3V3 domain` |
| 时钟 | 主控外部晶振引脚 | `main_xtal=U1 XTAL_P/XTAL_N not connected`；`rtc_xtal=U1 XTAL_32K_P/XTAL_32K_N not connected`；`external_crystal=false`；`internal_clock_frequency=null` |
| 核心器件 | 显示驱动 IC、尺寸与分辨率 | `documented_size=0.85 inch`；`documented_resolution=128x128`；`documented_current_driver=ST7735`；`documented_previous_driver=GC9107`；`documented_change_date=2026-05-14`；`schematic_driver=null`；`schematic_resolution=null` |
| 总线地址 | BMI270 与 BMM150 I2C 地址 | `documented_bmi270=0x68`；`bmm150=null`；`topology=ESP32 SYS I2C -> BMI270 -> auxiliary I2C -> BMM150`；`schematic_addresses=null` |
| 总线地址 | LP5562 I2C 地址 | `device=U4 LP5562`；`bus=SYS_SCL/SYS_SDA`；`ad1=GND`；`ad0=GND`；`address=null` |
| 内存与 Flash | 8MB Flash 与 8MB PSRAM | `part_number=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB Octal`；`external_memory=null`；`schematic_capacity_fields=null` |
| 射频 | 增强 3D 天线性能 | `antenna=ANT1 ESP-H0920-PIFA`；`matching=R1/C1/C2`；`gain=null`；`efficiency=null`；`range=null`；`return_loss=null`；`certification=null` |
| 其他事实 | 红外距离与休眠电流 | `documented_ir_distance=12.46m at 180 degrees unobstructed`；`documented_gpio_5v_sleep=11.63uA`；`documented_grove_5v_sleep=10.75uA`；`documented_usb_5v_sleep=92.50uA including PD resistor loss`；`measurement_conditions=null` |

## 待确认事项

- `component.display-driver-spec`：正文当前规格写 0.85 英寸、128x128、ST7735，并记录 2026-05-14 从 GC9107 变更为 ST7735；原理图只画 J1 显示接口及信号，没有面板位号、驱动 IC 型号、尺寸或分辨率。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A5，J1 仅显示八针接口，无 ST7735/GC9107/128x128 文字）
- `address.imu-addresses`：正文给出 BMI270 地址 0x68，并说明 BMM150 通过 BMI270 Sensor Hub 访问；原理图确认总线拓扑，但未标出 BMI270/BMM150 的 7 位地址或 BMI270 地址选择状态。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C5-D6，U6/U9 总线，无地址文字）
- `address.lp5562`：U4 LP5562 的 AD1 与 AD0 引脚均接 GND，原理图确认其地址脚状态，但本页没有写出对应 7 位 I2C 地址。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 C1-D2，U4 LP5562 AD1/AD0 接 GND，无地址文字）
- `memory.documented-n8r8`：原理图明确标 U1 为 ESP32-S3-PICO-1-N8R8，正文解释为 8MB Flash 和 8MB Octal PSRAM；板级图未单列容量字段或外部存储器，容量含义需由 SiP datasheet 或实机确认。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A3-B4，U1 型号，无独立 Flash/PSRAM 容量字段）
- `rf.documented-performance`：原理图确认 ANT1 ESP-H0920-PIFA 及 R1/C1/C2 匹配网络，但正文所称增强性能和稳定性未在图中给出增益、效率、范围、回波损耗或认证结果。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A1-A3，ANT1 匹配网络，无射频性能表）
- `other.documented-ir-sleep-performance`：正文给出 180° 时红外无遮挡距离 12.46m，并列出 GPIO-5V、Grove-5V、USB-5V 三种休眠电流；原理图只确认红外驱动和三种 VIN_5V 入口路径，未提供光学测试条件或电流测量结果。（证据：图 f6814e0cd0e8 / 第 1 页 / 网格 A6-A7 USB 供电、B6/C6 GPIO/Grove 供电及 B7-C8 红外驱动，无测量数据）
- `review.display-driver-spec`：请按当前量产 BOM/屏幕模组丝印确认驱动 IC 为 ST7735，并确认 0.85 英寸与 128x128；同时明确该 v0.4.1 原理图对应变更前还是变更后硬件。；原因：原理图只有 J1 电气接口，正文另记录 GC9107 到 ST7735 的版本变更。
- `review.imu-addresses`：请确认 BMI270 的 7 位地址是否为 0x68，以及 BMM150 在 Sensor Hub 辅助总线上的地址和初始化方式。；原因：原理图未标地址。
- `review.lp5562-address`：LP5562 在 AD1=0、AD0=0 时的正式 7 位 I2C 地址是什么？；原因：原理图只给出地址脚电平。
- `review.memory-capacity`：请用 ESP32-S3-PICO-1-N8R8 datasheet 或实机确认 8MB Flash 和 8MB Octal PSRAM。；原因：容量解释不是板级原理图直接字段。
- `review.rf-performance`：ANT1 的增益、效率、匹配验证、范围、回波损耗和认证结果是什么？；原因：原理图只确认天线器件和匹配网络。
- `review.ir-sleep-performance`：请提供红外 12.46m 测试条件及三种供电路径休眠电流的硬件版本、固件状态和测量方法。；原因：这些性能数据不能由连接图独立验证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f6814e0cd0e897a09992bb89ebb5592d44b28aa2e3fd2391db43300349894ede` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1_page_01.png` |

---

源文档：`zh_CN/core/AtomS3R.md`

源文档 SHA-256：`d2f630a422f47d67e5545a9ec6ecc0d2359a18cf84f4c9a67324cdd84148e43b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
