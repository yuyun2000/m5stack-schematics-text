# StampFly 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StampFly |
| SKU | K138 |
| 产品 ID | `stampfly-156124ab77ad` |
| 源文档 | `zh_CN/app/Stamp Fly.md` |

## 概述

StampFly 通过双排连接器承载 Stamp-S3 主控模块，主板集成 INA3221AIRGVR 电流/电压监测、BMI270、BMM150、BMP280、内置 VL53L3C、两路 Grove、用户键、两颗 WS2812 和晶体管驱动蜂鸣器。四路 SI2302 低端开关分别驱动 L-Up、R-Up、L-Down、R-Down 电机接口，电机电源来自 VBAT_IN。另一块 VL53L3C 子板通过 2x4P 接口接入外部 I2C/XSHUT/GPIO1，并由 HT7533 从 VBAT 生成 3.3V。PMW3901MB-TXQT 光流子板使用 4 线 SPI，5V 经两颗 TPAP7343D LDO 分别生成 1.8V 和 3.3V/VDDIO。

## 检索关键词

`StampFly`、`K138`、`Stamp-S3`、`INA3221AIRGVR`、`INA3221 0x40`、`VL53L3CXV0DH/1`、`BMI270`、`BMM150`、`BMP280`、`PMW3901MB-TXQT`、`HT7533`、`TPAP7343D-18FS4`、`TPAP7343D-33FS4`、`WS2812`、`SI2302`、`SS8050 Y1`、`INT_SCL`、`INT_SDA`、`EXT_XSHUT`、`INT_XSHUT`、`MOSI`、`MISO`、`SCK`、`CS`、`CS2`、`L-Up`、`R-Up`、`L-Down`、`R-Down`、`GROVE_I`、`GROVE_O`、`BEEP`、`RGB`、`VBAT_IN`、`+5VOUT`、`4-Wire SPI 2MHz`

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

### StampFly 硬件架构

Stamp-S3 通过 P1/P2 双排接口连接四路电机开关、INA3221AIRGVR、BMI270、BMM150、BMP280、内置与外置 VL53L3C、PMW3901MB 光流子板、两路 Grove、蜂鸣器、用户键和 RGB LED。

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
| 系统结构 | StampFly 硬件架构 | `controller_interface=P1/P2 STAMP-S3-DIP-1.27`；`power_monitor=U1 INA3221AIRGVR`；`imu=U4 BMI270`；`magnetometer=U3 BMM150`；`barometer=U5 BMP280`；`tof=two VL53L3CXV0DH/1`；`optical_flow=U4 PMW3901MB-TXQT` |
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

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `16e1db200cad2e6afcb6076ad56bcb615543fa40673878b472fb15788e3c3768` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/StampS3_Fly_Hat_page_01.png` |
| 2 | 1 | `3fbf45786e9eab5bb1c7754cf1d3973d27e4c471b1918e11a36cc39dee4014c6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Stamp_Fly_v1.0_page_01.png` |
| 3 | 1 | `ea2f8747c4cca49981dfc5f2264394fe69ca1efaf2244b3c55a74ba52b8da7f0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Sch_PMW3901MB_SPI_page_01.png` |

---

源文档：`zh_CN/app/Stamp Fly.md`

源文档 SHA-256：`57691597cc18b3417fe2fa25535b7834fad6f2af813df6b940753ac731014791`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
