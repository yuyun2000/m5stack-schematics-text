# Stamp-C3 Mate 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-C3 Mate |
| SKU | K056 |
| 产品 ID | `stamp-c3-mate-47c961525c5c` |
| 源文档 | `zh_CN/core/stamp_c3_mate.md` |

## 概述

Stamp-C3 Mate 原理图以 U1 ESP32-C3 为主控，连接 PROANT_440 天线、外部晶体、SK6812、GPIO3 用户按键和 CH9102F USB-UART。J1 USB Type-C 提供 USB_D_P/USB_D_N 与 VIN，VIN 经 L3 形成 VIN_5V，再由 U2 SY8003 降压为 VCC_3V3。CH9102F 的握手信号经 VT1/VT2、D1 和电阻网络控制 ESP32_EN/GPIO9，实现复位与下载控制。

## 检索关键词

`Stamp-C3 Mate`、`K056`、`ESP32-C3`、`SY8003`、`CH9102F`、`SK6812`、`PROANT_440`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VIN`、`VIN_5V`、`VCC_3V3`、`VDD_SPI`、`ESP32_EN`、`ESP32_U0RXD`、`ESP32_U0TXD`、`CP_DTR`、`CP_RTS`、`CP_TXD`、`GPIO2 SK6812`、`GPIO3 Button`、`GPIO9 Boot`、`OS1 Reset`、`OS2 Button`、`LQM2MPN2R2NG0L`、`UPZ1608E101-3R0TF`、`LQP15MN2N7B02D`、`TXC/8Z40000017`、`R1 5.1K`、`R3 5.1K`、`R5 68K`、`R6 15K`、`R13 47R`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-C3 | 主控 SoC，连接射频、晶体、UART、GPIO、按键和 RGB LED | 图 873538e7cbc7 / 第 1 页 / 第1页左上：U1 ESP32-C3，pins1-33 |
| U2 | SY8003 | VIN_5V 到 VCC_3V3 的同步降压转换器 | 图 873538e7cbc7 / 第 1 页 / 第1页中央上：U2 SY8003、L2、R5、R6 |
| L2 | LQM2MPN2R2NG0L | U2 LX 开关节点到 VCC_3V3 的降压储能电感 | 图 873538e7cbc7 / 第 1 页 / 第1页中央上：L2 LQM2MPN2R2NG0L |
| U3 | CH9102F | USB 到 UART 桥接及自动下载握手控制 | 图 873538e7cbc7 / 第 1 页 / 第1页中央下：U3 CH9102F |
| U4 | SK6812 | GPIO2 控制的可编程 RGB LED | 图 873538e7cbc7 / 第 1 页 / 第1页右下：U4 SK6812 |
| J1 | USB-TYPEC | USB 数据接口和 VIN 电源输入 | 图 873538e7cbc7 / 第 1 页 / 第1页右上：J1 USB-TYPEC |
| ANT1 | PROANT_440 | 经 C1/L1/C2 匹配网络连接 ESP_LNA 的板载射频天线 | 图 873538e7cbc7 / 第 1 页 / 第1页上部：ANT1 PROANT_440 与 RF matching 网络 |
| X1 | TXC/8Z40000017/立创采购 | 连接 U1 XTAL_P/XTAL_N 的主晶体 | 图 873538e7cbc7 / 第 1 页 / 第1页左中：X1，标注 TXC/8Z40000017/立创采购 |
| OS1 | SMT_SW_PTS_820 | 按下将 ESP32_EN 拉低的复位按键 | 图 873538e7cbc7 / 第 1 页 / 第1页右中：OS1 SMT_SW_PTS_820，ESP32_EN 到 GND |
| OS2 | SMT_SW_PTS_820 | 按下将 GPIO3 拉低的用户按键 | 图 873538e7cbc7 / 第 1 页 / 第1页右中：OS2 SMT_SW_PTS_820，GPIO3 到 GND |
| L3 | Sunlord/UPZ1608E101-3R0TF/100R/3A | VIN 到 VIN_5V 的串联电源滤波器件 | 图 873538e7cbc7 / 第 1 页 / 第1页右上：L3，VIN 到 VIN_5V |
| VT1,VT2 | 未标注 | 由 CP_RTS/CP_DTR 驱动并控制 ESP32_EN/GPIO9 的自动下载晶体管 | 图 873538e7cbc7 / 第 1 页 / 第1页右下中央：VT1/VT2、R9/R10/R11、CP_RTS/CP_DTR |
| D1 | 1N4148 | 自动下载电路中连接 GPIO9 支路的二极管 | 图 873538e7cbc7 / 第 1 页 / 第1页右下中央：D1 1N4148、GPIO9、R12 |

## 系统结构

### Stamp-C3 Mate 架构

U1 ESP32-C3 连接 PROANT_440 天线、外部晶体、U4 SK6812、GPIO3 按键和 U3 CH9102F；J1 提供 USB 与 VIN，U2 SY8003 将 VIN_5V 转换为 VCC_3V3。

- 参数与网络：`soc=U1 ESP32-C3`；`power=U2 SY8003`；`usb_uart=U3 CH9102F`；`rgb=U4 SK6812`；`antenna=ANT1 PROANT_440`；`usb=J1 USB-TYPEC`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页完整单页：U1-U4、J1、ANT1、X1、OS1/OS2

## 电源

### USB VIN 输入与滤波

J1 VCC 连接 VIN；VIN 经 L3 Sunlord/UPZ1608E101-3R0TF/100R/3A 串联形成 VIN_5V，C8 4.7uF/10V 从 VIN_5V 对地。

- 参数与网络：`connector=J1 VCC`；`input=VIN`；`filter=L3 Sunlord/UPZ1608E101-3R0TF/100R/3A`；`output=VIN_5V`；`capacitor=C8 4.7uF/10V`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页右上：J1 VCC/VIN 与 L3/C8/VIN_5V

### VIN_5V 到 VCC_3V3

U2 SY8003 的 IN 和 EN 接 VIN_5V，LX 经 L2 LQM2MPN2R2NG0L 输出 VCC_3V3；FB 由 R5 68KΩ/1% 与 R6 15KΩ/1% 分压，C4、C5 均为 22uF/6.3V。

- 参数与网络：`converter=U2 SY8003`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L2 LQM2MPN2R2NG0L`；`output=VCC_3V3`；`feedback_top=R5 68KΩ/1%`；`feedback_bottom=R6 15KΩ/1%`；`input_caps=C6/C7 4.7uF/10V`；`output_caps=C4/C5 22uF/6.3V`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页中央上：U2 pins1-9、L2、R5/R6、C4-C7

### ESP32-C3 电源域与去耦

U1 VDD3P3、VDD3P4、VDD3P3_CPU、VDD3P3_RTC、VDDA pins2/3/17/11/31/32 接 VCC_3V3；C13-C16 为 4.7uF/10V 去耦，C17-C20/C22 为 470nF/10V 去耦。

- 参数与网络：`rail=VCC_3V3`；`soc_pins=U1 pins2,3,17,11,31,32`；`bulk_caps=C13/C14/C15/C16 4.7uF/10V`；`high_frequency_caps=C17/C18/C19/C20/C22 470nF/10V`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页左部 U1 power pins 与左下 C13-C20/C22 banks

### CH9102F 电源去耦

U3 VIO pin5 由 C12 4.7uF/10V 对地去耦，VDD pin6 由 C11 100nF/25V 对地去耦，RST pin9 由 R8 10KΩ上拉至 VCC_3V3。

- 参数与网络：`vio=U3 pin5 VCC_3V3; C12 4.7uF/10V`；`vdd=U3 pin6 VCC_3V3; C11 100nF/25V`；`reset=U3 RST pin9; R8 10KΩ to VCC_3V3`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页中央下：U3 pins5/6/9、C11/C12、R8

## 接口

### J1 USB Type-C 接口

J1 的 DP1/DP2 并联为 USB_D_P，DN1/DN2 并联为 USB_D_N；CC1、CC2 分别由 R1、R3 5.1KΩ下拉到 GND，VCC 连接 VIN，GND1/GND2 与 SHELL 接地。

- 参数与网络：`connector=J1 USB-TYPEC`；`dp=A6/B6 DP1/DP2 -> USB_D_P`；`dm=A7/B7 DN1/DN2 -> USB_D_N`；`cc1=A5 CC1 -> R1 5.1KΩ -> GND`；`cc2=B5 CC2 -> R3 5.1KΩ -> GND`；`vbus=VCC -> VIN`；`ground=GND1/GND2/SHELL`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页右上：J1、R1、R3、USB_D_P、USB_D_N、VIN

## 总线

### CH9102F USB-UART

J1 USB_D_P/USB_D_N 分别连接 U3 CH9102F D+/D- pins3/4；U3 VBUS 与 REGIN 接 VIN_5V，VIO 与 VDD 接 VCC_3V3。

- 参数与网络：`bridge=U3 CH9102F`；`usb_dp=USB_D_P -> U3 D+ pin3`；`usb_dm=USB_D_N -> U3 D- pin4`；`vbus=U3 VBUS pin8 -> VIN_5V`；`regin=U3 REGIN pin7 -> VIN_5V`；`io_supply=U3 VIO pin5 -> VCC_3V3`；`core_supply=U3 VDD pin6 -> VCC_3V3`；`direction=USB bidirectional; UART TX/RX`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页中央下：U3 pins3-8、USB_D_P/USB_D_N、VIN_5V、VCC_3V3

## GPIO 与控制信号

### GPIO3 用户按键

OS2 SMT_SW_PTS_820 连接 GPIO3 与 GND，按下时将 U1 GPIO3 pin8 拉低。

- 参数与网络：`switch=OS2 SMT_SW_PTS_820`；`gpio=U1 GPIO3 pin8`；`active_level=low`；`connection=GPIO3 -> OS2 -> GND`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页 U1 GPIO3 与右中 OS2/GPIO3

### GPIO2 RGB LED

U1 GPIO2 pin6 连接 U4 SK6812 DIN pin1；U4 VDD pin2 接 VCC_3V3，VSS pin4 接 GND，DOUT pin3 未连接。

- 参数与网络：`controller=U1 GPIO2 pin6`；`data=GPIO2 -> U4 DIN pin1`；`supply=U4 VDD pin2 -> VCC_3V3`；`ground=U4 VSS pin4 -> GND`；`data_out=U4 DOUT pin3 NC`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页 U1 GPIO2 与右下 U4 SK6812 pins1-4

### ESP32-C3 图中 GPIO 网络

U1 右侧依次画出 GPIO0-GPIO10 以及 GPIO18、GPIO19；GPIO8 由 R2 10KΩ上拉至 VCC_3V3，GPIO2 连接 SK6812，GPIO3 连接按键，GPIO9 连接自动下载支路。

- 参数与网络：`general_gpio=GPIO0,GPIO1,GPIO2,GPIO3,GPIO4,GPIO5,GPIO6,GPIO7,GPIO8,GPIO9,GPIO10,GPIO18,GPIO19`；`gpio8_pullup=R2 10KΩ to VCC_3V3`；`gpio2=SK6812 DIN`；`gpio3=OS2 button`；`gpio9=auto-download boot branch`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页左上 U1 GPIO0-GPIO10/GPIO18/GPIO19 与 R2，右侧 GPIO2/GPIO3/GPIO9 peripherals

## 时钟

### 外部主晶体连接

X1 标注 TXC/8Z40000017/立创采购，连接 U1 XTAL_P pin30 与 XTAL_N pin29；XTAL_N 支路串 R7 LQP15MN2N7NG02D，C9、C10 对地并标注 GRM1555C1H180JA01D。

- 参数与网络：`crystal=X1 TXC/8Z40000017/立创采购`；`xtal_p=U1 XTAL_P pin30`；`xtal_n=U1 XTAL_N pin29`；`series=R7 LQP15MN2N7NG02D`；`load_caps=C9/C10 GRM1555C1H180JA01D`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页左中：X1、R7、C9/C10 与 U1 XTAL_P/XTAL_N

## 复位

### 稳压器 PG 与 ESP32_EN

U2 PG pin2 连接 ESP32_EN，ESP32_EN 同时连接 U1 CHIP_EN pin7、OS1、R9 10KΩ上拉和自动下载晶体管网络。

- 参数与网络：`power_good=U2 PG pin2`；`net=ESP32_EN`；`soc_pin=U1 CHIP_EN pin7`；`pullup=R9 10KΩ to VCC_3V3`；`manual_reset=OS1 to GND`；`auto_reset=VT1/VT2 network`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页 U2 PG/ESP32_EN、U1 CHIP_EN 与右中 OS1/R9/VT1

### OS1 手动复位

OS1 SMT_SW_PTS_820 连接 ESP32_EN 与 GND，按下将 ESP32_EN 拉低；ESP32_EN 由 R9 10KΩ上拉至 VCC_3V3。

- 参数与网络：`switch=OS1 SMT_SW_PTS_820`；`net=ESP32_EN`；`active_level=low`；`pullup=R9 10KΩ to VCC_3V3`；`soc_pin=U1 CHIP_EN pin7`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页右中：OS1、ESP32_EN 与 R9

## 关键网络

### GPIO9 启动控制网络

GPIO9 从 U1 pin15 引出并连接自动下载电路；该支路通过 R12 2.2KΩ上拉到 VCC_3V3，并经 D1 1N4148 与 VT2 控制路径相连。

- 参数与网络：`soc_pin=U1 GPIO9 pin15`；`net=GPIO9`；`pullup=R12 2.2KΩ to VCC_3V3`；`diode=D1 1N4148`；`auto_control=VT2 / CP_DTR-CP_RTS network`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页 U1 GPIO9 与右下中央 GPIO9/R12/D1/VT2

## 内存与 Flash

### ESP32-C3 存储连接可见性

U1 VDD_SPI pin18 接 VDD_SPI 并由 C3 4.7uF/10V 去耦；SPIHD、SPIWP、SPICS0、SPICLK、SPID、SPIQ pins19-24 标为未连接，图中未画独立外部 Flash 或 PSRAM。

- 参数与网络：`soc=U1 ESP32-C3`；`flash_supply=VDD_SPI`；`decoupling=C3 4.7uF/10V`；`unused_pins=SPIHD/SPIWP/SPICS0/SPICLK/SPID/SPIQ pins19-24`；`external_flash_shown=false`；`external_psram_shown=false`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页左上：U1 VDD_SPI pin18、pins19-24、C3

## 射频

### PROANT_440 射频路径

U1 LNA_IN pin1 使用 ESP_LNA 网络，经 C1 串联到 ANT1 PROANT_440；ESP_LNA 侧有 L1 对地，天线侧有 C2 对地，图纸注明该网络仍需进一步 RF matching。

- 参数与网络：`soc_pin=U1 LNA_IN pin1`；`net=ESP_LNA`；`series=C1, marked LQP15MN2N7B02D`；`soc_side_shunt=L1`；`antenna_side_shunt=C2, marked GRM1555C1H2R4BA01D`；`antenna=ANT1 PROANT_440`；`schematic_note=TBD, need further RF matching`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页上部：ESP_LNA、L1/C1/C2、ANT1 PROANT_440 及 TBD note

## 调试与烧录

### ESP32-C3 UART0 下载串口

U1 U0RXD pin27 使用 ESP32_U0RXD 网络，U1 U0TXD pin28 使用 ESP32_U0TXD 网络；U3 的 CP_TXD 经 R13 47Ω连接 ESP32_U0RXD，U3 另有 ESP32_U0TXD 网络直接连接。

- 参数与网络：`soc_rx=U1 U0RXD pin27 / ESP32_U0RXD`；`soc_tx=U1 U0TXD pin28 / ESP32_U0TXD`；`bridge_to_rx=CP_TXD -> R13 47Ω -> ESP32_U0RXD`；`bridge_tx_net=U3 ESP32_U0TXD`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页 U1 pins27-28、U3 UART/握手侧与底部 R13

### 自动复位与下载控制

U3 的 CP_RTS 与 CP_DTR 进入 VT1/VT2、R10/R11 网络，控制 ESP32_EN 与 GPIO9 支路；GPIO9 支路含 D1 1N4148 和 R12 2.2KΩ上拉到 VCC_3V3。

- 参数与网络：`handshake=CP_RTS,CP_DTR`；`transistors=VT1,VT2`；`resistors=R10 10KΩ; R11 10KΩ`；`reset_target=ESP32_EN`；`boot_target=GPIO9`；`boot_diode=D1 1N4148`；`boot_pullup=R12 2.2KΩ to VCC_3V3`
- 证据：图 873538e7cbc7 / 第 1 页 / 第1页右下中央：CP_RTS/CP_DTR、VT1/VT2、R10/R11、D1/R12、GPIO9

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-C3 Mate 架构 | `soc=U1 ESP32-C3`；`power=U2 SY8003`；`usb_uart=U3 CH9102F`；`rgb=U4 SK6812`；`antenna=ANT1 PROANT_440`；`usb=J1 USB-TYPEC` |
| 电源 | USB VIN 输入与滤波 | `connector=J1 VCC`；`input=VIN`；`filter=L3 Sunlord/UPZ1608E101-3R0TF/100R/3A`；`output=VIN_5V`；`capacitor=C8 4.7uF/10V` |
| 电源 | VIN_5V 到 VCC_3V3 | `converter=U2 SY8003`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L2 LQM2MPN2R2NG0L`；`output=VCC_3V3`；`feedback_top=R5 68KΩ/1%`；`feedback_bottom=R6 15KΩ/1%`；`input_caps=C6/C7 4.7uF/10V`；`output_caps=C4/C5 22uF/6.3V` |
| 复位 | 稳压器 PG 与 ESP32_EN | `power_good=U2 PG pin2`；`net=ESP32_EN`；`soc_pin=U1 CHIP_EN pin7`；`pullup=R9 10KΩ to VCC_3V3`；`manual_reset=OS1 to GND`；`auto_reset=VT1/VT2 network` |
| 接口 | J1 USB Type-C 接口 | `connector=J1 USB-TYPEC`；`dp=A6/B6 DP1/DP2 -> USB_D_P`；`dm=A7/B7 DN1/DN2 -> USB_D_N`；`cc1=A5 CC1 -> R1 5.1KΩ -> GND`；`cc2=B5 CC2 -> R3 5.1KΩ -> GND`；`vbus=VCC -> VIN`；`ground=GND1/GND2/SHELL` |
| 总线 | CH9102F USB-UART | `bridge=U3 CH9102F`；`usb_dp=USB_D_P -> U3 D+ pin3`；`usb_dm=USB_D_N -> U3 D- pin4`；`vbus=U3 VBUS pin8 -> VIN_5V`；`regin=U3 REGIN pin7 -> VIN_5V`；`io_supply=U3 VIO pin5 -> VCC_3V3`；`core_supply=U3 VDD pin6 -> VCC_3V3`；`direction=USB bidirectional; UART TX/RX` |
| 调试与烧录 | ESP32-C3 UART0 下载串口 | `soc_rx=U1 U0RXD pin27 / ESP32_U0RXD`；`soc_tx=U1 U0TXD pin28 / ESP32_U0TXD`；`bridge_to_rx=CP_TXD -> R13 47Ω -> ESP32_U0RXD`；`bridge_tx_net=U3 ESP32_U0TXD` |
| 调试与烧录 | 自动复位与下载控制 | `handshake=CP_RTS,CP_DTR`；`transistors=VT1,VT2`；`resistors=R10 10KΩ; R11 10KΩ`；`reset_target=ESP32_EN`；`boot_target=GPIO9`；`boot_diode=D1 1N4148`；`boot_pullup=R12 2.2KΩ to VCC_3V3` |
| 复位 | OS1 手动复位 | `switch=OS1 SMT_SW_PTS_820`；`net=ESP32_EN`；`active_level=low`；`pullup=R9 10KΩ to VCC_3V3`；`soc_pin=U1 CHIP_EN pin7` |
| GPIO 与控制信号 | GPIO3 用户按键 | `switch=OS2 SMT_SW_PTS_820`；`gpio=U1 GPIO3 pin8`；`active_level=low`；`connection=GPIO3 -> OS2 -> GND` |
| GPIO 与控制信号 | GPIO2 RGB LED | `controller=U1 GPIO2 pin6`；`data=GPIO2 -> U4 DIN pin1`；`supply=U4 VDD pin2 -> VCC_3V3`；`ground=U4 VSS pin4 -> GND`；`data_out=U4 DOUT pin3 NC` |
| GPIO 与控制信号 | ESP32-C3 图中 GPIO 网络 | `general_gpio=GPIO0,GPIO1,GPIO2,GPIO3,GPIO4,GPIO5,GPIO6,GPIO7,GPIO8,GPIO9,GPIO10,GPIO18,GPIO19`；`gpio8_pullup=R2 10KΩ to VCC_3V3`；`gpio2=SK6812 DIN`；`gpio3=OS2 button`；`gpio9=auto-download boot branch` |
| 射频 | PROANT_440 射频路径 | `soc_pin=U1 LNA_IN pin1`；`net=ESP_LNA`；`series=C1, marked LQP15MN2N7B02D`；`soc_side_shunt=L1`；`antenna_side_shunt=C2, marked GRM1555C1H2R4BA01D`；`antenna=ANT1 PROANT_440`；`schematic_note=TBD, need further RF matching` |
| 时钟 | 外部主晶体连接 | `crystal=X1 TXC/8Z40000017/立创采购`；`xtal_p=U1 XTAL_P pin30`；`xtal_n=U1 XTAL_N pin29`；`series=R7 LQP15MN2N7NG02D`；`load_caps=C9/C10 GRM1555C1H180JA01D` |
| 时钟 | X1 晶体频率 | `reference=X1`；`part_number=TXC/8Z40000017`；`explicit_frequency_shown=false` |
| 内存与 Flash | ESP32-C3 存储连接可见性 | `soc=U1 ESP32-C3`；`flash_supply=VDD_SPI`；`decoupling=C3 4.7uF/10V`；`unused_pins=SPIHD/SPIWP/SPICS0/SPICLK/SPID/SPIQ pins19-24`；`external_flash_shown=false`；`external_psram_shown=false` |
| 内存与 Flash | Flash 容量 | `documented_capacity=4MB`；`schematic_part_number=ESP32-C3`；`explicit_capacity_field_on_schematic=false`；`full_ordering_code_shown=false` |
| 电源 | ESP32-C3 电源域与去耦 | `rail=VCC_3V3`；`soc_pins=U1 pins2,3,17,11,31,32`；`bulk_caps=C13/C14/C15/C16 4.7uF/10V`；`high_frequency_caps=C17/C18/C19/C20/C22 470nF/10V` |
| 电源 | CH9102F 电源去耦 | `vio=U3 pin5 VCC_3V3; C12 4.7uF/10V`；`vdd=U3 pin6 VCC_3V3; C11 100nF/25V`；`reset=U3 RST pin9; R8 10KΩ to VCC_3V3` |
| 关键网络 | GPIO9 启动控制网络 | `soc_pin=U1 GPIO9 pin15`；`net=GPIO9`；`pullup=R12 2.2KΩ to VCC_3V3`；`diode=D1 1N4148`；`auto_control=VT2 / CP_DTR-CP_RTS network` |

## 待确认事项

- `clock.external-crystal-frequency`：原理图打印 X1 采购料号 TXC/8Z40000017，但没有独立打印晶体频率数值。（证据：图 873538e7cbc7 / 第 1 页 / 第1页左中：X1 TXC/8Z40000017 标注）
- `memory.flash-capacity`：产品正文标称 4MB Flash；原理图仅标 U1 为 ESP32-C3 并显示 VDD_SPI，未打印具体 Flash 容量或完整芯片订货型号。（证据：图 873538e7cbc7 / 第 1 页 / 第1页左上：U1 ESP32-C3、VDD_SPI 与未连接 SPI memory pins）
- `review.crystal-frequency`：X1 TXC/8Z40000017 的标称晶体频率是多少？；原因：原理图显示采购料号与 XTAL_P/XTAL_N 连接，但未独立打印频率数值。
- `review.flash-capacity`：K056 当前 U1 的集成 Flash 容量是否固定为 4MB？；原因：4MB 来自产品正文；原理图只标 ESP32-C3 和 VDD_SPI，未打印容量或完整订货型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `873538e7cbc79bb65b630146e6d4ee81384269df9f2005cd0267017a96a9c982` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3/stamp_c3_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_c3_mate.md`

源文档 SHA-256：`3929177ee9262d1f2880b629b1e1879f281886011805edca52be22b969e03d1d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
