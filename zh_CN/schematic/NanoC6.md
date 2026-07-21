# NanoC6 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | NanoC6 |
| SKU | C125 |
| 产品 ID | `nanoc6-6ea666d1c510` |
| 源文档 | `zh_CN/core/M5NanoC6.md` |

## 概述

NanoC6 以 U1 ESP32-C6FH4 为主控，配置 40MHz 晶体和 ANT16008LCS2442MA2 陶瓷天线匹配网络。USB Type-C 提供原生 USB D+/D- 与 VBUS，U3 BL8075CB5TR33 生成 VDD_3V3，并通过 Grove 引出 GPIO1/GPIO2 与 5V。GPIO19 控制 AW35122FDR 为 WS2812 供电，GPIO20 驱动 RGB 数据，GPIO3 驱动红外，GPIO7 驱动蓝灯，GPIO9 为低有效按键。

## 检索关键词

`NanoC6`、`C125`、`ESP32-C6FH4`、`BL8075CB5TR33`、`AW35122FDR`、`WS2812`、`ANT16008LCS2442MA2`、`40MHz`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VBUS`、`VDD_3V3`、`GPIO1`、`GPIO2`、`GPIO3 IR`、`GPIO7 Blue LED`、`GPIO9 Button`、`GPIO19 RGBPWR`、`GPIO20 RGB`、`RGBPWR`、`F3V3`、`Grove`、`HY-2.0`、`PESDNC2FD3V3B`、`F1 6V/1A/PPTC`、`CC1`、`CC2`、`UTX`、`URX`、`ESP_LNA`、`EN`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-C6FH4 | 主控 SoC，连接 USB、射频、RGB、IR、按键、LED 和 Grove GPIO | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 B1-C3：U1 ESP32-C6FH4 |
| USB1 | TYPEC-304S-ACP16 | 原生 USB 数据和 VBUS 电源输入 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 A1-A2：USB1/F1/R3/R4/D2/D3 |
| F1 | 6V/1A/PPTC | USB VBUS 自恢复过流保护 | 图 c51f3fce752d / 第 1 页 / 第 1 页 USB1 VBUS 到 F1/VBUS |
| D2,D3 | PESDNC2FD3V3B | USB D+/D- 静电保护 | 图 c51f3fce752d / 第 1 页 / 第 1 页 Type-C 区 USB_D_P/N 与 D2/D3 |
| U3 | BL8075CB5TR33 | VBUS 到 VDD_3V3 的 3.3V LDO | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 A3-A4：LDO 3.3V 区 U3/C14-C19 |
| X1 | 40MHz | ESP32-C6 主时钟晶体 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 C2：X1 40MHz、L3、C3/C4 |
| ANT1 | ANT16008LCS2442MA2 | ESP32-C6 陶瓷射频天线 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 B2：ANT1/L1/L2/L5/C21/C22 |
| J1 | HY-2.0 | GPIO1、GPIO2、VBUS 和 GND 的 Grove 接口 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 B4-C4：J1/D4-D6 |
| U6 | AW35122FDR | GPIO19/RGBPWR 控制的 RGB 3.3V 负载开关 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 D1-D2：RGB LED 区 U6 |
| U2 | WS2812 | GPIO20/RGB 数据驱动的可编程 RGB LED | 图 c51f3fce752d / 第 1 页 / 第 1 页 RGB LED 区 U2 WS2812 |
| S1 | SMT_SW_PTS_820 | GPIO9 低有效下载/用户按键 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 C4：Button 区 S1/R2/D1 |
| IR1,R1 | IR LED / 22R/1% | GPIO3 红外发射支路 | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 D4：GPIO3-IR1-R1-GND |
| LED1,R9 | Blue LED / 22R/1% | GPIO7 蓝色状态 LED | 图 c51f3fce752d / 第 1 页 / 第 1 页网格 D4：GPIO7-LED1-R9-GND |

## 系统结构

### NanoC6 系统架构

U1 ESP32-C6FH4 连接原生 USB-C、40MHz 晶体、陶瓷天线、Grove、受控 WS2812、红外、蓝灯和 GPIO9 按键；U3 从 VBUS 生成 VDD_3V3。

- 参数与网络：`soc=ESP32-C6FH4`；`usb=USB1 native USB`；`power=U3 BL8075CB5TR33`；`rf=ANT1 ANT16008LCS2442MA2`；`rgb=U6 + U2 WS2812`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页完整单页全部功能分区

## 电源

### USB VBUS 输入

USB1 VBUS 经 F1 6V/1A/PPTC 形成 VBUS，供给 U3 和 Grove J1 pin3；CC1/CC2 各经 R3/R4 5.1KΩ 下拉。

- 参数与网络：`connector=USB1 TYPEC-304S-ACP16`；`fuse=F1 6V/1A/PPTC`；`rail=VBUS`；`cc=R3/R4 5.1KΩ to GND`；`consumers=U3, J1 pin3`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 A1-A2 USB1/F1/R3/R4

### VDD_3V3 LDO

U3 BL8075CB5TR33 VIN/EN 接 VBUS，VOUT 输出 VDD_3V3；输入 C19 100nF、C14/C15 10uF，输出 C17/C18 10uF 与 C16 100nF。

- 参数与网络：`ldo=U3 BL8075CB5TR33`；`input=VBUS`；`enable=VBUS`；`output=VDD_3V3`；`input_caps=C19 100nF; C14/C15 10uF`；`output_caps=C17/C18 10uF; C16 100nF`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 A3-A4 U3/C14-C19

### RGB 受控电源

U6 AW35122FDR VIN 接 VDD_3V3，EN 接 GPIO19/RGBPWR，VOUT 形成 F3V3 为 U2 WS2812 供电。

- 参数与网络：`switch=U6 AW35122FDR`；`input=VDD_3V3`；`enable=GPIO19 / RGBPWR`；`output=F3V3`；`consumer=U2 WS2812`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 D1-D2 RGB LED 区 U6/U2

## 接口

### J1 Grove 接口

J1 pin1=GPIO1/IO1、pin2=GPIO2/IO2、pin3=VBUS/+5V、pin4=GND；D4/D5/D6 PESDNC2FD3V3B 分别保护 GPIO1、GPIO2 和 VBUS。

- 参数与网络：`pin1=GPIO1`；`pin2=GPIO2`；`pin3=VBUS`；`pin4=GND`；`protection=D4/D5/D6 PESDNC2FD3V3B`；`gpio_level=VDD_3V3 domain`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 B4-C4 J1/D4-D6

## 总线

### ESP32-C6 原生 USB

USB1 DP1/DP2 形成 USB_D_P 并接 U1 GPIO13/USB_D+ pin17，DN1/DN2 形成 USB_D_N 并接 GPIO12/USB_D- pin16。

- 参数与网络：`controller=U1 ESP32-C6FH4`；`dp=USB1 -> USB_D_P -> GPIO13 pin17`；`dm=USB1 -> USB_D_N -> GPIO12 pin16`；`direction=bidirectional`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 USB1 与 U1 GPIO12/GPIO13

## GPIO 与控制信号

### RGB、IR 与蓝灯 GPIO

GPIO20/RGB 接 U2 WS2812 DI；GPIO3 经 IR1/R1 22Ω 驱动红外；GPIO7 经 LED1/R9 22Ω 驱动蓝色 LED。

- 参数与网络：`rgb=GPIO20 -> U2 DI`；`ir=GPIO3 -> IR1 -> R1 22Ω -> GND`；`blue=GPIO7 -> LED1 -> R9 22Ω -> GND`；`direction=output`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 D1-D4 RGB LED 与 IR&LED 区

### GPIO9 下载按键

S1 按下将 GPIO9 拉低，R2 10KΩ 上拉到 VDD_3V3，D1 PESDNC2FD3V3B 提供对地保护。

- 参数与网络：`gpio=GPIO9`；`switch=S1 SMT_SW_PTS_820`；`active=low`；`pullup=R2 10KΩ`；`protection=D1 PESDNC2FD3V3B`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 C4 Button 区 S1/R2/D1

## 时钟

### 40MHz 主时钟

X1 40MHz 连接 U1 XTAL_P/XTAL_N，XTAL_P 串 L3 24nH，C3/C4 各 12pF 对地。

- 参数与网络：`crystal=X1 40MHz`；`pins=U1 XTAL_P pin31; XTAL_N pin30`；`series=L3 24nH`；`loads=C3/C4 12pF`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 C2 X1/L3/C3/C4

## 复位

### ESP32-C6 EN 网络

U1 CHIP_PU pin4 形成 EN，由 R7 10KΩ 上拉到 VDD_3V3、C2 1uF 对地，并引到 JP1 测试点。

- 参数与网络：`soc_pin=U1 CHIP_PU pin4`；`net=EN`；`pullup=R7 10KΩ`；`capacitor=C2 1uF`；`testpoint=JP1`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 C3 EN/R7/C2/JP1

## 保护电路

### USB 数据与过流保护

D2/D3 PESDNC2FD3V3B 分别保护 USB_D_P/USB_D_N，F1 6V/1A/PPTC 提供 VBUS 过流保护。

- 参数与网络：`dp_esd=D2 PESDNC2FD3V3B`；`dm_esd=D3 PESDNC2FD3V3B`；`overcurrent=F1 6V/1A/PPTC`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 Type-C 区 D2/D3/F1

## 关键网络

### 主要电源网络

VBUS 来自 USB/F1并供给 U3 与 Grove；VDD_3V3 由 U3 生成并供给 U1 和逻辑；F3V3 由 U6 受 GPIO19 控制，仅供 WS2812。

- 参数与网络：`VBUS=USB1/F1 -> U3,J1`；`VDD_3V3=U3 -> U1,logic`；`F3V3=U6 -> U2 WS2812`；`control=GPIO19 RGBPWR`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 VBUS/VDD_3V3/F3V3 同名网络

## 射频

### 陶瓷天线匹配

U1 ANT pin1 经 ESP_LNA、L5 2.2nH、L1 4.7nH 接 ANT1 feed point，C22 2.0pF、C21 1.5pF 和 L2 2.4pF 对地构成匹配网络。

- 参数与网络：`soc_pin=U1 ANT pin1`；`antenna=ANT1 ANT16008LCS2442MA2`；`series=L5 2.2nH; L1 4.7nH`；`shunt=C22 2.0pF; C21 1.5pF; L2 2.4pF`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 B2 ANT1/L1/L2/L5/C21/C22

## 调试与烧录

### UART 测试点

U1 GPIO16/U0TXD pin21 形成 UTX 并引到 JP2，GPIO17/U0RXD pin22 形成 URX 并引到 JP3。

- 参数与网络：`tx=GPIO16/U0TXD -> UTX -> JP2`；`rx=GPIO17/U0RXD -> URX -> JP3`
- 证据：图 c51f3fce752d / 第 1 页 / 第 1 页 U1 pins21/22 与 JP2/JP3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | NanoC6 系统架构 | `soc=ESP32-C6FH4`；`usb=USB1 native USB`；`power=U3 BL8075CB5TR33`；`rf=ANT1 ANT16008LCS2442MA2`；`rgb=U6 + U2 WS2812` |
| 电源 | USB VBUS 输入 | `connector=USB1 TYPEC-304S-ACP16`；`fuse=F1 6V/1A/PPTC`；`rail=VBUS`；`cc=R3/R4 5.1KΩ to GND`；`consumers=U3, J1 pin3` |
| 电源 | VDD_3V3 LDO | `ldo=U3 BL8075CB5TR33`；`input=VBUS`；`enable=VBUS`；`output=VDD_3V3`；`input_caps=C19 100nF; C14/C15 10uF`；`output_caps=C17/C18 10uF; C16 100nF` |
| 总线 | ESP32-C6 原生 USB | `controller=U1 ESP32-C6FH4`；`dp=USB1 -> USB_D_P -> GPIO13 pin17`；`dm=USB1 -> USB_D_N -> GPIO12 pin16`；`direction=bidirectional` |
| 保护电路 | USB 数据与过流保护 | `dp_esd=D2 PESDNC2FD3V3B`；`dm_esd=D3 PESDNC2FD3V3B`；`overcurrent=F1 6V/1A/PPTC` |
| 射频 | 陶瓷天线匹配 | `soc_pin=U1 ANT pin1`；`antenna=ANT1 ANT16008LCS2442MA2`；`series=L5 2.2nH; L1 4.7nH`；`shunt=C22 2.0pF; C21 1.5pF; L2 2.4pF` |
| 时钟 | 40MHz 主时钟 | `crystal=X1 40MHz`；`pins=U1 XTAL_P pin31; XTAL_N pin30`；`series=L3 24nH`；`loads=C3/C4 12pF` |
| 接口 | J1 Grove 接口 | `pin1=GPIO1`；`pin2=GPIO2`；`pin3=VBUS`；`pin4=GND`；`protection=D4/D5/D6 PESDNC2FD3V3B`；`gpio_level=VDD_3V3 domain` |
| 电源 | RGB 受控电源 | `switch=U6 AW35122FDR`；`input=VDD_3V3`；`enable=GPIO19 / RGBPWR`；`output=F3V3`；`consumer=U2 WS2812` |
| GPIO 与控制信号 | RGB、IR 与蓝灯 GPIO | `rgb=GPIO20 -> U2 DI`；`ir=GPIO3 -> IR1 -> R1 22Ω -> GND`；`blue=GPIO7 -> LED1 -> R9 22Ω -> GND`；`direction=output` |
| GPIO 与控制信号 | GPIO9 下载按键 | `gpio=GPIO9`；`switch=S1 SMT_SW_PTS_820`；`active=low`；`pullup=R2 10KΩ`；`protection=D1 PESDNC2FD3V3B` |
| 复位 | ESP32-C6 EN 网络 | `soc_pin=U1 CHIP_PU pin4`；`net=EN`；`pullup=R7 10KΩ`；`capacitor=C2 1uF`；`testpoint=JP1` |
| 调试与烧录 | UART 测试点 | `tx=GPIO16/U0TXD -> UTX -> JP2`；`rx=GPIO17/U0RXD -> URX -> JP3` |
| 内存与 Flash | ESP32-C6FH4 Flash 容量 | `soc=ESP32-C6FH4`；`documented_flash=4MB`；`external_flash_shown=false`；`capacity_text_shown=false` |
| 关键网络 | 主要电源网络 | `VBUS=USB1/F1 -> U3,J1`；`VDD_3V3=U3 -> U1,logic`；`F3V3=U6 -> U2 WS2812`；`control=GPIO19 RGBPWR` |

## 待确认事项

- `memory.documented-flash`：产品正文写 4MB Flash，原理图器件字段为 ESP32-C6FH4，页面未单独打印容量数值或外部存储器。（证据：图 c51f3fce752d / 第 1 页 / 第 1 页 U1 ESP32-C6FH4 与完整存储范围）
- `review.flash-capacity`：C125 当前 ESP32-C6FH4 的集成 Flash 容量是否固定为 4MB？；原因：容量来自正文与料号解释，原理图未单独打印容量字段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c51f3fce752dc902fc500316dd86fbbd455773c2ca0e6da7fe5cd0b97bccf38d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/Sch_M5NanoC6_v0.0.1_sch_01.png` |

---

源文档：`zh_CN/core/M5NanoC6.md`

源文档 SHA-256：`b81c36d96acb7c23e43e2b7d2fce5485c10a9727ca2a1cf0158d1f1a5de59d76`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
