# PaperMono 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PaperMono |
| SKU | C153 |
| 产品 ID | `papermono-59c8b1a7cae9` |
| 源文档 | `zh_CN/core/PaperMono.md` |

## 概述

PaperMono 以 ESP32-S3R8 为主控，由 M5PM1 电源管理器和 M5IOE1 I/O 扩展器协调多级电源域、唤醒源及外设使能。板上原理图覆盖 USB Type-C 输入与 IP2315 充电、外部 NOR Flash、microSD、PDM 麦克风、RTC、IMU、LoRa 模组、电子纸接口和前光升压链路。独立 NFC 子板采用 ST25R3916-AQWT、27.12 MHz 晶振以及 13.56 MHz 线圈匹配网络，并通过板对板连接器接入系统 I2C、复位和中断信号。图面未直接展示触控控制器与电子纸面板内部器件，因此相关型号、地址及显示参数保留为待确认事实。

## 检索关键词

`PaperMono`、`C153`、`ESP32-S3R8`、`M5PM1`、`0x6E`、`M5IOE1`、`0x4F`、`IP2315`、`AW32901FCR`、`SSP7615-33DFR`、`JW5712`、`AW9967DNR`、`RX8130CE`、`0x32`、`BMI270`、`0x68`、`Stamp-LoRa-1262-mini`、`ST25R3916-AQWT`、`LMD4737T261-AC02`、`microSD`、`USB Type-C`、`G47_SYS_SDA`、`G48_SYS_SCL`、`G38_SPI1_MOSI`、`G40_SPI1_MISO`、`G39_SPI1_CLK`、`G14_SPI2_MOSI`、`G15_SPI2_CLK`、`EPD_3V3_L3B`、`TF_3V3_L3`、`TP_VDD`、`PDM_VDD`、`BL_15V_L3B`、`BAT_ADC`、`5VIN_ADC`、`PWR_BTN`、`G2_KEY1`、`G3_KEY2`、`G6_RFID_INT`、`ANT_NFC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| USB | TYPEC-302-BRP16SC08 | 主 USB Type-C 电源与 USB 2.0 数据连接器 | 图 52af03768faf / 第 1 页 / A1 TYPEC 分区，USB 连接器符号及 VUSB_IN、USB_N、USB_P、CC1、CC2 网络 |
| TVS1, TVS2 | ESD5311 | USB_N 与 USB_P 数据线 ESD 保护 | 图 52af03768faf / 第 1 页 / A1 TYPEC 分区，TVS1/TVS2 从 USB_N/USB_P 接至 GND |
| U2 (PROTECTION) | AW32901FCR | VUSB_IN 到 5V_IN 的输入过压保护开关 | 图 52af03768faf / 第 1 页 / A2 PROTECTION 分区，U2 标注 AW32901FCR、OVP=5.95V |
| U1 (CHARG) | IP2315 | 5V_IN 输入的电池充电管理器 | 图 52af03768faf / 第 1 页 / A3 CHARG 分区，U1 IP2315、LX/BAT/VSYS 与 CHG_SYS_SCL/SDA 引脚 |
| J2 | CON2_SMD | 两针电池连接器 | 图 52af03768faf / 第 1 页 / B2 Battery 分区，J2 接 VBAT_L0 与 GND |
| U4, U5, U6, U9 | SSP7615-33DFR | 3.3 V L0/L1、电子纸和 LoRa 分域 LDO | 图 52af03768faf / 第 1 页 / B1-D2 L0_SW、L1_SW、L2_SW 与 L3_SW/EPD_3V3 分区 |
| U10 | JW5712 | VBUS_L0 到 3V3_L2 的受控降压转换器 | 图 52af03768faf / 第 1 页 / D1 L2_SW 分区，U10 JW5712、EN=3V3_L2_EN、输出 3V3_L2 |
| U8, U18, U21 | AW35122FDR | microSD、触控接口和 PDM 麦克风的受控电源负载开关 | 图 52af03768faf / 第 1 页 / C3 TF_3V3V 分区，U8 从 3V3_L2 产生 TF_3V3_L3; 图 88b42aecfd86 / 第 1 页 / B4 TP 与 D1 KEY&RGB&PDM 分区，U18/U21 分别产生 TP_VDD/PDM_VDD |
| U11 | AW9967DNR | 电子纸前光升压和恒流控制器 | 图 52af03768faf / 第 1 页 / D2 EINK_BL 分区，U11、L3、D2、BL_FB 与 BL_15V_L3B |
| U3, U19 | AW39112DNR | 充电器 I2C 与触控 I2C 的双电源域电平转换器 | 图 52af03768faf / 第 1 页 / B3 CHARG 分区，U3 在 3V3_L2 与 VBAT_L0 域之间转换 CHG_SYS_SCL/SDA; 图 88b42aecfd86 / 第 1 页 / B3-B4 TP 分区，U19 在 TP_VDD 与 3V3_L2 域之间转换 I2C |
| U7 | M5PM1 | 多级电源管理、按键、ADC、IRQ 与外设使能控制器 | 图 52af03768faf / 第 1 页 / C4-D4 PMIC 分区，U7 M5PM1 与 IIC Address:0x6E 标注 |
| Q1A, Q1B | CJ3439KDW | 受 BAT_ADC_EN 控制的电池电压采样门控电路 | 图 52af03768faf / 第 1 页 / A4 ADC_DET 分区，Q1A/Q1B、BAT_ADC_EN 与 BAT_ADC 分压链 |
| U12 | ESP32_S3R8 | 主控 SoC | 图 f547ea1ebc45 / 第 1 页 / B3-C3 MCU_Core 分区，U12 器件标注 ESP32_S3R8 |
| ANT1 (MCU) | ANT_PIFA | ESP32-S3 射频天线及匹配网络端点 | 图 f547ea1ebc45 / 第 1 页 / A1-A2 MCU_Core 左上，ANT1 ANT_PIFA 经 L5/L4 接 U12 LNA_IN |
| X1 (MCU) | CN4040M000157A530001 | ESP32-S3 主晶振 | 图 f547ea1ebc45 / 第 1 页 / A4-B4 MCU_Core 右上，X1 位于 XTAL_P/XTAL_N 与 C45/C50 之间 |
| U13 | XM25UH128DHIQT | ESP32-S3 外部 NOR Flash | 图 f547ea1ebc45 / 第 1 页 / C4 MCU_Core 右侧，U13 与 NOR_CS/DO/SCK/DI/HOLD/WP 网络 |
| FT1 | ICMF062P900MFR | USB 差分线共模滤波器 | 图 f547ea1ebc45 / 第 1 页 / D1 DEBUG 左侧，FT1 位于 USB_N/P 与 G19_USB_N/G20_USB_P 之间 |
| U16 | RX8130CE | I2C 实时时钟与低功耗中断源 | 图 88b42aecfd86 / 第 1 页 / A1 RTC 分区，U16 RX8130CE 与 IIC Address:0x32 |
| U15 | BMI270 | I2C IMU 与中断源 | 图 88b42aecfd86 / 第 1 页 / A2 IMU 分区，U15 BMI270 与 IIC Address:0x68 |
| Q3, D3 | SK2302AAT / 1N4148WS | 蜂鸣器低边驱动与反向钳位 | 图 88b42aecfd86 / 第 1 页 / A3 BUZZER 分区，G42_BB_PWM 驱动 Q3，D3 跨接蜂鸣器支路 |
| U14 | Stamp-LoRa-1262-mini | LoRa SPI 无线模组 | 图 88b42aecfd86 / 第 1 页 / A5-A6 LoRa 分区，U14 标注 Stamp-LoRa-1262-mini |
| U17 | M5IOE1 | I2C I/O 扩展、外设复位、供电使能、PWM 与状态检测控制器 | 图 88b42aecfd86 / 第 1 页 / B1-B2 PYB_IIC 分区，U17 M5IOE1 与 IIC Address:0x4F |
| J4 | 未标注 | 触控面板 I2C、中断与复位连接器 | 图 88b42aecfd86 / 第 1 页 / B3-B4 TP 分区，J4 引出 TP_SYS_SCL、TP_SYS_SDA、G4_TP_INT、PYB_TP_RST、TP_VDD 与 GND |
| U20 | MicroSD | microSD 卡座 | 图 88b42aecfd86 / 第 1 页 / D2-D3 TF 分区，U20 MicroSD 的 DAT0-DAT3、CMD、CLK 与 SW 引脚 |
| J5 | FPC0.5-SMT-24P-B | 电子纸面板 24 针 FPC 连接器 | 图 88b42aecfd86 / 第 1 页 / C5-D6 EINK 分区，J5 连接 SPI、BUSY、RST、GDR/RESE 与 PREVGH/PREVGL |
| Q4, L8, D4-D6 | CJ2310 / SPH252010H330MT / 1N5819WS | 电子纸面板高压偏置生成网络 | 图 88b42aecfd86 / 第 1 页 / B5-B6 EINK 分区，EPD_3V3_L3、GDR/RESE 与 PREVGH/PREVGL 网络 |
| S1, S2, S3 | SW | 电源按键和两个用户按键 | 图 920bd393c299 / 第 1 页 / A1-B1 KEY 分区，S1=PWR_BTN、S2=G2_KEY1、S3=G3_KEY2 |
| U1 (PDM) | LMD4737T261-AC02 | PDM 数字 MEMS 麦克风 | 图 920bd393c299 / 第 1 页 / A2-B3 PDM 分区，U1 DAT=G46_PDM_DAT、CLK=G45_PDM_CLK |
| LED1 | RS-C1415MBAR | 三色 RGB 指示灯 | 图 920bd393c299 / 第 1 页 / C1 RGB 分区，LED1 的 PYB_LED_B、PYB_LED_G、PY_LED_R 支路 |
| J1 (NFC BTB) | BTB0.408-10PLBDR-G41 | NFC 子板与主板之间的板对板连接器 | 图 41848ade172b / 第 1 页 / A1 Mono BTB 分区，J1 引出 3V3_L2、G48_SYS_SCL、G47_SYS_SDA、G6_RFID_INT、PYB_RFID_RST |
| U2 (NFC) | ST25R3916-AQWT | NFC/RFID 收发器 | 图 41848ade172b / 第 1 页 / B2-C2 Paper Mono NFC 分区，U2 ST25R3916-AQWT |
| X1 (NFC) | 未标注 | ST25R3916 的 27.12 MHz 晶振 | 图 41848ade172b / 第 1 页 / C1-C2 NFC 分区，X1 标注 27.12MHZ 并连接 U2 XTO/XTI |
| ANT1 (NFC) | ANT_NFC | 13.56 MHz NFC PCB 线圈及差分匹配网络 | 图 41848ade172b / 第 1 页 / B3-B4 NFC 天线分区，RFI_P/RFI_N 经 L1/L2、C2-C13、R3/R5 接 ANT1 |
| DR1, DR2, DR3 | ESD5311 | 电源键与用户按键网络 ESD 保护 | 图 920bd393c299 / 第 1 页 / A1-B1 KEY 分区，DR1-DR3 分别跨接 PWR_BTN、G2_KEY1、G3_KEY2 到 GND |
| TVS3-TVS9 | ESD5311 | microSD 数据信号和检测信号 ESD 保护阵列 | 图 88b42aecfd86 / 第 1 页 / D2 TF 分区，TVS3-TVS9 连接 DAT2、DAT3、CMD、CLK、DAT0、DAT1、PYB_TF_DET |
| J1 (EINK_BL) | 未标注 | 电子纸前光输出与反馈连接器 | 图 52af03768faf / 第 1 页 / D2-D3 EINK_BL 分区，J1 引出 BL_15V_L3B 与 BL_FB |

## 系统结构

### 系统功能分区

系统总览将 ESP32-S3R8 主控、M5PM1 电源管理、M5IOE1 I/O 扩展、电子纸、触控、RTC、IMU、LoRa、RFID、microSD、RGB、PDM 麦克风和蜂鸣器组织为同一平台。

- 参数与网络：`soc=ESP32-S3-R8`；`pmic=M5PM1`；`io_expander=M5IOE1`
- 证据：图 d60bc2217ff3 / 第 1 页 / A1-B8 Functions、Power Network 与 I/Os Map 总览

### 电源状态层级

Power Mode 图定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE 和 L3B All ACTIVE 五个状态层级。

- 参数与网络：`L0=Shipping`；`L1=Standby`；`L2=DeepSleep`；`L3A=CORE ACTIVE`；`L3B=All ACTIVE`
- 证据：图 d60bc2217ff3 / 第 1 页 / C1-D3 Power Mode 状态图和 A5-A8 Power Network 状态列

### L2 到活动态唤醒源

状态图列出单击 KEY1/2、触控中断、LoRa_INT 和 RFID_INT 作为 ESP32-S3 I/O 唤醒源，并列出 M5PM1 拉低 IRQ 的唤醒路径。

- 参数与网络：`gpio_wake=G2_KEY1, G3_KEY2, G4_TP_INT, G5_LoRa_INT, G6_RFID_INT`；`pmic_irq=G1_PY_IRQ`
- 证据：图 d60bc2217ff3 / 第 1 页 / C1-D3 Power Mode 图，L2 到 L3A 的 S3_IO Wake-up/PM1 条目

## 电源

### 5 V 输入保护

AW32901FCR 位于 VUSB_IN 与 5V_IN 之间，图中标注过压阈值 OVP=5.95V。

- 参数与网络：`reference=U2`；`input=VUSB_IN`；`output=5V_IN`；`ovp=5.95V`
- 证据：图 52af03768faf / 第 1 页 / A2 PROTECTION 分区，U2 AW32901FCR

### 电池充电路径

IP2315 的 VIN/VSYS 侧接 5V_IN，LX 侧经 L1 与 D1 形成开关节点，BAT 引脚输出到 VBAT_L0，图中同时标注 Ipeak 1.5A。

- 参数与网络：`reference=U1`；`part_number=IP2315`；`input=5V_IN`；`battery_net=VBAT_L0`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`ipeak=1.5A`
- 证据：图 52af03768faf / 第 1 页 / A2-A3 CHARG 分区，U1、L1、D1 与 VBAT_L0

### VBAT_L0 与 VBUS_L0

VBAT_L0 通过 R20 0 Ω 连接 VBUS_L0，后者作为 L0/L1/L2 与电子纸分域电源转换器的上游母线。

- 参数与网络：`link=R20 0R/1%`；`upstream=VBAT_L0`；`downstream=VBUS_L0`
- 证据：图 52af03768faf / 第 1 页 / B1 L0_SW 上方 R20，以及 L0/L1/L2/L3_SW 各分区的 VBUS_L0 输入

### 3V3_L0 常开电源轨

U4 SSP7615-33DFR 的 VIN 与 EN 同接 VBUS_L0，输出 3V3_L0，因此图中该 LDO 未设置独立控制网络。

- 参数与网络：`reference=U4`；`input=VBUS_L0`；`enable=VBUS_L0`；`output=3V3_L0`
- 证据：图 52af03768faf / 第 1 页 / B1 L0_SW 分区，U4 VIN/EN 与 OUT

### 3V3_L1 电源轨

U6 SSP7615-33DFR 从 VBUS_L0 生成 3V3_L1，使能网络为 3V3_L1_EN。

- 参数与网络：`reference=U6`；`input=VBUS_L0`；`enable=3V3_L1_EN`；`output=3V3_L1`
- 证据：图 52af03768faf / 第 1 页 / C1 L1_SW 分区

### LoRa 分域电源

U9 SSP7615-33DFR 从 VBUS_L0 生成 3V3_L2_LoRa，使能网络为 PYG2_LoRa_EN。

- 参数与网络：`reference=U9`；`input=VBUS_L0`；`enable=PYG2_LoRa_EN`；`output=3V3_L2_LoRa`
- 证据：图 52af03768faf / 第 1 页 / C1-C2 L2_SW 分区 U9

### 3V3_L2 核心活动电源轨

U10 JW5712 从 VBUS_L0 降压生成 3V3_L2，3V3_L2_EN 控制 EN，输出端经 L2 和 C33-C36 滤波；总览将该转换器标为 600 mA。

- 参数与网络：`reference=U10`；`input=VBUS_L0`；`enable=3V3_L2_EN`；`output=3V3_L2`；`rated_current_label=600mA`
- 证据：图 52af03768faf / 第 1 页 / D1-D2 L2_SW 分区 U10 JW5712; 图 d60bc2217ff3 / 第 1 页 / A6-B7 Power Network 中 JW5712 DCDC 600mA

### 电子纸 3.3 V 分域

U5 SSP7615-33DFR 从 VBUS_L0 生成 EPD_3V3_L3，PYB_EPD_EN 控制其 EN。

- 参数与网络：`reference=U5`；`input=VBUS_L0`；`enable=PYB_EPD_EN`；`output=EPD_3V3_L3`
- 证据：图 52af03768faf / 第 1 页 / C2 L3_SW EPD_3V3 分区

### microSD 电源分域

U8 AW35122FDR 从 3V3_L2 生成 TF_3V3_L3，PYB_TF_EN 控制其 EN。

- 参数与网络：`reference=U8`；`input=3V3_L2`；`enable=PYB_TF_EN`；`output=TF_3V3_L3`
- 证据：图 52af03768faf / 第 1 页 / C3 TF_3V3V 分区

### 触控接口电源分域

U18 AW35122FDR 从 3V3_L2 生成 TP_VDD，PYB_TP_EN 控制其 EN。

- 参数与网络：`reference=U18`；`input=3V3_L2`；`enable=PYB_TP_EN`；`output=TP_VDD`
- 证据：图 88b42aecfd86 / 第 1 页 / B3-B4 TP 分区 U18

### PDM 麦克风电源分域

U21 AW35122FDR 从 3V3_L2 生成 PDM_VDD，PYB_PDM_EN 控制其 EN。

- 参数与网络：`reference=U21`；`input=3V3_L2`；`enable=PYB_PDM_EN`；`output=PDM_VDD`
- 证据：图 88b42aecfd86 / 第 1 页 / D1 KEY&RGB&PDM 分区 U21

### 电子纸前光电源

AW9967DNR 以 EPD_3V3_L3 为输入，经 L3 和 D2 升压到 BL_15V_L3B，PYG3_BL_PWM 接 CTRL，BL_FB 接反馈网络。

- 参数与网络：`reference=U11`；`input=EPD_3V3_L3`；`control=PYG3_BL_PWM`；`output=BL_15V_L3B`；`feedback=BL_FB`
- 证据：图 52af03768faf / 第 1 页 / D2-D3 EINK_BL 分区

### 电子纸高压偏置网络

EPD_3V3_L3 通过 L8、Q4 CJ2310 和 D4-D6 1N5819WS 形成 PREVGH、PREVGL、GDR 与 RESE 网络，并将 PREVGH/PREVGL 接到 J5。

- 参数与网络：`input=EPD_3V3_L3`；`inductor=L8 SPH252010H330MT`；`transistor=Q4 CJ2310`；`diodes=D4-D6 1N5819WS`；`outputs=PREVGH, PREVGL, GDR, RESE`
- 证据：图 88b42aecfd86 / 第 1 页 / B5-B6 EINK 偏置网络与 C5-D6 J5

### NFC 子板受控电源

NFC 子板 U1 从 3V3_L2 生成 VCC_3V3，EN 由 PYB_RFID_RST 控制；R1 0 Ω 连接输入与输出供电节点，R2 标为 NC。

- 参数与网络：`reference=U1`；`input=3V3_L2`；`output=VCC_3V3`；`enable=PYB_RFID_RST`；`bypass=R1 0R`；`optional_resistor=R2 NC`
- 证据：图 41848ade172b / 第 1 页 / A2 Mono BTB 电源开关 U1、R1、R2

### NFC 掉电电流图注

NFC 子页图注明确标出 operation control register 的 en=0 时，Power-down mode 供电电流 I=2.5 µA。

- 参数与网络：`mode=Power-down`；`condition=operation control register en=0`；`supply_current=2.5uA`
- 证据：图 41848ade172b / 第 1 页 / D1 NFC 页左下 Supply current in Power-down mode 图注

## 接口

### USB Type-C 接口

USB Type-C 连接器将 VBUS 汇为 VUSB_IN，USB 2.0 数据线汇为 USB_N 和 USB_P，CC1 与 CC2 各经 5.1 kΩ 电阻接地。

- 参数与网络：`connector=TYPEC-302-BRP16SC08`；`power_net=VUSB_IN`；`data_n=USB_N`；`data_p=USB_P`；`cc_resistors=R4/R14 5.1K/1%`
- 证据：图 52af03768faf / 第 1 页 / A1 TYPEC 分区，USB 引脚、R4、R14 与网络标注

### 电池连接器

J2 为两针电池连接器，针 2 接 VBAT_L0，针 1 接 GND，并在连接器处并联 C13 22 µF/10 V。

- 参数与网络：`reference=J2`；`pin_2=VBAT_L0`；`pin_1=GND`；`capacitor=C13 22uF/10V`
- 证据：图 52af03768faf / 第 1 页 / B2 Battery 分区，J2 与 C13

### ESP32-S3 原生 USB 数据链

USB_N/USB_P 经过 R40/R41 两个 22 Ω 电阻和 FT1 共模滤波器后分别连接 G19_USB_N/G20_USB_P，即 U12 GPIO19/GPIO20。

- 参数与网络：`usb_n=USB_N -> R40 -> FT1 -> G19_USB_N -> GPIO19`；`usb_p=USB_P -> R41 -> FT1 -> G20_USB_P -> GPIO20`；`series_resistors=R40/R41 22R/1%`；`filter=FT1 ICMF062P900MFR`
- 证据：图 f547ea1ebc45 / 第 1 页 / D1 USB 差分线与 B2-C2 U12 GPIO19/GPIO20

### NFC 子板连接

NFC 子板 J1 将 3V3_L2、G48_SYS_SCL、G47_SYS_SDA、G6_RFID_INT 与 PYB_RFID_RST 接入主板，其余偶数信号针和外壳焊盘接 GND。

- 参数与网络：`connector=J1 BTB0.408-10PLBDR-G41`；`pin_1=3V3_L2`；`pin_3=G48_SYS_SCL`；`pin_5=G47_SYS_SDA`；`pin_7=G6_RFID_INT`；`pin_9=PYB_RFID_RST`；`ground_pins=2,4,6,8,10,11-14`
- 证据：图 41848ade172b / 第 1 页 / A1 Mono BTB 分区 J1

## 总线

### 系统 I2C 总线

ESP32-S3 的 GPIO47 和 GPIO48 分别连接 G47_SYS_SDA 与 G48_SYS_SCL，并由 R36/R37 两个 2.2 kΩ 电阻上拉到 3V3_L2。

- 参数与网络：`sda=GPIO47/G47_SYS_SDA`；`scl=GPIO48/G48_SYS_SCL`；`pullups=R36/R37 2.2K/1%`；`pullup_rail=3V3_L2`
- 证据：图 f547ea1ebc45 / 第 1 页 / C1 IIC PULL_UP 与 C3 U12 GPIO47/GPIO48

### 充电器 I2C 接入控制

U3 AW39112DNR 将 G48_SYS_SCL/G47_SYS_SDA 转换到 CHG_SYS_SCL/CHG_SYS_SDA，OE 由 PYB_CHG_IIC 控制并经 R22 100 kΩ 下拉。

- 参数与网络：`translator=U3 AW39112DNR`；`controller_side=G48_SYS_SCL, G47_SYS_SDA`；`charger_side=CHG_SYS_SCL, CHG_SYS_SDA`；`enable=PYB_CHG_IIC`；`enable_pulldown=R22 100K/1%`
- 证据：图 52af03768faf / 第 1 页 / B3 CHARG 分区 U3 与 R22

### LoRa SPI 总线

Stamp-LoRa-1262-mini 的 SPI_MOSI、SPI_MISO、SPI_CLK、SX_NSS 分别连接 G38_SPI1_MOSI、G40_SPI1_MISO、G39_SPI1_CLK、G41_LoRa_NSS。

- 参数与网络：`module=U14 Stamp-LoRa-1262-mini`；`mosi=G38_SPI1_MOSI`；`miso=G40_SPI1_MISO`；`sclk=G39_SPI1_CLK`；`cs=G41_LoRa_NSS`
- 证据：图 88b42aecfd86 / 第 1 页 / A5-A6 LoRa 分区 U14 右侧 SPI 网络

### 触控 I2C 接口

U19 AW39112DNR 将 G48_SYS_SCL/G47_SYS_SDA 转换到 TP_SYS_SCL/TP_SYS_SDA，J4 同时引出 G4_TP_INT、PYB_TP_RST、TP_VDD 和 GND。

- 参数与网络：`translator=U19 AW39112DNR`；`controller_side=G48_SYS_SCL, G47_SYS_SDA`；`panel_side=TP_SYS_SCL, TP_SYS_SDA`；`interrupt=G4_TP_INT`；`reset=PYB_TP_RST`；`power=TP_VDD`
- 证据：图 88b42aecfd86 / 第 1 页 / B3-B4 TP 分区 U19 与 J4

### 电子纸 SPI 接口

电子纸 FPC J5 将 G14_SPI2_MOSI、G15_SPI2_CLK、G16_EINK_CS、G17_EINK_DC、G18_EINK_BUSY 和 PYB_EINK_RST 引至面板侧。

- 参数与网络：`mosi=GPIO14/G14_SPI2_MOSI`；`sclk=GPIO15/G15_SPI2_CLK`；`cs=GPIO16/G16_EINK_CS`；`dc=GPIO17/G17_EINK_DC`；`busy=GPIO18/G18_EINK_BUSY`；`reset=PYB_EINK_RST`
- 证据：图 88b42aecfd86 / 第 1 页 / C5-D6 EINK 分区 J5 引脚 9-14

### ST25R3916 通信模式

ST25R3916-AQWT 的 I2C_EN 通过 R4 0 Ω 接 VCC_3V3，图注明确给出 I2C_EN=VDD 选择 I2C 模式；SCLK/MISO 网络分别接 G48_SYS_SCL/G47_SYS_SDA，IRQ 接 G6_RFID_INT。

- 参数与网络：`reference=U2`；`mode=I2C`；`mode_select=I2C_EN=VCC_3V3 via R4 0R`；`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`irq=G6_RFID_INT`
- 证据：图 41848ade172b / 第 1 页 / B1-B2 U2 左侧 I2C_EN、SCLK/MISO 与 Communication mode 图注

## 总线地址

### M5PM1 I2C 地址

PMIC 分区明确标注 M5PM1 的 IIC 地址为 0x6E。

- 参数与网络：`reference=U7`；`address_7bit=0x6E`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`
- 证据：图 52af03768faf / 第 1 页 / C4-D4 PMIC 分区底部 IIC Address:0x6E

### RX8130CE I2C 地址

RTC 分区明确标注 RX8130CE 的 IIC 地址为 0x32。

- 参数与网络：`reference=U16`；`address_7bit=0x32`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`
- 证据：图 88b42aecfd86 / 第 1 页 / A1 RTC 分区蓝色 IIC Address:0x32 标注

### BMI270 I2C 地址

IMU 分区明确标注 BMI270 的 IIC 地址为 0x68。

- 参数与网络：`reference=U15`；`address_7bit=0x68`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`
- 证据：图 88b42aecfd86 / 第 1 页 / A2 IMU 分区蓝色 IIC Address:0x68 标注

### M5IOE1 I2C 地址

PYB_IIC 分区明确标注 M5IOE1 的 IIC 地址为 0x4F。

- 参数与网络：`reference=U17`；`address_7bit=0x4F`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`；`irq=G7_PYB_IRQ`
- 证据：图 88b42aecfd86 / 第 1 页 / B1-B2 PYB_IIC 分区蓝色 IIC Address:0x4F 标注

## GPIO 与控制信号

### BOOT 控制网络

U12 GPIO0[strap] 连接 G0_BOOT_OUT，R33 10 kΩ 将该网络上拉到 3V3_L2；同一网络连接 M5PM1 的 BOOT_OUT_OD。

- 参数与网络：`soc_pin=GPIO0[strap]`；`net=G0_BOOT_OUT`；`pullup=R33 10K/1%`；`pmic_pin=BOOT_OUT_OD`
- 证据：图 f547ea1ebc45 / 第 1 页 / B1-B2 G0_BOOT_OUT 与 U12 GPIO0; 图 52af03768faf / 第 1 页 / D4 U7 BOOT_OUT_OD 引脚

### LoRa 控制与状态信号

LoRa 模组的 SX_NRST、SX_BUSY、LORA_IRQ、SX_ANT_SW 分别连接 PYB_LoRa_RST、G21_LoRa_BUSY、G5_LoRa_INT、PYB_LoRa_ANT_SW，并由 3V3_L2_LoRa 供电。

- 参数与网络：`reset=PYB_LoRa_RST`；`busy=G21_LoRa_BUSY`；`irq=G5_LoRa_INT`；`antenna_switch=PYB_LoRa_ANT_SW`；`power=3V3_L2_LoRa`
- 证据：图 88b42aecfd86 / 第 1 页 / A5-A6 LoRa 分区 U14 左侧与电源引脚

### M5IOE1 外设控制映射

M5IOE1 将 PYG14/PYG1 用作 PYB_TF_EN/PYB_TF_DET，PYG10/PYG2 用作 LoRa 复位与天线开关，PYG6/PYG13 用作触控复位与电源使能，PYG5/PYG3 用作电子纸复位与电源使能。

- 参数与网络：`microSD=PYG14=PYB_TF_EN, PYG1=PYB_TF_DET`；`lora=PYG10=PYB_LoRa_RST, PYG2=PYB_LoRa_ANT_SW`；`touch=PYG6=PYB_TP_RST, PYG13=PYB_TP_EN`；`eink=PYG5=PYB_EINK_RST, PYG3=PYB_EPD_EN`
- 证据：图 88b42aecfd86 / 第 1 页 / B1-B2 PYB_IIC 分区 U17 两侧网络

### microSD 插卡检测

U20 的卡座开关 SW 接 PYB_TF_DET，图注明确说明该 M5IOE1 引脚使用内部上拉、通过检测对地连接识别插卡并唤醒 ESP32。

- 参数与网络：`detect_net=PYB_TF_DET`；`io_expander_pin=M5IOE1 PYG1`；`active_condition=ground connection`；`series_resistor=R68 1M/1%`
- 证据：图 88b42aecfd86 / 第 1 页 / D2-D3 TF 分区 U20 SW 引脚与底部英文图注

### 实体按键网络

S1、S2、S3 按下时分别将 PWR_BTN、G2_KEY1、G3_KEY2 接地；三个网络分别由 10 kΩ 电阻上拉并并联 100 nF 电容与 ESD5311。

- 参数与网络：`power_key=S1/PWR_BTN/R1/DR1/C1`；`user_key_1=S2/G2_KEY1/R2/DR2/C3`；`user_key_2=S3/G3_KEY2/R5/DR3/C4`；`pullups=10K/1%`；`capacitors=100nF/10V`
- 证据：图 920bd393c299 / 第 1 页 / A1-B1 KEY 分区

### RGB 指示灯控制

LED1 RS-C1415MBAR 的蓝、绿、红通道分别由 PYB_LED_B、PYB_LED_G、PY_LED_R 驱动，并分别串联 R6 560 Ω、R7 820 Ω、R8 1 kΩ，公共端接地。

- 参数与网络：`blue=PYB_LED_B via R6 560R`；`green=PYB_LED_G via R7 820R`；`red=PY_LED_R via R8 1K`；`common=GND`
- 证据：图 920bd393c299 / 第 1 页 / C1 RGB 分区 LED1 与 R6-R8

## 时钟

### ESP32-S3 主时钟

X1 跨接 XTAL_P 与 XTAL_N，XTAL_P 侧串联 L7 24 nH，C45 与 C50 均为 24 pF 对地负载电容。

- 参数与网络：`reference=X1`；`nets=XTAL_P, XTAL_N`；`series_inductor=L7 24nH`；`load_capacitors=C45=24pF, C50=24pF`
- 证据：图 f547ea1ebc45 / 第 1 页 / A4-B4 U12 右侧晶振网络

### NFC 时钟

ST25R3916-AQWT 的 XTO/XTI 接 X1 27.12 MHz 晶振，C14 与 C15 各为 10 pF 对地负载电容。

- 参数与网络：`reference=X1`；`frequency=27.12MHz`；`controller_pins=U2 XTO/XTI`；`load_capacitors=C14=10pF, C15=10pF`
- 证据：图 41848ade172b / 第 1 页 / C1-C2 U2 XTO/XTI 与 X1

## 复位

### ESP32-S3 复位网络

SOC_RESET 通过 R32 0 Ω 接到由 R31 10 kΩ 上拉至 3V3_L2、C53 1 µF 下拉至 GND 的 RC 节点，并连接 U12 CHIP_PU。

- 参数与网络：`net=SOC_RESET`；`soc_pin=U12 CHIP_PU`；`pullup=R31 10K/1%`；`series=R32 0R/1%`；`capacitor=C53 1uF/25V`
- 证据：图 f547ea1ebc45 / 第 1 页 / B1 RC_RESET 与 B2 U12 CHIP_PU

## 保护电路

### USB 数据线保护

USB_N 和 USB_P 各由一颗 ESD5311 对地保护，器件位号为 TVS1 和 TVS2。

- 参数与网络：`devices=TVS1, TVS2`；`part_number=ESD5311`；`protected_nets=USB_N, USB_P`
- 证据：图 52af03768faf / 第 1 页 / A1 TYPEC 分区右侧 TVS1/TVS2

### microSD 信号保护

DAT2、DAT3、CMD、CLK、DAT0、DAT1 和 PYB_TF_DET 各经串联电阻后接 ESD5311 对地保护器件 TVS3-TVS9。

- 参数与网络：`protected_nets=G9_TF_DATA2, G8_TF_DATA3, G12_TF_CMD, G13_TF_CLK, G11_TF_DATA0, G10_TF_DATA1, PYB_TF_DET`；`series_resistors=R62-R67 4.7K, R68 1M`；`protectors=TVS3-TVS9 ESD5311`
- 证据：图 88b42aecfd86 / 第 1 页 / D2 TF 分区 R62-R68 与 TVS3-TVS9

## 存储

### 外部 NOR Flash 连接

U13 XM25UH128DHIQT 接 ESP32-S3 专用 SPI Flash 网络 NOR_CS、NOR_DO、NOR_SCK、NOR_DI、NOR_HOLD、NOR_WP，电源网络为 VDD_NOR。

- 参数与网络：`reference=U13`；`part_number=XM25UH128DHIQT`；`signals=NOR_CS, NOR_DO, NOR_SCK, NOR_DI, NOR_HOLD, NOR_WP`；`power=VDD_NOR`
- 证据：图 f547ea1ebc45 / 第 1 页 / C4 MCU_Core 右侧 U13

### microSD 4 位总线

microSD 卡座 U20 以 G8_TF_DATA3、G9_TF_DATA2、G10_TF_DATA1、G11_TF_DATA0、G12_TF_CMD、G13_TF_CLK 连接 ESP32-S3，并由 TF_3V3_L3 供电。

- 参数与网络：`data3=GPIO8/G8_TF_DATA3`；`data2=GPIO9/G9_TF_DATA2`；`data1=GPIO10/G10_TF_DATA1`；`data0=GPIO11/G11_TF_DATA0`；`cmd=GPIO12/G12_TF_CMD`；`clk=GPIO13/G13_TF_CLK`；`power=TF_3V3_L3`
- 证据：图 88b42aecfd86 / 第 1 页 / D2-D3 TF 分区 U20; 图 f547ea1ebc45 / 第 1 页 / B2-C2 U12 GPIO8-GPIO13 网络

## 音频

### 蜂鸣器驱动

G42_BB_PWM 经 R50 驱动 Q3 SK2302AAT 低边开关，蜂鸣器另一端接 3V3_L2，并由 D3 1N4148WS 跨接钳位。

- 参数与网络：`control=G42_BB_PWM`；`transistor=Q3 SK2302AAT`；`diode=D3 1N4148WS`；`supply=3V3_L2`
- 证据：图 88b42aecfd86 / 第 1 页 / A3 BUZZER 分区

### PDM 麦克风

U1 LMD4737T261-AC02 由 PDM_VDD 供电，DAT 经 R3 22 Ω 连接 G46_PDM_DAT，CLK 经 R4 22 Ω 连接 G45_PDM_CLK，SELECT 接地。

- 参数与网络：`reference=U1`；`part_number=LMD4737T261-AC02`；`data=G46_PDM_DAT`；`clock=G45_PDM_CLK`；`power=PDM_VDD`；`select=GND`
- 证据：图 920bd393c299 / 第 1 页 / A2-B3 PDM 分区

## 传感器

### RTC 连接与中断

RX8130CE 的 SCL/SDA 接系统 I2C，nIRQ 经 R47 22 Ω 输出 PYG0_RTC_INT，该网络由 R49 100 kΩ 上拉到 3V3_L0。

- 参数与网络：`reference=U16`；`interrupt=PYG0_RTC_INT`；`series_resistor=R47 22R/1%`；`pullup=R49 100K/1%`；`power=3V3_L0`
- 证据：图 88b42aecfd86 / 第 1 页 / A1 RTC 分区 U16、R47、R49

### IMU 连接与中断

BMI270 的 SCx/SDx 接 G48_SYS_SCL/G47_SYS_SDA，INT1 经 R44 22 Ω 输出 PYG4_IMU_INT，器件由 3V3_L1 供电。

- 参数与网络：`reference=U15`；`interrupt=PYG4_IMU_INT`；`series_resistor=R44 22R/1%`；`power=3V3_L1`
- 证据：图 88b42aecfd86 / 第 1 页 / A2 IMU 分区 U15 与 R44

## 射频

### ESP32-S3 天线匹配

U12 LNA_IN 以 50 Ω 走线连接 ANT1 ANT_PIFA，路径包含 L5 0 Ω、L4 LQP03TN2N6B02D 及 C39-C42 匹配焊位，其中 C39/C40 标为 NC(TBD)。

- 参数与网络：`soc_pin=LNA_IN`；`antenna=ANT1 ANT_PIFA`；`impedance_label=50ohm`；`series_parts=L5 0R, L4 LQP03TN2N6B02D`；`unpopulated_labels=C39/C40 NC(TBD)`
- 证据：图 f547ea1ebc45 / 第 1 页 / A1-A2 MCU_Core 顶部 ANT1 到 U12 LNA_IN

### NFC 差分匹配网络

ST25R3916 的 RFO1/RFO2 经 L1/L2 270 nH 和 C2-C13 匹配网络形成 ANT1_P/ANT1_N，再经 R3/R5 2 Ω 驱动 ANT_NFC 线圈。

- 参数与网络：`transmitter_outputs=RFO1, RFO2`；`series_inductors=L1/L2 270nH 5%`；`matching_capacitors=C2-C13`；`series_resistors=R3/R5 2R`；`antenna_nodes=ANT1_P, ANT1_N`；`antenna=ANT_NFC`
- 证据：图 41848ade172b / 第 1 页 / B2-B4 U2 RFO1/RFO2 到 ANT1 的匹配网络

### NFC PCB 天线几何参数

NFC Antenna Layout Note 标注线圈 4 匝、长宽各 25 mm、线宽 0.25 mm、线距 0.3 mm、铜厚 17 µm；页面计算截图给出 13.56 MHz 时等效电感 956.94 nH。

- 参数与网络：`turns=4`；`length_mm=25`；`width_mm=25`；`trace_width_mm=0.25`；`spacing_mm=0.3`；`copper_thickness_um=17`；`equivalent_inductance=956.94nH @13.56MHz`
- 证据：图 41848ade172b / 第 1 页 / A3-A4 Geometry/Antenna Results 截图与 B4 NFC Antance Layout Note

## 调试与烧录

### 调试测试点

调试区提供 3V3_L0、VBUS_L0、3V3_L2_LoRa、3V3_L1、3V3_L2、GND、UART0 TX/RX、SOC_RESET、G0_BOOT_OUT、BAT_ADC_EN 与 PY_LED_R 测试点。

- 参数与网络：`power=TP1=3V3_L0, TP6=VBUS_L0, TP2=3V3_L2_LoRa, TP7=3V3_L1, TP3=3V3_L2, TP8=GND`；`signals=TP4=G43_U0_TX, TP9=G44_U0_RX, TP5=SOC_RESET, TP10=G0_BOOT_OUT, TP11=BAT_ADC_EN, TP12=PY_LED_R`
- 证据：图 f547ea1ebc45 / 第 1 页 / D2-D3 DEBUG 分区 TP1-TP12

## 模拟电路

### 前光电流设定

EINK_BL 图注给出 Iset 最大值不超过 20 mA，并以 Duty=100%、Vfb=200 mV、Iset=15 mA 推得 Rset=11 Ω。

- 参数与网络：`iset_max=20mA`；`example_iset=15mA`；`example_rset=11R`；`feedback_resistor=R29 18R/1%`
- 证据：图 52af03768faf / 第 1 页 / D2 EINK_BL 下方红色 Iset/Rset 图注

### 电池电压采样

BAT_ADC_EN 控制 Q1A/Q1B CJ3439KDW 门控电路，将 VBAT_L0 经 R3、R5、R12 与 C7 网络送到 BAT_ADC。

- 参数与网络：`enable=BAT_ADC_EN`；`output=BAT_ADC`；`switch=Q1A/Q1B CJ3439KDW`；`resistors=R3 1M, R5 1K, R12 1K`
- 证据：图 52af03768faf / 第 1 页 / A4 ADC_DET 上半部

### 5 V 输入检测

5V_IN 通过 R19/R21 两个 10 kΩ 电阻分压形成 5VIN_ADC，并由 C12 100 nF 对地滤波。

- 参数与网络：`input=5V_IN`；`output=5VIN_ADC`；`divider=R19=10K, R21=10K`；`filter=C12 100nF/25V`
- 证据：图 52af03768faf / 第 1 页 / B4 ADC_DET 下半部

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统功能分区 | `soc=ESP32-S3-R8`；`pmic=M5PM1`；`io_expander=M5IOE1` |
| 系统结构 | 电源状态层级 | `L0=Shipping`；`L1=Standby`；`L2=DeepSleep`；`L3A=CORE ACTIVE`；`L3B=All ACTIVE` |
| 系统结构 | L2 到活动态唤醒源 | `gpio_wake=G2_KEY1, G3_KEY2, G4_TP_INT, G5_LoRa_INT, G6_RFID_INT`；`pmic_irq=G1_PY_IRQ` |
| 接口 | USB Type-C 接口 | `connector=TYPEC-302-BRP16SC08`；`power_net=VUSB_IN`；`data_n=USB_N`；`data_p=USB_P`；`cc_resistors=R4/R14 5.1K/1%` |
| 保护电路 | USB 数据线保护 | `devices=TVS1, TVS2`；`part_number=ESD5311`；`protected_nets=USB_N, USB_P` |
| 电源 | 5 V 输入保护 | `reference=U2`；`input=VUSB_IN`；`output=5V_IN`；`ovp=5.95V` |
| 电源 | 电池充电路径 | `reference=U1`；`part_number=IP2315`；`input=5V_IN`；`battery_net=VBAT_L0`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`ipeak=1.5A` |
| 接口 | 电池连接器 | `reference=J2`；`pin_2=VBAT_L0`；`pin_1=GND`；`capacitor=C13 22uF/10V` |
| 电源 | VBAT_L0 与 VBUS_L0 | `link=R20 0R/1%`；`upstream=VBAT_L0`；`downstream=VBUS_L0` |
| 电源 | 3V3_L0 常开电源轨 | `reference=U4`；`input=VBUS_L0`；`enable=VBUS_L0`；`output=3V3_L0` |
| 电源 | 3V3_L1 电源轨 | `reference=U6`；`input=VBUS_L0`；`enable=3V3_L1_EN`；`output=3V3_L1` |
| 电源 | LoRa 分域电源 | `reference=U9`；`input=VBUS_L0`；`enable=PYG2_LoRa_EN`；`output=3V3_L2_LoRa` |
| 电源 | 3V3_L2 核心活动电源轨 | `reference=U10`；`input=VBUS_L0`；`enable=3V3_L2_EN`；`output=3V3_L2`；`rated_current_label=600mA` |
| 电源 | 电子纸 3.3 V 分域 | `reference=U5`；`input=VBUS_L0`；`enable=PYB_EPD_EN`；`output=EPD_3V3_L3` |
| 电源 | microSD 电源分域 | `reference=U8`；`input=3V3_L2`；`enable=PYB_TF_EN`；`output=TF_3V3_L3` |
| 电源 | 触控接口电源分域 | `reference=U18`；`input=3V3_L2`；`enable=PYB_TP_EN`；`output=TP_VDD` |
| 电源 | PDM 麦克风电源分域 | `reference=U21`；`input=3V3_L2`；`enable=PYB_PDM_EN`；`output=PDM_VDD` |
| 电源 | 电子纸前光电源 | `reference=U11`；`input=EPD_3V3_L3`；`control=PYG3_BL_PWM`；`output=BL_15V_L3B`；`feedback=BL_FB` |
| 模拟电路 | 前光电流设定 | `iset_max=20mA`；`example_iset=15mA`；`example_rset=11R`；`feedback_resistor=R29 18R/1%` |
| 模拟电路 | 电池电压采样 | `enable=BAT_ADC_EN`；`output=BAT_ADC`；`switch=Q1A/Q1B CJ3439KDW`；`resistors=R3 1M, R5 1K, R12 1K` |
| 模拟电路 | 5 V 输入检测 | `input=5V_IN`；`output=5VIN_ADC`；`divider=R19=10K, R21=10K`；`filter=C12 100nF/25V` |
| 总线地址 | M5PM1 I2C 地址 | `reference=U7`；`address_7bit=0x6E`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL` |
| 总线 | 系统 I2C 总线 | `sda=GPIO47/G47_SYS_SDA`；`scl=GPIO48/G48_SYS_SCL`；`pullups=R36/R37 2.2K/1%`；`pullup_rail=3V3_L2` |
| 总线 | 充电器 I2C 接入控制 | `translator=U3 AW39112DNR`；`controller_side=G48_SYS_SCL, G47_SYS_SDA`；`charger_side=CHG_SYS_SCL, CHG_SYS_SDA`；`enable=PYB_CHG_IIC`；`enable_pulldown=R22 100K/1%` |
| 复位 | ESP32-S3 复位网络 | `net=SOC_RESET`；`soc_pin=U12 CHIP_PU`；`pullup=R31 10K/1%`；`series=R32 0R/1%`；`capacitor=C53 1uF/25V` |
| GPIO 与控制信号 | BOOT 控制网络 | `soc_pin=GPIO0[strap]`；`net=G0_BOOT_OUT`；`pullup=R33 10K/1%`；`pmic_pin=BOOT_OUT_OD` |
| 时钟 | ESP32-S3 主时钟 | `reference=X1`；`nets=XTAL_P, XTAL_N`；`series_inductor=L7 24nH`；`load_capacitors=C45=24pF, C50=24pF` |
| 射频 | ESP32-S3 天线匹配 | `soc_pin=LNA_IN`；`antenna=ANT1 ANT_PIFA`；`impedance_label=50ohm`；`series_parts=L5 0R, L4 LQP03TN2N6B02D`；`unpopulated_labels=C39/C40 NC(TBD)` |
| 存储 | 外部 NOR Flash 连接 | `reference=U13`；`part_number=XM25UH128DHIQT`；`signals=NOR_CS, NOR_DO, NOR_SCK, NOR_DI, NOR_HOLD, NOR_WP`；`power=VDD_NOR` |
| 接口 | ESP32-S3 原生 USB 数据链 | `usb_n=USB_N -> R40 -> FT1 -> G19_USB_N -> GPIO19`；`usb_p=USB_P -> R41 -> FT1 -> G20_USB_P -> GPIO20`；`series_resistors=R40/R41 22R/1%`；`filter=FT1 ICMF062P900MFR` |
| 调试与烧录 | 调试测试点 | `power=TP1=3V3_L0, TP6=VBUS_L0, TP2=3V3_L2_LoRa, TP7=3V3_L1, TP3=3V3_L2, TP8=GND`；`signals=TP4=G43_U0_TX, TP9=G44_U0_RX, TP5=SOC_RESET, TP10=G0_BOOT_OUT, TP11=BAT_ADC_EN, TP12=PY_LED_R` |
| 总线地址 | RX8130CE I2C 地址 | `reference=U16`；`address_7bit=0x32`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL` |
| 传感器 | RTC 连接与中断 | `reference=U16`；`interrupt=PYG0_RTC_INT`；`series_resistor=R47 22R/1%`；`pullup=R49 100K/1%`；`power=3V3_L0` |
| 总线地址 | BMI270 I2C 地址 | `reference=U15`；`address_7bit=0x68`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL` |
| 传感器 | IMU 连接与中断 | `reference=U15`；`interrupt=PYG4_IMU_INT`；`series_resistor=R44 22R/1%`；`power=3V3_L1` |
| 音频 | 蜂鸣器驱动 | `control=G42_BB_PWM`；`transistor=Q3 SK2302AAT`；`diode=D3 1N4148WS`；`supply=3V3_L2` |
| 总线 | LoRa SPI 总线 | `module=U14 Stamp-LoRa-1262-mini`；`mosi=G38_SPI1_MOSI`；`miso=G40_SPI1_MISO`；`sclk=G39_SPI1_CLK`；`cs=G41_LoRa_NSS` |
| GPIO 与控制信号 | LoRa 控制与状态信号 | `reset=PYB_LoRa_RST`；`busy=G21_LoRa_BUSY`；`irq=G5_LoRa_INT`；`antenna_switch=PYB_LoRa_ANT_SW`；`power=3V3_L2_LoRa` |
| 总线地址 | M5IOE1 I2C 地址 | `reference=U17`；`address_7bit=0x4F`；`sda=G47_SYS_SDA`；`scl=G48_SYS_SCL`；`irq=G7_PYB_IRQ` |
| GPIO 与控制信号 | M5IOE1 外设控制映射 | `microSD=PYG14=PYB_TF_EN, PYG1=PYB_TF_DET`；`lora=PYG10=PYB_LoRa_RST, PYG2=PYB_LoRa_ANT_SW`；`touch=PYG6=PYB_TP_RST, PYG13=PYB_TP_EN`；`eink=PYG5=PYB_EINK_RST, PYG3=PYB_EPD_EN` |
| 总线 | 触控 I2C 接口 | `translator=U19 AW39112DNR`；`controller_side=G48_SYS_SCL, G47_SYS_SDA`；`panel_side=TP_SYS_SCL, TP_SYS_SDA`；`interrupt=G4_TP_INT`；`reset=PYB_TP_RST`；`power=TP_VDD` |
| 存储 | microSD 4 位总线 | `data3=GPIO8/G8_TF_DATA3`；`data2=GPIO9/G9_TF_DATA2`；`data1=GPIO10/G10_TF_DATA1`；`data0=GPIO11/G11_TF_DATA0`；`cmd=GPIO12/G12_TF_CMD`；`clk=GPIO13/G13_TF_CLK`；`power=TF_3V3_L3` |
| GPIO 与控制信号 | microSD 插卡检测 | `detect_net=PYB_TF_DET`；`io_expander_pin=M5IOE1 PYG1`；`active_condition=ground connection`；`series_resistor=R68 1M/1%` |
| 保护电路 | microSD 信号保护 | `protected_nets=G9_TF_DATA2, G8_TF_DATA3, G12_TF_CMD, G13_TF_CLK, G11_TF_DATA0, G10_TF_DATA1, PYB_TF_DET`；`series_resistors=R62-R67 4.7K, R68 1M`；`protectors=TVS3-TVS9 ESD5311` |
| 总线 | 电子纸 SPI 接口 | `mosi=GPIO14/G14_SPI2_MOSI`；`sclk=GPIO15/G15_SPI2_CLK`；`cs=GPIO16/G16_EINK_CS`；`dc=GPIO17/G17_EINK_DC`；`busy=GPIO18/G18_EINK_BUSY`；`reset=PYB_EINK_RST` |
| 电源 | 电子纸高压偏置网络 | `input=EPD_3V3_L3`；`inductor=L8 SPH252010H330MT`；`transistor=Q4 CJ2310`；`diodes=D4-D6 1N5819WS`；`outputs=PREVGH, PREVGL, GDR, RESE` |
| GPIO 与控制信号 | 实体按键网络 | `power_key=S1/PWR_BTN/R1/DR1/C1`；`user_key_1=S2/G2_KEY1/R2/DR2/C3`；`user_key_2=S3/G3_KEY2/R5/DR3/C4`；`pullups=10K/1%`；`capacitors=100nF/10V` |
| 音频 | PDM 麦克风 | `reference=U1`；`part_number=LMD4737T261-AC02`；`data=G46_PDM_DAT`；`clock=G45_PDM_CLK`；`power=PDM_VDD`；`select=GND` |
| GPIO 与控制信号 | RGB 指示灯控制 | `blue=PYB_LED_B via R6 560R`；`green=PYB_LED_G via R7 820R`；`red=PY_LED_R via R8 1K`；`common=GND` |
| 接口 | NFC 子板连接 | `connector=J1 BTB0.408-10PLBDR-G41`；`pin_1=3V3_L2`；`pin_3=G48_SYS_SCL`；`pin_5=G47_SYS_SDA`；`pin_7=G6_RFID_INT`；`pin_9=PYB_RFID_RST`；`ground_pins=2,4,6,8,10,11-14` |
| 电源 | NFC 子板受控电源 | `reference=U1`；`input=3V3_L2`；`output=VCC_3V3`；`enable=PYB_RFID_RST`；`bypass=R1 0R`；`optional_resistor=R2 NC` |
| 总线 | ST25R3916 通信模式 | `reference=U2`；`mode=I2C`；`mode_select=I2C_EN=VCC_3V3 via R4 0R`；`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`irq=G6_RFID_INT` |
| 时钟 | NFC 时钟 | `reference=X1`；`frequency=27.12MHz`；`controller_pins=U2 XTO/XTI`；`load_capacitors=C14=10pF, C15=10pF` |
| 射频 | NFC 差分匹配网络 | `transmitter_outputs=RFO1, RFO2`；`series_inductors=L1/L2 270nH 5%`；`matching_capacitors=C2-C13`；`series_resistors=R3/R5 2R`；`antenna_nodes=ANT1_P, ANT1_N`；`antenna=ANT_NFC` |
| 射频 | NFC PCB 天线几何参数 | `turns=4`；`length_mm=25`；`width_mm=25`；`trace_width_mm=0.25`；`spacing_mm=0.3`；`copper_thickness_um=17`；`equivalent_inductance=956.94nH @13.56MHz` |
| 电源 | NFC 掉电电流图注 | `mode=Power-down`；`condition=operation control register en=0`；`supply_current=2.5uA` |
| 总线地址 | IP2315 I2C 地址 | `source_document_claim=0x75`；`schematic_address_label=null`；`bus=CHG_SYS_SCL, CHG_SYS_SDA` |
| 核心器件 | 触控控制器型号与地址 | `source_document_model=FT6336G`；`source_document_address=0x38`；`schematic_visible_interface=J4 TP_SYS_SCL/TP_SYS_SDA/G4_TP_INT/PYB_TP_RST` |
| 核心器件 | 电子纸驱动器与面板参数 | `source_document_driver=SSD1677`；`source_document_resolution=480x800`；`source_document_grayscale=4-level`；`schematic_visible_interface=J5 FPC0.5-SMT-24P-B` |
| 存储 | 外部 Flash 容量 | `source_document_capacity=16MB`；`schematic_part_number=XM25UH128DHIQT`；`schematic_capacity_label=null` |
| 内存与 Flash | PSRAM 容量 | `source_document_capacity=8MB`；`schematic_soc_label=ESP32_S3R8`；`external_psram_symbol=null` |
| 电源 | 电池容量 | `source_document_capacity=1150mAh`；`schematic_capacity_label=null`；`battery_net=VBAT_L0` |
| 射频 | LoRa 工作频段 | `source_document_frequency_range=868MHz-923MHz`；`schematic_module_label=Stamp-LoRa-1262-mini`；`schematic_frequency_label=null` |
| 总线地址 | ST25R3916 I2C 地址 | `source_document_claim=0x50`；`schematic_address_label=null`；`controller=ST25R3916-AQWT` |
| 关键网络 | EINK 与 TF 的 L3 电源网命名 | `overview_names=EPD_3V3_L3B, TF_3V3_L3B`；`detail_names=EPD_3V3_L3, TF_3V3_L3`；`alias_confirmed=false` |

## 待确认事项

- `address.ip2315`：源文档将 IP2315 地址写为 0x75，但原理图只画出 CHG_SYS_SCL/CHG_SYS_SDA 及其门控电路，未在图面标注数值地址。（证据：图 52af03768faf / 第 1 页 / A3-B3 CHARG 分区，IP2315 与 CHG I2C 网络可见但无地址标注）
- `component.touch-controller`：源文档声称触控控制器为 FT6336G、地址 0x38；原理图 TP 分区仅展示电平转换、受控电源和 J4 面板连接器，未展示触控 IC 本体或地址。（证据：图 88b42aecfd86 / 第 1 页 / B3-B4 TP 分区仅有 U18/U19/J4，无触控控制器符号和地址标注）
- `component.eink-panel`：源文档声称面板使用 SSD1677、分辨率 480x800、4 阶灰度；原理图 EINK 分区仅展示 J5、SPI/控制网络和偏置电源，未展示 SSD1677 器件符号或面板参数。（证据：图 88b42aecfd86 / 第 1 页 / B5-D6 EINK 分区仅显示面板接口与高压偏置网络）
- `storage.flash-capacity`：源文档声称外部 Flash 容量为 16 MB；原理图标出 U13 料号 XM25UH128DHIQT，但未以容量字段直接标注 16 MB。（证据：图 f547ea1ebc45 / 第 1 页 / C4 U13 外部 NOR Flash，仅标料号与 NOR_* 网络）
- `memory.psram-capacity`：源文档声称 PSRAM 容量为 8 MB；原理图仅标出 ESP32_S3R8 器件名，未独立标注 PSRAM 容量或外部 PSRAM 器件。（证据：图 f547ea1ebc45 / 第 1 页 / B2-C3 U12 ESP32_S3R8；整页未见独立 PSRAM 容量标注）
- `power.battery-capacity`：源文档声称内置电池容量为 1150 mAh；原理图只展示 J2 电池接口、VBAT_L0 和充电/检测路径，未标注容量。（证据：图 52af03768faf / 第 1 页 / B2 Battery 分区 J2 与 VBAT_L0，无容量标注）
- `rf.lora-frequency`：源文档声称 LoRa 支持 868 MHz 至 923 MHz；原理图只标出 Stamp-LoRa-1262-mini 模组和 SPI/控制网络，未标注工作频段。（证据：图 88b42aecfd86 / 第 1 页 / A5-A6 LoRa 分区 U14，无频率标注）
- `address.nfc`：源文档将 ST25R3916 地址写为 0x50；NFC 子页确认 I2C 模式和总线连接，但未在图面标注数值地址。（证据：图 41848ade172b / 第 1 页 / B1-C2 U2 与 Communication mode 图注，仅确认 I2C 模式而无地址）
- `key-net.l3-rail-names`：第 1 页电源总览使用 EPD_3V3_L3B 和 TF_3V3_L3B，而第 2 页及第 4 页器件级电路使用 EPD_3V3_L3 和 TF_3V3_L3；现有图页未明确声明这两组名称互为别名。（证据：图 d60bc2217ff3 / 第 1 页 / A7-B8 Power Network 总览，EINK/TF 分支使用 EPD_3V3_L3B、TF_3V3_L3B; 图 52af03768faf / 第 1 页 / C2-C3 L3_SW 明细，U5/U8 输出使用 EPD_3V3_L3、TF_3V3_L3; 图 88b42aecfd86 / 第 1 页 / D2-D6 TF/EINK 明细使用 TF_3V3_L3、EPD_3V3_L3）
- `review.ip2315-address`：IP2315 在该硬件配置下的 7 位 I2C 地址是否确为 0x75？；原因：数值地址仅见于源文档，当前原理图页未直接标注。
- `review.touch-controller`：J4 所接触控面板是否固定使用 FT6336G，且 7 位 I2C 地址是否为 0x38？；原因：原理图只展示接口、电平转换和供电控制，没有触控 IC 本体与地址。
- `review.eink-panel`：J5 所接电子纸面板的驱动器、分辨率和灰阶是否分别为 SSD1677、480x800 和 4 阶灰度？；原因：原理图只展示 FPC 信号与偏置电源，面板内部驱动器和显示参数不可见。
- `review.flash-capacity`：U13 对应的装配容量是否为源文档所述 16 MB？；原因：原理图标出器件料号但没有单独的容量字段；不从型号命名换算容量。
- `review.psram-capacity`：ESP32_S3R8 对应的实际 PSRAM 容量是否为源文档所述 8 MB？；原因：图面未将型号后缀解释为容量，也未展示独立 PSRAM 器件或容量标注。
- `review.battery-capacity`：实际装配电池容量是否为源文档所述 1150 mAh？；原因：原理图未标注电芯料号或容量。
- `review.lora-frequency`：当前 U14 模组的实际射频覆盖范围是否为 868 MHz 至 923 MHz？；原因：原理图未给出频段、射频前端或天线规格，只给出模组名称与数字接口。
- `review.nfc-address`：ST25R3916-AQWT 在 I2C 模式下的 7 位地址是否为源文档所述 0x50？；原因：NFC 子页确认 I2C_EN 接 VCC_3V3，但未给出数值地址。
- `review.l3-rail-names`：EPD_3V3_L3B/TF_3V3_L3B 是否分别与 EPD_3V3_L3/TF_3V3_L3 为同一网络的层次化别名？；原因：系统总览与器件级明细使用不同网络名，当前图页没有别名表或网表用于证明等价关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d60bc2217ff36b152ed179c527b5aabd3a8484cc2a74b68069d39dcb68005037` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_01.png` |
| 2 | 1 | `52af03768fafce8555187def932925b674513bc266a2c5be839f1a82d787f240` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_02.png` |
| 3 | 1 | `f547ea1ebc4507cebe53cfcfc940f6d37138931dab077b2f20d658aa8d666231` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_03.png` |
| 4 | 1 | `88b42aecfd86fecc6580f11ea29fb876322ff1aa451c6e4d5b62c53dc8e14e73` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_04.png` |
| 5 | 1 | `920bd393c29979622128e6900db23dd6ea1c6bfa8d86f34a2badc3e44411349d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_05.png` |
| 6 | 1 | `41848ade172b00ccafceb123b1b9b7a585fb65fcfd87cd7ac0d4a215cc9c0714` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/PaperMono_SCH_V0.6.2_20260522_page_06.png` |

---

源文档：`zh_CN/core/PaperMono.md`

源文档 SHA-256：`a0486bb3b3511e4fbce79a0b6e66b7d428086909edf54ae217f3930bfbaa51e1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
