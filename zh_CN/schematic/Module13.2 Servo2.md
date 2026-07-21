# Module13.2 Servo2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 Servo2 |
| SKU | M014-B |
| 产品 ID | `module13-2-servo2-40ec9a04a77c` |
| 源文档 | `zh_CN/module/servo2.md` |

## 概述

Module13.2 Servo2 以 U3 PCA9685 产生 Sv0-Sv15 共 16 路 PWM，经 4.7K 电阻阵列连接两组八路三针舵机接口。U1、U2 两颗 SY8368AQQC 分别把 VBAT_2-3S 转换为 VOUT1_P5V、VOUT2_P5V，各为 8 路舵机供电；U4 JW5033 生成系统 VCC_5V，M5-Bus 提供 VCC_3V3 与 IIC_SCL/IIC_SDA。XT_60 输入经 S1 电源开关进入 VBAT_2-3S，UVLO/AutoEnable 电路驱动 nHOST，三位地址开关与下拉阵列配置 PCA9685 A0-A2。

## 检索关键词

`Module13.2 Servo2`、`M014-B`、`PCA9685`、`SY8368AQQC`、`JW5033`、`Servo`、`PWM`、`Sv0`、`Sv1`、`Sv2`、`Sv3`、`Sv4`、`Sv5`、`Sv6`、`Sv7`、`Sv8`、`Sv9`、`Sv10`、`Sv11`、`Sv12`、`Sv13`、`Sv14`、`Sv15`、`I2C`、`0x40`、`0x47`、`IIC_SCL`、`IIC_SDA`、`A0`、`A1`、`A2`、`VBAT_2-3S`、`VOUT1_P5V`、`VOUT2_P5V`、`VCC_5V`、`VCC_3V3`、`XT_60`、`nHOST`、`M5BUS`、`Power SW`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | PCA9685 | 16 通道 I2C PWM 控制器，输出 LED0-LED15 对应 Sv0-Sv15 | 图 d97d5f7e1bf0 / 第 1 页 / 页面中央 PWM 区 U3 PCA9685，VDD/GND/OE/EXTCLK/SCL/SDA/A0-A5 与 LED0-LED15 |
| U1,U2 | SY8368AQQC; SY8368AQQC | 两路 VBAT_2-3S 至 5V 的大电流舵机降压转换器 | 图 d97d5f7e1bf0 / 第 1 页 / 页面左上 U1 与上中 U2 SY8368AQQC，分别输出 VOUT1_P5V 与 VOUT2_P5V |
| U4 | JW5033 | VBAT_2-3S 至 VCC_5V 的系统降压转换器 | 图 d97d5f7e1bf0 / 第 1 页 / 页面左中 Sys Buck DC-DC 区 U4 JW5033、D2、L3 与 VCC_5V |
| J1 | XT_60 | 外部 2S/3S 电池或直流电源输入连接器 | 图 d97d5f7e1bf0 / 第 1 页 / 页面右上 Battery IN 区 J1 XT_60，pin 1/PVCC 接 VBAT_2-3S_IN，pin 2/PGND 接 GND |
| S1 | SW-TH_3P-P4.70_L11.1-W12.7 | VBAT_2-3S_IN 到 VBAT_2-3S 的三脚电源开关 | 图 d97d5f7e1bf0 / 第 1 页 / 页面右上 Power SW 区 S1，VBAT_2-3S_IN 与 VBAT_2-3S 网络 |
| Q1,Q2,D1 | Si2301; S8050; 1N5819 | 欠压锁定与自动使能 nHOST 控制电路 | 图 d97d5f7e1bf0 / 第 1 页 / 页面上中偏右 UVLO&AutoEnable 区 Q1 Si2301、Q2 S8050、D1 1N5819 与 nHOST/VBAT/VCC_3V3 |
| D2,L3 | SS34; 3.3uH/L4012 | JW5033 输入串联肖特基与输出电感 | 图 d97d5f7e1bf0 / 第 1 页 / 页面左中 U4 周围 D2 SS34 与 L3 3.3uH/L4012 |
| L1,L2 | 3.3uH/SPM6530T/MCW-0630; 3.3uH/SPM6530T/MCW-0630 | U1/U2 两路舵机 5V 降压输出电感 | 图 d97d5f7e1bf0 / 第 1 页 / 页面上方 U1/U2 LX 后 L1/L2，均标 3.3uH/SPM6530T/MCW-0630 |
| LED1,R9; LED2,R10 | GREEN,4.7K; GREEN,4.7K | VOUT1_P5V 与 VOUT2_P5V 两路舵机电源指示 | 图 d97d5f7e1bf0 / 第 1 页 / 页面 U1/U2 左侧 R9/LED1 GREEN 与 R10/LED2 GREEN，从各 VOUT_P5V 接到 GND |
| RP1,RP2,RP3,RP4 | 4.7K resistor arrays | PCA9685 LED0-LED15 到 Sv0-Sv15 的串联电阻阵列 | 图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 右侧四组 4.7K 电阻阵列，将 LED0-LED15 接至 Sv0-Sv15 |
| 地址开关,RP5 | 3-position DIP; 4.7K resistor array | PCA9685 A0-A2 上拉选择与 A0-A5 默认下拉 | 图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 左侧三位开关上端共接 VCC_3V3、下端接 A0-A2，RP5 4.7K 将 A0-A5 拉向 GND |
| J3A,J2B,J2C | THT_Male_P arrays | Sv0-Sv7、VOUT2_P5V、GND 组成的上半组八路三针舵机接口 | 图 d97d5f7e1bf0 / 第 1 页 / 页面右中 ServoCon 上半组 J3A 信号 Sv0-Sv7、J2B VOUT2_P5V、J2C GND |
| J2A,J3B,J3C | THT_Male_P arrays | Sv8-Sv15、VOUT1_P5V、GND 组成的下半组八路三针舵机接口 | 图 d97d5f7e1bf0 / 第 1 页 / 页面右中 ServoCon 下半组 J2A 信号 Sv8-Sv15、J3B VOUT1_P5V、J3C GND |
| BUS1 | M5BUS | 30 针主机堆叠接口，提供 I2C、VCC_3V3、VCC_5V、HPWR/VBAT_2-3S 与 GND | 图 d97d5f7e1bf0 / 第 1 页 / 页面右下 BUS1 M5BUS，pin 1-30 与 IIC_SCL/IIC_SDA/VCC/VBAT/GND 网络 |

## 系统结构

### Module13.2 Servo2 系统架构

PCA9685 通过 I2C 接收主机命令并产生 16 路 PWM；两颗 SY8368AQQC 分别为两组 8 路舵机接口供电，JW5033 生成系统 5V，XT60/S1 提供外部电源输入与开关控制。

- 参数与网络：`pwm_controller=U3 PCA9685`；`channels=16`；`servo_bucks=U1/U2 SY8368AQQC`；`system_buck=U4 JW5033`；`input=J1 XT_60`；`power_switch=S1`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 完整单页 U1-U4、ServoCon、Power SW、Battery IN 与 M5 Bus 分区

## 核心器件

### PCA9685 控制与时钟针脚

U3 VDD 接 VCC_3V3，GND 接地，OE pin 23 接地，SCL/SDA 接 I2C；EXTCLK pin 25 未外接，PWM 使用芯片内部未展开时钟。

- 参数与网络：`supply=pin 28/VDD -> VCC_3V3`；`ground=pin 14/GND`；`output_enable=pin 23/OE -> GND`；`external_clock=pin 25/EXTCLK unconnected`；`i2c=pin 27/SCL,pin 26/SDA`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 顶部/左侧 VDD/GND/OE/EXTCLK/SCL/SDA

## 电源

### XT60 外部电源与开关

J1 XT_60 pin 1/PVCC 连接 VBAT_2-3S_IN，pin 2/PGND 接 GND；S1 在 VBAT_2-3S_IN 与 VBAT_2-3S 之间切换电源。

- 参数与网络：`connector=J1 XT_60`；`positive=pin 1/PVCC -> VBAT_2-3S_IN`；`negative=pin 2/PGND -> GND`；`switch=S1 -> VBAT_2-3S`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面右上 Battery IN 与 Power SW 区

### U1 VOUT1_P5V 降压

U1 SY8368AQQC 由 VBAT_2-3S 供电，LX 经 L1 3.3uH 输出 VOUT1_P5V；R7 36K/R13 4.7K 为反馈分压，输出由 C9 1000uF/10V、C10 22uF/6.3V、C11 470nF/16V 滤波。

- 参数与网络：`converter=U1 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`inductor=L1 3.3uH/SPM6530T/MCW-0630`；`output=VOUT1_P5V`；`feedback=R7 36K,R13 4.7K`；`output_caps=C9 1000uF/10V,C10 22uF/6.3V,C11 470nF/16V`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面左上 IN Power Buck DC-DC1 U1/L1/R7/R13/C9-C11

### U2 VOUT2_P5V 降压

U2 SY8368AQQC 由 VBAT_2-3S 供电，LX 经 L2 3.3uH 输出 VOUT2_P5V；R6 36K/R14 4.7K 为反馈分压，输出由 C12 1000uF/10V、C13 22uF/6.3V、C14 470nF/16V 滤波。

- 参数与网络：`converter=U2 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`inductor=L2 3.3uH/SPM6530T/MCW-0630`；`output=VOUT2_P5V`；`feedback=R6 36K,R14 4.7K`；`output_caps=C12 1000uF/10V,C13 22uF/6.3V,C14 470nF/16V`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面上中 IN Power Buck DC-DC2 U2/L2/R6/R14/C12-C14

### U4 VCC_5V 系统降压

VBAT_2-3S 经 D2 SS34 进入 U4 JW5033，EN 接 DCDC_EN，SW 经 L3 3.3uH/L4012 输出 VCC_5V；R18 330K/R19 62K 构成反馈分压。

- 参数与网络：`input=VBAT_2-3S -> D2 SS34`；`converter=U4 JW5033`；`enable=DCDC_EN`；`inductor=L3 3.3uH/L4012`；`output=VCC_5V`；`feedback=R18 330K,R19 62K`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面左中 Sys Buck DC-DC U4/D2/L3/R18/R19

### UVLO 与 nHOST 自动使能

UVLO&AutoEnable 区使用 Q1 Si2301、Q2 S8050、D1 1N5819 及 R2/R11/R15/R12/R8 网络，在 VBAT_2-3S 与 VCC_3V3 域之间生成 nHOST 控制两颗 SY8368AQQC EN。

- 参数与网络：`mosfet=Q1 Si2301`；`transistor=Q2 S8050`；`diode=D1 1N5819`；`input=VBAT_2-3S`；`logic_supply=VCC_3V3`；`output=nHOST -> U1/U2 EN`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面上中偏右 UVLO&AutoEnable 完整电路与 U1/U2 nHOST

### BUS1 电源针脚

BUS1 pin 2、4、6 的 HPWR 共接 VBAT_2-3S；pin 3/5V 接 VCC_5V，pin 19/3.3V 接 VCC_3V3，pin 26、28、30 接 GND；pin 1/BAT 带未连接标记。

- 参数与网络：`hpwr=pins 2,4,6 -> VBAT_2-3S`；`five_volt=pin 3 -> VCC_5V`；`three3=pin 19 -> VCC_3V3`；`ground=pins 26,28,30`；`battery_pin=pin 1/BAT no-connect`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面右下 BUS1 外部 VBAT_2-3S/VCC_5V/VCC_3V3/GND/BAT 网络

## 接口

### Sv0-Sv7 舵机接口组

J3A 引出 Sv0-Sv7 信号，J2B 的八个对应电源针共接 VOUT2_P5V，J2C 的八个对应回路针共接 GND，组成上半组八路三针舵机接口。

- 参数与网络：`signals=Sv0,Sv1,Sv2,Sv3,Sv4,Sv5,Sv6,Sv7`；`supply=VOUT2_P5V`；`ground=GND`；`connectors=J3A signal,J2B power,J2C ground`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面右中 ServoCon 上半组 J3A/J2B/J2C

### Sv8-Sv15 舵机接口组

J2A 引出 Sv8-Sv15 信号，J3B 的八个对应电源针共接 VOUT1_P5V，J3C 的八个对应回路针共接 GND，组成下半组八路三针舵机接口。

- 参数与网络：`signals=Sv8,Sv9,Sv10,Sv11,Sv12,Sv13,Sv14,Sv15`；`supply=VOUT1_P5V`；`ground=GND`；`connectors=J2A signal,J3B power,J3C ground`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面右中 ServoCon 下半组 J2A/J3B/J3C

## 总线

### PCA9685 I2C 总线

BUS1 pin 13/G22/IIC_SCL 连接 IIC_SCL 至 U3 pin 27/SCL，pin 14/G21/IIS_SDA 连接 IIC_SDA 至 U3 pin 26/SDA；R16/R17 各 4.7K 将 SCL/SDA 上拉到 VCC_3V3。

- 参数与网络：`controller=M5 host via BUS1`；`device=U3 PCA9685`；`scl=BUS1 pin 13 -> IIC_SCL -> U3 pin 27`；`sda=BUS1 pin 14 -> IIC_SDA -> U3 pin 26`；`pullups=R16 4.7K,R17 4.7K to VCC_3V3`；`level=VCC_3V3`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 SCL/SDA/R16/R17 与右下 BUS1 IIC_SCL/IIC_SDA

## 总线地址

### PCA9685 地址硬件配置

U3 A0、A1、A2 分别连接三位开关，可切换到 VCC_3V3；RP5 4.7K 电阻阵列将 A0-A5 默认下拉到 GND，A3-A5 没有开关。硬件因此提供 A0-A2 三位可调。

- 参数与网络：`adjustable_bits=A0,A1,A2`；`switch_high=to VCC_3V3`；`pulldowns=RP5 4.7K on A0-A5 to GND`；`fixed_low_bits=A3,A4,A5`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 左侧三位地址开关、RP5 与 A0-A5

## GPIO 与控制信号

### 16 路 PWM 信号映射

U3 LED0-LED7 经上方两组 4.7K 阵列形成 Sv0-Sv7，LED8-LED15 经下方两组 4.7K 阵列形成 Sv8-Sv15，共 16 路独立舵机控制信号。

- 参数与网络：`channels_0_7=LED0-LED7 -> 4.7K arrays -> Sv0-Sv7`；`channels_8_15=LED8-LED15 -> 4.7K arrays -> Sv8-Sv15`；`channel_count=16`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面中央 U3 LED0-LED15、RP1-RP4 与 Sv0-Sv15

### 双路舵机电源指示灯

VOUT1_P5V 经 R9 4.7K 与 LED1 GREEN 接 GND；VOUT2_P5V 经 R10 4.7K 与 LED2 GREEN 接 GND。

- 参数与网络：`channel1=VOUT1_P5V -> R9 4.7K -> LED1 GREEN -> GND`；`channel2=VOUT2_P5V -> R10 4.7K -> LED2 GREEN -> GND`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面 U1/U2 左侧 LED1/LED2 电源指示支路

## 时钟

### 外部时钟可见性

原理图没有晶体、谐振器或振荡器；U3 EXTCLK pin 25 未连接。

- 参数与网络：`crystal_visible=false`；`oscillator_visible=false`；`pca9685_extclk=pin 25 unconnected`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 页面 U3 EXTCLK 与完整单页，无 Y/X 时钟位号

## 保护电路

### 输入与舵机接口保护可见性

系统降压输入串联 D2 SS34，UVLO 电路含 D1 1N5819；原理图未绘出输入保险丝、TVS、反接专用 MOSFET、舵机信号 ESD 或每路过流保护。

- 参数与网络：`series_diode=D2 SS34`；`uvlo_diode=D1 1N5819`；`fuse_visible=false`；`tvs_visible=false`；`servo_esd_visible=false`；`per_channel_overcurrent_visible=false`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 完整电源输入、UVLO 与 ServoCon 外围

## 内存与 Flash

### 存储器与内存可见性

原理图没有 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 完整单页全部器件，无存储位号

## 调试与烧录

### 复位、BOOT 与调试可见性

原理图没有 MCU、复位按键、BOOT、SWD/JTAG 或专用调试接口；PCA9685 只通过 I2C 与地址开关配置。

- 参数与网络：`mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 完整单页器件与接口

## 其他事实

### 其他功能分区可见性

原理图未绘出 SPI、UART、CAN、RS-485、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；核心接口为 I2C 与 16 路 PWM。

- 参数与网络：`spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 d97d5f7e1bf0 / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 Servo2 系统架构 | `pwm_controller=U3 PCA9685`；`channels=16`；`servo_bucks=U1/U2 SY8368AQQC`；`system_buck=U4 JW5033`；`input=J1 XT_60`；`power_switch=S1` |
| 电源 | XT60 外部电源与开关 | `connector=J1 XT_60`；`positive=pin 1/PVCC -> VBAT_2-3S_IN`；`negative=pin 2/PGND -> GND`；`switch=S1 -> VBAT_2-3S` |
| 电源 | U1 VOUT1_P5V 降压 | `converter=U1 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`inductor=L1 3.3uH/SPM6530T/MCW-0630`；`output=VOUT1_P5V`；`feedback=R7 36K,R13 4.7K`；`output_caps=C9 1000uF/10V,C10 22uF/6.3V,C11 470nF/16V` |
| 电源 | U2 VOUT2_P5V 降压 | `converter=U2 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`inductor=L2 3.3uH/SPM6530T/MCW-0630`；`output=VOUT2_P5V`；`feedback=R6 36K,R14 4.7K`；`output_caps=C12 1000uF/10V,C13 22uF/6.3V,C14 470nF/16V` |
| 电源 | U4 VCC_5V 系统降压 | `input=VBAT_2-3S -> D2 SS34`；`converter=U4 JW5033`；`enable=DCDC_EN`；`inductor=L3 3.3uH/L4012`；`output=VCC_5V`；`feedback=R18 330K,R19 62K` |
| 电源 | UVLO 与 nHOST 自动使能 | `mosfet=Q1 Si2301`；`transistor=Q2 S8050`；`diode=D1 1N5819`；`input=VBAT_2-3S`；`logic_supply=VCC_3V3`；`output=nHOST -> U1/U2 EN` |
| 电源 | 输入范围与输出功率 | `documented_input=6-12V`；`documented_dual_output=35W total,5V/3.5A x2`；`documented_single_output=25W,5V/5A`；`documented_bus_output=5V/2A`；`schematic_ratings_visible=false` |
| 总线 | PCA9685 I2C 总线 | `controller=M5 host via BUS1`；`device=U3 PCA9685`；`scl=BUS1 pin 13 -> IIC_SCL -> U3 pin 27`；`sda=BUS1 pin 14 -> IIC_SDA -> U3 pin 26`；`pullups=R16 4.7K,R17 4.7K to VCC_3V3`；`level=VCC_3V3` |
| 总线地址 | PCA9685 地址硬件配置 | `adjustable_bits=A0,A1,A2`；`switch_high=to VCC_3V3`；`pulldowns=RP5 4.7K on A0-A5 to GND`；`fixed_low_bits=A3,A4,A5` |
| 总线地址 | PCA9685 I2C 地址范围 | `documented_default=0x40`；`documented_range=0x40-0x47`；`adjustable_bits=3`；`schematic_numeric_address_visible=false` |
| GPIO 与控制信号 | 16 路 PWM 信号映射 | `channels_0_7=LED0-LED7 -> 4.7K arrays -> Sv0-Sv7`；`channels_8_15=LED8-LED15 -> 4.7K arrays -> Sv8-Sv15`；`channel_count=16` |
| 接口 | Sv0-Sv7 舵机接口组 | `signals=Sv0,Sv1,Sv2,Sv3,Sv4,Sv5,Sv6,Sv7`；`supply=VOUT2_P5V`；`ground=GND`；`connectors=J3A signal,J2B power,J2C ground` |
| 接口 | Sv8-Sv15 舵机接口组 | `signals=Sv8,Sv9,Sv10,Sv11,Sv12,Sv13,Sv14,Sv15`；`supply=VOUT1_P5V`；`ground=GND`；`connectors=J2A signal,J3B power,J3C ground` |
| 核心器件 | PCA9685 控制与时钟针脚 | `supply=pin 28/VDD -> VCC_3V3`；`ground=pin 14/GND`；`output_enable=pin 23/OE -> GND`；`external_clock=pin 25/EXTCLK unconnected`；`i2c=pin 27/SCL,pin 26/SDA` |
| 电源 | BUS1 电源针脚 | `hpwr=pins 2,4,6 -> VBAT_2-3S`；`five_volt=pin 3 -> VCC_5V`；`three3=pin 19 -> VCC_3V3`；`ground=pins 26,28,30`；`battery_pin=pin 1/BAT no-connect` |
| GPIO 与控制信号 | 双路舵机电源指示灯 | `channel1=VOUT1_P5V -> R9 4.7K -> LED1 GREEN -> GND`；`channel2=VOUT2_P5V -> R10 4.7K -> LED2 GREEN -> GND` |
| 保护电路 | 输入与舵机接口保护可见性 | `series_diode=D2 SS34`；`uvlo_diode=D1 1N5819`；`fuse_visible=false`；`tvs_visible=false`；`servo_esd_visible=false`；`per_channel_overcurrent_visible=false` |
| 时钟 | 外部时钟可见性 | `crystal_visible=false`；`oscillator_visible=false`；`pca9685_extclk=pin 25 unconnected` |
| 调试与烧录 | 复位、BOOT 与调试可见性 | `mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `power.documented-ratings`：产品正文记载外部输入 6-12V、双路总功率 35W（5V/3.5A×2）、单路最大 25W（5V/5A），电池底座供电最高 5V/2A；原理图只标 VBAT_2-3S、P5V 与器件值，未打印这些额定参数。（证据：图 d97d5f7e1bf0 / 第 1 页 / 完整电源区仅标 VBAT_2-3S、VOUT1_P5V、VOUT2_P5V 与元件参数）
- `address.documented-range`：产品正文记载地址范围为 0x40-0x47；原理图显示 A0-A2 三位选择，但未打印十六进制基地址或数值范围。（证据：图 d97d5f7e1bf0 / 第 1 页 / 页面 U3 PCA9685 A0-A5 地址区，无十六进制地址文字）
- `review.power-ratings`：Module13.2 Servo2 的正式输入范围与双路/单路输出功率是否与产品正文参数完全一致？；原因：原理图只给出 VBAT_2-3S、5V 输出网络和元件值，没有打印 6-12V、3.5A/5A 或功率额定值。
- `review.i2c-address`：当前 PCA9685 硬件的正式 I2C 地址范围是否确认为 0x40-0x47？；原因：原理图确认 A0-A2 三位选择，但未打印 PCA9685 十六进制基地址。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d97d5f7e1bf0a4c4489ad7fcf44a230895aecc510051a36c437a06018103930d` | `https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_sch_01.webp` |

---

源文档：`zh_CN/module/servo2.md`

源文档 SHA-256：`f2d93ebe04ed2fed266fb3a6ba37cb915ad793e98a70e94455837a6ccc4245ec`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
