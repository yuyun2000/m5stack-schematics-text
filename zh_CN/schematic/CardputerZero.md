# CardputerZero 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CardputerZero |
| SKU | C154 |
| 产品 ID | `cardputerzero-5fe3a896d37a` |
| 源文档 | `zh_CN/CardputerZero.md` |

## 概述

CardputerZero 以 132 Pin CM0 为主控核心，连接 HDMI、4-Lane CSI 摄像头、microSD、SPI LCD、I2C 键盘/IMU/RTC/IO 扩展、I2S 音频和多路 USB。电源由右侧 USB-C 与电池经 IP2315、BQ27220、AW32901FCR 和电源路径管理后形成 VSYS_IN，再由两颗 SY7088 与 SY8003 生成 VSYS_CM0、VSYS_5V 和 VSYS_3V3。GL852G-OHY60 将 CM0 USB 扩展到 SR9900A 百兆以太网、USB-A、左侧 USB-C 和 HAT USB，FSW7227 器件负责 Host/Slave、HAT 与 Grove 功能切换。详细页的 IMU 标为 LSM6DS3TR-C，而正文称 BMI270+BMM150；电源框图音频标为 ES8390、详细页标为 ES8389，两个版本差异需确认。

## 检索关键词

`CardputerZero`、`C154`、`CM0`、`IP2315`、`BQ27220YZFR`、`0x55`、`SY7088DGC`、`SY8003`、`M5IOE1`、`0x4F`、`TCA8418RTWR`、`0x34`、`LSM6DS3TR-C`、`0x68`、`RX8130CE`、`0x32`、`ES8389`、`0x10`、`TPA6130A2RTJR`、`0x60`、`AW8737A`、`GL852G-OHY60`、`SR9900A`、`FSW7227YUWQ10G/TR`、`microSD`、`HDMI`、`MIPI CSI`、`USB Host`、`USB Slave`、`G2_I2C1_SDA`、`G3_I2C1_SCL`、`VSYS_IN`、`VSYS_CM0`、`VSYS_5V`、`VSYS_3V3`、`HAT_P0`、`HAT_P1`、`GROVE_P0`、`GROVE_P1`、`HP_DET`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7A~U7D | CM0 132PIN | 系统主控模块，提供 HDMI、USB、CSI、SDIO、I2C、SPI、UART、I2S 与 GPIO | 图 d7e0ef0e42bc / 第 1 页 / A1-C8：U7A~U7D CM0 1~132 脚 |
| U1（电源页） | IP2315 | USB-C 输入的单节锂电池充电控制器 | 图 f850fac137a9 / 第 1 页 / A2-B4：U1 IP2315、L1、D1、VBAT+ 与 LED1/LED2 |
| U2（电源页） | BQ27220YZFR | 电池电量计，监测 0.01Ω 分流器、VBAT_IN 与 BAT_NTC | 图 f850fac137a9 / 第 1 页 / A6-B8：U2 BQ27220YZFR、R3 0.01R、JP1、ADDR 0X55 |
| U3（电源页） | AW32901FCR | USBC_R_IN 到 USBC_R_5V 的输入过压保护/负载开关 | 图 f850fac137a9 / 第 1 页 / B1-C3：U3 AW32901FCR Power Path Management Circuit |
| U4/U5 | SY7088DGC | 分别生成 VSYS_CM0 与 VSYS_5V 的 5.2V 升降压转换器 | 图 f850fac137a9 / 第 1 页 / B5-D8：U4/U5 SY7088DGC、L2/L3、VSYS_CM0/VSYS_5V |
| U28 | SY8003 | 由 VSYS_IN 生成 VSYS_3V3 的 1A 降压转换器 | 图 f850fac137a9 / 第 1 页 / D5-D8：U28 SY8003、L4、CM0_3V3、VSYS_3V3、Imax=1A |
| U6/U22/U30 | FSW7227YUWQ10G/TR | USB Host/Slave、Grove UART/I2C 和 HAT USB/GPIO 差分/双通道切换器 | 图 f850fac137a9 / 第 1 页 / D1-D3：U6 CM0 USB Host/Slave 切换; 图 6197a8298fac / 第 1 页 / A6-B8：U22 Grove 功能切换; 图 d76b08021a97 / 第 1 页 / D7-D8：U30 HAT_P0/P1 USB/GPIO 切换 |
| U27 | AW32901FCR | VSYS_CM0 到 CM0_5V 的主控电源保护开关 | 图 d7e0ef0e42bc / 第 1 页 / C1-D3：F1、U27 AW32901FCR、VSYS_CM0 与 CM0_5V |
| U23 | TXB0104RUTR | CM0 SPI0 到 HAT_SPI0 的四通道电平转换器 | 图 d7e0ef0e42bc / 第 1 页 / C3-D5：U23 TXB0104RUTR、G10/G11/G7/G9 与 HAT_SPI0 |
| U25 | AW39112DNR | G2/G3 I2C1 到 HAT_I2C1 的双通道电平转换器 | 图 d7e0ef0e42bc / 第 1 页 / D3-D5：U25 AW39112DNR、G2/G3 与 HAT_I2C1 |
| U9 | LSM6DS3TR-C | I2C 惯性传感器，地址图示 0x68 | 图 d7e0ef0e42bc / 第 1 页 / C7-D8：U9 LSM6DS3TR-C、G2/G3、CSB/SDO、IIC Address:0X68 |
| U8 | RX8130CE:B3 | I2C 实时时钟，地址图示 0x32 | 图 d7e0ef0e42bc / 第 1 页 / D6-D8：U8 RX8130CE:B3、RTC_VCC、G2/G3、IIC Address:0X32 |
| U11 | M5IOE1 | I2C GPIO/PWM/ADC 扩展器，控制复位、背光、LED、HAT 和电源状态 | 图 d76b08021a97 / 第 1 页 / A1-B3：U11 M5IOE1、PYG1~PYG14、IIC Address:0X4F |
| U10 | SR9900A | USB 2.0 转 10/100M 以太网控制器 | 图 d76b08021a97 / 第 1 页 / A4-B8：U10 SR9900A、GL_USB1_D_P/N、DMI0/DMI1 与 LAN_LED |
| J3（RJ45） | HR961160C | 带磁性器件和 LED 的 10/100M RJ45 接口 | 图 6197a8298fac / 第 1 页 / A4-B6：J3 HR961160C、RJ_DMI0/1、LAN_LED0/1 |
| U13 | GL852G-OHY60 | 一上行四下行 USB 2.0 Hub | 图 d76b08021a97 / 第 1 页 / B1-D3：U13 GL852G-OHY60、HUB_USBD、GL_USB1~4 |
| U12 | MicroSD | SDIO microSD 卡座 | 图 d76b08021a97 / 第 1 页 / B4-C8：U12 MicroSD、SD_DAT0~3/CMD/CLK、DR4/DR5 |
| JP3 | 未标注 | 10 Pin SPI LCD/背光接口 | 图 d76b08021a97 / 第 1 页 / C4-D6：JP3、G10/G11/G8/G25、PYG5_LCD_RST、LEDK |
| U14 | TCA8418RTWR | 5×10 键盘矩阵扫描控制器，地址图示 0x34 | 图 782b427f5691 / 第 1 页 / C1-D3：U14 TCA8418RTWR、ROW/COL、G2/G3、G27_KB_INT、IIC Address:0X34 |
| S2~S47/D3~D48 | 46 keys / matrix diodes | 46 键、逐键二极管的 5×10 键盘矩阵 | 图 782b427f5691 / 第 1 页 / A1-C8：S2~S47、D3~D48、ROW0~4、COL0~9 |
| U18 | ES8389 | I2C/I2S 音频编解码器，地址图示 0x10 | 图 eb7d4b158c26 / 第 1 页 / B1-C4：U18 ES8389、I2C/I2S、MIC/LINE 与 LOUT/ROUT、IIC Address:0X10 |
| U15 | LMA3729T381-OY3S | 板载麦克风，差分接入 ES_MIC1_P/ES_MIC1_N | 图 eb7d4b158c26 / 第 1 页 / A5-A7：U15 LMA3729T381-OY3S、R79~R82、ES_MIC1_P/N |
| U19 | AW8737A | 差分扬声器功率放大器，输出 SPK_P/SPK_N | 图 eb7d4b158c26 / 第 1 页 / B5-C8：U19 AW8737A、AUDIO_OUT_P/N、AW_SPK_EN、SPK_P/N |
| U20 | TPA6130A2RTJR | I2C 立体声耳机放大器，地址图示 0x60 | 图 eb7d4b158c26 / 第 1 页 / C6-D8：U20 TPA6130A2RTJR、ES_LOUT/ROUT、HPOUT_L/R、IIC Address:0X60 |
| U17 | SN74LVC1G3157DCKR | 由 HP_DET 选择 TPA_SPK_EN/AW_SPK_EN 的模拟开关 | 图 eb7d4b158c26 / 第 1 页 / D3-D5：U17 SN74LVC1G3157DCKR、G24_SPK_EN、HP_DET、TPA_SPK_EN/AW_SPK_EN |
| CON1 | PJ-342 14L CT507452 | 仅 DAC 输出的 3.5mm 耳机接口，带 HP_DET | 图 eb7d4b158c26 / 第 1 页 / C1-D2：CON1 PJ-342、HP_DET、HPOUT_L/R 与注释 |
| U21/U24 | ME1502CM5G / SSP7615-33DFR | 左侧 USB 5V 和摄像头 3.3V 负载开关/LDO | 图 6197a8298fac / 第 1 页 / A1-A3：U21 ME1502CM5G，VSYS_5V 到 USB_5V; 图 6197a8298fac / 第 1 页 / C4-D6：U24 SSP7615-33DFR，G16_CAM_EN、CAM_3V3 |
| U26 | AW35112FDR | 由 G17_GROVE_EN 控制的 GROVE_5V 输出开关 | 图 6197a8298fac / 第 1 页 / B6-B8：U26 AW35112FDR、VSYS_5V、G17_GROVE_EN、GROVE_5V |
| J5/JP6/JP5 | HDMI-001 19PCBTP / Camera 22P / HAT 14P | HDMI、4-Lane CSI 摄像头与 EXT HAT 外部接口 | 图 6197a8298fac / 第 1 页 / C1-D8：J5 HDMI、JP6 Camera、JP5 HAT.PORT |

## 系统结构

### CardputerZero 系统框图

CM0 连接 HDMI、4-Lane CSI CAMERA、USB2.0 Host/Slave、microSD、SPI LCD、I2C RTC/IMU/键盘/IO 扩展、I2S 音频和 UART/GPIO 扩展。USB Hub 四路下行分别用于以太网、USB-A、左侧 USB-C 与 HAT USB。

- 参数与网络：`main=CM0 132PIN`；`usb=U13 GL852G-OHY60 + U10 SR9900A + USB-A/USBC-L/HAT`；`display=SPI LCD`；`camera=4-lane CSI`；`storage=microSD`；`hmi=TCA8418 keyboard, IMU, RTC`；`audio=ES8389/AW8737A/TPA6130A2`
- 证据：图 fcf99e45d46b / 第 1 页 / A1-D8：Block diagram 全页; 图 d76b08021a97 / 第 1 页 / Peripheral 详细页 USB/LAN/SD/LCD/HAT

## 核心器件

### U13 GL852G-OHY60

U13 上行连接 HUB_USBD_P/N，下行 DM1~DM4/DP1~DP4 分别形成 GL_USB1~GL_USB4；PYG6_HUB_RST 控制 RST#，RREF 使用 R54 680Ω。

- 参数与网络：`upstream=HUB_USBD_P/N`；`downstream=GL_USB1_D_P/N,GL_USB2_D_P/N,GL_USB3_D_P/N,GL_USB4_D_P/N`；`reset=PYG6_HUB_RST`；`rref=R54 680R`
- 证据：图 d76b08021a97 / 第 1 页 / B1-D3：U13 USB 2.0 HUB

## 电源

### 右侧 USB-C 充电输入

J1 USB-C 的 DP/DM 经 FL1 共模滤波，CC1/CC2 各经 R12/R13 5.1KΩ到 GND；USBC_R_5V 进入 IP2315 充电器，DR1/DR2 ESD5311 保护 USB 数据线。

- 参数与网络：`connector=J1 USB_C`；`cc=R12 5.1KΩ,R13 5.1KΩ`；`data_filter=FL1 ICMF062P900MFR`；`esd=DR1/DR2 ESD5311`；`charger_input=USBC_R_5V`
- 证据：图 f850fac137a9 / 第 1 页 / A1-B3：J1、FL1、R12/R13、DR1/DR2、USBC_R_5V

### U1 IP2315

IP2315 由 USBC_R_5V 供电，经 L1 FTC252012S2R2MBCA 与 D1 DSK34 形成 VBAT+ 充电输出；LED1 红、LED2 绿连接其状态脚。

- 参数与网络：`input=USBC_R_5V`；`output=VBAT+`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`indicators=LED1 RED,LED2 GREEN`；`charge_set=R14 100K-NTC,R15 82K,R16 15K,R17 NC`
- 证据：图 f850fac137a9 / 第 1 页 / A2-B5：U1 IP2315、L1/D1、VBAT+、LED1/LED2、R14~R17

### USB/电池电源路径管理

U3 AW32901FCR 将 USBC_R_IN 保护后输出 USBC_R_5V，D53 SP5100L 将其送至 VSYS_IN；VBAT+ 通过 Q4/Q3 高边路径接 VSYS_IN，并由 BAT_EN、Q5/Q6 控制。

- 参数与网络：`usb_path=USBC_R_IN-U3 AW32901FCR-USBC_R_5V-D53 SP5100L-VSYS_IN`；`battery_path=VBAT+-Q4/Q3-VSYS_IN`；`control=BAT_EN,Q5/Q6 2N7002KT`
- 证据：图 f850fac137a9 / 第 1 页 / B1-C4：Power Path Management Circuit，U3/D53/Q3~Q6

### PWR_SW

SW1 的 3 脚接 VBAT+、2 脚经 R21 0Ω形成 VSYS_PW_EN、1 脚接 GND，作为系统电源物理开关。

- 参数与网络：`pin_3=VBAT+`；`pin_2=VSYS_PW_EN through R21 0R`；`pin_1=GND`
- 证据：图 f850fac137a9 / 第 1 页 / C3-D4：PWR_SW SW1、R21、VBAT+/VSYS_PW_EN/GND

### U4 SY7088DGC

U4 由 VSYS_IN 供电，EN 经 R23 10KΩ连接 VSYS_PW_EN，输出 VSYS_CM0；反馈 R22 120KΩ/R25 36KΩ，图注 Vout=5.2V。

- 参数与网络：`input=VSYS_IN`；`enable=VSYS_PW_EN via R23 10KΩ`；`output=VSYS_CM0`；`feedback=R22 120KΩ,R25 36KΩ`；`voltage_note=5.2V`
- 证据：图 f850fac137a9 / 第 1 页 / B5-C8：U4、L2、VSYS_IN/VSYS_CM0、SY_FB1

### U5 SY7088DGC

U5 由 VSYS_IN 供电并输出 VSYS_5V，反馈 R26 120KΩ/R136 36KΩ，图注 Vout=5.2V；PYG14_VSYS_EN 经 Q7 参与使能控制。

- 参数与网络：`input=VSYS_IN`；`output=VSYS_5V`；`feedback=R26 120KΩ,R136 36KΩ`；`control=PYG14_VSYS_EN,Q7 2N7002KT`；`voltage_note=5.2V`
- 证据：图 f850fac137a9 / 第 1 页 / C5-D8：U5、L3、Q7、PYG14_VSYS_EN、VSYS_5V

### U28 SY8003

U28 由 VSYS_IN 供电，CM0_3V3 经 R138 10KΩ连接 EN，L4 与反馈 R139 100KΩ/R140 22.1KΩ形成 VSYS_3V3；图注 Imax=1A。

- 参数与网络：`input=VSYS_IN`；`enable=CM0_3V3 via R138 10KΩ`；`output=VSYS_3V3`；`inductor=L4 FTC252012S1R0MBCD`；`feedback=R139 100KΩ,R140 22.1KΩ`；`imax=1A`
- 证据：图 f850fac137a9 / 第 1 页 / D5-D8：U28 SY8003、L4、CM0_3V3、VSYS_3V3

### 系统上电顺序与电池功率预算

电源框图标注 POWER_SW ON→VSYS_5V→CM0_5V→CM0_3V3→VSYS_3V3；仅电池运行时 VSYS_5V 平均总预算 6W，CM0 约 3W，其余输出平均预算小于 3W。

- 参数与网络：`sequence=POWER_SW ON->VSYS_5V->CM0_5V->CM0_3V3->VSYS_3V3`；`battery_vsys_5v_budget=6W avg`；`cm0=about 3W`；`other_outputs=less than 3W avg`
- 证据：图 f311c7985c75 / 第 1 页 / C1-D3：System Power-up Sequence 与 Battery Power Constraint 注释

### GROVE_5V

U26 AW35112FDR 由 VSYS_5V 供电，G17_GROVE_EN 控制 EN，输出 GROVE_5V；图注最大电流不超过 0.5A。

- 参数与网络：`input=VSYS_5V`；`switch=U26 AW35112FDR`；`enable=G17_GROVE_EN`；`output=GROVE_5V`；`max_current=0.5A`
- 证据：图 6197a8298fac / 第 1 页 / B6-B8：U26、GROVE_5V 与 0.5A 注释

## 接口

### USB-A 与左侧 USB-C

USB-A 使用 GL_USB2_D_P/N；左侧 USB-C J4 使用 GL_USB3_D_P/N，经 R145/R146 22Ω与 DR13/DR14 ESD5311；两端口共享 USB_5V，图注总电流限制 1A 且仅输出。

- 参数与网络：`usb_a=GL_USB2_D_P/N`；`usb_c_left=GL_USB3_D_P/N via R145/R146 22R`；`esd=DR13/DR14 ESD5311`；`power=USB_5V`；`limit=USBA+USBC_L 1A`；`mode=Only Output`
- 证据：图 6197a8298fac / 第 1 页 / A1-B4：USBC_L 与 USBA 电路及 Current Limit 1A 注释

### J5 HDMI

J5 引出 HDMI_D0/D1/D2、HDMI_CK、HDMI_CEC、HDMI_SCL/SDA、HOTPLUG 与 HDMI_5V；DR15~DR17 ESD0524P 保护高速/控制信号。

- 参数与网络：`video_pairs=HDMI_D0_P/N,HDMI_D1_P/N,HDMI_D2_P/N,HDMI_CK_P/N`；`control=HDMI_CEC,HDMI_SCL,HDMI_SDA,HDMI_HOTPLUG`；`power=HDMI_5V`；`esd=DR15~DR17 ESD0524P`
- 证据：图 6197a8298fac / 第 1 页 / C1-D3：J5 HDMI-001 19PCBTP 与 DR15~DR17

### JP6 CAMERA

JP6 引出 CAM_D0~D3 四组差分数据、CAM_C 差分时钟、CAM_GPIO、SCL0、SDA0、CAM_3V3 和 GND；U24 由 VSYS_5V 产生 CAM_3V3，G16_CAM_EN 控制 EN。

- 参数与网络：`lanes=CAM_D0_P/N,CAM_D1_P/N,CAM_D2_P/N,CAM_D3_P/N`；`clock=CAM_C_P/N`；`control=CAM_GPIO,SCL0,SDA0`；`power=CAM_3V3`；`regulator=U24 SSP7615-33DFR`；`enable=G16_CAM_EN`
- 证据：图 6197a8298fac / 第 1 页 / C4-D6：U24 与 JP6 CAMERA 22 Pin

### JP3 LCD

LCD 接口使用 G10_SPI0_MOSI、G11_SPI0_CLK、G8_SPI0_CS0、G25_LCD_DC 与 PYG5_LCD_RST；PYG10_BL_PWM 经 Q10 2N7002KT 控制 LEDK 背光。

- 参数与网络：`mosi=G10_SPI0_MOSI`；`sclk=G11_SPI0_CLK`；`cs=G8_SPI0_CS0`；`dc=G25_LCD_DC`；`reset=PYG5_LCD_RST`；`backlight=PYG10_BL_PWM-Q10-LEDK`
- 证据：图 d76b08021a97 / 第 1 页 / C4-D6：LCD JP3、Q10、PYG10_BL_PWM

### Grove UART/I2C 接口

U22 将 GROVE_P0/P1 在 G15_UART_RXD/G14_UART_TXD 与 G3_I2C1_SCL/G2_I2C1_SDA 之间切换，G4_I2C/UART_SW=L 选择 UART、H 选择 I2C1。JP4.4=P0、3=P1、2=GROVE_5V、1=GND。

- 参数与网络：`select=G4_I2C/UART_SW`；`low=UART: G15_RXD/G14_TXD`；`high=I2C1: G3_SCL/G2_SDA`；`pin_4=GROVE_P0`；`pin_3=GROVE_P1`；`pin_2=GROVE_5V`；`pin_1=GND`
- 证据：图 6197a8298fac / 第 1 页 / A6-B8：U22、真值表、U26 与 JP4

### JP5 EXT HAT 14P

JP5.1=HAT_P0，2=HAT_P1，3=GPIO22，4=HAT_SPI0_CLK，5=HAT_SPI0_MOSI，6=HAT_SPI0_MISO，7=HAT_SPI0_CS1，8=G14_UART_TXD，9=G15_UART_RXD，10=HAT_I2C1_SCL，11=HAT_I2C1_SDA，12=GND，13=EXT_5VOUT，14=EXT_5VIN。

- 参数与网络：`pins_1_7=1:HAT_P0,2:HAT_P1,3:GPIO22,4:HAT_SPI0_CLK,5:HAT_SPI0_MOSI,6:HAT_SPI0_MISO,7:HAT_SPI0_CS1`；`pins_8_14=8:G14_UART_TXD,9:G15_UART_RXD,10:HAT_I2C1_SCL,11:HAT_I2C1_SDA,12:GND,13:EXT_5VOUT,14:EXT_5VIN`
- 证据：图 6197a8298fac / 第 1 页 / C6-D8：JP5 HAT.PORT 1~14 脚及 R118~R128

## 总线

### CM0 USB Host/Slave 切换

U6 将 CM0_USBD_P/N 在 HUB_USBD_P/N 与 USB_D_P/N 之间切换，SEL=USB_SW；图面真值表为 USB_SW=L 连接 HUB_USBD_P/N，USB_SW=H 连接 USBC2_D_P/N。

- 参数与网络：`switch=U6 FSW7227YUWQ10G/TR`；`common=CM0_USBD_P/N`；`low=HUB_USBD_P/N`；`high=USBC2_D_P/N`；`select=USB_SW`
- 证据：图 f850fac137a9 / 第 1 页 / D1-D4：U6、SW2、USB_SW Function 表

### USB1 到 100M 以太网

GL_USB1_D_P/N 经 R45/R47 0Ω连接 U10 SR9900A 的 U2DP/U2DM，U10 的 MDI0/MDI1 差分对经共模滤波后连接 RJ_DMI0/RJ_DMI1 与 J3 RJ45。

- 参数与网络：`usb=GL_USB1_D_P/N`；`controller=U10 SR9900A`；`mdi=DMI0_P/N,DMI1_P/N`；`connector=J3 HR961160C`
- 证据：图 d76b08021a97 / 第 1 页 / A4-B8：SR9900A USB TO LAN 100M; 图 6197a8298fac / 第 1 页 / A4-B6：J3 RJ45 磁性接口

### G2/G3 I2C1

G2_I2C1_SDA 与 G3_I2C1_SCL 连接 BQ27220、M5IOE1、TCA8418、LSM6DS3TR-C、RX8130CE、ES8389、TPA6130A2，并通过 U25 转换到 HAT_I2C1。

- 参数与网络：`sda=G2_I2C1_SDA`；`scl=G3_I2C1_SCL`；`devices=BQ27220,M5IOE1,TCA8418,LSM6DS3TR-C,RX8130CE,ES8389,TPA6130A2`；`hat_bridge=U25 AW39112DNR`
- 证据：图 d7e0ef0e42bc / 第 1 页 / B6-D8：CM0 G2/G3、U9/U8/U25; 图 d76b08021a97 / 第 1 页 / A1-B3：M5IOE1 G2/G3; 图 782b427f5691 / 第 1 页 / C1-D3：TCA8418 G2/G3; 图 eb7d4b158c26 / 第 1 页 / B1-D8：ES8389/TPA6130 G2/G3

### HAT_P0/P1 功能切换

U30 将 HAT_P0/P1 在 GPIO26/GPIO23 与 GL_USB4_D_P/N 之间切换，选择网络为 PYG1_HAT_SW。

- 参数与网络：`common=HAT_P0,HAT_P1`；`gpio=GPIO26,GPIO23`；`usb=GL_USB4_D_P,GL_USB4_D_N`；`select=PYG1_HAT_SW`
- 证据：图 d76b08021a97 / 第 1 页 / D7-D8：U30 EXT.HAT-USB

## 总线地址

### U2 BQ27220YZFR

原理图明确标注 BQ27220 的 IIC Address:0X55，SCL/SDA 连接 G3_I2C1_SCL/G2_I2C1_SDA。

- 参数与网络：`address=0x55`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA`
- 证据：图 f850fac137a9 / 第 1 页 / A6-B8：U2 SCL/SDA 与 IIC Address:0X55

### I2C1 地址映射

原理图明确标注 M5IOE1=0x4F、TCA8418=0x34、LSM6DS3TR-C=0x68、RX8130CE=0x32、ES8389=0x10、TPA6130A2=0x60、BQ27220=0x55。

- 参数与网络：`M5IOE1=0x4F`；`TCA8418RTWR=0x34`；`LSM6DS3TR-C=0x68`；`RX8130CE=0x32`；`ES8389=0x10`；`TPA6130A2RTJR=0x60`；`BQ27220YZFR=0x55`
- 证据：图 f850fac137a9 / 第 1 页 / BQ27220 下方 IIC Address:0X55; 图 d7e0ef0e42bc / 第 1 页 / U9/U8 下方 IIC Address:0X68/0X32; 图 d76b08021a97 / 第 1 页 / U11 下方 IIC Address:0X4F; 图 782b427f5691 / 第 1 页 / U14 下方 IIC Address:0X34; 图 eb7d4b158c26 / 第 1 页 / U18/U20 下方 IIC Address:0X10/0X60

## GPIO 与控制信号

### M5IOE1 控制网络

M5IOE1 连接 PYG1_HAT_SW、PYG3_KB_RST、PYG6_HUB_RST、PYG10_BL_PWM、PYG5_LCD_RST、PYG8/9_KEY_LED、PYG14_VSYS_EN，并以 PYG2/4/5 ADC 监测 5V 电源节点。

- 参数与网络：`hat_switch=PYG1_HAT_SW`；`keyboard_reset=PYG3_KB_RST`；`hub_reset=PYG6_HUB_RST`；`backlight=PYG10_BL_PWM`；`lcd_reset=PYG5_LCD_RST`；`key_leds=PYG8_KEY_LED1,PYG9_KEY_LED2`；`vsys_enable=PYG14_VSYS_EN`；`adc=PYG2_5V_ADC,PYG4_USB_DET,PYG5_CM05V_ADC`
- 证据：图 d76b08021a97 / 第 1 页 / A1-B3：U11 M5IOE1 各 PYG 网络与 ADC 分压

### 46 键键盘矩阵

S2~S47 共 46 键通过 D3~D48 逐键二极管组成 ROW0~ROW4、COL0~COL9 矩阵；U14 仅使用 ROW0~4，ROW5~7 未连接，COL0~9 各串联 22Ω。

- 参数与网络：`keys=46`；`switches=S2~S47`；`diodes=D3~D48`；`rows=ROW0~ROW4; ROW5~ROW7 NC`；`columns=COL0~COL9`；`column_resistors=R67,R69,R71~R78 22R`
- 证据：图 782b427f5691 / 第 1 页 / A1-D8：矩阵、U14 与 Keyboard Layout

### TCA8418 控制

U14 RESET# 由 PYG3_KB_RST 经 R64 10KΩ控制，INT# 输出 G27_KB_INT 并由 R65 100KΩ上拉到 VSYS_3V3。

- 参数与网络：`reset=PYG3_KB_RST via R64 10KΩ`；`interrupt=G27_KB_INT`；`interrupt_pullup=R65 100KΩ to VSYS_3V3`
- 证据：图 782b427f5691 / 第 1 页 / C1-D3：U14 RESET#/INT#、R64/R65

### HP_DET 与功放切换

CON1 的 HP_DET 由 R96 1MΩ上拉到 AU_3V3，经 R84 0Ω控制 U17 选择；U17 将 G24_SPK_EN 路由到 TPA_SPK_EN 或 AW_SPK_EN，图注耳机插入会关闭扬声器功放。

- 参数与网络：`detect=HP_DET`；`pullup=R96 1MΩ to AU_3V3`；`switch=U17 SN74LVC1G3157DCKR`；`source=G24_SPK_EN`；`targets=TPA_SPK_EN,AW_SPK_EN`
- 证据：图 eb7d4b158c26 / 第 1 页 / C1-D5：CON1 HP_DET、R96/R84、U17 与注释

## 时钟

### U8 RX8130CE RTC

U8 由 VSYS_3V3 供 VIO/VDD，VBAT 接 RTC_VCC 与 BAT1 SM3R3333 备用储能器件；SCL/SDA 接 G3/G2，nIRQ/nT/FOUT 未连接。

- 参数与网络：`supply=VSYS_3V3`；`backup=RTC_VCC + BAT1 SM3R3333`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA`；`address=0x32`；`unused=nIRQ,nT,FOUT`
- 证据：图 d7e0ef0e42bc / 第 1 页 / D6-D8：RTC 电源、BAT1 与 U8

### USB Hub 与以太网时钟

SR9900A 使用 X1 晶振及 C40/C42 8pF，GL852G 使用 X2 晶振及 C57/C60 10pF；图面未清晰打印可确认的晶振频率。

- 参数与网络：`ethernet=U10 XTAL1/XTAL2-X1-C40/C42 8pF`；`hub=U13 X1/X2-X2-C57/C60 10pF`；`frequency=not legibly printed`
- 证据：图 d76b08021a97 / 第 1 页 / A5-B7：SR9900A X1；C2-D3：GL852G X2

## 复位

### 外设复位网络

PYG3_KB_RST 控制 TCA8418 RESET#，PYG6_HUB_RST 控制 GL852G RST#，PYG5_LCD_RST 连接 LCD 接口；这些网络均由 M5IOE1 输出。

- 参数与网络：`keyboard=PYG3_KB_RST`；`usb_hub=PYG6_HUB_RST`；`lcd=PYG5_LCD_RST`；`controller=U11 M5IOE1`
- 证据：图 d76b08021a97 / 第 1 页 / A1-D6：M5IOE1、USB HUB 与 LCD reset 网络; 图 782b427f5691 / 第 1 页 / C1-D3：TCA8418 RESET#

## 保护电路

### EXT_5VIN 与 USBC_R 并供限制

HAT 页明确警告不得同时通过 USBC_R 和 EXT_5VIN 供电；EXT_5VIN 经 Q13/Q14A/Q14B 路径连接 USBC_R_5V。

- 参数与网络：`warning=Do not supply power through USBC_R and EXT_5VIN at the same time`；`path=EXT_5VIN-Q13/Q14-USBC_R_5V`
- 证据：图 6197a8298fac / 第 1 页 / C6-D8：HAT.PORT 电源路径与红色 WARNING

## 存储

### U12 MicroSD

microSD 使用 CM0 SD_DAT0~3、SD_CMD、SD_CLK 六线 SDIO；SD_3V3 经 FB2 供电，DR4/DR5 ESD0524P 保护信号，卡检测 SW 脚未连接。

- 参数与网络：`bus=SD_DAT0,SD_DAT1,SD_DAT2,SD_DAT3,SD_CMD,SD_CLK`；`supply=SD_3V3 via FB2`；`esd=DR4/DR5 ESD0524P`；`card_detect=U12.9 SW no-connect`
- 证据：图 d76b08021a97 / 第 1 页 / B4-C8：U12 MicroSD、FB2、DR4/DR5、RP1/RP2

## 内存与 Flash

### 系统内存

原理图将处理器和内存封装在 CM0 模块符号内，八张页面未绘制独立外部 RAM 器件或容量标注。

- 参数与网络：`module=CM0`；`external_ram=none shown`；`capacity=not printed on schematic`
- 证据：图 fcf99e45d46b / 第 1 页 / 框图 CM0 模块，未单列 RAM; 图 d7e0ef0e42bc / 第 1 页 / CM0 132 Pin 详细页无外部 RAM

## 音频

### U18 ES8389

ES8389 以地址 0x10 接 G2/G3 I2C；I2S 网络为 G20_IIS_DIN、G19_IIS_LRCK、G21_IIS_DOUT、G18_IIS_BLCK 与 ES_IIS_MCLK，串联 R33/R34/R36/R39/R49/R89 等 33Ω/0Ω电阻。

- 参数与网络：`address=0x10`；`i2c=G2_I2C1_SDA,G3_I2C1_SCL`；`din=G20_IIS_DIN`；`lrck=G19_IIS_LRCK`；`dout=G21_IIS_DOUT`；`bclk=G18_IIS_BLCK`；`mclk=ES_IIS_MCLK`
- 证据：图 eb7d4b158c26 / 第 1 页 / B1-C4：U18 ES8389 数字音频与 I2C 接线

### U15 麦克风输入

U15 LMA3729T381-OY3S 由 AU_3V3 经 R79 100Ω供电，OUT 经 R80 0Ω形成 ES_MIC1_P，GND 经 R81 0Ω形成 ES_MIC1_N；两线经 C90/C92 1uF 接 ES8389 AUDIO_IN_P/N。

- 参数与网络：`microphone=U15 LMA3729T381-OY3S`；`supply=AU_3V3 via R79 100R`；`positive=ES_MIC1_P`；`negative=ES_MIC1_N`；`codec_coupling=C90/C92 1uF to AUDIO_IN_P/N`
- 证据：图 eb7d4b158c26 / 第 1 页 / A5-C4：U15 与 U18 MIC/LINE 输入

### AW8737A 扬声器路径

AUDIO_OUT_P/N 经 C133/C134 33nF 与 R86/R87 150KΩ进入 U19 AW8737A，AW_SPK_EN 控制 SHDN；VOP/VON 经 FB4/FB5 330Ω@100MHz 形成 SPK_P/SPK_N。

- 参数与网络：`inputs=AUDIO_OUT_P/N`；`coupling=C133/C134 33nF,R86/R87 150KΩ`；`enable=AW_SPK_EN`；`outputs=SPK_P/SPK_N`；`beads=FB4/FB5 330R@100MHz`
- 证据：图 eb7d4b158c26 / 第 1 页 / B5-C8：U19 AW8737A 完整功放链

### TPA6130A2 与 3.5mm 输出

U20 以 ES_LOUT_P/N 与 ES_ROUT_P/N 为输入，经 R98/R99 0Ω输出 HPOUT_L/R 到 CON1；TPA_SPK_EN 控制 SD，I2C 地址为 0x60。CON1 注释为仅支持 DAC 输出、不支持 MIC 输入。

- 参数与网络：`amplifier=U20 TPA6130A2RTJR`；`address=0x60`；`inputs=ES_LOUT_P/N,ES_ROUT_P/N`；`outputs=HPOUT_L/R`；`shutdown=TPA_SPK_EN`；`jack=CON1 PJ-342`；`mic_input=not supported`
- 证据：图 eb7d4b158c26 / 第 1 页 / C1-D8：CON1、U17、U20 与 DAC-only 注释

## 传感器

### U9 LSM6DS3TR-C

U9 由 VSYS_3V3 供电，SCL/SDA 接 G3/G2，CSB 接 VSYS_3V3、SDO 接 GND，图示地址 0x68；INT1/INT2、辅助 I2C 与 OCS 脚未连接。

- 参数与网络：`supply=VSYS_3V3`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA`；`csb=VSYS_3V3`；`sdo=GND`；`address=0x68`；`interrupts=INT1/INT2 NC`
- 证据：图 d7e0ef0e42bc / 第 1 页 / C7-D8：U9 完整接线

## 射频

### Wi-Fi/BT 控制

CM0 引出 WiFi_ON 与 BT_ON（U7D.116/117），图中 R100/R103 均为 NC 到 GND；原理图未绘制独立射频收发器、天线或匹配网络。

- 参数与网络：`wifi_on=U7D.116, R100 NC`；`bt_on=U7D.117, R103 NC`；`external_rf=none shown`
- 证据：图 d7e0ef0e42bc / 第 1 页 / B7-C8：WiFi_ON/BT_ON 与 R100/R103 NC

## 调试与烧录

### CM0 启动与调试控制

CM0 提供 RUN、GLOBAL_EN、RPI_BOOT、USB_OTG、VREF_GPIO 和 SD_VREF；S1 将 RPI_BOOT 接 GND，RUN_PG 与 GLOBAL_EN 设测试点，SD_VREF 当前经 R31 0Ω接 CM0_3V3，R35 到 CM0_1V8 为 NC。

- 参数与网络：`boot=RPI_BOOT-S1-GND`；`run=U7B.61 RUN / TP4 RUN_PG`；`global_enable=U7B.62 GLOBAL_EN / TP5`；`usb_otg=U7B.38 via R132 0R`；`vref_gpio=R30 0R to CM0_3V3`；`sd_vref=R31 0R to CM0_3V3; R35 NC to CM0_1V8`
- 证据：图 f850fac137a9 / 第 1 页 / C1-D2：S1 RPI_BOOT 与 U6 USB_OTG; 图 d7e0ef0e42bc / 第 1 页 / B2-D3：RUN/GLOBAL_EN/VREF_GPIO/SD_VREF

## 模拟电路

### BQ27220 电流采样

R3 0.01Ω/1% 串联在 VBAT+ 与 VBAT_IN 之间，U2 BQ27220 的 SRP/SRN 跨接分流器；BIN 连接 BAT_NTC，JP1 引出 VBAT_IN 与 GND。

- 参数与网络：`shunt=R3 0.01R/1%`；`positive=VBAT+`；`negative=VBAT_IN`；`monitor=U2 SRP/SRN`；`temperature=BAT_NTC with R10 10K-NTC`；`battery_connector=JP1 VBAT_IN/GND`
- 证据：图 f850fac137a9 / 第 1 页 / A6-B8：R3、U2 SRP/SRN/BIN、R10、JP1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CardputerZero 系统框图 | `main=CM0 132PIN`；`usb=U13 GL852G-OHY60 + U10 SR9900A + USB-A/USBC-L/HAT`；`display=SPI LCD`；`camera=4-lane CSI`；`storage=microSD`；`hmi=TCA8418 keyboard, IMU, RTC`；`audio=ES8389/AW8737A/TPA6130A2` |
| 电源 | 右侧 USB-C 充电输入 | `connector=J1 USB_C`；`cc=R12 5.1KΩ,R13 5.1KΩ`；`data_filter=FL1 ICMF062P900MFR`；`esd=DR1/DR2 ESD5311`；`charger_input=USBC_R_5V` |
| 电源 | U1 IP2315 | `input=USBC_R_5V`；`output=VBAT+`；`inductor=L1 FTC252012S2R2MBCA`；`diode=D1 DSK34`；`indicators=LED1 RED,LED2 GREEN`；`charge_set=R14 100K-NTC,R15 82K,R16 15K,R17 NC` |
| 模拟电路 | BQ27220 电流采样 | `shunt=R3 0.01R/1%`；`positive=VBAT+`；`negative=VBAT_IN`；`monitor=U2 SRP/SRN`；`temperature=BAT_NTC with R10 10K-NTC`；`battery_connector=JP1 VBAT_IN/GND` |
| 总线地址 | U2 BQ27220YZFR | `address=0x55`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA` |
| 电源 | USB/电池电源路径管理 | `usb_path=USBC_R_IN-U3 AW32901FCR-USBC_R_5V-D53 SP5100L-VSYS_IN`；`battery_path=VBAT+-Q4/Q3-VSYS_IN`；`control=BAT_EN,Q5/Q6 2N7002KT` |
| 电源 | PWR_SW | `pin_3=VBAT+`；`pin_2=VSYS_PW_EN through R21 0R`；`pin_1=GND` |
| 电源 | U4 SY7088DGC | `input=VSYS_IN`；`enable=VSYS_PW_EN via R23 10KΩ`；`output=VSYS_CM0`；`feedback=R22 120KΩ,R25 36KΩ`；`voltage_note=5.2V` |
| 电源 | U5 SY7088DGC | `input=VSYS_IN`；`output=VSYS_5V`；`feedback=R26 120KΩ,R136 36KΩ`；`control=PYG14_VSYS_EN,Q7 2N7002KT`；`voltage_note=5.2V` |
| 电源 | U28 SY8003 | `input=VSYS_IN`；`enable=CM0_3V3 via R138 10KΩ`；`output=VSYS_3V3`；`inductor=L4 FTC252012S1R0MBCD`；`feedback=R139 100KΩ,R140 22.1KΩ`；`imax=1A` |
| 电源 | 系统上电顺序与电池功率预算 | `sequence=POWER_SW ON->VSYS_5V->CM0_5V->CM0_3V3->VSYS_3V3`；`battery_vsys_5v_budget=6W avg`；`cm0=about 3W`；`other_outputs=less than 3W avg` |
| 总线 | CM0 USB Host/Slave 切换 | `switch=U6 FSW7227YUWQ10G/TR`；`common=CM0_USBD_P/N`；`low=HUB_USBD_P/N`；`high=USBC2_D_P/N`；`select=USB_SW` |
| 核心器件 | U13 GL852G-OHY60 | `upstream=HUB_USBD_P/N`；`downstream=GL_USB1_D_P/N,GL_USB2_D_P/N,GL_USB3_D_P/N,GL_USB4_D_P/N`；`reset=PYG6_HUB_RST`；`rref=R54 680R` |
| 总线 | USB1 到 100M 以太网 | `usb=GL_USB1_D_P/N`；`controller=U10 SR9900A`；`mdi=DMI0_P/N,DMI1_P/N`；`connector=J3 HR961160C` |
| 接口 | USB-A 与左侧 USB-C | `usb_a=GL_USB2_D_P/N`；`usb_c_left=GL_USB3_D_P/N via R145/R146 22R`；`esd=DR13/DR14 ESD5311`；`power=USB_5V`；`limit=USBA+USBC_L 1A`；`mode=Only Output` |
| 接口 | J5 HDMI | `video_pairs=HDMI_D0_P/N,HDMI_D1_P/N,HDMI_D2_P/N,HDMI_CK_P/N`；`control=HDMI_CEC,HDMI_SCL,HDMI_SDA,HDMI_HOTPLUG`；`power=HDMI_5V`；`esd=DR15~DR17 ESD0524P` |
| 接口 | JP6 CAMERA | `lanes=CAM_D0_P/N,CAM_D1_P/N,CAM_D2_P/N,CAM_D3_P/N`；`clock=CAM_C_P/N`；`control=CAM_GPIO,SCL0,SDA0`；`power=CAM_3V3`；`regulator=U24 SSP7615-33DFR`；`enable=G16_CAM_EN` |
| 存储 | U12 MicroSD | `bus=SD_DAT0,SD_DAT1,SD_DAT2,SD_DAT3,SD_CMD,SD_CLK`；`supply=SD_3V3 via FB2`；`esd=DR4/DR5 ESD0524P`；`card_detect=U12.9 SW no-connect` |
| 接口 | JP3 LCD | `mosi=G10_SPI0_MOSI`；`sclk=G11_SPI0_CLK`；`cs=G8_SPI0_CS0`；`dc=G25_LCD_DC`；`reset=PYG5_LCD_RST`；`backlight=PYG10_BL_PWM-Q10-LEDK` |
| 总线 | G2/G3 I2C1 | `sda=G2_I2C1_SDA`；`scl=G3_I2C1_SCL`；`devices=BQ27220,M5IOE1,TCA8418,LSM6DS3TR-C,RX8130CE,ES8389,TPA6130A2`；`hat_bridge=U25 AW39112DNR` |
| 总线地址 | I2C1 地址映射 | `M5IOE1=0x4F`；`TCA8418RTWR=0x34`；`LSM6DS3TR-C=0x68`；`RX8130CE=0x32`；`ES8389=0x10`；`TPA6130A2RTJR=0x60`；`BQ27220YZFR=0x55` |
| GPIO 与控制信号 | M5IOE1 控制网络 | `hat_switch=PYG1_HAT_SW`；`keyboard_reset=PYG3_KB_RST`；`hub_reset=PYG6_HUB_RST`；`backlight=PYG10_BL_PWM`；`lcd_reset=PYG5_LCD_RST`；`key_leds=PYG8_KEY_LED1,PYG9_KEY_LED2`；`vsys_enable=PYG14_VSYS_EN`；`adc=PYG2_5V_ADC,PYG4_USB_DET,PYG5_CM05V_ADC` |
| GPIO 与控制信号 | 46 键键盘矩阵 | `keys=46`；`switches=S2~S47`；`diodes=D3~D48`；`rows=ROW0~ROW4; ROW5~ROW7 NC`；`columns=COL0~COL9`；`column_resistors=R67,R69,R71~R78 22R` |
| GPIO 与控制信号 | TCA8418 控制 | `reset=PYG3_KB_RST via R64 10KΩ`；`interrupt=G27_KB_INT`；`interrupt_pullup=R65 100KΩ to VSYS_3V3` |
| 传感器 | U9 LSM6DS3TR-C | `supply=VSYS_3V3`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA`；`csb=VSYS_3V3`；`sdo=GND`；`address=0x68`；`interrupts=INT1/INT2 NC` |
| 传感器 | IMU 型号版本 | `schematic=U9 LSM6DS3TR-C`；`product_document=BMI270+BMM150`；`bmm150_in_schematic=not found` |
| 时钟 | U8 RX8130CE RTC | `supply=VSYS_3V3`；`backup=RTC_VCC + BAT1 SM3R3333`；`scl=G3_I2C1_SCL`；`sda=G2_I2C1_SDA`；`address=0x32`；`unused=nIRQ,nT,FOUT` |
| 音频 | U18 ES8389 | `address=0x10`；`i2c=G2_I2C1_SDA,G3_I2C1_SCL`；`din=G20_IIS_DIN`；`lrck=G19_IIS_LRCK`；`dout=G21_IIS_DOUT`；`bclk=G18_IIS_BLCK`；`mclk=ES_IIS_MCLK` |
| 音频 | U15 麦克风输入 | `microphone=U15 LMA3729T381-OY3S`；`supply=AU_3V3 via R79 100R`；`positive=ES_MIC1_P`；`negative=ES_MIC1_N`；`codec_coupling=C90/C92 1uF to AUDIO_IN_P/N` |
| 音频 | AW8737A 扬声器路径 | `inputs=AUDIO_OUT_P/N`；`coupling=C133/C134 33nF,R86/R87 150KΩ`；`enable=AW_SPK_EN`；`outputs=SPK_P/SPK_N`；`beads=FB4/FB5 330R@100MHz` |
| 音频 | TPA6130A2 与 3.5mm 输出 | `amplifier=U20 TPA6130A2RTJR`；`address=0x60`；`inputs=ES_LOUT_P/N,ES_ROUT_P/N`；`outputs=HPOUT_L/R`；`shutdown=TPA_SPK_EN`；`jack=CON1 PJ-342`；`mic_input=not supported` |
| GPIO 与控制信号 | HP_DET 与功放切换 | `detect=HP_DET`；`pullup=R96 1MΩ to AU_3V3`；`switch=U17 SN74LVC1G3157DCKR`；`source=G24_SPK_EN`；`targets=TPA_SPK_EN,AW_SPK_EN` |
| 音频 | 音频编解码器型号 | `power_block=ES8390`；`detailed_schematic=U18 ES8389`；`detailed_address=0x10` |
| 接口 | Grove UART/I2C 接口 | `select=G4_I2C/UART_SW`；`low=UART: G15_RXD/G14_TXD`；`high=I2C1: G3_SCL/G2_SDA`；`pin_4=GROVE_P0`；`pin_3=GROVE_P1`；`pin_2=GROVE_5V`；`pin_1=GND` |
| 电源 | GROVE_5V | `input=VSYS_5V`；`switch=U26 AW35112FDR`；`enable=G17_GROVE_EN`；`output=GROVE_5V`；`max_current=0.5A` |
| 接口 | JP5 EXT HAT 14P | `pins_1_7=1:HAT_P0,2:HAT_P1,3:GPIO22,4:HAT_SPI0_CLK,5:HAT_SPI0_MOSI,6:HAT_SPI0_MISO,7:HAT_SPI0_CS1`；`pins_8_14=8:G14_UART_TXD,9:G15_UART_RXD,10:HAT_I2C1_SCL,11:HAT_I2C1_SDA,12:GND,13:EXT_5VOUT,14:EXT_5VIN` |
| 总线 | HAT_P0/P1 功能切换 | `common=HAT_P0,HAT_P1`；`gpio=GPIO26,GPIO23`；`usb=GL_USB4_D_P,GL_USB4_D_N`；`select=PYG1_HAT_SW` |
| 保护电路 | EXT_5VIN 与 USBC_R 并供限制 | `warning=Do not supply power through USBC_R and EXT_5VIN at the same time`；`path=EXT_5VIN-Q13/Q14-USBC_R_5V` |
| 调试与烧录 | CM0 启动与调试控制 | `boot=RPI_BOOT-S1-GND`；`run=U7B.61 RUN / TP4 RUN_PG`；`global_enable=U7B.62 GLOBAL_EN / TP5`；`usb_otg=U7B.38 via R132 0R`；`vref_gpio=R30 0R to CM0_3V3`；`sd_vref=R31 0R to CM0_3V3; R35 NC to CM0_1V8` |
| 复位 | 外设复位网络 | `keyboard=PYG3_KB_RST`；`usb_hub=PYG6_HUB_RST`；`lcd=PYG5_LCD_RST`；`controller=U11 M5IOE1` |
| 时钟 | USB Hub 与以太网时钟 | `ethernet=U10 XTAL1/XTAL2-X1-C40/C42 8pF`；`hub=U13 X1/X2-X2-C57/C60 10pF`；`frequency=not legibly printed` |
| 内存与 Flash | 系统内存 | `module=CM0`；`external_ram=none shown`；`capacity=not printed on schematic` |
| 射频 | Wi-Fi/BT 控制 | `wifi_on=U7D.116, R100 NC`；`bt_on=U7D.117, R103 NC`；`external_rf=none shown` |

## 待确认事项

- `sensor.imu-version-conflict`：详细原理图将 U9 标为 LSM6DS3TR-C，产品正文则称 BMI270+BMM150；现有八页中未见 BMI270 或 BMM150 位号，需确认 C154 V0.3 实装型号。（证据：图 d7e0ef0e42bc / 第 1 页 / C7-D8：U9 标注 LSM6DS3TR-C，页面无 BMI270/BMM150; 图 fcf99e45d46b / 第 1 页 / 框图仅标 IMU，不给型号）
- `audio.codec-label-conflict`：电源框图 AUDIO 区标注 ES8390，而音频详细页 U18 明确标注 ES8389 且地址 0x10；应确认框图文字是否为旧版或笔误。（证据：图 f311c7985c75 / 第 1 页 / D3-D4：AUDIO 方框内标注 ES8390; 图 eb7d4b158c26 / 第 1 页 / B1-C4：详细页 U18 标注 ES8389、IIC Address:0X10）
- `review.imu-model`：请确认 C154 V0.3 实装 IMU 是 LSM6DS3TR-C，还是正文中的 BMI270+BMM150 组合，并同步对应资料。；原因：详细原理图与产品正文器件型号不一致，且现有页面未见 BMM150。
- `review.audio-codec-model`：请确认电源框图 ES8390 是否为笔误，当前详细音频页是否以 ES8389 为正式 BOM。；原因：同一原理图资源的框图与详细页标注不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fcf99e45d46bbbf2440d341160b5c734030d6ae5c109b4b23b929660dcba9324` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_01.png` |
| 2 | 1 | `f311c7985c75a53b15440b8098f8ae468c25a026cc33dd1d97a6532a87002291` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_02.png` |
| 3 | 1 | `f850fac137a90a8173bbb3494561b8563d9cab905068bdc1e42772ca99193745` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_03.png` |
| 4 | 1 | `d7e0ef0e42bcc181084e5fc394ade86051bce9300b33099f93b8530e076b4367` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_04.png` |
| 5 | 1 | `d76b08021a97f45c79c76924d89c2f53592464a6cb6c98ea3e9ffd10664e0500` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_05.png` |
| 6 | 1 | `782b427f5691c0f3fa18a2e44abd8889bdc92740a259d07fccae3fb6fdaa82e8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_06.png` |
| 7 | 1 | `eb7d4b158c26d7020c374c45893d99ea1206f4b317bb9d71ed44068b52bd0585` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_07.png` |
| 8 | 1 | `6197a8298facc8d8edf63efa31a1dcaac80217ed8a68ab8ae7bf28ff75f9ac68` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCHE_PRJ_V0.3_20260430_page_08.png` |

---

源文档：`zh_CN/CardputerZero.md`

源文档 SHA-256：`c95e2813ebd5fd9357eb7bd47a203eaedd59e1a2d7524bc1d65b3dbc92718a0d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
