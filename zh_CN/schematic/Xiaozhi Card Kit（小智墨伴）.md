# Xiaozhi Card Kit（小智墨伴） 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Xiaozhi Card Kit（小智墨伴） |
| SKU | K146 |
| 产品 ID | `xiaozhi-card-kit-c26d860f8f0b` |
| 源文档 | `zh_CN/core/Xiaozhi_Card_Kit.md` |

## 概述

Xiaozhi Card Kit（小智墨伴）由 ESP32-S3-PICO-1-N8R8 主机和 USB-C 磁吸底座组成。主机集成 ES8311 音频编解码、模拟 MEMS 麦克风、AW8737A 扬声器功放、ML307 4G 模组与 nano SIM、SD NAND、电池充电与电量计、电子墨水屏及触摸 FPC；底座提供 USB-C、Grove、WS2812C RGB、复位/下载控制和两组主机连接网络。图面直接标注的器件与网络为确定事实，产品页给出的屏幕/触摸型号、容量、精确 4G 子型号、部分 I2C 地址、续航功耗和 Pogo 对应关系集中列为待确认。

## 检索关键词

`Xiaozhi Card Kit`、`小智墨伴`、`K146`、`ESP32-S3-PICO-1-N8R8`、`8MB Flash`、`8MB PSRAM`、`ES8311`、`0x18`、`MSM421A3729H9KRMC`、`AW8737A`、`TPS7A2033`、`JW5712`、`CH442E`、`ZDSD512MLGAAG`、`64MB SD NAND`、`BMI270 NC`、`ML307`、`ML307R-DL`、`SN74AVC4T245RSV`、`AW32001`、`BQ27220`、`GDEY027T91`、`FT6336U`、`AW32901FCR`、`LPW5209AB5F`、`SE8533X2-HF`、`WS2812C_2020`、`SYS_I2C_SCL`、`SYS_I2C_SDA`、`USB_SWC`、`EINK_BUSY`、`EINK_TP_RST`、`VCC_DOCK`、`MCU_BOOT`、`MCU_RST`、`MCU_SDA`、`MCU_SCL`、`HY2.0-4P`、`300mAh`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-S3-PICO-1-N8R8 | 主控制器，连接音频、SD NAND、电子墨水屏、触摸、4G、USB、按键和外部接口 | 图 6921177a261d / 第 1 页 / 网格 A2-C4，U5 ESP32-S3-PICO-1-N8R8 与全部 GPIO 网络 |
| J4 | IPEX4 | ESP32-S3 的 RF_50R 外部天线接口 | 图 6921177a261d / 第 1 页 / 网格 A1-A2，J4 IPEX4、RF_50R 与 U5 LNA_IN |
| U1 | ES8311 | I2C 控制的单声道音频编解码器 | 图 e82c146c5558 / 第 1 页 / 网格 A1-B3，Audio Codec 区 U1 ES8311 与 I2C ADDR(7bit):0x18 |
| U2 | MSM421A3729H9KRMC | 连接 ES8311 AUD_IN_P/AUD_IN_N 的模拟 MEMS 麦克风 | 图 e82c146c5558 / 第 1 页 / 网格 A4-A6，MEMS MIC 区 U2 与 MIC_OUT_P/AUD_IN_P/AUD_IN_N |
| U3 | AW8737A | VBAT_AUD 供电的差分扬声器功率放大器 | 图 e82c146c5558 / 第 1 页 / 网格 B4-C7，Speaker PA 区 U3 AW8737A、AUD_EN 与 SPK_VOP/SPK_VON |
| U4 | TPS7A2033 | VSYS 到 AVDD_3V3 的音频低噪声 LDO | 图 e82c146c5558 / 第 1 页 / 网格 B1-C3，Audio Low-noise LDO 区 U4 TPS7A2033 |
| U6 | CH442E | 在外部 USB 与 4G 模组 USB 之间选择 D+/D- 路径 | 图 6921177a261d / 第 1 页 / 网格 C1-C3，USB Analog Switch 区 U6 CH442E |
| U7 | JW5712 | VSYS 到 VDD_3V3 的主电源降压转换器 | 图 6921177a261d / 第 1 页 / 网格 D1-D5，Low-power DCDC 区 U7 JW5712、L4 与 VDD_3V3 |
| U8 | ZDSD512MLGAAG | SPI 接口 SD NAND 存储器 | 图 6921177a261d / 第 1 页 / 网格 C3-C5，SD NAND 区 U8 ZDSD512MLGAAG |
| U17/NC | BMI270 | 标为 NC 的可选 I2C IMU 位置 | 图 6921177a261d / 第 1 页 / 网格 C5-C7，IMU 区 U17/NC BMI270 |
| U9A/U9B/U9C | ML307 | 4G 模组，提供射频、SIM、USB、UART 和控制接口 | 图 3f12cfeafe97 / 第 1 页 / 网格 A1-D5，U9A/U9B/U9C ML307 三个原理图单元 |
| J5 | IPEX4 | ML307 ANT_MAIN 的 RF_50R 外部天线接口 | 图 3f12cfeafe97 / 第 1 页 / 网格 A1-A4，J5 IPEX4、匹配网络与 U9A ANT_MAIN |
| U10 | SN74AVC4T245RSV | VDD_3V3 与 VDDE_1V8 之间的 4 路 UART 电平转换器 | 图 3f12cfeafe97 / 第 1 页 / 网格 B5-B7，4G Module Voltage Translator 区 U10 |
| J1（主机） | NANO_SIM_HOLDER | 4G 模组 SIM0 接口 | 图 3f12cfeafe97 / 第 1 页 / 网格 C1-D4，SIM Cards 区 J1 NANO_SIM_HOLDER |
| U13 | AW32001 | VIN、VSYS、VBAT 三端电源与电池充电管理器 | 图 d68ecc1a2110 / 第 1 页 / 网格 A1-A4，Battery Charger 区 U13 AW32001 |
| U14 | BQ27220 | 带 0.01 欧姆分流器的电池电量计 | 图 d68ecc1a2110 / 第 1 页 / 网格 B1-B4，Battery Gauge 区 U14 BQ27220 与 R35 R010 |
| U12/U15/U16 | PESDALC10N5VU | SIM、USB 和外部 GPIO 接口 ESD 防护 | 图 3f12cfeafe97 / 第 1 页 / 网格 C3-D5，U12 保护 SIM0E_DAT/CLK/RST/DET; 图 d68ecc1a2110 / 第 1 页 / 网格 C1-D5，U15 保护 USB_D_EXT，U16 保护 GPIO0/EN/GPIO17/GPIO18 |
| J2/J3 | FPC 0.5mm 24P / FPC 0.5mm 6P | 电子墨水屏和触摸模组连接器 | 图 d1b36f06469f / 第 1 页 / 网格 A4-B5，J2 24P EINK FPC 与 J3 6P TOUCH FPC |
| J1（底座） | USB_C_16P_Horizontal | 底座 USB-C 供电和 USB 2.0 数据接口 | 图 c62bcc73ac90 / 第 1 页 / 网格 B1-B2，底座 J1 USB_C_16P_Horizontal、MCU_DP/MCU_DM 与 CC 下拉 |
| U4（底座） | AW32901FCR | VUSBIN 到 VBUS_VIN 的 USB 输入保护开关 | 图 c62bcc73ac90 / 第 1 页 / 网格 B2，底座 U4 AW32901FCR、VUSBIN 与 VBUS_VIN |
| U3（底座） | LPW5209AB5F | VBUS_VIN 到 VCC_DOCK 的 5V 电源转换器 | 图 c62bcc73ac90 / 第 1 页 / 网格 B3，底座 U3 LPW5209AB5F、VBUS_VIN 与 VCC_DOCK |
| U2（底座） | SE8533X2-HF | VBUS_VIN 到 VDD_3V3 的底座 LDO | 图 c62bcc73ac90 / 第 1 页 / 网格 B1-C2，底座 U2 SE8533X2-HF 与 VDD_3V3 |
| U1（底座） | WS2812C_2020 | 由 MCU_BOOT 输入数据的底座 RGB 指示灯 | 图 c62bcc73ac90 / 第 1 页 / 网格 C1-C2，底座 U1 WS2812C_2020、MCU_BOOT 与 Q2/Q3 供电控制 |
| J2（底座） | GROVE | 底座四针电源和 I2C 扩展接口 | 图 c62bcc73ac90 / 第 1 页 / 网格 C4，底座 J2 GROVE，GND/VBUS_VIN/MCU_SDA/MCU_SCL |

## 系统结构

### Xiaozhi Card Kit 硬件架构

主机以 U5 ESP32-S3-PICO-1-N8R8 为核心，连接 ES8311 音频链、ML307 4G/SIM、SD NAND、电池管理、EINK/TOUCH FPC 和外部 USB/GPIO；独立底座提供 USB-C、电源转换、WS2812C、按键、Grove 及 MCU_BOOT/MCU_RST/MCU_SDA/MCU_SCL/MCU_DP/MCU_DM/VCC_DOCK 接口网络。

- 参数与网络：`controller=U5 ESP32-S3-PICO-1-N8R8`；`audio=ES8311+MSM421A3729H9KRMC+AW8737A`；`cellular=ML307+nano SIM`；`storage=U8 SD NAND`；`display=J2 EINK FPC`；`base=USB-C+WS2812C+Grove+dock nets`
- 证据：图 6921177a261d / 第 1 页 / 主机第 2 页全图，U5、USB 开关、SD NAND、IMU 与主电源; 图 3f12cfeafe97 / 第 1 页 / 主机第 3 页全图，ML307、SIM、UART 和 USB; 图 c62bcc73ac90 / 第 1 页 / 底座完整单页，USB-C、电源、RGB、按键、Grove 和接口测试点

### ESP32-S3 主控制器

U5 器件值明确为 ESP32-S3-PICO-1-N8R8；GPIO1/2 承载系统 I2C，GPIO3-8 承载音频，GPIO9-12 连接 4G UART 和 IMU 中断，GPIO13/14 连接 SD NAND，GPIO15 控制 USB 选择，GPIO16 连接触摸中断，GPIO19/20 为原生 USB，GPIO21 为 ESP_INT，GPIO45-48 连接 EINK/SPI。

- 参数与网络：`reference=U5`；`part_number=ESP32-S3-PICO-1-N8R8`；`i2c=GPIO1 SCL,GPIO2 SDA`；`audio=GPIO3-GPIO8`；`cellular=GPIO9-GPIO11,GPIO15`；`storage=GPIO13,GPIO14,GPIO45,GPIO46`；`usb=GPIO19 D-,GPIO20 D+`；`eink=GPIO45-GPIO48`
- 证据：图 6921177a261d / 第 1 页 / 网格 A2-C4，U5 引脚与右侧全部网络标号

## 电源

### 主机 VDD_3V3 电源

U7 JW5712 以 VSYS 为 VIN，VSEL1/2/3 均接 VSYS，经 L4 MWTC201608S2R2 生成 VDD_3V3；该电源向 U5 和主机外设供电。

- 参数与网络：`converter=U7 JW5712`；`input=VSYS`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`select=VSEL1,VSEL2,VSEL3=VSYS`
- 证据：图 6921177a261d / 第 1 页 / 网格 D1-D5，U7/L4/C48-C52/C95-C96 与 VDD_3V3

### 音频 AVDD_3V3 低噪声电源

U4 TPS7A2033 的 IN/EN 接 VSYS，OUT 输出 AVDD_3V3；输入使用 C23 22 uF 和 C26 1 uF，输出使用 C29 1 uF、C30/C31 各 22 uF。

- 参数与网络：`regulator=U4 TPS7A2033`；`input=VSYS`；`enable=VSYS`；`output=AVDD_3V3`；`input_caps=C23 22uF,C26 1uF`；`output_caps=C29 1uF,C30 22uF,C31 22uF`
- 证据：图 e82c146c5558 / 第 1 页 / 网格 B1-C3，U4 TPS7A2033 与输入输出电容

### AW32001 电池充电与系统电源路径

U13 AW32001 的 IN 接 VIN，SYS 输出 VSYS，BAT 接 VBAT；SDA/SCL 接 SYS_I2C_SDA/SYS_I2C_SCL，INT 连接 AW_INT，VDD 网络为 AW_VDD，NTC 外围 R31/R32 均标 NC。

- 参数与网络：`charger=U13 AW32001`；`input=VIN`；`system_output=VSYS`；`battery=VBAT`；`bus=SYS_I2C_SDA/SYS_I2C_SCL`；`interrupt=AW_INT`；`ntc_population=R31/R32 NC`
- 证据：图 d68ecc1a2110 / 第 1 页 / 网格 A1-A4，U13 AW32001 与 VIN/VSYS/VBAT/I2C/NTC

### 电子墨水屏驱动电源

VDD_3V3 经 L5 WPN201610H100MT 和 FET6 SK2302AAT 驱动 D10/D11/D12 LMBR4010BST5G 网络，形成 EINK_RSE、EINK_VEE、EINK_VP 并送入 J2。

- 参数与网络：`input=VDD_3V3`；`inductor=L5 WPN201610H100MT`；`switch=FET6 SK2302AAT`；`diodes=D10,D11,D12 LMBR4010BST5G`；`outputs=EINK_RSE,EINK_VEE,EINK_VP`
- 证据：图 d1b36f06469f / 第 1 页 / 网格 A1-A5，EINK 电源区 L5/FET6/D10-D12 与 J2

### 底座 USB 输入保护与 VBUS_VIN

VUSBIN 接 U4 AW32901FCR 的三路 IN，三路 OUT 汇合为 VBUS_VIN；输入和输出分别使用 C7 1 uF 与 C8 1 uF，R13/R14 标为 NC。

- 参数与网络：`protector=U4 AW32901FCR`；`input=VUSBIN`；`output=VBUS_VIN`；`input_cap=C7 1uF`；`output_cap=C8 1uF`；`not_populated=R13,R14`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 B2，底座 U4/C7/C8/R13/R14

### 底座 VCC_DOCK 与 VDD_3V3

U3 LPW5209AB5F 以 VBUS_VIN 为 VIN 并输出 VCC_DOCK，EN 接输入侧；U2 SE8533X2-HF 以 VBUS_VIN 生成 VDD_3V3，VBUS_VIN 另通过 R1 10 kΩ 驱动绿色 LED2。

- 参数与网络：`dock_converter=U3 LPW5209AB5F`；`dock_input=VBUS_VIN`；`dock_output=VCC_DOCK`；`logic_regulator=U2 SE8533X2-HF`；`logic_output=VDD_3V3`；`power_led=R1+LED2 GREEN`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 B1-B3，底座 U2/U3、LED2、VDD_3V3 与 VCC_DOCK

## 接口

### 主机 USB 数据路径选择

U5 GPIO19/20 的 USB_D_N/USB_D_P 经 R14/R13 22 Ω 进入 U6 CH442E；U6 一组输出为 USB_D_EXT_N/P，另一组为 USB_D_4G_N/P，选择输入 IN 接 USB_SWC，USB_SWC 由 U5 GPIO15 驱动并由 R15 47 kΩ 下拉。

- 参数与网络：`switch=U6 CH442E`；`mcu=GPIO20 USB_D_P,GPIO19 USB_D_N`；`external=USB_D_EXT_P,USB_D_EXT_N`；`cellular=USB_D_4G_P,USB_D_4G_N`；`select=GPIO15 USB_SWC`；`series=R13=22R,R14=22R`
- 证据：图 6921177a261d / 第 1 页 / 网格 C1-C3，U6 CH442E、USB_D_P/N、EXT/4G 分支与 USB_SWC

### ML307 控制与状态网络

U9A RESET、PWR_ON/OFF、WAKEUP_OUT 分别接 ML_RST、ML_PWR、ML_WAKE；FET1/FET2/FET3 2N7002 将 ML_WAKE、ML_PWR_ESP、ML_RST_ESP 与模组侧网络连接，NETLIGHT/STATE 引出为 ML_NET_LED/ML_STATE_LED，相关 D2/D3/FET4/FET5 标为 NC。

- 参数与网络：`reset=ML_RST via FET3 from ML_RST_ESP`；`power=ML_PWR via FET2 from ML_PWR_ESP`；`wake=ML_WAKE via FET1 to ML_WAKE_ESP`；`status=ML_NET_LED,ML_STATE_LED`；`status_led_assembly=D2,D3,FET4,FET5 NC`
- 证据：图 3f12cfeafe97 / 第 1 页 / 网格 A3-A8，U9A 控制脚、FET1-FET5 与 LED 网络

### ML307 UART 与电平转换

U5 GPIO9/GPIO10/GPIO11 连接 ML_UART_E_RXD/ML_UART_E_DTR/ML_UART_E_TXD；U10 SN74AVC4T245RSV 以 VDD_3V3 为 VCCA、VDDE_1V8 为 VCCB，将其转换为 ML_UART_RXD/ML_UART_DTR/ML_UART_TXD 接 U9C UART0。

- 参数与网络：`mcu_rx=GPIO9 ML_UART_E_RXD`；`mcu_dtr=GPIO10 ML_UART_E_DTR`；`mcu_tx=GPIO11 ML_UART_E_TXD`；`translator=U10 SN74AVC4T245RSV`；`module=ML_UART_RXD,ML_UART_DTR,ML_UART_TXD`；`rails=VDD_3V3/VDDE_1V8`
- 证据：图 6921177a261d / 第 1 页 / 网格 A2-B4，U5 GPIO9-GPIO11; 图 3f12cfeafe97 / 第 1 页 / 网格 B4-B7，U9C UART0 与 U10 电平转换器

### ML307 USB 接口

U9C USB_DP/USB_DM 分别连接 USB_D_4G_P/USB_D_4G_N，USB_VBUS 经 R23 0 Ω 接 USB_SWC；数据对接入 U6 CH442E 的 4G 分支。

- 参数与网络：`module_dp=U9C USB_DP -> USB_D_4G_P`；`module_dm=U9C USB_DM -> USB_D_4G_N`；`vbus=USB_SWC via R23 0R`；`switch=U6 CH442E`
- 证据：图 3f12cfeafe97 / 第 1 页 / 网格 B3-B5，U9C USB_VBUS/USB_DP/USB_DM 与 R23; 图 6921177a261d / 第 1 页 / 网格 C1-C3，U6 USB_D_4G_P/N 分支

### nano SIM 接口

J1 NANO_SIM_HOLDER 的 VDD、RST、CLK、DAT、CD 分别连接 SIM0_VCC、SIM0E_RST、SIM0E_CLK、SIM0E_DAT、SIM0_DET；U9B 提供 SIM0/SIM1 两组接口，其中实际连接器使用 SIM0 路径。

- 参数与网络：`connector=J1 NANO_SIM_HOLDER`；`supply=SIM0_VCC`；`reset=SIM0E_RST`；`clock=SIM0E_CLK`；`data=SIM0E_DAT`；`detect=SIM0_DET`；`module_unit=U9B`
- 证据：图 3f12cfeafe97 / 第 1 页 / 网格 C1-D5，U9B、J1、U12 与 SIM0 网络

### 主机按键双中断输入

S1 SMT_SW_TACTILE 按下时将公共节点接 GND，ESP_INT 和 AW_INT 分别通过 D5/D6 1N5819 接到该节点；ESP_INT 连接 U5 GPIO21，AW_INT 连接 U13 INT。

- 参数与网络：`button=S1 SMT_SW_TACTILE`；`mcu_interrupt=ESP_INT via D5 1N5819 to GPIO21`；`charger_interrupt=AW_INT via D6 1N5819 to U13 INT`；`active_level=GND when pressed`
- 证据：图 d68ecc1a2110 / 第 1 页 / 网格 C3-C4，Button 区 D5/D6/S1/ESP_INT/AW_INT; 图 6921177a261d / 第 1 页 / 网格 B2-B4，U5 GPIO21 ESP_INT

### 电子墨水屏 FPC 信号

J2 24P FPC 引出 EINK_GDR、EINK_RSE、EINK_BUSY、EINK_TP_RST、EINK_DC、EINK_CS、SPI_SCK、SPI_MOSI、VDD_3V3、EINK_VP、EINK_VEE 和 GND；控制端在 U5 侧连接 GPIO45/46/47/48 及 EINK_BUSY/EINK_TP_RST 网络。

- 参数与网络：`connector=J2 FPC 0.5mm 24P`；`spi=SPI_SCK,SPI_MOSI,EINK_CS`；`control=EINK_DC,EINK_BUSY,EINK_TP_RST`；`drive=EINK_GDR,EINK_RSE`；`rails=VDD_3V3,EINK_VP,EINK_VEE`
- 证据：图 d1b36f06469f / 第 1 页 / 网格 A4-A5，J2 24P FPC 全部 EINK/SPI/电源网络; 图 6921177a261d / 第 1 页 / 网格 B2-C4，U5 EINK_BUSY/EINK_TP_RST/EINK_DC/EINK_CS/SPI_SCK/SPI_MOSI

### 触摸模组 FPC

J3 6P FPC 的 1-6 脚依次连接 GND、EINK_TP_RST、TP_INT、SYS_I2C_SDA、SYS_I2C_SCL、VDD_3V3；TP_INT 接 U5 GPIO16，EINK_TP_RST 接 U5 对应屏幕复位网络。

- 参数与网络：`pinout=1:GND,2:EINK_TP_RST,3:TP_INT,4:SYS_I2C_SDA,5:SYS_I2C_SCL,6:VDD_3V3`；`interrupt=GPIO16 TP_INT`；`reset=EINK_TP_RST`
- 证据：图 d1b36f06469f / 第 1 页 / 网格 B1-B4，J3 6P TOUCH FPC; 图 6921177a261d / 第 1 页 / 网格 B2-B4，U5 GPIO16 TP_INT 与 EINK_TP_RST

### 主机外部 USB 与 GPIO 网络

主机将 USB_D_EXT_P/N 引至 U15 ESD 防护，并将 ESP_EN、GPIO0、GPIO17、GPIO18 分别经 R36 220 Ω、R37 220 Ω、R38 51 Ω、R39 51 Ω 形成 ESP_EN_EXT、GPIO0_EXT、GPIO17_EXT、GPIO18_EXT，再由 U16 保护。

- 参数与网络：`usb=USB_D_EXT_P,USB_D_EXT_N`；`reset=ESP_EN_EXT via R36 220R`；`boot=GPIO0_EXT via R37 220R`；`data=GPIO17_EXT via R38 51R,GPIO18_EXT via R39 51R`；`esd=U15,U16 PESDALC10N5VU`
- 证据：图 d68ecc1a2110 / 第 1 页 / 网格 C1-D5，USB ESD 与 Interface 区 R36-R39/U15/U16

### 底座 USB-C 输入

底座 J1 USB_C_16P_Horizontal 将 A6/B6 并接 MCU_DP、A7/B7 并接 MCU_DM，CC1/CC2 分别经 R2/R3 5.1 kΩ 下拉至 GND；VBUS 经 FU1 SMD0805-200-6V 形成 VUSBIN。

- 参数与网络：`connector=J1 USB_C_16P_Horizontal`；`d_plus=A6,B6 MCU_DP`；`d_minus=A7,B7 MCU_DM`；`cc=R2=5.1k,R3=5.1k`；`power=VBUS -> FU1 -> VUSBIN`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 B1-B2，底座 J1/FU1/R2/R3 与 MCU_DP/MCU_DM

### 底座 WS2812C RGB

U1 WS2812C_2020 的 DIN 接 MCU_BOOT，VDD 经 Q2 CJ2101 高边路径供电；Q3 2N7002W 的控制端接 MCU_RST，R8/R9/R10 和 C1 构成外围偏置与滤波。

- 参数与网络：`rgb=U1 WS2812C_2020`；`data=MCU_BOOT`；`power_switch=Q2 CJ2101`；`control=MCU_RST via Q3 2N7002W`；`supply=VDD_3V3`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 C1-C2，底座 Q2/Q3/U1/R8-R10/C1

### 底座 Grove 接口

J2 GROVE 的 1-4 脚依次为 GND、VBUS_VIN、MCU_SDA、MCU_SCL，向外提供底座输入电源和两线通信网络。

- 参数与网络：`pinout=1:GND,2:VBUS_VIN,3:MCU_SDA,4:MCU_SCL`；`power=VBUS_VIN`；`data=MCU_SDA,MCU_SCL`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 C4，底座 J2 GROVE 1-4 脚

## 总线

### SYS_I2C_SCL/SYS_I2C_SDA

U5 GPIO1/2 分别连接 SYS_I2C_SCL/SYS_I2C_SDA；总线连接 ES8311、AW32001、BQ27220、触摸 FPC，并连接标为 U17/NC 的 BMI270，R8/R10 各 2.2 kΩ 上拉至 VDD_3V3。

- 参数与网络：`scl=GPIO1 SYS_I2C_SCL`；`sda=GPIO2 SYS_I2C_SDA`；`pullups=R8=2.2k,R10=2.2k`；`devices=ES8311,AW32001,BQ27220,J3 touch,U17/NC BMI270`
- 证据：图 6921177a261d / 第 1 页 / 网格 A2-C7，U5 GPIO1/2、R8/R10 与 U17/NC; 图 d68ecc1a2110 / 第 1 页 / 网格 A1-B4，U13/U14 的 SYS_I2C_SCL/SDA; 图 d1b36f06469f / 第 1 页 / 网格 B1-B4，J3 触摸 FPC 的 SYS_I2C_SDA/SCL

## 总线地址

### ES8311 I2C 地址

Audio Codec 区在 U1 ES8311 上方明确标注 I2C ADDR(7bit): 0x18，SCL/SDA 接 SYS_I2C_SCL/SYS_I2C_SDA。

- 参数与网络：`reference=U1`；`part_number=ES8311`；`address_7bit=0x18`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`
- 证据：图 e82c146c5558 / 第 1 页 / 网格 A1-A3，U1 上方 I2C ADDR(7bit): 0x18 注记

## 时钟

### ES8311 音频时钟

U5 GPIO3、GPIO4、GPIO6 分别连接 AUD_MCLK、AUD_BCLK、AUD_LRCK；AUD_MCLK 经 R1 22 Ω 接 U1 MCLK，AUD_BCLK/AUD_LRCK 直连 U1 SCLK/LRCK。

- 参数与网络：`mclk=GPIO3 AUD_MCLK via R1 22R`；`bit_clock=GPIO4 AUD_BCLK`；`word_clock=GPIO6 AUD_LRCK`；`codec=U1 ES8311`
- 证据：图 6921177a261d / 第 1 页 / 网格 A2-B4，U5 GPIO3/GPIO4/GPIO6 音频网络; 图 e82c146c5558 / 第 1 页 / 网格 A1-A3，U1 MCLK/SCLK/LRCK 与 R1

## 复位

### ESP_EN 复位网络

U5 CHIP_PU 连接 ESP_EN，R12 10 kΩ 将 ESP_EN 上拉至 VDD_3V3，C38 1 uF 将该网络连接到 GND；ESP_EN 另经 R36 220 Ω 引出为 ESP_EN_EXT。

- 参数与网络：`controller_pin=U5 CHIP_PU`；`net=ESP_EN`；`pullup=R12 10k`；`capacitor=C38 1uF`；`external=R36 220R -> ESP_EN_EXT`
- 证据：图 6921177a261d / 第 1 页 / 网格 B5-B6，RESET 区 R12/C38/ESP_EN; 图 d68ecc1a2110 / 第 1 页 / 网格 D1-D4，R36 ESP_EN 至 ESP_EN_EXT

### 底座按键与复位/下载网络

底座 S1 将 SYS_SW 接到 VDD_3V3，Q1A/Q1B 2N7002DW、D1/D2 1N5819WS、R11 220 kΩ 与 C5 4.7 uF 连接 MCU_RST 和 MCU_BOOT；两路网络分别引出至 TP6 和 TP5。

- 参数与网络：`button=S1 SW`；`switch_node=SYS_SW`；`transistors=Q1A/Q1B 2N7002DW`；`diodes=D1,D2 1N5819WS`；`reset=MCU_RST TP6`；`boot=MCU_BOOT TP5`
- 证据：图 c62bcc73ac90 / 第 1 页 / 网格 C2-C3，底座 S1/Q1A/Q1B/D1/D2/R11/C5 与 MCU_RST/MCU_BOOT

## 保护电路

### 主机外部接口 ESD 防护

U12 PESDALC10N5VU 保护 SIM0E_DAT/CLK/RST/DET，U15 同型号器件保护 USB_D_EXT_P/N，U16 保护 GPIO0_EXT、ESP_EN_EXT、GPIO17_EXT、GPIO18_EXT；D4/NC、D7/NC 为未装配 TVS 位置。

- 参数与网络：`sim=U12 PESDALC10N5VU`；`usb=U15 PESDALC10N5VU`；`external_gpio=U16 PESDALC10N5VU`；`not_populated=D4/NC,D7/NC`
- 证据：图 3f12cfeafe97 / 第 1 页 / 网格 C3-D5，U12 与 D4/NC; 图 d68ecc1a2110 / 第 1 页 / 网格 C1-D5，U15/U16 与 D7/NC

## 存储

### SD NAND SPI 连接

U8 ZDSD512MLGAAG 由 VDD_3V3 供电，CLK 接 SPI_SCK，CMD/DI 接 SPI_MOSI，DAT0/DO 接 SD_MISO，DAT3/CS 接 SD_CS；R24/R42/R43/R44/R45/R46 均为 10 kΩ 上拉。

- 参数与网络：`device=U8 ZDSD512MLGAAG`；`clock=SPI_SCK`；`mosi=SPI_MOSI`；`miso=SD_MISO`；`chip_select=SD_CS`；`supply=VDD_3V3`
- 证据：图 6921177a261d / 第 1 页 / 网格 C3-C5，U8 SD NAND 与 R24/R42-R46

## 音频

### ES8311 数字音频数据与使能

U5 GPIO5 连接 AUD_DOUT 并接 U1 ASDOUT，GPIO7 连接 AUD_DIN 并接 U1 DSDIN，GPIO8 连接 AUD_EN；U1 差分输出 AUD_OUT_P/AUD_OUT_N 进入 U3 功放输入网络。

- 参数与网络：`codec_to_mcu=U1 ASDOUT/AUD_DOUT -> GPIO5`；`mcu_to_codec=GPIO7/AUD_DIN -> U1 DSDIN`；`enable=GPIO8 AUD_EN`；`analog_output=AUD_OUT_P,AUD_OUT_N`
- 证据：图 6921177a261d / 第 1 页 / 网格 A2-B4，U5 GPIO5/GPIO7/GPIO8; 图 e82c146c5558 / 第 1 页 / 网格 A1-C7，U1 数字接口与 U1 OUTP/OUTN 至 U3

### MEMS 麦克风输入

U2 MSM421A3729H9KRMC 由 AVDD_3V3 经 FB1 供电，OUT 经 C3 1 uF 形成 AUD_IN_P，GND 参考经 C8 1 uF 形成 AUD_IN_N，两路接入 U1 ES8311 MIC1P/MIC1N。

- 参数与网络：`microphone=U2 MSM421A3729H9KRMC`；`supply=AVDD_3V3 via FB1`；`positive=OUT-C3-AUD_IN_P`；`negative=GND-C8-AUD_IN_N`；`codec_inputs=U1 MIC1P/MIC1N`
- 证据：图 e82c146c5558 / 第 1 页 / 网格 A4-A6，U2/FB1/C3/C8 与 U1 AUD_IN_P/N

### AW8737A 扬声器功放

U1 AUD_OUT_P/AUD_OUT_N 经 C14/C19 与 R2/R3 形成 AMP_IN_P/AMP_IN_N，接入 U3 AW8737A；U3 由 VBAT_AUD 供电、AUD_EN 控制 SHDN，差分输出经 FB2/FB3 形成 SPK_VOP/SPK_VON。

- 参数与网络：`amplifier=U3 AW8737A`；`input=AMP_IN_P,AMP_IN_N`；`enable=AUD_EN`；`supply=VBAT_AUD`；`output=SPK_VOP,SPK_VON`
- 证据：图 e82c146c5558 / 第 1 页 / 网格 B4-C7，Speaker PA 区完整差分输入、U3 与输出滤波

## 传感器

### BMI270 预留位置

IMU 区器件标号明确写为 U17/NC、器件值为 BMI270；SCx/SDx 接 SYS_I2C_SCL/SYS_I2C_SDA，INT1 接 IMU_INT，SDO 接 GND，INT2、ASDx、ASCx 未连接。

- 参数与网络：`reference=U17/NC`；`part_number=BMI270`；`assembly=NC`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`interrupt=IMU_INT`；`sdo=GND`
- 证据：图 6921177a261d / 第 1 页 / 网格 C5-C7，U17/NC BMI270 与 I2C/IMU_INT/SDO

## 射频

### ESP32-S3 射频接口

U5 LNA_IN 通过 ESP_LNA、R7 1 nH 及 C35/C36 匹配预留网络连接 J4 IPEX4，主信号网络标为 RF_50R。

- 参数与网络：`controller=U5 LNA_IN`；`connector=J4 IPEX4`；`net=RF_50R`；`series=R7 1nH`；`shunt=C35 NC,C36 1.8pF`
- 证据：图 6921177a261d / 第 1 页 / 网格 A1-A2，J4/R7/C35/C36 至 U5 LNA_IN

### ML307 4G 模组射频与供电

U9A/U9B/U9C 器件值均为 ML307；U9A ANT_MAIN 通过 RF_50R 匹配网络连接 J5 IPEX4，VBAT 引脚接 VDD_ML，VDD_EXT 输出 VDDE_1V8。

- 参数与网络：`module=U9A/U9B/U9C ML307`；`antenna=ANT_MAIN -> RF_50R -> J5 IPEX4`；`main_supply=VDD_ML`；`io_supply=VDD_EXT -> VDDE_1V8`
- 证据：图 3f12cfeafe97 / 第 1 页 / 网格 A1-B4，J5/U9A/VDD_ML/VDDE_1V8 与 U9C ML307

## 调试与烧录

### 主机与底座测试点

主机图引出 TP1/TP3/TP6/TP7 等 MCU 侧网络以及 TP13-TP19、TP22-TP28 等 ML307 电源、UART、USB 和 GPIO 测试点；底座 TP1-TP12 覆盖 VBUS/GND、MCU_DP/DM、MCU_BOOT、MCU_RST、MCU_SDA/SCL、VCC_DOCK。

- 参数与网络：`mcu=TP1,TP3,TP6,TP7,TP8,TP9,TP10,TP11,TP12,TP21`；`cellular=TP13-TP19,TP22-TP28`；`base=TP1-TP12`；`base_signals=MCU_DP,MCU_DM,MCU_BOOT,MCU_RST,MCU_SDA,MCU_SCL,VCC_DOCK,GND`
- 证据：图 6921177a261d / 第 1 页 / 主机第 2 页 U5/U6/U7 周边 TP1/TP3/TP6-TP12/TP21; 图 3f12cfeafe97 / 第 1 页 / 主机第 3 页 U9 周边 TP13-TP19/TP22-TP28; 图 c62bcc73ac90 / 第 1 页 / 底座完整单页 TP1-TP12

## 模拟电路

### BQ27220 电流与电量采样

U14 BQ27220 的 SRP/SRN 跨接 R35 R010/1% 分流器，SRP 侧为 VBAT_IN、SRN 侧为 VBAT；SDA/SCL 接系统 I2C，GPOUT 通过 R47 10 kΩ 上拉至 BQ_VDD，BAT/BIN 与电池网络连接。

- 参数与网络：`gauge=U14 BQ27220`；`shunt=R35 R010/1%`；`positive=VBAT_IN`；`negative=VBAT`；`bus=SYS_I2C_SDA/SYS_I2C_SCL`；`interrupt=GAUGE_GPOUT`；`supply=BQ_VDD`
- 证据：图 d68ecc1a2110 / 第 1 页 / 网格 B1-B4，U14 BQ27220、R35、VBAT_IN/VBAT 与 GPOUT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Xiaozhi Card Kit 硬件架构 | `controller=U5 ESP32-S3-PICO-1-N8R8`；`audio=ES8311+MSM421A3729H9KRMC+AW8737A`；`cellular=ML307+nano SIM`；`storage=U8 SD NAND`；`display=J2 EINK FPC`；`base=USB-C+WS2812C+Grove+dock nets` |
| 系统结构 | ESP32-S3 主控制器 | `reference=U5`；`part_number=ESP32-S3-PICO-1-N8R8`；`i2c=GPIO1 SCL,GPIO2 SDA`；`audio=GPIO3-GPIO8`；`cellular=GPIO9-GPIO11,GPIO15`；`storage=GPIO13,GPIO14,GPIO45,GPIO46`；`usb=GPIO19 D-,GPIO20 D+`；`eink=GPIO45-GPIO48` |
| 射频 | ESP32-S3 射频接口 | `controller=U5 LNA_IN`；`connector=J4 IPEX4`；`net=RF_50R`；`series=R7 1nH`；`shunt=C35 NC,C36 1.8pF` |
| 电源 | 主机 VDD_3V3 电源 | `converter=U7 JW5712`；`input=VSYS`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`select=VSEL1,VSEL2,VSEL3=VSYS` |
| 复位 | ESP_EN 复位网络 | `controller_pin=U5 CHIP_PU`；`net=ESP_EN`；`pullup=R12 10k`；`capacitor=C38 1uF`；`external=R36 220R -> ESP_EN_EXT` |
| 总线 | SYS_I2C_SCL/SYS_I2C_SDA | `scl=GPIO1 SYS_I2C_SCL`；`sda=GPIO2 SYS_I2C_SDA`；`pullups=R8=2.2k,R10=2.2k`；`devices=ES8311,AW32001,BQ27220,J3 touch,U17/NC BMI270` |
| 总线地址 | ES8311 I2C 地址 | `reference=U1`；`part_number=ES8311`；`address_7bit=0x18`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA` |
| 时钟 | ES8311 音频时钟 | `mclk=GPIO3 AUD_MCLK via R1 22R`；`bit_clock=GPIO4 AUD_BCLK`；`word_clock=GPIO6 AUD_LRCK`；`codec=U1 ES8311` |
| 音频 | ES8311 数字音频数据与使能 | `codec_to_mcu=U1 ASDOUT/AUD_DOUT -> GPIO5`；`mcu_to_codec=GPIO7/AUD_DIN -> U1 DSDIN`；`enable=GPIO8 AUD_EN`；`analog_output=AUD_OUT_P,AUD_OUT_N` |
| 音频 | MEMS 麦克风输入 | `microphone=U2 MSM421A3729H9KRMC`；`supply=AVDD_3V3 via FB1`；`positive=OUT-C3-AUD_IN_P`；`negative=GND-C8-AUD_IN_N`；`codec_inputs=U1 MIC1P/MIC1N` |
| 音频 | AW8737A 扬声器功放 | `amplifier=U3 AW8737A`；`input=AMP_IN_P,AMP_IN_N`；`enable=AUD_EN`；`supply=VBAT_AUD`；`output=SPK_VOP,SPK_VON` |
| 电源 | 音频 AVDD_3V3 低噪声电源 | `regulator=U4 TPS7A2033`；`input=VSYS`；`enable=VSYS`；`output=AVDD_3V3`；`input_caps=C23 22uF,C26 1uF`；`output_caps=C29 1uF,C30 22uF,C31 22uF` |
| 存储 | SD NAND SPI 连接 | `device=U8 ZDSD512MLGAAG`；`clock=SPI_SCK`；`mosi=SPI_MOSI`；`miso=SD_MISO`；`chip_select=SD_CS`；`supply=VDD_3V3` |
| 接口 | 主机 USB 数据路径选择 | `switch=U6 CH442E`；`mcu=GPIO20 USB_D_P,GPIO19 USB_D_N`；`external=USB_D_EXT_P,USB_D_EXT_N`；`cellular=USB_D_4G_P,USB_D_4G_N`；`select=GPIO15 USB_SWC`；`series=R13=22R,R14=22R` |
| 传感器 | BMI270 预留位置 | `reference=U17/NC`；`part_number=BMI270`；`assembly=NC`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`interrupt=IMU_INT`；`sdo=GND` |
| 射频 | ML307 4G 模组射频与供电 | `module=U9A/U9B/U9C ML307`；`antenna=ANT_MAIN -> RF_50R -> J5 IPEX4`；`main_supply=VDD_ML`；`io_supply=VDD_EXT -> VDDE_1V8` |
| 接口 | ML307 控制与状态网络 | `reset=ML_RST via FET3 from ML_RST_ESP`；`power=ML_PWR via FET2 from ML_PWR_ESP`；`wake=ML_WAKE via FET1 to ML_WAKE_ESP`；`status=ML_NET_LED,ML_STATE_LED`；`status_led_assembly=D2,D3,FET4,FET5 NC` |
| 接口 | ML307 UART 与电平转换 | `mcu_rx=GPIO9 ML_UART_E_RXD`；`mcu_dtr=GPIO10 ML_UART_E_DTR`；`mcu_tx=GPIO11 ML_UART_E_TXD`；`translator=U10 SN74AVC4T245RSV`；`module=ML_UART_RXD,ML_UART_DTR,ML_UART_TXD`；`rails=VDD_3V3/VDDE_1V8` |
| 接口 | ML307 USB 接口 | `module_dp=U9C USB_DP -> USB_D_4G_P`；`module_dm=U9C USB_DM -> USB_D_4G_N`；`vbus=USB_SWC via R23 0R`；`switch=U6 CH442E` |
| 接口 | nano SIM 接口 | `connector=J1 NANO_SIM_HOLDER`；`supply=SIM0_VCC`；`reset=SIM0E_RST`；`clock=SIM0E_CLK`；`data=SIM0E_DAT`；`detect=SIM0_DET`；`module_unit=U9B` |
| 保护电路 | 主机外部接口 ESD 防护 | `sim=U12 PESDALC10N5VU`；`usb=U15 PESDALC10N5VU`；`external_gpio=U16 PESDALC10N5VU`；`not_populated=D4/NC,D7/NC` |
| 电源 | AW32001 电池充电与系统电源路径 | `charger=U13 AW32001`；`input=VIN`；`system_output=VSYS`；`battery=VBAT`；`bus=SYS_I2C_SDA/SYS_I2C_SCL`；`interrupt=AW_INT`；`ntc_population=R31/R32 NC` |
| 模拟电路 | BQ27220 电流与电量采样 | `gauge=U14 BQ27220`；`shunt=R35 R010/1%`；`positive=VBAT_IN`；`negative=VBAT`；`bus=SYS_I2C_SDA/SYS_I2C_SCL`；`interrupt=GAUGE_GPOUT`；`supply=BQ_VDD` |
| 接口 | 主机按键双中断输入 | `button=S1 SMT_SW_TACTILE`；`mcu_interrupt=ESP_INT via D5 1N5819 to GPIO21`；`charger_interrupt=AW_INT via D6 1N5819 to U13 INT`；`active_level=GND when pressed` |
| 接口 | 电子墨水屏 FPC 信号 | `connector=J2 FPC 0.5mm 24P`；`spi=SPI_SCK,SPI_MOSI,EINK_CS`；`control=EINK_DC,EINK_BUSY,EINK_TP_RST`；`drive=EINK_GDR,EINK_RSE`；`rails=VDD_3V3,EINK_VP,EINK_VEE` |
| 电源 | 电子墨水屏驱动电源 | `input=VDD_3V3`；`inductor=L5 WPN201610H100MT`；`switch=FET6 SK2302AAT`；`diodes=D10,D11,D12 LMBR4010BST5G`；`outputs=EINK_RSE,EINK_VEE,EINK_VP` |
| 接口 | 触摸模组 FPC | `pinout=1:GND,2:EINK_TP_RST,3:TP_INT,4:SYS_I2C_SDA,5:SYS_I2C_SCL,6:VDD_3V3`；`interrupt=GPIO16 TP_INT`；`reset=EINK_TP_RST` |
| 接口 | 主机外部 USB 与 GPIO 网络 | `usb=USB_D_EXT_P,USB_D_EXT_N`；`reset=ESP_EN_EXT via R36 220R`；`boot=GPIO0_EXT via R37 220R`；`data=GPIO17_EXT via R38 51R,GPIO18_EXT via R39 51R`；`esd=U15,U16 PESDALC10N5VU` |
| 接口 | 底座 USB-C 输入 | `connector=J1 USB_C_16P_Horizontal`；`d_plus=A6,B6 MCU_DP`；`d_minus=A7,B7 MCU_DM`；`cc=R2=5.1k,R3=5.1k`；`power=VBUS -> FU1 -> VUSBIN` |
| 电源 | 底座 USB 输入保护与 VBUS_VIN | `protector=U4 AW32901FCR`；`input=VUSBIN`；`output=VBUS_VIN`；`input_cap=C7 1uF`；`output_cap=C8 1uF`；`not_populated=R13,R14` |
| 电源 | 底座 VCC_DOCK 与 VDD_3V3 | `dock_converter=U3 LPW5209AB5F`；`dock_input=VBUS_VIN`；`dock_output=VCC_DOCK`；`logic_regulator=U2 SE8533X2-HF`；`logic_output=VDD_3V3`；`power_led=R1+LED2 GREEN` |
| 接口 | 底座 WS2812C RGB | `rgb=U1 WS2812C_2020`；`data=MCU_BOOT`；`power_switch=Q2 CJ2101`；`control=MCU_RST via Q3 2N7002W`；`supply=VDD_3V3` |
| 复位 | 底座按键与复位/下载网络 | `button=S1 SW`；`switch_node=SYS_SW`；`transistors=Q1A/Q1B 2N7002DW`；`diodes=D1,D2 1N5819WS`；`reset=MCU_RST TP6`；`boot=MCU_BOOT TP5` |
| 接口 | 底座 Grove 接口 | `pinout=1:GND,2:VBUS_VIN,3:MCU_SDA,4:MCU_SCL`；`power=VBUS_VIN`；`data=MCU_SDA,MCU_SCL` |
| 调试与烧录 | 主机与底座测试点 | `mcu=TP1,TP3,TP6,TP7,TP8,TP9,TP10,TP11,TP12,TP21`；`cellular=TP13-TP19,TP22-TP28`；`base=TP1-TP12`；`base_signals=MCU_DP,MCU_DM,MCU_BOOT,MCU_RST,MCU_SDA,MCU_SCL,VCC_DOCK,GND` |
| 内存与 Flash | ESP32-S3 Flash 与 PSRAM 容量 | `part_number=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB`；`schematic_capacity_text=null` |
| 存储 | SD NAND 容量 | `device=U8 ZDSD512MLGAAG`；`documented_capacity=64MB`；`schematic_capacity_text=null`；`usable_capacity=null` |
| 核心器件 | 电子墨水屏型号与显示规格 | `documented_model=GDEY027T91`；`documented_size=2.7 inch`；`documented_resolution=176x264`；`documented_gray=1-bit monochrome`；`schematic_model=null` |
| 传感器 | 触摸控制器型号与地址 | `documented_controller=FT6336U`；`documented_address=0x38`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`interrupt=TP_INT`；`reset=EINK_TP_RST`；`schematic_controller=null` |
| 总线地址 | AW32001 与 BQ27220 I2C 地址 | `documented_charger=AW32001 0x49`；`documented_gauge=BQ27220 0x55`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`schematic_addresses=null` |
| 射频 | 4G 模组精确子型号与网络能力 | `schematic_model=ML307`；`documented_model=ML307R-DL`；`documented_class=LTE Cat.1`；`documented_fdd=B1/B3/B5/B8`；`documented_tdd=B34/B38/B39/B40/B41`；`hardware_variant_marking=null` |
| 电源 | 内置电池规格 | `documented_capacity=300mAh`；`documented_voltage=3.7V`；`charger=U13 AW32001`；`gauge=U14 BQ27220`；`cell_part_number=null`；`protection=null`；`temperature=null` |
| 电源 | 续航与整机功耗 | `documented_4g_runtime=3h18min`；`documented_wifi_runtime=3h15min`；`documented_dock_active=5.12V@388.50mA`；`documented_external_active=5V@177.11mA`；`documented_4g_sleep=4.27V@46.28mA`；`documented_off=4.26V@15.28uA`；`test_conditions_complete=false` |
| 接口 | 主机与底座 Pogo Pin 对应关系 | `documented_port1=5V:VCC_DOCK,DP:MCU_DP,DM:MCU_DM,GND:GND`；`documented_port2=GPIO0:MCU_BOOT,EN:MCU_RST,GPIO17:MCU_SDA,GPIO18:MCU_SCL`；`main_nets=USB_D_EXT_P/N,GPIO0_EXT,ESP_EN_EXT,GPIO17_EXT,GPIO18_EXT`；`base_nets=VCC_DOCK,MCU_DP/DM,MCU_BOOT/RST/SDA/SCL`；`schematic_connector=null` |

## 待确认事项

- `memory.soc-capacity`：源文档把 U5 写为 ESP32-S3-PICO-1-N8R8，并列出 8MB Flash 与 8MB PSRAM；图面确认完整器件后缀，但没有独立容量文字或存储测试结果。（证据：图 6921177a261d / 第 1 页 / 网格 A2-C4，U5 仅以器件值 ESP32-S3-PICO-1-N8R8 表示容量后缀）
- `storage.documented-capacity`：源文档称板载 64MB SD NAND，原理图确认 U8 ZDSD512MLGAAG 和 SPI 网络，但页面没有直接写出 64MB 或可用容量。（证据：图 6921177a261d / 第 1 页 / 网格 C3-C5，U8 SD NAND 仅标器件型号和 SPI 网络）
- `component.display-panel`：源文档给出 GDEY027T91、2.7 英寸、176 x 264、1-bit 黑白显示；原理图只绘制 J2 24P FPC、EINK 信号和驱动电源，没有面板型号、尺寸、分辨率或灰度注记。（证据：图 d1b36f06469f / 第 1 页 / 网格 A1-A5，J2 EINK FPC 与电源电路无面板型号或显示规格）
- `sensor.touch-controller`：源文档给出 FT6336U 和 7 位地址 0x38；原理图只绘制 J3 6P 触摸 FPC 的 I2C、TP_INT、EINK_TP_RST 和 3.3V 网络，没有控制器器件或地址选择。（证据：图 d1b36f06469f / 第 1 页 / 网格 B1-B4，J3 TOUCH 仅为 6P FPC，无 FT6336U 或 0x38 文字）
- `address.power-devices`：源文档给出 AW32001=0x49、BQ27220=0x55；原理图确认两者连接 SYS_I2C_SCL/SYS_I2C_SDA，但本页没有地址文字或地址选择说明。（证据：图 d68ecc1a2110 / 第 1 页 / 网格 A1-B4，U13/U14 的 I2C 连接区域无地址注记）
- `rf.cellular-variant`：源文档称模组为 ML307R-DL、LTE Cat.1，并列出运营商和 LTE 频段；原理图所有单元仅标 ML307，没有 R-DL 后缀、Cat.1、频段或运营商兼容性文字。（证据：图 3f12cfeafe97 / 第 1 页 / U9A/U9B/U9C 均仅标 ML307，无精确子型号与频段表）
- `power.battery-spec`：源文档称内置电池为 300mAh @3.7V；原理图确认 VBAT/VBAT_IN、AW32001 与 BQ27220 路径，但没有电芯连接器、料号、容量、电压平台、保护板或温度参数。（证据：图 d68ecc1a2110 / 第 1 页 / 网格 A1-B4，电池充电与电量计电路无电芯容量和料号）
- `power.performance`：源文档列出 4G/Wi-Fi 待机时长、底座供电和外部 5V 下的工作电流、4G 休眠电流及关机电流；六页原理图只提供电源架构，没有固件版本、网络状态、温度、电池老化、采样仪器和统计方法。（证据：图 6921177a261d / 第 1 页 / 主机第 2 页 JW5712 与负载电源架构，无整机功耗测试条件; 图 d68ecc1a2110 / 第 1 页 / 主机第 4 页电池管理电路，无续航测试结果; 图 c62bcc73ac90 / 第 1 页 / 底座电源页仅含 USB 输入与 VCC_DOCK/VDD_3V3 电路）
- `interface.pogo-map`：源文档把 VCC_DOCK/MCU_DP/MCU_DM/GND 映射到主机 5V/DP/DM/GND，并把 MCU_BOOT/MCU_RST/MCU_SDA/MCU_SCL 映射到 GPIO0/EN/GPIO17/GPIO18；主机页和底座页分别给出 EXT 与 MCU 网络，但图面没有画出两块板之间的 Pogo 连接器及逐针对应。（证据：图 d68ecc1a2110 / 第 1 页 / 网格 C1-D5，主机 USB_D_EXT 与 GPIO/EN_EXT 网络，无 Pogo 连接器; 图 c62bcc73ac90 / 第 1 页 / 网格 B4-C4，底座 TP5-TP12 MCU/VCC_DOCK 网络，无逐针 Pogo 连接器）
- `review.soc-capacity`：ESP32-S3-PICO-1-N8R8 的装配料号、8MB Flash 与 8MB PSRAM 是否已由 BOM 和量产读回确认？；原因：图面只有完整器件后缀，没有独立容量文字或存储测试结果。
- `review.sd-nand-capacity`：U8 ZDSD512MLGAAG 的标称与可用容量是否均为 64MB？；原因：原理图未直接标注容量，需由 datasheet、BOM 或固件读回确认。
- `review.display-panel`：J2 所接面板是否为 GDEY027T91，且量产配置固定为 2.7 英寸、176 x 264、1-bit 黑白？；原因：图面只给出 FPC 与电源信号，未写面板型号和显示规格。
- `review.touch-controller`：J3 所接触摸控制器是否固定为 FT6336U，7 位地址是否固定为 0x38？；原因：原理图只绘制触摸 FPC，总线和地址来自源文档。
- `review.power-i2c-addresses`：U13 AW32001 与 U14 BQ27220 的量产 7 位地址是否分别固定为 0x49 和 0x55？；原因：图面确认 I2C 总线，但未标注地址或地址选择状态。
- `review.cellular-variant`：U9 量产模组是否为 ML307R-DL，LTE Cat.1 与所列频段及运营商范围是否适用于当前硬件版本？；原因：图面仅标 ML307，精确子型号和网络能力来自源文档。
- `review.battery-spec`：内置 300mAh @3.7V 电芯的料号、保护方案、温度范围和 AW32001 充电参数是什么？；原因：原理图仅给出充电和电量采样网络，没有电芯与充电性能数据。
- `review.power-performance`：源文档中的待机时长和各工作、休眠、关机电流采用了什么固件、网络、温度、电池状态和测量方法？；原因：图面不能证明整机运行状态、统计方法和重复性。
- `review.pogo-map`：主机 EXT 网络与底座 MCU/VCC_DOCK 网络的 Pogo Pin 逐针对应是否已由连接器图、网表或 PCB 核对？；原因：两份原理图未画跨板连接器，映射来自源文档。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e82c146c5558b12cb58a3cd9cf23f8f8d81f27a03e387ced0259b8eb46c5c602` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Schematics_page_01.png` |
| 2 | 1 | `6921177a261d2c956e90b95895ab3f528ddc79d3ec4a091b02d189477fda78bb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Schematics_page_02.png` |
| 3 | 1 | `3f12cfeafe97926e7f3d090c5f3c9f575d34e5c8af8efecc08ca0ad9c624cd2e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Schematics_page_03.png` |
| 4 | 1 | `d68ecc1a21108b6f32c34075a6f833f7dd36c4064048f34faa2b1ff2364a2474` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Schematics_page_04.png` |
| 5 | 1 | `d1b36f06469feca9f144fa8eeb3f25415e85b24b83951d49889a1dd9a3a9a591` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Schematics_page_05.png` |
| 6 | 1 | `c62bcc73ac9070d83fd1ba6d812fde6307a9e83ac4992b248b0ee767eb7e9745` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/Xiaozhi_Card_Base_Schematics.png` |

---

源文档：`zh_CN/core/Xiaozhi_Card_Kit.md`

源文档 SHA-256：`947eccd9e77acbf31d706b9c356905d6aa3df18f9ab3299d6a885613a078a43a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
