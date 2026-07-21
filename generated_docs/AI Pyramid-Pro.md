# AI Pyramid-Pro 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AI Pyramid-Pro |
| SKU | AI-003-Pro |
| 产品 ID | `ai-pyramid-pro-0d03bb19c983` |
| 源文档 | `zh_CN/ai_hardware/AI_Pyramid-Pro.md` |

## 概述

AI Pyramid-Pro V0.2 原理图展开一套以 U1 AX650N/AX650C 标注 SoC 为核心的多板系统，配有 U15 STM32G431CBU6 EC、两颗 FLXW2004G-P1 LPDDR4、eMMC、microSD、双 M.2、双 RTL8211F 千兆网口与 GL3510 USB 3.0 Hub。Type-C PD 输入经 HUSB238 和 AW32901 后生成双 5V 母线、待机 3.3V，并通过 SY8003/JW5255/MAX77812 等形成 VDD_CORE、NNVDD、VDD_CPU、VDDR_1V1、VDDR_0V6、VDD_3V3、VDD_1V8 与扩展电源。系统提供 HDMI0/HDMI1、高速 USB/PCIe、双 Grove、风扇、RTC、SWD、按键/NeoPixel，以及 ES7210、ES8311、AW8737A 组成的四麦克风与扬声器音频链。正文称 SoC 为 AX8850、内存 8GB、eMMC 32GB 与 24 TOPS，但这些值与原理图标识存在冲突或未在器件页直接标注，需单独确认。

## 检索关键词

`AI Pyramid-Pro`、`AI-003-Pro`、`AX650N`、`AX650C`、`AX8850`、`STM32G431CBU6`、`HUSB238`、`AW32901`、`SY8368`、`MAX77812`、`INA3221`、`FLXW2004G-P1`、`LPDDR4`、`eMMC5.1`、`microSD`、`PI6C557-05`、`M.2 M-Key`、`RTL8211F-CG`、`GL3510`、`USB3.0`、`HDMI0`、`HDMI1`、`MS2131S`、`BM8563`、`ES7210`、`ES8311`、`0x18`、`AW8737A`、`VDD_CORE`、`NNVDD`、`VDD_CPU`、`VDDR_1V1`、`VDDR_0V6`、`VDD_3V3`、`VDD_1V8`、`VDD_EXT_5V`、`VSTB_3V3`、`EC_I2C_SCL`、`GROVE 2`、`GROVE 3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | AX650N / AX650C | 主 SoC，连接 LPDDR4、eMMC/SD、PCIe、双 RGMII、USB、HDMI、I2S 与系统控制信号 | 图 cc391a73f5c8 / 第 1 页 / 资源 5 第 1 页 AX650N Power/Ground Nets，U1; 图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 AX650C Sys/HDMI/USB/PCIe/Eth/SD/I2S blocks |
| U15 | STM32G431CBU6 | EC 协处理器，控制电源时序、风扇、按钮、Grove、PCIe/USB/显示电源并采集监测数据 | 图 ac95559493fa / 第 1 页 / 资源 3 第 1 页 EC MCU，U15 STM32G431CBU6 |
| U16,U17 | INA3221AIDGSR | 两颗三通道电源电压/电流监测器，通过 EC_I2C_SCL/SDA 连接 EC | 图 ac95559493fa / 第 1 页 / 资源 3 第 1 页 Power Sensor 1/2，U16/U17 INA3221 |
| U4 | HUSB238 | Type-C PD 协议控制器，通过 EC_I2C_SCL/SDA 与 EC 通信 | 图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 CC Protocol，U4 HUSB238 |
| U7 | AW32901 | Type-C 输入过压保护与 5A 高电流路径开关 | 图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 Input Protection，U7 AW32901 |
| U8,U9 | SY8368 | 分别生成 VDD_5V 与 VDD_EXT_5V 的主/辅助 5V Buck | 图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 Main 5V Buck 与 Aux 5V Buck，U8/U9 |
| U2A/U2B,U3A/U3B | MAX77812 | PMIC1/PMIC2 多相 Buck，生成 Core/NPU/CPU/DDR 低压电源轨 | 图 34ab6bdc81ab / 第 1 页 / 资源 4 第 1 页 PMIC1/PMIC2，MAX77812 U2A/U2B/U3A/U3B |
| U5,U6 | FLXW2004G-P1 | 两颗 LPDDR4 存储器，分别连接 AX650 DDR0/DDR1 控制器 | 图 2a0a507636e9 / 第 1 页 / 资源 7 第 1 页 LPDDR4 DRAM0，U5 FLXW2004G-P1; 图 927f50498059 / 第 1 页 / 资源 8 第 1 页 LPDDR4 DRAM1，U6 FLXW2004G-P1 |
| U21,U22 | MicroSD / EMMC_V5.1 | 可移除 microSD 与板载 eMMC 存储接口 | 图 ed6d3ba4bc0d / 第 1 页 / 资源 9 第 1 页 SDCard Slot U21 与 EMMC U22 |
| U23,X3 | PI6C557-05 / 25MHz | PCIe 参考时钟发生器与 25MHz 基准晶振 | 图 5362608ad7f4 / 第 1 页 / 资源 10 第 1 页 PCIe Clock Ref Source，U23 PI6C557-05、X3 25MHz |
| J1,J3 | M.2 NGFF M-Key | 两路 PCIe x4 M.2 M-Key 插槽，分别使用 PCIE0/PCIE1 | 图 5362608ad7f4 / 第 1 页 / 资源 10 第 1 页 NGFF M.2 M-Key Slot 1/2，J1/J3 |
| U24,U25 | JL2101-N040/RTL8211F-CG | 两颗 RGMII 千兆以太网 PHY，分别构成 ETH0/ETH1 | 图 d5a32b70abe2 / 第 1 页 / 资源 11 第 1 页 Gigabit Ethernet Phy 1/2，U24/U25 |
| U31,U28 | RJ45-GBE-MagJack-SMD | ETH0/ETH1 带磁性器件的 RJ45 千兆网口 | 图 d5a32b70abe2 / 第 1 页 / 资源 11 第 1 页 Gigabit Ethernet Port 1/2，U31/U28 |
| U36 | GL3510 | 一上行四下行 USB 3.0 Hub 控制器 | 图 7437df3f6ea7 / 第 1 页 / 资源 12 第 1 页 GL3510 USB3.0 Hub，U36A-U36G |
| J4,J5 | USB3.0_TypeA_SMD | GL3510 下行端口 DS1/DS2 的外部 USB 3.0 Type-A 接口 | 图 7437df3f6ea7 / 第 1 页 / 资源 12 第 1 页 DS Port 1/2，J4/J5 USB3.0 Type-A |
| J11,J15 | PH2.0-4P-SMD | Grove 2 I2C 与 Grove 3 UART 四针扩展接口 | 图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 GROVE 2/3，J11/J15 |
| U47 | BM8563 | 系统 RTC，连接 SYS_SCL/SYS_SDA 与 32.768kHz 晶振/备用电池 | 图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 Sys RTC，U47 BM8563、X5、BAT1 |
| U5,U7,U6 [audio board] | ES7210 / ES8311 / AW8737A | 四路麦克风 ADC、音频编解码器与扬声器功放 | 图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页 Audio，U5 ES7210、U7 ES8311、U6 AW8737A |
| S1 | SMT_SW_TACTILE | EC_BUTTON/PYM_BUTTON 双二极管汇入的用户按键 | 图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页按键区，S1 与 D1/D3 |
| U12,U11 | MS2131S / W25Qxx | HDMI/USB 桥接控制器及其 SPI Flash | 图 5d4ae556508a / 第 1 页 / 资源 16 第 1 页 HDMI Through，U12 MS2131S 与 U11 W25Qxx |

## 系统结构

### AI Pyramid-Pro 系统架构

原理图系统由 AX650N/AX650C SoC、STM32G431CBU6 EC、双 LPDDR4、eMMC/microSD、双 M.2、双以太网、USB 3.0 Hub、HDMI/USB 桥、RTC、音频/按键板和多路电源组成；EC 负责电源、风扇、按钮与扩展控制。

- 参数与网络：`soc=U1 AX650N/AX650C`；`ec=U15 STM32G431CBU6`；`memory=U5/U6 FLXW2004G-P1`；`storage=U21 microSD,U22 eMMC`；`pcie=J1/J3 M.2`；`ethernet=U24/U25,U31/U28`；`usb=U36 GL3510`；`audio=ES7210/ES8311/AW8737A`
- 证据：图 8ab27a9b3894 / 第 1 页 / 资源 1 第 1 页 Power Tree; 图 cc391a73f5c8 / 第 1 页 / 资源 5 第 1 页 SoC Power/Ground; 图 163a673ac43f / 第 1 页 / 资源 13 第 1 页系统连接器; 图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页按键/音频板

### STM32 EC 控制映射

U15 STM32G431CBU6 连接 FAN_TACO/FAN_PWM、PMIC1/2 CE/CS、SPI、AX UART、5V 电源使能、PCIe present/reset、NGFF1/2 电源、系统复位、Grove 电源、DS1/DS2/DS3 电源与高速开关、EC_BUTTON/EC_I2C/SYS SWD。

- 参数与网络：`fan=FAN_TACO,FAN_PWM`；`pmic=PMIC1_CE/CS,PMIC2_CE/CS`；`soc_uart=AX_UART3_RX/TX`；`m2=NGFF1_PWR_EN,NGFF2_PWR_EN`；`pcie=PCIE0/1_PRSNTN,GL_RESET_J`；`usb=DS1/DS2/DS3_PWR_EN,DS1/DS2_HS_EN`；`grove=PWR_GRV2_EN,PWR_GRV3_EN`；`buttons=EC_BUTTON,EC_BUTTON2`
- 证据：图 ac95559493fa / 第 1 页 / 资源 3 第 1 页 EC MCU U15 全部网络

## 核心器件

### 主 SoC 原理图标识

主芯片 U1 的电源/地页标为 AX650N，功能分块页标为 AX650C；DDR、eMMC、HDMI、USB、PCIe、RGMII 等均连接该 AX650 系列符号。

- 参数与网络：`reference=U1`；`power_symbol=AX650N`；`function_symbol=AX650C`；`interfaces=LPDDR4,eMMC,SD,HDMI,USB,PCIe,RGMII,I2S`
- 证据：图 cc391a73f5c8 / 第 1 页 / 资源 5 第 1 页 U1 AX650N; 图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 AX650C 各功能块

## 电源

### 系统电源树

Type-C PD 5V~20V 经 HUSB238 协议控制与 AW32901 OVP 后，分别进入 HV LDO 生成 VSTB_3V3、SY8368 生成 VDD_5V/VDD_EXT_5V；后级 MAX77812、SY8003、JW5255 与 ME1502 形成核心、CPU、NPU、DDR、M.2、USB 和扩展电源轨。

- 参数与网络：`input=Type-C PD 5V~20V`；`pd=HUSB238`；`ovp=AW32901`；`standby=VSTB_3V3`；`main_5v=VDD_5V`；`aux_5v=VDD_EXT_5V`；`core_rails=VDD_CORE,NNVDD,VDD_CPU,VDDR_1V1,VDDR_0V6,VDD_3V3,VDD_1V8`；`switched=USB1_5V,USB2_5V,USB3_5V,Extension Boards`
- 证据：图 8ab27a9b3894 / 第 1 页 / 资源 1 第 1 页完整 Power Tree

### Type-C PD 输入与保护

Type-C 电源连接器的 PD_CC1/PD_CC2 与 PD_USB_DP/DN 连接 U4 HUSB238，EC_I2C_SCL/SDA 接其 I2C；VIN_USB 经 U7 AW32901 OVP 形成 VIN_ISEN_P/VDD_VIN1/VDD_VIN2，AW32901 OVP 阈值网络标注 OVLO 24V、Ic max 5A。

- 参数与网络：`connector=Type-C PWR`；`pd_controller=U4 HUSB238`；`i2c=EC_I2C_SCL/SDA`；`protection=U7 AW32901`；`ovlo=24V`；`path_rating_mark=5A`；`outputs=VDD_VIN1,VDD_VIN2`
- 证据：图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 Type-C/CC Protocol/Input Protection

### 低压核心与扩展电源转换

U11/U12 SY8003 由 VDD_5V 生成 VDD_3V3/VDD_1V8；U13/U14 JW5255A 由 VDD_EXT_5V 生成 NGFF1_3V3/NGFF2_3V3；MAX77812 PMIC1 输出 VDD_CORE/NNVDD，PMIC2 输出 VDD_CPU/VDDR_1V1/VDDR_0V6。

- 参数与网络：`soc_3v3=U11 SY8003 -> VDD_3V3`；`soc_1v8=U12 SY8003 -> VDD_1V8`；`m2_1=U13 JW5255A -> NGFF1_3V3`；`m2_2=U14 JW5255A -> NGFF2_3V3`；`pmic1=MAX77812 -> VDD_CORE,NNVDD`；`pmic2=MAX77812 -> VDD_CPU,VDDR_1V1,VDDR_0V6`
- 证据：图 34ab6bdc81ab / 第 1 页 / 资源 4 第 1 页全部 DCDC/PMIC 分区

## 接口

### Grove 2 I2C 接口

J11 PH2.0-4P-SMD 提供 I2C3_SDA、I2C3_SCL、VDD_GRV2、GND；SDA/SCL 各串 47Ω并通过 2.2K 上拉到 VDD_3V3，配 PESD3V3S1BA-N ESD，U44 ME1502CM5G 由 PWR_GRV2_EN 控制 VDD_GRV2。

- 参数与网络：`connector=J11`；`signals=I2C3_SDA,I2C3_SCL`；`power=VDD_GRV2`；`series=R182/R184 47Ω`；`pullups=R181/R185 2.2K`；`switch=U44 ME1502CM5G`；`enable=PWR_GRV2_EN`
- 证据：图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 GROVE 2

### Grove 3 UART 接口

J15 PH2.0-4P-SMD 提供 THM_TXD、THM_RXD、VDD_GRV3、GND；TXD/RXD 各串 47Ω并配 10K 偏置与 ESD，U45 ME1502CM5G 由 PWR_GRV3_EN 控制 VDD_GRV3。THM UART 通过 U46 SN74AVC4T245RSV 在 3.3V/1.8V 间转换。

- 参数与网络：`connector=J15`；`signals=THM_TXD,THM_RXD`；`power=VDD_GRV3`；`series=R189/R191 47Ω`；`level_shifter=U46 SN74AVC4T245RSV`；`switch=U45 ME1502CM5G`；`enable=PWR_GRV3_EN`
- 证据：图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 UART Level Shifter 与 GROVE 3

### 双 HDMI 与 HDMI/USB 桥

AX650 引出 HDMI0/HDMI1 差分、HPD、CEC、SDA/SCL；J18 36针 FPC 汇总两路 HDMI。资源 16 的 U12 MS2131S、U13 视频开关及 TX/RX 连接器形成 HDMI Through/USB 桥接板，含 SPI Flash U11 与 ESD/共模器件。

- 参数与网络：`soc_ports=HDMI0,HDMI1`；`main_fpc=J18 36-pin`；`bridge=U12 MS2131S`；`switch=U13`；`flash=U11 W25Qxx`；`directions=TX and RX sections`；`protection=PESDALC10N5VU/common-mode chokes`
- 证据：图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 AX650 HDMI0/HDMI1; 图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 HDMI J18; 图 5d4ae556508a / 第 1 页 / 资源 16 第 1 页 HDMI Through TX/RX

### MIPI PHY RX 未使用

资源 14 标题明确为 MIPI Phy RX (Not Used)，AX650 RX0-RX3 全部 MIPI/ISP 差分引脚带未连接标记，仅 CSI_REXT 通过 R41 200Ω接 GND。

- 参数与网络：`block=MIPI PHY RX`；`status=Not Used`；`lanes=RX0,RX1,RX2,RX3 no connection`；`rext=R41 200Ω to GND`
- 证据：图 7ea351721983 / 第 1 页 / 资源 14 第 1 页 MIPI Phy RX (Not Used)

## 总线

### 双 PCIe x4 M.2 M-Key

J1 Slot1 连接 PCIE0_TX0-3/RX0-3、PCIE_REFCLK0、PCIE0_RSTN/PRSNTN/PEWAKE；J3 Slot2 连接 PCIE1_TX0-3/RX0-3、PCIE_REFCLK1、PCIE1_RSTN/PRSNTN/PEWAKE。两插槽各由独立 NGFF 3.3V Buck 供电。

- 参数与网络：`slot1=J1 PCIE0 x4,NGFF1_3V3`；`slot2=J3 PCIE1 x4,NGFF2_3V3`；`clock=PCIE_REFCLK0/1`；`control=RSTN,PRSNTN,PEWAKE`
- 证据：图 5362608ad7f4 / 第 1 页 / 资源 10 第 1 页 M.2 Slot1/Slot2; 图 34ab6bdc81ab / 第 1 页 / 资源 4 第 1 页 NGFF1/2 3V3 Buck

### 双 RGMII 千兆以太网

U24/U25 RTL8211F-CG PHY 分别连接 AX650 RGMII0/RGMII1 与 MDI 四对差分线，PHY0 地址绑带均标 3'b001；U31/U28 RJ45 MagJack 输出 ETH0/ETH1，MDI 线配有 PESD2ETH ESD。

- 参数与网络：`eth0=U24 RTL8211F-CG -> U31 RJ45`；`eth1=U25 RTL8211F-CG -> U28 RJ45`；`host_bus=RGMII0/RGMII1`；`phy_address=3'b001`；`protection=PESD2ETH`
- 证据：图 d5a32b70abe2 / 第 1 页 / 资源 11 第 1 页双 PHY 与双 RJ45

### GL3510 USB 3.0 Hub

U36 GL3510 连接一组 USB2/USB3 上行端口和 DS1-DS4 四组下行端口，使用 X4 25MHz；J4/J5 为 DS1/DS2 Type-A，DS3/DS4 经 J12/J16/扩展板继续引出，各端口配有独立 5V 负载开关和 ESD。

- 参数与网络：`hub=U36 GL3510`；`clock=X4 25MHz`；`upstream=USB2_D0,USB3 RX/TX`；`downstream=DS1,DS2,DS3,DS4`；`external_type_a=J4/J5`；`power_switches=ME1502CM5G`；`protection=PESD2ETH/PESDALC10N5VU`
- 证据：图 7437df3f6ea7 / 第 1 页 / 资源 12 第 1 页 GL3510 Hub/DS1-DS4; 图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 USB3/USB3 Dummy connectors; 图 5d4ae556508a / 第 1 页 / 资源 16 第 1 页 DS3/DS4 connectors and protection

## 总线地址

### ES8311 I2C 地址

音频板 U7 ES8311 旁明确标注 I2CADDR(7bit):0x18，CCLK/CDATA 连接 SYS_SCL/SYS_SDA。

- 参数与网络：`device=U7 ES8311`；`address_7bit=0x18`；`scl=SYS_SCL`；`sda=SYS_SDA`
- 证据：图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页 U7 ES8311，I2CADDR(7bit):0x18

## GPIO 与控制信号

### 用户按键与 NeoPixel 链

S1 通过 D1/D3 分别连接 EC_BUTTON/PYM_BUTTON，并由 R9/C8 形成上拉/滤波；NEOPIXEL_DRV 串接一排 WS2812 类器件，末端为 NP_DRV_00，各器件由 VDD_3V3 供电并配置 470nF 去耦。

- 参数与网络：`button=S1 SMT_SW_TACTILE`；`ec_signal=EC_BUTTON via D1 1N5819`；`soc_signal=PYM_BUTTON via D3 1N5819`；`led_input=NEOPIXEL_DRV`；`led_output=NP_DRV_00`；`supply=VDD_3V3`
- 证据：图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页按键与 NeoPixel 行

### 四针风扇接口

J6 风扇接口提供 FAN_TACO、FAN_PWM、GND、VDD_5V_F1；FAN_TACO/FAN_PWM 由 U15 EC 连接，二者在 EC 页配有 PESD3V3S1BA-N ESD。

- 参数与网络：`connector=J6 PH1.25-4P`；`pin4=FAN_TACO`；`pin3=FAN_PWM`；`pin2=GND`；`pin1=VDD_5V_F1`；`controller=U15 STM32G431CBU6`
- 证据：图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 FAN J6; 图 ac95559493fa / 第 1 页 / 资源 3 第 1 页 FAN_TACO/FAN_PWM 与 D16/D17

## 时钟

### SoC、RTC 与 PCIe 时钟

AX650 使用 X1 24MHz 与 X2 32.768kHz 晶振；U47 BM8563 RTC 使用 X5 32.768kHz 并连接 SYS_SCL/SDA、BAT1；PCIe 时钟 U23 PI6C557-05 使用 X3 25MHz，输出 PCIE_REFCLK0-3。

- 参数与网络：`soc_main=X1 24MHz`；`soc_lse=X2 32.768kHz`；`rtc=U47 BM8563,X5 32.768kHz`；`pcie=U23 PI6C557-05,X3 25MHz,REFCLK0-3`
- 证据：图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 AX650 clocks 与 Sys RTC; 图 5362608ad7f4 / 第 1 页 / 资源 10 第 1 页 PCIe Clock Ref Source

## 保护电路

### 高速接口与输入保护

Type-C 输入有 AW32901 OVP；双 RJ45 MDI 配 PESD2ETH；USB2/USB3 与 Grove 信号配 PESD/TVS；HDMI 差分与控制线配 ESD/共模器件。各 5V USB 下行端口使用 ME1502CM5G 独立限流负载开关。

- 参数与网络：`input_ovp=AW32901`；`ethernet_esd=PESD2ETH`；`usb_esd=PESD2ETH/PESDALC10N5VU`；`grove_esd=PESD3V3S1BA-N`；`hdmi_protection=ESD/common-mode chokes`；`usb_switch=ME1502CM5G`
- 证据：图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 AW32901; 图 d5a32b70abe2 / 第 1 页 / 资源 11 第 1 页 Ethernet ESD; 图 7437df3f6ea7 / 第 1 页 / 资源 12 第 1 页 USB ESD/load switches; 图 5d4ae556508a / 第 1 页 / 资源 16 第 1 页 HDMI/USB protection

## 存储

### eMMC 与 microSD 存储

U22 EMMC_V5.1 通过 EMMC_CLK/CMD/DAT0-DAT7/RST_N/DS 连接 AX650，U20 负载开关控制 VDD_EMMC；U21 MicroSD 通过 SDCARD_CLK/CMD/DAT0-DAT3/DET 连接 AX650，U19 SGM2578 控制 VDD_SDCARD，数据线配有上拉与 ESD。

- 参数与网络：`emmc=U22 EMMC_V5.1,8-bit data`；`emmc_power=U20 load switch VDD_EMMC`；`sd=U21 MicroSD,4-bit data`；`sd_power=U19 SGM2578 VDD_SDCARD`；`protection=SDCard ESD and pull-ups`；`capacity=null`
- 证据：图 ed6d3ba4bc0d / 第 1 页 / 资源 9 第 1 页 Storage 全部区域

## 内存与 Flash

### 双通道 LPDDR4

U5 与 U6 均标 FLXW2004G-P1，分别连接 AX650 DDR0 与 DDR1 的 CA/DQ/CK/DQS/RESET 网络；电源使用 VDDR_1V1、VDD_1V8、VDDR_0V6，并配置独立去耦。

- 参数与网络：`ddr0=U5 FLXW2004G-P1`；`ddr1=U6 FLXW2004G-P1`；`controllers=AX650 DDR0/DDR1`；`rails=VDDR_1V1,VDD_1V8,VDDR_0V6`；`capacity=null`
- 证据：图 2a0a507636e9 / 第 1 页 / 资源 7 第 1 页 LPDDR4 DRAM0; 图 927f50498059 / 第 1 页 / 资源 8 第 1 页 LPDDR4 DRAM1

## 音频

### 四麦克风与扬声器音频链

U5 ES7210 接 MIC1-MIC4 差分输入和 I2S0_MCLK/SCLK/LRCK/DIN0/DIN1；U7 ES8311 接 I2S0_MCLK/SCLK/LRCK/DOUT 与 AUD_OUT_P/N；AUD_OUT 经 U6 AW8737A 放大到 J3 SPK_VOP/SPK_VON。

- 参数与网络：`mic_adc=U5 ES7210`；`microphones=MIC1,MIC2,MIC3,MIC4`；`codec=U7 ES8311`；`i2s=I2S0_MCLK,SCLK,LRCK,DIN0,DIN1,DOUT`；`amplifier=U6 AW8737A`；`speaker=J3 SPK_VOP/SPK_VON`
- 证据：图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页完整 Audio 区

## 传感器

### 双 INA3221 电源监测

U16/U17 INA3221 共用 EC_I2C_SCL/SDA；U16 监测 VUSB_DS1、NGFF2_3V3、VDD_VIN1，U17 监测 VDD_VIN2、NGFF1_3V3、VUSB_DS2，A0 均接 GND。

- 参数与网络：`bus=EC_I2C_SCL/SDA`；`monitor1=VUSB_DS1,NGFF2_3V3,VDD_VIN1`；`monitor2=VDD_VIN2,NGFF1_3V3,VUSB_DS2`；`address_strap=A0 GND`；`numeric_address=null`
- 证据：图 ac95559493fa / 第 1 页 / 资源 3 第 1 页 Power Sensor 1/2

## 调试与烧录

### EC 调试与扩展接口

J7 引出 EC_RST、SYS_SWDIO、SYS_SWCLK、GND、VSTB_3V3；J9 12针 EC Extension 引出 USB2_D1、SYS_SCL/SDA/INT、EC_I2C_SCL/SDA、EC_BUTTON2、VSTB_3V3、VDD_5V。

- 参数与网络：`debug=J7 EC_RST,SYS_SWDIO,SYS_SWCLK,GND,VSTB_3V3`；`extension=J9 USB2_D1,SYS I2C,EC I2C,button,power`
- 证据：图 163a673ac43f / 第 1 页 / 资源 13 第 1 页 EC Debug 与 EC Extension

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AI Pyramid-Pro 系统架构 | `soc=U1 AX650N/AX650C`；`ec=U15 STM32G431CBU6`；`memory=U5/U6 FLXW2004G-P1`；`storage=U21 microSD,U22 eMMC`；`pcie=J1/J3 M.2`；`ethernet=U24/U25,U31/U28`；`usb=U36 GL3510`；`audio=ES7210/ES8311/AW8737A` |
| 电源 | 系统电源树 | `input=Type-C PD 5V~20V`；`pd=HUSB238`；`ovp=AW32901`；`standby=VSTB_3V3`；`main_5v=VDD_5V`；`aux_5v=VDD_EXT_5V`；`core_rails=VDD_CORE,NNVDD,VDD_CPU,VDDR_1V1,VDDR_0V6,VDD_3V3,VDD_1V8`；`switched=USB1_5V,USB2_5V,USB3_5V,Extension Boards` |
| 电源 | Type-C PD 输入与保护 | `connector=Type-C PWR`；`pd_controller=U4 HUSB238`；`i2c=EC_I2C_SCL/SDA`；`protection=U7 AW32901`；`ovlo=24V`；`path_rating_mark=5A`；`outputs=VDD_VIN1,VDD_VIN2` |
| 电源 | 低压核心与扩展电源转换 | `soc_3v3=U11 SY8003 -> VDD_3V3`；`soc_1v8=U12 SY8003 -> VDD_1V8`；`m2_1=U13 JW5255A -> NGFF1_3V3`；`m2_2=U14 JW5255A -> NGFF2_3V3`；`pmic1=MAX77812 -> VDD_CORE,NNVDD`；`pmic2=MAX77812 -> VDD_CPU,VDDR_1V1,VDDR_0V6` |
| 系统结构 | STM32 EC 控制映射 | `fan=FAN_TACO,FAN_PWM`；`pmic=PMIC1_CE/CS,PMIC2_CE/CS`；`soc_uart=AX_UART3_RX/TX`；`m2=NGFF1_PWR_EN,NGFF2_PWR_EN`；`pcie=PCIE0/1_PRSNTN,GL_RESET_J`；`usb=DS1/DS2/DS3_PWR_EN,DS1/DS2_HS_EN`；`grove=PWR_GRV2_EN,PWR_GRV3_EN`；`buttons=EC_BUTTON,EC_BUTTON2` |
| 传感器 | 双 INA3221 电源监测 | `bus=EC_I2C_SCL/SDA`；`monitor1=VUSB_DS1,NGFF2_3V3,VDD_VIN1`；`monitor2=VDD_VIN2,NGFF1_3V3,VUSB_DS2`；`address_strap=A0 GND`；`numeric_address=null` |
| 核心器件 | 主 SoC 原理图标识 | `reference=U1`；`power_symbol=AX650N`；`function_symbol=AX650C`；`interfaces=LPDDR4,eMMC,SD,HDMI,USB,PCIe,RGMII,I2S` |
| 内存与 Flash | 双通道 LPDDR4 | `ddr0=U5 FLXW2004G-P1`；`ddr1=U6 FLXW2004G-P1`；`controllers=AX650 DDR0/DDR1`；`rails=VDDR_1V1,VDD_1V8,VDDR_0V6`；`capacity=null` |
| 存储 | eMMC 与 microSD 存储 | `emmc=U22 EMMC_V5.1,8-bit data`；`emmc_power=U20 load switch VDD_EMMC`；`sd=U21 MicroSD,4-bit data`；`sd_power=U19 SGM2578 VDD_SDCARD`；`protection=SDCard ESD and pull-ups`；`capacity=null` |
| 时钟 | SoC、RTC 与 PCIe 时钟 | `soc_main=X1 24MHz`；`soc_lse=X2 32.768kHz`；`rtc=U47 BM8563,X5 32.768kHz`；`pcie=U23 PI6C557-05,X3 25MHz,REFCLK0-3` |
| 总线 | 双 PCIe x4 M.2 M-Key | `slot1=J1 PCIE0 x4,NGFF1_3V3`；`slot2=J3 PCIE1 x4,NGFF2_3V3`；`clock=PCIE_REFCLK0/1`；`control=RSTN,PRSNTN,PEWAKE` |
| 总线 | 双 RGMII 千兆以太网 | `eth0=U24 RTL8211F-CG -> U31 RJ45`；`eth1=U25 RTL8211F-CG -> U28 RJ45`；`host_bus=RGMII0/RGMII1`；`phy_address=3'b001`；`protection=PESD2ETH` |
| 总线 | GL3510 USB 3.0 Hub | `hub=U36 GL3510`；`clock=X4 25MHz`；`upstream=USB2_D0,USB3 RX/TX`；`downstream=DS1,DS2,DS3,DS4`；`external_type_a=J4/J5`；`power_switches=ME1502CM5G`；`protection=PESD2ETH/PESDALC10N5VU` |
| 接口 | Grove 2 I2C 接口 | `connector=J11`；`signals=I2C3_SDA,I2C3_SCL`；`power=VDD_GRV2`；`series=R182/R184 47Ω`；`pullups=R181/R185 2.2K`；`switch=U44 ME1502CM5G`；`enable=PWR_GRV2_EN` |
| 接口 | Grove 3 UART 接口 | `connector=J15`；`signals=THM_TXD,THM_RXD`；`power=VDD_GRV3`；`series=R189/R191 47Ω`；`level_shifter=U46 SN74AVC4T245RSV`；`switch=U45 ME1502CM5G`；`enable=PWR_GRV3_EN` |
| 接口 | 双 HDMI 与 HDMI/USB 桥 | `soc_ports=HDMI0,HDMI1`；`main_fpc=J18 36-pin`；`bridge=U12 MS2131S`；`switch=U13`；`flash=U11 W25Qxx`；`directions=TX and RX sections`；`protection=PESDALC10N5VU/common-mode chokes` |
| 总线地址 | ES8311 I2C 地址 | `device=U7 ES8311`；`address_7bit=0x18`；`scl=SYS_SCL`；`sda=SYS_SDA` |
| 音频 | 四麦克风与扬声器音频链 | `mic_adc=U5 ES7210`；`microphones=MIC1,MIC2,MIC3,MIC4`；`codec=U7 ES8311`；`i2s=I2S0_MCLK,SCLK,LRCK,DIN0,DIN1,DOUT`；`amplifier=U6 AW8737A`；`speaker=J3 SPK_VOP/SPK_VON` |
| GPIO 与控制信号 | 用户按键与 NeoPixel 链 | `button=S1 SMT_SW_TACTILE`；`ec_signal=EC_BUTTON via D1 1N5819`；`soc_signal=PYM_BUTTON via D3 1N5819`；`led_input=NEOPIXEL_DRV`；`led_output=NP_DRV_00`；`supply=VDD_3V3` |
| GPIO 与控制信号 | 四针风扇接口 | `connector=J6 PH1.25-4P`；`pin4=FAN_TACO`；`pin3=FAN_PWM`；`pin2=GND`；`pin1=VDD_5V_F1`；`controller=U15 STM32G431CBU6` |
| 调试与烧录 | EC 调试与扩展接口 | `debug=J7 EC_RST,SYS_SWDIO,SYS_SWCLK,GND,VSTB_3V3`；`extension=J9 USB2_D1,SYS I2C,EC I2C,button,power` |
| 接口 | MIPI PHY RX 未使用 | `block=MIPI PHY RX`；`status=Not Used`；`lanes=RX0,RX1,RX2,RX3 no connection`；`rext=R41 200Ω to GND` |
| 保护电路 | 高速接口与输入保护 | `input_ovp=AW32901`；`ethernet_esd=PESD2ETH`；`usb_esd=PESD2ETH/PESDALC10N5VU`；`grove_esd=PESD3V3S1BA-N`；`hdmi_protection=ESD/common-mode chokes`；`usb_switch=ME1502CM5G` |
| 核心器件 | 正文 AX8850 与原理图 AX650 标识冲突 | `documented_soc=Axera AX8850`；`schematic_soc=AX650N/AX650C`；`bom_confirmation=null` |
| 内存与 Flash | LPDDR4 容量与速率 | `documented_capacity=8GB (4+4)`；`documented_type=LPDDR4x`；`documented_width=64-bit`；`documented_rate=4266Mbps`；`schematic_parts=U5/U6 FLXW2004G-P1`；`schematic_capacity=null` |
| 存储 | eMMC 容量 | `documented_standard=eMMC5.1`；`documented_capacity=32GB`；`reference=U22`；`part_number=null`；`schematic_capacity=null` |
| 系统结构 | CPU/NPU 与视频性能 | `documented_cpu=8x Cortex-A55 1.7GHz`；`documented_npu=24 TOPS INT8`；`documented_video=8K30 H.264/H.265,16x1080p decode`；`schematic_performance=null` |
| 电源 | PD 100W 与整机供电要求 | `documented_protocol=USB PD3.0`；`documented_max=100W`；`documented_profiles=9V,12V,20V`；`documented_minimum=>9V@3A`；`schematic_input=5V~20V`；`pdo_table=null` |
| GPIO 与控制信号 | RGB LED 数量 | `documented_count=48`；`input=NEOPIXEL_DRV`；`output=NP_DRV_00`；`schematic_count=null`；`part_number=null` |

## 待确认事项

- `component.soc-conflict`：产品正文称 SoC 为 Axera AX8850；16 页原理图的主 SoC 电源页和功能页反复标为 AX650N/AX650C，没有出现 AX8850 器件标识。（证据：图 cc391a73f5c8 / 第 1 页 / 资源 5 第 1 页 U1 AX650N; 图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 AX650C 各功能块）
- `memory.documented-capacity`：正文称 8GB（4+4）、64-bit LPDDR4x、4266Mbps；原理图确认两颗 FLXW2004G-P1 与 DDR0/DDR1 总线，但未直接标注单颗/总容量、LPDDR4x、总线宽度汇总或运行速率。（证据：图 2a0a507636e9 / 第 1 页 / 资源 7 第 1 页 U5 LPDDR4; 图 927f50498059 / 第 1 页 / 资源 8 第 1 页 U6 LPDDR4）
- `storage.documented-emmc-capacity`：正文称 eMMC5.1 容量 32GB；原理图只将 U22 标为 EMMC_V5.1，没有具体料号或容量。（证据：图 ed6d3ba4bc0d / 第 1 页 / 资源 9 第 1 页 U22 EMMC_V5.1）
- `system.documented-performance`：正文称八核 Cortex-A55 1.7GHz、24 TOPS@INT8、8K H.264/H.265 与 16路 1080p；原理图只展示 AX650N/AX650C 连接与供电，没有 CPU 核数/频率、NPU TOPS 或编解码吞吐参数。（证据：图 cc391a73f5c8 / 第 1 页 / 资源 5 第 1 页 SoC power only; 图 7b76986f4203 / 第 1 页 / 资源 6 第 1 页 SoC interfaces only）
- `power.documented-pd-rating`：正文称 USB PD3.0 100W、支持 9V/12V/20V并要求大于9V@3A；原理图框图标 Type-C PD Input 5V~20V、AW32901 5A，未标 PD3.0、100W PDO 表或整机 27W 最低要求。（证据：图 8ab27a9b3894 / 第 1 页 / 资源 1 第 1 页 Type-C PD Input 5V~20V; 图 c81ac592f3be / 第 1 页 / 资源 2 第 1 页 HUSB238/AW32901，无 PDO/100W 表）
- `gpio.documented-rgb-count`：正文称 48 x RGB LED；按键板原理图显示 NEOPIXEL_DRV 到 NP_DRV_00 的串行器件链，但器件符号未逐个给出清晰位号/型号，无法从页内可靠确认总数为 48。（证据：图 bb5881ae854e / 第 1 页 / 资源 15 第 1 页 NeoPixel 串行器件行）
- `review.soc`：请用当前量产 BOM、芯片丝印或正式 AX8850 原理图确认 AI Pyramid-Pro 实际 SoC；现有 V0.2 图反复标 AX650N/AX650C。；原因：正文与原理图主芯片型号直接冲突。
- `review.memory`：请依据 FLXW2004G-P1 datasheet、BOM 或系统检测确认双 LPDDR4 的总容量、LPDDR4x 类型、64-bit 宽度和 4266Mbps 速率。；原因：原理图只给出两颗料号与 DDR0/DDR1 连接。
- `review.emmc`：请用 U22 量产料号或系统容量查询确认 eMMC5.1 为 32GB。；原因：原理图未标 U22 具体料号和容量。
- `review.performance`：请基于实际 SoC datasheet、固件和性能测试确认 CPU/NPU/视频指标。；原因：原理图不包含计算和编解码性能参数，且 SoC 型号冲突。
- `review.pd-rating`：请用 HUSB238 配置/PDO、PD 固件与整机测试确认 PD3.0、100W、9/12/20V 档位和最低 9V@3A 要求。；原因：原理图只显示 5V~20V 输入与 5A 保护路径。
- `review.rgb-count`：请用按键/RGB 板 BOM 或实物确认串行 RGB LED 总数为 48及具体型号。；原因：原理图器件行未提供可可靠计数的清晰位号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8ab27a9b389416d7d0781f6b719f93b66841f6ac47c94ec90f9a84479f0b2b67` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_01.png` |
| 2 | 1 | `c81ac592f3be019b7c56f7b09032f4fc12ee84e8a7f130f9db72677ee6ea458a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_02.png` |
| 3 | 1 | `ac95559493fa274dfae5141980241ba108f8aee180413ff4ab99243879e05b9d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_03.png` |
| 4 | 1 | `34ab6bdc81ab566d13af6a93b908bc103b825271212c37a9e00e47962c6cbaa4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_04.png` |
| 5 | 1 | `cc391a73f5c8216c17363881f1072ad7d8d9bb998309140ddddc85d330580ccc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_05.png` |
| 6 | 1 | `7b76986f4203b27321562b629358f691ccee4737c5a94732d89942c60c8526e5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_06.png` |
| 7 | 1 | `2a0a507636e968ca913843affcad96ba004f690a8fea145531f9c22411bbf877` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_07.png` |
| 8 | 1 | `927f504980596ab392662ee4eb1dbea6e55073a992cb031739478c5312966210` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_08.png` |
| 9 | 1 | `ed6d3ba4bc0dd85256d4594d9672db48a06a92776da54d304082697e372e1f22` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_09.png` |
| 10 | 1 | `5362608ad7f425bbfbc4b0445ac30d21225eb7b8626658b42314c822d5dbd052` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_10.png` |
| 11 | 1 | `d5a32b70abe240265f5f6c7097551677b1047e0917314bbae66bee992a4b07cb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_11.png` |
| 12 | 1 | `7437df3f6ea746948b1d0ba7243e8339086383eb834b25b555938655982d1ac4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_12.png` |
| 13 | 1 | `163a673ac43f27124de7d43bb2bb8cfed2362df1cdb98a8e19f35c3299bbecfb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_13.png` |
| 14 | 1 | `7ea3517219831b4f17554909eb03e2768f8651b302e29fba0c592b0c8d859690` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_14.png` |
| 15 | 1 | `bb5881ae854e765af3e1f9e59952fd18caff91fb85f7936cfb6017fff91098cf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/AI-003-AI_Pyramid_PCB_KEY_V0.2_2026_01_30_16_52_44_page_01.png` |
| 16 | 1 | `5d4ae556508a8bc2c6017f47a8299a77360474cdda485cedf5aaa7b7192c148a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1216/M5_AI_Pyramid-Pro_PCB_HDMI_THROUGH_page_01.png` |

---

源文档：`zh_CN/ai_hardware/AI_Pyramid-Pro.md`

源文档 SHA-256：`654f5069777ae50cd92cd60f88a493bb110e5d9694607daffb3ca081ca31e814`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
