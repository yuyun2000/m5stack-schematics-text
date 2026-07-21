# Module USB 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module USB |
| SKU | M020 |
| 产品 ID | `module-usb-e0c9e68607fe` |
| 源文档 | `zh_CN/module/usb.md` |

## 概述

Module USB 以 U1（图示值 MAX3421）为 USB 控制器，通过 MOSI/MISO/SCLK/SS 接入 M5Stack_BUS，并以 INT 和 EN/RST 与主机握手。J1 USB Type-A 的 D-/D+ 分别经 33Ω 串阻连接 U1，VBUS 直接来自 M5-Bus VBUS 电源网；VR1 AMS1117-3.3 由 VBUS 生成 +3.3V。Y1 12MHz 为 U1 提供时钟，P1/P2 分别引出 5 路 GPIO 输入和 5 路 GPIO 输出，并附带 GND、+3.3V、VBUS。芯片精确后缀、USB 主机/外设工作模式、板载电池座实现和 EN 兼容性行为未由当前单页完全确认。

## 检索关键词

`Module USB`、`M020`、`MAX3421`、`MAX3421E`、`MAX3421EETJ+`、`AMS1117-3.3`、`USB Type-A`、`USB 2.0`、`SPI`、`MOSI`、`MISO`、`SCLK`、`SS`、`INT`、`EN`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO5`、`GPIO35`、`GPIOIN0`、`GPIOIN1`、`GPIOIN2`、`GPIOIN3`、`GPIOIN4`、`GPIOOUT0`、`GPIOOUT1`、`GPIOOUT2`、`GPIOOUT3`、`GPIOOUT4`、`USB_P`、`USB_N`、`VBUS`、`+3.3V`、`12MHz`、`B5819W SL`、`Header 8`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX3421 | SPI 接口 USB 控制器，提供 USB D+/D-、INT、RST 和 GPIOIN/GPIOOUT | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页中央 U1 MAX3421 |
| VR1 | AMS1117-3.3 | VBUS 到 +3.3V 的线性稳压器 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页左上 VR1 AMS1117-3.3 |
| J1 | USB_TYPE_A | VBUS、D-、D+、GND 标准 USB-A 外部接口 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页左中 J1 USB_TYPE_A |
| J2 | M5Stack_BUS | 主机 SPI、INT、EN、VBUS、+3.3V、BAT 和 GND 堆叠接口 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页右下 J2 M5Stack_BUS |
| P1 | Header 8 | GPIOIN0~GPIOIN4、GND、+3.3V、VBUS 输入扩展口 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页右上 P1 Header 8 |
| P2 | Header 8 | GPIOOUT0~GPIOOUT4、GND、+3.3V、VBUS 输出扩展口 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页右中 P2 Header 8 |
| Y1 | 12MHz | U1 XI/XO 的外部晶振 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 左下 Y1 12MHz |
| D1 | B5819W SL | VBUS/USB 前端中的肖特基二极管 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页 J1 与 U1 之间 D1 B5819W SL |
| R1/R2 | 33Ω | USB D-/D+ 数据线串联电阻 | 图 e830dfd0f4e1 / 第 1 页 / 第 1 页 J1 D-/D+ 与 U1 之间 R1/R2 33Ω |

## 系统结构

### Module USB

U1 通过 SPI、INT 和 EN/RST 连接 J2 主机，通过 USB_P/USB_N 连接 J1，并以 Y1 12MHz 运行；P1/P2 引出 U1 的 GPIO 输入/输出。

- 参数与网络：`controller=U1 MAX3421`；`host=J2 M5Stack_BUS`；`usb=J1 USB_TYPE_A`；`clock=Y1 12MHz`；`gpio_headers=P1/P2`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页完整功能分区

## 电源

### VBUS 电源网

VBUS 由 J2 M5Stack_BUS 的 +5V 端进入，连接 J1.1、VR1 输入以及 P1/P2.8；原理图未画 USB VBUS 负载开关、限流 IC、保险丝或独立使能。

- 参数与网络：`source=J2 +5V/VBUS`；`usb=J1.1`；`regulator_input=VR1 Vin`；`headers=P1.8,P2.8`；`load_switch_shown=false`；`current_limit_shown=false`；`fuse_shown=false`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页全部 VBUS 网络

### VR1 AMS1117-3.3

VR1 Vin 接 VBUS、Vout 输出 +3.3V、GND 接地；输入 C2 100nF/C3 2.2uF，输出 C1 10uF/C4 100nF。

- 参数与网络：`input=VBUS`；`output=+3.3V`；`input_caps=C2 100nF,C3 2.2uF`；`output_caps=C1 10uF,C4 100nF`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页左上 VR1 电源

## 接口

### J1 USB_TYPE_A

J1.1=VBUS、J1.2=D-、J1.3=D+、J1.4=GND；VBUS 同时由 C6 100nF、C7 2.2uF、C5 100nF 对地去耦。

- 参数与网络：`pin_1=VBUS`；`pin_2=D-`；`pin_3=D+`；`pin_4=GND`；`vbus_caps=C6 100nF,C7 2.2uF,C5 100nF`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页左中 J1 与 VBUS 电容

### J2 M5Stack_BUS

本板使用 J2.1/.3/.5=GND、.2=GPIO35/INT、.6=EN、.7=GPIO23/MOSI、.9=GPIO19/MISO、.11=GPIO18/SCLK、.12=+3.3V、.20=GPIO5/SS、.28=VBUS，图中另标 BAT 端。

- 参数与网络：`ground=1,3,5`；`interrupt=2 GPIO35`；`enable=6 EN`；`spi=7 GPIO23 MOSI,9 GPIO19 MISO,11 GPIO18 SCLK,20 GPIO5 SS`；`3v3=12`；`vbus=28`；`battery_label=BAT`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页右下 J2 外部网络

## 总线

### U1 SPI

J2.7 GPIO23/MOSI 连接 U1.16 MOSI，J2.9 GPIO19/MISO 连接 U1.17 MISO，J2.11 GPIO18/SCLK 连接 U1.13 SCLK，J2.20 GPIO5/SS 连接 U1.14 SS。

- 参数与网络：`mosi=J2.7 GPIO23 -> U1.16`；`miso=U1.17 -> J2.9 GPIO19`；`sclk=J2.11 GPIO18 -> U1.13`；`chip_select=J2.20 GPIO5 -> U1.14`；`controller=M5 host`；`device=U1`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 SPI 与 J2

### J1 USB 数据

J1.2 D- 经 R1 33Ω 形成 USB_P 并连接 U1.20 D-；J1.3 D+ 经 R2 33Ω 形成 USB_N 并连接 U1.21 D+。原理图网络名 USB_P/USB_N 与引脚正负命名相反，本文保留图纸原文。

- 参数与网络：`d_minus=J1.2 -> R1 33Ω -> USB_P -> U1.20 D-`；`d_plus=J1.3 -> R2 33Ω -> USB_N -> U1.21 D+`；`connector=USB Type-A`；`net_name_note=USB_P labels D- path; USB_N labels D+ path`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 J1 D-/D+、R1/R2、U1.20/.21

## GPIO 与控制信号

### U1 INT

U1.18 INT 连接 J2.2 GPIO35/INT，并由 R3 2.2K 上拉到 +3.3V。

- 参数与网络：`device_pin=U1.18 INT`；`host_pin=J2.2 GPIO35`；`pullup=R3 2.2K to +3.3V`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 INT、R3 与 J2 GPIO35

### P1 GPIO 输入扩展

P1.1~.5 分别为 GPIOIN0~GPIOIN4，P1.6=GND、P1.7=+3.3V、P1.8=VBUS；U1 GPIOIN5~GPIOIN7 未在 P1 引出。

- 参数与网络：`pin_1=GPIOIN0`；`pin_2=GPIOIN1`；`pin_3=GPIOIN2`；`pin_4=GPIOIN3`；`pin_5=GPIOIN4`；`pin_6=GND`；`pin_7=+3.3V`；`pin_8=VBUS`；`not_exported=GPIOIN5,GPIOIN6,GPIOIN7`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 GPIOIN 与 P1

### P2 GPIO 输出扩展

P2.1~.5 分别为 GPIOOUT0~GPIOOUT4，P2.6=GND、P2.7=+3.3V、P2.8=VBUS；U1 GPIOOUT5~GPIOOUT7 未在 P2 引出。

- 参数与网络：`pin_1=GPIOOUT0`；`pin_2=GPIOOUT1`；`pin_3=GPIOOUT2`；`pin_4=GPIOOUT3`；`pin_5=GPIOOUT4`；`pin_6=GND`；`pin_7=+3.3V`；`pin_8=VBUS`；`not_exported=GPIOOUT5,GPIOOUT6,GPIOOUT7`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 GPIOOUT 与 P2

## 时钟

### U1 USB 时钟

Y1 12MHz 连接 U1.25 XO 与 U1.24 XI，C8/C9 各 18pF 对 GND。

- 参数与网络：`crystal=Y1 12MHz`；`xo=U1.25`；`xi=U1.24`；`load_caps=C8 18pF,C9 18pF`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 左下 Y1/C8/C9

## 复位

### U1 RST 与主机 EN

U1.12 RST 连接 EN 网络并直达 J2.6 EN，且由图示上拉电阻连接 +3.3V；U1 复位与主机使能共用同一网络。

- 参数与网络：`device_pin=U1.12 RST`；`host_pin=J2.6 EN`；`net=EN`；`pullup_rail=+3.3V`；`shared_reset_enable=true`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 RST/EN 与 J2.6

## 保护电路

### USB 与 VBUS 保护

图中 USB 前端包含 D1 B5819W SL 和 D-/D+ 串联 33Ω，但未画专用 USB ESD 阵列；VBUS 未画过流开关或保险丝。

- 参数与网络：`schottky=D1 B5819W SL`；`data_series=R1/R2 33Ω`；`usb_esd_array_shown=false`；`vbus_overcurrent_shown=false`；`vbus_fuse_shown=false`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 J1/U1 USB 前端与 VBUS

## 内存与 Flash

### 外部存储器

完整原理图未展示 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页完整图无存储器

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module USB | `controller=U1 MAX3421`；`host=J2 M5Stack_BUS`；`usb=J1 USB_TYPE_A`；`clock=Y1 12MHz`；`gpio_headers=P1/P2` |
| 核心器件 | U1 精确型号 | `schematic_value=MAX3421`；`document_family=MAX3421E`；`old_variant=MAX3421EEHJ+`；`new_variant=MAX3421EETJ+`；`assembled_variant=null` |
| 总线 | U1 SPI | `mosi=J2.7 GPIO23 -> U1.16`；`miso=U1.17 -> J2.9 GPIO19`；`sclk=J2.11 GPIO18 -> U1.13`；`chip_select=J2.20 GPIO5 -> U1.14`；`controller=M5 host`；`device=U1` |
| GPIO 与控制信号 | U1 INT | `device_pin=U1.18 INT`；`host_pin=J2.2 GPIO35`；`pullup=R3 2.2K to +3.3V` |
| 复位 | U1 RST 与主机 EN | `device_pin=U1.12 RST`；`host_pin=J2.6 EN`；`net=EN`；`pullup_rail=+3.3V`；`shared_reset_enable=true` |
| 其他事实 | 正文中的 Core2/CoreS3 兼容性 | `documented_incompatible=Core2,CoreS3`；`documented_cause=3.3V power-up timing / EN low`；`schematic_shared_net=true`；`verified_boot_behavior=null` |
| 总线 | J1 USB 数据 | `d_minus=J1.2 -> R1 33Ω -> USB_P -> U1.20 D-`；`d_plus=J1.3 -> R2 33Ω -> USB_N -> U1.21 D+`；`connector=USB Type-A`；`net_name_note=USB_P labels D- path; USB_N labels D+ path` |
| 接口 | J1 USB_TYPE_A | `pin_1=VBUS`；`pin_2=D-`；`pin_3=D+`；`pin_4=GND`；`vbus_caps=C6 100nF,C7 2.2uF,C5 100nF` |
| 电源 | VBUS 电源网 | `source=J2 +5V/VBUS`；`usb=J1.1`；`regulator_input=VR1 Vin`；`headers=P1.8,P2.8`；`load_switch_shown=false`；`current_limit_shown=false`；`fuse_shown=false` |
| 电源 | VR1 AMS1117-3.3 | `input=VBUS`；`output=+3.3V`；`input_caps=C2 100nF,C3 2.2uF`；`output_caps=C1 10uF,C4 100nF` |
| 时钟 | U1 USB 时钟 | `crystal=Y1 12MHz`；`xo=U1.25`；`xi=U1.24`；`load_caps=C8 18pF,C9 18pF` |
| GPIO 与控制信号 | P1 GPIO 输入扩展 | `pin_1=GPIOIN0`；`pin_2=GPIOIN1`；`pin_3=GPIOIN2`；`pin_4=GPIOIN3`；`pin_5=GPIOIN4`；`pin_6=GND`；`pin_7=+3.3V`；`pin_8=VBUS`；`not_exported=GPIOIN5,GPIOIN6,GPIOIN7` |
| GPIO 与控制信号 | P2 GPIO 输出扩展 | `pin_1=GPIOOUT0`；`pin_2=GPIOOUT1`；`pin_3=GPIOOUT2`；`pin_4=GPIOOUT3`；`pin_5=GPIOOUT4`；`pin_6=GND`；`pin_7=+3.3V`；`pin_8=VBUS`；`not_exported=GPIOOUT5,GPIOOUT6,GPIOOUT7` |
| 接口 | J2 M5Stack_BUS | `ground=1,3,5`；`interrupt=2 GPIO35`；`enable=6 EN`；`spi=7 GPIO23 MOSI,9 GPIO19 MISO,11 GPIO18 SCLK,20 GPIO5 SS`；`3v3=12`；`vbus=28`；`battery_label=BAT` |
| 保护电路 | USB 与 VBUS 保护 | `schottky=D1 B5819W SL`；`data_series=R1/R2 33Ω`；`usb_esd_array_shown=false`；`vbus_overcurrent_shown=false`；`vbus_fuse_shown=false` |
| 其他事实 | 正文中的 USB 主机/外设模式 | `documented_modes=USB host and peripheral`；`connector=USB Type-A`；`role_switch_network_shown=false`；`usb_id_shown=false`；`firmware_mode=null` |
| 电源 | 正文中的板载锂电池座 | `documented_battery_holder=true`；`battery_connector_reference=null`；`charger_shown=false`；`battery_protection_shown=false`；`bat_to_vbus_path_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `component.controller-variant`：原理图器件值写为 MAX3421，正文写 MAX3421E 且版本记录称由 MAX3421EEHJ+ 改为 MAX3421EETJ+；当前装配后缀不能仅由本页确定。（证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1 标注 MAX3421）
- `other.en-compatibility`：正文称 3.3V 上电时序可能使 USB 芯片拉低共享 EN，导致 Core2/CoreS3 无法启动；原理图确认 RST/EN 共网，但不能确认具体主机上的启动行为。（证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 U1.12 RST 与 J2.6 EN 共网）
- `other.usb-modes`：正文称支持 USB 主机和外设模式；原理图显示 USB Type-A、MAX3421 系列硬件与 SPI，但未定义固件模式、角色切换或 USB ID/OTG 检测。（证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页 J1/U1 无角色切换网络）
- `power.documented-battery-holder`：正文称板载锂电池座，原理图 J2 仅显示 BAT 端标注，未画独立电池连接器、充电 IC、保护 IC 或 BAT 到 VBUS 的电源路径。（证据：图 e830dfd0f4e1 / 第 1 页 / 第 1 页完整电源图与 J2 BAT 标注）
- `review.controller-variant`：请依据 M020 当前 BOM 与 U1 丝印确认 MAX3421E 的准确封装后缀和硬件版本。；原因：原理图仅标 MAX3421，版本记录列出两个不同后缀。
- `review.en-compatibility`：请在对应 Core2/CoreS3 硬件版本上确认共享 EN 的上电波形与启动失败条件。；原因：原理图确认共网，但不能证明所有主机版本的动态行为。
- `review.usb-modes`：请依据 U1 具体变体和模块固件确认可用的 USB 主机/外设模式及角色配置方式。；原因：原理图未显示 OTG/ID 或角色切换电路。
- `review.battery-holder`：请依据 PCB/BOM 确认板载锂电池座位号以及 BAT 的供电、保护和充电路径。；原因：当前页只在 J2 标 BAT，没有画电池座或电源管理电路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e830dfd0f4e1753eeff48b9b1b5500a81472a873437c04c69e2da68531f2d80c` | `https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_sch_01.webp` |

---

源文档：`zh_CN/module/usb.md`

源文档 SHA-256：`faaee67c427d011bfa181e834b50d78edff732a37a91eb1ca6602ba1056faecb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
