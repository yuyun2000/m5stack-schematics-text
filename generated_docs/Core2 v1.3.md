# Core2 v1.3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core2 v1.3 |
| SKU | K010-V13 |
| 产品 ID | `core2-v1-3-7def93e81521` |
| 源文档 | `zh_CN/core/Core2_v1.3.md` |

## 概述

Core2 v1.3 的资源由一张 CORE2_V1.0 核心板整页图和一张 v1.3 扩展板图组成。核心板以 ESP32-D0WDQ6、AXP192、XM25QH128B、ESPPSRAM64H、CP2104、BM8563、NS4168 与 SY7088 构成主控、电源、存储、USB-UART、RTC、音频、LCD/触摸、microSD、M5-Bus 和 5V 升压系统；v1.3 扩展板通过 M5-Bus 的 G21/G22 与 G0/G34 分别连接 BMI270 和 SPM1423HM4H-B。产品页声称的 -V3 SoC、CH9102F、容量、显示/触摸型号、I2C 地址、电池与额定音频参数未全部在两张图中直接标明，因此与旧核心板图的版本差异单列为待确认。

## 检索关键词

`Core2 v1.3`、`K010-V13`、`CORE2_V1.0`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`AXP192`、`XM25QH128B`、`ESPPSRAM64H`、`CP2104-F03-GMR`、`CH9102F`、`BM8563`、`NS4168`、`SY7088`、`BMI270`、`SPM1423HM4H-B`、`ILI9342C`、`FT6336U`、`USB Type-C`、`M5-Bus`、`microSD`、`SYS_SDA`、`SYS_SCL`、`IMU_SDA`、`IMU_SCL`、`MIC_CLK`、`MIC_DAT`、`I2S`、`SPK_EN`、`VIB_MOTOR`、`LCD_BL`、`LCD_RST`、`RTC_VDD`、`MCU_VDD`、`PERI_VDD`、`IPS_BUS`、`BUS_5V`、`SYS_VBAT`、`GPIO0`、`GPIO2`、`GPIO4`、`GPIO5`、`GPIO12`、`GPIO15`、`GPIO18`、`GPIO21`、`GPIO22`、`GPIO23`、`GPIO32`、`GPIO33`、`GPIO34`、`GPIO38`、`GPIO39`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| MCU block [main] | ESP32-D0WDQ6 | 核心主控，连接 SPI Flash、PSRAM、LCD、触摸、microSD、音频、RTC、USB-UART、M5-Bus 与天线 | 图 6c305db1571c / 第 1 页 / 网格 A2-C3，MCU 区 ESP32-D0WDQ6 全部引脚 |
| U4 [main] | AXP192 | USB/电池输入、电源轨、按键、指示灯、扬声器、背光和振动控制的 PMU | 图 6c305db1571c / 第 1 页 / 网格 A1-C2，PMU 区 U4 AXP192 |
| U1 [main] | XM25QH128B | ESP32 外部 SPI Flash | 图 6c305db1571c / 第 1 页 / 网格 D1，FLASH 区 U1 XM25QH128B |
| U2 [main] | ESPPSRAM64H | ESP32 外部 PSRAM | 图 6c305db1571c / 第 1 页 / 网格 D1，PSRAM 区 U2 ESPPSRAM64H |
| U3 [main] | CP2104-F03-GMR | USB 转 UART 与自动下载控制 | 图 6c305db1571c / 第 1 页 / 网格 C1-D1，USB2UART 区 U3 CP2104-F03-GMR |
| RTC block [main] | BM8563 | 通过内部 I2C 连接 ESP32 的实时时钟 | 图 6c305db1571c / 第 1 页 / 网格 D2，RTC 区 BM8563、X1、BAT1 |
| U6 [main] | NS4168 | I2S 输入的扬声器功放 | 图 6c305db1571c / 第 1 页 / 网格 C2，SPEAKER 区 U6 NS4168 |
| U8 [main] | SY7088 | IPS_BUS 至 BUS_5V 的升压转换器 | 图 6c305db1571c / 第 1 页 / 网格 C2-D3，5V_BOOST 区 U8 SY7088、L4 |
| J3 [main] | TYPEC_16P | USB 5V、电源和 USB_D_P/USB_D_M 数据接口 | 图 6c305db1571c / 第 1 页 / 网格 B3，USB 区 J3 TYPEC_16P |
| LCD1 [main] | M5_CORE2_LCD_10P | 10 针 SPI LCD 模组接口 | 图 6c305db1571c / 第 1 页 / 网格 B4-C4，LCD 区 LCD1 M5_CORE2_LCD_10P |
| CTP1 [main] | CTP_2.0inch | I2C 电容触摸模组接口 | 图 6c305db1571c / 第 1 页 / 网格 C4-D4，C-TP 区 CTP1 CTP_2.0inch |
| BUS1 [main/base] | M5_BUS | 30 针主板堆叠总线，并向 v1.3 扩展板传递 3.3V、I2C 和 PDM 麦克风信号 | 图 6c305db1571c / 第 1 页 / 网格 A3-B3，M5_BUS 区 BUS1 pins 1-30; 图 4fd2445db21c / 第 1 页 / 网格 B1-C2，扩展板 BUS1 与 IMU/MIC 网络 |
| ANT1,ANT2 [main] | RF antenna / IPEX | ESP32 LNA_IN 的板载与 IPEX 天线路径 | 图 6c305db1571c / 第 1 页 / 网格 A2，ANT1/ANT2 IPEX 与 L1/C1/C2/R1/R2 |
| D3-D8 [main] | SRV05-4 | M5-Bus、外部端口、USB 与复位信号 ESD 阵列 | 图 6c305db1571c / 第 1 页 / 网格 A4-B4，ESD 区 D3-D8 SRV05-4 |
| U1 [base] | BMI270 | Core2 v1.3 扩展板六轴 IMU，通过 IMU_SDA/IMU_SCL 接主板 | 图 4fd2445db21c / 第 1 页 / 网格 C1-D3，U1 BMI270、R1、IMU_SDA/IMU_SCL |
| U2 [base] | SPM1423HM4H-B | Core2 v1.3 扩展板 PDM 麦克风，通过 MIC_CLK/MIC_DAT 接主板 | 图 4fd2445db21c / 第 1 页 / 网格 C1-C2，U2 SPM1423HM4H-B |

## 系统结构

### Core2 v1.3 硬件组成

系统由 CORE2_V1.0 核心板电路与 v1.3 扩展板组成；核心板提供 ESP32、AXP192、Flash/PSRAM、USB-UART、显示触摸、microSD、RTC、扬声器、振动和 M5-Bus，扩展板增加 BMI270 与 PDM 麦克风。

- 参数与网络：`main_board=CORE2_V1.0_SCH`；`soc=ESP32-D0WDQ6`；`pmu=AXP192`；`storage=XM25QH128B`；`memory=ESPPSRAM64H`；`base_imu=BMI270`；`base_mic=SPM1423HM4H-B`
- 证据：图 6c305db1571c / 第 1 页 / 核心板整页; 图 4fd2445db21c / 第 1 页 / v1.3 扩展板整页

## 核心器件

### ESP32-D0WDQ6

核心板 MCU 区器件明确标为 ESP32-D0WDQ6，CHIP_PU 接 MCU_RST，LNA_IN 接天线网络，GPIO0~39 分配至板载外设和 M5-Bus。

- 参数与网络：`part_number=ESP32-D0WDQ6`；`enable=MCU_RST`；`rf=LNA_IN`；`supply=MCU_VDD,VDD_SDIO`；`gpio_range=GPIO0~39`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A2-C3，MCU 区 ESP32-D0WDQ6

### BM8563 RTC

BM8563 以 RTC_VDD 供电，SDA/SCL 接 GPIO21/GPIO22，INT 接 PWR_KEY，X1 32.768K 与 C30/C31 6.8pF 构成时钟网络，BAT1 为 RTC 后备电池接口。

- 参数与网络：`part_number=BM8563`；`supply=RTC_VDD`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=PWR_KEY`；`crystal=X1 32.768K`；`load_caps=C30/C31 6.8pF`；`backup=BAT1 BATTERY_RTC`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D2，RTC 区 BM8563/X1/C30/C31/BAT1

## 电源

### AXP192 输入与电池

U4 AXP192 的 ACIN/VBUS 接 USB_5V，BAT 接 SYS_VBAT，BACKUP 接 RTC_BAT，SDA/SCK 分别接 GPIO21/GPIO22。

- 参数与网络：`reference=U4`；`part_number=AXP192`；`usb_input=USB_5V`；`battery=SYS_VBAT`；`backup=RTC_BAT`；`i2c_sda=GPIO21`；`i2c_scl=GPIO22`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A1-B1，U4 ACIN/VBUS/BAT/BACKUP/SDA/SCK

### AXP192 受控电源轨

AXP192 DCDC1 经 L3 输出 MCU_VDD，DCDC3 经 L2/R17 输出 LCD_BL，LDO1 输出 RTC_VDD，LDO2 输出 PERI_VDD，LDO3 输出 VIB_MOTOR，IPSOUT 输出 IPS_BUS。

- 参数与网络：`dcdc1=MCU_VDD via L3 SWPA3015S2R2MT`；`dcdc3=LCD_BL via L2 SWPA3015S2R2MT and R17 4.7R`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A1-C2，U4 DCDC1/DCDC3/LDO1/LDO2/LDO3/IPSOUT

### AXP192 控制信号

AXP192 控制网络包括 PWR_KEY、MCU_RST、BST_EN、BUS_PW_EN、SYS_LED、SPK_EN 和 LCD_RST，用于开机、复位、5V 升压、指示灯、功放和显示复位。

- 参数与网络：`power_key=PWR_KEY`；`reset=MCU_RST`；`boost_enable=BST_EN`；`bus_power_enable=BUS_PW_EN`；`led=SYS_LED`；`speaker_enable=SPK_EN`；`lcd_reset=LCD_RST`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B1-C1，U4 PWRON/N_RSTO/EXTEN/GPIO0~4 网络

### 振动马达输出

AXP192 LDO3 输出 VIB_MOTOR，经 R21 22R 接 PAD2，D2 4148 跨接马达焊盘用于反向钳位。

- 参数与网络：`rail=VIB_MOTOR from AXP192 LDO3`；`series=R21 22R`；`flyback=D2 4148`；`connector=PAD2 VIB_MOTOR_PAD`
- 证据：图 6c305db1571c / 第 1 页 / 网格 C2-D2，VIB_MOTOR 区 R21/D2/PAD2

### SY7088 总线 5V 升压

U8 SY7088 以 IPS_BUS 供电，LX 经 L4 2.2uH 构成升压级，EN 接 BST_EN，输出为 BUS_5V，反馈分压为 R18 10K 与 R31 1.47K。

- 参数与网络：`reference=U8`；`part_number=SY7088`；`input=IPS_BUS`；`enable=BST_EN`；`inductor=L4 2.2uH`；`output=BUS_5V`；`feedback=R18 10K,R31 1.47K`
- 证据：图 6c305db1571c / 第 1 页 / 网格 C2-D3，5V_BOOST 区 U8/L4/R18/R31

## 接口

### USB Type-C 电源与数据

J3 TYPEC_16P 将 DP1/DP2 并为 SYS_DP、DN1/DN2 并为 SYS_DM，VBUS 通过 FU1 1A/6V 形成 USB_5V，CC1/CC2 各有 5.1K 下拉。

- 参数与网络：`connector=J3 TYPEC_16P`；`data_plus=SYS_DP`；`data_minus=SYS_DM`；`fuse=FU1 1A/6V`；`vbus=USB_5V`；`cc_pull_down=2x 5.1K`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B3，USB 区 J3/FU1/CC1/CC2/SYS_DP/SYS_DM

### LCD SPI 接口

LCD1 的 MOSI、MISO、SCK、CS、D/C 分别经 R61~R63 47R 与相关网络连接 GPIO23、GPIO38、GPIO18、GPIO5、GPIO15，RST 接 LCD_RST，LED_A 接 LCD_BL，VDD 接 PERI_VDD。

- 参数与网络：`mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`chip_select=GPIO5`；`data_command=GPIO15`；`reset=LCD_RST`；`backlight=LCD_BL`；`supply=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B4-C4，LCD 区 LCD1 pins 2-10

### 电容触摸接口

CTP1 的 SDA、SCL、INT、RST 分别连接 GPIO21、GPIO22、GPIO39、LCD_RST，VDD 接 MCU_VDD。

- 参数与网络：`connector=CTP1 CTP_2.0inch`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=LCD_RST`；`supply=MCU_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 网格 C4-D4，C-TP 区 CTP1

### PORT-A HY2.0-4P

J4 PORT-A 的 IO2、IO1、5V、GND 分别连接 EXT_G33、EXT_G32、BUS_5V、GND。

- 参数与网络：`connector=J4 PORT-A`；`pin1=GND`；`pin2=BUS_5V`；`pin3=EXT_G32`；`pin4=EXT_G33`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B3，EXT.PORTA 区 J4

## 总线

### LCD 与 microSD 共用 SPI

LCD 与 microSD 共用 GPIO23 MOSI、GPIO38 MISO、GPIO18 SCK，LCD 使用 GPIO5 CS，microSD 使用 GPIO4 CS。

- 参数与网络：`mosi=GPIO23`；`miso=GPIO38`；`clock=GPIO18`；`lcd_cs=GPIO5`；`sd_cs=GPIO4`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B4-C4 LCD 与网格 D2-D3 CARD

### 30 针 M5-Bus

BUS1 引出 GND、GPIO35/36、EN/RST、GPIO23/25、GPIO38/26、GPIO18、3.3V、GPIO3/1、GPIO13/14、GPIO21/22、GPIO32/33、GPIO27/19、GPIO2/0、HPWR、GPIO34、5V 与 BAT。

- 参数与网络：`pins_1_6=1 GND,2 G35,3 GND,4 G36,5 GND,6 EN/RST`；`pins_7_12=7 G23,8 G25,9 G38,10 G26,11 G18,12 3.3V`；`pins_13_18=13 G3,14 G1,15 G13,16 G14,17 G21,18 G22`；`pins_19_24=19 G32,20 G33,21 G27,22 G19,23 G2,24 G0`；`pins_25_30=25 HPWR,26 G34,27 HPWR,28 5V,29 HPWR,30 BAT`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A3-B3，M5_BUS 区 BUS1 pins 1-30

### 内部与外部 I2C 上拉

内部 GPIO21/GPIO22 由 R57/R58 2.2K 上拉到 MCU_VDD，外部 GPIO33/GPIO32 由 R59/R60 5.1K 上拉到 MCU_VDD。

- 参数与网络：`internal=GPIO21/GPIO22,R57/R58 2.2K`；`external=GPIO33/GPIO32,R59/R60 5.1K`；`rail=MCU_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D4，INTERNAL I2C PULLUP 与 EXT.I2C PULLUP

## 时钟

### ESP32 40MHz 晶振

MCU XTAL_P/XTAL_N 接 X2 40M 晶振，串联 R3 51R，C3/C4 各 12pF 对地。

- 参数与网络：`crystal=X2 40M`；`series_resistor=R3 51R`；`load_caps=C3 12pF,C4 12pF`
- 证据：图 6c305db1571c / 第 1 页 / 网格 B2-C3，MCU XTAL_P/XTAL_N、X2、R3、C3/C4

## 复位

### 复位与电源按键

S1 SMT_SW_TS_015 按下将 MCU_RST 接地，S2 SMT_SW_TS_015 按下将 PWR_KEY 接地。

- 参数与网络：`reset=S1 MCU_RST to GND`；`power=S2 PWR_KEY to GND`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D2，BUTTON 区 S1/S2

## 保护电路

### 外部信号 ESD 与串联电阻

D3-D8 SRV05-4 阵列保护 M5-Bus GPIO、PORT-A、USB_D_P/USB_D_M 与 MCU_RST；多路 GPIO 在阵列前串联 R34~R56 47R。

- 参数与网络：`devices=D3-D8 SRV05-4`；`series_resistors=R34-R56 47R`；`protected_groups=M5-Bus GPIO,PORT-A,USB DP/DM,MCU_RST`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A4-B4，ESD 区 D3-D8/R34-R56

## 存储

### XM25QH128B SPI Flash

U1 XM25QH128B 以 MCU_VDD 供电，CS#、SO、SCLK、SI 分别连接 GPIO11、GPIO27、GPIO6、GPIO8。

- 参数与网络：`reference=U1 [main]`；`part_number=XM25QH128B`；`supply=MCU_VDD`；`chip_select=GPIO11`；`miso=GPIO27`；`clock=GPIO6`；`mosi=GPIO8`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D1，FLASH 区 U1

### microSD SPI 接口

TF_CARD_SOCKET 的 DAT0/MISO、DAT3/CS、CLK/SCK、CMD/MOSI 分别经 R25~R28 10K 网络连接 GPIO38、GPIO4、GPIO18、GPIO23，VDD 接 PERI_VDD。

- 参数与网络：`miso=GPIO38`；`chip_select=GPIO4`；`clock=GPIO18`；`mosi=GPIO23`；`pullups=R25-R28 10K`；`supply=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D2-D3，CARD 区 TF_CARD_SOCKET/R25-R28

## 内存与 Flash

### ESPPSRAM64H

U2 ESPPSRAM64H 以 MCU_VDD 供电，SIO0/SIO1/SIO2/SIO3、SCLK、CS# 接 ESP32 的 GPIO8/GPIO27/GPIO10/GPIO9/GPIO16/GPIO17。

- 参数与网络：`reference=U2 [main]`；`part_number=ESPPSRAM64H`；`supply=MCU_VDD`；`sio0=GPIO8`；`sio1=GPIO27`；`sio2=GPIO10`；`sio3=GPIO9`；`clock=GPIO16`；`chip_select=GPIO17`
- 证据：图 6c305db1571c / 第 1 页 / 网格 D1，PSRAM 区 U2

## 音频

### NS4168 I2S 扬声器

U6 NS4168 的 LRCK、BCLK、SADATA 分别连接 GPIO0、GPIO12、GPIO2，CTRL 接 SPK_EN，VDD 接 MCU_VDD，VOP/VON 经 R20/R22 4.7R 接 PAD1 扬声器焊盘。

- 参数与网络：`reference=U6`；`part_number=NS4168`；`lrck=GPIO0`；`bclk=GPIO12`；`data=GPIO2`；`enable=SPK_EN`；`supply=MCU_VDD`；`output=VOP/VON to PAD1 via R20/R22 4.7R`
- 证据：图 6c305db1571c / 第 1 页 / 网格 C2，SPEAKER 区 U6/PAD1/R20/R22

### SPM1423 PDM 麦克风

扩展板 U2 SPM1423HM4H-B 的 CLK/DATA 接 MIC_CLK/MIC_DAT，VCC 接 SYS_P033，SELECT 与两个 GND 引脚接地；BUS1 将 MIC_CLK/MIC_DAT 接至 pins 24/26，即主板 GPIO0/GPIO34。

- 参数与网络：`reference=U2 [base]`；`part_number=SPM1423HM4H-B`；`clock=MIC_CLK BUS1 pin24 GPIO0`；`data=MIC_DAT BUS1 pin26 GPIO34`；`supply=SYS_P033`；`select=GND`
- 证据：图 4fd2445db21c / 第 1 页 / 网格 B1-C2，BUS1 MIC_CLK/MIC_DAT 与 U2 SPM1423HM4H-B

## 传感器

### BMI270 扩展板 IMU

扩展板 U1 BMI270 的 SDX/SCX 接 IMU_SDA/IMU_SCL，VDD/VDDIO/CSB 接 SYS_P033，SDO 经 R1 10K 接地，INT1/INT2 和辅助接口未连接。

- 参数与网络：`reference=U1 [base]`；`part_number=BMI270`；`sda=IMU_SDA via BUS1 pin17/GPIO21`；`scl=IMU_SCL via BUS1 pin18/GPIO22`；`supply=SYS_P033`；`csb=SYS_P033`；`sdo=R1 10K to GND`；`interrupts=NC`
- 证据：图 4fd2445db21c / 第 1 页 / 网格 C1-D3，U1 BMI270/R1 与 BUS1 IMU_SDA/IMU_SCL

## 射频

### ESP32 天线路径

ESP32 LNA_IN 经 L1/C1/C2 匹配位和 R1/R2 0R/DNP 选择网络连接 ANT1 与 ANT2 IPEX，匹配位标注 RF_L(TBD) 与 RF_C(TBD/DNP)。

- 参数与网络：`soc_net=LNA_IN`；`matching=L1 RF_L(TBD),C1 RF_C(TBD),C2 RF_C(TBD/DNP)`；`selection=R1 0R,R2 DNP`；`connectors=ANT1,ANT2 IPEX`
- 证据：图 6c305db1571c / 第 1 页 / 网格 A2，LNA_IN、L1/C1/C2/R1/R2、ANT1/ANT2

## 调试与烧录

### CP2104 USB-UART

U3 CP2104-F03-GMR 的 DP/DM 接 SYS_DP/SYS_DM，TXD/RXD 经 CP_TX/CP_RX 与 R7/R8 47R 连接 GPIO3/GPIO1，DTR/RTS 通过 Q1/Q2 S8050 控制 MCU_RST 与 GPIO0。

- 参数与网络：`reference=U3 [main]`；`part_number=CP2104-F03-GMR`；`usb=SYS_DP,SYS_DM`；`uart=CP_TX->R7 47R->GPIO3,CP_RX->R8 47R->GPIO1`；`auto_download=Q1/Q2 S8050 to MCU_RST/GPIO0`
- 证据：图 6c305db1571c / 第 1 页 / 网格 C1-D1，USB2UART 区 U3/Q1/Q2/R7/R8

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Core2 v1.3 硬件组成 | `main_board=CORE2_V1.0_SCH`；`soc=ESP32-D0WDQ6`；`pmu=AXP192`；`storage=XM25QH128B`；`memory=ESPPSRAM64H`；`base_imu=BMI270`；`base_mic=SPM1423HM4H-B` |
| 核心器件 | ESP32-D0WDQ6 | `part_number=ESP32-D0WDQ6`；`enable=MCU_RST`；`rf=LNA_IN`；`supply=MCU_VDD,VDD_SDIO`；`gpio_range=GPIO0~39` |
| 时钟 | ESP32 40MHz 晶振 | `crystal=X2 40M`；`series_resistor=R3 51R`；`load_caps=C3 12pF,C4 12pF` |
| 射频 | ESP32 天线路径 | `soc_net=LNA_IN`；`matching=L1 RF_L(TBD),C1 RF_C(TBD),C2 RF_C(TBD/DNP)`；`selection=R1 0R,R2 DNP`；`connectors=ANT1,ANT2 IPEX` |
| 电源 | AXP192 输入与电池 | `reference=U4`；`part_number=AXP192`；`usb_input=USB_5V`；`battery=SYS_VBAT`；`backup=RTC_BAT`；`i2c_sda=GPIO21`；`i2c_scl=GPIO22` |
| 电源 | AXP192 受控电源轨 | `dcdc1=MCU_VDD via L3 SWPA3015S2R2MT`；`dcdc3=LCD_BL via L2 SWPA3015S2R2MT and R17 4.7R`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS` |
| 电源 | AXP192 控制信号 | `power_key=PWR_KEY`；`reset=MCU_RST`；`boost_enable=BST_EN`；`bus_power_enable=BUS_PW_EN`；`led=SYS_LED`；`speaker_enable=SPK_EN`；`lcd_reset=LCD_RST` |
| 存储 | XM25QH128B SPI Flash | `reference=U1 [main]`；`part_number=XM25QH128B`；`supply=MCU_VDD`；`chip_select=GPIO11`；`miso=GPIO27`；`clock=GPIO6`；`mosi=GPIO8` |
| 内存与 Flash | ESPPSRAM64H | `reference=U2 [main]`；`part_number=ESPPSRAM64H`；`supply=MCU_VDD`；`sio0=GPIO8`；`sio1=GPIO27`；`sio2=GPIO10`；`sio3=GPIO9`；`clock=GPIO16`；`chip_select=GPIO17` |
| 接口 | USB Type-C 电源与数据 | `connector=J3 TYPEC_16P`；`data_plus=SYS_DP`；`data_minus=SYS_DM`；`fuse=FU1 1A/6V`；`vbus=USB_5V`；`cc_pull_down=2x 5.1K` |
| 调试与烧录 | CP2104 USB-UART | `reference=U3 [main]`；`part_number=CP2104-F03-GMR`；`usb=SYS_DP,SYS_DM`；`uart=CP_TX->R7 47R->GPIO3,CP_RX->R8 47R->GPIO1`；`auto_download=Q1/Q2 S8050 to MCU_RST/GPIO0` |
| 接口 | LCD SPI 接口 | `mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`chip_select=GPIO5`；`data_command=GPIO15`；`reset=LCD_RST`；`backlight=LCD_BL`；`supply=PERI_VDD` |
| 接口 | 电容触摸接口 | `connector=CTP1 CTP_2.0inch`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=LCD_RST`；`supply=MCU_VDD` |
| 存储 | microSD SPI 接口 | `miso=GPIO38`；`chip_select=GPIO4`；`clock=GPIO18`；`mosi=GPIO23`；`pullups=R25-R28 10K`；`supply=PERI_VDD` |
| 总线 | LCD 与 microSD 共用 SPI | `mosi=GPIO23`；`miso=GPIO38`；`clock=GPIO18`；`lcd_cs=GPIO5`；`sd_cs=GPIO4` |
| 音频 | NS4168 I2S 扬声器 | `reference=U6`；`part_number=NS4168`；`lrck=GPIO0`；`bclk=GPIO12`；`data=GPIO2`；`enable=SPK_EN`；`supply=MCU_VDD`；`output=VOP/VON to PAD1 via R20/R22 4.7R` |
| 电源 | 振动马达输出 | `rail=VIB_MOTOR from AXP192 LDO3`；`series=R21 22R`；`flyback=D2 4148`；`connector=PAD2 VIB_MOTOR_PAD` |
| 电源 | SY7088 总线 5V 升压 | `reference=U8`；`part_number=SY7088`；`input=IPS_BUS`；`enable=BST_EN`；`inductor=L4 2.2uH`；`output=BUS_5V`；`feedback=R18 10K,R31 1.47K` |
| 核心器件 | BM8563 RTC | `part_number=BM8563`；`supply=RTC_VDD`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=PWR_KEY`；`crystal=X1 32.768K`；`load_caps=C30/C31 6.8pF`；`backup=BAT1 BATTERY_RTC` |
| 复位 | 复位与电源按键 | `reset=S1 MCU_RST to GND`；`power=S2 PWR_KEY to GND` |
| 总线 | 30 针 M5-Bus | `pins_1_6=1 GND,2 G35,3 GND,4 G36,5 GND,6 EN/RST`；`pins_7_12=7 G23,8 G25,9 G38,10 G26,11 G18,12 3.3V`；`pins_13_18=13 G3,14 G1,15 G13,16 G14,17 G21,18 G22`；`pins_19_24=19 G32,20 G33,21 G27,22 G19,23 G2,24 G0`；`pins_25_30=25 HPWR,26 G34,27 HPWR,28 5V,29 HPWR,30 BAT` |
| 接口 | PORT-A HY2.0-4P | `connector=J4 PORT-A`；`pin1=GND`；`pin2=BUS_5V`；`pin3=EXT_G32`；`pin4=EXT_G33` |
| 保护电路 | 外部信号 ESD 与串联电阻 | `devices=D3-D8 SRV05-4`；`series_resistors=R34-R56 47R`；`protected_groups=M5-Bus GPIO,PORT-A,USB DP/DM,MCU_RST` |
| 总线 | 内部与外部 I2C 上拉 | `internal=GPIO21/GPIO22,R57/R58 2.2K`；`external=GPIO33/GPIO32,R59/R60 5.1K`；`rail=MCU_VDD` |
| 传感器 | BMI270 扩展板 IMU | `reference=U1 [base]`；`part_number=BMI270`；`sda=IMU_SDA via BUS1 pin17/GPIO21`；`scl=IMU_SCL via BUS1 pin18/GPIO22`；`supply=SYS_P033`；`csb=SYS_P033`；`sdo=R1 10K to GND`；`interrupts=NC` |
| 音频 | SPM1423 PDM 麦克风 | `reference=U2 [base]`；`part_number=SPM1423HM4H-B`；`clock=MIC_CLK BUS1 pin24 GPIO0`；`data=MIC_DAT BUS1 pin26 GPIO34`；`supply=SYS_P033`；`select=GND` |
| 系统结构 | CORE2_V1.0 核心板图对 v1.3 的适用范围 | `main_schematic=CORE2_V1.0_SCH`；`target_product=Core2 v1.3`；`base_schematic=core2_v1.3` |
| 核心器件 | Core2 v1.3 SoC 具体版本 | `source_document=ESP32-D0WDQ6-V3`；`schematic=ESP32-D0WDQ6` |
| 存储 | Core2 v1.3 Flash 容量 | `source_document=16MB`；`schematic_part=XM25QH128B`；`reference=U1 [main]` |
| 内存与 Flash | Core2 v1.3 PSRAM 容量 | `source_document=8MB`；`schematic_part=ESPPSRAM64H`；`reference=U2 [main]` |
| 调试与烧录 | Core2 v1.3 USB-TTL 芯片 | `source_document=CH9102F`；`schematic=CP2104-F03-GMR`；`reference=U3 [main]` |
| 核心器件 | LCD 与触摸控制器型号 | `source_document_lcd=ILI9342C`；`source_document_touch=FT6336U`；`schematic_lcd=M5_CORE2_LCD_10P`；`schematic_touch=CTP_2.0inch` |
| 总线地址 | 内部 I2C 地址 | `axp192=0x34`；`bm8563=0x51`；`ft6336u=0x38`；`bmi270=0x68`；`bus=GPIO21 SDA,GPIO22 SCL` |
| 电源 | 主电池与 RTC 电池规格 | `source_document_main=3.7V 500mAh`；`source_document_rtc=MS412FE 3V 1.0mAh`；`schematic_main=SYS_VBAT/J5`；`schematic_rtc=BAT1 BATTERY_RTC` |
| 音频 | 扬声器额定规格 | `amplifier=NS4168`；`output=PAD1 SPEAKER_PAD`；`speaker_model=null`；`impedance=null`；`power=null` |
| 系统结构 | 主频与 Wi-Fi 运行规格 | `source_document_cpu=240MHz`；`source_document_wifi=2.4GHz Wi-Fi`；`schematic=ESP32-D0WDQ6 and antenna path` |

## 待确认事项

- `system.main-schematic-applicability`：核心板资源文件名为 CORE2_V1.0，而目标产品为 Core2 v1.3；该图是否完整反映 v1.3 核心板器件版本和全部量产变更无法由当前两页确认。（证据：图 6c305db1571c / 第 1 页 / 核心板资源整页及 CORE2_V1.0 来源文件名; 图 4fd2445db21c / 第 1 页 / v1.3 扩展板整页）
- `component.soc-v13`：产品源文档标注 ESP32-D0WDQ6-V3，而核心板图只标 ESP32-D0WDQ6；量产 v1.3 是否使用 -V3 版本需由当前核心板 BOM 或原理图确认。（证据：图 6c305db1571c / 第 1 页 / 网格 A2-C3，MCU 区 ESP32-D0WDQ6）
- `storage.flash-capacity`：产品源文档标注 16MB Flash，核心板图标出 U1 XM25QH128B 但没有在页内直接写容量；16MB 配置需由器件资料或 BOM 复核。（证据：图 6c305db1571c / 第 1 页 / 网格 D1，FLASH 区 U1 XM25QH128B）
- `memory.psram-capacity`：产品源文档标注 8MB PSRAM，核心板图标出 U2 ESPPSRAM64H 但没有在页内直接写容量；8MB 配置需由器件资料或 BOM 复核。（证据：图 6c305db1571c / 第 1 页 / 网格 D1，PSRAM 区 U2 ESPPSRAM64H）
- `debug.usb-uart-v13`：产品源文档标注 CH9102F，而核心板图 U3 标为 CP2104-F03-GMR；v1.3 量产板的 USB-TTL 器件与自动下载连接需按当前版本资料确认。（证据：图 6c305db1571c / 第 1 页 / 网格 C1-D1，USB2UART 区 U3 CP2104-F03-GMR）
- `component.display-touch-v13`：产品源文档标注 ILI9342C 与 FT6336U，核心板图只显示 LCD1 M5_CORE2_LCD_10P 和 CTP1 CTP_2.0inch 接口，未显示控制器型号。（证据：图 6c305db1571c / 第 1 页 / 网格 B4-D4，LCD1 与 CTP1 接口）
- `address.internal-i2c`：产品源文档列出 AXP192 0x34、BM8563 0x51、FT6336U 0x38 与 BMI270 0x68；图面显示其总线或地址绑定位，但没有直接标注这些十六进制地址。（证据：图 6c305db1571c / 第 1 页 / 网格 A1-D4，AXP192/BM8563/CTP1 与 GPIO21/22 I2C 网络，未标地址; 图 4fd2445db21c / 第 1 页 / 网格 C1-D3，BMI270 SDO 下拉与 I2C 网络，未标地址）
- `power.battery-ratings`：产品源文档标注 3.7V 500mAh 主电池与 MS412FE 3V 1.0mAh RTC 电池；原理图只显示 SYS_VBAT、J5 EXT.BATT 和 BAT1 BATTERY_RTC，没有容量或电池型号。（证据：图 6c305db1571c / 第 1 页 / 网格 A1-D3，AXP192 SYS_VBAT、J5 EXT.BATT、RTC BAT1）
- `audio.rated-output`：核心板图可确认 NS4168 与 PAD1 差分输出，但未显示扬声器型号、阻抗、功率或音频采样格式。（证据：图 6c305db1571c / 第 1 页 / 网格 C2，SPEAKER 区 U6/PAD1）
- `system.operating-specs`：产品源文档标注 240MHz 与 2.4GHz Wi-Fi，原理图展示 ESP32-D0WDQ6 与天线网络，但未直接给出 CPU 运行频率或无线协议参数。（证据：图 6c305db1571c / 第 1 页 / 网格 A2-C3，ESP32-D0WDQ6 与天线网络，未标运行规格）
- `review.main-schematic-applicability`：CORE2_V1.0 核心板图是否完整适用于 Core2 v1.3 量产主板？；原因：核心板资源版本早于目标产品，且 SoC 与 USB-TTL 型号和产品源文档不一致。
- `review.soc-v13`：Core2 v1.3 量产 SoC 是否确认为 ESP32-D0WDQ6-V3？；原因：产品源文档带 -V3，核心板图未带该后缀。
- `review.flash-capacity`：U1 XM25QH128B 在 Core2 v1.3 上的确认容量是否为 16MB？；原因：容量来自产品源文档，原理图页只标器件型号。
- `review.psram-capacity`：U2 ESPPSRAM64H 在 Core2 v1.3 上的确认容量是否为 8MB？；原因：容量来自产品源文档，原理图页只标器件型号。
- `review.usb-uart-v13`：Core2 v1.3 当前量产板的 USB-TTL 是否为 CH9102F，并有对应新版原理图？；原因：产品源文档标注 CH9102F，核心板图标注 CP2104-F03-GMR。
- `review.display-touch-v13`：Core2 v1.3 的 LCD 与触摸模组是否分别确认为 ILI9342C 和 FT6336U？；原因：原理图只显示通用 LCD/CTP 接口，未显示控制器型号。
- `review.internal-i2c-addresses`：AXP192、BM8563、FT6336U、BMI270 的量产地址是否分别为 0x34、0x51、0x38、0x68？；原因：地址来自产品源文档，当前原理图没有直接标注十六进制地址。
- `review.battery-ratings`：Core2 v1.3 主电池与 RTC 电池的量产型号、容量是否为 3.7V 500mAh 和 MS412FE 3V 1.0mAh？；原因：原理图只给出电池网络和连接器，没有容量与具体型号。
- `review.audio-rating`：Core2 v1.3 扬声器的型号、阻抗、额定功率和 I2S 格式是什么？；原因：NS4168 页只显示数字接口与差分输出连接。
- `review.operating-specs`：Core2 v1.3 的量产固件运行主频和无线规格是否确认为 240MHz 与 2.4GHz Wi-Fi？；原因：这些参数来自产品源文档，原理图未直接给出运行配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6c305db1571c5d0b2bf6bf88a747719ac07a7be236002d15e44fc5974aa50204` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png` |
| 2 | 1 | `4fd2445db21cc352925f3cb736935d5e6f4f8d6a0d48165e09af6a33cb75d0a6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/core2_v1.3_SCH_2025_11_14_09_40_33_page_01.png` |

---

源文档：`zh_CN/core/Core2_v1.3.md`

源文档 SHA-256：`de2f8062fb9474dd35a19f91ade411e8f2d9d5edd61eef1ed02c0a98ddb73fe1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
