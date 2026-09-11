# PaperMono-Lite 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PaperMono-Lite |
| SKU | C153-Lite |
| 产品 ID | `papermono-lite-2ac40c4cf3c5` |
| 源文档 | `zh_CN/core/PaperMono-Lite.md` |

## 概述

PaperMono-Lite 以 ESP32-S3R8 为主控，外接 XM25UH128DHIQT NOR Flash，并通过系统 I2C 总线连接 M5PM1 电源管理、M5IOE1 扩展、RX8130CE RTC 和 BMI270 IMU。USB-C 输入经 AW32901FCR 保护与 IP2315 充电路径形成 VBUS_L0，再由多级 LDO、JW5712 和受控负载开关生成 3V3_L0、3V3_L1、3V3_L2、EPD_3V3_L3、TF_3V3_L3、TP_VDD 与 PDM_VDD。电子纸、microSD、触控、PDM 音频、蜂鸣器、RGB LED、按键和调试测试点均有明确网络映射；LoRa 与 RFID 仅保留未装配设计位。

## 检索关键词

`PaperMono-Lite`、`C153-Lite`、`ESP32-S3R8`、`M5PM1`、`M5IOE1`、`IP2315`、`AW32901FCR`、`JW5712`、`SSP7615-33DFR`、`AW9967DNR`、`XM25UH128DHIQT`、`RX8130CE`、`BMI270`、`USB-C`、`microSD`、`E-Paper`、`PDM`、`I2C`、`SPI`、`SDIO`、`0x6E`、`0x4F`、`0x32`、`0x68`、`G47_SYS_SDA`、`G48_SYS_SCL`、`EPD_3V3_L3`、`TF_3V3_L3`、`TP_VDD`、`PDM_VDD`、`BL_15V_L3B`、`BAT_ADC`、`5VIN_ADC`、`PYB_EPD_EN`、`PYB_TF_EN`、`PYB_TP_EN`、`G18_EINK_BUSY`、`LoRa DNP`、`RFID DNP`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| USB | TYPEC-302-BRP16SC08 | 仅输入的 USB Type-C 连接器，引出 VUSB_IN、USB_P、USB_N、CC1 和 CC2。 | 图 431347b4c4ad / 第 1 页 / A1 TYPEC 分区，USB/TYPEC-302-BRP16SC08 符号及 VUSB_IN、USB_P、USB_N 网络 |
| TVS1/TVS2 | ESD5311 | USB_N 与 USB_P 数据线的对地静电保护器件。 | 图 431347b4c4ad / 第 1 页 / A1 TYPEC 分区，TVS1/TVS2 ESD5311 分别连接 USB_N/USB_P 与 GND |
| U2 | AW32901FCR | VUSB_IN 到 5V_IN 的输入过压保护开关，图示 OVP=5.95V。 | 图 431347b4c4ad / 第 1 页 / A2 PROTECTION 分区，U2 AW32901FCR、VUSB_IN/5V_IN 与 OVP=5.95V 标注 |
| U1 | IP2315 | 由 5V_IN 为 VBAT_L0 充电的电池充电控制器。 | 图 431347b4c4ad / 第 1 页 / A3 CHARG 分区，U1 IP2315、5V_IN 输入、BAT/VBAT_L0 输出及 ICHGSET/NTC 引脚 |
| U3 | AW39112DNR | 在 3V3_L2 系统 I2C 与 VBAT_L0 侧充电 I2C 之间进行双向电平转换，并由 PYB_CHG_IIC 控制 OE。 | 图 431347b4c4ad / 第 1 页 / B3 CHARG 分区，U3 AW39112DNR 的 VCCA/VCCB、G47/G48、CHG_SYS_SDA/SCL 与 PYB_CHG_IIC |
| J2 | CON2_SMD | 两针锂电池连接器，连接 VBAT_L0 与 GND。 | 图 431347b4c4ad / 第 1 页 / B2 Battery 分区，J2 CON2_SMD 两针连接器及 VBAT_L0/GND |
| Q1A/Q1B | CJ3439KDW | 由 BAT_ADC_EN 控制的电池采样门控与 BAT_ADC 分压网络。 | 图 431347b4c4ad / 第 1 页 / A4 ADC_DET 分区，Q1A/Q1B CJ3439KDW、BAT_ADC_EN、VBAT_L0 与 BAT_ADC |
| U4 | SSP7615-33DFR | 由 VBUS_L0 生成常开 3V3_L0 的 L0 级 LDO。 | 图 431347b4c4ad / 第 1 页 / B1 L0_SW 分区，U4 SSP7615-33DFR 从 VBUS_L0 输出 3V3_L0 |
| U6 | SSP7615-33DFR | 由 3V3_L1_EN 控制、从 VBUS_L0 生成 3V3_L1 的 L1 级 LDO。 | 图 431347b4c4ad / 第 1 页 / C1 L1_SW 分区，U6 SSP7615-33DFR、3V3_L1_EN 与 3V3_L1 |
| U9 | SSP7615-33DFR | LoRa 专用 3V3_L2_LoRa 电源的预留 LDO；器件及外围在 Lite 图中标为不装。 | 图 431347b4c4ad / 第 1 页 / C1-D1 L2_SW 分区，U9 与 C22/R26/C23 交叉阴影并标 NC，网络 PYG2_LoRa_EN/3V3_L2_LoRa |
| U10 | JW5712 | 由 3V3_L2_EN 控制、从 VBUS_L0 生成 3V3_L2 的降压转换器。 | 图 431347b4c4ad / 第 1 页 / D1-D2 L2_SW 分区，U10 JW5712、3V3_L2_EN、L2 与 3V3_L2; 图 fcf5a820e5f2 / 第 1 页 / A6 Power Network，JW5712 DCDC 600mA 从 VBUS_L0 输出 3V3_L2 |
| U5 | SSP7615-33DFR | 由 PYB_EPD_EN 控制、从 VBUS_L0 生成 EPD_3V3_L3 的电子纸电源开关。 | 图 431347b4c4ad / 第 1 页 / C2 L3_SW/EPD_3V3 分区，U5 SSP7615-33DFR、PYB_EPD_EN 与 EPD_3V3_L3 |
| U8 | AW35122FDR | 由 PYB_TF_EN 控制、从 3V3_L2 生成 TF_3V3_L3 的 microSD 电源开关。 | 图 431347b4c4ad / 第 1 页 / C2-C3 L3_SW/TF_3V3V 分区，U8 AW35122FDR、PYB_TF_EN 与 TF_3V3_L3 |
| U11 | AW9967DNR | 由 PYG3_BL_PWM 调光、把 EPD_3V3_L3 升压为 BL_15V_L3B 的前光驱动器。 | 图 431347b4c4ad / 第 1 页 / D2-D3 EINK_BL 分区，U11 AW9967DNR、L3、D2、PYG3_BL_PWM、BL_FB 与 BL_15V_L3B |
| J1 | 未标注 | 前光输出连接器，引出 BL_15V_L3B 与 BL_FB。 | 图 431347b4c4ad / 第 1 页 / D3 EINK_BL 分区，J1 六针连接器的 BL_15V_L3B 与 BL_FB 网络 |
| U7 | M5PM1 | I2C 电源管理与低功耗状态控制器，管理 L1/L2 使能、ADC、唤醒源、按键和红色 LED。 | 图 431347b4c4ad / 第 1 页 / C4-D4 PMIC 分区，U7 M5PM1、IIC Address:0x6E 及全部控制网络 |
| U12 | ESP32_S3R8 | 系统主控，连接 USB、I2C、UART、电子纸、microSD、PDM、按键、中断、外部 Flash 与板载天线。 | 图 ae396bd19142 / 第 1 页 / A2-D3 MCU_Core 分区，U12 ESP32_S3R8 主控及 GPIO/SPI/USB/XTAL 引脚 |
| U13 | XM25UH128DHIQT | 通过 NOR_CS/NOR_DO/NOR_SCK/NOR_DI/NOR_HOLD/NOR_WP 连接主控的外部 NOR Flash。 | 图 ae396bd19142 / 第 1 页 / C4 MCU_Core 右侧，U13 XM25UH128DHIQT 与六条 NOR_* 网络 |
| ANT1 | ANT_PIFA | ESP32-S3 的板载 PIFA 射频天线，经过 L5/L4 与匹配电容网络连接 LNA_IN。 | 图 ae396bd19142 / 第 1 页 / A1-A2 MCU_Core 左上，ANT1 ANT_PIFA、L5/L4、C39-C42 与 U12 LNA_IN |
| X1 | CN4040M000157A530001 | ESP32-S3 的 XTAL_P/XTAL_N 主晶振网络。 | 图 ae396bd19142 / 第 1 页 / A4-B4 MCU_Core 右上，X1、L7 24nH、C45/C50 24pF 与 XTAL_P/XTAL_N |
| FT1 | ICMF062P900MFR | USB_P/USB_N 到 ESP32 GPIO20/GPIO19 之间的共模滤波器。 | 图 ae396bd19142 / 第 1 页 / D1-D2 MCU_Core/USB，FT1 ICMF062P900MFR、R40/R41 22R 与 G19_USB_N/G20_USB_P |
| U16 | RX8130CE | 地址 0x32 的 I2C 实时时钟，nIRQ 连接 PYG0_RTC_INT。 | 图 0cdf2ccee1a8 / 第 1 页 / A1 RTC 分区，U16 RX8130CE、IIC Address:0x32、G47/G48 与 PYG0_RTC_INT |
| U15 | BMI270 | 地址 0x68 的 I2C IMU，INT1 连接 PYG4_IMU_INT，供电为 3V3_L1。 | 图 0cdf2ccee1a8 / 第 1 页 / A2 IMU 分区，U15 BMI270、IIC Address:0x68、G47/G48、PYG4_IMU_INT 与 3V3_L1 |
| Q3 | SK2302AAT | 由 G42_BB_PWM 控制蜂鸣器的低边开关，D3 提供感性回扫路径。 | 图 0cdf2ccee1a8 / 第 1 页 / A3 BUZZER 分区，Q3 SK2302AAT、D3 1N4148WS、3V3_L2 与 G42_BB_PWM |
| RFID footprint | 未标注 | Lite 版本未装配的 RFID/NFC 预留位，保留 I2C、中断和使能网络标注。 | 图 0cdf2ccee1a8 / 第 1 页 / A4 RFID 分区，器件与 C59 交叉阴影/NC，网络 G47/G48、G6_RFID_INT、PYB_NFC_EN |
| U14 | 未标注 | Lite 版本未装配的 LoRa 模组预留位，相关电源与器件以交叉阴影或 NC 标记。 | 图 0cdf2ccee1a8 / 第 1 页 / A5-A6 LoRa 分区，U14 与 C65 交叉阴影，3V3_L2_LoRa 标 NC，并保留 G38-G41/G5/G21/PYB 网络 |
| U17 | M5IOE1 | 地址 0x4F 的 I2C GPIO/PWM/ADC 扩展器，管理触控、电子纸、microSD、PDM、RGB 与预留射频控制。 | 图 0cdf2ccee1a8 / 第 1 页 / B1-B2 PYB_IIC 分区，U17 M5IOE1、IIC Address:0x4F 及 PYG1-PYG14 网络 |
| U18 | AW35122FDR | 由 PYB_TP_EN 控制、从 3V3_L2 生成 TP_VDD 的触控电源开关。 | 图 0cdf2ccee1a8 / 第 1 页 / B3 TP 分区，U18 AW35122FDR、PYB_TP_EN、3V3_L2 与 TP_VDD |
| U19 | AW39112DNR | G47/G48 系统 I2C 与 TP_SYS_SDA/TP_SYS_SCL 触控电源域之间的双向电平转换器。 | 图 0cdf2ccee1a8 / 第 1 页 / B3 TP 分区，U19 AW39112DNR、VCCA=TP_VDD、VCCB=3V3_L2 及两侧 I2C 网络 |
| J4 | 未标注 | 六针触控接口，提供 TP_VDD、GND、TP_SYS_SCL、TP_SYS_SDA、G4_TP_INT 与 PYB_TP_RST。 | 图 0cdf2ccee1a8 / 第 1 页 / B3-C4 TP 分区，J4 六针连接器及 TP_SYS_SCL/SDA、G4_TP_INT、PYB_TP_RST、TP_VDD |
| KEY/RGB/PDM connector | AXE512127D | 连接按键、RGB LED 与 PDM 麦克风子组件的板对板连接器。 | 图 0cdf2ccee1a8 / 第 1 页 / C1-D1 KEY&RGB&PDM 分区，AXE512127D 与 PY_LED_R/PYB_LED_G/B、PWR_BTN、G2/G3、G45/G46 网络 |
| U21 | AW35122FDR | 由 PYB_PDM_EN 控制、从 3V3_L2 生成 PDM_VDD 的麦克风电源开关。 | 图 0cdf2ccee1a8 / 第 1 页 / D1 KEY&RGB&PDM 分区，U21 AW35122FDR、PYB_PDM_EN 与 PDM_VDD |
| U20 | MicroSD | 由 TF_3V3_L3 供电的 microSD 卡座，提供 DAT0-DAT3、CMD、CLK 与卡检测开关。 | 图 0cdf2ccee1a8 / 第 1 页 / C2-D3 TF 分区，U20 MicroSD、G8-G13 数据/命令/时钟与 PYB_TF_DET |
| TVS3-TVS9 | ESD5311 | microSD DAT2、DAT3、CMD、CLK、DAT0、DAT1 与检测线的对地 ESD 保护阵列。 | 图 0cdf2ccee1a8 / 第 1 页 / D2 TF 分区，TVS3-TVS9 ESD5311 分别连接 G8-G13/PYB_TF_DET 与 GND |
| Q4 | CJ2310 | 与 L8、D4-D6 构成电子纸 PREVGH/PREVGL 偏压生成电路。 | 图 0cdf2ccee1a8 / 第 1 页 / B5-B6 EINK 分区，Q4 CJ2310、L8、D4-D6、GDR/RESE 与 PREVGH/PREVGL |
| J5 | FPC0.5-SMT-24P-B | 24 针电子纸 FPC，承载 SPI 控制、忙信号、复位、偏压与 EPD_3V3_L3。 | 图 0cdf2ccee1a8 / 第 1 页 / C5-D6 EINK 分区，J5 FPC0.5-SMT-24P-B 与 G14-G18/PYB_EINK_RST/PREVGH/PREVGL/EPD_3V3_L3 |

## 系统结构

### 系统架构

ESP32-S3R8 作为主控，M5PM1 管理多级电源与唤醒，M5IOE1 扩展触控、电子纸、microSD、PDM 和 RGB 控制，外设经 I2C、SPI/SDIO、USB、UART 与专用 GPIO 连接。

- 参数与网络：`soc=U12 ESP32_S3R8`；`pmic=U7 M5PM1`；`io_expander=U17 M5IOE1`；`system_i2c=G47_SYS_SDA/G48_SYS_SCL`
- 证据：图 fcf5a820e5f2 / 第 1 页 / A5-D8 Power Network 与 I/Os Map，总览 PMIC、ESP-S3、PYB 及各功能块; 图 ae396bd19142 / 第 1 页 / A2-D4 MCU_Core，U12 与外部 Flash、USB、天线和测试点

### 低功耗状态

系统框图定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE 与 L3B All ACTIVE 五级状态；L0 自动进入 L1，S3 可用 I2C 关机命令返回 L0。

- 参数与网络：`L0=Shipping`；`L1=Standby`；`L2=DeepSleep`；`L3A=CORE ACTIVE`；`L3B=All ACTIVE`
- 证据：图 fcf5a820e5f2 / 第 1 页 / A5-A8 Power Network 状态列与 C1-D3 Power Mode 状态图

### Lite 版本射频预留

LoRa U14、LoRa 专用 U9 电源及 RFID 预留位在 Lite 原理图中以交叉阴影和 NC 标记，相关网络是设计预留而非实装功能。

- 参数与网络：`lora_module=U14 DNP`；`lora_power=U9 DNP`；`rfid=DNP`；`reserved_nets=G38_SPI1_MOSI,G39_SPI1_CLK,G40_SPI1_MISO,G41_LoRa_NSS,G5_LoRa_INT,G21_LoRa_BUSY,G6_RFID_INT`
- 证据：图 431347b4c4ad / 第 1 页 / C1-D1 L2_SW，U9/C22/R26/C23 交叉阴影并标 NC; 图 0cdf2ccee1a8 / 第 1 页 / A4-A6 RFID 与 LoRa 分区，预留器件及去耦件交叉阴影/NC

### 唤醒源

M5PM1 的 G0_WAKEin 接 PYG0_RTC_INT，G4_WAKEin 接 PYG4_IMU_INT；ESP32 还接收 G7_PYB_IRQ、G4_TP_INT 与两个按键网络，框图把 RTC、IMU、触控和按键列为低功耗唤醒路径。

- 参数与网络：`pmic_wake0=PYG0_RTC_INT`；`pmic_wake4=PYG4_IMU_INT`；`soc_io_wake=G7_PYB_IRQ,G4_TP_INT,G2_KEY1,G3_KEY2`
- 证据：图 fcf5a820e5f2 / 第 1 页 / C1-D3 Power Mode 唤醒箭头与 C4-D8 I/Os Map 中断网络; 图 431347b4c4ad / 第 1 页 / C4-D4 U7 M5PM1 G0_WAKEin/G4_WAKEin 与 PYG0_RTC_INT/PYG4_IMU_INT

## 电源

### USB 输入与充电路径

USB-C 的 VBUS 形成 VUSB_IN，经 U2 AW32901FCR 保护后成为 5V_IN，再进入 U1 IP2315 并由 BAT 引脚输出到 VBAT_L0。

- 参数与网络：`path=USB VBUS -> VUSB_IN -> U2 -> 5V_IN -> U1 -> VBAT_L0`；`protector=AW32901FCR`；`charger=IP2315`
- 证据：图 431347b4c4ad / 第 1 页 / A1-A3 TYPEC/PROTECTION/CHARG，VUSB_IN、5V_IN、U2 与 U1 连接

### 系统母线来源

VBAT_L0 通过 R20 0R 串联连接 VBUS_L0，使电池/充电节点成为后级各电源转换器的输入母线。

- 参数与网络：`from=VBAT_L0`；`link=R20 0R/1%`；`to=VBUS_L0`
- 证据：图 431347b4c4ad / 第 1 页 / B1 L0_SW 上方，R20 0R 连接 VBAT_L0 与 VBUS_L0

### 3V3_L0 电源域

U4 SSP7615-33DFR 的 EN 直接接 VBUS_L0，输出 3V3_L0；框图将该 LDO 标为 Always On。

- 参数与网络：`input=VBUS_L0`；`output=3V3_L0`；`regulator=U4 SSP7615-33DFR`；`mode=Always On`
- 证据：图 431347b4c4ad / 第 1 页 / B1 L0_SW，U4 输入/使能接 VBUS_L0 并输出 3V3_L0; 图 fcf5a820e5f2 / 第 1 页 / A5-A6 Power Network，SSP7615 LDO 400mA Always On 输出 3V3_L0

### 3V3_L1 电源域

U6 SSP7615-33DFR 从 VBUS_L0 生成 3V3_L1，其 EN 由 M5PM1 的 3V3_L1_EN 控制，BMI270 使用该电源域。

- 参数与网络：`input=VBUS_L0`；`output=3V3_L1`；`enable=3V3_L1_EN`；`load=BMI270`
- 证据：图 431347b4c4ad / 第 1 页 / C1 L1_SW，U6 SSP7615-33DFR 与 3V3_L1_EN/3V3_L1; 图 0cdf2ccee1a8 / 第 1 页 / A2 IMU，U15 BMI270 的 VDD/VDDIO 接 3V3_L1

### 3V3_L2 核心电源域

U10 JW5712 在 3V3_L2_EN 有效时将 VBUS_L0 降压为 3V3_L2，框图标注该转换器额定 600mA。

- 参数与网络：`input=VBUS_L0`；`output=3V3_L2`；`enable=3V3_L2_EN`；`converter=U10 JW5712`；`diagram_rating=600mA`
- 证据：图 431347b4c4ad / 第 1 页 / D1-D2 L2_SW，U10 JW5712、L2、3V3_L2_EN 与 3V3_L2; 图 fcf5a820e5f2 / 第 1 页 / A6 Power Network，JW5712 DCDC 600mA 标注

### LoRa 预留电源

3V3_L2_LoRa 原设计由 U9 SSP7615-33DFR 从 VBUS_L0 生成并受 PYG2_LoRa_EN 控制，但 U9 与外围均在 Lite 图中标为不装。

- 参数与网络：`input=VBUS_L0`；`output=3V3_L2_LoRa`；`enable=PYG2_LoRa_EN`；`assembly=DNP`
- 证据：图 431347b4c4ad / 第 1 页 / C1-D1 L2_SW，U9/C22/R26/C23 灰色交叉阴影并标 NC

### 电子纸 3.3V 开关

U5 SSP7615-33DFR 由 PYB_EPD_EN 控制，把 VBUS_L0 切换为 EPD_3V3_L3。

- 参数与网络：`input=VBUS_L0`；`output=EPD_3V3_L3`；`enable=PYB_EPD_EN`
- 证据：图 431347b4c4ad / 第 1 页 / C2 L3_SW/EPD_3V3，U5 与 PYB_EPD_EN/EPD_3V3_L3

### microSD 电源开关

U8 AW35122FDR 由 PYB_TF_EN 控制，把 3V3_L2 切换为 TF_3V3_L3 供给 microSD。

- 参数与网络：`input=3V3_L2`；`output=TF_3V3_L3`；`enable=PYB_TF_EN`
- 证据：图 431347b4c4ad / 第 1 页 / C2-C3 L3_SW/TF_3V3V，U8 与 PYB_TF_EN/TF_3V3_L3; 图 0cdf2ccee1a8 / 第 1 页 / C2-D3 TF，U20 VDD 接 TF_3V3_L3

### 触控电源开关

U18 AW35122FDR 由 PYB_TP_EN 控制，把 3V3_L2 切换为 TP_VDD；TP_VDD 同时供给 J4 与 U19 低压侧。

- 参数与网络：`input=3V3_L2`；`output=TP_VDD`；`enable=PYB_TP_EN`；`loads=J4,U19 VCCA`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B3-B4 TP，U18/U19/J4 与 TP_VDD/PYB_TP_EN

### PDM 麦克风电源开关

U21 AW35122FDR 由 PYB_PDM_EN 控制，把 3V3_L2 切换为 PDM_VDD。

- 参数与网络：`input=3V3_L2`；`output=PDM_VDD`；`enable=PYB_PDM_EN`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / D1 KEY&RGB&PDM，U21 与 PYB_PDM_EN/PDM_VDD

### 电子纸前光升压

U11 AW9967DNR 使用 EPD_3V3_L3、L3 10uH 和 D2 生成 BL_15V_L3B，PYG3_BL_PWM 接 CTRL，BL_FB 经 R29 18R 反馈。

- 参数与网络：`input=EPD_3V3_L3`；`output=BL_15V_L3B`；`control=PYG3_BL_PWM`；`feedback=BL_FB`；`inductor=L3 10uH`；`diode=D2 RB162VAM-20TR`
- 证据：图 431347b4c4ad / 第 1 页 / D2-D3 EINK_BL，U11/L3/D2/R29/J1 及 BL_15V_L3B/BL_FB/PYG3_BL_PWM

### 电子纸偏压

Q4 CJ2310、L8 与 D4-D6 从 EPD_3V3_L3 形成 PREVGH 和 PREVGL，并以 GDR/RESE 网络控制开关。

- 参数与网络：`input=EPD_3V3_L3`；`outputs=PREVGH,PREVGL`；`switch=Q4 CJ2310`；`inductor=L8 SPH252010H330MT`；`diodes=D4/D5/D6 1N5819WS`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B5-B6 EINK，Q4/L8/D4-D6 与 GDR/RESE/PREVGH/PREVGL

## 接口

### USB-C 接口

USB 连接器的 VBUS 脚并联为 VUSB_IN，D+/D- 分别形成 USB_P/USB_N，CC1 与 CC2 各通过 5.1K 电阻下拉到 GND。

- 参数与网络：`connector=USB TYPEC-302-BRP16SC08`；`power=VUSB_IN`；`data_plus=USB_P`；`data_minus=USB_N`；`cc_resistors=R4/R14 5.1K/1%`
- 证据：图 431347b4c4ad / 第 1 页 / A1 TYPEC，USB 引脚 1-16、R4/R14 与 USB_P/USB_N/VUSB_IN

### 电池接口

J2 是两针电池连接器，1 脚接 GND，2 脚接 VBAT_L0，并在 VBAT_L0 侧以 C13 22uF/10V 去耦。

- 参数与网络：`reference=J2`；`pin1=GND`；`pin2=VBAT_L0`；`capacitor=C13 22uF/10V`
- 证据：图 431347b4c4ad / 第 1 页 / B2 Battery，J2 CON2_SMD 与 C13

### 电子纸 FPC

J5 FPC0.5-SMT-24P-B 引出 EPD_3V3_L3、G14-G18 控制总线、PYB_EINK_RST、GDR、RESE、PREVGH、PREVGL 与多个 GND/去耦节点。

- 参数与网络：`connector=J5 FPC0.5-SMT-24P-B`；`logic_supply=EPD_3V3_L3`；`logic_signals=G14_SPI2_MOSI,G15_SPI2_CLK,G16_EINK_CS,G17_EINK_DC,G18_EINK_BUSY,PYB_EINK_RST`；`bias_signals=GDR,RESE,PREVGH,PREVGL`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / C5-D6 EINK，J5 24 针 FPC 的网络标签

### 按键/RGB/PDM 连接器

AXE512127D 板对板连接器集中承载 3V3_L2、3V3_L0、PDM_VDD、GND、PY_LED_R、PYB_LED_G/B、PWR_BTN、G2_KEY1、G3_KEY2 与 G45/G46 PDM 网络。

- 参数与网络：`part_number=AXE512127D`；`power=3V3_L2,3V3_L0,PDM_VDD,GND`；`signals=PY_LED_R,PYB_LED_G,PYB_LED_B,PWR_BTN,G2_KEY1,G3_KEY2,G45_PDM_CLK,G46_PDM_DAT`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / C1-D1 KEY&RGB&PDM，AXE512127D 连接器全部引脚网络

## 总线

### 系统 I2C 总线

ESP32-S3 GPIO47/GPIO48 分别承载 G47_SYS_SDA/G48_SYS_SCL，并由 R36/R37 2.2K 上拉到 3V3_L2，连接 M5PM1、M5IOE1、RTC、IMU 及受控外设桥。

- 参数与网络：`sda=GPIO47/G47_SYS_SDA`；`scl=GPIO48/G48_SYS_SCL`；`pullups=R36/R37 2.2K/1% to 3V3_L2`
- 证据：图 ae396bd19142 / 第 1 页 / C1 IIC PULL_UP 与 U12 GPIO47/GPIO48，R36/R37 2.2K; 图 0cdf2ccee1a8 / 第 1 页 / A1-A2 与 B1-B3，RTC/IMU/M5IOE1/触控桥的 G47/G48 网络

### 充电器 I2C 隔离

U3 AW39112DNR 将 G47_SYS_SDA/G48_SYS_SCL 转换为 CHG_SYS_SDA/CHG_SYS_SCL，VCCA 为 3V3_L2、VCCB 为 VBAT_L0，PYB_CHG_IIC 控制 OE。

- 参数与网络：`system_side=G47_SYS_SDA/G48_SYS_SCL at 3V3_L2`；`charger_side=CHG_SYS_SDA/CHG_SYS_SCL at VBAT_L0`；`enable=PYB_CHG_IIC`；`translator=U3 AW39112DNR`
- 证据：图 431347b4c4ad / 第 1 页 / B3 CHARG，U3 AW39112DNR 电源、A/B 通道与 OE

### 触控 I2C 接口

U19 将 G48_SYS_SCL/G47_SYS_SDA 转换为 TP_SYS_SCL/TP_SYS_SDA，J4 同时引出 G4_TP_INT 与 PYB_TP_RST。

- 参数与网络：`scl_system=G48_SYS_SCL`；`sda_system=G47_SYS_SDA`；`scl_touch=TP_SYS_SCL`；`sda_touch=TP_SYS_SDA`；`interrupt=G4_TP_INT`；`reset=PYB_TP_RST`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B3-C4 TP，U19 AW39112DNR 与 J4 网络

### 电子纸 SPI

电子纸接口使用 G14_SPI2_MOSI、G15_SPI2_CLK、G16_EINK_CS、G17_EINK_DC 与 G18_EINK_BUSY，复位由 PYB_EINK_RST 提供。

- 参数与网络：`mosi=GPIO14/G14_SPI2_MOSI`；`clock=GPIO15/G15_SPI2_CLK`；`chip_select=GPIO16/G16_EINK_CS`；`data_command=GPIO17/G17_EINK_DC`；`busy=GPIO18/G18_EINK_BUSY`；`reset=PYB_EINK_RST`
- 证据：图 ae396bd19142 / 第 1 页 / C2 U12 GPIO14-GPIO18 的 G14-G18 电子纸网络; 图 0cdf2ccee1a8 / 第 1 页 / C5-D6 EINK，J5 上的 G14-G18 与 PYB_EINK_RST

### microSD 数据总线

microSD U20 使用六线接口：G8_TF_DATA3、G9_TF_DATA2、G10_TF_DATA1、G11_TF_DATA0、G12_TF_CMD 与 G13_TF_CLK。

- 参数与网络：`DAT3=GPIO8/G8_TF_DATA3`；`DAT2=GPIO9/G9_TF_DATA2`；`DAT1=GPIO10/G10_TF_DATA1`；`DAT0=GPIO11/G11_TF_DATA0`；`CMD=GPIO12/G12_TF_CMD`；`CLK=GPIO13/G13_TF_CLK`
- 证据：图 ae396bd19142 / 第 1 页 / B2-C2 U12 GPIO8-GPIO13 的 TF 网络; 图 0cdf2ccee1a8 / 第 1 页 / C2-D3 TF，U20 MicroSD DAT0-DAT3/CMD/CLK

### UART0 调试串口

ESP32-S3 GPIO43/U0TXD 通过 R30 499R 引出 G43_U0_TX，GPIO44/U0RXD 引出 G44_U0_RX，两线分别连接 TP4 与 TP9。

- 参数与网络：`tx=GPIO43/G43_U0_TX/TP4`；`rx=GPIO44/G44_U0_RX/TP9`；`tx_series=R30 499R/1%`
- 证据：图 ae396bd19142 / 第 1 页 / A3-B3 U12 GPIO43/44 与 D3 DEBUG TP4/TP9

## 总线地址

### M5PM1 I2C 地址

M5PM1 U7 的原理图可见 I2C 地址为 0x6E。

- 参数与网络：`reference=U7`；`address=0x6E`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`
- 证据：图 431347b4c4ad / 第 1 页 / C4-D4 PMIC，U7 M5PM1 下方 IIC Address:0x6E

### M5IOE1 I2C 地址

M5IOE1 U17 的原理图可见 I2C 地址为 0x4F。

- 参数与网络：`reference=U17`；`address=0x4F`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B1-B2 PYB_IIC，U17 M5IOE1 上方 IIC Address:0x4F

### RTC I2C 地址

RX8130CE U16 的原理图可见 I2C 地址为 0x32。

- 参数与网络：`reference=U16`；`address=0x32`；`interrupt=PYG0_RTC_INT`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / A1 RTC，IIC Address:0x32 与 U16 RX8130CE

### IMU I2C 地址

BMI270 U15 的原理图可见 I2C 地址为 0x68。

- 参数与网络：`reference=U15`；`address=0x68`；`interrupt=PYG4_IMU_INT`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / A2 IMU，IIC Address:0x68 与 U15 BMI270

## GPIO 与控制信号

### 用户按键

两个用户按键分别连接 ESP32-S3 GPIO2/G2_KEY1 与 GPIO3/G3_KEY2，电源按键 PWR_BTN 接 M5PM1 BTN_PU。

- 参数与网络：`key1=GPIO2/G2_KEY1`；`key2=GPIO3/G3_KEY2`；`power_button=PWR_BTN -> M5PM1 BTN_PU`
- 证据：图 fcf5a820e5f2 / 第 1 页 / C6-D8 I/Os Map，KEY 框与 ESP32 G2/G3、M5PM1 PWR_BTN; 图 0cdf2ccee1a8 / 第 1 页 / C1-D1 KEY&RGB&PDM，AXE512127D 上的 PWR_BTN/G2_KEY1/G3_KEY2

### M5IOE1 中断

M5IOE1 的 OD_INTOUT 通过 G7_PYB_IRQ 接 ESP32-S3 GPIO7，并由 R53 10K 上拉到 3V3_L2。

- 参数与网络：`source=U17 OD_INTOUT pin 2`；`net=G7_PYB_IRQ`；`destination=U12 GPIO7`；`pullup=R53 10K/1% to 3V3_L2`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B1 PYB_IIC，U17 pin2 G7_PYB_IRQ 与 R53; 图 ae396bd19142 / 第 1 页 / B2 U12 GPIO7 的 G7_PYB_IRQ

### 触控控制信号

触控中断 G4_TP_INT 直达 ESP32-S3 GPIO4，触控复位 PYB_TP_RST 来自 M5IOE1 PYG6，电源使能 PYB_TP_EN 来自 PYG13。

- 参数与网络：`interrupt=GPIO4/G4_TP_INT`；`reset=U17 PYG6/PYB_TP_RST`；`power_enable=U17 PYG13/PYB_TP_EN`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B2-B4 PYB_IIC 与 TP，U17 PYG6/PYG13、J4 G4_TP_INT/PYB_TP_RST; 图 ae396bd19142 / 第 1 页 / B2 U12 GPIO4 的 G4_TP_INT

### 电子纸扩展控制

M5IOE1 PYG5_ADC3 输出 PYB_EINK_RST，PYG3 输出 PYB_EPD_EN；前光 PWM 由 M5PM1 PYG3_BL_PWM 提供。

- 参数与网络：`reset=U17 PYG5_ADC3/PYB_EINK_RST`；`power_enable=U17 PYG3/PYB_EPD_EN`；`backlight_pwm=U7 G3_WAKEin/PYG3_BL_PWM`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B2 PYB_IIC，U17 PYG5_ADC3/PYG3；C5-D6 J5 PYB_EINK_RST; 图 431347b4c4ad / 第 1 页 / D3-D4 U7 PYG3_BL_PWM 与 U11 CTRL

### microSD 电源与检测

M5IOE1 PYG14 输出 PYB_TF_EN 控制卡电源，PYG1 输入 PYB_TF_DET 接收卡座开关状态。

- 参数与网络：`power_enable=U17 PYG14/PYB_TF_EN`；`detect=U17 PYG1/PYB_TF_DET`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B1-B2 PYB_IIC，U17 PYG14/PYG1；C2-D3 TF，U20 SW/PYB_TF_DET

### RGB LED 控制

RGB 三色控制分别为 M5PM1 LED_EN_PP/PY_LED_R、M5IOE1 PYG8_PWM2/PYB_LED_G 与 PYG9_PWM1/PYB_LED_B。

- 参数与网络：`red=U7 LED_EN_PP/PY_LED_R`；`green=U17 PYG8_PWM2/PYB_LED_G`；`blue=U17 PYG9_PWM1/PYB_LED_B`
- 证据：图 fcf5a820e5f2 / 第 1 页 / C6-D7 I/Os Map，RGB 框与 M5PM1/M5IOE1 网络; 图 0cdf2ccee1a8 / 第 1 页 / B1-B2 U17 PYG8/PYG9 与 C1-D1 AXE512127D 的 PY_LED_R/PYB_LED_G/B

### M5PM1 电源控制输出

M5PM1 DCDC3V3_EN_PP 输出 3V3_L2_EN，LDO3V3_EN_PP 输出 3V3_L1_EN；BOOST5V_EN_PP 与 CHG_EN_PP 在图中不连接。

- 参数与网络：`l2_enable=DCDC3V3_EN_PP/3V3_L2_EN`；`l1_enable=LDO3V3_EN_PP/3V3_L1_EN`；`not_connected=BOOST5V_EN_PP,CHG_EN_PP`
- 证据：图 431347b4c4ad / 第 1 页 / C4 PMIC，U7 pins 14/18/10/2 与 3V3_L2_EN/3V3_L1_EN/NC

### 启动控制

M5PM1 BOOT_OUT_OD 通过 G0_BOOT_OUT 接 ESP32-S3 GPIO0 启动绑带脚，R33 10K 将该网络上拉到 3V3_L2。

- 参数与网络：`pmic_pin=U7 BOOT_OUT_OD`；`net=G0_BOOT_OUT`；`soc_pin=U12 GPIO0[strap]`；`pullup=R33 10K/1% to 3V3_L2`
- 证据：图 431347b4c4ad / 第 1 页 / D4 PMIC，U7 BOOT_OUT_OD/G0_BOOT_OUT; 图 ae396bd19142 / 第 1 页 / B2 MCU_Core，R33 10K 与 U12 GPIO0[strap]/G0_BOOT_OUT

## 时钟

### ESP32-S3 主晶振

U12 XTAL_P/XTAL_N 连接 X1，XTAL_P 支路串联 L7 24nH，C45 与 C50 各为 24pF 对地。

- 参数与网络：`crystal=X1 CN4040M000157A530001`；`nets=XTAL_P,XTAL_N`；`series_inductor=L7 24nH`；`load_capacitors=C45=24pF,C50=24pF`
- 证据：图 ae396bd19142 / 第 1 页 / A3-B4 MCU_Core，U12 XTAL_P/XTAL_N、L7、X1、C45/C50

## 复位

### ESP32-S3 复位

SOC_RESET 接 U12 CHIP_PU，R31 10K 上拉到 3V3_L2，C53 1uF 接地形成 RC，R32 0R 串接到 SOC_RESET 网络。

- 参数与网络：`soc_pin=U12 CHIP_PU`；`net=SOC_RESET`；`pullup=R31 10K/1%`；`capacitor=C53 1uF/25V`；`series=R32 0R/1%`
- 证据：图 ae396bd19142 / 第 1 页 / B1-B2 RC_RESET，R31/R32/C53 与 U12 CHIP_PU/SOC_RESET

### M5IOE1 复位

M5IOE1 U17 的 NRST 接 RST 网络，并由 R51 上拉到 3V3_L2；RST 同时引到 TP15。

- 参数与网络：`reference=U17`；`pin=NRST`；`net=RST`；`pullup=R51 to 3V3_L2`；`test_point=TP15`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / B1-B2 PYB_IIC，U17 NRST/RST、R51 与 TP15

## 保护电路

### USB 数据线 ESD

TVS1 与 TVS2 ESD5311 分别从 USB_N 与 USB_P 箝位到 GND。

- 参数与网络：`negative_line=USB_N -> TVS1 -> GND`；`positive_line=USB_P -> TVS2 -> GND`
- 证据：图 431347b4c4ad / 第 1 页 / A1 TYPEC，TVS1/TVS2 ESD5311 与 USB_N/USB_P

### USB 输入过压保护

U2 AW32901FCR 位于 VUSB_IN 与 5V_IN 之间，图中给出的过压阈值为 5.95V。

- 参数与网络：`input=VUSB_IN`；`output=5V_IN`；`ovp=5.95V`
- 证据：图 431347b4c4ad / 第 1 页 / A2 PROTECTION，U2 AW32901FCR 与 OVP=5.95V

### microSD 信号保护

TVS3-TVS9 ESD5311 对 G8_TF_DATA3、G9_TF_DATA2、G10_TF_DATA1、G11_TF_DATA0、G12_TF_CMD、G13_TF_CLK 和 PYB_TF_DET 提供对地 ESD 箝位。

- 参数与网络：`devices=TVS3,TVS4,TVS5,TVS6,TVS7,TVS8,TVS9`；`part_number=ESD5311`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / D2 TF，R62-R68 与 TVS3-TVS9 信号阵列

## 存储

### 外部 NOR Flash

U13 XM25UH128DHIQT 由 VDD_NOR 供电，CS#/SO/SCLK/SI/HOLD#/WP# 分别连接 NOR_CS/NOR_DO/NOR_SCK/NOR_DI/NOR_HOLD/NOR_WP。

- 参数与网络：`reference=U13`；`part_number=XM25UH128DHIQT`；`supply=VDD_NOR`；`signals=NOR_CS,NOR_DO,NOR_SCK,NOR_DI,NOR_HOLD,NOR_WP`
- 证据：图 ae396bd19142 / 第 1 页 / C3-C4 MCU_Core，U12 SPI Flash 引脚与 U13 XM25UH128DHIQT

### microSD 插卡检测

U20 卡座开关接 PYB_TF_DET；图下注释说明该信号用内部上拉检测对地连接，用于识别插卡并唤醒 ESP32。

- 参数与网络：`socket=U20`；`detect_net=PYB_TF_DET`；`receiver=U17 PYG1`；`pullup=R68 1M/1% to TF_3V3_L3`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / D2-D3 TF，U20 SW/PYB_TF_DET、R68 及底部英文检测/唤醒注释

## 音频

### PDM 数字麦克风总线

ESP32-S3 GPIO46 接 G46_PDM_DAT，GPIO45 接 G45_PDM_CLK；两线通过 AXE512127D 连接器到 PDM 子组件。

- 参数与网络：`data=GPIO46/G46_PDM_DAT`；`clock=GPIO45/G45_PDM_CLK`；`power=PDM_VDD`
- 证据：图 ae396bd19142 / 第 1 页 / A3-B3 U12 GPIO46/GPIO45 的 G46_PDM_DAT/G45_PDM_CLK; 图 0cdf2ccee1a8 / 第 1 页 / C1-D1 KEY&RGB&PDM，AXE512127D 与 PDM 数据/时钟/电源

### 蜂鸣器驱动

G42_BB_PWM 驱动 Q3 SK2302AAT 低边开关，蜂鸣器高端接 3V3_L2，D3 1N4148WS 跨接负载。

- 参数与网络：`control=GPIO42/G42_BB_PWM`；`supply=3V3_L2`；`switch=Q3 SK2302AAT`；`flyback_diode=D3 1N4148WS`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / A3 BUZZER，Q3/D3/蜂鸣器符号与 G42_BB_PWM/3V3_L2

## 传感器

### RTC 连接

RX8130CE U16 的 SCL/SDA 接 G48_SYS_SCL/G47_SYS_SDA，nIRQ 经 R47 22R 输出 PYG0_RTC_INT，并由 R49 100K 上拉到 3V3_L0。

- 参数与网络：`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`interrupt=PYG0_RTC_INT`；`series=R47 22R/1%`；`pullup=R49 100K/1% to 3V3_L0`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / A1 RTC，U16/R47/R49 与 G47/G48/PYG0_RTC_INT

### IMU 连接

BMI270 U15 的 SCx/SDx 接 G48_SYS_SCL/G47_SYS_SDA，INT1 经 R44 22R 输出 PYG4_IMU_INT，INT2、ASDx、ASCx、OCSB 与 OSDO 标为不连接或接地配置。

- 参数与网络：`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`interrupt=PYG4_IMU_INT`；`interrupt_pin=INT1`；`supply=3V3_L1`
- 证据：图 0cdf2ccee1a8 / 第 1 页 / A2 IMU，U15 BMI270 引脚、R44 与 3V3_L1/G47/G48/PYG4_IMU_INT

## 射频

### 主控射频天线

ANT1 PIFA 天线经 L5 0R、L4 LQP03TN2N6B02D 与 C39-C42 匹配网络接到 U12 LNA_IN；C39/C40 标为 NC(TBD)。

- 参数与网络：`antenna=ANT1 ANT_PIFA`；`soc_pin=U12 LNA_IN`；`series=L5 0R/1%, L4 LQP03TN2N6B02D`；`optional_caps=C39/C40 NC(TBD)`
- 证据：图 ae396bd19142 / 第 1 页 / A1-A2 MCU_Core 左上，ANT1 至 U12 LNA_IN 的 50ohm 射频链路

## 调试与烧录

### 调试测试点

TP1-TP12 引出 3V3_L0、VBUS_L0、3V3_L2_LoRa、3V3_L1、3V3_L2、GND、UART0 TX/RX、SOC_RESET、G0_BOOT_OUT、BAT_ADC_EN 与 PY_LED_R。

- 参数与网络：`TP1=3V3_L0`；`TP2=3V3_L2_LoRa`；`TP3=3V3_L2`；`TP4=G43_U0_TX`；`TP5=SOC_RESET`；`TP6=VBUS_L0`；`TP7=3V3_L1`；`TP8=GND`；`TP9=G44_U0_RX`；`TP10=G0_BOOT_OUT`；`TP11=BAT_ADC_EN`；`TP12=PY_LED_R`
- 证据：图 ae396bd19142 / 第 1 页 / D2-D3 DEBUG，TP1-TP12 标签与网络名

## 模拟电路

### USB 5V 采样

5V_IN 经 R19 10K 与 R21 10K 等值分压形成 5VIN_ADC，C12 100nF 对采样节点滤波。

- 参数与网络：`source=5V_IN`；`output=5VIN_ADC`；`upper=R19 10K/1%`；`lower=R21 10K/1%`；`filter=C12 100nF/25V`
- 证据：图 431347b4c4ad / 第 1 页 / B4 ADC_DET，R19/R21/C12 与 5VIN_ADC

### 电池电压采样

BAT_ADC_EN 驱动 Q1A/Q1B 门控 VBAT_L0 分压，R5 与 R12 均为 1K，分压节点输出 BAT_ADC 并由 C7 100nF 滤波。

- 参数与网络：`source=VBAT_L0`；`enable=BAT_ADC_EN`；`output=BAT_ADC`；`switch=Q1A/Q1B CJ3439KDW`；`divider=R5=1K,R12=1K`；`filter=C7 100nF/25V`
- 证据：图 431347b4c4ad / 第 1 页 / A4 ADC_DET，Q1A/Q1B、R3/R5/R11/R12/C7 与 BAT_ADC_EN/BAT_ADC

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统架构 | `soc=U12 ESP32_S3R8`；`pmic=U7 M5PM1`；`io_expander=U17 M5IOE1`；`system_i2c=G47_SYS_SDA/G48_SYS_SCL` |
| 系统结构 | 低功耗状态 | `L0=Shipping`；`L1=Standby`；`L2=DeepSleep`；`L3A=CORE ACTIVE`；`L3B=All ACTIVE` |
| 系统结构 | Lite 版本射频预留 | `lora_module=U14 DNP`；`lora_power=U9 DNP`；`rfid=DNP`；`reserved_nets=G38_SPI1_MOSI,G39_SPI1_CLK,G40_SPI1_MISO,G41_LoRa_NSS,G5_LoRa_INT,G21_LoRa_BUSY,G6_RFID_INT` |
| 电源 | USB 输入与充电路径 | `path=USB VBUS -> VUSB_IN -> U2 -> 5V_IN -> U1 -> VBAT_L0`；`protector=AW32901FCR`；`charger=IP2315` |
| 电源 | 系统母线来源 | `from=VBAT_L0`；`link=R20 0R/1%`；`to=VBUS_L0` |
| 电源 | 3V3_L0 电源域 | `input=VBUS_L0`；`output=3V3_L0`；`regulator=U4 SSP7615-33DFR`；`mode=Always On` |
| 电源 | 3V3_L1 电源域 | `input=VBUS_L0`；`output=3V3_L1`；`enable=3V3_L1_EN`；`load=BMI270` |
| 电源 | 3V3_L2 核心电源域 | `input=VBUS_L0`；`output=3V3_L2`；`enable=3V3_L2_EN`；`converter=U10 JW5712`；`diagram_rating=600mA` |
| 电源 | LoRa 预留电源 | `input=VBUS_L0`；`output=3V3_L2_LoRa`；`enable=PYG2_LoRa_EN`；`assembly=DNP` |
| 电源 | 电子纸 3.3V 开关 | `input=VBUS_L0`；`output=EPD_3V3_L3`；`enable=PYB_EPD_EN` |
| 电源 | microSD 电源开关 | `input=3V3_L2`；`output=TF_3V3_L3`；`enable=PYB_TF_EN` |
| 电源 | 触控电源开关 | `input=3V3_L2`；`output=TP_VDD`；`enable=PYB_TP_EN`；`loads=J4,U19 VCCA` |
| 电源 | PDM 麦克风电源开关 | `input=3V3_L2`；`output=PDM_VDD`；`enable=PYB_PDM_EN` |
| 电源 | 电子纸前光升压 | `input=EPD_3V3_L3`；`output=BL_15V_L3B`；`control=PYG3_BL_PWM`；`feedback=BL_FB`；`inductor=L3 10uH`；`diode=D2 RB162VAM-20TR` |
| 电源 | 电子纸偏压 | `input=EPD_3V3_L3`；`outputs=PREVGH,PREVGL`；`switch=Q4 CJ2310`；`inductor=L8 SPH252010H330MT`；`diodes=D4/D5/D6 1N5819WS` |
| 保护电路 | USB 数据线 ESD | `negative_line=USB_N -> TVS1 -> GND`；`positive_line=USB_P -> TVS2 -> GND` |
| 保护电路 | USB 输入过压保护 | `input=VUSB_IN`；`output=5V_IN`；`ovp=5.95V` |
| 保护电路 | microSD 信号保护 | `devices=TVS3,TVS4,TVS5,TVS6,TVS7,TVS8,TVS9`；`part_number=ESD5311` |
| 接口 | USB-C 接口 | `connector=USB TYPEC-302-BRP16SC08`；`power=VUSB_IN`；`data_plus=USB_P`；`data_minus=USB_N`；`cc_resistors=R4/R14 5.1K/1%` |
| 接口 | 电池接口 | `reference=J2`；`pin1=GND`；`pin2=VBAT_L0`；`capacitor=C13 22uF/10V` |
| 模拟电路 | USB 5V 采样 | `source=5V_IN`；`output=5VIN_ADC`；`upper=R19 10K/1%`；`lower=R21 10K/1%`；`filter=C12 100nF/25V` |
| 模拟电路 | 电池电压采样 | `source=VBAT_L0`；`enable=BAT_ADC_EN`；`output=BAT_ADC`；`switch=Q1A/Q1B CJ3439KDW`；`divider=R5=1K,R12=1K`；`filter=C7 100nF/25V` |
| 总线 | 系统 I2C 总线 | `sda=GPIO47/G47_SYS_SDA`；`scl=GPIO48/G48_SYS_SCL`；`pullups=R36/R37 2.2K/1% to 3V3_L2` |
| 总线地址 | M5PM1 I2C 地址 | `reference=U7`；`address=0x6E`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL` |
| 总线地址 | M5IOE1 I2C 地址 | `reference=U17`；`address=0x4F`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL` |
| 总线地址 | RTC I2C 地址 | `reference=U16`；`address=0x32`；`interrupt=PYG0_RTC_INT` |
| 总线地址 | IMU I2C 地址 | `reference=U15`；`address=0x68`；`interrupt=PYG4_IMU_INT` |
| 总线 | 充电器 I2C 隔离 | `system_side=G47_SYS_SDA/G48_SYS_SCL at 3V3_L2`；`charger_side=CHG_SYS_SDA/CHG_SYS_SCL at VBAT_L0`；`enable=PYB_CHG_IIC`；`translator=U3 AW39112DNR` |
| 总线 | 触控 I2C 接口 | `scl_system=G48_SYS_SCL`；`sda_system=G47_SYS_SDA`；`scl_touch=TP_SYS_SCL`；`sda_touch=TP_SYS_SDA`；`interrupt=G4_TP_INT`；`reset=PYB_TP_RST` |
| 总线 | 电子纸 SPI | `mosi=GPIO14/G14_SPI2_MOSI`；`clock=GPIO15/G15_SPI2_CLK`；`chip_select=GPIO16/G16_EINK_CS`；`data_command=GPIO17/G17_EINK_DC`；`busy=GPIO18/G18_EINK_BUSY`；`reset=PYB_EINK_RST` |
| 总线 | microSD 数据总线 | `DAT3=GPIO8/G8_TF_DATA3`；`DAT2=GPIO9/G9_TF_DATA2`；`DAT1=GPIO10/G10_TF_DATA1`；`DAT0=GPIO11/G11_TF_DATA0`；`CMD=GPIO12/G12_TF_CMD`；`CLK=GPIO13/G13_TF_CLK` |
| 音频 | PDM 数字麦克风总线 | `data=GPIO46/G46_PDM_DAT`；`clock=GPIO45/G45_PDM_CLK`；`power=PDM_VDD` |
| 音频 | 蜂鸣器驱动 | `control=GPIO42/G42_BB_PWM`；`supply=3V3_L2`；`switch=Q3 SK2302AAT`；`flyback_diode=D3 1N4148WS` |
| 传感器 | RTC 连接 | `scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`interrupt=PYG0_RTC_INT`；`series=R47 22R/1%`；`pullup=R49 100K/1% to 3V3_L0` |
| 传感器 | IMU 连接 | `scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`interrupt=PYG4_IMU_INT`；`interrupt_pin=INT1`；`supply=3V3_L1` |
| GPIO 与控制信号 | 用户按键 | `key1=GPIO2/G2_KEY1`；`key2=GPIO3/G3_KEY2`；`power_button=PWR_BTN -> M5PM1 BTN_PU` |
| GPIO 与控制信号 | M5IOE1 中断 | `source=U17 OD_INTOUT pin 2`；`net=G7_PYB_IRQ`；`destination=U12 GPIO7`；`pullup=R53 10K/1% to 3V3_L2` |
| GPIO 与控制信号 | 触控控制信号 | `interrupt=GPIO4/G4_TP_INT`；`reset=U17 PYG6/PYB_TP_RST`；`power_enable=U17 PYG13/PYB_TP_EN` |
| GPIO 与控制信号 | 电子纸扩展控制 | `reset=U17 PYG5_ADC3/PYB_EINK_RST`；`power_enable=U17 PYG3/PYB_EPD_EN`；`backlight_pwm=U7 G3_WAKEin/PYG3_BL_PWM` |
| GPIO 与控制信号 | microSD 电源与检测 | `power_enable=U17 PYG14/PYB_TF_EN`；`detect=U17 PYG1/PYB_TF_DET` |
| GPIO 与控制信号 | RGB LED 控制 | `red=U7 LED_EN_PP/PY_LED_R`；`green=U17 PYG8_PWM2/PYB_LED_G`；`blue=U17 PYG9_PWM1/PYB_LED_B` |
| GPIO 与控制信号 | M5PM1 电源控制输出 | `l2_enable=DCDC3V3_EN_PP/3V3_L2_EN`；`l1_enable=LDO3V3_EN_PP/3V3_L1_EN`；`not_connected=BOOST5V_EN_PP,CHG_EN_PP` |
| GPIO 与控制信号 | 启动控制 | `pmic_pin=U7 BOOT_OUT_OD`；`net=G0_BOOT_OUT`；`soc_pin=U12 GPIO0[strap]`；`pullup=R33 10K/1% to 3V3_L2` |
| 复位 | ESP32-S3 复位 | `soc_pin=U12 CHIP_PU`；`net=SOC_RESET`；`pullup=R31 10K/1%`；`capacitor=C53 1uF/25V`；`series=R32 0R/1%` |
| 复位 | M5IOE1 复位 | `reference=U17`；`pin=NRST`；`net=RST`；`pullup=R51 to 3V3_L2`；`test_point=TP15` |
| 时钟 | ESP32-S3 主晶振 | `crystal=X1 CN4040M000157A530001`；`nets=XTAL_P,XTAL_N`；`series_inductor=L7 24nH`；`load_capacitors=C45=24pF,C50=24pF` |
| 存储 | 外部 NOR Flash | `reference=U13`；`part_number=XM25UH128DHIQT`；`supply=VDD_NOR`；`signals=NOR_CS,NOR_DO,NOR_SCK,NOR_DI,NOR_HOLD,NOR_WP` |
| 存储 | microSD 插卡检测 | `socket=U20`；`detect_net=PYB_TF_DET`；`receiver=U17 PYG1`；`pullup=R68 1M/1% to TF_3V3_L3` |
| 射频 | 主控射频天线 | `antenna=ANT1 ANT_PIFA`；`soc_pin=U12 LNA_IN`；`series=L5 0R/1%, L4 LQP03TN2N6B02D`；`optional_caps=C39/C40 NC(TBD)` |
| 调试与烧录 | 调试测试点 | `TP1=3V3_L0`；`TP2=3V3_L2_LoRa`；`TP3=3V3_L2`；`TP4=G43_U0_TX`；`TP5=SOC_RESET`；`TP6=VBUS_L0`；`TP7=3V3_L1`；`TP8=GND`；`TP9=G44_U0_RX`；`TP10=G0_BOOT_OUT`；`TP11=BAT_ADC_EN`；`TP12=PY_LED_R` |
| 接口 | 电子纸 FPC | `connector=J5 FPC0.5-SMT-24P-B`；`logic_supply=EPD_3V3_L3`；`logic_signals=G14_SPI2_MOSI,G15_SPI2_CLK,G16_EINK_CS,G17_EINK_DC,G18_EINK_BUSY,PYB_EINK_RST`；`bias_signals=GDR,RESE,PREVGH,PREVGL` |
| 总线 | UART0 调试串口 | `tx=GPIO43/G43_U0_TX/TP4`；`rx=GPIO44/G44_U0_RX/TP9`；`tx_series=R30 499R/1%` |
| 接口 | 按键/RGB/PDM 连接器 | `part_number=AXE512127D`；`power=3V3_L2,3V3_L0,PDM_VDD,GND`；`signals=PY_LED_R,PYB_LED_G,PYB_LED_B,PWR_BTN,G2_KEY1,G3_KEY2,G45_PDM_CLK,G46_PDM_DAT` |
| 系统结构 | 唤醒源 | `pmic_wake0=PYG0_RTC_INT`；`pmic_wake4=PYG4_IMU_INT`；`soc_io_wake=G7_PYB_IRQ,G4_TP_INT,G2_KEY1,G3_KEY2` |
| 电源 | 充电电流设定 | `overview_label=0.5C`；`charger_label=Ipeak 1.5A`；`ichgset=U1 pin27 with R17 15K/1%` |
| 核心器件 | 触控控制器型号与地址 | `visible_interface=J4`；`document_claim=FT6336G/0x38`；`schematic_status=controller not shown` |
| 核心器件 | 电子纸控制器型号 | `visible_interface=J5 FPC0.5-SMT-24P-B`；`document_claim=SSD1677`；`schematic_status=controller not shown` |
| 音频 | PDM 麦克风型号 | `visible_interface=AXE512127D`；`document_claim=LMD4737T261-AC02`；`schematic_status=microphone device not shown` |

## 待确认事项

- `uncertain.charge-current`：系统总览标注充电电流 0.5C，而 U1 充电页标注 Ipeak 1.5A 并给出 ICHGSET 电阻网络；四页内容不能唯一确定实际恒流充电设定值。（证据：图 fcf5a820e5f2 / 第 1 页 / A3-A4 Power Network，IP2315 旁标注 充电电流 0.5C; 图 431347b4c4ad / 第 1 页 / A3 CHARG，5V_IN 旁 Ipeak 1.5A 与 U1 ICHGSET/R17 网络）
- `uncertain.touch-controller`：四页原理图只绘出 J4 触控接口、U18 电源开关与 U19 I2C 电平转换器，未绘出面板侧触控控制器型号或 I2C 地址，无法由这些页面独立复核源文档中的 FT6336G/0x38。（证据：图 0cdf2ccee1a8 / 第 1 页 / B3-C4 TP，U18/U19/J4 仅显示电源、总线、中断和复位接口）
- `uncertain.epd-controller`：四页原理图只绘出 J5 电子纸 FPC、SPI/控制信号和偏压电路，未绘出面板侧控制器型号，无法由这些页面独立复核源文档中的 SSD1677。（证据：图 0cdf2ccee1a8 / 第 1 页 / B5-D6 EINK，偏压电路与 J5 FPC，未出现 SSD1677 器件符号）
- `uncertain.microphone-model`：四页原理图只在 AXE512127D 连接器显示 G46_PDM_DAT、G45_PDM_CLK 与 PDM_VDD，未绘出麦克风器件型号，无法由这些页面独立复核源文档中的 LMD4737T261-AC02。（证据：图 0cdf2ccee1a8 / 第 1 页 / C1-D1 KEY&RGB&PDM，连接器与 U21 仅显示 PDM 接口和电源）
- `review.charge-current`：IP2315 的实际恒流充电设定值是多少，0.5C、1.5A 峰值与 ICHGSET 网络应如何对应？；原因：系统总览与充电细页给出不同口径，且仅凭图中电阻网络不能闭合实际配置。
- `review.touch-controller`：面板侧触控控制器是否为 FT6336G，量产固件使用的 I2C 地址是否为 0x38？；原因：主板原理图止于 J4，不包含面板侧触控控制器符号或地址标注。
- `review.epd-controller`：J5 所接电子纸模组的控制器是否为 SSD1677？；原因：主板原理图只显示 FPC 信号与偏压，未显示面板控制器器件。
- `review.microphone-model`：AXE512127D 所接 PDM 麦克风实装型号是否为 LMD4737T261-AC02？；原因：四页主板原理图只给出 PDM 数据、时钟和电源网络，未出现麦克风型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fcf5a820e5f2fb3b691c13d1f9e7d9f6a41c741aa5e8ba4f0d07b7d0e975f40b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_02.png` |
| 2 | 1 | `431347b4c4addf9ac195282f0817c9b03094773983f5d470d7a512957cb3265f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_03.png` |
| 3 | 1 | `ae396bd191420610ba9943a9018c0013b16bc29de1b3d63bb7bfd562dd0c6174` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_04.png` |
| 4 | 1 | `0cdf2ccee1a8167dc74f050961f3ca34f00229b03790eea52a2dc65fe52982c1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_05.png` |

---

源文档：`zh_CN/core/PaperMono-Lite.md`

源文档 SHA-256：`7b6949df2252c7ea73b07fd1335c8d3ae2512268faa7cf24c9f08f444dfdf161`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
