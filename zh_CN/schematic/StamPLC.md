# StamPLC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StamPLC |
| SKU | K141 |
| 产品 ID | `stamplc-0cdf00b2da3a` |
| 源文档 | `zh_CN/core/StamPLC.md` |

## 概述

StamPLC 由 CPU 板与 IO 板组成，以 STAMP_S3 模组为控制核心，通过 I2C、SPI、CAN、RS-485 和扩展总线连接显示、microSD、RTC、传感器与工业接口。IO 板将 SYS_VIN 经 MP4560DN 转换为 SYS_5V，并提供 8 路 EL3H4 光耦输入、4 路 AW9523B/ULN2003A 驱动的继电器输出、SIT1044 CAN 和 INA226/LM75 监测。CPU 板还集成 PI4IOE5V6408、LCD、三按键、RGB、蜂鸣器、PWR-485 与两个 HY2.0-4P 接口。

## 检索关键词

`StamPLC`、`K141`、`STAMP_S3`、`MP4560DN`、`SIT3088EEUA`、`SIT1044QTK/3`、`AW9523B`、`0x59`、`PI4IOE5V6408`、`INA226AIDGSR`、`LM75BDP`、`RX8130CE`、`EL3H4`、`ULN2003A`、`HF3FF/005-1ZTF`、`LPW5209AB5F`、`SE8533K1-HF`、`SYS_VIN`、`SYS_HV`、`PMU_5V`、`SYS_5V`、`SYS_3.3V`、`MCU_5V`、`MCU_3.3V`、`EXT_5V`、`G15_SYS_SCL`、`G13_SYS_SDA`、`G14_SYS_INT`、`G42_CAN_TX`、`G43_CAN_RX`、`G46_RS485_DIR`、`G0_RS485_TX/BOOT`、`G39_RS485_RX`、`microSD`、`G7_SPI_SCK`、`G8_SPI_MOSI`、`G9_SPI_MISO`、`G10_SPI_CS_CARD`、`PWR-CAN`、`PWR-485`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| STAMP_S3 | STAMP_S3 | 主控模组，连接工业总线、I2C、SPI、LCD、UART、蜂鸣器和扩展 GPIO | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 A2-B2：STAMP_S3 pins1-28 |
| U2 (CPU) | SIT3088EEUA | RS-485 收发器 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 B1-B2：U2 SIT3088EEUA |
| U3 (CPU) | SE8533K1-HF | SYS_5V 到 SYS_3.3V 的 LDO | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 B1：U3 SE8533K1-HF |
| U4 (CPU) | LPW5209AB5F | SYS_5V 到 EXT_5V 的负载开关 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 B3：U4 LPW5209AB5F |
| U5 (CPU) | PI4IOE5V6408 | 按键、RGB 与 LCD 背光的 I2C GPIO 扩展器 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 C3：U5 PI4IOE5V6408 |
| U6 (CPU) | LCD | SPI 彩色显示模块 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 A4：U6 LCD pins1-10 |
| J5 (CPU) | TF | SPI microSD 卡座 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 B4：J5 TF |
| U7 (CPU) | RX8130CE | I2C 实时时钟及后备电池接口 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 D3-D4：U7 RX8130CE/B1 |
| BZ1 | HYG8503-8WS | G44_BUZZER_PWM 控制的蜂鸣器 | 图 0138054fc63d / 第 1 页 / CPU板第1页网格 C3：BZ1/Q3/R29/D3 |
| U1 (IO) | MP4560DN | SYS_VIN 到 PMU_5V/SYS_5V 的宽压降压转换器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 A1-A2：U1 MP4560DN |
| U2 (IO) | SIT1044QTK/3 | CAN 总线收发器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 B1-B2：U2 SIT1044QTK/3 |
| U4 (IO) | AW9523B | 8 路光耦输入采样和 4 路继电器控制的 I2C 扩展器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 A3-B3：U4 AW9523B，Address:0X59 |
| U5 (IO) | ULN2003A | SYS_OUT1-SYS_OUT4 到继电器线圈的低侧驱动器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 B3：U5 ULN2003A |
| U6 (IO) | LM75BDP,118 | I2C 板内温度传感器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 C2：U6 LM75BDP,118 |
| U7 (IO) | INA226AIDGSR | SYS_VIN 电压与分流路径监测器 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 D1-D2：U7 INA226AIDGSR |
| PC1-PC8 | EL3H4 | EXCON_IN1-EXCON_IN8 的 8 路隔离输入光耦 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 A2-D3：PC1-PC8 EL3H4 |
| RLY1-RLY4 | HF3FF/005-1ZTF | 四路 SYS_5V 线圈继电器输出 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 A4-C4：RLY1-RLY4 |
| J1 (IO) | DC-0440-2.5A-2.0 | SYS_VIN 直流电源输入插座 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 C1：J1 DC-0440-2.5A-2.0/FU4 |
| J2 (IO) | XT30(2+2)PW-M | 带 SYS_VIN/GND 的 PWR-CAN 接口 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 C1：J2 XT30(2+2)PW-M |
| J10-J13 | KF128_5.0mm_3P | 四组继电器公共端/常开/常闭输出端子 | 图 a47ec05d0497 / 第 1 页 / IO板第1页网格 A4-C4：J10-J13 |

## 系统结构

### StamPLC 双板架构

CPU 板以 STAMP_S3 为主控并承载 RS-485、LCD、microSD、RTC、按键/RGB/蜂鸣器；IO 板承载宽压电源、CAN、INA226、LM75、8 路光耦输入和 4 路继电器输出，两板通过 J3/J8 2x10 总线连接。

- 参数与网络：`cpu_asset=K141_sch_StamPLC_V10_CPU`；`io_asset=K141_sch_StamPLC_V10_IO`；`controller=STAMP_S3`；`interboard=CPU J3 <-> IO J8 2x10`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页完整单页; 图 a47ec05d0497 / 第 1 页 / IO板第1页完整单页

## 电源

### SYS_VIN 到 SYS_5V

J1 直流插座经 FU4 2.5A/36V 自恢复保险丝进入 SYS_VIN；SYS_VIN 经 FU1 1.5A/60V、U1 MP4560DN、L1 10uH 和反馈网络生成 PMU_5V，再经 FU5 2A/12V 形成 SYS_5V。

- 参数与网络：`input=J1 DC-0440-2.5A-2.0`；`input_fuse=FU4 2.5A/36V`；`rail=SYS_VIN`；`converter=U1 MP4560DN`；`inductor=L1 10uH/4.5A_0650`；`intermediate=PMU_5V`；`output_fuse=FU5 2A/12V`；`output=SYS_5V`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 A1-A2/C1：J1/FU4/FU1/U1/L1/FU5

### SYS_5V 到 SYS_3.3V

CPU 板 U3 SE8533K1-HF 的 VIN 接 SYS_5V，OUT 输出 SYS_3.3V，C3/C4 均为 22uF/16V。

- 参数与网络：`ldo=U3 SE8533K1-HF`；`input=SYS_5V`；`output=SYS_3.3V`；`input_cap=C3 22uF/16V`；`output_cap=C4 22uF/16V`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 B1：U3/C3/C4

### MCU_5V 与 EXT_5V 分配

CPU 板 SYS_5V 经 FU3 0.5A 自恢复保险丝形成 MCU_5V；U4 LPW5209AB5F 由 SYS_5V 输入并输出 EXT_5V，J6/J7 使用 EXT_5V。

- 参数与网络：`mcu_path=SYS_5V -> FU3 0.5A -> MCU_5V`；`load_switch=U4 LPW5209AB5F`；`switch_input=SYS_5V`；`switch_output=EXT_5V`；`loads=J6,J7`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 B3/C1/C4：FU3/U4/J6/J7

## 接口

### SPI LCD 与背光

U6 LCD 的 SCK/MOSI/RS/CS/RESET 分别接 GPIO7/GPIO8/GPIO6/GPIO12/GPIO3；Q2 SI2301 控制 LEDA，栅极由 EIO_LCD_BL 经 R24 100Ω驱动。

- 参数与网络：`sck=G7_SPI_SCK`；`mosi=G8_SPI_MOSI`；`rs=G6_LCD_RS`；`cs=G12_SPI_CS_LCD`；`reset=G3_PHY_RST`；`backlight=EIO_LCD_BL -> R24 100Ω -> Q2 SI2301 -> LEDA`；`supply=SYS_3.3V`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 A4：U6/Q2/R19/R24/C11

### 隔离输入端子

J3 提供 EXCON_COM，J4/J5/J6/J7 分别提供 EXCON_IN1-2、IN3-4、IN5-6、IN7-8。

- 参数与网络：`common=J3 pin1 EXCON_COM; pins2/3 GND`；`inputs12=J4 EXCON_IN1/IN2`；`inputs34=J5 EXCON_IN3/IN4`；`inputs56=J6 EXCON_IN5/IN6`；`inputs78=J7 EXCON_IN7/IN8`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 C1-D1：J3-J7 KF128 terminals

### 四路继电器输出

SYS_OUT1-SYS_OUT4 进入 U5 ULN2003A，形成 RLY_DRV1-RLY_DRV4 驱动 RLY1-RLY4 的 SYS_5V 线圈；J10-J13 各提供一组 3 针转换触点。

- 参数与网络：`driver=U5 ULN2003A`；`inputs=SYS_OUT1-SYS_OUT4`；`coil_drives=RLY_DRV1-RLY_DRV4`；`relays=RLY1-RLY4 HF3FF/005-1ZTF`；`connectors=J10-J13 KF128_5.0mm_3P`；`coil_supply=SYS_5V`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 A3-C4：U5/RLY1-RLY4/J10-J13

### HY2.0-4P 与扩展口

CPU 板 J6 pins1-4 为 GND、EXT_5V、EXT_G2、EXT_G1，J7 pins1-4 为 GND、EXT_5V、EXT_G5、EXT_G4；D2 SMF15C 对 EXT_G1/G2/G4/G5 提供钳位。

- 参数与网络：`J6=pin1 GND; pin2 EXT_5V; pin3 EXT_G2; pin4 EXT_G1`；`J7=pin1 GND; pin2 EXT_5V; pin3 EXT_G5; pin4 EXT_G4`；`series=R20-R23 10Ω/1%`；`tvs=D2 SMF15C`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 C4：J6/J7/R20-R23/D2

### CPU/IO 板互连总线

CPU J3 与 IO J8 的 2x10 接口传递 SYS_HV、SYS_5V、SYS_3.3V、GND、G3/G7/G8/G9/G11/G13/G14/G15/G40/G41/G42/G43 等电源与控制网络。

- 参数与网络：`connectors=CPU J3; IO J8`；`pins=1-20`；`power=SYS_HV,SYS_5V,SYS_3.3V,GND`；`signals=G3_PHY_RST,G7_SPI_SCK,G8_SPI_MOSI,G9_SPI_MISO,G11_SPI_CS_EXT,G13_SYS_SDA,G14_SYS_INT,G15_SYS_SCL,EXT_G40,EXT_G41,G42_CAN_TX,G43_CAN_RX`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 C2：J3 2x10; 图 a47ec05d0497 / 第 1 页 / IO板第1页 C2：J8 2x10

## 总线

### 系统 I2C 与中断/复位

STAMP_S3 G15_SYS_SCL 与 G13_SYS_SDA 连接 PI4IOE5V6408、RX8130CE、AW9523B、LM75BDP 和 INA226；G14_SYS_INT 连接相关中断，G3_PHY_RST 连接扩展器复位。

- 参数与网络：`controller=STAMP_S3`；`scl=GPIO15 / G15_SYS_SCL`；`sda=GPIO13 / G13_SYS_SDA`；`interrupt=GPIO14 / G14_SYS_INT`；`reset=GPIO3 / G3_PHY_RST`；`devices=PI4IOE5V6408,RX8130CE,AW9523B,LM75BDP,INA226`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 STAMP_S3/U5/U7 I2C nets; 图 a47ec05d0497 / 第 1 页 / IO板第1页 U4/U6/U7 I2C nets

### LCD、microSD 与扩展 SPI

STAMP_S3 GPIO7 为 G7_SPI_SCK，GPIO8 为 G8_SPI_MOSI，GPIO9 为 G9_SPI_MISO；GPIO10/G12/G11 分别为 microSD、LCD、扩展设备片选。

- 参数与网络：`controller=STAMP_S3`；`sck=GPIO7 / G7_SPI_SCK`；`mosi=GPIO8 / G8_SPI_MOSI`；`miso=GPIO9 / G9_SPI_MISO`；`sd_cs=GPIO10 / G10_SPI_CS_CARD`；`lcd_cs=GPIO12 / G12_SPI_CS_LCD`；`ext_cs=GPIO11 / G11_SPI_CS_EXT`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 STAMP_S3 GPIO7-12、U6 LCD、J5 TF

### PWR-485 接口

U2 SIT3088EEUA 的 RO 经 R7 5.1KΩ连接 GPIO39/G39_RS485_RX，DI 经 R9 1KΩ连接 GPIO0/G0_RS485_TX/BOOT，RE/DE 由 GPIO46/G46_RS485_DIR 控制；A/B 到 J1 EXT_485_A/B。

- 参数与网络：`transceiver=U2 SIT3088EEUA`；`rx=RO -> R7 5.1KΩ -> GPIO39`；`tx=GPIO0 -> R9 1KΩ -> DI`；`direction=GPIO46 -> RE/DE`；`a=EXT_485_A -> J1 pin3`；`b=EXT_485_B -> J1 pin4`；`power=J1 pin2 SYS_HV; pin1 GND`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 A1-B2：J1/U2/R7/R9

### PWR-CAN 接口

U2 SIT1044QTK/3 的 TXD 经 R11 100Ω连接 GPIO42/G42_CAN_TX，RXD 经 R12 100Ω连接 GPIO43/G43_CAN_RX；CANH/CANL 连接 J2 EXCON_CANH/EXCON_CANL。

- 参数与网络：`transceiver=U2 SIT1044QTK/3`；`tx=GPIO42 -> R11 100Ω -> TXD`；`rx=RXD -> R12 100Ω -> GPIO43`；`canh=EXCON_CANH -> J2 pin3`；`canl=EXCON_CANL -> J2 pin4`；`power=J2 pin1 SYS_VIN; pin2 GND`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 B1-C1：U2/J2/R11/R12

## 总线地址

### AW9523B I2C 地址

IO 板在 U4 AW9523B 下方明确打印 Address: 0X59。

- 参数与网络：`device=U4 AW9523B`；`address=0x59`；`bus=G15_SYS_SCL/G13_SYS_SDA`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 B3：U4 下方 Address: 0X59

## GPIO 与控制信号

### PI4IOE5V6408 端口映射

U5 P0/P1/P2 连接 EIO_KEY3/EIO_KEY2/EIO_KEY1，P4/P5/P6 连接 EIO_LEDB/EIO_LEDG/EIO_LEDR，P7 连接 EIO_LCD_BL。

- 参数与网络：`P0=EIO_KEY3`；`P1=EIO_KEY2`；`P2=EIO_KEY1`；`P4=EIO_LEDB`；`P5=EIO_LEDG`；`P6=EIO_LEDR`；`P7=EIO_LCD_BL`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 C3：U5 ports P0-P7

### 三按键与 RGB 指示灯

S3/S4/S5 按下分别将 EIO_KEY1/EIO_KEY2/EIO_KEY3 拉低，并各有 100nF 电容和 SD05 保护；LED2 三色通道由 EIO_LEDR/EIO_LEDG/EIO_LEDB 经 1KΩ电阻驱动。

- 参数与网络：`keys=S3 EIO_KEY1; S4 EIO_KEY2; S5 EIO_KEY3`；`key_filters=C6/C7/C8 100nF/25V`；`key_esd=D5/D6/D7 SD05`；`rgb=LED2 NHB-B2020RGB-A-HF`；`rgb_resistors=R25/R26/R27 1KΩ`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 A3-B3/C2：S3-S5、D5-D7、LED2/R25-R27

### 8 路光耦数字输入

PC1-PC8 EL3H4 的外侧输入为 EXCON_IN1-EXCON_IN8 与公共端 EXCON_COM；逻辑侧输出为 SYS_IN1-SYS_IN8，并由 5.1KΩ上拉至 SYS_3.3V、1nF/50V 滤波。

- 参数与网络：`optocouplers=PC1-PC8 EL3H4`；`external=EXCON_IN1-EXCON_IN8; EXCON_COM`；`logic=SYS_IN1-SYS_IN8`；`input_resistors=6.2KΩ/1% pairs`；`pullups=R30-R37 5.1KΩ`；`filters=C11-C18 1nF/50V`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 A2-D3：PC1-PC8/R14-R45/C11-C18

### AW9523B 继电器与输入映射

AW9523B P0_0-P0_3 输出 SYS_OUT1-SYS_OUT4，P0_4-P0_7 输入 SYS_IN1-SYS_IN4，P1_4-P1_7 输入 SYS_IN5-SYS_IN8。

- 参数与网络：`relay_outputs=P0_0 SYS_OUT1; P0_1 SYS_OUT2; P0_2 SYS_OUT3; P0_3 SYS_OUT4`；`inputs1_4=P0_4-P0_7 SYS_IN1-SYS_IN4`；`inputs5_8=P1_4-P1_7 SYS_IN5-SYS_IN8`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 A3-B3：U4 P0_0-P1_7

## 时钟

### RX8130CE 实时时钟

U7 RX8130CE 的 SCL/SDA 接 G15_SYS_SCL/G13_SYS_SDA，IRQ 接 G14_SYS_INT，VDD 接 SYS_3.3V，VBAT 连接 BATTERY_RTC。

- 参数与网络：`rtc=U7 RX8130CE`；`scl=GPIO15`；`sda=GPIO13`；`irq=GPIO14`；`supply=SYS_3.3V`；`backup=BATTERY_RTC`；`battery=B1`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 D3-D4：U7/C17/C18/R36/B1

## 保护电路

### RS-485 保护与终端

EXT_485_A/B 各串 FU1/FU2 24V/100mA，自恢复保护后由 D1 SM712 钳位；S1 与 R1 120Ω/1% 构成可选 A-B 终端。

- 参数与网络：`fuses=FU1/FU2 24V/100mA`；`tvs=D1 SM712`；`termination=S1 + R1 120Ω/1%`；`lines=EXT_485_A,EXT_485_B`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 A1-B1：FU1/FU2/D1/S1/R1

### CAN 保护与终端

EXCON_CANH/CANL 各串 FU2/FU3 24V/100mA，并由 D2 SM24CAN 钳位；S1 与 R1 120Ω/1% 构成可选终端。

- 参数与网络：`fuses=FU2/FU3 24V/100mA`；`tvs=D2 SM24CAN`；`termination=S1 + R1 120Ω/1%`；`lines=EXCON_CANH,EXCON_CANL`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 B1：FU2/FU3/D2/S1/R1

### 2x8 扩展信号保护

IO 板 J9 的 G3/G7/G8/G9/G11/G13/G14/G15/G40/G41 信号分别由 TVS1-TVS10 ESDS523.3C 对地保护。

- 参数与网络：`connector=J9 2x8`；`devices=TVS1-TVS10 ESDS523.3C`；`protected=G3_PHY_RST,G7_SPI_SCK,G8_SPI_MOSI,G9_SPI_MISO,G11_SPI_CS_EXT,G13_SYS_SDA,G14_SYS_INT,G15_SYS_SCL,EXT_G40,EXT_G41`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 C4-D4：J9/TVS1-TVS10

## 存储

### microSD SPI 连接

J5 TF 的 DAT0/MISO、DAT3/CS、CLK/SCK、CMD/MOSI 分别连接 G9_SPI_MISO、G10_SPI_CS_CARD、G7_SPI_SCK、G8_SPI_MOSI，VDD 接 SYS_3.3V。

- 参数与网络：`connector=J5 TF`；`miso=pin7 DAT0 -> GPIO9`；`cs=pin2 DAT3/CS -> GPIO10`；`sck=pin5 CLK -> GPIO7`；`mosi=pin3 CMD -> GPIO8`；`supply=SYS_3.3V`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 B4：J5/R15-R18/C12

## 音频

### 蜂鸣器驱动

STAMP_S3 GPIO44 形成 G44_BUZZER_PWM，经 R29 5.1KΩ驱动 Q3 SI2302，低侧控制 SYS_5V 供电的 BZ1；D3 1N4148WS 跨接感性支路。

- 参数与网络：`gpio=GPIO44 / G44_BUZZER_PWM`；`mosfet=Q3 SI2302`；`gate=R29 5.1KΩ`；`buzzer=BZ1 HYG8503-8WS`；`supply=SYS_5V`；`diode=D3 1N4148WS`
- 证据：图 0138054fc63d / 第 1 页 / CPU板第1页 C3：BZ1/Q3/R28/R29/D3

## 传感器

### LM75 温度传感器

U6 LM75BDP,118 的 SDA/SCL 连接 G13_SYS_SDA/G15_SYS_SCL，OS 经 R47 100Ω连接 G14_SYS_INT，A0/A1/A2 接地，VCC 接 SYS_3.3V。

- 参数与网络：`device=U6 LM75BDP,118`；`sda=GPIO13`；`scl=GPIO15`；`interrupt=OS -> R47 100Ω -> GPIO14`；`address_pins=A0=A1=A2=GND`；`supply=SYS_3.3V`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 C2：U6/R47/C21

### INA226 电压电流监测

U7 INA226AIDGSR 的 SCL/SDA 接 G15_SYS_SCL/G13_SYS_SDA，ALERT 经 R50 100Ω接 G14_SYS_INT；VBUS 经 R49 10Ω采样 SYS_VIN，IN+/IN- 使用 VOUT_CSP/VOUT_CSN。

- 参数与网络：`device=U7 INA226AIDGSR`；`scl=GPIO15`；`sda=GPIO13`；`alert=R50 100Ω -> GPIO14`；`vbus=SYS_VIN -> R49 10Ω -> VBUS`；`shunt_inputs=VOUT_CSP,VOUT_CSN`；`address_pins=A0/A1 tied low`；`supply=SYS_3.3V`
- 证据：图 a47ec05d0497 / 第 1 页 / IO板第1页 D1-D2：U7/Q1/R49/R50

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StamPLC 双板架构 | `cpu_asset=K141_sch_StamPLC_V10_CPU`；`io_asset=K141_sch_StamPLC_V10_IO`；`controller=STAMP_S3`；`interboard=CPU J3 <-> IO J8 2x10` |
| 电源 | SYS_VIN 到 SYS_5V | `input=J1 DC-0440-2.5A-2.0`；`input_fuse=FU4 2.5A/36V`；`rail=SYS_VIN`；`converter=U1 MP4560DN`；`inductor=L1 10uH/4.5A_0650`；`intermediate=PMU_5V`；`output_fuse=FU5 2A/12V`；`output=SYS_5V` |
| 电源 | SYS_5V 到 SYS_3.3V | `ldo=U3 SE8533K1-HF`；`input=SYS_5V`；`output=SYS_3.3V`；`input_cap=C3 22uF/16V`；`output_cap=C4 22uF/16V` |
| 电源 | MCU_5V 与 EXT_5V 分配 | `mcu_path=SYS_5V -> FU3 0.5A -> MCU_5V`；`load_switch=U4 LPW5209AB5F`；`switch_input=SYS_5V`；`switch_output=EXT_5V`；`loads=J6,J7` |
| 总线 | 系统 I2C 与中断/复位 | `controller=STAMP_S3`；`scl=GPIO15 / G15_SYS_SCL`；`sda=GPIO13 / G13_SYS_SDA`；`interrupt=GPIO14 / G14_SYS_INT`；`reset=GPIO3 / G3_PHY_RST`；`devices=PI4IOE5V6408,RX8130CE,AW9523B,LM75BDP,INA226` |
| 总线地址 | AW9523B I2C 地址 | `device=U4 AW9523B`；`address=0x59`；`bus=G15_SYS_SCL/G13_SYS_SDA` |
| 总线地址 | 其余 I2C 器件地址 | `PI4IOE5V6408=0x43`；`INA226AIDGSR=0x40`；`LM75BDP=0x48`；`RX8130CE=0x32`；`explicit_address_text_on_schematic=false` |
| 总线 | LCD、microSD 与扩展 SPI | `controller=STAMP_S3`；`sck=GPIO7 / G7_SPI_SCK`；`mosi=GPIO8 / G8_SPI_MOSI`；`miso=GPIO9 / G9_SPI_MISO`；`sd_cs=GPIO10 / G10_SPI_CS_CARD`；`lcd_cs=GPIO12 / G12_SPI_CS_LCD`；`ext_cs=GPIO11 / G11_SPI_CS_EXT` |
| 存储 | microSD SPI 连接 | `connector=J5 TF`；`miso=pin7 DAT0 -> GPIO9`；`cs=pin2 DAT3/CS -> GPIO10`；`sck=pin5 CLK -> GPIO7`；`mosi=pin3 CMD -> GPIO8`；`supply=SYS_3.3V` |
| 接口 | SPI LCD 与背光 | `sck=G7_SPI_SCK`；`mosi=G8_SPI_MOSI`；`rs=G6_LCD_RS`；`cs=G12_SPI_CS_LCD`；`reset=G3_PHY_RST`；`backlight=EIO_LCD_BL -> R24 100Ω -> Q2 SI2301 -> LEDA`；`supply=SYS_3.3V` |
| GPIO 与控制信号 | PI4IOE5V6408 端口映射 | `P0=EIO_KEY3`；`P1=EIO_KEY2`；`P2=EIO_KEY1`；`P4=EIO_LEDB`；`P5=EIO_LEDG`；`P6=EIO_LEDR`；`P7=EIO_LCD_BL` |
| GPIO 与控制信号 | 三按键与 RGB 指示灯 | `keys=S3 EIO_KEY1; S4 EIO_KEY2; S5 EIO_KEY3`；`key_filters=C6/C7/C8 100nF/25V`；`key_esd=D5/D6/D7 SD05`；`rgb=LED2 NHB-B2020RGB-A-HF`；`rgb_resistors=R25/R26/R27 1KΩ` |
| 音频 | 蜂鸣器驱动 | `gpio=GPIO44 / G44_BUZZER_PWM`；`mosfet=Q3 SI2302`；`gate=R29 5.1KΩ`；`buzzer=BZ1 HYG8503-8WS`；`supply=SYS_5V`；`diode=D3 1N4148WS` |
| 总线 | PWR-485 接口 | `transceiver=U2 SIT3088EEUA`；`rx=RO -> R7 5.1KΩ -> GPIO39`；`tx=GPIO0 -> R9 1KΩ -> DI`；`direction=GPIO46 -> RE/DE`；`a=EXT_485_A -> J1 pin3`；`b=EXT_485_B -> J1 pin4`；`power=J1 pin2 SYS_HV; pin1 GND` |
| 保护电路 | RS-485 保护与终端 | `fuses=FU1/FU2 24V/100mA`；`tvs=D1 SM712`；`termination=S1 + R1 120Ω/1%`；`lines=EXT_485_A,EXT_485_B` |
| 总线 | PWR-CAN 接口 | `transceiver=U2 SIT1044QTK/3`；`tx=GPIO42 -> R11 100Ω -> TXD`；`rx=RXD -> R12 100Ω -> GPIO43`；`canh=EXCON_CANH -> J2 pin3`；`canl=EXCON_CANL -> J2 pin4`；`power=J2 pin1 SYS_VIN; pin2 GND` |
| 保护电路 | CAN 保护与终端 | `fuses=FU2/FU3 24V/100mA`；`tvs=D2 SM24CAN`；`termination=S1 + R1 120Ω/1%`；`lines=EXCON_CANH,EXCON_CANL` |
| 传感器 | LM75 温度传感器 | `device=U6 LM75BDP,118`；`sda=GPIO13`；`scl=GPIO15`；`interrupt=OS -> R47 100Ω -> GPIO14`；`address_pins=A0=A1=A2=GND`；`supply=SYS_3.3V` |
| 传感器 | INA226 电压电流监测 | `device=U7 INA226AIDGSR`；`scl=GPIO15`；`sda=GPIO13`；`alert=R50 100Ω -> GPIO14`；`vbus=SYS_VIN -> R49 10Ω -> VBUS`；`shunt_inputs=VOUT_CSP,VOUT_CSN`；`address_pins=A0/A1 tied low`；`supply=SYS_3.3V` |
| 时钟 | RX8130CE 实时时钟 | `rtc=U7 RX8130CE`；`scl=GPIO15`；`sda=GPIO13`；`irq=GPIO14`；`supply=SYS_3.3V`；`backup=BATTERY_RTC`；`battery=B1` |
| GPIO 与控制信号 | 8 路光耦数字输入 | `optocouplers=PC1-PC8 EL3H4`；`external=EXCON_IN1-EXCON_IN8; EXCON_COM`；`logic=SYS_IN1-SYS_IN8`；`input_resistors=6.2KΩ/1% pairs`；`pullups=R30-R37 5.1KΩ`；`filters=C11-C18 1nF/50V` |
| 接口 | 隔离输入端子 | `common=J3 pin1 EXCON_COM; pins2/3 GND`；`inputs12=J4 EXCON_IN1/IN2`；`inputs34=J5 EXCON_IN3/IN4`；`inputs56=J6 EXCON_IN5/IN6`；`inputs78=J7 EXCON_IN7/IN8` |
| GPIO 与控制信号 | AW9523B 继电器与输入映射 | `relay_outputs=P0_0 SYS_OUT1; P0_1 SYS_OUT2; P0_2 SYS_OUT3; P0_3 SYS_OUT4`；`inputs1_4=P0_4-P0_7 SYS_IN1-SYS_IN4`；`inputs5_8=P1_4-P1_7 SYS_IN5-SYS_IN8` |
| 接口 | 四路继电器输出 | `driver=U5 ULN2003A`；`inputs=SYS_OUT1-SYS_OUT4`；`coil_drives=RLY_DRV1-RLY_DRV4`；`relays=RLY1-RLY4 HF3FF/005-1ZTF`；`connectors=J10-J13 KF128_5.0mm_3P`；`coil_supply=SYS_5V` |
| 接口 | HY2.0-4P 与扩展口 | `J6=pin1 GND; pin2 EXT_5V; pin3 EXT_G2; pin4 EXT_G1`；`J7=pin1 GND; pin2 EXT_5V; pin3 EXT_G5; pin4 EXT_G4`；`series=R20-R23 10Ω/1%`；`tvs=D2 SMF15C` |
| 接口 | CPU/IO 板互连总线 | `connectors=CPU J3; IO J8`；`pins=1-20`；`power=SYS_HV,SYS_5V,SYS_3.3V,GND`；`signals=G3_PHY_RST,G7_SPI_SCK,G8_SPI_MOSI,G9_SPI_MISO,G11_SPI_CS_EXT,G13_SYS_SDA,G14_SYS_INT,G15_SYS_SCL,EXT_G40,EXT_G41,G42_CAN_TX,G43_CAN_RX` |
| 保护电路 | 2x8 扩展信号保护 | `connector=J9 2x8`；`devices=TVS1-TVS10 ESDS523.3C`；`protected=G3_PHY_RST,G7_SPI_SCK,G8_SPI_MOSI,G9_SPI_MISO,G11_SPI_CS_EXT,G13_SYS_SDA,G14_SYS_INT,G15_SYS_SCL,EXT_G40,EXT_G41` |
| 内存与 Flash | Stamp 模组 Flash 容量 | `documented_module=Stamp-S3A / ESP32-S3FN8`；`documented_flash=8MB`；`schematic_symbol=STAMP_S3`；`explicit_capacity_shown=false` |

## 待确认事项

- `address.documented-i2c`：产品正文列出 PI4IOE5V6408 0x43、INA226 0x40、LM75 0x48、RX8130CE 0x32；两张原理图显示器件和地址配置引脚，但未独立打印这些地址数值。（证据：图 0138054fc63d / 第 1 页 / CPU板第1页 U5 PI4IOE5V6408 ADDR 与 U7 RX8130CE; 图 a47ec05d0497 / 第 1 页 / IO板第1页 U6 LM75 A0-A2 与 U7 INA226 A0/A1）
- `memory.stamp-flash-capacity`：产品正文标称 Stamp-S3A/ESP32-S3FN8 含 8MB Flash；CPU 原理图只将控制模组标为 STAMP_S3，未独立打印 SoC 完整料号或 Flash 容量。（证据：图 0138054fc63d / 第 1 页 / CPU板第1页 A2-B2：STAMP_S3 模组）
- `review.i2c-addresses`：PI4IOE5V6408、INA226、LM75 和 RX8130CE 的板级 I2C 地址是否分别固定为 0x43、0x40、0x48、0x32？；原因：地址来自产品正文；原理图显示器件与地址配置引脚，但未像 AW9523B 一样打印地址数值。
- `review.flash-capacity`：K141 当前 STAMP_S3 控制模组的 Flash 容量是否固定为 8MB？；原因：8MB 和 ESP32-S3FN8 来自产品正文；CPU 原理图只打印 STAMP_S3 模组名称。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0138054fc63d55ca4286a7f8c5ebf8e9aadbeb0c16e87dcf8bc0adbd22564268` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_CPU_sch_01.png` |
| 2 | 1 | `a47ec05d049715703e2b487f52597967d4070f8d1fbc638acb2edebaff74b651` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_IO_sch_01.png` |

---

源文档：`zh_CN/core/StamPLC.md`

源文档 SHA-256：`8dffb340a8ee64bb9f449e9aeb92ae6e0e9eded7a2d8633dc4077178c4070c0c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
