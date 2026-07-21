# Core2 For AWS v1.3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core2 For AWS v1.3 |
| SKU | K010-AWS-V13 |
| 产品 ID | `core2-for-aws-v1-3-9e942e074984` |
| 源文档 | `zh_CN/core/Core2_For_AWS_v1.3.md` |

## 概述

该产品资源由 CORE2_V1.0 主板总图与 M5GO Bottom2 v1.3 AWS 底座图组成。主板包含 ESP32-D0WDQ6、外部 Flash/PSRAM、AXP192 电源、LCD/触摸、CP2104 USB-UART、NS4168 音频、BM8563 RTC、microSD 与 M5-Bus；底座集成 BMI270、ATECC608B、数字麦克风、10 颗 SK6812、TP4057 充电和 UART/GPIO/I2C 扩展接口。

## 检索关键词

`Core2 For AWS v1.3`、`K010-AWS-V13`、`CORE2_V1.0`、`M5GO Bottom2 v1.3`、`ESP32-D0WDQ6`、`AXP192`、`XM25QH128B`、`ESPPSRAM64H`、`CP2104-F03-GMR`、`NS4168`、`BM8563`、`SY7088`、`M5_CORE2_LCD_10P`、`CTP_2.0inch`、`BMI270`、`0x68`、`ATECC608B`、`LMD4737T261`、`SK6812`、`TP4057`、`M5-Bus`、`GPIO21`、`GPIO22`、`SYS_SDA`、`SYS_SCL`、`BUS_5V`、`SYS_VBAT`、`AWS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 (MCU) | ESP32-D0WDQ6 | Core2 主控制器 | 图 6c305db1571c / 第 1 页 / A2-C3 MCU 区域 U2 主控符号，器件值标注 ESP32-D0WDQ6 |
| U4 | AXP192 | Core2 多路电源管理芯片 | 图 6c305db1571c / 第 1 页 / A1-C2 PMU 区域 U4 AXP192 及 DCDC/LDO/GPIO 输出 |
| U1 (Flash) | XM25QH128B | ESP32 外部 SPI Flash | 图 6c305db1571c / 第 1 页 / D1 FLASH 区域 U1 XM25QH128B，连接 GPIO6-11 |
| U2 (PSRAM) | ESPPSRAM64H | ESP32 外部 PSRAM | 图 6c305db1571c / 第 1 页 / D1 PSRAM 区域 U2 ESPPSRAM64H，连接 GPIO6-10 和 GPIO17 |
| U3 (USB-UART) | CP2104-F03-GMR | Core2 USB-UART 桥接器 | 图 6c305db1571c / 第 1 页 / C1-D1 USB2UART 区域 U3 CP2104-F03-GMR |
| U6 | NS4168 | I2S/数字音频扬声器功率放大器 | 图 6c305db1571c / 第 1 页 / C2 SPEAKER 区域 U6 NS4168 与 PADA1 SPEAKER_PAD |
| U5 | BM8563 | RTC 实时时钟 | 图 6c305db1571c / 第 1 页 / D1-D2 RTC 区域 U5 BM8563、X1 32.768K 和 BT1 |
| U8 | SY7088 | M5-Bus 5 V 升压转换器 | 图 6c305db1571c / 第 1 页 / C2-C3 5V_BOOST 区域 U8 SY7088，IPS_BUS 输入、BUS_5V 输出 |
| LCD1 | M5_CORE2_LCD_10P | Core2 SPI LCD 模块 | 图 6c305db1571c / 第 1 页 / B4-C4 LCD 区域 LCD1 M5_CORE2_LCD_10P |
| CTP1 | CTP_2.0inch | 2.0 英寸电容触摸模块 | 图 6c305db1571c / 第 1 页 / C4-D4 C-TP 区域 CTP1 CTP_2.0inch |
| BUS1 | M5_BUS | 30 Pin M5-Bus 主板扩展连接器 | 图 6c305db1571c / 第 1 页 / A3-B3 BUS1 M5_BUS 完整 1-30 脚定义 |
| LED1-LED10 | SK6812 | AWS Bottom2 串联 RGB LED | 图 7343f6f305ba / 第 1 页 / A1-A4 RGB LED *10 区域 LED1-LED10 SK6812 级联 |
| U1 (Bottom IMU) | BMI270 | AWS Bottom2 六轴 IMU | 图 7343f6f305ba / 第 1 页 / B2-B3 U1 BMI270、I2C_SDA/I2C_SCL 与地址选择 |
| U2 (Bottom microphone) | LMD4737T261 | AWS Bottom2 数字麦克风 | 图 7343f6f305ba / 第 1 页 / B1-B2 Microphone 区域 U2 LMD4737T261，输出 DAT/CLK |
| U4 (Bottom security) | ATECC608B | AWS Bottom2 硬件安全/加密器件 | 图 7343f6f305ba / 第 1 页 / D2-D3 U4 ATECC608B，连接 I2C_SCL/I2C_SDA |
| U3 (Bottom charger) | TP4057 | AWS Bottom2 电池充电芯片 | 图 7343f6f305ba / 第 1 页 / C1-D2 Power 区域 U3 TP4057，VIN 输入、BAT+ 输出 |
| J4 | M5Stack_BUS2 | AWS Bottom2 30 Pin M5-Bus 底座连接器 | 图 7343f6f305ba / 第 1 页 / C3-D4 J4 M5Stack_BUS2 及 RGB、UART、I2C、麦克风、5V、BAT+ 信号 |

## 系统结构

### 资源版本范围

本产品资源组合包含 CORE2_V1.0 主板原理图和 M5GO Bottom2 v1.3 AWS Version 底座原理图，结构化事实分别保留两张图的器件与网络边界。

- 参数与网络：`core_asset=CORE2_V1.0_SCH`；`bottom_asset=M5GO_Bottom2_SCH_Main_V1.3_AWS_Version`
- 证据：图 6c305db1571c / 第 1 页 / Core2 主板总图，包含 PMU、MCU、USB2UART、LCD、M5_BUS 等功能区; 图 7343f6f305ba / 第 1 页 / AWS Bottom2 底座总图，包含 RGB LED、Microphone、BMI270、ATECC608B 和 M5Bus

### Core2 主控制器

随附 CORE2_V1.0 主板图将 U2 标注为 ESP32-D0WDQ6，并引出 GPIO0-39、CHIP_PU、XTAL、VDD_SDIO 与 CAP1/CAP2。

- 参数与网络：`reference=U2`；`part_number=ESP32-D0WDQ6`；`schematic=CORE2_V1.0`
- 证据：图 6c305db1571c / 第 1 页 / A2-C3 MCU 区域 U2 ESP32-D0WDQ6 主控符号

## 核心器件

### ATECC608B 安全器件

U4 ATECC608B 由 3.3 V 供电，并通过 I2C_SCL/I2C_SDA 接入 AWS Bottom2 的 I2C 总线。

- 参数与网络：`reference=U4`；`part_number=ATECC608B`；`supply=+3.3V`；`scl=I2C_SCL`；`sda=I2C_SDA`
- 证据：图 7343f6f305ba / 第 1 页 / D2-D3 U4 ATECC608B、+3.3V、I2C_SCL/I2C_SDA

## 电源

### AXP192 电源树

U4 AXP192 的 DCDC1 经 L3 2.2 µH 生成 MCU_VDD，DCDC3 经 L2 2.2 µH 生成 LCD_BL；LDO1、LDO2、LDO3 分别输出 RTC_VDD、PERI_VDD、VIB_MOTOR，IPSOUT 输出 IPS_BUS。

- 参数与网络：`dcdc1=MCU_VDD via L3 2.2uH`；`dcdc3=LCD_BL via L2 2.2uH`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS`
- 证据：图 6c305db1571c / 第 1 页 / A1-C2 PMU 区域 U4 AXP192 的 DCDC1/DCDC3/LDO1/LDO2/LDO3/IPSOUT 网络

### M5-Bus 5 V 升压

U8 SY7088 以 IPS_BUS 为输入，经 L4 2.2 µH 生成 BUS_5V，并由 BST_EN 控制 EN。

- 参数与网络：`reference=U8`；`part_number=SY7088`；`input=IPS_BUS`；`output=BUS_5V`；`inductor=L4 2.2uH`；`enable=BST_EN`
- 证据：图 6c305db1571c / 第 1 页 / C2-C3 5V_BOOST 区域 U8 SY7088、L4、BST_EN 与 BUS_5V

### AWS Bottom2 充电电路

U3 TP4057 的 VCC 接 VIN，BAT 输出 BAT+，PROG 经 R9 2 kΩ 接地；D1 1615RG 与 R6 1 kΩ 连接 CHRG/STDBY 状态端。

- 参数与网络：`charger=U3 TP4057`；`input=VIN`；`battery_output=BAT+`；`program_resistor=R9 2k`；`status_led=D1 1615RG via R6 1k`
- 证据：图 7343f6f305ba / 第 1 页 / C1-D2 Power 区域 U3 TP4057、D1、R6/R9、VIN 与 BAT+

## 接口

### Core2 USB-UART

U3 CP2104-F03-GMR 的 DP/DM 连接 SYS_DP/SYS_DM，TXD 输出 CP_TX 并经 R7 47 Ω 接 GPIO3，RXD 输入 CP_RX 并经 R8 47 Ω 接 GPIO1；DTR/RTS 通过 Q1/Q2 8050 自动控制 MCU_RST 与 GPIO0。

- 参数与网络：`bridge=CP2104-F03-GMR`；`usb_dp=SYS_DP`；`usb_dm=SYS_DM`；`uart_tx=GPIO3 via R7 47R`；`uart_rx=GPIO1 via R8 47R`；`auto_download=DTR/RTS via Q1/Q2 8050 to MCU_RST/GPIO0`
- 证据：图 6c305db1571c / 第 1 页 / C1-D1 USB2UART 区域 U3、R7/R8、Q1/Q2 与 MCU_RST/GPIO0 网络

### USB Type-C 接口

J3 TYPEC_16P 的 DP1/DP2 接 USB_DP、DN1/DN2 接 USB_DM，CC1/CC2 各经 5.1 kΩ 电阻接地，VBUS 经 FU1 1 A/6 V 保险器形成 USB_5V。

- 参数与网络：`connector=J3 TYPEC_16P`；`usb_dp=USB_DP`；`usb_dm=USB_DM`；`cc_pulldowns=R32=5.1k,R33=5.1k`；`fuse=FU1 1A/6V`；`supply=USB_5V`
- 证据：图 6c305db1571c / 第 1 页 / A3-B3 USB 区域 J3 TYPEC_16P、R32/R33、FU1 与 USB_DP/DM/5V

### Core2 LCD

LCD1 的 MOSI=GPIO23、MISO=GPIO38、SCK=GPIO18、CS=GPIO5、RST=LCD_RST、D/C=GPIO15、LED_A=LCD_BL，VDD 连接 PERI_VDD。

- 参数与网络：`mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`chip_select=GPIO5`；`reset=LCD_RST`；`data_command=GPIO15`；`backlight=LCD_BL`；`supply=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / B4-C4 LCD1 M5_CORE2_LCD_10P 引脚网络

### Core2 电容触摸

CTP1 的 SDA=GPIO21、SCL=GPIO22、INT=GPIO39、RST=LCD_RST，VDD 经 R65 47 Ω 接 MCU_VDD。

- 参数与网络：`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=LCD_RST`；`supply=MCU_VDD via R65 47R`
- 证据：图 6c305db1571c / 第 1 页 / C4-D4 CTP1 CTP_2.0inch 引脚网络

### Core2 30 Pin M5-Bus

BUS1 的 1–30 脚依次为 GND、GPIO35、GND、GPIO36、GND、EN/RST、GPIO23、GPIO25、GPIO38、GPIO26、GPIO18、MCU_VDD、GPIO3、GPIO1、GPIO13、GPIO14、GPIO21、GPIO22、GPIO32、GPIO33、GPIO27、GPIO19、GPIO2、GPIO0、HPWR、GPIO34、HPWR、BUS_5V、HPWR、SYS_VBAT。

- 参数与网络：`reference=BUS1`；`pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN/RST,7:GPIO23,8:GPIO25,9:GPIO38,10:GPIO26,11:GPIO18,12:MCU_VDD,13:GPIO3,14:GPIO1,15:GPIO13,16:GPIO14,17:GPIO21,18:GPIO22,19:GPIO32,20:GPIO33,21:GPIO27,22:GPIO19,23:GPIO2,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:BUS_5V,29:HPWR,30:SYS_VBAT`
- 证据：图 6c305db1571c / 第 1 页 / A3-B3 BUS1 M5_BUS 1-30 脚定义

### AWS Bottom2 扩展接口

J1 UART 4P 引出 U2_RXD、U2_TXD、+5V、GND；J2 GPIO 4P 引出 GPIO36、GPIO26、+5V、GND；J3 电源/I2C 4P 引出 GND、+5V、I2C_SDA、I2C_SCL，SDA/SCL 各由 4.7 kΩ 上拉到 3.3 V。

- 参数与网络：`uart_j1=U2_RXD,U2_TXD,+5V,GND`；`gpio_j2=GPIO36,GPIO26,+5V,GND`；`i2c_j3=GND,+5V,I2C_SDA,I2C_SCL`；`i2c_pullups=R2=4.7k,R3=4.7k`
- 证据：图 7343f6f305ba / 第 1 页 / A4-C4 Socket 区域 J1/J2/J3 与 R2/R3

## 总线

### Core2 内部 I2C

Core2 内部 I2C 使用 GPIO21/SYS_SDA 与 GPIO22/SYS_SCL，R57/R58 各 2.2 kΩ 上拉到 MCU_VDD；AXP192、BM8563 和触摸模块连接该总线。

- 参数与网络：`sda=GPIO21/SYS_SDA`；`scl=GPIO22/SYS_SCL`；`pullups=R57=2.2k,R58=2.2k`；`devices=AXP192,BM8563,CTP1`
- 证据：图 6c305db1571c / 第 1 页 / PMU/RTC/C-TP 的 GPIO21/22 网络及 D4 INTERNAL I2C PULUP R57/R58

## GPIO 与控制信号

### 按键、系统 LED 与震动马达

S1 按键连接 MCU_RST，S2 按键连接 PWR_KEY；绿色 LED1 由 SYS_LED 网络控制，震动马达 PADA2 由 VIB_MOTOR 经 R21 22 Ω 和 D2 4148 支路驱动。

- 参数与网络：`reset_button=S1/MCU_RST`；`power_button=S2/PWR_KEY`；`green_led=LED1/SYS_LED`；`vibration_motor=PADA2/VIB_MOTOR`；`motor_resistor=R21 22R`；`flyback_diode=D2 4148`
- 证据：图 6c305db1571c / 第 1 页 / D2 BUTTON、C1 LED 与 C2 VIB_MOTOR 功能区

### AWS Bottom2 RGB LED 链

LED1-LED10 为十颗 5 V 供电的 SK6812 串联灯，数据输入网络为 SK6812；M5-Bus 的 RGB 信号由 GPIO25 引入，并通过 R7/R8 与 Q1 SS8550 Y2 驱动该网络。

- 参数与网络：`count=10`；`part_number=SK6812`；`supply=+5V`；`host_gpio=GPIO25`；`driver=Q1 SS8550 Y2`；`network=SK6812`
- 证据：图 7343f6f305ba / 第 1 页 / A1-A4 LED1-LED10 SK6812 级联及 C2-D2 RGB-R7/R8-Q1 驱动电路

## 时钟

### ESP32 主晶振

X2 标注为 X2520-40MM4S，连接 ESP32 XTAL_P/XTAL_N，两侧各配置 12 pF 电容 C3、C4，XTAL_P 串联 R3 51 Ω。

- 参数与网络：`reference=X2`；`part_number=X2520-40MM4S`；`frequency_mhz=40`；`load_capacitors=C3=12pF,C4=12pF`；`series_resistor=R3 51R`
- 证据：图 6c305db1571c / 第 1 页 / B2-B3 MCU 区域 X2、R3、C3、C4 与 XTAL_P/N 网络

### BM8563 RTC

U5 BM8563 通过 GPIO21/SDA 与 GPIO22/SCL 接入内部 I2C，INT 输出连接 PWR_KEY，X1 为 32.768 kHz 晶振，BT1 为 RTC_BAT 备份电源。

- 参数与网络：`part_number=BM8563`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=PWR_KEY`；`crystal=X1 32.768kHz`；`backup=BT1 RTC_BAT`
- 证据：图 6c305db1571c / 第 1 页 / D1-D2 RTC 区域 U5 BM8563、GPIO21/22、PWR_KEY、X1 和 BT1

## 保护电路

### M5-Bus ESD 与串联保护

M5-Bus 外部信号 EXT_G35/G36/G23/G38/G18/G3/G13/G21/G32/G27/G25/G26/G1/G14/G22/G33/G19/G2/G0/G34 通过 R34-R56 的 47 Ω 串联电阻和 D3-D8 SRV05-4 阵列保护。

- 参数与网络：`series_resistors=R34-R56 47R`；`esd_arrays=D3-D8 SRV05-4`；`protected_signals=G35,G36,G23,G38,G18,G3,G13,G21,G32,G27,G25,G26,G1,G14,G22,G33,G19,G2,G0,G34`
- 证据：图 6c305db1571c / 第 1 页 / A4-B4 ESD 区域 R34-R56 与 D3-D8 SRV05-4

## 存储

### 外部 Flash

U1 XM25QH128B 连接 GPIO11/CS#、GPIO7/HOLD#、GPIO6/SCLK、GPIO10/WP#、GPIO8/SI 和 GPIO9/SO。

- 参数与网络：`reference=U1`；`part_number=XM25QH128B`；`chip_select=GPIO11`；`hold=GPIO7`；`clock=GPIO6`；`write_protect=GPIO10`；`mosi=GPIO8`；`miso=GPIO9`
- 证据：图 6c305db1571c / 第 1 页 / D1 FLASH 区域 U1 XM25QH128B 引脚网络

### microSD 卡接口

TF_CARD_SOCKET 的 DAT0/MISO=GPIO38、DAT3/CS=GPIO4、CLK/SCK=GPIO18、CMD/MOSI=GPIO23，并由 PERI_VDD 供电。

- 参数与网络：`miso=GPIO38`；`chip_select=GPIO4`；`clock=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / D2-D3 CARD 区域 TF_CARD_SOCKET、GPIO38/4/18/23 与 PERI_VDD

## 内存与 Flash

### 外部 PSRAM

U2 ESPPSRAM64H 的 SCLK=GPIO6、CS#=GPIO17、SI/SIO0=GPIO8、SO/SIO1=GPIO7、SIO2=GPIO10、SIO3=GPIO9。

- 参数与网络：`reference=U2`；`part_number=ESPPSRAM64H`；`clock=GPIO6`；`chip_select=GPIO17`；`sio0=GPIO8`；`sio1=GPIO7`；`sio2=GPIO10`；`sio3=GPIO9`
- 证据：图 6c305db1571c / 第 1 页 / D1 PSRAM 区域 U2 ESPPSRAM64H 引脚网络

## 音频

### NS4168 扬声器链

U6 NS4168 的 BCLK=GPIO12、LRCLK=GPIO0、SADATA=GPIO2、CTRL=SPK_EN，VOP/VON 经 R20 5.1 kΩ 与 PADA1 SPEAKER_PAD 连接。

- 参数与网络：`part_number=NS4168`；`bclk=GPIO12`；`lrclk=GPIO0`；`data=GPIO2`；`enable=SPK_EN`；`output=VOP,VON to PADA1`
- 证据：图 6c305db1571c / 第 1 页 / C2 SPEAKER 区域 U6 NS4168、GPIO0/2/12、SPK_EN 与 PADA1

### AWS Bottom2 数字麦克风

U2 LMD4737T261 由 3.3 V 供电，数字输出 DAT 连接 M5-Bus GPIO34，时钟 CLK 连接 M5-Bus GPIO0。

- 参数与网络：`part_number=LMD4737T261`；`supply=+3.3V`；`data=GPIO34`；`clock=GPIO0`
- 证据：图 7343f6f305ba / 第 1 页 / B1-B2 U2 LMD4737T261 DAT/CLK 网络及 D4 J4 pin24 CLK/pin26 DAT

## 传感器

### AWS Bottom2 BMI270

U1 BMI270 通过 I2C_SDA/I2C_SCL 接入底座总线，SDO 由 R5 4.7 kΩ 下拉且 R4 上拉位置为 NC，因此图面标注默认 7 位地址 0x68。

- 参数与网络：`part_number=BMI270`；`sda=I2C_SDA`；`scl=I2C_SCL`；`sdo_pulldown=R5 4.7k`；`sdo_pullup=R4 NC`；`i2c_address=0x68`
- 证据：图 7343f6f305ba / 第 1 页 / B2-B3 U1 BMI270、R4/R5 与 SDO=0 addr:0x68(default) 注记

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 资源版本范围 | `core_asset=CORE2_V1.0_SCH`；`bottom_asset=M5GO_Bottom2_SCH_Main_V1.3_AWS_Version` |
| 系统结构 | Core2 主控制器 | `reference=U2`；`part_number=ESP32-D0WDQ6`；`schematic=CORE2_V1.0` |
| 系统结构 | v1.3 产品的 Core 主板 BOM | `schematic_controller=ESP32-D0WDQ6`；`schematic_usb_uart=CP2104-F03-GMR`；`source_controller=ESP32-D0WDQ6-V3`；`source_usb_uart=CH9102F` |
| 存储 | 外部 Flash | `reference=U1`；`part_number=XM25QH128B`；`chip_select=GPIO11`；`hold=GPIO7`；`clock=GPIO6`；`write_protect=GPIO10`；`mosi=GPIO8`；`miso=GPIO9` |
| 内存与 Flash | 外部 PSRAM | `reference=U2`；`part_number=ESPPSRAM64H`；`clock=GPIO6`；`chip_select=GPIO17`；`sio0=GPIO8`；`sio1=GPIO7`；`sio2=GPIO10`；`sio3=GPIO9` |
| 时钟 | ESP32 主晶振 | `reference=X2`；`part_number=X2520-40MM4S`；`frequency_mhz=40`；`load_capacitors=C3=12pF,C4=12pF`；`series_resistor=R3 51R` |
| 射频 | ESP32 天线网络 | `antenna=ANT1 IPEX`；`series_l1=TBD/DNP`；`shunt_c1=TBD/DNP`；`shunt_c2=TBD/DNP`；`series_r2=DNP`；`bypass_r1=0R` |
| 电源 | AXP192 电源树 | `dcdc1=MCU_VDD via L3 2.2uH`；`dcdc3=LCD_BL via L2 2.2uH`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS` |
| 总线 | Core2 内部 I2C | `sda=GPIO21/SYS_SDA`；`scl=GPIO22/SYS_SCL`；`pullups=R57=2.2k,R58=2.2k`；`devices=AXP192,BM8563,CTP1` |
| 电源 | M5-Bus 5 V 升压 | `reference=U8`；`part_number=SY7088`；`input=IPS_BUS`；`output=BUS_5V`；`inductor=L4 2.2uH`；`enable=BST_EN` |
| 接口 | Core2 USB-UART | `bridge=CP2104-F03-GMR`；`usb_dp=SYS_DP`；`usb_dm=SYS_DM`；`uart_tx=GPIO3 via R7 47R`；`uart_rx=GPIO1 via R8 47R`；`auto_download=DTR/RTS via Q1/Q2 8050 to MCU_RST/GPIO0` |
| 接口 | USB Type-C 接口 | `connector=J3 TYPEC_16P`；`usb_dp=USB_DP`；`usb_dm=USB_DM`；`cc_pulldowns=R32=5.1k,R33=5.1k`；`fuse=FU1 1A/6V`；`supply=USB_5V` |
| 音频 | NS4168 扬声器链 | `part_number=NS4168`；`bclk=GPIO12`；`lrclk=GPIO0`；`data=GPIO2`；`enable=SPK_EN`；`output=VOP,VON to PADA1` |
| 时钟 | BM8563 RTC | `part_number=BM8563`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=PWR_KEY`；`crystal=X1 32.768kHz`；`backup=BT1 RTC_BAT` |
| GPIO 与控制信号 | 按键、系统 LED 与震动马达 | `reset_button=S1/MCU_RST`；`power_button=S2/PWR_KEY`；`green_led=LED1/SYS_LED`；`vibration_motor=PADA2/VIB_MOTOR`；`motor_resistor=R21 22R`；`flyback_diode=D2 4148` |
| 接口 | Core2 LCD | `mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`chip_select=GPIO5`；`reset=LCD_RST`；`data_command=GPIO15`；`backlight=LCD_BL`；`supply=PERI_VDD` |
| 接口 | Core2 电容触摸 | `sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=LCD_RST`；`supply=MCU_VDD via R65 47R` |
| 存储 | microSD 卡接口 | `miso=GPIO38`；`chip_select=GPIO4`；`clock=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD` |
| 接口 | Core2 30 Pin M5-Bus | `reference=BUS1`；`pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN/RST,7:GPIO23,8:GPIO25,9:GPIO38,10:GPIO26,11:GPIO18,12:MCU_VDD,13:GPIO3,14:GPIO1,15:GPIO13,16:GPIO14,17:GPIO21,18:GPIO22,19:GPIO32,20:GPIO33,21:GPIO27,22:GPIO19,23:GPIO2,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:BUS_5V,29:HPWR,30:SYS_VBAT` |
| 保护电路 | M5-Bus ESD 与串联保护 | `series_resistors=R34-R56 47R`；`esd_arrays=D3-D8 SRV05-4`；`protected_signals=G35,G36,G23,G38,G18,G3,G13,G21,G32,G27,G25,G26,G1,G14,G22,G33,G19,G2,G0,G34` |
| GPIO 与控制信号 | AWS Bottom2 RGB LED 链 | `count=10`；`part_number=SK6812`；`supply=+5V`；`host_gpio=GPIO25`；`driver=Q1 SS8550 Y2`；`network=SK6812` |
| 传感器 | AWS Bottom2 BMI270 | `part_number=BMI270`；`sda=I2C_SDA`；`scl=I2C_SCL`；`sdo_pulldown=R5 4.7k`；`sdo_pullup=R4 NC`；`i2c_address=0x68` |
| 音频 | AWS Bottom2 数字麦克风 | `part_number=LMD4737T261`；`supply=+3.3V`；`data=GPIO34`；`clock=GPIO0` |
| 核心器件 | ATECC608B 安全器件 | `reference=U4`；`part_number=ATECC608B`；`supply=+3.3V`；`scl=I2C_SCL`；`sda=I2C_SDA` |
| 电源 | AWS Bottom2 充电电路 | `charger=U3 TP4057`；`input=VIN`；`battery_output=BAT+`；`program_resistor=R9 2k`；`status_led=D1 1615RG via R6 1k` |
| 接口 | AWS Bottom2 扩展接口 | `uart_j1=U2_RXD,U2_TXD,+5V,GND`；`gpio_j2=GPIO36,GPIO26,+5V,GND`；`i2c_j3=GND,+5V,I2C_SDA,I2C_SCL`；`i2c_pullups=R2=4.7k,R3=4.7k` |

## 待确认事项

- `system.core_bom_revision`：随附 Core 主板图是 CORE2_V1.0，并标注 ESP32-D0WDQ6 与 CP2104-F03-GMR；产品源文档则描述 ESP32-D0WDQ6-V3 与 CH9102F，现有资源无法确认 K010-AWS-V13 实物采用哪组 Core 主板 BOM。（证据：图 6c305db1571c / 第 1 页 / MCU 区域 U2 ESP32-D0WDQ6 与 USB2UART 区域 U3 CP2104-F03-GMR 标注）
- `rf.wifi_antenna`：ESP32 LNA_IN 经 L1、C1、C2 和 R2 匹配位置连接 ANT1 IPEX；L1/C1/C2 标注 RF_C(TBD;DNP)，R2 标注 DNP 并并联 R1 0 Ω 路径。（证据：图 6c305db1571c / 第 1 页 / A2 MCU 上方 LNA_IN-L1/C1/C2-R1/R2-ANT1 IPEX 匹配网络）
- `review.core_bom_revision`：K010-AWS-V13 量产实物的 Core 主板实际采用 ESP32-D0WDQ6 还是 ESP32-D0WDQ6-V3，以及 CP2104-F03-GMR 还是 CH9102F？；原因：随附主板资源为 CORE2_V1.0 且标注 ESP32-D0WDQ6/CP2104-F03-GMR，产品源文档描述 ESP32-D0WDQ6-V3/CH9102F，两者版本记录不一致。
- `review.wifi_antenna_matching`：量产 Core2 主板的 ESP32 LNA_IN 至 ANT1 IPEX 匹配网络中，L1/C1/C2/R2 的实际装配值和 DNP 状态是什么？；原因：主板图将 L1/C1/C2 标为 TBD/DNP、R2 标为 DNP，只明确 R1 为 0 Ω，无法从现有图面恢复最终射频 BOM。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6c305db1571c5d0b2bf6bf88a747719ac07a7be236002d15e44fc5974aa50204` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png` |
| 2 | 1 | `7343f6f305ba3794f85b93c5f2f378ff48a0d476cc98dc4de7b2d4f18b6128db` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/SCH_M5GO_Bottom2_SCH_Main_V1.3_AWS_Version_2026_01_30_10_06_42_page_01.png` |

---

源文档：`zh_CN/core/Core2_For_AWS_v1.3.md`

源文档 SHA-256：`ac659cd149bec6294444538603eb3db8dc33cd6f3354694ee496774efc522101`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
