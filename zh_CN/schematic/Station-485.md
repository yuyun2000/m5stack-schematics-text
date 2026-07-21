# Station-485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Station-485 |
| SKU | K123 |
| 产品 ID | `station-485-a0c0e6720492` |
| 源文档 | `zh_CN/core/station_485.md` |

## 概述

Station-485 以 U3 ESP32-D0WDQ6 为主控，配套 W25Q128、CH9102F、MPU-6886、BM8563、SPI TFT、7 颗 SK6812 和三枚用户按键。AXP192 管理 USB/电池输入及主控、RTC、背光电源，SCT12A0DHKR 提供电池升压，SY8303 将 PWR485 输入降压到 5 V。六路 Grove/USB-A 负载由 SGM2553D 分路，INA3221 0x40/0x41 和 INA199 采样；SP3485 提供带保护的 RS-485。

## 检索关键词

`Station-485`、`K123`、`ESP32-D0WDQ6`、`W25Q128JVPIQ`、`CH9102F`、`MPU-6886`、`BM8563`、`AXP192`、`SP3485`、`SY8303`、`SCT12A0DHKR`、`INA3221`、`INA199A1DCKR`、`SGM2553DYTD16G/TR`、`0x40`、`0x41`、`RS485`、`PWR485`、`USB Type-C`、`USB-A power output`、`HY2.0-4P`、`SK6812_3535`、`GPIO37`、`GPIO38`、`GPIO39`、`GPIO21`、`GPIO22`、`GPIO2`、`GPIO1`、`GPIO3`、`BUS_P050`、`USB_P050`、`SYS_BAT`、`MCU_VDD`、`LCD_BL`、`RTC_VDD`、`32.768K`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| UE1 | SP3485 | GPIO1/GPIO3/GPIO2 控制的半双工 RS-485 收发器 | 图 9abe5c6bdfb6 / 第 1 页 / A2，UE1 RS-485 收发器，GPIO3/GPIO1/GPIO2 与 RS_A/RS_B |
| JE1/JE2 | HT3.96_4P / 1.25MM_4P_立贴 | 外部和内部 PWR485 连接器，提供 RS_A、RS_B、VIN_12V 与 GND | 图 9abe5c6bdfb6 / 第 1 页 / A1-B1，JE1/JE2 PWR485 连接器 |
| UE2 | SY8303 | VIN_12V 到 USB_P050 的降压转换器 | 图 9abe5c6bdfb6 / 第 1 页 / B1-B2，UE2 SY8303、L4 10UH、VIN_12V/USB_P050 |
| U3 | ESP32-D0WDQ6 | 系统主控，连接显示、USB-UART、I2C、RS-485、按键、RGB 和 Grove GPIO | 图 cc25a3bc6d25 / 第 1 页 / A3-C4，U3 ESP32-D0WDQ6 全部 GPIO 网络 |
| U4 | W25Q128JVPIQ | ESP32 外部 SPI Flash | 图 cc25a3bc6d25 / 第 1 页 / C3-D3，U4 W25Q128JVPIQ、GPIO6/7/8/9/10/11 |
| U1 | CH9102F | USB 转 UART 下载桥接器，带 DTR/RTS 自动下载控制 | 图 cc25a3bc6d25 / 第 1 页 / A2-B3，U1 CH9102F、SER_DP/DM、GPIO1/GPIO3、DTR/RTS |
| J1 | TYPEC | USB 供电与 CH9102F 数据接口 | 图 cc25a3bc6d25 / 第 1 页 / A1，J1 TYPEC、USB_P050、SER_DP/SER_DM、FU1 |
| ANT1/ANT2 | 五金3D天线 / KH-IPEX-K501-29 | 板载与 IPEX 可选射频天线路径 | 图 cc25a3bc6d25 / 第 1 页 / A3-A4，ANT1 五金3D天线、ANT2 KH-IPEX-K501-29、R12 DNP/R53 0R |
| X1 | X2520M4B40S | ESP32 40 MHz 主晶体 | 图 cc25a3bc6d25 / 第 1 页 / B3-C4，X1 X2520M4B40S、XTAL_P/XTAL_N |
| U2 | MPU-6886 | 系统 I2C 惯性传感器 | 图 cc25a3bc6d25 / 第 1 页 / C2-C3，U2 MPU-6886、GPIO21/GPIO22/GPIO27 |
| LED1-LED7 | SK6812_3535 | GPIO4 驱动的七颗串联可寻址 RGB LED | 图 cc25a3bc6d25 / 第 1 页 / C1-D3，LED1-LED7 SK6812_3535 串联链 |
| S1/S2/S3/S4 | SW | GPIO37/GPIO38/GPIO39 三枚用户按键与 PWR_KEY 电源按键 | 图 cc25a3bc6d25 / 第 1 页 / C1，S1 GPIO37、S2 GPIO38、S3 GPIO39、S4 PWR_KEY |
| J2 | FPC_8P后翻 | SPI TFT 显示与背光连接器 | 图 cc25a3bc6d25 / 第 1 页 / C4-D4，J2 FPC_8P，SCK/MOSI/RS/CS/RESET/LEDA/VDD |
| U7 | AXP192 | USB/电池输入、电池充电、系统电源、RTC 与 LCD 背光管理 PMIC | 图 5b1d9bbc2949 / 第 1 页 / A2-C2，U7 AXP192 全部电源、I2C 与 GPIO 网络 |
| U5 | BM8563 | 低功耗 I2C RTC，INT 参与电源唤醒 | 图 5b1d9bbc2949 / 第 1 页 / C1-D1，U5 BM8563、GPIO21/GPIO22、PWR_KEY、RTC_VDD |
| X2 | 32.768K | BM8563 RTC 晶体 | 图 5b1d9bbc2949 / 第 1 页 / D1，X2 32.768K、C28/C29 6PF |
| U6 | SCT12A0DHKR | SYS_BAT 到 BUS_P050 的升压转换器 | 图 5b1d9bbc2949 / 第 1 页 / C2-D3，U6 SCT12A0DHKR、L2、SYS_BAT/BUS_P050 |
| U8/U16 | INA3221 | 六路 Grove 分支电压电流监测器，地址 0x41 与 0x40 | 图 5b1d9bbc2949 / 第 1 页 / A3-A4，U8 INA3221 0X41、U16 INA3221 0X40 |
| U9/U11/U12/U13/U14/U10 | SGM2553DYTD16G/TR | Port A、B1、B2、C1、C2 与 USB-A 六路独立负载开关 | 图 5b1d9bbc2949 / 第 1 页 / A3-D4，六颗 SGM2553DYTD16G/TR 与 PS0-PS4/SP1-SP7 |
| U15 | INA199A1DCKR | USB-A 输出电流采样放大器 | 图 5b1d9bbc2949 / 第 1 页 / D3-D4，U15 INA199A1DCKR、SP7/SN7/MCU_VDD |
| J4/J5/J6/J7/J8/J9 | GROVE | Port A1/A2/B1/B2/C1/C2 六组 Grove 扩展接口 | 图 5b1d9bbc2949 / 第 1 页 / A4-D4，J4-J9 Grove 接口及 GPIO/5V/GND |
| J3 | USB-A | 仅电源输出的 USB Type-A 连接器 | 图 5b1d9bbc2949 / 第 1 页 / D4，J3 USB-A，VCC=SN7，DM/DP 未连接 |
| JE3 | 1.25MM_4P_立贴 | 内部 SYS_BAT 电池连接器 | 图 5b1d9bbc2949 / 第 1 页 / A1，JE3 1.25MM_4P_立贴、SYS_BAT/GND |

## 系统结构

### 系统架构

ESP32-D0WDQ6 连接外部 Flash、CH9102F、MPU-6886、BM8563、SPI TFT、7 颗 RGB、按键和 RS-485；AXP192 与 SCT12A0DHKR 管理 USB/电池/端口电源。

- 参数与网络：`controller=U3 ESP32-D0WDQ6`；`flash=U4 W25Q128JVPIQ`；`usb_uart=U1 CH9102F`；`imu=U2 MPU-6886`；`rtc=U5 BM8563`；`pmic=U7 AXP192`；`boost=U6 SCT12A0DHKR`；`rs485=UE1 SP3485`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / PWR485 与 SY8303 子板; 图 cc25a3bc6d25 / 第 1 页 / ESP32、Flash、USB-UART、IMU、显示与人机接口; 图 5b1d9bbc2949 / 第 1 页 / AXP192、RTC、升压与分路电源

## 电源

### PWR485 降压

VIN_12V 经 FE1 自恢复保险丝进入 UE2 SY8303，经 L4 10 µH 输出 USB_P050，并经 FE2 自恢复保险丝保护输出。

- 参数与网络：`input=VIN_12V`；`input_fuse=FE1 BSMD0805-050-24V`；`converter=UE2 SY8303`；`inductor=L4 10UH`；`output_fuse=FE2 BSMD0805-110-6V`；`output=USB_P050`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / B1-B2，FE1/UE2/L4/FE2

### AXP192 电源管理

U7 AXP192 接收 USB_P050 与 SYS_BAT，DCDC1 经 L3 输出 MCU_VDD，LDO1 输出 RTC_VDD，LDO3 经 R26 输出 LCD_BL，并连接 GPIO21/22 I2C。

- 参数与网络：`reference=U7`；`part_number=AXP192`；`usb_input=USB_P050`；`battery=SYS_BAT`；`dcdc1=MCU_VDD via L3`；`ldo1=RTC_VDD`；`ldo3=LCD_BL via R26 4.7R`；`sda=GPIO21`；`scl=GPIO22`
- 证据：图 5b1d9bbc2949 / 第 1 页 / A2-C2，U7 AXP192 ACIN/BAT/DCDC1/LDO1/LDO3/SDA/SCK

### USB 5 V 到端口总线

USB_P050 经 D2 DSK34 直接馈入 BUS_P050，BUS_P050 为 Grove 与 USB-A 负载开关的输入电源。

- 参数与网络：`input=USB_P050`；`diode=D2 DSK34`；`output=BUS_P050`；`consumers=U9/U10/U11/U12/U13/U14 SGM2553`
- 证据：图 5b1d9bbc2949 / 第 1 页 / B1 D2 USB_P050→BUS_P050 与右侧负载开关输入

### 电池升压

U6 SCT12A0DHKR 由 SYS_BAT 供电，经 L2 1.5 µH 升压输出 BUS_P050，B5T_EN 通过 Q3/Q4 控制使能。

- 参数与网络：`reference=U6`；`part_number=SCT12A0DHKR`；`input=SYS_BAT`；`inductor=L2 1.5uH`；`output=BUS_P050`；`enable=B5T_EN via Q3/Q4`
- 证据：图 5b1d9bbc2949 / 第 1 页 / C2-D3，U6/L2/Q3/Q4/SYS_BAT/BUS_P050

### Grove 分路电源

Port A1/A2 共用 U9 开关供电，Port B1/B2/C1/C2 分别由 U11/U12/U13/U14 开关供电；PS0-PS4 控制各 SGM2553D EN。

- 参数与网络：`port_a_shared=U9 controlled by PS0, outputs SP1/SP2`；`port_b1=U11 PS1/SP3`；`port_b2=U12 PS2/SP4`；`port_c1=U13 PS3/SP5`；`port_c2=U14 PS4/SP6`
- 证据：图 5b1d9bbc2949 / 第 1 页 / A3-D4，U9/U11/U12/U13/U14 与 J4-J9

## 接口

### PWR485 外部接口

JE1 HT3.96-4P pins 4/3/2/1 依次为 RS_B、RS_A、VIN_12V、GND；JE2 提供同组内部信号。

- 参数与网络：`external=JE1 HT3.96_4P`；`pin4=RS_B`；`pin3=RS_A`；`pin2=VIN_12V`；`pin1=GND`；`internal=JE2 1.25MM_4P_立贴`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / A1-B1，JE1/JE2

### USB Type-C

J1 TYPEC 的 VCC 经 FU1 接 USB_P050，CC1/CC2 各通过 5.1 kΩ 接地，DP/DM 连接 SER_DP/SER_DM。

- 参数与网络：`reference=J1`；`power=USB_P050 via FU1 BSMD0805-110-6V`；`dp=SER_DP`；`dm=SER_DM`；`cc1=5.1K to GND`；`cc2=5.1K to GND`
- 证据：图 cc25a3bc6d25 / 第 1 页 / A1，J1 TYPEC/FU1/R1/R2

### TFT 显示接口

J2 FPC pins 6/5/4/8/3/1 分别为 GPIO18 SCK、GPIO23 MOSI、GPIO19 RS、GPIO5 CS、GPIO15 RESET、LCD_BL LEDA；VDD 为 MCU_VDD。

- 参数与网络：`reference=J2`；`sck=GPIO18`；`mosi=GPIO23`；`dc_rs=GPIO19`；`cs=GPIO5`；`reset=GPIO15`；`backlight=LCD_BL`；`vdd=MCU_VDD`
- 证据：图 cc25a3bc6d25 / 第 1 页 / C4-D4，J2 FPC_8P pin labels

### 六路 Grove GPIO

Port A1/A2 共用 GPIO33/GPIO32；B1 使用 GPIO35/GPIO25，B2 使用 GPIO36/GPIO26，C1 使用 GPIO13/GPIO14，C2 使用 GPIO16/GPIO17。

- 参数与网络：`A1=GPIO33/GPIO32`；`A2=GPIO33/GPIO32`；`B1=GPIO35/GPIO25`；`B2=GPIO36/GPIO26`；`C1=GPIO13/GPIO14`；`C2=GPIO16/GPIO17`
- 证据：图 5b1d9bbc2949 / 第 1 页 / J4-J9 IO2/IO1 网络

### USB-A 电源输出

J3 USB-A 的 VCC 连接 SN7，GND/SHIELD 接地，DM 与 DP 均未连接，因此原理图仅实现供电输出。

- 参数与网络：`reference=J3`；`vcc=SN7`；`dm=NC`；`dp=NC`；`ground=GND`；`shield=GND`
- 证据：图 5b1d9bbc2949 / 第 1 页 / D4，J3 USB-A pins VCC/DM/DP/GND/SHIELD

## 总线

### 系统 I2C

ESP32 GPIO22/SCL 与 GPIO21/SDA 连接 MPU-6886、AXP192、BM8563 和两颗 INA3221。

- 参数与网络：`controller=U3 ESP32-D0WDQ6`；`scl=GPIO22`；`sda=GPIO21`；`devices=U2 MPU-6886; U7 AXP192; U5 BM8563; U8/U16 INA3221`
- 证据：图 cc25a3bc6d25 / 第 1 页 / U3/U2 GPIO21/GPIO22 与 I2C 上拉; 图 5b1d9bbc2949 / 第 1 页 / U7/U5/U8/U16 SDA/SCK

### PWR485 通信

SP3485 的 RO 通过 D1 连接 GPIO3，DI 连接 GPIO1，RE/DE 共用 GPIO2；A/B 连接 RS_A/RS_B。

- 参数与网络：`transceiver=UE1 SP3485`；`rx=GPIO3 via DE1 1N4148WS`；`tx=GPIO1`；`direction=GPIO2`；`a=RS_A`；`b=RS_B`；`supply=MCU_VDD`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / A2，UE1 RO/RE/DE/DI/A/B 网络

## 总线地址

### INA3221 地址

U16 INA3221 原理图标注地址 0x40，U8 INA3221 标注地址 0x41。

- 参数与网络：`U16=0x40`；`U8=0x41`
- 证据：图 5b1d9bbc2949 / 第 1 页 / A3-A4，U16 0X40、U8 0X41

## GPIO 与控制信号

### 物理按键

S1/S2/S3 按下时分别将 GPIO37/GPIO38/GPIO39 拉低，三路各由 5.1 kΩ 上拉到 MCU_VDD；S4 将 PWR_KEY 拉低。

- 参数与网络：`S1=GPIO37`；`S2=GPIO38`；`S3=GPIO39`；`S4=PWR_KEY`；`active_level=low`
- 证据：图 cc25a3bc6d25 / 第 1 页 / C1，R3/R4/R5、S1/S2/S3/S4

### 七颗 RGB LED

GPIO4 驱动 LED1，LED1 至 LED7 以 DOUT→DIN 串联，全部由 MCU_VDD 供电。

- 参数与网络：`data_gpio=GPIO4`；`devices=LED1-LED7 SK6812_3535`；`count=7`；`supply=MCU_VDD`
- 证据：图 cc25a3bc6d25 / 第 1 页 / C1-D3，GPIO4 与 LED1-LED7 串联链

## 时钟

### ESP32 主时钟

X1 标注 X2520M4B40S，连接 ESP32 XTAL_P/XTAL_N，串联 R13 51 Ω。

- 参数与网络：`reference=X1`；`part_number=X2520M4B40S`；`nets=XTAL_P; XTAL_N`；`series_resistor=R13 51R/1%`
- 证据：图 cc25a3bc6d25 / 第 1 页 / B3-C4，X1/R13/XTAL_P/XTAL_N

### RTC 晶体

X2 为 BM8563 提供 32.768 kHz 时钟，C28/C29 均标注 6 pF。

- 参数与网络：`reference=X2`；`frequency=32.768K`；`capacitors=C28 6PF; C29 6PF`；`device=U5 BM8563`
- 证据：图 5b1d9bbc2949 / 第 1 页 / D1，X2 32.768K、C28/C29

## 保护电路

### RS-485 保护与偏置

RS_A/RS_B 侧配置多颗 PESD05CLP 类 TVS，RE7 5.1 kΩ 上拉 RS_A，RE3 5.1 kΩ 下拉 RS_B；RE1 22 kΩ 下拉方向控制。

- 参数与网络：`line_tvs=multiple PESD05CLP devices`；`a_bias=RE7 5.1K to MCU_VDD`；`b_bias=RE3 5.1K to GND`；`direction_pulldown=RE1 22K`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / UE1 右侧 RS_A/RS_B TVS 与 RE7/RE3，RE1

## 存储

### 外部 Flash

U4 W25Q128JVPIQ 通过 GPIO6/7/8/9/10/11 对应的 SPI 存储总线连接 ESP32。

- 参数与网络：`reference=U4`；`part_number=W25Q128JVPIQ`；`cs=GPIO11`；`clock=GPIO6`；`data=GPIO7; GPIO8; GPIO9; GPIO10`
- 证据：图 cc25a3bc6d25 / 第 1 页 / C3-D3，U4 W25Q128JVPIQ pins CS#/SCLK/SI/SO/WP#/HOLD#

## 传感器

### MPU-6886

U2 MPU-6886 由 MCU_VDD 供电，SCL/SDA 连接 GPIO22/GPIO21，INT 连接 GPIO27，AD0 接 MCU_VDD。

- 参数与网络：`reference=U2`；`part_number=MPU-6886`；`scl=GPIO22`；`sda=GPIO21`；`interrupt=GPIO27`；`ad0=MCU_VDD`
- 证据：图 cc25a3bc6d25 / 第 1 页 / C2-C3，U2 SCL/SDA/INT/AD0

### BM8563 RTC

U5 BM8563 由 RTC_VDD 供电，SDA/SCL 连接 GPIO21/GPIO22，INT 通过 P 沟道器件连接 PWR_KEY/AXP_PWR 唤醒链路。

- 参数与网络：`reference=U5`；`part_number=BM8563`；`supply=RTC_VDD`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=INT -> PMOS -> PWR_KEY/AXP_PWR`
- 证据：图 5b1d9bbc2949 / 第 1 页 / C1-D1，U5 BM8563 与 INT/PWR_KEY/AXP_PWR

## 射频

### 射频天线选择

ESP32 LNA_IN 经 L1/C12/C13 匹配网络后，R53 0 Ω 路径连接 ANT1 五金3D天线；通往 ANT2 KH-IPEX-K501-29 的 R12 标为 DNP。

- 参数与网络：`internal=ANT1 五金3D天线 via R53 0R`；`external=ANT2 KH-IPEX-K501-29 via R12 DNP`；`matching=L1 2.2nH; C12 2.4pF; C13 2.0pF`
- 证据：图 cc25a3bc6d25 / 第 1 页 / A3-A4，L1/C12/C13/R53/R12/ANT1/ANT2

## 调试与烧录

### USB-UART 下载

U1 CH9102F 将 SER_DP/DM 转换为 GPIO1 TX 与 GPIO3 RX，DTR/RTS 经双晶体管电路控制 MCU_RST 与 GPIO0。

- 参数与网络：`reference=U1`；`part_number=CH9102F`；`usb=SER_DP; SER_DM`；`uart_tx_to_esp=GPIO3`；`uart_rx_from_esp=GPIO1`；`auto_program=DTR/RTS -> MCU_RST/GPIO0`
- 证据：图 cc25a3bc6d25 / 第 1 页 / A2-B3，U1 CH9102F、D3、Q1/Q2、DTR/RTS

## 模拟电路

### Grove 电压电流监测

U16 INA3221 0x40 监测 SN1/SN2/SN3，U8 INA3221 0x41 监测 SN4/SN5/SN6，各通道使用 R1206 0.01 Ω/1%/1W 分流电阻。

- 参数与网络：`U16_0x40=SN1; SN2; SN3`；`U8_0x41=SN4; SN5; SN6`；`shunts=R39-R43 and associated R1206 0.01R/1%/1W`
- 证据：图 5b1d9bbc2949 / 第 1 页 / A3-D4，U16/U8 与 SN1-SN6 分流网络

### USB-A 电流采样

U10 SGM2553D 受 GPIO12 控制并经 SP7/SN7 向 USB-A 供电，U15 INA199A1DCKR 跨分流电阻采样并输出 MCU_VDD 域信号。

- 参数与网络：`switch=U10 SGM2553DYTD16G/TR`；`enable=GPIO12`；`shunt_nets=SP7; SN7`；`amplifier=U15 INA199A1DCKR`；`load=J3 USB-A`
- 证据：图 5b1d9bbc2949 / 第 1 页 / D3-D4，U10/U15/SP7/SN7/J3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统架构 | `controller=U3 ESP32-D0WDQ6`；`flash=U4 W25Q128JVPIQ`；`usb_uart=U1 CH9102F`；`imu=U2 MPU-6886`；`rtc=U5 BM8563`；`pmic=U7 AXP192`；`boost=U6 SCT12A0DHKR`；`rs485=UE1 SP3485` |
| 总线 | 系统 I2C | `controller=U3 ESP32-D0WDQ6`；`scl=GPIO22`；`sda=GPIO21`；`devices=U2 MPU-6886; U7 AXP192; U5 BM8563; U8/U16 INA3221` |
| 总线地址 | INA3221 地址 | `U16=0x40`；`U8=0x41` |
| 总线 | PWR485 通信 | `transceiver=UE1 SP3485`；`rx=GPIO3 via DE1 1N4148WS`；`tx=GPIO1`；`direction=GPIO2`；`a=RS_A`；`b=RS_B`；`supply=MCU_VDD` |
| 接口 | PWR485 外部接口 | `external=JE1 HT3.96_4P`；`pin4=RS_B`；`pin3=RS_A`；`pin2=VIN_12V`；`pin1=GND`；`internal=JE2 1.25MM_4P_立贴` |
| 保护电路 | RS-485 保护与偏置 | `line_tvs=multiple PESD05CLP devices`；`a_bias=RE7 5.1K to MCU_VDD`；`b_bias=RE3 5.1K to GND`；`direction_pulldown=RE1 22K` |
| 电源 | PWR485 降压 | `input=VIN_12V`；`input_fuse=FE1 BSMD0805-050-24V`；`converter=UE2 SY8303`；`inductor=L4 10UH`；`output_fuse=FE2 BSMD0805-110-6V`；`output=USB_P050` |
| 接口 | USB Type-C | `reference=J1`；`power=USB_P050 via FU1 BSMD0805-110-6V`；`dp=SER_DP`；`dm=SER_DM`；`cc1=5.1K to GND`；`cc2=5.1K to GND` |
| 调试与烧录 | USB-UART 下载 | `reference=U1`；`part_number=CH9102F`；`usb=SER_DP; SER_DM`；`uart_tx_to_esp=GPIO3`；`uart_rx_from_esp=GPIO1`；`auto_program=DTR/RTS -> MCU_RST/GPIO0` |
| 存储 | 外部 Flash | `reference=U4`；`part_number=W25Q128JVPIQ`；`cs=GPIO11`；`clock=GPIO6`；`data=GPIO7; GPIO8; GPIO9; GPIO10` |
| 传感器 | MPU-6886 | `reference=U2`；`part_number=MPU-6886`；`scl=GPIO22`；`sda=GPIO21`；`interrupt=GPIO27`；`ad0=MCU_VDD` |
| GPIO 与控制信号 | 物理按键 | `S1=GPIO37`；`S2=GPIO38`；`S3=GPIO39`；`S4=PWR_KEY`；`active_level=low` |
| GPIO 与控制信号 | 七颗 RGB LED | `data_gpio=GPIO4`；`devices=LED1-LED7 SK6812_3535`；`count=7`；`supply=MCU_VDD` |
| 接口 | TFT 显示接口 | `reference=J2`；`sck=GPIO18`；`mosi=GPIO23`；`dc_rs=GPIO19`；`cs=GPIO5`；`reset=GPIO15`；`backlight=LCD_BL`；`vdd=MCU_VDD` |
| 射频 | 射频天线选择 | `internal=ANT1 五金3D天线 via R53 0R`；`external=ANT2 KH-IPEX-K501-29 via R12 DNP`；`matching=L1 2.2nH; C12 2.4pF; C13 2.0pF` |
| 时钟 | ESP32 主时钟 | `reference=X1`；`part_number=X2520M4B40S`；`nets=XTAL_P; XTAL_N`；`series_resistor=R13 51R/1%` |
| 电源 | AXP192 电源管理 | `reference=U7`；`part_number=AXP192`；`usb_input=USB_P050`；`battery=SYS_BAT`；`dcdc1=MCU_VDD via L3`；`ldo1=RTC_VDD`；`ldo3=LCD_BL via R26 4.7R`；`sda=GPIO21`；`scl=GPIO22` |
| 电源 | USB 5 V 到端口总线 | `input=USB_P050`；`diode=D2 DSK34`；`output=BUS_P050`；`consumers=U9/U10/U11/U12/U13/U14 SGM2553` |
| 电源 | 电池升压 | `reference=U6`；`part_number=SCT12A0DHKR`；`input=SYS_BAT`；`inductor=L2 1.5uH`；`output=BUS_P050`；`enable=B5T_EN via Q3/Q4` |
| 电源 | Grove 分路电源 | `port_a_shared=U9 controlled by PS0, outputs SP1/SP2`；`port_b1=U11 PS1/SP3`；`port_b2=U12 PS2/SP4`；`port_c1=U13 PS3/SP5`；`port_c2=U14 PS4/SP6` |
| 接口 | 六路 Grove GPIO | `A1=GPIO33/GPIO32`；`A2=GPIO33/GPIO32`；`B1=GPIO35/GPIO25`；`B2=GPIO36/GPIO26`；`C1=GPIO13/GPIO14`；`C2=GPIO16/GPIO17` |
| 模拟电路 | Grove 电压电流监测 | `U16_0x40=SN1; SN2; SN3`；`U8_0x41=SN4; SN5; SN6`；`shunts=R39-R43 and associated R1206 0.01R/1%/1W` |
| 接口 | USB-A 电源输出 | `reference=J3`；`vcc=SN7`；`dm=NC`；`dp=NC`；`ground=GND`；`shield=GND` |
| 模拟电路 | USB-A 电流采样 | `switch=U10 SGM2553DYTD16G/TR`；`enable=GPIO12`；`shunt_nets=SP7; SN7`；`amplifier=U15 INA199A1DCKR`；`load=J3 USB-A` |
| 传感器 | BM8563 RTC | `reference=U5`；`part_number=BM8563`；`supply=RTC_VDD`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=INT -> PMOS -> PWR_KEY/AXP_PWR` |
| 时钟 | RTC 晶体 | `reference=X2`；`frequency=32.768K`；`capacitors=C28 6PF; C29 6PF`；`device=U5 BM8563` |
| 核心器件 | ESP32 芯片版本 | `reference=U3`；`schematic_model=ESP32-D0WDQ6`；`document_model=ESP32-D0WDQ6-V3` |
| 存储 | Flash 容量 | `reference=U4`；`part_number=W25Q128JVPIQ`；`claimed_capacity=16MB` |
| 接口 | TFT 型号与显示规格 | `confirmed_connector=J2 FPC_8P后翻`；`unverified_claims=ST7789V2; 1.14 inch; 240x135 IPS` |
| 总线地址 | AXP192/BM8563/MPU-6886 地址 | `devices=U7 AXP192; U5 BM8563; U2 MPU-6886`；`addresses=not printed` |
| 电源 | PWR485 输入额定范围 | `net=VIN_12V`；`converter=UE2 SY8303`；`unverified_rating=9-24V@1A` |
| 电源 | 内部电池规格 | `connector=JE3 1.25MM_4P_立贴`；`net=SYS_BAT`；`manager=U7 AXP192`；`capacity=not printed` |

## 待确认事项

- `component.soc-version`：原理图 U3 标注 ESP32-D0WDQ6，产品正文标注 ESP32-D0WDQ6-V3；是否为 V3 修订需由 BOM 复核。（证据：图 cc25a3bc6d25 / 第 1 页 / U3 顶部型号 ESP32-D0WDQ6）
- `storage.flash-capacity`：原理图确认 U4 型号 W25Q128JVPIQ，但未直接以容量字段写出 16 MB。（证据：图 cc25a3bc6d25 / 第 1 页 / U4 仅标 W25Q128JVPIQ）
- `interface.display-spec`：原理图只显示 J2 FPC 与 SPI/控制信号，未直接标注 ST7789V2、1.14 英寸或 240×135。（证据：图 cc25a3bc6d25 / 第 1 页 / J2 只列 SCK/MOSI/RS/CS/RESET/LEDA/VDD）
- `address.axp-rtc-imu`：AXP192、BM8563 与 MPU-6886 连接系统 I2C，但原理图未直接印出其 7-bit 地址。（证据：图 cc25a3bc6d25 / 第 1 页 / U2 MPU-6886 I2C，无地址文本; 图 5b1d9bbc2949 / 第 1 页 / U7/U5 I2C，无地址文本）
- `power.pwr485-rating`：原理图使用 VIN_12V 网络名并给出 SY8303 电路，但未直接列出产品正文所述 9–24 V@1 A 输入范围。（证据：图 9abe5c6bdfb6 / 第 1 页 / JE1/JE2 VIN_12V 与 UE2，未印输入范围）
- `power.battery-spec`：原理图确认 JE3 SYS_BAT 电池接口及 AXP192 充电/供电路径，但未标注电池化学体系、标称电压或容量。（证据：图 5b1d9bbc2949 / 第 1 页 / A1-A2，JE3/SYS_BAT/U7 BAT pins）
- `review.soc-version`：Station-485 K123 实际装配是否为 ESP32-D0WDQ6-V3？；原因：原理图型号未带 -V3，正文带 -V3。
- `review.flash-capacity`：请用 W25Q128JVPIQ datasheet/BOM 确认 16 MB Flash。；原因：原理图只给出器件型号。
- `review.display-spec`：请用 LCD FPC/BOM 确认 ST7789V2、1.14 英寸和 240×135 IPS。；原因：原理图只提供连接器与信号。
- `review.i2c-addresses`：请用 AXP192、BM8563、MPU-6886 datasheet 复核 7-bit I2C 地址。；原因：这些地址未印在原理图中。
- `review.pwr485-rating`：请用 SY8303 电源设计/BOM 复核 9–24 V@1 A PWR485 输入额定值。；原因：原理图只标 VIN_12V 网络名。
- `review.battery-spec`：请用电池/BOM 确认 JE3 适配电池的电压、化学体系和容量。；原因：原理图仅显示 SYS_BAT 电气路径。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9abe5c6bdfb6898cc836353d20cf9f6283c3f27c2e0068ce6d19f3823210a743` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_01.png` |
| 2 | 1 | `cc25a3bc6d25ed4e4f29d4a1ef657523923c972e5e4182afa3076152ab6f365e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_02.png` |
| 3 | 1 | `5b1d9bbc2949194dc3d09127d66ad87203165cf372825fffdf48129ebd0d46fc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_03.png` |

---

源文档：`zh_CN/core/station_485.md`

源文档 SHA-256：`ad65a054b6b06342501d1cc86f2b7a58ebcd4c728265adfdd14f6a7f6958778e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
