# CoreS3 Thread BR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CoreS3 Thread BR |
| SKU | K149 |
| 产品 ID | `cores3-thread-br-3d5cedb82525` |
| 源文档 | `zh_CN/core/CoreS3_Thread_BR.md` |

## 概述

CoreS3 Thread BR 由三套原理图组成：七页 CoreS3 v1.0 以 ESP32-S3、AXP2101、128Mbit Flash、外部 PSRAM、USB-C/OTG、BM8563、AW88298、ES7210 双麦克风、AW9523B、摄像头/LCD/触摸接口、microSD 和 BMI270+BMM150 构成主控；DIN Base v1.1 以 SY8303AIC、TP4057 和电源开关提供 DC/电池供电及两路 Grove；Gateway H2 v0.4 以 ESP32-H2-MINI-1-N2 作为无线协处理器，通过 M5-Bus、0Ω电阻和八位 DIP 开关把 UART、SPI、使能及共存信号映射到 CoreS3。图面明确标注 AXP2101=0x34、AW88298=0x36、ES7210=0x40、AW9523B=0x58、BMI270=0x69；协议能力、部分子板器件、容量与额定参数单列为待确认。

## 检索关键词

`CoreS3 Thread BR`、`K149`、`CoreS3 v1.0`、`DIN Base v1.1`、`Module Gateway H2 v0.4`、`ESP32-S3`、`ESP32-H2-MINI-1-N2`、`AXP2101`、`0x34`、`AW88298`、`0x36`、`ES7210`、`0x40`、`AW9523B`、`0x58`、`BMI270`、`0x69`、`BMM150`、`BM8563`、`SY7088`、`SY8303AIC`、`TP4057`、`ME1502AM5G`、`ME1502CM5G`、`GD25Q128`、`W25Q128`、`EPSRAM`、`USB Type-C`、`USB OTG`、`M5-Bus`、`Thread`、`IEEE 802.15.4`、`OpenThread RCP`、`Zigbee`、`Matter`、`SPI_MOSI`、`SPI_MISO`、`SPI_SCK`、`SPI_CS`、`WL_ACTIVE`、`BT_ACTIVE`、`BT_PRIORITY`、`I2C_SYS_SDA`、`I2C_SYS_SCL`、`I2S_BCK`、`I2S_WCK`、`I2S_DATO`、`I2S_DATI`、`BUS_OUT`、`BUS_5V`、`BUS_BAT`、`HPWR`、`VBAT`、`GC0308`、`LTR-553ALS-WA`、`ILI9342C`、`FT6336U`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 [CoreS3 power] | AXP2101 | I2C 地址 0x34 的电源管理器，管理 VBUS/VBAT 并生成 CoreS3 多路电源 | 图 de85c198f634 / 第 1 页 / 网格 A1-D2，U1 AXP2101 与 0x34 注记 |
| U2 [CoreS3 boot] | LMV331 | AXP_PG 至 ESP_BOOT 的比较器与启动状态电路 | 图 674d725f5dc6 / 第 1 页 / 网格 A1-A3，U2 LMV331、AXP_PG、ESP_BOOT |
| U3 [CoreS3 boost] | SY7088 | AXP_PS 至 BUS_5V 的升压转换器 | 图 674d725f5dc6 / 第 1 页 / 网格 B1-C3，U3 SY7088、L5 |
| U4 [CoreS3 RTC] | BM8563 | RTC_VDD 供电的 I2C RTC，INT 接 AXP_WAKEUP | 图 674d725f5dc6 / 第 1 页 / 网格 C1-D3，U4 BM8563、Y1、BAT1 |
| U5 [CoreS3] | ESP32-S3 | 主控 SoC，连接存储、USB、音频、摄像头、LCD、microSD、M5-Bus、I2C 与射频 | 图 8f2f5466da03 / 第 1 页 / 网格 A1-C2，U5 ESP32-S3 全部引脚 |
| U6 [CoreS3] | GD25Q128/W25Q128/128Mbit/3.3V | ESP32-S3 外部 128Mbit QSPI Flash | 图 8f2f5466da03 / 第 1 页 / 网格 A3-B4，U6 Flash |
| U7 [CoreS3] | EPSRAM | ESP32-S3 外部 SPI PSRAM，使用 FLASH_CS1 | 图 8f2f5466da03 / 第 1 页 / 网格 B3-B4，U7 EPSRAM |
| U8 [CoreS3 audio] | AW88298 | I2C 地址 0x36 的 I2S 扬声器功放 | 图 f7f0dc3f29b1 / 第 1 页 / 网格 A1-B2，U8 AW88298 与 0x36 注记 |
| U9 [CoreS3 audio] | ES7210 | I2C 地址 0x40 的多通道音频 ADC，连接双麦克风与 AEC 回采 | 图 f7f0dc3f29b1 / 第 1 页 / 网格 B1-D3，U9 ES7210 与 0x40 注记 |
| U12,U13 [CoreS3 audio] | MSM381A3729H9BPC | 两颗模拟麦克风，连接 ES7210 MIC1/MIC2 差分输入 | 图 f7f0dc3f29b1 / 第 1 页 / 网格 B4-D4，U12/U13 麦克风 |
| U10 [CoreS3 IO] | AW9523B | I2C 地址 0x58 的 IO 扩展器，控制触摸、显示、摄像头、音频、TF 与电源 | 图 12e215412fd9 / 第 1 页 / 网格 A3-B4，U10 AW9523B 与 0x58 注记 |
| U11 [CoreS3] | MicroSD-SPI | 3.3V SPI microSD 卡槽 | 图 12e215412fd9 / 第 1 页 / 网格 C2-D3，U11 MicroSD-SPI |
| U15 [CoreS3 IMU] | BMI270 | I2C 地址 0x69 的六轴 IMU，并向 BMM150 提供辅助 I2C | 图 95d654aa1d79 / 第 1 页 / 网格 B1-C3，U15 BMI270、SA0 与地址说明 |
| U20 [CoreS3 IMU] | BMM150 | 连接 BMI270 ASDX/ASCX 的三轴磁力计 | 图 95d654aa1d79 / 第 1 页 / 网格 B3-C4，U20 BMM150 |
| J1,J2,LCD1,CTP1 [CoreS3] | USB-TYPEC / AFC34-S24FIA-00 / M5_LCD_10P / M5_TOUCH_8P | USB-C、摄像头、LCD 与触摸外设接口 | 图 674d725f5dc6 / 第 1 页 / 网格 A4-B4，J1 USB-TYPEC; 图 12e215412fd9 / 第 1 页 / 网格 A1-D4，J2/LCD1/CTP1 |
| BUS1 [CoreS3] | M5.BUS | 30 针堆叠总线，连接 Gateway H2 与 DIN Base | 图 12e215412fd9 / 第 1 页 / 网格 C1-D2，BUS1 M5.BUS pins1-30 |
| U14,U17,U18,U19 [CoreS3 power] | ME1502AM5G / ME1502CM5G | BUS_5V、BUS_OUT、VUSB 与 VBUS 间的受控双向电源路径 | 图 97e9cd876f18 / 第 1 页 / 网格 A1-C4，U14/U17/U18/U19 电源流向 |
| UE1 [DIN] | SY8303AIC | DIN Base 的 HPWR 至 BUS_5V 降压转换器 | 图 c1548d89f72e / 第 1 页 / 网格 A1-B3，Power 区 UE1 SY8303AIC |
| U2 [DIN] | TP4057 | VCC_5V 至 BUS_BAT 的锂电池充电器 | 图 c1548d89f72e / 第 1 页 / 网格 C1-D2，Charge 区 U2 TP4057 |
| DC1,D3,S1 [DIN] | DC-044 / DSS34 / Switch | DIN Base 直流输入、反向保护和 HPWR/BUS_BAT 双刀切换 | 图 c1548d89f72e / 第 1 页 / 网格 A1-A2，DC1/D3/S1 |
| J1,J2,J3 [DIN] | GROVE / M5_BUS | DIN Base GPIO/UART Grove 与 30 针 M5-Bus | 图 c1548d89f72e / 第 1 页 / 网格 A4-D4，J1/J2/J3 |
| M1 [Gateway H2] | ESP32-H2-MINI-1-N2 | Gateway H2 主控/无线模组，通过 M5-Bus 与 CoreS3 通信 | 图 22340fe8b841 / 第 1 页 / 网格 B1-C3，M1 ESP32-H2-MINI-1-N2 |
| S1 [Gateway H2] | SW DIP-8 | SPI 与无线共存信号到 M5-Bus 的八位拨码路由 | 图 22340fe8b841 / 第 1 页 / 网格 C3-C4，S1 SW DIP-8、R15-R21 |
| J2,J3/J4 [Gateway H2] | DownloadSocketGND / M5Stack_BUS | Gateway H2 下载接口与 30 针主机总线 | 图 22340fe8b841 / 第 1 页 / 网格 B4-D4，J2 与 J3/J4 |

## 系统结构

### CoreS3 Thread BR 三板架构

套件由 CoreS3 v1.0 主控板、DIN Base v1.1 电源底座和 Module Gateway H2 v0.4 无线模块组成；CoreS3 通过 M5-Bus 同时接收 DIN 电源并与 ESP32-H2 通信。

- 参数与网络：`controller=CoreS3 v1.0 ESP32-S3`；`base=DIN Base v1.1`；`radio_module=Module Gateway H2 v0.4 ESP32-H2-MINI-1-N2`；`interconnect=M5-Bus`
- 证据：图 12e215412fd9 / 第 1 页 / CoreS3 BUS1 M5.BUS; 图 c1548d89f72e / 第 1 页 / DIN Base J3 M5_BUS; 图 22340fe8b841 / 第 1 页 / Gateway H2 J3/J4 M5Stack_BUS

### DIN Base 电源架构

DIN Base 的 DC1 经 D3 与 S1 分配到 HPWR/BUS_BAT，UE1 SY8303AIC 将 HPWR 降压为 BUS_5V，U2 TP4057 连接 VCC_5V 与 BUS_BAT，Q1/Q2 构成 BUS_5V 至 VCC_5V 的受控通路。

- 参数与网络：`input=DC1/D3/S1`；`buck=UE1 SY8303AIC`；`charge=U2 TP4057`；`power_path=Q1 SI2301,Q2 DTC114YUA`
- 证据：图 c1548d89f72e / 第 1 页 / 网格 A1-D3，Power 与 Charge 区

### Gateway H2 模块架构

M1 ESP32-H2-MINI-1-N2 由 M5-Bus +3.3V 供电；UART、G9 与 H2-EN 通过固定 0R 路由，SPI 与 WL_ACTIVE/BT_ACTIVE/BT_PRIORITY 通过 S1 八位 DIP 开关路由。

- 参数与网络：`module=M1 ESP32-H2-MINI-1-N2`；`supply=+3.3V`；`fixed=TX0,RX0,G9,H2-EN`；`switchable=SPI,WL_ACTIVE,BT_ACTIVE,BT_PRIORITY`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 B1-D4，M1/S1/J3-J4

## 电源

### AXP2101 电源轨

AXP2101 从 VBUS/VBAT 供电：LX1 经 L1 输出 VDD_3V3，LX3 经 L3 输出 VCC_3V3，BLDO1/2 输出 AVDD/DVDD，DLDO1/DC1SW 输出 VCC_BL，VBackup/VRTC 连接 RTC_VDD，ALDO1~4 输出 VDD_1V8、VDDA_3V3、VDDCAM_3V3、VDD_3V3_SD。

- 参数与网络：`dcdc1=VDD_3V3`；`dcdc3=VCC_3V3`；`bldo=AVDD,DVDD`；`dldo=VCC_BL`；`backup=RTC_VDD`；`aldo=VDD_1V8,VDDA_3V3,VDDCAM_3V3,VDD_3V3_SD`
- 证据：图 de85c198f634 / 第 1 页 / 网格 A1-D3，U1 全部电源输出

### AXP2101 控制与按键

AXP2101 PWROK 输出 AXP_PG、PWRON 接 PWR_KEY、IRQ 输出 AXP_WAKEUP；S1/S2 分别经 R38/R39 510R 把 AXP_PG/PWR_KEY 按下接地，CHGLED 驱动红色 LED1。

- 参数与网络：`power_good=AXP_PG`；`power_key=PWR_KEY`；`irq=AXP_WAKEUP`；`buttons=S1/S2`；`charge_led=LED1 RED`
- 证据：图 de85c198f634 / 第 1 页 / 网格 C1-D4，PWROK/PWRON/IRQ/CHGLED 与 S1/S2/LED1

### CoreS3 BUS_5V 升压

U3 SY7088 从 AXP_PS 取电，经 L5 WPN3012H2R2MT 产生 BUS_5V，反馈为 R11 15K/R12 4.7K，BOOST_EN 经 R13 47R 接 EN。

- 参数与网络：`reference=U3`；`input=AXP_PS`；`output=BUS_5V`；`inductor=L5 WPN3012H2R2MT`；`feedback=R11 15K,R12 4.7K`；`enable=BOOST_EN`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 B1-C3，U3/L5/R11-R14

### CoreS3 USB/总线双向电源路径

U14 在 BUS_OUT_EN 高时把 BUS_5V 送至 BUS_OUT，U17 在 USB_OTG_EN 高时把 BUS_OUT 送至 VUSB；U19 在 BUS_OUT_EN 低时把 BUS_OUT 送至 VBUS，U18 在 USB_OTG_EN 低时把 VUSB 送至 VBUS。

- 参数与网络：`boost_to_bus=U14 ME1502AM5G`；`bus_to_otg=U17 ME1502AM5G`；`bus_to_pmu=U19 ME1502CM5G`；`usb_to_pmu=U18 ME1502CM5G`
- 证据：图 97e9cd876f18 / 第 1 页 / 网格 A1-C4，Boost/OTG/USB/PMU 箭头与 U14/U17/U18/U19

### DIN Base DC 与降压

DC1 PWR 经 D3 DSS34 到 S1，S1 切换 HPWR/BUS_BAT；UE1 VIN/EN 接 HPWR，LX 经 L1 10uH 输出 BUS_5V，反馈为 R1 120K/R3 16K，HPWR 有 D4 SMF30CA，BUS_5V 有 D1 TVS 5V。

- 参数与网络：`input=DC1 DC-044`；`diode=D3 DSS34`；`switch=S1`；`buck=UE1 SY8303AIC`；`output=BUS_5V`；`inductor=L1 10uH`；`protection=D4 SMF30CA,D1 TVS 5V`
- 证据：图 c1548d89f72e / 第 1 页 / 网格 A1-B3，DC1/D3/S1/UE1/L1/D4/D1

### DIN Base 电池充电

U2 TP4057 的 VCC 接 VCC_5V、BAT 接 BUS_BAT、PROG 经 R8 2K 接地；CHRG/STDBY 驱动 D2 红绿状态灯，P1 引出 BAT+ 与 GND。

- 参数与网络：`charger=U2 TP4057`；`input=VCC_5V`；`battery_net=BUS_BAT`；`program_resistor=R8 2K`；`status=D2 1615RG`；`battery_header=P1`
- 证据：图 c1548d89f72e / 第 1 页 / 网格 C1-D2，U2/R8/D2/P1

## 接口

### CoreS3 USB-C

J1 USB-TYPEC 的 CC1/CC2 各经 R6/R9 5.1K 接地，USB_D_P/N 由 D4/D6 ESD5Z3V3 保护，并经 R47/R25 22R 接 ESP32-S3 USB_DU_P/N；VCC 接 VUSB。

- 参数与网络：`cc=R6/R9 5.1K to GND`；`data_esd=D4/D6 ESD5Z3V3`；`series=R47/R25 22R`；`soc_gpio=GPIO20 USB_DU_P,GPIO19 USB_DU_N`；`vbus=VUSB`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 A3-B4，J1/R6/R9/R25/R47/D4/D6; 图 8f2f5466da03 / 第 1 页 / U5 GPIO19/20 USB_DU_N/P

### 摄像头/传感子板接口

J2 24-pin 接口承载 CAM_D2~D9、CAM_PCLK、CAM_VSYNC、CAM_HREF、CAM_RST、CAM_PWDN、CAM_MCLK、I2C_SYS_SDA/SCL，以及 AVDD、DVDD、VDDCAM_3V3 和 GND；X2 20MHz 输出经 R31 51R 提供 CAM_MCLK。

- 参数与网络：`connector=J2 AFC34-S24FIA-00`；`pixel_bus=CAM_D2~D9`；`sync=CAM_PCLK,CAM_VSYNC,CAM_HREF`；`control=CAM_RST,CAM_PWDN`；`clock=X2 20MHz via R31 51R`；`bus=I2C_SYS_SDA/SCL`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 A1-B3，J2/X2/R31

### LCD 与触摸接口

LCD1 连接 SPI_MOSI、SPI_SCK、LCD_CS、LCD_RST、SPI_MISO、VDD_3V3、VCC_BL 与 GND；CTP1 pins1~6 为 VDD_3V3、GND、I2C_SYS_SDA、I2C_SYS_SCL、TOUCH_INT、TOUCH_RST。

- 参数与网络：`lcd=M5_LCD_10P`；`lcd_spi=SPI_MOSI,SPI_SCK,LCD_CS,SPI_MISO`；`lcd_control=LCD_RST,VCC_BL`；`touch=M5_TOUCH_8P`；`touch_bus=I2C_SYS_SDA/SCL`；`touch_control=TOUCH_INT,TOUCH_RST`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 B4-D4，LCD1/CTP1

### DIN Base Grove 接口

J1 Grove 的 IO2/IO1 接 GPIO36/GPIO26，J2 Grove 的 IO2/IO1 接 RXD/TXD；两口均由 BUS_5V 供电并接 GND。

- 参数与网络：`gpio_port=J1 GPIO36,GPIO26`；`uart_port=J2 RXD,TXD`；`power=BUS_5V`
- 证据：图 c1548d89f72e / 第 1 页 / 网格 A4-B4，J1/J2 Grove

### Gateway H2 未装选项

M1 IO27/IO26 经 R3/R4 0R/NC 引至 USB_DP/USB_DN 与 JP1；Y1 32.768kHz、C3/C4、R6 和两路 D1/D2 LED 支路均标 NC。

- 参数与网络：`usb=IO27/IO26 via R3/R4 NC`；`crystal=Y1/C3/C4/R6 NC`；`leds=D1/D2 branches NC`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 B2-C3，JP1/Y1/D1/D2 与 NC 标记

## 总线

### CoreS3 内部 I2C

ESP32-S3 GPIO12/GPIO11 分别连接 I2C_SYS_SDA/I2C_SYS_SCL，R20/R32 各 2.2K 上拉到 VDD_3V3；AXP2101、BM8563、AW88298、ES7210、AW9523B 与 BMI270 接入该总线。

- 参数与网络：`sda=GPIO12`；`scl=GPIO11`；`pullups=R20/R32 2.2K`；`devices=AXP2101,BM8563,AW88298,ES7210,AW9523B,BMI270`
- 证据：图 8f2f5466da03 / 第 1 页 / U5 GPIO11/12 与 R20/R32; 图 f7f0dc3f29b1 / 第 1 页 / U8/U9 I2C; 图 12e215412fd9 / 第 1 页 / U10 I2C

### CoreS3 M5-Bus 信号

BUS1 引出 BUS_ADC1、BUS_PB_IN、AXP_PG、SPI_MOSI/MISO/SCK、BUS_G5/G6/G7、BUS_PB_OUT、UART0、BUS_PC_RX/TX、I2C_SYS_SDA/SCL、BUS_PA_SDA/SCL、I2S_DATO/ESP_BOOT/I2S_DATI、VCC_3V3、BUS_OUT 与 VBAT。

- 参数与网络：`spi=pins7 SPI_MOSI,9 SPI_MISO,11 SPI_SCK`；`uart=pins13/14 BUS_U0RXD/TXD,pins15/16 BUS_PC_RX/TX`；`i2c=pins17/18 I2C_SYS_SDA/SCL,pins19/20 BUS_PA_SDA/SCL`；`coexistence=pins8 BUS_G5,21 BUS_G6,22 BUS_G7,24 ESP_BOOT`；`power=pin12 VCC_3V3,pin28 BUS_OUT,pin30 VBAT`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 C1-D2，BUS1 pins1-30

### Gateway H2 固定路由到 CoreS3

Gateway M1 TX0 经模块总线 pin2 到 CoreS3 BUS_ADC1/GPIO10，RX0 经 pin16 到 BUS_PC_TX/GPIO17，G9 经 pin15 到 BUS_PC_RX/GPIO18，H2-EN 经 pin22 到 BUS_G7/GPIO7。

- 参数与网络：`tx0=module pin2 -> CoreS3 GPIO10`；`rx0=module pin16 -> CoreS3 GPIO17`；`g9=module pin15 -> CoreS3 GPIO18`；`enable=module pin22 -> CoreS3 GPIO7`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 C3-D4，R10-R13 与 J3/J4 物理 pins; 图 12e215412fd9 / 第 1 页 / BUS1 pins2/15/16/22 到 BUS_ADC1/BUS_PC_RX/BUS_PC_TX/BUS_G7; 图 8f2f5466da03 / 第 1 页 / U5 GPIO10/17/18/7 网络

### Gateway H2 SPI 与共存信号到 CoreS3

S1 闭合时，H2 SPI_CS/MOSI/CLK/MISO 分别经模块总线 pins23/7/11/9 到 CoreS3 GPIO13/37/36/35；WL_ACTIVE、BT_ACTIVE、BT_PRIORITY 分别经 pins24/21/8 到 CoreS3 GPIO0/6/5。

- 参数与网络：`spi=CS GPIO13,MOSI GPIO37,CLK GPIO36,MISO GPIO35`；`coexistence=WL_ACTIVE GPIO0,BT_ACTIVE GPIO6,BT_PRIORITY GPIO5`；`switch=S1 SW DIP-8`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 C3-D4，R15-R21/S1/J3-J4; 图 12e215412fd9 / 第 1 页 / CoreS3 BUS1 physical pins7/8/9/11/21/23/24; 图 8f2f5466da03 / 第 1 页 / CoreS3 U5 GPIO0/5/6/13/35/36/37

## 总线地址

### 图面明确标注的 I2C 地址

CoreS3 图面明确标注 U1 AXP2101=0x34、U8 AW88298=0x36、U9 ES7210=0x40、U10 AW9523B=0x58、U15 BMI270=0x69，均为 7-bit 地址。

- 参数与网络：`AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69`
- 证据：图 de85c198f634 / 第 1 页 / U1 上方 I2C ADDR(7bit):0x34; 图 f7f0dc3f29b1 / 第 1 页 / U8 0x36 与 U9 0x40 注记; 图 12e215412fd9 / 第 1 页 / U10 0x58 注记; 图 95d654aa1d79 / 第 1 页 / BMI270 SDO 地址 0x68/0x69 注记与 R50 上拉

## GPIO 与控制信号

### AW9523B 控制映射

U10 P0_0~P0_5 依次连接 TOUCH_RST、BUS_OUT_EN、AW_RST、ES_INT、TF_SW、USB_OTG_EN；P1_0~P1_3 依次连接 CAM_RST、LCD_RST、TOUCH_INT、AW_INT，P1_7 连接 BOOST_EN。

- 参数与网络：`p0=TOUCH_RST,BUS_OUT_EN,AW_RST,ES_INT,TF_SW,USB_OTG_EN`；`p1=CAM_RST,LCD_RST,TOUCH_INT,AW_INT,BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 A3-B4，U10 P0/P1

## 时钟

### ESP32-S3 40MHz 晶振

X1 标注 40MHz/10ppm/20pF/2520，连接 XTAL_40M_P/N；R33 22nH 位于 P 端，C44/C51 各 12pF 接地。

- 参数与网络：`frequency=40MHz`；`tolerance=10ppm`；`load=20pF`；`package=2520`；`network=R33 22nH,C44/C51 12pF`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 C1-D2，X1/R33/C44/C51

### BM8563 RTC

U4 BM8563 的 SCL/SDA 接 I2C_SYS_SCL/SDA，INT 接 AXP_WAKEUP，VDD 接 RTC_VDD；Y1 接 OSCI/OSCO，C30/C32 各 6pF，BAT1 标 NC。

- 参数与网络：`reference=U4`；`bus=I2C_SYS_SCL/SDA`；`interrupt=AXP_WAKEUP`；`supply=RTC_VDD`；`crystal=Y1 TXC/9H0320`；`battery=BAT1/NC XH414HG-IV01E`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 C1-D3，U4/Y1/C30/C32/BAT1

## 复位

### ESP_BOOT 比较器

U2 LMV331 由 VDD_3V3 供电，输出 ESP_BOOT 并由 R4 10K 上拉；AXP_PG 经 D3/R5 和 RC/二极管网络进入比较器，LED2 GREEN 连接 ESP_BOOT。

- 参数与网络：`reference=U2`；`input=AXP_PG`；`output=ESP_BOOT`；`pullup=R4 10K`；`indicator=LED2 GREEN`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 A1-A3，U2/D3/D5/R4/R5/LED2

### ESP32-H2 使能

M1 EN 连接 H2-EN，R2 10K 上拉至 3.3V、C13 1uF 对地；H2-EN 经 R13 0R 接 M5-Bus GPIO13，并连接 J2 pin4。

- 参数与网络：`enable=H2-EN`；`pullup=R2 10K`；`cap=C13 1uF`；`route=R13 0R to module-bus GPIO13`；`download=J2 pin4`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 B1-C4，M1 EN/R2/C13/R13/J2

## 存储

### 128Mbit QSPI Flash

U6 标注 GD25Q128/W25Q128/128Mbit/3.3V，nCS/CLK/DI/DO/nWP/nHOLD 分别连接 FLASH_CS0、FLASH_CLK、FLASH_D、FLASH_Q、FLASH_WP、FLASH_HD。

- 参数与网络：`capacity=128Mbit`；`voltage=3.3V`；`signals=FLASH_CS0,FLASH_CLK,FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 A3-B4，U6

### microSD SPI

U11 的 CS、DI、SCLK、DO 接 TF_CS、SPI_MOSI、SPI_SCK、SPI_MISO，VDD 接 VDD_3V3_SD；卡检测 SW 输出 TF_SW 并由 R28 10K 上拉。

- 参数与网络：`chip_select=TF_CS GPIO4`；`mosi=SPI_MOSI GPIO37`；`clock=SPI_SCK GPIO36`；`miso=SPI_MISO GPIO35`；`detect=TF_SW`；`supply=VDD_3V3_SD`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 C2-D3，U11/R28

## 内存与 Flash

### 外部 EPSRAM

U7 EPSRAM 使用 FLASH_CS1 片选、FLASH_CLK 时钟和 FLASH_D/Q/WP/HD 四条数据网络，VDD 接 FLASH_VCC。

- 参数与网络：`chip_select=FLASH_CS1`；`clock=FLASH_CLK`；`data=FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD`；`supply=FLASH_VCC`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 B3-B4，U7 EPSRAM

## 音频

### AW88298 扬声器功放

U8 AW88298 的 BCK/WCK/DATAI 接 I2S_BCK/I2S_WCK/I2S_DATO，AW_RST/AW_INT 为复位和中断；VOP/VON 经 FB2/FB1 输出 SPK_VOP/SPK_VON。

- 参数与网络：`address=0x36`；`i2s=I2S_BCK,I2S_WCK,I2S_DATO`；`control=AW_RST,AW_INT`；`output=SPK_VOP,SPK_VON`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 A1-B2，U8/FB1/FB2

### ES7210 双麦克风采集

U9 ES7210 MCLK 经 R34 51R 接 ESP_BOOT，SCLK/LRCK/SDOUT1 接 I2S_BCK/I2S_WCK/I2S_DATI；U12/U13 由 VBIAS_MIC 供电并连接 MIC1_P/N、MIC2_P/N。

- 参数与网络：`address=0x40`；`mclk=ESP_BOOT through R34 51R`；`i2s=I2S_BCK,I2S_WCK,I2S_DATI`；`microphones=U12/U13 MSM381A3729H9BPC`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 B1-D4，U9/U12/U13

### 扬声器 AEC 回采

SPK_VOP/SPK_VON 分别经 R40/R42 150K 和 C102/C104 耦合到 AEC_P/AEC_N，AEC_P/N 接 ES7210 MIC3P/MIC3N。

- 参数与网络：`positive=SPK_VOP->R40/C102->AEC_P`；`negative=SPK_VON->R42/C104->AEC_N`；`codec_input=ES7210 MIC3P/MIC3N`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 B2-C3，AEC_P/AEC_N 回采网络

## 传感器

### BMI270 与 BMM150

U15 BMI270 通过 I2C_SYS_SDA/SCL 接主控，SDO/SA0 由 R50 2.2K 上拉到 VDD_3V3，配置为 0x69；ASDX/ASCX 输出 BMM_SDA/BMM_SCL 到 U20 BMM150，BMM150 CSB 与 SDO 接地。

- 参数与网络：`imu=U15 BMI270 0x69`；`main_bus=I2C_SYS_SDA/SCL`；`address_strap=R50 2.2K to VDD_3V3`；`magnetometer=U20 BMM150`；`aux_bus=BMM_SDA/BMM_SCL`
- 证据：图 95d654aa1d79 / 第 1 页 / 网格 B1-C4，U15/U20/R50

## 射频

### ESP32-S3 天线路径

ESP_LNA 经 C68、C69/C86 匹配网络和 R35 0R 连接 ANT1 PROANT440；R36、L9、C121 标 NC，J4 IPEX 为未装备用路径。

- 参数与网络：`antenna=ANT1 PROANT440`；`selected_path=R35 0R`；`optional=J4 IPEX,R36/L9/C121 NC`；`matching=C68,C69,C86`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 D1-D3，ESP_LNA/ANT1/J4

## 调试与烧录

### Gateway H2 下载接口

J2 pins1~6 依次为 +3.3V、TXD/TX0、RXD/RX0、EN/H2-EN、G0/G9 网络与 GND，3.3V 端配置 C5 100nF。

- 参数与网络：`pin1=+3.3V`；`pin2=TX0`；`pin3=RX0`；`pin4=H2-EN`；`pin5=G9`；`pin6=GND`
- 证据：图 22340fe8b841 / 第 1 页 / 网格 A4-B4，J2 DownloadSocketGND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CoreS3 Thread BR 三板架构 | `controller=CoreS3 v1.0 ESP32-S3`；`base=DIN Base v1.1`；`radio_module=Module Gateway H2 v0.4 ESP32-H2-MINI-1-N2`；`interconnect=M5-Bus` |
| 总线地址 | 图面明确标注的 I2C 地址 | `AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69` |
| 电源 | AXP2101 电源轨 | `dcdc1=VDD_3V3`；`dcdc3=VCC_3V3`；`bldo=AVDD,DVDD`；`dldo=VCC_BL`；`backup=RTC_VDD`；`aldo=VDD_1V8,VDDA_3V3,VDDCAM_3V3,VDD_3V3_SD` |
| 电源 | AXP2101 控制与按键 | `power_good=AXP_PG`；`power_key=PWR_KEY`；`irq=AXP_WAKEUP`；`buttons=S1/S2`；`charge_led=LED1 RED` |
| 电源 | CoreS3 BUS_5V 升压 | `reference=U3`；`input=AXP_PS`；`output=BUS_5V`；`inductor=L5 WPN3012H2R2MT`；`feedback=R11 15K,R12 4.7K`；`enable=BOOST_EN` |
| 电源 | CoreS3 USB/总线双向电源路径 | `boost_to_bus=U14 ME1502AM5G`；`bus_to_otg=U17 ME1502AM5G`；`bus_to_pmu=U19 ME1502CM5G`；`usb_to_pmu=U18 ME1502CM5G` |
| 接口 | CoreS3 USB-C | `cc=R6/R9 5.1K to GND`；`data_esd=D4/D6 ESD5Z3V3`；`series=R47/R25 22R`；`soc_gpio=GPIO20 USB_DU_P,GPIO19 USB_DU_N`；`vbus=VUSB` |
| 复位 | ESP_BOOT 比较器 | `reference=U2`；`input=AXP_PG`；`output=ESP_BOOT`；`pullup=R4 10K`；`indicator=LED2 GREEN` |
| 存储 | 128Mbit QSPI Flash | `capacity=128Mbit`；`voltage=3.3V`；`signals=FLASH_CS0,FLASH_CLK,FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD` |
| 内存与 Flash | 外部 EPSRAM | `chip_select=FLASH_CS1`；`clock=FLASH_CLK`；`data=FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD`；`supply=FLASH_VCC` |
| 时钟 | ESP32-S3 40MHz 晶振 | `frequency=40MHz`；`tolerance=10ppm`；`load=20pF`；`package=2520`；`network=R33 22nH,C44/C51 12pF` |
| 射频 | ESP32-S3 天线路径 | `antenna=ANT1 PROANT440`；`selected_path=R35 0R`；`optional=J4 IPEX,R36/L9/C121 NC`；`matching=C68,C69,C86` |
| 总线 | CoreS3 内部 I2C | `sda=GPIO12`；`scl=GPIO11`；`pullups=R20/R32 2.2K`；`devices=AXP2101,BM8563,AW88298,ES7210,AW9523B,BMI270` |
| 时钟 | BM8563 RTC | `reference=U4`；`bus=I2C_SYS_SCL/SDA`；`interrupt=AXP_WAKEUP`；`supply=RTC_VDD`；`crystal=Y1 TXC/9H0320`；`battery=BAT1/NC XH414HG-IV01E` |
| 音频 | AW88298 扬声器功放 | `address=0x36`；`i2s=I2S_BCK,I2S_WCK,I2S_DATO`；`control=AW_RST,AW_INT`；`output=SPK_VOP,SPK_VON` |
| 音频 | ES7210 双麦克风采集 | `address=0x40`；`mclk=ESP_BOOT through R34 51R`；`i2s=I2S_BCK,I2S_WCK,I2S_DATI`；`microphones=U12/U13 MSM381A3729H9BPC` |
| 音频 | 扬声器 AEC 回采 | `positive=SPK_VOP->R40/C102->AEC_P`；`negative=SPK_VON->R42/C104->AEC_N`；`codec_input=ES7210 MIC3P/MIC3N` |
| GPIO 与控制信号 | AW9523B 控制映射 | `p0=TOUCH_RST,BUS_OUT_EN,AW_RST,ES_INT,TF_SW,USB_OTG_EN`；`p1=CAM_RST,LCD_RST,TOUCH_INT,AW_INT,BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT` |
| 接口 | 摄像头/传感子板接口 | `connector=J2 AFC34-S24FIA-00`；`pixel_bus=CAM_D2~D9`；`sync=CAM_PCLK,CAM_VSYNC,CAM_HREF`；`control=CAM_RST,CAM_PWDN`；`clock=X2 20MHz via R31 51R`；`bus=I2C_SYS_SDA/SCL` |
| 接口 | LCD 与触摸接口 | `lcd=M5_LCD_10P`；`lcd_spi=SPI_MOSI,SPI_SCK,LCD_CS,SPI_MISO`；`lcd_control=LCD_RST,VCC_BL`；`touch=M5_TOUCH_8P`；`touch_bus=I2C_SYS_SDA/SCL`；`touch_control=TOUCH_INT,TOUCH_RST` |
| 存储 | microSD SPI | `chip_select=TF_CS GPIO4`；`mosi=SPI_MOSI GPIO37`；`clock=SPI_SCK GPIO36`；`miso=SPI_MISO GPIO35`；`detect=TF_SW`；`supply=VDD_3V3_SD` |
| 总线 | CoreS3 M5-Bus 信号 | `spi=pins7 SPI_MOSI,9 SPI_MISO,11 SPI_SCK`；`uart=pins13/14 BUS_U0RXD/TXD,pins15/16 BUS_PC_RX/TX`；`i2c=pins17/18 I2C_SYS_SDA/SCL,pins19/20 BUS_PA_SDA/SCL`；`coexistence=pins8 BUS_G5,21 BUS_G6,22 BUS_G7,24 ESP_BOOT`；`power=pin12 VCC_3V3,pin28 BUS_OUT,pin30 VBAT` |
| 传感器 | BMI270 与 BMM150 | `imu=U15 BMI270 0x69`；`main_bus=I2C_SYS_SDA/SCL`；`address_strap=R50 2.2K to VDD_3V3`；`magnetometer=U20 BMM150`；`aux_bus=BMM_SDA/BMM_SCL` |
| 系统结构 | DIN Base 电源架构 | `input=DC1/D3/S1`；`buck=UE1 SY8303AIC`；`charge=U2 TP4057`；`power_path=Q1 SI2301,Q2 DTC114YUA` |
| 电源 | DIN Base DC 与降压 | `input=DC1 DC-044`；`diode=D3 DSS34`；`switch=S1`；`buck=UE1 SY8303AIC`；`output=BUS_5V`；`inductor=L1 10uH`；`protection=D4 SMF30CA,D1 TVS 5V` |
| 电源 | DIN Base 电池充电 | `charger=U2 TP4057`；`input=VCC_5V`；`battery_net=BUS_BAT`；`program_resistor=R8 2K`；`status=D2 1615RG`；`battery_header=P1` |
| 接口 | DIN Base Grove 接口 | `gpio_port=J1 GPIO36,GPIO26`；`uart_port=J2 RXD,TXD`；`power=BUS_5V` |
| 系统结构 | Gateway H2 模块架构 | `module=M1 ESP32-H2-MINI-1-N2`；`supply=+3.3V`；`fixed=TX0,RX0,G9,H2-EN`；`switchable=SPI,WL_ACTIVE,BT_ACTIVE,BT_PRIORITY` |
| 复位 | ESP32-H2 使能 | `enable=H2-EN`；`pullup=R2 10K`；`cap=C13 1uF`；`route=R13 0R to module-bus GPIO13`；`download=J2 pin4` |
| 总线 | Gateway H2 固定路由到 CoreS3 | `tx0=module pin2 -> CoreS3 GPIO10`；`rx0=module pin16 -> CoreS3 GPIO17`；`g9=module pin15 -> CoreS3 GPIO18`；`enable=module pin22 -> CoreS3 GPIO7` |
| 总线 | Gateway H2 SPI 与共存信号到 CoreS3 | `spi=CS GPIO13,MOSI GPIO37,CLK GPIO36,MISO GPIO35`；`coexistence=WL_ACTIVE GPIO0,BT_ACTIVE GPIO6,BT_PRIORITY GPIO5`；`switch=S1 SW DIP-8` |
| 调试与烧录 | Gateway H2 下载接口 | `pin1=+3.3V`；`pin2=TX0`；`pin3=RX0`；`pin4=H2-EN`；`pin5=G9`；`pin6=GND` |
| 接口 | Gateway H2 未装选项 | `usb=IO27/IO26 via R3/R4 NC`；`crystal=Y1/C3/C4/R6 NC`；`leds=D1/D2 branches NC` |
| 内存与 Flash | CoreS3 PSRAM 容量 | `source_document=8MB`；`schematic=U7 EPSRAM` |
| 核心器件 | 显示与触摸器件 | `lcd=ILI9342C 320x240`；`touch=FT6336U 0x38`；`schematic=LCD1/CTP1 connectors` |
| 传感器 | 摄像头与接近传感器 | `camera=GC0308 0.3MP`；`proximity=LTR-553ALS-WA 0x23`；`schematic=J2 interface only` |
| 总线地址 | 未在图面标注的 I2C 地址 | `BM8563=0x51`；`BMM150=0x10`；`GC0308=0x21`；`LTR553=0x23`；`FT6336U=0x38` |
| 电源 | DIN Base 电池容量 | `source_document=500mAh`；`schematic=TP4057/BUS_BAT/P1` |
| 音频 | 扬声器额定参数 | `source_document=16-bit I2S,1W speaker`；`schematic=AW88298/SPK_VOP/SPK_VON` |
| 电源 | DIN Base DC 输入范围 | `source_document=DC 9~24V`；`schematic=DC1/D4 SMF30CA/UE1 SY8303AIC` |
| 接口 | DIN HPWR 与 CoreS3 HVIN 对应 | `source_document=HVIN on three Base DIN positions`；`cores3_schematic=BUS1 high-power positions NC`；`din_schematic=three HPWR positions` |
| 射频 | Gateway H2 无线协议能力 | `source_document=IEEE 802.15.4,Thread,Zigbee,Matter`；`schematic=ESP32-H2-MINI-1-N2` |
| 系统结构 | OpenThread RCP 角色与运行规格 | `role=OpenThread RCP`；`cpu=RISC-V single-core`；`frequency=96MHz`；`schematic=M1 ESP32-H2-MINI-1-N2 only` |
| 系统结构 | CoreS3 主控运行规格 | `cpu=dual-core 240MHz`；`wifi=2.4GHz Wi-Fi`；`schematic=ESP32-S3/X1/antenna path` |

## 待确认事项

- `memory.documented-8mb-psram`：产品源文档标注 8MB PSRAM；原理图 U7 只标 EPSRAM 并显示 SPI 网络，没有器件型号或容量。（证据：图 8f2f5466da03 / 第 1 页 / 网格 B3-B4，U7 EPSRAM）
- `component.display-touch`：产品源文档标注 2.0英寸 320x240 ILI9342C 与 FT6336U 0x38；主板图只给 LCD1/CTP1 连接器和网络，没有显示这两颗控制器。（证据：图 12e215412fd9 / 第 1 页 / 网格 B4-D4，LCD1/CTP1）
- `sensor.camera-proximity`：产品源文档标注 GC0308 0.3MP 与 LTR-553ALS-WA 0x23；主板图仅给 J2 摄像头/传感子板接口，没有这两个器件、地址或像素参数。（证据：图 12e215412fd9 / 第 1 页 / 网格 A1-B3，J2 摄像头/传感子板接口）
- `address.unannotated-devices`：产品源文档列 BM8563=0x51、BMM150=0x10、GC0308=0x21、LTR-553ALS-WA=0x23、FT6336U=0x38；图中 BM8563/BMM150 未写地址，其余三颗器件未画出。（证据：图 674d725f5dc6 / 第 1 页 / U4 BM8563 无地址注记; 图 95d654aa1d79 / 第 1 页 / U20 BMM150 无地址注记; 图 12e215412fd9 / 第 1 页 / J2/LCD1/CTP1 仅为接口）
- `power.documented-battery`：产品源文档标注 DIN Base 内置 500mAh 锂电池；DIN 原理图只显示 TP4057、BUS_BAT 与 P1 BAT+ 接口，没有电池型号、容量或保护参数。（证据：图 c1548d89f72e / 第 1 页 / 网格 C1-D2，U2/P1/BUS_BAT）
- `audio.documented-speaker`：产品源文档标注 AW88298 16-bit I2S 与 1W 扬声器；音频页只显示 AW88298 和 SPK_VOP/SPK_VON 网络，没有扬声器器件、阻抗、功率或 I2S 位宽。（证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 A1-B3，U8 与 SPK_VOP/SPK_VON）
- `power.din-input-range`：产品源文档标注 DC 9~24V 输入；DIN 原理图显示 DC1、SMF30CA、SY8303AIC 与 5V 输出，但没有在页内直接标注允许输入范围。（证据：图 c1548d89f72e / 第 1 页 / 网格 A1-B3，DIN Power 区未标输入范围）
- `interface.din-cores3-hvin`：产品源文档把 CoreS3 M5-Bus 三个高压位置标为 HVIN(Base DIN)，CoreS3 v1.0 原理图 BUS1 对应位置标为 NC，而 DIN 图显示三路 HPWR；准确物理编号与量产连接需确认。（证据：图 12e215412fd9 / 第 1 页 / CoreS3 BUS1 pins25/27/29 标 NC; 图 c1548d89f72e / 第 1 页 / DIN J3 三路 HPWR 与 BUS_5V/BUS_BAT）
- `rf.gateway-protocols`：产品源文档标注 IEEE 802.15.4、Thread、Zigbee 与 Matter；Gateway 原理图只标 ESP32-H2-MINI-1-N2 和板载天线，没有协议版本或固件能力。（证据：图 22340fe8b841 / 第 1 页 / 网格 B1-C3，M1 模组与天线符号）
- `system.gateway-rcp-role`：产品源文档称 Gateway H2 作为 OpenThread Radio 协处理器，并标注 RISC-V 单核 96MHz；这些运行角色、固件与频率没有印在原理图页面。（证据：图 22340fe8b841 / 第 1 页 / M1 模组页未标运行角色或频率）
- `system.cores3-operating-specs`：产品源文档标注 ESP32-S3 双核 240MHz 与 2.4GHz Wi-Fi；原理图显示 ESP32-S3、40MHz 晶振与天线网络，但未直接给出 CPU 运行频率或无线协议参数。（证据：图 8f2f5466da03 / 第 1 页 / U5 ESP32-S3、X1 与 RF 网络，未标运行规格）
- `review.psram`：CoreS3 的 U7 PSRAM 具体型号与容量是否确认为 8MB？；原因：原理图只标 EPSRAM，未给器件型号与容量。
- `review.display-touch`：CoreS3 Thread BR 的 LCD 与触摸控制器是否分别为 ILI9342C 和 FT6336U？；原因：主板页只显示连接器。
- `review.camera-proximity`：摄像头/传感子板是否确认为 GC0308 0.3MP 与 LTR-553ALS-WA？；原因：原理图只显示 J2 接口，没有子板器件。
- `review.unannotated-addresses`：BM8563、BMM150、GC0308、LTR-553ALS-WA、FT6336U 的量产地址是否分别为 0x51、0x10、0x21、0x23、0x38？；原因：这些地址未在当前图面直接标注。
- `review.battery`：DIN Base 内置电池的型号、容量和保护参数是否确认为 500mAh？；原因：原理图未显示电池料号或容量。
- `review.speaker`：CoreS3 扬声器的型号、阻抗、额定 1W 条件和 I2S 位宽是什么？；原因：音频页没有扬声器负载与格式参数。
- `review.din-input-range`：DIN Base 的确认 DC 输入范围是否为 9~24V？；原因：范围来自产品源文档，原理图未直接标注。
- `review.din-hvin-map`：DIN Base 三路 HPWR 与 CoreS3 文档所称 HVIN 的准确物理针号是什么？；原因：CoreS3 v1.0 图对应位置标 NC，而产品源文档称 HVIN。
- `review.gateway-protocols`：Gateway H2 的量产固件支持哪些 IEEE 802.15.4、Thread、Zigbee 与 Matter 版本？；原因：原理图无法证明协议与固件能力。
- `review.gateway-rcp`：Gateway H2 的 RCP 固件、96MHz 运行配置和主控接口模式是什么？；原因：原理图只显示硬件路由。
- `review.cores3-operating-specs`：CoreS3 的量产运行主频与无线规格是否确认为 240MHz 和 2.4GHz Wi-Fi？；原因：参数来自产品源文档，原理图未直接给出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `de85c198f6340569fcb9880840cb6d621959f85ca828bac072b6027148c6dbc7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_01.png` |
| 2 | 1 | `674d725f5dc6e794929e90b12382509383d1288daa1c072076dfb5dfcc3880b3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_02.png` |
| 3 | 1 | `8f2f5466da03500bf49e2ad964b43197786bf9dc5c6df50fb5163b31587e67eb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_03.png` |
| 4 | 1 | `f7f0dc3f29b13b37133d50f1f10161c4279e0d32cccd48127e770ab59d006060` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_04.png` |
| 5 | 1 | `12e215412fd96b2d51e3979a012840b5eab11d88da6427b3e85411d98d05908c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_05.png` |
| 6 | 1 | `97e9cd876f18a199c947ff69bb91418d59d48a2f508fc54ccfd1c053bc60ecb4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_06.png` |
| 7 | 1 | `95d654aa1d7999f926432f23a42b5414b0f342edfeb1a8a7dfec078025224d5a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_07.png` |
| 8 | 1 | `c1548d89f72e6124d5633f0cd14460607633bdc235e5b0e2d6d1ecaa0721891a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1_sch_01.png` |
| 9 | 1 | `22340fe8b8415acb6d145b3480e9aee492d2f094be4e644acb06cdc68e395b4f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4_sch_01.png` |

---

源文档：`zh_CN/core/CoreS3_Thread_BR.md`

源文档 SHA-256：`d3831dd6386364059ba7dab7b0d22b8969f87e3eb6272784b65dbc053f8e2946`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
