# Module HMI 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module HMI |
| SKU | M129 |
| 产品 ID | `module-hmi-3a13e8f227d3` |
| 源文档 | `zh_CN/module/HMI Module.md` |

## 概述

Module HMI 以 U5 STM32F030F4P6 采集 S1 旋转编码器与 S2/S3 两个按键，并以 LEDA/LEDB 驱动 D4/D5 两个红色指示灯。U5 的 SDA/SCL 连接 M5-Bus，PORT.B 将 GPIO36/GPIO26 直通 Grove，PORT.C 将 RXD/TXD 直通 Grove；J4 提供 SWD。BUS_5V 经 U2 HX6306P332 生成 VCC_3V3，BAT+ 在 P1 电池接口与 M5-Bus 之间引出，但 I2C 地址 0x41、500mAh 容量和充电路径未由本页确认。

## 检索关键词

`Module HMI`、`M129`、`STM32F030F4P6`、`HX6306P332`、`SIQ-02FVS3`、`Encoder`、`BTN_A`、`BTN_B`、`BTN_S`、`INA`、`INB`、`LEDA`、`LEDB`、`D4 Red 0603`、`D5 Red 0603`、`I2C`、`0x41`、`SDA`、`SCL`、`GPIO36`、`GPIO26`、`RXD`、`TXD`、`PORT.B`、`PORT.C`、`BUS_5V`、`VCC_3V3`、`BAT+`、`SWD_5P`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`M5_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | STM32F030F4P6 | 采集编码器与按键、驱动两路 LED，并通过 I2C 与主机通信的 MCU | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1-B1 U5，底部标 STM32F030F4P6，PA/PF/PB、BOOT0/NRST、电源引脚 |
| U2 | HX6306P332 | 将 BUS_5V 转换为 VCC_3V3 的三脚稳压器 | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 A2 U2 HX6306P332，VIN 接 BUS_5V、VOUT 接 VCC_3V3、GND 接地 |
| S1 | SIQ-02FVS3 | 旋转编码器兼按压输入，输出 INA、INB 和 BTN_S | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 B2 S1 SIQ-02FVS3，A/S/C/B 引脚与 INA/BTN_S/GND/INB |
| S2/S3 | 4.5*4.5*7 | BTN_A 与 BTN_B 两个对地输入按键 | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 B3-C3 BTN_A/BTN_B 区 S2/S3，2 脚接信号、1/3 脚接 GND |
| D4/D5 | Red 0603 | 由 LEDA/LEDB 控制的两路红色指示 LED | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 B4/C4 D4/D5 Red 0603，与 R13/R14 1K 和 VCC_3V3 |
| J1 | GROVE | PORT.B 接口，引出 GPIO36、GPIO26、BUS_5V 和 GND | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 C1 J1 GROVE，IO2 GPIO36、IO1 GPIO26、5V BUS_5V、GND |
| J2 | GROVE | PORT.C UART 接口，引出 RXD、TXD、BUS_5V 和 GND | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 C1-D1 J2 GROVE，IO2 RXD、IO1 TXD、5V BUS_5V、GND |
| J3 | M5_BUS | 30 针 M5-Bus，连接 I2C、UART、PORT.B、5V、BAT+、HPWR 与 GND | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 D3-D4 J3 M5_BUS，1~30 脚及外部网络 |
| J4 | SWD_5P | MCU 调试与复位接口，引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 B1-C1 J4 SWD_5P，1~5 脚 |
| P1 | 未标注 | 四焊盘电池接口，BAT+ 一脚及三路 GND | 图 df6864d1b3d9 / 第 1 页 / 第 1 页 D2-D3 P1，1 接 BAT+，2/3/4 接 GND |

## 系统结构

### Module HMI

U5 STM32F030F4P6 采集 S1 编码器与 S2/S3 按键，控制 D4/D5 LED，并通过 SDA/SCL 接 J3；J1/J2 分别直通 PORT.B GPIO 与 PORT.C UART，U2 由 BUS_5V 生成 VCC_3V3。

- 参数与网络：`mcu=U5 STM32F030F4P6`；`encoder=S1 SIQ-02FVS3`；`buttons=S2 BTN_A,S3 BTN_B`；`leds=D4 LEDA,D5 LEDB`；`host_bus=J3 M5_BUS`；`regulator=U2 HX6306P332`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页完整原理图各功能分区及同名网络

## 核心器件

### U5

主控制器位号 U5，型号标为 STM32F030F4P6。

- 参数与网络：`reference=U5`；`part_number=STM32F030F4P6`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5 底部 STM32F030F4P6

## 电源

### U2 HX6306P332

U2.3 VIN 接 BUS_5V，U2.2 VOUT 输出 VCC_3V3，U2.1 GND 接地；输入侧有 C7 4.7uF 与 C8 100nF，输出侧有 4.7uF 电容。

- 参数与网络：`input=U2.3 BUS_5V`；`output=U2.2 VCC_3V3`；`ground=U2.1 GND`；`input_caps=C7 4.7uF,C8 100nF`；`output_cap=4.7uF`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A2 U2 与 C7/C8/输出电容、BUS_5V/VCC_3V3/GND

### U5 3.3V 电源

U5.16 VDD 与 U5.5 VDDA 接 VCC_3V3，U5.15 VSS 接 GND；100nF 电容跨接 VCC_3V3 与 GND。

- 参数与网络：`VDD=U5.16 VCC_3V3`；`VDDA=U5.5 VCC_3V3`；`VSS=U5.15 GND`；`decoupling=100nF`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 B1 U5 VDD/VDDA/VSS 与 100nF 去耦

### P1 BAT+

P1.1 接 BAT+，P1.2/P1.3/P1.4 接 GND；BAT+ 同名网络连接 J3.29。页面未展示电池保护、充电器或电量监测器件。

- 参数与网络：`P1_pin_1=BAT+`；`P1_pins_2_3_4=GND`；`bus_pin=J3.29`；`charger_shown=false`；`gauge_shown=false`；`protection_ic_shown=false`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 D2-D3 P1 与 D4 J3.29 BAT+；全图无电池管理 IC

## 接口

### S1 输入调理

INA、BTN_S、INB 各通过 R1/R2/R3 10K 上拉到 VCC_3V3；INA 与 INB 各有 C1/C2 100nF 对地滤波。

- 参数与网络：`pullups=R1,R2,R3 each 10K to VCC_3V3`；`ina_filter=C1 100nF to GND`；`inb_filter=C2 100nF to GND`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 B2 S1 左侧 R1/R2/R3 与 C1/C2

### J1 PORT.B

J1 Grove 的 IO2 接 GPIO36、IO1 接 GPIO26、5V 接 BUS_5V、GND 接 GND；GPIO36/GPIO26 分别直连 J3.3/J3.9。

- 参数与网络：`IO2=GPIO36 -> J3.3`；`IO1=GPIO26 -> J3.9`；`5V=BUS_5V`；`GND=GND`；`direction=not specified by schematic`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 C1 J1 与 D4 J3.3 GPIO36/J3.9 GPIO26

### J2 PORT.C UART

J2 Grove 的 IO2 接 RXD、IO1 接 TXD、5V 接 BUS_5V、GND 接 GND；RXD/TXD 分别直连 J3.16/J3.15。

- 参数与网络：`IO2=RXD -> J3.16`；`IO1=TXD -> J3.15`；`5V=BUS_5V`；`GND=GND`；`logic_level=not annotated`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 C1-D1 J2 与 D4 J3.16 RXD/J3.15 TXD

### J3 M5_BUS 已用针脚

J3.2/.4/.6 接 GND，J3.3=GPIO36，J3.9=GPIO26，J3.15=TXD，J3.16=RXD，J3.17=SCL，J3.18=SDA，J3.27=BUS_5V，J3.29=BAT+，J3.30 标为 HPWR 并接 12V。

- 参数与网络：`pins_2_4_6=GND`；`pin_3=GPIO36`；`pin_9=GPIO26`；`pin_15=TXD`；`pin_16=RXD`；`pin_17=SCL`；`pin_18=SDA`；`pin_27=BUS_5V`；`pin_29=BAT+`；`pin_30=12V / HPWR`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 D3-D4 J3 全部外部网络标注

## 总线

### U5 I2C

U5.17 PA9 接 SCL，U5.18 PA10 接 SDA；SCL/SDA 分别连接 J3.17/J3.18。页面未显示板载 I2C 上拉电阻。

- 参数与网络：`controller=U5`；`scl=U5.17 PA9 -> SCL -> J3.17`；`sda=U5.18 PA10 -> SDA -> J3.18`；`pullups_shown=false`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5 SCL/SDA 与 D4 J3.17/J3.18

## GPIO 与控制信号

### S1 编码器 GPIO

U5.12 PA6 接 INA，U5.13 PA7 接 INB，U5.11 PA5 接 BTN_S；S1 的 A/B/S 分别连接 INA/INB/BTN_S，C 接 GND。

- 参数与网络：`INA=U5.12 PA6 -> S1.A`；`INB=U5.13 PA7 -> S1.B`；`BTN_S=U5.11 PA5 -> S1.S`；`common=S1.C GND`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5 INA/INB/BTN_S 与 B2 S1 A/B/S/C

### BTN_A/BTN_B

U5.9 PA3 接 BTN_A，U5.10 PA4 接 BTN_B；S2/S3 将相应信号按下时接 GND，R4/R5 各 10K 将信号上拉到 VCC_3V3。

- 参数与网络：`BTN_A=U5.9 PA3, S2 to GND, R4 10K pull-up`；`BTN_B=U5.10 PA4, S3 to GND, R5 10K pull-up`；`active_level=low when pressed`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5 BTN_A/BTN_B 与 B3-C3 S2/S3/R4/R5

### LEDA/LEDB

U5.6 PA0 接 LEDA，U5.7 PA1 接 LEDB；D4/D5 均为 Red 0603，并分别经 R13/R14 1K 接 VCC_3V3。

- 参数与网络：`LEDA=U5.6 PA0 -> D4 Red 0603 -> R13 1K -> VCC_3V3`；`LEDB=U5.7 PA1 -> D5 Red 0603 -> R14 1K -> VCC_3V3`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5 LEDA/LEDB 与 B4/C4 D4/D5/R13/R14

## 复位

### U5 BOOT0 与 NRST

U5.1 BOOT0 通过 R10 10K 接 GND；U5.4 NRST 连接 NRST 网络，由 R9 10K 上拉到 VCC_3V3，并由 C6 100nF 对地。

- 参数与网络：`boot0=U5.1 via R10 10K to GND`；`reset_pin=U5.4 NRST`；`reset_pullup=R9 10K to VCC_3V3`；`reset_cap=C6 100nF to GND`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1-A2 U5 BOOT0/R10 与 NRST/R9/C6

## 调试与烧录

### J4 SWD_5P

J4.1=VCC_3V3，J4.2=MCU_SWCLK，J4.3=MCU_SWDIO，J4.4=NRST，J4.5=GND；MCU_SWCLK/SWDIO 分别连接 U5 PA14/PA13。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=MCU_SWCLK / U5 PA14`；`pin_3=MCU_SWDIO / U5 PA13`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 B1-C1 J4 与 A1 U5 PA13/PA14 同名网络

## 其他事实

### 未展示功能分区

页面未展示显示屏、触摸控制器、音频编解码器、扬声器、麦克风、RF、独立存储器或 SD 卡接口。

- 参数与网络：`display_shown=false`；`touch_shown=false`；`audio_shown=false`；`rf_shown=false`；`external_storage_shown=false`；`sd_shown=false`
- 证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页完整原理图仅含 MCU、编码器/按键/LED、稳压、电池与连接器

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module HMI | `mcu=U5 STM32F030F4P6`；`encoder=S1 SIQ-02FVS3`；`buttons=S2 BTN_A,S3 BTN_B`；`leds=D4 LEDA,D5 LEDB`；`host_bus=J3 M5_BUS`；`regulator=U2 HX6306P332` |
| 核心器件 | U5 | `reference=U5`；`part_number=STM32F030F4P6` |
| 电源 | U2 HX6306P332 | `input=U2.3 BUS_5V`；`output=U2.2 VCC_3V3`；`ground=U2.1 GND`；`input_caps=C7 4.7uF,C8 100nF`；`output_cap=4.7uF` |
| 电源 | U5 3.3V 电源 | `VDD=U5.16 VCC_3V3`；`VDDA=U5.5 VCC_3V3`；`VSS=U5.15 GND`；`decoupling=100nF` |
| 复位 | U5 BOOT0 与 NRST | `boot0=U5.1 via R10 10K to GND`；`reset_pin=U5.4 NRST`；`reset_pullup=R9 10K to VCC_3V3`；`reset_cap=C6 100nF to GND` |
| 调试与烧录 | J4 SWD_5P | `pin_1=VCC_3V3`；`pin_2=MCU_SWCLK / U5 PA14`；`pin_3=MCU_SWDIO / U5 PA13`；`pin_4=NRST`；`pin_5=GND` |
| 总线 | U5 I2C | `controller=U5`；`scl=U5.17 PA9 -> SCL -> J3.17`；`sda=U5.18 PA10 -> SDA -> J3.18`；`pullups_shown=false` |
| 总线地址 | 正文中的 I2C 地址 | `documented_address=0x41`；`address_on_schematic=null`；`address_straps_shown=false` |
| GPIO 与控制信号 | S1 编码器 GPIO | `INA=U5.12 PA6 -> S1.A`；`INB=U5.13 PA7 -> S1.B`；`BTN_S=U5.11 PA5 -> S1.S`；`common=S1.C GND` |
| 接口 | S1 输入调理 | `pullups=R1,R2,R3 each 10K to VCC_3V3`；`ina_filter=C1 100nF to GND`；`inb_filter=C2 100nF to GND` |
| GPIO 与控制信号 | BTN_A/BTN_B | `BTN_A=U5.9 PA3, S2 to GND, R4 10K pull-up`；`BTN_B=U5.10 PA4, S3 to GND, R5 10K pull-up`；`active_level=low when pressed` |
| GPIO 与控制信号 | LEDA/LEDB | `LEDA=U5.6 PA0 -> D4 Red 0603 -> R13 1K -> VCC_3V3`；`LEDB=U5.7 PA1 -> D5 Red 0603 -> R14 1K -> VCC_3V3` |
| 接口 | J1 PORT.B | `IO2=GPIO36 -> J3.3`；`IO1=GPIO26 -> J3.9`；`5V=BUS_5V`；`GND=GND`；`direction=not specified by schematic` |
| 接口 | J2 PORT.C UART | `IO2=RXD -> J3.16`；`IO1=TXD -> J3.15`；`5V=BUS_5V`；`GND=GND`；`logic_level=not annotated` |
| 接口 | J3 M5_BUS 已用针脚 | `pins_2_4_6=GND`；`pin_3=GPIO36`；`pin_9=GPIO26`；`pin_15=TXD`；`pin_16=RXD`；`pin_17=SCL`；`pin_18=SDA`；`pin_27=BUS_5V`；`pin_29=BAT+`；`pin_30=12V / HPWR` |
| 电源 | P1 BAT+ | `P1_pin_1=BAT+`；`P1_pins_2_3_4=GND`；`bus_pin=J3.29`；`charger_shown=false`；`gauge_shown=false`；`protection_ic_shown=false` |
| 电源 | 正文中的 500mAh 电池 | `documented_capacity=500mAh`；`documented_type=polymer battery`；`capacity_on_schematic=null`；`battery_model=null` |
| 内存与 Flash | 正文中的 MCU 存储容量 | `part_number=STM32F030F4P6`；`documented_flash=16KB`；`documented_sram=4KB`；`capacity_on_schematic=null`；`external_memory_shown=false` |
| 时钟 | U5 时钟 | `PF0_OSC_IN=not connected`；`PF1_OSC_OUT=not connected`；`external_crystal_shown=false`；`clock_frequency=null` |
| 保护电路 | 外部接口保护 | `esd_shown=false`；`tvs_shown=false`；`fuse_shown=false`；`reverse_protection_shown=false`；`i2c_pullups_shown=false` |
| 其他事实 | 未展示功能分区 | `display_shown=false`；`touch_shown=false`；`audio_shown=false`；`rf_shown=false`；`external_storage_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x41`：产品正文给出 I2C 地址 0x41，但原理图没有 0x41、地址跳线或地址配置电阻，需由固件/协议确认。（证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 U5 与 J3 SDA/SCL 范围，无 0x41 标注）
- `power.documented-battery-capacity`：产品正文称内置 500mAh 聚合物电池，但原理图只显示 P1/BAT+ 接线，没有容量、型号或充电参数，因此 500mAh 需由电池标签/BOM 确认。（证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 P1 与 BAT+ 网络，无容量或电池型号）
- `memory.documented-mcu-capacity`：产品正文列出 16KB Flash 和 4KB SRAM；原理图确认 STM32F030F4P6 型号，但页面本身未标注 Flash/SRAM 容量，容量需由对应芯片 datasheet 复核。（证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 U5 仅标 STM32F030F4P6，无存储容量或外部存储器）
- `clock.mcu-clock-not-shown`：U5 PF0-OSC_IN 与 PF1-OSC_OUT 未连接，页面未显示外部晶振或时钟频率，实际时钟配置无法确认。（证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 A1 U5.2 PF0-OSC_IN 与 U5.3 PF1-OSC_OUT 无外部连线）
- `protection.interfaces-not-shown`：页面未展示 J1/J2/J3/P1 的 ESD、TVS、保险丝、反接或过流保护；I2C 也未画本地上拉，实际接口保护与总线依赖需进一步确认。（证据：图 df6864d1b3d9 / 第 1 页 / 第 1 页 J1/J2/J3/P1 与 SDA/SCL 路径，无保护器件或上拉电阻）
- `review.i2c-address`：请通过 M129 当前固件或通信协议确认 7-bit I2C 地址是否固定为 0x41。；原因：原理图未显示地址或硬件配置，地址属于固件行为。
- `review.battery-capacity`：请用当前量产 BOM 或电池标签确认 P1 所接电池的 500mAh 容量、型号与保护/充电要求。；原因：页面只画 BAT+ 和 GND，不含容量或电池管理信息。
- `review.mcu-memory`：请以 STM32F030F4P6 对应版本 datasheet/BOM 确认 16KB Flash 与 4KB SRAM。；原因：容量未在原理图中标注。
- `review.mcu-clock`：请确认 U5 使用的内部时钟源、频率和固件时钟配置。；原因：PF0/PF1 未接外部晶振，原理图不能说明内部时钟配置。
- `review.interface-protection`：请确认 M129 的 Grove、M5-Bus、电池与 I2C 接口是否在其他页面或 PCB 上实现 ESD、过流、反接保护和 I2C 上拉。；原因：当前页面未展示这些器件，不能区分省略与实际不存在。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `df6864d1b3d9fe2fe0c6a9c79c648b703c0ccc2237fe5f867af01b051b2c873a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/556/SCH_Module_HMI_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/HMI Module.md`

源文档 SHA-256：`85c8a6b93ad9433358bf294529dc2f22e496293881d0401b43dc031e72fd1828`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
