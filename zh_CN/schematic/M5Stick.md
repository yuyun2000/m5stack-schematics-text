# M5Stick 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5Stick |
| SKU | K016 |
| 产品 ID | `m5stick-ccff3e07ed3c` |
| 源文档 | `zh_CN/core/m5stick.md` |

## 概述

M5Stick 以 U1 ESP32-WROOM32 为主控，SPI 驱动 U2 OLED，并控制蓝色 LED、红外发射 LED、S8050 蜂鸣器驱动和用户按键；灰色版本相关页还画出 U8 MPU9250 I2C IMU。U3 IP5306 负责 USB/电池充放电并在原理图中明确标注 I2C 地址 0x75，U4 MP1541 生成 OLED VCC_9V，U5 SY8089 生成 VCC_3V3。U6 CP2104 提供 USB-UART 与自动下载复位，但当前 USB-UART 页画出 Micro-USB，与产品正文的 Type-C 描述存在版本差异。

## 检索关键词

`M5Stick`、`K016`、`ESP32-WROOM32`、`IP5306`、`0x75`、`MP1541`、`SY8089`、`CP2104`、`MPU9250`、`ZJY-6428TSWOG01`、`DET402-G-1`、`VCC_3V3`、`VCC_5V`、`VCC_9V`、`VIN_USB`、`VBAT`、`GPIO14 OLED_CS`、`GPIO27 OLED_DC`、`GPIO33 OLED_RST`、`GPIO18 OLED_D0`、`GPIO23 OLED_D1`、`GPIO21 SDA`、`GPIO22 SCL`、`GPIO19 BLUE_LED`、`GPIO17 IR_LED`、`GPIO26 BUZZER`、`GPIO35 BUTTON`、`USB_Micro`、`USB Type-C`、`TXD0`、`RXD0`、`PWR_KEY`、`Grove`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-WROOM32 | 主控模块，连接 OLED、IMU、LED、IR、蜂鸣器、按键与 USB-UART | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 A1-B2，U1 ESP32-WROOM32 |
| U2 | ZJY-6428TSWOG01 | SPI OLED 显示模组，使用 VCC_9V 与 VCC_3V3 | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 C1-C2，U2 ZJY-6428TSWOG01 |
| U8 | MPU9250 | I2C 九轴 IMU，SCL/SDA 接 GPIO21/GPIO22，AD0 接地 | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 C3-D3，U8 MPU9250 |
| LED1 | BLUE_LED | GPIO19 控制的蓝色状态 LED | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 A3-B3，LED1 BLUE_LED |
| LED2 | IR_LED | GPIO17 控制的红外发射 LED | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 B3，LED2 IR_LED |
| LS1/VT3 | DET402-G-1/NPN-S8050 | GPIO26 控制的有源蜂鸣器与低边驱动管 | 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 A4，LS1 DET402-G-1、VT3 S8050 |
| U3 | IP5306 | USB 输入、电池充电与 5V 升压电源管理，定制 I2C 地址 0x75 | 图 f9d2de52c30a / 第 1 页 / Power 页 A1-A2，U3 IP5306 与页下注释 |
| U4 | MP1541 | 从 VCC_5V 生成 OLED VCC_9V 的升压转换器 | 图 f9d2de52c30a / 第 1 页 / Power 页 A3-A4，U4 MP1541 |
| U5 | SY8089 | 从 VCC_5V 生成 VCC_3V3 的降压转换器 | 图 f9d2de52c30a / 第 1 页 / Power 页 B1-B2，U5 SY8089 |
| U6 | CP2104 | USB-UART 桥，连接 ESP32 UART0 并提供 DTR/RTS 自动下载控制 | 图 29eddc8e6351 / 第 1 页 / UsbUART 页 A2-B3，U6 CP2104 |
| U7 | USB_Micro | USB 5V 输入与数据连接器 | 图 29eddc8e6351 / 第 1 页 / UsbUART 页 C2-C3，U7 USB_Micro |
| VT1/VT2 | NPN-S8050 | CP2104 DTR/RTS 至 EN/GPIO0 的自动下载晶体管网络 | 图 29eddc8e6351 / 第 1 页 / UsbUART 页 A1-B1，VT1/VT2 NPN-S8050 |
| S1 | SMT_SW_TS_015 | ESP32 EN 手动复位按键 | 图 29eddc8e6351 / 第 1 页 / UsbUART 页 C1，S1 接 EN/GND |
| S2 | SMT_SW_TS_015 | 用户按键；图中标题 GPIO35，但网络文字显示 GPIO25 | 图 29eddc8e6351 / 第 1 页 / UsbUART 页 D1，GPIO35 标题、GPIO25 网络与 S2 |

## 系统结构

### M5Stick 系统架构

ESP32-WROOM32 连接 SPI OLED、MPU9250、LED/IR/蜂鸣器和按键；IP5306 管理 USB/电池与 5V，MP1541/SY8089 生成 9V/3.3V，CP2104 提供下载串口。

- 参数与网络：`mcu=U1 ESP32-WROOM32`；`display=U2 ZJY-6428TSWOG01`；`imu=U8 MPU9250`；`pmu=U3 IP5306`；`usb_uart=U6 CP2104`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 完整页; 图 f9d2de52c30a / 第 1 页 / Power 完整页; 图 29eddc8e6351 / 第 1 页 / UsbUART 完整页

## 核心器件

### U1 ESP32-WROOM32

U1 明确标为 ESP32-WROOM32，EN、GPIO0/2/4/5/12-19/21-23/25-27/32-36/39 与 UART0 在页内引出。

- 参数与网络：`reference=U1`；`part_number=ESP32-WROOM32`；`power=VCC_3V3`；`reset=EN`；`uart=TXD0/RXD0`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U1 ESP32-WROOM32

## 电源

### OLED 供电

U2 OLED VPP 接 VCC_9V、VDD 接 VCC_3V3，VCOMH 以 C5 2.2uF/16V 去耦，IREF 通过 R2 560K 接地。

- 参数与网络：`vpp=VCC_9V`；`vdd=VCC_3V3`；`vcomh=C5 2.2uF/16V`；`iref=R2 560K to GND`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 C1 U2 电源引脚

### U3 IP5306 充放电

U3 IP5306 的 VIN 接 VIN_USB、VOUT 输出 VCC_5V、BAT 接 VBAT、SW 接 L1，KEY 接 PWR_KEY；原理图说明该器件为定制 I2C 版本。

- 参数与网络：`reference=U3`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`switch_node=SW -> L1`；`key=PWR_KEY`；`interface=custom IIC`
- 证据：图 f9d2de52c30a / 第 1 页 / Power 页 A1-A2 U3 IP5306

### VCC_9V 升压

U4 MP1541 以 VCC_5V 为输入，经 L1 10uH 与 D1 1N5819 生成 VCC_9V，反馈电阻为 R4 73.2K/R6 11.8K。

- 参数与网络：`reference=U4`；`input=VCC_5V`；`output=VCC_9V`；`inductor=L1 10uH`；`diode=D1 1N5819`；`feedback=R4 73.2K; R6 11.8K`
- 证据：图 f9d2de52c30a / 第 1 页 / Power 页 A3-A4 U4 MP1541

### VCC_3V3 降压

U5 SY8089 以 VCC_5V 为输入，经 L2 2.2uH 生成 VCC_3V3，反馈为 R7 267K/R8 59K。

- 参数与网络：`reference=U5`；`input=VCC_5V`；`output=VCC_3V3`；`inductor=L2 2.2uH`；`feedback=R7 267K; R8 59K`
- 证据：图 f9d2de52c30a / 第 1 页 / Power 页 B1-B2 U5 SY8089

## 接口

### U7 Micro-USB

U7 VCC 接 VIN_USB，D-/D+ 经 R16/R17 22Ω 接 USB_DN/USB_DP，并由 D2-D5 RLSD52A031V 对电源/数据提供钳位。

- 参数与网络：`reference=U7`；`power=VIN_USB`；`dm=D- -> R16 22R -> USB_DN`；`dp=D+ -> R17 22R -> USB_DP`；`protection=D2-D5 RLSD52A031V`
- 证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 C2-C3 U7/D2-D5

## 总线

### OLED SPI

U2 OLED 的 CS/RES/DC/D0/D1 分别连接 GPIO14/GPIO33/GPIO27/GPIO18/GPIO23，数据路径为单向时钟/数据接口。

- 参数与网络：`device=U2 ZJY-6428TSWOG01`；`cs=GPIO14`；`reset=GPIO33`；`dc=GPIO27`；`sck=GPIO18 / D0`；`mosi=GPIO23 / D1`；`miso=null`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 C1-C2 U2 OLED

### MPU9250 I2C

ESP32 GPIO21/GPIO22 作为 MPU9250 SCL/SDA；AD0 接地，但原理图未标数值 I2C 地址。

- 参数与网络：`controller=U1 ESP32-WROOM32`；`device=U8 MPU9250`；`scl=GPIO21`；`sda=GPIO22`；`address_strap=AD0=GND`；`address_visible=false`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U8 SCL/SDA/AD0

## 总线地址

### IP5306 I2C 地址

Power 页注释明确写明定制 IP5306 通过 IIC 与 ESP32 通信，IIC address is 0x75。

- 参数与网络：`device=U3 IP5306`；`bus=IIC`；`address=0x75`
- 证据：图 f9d2de52c30a / 第 1 页 / Power 页 C1-C2 Note: IIC address is 0x75

## GPIO 与控制信号

### LED、IR 与蜂鸣器 GPIO

GPIO19 经 R19 330Ω 驱动 BLUE_LED，GPIO17 经 R20 330Ω 驱动 IR_LED；GPIO26 经 R21 330Ω 驱动 VT3 S8050，低边控制 LS1 蜂鸣器。

- 参数与网络：`blue_led=GPIO19 -> R19 330R -> LED1`；`ir_led=GPIO17 -> R20 330R -> LED2`；`buzzer=GPIO26 -> R21 330R -> VT3 S8050 -> LS1`；`buzzer_supply=VCC_3V3`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 A3-B4 LED/IR/LS1 区

## 复位

### 自动下载与复位

CP2104 DTR/RTS 经 R13/R14 10K 与 VT1/VT2 S8050 控制 EN/GPIO0；S1 手动将 EN 拉低，R15 10K 上拉 EN，C20 2.2uF 对地。

- 参数与网络：`reset=EN`；`boot=GPIO0`；`sources=DTR/RTS`；`transistors=VT1/VT2 S8050`；`manual_reset=S1`；`pullup=R15 10K`；`capacitor=C20 2.2uF`
- 证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 A1-B1 自动下载与 C1 S1

## 保护电路

### USB 钳位保护

U7 USB_Micro 的 VIN_USB、USB_DN、USB_DP 分别由 D2-D5 RLSD52A031V 对地钳位，数据线上另串联 R16/R17 22Ω。

- 参数与网络：`devices=D2-D5 RLSD52A031V`；`protected_nets=VIN_USB; USB_DN; USB_DP`；`series_resistors=R16/R17 22R`
- 证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 C2-C3 USB 保护区

## 传感器

### U8 MPU9250

U8 MPU9250 的 SCL/SCLK 接 GPIO21、SDA/SDI 接 GPIO22，AD0/SDO 接 GND，nCS 接 VCC_3V3；INT 未连接。

- 参数与网络：`reference=U8`；`part_number=MPU9250`；`scl=GPIO21`；`sda=GPIO22`；`ad0=GND`；`chip_select=VCC_3V3`；`interrupt=null`
- 证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 C3-D3 U8 MPU9250

## 调试与烧录

### CP2104 USB-UART

U6 CP2104 的 DP/DM 接 USB_DP/USB_DN；TXD 经 R11 470Ω 接 ESP32 RXD0，RXD 接 ESP32 TXD0，DTR/RTS 接自动下载网络。

- 参数与网络：`bridge=U6 CP2104`；`usb=USB_DP/USB_DN`；`bridge_txd=TXD -> R11 470R -> RXD0`；`bridge_rxd=RXD <- TXD0`；`control=DTR/RTS`
- 证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 U6 CP2104

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M5Stick 系统架构 | `mcu=U1 ESP32-WROOM32`；`display=U2 ZJY-6428TSWOG01`；`imu=U8 MPU9250`；`pmu=U3 IP5306`；`usb_uart=U6 CP2104` |
| 核心器件 | U1 ESP32-WROOM32 | `reference=U1`；`part_number=ESP32-WROOM32`；`power=VCC_3V3`；`reset=EN`；`uart=TXD0/RXD0` |
| 内存与 Flash | ESP32-WROOM32 Flash | `module=ESP32-WROOM32`；`documented_capacity=4MB`；`schematic_capacity_label=null` |
| 总线 | OLED SPI | `device=U2 ZJY-6428TSWOG01`；`cs=GPIO14`；`reset=GPIO33`；`dc=GPIO27`；`sck=GPIO18 / D0`；`mosi=GPIO23 / D1`；`miso=null` |
| 核心器件 | OLED 驱动与规格 | `schematic_part=ZJY-6428TSWOG01`；`documented_driver=SH1107`；`documented_size=1.3 inch`；`documented_resolution=64x128` |
| 电源 | OLED 供电 | `vpp=VCC_9V`；`vdd=VCC_3V3`；`vcomh=C5 2.2uF/16V`；`iref=R2 560K to GND` |
| 传感器 | U8 MPU9250 | `reference=U8`；`part_number=MPU9250`；`scl=GPIO21`；`sda=GPIO22`；`ad0=GND`；`chip_select=VCC_3V3`；`interrupt=null` |
| 核心器件 | MPU9250 灰色版配置 | `schematic_device=U8 MPU9250`；`documented_variant=灰色款`；`assembly_option_visible=false` |
| 总线 | MPU9250 I2C | `controller=U1 ESP32-WROOM32`；`device=U8 MPU9250`；`scl=GPIO21`；`sda=GPIO22`；`address_strap=AD0=GND`；`address_visible=false` |
| GPIO 与控制信号 | LED、IR 与蜂鸣器 GPIO | `blue_led=GPIO19 -> R19 330R -> LED1`；`ir_led=GPIO17 -> R20 330R -> LED2`；`buzzer=GPIO26 -> R21 330R -> VT3 S8050 -> LS1`；`buzzer_supply=VCC_3V3` |
| 电源 | U3 IP5306 充放电 | `reference=U3`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`switch_node=SW -> L1`；`key=PWR_KEY`；`interface=custom IIC` |
| 总线地址 | IP5306 I2C 地址 | `device=U3 IP5306`；`bus=IIC`；`address=0x75` |
| 电源 | VCC_9V 升压 | `reference=U4`；`input=VCC_5V`；`output=VCC_9V`；`inductor=L1 10uH`；`diode=D1 1N5819`；`feedback=R4 73.2K; R6 11.8K` |
| 电源 | VCC_3V3 降压 | `reference=U5`；`input=VCC_5V`；`output=VCC_3V3`；`inductor=L2 2.2uH`；`feedback=R7 267K; R8 59K` |
| 电源 | 内置电池容量 | `documented_capacity=80mAh`；`documented_voltage=3.7V`；`schematic_net=VBAT`；`capacity_visible=false` |
| 调试与烧录 | CP2104 USB-UART | `bridge=U6 CP2104`；`usb=USB_DP/USB_DN`；`bridge_txd=TXD -> R11 470R -> RXD0`；`bridge_rxd=RXD <- TXD0`；`control=DTR/RTS` |
| 复位 | 自动下载与复位 | `reset=EN`；`boot=GPIO0`；`sources=DTR/RTS`；`transistors=VT1/VT2 S8050`；`manual_reset=S1`；`pullup=R15 10K`；`capacitor=C20 2.2uF` |
| 接口 | USB 连接器版本 | `documented_connector=USB Type-C`；`schematic_connector=U7 USB_Micro`；`cc_resistors=R9/R12 5.1K`；`revision_match=null` |
| 接口 | U7 Micro-USB | `reference=U7`；`power=VIN_USB`；`dm=D- -> R16 22R -> USB_DN`；`dp=D+ -> R17 22R -> USB_DP`；`protection=D2-D5 RLSD52A031V` |
| GPIO 与控制信号 | 用户按键 GPIO | `section_label=GPIO35`；`wire_label=GPIO25`；`documented_gpio=GPIO35`；`switch=S2 SMT_SW_TS_015`；`pullup=R18 10K` |
| 接口 | Grove/HY2.0-4P | `documented_signals=GPIO32; GPIO33; 5V; GND`；`connector_reference=null`；`schematic_visible=false` |
| 保护电路 | USB 钳位保护 | `devices=D2-D5 RLSD52A031V`；`protected_nets=VIN_USB; USB_DN; USB_DP`；`series_resistors=R16/R17 22R` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash，三张原理图未画独立 Flash 或在 U1 上标注容量。（证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U1 与完整页，无 Flash 容量）
- `component.oled-specification`：原理图仅标 U2 ZJY-6428TSWOG01，未直接标出产品正文中的 SH1107、1.3 英寸和 64x128 分辨率。（证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U2，未标 SH1107/尺寸/分辨率）
- `component.imu-variant`：原理图画出 U8 MPU9250，但产品正文称只有灰色款配备；现有原理图未标机壳颜色或装配选项，无法确定所有 K016 均装配 U8。（证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U8 MPU9250，无装配选项）
- `power.battery-capacity`：产品正文称内置 80mAh@3.7V 电池；Power 页只显示 VBAT 网络与 IP5306 BAT 引脚，未标容量或电池连接器。（证据：图 f9d2de52c30a / 第 1 页 / Power 页 U3 BAT/VBAT，未标容量）
- `interface.usb-connector-version`：产品正文称 USB Type-C，但本地 UsbUART 原理图明确画出 U7 USB_Micro；同页另有 USB_CC_1/USB_CC_2 5.1K 下拉，未显示其 Type-C 连接器。（证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 A4 R9/R12 与 C2-C3 U7 USB_Micro）
- `gpio.user-button-conflict`：UsbUART 页底部按键区域标题为 GPIO35，但连接 S2 的红色网络文字显示 GPIO25；EspCore 页 GPIO35 存在且产品正文映射按键为 G35，当前图内标注互相冲突。（证据：图 29eddc8e6351 / 第 1 页 / UsbUART 页 D1，GPIO35 标题与 GPIO25 网络冲突; 图 65d5fc33c5d6 / 第 1 页 / EspCore 页 U1 GPIO35）
- `interface.grove-not-shown`：产品正文称提供 Grove/HY2.0-4P 并映射 GPIO32/GPIO33/5V/GND，但三张本地原理图均未画出该连接器。（证据：图 65d5fc33c5d6 / 第 1 页 / EspCore 完整页，无 Grove 连接器; 图 f9d2de52c30a / 第 1 页 / Power 完整页，无 Grove 连接器; 图 29eddc8e6351 / 第 1 页 / UsbUART 完整页，无 Grove 连接器）
- `review.flash-capacity`：当前 M5Stick K016 的 ESP32-WROOM32 Flash 是否固定为 4MB？；原因：4MB 来自产品正文，原理图未标容量。
- `review.oled-spec`：U2 ZJY-6428TSWOG01 是否确定采用 SH1107、1.3 英寸、64x128 面板？；原因：这些参数来自产品正文，原理图只给出模组料号。
- `review.imu-variant`：哪些 M5Stick K016 颜色/BOM 批次实际装配 U8 MPU9250？；原因：产品正文限定灰色款，原理图未标装配选项。
- `review.battery-capacity`：内置电池是否固定为 80mAh@3.7V？；原因：容量来自产品正文，Power 页未标。
- `review.usb-connector`：当前 K016 批次实际使用 Micro-USB 还是 USB Type-C，对应哪一版 USB-UART 原理图？；原因：产品正文与本地原理图连接器类型冲突。
- `review.user-button-gpio`：S2 用户按键实际连接 GPIO35 还是 GPIO25？；原因：同一原理图区域标题与网络标注冲突，正文映射为 GPIO35。
- `review.grove-connector`：Grove/HY2.0-4P 连接器位号和保护电路位于哪一版 M5Stick 原理图？；原因：正文列出该接口，但三个本地资源均未画出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `65d5fc33c5d630f895a6f83286687ee87195372f56c9b681cde1b1b791808dc0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/EspCore_page_01.png` |
| 2 | 1 | `f9d2de52c30ac55c9539544651b32ee4c423f9ffdf71380ded407172833e77cc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/Power_page_01.png` |
| 3 | 1 | `29eddc8e6351de38581693060e0c38082790c96a68687a508faacd08d798aba4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/UsbUART_page_01.png` |

---

源文档：`zh_CN/core/m5stick.md`

源文档 SHA-256：`84f16b52e6f48ed7027860860bfabf4a1f6f84663ac28aa8f65e450dff6e023c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
