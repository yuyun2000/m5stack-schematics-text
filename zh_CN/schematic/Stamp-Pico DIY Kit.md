# Stamp-Pico DIY Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-Pico DIY Kit |
| SKU | K051-B |
| 产品 ID | `stamp-pico-diy-kit-8e4dd31d2e05` |
| 源文档 | `zh_CN/core/stamp_pico_diy_kit.md` |

## 概述

Stamp-Pico DIY Kit 的本地原理图资源仅覆盖 Stamp-Pico 核心板本体，以 U2 ESP32-PICO-D4 为主控，配置金属 3D 天线、SY8079AAAC 5 V 转 3.3 V 电源、SK6812 RGB LED 和 GPIO39 用户按键。J1 提供 GPIO32/GPIO33 Grove 接口，J2 为 DNP 的 16 针核心板引出，包含 12 路 GPIO、EN、5 V、3.3 V 和 GND。Kit 所含 USB-TTL Downloader 未出现在该原理图页中，因此其桥接芯片与 USB/自动下载电路未确认。

## 检索关键词

`Stamp-Pico DIY Kit`、`K051-B`、`Stamp-Pico`、`ESP32-PICO-D4`、`PICO_D4`、`SY8079AAAC`、`SK6812_3535`、`GPIO27`、`GPIO39`、`GPIO0`、`GPIO1`、`GPIO3`、`GPIO18`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO26`、`GPIO32`、`GPIO33`、`GPIO36`、`SYS_P050`、`MCU_P033`、`HY2.0-4P`、`GROVE`、`3D天线`、`ESP32 Downloader`、`UART0`、`EN`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | PICO_D4 | ESP32-PICO-D4 系统主控，连接天线、UART、GPIO、RGB LED、按键和引出接口 | 图 81479376963d / 第 1 页 / 中央，U2 PICO_D4 全部 IO 与电源引脚 |
| ANT1 | 五金3D天线 | ESP32-PICO-D4 射频天线 | 图 81479376963d / 第 1 页 / 上中，ANT1 五金3D天线、L2/C5/C6 匹配网络 |
| U1 | SY8079AAAC | SYS_P050 输入的降压转换器，生成 MCU_P033 | 图 81479376963d / 第 1 页 / 左下，U1 SY8079AAAC、L1 2.2uH、R1/R2、SYS_P050/MCU_P033 |
| L1 | 2.20H | SY8079AAAC 降压输出电感 | 图 81479376963d / 第 1 页 / U1 SW3 到 MCU_P033，L1 标注 2.20H |
| LED1 | SK6812_3535 | GPIO27 控制的可编程 RGB LED | 图 81479376963d / 第 1 页 / 下中，LED1 SK6812_3535、GPIO27、MCU_P033 |
| S1 | SW | GPIO39 低有效用户按键 | 图 81479376963d / 第 1 页 / 右下，S1 SW、GPIO39、R3 5.1K |
| J1 | GROVE | GPIO33/GPIO32、5 V 与 GND 的四针 Grove 接口 | 图 81479376963d / 第 1 页 / 左上，J1 GROVE pins 1-4 |
| J2 | DNP | 核心板 16 针可选排针/排母引出接口 | 图 81479376963d / 第 1 页 / 左中，J2 DNP，EN/GPIO/5V/3V3/GND |
| R4/C13 | 5.1K / 105/6.3V | ESP32 EN 上拉与上电复位 RC 网络 | 图 81479376963d / 第 1 页 / 右下，MCU_P033-R4-EN-C13-GND |
| R5 | 5.1K/1% | GPIO0 上拉电阻 | 图 81479376963d / 第 1 页 / 右下，R5 5.1K/1% 从 MCU_P033 到 GPIO0 |

## 系统结构

### 核心板架构

本地原理图中的 Stamp-Pico 核心板由 U2 PICO_D4、SY8079AAAC 降压、五金 3D 天线、SK6812_3535、GPIO39 按键和两组引出接口组成。

- 参数与网络：`controller=U2 PICO_D4`；`regulator=U1 SY8079AAAC`；`antenna=ANT1 五金3D天线`；`rgb=LED1 SK6812_3535`；`button=S1 GPIO39`；`interfaces=J1 GROVE; J2 DNP`
- 证据：图 81479376963d / 第 1 页 / 整页：U2/U1/ANT1/LED1/S1/J1/J2

## 核心器件

### ESP32-PICO-D4 主控

U2 原理图值为 PICO_D4，LNA_IN 接天线，IO1/IO3 标为 UART0 TXD/RXD，其余使用的 GPIO 直接引出或连接板载功能。

- 参数与网络：`reference=U2`；`part_number=PICO_D4`；`rf_pin=LNA_IN`；`uart_tx=IO1/U0TXD`；`uart_rx=IO3/U0RXD`
- 证据：图 81479376963d / 第 1 页 / U2 PICO_D4 引脚框

## 电源

### 5 V 输入轨

SYS_P050 从 J1 pin 2 和 J2 5V 引脚进入板内，供 U1 SY8079AAAC IN/EN。

- 参数与网络：`net=SYS_P050`；`sources=J1 pin 2; J2 5V`；`consumer=U1 SY8079AAAC IN/EN`
- 证据：图 81479376963d / 第 1 页 / J1/J2 SYS_P050 与 U1 IN/EN

### 3.3 V 降压电源

U1 SY8079AAAC 由 SYS_P050 供电，经 L1 标注 2.20H 输出 MCU_P033；反馈分压为 R1 22 kΩ 与 R2 5.1 kΩ。

- 参数与网络：`reference=U1`；`part_number=SY8079AAAC`；`input=SYS_P050`；`enable=SYS_P050`；`inductor=L1 2.20H`；`output=MCU_P033`；`feedback_upper=R1 22K/1%`；`feedback_lower=R2 5.1K/1%`
- 证据：图 81479376963d / 第 1 页 / 左下，U1/L1/R1/R2/C1/C2/C3

## 接口

### Grove 接口

J1 pins 4/3/2/1 依次为 GPIO33、GPIO32、SYS_P050 和 GND。

- 参数与网络：`reference=J1`；`pin4=GPIO33`；`pin3=GPIO32`；`pin2=SYS_P050`；`pin1=GND`
- 证据：图 81479376963d / 第 1 页 / 左上，J1 GROVE pins 1-4

### 16 针核心板引出

J2 标为 DNP，引出 EN、GPIO0、GPIO1、GPIO3、GPIO18、GPIO19、GPIO21、GPIO22、GPIO26、GPIO25、GPIO36、GPIO32、GPIO33、SYS_P050、MCU_P033 和 GND。

- 参数与网络：`reference=J2`；`population=DNP`；`signals=EN; GPIO0; GPIO1; GPIO3; GPIO18; GPIO19; GPIO21; GPIO22; GPIO26; GPIO25; GPIO36; GPIO32; GPIO33`；`power=SYS_P050; MCU_P033; GND`
- 证据：图 81479376963d / 第 1 页 / 左中，J2 DNP 全部 16 项标签

## 总线

### UART0

U2 IO1/U0TXD 对应 GPIO1，IO3/U0RXD 对应 GPIO3，两路均由 J2 引出。

- 参数与网络：`tx=GPIO1/IO1/U0TXD`；`rx=GPIO3/IO3/U0RXD`；`connector=J2`
- 证据：图 81479376963d / 第 1 页 / U2 IO1/U0TXD、IO3/U0RXD 与 J2 GPIO1/GPIO3

## GPIO 与控制信号

### 外接 GPIO 映射

J2 提供 12 路 GPIO：0、1、3、18、19、21、22、26、25、36、32、33；GPIO32/33 同时连接 J1 Grove。

- 参数与网络：`count=12`；`gpios=GPIO0; GPIO1; GPIO3; GPIO18; GPIO19; GPIO21; GPIO22; GPIO25; GPIO26; GPIO32; GPIO33; GPIO36`；`shared_grove=GPIO32; GPIO33`
- 证据：图 81479376963d / 第 1 页 / J2 GPIO 列表与 J1 GPIO32/GPIO33

### RGB LED GPIO

LED1 SK6812_3535 的 DI 连接 U2 GPIO27，VDD 连接 MCU_P033，DO 未继续连接。

- 参数与网络：`reference=LED1`；`part_number=SK6812_3535`；`data_in=GPIO27`；`supply=MCU_P033`；`data_out=NC`
- 证据：图 81479376963d / 第 1 页 / 下中，LED1 DI/VDD/DO/GND

### 用户按键 GPIO

S1 按下时将 GPIO39 拉低，R3 5.1 kΩ 将 GPIO39 上拉到 MCU_P033。

- 参数与网络：`reference=S1`；`gpio=GPIO39`；`active_level=low`；`pullup=R3 5.1K/1% to MCU_P033`
- 证据：图 81479376963d / 第 1 页 / 右下，R3/GPIO39/S1/GND

### GPIO0 上拉

GPIO0 由 R5 5.1 kΩ 上拉到 MCU_P033，并通过 J2 引出。

- 参数与网络：`gpio=GPIO0`；`pullup=R5 5.1K/1%`；`connector=J2`
- 证据：图 81479376963d / 第 1 页 / 右下 R5/GPIO0；左中 J2 G0

## 复位

### 主控 EN 复位网络

EN 由 R4 5.1 kΩ 上拉到 MCU_P033，并由 C13（105/6.3V）对地形成上电复位 RC。

- 参数与网络：`net=EN`；`pullup=R4 5.1K/1%`；`capacitor=C13 105/6.3V`；`supply=MCU_P033`
- 证据：图 81479376963d / 第 1 页 / 右下，R4/EN/C13

## 射频

### 3D 天线与匹配

U2 LNA_IN 通过 L2 0 Ω 串联到 ANT1 五金3D天线，C5/C6 两个并联匹配位均标注 TBD。

- 参数与网络：`controller_pin=U2 LNA_IN`；`series=L2 0R`；`shunt_positions=C5 TBD; C6 TBD`；`antenna=ANT1 五金3D天线`
- 证据：图 81479376963d / 第 1 页 / 上中，U2 LNA_IN/L2/C5/C6/ANT1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 核心板架构 | `controller=U2 PICO_D4`；`regulator=U1 SY8079AAAC`；`antenna=ANT1 五金3D天线`；`rgb=LED1 SK6812_3535`；`button=S1 GPIO39`；`interfaces=J1 GROVE; J2 DNP` |
| 核心器件 | ESP32-PICO-D4 主控 | `reference=U2`；`part_number=PICO_D4`；`rf_pin=LNA_IN`；`uart_tx=IO1/U0TXD`；`uart_rx=IO3/U0RXD` |
| 接口 | Grove 接口 | `reference=J1`；`pin4=GPIO33`；`pin3=GPIO32`；`pin2=SYS_P050`；`pin1=GND` |
| 接口 | 16 针核心板引出 | `reference=J2`；`population=DNP`；`signals=EN; GPIO0; GPIO1; GPIO3; GPIO18; GPIO19; GPIO21; GPIO22; GPIO26; GPIO25; GPIO36; GPIO32; GPIO33`；`power=SYS_P050; MCU_P033; GND` |
| GPIO 与控制信号 | 外接 GPIO 映射 | `count=12`；`gpios=GPIO0; GPIO1; GPIO3; GPIO18; GPIO19; GPIO21; GPIO22; GPIO25; GPIO26; GPIO32; GPIO33; GPIO36`；`shared_grove=GPIO32; GPIO33` |
| 总线 | UART0 | `tx=GPIO1/IO1/U0TXD`；`rx=GPIO3/IO3/U0RXD`；`connector=J2` |
| GPIO 与控制信号 | RGB LED GPIO | `reference=LED1`；`part_number=SK6812_3535`；`data_in=GPIO27`；`supply=MCU_P033`；`data_out=NC` |
| GPIO 与控制信号 | 用户按键 GPIO | `reference=S1`；`gpio=GPIO39`；`active_level=low`；`pullup=R3 5.1K/1% to MCU_P033` |
| 复位 | 主控 EN 复位网络 | `net=EN`；`pullup=R4 5.1K/1%`；`capacitor=C13 105/6.3V`；`supply=MCU_P033` |
| GPIO 与控制信号 | GPIO0 上拉 | `gpio=GPIO0`；`pullup=R5 5.1K/1%`；`connector=J2` |
| 电源 | 5 V 输入轨 | `net=SYS_P050`；`sources=J1 pin 2; J2 5V`；`consumer=U1 SY8079AAAC IN/EN` |
| 电源 | 3.3 V 降压电源 | `reference=U1`；`part_number=SY8079AAAC`；`input=SYS_P050`；`enable=SYS_P050`；`inductor=L1 2.20H`；`output=MCU_P033`；`feedback_upper=R1 22K/1%`；`feedback_lower=R2 5.1K/1%` |
| 射频 | 3D 天线与匹配 | `controller_pin=U2 LNA_IN`；`series=L2 0R`；`shunt_positions=C5 TBD; C6 TBD`；`antenna=ANT1 五金3D天线` |
| 存储 | 嵌入式 Flash 容量 | `reference=U2`；`schematic_marking=PICO_D4`；`claimed_flash=4MB` |
| 内存与 Flash | 片内 SRAM 容量 | `reference=U2`；`controller=PICO_D4`；`claimed_sram=520KB` |
| 系统结构 | 处理器与无线规格 | `controller=U2 PICO_D4`；`unverified_cpu=dual Xtensa LX6 up to 240MHz`；`unverified_radio=2.4GHz Wi-Fi and Bluetooth` |
| 调试与烧录 | Kit USB-TTL Downloader | `kit_accessory=ESP32 Downloader`；`unverified_bridge_variants=CP2104; CH9102`；`schematic_scope=Stamp-Pico core only` |
| 接口 | DIY Kit 排针排母与下载器线序 | `confirmed_board_interfaces=J1 GROVE; J2 DNP`；`unverified_kit_parts=2.54-9P headers; 2.54-6P headers; 90-degree HY2.0-4P socket; downloader mating order` |

## 待确认事项

- `storage.flash-capacity`：原理图只标注 U2 为 PICO_D4，未直接以容量字段标注产品正文所述 4 MB Flash。（证据：图 81479376963d / 第 1 页 / U2 仅标 PICO_D4，无容量文本）
- `memory.sram-capacity`：原理图未直接标注产品正文所述 520 KB SRAM。（证据：图 81479376963d / 第 1 页 / U2 型号框未列 SRAM 容量）
- `system.performance-radio`：原理图未直接标注双核 Xtensa LX6、240 MHz 主频、2.4 GHz Wi-Fi 或蓝牙性能。（证据：图 81479376963d / 第 1 页 / U2/ANT1 仅标型号和天线，不列性能）
- `debug.downloader`：本地原理图只覆盖 Stamp-Pico 核心板，未显示 Kit 所含 ESP32 Downloader、USB 接口、USB-UART 芯片或自动下载电路。（证据：图 81479376963d / 第 1 页 / 整页无 USB 连接器、USB-UART 位号或 DTR/RTS 电路）
- `interface.kit-accessories`：原理图确认 J1/J2 的电气信号，但未显示套件中独立排针、排母、90° HY2.0-4P 母座及 Downloader 的实体线序和装配关系。（证据：图 81479376963d / 第 1 页 / 仅 J1/J2 电气符号，无套件附件装配图）
- `review.flash-capacity`：请用 ESP32-PICO-D4 datasheet/BOM 确认 4 MB Flash。；原因：原理图只标 PICO_D4，未单列容量。
- `review.sram-capacity`：请用 ESP32-PICO-D4 datasheet 确认 520 KB SRAM。；原因：片内存储容量未印在原理图中。
- `review.performance-radio`：请用主控 datasheet 复核 CPU 架构/频率和无线规格。；原因：原理图只给出 PICO_D4 与天线。
- `review.downloader`：请提供 Kit 中 ESP32 Downloader 原理图/BOM，确认 USB-UART 型号与自动下载电路。；原因：当前资源只有核心板本体，下载器未出现。
- `review.kit-accessories`：请用套件装配图/BOM 确认排针排母、90° Grove 母座和 Downloader 对接线序。；原因：原理图仅显示板上 J1/J2 电气接口。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `81479376963d1b7ac69231f718bbe2287d47d6a373437cba92c073bfa11365c5` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_pico_diy_kit.md`

源文档 SHA-256：`0b07c083b78cea43efb09a57b254d5eef0d65214a5fea030453542300dc50338`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
