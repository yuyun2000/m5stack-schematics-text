# AI Pyramid 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AI Pyramid |
| SKU | AI-003 |
| 产品 ID | `ai-pyramid-fd54617506a4` |
| 源文档 | `zh_CN/ai_hardware/AI_Pyramid.md` |

## 概述

AI Pyramid 主板以 AX650C/AX650N（U1）为 SoC，配两颗 LPDDR4、eMMC 5.1、microSD、双 M.2 M-Key PCIe、双千兆以太网、GL3510 USB3 Hub 和双 HDMI 输出。STM32G431CBU6（U15）作为 EC，通过 I2C/SPI/UART 管理 PD、电源监测、多路稳压与负载开关、风扇、Grove、按键和 NeoPixel。音频链由 ES7210 四路麦克风 ADC、ES8311 Codec（0x18）和 AW8737A 功放组成。Type-C PD 使用 HUSB238 与 AW32901 输入保护，电源树生成 VDD_5V、VDD_EXT_5V、STB_3V3、VDD_CORE、NNVDD、VDD_CPU、VDDR_1V1、VDDR_0V6、VDD_3V3 与 VDD_1V8。图面 SoC 标注 AX650C/AX650N，与产品正文 AX8850 冲突；LPDDR4 与 eMMC 容量也未在器件页打印。

## 检索关键词

`AI Pyramid`、`AI-003`、`AX650C`、`AX650N`、`AX8850`、`STM32G431CBU6`、`LPDDR4`、`FLXW2004G-P1`、`eMMC 5.1`、`microSD`、`MAX77812`、`HUSB238`、`AW32901`、`SY8368`、`INA3221`、`GL3510`、`JL210-N040I`、`RTL8211F-CG`、`PCIe`、`M.2 M-Key`、`ES7210`、`ES8311`、`0x18`、`AW8737A`、`I2S`、`HDMI0`、`HDMI1`、`USB3`、`GROVE 2`、`GROVE 3`、`EC_I2C_SCL`、`EC_I2C_SDA`、`VDD_CORE`、`NNVDD`、`VDD_CPU`、`VDD_3V3`、`VDD_1V8`、`24MHz`、`32.768kHz`、`NeoPixel`、`FAN_PWM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | AX650C | 主 SoC，连接 LPDDR4、存储、PCIe、USB、双以太网、HDMI、I2S 与系统控制网络 | 图 7b76986f4203 / 第 1 页 / 主板第 6 页 source_006，AX650 Sys/IO/HDMI/USB/PCIe/SD 多分区 U1A~U1H |
| U15 | STM32G431CBU6 | EC 协处理器，管理电源、风扇、扩展接口、按键与系统控制 | 图 ac95559493fa / 第 1 页 / 主板第 3 页 source_003，EC MCU 区 U15 STM32G431CBU6 与全部控制网络 |
| U5/U6 | FLXW2004G-P1 | 两颗 LPDDR4 存储器，分别连接 DDR0/DDR1 控制器 | 图 2a0a507636e9 / 第 1 页 / 主板第 7 页 source_007，U5 LPDDR4 CA/DQ/Power; 图 927f50498059 / 第 1 页 / 主板第 8 页 source_008，U6 LPDDR4 CA/DQ/Power |
| U22/U21 | EMMC_V5.1 / MicroSD | 板载 eMMC 与可移除 microSD 存储 | 图 ed6d3ba4bc0d / 第 1 页 / 主板第 9 页 source_009，U22 eMMC、U21 MicroSD、各自负载开关与 ESD/上拉 |
| U24/U25 | JL210-N040I/RTL8211F-CG | ETH0/ETH1 双千兆 RGMII PHY | 图 d5a32b70abe2 / 第 1 页 / 主板第 11 页 source_011，Gigabit Ethernet PHY 1/2 与 RJ45 MagJack |
| U36 | GL3510 | USB3.0 Hub，连接一个上行口与四个下行口 | 图 7437df3f6ea7 / 第 1 页 / 主板第 12 页 source_012，GL3510 USB3.0 Hub Power/Sys/US/DS1~DS4 |
| U5/U7/U6 (audio) | ES7210 / ES8311 / AW8737A | 四麦克风 ADC、音频 Codec 与扬声器功放链 | 图 bb5881ae854e / 第 1 页 / 按键/音频板 source_015，下部 ES7210、ES8311、AW8737A 与麦克风/扬声器接口 |
| U4/U7 | HUSB238 / AW32901 | Type-C PD 协议与输入过压保护 | 图 c81ac592f3be / 第 1 页 / 主板第 2 页 source_002，CC Protocol HUSB238 与 Input Protection AW32901 |
| U2/U3 | MAX77812 | SPI/I2C 管理的多相 PMIC，生成核心、NPU、CPU 与 DDR 电源轨 | 图 34ab6bdc81ab / 第 1 页 / 主板第 4 页 source_004，PMIC1/PMIC2 MAX77812 与 VDD_CORE/NNVDD/VDD_CPU/VDDR_1V1/VDDR_0V6 |
| J1/J3 | M.2 NGFF M-Key | 两路 PCIe M.2 扩展槽 | 图 5362608ad7f4 / 第 1 页 / 主板第 10 页 source_010，NGFF M.2 M-Key Slot 1/2 与 PCIe0/PCIe1 |
| J31/U28 | RJ45-GBE-MagJack-SMD | 双千兆以太网磁性 RJ45 接口 | 图 d5a32b70abe2 / 第 1 页 / 主板第 11 页 source_011，Gigabit Ethernet Port 1/2 J31/U28 与 ESD |
| J5/HDMI connectors | HDMI 2.0 interface | 两路 HDMI0/HDMI1 差分视频、CEC、SDA/SCL 与 HPD 接口 | 图 fa3eec98c394 / 第 1 页 / HDMI 板 source_016，双 HDMI 连接器、共模电感、ESD、CEC/SCL/SDA/HPD 电平转换 |

## 系统结构

### AI Pyramid 系统架构

AX650C SoC 配双 LPDDR4、eMMC/microSD、双 M.2 PCIe、双千兆网、GL3510 USB3 Hub、双 HDMI 与 I2S 音频；STM32G431CBU6 EC 管理电源和低速外设。

- 参数与网络：`soc=U1 AX650C/AX650N`；`ec=U15 STM32G431CBU6`；`memory=U5/U6 LPDDR4`；`storage=eMMC 5.1,microSD`；`network=dual RGMII Gigabit Ethernet`；`expansion=dual M.2 PCIe,USB3,Grove`；`display=HDMI0,HDMI1`；`audio=ES7210/ES8311/AW8737A`
- 证据：图 8ab27a9b3894 / 第 1 页 / 主板第 1 页 source_001 电源树总览; 图 7b76986f4203 / 第 1 页 / 主板第 6 页 source_006 AX650 系统接口分区

## 核心器件

### U15 STM32G431CBU6

EC 通过 EC_I2C_SCL/SDA、PMIC SPI、AUX UART、SWD 与 GPIO 管理风扇、电源使能、PCIe/USB/Grove/按键等控制信号。

- 参数与网络：`i2c=EC_I2C_SCL,EC_I2C_SDA`；`spi=SPI_CLK,MISO,MOSI,PMIC1_CS,PMIC2_CS`；`uart=AUX_UART_RX/TX`；`debug=SYS_SWDIO,SYS_SWCLK`；`controls=FAN_PWM,power enables,EC_BUTTON`
- 证据：图 ac95559493fa / 第 1 页 / 主板第 3 页 source_003 U15 全部引脚网络

## 电源

### Type-C PD 输入与保护

Type-C PD Input 标注 5V~20V/5A Max，经 HUSB238 协议控制和 AW32901 OVP 后形成 VIN_ISEN_P/VDD_VIN1/VDD_VIN2。

- 参数与网络：`connector=Type-C PWR`；`pd_controller=U4 HUSB238`；`ovp=U7 AW32901`；`range=5V~20V`；`max_current=5A`；`ovlo=24V`
- 证据：图 c81ac592f3be / 第 1 页 / 主板第 2 页 source_002 Type-C/CC Protocol/Input Protection

### 主电源轨

SY8368/JW5255/MAX77812/SY8003/ME1502 生成 VDD_5V、VDD_EXT_5V、NGFF1_3V3、NGFF2_3V3、USB1~3_5V、VDD_CORE、NNVDD、VDD_CPU、VDDR_1V1、VDDR_0V6、VDD_3V3 与 VDD_1V8。

- 参数与网络：`five_volt=VDD_5V,VDD_EXT_5V`；`m2=NGFF1_3V3,NGFF2_3V3`；`usb=USB1_5V,USB2_5V,USB3_5V`；`soc=VDD_CORE,NNVDD,VDD_CPU,VDD_3V3,VDD_1V8`；`ddr=VDDR_1V1,VDDR_0V6`
- 证据：图 8ab27a9b3894 / 第 1 页 / 主板第 1 页 source_001 Power Tree; 图 34ab6bdc81ab / 第 1 页 / 主板第 4 页 source_004 详细 DCDC/PMIC

## 接口

### 双 HDMI 输出

HDMI0/HDMI1 各含 CLK、D0~D2 差分对、HPD、CEC、SDA、SCL 与 5V，外接板配置共模电感、ESD、保险丝与 CEC/DDC 电平转换。

- 参数与网络：`ports=HDMI0,HDMI1`；`differential=CLK,D0,D1,D2`；`control=HPD,CEC,SDA,SCL`；`protection=ESD/common-mode chokes/100mA fuse`
- 证据：图 163a673ac43f / 第 1 页 / 主板第 13 页 source_013 HDMI FPC; 图 fa3eec98c394 / 第 1 页 / HDMI 板 source_016 双接口电路

### GROVE 2/3

GROVE 2 J11 提供 I2C3_SDA/I2C3_SCL、VDD_GRV2、GND；GROVE 3 J15 提供 THM_TXD/THM_RXD、VDD_GRV3、GND，两路 5V 均由 ME1502CM5G 500mA 负载开关控制。

- 参数与网络：`grove2=I2C3_SDA,I2C3_SCL,VDD_GRV2,GND`；`grove3=THM_TXD,THM_RXD,VDD_GRV3,GND`；`switches=U44,U45 ME1502CM5G`；`limit=500mA`
- 证据：图 163a673ac43f / 第 1 页 / 主板第 13 页 source_013 GROVE 2/3

### MIPI PHY RX

主板第 14 页明确标注 MIPI Phy RX (Not Used)，相关 AX650 引脚均为未连接。

- 参数与网络：`interface=MIPI CSI RX`；`status=not used`；`channels=RX0~RX3`
- 证据：图 7ea351721983 / 第 1 页 / 主板第 14 页 source_014 标题 MIPI Phy RX (Not Used) 与全部 NC 标记

## 总线

### 双 PCIe M.2

PCIe0/PCIe1 各以四条差分 TX/RX lane、REFCLK、PERST、CLKREQ 与 PWR_EN 连接 J1/J3 M.2 M-Key。

- 参数与网络：`slot1=J1 PCIe0 x4`；`slot2=J3 PCIe1 x4`；`clock=PCIe857-05 fanout`；`power=NGFF1_3V3,NGFF2_3V3`
- 证据：图 5362608ad7f4 / 第 1 页 / 主板第 10 页 source_010 PCIe Clock/M.2 Slots

### 双千兆以太网

AX650 RGMII0/RGMII1 分别连接 U24/U25 PHY，再经四对 MDI、ESD 与 RJ45 MagJack 形成 ETH0/ETH1；图面标注 PHY0 Address=3'b001。

- 参数与网络：`eth0=RGMII0-U24-J31`；`eth1=RGMII1-U25-U28`；`phy=JL210-N040I/RTL8211F-CG`；`address=3'b001`；`speed_label=Gigabit Ethernet`
- 证据：图 d5a32b70abe2 / 第 1 页 / 主板第 11 页 source_011 双 PHY 与双 RJ45

### GL3510 USB3 Hub

U36 GL3510 使用 25MHz 晶振，AX650 USB 上行口连接 Hub US，Hub 提供 DS1~DS4 四个 USB2/USB3 下行端口并配独立 5V 负载开关与 ESD。

- 参数与网络：`hub=U36 GL3510`；`clock=X4 25MHz`；`upstream=USB2/USB3 US`；`downstream=DS1,DS2,DS3,DS4`；`power_switch=ME1502CM5G per port`
- 证据：图 7437df3f6ea7 / 第 1 页 / 主板第 12 页 source_012 GL3510; 图 fa3eec98c394 / 第 1 页 / HDMI/USB 板 source_016 DS3/DS4 Type-A

## 总线地址

### ES8311 I2C 地址

音频页在 ES8311 上方明确标注 I2CADDR(7bit):0x18。

- 参数与网络：`device=ES8311`；`address=0x18`；`format=7-bit`；`bus=SYS_SCL/SYS_SDA`
- 证据：图 bb5881ae854e / 第 1 页 / 按键/音频板 source_015，U7 ES8311 上方地址文字

## GPIO 与控制信号

### 按键、NeoPixel 与风扇

按键板将 EC_BUTTON/PYM_BUTTON 通过 S1 输入，并串接 12 颗 WS2812 系列 NeoPixel；风扇 J6 提供 VDD_5V_F、FAN_PWM、FAN_TACO、GND。

- 参数与网络：`buttons=EC_BUTTON,PYM_BUTTON,S1`；`rgb=12 daisy-chained NeoPixel shown on key board`；`fan=J6 VDD_5V_F,FAN_PWM,FAN_TACO,GND`
- 证据：图 bb5881ae854e / 第 1 页 / 按键板 source_015，S1 与 NeoPixel 链; 图 163a673ac43f / 第 1 页 / 主板第 13 页 source_013 FAN J6

## 时钟

### 系统时钟源

AX650 使用 X1 24MHz 与 X2 32.768kHz 晶振；RTC BM8563 使用 X5 32.768kHz；PCIe 时钟发生器 U23 与 GL3510 Hub 分别使用 25MHz 晶振。

- 参数与网络：`soc_main=X1 24MHz`；`soc_rtc=X2 32.768kHz`；`rtc=X5 32.768kHz BM8563`；`pcie=X3 25MHz`；`usb_hub=X4 25MHz`
- 证据：图 7b76986f4203 / 第 1 页 / 主板第 6 页 source_006 SoC/RTC crystals; 图 5362608ad7f4 / 第 1 页 / 主板第 10 页 PCIe 25MHz; 图 7437df3f6ea7 / 第 1 页 / 主板第 12 页 GL3510 25MHz

## 保护电路

### 接口保护

PD 输入使用 AW32901 OVP；microSD、USB、以太网和 HDMI 均配置 ESD 器件，HDMI 5V 另有 100mA 保险丝，USB 下行口使用限流负载开关。

- 参数与网络：`pd=AW32901 OVP`；`sd=PESD3V3S1BA-N`；`usb=PESD2ETH/PESDALC10N5VU`；`ethernet=PESD2ETH`；`hdmi=ESD + 100mA fuse`；`usb_power=ME1502CM5G`
- 证据：图 c81ac592f3be / 第 1 页 / 主板第 2 页 Input Protection; 图 ed6d3ba4bc0d / 第 1 页 / 主板第 9 页 SD ESD; 图 d5a32b70abe2 / 第 1 页 / 主板第 11 页 Ethernet ESD; 图 fa3eec98c394 / 第 1 页 / HDMI 板 ESD/fuse

## 关键网络

### AI Pyramid 关键网络索引

关键链路包括 PD_USB→AW32901→VDD_5V/VDD_EXT_5V→PMIC/负载开关，AX650↔DDR0/DDR1/eMMC/SD/PCIe0/1/RGMII0/1/USB/HDMI/I2S，以及 EC_I2C/PMIC_SPI/电源使能/风扇/Grove/按键网络。

- 参数与网络：`power=PD_USB-AW32901-SY8368/MAX77812`；`memory=DDR0,DDR1`；`storage=EMMC_DATA0~7,SDCARD_DATA0~3`；`pcie=PCIE0/1 TX/RX/REFCLK`；`network=RGMII0/1`；`display=HDMI0/1`；`audio=I2S0`；`ec=EC_I2C,PMIC SPI,power enables`
- 证据：图 8ab27a9b3894 / 第 1 页 / 主板第 1 页电源树; 图 7b76986f4203 / 第 1 页 / 主板第 6 页 AX650 系统引脚

## 存储

### eMMC 与 microSD

AX650 eMMC 8-bit 总线连接 U22 EMMC_V5.1，SDIO 连接 U21 MicroSD；两路均有独立负载开关，microSD 另有 ESD 和 10K 上拉。

- 参数与网络：`emmc=U22 EMMC_V5.1,8-bit`；`sd=U21 MicroSD,SDIO`；`load_switches=U20 eMMC,U19 SDCard`；`protection=microSD ESD D18 and pull-ups R75~R80`
- 证据：图 ed6d3ba4bc0d / 第 1 页 / 主板第 9 页 source_009 Storage

## 内存与 Flash

### 双 LPDDR4

U5/U6 FLXW2004G-P1 分别连接 AX650 DDR0/DDR1 控制器，使用 VDDR_1V1、VDD_1V8、VDDR_0V6 电源域。

- 参数与网络：`devices=U5,U6 FLXW2004G-P1`；`channels=DDR0,DDR1`；`rails=VDDR_1V1,VDD_1V8,VDDR_0V6`；`capacity=not printed`
- 证据：图 2a0a507636e9 / 第 1 页 / 主板第 7 页 source_007 DDR0; 图 927f50498059 / 第 1 页 / 主板第 8 页 source_008 DDR1

## 音频

### 麦克风与扬声器音频链

ES7210 接四组 MIC1~MIC4 差分麦克风并通过 I2S0 输出；ES8311（7-bit 0x18）通过 I2S0 接收/发送音频并输出 AUD_OUT_P/N；AW8737A 放大后驱动 4Ω 扬声器接口。

- 参数与网络：`mic_adc=ES7210,4 differential mics`；`codec=ES8311 address 0x18`；`amplifier=AW8737A`；`bus=I2S0_MCLK/LRCK/SCLK/DOUT/DIN`；`speaker=SPK_VOP/SPK_VON`
- 证据：图 bb5881ae854e / 第 1 页 / 按键/音频板 source_015 下部完整音频链

## 传感器

### 双 INA3221 电源监测

U16/U17 通过 EC I2C 监测 VIN、NGFF、VUSB 等多路电压/电流感测网络。

- 参数与网络：`devices=U16,U17 INA3221 family`；`bus=EC_I2C_SCL/SDA`；`channels=VIN_ISEN,NGFF1/2,VUSB_DS1/2/3`
- 证据：图 ac95559493fa / 第 1 页 / 主板第 3 页 source_003 Power Sensor 1/2

## 射频

### 射频功能

16 页原理图未绘出 Wi-Fi/BT 射频芯片、天线或 RF 匹配网络。

- 参数与网络：`wifi=null`；`bluetooth=null`；`antenna=null`；`rf_matching=null`
- 证据：图 8ab27a9b3894 / 第 1 页 / 主板第 1 页系统总览无 RF; 图 163a673ac43f / 第 1 页 / 主板第 13 页外部接口无 RF

## 调试与烧录

### EC 调试接口

J7 5-pin EC Debug 引出 EC_RST、SYS_SWDIO、SYS_SWCLK、VSTB_3V3、GND；J10 引出 DBG_TXD/DBG_RXD/GND。

- 参数与网络：`swd=J7 EC_RST,SWDIO,SWCLK,3V3,GND`；`uart=J10 DBG_TXD,DBG_RXD,GND`
- 证据：图 163a673ac43f / 第 1 页 / 主板第 13 页 source_013 EC Debug

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AI Pyramid 系统架构 | `soc=U1 AX650C/AX650N`；`ec=U15 STM32G431CBU6`；`memory=U5/U6 LPDDR4`；`storage=eMMC 5.1,microSD`；`network=dual RGMII Gigabit Ethernet`；`expansion=dual M.2 PCIe,USB3,Grove`；`display=HDMI0,HDMI1`；`audio=ES7210/ES8311/AW8737A` |
| 核心器件 | SoC 型号 | `schematic=AX650C/AX650N`；`product_document=Axera AX8850`；`verification=revision BOM or chip marking` |
| 电源 | Type-C PD 输入与保护 | `connector=Type-C PWR`；`pd_controller=U4 HUSB238`；`ovp=U7 AW32901`；`range=5V~20V`；`max_current=5A`；`ovlo=24V` |
| 电源 | 主电源轨 | `five_volt=VDD_5V,VDD_EXT_5V`；`m2=NGFF1_3V3,NGFF2_3V3`；`usb=USB1_5V,USB2_5V,USB3_5V`；`soc=VDD_CORE,NNVDD,VDD_CPU,VDD_3V3,VDD_1V8`；`ddr=VDDR_1V1,VDDR_0V6` |
| 核心器件 | U15 STM32G431CBU6 | `i2c=EC_I2C_SCL,EC_I2C_SDA`；`spi=SPI_CLK,MISO,MOSI,PMIC1_CS,PMIC2_CS`；`uart=AUX_UART_RX/TX`；`debug=SYS_SWDIO,SYS_SWCLK`；`controls=FAN_PWM,power enables,EC_BUTTON` |
| 传感器 | 双 INA3221 电源监测 | `devices=U16,U17 INA3221 family`；`bus=EC_I2C_SCL/SDA`；`channels=VIN_ISEN,NGFF1/2,VUSB_DS1/2/3` |
| 内存与 Flash | 双 LPDDR4 | `devices=U5,U6 FLXW2004G-P1`；`channels=DDR0,DDR1`；`rails=VDDR_1V1,VDD_1V8,VDDR_0V6`；`capacity=not printed` |
| 内存与 Flash | LPDDR4 容量与速率 | `schematic_capacity=null`；`schematic_speed=null`；`product_document=4GB 64-bit LPDDR4x 4266Mbps` |
| 存储 | eMMC 与 microSD | `emmc=U22 EMMC_V5.1,8-bit`；`sd=U21 MicroSD,SDIO`；`load_switches=U20 eMMC,U19 SDCard`；`protection=microSD ESD D18 and pull-ups R75~R80` |
| 存储 | eMMC 容量 | `schematic=EMMC_V5.1`；`capacity=null`；`product_document=32GB` |
| 总线 | 双 PCIe M.2 | `slot1=J1 PCIe0 x4`；`slot2=J3 PCIe1 x4`；`clock=PCIe857-05 fanout`；`power=NGFF1_3V3,NGFF2_3V3` |
| 总线 | 双千兆以太网 | `eth0=RGMII0-U24-J31`；`eth1=RGMII1-U25-U28`；`phy=JL210-N040I/RTL8211F-CG`；`address=3'b001`；`speed_label=Gigabit Ethernet` |
| 总线 | GL3510 USB3 Hub | `hub=U36 GL3510`；`clock=X4 25MHz`；`upstream=USB2/USB3 US`；`downstream=DS1,DS2,DS3,DS4`；`power_switch=ME1502CM5G per port` |
| 接口 | 双 HDMI 输出 | `ports=HDMI0,HDMI1`；`differential=CLK,D0,D1,D2`；`control=HPD,CEC,SDA,SCL`；`protection=ESD/common-mode chokes/100mA fuse` |
| 音频 | 麦克风与扬声器音频链 | `mic_adc=ES7210,4 differential mics`；`codec=ES8311 address 0x18`；`amplifier=AW8737A`；`bus=I2S0_MCLK/LRCK/SCLK/DOUT/DIN`；`speaker=SPK_VOP/SPK_VON` |
| 总线地址 | ES8311 I2C 地址 | `device=ES8311`；`address=0x18`；`format=7-bit`；`bus=SYS_SCL/SYS_SDA` |
| 接口 | GROVE 2/3 | `grove2=I2C3_SDA,I2C3_SCL,VDD_GRV2,GND`；`grove3=THM_TXD,THM_RXD,VDD_GRV3,GND`；`switches=U44,U45 ME1502CM5G`；`limit=500mA` |
| GPIO 与控制信号 | 按键、NeoPixel 与风扇 | `buttons=EC_BUTTON,PYM_BUTTON,S1`；`rgb=12 daisy-chained NeoPixel shown on key board`；`fan=J6 VDD_5V_F,FAN_PWM,FAN_TACO,GND` |
| 时钟 | 系统时钟源 | `soc_main=X1 24MHz`；`soc_rtc=X2 32.768kHz`；`rtc=X5 32.768kHz BM8563`；`pcie=X3 25MHz`；`usb_hub=X4 25MHz` |
| 调试与烧录 | EC 调试接口 | `swd=J7 EC_RST,SWDIO,SWCLK,3V3,GND`；`uart=J10 DBG_TXD,DBG_RXD,GND` |
| 保护电路 | 接口保护 | `pd=AW32901 OVP`；`sd=PESD3V3S1BA-N`；`usb=PESD2ETH/PESDALC10N5VU`；`ethernet=PESD2ETH`；`hdmi=ESD + 100mA fuse`；`usb_power=ME1502CM5G` |
| 接口 | MIPI PHY RX | `interface=MIPI CSI RX`；`status=not used`；`channels=RX0~RX3` |
| 射频 | 射频功能 | `wifi=null`；`bluetooth=null`；`antenna=null`；`rf_matching=null` |
| 关键网络 | AI Pyramid 关键网络索引 | `power=PD_USB-AW32901-SY8368/MAX77812`；`memory=DDR0,DDR1`；`storage=EMMC_DATA0~7,SDCARD_DATA0~3`；`pcie=PCIE0/1 TX/RX/REFCLK`；`network=RGMII0/1`；`display=HDMI0/1`；`audio=I2S0`；`ec=EC_I2C,PMIC SPI,power enables` |

## 待确认事项

- `component.soc-conflict`：原理图器件与页标题标注 AX650C/AX650N，而产品正文标注 Axera AX8850；当前资料存在型号冲突。（证据：图 cc391a73f5c8 / 第 1 页 / 主板第 5 页 source_005，U1 AX650N Power/Ground Nets，器件底部 AX650N; 图 7b76986f4203 / 第 1 页 / 主板第 6 页 source_006，U1 分区底部 AX650C）
- `memory.capacity-not-shown`：原理图未打印两颗 LPDDR4 的总容量、位宽汇总或 4266Mbps 速率，无法仅由器件页确认正文 4GB 64-bit 参数。（证据：图 2a0a507636e9 / 第 1 页 / 主板第 7 页 U5 未标容量; 图 927f50498059 / 第 1 页 / 主板第 8 页 U6 未标容量）
- `storage.emmc-capacity`：U22 仅标 EMMC_V5.1，原理图未打印容量，不能从图面确认正文 32GB。（证据：图 ed6d3ba4bc0d / 第 1 页 / 主板第 9 页 U22 eMMC 器件框）
- `review.soc-model`：V0.2 主板实际装配的是 AX650C/AX650N 还是产品正文所述 AX8850？；原因：原理图与产品正文主控型号直接冲突，需 BOM、芯片丝印或版本说明确认。
- `review.memory-capacity`：U5/U6 的单颗容量、总容量、位宽和运行速率是否构成正文 4GB 64-bit LPDDR4x 4266Mbps？；原因：原理图给出器件连接与电源但未打印容量/速率。
- `review.emmc-capacity`：U22 eMMC 的完整料号与容量是否为正文所述 32GB？；原因：器件框仅标 EMMC_V5.1，没有容量或订货型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8ab27a9b389416d7d0781f6b719f93b66841f6ac47c94ec90f9a84479f0b2b67` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_01.png` |
| 2 | 1 | `c81ac592f3be019b7c56f7b09032f4fc12ee84e8a7f130f9db72677ee6ea458a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_02.png` |
| 3 | 1 | `ac95559493fa274dfae5141980241ba108f8aee180413ff4ab99243879e05b9d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_03.png` |
| 4 | 1 | `34ab6bdc81ab566d13af6a93b908bc103b825271212c37a9e00e47962c6cbaa4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_04.png` |
| 5 | 1 | `cc391a73f5c8216c17363881f1072ad7d8d9bb998309140ddddc85d330580ccc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_05.png` |
| 6 | 1 | `7b76986f4203b27321562b629358f691ccee4737c5a94732d89942c60c8526e5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_06.png` |
| 7 | 1 | `2a0a507636e968ca913843affcad96ba004f690a8fea145531f9c22411bbf877` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_07.png` |
| 8 | 1 | `927f504980596ab392662ee4eb1dbea6e55073a992cb031739478c5312966210` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_08.png` |
| 9 | 1 | `ed6d3ba4bc0dd85256d4594d9672db48a06a92776da54d304082697e372e1f22` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_09.png` |
| 10 | 1 | `5362608ad7f425bbfbc4b0445ac30d21225eb7b8626658b42314c822d5dbd052` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_10.png` |
| 11 | 1 | `d5a32b70abe240265f5f6c7097551677b1047e0917314bbae66bee992a4b07cb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_11.png` |
| 12 | 1 | `7437df3f6ea746948b1d0ba7243e8339086383eb834b25b555938655982d1ac4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_12.png` |
| 13 | 1 | `163a673ac43f27124de7d43bb2bb8cfed2362df1cdb98a8e19f35c3299bbecfb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_13.png` |
| 14 | 1 | `7ea3517219831b4f17554909eb03e2768f8651b302e29fba0c592b0c8d859690` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_MAIN_V0.2_20251117_2026_01_30_16_54_30_page_14.png` |
| 15 | 1 | `bb5881ae854e765af3e1f9e59952fd18caff91fb85f7936cfb6017fff91098cf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PCB_KEY_V0.2_2026_01_30_16_52_44_page_01.png` |
| 16 | 1 | `fa3eec98c394a17a570914eefc5394c00a7496a786ca77a83f3c464acdc3c634` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/AI-003-AI_Pyramid_PRJ_HDMI_V0.3_20251031_2026_01_30_16_51_54_page_01.png` |

---

源文档：`zh_CN/ai_hardware/AI_Pyramid.md`

源文档 SHA-256：`6858bf7f196d27c6b7260c6704581cfde135a952d01e80e993fdf2596809b5a5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
