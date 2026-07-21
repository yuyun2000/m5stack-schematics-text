# Stamp-Pico Mate 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-Pico Mate |
| SKU | K051 |
| 产品 ID | `stamp-pico-mate-ac5ec8809d80` |
| 源文档 | `zh_CN/core/stamp_pico_mate.md` |

## 概述

Stamp-Pico Mate 原理图以 U2 ESP32-PICO-D4 为主控，U1 SY8079AAAC 从 SYS_P050 生成 MCU_P033。J2 DNP 主接口引出 12 路 GPIO、EN、5V、3.3V 和 GND，J1 Grove 引出 GPIO32/GPIO33 与 SYS_P050。LED1 SK6812_3535 接 GPIO27，S1 按键通过 5.1K 支路关联 GPIO39、EN 与 GPIO0；板上不含 USB-UART 下载器。

## 检索关键词

`Stamp-Pico Mate`、`K051`、`ESP32-PICO-D4`、`PICO_D4`、`SY8079AAAC`、`SK6812_3535`、`SYS_P050`、`MCU_P033`、`GPIO27 RGB`、`GPIO39 Button`、`GPIO0 BOOT`、`EN`、`J1 GROVE`、`J2 DNP`、`GPIO32`、`GPIO33`、`GPIO25`、`GPIO26`、`GPIO36`、`GPIO18`、`GPIO19`、`GPIO21`、`GPIO22`、`UART0`、`3D antenna`、`ANT1`、`no USB-UART`、`2.54mm`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ESP32-PICO-D4 | 主控 SiP，提供 12 路外部 GPIO、UART0、RF 与启动控制 | 图 81479376963d / 第 1 页 / 中央 U2 PICO_D4 |
| U1 | SY8079AAAC | SYS_P050 至 MCU_P033 的 3.3V 降压转换器 | 图 81479376963d / 第 1 页 / 左下 U1 SY8079AAAC |
| LED1 | SK6812_3535 | GPIO27 控制的可编程 RGB LED | 图 81479376963d / 第 1 页 / 下中 LED1 SK6812_3535 |
| S1 | SW | GPIO39/EN/GPIO0 复合按键网络 | 图 81479376963d / 第 1 页 / 右下 S1、R3-R5、C13 |
| J1 | GROVE | 4 针 Grove 接口，提供 GPIO33/GPIO32、SYS_P050 与 GND | 图 81479376963d / 第 1 页 / 左上 J1 GROVE |
| J2 | DNP | 主模组接口，引出 EN、12 路 GPIO、5V、3.3V 与 GND | 图 81479376963d / 第 1 页 / 左中 J2 DNP |
| ANT1 | 五金3D天线 | ESP32 射频天线，配套 L2/C5/C6 匹配位 | 图 81479376963d / 第 1 页 / 上中 ANT1 五金3D天线 |

## 系统结构

### Stamp-Pico Mate 核心板架构

ESP32-PICO-D4 由 SY8079AAAC 3.3V 电源供电，J2/J1 引出 GPIO 与电源，板载 SK6812 和复合按键，无 USB 下载桥。

- 参数与网络：`mcu=U2 ESP32-PICO-D4`；`dcdc=U1 SY8079AAAC`；`rgb=LED1 SK6812_3535`；`main_interface=J2 DNP`；`grove=J1`；`usb_uart=null`
- 证据：图 81479376963d / 第 1 页 / 完整原理图页

## 核心器件

### U2 ESP32-PICO-D4

U2 图中标 PICO_D4，EN、GPIO0/1/3/18/19/21/22/25/26/27/32/33/36/39 与 UART0 清晰引出。

- 参数与网络：`reference=U2`；`part_number=ESP32-PICO-D4`；`power=MCU_P033`；`enable=EN`；`uart=GPIO1 U0TXD; GPIO3 U0RXD`
- 证据：图 81479376963d / 第 1 页 / 中央 U2

## 电源

### U1 SY8079AAAC

U1 SY8079AAAC 的 IN/EN 接 SYS_P050，经 L1 2.20uH 生成 MCU_P033，反馈为 R1 22K/R2 5.1K。

- 参数与网络：`reference=U1`；`input=SYS_P050`；`output=MCU_P033`；`inductor=L1 2.20uH`；`feedback=R1 22K; R2 5.1K`；`enable=SYS_P050`
- 证据：图 81479376963d / 第 1 页 / 左下 U1 电源区

## 接口

### J2 主接口

J2 引出 EN、GPIO0/1/3/18/19/21/22/26/25/36/32/33、SYS_P050、MCU_P033 与 GND，器件属性标 DNP。

- 参数与网络：`reference=J2`；`part=DNP`；`gpios=GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36`；`gpio_count=12`；`power=SYS_P050; MCU_P033`；`control=EN`；`ground=GND`
- 证据：图 81479376963d / 第 1 页 / 左中 J2 DNP

### J1 Grove

J1 pin1 GND、pin2 SYS_P050、pin3 GPIO32、pin4 GPIO33。

- 参数与网络：`pin_1=GND`；`pin_2=SYS_P050`；`pin_3=GPIO32`；`pin_4=GPIO33`；`signal_level=MCU_P033`；`power=SYS_P050`
- 证据：图 81479376963d / 第 1 页 / 左上 J1 GROVE

## 总线

### 可复用总线

板上未连接 I2C/SPI/I2S/SDIO 外设；GPIO21/22、18/19、25/26、32/33 等通过 J2/J1 供外部复用。

- 参数与网络：`onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`external_gpio=J1/J2`
- 证据：图 81479376963d / 第 1 页 / 完整页

## GPIO 与控制信号

### LED1 SK6812

LED1 SK6812_3535 VDD 接 MCU_P033，DI 接 GPIO27，GND 接地，DO 未连接。

- 参数与网络：`reference=LED1`；`part_number=SK6812_3535`；`data=GPIO27`；`power=MCU_P033`；`data_out=null`
- 证据：图 81479376963d / 第 1 页 / 下中 LED1

### S1 复合按键

S1 将公共节点接地；GPIO39、EN、GPIO0 分别经 R3/R4/R5 5.1K 接该节点，C13 10uF/6.3V 对地。

- 参数与网络：`switch=S1`；`gpio39=R3 5.1K`；`enable=R4 5.1K`；`gpio0=R5 5.1K`；`capacitor=C13 10uF/6.3V`
- 证据：图 81479376963d / 第 1 页 / 右下 S1 网络

## 复位

### 外部 UART 下载

板上无 USB-UART；J2 引出 EN、GPIO0、GPIO1/U0TXD 与 GPIO3/U0RXD，供外部 USB-TTL 下载器控制复位、BOOT 和 UART0。

- 参数与网络：`onboard_bridge=null`；`enable=J2 EN`；`boot=J2 GPIO0`；`tx=J2 GPIO1`；`rx=J2 GPIO3`
- 证据：图 81479376963d / 第 1 页 / J2 与 U2 UART0/EN/GPIO0

## 保护电路

### 可见保护

原理图未画 USB、外部 GPIO ESD 阵列、输入保险丝或反接保护；电源输入直接由 SYS_P050 进入 SY8079AAAC。

- 参数与网络：`usb_esd=null`；`gpio_esd=null`；`input_fuse=null`；`reverse_protection=null`；`input=SYS_P050`
- 证据：图 81479376963d / 第 1 页 / 完整页电源/接口范围

## 射频

### 3D 天线

U2 LNA_IN 经 L2 0R 与 C5/C6 TBD 匹配位连接 ANT1 五金3D天线。

- 参数与网络：`source=LNA_IN`；`series=L2 0R`；`matching_caps=C5/C6 TBD`；`antenna=ANT1 五金3D天线`
- 证据：图 81479376963d / 第 1 页 / 上中 RF 区

## 调试与烧录

### UART0 下载串口

U2 GPIO1/U0TXD 与 GPIO3/U0RXD 直接引出至 J2，图中无串联 USB-UART 或自动下载晶体管。

- 参数与网络：`tx=GPIO1/U0TXD`；`rx=GPIO3/U0RXD`；`connector=J2`；`bridge=null`；`auto_download=null`
- 证据：图 81479376963d / 第 1 页 / U2 GPIO1/3 与 J2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-Pico Mate 核心板架构 | `mcu=U2 ESP32-PICO-D4`；`dcdc=U1 SY8079AAAC`；`rgb=LED1 SK6812_3535`；`main_interface=J2 DNP`；`grove=J1`；`usb_uart=null` |
| 核心器件 | U2 ESP32-PICO-D4 | `reference=U2`；`part_number=ESP32-PICO-D4`；`power=MCU_P033`；`enable=EN`；`uart=GPIO1 U0TXD; GPIO3 U0RXD` |
| 内存与 Flash | ESP32-PICO-D4 Flash | `documented_capacity=4MB`；`module=ESP32-PICO-D4`；`schematic_capacity_label=null` |
| 电源 | U1 SY8079AAAC | `reference=U1`；`input=SYS_P050`；`output=MCU_P033`；`inductor=L1 2.20uH`；`feedback=R1 22K; R2 5.1K`；`enable=SYS_P050` |
| 接口 | J2 主接口 | `reference=J2`；`part=DNP`；`gpios=GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36`；`gpio_count=12`；`power=SYS_P050; MCU_P033`；`control=EN`；`ground=GND` |
| 接口 | Mate 2.54mm 配件 | `documented_pitch=2.54mm`；`documented_accessories=9P/6P headers and sockets; HY2.0-4P socket`；`main_footprint=J2 DNP`；`grove_footprint=J1 GROVE`；`assembly_visible=false` |
| 接口 | J1 Grove | `pin_1=GND`；`pin_2=SYS_P050`；`pin_3=GPIO32`；`pin_4=GPIO33`；`signal_level=MCU_P033`；`power=SYS_P050` |
| GPIO 与控制信号 | LED1 SK6812 | `reference=LED1`；`part_number=SK6812_3535`；`data=GPIO27`；`power=MCU_P033`；`data_out=null` |
| GPIO 与控制信号 | S1 复合按键 | `switch=S1`；`gpio39=R3 5.1K`；`enable=R4 5.1K`；`gpio0=R5 5.1K`；`capacitor=C13 10uF/6.3V` |
| 复位 | 外部 UART 下载 | `onboard_bridge=null`；`enable=J2 EN`；`boot=J2 GPIO0`；`tx=J2 GPIO1`；`rx=J2 GPIO3` |
| 调试与烧录 | UART0 下载串口 | `tx=GPIO1/U0TXD`；`rx=GPIO3/U0RXD`；`connector=J2`；`bridge=null`；`auto_download=null` |
| 射频 | 3D 天线 | `source=LNA_IN`；`series=L2 0R`；`matching_caps=C5/C6 TBD`；`antenna=ANT1 五金3D天线` |
| 总线 | 可复用总线 | `onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`external_gpio=J1/J2` |
| 保护电路 | 可见保护 | `usb_esd=null`；`gpio_esd=null`；`input_fuse=null`；`reverse_protection=null`；`input=SYS_P050` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash，原理图无独立 Flash 且未标 SiP 内部容量。（证据：图 81479376963d / 第 1 页 / U2 与完整页）
- `interface.mate-pitch-accessories`：产品正文列出 2.54mm 排针/排母和 HY2.0-4P 母座；原理图 J2 标 DNP、J1 标 GROVE，但未标机械间距和套装装配状态。（证据：图 81479376963d / 第 1 页 / J1/J2，无机械间距）
- `review.flash-capacity`：ESP32-PICO-D4 内部 Flash 是否固定为 4MB？；原因：容量来自正文，原理图未标。
- `review.mate-assembly`：Mate 套装 2.54mm 排针/排母与 HY2.0-4P 母座的推荐装配和针序是什么？；原因：电气图只标 J2 DNP/J1 GROVE，未标机械间距和套装装配。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `81479376963d1b7ac69231f718bbe2287d47d6a373437cba92c073bfa11365c5` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_pico_mate.md`

源文档 SHA-256：`eb033229e92dd406a6b0ae29e7a9c251e5b326e34aee725c92ace00bef608a05`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
