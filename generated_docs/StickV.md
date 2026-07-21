# StickV 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickV |
| SKU | K027 |
| 产品 ID | `stickv-b3c3e7b4b90e` |
| 源文档 | `zh_CN/core/m5stickv.md` |

## 概述

StickV 原理图资源是一张日期为 2020/3/20 的 2x2 拼版，四个分区分别覆盖 AXP192 电源与 SH200Q、K210 电源、K210 Flash 与摄像头接口、K210 GPIO 与显示/音频/USB 外设。图面明确给出 K210、GD25LQ256、26MHz 晶振、AXP192、SH200Q、MP1541、1.14 英寸 IPS 接口、W2SA50TS RGBW LED、Goertek 4737 数字麦克风和 MAX98357。产品源文档另外声明 MPU6886、OV7740、16MB Flash、ST7789 135x240、200mAh 电池、TF 卡、USB Type-C 和 FTDI 驱动，但这些型号或参数在当前图面中缺失或与图面标记不同，因此按版本差异列入待确认。

## 检索关键词

`StickV`、`M5StickV`、`K027`、`Kendryte K210`、`K210`、`AXP192`、`SH200Q`、`MPU6886`、`GD25LQ256`、`16MB Flash`、`OV7740`、`OV-Camera`、`DVP`、`26MHz`、`MP1541`、`MAX98357`、`Goertek 4737`、`W2SA50TS`、`RGBW`、`ZJY_IPS_1.14_LCD`、`ST7789`、`USB Type-C`、`CH552_VCC`、`FTDI`、`TF-card`、`microSD`、`VDD_0.9V`、`VDD_1.5V`、`VDD_1.8V`、`VDD_2.8V`、`VDD_3V3`、`VBAT`、`VUSB`、`VBUS`、`IPSOUT`、`FPIOA`、`SPI`、`I2C`、`I2S`、`UART`、`JTAG`、`MIC_DAT`、`SPK_OUTP`、`SPK_OUTN`、`LCD_SDA`、`MPU_CSB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1A,U1B,U1C | K210 | 主控 SoC，包含 GPIO、DVP、SPI Flash、时钟和多电压电源分区 | 图 4d7945f7a615 / 第 1 页 / 右下分区 U1A、左下分区 U1B、右上分区 U1C |
| U2 | GD25LQ256 | K210 的 1.8V 四线 SPI Flash | 图 4d7945f7a615 / 第 1 页 / 左下分区网格 A2-B3，U2 GD25LQ256 |
| U3 | OV-Camera | DVP 并行摄像头接口模组，带 SCCB 控制与多路电源 | 图 4d7945f7a615 / 第 1 页 / 左下分区网格 B1-D2，U3 OV-Camera |
| U4 | 未标注 | 连接 USB_DP/USB_DM 与 K210 UART、RESET、BOOT 的辅助 MCU，供电网络标为 CH552_VCC | 图 4d7945f7a615 / 第 1 页 / 右下分区网格 A3-A4，U4 与 CH552_VCC/USB_DP/USB_DM |
| U5 | AXP192 | USB、电池和多路系统电源管理器 | 图 4d7945f7a615 / 第 1 页 / 左上分区网格 A1-D2，U5 AXP192 |
| U6 | SH200Q | 六轴传感器，连接 MPU_MISO/CSB/SCK/MOSI 与 MPU_INT | 图 4d7945f7a615 / 第 1 页 / 左上分区网格 B3-B4，U6 SH200Q |
| U7 | MP1541 | 由 IPSOUT 升压生成 VBUS 的转换器 | 图 4d7945f7a615 / 第 1 页 / 左上分区网格 C3-C4，U7 MP1541 |
| U9 | Goertek 4737 | I2S 风格时钟/数据数字麦克风 | 图 4d7945f7a615 / 第 1 页 / 右下分区网格 B3-C3，U9 Goertek 4737 |
| U10 | MAX98357 | I2S 输入的差分 D 类扬声器功放 | 图 4d7945f7a615 / 第 1 页 / 右下分区网格 C2-D3，U10 MAX98357 |
| J1 | ZJY_IPS_1.14_LCD | 1.14 英寸 IPS 显示接口 | 图 4d7945f7a615 / 第 1 页 / 右下分区网格 C1-D2，J1 ZJY_IPS_1.14_LCD |
| LEDx1 | W2SA50TS | 四通道 RGBW LED | 图 4d7945f7a615 / 第 1 页 / 右下分区网格 B3，LEDx1 W2SA50TS |
| X1 | 26MHz/12pF | K210 主晶振 | 图 4d7945f7a615 / 第 1 页 / 左下分区网格 A2-A3，X1 26MHz/12pF |
| J2 | SMT_HDR_2x1.25mm | VBAT 与 GND 两针电池连接器 | 图 4d7945f7a615 / 第 1 页 / 左上分区网格 A2-A3，J2 |
| S1,S2,S3 | SMT_SW_TS_015 | 电源键与两个用户按键 | 图 4d7945f7a615 / 第 1 页 / 左上分区网格 A3-B4，S1-S3 |

## 系统结构

### 原理图拼版结构

本地资源是一张 2x2 拼版，四个标题栏文件分别为 A4-AXP_IMU、A1-PWR、A2-FLASH_CAM 和 A3-K210_IO，日期均为 2020/3/20。

- 参数与网络：`date=2020/3/20`；`sections=A4-AXP_IMU,A1-PWR,A2-FLASH_CAM,A3-K210_IO`
- 证据：图 4d7945f7a615 / 第 1 页 / 四个分区的标题栏

## 核心器件

### K210 主控

U1 由 U1A、U1B、U1C 三个分区组成，图面器件名均标为 K210，覆盖 IO_0 至 IO_47、DVP、SPI3、时钟、复位和多路电源引脚。

- 参数与网络：`reference=U1A,U1B,U1C`；`part_number=K210`；`gpio_range=IO_0-IO_47`；`interfaces=DVP,SPI3,GPIO`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下 U1A、左下 U1B、右上 U1C

## 电源

### K210 电源轨

U1C 的核心 VDD 接 VDD_0.9V，VDDO18 接 VDD_1.8V，部分 VDDIO 组接 VDD_3V3 或 VDD_1.8V；VDDPLL 与 VSSPLL 通过 L2、L3 600R 磁珠滤波。

- 参数与网络：`core=VDD_0.9V`；`io_1v8=VDD_1.8V`；`io_3v3=VDD_3V3`；`pll_filter=L2/L3 600R`
- 证据：图 4d7945f7a615 / 第 1 页 / 右上分区 U1C POWER 与 L1-L3

### 摄像头多路供电

U3 OV-Camera 的 AVDD 接 VDD_2.8V，DVDD 接 VDD_1.5V，DOVDD 接 VDD_1.8V，Y1(AF_VDD) 接 VDD_3V3；DVP-SIO_C 与 DVP-SIO_D 各由 10K 上拉至 VDD_1.8V。

- 参数与网络：`analog=VDD_2.8V`；`core=VDD_1.5V`；`io=VDD_1.8V`；`af=VDD_3V3`；`sccb_pullups=R2/R3 10K to VDD_1.8V`
- 证据：图 4d7945f7a615 / 第 1 页 / 左下分区网格 B1-D2，U3/R2/R3

### AXP192 输入与电池连接

U5 AXP192 的 ACIN 接 VUSB，VBUS 接 VBUS，BAT 两脚接 VBAT；J2 将 VBAT 与 GND 引出为两针电池连接器。

- 参数与网络：`usb_input=VUSB/VBUS`；`battery_net=VBAT`；`battery_connector=J2 SMT_HDR_2x1.25mm`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区网格 A1-B2，U5/J2

### AXP192 系统电源输出

AXP192 DCDC1、DCDC2、DCDC3 分别经 L4、L5、L6 生成 VDD_3V3、VDD_0.9V、VDD_1.8V；LDO1、LDO2、LDO3 分别输出 RTC_VDD、VDD_2.8V、VDD_1.5V。

- 参数与网络：`dcdc1=VDD_3V3 via L4 2.2uH`；`dcdc2=VDD_0.9V via L5 4.7uH`；`dcdc3=VDD_1.8V via L6 4.7uH`；`ldo1=RTC_VDD`；`ldo2=VDD_2.8V`；`ldo3=VDD_1.5V`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区 U5 DCDC1-DCDC3 与 LDO1-LDO3

### MP1541 VBUS 升压

U7 MP1541 以 IPSOUT 为输入，EXT_EN 控制使能，SW 经 L7 6.8uH 与 D4 1N5819 输出 VBUS，反馈分压为 R10 10.2K 与 R12 3.4K。

- 参数与网络：`input=IPSOUT`；`enable=EXT_EN`；`output=VBUS`；`inductor=L7 6.8uH`；`diode=D4 1N5819`；`feedback=R10 10.2K/R12 3.4K`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区网格 C3-C4，U7/L7/D4/R10/R12

## 接口

### 摄像头 DVP 接口

U3 OV-Camera 的 Y2-Y9 连接 K210 DVP_D0-DVP_D7，并引出 DVP_XCLK、PCLK、VSYNC、HREF、PWDN、RESET 以及 DVP-SIO_C/D 控制信号。

- 参数与网络：`data=Y2-Y9 to DVP_D0-DVP_D7`；`clock=DVP_XCLK,DVP_PCLK`；`sync=DVP_VSYNC,DVP_HREF`；`control=DVP_PWDN,DVP_RESET,DVP-SIO_C,DVP-SIO_D`
- 证据：图 4d7945f7a615 / 第 1 页 / 左下分区 U3 OV-Camera 与 U1B DVP IN

### 外部 GPIO

K210 BANK5 的 IO_30 至 IO_35 分别引出为 EXT_IO30 至 EXT_IO35，BANK6 的 IO_38 与 IO_39 引出为 EXTV8_IO38 与 EXTV8_IO39。

- 参数与网络：`bank5=EXT_IO30-EXT_IO35`；`bank6=EXTV8_IO38,EXTV8_IO39`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A1-B1，U1A BANK5/BANK6

### 1.14 英寸 IPS 接口

J1 标为 ZJY_IPS_1.14_LCD，以 VDD_3V3 供电；SDA、SCL、RS、RST、CS 分别连接 K210 IO_18、IO_19、IO_20、IO_21、IO_22，LEDA 接 LCD_BL，LEDK 接地。

- 参数与网络：`part_number=ZJY_IPS_1.14_LCD`；`supply=VDD_3V3`；`sda=IO18`；`scl=IO19`；`dc=IO20`；`reset=IO21`；`cs=IO22`；`backlight=AXP192 GPIO0/LCD_BL`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 B2-D2，U1A BANK3 与 J1

## 总线

### AXP192 控制总线

AXP192 的 SCK、SDA、IRQ 分别连接 INTL_SCL、INTL_SDA、INTL_INT，PWRON 连接 PWR_KEY，GPIO0 连接 LCD_BL。

- 参数与网络：`scl=INTL_SCL`；`sda=INTL_SDA`；`interrupt=INTL_INT`；`power_key=PWR_KEY`；`backlight=GPIO0/LCD_BL`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区 U5 下半部 SCK/SDA/IRQ/PWRON/GPIO0

## GPIO 与控制信号

### K210 GPIO Bank 映射

U1A 标注 GPIO 为 3.3V/1.8V SWITCHABLE，并将 IO_0-5 分配给 K210 JTAG/UART，IO_6-11 分配给 RGBW LED 与 SPK_SD，IO_12-17 分配给麦克风和扬声器，IO_18-23 分配给 LCD 与 INTL_INT。

- 参数与网络：`bank0=IO0-5 JTAG/UART`；`bank1=IO6-11 LED/SPK_SD`；`bank2=IO12-17 MIC/SPK/Ken_BOOT`；`bank3=IO18-23 LCD/INTL_INT`；`voltage=3.3V/1.8V switchable`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A1-C2，U1A BANK0-BANK3

### K210 传感器引脚映射

K210 IO_24、IO_25、IO_26、IO_27 分别连接 MPU_MISO、MPU_CSB、MPU_SCK、MPU_MOSI，IO_28、IO_29 分别连接 INTL_SCL、INTL_SDA，IO_23 连接 INTL_INT。

- 参数与网络：`io24=MPU_MISO`；`io25=MPU_CSB`；`io26=MPU_SCK`；`io27=MPU_MOSI`；`io28=INTL_SCL`；`io29=INTL_SDA`；`io23=INTL_INT`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A1，U1A BANK4 与 IO23

### 用户按键

S2 USER1_KEY 与 S3 USER2_KEY 按下时接地并各带 ESD3/3.3V 保护，分别连接 K210 IO_37 与 IO_36；S1 PWR_KEY 按下接地并连接 AXP192 PWRON。

- 参数与网络：`user1=IO37/S2`；`user2=IO36/S3`；`power=AXP192 PWRON/S1`；`protection=ESD3/3.3V`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区 S1-S3 与右下 U1A IO36/IO37

### RGBW LED

LEDx1 标为 W2SA50TS，W+、G+、R+、B+ 共接 VDD_3V3，W-、R-、G-、B- 分别经 R13-R16 10R 接 LED_W、LED_R、LED_G、LED_B，对应 K210 IO_6、IO_7、IO_8、IO_9。

- 参数与网络：`part_number=W2SA50TS`；`common=VDD_3V3`；`white=IO6 via R13 10R`；`red=IO7 via R14 10R`；`green=IO8 via R15 10R`；`blue=IO9 via R16 10R`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A2-B3，U1A BANK1 与 LEDx1/R13-R16

## 时钟

### K210 26MHz 晶振

X1 标为 26MHz/12pF，XTAL_OUT 与 XTAL_IN 两端各以 C26、C27 12pF 接地，并通过 R1 1M 跨接。

- 参数与网络：`frequency=26MHz`；`load=12pF`；`capacitors=C26/C27 12pF`；`bias_resistor=R1 1M`
- 证据：图 4d7945f7a615 / 第 1 页 / 左下分区网格 A2-A3，X1/R1/C26/C27

## 复位

### K210 复位与启动

K210 RESET 引脚连接 Ken_RST，U1A IO_16 连接 Ken_BOOT；U4 同时连接 Ken_RST 和 Ken_BOOT，Ken_BOOT 由 R4 10K 上拉至 VDD_3V3。

- 参数与网络：`reset=Ken_RST`；`boot=IO16/Ken_BOOT`；`boot_pullup=R4 10K to VDD_3V3`
- 证据：图 4d7945f7a615 / 第 1 页 / 左下 U1B RESET 与右下 U1A IO16/U4/R4

## 存储

### GD25LQ256 Flash 接口

U2 标为 GD25LQ256，以 VDD_1.8V 供电，nCS、CLK、IO0、IO1、IO2、IO3 分别连接 Flash_CS、Flash_CLK、Flash_D0、Flash_D1、Flash_D2、Flash_D3。

- 参数与网络：`part_number=GD25LQ256`；`supply=VDD_1.8V`；`signals=Flash_CS,Flash_CLK,Flash_D0-Flash_D3`
- 证据：图 4d7945f7a615 / 第 1 页 / 左下分区网格 A2-B3，U2

## 音频

### Goertek 4737 数字麦克风

U9 标为 Goertek 4737，以 VDD_3V3 供电，DAT 与 CLK 分别连接 MIC_DAT 与 MIC_CLK，SEL 接地；MIC_DAT 与 MIC_CLK 对应 K210 IO_12 与 IO_13。

- 参数与网络：`part_number=Goertek 4737`；`supply=VDD_3V3`；`data=IO12/MIC_DAT`；`clock=IO13/MIC_CLK`；`select=GND`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 B2-C3，U1A IO12/IO13 与 U9

### MAX98357 I2S 功放

U10 标为 MAX98357，以 IPSOUT 供电，DIN、LRCLK、BCLK 分别连接 SPK_DIN、SPK_LRCLK、SPK_BCLK，SD_MODE 由 SPK_SD 经 R18 600K 驱动，差分输出为 SPK_OUTP 与 SPK_OUTN。

- 参数与网络：`part_number=MAX98357`；`supply=IPSOUT`；`din=IO17/SPK_DIN`；`lrclk=IO14/SPK_LRCLK`；`bclk=IO15/SPK_BCLK`；`shutdown=IO11/SPK_SD via R18 600K`；`outputs=SPK_OUTP,SPK_OUTN`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 B2-D3，U1A BANK1/BANK2 与 U10

## 传感器

### SH200Q 传感器接口

U6 标为 SH200Q，VDDIO 与 VDD 接 VDD_3V3，SDO/A0、SENB、SCK、SDA 分别连接 MPU_MISO、MPU_CSB、MPU_SCK、MPU_MOSI，INT 连接 MPU_INT。

- 参数与网络：`part_number=SH200Q`；`supply=VDD_3V3`；`miso=MPU_MISO`；`cs=MPU_CSB`；`clock=MPU_SCK`；`mosi=MPU_MOSI`；`interrupt=MPU_INT`
- 证据：图 4d7945f7a615 / 第 1 页 / 左上分区网格 B3-B4，U6 SH200Q

## 调试与烧录

### K210 JTAG 与 UART

K210 IO_0、IO_1、IO_2、IO_3 分别连接 Ken_TCLK、Ken_TDI、Ken_TMS、Ken_TDO，IO_4 与 IO_5 分别连接 Ken_RxD 与 Ken_TxD。

- 参数与网络：`jtag=IO0 TCLK,IO1 TDI,IO2 TMS,IO3 TDO`；`uart=IO4 RxD,IO5 TxD`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A2，U1A BANK0

### USB 辅助 MCU

U4 的 USB 数据脚连接 USB_DM 与 USB_DP，串口脚连接 Ken_RxD 与 Ken_TxD，并连接 Ken_RST 与 Ken_BOOT；其两路供电网络标为 CH552_VCC 与 VUSB_VCC。

- 参数与网络：`usb=USB_DM,USB_DP`；`uart=Ken_RxD,Ken_TxD`；`control=Ken_RST,Ken_BOOT`；`supplies=CH552_VCC,VUSB_VCC`
- 证据：图 4d7945f7a615 / 第 1 页 / 右下分区网格 A3-A4，U4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 原理图拼版结构 | `date=2020/3/20`；`sections=A4-AXP_IMU,A1-PWR,A2-FLASH_CAM,A3-K210_IO` |
| 核心器件 | K210 主控 | `reference=U1A,U1B,U1C`；`part_number=K210`；`gpio_range=IO_0-IO_47`；`interfaces=DVP,SPI3,GPIO` |
| 电源 | K210 电源轨 | `core=VDD_0.9V`；`io_1v8=VDD_1.8V`；`io_3v3=VDD_3V3`；`pll_filter=L2/L3 600R` |
| GPIO 与控制信号 | K210 GPIO Bank 映射 | `bank0=IO0-5 JTAG/UART`；`bank1=IO6-11 LED/SPK_SD`；`bank2=IO12-17 MIC/SPK/Ken_BOOT`；`bank3=IO18-23 LCD/INTL_INT`；`voltage=3.3V/1.8V switchable` |
| 时钟 | K210 26MHz 晶振 | `frequency=26MHz`；`load=12pF`；`capacitors=C26/C27 12pF`；`bias_resistor=R1 1M` |
| 复位 | K210 复位与启动 | `reset=Ken_RST`；`boot=IO16/Ken_BOOT`；`boot_pullup=R4 10K to VDD_3V3` |
| 存储 | GD25LQ256 Flash 接口 | `part_number=GD25LQ256`；`supply=VDD_1.8V`；`signals=Flash_CS,Flash_CLK,Flash_D0-Flash_D3` |
| 接口 | 摄像头 DVP 接口 | `data=Y2-Y9 to DVP_D0-DVP_D7`；`clock=DVP_XCLK,DVP_PCLK`；`sync=DVP_VSYNC,DVP_HREF`；`control=DVP_PWDN,DVP_RESET,DVP-SIO_C,DVP-SIO_D` |
| 电源 | 摄像头多路供电 | `analog=VDD_2.8V`；`core=VDD_1.5V`；`io=VDD_1.8V`；`af=VDD_3V3`；`sccb_pullups=R2/R3 10K to VDD_1.8V` |
| 电源 | AXP192 输入与电池连接 | `usb_input=VUSB/VBUS`；`battery_net=VBAT`；`battery_connector=J2 SMT_HDR_2x1.25mm` |
| 电源 | AXP192 系统电源输出 | `dcdc1=VDD_3V3 via L4 2.2uH`；`dcdc2=VDD_0.9V via L5 4.7uH`；`dcdc3=VDD_1.8V via L6 4.7uH`；`ldo1=RTC_VDD`；`ldo2=VDD_2.8V`；`ldo3=VDD_1.5V` |
| 总线 | AXP192 控制总线 | `scl=INTL_SCL`；`sda=INTL_SDA`；`interrupt=INTL_INT`；`power_key=PWR_KEY`；`backlight=GPIO0/LCD_BL` |
| 电源 | MP1541 VBUS 升压 | `input=IPSOUT`；`enable=EXT_EN`；`output=VBUS`；`inductor=L7 6.8uH`；`diode=D4 1N5819`；`feedback=R10 10.2K/R12 3.4K` |
| 传感器 | SH200Q 传感器接口 | `part_number=SH200Q`；`supply=VDD_3V3`；`miso=MPU_MISO`；`cs=MPU_CSB`；`clock=MPU_SCK`；`mosi=MPU_MOSI`；`interrupt=MPU_INT` |
| GPIO 与控制信号 | K210 传感器引脚映射 | `io24=MPU_MISO`；`io25=MPU_CSB`；`io26=MPU_SCK`；`io27=MPU_MOSI`；`io28=INTL_SCL`；`io29=INTL_SDA`；`io23=INTL_INT` |
| GPIO 与控制信号 | 用户按键 | `user1=IO37/S2`；`user2=IO36/S3`；`power=AXP192 PWRON/S1`；`protection=ESD3/3.3V` |
| 接口 | 外部 GPIO | `bank5=EXT_IO30-EXT_IO35`；`bank6=EXTV8_IO38,EXTV8_IO39` |
| 调试与烧录 | K210 JTAG 与 UART | `jtag=IO0 TCLK,IO1 TDI,IO2 TMS,IO3 TDO`；`uart=IO4 RxD,IO5 TxD` |
| 调试与烧录 | USB 辅助 MCU | `usb=USB_DM,USB_DP`；`uart=Ken_RxD,Ken_TxD`；`control=Ken_RST,Ken_BOOT`；`supplies=CH552_VCC,VUSB_VCC` |
| GPIO 与控制信号 | RGBW LED | `part_number=W2SA50TS`；`common=VDD_3V3`；`white=IO6 via R13 10R`；`red=IO7 via R14 10R`；`green=IO8 via R15 10R`；`blue=IO9 via R16 10R` |
| 音频 | Goertek 4737 数字麦克风 | `part_number=Goertek 4737`；`supply=VDD_3V3`；`data=IO12/MIC_DAT`；`clock=IO13/MIC_CLK`；`select=GND` |
| 接口 | 1.14 英寸 IPS 接口 | `part_number=ZJY_IPS_1.14_LCD`；`supply=VDD_3V3`；`sda=IO18`；`scl=IO19`；`dc=IO20`；`reset=IO21`；`cs=IO22`；`backlight=AXP192 GPIO0/LCD_BL` |
| 音频 | MAX98357 I2S 功放 | `part_number=MAX98357`；`supply=IPSOUT`；`din=IO17/SPK_DIN`；`lrclk=IO14/SPK_LRCLK`；`bclk=IO15/SPK_BCLK`；`shutdown=IO11/SPK_SD via R18 600K`；`outputs=SPK_OUTP,SPK_OUTN` |
| 系统结构 | StickV 硬件版本对应关系 | `source_history=2019 initial,2020.3 microphone and IMU update`；`schematic_date=2020/3/20`；`revision=not marked` |
| 传感器 | StickV MPU6886 与 SH200Q | `source_document=MPU6886`；`blue_pcb=I2C SCL28/SDA29`；`black_pcb=SPI/I2C SCL26/SDA27`；`schematic=SH200Q IO24-27,INT IO23` |
| 核心器件 | StickV OV7740 摄像头 | `source_document=OV7740 0.3MP 55deg`；`schematic=OV-Camera generic interface` |
| 存储 | StickV Flash 容量 | `source_document=16MB`；`schematic=GD25LQ256` |
| 核心器件 | StickV ST7789 显示 | `source_document=1.14 inch 135x240 ST7789`；`schematic=ZJY_IPS_1.14_LCD` |
| 电源 | StickV 200mAh 电池 | `source_document=200mAh`；`schematic=VBAT/J2/AXP192` |
| 存储 | StickV TF 卡接口 | `source_document=TF-card microSD`；`schematic=not shown` |
| 接口 | StickV USB Type-C 与 USB 转串口 | `source_document=USB Type-C,FTDI driver`；`schematic=U4 unlabeled,CH552_VCC nets,connector absent` |
| 系统结构 | StickV K210 性能参数 | `source_document=dual-core RV64GC 400MHz,8MB SRAM,0.8TOPS`；`schematic=K210 part marking only` |
| 电源 | StickV 5V 500mA 输入规格 | `source_document=5V@500mA`；`schematic=VUSB/VBUS/AXP192/MP1541` |

## 待确认事项

- `system.hardware-revision`：产品源文档记录 2019 首发、2020.3 增加麦克风并更改 IMU 通信引脚，当前拼版日期为 2020/3/20，但标题栏未标 StickV、K027、PCB 颜色或修订号，无法确认该图对应的具体量产版本。（证据：图 4d7945f7a615 / 第 1 页 / 四个标题栏日期与空白 Revision 字段）
- `sensor.product-imu`：产品源文档规格标注 MPU6886，并区分蓝色 PCB 的 IO28/29 I2C 与黑色 PCB 的 IO26/27 SPI/I2C；当前图面器件标为 SH200Q，连接 IO24-27 与 IO23 中断，实际量产 IMU 及版本映射需确认。（证据：图 4d7945f7a615 / 第 1 页 / 左上 U6 SH200Q 与右下 U1A BANK4）
- `component.product-camera`：产品源文档标注 OV7740、0.3MP 与 55 度 FOV，图面 U3 只标 OV-Camera 并给出 DVP 接口和供电，未标传感器型号、像素或镜头视场。（证据：图 4d7945f7a615 / 第 1 页 / 左下分区 U3 OV-Camera）
- `storage.product-flash-capacity`：产品源文档标注 16MB Flash，图面只标 U2 GD25LQ256 而未直接写出容量，目标产品的实际 Flash 容量和器件版本需确认。（证据：图 4d7945f7a615 / 第 1 页 / 左下分区 U2 GD25LQ256）
- `component.product-display`：产品源文档标注 1.14 英寸 135x240 ST7789，图面只标 J1 ZJY_IPS_1.14_LCD，未标控制器型号和分辨率。（证据：图 4d7945f7a615 / 第 1 页 / 右下分区 J1 ZJY_IPS_1.14_LCD）
- `power.product-battery`：产品源文档标注 200mAh 锂电池，图面只显示 VBAT、AXP192 BAT 引脚和 J2 电池接口，未标容量、标称电压、料号或保护参数。（证据：图 4d7945f7a615 / 第 1 页 / 左上分区 U5 BAT 与 J2）
- `storage.product-microsd`：产品源文档声明 TF-card microSD 外部存储并提供兼容性测试，当前四个原理图分区没有 microSD 卡座或对应信号，接口电路与版本适用性需确认。（证据：图 4d7945f7a615 / 第 1 页 / 四个分区均未画 microSD 卡座）
- `interface.product-usb`：产品源文档标注 USB Type-C 并要求 FTDI 驱动，图面只显示 USB_DP/USB_DM、VUSB/VBUS 和辅助 U4，U4 未标器件型号且没有 USB 连接器符号，实际接口和 USB 转串口方案需确认。（证据：图 4d7945f7a615 / 第 1 页 / 右下分区 U4/USB_DP/USB_DM 与左上 VUSB/VBUS）
- `system.product-performance`：产品源文档标注双核 64 位 RV64GC、400MHz、8MB SRAM 和 0.8TOPS KPU，图面只确认 K210 器件与外部连接，未直接标出这些性能参数。（证据：图 4d7945f7a615 / 第 1 页 / U1A/U1B/U1C K210）
- `power.product-input-rating`：产品源文档标注输入电压 5V@500mA，图面显示 VUSB、VBUS、AXP192 与 MP1541 网络，但未标 USB 输入额定电流或完整连接器端口。（证据：图 4d7945f7a615 / 第 1 页 / 左上分区 U5 AXP192 与 U7 MP1541）
- `review.hardware-revision`：2020/3/20 的 k210_CAMv2 拼版对应 StickV/K027 的哪一 PCB 颜色、批次和修订版本？；原因：标题栏没有产品名或修订号，产品页同时记录 2019 与 2020 两代硬件变化。
- `review.product-imu`：StickV 各 PCB 版本实际装配 MPU6886 还是 SH200Q，蓝色与黑色版本的 IO24-29 映射如何对应？；原因：产品源文档标 MPU6886，当前图面标 SH200Q，且产品页描述两套不同通信引脚。
- `review.product-camera`：U3 OV-Camera 是否固定装配 OV7740，其 0.3MP 和 55 度 FOV 对应哪个镜头与硬件版本？；原因：图面没有标摄像头传感器型号、像素或镜头参数。
- `review.product-flash-capacity`：StickV 实际 Flash 是否为 16MB，U2 GD25LQ256 对应的装配容量和物料版本是什么？；原因：产品页给出容量，图面仅给器件型号而未直接标容量。
- `review.product-display`：J1 ZJY_IPS_1.14_LCD 是否使用 ST7789 135x240 面板，具体屏幕物料是什么？；原因：图面未标控制器型号和分辨率。
- `review.product-battery`：StickV 电池是否为 200mAh，其标称电压、料号和保护参数是什么？；原因：图面只显示 VBAT 网络与 J2，没有电池容量或物料信息。
- `review.product-microsd`：StickV 的 TF-card 卡座、供电和 K210 信号连接位于哪一版原理图？；原因：产品页声明 microSD，但当前四个分区没有相关电路。
- `review.product-usb`：StickV 的 USB 连接器是否为 Type-C，辅助 U4 的具体型号及其与 FTDI 驱动说明的关系是什么？；原因：图面没有 USB 连接器，U4 无器件值，但电源网名包含 CH552_VCC，产品页却说明 FTDI 驱动。
- `review.product-performance`：StickV 量产配置是否确认为双核 RV64GC 400MHz、8MB SRAM 和 0.8TOPS KPU？；原因：参数来自产品源文档，当前原理图未直接标出。
- `review.product-input-rating`：StickV 的 USB 输入是否为 5V@500mA，完整连接器、电源路径和保护电路是什么？；原因：图面只有 VUSB/VBUS 电源网络，没有端口额定值或完整连接器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4d7945f7a61579ee2853d3afe73bf33d057f7aab40936b5c21c8076ce6defbf8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/k210_CAMv2_page_01.png` |

---

源文档：`zh_CN/core/m5stickv.md`

源文档 SHA-256：`0d85a42b3972bbc460be22eec2eab1bb568a7590f61e55dd18da51e0f8f8716c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
