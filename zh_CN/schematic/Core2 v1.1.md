# Core2 v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core2 v1.1 |
| SKU | K010-V11 |
| 产品 ID | `core2-v1-1-65056692be18` |
| 源文档 | `zh_CN/core/Core2 v1.1.md` |

## 概述

Core2 v1.1 以 U3 ESP32-D0WDQ6-V3 为主控，连接 U1 ESP-PSRAM64H、U2 XM25QH128CHIQ、40MHz 时钟、板载/ANT_IPEX 射频接口和 CH9102F USB-UART。INT_SDA/INT_SCL 总线连接 RTC8563、INA3221、AXP2101 以及显示触摸等内部外设，其中 INA3221 页明确标注 7 位地址 0x40。AXP2101 管理 BATT/VBUS、AXP_ESP、AXP_BUS_3.3V、显示/触摸/microSD/音频/马达电源，SY7088 生成 Boost_5V；主板还提供 LCD/触摸、microSD、NS4168 扬声器、震动马达、M5-Bus 和 Grove。当前 5 页未画出正文所述 MPU6886 与 SPM1423 后板，屏幕/触摸芯片型号、部分地址、容量和额定性能需另行确认。

## 检索关键词

`Core2 v1.1`、`K010-V11`、`ESP32-D0WDQ6-V3`、`ESP-PSRAM64H`、`XM25QH128CHIQ`、`AXP2101`、`INA3221`、`INA3221 0x40`、`RTC8563`、`BM8563`、`CH9102F`、`SY7088`、`ME1502CM5G`、`NS4168`、`ILI9342C`、`FT6336U`、`MPU6886`、`SPM1423`、`INT_SDA GPIO21`、`INT_SCL GPIO22`、`AXP_ESP`、`AXP_BUS_3.3V`、`AXP_LCD_EN`、`AXP_BL`、`AXP_TF`、`AXP_TP`、`AXP_SPK_EN`、`AXP_VIB`、`Boost_5V`、`BUS_5V`、`microSD`、`GPIO4 SD_CS`、`GPIO23 MOSI`、`GPIO18 SCK`、`GPIO38 MISO`、`USB-UART`、`M5Stack_BUS2`、`HY2.0-4P`、`40MHz`、`32.768kHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-D0WDQ6-V3 | 主控 SoC，连接存储、时钟、射频、内部总线、显示、USB-UART 和扩展接口 | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 A2-C3，U3 ESP32-D0WDQ6-V3 全部引脚 |
| U1 | ESP-PSRAM64H | 通过 SD0-SD3/SCK/CS 六线接口连接主控的外部 PSRAM | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 B1-C1，U1 ESP-PSRAM64H |
| U2 | XM25QH128CHIQ | 通过 SCS/SD0-SD3/SCK 连接主控的外部串行 Flash | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 C1-D1，U2 XM25QH128CHIQ |
| Y1 | 40M | ESP32 XTAL_P/XTAL_N 主晶振 | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 D2-D3，Y1 40M、R8、C11/C12 |
| E1,E2 | Antenna / ANT_IPEX | 经 L2/C14/C19 与 R14/R15 选择支路连接 LNA_IN 的射频接口 | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 B3，LNA_IN/L2/C14/C19/R14/R15/E1/E2 |
| U4 | RTC8563 | 带 32.768kHz 晶振和独立电池备份的 I2C RTC | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 C3-D4，U4 RTC8563、Y2、BT1、INT_SDA/INT_SCL |
| BT1 | Battery | RTC8563 VDD 的独立备份电池 | 图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 D4，BT1、D1、R16、AXP_VRTC |
| U16 | INA3221AIRGVR | BAT、VBUS、BUS 三通道电流/电压监测器，图注明确地址 0x40 | 图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页网格 B2-C3，U16 INA3221AIRGVR 与 I2C Addr 7-bit 40H |
| J1 | M5Stack_BUS2 | 30 针 M5-Bus，承载 GPIO、SPI、UART、I2C、I2S、电源和电池 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A1-B1，J1 M5Stack_BUS2 pins1-30 |
| U6-U10 | SRV05-4-P-T7 | M5-Bus 多组 GPIO 的四通道 ESD 保护阵列 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A2-C2，U6-U10、Rp2-Rp6 与 EXT_Gxx/GPIOxx |
| J2 | HY-2.0_IIC | GPIO33/GPIO32 与 BUS_5V/GND 的 Grove I2C 接口 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A3-A4，J2、GPIO33/GPIO32/BUS_5V 与保护器件 |
| LCD1 | M5_CORE2_LCD_10P | SPI LCD 电源、背光、复位与数据接口 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 B3-B4，LCD1 pin1-pin10 |
| CTP1 | CTP_2.0Inch | GPIO21/GPIO22 I2C、GPIO39 中断的电容触摸接口 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 C3-C4，CTP1 pin1-pin8 |
| J3 | TF-015 | GPIO4/23/18/38 SPI microSD 卡座 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D3-D4，J3 TF-015、Rp7、D9-D12 |
| U5,LS1 | NS4168 / Speaker | I2S 输入并差分驱动板载扬声器 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D1-D2，U5 NS4168 与 LS1 Speaker |
| M1 | Motor | 由 AXP_VIB 供电并带 D5 续流二极管的震动马达 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D3，M1 Motor、R24、D5、AXP_VIB |
| S1,S2 | SW-PB | AXP_PG 复位/电源良好与 AXP_PWRON 电源按键 | 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 B1-C1，S1/S2、R18/R19、D2/D3 |
| U11 | AXP2101 | BATT/VBUS 输入和多路 DC/DC/LDO/RTC/IRQ/I2C 电源管理器 | 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 A1-D3，U11 AXP2101 全部输入输出 |
| U13 | SY7088 | AXP_PS 输入、AXP_BoostEN 控制并经 D15 输出 Boost_5V 的升压器 | 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 A3-A4 Boost 虚线框，U13/L6/R39/R40/D15 |
| U12 | ME1502CM5G | 受 AXP_BoostEN 控制的 VBUS/Boost_5V/BUS_5V 电源通路器件 | 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 B3-B4，U12、VBUS、Boost_5V、BUS_5V、R52 |
| U15 (opt.) | STM32F030F4P6 | 图中 opt. 虚线框内的可选 I2C/SWD/复位协处理器 | 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 C3-D4 opt. 虚线框，U15 STM32F030F4P6 |
| USB1 | TYPEC-304S-ACP16 | VBUS 与 USB_P/USB_N 的 USB Type-C 接口 | 图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 A1-B2，USB1、P2、F1、R41/R42、D16-D18 |
| U14 | CH9102F | USB D+/D- 到 U0RX/U0TX 的 USB-UART 桥，输出 DTR/RTS 自动下载控制 | 图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 A3-B3，U14 CH9102F、USB_P/N、U0RX/U0TX、CH_DTR/CH_RTS |
| Q1,Q2 | SS8050 Y1 | CH_DTR/CH_RTS 到 AXP_PG/GPIO0 的自动复位与下载晶体管网络 | 图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 C2-D3，Q1/Q2、R43/R44、D19 |

## 系统结构

### Core2 v1.1 系统架构

U3 ESP32-D0WDQ6-V3 连接 U1 PSRAM、U2 Flash、40MHz 晶振、天线、INT I2C、LCD/触摸、microSD、NS4168、马达、M5-Bus/Grove 与 CH9102F；U11 AXP2101 和 U16 INA3221 构成电源管理与监测核心。

- 参数与网络：`soc=U3 ESP32-D0WDQ6-V3`；`psram=U1 ESP-PSRAM64H`；`flash=U2 XM25QH128CHIQ`；`pmic=U11 AXP2101`；`monitor=U16 INA3221AIRGVR`；`rtc=U4 RTC8563`；`usb_uart=U14 CH9102F`；`display=LCD1/CTP1`；`storage=J3 microSD`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页主控/存储/RTC; 图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页 INA3221; 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页接口/显示/音频; 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页 PMIC/Boost; 图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页 USB-UART

## 核心器件

### 震动马达路径

AXP_VIB 经 R24 22Ω 接 M1 Motor，一端回 GND；D5 1N4148WS T4 跨接马达两端，C27 100nF 对地。

- 参数与网络：`supply=AXP_VIB`；`series_resistor=R24 22Ω`；`motor=M1`；`flyback=D5 1N4148WS T4`；`capacitor=C27 100nF`；`return=GND`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D3，AXP_VIB/R24/M1/D5/C27

## 电源

### AXP2101 BATT/VBUS 输入与电流采样

P1 pin2 BATT 经 R50 0.01Ω 接 IN1P 和 U11 BAT pin33；VBUS 经 R51 0.01Ω 接 IN3N/U11 VBUS pin37；BUS_5V 侧经 R52 0.01Ω 形成 INA3221 BUS 通道，三条电源路径由 U16 监测。

- 参数与网络：`battery=P1 pin2 BATT -> R50 0.01Ω -> IN1P/U11 BAT`；`usb=VBUS -> R51 0.01Ω -> IN3N/U11 VBUS`；`bus=Boost_5V/BUS_5V via R52 0.01Ω`；`pmic=U11 AXP2101`；`monitor=U16 INA3221`
- 证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 A1-B2 与 B3-B4，P1/R50/R51/U11/R52; 图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页 U16 BAT/VBUS/BUS 通道

### AXP2101 受控电源轨

U11 LX1 经 L4 输出 AXP_ESP，LX3 经 L5 输出 AXP_BUS_3.3V；BLDO1 输出 AXP_BL，BLDO2 控制 AXP_BoostEN，DLDO1/DC1SW 输出 AXP_VIB，ALDO2 输出 AXP_LCD_EN，ALDO3 输出 AXP_SPK_EN，ALDO4 经 0Ω 选配支路形成 AXP_TF/AXP_TP/AXP_LCD，VRTC 输出 AXP_VRTC。

- 参数与网络：`dcdc1=LX1/L4 -> AXP_ESP`；`dcdc3=LX3/L5 -> AXP_BUS_3.3V`；`bldo1=AXP_BL`；`bldo2=AXP_BoostEN`；`dldo1=AXP_VIB`；`aldo2=AXP_LCD_EN`；`aldo3=AXP_SPK_EN`；`aldo4=0Ω branches -> AXP_TF,AXP_TP,AXP_LCD`；`vrtc=AXP_VRTC`
- 证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 B1-D3，U11 输出引脚、L4/L5 与各 AXP_* 网络

### AXP_PS 到 Boost_5V

AXP_PS 经 R36 0Ω 与 L6 3015 1.5uH 进入 U13 SY7088，EN 由 AXP_BoostEN 控制并由 R37 1MΩ 下拉；反馈为 R39 52.3KΩ/R40 15KΩ，输出经 D15 DSK34 形成 Boost_5V。

- 参数与网络：`input=AXP_PS`；`converter=U13 SY7088`；`series=R36 0Ω`；`inductor=L6 3015 1.5uH`；`enable=AXP_BoostEN,R37 1MΩ`；`feedback=R39 52.3KΩ,R40 15KΩ`；`diode=D15 DSK34`；`output=Boost_5V`
- 证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 A3-A4 Boost 虚线框

### VBUS、Boost_5V 与 BUS_5V 通路

U12 ME1502CM5G 的 VOUT pin1 接 VBUS、VIN pin5 接 Boost_5V，EN pin4 接 AXP_BoostEN，RSET pin3 经 R38 27KΩ 接 GND；Boost_5V 经 R52 0.01Ω 形成 IN2N/BUS_5V。

- 参数与网络：`device=U12 ME1502CM5G`；`vout_pin=VBUS`；`vin_pin=Boost_5V`；`enable=AXP_BoostEN`；`rset=R38 27KΩ`；`bus_path=Boost_5V -> R52 0.01Ω -> IN2N/BUS_5V`
- 证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页网格 B3-B4，U12/R38/R52/VBUS/Boost_5V/BUS_5V

## 接口

### M5Stack_BUS2 引脚

J1 30 针总线引出 EXT_G23/G38/G18/G3/G13/G21/G32/G27/G2、EXT_G35/G36/EN/G25/G26、AXP_BUS_3.3V、EXT_G1/G14/G22/G33/G19/G0/G34、BUS_5V 与 BATT，pins25/27/29 的 HPWR 标为未连接。

- 参数与网络：`left_even_or_odd=pins1/3/5 GND;7 G23;9 G38;11 G18;13 G3;15 G13;17 G21;19 G32;21 G27;23 G2`；`right=2 G35;4 G36;6 EN;8 G25;10 G26;12 AXP_BUS_3.3V;14 G1;16 G14;18 G22;20 G33;22 G19;24 G0;26 G34;28 BUS_5V;30 BATT`；`unconnected=pins25,27,29 HPWR`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A1-B1，J1 pins1-30

### J2 Grove I2C

J2 HY-2.0_IIC pin1=GPIO33/IIC_SCL、pin2=GPIO32/IIC_SDA、pin3=BUS_5V、pin4=GND；两条信号与 VCC 均有对地保护器件。

- 参数与网络：`pin1=GPIO33 IIC_SCL`；`pin2=GPIO32 IIC_SDA`；`pin3=BUS_5V`；`pin4=GND`；`direction=GPIO32/33 bidirectional`；`protection=PESDNC2FD3V3B x2,LESD3Z5.0CMT1G on VCC`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A3-A4，J2 GPIO33/GPIO32/BUS_5V/GND

## 总线

### INT_SDA/INT_SCL 内部 I2C

U3 GPIO21 形成 INT_SDA，GPIO22 形成 INT_SCL；R4/R3 各 2.2KΩ 上拉到 AXP_ESP，并连接 RTC8563、INA3221、AXP2101 及 CTP1 触摸接口。

- 参数与网络：`controller=U3 ESP32-D0WDQ6-V3`；`sda=GPIO21 INT_SDA`；`scl=GPIO22 INT_SCL`；`pullups=R4/R3 2.2KΩ to AXP_ESP`；`devices_shown=U4 RTC8563,U16 INA3221,U11 AXP2101,CTP1`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页 U3 GPIO21/22、R3/R4、U4; 图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页 U16 SCL/SDA; 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页 U11 SDA/SCK

### LCD SPI 与 PMIC 控制

LCD1 pin2 MOSI=GPIO23、pin3 MISO=GPIO38、pin4 SCK=GPIO18、pin5 CS=GPIO5、pin6 RST=AXP_LCD_EN、pin7 D/C=GPIO15、pin8 VDD=AXP_LCD、pin9 LED_A=AXP_BL，pins1/10/0 为 GND。

- 参数与网络：`mosi=GPIO23`；`miso=GPIO38 via R28 22Ω`；`sck=GPIO18 via R25 220Ω FB`；`cs=GPIO5`；`reset=AXP_LCD_EN`；`dc=GPIO15`；`power=AXP_LCD`；`backlight=AXP_BL`；`connector=LCD1 M5_CORE2_LCD_10P`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 B3-B4，LCD1/R25/R28/AXP_LCD_EN/AXP_LCD/AXP_BL

### 电容触摸 I2C 与中断

CTP1 pin1 VDD=AXP_TP、pin2 GND、pin3 SDA=GPIO21、pin4 SCL=GPIO22、pin5 INT=GPIO39、pin6 RST=AXP_LCD_EN，pins7/8 NC；C30 100nF 为 AXP_TP 去耦。

- 参数与网络：`connector=CTP1 CTP_2.0Inch`；`supply=AXP_TP`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=AXP_LCD_EN`；`nc=pins7,8`；`decoupling=C30 100nF`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 C3-C4，CTP1 pins1-8

## 总线地址

### INA3221 I2C 地址

U16 INA3221AIRGVR 的 A0 pin5 接 GND，页面明确标注 I2C Addr 7-bit 40H，因此其 7 位地址为 0x40。

- 参数与网络：`device=U16 INA3221AIRGVR`；`address_pin=A0 GND`；`address_7bit=0x40`；`bus=INT_SDA/INT_SCL`
- 证据：图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页网格 B3-C3，U16 A0 与 I2C Addr 7-bit 40H 文字

## 时钟

### ESP32 40MHz 主时钟

Y1 标注 40M，XO/XI 分别连接 X_N/X_P 到 U3 XTAL_N/XTAL_P；R8 0Ω 串接 X_P，C11/C12 各 12pF 对地。

- 参数与网络：`crystal=Y1 40M`；`mcu=U3 ESP32-D0WDQ6-V3`；`pins=XTAL_P/XTAL_N`；`series=R8 0Ω`；`load_caps=C11 12pF,C12 12pF`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 D2-D3，Y1/R8/C11/C12/X_P/X_N

### RTC 32.768kHz 时钟与备份

U4 RTC8563 OSCI/OSCO 连接 Y2 32.768kHz±20ppm，并各配 C16/C17 6.0pF 对地；VDD 节点由 AXP_VRTC 经 D1 B5819WT/R16 100Ω 和 BT1 备份电池共同连接。

- 参数与网络：`rtc=U4 RTC8563`；`crystal=Y2 32.768kHz±20ppm`；`caps=C16/C17 6.0pF`；`main_supply=AXP_VRTC -> D1 B5819WT -> R16 100Ω`；`backup=BT1 Battery`；`interrupt=AXP_WAKEUP`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 C3-D4，U4/Y2/C16/C17/D1/R16/BT1

## 复位

### 复位与电源按键

S1 按下经 R18 47Ω 拉低 AXP_PG，S2 按下经 R19 510Ω 拉低 AXP_PWRON；D2/D3 提供 ESD 保护，C23/C24 各 1nF 对地。EXT_EN 经 R22 22Ω 接 AXP_PG 并由 D4 保护。

- 参数与网络：`reset=S1 -> R18 47Ω -> AXP_PG`；`power=S2 -> R19 510Ω -> AXP_PWRON`；`esd=D2/D3/D4 PESDNC2FD3V3B`；`caps=C23/C24 1nF`；`external_enable=EXT_EN -> R22 22Ω -> AXP_PG`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 B1-C2，S1/S2/R18/R19/C23/C24/R22/D2-D4

### CH9102F 自动复位与下载

CH_DTR 经 R43 10KΩ 驱动 Q1 SS8050 Y1 并控制 AXP_PG，CH_RTS 经 R44 10KΩ 驱动 Q2 SS8050 Y1，Q2 输出经 D19 1N4148WS T4 控制 GPIO0；两晶体管采用交叉连接。

- 参数与网络：`dtr=CH_DTR -> R43 10KΩ -> Q1 -> AXP_PG`；`rts=CH_RTS -> R44 10KΩ -> Q2 -> D19 -> GPIO0`；`transistors=Q1/Q2 SS8050 Y1`；`diode=D19 1N4148WS T4`；`topology=cross-coupled auto-program`
- 证据：图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 C2-D3，CH_DTR/CH_RTS/R43/R44/Q1/Q2/D19

## 保护电路

### M5-Bus GPIO 保护

EXT_G36/G35/G25/G23、EXT_G26/G38/G18/G3、EXT_G1/G13/G14/G21、EXT_G32/G22/G27/G33、EXT_G2/G19/G0/G34 各经 Rp2-Rp6 33Ω 阵列后进入 U6-U10 SRV05-4-P-T7 ESD 阵列并连接内部 GPIO。

- 参数与网络：`series_arrays=Rp2-Rp6 33Ω`；`esd_arrays=U6-U10 SRV05-4-P-T7`；`reference=AXP_ESP`；`protected_groups=G36/G35/G25/G23;G26/G38/G18/G3;G1/G13/G14/G21;G32/G22/G27/G33;G2/G19/G0/G34`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 A2-C2，Rp2-Rp6/U6-U10

### USB 电源与数据保护

USB1 CC1/CC2 分别经 R41/R42 5.1KΩ 接 GND，VBUS 串 F1 6V/1A；D16 LESD3Z5.0CMT1G 保护 VBUS，D17/D18 PESDNC2FD3V3B 分别保护 USB_P/USB_N。

- 参数与网络：`cc=R41/R42 5.1KΩ`；`overcurrent=F1 6V/1A`；`vbus_esd=D16 LESD3Z5.0CMT1G`；`data_esd=D17 USB_P,D18 USB_N PESDNC2FD3V3B`
- 证据：图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 A1-B2，USB1/R41/R42/F1/D16-D18

## 存储

### microSD SPI 映射

J3 TF-015 pin2 CS=GPIO4、pin3 MOSI=GPIO23、pin5 CLK=GPIO18、pin7 MISO=GPIO38，经 Rp7 33Ω 阵列连接；pin4 VCC=AXP_TF，pins6/0 GND，D9-D12 对四条信号做 ESD 保护。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`clk=GPIO18`；`miso=GPIO38`；`series=Rp7 33Ω`；`supply=AXP_TF`；`esd=D9-D12 PESDNC2FD3V3B`；`connector=J3 TF-015`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D3-D4，J3/Rp7/D9-D12/AXP_TF

## 内存与 Flash

### PSRAM 与 Flash 连接

U1 ESP-PSRAM64H 与 U2 XM25QH128CHIQ 共用 U3 的 SCS/CMD、SD0/SD0、SWP/SD3、SHD/SD2、SDI/SD1、SCK/CLK 专用存储总线，U1 CE 另由 GPIO16 控制，二者由 VDD_SDIO 供电。

- 参数与网络：`psram=U1 ESP-PSRAM64H`；`flash=U2 XM25QH128CHIQ`；`bus=SCS/CMD,SD0/SD0,SWP/SD3,SHD/SD2,SDI/SD1,SCK/CLK`；`psram_ce=GPIO16`；`supply=VDD_SDIO`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 B1-D2，U1/U2 与 U3 SD_* 引脚

## 音频

### NS4168 I2S 扬声器

U5 NS4168 的 LRCLK/BCLK/SDATA 分别经 Rp1 33Ω 接 GPIO0/GPIO12/GPIO2，CTRL 接 AXP_SPK_EN，VDD 接 AXP_BUS_3.3V；VON/VOP 差分输出驱动 LS1 Speaker，VOP 串 R23 4.7Ω。

- 参数与网络：`amplifier=U5 NS4168`；`lrclk=GPIO0`；`bclk=GPIO12`；`sdata=GPIO2`；`enable=AXP_SPK_EN`；`supply=AXP_BUS_3.3V`；`speaker=LS1 differential VON/VOP`；`series=R23 4.7Ω on VOP`
- 证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页网格 D1-D2，Rp1/U5/LS1/R23

## 射频

### 板载与 IPEX 天线路径

U3 LNA_IN 经 L2 1.8nH 和 C14 2.4pF/C19 1.5pF 匹配节点后，通过 R14 0Ω 到 E1 Antenna，并通过 R15 0Ω 到 E2 ANT_IPEX。

- 参数与网络：`mcu_pin=U3 LNA_IN`；`series=L2 1.8nH`；`shunt=C14 2.4pF,C19 1.5pF`；`onboard=R14 0Ω -> E1 Antenna`；`external=R15 0Ω -> E2 ANT_IPEX`
- 证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页网格 B3，LNA_IN/L2/C14/C19/R14/R15/E1/E2

## 调试与烧录

### USB Type-C 到 CH9102F UART

USB1 DP1/DP2 汇合为 USB_P、DN1/DN2 汇合为 USB_N 并连接 U14 CH9102F D+/D-；U14 TXD 接 U0RX，RXD 接 U0TX，DTR/RTS 输出 CH_DTR/CH_RTS，VBUS 经 F1 6V/1A 进入系统。

- 参数与网络：`connector=USB1 TYPEC-304S-ACP16`；`bridge=U14 CH9102F`；`usb=USB_P/USB_N`；`uart=TXD -> U0RX,RXD -> U0TX`；`control=DTR CH_DTR,RTS CH_RTS`；`fuse=F1 6V/1A`；`alternate_header=P2 5V/GND/DM/DP`
- 证据：图 bd832bf30574 / 第 1 页 / 第 5 张第 1 页网格 A1-B3，USB1/P2/F1/U14

## 模拟电路

### INA3221 三通道监测

U16 CH1N/CH1P、CH2N/CH2P、CH3N/CH3P 分别接 IN-1/IN+1、IN-2/IN+2、IN-3/IN+3，页面网络标识对应 BAT、VBUS、BUS；每对输入通过 R53-R58 10Ω 与 C67-C69 100nF 形成差分滤波。

- 参数与网络：`channel1=BAT / CH1N-CH1P`；`channel2=VBUS / CH2N-CH2P`；`channel3=BUS / CH3N-CH3P`；`series=R53-R58 10Ω`；`filters=C67-C69 100nF`；`supply=AXP_ESP`；`vpu=BUS_5V`
- 证据：图 1a15f5707b6e / 第 1 页 / 第 2 张第 1 页网格 B1-C3，R53-R58/C67-C69/U16 三通道

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Core2 v1.1 系统架构 | `soc=U3 ESP32-D0WDQ6-V3`；`psram=U1 ESP-PSRAM64H`；`flash=U2 XM25QH128CHIQ`；`pmic=U11 AXP2101`；`monitor=U16 INA3221AIRGVR`；`rtc=U4 RTC8563`；`usb_uart=U14 CH9102F`；`display=LCD1/CTP1`；`storage=J3 microSD` |
| 内存与 Flash | PSRAM 与 Flash 连接 | `psram=U1 ESP-PSRAM64H`；`flash=U2 XM25QH128CHIQ`；`bus=SCS/CMD,SD0/SD0,SWP/SD3,SHD/SD2,SDI/SD1,SCK/CLK`；`psram_ce=GPIO16`；`supply=VDD_SDIO` |
| 时钟 | ESP32 40MHz 主时钟 | `crystal=Y1 40M`；`mcu=U3 ESP32-D0WDQ6-V3`；`pins=XTAL_P/XTAL_N`；`series=R8 0Ω`；`load_caps=C11 12pF,C12 12pF` |
| 射频 | 板载与 IPEX 天线路径 | `mcu_pin=U3 LNA_IN`；`series=L2 1.8nH`；`shunt=C14 2.4pF,C19 1.5pF`；`onboard=R14 0Ω -> E1 Antenna`；`external=R15 0Ω -> E2 ANT_IPEX` |
| 总线 | INT_SDA/INT_SCL 内部 I2C | `controller=U3 ESP32-D0WDQ6-V3`；`sda=GPIO21 INT_SDA`；`scl=GPIO22 INT_SCL`；`pullups=R4/R3 2.2KΩ to AXP_ESP`；`devices_shown=U4 RTC8563,U16 INA3221,U11 AXP2101,CTP1` |
| 时钟 | RTC 32.768kHz 时钟与备份 | `rtc=U4 RTC8563`；`crystal=Y2 32.768kHz±20ppm`；`caps=C16/C17 6.0pF`；`main_supply=AXP_VRTC -> D1 B5819WT -> R16 100Ω`；`backup=BT1 Battery`；`interrupt=AXP_WAKEUP` |
| 总线地址 | INA3221 I2C 地址 | `device=U16 INA3221AIRGVR`；`address_pin=A0 GND`；`address_7bit=0x40`；`bus=INT_SDA/INT_SCL` |
| 模拟电路 | INA3221 三通道监测 | `channel1=BAT / CH1N-CH1P`；`channel2=VBUS / CH2N-CH2P`；`channel3=BUS / CH3N-CH3P`；`series=R53-R58 10Ω`；`filters=C67-C69 100nF`；`supply=AXP_ESP`；`vpu=BUS_5V` |
| 接口 | M5Stack_BUS2 引脚 | `left_even_or_odd=pins1/3/5 GND;7 G23;9 G38;11 G18;13 G3;15 G13;17 G21;19 G32;21 G27;23 G2`；`right=2 G35;4 G36;6 EN;8 G25;10 G26;12 AXP_BUS_3.3V;14 G1;16 G14;18 G22;20 G33;22 G19;24 G0;26 G34;28 BUS_5V;30 BATT`；`unconnected=pins25,27,29 HPWR` |
| 保护电路 | M5-Bus GPIO 保护 | `series_arrays=Rp2-Rp6 33Ω`；`esd_arrays=U6-U10 SRV05-4-P-T7`；`reference=AXP_ESP`；`protected_groups=G36/G35/G25/G23;G26/G38/G18/G3;G1/G13/G14/G21;G32/G22/G27/G33;G2/G19/G0/G34` |
| 接口 | J2 Grove I2C | `pin1=GPIO33 IIC_SCL`；`pin2=GPIO32 IIC_SDA`；`pin3=BUS_5V`；`pin4=GND`；`direction=GPIO32/33 bidirectional`；`protection=PESDNC2FD3V3B x2,LESD3Z5.0CMT1G on VCC` |
| 总线 | LCD SPI 与 PMIC 控制 | `mosi=GPIO23`；`miso=GPIO38 via R28 22Ω`；`sck=GPIO18 via R25 220Ω FB`；`cs=GPIO5`；`reset=AXP_LCD_EN`；`dc=GPIO15`；`power=AXP_LCD`；`backlight=AXP_BL`；`connector=LCD1 M5_CORE2_LCD_10P` |
| 总线 | 电容触摸 I2C 与中断 | `connector=CTP1 CTP_2.0Inch`；`supply=AXP_TP`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO39`；`reset=AXP_LCD_EN`；`nc=pins7,8`；`decoupling=C30 100nF` |
| 存储 | microSD SPI 映射 | `cs=GPIO4`；`mosi=GPIO23`；`clk=GPIO18`；`miso=GPIO38`；`series=Rp7 33Ω`；`supply=AXP_TF`；`esd=D9-D12 PESDNC2FD3V3B`；`connector=J3 TF-015` |
| 音频 | NS4168 I2S 扬声器 | `amplifier=U5 NS4168`；`lrclk=GPIO0`；`bclk=GPIO12`；`sdata=GPIO2`；`enable=AXP_SPK_EN`；`supply=AXP_BUS_3.3V`；`speaker=LS1 differential VON/VOP`；`series=R23 4.7Ω on VOP` |
| 核心器件 | 震动马达路径 | `supply=AXP_VIB`；`series_resistor=R24 22Ω`；`motor=M1`；`flyback=D5 1N4148WS T4`；`capacitor=C27 100nF`；`return=GND` |
| 复位 | 复位与电源按键 | `reset=S1 -> R18 47Ω -> AXP_PG`；`power=S2 -> R19 510Ω -> AXP_PWRON`；`esd=D2/D3/D4 PESDNC2FD3V3B`；`caps=C23/C24 1nF`；`external_enable=EXT_EN -> R22 22Ω -> AXP_PG` |
| 电源 | AXP2101 BATT/VBUS 输入与电流采样 | `battery=P1 pin2 BATT -> R50 0.01Ω -> IN1P/U11 BAT`；`usb=VBUS -> R51 0.01Ω -> IN3N/U11 VBUS`；`bus=Boost_5V/BUS_5V via R52 0.01Ω`；`pmic=U11 AXP2101`；`monitor=U16 INA3221` |
| 电源 | AXP2101 受控电源轨 | `dcdc1=LX1/L4 -> AXP_ESP`；`dcdc3=LX3/L5 -> AXP_BUS_3.3V`；`bldo1=AXP_BL`；`bldo2=AXP_BoostEN`；`dldo1=AXP_VIB`；`aldo2=AXP_LCD_EN`；`aldo3=AXP_SPK_EN`；`aldo4=0Ω branches -> AXP_TF,AXP_TP,AXP_LCD`；`vrtc=AXP_VRTC` |
| 电源 | AXP_PS 到 Boost_5V | `input=AXP_PS`；`converter=U13 SY7088`；`series=R36 0Ω`；`inductor=L6 3015 1.5uH`；`enable=AXP_BoostEN,R37 1MΩ`；`feedback=R39 52.3KΩ,R40 15KΩ`；`diode=D15 DSK34`；`output=Boost_5V` |
| 电源 | VBUS、Boost_5V 与 BUS_5V 通路 | `device=U12 ME1502CM5G`；`vout_pin=VBUS`；`vin_pin=Boost_5V`；`enable=AXP_BoostEN`；`rset=R38 27KΩ`；`bus_path=Boost_5V -> R52 0.01Ω -> IN2N/BUS_5V` |
| 调试与烧录 | USB Type-C 到 CH9102F UART | `connector=USB1 TYPEC-304S-ACP16`；`bridge=U14 CH9102F`；`usb=USB_P/USB_N`；`uart=TXD -> U0RX,RXD -> U0TX`；`control=DTR CH_DTR,RTS CH_RTS`；`fuse=F1 6V/1A`；`alternate_header=P2 5V/GND/DM/DP` |
| 复位 | CH9102F 自动复位与下载 | `dtr=CH_DTR -> R43 10KΩ -> Q1 -> AXP_PG`；`rts=CH_RTS -> R44 10KΩ -> Q2 -> D19 -> GPIO0`；`transistors=Q1/Q2 SS8050 Y1`；`diode=D19 1N4148WS T4`；`topology=cross-coupled auto-program` |
| 保护电路 | USB 电源与数据保护 | `cc=R41/R42 5.1KΩ`；`overcurrent=F1 6V/1A`；`vbus_esd=D16 LESD3Z5.0CMT1G`；`data_esd=D17 USB_P,D18 USB_N PESDNC2FD3V3B` |
| 内存与 Flash | 16MB Flash 与 8MB PSRAM | `flash_part=XM25QH128CHIQ`；`documented_flash=16MB`；`psram_part=ESP-PSRAM64H`；`documented_psram=8MB`；`schematic_capacity_fields=null` |
| 总线地址 | AXP2101、RTC、触摸与 IMU 地址 | `documented_axp2101=0x34`；`documented_rtc=0x51`；`documented_touch=0x38`；`documented_mpu6886=0x68`；`schematic_confirmed=INA3221 0x40 only`；`mpu6886_shown=false` |
| 核心器件 | RTC8563 与 BM8563 命名 | `schematic_part=RTC8563`；`documented_part=BM8563`；`documented_address=0x51`；`production_part=null` |
| 核心器件 | LCD 与触摸控制器规格 | `documented_lcd=ILI9342C`；`documented_size=2.0 inch`；`documented_resolution=320x240`；`documented_touch=FT6336U`；`lcd_connector=LCD1 M5_CORE2_LCD_10P`；`touch_connector=CTP1 CTP_2.0Inch`；`schematic_controller_parts=null` |
| 传感器 | MPU6886 与 SPM1423 后板 | `documented_imu=MPU6886`；`documented_microphone=SPM1423`；`documented_mic_clk=GPIO0`；`documented_mic_data=GPIO34`；`schematic_imu=null`；`schematic_microphone=null`；`rear_board_asset=null` |
| 电源 | 500mAh 电池与 PMU 性能 | `documented_battery=500mAh@3.7V`；`documented_input=5V@500mA`；`documented_charge_current=100mA`；`documented_charge_efficiency=94%`；`documented_termination_current=10mA`；`documented_discharge_efficiency=96%`；`cell_part_number=null`；`protection=null`；`temperature_monitor=null` |
| 音频 | 扬声器与麦克风性能 | `amplifier=NS4168`；`documented_power=1W`；`documented_microphone=SPM1423`；`speaker_impedance=null`；`measured_power=null`；`thd=null`；`microphone_specs=null` |
| 射频 | 2.4G 3D 天线性能 | `onboard=E1 Antenna`；`external=E2 ANT_IPEX`；`matching=L2/C14/C19/R14/R15`；`gain=null`；`efficiency=null`；`range=null`；`return_loss=null`；`selected_path=null` |
| 核心器件 | 可选 STM32F030F4P6 装配 | `reference=U15`；`part_number=STM32F030F4P6`；`marked_optional=true`；`interfaces=INT_SDA,INT_SCL,SWCLK,SWDIO,NRST`；`supply=AXP_ESP`；`population=null`；`firmware_role=null` |

## 待确认事项

- `memory.documented-capacities`：原理图标 U2 XM25QH128CHIQ 和 U1 ESP-PSRAM64H，正文解释为 16MB Flash 与 8MB PSRAM；图中没有单独容量字段，容量换算需由对应芯片 datasheet 或实机确认。（证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页 U1/U2 型号与总线，无容量文字）
- `address.documented-internal-devices`：正文给出 AXP2101=0x34、BM8563=0x51、FT6336U=0x38、MPU6886=0x68；原理图只明确 INA3221=0x40，未在 U11、U4 或 CTP1 旁标出这些地址，且当前 5 页未出现 MPU6886 器件。（证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页 U4 RTC8563，无地址文字; 图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页 CTP1 仅接口，无触摸 IC 型号/地址; 图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页 U11 AXP2101，无地址文字）
- `component.rtc-name`：原理图 U4 器件文字为 RTC8563，而正文和管脚表称 BM8563；两者命名对应关系及量产料号无法仅从当前页面确认。（证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页 U4 器件文字 RTC8563）
- `component.documented-display-touch`：正文称 LCD 为 ILI9342C、2.0英寸、320×240，触摸控制器为 FT6336U；原理图只显示 LCD1/CTP1 连接器、信号和电源，未画出面板控制器位号、型号、尺寸或分辨率。（证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页 LCD1/CTP1 接口区，无 ILI9342C/FT6336U/320x240 文字）
- `sensor.documented-rear-board`：正文称背部扩展小板集成 MPU6886 六轴 IMU 与 SPM1423 PDM 麦克风；当前资源的 5 张页面没有出现这两个器件位号、型号或其 GPIO 连接，无法确认后板版本和实际网络。（证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页完整外设页仅有 NS4168/显示/触摸/microSD/马达，无 MPU6886/SPM1423）
- `power.documented-battery-performance`：正文称 500mAh@3.7V 电池、5V@500mA 输入，并给出 AXP2101 充电电流/效率/终止电流和输出效率；原理图只显示 P1、R50、AXP2101、INA3221 与电源轨，未标电芯型号、容量、保护板、温度监测或这些性能测试条件。（证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页 P1/R50/U11 电池与 PMIC 区，无容量/性能表）
- `audio.documented-performance`：正文称 NS4168 扬声器功放输出 1W，并使用 SPM1423 麦克风；原理图确认 NS4168/LS1 连接但未标扬声器阻抗、额定功率、失真或声学条件，且 SPM1423 未出现在当前 5 页。（证据：图 e888a2efb774 / 第 1 页 / 第 3 张第 1 页 U5/LS1 音频区，无额定性能或麦克风电路）
- `rf.documented-performance`：原理图确认 E1 板载 Antenna、E2 ANT_IPEX 和匹配网络，但正文的 2.4G 3D 天线描述未在图中量化增益、效率、范围、回波损耗、天线选择 BOM 或认证结果。（证据：图 af3beb20f220 / 第 1 页 / 第 1 张第 1 页射频区 E1/E2/R14/R15，无性能表或装配说明）
- `component.optional-stm32`：第 4 页以 opt. 虚线框画出 U15 STM32F030F4P6、SWD、NRST、INT_SDA/INT_SCL 与 AXP_ESP，但原理图未说明该器件在 K010-V11 量产板上是否装配及固件职责。（证据：图 47c7f164ed30 / 第 1 页 / 第 4 张第 1 页 C3-D4 opt. 虚线框 U15）
- `review.memory-capacities`：请用 XM25QH128CHIQ 与 ESP-PSRAM64H datasheet 或实机确认 16MB Flash 和 8MB PSRAM。；原因：原理图只标芯片型号，未写容量字段。
- `review.internal-addresses`：请确认 AXP2101=0x34、RTC=0x51、FT6336U=0x38、MPU6886=0x68，并说明地址脚与后板连接。；原因：当前原理图只明确 INA3221=0x40。
- `review.rtc-part`：K010-V11 量产 RTC 的正式料号是 RTC8563 还是 BM8563，且其 7 位地址是否为 0x51？；原因：原理图和产品正文命名不一致。
- `review.display-touch`：请用屏幕/触摸模组 BOM 或丝印确认 ILI9342C、FT6336U、2.0英寸、320×240 及初始化参数。；原因：当前原理图只有 LCD1/CTP1 接口。
- `review.rear-board`：请提供 K010-V11 后板原理图/BOM，确认 MPU6886、SPM1423、GPIO0/GPIO34 及其供电/中断网络。；原因：当前 5 张资源未包含 IMU 和麦克风器件。
- `review.battery-performance`：请确认 500mAh@3.7V 电芯型号、保护/温度配置，以及 AXP2101 充电与输出性能的测试条件。；原因：这些容量与性能数据未标在原理图。
- `review.audio-performance`：请用扬声器 BOM、NS4168/SPM1423 datasheet 和整机实测确认 1W、阻抗、失真及麦克风参数。；原因：连接图不能证明额定音频性能，麦克风页缺失。
- `review.rf-performance`：请确认 E1/E2 的量产装配选择，并提供天线增益、效率、范围、回波损耗和认证结果。；原因：原理图只给出并列天线路径和匹配元件。
- `review.optional-stm32`：K010-V11 量产板是否装配 U15 STM32F030F4P6；若装配，其固件版本和 AXP/I2C 职责是什么？；原因：器件位于 opt. 虚线框，未给出装配状态。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `af3beb20f220ef8af4930e0e4411dada39e5b37078ca710366e4d1d975e29360` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_01.png` |
| 2 | 1 | `1a15f5707b6ec0436c735064b0b2c583a24d741ad998c75fda368ea5494f4d3d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_02.png` |
| 3 | 1 | `e888a2efb7743d521c2961b2cf591859007cbc79e7ffc013a389964ae96d04ff` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_03.png` |
| 4 | 1 | `47c7f164ed307288f1dc402f1452164f909e16cb6048721febb2fe51028c50ba` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_04.png` |
| 5 | 1 | `bd832bf305740fd3136230c4e4184daf1e0982525505a254d0d77d3b0e2e0ea4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_05.png` |

---

源文档：`zh_CN/core/Core2 v1.1.md`

源文档 SHA-256：`93075c920447450ff766292ffdffbbdd970eda0b5c625bc79972ffb06dfd9a36`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
