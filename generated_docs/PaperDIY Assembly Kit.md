# PaperDIY Assembly Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PaperDIY Assembly Kit |
| SKU | K159 |
| 产品 ID | `paperdiy-assembly-kit-d0e86df6fdd8` |
| 源文档 | `zh_CN/core/PaperDIY_Assembly_Kit.md` |

## 概述

PaperDIY Assembly Kit 是 K159 自主装配版 4.7 英寸电子墨水屏开发套件，由 ESP32-S3-WROOM-1、M5PM1/PY32L020F15U6 电源管理、USB-C/锂电池供电、microSD 与两路 12Pin FPC 扩展构成；原理图另含 EPD 正负压、VCOM/VGH/VGL 驱动网络和按键保护电路。

## 检索关键词

`PaperDIY Assembly Kit`、`K159`、`ESP32-S3-WROOM-1`、`PY32L020F15U6`、`M5PM1`、`AXE544127`、`EPD1`、`LGS4056H`、`AW32901FCR`、`SY8089AAAC`、`MT9700`、`MT3608`、`TPS7A2033PDBVR`、`LP5907`、`CH213K`、`CJ3439KDW`、`USB_5V`、`SYS_VBUS`、`VBAT`、`3V3_L2`、`3V3_L0`、`3V3_AU`、`EPD_PWR`、`EPD_VPOS`、`EPD_VNEG`、`SYS_SCL`、`SYS_SDA`、`CARD_SCK`、`microSD`、`FPC 0.5mm-12P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3-WROOM-1 | 主控模组，提供 GPIO、USB、I2C、SPI、EPD 并行控制和启动引脚 | 图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：U1 型号、引脚号与网络名） |
| U2 | PY32L020F15U6 (PY32_PMIC) | M5PM1 电源管理控制器，管理电源模式、充电使能、ADC、LED 与唤醒信号 | 图 26546fd01aa3 / 第 1 页 / 图1（A1-A2：Functions 表中 PMIC 型号 PY32L020F15U6）; 图 8c6b37330dbe / 第 1 页 / 图3（A3-B4：U2 PY32_PMIC 引脚与网络） |
| U3 | LGS4056H(DFN-8) | 单节锂电池线性充电器，输出 VBAT 并给出充电状态 | 图 8c6b37330dbe / 第 1 页 / 图3（A2-B2：U3 型号及 VCC/CE/PROG/BAT/CHRG 引脚） |
| U4 | AW32901FCR | USB 输入过压/过流保护与负载开关，VUSBIN 转 USB_5V | 图 8c6b37330dbe / 第 1 页 / 图3（A1-B1：U4 型号及 IN/OUT/OVLO/nEN 引脚） |
| U5 | SY8089AAAC | SYS_VBUS 转 3V3_L2 的降压转换器 | 图 8c6b37330dbe / 第 1 页 / 图3（B2：U5、L1、反馈与输出电容网络） |
| U6 / U8 | CH213K | USB_5V 到 SYS_VBUS 的两路并联理想二极管/电源路径器件 | 图 8c6b37330dbe / 第 1 页 / 图3（C1-C2：U6、U8 CH213K 与输入输出网络） |
| U7 / U9 | CH213K | VBAT 到 SYS_VBUS 的两路并联理想二极管/电源路径器件 | 图 8c6b37330dbe / 第 1 页 / 图3（C2-C3：U7、U9 CH213K 与输入输出网络） |
| U10 | LP5907 | SYS_VBUS 转 3V3_L0 的 LDO，为 PMIC 与按键上拉供电 | 图 8c6b37330dbe / 第 1 页 / 图3（D1：U10 LP5907 与 C25/C26） |
| U11 | MT9700 | SYS_VBUS 到 BST_VIN 的 EPD 电源开关 | 图 8320646224ff / 第 1 页 / 图4（A2-B2：U11 MT9700 及 EN/SET 网络） |
| U12 | MT3608 | EPD 正压/负压电源所需的升压开关控制器 | 图 8320646224ff / 第 1 页 / 图4（A2-B3：U12 MT3608、L3、D7、反馈网络） |
| U13 | TPS7A2033PDBVR | SYS_VBUS 转 3V3_AU 的低噪声 LDO | 图 8c6b37330dbe / 第 1 页 / 图3（D3-D4：U13 TPS7A2033PDBVR 与 C54/C55） |
| EPD1 | AXE544127 | 44Pin 电子墨水屏连接器，包含 VPOS/VNEG/VCOM/VGH/VGL、控制与 8 位数据 | 图 8320646224ff / 第 1 页 / 图4（A3-D4：EPD1 AXE544127 全部引脚与网络） |
| J1 | USB_C_16P_Horizontal | USB Type-C 16Pin 卧式接口，提供 VBUS、USB 数据、CC 和壳体接地 | 图 8c6b37330dbe / 第 1 页 / 图3（A1：J1 引脚、R9/R10/R13/R14 与 ESD 网络） |
| J2 | microSD (TF) | microSD 卡座，连接 4 线 SPI、卡检测、3V3_L2 与 GND | 图 8320646224ff / 第 1 页 / 图4（C1-D2：J2 TF 卡座及 R35/R36/R39/R40、C46） |
| JP1 | 未标注 | 两 Pin 电池连接器，Pin2 接 VBAT、Pin1 接 GND | 图 8c6b37330dbe / 第 1 页 / 图3（A2：JP1 两 Pin 与 VBAT/GND 网络） |
| JP2 | FPC 0.5mm-12P | 12Pin FPC 扩展，提供 I2S 时钟/数据、I2C、PY_G0 与 3V3_AU | 图 8320646224ff / 第 1 页 / 图4（A1-A2：JP2 及 C52/C53） |
| JP3 | FPC 0.5mm-12P | 12Pin FPC 扩展，提供 SPI、复位、BUSY、IRQ、SW 与 3V3_L2 | 图 8320646224ff / 第 1 页 / 图4（A2-B2：JP3 及 C43） |
| Q1A / Q1B | CJ3439KDW | VBAT 电池电压采样通路的双 MOSFET 开关 | 图 8c6b37330dbe / 第 1 页 / 图3（C3-D3：Q1A/Q1B、R22/R23/R24/R25、C27） |
| D1 / D2 | ESD5311 | USB_DP 与 USB_DM 的 ESD 保护 | 图 8c6b37330dbe / 第 1 页 / 图3（A1：D1、D2 分别连接 USB_DP/USB_DM） |
| D3 / D4 / D5 | ESD5311 | G3_KEY2、G4_KEY1、PY_BTN 按键网络 ESD 保护 | 图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：三组 TS_015 按键与 ESD5311） |
| D6 / D7 | B5819WS | EPD_VNEG/EPD_VPOS 电源支路肖特基二极管 | 图 8320646224ff / 第 1 页 / 图4（A2-B3：D6、D7 与 L2/L4 网络） |
| D8 / D9 / D13 | 1N4148WT / BZT52C7V5S | EPD_VPOS 到 EPD_VGH 的二极管/稳压网络 | 图 8320646224ff / 第 1 页 / 图4（B2-C3：D8、D9、D13 与 R30/R31、C37/C38/C39） |
| D10 / D12 | BZT52C9V1S | EPD_VNEG 到 EPD_VGL 的稳压二极管 | 图 8320646224ff / 第 1 页 / 图4（B3-C4：D10/D12 与 R32/R33、C40/C41/C42） |
| D11 | 未标注 | EPD_VNEG 到 EPD_VGL 网络中的二极管，图面未标注型号 | 图 8320646224ff / 第 1 页 / 图4（B3-C4：D11 与 R32/R33、C40/C41/C42） |
| L1 | MWTC201608S2R2MT | SY8089 降压转换器开关电感 | 图 8c6b37330dbe / 第 1 页 / 图3（B2：L1 位于 U5 LX 与 3V3_L2 之间） |
| L2 / L4 | WPN201610H4R7MT | EPD 正负压支路的 4.7uH 电感 | 图 8320646224ff / 第 1 页 / 图4（A2-B3：L2、L4 与 D6/D7、C28/C35/C36） |
| L3 | WPN201610H2R2MT | MT3608 开关节点串联的 2.2uH 电感 | 图 8320646224ff / 第 1 页 / 图4（A2-B3：L3 位于 BST_VIN 与 U12 SW 之间） |
| S1 / S2 / S3 | TS_015 | KEY2、KEY1 与电源/唤醒按键 | 图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：S1/S2/S3 与上拉、ESD 网络） |
| LED1 | 未标注 | PY_LED 驱动的红色指示 LED | 图 8c6b37330dbe / 第 1 页 / 图3（B4：LED1、R21 1K 与 PY_LED） |
| R1 / R2 | 2.2K | SYS_SCL/SYS_SDA 到 3V3_L2 的 I2C 上拉 | 图 4d2aad0f2b99 / 第 1 页 / 图2（B3：R1/R2 2.2K/1%） |
| R3 / R4 | 100R / 22R | EPD_XCL 与 CARD_SCK 的串联电阻 | 图 4d2aad0f2b99 / 第 1 页 / 图2（A2-B3：R3 EPD_XCL、R4 CARD_SCK） |
| R9 / R10 / R13 / R14 | 22R / 5.1K | USB 数据串联电阻与 USB-C CC1/CC2 下拉电阻 | 图 8c6b37330dbe / 第 1 页 / 图3（A1：R9/R10 22R、R13/R14 5.1K） |
| R41 / R42 / R43 | 1M / 1M / NC | KEY2、KEY1 与 PY_BTN 的 3V3_L0 上拉网络 | 图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：R41/R42 1M、R43 NC） |
| C1 / C2 | 10uF | U1 3V3_L2 电源去耦 | 图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B1：C1/C2 10uF/6.3V） |
| R17 / R20 / C16 | 1K / 1K / 100nF | USB_5V 到 USB_ADC 的分压与滤波网络 | 图 8c6b37330dbe / 第 1 页 / 图3（B1：R17/R20 1K/1%、C16 100nF/50V） |
| R23 / R25 / C27 | 1K / 1K / 100nF | VBAT 采样分压与 BAT_ADC 滤波 | 图 8c6b37330dbe / 第 1 页 / 图3（C3-D3：R23/R25 1K/1%、C27 100nF/50V） |
| R26 / R29 / C32 | 120K / 5.1K / 22pF | MT3608 反馈分压与前馈电容 | 图 8320646224ff / 第 1 页 / 图4（B2-B3：R26/R29、C32） |
| R35 / R36 / R39 / R40 | NC | microSD SPI 信号串联位，原理图均标注 NC | 图 8320646224ff / 第 1 页 / 图4（C1-D2：R35/R36/R39/R40 标注 NC） |
| R30 / R31 / R32 / R33 | 120K | EPD VPOS/VGH 与 VNEG/VGL 支路的平衡电阻 | 图 8320646224ff / 第 1 页 / 图4（B2-C4：R30/R31、R32/R33 均为 120K/1%） |
| C43 / C46 / C52 / C53 | C43=22uF; C46=10uF; C52/C53=10uF | JP3、microSD 与 JP2 的本地电源去耦 | 图 8320646224ff / 第 1 页 / 图4（A1-A2：C52/C53 10uF/16V）; 图 8320646224ff / 第 1 页 / 图4（A2-B2：C43 22uF/16V）; 图 8320646224ff / 第 1 页 / 图4（C1-D2：C46 10uF/16V） |
| C50 / C6 / C51 / C7 | 10uF | LGS4056H 充电器输入与 VBAT 输出去耦 | 图 8c6b37330dbe / 第 1 页 / 图3（A2-B2：C50/C6/C51/C7 均为 10uF/10V） |

## 系统结构

### 电源与运行模式

总览图定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE、L3B All ACTIVE 五种模式；PMIC 在五种模式均标为工作，EINK 在 L3B 工作，按键在 L2/L3A/L3B 可唤醒。

- 参数与网络：`modes=L0/L1/L2/L3A/L3B`；`wake_sources=PWR_BTN/KEY1/KEY2`
- 证据：图 26546fd01aa3 / 第 1 页 / 图1（A1-A2：Functions/PowerMode 表）

### 功能域划分

总览将 ESP32-S3、PMIC、BATTERY、EINK、BUTTON、TF 与 EXT.GPIO 归入 SOC、POWER、HMI、FUNC、EXT 五类功能域。

- 参数与网络：`soc=ESP32-S3`；`power=PMIC/BATTERY`；`hmi=EINK/BUTTON`；`func=TF`；`ext=EXT.GPIO`
- 证据：图 26546fd01aa3 / 第 1 页 / 图1（A1-A2：Functions 分类表）

## 核心器件

### U1

U1 为 ESP32-S3-WROOM-1；Pin2=3V3、Pin3=EN/CHIP_PU、Pin1/Pin40/Pin41=GND，USB_DM/USB_DP 分别接 Pin13 IO19 与 Pin14 IO20。

- 参数与网络：`part=ESP32-S3-WROOM-1`；`power=3V3_L2`；`en_pin=3`；`usb_dm_pin=13`；`usb_dp_pin=14`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：U1 各引脚与网络）

### U2

U2 在电源页标为 PY32_PMIC，总览页将 PMIC 型号列为 PY32L020F15U6；VCC Pin6 接 3V3_L0，GND Pin4/Pin21 接地，I2C Pin9/Pin8 为 SYS_SCL/SYS_SDA。

- 参数与网络：`overview_part=PY32L020F15U6`；`symbol=PY32_PMIC`；`vcc_pin=6`；`scl_pin=9`；`sda_pin=8`
- 证据：图 26546fd01aa3 / 第 1 页 / 图1（A1：Functions 表 PMIC/PY32L020F15U6）; 图 8c6b37330dbe / 第 1 页 / 图3（A3-B4：U2 PY32_PMIC 引脚）

### EPD1

EPD1 为 AXE544127 墨水屏连接器，包含 VPOS、VNEG、VCOM、VGH、VGL、XCL/XLE/XOE/XSTL、D0-D7、CKV/SPV/MODE1 与多个 VSS/NC 引脚。

- 参数与网络：`part=AXE544127`；`data_pins=D0-D7`；`power_pins=VPOS/VNEG/VCOM/VGH/VGL`
- 证据：图 8320646224ff / 第 1 页 / 图4（A3-D4：EPD1 AXE544127）

## 电源

### U4

VUSBIN 进入 U4 AW32901FCR 的 IN Pin B3/C2/C3，OUT Pin A2/A3/B2 形成 USB_5V；C12/C13 为 1uF，R17/R20 各 1K 将 USB_5V 分压为 USB_ADC，C16 为 100nF。

- 参数与网络：`input=VUSBIN`；`output=USB_5V`；`input_cap=C12 1uF`；`output_cap=C13 1uF`；`adc_divider=R17/R20 1K/1K`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A1-B1：U4、C12/C13、R17/R20/C16）

### U3

U3 LGS4056H 的 VCC Pin4 接 USB_5V，CE Pin8 接 CHG_EN，PROG Pin2 经 R11 2K 接地，TEMP Pin1 与 PAD Pin0 接地，BAT Pin5 输出 VBAT，CHRG Pin7 为 CHG_STAT；输入 C50/C6 与输出 C51/C7 均为 10uF。

- 参数与网络：`charger=LGS4056H(DFN-8)`；`vcc_pin=4`；`ce_pin=8`；`prog_pin=2`；`prog_r=R11 2K`；`bat_pin=5`；`chrg_pin=7`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A2-B2：U3 LGS4056H 完整引脚网络）

### SYS_VBUS

U6/U8 CH213K 将 USB_5V 汇入 SYS_VBUS，U7/U9 CH213K 将 VBAT 汇入 SYS_VBUS；输入侧 C21-C24 与输出侧 C17-C20 均为 22uF。

- 参数与网络：`usb_path=U6/U8`；`battery_path=U7/U9`；`input_caps=C21-C24 22uF`；`output_caps=C17-C20 22uF`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（C1-C3：四颗 CH213K 与 C17-C24）

### U5

U5 SY8089AAAC 以 SYS_VBUS 为 IN Pin4、PY_MPWR_EN 为 EN Pin1，LX Pin3 经 L1 MWTC201608S2R2MT 产生 3V3_L2；输入 C10/C11/C47 为 10uF，输出 C14/C15/C48/C49 为 22uF，R18 为 EN 下拉 100K。

- 参数与网络：`input=SYS_VBUS`；`enable=PY_MPWR_EN`；`output=3V3_L2`；`inductor=L1 2.2uH`；`en_pulldown=R18 100K`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（B2-B3：U5、L1、输入输出电容与 EN）

### U10

U10 LP5907 的 IN Pin1 与 EN Pin3 接 SYS_VBUS，OUT Pin5 为 3V3_L0；输入 C26 与输出 C25 均为 1uF。

- 参数与网络：`ldo=LP5907`；`input=SYS_VBUS`；`output=3V3_L0`；`caps=C26/C25 1uF`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（D1：U10 LP5907）

### U13

U13 TPS7A2033PDBVR 的 IN Pin1 与 EN Pin3 接 SYS_VBUS，OUT Pin5 为 3V3_AU；输入 C55 与输出 C54 均为 1uF。

- 参数与网络：`ldo=TPS7A2033PDBVR`；`input=SYS_VBUS`；`output=3V3_AU`；`caps=C55/C54 1uF`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（D3-D4：U13 TPS7A2033PDBVR）

### U11

U11 MT9700 的 VIN Pin5 接 SYS_VBUS，EN Pin4 接 BST_EN 并由 R27 10K 下拉，SET Pin3 由 R28 10K 下拉，OUT Pin1 形成 BST_VIN；C33/C34 为 22uF。

- 参数与网络：`input=SYS_VBUS`；`output=BST_VIN`；`enable=BST_EN`；`r27=10K pulldown`；`r28=10K pulldown`；`caps=C33/C34 22uF`
- 证据：图 8320646224ff / 第 1 页 / 图4（A2-B2：U11 MT9700 与 R27/R28/C33/C34）

### U12

U12 MT3608 的 EN Pin4 与 IN Pin5 接 BST_VIN，BST_VIN 经 L3 WPN201610H2R2MT 到 SW 节点，D7 B5819WS 将开关节点整流至 EPD_VPOS；反馈网络为 R26 120K、R29 5.1K 与 C32 22pF，输出侧 C35/C36 为 4.7uF。

- 参数与网络：`boost=MT3608`；`input=BST_VIN`；`inductor=L3 2.2uH`；`rectifier=D7 B5819WS`；`output=EPD_VPOS`；`feedback=R26 120K / R29 5.1K / C32 22pF`
- 证据：图 8320646224ff / 第 1 页 / 图4（A2-B3：U12、L3、D7、反馈与输出电容）

### EPD_VNEG

EPD_VNEG 支路包含 L2 WPN201610H4R7MT、D6 B5819WS 与 C28 4.7uF；EPD_VPOS/EPD_VGH 方向还包含 D13/D8 1N4148WT、D9 BZT52C7V5S、R30/R31 120K 与 C37/C38/C39。

- 参数与网络：`negative_inductor=L2 4.7uH`；`negative_diode=D6 B5819WS`；`negative_cap=C28 4.7uF`；`positive_clamps=D8/D9/D13`；`balance_resistors=R30/R31 120K`
- 证据：图 8320646224ff / 第 1 页 / 图4（A2-C3：EPD_VNEG、EPD_VPOS、EPD_VGH 支路）

### EPD_VCOM

EPD_VNEG 经 R34 5.6K 接到 VCOM 节点，VCOM 另经 R38 1K 与 C44 1uF 到地；EPD_PWR 经 R37 5.1K 与 C45 1uF 到地。

- 参数与网络：`vcom_series=R34 5.6K`；`vcom_divider=R38 1K`；`vcom_cap=C44 1uF`；`epd_pwr_r=R37 5.1K`；`epd_pwr_c=C45 1uF`
- 证据：图 8320646224ff / 第 1 页 / 图4（C2-D3：R34/R38/C44 与 R37/C45）

### Q1A/Q1B

VBAT 经 R22 100K 接 Q1B 栅极网络，Q1A 栅极接 BAT_ADC_EN 且 R24 标注 NC；Q1B 的 VBAT 侧经 R23 1K 到 BAT_ADC 节点，再由 R25 1K 到地，C27 100nF 对地。

- 参数与网络：`gate_pullup=R22 100K`；`enable=BAT_ADC_EN`；`r24=NC`；`top_divider=R23 1K`；`bottom_divider=R25 1K`；`filter=C27 100nF`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（C3-D3：Q1A/Q1B、R22-R25、C27）

## 接口

### J1

J1 USB_C_16P_Horizontal 的 VBUS 为 A4/B9，GND 为 A1/B12，USB 数据为 DP1/DP2(A6/B6) 与 DM1/DM2(A7/B7)，CC1/CC2 为 A5/B5，SBU1/SBU2 为 A8/B8，MH1-MH4 壳体接地。

- 参数与网络：`vbus=A4/B9`；`dp=A6/B6`；`dm=A7/B7`；`cc1=A5`；`cc2=B5`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A1：J1 USB_C_16P_Horizontal 引脚）

### JP2

JP2 的 12Pin 映射为 1=EXT_G5/SCLK、2=GND、3=PY_G0、4=SYS_SDA、5=SYS_SCL、6=GND、7=EXT_G2/LRCK、8=EXT_G1/DSDIN、9=EXT_G0/DOUT、10=EXT_G45/MCLK、11/12=3V3_AU。

- 参数与网络：`pin1=EXT_G5/SCLK`；`pin3=PY_G0`；`pin4=SYS_SDA`；`pin5=SYS_SCL`；`pin7=EXT_G2/LRCK`；`pin8=EXT_G1/DSDIN`；`pin9=EXT_G0/DOUT`；`pin10=EXT_G45/MCLK`；`pin11_12=3V3_AU`
- 证据：图 8320646224ff / 第 1 页 / 图4（A1-A2：JP2 与全部网络）

### JP3

JP3 的 12Pin 映射为 1=CARD_SCK、2=GND、3=G21、4=CARD_MOSI、5=CARD_MISO、6=GND、7=PY_G4、8=U0TXD_GPIO43、9=U0RXD_GPIO44、10=PY_G1、11/12=3V3_L2。

- 参数与网络：`pin1=CARD_SCK`；`pin3=G21`；`pin4=CARD_MOSI`；`pin5=CARD_MISO`；`pin7=PY_G4`；`pin8=U0TXD_GPIO43`；`pin9=U0RXD_GPIO44`；`pin10=PY_G1`；`pin11_12=3V3_L2`
- 证据：图 8320646224ff / 第 1 页 / 图4（A2-B2：JP3 与全部网络）

### S1/S2/S3

S1 连接 G3_KEY2、S2 连接 G4_KEY1、S3 连接 PY_BTN，三者另一端接地；G3_KEY2/G4_KEY1 各由 R41/R42 1M 上拉到 3V3_L0，PY_BTN 的 R43 标注 NC，D3/D4/D5 为 ESD5311。

- 参数与网络：`key2=S1/G3_KEY2`；`key1=S2/G4_KEY1`；`power_key=S3/PY_BTN`；`pullups=R41/R42 1M`；`r43=NC`；`esd=D3/D4/D5 ESD5311`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：S1/S2/S3、R41-R43、D3-D5）

### EPD1

EPD1 的 Pin1/2 为 EPD_VNEG/EPD_VPOS，Pin7/12/23/38 接 EPD_PWR，Pin10-13 为 EPD_XCL/XLE/EPD_PWR/XSTL，Pin14-21 为 EPD_DB0-EPD_DB7，Pin24/26 为 VCOM、Pin25/27 为 EPD_VGH、Pin31/33 为 EPD_VGL，Pin36/37 为 EPD_CKV/EPD_SPV。

- 参数与网络：`pin1=EPD_VNEG`；`pin2=EPD_VPOS`；`power_pins=7/12/23/38 EPD_PWR`；`data_pins=14-21 DB0-DB7`；`vcom_pins=24/26 VCOM`；`vgh_pins=25/27 EPD_VGH`；`vgl_pins=31/33 EPD_VGL`
- 证据：图 8320646224ff / 第 1 页 / 图4（A3-D4：EPD1 AXE544127 引脚映射）

## 总线

### USB_DM/USB_DP

J1 的 USB_DM 经 R10 22R 接 U1 IO19 Pin13，USB_DP 经 R9 22R 接 U1 IO20 Pin14；两条数据线分别由 D2/D1 ESD5311 保护。

- 参数与网络：`dm_series=R10 22R`；`dp_series=R9 22R`；`dm_mcu_pin=IO19/13`；`dp_mcu_pin=IO20/14`；`esd=D1/D2 ESD5311`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B1：USB_DM/USB_DP 至 IO19/IO20）; 图 8c6b37330dbe / 第 1 页 / 图3（A1：R9/R10 与 D1/D2）

### SYS_SCL/SYS_SDA

SYS_SCL 接 U1 IO42 Pin35、SYS_SDA 接 U1 IO41 Pin34，并分别由 R1/R2 2.2K 上拉到 3V3_L2；两路同时接 U2 Pin9/Pin8 与 JP2 Pin5/Pin6。

- 参数与网络：`scl_mcu=IO42/35`；`sda_mcu=IO41/34`；`pullups=R1/R2 2.2K`；`pmic=U2 pin9/pin8`；`fpc=JP2 pin5/pin6`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B3：R1/R2 与 SYS_SCL/SYS_SDA）; 图 8c6b37330dbe / 第 1 页 / 图3（A3-A4：U2 I2C）; 图 8320646224ff / 第 1 页 / 图4（A1-A2：JP2 I2C）

### microSD SPI

microSD SPI 使用 CARD_SCK/IO39 Pin32（经 R4 22R）、CARD_MOSI/IO38 Pin31、CARD_MISO/IO40 Pin33、CARD_CS/IO47 Pin24 与 CARD_DET/IO48 Pin25，并接到 J2 Pin5/Pin3/Pin7/Pin2/Pin9。

- 参数与网络：`sck=IO39/32 via R4 22R`；`mosi=IO38/31`；`miso=IO40/33`；`cs=IO47/24`；`det=IO48/25`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B2-C3：CARD_* 网络）; 图 8320646224ff / 第 1 页 / 图4（C1-D2：J2 microSD）

### EPD_DB0-EPD_DB7

EPD 8 位数据总线映射为 EPD_DB0=IO6、EPD_DB1=IO14、EPD_DB2=IO7、EPD_DB3=IO12、EPD_DB4=IO9、EPD_DB5=IO11、EPD_DB6=IO8、EPD_DB7=IO10，并对应 EPD1 Pin14-Pin21 的 D0-D7。

- 参数与网络：`db0=IO6`；`db1=IO14`；`db2=IO7`；`db3=IO12`；`db4=IO9`；`db5=IO11`；`db6=IO8`；`db7=IO10`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：EPD_DB0-EPD_DB7）; 图 8320646224ff / 第 1 页 / 图4（A3-B4：EPD1 D0-D7）

## GPIO 与控制信号

### U1

EPD 控制信号映射为 EPD_XCL=IO16 Pin9、EPD_XLE=IO15 Pin8、EPD_SPV=IO17 Pin10、EPD_CKV=IO18 Pin11、EPD_XSTL=IO13 Pin21、BST_EN=IO46 Pin16。

- 参数与网络：`xcl=IO16/9`；`xle=IO15/8`；`spv=IO17/10`；`ckv=IO18/11`；`xstl=IO13/21`；`bst_en=IO46/16`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：U1 EPD 控制网络）

### U1/PMIC

G4_KEY1 接 U1 IO4 Pin4，G3_KEY2 接 U1 IO3 Pin15；电源按键 PY_BTN 接 U2 BTN_PU Pin7，而不是直接接 ESP32 GPIO。

- 参数与网络：`key1=IO4/4`；`key2=IO3/15`；`power_key=U2 pin7 BTN_PU`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：G4_KEY1/G3_KEY2）; 图 8c6b37330dbe / 第 1 页 / 图3（B3-B4：U2 BTN_PU）

### U2

U2 控制/监测映射包含 PY_MPWR_EN=Pin14、CHG_EN=Pin2、EPD_PWR=Pin20、PY_G0=Pin3、PY_G4=Pin12、CHG_STAT=Pin13、PY_G1=Pin17、PY_LED=Pin5、PY_BOOT=Pin15、PY_BTN=Pin7。

- 参数与网络：`py_mpwr_en=pin14`；`chg_en=pin2`；`epd_pwr=pin20`；`py_g0=pin3`；`py_g4=pin12`；`chg_stat=pin13`；`py_g1=pin17`；`py_led=pin5`；`py_boot=pin15`；`py_btn=pin7`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A3-B4：U2 左侧控制与监测引脚）

## 时钟

### EPD_XCL

EPD_XCL 由 U1 IO16 Pin9 输出，经 R3 100R/1% 串联后接 EPD1 Pin10 XCL。

- 参数与网络：`source=IO16 pin9`；`series_r=R3 100R`；`destination=EPD1 pin10 XCL`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A2：EPD_XCL 与 R3）; 图 8320646224ff / 第 1 页 / 图4（A3-B4：EPD1 XCL）

### EXT_G45/MCLK

JP2 Pin10 的 MCLK 网络为 EXT_G45，对应 U1 IO45 Pin26；同组 I2S 网络还包括 LRCK/EXT_G2、DSDIN/EXT_G1、DOUT/EXT_G0 与 SCLK/EXT_G5。

- 参数与网络：`mclk=EXT_G45/IO45`；`lrck=EXT_G2/IO2`；`dsdin=EXT_G1/IO1`；`dout=EXT_G0/IO0`；`sclk=EXT_G5/IO5`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（A1-B2：EXT_G0-G2/G5/G45）; 图 8320646224ff / 第 1 页 / 图4（A1-A2：JP2 I2S）

## 复位

### U1 EN/CHIP_PU

SOC_RESET 网络由 R7 100K 上拉到 3V3_L2、C4 1uF 对地，并经 R8 0R 接到 U1 EN/CHIP_PU Pin3。

- 参数与网络：`pullup=R7 100K`；`cap=C4 1uF`；`series_r=R8 0R`；`mcu_pin=EN/CHIP_PU pin3`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（C1-D1：SOC_RESET/R7/C4/R8/CHIP_PU）

## 保护电路

### J1/U4

USB-C 数据线使用 R9/R10 22R 串联电阻与 D1/D2 ESD5311 保护，VBUS 经 U4 AW32901FCR 输入保护后形成 USB_5V。

- 参数与网络：`series_r=R9/R10 22R`；`esd=D1/D2 ESD5311`；`input_protection=U4 AW32901FCR`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A1-B1：USB 输入保护）

### CC1/CC2

J1 CC1(A5) 经 R13 5.1K/1% 接地，CC2(B5) 经 R14 5.1K/1% 接地。

- 参数与网络：`cc1_r=R13 5.1K`；`cc2_r=R14 5.1K`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（A1：R13/R14 CC 下拉）

### S1/S2/S3

三个 TS_015 按键的 G3_KEY2、G4_KEY1、PY_BTN 节点分别并联 D3/D4/D5 ESD5311 到地。

- 参数与网络：`key2_esd=D3`；`key1_esd=D4`；`power_key_esd=D5`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：按键 ESD 网络）

## 关键网络

### BST_EN

BST_EN 由 ESP32-S3 IO46 Pin16 引出，接 U11 MT9700 EN Pin4，并由 R27 10K 下拉到地。

- 参数与网络：`source=IO46/16`；`destination=U11 pin4`；`pulldown=R27 10K`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B2：IO46/BST_EN）; 图 8320646224ff / 第 1 页 / 图4（A2-B2：BST_EN/R27/U11 EN）

### EPD_PWR

EPD_PWR 由 U2 Pin20 的 G2_WAKEIn/IRQout_ADC 引出，接 EPD1 Pin7/12/23/38，并在 R37 5.1K 与 C45 1uF 网络处形成本地负载。

- 参数与网络：`source=U2 pin20`；`connector_pins=EPD1 7/12/23/38`；`load_network=R37 5.1K / C45 1uF`
- 证据：图 8c6b37330dbe / 第 1 页 / 图3（B4：U2 pin20 EPD_PWR）; 图 8320646224ff / 第 1 页 / 图4（A3-D4：EPD1 EPD_PWR 与 R37/C45）

### EXT_G0/PY_BOOT

U1 IO0 Pin27 为 EXT_G0；该网络由 R5 10K 上拉到 3V3_L2、C3 标注 NC 对地，并经 D14 与 PY_BOOT 相连。

- 参数与网络：`mcu_net=EXT_G0/IO0/pin27`；`pullup=R5 10K`；`cap=C3 NC`；`diode=D14`；`pmic_net=PY_BOOT`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B1-C1：EXT_G0、R5、C3、D14、PY_BOOT）

## 存储

### J2

J2 microSD 卡座的 DAT0/MISO Pin7、DAT3/CS Pin2、CLK/SCK Pin5、CMD/MOSI Pin3、Detect Pin9、VDD Pin4、VSS Pin6 与 SHELL Pin0 分别接 CARD_MISO、CARD_CS、CARD_SCK、CARD_MOSI、CARD_DET、3V3_L2、GND；对应串联位 R35/R36/R39/R40 均标注 NC。

- 参数与网络：`miso=pin7`；`cs=pin2`；`sck=pin5`；`mosi=pin3`；`det=pin9`；`vdd=pin4 3V3_L2`；`vss=pin6/0 GND`；`series_resistors=R35/R36/R39/R40 NC`
- 证据：图 8320646224ff / 第 1 页 / 图4（C1-D2：J2 TF 卡座与 R35/R36/R39/R40）

## 其他事实

### TP1-TP10

测试点映射为 TP1=CHIP_PU、TP2=U0TXD_GPIO43、TP3=PY_BOOT、TP4=U0RXD_GPIO44、TP5=3V3_L2、TP6=GND、TP9=SYS_SCL、TP10=SYS_SDA。

- 参数与网络：`tp1=CHIP_PU`；`tp2=U0TXD_GPIO43`；`tp3=PY_BOOT`；`tp4=U0RXD_GPIO44`；`tp5=3V3_L2`；`tp6=GND`；`tp9=SYS_SCL`；`tp10=SYS_SDA`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B3-C4：TP1-TP10 测试点框）

### NC 标注

原理图明确标注 C3、R24、R43、R35、R36、R39、R40 为 NC；C3 位于 EXT_G0 对地位置，R24 位于 BAT_ADC_EN 网络，R43 位于 PY_BTN 上拉位置。

- 参数与网络：`page2=C3`；`page3=R24/R43`；`page4=R35/R36/R39/R40`
- 证据：图 4d2aad0f2b99 / 第 1 页 / 图2（B1：C3 NC）; 图 8c6b37330dbe / 第 1 页 / 图3（C3-D4：R24/R43 NC）; 图 8320646224ff / 第 1 页 / 图4（C1-D2：R35/R36/R39/R40 NC）

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 电源与运行模式 | `modes=L0/L1/L2/L3A/L3B`；`wake_sources=PWR_BTN/KEY1/KEY2` |
| 系统结构 | 功能域划分 | `soc=ESP32-S3`；`power=PMIC/BATTERY`；`hmi=EINK/BUTTON`；`func=TF`；`ext=EXT.GPIO` |
| 核心器件 | U1 | `part=ESP32-S3-WROOM-1`；`power=3V3_L2`；`en_pin=3`；`usb_dm_pin=13`；`usb_dp_pin=14` |
| 核心器件 | U2 | `overview_part=PY32L020F15U6`；`symbol=PY32_PMIC`；`vcc_pin=6`；`scl_pin=9`；`sda_pin=8` |
| 核心器件 | EPD1 | `part=AXE544127`；`data_pins=D0-D7`；`power_pins=VPOS/VNEG/VCOM/VGH/VGL` |
| 电源 | U4 | `input=VUSBIN`；`output=USB_5V`；`input_cap=C12 1uF`；`output_cap=C13 1uF`；`adc_divider=R17/R20 1K/1K` |
| 电源 | U3 | `charger=LGS4056H(DFN-8)`；`vcc_pin=4`；`ce_pin=8`；`prog_pin=2`；`prog_r=R11 2K`；`bat_pin=5`；`chrg_pin=7` |
| 电源 | SYS_VBUS | `usb_path=U6/U8`；`battery_path=U7/U9`；`input_caps=C21-C24 22uF`；`output_caps=C17-C20 22uF` |
| 电源 | U5 | `input=SYS_VBUS`；`enable=PY_MPWR_EN`；`output=3V3_L2`；`inductor=L1 2.2uH`；`en_pulldown=R18 100K` |
| 电源 | U5 | `fb_pin=5`；`top_feedback=R16 100K`；`bottom_feedback=R19 22K`；`feedforward_cap=C8 22pF`；`formula_note=Vout=0.6*(1+R18/R19)` |
| 电源 | U10 | `ldo=LP5907`；`input=SYS_VBUS`；`output=3V3_L0`；`caps=C26/C25 1uF` |
| 电源 | U13 | `ldo=TPS7A2033PDBVR`；`input=SYS_VBUS`；`output=3V3_AU`；`caps=C55/C54 1uF` |
| 电源 | U11 | `input=SYS_VBUS`；`output=BST_VIN`；`enable=BST_EN`；`r27=10K pulldown`；`r28=10K pulldown`；`caps=C33/C34 22uF` |
| 电源 | U12 | `boost=MT3608`；`input=BST_VIN`；`inductor=L3 2.2uH`；`rectifier=D7 B5819WS`；`output=EPD_VPOS`；`feedback=R26 120K / R29 5.1K / C32 22pF` |
| 电源 | EPD_VNEG | `negative_inductor=L2 4.7uH`；`negative_diode=D6 B5819WS`；`negative_cap=C28 4.7uF`；`positive_clamps=D8/D9/D13`；`balance_resistors=R30/R31 120K` |
| 电源 | L4 | `part=WPN201610H4R7MT`；`visible_nodes=U12 SW / D7 / GND` |
| 电源 | EPD_VCOM | `vcom_series=R34 5.6K`；`vcom_divider=R38 1K`；`vcom_cap=C44 1uF`；`epd_pwr_r=R37 5.1K`；`epd_pwr_c=C45 1uF` |
| 电源 | Q1A/Q1B | `gate_pullup=R22 100K`；`enable=BAT_ADC_EN`；`r24=NC`；`top_divider=R23 1K`；`bottom_divider=R25 1K`；`filter=C27 100nF` |
| 接口 | J1 | `vbus=A4/B9`；`dp=A6/B6`；`dm=A7/B7`；`cc1=A5`；`cc2=B5` |
| 接口 | JP2 | `pin1=EXT_G5/SCLK`；`pin3=PY_G0`；`pin4=SYS_SDA`；`pin5=SYS_SCL`；`pin7=EXT_G2/LRCK`；`pin8=EXT_G1/DSDIN`；`pin9=EXT_G0/DOUT`；`pin10=EXT_G45/MCLK`；`pin11_12=3V3_AU` |
| 接口 | JP3 | `pin1=CARD_SCK`；`pin3=G21`；`pin4=CARD_MOSI`；`pin5=CARD_MISO`；`pin7=PY_G4`；`pin8=U0TXD_GPIO43`；`pin9=U0RXD_GPIO44`；`pin10=PY_G1`；`pin11_12=3V3_L2` |
| 接口 | S1/S2/S3 | `key2=S1/G3_KEY2`；`key1=S2/G4_KEY1`；`power_key=S3/PY_BTN`；`pullups=R41/R42 1M`；`r43=NC`；`esd=D3/D4/D5 ESD5311` |
| 接口 | EPD1 | `pin1=EPD_VNEG`；`pin2=EPD_VPOS`；`power_pins=7/12/23/38 EPD_PWR`；`data_pins=14-21 DB0-DB7`；`vcom_pins=24/26 VCOM`；`vgh_pins=25/27 EPD_VGH`；`vgl_pins=31/33 EPD_VGL` |
| 总线 | USB_DM/USB_DP | `dm_series=R10 22R`；`dp_series=R9 22R`；`dm_mcu_pin=IO19/13`；`dp_mcu_pin=IO20/14`；`esd=D1/D2 ESD5311` |
| 总线 | SYS_SCL/SYS_SDA | `scl_mcu=IO42/35`；`sda_mcu=IO41/34`；`pullups=R1/R2 2.2K`；`pmic=U2 pin9/pin8`；`fpc=JP2 pin5/pin6` |
| 总线 | microSD SPI | `sck=IO39/32 via R4 22R`；`mosi=IO38/31`；`miso=IO40/33`；`cs=IO47/24`；`det=IO48/25` |
| 总线 | EPD_DB0-EPD_DB7 | `db0=IO6`；`db1=IO14`；`db2=IO7`；`db3=IO12`；`db4=IO9`；`db5=IO11`；`db6=IO8`；`db7=IO10` |
| GPIO 与控制信号 | U1 | `xcl=IO16/9`；`xle=IO15/8`；`spv=IO17/10`；`ckv=IO18/11`；`xstl=IO13/21`；`bst_en=IO46/16` |
| GPIO 与控制信号 | U1/PMIC | `key1=IO4/4`；`key2=IO3/15`；`power_key=U2 pin7 BTN_PU` |
| GPIO 与控制信号 | U2 | `py_mpwr_en=pin14`；`chg_en=pin2`；`epd_pwr=pin20`；`py_g0=pin3`；`py_g4=pin12`；`chg_stat=pin13`；`py_g1=pin17`；`py_led=pin5`；`py_boot=pin15`；`py_btn=pin7` |
| 时钟 | EPD_XCL | `source=IO16 pin9`；`series_r=R3 100R`；`destination=EPD1 pin10 XCL` |
| 时钟 | EXT_G45/MCLK | `mclk=EXT_G45/IO45`；`lrck=EXT_G2/IO2`；`dsdin=EXT_G1/IO1`；`dout=EXT_G0/IO0`；`sclk=EXT_G5/IO5` |
| 复位 | U1 EN/CHIP_PU | `pullup=R7 100K`；`cap=C4 1uF`；`series_r=R8 0R`；`mcu_pin=EN/CHIP_PU pin3` |
| 保护电路 | J1/U4 | `series_r=R9/R10 22R`；`esd=D1/D2 ESD5311`；`input_protection=U4 AW32901FCR` |
| 保护电路 | CC1/CC2 | `cc1_r=R13 5.1K`；`cc2_r=R14 5.1K` |
| 保护电路 | S1/S2/S3 | `key2_esd=D3`；`key1_esd=D4`；`power_key_esd=D5` |
| 关键网络 | BST_EN | `source=IO46/16`；`destination=U11 pin4`；`pulldown=R27 10K` |
| 关键网络 | EPD_PWR | `source=U2 pin20`；`connector_pins=EPD1 7/12/23/38`；`load_network=R37 5.1K / C45 1uF` |
| 关键网络 | EXT_G0/PY_BOOT | `mcu_net=EXT_G0/IO0/pin27`；`pullup=R5 10K`；`cap=C3 NC`；`diode=D14`；`pmic_net=PY_BOOT` |
| 存储 | J2 | `miso=pin7`；`cs=pin2`；`sck=pin5`；`mosi=pin3`；`det=pin9`；`vdd=pin4 3V3_L2`；`vss=pin6/0 GND`；`series_resistors=R35/R36/R39/R40 NC` |
| 其他事实 | TP1-TP10 | `tp1=CHIP_PU`；`tp2=U0TXD_GPIO43`；`tp3=PY_BOOT`；`tp4=U0RXD_GPIO44`；`tp5=3V3_L2`；`tp6=GND`；`tp9=SYS_SCL`；`tp10=SYS_SDA` |
| 其他事实 | NC 标注 | `page2=C3`；`page3=R24/R43`；`page4=R35/R36/R39/R40` |

## 待确认事项

- `power.3v3-l2-feedback`：U5 的 FB Pin5 网络实际可见 R16 100K 与 R19 22K 分压并并联 C8 22pF，但旁注公式写为 Vout=0.6*(1+R18/R19)；R18 在 EN 网络中，无法据图确认公式所指电阻是否应改为 R16。（证据：图 8c6b37330dbe / 第 1 页 / 图3（B2-B3：R16/R18/R19、C8 与公式旁注））
- `power.epd-l4-role`：EPD 电源区可见 L4 WPN201610H4R7MT 与 U12 开关节点、D7 和地网络交叠，但当前图面无法无歧义重建 L4 的完整拓扑归属。（证据：图 8320646224ff / 第 1 页 / 图4（A2-B3：L4 与 U12 SW、D7、地线交叠区域））
- `nr-3v3-l2-feedback`：U5 的 3V3_L2 反馈分压上臂应标为 R16 还是公式旁注中的 R18？；原因：图面 FB 网络连接 R16/R19/C8，而公式写为 Vout=0.6*(1+R18/R19)，R18 同时在 EN 下拉网络。
- `nr-epd-l4-role`：L4 WPN201610H4R7MT 在 MT3608 正负压网络中的确切两端连接是什么？；原因：图面中 L4 与 U12 SW、D7、地线存在交叠，无法仅凭当前渲染页面无歧义重建拓扑。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `26546fd01aa3d3d1b6c8c3ea5ae9e67b587d8389139e7c30175c01ac1a7a209a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1288/K159-B_PaperDIY_sche_01.png` |
| 2 | 1 | `4d2aad0f2b997006efd2a918680860e34ec4358c1a24b87b9ba71fc272b6c938` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1288/K159-B_PaperDIY_sche_02.png` |
| 3 | 1 | `8c6b37330dbecf33735d3ef59370cc464705dd1c5a15e88f08939ec6015ff6c3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1288/K159-B_PaperDIY_sche_03.png` |
| 4 | 1 | `8320646224ff4b1f44899b04729039aa36be30bf0a7cf621a60c855ee2215ac5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1288/K159-B_PaperDIY_sche_04.png` |

---

源文档：`zh_CN/core/PaperDIY_Assembly_Kit.md`

源文档 SHA-256：`d71c2ba326f44002bbac11d6d483df2940b4ba624c23eb7a79bf1ea05a47e996`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
