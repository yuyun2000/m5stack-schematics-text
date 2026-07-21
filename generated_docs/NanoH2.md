# NanoH2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | NanoH2 |
| SKU | C149 |
| 产品 ID | `nanoh2-6dd9fc2743d5` |
| 源文档 | `zh_CN/core/NanoH2.md` |

## 概述

NanoH2 v0.0.3 以 ESP32-H2FH4S 为主控，USB Type-C 数据线直连片上 USB，经 AW32901FCR 过压保护和 JW5712 降压生成 VDD_3V3；板上还包含 32 MHz 晶振、2.4 GHz 天线匹配、HY-2.0 Grove、GPIO9 下载按键、AW35122FDR 门控的 WS2812、GPIO3 红外 LED 与 GPIO4 蓝色 LED。

## 检索关键词

`NanoH2`、`C149`、`v0.0.3`、`ESP32-H2FH4S`、`ESP32-H2`、`ESP32-C6FH4`、`USB Type-C`、`TYPEC-304S-ACP16`、`AW32901FCR`、`JW5712`、`MWTC201608S2R2`、`VDD_3V3`、`ANT016008LCS2442MA2`、`32MHz`、`HY-2.0`、`GPIO1`、`GPIO2`、`GPIO9`、`GPIO10 RGBPWR`、`GPIO11 RGB`、`AW35122FDR`、`WS2812`、`GPIO3 IR`、`GPIO4 Blue LED`、`PESDNC2FD3V3B`、`Zigbee`、`Thread`、`Matter`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-H2FH4S | NanoH2 主控制器，集成 USB 和射频接口 | 图 b893c5d803b3 / 第 1 页 / B1-C2 SoC:ESP32-H2FH4S 区域 U3 主控符号 |
| USB1 | TYPEC-304S-ACP16 | USB Type-C 供电与数据接口 | 图 b893c5d803b3 / 第 1 页 / A1-A2 Type-C 区域 USB1 TYPEC-304S-ACP16 |
| U4 | AW32901FCR | USB VBUS 输入过压保护开关 | 图 b893c5d803b3 / 第 1 页 / A2 OVP 区域 U4 AW32901FCR、VBUSIN 与 VBUS |
| U1 | JW5712 | VBUS 至 VDD_3V3 同步降压转换器 | 图 b893c5d803b3 / 第 1 页 / A3-A4 DCDC 3.3V 区域 U1 JW5712、L6 与 VDD_3V3 |
| ANT1 | ANT016008LCS2442MA2 | ESP32-H2 射频天线 | 图 b893c5d803b3 / 第 1 页 / B1-B3 U3 ANT 至 ANT1 的 L/C 匹配网络 |
| X1 | 32MHz | ESP32-H2 主晶振 | 图 b893c5d803b3 / 第 1 页 / C1-C2 X1 32MHz、L3、C3/C4 与 XTAL_P/N |
| J1 | HY-2.0 | GPIO1/GPIO2 Grove 扩展接口 | 图 b893c5d803b3 / 第 1 页 / B3-B4 Grove 区域 J1 HY-2.0 |
| S1 | SMT_SW_PTS_820 | GPIO9 用户与下载模式按键 | 图 b893c5d803b3 / 第 1 页 / C3-C4 Button 区域 S1、GPIO9 与启动模式表 |
| U6 | AW35122FDR | GPIO10 控制的 RGB 电源负载开关 | 图 b893c5d803b3 / 第 1 页 / D1-D2 RGB LED 区域 U6 AW35122FDR、RGBPWR 与 F3V3 |
| U2 | WS2812 | GPIO11 控制的可编程 RGB LED | 图 b893c5d803b3 / 第 1 页 / D2 RGB LED 区域 U2 WS2812、F3V3 与 RGB |
| IR1/LED1 | IR/Blue LED | GPIO3 红外发射与 GPIO4 蓝色状态指示 | 图 b893c5d803b3 / 第 1 页 / D3-D4 IR&LED 区域 IR1、LED1、R1/R9 |

## 系统结构

### NanoH2 主控制器

U3 原理图器件型号明确标为 ESP32-H2FH4S，CHIP_PU 经 R8 0 Ω 连接 EN，USB_D-/USB_D+ 分别为 GPIO26/GPIO27，射频端 ANT 接外部匹配网络。

- 参数与网络：`reference=U3`；`part_number=ESP32-H2FH4S`；`enable=CHIP_PU to EN via R8 0R`；`usb_d_minus=GPIO26 USB_D_N`；`usb_d_plus=GPIO27 USB_D_P`；`rf=ANT`
- 证据：图 b893c5d803b3 / 第 1 页 / B1-C2 SoC 区域 U3 ESP32-H2FH4S、R8、USB 与 ANT 引脚

## 电源

### USB VBUS 过压保护

U4 AW32901FCR 的三路 IN 接 VBUSIN、三路 OUT 接 VBUS，输入和输出分别由 C26/C27 1 µF 去耦。

- 参数与网络：`reference=U4`；`part_number=AW32901FCR`；`input=VBUSIN`；`output=VBUS`；`input_capacitor=C26 1uF`；`output_capacitor=C27 1uF`
- 证据：图 b893c5d803b3 / 第 1 页 / A2 OVP 区域 U4、VBUSIN/VBUS 与 C26/C27

### JW5712 3.3V 电源

U1 JW5712 以 VBUS 为 VIN，EN 由 R6 10 kΩ 上拉，SW 经 L6 MWTC201608S2R2 输出 VDD_3V3；C17/C18 各 10 µF、C16 100 nF 提供输出滤波，D7 PESDNC2FD3V3B 对 VDD_3V3 提供保护。

- 参数与网络：`converter=U1 JW5712`；`input=VBUS`；`enable_pullup=R6 10k`；`inductor=L6 MWTC201608S2R2`；`output=VDD_3V3`；`output_capacitors=C17=10uF,C18=10uF,C16=100nF`；`esd=D7 PESDNC2FD3V3B`
- 证据：图 b893c5d803b3 / 第 1 页 / A3-A4 DCDC 3.3V 区域 U1、R6、L6、C16-C18 与 D7

### RGB 电源门控

U6 AW35122FDR 以 VDD_3V3 为 VIN，EN 接 RGBPWR/GPIO10，VOUT 生成 F3V3 为 WS2812 供电；C1/C5 各 10 µF 提供输入输出滤波。

- 参数与网络：`switch=U6 AW35122FDR`；`input=VDD_3V3`；`enable=GPIO10 RGBPWR`；`output=F3V3`；`capacitors=C1=10uF,C5=10uF`
- 证据：图 b893c5d803b3 / 第 1 页 / D1-D2 RGB LED 区域 U6、C1/C5、RGBPWR 与 F3V3

## 接口

### USB Type-C 数据与 CC

USB1 为 TYPEC-304S-ACP16，A6/B6 并接 USB_D_P，A7/B7 并接 USB_D_N；CC1/CC2 分别经 R3/R4 5.1 kΩ 下拉到 GND，VBUS 经 F1 6V/1A PTC 输出 VBUSIN。

- 参数与网络：`connector=USB1 TYPEC-304S-ACP16`；`d_plus=A6,B6 to USB_D_P`；`d_minus=A7,B7 to USB_D_N`；`cc1_pulldown=R3 5.1k`；`cc2_pulldown=R4 5.1k`；`vbus_protection=F1 6V/1A PTC to VBUSIN`
- 证据：图 b893c5d803b3 / 第 1 页 / A1-A2 Type-C 区域 USB1、F1、R3/R4 与 USB_D_P/N

### HY-2.0 Grove 接口

J1 HY-2.0 的 1-4 脚依次为 IO1/GPIO1、IO2/GPIO2、+5V/VBUS、GND；GPIO1、GPIO2 与 VBUS 分别由 D4、D5、D6 PESDNC2FD3V3B 对地保护。

- 参数与网络：`connector=J1 HY-2.0`；`pinout=1:GPIO1,2:GPIO2,3:VBUS,4:GND`；`esd=D4:GPIO1,D5:GPIO2,D6:VBUS`
- 证据：图 b893c5d803b3 / 第 1 页 / B3-B4 Grove 区域 J1、GPIO1/GPIO2/VBUS 与 D4-D6

## GPIO 与控制信号

### 主要 GPIO 功能映射

GPIO1/GPIO2 接 Grove IO1/IO2，GPIO3=IR，GPIO4=Blue LED，GPIO9 接按键，GPIO10=RGBPWR，GPIO11=RGB，GPIO23/U0RXD=URX，GPIO24/U0TXD=UTX。

- 参数与网络：`grove=GPIO1:IO1,GPIO2:IO2`；`ir=GPIO3`；`blue_led=GPIO4`；`button=GPIO9`；`rgb_power=GPIO10 RGBPWR`；`rgb_data=GPIO11 RGB`；`uart_rx=GPIO23 URX`；`uart_tx=GPIO24 UTX`
- 证据：图 b893c5d803b3 / 第 1 页 / B1-C2 U3 左侧 GPIO1-11 与 GPIO23/24 外部网络名

### WS2812 RGB LED

U2 WS2812 的 VDD 接 F3V3，DI 接 RGB/GPIO11，DO 标为未连接，GND 接地。

- 参数与网络：`reference=U2`；`part_number=WS2812`；`supply=F3V3`；`data_input=GPIO11 RGB`；`data_output=NC`
- 证据：图 b893c5d803b3 / 第 1 页 / D2 U2 WS2812、F3V3、RGB 与 DO 未连接标记

### 红外与蓝色 LED

GPIO3 通过 IR1 红外 LED 和 R1 22 Ω 接地；GPIO4 通过 LED1 Blue 和 R9 22 Ω 接地。

- 参数与网络：`ir=GPIO3-IR1-R1 22R-GND`；`blue_led=GPIO4-LED1-R9 22R-GND`
- 证据：图 b893c5d803b3 / 第 1 页 / D3-D4 IR&LED 区域 GPIO3/IR1/R1 与 GPIO4/LED1/R9

## 时钟

### 32 MHz 主晶振

X1 标注 32 MHz，XTAL_P 侧串联 L3 24 nH/TBD 并由 C3 12 pF/TBD 接地，XTAL_N 侧由 C4 10 pF 接地。

- 参数与网络：`reference=X1`；`frequency_hz=32000000`；`xtal_p_series=L3 24nH/TBD`；`xtal_p_capacitor=C3 12pF/TBD`；`xtal_n_capacitor=C4 10pF`
- 证据：图 b893c5d803b3 / 第 1 页 / C1-C2 X1 32MHz、L3、C3/C4 与 U3 XTAL_P/N

## 复位

### GPIO9 下载模式按键

GPIO9 由 R2 10 kΩ 上拉至 VDD_3V3，并由 S1 按下接地，D1 PESDNC2FD3V3B 提供保护；启动模式表标明 GPIO9=0 且 GPIO8=1 时进入 Joint Download Boot。

- 参数与网络：`button=S1 SMT_SW_PTS_820`；`gpio=GPIO9`；`pullup=R2 10k`；`esd=D1 PESDNC2FD3V3B`；`download_condition=GPIO8=1,GPIO9=0`
- 证据：图 b893c5d803b3 / 第 1 页 / C3-C4 Button 区域 R2、S1、D1 与 Boot Mode 表

## 保护电路

### USB 数据 ESD 保护

USB_D_P 与 USB_D_N 分别由 D2、D3 PESDNC2FD3V3B 对地保护。

- 参数与网络：`d_plus_esd=D2 PESDNC2FD3V3B`；`d_minus_esd=D3 PESDNC2FD3V3B`
- 证据：图 b893c5d803b3 / 第 1 页 / A1-A2 USB_D_P/N 旁 D2/D3 PESDNC2FD3V3B

## 射频

### ESP32-H2 天线匹配

U3 ANT 经 L5 2.4 nH、C22 1.7 pF、C21 1.2 pF、C23 1.3 pF、L2 3.7 nH 和 L1 0 Ω 连接 ANT1 ANT016008LCS2442MA2。

- 参数与网络：`antenna=ANT1 ANT016008LCS2442MA2`；`series=L5 2.4nH,C23 1.3pF,L1 0R`；`shunt=C22 1.7pF,C21 1.2pF,L2 3.7nH`
- 证据：图 b893c5d803b3 / 第 1 页 / B1-B3 U3 ANT 至 ANT1 的 L5/C22/C21/C23/L2/L1 匹配链

## 调试与烧录

### UART 与使能测试焊盘

UTX、URX 和 EN 分别引出至 JP2、JP3 和 JP1 焊盘。

- 参数与网络：`uart_tx=UTX JP2`；`uart_rx=URX JP3`；`enable=EN JP1`
- 证据：图 b893c5d803b3 / 第 1 页 / B2-B3 UTX JP2、URX JP3 与 EN JP1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 接口 | USB Type-C 数据与 CC | `connector=USB1 TYPEC-304S-ACP16`；`d_plus=A6,B6 to USB_D_P`；`d_minus=A7,B7 to USB_D_N`；`cc1_pulldown=R3 5.1k`；`cc2_pulldown=R4 5.1k`；`vbus_protection=F1 6V/1A PTC to VBUSIN` |
| 保护电路 | USB 数据 ESD 保护 | `d_plus_esd=D2 PESDNC2FD3V3B`；`d_minus_esd=D3 PESDNC2FD3V3B` |
| 电源 | USB VBUS 过压保护 | `reference=U4`；`part_number=AW32901FCR`；`input=VBUSIN`；`output=VBUS`；`input_capacitor=C26 1uF`；`output_capacitor=C27 1uF` |
| 电源 | JW5712 3.3V 电源 | `converter=U1 JW5712`；`input=VBUS`；`enable_pullup=R6 10k`；`inductor=L6 MWTC201608S2R2`；`output=VDD_3V3`；`output_capacitors=C17=10uF,C18=10uF,C16=100nF`；`esd=D7 PESDNC2FD3V3B` |
| 系统结构 | NanoH2 主控制器 | `reference=U3`；`part_number=ESP32-H2FH4S`；`enable=CHIP_PU to EN via R8 0R`；`usb_d_minus=GPIO26 USB_D_N`；`usb_d_plus=GPIO27 USB_D_P`；`rf=ANT` |
| GPIO 与控制信号 | 主要 GPIO 功能映射 | `grove=GPIO1:IO1,GPIO2:IO2`；`ir=GPIO3`；`blue_led=GPIO4`；`button=GPIO9`；`rgb_power=GPIO10 RGBPWR`；`rgb_data=GPIO11 RGB`；`uart_rx=GPIO23 URX`；`uart_tx=GPIO24 UTX` |
| 射频 | ESP32-H2 天线匹配 | `antenna=ANT1 ANT016008LCS2442MA2`；`series=L5 2.4nH,C23 1.3pF,L1 0R`；`shunt=C22 1.7pF,C21 1.2pF,L2 3.7nH` |
| 时钟 | 32 MHz 主晶振 | `reference=X1`；`frequency_hz=32000000`；`xtal_p_series=L3 24nH/TBD`；`xtal_p_capacitor=C3 12pF/TBD`；`xtal_n_capacitor=C4 10pF` |
| 调试与烧录 | UART 与使能测试焊盘 | `uart_tx=UTX JP2`；`uart_rx=URX JP3`；`enable=EN JP1` |
| 接口 | HY-2.0 Grove 接口 | `connector=J1 HY-2.0`；`pinout=1:GPIO1,2:GPIO2,3:VBUS,4:GND`；`esd=D4:GPIO1,D5:GPIO2,D6:VBUS` |
| 复位 | GPIO9 下载模式按键 | `button=S1 SMT_SW_PTS_820`；`gpio=GPIO9`；`pullup=R2 10k`；`esd=D1 PESDNC2FD3V3B`；`download_condition=GPIO8=1,GPIO9=0` |
| 电源 | RGB 电源门控 | `switch=U6 AW35122FDR`；`input=VDD_3V3`；`enable=GPIO10 RGBPWR`；`output=F3V3`；`capacitors=C1=10uF,C5=10uF` |
| GPIO 与控制信号 | WS2812 RGB LED | `reference=U2`；`part_number=WS2812`；`supply=F3V3`；`data_input=GPIO11 RGB`；`data_output=NC` |
| GPIO 与控制信号 | 红外与蓝色 LED | `ir=GPIO3-IR1-R1 22R-GND`；`blue_led=GPIO4-LED1-R9 22R-GND` |
| 核心器件 | 源文档 SoC 型号冲突 | `schematic=ESP32-H2FH4S`；`source_description=ESP32-H2FH4S`；`source_pinmap_header=ESP32-C6FH4` |
| 存储 | 4MB Flash 实现方式 | `source_document_capacity=4MB`；`schematic_soc=ESP32-H2FH4S`；`external_flash=not shown` |
| 电源 | Grove 最大带载能力 | `source_document=DC 4.43V@2A,5min,25.2C`；`schematic_rail=J1 pin3 VBUS`；`input_protection=F1 6V/1A PTC and U4 AW32901FCR` |
| 射频 | 红外发射距离 | `source_document=0deg:395cm,45deg:70cm,90deg:10cm`；`schematic_drive=GPIO3-IR1-R1 22R-GND`；`emitter_part_number=not specified` |

## 待确认事项

- `component.soc-document-conflict`：正式原理图 U3 与源文档描述/规格均指向 ESP32-H2FH4S，但源文档管脚映射表表头写 ESP32-C6FH4；该表头是否为复制错误需确认。（证据：图 b893c5d803b3 / 第 1 页 / B1-C2 原理图标题 SoC:ESP32-H2FH4S 与 U3 ESP32-H2FH4S）
- `storage.integrated-flash`：源文档标注 4MB Flash，原理图只绘制 U3 ESP32-H2FH4S 且没有独立 Flash 器件；Flash 是否集成于该封装及其实际容量需由器件资料或 BOM 确认。（证据：图 b893c5d803b3 / 第 1 页 / B1-C3 SoC 区域仅有 U3 ESP32-H2FH4S，无独立 Flash 器件）
- `power.grove-load-limit`：源文档标注 Grove 最大带载 DC 4.43V@2A，并给出 5 分钟和 25.2℃ 条件；原理图只显示 J1 的 +5V/VBUS、AW32901FCR 和输入 PTC，未给出该性能限制的完整测试边界。（证据：图 b893c5d803b3 / 第 1 页 / A1-B4 F1/U4 VBUS 电源路径与 J1 Grove +5V 引脚）
- `rf.ir-distance`：源文档给出 0°/45°/90° 下 395 cm/70 cm/10 cm 的红外距离，但原理图只显示 GPIO3、IR1 与 R1 22 Ω，未给出 IR1 具体料号、驱动电流公差和测试环境。（证据：图 b893c5d803b3 / 第 1 页 / D3-D4 IR1 仅标 IR，串联 R1 22R，未标料号或光学参数）
- `review.soc-document-conflict`：NanoH2 源文档管脚映射表中的 ESP32-C6FH4 是否应更正为 ESP32-H2FH4S？；原因：正式原理图和源文档主体均为 ESP32-H2FH4S，只有管脚表表头出现 ESP32-C6FH4。
- `review.integrated-flash`：U3 ESP32-H2FH4S 是否集成源文档所述 4MB Flash，实际容量如何由 BOM 或器件资料确认？；原因：原理图没有独立 Flash 器件，也未直接标注容量。
- `review.grove-load-limit`：Grove DC 4.43V@2A 最大带载指标的输入电压、保护器件温升和持续时间边界是什么？；原因：原理图未给出性能测试条件，且输入路径含 6V/1A PTC 与 AW32901FCR。
- `review.ir-distance`：NanoH2 红外距离指标所用 IR1 料号、电流、载波和环境条件是什么？；原因：原理图只标 IR1 与 R1 22 Ω，不能还原光学测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b893c5d803b36526297c161bbabdba4507277a2c86da4d7355e672c0c699b5f8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/SCH_M5NanoH2_v0.0.3_2025_08_20_17_17_26_page_01.png` |

---

源文档：`zh_CN/core/NanoH2.md`

源文档 SHA-256：`130aceaba5160349ea0cc9e1b5085d9afa50a7bfa325ceedadf7968407ad471c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
