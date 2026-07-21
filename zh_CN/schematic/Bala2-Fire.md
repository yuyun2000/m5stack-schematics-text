# Bala2-Fire 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Bala2-Fire |
| SKU | K014-E |
| 产品 ID | `bala2-fire-a634eb077ea9` |
| 源文档 | `zh_CN/app/bala2fire.md` |

## 概述

Bala2-Fire 底座以 STM32F030C8T6 为控制器，通过 M5-BUS 与上层 Core 连接，并驱动双路电机、双路编码器和八路舵机。底座使用 TPS61088 生成 DRV_P060 电机电源轨，DRV8833PWP 驱动 M0/M1，SPX3819 生成 MCU_P033 逻辑电源，同时引出 SWD、Port B、Port C 和电池接口。当前原理图与产品正文对电机驱动型号、I2C 地址和 IMU 装配信息存在无法仅凭原理图消除的差异，已列入待确认事项。

## 检索关键词

`Bala2-Fire`、`BALA2`、`K014-E`、`STM32F030C8T6`、`DRV8833PWP`、`TPS61088`、`SPX3819`、`CJ3401`、`WSP4407`、`S8050`、`M5_BUS`、`SWD`、`DRV_P060`、`SVR_P037`、`MCU_P033`、`VBAT_P037`、`CORE_P050`、`CORE_SCL`、`CORE_SDA`、`MCU_SCL`、`MCU_SDA`、`IMU_SCL`、`IMU_SDA`、`DRV_M0_A`、`DRV_M0_B`、`DRV_M1_A`、`DRV_M1_B`、`M0_EA`、`M0_EB`、`M1_EA`、`M1_EB`、`SVR_MAIN1`、`SVR_OTTO1`、`PORTB`、`PORTC`、`G26 DAC`、`G36 ADC`、`G16 RXD2`、`G17 TXD2`、`0x3A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | STM32F030C8T6 | 底座控制器，连接 I2C、电机控制与编码器、八路舵机、状态 LED、复位和 SWD | 图 912c12152f1b / 第 1 页 / 第 1 页下中 MCU 区，U4 STM32F030C8T6 及 PA/PB/PF、NRST、BOOT0 网络 |
| U3 | DRV8833PWP | 双路直流电机 H 桥驱动器，连接 M0/M1 控制、输出和故障/使能网络 | 图 912c12152f1b / 第 1 页 / 第 1 页上中右 DRIVER 区，U3 明确标注 DRV8833PWP |
| U2 | TPS61088 | 将 SVR_P037 升压为 DRV_P060 的 6V BOOST 转换器 | 图 912c12152f1b / 第 1 页 / 第 1 页上中 6V BOOST 区，U2 TPS61088、L1 2.2uH、SVR_P037 和 DRV_P060 |
| U1 | SPX3819 | 从受保护的 SYS_P050 生成 MCU_P033 逻辑电源 | 图 912c12152f1b / 第 1 页 / 第 1 页左上 UVP+LDO 区，U1 SPX3819 的 VIN/EN、OUT/BYP 与 SYS_P050/MCU_P033 |
| Q2,Q4 | CJ3401 / S8050 | CORE_P050 到 SYS_P050 的欠压保护与高边开关网络 | 图 912c12152f1b / 第 1 页 / 第 1 页左上 UVP+LDO 区，Q2 CJ3401、Q4 S8050、R2/R3/R4 与 CORE_P050/SYS_P050 |
| Q1,Q3 | WSP4407 / S8050 | VBAT_P037 到 SVR_P037 的 PWR_SW 高边电源开关网络 | 图 912c12152f1b / 第 1 页 / 第 1 页左上 PWR_SW 区，Q1 WSP4407、Q3 S8050、R1/R5/R6 与 VBAT_P037/SVR_P037 |
| BUS1 | M5_BUS | 连接 Fire Core 的电源、I2C、UART、模拟/GPIO 和复位信号 | 图 912c12152f1b / 第 1 页 / 第 1 页左中 M5_BUS 区，BUS1 30 针逐针网络标注 |
| ISP1 | SWD | STM32 复位、SWCLK、SWDIO、MCU_P033 和 GND 调试接口 | 图 912c12152f1b / 第 1 页 / 第 1 页中央 ISP1 SWD，RST/CLK/DIO/VCC/GND 标注 |
| U5 | DNP | 未明确装配型号的可选 IMU 电路位，连接 IMU_SCL/IMU_SDA 和 MCU_P033 | 图 912c12152f1b / 第 1 页 / 第 1 页下中 IMU 区，U5 型号字段标为 DNP，SCL/SDA/VDD/VDDIO/A0/nCS 可见 |
| J2,J3 | ZH1.5_6PIN | M0/M1 电机和 AB 相编码器六针连接器 | 图 912c12152f1b / 第 1 页 / 第 1 页右上 MOTOR CONNECTOR 区，J2/J3 ZH1.5_6PIN 的 M+/M-/A/B/E+/E- |
| J4 | SERVO_4X | 四路 SVR_MAIN 舵机信号与 SVR_P037/GND 接口 | 图 912c12152f1b / 第 1 页 / 第 1 页右中 SERVO_MAIN 区，J4 S1-S4/VCC/GND |
| J5 | SERVO_4X | 四路 SVR_OTTO 舵机信号与 SVR_P037/GND 接口 | 图 912c12152f1b / 第 1 页 / 第 1 页右中 SERVO_OTTO 区，J5 S1-S4/VCC/GND |
| J6,J7 | GROVE | Port B 与 Port C 两组 Grove 扩展接口 | 图 912c12152f1b / 第 1 页 / 第 1 页右下 GROVE 区，J6 PORTB 与 J7 PORTC 的 IO2/IO1/5V/GND |
| J1 | 未标注 | VBAT_P037 与 GND 电池连接器 | 图 912c12152f1b / 第 1 页 / 第 1 页右下 BAT 区，J1 与 VBAT_P037/GND |
| LED1 | LED | 由 SYS_LED 网络驱动的状态指示灯 | 图 912c12152f1b / 第 1 页 / 第 1 页中央 SYS_LED/R9 1K/LED1 到 GND |

## 系统结构

### Bala2-Fire 底座系统架构

底座通过 M5_BUS 连接 Core，以 STM32F030C8T6 管理双路电机与编码器、八路舵机、I2C、Grove、状态 LED 和调试接口，并包含逻辑电源、舵机电源开关和 6V 电机升压电源。

- 参数与网络：`controller=U4 STM32F030C8T6`；`motor_driver=U3 DRV8833PWP`；`motor_channels=2`；`servo_channels=8`；`host_connector=BUS1 M5_BUS`；`debug=ISP1 SWD`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页完整原理图，UVP+LDO、PWR_SW、6V BOOST、DRIVER、MCU、MOTOR、SERVO、M5_BUS 与 GROVE 功能区

## 核心器件

### DRV8833PWP 双路电机驱动

U3 DRV8833PWP 的 AIN1/AIN2 驱动 M1 通道，BIN1/BIN2 驱动 M0 通道；AOUT1/AOUT2 连接 M1_N/M1_P，BOUT1/BOUT2 连接 M0_N/M0_P，并引出 DRV_EN 与 DRV_FLT。

- 参数与网络：`driver=U3 DRV8833PWP`；`channel_a_inputs=DRV_M1_A, DRV_M1_B`；`channel_a_outputs=M1_N, M1_P`；`channel_b_inputs=DRV_M0_A, DRV_M0_B`；`channel_b_outputs=M0_N, M0_P`；`enable=DRV_EN`；`fault=DRV_FLT`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页上中右 DRIVER 区，U3 AIN/BIN/AOUT/BOUT/nSLEEP/nFAULT 网络

## 电源

### CORE_P050 到 MCU_P033 逻辑电源

CORE_P050 经过 Q2 CJ3401 与 Q4 S8050 构成的 UVP+LDO 前级形成 SYS_P050，随后由 U1 SPX3819 输出 MCU_P033。

- 参数与网络：`input=CORE_P050`；`protected_rail=SYS_P050`；`output=MCU_P033`；`pass_device=Q2 CJ3401`；`control_transistor=Q4 S8050`；`ldo=U1 SPX3819`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页左上 UVP+LDO 区，CORE_P050、Q2/Q4、SYS_P050、U1 与 MCU_P033

### VBAT_P037 到 SVR_P037 舵机电源开关

VBAT_P037 经过 Q1 WSP4407 高边路径形成 SVR_P037，Q3 S8050 与 R1/R5/R6 构成其 PWR_SW 控制网络。

- 参数与网络：`input=VBAT_P037`；`output=SVR_P037`；`pass_device=Q1 WSP4407`；`control_transistor=Q3 S8050`；`control_bias=R1 15K, R5 4.7K, R6 15K`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页左上 PWR_SW 区，VBAT_P037、Q1/Q3、R1/R5/R6 与 SVR_P037

### SVR_P037 到 DRV_P060 6V 升压

U2 TPS61088 以 SVR_P037 为输入，通过 L1 2.2uH 和反馈/补偿网络生成标记为 DRV_P060 的 6V 电机驱动电源轨。

- 参数与网络：`converter=U2 TPS61088`；`input=SVR_P037`；`output=DRV_P060`；`output_voltage_label=6V`；`inductor=L1 2.2uH`；`feedback=R11 4.7K, R12 1.2K`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页上中 6V BOOST 区，U2、L1、SVR_P037、DRV_P060、R11/R12

### 主要电源轨负载

DRV_P060 连接 U3 的 VM，SVR_P037 连接 J4/J5 舵机 VCC，MCU_P033 连接 U4 逻辑电源与 SWD VCC，CORE_P050 连接两组 Grove 的 5V。

- 参数与网络：`DRV_P060=U3 VM`；`SVR_P037=J4/J5 VCC`；`MCU_P033=U4 power and ISP1 VCC`；`CORE_P050=J6/J7 5V`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页 DRIVER、SERVO、MCU、SWD 和 GROVE 区的同名电源网络

### 底座电池输入

J1 BAT 将电池正端引入 VBAT_P037，负端接 GND；VBAT_P037 同时连接 M5_BUS 的 BAT 网络和 PWR_SW 输入。原理图未标注电池容量。

- 参数与网络：`connector=J1`；`positive_net=VBAT_P037`；`negative_net=GND`；`bus_connection=BUS1 pin1 BAT`；`capacity_in_schematic=null`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页右下 BAT J1、左中 BUS1 pin1 与左上 PWR_SW 的 VBAT_P037

## 接口

### M0/M1 电机与编码器连接器

J2/J3 均为六针 M+/M-/A/B/E+/E- 接口；J2 使用 M0_P/M0_N、M0_EA/M0_EB，J3 使用 M1_P/M1_N、M1_EA/M1_EB，编码器 E+ 接 ENC_P050、E- 接 GND。

- 参数与网络：`J2=M0_P, M0_N, M0_EA, M0_EB, ENC_P050, GND`；`J3=M1_P, M1_N, M1_EA, M1_EB, ENC_P050, GND`；`encoder_series_resistors=R21/R22/R23/R24 1K`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页右上 MOTOR CONNECTOR 区，J2/J3 与 R21-R24

### J4 四路 SVR_MAIN 舵机接口

U4 PB4/PB5/PB8/PB9 分别生成 SVR_MAIN1/2/3/4，经 R25/R26/R27/R28 各 100Ω 接 J4 S1/S2/S3/S4；J4 VCC 为 SVR_P037，GND 接地。

- 参数与网络：`PB4=SVR_MAIN1`；`PB5=SVR_MAIN2`；`PB8=SVR_MAIN3`；`PB9=SVR_MAIN4`；`series_resistors=R25-R28 100R`；`supply=SVR_P037`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页 MCU PB4/PB5/PB8/PB9 与右中 SERVO_MAIN J4/R25-R28

### J5 四路 SVR_OTTO 舵机接口

U4 PA3/PA7/PB0/PB1 分别连接 SVR_OTTO1/2/3/4，并接到 J5 S1/S2/S3/S4；J5 VCC 为 SVR_P037，GND 接地。

- 参数与网络：`PA3=SVR_OTTO1`；`PA7=SVR_OTTO2`；`PB0=SVR_OTTO3`；`PB1=SVR_OTTO4`；`supply=SVR_P037`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页 MCU PA3/PA7/PB0/PB1 与右中 SERVO_OTTO J5

### J6 Port B Grove 映射

J6 PORTB 的 IO2=CORE_G36、IO1=CORE_G26、5V=CORE_P050、GND=GND；BUS1 同名网络将 CORE_G36 标为 G36/ADC，将 CORE_G26 标为 G26/DAC。

- 参数与网络：`connector=J6 PORTB`；`io2=CORE_G36 G36/ADC`；`io1=CORE_G26 G26/DAC`；`power=CORE_P050`；`ground=GND`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页右下 J6 PORTB 与左中 BUS1 pin23/pin21

### J7 Port C Grove 映射

J7 PORTC 的 IO2=CORE_G16、IO1=CORE_G17、5V=CORE_P050、GND=GND；BUS1 同名网络将 CORE_G16 标为 G16/RXD2，将 CORE_G17 标为 G17/TXD2。

- 参数与网络：`connector=J7 PORTC`；`io2=CORE_G16 G16/RXD2`；`io1=CORE_G17 G17/TXD2`；`power=CORE_P050`；`ground=GND`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页右下 J7 PORTC 与左中 BUS1 pin16/pin15

### M5-BUS 底座使用信号

BUS1 将 VBAT_P037、CORE_P050、CORE_SCL/G22、CORE_SDA/G21、CORE_G16/G16、CORE_G17/G17、CORE_G26/G26、CORE_G36/G36、CORE_RST 和 GND 引入底座，其余 M5-BUS 引脚按图保留。

- 参数与网络：`battery=pin1 VBAT_P037`；`five_volt=pin3 CORE_P050`；`i2c=pin13 CORE_SCL, pin14 CORE_SDA`；`uart=pin16 CORE_G16, pin15 CORE_G17`；`port_b=pin21 CORE_G26, pin27 CORE_G36`；`reset=pin25 CORE_RST`；`ground=pins 26, 28, 30`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页左中 BUS1 M5_BUS 30 针网络表

## 总线

### Core 与 STM32 的 I2C 链路

BUS1 的 CORE_SCL/G22 与 CORE_SDA/G21 经过 R17/R18 各 22Ω 串联到 MCU_SCL/MCU_SDA，分别连接 U4 PB10/PB11；R14/R15 各 4.7kΩ 上拉到 MCU_P033。

- 参数与网络：`host_scl=CORE_SCL G22`；`host_sda=CORE_SDA G21`；`mcu_scl=PB10 MCU_SCL`；`mcu_sda=PB11 MCU_SDA`；`series_resistors=R17/R18 22R`；`pullups=R14/R15 4.7K to MCU_P033`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页 M5_BUS pin13/14、MCU 下方 R14/R15/R17/R18 与 U4 PB10/PB11

## GPIO 与控制信号

### STM32 电机控制映射

U4 使用 PA8/PA9 控制 DRV_M1_A/DRV_M1_B，PA11/PA10 控制 DRV_M0_A/DRV_M0_B，并以 PF6/PF7 连接 DRV_EN/DRV_FLT。

- 参数与网络：`PA8=DRV_M1_A`；`PA9=DRV_M1_B`；`PA10=DRV_M0_B`；`PA11=DRV_M0_A`；`PF6=DRV_EN`；`PF7=DRV_FLT`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页下中 MCU 区，U4 PA8-PA11 与 PF6/PF7 右侧同名网络

### STM32 编码器输入映射

M0 编码器 B/A 相分别连接 U4 PB12/PB13，M1 编码器 B/A 相分别连接 PB14/PB15。

- 参数与网络：`PB12=M0_EB`；`PB13=M0_EA`；`PB14=M1_EB`；`PB15=M1_EA`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页下中 MCU 区，U4 PB12-PB15 对应 M0_EB/M0_EA/M1_EB/M1_EA

### STM32 状态 LED

U4 PA15 连接 SYS_LED，SYS_LED 经 R9 1kΩ 和 LED1 串联到 GND。

- 参数与网络：`mcu_pin=PA15`；`net=SYS_LED`；`resistor=R9 1K`；`indicator=LED1`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页中央 SYS_LED/R9/LED1 与 MCU 区 U4 PA15

## 复位

### STM32 复位与 BOOT0

BUS1 pin25 的 CORE_RST 经过 R16 1kΩ 连接 U4 NRST，NRST 节点由 C20 100nF 接地；U4 BOOT0 直接接 GND。

- 参数与网络：`reset_source=BUS1 pin25 CORE_RST`；`reset_pin=U4 NRST`；`series_resistor=R16 1K`；`reset_capacitor=C20 100nF`；`BOOT0=GND`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页 M5_BUS pin25 与 MCU 左下 CORE_RST/R16/C20/NRST/BOOT0

## 传感器

### 可选 U5 IMU 接口

U5 的 SCL/SDA 分别通过 IMU_SCL/IMU_SDA 连接 U4 PB6/PB7，VDD/VDDIO 接 MCU_P033，A0 接 GND；R29/R30 上拉位和 C15/C17 均标为 DNP。

- 参数与网络：`reference=U5`；`part_field=DNP`；`scl=IMU_SCL to PB6`；`sda=IMU_SDA to PB7`；`supply=MCU_P033`；`address_pin=A0 to GND`；`dnp_parts=R29, R30, C15, C17`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页下中 IMU 区 U5/R29/R30/C15/C17 与 MCU PB6/PB7

## 调试与烧录

### STM32 SWD 调试接口

ISP1 引出 CORE_RST、SWCLK、SWDIO、MCU_P033 和 GND；SWDIO/SWCLK 分别连接 U4 PA13/PA14。

- 参数与网络：`connector=ISP1`；`signals=CORE_RST, SWCLK, SWDIO, MCU_P033, GND`；`SWDIO=PA13`；`SWCLK=PA14`
- 证据：图 912c12152f1b / 第 1 页 / 第 1 页中央 ISP1 SWD 与下中 U4 PA13/SWDIO、PA14/SWCLK

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Bala2-Fire 底座系统架构 | `controller=U4 STM32F030C8T6`；`motor_driver=U3 DRV8833PWP`；`motor_channels=2`；`servo_channels=8`；`host_connector=BUS1 M5_BUS`；`debug=ISP1 SWD` |
| 电源 | CORE_P050 到 MCU_P033 逻辑电源 | `input=CORE_P050`；`protected_rail=SYS_P050`；`output=MCU_P033`；`pass_device=Q2 CJ3401`；`control_transistor=Q4 S8050`；`ldo=U1 SPX3819` |
| 电源 | VBAT_P037 到 SVR_P037 舵机电源开关 | `input=VBAT_P037`；`output=SVR_P037`；`pass_device=Q1 WSP4407`；`control_transistor=Q3 S8050`；`control_bias=R1 15K, R5 4.7K, R6 15K` |
| 电源 | SVR_P037 到 DRV_P060 6V 升压 | `converter=U2 TPS61088`；`input=SVR_P037`；`output=DRV_P060`；`output_voltage_label=6V`；`inductor=L1 2.2uH`；`feedback=R11 4.7K, R12 1.2K` |
| 电源 | 主要电源轨负载 | `DRV_P060=U3 VM`；`SVR_P037=J4/J5 VCC`；`MCU_P033=U4 power and ISP1 VCC`；`CORE_P050=J6/J7 5V` |
| 核心器件 | DRV8833PWP 双路电机驱动 | `driver=U3 DRV8833PWP`；`channel_a_inputs=DRV_M1_A, DRV_M1_B`；`channel_a_outputs=M1_N, M1_P`；`channel_b_inputs=DRV_M0_A, DRV_M0_B`；`channel_b_outputs=M0_N, M0_P`；`enable=DRV_EN`；`fault=DRV_FLT` |
| 核心器件 | 电机驱动器型号版本冲突 | `schematic_part=DRV8833PWP`；`product_document_part=HR8833`；`reference=U3` |
| 接口 | M0/M1 电机与编码器连接器 | `J2=M0_P, M0_N, M0_EA, M0_EB, ENC_P050, GND`；`J3=M1_P, M1_N, M1_EA, M1_EB, ENC_P050, GND`；`encoder_series_resistors=R21/R22/R23/R24 1K` |
| GPIO 与控制信号 | STM32 电机控制映射 | `PA8=DRV_M1_A`；`PA9=DRV_M1_B`；`PA10=DRV_M0_B`；`PA11=DRV_M0_A`；`PF6=DRV_EN`；`PF7=DRV_FLT` |
| GPIO 与控制信号 | STM32 编码器输入映射 | `PB12=M0_EB`；`PB13=M0_EA`；`PB14=M1_EB`；`PB15=M1_EA` |
| 接口 | J4 四路 SVR_MAIN 舵机接口 | `PB4=SVR_MAIN1`；`PB5=SVR_MAIN2`；`PB8=SVR_MAIN3`；`PB9=SVR_MAIN4`；`series_resistors=R25-R28 100R`；`supply=SVR_P037` |
| 接口 | J5 四路 SVR_OTTO 舵机接口 | `PA3=SVR_OTTO1`；`PA7=SVR_OTTO2`；`PB0=SVR_OTTO3`；`PB1=SVR_OTTO4`；`supply=SVR_P037` |
| 总线 | Core 与 STM32 的 I2C 链路 | `host_scl=CORE_SCL G22`；`host_sda=CORE_SDA G21`；`mcu_scl=PB10 MCU_SCL`；`mcu_sda=PB11 MCU_SDA`；`series_resistors=R17/R18 22R`；`pullups=R14/R15 4.7K to MCU_P033` |
| 总线地址 | STM32 控制器 I2C 地址 | `documented_address=0x3A`；`schematic_address_setting=null`；`controller=U4 STM32F030C8T6` |
| 调试与烧录 | STM32 SWD 调试接口 | `connector=ISP1`；`signals=CORE_RST, SWCLK, SWDIO, MCU_P033, GND`；`SWDIO=PA13`；`SWCLK=PA14` |
| 复位 | STM32 复位与 BOOT0 | `reset_source=BUS1 pin25 CORE_RST`；`reset_pin=U4 NRST`；`series_resistor=R16 1K`；`reset_capacitor=C20 100nF`；`BOOT0=GND` |
| GPIO 与控制信号 | STM32 状态 LED | `mcu_pin=PA15`；`net=SYS_LED`；`resistor=R9 1K`；`indicator=LED1` |
| 传感器 | 可选 U5 IMU 接口 | `reference=U5`；`part_field=DNP`；`scl=IMU_SCL to PB6`；`sda=IMU_SDA to PB7`；`supply=MCU_P033`；`address_pin=A0 to GND`；`dnp_parts=R29, R30, C15, C17` |
| 传感器 | U5 IMU 装配型号 | `documented_model=MPU6886`；`schematic_u5=DNP`；`population_confirmed=false` |
| 接口 | J6 Port B Grove 映射 | `connector=J6 PORTB`；`io2=CORE_G36 G36/ADC`；`io1=CORE_G26 G26/DAC`；`power=CORE_P050`；`ground=GND` |
| 接口 | J7 Port C Grove 映射 | `connector=J7 PORTC`；`io2=CORE_G16 G16/RXD2`；`io1=CORE_G17 G17/TXD2`；`power=CORE_P050`；`ground=GND` |
| 接口 | M5-BUS 底座使用信号 | `battery=pin1 VBAT_P037`；`five_volt=pin3 CORE_P050`；`i2c=pin13 CORE_SCL, pin14 CORE_SDA`；`uart=pin16 CORE_G16, pin15 CORE_G17`；`port_b=pin21 CORE_G26, pin27 CORE_G36`；`reset=pin25 CORE_RST`；`ground=pins 26, 28, 30` |
| 电源 | 底座电池输入 | `connector=J1`；`positive_net=VBAT_P037`；`negative_net=GND`；`bus_connection=BUS1 pin1 BAT`；`capacity_in_schematic=null` |

## 待确认事项

- `component.motor-driver-version-conflict`：当前原理图将 U3 标为 DRV8833PWP，而产品正文规格写为 HR8833；仅凭当前输入无法确认目标出货硬件应采用哪一型号。（证据：图 912c12152f1b / 第 1 页 / 第 1 页上中右 DRIVER 区，U3 型号字段明确为 DRV8833PWP）
- `address.controller-i2c`：产品正文给出 I2C 地址 0x3A，但当前原理图仅显示 CORE_SCL/CORE_SDA 到 STM32 的连接，没有地址设定引脚、跳线或固件常量，因此无法从原理图独立确认 0x3A。（证据：图 912c12152f1b / 第 1 页 / 第 1 页 M5_BUS/I2C 与 MCU 区，只显示 CORE_SCL/CORE_SDA、MCU_SCL/MCU_SDA 连接）
- `sensor.imu-population-model`：产品正文写有 MPU6886，但底座原理图的 U5 型号字段和相关器件标为 DNP；无法仅凭当前原理图确认 U5 是否装配及其实际型号，也无法确认正文所述 MPU6886 是否专指 Fire Core 内部器件。（证据：图 912c12152f1b / 第 1 页 / 第 1 页下中 IMU 区，U5 型号字段为 DNP，R29/R30/C15/C17 同样标 DNP）
- `review.motor-driver-model`：Bala2-Fire 当前出货硬件的 U3 应确认为 DRV8833PWP 还是产品正文中的 HR8833？；原因：当前正式原理图和产品正文的电机驱动型号不一致，需要按硬件版本或 BOM 核对。
- `review.controller-i2c-address`：产品正文给出的 STM32 I2C 地址 0x3A 是否适用于当前原理图对应的固件和硬件版本？；原因：I2C 地址由固件决定，当前原理图没有地址设定信息，无法从电路图验证 0x3A。
- `review.imu-population`：U5 是否装配、实际型号是什么，以及产品正文的 MPU6886 是否只位于 Fire Core？；原因：底座原理图将 U5 及部分外围标为 DNP，无法确认其装配状态和型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `912c12152f1b860780a4bf59d793b269e0db52cb32e4bf1a9696438d96fab8c3` | `https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_sch_01.webp` |

---

源文档：`zh_CN/app/bala2fire.md`

源文档 SHA-256：`de9a42dc2bfbba2cd75e8c1d04b7e1b082cd5ef191b5a874fa19c1858f6dc584`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
