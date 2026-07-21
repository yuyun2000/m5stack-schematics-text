# Stamp-C3U Mate 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-C3U Mate |
| SKU | K122 |
| 产品 ID | `stamp-c3u-mate-2c4b99d9b539` |
| 源文档 | `zh_CN/core/stamp_c3u_mate.md` |

## 概述

Stamp-C3U Mate 的本地原理图为 Stamp-C3U 核心板：U1 ESP32-C3 直接以 GPIO18/GPIO19 原生 USB D-/D+ 连接 J1 Type-C，不使用外置 USB-UART。U2 HM8089 从 VIN_5V 生成 VCC_3V3，OS1/OS2 分别控制 ESP32_EN 与 GPIO9 BOOT，U3 SK6812 接 GPIO2。射频由 ESP_LNA 经预留匹配连接 ANT1 PROANT_440；Mate 套装附带的排针、排母与 HY2.0-4P 母座未出现在该核心板电气图中。

## 检索关键词

`Stamp-C3U Mate`、`K122`、`Stamp-C3U`、`ESP32-C3`、`HM8089`、`SK6812`、`PROANT_440`、`native USB`、`USB CDC`、`USB JTAG`、`USB_D_N`、`USB_D_P`、`GPIO18`、`GPIO19`、`GPIO9 BOOT`、`GPIO2 RGB`、`ESP32_EN`、`VIN`、`VIN_5V`、`VCC_3V3`、`USB Type-C`、`UART0`、`GPIO0`、`GPIO1`、`GPIO3`、`GPIO4`、`GPIO5`、`GPIO6`、`GPIO7`、`GPIO8`、`GPIO10`、`GPIO21`、`GPIO22`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-C3 | 主控，提供原生 USB、UART0、14 路 GPIO、RF 与启动控制 | 图 eafaa3fac84e / 第 1 页 / 左上 U1 ESP32-C3 |
| U2 | HM8089 | VIN_5V 至 VCC_3V3 的降压转换器 | 图 eafaa3fac84e / 第 1 页 / 中央下 U2 HM8089 |
| U3 | SK6812 | GPIO2 控制的可编程 RGB LED | 图 eafaa3fac84e / 第 1 页 / 右下 U3 SK6812 |
| J1 | USB-TYPEC | VIN 输入与 ESP32-C3 原生 USB 数据接口 | 图 eafaa3fac84e / 第 1 页 / 右上 J1 USB-TYPEC |
| ANT1 | PROANT_440 | ESP32-C3 射频天线与预留匹配网络 | 图 eafaa3fac84e / 第 1 页 / 上中 ANT1 PROANT_440 |
| X1 | TXC/8Z40000017 | ESP32-C3 外部主晶振 | 图 eafaa3fac84e / 第 1 页 / 左中 X1 |
| OS1/OS2 | SMT_SW_PTS_820 | ESP32_EN 复位按键与 GPIO9 BOOT/用户按键 | 图 eafaa3fac84e / 第 1 页 / 右中 OS1/OS2 |
| D1 | B5819WS SOD323 | VIN_5V 至 HM8089 输入 VI 的串联肖特基二极管 | 图 eafaa3fac84e / 第 1 页 / 中央下 D1 B5819WS |
| L2 | Sunlord/UPZ1608E101-3R0TF/100R/3A | VIN 至 VIN_5V 输入滤波磁珠 | 图 eafaa3fac84e / 第 1 页 / 右上 VIN/L2/VIN_5V |

## 系统结构

### Stamp-C3U Mate 核心板架构

ESP32-C3 直接连接 Type-C 原生 USB，HM8089 生成 3.3V，SK6812 接 GPIO2，EN/GPIO9 配置复位与 BOOT 按键，PROANT_440 构成射频端。

- 参数与网络：`mcu=U1 ESP32-C3`；`dcdc=U2 HM8089`；`rgb=U3 SK6812`；`usb=J1 USB-TYPEC`；`antenna=ANT1 PROANT_440`；`usb_bridge=null`
- 证据：图 eafaa3fac84e / 第 1 页 / 完整原理图页

## 核心器件

### U1 ESP32-C3

U1 明确标 ESP32-C3，GPIO0-10、GPIO18/19/21/22、UART0、XTAL、ESP_LNA 与 CHIP_EN 在图中引出。

- 参数与网络：`reference=U1`；`part_number=ESP32-C3`；`power=VCC_3V3`；`enable=ESP32_EN`；`uart=ESP32_U0RXD/ESP32_U0TXD`；`native_usb=GPIO18/19`
- 证据：图 eafaa3fac84e / 第 1 页 / 左上 U1

## 电源

### VIN 输入滤波

VIN 经 L2 Sunlord/UPZ1608E101-3R0TF/100R/3A 形成 VIN_5V，C4 4.7uF/10V 接地。

- 参数与网络：`input=VIN`；`output=VIN_5V`；`filter=L2 100R/3A`；`capacitor=C4 4.7uF/10V`
- 证据：图 eafaa3fac84e / 第 1 页 / 右上 VIN/L2/C4

### U2 HM8089

VIN_5V 经 D1 B5819WS 形成 VI，U2 HM8089 以 VI 为 VIN/EN，经 L3 LQM2MPN2R2NG0L 输出 VCC_3V3，反馈为 R8 68K/R9 15K。

- 参数与网络：`reference=U2`；`input=VIN_5V -> D1 -> VI`；`output=VCC_3V3`；`enable=VI`；`inductor=L3 LQM2MPN2R2NG0L`；`feedback=R8 68K; R9 15K`
- 证据：图 eafaa3fac84e / 第 1 页 / 中央下 D1/U2/L3

## 接口

### J1 USB Type-C

J1 VCC 接 VIN，A6/B6 汇入 USB_D_P，A7/B7 汇入 USB_D_N，CC1/CC2 经 R1/R3 5.1K 接地。

- 参数与网络：`reference=J1`；`power=VIN`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R3 5.1K to GND`
- 证据：图 eafaa3fac84e / 第 1 页 / 右上 J1

## 总线

### ESP32-C3 原生 USB

GPIO18 接 USB_D_N，GPIO19 接 USB_D_P 并直接连接 J1；图中无 CH9102/CP2104 等 USB-UART 桥。

- 参数与网络：`controller=U1 ESP32-C3`；`dm=GPIO18 / USB_D_N`；`dp=GPIO19 / USB_D_P`；`connector=J1 USB-TYPEC`；`bridge=null`；`functions=download/JTAG/CDC (controller capability documented, wiring confirmed)`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 GPIO18/19 与 J1 USB D-/D+

### 可复用外设总线

板上仅固定使用原生 USB、UART0、GPIO2 RGB 和 GPIO9 按键；未连接板载 I2C/SPI/I2S/TWAI 外设。

- 参数与网络：`usb=GPIO18/19`；`uart=UART0 exposed`；`onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`onboard_twai_devices=null`
- 证据：图 eafaa3fac84e / 第 1 页 / 完整页

## GPIO 与控制信号

### 14 路 GPIO

U1 图中可见 GPIO0-10、GPIO18、GPIO19、GPIO21、GPIO22；扣除板载 GPIO2 RGB 与 GPIO9 按键后，其余仍作为通用复用信号。

- 参数与网络：`gpios=GPIO0-GPIO10; GPIO18; GPIO19; GPIO21; GPIO22`；`visible_count=15`；`documented_io_count=14`；`rgb=GPIO2`；`button=GPIO9`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 GPIO 列

### U3 SK6812

U3 SK6812 DIN 接 GPIO2，VDD 接 VCC_3V3，VSS 接 GND，DOUT 未连接。

- 参数与网络：`reference=U3`；`data=GPIO2`；`power=VCC_3V3`；`data_out=null`
- 证据：图 eafaa3fac84e / 第 1 页 / 右下 U3

### EN 与 GPIO9 按键

OS1 按下将 ESP32_EN 接地，R10 10K 上拉且 C21 470nF 对地；OS2 按下将 GPIO9 接地，R6 10K 上拉。

- 参数与网络：`reset=OS1 -> ESP32_EN`；`reset_pullup=R10 10K`；`reset_cap=C21 470nF`；`boot_button=OS2 -> GPIO9`；`boot_pullup=R6 10K`
- 证据：图 eafaa3fac84e / 第 1 页 / 右中 OS1/OS2

## 时钟

### ESP32-C3 主晶振

X1 TXC/8Z40000017 连接 XTAL_P/N，R7/LQP15MN27NG02D 串联于 XTAL_N，C5/C6 接地；频率未直接标注。

- 参数与网络：`crystal=X1 TXC/8Z40000017`；`series=R7 LQP15MN27NG02D`；`capacitors=C5/C6 GRM1555C1H180JA01D`；`frequency_visible=false`
- 证据：图 eafaa3fac84e / 第 1 页 / 左中 X1

## 复位

### GPIO9 下载启动

GPIO9 由 R6 10K 上拉至 VCC_3V3，OS2 可将其拉低；该按键用于进入下载模式，ESP32_EN 由独立 OS1 控制。

- 参数与网络：`boot_gpio=GPIO9`；`boot_switch=OS2`；`boot_pullup=R6 10K`；`reset_switch=OS1`
- 证据：图 eafaa3fac84e / 第 1 页 / 右中 GPIO9/OS2 与 ESP32_EN/OS1

## 保护电路

### 输入与 USB 可见保护

原理图显示 VIN 磁珠 L2、D1 输入肖特基和 CC 下拉，但未画 USB D+/D- ESD 阵列或 VBUS 自恢复保险丝。

- 参数与网络：`input_filter=L2`；`input_diode=D1 B5819WS`；`cc_resistors=R1/R3 5.1K`；`usb_data_esd_visible=false`；`vbus_fuse_visible=false`
- 证据：图 eafaa3fac84e / 第 1 页 / J1 USB 与 VIN/U2 电源区

## 射频

### ESP_LNA 天线网络

ESP_LNA 经 L1/C1/C2 预留匹配连接 ANT1 PROANT_440，图中注释 TBD, need further RF matching。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series=C1 LQP15MN2N7B02D`；`shunt=L1; C2 GRM1555C1H2R4BA01D`
- 证据：图 eafaa3fac84e / 第 1 页 / 上中 RF 区

## 调试与烧录

### UART0 引出

U1 U0TXD 经 R5 499R 输出 ESP32_U0TXD，U0RXD 网络为 ESP32_U0RXD；两线未接板载桥。

- 参数与网络：`tx=U0TXD -> R5 499R -> ESP32_U0TXD`；`rx=ESP32_U0RXD`；`onboard_bridge=null`
- 证据：图 eafaa3fac84e / 第 1 页 / U1 U0RXD/U0TXD

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-C3U Mate 核心板架构 | `mcu=U1 ESP32-C3`；`dcdc=U2 HM8089`；`rgb=U3 SK6812`；`usb=J1 USB-TYPEC`；`antenna=ANT1 PROANT_440`；`usb_bridge=null` |
| 核心器件 | U1 ESP32-C3 | `reference=U1`；`part_number=ESP32-C3`；`power=VCC_3V3`；`enable=ESP32_EN`；`uart=ESP32_U0RXD/ESP32_U0TXD`；`native_usb=GPIO18/19` |
| 内存与 Flash | ESP32-C3 Flash | `documented_capacity=4MB`；`discrete_flash=null`；`schematic_capacity_label=null` |
| GPIO 与控制信号 | 14 路 GPIO | `gpios=GPIO0-GPIO10; GPIO18; GPIO19; GPIO21; GPIO22`；`visible_count=15`；`documented_io_count=14`；`rgb=GPIO2`；`button=GPIO9` |
| 接口 | Mate 排针/排母/HY2.0 配件 | `documented_accessories=2.54mm headers/sockets; HY2.0-4P sockets`；`connector_references=null`；`schematic_visible=false` |
| 总线 | ESP32-C3 原生 USB | `controller=U1 ESP32-C3`；`dm=GPIO18 / USB_D_N`；`dp=GPIO19 / USB_D_P`；`connector=J1 USB-TYPEC`；`bridge=null`；`functions=download/JTAG/CDC (controller capability documented, wiring confirmed)` |
| 接口 | J1 USB Type-C | `reference=J1`；`power=VIN`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R3 5.1K to GND` |
| 调试与烧录 | UART0 引出 | `tx=U0TXD -> R5 499R -> ESP32_U0TXD`；`rx=ESP32_U0RXD`；`onboard_bridge=null` |
| 电源 | VIN 输入滤波 | `input=VIN`；`output=VIN_5V`；`filter=L2 100R/3A`；`capacitor=C4 4.7uF/10V` |
| 电源 | U2 HM8089 | `reference=U2`；`input=VIN_5V -> D1 -> VI`；`output=VCC_3V3`；`enable=VI`；`inductor=L3 LQM2MPN2R2NG0L`；`feedback=R8 68K; R9 15K` |
| GPIO 与控制信号 | U3 SK6812 | `reference=U3`；`data=GPIO2`；`power=VCC_3V3`；`data_out=null` |
| GPIO 与控制信号 | EN 与 GPIO9 按键 | `reset=OS1 -> ESP32_EN`；`reset_pullup=R10 10K`；`reset_cap=C21 470nF`；`boot_button=OS2 -> GPIO9`；`boot_pullup=R6 10K` |
| 复位 | GPIO9 下载启动 | `boot_gpio=GPIO9`；`boot_switch=OS2`；`boot_pullup=R6 10K`；`reset_switch=OS1` |
| 射频 | ESP_LNA 天线网络 | `source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series=C1 LQP15MN2N7B02D`；`shunt=L1; C2 GRM1555C1H2R4BA01D` |
| 时钟 | ESP32-C3 主晶振 | `crystal=X1 TXC/8Z40000017`；`series=R7 LQP15MN27NG02D`；`capacitors=C5/C6 GRM1555C1H180JA01D`；`frequency_visible=false` |
| 总线 | 可复用外设总线 | `usb=GPIO18/19`；`uart=UART0 exposed`；`onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`onboard_twai_devices=null` |
| 保护电路 | 输入与 USB 可见保护 | `input_filter=L2`；`input_diode=D1 B5819WS`；`cc_resistors=R1/R3 5.1K`；`usb_data_esd_visible=false`；`vbus_fuse_visible=false` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash，原理图未画独立 Flash，也未标 U1 容量。（证据：图 eafaa3fac84e / 第 1 页 / U1 与完整页）
- `interface.mate-accessories`：产品正文列出 2.54mm 排针、排母与 HY2.0-4P 母座，但当前 Stamp-C3U 核心板原理图未画这些配件的连接器位号、针脚顺序或底板电路。（证据：图 eafaa3fac84e / 第 1 页 / 完整页，无 Mate 配件连接器）
- `review.flash-capacity`：Stamp-C3U 的 Flash 是否固定为 4MB，且是芯片内封装还是未画外置器件？；原因：正文标容量，原理图无 Flash 器件/容量。
- `review.mate-accessories`：Mate 套装排针/排母/HY2.0-4P 的推荐针脚顺序和连接方式是什么？；原因：本地资源只有核心板电路，未包含配件/底板连接器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `eafaa3fac84eb1b3d7575a74e0e222e3b4d255255e1460c27ed9f8baf8a11957` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3u_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_c3u_mate.md`

源文档 SHA-256：`1e9ffdf042991c3b41917d63a81ec18ac01844fb8b3062df5b1ed07ddfbfc691`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
