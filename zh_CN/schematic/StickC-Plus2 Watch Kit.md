# StickC-Plus2 Watch Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC-Plus2 Watch Kit |
| SKU | K016-H2 |
| 产品 ID | `stickc-plus2-watch-kit-32a0fef6022f` |
| 源文档 | `zh_CN/accessory/M5StickC Plus2 with Watch Accessories.md` |

## 概述

StickC-Plus2 Watch Kit 的主板以 ESP32-PICO-V3-02 为核心，板上集成 CH9102F USB-UART、RTC8563 实时时钟、MPU-6886 惯性传感器和 SPM1423HM4H-B 数字麦克风。外部接口包括 USB Type-C、STICKIO、四针 I2C 接口、GH2.0-4P GPIO 接口和 8 针 SPI LCD FPC，并配置三枚按键及晶体管驱动蜂鸣器。电源部分由 TP4057 充电器、LP3218DT1G 开关网络、SY7088 5V 升压和 SY8089 3.3V 降压组成，HOLD、WAKE 与 RTC INT 共同参与上电保持和唤醒。原理图还给出了板载天线匹配、USB/外部 IO ESD 防护、自动下载电路和电池电压采样路径。

## 检索关键词

`StickC-Plus2 Watch Kit`、`K016-H2`、`ESP32-PICO-V3-02`、`CH9102F`、`TP4057`、`RTC8563`、`MPU-6886`、`SPM1423HM4H-B`、`SY7088`、`SY8089`、`GS321`、`SGM2578`、`WS4622C-4/TR`、`USB Type-C`、`STICKIO`、`GH2.0-4P`、`I2C`、`SCL GPIO22`、`SDA GPIO21`、`MPU-6886 0x68`、`URX GPIO3`、`UTX GPIO1`、`HOLD GPIO4`、`WAKE`、`RTC INT`、`GPIO34 microphone data`、`GPIO0 microphone clock`、`GPIO2 buzzer`、`GPIO27 LCD backlight`、`GPIO38 battery monitor`、`+5VIN`、`+5VOUT`、`+3.3V`、`VBAT_IN`、`SPI LCD`、`board antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-V3-02 | 主控模块，连接射频、I2C、UART、LCD、音频、按键和电源控制网络 | 图 a44b23c200a4 / 第 1 页 / 网格 1A-2B，U1 ESP32-PICO-V3-02 符号及右侧 GPIO/SCL/SDA/URX/UTX 网络 |
| E1 | 未标注 | 板载射频天线，经 L1/C1/C2 匹配网络连接 U1 LNA_IN | 图 a44b23c200a4 / 第 1 页 / 网格 1A，E1 Antenna、L1 1.8nH、C1 2.0pF、C2 2.4pF 与 U1 LNA_IN |
| Q1 | LMBT3904DW1T1G | 由 DTR/RTS 驱动 EN 和 GPIO0 的自动下载双晶体管电路 | 图 a44b23c200a4 / 第 1 页 / 网格 3A，Q1 LMBT3904DW1T1G、R3/R4 10kΩ 与 DTR/RTS/EN/GPIO0 |
| U2 | CH9102F | USB 转 UART 芯片，提供 TXD/RXD/DTR/RTS | 图 a44b23c200a4 / 第 1 页 / 网格 3A-B，U2 CH9102F、USB_DU_P/N、TXD/RXD/DTR/RTS 和 JP1/JP2 |
| P1 | STICKIO | 八针板间接口，引出电源、电池和 GPIO0/GPIO25/GPIO26/GPIO36 | 图 a44b23c200a4 / 第 1 页 / 网格 3B，P1 STICKIO 的 1-8 脚网络标注 |
| J2 | USB-TYPEC | USB 2.0 数据和 5V 电源输入连接器 | 图 a44b23c200a4 / 第 1 页 / 网格 2D，J2 USB-TYPEC、DP/DN、CC1/CC2、VBUS 与 F1 |
| P2 | Header 4 | 四针 I2C 扩展接口，引出 SCL、SDA、+5VOUT 和 GND | 图 a44b23c200a4 / 第 1 页 / 网格 3C，P2 Header 4 的 SCL/SDA/+5VOUT/GND 引脚 |
| J1 | GH2.0-4P | 四针 GPIO 扩展接口，引出 GPIO33、GPIO32、+5VOUT 和 GND | 图 a44b23c200a4 / 第 1 页 / 网格 4C，J1 GH2.0-4P 的 GPIO33/GPIO32/+5VOUT/GND 引脚 |
| U3 | FPC-0.5-8P | 八针 SPI LCD 接口，包含背光、复位、命令/数据和片选信号 | 图 a44b23c200a4 / 第 1 页 / 网格 4C-D，U3 FPC-0.5-8P 的 CS/VCC/SCK/MOSI/D-C/RST/GND/VLED |
| U4 | SGM2578 / WS4622C-4/TR | GPIO27 控制的 LCD 背光电源负载开关 | 图 a44b23c200a4 / 第 1 页 / 网格 4D，U4 标注 SGM2578、WS4622C-4/TR，VIN=+3.3V、EN=GPIO27、VOUT 接 U3 VLED |
| LS1 | Buzzer | 由 Q2 低端驱动的板载蜂鸣器 | 图 a44b23c200a4 / 第 1 页 / 网格 3C-D，LS1 Buzzer、Q2 SS8050 Y1、D14、R19/C12 和 GPIO2 |
| S1 | SW-PB | 按下接地的 GPIO39 按键 | 图 a44b23c200a4 / 第 1 页 / 网格 2C，S1 SW-PB、GPIO39 与 D5 PESDNC2FD3V3B |
| S2 | SW-PB | 按下接地的 GPIO37 按键 | 图 a44b23c200a4 / 第 1 页 / 网格 2C，S2 SW-PB、GPIO37 与 D8 PESDNC2FD3V3B |
| U5 | TP4057 | +5VIN 输入的单节电池充电控制器 | 图 e56bc0b20196 / 第 1 页 / 网格 1A-B，U5 TP4057、R21 0.8Ω、R26 5.3kΩ 与 VBAT_IN |
| Q3, Q4 | LP3218DT1G | VBAT_IN、+VIN 和 VBAT_OUT 之间的电源路径 MOSFET | 图 e56bc0b20196 / 第 1 页 / 网格 1B-2B，Q3/Q4 LP3218DT1G 及 VBAT_IN/+VIN/VBAT_OUT 主路径 |
| Q7 | SI2302 N SOT-23 | 由 HOLD 网络控制 Q4 门极的电源保持 MOSFET | 图 e56bc0b20196 / 第 1 页 / 网格 2B-C，Q7 SI2302、HOLD、R34 100kΩ 与 Q4 门极控制节点 |
| S3 | SW-PB | 连接 WAKE 网络的电源/唤醒按键 | 图 e56bc0b20196 / 第 1 页 / 网格 2B-C，S3 SW-PB、WAKE、D23 B5819WT 与 D25 ESD |
| U6 | SY7088 | VBAT_OUT 到 5.3V/+5VOUT 的升压转换器 | 图 e56bc0b20196 / 第 1 页 / 网格 3A-B，U6 SY7088、L2 1.5uH、R25/R27、D20 与 +5VOUT |
| U7 | SY8089 | VBAT_OUT 到 +3.3V 的降压转换器 | 图 e56bc0b20196 / 第 1 页 / 网格 3B-C，U7 SY8089、3V3EN、L3 4.7uH、R32/R33 与 +3V3OUT/+3.3V |
| U8 | GS321 | 根据 WAKE/+5VOUT 网络生成 3V3EN 并驱动绿色指示网络 | 图 e56bc0b20196 / 第 1 页 / 网格 1D-2D，U8 GS321、D26/D27、R35-R38、3V3EN 和 LED1 GREEN |
| U9 | RTC8563 | 由 VBAT_IN 供电的 I2C 实时时钟，提供 INT 唤醒信号 | 图 e56bc0b20196 / 第 1 页 / 网格 4D，U9 RTC8563、SCL/SDA/INT、VBAT_IN 与 Y1 |
| Y1 | 32.768kHz ±20ppm 12.5pF | RTC8563 的低频时钟晶体 | 图 e56bc0b20196 / 第 1 页 / 网格 3D，Y1 32.768kHz 与 C26/C28 6.0pF、OSCI/OSCO |
| J3 | Header 2 | VBAT_IN 与 GND 的两针电池连接器 | 图 e56bc0b20196 / 第 1 页 / 网格 1C，J3 Header 2，pin2=VBAT_IN、pin1=GND |
| U10 | MPU-6886 | I2C 惯性传感器，原理图标注 7 位地址 0x68 | 图 133d1dbcee40 / 第 1 页 / 网格 2B-3B，U10 MPU-6886、SCL/SDA、AD0/SDO、CS、VDD/VDDIO 与 0x68 标注 |
| U11 | SPM1423HM4H-B | 3.3V 数字麦克风，DAT 接 GPIO34、CLK 接 GPIO0 | 图 133d1dbcee40 / 第 1 页 / 网格 2C-3C，U11 SPM1423HM4H-B、3V3、DAT GPIO34、CLK GPIO0 与 SELECT/GND |

## 系统结构

### 主板功能架构

U1 ESP32-PICO-V3-02 连接板载天线、CH9102F USB-UART、I2C RTC8563 与 MPU-6886、SPM1423HM4H-B 数字麦克风、SPI LCD、三枚按键、蜂鸣器和电源控制网络。

- 参数与网络：`controller=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`microphone=U11 SPM1423HM4H-B`
- 证据：图 a44b23c200a4 / 第 1 页 / 全图 U1 及 USB-UART、LCD、按键、蜂鸣器和外部接口网络; 图 e56bc0b20196 / 第 1 页 / 全图充电、稳压、保持/唤醒和 RTC 电路; 图 133d1dbcee40 / 第 1 页 / 网格 2B-3C 的 MPU-6886 与 SPM1423HM4H-B

## 电源

### USB 5V 输入路径

J2 VCC 经 F1 6V/1A PPTC 到 VBUS，再经 D15 SS34 形成 +5VIN；VBUS 还经 D29 1N4148WT 向 CH9102F 的 +VDD 供电节点送电。

- 参数与网络：`connector=J2`；`fuse=F1 6V/1A/PPTC`；`input_net=VBUS`；`system_input=+5VIN via D15 SS34`；`usb_uart_supply=+VDD via D29 1N4148WT`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2D-3D 的 J2/F1/VBUS/D15/+5VIN 与网格 3B 的 D29/+VDD/U2

### TP4057 电池充电路径

+5VIN 经 R21 0.8Ω 进入 U5 TP4057 VCC，U5 BAT 输出 VBAT_IN，PROG 通过 R26 5.3kΩ 接地。

- 参数与网络：`charger=U5 TP4057`；`input=+5VIN via R21 0.8Ω`；`battery_net=VBAT_IN`；`program_resistor=R26 5.3kΩ`；`input_capacitor=C14 10uF`；`battery_capacitor=C20 10uF`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 1A-B，+5VIN、R21、U5、R26、VBAT_IN、C14/C20

### 电池主电源路径

VBAT_IN 经 Q3 LP3218DT1G 到 +VIN，再经 Q4 LP3218DT1G 到 VBAT_OUT；+5VIN 还通过 D21 SS34 连接 VBAT_OUT。

- 参数与网络：`battery_path=VBAT_IN-Q3-+VIN-Q4-VBAT_OUT`；`usb_feed=+5VIN-D21-VBAT_OUT`；`mosfets=Q3 LP3218DT1G, Q4 LP3218DT1G`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 1A-3B，VBAT_IN、Q3、+VIN、Q4、VBAT_OUT 与 D21

### 电源保持与唤醒控制

Q4 门极控制节点通过 D22 B5819WT 接 RTC INT、通过 D23 B5819WT 接 WAKE，并由 Q7 SI2302 受 HOLD 控制；HOLD 由 U1 GPIO4 输出。

- 参数与网络：`switched_device=Q4 LP3218DT1G`；`rtc_wake=INT via D22 B5819WT`；`button_wake=WAKE via D23 B5819WT`；`hold_switch=Q7 SI2302`；`hold_gpio=4`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2B，U1 IO4 标注 HOLDGPIO4; 图 e56bc0b20196 / 第 1 页 / 网格 2B-C，Q4 门极、D22 INT、D23 WAKE、Q7 HOLD 与 R24/R34

### +5VOUT 升压电源

U6 SY7088 从 VBAT_OUT 经 R22 0Ω 和 L2 1.5uH 取电，输出节点标注 5.3V，并经 D20 SS34 形成 +5VOUT；反馈分压为 R25 160kΩ 与 R27 47kΩ。

- 参数与网络：`converter=U6 SY7088`；`input=VBAT_OUT`；`inductor=L2 1.5uH`；`intermediate_output=5.3V`；`system_output=+5VOUT via D20 SS34`；`feedback=R25 160kΩ, R27 47kΩ`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 3A-B，R22/L2/U6/R25/R27/5.3V/D20/+5VOUT

### +3.3V 降压电源

U7 SY8089 从 VBAT_OUT 降压，EN 接 3V3EN，经 L3 4.7uH 输出 +3V3OUT/+3.3V；反馈分压为 R32 68kΩ 与 R33 15kΩ。

- 参数与网络：`converter=U7 SY8089`；`input=VBAT_OUT`；`enable=3V3EN`；`inductor=L3 4.7uH`；`output=+3V3OUT / +3.3V`；`feedback=R32 68kΩ, R33 15kΩ`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 3B-C，U7、3V3EN、L3、R32/R33 与 +3V3OUT/+3.3V

### 3V3EN 与绿色电源指示

U8 GS321 由 +5VOUT 供电，输入网络连接 WAKE 和 +5VOUT 分压，输出为 3V3EN；该输出节点同时连接 LED1 GREEN 与 R39 2kΩ 指示支路。

- 参数与网络：`comparator=U8 GS321`；`supply=+5VOUT`；`output=3V3EN`；`indicator=LED1 GREEN with R39 2kΩ`；`input_network=D26, D27, R35 680kΩ, R36 270kΩ, R37 10kΩ, R38 10kΩ`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 1D-2D，WAKE、D26/D27、U8、3V3EN、LED1 和 R35-R39

## 接口

### USB Type-C 数据和 CC 配置

J2 的 DP1/DP2 并接 USB_DU_P，DN1/DN2 并接 USB_DU_N；CC1 和 CC2 分别通过 R18/R20 5.1kΩ 接地。

- 参数与网络：`connector=J2 USB-TYPEC`；`dp_net=USB_DU_P`；`dm_net=USB_DU_N`；`cc1_pulldown=R18 5.1kΩ`；`cc2_pulldown=R20 5.1kΩ`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2D，J2 DP1/DP2/DN1/DN2/CC1/CC2 与 R18/R20

### P1 STICKIO 引脚

P1 pin1=GND、pin2=+5VOUT、pin3=GPIO26、pin4 同时连接 GPIO36 与 GPIO25、pin5=GPIO0、pin6=VBAT_IN、pin7=+3.3V、pin8 通过 D2 SS34 连接 +5VIN。

- 参数与网络：`connector=P1 STICKIO`；`pin1=GND`；`pin2=+5VOUT`；`pin3=GPIO26`；`pin4=GPIO36 and GPIO25`；`pin5=GPIO0`；`pin6=VBAT_IN`；`pin7=+3.3V`；`pin8=+5VIN via D2 SS34`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 3B，P1 STICKIO 1-8 脚及左侧网络

### P2 四针 I2C 接口

P2 pin1=SCL、pin2=SDA、pin3=+5VOUT、pin4=GND。

- 参数与网络：`connector=P2 Header 4`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 3C，P2 Header 4 的四个引脚

### J1 四针 GPIO 接口

J1 pin1=GPIO33、pin2=GPIO32、pin3=+5VOUT、pin4=GND；GPIO33、GPIO32 和 +5VOUT 分别配置 D12、D13、D28 对地防护。

- 参数与网络：`connector=J1 GH2.0-4P`；`pin1=GPIO33`；`pin2=GPIO32`；`pin3=+5VOUT`；`pin4=GND`；`protection=D12, D13, D28`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 4C，J1 GH2.0-4P 与 D12/D13/D28

### SPI LCD FPC 引脚

U3 pin1 CS=GPIO5、pin2 VCC=+3.3V、pin3 SCK=GPIO13 经 R17 0Ω、pin4 MOSI=GPIO15、pin5 D/C=GPIO14、pin6 RST=GPIO12、pin7=GND、pin8=VLED。

- 参数与网络：`connector=U3 FPC-0.5-8P`；`cs_gpio=5`；`sck_gpio=13`；`mosi_gpio=15`；`dc_gpio=14`；`reset_gpio=12`；`supply=+3.3V`；`backlight=VLED`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 4C-D，U3 1-8 脚、GPIO5/13/15/14/12、R17 和 VLED

### J3 电池接口

J3 Header 2 的 pin2 接 VBAT_IN，pin1 接 GND；VBAT_IN 配置 C35 100nF 对地。

- 参数与网络：`connector=J3 Header 2`；`pin1=GND`；`pin2=VBAT_IN`；`decoupling=C35 100nF`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 1C，J3、VBAT_IN、GND 与 C35

## 总线

### 主 I2C 总线

U1 GPIO22 形成 SCL，GPIO21 形成 SDA；SCL/SDA 连接 P2、RTC8563 和 MPU-6886，并分别通过 R10/R13 2.2kΩ 上拉到 +3.3V。

- 参数与网络：`scl_gpio=22`；`sda_gpio=21`；`scl_pullup=R10 2.2kΩ`；`sda_pullup=R13 2.2kΩ`；`devices=P2, U9 RTC8563, U10 MPU-6886`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2B-3C，U1 IO22/IO21、R10/R13 与 P2 SCL/SDA; 图 e56bc0b20196 / 第 1 页 / 网格 4D，U9 SCL/SDA; 图 133d1dbcee40 / 第 1 页 / 网格 2B，U10 SCL/SCLK 与 SDA/SDI

### ESP32 与 CH9102F UART

U1 U0RXD/IO3 经 R11 0Ω 连接 URX，U1 U0TXD/IO1 经 R12 0Ω 连接 UTX；URX 接 U2 TXD，UTX 接 U2 RXD。

- 参数与网络：`rx_gpio=3`；`tx_gpio=1`；`rx_path=U2 TXD-URX-R11-U1 U0RXD/IO3`；`tx_path=U1 U0TXD/IO1-R12-UTX-U2 RXD`；`series_resistors=R11 0Ω, R12 0Ω`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2B-4A，U1 U0RXD/U0TXD、R11/R12、URX/UTX 与 U2 TXD/RXD

### RTC8563 连接

U9 RTC8563 的 SCL/SDA 接主 I2C 总线，INT 接电源唤醒控制网络，VDD 接 VBAT_IN，VSS 接 GND。

- 参数与网络：`reference=U9`；`part_number=RTC8563`；`bus=I2C SCL/SDA`；`interrupt=INT`；`supply=VBAT_IN`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 4D，U9 的 SCL/SDA/INT/VDD/VSS

## 总线地址

### MPU-6886 I2C 地址

原理图在 U10 下方明确标注 MPU-6886 的 7 位 I2C 地址为 0x68。

- 参数与网络：`device=U10 MPU-6886`；`address_7bit=0x68`；`ad0_level=GND`
- 证据：图 133d1dbcee40 / 第 1 页 / 网格 2B，U10 下方文字 I2C Addr(7-bit): 0x68

## GPIO 与控制信号

### LCD 背光使能

U4 的 VIN 接 +3.3V、VOUT 接 U3 VLED、EN 接 GPIO27，因此 GPIO27 控制 LCD 背光供电。

- 参数与网络：`switch=U4 SGM2578 / WS4622C-4/TR`；`enable_gpio=27`；`input=+3.3V`；`output=U3 VLED`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 4D，U4 VIN/VOUT/EN 与 U3 VLED、GPIO27

### S1 用户按键

S1 按下时将 GPIO39 接地，GPIO39 经 R2 10kΩ 上拉到 +3.3V，并由 D5 PESDNC2FD3V3B 对地防护。

- 参数与网络：`switch=S1`；`gpio=39`；`active_level=low`；`pullup=R2 10kΩ`；`protection=D5 PESDNC2FD3V3B`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2A-C，U1 GPIO39、R2、S1 和 D5

### S2 用户按键

S2 按下时将 GPIO37 接地，GPIO37 经 R1 10kΩ 上拉到 +3.3V，并由 D8 PESDNC2FD3V3B 对地防护。

- 参数与网络：`switch=S2`；`gpio=37`；`active_level=low`；`pullup=R1 10kΩ`；`protection=D8 PESDNC2FD3V3B`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2A-C，U1 GPIO37、R1、S2 和 D8

### S3 WAKE 按键

S3 按下时将 WAKE 网络接地；WAKE 通过 D23 B5819WT 接入 Q4 门极控制节点，并由 D25 PESDNC2FD3V3B 对地防护。

- 参数与网络：`switch=S3`；`net=WAKE`；`active_level=low`；`gate_diode=D23 B5819WT`；`protection=D25 PESDNC2FD3V3B`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 2B-C，S3、WAKE、D23、D25 与 Q4 门极网络

### WAKE 到 ESP32 监测路径

U1 SENSOR_CAPN/IO35 节点通过 D1 B5819WT 连接 WAKE，IO35 侧由 R6 10kΩ 上拉到 +3.3V。

- 参数与网络：`gpio=35`；`net=WAKE`；`diode=D1 B5819WT`；`pullup=R6 10kΩ`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2A，U1 pin11 SENSOR_CAPN/IO35、R6、D1 与 WAKE

## 时钟

### RTC 32.768kHz 时钟

Y1 32.768kHz ±20ppm 12.5pF 晶体连接 U9 OSCI/OSCO，两个端点分别通过 C26/C28 6.0pF 对地。

- 参数与网络：`rtc=U9 RTC8563`；`crystal=Y1 32.768kHz ±20ppm 12.5pF`；`load_capacitors=C26 6.0pF, C28 6.0pF`；`pins=OSCI, OSCO`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 3D-4D，Y1、C26/C28 与 U9 OSCI/OSCO

## 复位

### ESP32 EN 上拉与延时

U1 EN 网络由 R7 10kΩ 上拉到 +3.3V，并由 C6 100nF 对地；Q1 自动下载网络也连接该 EN 节点。

- 参数与网络：`net=EN`；`pullup=R7 10kΩ`；`capacitor=C6 100nF`；`controller_pin=U1 pin9 EN`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 1A-B，U1 pin9 EN、R7 和 C6；网格 3A Q1 EN 输出

## 保护电路

### USB 数据线 ESD 防护

USB_DU_P 和 USB_DU_N 在 J2 侧分别由 D18 和 D19 PESDNC2FD3V3B 对地防护。

- 参数与网络：`dp_protection=D18 PESDNC2FD3V3B`；`dm_protection=D19 PESDNC2FD3V3B`；`reference=GND`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 1D-2D，USB_DU_P/N 与 D18/D19 对地支路

### STICKIO 和电源轨 ESD 防护

P1 相关的 +5VOUT、GPIO26、GPIO36、GPIO0、VBAT_IN、+3.3V 和 +5VIN 分别由 D3、D4、D6、D7、D9、D10、D11 对地防护。

- 参数与网络：`+5VOUT=D3 PESDNC2FD5VB`；`GPIO26=D4 PESDNC2FD3V3B`；`GPIO36=D6 PESDNC2FD3V3B`；`GPIO0=D7 PESDNC2FD3V3B`；`VBAT_IN=D9 PESDNC2FD5VB`；`+3.3V=D10 PESDNC2FD3V3B`；`+5VIN=D11 PESDNC2FD5VB`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 1B-C，D3/D4/D6/D7/D9/D10/D11 与各网络名

## 关键网络

### 主要 GPIO 功能映射

原理图映射为 GPIO4=HOLD、GPIO22=SCL、GPIO21=SDA、GPIO3=URX、GPIO1=UTX、GPIO5/13/15/14/12=LCD CS/SCK/MOSI/D-C/RST、GPIO27=LCD 背光使能、GPIO2=蜂鸣器、GPIO38=电池采样、GPIO34/0=麦克风 DAT/CLK。

- 参数与网络：`hold=GPIO4`；`i2c=SCL GPIO22, SDA GPIO21`；`uart=URX GPIO3, UTX GPIO1`；`lcd=CS GPIO5, SCK GPIO13, MOSI GPIO15, D/C GPIO14, RST GPIO12, BL GPIO27`；`buzzer=GPIO2`；`battery_adc=GPIO38`；`microphone=DAT GPIO34, CLK GPIO0`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 右侧 GPIO 网络以及网格 3C-4D 的蜂鸣器、LCD 和接口连接; 图 e56bc0b20196 / 第 1 页 / 网格 1C 的 GPIO38 电池分压与网格 2B-C 的 HOLD 控制; 图 133d1dbcee40 / 第 1 页 / 网格 2C-3C，U11 DAT GPIO34 与 CLK GPIO0

### 主要电源轨关系

+5VIN 为 USB 输入和充电器输入，VBAT_IN 为电池/RTC 供电节点，VBAT_OUT 为受保持/唤醒控制后的稳压输入，U6 生成 +5VOUT，U7 生成 +3.3V。

- 参数与网络：`usb_input=+5VIN`；`battery_and_rtc=VBAT_IN`；`switched_source=VBAT_OUT`；`five_volt_output=+5VOUT via U6 SY7088`；`three_volt_output=+3.3V via U7 SY8089`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 2D-4D，USB +5VIN、+5VOUT 和 +3.3V 的使用端; 图 e56bc0b20196 / 第 1 页 / 全图 +5VIN、VBAT_IN、VBAT_OUT、U6 +5VOUT 与 U7 +3.3V 电源链

## 音频

### 蜂鸣器驱动

GPIO2 经 R19 470Ω 和 C12 10uF 驱动 Q2 SS8050 Y1，Q2 低端开关控制 LS1 Buzzer；D14 1N4148WT 跨接蜂鸣器支路。

- 参数与网络：`control_gpio=2`；`transistor=Q2 SS8050 Y1`；`buzzer=LS1`；`input_network=R19 470Ω, C12 10uF, D19 1N4148WT`；`flyback_diode=D14 1N4148WT`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 3C-D，GPIO2、R19、C12、D19、Q2、LS1 和 D14

### SPM1423 数字麦克风

U11 SPM1423HM4H-B 由 +3.3V 供电，DAT 接 GPIO34，CLK 接 GPIO0，SELECT 与两个 GND 引脚均接地。

- 参数与网络：`reference=U11`；`part_number=SPM1423HM4H-B`；`data_gpio=34`；`clock_gpio=0`；`select=GND`；`supply=+3.3V`
- 证据：图 133d1dbcee40 / 第 1 页 / 网格 2C-3C，U11 SPM1423HM4H-B、DAT/CLK/SELECT/3V3/GND

## 传感器

### MPU-6886 I2C 连接

U10 MPU-6886 的 SCL/SCLK 接 SCL、SDA/SDI 接 SDA，CS 接 +3.3V，AD0/SDO 接 GND，VDD 和 VDDIO 接 +3.3V；INT 未连接。

- 参数与网络：`reference=U10`；`part_number=MPU-6886`；`bus=I2C`；`cs=+3.3V`；`ad0=GND`；`supply=+3.3V`；`interrupt=NC`
- 证据：图 133d1dbcee40 / 第 1 页 / 网格 2B-3B，U10 全部总线、地址选择、电源和 INT 引脚

## 射频

### 板载天线射频路径

E1 Antenna 通过 L1 1.8nH 串联至 U1 LNA_IN，天线侧配置 C1 2.0pF、芯片侧配置 C2 2.4pF 对地。

- 参数与网络：`antenna=E1`；`soc_pin=U1 LNA_IN`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF, C2 2.4pF`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 1A，E1、L1、C1、C2 与 U1 LNA_IN

## 调试与烧录

### UART 自动下载控制

U2 的 DTR 和 RTS 进入 Q1 LMBT3904DW1T1G 双晶体管网络，分别协同控制 U1 的 EN 与 GPIO0，R3/R4 均为 10kΩ。

- 参数与网络：`uart_bridge=U2 CH9102F`；`transistor=Q1 LMBT3904DW1T1G`；`control_inputs=DTR, RTS`；`controlled_nets=EN, GPIO0`；`resistors=R3 10kΩ, R4 10kΩ`
- 证据：图 a44b23c200a4 / 第 1 页 / 网格 3A，Q1 与 DTR/RTS/EN/GPIO0；网格 4A 的 U2 DTR/RTS

## 模拟电路

### 电池电压采样

VBAT_IN 通过 R40/R41 各 100kΩ 分压到 GPIO38，分压中点配置 C42 100nF 对地。

- 参数与网络：`source=VBAT_IN`；`adc_gpio=38`；`upper_resistor=R40 100kΩ`；`lower_resistor=R41 100kΩ`；`filter_capacitor=C42 100nF`
- 证据：图 e56bc0b20196 / 第 1 页 / 网格 1C，VBAT_IN、R40/R41、GPIO38 与 C42

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 主板功能架构 | `controller=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`microphone=U11 SPM1423HM4H-B` |
| 射频 | 板载天线射频路径 | `antenna=E1`；`soc_pin=U1 LNA_IN`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF, C2 2.4pF` |
| 总线 | 主 I2C 总线 | `scl_gpio=22`；`sda_gpio=21`；`scl_pullup=R10 2.2kΩ`；`sda_pullup=R13 2.2kΩ`；`devices=P2, U9 RTC8563, U10 MPU-6886` |
| 总线 | ESP32 与 CH9102F UART | `rx_gpio=3`；`tx_gpio=1`；`rx_path=U2 TXD-URX-R11-U1 U0RXD/IO3`；`tx_path=U1 U0TXD/IO1-R12-UTX-U2 RXD`；`series_resistors=R11 0Ω, R12 0Ω` |
| 调试与烧录 | UART 自动下载控制 | `uart_bridge=U2 CH9102F`；`transistor=Q1 LMBT3904DW1T1G`；`control_inputs=DTR, RTS`；`controlled_nets=EN, GPIO0`；`resistors=R3 10kΩ, R4 10kΩ` |
| 复位 | ESP32 EN 上拉与延时 | `net=EN`；`pullup=R7 10kΩ`；`capacitor=C6 100nF`；`controller_pin=U1 pin9 EN` |
| 接口 | USB Type-C 数据和 CC 配置 | `connector=J2 USB-TYPEC`；`dp_net=USB_DU_P`；`dm_net=USB_DU_N`；`cc1_pulldown=R18 5.1kΩ`；`cc2_pulldown=R20 5.1kΩ` |
| 电源 | USB 5V 输入路径 | `connector=J2`；`fuse=F1 6V/1A/PPTC`；`input_net=VBUS`；`system_input=+5VIN via D15 SS34`；`usb_uart_supply=+VDD via D29 1N4148WT` |
| 保护电路 | USB 数据线 ESD 防护 | `dp_protection=D18 PESDNC2FD3V3B`；`dm_protection=D19 PESDNC2FD3V3B`；`reference=GND` |
| 接口 | P1 STICKIO 引脚 | `connector=P1 STICKIO`；`pin1=GND`；`pin2=+5VOUT`；`pin3=GPIO26`；`pin4=GPIO36 and GPIO25`；`pin5=GPIO0`；`pin6=VBAT_IN`；`pin7=+3.3V`；`pin8=+5VIN via D2 SS34` |
| 接口 | P2 四针 I2C 接口 | `connector=P2 Header 4`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND` |
| 接口 | J1 四针 GPIO 接口 | `connector=J1 GH2.0-4P`；`pin1=GPIO33`；`pin2=GPIO32`；`pin3=+5VOUT`；`pin4=GND`；`protection=D12, D13, D28` |
| 接口 | SPI LCD FPC 引脚 | `connector=U3 FPC-0.5-8P`；`cs_gpio=5`；`sck_gpio=13`；`mosi_gpio=15`；`dc_gpio=14`；`reset_gpio=12`；`supply=+3.3V`；`backlight=VLED` |
| GPIO 与控制信号 | LCD 背光使能 | `switch=U4 SGM2578 / WS4622C-4/TR`；`enable_gpio=27`；`input=+3.3V`；`output=U3 VLED` |
| 音频 | 蜂鸣器驱动 | `control_gpio=2`；`transistor=Q2 SS8050 Y1`；`buzzer=LS1`；`input_network=R19 470Ω, C12 10uF, D19 1N4148WT`；`flyback_diode=D14 1N4148WT` |
| GPIO 与控制信号 | S1 用户按键 | `switch=S1`；`gpio=39`；`active_level=low`；`pullup=R2 10kΩ`；`protection=D5 PESDNC2FD3V3B` |
| GPIO 与控制信号 | S2 用户按键 | `switch=S2`；`gpio=37`；`active_level=low`；`pullup=R1 10kΩ`；`protection=D8 PESDNC2FD3V3B` |
| GPIO 与控制信号 | S3 WAKE 按键 | `switch=S3`；`net=WAKE`；`active_level=low`；`gate_diode=D23 B5819WT`；`protection=D25 PESDNC2FD3V3B` |
| 电源 | TP4057 电池充电路径 | `charger=U5 TP4057`；`input=+5VIN via R21 0.8Ω`；`battery_net=VBAT_IN`；`program_resistor=R26 5.3kΩ`；`input_capacitor=C14 10uF`；`battery_capacitor=C20 10uF` |
| 接口 | J3 电池接口 | `connector=J3 Header 2`；`pin1=GND`；`pin2=VBAT_IN`；`decoupling=C35 100nF` |
| 模拟电路 | 电池电压采样 | `source=VBAT_IN`；`adc_gpio=38`；`upper_resistor=R40 100kΩ`；`lower_resistor=R41 100kΩ`；`filter_capacitor=C42 100nF` |
| 电源 | 电池主电源路径 | `battery_path=VBAT_IN-Q3-+VIN-Q4-VBAT_OUT`；`usb_feed=+5VIN-D21-VBAT_OUT`；`mosfets=Q3 LP3218DT1G, Q4 LP3218DT1G` |
| 电源 | 电源保持与唤醒控制 | `switched_device=Q4 LP3218DT1G`；`rtc_wake=INT via D22 B5819WT`；`button_wake=WAKE via D23 B5819WT`；`hold_switch=Q7 SI2302`；`hold_gpio=4` |
| GPIO 与控制信号 | WAKE 到 ESP32 监测路径 | `gpio=35`；`net=WAKE`；`diode=D1 B5819WT`；`pullup=R6 10kΩ` |
| 电源 | +5VOUT 升压电源 | `converter=U6 SY7088`；`input=VBAT_OUT`；`inductor=L2 1.5uH`；`intermediate_output=5.3V`；`system_output=+5VOUT via D20 SS34`；`feedback=R25 160kΩ, R27 47kΩ` |
| 电源 | +3.3V 降压电源 | `converter=U7 SY8089`；`input=VBAT_OUT`；`enable=3V3EN`；`inductor=L3 4.7uH`；`output=+3V3OUT / +3.3V`；`feedback=R32 68kΩ, R33 15kΩ` |
| 电源 | 3V3EN 与绿色电源指示 | `comparator=U8 GS321`；`supply=+5VOUT`；`output=3V3EN`；`indicator=LED1 GREEN with R39 2kΩ`；`input_network=D26, D27, R35 680kΩ, R36 270kΩ, R37 10kΩ, R38 10kΩ` |
| 时钟 | RTC 32.768kHz 时钟 | `rtc=U9 RTC8563`；`crystal=Y1 32.768kHz ±20ppm 12.5pF`；`load_capacitors=C26 6.0pF, C28 6.0pF`；`pins=OSCI, OSCO` |
| 总线 | RTC8563 连接 | `reference=U9`；`part_number=RTC8563`；`bus=I2C SCL/SDA`；`interrupt=INT`；`supply=VBAT_IN` |
| 传感器 | MPU-6886 I2C 连接 | `reference=U10`；`part_number=MPU-6886`；`bus=I2C`；`cs=+3.3V`；`ad0=GND`；`supply=+3.3V`；`interrupt=NC` |
| 总线地址 | MPU-6886 I2C 地址 | `device=U10 MPU-6886`；`address_7bit=0x68`；`ad0_level=GND` |
| 音频 | SPM1423 数字麦克风 | `reference=U11`；`part_number=SPM1423HM4H-B`；`data_gpio=34`；`clock_gpio=0`；`select=GND`；`supply=+3.3V` |
| 保护电路 | STICKIO 和电源轨 ESD 防护 | `+5VOUT=D3 PESDNC2FD5VB`；`GPIO26=D4 PESDNC2FD3V3B`；`GPIO36=D6 PESDNC2FD3V3B`；`GPIO0=D7 PESDNC2FD3V3B`；`VBAT_IN=D9 PESDNC2FD5VB`；`+3.3V=D10 PESDNC2FD3V3B`；`+5VIN=D11 PESDNC2FD5VB` |
| 关键网络 | 主要 GPIO 功能映射 | `hold=GPIO4`；`i2c=SCL GPIO22, SDA GPIO21`；`uart=URX GPIO3, UTX GPIO1`；`lcd=CS GPIO5, SCK GPIO13, MOSI GPIO15, D/C GPIO14, RST GPIO12, BL GPIO27`；`buzzer=GPIO2`；`battery_adc=GPIO38`；`microphone=DAT GPIO34, CLK GPIO0` |
| 关键网络 | 主要电源轨关系 | `usb_input=+5VIN`；`battery_and_rtc=VBAT_IN`；`switched_source=VBAT_OUT`；`five_volt_output=+5VOUT via U6 SY7088`；`three_volt_output=+3.3V via U7 SY8089` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a44b23c200a4052e33ff2e67e575176683c6335c25e093443e17e6628ebf0a36` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_01.png` |
| 2 | 1 | `e56bc0b20196c58678f9329745e939049a8df033794105dfc0965a88d05582e9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_02.png` |
| 3 | 1 | `133d1dbcee40c1d727b4f9c1969d5684a74b19959a8c16b1c759ebc97537137e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_03.png` |

---

源文档：`zh_CN/accessory/M5StickC Plus2 with Watch Accessories.md`

源文档 SHA-256：`78443b632ada703102c7027f2f2532456c4d6e550a35d3a5fb8d4b51917069c8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
