# Module 4EncoderMotor v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module 4EncoderMotor v1.1 |
| SKU | M138-V11 |
| 产品 ID | `module-4encodermotor-v1-1-5d1e23f0b5b5` |
| 源文档 | `zh_CN/module/Module_4EncoderMotor_V1.1.md` |

## 概述

Module 4EncoderMotor v1.1 以 U3 STM32F030C8T6 控制 U4~U7 四颗 BL5617，每路具有 PWM、正反向控制、M+/M- 输出和 A/B 编码反馈。v1.1 将每路编码器、电源、地和电机输出统一到 P2/P4/P6/P8 六针接口。U2 INA199A1DCKR 配合 R24 10mΩ 采集电流，ADC1_OUT 采集 VM 电压；U1 SY8205FCC、U9 SY8303AIC、U10 ME6206A33XG 构成 VCC_5V、BUS_5V、MCU_3V3 电源链，I2C 0x24、3A/10W 和 1kHz PWM 等额定/固件参数需另行确认。

## 检索关键词

`Module 4EncoderMotor v1.1`、`M138-V11`、`STM32F030C8T6`、`BL5617`、`INA199A1DCKR`、`SY8205FCC`、`SY8303AIC`、`ME6206A33XG`、`TL432`、`I2C`、`0x24`、`ADC1_OUT`、`ADC2_OUT`、`MCU_PWM_M1`、`MCU_PWM_M2`、`MCU_PWM_M3`、`MCU_PWM_M4`、`MCU_DIR_M1R`、`MCU_DIR_M1F`、`E1_A`、`E1_B`、`E2_A`、`E2_B`、`E3_A`、`E3_B`、`E4_A`、`E4_B`、`Header 6`、`VIN_12V`、`VM`、`VM_IN`、`BUS_5V`、`MCU_3V3`、`1kHz PWM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030C8T6 | 四路电机控制、编码器采集、I2C 通信与模拟监测 MCU | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 A2-B3 MCU 区 U3 STM32F030C8T6 |
| U4/U5/U6/U7 | BL5617 | 四路有刷直流电机 H 桥驱动器 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 A4-B4 4x BDC DRIVERS U4~U7 BL5617 |
| U2 | INA199A1DCKR | 跨 R24 分流电阻测量 VM 电流并输出 ADC2_OUT | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 D3-D4 U2 INA199A1DCKR 与 R24 |
| U1 | SY8205FCC | VIN_12V 到 VCC_5V 的降压转换器 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 B2-C3 U1 SY8205FCC |
| U9 | SY8303AIC | VIN_12V 到 BUS_5V 的降压转换器 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 C2-D3 BUCK_5V U9 SY8303AIC |
| U10 | ME6206A33XG | BUS_5V 到 MCU_3V3 的稳压器 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 D2-D3 U10 ME6206A33XG |
| U8 | TL432 | MCU_3V3 电源网络的并联参考/钳位器件 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 D3-D4 U8 TL432 |
| P2/P4/P6/P8 | Header 6 | 四组统一电机接口，各集成编码器 A/B、BUS_5V、GND、M-/M+ | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 B4-D4 PORTS 区 P2/P4/P6/P8 Header 6 |
| J2 | M5_BUS | I2C、复位、BUS_3V3/BUS_5V/BUS_BAT、HPWR 与 GND 主机接口 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 A1 J2 M5_BUS |
| J4 | DBG_SWD | MCU SWD/复位调试接口 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 A3 J4 DBG_SWD |
| J1 | Header 2 | HPWR/GND 外部电源输入 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 B1 J1 PWR+/PWR- |
| S3/S4 | SW-PWR | VIN_12V 和 VM 电源路径选择开关 | 图 2bf30dbd2838 / 第 1 页 / 第 1 页 B1 POWER&SWITCH 与 C1-D1 VM SWITCH |

## 系统结构

### Module 4EncoderMotor v1.1

U3 通过 I2C 接 J2，驱动 U4~U7 四路 BL5617并采集四组编码器与 ADC1/ADC2；P2/P4/P6/P8 各自整合一套编码器、电源和电机输出。

- 参数与网络：`mcu=U3 STM32F030C8T6`；`drivers=U4-U7 BL5617`；`ports=P2,P4,P6,P8 Header 6`；`monitoring=ADC1_OUT,ADC2_OUT`；`host=I2C`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页完整功能分区

## 电源

### U1 SY8205FCC

U1 从 VIN_12V 经 L1 0530/10uH 生成 VCC_5V，R2 220K/R3 33K 构成反馈。

- 参数与网络：`input=VIN_12V`；`output=VCC_5V`；`inductor=L1 0530/10uH`；`feedback=R2 220K,R3 33K`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 B2-C3 U1 电源

### U9 SY8303AIC

U9 从 VIN_12V 经 D3 SS54 与 L3 6.8uH 生成 BUS_5V，D17 TVS 5V 保护输出，D14/R38 为红色电源指示。

- 参数与网络：`input=VIN_12V via D3 SS54`；`output=BUS_5V`；`inductor=L3 6.8uH`；`protection=D17 TVS 5V`；`indicator=D14 RED 0603,R38 2K`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 C2-D3 BUCK_5V

### U10 ME6206A33XG

U10 VIN 接 BUS_5V、VOUT 输出 MCU_3V3、GND 接地，U8 TL432 并接 MCU_3V3 到 GND。

- 参数与网络：`input=BUS_5V`；`output=MCU_3V3`；`regulator=ME6206A33XG`；`reference_clamp=U8 TL432`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 D2-D4 U10/U8

### VIN_12V/VM 开关

J1 提供 HPWR/GND；S3/Q4/Q5 形成 HPWR 到 VIN_12V 的开关，S4 与 Q1/Q2/Q3/Q6/Q7 网络控制 VM_IN/VM 电机电源路径。

- 参数与网络：`input=J1 HPWR`；`vin_switch=S3,Q4 AP20P30Q,Q5 DTC114YUA`；`vm_switch=S4,Q1/Q2/Q7 AP20P30Q,Q3/Q6 DTC114YUA`；`motor_rail=VM`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 B1 POWER&SWITCH 与 C1-D1 VM SWITCH

## 接口

### P2/P4/P6/P8 Header 6

每个六针口按相同顺序：1=Ex_A，2=Ex_B，3=BUS_5V，4=GND，5=Mx-，6=Mx+；A/B 各经 4.7K 串联电阻。

- 参数与网络：`pin_1=Ex_A`；`pin_2=Ex_B`；`pin_3=BUS_5V`；`pin_4=GND`；`pin_5=Mx-`；`pin_6=Mx+`；`ports=P2/P4/P6/P8`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 B4-D4 PORTS 四个 Header 6

### J2 M5_BUS

J2.2/.4/.6=GND，5=CORE_RST，11=BUS_3V3，17/18=MCU_IIC_SCL/SDA，27=BUS_5V，29=BUS_BAT，26/28/30=HPWR。

- 参数与网络：`ground=2,4,6`；`reset=5`；`3v3=11`；`i2c=17 SCL,18 SDA`；`5v=27`；`battery=29`；`hpwr=26,28,30`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 A1 J2

## 总线

### U3 I2C

U3 PB10/PB11 连接 MCU_IIC_SCL/MCU_IIC_SDA 到 J2.17/J2.18，R13/R12 各 4.7K 上拉至 MCU_3V3。

- 参数与网络：`scl=U3 PB10 -> J2.17`；`sda=U3 PB11 -> J2.18`；`pullups=R13/R12 4.7K`；`rail=MCU_3V3`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 A1-A2 I2C 网络

### U4~U7 输出

U4/U5/U6/U7 OUTR/OUTF 分别连接 M1-/M1+、M2-/M2+、M3-/M3+、M4-/M4+，驱动器 VCC 均接 VM。

- 参数与网络：`U4=M1-/M1+`；`U5=M2-/M2+`；`U6=M3-/M3+`；`U7=M4-/M4+`；`supply=VM`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 A4-B4 U4~U7

## GPIO 与控制信号

### 四路 PWM

MCU_PWM_M1/M2/M3/M4 分别连接 U3 PA9/PA8/PA11/PA10，并通过成对 10K 电阻送往对应 BL5617 INR/INF。

- 参数与网络：`M1=PA9`；`M2=PA8`；`M3=PA11`；`M4=PA10`；`resistors=R15/R16,R18/R25,R27/R31,R30/R32 10K`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 A2-A3 PWM 网络

### 四路方向控制

M1R/F=PB14/PB15，M2R/F=PB12/PB13，M3R/F=PB4/PB5，M4R/F=PA15/PB3；D4~D11 1N4148WT 将方向信号送到 U4~U7。

- 参数与网络：`M1=PB14/PB15`；`M2=PB12/PB13`；`M3=PB4/PB5`；`M4=PA15/PB3`；`diodes=D4-D11 1N4148WT`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 U3 DIR 网络与 U4~U7

### 四组编码器

E1_A/B 接 U3 PA6/PA7，E2_A/B 接 PA4/PA5，E3_A/B 接 PB9/PB8，E4_A/B 接 PB7/PB6。

- 参数与网络：`E1=PA6/PA7`；`E2=PA4/PA5`；`E3=PB9/PB8`；`E4=PB7/PB6`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 U3 MCU_ENC 网络与 P2/P4/P6/P8

## 内存与 Flash

### 外部存储器

页面未展示 U3 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页完整图无存储器

## 调试与烧录

### CORE_RST 与 J4 SWD

U3 NRST 接 CORE_RST，R29 10K 上拉、C2 100nF 对地；J4.1~5 为 MCU_3V3、MCU_SWCLK、MCU_SWDIO、CORE_RST、GND。

- 参数与网络：`reset=R29 10K,C2 100nF`；`swd_pinout=1 MCU_3V3,2 SWCLK,3 SWDIO,4 CORE_RST,5 GND`；`boot0=GND`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 A3-B2 J4/U3 reset

## 模拟电路

### ADC1_OUT

VM 经 R4 330R 和分压网络形成 ADC1_OUT，D2/D12 B5819W SL 对 MCU_3V3/GND 钳位，ADC1_OUT 接 U3 PB0。

- 参数与网络：`measured=VM`；`series=R4 330R`；`clamps=D2,D12 B5819W SL`；`mcu=U3 PB0`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 B3 ADC1_OUT 网络

### ADC2_OUT

R24 10mR/1206 位于 VM 与 VM_IN 之间，U2 INA199A1DCKR 跨接分流电阻并输出 ADC2_OUT 到 U3 PB1。

- 参数与网络：`shunt=R24 10mR/1206`；`amplifier=U2 INA199A1DCKR`；`output=ADC2_OUT`；`mcu=U3 PB1`；`rails=VM/VM_IN`
- 证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 D3-D4 U2/R24

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module 4EncoderMotor v1.1 | `mcu=U3 STM32F030C8T6`；`drivers=U4-U7 BL5617`；`ports=P2,P4,P6,P8 Header 6`；`monitoring=ADC1_OUT,ADC2_OUT`；`host=I2C` |
| 总线 | U3 I2C | `scl=U3 PB10 -> J2.17`；`sda=U3 PB11 -> J2.18`；`pullups=R13/R12 4.7K`；`rail=MCU_3V3` |
| 总线地址 | 正文中的 I2C 地址 | `documented_default=0x24`；`configurable=true`；`address_on_schematic=null` |
| GPIO 与控制信号 | 四路 PWM | `M1=PA9`；`M2=PA8`；`M3=PA11`；`M4=PA10`；`resistors=R15/R16,R18/R25,R27/R31,R30/R32 10K` |
| GPIO 与控制信号 | 四路方向控制 | `M1=PB14/PB15`；`M2=PB12/PB13`；`M3=PB4/PB5`；`M4=PA15/PB3`；`diodes=D4-D11 1N4148WT` |
| GPIO 与控制信号 | 四组编码器 | `E1=PA6/PA7`；`E2=PA4/PA5`；`E3=PB9/PB8`；`E4=PB7/PB6` |
| 接口 | P2/P4/P6/P8 Header 6 | `pin_1=Ex_A`；`pin_2=Ex_B`；`pin_3=BUS_5V`；`pin_4=GND`；`pin_5=Mx-`；`pin_6=Mx+`；`ports=P2/P4/P6/P8` |
| 总线 | U4~U7 输出 | `U4=M1-/M1+`；`U5=M2-/M2+`；`U6=M3-/M3+`；`U7=M4-/M4+`；`supply=VM` |
| 模拟电路 | ADC1_OUT | `measured=VM`；`series=R4 330R`；`clamps=D2,D12 B5819W SL`；`mcu=U3 PB0` |
| 模拟电路 | ADC2_OUT | `shunt=R24 10mR/1206`；`amplifier=U2 INA199A1DCKR`；`output=ADC2_OUT`；`mcu=U3 PB1`；`rails=VM/VM_IN` |
| 电源 | U1 SY8205FCC | `input=VIN_12V`；`output=VCC_5V`；`inductor=L1 0530/10uH`；`feedback=R2 220K,R3 33K` |
| 电源 | U9 SY8303AIC | `input=VIN_12V via D3 SS54`；`output=BUS_5V`；`inductor=L3 6.8uH`；`protection=D17 TVS 5V`；`indicator=D14 RED 0603,R38 2K` |
| 电源 | U10 ME6206A33XG | `input=BUS_5V`；`output=MCU_3V3`；`regulator=ME6206A33XG`；`reference_clamp=U8 TL432` |
| 电源 | VIN_12V/VM 开关 | `input=J1 HPWR`；`vin_switch=S3,Q4 AP20P30Q,Q5 DTC114YUA`；`vm_switch=S4,Q1/Q2/Q7 AP20P30Q,Q3/Q6 DTC114YUA`；`motor_rail=VM` |
| 接口 | J2 M5_BUS | `ground=2,4,6`；`reset=5`；`3v3=11`；`i2c=17 SCL,18 SDA`；`5v=27`；`battery=29`；`hpwr=26,28,30` |
| 调试与烧录 | CORE_RST 与 J4 SWD | `reset=R29 10K,C2 100nF`；`swd_pinout=1 MCU_3V3,2 SWCLK,3 SWDIO,4 CORE_RST,5 GND`；`boot0=GND` |
| 其他事实 | 正文中的额定和控制模式 | `documented_current=3.0A`；`documented_power=10W`；`documented_pwm=1kHz`；`documented_modes=duty,absolute position,speed,forward,reverse,stop,brake`；`on_schematic=null` |
| 时钟 | U3 时钟 | `PF0=NC`；`PF1=NC`；`crystal_shown=false`；`frequency=null` |
| 保护电路 | 统一端口保护 | `direction_diodes=D4-D11`；`adc_clamps=D2,D12`；`bus5_tvs=D17`；`port_tvs_shown=false`；`encoder_esd_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x24`：正文给出默认 0x24 且可修改，原理图没有地址配置硬件或地址标注，需由固件确认。（证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 I2C 网络无地址）
- `other.documented-ratings-modes`：正文列出 3.0A、10W、1kHz PWM 以及占空比/绝对位置/速度/制动等模式；原理图未标这些额定条件或固件算法。（证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 U3/U4~U7 无额定/算法标注）
- `clock.mcu-clock-not-shown`：U3 PF0-OSCIN/PF1-OSCOUT 未连接，页面未显示外部晶振或时钟频率。（证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 U3 PF0/PF1）
- `protection.motor-ports`：图中有方向二极管、ADC 钳位、BUS_5V TVS 和输入 SS54，但 P2/P4/P6/P8 的 M+/M-/编码器线上未画专用 TVS/ESD 阵列。（证据：图 2bf30dbd2838 / 第 1 页 / 第 1 页 P2/P4/P6/P8 与 U4~U7）
- `review.i2c-address`：请确认 v1.1 固件的默认 0x24 地址及修改机制。；原因：原理图无地址硬件。
- `review.ratings-modes`：请确认 3A/10W/1kHz 的测试条件和各闭环控制模式固件行为。；原因：额定与算法未在图纸标注。
- `review.mcu-clock`：请确认 U3 内部时钟源、频率与固件配置。；原因：PF0/PF1 未接外部时钟。
- `review.port-protection`：请确认统一六针端口是否有 PCB/BOM 中未画出的 TVS、ESD、过流或短路保护。；原因：当前图未画端口专用保护阵列。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2bf30dbd28382e04a9a39584cd8fe397c15b9b473c0ee5810f3d7ca613f9a8d5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/566/SCH_4EncoderMotor_V1.1_sch_01.png` |

---

源文档：`zh_CN/module/Module_4EncoderMotor_V1.1.md`

源文档 SHA-256：`914857eb5734037a6b217047d02a33468dc36aedcd3ee60a22ffa972108da77b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
