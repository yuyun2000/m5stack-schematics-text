# CoreInk 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CoreInk |
| SKU | K048 |
| 产品 ID | `coreink-51c3aed4a6bc` |
| 源文档 | `zh_CN/core/coreink.md` |

## 概述

CoreInk 以 U1 ESP32-PICO-D4 SiP 为主控，通过 SPI 驱动 EPD1 电子墨水屏，并以 I2C 连接 U4 BM8563 RTC。USB Type-C 经 U2 CP2104 提供下载调试串口，M5-Bus、Grove 与 10 针 HAT FPC 引出电源和 GPIO。电源由 U6 TP4057 负责电池充电，U5 SY7088 生成 SYS_P050，U3 SY8089 生成 MCU_VDD，独立升压网络产生电子墨水屏 VGG/VEE 高压轨。

## 检索关键词

`CoreInk`、`K048`、`ESP32-PICO-D4`、`PICO_D4`、`CP2104-F03-GMR`、`BM8563`、`TP4057`、`SY7088`、`SY8089`、`EPD_SPI`、`E-Ink`、`GDEW0154M09`、`M5_BUS_16P_H7.1`、`USB Type-C`、`GROVE`、`HY2.0-4P`、`HAT CON10`、`SYS_BAT`、`BST_IN`、`SYS_P050`、`MCU_VDD`、`EXT_5V0`、`PWR_TRIG`、`MCU_RST`、`CP_TX`、`CP_RX`、`GPIO21 SDA`、`GPIO22 SCL`、`GPIO18 SCK`、`GPIO23 MOSI`、`GPIO9 EPD_CS`、`GPIO15 EPD_DC`、`GPIO4 EPD_BUSY`、`GPIO0 EPD_RST`、`32.768K`、`SRV05-4`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-D4 | 主控 SiP，连接射频、电子墨水屏、RTC、USB-UART、按键、蜂鸣器和扩展接口 | 图 7cd4730d0074 / 第 1 页 / 主原理图 A2-B2，U1 PICO_D4，GPIO0-GPIO39、LNA_IN、EN 与电源引脚 |
| U2 | CP2104-F03-GMR | USB 转 UART 桥，连接 SYS_DP/SYS_DM 与 ESP32 下载调试串口 | 图 7cd4730d0074 / 第 1 页 / 主原理图 C2 USB2UART 区，U2 CP2104-F03-GMR |
| U3 | SY8089 | 3.3V 降压转换器，从 SYS_P050 生成 MCU_VDD | 图 7cd4730d0074 / 第 1 页 / 主原理图 C3 3.3V DC-DC 区，U3 SY8089、L3 2.2uH、R39/R40 |
| U4 | BM8563 | 实时时钟，通过 GPIO21/GPIO22 I2C 连接主控并提供 CLKOUT/INT | 图 7cd4730d0074 / 第 1 页 / 主原理图 D3 RTC 区，U4 BM8563 与 X1 32.768K |
| U5 | SY7088 | 5V 升压转换器，从 BST_IN 生成 SYS_P050 | 图 7cd4730d0074 / 第 1 页 / 主原理图 C3 5V DC-DC 区，U5 SY7088、L2 2.2uH、R43/R44 |
| U6 | TP4057 | 单节电池线性充电控制器，CHG 输入连接 SYS_BAT 输出并带充电指示 | 图 7cd4730d0074 / 第 1 页 / 主原理图 B3 CHARGER 区，U6 TP4057、R45 5.1K、LED1 |
| EPD1 | EPD_SPI | 24 针电子墨水屏连接器，承载 SPI、BUSY/RESET 和 VGG/VEE/VCOM 等显示电源 | 图 7cd4730d0074 / 第 1 页 / 主原理图 B4 EPD_SPI 区，EPD1 1-24 脚及 SHELL_GND |
| BUS1 | M5_BUS_16P_H7.1 | 16 针 M5-Bus 扩展连接器，引出电池、5V、3.3V、复位、UART、I2C、SPI 与 GPIO | 图 7cd4730d0074 / 第 1 页 / 主原理图 A1 BUS 区，BUS1 M5_BUS_16P_H7.1，针脚 1-16 |
| J2 | TYPEC | USB Type-C 供电和 USB 2.0 数据接口 | 图 7cd4730d0074 / 第 1 页 / 主原理图 C1 USB TYPE-C 区，J2 TYPEC、CC1/CC2、DP/DM、USB_5V |
| J3 | GROVE | 4 针 Grove 连接器，提供 EXT_G33、EXT_G32、EXT_5V0 与 GND | 图 7cd4730d0074 / 第 1 页 / 主原理图 A4 GROVE 区，J3 针脚 1-4 与 SH |
| J1 | CON10 | 10 针 HAT FPC，连接 LED、KEY、扩展 GPIO 和多路电源 | 图 7cd4730d0074 / 第 1 页 / 主原理图 C1-D1 FPC TO HAT 区，J1 CON10 针脚 1-10 |
| U4 (CON2) | CON2 | 两针电池端口，连接 SYS_BAT 与 GND；图中连接器位号显示为 U4 | 图 7cd4730d0074 / 第 1 页 / 主原理图 D4 BATTERY PORT 区，U4/CON2，1 脚 SYS_BAT、2 脚 GND、SH GND |
| D1-D3 | SRV05-4 | 扩展 GPIO 与复位线的多通道 ESD 保护阵列 | 图 7cd4730d0074 / 第 1 页 / 主原理图 B1 ESD 区，D1-D3 SRV05-4 与 R6-R16 47R 串联电阻 |
| Q2/Q4 | SI2302/SI2301 | 电池升压输入的电源锁存和 PWR_TRIG 控制级 | 图 7cd4730d0074 / 第 1 页 / 主原理图 B3 PWR_SW&ADC 区，Q4 SI2301、Q2 SI2302、GPIO12、PWR_TRIG |
| Q1/BZ1 | S8050/BUZZER | GPIO2 控制的低边蜂鸣器驱动，带 D4 1N4148 续流二极管 | 图 7cd4730d0074 / 第 1 页 / 主原理图 D1 BUZZER 区，Q1 S8050、BZ1、D4 1N4148 |
| S1/S2/S3 | POWER/RESET/K1-15025A-02 | 电源、复位和三向多功能拨轮/按键输入 | 图 7cd4730d0074 / 第 1 页 / 主原理图 D2 BUTTONS 区，S1 POWER、S2 RESET、S3 MULTI-FUNCTION |
| ANT1/ANT2 | ANT1/IPEX | ESP32 射频天线端，带 L1/C4/C6 匹配网络和 IPEX 连接点 | 图 7cd4730d0074 / 第 1 页 / 主原理图 A2，U1 LNA_IN 至 L1 1.8nH、C4 1.5pF、C6 1.2pF、ANT1/ANT2 IPEX |
| L4/D15-D17 | 10uH/1N5819 | 电子墨水屏高压升压与整流网络，生成 VGG 和 VEE | 图 7cd4730d0074 / 第 1 页 / 主原理图 C4 EPD BOOST 区，L4 10uH、D15-D17 1N5819、VGG/VEE |

## 系统结构

### CoreInk 系统架构

ESP32-PICO-D4 SiP 连接 EPD、BM8563 RTC、CP2104 USB-UART、按键、蜂鸣器及 M5-Bus/Grove/HAT 扩展；电池充电、5V/3.3V 转换与 EPD 高压由独立电源分区完成。

- 参数与网络：`mcu=U1 ESP32-PICO-D4`；`display=EPD1 EPD_SPI`；`rtc=U4 BM8563`；`usb_uart=U2 CP2104-F03-GMR`；`power=TP4057 + SY7088 + SY8089 + EPD BOOST`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图完整页，BUS/MCU/USB2UART/PMU/EPD/RTC 等分区; 图 b0e23e40780f / 第 1 页 / 系统框图完整页，ESP32-PICO-D4 与 E-INK、RTC、CP2104、电源和扩展接口连接

## 核心器件

### U1 ESP32-PICO-D4

U1 为 ESP32-PICO-D4，EN 接 MCU_RST，GPIO0-GPIO39 分配给显示、RTC、UART、按键、蜂鸣器和扩展信号。

- 参数与网络：`reference=U1`；`part_number=ESP32-PICO-D4`；`reset_net=MCU_RST`；`power_net=MCU_VDD`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A2-B2，U1 PICO_D4

## 电源

### USB、扩展 5V 与电池电源汇合

USB_5V、EXT_5V1 与 SYS_BAT 通过 D8-D11 和 D9 等肖特基二极管形成 CHG、EXT_5V0 与 BST_IN 路径。

- 参数与网络：`usb_input=USB_5V`；`external_input=EXT_5V1`；`battery=SYS_BAT`；`charge_net=CHG`；`boost_input=BST_IN`；`diodes=D8/D11 1N5819; D9 1N5819; D10 SS34`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A3 PMU 区，USB_5V/SYS_BAT/EXT_5V0/CHG/BST_IN 与 D8-D11

### U6 TP4057 充电路径

U6 TP4057 的 VCC 接 CHG、BAT 接 SYS_BAT、PROG 接 R45 5.1K，CHG 状态脚驱动 LED1 充电指示。

- 参数与网络：`reference=U6`；`part_number=TP4057`；`input=CHG`；`battery_net=SYS_BAT`；`program_resistor=R45 5.1K`；`indicator=LED1 + R34 2K`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B3 CHARGER 区

### 电池连接器

BATTERY PORT 的 CON2 两针连接器将 1 脚接 SYS_BAT、2 脚接 GND，屏蔽脚 SH 接 GND。

- 参数与网络：`reference_as_drawn=U4`；`connector=CON2`；`pin_1=SYS_BAT`；`pin_2=GND`；`shield=GND`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D4 BATTERY PORT 区

### 电源锁存与控制

SYS_BAT 经 Q4 SI2301 向 BST_IN 供电，Q2 SI2302 的门极由 GPIO12 驱动，PWR_TRIG 与 GPIO35 参与开机触发和状态检测网络。

- 参数与网络：`high_side=Q4 SI2301`；`control_transistor=Q2 SI2302`；`hold_gpio=GPIO12`；`trigger_net=PWR_TRIG`；`sense_gpio=GPIO35`；`input=SYS_BAT`；`output=BST_IN`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B3 PWR_SW&ADC 区

### SYS_P050 5V 电源轨

U5 SY7088 以 BST_IN 为输入，经 L2 2.2uH 升压并由 R43 51K/R44 4.7K 反馈，输出网络标为 SYS_P050。

- 参数与网络：`reference=U5`；`part_number=SY7088`；`input=BST_IN`；`output=SYS_P050`；`inductor=L2 2.2uH`；`feedback=R43 51K; R44 4.7K`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C3 5V DC-DC 区

### MCU_VDD 3.3V 电源轨

U3 SY8089 从 SYS_P050 降压，经 L3 2.2uH 和 R39 22K/R40 5.1K 反馈生成 MCU_VDD；该分区标题标为 3.3V DC-DC。

- 参数与网络：`reference=U3`；`part_number=SY8089`；`input=SYS_P050`；`output=MCU_VDD`；`nominal_voltage=3.3V`；`inductor=L3 2.2uH`；`feedback=R39 22K; R40 5.1K`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C3 3.3V DC-DC 区

### 电子墨水屏 VGG/VEE 电源

EPD BOOST 区以 MCU_VDD 为输入，L4 10uH、开关管及 D15-D17 1N5819 产生 VGG 和 VEE，并接入 EPD1 PREVGH/PREVGL。

- 参数与网络：`input=MCU_VDD`；`control=EPD_CD`；`inductor=L4 10uH`；`diodes=D15-D17 1N5819`；`positive_rail=VGG`；`negative_rail=VEE`；`display_pins=EPD1-21 PREVGH; EPD1-23 PREVGL`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C4 EPD BOOST 区与 B4 EPD1 21/23 脚

## 接口

### J2 USB Type-C

J2 提供 USB_5V 输入和 USB 2.0 DP/DM；A6/B6 汇入 SYS_DP，A7/B7 汇入 SYS_DM，CC1/CC2 分别以 R3/R4 5.1K 下拉至 GND。

- 参数与网络：`reference=J2`；`power_pin=VCC -> USB_5V`；`data_plus=A6/B6 -> SYS_DP`；`data_minus=A7/B7 -> SYS_DM`；`cc1=R3 5.1K to GND`；`cc2=R4 5.1K to GND`；`direction=USB data bidirectional; VCC input`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C1 USB TYPE-C 区，J2

### BUS1 M5-Bus

BUS1 16 针接口引出 GND、SYS_BAT、5V 输入/输出、MCU_VDD、EXT_RST，以及 EXT_G13/G14/G21/G22/G18/G36/G34/G26/G23/G25。

- 参数与网络：`reference=BUS1`；`pin_1=GND`；`pin_2=SYS_BAT`；`pin_3=EXT_5V1`；`pin_4=EXT_5V0`；`pin_5=EXT_RST`；`pin_6=MCU_VDD`；`pin_7=EXT_G13`；`pin_8=EXT_G14`；`pin_9=EXT_G21`；`pin_10=EXT_G22`；`pin_11=EXT_G18`；`pin_12=EXT_G36`；`pin_13=EXT_G34`；`pin_14=EXT_G26`；`pin_15=EXT_G23`；`pin_16=EXT_G25`；`logic_level=MCU_VDD (3.3V)`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A1 BUS1 针脚 1-16

### J3 Grove

J3 的 1 脚和屏蔽脚接 GND，2 脚接 EXT_5V0，3 脚为 EXT_G32，4 脚为 EXT_G33；GPIO32/GPIO33 分别经 R48/R49 47R 串联。

- 参数与网络：`reference=J3`；`pin_1=GND`；`pin_2=EXT_5V0`；`pin_3=EXT_G32`；`pin_4=EXT_G33`；`shield=GND`；`series_resistors=R48/R49 47R`；`signal_direction=ESP32 GPIO bidirectional`；`logic_level=MCU_VDD (3.3V)`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A4 GROVE 区 J3 与 R48/R49

### J1 HAT FPC

J1 CON10 引出 GPIO10/LED、GPIO5/KEY、EXT_G26、EXT_G36、EXT_G25、SYS_BAT、MCU_VDD 及 5V 电源网络，外壳接 GND。

- 参数与网络：`reference=J1`；`pin_1=GPIO10 / LED`；`pin_2=GPIO5 / KEY`；`pin_4=EXT_5V0`；`pin_5=EXT_G26`；`pin_6=EXT_G36`；`pin_7=EXT_G25`；`pin_8=SYS_BAT`；`pin_9=MCU_VDD`；`pin_10=EXT_5V1`；`shield=GND`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C1-D1 FPC TO HAT 区，J1 CON10

## 总线

### CP2104 UART

U2 CP2104 的 USB D+/D- 接 SYS_DP/SYS_DM；TXD 网络 CP_TX 经 47R 接 ESP32 GPIO3/U0RXD，RXD 网络 CP_RX 经 47R 接 GPIO1/U0TXD。

- 参数与网络：`bridge=U2 CP2104-F03-GMR`；`usb=SYS_DP/SYS_DM`；`bridge_txd=CP_TX -> GPIO3/U0RXD`；`bridge_rxd=CP_RX <- GPIO1/U0TXD`；`series_resistors=R21/R22 47R`；`logic_rail=MCU_VDD`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C2 USB2UART 区，U2 TXD/RXD 与 CP_TX/CP_RX、R21/R22

### BM8563 I2C

U1 GPIO21/SDA 与 GPIO22/SCL 连接 U4 BM8563 的 SDA/SCL，并通过 R26/R27 2.2K 上拉至 MCU_VDD；同一信号也引出至 M5-Bus。

- 参数与网络：`controller=U1 ESP32-PICO-D4`；`device=U4 BM8563`；`sda=GPIO21 / EXT_G21`；`scl=GPIO22 / EXT_G22`；`pullups=R26/R27 2.2K to MCU_VDD`；`logic_level=3.3V`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A2 U1 GPIO21/22 与 R26/R27；D3 U4 SDA/SCL；A1 BUS1 pins 9/10

### 电子墨水屏 SPI

U1 以 GPIO18/SCK 和 GPIO23/MOSI 驱动 EPD1，GPIO9 为 CS#、GPIO15 为 D/C；该接口未画出 MISO 返回线。

- 参数与网络：`controller=U1 ESP32-PICO-D4`；`device=EPD1 EPD_SPI`；`sck=GPIO18 -> EPD1-13`；`mosi=GPIO23 -> EPD1-14`；`chip_select=GPIO9 -> EPD1-12 CS#`；`data_command=GPIO15 -> EPD1-11 D/C`；`miso=null`；`direction=MCU to display`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B4 EPD1 pins 11-14 与 A2 U1 GPIO9/15/18/23

## 总线地址

### BM8563 I2C 地址

两张原理图均未标注 BM8563 的数值 I2C 地址。

- 参数与网络：`device=U4 BM8563`；`bus=GPIO21 SDA / GPIO22 SCL`；`address_visible=false`；`address=null`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D3 RTC 区 U4 BM8563，未见地址标注; 图 b0e23e40780f / 第 1 页 / 系统框图 RTC:BM8563，未见地址标注

## GPIO 与控制信号

### EPD 控制 GPIO

EPD1 BUSY 接 GPIO4、RST# 接 GPIO0、D/C 接 GPIO15、CS# 接 GPIO9、SCK 接 GPIO18、MOSI 接 GPIO23。

- 参数与网络：`busy=EPD1-9 -> GPIO4 (display to MCU)`；`reset=EPD1-10 RST# <- GPIO0`；`dc=EPD1-11 D/C <- GPIO15`；`cs=EPD1-12 CS# <- GPIO9`；`sck=EPD1-13 <- GPIO18`；`mosi=EPD1-14 <- GPIO23`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B4 EPD1 pins 9-14

### 多功能拨轮与按键

S3 MULTI-FUNCTION 将 GPIO37、GPIO39、GPIO38 作为三路开关输入，各自带 10K 上拉至 MCU_VDD 和 0.1uF 对地电容；J1 KEY 信号另接 GPIO5。

- 参数与网络：`switch=S3 K1-15025A-02`；`input_1=GPIO37`；`input_2=GPIO39`；`input_3=GPIO38`；`pullups=R23/R24/R25 10K`；`filters=C5/C6/C7 0.1uF`；`user_key=J1-2 KEY -> GPIO5`；`direction=input`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D2 BUTTONS 区 S3 与 C5-C7/R23-R25；C1 J1 pins 1-2

### HAT LED 与 KEY

J1 HAT FPC 的 1 脚将 GPIO10 标为 LED，2 脚将 GPIO5 标为 KEY。

- 参数与网络：`led=J1-1 GPIO10 / LED (MCU output)`；`key=J1-2 GPIO5 / KEY (MCU input)`；`connector=J1 CON10`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C1 FPC TO HAT，J1 pins 1-2

## 时钟

### ESP32-PICO-D4 时钟

系统框图将 ESP32-PICO-D4 标注为 SiP 模块并标出晶振频率 40MHz。

- 参数与网络：`device=ESP32-PICO-D4`；`frequency=40MHz`；`integration=SIP MODULE`
- 证据：图 b0e23e40780f / 第 1 页 / 系统框图中央 ESP32-PICO-D4，SIP MODULE CRYSTAL:40MHz

### BM8563 RTC 晶振

U4 BM8563 的 OSCI/OSCO 连接 X1 32.768K 晶振；CLKOUT 经 D12 1N4148 接 GPIO19。

- 参数与网络：`rtc=U4 BM8563`；`crystal=X1`；`frequency=32.768K`；`clock_output=CLKOUT -> D12 1N4148 -> GPIO19`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D3 RTC 区 U4、X1、D12

## 复位

### ESP32 自动复位与 BOOT

CP2104 的 DTR/RTS 控制晶体管网络分别作用于 GPIO0 和 MCU_RST，GPIO0 带 R29 2.2K 上拉，MCU_RST 接 U1 EN。

- 参数与网络：`boot=GPIO0`；`reset=MCU_RST -> U1 EN`；`pullup=R29 2.2K to MCU_VDD`；`source=U2 DTR/RTS`；`diodes=D7/D8 1N4148`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C2 USB2UART 自动下载网络与 A2 U1 EN

### 手动电源与复位按键

S1 POWER 接入 PWR_TRIG 电源触发链路，S2 RESET 将 MCU_RST 拉低；MCU_RST 同时连接 U1 EN 和 M5-Bus EXT_RST。

- 参数与网络：`power_switch=S1 POWER -> PWR_TRIG`；`reset_switch=S2 RESET -> MCU_RST`；`mcu_pin=U1 EN`；`external_reset=BUS1-5 EXT_RST`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D2 BUTTONS 区 S1/S2，A2 U1 EN，A1 BUS1 pin 5

## 保护电路

### M5-Bus 信号保护

D1-D3 三颗 SRV05-4 保护 EXT_G13/G14/EXT_RST、EXT_G18/G21/G22/G36 与 EXT_G34/G26/G23/G25；各线在 MCU 与外部网之间串联 47R。

- 参数与网络：`devices=D1-D3 SRV05-4`；`protected_nets=EXT_G13, EXT_G14, EXT_RST, EXT_G18, EXT_G21, EXT_G22, EXT_G36, EXT_G34, EXT_G26, EXT_G23, EXT_G25`；`series_resistors=R6-R16 47R`；`rail=MCU_VDD/GND`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B1 ESD 区 D1-D3 与 R6-R16

## 关键网络

### RTC 唤醒电源触发

BM8563 的 INT 输出经 D13 1N4148 汇入 PWR_TRIG，形成 RTC 到电源锁存电路的唤醒路径。

- 参数与网络：`source=U4 INT`；`diode=D13 1N4148`；`destination=PWR_TRIG`；`function=power trigger/wakeup`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D3 RTC 区 U4 INT、D13、PWR_TRIG 与 B3 PWR_SW&ADC

## 音频

### 蜂鸣器驱动

GPIO2 经 R2 2.2K 驱动 Q1 S8050 低边开关，BZ1 从 EXT_5V0 经 R5 4.7R 供电，D4 1N4148 跨接蜂鸣器支路。

- 参数与网络：`gpio=GPIO2`；`base_resistor=R2 2.2K`；`transistor=Q1 S8050`；`buzzer=BZ1`；`supply=EXT_5V0 via R5 4.7R`；`flyback_diode=D4 1N4148`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 D1 BUZZER 区

## 射频

### ESP32 射频路径

U1 LNA_IN 经 L1 1.8nH 与 C4 1.5pF、C6 1.2pF 匹配网络连接 ANT1，并并列标出 ANT2 IPEX 射频点。

- 参数与网络：`source_pin=U1 LNA_IN`；`inductor=L1 1.8nH`；`capacitors=C4 1.5pF; C6 1.2pF`；`antenna=ANT1`；`connector=ANT2 IPEX`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A2 射频匹配网络与 ANT1/ANT2

## 调试与烧录

### USB 下载与调试路径

J2 USB 数据经 U2 CP2104 转换为 ESP32 UART0，U2 DTR/RTS 再通过 Q5/Q6、D7/D8 和电阻网络控制 GPIO0 与 MCU_RST，实现自动下载复位。

- 参数与网络：`connector=J2`；`bridge=U2 CP2104-F03-GMR`；`uart=GPIO1/GPIO3`；`boot_pin=GPIO0`；`reset_net=MCU_RST`；`control_pins=DTR/RTS`；`transistors=Q5/Q6`
- 证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C2 USB2UART 右侧自动下载电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CoreInk 系统架构 | `mcu=U1 ESP32-PICO-D4`；`display=EPD1 EPD_SPI`；`rtc=U4 BM8563`；`usb_uart=U2 CP2104-F03-GMR`；`power=TP4057 + SY7088 + SY8089 + EPD BOOST` |
| 核心器件 | U1 ESP32-PICO-D4 | `reference=U1`；`part_number=ESP32-PICO-D4`；`reset_net=MCU_RST`；`power_net=MCU_VDD` |
| 内存与 Flash | ESP32-PICO-D4 Flash | `package=ESP32-PICO-D4 SiP`；`documented_capacity=4MB`；`schematic_capacity_label=null`；`discrete_flash_reference=null` |
| 射频 | ESP32 射频路径 | `source_pin=U1 LNA_IN`；`inductor=L1 1.8nH`；`capacitors=C4 1.5pF; C6 1.2pF`；`antenna=ANT1`；`connector=ANT2 IPEX` |
| 时钟 | ESP32-PICO-D4 时钟 | `device=ESP32-PICO-D4`；`frequency=40MHz`；`integration=SIP MODULE` |
| 电源 | USB、扩展 5V 与电池电源汇合 | `usb_input=USB_5V`；`external_input=EXT_5V1`；`battery=SYS_BAT`；`charge_net=CHG`；`boost_input=BST_IN`；`diodes=D8/D11 1N5819; D9 1N5819; D10 SS34` |
| 电源 | U6 TP4057 充电路径 | `reference=U6`；`part_number=TP4057`；`input=CHG`；`battery_net=SYS_BAT`；`program_resistor=R45 5.1K`；`indicator=LED1 + R34 2K` |
| 电源 | 电池连接器 | `reference_as_drawn=U4`；`connector=CON2`；`pin_1=SYS_BAT`；`pin_2=GND`；`shield=GND` |
| 电源 | 电源锁存与控制 | `high_side=Q4 SI2301`；`control_transistor=Q2 SI2302`；`hold_gpio=GPIO12`；`trigger_net=PWR_TRIG`；`sense_gpio=GPIO35`；`input=SYS_BAT`；`output=BST_IN` |
| 电源 | SYS_P050 5V 电源轨 | `reference=U5`；`part_number=SY7088`；`input=BST_IN`；`output=SYS_P050`；`inductor=L2 2.2uH`；`feedback=R43 51K; R44 4.7K` |
| 电源 | MCU_VDD 3.3V 电源轨 | `reference=U3`；`part_number=SY8089`；`input=SYS_P050`；`output=MCU_VDD`；`nominal_voltage=3.3V`；`inductor=L3 2.2uH`；`feedback=R39 22K; R40 5.1K` |
| 电源 | 电子墨水屏 VGG/VEE 电源 | `input=MCU_VDD`；`control=EPD_CD`；`inductor=L4 10uH`；`diodes=D15-D17 1N5819`；`positive_rail=VGG`；`negative_rail=VEE`；`display_pins=EPD1-21 PREVGH; EPD1-23 PREVGL` |
| 接口 | J2 USB Type-C | `reference=J2`；`power_pin=VCC -> USB_5V`；`data_plus=A6/B6 -> SYS_DP`；`data_minus=A7/B7 -> SYS_DM`；`cc1=R3 5.1K to GND`；`cc2=R4 5.1K to GND`；`direction=USB data bidirectional; VCC input` |
| 总线 | CP2104 UART | `bridge=U2 CP2104-F03-GMR`；`usb=SYS_DP/SYS_DM`；`bridge_txd=CP_TX -> GPIO3/U0RXD`；`bridge_rxd=CP_RX <- GPIO1/U0TXD`；`series_resistors=R21/R22 47R`；`logic_rail=MCU_VDD` |
| 调试与烧录 | USB 下载与调试路径 | `connector=J2`；`bridge=U2 CP2104-F03-GMR`；`uart=GPIO1/GPIO3`；`boot_pin=GPIO0`；`reset_net=MCU_RST`；`control_pins=DTR/RTS`；`transistors=Q5/Q6` |
| 复位 | ESP32 自动复位与 BOOT | `boot=GPIO0`；`reset=MCU_RST -> U1 EN`；`pullup=R29 2.2K to MCU_VDD`；`source=U2 DTR/RTS`；`diodes=D7/D8 1N4148` |
| 接口 | BUS1 M5-Bus | `reference=BUS1`；`pin_1=GND`；`pin_2=SYS_BAT`；`pin_3=EXT_5V1`；`pin_4=EXT_5V0`；`pin_5=EXT_RST`；`pin_6=MCU_VDD`；`pin_7=EXT_G13`；`pin_8=EXT_G14`；`pin_9=EXT_G21`；`pin_10=EXT_G22`；`pin_11=EXT_G18`；`pin_12=EXT_G36`；`pin_13=EXT_G34`；`pin_14=EXT_G26`；`pin_15=EXT_G23`；`pin_16=EXT_G25`；`logic_level=MCU_VDD (3.3V)` |
| 接口 | J3 Grove | `reference=J3`；`pin_1=GND`；`pin_2=EXT_5V0`；`pin_3=EXT_G32`；`pin_4=EXT_G33`；`shield=GND`；`series_resistors=R48/R49 47R`；`signal_direction=ESP32 GPIO bidirectional`；`logic_level=MCU_VDD (3.3V)` |
| 接口 | J1 HAT FPC | `reference=J1`；`pin_1=GPIO10 / LED`；`pin_2=GPIO5 / KEY`；`pin_4=EXT_5V0`；`pin_5=EXT_G26`；`pin_6=EXT_G36`；`pin_7=EXT_G25`；`pin_8=SYS_BAT`；`pin_9=MCU_VDD`；`pin_10=EXT_5V1`；`shield=GND` |
| 总线 | BM8563 I2C | `controller=U1 ESP32-PICO-D4`；`device=U4 BM8563`；`sda=GPIO21 / EXT_G21`；`scl=GPIO22 / EXT_G22`；`pullups=R26/R27 2.2K to MCU_VDD`；`logic_level=3.3V` |
| 总线地址 | BM8563 I2C 地址 | `device=U4 BM8563`；`bus=GPIO21 SDA / GPIO22 SCL`；`address_visible=false`；`address=null` |
| 时钟 | BM8563 RTC 晶振 | `rtc=U4 BM8563`；`crystal=X1`；`frequency=32.768K`；`clock_output=CLKOUT -> D12 1N4148 -> GPIO19` |
| 关键网络 | RTC 唤醒电源触发 | `source=U4 INT`；`diode=D13 1N4148`；`destination=PWR_TRIG`；`function=power trigger/wakeup` |
| 总线 | 电子墨水屏 SPI | `controller=U1 ESP32-PICO-D4`；`device=EPD1 EPD_SPI`；`sck=GPIO18 -> EPD1-13`；`mosi=GPIO23 -> EPD1-14`；`chip_select=GPIO9 -> EPD1-12 CS#`；`data_command=GPIO15 -> EPD1-11 D/C`；`miso=null`；`direction=MCU to display` |
| GPIO 与控制信号 | EPD 控制 GPIO | `busy=EPD1-9 -> GPIO4 (display to MCU)`；`reset=EPD1-10 RST# <- GPIO0`；`dc=EPD1-11 D/C <- GPIO15`；`cs=EPD1-12 CS# <- GPIO9`；`sck=EPD1-13 <- GPIO18`；`mosi=EPD1-14 <- GPIO23` |
| 核心器件 | 电子墨水屏具体型号 | `schematic_label=EPD1 EPD_SPI`；`documented_model=GDEW0154M09`；`documented_resolution=200x200`；`documented_size=1.54 inch` |
| GPIO 与控制信号 | 多功能拨轮与按键 | `switch=S3 K1-15025A-02`；`input_1=GPIO37`；`input_2=GPIO39`；`input_3=GPIO38`；`pullups=R23/R24/R25 10K`；`filters=C5/C6/C7 0.1uF`；`user_key=J1-2 KEY -> GPIO5`；`direction=input` |
| 复位 | 手动电源与复位按键 | `power_switch=S1 POWER -> PWR_TRIG`；`reset_switch=S2 RESET -> MCU_RST`；`mcu_pin=U1 EN`；`external_reset=BUS1-5 EXT_RST` |
| 音频 | 蜂鸣器驱动 | `gpio=GPIO2`；`base_resistor=R2 2.2K`；`transistor=Q1 S8050`；`buzzer=BZ1`；`supply=EXT_5V0 via R5 4.7R`；`flyback_diode=D4 1N4148` |
| GPIO 与控制信号 | HAT LED 与 KEY | `led=J1-1 GPIO10 / LED (MCU output)`；`key=J1-2 GPIO5 / KEY (MCU input)`；`connector=J1 CON10` |
| 保护电路 | M5-Bus 信号保护 | `devices=D1-D3 SRV05-4`；`protected_nets=EXT_G13, EXT_G14, EXT_RST, EXT_G18, EXT_G21, EXT_G22, EXT_G36, EXT_G34, EXT_G26, EXT_G23, EXT_G25`；`series_resistors=R6-R16 47R`；`rail=MCU_VDD/GND` |
| 核心器件 | USB-UART 硬件批次 | `schematic_part=CP2104-F03-GMR`；`documented_variant=CH9102`；`variant_schematic_available=false` |

## 待确认事项

- `memory.flash-capacity`：主原理图未放置独立 Flash 器件；产品正文标称 4MB Flash，但该容量未在两张原理图中标注。（证据：图 7cd4730d0074 / 第 1 页 / 主原理图 A2-B2 U1 PICO_D4；整页无独立 Flash 位号; 图 b0e23e40780f / 第 1 页 / 系统框图中央 ESP32-PICO-D4 SIP MODULE，未标 Flash 容量）
- `component.epd-model`：产品正文称屏幕为 GDEW0154M09、200x200、1.54 英寸，但原理图连接器仅标 EPD_SPI，未标出面板型号和分辨率。（证据：图 7cd4730d0074 / 第 1 页 / 主原理图 B4 EPD1 仅标 EPD_SPI; 图 b0e23e40780f / 第 1 页 / 系统框图仅标 E-INK，未标面板型号或分辨率）
- `component.usb-uart-variant`：本地原理图明确画出 U2 CP2104-F03-GMR；产品正文同时提示存在 CH9102 驱动芯片版本，但未提供对应本地原理图，无法确认其电路与本图是否完全等价。（证据：图 7cd4730d0074 / 第 1 页 / 主原理图 C2 U2 明确标 CP2104-F03-GMR; 图 b0e23e40780f / 第 1 页 / 系统框图 USB-UART 模块明确标 CP2104）
- `review.flash-capacity`：当前 CoreInk K048 硬件批次的 ESP32-PICO-D4 内部 Flash 容量是否固定为 4MB？；原因：4MB 来自产品正文，两个原理图资源均未标出 Flash 容量。
- `review.epd-model`：本原理图对应的 EPD1 面板是否确定为 GDEW0154M09、200x200、1.54 英寸？；原因：型号和规格来自产品正文，原理图只标 EPD_SPI/E-INK。
- `review.usb-uart-variant`：CH9102 批次是否有独立原理图，且其自动下载、供电和 UART 网络是否与当前 CP2104 图一致？；原因：现有两张原理图均只显示 CP2104，无法验证产品正文提到的 CH9102 批次。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7cd4730d0074fdbab3d21193e52cda999831ba42cd0b504c679431a194a588a3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/coreink_sch_page_01.png` |
| 2 | 1 | `b0e23e40780f602b19469bc70a064f8869bcb46c4bc862153ff8b06a6f32cbec` | `https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_sch_01.webp` |

---

源文档：`zh_CN/core/coreink.md`

源文档 SHA-256：`752f7bf40c22ea39aa1bc54fe24bc7b5c8796d37f6738ad5951826811a6cd7e7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
