# Module 4EncoderMotor 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module 4EncoderMotor |
| SKU | M138 |
| 产品 ID | `module-4encodermotor-0af1ee832906` |
| 源文档 | `zh_CN/module/Module-4EncoderMotor.md` |

## 概述

Module 4EncoderMotor 以 U3 STM32F030C8T6 控制 U4~U7 四颗 BL5617 单通道 H 桥，每路提供 PWM、正反向控制、M+/M- 输出及 A/B 编码反馈。U2 INA199A1DCKR 配合 R24 10mΩ 检测 VM 电流，VM 分压/钳位网络形成 ADC1_OUT 电压采样。VIN_12V 分别经 U1 SY8205FCC 生成 VCC_5V、经 U9 SY8303AIC 生成 BUS_5V，U10 HX6306P332MR 再生成 MCU_3V3；I2C 地址 0x24、3A/10W 能力及高级控制模式需由固件和器件资料确认。

## 检索关键词

`Module 4EncoderMotor`、`M138`、`STM32F030C8T6`、`BL5617`、`INA199A1DCKR`、`SY8205FCC`、`SY8303AIC`、`HX6306P332MR`、`TL432`、`I2C`、`0x24`、`MCU_IIC_SDA`、`MCU_IIC_SCL`、`ADC1_OUT`、`ADC2_OUT`、`MCU_PWM_M1`、`MCU_PWM_M2`、`MCU_PWM_M3`、`MCU_PWM_M4`、`MCU_DIR_M1R`、`MCU_DIR_M1F`、`MCU_DIR_M2R`、`MCU_DIR_M2F`、`MCU_DIR_M3R`、`MCU_DIR_M3F`、`MCU_DIR_M4R`、`MCU_DIR_M4F`、`E1_A`、`E1_B`、`E2_A`、`E2_B`、`E3_A`、`E3_B`、`E4_A`、`E4_B`、`VIN_12V`、`VM`、`BUS_5V`、`MCU_3V3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030C8T6 | I2C 从控制器，执行四路 PWM/方向控制、编码器采集与电流电压 ADC 采样 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 A2-B3 MCU 区 U3 STM32F030C8T6 |
| U4/U5/U6/U7 | BL5617 | 四路独立有刷直流电机 H 桥驱动器 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 A3-B4 4x BDC DRIVERS 区 U4~U7 BL5617 |
| U2 | INA199A1DCKR | 跨 R24 分流电阻测量 VM 电流并输出 ADC2_OUT | 图 44cdc4d4acae / 第 1 页 / 第 1 页 D3-D4 U2 INA199A1DCKR、R24 10mR/1206 与 ADC2_OUT |
| U1 | SY8205FCC | 将 VIN_12V 降压为 VCC_5V | 图 44cdc4d4acae / 第 1 页 / 第 1 页 B2-C3 U1 SY8205FCC 与 L1、VCC_5V |
| U9 | SY8303AIC | 将 VIN_12V 降压为 BUS_5V | 图 44cdc4d4acae / 第 1 页 / 第 1 页 D2-D3 BUCK_5V 区 U9 SY8303AIC 与 L3、BUS_5V |
| U10 | HX6306P332MR | 由 BUS_5V 生成 MCU_3V3 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 D4 U10 HX6306P332MR，VIN BUS_5V、VOUT MCU_3V3 |
| U8 | TL432 | MCU_3V3 电源网络的并联基准/钳位器件 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 D4 U8 TL432 接 MCU_3V3 与 GND |
| J2 | M5_BUS | 30 针堆叠接口，引出 I2C、复位、BUS_3V3、BUS_5V、BUS_BAT、HPWR 与 GND | 图 44cdc4d4acae / 第 1 页 / 第 1 页 A1-B1 CORE_BUS 区 J2 M5_BUS |
| J4 | DBG_SWD | MCU_3V3、SWCLK、SWDIO、CORE_RST 与 GND 调试接口 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 A3 J4 DBG_SWD 1~5 脚 |
| P1/P3/P5/P7 | Header 2 | 四组电机 M+/M- 输出接口 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 A4-B4 P1/P3/P5/P7 Header 2 |
| P2/P4/P6/P8 | GROVE 4P | 四组编码器 A/B、BUS_5V、GND 接口 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 B4-C4 PORTS 区 P2/P4/P6/P8 GROVE 4P |
| J1 | Header 2 | HPWR/GND 外部电源输入端 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 B1 POWER&SWITCH 区 J1 PWR+/PWR- |
| S3/S4 | SW-PWR | VIN_12V 与 VM 电源路径选择开关 | 图 44cdc4d4acae / 第 1 页 / 第 1 页 B1 S3 POWER&SWITCH 与 C1-D1 S4 VM SWITCH |

## 系统结构

### Module 4EncoderMotor

U3 STM32F030C8T6 通过 I2C 接 J2，输出四路 PWM 和八路方向信号控制 U4~U7 BL5617，并采集四组编码器 A/B 与 ADC1_OUT/ADC2_OUT。

- 参数与网络：`mcu=U3 STM32F030C8T6`；`drivers=U4,U5,U6,U7 BL5617`；`motors=4`；`encoders=4`；`monitoring=ADC1_OUT voltage,ADC2_OUT current`；`host_bus=I2C`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页全图 MCU、4x BDC DRIVERS、PORTS、监测与 CORE_BUS

## 核心器件

### U3

主控制器位号 U3，型号标为 STM32F030C8T6。

- 参数与网络：`reference=U3`；`part_number=STM32F030C8T6`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 U3 顶部 STM32F030C8T6

## 电源

### U1 SY8205FCC

U1 从 VIN_12V 经 LX/L1 生成 VCC_5V，EN 由 R1 100K 接 VIN_12V，R2 220K 与 R3 33K 构成 FB 分压。

- 参数与网络：`input=VIN_12V`；`converter=U1 SY8205FCC`；`inductor=L1 0530/10uH`；`output=VCC_5V`；`feedback=R2 220K,R3 33K`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 B2-C3 U1/L1/VCC_5V

### U9 SY8303AIC

U9 从 VIN_12V 经 LX/L3 6.8uH 生成 BUS_5V，输入串有 D3 SS54，输出并有 D17 TVS 5V 与红色电源 LED D14/R38。

- 参数与网络：`input=VIN_12V via D3 SS54`；`converter=U9 SY8303AIC`；`inductor=L3 6.8uH`；`output=BUS_5V`；`protection=D17 TVS 5V`；`indicator=D14 RED 0603,R38 2K`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 D2-D3 BUCK_5V 区

### U10 HX6306P332MR

U10 由 BUS_5V 输入并输出 MCU_3V3，输入/输出配置 C32/C33 10uF 与 C36/C35 10uF，U8 TL432 并接 MCU_3V3 对地。

- 参数与网络：`input=BUS_5V`；`regulator=U10 HX6306P332MR`；`output=MCU_3V3`；`reference_clamp=U8 TL432`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 D4 U10/U8 电源区

### HPWR/VIN_12V/VM 开关网络

J1 提供 HPWR/GND；S3 与 Q4 APM230Q、Q5 DTC114YUA 形成 HPWR 到 VIN_12V 的电源开关，S4 与 Q1/Q2/Q7/Q3/Q6 网络选择/控制 VM_IN 与 VM 路径。

- 参数与网络：`input=J1 HPWR`；`vin_switch=S3,Q4 APM230Q,Q5 DTC114YUA`；`vin_output=VIN_12V`；`vm_switch=S4,Q1/Q2/Q7 APM230Q,Q3/Q6 DTC114YUA`；`motor_rail=VM`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 B1 POWER&SWITCH 与 C1-D1 VM SWITCH

## 接口

### P2/P4/P6/P8

四组 Grove 编码器口均为 IO2=Ex_A、IO1=Ex_B、5V=BUS_5V、GND=GND；A/B 信号各经 4.7K 串联电阻连接 MCU_ENC 网络。

- 参数与网络：`P2=E1_A,E1_B,BUS_5V,GND`；`P4=E2_A,E2_B,BUS_5V,GND`；`P6=E3_A,E3_B,BUS_5V,GND`；`P8=E4_A,E4_B,BUS_5V,GND`；`series_resistors=R6/R7,R8/R9,R20/R21,R22/R23 4.7K`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 B4-C4 PORTS 区

### J2 M5_BUS

J2.2/.4/.6 接 GND，J2.5 接 CORE_RST，J2.11 接 BUS_3V3，J2.17/18 接 MCU_IIC_SCL/SDA，J2.27 接 BUS_5V，J2.29 接 BUS_BAT，J2.26/.28/.30 接 HPWR。

- 参数与网络：`ground=pins2,4,6`；`reset=pin5 CORE_RST`；`3v3=pin11 BUS_3V3`；`i2c=pin17 SCL,pin18 SDA`；`5v=pin27 BUS_5V`；`battery=pin29 BUS_BAT`；`hpwr=pins26,28,30`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A1 J2 外部网络

## 总线

### U3 I2C

U3 PB10/PB11 分别接 MCU_IIC_SCL/MCU_IIC_SDA，并连接 J2.17/J2.18；R13/R12 各 4.7K 将 SCL/SDA 上拉到 MCU_3V3。

- 参数与网络：`scl=U3 PB10 -> MCU_IIC_SCL -> J2.17`；`sda=U3 PB11 -> MCU_IIC_SDA -> J2.18`；`scl_pullup=R13 4.7K`；`sda_pullup=R12 4.7K`；`rail=MCU_3V3`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A1 J2/R12/R13 与 A2 U3 PB10/PB11

### U4~U7 电机输出

U4/U5/U6/U7 的 OUTR/OUTF 分别形成 M1-/M1+、M2-/M2+、M3-/M3+、M4-/M4+，并连接 P1/P3/P5/P7。

- 参数与网络：`U4=M1-/M1+ -> P1`；`U5=M2-/M2+ -> P3`；`U6=M3-/M3+ -> P5`；`U7=M4-/M4+ -> P7`；`supply=VM`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A4-B4 U4~U7 与 P1/P3/P5/P7

## GPIO 与控制信号

### 四路 PWM

MCU_PWM_M1/M2/M3/M4 分别连接 U3 PA9/PA8/PA11/PA10，并各经两只 10K 电阻分配到对应 BL5617 的 INR/INF。

- 参数与网络：`M1=U3 PA9`；`M2=U3 PA8`；`M3=U3 PA11`；`M4=U3 PA10`；`distribution=R15/R16,R18/R25,R27/R31,R30/R32 each 10K`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A2 U3 PWM 网络与 A3 分配电阻

### 四路方向控制

M1R/M1F 接 U3 PB14/PB15，M2R/M2F 接 PB12/PB13，M3R/M3F 接 PB4/PB5，M4R/M4F 接 PA15/PB3；各路经 1N4148WT 二极管接对应 BL5617 INR/INF。

- 参数与网络：`M1=PB14/PB15`；`M2=PB12/PB13`；`M3=PB4/PB5`；`M4=PA15/PB3`；`diodes=D4-D11 1N4148WT`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 U3 DIR 网络与 U4~U7 前 D4~D11

### 四组编码器输入

E1_A/E1_B 接 U3 PA6/PA7，E2_A/E2_B 接 PA4/PA5，E3_A/E3_B 接 PB9/PB8，E4_A/E4_B 接 PB7/PB6。

- 参数与网络：`E1=PA6/PA7`；`E2=PA4/PA5`；`E3=PB9/PB8`；`E4=PB7/PB6`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A2 U3 MCU_ENC_MxA/B 与 B4-C4 P2/P4/P6/P8 E1~E4

## 复位

### U3 NRST

U3 NRST 连接 CORE_RST，由 R29 10K 上拉至 MCU_3V3 并由 C2 100nF 对地；BOOT0 接 GND。

- 参数与网络：`reset_net=CORE_RST`；`pullup=R29 10K`；`capacitor=C2 100nF`；`boot0=GND`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 B2 U3 NRST/BOOT0/R29/C2

## 内存与 Flash

### 外部存储器

页面未展示 U3 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页完整原理图无独立存储器

## 调试与烧录

### J4 DBG_SWD

J4.1=MCU_3V3，J4.2=MCU_SWCLK，J4.3=MCU_SWDIO，J4.4=CORE_RST，J4.5=GND。

- 参数与网络：`pin_1=MCU_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=CORE_RST`；`pin_5=GND`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 A3 J4 DBG_SWD

## 模拟电路

### ADC1_OUT

VM 经 R3 20K 与 R5 2K 分压，R4 330R 串联形成 ADC1_OUT；D2/D12 B5819W SL 分别钳位至 MCU_3V3 与 GND，ADC1_OUT 接 U3 PB0。

- 参数与网络：`measured_net=VM`；`divider=R3 20K,R5 2K`；`series=R4 330R`；`clamps=D2,D12 B5819W SL`；`mcu_adc=U3 PB0 ADC1_OUT`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 C3 ADC1_OUT 分压/钳位与 A2 U3 PB0

### ADC2_OUT

R24 标注 10mR/1206 串联于 VM 电流路径，U2 INA199A1DCKR 以 IN+/IN- 跨接 R24并输出 ADC2_OUT，ADC2_OUT 接 U3 PB1。

- 参数与网络：`shunt=R24 10mR/1206`；`amplifier=U2 INA199A1DCKR`；`output=ADC2_OUT`；`mcu_adc=U3 PB1`；`decoupling=C16 100nF`
- 证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 D3-D4 R24/U2/ADC2_OUT 与 A2 U3 PB1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module 4EncoderMotor | `mcu=U3 STM32F030C8T6`；`drivers=U4,U5,U6,U7 BL5617`；`motors=4`；`encoders=4`；`monitoring=ADC1_OUT voltage,ADC2_OUT current`；`host_bus=I2C` |
| 核心器件 | U3 | `reference=U3`；`part_number=STM32F030C8T6` |
| 总线 | U3 I2C | `scl=U3 PB10 -> MCU_IIC_SCL -> J2.17`；`sda=U3 PB11 -> MCU_IIC_SDA -> J2.18`；`scl_pullup=R13 4.7K`；`sda_pullup=R12 4.7K`；`rail=MCU_3V3` |
| 总线地址 | 正文中的 I2C 地址 | `documented_default=0x24`；`documented_configurable=true`；`address_on_schematic=null`；`straps_shown=false` |
| GPIO 与控制信号 | 四路 PWM | `M1=U3 PA9`；`M2=U3 PA8`；`M3=U3 PA11`；`M4=U3 PA10`；`distribution=R15/R16,R18/R25,R27/R31,R30/R32 each 10K` |
| GPIO 与控制信号 | 四路方向控制 | `M1=PB14/PB15`；`M2=PB12/PB13`；`M3=PB4/PB5`；`M4=PA15/PB3`；`diodes=D4-D11 1N4148WT` |
| 总线 | U4~U7 电机输出 | `U4=M1-/M1+ -> P1`；`U5=M2-/M2+ -> P3`；`U6=M3-/M3+ -> P5`；`U7=M4-/M4+ -> P7`；`supply=VM` |
| GPIO 与控制信号 | 四组编码器输入 | `E1=PA6/PA7`；`E2=PA4/PA5`；`E3=PB9/PB8`；`E4=PB7/PB6` |
| 接口 | P2/P4/P6/P8 | `P2=E1_A,E1_B,BUS_5V,GND`；`P4=E2_A,E2_B,BUS_5V,GND`；`P6=E3_A,E3_B,BUS_5V,GND`；`P8=E4_A,E4_B,BUS_5V,GND`；`series_resistors=R6/R7,R8/R9,R20/R21,R22/R23 4.7K` |
| 模拟电路 | ADC1_OUT | `measured_net=VM`；`divider=R3 20K,R5 2K`；`series=R4 330R`；`clamps=D2,D12 B5819W SL`；`mcu_adc=U3 PB0 ADC1_OUT` |
| 模拟电路 | ADC2_OUT | `shunt=R24 10mR/1206`；`amplifier=U2 INA199A1DCKR`；`output=ADC2_OUT`；`mcu_adc=U3 PB1`；`decoupling=C16 100nF` |
| 电源 | U1 SY8205FCC | `input=VIN_12V`；`converter=U1 SY8205FCC`；`inductor=L1 0530/10uH`；`output=VCC_5V`；`feedback=R2 220K,R3 33K` |
| 电源 | U9 SY8303AIC | `input=VIN_12V via D3 SS54`；`converter=U9 SY8303AIC`；`inductor=L3 6.8uH`；`output=BUS_5V`；`protection=D17 TVS 5V`；`indicator=D14 RED 0603,R38 2K` |
| 电源 | U10 HX6306P332MR | `input=BUS_5V`；`regulator=U10 HX6306P332MR`；`output=MCU_3V3`；`reference_clamp=U8 TL432` |
| 电源 | HPWR/VIN_12V/VM 开关网络 | `input=J1 HPWR`；`vin_switch=S3,Q4 APM230Q,Q5 DTC114YUA`；`vin_output=VIN_12V`；`vm_switch=S4,Q1/Q2/Q7 APM230Q,Q3/Q6 DTC114YUA`；`motor_rail=VM` |
| 接口 | J2 M5_BUS | `ground=pins2,4,6`；`reset=pin5 CORE_RST`；`3v3=pin11 BUS_3V3`；`i2c=pin17 SCL,pin18 SDA`；`5v=pin27 BUS_5V`；`battery=pin29 BUS_BAT`；`hpwr=pins26,28,30` |
| 调试与烧录 | J4 DBG_SWD | `pin_1=MCU_3V3`；`pin_2=MCU_SWCLK`；`pin_3=MCU_SWDIO`；`pin_4=CORE_RST`；`pin_5=GND` |
| 复位 | U3 NRST | `reset_net=CORE_RST`；`pullup=R29 10K`；`capacitor=C2 100nF`；`boot0=GND` |
| 其他事实 | 正文中的电机能力 | `documented_max_current=3.0A`；`documented_max_power=10W`；`documented_modes=duty,absolute position,speed,forward,reverse,stop,brake`；`ratings_on_schematic=null`；`firmware_required=true` |
| 时钟 | U3 时钟 | `external_crystal_shown=false`；`PF0=not connected`；`PF1=not connected`；`frequency=null` |
| 保护电路 | 电机与编码器接口保护 | `direction_diodes=D4-D11 1N4148WT`；`adc_clamps=D2,D12 B5819W SL`；`bus5_tvs=D17 TVS 5V`；`motor_port_tvs_shown=false`；`encoder_esd_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x24`：产品正文给出默认地址 0x24 并称支持修改，但原理图没有地址配置硬件或 0x24 标注，需由固件协议确认。（证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 I2C 网络无地址标注）
- `other.documented-performance-modes`：产品正文列出最大 3.0A、10W，并声称支持占空比、绝对位置、速度调节、正反转、停止和制动；这些额定值和控制算法未直接标在原理图上。（证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 BL5617 与 MCU 硬件连接，无额定电流/功率或算法标注）
- `clock.mcu-clock-not-shown`：U3 PF0-OSCIN 与 PF1-OSCOUT 未连接，页面未显示外部晶振或时钟频率。（证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 B2 U3 PF0/PF1）
- `protection.motor-ports`：页面显示方向二极管、ADC 钳位、BUS_5V TVS 与输入 SS54，但未显示 M+/M- 或编码器 Grove 端口的专用 TVS/ESD 阵列，端口保护能力需确认。（证据：图 44cdc4d4acae / 第 1 页 / 第 1 页 U4~U7/P1~P8 与保护器件）
- `review.i2c-address`：请通过 M138 固件/协议确认默认 I2C 地址 0x24 及地址修改机制。；原因：原理图无地址配置。
- `review.ratings-modes`：请以 BL5617/PCB 热设计和固件协议确认 3A、10W 额定条件与各控制模式行为。；原因：原理图不包含算法或完整额定条件。
- `review.mcu-clock`：请确认 U3 内部时钟源、频率和固件配置。；原因：PF0/PF1 未接外部晶振。
- `review.port-protection`：请确认四路电机与编码器接口是否在 PCB/BOM 中配置额外 TVS、ESD、过流或短路保护。；原因：当前页面未画端口专用保护阵列。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `44cdc4d4acae8f8aacd78e233dfdaea32a1c66c944a0a5455b0974165c44ab35` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/564/SCH_4EncoderMotor_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/Module-4EncoderMotor.md`

源文档 SHA-256：`90e69092a154071bfae6123a6f7ff73b1e26b322055d795f8aa8e259663af843`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
