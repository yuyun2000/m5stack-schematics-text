# StampFly v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StampFly v1.1 |
| SKU | K138-V11 |
| 产品 ID | `stampfly-v1-1-f012eacc6ec8` |
| 源文档 | `zh_CN/app/StampFly_v1.1.md` |

## 概述

StampFly v1.1 清单提供的三张资源图显示一套 Stamp-S3 双排主控架构：主板集成 INA3221AIRGVR、BMI270、BMM150、BMP280、内置 VL53L3C、四路 SI2302 电机开关、Grove、蜂鸣器和 WS2812。外置 VL53L3C 子板通过 2x4P 接口接入 I2C/XSHUT/GPIO1，并由 HT7533 从 VBAT 生成 3.3V；PMW3901MB-TXQT 光流子板使用标注 2MHz 的四线 SPI，5V 经 LDO 生成 1.8V 与 3.3V/VDDIO。主板以 INA3221 通道 2 和 0.01Ω 分流器监测 VBAT_IN，四路电机由 L-Up/R-Up/L-Down/R-Down 控制。产品正文称 v1.1 改用 Stamp-S3A，但主板资源文件名为 Stamp_Fly_v1.0，图中模块仍标 STAMP-S3-DIP-1.27，因此 v1.1 的主控、射频、Flash、地址和电池参数需当前版本图纸复核。

## 检索关键词

`StampFly v1.1`、`K138-V11`、`Stamp-S3A`、`STAMP-S3-DIP-1.27`、`Stamp_Fly_v1.0`、`INA3221AIRGVR`、`INA3221 0x40`、`VL53L3C 0x29`、`VL53L3CXV0DH/1`、`BMI270`、`BMM150 0x10`、`BMP280 0x76`、`PMW3901MB-TXQT`、`HT7533`、`TPAP7343D-18FS4`、`TPAP7343D-33FS4`、`WS2812`、`SI2302`、`SS8050 Y1`、`INT_SCL`、`INT_SDA`、`EXT_XSHUT`、`INT_XSHUT`、`MOSI`、`MISO`、`SCK`、`CS`、`CS2`、`L-Up`、`R-Up`、`L-Down`、`R-Down`、`GROVE_I`、`GROVE_O`、`BEEP`、`RGB`、`VBAT_IN`、`4-Wire SPI 2MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1, P2 | STAMP-S3-DIP-1.27 | Stamp-S3 双排主控接口，引出传感器总线、电机控制、Grove、蜂鸣器、RGB 和用户键网络 | 图 3fbf45786e9e / 第 1 页 / 网格 2C-D-3D，P1 Header 17、P2 Header 11 与中间 STAMP-S3-DIP-1.27 引脚映射 |
| U1 | INA3221AIRGVR | I2C 三通道电流/电压监测器，原理图使用通道 2 监测 VBAT_IN 路径 | 图 3fbf45786e9e / 第 1 页 / 网格 1A-B，U1 INA3221AIRGVR、CH2N/CH2P、INT_SCL/INT_SDA、A0 与 0x40 标注 |
| U2 | VL53L3CXV0DH/1 | 主板内置 I2C ToF 距离传感器，带 INT_XSHUT 和 INT_G1 控制/中断网络 | 图 3fbf45786e9e / 第 1 页 / 网格 3A-B，U2 VL53L3CXV0DH/1、INT_SCL/INT_SDA、INT_XSHUT、INT_G1 和 +3.3V |
| U3 | BMM150 | INT_SCL/INT_SDA 总线上的 3.3V 磁传感器 | 图 3fbf45786e9e / 第 1 页 / 网格 3B，U3 BMM150、SCK/SDI、PS/CSB、VDD/VDDIO 和 GND |
| U4 | BMI270 | SPI 惯性传感器，连接 MOSI/MISO/SCK/CS 和 INT1 | 图 3fbf45786e9e / 第 1 页 / 网格 2B-C，U4 BMI270、MOSI/MISO/SCK/CS、INT1/INT2 和 +3.3V |
| U5 | BMP280 | INT_SCL/INT_SDA 总线上的 3.3V 气压传感器 | 图 3fbf45786e9e / 第 1 页 / 网格 4B，U5 BMP280、SCK/SDI、CSB、Vdd/Vddio 和 GND |
| P3 | A2005WR-2x4P | 外置 VL53L3C 子板接口，提供 VBAT、GND、INT_SCL/INT_SDA 和 EXT_G1/EXT_XSHUT | 图 3fbf45786e9e / 第 1 页 / 网格 2A，P3 A2005WR-2x4P 的 VBAT/GND/INT_SCL/INT_SDA/EXT_G1/EXT_XSHUT |
| J3 | HY-2.0_IIC | SCL/SDA、+5VOUT 和 GND 的四针 I2C Grove 接口 | 图 3fbf45786e9e / 第 1 页 / 网格 1C，J3 HY-2.0_IIC、SCL/SDA/+5VOUT/GND 与 R23/R24 |
| J2 | HY-2.0_IO | GROVE_I/GROVE_O、+5VOUT 和 GND 的四针通用 Grove 接口 | 图 3fbf45786e9e / 第 1 页 / 网格 4C，J2 HY-2.0_IO、GROVE_I/GROVE_O/+5VOUT/GND |
| P4 | KH-A1001WF-06A | PMW3901MB 子板的六针 SPI 与 5V 电源接口 | 图 3fbf45786e9e / 第 1 页 / 网格 4B-C，P4 的 GND/+5VOUT/MOSI/MISO/SCK/CS2 |
| Q3, Q4, Q5, Q6 | SI2302 | 四路电机的低端开关，分别由 R-Up、L-Up、L-Down、R-Down 控制 | 图 3fbf45786e9e / 第 1 页 / 网格 1A/D 与 4A/D，Q3-Q6 SI2302、四个电机连接器和控制网络 |
| LS1 | Buzzer | 由 Q2 SS8050 Y1 和 BEEP 网络驱动的板载蜂鸣器 | 图 3fbf45786e9e / 第 1 页 / 网格 1C-D，LS1 Buzzer、Q2、D1/D2、R10/R11 与 BEEP |
| LED1, LED2 | WS2812 | 由 RGB 网络驱动的两颗级联可编程 LED | 图 3fbf45786e9e / 第 1 页 / 网格 3C-D，LED1/LED2 WS2812、RGB、DO/DI 和 +3.3V |
| S1 | SW-PB | 按下接地的 USER_A 用户按键 | 图 3fbf45786e9e / 第 1 页 / 网格 3C，S1 SW-PB、USER_A 与 GND |
| U1 | VL53L3CXV0DH/1 | 外置 ToF 子板上的 I2C 距离传感器 | 图 16e1db200cad / 第 1 页 / 网格 2B-3C，U1 VL53L3CXV0DH/1、SDA/SCL、GPIO1、XSHUT、AVDD 和 GND |
| U2 | HT7533 | 外置 ToF 子板的 VBAT 到 3.3V 线性稳压器 | 图 16e1db200cad / 第 1 页 / 网格 2C-3C，U2 HT7533、VBAT、+3.3V、C2/C3 和 J1 |
| P1 | A2005WR-2x4P | 外置 ToF 子板的 VBAT/GND/SCL/SDA/G1/XSHUT 接口 | 图 16e1db200cad / 第 1 页 / 网格 2B，P1 A2005WR-2x4P 与 VBAT、GND、SCL、SDA、G1、XSHUT |
| U4 | PMW3901MB-TXQT | 光流传感器，使用 4 线 SPI 并具有独立 1.8V 和 VDDIO 电源 | 图 ea2f8747c4cc / 第 1 页 / 网格 2C-3D，U4 PMW3901MB-TXQT、MOSI/MISO/SCLK/NCS、NRESET、VDD/VDDIO/VREG |
| U1 | TPAP7343D-18FS4 | PMW3901MB 子板的 5V 到 1.8V LDO | 图 ea2f8747c4cc / 第 1 页 / 网格 2B，U1 TPAP7343D-18FS4、5V、1.8V 和 C1/C2 |
| U2 | TPAP7343D-33FS4 | PMW3901MB 子板的 5V 到 3.3V LDO | 图 ea2f8747c4cc / 第 1 页 / 网格 2B-C，U2 TPAP7343D-33FS4、5V、+3.3V 和 C4/C5 |
| P1 | KH-A1001WF-06A | PMW3901MB 子板的 GND/5V/MOSI/MISO/SCLK/CS2 接口 | 图 ea2f8747c4cc / 第 1 页 / 网格 3B，P1 KH-A1001WF-06A 六针 SPI 接口 |

## 系统结构

### 资源图硬件架构

三张资源图显示 STAMP-S3-DIP-1.27 通过 P1/P2 双排接口连接四路电机开关、INA3221AIRGVR、BMI270、BMM150、BMP280、内置与外置 VL53L3C、PMW3901MB 光流子板、两路 Grove、蜂鸣器、用户键和 RGB LED。

- 参数与网络：`controller_interface=P1/P2 STAMP-S3-DIP-1.27`；`power_monitor=U1 INA3221AIRGVR`；`imu=U4 BMI270`；`magnetometer=U3 BMM150`；`barometer=U5 BMP280`；`tof=two VL53L3CXV0DH/1`；`optical_flow=U4 PMW3901MB-TXQT`
- 证据：图 16e1db200cad / 第 1 页 / 全图外置 VL53L3C 子板及 VBAT 到 3.3V 供电; 图 3fbf45786e9e / 第 1 页 / 全图 Stamp-S3 接口、传感器、四电机、Grove、蜂鸣器和 RGB; 图 ea2f8747c4cc / 第 1 页 / 全图 PMW3901MB 子板、SPI 接口和 1.8V/3.3V 电源

## 电源

### 外置 ToF 子板 3.3V 电源

U2 HT7533 从 VBAT 生成 +3.3V，输入/输出分别配置 C3/C2 10uF；+3.3V 同时供给 VL53L3C、信号上拉和 D1 红色 LED 支路。

- 参数与网络：`regulator=U2 HT7533`；`input=VBAT`；`output=+3.3V`；`input_capacitor=C3 10uF`；`output_capacitor=C2 10uF`；`indicator=D1 red 0603 with R5 10kΩ`
- 证据：图 16e1db200cad / 第 1 页 / 网格 1C-3C，J1、VBAT、U2 HT7533、C2/C3、+3.3V、D1/R5

### PMW3901MB 子板电源

U1 TPAP7343D-18FS4 从 5V 生成 1.8V，U2 TPAP7343D-33FS4 从 5V 生成 +3.3V；PMW3901MB VDD 经 R6 3Ω 接 1.8V，VDDIO 接 VDDIO/+3.3V。

- 参数与网络：`core_ldo=U1 TPAP7343D-18FS4`；`core_rail=1.8V`；`io_ldo=U2 TPAP7343D-33FS4`；`io_rail=+3.3V / VDDIO`；`vdd_series_resistor=R6 3Ω`；`input=5V`
- 证据：图 ea2f8747c4cc / 第 1 页 / 网格 2B-C 的 U1/U2 LDO 与网格 2C-4C 的 U4 VDD/VDDIO/R6 和去耦

### +5VOUT 路径

VBAT_IN 通过 D3 B5819W SL 连接 +5VOUT；+5VOUT 供给 J2/J3 Grove、P4 光流子板接口，并通过 M5V 网络连接 Stamp-S3 接口。

- 参数与网络：`source=VBAT_IN`；`diode=D3 B5819W SL`；`rail=+5VOUT`；`loads=J2, J3, P4 and Stamp-S3 M5V`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1C-4C，D3 VBAT_IN/+5VOUT、J2/J3/P4 电源与 P1 M5V

## 接口

### 外置 VL53L3C 子板连接

主板 P3 向外置子板提供 VBAT、GND、INT_SCL、INT_SDA、EXT_G1 和 EXT_XSHUT；子板 P1 将这些网络映射为 VBAT、GND、SCL、SDA、G1 和 XSHUT。

- 参数与网络：`main_connector=P3 A2005WR-2x4P`；`module_connector=P1 A2005WR-2x4P`；`power=VBAT and GND`；`bus=INT_SCL/INT_SDA to SCL/SDA`；`control=EXT_G1/EXT_XSHUT to G1/XSHUT`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 2A，主板 P3 的 VBAT/GND/INT_SCL/INT_SDA/EXT_G1/EXT_XSHUT; 图 16e1db200cad / 第 1 页 / 网格 2B，子板 P1 的 VBAT/GND/SCL/SDA/G1/XSHUT

### J3 I2C Grove 接口

J3 pin1=SCL、pin2=SDA、pin3=+5VOUT、pin4=GND；SCL/SDA 由 R24/R23 各 4.7kΩ 上拉到 +3.3V。

- 参数与网络：`connector=J3 HY-2.0_IIC`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND`；`pullups=R24 SCL 4.7kΩ, R23 SDA 4.7kΩ`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1C，J3、R23/R24、SCL/SDA/+5VOUT/GND

### J2 通用 Grove 接口

J2 pin1=GROVE_I、pin2=GROVE_O、pin3=+5VOUT、pin4=GND。

- 参数与网络：`connector=J2 HY-2.0_IO`；`pin1=GROVE_I`；`pin2=GROVE_O`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 4C，J2 的 GROVE_I/GROVE_O/+5VOUT/GND

### PMW3901MB 子板接口

主板 P4 与光流子板 P1 均定义 pin1=GND、pin2=5V、pin3=MOSI、pin4=MISO、pin5=SCK/SCLK、pin6=CS/CS2。

- 参数与网络：`main_connector=P4 KH-A1001WF-06A`；`module_connector=P1 KH-A1001WF-06A`；`pin1=GND`；`pin2=5V`；`pin3=MOSI`；`pin4=MISO`；`pin5=SCK/SCLK`；`pin6=CS2`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 4B-C，主板 P4 六针定义; 图 ea2f8747c4cc / 第 1 页 / 网格 3B，光流子板 P1 六针定义

## 总线

### 内部 I2C 总线

INT_SCL/INT_SDA 连接 INA3221、内置 VL53L3C、BMM150、BMP280 和 Stamp-S3 接口；总线由 R13/R14 4.7kΩ 上拉到 +3.3V。

- 参数与网络：`scl=INT_SCL`；`sda=INT_SDA`；`scl_pullup=R13 4.7kΩ`；`sda_pullup=R14 4.7kΩ`；`devices=INA3221, internal VL53L3C, BMM150, BMP280, Stamp-S3`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1A-4B 的 INT_SCL/INT_SDA 同名网络及 R13/R14

### PMW3901MB 4 线 SPI

U4 PMW3901MB-TXQT 的 MOSI/SCLK/MISO/NCS 连接子板接口的 MOSI/SCLK/MISO/CS2，原理图标注 4-Wire SPI @ 2 MHz。

- 参数与网络：`device=U4 PMW3901MB-TXQT`；`mosi=pin16 MOSI`；`clock=pin17 SCLK`；`miso=pin18 MISO`；`chip_select=pin19 NCS to CS2`；`mode=4-Wire SPI`；`frequency=2 MHz`
- 证据：图 ea2f8747c4cc / 第 1 页 / 网格 1C-2D，U4 MOSI/SCLK/MISO/NCS 和文字 4-Wire SPI @ 2 MHz

## 总线地址

### INA3221 I2C 地址

原理图在 U1 下方明确标注 INA3221AIRGVR 的 7 位 I2C 地址为 0x40，A0 接 GND。

- 参数与网络：`device=U1 INA3221AIRGVR`；`address_7bit=0x40`；`a0=GND`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1A，U1 A0 接地及文字 I2C Addr 7-bit 40H

## GPIO 与控制信号

### L-Up 与 R-Up 电机开关

L-Up 经 R5 100Ω 驱动 Q4 SI2302，R-Up 经 R6 100Ω 驱动 Q3 SI2302；两路门极各由 10kΩ 电阻下拉，电机连接器另一端接 VBAT_IN。

- 参数与网络：`left_up=L-Up-R5 100Ω-Q4 SI2302-J1`；`right_up=R-Up-R6 100Ω-Q3 SI2302-J4`；`gate_pulldowns=R8 10kΩ, R9 10kΩ`；`motor_supply=VBAT_IN`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1A 与 4A，J1/Q4/R5/R8/L-Up 及 J4/Q3/R6/R9/R-Up

### L-Down 与 R-Down 电机开关

L-Down 经 R19 100Ω 驱动 Q5 SI2302，R-Down 经 R20 100Ω 驱动 Q6 SI2302；两路门极各由 10kΩ 电阻下拉，电机连接器另一端接 VBAT_IN。

- 参数与网络：`left_down=L-Down-R19 100Ω-Q5 SI2302-J5`；`right_down=R-Down-R20 100Ω-Q6 SI2302-J6`；`gate_pulldowns=R21 10kΩ, R22 10kΩ`；`motor_supply=VBAT_IN`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1D 与 4D，J5/Q5/R19/R21/L-Down 及 J6/Q6/R20/R22/R-Down

### 双 WS2812 指示灯

RGB 接 LED1 DI，LED1 DO 接 LED2 DI，LED2 DO 未继续连接；两颗 WS2812 均由 +3.3V 供电。

- 参数与网络：`data=RGB`；`first=LED1 WS2812`；`second=LED2 WS2812`；`chain=LED1 DO to LED2 DI`；`supply=+3.3V`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 3C-D，RGB、LED1/LED2 DI/DO/VDD/GND

### USER_A 按键

S1 按下时将 USER_A 接 GND，USER_A 同时引出到 Stamp-S3 接口。

- 参数与网络：`switch=S1 SW-PB`；`net=USER_A`；`active_level=low`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 3C-D，S1 USER_A 到 GND 及 P2 USER_A 网络

## 复位

### PMW3901MB 上电复位

U4 NRESET 网络由 VDDIO 侧电阻上拉并配置 C3 10uF 对地，原理图标注 Power on reset 100ms。

- 参数与网络：`device=U4 PMW3901MB-TXQT`；`pin=NRESET pin7`；`capacitor=C3 10uF`；`delay=100ms`
- 证据：图 ea2f8747c4cc / 第 1 页 / 网格 1C-2D，U4 NRESET、C3 和文字 Power on reset 100ms

## 关键网络

### Stamp-S3 功能网络映射

P1/P2 将 GROVE_I、GROVE_O、INT_SDA、INT_SCL、L-Up、INT_G1、INT_XSHUT、EXT_G1、EXT_XSHUT、L-Down、INT1、CS2、SDA、MOSI、SCL、CS、MISO、R-Up、SCK、R-Down、RST、BEEP、USER_A 和 RGB 引到 Stamp-S3。

- 参数与网络：`left_header=P1 Header 17`；`right_header=P2 Header 11`；`motor_controls=L-Up, R-Up, L-Down, R-Down`；`sensor_controls=INT_G1, INT_XSHUT, EXT_G1, EXT_XSHUT, INT1`；`buses=INT_SCL/INT_SDA, SCL/SDA, MOSI/MISO/SCK/CS/CS2`；`user_io=GROVE_I, GROVE_O, BEEP, USER_A, RGB, RST`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 2C-D-3D，P1/P2 两侧全部红色网络标签

## 音频

### 板载蜂鸣器驱动

BEEP 经 R11 470Ω 和 C11 10uF 驱动 Q2 SS8050 Y1，Q2 低端控制 LS1 Buzzer；D1 1N4148WT 跨接蜂鸣器，D2 1N4148WT 对基极节点钳位。

- 参数与网络：`control=BEEP`；`input_network=R11 470Ω, C11 10uF`；`transistor=Q2 SS8050 Y1`；`buzzer=LS1`；`diodes=D1 and D2 1N4148WT`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1C-D，BEEP、R11、C11、D1/D2、Q2 和 LS1

## 传感器

### 主板内置 VL53L3C

U2 VL53L3CXV0DH/1 由 +3.3V 供电，SCL/SDA 接 INT_SCL/INT_SDA，XSHUT 接 INT_XSHUT，GPIO1 接 INT_G1；四个信号均有 4.7kΩ 上拉。

- 参数与网络：`reference=U2`；`part_number=VL53L3CXV0DH/1`；`bus=INT_SCL/INT_SDA`；`shutdown=INT_XSHUT`；`gpio1=INT_G1`；`pullups=R1-R4 4.7kΩ`；`supply=+3.3V`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 3A-B，U2 与 INT_XSHUT/INT_G1/INT_SCL/INT_SDA、R1-R4

### 外置 VL53L3C

外置子板 U1 VL53L3CXV0DH/1 的 SCL/SDA 接子板总线，GPIO1 接 G1，XSHUT 接 XSHUT，AVDD 接 +3.3V，全部地引脚接 GND。

- 参数与网络：`reference=U1`；`part_number=VL53L3CXV0DH/1`；`bus=SCL/SDA`；`gpio1=G1`；`shutdown=XSHUT`；`supply=+3.3V`
- 证据：图 16e1db200cad / 第 1 页 / 网格 2B-3C，U1 全部信号、电源与地连接

### BMI270 SPI 连接

U4 BMI270 的 SDX/SCX/SDO/CSB 分别接 MOSI/SCK/MISO/CS，VDD 和 VDDIO 接 +3.3V，INT1 引出并由 R18 4.7kΩ 上拉，INT2 在器件端标记未连接。

- 参数与网络：`reference=U4 BMI270`；`mosi=SDX`；`miso=SDO`；`clock=SCX`；`chip_select=CSB to CS`；`interrupt=INT1`；`int1_pullup=R18 4.7kΩ`；`int2=NC`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 2B-C，U4 MOSI/MISO/SCK/CS、INT1/INT2、电源和 R18

### BMM150 I2C 连接

U3 BMM150 的 SCK 接 INT_SCL、SDI 接 INT_SDA，PS 接 +3.3V、CSB 接 GND，VDD/VDDIO 接 +3.3V，INT 与 DRDY 未连接。

- 参数与网络：`reference=U3 BMM150`；`scl=INT_SCL`；`sda=INT_SDA`；`ps=+3.3V`；`csb=GND`；`supply=+3.3V`；`interrupts=INT and DRDY NC`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 3B，U3 SCK/SDI/PS/CSB/VDD/VDDIO/INT/DRDY

### BMP280 I2C 连接

U5 BMP280 的 SCK 接 INT_SCL、SDI 接 INT_SDA，CSB 接 +3.3V，Vdd/Vddio 接 +3.3V，SDO 未连接。

- 参数与网络：`reference=U5 BMP280`；`scl=INT_SCL`；`sda=INT_SDA`；`csb=+3.3V`；`sdo=NC`；`supply=+3.3V`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 4B，U5 SCK/SDI/CSB/SDO/Vdd/Vddio

## 模拟电路

### VBAT_IN 电流监测通道

INA3221 U1 仅连接 IN-2/IN+2 到 CH2N/CH2P；CH2N/CH2P 经 R7/R16 各 10Ω 和 C5 100nF 滤波，跨接于 R12 0.01Ω 分流路径两侧。

- 参数与网络：`monitor=U1 INA3221AIRGVR channel 2`；`negative_input=CH2N via R7 10Ω`；`positive_input=CH2P via R16 10Ω`；`filter=C5 100nF`；`shunt=R12 0.01Ω`；`unused_channels=channel 1 and channel 3 marked NC`
- 证据：图 3fbf45786e9e / 第 1 页 / 网格 1A-B，U1 IN±1/2/3、CH2N/CH2P、R7/R16/C5 与 R12

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 资源图硬件架构 | `controller_interface=P1/P2 STAMP-S3-DIP-1.27`；`power_monitor=U1 INA3221AIRGVR`；`imu=U4 BMI270`；`magnetometer=U3 BMM150`；`barometer=U5 BMP280`；`tof=two VL53L3CXV0DH/1`；`optical_flow=U4 PMW3901MB-TXQT` |
| 总线地址 | INA3221 I2C 地址 | `device=U1 INA3221AIRGVR`；`address_7bit=0x40`；`a0=GND` |
| 模拟电路 | VBAT_IN 电流监测通道 | `monitor=U1 INA3221AIRGVR channel 2`；`negative_input=CH2N via R7 10Ω`；`positive_input=CH2P via R16 10Ω`；`filter=C5 100nF`；`shunt=R12 0.01Ω`；`unused_channels=channel 1 and channel 3 marked NC` |
| 总线 | 内部 I2C 总线 | `scl=INT_SCL`；`sda=INT_SDA`；`scl_pullup=R13 4.7kΩ`；`sda_pullup=R14 4.7kΩ`；`devices=INA3221, internal VL53L3C, BMM150, BMP280, Stamp-S3` |
| 传感器 | 主板内置 VL53L3C | `reference=U2`；`part_number=VL53L3CXV0DH/1`；`bus=INT_SCL/INT_SDA`；`shutdown=INT_XSHUT`；`gpio1=INT_G1`；`pullups=R1-R4 4.7kΩ`；`supply=+3.3V` |
| 接口 | 外置 VL53L3C 子板连接 | `main_connector=P3 A2005WR-2x4P`；`module_connector=P1 A2005WR-2x4P`；`power=VBAT and GND`；`bus=INT_SCL/INT_SDA to SCL/SDA`；`control=EXT_G1/EXT_XSHUT to G1/XSHUT` |
| 传感器 | 外置 VL53L3C | `reference=U1`；`part_number=VL53L3CXV0DH/1`；`bus=SCL/SDA`；`gpio1=G1`；`shutdown=XSHUT`；`supply=+3.3V` |
| 电源 | 外置 ToF 子板 3.3V 电源 | `regulator=U2 HT7533`；`input=VBAT`；`output=+3.3V`；`input_capacitor=C3 10uF`；`output_capacitor=C2 10uF`；`indicator=D1 red 0603 with R5 10kΩ` |
| 传感器 | BMI270 SPI 连接 | `reference=U4 BMI270`；`mosi=SDX`；`miso=SDO`；`clock=SCX`；`chip_select=CSB to CS`；`interrupt=INT1`；`int1_pullup=R18 4.7kΩ`；`int2=NC` |
| 传感器 | BMM150 I2C 连接 | `reference=U3 BMM150`；`scl=INT_SCL`；`sda=INT_SDA`；`ps=+3.3V`；`csb=GND`；`supply=+3.3V`；`interrupts=INT and DRDY NC` |
| 传感器 | BMP280 I2C 连接 | `reference=U5 BMP280`；`scl=INT_SCL`；`sda=INT_SDA`；`csb=+3.3V`；`sdo=NC`；`supply=+3.3V` |
| 接口 | J3 I2C Grove 接口 | `connector=J3 HY-2.0_IIC`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND`；`pullups=R24 SCL 4.7kΩ, R23 SDA 4.7kΩ` |
| 接口 | J2 通用 Grove 接口 | `connector=J2 HY-2.0_IO`；`pin1=GROVE_I`；`pin2=GROVE_O`；`pin3=+5VOUT`；`pin4=GND` |
| 接口 | PMW3901MB 子板接口 | `main_connector=P4 KH-A1001WF-06A`；`module_connector=P1 KH-A1001WF-06A`；`pin1=GND`；`pin2=5V`；`pin3=MOSI`；`pin4=MISO`；`pin5=SCK/SCLK`；`pin6=CS2` |
| 总线 | PMW3901MB 4 线 SPI | `device=U4 PMW3901MB-TXQT`；`mosi=pin16 MOSI`；`clock=pin17 SCLK`；`miso=pin18 MISO`；`chip_select=pin19 NCS to CS2`；`mode=4-Wire SPI`；`frequency=2 MHz` |
| 电源 | PMW3901MB 子板电源 | `core_ldo=U1 TPAP7343D-18FS4`；`core_rail=1.8V`；`io_ldo=U2 TPAP7343D-33FS4`；`io_rail=+3.3V / VDDIO`；`vdd_series_resistor=R6 3Ω`；`input=5V` |
| 复位 | PMW3901MB 上电复位 | `device=U4 PMW3901MB-TXQT`；`pin=NRESET pin7`；`capacitor=C3 10uF`；`delay=100ms` |
| GPIO 与控制信号 | L-Up 与 R-Up 电机开关 | `left_up=L-Up-R5 100Ω-Q4 SI2302-J1`；`right_up=R-Up-R6 100Ω-Q3 SI2302-J4`；`gate_pulldowns=R8 10kΩ, R9 10kΩ`；`motor_supply=VBAT_IN` |
| GPIO 与控制信号 | L-Down 与 R-Down 电机开关 | `left_down=L-Down-R19 100Ω-Q5 SI2302-J5`；`right_down=R-Down-R20 100Ω-Q6 SI2302-J6`；`gate_pulldowns=R21 10kΩ, R22 10kΩ`；`motor_supply=VBAT_IN` |
| 音频 | 板载蜂鸣器驱动 | `control=BEEP`；`input_network=R11 470Ω, C11 10uF`；`transistor=Q2 SS8050 Y1`；`buzzer=LS1`；`diodes=D1 and D2 1N4148WT` |
| GPIO 与控制信号 | 双 WS2812 指示灯 | `data=RGB`；`first=LED1 WS2812`；`second=LED2 WS2812`；`chain=LED1 DO to LED2 DI`；`supply=+3.3V` |
| GPIO 与控制信号 | USER_A 按键 | `switch=S1 SW-PB`；`net=USER_A`；`active_level=low` |
| 电源 | +5VOUT 路径 | `source=VBAT_IN`；`diode=D3 B5819W SL`；`rail=+5VOUT`；`loads=J2, J3, P4 and Stamp-S3 M5V` |
| 关键网络 | Stamp-S3 功能网络映射 | `left_header=P1 Header 17`；`right_header=P2 Header 11`；`motor_controls=L-Up, R-Up, L-Down, R-Down`；`sensor_controls=INT_G1, INT_XSHUT, EXT_G1, EXT_XSHUT, INT1`；`buses=INT_SCL/INT_SDA, SCL/SDA, MOSI/MISO/SCK/CS/CS2`；`user_io=GROVE_I, GROVE_O, BEEP, USER_A, RGB, RST` |
| 系统结构 | v1.1 与资源图版本适用性 | `manifest_product=StampFly v1.1`；`sku=K138-V11`；`documented_controller=Stamp-S3A`；`schematic_file=Stamp_Fly_v1.0`；`schematic_module=STAMP-S3-DIP-1.27`；`v1_1_revision_mark=null` |
| 总线地址 | 正文传感器 I2C 地址 | `confirmed_ina3221=0x40`；`documented_bmm150=0x10`；`documented_bmp280=0x76`；`documented_vl53l3=0x29`；`schematic_bmm150_address=null`；`schematic_bmp280_address=null`；`schematic_vl53l3_address=null`；`dual_tof_address_sequence=null` |
| 射频 | Stamp-S3A 无线与天线升级 | `documented_module=Stamp-S3A`；`documented_radio=2.4GHz Wi-Fi / ESP-NOW`；`documented_antenna_change=optimized antenna`；`schematic_rf=null`；`antenna_part=null`；`matching_network=null` |
| 内存与 Flash | 正文 8MB Flash | `documented_flash=8MB`；`flash_part_number=null`；`flash_bus=null`；`flash_voltage=null`；`partition_layout=null` |
| 电源 | 正文电池与充电参数 | `documented_capacity=320mAh`；`documented_full_voltage=4.35V`；`documented_charge_input=5V@1A`；`documented_charge_time=about 55min`；`onboard_charger=null`；`battery_protection=null`；`temperature_monitor=null`；`charge_termination=null` |
| 传感器 | 正文传感器性能参数 | `documented_tof_range=3m`；`documented_bmp280_range=300-1100hPa`；`documented_bmi270_axes=6-axis`；`documented_bmm150_axes=3-axis`；`schematic_accuracy=null`；`sample_rate=null`；`mounting_orientation=null`；`calibration=null` |

## 待确认事项

- `system.v1-1-resource-applicability`：产品清单是 StampFly v1.1/K138-V11，正文称主控升级为 Stamp-S3A；但资源中的主板文件名为 Stamp_Fly_v1.0，图中央模块标为 STAMP-S3-DIP-1.27，三张图均未出现 Stamp-S3A 或 v1.1 版号。（证据：图 3fbf45786e9e / 第 1 页 / 全图中央 P1/P2 灰色模块标注 STAMP-S3-DIP-1.27；资源 URL/文件名为 Stamp_Fly_v1.0）
- `address.documented-sensor-addresses`：正文管脚表列出 BMM150=0x10、BMP280=0x76、VL53L3=0x29；主板原理图只明确标注 INA3221 7-bit 0x40，BMM150/BMP280/VL53L3 的地址值与双 VL53L3 上电后地址管理没有文字说明。（证据：图 3fbf45786e9e / 第 1 页 / 网格 1A-4B，U1 INA3221 有 40H 标注，U2 VL53L3C/U3 BMM150/U5 BMP280 无地址文字; 图 16e1db200cad / 第 1 页 / 网格 2B-3C，外置 U1 VL53L3C 的 SCL/SDA/G1/XSHUT，无地址文字）
- `rf.documented-stamp-s3a-wireless`：正文称 v1.1 使用 Stamp-S3A、优化天线并通过 ESP-NOW 通信；原理图仅显示 STAMP-S3-DIP-1.27 外部引脚接口，没有 ESP32-S3、2.4GHz 射频、天线、匹配网络或 ESP-NOW 电路信息。（证据：图 3fbf45786e9e / 第 1 页 / 网格 2C-D-3D，主控仅以 STAMP-S3-DIP-1.27 接口块表示，无 RF/天线网络）
- `memory.documented-stamp-s3a-flash`：正文规格列出 Stamp-S3A 内含 8MB Flash；三张原理图没有主控模组内部存储器、Flash 型号、容量、SPI/OSPI 连接或分区信息。（证据：图 3fbf45786e9e / 第 1 页 / 全图仅有 STAMP-S3-DIP-1.27 接口块，无独立 Flash 或容量标注）
- `power.documented-battery-and-charge`：正文列出 320mAh、4.35V 高压锂电池和外部 5V@1A/约55分钟充电参数；资源图显示 VBAT/VBAT_IN、电机负载、HT7533 与电源二极管，但未显示充电 IC、电池保护、温度检测、5V 充电输入或充电终止路径。（证据：图 3fbf45786e9e / 第 1 页 / 全图 VBAT/VBAT_IN、INA3221、四电机与 D3 +5VOUT 路径，无充电器件; 图 16e1db200cad / 第 1 页 / 网格 2C-3C，J1 BAT 接口与 HT7533 供电路径，无充电器件）
- `sensor.documented-performance`：正文列出 VL53L3C 最大检测距离3米、BMP280 300-1100hPa，并称 BMI270 六轴与 BMM150 三轴；原理图可确认器件型号和总线连接，但没有量程、精度、采样率、噪声、安装方向或飞控校准参数。（证据：图 3fbf45786e9e / 第 1 页 / 网格 2B-4B，BMI270/BMM150/BMP280/内置 VL53L3C 器件与总线，无性能参数; 图 16e1db200cad / 第 1 页 / 网格 2B-3C，外置 VL53L3C 器件连接，无测距性能参数）
- `review.v1-1-schematic`：请提供 StampFly v1.1/K138-V11 当前正式主板与 Stamp-S3A 模组原理图或网表，并确认哪些 v1.0 网络、器件和 GPIO 映射在 v1.1 保持不变。；原因：资源图仍标 STAMP-S3-DIP-1.27，主板文件名明确为 Stamp_Fly_v1.0。
- `review.sensor-addresses`：请用各器件 datasheet、v1.1 网表和启动代码确认 BMM150/BMP280/两颗 VL53L3C 的实际 7 位地址，以及双 ToF 通过 XSHUT 改址的顺序。；原因：除 INA3221 0x40 外，地址值和双 ToF 地址管理未在原理图明确标注。
- `review.stamp-s3a-rf`：请确认 v1.1 Stamp-S3A 的 ESP32-S3 型号、天线实现、匹配网络、射频版图约束和 ESP-NOW/Wi-Fi 发射性能。；原因：提供的板级原理图把主控模组抽象为旧版接口块，没有射频证据。
- `review.stamp-s3a-flash`：请由 Stamp-S3A 当前 BOM/原理图确认 8MB Flash 的型号、总线、电压、速度和可用分区。；原因：三张资源图均未展开主控模组内部存储。
- `review.battery-charge`：请确认 320mAh/4.35V 电池型号、保护板、允许放电电流及 Atom Joystick 外部充电器的 5V 输入、充电电流、终止电压和温度保护。；原因：StampFly 三张资源图没有充电与电池保护电路。
- `review.sensor-performance`：请用 datasheet、v1.1 安装方向和飞控配置确认各传感器量程、采样率、滤波、校准、坐标系与有效检测距离。；原因：原理图只确认型号和连接，不包含飞控性能参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `16e1db200cad2e6afcb6076ad56bcb615543fa40673878b472fb15788e3c3768` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/StampS3_Fly_Hat_page_01.png` |
| 2 | 1 | `3fbf45786e9eab5bb1c7754cf1d3973d27e4c471b1918e11a36cc39dee4014c6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Stamp_Fly_v1.0_page_01.png` |
| 3 | 1 | `ea2f8747c4cca49981dfc5f2264394fe69ca1efaf2244b3c55a74ba52b8da7f0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Sch_PMW3901MB_SPI_page_01.png` |

---

源文档：`zh_CN/app/StampFly_v1.1.md`

源文档 SHA-256：`bf7610a7c9a727ef9a8c7c1c70a53a2408b07d5861ca7f837c27a6b092244f10`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
