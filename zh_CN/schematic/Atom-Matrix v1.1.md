# Atom-Matrix v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom-Matrix v1.1 |
| SKU | C008-B-V11 |
| 产品 ID | `atom-matrix-v1-1-055d78a9ea4e` |
| 源文档 | `zh_CN/core/Atom-Matrix_v1.1.md` |

## 概述

Atom-Matrix v1.1 的主控资源是 M5 ATOM Matrix 功能框图，显示 ESP32-PICO、USB Type-C/USB-UART 自动下载、5V 到 3.3V 电源、Grove、用户/复位按键和底部扩展引脚。灯板资源 ATOM KEYPAD V1.2 以 U2 BMI270 为 0x68 I2C 设备，SCL/SDA 分别接 GPIO21/GPIO25，并由 GPIO27 驱动 25 颗串联 WS2812B 的 5×5 点阵。灯板 P1 同时传送 WS2812、5V、GND、SCL、SDA 与 3.3V。正文所列 ESP32-PICO-D4、4MB Flash、无线/3D 天线、IR G12、WS2812C-2020 和功耗参数未在两页中完整或一致地标注，保留待确认。

## 检索关键词

`Atom-Matrix v1.1`、`C008-B-V11`、`M5 ATOM Matrix`、`ESP32-PICO`、`ESP32-PICO-D4`、`BMI270`、`BMI270 0x68`、`WS2812B`、`WS2812C-2020`、`5x5 RGB Matrix`、`GPIO27`、`GPIO39`、`GPIO21`、`GPIO25`、`GPIO26`、`GPIO32`、`GPIO12`、`SCL`、`SDA`、`WS2812`、`USB Type-C`、`USB 2 UART`、`Auto Download`、`DC-DC 5V to 3.3V`、`GROVE`、`Reset Button`、`User Button`、`P1`、`TP1`、`TP7`、`VCC_5V`、`3.3V`、`4MB Flash`、`2.4GHz Wi-Fi`、`3D antenna`、`ATOM KEYPAD V1.2`、`IIC Adress 0x68`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ESP32-PICO block | ESP32-PICO | 功能框图主控，连接 USB-UART、BMI270、RGB 点阵、按键、Grove 与底部扩展引脚 | 图 f3a7bfae8cbf / 第 1 页 / 主控页中央橙色 ESP32-PICO 方框 |
| U2 | BMI270 | 0x68 六轴 IMU，使用 GPIO21/GPIO25 I2C | 图 729264655058 / 第 1 页 / 灯板页网格 A2-B3，U2 BMI270 与 IIC Adress:0X68 |
| LED1-LED25 | WS2812B | 5V 供电、串联形成 5×5 点阵的 25 颗可寻址 RGB LED | 图 729264655058 / 第 1 页 / 灯板页网格 A3-D6，LED1-LED25 WS2812B |
| P1 | 7-pin board connector | 灯板接口，承载 WS2812、+5V、GND、SCL、SDA、+3.3V 与一脚 NC | 图 729264655058 / 第 1 页 / 灯板页网格 B1-B2，P1 pins1-7 |
| R1,R2 | 4.7KΩ / 4.7KΩ | BMI270 SDA/SCL 上拉到 3.3V | 图 729264655058 / 第 1 页 / 灯板页网格 A1-A2，R1/R2、SDA/SCL |
| USB Type-C block | 未标注 | 框图中的 5V 与 USB DM/DP 输入接口 | 图 f3a7bfae8cbf / 第 1 页 / 主控页左下 USB Type-C 方框 |
| USB 2 UART block | 未标注 | USB DM/DP 到 ESP32 EN/GPIO0/TXD(GPIO1)/RXD(GPIO3) 的自动下载接口 | 图 f3a7bfae8cbf / 第 1 页 / 主控页左下 USB 2 UART & Auto Download 方框 |
| DC-DC block | 未标注 | 框图中的 5V 到 3.3V 电源转换 | 图 f3a7bfae8cbf / 第 1 页 / 主控页 DC-DC 5V To 3.3V 方框及 0.5A FUSE |
| GROVE block | 未标注 | GPIO32/GPIO26/5V/GND 四线 Grove 接口 | 图 f3a7bfae8cbf / 第 1 页 / 主控页左侧 GROVE 方框 |
| Reset Button,User Button | 未标注 | 复位按键与 GPIO39 低有效用户按键 | 图 f3a7bfae8cbf / 第 1 页 / 主控页左上 Reset Button/User Button 方框 |

## 系统结构

### Atom-Matrix v1.1 架构

ESP32-PICO 功能块连接 USB-UART、电源、Grove、按键、BMI270 与 5×5 RGB 灯板；灯板以 P1 集中连接主板。

- 参数与网络：`controller=ESP32-PICO block`；`imu=U2 BMI270`；`matrix=LED1-LED25`；`usb=USB Type-C/USB 2 UART`；`grove=GPIO32/GPIO26`；`board_link=P1`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页完整功能框图; 图 729264655058 / 第 1 页 / 灯板页完整 BMI270/P1/25 LED 电路

## 电源

### RGB 点阵 5V 供电

LED1-LED25 VDD 均接 VCC_5V，GND 接地；C4-C23 为分布式 100nF 去耦，P1 pin2/TP2 引出 5V，pin3/TP3 为 GND。

- 参数与网络：`rail=VCC_5V`；`loads=LED1-LED25`；`decoupling=C4-C23 100nF`；`connector=P1 pin2 +5V,pin3 GND`；`testpoints=TP2 5V,TP3 GND`
- 证据：图 729264655058 / 第 1 页 / 灯板页全部 LED VDD/GND、C4-C23、P1/TP2/TP3

### 主控 5V 到 3.3V 电源

主控框图显示 USB Type-C 经二极管与 0.5A FUSE 进入 5V 网络，DC-DC 5V To 3.3V 向 ESP32-PICO 提供 3.3V；Grove 也连接同一 5V。

- 参数与网络：`usb_source=USB Type-C`；`series=diode and 0.5A fuse`；`five_volt=5V`；`converter=DC-DC 5V To 3.3V`；`output=3.3V`；`alternate_source=Grove 5V`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 USB/Grove/Diode/0.5A FUSE/DC-DC 电源路径

## 接口

### 灯板 P1 针脚

P1 pin1=WS2812、pin2=+5V、pin3=GND、pin4=SCL、pin5=SDA、pin6=+3.3V、pin7 未连接。

- 参数与网络：`pin1=WS2812`；`pin2=+5V`；`pin3=GND`；`pin4=SCL`；`pin5=SDA`；`pin6=+3.3V`；`pin7=NC`
- 证据：图 729264655058 / 第 1 页 / 灯板页网格 B1-B2，P1 pins1-7

### Grove 接口

主控框图显示 Grove 四线为 GPIO32、GPIO26、5V、GND。

- 参数与网络：`signal1=GPIO32`；`signal2=GPIO26`；`power=5V`；`ground=GND`；`directions=not marked`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页左侧 GROVE 方框

### 底部扩展引脚

主控框图底部连接器左侧引出 GPIO21、GPIO25、5V、GND，右侧引出 3V3、GPIO22、GPIO19、GPIO23、GPIO33；另有 GPIO34 经 100Ω 连接到右侧网络。

- 参数与网络：`left=GPIO21,GPIO25,5V,GND`；`right=3V3,GPIO22,GPIO19,GPIO23,GPIO33`；`series=GPIO34 through 100R`；`view=Top view`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页右下 Connector (Top view) 与 GPIO34/100Ω

## 总线

### BMI270 I2C 映射

U2 SCK pin13 接 SCL，SDx pin14 接 SDA；R2/R1 各 4.7KΩ上拉至 3.3V，P1 pins4/5 和 TP4/TP5 引出 SCL/SDA。主控框图映射 SCL=GPIO21、SDA=GPIO25。

- 参数与网络：`scl=GPIO21/SCL -> U2 pin13`；`sda=GPIO25/SDA -> U2 pin14`；`pullups=R2 SCL 4.7K,R1 SDA 4.7K`；`connector=P1 pin4 SCL,pin5 SDA`；`testpoints=TP4 GPIO21,TP5 GPIO25`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 ESP32-PICO 到 BMI270 SDA/SCL 与 GPIO21/GPIO25; 图 729264655058 / 第 1 页 / 灯板页 U2/R1/R2/P1/TP4/TP5

## 总线地址

### BMI270 I2C 地址

灯板页明确标注 IIC Adress:0X68；U2 SDO pin1 接 GND、CSB pin12 接 3.3V。

- 参数与网络：`device=U2 BMI270`；`address_7bit=0x68`；`sdo=GND`；`csb=+3.3V`；`mode=I2C`
- 证据：图 729264655058 / 第 1 页 / 灯板页 U2 BMI270、SDO/CSB 与 0X68 标注

## GPIO 与控制信号

### GPIO27 5×5 RGB 数据链

GPIO27/WS2812 从 P1 pin1 和 TP1 进入 LED1 DI，LED1-LED25 逐级 DO 到下一颗 DI，LED25 DO 输出 H5/TP7。

- 参数与网络：`gpio=GPIO27`；`net=WS2812`；`first=LED1 DI`；`last=LED25 DO -> H5`；`count=25`；`layout=5x5`；`connector=P1 pin1`；`testpoints=TP1 GPIO27,TP7 H5`
- 证据：图 729264655058 / 第 1 页 / 灯板页 P1/TP1、LED1-LED25 与 H5/TP7

### 用户按键

User Button 在主控框图中连接 GPIO39 与 GND，按下形成低电平。

- 参数与网络：`gpio=GPIO39`；`other_terminal=GND`；`active_level=low`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页左上 User Button/GPIO39/GND

## 复位

### 复位按键

Reset Button 连接标为 RESET 的网络并进入 ESP32-PICO 方框；页面未给 EN 引脚号、上拉或 RC 参数。

- 参数与网络：`control=Reset Button`；`net=RESET`；`target=ESP32-PICO`；`pullup=null`；`capacitor=null`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页左上 Reset Button/RESET 到 ESP32-PICO

## 传感器

### BMI270 电源与中断

BMI270 VDD/VDDIO 接 3.3V，C1/C2 各 100nF 去耦；INT1/INT2、ASDx/ASCx、OCSB/OSDO 均未连接。

- 参数与网络：`supply=VDD/VDDIO=3.3V`；`decoupling=C1/C2 100nF`；`int1=NC`；`int2=NC`；`aux_interface=NC`
- 证据：图 729264655058 / 第 1 页 / 灯板页 U2 全部引脚与 C1/C2

## 调试与烧录

### USB-UART 自动下载

USB Type-C DM/DP 进入 USB 2 UART & Auto Download 方框，后者连接 ESP32-PICO EN、GPIO0、TXD(GPIO1)、RXD(GPIO3)。

- 参数与网络：`usb=DM/DP`；`bridge=USB 2 UART & Auto Download`；`reset=EN`；`boot=GPIO0`；`uart_tx=GPIO1`；`uart_rx=GPIO3`
- 证据：图 f3a7bfae8cbf / 第 1 页 / 主控页左下 USB Type-C/USB 2 UART/ESP32-PICO

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom-Matrix v1.1 架构 | `controller=ESP32-PICO block`；`imu=U2 BMI270`；`matrix=LED1-LED25`；`usb=USB Type-C/USB 2 UART`；`grove=GPIO32/GPIO26`；`board_link=P1` |
| 总线地址 | BMI270 I2C 地址 | `device=U2 BMI270`；`address_7bit=0x68`；`sdo=GND`；`csb=+3.3V`；`mode=I2C` |
| 总线 | BMI270 I2C 映射 | `scl=GPIO21/SCL -> U2 pin13`；`sda=GPIO25/SDA -> U2 pin14`；`pullups=R2 SCL 4.7K,R1 SDA 4.7K`；`connector=P1 pin4 SCL,pin5 SDA`；`testpoints=TP4 GPIO21,TP5 GPIO25` |
| 传感器 | BMI270 电源与中断 | `supply=VDD/VDDIO=3.3V`；`decoupling=C1/C2 100nF`；`int1=NC`；`int2=NC`；`aux_interface=NC` |
| GPIO 与控制信号 | GPIO27 5×5 RGB 数据链 | `gpio=GPIO27`；`net=WS2812`；`first=LED1 DI`；`last=LED25 DO -> H5`；`count=25`；`layout=5x5`；`connector=P1 pin1`；`testpoints=TP1 GPIO27,TP7 H5` |
| 电源 | RGB 点阵 5V 供电 | `rail=VCC_5V`；`loads=LED1-LED25`；`decoupling=C4-C23 100nF`；`connector=P1 pin2 +5V,pin3 GND`；`testpoints=TP2 5V,TP3 GND` |
| 接口 | 灯板 P1 针脚 | `pin1=WS2812`；`pin2=+5V`；`pin3=GND`；`pin4=SCL`；`pin5=SDA`；`pin6=+3.3V`；`pin7=NC` |
| 接口 | Grove 接口 | `signal1=GPIO32`；`signal2=GPIO26`；`power=5V`；`ground=GND`；`directions=not marked` |
| 接口 | 底部扩展引脚 | `left=GPIO21,GPIO25,5V,GND`；`right=3V3,GPIO22,GPIO19,GPIO23,GPIO33`；`series=GPIO34 through 100R`；`view=Top view` |
| GPIO 与控制信号 | 用户按键 | `gpio=GPIO39`；`other_terminal=GND`；`active_level=low` |
| 复位 | 复位按键 | `control=Reset Button`；`net=RESET`；`target=ESP32-PICO`；`pullup=null`；`capacitor=null` |
| 调试与烧录 | USB-UART 自动下载 | `usb=DM/DP`；`bridge=USB 2 UART & Auto Download`；`reset=EN`；`boot=GPIO0`；`uart_tx=GPIO1`；`uart_rx=GPIO3` |
| 电源 | 主控 5V 到 3.3V 电源 | `usb_source=USB Type-C`；`series=diode and 0.5A fuse`；`five_volt=5V`；`converter=DC-DC 5V To 3.3V`；`output=3.3V`；`alternate_source=Grove 5V` |
| 系统结构 | 资源图版本与详细程度 | `product=Atom-Matrix v1.1`；`main_title=M5 ATOM Matrix`；`main_type=functional block diagram`；`lamp_revision=V1.2`；`complete_bom=null` |
| 内存与 Flash | 正文 PICO-D4 与存储 | `documented_soc=ESP32-PICO-D4`；`schematic_label=ESP32-PICO`；`documented_sram=520KB`；`documented_flash=4MB`；`flash_part=null`；`flash_bus=null` |
| 射频 | 正文 Wi-Fi 与 3D 天线 | `documented_radio=2.4GHz Wi-Fi`；`documented_antenna=2.4G 3D antenna`；`antenna_part=null`；`matching_network=null`；`rf_clock=null`；`certification=null` |
| GPIO 与控制信号 | 正文红外发射 | `documented_gpio=GPIO12`；`ir_led=null`；`driver=null`；`current_resistor=null`；`protection=null` |
| 核心器件 | RGB LED 型号差异 | `documented=WS2812C-2020`；`lamp_schematic=WS2812B`；`block_diagram=WS2812-2020`；`production_part=null` |
| 电源 | 正文输入与功耗 | `documented_input=5V@500mA`；`documented_consumption=5V@61.65mA`；`fuse=0.5A annotation`；`input_range=null`；`led_brightness=null`；`measurement_conditions=null` |

## 待确认事项

- `system.resource-version-detail`：主控资源标题仅为 M5 ATOM Matrix 且为功能框图，灯板图框为 ATOM KEYPAD Revision V1.2；两页未提供完整主控器件位号/BOM。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页标题与功能块; 图 729264655058 / 第 1 页 / 灯板页右下 ATOM KEYPAD Revision V1.2）
- `component.documented-soc-memory`：正文称 SoC 为 ESP32-PICO-D4、SRAM 520KB、Flash 4MB；主控框图只标 ESP32-PICO，没有 D4 后缀、存储器型号、总线或容量。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 ESP32-PICO 方框，无存储信息）
- `rf.documented-wireless-antenna`：正文列出 2.4GHz Wi-Fi 与 2.4G 3D 天线；两页均未显示射频引脚、天线、匹配网络、晶振或认证信息。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 ESP32-PICO 方框，无 RF/天线）
- `gpio.documented-ir`：正文管脚表称 IR_TX 使用 GPIO12；主控框图与灯板原理图均未显示红外 LED、GPIO12、驱动晶体管、限流电阻或保护。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页完整框图，无 IR; 图 729264655058 / 第 1 页 / 灯板页完整电路，无 IR）
- `component.led-part-conflict`：正文规格称 25 颗 WS2812C-2020，灯板原理图 LED1-LED25 均标 WS2812B，主控框图写 5X5 WS2812-2020 Matrix；当前资料无法确认量产料号。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 5X5 WS2812-2020 Matrix; 图 729264655058 / 第 1 页 / 灯板页 LED1-LED25 WS2812B）
- `power.documented-consumption`：正文称输入 5V@500mA、整机功耗 5V@61.65mA；框图只标 0.5A 保险丝和电源拓扑，没有输入容差、各轨电流、LED 亮度或测量条件。（证据：图 f3a7bfae8cbf / 第 1 页 / 主控页 0.5A FUSE/DC-DC 与灯板，无功耗条件）
- `review.resource-version`：请提供 Atom-Matrix v1.1 当前完整主控原理图/BOM，确认主控框图和灯板 V1.2 的组合版本。；原因：主控资源是无位号功能框图。
- `review.soc-memory`：请确认 ESP32-PICO-D4、4MB Flash、520KB SRAM 的当前料号和存储实现。；原因：框图只标 ESP32-PICO。
- `review.rf`：请确认 Wi-Fi 射频、3D 天线、匹配网络、布局和认证。；原因：两页无 RF 证据。
- `review.ir`：请确认 GPIO12 红外发射器件、驱动、限流、波长、载波和最大占空比。；原因：原理图资源未显示 IR 电路。
- `review.led-part`：请由量产 BOM 确认 25 颗 RGB LED 是 WS2812B、WS2812C-2020 还是其他兼容料号。；原因：正文、框图和灯板型号不一致。
- `review.power`：请确认输入容差、保险丝规格、各电源轨与 LED 亮度条件下的 61.65mA 功耗。；原因：框图没有实测条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f3a7bfae8cbff537c2eaf1a6de5091bdd4279ac2bd072056d7b9b294c5115406` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/SCH_Atom_Matrix_V1_1.png` |
| 2 | 1 | `72926465505862437891fc3049ec4e5e291fe2b0c24dee0ece7862333bef3a2b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/SCH_ATOM_KEYPAD_V1.2_20251211_2025_12_13_11_18_14_page_01.png` |

---

源文档：`zh_CN/core/Atom-Matrix_v1.1.md`

源文档 SHA-256：`708997d021d066aafb7f57a71dce262beb50855bcd312e4a674b8ceb4e41a268`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
