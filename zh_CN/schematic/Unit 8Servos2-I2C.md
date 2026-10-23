# Unit 8Servos2-I2C 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 8Servos2-I2C |
| SKU | U222 |
| 产品 ID | `unit-8servos2-i2c-781bab2970d2` |
| 源文档 | `zh_CN/unit/Unit_8Servos2-I2C.md` |

## 概述

Unit 8Servos2-I2C 是 9~24V 供电的 8 路舵机驱动单元：DC 输入经 PTC/TVS 保护后由 SY8303AIC 降压到 5V，再由 SSP7615-33 产生 3.3V；STM32G031G8U6 输出 8 路 PWM 控制 4 个 2×3 舵机排针，INA199A1DCKR 通过 10mΩ 采样电阻监测舵机电流；两个 GROVE 口均并入 I2C1，并用 SKAR-16 16 位旋钮设置地址。

## 检索关键词

`Unit 8Servos2-I2C`、`U222`、`SY8303AIC`、`SSP7615-33`、`INA199A1DCKR`、`STM32G031G8U6`、`FXL0530-6R8-M`、`DC-044`、`SMD1812-200-30`、`SMF30CA`、`SERVOS_5V`、`VCC_5V`、`VCC_3V3`、`TIM2_CH1`、`TIM2_CH4`、`TIM3_CH1`、`TIM3_CH4`、`ADC1_IN4`、`ADC1_IN5`、`I2C`、`UART`、`SWD`、`SKAR-16`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SY8303AIC | 同步降压控制器，DC 9~24V 转 5V/3A | 图 efb4d0734400 / 第 1 页 / A 区 DC-DC：U1 型号与 IN/EN/BS/LX/FB/FS 引脚 |
| U2 | SSP7615-33 | 5V 转 3.3V LDO，最大 300mA | 图 efb4d0734400 / 第 1 页 / A 区：U2 SSP7615-33 与 VIN/OUT/EN/GND_EP |
| U3 | INA199A1DCKR | 高边电流检测放大器，监测舵机供电电流 | 图 efb4d0734400 / 第 1 页 / B 区：U3 INA199A1DCKR 与 IN+/IN-/OUT/REF 引脚 |
| U5 | STM32G031G8U6 | 主控 MCU，产生 8 路舵机 PWM 并处理通信/采样 | 图 efb4d0734400 / 第 1 页 / D 区：U5 型号与 1~28 脚 |
| U4 | 未标注 | 丝印未标注型号的 6 脚器件位置 | 图 efb4d0734400 / 第 1 页 / C 区：U4 位置 |
| DC1 | DC-044 | DC 电源输入插座 | 图 efb4d0734400 / 第 1 页 / A 区左侧：DC1 DC-044 |
| F1 | SMD1812-200-30 | 自恢复保险丝（Ihold 2A / Itrip 4A） | 图 efb4d0734400 / 第 1 页 / A 区：F1 与 2A/4A 标注 |
| DR1 | SMF30CA | DC 输入端 TVS 保护 | 图 efb4d0734400 / 第 1 页 / A 区：DR1 SMF30CA |
| L1 | FXL0530-6R8-M | 降压电感 6.8uH | 图 efb4d0734400 / 第 1 页 / A 区：L1 FXL0530-6R8-M |
| R4 | 10mR/1% | 舵机供电电流采样电阻 | 图 efb4d0734400 / 第 1 页 / B 区：R4 10mR/1% |
| JP4 / JP5 / JP1 / JP6 | 2x3 servo header | 4 个 2×3 舵机排针，每口 2 路，共 8 路；针序 GND/5V/SIG | 图 efb4d0734400 / 第 1 页 / B/C 区右侧：JP4、JP5、JP1、JP6 |
| JP2 / JP3 | 4-pin header | 链式/总线接口：1=GND、2=VCC_5V、3=D2、4=D1 | 图 efb4d0734400 / 第 1 页 / B 区左侧：JP2(IN) 与 JP3(OUT) |
| DR2-DR5 | ESD5311 | GROVE D1/D2 的 ESD 保护 | 图 efb4d0734400 / 第 1 页 / B 区：DR2~DR5 ESD5311 |
| R19 / R23 | 10K/1% | SERVOS_5V 分压到 ADC1_IN5 | 图 efb4d0734400 / 第 1 页 / C 区：R19/R23 10K 分压 |
| R21 / R22 | 2.2K/5% | SDA/RX1 与 SCL/TX1 上拉到 VCC_3V3 | 图 efb4d0734400 / 第 1 页 / C 区：R21/R22 2.2K |
| R14 | 4.7K/5% | PA8 驱动 LED1 绿色指示灯限流 | 图 efb4d0734400 / 第 1 页 / C 区：R14 4.7K 与 LED1 |
| R20 / C18 | 10K / 100nF | STM_RST 上拉与滤波 | 图 efb4d0734400 / 第 1 页 / D 区左侧：R20 10K、C18 100nF |
| SW1 | SKAR-16 | 16 位旋转编码开关，设置 I2C 地址 | 图 efb4d0734400 / 第 1 页 / D 区右侧：SW1 SKAR-16 与真值表 |
| R15-R18 | 10K/1% | 地址位 PB3/PB4/PB5/PB8 上拉 | 图 efb4d0734400 / 第 1 页 / D 区右侧：R15~R18 10K |
| R8-R11 | 0R / NC | I2C 模式下 R8/R9=0R 将 GROVE2 并入 I2C，R10/R11=NC | 图 efb4d0734400 / 第 1 页 / C 区：R8~R11 与 Design Note |

## 系统结构

### U5

U5(STM32G031G8U6)：VDD/VDDA(3)=VCC_3V3，VSS/VSSA(4)=GND，PF2-NRST(5)=STM_RST；C5 100nF/50V 去耦。

- 参数与网络：`vdd=VCC_3V3`；`nrst=STM_RST`
- 证据：图 efb4d0734400 / 第 1 页 / D 区 U5 与 C5

## 电源

### U1

U1(SY8303AIC) 将 DC_IN 降压到 5V：IN(5) 接输入，EN(8) 使能，LX(6) 经 L1 到输出，FB(1) 反馈，FS(2) 接 R2(200K) 地，BS(7) 经 C1 100nF 自举；R1=220K、R3=30K 决定 Vout≈5.0V。

- 参数与网络：`vin=DC_IN`；`vout=VCC_5V`；`l1=FXL0530-6R8-M`；`r1=220K`；`r3=30K`；`iout_max=3A`
- 证据：图 efb4d0734400 / 第 1 页 / A 区 DC-DC

### U2

U2(SSP7615-33) 将 VCC_5V 转为 VCC_3V3：VIN(4)=5V、EN(3)=5V、OUT(1)=3.3V、GND(2)/GND_EP(0) 接地；C6/C7 各 1uF/25V。

- 参数与网络：`vin=VCC_5V`；`vout=VCC_3V3`；`iout_max=300mA`
- 证据：图 efb4d0734400 / 第 1 页 / A 区 SSP7615-33

## 接口

### U5

8 路舵机 PWM 映射：PA0=TIM2_CH1、PA1=TIM2_CH2、PA2=TIM2_CH3、PA3=TIM2_CH4、PA6=TIM3_CH1、PA7=TIM3_CH2、PB0=TIM3_CH3、PB1=TIM3_CH4。

- 参数与网络：`PA0=TIM2_CH1`；`PA1=TIM2_CH2`；`PA2=TIM2_CH3`；`PA3=TIM2_CH4`；`PA6=TIM3_CH1`；`PA7=TIM3_CH2`；`PB0=TIM3_CH3`；`PB1=TIM3_CH4`
- 证据：图 efb4d0734400 / 第 1 页 / D 区 U5 引脚与 B/C 区舵机接口

### JP4/JP5/JP1/JP6

4 个 2×3 排针各提供 2 路舵机，针序为 GND/5V/SIG；SERVOS_5V 由 C16/C17 10uF/35V 与 E2 100uF/35V 滤波。

- 参数与网络：`connectors=JP4,JP5,JP1,JP6`；`pins=GND/5V/SIG`；`bulk=E2 100uF/35V`
- 证据：图 efb4d0734400 / 第 1 页 / B/C 区右侧

### JP2/JP3

JP2(IN) 与 JP3(OUT) 均为 4 Pin：1=GND、2=VCC_5V、3=D2、4=D1；D1/D2 各有 ESD5311 保护，5V 侧 C14/C15 10uF/35V。

- 参数与网络：`pin1=GND`；`pin2=VCC_5V`；`pin3=D2`；`pin4=D1`；`esd=ESD5311`
- 证据：图 efb4d0734400 / 第 1 页 / B 区 JP2/JP3

### R14/LED1

PA8 经 R14(4.7K) 驱动 LED1 绿色指示灯到地。

- 参数与网络：`pin=PA8`；`resistor=R14 4.7K`
- 证据：图 efb4d0734400 / 第 1 页 / C 区 LED1/R14

## 总线

### R21/R22

SDA/RX1 由 R21(2.2K) 上拉到 VCC_3V3，SCL/TX1 由 R22(2.2K) 上拉。

- 参数与网络：`sda=R21 2.2K`；`scl=R22 2.2K`
- 证据：图 efb4d0734400 / 第 1 页 / C 区 R21/R22

### U5

I2C 模式：GROVE1_D2/D1 接 SDA/RX1(PD6)/SCL/TX1(PD5)；GROVE2_D2/D1 经 R8/R9(0R) 并入同一 I2C 总线，R10/R11 为 NC。

- 参数与网络：`grove1=I2C1 SDA/SCL`；`grove2=via R8/R9 0R`；`r10_r11=NC`
- 证据：图 efb4d0734400 / 第 1 页 / C 区 R8~R11 与 Design Note

## 总线地址

### SW1

SW1(SKAR-16) 为 16 位旋转编码开关，4 个地址位 PB3/PB4/PB5/PB8 由 R15~R18(10K) 上拉，开关将选中位接地形成地址；C20~C23 为 1nF/50V 滤波。

- 参数与网络：`switch=SKAR-16`；`addr_bits=PB3,PB4,PB5,PB8`；`pullups=R15-R18 10K`
- 证据：图 efb4d0734400 / 第 1 页 / D 区右侧 SW1 与真值表

## 复位

### R20/C18

STM_RST 由 R20(10K) 上拉到 VCC_3V3，C18(100nF) 对地，并接 MCU PF2-NRST(5)。

- 参数与网络：`pullup=R20 10K`；`cap=C18 100nF`
- 证据：图 efb4d0734400 / 第 1 页 / D 区左侧 R20/C18

## 保护电路

### DC1/F1/DR1

DC1(DC-044) 输入经 F1(SMD1812-200-30，2A 保持/4A 触发) 与 DR1(SMF30CA) TVS，输入范围为 9~24V；E1 100uF/35V、C3/C4 10uF/35V 滤波。

- 参数与网络：`input=DC 9~24V`；`fuse=SMD1812-200-30`；`tvs=SMF30CA`；`bulk=E1 100uF/35V`
- 证据：图 efb4d0734400 / 第 1 页 / A 区电气输入

## 模拟电路

### U3

U3(INA199A1DCKR) 的 IN+(4)/IN-(5) 跨接 R4(10mR/1%)，V+(3)=VCC_5V 并由 C13 100nF/50V 去耦，OUT(6)=ADC1_IN4 接 MCU PA4，REF(1) 与 GND(2) 接地。

- 参数与网络：`shunt=R4 10mR`；`gain=50V/V (A1)`；`out=ADC1_IN4/PA4`
- 证据：图 efb4d0734400 / 第 1 页 / B 区 INA199

### R19/R23

SERVOS_5V 经 R19(10K)/R23(10K) 分压后接 ADC1_IN5(PA5)，用于监测舵机供电电压。

- 参数与网络：`divider=R19/R23 10K`；`adc=ADC1_IN5/PA5`
- 证据：图 efb4d0734400 / 第 1 页 / C 区 R19/R23

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 保护电路 | DC1/F1/DR1 | `input=DC 9~24V`；`fuse=SMD1812-200-30`；`tvs=SMF30CA`；`bulk=E1 100uF/35V` |
| 电源 | U1 | `vin=DC_IN`；`vout=VCC_5V`；`l1=FXL0530-6R8-M`；`r1=220K`；`r3=30K`；`iout_max=3A` |
| 电源 | U2 | `vin=VCC_5V`；`vout=VCC_3V3`；`iout_max=300mA` |
| 模拟电路 | U3 | `shunt=R4 10mR`；`gain=50V/V (A1)`；`out=ADC1_IN4/PA4` |
| 总线 | R21/R22 | `sda=R21 2.2K`；`scl=R22 2.2K` |
| 模拟电路 | R19/R23 | `divider=R19/R23 10K`；`adc=ADC1_IN5/PA5` |
| 系统结构 | U5 | `vdd=VCC_3V3`；`nrst=STM_RST` |
| 接口 | U5 | `PA0=TIM2_CH1`；`PA1=TIM2_CH2`；`PA2=TIM2_CH3`；`PA3=TIM2_CH4`；`PA6=TIM3_CH1`；`PA7=TIM3_CH2`；`PB0=TIM3_CH3`；`PB1=TIM3_CH4` |
| 接口 | JP4/JP5/JP1/JP6 | `connectors=JP4,JP5,JP1,JP6`；`pins=GND/5V/SIG`；`bulk=E2 100uF/35V` |
| 接口 | JP2/JP3 | `pin1=GND`；`pin2=VCC_5V`；`pin3=D2`；`pin4=D1`；`esd=ESD5311` |
| 总线 | U5 | `grove1=I2C1 SDA/SCL`；`grove2=via R8/R9 0R`；`r10_r11=NC` |
| 总线地址 | SW1 | `switch=SKAR-16`；`addr_bits=PB3,PB4,PB5,PB8`；`pullups=R15-R18 10K` |
| 接口 | R14/LED1 | `pin=PA8`；`resistor=R14 4.7K` |
| 复位 | R20/C18 | `pullup=R20 10K`；`cap=C18 100nF` |

## 待确认事项

- `nr-1`：JP2/JP3 的 D1/D2 在 Chain 与 I2C 两种固件下的最终用途是否与电阻配置一致？；原因：原理图给出 Design Note 与 0R/NC 组合，实际功能取决于贴装与固件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `efb4d0734400ff0b01d0ce36feb87564f890d41beff42199ab904d3c915d296c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/SCH_Unit_8Servos2-I2C_V0.4_SCH_PDF_20260526_2026_05_26_11_47_47_page_01.png` |

---

源文档：`zh_CN/unit/Unit_8Servos2-I2C.md`

源文档 SHA-256：`ccd15d68d4437443693dc49117b07954c6a5435daec5ceeb71bfdf2d33baa62f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
