# Module LLM Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LLM Kit |
| SKU | K144 |
| 产品 ID | `module-llm-kit-6dad0f809655` |
| 源文档 | `zh_CN/module/Module LLM Kit.md` |

## 概述

Module LLM Kit 由 M140 Module LLM 主模块与 K144 Module13.2 LLM Mate 组成。主模块以 U1 AX630C 为核心，配有 LPDDR4 与 eMMC 5.1 总线、microSD、五路主要电源、24MHz/32.768kHz 时钟、模拟 MEMS 麦克风、AW8737A 功放、USB-C/OTG 硬件、LP5562 三 RGB、M5-Bus、调试 UART 和片上以太网 PHY/FPC；Mate 通过 USB-C 与 CH340N 提供串口，FPC-8P 承载串口和以太网差分对，11FB-05NL 与 RJ45 构成网络口。图面未直接标注 4GB/32GB、NPU 算力、百兆速率、整机功耗和软件模型能力，均保留为待确认。

## 检索关键词

`Module LLM Kit`、`K144`、`M140`、`Module13.2 LLM Mate`、`AX630C`、`Dual Cortex-A53`、`3.2 TOPS INT8`、`12.8 TOPS INT4`、`LPDDR4`、`4GB`、`eMMC 5.1`、`32GB`、`microSD`、`AW32901`、`SY8089A1AAA`、`JW5255A`、`LP5907MFX-1.8`、`MSM421A3729H9KRMC`、`AW8737A`、`LP5562`、`SGM7220`、`SGM2578`、`CH340N`、`11FB-05NL`、`RJ45`、`FPC-8P`、`M5Stack_BUS`、`USB OTG`、`DBG_TXD`、`DBG_RXD`、`TRM_TXD`、`TRM_RXD`、`BUS_SCL`、`BUS_SDA`、`SYS_SCL`、`SYS_SDA`、`VDD_5V`、`VDD_3V3`、`VDD_1V8`、`VDDR_1V1`、`VCORE_0V8`、`AVDD_1V8`、`24MHz`、`32.768kHz`、`StackFlow`、`Ubuntu`、`KWS`、`ASR`、`TTS`、`115200 8N1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1A-U1O | AX630C | Module LLM 主 SoC，连接电源、LPDDR4、eMMC、SD、音频、USB、UART、I2C 和以太网 PHY | 图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 U1A/U1L AX630C 电源与接地单元; 图 d660230e4d50 / 第 1 页 / 主模块第 3 页 U1B/U1E/U1O AX630C 启动、IO 与 USB 单元 |
| U2 | AW32901 | VIN_5V 到 VDD_5V 的输入保护开关 | 图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 A5-A7，U2 AW32901、VIN_5V/VDD_5V 与 OVLO 分压 |
| U3/U4/U6 | SY8089A1AAA | VDD_5V 到 VDD_3V3、VDD_1V8 与 VDDR_1V1 的三路降压转换器 | 图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 B3-C6，U3/U4/U6 SY8089A1AAA 与 L1-L3 |
| U5/U7 | LP5907MFX-1.8/NOPB / JW5255A | AVDD_1V8 低噪声 LDO 与 VCORE_0V8 降压转换器 | 图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 C6-D7，U5 LP5907 与 U7 JW5255A |
| U8A/U8B/U8C | LPDDR4 | AX630C 外部 LPDDR4 存储器 | 图 a26d069d6b4e / 第 1 页 / 主模块第 4 页 A4-C8，U8A/U8B/U8C LPDDR4 与 DDR_CA/DQ/DQS/CLK |
| U9/U10/U11 | WL2811EA-5/TR / MicroSD / EMMC_V5.1 | microSD 供电与卡座、eMMC 5.1 存储接口 | 图 b3098cc77650 / 第 1 页 / 主模块第 5 页 A1-D6，U9/U10/U11 SD 与 eMMC 电路 |
| U12 | MSM421A3729H9KRMC | 连接 AX630C AUDIO_IN_P/N 的模拟 MEMS 麦克风 | 图 00b1d013437d / 第 1 页 / 主模块第 6 页 B1-B4，U12 麦克风与 AUDIO_IN_P/N |
| U13 | AW8737A | VDD_5V 供电的差分扬声器功放 | 图 00b1d013437d / 第 1 页 / 主模块第 6 页 C2-D5，U13 AW8737A 与 SPK_VOP/SPK_VON |
| J1/U14/U15/L5 | USB-C / SGM7220 / SRV05-4 / SDMM0806H-2-900T | 主模块 USB-C、CC/ID 控制、ESD 与差分共模滤波 | 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 A1-A4，J1/U14/U15/L5 USB 电路 |
| U16/FET4 | SGM2578 / 2N7002 | USB_ID 控制的 VIN_5V 到 VUSB_5V 电源路径 | 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 A4-A6，U16 SGM2578、FET4、D9 与 VUSB_5V |
| U20/U18/U21/U22 | LP5562 / LED-2020-RGB | SYS I2C 控制的三颗 RGB 指示灯 | 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 C2-C4，U20 LP5562 与 U18/U21/U22 RGB |
| X1/Y1 | 24MHz / 32.768kHz | AX630C 主晶振与低速晶振 | 图 d660230e4d50 / 第 1 页 / 主模块第 3 页 B5-B7，X1 24MHz 与 Y1 32.768kHz |
| J2（主模块） | FPC-SMD_8P-P0.50 | 向 Mate 引出 EPHY_TX/RX 与 DBG_RXD/TXD | 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 B1-B2，J2 8P FPC |
| J4 | MBUS_Core2 | Module LLM 30-pin M5-Bus 与 UART Net-Tie 接口 | 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 D1-D4，J4 MBUS_Core2 与 Tie1-Tie8 |
| USB1/U1（Mate） | TYPEC-304S-ACP16 / CH340N | Mate USB-C 到 UART 转换 | 图 96d376b6efb7 / 第 1 页 / Mate 页 A1-B3，USB1、F1、U1 CH340N 与 J2 |
| J2（Mate） | HDGC/0.5K-HX-8PWB/NC | Mate 的 8P 串口与以太网差分 FPC | 图 96d376b6efb7 / 第 1 页 / Mate 页 A3-A4，J2 8P、RXP/RXN/TXP/TXN 与 CH340N 串口 |
| J5/T1（Mate） | HC-RJ45-053-5 / 11FB-05NL | Mate RJ45 与板载网络变压器 | 图 96d376b6efb7 / 第 1 页 / Mate 页 C1-D3，J5 RJ45、T1 11FB-05NL 与 TX/RX 差分对 |
| J3/J4（Mate） | M5Stack_BUS | Mate 30-pin 堆叠供电和 GPIO/I2C 接口 | 图 96d376b6efb7 / 第 1 页 / Mate 页 C3-D4，J3/J4 M5Stack_BUS |

## 系统结构

### Module LLM Kit 双模块架构

Kit 资源由九页 M140 Module LLM 与一页 K144 Module13.2 LLM Mate 组成；主模块包含 AX630C、内存/存储、电源、音频、USB、RGB、M5-Bus 与 EPHY，Mate 包含 USB-C/CH340N、FPC-8P、RJ45/网络变压器和 M5Stack_BUS。

- 参数与网络：`main=M140 Module LLM`；`mate=K144 Module13.2 LLM Mate`；`main_pages=9`；`mate_pages=1`；`interconnect=FPC-8P + M5-Bus`
- 证据：图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 AX630C 与电源; 图 96d376b6efb7 / 第 1 页 / Mate 完整单页 USB-UART、FPC、RJ45 与 M5-Bus

### AX630C 主 SoC

U1A-U1O 的器件值均属于 AX630C，多单元分别展开电源/接地、启动与通用 IO、LPDDR4、eMMC/SD、音频、USB、MIPI/DVP、RGMII 与片上 EPHY 接口。

- 参数与网络：`reference=U1A-U1O`；`part_number=AX630C`；`memory=LPDDR4`；`storage=eMMC5.1,microSD`；`interfaces=USB,UART,I2C,EPHY,MIPI,DVP,SDIO,audio`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 U1B/U1E/U1O; 图 141a3b26d17b / 第 1 页 / 主模块第 9 页 U1J/U1K EPHY/RGMII

## 电源

### AX630C 多路电源树

VDD_5V 经 U3/U4/U6 三颗 SY8089A1AAA 与 L1/L2/L3 生成 VDD_3V3、VDD_1V8、VDDR_1V1；U5 LP5907MFX-1.8/NOPB 生成 AVDD_1V8；U7 JW5255A 与 L4 生成 VCORE_0V8。

- 参数与网络：`input=VDD_5V`；`vdd_3v3=U3 SY8089A1AAA`；`vdd_1v8=U4 SY8089A1AAA`；`vddr_1v1=U6 SY8089A1AAA`；`avdd_1v8=U5 LP5907MFX-1.8/NOPB`；`vcore_0v8=U7 JW5255A`
- 证据：图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 B3-D8，U3-U7 与五路输出

### microSD 电源与 IO 电压

U9 WL2811EA-5/TR 从 VDD_5V 生成 VDDIO_SDCARD，SD_PWR_SW 连接其调整网络；FET3 CJ2301 从 VDD_3V3 生成 VDD_SDCARD，VT1 PMBT3904 受 SD_PWR_EN 控制。

- 参数与网络：`io_regulator=U9 WL2811EA-5/TR`；`io_input=VDD_5V`；`io_output=VDDIO_SDCARD`；`card_switch=FET3 CJ2301`；`card_input=VDD_3V3`；`card_output=VDD_SDCARD`；`enable=SD_PWR_EN via VT1 PMBT3904`
- 证据：图 b3098cc77650 / 第 1 页 / 主模块第 5 页 A1-A6，U9/FET3/VT1 与 SD 电源

### USB VBUS 受控电源路径

U16 SGM2578 以 VIN_5V 为输入、VUSB_5V 为输出，USB_ID 通过 FET4 2N7002 控制 EN，D9 PMEG3030EP 跨接 VIN/VOUT；R68 100 kΩ 与 C148/C177 组成输出网络。

- 参数与网络：`switch=U16 SGM2578`；`input=VIN_5V`；`output=VUSB_5V`；`control=USB_ID via FET4 2N7002`；`diode=D9 PMEG3030EP`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 A4-A6，U16/FET4/D9

## 接口

### Module LLM USB-C 数据与 CC/ID 控制

J1 USB-C 将 D+/D- 形成 USB_D_E_P/N，经 U15 SRV05-4 防护与 L5 SDMM0806H-2-900T 共模滤波后形成 USB_D_P/N；PD_CC1/PD_CC2 接 U14 SGM7220 CC1/CC2，U14 同时连接 USB_ID、USB_DET 与 SYS_SDA/SYS_SCL。

- 参数与网络：`connector=J1 USB-C`；`external_data=USB_D_E_P,USB_D_E_N`；`soc_data=USB_D_P,USB_D_N`；`esd=U15 SRV05-4`；`filter=L5 SDMM0806H-2-900T`；`controller=U14 SGM7220`；`cc=PD_CC1,PD_CC2`；`signals=USB_ID,USB_DET`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 A1-A4，J1/U14/U15/L5

### LP5562 三 RGB 指示灯

U20 LP5562 由 VDD_3V3 供电，经 SYS_SDA/SYS_SCL 控制，AD1/AD0 与 CLK_IN 接 GND；R/G/B 输出形成 LED_R/LED_G/LED_B并并联驱动 U18/U21/U22 三颗 LED-2020-RGB。

- 参数与网络：`driver=U20 LP5562`；`bus=SYS_SDA,SYS_SCL`；`address_pins=AD1=GND,AD0=GND`；`leds=U18,U21,U22 LED-2020-RGB`；`outputs=LED_R,LED_G,LED_B`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 C2-C4，U20/U18/U21/U22

### Module LLM M5-Bus 与 UART Net-Tie

J4 MBUS_Core2 引出 GND、MBUS_3V3、VIN_5V、MBUS_RST、BUS_SDA/BUS_SCL 和多组 BUS_Gx；Tie1-Tie4 允许 TRM_RXD 切换到 BUS_G17/G13/G6/G0，Tie5-Tie8 允许 TRM_TXD 切换到 BUS_G18/G7/G14/G10。

- 参数与网络：`connector=J4 MBUS_Core2`；`power=MBUS_3V3,VIN_5V`；`reset=MBUS_RST`；`i2c=BUS_SDA,BUS_SCL`；`rxd_options=BUS_G17,BUS_G13,BUS_G6,BUS_G0`；`txd_options=BUS_G18,BUS_G7,BUS_G14,BUS_G10`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 D1-D4，J4 与 Tie1-Tie8

### AX630C EPHY 到 FPC-8P

U1J AX630C EPHY_RXP/RXN 与 EPHY_TXP/TXN 由 VDD_3V3_EPHY、VDD_1V8_EPHY、VCORE_0V8_EPHY 供电并引出差分对；主模块 J2 FPC pins1-5 承载 EPHY_TX_N/P、GND、EPHY_RX_N/P，pins7/8 承载 DBG_RXD/DBG_TXD。

- 参数与网络：`phy=AX630C U1J EPHY`；`differential=EPHY_TX_P/N,EPHY_RX_P/N`；`fpc=J2 FPC-SMD_8P-P0.50`；`debug=DBG_RXD,DBG_TXD`；`rails=VDD_3V3_EPHY,VDD_1V8_EPHY,VCORE_0V8_EPHY`
- 证据：图 141a3b26d17b / 第 1 页 / 主模块第 9 页 B1-C6，U1J EPHY 差分与电源; 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 B1-B2，J2 8P FPC

### 未连接 DVP 与 MIPI 接口

主模块第 8 页 U1G DVP_IN VI_D0-D9/VI_CLK0 和 U1H MIPI_TX TX_CD0-CD4 均标未连接；第 10 页 MIPI_RX RX_CD0-CD5 全部标未连接。

- 参数与网络：`dvp=VI_D0-D9,VI_CLK0 NC`；`mipi_tx=TX_CD0-CD4 NC`；`mipi_rx=RX_CD0-CD5 NC`
- 证据：图 e996fa2558a7 / 第 1 页 / 主模块第 8 页 U1G DVP_IN 与 U1H MIPI_TX 全部红叉; 图 225a0cfb34ba / 第 1 页 / 主模块第 10 页 MIPI_RX RX_CD0-CD5 全部红叉

### Mate USB-C 到 CH340N 串口

Mate USB1 TYPEC-304S-ACP16 的 VBUS 经 F1 6V/1A PPTC 形成 +5V，CC1/CC2 分别经 R3/R4 5.1 kΩ 下拉；D+/D- 接 U1 CH340N UD+/UD-，CH340N RXD/TXD 经 R1/R2 100 Ω 和 D1 网络引至 J2 FPC。

- 参数与网络：`connector=USB1 TYPEC-304S-ACP16`；`fuse=F1 6V/1A PPTC`；`cc=R3,R4 5.1k`；`bridge=U1 CH340N`；`serial=RXD,TXD`；`fpc=J2 8P`
- 证据：图 96d376b6efb7 / 第 1 页 / Mate 页 A1-B4，USB1/F1/U1 CH340N/J2

### Mate RJ45 与网络变压器

Mate J2 FPC 引出 RXP/RXN/TXP/TXN，连接 T1 11FB-05NL 的 RD+/RD-/TD+/TD-；T1 另一侧 ETX+/ETX-/ERX+/ERX- 接 J5 HC-RJ45-053-5，四路各有 75 Ω/22 nF 端接并汇入 C13 1 nF/2000V。

- 参数与网络：`fpc=J2 RXP/RXN/TXP/TXN`；`transformer=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5`；`cable_pairs=ETX+,ETX-,ERX+,ERX-`；`termination=R5-R8 75R,C2/C3/C7/C8 22nF,C13 1nF/2000V`
- 证据：图 96d376b6efb7 / 第 1 页 / Mate 页 C1-D3，J2/T1/J5 完整以太网磁性链

### Mate M5Stack_BUS

Mate J3/J4 M5Stack_BUS 展开 30 针接口，pins1/3/5 为 GND，pins17/18 为 SDA/SCL，pins25/27/29 为 HPWR，pin28 为 +5V，pin30 为 BAT，其他 GPIO 按标准名称引出。

- 参数与网络：`connector=J3/J4 M5Stack_BUS`；`ground=pins1,3,5`；`i2c=pin17 SDA,pin18 SCL`；`power=pins25,27,29 HPWR,pin28 +5V,pin30 BAT`
- 证据：图 96d376b6efb7 / 第 1 页 / Mate 页 C3-D4，J3/J4 M5Stack_BUS pins1-30

## 总线

### BUS 与 SYS 两组 I2C

AX630C I2C0_SCL/SDA 形成 BUS_SCL/BUS_SDA，经 R24/R69 各 2.2 kΩ 上拉并接 J4 M5-Bus；另一组 SYS_SCL/SYS_SDA 由 AX630C GPIO2_A2/A3 引出，连接 U14 SGM7220 与 U20 LP5562。

- 参数与网络：`bus_i2c=BUS_SCL,BUS_SDA from I2C0`；`bus_pullups=R24,R69 2.2k`；`bus_external=J4 M5-Bus`；`system_i2c=SYS_SCL,SYS_SDA from GPIO2_A2/A3`；`system_devices=U14 SGM7220,U20 LP5562`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 D5-D7，BUS_SCL/SDA 与 R24/R69; 图 e996fa2558a7 / 第 1 页 / 主模块第 8 页 C3-C4，SYS_SCL/SYS_SDA; 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 A2-A4 与 C2-C4，U14/U20 SYS I2C

## 时钟

### AX630C 24MHz 与 32.768kHz 时钟

X1 24MHz/12pF/2520 连接 AX_24M_XIN/AX_24M_XOUT，外围为 R21 1 MΩ、R22 100 Ω、C70 12 pF、C72 12 pF；Y1 32.768kHz/12.5pF/3215 连接 AX_32K_XIN/AX_32K_XOUT，外围 C73/C74 各 12.5 pF。

- 参数与网络：`main=X1 24MHz`；`main_nets=AX_24M_XIN,AX_24M_XOUT`；`rtc=Y1 32.768kHz`；`rtc_nets=AX_32K_XIN,AX_32K_XOUT`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 B5-B7，X1/Y1 与外围

## 复位

### 复位与启动模式选择

AX_BOND0、AX_BOND1 与 AX_GPIOA3 各通过 47 kΩ 下拉，AX_GPIOA2_BOOT 通过 R17 10 kΩ 上拉至 VDD_1V8并由 S1 按键拉低；表格对应默认 EMMC UDA，GPIO3_A2=0 对应 USB DL、SD Card 或 UART 下载。MBUS_RST 经 FET1/FET2 2N7002/CJ139K 网络作用到 SYS_RST_IN。

- 参数与网络：`default=EMMC UDA`；`download=USB DL or SD Card or UART`；`boot_button=S1 AX_GPIOA2_BOOT`；`straps=AX_BOND0=0,AX_BOND1=0,AX_GPIOA3=0`；`external_reset=MBUS_RST -> FET1/FET2 -> SYS_RST_IN`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 A5-B7，启动表、S1、R17-R20 与复位网络

## 保护电路

### VIN_5V 输入保护

U2 AW32901 的三路 IN 接 VIN_5V、三路 OUT 输出 VDD_5V，EN 接 VIN_5V；R1 35.7 kΩ 与 R2 10.2 kΩ 设置 OVLO，输入 C160 100 nF/25V、输出 C161 1 uF 去耦。

- 参数与网络：`device=U2 AW32901`；`input=VIN_5V`；`output=VDD_5V`；`ovlo=R1 35.7k,R2 10.2k`；`enable=VIN_5V`
- 证据：图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页 A5-A7，U2 AW32901

## 存储

### eMMC 5.1 接口

U1M AX630C 的 EMMC_CLK/CMD/DAT0-DAT7/DS/RESET_N 连接 U11 EMMC_V5.1；U11 VCC 由 VDD_3V3 供电、VCCQ 由 VDD_1V8 供电，CMD 与 CLK 使用 R53/R52 10 kΩ 网络。

- 参数与网络：`device=U11 EMMC_V5.1`；`bus=CLK,CMD,DAT0-DAT7,DS,RESET_N`；`vcc=VDD_3V3`；`vccq=VDD_1V8`；`controller=U1M AX630C`
- 证据：图 b3098cc77650 / 第 1 页 / 主模块第 5 页 C1-D6，U1M/U11 eMMC 总线

### microSD 接口与保护

U10 MicroSD 的 DAT0-DAT3、CMD、CLK、SD_DET_N 连接 AX630C SDCARD 总线；CLK 经 R47 22 Ω，D2-D8 WS05DLC-B 保护数据、命令、检测和时钟网络，R45-R51 为 10 kΩ 上拉。

- 参数与网络：`connector=U10 MicroSD`；`bus=SDCARD_CLK,CMD,DAT0-DAT3`；`detect=SD_DET_N`；`clock_series=R47 22R`；`esd=D2-D8 WS05DLC-B`；`pullups=R45-R51 10k`
- 证据：图 b3098cc77650 / 第 1 页 / 主模块第 5 页 A4-C8，U10/D2-D8/R45-R51

## 内存与 Flash

### AX630C LPDDR4 总线

U1D AX630C 通过 DDR_CA0-CA5、CSA/CSB、CK/CKE、DQ0-DQ15、DQS0/1、DMI0/1 与 RESET_N 连接 U8A LPDDR4；U8B/U8C 展开 VDD1/VDD2/VDDQ 与 VSS 电源/地引脚，工作电源为 VDDR_1V1 与 VDD_1V8。

- 参数与网络：`soc=U1D AX630C`；`memory=U8A/U8B/U8C LPDDR4`；`data_width=DQ0-DQ15`；`address=CA0-CA5`；`clocks=DDR_CLK_P/N`；`rails=VDDR_1V1,VDD_1V8`
- 证据：图 a26d069d6b4e / 第 1 页 / 主模块第 4 页完整 LPDDR4 总线、电源和接地

## 音频

### AX630C 模拟音频接口

U1F AX630C 的 MICP_R/MICN_R 引出 AUDIO_IN_P/AUDIO_IN_N，HPPR/HPRN 引出 AUDIO_OUT_P/AUDIO_OUT_N，模拟电源为 AVDD_1V8，MIC_BIAS0 与 VCAP 各使用本地去耦。

- 参数与网络：`input=AUDIO_IN_P,AUDIO_IN_N`；`output=AUDIO_OUT_P,AUDIO_OUT_N`；`supply=AVDD_1V8`；`bias=MIC_BIAS0`；`controller=U1F AX630C`
- 证据：图 00b1d013437d / 第 1 页 / 主模块第 6 页 A1-A4，U1F AX630C AUDIO 单元

### MSM421A 麦克风输入

U12 MSM421A3729H9KRMC 由 AVDD_1V8 经 FB3 BLM15AG102SN1D 供电，OUT 经 C128 100 nF 形成 AUDIO_IN_P，GND 参考经 C132 100 nF 形成 AUDIO_IN_N，两路进入 AX630C 模拟音频输入。

- 参数与网络：`microphone=U12 MSM421A3729H9KRMC`；`supply=AVDD_1V8 via FB3`；`positive=OUT-C128-AUDIO_IN_P`；`negative=GND-C132-AUDIO_IN_N`；`soc=U1F AX630C`
- 证据：图 00b1d013437d / 第 1 页 / 主模块第 6 页 B1-B4，U12/FB3/C128/C132

### AW8737A 扬声器功放

AUDIO_OUT_P/N 经 C134/C136、R57/R58 形成 AMP_IN_P/N，接 U13 AW8737A；AUDIO_AP_EN 经 R56 0 Ω 形成 AMP_EN 并控制 SHDN，U13 由 VDD_5V 供电，输出经 FB4/FB5 形成 SPK_VOP/SPK_VON。

- 参数与网络：`amplifier=U13 AW8737A`；`input=AUDIO_OUT_P/N -> AMP_IN_P/N`；`enable=AUDIO_AP_EN -> AMP_EN`；`supply=VDD_5V`；`output=SPK_VOP,SPK_VON`
- 证据：图 00b1d013437d / 第 1 页 / 主模块第 6 页 C2-D5，U13 完整功放链

## 调试与烧录

### 调试 UART 与终端 UART

AX630C UART0_TXD/RXD 引出 DBG_TXD/DBG_RXD 并送往主模块 J2 FPC pins8/7；UART1_TXD/RXD 引出 TRM_TXD/TRM_RXD，经 R71/R72 10 kΩ 上拉、D10/D11 ESD 防护和 Tie1-Tie8 Net-Tie 路由到 M5-Bus 候选 GPIO。

- 参数与网络：`debug=UART0 DBG_TXD/DBG_RXD -> J2 FPC`；`terminal=UART1 TRM_TXD/TRM_RXD`；`protection=D10,D11 WS05DLC-B`；`routing=Tie1-Tie8 to M5-Bus`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 D5-D7，DBG/TRM UART; 图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 B1-D4，J2、D10/D11 与 Net-Tie

## 模拟电路

### BOARD_ID ADC 分压

BOARD_ID 由 R28 402 Ω 上拉至 VDD_1V8、R29 1.2 kΩ 下拉至 GND，并连接 AX630C THM_AIN0；图面右侧同时给出 VREFP=1.8V 的板 ID 分压查询表。

- 参数与网络：`adc=THM_AIN0`；`net=BOARD_ID`；`pullup=R28 402R to VDD_1V8`；`pulldown=R29 1.2k to GND`；`reference=VREFP 1.8V`
- 证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 B1-C8，THM_AIN0/BOARD_ID/R28/R29 与电阻表

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module LLM Kit 双模块架构 | `main=M140 Module LLM`；`mate=K144 Module13.2 LLM Mate`；`main_pages=9`；`mate_pages=1`；`interconnect=FPC-8P + M5-Bus` |
| 系统结构 | AX630C 主 SoC | `reference=U1A-U1O`；`part_number=AX630C`；`memory=LPDDR4`；`storage=eMMC5.1,microSD`；`interfaces=USB,UART,I2C,EPHY,MIPI,DVP,SDIO,audio` |
| 保护电路 | VIN_5V 输入保护 | `device=U2 AW32901`；`input=VIN_5V`；`output=VDD_5V`；`ovlo=R1 35.7k,R2 10.2k`；`enable=VIN_5V` |
| 电源 | AX630C 多路电源树 | `input=VDD_5V`；`vdd_3v3=U3 SY8089A1AAA`；`vdd_1v8=U4 SY8089A1AAA`；`vddr_1v1=U6 SY8089A1AAA`；`avdd_1v8=U5 LP5907MFX-1.8/NOPB`；`vcore_0v8=U7 JW5255A` |
| 时钟 | AX630C 24MHz 与 32.768kHz 时钟 | `main=X1 24MHz`；`main_nets=AX_24M_XIN,AX_24M_XOUT`；`rtc=Y1 32.768kHz`；`rtc_nets=AX_32K_XIN,AX_32K_XOUT` |
| 复位 | 复位与启动模式选择 | `default=EMMC UDA`；`download=USB DL or SD Card or UART`；`boot_button=S1 AX_GPIOA2_BOOT`；`straps=AX_BOND0=0,AX_BOND1=0,AX_GPIOA3=0`；`external_reset=MBUS_RST -> FET1/FET2 -> SYS_RST_IN` |
| 模拟电路 | BOARD_ID ADC 分压 | `adc=THM_AIN0`；`net=BOARD_ID`；`pullup=R28 402R to VDD_1V8`；`pulldown=R29 1.2k to GND`；`reference=VREFP 1.8V` |
| 总线 | BUS 与 SYS 两组 I2C | `bus_i2c=BUS_SCL,BUS_SDA from I2C0`；`bus_pullups=R24,R69 2.2k`；`bus_external=J4 M5-Bus`；`system_i2c=SYS_SCL,SYS_SDA from GPIO2_A2/A3`；`system_devices=U14 SGM7220,U20 LP5562` |
| 调试与烧录 | 调试 UART 与终端 UART | `debug=UART0 DBG_TXD/DBG_RXD -> J2 FPC`；`terminal=UART1 TRM_TXD/TRM_RXD`；`protection=D10,D11 WS05DLC-B`；`routing=Tie1-Tie8 to M5-Bus` |
| 内存与 Flash | AX630C LPDDR4 总线 | `soc=U1D AX630C`；`memory=U8A/U8B/U8C LPDDR4`；`data_width=DQ0-DQ15`；`address=CA0-CA5`；`clocks=DDR_CLK_P/N`；`rails=VDDR_1V1,VDD_1V8` |
| 存储 | eMMC 5.1 接口 | `device=U11 EMMC_V5.1`；`bus=CLK,CMD,DAT0-DAT7,DS,RESET_N`；`vcc=VDD_3V3`；`vccq=VDD_1V8`；`controller=U1M AX630C` |
| 存储 | microSD 接口与保护 | `connector=U10 MicroSD`；`bus=SDCARD_CLK,CMD,DAT0-DAT3`；`detect=SD_DET_N`；`clock_series=R47 22R`；`esd=D2-D8 WS05DLC-B`；`pullups=R45-R51 10k` |
| 电源 | microSD 电源与 IO 电压 | `io_regulator=U9 WL2811EA-5/TR`；`io_input=VDD_5V`；`io_output=VDDIO_SDCARD`；`card_switch=FET3 CJ2301`；`card_input=VDD_3V3`；`card_output=VDD_SDCARD`；`enable=SD_PWR_EN via VT1 PMBT3904` |
| 音频 | AX630C 模拟音频接口 | `input=AUDIO_IN_P,AUDIO_IN_N`；`output=AUDIO_OUT_P,AUDIO_OUT_N`；`supply=AVDD_1V8`；`bias=MIC_BIAS0`；`controller=U1F AX630C` |
| 音频 | MSM421A 麦克风输入 | `microphone=U12 MSM421A3729H9KRMC`；`supply=AVDD_1V8 via FB3`；`positive=OUT-C128-AUDIO_IN_P`；`negative=GND-C132-AUDIO_IN_N`；`soc=U1F AX630C` |
| 音频 | AW8737A 扬声器功放 | `amplifier=U13 AW8737A`；`input=AUDIO_OUT_P/N -> AMP_IN_P/N`；`enable=AUDIO_AP_EN -> AMP_EN`；`supply=VDD_5V`；`output=SPK_VOP,SPK_VON` |
| 接口 | Module LLM USB-C 数据与 CC/ID 控制 | `connector=J1 USB-C`；`external_data=USB_D_E_P,USB_D_E_N`；`soc_data=USB_D_P,USB_D_N`；`esd=U15 SRV05-4`；`filter=L5 SDMM0806H-2-900T`；`controller=U14 SGM7220`；`cc=PD_CC1,PD_CC2`；`signals=USB_ID,USB_DET` |
| 电源 | USB VBUS 受控电源路径 | `switch=U16 SGM2578`；`input=VIN_5V`；`output=VUSB_5V`；`control=USB_ID via FET4 2N7002`；`diode=D9 PMEG3030EP` |
| 接口 | LP5562 三 RGB 指示灯 | `driver=U20 LP5562`；`bus=SYS_SDA,SYS_SCL`；`address_pins=AD1=GND,AD0=GND`；`leds=U18,U21,U22 LED-2020-RGB`；`outputs=LED_R,LED_G,LED_B` |
| 接口 | Module LLM M5-Bus 与 UART Net-Tie | `connector=J4 MBUS_Core2`；`power=MBUS_3V3,VIN_5V`；`reset=MBUS_RST`；`i2c=BUS_SDA,BUS_SCL`；`rxd_options=BUS_G17,BUS_G13,BUS_G6,BUS_G0`；`txd_options=BUS_G18,BUS_G7,BUS_G14,BUS_G10` |
| 接口 | AX630C EPHY 到 FPC-8P | `phy=AX630C U1J EPHY`；`differential=EPHY_TX_P/N,EPHY_RX_P/N`；`fpc=J2 FPC-SMD_8P-P0.50`；`debug=DBG_RXD,DBG_TXD`；`rails=VDD_3V3_EPHY,VDD_1V8_EPHY,VCORE_0V8_EPHY` |
| 接口 | 未连接 DVP 与 MIPI 接口 | `dvp=VI_D0-D9,VI_CLK0 NC`；`mipi_tx=TX_CD0-CD4 NC`；`mipi_rx=RX_CD0-CD5 NC` |
| 接口 | Mate USB-C 到 CH340N 串口 | `connector=USB1 TYPEC-304S-ACP16`；`fuse=F1 6V/1A PPTC`；`cc=R3,R4 5.1k`；`bridge=U1 CH340N`；`serial=RXD,TXD`；`fpc=J2 8P` |
| 接口 | Mate RJ45 与网络变压器 | `fpc=J2 RXP/RXN/TXP/TXN`；`transformer=T1 11FB-05NL`；`connector=J5 HC-RJ45-053-5`；`cable_pairs=ETX+,ETX-,ERX+,ERX-`；`termination=R5-R8 75R,C2/C3/C7/C8 22nF,C13 1nF/2000V` |
| 接口 | Mate M5Stack_BUS | `connector=J3/J4 M5Stack_BUS`；`ground=pins1,3,5`；`i2c=pin17 SDA,pin18 SCL`；`power=pins25,27,29 HPWR,pin28 +5V,pin30 BAT` |
| 系统结构 | AX630C CPU 与 NPU 算力 | `documented_cpu=Dual Cortex-A53 1.2GHz`；`documented_int4=12.8 TOPS`；`documented_int8=3.2 TOPS`；`schematic_performance=null` |
| 内存与 Flash | 4GB LPDDR4 及内存分配 | `documented_total=4GB`；`documented_system=1GB`；`documented_accelerator=3GB`；`schematic_part_number=LPDDR4 generic`；`schematic_capacity=null` |
| 存储 | 32GB eMMC5.1 容量 | `documented_capacity=32GB`；`documented_standard=eMMC5.1`；`schematic_part=U11 EMMC_V5.1`；`usable_capacity=null`；`endurance=null` |
| 总线地址 | SGM7220 与 LP5562 I2C 地址 | `sgm7220_addr_pin=GND via R61 0R`；`lp5562_ad1=GND`；`lp5562_ad0=GND`；`sgm7220_address=null`；`lp5562_address=null` |
| 音频 | 8Ω@1W 2014 扬声器 | `documented_impedance=8ohm`；`documented_power=1W`；`documented_size=2014 cavity`；`amplifier=U13 AW8737A`；`speaker_part=null` |
| 接口 | 默认 115200@8N1 串口 | `documented_baud=115200`；`documented_format=8N1`；`documented_adjustable=true`；`hardware_paths=DBG UART,TRM UART,CH340N`；`flow_control=null` |
| 接口 | 百兆以太网能力 | `documented_speed=100Mbps`；`phy=AX630C integrated EPHY`；`transformer=11FB-05NL`；`connector=RJ45`；`autonegotiation=null` |
| 电源 | 空载与满载功耗 | `documented_idle=5V@0.5W`；`documented_full=5V@1.5W`；`firmware=null`；`workload=null`；`temperature=null`；`measurement=null` |
| 接口 | USB OTG 行为 | `documented_otg=true`；`data=USB_D_P,USB_D_N`；`cc_controller=U14 SGM7220`；`vbus_switch=U16 SGM2578`；`role_table=null`；`current_limit=null`；`supported_classes=null` |
| 调试与烧录 | SD/Type-C 升级与 ADB 调试 | `documented_update=SD card,Type-C`；`documented_adb=true`；`boot_hardware=GPIOA2 low -> USB DL or SD Card or UART`；`image_format=null`；`priority=null`；`rollback=null` |
| 其他事实 | Ubuntu、StackFlow 与离线 AI 功能 | `documented_os=Ubuntu`；`documented_framework=StackFlow`；`documented_model=Qwen2.5-0.5B`；`documented_functions=KWS,ASR,LLM,TTS`；`documented_update=apt`；`documented_api=OpenAI-compatible plugin`；`firmware_version=null` |
| 接口 | HT3.96*9P DIY 扩展焊盘 | `documented_header=HT3.96*9P`；`schematic_headers=P1 Header4,P2 Header4`；`schematic_connected_nets=null`；`pinout=null` |

## 待确认事项

- `system.documented-performance`：源文档称 AX630C 为双 Cortex-A53 1.2GHz，并给出 12.8 TOPS @INT4 与 3.2 TOPS @INT8；图面确认 AX630C 器件与电源/接口，但没有 CPU 频率、NPU 单元、精度条件或性能测试文字。（证据：图 d660230e4d50 / 第 1 页 / AX630C 多单元仅标芯片型号和接口，无 CPU/NPU 性能注记）
- `memory.documented-capacity`：源文档称 LPDDR4 总容量为 4GB，其中 1GB 为系统内存、3GB 为硬件加速专用；原理图的 U8 仅标 LPDDR4 和总线/电源，没有颗粒完整料号、密度、位宽组合或固件内存划分。（证据：图 a26d069d6b4e / 第 1 页 / 主模块第 4 页 U8A/U8B/U8C 仅标 LPDDR4，无容量文字）
- `storage.documented-emmc-capacity`：源文档称板载 32GB eMMC5.1；原理图 U11 仅标 EMMC_V5.1 并给出总线/电源，没有具体料号、标称容量、可用容量或寿命等级。（证据：图 b3098cc77650 / 第 1 页 / 主模块第 5 页 U11 仅标 EMMC_V5.1）
- `address.i2c-devices`：图面确认 U14 SGM7220 ADDR 经 R61 0 Ω 接 GND，U20 LP5562 AD1/AD0 均接 GND，但没有写出对应 7 位地址。（证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 U14 ADDR 与 U20 AD1/AD0，无地址文字）
- `audio.documented-speaker`：源文档称扬声器为 8Ω@1W、2014 腔体；原理图确认 AW8737A 与 SPK_VOP/SPK_VON，但没有扬声器连接器、料号、阻抗、额定功率或腔体尺寸文字。（证据：图 00b1d013437d / 第 1 页 / 主模块第 6 页只有 U13 与 SPK_VOP/SPK_VON，无扬声器规格）
- `interface.documented-uart-default`：源文档称默认串口为 115200@8N1 且可调；图面确认 DBG/TRM UART、CH340N 和 Net-Tie/FPC 路径，但没有波特率、帧格式、流控或固件配置。（证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页 UART0/UART1 仅标 DBG/TRM 网络; 图 96d376b6efb7 / 第 1 页 / Mate CH340N 路径无波特率或帧格式）
- `interface.documented-ethernet-speed`：源文档称 Mate 的 RJ45 与 11FB-05NL 扩展百兆以太网；图面确认 AX630C EPHY 差分、FPC、11FB-05NL 与 RJ45 链路，但没有 10/100 速率、自动协商、线序、时钟或网络性能文字。（证据：图 141a3b26d17b / 第 1 页 / 主模块第 9 页 EPHY 仅标差分接口; 图 96d376b6efb7 / 第 1 页 / Mate RJ45/11FB-05NL 无速率注记）
- `power.documented-consumption`：源文档列出空载 5V@0.5W、满载 5V@1.5W；原理图提供电源树和负载接口，但没有模型、NPU 利用率、温度、外设、输入位置、测量仪器或统计方法。（证据：图 04d8e4d3a1f4 / 第 1 页 / 主模块第 2 页电源树无整机功耗测试条件）
- `interface.documented-otg`：源文档称支持 OTG；图面确认 USB-C 数据、SGM7220 CC/ID、USB_ID 与 SGM2578 受控 VBUS 路径，但没有角色检测真值表、供电方向、电流限制、支持设备类别或协议栈。（证据：图 3cd38ef8bf5d / 第 1 页 / 主模块第 7 页 USB-C/SGM7220/SGM2578 硬件，无 OTG 行为表）
- `debug.documented-update-adb`：源文档称支持 SD 卡和 Type-C 固件升级、ADB 调试，并通过下载按键进入升级模式；启动表确认 GPIOA2 低时可选 USB DL、SD Card 或 UART，但没有镜像格式、优先级、ADB USB 配置、恢复流程或失败回滚。（证据：图 d660230e4d50 / 第 1 页 / 主模块第 3 页启动表与 S1，无固件/ADB 流程）
- `other.documented-software`：源文档称内置 Ubuntu 与 StackFlow，出厂预装 Qwen2.5-0.5B，并提供 KWS、ASR、LLM、TTS、apt 模型更新及 OpenAI API 插件；十页原理图只描述硬件，不能证明操作系统镜像、模型版本、API 兼容性、并行模型数量或离线推理表现。（证据：图 d660230e4d50 / 第 1 页 / AX630C 硬件页无 OS、StackFlow、模型或 API 信息）
- `interface.documented-diy-header`：源文档称 Mate 预留 HT3.96*9P 焊盘；Mate 图右侧只显示 P1/P2 两组 Header 4 且均无网络连接，页面未标 HT3.96、9P 总针数或逐针功能。（证据：图 96d376b6efb7 / 第 1 页 / Mate 页 C4-D4，P1/P2 各 Header 4，无网络与 HT3.96/9P 注记）
- `review.soc-performance`：AX630C 双 Cortex-A53 1.2GHz、12.8 TOPS INT4 与 3.2 TOPS INT8 的工作条件和实测边界是什么？；原因：图面仅确认 AX630C 器件和硬件接口。
- `review.lpddr4-capacity`：U8 LPDDR4 的完整颗粒料号、总容量和 1GB/3GB 内存分配由什么 BOM 与固件配置确认？；原因：图面仅标 LPDDR4 通用符号和总线。
- `review.emmc-capacity`：U11 eMMC 的完整料号、32GB 标称/可用容量和寿命等级是什么？；原因：图面仅标 EMMC_V5.1。
- `review.i2c-addresses`：SGM7220 ADDR=0 与 LP5562 AD1/AD0=0 时的正式 7 位 I2C 地址分别是什么？；原因：图面只给出地址脚电平，没有地址文字。
- `review.speaker`：8Ω@1W 2014 扬声器的具体料号、连接器和 AW8737A 额定条件是什么？；原因：图面只有功放和 SPK 差分网络。
- `review.uart-default`：DBG/TRM/CH340N 哪一路默认使用 115200@8N1，调速、流控和端口映射如何定义？；原因：图面提供多条 UART 硬件路径但无固件配置。
- `review.ethernet-speed`：AX630C EPHY、FPC、11FB-05NL 与 RJ45 的正式 10/100 模式、自动协商和线序是什么？；原因：图面没有百兆或协议层注记。
- `review.power-consumption`：空载 0.5W 与满载 1.5W 使用什么固件、模型、NPU 负载、外设和测量方法？；原因：原理图不能证明整机工作状态与测试边界。
- `review.otg`：USB OTG 的角色检测真值表、供电方向、电流限制与支持设备类别是什么？；原因：图面只确认 CC/ID 与受控 VBUS 硬件。
- `review.update-adb`：SD、Type-C、UART 下载的优先级、镜像格式、ADB 配置和失败回滚流程是什么？；原因：启动表只给下载入口类别。
- `review.software`：量产 Ubuntu、StackFlow、Qwen2.5、KWS/ASR/LLM/TTS 与 OpenAI API 插件的版本和资源边界是什么？；原因：软件与模型能力不在原理图中。
- `review.diy-header`：Mate 的 HT3.96*9P 焊盘对应哪些位号和逐针网络，P1/P2 两组 Header4 是否属于该接口？；原因：源文档与图面针数/标注无法直接对应。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `04d8e4d3a1f437648d64f0954da6e7d4209fe030dd80e12e5d0fc21294ab27df` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_02.png` |
| 2 | 1 | `d660230e4d50db57eb25c1a5b8f9316e1cded68db9b69c0f3c6db53fd77037fc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_03.png` |
| 3 | 1 | `a26d069d6b4ed101321cf768d1a0ffaea0206507b2c1300b7e61028077627767` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_04.png` |
| 4 | 1 | `b3098cc77650a26b76198ae615d4047069e89cf24f3e9c681b172d35b936f3f1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_05.png` |
| 5 | 1 | `00b1d013437da8f15a51912587a12f6c6eaf685c768689d73d16de0b171bcee3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_06.png` |
| 6 | 1 | `3cd38ef8bf5d582ca4f6ded3f8b34f5f26951091096fa3c8fbc35fac9b7ee71a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_07.png` |
| 7 | 1 | `e996fa2558a73720ba0f6b541a2d5ab8057c28f5039b8e41d8241da1263d2408` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_08.png` |
| 8 | 1 | `141a3b26d17b1ea2281ff2704819e269f807faf914febf0a5bffb52d34561338` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_09.png` |
| 9 | 1 | `225a0cfb34baeb01152e260ae545722a1e21cf41ed2af775108486e605f7f161` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_10.png` |
| 10 | 1 | `96d376b6efb757bb95f884609a0dbf184d712c7402eb016f62704a39b1970204` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_Sch_Module13.2_LLM_MATE_page_01.png` |

---

源文档：`zh_CN/module/Module LLM Kit.md`

源文档 SHA-256：`412b97a529b9ec0770454d87a40f41cb744d7cad2e1727d8e8265cdbdf5e4bba`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
