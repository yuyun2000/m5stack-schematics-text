# AtomS3R-M12 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R-M12 |
| SKU | C126-M12 |
| 产品 ID | `atoms3r-m12-83a8cec27f25` |
| 源文档 | `zh_CN/core/AtomS3R-M12.md` |

## 概述

AtomS3R-M12 主板以 U1 ESP32-S3-PICO-1-N8R8 为核心，JW5712 将 VIN_5V 转为 VDD_3V3，USB-C 的 D+/D- 直连原生 USB，并集成 BMI270、BMM150、PIFA 天线、GPIO47 红外驱动、Grove 和底部 GPIO。BMI270 通过 SYS_SCL/SYS_SDA 接主控，BMM150 连接 BMI270 的 A_SCL/A_SDA 辅助总线。扩展板通过 J4/BTB1 承载并行摄像头接口，GPIO18 控制 CJ2301 3.3V 开关，并由 LP3992-12B5F、WL2863E28-5/TR 和 IMP809S/CN809S 提供 1.2V、2.8V 与 CAM_RST。原理图未直接标摄像头芯片型号/性能、IMU 地址、内存容量、UVC 固件或射频性能，且正文的 OV3660 与管脚表的 OV3360(M12) 存在命名冲突。

## 检索关键词

`AtomS3R-M12`、`C126-M12`、`ESP32-S3-PICO-1-N8R8`、`JW5712`、`BMI270`、`BMM150`、`OV3660`、`OV3360(M12)`、`LP3992-12B5F`、`WL2863E28-5/TR`、`IMP809S/CN809S`、`ESP-H0920-PIFA`、`USB-C`、`USB_D_P`、`USB_D_N`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`IR_LED_DRV`、`GPIO47`、`GPIO18`、`CAM_RST`、`SIO_D`、`SIO_C`、`VSYNC`、`HREF`、`XCLK`、`PCLK`、`Y2-Y9`、`VDD_3V3`、`DVDD 1.2V`、`AVDD 2.8V`、`FPC1`、`BTB1`、`J4`、`GPIO1`、`GPIO2`、`8MB Flash`、`8MB PSRAM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (主板) | ESP32-S3-PICO-1-N8R8 | 主控 SiP，连接 USB、摄像头、IMU、红外、GPIO、按键和射频 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A3-B4，U1 ESP32-S3-PICO-1-N8R8 全部 GPIO/USB/射频/电源引脚 |
| U2 (主板) | JW5712 | 将 VIN_5V 转换为 VDD_3V3 的开关稳压器 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C1-C3，U2 JW5712、L1 与 VDD_3V3 |
| U6 | BMI270 | 连接 SYS_SCL/SYS_SDA 与 A_SCL/A_SDA 的六轴惯性传感器 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C6-D6，U6 BMI270 |
| U9 | BMM150 | 连接 BMI270 辅助 I2C A_SCL/A_SDA 的三轴磁力计 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C5，U9 BMM150 与 A_SCL/A_SDA |
| U7 | PMS150G-U6 | 连接 SYS_SCL/GPIO_LED/ESP_EN 的辅助控制器 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 D2-D3，U7 PMS150G-U6 与 D1 GREEN、ESP_EN |
| ANT1 | ESP-H0920-PIFA | ESP_LNA 射频端的 PIFA 天线 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A1-A2，ANT1 ESP-H0920-PIFA 与 R1/C1/C2 |
| J2 | USB-TYPEC | VIN_5V 与原生 USB_D_P/USB_D_N 接口 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A6-A7，J2 USB-TYPEC、F1、R4/R5、R19/R20、D3/D4 |
| FET2,D2 | CJ3134K KF / XMEIHUA/MHS153IRCT | GPIO47 IR_LED_DRV 控制的红外 LED 低侧驱动 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B7-C8，D2 红外 LED、R2、FET2、R3/IR_LED_DRV |
| J7 | GH2.0-4P | GPIO1、GPIO2、VIN_5V、GND Grove 扩展接口 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B5-C6，J7 GH2.0-4P 与 D5/D6/R17/R18 |
| J5,J6 | THT_Male_P_1x5 / THT_Male_P_1x4 | 底部 GPIO、3.3V、5V 与 GND 扩展接口 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B6，J5/J6 引脚网络 |
| J4 | XKB_X0400FVS-24 | 24 针主板到摄像头扩展板连接器 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A5-B6，J4 24 针 GPIO/SYS_SCL/SYS_SDA/VDD_3V3 |
| BTB1 | X0400WVS-24-LPV01 | 扩展板 24 针板间连接器，与主板 J4 对应 | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 C1-D2，BTB1 pin1-pin28 |
| FPC1 | FPC-0.5-24P | 摄像头模组接口，连接控制、同步、时钟、Y2-Y9 数据和三路电源 | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 A1-B2，FPC1 FPC-0.5-24P |
| U1 (扩展板) | LP3992-12B5F | VDD_3V3 输入、DVDD 1.2V/300mA 输出的摄像头 LDO | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 B3，U1 LP3992-12B5F，红字 Vout:1.2V Imax:300mA |
| U2 (扩展板) | WL2863E28-5/TR | VDD_3V3 输入、AVDD 2.8V/250mA 输出的摄像头 LDO | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 C3，U2 WL2863E28-5/TR，红字 Vout:2.8V Imax:250mA |
| U3 (扩展板) | IMP809S/CN809S | 产生 CAM_RST 的复位监控器 | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 D3，U3 IMP809S/CN809S 与 CAM_RST |
| Q1 (扩展板) | CJ2301 | GPIO18 控制 VDD_3V3_IN 到 VDD_3V3 的摄像头电源开关 | 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 A3-B4，Q1 CJ2301、R4、GPIO18 |
| S2 | SMT_SW_TS_015 | ESP_EN 对地复位/下载按键 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C4，S2 SMT_SW_TS_015 与 ESP_EN |
| F1,D3-D6 | 6V/2A/PPTC / ESD5Z3V3 | USB 5V 过流保护及 USB/Grove 信号 ESD 保护 | 图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A6-A7 与 B5-C6，F1、D3-D6 |

## 系统结构

### AtomS3R-M12 系统架构

U1 ESP32-S3-PICO-1-N8R8 连接原生 USB、PIFA 天线、BMI270/BMM150、IR_LED_DRV、Grove 和 J4；J4/BTB1 将摄像头 GPIO、SYS I2C 和 3.3V 送到扩展板，FPC1 再连接摄像头模组，扩展板生成 DVDD 1.2V、AVDD 2.8V 和受 GPIO18 控制的 VDD_3V3。

- 参数与网络：`mcu=ESP32-S3-PICO-1-N8R8`；`imu=BMI270+BMM150`；`camera=J4/BTB1 -> FPC1`；`camera_rails=VDD_3V3,DVDD 1.2V,AVDD 2.8V`；`usb=J2 native USB`；`rf=ANT1 PIFA`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页完整主板; 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页完整摄像头扩展板

## 电源

### VIN_5V 到 VDD_3V3

U2 JW5712 的 VIN 接 VIN_5V，SW 经 L1 MWTC201608S2R2 输出 VDD_3V3；输入 C15 10uF/C16 100nF、输出 C7 100nF/C13 10uF，C12 1nF 连接 VOS 网络。

- 参数与网络：`converter=U2 JW5712`；`input=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C1-C3 U2/L1/VIN_5V/VDD_3V3

### GPIO18 摄像头 3.3V 电源开关

BTB1 的 VDD_3V3_IN 经 Q1 CJ2301 形成 VDD_3V3，Q1 栅极由 GPIO18 控制并由 R4 10KΩ 拉向 VDD_3V3_IN；VDD_3V3 供摄像头板 LDO、复位与 FPC 电路。

- 参数与网络：`input=VDD_3V3_IN`；`switch=Q1 CJ2301`；`control=GPIO18`；`pullup=R4 10KΩ`；`output=VDD_3V3`
- 证据：图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 A3-B4 Q1/R4/GPIO18

### 摄像头 1.2V 与 2.8V 电源

U1 LP3992-12B5F 从 VDD_3V3 生成 DVDD，图中标 Vout 1.2V、Imax 300mA；U2 WL2863E28-5/TR 从 VDD_3V3 生成 AVDD，图中标 Vout 2.8V、Imax 250mA。

- 参数与网络：`digital=LP3992-12B5F -> DVDD 1.2V 300mA`；`analog=WL2863E28-5/TR -> AVDD 2.8V 250mA`；`input=VDD_3V3`；`caps=C1-C4 1uF`
- 证据：图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 B3-C4 U1/U2 与红色输出参数

## 接口

### J7 Grove 接口

J7 GH2.0-4P 的 pin1=GPIO1、pin2=GPIO2、pin3=VIN_5V、pin4=GND；GPIO1/GPIO2 各带 D5/D6 ESD5Z3V3 对地保护及 R17/R18 串联器件。

- 参数与网络：`pin1=GPIO1, bidirectional 3.3V GPIO`；`pin2=GPIO2, bidirectional 3.3V GPIO`；`pin3=VIN_5V power`；`pin4=GND`；`protection=D5/D6 ESD5Z3V3`；`series=R17/R18 PRG15BC330MM1RC`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B5-C6 J7/D5/D6/R17/R18

### 底部 GPIO 与电源接口

J5 1x5 引出 VDD_3V3、GPIO6、GPIO5、GPIO7、GPIO8；J6 1x4 引出 GPIO39、GPIO38、VIN_5V、GND。

- 参数与网络：`J5=pin1 VDD_3V3,pin2 GPIO6,pin3 GPIO5,pin4 GPIO7,pin5 GPIO8`；`J6=pin1 GPIO39,pin2 GPIO38,pin3 VIN_5V,pin4 GND`；`gpio_level=VDD_3V3 domain`；`gpio_direction=bidirectional`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B6 J5/J6

## 总线

### USB-C 原生 USB

J2 DP1/DN1 经 R19/R20 各 22Ω 形成 USB_D_P/USB_D_N，并分别连接 U1 GPIO20/GPIO19；CC1/CC2 通过 R4/R5 5.1KΩ 接 GND，VIN_5V 经 F1 6V/2A PPTC。

- 参数与网络：`dp=J2 DP1 -> R19 22Ω -> USB_D_P -> GPIO20`；`dn=J2 DN1 -> R20 22Ω -> USB_D_N -> GPIO19`；`cc=R4/R5 5.1KΩ`；`fuse=F1 6V/2A PPTC`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A6-A7 J2 USB-C 与 U1 USB_D_N/USB_D_P

### BMI270 系统 I2C

U1 GPIO0 形成 SYS_SCL，GPIO45 形成 SYS_SDA；两线经 R10/R11 各 2.2KΩ 上拉到 VDD_3V3，并连接 U6 BMI270 SCx/SDx 和板间 J4/BTB1。

- 参数与网络：`controller=U1 ESP32-S3`；`scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270`；`extension=J4/BTB1`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页 U1 SYS_SCL/SYS_SDA、R10/R11 与 U6 BMI270

### BMI270 辅助 I2C 与 BMM150

U6 BMI270 ASDx/ASCx 分别连接 A_SDA/A_SCL，R12 2.2KΩ 将 A_SDA 上拉到 VDD_3V3；A_SDA/A_SCL 进入 U9 BMM150 的 SDx/SCK，引脚 CSB 接 GND。

- 参数与网络：`hub=U6 BMI270`；`magnetometer=U9 BMM150`；`sda=ASDx/A_SDA`；`scl=ASCx/A_SCL`；`pullup=R12 2.2KΩ on A_SDA`；`bmm150_csb=GND`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C5-D6 U6/U9 与 A_SDA/A_SCL

### 摄像头控制与并行数据映射

FPC1 SIO_D/SIO_C 分别连接 GPIO12/GPIO9，RESET 接 CAM_RST，VSYNC/HREF 接 GPIO10/GPIO14，XCLK 接 GPIO21，PCLK 接 GPIO40；Y9/Y8/Y7/Y6/Y5/Y4/Y3/Y2 分别接 GPIO13/GPIO11/GPIO17/GPIO4/GPIO48/GPIO46/GPIO42/GPIO3。

- 参数与网络：`controller=U1 ESP32-S3-PICO-1-N8R8`；`control=SIO_D GPIO12,SIO_C GPIO9,CAM_RST`；`sync=VSYNC GPIO10,HREF GPIO14`；`clocks=XCLK GPIO21 output,PCLK GPIO40 input`；`data=Y9 G13,Y8 G11,Y7 G17,Y6 G4,Y5 G48,Y4 G46,Y3 G42,Y2 G3`
- 证据：图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 A1-B2 FPC1 pin2-pin24

## GPIO 与控制信号

### 红外 LED 驱动

U1 GPIO47 输出 IR_LED_DRV，经 R3 100KΩ 接 FET2 栅极；FET2 CJ3134K KF 低侧驱动 D2 红外 LED，D2 经 R2 15Ω 接 VDD_3V3。

- 参数与网络：`gpio=GPIO47`；`net=IR_LED_DRV`；`gate_resistor=R3 100KΩ`；`fet=FET2 CJ3134K KF`；`led=D2 XMEIHUA/MHS153IRCT`；`series_resistor=R2 15Ω`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 B7-C8 IR_LED_DRV/FET2/D2

## 复位

### ESP_EN 复位与监控

S2 SMT_SW_TS_015 将 ESP_EN 按下接 GND，C17 1nF 对地；R14 10KΩ 上拉 ESP_EN 到 VDD_3V3，C24 1uF 对地。U7 PMS150G-U6 也连接 ESP_EN 与绿色 D1 指示网络。

- 参数与网络：`button=S2`；`net=ESP_EN`；`pullup=R14 10KΩ`；`caps=C17 1nF,C24 1uF`；`supervisor_mcu=U7 PMS150G-U6`；`indicator=D1 GREEN`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 C4-D3 S2/ESP_EN/R14/C24/U7/D1

### 摄像头 CAM_RST

U3 IMP809S/CN809S 由 VDD_3V3 供电，/RST 输出形成 CAM_RST；R2 10KΩ 将 CAM_RST 上拉到 VDD_3V3，C8 1uF 对地，CAM_RST 连接 FPC1 RESET pin6。

- 参数与网络：`supervisor=U3 IMP809S/CN809S`；`supply=VDD_3V3`；`output=CAM_RST`；`pullup=R2 10KΩ`；`capacitor=C8 1uF`；`camera_pin=FPC1 pin6 RESET`
- 证据：图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页网格 D3 U3/R2/C8 与 FPC1 CAM_RST

## 保护电路

### USB 与 Grove 保护

D3/D4 ESD5Z3V3 分别在 USB_D_P/USB_D_N 对地钳位，D5/D6 ESD5Z3V3 分别在 GPIO1/GPIO2 对地钳位；F1 6V/2A PPTC 串接 USB VCC 到 VIN_5V。

- 参数与网络：`usb_esd=D3 USB_D_P,D4 USB_D_N`；`grove_esd=D5 GPIO1,D6 GPIO2`；`usb_overcurrent=F1 6V/2A PPTC`；`device=ESD5Z3V3`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A6-A7 J2/D3/D4/F1 与 B5-C6 D5/D6

## 射频

### PIFA 天线匹配

U1 LNA_IN 通过 ESP_LNA 网络连接 ANT1 ESP-H0920-PIFA；串联 R1 2.4nH，C1 2.7pF 与 C2 2.0pF 对地形成匹配网络。

- 参数与网络：`antenna=ANT1 ESP-H0920-PIFA`；`mcu_pin=LNA_IN`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF`
- 证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页网格 A1-A3 ANT1/R1/C1/C2/ESP_LNA/LNA_IN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3R-M12 系统架构 | `mcu=ESP32-S3-PICO-1-N8R8`；`imu=BMI270+BMM150`；`camera=J4/BTB1 -> FPC1`；`camera_rails=VDD_3V3,DVDD 1.2V,AVDD 2.8V`；`usb=J2 native USB`；`rf=ANT1 PIFA` |
| 电源 | VIN_5V 到 VDD_3V3 | `converter=U2 JW5712`；`input=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF` |
| 总线 | USB-C 原生 USB | `dp=J2 DP1 -> R19 22Ω -> USB_D_P -> GPIO20`；`dn=J2 DN1 -> R20 22Ω -> USB_D_N -> GPIO19`；`cc=R4/R5 5.1KΩ`；`fuse=F1 6V/2A PPTC` |
| 保护电路 | USB 与 Grove 保护 | `usb_esd=D3 USB_D_P,D4 USB_D_N`；`grove_esd=D5 GPIO1,D6 GPIO2`；`usb_overcurrent=F1 6V/2A PPTC`；`device=ESD5Z3V3` |
| 射频 | PIFA 天线匹配 | `antenna=ANT1 ESP-H0920-PIFA`；`mcu_pin=LNA_IN`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF` |
| 总线 | BMI270 系统 I2C | `controller=U1 ESP32-S3`；`scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270`；`extension=J4/BTB1` |
| 总线 | BMI270 辅助 I2C 与 BMM150 | `hub=U6 BMI270`；`magnetometer=U9 BMM150`；`sda=ASDx/A_SDA`；`scl=ASCx/A_SCL`；`pullup=R12 2.2KΩ on A_SDA`；`bmm150_csb=GND` |
| GPIO 与控制信号 | 红外 LED 驱动 | `gpio=GPIO47`；`net=IR_LED_DRV`；`gate_resistor=R3 100KΩ`；`fet=FET2 CJ3134K KF`；`led=D2 XMEIHUA/MHS153IRCT`；`series_resistor=R2 15Ω` |
| 接口 | J7 Grove 接口 | `pin1=GPIO1, bidirectional 3.3V GPIO`；`pin2=GPIO2, bidirectional 3.3V GPIO`；`pin3=VIN_5V power`；`pin4=GND`；`protection=D5/D6 ESD5Z3V3`；`series=R17/R18 PRG15BC330MM1RC` |
| 接口 | 底部 GPIO 与电源接口 | `J5=pin1 VDD_3V3,pin2 GPIO6,pin3 GPIO5,pin4 GPIO7,pin5 GPIO8`；`J6=pin1 GPIO39,pin2 GPIO38,pin3 VIN_5V,pin4 GND`；`gpio_level=VDD_3V3 domain`；`gpio_direction=bidirectional` |
| 复位 | ESP_EN 复位与监控 | `button=S2`；`net=ESP_EN`；`pullup=R14 10KΩ`；`caps=C17 1nF,C24 1uF`；`supervisor_mcu=U7 PMS150G-U6`；`indicator=D1 GREEN` |
| 总线 | 摄像头控制与并行数据映射 | `controller=U1 ESP32-S3-PICO-1-N8R8`；`control=SIO_D GPIO12,SIO_C GPIO9,CAM_RST`；`sync=VSYNC GPIO10,HREF GPIO14`；`clocks=XCLK GPIO21 output,PCLK GPIO40 input`；`data=Y9 G13,Y8 G11,Y7 G17,Y6 G4,Y5 G48,Y4 G46,Y3 G42,Y2 G3` |
| 电源 | GPIO18 摄像头 3.3V 电源开关 | `input=VDD_3V3_IN`；`switch=Q1 CJ2301`；`control=GPIO18`；`pullup=R4 10KΩ`；`output=VDD_3V3` |
| 电源 | 摄像头 1.2V 与 2.8V 电源 | `digital=LP3992-12B5F -> DVDD 1.2V 300mA`；`analog=WL2863E28-5/TR -> AVDD 2.8V 250mA`；`input=VDD_3V3`；`caps=C1-C4 1uF` |
| 复位 | 摄像头 CAM_RST | `supervisor=U3 IMP809S/CN809S`；`supply=VDD_3V3`；`output=CAM_RST`；`pullup=R2 10KΩ`；`capacitor=C8 1uF`；`camera_pin=FPC1 pin6 RESET` |
| 核心器件 | 摄像头型号与成像性能 | `documented_model=OV3660`；`pin_table_model=OV3360(M12)`；`documented_resolution=3MP`；`documented_fps=30fps`；`documented_formats=RAW RGB,RGB565/555/444,CCIR656,YCbCr422,compression`；`documented_aperture=F2.4`；`documented_focal_length=1.8±5% mm`；`documented_fov=120°`；`schematic_model=null` |
| 总线地址 | BMI270/BMM150 地址 | `documented_bmi270=0x68`；`bmm150=null`；`topology=ESP32 SYS I2C -> BMI270 -> auxiliary I2C -> BMM150`；`schematic_addresses=null` |
| 内存与 Flash | 8MB Flash 与 8MB PSRAM | `part_number=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB`；`external_memory=null` |
| 射频 | 增强 3D 天线性能 | `antenna=ANT1 ESP-H0920-PIFA`；`matching=R1/C1/C2`；`gain=null`；`efficiency=null`；`range=null`；`certification=null` |
| 其他事实 | UVC 与 Wi-Fi 图传固件 | `documented_features=UVC,Wi-Fi image streaming`；`firmware_version=null`；`usb_descriptors=null`；`stream_fps=null` |

## 待确认事项

- `component.camera-model-performance`：正文描述和规格表称摄像头为 OV3660、3MP、30fps 并列出格式/F2.4/焦距/FOV，但管脚映射标题写作 OV3360(M12)；扩展板原理图只显示 FPC1 电气接口，没有摄像头芯片位号、型号或光学参数。（证据：图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页 FPC1 仅显示信号和电源，无 OV3660/OV3360 型号文字）
- `address.imu-addresses`：正文给出 BMI270 地址 0x68，并称 BMM150 挂载于 BMI270 Sensor Hub；原理图确认总线拓扑，但没有标出任何 7 位地址或 BMI270 地址选择状态。（证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页 U6 BMI270/U9 BMM150 总线，无地址文字）
- `memory.documented-n8r8`：主板原理图明确标 U1 为 ESP32-S3-PICO-1-N8R8，正文解释为 8MB Flash 和 8MB PSRAM；图中未单列存储容量字段或外部存储器，容量含义需由该 SiP datasheet 或实机确认。（证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页 U1 型号，图中无独立容量字段）
- `rf.documented-performance`：原理图确认 ANT1 PIFA 及匹配元件，但正文所称增强性能、稳定性、Wi-Fi 范围和认证结果没有在图中量化。（证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页 ANT1 匹配网络，无性能表）
- `other.documented-uvc-firmware`：正文描述出厂 UVC 和 Wi-Fi 图传功能；原理图只确认原生 USB、摄像头并口和 Wi-Fi 天线硬件，不能证明固件版本、USB 描述符、帧率或浏览器服务行为。（证据：图 f49bdafb26fd / 第 1 页 / 第 1 张第 1 页 USB/天线/主控硬件; 图 ad976aa0df7f / 第 1 页 / 第 2 张第 1 页摄像头接口硬件）
- `review.camera-bom-performance`：请用摄像头模组 BOM/丝印/datasheet 确认实际型号是 OV3660 还是 OV3360(M12)，并确认 3MP、帧率、格式和光学参数。；原因：正文与管脚映射命名冲突，且原理图只有 FPC 电气接口。
- `review.imu-addresses`：请确认 BMI270 的 7 位地址是否为 0x68，以及 BMM150 在 Sensor Hub 辅助总线上的地址和初始化方式。；原因：原理图未标地址。
- `review.memory-capacity`：请用 ESP32-S3-PICO-1-N8R8 datasheet 或实机确认 8MB Flash 和 8MB PSRAM。；原因：容量解释不作为板级原理图直接字段。
- `review.rf-performance`：ANT1 的增益、效率、匹配验证、辐射范围和认证结果是什么？；原因：原理图只确认器件和匹配网络。
- `review.uvc-firmware`：当前出厂固件的 UVC/Wi-Fi 图传版本、分辨率、帧率、USB 描述符和网络行为是什么？；原因：软件行为不能由原理图独立验证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f49bdafb26fd74eea17cd01f86c09f6aca443b63c24d1f5eb280b9f7da32f9d9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic_page_01.png` |
| 2 | 1 | `ad976aa0df7f263e73a6ce7dda91308f7f9e9cff3d15b03f7e1906afb0fd2a97` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic_page_01.png` |

---

源文档：`zh_CN/core/AtomS3R-M12.md`

源文档 SHA-256：`8a782038be9b8dfc3c423fa0c581eb814722c129a393e31ab905aaa0de0e55a1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
