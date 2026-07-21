# Stamp-C3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-C3 |
| SKU | C056-B |
| 产品 ID | `stamp-c3-ba12ba083e85` |
| 源文档 | `zh_CN/core/stamp_c3.md` |

## 概述

Stamp-C3 以 U1 ESP32-C3 为主控，外接 U3 CH9102F USB-UART，VT1/VT2 自动下载网络控制 ESP32_EN 与 GPIO9。J1 USB Type-C 提供 VIN 和 USB D+/D-，U2 SY8003 将 VIN_5V 转为 VCC_3V3 并以 PG 驱动 ESP32_EN。板载 U4 SK6812 接 GPIO2，OS1/OS2 分别为 EN 复位与 GPIO3 用户按键，ANT1 PROANT_440 通过预留 RF 匹配网络连接 ESP_LNA。

## 检索关键词

`Stamp-C3`、`C056-B`、`ESP32-C3`、`CH9102F`、`SY8003`、`SK6812`、`PROANT_440`、`USB Type-C`、`VIN`、`VIN_5V`、`VCC_3V3`、`ESP32_EN`、`GPIO2 RGB`、`GPIO3 Button`、`GPIO9 BOOT`、`CP_DTR`、`CP_RTS`、`CP_TXD`、`ESP32_U0RXD`、`ESP32_U0TXD`、`USB_D_P`、`USB_D_N`、`GPIO0`、`GPIO1`、`GPIO4`、`GPIO5`、`GPIO6`、`GPIO7`、`GPIO8`、`GPIO10`、`GPIO18`、`GPIO19`、`2.54mm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-C3 | RISC-V 主控，提供 GPIO0-10/18/19、UART、RF 与启动控制 | 图 873538e7cbc7 / 第 1 页 / 左上 U1 ESP32-C3 |
| U2 | SY8003 | VIN_5V 至 VCC_3V3 降压转换器，PG 输出 ESP32_EN | 图 873538e7cbc7 / 第 1 页 / 中央上 U2 SY8003 |
| U3 | CH9102F | USB-UART 桥，连接 USB D+/D-、ESP32 UART0 与 DTR/RTS 自动下载 | 图 873538e7cbc7 / 第 1 页 / 中央下 U3 CH9102F |
| U4 | SK6812 | GPIO2 控制的可编程 RGB LED | 图 873538e7cbc7 / 第 1 页 / 右下 U4 SK6812 |
| J1 | USB-TYPEC | USB Type-C 电源和 USB 2.0 数据接口 | 图 873538e7cbc7 / 第 1 页 / 右上 J1 USB-TYPEC |
| ANT1 | PROANT_440 | ESP32-C3 射频天线与 TBD 匹配网络 | 图 873538e7cbc7 / 第 1 页 / 上中 ANT1 PROANT_440、L1/C1/C2 |
| X1 | TXC/8Z40000017 | ESP32-C3 外部主晶振 | 图 873538e7cbc7 / 第 1 页 / 左中 X1 TXC/8Z40000017 |
| OS1/OS2 | SMT_SW_PTS_820 | ESP32_EN 复位按键与 GPIO3 用户按键 | 图 873538e7cbc7 / 第 1 页 / 右中 OS1/OS2 |
| VT1/VT2 | 未标注 | CH9102F DTR/RTS 至 ESP32_EN/GPIO9 的自动下载晶体管网络 | 图 873538e7cbc7 / 第 1 页 / 右下 VT1/VT2、D1、R9-R12 |
| L3 | Sunlord/UPZ1608SE101-3R0TF/100R/3A | VIN 至 VIN_5V 的输入滤波磁珠 | 图 873538e7cbc7 / 第 1 页 / 右上 VIN/L3/VIN_5V |

## 系统结构

### Stamp-C3 架构

ESP32-C3 连接 CH9102F USB-UART、SK6812、EN/GPIO3 按键与 PROANT_440；SY8003 从 VIN_5V 生成 VCC_3V3。

- 参数与网络：`mcu=U1 ESP32-C3`；`usb_uart=U3 CH9102F`；`dcdc=U2 SY8003`；`rgb=U4 SK6812`；`antenna=ANT1 PROANT_440`
- 证据：图 873538e7cbc7 / 第 1 页 / 完整原理图页

## 核心器件

### U1 ESP32-C3

U1 明确标 ESP32-C3，GPIO0-10、GPIO18/19、UART0、XTAL_P/N、ESP_LNA 与 CHIP_EN 在图中连接。

- 参数与网络：`reference=U1`；`part_number=ESP32-C3`；`power=VCC_3V3`；`enable=ESP32_EN`；`uart=ESP32_U0RXD/ESP32_U0TXD`；`rf=ESP_LNA`
- 证据：图 873538e7cbc7 / 第 1 页 / 左上 U1

## 电源

### VIN 输入

VIN 经 L3 Sunlord/UPZ1608SE101-3R0TF/100R/3A 滤波形成 VIN_5V，C8 4.7uF/10V 对地。

- 参数与网络：`input=VIN`；`output=VIN_5V`；`filter=L3 100R/3A`；`capacitor=C8 4.7uF/10V`
- 证据：图 873538e7cbc7 / 第 1 页 / 右上 VIN/L3/C8

### U2 SY8003

U2 SY8003 以 VIN_5V 为输入，经 L2 LQM2MPN2R2NG0L 生成 VCC_3V3，反馈 R5 68K/R6 15K，PG 输出 ESP32_EN。

- 参数与网络：`reference=U2`；`input=VIN_5V`；`output=VCC_3V3`；`inductor=L2 LQM2MPN2R2NG0L`；`feedback=R5 68K; R6 15K`；`power_good=ESP32_EN`
- 证据：图 873538e7cbc7 / 第 1 页 / 中央上 U2 SY8003

## 接口

### J1 USB Type-C

J1 VCC 接 VIN，A6/B6 汇入 USB_D_P，A7/B7 汇入 USB_D_N，CC1/CC2 经 R1/R3 5.1K 接地。

- 参数与网络：`reference=J1`；`power=VIN`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R3 5.1K to GND`
- 证据：图 873538e7cbc7 / 第 1 页 / 右上 J1 USB-TYPEC

## 总线

### 外设总线复用

原理图只引出通用 GPIO 与 UART0，不在板上连接 I2C、SPI、I2S 或 TWAI 外设；这些控制器由 ESP32-C3 GPIO 复用。

- 参数与网络：`onboard_uart=UART0 to CH9102F`；`onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`onboard_twai_devices=null`
- 证据：图 873538e7cbc7 / 第 1 页 / 完整页，总线连接范围

## GPIO 与控制信号

### 13 路 GPIO 电气引出

U1 图中可见 GPIO0-10、GPIO18 与 GPIO19，共 13 路；GPIO2 接 SK6812，GPIO3 接用户按键，GPIO9 参与自动下载。

- 参数与网络：`gpios=GPIO0-GPIO10; GPIO18; GPIO19`；`count=13`；`rgb=GPIO2`；`button=GPIO3`；`boot=GPIO9`
- 证据：图 873538e7cbc7 / 第 1 页 / U1 GPIO 列与右侧 U4/OS2/自动下载

### U4 SK6812

U4 SK6812 DIN 接 GPIO2，VDD 接 VCC_3V3，VSS 接 GND，DOUT 未连接。

- 参数与网络：`reference=U4`；`part_number=SK6812`；`data=GPIO2`；`power=VCC_3V3`；`data_out=null`
- 证据：图 873538e7cbc7 / 第 1 页 / 右下 U4 SK6812

### 复位与用户按键

OS1 按下将 ESP32_EN 接地，OS2 按下将 GPIO3 接地。

- 参数与网络：`reset_button=OS1 -> ESP32_EN`；`user_button=OS2 -> GPIO3`；`part=SMT_SW_PTS_820`
- 证据：图 873538e7cbc7 / 第 1 页 / 右中 OS1/OS2

## 时钟

### ESP32-C3 晶振

U1 XTAL_P/XTAL_N 连接 X1 TXC/8Z40000017，R7/LQP15MN27NG02D 串联于 XTAL_N，C9/C10 接地；图中未直接写频率。

- 参数与网络：`crystal=X1 TXC/8Z40000017`；`nets=XTAL_P/XTAL_N`；`series=R7 LQP15MN27NG02D`；`capacitors=C9/C10 GRM1555C1H180JA01D`；`frequency_visible=false`
- 证据：图 873538e7cbc7 / 第 1 页 / 左中 X1 区

## 复位

### 自动下载与复位

CP_RTS/CP_DTR 经 VT1/VT2 与 R9-R11 控制 ESP32_EN/GPIO9，D1 1N4148 与 R12 2.2K 连接 GPIO9 启动节点；OS1 可将 ESP32_EN 拉低。

- 参数与网络：`reset=ESP32_EN`；`boot=GPIO9`；`sources=CP_RTS/CP_DTR`；`transistors=VT1/VT2`；`diode=D1 1N4148`；`boot_pullup=R12 2.2K`；`manual_reset=OS1`
- 证据：图 873538e7cbc7 / 第 1 页 / 右中/右下 ESP32_EN、VT1/VT2、GPIO9

## 保护电路

### 可见保护/滤波

原理图显示 VIN 输入磁珠 L3 和 USB CC 下拉，但未画 USB D+/D- 专用 ESD 阵列或 VBUS 自恢复保险丝。

- 参数与网络：`input_filter=L3 100R/3A`；`cc_resistors=R1/R3 5.1K`；`usb_data_esd_visible=false`；`vbus_fuse_visible=false`
- 证据：图 873538e7cbc7 / 第 1 页 / J1 USB 与 VIN 输入区

## 射频

### ESP_LNA 天线网络

ESP_LNA 经 L1/C1/C2 预留匹配网络连接 ANT1 PROANT_440，图中注释 TBD, need further RF matching。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series=C1 LQP15MN2N7B02D`；`shunt=L1; C2 GRM1555C1H2R4BA01D`；`note=TBD, need further RF matching`
- 证据：图 873538e7cbc7 / 第 1 页 / 上中 RF 区

## 调试与烧录

### CH9102F USB-UART

U3 CH9102F D+/D- 接 USB_D_P/N，TXD 网络 CP_TXD 经 R13 47R 接 ESP32_U0RXD，RXD 接 ESP32_U0TXD，DTR/RTS 接自动下载电路。

- 参数与网络：`bridge=U3 CH9102F`；`usb=USB_D_P/USB_D_N`；`tx=CP_TXD -> R13 47R -> ESP32_U0RXD`；`rx=RXD -> ESP32_U0TXD`；`control=CP_DTR/CP_RTS`
- 证据：图 873538e7cbc7 / 第 1 页 / 中央下 U3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-C3 架构 | `mcu=U1 ESP32-C3`；`usb_uart=U3 CH9102F`；`dcdc=U2 SY8003`；`rgb=U4 SK6812`；`antenna=ANT1 PROANT_440` |
| 核心器件 | U1 ESP32-C3 | `reference=U1`；`part_number=ESP32-C3`；`power=VCC_3V3`；`enable=ESP32_EN`；`uart=ESP32_U0RXD/ESP32_U0TXD`；`rf=ESP_LNA` |
| 内存与 Flash | ESP32-C3 Flash | `documented_capacity=4MB`；`discrete_flash=null`；`schematic_capacity_label=null` |
| GPIO 与控制信号 | 13 路 GPIO 电气引出 | `gpios=GPIO0-GPIO10; GPIO18; GPIO19`；`count=13`；`rgb=GPIO2`；`button=GPIO3`；`boot=GPIO9` |
| 接口 | 2.54mm GPIO 接口 | `documented_pitch=2.54mm`；`documented_gpio_count=13`；`connector_reference=null`；`pins_visible=false` |
| 射频 | ESP_LNA 天线网络 | `source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`series=C1 LQP15MN2N7B02D`；`shunt=L1; C2 GRM1555C1H2R4BA01D`；`note=TBD, need further RF matching` |
| 时钟 | ESP32-C3 晶振 | `crystal=X1 TXC/8Z40000017`；`nets=XTAL_P/XTAL_N`；`series=R7 LQP15MN27NG02D`；`capacitors=C9/C10 GRM1555C1H180JA01D`；`frequency_visible=false` |
| 电源 | VIN 输入 | `input=VIN`；`output=VIN_5V`；`filter=L3 100R/3A`；`capacitor=C8 4.7uF/10V` |
| 电源 | U2 SY8003 | `reference=U2`；`input=VIN_5V`；`output=VCC_3V3`；`inductor=L2 LQM2MPN2R2NG0L`；`feedback=R5 68K; R6 15K`；`power_good=ESP32_EN` |
| 接口 | J1 USB Type-C | `reference=J1`；`power=VIN`；`dp=A6/B6 USB_D_P`；`dm=A7/B7 USB_D_N`；`cc=R1/R3 5.1K to GND` |
| 调试与烧录 | CH9102F USB-UART | `bridge=U3 CH9102F`；`usb=USB_D_P/USB_D_N`；`tx=CP_TXD -> R13 47R -> ESP32_U0RXD`；`rx=RXD -> ESP32_U0TXD`；`control=CP_DTR/CP_RTS` |
| 复位 | 自动下载与复位 | `reset=ESP32_EN`；`boot=GPIO9`；`sources=CP_RTS/CP_DTR`；`transistors=VT1/VT2`；`diode=D1 1N4148`；`boot_pullup=R12 2.2K`；`manual_reset=OS1` |
| GPIO 与控制信号 | U4 SK6812 | `reference=U4`；`part_number=SK6812`；`data=GPIO2`；`power=VCC_3V3`；`data_out=null` |
| GPIO 与控制信号 | 复位与用户按键 | `reset_button=OS1 -> ESP32_EN`；`user_button=OS2 -> GPIO3`；`part=SMT_SW_PTS_820` |
| 总线 | 外设总线复用 | `onboard_uart=UART0 to CH9102F`；`onboard_i2c_devices=null`；`onboard_spi_devices=null`；`onboard_i2s_devices=null`；`onboard_twai_devices=null` |
| 保护电路 | 可见保护/滤波 | `input_filter=L3 100R/3A`；`cc_resistors=R1/R3 5.1K`；`usb_data_esd_visible=false`；`vbus_fuse_visible=false` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash，原理图未画独立 Flash，也未在 U1 上标容量。（证据：图 873538e7cbc7 / 第 1 页 / U1 与完整页，无 Flash）
- `interface.gpio-connector`：产品正文称 13 路 GPIO 使用 2.54mm 接口，但当前原理图未画对应连接器位号或针脚编号。（证据：图 873538e7cbc7 / 第 1 页 / 完整页，无 GPIO 连接器）
- `review.flash-capacity`：Stamp-C3 当前 BOM 的 Flash 是否固定为 4MB，且是芯片内封装还是未画出的外置器件？；原因：产品正文标 4MB，原理图无容量和独立 Flash。
- `review.gpio-connector`：13 路 GPIO 的 2.54mm 接口位号和针脚顺序是什么？；原因：产品正文给出间距，原理图未画连接器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `873538e7cbc79bb65b630146e6d4ee81384269df9f2005cd0267017a96a9c982` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3/stamp_c3_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_c3.md`

源文档 SHA-256：`dcc29bb0f2bb2c06b01747f907ea089f5734c203fcbd180543296303dab36a1a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
