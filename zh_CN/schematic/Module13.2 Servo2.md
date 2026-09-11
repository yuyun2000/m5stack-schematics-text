# Module13.2 Servo2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 Servo2 |
| SKU | M014-B |
| 产品 ID | `module13-2-servo2-40ec9a04a77c` |
| 源文档 | `zh_CN/module/servo2.md` |

## 概述

Module13.2 Servo2 以 U3 PCA9685 将 M5BUS 的 IIC_SCL/IIC_SDA 转换为 Sv0-Sv15 共 16 路 PWM 控制信号，每路经 100R 阵列电阻连接舵机排针。U1、U2 两颗 SY8368AQQC 从 VBAT_2-3S 分别生成 VOUT1_P5V、VOUT2_P5V，为两组八路接口供电；U4 JW5033 生成 VCC_5V。外部电源由 J1 XT_60 和 S1 接入，UVLO&AutoEnable 电路输出 DCDC_EN 与 nHOST，S2 配合 RP5 配置 PCA9685 地址引脚。

## 检索关键词

`Module13.2 Servo2`、`M014-B`、`PCA9685`、`SY8368AQQC`、`JW5033`、`Si2301`、`S8050`、`SS34`、`1N5819`、`I2C`、`IIC_SCL`、`IIC_SDA`、`PWM`、`Sv0-Sv15`、`A0-A5`、`VBAT_2-3S_IN`、`VBAT_2-3S`、`VOUT1_P5V`、`VOUT2_P5V`、`VCC_5V`、`VCC_3V3`、`DCDC_EN`、`nHOST`、`XT_60`、`M5BUS`、`S1`、`S2`、`100R`、`10K`、`3.3uH`、`ServoCon`、`UVLO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SY8368AQQC | 将 VBAT_2-3S 降压为 VOUT1_P5V 的舵机电源转换器 | 图 840a6d377e6b / 第 1 页 / 第1页 A1-A2，IN Power Buck DC-DC1 区 U1 SY8368AQQC、L1 与 VOUT1_P5V |
| U2 | SY8368AQQC | 将 VBAT_2-3S 降压为 VOUT2_P5V 的舵机电源转换器 | 图 840a6d377e6b / 第 1 页 / 第1页 A2-A3，IN Power Buck DC-DC2 区 U2 SY8368AQQC、L2 与 VOUT2_P5V |
| U3 | PCA9685 | 通过 I2C 控制 LED0-LED15 共 16 路 PWM 输出 | 图 840a6d377e6b / 第 1 页 / 第1页 B2-B3，PWM 区 U3 PCA9685，左侧控制引脚与右侧 LED0-LED15 |
| U4 | JW5033 | 将 VBAT_2-3S 降压为系统电源 VCC_5V | 图 840a6d377e6b / 第 1 页 / 第1页 B1-B2，Sys Buck DC-DC 区 U4 JW5033、D2、L3 与 VCC_5V |
| J1 | XT_60 | VBAT_2-3S_IN 与 GND 的外部电源输入连接器 | 图 840a6d377e6b / 第 1 页 / 第1页 A4，Battery IN 区 J1 XT_60，PVCC pin 1 与 PGND pin 2 |
| S1 | SW-TH_3P-P4.70_L11.1-W12.7 | 外部电源输入与 VBAT_2-3S 之间的三脚电源开关 | 图 840a6d377e6b / 第 1 页 / 第1页 A4，Power SW 区 S1，pin 1 标注 VBAT_2-3S_IN，pin 2 标注 VBAT_2-3S |
| Q1,Q2,D1 | Si2301; S8050; 1N5819 | 组成标注为 UVLO&AutoEnable 的 DCDC_EN 与 nHOST 控制电路 | 图 840a6d377e6b / 第 1 页 / 第1页 A3-A4，UVLO&AutoEnable 区 Q1、Q2、D1 及 DCDC_EN/nHOST 网络 |
| D2 | SS34 | 串接在 VBAT_2-3S 与 U4 VIN 输入路径上的二极管 | 图 840a6d377e6b / 第 1 页 / 第1页 B1，Sys Buck DC-DC 输入端 D2 SS34 |
| L1,L2 | 3.3uH/SPM6530T/MCW-0630 | U1、U2 两路舵机降压电源的输出电感 | 图 840a6d377e6b / 第 1 页 / 第1页 A1-A3，U1 LX 后 L1 与 U2 LX 后 L2，均标注 3.3uH/SPM6530T/MCW-0630 |
| L3 | 3.3uH/L4012 | U4 系统降压电源的输出电感 | 图 840a6d377e6b / 第 1 页 / 第1页 B1-B2，U4 SW 后 L3 3.3uH/L4012 至 VCC_5V |
| LED1,R9; LED2,R10 | GREEN,4.7K; GREEN,4.7K | 分别指示 VOUT1_P5V 与 VOUT2_P5V 电源状态 | 图 840a6d377e6b / 第 1 页 / 第1页 A1 与 A2，R9/LED1、R10/LED2 从对应 VOUTx_P5V 接至 GND |
| RP1,RP2,RP3,RP4 | 100R resistor arrays | 串接于 PCA9685 LED0-LED15 与 Sv0-Sv15 之间 | 图 840a6d377e6b / 第 1 页 / 第1页 B3，U3 右侧 RP1-RP4 均标注 100R，连接 LED0-LED15 与 Sv0-Sv15 |
| S2,RP5 | 3-position switch; 4.7K resistor array | 配置 PCA9685 的 A0-A2 地址引脚；RP5 提供三路下拉并保留一个未用电阻 | 图 840a6d377e6b / 第 1 页 / 第1页 B2，U3 左侧 S2 pins 1-6、RP5 4.7K、A0-A2 与 GND/VCC_3V3 |
| R16,R17 | 10K | 将 IIC_SCL 与 IIC_SDA 上拉到 VCC_3V3 | 图 840a6d377e6b / 第 1 页 / 第1页 B2，U3 左上 R16/R17 均标注 10K，连接 VCC_3V3 与 IIC_SCL/IIC_SDA |
| J3A,J2B,J2C | THT_Male_P arrays | Sv0-Sv7、VOUT2_P5V 与 GND 组成的八路三针舵机接口组 | 图 840a6d377e6b / 第 1 页 / 第1页 B4，ServoCon 上组 J3A 信号、J2B VOUT2_P5V、J2C GND |
| J2A,J3B,J3C | THT_Male_P arrays | Sv8-Sv15、VOUT1_P5V 与 GND 组成的八路三针舵机接口组 | 图 840a6d377e6b / 第 1 页 / 第1页 B4，ServoCon 下组 J2A 信号、J3B VOUT1_P5V、J3C GND |
| BUS1 | M5BUS | 30 针主机堆叠接口，连接 I2C、VCC_3V3、VCC_5V、HPWR/VBAT_2-3S 与 GND | 图 840a6d377e6b / 第 1 页 / 第1页 C4-D4，BUS1 M5BUS pins 1-30 及外接电源和 IIC 网络 |

## 系统结构

### Module13.2 Servo2 系统架构

U3 PCA9685 通过 M5BUS 的 IIC_SCL/IIC_SDA 产生 Sv0-Sv15 共 16 路控制信号；U1/U2 分别生成两组舵机 5V 电源，U4 生成 VCC_5V，J1/S1 与 BUS1 提供外部和主机侧电源连接。

- 参数与网络：`pwm_controller=U3 PCA9685`；`channels=16`；`servo_bucks=U1/U2 SY8368AQQC`；`system_buck=U4 JW5033`；`external_input=J1 XT_60 via S1`；`host_interface=BUS1 M5BUS`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页完整单页，IN Power Buck DC-DC1/2、Sys Buck DC-DC、PWM、ServoCon、Battery IN 与 M5 BUS 分区

## 核心器件

### PCA9685 供电、控制与时钟引脚

U3 pin 28/VDD 接 VCC_3V3，pin 14/GND 接地，pin 23/OE 与 pin 25/EXTCLK 均接 GND；C15 470nF/16V 与 C16 1uF/16V 为 VDD 对地电容。

- 参数与网络：`supply=pin 28/VDD -> VCC_3V3`；`ground=pin 14/GND -> GND`；`output_enable=pin 23/OE -> GND`；`external_clock=pin 25/EXTCLK -> GND`；`decoupling=C15 470nF/16V,C16 1uF/16V`；`i2c=pin 26/SCL,pin 27/SDA`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B2，U3 左侧 VDD/GND/OE/EXTCLK/SCL/SDA 与 C15/C16

### PCA9685 输出串联电阻

RP1、RP2、RP3、RP4 均标注 100R，分别覆盖 LED0-LED3、LED4-LED7、LED8-LED11、LED12-LED15 到 Sv0-Sv15 的串联路径。

- 参数与网络：`rp1=LED0-LED3 -> Sv0-Sv3`；`rp2=LED4-LED7 -> Sv4-Sv7`；`rp3=LED8-LED11 -> Sv8-Sv11`；`rp4=LED12-LED15 -> Sv12-Sv15`；`value=100R`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B3，PCA9685 右侧四组电阻阵列 RP1-RP4 与 100R 标注

### I2C 上拉电阻

R16 与 R17 均标注 10K，分别将 IIC_SCL 与 IIC_SDA 上拉到 VCC_3V3。

- 参数与网络：`scl_pullup=R16 10K -> VCC_3V3`；`sda_pullup=R17 10K -> VCC_3V3`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B2，U3 左上 R16/R17 的 10K 标注与 IIC_SCL/IIC_SDA 网络

## 电源

### XT60 外部电源与开关

J1 XT_60 的 pin 1/PVCC 接 VBAT_2-3S_IN，pin 2/PGND 接 GND；S1 pin 1 接 VBAT_2-3S_IN，pin 2 接 VBAT_2-3S，pin 3 未见外接网络。

- 参数与网络：`connector=J1 XT_60`；`positive=pin 1/PVCC -> VBAT_2-3S_IN`；`negative=pin 2/PGND -> GND`；`switch_input=S1 pin 1 -> VBAT_2-3S_IN`；`switch_output=S1 pin 2 -> VBAT_2-3S`；`switch_pin3_external_net=null`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 A4，Power SW 的 S1 pins 1-3 与 Battery IN 的 J1 pins 1-2

### U1 VOUT1_P5V 降压

U1 SY8368AQQC 由 VBAT_2-3S 供电，EN 接 nHOST，LX 经 L1 3.3uH/SPM6530T/MCW-0630 输出 VOUT1_P5V；R7 36K/R13 4.7K 构成反馈分压，R4 1K/C7 220pF/50V 接入反馈网络。

- 参数与网络：`converter=U1 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`bootstrap=C3 100nF/50V`；`inductor=L1 3.3uH/SPM6530T/MCW-0630`；`output=VOUT1_P5V`；`feedback=R7 36K,R13 4.7K,R4 1K,C7 220pF/50V`；`output_caps=C9 1000uF/10V,C10 22uF/6.3V,C11 470nF/16V`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 A1-A2，IN Power Buck DC-DC1 的 U1、C3、L1、R4/R7/R13、C7 与 C9-C11

### U2 VOUT2_P5V 降压

U2 SY8368AQQC 由 VBAT_2-3S 供电，EN 接 nHOST，LX 经 L2 3.3uH/SPM6530T/MCW-0630 输出 VOUT2_P5V；R6 36K/R14 4.7K 构成反馈分压，R5 1K/C8 220pF/50V 接入反馈网络。

- 参数与网络：`converter=U2 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`bootstrap=C4 100nF/50V`；`inductor=L2 3.3uH/SPM6530T/MCW-0630`；`output=VOUT2_P5V`；`feedback=R6 36K,R14 4.7K,R5 1K,C8 220pF/50V`；`output_caps=C12 1000uF/10V,C13 22uF/6.3V,C14 470nF/16V`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 A2-A3，IN Power Buck DC-DC2 的 U2、C4、L2、R5/R6/R14、C8 与 C12-C14

### U4 VCC_5V 系统降压

VBAT_2-3S 经 D2 SS34 接到 U4 JW5033 VIN，U4 EN 接 DCDC_EN，SW 经 L3 3.3uH/L4012 输出 VCC_5V；R18 330K/R19 62K 构成反馈分压。

- 参数与网络：`input=VBAT_2-3S -> D2 SS34 -> U4 VIN pin 3`；`converter=U4 JW5033`；`enable=DCDC_EN -> pin 5/EN`；`bootstrap=C17 100nF/50V`；`inductor=L3 3.3uH/L4012`；`output=VCC_5V`；`feedback=R18 330K,R19 62K`；`output_caps=C20 470nF/16V,C21 22uF/6.3V`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B1-B2，Sys Buck DC-DC 的 D2、U4、C17、L3、R18/R19 与 C20/C21

### UVLO 与自动使能网络

标注为 UVLO&AutoEnable 的电路由 Q1 Si2301、Q2 S8050、D1 1N5819 和 R1/R2/R3/R8/R11/R12/R15 构成；该区引出 DCDC_EN 到 U4 EN，并引出 nHOST 到 U1/U2 EN。

- 参数与网络：`mosfet=Q1 Si2301`；`transistor=Q2 S8050`；`diode=D1 1N5819`；`resistors=R1 10K,R2 10K,R3 10K,R8 100K,R11 200K,R12 10K,R15 20K`；`system_enable=DCDC_EN -> U4 pin 5/EN`；`servo_enable=nHOST -> U1/U2 pin 1/EN`；`domains=VBAT_2-3S,VCC_3V3,GND`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 A3-A4，UVLO&AutoEnable 全区；A1-A3 的 U1/U2 nHOST；B1 的 U4 DCDC_EN

### 电源轨附加电容

页面下部为 VBAT_2-3S_IN、VBAT_2-3S、VOUT1_P5V、VOUT2_P5V 和 VCC_5V 配置附加对地电容。

- 参数与网络：`input_cap=C22 22uF/16V on VBAT_2-3S_IN`；`battery_caps=C23,C24,C26,C27 22uF/16V on VBAT_2-3S`；`servo_caps=C28 22uF/6.3V on VOUT1_P5V; C29 22uF/6.3V on VOUT2_P5V`；`system_5v_cap=C25 22uF/6.3V on VCC_5V`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 C3-C4，C22-C29 与 C25 的网络名、容量、耐压和 GND

### BUS1 电源针脚

BUS1 pins 2/4/6 的 HPWR 接 VBAT_2-3S，pin 3/5V 接 VCC_5V，pin 19/3.3V 接 VCC_3V3，pins 26/28/30 接 GND；pin 1/BAT 标为未连接。

- 参数与网络：`hpwr=pins 2,4,6 -> VBAT_2-3S`；`five_volt=pin 3 -> VCC_5V`；`three3=pin 19 -> VCC_3V3`；`ground=pins 26,28,30 -> GND`；`battery_pin=pin 1/BAT no-connect`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 C4-D4，BUS1 的 HPWR/5V/3.3V/GND/BAT 引脚与外部网络

## 接口

### Sv0-Sv7 舵机接口组

J3A 将 Sv0-Sv7 依次接到 pins 22/19/16/13/10/7/4/1；J2B 的 pins 2/5/8/11/14/17/20/23 共接 VOUT2_P5V，J2C 的 pins 3/6/9/12/15/18/21/24 共接 GND。

- 参数与网络：`signals=Sv0->22,Sv1->19,Sv2->16,Sv3->13,Sv4->10,Sv5->7,Sv6->4,Sv7->1`；`supply=J2B pins 2,5,8,11,14,17,20,23 -> VOUT2_P5V`；`ground=J2C pins 3,6,9,12,15,18,21,24 -> GND`；`channels=8`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B4，ServoCon 上组 J3A/J2B/J2C 的逐行信号、电源、地和针号

### Sv8-Sv15 舵机接口组

J2A 将 Sv8-Sv15 依次接到 pins 22/19/16/13/10/7/4/1；J3B 的 pins 2/5/8/11/14/17/20/23 共接 VOUT1_P5V，J3C 的 pins 3/6/9/12/15/18/21/24 共接 GND。

- 参数与网络：`signals=Sv8->22,Sv9->19,Sv10->16,Sv11->13,Sv12->10,Sv13->7,Sv14->4,Sv15->1`；`supply=J3B pins 2,5,8,11,14,17,20,23 -> VOUT1_P5V`；`ground=J3C pins 3,6,9,12,15,18,21,24 -> GND`；`channels=8`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B4，ServoCon 下组 J2A/J3B/J3C 的逐行信号、电源、地和针号

## 总线

### PCA9685 I2C 总线

BUS1 pin 13/G22/IIC_SCL 连接 IIC_SCL 到 U3 pin 26/SCL，BUS1 pin 14/G21/IIS_SDA 连接 IIC_SDA 到 U3 pin 27/SDA；R16/R17 各 10K 将两条总线上拉到 VCC_3V3。

- 参数与网络：`controller=M5 host via BUS1`；`device=U3 PCA9685`；`scl=BUS1 pin 13 -> IIC_SCL -> U3 pin 26/SCL`；`sda=BUS1 pin 14 -> IIC_SDA -> U3 pin 27/SDA`；`pullups=R16 10K,R17 10K to VCC_3V3`；`logic_supply=VCC_3V3`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B2 的 U3 pins 26/27 与 R16/R17；C4-D4 的 BUS1 pins 13/14

## 总线地址

### PCA9685 地址硬件配置

S2 的三路开关分别把 U3 A0、A1、A2 接到 VCC_3V3；RP5 的三路 4.7K 电阻将 A0-A2 下拉到 GND，阵列另一电阻两端均标为未连接；A3、A4、A5 直接接 GND。

- 参数与网络：`adjustable_bits=A0 pin 1,A1 pin 2,A2 pin 3`；`switch=S2 pins 1-3 to A0-A2; pins 4-6 to VCC_3V3`；`pulldowns=three RP5 4.7K elements on A0-A2 to GND`；`unused_array_element=true`；`fixed_low_bits=A3 pin 4,A4 pin 5,A5 pin 24 -> GND`；`numeric_address_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B2，S2 pins 1-6、RP5 四电阻阵列、U3 A0-A5 与 GND/VCC_3V3

## GPIO 与控制信号

### 16 路 PWM 信号映射

U3 LED0-LED15 分别经 RP1-RP4 的 100R 电阻形成 Sv0-Sv15，共 16 路舵机控制信号。

- 参数与网络：`channels_0_7=LED0-LED7 -> RP1/RP2 100R -> Sv0-Sv7`；`channels_8_15=LED8-LED15 -> RP3/RP4 100R -> Sv8-Sv15`；`channel_count=16`；`series_resistance=100R`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B3，U3 LED0-LED15、RP1-RP4 100R 与 Sv0-Sv15

### 双路舵机电源指示灯

VOUT1_P5V 经 R9 4.7K 与 LED1 GREEN 接 GND；VOUT2_P5V 经 R10 4.7K 与 LED2 GREEN 接 GND。

- 参数与网络：`channel1=VOUT1_P5V -> R9 4.7K -> LED1 GREEN -> GND`；`channel2=VOUT2_P5V -> R10 4.7K -> LED2 GREEN -> GND`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 A1 与 A2，U1/U2 左侧 R9/LED1 与 R10/LED2 支路

## 时钟

### PCA9685 外部时钟连接

U3 PCA9685 的 pin 25/EXTCLK 直接接 GND；完整单页未见晶体、谐振器或振荡器位号。

- 参数与网络：`pca9685_extclk=pin 25/EXTCLK -> GND`；`crystal_visible=false`；`resonator_visible=false`；`oscillator_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B2，U3 pin 25/EXTCLK 至 GND；完整单页无 Y/X 时钟位号

## 保护电路

### 可见二极管与保护器件范围

D2 SS34 串在 VBAT_2-3S 至 U4 VIN 路径，D1 1N5819 位于 UVLO&AutoEnable 区；完整单页未见保险丝、TVS 或舵机信号 ESD 器件位号。

- 参数与网络：`series_diode=D2 SS34`；`uvlo_diode=D1 1N5819`；`fuse_visible=false`；`tvs_visible=false`；`servo_esd_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页完整单页，B1 的 D2、A3-A4 的 D1 及 Battery IN/ServoCon 外围

## 关键网络

### 两组舵机电源分配

VOUT2_P5V 供给 Sv0-Sv7 对应接口组的 J2B，VOUT1_P5V 供给 Sv8-Sv15 对应接口组的 J3B；两组回路分别经 J2C、J3C 接 GND。

- 参数与网络：`group_0_7=VOUT2_P5V -> J2B; GND -> J2C`；`group_8_15=VOUT1_P5V -> J3B; GND -> J3C`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页 B4，ServoCon 上下两组的 VOUT2_P5V/VOUT1_P5V 与 GND 母线

## 内存与 Flash

### 存储器与内存可见性

完整单页未绘出 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页完整单页全部器件，无存储器件或存储接口位号

## 调试与烧录

### 复位、BOOT 与调试可见性

完整单页未绘出 MCU、复位按键、BOOT、SWD、JTAG 或专用调试连接器；可见数字控制接口为 PCA9685 的 I2C、地址开关和 PWM 输出。

- 参数与网络：`mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页完整单页全部功能分区、器件位号与连接器

## 其他事实

### 其他总线与功能链路可见性

完整单页未绘出 SPI、UART、CAN、RS-485、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；可见功能接口为 I2C、16 路 PWM、舵机电源和 M5BUS 电源网络。

- 参数与网络：`spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 840a6d377e6b / 第 1 页 / 第1页完整单页全部功能分区与网络标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 Servo2 系统架构 | `pwm_controller=U3 PCA9685`；`channels=16`；`servo_bucks=U1/U2 SY8368AQQC`；`system_buck=U4 JW5033`；`external_input=J1 XT_60 via S1`；`host_interface=BUS1 M5BUS` |
| 电源 | XT60 外部电源与开关 | `connector=J1 XT_60`；`positive=pin 1/PVCC -> VBAT_2-3S_IN`；`negative=pin 2/PGND -> GND`；`switch_input=S1 pin 1 -> VBAT_2-3S_IN`；`switch_output=S1 pin 2 -> VBAT_2-3S`；`switch_pin3_external_net=null` |
| 电源 | U1 VOUT1_P5V 降压 | `converter=U1 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`bootstrap=C3 100nF/50V`；`inductor=L1 3.3uH/SPM6530T/MCW-0630`；`output=VOUT1_P5V`；`feedback=R7 36K,R13 4.7K,R4 1K,C7 220pF/50V`；`output_caps=C9 1000uF/10V,C10 22uF/6.3V,C11 470nF/16V` |
| 电源 | U2 VOUT2_P5V 降压 | `converter=U2 SY8368AQQC`；`input=VBAT_2-3S`；`enable=nHOST`；`bootstrap=C4 100nF/50V`；`inductor=L2 3.3uH/SPM6530T/MCW-0630`；`output=VOUT2_P5V`；`feedback=R6 36K,R14 4.7K,R5 1K,C8 220pF/50V`；`output_caps=C12 1000uF/10V,C13 22uF/6.3V,C14 470nF/16V` |
| 电源 | U4 VCC_5V 系统降压 | `input=VBAT_2-3S -> D2 SS34 -> U4 VIN pin 3`；`converter=U4 JW5033`；`enable=DCDC_EN -> pin 5/EN`；`bootstrap=C17 100nF/50V`；`inductor=L3 3.3uH/L4012`；`output=VCC_5V`；`feedback=R18 330K,R19 62K`；`output_caps=C20 470nF/16V,C21 22uF/6.3V` |
| 电源 | UVLO 与自动使能网络 | `mosfet=Q1 Si2301`；`transistor=Q2 S8050`；`diode=D1 1N5819`；`resistors=R1 10K,R2 10K,R3 10K,R8 100K,R11 200K,R12 10K,R15 20K`；`system_enable=DCDC_EN -> U4 pin 5/EN`；`servo_enable=nHOST -> U1/U2 pin 1/EN`；`domains=VBAT_2-3S,VCC_3V3,GND` |
| 电源 | 电源轨附加电容 | `input_cap=C22 22uF/16V on VBAT_2-3S_IN`；`battery_caps=C23,C24,C26,C27 22uF/16V on VBAT_2-3S`；`servo_caps=C28 22uF/6.3V on VOUT1_P5V; C29 22uF/6.3V on VOUT2_P5V`；`system_5v_cap=C25 22uF/6.3V on VCC_5V` |
| 总线 | PCA9685 I2C 总线 | `controller=M5 host via BUS1`；`device=U3 PCA9685`；`scl=BUS1 pin 13 -> IIC_SCL -> U3 pin 26/SCL`；`sda=BUS1 pin 14 -> IIC_SDA -> U3 pin 27/SDA`；`pullups=R16 10K,R17 10K to VCC_3V3`；`logic_supply=VCC_3V3` |
| 总线地址 | PCA9685 地址硬件配置 | `adjustable_bits=A0 pin 1,A1 pin 2,A2 pin 3`；`switch=S2 pins 1-3 to A0-A2; pins 4-6 to VCC_3V3`；`pulldowns=three RP5 4.7K elements on A0-A2 to GND`；`unused_array_element=true`；`fixed_low_bits=A3 pin 4,A4 pin 5,A5 pin 24 -> GND`；`numeric_address_visible=false` |
| GPIO 与控制信号 | 16 路 PWM 信号映射 | `channels_0_7=LED0-LED7 -> RP1/RP2 100R -> Sv0-Sv7`；`channels_8_15=LED8-LED15 -> RP3/RP4 100R -> Sv8-Sv15`；`channel_count=16`；`series_resistance=100R` |
| 接口 | Sv0-Sv7 舵机接口组 | `signals=Sv0->22,Sv1->19,Sv2->16,Sv3->13,Sv4->10,Sv5->7,Sv6->4,Sv7->1`；`supply=J2B pins 2,5,8,11,14,17,20,23 -> VOUT2_P5V`；`ground=J2C pins 3,6,9,12,15,18,21,24 -> GND`；`channels=8` |
| 接口 | Sv8-Sv15 舵机接口组 | `signals=Sv8->22,Sv9->19,Sv10->16,Sv11->13,Sv12->10,Sv13->7,Sv14->4,Sv15->1`；`supply=J3B pins 2,5,8,11,14,17,20,23 -> VOUT1_P5V`；`ground=J3C pins 3,6,9,12,15,18,21,24 -> GND`；`channels=8` |
| 核心器件 | PCA9685 供电、控制与时钟引脚 | `supply=pin 28/VDD -> VCC_3V3`；`ground=pin 14/GND -> GND`；`output_enable=pin 23/OE -> GND`；`external_clock=pin 25/EXTCLK -> GND`；`decoupling=C15 470nF/16V,C16 1uF/16V`；`i2c=pin 26/SCL,pin 27/SDA` |
| 核心器件 | PCA9685 输出串联电阻 | `rp1=LED0-LED3 -> Sv0-Sv3`；`rp2=LED4-LED7 -> Sv4-Sv7`；`rp3=LED8-LED11 -> Sv8-Sv11`；`rp4=LED12-LED15 -> Sv12-Sv15`；`value=100R` |
| 核心器件 | I2C 上拉电阻 | `scl_pullup=R16 10K -> VCC_3V3`；`sda_pullup=R17 10K -> VCC_3V3` |
| 电源 | BUS1 电源针脚 | `hpwr=pins 2,4,6 -> VBAT_2-3S`；`five_volt=pin 3 -> VCC_5V`；`three3=pin 19 -> VCC_3V3`；`ground=pins 26,28,30 -> GND`；`battery_pin=pin 1/BAT no-connect` |
| GPIO 与控制信号 | 双路舵机电源指示灯 | `channel1=VOUT1_P5V -> R9 4.7K -> LED1 GREEN -> GND`；`channel2=VOUT2_P5V -> R10 4.7K -> LED2 GREEN -> GND` |
| 关键网络 | 两组舵机电源分配 | `group_0_7=VOUT2_P5V -> J2B; GND -> J2C`；`group_8_15=VOUT1_P5V -> J3B; GND -> J3C` |
| 保护电路 | 可见二极管与保护器件范围 | `series_diode=D2 SS34`；`uvlo_diode=D1 1N5819`；`fuse_visible=false`；`tvs_visible=false`；`servo_esd_visible=false` |
| 时钟 | PCA9685 外部时钟连接 | `pca9685_extclk=pin 25/EXTCLK -> GND`；`crystal_visible=false`；`resonator_visible=false`；`oscillator_visible=false` |
| 调试与烧录 | 复位、BOOT 与调试可见性 | `mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他总线与功能链路可见性 | `spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `840a6d377e6bdda08bab3edbe6f1ac3fb21fc898f69a788bd48abea175801971` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/M014-B_Module13.2_Servo2_Sche_page_01.png` |

---

源文档：`zh_CN/module/servo2.md`

源文档 SHA-256：`c30717e9dc831591c88c24e0809ba88d6aec355f6da9fb6e12d4fd0e340b90e0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
