# Tough 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Tough |
| SKU | K034 |
| 产品 ID | `tough-1f2d2983b489` |
| 源文档 | `zh_CN/core/tough.md` |

## 概述

Tough 主板以 ESP32-D0WDQ6 为核心，配置 AXP192 PMU、独立 Flash/PSRAM、SPI LCD/microSD、NS2009 触控、BM8563 RTC、NS4168 音频和 CP2104 USB-UART。IPS_BUS 经 SY7088 升压为 BUS_5V，外部电池、USB_5V 与 M5-Bus 进入 AXP192 电源域。扩展板以 ME3116AM6G 将 +24V 转为 +5V，并通过 SP485EEN-L/TR、四个 HY2.0 接口和 M5Stack_BUS2 提供 RS-485、I2C、GPIO、UART 与复位接口。

## 检索关键词

`Tough`、`K034`、`ESP32-D0WDQ6`、`AXP192`、`CP2104-F03-GMR`、`XM25QH128B`、`ESPPSRAM64H`、`NS4168`、`SY7088`、`BM8563`、`NS2009`、`CORE2_LCD`、`ME3116AM6G`、`SP485EEN-L/TR`、`USB_5V`、`SYS_VBAT`、`MCU_VDD`、`PERI_VDD`、`RTC_VDD`、`IPS_BUS`、`BUS_5V`、`+24V`、`+5V`、`GPIO21 SDA`、`GPIO22 SCL`、`GPIO39 TP_INT`、`GPIO38 MISO`、`GPIO23 MOSI`、`GPIO18 SCK`、`GPIO4 SD_CS`、`GPIO5 LCD_CS`、`GPIO15 LCD_DC`、`GPIO27 RS485_RX`、`GPIO19 RS485_DIR`、`PORT-A`、`HY-2.0_IIC`、`HY-2.0_IO`、`HY-2.0_UART`、`HY-2.0_RS485`、`M5_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| MCU | ESP32-D0WDQ6 | 主控 SoC，连接存储、LCD、触控、音频、USB-UART、microSD 与扩展总线 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 A2-B3：ESP32-D0WDQ6 pins0-48 |
| U4 | AXP192 | USB、电池与系统多路电源管理器 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 A1-B1：U4 AXP192 |
| U3 | CP2104-F03-GMR | USB 到 UART 下载桥 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 C1：U3 CP2104-F03-GMR |
| U1 (FLASH) | XM25QH128BHQ | 连接 ESP32 SPI0/1 的外部串行 Flash | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 D1：FLASH U1 XM25QH128BHQ |
| U2 (PSRAM) | ESPPSRAM64H | 连接 ESP32 SPI0/1 的外部 PSRAM | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 D1：PSRAM U2 ESPPSRAM64H |
| U6 | NS4168 | I2S 数字音频功率放大器 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 C2：U6 NS4168/SPEAKER_PAD |
| U8 | SY7088 | IPS_BUS 到 BUS_5V 的升压转换器 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 C2-C3：U8 SY7088/L4 |
| U5 | BM8563 | I2C 实时时钟与 RTC_BAT 后备电源接口 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 D1-D2：U5 BM8563/X1/BT1 |
| LCD1 | CORE2_LCD | SPI LCD 显示模块 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 B4-C4：LCD1 CORE2_LCD |
| U9 | NS2009 | I2C 电阻触摸控制器 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 C4：U9 NS2009/R-TP |
| TF_CARD_SOCKET | TF_CARD_SOCKET | SPI microSD 卡座 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 D2-D3：TF_CARD_SOCKET |
| J3 (USB) | TYPEC_16P | USB-C 数据与 USB_5V 输入 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 A3-B3：J3 TYPEC_16P |
| BUS1 | M5_BUS | 30 针系统电源与 GPIO 扩展总线 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 A3-B3：BUS1 M5_BUS pins1-30 |
| U1 (EXT) | ME3116AM6G | +24V 到 +5V 的扩展板降压转换器 | 图 ed90b8c76cce / 第 1 页 / Ext Board第1页网格 B1-B2：U1 ME3116AM6G |
| U2 (EXT) | SP485EEN-L/TR | RS-485 收发器 | 图 ed90b8c76cce / 第 1 页 / Ext Board第1页网格 C2-C3：U2 SP485EEN-L/TR |
| J1-J4 (EXT) | HY2.0-4P | I2C、GPIO、UART 与带电源 RS-485 外部接口 | 图 ed90b8c76cce / 第 1 页 / Ext Board第1页网格 A4-C4：J1-J4 HY-2.0 |
| J7 (EXT) | HY-2.0_RESET | EN/GPIO25/+5V/GND 复位接口 | 图 ed90b8c76cce / 第 1 页 / Ext Board第1页网格 A3：J7 HY-2.0_RESET |
| J6 (EXT) | M5Stack_BUS2 | 扩展板 30 针主板互连总线 | 图 ed90b8c76cce / 第 1 页 / Ext Board第1页网格 C4-D4：J6 M5Stack_BUS2 |
| D3-D7 | SRV05-4 | M5-Bus GPIO 多通道 ESD 保护阵列 | 图 96eb13a23c36 / 第 1 页 / 主板第1页网格 A4-B4：D3-D7 SRV05-4 |

## 系统结构

### Tough 主板与扩展板架构

主板以 ESP32-D0WDQ6 为核心，连接 AXP192、Flash、PSRAM、LCD、NS2009、BM8563、NS4168、CP2104 和 microSD；Ext Board 通过 M5Stack_BUS2 提供 24V 降压、RS-485 和四组 HY2.0 接口。

- 参数与网络：`soc=ESP32-D0WDQ6`；`pmu=AXP192`；`usb_uart=CP2104-F03-GMR`；`touch=NS2009`；`rtc=BM8563`；`audio=NS4168`；`ext_power=ME3116AM6G`；`rs485=SP485EEN-L/TR`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页完整单页; 图 ed90b8c76cce / 第 1 页 / Ext Board第1页完整单页

## 电源

### AXP192 输入与电池路径

U4 AXP192 ACIN/VBUS 接 USB_5V，BAT pins34/35 接 SYS_VBAT，BACKUP pin30 接 RTC_BAT，IPSOUT pins38/39 输出 IPS_BUS。

- 参数与网络：`pmu=U4 AXP192`；`usb_input=USB_5V -> ACIN/VBUS`；`battery=SYS_VBAT -> BAT pins34/35`；`rtc_backup=RTC_BAT -> BACKUP pin30`；`system_output=IPSOUT pins38/39 -> IPS_BUS`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A1-B1：U4 ACIN/VBUS/BAT/BACKUP/IPSOUT

### AXP192 电源轨输出

AXP192 DCDC1 经 L3 SWPA3015S2R2MT 输出 MCU_VDD，LDO1 输出 RTC_VDD，LDO2 输出 PERI_VDD，LDO3 通过 R17 4.7Ω形成 LCD_BL。

- 参数与网络：`dcdc1=L3 SWPA3015S2R2MT -> MCU_VDD`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=R17 4.7Ω -> LCD_BL`；`control_bus=GPIO21 SDA; GPIO22 SCK`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A1-B1：U4 DCDC1/LDO1/LDO2/LDO3

### IPS_BUS 到 BUS_5V 升压

U8 SY7088 由 IPS_BUS 输入，LX 经 L4 2.2uH 升压并输出 BUS_5V；EN 网络标为 BST_EN。

- 参数与网络：`converter=U8 SY7088`；`input=IPS_BUS`；`inductor=L4 2.2uH`；`enable=BST_EN`；`output=BUS_5V`；`feedback=R30 51KΩ/1%; R31 4.7KΩ/1%`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C2-C3：U8/L4/R30/R31

### Ext Board 24V 到 5V

+24V 经 F1 PPTC-1812 形成 IN+，U1 ME3116AM6G 与 L1 10uH、D1 B5819W SL、R2 52.3KΩ/R3 10KΩ生成 +5V。

- 参数与网络：`input=+24V`；`fuse=F1 PPTC-1812`；`converter=U1 ME3116AM6G`；`inductor=L1 10uH`；`diode=D1 B5819W SL`；`feedback=R2 52.3KΩ; R3 10KΩ`；`output=+5V`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 A1-B2：F1/U1/L1/D1/R2/R3

## 接口

### LCD 接口

LCD1 CORE2_LCD 的 MOSI/MISO/SCK/CS/D-C 分别为 GPIO23/GPIO38/GPIO18/GPIO5/GPIO15，RST 为 LCD_RST，LEDA 为 LCD_BL，VDD 为 PERI_VDD。

- 参数与网络：`display=LCD1 CORE2_LCD`；`mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18 via R63 47Ω`；`cs=GPIO5`；`dc=GPIO15`；`reset=LCD_RST`；`backlight=LCD_BL`；`supply=PERI_VDD`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 B4-C4：LCD1/R63/R64/C53

### USB Type-C 接口

J3 TYPEC_16P 的 DP1/DP2 和 DN1/DN2 形成 SYS_DP/SYS_DM，VCC 经 FU1 1A/6V 形成 USB_5V，CC1/CC2 各由 5.1KΩ下拉。

- 参数与网络：`connector=J3 TYPEC_16P`；`dp=SYS_DP`；`dm=SYS_DM`；`vbus=J3 VCC -> FU1 1A/6V -> USB_5V`；`cc=R31/R32 5.1KΩ to GND`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A3-B3：J3/FU1/R31/R32

### M5-Bus 引脚

BUS1 M5_BUS 引出 USB_5V、SYS_VBAT、MCU_VDD、MCU_RST、GPIO0/1/2/3/13/14/18/19/21/22/23/25/26/27/32/33/34/35/36/38 与多个 GND/HPWR。

- 参数与网络：`connector=BUS1 M5_BUS`；`power=USB_5V,SYS_VBAT,MCU_VDD,HPWR,GND`；`reset=MCU_RST`；`gpio=GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A3-B3：BUS1 pins1-30

### 主板辅助接口

J4 PORT-A pins1-4 为 GND、BUS_5V、GPIO32、GPIO33；J5 为 SYS_VBAT/GND 外部电池；J7 FPC_8P 引出 BUS_5V、MCU_VDD、GPIO15/5/39/21/22 与 GND。

- 参数与网络：`port_a=J4 GND,BUS_5V,GPIO32,GPIO33`；`ext_battery=J5 GND,SYS_VBAT`；`fpc=J7 BUS_5V,GND,MCU_VDD,GPIO15,GPIO5,GPIO39,GPIO21,GPIO22`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 B3-C3：J4/J5/J7

### Ext Board HY2.0 接口映射

J1 I2C 为 GPIO33 SCL、GPIO32 SDA、+5V、GND；J2 IO 为 GPIO36 I、GPIO26 O、+5V、GND；J3 UART 为 GPIO13 RX、GPIO14 TX、+5V、GND；J4 RS485 为 B、A、+24V、GND。

- 参数与网络：`J1=GPIO33 SCL; GPIO32 SDA; +5V; GND`；`J2=GPIO36 I; GPIO26 O; +5V; GND`；`J3=GPIO13 RX; GPIO14 TX; +5V; GND`；`J4=RS485_B; RS485_A; +24V; GND`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 A4-C4：J1-J4

### Ext Board M5Stack_BUS2

J6 M5Stack_BUS2 对接主板 30 针总线，包含 IN+/HPWR、+5V、EN、GPIO0/1/2/3/13/14/18/19/21/22/23/25/26/27/32/33/34/35/36/38 和 GND。

- 参数与网络：`connector=J6 M5Stack_BUS2`；`power=IN+,HPWR,+5V,GND`；`signals=EN,GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 C4-D4：J6 pins1-30

## 总线

### 主板 I2C 总线

ESP32 GPIO21/GPIO22 作为 SDA/SCL，连接 AXP192、BM8563 和 U9 NS2009；GPIO21/22 各由 R57/R58 2.2KΩ上拉到 MCU_VDD。

- 参数与网络：`controller=ESP32-D0WDQ6`；`sda=GPIO21`；`scl=GPIO22`；`devices=AXP192,BM8563,NS2009`；`pullups=R57/R58 2.2KΩ to MCU_VDD`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 U4/U5/U9 与 D4 INTERNAL I2C PULLUP

### LCD 与 microSD 共享 SPI

GPIO23 为 MOSI、GPIO38 为 MISO、GPIO18 为 SCK；LCD 使用 GPIO5 片选和 GPIO15 D/C，microSD 使用 GPIO4 片选。

- 参数与网络：`mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`lcd_cs=GPIO5`；`lcd_dc=GPIO15`；`sd_cs=GPIO4`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 BUS1/LCD1/TF_CARD_SOCKET SPI nets

### Ext Board RS-485

U2 SP485EEN-L/TR RO 经 R5 1KΩ连接 GPIO27；GPIO19 经 R8 1KΩ驱动 Q1 SS8050 Y1，控制 RE/DE，DI 在图中接地；A/B 连接 RS485_A/RS485_B。

- 参数与网络：`transceiver=U2 SP485EEN-L/TR`；`rx=RO -> R5 1KΩ -> GPIO27`；`direction=GPIO19 -> R8 -> Q1 -> RE/DE`；`di=GND`；`a=RS485_A`；`b=RS485_B`；`supply=+5V`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 C2-C3：U2/Q1/R5/R8

## 时钟

### ESP32 主时钟

ESP32 XTAL_P/XTAL_N pins45/44 连接 X2520 40MHz 晶体，R3 为 51Ω/1%，两侧各有 12pF 负载电容。

- 参数与网络：`crystal=X2520 40MHz`；`pins=XTAL_P pin45; XTAL_N pin44`；`series=R3 51Ω/1%`；`load_caps=12pF + 12pF`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 B2：ESP32 XTAL_P/XTAL_N 与 40MHz 晶体

### BM8563 RTC 时钟

U5 BM8563 使用 GPIO21 SDA、GPIO22 SCL，X1 为 32.768K 晶体，RTC_BAT 连接 BT1 后备电池，VDD 接 RTC_VDD。

- 参数与网络：`rtc=U5 BM8563`；`sda=GPIO21`；`scl=GPIO22`；`crystal=X1 32.768K`；`backup=RTC_BAT / BT1`；`supply=RTC_VDD`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 D1-D2：U5/X1/BT1

## 复位

### HY2.0_RESET 接口

J7 HY-2.0_RESET pins1-4 为 EN、GPIO25、+5V、GND。

- 参数与网络：`connector=J7 HY-2.0_RESET`；`pin1=EN`；`pin2=GPIO25`；`pin3=+5V`；`pin4=GND`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 A3：J7 pins1-4

## 保护电路

### M5-Bus ESD 保护

D3-D7 SRV05-4 对 BUS1 上的 GPIO0/1/2/3/13/14/18/19/21/22/23/25/26/27/32/33/34/35/36/38 提供多通道对地保护。

- 参数与网络：`devices=D3-D7 SRV05-4`；`protected=GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A4-B4：D3-D7

### RS-485 偏置、终端与浪涌保护

RS485_B 由 R4 4.7KΩ下拉，RS485_A 由 R9 4.7KΩ上拉，R7 120Ω跨接 A/B；D2-D4 SMAJ6.5CA-E3 对 A/B 提供对地及线间保护。

- 参数与网络：`bias_b=R4 4.7KΩ to GND`；`bias_a=R9 4.7KΩ to +5V`；`termination=R7 120Ω`；`tvs=D2-D4 SMAJ6.5CA-E3`
- 证据：图 ed90b8c76cce / 第 1 页 / Ext Board第1页 B3-C3：R4/R7/R9/D2-D4

## 存储

### microSD 卡连接

TF_CARD_SOCKET DAT0/MISO、DAT3/CS、CLK/SCK、CMD/MOSI 分别连接 GPIO38、GPIO4、GPIO18、GPIO23，VDD 接 PERI_VDD。

- 参数与网络：`miso=GPIO38`；`cs=GPIO4`；`sck=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD`；`pullups=R25-R28 10KΩ/1%`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 D2-D3：TF_CARD_SOCKET/R25-R28

## 内存与 Flash

### 外部 Flash 与 PSRAM 连接

U1 XM25QH128BHQ 与 U2 ESPPSRAM64H 连接 ESP32 GPIO6-GPIO11 的 SPI0/1 存储总线，二者由 MCU_VDD 供电。

- 参数与网络：`flash=U1 XM25QH128BHQ`；`psram=U2 ESPPSRAM64H`；`bus=GPIO6/SD_CLK,GPIO7/SD_DATA0,GPIO8/SD_DATA1,GPIO9/SD_DATA2,GPIO10/SD_DATA3,GPIO11/SD_CMD`；`supply=MCU_VDD`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 D1：FLASH U1 与 PSRAM U2

## 音频

### NS4168 I2S 扬声器

U6 NS4168 的 LRCK/BCLK/SADATA 分别接 GPIO0/GPIO12/GPIO2，CTRL 由 SPK_EN 控制，VOP/VON 经 PA1 SPEAKER_PAD 输出。

- 参数与网络：`amplifier=U6 NS4168`；`lrck=GPIO0`；`bclk=GPIO12`；`data=GPIO2`；`enable=SPK_EN`；`output=PA1 SPEAKER_PAD`；`supply=MCU_VDD`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C2：U6/PA1

## 传感器

### NS2009 触控连接

原理图 U9 标为 NS2009，SCL/SDA 接 GPIO22/GPIO21，PENIRQ 接 GPIO39，VDD 接 MCU_VDD，XP/YP/XN/YN 连接 TP_TOUCH。

- 参数与网络：`controller=U9 NS2009`；`scl=GPIO22`；`sda=GPIO21`；`interrupt=GPIO39`；`supply=MCU_VDD`；`panel=XP,YP,XN,YN -> TP_TOUCH`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C4：U9 NS2009/TP_TOUCH

## 射频

### ESP32 天线路径

ESP32 LNA_IN pin2 经 L1 RF_L(TBD:0R) 和 C1/C2 可选匹配网络连接 ANT1，ANT2 标为 DNP。

- 参数与网络：`soc_pin=LNA_IN pin2`；`series=L1 RF_L(TBD:0R)`；`matching=C1 RF_C(TBD:DNP); C2 RF_C(TBD:DNP)`；`antenna=ANT1`；`alternate=ANT2 DNP`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 A2：L1/C1/C2/ANT1/ANT2

## 调试与烧录

### CP2104 USB-UART 下载

U3 CP2104-F03-GMR D+/D- 接 SYS_DP/SYS_DM，CP_TX 经 R7 47Ω连接 GPIO3，CP_RX 经 R8 47Ω连接 GPIO1；握手信号经 Q1/Q2/D1 控制 MCU_RST 与 GPIO0。

- 参数与网络：`bridge=U3 CP2104-F03-GMR`；`usb=SYS_DP/SYS_DM`；`tx=CP_TX -> R7 47Ω -> GPIO3`；`rx=CP_RX -> R8 47Ω -> GPIO1`；`auto_program=Q1/Q2 SS8050 + D1 1N4148 -> MCU_RST/GPIO0`
- 证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C1-D2：U3/R7/R8/Q1/Q2/D1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Tough 主板与扩展板架构 | `soc=ESP32-D0WDQ6`；`pmu=AXP192`；`usb_uart=CP2104-F03-GMR`；`touch=NS2009`；`rtc=BM8563`；`audio=NS4168`；`ext_power=ME3116AM6G`；`rs485=SP485EEN-L/TR` |
| 电源 | AXP192 输入与电池路径 | `pmu=U4 AXP192`；`usb_input=USB_5V -> ACIN/VBUS`；`battery=SYS_VBAT -> BAT pins34/35`；`rtc_backup=RTC_BAT -> BACKUP pin30`；`system_output=IPSOUT pins38/39 -> IPS_BUS` |
| 电源 | AXP192 电源轨输出 | `dcdc1=L3 SWPA3015S2R2MT -> MCU_VDD`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=R17 4.7Ω -> LCD_BL`；`control_bus=GPIO21 SDA; GPIO22 SCK` |
| 电源 | IPS_BUS 到 BUS_5V 升压 | `converter=U8 SY7088`；`input=IPS_BUS`；`inductor=L4 2.2uH`；`enable=BST_EN`；`output=BUS_5V`；`feedback=R30 51KΩ/1%; R31 4.7KΩ/1%` |
| 电源 | Ext Board 24V 到 5V | `input=+24V`；`fuse=F1 PPTC-1812`；`converter=U1 ME3116AM6G`；`inductor=L1 10uH`；`diode=D1 B5819W SL`；`feedback=R2 52.3KΩ; R3 10KΩ`；`output=+5V` |
| 总线 | 主板 I2C 总线 | `controller=ESP32-D0WDQ6`；`sda=GPIO21`；`scl=GPIO22`；`devices=AXP192,BM8563,NS2009`；`pullups=R57/R58 2.2KΩ to MCU_VDD` |
| 总线地址 | BM8563 地址 | `device=U5 BM8563`；`documented_address=0x51`；`explicit_address_on_schematic=false` |
| 内存与 Flash | 外部 Flash 与 PSRAM 连接 | `flash=U1 XM25QH128BHQ`；`psram=U2 ESPPSRAM64H`；`bus=GPIO6/SD_CLK,GPIO7/SD_DATA0,GPIO8/SD_DATA1,GPIO9/SD_DATA2,GPIO10/SD_DATA3,GPIO11/SD_CMD`；`supply=MCU_VDD` |
| 内存与 Flash | Flash 与 PSRAM 容量 | `documented_flash=16MB`；`documented_psram=8MB`；`flash_part=XM25QH128BHQ`；`psram_part=ESPPSRAM64H`；`explicit_mb_fields=false` |
| 时钟 | ESP32 主时钟 | `crystal=X2520 40MHz`；`pins=XTAL_P pin45; XTAL_N pin44`；`series=R3 51Ω/1%`；`load_caps=12pF + 12pF` |
| 射频 | ESP32 天线路径 | `soc_pin=LNA_IN pin2`；`series=L1 RF_L(TBD:0R)`；`matching=C1 RF_C(TBD:DNP); C2 RF_C(TBD:DNP)`；`antenna=ANT1`；`alternate=ANT2 DNP` |
| 总线 | LCD 与 microSD 共享 SPI | `mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18`；`lcd_cs=GPIO5`；`lcd_dc=GPIO15`；`sd_cs=GPIO4` |
| 存储 | microSD 卡连接 | `miso=GPIO38`；`cs=GPIO4`；`sck=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD`；`pullups=R25-R28 10KΩ/1%` |
| 接口 | LCD 接口 | `display=LCD1 CORE2_LCD`；`mosi=GPIO23`；`miso=GPIO38`；`sck=GPIO18 via R63 47Ω`；`cs=GPIO5`；`dc=GPIO15`；`reset=LCD_RST`；`backlight=LCD_BL`；`supply=PERI_VDD` |
| 传感器 | NS2009 触控连接 | `controller=U9 NS2009`；`scl=GPIO22`；`sda=GPIO21`；`interrupt=GPIO39`；`supply=MCU_VDD`；`panel=XP,YP,XN,YN -> TP_TOUCH` |
| 核心器件 | 触控控制器型号差异 | `schematic=U9 NS2009 / R-TP`；`documented=CHSC6540 / capacitive touch / 0x2E` |
| 音频 | NS4168 I2S 扬声器 | `amplifier=U6 NS4168`；`lrck=GPIO0`；`bclk=GPIO12`；`data=GPIO2`；`enable=SPK_EN`；`output=PA1 SPEAKER_PAD`；`supply=MCU_VDD` |
| 时钟 | BM8563 RTC 时钟 | `rtc=U5 BM8563`；`sda=GPIO21`；`scl=GPIO22`；`crystal=X1 32.768K`；`backup=RTC_BAT / BT1`；`supply=RTC_VDD` |
| 接口 | USB Type-C 接口 | `connector=J3 TYPEC_16P`；`dp=SYS_DP`；`dm=SYS_DM`；`vbus=J3 VCC -> FU1 1A/6V -> USB_5V`；`cc=R31/R32 5.1KΩ to GND` |
| 调试与烧录 | CP2104 USB-UART 下载 | `bridge=U3 CP2104-F03-GMR`；`usb=SYS_DP/SYS_DM`；`tx=CP_TX -> R7 47Ω -> GPIO3`；`rx=CP_RX -> R8 47Ω -> GPIO1`；`auto_program=Q1/Q2 SS8050 + D1 1N4148 -> MCU_RST/GPIO0` |
| 核心器件 | USB-UART 型号差异 | `schematic=U3 CP2104-F03-GMR`；`documented=CH9102` |
| 接口 | M5-Bus 引脚 | `connector=BUS1 M5_BUS`；`power=USB_5V,SYS_VBAT,MCU_VDD,HPWR,GND`；`reset=MCU_RST`；`gpio=GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38` |
| 保护电路 | M5-Bus ESD 保护 | `devices=D3-D7 SRV05-4`；`protected=GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38` |
| 接口 | 主板辅助接口 | `port_a=J4 GND,BUS_5V,GPIO32,GPIO33`；`ext_battery=J5 GND,SYS_VBAT`；`fpc=J7 BUS_5V,GND,MCU_VDD,GPIO15,GPIO5,GPIO39,GPIO21,GPIO22` |
| 总线 | Ext Board RS-485 | `transceiver=U2 SP485EEN-L/TR`；`rx=RO -> R5 1KΩ -> GPIO27`；`direction=GPIO19 -> R8 -> Q1 -> RE/DE`；`di=GND`；`a=RS485_A`；`b=RS485_B`；`supply=+5V` |
| 保护电路 | RS-485 偏置、终端与浪涌保护 | `bias_b=R4 4.7KΩ to GND`；`bias_a=R9 4.7KΩ to +5V`；`termination=R7 120Ω`；`tvs=D2-D4 SMAJ6.5CA-E3` |
| 接口 | Ext Board HY2.0 接口映射 | `J1=GPIO33 SCL; GPIO32 SDA; +5V; GND`；`J2=GPIO36 I; GPIO26 O; +5V; GND`；`J3=GPIO13 RX; GPIO14 TX; +5V; GND`；`J4=RS485_B; RS485_A; +24V; GND` |
| 复位 | HY2.0_RESET 接口 | `connector=J7 HY-2.0_RESET`；`pin1=EN`；`pin2=GPIO25`；`pin3=+5V`；`pin4=GND` |
| 接口 | Ext Board M5Stack_BUS2 | `connector=J6 M5Stack_BUS2`；`power=IN+,HPWR,+5V,GND`；`signals=EN,GPIO0,1,2,3,13,14,18,19,21,22,23,25,26,27,32,33,34,35,36,38` |

## 待确认事项

- `address.bm8563`：产品正文标称 BM8563 地址为 0x51；原理图显示 U5 BM8563 接 GPIO21/22，但未独立打印地址数值。（证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 D1-D2：U5 BM8563 SCL/SDA）
- `memory.documented-capacities`：产品正文标称 16MB Flash 与 8MB PSRAM；原理图打印 XM25QH128BHQ 和 ESPPSRAM64H 料号，但未独立打印 MB 容量字段。（证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 D1：U1/U2 存储器料号）
- `component.touch-doc-conflict`：当前原理图打印 U9 NS2009 与 R-TP，产品正文则标称 CHSC6540 电容触控，型号和触控类型不一致。（证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C4：U9 NS2009 与 R-TP 标题）
- `component.usb-uart-doc-conflict`：当前原理图打印 U3 CP2104-F03-GMR，产品正文规格则标称 CH9102，二者不一致。（证据：图 96eb13a23c36 / 第 1 页 / 主板第1页 C1：U3 CP2104-F03-GMR）
- `review.bm8563-address`：BM8563 在 K034 主板上的 I2C 地址是否固定为 0x51？；原因：地址来自产品正文，原理图未独立打印地址数值。
- `review.memory-capacity`：U1/U2 当前装配容量是否分别固定为 16MB Flash 与 8MB PSRAM？；原因：容量来自产品正文；原理图打印器件料号但没有独立 MB 容量字段。
- `review.touch-controller`：K034 当前量产触控控制器是原理图 U9 NS2009 还是产品正文 CHSC6540？；原因：当前原理图与产品正文的型号及触控类型不一致。
- `review.usb-uart`：K034 当前量产 USB-UART 器件是原理图 CP2104-F03-GMR 还是产品正文 CH9102？；原因：当前原理图与产品正文型号不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `96eb13a23c3655d826ed598b89456993ef3edd35fe6ef748823484dd3de10e96` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough-Schematics-PDF_page_01.png` |
| 2 | 1 | `ed90b8c76cce415acfda210a7ea60737b44b9039fb44e7a9613e9bb4ab343900` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough-Ext-Board-Schematics-PDF_page_01.png` |

---

源文档：`zh_CN/core/tough.md`

源文档 SHA-256：`f98096b9aa7a2bf77d4c7e204504bcb6f46f76a0ce2e0f40161d959968ff5e24`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
