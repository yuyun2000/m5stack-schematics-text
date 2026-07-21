# Stamp-S3A 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3A |
| SKU | S007-V033 |
| 产品 ID | `stamp-s3a-5b8c594bed8f` |
| 源文档 | `zh_CN/core/Stamp-S3A.md` |

## 概述

Stamp-S3A 以 U1 ESP32-S3FN8 为主控，使用 40MHz 晶振、优化的 ANT1 射频匹配和原生 USB D+/D-。U4 JW5712 将 VIN_5V 转换为 VDD_3V3；U2 AW35122FDR 生成受 GPIO38/DISP_BL 控制的 BL_3V3，并同时供 LCD 背光与 U3 WS2812 RGB LED。M1 28 针接口引出 23 个 GPIO、电源、EN 与 UART，J1/J3 另提供 GPIO16-18 和 LCD SPI/控制信号。

## 检索关键词

`Stamp-S3A`、`S007-V033`、`ESP32-S3FN8`、`STAMP-S3M`、`JW5712`、`MUN3CAD01-SC`、`AW35122FDR`、`WS2812`、`BL_3V3`、`ANT1`、`VIN_5V`、`VDD_3V3`、`GPIO0`、`GPIO46`、`USB_DU_P`、`USB_DU_N`、`DISP_RST`、`DISP_RS`、`DISP_MOSI`、`DISP_SCK`、`DISP_CS`、`DISP_BL`、`SK_DIN`、`40MHz`、`USB Type-C`、`1.27mm`、`2.54mm`、`M1 28-pin`、`J1 12-pin`、`J3 8-pin`、`ESP_EN`、`native USB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | 主控 SoC，提供原生 USB、GPIO、UART、RGB 与 LCD 控制 | 图 1156e645de35 / 第 1 页 / A2-C2 ESP32 区，U1 ESP32-S3FN8 |
| U4 | JW5712 | VIN_5V 至 VDD_3V3 的 0~0.6A DC-DC 转换器 | 图 1156e645de35 / 第 1 页 / D1-D2 DCDC 区，U4 JW5712 |
| U2 | AW35122FDR | 受 DISP_BL 控制的 BL_3V3 电源开关，为 LCD 背光和 RGB LED 供电 | 图 1156e645de35 / 第 1 页 / A3 LCD 区，U2 AW35122FDR |
| U3 | WS2812 | GPIO21/SK_DIN 控制的可编程 RGB LED，电源为 BL_3V3 | 图 1156e645de35 / 第 1 页 / B3 RGB LED 区，U3 WS2812 |
| ANT1 | ANT1 | ESP32 射频天线，配套 L6/C19/C20/L1/C2/C1 匹配网络 | 图 1156e645de35 / 第 1 页 / A1 射频区，ANT1 与匹配网络 |
| X1 | 40MHz | ESP32-S3 主时钟晶振 | 图 1156e645de35 / 第 1 页 / B1，X1 40MHz |
| S1 | SMT_SW_1TS026A | GPIO0 用户/BOOT 按键 | 图 1156e645de35 / 第 1 页 / B3-C3 BTN-USER 区 |
| M1 | STAMP-S3M | 28 针模组接口，引出 23 GPIO、VIN_5V、VDD_3V3、EN、UART 与 GND | 图 1156e645de35 / 第 1 页 / B4-C4 M1 STAMP-S3M pins 1-28 |
| J2 | USB-TYPEC | USB Type-C 5V 输入与原生 USB 数据接口 | 图 1156e645de35 / 第 1 页 / D4 Type-A USB 区，J2 USB-TYPEC |
| J1 | HDGC/0.5K-HX-12PWB/NC | 12 针 LCD/扩展 FPC，引出 VIN_5V、GPIO16-18 与显示信号 | 图 1156e645de35 / 第 1 页 / A4 J1 12-pin |
| J3 | HDGC/0.5K-HX-8PWB/NC | 8 针 LCD FPC，提供 BL_3V3、GND、SPI 与控制信号 | 图 1156e645de35 / 第 1 页 / A3-A4 J3 8-pin |
| F1 | 6V/1A/PPTC | USB VCC 到 VIN_5V 的自恢复保险丝 | 图 1156e645de35 / 第 1 页 / D4 F1 6V/1A/PPTC |
| D1/D3/D5/D7/D14 | PESDNC2FD3V3B/PESDNC2FD5VB | GPIO0、USB 数据及模组电源的 ESD/浪涌保护 | 图 1156e645de35 / 第 1 页 / B3 D1；C4 D7；D4 D3/D5/D14 |

## 系统结构

### Stamp-S3A 架构

ESP32-S3FN8 使用 40MHz 晶振、优化天线和原生 USB；JW5712 生成 VDD_3V3，AW35122FDR 生成 BL_3V3 并为 LCD 背光与 WS2812 供电，M1/J1/J3 引出 GPIO 和显示接口。

- 参数与网络：`mcu=U1 ESP32-S3FN8`；`dcdc=U4 JW5712`；`backlight_switch=U2 AW35122FDR`；`rgb=U3 WS2812`；`connector=M1 STAMP-S3M`；`usb=J2 USB-TYPEC`
- 证据：图 1156e645de35 / 第 1 页 / 完整原理图页

## 核心器件

### U1 ESP32-S3FN8

U1 明确标 ESP32-S3FN8，CHIP_PU 经 L7 0R 接 ESP_EN，VDD_SPI 接 FLASH_VCC，GPIO19/20 为 USB，GPIO21 为 SK_DIN。

- 参数与网络：`reference=U1`；`part_number=ESP32-S3FN8`；`enable=ESP_EN via L7 0R`；`flash_power=FLASH_VCC`；`usb=GPIO19/20`；`rgb=GPIO21`
- 证据：图 1156e645de35 / 第 1 页 / A2-C2 U1

## 电源

### U4 JW5712 DC-DC

U4 JW5712 以 VIN_5V 为输入，经 L4 MWTC201608S2R2 生成 VDD_3V3，原理图标注 IOUT 0~0.6A；VSEL1/2/3 接 VIN_5V。

- 参数与网络：`reference=U4`；`part_number=JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`current_label=0~0.6A`；`select=VSEL1/VSEL2/VSEL3=VIN_5V`
- 证据：图 1156e645de35 / 第 1 页 / D1-D2 DCDC 区

### BL_3V3 背光/RGB 复用

U2 AW35122FDR 以 VDD_3V3 为 VIN、DISP_BL 为 EN，输出 BL_3V3；BL_3V3 同时连接 J3 pin 8 背光电源和 U3 WS2812 VDD。

- 参数与网络：`switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL / GPIO38`；`output=BL_3V3`；`loads=J3 pin 8; U3 WS2812 VDD`
- 证据：图 1156e645de35 / 第 1 页 / A3 LCD 区与 B3 RGB LED 区

## 接口

### J2 USB Type-C

J2 VCC 经 F1 6V/1A PPTC 接 VIN_5V，A6/B6 汇为 USB_D_P，A7/B7 汇为 USB_D_N，CC1/CC2 经 R1/R2 5.1K 接地。

- 参数与网络：`reference=J2`；`power=VCC -> F1 -> VIN_5V`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R2 5.1K to GND`
- 证据：图 1156e645de35 / 第 1 页 / D3-D4 USB 区

### M1 STAMP-S3M 28 针接口

M1 pins 1-17 引出 GPIO1-15、GND 与 VIN_5V；pins 18-28 引出 GND、GPIO39、GPIO0、GPIO40、EN、GPIO41、RX/GPIO44、GPIO42、TX/GPIO43、GPIO46 与 VDD_3V3。

- 参数与网络：`reference=M1`；`left=1:G1...10:G10,11:GND,12:G11,13:5V,14:G12,15:G13,16:G14,17:G15`；`right=18:GND,19:G39,20:G0,21:G40,22:EN,23:G41,24:G44/RX,25:G42,26:G43/TX,27:G46,28:3V3`；`gpio_count=23`
- 证据：图 1156e645de35 / 第 1 页 / B4-C4 M1 pins 1-28

### J1/J3 LCD FPC

J3 8 针接口承载 BL_3V3、GND、DISP_RST/RS/MOSI/SCK、VDD_3V3 与 DISP_CS；J1 12 针接口另引出 VIN_5V、GPIO16/17/18。

- 参数与网络：`j3=8-pin 0.5mm`；`j3_signals=BL_3V3,GND,DISP_RST,DISP_RS,DISP_MOSI,DISP_SCK,VDD_3V3,DISP_CS`；`j1=12-pin 0.5mm`；`j1_extra=VIN_5V,GPIO16,GPIO17,GPIO18`
- 证据：图 1156e645de35 / 第 1 页 / A3-A4 J3/J1

## 总线

### ESP32-S3 原生 USB

GPIO20 USB_DU_P 与 GPIO19 USB_DU_N 经 L5 共模器件连接 J2 USB_D_P/N，D3/D5 提供 ESD 保护，图中无 USB-UART 桥。

- 参数与网络：`controller=U1 ESP32-S3FN8`；`dp=GPIO20 / USB_DU_P`；`dm=GPIO19 / USB_DU_N`；`filter=L5`；`protection=D3/D5 PESDNC2FD3V3B`；`bridge=null`
- 证据：图 1156e645de35 / 第 1 页 / B2 U1 GPIO19/20 与 D3-D4 USB

### LCD SPI/控制

GPIO33/34/35/36/37/38 分别为 DISP_RST/RS/MOSI/SCK/CS/BL，并引出 J3/J1；图中未画 MISO。

- 参数与网络：`reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight=GPIO38`；`miso=null`
- 证据：图 1156e645de35 / 第 1 页 / B2 U1 GPIO33-38 与 A3-A4 LCD

## GPIO 与控制信号

### GPIO0 用户/BOOT 按键

S1 按下将 GPIO0 接地，R4 10K 上拉至 VDD_3V3，D1 PESDNC2FD3V3B 对地保护；M1 pin 20 引出 G0/Boot。

- 参数与网络：`gpio=GPIO0`；`switch=S1 SMT_SW_1TS026A`；`pullup=R4 10K`；`protection=D1 PESDNC2FD3V3B`；`connector=M1 pin 20`
- 证据：图 1156e645de35 / 第 1 页 / B3-C3 BTN-USER 与 C4 M1

### WS2812 RGB LED

U3 WS2812 DI 接 SK_DIN/GPIO21，VDD 接 BL_3V3，DO 为 SK_DOUT，C17 10uF 去耦。

- 参数与网络：`reference=U3`；`gpio=GPIO21 / SK_DIN`；`power=BL_3V3`；`data_out=SK_DOUT`；`capacitor=C17 10uF`
- 证据：图 1156e645de35 / 第 1 页 / B3 RGB LED 区

### 23 GPIO 引出

M1 引出 GPIO0-GPIO15、GPIO39-GPIO44 与 GPIO46，共 23 路；GPIO43/44 标为 TX/RX。

- 参数与网络：`gpios=GPIO0-GPIO15; GPIO39-GPIO44; GPIO46`；`count=23`；`tx=GPIO43`；`rx=GPIO44`
- 证据：图 1156e645de35 / 第 1 页 / U1 GPIO 与 M1 映射

## 时钟

### ESP32-S3 主时钟

U1 XTAL_P/XTAL_N 连接 X1 40MHz 晶振，L3 10nH 串联于 XTAL_40M_P，C9/C14 各 12pF 接地。

- 参数与网络：`crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF`；`nets=XTAL_40M_P/XTAL_40M_N`
- 证据：图 1156e645de35 / 第 1 页 / B1-B2 X1

## 复位

### ESP_EN

U1 CHIP_PU 经 L7 0R 接 ESP_EN，C24 3pF 对地；ESP_EN 由 R7 10K 上拉至 VDD_3V3、C23 1uF 对地，并引出 M1 EN。

- 参数与网络：`mcu_pin=CHIP_PU`；`net=ESP_EN`；`series=L7 0R`；`chip_cap=C24 3pF`；`pullup=R7 10K`；`reset_cap=C23 1uF`；`connector=M1 pin 22 EN`
- 证据：图 1156e645de35 / 第 1 页 / A2 U1 CHIP_PU 与 D1 ESP_EN

## 保护电路

### USB 与电源保护

USB_D_P/N 由 D3/D5 PESDNC2FD3V3B 保护，VIN_5V 由 D14 PESDNC2FD5VB 钳位并串联 F1 6V/1A PPTC。

- 参数与网络：`data_esd=D3/D5 PESDNC2FD3V3B`；`power_tvs=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC`
- 证据：图 1156e645de35 / 第 1 页 / D3-D4 USB 区

## 关键网络

### GPIO46 启动脚

U1 GPIO46 直接连接 M1 pin 27，原理图未画外部上下拉。

- 参数与网络：`gpio=GPIO46`；`connector=M1 pin 27`；`external_bias_visible=false`
- 证据：图 1156e645de35 / 第 1 页 / C2 U1 GPIO46 与 C4 M1

## 射频

### 天线匹配网络

ESP_LNA 经 L1 2.7nH 与 C2 2.2pF、C1 1.8pF 连接 ANT1，天线侧另有 L6 0R、C19 4.3nH 标注与 C20 NC 匹配位。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1`；`main_match=L1 2.7nH; C2 2.2pF; C1 1.8pF`；`antenna_side=L6 0R; C19 4.3nH(as drawn); C20 NC`
- 证据：图 1156e645de35 / 第 1 页 / A1 射频区

## 调试与烧录

### UART 引出

U1 U0TXD/U0RXD 经 R5 510R 网络连接 TX/RX，并分别引出 M1 GPIO43 pin 26 与 GPIO44 pin 24。

- 参数与网络：`tx=U0TXD -> TX -> GPIO43/M1-26`；`rx=U0RXD -> RX -> GPIO44/M1-24`；`series=R5 510R/1%`
- 证据：图 1156e645de35 / 第 1 页 / C2 U1 UART 与 C4 M1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3A 架构 | `mcu=U1 ESP32-S3FN8`；`dcdc=U4 JW5712`；`backlight_switch=U2 AW35122FDR`；`rgb=U3 WS2812`；`connector=M1 STAMP-S3M`；`usb=J2 USB-TYPEC` |
| 核心器件 | U1 ESP32-S3FN8 | `reference=U1`；`part_number=ESP32-S3FN8`；`enable=ESP_EN via L7 0R`；`flash_power=FLASH_VCC`；`usb=GPIO19/20`；`rgb=GPIO21` |
| 内存与 Flash | ESP32-S3FN8 Flash | `mcu=ESP32-S3FN8`；`documented_capacity=8MB`；`discrete_flash=null`；`schematic_capacity_label=null` |
| 射频 | 天线匹配网络 | `source=ESP_LNA`；`antenna=ANT1`；`main_match=L1 2.7nH; C2 2.2pF; C1 1.8pF`；`antenna_side=L6 0R; C19 4.3nH(as drawn); C20 NC` |
| 时钟 | ESP32-S3 主时钟 | `crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF`；`nets=XTAL_40M_P/XTAL_40M_N` |
| 电源 | U4 JW5712 DC-DC | `reference=U4`；`part_number=JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`current_label=0~0.6A`；`select=VSEL1/VSEL2/VSEL3=VIN_5V` |
| 核心器件 | DC-DC 型号 | `documented_part=MUN3CAD01-SC`；`schematic_part=U4 JW5712`；`schematic_revision=v0.3.3` |
| 电源 | BL_3V3 背光/RGB 复用 | `switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL / GPIO38`；`output=BL_3V3`；`loads=J3 pin 8; U3 WS2812 VDD` |
| 接口 | J2 USB Type-C | `reference=J2`；`power=VCC -> F1 -> VIN_5V`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R2 5.1K to GND` |
| 总线 | ESP32-S3 原生 USB | `controller=U1 ESP32-S3FN8`；`dp=GPIO20 / USB_DU_P`；`dm=GPIO19 / USB_DU_N`；`filter=L5`；`protection=D3/D5 PESDNC2FD3V3B`；`bridge=null` |
| GPIO 与控制信号 | GPIO0 用户/BOOT 按键 | `gpio=GPIO0`；`switch=S1 SMT_SW_1TS026A`；`pullup=R4 10K`；`protection=D1 PESDNC2FD3V3B`；`connector=M1 pin 20` |
| 复位 | ESP_EN | `mcu_pin=CHIP_PU`；`net=ESP_EN`；`series=L7 0R`；`chip_cap=C24 3pF`；`pullup=R7 10K`；`reset_cap=C23 1uF`；`connector=M1 pin 22 EN` |
| GPIO 与控制信号 | WS2812 RGB LED | `reference=U3`；`gpio=GPIO21 / SK_DIN`；`power=BL_3V3`；`data_out=SK_DOUT`；`capacitor=C17 10uF` |
| 接口 | M1 STAMP-S3M 28 针接口 | `reference=M1`；`left=1:G1...10:G10,11:GND,12:G11,13:5V,14:G12,15:G13,16:G14,17:G15`；`right=18:GND,19:G39,20:G0,21:G40,22:EN,23:G41,24:G44/RX,25:G42,26:G43/TX,27:G46,28:3V3`；`gpio_count=23` |
| GPIO 与控制信号 | 23 GPIO 引出 | `gpios=GPIO0-GPIO15; GPIO39-GPIO44; GPIO46`；`count=23`；`tx=GPIO43`；`rx=GPIO44` |
| 总线 | LCD SPI/控制 | `reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight=GPIO38`；`miso=null` |
| 接口 | J1/J3 LCD FPC | `j3=8-pin 0.5mm`；`j3_signals=BL_3V3,GND,DISP_RST,DISP_RS,DISP_MOSI,DISP_SCK,VDD_3V3,DISP_CS`；`j1=12-pin 0.5mm`；`j1_extra=VIN_5V,GPIO16,GPIO17,GPIO18` |
| 核心器件 | LCD 外设型号 | `connectors=J1/J3`；`driver_model=null`；`panel_model=null` |
| 调试与烧录 | UART 引出 | `tx=U0TXD -> TX -> GPIO43/M1-26`；`rx=U0RXD -> RX -> GPIO44/M1-24`；`series=R5 510R/1%` |
| 关键网络 | GPIO46 启动脚 | `gpio=GPIO46`；`connector=M1 pin 27`；`external_bias_visible=false` |
| 保护电路 | USB 与电源保护 | `data_esd=D3/D5 PESDNC2FD3V3B`；`power_tvs=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC` |

## 待确认事项

- `memory.internal-flash`：产品正文标称 8MB Flash，原理图无独立 Flash 且未以字节数标注 U1 内部容量。（证据：图 1156e645de35 / 第 1 页 / U1 与完整页，无独立 Flash/容量）
- `component.dcdc-model-conflict`：产品正文规格表称 DC-DC 为 MUN3CAD01-SC，但 v0.3.3 原理图 U4 明确标 JW5712。（证据：图 1156e645de35 / 第 1 页 / D1-D2 U4 JW5712）
- `component.lcd-model`：原理图只显示 J1/J3 FPC 与 LCD SPI/控制网络，未标具体面板或驱动器型号。（证据：图 1156e645de35 / 第 1 页 / A3-A4 LCD 区）
- `review.flash-capacity`：ESP32-S3FN8 的内部 Flash 容量是否固定为 8MB？；原因：8MB 来自正文，原理图未标字节容量。
- `review.dcdc-model`：Stamp-S3A S007-V033 的 DC-DC BOM 应为 JW5712 还是 MUN3CAD01-SC？；原因：v0.3.3 原理图与产品正文规格表冲突。
- `review.lcd-model`：J1/J3 对应的官方 LCD 面板与驱动器型号是什么？；原因：原理图只给出 FPC 与信号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |

---

源文档：`zh_CN/core/Stamp-S3A.md`

源文档 SHA-256：`c7ad14b925a7edbad1179609ffe85f7d9de90ce1d1fd5025a49e6fe583b76d60`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
