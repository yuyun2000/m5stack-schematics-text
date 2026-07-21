# Stamp-S3A PIN2.54 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3A PIN2.54 |
| SKU | S007-PIN254-V033 |
| 产品 ID | `stamp-s3a-pin2-54-7a199e4470e6` |
| 源文档 | `zh_CN/core/Stamp-S3A_PIN254.md` |

## 概述

Stamp-S3A PIN2.54 复用 v0.3.3 电路，以 U1 ESP32-S3FN8 为主控，使用 40MHz 晶振、优化 ANT1 匹配与原生 USB。U4 JW5712 从 VIN_5V 生成 VDD_3V3，U2 AW35122FDR 生成 BL_3V3，并同时为 LCD 背光与 U3 WS2812 供电。M1 28 针电气接口引出 23 个 GPIO、电源、EN 与 UART，J1/J3 提供 GPIO16-18 和 LCD SPI/控制信号；2.54mm SMT 属机械装配信息，原理图未标接口间距。

## 检索关键词

`Stamp-S3A PIN2.54`、`S007-PIN254-V033`、`ESP32-S3FN8`、`STAMP-S3M`、`JW5712`、`MUN3CAD01-SC`、`AW35122FDR`、`WS2812`、`BL_3V3`、`ANT1`、`VIN_5V`、`VDD_3V3`、`GPIO0`、`GPIO46`、`USB_DU_P`、`USB_DU_N`、`DISP_RST`、`DISP_RS`、`DISP_MOSI`、`DISP_SCK`、`DISP_CS`、`DISP_BL`、`SK_DIN`、`40MHz`、`USB Type-C`、`2.54mm SMT`、`M1 28-pin`、`J1 12-pin`、`J3 8-pin`、`ESP_EN`、`native USB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | 主控 SoC，提供原生 USB、GPIO、UART、RGB 与 LCD 控制 | 图 1156e645de35 / 第 1 页 / A2-C2 ESP32 区，U1 ESP32-S3FN8 |
| U4 | JW5712 | VIN_5V 至 VDD_3V3 的 0~0.6A DC-DC 转换器 | 图 1156e645de35 / 第 1 页 / D1-D2 DCDC 区，U4 JW5712 |
| U2 | AW35122FDR | 受 DISP_BL 控制的 BL_3V3 电源开关 | 图 1156e645de35 / 第 1 页 / A3 LCD 区，U2 AW35122FDR |
| U3 | WS2812 | GPIO21/SK_DIN 控制的 RGB LED，电源为 BL_3V3 | 图 1156e645de35 / 第 1 页 / B3 RGB LED 区 |
| ANT1 | ANT1 | ESP32 射频天线与优化匹配网络 | 图 1156e645de35 / 第 1 页 / A1 ANT1 与 L6/C19/C20/L1/C2/C1 |
| X1 | 40MHz | ESP32-S3 主时钟晶振 | 图 1156e645de35 / 第 1 页 / B1 X1 40MHz |
| S1 | SMT_SW_1TS026A | GPIO0 用户/BOOT 按键 | 图 1156e645de35 / 第 1 页 / B3-C3 BTN-USER 区 |
| M1 | STAMP-S3M | 28 针电气接口，引出 23 GPIO、电源、EN、UART 与 GND | 图 1156e645de35 / 第 1 页 / B4-C4 M1 STAMP-S3M pins 1-28 |
| J2 | USB-TYPEC | USB Type-C 5V 输入和原生 USB 数据接口 | 图 1156e645de35 / 第 1 页 / D4 J2 USB-TYPEC |
| J1 | HDGC/0.5K-HX-12PWB/NC | 12 针 LCD/扩展 FPC | 图 1156e645de35 / 第 1 页 / A4 J1 12-pin |
| J3 | HDGC/0.5K-HX-8PWB/NC | 8 针 LCD FPC | 图 1156e645de35 / 第 1 页 / A3-A4 J3 8-pin |
| F1 | 6V/1A/PPTC | USB VCC 至 VIN_5V 自恢复保险丝 | 图 1156e645de35 / 第 1 页 / D4 F1 |
| D1/D3/D5/D7/D14 | PESDNC2FD3V3B/PESDNC2FD5VB | GPIO0、USB 数据及电源 ESD/浪涌保护 | 图 1156e645de35 / 第 1 页 / B3/C4/D4 保护器件 |

## 系统结构

### Stamp-S3A PIN2.54 架构

ESP32-S3FN8 使用 40MHz 晶振、优化天线与原生 USB；JW5712 生成 3.3V，AW35122FDR 生成 BL_3V3，M1/J1/J3 引出 GPIO 与显示信号。

- 参数与网络：`mcu=U1 ESP32-S3FN8`；`dcdc=U4 JW5712`；`backlight=U2 AW35122FDR`；`rgb=U3 WS2812`；`main_interface=M1 STAMP-S3M`
- 证据：图 1156e645de35 / 第 1 页 / 完整原理图页

## 核心器件

### U1 ESP32-S3FN8

U1 明确标 ESP32-S3FN8，CHIP_PU 经 L7 0R 接 ESP_EN，GPIO19/20 为原生 USB，GPIO21 为 SK_DIN。

- 参数与网络：`reference=U1`；`part_number=ESP32-S3FN8`；`enable=ESP_EN via L7 0R`；`usb=GPIO19/20`；`rgb=GPIO21`
- 证据：图 1156e645de35 / 第 1 页 / A2-C2 U1

## 电源

### U4 JW5712

U4 JW5712 以 VIN_5V 为输入，经 L4 MWTC201608S2R2 生成 VDD_3V3，图示 IOUT 0~0.6A。

- 参数与网络：`reference=U4`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`current=0~0.6A`
- 证据：图 1156e645de35 / 第 1 页 / D1-D2 DCDC 区

### BL_3V3 复用电源

U2 AW35122FDR 以 VDD_3V3 为输入、DISP_BL 为 EN，输出 BL_3V3，同时供 J3 背光和 U3 WS2812。

- 参数与网络：`switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL/GPIO38`；`output=BL_3V3`；`loads=J3 pin8; U3 VDD`
- 证据：图 1156e645de35 / 第 1 页 / A3 LCD 与 B3 RGB 区

## 接口

### J2 USB Type-C

J2 VCC 经 F1 6V/1A PPTC 接 VIN_5V，A6/B6 为 USB_D_P，A7/B7 为 USB_D_N，CC1/CC2 经 R1/R2 5.1K 接地。

- 参数与网络：`power=VCC->F1->VIN_5V`；`dp=A6/B6`；`dm=A7/B7`；`cc=R1/R2 5.1K`
- 证据：图 1156e645de35 / 第 1 页 / D3-D4 USB 区

### M1 28 针电气接口

M1 pins 1-17 引出 GPIO1-15、GND、VIN_5V；pins 18-28 引出 GND、GPIO39、GPIO0、GPIO40、EN、GPIO41、GPIO44/RX、GPIO42、GPIO43/TX、GPIO46、VDD_3V3。

- 参数与网络：`gpio_count=23`；`gpios=GPIO0-GPIO15; GPIO39-GPIO44; GPIO46`；`power=VIN_5V; VDD_3V3`；`uart=GPIO43 TX; GPIO44 RX`
- 证据：图 1156e645de35 / 第 1 页 / B4-C4 M1

### J1/J3 LCD FPC

J3 8 针承载 BL_3V3、GND、SPI/控制与 VDD_3V3；J1 12 针另引出 VIN_5V、GPIO16/17/18。

- 参数与网络：`j3=8-pin 0.5mm`；`j1=12-pin 0.5mm`；`j1_extra=VIN_5V,GPIO16,GPIO17,GPIO18`
- 证据：图 1156e645de35 / 第 1 页 / A3-A4 J1/J3

## 总线

### 原生 USB

GPIO20 USB_DU_P 与 GPIO19 USB_DU_N 经 L5 接 J2，D3/D5 提供 ESD 保护，图中无 USB-UART 桥。

- 参数与网络：`controller=ESP32-S3FN8`；`dp=GPIO20`；`dm=GPIO19`；`filter=L5`；`protection=D3/D5`；`bridge=null`
- 证据：图 1156e645de35 / 第 1 页 / B2 与 D3-D4 USB

### LCD SPI

GPIO33/34/35/36/37/38 分别为 DISP_RST/RS/MOSI/SCK/CS/BL，并引出 J3/J1；无 MISO。

- 参数与网络：`reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight=GPIO38`；`miso=null`
- 证据：图 1156e645de35 / 第 1 页 / B2 与 A3-A4 LCD

## GPIO 与控制信号

### GPIO0 BOOT 按键

S1 按下将 GPIO0 接地，R4 10K 上拉，D1 提供 ESD 保护；M1 pin20 引出 GPIO0。

- 参数与网络：`gpio=GPIO0`；`switch=S1`；`pullup=R4 10K`；`protection=D1`；`connector=M1 pin20`
- 证据：图 1156e645de35 / 第 1 页 / B3-C3 BTN-USER

### WS2812 RGB

U3 DI 接 SK_DIN/GPIO21，VDD 接 BL_3V3，DO 为 SK_DOUT。

- 参数与网络：`gpio=GPIO21`；`power=BL_3V3`；`data_out=SK_DOUT`；`capacitor=C17 10uF`
- 证据：图 1156e645de35 / 第 1 页 / B3 RGB LED

## 时钟

### ESP32 主时钟

X1 40MHz 连接 XTAL_40M_P/N，L3 10nH 串联，C9/C14 各 12pF 接地。

- 参数与网络：`crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF`
- 证据：图 1156e645de35 / 第 1 页 / B1 X1

## 复位

### ESP_EN

CHIP_PU 经 L7 0R 接 ESP_EN，R7 10K 上拉、C23 1uF 对地，M1 pin22 引出 EN。

- 参数与网络：`net=ESP_EN`；`series=L7 0R`；`pullup=R7 10K`；`capacitor=C23 1uF`；`connector=M1 pin22`
- 证据：图 1156e645de35 / 第 1 页 / A2/D1/C4 ESP_EN

## 保护电路

### USB/电源保护

D3/D5 保护 USB_D_P/N，D14 钳位 VIN_5V，F1 6V/1A PPTC 串联 USB VCC。

- 参数与网络：`data_esd=D3/D5 PESDNC2FD3V3B`；`power_tvs=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC`
- 证据：图 1156e645de35 / 第 1 页 / D3-D4 USB 区

## 关键网络

### GPIO46

GPIO46 直接连接 M1 pin27，图中未画外部上下拉。

- 参数与网络：`gpio=GPIO46`；`connector=M1 pin27`；`external_bias_visible=false`
- 证据：图 1156e645de35 / 第 1 页 / C2/C4 GPIO46

## 射频

### 优化天线匹配

ESP_LNA 经 L1 2.7nH、C2 2.2pF、C1 1.8pF 连接 ANT1，天线侧另设 L6 0R、C19 4.3nH 标注与 C20 NC。

- 参数与网络：`source=ESP_LNA`；`main_match=L1 2.7nH; C2 2.2pF; C1 1.8pF`；`antenna_side=L6 0R; C19 4.3nH(as drawn); C20 NC`；`antenna=ANT1`
- 证据：图 1156e645de35 / 第 1 页 / A1 射频区

## 调试与烧录

### UART

U0TXD/U0RXD 经 R5 510R 网络连接 M1 GPIO43/TX 与 GPIO44/RX。

- 参数与网络：`tx=GPIO43/M1-26`；`rx=GPIO44/M1-24`；`series=R5 510R`
- 证据：图 1156e645de35 / 第 1 页 / C2 UART 与 C4 M1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3A PIN2.54 架构 | `mcu=U1 ESP32-S3FN8`；`dcdc=U4 JW5712`；`backlight=U2 AW35122FDR`；`rgb=U3 WS2812`；`main_interface=M1 STAMP-S3M` |
| 核心器件 | U1 ESP32-S3FN8 | `reference=U1`；`part_number=ESP32-S3FN8`；`enable=ESP_EN via L7 0R`；`usb=GPIO19/20`；`rgb=GPIO21` |
| 内存与 Flash | ESP32-S3FN8 Flash | `mcu=ESP32-S3FN8`；`documented_capacity=8MB`；`schematic_capacity_label=null` |
| 核心器件 | 2.54mm SMT 接口形式 | `documented_pitch=2.54mm`；`documented_assembly=SMT pin header`；`schematic_interface=M1 STAMP-S3M 28-pin`；`pitch_visible=false` |
| 射频 | 优化天线匹配 | `source=ESP_LNA`；`main_match=L1 2.7nH; C2 2.2pF; C1 1.8pF`；`antenna_side=L6 0R; C19 4.3nH(as drawn); C20 NC`；`antenna=ANT1` |
| 时钟 | ESP32 主时钟 | `crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF` |
| 电源 | U4 JW5712 | `reference=U4`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`current=0~0.6A` |
| 核心器件 | DC-DC 型号 | `documented_part=MUN3CAD01-SC`；`schematic_part=JW5712`；`reference=U4` |
| 电源 | BL_3V3 复用电源 | `switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL/GPIO38`；`output=BL_3V3`；`loads=J3 pin8; U3 VDD` |
| 接口 | J2 USB Type-C | `power=VCC->F1->VIN_5V`；`dp=A6/B6`；`dm=A7/B7`；`cc=R1/R2 5.1K` |
| 总线 | 原生 USB | `controller=ESP32-S3FN8`；`dp=GPIO20`；`dm=GPIO19`；`filter=L5`；`protection=D3/D5`；`bridge=null` |
| GPIO 与控制信号 | GPIO0 BOOT 按键 | `gpio=GPIO0`；`switch=S1`；`pullup=R4 10K`；`protection=D1`；`connector=M1 pin20` |
| 复位 | ESP_EN | `net=ESP_EN`；`series=L7 0R`；`pullup=R7 10K`；`capacitor=C23 1uF`；`connector=M1 pin22` |
| GPIO 与控制信号 | WS2812 RGB | `gpio=GPIO21`；`power=BL_3V3`；`data_out=SK_DOUT`；`capacitor=C17 10uF` |
| 接口 | M1 28 针电气接口 | `gpio_count=23`；`gpios=GPIO0-GPIO15; GPIO39-GPIO44; GPIO46`；`power=VIN_5V; VDD_3V3`；`uart=GPIO43 TX; GPIO44 RX` |
| 总线 | LCD SPI | `reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight=GPIO38`；`miso=null` |
| 接口 | J1/J3 LCD FPC | `j3=8-pin 0.5mm`；`j1=12-pin 0.5mm`；`j1_extra=VIN_5V,GPIO16,GPIO17,GPIO18` |
| 核心器件 | LCD 型号 | `connectors=J1/J3`；`driver=null`；`panel=null` |
| 调试与烧录 | UART | `tx=GPIO43/M1-26`；`rx=GPIO44/M1-24`；`series=R5 510R` |
| 关键网络 | GPIO46 | `gpio=GPIO46`；`connector=M1 pin27`；`external_bias_visible=false` |
| 保护电路 | USB/电源保护 | `data_esd=D3/D5 PESDNC2FD3V3B`；`power_tvs=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC` |

## 待确认事项

- `memory.internal-flash`：产品正文标称 8MB Flash，原理图无独立 Flash 且未以字节数标注容量。（证据：图 1156e645de35 / 第 1 页 / U1 与完整页）
- `component.pin-pitch`：产品正文称该 SKU 焊接 2.54mm SMT 排针，但电气原理图只显示 M1 STAMP-S3M 28 针接口，未标机械间距或装配形式。（证据：图 1156e645de35 / 第 1 页 / B4-C4 M1，无间距/装配标注）
- `component.dcdc-conflict`：正文规格表称 MUN3CAD01-SC，但 v0.3.3 原理图 U4 明确标 JW5712。（证据：图 1156e645de35 / 第 1 页 / D1-D2 U4 JW5712）
- `component.lcd-model`：原理图只显示 LCD FPC 与信号，未标面板或驱动器型号。（证据：图 1156e645de35 / 第 1 页 / A3-A4 LCD 区）
- `review.flash-capacity`：ESP32-S3FN8 内部 Flash 是否固定为 8MB？；原因：正文标容量，原理图未标。
- `review.pin-pitch`：S007-PIN254-V033 的 M1 实装是否确定为 2.54mm SMT 排针？；原因：机械装配信息来自正文，电气图未标间距。
- `review.dcdc`：该 SKU 的 DC-DC BOM 是 JW5712 还是 MUN3CAD01-SC？；原因：v0.3.3 原理图与正文规格冲突。
- `review.lcd`：J1/J3 对应 LCD 面板与驱动器型号是什么？；原因：原理图只给 FPC 与信号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |

---

源文档：`zh_CN/core/Stamp-S3A_PIN254.md`

源文档 SHA-256：`3d713e11dc8564c87ba20f8598ca96b7925bcac8cfe632bbf55a4f446ed88578`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
