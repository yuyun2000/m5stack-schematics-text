# Stamp-S3 PIN2.54 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3 PIN2.54 |
| SKU | S007-PIN254 |
| 产品 ID | `stamp-s3-pin2-54-5c5f339edd77` |
| 源文档 | `zh_CN/core/M5StampS3 PIN2.54.md` |

## 概述

Stamp-S3 PIN2.54 以 U1 ESP32-S3FN8 为主控，配置 PROANT440 板载天线、40MHz 晶体、原生 USB Type-C、WS2812 和 GPIO0 按键。VIN_5V 经 M2 MIUN3CAD01-SC 生成 VDD_3V3，为主控、RGB 与显示接口供电。M1 STAMP-S3M 引出 GPIO0-GPIO15、GPIO39-GPIO44、GPIO46、TX/RX、EN、5V、3.3V 和 GND，J3/J1 提供 SPI LCD 和额外 GPIO16-GPIO18/VIN_5V 接口。

## 检索关键词

`Stamp-S3 PIN2.54`、`S007-PIN254`、`ESP32-S3FN8`、`MIUN3CAD01-SC`、`PROANT440`、`40MHz`、`WS2812`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`GPIO0 Button`、`GPIO21 SK_DIN`、`DISP_RST`、`DISP_RS`、`DISP_MOSI`、`DISP_SCK`、`DISP_CS`、`DISP_BL`、`GPIO33`、`GPIO34`、`GPIO35`、`GPIO36`、`GPIO37`、`GPIO38`、`TX`、`RX`、`EN`、`STAMP-S3M`、`M1`、`J3`、`J1`、`F1 6V/1A/PPTC`、`PESDNC2FD3V3B`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | 主控 SoC，连接射频、USB、RGB、按键、LCD 和全部引出 GPIO | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 A2-C2：U1 ESP32-S3FN8 |
| M2 | MIUN3CAD01-SC | VIN_5V 到 VDD_3V3 的电源转换器 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 D1-D2：M2 MIUN3CAD01-SC |
| ANT1 | PROANT440 | ESP32-S3 板载 2.4GHz 天线 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 A1：ANT1/L1/C1/C2 |
| X1 | 40MHz | ESP32-S3 主时钟晶体 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 B1：X1/L3/C9/C14 |
| J2 | USB-TYPEC | 原生 USB 数据与 5V 输入 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 D3-D4：J2/F1/R1/R2/D3/D4/D14 |
| F1 | 6V/1A/PPTC | USB VBUS 到 VIN_5V 的自恢复保险丝 | 图 aaa7dbf40110 / 第 1 页 / 第1页 Type-A USB 区 F1 |
| U3 | WS2812 | GPIO21/SK_DIN 控制的可编程 RGB LED | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 B3-B4：U3 WS2812 |
| S1 | SMT_SW_1TS026A | GPIO0 低有效 BOOT/用户按键 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 C3：BTN-USER S1/R4/D1 |
| U2 | SGM2578 / WS4622C-4/TR | DISP_BL 控制的 LCD 背光负载开关 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 A3-A4：LCD 区 U2 |
| J3 | HDGC/0.5K-HX-8PWB/NC | LCD 8针背光、SPI、复位与控制接口 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 A3-A4：J3 pins1-8 |
| J1 | HDGC/0.5K-HX_12P/NC | GPIO16-GPIO18、VIN_5V 与 LCD 信号的 12针接口 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 A4：J1 pins1-12 |
| M1 | STAMP-S3M | Stamp-S3 模组 28针/焊盘外部资源接口 | 图 aaa7dbf40110 / 第 1 页 / 第1页网格 C3-C4：M1 STAMP-S3M pins1-28 |
| D3,D4,D14 | PESDNC2FD3V3B / PESDNC2FD5VB | USB D+/D- 与 VBUS 瞬态保护 | 图 aaa7dbf40110 / 第 1 页 / 第1页 USB 区 D3/D4/D14 |

## 系统结构

### Stamp-S3 PIN2.54 架构

U1 ESP32-S3FN8 连接 40MHz 晶体、PROANT440、原生 USB、WS2812、GPIO0 按键和 SPI LCD；M2 由 VIN_5V 生成 VDD_3V3，M1/J1/J3 引出接口。

- 参数与网络：`soc=ESP32-S3FN8`；`power=M2 MIUN3CAD01-SC`；`rf=ANT1 PROANT440`；`usb=J2 native USB`；`rgb=U3 WS2812`；`headers=M1,J1,J3`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页完整单页

## 电源

### VIN_5V 到 VDD_3V3

M2 MIUN3CAD01-SC VIN pin3 接 VIN_5V，EN pin1 由 ESP_EN/R7/C23/D6/R16 网络控制，VOUT pin6 输出 VDD_3V3，反馈 R6 100KΩ/R17 22.1KΩ。

- 参数与网络：`converter=M2 MIUN3CAD01-SC`；`input=VIN_5V`；`enable=EN from ESP_EN`；`output=VDD_3V3`；`feedback=R6 100KΩ; R17 22.1KΩ`；`caps=C21/C22 10uF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 D1-D2 M2/R6/R17/C21/C22

### USB 5V 输入

J2 VCC 经 F1 6V/1A/PPTC 形成 VIN_5V；CC1/CC2 由 R1/R2 5.1KΩ 下拉，D14 PESDNC2FD5VB 保护 VBUS。

- 参数与网络：`connector=J2 USB-TYPEC`；`fuse=F1 6V/1A/PPTC`；`rail=VIN_5V`；`cc=R1/R2 5.1KΩ`；`vbus_esd=D14 PESDNC2FD5VB`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 D3-D4 J2/F1/R1/R2/D14

### LCD 背光开关

U2 SGM2578/WS4622C-4/TR VIN 接 VDD_3V3，EN 接 DISP_BL/GPIO38，VOUT 输出 J3 pin1 背光电源。

- 参数与网络：`switch=U2 SGM2578 / WS4622C-4/TR`；`input=VDD_3V3`；`enable=GPIO38 / DISP_BL`；`output=J3 pin1`；`capacitor=C3 100nF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 A3-A4 U2/C3/J3

## 接口

### LCD SPI 接口

J3 pins1-8 为背光输出、GND、DISP_RST、DISP_RS、DISP_MOSI、DISP_SCK、VDD_3V3、DISP_CS；对应 GPIO33-GPIO38。

- 参数与网络：`pin1=backlight VOUT`；`pin2=GND`；`pin3=DISP_RST GPIO33`；`pin4=DISP_RS GPIO34`；`pin5=DISP_MOSI GPIO35`；`pin6=DISP_SCK GPIO36`；`pin7=VDD_3V3`；`pin8=DISP_CS GPIO37`；`backlight_enable=DISP_BL GPIO38`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 A3-A4 U2/J3 与 U1 GPIO33-GPIO38

### M1 Stamp-S3M 引脚

M1 pins1-17 引出 GPIO1-GPIO15、VIN_5V/GND，pins18-28 引出 GND、GPIO39、GPIO0、GPIO40、EN、GPIO41、GPIO42、RX、TX、GPIO46、VDD_3V3。

- 参数与网络：`left=GPIO1-10,GND,VIN_5V,GPIO11-15`；`right=GND,GPIO39,GPIO0,GPIO40,EN,GPIO41,GPIO42,RX,TX,GPIO46,VDD_3V3`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 C3-C4 M1 pins1-28

### J1 12针接口

J1 pins1-5 为 VIN_5V/GPIO18/GPIO17/GPIO16/NC，pins6-12 为 DISP_RST/DISP_RS/DISP_MOSI/DISP_SCK/NC/DISP_CS/GND。

- 参数与网络：`pins1_5=VIN_5V,GPIO18,GPIO17,GPIO16,NC`；`pins6_12=DISP_RST,DISP_RS,DISP_MOSI,DISP_SCK,NC,DISP_CS,GND`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 A4 J1 pins1-12

## 总线

### ESP32-S3 原生 USB

J2 DP1/DP2 形成 USB_D_P 并接 U1 GPIO20 pin26，DN1/DN2 形成 USB_D_N 并接 GPIO19 pin25，D3/D4 提供 ESD 保护。

- 参数与网络：`dp=J2 -> USB_D_P -> GPIO20`；`dm=J2 -> USB_D_N -> GPIO19`；`esd=D3/D4 PESDNC2FD3V3B`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 U1 GPIO19/20 与 J2/D3/D4

## GPIO 与控制信号

### RGB 与 GPIO0 按键

U1 GPIO21 形成 SK_DIN 驱动 U3 WS2812；S1 按下将 GPIO0 拉低，R4 10KΩ 上拉且 D1 PESDNC2FD3V3B 对地保护。

- 参数与网络：`rgb=GPIO21 -> SK_DIN -> U3`；`button=S1 GPIO0 low`；`pullup=R4 10KΩ`；`esd=D1 PESDNC2FD3V3B`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 B3-C3 U3/S1/R4/D1

## 时钟

### 40MHz 主时钟

X1 40MHz 连接 U1 XTAL_P/XTAL_N，XTAL_P 串 L3 10nH，C9 10pF 与 C14 12pF 对地。

- 参数与网络：`crystal=X1 40MHz`；`pins=U1 XTAL_P pin54; XTAL_N pin53`；`series=L3 10nH`；`loads=C9 10pF; C14 12pF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 B1 X1/L3/C9/C14

## 复位

### ESP_EN 网络

U1 CHIP_PU pin4 形成 ESP_EN；R7 10KΩ 上拉、C23 1uF 对地，D6 1N4148WT 将 ESP_EN 耦合到 M2 EN。

- 参数与网络：`soc_pin=U1 CHIP_PU pin4`；`pullup=R7 10KΩ`；`capacitor=C23 1uF`；`diode=D6 1N4148WT`；`converter_enable=M2 EN`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 U1 ESP_EN 与 D1 DCDC 区

## 保护电路

### USB 保护

D3/D4 PESDNC2FD3V3B 对 USB D+/D- 提供保护，D14 PESDNC2FD5VB 保护 VIN_5V，F1 提供 6V/1A 过流保护。

- 参数与网络：`data=D3/D4 PESDNC2FD3V3B`；`power=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 USB 区 D3/D4/D14/F1

## 内存与 Flash

### ESP32-S3FN8 存储可见性

U1 标为 ESP32-S3FN8，VDD_SPI pin29 接 FLASH_VCC，SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID pins30-35 未连接，未画外部 Flash/PSRAM。

- 参数与网络：`soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`psram_shown=false`；`unused=pins30-35`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 U1 pin29/pins30-35

## 射频

### PROANT440 天线

U1 LNA_IN 经 L1 2.2nH 连接 ANT1 PROANT440，C1 2.2pF/C2 2.0pF 对地。

- 参数与网络：`antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`series=L1 2.2nH`；`shunt=C1 2.2pF; C2 2.0pF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 A1 ANT1/L1/C1/C2

## 调试与烧录

### UART TX/RX 引出

U1 U0TXD pin49 经 R5 510Ω/1% 形成 TX 并引到 M1 pin26，U0RXD pin50 形成 RX 并引到 M1 pin24。

- 参数与网络：`tx=U0TXD -> R5 510Ω -> TX -> M1 pin26`；`rx=U0RXD -> RX -> M1 pin24`
- 证据：图 aaa7dbf40110 / 第 1 页 / 第1页 U1 pins49/50 与 M1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3 PIN2.54 架构 | `soc=ESP32-S3FN8`；`power=M2 MIUN3CAD01-SC`；`rf=ANT1 PROANT440`；`usb=J2 native USB`；`rgb=U3 WS2812`；`headers=M1,J1,J3` |
| 电源 | VIN_5V 到 VDD_3V3 | `converter=M2 MIUN3CAD01-SC`；`input=VIN_5V`；`enable=EN from ESP_EN`；`output=VDD_3V3`；`feedback=R6 100KΩ; R17 22.1KΩ`；`caps=C21/C22 10uF` |
| 电源 | USB 5V 输入 | `connector=J2 USB-TYPEC`；`fuse=F1 6V/1A/PPTC`；`rail=VIN_5V`；`cc=R1/R2 5.1KΩ`；`vbus_esd=D14 PESDNC2FD5VB` |
| 总线 | ESP32-S3 原生 USB | `dp=J2 -> USB_D_P -> GPIO20`；`dm=J2 -> USB_D_N -> GPIO19`；`esd=D3/D4 PESDNC2FD3V3B` |
| 时钟 | 40MHz 主时钟 | `crystal=X1 40MHz`；`pins=U1 XTAL_P pin54; XTAL_N pin53`；`series=L3 10nH`；`loads=C9 10pF; C14 12pF` |
| 射频 | PROANT440 天线 | `antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`series=L1 2.2nH`；`shunt=C1 2.2pF; C2 2.0pF` |
| GPIO 与控制信号 | RGB 与 GPIO0 按键 | `rgb=GPIO21 -> SK_DIN -> U3`；`button=S1 GPIO0 low`；`pullup=R4 10KΩ`；`esd=D1 PESDNC2FD3V3B` |
| 接口 | LCD SPI 接口 | `pin1=backlight VOUT`；`pin2=GND`；`pin3=DISP_RST GPIO33`；`pin4=DISP_RS GPIO34`；`pin5=DISP_MOSI GPIO35`；`pin6=DISP_SCK GPIO36`；`pin7=VDD_3V3`；`pin8=DISP_CS GPIO37`；`backlight_enable=DISP_BL GPIO38` |
| 电源 | LCD 背光开关 | `switch=U2 SGM2578 / WS4622C-4/TR`；`input=VDD_3V3`；`enable=GPIO38 / DISP_BL`；`output=J3 pin1`；`capacitor=C3 100nF` |
| 接口 | M1 Stamp-S3M 引脚 | `left=GPIO1-10,GND,VIN_5V,GPIO11-15`；`right=GND,GPIO39,GPIO0,GPIO40,EN,GPIO41,GPIO42,RX,TX,GPIO46,VDD_3V3` |
| 接口 | J1 12针接口 | `pins1_5=VIN_5V,GPIO18,GPIO17,GPIO16,NC`；`pins6_12=DISP_RST,DISP_RS,DISP_MOSI,DISP_SCK,NC,DISP_CS,GND` |
| 复位 | ESP_EN 网络 | `soc_pin=U1 CHIP_PU pin4`；`pullup=R7 10KΩ`；`capacitor=C23 1uF`；`diode=D6 1N4148WT`；`converter_enable=M2 EN` |
| 调试与烧录 | UART TX/RX 引出 | `tx=U0TXD -> R5 510Ω -> TX -> M1 pin26`；`rx=U0RXD -> RX -> M1 pin24` |
| 内存与 Flash | ESP32-S3FN8 存储可见性 | `soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`psram_shown=false`；`unused=pins30-35` |
| 内存与 Flash | 8MB Flash 容量 | `documented_flash=8MB`；`soc=ESP32-S3FN8`；`capacity_text_shown=false` |
| 保护电路 | USB 保护 | `data=D3/D4 PESDNC2FD3V3B`；`power=D14 PESDNC2FD5VB`；`fuse=F1 6V/1A/PPTC` |

## 待确认事项

- `memory.documented-capacity`：正文写 8MB Flash，原理图只打印 ESP32-S3FN8 料号和 FLASH_VCC，未单独打印容量字段。（证据：图 aaa7dbf40110 / 第 1 页 / 第1页 U1 ESP32-S3FN8/FLASH_VCC）
- `review.flash-capacity`：S007-PIN254 当前 ESP32-S3FN8 集成 Flash 容量是否固定为 8MB？；原因：容量来自正文，原理图未单独打印容量字段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `aaa7dbf40110a4ec90c6f2dae371394bafe3c0894ae255aca506aba1b636899f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/510/Sch_M5StampS3_v0.2_sch_01.png` |

---

源文档：`zh_CN/core/M5StampS3 PIN2.54.md`

源文档 SHA-256：`46b769e49faa04bbbac847fedf572ec09e13e489daef39a58bf8e4d1742aa754`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
