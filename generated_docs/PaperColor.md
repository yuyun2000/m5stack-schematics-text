# PaperColor 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PaperColor |
| SKU | C151 |
| 产品 ID | `papercolor-a872f67ef4c9` |
| 源文档 | `zh_CN/core/PaperColor.md` |

## 概述

PaperColor C151 的三页 V0.5 原理图以 ESP32-S3R8 为主控，外接 W25Q128JVPIQ NOR Flash，并由 M5PM1/PY32 PMIC 管理常开、待机、深睡眠、核心活动和全功能活动电源域；系统包含 USB-C 充电与数据、1250mAh 电池、E Ink SPI/FPC、高压驱动、ES8311 与 ES7210 音频链路、AW8737A 扬声器功放、RX8130CE RTC、SHT40、microSD、双向供电 Grove、三按键、红外和双 RGB LED。

## 检索关键词

`PaperColor`、`C151`、`ESP32-S3R8`、`M5PM1`、`PY32L020F15U6`、`W25Q128JVPIQ`、`E Ink`、`EINK`、`EPD_3V3_L3B`、`ES8311`、`ES7210`、`AW8737A`、`RX8130CE`、`SHT40`、`microSD`、`TYPEC-302-BRP16SC08`、`AW32901FCR`、`IP2315`、`IP2316`、`JW5712`、`SGM6603-5.0`、`MT9700`、`WS2812B-4020`、`SYS_VBUS`、`SYS_SCL`、`SYS_SDA`、`PY_EPD_EN`、`PY_SD_PWR_EN`、`PY_GROVE_OUT_EN`、`AUDIO_PWR_EN`、`GROVE_5V`、`SPI_CLK`、`SPI_MOSI`、`SPI_MISO`、`I2S_MCLK`、`I2S_BCLK`、`I2S_LRCK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | ESP32-S3R8 | 主控 SoC，连接外部 Flash、USB、E Ink、音频、microSD、RTC、SHT40、Grove、按键、红外和 RGB | 图 298eb46ddad2 / 第 1 页 / Core MCU 区 C4-D6，U7 ESP32_S3R8 及 GPIO 网络 |
| U9 | W25Q128JVPIQ | ESP32-S3R8 外部 NOR Flash | 图 298eb46ddad2 / 第 1 页 / Core MCU 区 B6，U9 W25Q128JVPIQ 与 NOR_CS/CLK/D0/D1/WP/HOLD |
| U14 | PY32_PMIC / PY32L020F15U6 (M5PM1) | 系统电源管理控制器，管理多级电源域、唤醒、按键、ADC 检测及外围电源使能 | 图 51251532fbba / 第 1 页 / Functions 与 I/Os Map 区 A1-B3、C4-D5，PMIC PY32L020F15U6 信号表; 图 298eb46ddad2 / 第 1 页 / PMIC 区 C1-D2，U14 PY32_PMIC |
| J1 | TYPEC-302-BRP16SC08 | USB Type-C 电源与 USB 2.0 数据接口 | 图 298eb46ddad2 / 第 1 页 / TYPEC 区 A1，J1 TYPEC-302-BRP16SC08 |
| U2,U5 | AW32901FCR | USB 输入和 Grove 端口电源保护器件 | 图 298eb46ddad2 / 第 1 页 / TYPEC 区 A2 的 U2 与 Grove 区 D3 的 U5，均标 AW32901FCR |
| U3 | IP2315 / IP2316 | USB 输入到 VBAT 的开关充电控制器；总览与详图型号标注冲突 | 图 51251532fbba / 第 1 页 / Power Network 区 A3，充电块标注 IP2316 0.5C; 图 298eb46ddad2 / 第 1 页 / CHARG 区 A3，U3 标注 PD Only IP2315 |
| U15 | TPAP7343D-33PS4 | SYS_VBUS 到 3V3_L0 的常开低静态电流 LDO | 图 298eb46ddad2 / 第 1 页 / PMIC 区 B1，U15 TPAP7343D-33PS4，输出 3V3_L0 |
| U6 | JW5712 | 由 PY_MPWR_EN 控制的主 3V3_L2 电源转换器 | 图 298eb46ddad2 / 第 1 页 / PowerPath/CorePower 区 B5-B6，U6 JW5712、L1 与 3V3_L2 |
| U8,U21,U23 | SGM6603-5.0 / MT9700 | 由 PY_GROVE_OUT_EN 控制的 Grove 5V 双向电源路径 | 图 298eb46ddad2 / 第 1 页 / Grove two-way control 区 B3-D4，U8、U21、U23 与 GROVE_5V/SYS_5VIN |
| U18 | SSP7615-33DFR | 由 AUDIO_PWR_EN 控制的 CODEC_3V3_L3B 音频电源 LDO | 图 1095527840e2 / 第 1 页 / Audio 左上 A1，U18 SSP7615-33DFR，SYS_VBUS 到 CODEC_3V3_L3B |
| U1,U24 | MT9700 | E Ink 和 microSD 的受控 3.3V 负载开关 | 图 1095527840e2 / 第 1 页 / EINK 区 A5-A6 的 U1 与 TF 区 D4-D5 的 U24，均标 MT9700 |
| U10 | ES8311 | I2C/I2S 音频编解码器，提供扬声器 DAC 差分信号 | 图 1095527840e2 / 第 1 页 / Audio Codec 区 B1，U10 ES8311 |
| U11 | ES7210 | I2C/I2S 音频 ADC，采集板载麦克风和 AEC 回采信号 | 图 1095527840e2 / 第 1 页 / Audio ADC 区 A2-C3，U11 ES7210 |
| U12 | MSM381A3729H9BPC | VBIAS_MIC 供电的模拟 MEMS 麦克风 | 图 1095527840e2 / 第 1 页 / MIC 区 C3，U12 及 MIC_P/MIC_N |
| U13,J4 | AW8737A / SPK 2-pin | 差分输入扬声器功放及扬声器连接器 | 图 1095527840e2 / 第 1 页 / SPEAK 区 A4-A5，U13 AW8737A、FB1/FB2 与 J4 SPK |
| U17 | RX8130CE | 系统 I2C 实时时钟与低功耗唤醒源 | 图 1095527840e2 / 第 1 页 / RTC 区 D1-D2，U17 RX8130CE |
| U19 | SHT40I-AD1B-R2 | 系统 I2C 温湿度传感器 | 图 1095527840e2 / 第 1 页 / SHT40 区 D1-D2，U19 SHT40I-AD1B-R2 |
| U16,U24 | MicroSD / MT9700 | 带受控电源、卡检测和 ESD 保护的 SPI microSD 接口 | 图 1095527840e2 / 第 1 页 / TF 区 D4-D5，U16 MicroSD、U24 MT9700 与 TVS3-TVS6 |
| J5 | 50-pin E Ink FPC | E Ink 面板数字控制、SPI 和高压电源接口 | 图 1095527840e2 / 第 1 页 / EINK 区 B6-D6，J5 50-pin 接口 |
| LED3,LED4 | WS2812B-4020 | 两颗串接的可寻址 RGB LED | 图 1095527840e2 / 第 1 页 / IR/RGB 区 C4-C5，LED3/LED4 WS2812B-4020 |
| S1,S2,S3 | SW | 三个低有效用户按键 USER_KEY1/2/3 | 图 1095527840e2 / 第 1 页 / KEY 区 B4-B5，S1/S2/S3 |
| J3 | CON4 | Grove/HY2.0-4P 端口，提供 GROVE_5V、GROVE_I、GROVE_O 与 GND | 图 298eb46ddad2 / 第 1 页 / Grove two-way control 区 D3-D4，J3 CON4 |
| J6 | SPI Expansion 12-pin | 扩展 SPI、外部中断、复位、忙信号和受控电源接口 | 图 1095527840e2 / 第 1 页 / SPI Expansion 区 D2-D3，J6 |
| ANT1 | ANT_PIFA | ESP32-S3R8 板载射频天线及匹配网络 | 图 298eb46ddad2 / 第 1 页 / Core MCU 区 C4，ANT1 ANT_PIFA 与 L2/L3/C82/C3 匹配网络 |

## 系统结构

### PaperColor 三页硬件架构

三页原理图以 U7 ESP32-S3R8 为主控，连接 U9 外部 NOR Flash、M5PM1 多级电源控制、USB-C 与电池充电、E Ink 接口与高压电源、ES8311/ES7210/AW8737A 音频链路、RX8130CE、SHT40、microSD、Grove、按键、红外和两颗 RGB LED。

- 参数与网络：`schematic_revision=V0.5`；`schematic_date=2026-04-24`；`page_count=3`
- 证据：图 51251532fbba / 第 1 页 / Functions、Power Network 与 I/Os Map 全页; 图 298eb46ddad2 / 第 1 页 / TYPEC、CHARG、PMIC、PowerPath、Grove 与 Core MCU 全页; 图 1095527840e2 / 第 1 页 / Audio、RTC、SHT40、SPI Expansion、KEY、IR/RGB、TF 与 EINK 全页

### L0/L1/L2/L3A/L3B 电源模式

功能总览定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE 和 L3B All ACTIVE。PMIC 和电池贯穿各模式；ESP32-S3R8 从 L2 起活动；E Ink、SHT40、TF、RGB、CODEC 和 SPEAKER 仅在 L3B 标为活动，用户按键可从低功耗状态唤醒。

- 参数与网络：`shipping=L0`；`standby=L1`；`deep_sleep=L2`；`core_active=L3A`；`all_active=L3B`
- 证据：图 51251532fbba / 第 1 页 / Functions 区 A1-B3 与 Power Mode 区 C1-D3

## 电源

### USB 输入、充电和电池主路径

J1 的 VUSBIN 经 U2 AW32901FCR 保护形成 SYS_5VIN，再进入 U3 开关充电级并输出 VBAT；电池 J2 接 VBAT/GND，R20 0Ω 将 VBAT 接至 SYS_VBUS。总览将充电级标为 0.5C，并把电池容量标为 1250mAh。

- 参数与网络：`battery_capacity_mah=1250`；`charge_label=0.5C`；`main_bus=SYS_VBUS`
- 证据：图 51251532fbba / 第 1 页 / Functions 与 Power Network 区 A1-A4，1250mAh lithium battery、VUSB_IN、SYS_5VIN、VBAT、SYS_VBUS; 图 298eb46ddad2 / 第 1 页 / TYPEC、CHARG 与 PowerPath 区 A1-B6，J1/U2/U3/J2/R20

### 3V3_L0 常开电源域

U15 TPAP7343D-33PS4 从 SYS_VBUS 产生 3V3_L0，EN 直接接 SYS_VBUS；总览标注该 LDO Always On，3V3_L0 供给 M5PM1 常开域和电源按键相关电路。

- 参数与网络：`input=SYS_VBUS`；`output=3V3_L0`；`always_on=true`
- 证据：图 51251532fbba / 第 1 页 / Power Network 区 A4-A5，TPAP7343D LDO Always On 与 3V3_L0; 图 298eb46ddad2 / 第 1 页 / PMIC 区 B1，U15、SYS_VBUS 与 3V3_L0

### 3V3_L2 主电源域

U6 JW5712 以 SYS_VBUS 为输入，EN 由 PY_MPWR_EN 控制，经 L1 2.2uH/1.8A 产生 3V3_L2；该电源域供给 ESP32-S3R8、按键、SHT40、IR，并作为 RGB、microSD 和 E Ink 受控支路的上游。

- 参数与网络：`input=SYS_VBUS`；`output=3V3_L2`；`enable=PY_MPWR_EN`
- 证据：图 51251532fbba / 第 1 页 / Power Network 区 A5-B8，JW5712、PY_MPWR_EN 与 3V3_L2 分支; 图 298eb46ddad2 / 第 1 页 / CorePower 区 B5-B6，U6、L1 与 3V3_L2

### CODEC_3V3_L3B 音频电源

U18 SSP7615-33DFR 从 SYS_VBUS 产生 CODEC_3V3_L3B，EN 由 ESP32-S3R8 的 AUDIO_PWR_EN 控制；该受控电源供给 ES8311、ES7210、麦克风偏置和音频侧 I2C 上拉。

- 参数与网络：`input=SYS_VBUS`；`output=CODEC_3V3_L3B`；`enable=AUDIO_PWR_EN`
- 证据：图 1095527840e2 / 第 1 页 / Audio 区 A1-C3，U18 与 U10/U11/U12 电源网络

### Grove 5V 双向电源控制

输出方向由 U8 SGM6603-5.0 把 SYS_VBUS 升压后经 U21 MT9700 送到 GROVE_5V；反向输入方向由 U23 MT9700 把 GROVE_5V 送到 SYS_5VIN。PY_GROVE_OUT_EN 同时控制 U8/U21，并经 Q3 2N7002T 反相控制 U23，J3 电源线上另有 U5 AW32901FCR 保护。

- 参数与网络：`control=PY_GROVE_OUT_EN`；`port_power=GROVE_5V`；`system_input=SYS_5VIN`
- 证据：图 298eb46ddad2 / 第 1 页 / Grove two-way control 区 B3-D4，U8/U21/U23/Q3/U5/J3

### E Ink、microSD 与 RGB 受控电源

PY_EPD_EN 控制 U1 MT9700 生成 EPD_3V3_L3B，PY_SD_PWR_EN 控制 U24 MT9700 生成 TF_3V3_L3B，PY_RGB_PWR_EN 控制 MOSFET 电路生成 RGB_3V3_L3B；三路均以上游 3V3_L2 为输入。

- 参数与网络：`eink_rail=EPD_3V3_L3B`；`sd_rail=TF_3V3_L3B`；`rgb_rail=RGB_3V3_L3B`
- 证据：图 51251532fbba / 第 1 页 / Power Network 区 B5-B8，EINK/TF/RGB 受控支路; 图 1095527840e2 / 第 1 页 / EINK 区 A5-A6、IR/RGB 区 C4-C5、TF 区 D4-D5

## 接口

### USB Type-C 电源与数据路径

J1 将 CC1/CC2 分别通过 5.1K 电阻接地，VBUS 形成 VUSBIN 并经 U2 AW32901FCR 保护；USB_DN/USB_DP 经 TVS1/TVS2 ESD5311 保护后连接 SOC_DM/SOC_DP，主控侧还有 22Ω 串联电阻和 ICMF062P900MFR 共模滤波器。

- 参数与网络：`cc_pulldown_ohm=5100`；`usb_dm_gpio=19`；`usb_dp_gpio=20`
- 证据：图 298eb46ddad2 / 第 1 页 / TYPEC 区 A1-A2 与 Core MCU 区 D5-D6，J1、TVS1/2、U2、R24/R25、U10 共模滤波器

### E Ink SPI、控制和电源接口

J5 50-pin FPC 接口承载 EINK_RST、EINK_BUSY、EINK_DC、EINK_CS、SPI_CLK、SPI_MOSI，以及 EPD_3V3_L3B、VPC、PREVGH、VGH、VGL、RESEC/GDRC 等面板电源网络；U1 MT9700 由 PY_EPD_EN 控制面板 3.3V，外围升压和反相电路生成面板高压轨。

- 参数与网络：`supply=EPD_3V3_L3B`；`enable=PY_EPD_EN`；`connector_pins=50`
- 证据：图 1095527840e2 / 第 1 页 / EINK 区 A5-D6，U1、Q9、高压网络与 J5 50-pin FPC

### 12 针 SPI 扩展接口

J6 引出 3V3_L2、TF_3V3_L3B、GPIO8_EXT、EXT_INT、EXT_BUSY、EXT_RST、SPI_MISO、SPI_MOSI、EXT_CS、SPI_CLK 和 GND；EXT_INT 由 R75 10K 上拉到 3V3_L2。

- 参数与网络：`connector_pins=12`；`interrupt=EXT_INT`；`chip_select=EXT_CS`
- 证据：图 1095527840e2 / 第 1 页 / SPI Expansion 区 D2-D3，J6 与 R75

### Grove/HY2.0-4P 端口

J3 CON4 的四线为 GROVE_5V、GROVE_I、GROVE_O 和 GND，信号线上串接双向保护器件；ESP32-S3R8 GPIO4/GPIO5 对应 Grove 两路数字信号，端口电源可在输出与外部输入方向之间切换。

- 参数与网络：`pin_count=4`；`power=GROVE_5V`
- 证据：图 298eb46ddad2 / 第 1 页 / Grove two-way control 区 D3-D4，J3、U5 与 GROVE_I/GROVE_O; 图 51251532fbba / 第 1 页 / I/Os Map 区 C5-D8，ESP32 GPIO4/GPIO5 与 GROVE 功能

### 红外发射与双 RGB LED

IR_TX 通过 Q6 2N7002T 驱动红外发射二极管，供电侧串联 R37 150Ω；LED3/LED4 为两颗串接 WS2812B-4020，数据输入为 RGB，电源 RGB_3V3_L3B 由 PY_RGB_PWR_EN 控制。

- 参数与网络：`ir_gpio=48`；`rgb_gpio=21`；`rgb_count=2`
- 证据：图 1095527840e2 / 第 1 页 / IR/RGB 区 C4-C5，Q6、R37、LED3/LED4 与电源开关

## 总线

### SYS_SCL/SYS_SDA 系统 I2C

ESP32-S3R8 GPIO2/GPIO3 与 M5PM1 I2C_SCL_OD/I2C_SDA_OD 共用 SYS_SCL/SYS_SDA；R22/R23 各 2.2K 上拉到 3V3_L2。RX8130CE 与 SHT40 直接挂载，音频侧经 2N7002DW 热插拔隔离级连接 AUDIO_I2C_SCL/SDA。

- 参数与网络：`scl=SYS_SCL`；`sda=SYS_SDA`；`pullup_ohm=2200`
- 证据：图 298eb46ddad2 / 第 1 页 / PMIC 区 C1-D2 与 Core MCU 区 C4-D6，SYS_SCL/SYS_SDA; 图 1095527840e2 / 第 1 页 / I2C HOT PLUGIN 区 A1-B2、RTC/SHT40 区 D1-D2

## GPIO 与控制信号

### M5PM1 控制与唤醒映射

M5PM1 的 DCDC3V3_EN_PP、LDO3V3_EN_PP、BOOST5V_EN_PP 分别连接 PY_MPWR_EN、PY_RGB_PWR_EN、PY_GROVE_OUT_EN；BAT_ADC_IN/EN_OD 连接 BAT_ADC/BAT_ADC_EN；G0、G2、G4、G3、G1 分别连接 PY_EPD_EN、RTC_IRQ、PY_SD_DET_EN、PY_SD_PWR_EN、CARD_DEC；BOOT_OUT_OD 与 BTN_PU 连接 PY_BOOT_OUT 与 PWR_KEY。

- 参数与网络：`i2c_scl=SYS_SCL`；`i2c_sda=SYS_SDA`
- 证据：图 51251532fbba / 第 1 页 / I/Os Map 区 C4-D5，PMIC 信号表; 图 298eb46ddad2 / 第 1 页 / PMIC 区 C1-D2，U14 PY32_PMIC 引脚网络

### ESP32-S3R8 主要 GPIO 映射

U7 将 GPIO0 连接 PY_BOOT_OUT，GPIO1/9/10 连接 USER_KEY1/2/3，GPIO2/3 连接 SYS_SCL/SYS_SDA，GPIO6 连接 EXT_INT，GPIO7 连接 RTC_IRQ，GPIO11/12 连接 EINK_BUSY/EINK_RST，GPIO13/14/15 连接 SPI_MOSI/SPI_MISO/SPI_CLK，GPIO19/20 连接 SOC_DM/SOC_DP，GPIO21 连接 RGB，GPIO38-42 连接 I2S_DSDIN/SDOUT/BCLK/LRCK/MCLK，GPIO43/44 连接 EINK_DC/EINK_CS，GPIO45 连接 AUDIO_PWR_EN，GPIO47 连接 Card_CS，GPIO48 连接 IR_TX。

- 参数与网络：`system_i2c_scl_gpio=2`；`system_i2c_sda_gpio=3`；`usb_dm_gpio=19`；`usb_dp_gpio=20`
- 证据：图 51251532fbba / 第 1 页 / I/Os Map 区 C5-D8，ESP32 GPIO 与各功能框; 图 298eb46ddad2 / 第 1 页 / Core MCU 区 C4-D6，U7 ESP32_S3R8 引脚网络

### 三个用户按键

S1/S2/S3 分别把 USER_KEY1/USER_KEY2/USER_KEY3 按下接地，各信号由 10K 电阻上拉到 3V3_L2 并有 100nF 电容对地；三路连接 ESP32-S3R8 GPIO1/GPIO9/GPIO10，可作为低功耗唤醒输入。

- 参数与网络：`key1_gpio=1`；`key2_gpio=9`；`key3_gpio=10`；`active_low=true`
- 证据：图 1095527840e2 / 第 1 页 / KEY 区 B4-B5，S1/S2/S3、R25/R31/R38 与 C44/C50/C64; 图 51251532fbba / 第 1 页 / Power Mode 与 I/Os Map 区 C1-D8，USER_KEY1/2/3 唤醒与 GPIO

## 时钟

### ESP32-S3R8 40MHz 晶振

X1 标注 40MHz/15pF/10ppm，连接 XTAL_P/XTAL_N；XTAL_P 侧串联 L5 22nH，C32/C33 各 22pF 接地。

- 参数与网络：`frequency_mhz=40`；`tolerance_ppm=10`；`load_pf=15`
- 证据：图 298eb46ddad2 / 第 1 页 / Core MCU 区 B5-B6，X1、L5、C32、C33 与 XTAL_P/N

### RX8130CE RTC 与唤醒

U17 RX8130CE 通过 SYS_SCL/SYS_SDA 接入系统 I2C，nIRQ 经 R60 连接 RTC_IRQ；VBAT 接 SYS_VBUS，VDD 经 R99 0Ω 接 3V3_L0，RTC_IRQ 同时进入 M5PM1 的 G2_WAKEin 和 ESP32-S3R8 GPIO7。

- 参数与网络：`interrupt=RTC_IRQ`；`rtc_supply=3V3_L0`；`backup_supply=SYS_VBUS`
- 证据：图 1095527840e2 / 第 1 页 / RTC 区 D1-D2，U17、R60、R98/R99 与 SYS_VBUS/3V3_L0; 图 51251532fbba / 第 1 页 / Power Mode 与 I/Os Map 区 C1-D8，RTC_IRQ 唤醒路径

## 存储

### W25Q128JVPIQ 外部 NOR Flash

U9 标注 W25Q128JVPIQ，VCC 接 VDD_NOR，nCS/SCLK/SI/SO/nWP/HOLD 分别连接 NOR_CS、NOR_SCK、NOR_D1、NOR_D0、NOR_WP、NOR_HOLD。

- 参数与网络：`part_number=W25Q128JVPIQ`；`supply=VDD_NOR`
- 证据：图 298eb46ddad2 / 第 1 页 / Core MCU 区 B6，U9 W25Q128JVPIQ

### 受控电源 microSD 接口

U16 MicroSD 的 CLK/CMD/DAT0/DAT1 分别连接 SPI_CLK/SPI_MOSI/SPI_MISO 与卡检测相关网络，Card_CS 为片选；U24 MT9700 由 PY_SD_PWR_EN 控制 TF_3V3_L3B，PY_SD_DET_EN 控制检测上拉，CARD_DEC 回到 M5PM1，TVS3-TVS6 ESD5311 保护信号线。

- 参数与网络：`power=TF_3V3_L3B`；`power_enable=PY_SD_PWR_EN`；`detect_enable=PY_SD_DET_EN`；`detect=CARD_DEC`
- 证据：图 1095527840e2 / 第 1 页 / TF 区 D4-D5，U16/U24、TVS3-TVS6 与检测电路

## 音频

### ES8311 与 ES7210 数字音频链路

U10 ES8311 与 U11 ES7210 共享 I2S_MCLK、I2S_BCLK 和 I2S_LRCK；ES8311 使用 I2S_DSDIN 接收播放数据并输出 DAC_P/DAC_N，ES7210 使用 I2S_SDOUT 输出采集数据。两器件分别通过 AUDIO_I2C_SCL/SDA 配置，并由 CODEC_3V3_L3B 供电。

- 参数与网络：`codec=ES8311`；`adc=ES7210`；`power=CODEC_3V3_L3B`
- 证据：图 1095527840e2 / 第 1 页 / Audio Codec 与 Audio ADC 区 A1-C3，U10/U11 数字总线

### 麦克风采集与 AEC 回采

U12 模拟 MEMS 麦克风由 VBIAS_MIC 供电，MIC_P/MIC_N 经 C111/C112 接 ES7210 MIC1P/MIC1N；扬声器 DAC_P/DAC_N 经 AEC Filtering 网络形成 MIC_3P/MIC_3N，再经 C113/C114 接 ES7210 MIC3P/MIC3N。

- 参数与网络：`microphone_input=MIC1`；`aec_input=MIC3`
- 证据：图 1095527840e2 / 第 1 页 / Audio ADC、Audio Codec、AEC Filtering 与 MIC 区 A1-C3

### AW8737A 扬声器输出

U13 AW8737A 以 DAC_P/DAC_N 为差分输入，SHDN 由 SPK_EN 控制，VOP/VON 经 FB1/FB2 连接 J4 两针 SPK；功放电源直接来自 SYS_VBUS。

- 参数与网络：`amplifier=AW8737A`；`enable=SPK_EN`；`supply=SYS_VBUS`
- 证据：图 1095527840e2 / 第 1 页 / SPEAK 区 A4-A5，U13、FB1/FB2 与 J4

## 传感器

### SHT40 温湿度传感器

U19 标注 SHT40I-AD1B-R2，SCL/SDA 分别接 SYS_SCL/SYS_SDA，VDD 接 3V3_L2；图中备注要求避免使用发热器件，并建议开槽、钻孔或切开铜皮以降低热耦合。

- 参数与网络：`supply=3V3_L2`；`scl=SYS_SCL`；`sda=SYS_SDA`
- 证据：图 1095527840e2 / 第 1 页 / SHT40 区 D1-D2，U19 与热设计备注

## 射频

### 板载 PIFA 天线

ESP32-S3R8 LNA_IN 经板载匹配网络连接 ANT1 ANT_PIFA；匹配网络包含 L2、L3、C82、C3，并在两处标注 Z=50R。

- 参数与网络：`impedance_ohm=50`；`antenna=ANT_PIFA`
- 证据：图 298eb46ddad2 / 第 1 页 / Core MCU 区 C4，ANT1、L2/L3/C82/C3 与 Z=50R 标注

## 调试与烧录

### ESP32-S3R8 原生 USB

U7 GPIO19/GPIO20 分别连接 SOC_DM/SOC_DP，经 22Ω 串联电阻与共模滤波器到 J1 USB_DN/USB_DP，构成无需外置 USB-UART 的原生 USB 数据和下载路径。

- 参数与网络：`dm=GPIO19`；`dp=GPIO20`
- 证据：图 298eb46ddad2 / 第 1 页 / Core MCU 区 D5-D6，U7 GPIO19/GPIO20、SOC_DM/SOC_DP 与 USB_N/USB_P

## 模拟电路

### 电池电压采样

Q1A/Q1B CJ3439KDW 与 BAT_ADC_EN 构成受控电池采样路径，VBAT 经开关和 R7/R86 分压输出 BAT_ADC 到 M5PM1 的 BAT_ADC_IN，BAT_ADC_EN_OD 控制采样使能。

- 参数与网络：`sense_net=BAT_ADC`；`enable_net=BAT_ADC_EN`
- 证据：图 298eb46ddad2 / 第 1 页 / PowerPath 区 A4-B4，Q1A/Q1B、BAT_ADC_EN 与 BAT_ADC

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | PaperColor 三页硬件架构 | `schematic_revision=V0.5`；`schematic_date=2026-04-24`；`page_count=3` |
| 系统结构 | L0/L1/L2/L3A/L3B 电源模式 | `shipping=L0`；`standby=L1`；`deep_sleep=L2`；`core_active=L3A`；`all_active=L3B` |
| 电源 | USB 输入、充电和电池主路径 | `battery_capacity_mah=1250`；`charge_label=0.5C`；`main_bus=SYS_VBUS` |
| 核心器件 | 充电控制器型号 | `overview_label=IP2316`；`detail_label=IP2315` |
| 模拟电路 | 电池电压采样 | `sense_net=BAT_ADC`；`enable_net=BAT_ADC_EN` |
| 电源 | 3V3_L0 常开电源域 | `input=SYS_VBUS`；`output=3V3_L0`；`always_on=true` |
| 电源 | 3V3_L2 主电源域 | `input=SYS_VBUS`；`output=3V3_L2`；`enable=PY_MPWR_EN` |
| 电源 | CODEC_3V3_L3B 音频电源 | `input=SYS_VBUS`；`output=CODEC_3V3_L3B`；`enable=AUDIO_PWR_EN` |
| 电源 | Grove 5V 双向电源控制 | `control=PY_GROVE_OUT_EN`；`port_power=GROVE_5V`；`system_input=SYS_5VIN` |
| 电源 | E Ink、microSD 与 RGB 受控电源 | `eink_rail=EPD_3V3_L3B`；`sd_rail=TF_3V3_L3B`；`rgb_rail=RGB_3V3_L3B` |
| GPIO 与控制信号 | M5PM1 控制与唤醒映射 | `i2c_scl=SYS_SCL`；`i2c_sda=SYS_SDA` |
| GPIO 与控制信号 | ESP32-S3R8 主要 GPIO 映射 | `system_i2c_scl_gpio=2`；`system_i2c_sda_gpio=3`；`usb_dm_gpio=19`；`usb_dp_gpio=20` |
| 总线 | SYS_SCL/SYS_SDA 系统 I2C | `scl=SYS_SCL`；`sda=SYS_SDA`；`pullup_ohm=2200` |
| 总线地址 | 正文列出的 I2C 地址 | `m5pm1=0x6e`；`es8311=0x18`；`es7210=0x40`；`rx8130ce=0x32`；`sht40=0x44` |
| 存储 | W25Q128JVPIQ 外部 NOR Flash | `part_number=W25Q128JVPIQ`；`supply=VDD_NOR` |
| 存储 | 16MB Flash 容量 | `documented_capacity_mb=16`；`schematic_part_number=W25Q128JVPIQ` |
| 内存与 Flash | ESP32-S3R8 与 8MB PSRAM | `documented_capacity_mb=8`；`schematic_part_number=ESP32-S3R8` |
| 时钟 | ESP32-S3R8 40MHz 晶振 | `frequency_mhz=40`；`tolerance_ppm=10`；`load_pf=15` |
| 射频 | 板载 PIFA 天线 | `impedance_ohm=50`；`antenna=ANT_PIFA` |
| 接口 | USB Type-C 电源与数据路径 | `cc_pulldown_ohm=5100`；`usb_dm_gpio=19`；`usb_dp_gpio=20` |
| 调试与烧录 | ESP32-S3R8 原生 USB | `dm=GPIO19`；`dp=GPIO20` |
| 接口 | E Ink SPI、控制和电源接口 | `supply=EPD_3V3_L3B`；`enable=PY_EPD_EN`；`connector_pins=50` |
| 核心器件 | E Ink 面板型号、尺寸和分辨率 | `documented_model=ED2208-DOA (EL040EF1)`；`documented_size_inch=4`；`documented_resolution=400x600` |
| 音频 | ES8311 与 ES7210 数字音频链路 | `codec=ES8311`；`adc=ES7210`；`power=CODEC_3V3_L3B` |
| 音频 | 麦克风采集与 AEC 回采 | `microphone_input=MIC1`；`aec_input=MIC3` |
| 音频 | AW8737A 扬声器输出 | `amplifier=AW8737A`；`enable=SPK_EN`；`supply=SYS_VBUS` |
| 音频 | 扬声器额定功率和阻抗 | `documented_power_w=1`；`documented_impedance_ohm=8`；`documented_size=2520` |
| 时钟 | RX8130CE RTC 与唤醒 | `interrupt=RTC_IRQ`；`rtc_supply=3V3_L0`；`backup_supply=SYS_VBUS` |
| 传感器 | SHT40 温湿度传感器 | `supply=3V3_L2`；`scl=SYS_SCL`；`sda=SYS_SDA` |
| 存储 | 受控电源 microSD 接口 | `power=TF_3V3_L3B`；`power_enable=PY_SD_PWR_EN`；`detect_enable=PY_SD_DET_EN`；`detect=CARD_DEC` |
| 接口 | 12 针 SPI 扩展接口 | `connector_pins=12`；`interrupt=EXT_INT`；`chip_select=EXT_CS` |
| 接口 | Grove/HY2.0-4P 端口 | `pin_count=4`；`power=GROVE_5V` |
| GPIO 与控制信号 | 三个用户按键 | `key1_gpio=1`；`key2_gpio=9`；`key3_gpio=10`；`active_low=true` |
| 接口 | 红外发射与双 RGB LED | `ir_gpio=48`；`rgb_gpio=21`；`rgb_count=2` |

## 待确认事项

- `component.charger-model-conflict`：同一套 V0.5 资源存在型号冲突：第一页 Power Network 把充电器标为 IP2316，第二页 CHARG 详图的 U3 标为 IP2315，无法仅凭当前三页确定量产器件。（证据：图 51251532fbba / 第 1 页 / Power Network 区 A3，IP2316 0.5C; 图 298eb46ddad2 / 第 1 页 / CHARG 区 A3，PD Only IP2315 与 U3）
- `address.documented-i2c-addresses`：产品正文列出 M5PM1=0x6e、ES8311=0x18、ES7210=0x40、RX8130CE=0x32、SHT40=0x44；三页原理图只显示器件及总线网络，没有这些 7-bit 地址或地址脚配置标注，因此地址仍需数据手册或实机扫描确认。（证据：图 298eb46ddad2 / 第 1 页 / PMIC 与 Core MCU 区，U14/U7 的 SYS_SCL/SYS_SDA; 图 1095527840e2 / 第 1 页 / Audio、RTC 与 SHT40 区，U10/U11/U17/U19 总线连接但无地址标注）
- `storage.documented-flash-capacity`：正文称板载 Flash 为 16MB，原理图 U9 标注 W25Q128JVPIQ 并显示 NOR 连线，但图面没有单独写出 bit 或 byte 容量，容量换算需由器件 datasheet 或 BOM 确认。（证据：图 298eb46ddad2 / 第 1 页 / Core MCU 区 B6，U9 W25Q128JVPIQ，未另标容量）
- `memory.documented-psram-capacity`：功能总览与 U7 器件标注均为 ESP32-S3R8，正文称内置 8MB PSRAM；三页原理图没有独立 PSRAM、容量字段或封装内存配置表，容量需由 ESP32-S3R8 datasheet 或量产 BOM 确认。（证据：图 51251532fbba / 第 1 页 / Functions 区 A1，SOC Feature 标注 ESP32-S3R8; 图 298eb46ddad2 / 第 1 页 / Core MCU 区 C4-D6，U7 ESP32_S3R8，未标 PSRAM 容量）
- `component.eink-panel-spec`：正文称面板为 4 英寸 E Ink Spectra 6、ED2208-DOA/EL040EF1、400x600；原理图只画 J5 50-pin FPC、数字信号和电源网络，未在器件或页标题中标出面板型号、尺寸、色彩体系或分辨率。（证据：图 1095527840e2 / 第 1 页 / EINK 区 B6-D6，J5 仅标 50-pin 引脚与网络）
- `audio.speaker-rating`：正文称内置扬声器为 1W、8Ω、2520；原理图只画 U13 AW8737A、差分输出和 J4 两针 SPK，没有扬声器器件型号、阻抗、额定功率或尺寸标注。（证据：图 1095527840e2 / 第 1 页 / SPEAK 区 A4-A5，J4 仅标 SPK 两针）
- `review.charger-model-conflict`：PaperColor C151 V0.5 量产 BOM 中的充电控制器是 IP2315 还是 IP2316；原因：第一页电源总览标 IP2316，第二页 U3 详图标 IP2315，两个标注直接冲突。
- `review.documented-i2c-addresses`：M5PM1、ES8311、ES7210、RX8130CE 与 SHT40 的量产 7-bit 地址是否与产品正文一致；原因：原理图显示器件和 I2C 网络，但未标出地址或所有地址选择条件。
- `review.documented-flash-capacity`：U9 W25Q128JVPIQ 对应的量产 Flash 容量是否为正文所述 16MB；原因：原理图给出完整器件型号和 NOR 连线，但未在图面单独写出 bit 或 byte 容量。
- `review.documented-psram-capacity`：U7 ESP32-S3R8 封装内 PSRAM 容量是否为正文所述 8MB；原因：原理图只有 ESP32-S3R8 型号，没有内存容量字段或封装配置表。
- `review.eink-panel-spec`：J5 所接量产 E Ink 面板是否为 ED2208-DOA/EL040EF1、4 英寸、400x600、Spectra 6；原因：主板原理图仅给 50-pin FPC 和电源网络，未给面板型号、尺寸、分辨率或色彩体系。
- `review.speaker-rating`：J4 所接量产扬声器是否为 1W、8Ω、2520 规格；原因：原理图仅给 AW8737A、滤波磁珠和两针 SPK 接口，没有扬声器料号或额定参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `51251532fbba1e4a2070e43001ee18bc4768e9132ee903d99bb52041d303214d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/C151-SCH_PaperColor_V0.5_SCH_PDF_20260424_EN_2026_04_24_11_01_17_page_01.png` |
| 2 | 1 | `298eb46ddad2a0c678f8685544feec805099f27ea33008ca760f5e8189011548` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/C151-SCH_PaperColor_V0.5_SCH_PDF_20260424_EN_2026_04_24_11_01_17_page_02.png` |
| 3 | 1 | `1095527840e25c09a00ce55701db03a5a7b94c28cb2c63e46e03983e3d632ccb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/C151-SCH_PaperColor_V0.5_SCH_PDF_20260424_EN_2026_04_24_11_01_17_page_03.png` |

---

源文档：`zh_CN/core/PaperColor.md`

源文档 SHA-256：`3d42fca51d9020c08eac4ebd1a72e629ee6672fa512bffdca359c414da3dda50`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
