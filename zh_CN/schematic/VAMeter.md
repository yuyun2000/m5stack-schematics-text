# VAMeter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | VAMeter |
| SKU | K136 |
| 产品 ID | `vameter-1ffcc2eeb50a` |
| 源文档 | `zh_CN/core/VA Meter.md` |

## 概述

VAMeter 以 U5 STAMP_S3 为主控，使用两颗 INA226 与 0.01 Ω/1 Ω 串联分流器实现高、低电流量程，并通过 CA-IS3020S I2C 隔离器和 CA-IS3642HW 数字隔离器隔离测量域。输入/输出使用 USB-C 和 Base 端子，LGS5148 从测量输入生成 5 V，主控还连接 ST7789 显示、旋转编码器、蜂鸣器及 BOOT/复位键。随附 Base 使用 5 V 继电器控制 PVOUT 到 VOUT，并提供 GPIO8/GPIO9 Grove 接口。

## 检索关键词

`VAMeter`、`K136`、`STAMP_S3`、`ESP32S3FN8`、`INA226`、`CA-IS3020S`、`CA-IS3642HW`、`LGS5148`、`ST7789`、`HF3FF/005-1ZTF`、`0.01R shunt`、`1R shunt`、`HICUR`、`GPIO46`、`FSDA GPIO5`、`FSCL GPIO6`、`ALERT1 GPIO41`、`ALERT2 GPIO40`、`BUZ_PWM GPIO14`、`EXT_G10`、`EXT_G9`、`EXT_G8`、`EXT_G42`、`GPIO10_REL`、`USB-C`、`FBUS_IN`、`FBUS_OUT`、`ISO-VIN`、`ISO-VOUT`、`P5V`、`FVDD`、`P3V3`、`SYS_5V`、`2.5uA`、`250uA`、`8.192A`、`81.92mA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | STAMP_S3 | ESP32-S3 主控模块，连接隔离测量、显示、编码器、蜂鸣器、USB 和扩展 GPIO | 图 6b1f2bf4df0c / 第 1 页 / C2-D3，U5 STAMP_S3 全部 GPIO 网络; 图 6de4fbef5669 / 第 1 页 / 逻辑图顶部 STAMP S3 / ESP32S3FN8 |
| U3/U4 | INA226 | 高电流与低电流两路电压/电流监测器 | 图 6b1f2bf4df0c / 第 1 页 / B1-C2，U3/U4 INA226、IN+/IN-/VBUS/SCL/SDA/ALERT/A0/A1 |
| R4/R6 | R010/1% / 1R/1% | 0.01 Ω 高电流与 1 Ω 低电流串联分流器 | 图 6b1f2bf4df0c / 第 1 页 / A1-B2，FBUS_IN-R4-R6-FBUS_OUT 测量路径 |
| Q1 | AP50P20Q | HICUR/RS_SW 控制的 1 Ω 分流器旁路 MOSFET | 图 6b1f2bf4df0c / 第 1 页 / A1-B2，Q1 AP50P20Q、D2 MM5Z12V、RS_SW、R6 |
| U2 | CA-IS3020S | 主控 SYS_SDA/SYS_SCL 到测量域 FSDA/FSCL 的双向 I2C 隔离器 | 图 6b1f2bf4df0c / 第 1 页 / D1-D2，U2 CA-IS3020S、SYS_SDA/SYS_SCL、FSDA/FSCL |
| U1 | CA-IS3642HW | HICUR 与两路 INA226 ALERT 的数字隔离器 | 图 6b1f2bf4df0c / 第 1 页 / C1-C2，U1 CA-IS3642HW、HICUR、SYS_ALERT1/2、ALERT1/2 |
| U6 | LGS5148 | PVIN 输入的降压转换器，生成 P5V | 图 6b1f2bf4df0c / 第 1 页 / A3-A4，D5/R10/U6 LGS5148/WPN3012H4R7MT/P5V |
| J1/J2 | GT-USB-9010AB | 测量输入与输出 USB-C 连接器，承载电源与 USB 数据/CC/SBU 网络 | 图 6b1f2bf4df0c / 第 1 页 / A1-B2，J1/J2 GT-USB-9010AB，FBUS_IN/FBUS_OUT 与 USB_* |
| S1 | MK-22D14-G020 | FBUS_IN/PVIN/FGND 供电和隔离模式选择开关 | 图 6b1f2bf4df0c / 第 1 页 / B1，S1 MK-22D14-G020、FBUS_IN/PVIN/FGND |
| J3/J4 | CON6 | VAMeter 与 Base 间的两组 6 针电源/GPIO连接器 | 图 6b1f2bf4df0c / 第 1 页 / B2-B3，J3/J4 CON6，FBUS/P5V/FGND/EXT_G* |
| BZ1/Q3 | BUZZER / A2N7002 | GPIO14 BUZ_PWM 驱动的蜂鸣器及低边 MOSFET | 图 6b1f2bf4df0c / 第 1 页 / B4-C4，BZ1 BUZZER、Q3 A2N7002、BUZ_PWM、D4 |
| S2 | SIQ-02FVS3 | GPIO3/GPIO1/GPIO2 旋转编码器及按压开关 | 图 6b1f2bf4df0c / 第 1 页 / C4-D4，S2 SIQ-02FVS3、ENC_A/ENC_B/ENC_S |
| S3/S4 | SW | SYS_RST 复位键与 SYS_G0 启动键 | 图 6b1f2bf4df0c / 第 1 页 / C4，S3 SYS_RST、S4 SYS_G0 |
| LCD (logic diagram) | ST7789 | 1.3 英寸 IPS 显示，使用 GPIO33-GPIO38 | 图 6de4fbef5669 / 第 1 页 / 逻辑图下部 1.3-inch IPS-LCD ST7789 与 DATA/SCK/RS/RST/CS/BL |
| RLY1 | HF3FF/005-1ZTF | Base 上串联控制 PVOUT 到 VOUT 的 5 V 继电器 | 图 fb6e390d8d88 / 第 1 页 / B3-C4，RLY1 HF3FF/005-1ZTF、PVOUT/VOUT/SYS_5V |
| Q1 (Base) | A2N7002 | GPIO10_REL 驱动 Base 继电器线圈的低边 MOSFET | 图 fb6e390d8d88 / 第 1 页 / C3-C4，GPIO10_REL/R1/Q1/D1/RLY1 |
| J3 (Base) | Grove 等高白色 | GPIO9/GPIO8/SYS_5V/FGND Grove 扩展口 | 图 fb6e390d8d88 / 第 1 页 / C1，J3 Grove、GPIO9/GPIO8/FU1/SYS_5V/FGND |
| J4/J5 (Base) | KF2EDGR_3.81mm_2P | Base PVIN 输入与 VOUT 输出接线端子 | 图 fb6e390d8d88 / 第 1 页 / B1-B2，J4 PVIN/PGND、J5 VOUT |

## 系统结构

### 隔离双量程功率计

STAMP_S3 通过隔离 I2C 和数字隔离器控制两颗 INA226；0.01 Ω 与 1 Ω 分流器串联，HICUR 控制 MOSFET 旁路 1 Ω 分流器以切换量程。

- 参数与网络：`controller=U5 STAMP_S3`；`monitors=U3/U4 INA226`；`i2c_isolator=U2 CA-IS3020S`；`digital_isolator=U1 CA-IS3642HW`；`high_current_shunt=R4 R010/1%`；`low_current_shunt=R6 1R/1%`；`range_control=GPIO46/HICUR`
- 证据：图 6b1f2bf4df0c / 第 1 页 / J1/J2 测量路径、U3/U4、U1/U2、Q1 与 U5; 图 6de4fbef5669 / 第 1 页 / 内部逻辑图 ISOLATED、INA226、1R/0.01R、MOS、SW:G46

## 电源

### 供电/隔离模式选择

S1 MK-22D14-G020 在 FBUS_IN、PVIN 与 FGND 网络之间选择主板供电路径，PVIN 随后进入 P5V 降压电路。

- 参数与网络：`reference=S1`；`part_number=MK-22D14-G020`；`nets=FBUS_IN; PVIN; FGND`；`downstream=U6 LGS5148 -> P5V`
- 证据：图 6b1f2bf4df0c / 第 1 页 / B1，S1 FBUS_IN/PVIN/FGND

### PVIN 到 P5V

PVIN 经 D5 DSK34 和 R10 0.5 Ω 进入 U6 LGS5148，经 WPN3012H4R7MT 电感输出 P5V。

- 参数与网络：`input=PVIN`；`diode=D5 DSK34`；`input_resistor=R10 0.5R/1%`；`converter=U6 LGS5148`；`inductor=WPN3012H4R7MT`；`output=P5V`
- 证据：图 6b1f2bf4df0c / 第 1 页 / A3-A4，PVIN/D5/R10/U6/电感/P5V

### 隔离电源域

主控侧使用 P3V3/GND，测量侧使用 FVDD/FGND；CA-IS3020S 和 CA-IS3642HW 分别跨越两电源域。

- 参数与网络：`controller_domain=P3V3/GND`；`field_domain=FVDD/FGND`；`isolators=U2 CA-IS3020S; U1 CA-IS3642HW`
- 证据：图 6b1f2bf4df0c / 第 1 页 / U1/U2 两侧 P3V3/GND 与 FVDD/FGND

### 测量输入电压范围

内部逻辑图明确标注 ISO-VIN 侧输入为 5–24 V。

- 参数与网络：`input=ISO-VIN/FBUS_IN`；`range=5-24V`
- 证据：图 6de4fbef5669 / 第 1 页 / 逻辑图右侧 5-24V INPUT / ISO-VIN

### Base 继电器输出

RLY1 HF3FF/005-1ZTF 常开触点串联 PVOUT 到 VOUT；5 V 线圈由 GPIO10_REL 经 Q1 A2N7002 低边驱动，D1 1N4148WS 续流。

- 参数与网络：`relay=RLY1 HF3FF/005-1ZTF`；`contact_input=PVOUT`；`contact_output=VOUT`；`coil_supply=SYS_5V`；`driver=GPIO10_REL -> Q1 A2N7002`；`flyback=D1 1N4148WS`
- 证据：图 fb6e390d8d88 / 第 1 页 / B3-C4，RLY1/Q1/D1/R1/PVOUT/VOUT

## 接口

### 测量输入/输出 USB-C

J1/J2 均为 GT-USB-9010AB，VBUS 分别接 FBUS_IN/FBUS_OUT；DP/DM、SBU1/2、CC1/2 分别以 USB_* 网络贯通到对应侧。

- 参数与网络：`input=J1 GT-USB-9010AB, VBUS=FBUS_IN`；`output=J2 GT-USB-9010AB, VBUS=FBUS_OUT`；`data=USB_DP; USB_DM`；`sideband=USB_SBU1; USB_SBU2`；`configuration=USB_CC1; USB_CC2`
- 证据：图 6b1f2bf4df0c / 第 1 页 / A1-B2，J1/J2 全部 USB-C 网络

### 旋转编码器

S2 SIQ-02FVS3 的 A/B/S 分别连接 ENC_A/ENC_B/ENC_S，对应 STAMP_S3 GPIO3/GPIO1/GPIO2，并由 R12/R14/R13 5.1 kΩ 上拉。

- 参数与网络：`reference=S2`；`part_number=SIQ-02FVS3`；`a=GPIO3/ENC_A`；`b=GPIO1/ENC_B`；`switch=GPIO2/ENC_S`；`pullups=R12/R14/R13 5.1K`
- 证据：图 6b1f2bf4df0c / 第 1 页 / C3-D4，U5 G1/G2/G3、R12-R14、S2

### STAMP_S3 USB

内部逻辑图明确标注 STAMP_S3 USB 仅以 5 V 输入供电，同时 D-/D+ 使用 GPIO19/GPIO20 提供 OTG/Serial。

- 参数与网络：`power=only 5V in`；`dm=GPIO19`；`dp=GPIO20`；`functions=OTG/Serial`
- 证据：图 6de4fbef5669 / 第 1 页 / 逻辑图顶部 USB ONLY 5V IN、OTG/SERIAL、D-:G19 D+:G20

### 1.3 英寸 ST7789 显示

内部逻辑图标注 1.3 英寸 IPS-LCD、ST7789，DATA/SCK/RS/RST/CS/BL 分别连接 GPIO35/36/34/33/37/38。

- 参数与网络：`controller=ST7789`；`size=1.3 inch`；`data=GPIO35`；`sck=GPIO36`；`rs=GPIO34`；`reset=GPIO33`；`cs=GPIO37`；`backlight=GPIO38`
- 证据：图 6de4fbef5669 / 第 1 页 / 逻辑图下部 1.3-inch IPS-LCD ST7789 pin mapping

### Base 输入输出端子

J4 3.81 mm 2P 提供 PVIN 与 PGND，J5 3.81 mm 2P 提供 VOUT。

- 参数与网络：`input=J4 pin1 PVIN; pin2 PGND`；`output=J5 VOUT`；`pitch=3.81mm`
- 证据：图 fb6e390d8d88 / 第 1 页 / B1-B2，J4/J5 KF2EDGR_3.81mm_2P

### Base Grove

J3 Grove pins 4/3/2/1 依次为 GPIO9、GPIO8、经 FU1 SMD0805B050TF 保护的 SYS_5V、FGND。

- 参数与网络：`pin4=GPIO9`；`pin3=GPIO8`；`pin2=SYS_5V via FU1 SMD0805B050TF`；`pin1=FGND`
- 证据：图 fb6e390d8d88 / 第 1 页 / C1，J3 Grove pins 1-4 与 FU1

## 总线

### 隔离 I2C

STAMP_S3 GPIO5/SYS_SDA 与 GPIO6/SYS_SCL 经 U2 CA-IS3020S 转换为测量域 FSDA/FSCL，连接两颗 INA226。

- 参数与网络：`controller=U5 STAMP_S3`；`controller_sda=GPIO5/SYS_SDA`；`controller_scl=GPIO6/SYS_SCL`；`isolator=U2 CA-IS3020S`；`field_sda=FSDA`；`field_scl=FSCL`；`devices=U3/U4 INA226`
- 证据：图 6b1f2bf4df0c / 第 1 页 / D1-D3，U5 G5/G6、U2、U3/U4 FSDA/FSCL; 图 6de4fbef5669 / 第 1 页 / 逻辑图 I2C SCL:G6 SDA:G5 与 CA-IS3020S

### 隔离告警与量程控制

U1 CA-IS3642HW 隔离 HICUR、SYS_ALERT1/GPIO41 与 SYS_ALERT2/GPIO40，对应测量侧 RS_SW、ALERT1、ALERT2。

- 参数与网络：`isolator=U1 CA-IS3642HW`；`range=GPIO46 HICUR -> RS_SW`；`alert1=ALERT1 -> SYS_ALERT1/GPIO41`；`alert2=ALERT2 -> SYS_ALERT2/GPIO40`
- 证据：图 6b1f2bf4df0c / 第 1 页 / C1-C3，U1 CA-IS3642HW 与 U5 G40/G41/G46; 图 6de4fbef5669 / 第 1 页 / 逻辑图 CA-IS3642 SW:G46 ALERT:G41 ALERT2:G40

## 总线地址

### INA226 地址脚

U3 的 A0/A1 均接 FGND；U4 的地址脚配置与 U3 不同，其中一脚连接 FVDD，形成两组不同硬件地址。

- 参数与网络：`U3=A0=FGND; A1=FGND`；`U4=one address strap=FVDD; other strap=FGND`
- 证据：图 6b1f2bf4df0c / 第 1 页 / B1-C2，U3/U4 pins A0/A1 与 FVDD/FGND

## GPIO 与控制信号

### 测量控制 GPIO

STAMP_S3 使用 GPIO5 FSDA、GPIO6 FSCL、GPIO41 ALERT1、GPIO40 ALERT2 和 GPIO46 HICUR。

- 参数与网络：`fsda=GPIO5`；`fscl=GPIO6`；`alert1=GPIO41`；`alert2=GPIO40`；`range=GPIO46`
- 证据：图 6b1f2bf4df0c / 第 1 页 / U5 STAMP_S3 G5/G6/G40/G41/G46 网络

### Base 扩展 GPIO

J3/J4 向 Base 引出 EXT_G10、EXT_G9、EXT_G8、EXT_G42；Base 使用 GPIO10_REL 驱动继电器，Grove 使用 GPIO9/GPIO8。

- 参数与网络：`main_connectors=J3 EXT_G10/EXT_G9/EXT_G8; J4 EXT_G42`；`relay=GPIO10_REL`；`grove=GPIO9; GPIO8`
- 证据：图 6b1f2bf4df0c / 第 1 页 / J3/J4 CON6 EXT_G10/G9/G8/G42; 图 fb6e390d8d88 / 第 1 页 / J1/J3 Base GPIO10_REL/GPIO9/GPIO8

## 复位

### 复位与 BOOT

S3 按下时将 SYS_RST 拉低，S4 按下时将 SYS_G0 拉低；两网络分别连接 STAMP_S3 EN 与 G0。

- 参数与网络：`reset=S3 SYS_RST -> U5 EN`；`boot=S4 SYS_G0 -> U5 G0`；`active_level=low`
- 证据：图 6b1f2bf4df0c / 第 1 页 / C3-C4，U5 SYS_RST/SYS_G0 与 S3/S4

## 音频

### 蜂鸣器

GPIO14/BUZ_PWM 经 R19 5.1 kΩ 驱动 Q3 A2N7002，低边控制 P5V 供电的 BZ1 BUZZER，D4 1N4148WT 提供反向钳位。

- 参数与网络：`gpio=GPIO14/BUZ_PWM`；`gate_resistor=R19 5.1K/1%`；`transistor=Q3 A2N7002`；`buzzer=BZ1`；`supply=P5V`；`flyback=D4 1N4148WT`
- 证据：图 6b1f2bf4df0c / 第 1 页 / B4-C4，P5V/R18/D4/BZ1/Q3/R19/BUZ_PWM

## 模拟电路

### 串联分流测量路径

FBUS_IN 依次通过 R4 0.01 Ω 和 R6 1 Ω 到 FBUS_OUT；两颗 INA226 分别跨接对应分流段并采样总线电压。

- 参数与网络：`input=FBUS_IN`；`high_current_shunt=R4 R010/1%`；`low_current_shunt=R6 1R/1%`；`output=FBUS_OUT`；`monitors=U3/U4 INA226`
- 证据：图 6b1f2bf4df0c / 第 1 页 / A1-C2，FBUS_IN-R4-R6-FBUS_OUT 与 U3/U4 IN+/IN-/VBUS

### 高低电流量程切换

HICUR 高电平经隔离器生成 RS_SW，驱动 Q1 AP50P20Q 旁路 R6 1 Ω；低电平时 R6 保持串入测量路径。

- 参数与网络：`controller_gpio=GPIO46/HICUR`；`isolated_net=RS_SW`；`switch=Q1 AP50P20Q`；`bypassed_shunt=R6 1R/1%`；`gate_protection=D2 MM5Z12V`
- 证据：图 6b1f2bf4df0c / 第 1 页 / A1-C2，U1 HICUR/RS_SW 与 Q1/D2/R6

### 原理图标注量程与分辨率

原理图注释给出 HICUR=1 时约 ±8.192 A peak、250 µA/div，HICUR=0 时约 ±81.92 mA peak、2.5 µA/div。

- 参数与网络：`high_current=HICUR=1; about ±8.192A peak; 250uA/div`；`low_current=HICUR=0; about ±81.92mA peak; 2.5uA/div`
- 证据：图 6b1f2bf4df0c / 第 1 页 / C1 左侧 HICUR measurement mode 注释; 图 6de4fbef5669 / 第 1 页 / 逻辑图 SW=1/SW=0 MAX/DIV 参数

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 隔离双量程功率计 | `controller=U5 STAMP_S3`；`monitors=U3/U4 INA226`；`i2c_isolator=U2 CA-IS3020S`；`digital_isolator=U1 CA-IS3642HW`；`high_current_shunt=R4 R010/1%`；`low_current_shunt=R6 1R/1%`；`range_control=GPIO46/HICUR` |
| 模拟电路 | 串联分流测量路径 | `input=FBUS_IN`；`high_current_shunt=R4 R010/1%`；`low_current_shunt=R6 1R/1%`；`output=FBUS_OUT`；`monitors=U3/U4 INA226` |
| 模拟电路 | 高低电流量程切换 | `controller_gpio=GPIO46/HICUR`；`isolated_net=RS_SW`；`switch=Q1 AP50P20Q`；`bypassed_shunt=R6 1R/1%`；`gate_protection=D2 MM5Z12V` |
| 模拟电路 | 原理图标注量程与分辨率 | `high_current=HICUR=1; about ±8.192A peak; 250uA/div`；`low_current=HICUR=0; about ±81.92mA peak; 2.5uA/div` |
| 总线 | 隔离 I2C | `controller=U5 STAMP_S3`；`controller_sda=GPIO5/SYS_SDA`；`controller_scl=GPIO6/SYS_SCL`；`isolator=U2 CA-IS3020S`；`field_sda=FSDA`；`field_scl=FSCL`；`devices=U3/U4 INA226` |
| 总线 | 隔离告警与量程控制 | `isolator=U1 CA-IS3642HW`；`range=GPIO46 HICUR -> RS_SW`；`alert1=ALERT1 -> SYS_ALERT1/GPIO41`；`alert2=ALERT2 -> SYS_ALERT2/GPIO40` |
| 总线地址 | INA226 地址脚 | `U3=A0=FGND; A1=FGND`；`U4=one address strap=FVDD; other strap=FGND` |
| 接口 | 测量输入/输出 USB-C | `input=J1 GT-USB-9010AB, VBUS=FBUS_IN`；`output=J2 GT-USB-9010AB, VBUS=FBUS_OUT`；`data=USB_DP; USB_DM`；`sideband=USB_SBU1; USB_SBU2`；`configuration=USB_CC1; USB_CC2` |
| 电源 | 供电/隔离模式选择 | `reference=S1`；`part_number=MK-22D14-G020`；`nets=FBUS_IN; PVIN; FGND`；`downstream=U6 LGS5148 -> P5V` |
| 电源 | PVIN 到 P5V | `input=PVIN`；`diode=D5 DSK34`；`input_resistor=R10 0.5R/1%`；`converter=U6 LGS5148`；`inductor=WPN3012H4R7MT`；`output=P5V` |
| 电源 | 隔离电源域 | `controller_domain=P3V3/GND`；`field_domain=FVDD/FGND`；`isolators=U2 CA-IS3020S; U1 CA-IS3642HW` |
| GPIO 与控制信号 | 测量控制 GPIO | `fsda=GPIO5`；`fscl=GPIO6`；`alert1=GPIO41`；`alert2=GPIO40`；`range=GPIO46` |
| GPIO 与控制信号 | Base 扩展 GPIO | `main_connectors=J3 EXT_G10/EXT_G9/EXT_G8; J4 EXT_G42`；`relay=GPIO10_REL`；`grove=GPIO9; GPIO8` |
| 音频 | 蜂鸣器 | `gpio=GPIO14/BUZ_PWM`；`gate_resistor=R19 5.1K/1%`；`transistor=Q3 A2N7002`；`buzzer=BZ1`；`supply=P5V`；`flyback=D4 1N4148WT` |
| 接口 | 旋转编码器 | `reference=S2`；`part_number=SIQ-02FVS3`；`a=GPIO3/ENC_A`；`b=GPIO1/ENC_B`；`switch=GPIO2/ENC_S`；`pullups=R12/R14/R13 5.1K` |
| 复位 | 复位与 BOOT | `reset=S3 SYS_RST -> U5 EN`；`boot=S4 SYS_G0 -> U5 G0`；`active_level=low` |
| 接口 | STAMP_S3 USB | `power=only 5V in`；`dm=GPIO19`；`dp=GPIO20`；`functions=OTG/Serial` |
| 接口 | 1.3 英寸 ST7789 显示 | `controller=ST7789`；`size=1.3 inch`；`data=GPIO35`；`sck=GPIO36`；`rs=GPIO34`；`reset=GPIO33`；`cs=GPIO37`；`backlight=GPIO38` |
| 电源 | 测量输入电压范围 | `input=ISO-VIN/FBUS_IN`；`range=5-24V` |
| 接口 | Base 输入输出端子 | `input=J4 pin1 PVIN; pin2 PGND`；`output=J5 VOUT`；`pitch=3.81mm` |
| 电源 | Base 继电器输出 | `relay=RLY1 HF3FF/005-1ZTF`；`contact_input=PVOUT`；`contact_output=VOUT`；`coil_supply=SYS_5V`；`driver=GPIO10_REL -> Q1 A2N7002`；`flyback=D1 1N4148WS` |
| 接口 | Base Grove | `pin4=GPIO9`；`pin3=GPIO8`；`pin2=SYS_5V via FU1 SMD0805B050TF`；`pin1=FGND` |
| 总线地址 | 两颗 INA226 地址 | `claimed_addresses=0x40; 0x41`；`schematic_evidence=different A0/A1 straps`；`devices=U3/U4 INA226` |
| 存储 | Stamp-S3 Flash 容量 | `module=STAMP_S3`；`soc=ESP32S3FN8`；`claimed_flash=8MB` |
| 模拟电路 | 整机采样误差 | `unverified_claims=1.01% small-current; 0.94% large-current; 0.69% uA-level; 0.11% voltage` |
| 电源 | PD 输出与继电器额定能力 | `unverified_pd_output=24V@3A/5A thermal ratings`；`unverified_relay=5-24V@5A` |

## 待确认事项

- `address.ina226`：产品正文称两颗 INA226 地址为 0x40/0x41；原理图只显示不同 A0/A1 接法，未直接印出十六进制地址，需结合 datasheet 复核对应关系。（证据：图 6b1f2bf4df0c / 第 1 页 / U3/U4 A0/A1 地址脚，未见 0x40/0x41 文本）
- `storage.flash-capacity`：本地逻辑图确认主控芯片为 ESP32S3FN8，但原理图未单独以容量字段标注 8 MB Flash。（证据：图 6b1f2bf4df0c / 第 1 页 / U5 仅标 STAMP_S3; 图 6de4fbef5669 / 第 1 页 / 逻辑图标 ESP32S3FN8，未分列 Flash 容量）
- `analog.accuracy`：原理图给出量程与分流器，但未直接标注产品正文中的小电流、大电流、µA 级和电压采样误差百分比。（证据：图 6b1f2bf4df0c / 第 1 页 / 测量路径注释仅给 MAX/DIV，不列误差百分比）
- `power.output-rating`：原理图确认分流器、USB-C、Base 继电器和端子，但未直接列出 24 V@3 A/5 A 热条件或继电器 5–24 V@5 A 整机额定值。（证据：图 6b1f2bf4df0c / 第 1 页 / J1/J2/R4/R6 未列整机热额定; 图 fb6e390d8d88 / 第 1 页 / RLY1/J4/J5 未列整机继电器额定范围）
- `review.ina226-addresses`：请用 INA226 datasheet 按 U3/U4 的 A0/A1 接法确认 0x40/0x41 对应关系。；原因：原理图未直接印出十六进制地址。
- `review.flash-capacity`：请用 Stamp-S3/ESP32S3FN8 datasheet 或 BOM 确认 8 MB Flash。；原因：本地资源未单列容量字段。
- `review.accuracy`：请用校准/测试报告复核电流和电压采样误差百分比。；原因：这些整机精度指标未印在原理图中。
- `review.output-ratings`：请用热测试与继电器/端子 BOM 复核 PD 输出和 Base 继电器额定能力。；原因：原理图确认拓扑但不列整机热额定。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6b1f2bf4df0cf37feae98aa54b5720154e9a6c6b32e71f37b047796889f67f27` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_V1.2_sch_01.png` |
| 2 | 1 | `fb6e390d8d880aeb546da9a0c8d011b74e9dc49fc488ebb4ceae3ed8b74e25b9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_base_V1.0_sch_01.png` |
| 3 | 1 | `6de4fbef5669146e7fcb1457f2771b21071ef4095d23f1b54016c30a41c60177` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/01.png` |

---

源文档：`zh_CN/core/VA Meter.md`

源文档 SHA-256：`6f66f16283d3ccdd9c0f11d6d38700aca37eef45144356d2b12c3d9ab879d67e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
