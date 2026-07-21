# Bala2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Bala2 |
| SKU | K014-C |
| 产品 ID | `bala2-73d3062b8111` |
| 源文档 | `zh_CN/app/bala2.md` |

## 概述

Bala2 底座以 STM32F030C8T6（U4）为控制器，通过 MCU_SCL/MCU_SDA 与 M5-BUS 主机通信，并控制 DRV8833PWP（U3）双电机驱动、两组编码器和八路舵机信号。电池 VBAT_P037 经 PWR_SW 开关路径形成 SVR_P037，TPS61088（U2）再生成 DRV_P060 约 6V 电机驱动电源；CORE_P050 另经欠压/开关与 SPX3819（U1）生成 MCU_P033。两只电机连接器同时引出电机和编码器，PORTB/PORTC 直接转接 M5-BUS GPIO 与 5V。

## 检索关键词

`Bala2`、`K014-C`、`STM32F030C8T6`、`DRV8833PWP`、`TPS61088`、`SPX3819`、`M5_BUS`、`MCU_SCL`、`MCU_SDA`、`CORE_SCL`、`CORE_SDA`、`DRV_P060`、`SVR_P037`、`MCU_P033`、`CORE_P050`、`M0_P`、`M0_N`、`M1_P`、`M1_N`、`M0_EA`、`M0_EB`、`M1_EA`、`M1_EB`、`SERVO_MAIN`、`SERVO_OTTO`、`PORTB`、`PORTC`、`SWDIO`、`SWCLK`、`0x3A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | STM32F030C8T6 | 底座主控，管理电机、编码器、舵机、I2C 和状态 LED | 图 912c12152f1b / 第 1 页 / MCU 区域 U4：STM32F030C8T6，PA/PB/PF、SWD、MCU_SCL/SDA、电机/舵机网络 |
| U3 | DRV8833PWP | 双路 H 桥电机驱动器，输出 M0_P/N 与 M1_P/N | 图 912c12152f1b / 第 1 页 / DRIVER 区域 U3：DRV8833PWP，AIN1/2、BIN1/2、AOUT1/2、BOUT1/2、nSLEEP/nFAULT、VM/VINT |
| U2 | TPS61088 | SVR_P037 到 DRV_P060 的 6V 升压转换器 | 图 912c12152f1b / 第 1 页 / 6V BOOST 区域 U2：TPS61088，L1 2.2uH、SW/VOUT/FB/EN/ILIM/MODE/COMP 与 DRV_P060 |
| U1 | SPX3819 | SYS_P050 到 MCU_P033 的低压差稳压器 | 图 912c12152f1b / 第 1 页 / UVP+LDO 区域 U1：SPX3819，IN/EN/OUT/BYP/GND，输入 SYS_P050、输出 MCU_P033 |
| Q1/Q3 | WSP4407 / S8050 | VBAT_P037 到 SVR_P037 的电源开关控制路径 | 图 912c12152f1b / 第 1 页 / PWR_SW 区域：VBAT_P037-Q1(WSP4407)-SVR_P037，Q3 S8050 与 MCU_P033/R5/R6 控制 |
| Q2/Q4 | CJ3401 / S8050 | CORE_P050 欠压/开关控制并向 SYS_P050 供电 | 图 912c12152f1b / 第 1 页 / UVP+LDO 区域：CORE_P050-Q2(CJ3401)-SYS_P050，Q4 S8050 与 R2/R3/R4 控制 |
| BUS1 | M5_BUS | M5 主机与底座的 30 Pin 电源、I2C、UART、GPIO 总线 | 图 912c12152f1b / 第 1 页 / M5_BUS 区域 BUS1：1~30 脚的 BAT/5V/HPWR/GPIO/I2C/UART/3.3V/GND 标注 |
| J2 | ZH1.5_6PIN | M0 电机与编码器连接器 | 图 912c12152f1b / 第 1 页 / MOTOR CONNECTOR 区域 J2：M0_P/M0_N、M0_EA/M0_EB、ENC_P050/GND 到 M+/M-/A/B/E+/E- |
| J3 | ZH1.5_6PIN | M1 电机与编码器连接器 | 图 912c12152f1b / 第 1 页 / MOTOR CONNECTOR 区域 J3：M1_P/M1_N、M1_EA/M1_EB、ENC_P050/GND 到 M+/M-/A/B/E+/E- |
| J4 | SERVO_4X | 四路外部主舵机接口，提供 SVR_MAIN1~4、SVR_P037 和 GND | 图 912c12152f1b / 第 1 页 / SERVO_MAIN 区域 J4：S1~S4、VCC、GND 与 SVR_MAIN1~4、R25~R28 100R、SVR_P037 |
| J5 | SERVO_4X | 四路内部 OTTO 舵机接口，提供 SVR_OTTO1~4、SVR_P037 和 GND | 图 912c12152f1b / 第 1 页 / SERVO_OTTO 区域 J5：S1~S4、VCC、GND 与 SVR_OTTO1~4、SVR_P037 |
| J6 | GROVE PORTB | PORTB GPIO/ADC/DAC 与 5V 接口 | 图 912c12152f1b / 第 1 页 / GROVE 区域 J6 PORTB：IO2 CORE_G36、IO1 CORE_G26、5V CORE_P050、GND |
| J7 | GROVE PORTC | PORTC UART 与 5V 接口 | 图 912c12152f1b / 第 1 页 / GROVE 区域 J7 PORTC：IO2 CORE_G16、IO1 CORE_G17、5V CORE_P050、GND |
| ISP1 | SWD | STM32 调试接口，引出 RST、CLK、DIO、VCC、GND | 图 912c12152f1b / 第 1 页 / MCU 左侧 ISP1 SWD：CORE_RST/SWCLK/SWDIO/MCU_P033/GND |
| U5 | DNP | 未装配的可选 IMU 器件位，SCL/SDA 与去耦同样标 DNP | 图 912c12152f1b / 第 1 页 / IMU 区域 U5：器件上方 DNP，R29/R30 与 C15/C17 亦标 DNP |
| LED1/R9 | LED / 1KΩ | 由 SYS_LED 网络控制的系统状态指示灯 | 图 912c12152f1b / 第 1 页 / M5_BUS 与 SWD 之间：SYS_LED-R9 1KΩ-LED1-GND |

## 系统结构

### Bala2 底座

U4 STM32F030C8T6 通过 M5_BUS 与主机连接，控制 U3 DRV8833PWP、两组电机编码器、八路舵机和状态 LED；底座电源由电池开关、6V 升压和 MCU 3.3V LDO 分区组成。

- 参数与网络：`mcu=U4 STM32F030C8T6`；`motor_driver=U3 DRV8833PWP`；`host_bus=BUS1 M5_BUS`；`motor_connectors=J2,J3`；`servos=J4,J5`；`power=U2 TPS61088,U1 SPX3819`
- 证据：图 912c12152f1b / 第 1 页 / 整页 U4/U3/U2/U1/BUS1/J2~J7 功能块及同名网络

## 电源

### VBAT_P037 到 SVR_P037

VBAT_P037 经 Q1 WSP4407 形成 SVR_P037；Q3 S8050 的控制网络连接 MCU_P033，并配 R1/R5/R6 与 C2/C4。

- 参数与网络：`input=VBAT_P037`；`switch=Q1 WSP4407`；`control=Q3 S8050,MCU_P033`；`output=SVR_P037`
- 证据：图 912c12152f1b / 第 1 页 / PWR_SW 区域 VBAT_P037-Q1-SVR_P037 与 Q3/MCU_P033 控制支路

### U2 TPS61088

U2 以 SVR_P037 为 VIN，经 L1 2.2uH 和开关网络输出 DRV_P060；反馈使用 R11 4.7KΩ、R12 1.2KΩ，ILIM/MODE/COMP 使用 R13/C9/C10 等外围。

- 参数与网络：`input=SVR_P037`；`inductor=L1 2.2uH`；`output=DRV_P060`；`feedback=R11 4.7KΩ,R12 1.2KΩ`；`controller=TPS61088`
- 证据：图 912c12152f1b / 第 1 页 / 6V BOOST 区域 U2、L1、DRV_P060、R11/R12/R13/C9/C10

### U1 SPX3819

CORE_P050 经 Q2/Q4 欠压开关形成 SYS_P050，U1 SPX3819 再从 SYS_P050 输出 MCU_P033。

- 参数与网络：`source=CORE_P050`；`uv_switch=Q2 CJ3401,Q4 S8050`；`intermediate=SYS_P050`；`ldo=U1 SPX3819`；`output=MCU_P033`
- 证据：图 912c12152f1b / 第 1 页 / UVP+LDO 区域 CORE_P050-Q2/Q4-SYS_P050-U1-MCU_P033

## 接口

### J2 M0

J2 的 M+/M- 接 M0_P/M0_N，A/B 经 R21/R22 1KΩ 接 M0_EA/M0_EB，E+ 接 ENC_P050，E- 和 SHELL 接 GND。

- 参数与网络：`motor_positive=M0_P`；`motor_negative=M0_N`；`encoder_A=M0_EA via R21 1KΩ`；`encoder_B=M0_EB via R22 1KΩ`；`encoder_supply=ENC_P050`；`encoder_return=GND`
- 证据：图 912c12152f1b / 第 1 页 / MOTOR CONNECTOR 区域 J2 M0：M+/M-/A/B/E+/E-/SHELL 与左侧网络

### J3 M1

J3 的 M+/M- 接 M1_P/M1_N，A/B 经 R23/R24 1KΩ 接 M1_EA/M1_EB，E+ 接 ENC_P050，E- 和 SHELL 接 GND。

- 参数与网络：`motor_positive=M1_P`；`motor_negative=M1_N`；`encoder_A=M1_EA via R23 1KΩ`；`encoder_B=M1_EB via R24 1KΩ`；`encoder_supply=ENC_P050`；`encoder_return=GND`
- 证据：图 912c12152f1b / 第 1 页 / MOTOR CONNECTOR 区域 J3 M1：M+/M-/A/B/E+/E-/SHELL 与左侧网络

### J6 PORTB

J6 的 IO2 接 CORE_G36，IO1 接 CORE_G26，5V 接 CORE_P050，GND 接地。

- 参数与网络：`IO2=CORE_G36`；`IO1=CORE_G26`；`5V=CORE_P050`；`GND=GND`
- 证据：图 912c12152f1b / 第 1 页 / GROVE 区域 J6 PORTB：4/3/2/1 脚与 CORE_G36/CORE_G26/CORE_P050/GND

### J7 PORTC

J7 的 IO2 接 CORE_G16，IO1 接 CORE_G17，5V 接 CORE_P050，GND 接地。

- 参数与网络：`IO2=CORE_G16`；`IO1=CORE_G17`；`5V=CORE_P050`；`GND=GND`
- 证据：图 912c12152f1b / 第 1 页 / GROVE 区域 J7 PORTC：4/3/2/1 脚与 CORE_G16/CORE_G17/CORE_P050/GND

## 总线

### CORE_SCL/SDA 到 MCU_SCL/SDA

BUS1 的 CORE_SCL 和 CORE_SDA 分别经 R17、R18 22Ω 串联到 MCU_SCL、MCU_SDA；R14、R15 4.7KΩ 将主机侧信号上拉到 MCU_P033，U4 PB10/PB11 接 MCU_SCL/MCU_SDA。

- 参数与网络：`scl=CORE_SCL-R17 22Ω-MCU_SCL-U4 PB10`；`sda=CORE_SDA-R18 22Ω-MCU_SDA-U4 PB11`；`pullups=R14/R15 4.7KΩ to MCU_P033`
- 证据：图 912c12152f1b / 第 1 页 / MCU 区域 U4 下方 R14/R15/R17/R18 与 BUS1 CORE_SCL/SDA、U4 PB10/PB11

### U4 到 U3 电机控制

U4 PA8/PA9 连接 DRV_M1_A/DRV_M1_B，PA11/PA10 连接 DRV_M0_A/DRV_M0_B；PF6/PF7 分别连接 DRV_EN/DRV_FLT。

- 参数与网络：`motor_1=PA8 DRV_M1_A,PA9 DRV_M1_B`；`motor_0=PA11 DRV_M0_A,PA10 DRV_M0_B`；`enable=PF6 DRV_EN`；`fault=PF7 DRV_FLT`
- 证据：图 912c12152f1b / 第 1 页 / MCU 区域 U4 左侧 PA8~PA11/PF6/PF7 与 DRIVER 区域 U3 AIN/BIN/nSLEEP/nFAULT

## GPIO 与控制信号

### M0/M1 编码器到 U4

U4 PB13/PB12 接 M0_EA/M0_EB，PB15/PB14 接 M1_EA/M1_EB。

- 参数与网络：`M0_EA=U4 PB13`；`M0_EB=U4 PB12`；`M1_EA=U4 PB15`；`M1_EB=U4 PB14`
- 证据：图 912c12152f1b / 第 1 页 / MCU 区域 U4 右侧 PB12~PB15 与 MOTOR CONNECTOR 同名 M0/M1_EA/EB 网络

### J4 SERVO_MAIN

U4 PB4/PB5/PB8/PB9 连接 SVR_MAIN1/2/3/4，分别经 R25/R26/R27/R28 100R 到 J4 S1/S2/S3/S4；J4 VCC 接 SVR_P037，GND 接地。

- 参数与网络：`S1=U4 PB4 SVR_MAIN1 via R25 100R`；`S2=U4 PB5 SVR_MAIN2 via R26 100R`；`S3=U4 PB8 SVR_MAIN3 via R27 100R`；`S4=U4 PB9 SVR_MAIN4 via R28 100R`；`power=SVR_P037`
- 证据：图 912c12152f1b / 第 1 页 / MCU U4 PB4/PB5/PB8/PB9 与 SERVO_MAIN J4/R25~R28/SVR_P037

### J5 SERVO_OTTO

U4 PA3、PA7、PB0、PB1 分别连接 SVR_OTTO1/2/3/4，并直接到 J5 S1/S2/S3/S4；J5 VCC 接 SVR_P037，GND 接地。

- 参数与网络：`S1=U4 PA3 SVR_OTTO1`；`S2=U4 PA7 SVR_OTTO2`；`S3=U4 PB0 SVR_OTTO3`；`S4=U4 PB1 SVR_OTTO4`；`power=SVR_P037`
- 证据：图 912c12152f1b / 第 1 页 / MCU U4 PA3/PA7/PB0/PB1 与 SERVO_OTTO J5/SVR_OTTO1~4/SVR_P037

### LED1

U4 PA15 连接 SYS_LED，SYS_LED 经 R9 1KΩ 和 LED1 接 GND。

- 参数与网络：`mcu_pin=U4 PA15`；`network=SYS_LED`；`resistor=R9 1KΩ`；`indicator=LED1`
- 证据：图 912c12152f1b / 第 1 页 / MCU U4 PA15 SYS_LED 与页面中央 SYS_LED-R9-LED1-GND 支路

## 传感器

### U5 可选 IMU

U5 器件位标注 DNP，其 SCL/SDA 串联位 R29/R30 与去耦 C15/C17 也标注 DNP，因此该页定义的 U5 IMU 支路不装配。

- 参数与网络：`device=U5 DNP`；`i2c_links=R29/R30 DNP`；`decoupling=C15/C17 DNP`；`bus=IMU_SCL,IMU_SDA`
- 证据：图 912c12152f1b / 第 1 页 / IMU 区域 U5 上方 DNP、R29/R30 DNP、C15/C17 DNP 标注

## 调试与烧录

### ISP1 SWD

ISP1 的 RST 接 CORE_RST/U4 NRST，CLK 接 SWCLK/U4 PA14，DIO 接 SWDIO/U4 PA13，VCC 接 MCU_P033，GND 接地。

- 参数与网络：`RST=CORE_RST U4 NRST`；`CLK=SWCLK U4 PA14`；`DIO=SWDIO U4 PA13`；`VCC=MCU_P033`；`GND=GND`
- 证据：图 912c12152f1b / 第 1 页 / MCU 左侧 ISP1 SWD 与 U4 NRST/PA13/PA14、MCU_P033/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Bala2 底座 | `mcu=U4 STM32F030C8T6`；`motor_driver=U3 DRV8833PWP`；`host_bus=BUS1 M5_BUS`；`motor_connectors=J2,J3`；`servos=J4,J5`；`power=U2 TPS61088,U1 SPX3819` |
| 电源 | VBAT_P037 到 SVR_P037 | `input=VBAT_P037`；`switch=Q1 WSP4407`；`control=Q3 S8050,MCU_P033`；`output=SVR_P037` |
| 电源 | U2 TPS61088 | `input=SVR_P037`；`inductor=L1 2.2uH`；`output=DRV_P060`；`feedback=R11 4.7KΩ,R12 1.2KΩ`；`controller=TPS61088` |
| 电源 | U1 SPX3819 | `source=CORE_P050`；`uv_switch=Q2 CJ3401,Q4 S8050`；`intermediate=SYS_P050`；`ldo=U1 SPX3819`；`output=MCU_P033` |
| 总线 | CORE_SCL/SDA 到 MCU_SCL/SDA | `scl=CORE_SCL-R17 22Ω-MCU_SCL-U4 PB10`；`sda=CORE_SDA-R18 22Ω-MCU_SDA-U4 PB11`；`pullups=R14/R15 4.7KΩ to MCU_P033` |
| 总线地址 | Bala2 底座 STM32 I2C 地址 | `documented_address=0x3A`；`schematic_address_label=null`；`address_source=firmware-controlled` |
| 总线 | U4 到 U3 电机控制 | `motor_1=PA8 DRV_M1_A,PA9 DRV_M1_B`；`motor_0=PA11 DRV_M0_A,PA10 DRV_M0_B`；`enable=PF6 DRV_EN`；`fault=PF7 DRV_FLT` |
| 接口 | J2 M0 | `motor_positive=M0_P`；`motor_negative=M0_N`；`encoder_A=M0_EA via R21 1KΩ`；`encoder_B=M0_EB via R22 1KΩ`；`encoder_supply=ENC_P050`；`encoder_return=GND` |
| 接口 | J3 M1 | `motor_positive=M1_P`；`motor_negative=M1_N`；`encoder_A=M1_EA via R23 1KΩ`；`encoder_B=M1_EB via R24 1KΩ`；`encoder_supply=ENC_P050`；`encoder_return=GND` |
| GPIO 与控制信号 | M0/M1 编码器到 U4 | `M0_EA=U4 PB13`；`M0_EB=U4 PB12`；`M1_EA=U4 PB15`；`M1_EB=U4 PB14` |
| GPIO 与控制信号 | J4 SERVO_MAIN | `S1=U4 PB4 SVR_MAIN1 via R25 100R`；`S2=U4 PB5 SVR_MAIN2 via R26 100R`；`S3=U4 PB8 SVR_MAIN3 via R27 100R`；`S4=U4 PB9 SVR_MAIN4 via R28 100R`；`power=SVR_P037` |
| GPIO 与控制信号 | J5 SERVO_OTTO | `S1=U4 PA3 SVR_OTTO1`；`S2=U4 PA7 SVR_OTTO2`；`S3=U4 PB0 SVR_OTTO3`；`S4=U4 PB1 SVR_OTTO4`；`power=SVR_P037` |
| 接口 | J6 PORTB | `IO2=CORE_G36`；`IO1=CORE_G26`；`5V=CORE_P050`；`GND=GND` |
| 接口 | J7 PORTC | `IO2=CORE_G16`；`IO1=CORE_G17`；`5V=CORE_P050`；`GND=GND` |
| 调试与烧录 | ISP1 SWD | `RST=CORE_RST U4 NRST`；`CLK=SWCLK U4 PA14`；`DIO=SWDIO U4 PA13`；`VCC=MCU_P033`；`GND=GND` |
| 传感器 | U5 可选 IMU | `device=U5 DNP`；`i2c_links=R29/R30 DNP`；`decoupling=C15/C17 DNP`；`bus=IMU_SCL,IMU_SDA` |
| GPIO 与控制信号 | LED1 | `mcu_pin=U4 PA15`；`network=SYS_LED`；`resistor=R9 1KΩ`；`indicator=LED1` |

## 待确认事项

- `address.stm32-i2c`：原理图显示 STM32 通过 MCU_SCL/MCU_SDA 通信，但页面没有地址值或硬件地址绑定位，因此仅凭此页无法确认 0x3A。（证据：图 912c12152f1b / 第 1 页 / MCU/M5_BUS 区域 U4 PB10/PB11 与 CORE_SCL/SDA；整页无 0x3A 或地址选择标注）
- `review.stm32-i2c-address`：请用 Bala2 STM32 固件或主机通信协议确认底座 I2C 地址是否固定为 0x3A。；原因：STM32 的从机地址由固件决定，原理图只显示 SCL/SDA 物理网络，无法证明 0x3A。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `912c12152f1b860780a4bf59d793b269e0db52cb32e4bf1a9696438d96fab8c3` | `https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_sch_01.webp` |

---

源文档：`zh_CN/app/bala2.md`

源文档 SHA-256：`e88d07caa0ebce9c984eb7baabc6dd5eb0dea3336dfd92ac931677829ead8867`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
