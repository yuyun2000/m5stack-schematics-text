# Stamp-P4 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-P4 |
| SKU | S013 |
| 产品 ID | `stamp-p4-dc40121df2ce` |
| 源文档 | `zh_CN/core/Stamp-P4.md` |

## 概述

Stamp-P4 S013 单页原理图以 U5 ESP32-P4 为核心，外接 U2 XM25UH128DHIGT NOR Flash 和 40MHz 晶振；USB Type-C 输入经 AW32901FCR 保护，VIN 与 USB 两路经 CH213K 汇入 SYS_5V，再由两颗 SY8089AAAC 生成 SOC_3.3V 与 SOC_VHP。模组通过 65 个 Stamp 焊盘及独立 CAM、SDIO 连接器引出 MIPI DSI/CSI、USB、RMII、UART、I2C、ADC、JTAG 和 GPIO。

## 检索关键词

`Stamp-P4`、`S013`、`ESP32-P4`、`ESP32-P4NRW32`、`XM25UH128DHIGT`、`SY8089AAAC`、`AW32901FCR`、`CH213K`、`AXE516127D`、`HC-PBB40C-20DS-0.4V-2.5-02`、`MIPI DSI`、`MIPI CSI`、`SDIO`、`RMII`、`USB2_HOST_DP`、`USB2_HOST_DM`、`G24_USBC_D-`、`G25_USBC_D+`、`G26_USB1_D-`、`G27_USB1_D+`、`SYS_5V`、`SOC_3.3V`、`SOC_VHP`、`ESP_LDO1`、`CHIP_EN`、`LPG9_SCL`、`LPG11_SDA`、`G32_RMII_CLK`、`G36_RMII_MDIO`、`G35_BOOT_RMII_TXD1`、`G41_RMII_TXD0`、`G33_RMII_TXEN`、`G31_RMII_MDC`、`G28_RMII_RXDV`、`G30_RMII_RXD1`、`G29_RMII_RXD0`、`G52_RMII_RST`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-P4 | 主控 SoC，连接外部 Flash、USB、MIPI DSI/CSI、RMII、SDIO、UART、I2C、ADC、JTAG 与 GPIO | 图 d30ac61d359b / 第 1 页 / Core-ESP32_P4 区 A5-D6，U5 ESP32-P4 |
| U2 | XM25UH128DHIGT | ESP32-P4 外部 NOR Flash | 图 d30ac61d359b / 第 1 页 / FLASH 区 A3-A4，U2 XM25UH128DHIGT |
| U7 | AW32901FCR | USB_VBUS 到 5V_USB_IN 的输入过压和接口保护器件 | 图 d30ac61d359b / 第 1 页 / Interface Protection 区 A2，U7 AW32901FCR |
| U1,U6 | CH213K | VIN 与 5V_USB_IN 两路输入汇入 SYS_5V 的电源路径器件 | 图 d30ac61d359b / 第 1 页 / SYS_5V 区 A3，U1/U6 CH213K |
| U3 | SY8089AAAC | SYS_5V 到 SOC_3.3V 的 600mA DCDC | 图 d30ac61d359b / 第 1 页 / DCDC:3.3V_600mA 区 B1-B2，U3 SY8089AAAC |
| U4 | SY8089AAAC | SOC_3.3V 到 SOC_VHP 的 1.2V 500mA DCDC，由 VHP_DCDC_EN 控制 | 图 d30ac61d359b / 第 1 页 / DCDC:1.2V_500mA 区 B2，U4 SY8089AAAC |
| J1 | 未标注 | USB Type-C 电源与 G24/G25 USB 数据接口 | 图 d30ac61d359b / 第 1 页 / USB Input 区 A1-A2，J1 TYPEC |
| TVS1,TVS2 | ESD5311 | USB 输入与数据线 ESD 保护 | 图 d30ac61d359b / 第 1 页 / USB Input 区 A1-A2，TVS1/TVS2 ESD5311 |
| X1 | 40MHz crystal | ESP32-P4 主晶振 | 图 d30ac61d359b / 第 1 页 / Crystal 区 B3-B4，X1 40MHz |
| STAMP1 | STAMP_P4 | 65 焊盘邮票孔接口，引出电源、GPIO、USB、RMII、MIPI DSI、UART、I2C、ADC 与控制信号 | 图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 B1-D3，STAMP1/STAMP_P4 pins 1-65 |
| J2 | AXE516127D | 20-pin MIPI CSI 摄像头连接器，含双数据 lane、时钟 lane、I2C、电源、复位和 MCLK | 图 d30ac61d359b / 第 1 页 / CAM 区 B3-C4，J2 AXE516127D |
| J3 | HC-PBB40C-20DS-0.4V-2.5-02 | 20-pin SDIO 扩展连接器，另引出电源、I2C、ADC 和 GPIO | 图 d30ac61d359b / 第 1 页 / SDIO 区 D3-D4，J3 HC-PBB40C-20DS-0.4V-2.5-02 |

## 系统结构

### Stamp-P4 单页模组架构

U5 ESP32-P4 通过 U2 外部 NOR Flash 和 X1 40MHz 晶振构成核心，USB/VIN 输入汇入 SYS_5V 后产生 SOC_3.3V 与 SOC_VHP；STAMP1、J2 与 J3 分别引出通用 Stamp、MIPI CSI 和 SDIO 接口，并包含 MIPI DSI、USB 与 RMII 高速信号。

- 参数与网络：`schematic_page_count=1`；`module_sku=S013`
- 证据：图 d30ac61d359b / 第 1 页 / 整页 USB Input、Power、STAMP HOLE、CAM、SDIO 与 Core-ESP32_P4

## 电源

### USB Type-C 输入保护

J1 VBUS 形成 USB_VBUS，经 U7 AW32901FCR 输出 5V_USB_IN；U7 的 nEN 接地，R3 标 NC、R4 为 0R，输入输出两侧均有去耦。J1 CC1/CC2 分别通过 R1/R2 5.1K 接地。

- 参数与网络：`input=USB_VBUS`；`output=5V_USB_IN`；`cc_pulldown_ohm=5100`
- 证据：图 d30ac61d359b / 第 1 页 / USB Input 与 Interface Protection 区 A1-A2，J1/U7/R1-R4

### VIN 与 USB 输入汇入 SYS_5V

U1 CH213K 以 VIN 为输入，U6 CH213K 以 5V_USB_IN 为输入，两者 VO 输出并联到 SYS_5V；两路输入和共享输出均配置 22uF 去耦。

- 参数与网络：`input_a=VIN`；`input_b=5V_USB_IN`；`output=SYS_5V`
- 证据：图 d30ac61d359b / 第 1 页 / SYS_5V 区 A3，U1/U6 CH213K 与 C1/C2/C4

### SOC_3.3V 600mA DCDC

U3 SY8089AAAC 以 SYS_5V 为输入，经 L1 和反馈网络输出 SOC_3.3V；图区标题明确标注 DCDC:3.3V_600mA。

- 参数与网络：`input=SYS_5V`；`output=SOC_3.3V`；`output_voltage_v=3.3`；`rated_current_ma=600`
- 证据：图 d30ac61d359b / 第 1 页 / DCDC:3.3V_600mA 区 B1-B2，U3/L1/R6/R7

### SOC_VHP 1.2V 500mA DCDC

U4 SY8089AAAC 从 SOC_3.3V 取电，经 L12 输出 SOC_VHP，EN 由 VHP_DCDC_EN 控制；图区标题明确标注 DCDC:1.2V_500mA。

- 参数与网络：`input=SOC_3.3V`；`output=SOC_VHP`；`output_voltage_v=1.2`；`rated_current_ma=500`；`enable=VHP_DCDC_EN`
- 证据：图 d30ac61d359b / 第 1 页 / DCDC:1.2V_500mA 区 B2，U4/L12/VHP_DCDC_EN

### ESP32-P4 供电域与内部 LDO 网络

U5 的 VDDA、VDD3P3、VDDSPI、VDDPST 与相关 3.3V 电源脚接 SOC_3.3V，VDD_HP0/1/2/3 接 SOC_VHP；EN_DCDC 输出 VHP_DCDC_EN，VFB_DCDC 接 VHP_DCDC_DVFS。VFB1/VFB2/VFB3/VFB4 与外部去耦形成 ESP_LDO1/2/3 等内部 LDO 网络，外部 Flash VCC 接 ESP_LDO1。

- 参数与网络：`main_rail=SOC_3.3V`；`high_performance_rail=SOC_VHP`；`flash_rail=ESP_LDO1`
- 证据：图 d30ac61d359b / 第 1 页 / Core-ESP32_P4 区 A5-D6，U5 电源脚、VHP_DCDC_EN/DVFS 与 ESP_LDO1/2/3

## 接口

### Type-C USB 数据路径

J1 DN1/DN2 与 DP1/DP2 分别并接到 G24_USBC_D- 与 G25_USBC_D+，TVS2 ESD5311 提供接口侧保护；U5 的 GPIO24/USBP1_0- 与 GPIO25/USBP1_0+ 对应这组网络，图中标注 90Ω 阻抗匹配。

- 参数与网络：`dm=G24_USBC_D-`；`dp=G25_USBC_D+`；`differential_impedance_ohm=90`
- 证据：图 d30ac61d359b / 第 1 页 / USB Input 区 A1 与 Core-ESP32_P4 区 C5-C6，G24/G25 USBP1_0 差分对

### 额外 USB1 与 USB2 Host 差分对

STAMP1 pins17/19 引出 G27_USB1_D+ 与 G26_USB1_D-，pins40/41 引出 USB2_HOST_DP 与 USB2_HOST_DM；U5 图中两组差分路径均标注 90Ω 阻抗匹配。

- 参数与网络：`usb1_dp=G27_USB1_D+`；`usb1_dm=G26_USB1_D-`；`usb2_dp=USB2_HOST_DP`；`usb2_dm=USB2_HOST_DM`；`differential_impedance_ohm=90`
- 证据：图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 C1-D3 pins17/19/40/41；Core-ESP32_P4 区 C4-C6 USB 差分线

### 双 lane MIPI DSI

U5 引出 LCD_DSI_D0_P/N、LCD_DSI_CK_P/N 和 LCD_DSI_D1_P/N 三组差分对，图中标注 100Ω 阻抗匹配；三组网络分别连接 STAMP1 pins57/58、60/61、63/64，并以 pins56/59/62/65 的 GND 分隔。

- 参数与网络：`data_lanes=2`；`differential_impedance_ohm=100`
- 证据：图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 D2-D3 pins56-65 与 Core-ESP32_P4 区 B4-C5 LCD_DSI 差分对

### 双 lane MIPI CSI 摄像头接口

J2 AXE516127D 引出 CAM_CSI_D0_P/N、CAM_CSI_CK_P/N、CAM_CSI_D1_P/N，配套 G54_CAM_RST、G53_CAM_MCLK、LPG11_SDA、LPG9_SCL、SOC_3.3V 和多脚 GND；CSI 差分线在 U5 侧标注 90Ω 阻抗匹配。

- 参数与网络：`data_lanes=2`；`differential_impedance_ohm=90`；`connector=AXE516127D`
- 证据：图 d30ac61d359b / 第 1 页 / CAM 区 B3-C4，J2；Core-ESP32_P4 区 B4-C5 CAM_CSI 差分对

### 20-pin SDIO 扩展接口

J3 标注 HC-PBB40C-20DS-0.4V-2.5-02，连接 G40/G42/G43/G44/G45/G46/G47/G48、G51_ADC1、LPG9_SCL、LPG11_SDA，以及 SYS_5V、SOC_3.3V 和多脚 GND。

- 参数与网络：`connector_pins=20`；`connector=HC-PBB40C-20DS-0.4V-2.5-02`
- 证据：图 d30ac61d359b / 第 1 页 / SDIO 区 D3-D4，J3 pins1-20

### RMII 以太网信号组

STAMP1 引出 G32_RMII_CLK、G36_RMII_MDIO、G35_BOOT_RMII_TXD1、G41_RMII_TXD0、G33_RMII_TXEN、G31_RMII_MDC、G28_RMII_RXDV、G30_RMII_RXD1、G29_RMII_RXD0 与 G52_RMII_RST，覆盖 RMII 时钟、管理、收发与复位。

- 参数与网络：`clock=G32_RMII_CLK`；`mdio=G36_RMII_MDIO`；`mdc=G31_RMII_MDC`；`reset=G52_RMII_RST`
- 证据：图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 C2-D3 pins46-55 与 Core-ESP32_P4 区 A5-D6 对应 GPIO 网络

## 总线

### 低功耗 GPIO、I2C 与 UART

STAMP1 引出 LPG0-LPG15，其中 LPG9 标 SCL、LPG11 标 SDA，LPG14/LPG15 兼作 LPTXD_PCTXD 与 LPRXD_PCRXD；常规 UART0 使用 G37_U0TX 与 G38_U0RX。J2/J3 同时复用 LPG9_SCL 与 LPG11_SDA。

- 参数与网络：`i2c_scl=LPG9_SCL`；`i2c_sda=LPG11_SDA`；`uart0_tx=G37_U0TX`；`uart0_rx=G38_U0RX`
- 证据：图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 B1-C3，LPG0-15/G37/G38；CAM/SDIO 区 LPG9_SCL/LPG11_SDA

## 时钟

### ESP32-P4 40MHz 晶振

X1 标注 40MHz，XTALP/XTALN 分别经 R10/R11 0R 接入，C4/C5 各 15pF 对地。

- 参数与网络：`frequency_mhz=40`；`load_capacitor_pf=15`；`series_resistor_ohm=0`
- 证据：图 d30ac61d359b / 第 1 页 / Crystal 区 B3-B4，X1/R10/R11/C4/C5

## 复位

### CHIP_EN、Boot 与 RMII 配置上拉

CHIP_EN 由 R23 10K 上拉到 SOC_3.3V，并由 C21 1uF 对地；G35_BOOT_RMII_TXD1 由 R18 10K 上拉，G36_RMII_MDIO 由 R16 10K 上拉。STAMP1 还引出 G34_JTAG_ENABLE。

- 参数与网络：`chip_enable=CHIP_EN`；`boot_rmii_txd1=G35_BOOT_RMII_TXD1`；`jtag_enable=G34_JTAG_ENABLE`
- 证据：图 d30ac61d359b / 第 1 页 / Core-ESP32_P4 区 D6，R16/R18/R23/C21；STAMP HOLE 区 C2-C3，G34_JTAG_ENABLE/CHIP_EN

## 存储

### XM25UH128DHIGT 外部 Flash

U2 标注 XM25UH128DHIGT，CS#/SO/SCLK/SI/HOLD#/WP# 分别连接 FLASH_CS、FLASH_D0、FLASH_SCK、FLASH_D1、FLASH_HOLD、FLASH_WP，VCC 接 ESP_LDO1，R5 10K 上拉 FLASH_CS。

- 参数与网络：`part_number=XM25UH128DHIGT`；`supply=ESP_LDO1`
- 证据：图 d30ac61d359b / 第 1 页 / FLASH 区 A3-A4，U2、R5 与 FLASH_CS/D0/SCK/D1/HOLD/WP

## 模拟电路

### ADC 引出网络

STAMP1 引出 G16_ADC1 至 G23_ADC1 八路、G49_ADC2 与 G50_ADC2 两路；J3 SDIO 连接器另引出 G51_ADC1。

- 参数与网络：`adc1_stamp_range=G16-G23`；`adc2_stamp=G49,G50`；`adc1_sdio=G51`
- 证据：图 d30ac61d359b / 第 1 页 / STAMP HOLE 区 B1-C3，G16-G23_ADC1/G49-G50_ADC2；SDIO 区 G51_ADC1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-P4 单页模组架构 | `schematic_page_count=1`；`module_sku=S013` |
| 核心器件 | ESP32-P4 量产变体 | `schematic_label=ESP32-P4`；`documented_variant=ESP32-P4NRW32` |
| 电源 | USB Type-C 输入保护 | `input=USB_VBUS`；`output=5V_USB_IN`；`cc_pulldown_ohm=5100` |
| 保护电路 | USB 输入过压保护阈值 | `documented_threshold=>6V`；`protection_ic=AW32901FCR` |
| 电源 | VIN 与 USB 输入汇入 SYS_5V | `input_a=VIN`；`input_b=5V_USB_IN`；`output=SYS_5V` |
| 电源 | SOC_3.3V 600mA DCDC | `input=SYS_5V`；`output=SOC_3.3V`；`output_voltage_v=3.3`；`rated_current_ma=600` |
| 电源 | SOC_VHP 1.2V 500mA DCDC | `input=SOC_3.3V`；`output=SOC_VHP`；`output_voltage_v=1.2`；`rated_current_ma=500`；`enable=VHP_DCDC_EN` |
| 电源 | ESP32-P4 供电域与内部 LDO 网络 | `main_rail=SOC_3.3V`；`high_performance_rail=SOC_VHP`；`flash_rail=ESP_LDO1` |
| 存储 | XM25UH128DHIGT 外部 Flash | `part_number=XM25UH128DHIGT`；`supply=ESP_LDO1` |
| 存储 | 16MB Flash 容量 | `documented_capacity_mb=16`；`schematic_part_number=XM25UH128DHIGT` |
| 内存与 Flash | 32MB Octal PSRAM | `documented_capacity_mb=32`；`documented_interface=Octal` |
| 时钟 | ESP32-P4 40MHz 晶振 | `frequency_mhz=40`；`load_capacitor_pf=15`；`series_resistor_ohm=0` |
| 复位 | CHIP_EN、Boot 与 RMII 配置上拉 | `chip_enable=CHIP_EN`；`boot_rmii_txd1=G35_BOOT_RMII_TXD1`；`jtag_enable=G34_JTAG_ENABLE` |
| 接口 | Type-C USB 数据路径 | `dm=G24_USBC_D-`；`dp=G25_USBC_D+`；`differential_impedance_ohm=90` |
| 接口 | 额外 USB1 与 USB2 Host 差分对 | `usb1_dp=G27_USB1_D+`；`usb1_dm=G26_USB1_D-`；`usb2_dp=USB2_HOST_DP`；`usb2_dm=USB2_HOST_DM`；`differential_impedance_ohm=90` |
| 接口 | 双 lane MIPI DSI | `data_lanes=2`；`differential_impedance_ohm=100` |
| 接口 | 双 lane MIPI CSI 摄像头接口 | `data_lanes=2`；`differential_impedance_ohm=90`；`connector=AXE516127D` |
| 接口 | 20-pin SDIO 扩展接口 | `connector_pins=20`；`connector=HC-PBB40C-20DS-0.4V-2.5-02` |
| 核心器件 | CAM 与 SDIO 连接器数据手册对应关系 | `schematic_cam=AXE516127D`；`linked_cam_datasheet=AXE616124D`；`schematic_sdio=HC-PBB40C-20DS-0.4V-2.5-02`；`linked_sdio_datasheet=HC-PBB40C-20DP-0.4V-02` |
| 接口 | RMII 以太网信号组 | `clock=G32_RMII_CLK`；`mdio=G36_RMII_MDIO`；`mdc=G31_RMII_MDC`；`reset=G52_RMII_RST` |
| 总线 | 低功耗 GPIO、I2C 与 UART | `i2c_scl=LPG9_SCL`；`i2c_sda=LPG11_SDA`；`uart0_tx=G37_U0TX`；`uart0_rx=G38_U0RX` |
| 模拟电路 | ADC 引出网络 | `adc1_stamp_range=G16-G23`；`adc2_stamp=G49,G50`；`adc1_sdio=G51` |

## 待确认事项

- `component.soc-production-variant`：原理图 U5 仅标 ESP32-P4，正文称量产主控为 ESP32-P4NRW32；图面没有 NRW32 完整后缀、封装内存配置或芯片订购码，无法仅凭该页确认 exact variant。（证据：图 d30ac61d359b / 第 1 页 / Core-ESP32_P4 区 A5-D6，U5 仅标 ESP32-P4）
- `protection.documented-overvoltage-threshold`：正文称 AW32901FCR 支持大于 6V 输入电压保护；原理图只给 U7 型号和 USB_VBUS/5V_USB_IN 路径，没有阈值设定值或 OVP 电压标注。（证据：图 d30ac61d359b / 第 1 页 / Interface Protection 区 A2，U7 AW32901FCR，无 OVP 阈值标注）
- `storage.documented-flash-capacity`：正文称 Stamp-P4 配置 16MB Flash；原理图给出 U2 XM25UH128DHIGT 型号与连线，但没有单独标注 bit 或 byte 容量，容量换算需由器件 datasheet 或量产 BOM 确认。（证据：图 d30ac61d359b / 第 1 页 / FLASH 区 A3-A4，U2 XM25UH128DHIGT，未另标容量）
- `memory.documented-psram-capacity`：正文称主控配置 32MB Octal PSRAM；原理图 U5 只标 ESP32-P4，单页中没有独立 PSRAM、PSRAM 总线、容量字段或 NRW32 完整订购码，因此内存集成方式与容量需查量产 BOM 或 ESP32-P4NRW32 datasheet。（证据：图 d30ac61d359b / 第 1 页 / Core-ESP32_P4 区 A5-D6，U5 仅标 ESP32-P4，未画独立 PSRAM）
- `component.connector-datasheet-match`：原理图明确标 J2=AXE516127D、J3=HC-PBB40C-20DS-0.4V-2.5-02；正文数据手册链接名称分别为 AXE616124D 与 HC-PBB40C-20DP-0.4V-02，链接型号与图面型号不一致，不能直接视为量产连接器的对应 datasheet。（证据：图 d30ac61d359b / 第 1 页 / CAM 区 J2 AXE516127D 与 SDIO 区 J3 HC-PBB40C-20DS-0.4V-2.5-02）
- `review.soc-production-variant`：Stamp-P4 S013 量产主控的完整订购码是否为 ESP32-P4NRW32；原因：正文给出 ESP32-P4NRW32，但原理图 U5 仅标 ESP32-P4，没有完整变体后缀或封装配置。
- `review.overvoltage-threshold`：U7 AW32901FCR 的量产 USB 输入过压保护阈值是否为正文所述大于 6V；原因：图面未给 U7 的 OVP 阈值或外部设定值。
- `review.flash-capacity`：U2 XM25UH128DHIGT 对应的量产 Flash 容量是否为正文所述 16MB；原因：原理图给出完整器件型号和总线，但未单独写出容量。
- `review.psram-capacity`：Stamp-P4 的 PSRAM 是否集成于 ESP32-P4NRW32 且容量为 32MB Octal；原因：原理图没有完整 SoC 订购码、独立 PSRAM 或容量标注。
- `review.connector-datasheets`：J2/J3 的量产连接器 datasheet 应分别使用哪个 exact 型号；原因：原理图型号 AXE516127D 与 HC-PBB40C-20DS-0.4V-2.5-02，和正文数据手册链接名称 AXE616124D 与 HC-PBB40C-20DP-0.4V-02 不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d30ac61d359b55ad9a12c403da6dd9cfea3119f38ae06b8bd413b4b665bedcad` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/SCH_Stamp-P4_2026_03_16_17_23_06_page_01.png` |

---

源文档：`zh_CN/core/Stamp-P4.md`

源文档 SHA-256：`fd1201c8a0793fa71d8d278eadf4fb93753b29daa0fe7bf4f79c93ff7c45121f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
