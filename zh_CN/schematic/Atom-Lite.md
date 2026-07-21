# Atom-Lite 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom-Lite |
| SKU | C008 |
| 产品 ID | `atom-lite-f7be27b3adc3` |
| 源文档 | `zh_CN/core/ATOM Lite.md` |

## 概述

Atom-Lite 的本地单页原理图以标值 PICO_D4 的主控为核心，使用 CH552T 实现 USB Type-C 到 UART/下载控制，SY8089A 将 VBUS_5V 降压为 VCC_3V3。板上包含 SK6812 RGB、GPIO12 红外 LED、GPIO39 用户键、SGM803 复位监控、3D 天线匹配、Grove GPIO32/GPIO26 和多组 2.0mm 引出。USB D+/D- 与按键/复位配置双向 TVS，Grove 5V 经 1N5819 和 6V/1A PTC 保护；主控/USB-UART 位号及量产器件版本需要进一步确认。

## 检索关键词

`Atom-Lite`、`C008`、`PICO_D4`、`ESP32-PICO-D4`、`CH552T`、`SY8089A`、`SGM803`、`SK6812`、`USB Type-C`、`USB_DP`、`USB_DM`、`VBUS_5V`、`VCC_3V3`、`GROVE_5V`、`GPIO27 RGB`、`GPIO39 button`、`GPIO12 IR`、`GPIO32`、`GPIO26`、`GPIO21`、`GPIO25`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO33`、`ESP_TX`、`ESP_RX`、`ESP_EN`、`ESP_GP0`、`E1 ANT`、`1N5819`、`FUSE1 6V/1A/PTC`、`PESD`、`SIP5_2.0`、`SIP4_2.0`、`GROVE`、`reset button`、`3D antenna`、`4MB Flash`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U? (main MCU) | PICO_D4 | 主控与 Wi-Fi/RF 核心，连接 USB-UART、GPIO、RGB、按键、红外、复位和天线 | 图 f79ca42d41a6 / 第 1 页 / 页面中右大型 U? PICO_D4，IO0-IO39、EN、LNA_IN 与电源引脚 |
| U? (USB-UART) | CH552T | USB D+/D- 到 ESP_TX/ESP_RX 串口并控制 ESP_GP0/ESP_EN | 图 f79ca42d41a6 / 第 1 页 / 页面左上 U? CH552T，USB_DP/USB_DM、ESP_RX/ESP_TX/ESP_GP0/ESP_EN |
| U5 | SY8089A | VBUS_5V 到 VCC_3V3 的降压转换器 | 图 f79ca42d41a6 / 第 1 页 / 页面左中 U5 SY8089A、L2、R7/R8 与 VCC_3V3 |
| J1 | TYPEC | USB Type-C 电源与 USB D+/D- 接口 | 图 f79ca42d41a6 / 第 1 页 / 页面左中 J1 TYPEC，VCC/CC1/CC2/GND/SHELL/DP/DN |
| J2 | GROVE | GPIO32、GPIO26、GROVE_5V 与 GND 四针接口 | 图 f79ca42d41a6 / 第 1 页 / 页面左下 J2 GROVE pins1-4 与 ESP_GP32/ESP_GP26/GROVE_5V/GND |
| U1 | SK6812 | GPIO27 控制的板载 RGB LED | 图 f79ca42d41a6 / 第 1 页 / 页面右上 U1 SK6812、ESP_GP27 输入、VBUS_5V/R102 与 6812_DOUT |
| D6,R1 | LED_IR / 22R | GPIO12 驱动的红外发射 LED 与限流电阻 | 图 f79ca42d41a6 / 第 1 页 / 页面中央 D6 LED_IR、R1 22R、ESP GPIO12 与 GND |
| S2 | PTS_820 | GPIO39 用户按键 | 图 f79ca42d41a6 / 第 1 页 / 页面右中 S2 PTS_820、ESP GPIO39、R3 4.7K 与 D1 |
| U3 | SGM803 | VCC_3V3 复位监控器，输出连接 ESP_EN | 图 f79ca42d41a6 / 第 1 页 / 页面中下 U3 SGM803、VCC/RST/GND 与 ESP_EN |
| S1 | T3_0.5 | ESP_EN 到 GND 的复位按钮 | 图 f79ca42d41a6 / 第 1 页 / 页面中下 S1 T3_0.5、ESP_EN 与 GND |
| E1,L1,C2,C3 | ANT / 1.8nH / 1.2pF / 5pF | PICO_D4 LNA_IN 的 2.4G 天线匹配与板载天线 | 图 f79ca42d41a6 / 第 1 页 / 页面右上 PICO_D4 LNA_IN 到 C3/L1/C2/E1 ANT |
| D3,D4 | 3.3V/TVS/BiDir | USB_DP 与 USB_DM 对地双向 TVS 保护 | 图 f79ca42d41a6 / 第 1 页 / 页面左中 J1 USB_DP/USB_DM 旁 D3/D4 3.3V/TVS/BiDir |
| D5,FUSE1 | 1N5819 / 6V/1A/PTC | VBUS_5V 到 GROVE_5V 的串联二极管与自恢复保险丝 | 图 f79ca42d41a6 / 第 1 页 / 页面左下 VBUS_5V-D5 1N5819-FUSE1 6V/1A/PTC-GROVE_5V |
| J3 | SIP4_2.0 | GPIO21、GPIO25、GROVE_5V 与 GND 四针引出 | 图 f79ca42d41a6 / 第 1 页 / 页面左下引出焊盘框 J3 SIP4_2.0 pins1-4 |
| J4 | SIP5_2.0 | VCC_3V3、GPIO22、GPIO19、GPIO23、GPIO33 五针引出 | 图 f79ca42d41a6 / 第 1 页 / 页面左下引出焊盘框 J4 SIP5_2.0 pins1-5 |

## 系统结构

### Atom-Lite 系统架构

PICO_D4 主控连接 CH552T USB-UART、SY8089A 3.3V 电源、SK6812、红外 LED、用户键、SGM803 复位、Grove/焊盘 GPIO 与板载天线。

- 参数与网络：`mcu=U? PICO_D4`；`usb_uart=U? CH552T`；`power=U5 SY8089A`；`rgb=U1 SK6812`；`ir=D6 LED_IR`；`button=S2 PTS_820`；`reset_monitor=U3 SGM803`；`antenna=E1 ANT`
- 证据：图 f79ca42d41a6 / 第 1 页 / 第 1 页完整单页所有功能区

## 电源

### VBUS_5V 到 VCC_3V3

U5 SY8089A 的 IN pin4 与 EN pin1 接 VBUS_5V，SW pin3 经 L2 2.2uH/1.2A/0806 输出 VCC_3V3，FB pin5 使用 R7 100K/1% 与 R8 22.1K/1% 分压。

- 参数与网络：`input=VBUS_5V`；`converter=U5 SY8089A`；`enable=pin1 VBUS_5V`；`inductor=L2 2.2uH/1.2A/0806`；`output=VCC_3V3`；`feedback=R7 100K/1%; R8 22.1K/1%`；`output_cap=C16 22uF/6.3V`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左中 U5/L2/R7/R8/C13/C16

### GROVE_5V 保护路径

VBUS_5V 依次经过 D5 1N5819 和 FUSE1 6V/1A/PTC 形成 GROVE_5V，C14 22uF/6.3V 从 GROVE_5V 接 GND。

- 参数与网络：`input=VBUS_5V`；`diode=D5 1N5819`；`fuse=FUSE1 6V/1A/PTC`；`output=GROVE_5V`；`capacitor=C14 22uF/6.3V`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左下 VBUS_5V/D5/FUSE1/GROVE_5V/C14

## 接口

### J1 USB Type-C

J1 VCC 接 VBUS_5V，DP1/DP2 汇合为 USB_DP，DN1/DN2 汇合为 USB_DM，CC1/CC2 分别经 R4/R5 5.1K 接 GND，GND/SHELL 接地。

- 参数与网络：`vbus=VBUS_5V`；`dp=A6/B6 USB_DP`；`dm=A7/B7 USB_DM`；`cc1=R4 5.1K to GND`；`cc2=R5 5.1K to GND`；`shield=GND`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左中 J1 TYPEC、R4/R5、USB_DP/USB_DM

### J2 Grove 接口

J2 pin4=ESP_GP32、pin3=ESP_GP26、pin2=GROVE_5V、pin1=GND。

- 参数与网络：`pin4=GPIO32`；`pin3=GPIO26`；`pin2=GROVE_5V`；`pin1=GND`；`logic_level=PICO_D4 GPIO domain`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左下 J2 GROVE pins1-4

### J3/J4 引出焊盘

J4 pins1-5 为 VCC_3V3、GPIO22、GPIO19、GPIO23、GPIO33；J3 pins1-4 为 GPIO21、GPIO25、GROVE_5V、GND。

- 参数与网络：`J4=pin1 VCC_3V3,pin2 GPIO22,pin3 GPIO19,pin4 GPIO23,pin5 GPIO33`；`J3=pin1 GPIO21,pin2 GPIO25,pin3 GROVE_5V,pin4 GND`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左下蓝框引出焊盘 J3/J4

## 总线

### CH552T 到 PICO_D4 UART

CH552T 的 ESP_RX 经 R11 100R 连接 PICO_D4 IO3/U0RXD pin40，ESP_TX 经 R12 100R 连接 IO1/U0TXD pin41；USB_DP/DM 连接 CH552T pins14/15。

- 参数与网络：`usb=USB_DP -> CH552T pin14; USB_DM -> pin15`；`uart_rx=CH552T ESP_RX -> R11 100R -> PICO_D4 IO3/U0RXD pin40`；`uart_tx=CH552T ESP_TX -> R12 100R -> PICO_D4 IO1/U0TXD pin41`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左上 CH552T 与中右 PICO_D4 ESP_RX/ESP_TX 网络

## GPIO 与控制信号

### CH552T 下载控制

CH552T 的 ESP_GP0 经 R9 100R 接出，ESP_EN 经 R10 100R 接出；ESP_EN 同名网络连接 PICO_D4 EN pin9 和复位电路。

- 参数与网络：`boot_control=CH552T ESP_GP0 via R9 100R`；`reset_control=CH552T ESP_EN via R10 100R`；`mcu_enable=PICO_D4 EN pin9`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左上 ESP_GP0/ESP_EN 与页面中下 PICO_D4 EN/复位网络

### SK6812 RGB

PICO_D4 IO27 pin16 的 ESP_GP27 连接 U1 SK6812 IN，U1 VCC 经 R102 100R 接 VBUS_5V，GND 接地，OUT 形成 6812_DOUT。

- 参数与网络：`gpio=GPIO27`；`device=U1 SK6812`；`data_in=ESP_GP27`；`supply=VBUS_5V via R102 100R`；`data_out=6812_DOUT`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面右上 PICO_D4 IO27 与 U1 SK6812/R102

### 红外发射

PICO_D4 IO12 pin18 经 R1 22R 和 D6 LED_IR 串联到 GND。

- 参数与网络：`gpio=GPIO12`；`series_resistor=R1 22R`；`emitter=D6 LED_IR`；`return=GND`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面中央 PICO_D4 IO12、R1、D6、GND

### GPIO39 用户按键

PICO_D4 IO39 pin7 连接 S2 PTS_820 按键网络，R3 4.7K 接 VCC_3V3，按键接 GND，并配置 D1 3.3V/TVS/BiDir 对地保护。

- 参数与网络：`gpio=GPIO39`；`switch=S2 PTS_820`；`pullup=R3 4.7K to VCC_3V3`；`active_level=pressed to GND`；`protection=D1 3.3V/TVS/BiDir`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面右中 PICO_D4 IO39、S2/R3/D1

## 复位

### ESP_EN 复位路径

U3 SGM803 由 VCC_3V3 供电，RST 输出连接 ESP_EN；S1 T3_0.5 按下把 ESP_EN 接 GND，ESP_EN 再连接 PICO_D4 EN pin9。

- 参数与网络：`supervisor=U3 SGM803`；`rail=VCC_3V3`；`reset_net=ESP_EN`；`button=S1 T3_0.5 to GND`；`mcu_pin=PICO_D4 EN pin9`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面中下 U3/S1/ESP_EN/PICO_D4 EN

## 保护电路

### USB 数据线 TVS

USB_DP 与 USB_DM 分别通过 D3/D4 3.3V/TVS/BiDir 接 GND。

- 参数与网络：`usb_dp=D3 3.3V/TVS/BiDir to GND`；`usb_dm=D4 3.3V/TVS/BiDir to GND`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面左中 USB_DP/USB_DM 与 D3/D4

## 射频

### 板载天线匹配

PICO_D4 LNA_IN pin2 经 C3 5pF/L1 1.8nH 网络连接 E1 ANT，天线节点另由 C2 1.2pF 接 GND。

- 参数与网络：`mcu_pin=LNA_IN pin2`；`series=L1 1.8nH`；`shunt_input=C3 5pF`；`shunt_antenna=C2 1.2pF`；`antenna=E1 ANT`
- 证据：图 f79ca42d41a6 / 第 1 页 / 页面右上 LNA_IN/C3/L1/C2/E1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom-Lite 系统架构 | `mcu=U? PICO_D4`；`usb_uart=U? CH552T`；`power=U5 SY8089A`；`rgb=U1 SK6812`；`ir=D6 LED_IR`；`button=S2 PTS_820`；`reset_monitor=U3 SGM803`；`antenna=E1 ANT` |
| 电源 | VBUS_5V 到 VCC_3V3 | `input=VBUS_5V`；`converter=U5 SY8089A`；`enable=pin1 VBUS_5V`；`inductor=L2 2.2uH/1.2A/0806`；`output=VCC_3V3`；`feedback=R7 100K/1%; R8 22.1K/1%`；`output_cap=C16 22uF/6.3V` |
| 接口 | J1 USB Type-C | `vbus=VBUS_5V`；`dp=A6/B6 USB_DP`；`dm=A7/B7 USB_DM`；`cc1=R4 5.1K to GND`；`cc2=R5 5.1K to GND`；`shield=GND` |
| 保护电路 | USB 数据线 TVS | `usb_dp=D3 3.3V/TVS/BiDir to GND`；`usb_dm=D4 3.3V/TVS/BiDir to GND` |
| 总线 | CH552T 到 PICO_D4 UART | `usb=USB_DP -> CH552T pin14; USB_DM -> pin15`；`uart_rx=CH552T ESP_RX -> R11 100R -> PICO_D4 IO3/U0RXD pin40`；`uart_tx=CH552T ESP_TX -> R12 100R -> PICO_D4 IO1/U0TXD pin41` |
| GPIO 与控制信号 | CH552T 下载控制 | `boot_control=CH552T ESP_GP0 via R9 100R`；`reset_control=CH552T ESP_EN via R10 100R`；`mcu_enable=PICO_D4 EN pin9` |
| 电源 | GROVE_5V 保护路径 | `input=VBUS_5V`；`diode=D5 1N5819`；`fuse=FUSE1 6V/1A/PTC`；`output=GROVE_5V`；`capacitor=C14 22uF/6.3V` |
| 接口 | J2 Grove 接口 | `pin4=GPIO32`；`pin3=GPIO26`；`pin2=GROVE_5V`；`pin1=GND`；`logic_level=PICO_D4 GPIO domain` |
| 接口 | J3/J4 引出焊盘 | `J4=pin1 VCC_3V3,pin2 GPIO22,pin3 GPIO19,pin4 GPIO23,pin5 GPIO33`；`J3=pin1 GPIO21,pin2 GPIO25,pin3 GROVE_5V,pin4 GND` |
| GPIO 与控制信号 | SK6812 RGB | `gpio=GPIO27`；`device=U1 SK6812`；`data_in=ESP_GP27`；`supply=VBUS_5V via R102 100R`；`data_out=6812_DOUT` |
| GPIO 与控制信号 | 红外发射 | `gpio=GPIO12`；`series_resistor=R1 22R`；`emitter=D6 LED_IR`；`return=GND` |
| GPIO 与控制信号 | GPIO39 用户按键 | `gpio=GPIO39`；`switch=S2 PTS_820`；`pullup=R3 4.7K to VCC_3V3`；`active_level=pressed to GND`；`protection=D1 3.3V/TVS/BiDir` |
| 复位 | ESP_EN 复位路径 | `supervisor=U3 SGM803`；`rail=VCC_3V3`；`reset_net=ESP_EN`；`button=S1 T3_0.5 to GND`；`mcu_pin=PICO_D4 EN pin9` |
| 射频 | 板载天线匹配 | `mcu_pin=LNA_IN pin2`；`series=L1 1.8nH`；`shunt_input=C3 5pF`；`shunt_antenna=C2 1.2pF`；`antenna=E1 ANT` |
| 核心器件 | 主控与 USB-UART 量产标识 | `schematic_mcu=U? PICO_D4`；`documented_mcu=ESP32-PICO-D4`；`schematic_usb_uart=U? CH552T`；`documented_driver_note=FTDI VCP`；`valid_references=false` |
| 内存与 Flash | 4MB SPI Flash | `documented_capacity=4MB`；`external_flash_shown=false`；`schematic_capacity_label=null`；`integration_confirmed=false` |
| 其他事实 | 正文中的处理器、Wi-Fi 与电源性能 | `documented_cpu=dual-core 240MHz`；`documented_sram=520KB`；`documented_wifi=2.4GHz`；`documented_input=5V@500mA`；`schematic_mcu=PICO_D4`；`measured_current=null` |

## 待确认事项

- `component.mcu-usb-uart-identification`：原理图把主控标为 U? PICO_D4、USB-UART 标为 U? CH552T，未给出有效位号；产品正文称 ESP32-PICO-D4，并另有 FTDI VCP 驱动说明，当前量产器件与图纸版本对应关系无法由本页唯一确认。（证据：图 f79ca42d41a6 / 第 1 页 / 页面左上 U? CH552T 与中右 U? PICO_D4）
- `memory.documented-flash`：产品正文写 4MB SPI Flash，当前原理图未画出独立 Flash 器件、SPI Flash 网络或容量标注；是否集成于当前 PICO_D4 量产封装需由器件资料和 BOM 确认。（证据：图 f79ca42d41a6 / 第 1 页 / 第 1 页完整单页及 U? PICO_D4，未见 Flash 器件或容量）
- `other.documented-performance`：正文列出双核 240MHz、520KB SRAM、2.4GHz Wi-Fi 和 5V@500mA；当前连接图未标注频率、内存容量、Wi-Fi 协议能力或整机电流边界。（证据：图 f79ca42d41a6 / 第 1 页 / 第 1 页 PICO_D4、电源和天线电路，图中无性能参数表）
- `review.mcu-usb-uart-identification`：C008 当前量产主控和 USB-UART 是否分别为 ESP32-PICO-D4 与 CH552T，缺失位号对应哪个正式版本图纸？；原因：当前图中两器件均为 U?，且正文 FTDI 驱动说明与 CH552T 标值需要版本/BOM 闭环。
- `review.flash-capacity`：C008 当前 PICO_D4 封装或板级 Flash 的正式容量和料号是否为 4MB？；原因：当前原理图未显示独立 Flash 或容量，需要器件 datasheet/BOM 确认。
- `review.documented-performance`：C008 当前硬件/固件正式确认的 CPU、SRAM、Wi-Fi 和 5V 输入电流规格是什么？；原因：这些参数不在当前连接原理图中，需器件资料和整机测试闭环。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f79ca42d41a64b94ee7900b566434a85c68be7b97eef3a20bde9c05f7802c100` | `https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-2e58eac3-d9ef-4be4-b486-d4dd9a8324fa.webp` |

---

源文档：`zh_CN/core/ATOM Lite.md`

源文档 SHA-256：`fa44326e2b050b752a35b51274fee118cfe88da67c67788ea0bab671c14b02d9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
