# Module Gateway H2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Gateway H2 |
| SKU | M141 |
| 产品 ID | `module-gateway-h2-1a78b06ae3b4` |
| 源文档 | `zh_CN/module/Module Gateway H2.md` |

## 概述

Module Gateway H2 以 M1 ESP32-H2-MINI-1-N2 为主控/无线模组，直接由 M5-Bus +3.3 V 供电。TX0、RX0、G9 和 H2-EN 经 0 Ω 电阻固定路由到主机 GPIO；SPI 与 WL_ACTIVE、BT_ACTIVE、BT_PRIORITY 则通过 S1 八位拨码开关选择连接。页面另提供 J2 六针下载接口、可选 USB D+/D- 网络、可选 32.768 kHz 晶振和两路可选 LED，并把 +5 V、BAT 与 HPWR 透传到 M5-Bus。

## 检索关键词

`Module Gateway H2`、`M141`、`ESP32-H2-MINI-1-N2`、`ESP32-H2`、`M5Stack_BUS`、`SW DIP-8`、`S1`、`UART`、`TX0`、`RX0`、`SPI`、`SPI_CS`、`SPI_MOSI`、`SPI_MISO`、`SPI_CLK`、`WL_ACTIVE`、`BT_ACTIVE`、`BT_PRIORITY`、`H2-EN`、`H2-G0`、`H2-G1`、`H2-G2`、`H2-G3`、`H2-G4`、`H2-G5`、`G9`、`GPIO35`、`GPIO17`、`GPIO16`、`GPIO13`、`GPIO0`、`GPIO12`、`GPIO25`、`GPIO15`、`GPIO23`、`GPIO18`、`GPIO19`、`USB_DP`、`USB_DN`、`32.768KHz`、`+3.3V`、`+5V`、`BAT`、`Zigbee`、`Thread`、`Matter`、`IEEE 802.15.4`、`2MB Flash`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | ESP32-H2-MINI-1-N2 | 主控与无线模组，提供 UART、SPI 配置 GPIO、USB、复位/使能和无线共存信号 | 图 22340fe8b841 / 第 1 页 / B2-C2 M1 ESP32-H2-MINI-1-N2 pins1-36 |
| S1 | SW DIP-8 | 八位拨码开关，将三条共存信号与四条 SPI 信号选择连接到 M5-Bus GPIO，另有一位未接 | 图 22340fe8b841 / 第 1 页 / B4-C4 S1 SW DIP-8 pins1-16 |
| J2 | DownloadSocketGND | 六针下载接口，提供 3.3 V、TXD、RXD、EN、G0 与 GND | 图 22340fe8b841 / 第 1 页 / A4-B4 J2 DownloadSocketGND pins1-6 |
| J3/J4 | M5Stack_BUS | 30 针堆叠主机接口，承载电源、UART、SPI、使能、G9 和无线共存信号 | 图 22340fe8b841 / 第 1 页 / C4-D4 J3 J4 M5Stack_BUS pins1-30 |
| R10-R13 | 0Ω | TX0、RX0、G9 与 H2-EN 到主机 GPIO 的固定路由电阻 | 图 22340fe8b841 / 第 1 页 / B3-B4 R10-R13 0Ω、Core v0.4 注记 |
| R15-R21 | 0Ω | WL_ACTIVE、BT_ACTIVE、BT_PRIORITY 和 SPI 信号到 S1 的串联配置电阻 | 图 22340fe8b841 / 第 1 页 / B3-C4 R15-R21 与 S1 |
| R2/C13 | 10KΩ / 1uF | M1 H2-EN 的 3.3 V 上拉与对地 RC 网络 | 图 22340fe8b841 / 第 1 页 / B1-B2 R2 10KΩ/C13 1uF/H2-EN/M1 EN pin8 |
| C6/C1/C2 | 22uF / 22uF / 100nF | M1 3.3 V 输入的对地去耦与储能电容 | 图 22340fe8b841 / 第 1 页 / B1 +3.3V 上 C6/C1/C2 与 M1 pin3 |
| Y1/C3/C4/R6 | 32.768KHz ±20ppm 12.5pF / 6.0pF/NC / 6.0pF/NC / 5.1MΩ/NC | 标记为不装的可选 32.768 kHz 外部低速晶振网络 | 图 22340fe8b841 / 第 1 页 / C1-C2 OSCI/OSCO、Y1/NC、C3/C4/R6 |
| R3/R4/JP1 | 0Ω/NC / 0Ω/NC / null | M1 IO27/IO26 到 USB_DP/USB_DN 的可选 USB 连接网络 | 图 22340fe8b841 / 第 1 页 / B2-B3 M1 IO27/IO26、R3/R4、USB_DP/USB_DN、JP1 |
| D1/D2/R5 | 0603/NC / 0603/NC / 1KΩ/NC | 连接 G25 与 G22 的两路可选 3.3 V 指示灯支路 | 图 22340fe8b841 / 第 1 页 / B2-C3 G25/D1 与 G22/D2/R5，均标 NC |

## 系统结构

### Module Gateway H2 系统架构

M1 ESP32-H2-MINI-1-N2 是页面唯一主控/无线模组，使用 M5-Bus +3.3 V 供电；UART 与控制信号经 0 Ω 电阻连接主机，SPI 和无线共存信号通过 S1 拨码开关连接。

- 参数与网络：`controller=M1 ESP32-H2-MINI-1-N2`；`host=J3/J4 M5Stack_BUS`；`power=+3.3V from M5-Bus`；`fixed_routes=TX0, RX0, G9, H2-EN`；`switched_routes=SPI and WL_ACTIVE/BT_ACTIVE/BT_PRIORITY`；`download=J2`；`usb_option=R3/R4/JP1`
- 证据：图 22340fe8b841 / 第 1 页 / 整页 M1/J2/S1/J3-J4 连接

## 核心器件

### ESP32-H2 模组标识

原理图将 M1 明确标为 ESP32-H2-MINI-1-N2，画出板载天线符号，并列出 36 个模组引脚。

- 参数与网络：`reference=M1`；`part_number=ESP32-H2-MINI-1-N2`；`pins=36`；`antenna_symbol=shown inside module symbol`
- 证据：图 22340fe8b841 / 第 1 页 / B2-C2 M1 title and antenna graphic

## 电源

### 3.3 V 主供电

J3/J4 M5-Bus pin12 的 +3.3 V 经 R14 0 Ω 进入板上 3.3 V 网络，供给 M1 pin3、EN 上拉与下载接口；页面没有独立 DC/DC 或 LDO。

- 参数与网络：`source=J3/J4 pin12 +3.3V`；`series=R14 0Ω`；`loads=M1 pin3; R2 EN pull-up; J2 pin1; optional LEDs`；`converter=not shown`；`ldo=not shown`
- 证据：图 22340fe8b841 / 第 1 页 / B1 M1 +3.3V；A4 J2 +3.3V；C4 J3/J4 pin12/R14

### M1 电源去耦

M1 3.3 V 输入配置 C6 22 uF、C1 22 uF 与 C2 100 nF 对地；J2 下载口 3.3 V 另配置 C5 100 nF。

- 参数与网络：`module_caps=C6 22uF; C1 22uF; C2 100nF`；`download_cap=C5 100nF`；`rail=+3.3V`；`ground=GND`
- 证据：图 22340fe8b841 / 第 1 页 / B1 C6/C1/C2；A4-B4 C5/J2

## 接口

### 可选 USB D+/D- 网络

M1 IO27 pin27 经 R3 0 Ω/NC 连接 USB_DP，IO26 pin26 经 R4 0 Ω/NC 连接 USB_DN，两网络终止于 JP1；R3/R4 标 NC，页面未给 JP1 型号或保护器件。

- 参数与网络：`dp=M1 IO27 pin27 -> R3 0Ω/NC -> USB_DP`；`dn=M1 IO26 pin26 -> R4 0Ω/NC -> USB_DN`；`endpoint=JP1`；`population=R3/R4 NC`；`connector_part=null`；`esd=not shown`
- 证据：图 22340fe8b841 / 第 1 页 / B2-B3 IO27/IO26/R3/R4/USB_DP/USB_DN/JP1

### 可选 GPIO 指示灯

G25 与 G22 各连接一路到 +3.3 V 的 0603 LED 支路，图中 D1/D2 与相关 1 kΩ 电阻均标 NC，因此为未装选项。

- 参数与网络：`channel_1=G25 / D1 0603/NC / 1KΩ/NC to +3.3V`；`channel_2=G22 / D2 0603/NC / R5 1KΩ/NC to +3.3V`；`population=NC`
- 证据：图 22340fe8b841 / 第 1 页 / B2-C3 G25/D1 与 G22/D2/R5

### M5-Bus 使用网络

J3/J4 使用 pins1/3/5 GND、pin2 GPIO35/TX0、pin7 GPIO23/SPI_MOSI、pin8 GPIO25/BT_PRIORITY、pin9 GPIO19/SPI_MISO、pin11 GPIO18/SPI_CLK、pin12 +3.3 V、pin15 GPIO16/G9、pin16 GPIO17/RX0、pin21 GPIO12/BT_ACTIVE、pin22 GPIO13/H2-EN、pin23 GPIO15/SPI_CS、pin24 GPIO0/WL_ACTIVE；pins25/27/29 HPWR、pin28 +5 V、pin30 BAT 保持总线连接。

- 参数与网络：`ground=pins1/3/5`；`uart=pin2 GPIO35 TX0; pin16 GPIO17 RX0`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 CLK; pin23 GPIO15 CS`；`coexistence=pin8 GPIO25 BT_PRIORITY; pin21 GPIO12 BT_ACTIVE; pin24 GPIO0 WL_ACTIVE`；`control=pin15 GPIO16 G9; pin22 GPIO13 H2-EN`；`power=pin12 +3.3V; pins25/27/29 HPWR; pin28 +5V; pin30 BAT`
- 证据：图 22340fe8b841 / 第 1 页 / C4-D4 J3/J4 M5Stack_BUS pins1-30

## 总线

### ESP32-H2 UART0 主机路由

M1 TX0 pin31 经 R10 0 Ω 连接 GPIO35/J3-J4 pin2，M1 RX0 pin30 经 R11 0 Ω 连接 GPIO17/J3-J4 pin16；两信号也分别连接 J2 TXD pin2 与 RXD pin3。

- 参数与网络：`module_tx=M1 TX0 pin31 -> R10 0Ω -> GPIO35 / bus pin2 -> J2 TXD pin2`；`module_rx=GPIO17 / bus pin16 -> R11 0Ω -> M1 RX0 pin30; J2 RXD pin3`；`direction=TX0 module-to-host; RX0 host-to-module`；`logic_level=+3.3V`
- 证据：图 22340fe8b841 / 第 1 页 / B2 M1 TX0/RX0；B3-B4 R10/R11；A4 J2；C4 J3/J4

### 拨码选择的 SPI 路由

S1 闭合对应通道时，H2-G2/SPI_CS 经 R18 0 Ω 接 GPIO15/J3-J4 pin23，H2-G3/SPI_MOSI 经 R19 接 GPIO23/pin7，H2-G0/SPI_CLK 经 R20 接 GPIO18/pin11，H2-G1/SPI_MISO 经 R21 接 GPIO19/pin9。

- 参数与网络：`chip_select=H2-G2 -> R18 0Ω -> S1 pins5/12 -> GPIO15 bus pin23`；`mosi=H2-G3 -> R19 0Ω -> S1 pins6/11 -> GPIO23 bus pin7`；`clock=H2-G0 -> R20 0Ω -> S1 pins7/10 -> GPIO18 bus pin11`；`miso=H2-G1 -> R21 0Ω -> S1 pins8/9 -> GPIO19 bus pin9`；`selection=S1 channel closure`
- 证据：图 22340fe8b841 / 第 1 页 / C2 H2-G0/G1/G2/G3；C3-C4 R18-R21/S1/J3-J4

## GPIO 与控制信号

### ESP32-H2 G9 路由

M1 的 G9 网络经 R12 0 Ω 连接主机 GPIO16/J3-J4 pin15，并连接 J2 pin5（接口内标 G0）。

- 参数与网络：`module_net=G9`；`route=R12 0Ω`；`host_gpio=GPIO16`；`bus_pin=J3/J4 pin15`；`download_pin=J2 pin5 labeled G0`
- 证据：图 22340fe8b841 / 第 1 页 / C2 M1 G9；B3-B4 R12/GPIO16；A4 J2 G9-to-G0 pin5

### 无线共存信号拨码路由

S1 闭合对应通道时，WL_ACTIVE/H2-G1 经 R15 0 Ω 接 GPIO0/J3-J4 pin24，BT_ACTIVE/H2-G4 经 R16 接 GPIO12/pin21，BT_PRIORITY/H2-G5 经 R17 接 GPIO25/pin8。

- 参数与网络：`wl_active=H2-G1 -> R15 0Ω -> S1 pins1/16 -> GPIO0 bus pin24`；`bt_active=H2-G4 -> R16 0Ω -> S1 pins2/15 -> GPIO12 bus pin21`；`bt_priority=H2-G5 -> R17 0Ω -> S1 pins3/14 -> GPIO25 bus pin8`；`unused_switch=S1 pins4/13 not connected`
- 证据：图 22340fe8b841 / 第 1 页 / B3-C4 WL_ACTIVE/BT_ACTIVE/BT_PRIORITY R15-R17/S1

## 时钟

### 可选 32.768 kHz 晶振

OSCI/OSCO 之间画有 Y1 32.768 kHz ±20 ppm、12.5 pF 晶振，C3/C4 各 6.0 pF 对地、R6 5.1 MΩ 跨接；Y1、C3、C4、R6 均标 NC。

- 参数与网络：`nets=OSCI/OSCO`；`crystal=Y1 32.768KHz ±20ppm 12.5pF / NC`；`load_caps=C3/C4 6.0pF / NC`；`feedback=R6 5.1MΩ / NC`；`population=not populated`
- 证据：图 22340fe8b841 / 第 1 页 / C1-C2 OSCI/OSCO/Y1/C3/C4/R6

## 复位

### H2-EN 使能/复位网络

M1 EN pin8 连接 H2-EN，R2 10 kΩ 上拉至 3.3 V、C13 1 uF 对地；H2-EN 经 R13 0 Ω 连接主机 GPIO13，并连接 J2 pin4 EN。

- 参数与网络：`target=M1 EN pin8`；`net=H2-EN`；`pullup=R2 10KΩ to +3.3V`；`capacitor=C13 1uF to GND`；`host=R13 0Ω -> GPIO13 / J3-J4 pin22`；`download=J2 pin4 EN`
- 证据：图 22340fe8b841 / 第 1 页 / B1-B2 R2/C13/M1 EN；B4 R13；A4 J2 pin4

## 调试与烧录

### 六针程序下载接口

J2 pin1 为 +3.3 V、pin2 TXD/TX0、pin3 RXD/RX0、pin4 EN/H2-EN、pin5 G0/G9 网络、pin6 GND，3.3 V 端由 C5 100 nF 去耦。

- 参数与网络：`connector=J2 DownloadSocketGND`；`pin1=+3.3V`；`pin2=TXD / TX0`；`pin3=RXD / RX0`；`pin4=EN / H2-EN`；`pin5=G0 label / G9 net`；`pin6=GND`；`decoupling=C5 100nF`
- 证据：图 22340fe8b841 / 第 1 页 / A4-B4 J2 pins1-6/C5

### v0.4 UART/G9 路由变更注记

R10-R12 旁注记标明 Core v0.4：G17 >> G35、G16 >> G17、G36 >> G16，对应当前 TX0->GPIO35、RX0->GPIO17、G9->GPIO16。

- 参数与网络：`revision=v0.4`；`changes=G17 -> G35; G16 -> G17; G36 -> G16`；`current_routes=TX0 GPIO35; RX0 GPIO17; G9 GPIO16`
- 证据：图 22340fe8b841 / 第 1 页 / B4 Core v0.4 annotation beside R10-R13

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Gateway H2 系统架构 | `controller=M1 ESP32-H2-MINI-1-N2`；`host=J3/J4 M5Stack_BUS`；`power=+3.3V from M5-Bus`；`fixed_routes=TX0, RX0, G9, H2-EN`；`switched_routes=SPI and WL_ACTIVE/BT_ACTIVE/BT_PRIORITY`；`download=J2`；`usb_option=R3/R4/JP1` |
| 核心器件 | ESP32-H2 模组标识 | `reference=M1`；`part_number=ESP32-H2-MINI-1-N2`；`pins=36`；`antenna_symbol=shown inside module symbol` |
| 电源 | 3.3 V 主供电 | `source=J3/J4 pin12 +3.3V`；`series=R14 0Ω`；`loads=M1 pin3; R2 EN pull-up; J2 pin1; optional LEDs`；`converter=not shown`；`ldo=not shown` |
| 电源 | M1 电源去耦 | `module_caps=C6 22uF; C1 22uF; C2 100nF`；`download_cap=C5 100nF`；`rail=+3.3V`；`ground=GND` |
| 复位 | H2-EN 使能/复位网络 | `target=M1 EN pin8`；`net=H2-EN`；`pullup=R2 10KΩ to +3.3V`；`capacitor=C13 1uF to GND`；`host=R13 0Ω -> GPIO13 / J3-J4 pin22`；`download=J2 pin4 EN` |
| 总线 | ESP32-H2 UART0 主机路由 | `module_tx=M1 TX0 pin31 -> R10 0Ω -> GPIO35 / bus pin2 -> J2 TXD pin2`；`module_rx=GPIO17 / bus pin16 -> R11 0Ω -> M1 RX0 pin30; J2 RXD pin3`；`direction=TX0 module-to-host; RX0 host-to-module`；`logic_level=+3.3V` |
| GPIO 与控制信号 | ESP32-H2 G9 路由 | `module_net=G9`；`route=R12 0Ω`；`host_gpio=GPIO16`；`bus_pin=J3/J4 pin15`；`download_pin=J2 pin5 labeled G0` |
| 调试与烧录 | 六针程序下载接口 | `connector=J2 DownloadSocketGND`；`pin1=+3.3V`；`pin2=TXD / TX0`；`pin3=RXD / RX0`；`pin4=EN / H2-EN`；`pin5=G0 label / G9 net`；`pin6=GND`；`decoupling=C5 100nF` |
| 总线 | 拨码选择的 SPI 路由 | `chip_select=H2-G2 -> R18 0Ω -> S1 pins5/12 -> GPIO15 bus pin23`；`mosi=H2-G3 -> R19 0Ω -> S1 pins6/11 -> GPIO23 bus pin7`；`clock=H2-G0 -> R20 0Ω -> S1 pins7/10 -> GPIO18 bus pin11`；`miso=H2-G1 -> R21 0Ω -> S1 pins8/9 -> GPIO19 bus pin9`；`selection=S1 channel closure` |
| GPIO 与控制信号 | 无线共存信号拨码路由 | `wl_active=H2-G1 -> R15 0Ω -> S1 pins1/16 -> GPIO0 bus pin24`；`bt_active=H2-G4 -> R16 0Ω -> S1 pins2/15 -> GPIO12 bus pin21`；`bt_priority=H2-G5 -> R17 0Ω -> S1 pins3/14 -> GPIO25 bus pin8`；`unused_switch=S1 pins4/13 not connected` |
| 接口 | 可选 USB D+/D- 网络 | `dp=M1 IO27 pin27 -> R3 0Ω/NC -> USB_DP`；`dn=M1 IO26 pin26 -> R4 0Ω/NC -> USB_DN`；`endpoint=JP1`；`population=R3/R4 NC`；`connector_part=null`；`esd=not shown` |
| 时钟 | 可选 32.768 kHz 晶振 | `nets=OSCI/OSCO`；`crystal=Y1 32.768KHz ±20ppm 12.5pF / NC`；`load_caps=C3/C4 6.0pF / NC`；`feedback=R6 5.1MΩ / NC`；`population=not populated` |
| 接口 | 可选 GPIO 指示灯 | `channel_1=G25 / D1 0603/NC / 1KΩ/NC to +3.3V`；`channel_2=G22 / D2 0603/NC / R5 1KΩ/NC to +3.3V`；`population=NC` |
| 接口 | M5-Bus 使用网络 | `ground=pins1/3/5`；`uart=pin2 GPIO35 TX0; pin16 GPIO17 RX0`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 CLK; pin23 GPIO15 CS`；`coexistence=pin8 GPIO25 BT_PRIORITY; pin21 GPIO12 BT_ACTIVE; pin24 GPIO0 WL_ACTIVE`；`control=pin15 GPIO16 G9; pin22 GPIO13 H2-EN`；`power=pin12 +3.3V; pins25/27/29 HPWR; pin28 +5V; pin30 BAT` |
| 调试与烧录 | v0.4 UART/G9 路由变更注记 | `revision=v0.4`；`changes=G17 -> G35; G16 -> G17; G36 -> G16`；`current_routes=TX0 GPIO35; RX0 GPIO17; G9 GPIO16` |
| 内存与 Flash | Flash 容量 | `document_flash=2MB`；`schematic_module=ESP32-H2-MINI-1-N2`；`external_flash=not shown`；`schematic_capacity=null` |
| 射频 | Zigbee、Thread、Matter 与 IEEE 802.15.4 | `document_protocols=IEEE 802.15.4; Zigbee 3.0; Thread 1.3; Matter`；`schematic_module=ESP32-H2-MINI-1-N2`；`firmware=not shown`；`protocol_versions=not shown` |
| 核心器件 | CPU 与硬件加密能力 | `document_cpu=32-bit single-core RISC-V`；`document_frequency=up to 96MHz`；`document_security=hardware encryption engine`；`schematic_details=not shown` |
| 电源 | 待机与 Thread 组网电流 | `document_standby=3.3V / 8.55mA`；`document_thread=3.3V / 18.35mA`；`schematic_measurement=not shown` |

## 待确认事项

- `memory.flash-capacity`：产品正文声明 2 MB Flash，原理图只给出完整模组标识 ESP32-H2-MINI-1-N2，没有在页面单独写出 Flash 容量或存储器位号。（证据：图 22340fe8b841 / 第 1 页 / M1 module marking without explicit Flash capacity）
- `rf.protocol-support`：产品正文列出 Zigbee 3.0、Thread 1.3、Matter 与 IEEE 802.15.4，但原理图只标 ESP32-H2-MINI-1-N2 和板载天线符号，未列协议版本或固件能力。（证据：图 22340fe8b841 / 第 1 页 / M1 antenna/module symbol lacks protocol table）
- `component.cpu-security`：产品正文称 32 位单核 RISC-V、最高 96 MHz 并带硬件加密引擎，这些内部架构与频率没有印在原理图页面。（证据：图 22340fe8b841 / 第 1 页 / M1 block contains pinout only）
- `power.consumption`：产品正文给出 3.3 V 待机 8.55 mA、Thread 组网 18.35 mA，但原理图没有测试条件、测量点或电流标注。（证据：图 22340fe8b841 / 第 1 页 / +3.3V input network lacks current measurement data）
- `review.flash-capacity`：请用 ESP32-H2-MINI-1-N2 对应 BOM 或官方模组规格确认板载 Flash 为 2 MB。；原因：容量来自产品正文，原理图没有明确容量字段。
- `review.protocol-support`：请用当前固件、ESP-IDF 配置和模组规格复核 Zigbee、Thread、Matter 与 IEEE 802.15.4 版本支持。；原因：协议能力由芯片与固件共同决定，原理图未列版本。
- `review.cpu-security`：请用 ESP32-H2-MINI-1-N2 对应芯片/模组 datasheet 复核 CPU 核心、主频与硬件加密能力。；原因：这些内部特性未印在原理图。
- `review.power-consumption`：请按对应固件、供电和无线测试条件复测待机与 Thread 组网电流。；原因：原理图未记录测试方法或电流值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `22340fe8b8415acb6d145b3480e9aee492d2f094be4e644acb06cdc68e395b4f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4_sch_01.png` |

---

源文档：`zh_CN/module/Module Gateway H2.md`

源文档 SHA-256：`3e21d6c894a4b01112b0159085e7b154bab0c45c00e3a6e606437b6ceeef930c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
