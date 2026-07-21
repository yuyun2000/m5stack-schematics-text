# Atom Display 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Display |
| SKU | K115 |
| 产品 ID | `atom-display-10d88169847b` |
| 源文档 | `zh_CN/atom/atom_display.md` |

## 概述

现有两张本地原理图完整覆盖 Atom PSRAM 控制器部分：U1 ESP32-V3-02 连接 Atom 4/5 Pin、Grove、按键、复位、WS2812B RGB LED 与板载/可选 IPEX 天线。第二张页面显示 USB Type-C 经 FUSE1 形成 VUSB_5V，U2 SY8089 将其转换为 VCC_3V3，U3 CP2104 提供 USB-UART，并通过 U5A/U5B 自动控制 ESP32_EN 与 GPIO0。两张资源均未出现产品正文提到的 GW1NR-9C FPGA、LT8618SX 或显示输出连接器，因此 Display Base 子系统无法从当前本地原理图确认。

## 检索关键词

`Atom Display`、`K115`、`Atom PSRAM`、`ESP32-V3-02`、`ESP32-PICO-V3-02`、`SY8089`、`CP2104`、`WS2812B-2020`、`MMDT4401`、`USB Type-C`、`USB_DP`、`USB_DM`、`VUSB_5V`、`VCC_3V3`、`PROANT_440`、`IPEX`、`ANT_LNA`、`BUTTON_G39`、`ESP32_EN`、`GPIO0`、`SK_DIN`、`SK_DOUT`、`GROVE_G32`、`GROVE_G26`、`CONN_GP21`、`CONN_GP25`、`CONN_GP22`、`CONN_GP19`、`CONN_GP5`、`CONN_GP33`、`U0RXD`、`U0TXD`、`CP_RTS`、`CP_DTR`、`GW1NR-9C`、`LT8618SX`、`display output`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-V3-02 | Atom PSRAM 控制器，连接 UART、按键、RGB、天线与扩展接口 | 图 a4dccc8bb44b / 第 1 页 / 左上 U1 ESP32-V3-02：LNA_IN/EN、GPIO、U0RXD/U0TXD、VCC_3V3 与 GND |
| ANT1 | PROANT_440 | ESP32 板载天线 | 图 a4dccc8bb44b / 第 1 页 / 上部中央 ANT1 PROANT_440，连接 ANT_LNA 匹配网络 |
| J5 | IPEX | 预留外部天线连接器，信号路径中的 C25 标为 NC | 图 a4dccc8bb44b / 第 1 页 / 上部 J5 IPEX：外壳 pins 2/3 接 GND，pin 1 经 C25 NC 到 ANT_LNA |
| J2 | 5P-2.54 | Atom 5 Pin 的 3.3V 与 GPIO22/19/5/33 接口 | 图 a4dccc8bb44b / 第 1 页 / 右上 J2 5P-2.54，pins 1~5 为 VCC_3V3/CONN_GP22/CONN_GP19/CONN_GP5/CONN_GP33 |
| J1 | 4PIN-2.54 | Atom 4 Pin 的 GPIO21/GPIO25/5V/GND 接口 | 图 a4dccc8bb44b / 第 1 页 / 右侧 J1 4PIN-2.54，pins 1~4 为 CONN_GP21/CONN_GP25/VUSB_5V/GND |
| J3 | PH2.0_4P_SMT | Grove GPIO32/GPIO26 与 5V/GND 接口 | 图 a4dccc8bb44b / 第 1 页 / 右侧 J3 PH2.0_4P_SMT，pins 1~4 为 GROVE_G32/GROVE_G26/VUSB_5V/GND |
| S2 | SMT_SW_PTS_820 | GPIO39 用户按键，按下接地 | 图 a4dccc8bb44b / 第 1 页 / 左下 BUTTON_G39-R1 5.1KΩ-S2 SMT_SW_PTS_820-GND |
| S1 | SMT_SW_TS_015 | ESP32_EN 复位按键，按下接地 | 图 a4dccc8bb44b / 第 1 页 / 下部 ESP32_EN-R2 5.1KΩ-C14 470nF-S1 SMT_SW_TS_015-GND，C13 NC |
| U2 | SY8089 | VUSB_5V 到 VCC_3V3 的降压转换器 | 图 524bc3ae016a / 第 1 页 / 上部 U2 SY8089：IN/EN/LX/FB/GND、L2 与 R13/R14 |
| J4 | USB-TYPEC | USB 5V 电源与 USB_DP/USB_DM 数据输入连接器 | 图 524bc3ae016a / 第 1 页 / 左中 J4 USB-TYPEC：VCC/DP/CC1/CC2/DN/GND/SHELL |
| FUSE1 | JK-SMD0603-100L | USB VCC 到 VUSB_5V 的可恢复保险丝，标注 1A/6V/2A 跳闸电流 | 图 524bc3ae016a / 第 1 页 / 左中 FUSE1：J4 VCC 与 VUSB_5V 之间，1A/6V/2A 跳闸电流/JK-SMD0603-100L |
| U3 | CP2104 | USB 转 UART 桥，连接 USB_DP/USB_DM 与 ESP32 U0RXD/U0TXD | 图 524bc3ae016a / 第 1 页 / 右中 U3 CP2104：VBUS/D+/D-/TXD/RXD/DTR/RTS/VIO/VDD/REGIN/GND |
| U5A/U5B | MMDT4401 | CP2104 DTR/RTS 到 ESP32_EN/GPIO0 的自动下载与复位控制晶体管 | 图 524bc3ae016a / 第 1 页 / 右侧 U5A/U5B MMDT4401 与 R3/R4/R5、CP_DTR/CP_RTS、ESP32_EN/GPIO0 |
| U4 | WS2812B-2020 | 可编程 RGB LED，数据输入为 SK_DIN，输出为 SK_DOUT | 图 524bc3ae016a / 第 1 页 / 左下 U4 WS2812B-2020：VDD/DI/DO/GND 与 C24 4.7uF |
| C25/C26/L1/C1/C2 | Antenna matching network | 板载天线与 IPEX 之间的可配置射频匹配网络 | 图 a4dccc8bb44b / 第 1 页 / 上部 ANT_LNA-C25 NC-C26 0R-L1 TBD/NC-C1 TBD/0R-C2 TBD/NC-ANT1 |

## 系统结构

### Atom Display 当前本地原理图范围

两张资源页面共同描述 Atom PSRAM 控制器：第一页包含 ESP32-V3-02、天线、Atom/Grove 接口、按键与复位，第二页包含 USB Type-C、SY8089、CP2104、自动下载控制与 WS2812B。

- 参数与网络：`page_1=ESP32-V3-02,antenna,connectors,button,reset`；`page_2=USB-TYPEC,SY8089,CP2104,MMDT4401,WS2812B-2020`
- 证据：图 a4dccc8bb44b / 第 1 页 / source_001 全页：U1、ANT1/J5、J1/J2/J3、S1/S2 与 VCC_3V3 去耦; 图 524bc3ae016a / 第 1 页 / source_002 全页：U2/J4/FUSE1/U3/U5A/U5B/U4

## 电源

### ESP32 VCC_3V3 电源域

VCC_3V3 连接 U1 的 VDDA pins 1/43/46、VDDA3P3 pins 3/4、VDD3P3_CPU pin 37 与 VDD3P3_RTC pin 19；C3/C4 各 4.7uF，C5~C12 各 470nF 接在 VCC_3V3 与 GND 之间。

- 参数与网络：`analog_supply=U1 pins 1,43,46`；`analog_3v3=U1 pins 3,4`；`cpu_supply=U1 pin 37`；`rtc_supply=U1 pin 19`；`bulk_decoupling=C3/C4 4.7uF/6.3V`；`local_decoupling=C5-C12 470nF/10V`
- 证据：图 a4dccc8bb44b / 第 1 页 / 左侧 U1 VCC_3V3 电源引脚与中下部 C3~C12 去耦阵列

### U2 SY8089 VCC_3V3

U2 IN pin 4 与 EN pin 1 接 VUSB_5V，LX pin 3 经 L2 2.2uH/1.2A/0806 输出 VCC_3V3；FB pin 5 接 R13 22.1KΩ 与 R14 100KΩ 分压网络。

- 参数与网络：`input=VUSB_5V`；`enable=U2 pin 1 tied to VUSB_5V`；`switch=U2 pin 3 LX`；`inductor=L2 2.2uH/1.2A/0806`；`output=VCC_3V3`；`feedback=R13 22.1KΩ,R14 100KΩ`；`input_caps=C15/C16 4.7uF/6.3V`；`output_caps=C17-C20 4.7uF/6.3V`
- 证据：图 524bc3ae016a / 第 1 页 / 上部 VUSB_5V-C15/C16-U2 SY8089-L2-R13/R14-VCC_3V3-C17~C20

### J4 USB Type-C 电源输入

J4 VCC 通过 FUSE1 JK-SMD0603-100L 连接 VUSB_5V；CC1 与 CC2 分别经 R15/R16 5.1KΩ 接 GND，J4 GND 与 SHELL 接地。

- 参数与网络：`connector=J4 USB-TYPEC`；`fuse=FUSE1 1A/6V/2A trip JK-SMD0603-100L`；`output=VUSB_5V`；`cc1=R15 5.1KΩ to GND`；`cc2=R16 5.1KΩ to GND`；`input_caps=C21/C23 4.7uF/6.3V`
- 证据：图 524bc3ae016a / 第 1 页 / 左中 J4/FUSE1/R15/R16 与 VUSB_5V/C21/C23

## 接口

### J2 Atom 5 Pin

J2 pins 1~5 依次连接 VCC_3V3、CONN_GP22、CONN_GP19、CONN_GP5、CONN_GP33；R6 标为 NC，预留在 CONN_GP23 与 CONN_GP5 之间。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=CONN_GP22`；`pin_3=CONN_GP19`；`pin_4=CONN_GP5`；`pin_5=CONN_GP33`；`optional_link=R6 NC between CONN_GP23 and CONN_GP5`
- 证据：图 a4dccc8bb44b / 第 1 页 / 右上 J2 5P-2.54 与 R6 NC、CONN_GP23/GP5

### J1 Atom 4 Pin

J1 pins 1~4 依次连接 CONN_GP21、CONN_GP25、VUSB_5V 与 GND。

- 参数与网络：`pin_1=CONN_GP21`；`pin_2=CONN_GP25`；`pin_3=VUSB_5V`；`pin_4=GND`
- 证据：图 a4dccc8bb44b / 第 1 页 / 右侧 J1 4PIN-2.54 pins 1~4 与左侧网络

### J3 Grove 接口

J3 pins 1~4 依次连接 GROVE_G32、GROVE_G26、VUSB_5V 与 GND，对应 U1 GPIO32、GPIO26、5V 和地。

- 参数与网络：`pin_1=GROVE_G32 U1 IO32`；`pin_2=GROVE_G26 U1 IO26`；`pin_3=VUSB_5V`；`pin_4=GND`
- 证据：图 a4dccc8bb44b / 第 1 页 / 右侧 J3 PH2.0_4P_SMT 与左上 U1 IO32/IO26 的 GROVE_G32/GROVE_G26 网络

## 总线

### USB Type-C 到 CP2104

J4 的 DP1/DP2 连接 USB_DP 并到 U3 D+ pin 3，DN1/DN2 连接 USB_DM 并到 U3 D- pin 4；U3 VBUS pin 8 与 REGIN pin 7 接 VUSB_5V。

- 参数与网络：`d_plus=J4 A6/B6-USB_DP-U3 pin 3 D+`；`d_minus=J4 A7/B7-USB_DM-U3 pin 4 D-`；`vbus=U3 pin 8 VBUS`；`regin=U3 pin 7 REGIN`
- 证据：图 524bc3ae016a / 第 1 页 / J4 USB_DP/USB_DM 与 U3 CP2104 pins 3/4/7/8

### CP2104 到 ESP32 UART

U3 TXD pin 21 连接 U0RXD 并到 U1 U0RXD/IO3 pin 40，U3 RXD pin 20 连接 U0TXD 并到 U1 U0TXD/IO1 pin 41。

- 参数与网络：`usb_uart_tx=U3 pin 21 TXD-U0RXD-U1 pin 40`；`usb_uart_rx=U3 pin 20 RXD-U0TXD-U1 pin 41`
- 证据：图 524bc3ae016a / 第 1 页 / 右中 U3 CP2104 pins 21/20 的 U0RXD/U0TXD; 图 a4dccc8bb44b / 第 1 页 / 左上 U1 pins 40/41 U0RXD/U0TXD

## GPIO 与控制信号

### U1 ESP32-V3-02 已连接 GPIO

U1 的 IO39 接 BUTTON_G39，IO32/IO26 接 GROVE_G32/GROVE_G26，IO33/IO25/IO5/IO19/IO22/IO21 接 CONN_GP33/25/5/19/22/21，IO27 接 SK_DIN，IO0 接 GPIO0，U0RXD/U0TXD 接同名 UART 网络。

- 参数与网络：`GPIO39=BUTTON_G39`；`GPIO32=GROVE_G32`；`GPIO26=GROVE_G26`；`GPIO33=CONN_GP33`；`GPIO25=CONN_GP25`；`GPIO5=CONN_GP5`；`GPIO19=CONN_GP19`；`GPIO22=CONN_GP22`；`GPIO21=CONN_GP21`；`GPIO27=SK_DIN`；`GPIO0=GPIO0`；`UART=U0RXD,U0TXD`
- 证据：图 a4dccc8bb44b / 第 1 页 / 左上 U1 pins 8/12~16/23/34/38~42 的网络标签

### BUTTON_G39

U1 IO39 连接 BUTTON_G39，R1 5.1KΩ 将该网络上拉到 VCC_3V3，S2 SMT_SW_PTS_820 按键将该网络接到 GND。

- 参数与网络：`mcu_pin=U1 IO39`；`network=BUTTON_G39`；`pullup=R1 5.1KΩ to VCC_3V3`；`switch=S2 SMT_SW_PTS_820 to GND`
- 证据：图 a4dccc8bb44b / 第 1 页 / U1 pin 8 SENSOR_VN/IO39 与左下 BUTTON_G39-R1-S2-GND

### U4 WS2812B-2020

U4 VDD pin 2 接 VCC_3V3，GND pin 4 接地，DI pin 1 连接 SK_DIN 并到 U1 IO27，DO pin 3 引出 SK_DOUT；C24 4.7uF/6.3V 跨接电源。

- 参数与网络：`power=pin 2 VCC_3V3`；`ground=pin 4 GND`；`data_in=pin 1 SK_DIN-U1 IO27`；`data_out=pin 3 SK_DOUT`；`decoupling=C24 4.7uF/6.3V`
- 证据：图 524bc3ae016a / 第 1 页 / 左下 U4 WS2812B-2020 与 C24、SK_DIN/SK_DOUT; 图 a4dccc8bb44b / 第 1 页 / 左上 U1 IO27 pin 16 SK_DIN

## 复位

### ESP32_EN 手动复位

U1 EN pin 9 连接 ESP32_EN，R2 5.1KΩ 上拉到 VCC_3V3，C14 470nF 接 GND，S1 SMT_SW_TS_015 按下时接 GND；跨按键的 C13 标为 NC。

- 参数与网络：`mcu_pin=U1 pin 9 EN`；`network=ESP32_EN`；`pullup=R2 5.1KΩ`；`capacitor=C14 470nF/10V`；`switch=S1 SMT_SW_TS_015`；`optional_capacitor=C13 NC`
- 证据：图 a4dccc8bb44b / 第 1 页 / U1 pin 9 EN 与下部 ESP32_EN-R2-C14-S1-C13-GND

### CP2104 自动下载控制

U3 DTR pin 23 输出 CP_DTR，RTS pin 19 输出 CP_RTS；两路信号通过 U5A/U5B MMDT4401 与 R3/R4/R5 5.1KΩ 网络连接 ESP32_EN 和 GPIO0。

- 参数与网络：`dtr=U3 pin 23 CP_DTR`；`rts=U3 pin 19 CP_RTS`；`transistors=U5A/U5B MMDT4401`；`resistors=R3/R4/R5 5.1KΩ`；`targets=ESP32_EN,GPIO0`
- 证据：图 524bc3ae016a / 第 1 页 / 右侧 U3 CP_DTR/CP_RTS-U5A/U5B-R3/R4/R5-ESP32_EN/GPIO0

## 射频

### ESP32 板载天线路径

U1 LNA_IN pin 2 的 ANT_LNA 网络经 C26 0R、C1 TBD/0R 到 ANT1 PROANT_440；L1 与 C2 为到 GND 的 TBD/NC 匹配位。

- 参数与网络：`radio_pin=U1 pin 2 LNA_IN`；`net=ANT_LNA`；`series_1=C26 0R`；`series_2=C1 TBD/0R`；`shunt_1=L1 TBD/NC to GND`；`shunt_2=C2 TBD/NC to GND`；`antenna=ANT1 PROANT_440`
- 证据：图 a4dccc8bb44b / 第 1 页 / 上部 U1 LNA_IN-ANT_LNA-C26-L1-C1-C2-ANT1 PROANT_440

### J5 IPEX 预留路径

J5 IPEX 的信号 pin 1 通过 C25 连接 ANT_LNA，C25 标为 NC；J5 外壳 pins 2/3 接 GND。

- 参数与网络：`connector=J5 IPEX`；`signal_pin=pin 1`；`link=C25 NC to ANT_LNA`；`ground_pins=2,3`
- 证据：图 a4dccc8bb44b / 第 1 页 / 上部 J5 IPEX-C25 NC-ANT_LNA 与两侧 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom Display 当前本地原理图范围 | `page_1=ESP32-V3-02,antenna,connectors,button,reset`；`page_2=USB-TYPEC,SY8089,CP2104,MMDT4401,WS2812B-2020` |
| GPIO 与控制信号 | U1 ESP32-V3-02 已连接 GPIO | `GPIO39=BUTTON_G39`；`GPIO32=GROVE_G32`；`GPIO26=GROVE_G26`；`GPIO33=CONN_GP33`；`GPIO25=CONN_GP25`；`GPIO5=CONN_GP5`；`GPIO19=CONN_GP19`；`GPIO22=CONN_GP22`；`GPIO21=CONN_GP21`；`GPIO27=SK_DIN`；`GPIO0=GPIO0`；`UART=U0RXD,U0TXD` |
| 电源 | ESP32 VCC_3V3 电源域 | `analog_supply=U1 pins 1,43,46`；`analog_3v3=U1 pins 3,4`；`cpu_supply=U1 pin 37`；`rtc_supply=U1 pin 19`；`bulk_decoupling=C3/C4 4.7uF/6.3V`；`local_decoupling=C5-C12 470nF/10V` |
| 接口 | J2 Atom 5 Pin | `pin_1=VCC_3V3`；`pin_2=CONN_GP22`；`pin_3=CONN_GP19`；`pin_4=CONN_GP5`；`pin_5=CONN_GP33`；`optional_link=R6 NC between CONN_GP23 and CONN_GP5` |
| 接口 | J1 Atom 4 Pin | `pin_1=CONN_GP21`；`pin_2=CONN_GP25`；`pin_3=VUSB_5V`；`pin_4=GND` |
| 接口 | J3 Grove 接口 | `pin_1=GROVE_G32 U1 IO32`；`pin_2=GROVE_G26 U1 IO26`；`pin_3=VUSB_5V`；`pin_4=GND` |
| GPIO 与控制信号 | BUTTON_G39 | `mcu_pin=U1 IO39`；`network=BUTTON_G39`；`pullup=R1 5.1KΩ to VCC_3V3`；`switch=S2 SMT_SW_PTS_820 to GND` |
| 复位 | ESP32_EN 手动复位 | `mcu_pin=U1 pin 9 EN`；`network=ESP32_EN`；`pullup=R2 5.1KΩ`；`capacitor=C14 470nF/10V`；`switch=S1 SMT_SW_TS_015`；`optional_capacitor=C13 NC` |
| 射频 | ESP32 板载天线路径 | `radio_pin=U1 pin 2 LNA_IN`；`net=ANT_LNA`；`series_1=C26 0R`；`series_2=C1 TBD/0R`；`shunt_1=L1 TBD/NC to GND`；`shunt_2=C2 TBD/NC to GND`；`antenna=ANT1 PROANT_440` |
| 射频 | J5 IPEX 预留路径 | `connector=J5 IPEX`；`signal_pin=pin 1`；`link=C25 NC to ANT_LNA`；`ground_pins=2,3` |
| 电源 | U2 SY8089 VCC_3V3 | `input=VUSB_5V`；`enable=U2 pin 1 tied to VUSB_5V`；`switch=U2 pin 3 LX`；`inductor=L2 2.2uH/1.2A/0806`；`output=VCC_3V3`；`feedback=R13 22.1KΩ,R14 100KΩ`；`input_caps=C15/C16 4.7uF/6.3V`；`output_caps=C17-C20 4.7uF/6.3V` |
| 电源 | J4 USB Type-C 电源输入 | `connector=J4 USB-TYPEC`；`fuse=FUSE1 1A/6V/2A trip JK-SMD0603-100L`；`output=VUSB_5V`；`cc1=R15 5.1KΩ to GND`；`cc2=R16 5.1KΩ to GND`；`input_caps=C21/C23 4.7uF/6.3V` |
| 总线 | USB Type-C 到 CP2104 | `d_plus=J4 A6/B6-USB_DP-U3 pin 3 D+`；`d_minus=J4 A7/B7-USB_DM-U3 pin 4 D-`；`vbus=U3 pin 8 VBUS`；`regin=U3 pin 7 REGIN` |
| 总线 | CP2104 到 ESP32 UART | `usb_uart_tx=U3 pin 21 TXD-U0RXD-U1 pin 40`；`usb_uart_rx=U3 pin 20 RXD-U0TXD-U1 pin 41` |
| 复位 | CP2104 自动下载控制 | `dtr=U3 pin 23 CP_DTR`；`rts=U3 pin 19 CP_RTS`；`transistors=U5A/U5B MMDT4401`；`resistors=R3/R4/R5 5.1KΩ`；`targets=ESP32_EN,GPIO0` |
| GPIO 与控制信号 | U4 WS2812B-2020 | `power=pin 2 VCC_3V3`；`ground=pin 4 GND`；`data_in=pin 1 SK_DIN-U1 IO27`；`data_out=pin 3 SK_DOUT`；`decoupling=C24 4.7uF/6.3V` |
| 其他事实 | Display Base 原理图覆盖范围 | `local_assets=2`；`gw1nr_9c_visible=false`；`lt8618sx_visible=false`；`display_connector_visible=false`；`covered_subsystem=Atom PSRAM controller` |

## 待确认事项

- `other.display-base-resource-coverage`：两张本地资源均未显示 GW1NR-9C、LT8618SX、RGB 视频总线或显示输出连接器，因此无法从当前资源确认 Atom Display 的 FPGA 与显示输出子系统。（证据：图 a4dccc8bb44b / 第 1 页 / source_001 全页：最高层器件为 ESP32-V3-02、天线、接口、按键与复位，无 FPGA/LT8618SX/显示连接器; 图 524bc3ae016a / 第 1 页 / source_002 全页：SY8089、USB-TYPEC、CP2104、MMDT4401、WS2812B，无 FPGA/LT8618SX/显示连接器）
- `review.display-base-missing-pages`：请补充 Sch_AtomDisplay.pdf 中包含 GW1NR-9C、LT8618SX、RGB 总线、电源与显示输出连接器的 Atomic Display Base 页面。；原因：当前两张本地页面只覆盖 Atom PSRAM 控制器，无法生成产品核心 Display Base 子系统的可追溯硬件事实。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a4dccc8bb44b9d7ca8938e2da1ba81c9d7000d44a1e8000ec87bdad8bf94f19a` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_sch_01.webp` |
| 2 | 1 | `524bc3ae016adab4b7cecedae7d710a9e85c66b4f06a38d821faec2e394c11b0` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_sch_02.webp` |

---

源文档：`zh_CN/atom/atom_display.md`

源文档 SHA-256：`b893c8dc4886e48a7ee1d373e2b007704c8032e4ea7d6dbd70bcda99d34b92b3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
