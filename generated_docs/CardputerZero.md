# CardputerZero 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CardputerZero |
| SKU | C154 |
| 产品 ID | `cardputerzero-5fe3a896d37a` |
| 源文档 | `zh_CN/CardputerZero.md` |

## 概述

CardputerZero 以 132 Pin CM0 模块为核心，连接 HDMI、四通道 MIPI CSI 摄像头、microSD、SPI LCD、I2C 外设、I2S 音频和四路 USB 2.0 Hub。右侧 USB-C、EXT_5VIN 与电池汇入电源系统，再生成 VSYS_CM0、VSYS_5V、VSYS_3V3、CAM_3V3、AU_3V3 及可控扩展电源。V0.6.1 页面明确采用 BMI270+BMM150、ES8389、SR9900A、TCA8418RTWR 与 M5IOE1，并提供 USB Host/Device、HAT USB/GPIO 和 Grove UART/I2C 切换。页内仍有硬件版本、5.2V 公式位号、USB 分支命名和音频时钟连接需要复核。

## 检索关键词

`CardputerZero`、`C154`、`V0.6.1`、`CM0`、`IP2315`、`BQ27220YZFR`、`AW32901FCR`、`TPS2116DRLR`、`SY7088DGC`、`SY8003`、`M5IOE1`、`TCA8418RTWR`、`BMI270`、`BMM150`、`RX8130CE`、`ES8389`、`AW8737A`、`GL852G-OHY60`、`SR9900A`、`microSD`、`HDMI`、`MIPI CSI`、`USB Host`、`USB Device`、`USB-A`、`USB-C`、`Grove`、`HAT`、`FSW7227YUWQ10G/TR`、`G2_I2C1_SDA`、`G3_I2C1_SCL`、`VSYS_IN`、`VSYS_CM0`、`VSYS_5V`、`VSYS_3V3`、`GROVE_5V`、`EXT_5VIN`、`G27_KB_INT`、`G17_HP_DET`、`G24_SPK_EN`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U11A~U11D | CM0 132PIN | 系统核心模块，提供 HDMI、USB、四通道 CSI、SDIO、I2C、SPI、UART、I2S 与 GPIO | 图 6e46c6377f56 / 第 1 页 / source_005.png 网格 A1-C8，U11A~U11D |
| U1 | IP2315 | VCHG_5V 到 VBAT 的锂电池充电控制器 | 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A5-B8，CHARG 的 U1 |
| U2/U3/U12 | AW32901FCR | USB-C、EXT_5VIN 与 CM0_5V 路径的输入保护/负载开关 | 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A3-C4，USB IN U2 与 EXT. IN U3; 图 6e46c6377f56 / 第 1 页 / source_005.png 网格 C1-D3，U12 |
| U4 | BQ27220YZFR | 通过 R15 分流器和 BAT_NTC 监测电池 | 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 B5-C8，BATTERY 的 U4 |
| U5 | TPS2116DRLR | USBC_R_5V 与 VEXT_5V 的充电输入选择器 | 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 D1-D2，PATH Switch U5 |
| U7/U8 | SY7088DGC | 从 VSYS_IN 生成 VSYS_CM0 与 VSYS_5V 的两路 DC/DC | 图 407976133b5d / 第 1 页 / source_004.png 网格 A5-C8，U7/U8 |
| U9/U10 | AW9967DNR / SY8003 | LCD 背光升压驱动器与 VSYS_3V3 DC/DC | 图 407976133b5d / 第 1 页 / source_004.png 网格 C1-D8，U9/U10 |
| U13 | SR9900A | USB 2.0 转 10/100M 以太网控制器 | 图 74f334394d13 / 第 1 页 / source_006.png 网格 A4-B8，USB TO LAN 100M |
| U14 | M5IOE1 | I2C GPIO/PWM/ADC 扩展器，管理复位、LED、背光、扩展供电和功能切换 | 图 74f334394d13 / 第 1 页 / source_006.png 网格 A1-B3，M5IOM1 的 U14 |
| U15 | GL852G-OHY60 | 一上行四下行 USB 2.0 Hub | 图 74f334394d13 / 第 1 页 / source_006.png 网格 C1-D3，USB 2.0 HUB |
| U16/U22/U32/U34 | FSW7227YUWQ10G/TR | CM0 USB、HAT USB/GPIO、耳麦触点与 Grove UART/I2C 双通道切换 | 图 74f334394d13 / 第 1 页 / source_006.png 网格 B6-C8，U16; 图 45f4b921b074 / 第 1 页 / source_007.png 网格 C6-D8，U22; 图 554c7022c99c / 第 1 页 / source_009.png 网格 C4-D6，U32; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A7-B8，U34 |
| U17 | MicroSD | 连接 CM0 SDIO 的 microSD 卡座 | 图 74f334394d13 / 第 1 页 / source_006.png 网格 C4-D8，SD 的 U17 |
| U18/U20 | BMI270 / BMM150 | I2C 惯性测量器件及其辅助总线磁力计 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 A5-B8，IMU |
| U19 | RX8130CE:B3 | I2C 实时时钟 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 A1-B4，RTC |
| U21/LED5 | XL-IRM-V838M3/TR / MHS153IRCT | G13_IR_RX 红外接收器与 G12_IR_TX 红外发射 LED | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 B5-C8，IR |
| U23/U35 | AW35112FDR | HAT EXT_5VOUT 与 Grove GROVE_5V 受控负载开关 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 C1-D3，U23; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 B7-C8，U35 |
| U24/U26/U37 | TXB0104RUTR / AW39112DNR | HAT SPI、I2C 与 UART 电平转换器 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 C3-D5，U24/U26/U37 |
| U25/U28/U36 | SSP7615-33DFR | 分别生成 EXT_3V3、AU_3V3 与 CAM_3V3 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 D1-D3，U25; 图 554c7022c99c / 第 1 页 / source_009.png 网格 A1-B3，U28; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 B4-C6，U36 |
| U27 | TCA8418RTWR | 5×10 键盘矩阵扫描控制器 | 图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 C1-D3，U27 |
| S2~S47/D11~D56 | 46 keys / matrix diodes | 带逐键二极管的 46 键矩阵 | 图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 A1-C8，S2~S47 与 D11~D56 |
| U29 | LMA3729T381-OY3S | 板载麦克风 | 图 554c7022c99c / 第 1 页 / source_009.png 网格 A5-B8，U29 |
| U30 | ES8389 | I2C/I2S 音频编解码器 | 图 554c7022c99c / 第 1 页 / source_009.png 网格 B1-C4，U30 |
| U31 | AW8737A | 差分扬声器功率放大器 | 图 554c7022c99c / 第 1 页 / source_009.png 网格 B5-C8，U31 |
| U33 | ME1502AM5G | USB-A 与左侧 USB-C 的常开共享电源开关 | 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A1-B3，U33 |
| J1/J4/USBA1 | USB_C / USB_C / U-A-39WD-W-1 | 右侧 USB-C Device/电源输入与左侧 USB-C、USB-A Host 端口 | 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A1-A3，J1; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A1-C4，J4/USBA1 |
| J3 | HR961160C | 带磁性器件与状态 LED 的 RJ45 连接器 | 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A4-B6，J3 |
| J5 | HDMI-001 19PCBTP | 19 Pin HDMI 输出连接器 | 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 C1-D4，J5 |
| JP2/JP5 | 未标注 | 10 Pin SPI LCD 与 22 Pin 四通道 CSI 摄像头连接器 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 B1-C4，JP2; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 C4-D6，JP5 |
| JP3/JP4 | 未标注 | EXT HAT 2×7 与 Grove 4 Pin 扩展连接器 | 图 45f4b921b074 / 第 1 页 / source_007.png 网格 D6-D8，JP3; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 B7-C8，JP4 |
| CON1/J2 | PJ-342 141 / CON2_SMD | 3.5mm TRRS 耳麦插座与差分扬声器连接器 | 图 554c7022c99c / 第 1 页 / source_009.png 网格 B7-D4，CON1/J2 |
| HAT_BTB/JP1 | AXE512127D / HC-1.25-6PLT | 板对板 HAT 接口与六针电池接口 | 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 C7-D8，HAT_BTB; 图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 B7-C8，JP1 |

## 系统结构

### CardputerZero 系统架构

CM0 连接 HDMI、四通道 MIPI CSI 摄像头、USB 2.0 Host/Device、microSD、SPI LCD、I2C RTC/IMU/键盘/M5IOE1、I2S 音频和 UART/GPIO 扩展；四路 USB Hub 下行用于以太网、USB-A、左侧 USB-C 与 HAT。

- 参数与网络：`core=CM0 132PIN`；`display=SPI0 LCD`；`camera=4-lane MIPI CSI + I2C0`；`storage=microSD SDIO`；`usb=GL852G-OHY60 four-port hub`；`audio=ES8389 + AW8737A`
- 证据：图 c266604db4a2 / 第 1 页 / source_001.png 网格 A1-D8，Block diagram

## 核心器件

### U15 GL852G-OHY60

U15 上行接 HUB_USBD_P/N，下行形成 GL_USB1~GL_USB4；PYG3_KB&HUB_RST 经 R90 10K 控制 RST#，RREF 使用 R89 680R。

- 参数与网络：`upstream=HUB_USBD_P/N`；`downstream=GL_USB1_D_P/N~GL_USB4_D_P/N`；`reset=PYG3_KB&HUB_RST via R90 10K`；`rref=R89 680R`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 C1-D3，USB 2.0 HUB

## 电源

### USB-C 与 EXT 输入

J1 的 USBC_R_IN 经 U2 AW32901FCR 输出 USBC_R_5V，再经 D2 SP1060L 接 VSYS_IN；EXT_5VIN 经 U3 AW32901FCR 输出 VEXT_5V，再经 D3 SS34F 接 VSYS_IN。

- 参数与网络：`usb=J1 USBC_R_IN->U2->USBC_R_5V->D2->VSYS_IN`；`external=EXT_5VIN->U3->VEXT_5V->D3->VSYS_IN`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A1-C4，USB IN 与 EXT. IN

### 充电输入选择

U5 TPS2116DRLR 以 USBC_R_5V 为 VIN1、VEXT_5V 为 VIN2并输出 VCHG_5V；Design Note 明确充电使用独立输入路径且 USB IN 优先于 EXT. IN。

- 参数与网络：`selector=U5 TPS2116DRLR`；`vin1=USBC_R_5V`；`vin2=VEXT_5V`；`output=VCHG_5V`；`priority=USB IN > EXT. IN`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 C1-D4，PATH Switch 与 Design Note

### U1 IP2315

U1 由 VCHG_5V 供电，经 L1 FTC252012S2R2MBCA 与 D1 DSK34 形成 VBAT 充电输出；LED1 红、LED2 绿接状态脚，NTC 接 R9 100K-NTC 与 NTC_CLR。

- 参数与网络：`input=VCHG_5V`；`output=VBAT`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`indicators=LED1 RED,LED2 GREEN`；`temperature=R9 100K-NTC,NTC_CLR`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A5-B8，CHARG

### 电池到 VSYS_IN

VBAT 经 Q3 LP3218DT1G 接入 VSYS_IN；USBC_R_5V 与 EXT_5VIN 分别通过 D4、D5 接入 Q3 控制节点，R30 将该节点下拉。

- 参数与网络：`battery=VBAT`；`switch=Q3 LP3218DT1G`；`output=VSYS_IN`；`external_detect=D4 USBC_R_5V,D5 EXT_5VIN`；`pulldown=R30 10K`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 D3-D5，Q3/D4/D5

### PWR_SW 锁存与检测

SW1 的 3 脚接 VBAT、2 脚输出 SW_EN、1 脚接 GND；SW_EN 经 D6 与 PYG14_PWR_EN 经 D8 汇合成 VSYS_PW_EN，PYG5_PWR_DET 与 G6_SW_DET 分别观察分压后的开关状态。

- 参数与网络：`switch=SW1 K3-1280SK1`；`latch=SW_EN via D6,PYG14_PWR_EN via D8`；`output=VSYS_PW_EN`；`m5io_detect=PYG5_PWR_DET`；`cm0_detect=G6_SW_DET`
- 证据：图 407976133b5d / 第 1 页 / source_004.png 网格 A1-B5，PWR_SW

### VSYS_CM0 与 VSYS_5V

U7 SY7088DGC 由 VSYS_IN 供电、EN 接 VSYS_PW_EN并输出 VSYS_CM0；U8 SY7088DGC 由 VSYS_IN 供电、EN 经 R45 接 VSYS_3V3并输出 VSYS_5V。

- 参数与网络：`u7=VSYS_IN->VSYS_CM0,EN=VSYS_PW_EN`；`u8=VSYS_IN->VSYS_5V,EN=VSYS_3V3 via R45 10K`
- 证据：图 407976133b5d / 第 1 页 / source_004.png 网格 A5-C8，U7/U8

### U10 SY8003

U10 由 VSYS_CM0 供电，CM0_3V3 经 R50 10K 接 EN，L5 与反馈 R51 100K/1%、R53 22.1K/1% 形成 VSYS_3V3；图注 Imax=1A。

- 参数与网络：`input=VSYS_CM0`；`enable=CM0_3V3 via R50 10K`；`output=VSYS_3V3`；`feedback=R51 100K/1%,R53 22.1K/1%`；`imax=1A`
- 证据：图 407976133b5d / 第 1 页 / source_004.png 网格 C5-D8，U10

### 上电顺序与电池功率预算

Power Network 页标注 POWER_SW ON→VSYS_5V→CM0_5V→CM0_3V3→VSYS_3V3→VSYS_5V；仅电池运行时 VSYS_5V 平均总功率 6W、CM0 约 3W、其余输出平均预算小于 3W。

- 参数与网络：`sequence=POWER_SW ON->VSYS_5V->CM0_5V->CM0_3V3->VSYS_3V3->VSYS_5V`；`battery_vsys_5v=6W avg`；`cm0=approximately 3W`；`other_outputs=less than 3W avg`
- 证据：图 c73497cb114d / 第 1 页 / source_002.png 网格 C1-D4，System Power-up Sequence 与 NOTE

### CM0_5V 与 LCD 背光

VSYS_CM0 经 F1 与 U12 AW32901FCR 输出 CM0_5V；U9 AW9967DNR 同样由 VSYS_CM0 供电，PYG10_BL_PWM 控制 FL_LEDA/FL_LEDK 背光回路，R55 为 15R。

- 参数与网络：`cm0_path=VSYS_CM0->F1 0805L100/16AR->U12->CM0_5V`；`backlight_driver=U9 AW9967DNR`；`control=PYG10_BL_PWM`；`led_nets=FL_LEDA/FL_LEDK`；`sense_resistor=R55 15R`
- 证据：图 6e46c6377f56 / 第 1 页 / source_005.png 网格 C1-D3，F1/U12; 图 407976133b5d / 第 1 页 / source_004.png 网格 C1-D4，LCD_BL

### HAT 电源与电平转换

U23 由 PYG13_HAT_EN 控制 VSYS_5V 到 EXT_5VOUT，U25 从 EXT_5VOUT 生成 EXT_3V3；U24/U26/U37 分别将 SPI、I2C、UART 从 VSYS_3V3 域转换到 EXT_3V3 域。

- 参数与网络：`switch=U23 AW35112FDR`；`control=PYG13_HAT_EN`；`output_5v=EXT_5VOUT`；`ldo=U25 SSP7615-33DFR`；`output_3v3=EXT_3V3`；`level_shifters=U24 SPI,U26 I2C,U37 UART`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 C1-D5，HAT.PORT 与电平转换

## 接口

### 左侧 USB-A 与 USB-C

USBA1 使用 GL_USB2_D_P/N，J4 使用 GL_USB3_D_P/N并串 R178/R179 22R与 DR8/DR9 ESD5311；两端口共享电源路径，图注总电流限制 1A且电源为 Only Output。

- 参数与网络：`usb_a=USBA1,GL_USB2_D_P/N`；`usb_c_left=J4,GL_USB3_D_P/N`；`series=R178/R179 22R`；`esd=DR8/DR9 ESD5311`；`current_limit=1A total`；`power_direction=Only Output`
- 证据：图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A1-C4，USBC_L/USBA

### JP2 SPI LCD

JP2 引出 FL_LEDA、FL_LEDK、G5_LCD_TE、G10_SPI0_MOSI、G8_SPI0_CS0、G25_LCD_DC、G11_SPI0_CLK、PYG12_LCD_RST、LCD_3V3 与 GND。

- 参数与网络：`connector=JP2 10-pin`；`mosi=G10_SPI0_MOSI`；`clock=G11_SPI0_CLK`；`cs=G8_SPI0_CS0`；`dc=G25_LCD_DC`；`te=G5_LCD_TE`；`reset=PYG12_LCD_RST`；`backlight=FL_LEDA/FL_LEDK`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 B1-C4，LCD

### JP3 EXT HAT 2×7

JP3.1=HAT_P0、2=HAT_P1、3=GPIO22、4=HAT_SPI0_CLK、5=HAT_SPI0_MOSI、6=HAT_SPI0_MISO、7=HAT_SPI0_CS1、8=HAT_UART_RXD、9=HAT_UART_TXD、10=HAT_I2C1_SCL、11=HAT_I2C1_SDA、12=EXT_5VOUT、13=GND、14=EXT_5VIN。

- 参数与网络：`pins_1_7=1:HAT_P0,2:HAT_P1,3:GPIO22,4:SPI_CLK,5:SPI_MOSI,6:SPI_MISO,7:SPI_CS1`；`pins_8_14=8:UART_RXD,9:UART_TXD,10:I2C_SCL,11:I2C_SDA,12:EXT_5VOUT,13:GND,14:EXT_5VIN`；`series=R108~R119 33R`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 D6-D8，JP3

### Grove UART/I2C 与 5V

U34 将 GROVE_P0/P1 在 G15_UART_RXD/G14_UART_TXD 与 G3_I2C1_SCL/G2_I2C1_SDA 之间切换，G4_GROVE_SW 低选 UART、高选 I2C1；U35 由 PYG4_GROVE_EN 控制 GROVE_5V，图注最大 0.5A。

- 参数与网络：`mux=U34 FSW7227YUWQ10G/TR`；`select=G4_GROVE_SW`；`low=UART`；`high=I2C1`；`power_switch=U35 AW35112FDR`；`power_enable=PYG4_GROVE_EN`；`max_current=0.5A`；`pinout=JP4.4 P0,.3 P1,.2 5V,.1 GND`
- 证据：图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A7-C8，GROVE

### J5 HDMI

J5 引出 HDMI_D0/D1/D2、HDMI_CK、HDMI_CEC、HDMI_SCL/SDA、HDMI_HOTPLUG 与 HDMI_5V；DR12~DR14 ESD0524P 保护信号，D59 DSK34 从 VSYS_5V 向 HDMI_5V 供电。

- 参数与网络：`video=HDMI_D0/D1/D2,HDMI_CK`；`control=CEC,SCL,SDA,HOTPLUG`；`power=VSYS_5V->D59->HDMI_5V`；`esd=DR12~DR14 ESD0524P`
- 证据：图 faa1c2386a42 / 第 1 页 / source_010.png 网格 C1-D4，HDMI

### JP5 CAMERA

JP5 引出 CAM_D0~D3 四组差分数据、CAM_C 差分时钟、CAM_GPIO、SCL0、SDA0、CAM_3V3 与 GND；U36 SSP7615-33DFR 从 VSYS_5V 生成 CAM_3V3。

- 参数与网络：`lanes=CAM_D0_P/N~CAM_D3_P/N`；`clock=CAM_C_P/N`；`control=CAM_GPIO,SCL0,SDA0`；`supply=CAM_3V3`；`regulator=U36 SSP7615-33DFR`
- 证据：图 faa1c2386a42 / 第 1 页 / source_010.png 网格 B4-D6，CAMERA

### HAT_BTB

HAT_BTB 的 AXE512127D 引出 VSYS_3V3、VSYS_5V、G3_I2C1_SCL、G2_I2C1_SDA、VBAT 与 NTC_CLR。

- 参数与网络：`part=AXE512127D`；`rails=VSYS_3V3,VSYS_5V,VBAT`；`signals=G3_I2C1_SCL,G2_I2C1_SDA,NTC_CLR`
- 证据：图 faa1c2386a42 / 第 1 页 / source_010.png 网格 C7-D8，HAT_BTB

## 总线

### USB1 到 100M 以太网

GL_USB1_D_P/N 经 R82/R84 0R 接 U13 SR9900A；DMI0/DMI1 差分对经 ICMF214P101MFR 滤波连接 J3 HR961160C，LAN_LED0/1 驱动 RJ45 指示灯。

- 参数与网络：`usb=GL_USB1_D_P/N`；`controller=U13 SR9900A`；`mdi=DMI0_P/N,DMI1_P/N`；`filter=ICMF214P101MFR`；`connector=J3 HR961160C`；`leds=LAN_LED0,LAN_LED1`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 A4-B8，U13; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A4-B6，J3

### HAT_P0/P1 功能切换

U22 将 HAT_P0/P1 在 GPIO26/GPIO23 与 GL_USB4_D_P/N 之间切换，SEL=PYG1_HAT_SW；低电平选择 GPIO，高电平选择 USB4_D_P/N。

- 参数与网络：`switch=U22 FSW7227YUWQ10G/TR`；`common=HAT_P0/HAT_P1`；`low=GPIO26/GPIO23`；`high=GL_USB4_D_P/N`；`select=PYG1_HAT_SW`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 C6-D8，EXT.HAT-USB

## 总线地址

### U4 BQ27220YZFR

原理图标注 BQ27220YZFR 的 IIC Address:0x55；BQ_I2C1_SCL/SDA 经 U6 AW39112DNR 转换到 G3_I2C1_SCL/G2_I2C1_SDA。

- 参数与网络：`address=0x55`；`local_bus=BQ_I2C1_SCL/BQ_I2C1_SDA`；`system_bus=G3_I2C1_SCL/G2_I2C1_SDA`；`translator=U6 AW39112DNR`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 B5-D8，U4 地址与 U6

### I2C 地址映射

原理图标注 BQ27220YZFR=0x55、M5IOE1=0x4F、TCA8418RTWR=0x34、BMI270=0x68、RX8130CE:B3=0x32、ES8389=0x10；BMM150 接 BMI270 辅助总线但页内未标地址。

- 参数与网络：`BQ27220YZFR=0x55`；`M5IOE1=0x4F`；`TCA8418RTWR=0x34`；`BMI270=0x68`；`RX8130CE:B3=0x32`；`ES8389=0x10`；`BMM150=not annotated`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 B5-C7，0x55; 图 74f334394d13 / 第 1 页 / source_006.png 网格 A1-B3，0x4F; 图 45f4b921b074 / 第 1 页 / source_007.png 网格 A1-B8，0x32/0x68; 图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 C1-D3，0x34; 图 554c7022c99c / 第 1 页 / source_009.png 网格 B1-C4，0x10

## GPIO 与控制信号

### CM0 GPIO 映射

CM0 映射 G20/G21/G18/G19 I2S、G2/G3 I2C1、G7~G11 SPI0、G14/G15 UART、G5_LCD_TE、G25_LCD_DC、G27_KB_INT、G12/G13 IR、G24_SPK_EN、G17_HP_DET、G6_SW_DET、G4_GROVE_SW 与 GPIO22/23/26。

- 参数与网络：`i2c1=G2 SDA,G3 SCL`；`uart=G14 TXD,G15 RXD`；`spi0=G10 MOSI,G9 MISO,G11 CLK,G8 CS0,G7 CS1`；`audio=G20 DIN,G21 DOUT,G19 LRCK,G18 BLCK`；`other=G4,G5,G6,G12,G13,G17,G22,G23,G24,G25,G26,G27`
- 证据：图 c266604db4a2 / 第 1 页 / source_001.png 网格 A5-C8，CM0 信号摘要; 图 6e46c6377f56 / 第 1 页 / source_005.png 网格 A4-C8，U11C/U11D

### M5IOE1 信号映射

U14 输出 PYG8/9/11_KEY_LED、PYG10_BL_PWM、PYG4_GROVE_EN、PYG1_HAT_SW、PYG3_KB&HUB_RST、PYG6_MIC_SW、PYG12_LCD_RST、PYG13_HAT_EN、PYG14_PWR_EN；ADC1/2/3 对应 PYG2_HW_DET、PYG4_GROVE_EN、PYG5_PWR_DET。

- 参数与网络：`leds=PYG8,PYG9,PYG11`；`backlight=PYG10`；`grove_power=PYG4`；`hat_switch=PYG1`；`shared_reset=PYG3`；`mic_switch=PYG6`；`lcd_reset=PYG12`；`hat_power=PYG13`；`power_latch=PYG14`；`adc=PYG2_HW_DET,PYG4_GROVE_EN,PYG5_PWR_DET`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 A1-B3，U14

### 46 键矩阵

S2~S47 共 46 键通过 D11~D56 逐键二极管组成 ROW0~ROW4、COL0~COL9 矩阵；ROW0~ROW3 各 10 键，ROW4 使用 COL0~COL4 与 COL9。

- 参数与网络：`switches=S2~S47`；`diodes=D11~D56`；`keys=46`；`rows=ROW0~ROW4`；`columns=COL0~COL9`；`row4=COL0~COL4,COL9`
- 证据：图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 A1-C8，键矩阵

### TCA8418 键盘控制

U27 使用 ROW0~ROW4、COL0~COL9，ROW5~ROW7 未连接；COL0~COL9 各串 22R，RESET# 接 PYG3_KB&HUB_RST，INT# 输出 G27_KB_INT并由 R124 100K 上拉；LED6~LED8 接 PYG9/8/11。

- 参数与网络：`address=0x34`；`rows=ROW0~ROW4;ROW5~ROW7 NC`；`columns=COL0~COL9 via 22R`；`reset=PYG3_KB&HUB_RST`；`interrupt=G27_KB_INT`；`leds=PYG9_KEY_LED2,PYG8_KEY_LED1,PYG11_KEY_LED3`
- 证据：图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 B5-D3，LED6~8 与 U27

### 耳机检测与扬声器使能

G24_SPK_EN 经 R162 10K 形成 AW_SPK_EN并由 R169 100K 下拉；G17_HP_DET 经 R167 100K 控制 Q7 2N7002KT，Q7 可将 AW_SPK_EN 拉低。

- 参数与网络：`source_enable=G24_SPK_EN`；`amp_enable=AW_SPK_EN`；`detect=G17_HP_DET`；`mute_transistor=Q7 2N7002KT`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 C6-D8，G24/G17/Q7

## 时钟

### USB Hub 与以太网时钟

SR9900A 的 XTAL1/XTAL2 接 X1（XL7EL89CKI-111YLC-25M）及 C60/C61 8pF；GL852G 的 X1/X2 接 X2（X252012MMB4SI-24）及 C75/C76 10pF。

- 参数与网络：`ethernet=X1 XL7EL89CKI-111YLC-25M,C60/C61 8pF`；`hub=X2 X252012MMB4SI-24,C75/C76 10pF`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 A7-B8 与 C2-D3，X1/X2

### U19 RX8130CE:B3

U19 的 VIO 接 VSYS_3V3、VDD 接 VBAT、VBAT 脚经 R95 0R 接 RTC_VCC 与 BAT1 NC；SCL/SDA 接 G3/G2，nIRQ、nRSTO、FOUT 未连接，地址标注 0x32。

- 参数与网络：`address=0x32`；`vio=VSYS_3V3`；`vdd=VBAT`；`backup=RTC_VCC via R95 0R,BAT1 NC`；`bus=G3_I2C1_SCL/G2_I2C1_SDA`；`unused=nIRQ,nRSTO,FOUT`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 A1-B4，RTC

## 复位

### 外设复位

G16_PY32_RST 接 M5IOE1 NRST；PYG3_KB&HUB_RST 同时接 GL852G RST# 与 TCA8418 RESET#；PYG12_LCD_RST 接 LCD JP2。

- 参数与网络：`m5ioe1=G16_PY32_RST`；`usb_hub=PYG3_KB&HUB_RST`；`keyboard=PYG3_KB&HUB_RST`；`lcd=PYG12_LCD_RST`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 A1-C3，U14/U15; 图 2a71cc89b4e7 / 第 1 页 / source_008.png 网格 C1-D3，U27; 图 45f4b921b074 / 第 1 页 / source_007.png 网格 B2-C4，JP2

## 保护电路

### 外部接口 ESD 保护

右侧 USB-C 使用 DR1/DR2 ESD5311，左侧 USB-C 使用 DR8/DR9，USB-A 使用 DR6/DR7，microSD 使用 DR4/DR5 ESD0524P，HDMI 使用 DR12~DR14 ESD0524P，Grove 使用 DR10/DR11 ESD5311。

- 参数与网络：`usb_c_right=DR1/DR2 ESD5311`；`usb_c_left=DR8/DR9 ESD5311`；`usb_a=DR6/DR7 ESD5311`；`microsd=DR4/DR5 ESD0524P`；`hdmi=DR12~DR14 ESD0524P`；`grove=DR10/DR11 ESD5311`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 A1-A3，DR1/DR2; 图 74f334394d13 / 第 1 页 / source_006.png 网格 C6-D8，DR4/DR5; 图 faa1c2386a42 / 第 1 页 / source_010.png 网格 A1-D8，DR6~DR14

## 存储

### U17 microSD

U17 使用 SD_DAT0~3、SD_CMD、SD_CLK 六线 SDIO；SD_3V3 经 FB2 供电，DR4/DR5 ESD0524P 保护信号，RP1/RP2 上拉到 VSYS_3V3，SW 卡检测脚未连接。

- 参数与网络：`bus=SD_DAT0~3,SD_CMD,SD_CLK`；`supply=SD_3V3 via FB2`；`esd=DR4/DR5 ESD0524P`；`pullups=RP1/RP2 YC124-JR-0747KL`；`card_detect=U17.9 SW no-connect`
- 证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 C4-D8，SD

## 音频

### AU_3V3 音频电源

U28 SSP7615-33DFR 从 VSYS_CM0 生成 AU_3V3，EN 由 R138 100K 上拉、R141 100K 下拉；R144 0R 将 GND 与 AGND 相连。

- 参数与网络：`regulator=U28 SSP7615-33DFR`；`input=VSYS_CM0`；`output=AU_3V3`；`enable=R138 100K/R141 100K`；`ground_tie=R144 0R`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 A1-B3，U28

### U30 ES8389

U30 以地址 0x10 接 G2_I2C1_SDA/G3_I2C1_SCL；ES_MIC1_P/N、ES_MIC2_P/N 接模拟输入，DAC_LP/DAC_RP 与 ES_LOUT_P/N 为已连接输出，ES_ROUT_P/N 经 NC 电容终止。

- 参数与网络：`address=0x10`；`i2c=G2_I2C1_SDA/G3_I2C1_SCL`；`inputs=ES_MIC1_P/N,ES_MIC2_P/N`；`headphone=DAC_LP/DAC_RP`；`speaker_line=ES_LOUT_P/N`；`unused=ES_ROUT_P/N via C141/C142 NC`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 B1-C5，U30

### U29 板载麦克风

U29 LMA3729T381-OY3S 由 AU_3V3 经 R139 100R 供电，OUT 经 R140 0R 接 ES_MIC1_P，GND 经 R142/R143 0R 形成 ES_MIC1_N 与 AGND 参考。

- 参数与网络：`microphone=U29 LMA3729T381-OY3S`；`supply=AU_3V3 via R139 100R`；`positive=ES_MIC1_P`；`negative=ES_MIC1_N/AGND`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 A5-B8，U29

### AW8737A 扬声器路径

ES_LOUT_P/N 经 R148/R149 150K 接 U31 AW8737A，AW_SPK_EN 控制 SHDN；VOP/VON 经 FB5/FB6 2.2R 输出 SPK_P/SPK_N 到 J2。

- 参数与网络：`amplifier=U31 AW8737A`；`inputs=ES_LOUT_P/N via R148/R149 150K`；`enable=AW_SPK_EN`；`outputs=SPK_P/SPK_N`；`series=FB5/FB6 2.2R`；`connector=J2`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 B5-C8，U31/J2

### CON1 TRRS 耳麦接口

CON1 的 DAC_LP/DAC_RP 分别经 C144/C146 22uF 与 R163/R168 33R 接耳机触点，HP_P1/HP_P2 接 U32 公共端，插入检测经 R198 0R 输出 G17_HP_DET。

- 参数与网络：`jack=CON1 PJ-342 141`；`left=DAC_LP via C144/R163`；`right=DAC_RP via C146/R168`；`switch_contacts=HP_P1/HP_P2`；`detect=G17_HP_DET via R198 0R`
- 证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 C1-D4，CON1

## 传感器

### BMI270 与 BMM150

U18 BMI270 以 G3_I2C1_SCL/G2_I2C1_SDA 接系统 I2C，SDO 经 R96 10K 接 GND，地址标注 0x68；BMI_SCL/BMI_SDA 辅助总线接 U20 BMM150，BMI270 INT1/INT2 未连接。

- 参数与网络：`imu=U18 BMI270`；`address=0x68`；`system_bus=G3_I2C1_SCL/G2_I2C1_SDA`；`sdo=R96 10K to GND`；`magnetometer=U20 BMM150`；`aux_bus=BMI_SCL/BMI_SDA`；`interrupts=INT1/INT2 no-connect`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 A5-B8，IMU

### 红外收发

U21 XL-IRM-V838M3/TR 由 IR_3V3 供电并输出 G13_IR_RX；LED5 MHS153IRCT 由 VSYS_5V 经 R97 47R 供电，Q5 2N7002KT 由 G12_IR_TX 经 R197 100R 驱动。

- 参数与网络：`receiver=U21 XL-IRM-V838M3/TR`；`rx=G13_IR_RX`；`transmitter=LED5 MHS153IRCT`；`tx=G12_IR_TX`；`driver=Q5 2N7002KT`；`led_resistor=R97 47R`
- 证据：图 45f4b921b074 / 第 1 页 / source_007.png 网格 B5-C8，IR

## 射频

### CM0 Wi-Fi/BT 控制脚

U11D.116 WiFi_ON 与 U11D.117 BT_ON 分别配置 R67/R68 的 NC 下拉选件；十页原理图未绘制独立射频收发器、天线或匹配网络。

- 参数与网络：`wifi_on=U11D.116,R67 NC`；`bt_on=U11D.117,R68 NC`；`external_rf=not shown`
- 证据：图 6e46c6377f56 / 第 1 页 / source_005.png 网格 A7-B8，WiFi_ON/BT_ON

## 调试与烧录

### CM0 启动与参考电压

CM0 引出 RUN_PG、GLOBAL_EN、USB_OTG、RPI_BOOT、VREF_GPIO 与 SD_VREF；TP5/TP6 位于 RUN_PG/GLOBAL_EN，S1 将 RPI_BOOT 接 GND，VREF_GPIO 与 SD_VREF 当前通过 0R 接 CM0_3V3，SD_VREF 到 CM0_1V8 为 NC。

- 参数与网络：`run=U11B.61 RUN_PG,TP5`；`global_enable=U11B.62 GLOBAL_EN,TP6`；`usb_otg=U11B.38`；`boot=U11D.121,S1 to GND`；`vref_gpio=R74 0R to CM0_3V3`；`sd_vref=R75 0R to CM0_3V3,R78 NC to CM0_1V8`
- 证据：图 6e46c6377f56 / 第 1 页 / source_005.png 网格 B2-D8，RUN/BOOT/VREF

## 模拟电路

### BQ27220 电池监测

R15 10mR/1% 串联在 VBAT 与 VBAT_IN 之间，U4 BQ27220YZFR 的 SRN/SRP 跨接分流器，BIN 接 BAT_NTC；JP1 成组引出 VBAT_IN、GND 与 BAT_NTC。

- 参数与网络：`shunt=R15 10mR/1%`；`positive=VBAT`；`negative=VBAT_IN`；`monitor=U4 SRN/SRP`；`temperature=BAT_NTC`；`connector=JP1 HC-1.25-6PLT`
- 证据：图 af8f7c3ac59a / 第 1 页 / source_003.png 网格 B5-C8，BATTERY

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CardputerZero 系统架构 | `core=CM0 132PIN`；`display=SPI0 LCD`；`camera=4-lane MIPI CSI + I2C0`；`storage=microSD SDIO`；`usb=GL852G-OHY60 four-port hub`；`audio=ES8389 + AW8737A` |
| GPIO 与控制信号 | CM0 GPIO 映射 | `i2c1=G2 SDA,G3 SCL`；`uart=G14 TXD,G15 RXD`；`spi0=G10 MOSI,G9 MISO,G11 CLK,G8 CS0,G7 CS1`；`audio=G20 DIN,G21 DOUT,G19 LRCK,G18 BLCK`；`other=G4,G5,G6,G12,G13,G17,G22,G23,G24,G25,G26,G27` |
| 电源 | USB-C 与 EXT 输入 | `usb=J1 USBC_R_IN->U2->USBC_R_5V->D2->VSYS_IN`；`external=EXT_5VIN->U3->VEXT_5V->D3->VSYS_IN` |
| 电源 | 充电输入选择 | `selector=U5 TPS2116DRLR`；`vin1=USBC_R_5V`；`vin2=VEXT_5V`；`output=VCHG_5V`；`priority=USB IN > EXT. IN` |
| 电源 | U1 IP2315 | `input=VCHG_5V`；`output=VBAT`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`indicators=LED1 RED,LED2 GREEN`；`temperature=R9 100K-NTC,NTC_CLR` |
| 模拟电路 | BQ27220 电池监测 | `shunt=R15 10mR/1%`；`positive=VBAT`；`negative=VBAT_IN`；`monitor=U4 SRN/SRP`；`temperature=BAT_NTC`；`connector=JP1 HC-1.25-6PLT` |
| 总线地址 | U4 BQ27220YZFR | `address=0x55`；`local_bus=BQ_I2C1_SCL/BQ_I2C1_SDA`；`system_bus=G3_I2C1_SCL/G2_I2C1_SDA`；`translator=U6 AW39112DNR` |
| 电源 | 电池到 VSYS_IN | `battery=VBAT`；`switch=Q3 LP3218DT1G`；`output=VSYS_IN`；`external_detect=D4 USBC_R_5V,D5 EXT_5VIN`；`pulldown=R30 10K` |
| 电源 | PWR_SW 锁存与检测 | `switch=SW1 K3-1280SK1`；`latch=SW_EN via D6,PYG14_PWR_EN via D8`；`output=VSYS_PW_EN`；`m5io_detect=PYG5_PWR_DET`；`cm0_detect=G6_SW_DET` |
| 系统结构 | 硬件版本电压编码 | `asset_revision=V0.6.1`；`table_revision=V0.6`；`sense_net=PYG2_HW_DET`；`voltage=2.0V`；`divider=R43 120K,R46 75K` |
| 电源 | VSYS_CM0 与 VSYS_5V | `u7=VSYS_IN->VSYS_CM0,EN=VSYS_PW_EN`；`u8=VSYS_IN->VSYS_5V,EN=VSYS_3V3 via R45 10K` |
| 电源 | SY7088 输出电压图注 | `annotated_voltage=5.2V`；`printed_refs=R15/R17`；`u7_feedback=R34 1M/1%,R39 300K/1%`；`u8_feedback=R44 1M/1%,R47 300K/1%` |
| 电源 | U10 SY8003 | `input=VSYS_CM0`；`enable=CM0_3V3 via R50 10K`；`output=VSYS_3V3`；`feedback=R51 100K/1%,R53 22.1K/1%`；`imax=1A` |
| 电源 | 上电顺序与电池功率预算 | `sequence=POWER_SW ON->VSYS_5V->CM0_5V->CM0_3V3->VSYS_3V3->VSYS_5V`；`battery_vsys_5v=6W avg`；`cm0=approximately 3W`；`other_outputs=less than 3W avg` |
| 电源 | CM0_5V 与 LCD 背光 | `cm0_path=VSYS_CM0->F1 0805L100/16AR->U12->CM0_5V`；`backlight_driver=U9 AW9967DNR`；`control=PYG10_BL_PWM`；`led_nets=FL_LEDA/FL_LEDK`；`sense_resistor=R55 15R` |
| 总线 | CM0 USB Host/Device 切换 | `switch=U16 FSW7227YUWQ10G/TR`；`common=CM0_USBD_P/N`；`select=USB_SW`；`low_table=USBC2_D_P/N`；`low_drawn=USB_D_P/N`；`high=HUB_USBD_P/N`；`host_control=USB_SW->Q4->USB_OTG low` |
| 核心器件 | U15 GL852G-OHY60 | `upstream=HUB_USBD_P/N`；`downstream=GL_USB1_D_P/N~GL_USB4_D_P/N`；`reset=PYG3_KB&HUB_RST via R90 10K`；`rref=R89 680R` |
| 接口 | 左侧 USB-A 与 USB-C | `usb_a=USBA1,GL_USB2_D_P/N`；`usb_c_left=J4,GL_USB3_D_P/N`；`series=R178/R179 22R`；`esd=DR8/DR9 ESD5311`；`current_limit=1A total`；`power_direction=Only Output` |
| 总线 | USB1 到 100M 以太网 | `usb=GL_USB1_D_P/N`；`controller=U13 SR9900A`；`mdi=DMI0_P/N,DMI1_P/N`；`filter=ICMF214P101MFR`；`connector=J3 HR961160C`；`leds=LAN_LED0,LAN_LED1` |
| 时钟 | USB Hub 与以太网时钟 | `ethernet=X1 XL7EL89CKI-111YLC-25M,C60/C61 8pF`；`hub=X2 X252012MMB4SI-24,C75/C76 10pF` |
| 存储 | U17 microSD | `bus=SD_DAT0~3,SD_CMD,SD_CLK`；`supply=SD_3V3 via FB2`；`esd=DR4/DR5 ESD0524P`；`pullups=RP1/RP2 YC124-JR-0747KL`；`card_detect=U17.9 SW no-connect` |
| 总线地址 | I2C 地址映射 | `BQ27220YZFR=0x55`；`M5IOE1=0x4F`；`TCA8418RTWR=0x34`；`BMI270=0x68`；`RX8130CE:B3=0x32`；`ES8389=0x10`；`BMM150=not annotated` |
| GPIO 与控制信号 | M5IOE1 信号映射 | `leds=PYG8,PYG9,PYG11`；`backlight=PYG10`；`grove_power=PYG4`；`hat_switch=PYG1`；`shared_reset=PYG3`；`mic_switch=PYG6`；`lcd_reset=PYG12`；`hat_power=PYG13`；`power_latch=PYG14`；`adc=PYG2_HW_DET,PYG4_GROVE_EN,PYG5_PWR_DET` |
| 复位 | 外设复位 | `m5ioe1=G16_PY32_RST`；`usb_hub=PYG3_KB&HUB_RST`；`keyboard=PYG3_KB&HUB_RST`；`lcd=PYG12_LCD_RST` |
| 传感器 | BMI270 与 BMM150 | `imu=U18 BMI270`；`address=0x68`；`system_bus=G3_I2C1_SCL/G2_I2C1_SDA`；`sdo=R96 10K to GND`；`magnetometer=U20 BMM150`；`aux_bus=BMI_SCL/BMI_SDA`；`interrupts=INT1/INT2 no-connect` |
| 时钟 | U19 RX8130CE:B3 | `address=0x32`；`vio=VSYS_3V3`；`vdd=VBAT`；`backup=RTC_VCC via R95 0R,BAT1 NC`；`bus=G3_I2C1_SCL/G2_I2C1_SDA`；`unused=nIRQ,nRSTO,FOUT` |
| 接口 | JP2 SPI LCD | `connector=JP2 10-pin`；`mosi=G10_SPI0_MOSI`；`clock=G11_SPI0_CLK`；`cs=G8_SPI0_CS0`；`dc=G25_LCD_DC`；`te=G5_LCD_TE`；`reset=PYG12_LCD_RST`；`backlight=FL_LEDA/FL_LEDK` |
| 传感器 | 红外收发 | `receiver=U21 XL-IRM-V838M3/TR`；`rx=G13_IR_RX`；`transmitter=LED5 MHS153IRCT`；`tx=G12_IR_TX`；`driver=Q5 2N7002KT`；`led_resistor=R97 47R` |
| GPIO 与控制信号 | 46 键矩阵 | `switches=S2~S47`；`diodes=D11~D56`；`keys=46`；`rows=ROW0~ROW4`；`columns=COL0~COL9`；`row4=COL0~COL4,COL9` |
| GPIO 与控制信号 | TCA8418 键盘控制 | `address=0x34`；`rows=ROW0~ROW4;ROW5~ROW7 NC`；`columns=COL0~COL9 via 22R`；`reset=PYG3_KB&HUB_RST`；`interrupt=G27_KB_INT`；`leds=PYG9_KEY_LED2,PYG8_KEY_LED1,PYG11_KEY_LED3` |
| 接口 | JP3 EXT HAT 2×7 | `pins_1_7=1:HAT_P0,2:HAT_P1,3:GPIO22,4:SPI_CLK,5:SPI_MOSI,6:SPI_MISO,7:SPI_CS1`；`pins_8_14=8:UART_RXD,9:UART_TXD,10:I2C_SCL,11:I2C_SDA,12:EXT_5VOUT,13:GND,14:EXT_5VIN`；`series=R108~R119 33R` |
| 电源 | HAT 电源与电平转换 | `switch=U23 AW35112FDR`；`control=PYG13_HAT_EN`；`output_5v=EXT_5VOUT`；`ldo=U25 SSP7615-33DFR`；`output_3v3=EXT_3V3`；`level_shifters=U24 SPI,U26 I2C,U37 UART` |
| 总线 | HAT_P0/P1 功能切换 | `switch=U22 FSW7227YUWQ10G/TR`；`common=HAT_P0/HAT_P1`；`low=GPIO26/GPIO23`；`high=GL_USB4_D_P/N`；`select=PYG1_HAT_SW` |
| 接口 | Grove UART/I2C 与 5V | `mux=U34 FSW7227YUWQ10G/TR`；`select=G4_GROVE_SW`；`low=UART`；`high=I2C1`；`power_switch=U35 AW35112FDR`；`power_enable=PYG4_GROVE_EN`；`max_current=0.5A`；`pinout=JP4.4 P0,.3 P1,.2 5V,.1 GND` |
| 接口 | J5 HDMI | `video=HDMI_D0/D1/D2,HDMI_CK`；`control=CEC,SCL,SDA,HOTPLUG`；`power=VSYS_5V->D59->HDMI_5V`；`esd=DR12~DR14 ESD0524P` |
| 接口 | JP5 CAMERA | `lanes=CAM_D0_P/N~CAM_D3_P/N`；`clock=CAM_C_P/N`；`control=CAM_GPIO,SCL0,SDA0`；`supply=CAM_3V3`；`regulator=U36 SSP7615-33DFR` |
| 接口 | HAT_BTB | `part=AXE512127D`；`rails=VSYS_3V3,VSYS_5V,VBAT`；`signals=G3_I2C1_SCL,G2_I2C1_SDA,NTC_CLR` |
| 音频 | AU_3V3 音频电源 | `regulator=U28 SSP7615-33DFR`；`input=VSYS_CM0`；`output=AU_3V3`；`enable=R138 100K/R141 100K`；`ground_tie=R144 0R` |
| 音频 | U30 ES8389 | `address=0x10`；`i2c=G2_I2C1_SDA/G3_I2C1_SCL`；`inputs=ES_MIC1_P/N,ES_MIC2_P/N`；`headphone=DAC_LP/DAC_RP`；`speaker_line=ES_LOUT_P/N`；`unused=ES_ROUT_P/N via C141/C142 NC` |
| 音频 | ES8389 I2S/MCLK | `codec_dout=G20_IIS_DIN via R154 33R`；`lrck=G19_IIS_LRCK via R155 33R`；`bclk=G18_IIS_BLCK via R159 33R`；`codec_din=G21_IIS_DOUT via R156 33R`；`mclk=G21_IIS_DOUT->R160 0R->ES_IIS_MLCK->R158 33R` |
| 音频 | U29 板载麦克风 | `microphone=U29 LMA3729T381-OY3S`；`supply=AU_3V3 via R139 100R`；`positive=ES_MIC1_P`；`negative=ES_MIC1_N/AGND` |
| 音频 | AW8737A 扬声器路径 | `amplifier=U31 AW8737A`；`inputs=ES_LOUT_P/N via R148/R149 150K`；`enable=AW_SPK_EN`；`outputs=SPK_P/SPK_N`；`series=FB5/FB6 2.2R`；`connector=J2` |
| 音频 | CON1 TRRS 耳麦接口 | `jack=CON1 PJ-342 141`；`left=DAC_LP via C144/R163`；`right=DAC_RP via C146/R168`；`switch_contacts=HP_P1/HP_P2`；`detect=G17_HP_DET via R198 0R` |
| 音频 | CTIA/OMTP 触点切换 | `switch=U32 FSW7227YUWQ10G/TR`；`select=PYG6_MIC_SW`；`codec_input=ES_MIC2_P via C143 100nF`；`bias=AU_3V3 via R166 10K`；`common=HP_P1/HP_P2`；`logic_mapping=not annotated` |
| GPIO 与控制信号 | 耳机检测与扬声器使能 | `source_enable=G24_SPK_EN`；`amp_enable=AW_SPK_EN`；`detect=G17_HP_DET`；`mute_transistor=Q7 2N7002KT` |
| 调试与烧录 | CM0 启动与参考电压 | `run=U11B.61 RUN_PG,TP5`；`global_enable=U11B.62 GLOBAL_EN,TP6`；`usb_otg=U11B.38`；`boot=U11D.121,S1 to GND`；`vref_gpio=R74 0R to CM0_3V3`；`sd_vref=R75 0R to CM0_3V3,R78 NC to CM0_1V8` |
| 射频 | CM0 Wi-Fi/BT 控制脚 | `wifi_on=U11D.116,R67 NC`；`bt_on=U11D.117,R68 NC`；`external_rf=not shown` |
| 保护电路 | 外部接口 ESD 保护 | `usb_c_right=DR1/DR2 ESD5311`；`usb_c_left=DR8/DR9 ESD5311`；`usb_a=DR6/DR7 ESD5311`；`microsd=DR4/DR5 ESD0524P`；`hdmi=DR12~DR14 ESD0524P`；`grove=DR10/DR11 ESD5311` |

## 待确认事项

- `system.hardware-version-indicator`：当前资源名标识 V0.6.1，但 Hardware Version 表仅将 PYG2_HW_DET=2.0V 对应到 V0.6；该编码是否同样代表 V0.6.1 未在图中说明。（证据：图 407976133b5d / 第 1 页 / source_004.png 网格 B1-C4，Hardware Version 表）
- `power.vsys-output-annotation`：U7 与 U8 区域均标注 Vout=1.2(1+(R15/R17))=5.2V，但实际反馈位号分别为 R34/R39 与 R44/R47；5.2V 数值与公式位号的对应关系不清晰。（证据：图 407976133b5d / 第 1 页 / source_004.png 网格 A5-C8，两处 5.2V 公式）
- `bus.usb-host-device-select`：U16 将 CM0_USBD_P/N 在右侧 USB 分支与 HUB_USBD_P/N 之间切换；低电平真值表写 USBC2_D_P/N，而 U16 分支标为 USB_D_P/N，两个名称是否等同未明确。（证据：图 74f334394d13 / 第 1 页 / source_006.png 网格 B4-C8，USB HOST & Device）
- `audio.codec-i2s-routing`：U30 ASDOUT 接 G20_IIS_DIN、LRCK 接 G19_IIS_LRCK、SCLK 接 G18_IIS_BLCK；G21_IIS_DOUT 一路经 R156 接 DSDIN，另一路经 R160/R158 接 MCLK，单一 G21 同时驱动 DSDIN 与 MCLK 的意图不清晰。（证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 B1-C4，R154~R160）
- `audio.mic-standard-select`：U32 由 PYG6_MIC_SW 选择 HP_P1/HP_P2 与 ES_MIC2_P/麦克风偏置的触点组合；图注只写 OMTP and CTIA，未给出高低电平分别对应哪一种标准。（证据：图 554c7022c99c / 第 1 页 / source_009.png 网格 C4-D6，U32 与图注）
- `review.hardware-version-label`：确认 PYG2_HW_DET=2.0V 的 V0.6 编码是否也适用于当前 V0.6.1。；原因：资源版本字符串与页内硬件版本表不完全一致。
- `review.vsys-formula-refs`：确认 U7/U8 的 5.2V 公式是否应引用 R34/R39 与 R44/R47。；原因：两处公式均写 R15/R17，与相邻反馈位号不符。
- `review.usb-branch-name`：确认 U16 的 USB_D_P/N 与真值表 USBC2_D_P/N 是否为同一右侧 USB-C 数据网络。；原因：同一区域使用了不同网络名。
- `review.es8389-g21-route`：确认 G21_IIS_DOUT 同时连接 ES8389 DSDIN 与 MCLK 是否为有意设计。；原因：R156 与 R160/R158 使同一信号到达两个功能脚。
- `review.mic-switch-logic`：确认 PYG6_MIC_SW 的 LOW/HIGH 分别对应 CTIA 还是 OMTP。；原因：原理图只列出两种标准，未给出逻辑真值表。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c266604db4a27d0bb074ead4f3073e452b4fe50d1aadaff16a3e660594fdd839` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_01.png` |
| 2 | 1 | `c73497cb114d00f40c358ed0f2fbb1b6c8ca37f14a5ea4dd6f941dab77147411` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_02.png` |
| 3 | 1 | `af8f7c3ac59a5ca51d4da0dc869794ac8d1e7486d28a2671d428edfd829e5906` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_03.png` |
| 4 | 1 | `407976133b5d62ff1bd81ec045bced9990e6f43a36f3c33252794953967cfbbe` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_04.png` |
| 5 | 1 | `6e46c6377f569cd16ed829eeb8ff6bc1d71dfecc383652fc200abe4f2664a51e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_05.png` |
| 6 | 1 | `74f334394d1379bd0311bff943d3522e0ec9d8c6bd5014afd7b0d6a7dbf1598b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_06.png` |
| 7 | 1 | `45f4b921b07499dba9b149cae2718fa39f4ee1105ce4fc55ea81899d32011a89` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_07.png` |
| 8 | 1 | `2a71cc89b4e755de3f65dd0a7550b21057e12a4a3e4a1a59455f180e245c265d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_08.png` |
| 9 | 1 | `554c7022c99cb425c9abaef56bd0870e36e6c3c5d55ecb64a039e6210c8f5dc8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_09.png` |
| 10 | 1 | `faa1c2386a4238b9ba0fd6727aca63330c0b137331ac0aa54f4bc4af084f9227` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_10.png` |

---

源文档：`zh_CN/CardputerZero.md`

源文档 SHA-256：`13654c0ea9780a83b4a2f630cb1bb5743a49daef30dcb9a136e326d0a68acb6e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
