# Stamp-C3U 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-C3U |
| SKU | C122-B |
| 产品 ID | `stamp-c3u-0078f7670939` |
| 源文档 | `zh_CN/core/stamp_c3u.md` |

## 概述

Stamp-C3U 以 U1 ESP32-C3 为主控，GPIO18/GPIO19 直接连接 USB-C 的 D-/D+，板上未配置独立 USB-UART 芯片。USB VBUS 经磁珠和肖特基二极管进入 HM8089 降压电路，生成 VCC_3V3。板上还包含 PROANT_440 天线、外部晶体、GPIO2 驱动的 SK6812、GPIO9 用户按键和 EN 复位按键。

## 检索关键词

`Stamp-C3U`、`C122-B`、`ESP32-C3`、`HM8089`、`SK6812`、`PROANT_440`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`GPIO18`、`GPIO19`、`GPIO2`、`GPIO9`、`ESP32_EN`、`ESP32_U0RXD`、`ESP32_U0TXD`、`VCC_3V3`、`VIN_5V`、`B5819WS`、`LQM2MPN2R2NG0L`、`LQP15MN2N7B02D`、`TXC/8Z4000017`、`USB CDC`、`USB JTAG`、`RISC-V`、`4MB Flash`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-C3 | 系统主控，集成原生 USB、GPIO、UART、SPI 存储接口和射频端口 | 图 eafaa3fac84e / 第 1 页 / 左上，U1 ESP32-C3 全部引脚与网络 |
| ANT1 | PROANT_440 | ESP32-C3 射频天线，连接 ESP_LNA 匹配网络 | 图 eafaa3fac84e / 第 1 页 / 上中，ANT1 PROANT_440、ESP_LNA、C1/L1/C2 匹配网络 |
| J1 | USB-TYPEC | USB 供电与 ESP32-C3 原生 USB 数据接口 | 图 eafaa3fac84e / 第 1 页 / 右上，J1 USB-TYPEC、VIN、USB_D_P/USB_D_N、R1/R3 |
| L2 | Sunlord/UPZ1608E101-3R0TF/100R/3A | USB VIN 到 VIN_5V 的电源磁珠滤波 | 图 eafaa3fac84e / 第 1 页 / 中上，L2 Sunlord/UPZ1608E101-3R0TF/100R/3A，VIN/VIN_5V |
| D1 | B5819WS SOD323 | VIN_5V 到 V1 的串联肖特基二极管 | 图 eafaa3fac84e / 第 1 页 / 中下，D1 B5819WS SOD323，VIN_5V 到 V1 |
| U2 | HM8089 | V1 输入的降压转换器，生成 VCC_3V3 | 图 eafaa3fac84e / 第 1 页 / 中下，U2 HM8089、L3、R8/R9、VCC_3V3 |
| L3 | LQM2MPN2R2NG0L | HM8089 降压输出电感 | 图 eafaa3fac84e / 第 1 页 / U2 SW pin 3 到 VCC_3V3，L3 LQM2MPN2R2NG0L |
| X1 | TXC/8Z4000017/立创采购 | ESP32-C3 外部主晶体 | 图 eafaa3fac84e / 第 1 页 / 左中，X1 TXC/8Z4000017，XTAL_P/XTAL_N、C5/C6 |
| OS1 | SMT_SW_PTS_820 | 将 ESP32_EN 拉低的复位按键 | 图 eafaa3fac84e / 第 1 页 / 右中，OS1 SMT_SW_PTS_820、ESP32_EN、R10/C21 |
| OS2 | SMT_SW_PTS_820 | GPIO9 用户/启动按键 | 图 eafaa3fac84e / 第 1 页 / 右中，OS2 SMT_SW_PTS_820、GPIO9、R6 10K |
| U3 | SK6812 | GPIO2 控制的可编程 RGB LED | 图 eafaa3fac84e / 第 1 页 / 右下，U3 SK6812、DIN GPIO2、VCC_3V3 |

## 系统结构

### 最小系统架构

Stamp-C3U 由单颗 U1 ESP32-C3、外部晶体、PROANT_440 天线、HM8089 3.3 V 降压、原生 USB-C、两枚按键和一颗 SK6812 构成。

- 参数与网络：`controller=U1 ESP32-C3`；`clock=X1 TXC/8Z4000017`；`antenna=ANT1 PROANT_440`；`regulator=U2 HM8089`；`usb=J1 USB-TYPEC`；`rgb=U3 SK6812`
- 证据：图 eafaa3fac84e / 第 1 页 / 整页：U1、ANT1、X1、J1、U2、OS1/OS2、U3

## 电源

### USB 输入滤波

J1 VIN 经 L2 Sunlord UPZ1608E101-3R0TF（标注 100R/3A）形成 VIN_5V，C4 4.7 µF 对 VIN_5V 去耦。

- 参数与网络：`input=VIN`；`filter=L2 Sunlord/UPZ1608E101-3R0TF/100R/3A`；`output=VIN_5V`；`capacitor=C4 4.7uF/10V`
- 证据：图 eafaa3fac84e / 第 1 页 / 中上，VIN/L2/VIN_5V/C4

### 3.3 V 降压电源

U2 HM8089 由 V1 供电，EN 接 V1，经 L3 LQM2MPN2R2NG0L 输出 VCC_3V3；反馈分压为 R8 68 kΩ 与 R9 15 kΩ。

- 参数与网络：`reference=U2`；`part_number=HM8089`；`input=V1`；`enable=V1`；`inductor=L3 LQM2MPN2R2NG0L`；`output=VCC_3V3`；`feedback_upper=R8 68K 1%`；`feedback_lower=R9 15K 1%`
- 证据：图 eafaa3fac84e / 第 1 页 / 中下，U2/L3/R8/R9/C9/C10

## 接口

### USB Type-C

J1 的 VCC 连接 VIN，DP1/DP2 并接 USB_D_P，DN1/DN2 并接 USB_D_N，CC1/CC2 分别通过 R1/R3 5.1 kΩ 接地。

- 参数与网络：`reference=J1`；`vbus=VIN`；`dp=USB_D_P`；`dn=USB_D_N`；`cc1=R1 5.1K to GND`；`cc2=R3 5.1K to GND`
- 证据：图 eafaa3fac84e / 第 1 页 / 右上，J1 pins A6/B6/A7/B7、R1/R3

## 总线

### ESP32-C3 原生 USB

U1 GPIO18 连接 USB_D_N，GPIO19 连接 USB_D_P，数据线直接到 J1，原理图中未设置独立 USB-UART 桥接芯片。

- 参数与网络：`controller=U1 ESP32-C3`；`dm=GPIO18/USB_D_N`；`dp=GPIO19/USB_D_P`；`connector=J1 USB-TYPEC`；`usb_uart_bridge=null`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 pins 25/26 GPIO18/GPIO19 与 J1 USB_D_N/P

### UART0

U1 U0RXD 引出为 ESP32_U0RXD，U0TXD 通过 R5 499 Ω 引出为 ESP32_U0TXD。

- 参数与网络：`rx=ESP32_U0RXD`；`tx=ESP32_U0TXD`；`tx_series_resistor=R5 499R`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 pins 27/28 U0RXD/U0TXD 与 R5

## GPIO 与控制信号

### 主控 GPIO 网络

原理图明确标出 GPIO0 至 GPIO10，以及 GPIO18、GPIO19；GPIO2 连接 RGB LED，GPIO9 连接按键，GPIO18/19 连接 USB。

- 参数与网络：`general_nets=GPIO0; GPIO1; GPIO3; GPIO4; GPIO5; GPIO6; GPIO7; GPIO8; GPIO10`；`rgb=GPIO2`；`button=GPIO9`；`usb_dm=GPIO18`；`usb_dp=GPIO19`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 右侧 GPIO0-GPIO10、GPIO18、GPIO19 网络

### RGB LED GPIO

U3 SK6812 的 DIN 连接 GPIO2，VDD 连接 VCC_3V3，DOUT 未连接。

- 参数与网络：`reference=U3`；`part_number=SK6812`；`data_in=GPIO2`；`supply=VCC_3V3`；`data_out=NC`
- 证据：图 eafaa3fac84e / 第 1 页 / 右下，U3 pins DIN/DOUT/VDD/VSS

### GPIO9 用户按键

OS2 按下时将 GPIO9 拉低，R6 10 kΩ 将 GPIO9 上拉到 VCC_3V3。

- 参数与网络：`reference=OS2`；`gpio=GPIO9`；`active_level=low`；`pullup=R6 10K to VCC_3V3`
- 证据：图 eafaa3fac84e / 第 1 页 / 右中，OS2/R6/GPIO9

## 时钟

### ESP32-C3 外部晶体

X1 标注 TXC/8Z4000017/立创采购，连接 XTAL_P/XTAL_N；C5/C6 均标注 GRM1555C1H180JA01D。

- 参数与网络：`reference=X1`；`part_number=TXC/8Z4000017/立创采购`；`nets=XTAL_P; XTAL_N`；`load_capacitors=C5/C6 GRM1555C1H180JA01D`
- 证据：图 eafaa3fac84e / 第 1 页 / 左中，X1/C5/C6/XTAL_P/XTAL_N

## 复位

### 主控复位

ESP32_EN 由 R10 10 kΩ 上拉到 VCC_3V3，并由 C21 470 nF 对地；OS1 按下时将 ESP32_EN 拉低复位。

- 参数与网络：`net=ESP32_EN`；`pullup=R10 10K`；`capacitor=C21 470nF/10V`；`switch=OS1 SMT_SW_PTS_820`；`active_level=low`
- 证据：图 eafaa3fac84e / 第 1 页 / 右中，R10/C21/OS1/ESP32_EN

## 保护电路

### 输入串联二极管

D1 B5819WS SOD323 串联在 VIN_5V 与 U2 输入节点 V1 之间。

- 参数与网络：`reference=D1`；`part_number=B5819WS SOD323`；`anode_net=VIN_5V`；`cathode_net=V1`
- 证据：图 eafaa3fac84e / 第 1 页 / 中下，D1 位于 VIN_5V/V1 之间

## 射频

### 射频天线与匹配

U1 LNA_IN 通过 ESP_LNA 匹配网络连接 ANT1 PROANT_440；原理图同时标注“TBD, need further RF matching”。

- 参数与网络：`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series_marking=C1 LQP15MN2N7B02D`；`shunt_marking=C2 GRM1555C1H2R4BA01D`；`note=TBD, need further RF matching`
- 证据：图 eafaa3fac84e / 第 1 页 / 上中，ESP_LNA/C1/L1/C2/ANT1 与 TBD 注释

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 最小系统架构 | `controller=U1 ESP32-C3`；`clock=X1 TXC/8Z4000017`；`antenna=ANT1 PROANT_440`；`regulator=U2 HM8089`；`usb=J1 USB-TYPEC`；`rgb=U3 SK6812` |
| 接口 | USB Type-C | `reference=J1`；`vbus=VIN`；`dp=USB_D_P`；`dn=USB_D_N`；`cc1=R1 5.1K to GND`；`cc2=R3 5.1K to GND` |
| 总线 | ESP32-C3 原生 USB | `controller=U1 ESP32-C3`；`dm=GPIO18/USB_D_N`；`dp=GPIO19/USB_D_P`；`connector=J1 USB-TYPEC`；`usb_uart_bridge=null` |
| 总线 | UART0 | `rx=ESP32_U0RXD`；`tx=ESP32_U0TXD`；`tx_series_resistor=R5 499R` |
| GPIO 与控制信号 | 主控 GPIO 网络 | `general_nets=GPIO0; GPIO1; GPIO3; GPIO4; GPIO5; GPIO6; GPIO7; GPIO8; GPIO10`；`rgb=GPIO2`；`button=GPIO9`；`usb_dm=GPIO18`；`usb_dp=GPIO19` |
| GPIO 与控制信号 | RGB LED GPIO | `reference=U3`；`part_number=SK6812`；`data_in=GPIO2`；`supply=VCC_3V3`；`data_out=NC` |
| GPIO 与控制信号 | GPIO9 用户按键 | `reference=OS2`；`gpio=GPIO9`；`active_level=low`；`pullup=R6 10K to VCC_3V3` |
| 复位 | 主控复位 | `net=ESP32_EN`；`pullup=R10 10K`；`capacitor=C21 470nF/10V`；`switch=OS1 SMT_SW_PTS_820`；`active_level=low` |
| 电源 | USB 输入滤波 | `input=VIN`；`filter=L2 Sunlord/UPZ1608E101-3R0TF/100R/3A`；`output=VIN_5V`；`capacitor=C4 4.7uF/10V` |
| 保护电路 | 输入串联二极管 | `reference=D1`；`part_number=B5819WS SOD323`；`anode_net=VIN_5V`；`cathode_net=V1` |
| 电源 | 3.3 V 降压电源 | `reference=U2`；`part_number=HM8089`；`input=V1`；`enable=V1`；`inductor=L3 LQM2MPN2R2NG0L`；`output=VCC_3V3`；`feedback_upper=R8 68K 1%`；`feedback_lower=R9 15K 1%` |
| 射频 | 射频天线与匹配 | `soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series_marking=C1 LQP15MN2N7B02D`；`shunt_marking=C2 GRM1555C1H2R4BA01D`；`note=TBD, need further RF matching` |
| 时钟 | ESP32-C3 外部晶体 | `reference=X1`；`part_number=TXC/8Z4000017/立创采购`；`nets=XTAL_P; XTAL_N`；`load_capacitors=C5/C6 GRM1555C1H180JA01D` |
| 存储 | Flash 容量 | `controller=U1 ESP32-C3`；`claimed_flash=4MB`；`external_flash=not shown` |
| 内存与 Flash | 片内 SRAM/ROM | `controller=U1 ESP32-C3`；`claimed_sram=400KB`；`claimed_rom=384KB`；`claimed_rtc_sram=8KB` |
| 系统结构 | 处理器与无线规格 | `controller=U1 ESP32-C3`；`unverified_cpu=32-bit RISC-V single core up to 160MHz`；`unverified_wifi=2.4GHz 802.11 b/g/n` |
| 时钟 | 主晶体频率 | `reference=X1`；`part_number=TXC/8Z4000017/立创采购`；`frequency=not printed` |
| 调试与烧录 | USB CDC/JTAG/下载功能 | `hardware=GPIO18/19 native USB`；`unverified_functions=USB CDC; USB JTAG; firmware download mode` |
| 接口 | 外接 IO 数量与焊盘映射 | `claimed_count=14`；`claimed_pitch=2.54mm`；`schematic_connectors=not shown` |

## 待确认事项

- `storage.flash-capacity`：原理图未显示独立 Flash 器件，也未直接标注产品正文所述 4 MB Flash。（证据：图 eafaa3fac84e / 第 1 页 / U1 SPIHD/SPIWP/SPICS0/SPICLK/SPID/SPIQ 区域未画外部 Flash）
- `memory.internal-memory`：原理图只标注 U1 为 ESP32-C3，未直接给出 400 KB SRAM、384 KB ROM 或 8 KB RTC SRAM。（证据：图 eafaa3fac84e / 第 1 页 / U1 型号框未列内部存储容量）
- `system.performance-radio`：原理图未直接标注 RISC-V 核心、160 MHz 主频或 2.4 GHz Wi-Fi 协议/速率参数。（证据：图 eafaa3fac84e / 第 1 页 / U1 仅标 ESP32-C3，ANT1 仅标 PROANT_440）
- `clock.crystal-frequency`：原理图给出 X1 采购型号，但未以频率文本直接标注其振荡频率。（证据：图 eafaa3fac84e / 第 1 页 / X1 周边无 MHz 频率标注）
- `debug.usb-functions`：原理图确认 ESP32-C3 原生 USB 电气连接，但未直接描述 CDC、JTAG 或下载模式的软件功能及启用条件。（证据：图 eafaa3fac84e / 第 1 页 / U1 GPIO18/19 到 J1，仅有电气网络）
- `interface.exposed-io`：原理图标出 GPIO 网络但未画模块边缘焊盘/连接器，无法仅由该页确认正文所述 14 路 IO 的完整外接焊盘列表与 2.54 mm 间距。（证据：图 eafaa3fac84e / 第 1 页 / 整页未画外接焊盘位号或连接器）
- `review.flash-capacity`：请用 ESP32-C3 封装/BOM 确认 4 MB Flash 的实现与容量。；原因：原理图未显示独立 Flash 或容量文本。
- `review.internal-memory`：请用 ESP32-C3 datasheet 复核 SRAM、ROM 与 RTC SRAM 容量。；原因：这些片内参数不在原理图中直接标注。
- `review.performance-radio`：请用 ESP32-C3 datasheet 复核 CPU 架构/频率和 Wi-Fi 规格。；原因：原理图只标芯片与天线，不列性能参数。
- `review.crystal-frequency`：请用 X1 料号资料确认主晶体频率。；原因：原理图未印出 MHz 数值。
- `review.usb-functions`：请用 ESP32-C3 datasheet/固件配置确认 USB CDC、JTAG 与下载模式行为。；原因：原理图只证明原生 USB 电气连接。
- `review.exposed-io`：请用 PinMap/PCB 文件确认 14 路外接 IO、焊盘编号和 2.54 mm 间距。；原因：当前原理图未画外接焊盘或连接器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `eafaa3fac84eb1b3d7575a74e0e222e3b4d255255e1460c27ed9f8baf8a11957` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3u_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_c3u.md`

源文档 SHA-256：`b3220e41dbbadc1c09f8d11b13af6bed03855af9cc976dc9004f8646621239f8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
