# Station-Bat 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Station-Bat |
| SKU | K124-B |
| 产品 ID | `station-bat-19af8aaec9ac` |
| 源文档 | `zh_CN/core/station_bat.md` |

## 概述

Station-Bat 以 U3 ESP32-D0WDQ6 为主控，外接 W25Q128JVPIQ Flash、CH9102F、MPU-6886、BM8563、SPI LCD、7 颗 SK6812 与三枚按键。AXP192 管理 USB/双电池输入和 MCU/RTC/LCD 电源，SCT12A0DHKR 从 SYS_BAT 生成 BUS_P050；六颗 SGM2553D 分配六路 Grove/USB-A 电源，两颗 INA3221 以 0x40/0x41 监测 Grove，INA199 监测 USB-A。资源第 1 页还包含 VIN_12V、SY8303 与 RS-485 收发电路，但其在 Station-Bat K124-B 上的装配适用性需确认。

## 检索关键词

`Station-Bat`、`K124-B`、`Sch_M5Station_v1.3`、`ESP32-D0WDQ6`、`W25Q128JVPIQ`、`CH9102F`、`MPU-6886`、`AXP192`、`BM8563`、`SCT12A0DHKR`、`INA3221`、`0x40`、`0x41`、`INA199A1DCKR`、`SGM2553D`、`SY8303`、`RS-485`、`SP3485`、`BUS_P050`、`SYS_BAT`、`USB_P050`、`MCU_VDD`、`AXP_IPS`、`RTC_VDD`、`LCD_BL`、`PS0`、`PS1`、`PS2`、`PS3`、`PS4`、`PORT A1`、`PORT A2`、`PORT B1`、`PORT B2`、`PORT C1`、`PORT C2`、`USB-A output`、`SK6812_3535`、`RTC_INT`、`PWR_KEY`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-D0WDQ6 | 系统主控，连接 Flash、USB-UART、I2C、LCD、LED、按键和扩展接口 | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 A3-C4，U3 ESP32-D0WDQ6 |
| U4 | W25Q128JVPIQ | ESP32 外部 SPI Flash | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 C3-D3，U4 W25Q128JVPIQ |
| U1 | CH9102F | USB-UART 下载桥与自动下载控制源 | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 A2-B2，U1 CH9102F |
| U2 | MPU-6886 | I2C 六轴 IMU，INT 接 GPIO27 | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 C2，U2 MPU-6886 |
| U7 | AXP192 | PMU，管理 USB/电池、充电、DCDC/LDO、五路电源开关控制与电源键 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 A2-C2，U7 AXP192 |
| U6 | SCT12A0DHKR | SYS_BAT 至 BUS_P050 的高功率升压转换器 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 C2-D2，U6 SCT12A0DHKR |
| U5 | BM8563 | 电池备份 RTC，通过 GPIO21/22 I2C 连接并输出 RTC_INT | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 C1-D1，U5 BM8563 |
| U8/U16 | INA3221 | 六路 Grove 电压/电流监测，地址分别标为 0x41 与 0x40 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 A3-A4，U8 0x41、U16 0x40 |
| U9-U14 | SGM2553D/YD16G/TR | 六路受控 5V 负载开关，分别生成 SP1-SP7 端口电源 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 A3-D3，U9/U11/U12/U13/U14/U10 |
| U15 | INA199A1DCKR | USB-A 供电输出电流检测放大器 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 D3，U15 INA199A1DCKR |
| J3 | USB-A | 仅供电输出 USB Type-A 接口，VCC 经 SGM2553D/INA199，数据脚未连接 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 D4，J3 USB-A |
| J4-J9 | GROVE | 六路 Grove 接口 PORT A1/A2/B1/B2/C1/C2 | 图 5b1d9bbc2949 / 第 1 页 / 第3资源 A4-D4，J4-J9 GROVE |
| LED1-LED7 | SK6812_3535 | GPIO4 串行控制的 7 颗 RGB LED | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 C1-D3，LED1-LED7 SK6812_3535 |
| J2 | FPC_8P | LCD FPC，承载 SPI/控制、背光、逻辑电源和 GND | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 C4-D4，J2 LCD FPC |
| J1 | TYPEC | USB Type-C 系统供电和 CH9102F 数据接口 | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 A1-B1，J1 TYPEC |
| S1-S4 | SW | GPIO37/38/39 三个用户按键与 PWR_KEY 电源键 | 图 cc25a3bc6d25 / 第 1 页 / 第2资源 C1，S1-S4 |
| UE1 | 未标注 | RS-485 收发器，RO/DI/RE/DE 接 GPIO3/GPIO1/GPIO2，A/B 接 RS_A/RS_B | 图 9abe5c6bdfb6 / 第 1 页 / 第1资源 A2-B2，UE1 RS-485 收发器 |
| UE2 | SY8303 | VIN_12V 至 USB_P050 的降压转换器 | 图 9abe5c6bdfb6 / 第 1 页 / 第1资源 B2-C2，UE2 SY8303 |
| JE1/JE2 | HT3.96_4P/1.25MM_4P | PWR485 VIN_12V、RS_A、RS_B 与 GND 连接器 | 图 9abe5c6bdfb6 / 第 1 页 / 第1资源 A1-B1，JE1/JE2 |

## 系统结构

### Station-Bat v1.3 架构

ESP32-D0WDQ6 连接 W25Q128 Flash、CH9102F、MPU-6886、LCD、RTC、AXP192、7 颗 RGB LED 与按键；AXP192/SCT12A0DHKR 供电，INA3221/INA199 监测六路 Grove 和 USB-A。

- 参数与网络：`mcu=U3 ESP32-D0WDQ6`；`flash=U4 W25Q128JVPIQ`；`pmu=U7 AXP192`；`boost=U6 SCT12A0DHKR`；`monitors=U8/U16 INA3221; U15 INA199`；`revision=v1.3`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源完整页; 图 5b1d9bbc2949 / 第 1 页 / 第3资源完整页

## 核心器件

### U3 ESP32-D0WDQ6

U3 明确标 ESP32-D0WDQ6，GPIO0-39、UART0、I2C、Flash SPI、LCD 与 RF 网络均在页内连接。

- 参数与网络：`reference=U3`；`part_number=ESP32-D0WDQ6`；`power=MCU_VDD`；`reset=MCU_RST`；`uart=GPIO1/GPIO3`；`i2c=GPIO21/GPIO22`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U3

### U5 BM8563

U5 SDA/SCL 接 GPIO21/22，VDD 接 RTC_VDD，INT 输出 RTC_INT，X2 为 32.768K。

- 参数与网络：`reference=U5`；`part_number=BM8563`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=RTC_INT`；`crystal=X2 32.768K`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 C1-D1 U5

## 电源

### 双电池并联输入

第3页画出两组电池支路并联至 SYS_BAT，每支路含 FUSE 与 SD0603S020 保护器件；另有 JE3M 4 针电池连接器。

- 参数与网络：`battery_net=SYS_BAT`；`branches=2`；`fuses=FUSE1/FUSE2`；`protection=SD0603S020 per branch`；`connector=JE3M 1.25MM_4P`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A1 电池区

### U7 AXP192

AXP192 ACIN/VBUS 接 USB_P050、BAT 接 SYS_BAT，DCDC1 经 L3 输出 MCU_VDD，LDO1 输出 RTC_VDD，LDO3 经 R26 输出 LCD_BL，GPIO0-4 输出 PS0-PS4 控制负载开关。

- 参数与网络：`input=USB_P050`；`battery=SYS_BAT`；`dcdc1=MCU_VDD`；`ldo1=RTC_VDD`；`ldo3=LCD_BL`；`gpio_controls=PS0-PS4`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A2-C2 U7 AXP192

### U6 SCT12A0DHKR

U6 以 SYS_BAT 为输入，Q3/Q4 与 BST_EN 控制启停，输出 BUS_P050；反馈为 R23 47K/R24 15K。

- 参数与网络：`reference=U6`；`input=SYS_BAT`；`output=BUS_P050`；`enable=BST_EN via Q3/Q4`；`feedback=R23 47K; R24 15K`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 C2-D2 U6

### USB 与电池 5V 合路

USB_P050 经 D2 DSK34 直接汇入 BUS_P050，电池路径由 SCT12A0DHKR 生成同一 BUS_P050。

- 参数与网络：`usb_path=USB_P050 -> D2 DSK34 -> BUS_P050`；`battery_path=SYS_BAT -> U6 -> BUS_P050`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 B1 D2 与 U6

### 六路 SGM2553D

U9/U11/U12/U13/U14/U10 以 BUS_P050 为输入，由 AXP192 PS0-PS4 控制，输出经 0.01Ω 分流电阻形成 SP1-SP7。

- 参数与网络：`devices=U9,U10,U11,U12,U13,U14`；`part_number=SGM2553D/YD16G/TR`；`input=BUS_P050`；`controls=PS0-PS4`；`outputs=SP1-SP7`；`shunts=R1206 0.01R 1% 1W`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A3-D3 负载开关

## 接口

### J1 USB Type-C

J1 VCC 经 FU1 接 USB_P050，A6/B6 与 A7/B7 汇入 SER_DP/SER_DM，CC1/CC2 以 R1/R2 5.1K 下拉。

- 参数与网络：`power=USB_P050 via FU1`；`dp=A6/B6 SER_DP`；`dm=A7/B7 SER_DM`；`cc=R1/R2 5.1K`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 A1 J1

### 六路 Grove

J4/J5 PORT A1/A2 共用 GPIO33/GPIO32；J6 B1 为 GPIO35/GPIO25，J7 B2 为 GPIO36/GPIO26，J8 C1 为 GPIO13/GPIO14，J9 C2 为 GPIO16/GPIO17；各口另有独立/共享 5V 与 GND。

- 参数与网络：`A1=GPIO33/GPIO32`；`A2=GPIO33/GPIO32`；`B1=GPIO35/GPIO25`；`B2=GPIO36/GPIO26`；`C1=GPIO13/GPIO14`；`C2=GPIO16/GPIO17`；`power=SP1-SP6`；`ground=GND`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A4-D4 J4-J9

### J3 USB-A 供电输出

J3 VCC 由 U10 SGM2553D 经 SN7 分流供电，DM/DP 未连接，GND/SHELL 接地。

- 参数与网络：`reference=J3`；`power=SP7/SN7`；`data_minus=null`；`data_plus=null`；`ground=GND`；`direction=power output only`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 D4 J3 USB-A

## 总线

### 内部 I2C

GPIO21/22 作为 SDA/SCL，R10/R11 各 2.2K 上拉至 MCU_VDD；总线连接 MPU-6886、AXP192、BM8563 与两颗 INA3221。

- 参数与网络：`controller=U3 ESP32`；`sda=GPIO21`；`scl=GPIO22`；`pullups=R10/R11 2.2K`；`devices=MPU-6886; AXP192; BM8563; INA3221 x2`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U2/U3/R10/R11; 图 5b1d9bbc2949 / 第 1 页 / 第3资源 U5/U7/U8/U16

### LCD SPI

J2 LCD SCK/MOSI/RS/CS/RESET 分别接 GPIO18/GPIO23/GPIO19/GPIO5/GPIO15，LEDA 接 LCD_BL，VDD 接 MCU_VDD。

- 参数与网络：`sck=GPIO18`；`mosi=GPIO23`；`dc=GPIO19`；`cs=GPIO5`；`reset=GPIO15`；`backlight=LCD_BL`；`power=MCU_VDD`；`miso=null`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 C4-D4 J2 LCD

## 总线地址

### INA3221 地址

第3页直接标注 U8 INA3221 为 0x41、U16 INA3221 为 0x40。

- 参数与网络：`U8=0x41`；`U16=0x40`；`bus=GPIO21/GPIO22 I2C`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A3-A4 U8 0x41/U16 0x40

### 其他内部 I2C 地址

原理图未直接标注 MPU-6886、AXP192 或 BM8563 的数值 I2C 地址。

- 参数与网络：`devices=MPU-6886; AXP192; BM8563`；`addresses_visible=false`；`addresses=null`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U2，未标地址; 图 5b1d9bbc2949 / 第 1 页 / 第3资源 U5/U7，未标地址

## GPIO 与控制信号

### 四个按键

S1/S2/S3 分别连接 GPIO37/GPIO38/GPIO39 并经 5.1K 上拉，S4 连接 PWR_KEY；按下均接地。

- 参数与网络：`button_a=GPIO37`；`button_b=GPIO38`；`button_c=GPIO39`；`power=PWR_KEY`；`pullups=R3/R4/R5 5.1K`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 C1 S1-S4

### 7 颗 SK6812

GPIO4 驱动 LED1 DI，LED1-LED7 以 DO/DI 串联，全部由 MCU_VDD 供电。

- 参数与网络：`source=GPIO4`；`devices=LED1-LED7 SK6812_3535`；`count=7`；`topology=serial daisy chain`；`power=MCU_VDD`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 C1-D3 LED1-LED7

## 时钟

### RTC 晶振

BM8563 OSCI/OSCO 连接 X2 32.768K，C28/C29 各 6pF 接地。

- 参数与网络：`frequency=32.768K`；`crystal=X2`；`capacitors=C28/C29 6pF`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 U5/X2

## 保护电路

### RS-485 保护

RS_A/RS_B 各有 P6SMB6.8CA/TVS05CA 保护，R7/R8 10K 偏置，R5 120Ω 终端，R6 2.2K 下拉使能。

- 参数与网络：`tvs=P6SMB6.8CA/TVS05CA arrays`；`termination=R5 120Ω`；`bias=R7/R8 10K`；`enable_pulldown=R6 2.2K`
- 证据：图 9abe5c6bdfb6 / 第 1 页 / 第1资源 UE1 RS_A/RS_B 保护网络

### 电池与 USB 保护

两条 SYS_BAT 支路各有保险丝与 SD0603S020，USB Type-C VCC 经过 FU1 BSMDO805-110-6V，自 USB_P050 至 BUS_P050 有 D2 DSK34 隔离。

- 参数与网络：`battery_fuses=FUSE1/FUSE2`；`battery_protection=SD0603S020`；`usb_fuse=FU1 BSMDO805-110-6V`；`oring_diode=D2 DSK34`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 J1/FU1; 图 5b1d9bbc2949 / 第 1 页 / 第3资源 A1/B1 电池/USB 保护

## 关键网络

### RTC 电源唤醒

RTC_INT 经 R15 10K 与 PWR_KEY 网络关联，PWR_KEY 连接 AXP192 PWRON。

- 参数与网络：`source=RTC_INT`；`resistor=R15 10K`；`destination=PWR_KEY`；`pmu=AXP192 PWRON`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 C1-D1 RTC/PWR_KEY 与 U7 PWRON

## 存储

### U4 W25Q128JVPIQ

U4 以 MCU_VDD 供电，CS#/SCLK/SI/SO/WP#/HOLD# 接 GPIO11/GPIO6/GPIO8/GPIO7/GPIO10/GPIO9。

- 参数与网络：`reference=U4`；`part_number=W25Q128JVPIQ`；`cs=GPIO11N`；`sclk=GPIO6N`；`mosi=GPIO8N`；`miso=GPIO7N`；`wp=GPIO10N`；`hold=GPIO9N`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U4

## 传感器

### U2 MPU-6886

U2 由 MCU_VDD 供电，SDA/SCL 接 GPIO21/GPIO22，INT 接 GPIO27。

- 参数与网络：`reference=U2`；`part_number=MPU-6886`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO27`；`power=MCU_VDD`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 C2 U2

## 射频

### ESP32 天线

ESP32 LNA_IN 经 L1 2.2nH 与 C12/C13 2.4pF/2.0pF 连接 ANT1 五金3D天线；R12 DNP/R53 0R 可选连接 ANT2 IPEX。

- 参数与网络：`source=LNA_IN`；`inductor=L1 2.2nH`；`capacitors=C12 2.4pF; C13 2.0pF`；`onboard=ANT1`；`external=ANT2 IPEX via R12 DNP/R53 0R`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 A3 RF 区

## 调试与烧录

### CH9102F USB-UART

J1 SER_DP/SER_DM 接 U1 CH9102F，TXD/RXD 分别连接 GPIO3/GPIO1，DTR/RTS 经 Q5/Q6 与 D3 控制 GPIO0/MCU_RST。

- 参数与网络：`bridge=U1 CH9102F`；`usb=SER_DP/SER_DM`；`tx=CH9102 TXD -> GPIO3/U0RXD`；`rx=CH9102 RXD <- GPIO1/U0TXD`；`boot=GPIO0`；`reset=MCU_RST`
- 证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 A1-B3 CH9102F/USB/自动下载

## 模拟电路

### Grove 电压/电流监测

U8/U16 两颗 INA3221 通过 SN1-SN6/SP1-SP6 监测六路 Grove 的 0.01Ω 分流电阻，SDA/SCL 接 GPIO21/22。

- 参数与网络：`monitors=U8 0x41; U16 0x40`；`channels=SN1-SN6/SP1-SP6`；`shunt=0.01Ω 1% 1W`；`bus=GPIO21/22 I2C`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 A3-A4 INA3221 与各端口分流

### USB-A 电流检测

U15 INA199A1DCKR 跨接 USB-A SN7 分流网络，OUT 标 MCU_VDD 并连接采样/参考电阻网络。

- 参数与网络：`reference=U15`；`part_number=INA199A1DCKR`；`channel=SN7`；`port=J3 USB-A`；`supply=MCU_VDD`
- 证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源 D3-D4 U15/J3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Station-Bat v1.3 架构 | `mcu=U3 ESP32-D0WDQ6`；`flash=U4 W25Q128JVPIQ`；`pmu=U7 AXP192`；`boost=U6 SCT12A0DHKR`；`monitors=U8/U16 INA3221; U15 INA199`；`revision=v1.3` |
| 核心器件 | U3 ESP32-D0WDQ6 | `reference=U3`；`part_number=ESP32-D0WDQ6`；`power=MCU_VDD`；`reset=MCU_RST`；`uart=GPIO1/GPIO3`；`i2c=GPIO21/GPIO22` |
| 核心器件 | ESP32 精确版本 | `documented_model=ESP32-D0WDQ6-V3`；`schematic_model=ESP32-D0WDQ6` |
| 存储 | U4 W25Q128JVPIQ | `reference=U4`；`part_number=W25Q128JVPIQ`；`cs=GPIO11N`；`sclk=GPIO6N`；`mosi=GPIO8N`；`miso=GPIO7N`；`wp=GPIO10N`；`hold=GPIO9N` |
| 内存与 Flash | Flash 容量 | `documented_capacity=16MB`；`schematic_part=W25Q128JVPIQ`；`byte_capacity_visible=false` |
| 调试与烧录 | CH9102F USB-UART | `bridge=U1 CH9102F`；`usb=SER_DP/SER_DM`；`tx=CH9102 TXD -> GPIO3/U0RXD`；`rx=CH9102 RXD <- GPIO1/U0TXD`；`boot=GPIO0`；`reset=MCU_RST` |
| 接口 | J1 USB Type-C | `power=USB_P050 via FU1`；`dp=A6/B6 SER_DP`；`dm=A7/B7 SER_DM`；`cc=R1/R2 5.1K` |
| 传感器 | U2 MPU-6886 | `reference=U2`；`part_number=MPU-6886`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=GPIO27`；`power=MCU_VDD` |
| 总线 | 内部 I2C | `controller=U3 ESP32`；`sda=GPIO21`；`scl=GPIO22`；`pullups=R10/R11 2.2K`；`devices=MPU-6886; AXP192; BM8563; INA3221 x2` |
| 总线地址 | INA3221 地址 | `U8=0x41`；`U16=0x40`；`bus=GPIO21/GPIO22 I2C` |
| 总线地址 | 其他内部 I2C 地址 | `devices=MPU-6886; AXP192; BM8563`；`addresses_visible=false`；`addresses=null` |
| GPIO 与控制信号 | 四个按键 | `button_a=GPIO37`；`button_b=GPIO38`；`button_c=GPIO39`；`power=PWR_KEY`；`pullups=R3/R4/R5 5.1K` |
| GPIO 与控制信号 | 7 颗 SK6812 | `source=GPIO4`；`devices=LED1-LED7 SK6812_3535`；`count=7`；`topology=serial daisy chain`；`power=MCU_VDD` |
| 总线 | LCD SPI | `sck=GPIO18`；`mosi=GPIO23`；`dc=GPIO19`；`cs=GPIO5`；`reset=GPIO15`；`backlight=LCD_BL`；`power=MCU_VDD`；`miso=null` |
| 核心器件 | LCD 型号与规格 | `documented_driver=ST7789V2`；`documented_size=1.14 inch`；`documented_resolution=240x135`；`schematic_connector=J2 FPC_8P` |
| 电源 | 双电池并联输入 | `battery_net=SYS_BAT`；`branches=2`；`fuses=FUSE1/FUSE2`；`protection=SD0603S020 per branch`；`connector=JE3M 1.25MM_4P` |
| 电源 | 18650 电池容量 | `documented_cells=18650 x2 parallel`；`documented_capacity=2200mAh`；`schematic_branches=2`；`capacity_visible=false` |
| 电源 | U7 AXP192 | `input=USB_P050`；`battery=SYS_BAT`；`dcdc1=MCU_VDD`；`ldo1=RTC_VDD`；`ldo3=LCD_BL`；`gpio_controls=PS0-PS4` |
| 电源 | U6 SCT12A0DHKR | `reference=U6`；`input=SYS_BAT`；`output=BUS_P050`；`enable=BST_EN via Q3/Q4`；`feedback=R23 47K; R24 15K` |
| 电源 | USB 与电池 5V 合路 | `usb_path=USB_P050 -> D2 DSK34 -> BUS_P050`；`battery_path=SYS_BAT -> U6 -> BUS_P050` |
| 电源 | 六路 SGM2553D | `devices=U9,U10,U11,U12,U13,U14`；`part_number=SGM2553D/YD16G/TR`；`input=BUS_P050`；`controls=PS0-PS4`；`outputs=SP1-SP7`；`shunts=R1206 0.01R 1% 1W` |
| 模拟电路 | Grove 电压/电流监测 | `monitors=U8 0x41; U16 0x40`；`channels=SN1-SN6/SP1-SP6`；`shunt=0.01Ω 1% 1W`；`bus=GPIO21/22 I2C` |
| 模拟电路 | USB-A 电流检测 | `reference=U15`；`part_number=INA199A1DCKR`；`channel=SN7`；`port=J3 USB-A`；`supply=MCU_VDD` |
| 接口 | 六路 Grove | `A1=GPIO33/GPIO32`；`A2=GPIO33/GPIO32`；`B1=GPIO35/GPIO25`；`B2=GPIO36/GPIO26`；`C1=GPIO13/GPIO14`；`C2=GPIO16/GPIO17`；`power=SP1-SP6`；`ground=GND` |
| 接口 | J3 USB-A 供电输出 | `reference=J3`；`power=SP7/SN7`；`data_minus=null`；`data_plus=null`；`ground=GND`；`direction=power output only` |
| 核心器件 | U5 BM8563 | `reference=U5`；`part_number=BM8563`；`sda=GPIO21`；`scl=GPIO22`；`interrupt=RTC_INT`；`crystal=X2 32.768K` |
| 时钟 | RTC 晶振 | `frequency=32.768K`；`crystal=X2`；`capacitors=C28/C29 6pF` |
| 关键网络 | RTC 电源唤醒 | `source=RTC_INT`；`resistor=R15 10K`；`destination=PWR_KEY`；`pmu=AXP192 PWRON` |
| 总线 | PWR485 RS-485 | `receiver_out=GPIO3`；`driver_in=GPIO1`；`direction_enable=GPIO2`；`differential=RS_A/RS_B`；`power=VIN_12V`；`connectors=JE1/JE2`；`station_bat_population=null` |
| 电源 | PWR485 12V 降压 | `reference=UE2`；`part_number=SY8303`；`input=VIN_12V`；`output=USB_P050`；`inductor=L4 10uH`；`station_bat_population=null` |
| 保护电路 | RS-485 保护 | `tvs=P6SMB6.8CA/TVS05CA arrays`；`termination=R5 120Ω`；`bias=R7/R8 10K`；`enable_pulldown=R6 2.2K` |
| 保护电路 | 电池与 USB 保护 | `battery_fuses=FUSE1/FUSE2`；`battery_protection=SD0603S020`；`usb_fuse=FU1 BSMDO805-110-6V`；`oring_diode=D2 DSK34` |
| 射频 | ESP32 天线 | `source=LNA_IN`；`inductor=L1 2.2nH`；`capacitors=C12 2.4pF; C13 2.0pF`；`onboard=ANT1`；`external=ANT2 IPEX via R12 DNP/R53 0R` |

## 待确认事项

- `component.mcu-revision`：产品正文称 ESP32-D0WDQ6-V3，原理图 U3 仅标 ESP32-D0WDQ6，未显示 V3 后缀。（证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U3）
- `memory.flash-capacity`：产品正文标称 16MB，原理图只标 W25Q128JVPIQ，未直接以字节数标注容量。（证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 U4）
- `component.lcd-spec`：正文称 ST7789V2、1.14英寸、240x135；原理图只标 J2 LCD FPC 与信号，未标驱动器/分辨率。（证据：图 cc25a3bc6d25 / 第 1 页 / 第2资源 J2 LCD）
- `power.battery-capacity`：原理图确认双支路并联，但未标正文中的 18650 x2 和 2200mAh 容量。（证据：图 5b1d9bbc2949 / 第 1 页 / 第3资源电池区，未标型号/容量）
- `bus.pwr485`：资源第1页 UE1 的 RO/DI/RE/DE 分别关联 GPIO3/GPIO1/GPIO2，A/B 接 RS_A/RS_B，JE1/JE2 同时带 VIN_12V/GND。（证据：图 9abe5c6bdfb6 / 第 1 页 / 第1资源 A1-B2 PWR485）
- `power.pwr485-12v`：资源第1页 UE2 SY8303 从 VIN_12V 经 L4 10uH 生成 USB_P050，并带 FF1/FF2、D5 与输入输出滤波。（证据：图 9abe5c6bdfb6 / 第 1 页 / 第1资源 B2-C2 UE2）
- `review.mcu-v3`：Station-Bat K124-B 的主控是否固定为 ESP32-D0WDQ6-V3？；原因：正文带 V3，原理图只标 ESP32-D0WDQ6。
- `review.flash-capacity`：W25Q128JVPIQ 在当前 BOM 中是否对应 16MB？；原因：16MB 来自正文，原理图只给料号。
- `review.lcd-spec`：J2 所接面板是否固定为 ST7789V2、1.14英寸、240x135？；原因：规格来自正文，原理图只画 FPC。
- `review.battery-capacity`：两节并联电池是否均为 18650，合计容量是否 2200mAh？；原因：原理图确认双并联支路但未标电芯规格/容量。
- `review.pwr485-population`：第1页 PWR485 的 UE1/UE2/JE1/JE2 是否在 Station-Bat K124-B 上装配，还是仅供 Station-485 共用？；原因：资源包含该页，但产品正文对比称 Station-485 搭载 PWR485、Station-Bat 搭载电池/IMU。
- `review.pwr485-dcdc`：SY8303 VIN_12V 至 USB_P050 路径是否属于 K124-B 的实装 BOM？；原因：与 PWR485 页装配适用性相同，不能由当前资源确定。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9abe5c6bdfb6898cc836353d20cf9f6283c3f27c2e0068ce6d19f3823210a743` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/Sch_M5Station_v1.3_sch_01.png` |
| 2 | 1 | `cc25a3bc6d25ed4e4f29d4a1ef657523923c972e5e4182afa3076152ab6f365e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/Sch_M5Station_v1.3_sch_02.png` |
| 3 | 1 | `5b1d9bbc2949194dc3d09127d66ad87203165cf372825fffdf48129ebd0d46fc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/Sch_M5Station_v1.3_sch_03.png` |

---

源文档：`zh_CN/core/station_bat.md`

源文档 SHA-256：`8fe37af83e71e8bbf5f3c00ffa0d6abcab92d7c3d3a9b357e997b9839f8f52c2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
