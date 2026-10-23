# Stamp Timer Power2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp Timer Power2 |
| SKU | S021 |
| 产品 ID | `stamp-timer-power2-bb65c8e7c60b` |
| 源文档 | `zh_CN/stamp/Stamp_Timer_Power2.md` |

## 概述

Stamp Timer Power2（S021）是以 U7 PY32_PMIC 电源管理控制器为核心的电源管理模组。5V_IN 经 U1 AW32901FCR 输入保护后形成 SYS_5VIN，并与 VBAT、Internal_5V、EXT_5V_INOUT 通过多组 YHM2031W4T 构成 Main PowerPath，汇聚到 SYS_VBUS。SYS_VBUS 分别经 U2、U13 两路 SSP7615-33DFR 产生 3V3_LDO_OUT 与 PY_3V3，另由 U6 JW5712 产生 3V3_DCDC_OUT、U8 SY7088 产生 BOOST_OUT，BOOST_OUT 再经 U9 MT9700 输出 EXT_5V_INOUT。U5 LGS4056HDA 构成 VBAT 充电电路，U7 通过 I2C、5 路可编程 IO、电源使能、ADC 检测、按键与 BOOT 信号连接 J1/J2 两排 2×14 邮票孔。

## 检索关键词

`Stamp Timer Power2`、`S021`、`M5PM1`、`PY32_PMIC`、`AW32901FCR`、`SSP7615-33DFR`、`YHM2031W4T`、`JW5712`、`SY7088`、`MT9700`、`LGS4056HDA`、`5V_IN`、`SYS_5VIN`、`SYS_VBUS`、`Internal_5V`、`EXT_5V_INOUT`、`VBAT`、`PY_3V3`、`3V3_LDO_OUT`、`3V3_DCDC_OUT`、`BOOST_OUT`、`I2C_SCL`、`I2C_SDA`、`VIN_DETECT`、`EXT_5V_ADC`、`BAT_ADC`、`VBAT_ADC_EN`、`PWR_BTN`、`BOOT_OUT`、`CHG_PROG`、`CHRG_STAT`、`G0_WAKE`、`G1_ADC_IO`、`G2_WAKE`、`G3_WAKE`、`G4_WAKE`、`Stamp Hole Pinmap`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | AW32901FCR | 5V_IN 输入保护器件，三路 IN 接 5V_IN、三路 OUT 接 SYS_5VIN | 图 566a5f4a5e33 / 第 1 页 / Input Protection 区：U1、AW32901FCR 及 IN/OUT/OVLO/nEN/GND 引脚 |
| U2 | SSP7615-33DFR | SYS_VBUS 转 3V3_LDO_OUT 的低静态电流 LDO | 图 566a5f4a5e33 / 第 1 页 / LDO OUT 区：U2、SSP7615-33DFR、3V3_LDO_EN 与 3V3_LDO_OUT |
| U13 | SSP7615-33DFR | SYS_VBUS 转 PY_3V3 的 LDO，为 U7 供电 | 图 566a5f4a5e33 / 第 1 页 / Logic Contor 区上部：U13、SSP7615-33DFR、VIN/EN/OUT 与 PY_3V3 |
| U6 | JW5712 | SYS_VBUS 转 3V3_DCDC_OUT 的降压转换器 | 图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区上部：U6、JW5712、VIN/EN/SW/VOS/VSEL 引脚 |
| U8 | SY7088 | SYS_VBUS 转 BOOST_OUT 的升压转换器 | 图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区下部：U8、SY7088、LX/IN/EN/OUT/FB 引脚 |
| U3 / U4 | YHM2031W4T | VBAT 到 SYS_VBUS 的两路并联供电开关 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath 上部：U3、U4 型号与 VDD/EN/OUT/GND 网络 |
| U18 / U10 | YHM2031W4T | SYS_5VIN 到 Internal_5V 的两路供电开关 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath 上部：U18、U10 型号与 SYS_5VIN/Internal_5V 网络 |
| U11 / U12 | YHM2031W4T | Internal_5V 到 SYS_VBUS 的两路供电开关 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath：U11、U12 型号与 Internal_5V/SYS_VBUS 网络 |
| U15 / U14 | YHM2031W4T | EXT_5V_INOUT 到 Internal_5V 的两路供电开关 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath：U15、U14 型号与 EXT_5V_INOUT/Internal_5V 网络 |
| U9 | MT9700 | BOOST_OUT 到 EXT_5V_INOUT 的限流负载开关 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath 下部：U9、MT9700、VIN/VOUT/EN/SET 引脚 |
| U5 | LGS4056HDA | VBAT 线性锂电池充电控制器 | 图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5、LGS4056HDA、VCC/BAT/PROG/CE/CHRG 引脚 |
| U7 | PY32_PMIC | 电源管理控制器，负责电源使能、ADC 检测、I2C、唤醒/IRQ 与按键/BOOT 信号 | 图 566a5f4a5e33 / 第 1 页 / Logic Contor 区：U7、PY32_PMIC 符号及全部引脚网络 |
| J1 / J2 | 未标注 | 2×14 邮票孔连接器，引出控制、GPIO、I2C 与各电源网络 | 图 566a5f4a5e33 / 第 1 页 / Stamp Hole Pinmap：J1 第 1~14 脚与 J2 第 15~28 脚 |
| Q1 | CJ3134KFK | EXT_5V_EN 控制路径中的 MOS 管 | 图 566a5f4a5e33 / 第 1 页 / Main PowerPath：Q1、CJ3134KFK、EXT_5V_EN、R3 与 R5 |
| Q2 / Q4 | 未标注 | VBAT_ADC_EN 控制 VBAT 采样支路的两只开关管 | 图 566a5f4a5e33 / 第 1 页 / ADC Sample 区左侧：Q2、Q4、VBAT_ADC_EN、R7、R22 |
| L1 | 2.2uH | U6 降压转换器的功率电感 | 图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区上部：L1 2.2uH 连接 U6 SW 与 3V3_DCDC_OUT |
| L2 | FTC201210S1R5MBCA | U8 升压转换器的功率电感 | 图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区下部：L2 型号连接 SYS_VBUS 与 U8 LX |
| R17 / R8 | 5.1K/1% / 2.2K/1% | U5 PROG 引脚的充电编程与 CHG_PROG 选择电阻 | 图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5 PROG 经 R17、R8 与 CHG_PROG 相连 |
| R19 / R20 | 10K/1% / 2.94K/1% | U8 BOOST_OUT 反馈分压电阻 | 图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区下部：R19、R20 与 U8 FB 引脚 |
| R7 / R9 / R10 / R22 | 100K / 1K/1% / 1K/1% / 10K/1% | VBAT ADC 开关控制与分压网络 | 图 566a5f4a5e33 / 第 1 页 / ADC Sample 区左侧：Q2/Q4 周边的 R7、R9、R10、R22 |

## 系统结构

### Stamp Timer Power2

模组以 U7 为电源管理控制中心：5V_IN 经 U1 到 SYS_5VIN，SYS_5VIN、VBAT、Internal_5V 与 EXT_5V_INOUT 通过 YHM2031W4T 开关汇聚到 SYS_VBUS，SYS_VBUS 再供给 3.3V LDO/DCDC、VBAT 充电器和 U7 的 PY_3V3 供电。

- 参数与网络：`input_net=5V_IN`；`protected_net=SYS_5VIN`；`powerpath_net=SYS_VBUS`；`control_ic=U7`
- 证据：图 566a5f4a5e33 / 第 1 页 / Input Protection、Main PowerPath、DCDC OUT、BAT Charge 与 Logic Contor 区块

## 核心器件

### U7

U7 的符号底部标注 PY32_PMIC，VCC(6) 接 PY_3V3，GND(4,2) 接地，C15(100nF/10V) 与 C14(4.7uF/6.3V) 为 VCC 去耦。

- 参数与网络：`part=PY32_PMIC`；`vcc_pin=6`；`gnd_pins=4,2`；`vcc_net=PY_3V3`；`decoupling=C15 100nF/10V, C14 4.7uF/6.3V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区：U7 符号、VCC(6)、GND(4,2)、C14/C15

### U7

U7 的 DCDC3V3_EN_PP(14)、LDO3V3_EN_PP(18)、BOOST5V_EN_PP(10)、CHG_EN_PP(2) 分别连接 3V3_DCDC_EN、3V3_LDO_EN、EXT_5V_EN、CHG_EN。

- 参数与网络：`pin14=DCDC3V3_EN_PP <- 3V3_DCDC_EN`；`pin18=LDO3V3_EN_PP <- 3V3_LDO_EN`；`pin10=BOOST5V_EN_PP <- EXT_5V_EN`；`pin2=CHG_EN_PP <- CHG_EN`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 左侧上部：14/18/10/2 脚及使能网络

### U7

U7 的 5VOUT_ADC_IN(19) 接 EXT_5V_ADC，5VIN_ADC_IN(16) 接 VIN_DETECT，BAT_ADC_IN(11) 接 BAT_ADC，BAT_ADC_EN_OD(1) 接 VBAT_ADC_EN。

- 参数与网络：`pin19=5VOUT_ADC_IN <- EXT_5V_ADC`；`pin16=5VIN_ADC_IN <- VIN_DETECT`；`pin11=BAT_ADC_IN <- BAT_ADC`；`pin1=BAT_ADC_EN_OD -> VBAT_ADC_EN`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 左侧中部：19/16/11/1 脚及 ADC 网络

## 电源

### U1

5V_IN 接 U1 的 IN(B3,C2,C3)，OUT(A2,A3,B2) 输出 SYS_5VIN；输入侧 C1=1uF/25V、输出侧 C21=1uF/10V 均接地。

- 参数与网络：`input=5V_IN`；`output=SYS_5VIN`；`input_in_pins=B3,C2,C3`；`output_out_pins=A2,A3,B2`；`input_cap=C1 1uF/25V`；`output_cap=C21 1uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Input Protection 区：U1 IN/OUT 引脚、C1 与 C21

### U2

SYS_VBUS 接 U2 VIN(4)，3V3_LDO_EN 接 EN(3)，OUT(1) 输出 3V3_LDO_OUT；C3=1uF/10V、C4=1uF/10V 分别为输入和输出电容，R4=NC 接在 EN 与地之间。

- 参数与网络：`input=SYS_VBUS`；`output=3V3_LDO_OUT`；`enable=3V3_LDO_EN`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`input_cap=C3 1uF/10V`；`output_cap=C4 1uF/10V`；`en_option=R4 NC`
- 证据：图 566a5f4a5e33 / 第 1 页 / LDO OUT 区：U2 VIN/EN/OUT、C3/C4 与 R4

### U13

U13 的 VIN(4) 与 EN(3) 同接 SYS_VBUS，OUT(1) 输出 PY_3V3；R16=NC 跨接输入与输出，C22=1uF/10V 接在 PY_3V3 与地之间。

- 参数与网络：`input=SYS_VBUS`；`output=PY_3V3`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`bypass=R16 NC`；`output_cap=C22 1uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区上部：U13 VIN/EN/OUT、R16 与 C22

### U6

U6 的 VIN(A2) 接 SYS_VBUS，EN(B1) 接 3V3_DCDC_EN 并由 R15=100K/1% 下拉，SW(A1) 经 L1=2.2uH 形成 3V3_DCDC_OUT，VOS(C2) 接输出反馈网络。

- 参数与网络：`part=JW5712`；`input=SYS_VBUS`；`output=3V3_DCDC_OUT`；`enable=3V3_DCDC_EN`；`vin_pin=A2`；`en_pin=B1`；`sw_pin=A1`；`vos_pin=C2`；`inductor=L1 2.2uH`；`en_pulldown=R15 100K/1%`
- 证据：图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区上部：U6 VIN/EN/SW/VOS、L1 与 R15

### 3V3_DCDC_OUT

3V3_DCDC_OUT 节点布置 C11=10uF/10V、C12=10uF/10V、C13=100nF/10V 对地，U6 SW 节点布置 C10=1nF/50V 对地。

- 参数与网络：`output_caps=C11 10uF/10V, C12 10uF/10V, C13 100nF/10V`；`sw_cap=C10 1nF/50V`；`output_net=3V3_DCDC_OUT`
- 证据：图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区上部：C10、C11、C12、C13 与 3V3_DCDC_OUT

### U8

U8 的 IN(6) 接 SYS_VBUS 输入网络，EN(3) 接 EXT_5V_EN 并由 R21=100K/1% 下拉，LX(1,2) 经 L2 接输入侧，OUT(8,7) 形成 BOOST_OUT，FB(5) 接 R19=10K/1% 与 R20=2.94K/1% 分压。

- 参数与网络：`part=SY7088`；`input_net=SYS_VBUS`；`output=BOOST_OUT`；`enable=EXT_5V_EN`；`in_pin=6`；`en_pin=3`；`lx_pins=1,2`；`out_pins=8,7`；`fb_pin=5`；`inductor=L2 FTC201210S1R5MBCA`；`feedback=R19 10K/1%, R20 2.94K/1%`；`en_pulldown=R21 100K/1%`
- 证据：图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区下部：U8、L2、R19/R20、R21 与 BOOST_OUT

### BOOST_OUT

BOOST_OUT 节点布置 C19=10uF/10V、C20=10uF/10V、C28=4.7uF/10V、C32=10uF/10V、C31=100nF/50V 对地，U8 输入侧布置 C29、C30、C23、C24、C17、C18（均标 10uF/10V）。

- 参数与网络：`output_caps=C19 10uF/10V, C20 10uF/10V, C28 4.7uF/10V, C32 10uF/10V, C31 100nF/50V`；`input_caps=C29, C30, C23, C24, C17, C18 10uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / DCDC OUT 区下部：U8 输入与 BOOST_OUT 输出电容组

### U3 / U4

VBAT 同时接 U3、U4 的 VDD(A1)，OUT(A2) 均为 SYS_VBUS；R25、R27 为 10K/1%，输入侧 C35、C36 为 4.7uF/10V，输出侧 C25、C27 为 10uF/10V。

- 参数与网络：`part=YHM2031W4T`；`input=VBAT`；`output=SYS_VBUS`；`en_pullups=R25 10K/1%, R27 10K/1%`；`input_caps=C35 4.7uF/10V, C36 4.7uF/10V`；`output_caps=C25 10uF/10V, C27 10uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Main PowerPath 上部：U3/U4、R25/R27、C35/C36、C25/C27

### U11 / U12

Internal_5V 同时接 U11、U12 的 VDD(A1)，OUT(A2) 均为 SYS_VBUS；R29、R30 为 10K/1%，输入侧 C42、C43 为 4.7uF/10V，输出侧 C40、C41 为 10uF/10V。

- 参数与网络：`part=YHM2031W4T`；`input=Internal_5V`；`output=SYS_VBUS`；`en_pullups=R29 10K/1%, R30 10K/1%`；`input_caps=C42 4.7uF/10V, C43 4.7uF/10V`；`output_caps=C40 10uF/10V, C41 10uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Main PowerPath：U11/U12、R29/R30、C42/C43、C40/C41

### U18 / U10

SYS_5VIN 同时接 U18、U10 的 VDD(A1)，OUT(A2) 均为 Internal_5V；R26、R28 为 10K/1%，输入侧 C37、C2 为 4.7uF/10V，输出侧 C38、C39 为 10uF/10V。

- 参数与网络：`part=YHM2031W4T`；`input=SYS_5VIN`；`output=Internal_5V`；`en_pullups=R26 10K/1%, R28 10K/1%`；`input_caps=C37 4.7uF/10V, C2 4.7uF/10V`；`output_caps=C38 10uF/10V, C39 10uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Main PowerPath 上部：U18/U10、R26/R28、C37/C2、C38/C39

### U15 / U14

EXT_5V_INOUT 同时接 U15、U14 的 VDD(A1)，OUT(A2) 均为 Internal_5V；输出侧 C34、C45 为 10uF/10V，另有 C46、C44 为 10uF/10V。

- 参数与网络：`part=YHM2031W4T`；`input=EXT_5V_INOUT`；`output=Internal_5V`；`output_caps=C34 10uF/10V, C45 10uF/10V`；`other_caps=C46 10uF/10V, C44 10uF/10V`
- 证据：图 566a5f4a5e33 / 第 1 页 / Main PowerPath：U15/U14、EXT_5V_INOUT、Internal_5V、C34/C45/C46/C44

### U9

U9 的 VIN(5) 接 BOOST_OUT，VOUT(1) 输出 EXT_5V_INOUT，EN(4) 接 EXT_5V_EN，SET(3) 接 R14=4.7K/1%，输出侧 C33=10uF/10V；原理图标注 Im=6.8K/4.7K=1.4A。

- 参数与网络：`part=MT9700`；`input=BOOST_OUT`；`output=EXT_5V_INOUT`；`enable=EXT_5V_EN`；`vin_pin=5`；`vout_pin=1`；`en_pin=4`；`set_pin=3`；`set_resistor=R14 4.7K/1%`；`output_cap=C33 10uF/10V`；`schematic_note=Im=6.8K/4.7K=1.4A`
- 证据：图 566a5f4a5e33 / 第 1 页 / Main PowerPath 下部：U9 MT9700、R14、C33 与限流标注

### U5

U5 的 VCC(4) 接 Internal_5V，BAT(5) 接 VBAT，GND(3,9) 接地；VCC 侧 C6=100nF/16V、BAT 侧 C5=100nF/16V，CE(8) 接 CHG_EN。

- 参数与网络：`part=LGS4056HDA`；`vcc=Internal_5V`；`battery=VBAT`；`vcc_pin=4`；`bat_pin=5`；`gnd_pins=3,9`；`ce_pin=8`；`ce_net=CHG_EN`；`vcc_cap=C6 100nF/16V`；`bat_cap=C5 100nF/16V`
- 证据：图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5 VCC/BAT/GND/CE、C6 与 C5

## 接口

### J1

J1 第 1~14 脚依次为 CHG_PROG、CHRG_STAT、PWR_BTN、GND、BOOT_OUT、LED_PWR_EN、G0_WAKE(0/2)_NEOPIXEL、G1_ADC_IO、G2_WAKE(0/2)_ADC、G3_WAKE(3/4)_PWM、G4_WAKE(3/4)_PWM、I2C_SDA、I2C_SCL、GND。

- 参数与网络：`pin1=CHG_PROG`；`pin2=CHRG_STAT`；`pin3=PWR_BTN`；`pin4=GND`；`pin5=BOOT_OUT`；`pin6=LED_PWR_EN`；`pin7=G0_WAKE(0/2)_NEOPIXEL`；`pin8=G1_ADC_IO`；`pin9=G2_WAKE(0/2)_ADC`；`pin10=G3_WAKE(3/4)_PWM`；`pin11=G4_WAKE(3/4)_PWM`；`pin12=I2C_SDA`；`pin13=I2C_SCL`；`pin14=GND`
- 证据：图 566a5f4a5e33 / 第 1 页 / Stamp Hole Pinmap：J1 第 1~14 脚网络名

### J2

J2 第 16、18、20、22、24、26、28 脚分别为 5V_IN、EXT_5V_INOUT、VBAT、PY_3V3、SYS_VBUS、3V3_DCDC_OUT、3V3_LDO_OUT；第 15、17、19、21、23、25、27 脚均接 GND。

- 参数与网络：`pin15=GND`；`pin16=5V_IN`；`pin17=GND`；`pin18=EXT_5V_INOUT`；`pin19=GND`；`pin20=VBAT`；`pin21=GND`；`pin22=PY_3V3`；`pin23=GND`；`pin24=SYS_VBUS`；`pin25=GND`；`pin26=3V3_DCDC_OUT`；`pin27=GND`；`pin28=3V3_LDO_OUT`
- 证据：图 566a5f4a5e33 / 第 1 页 / Stamp Hole Pinmap：J2 第 15~28 脚网络名

### BOOT_OUT / LED_PWR_EN

J1 第 5 脚 BOOT_OUT 接 U7 BOOT_OUT_OD(15)，J1 第 6 脚 LED_PWR_EN 接 U7 LED_EN_PP(5)。

- 参数与网络：`boot_connector_pin=J1-5`；`boot_controller_pin=U7-15`；`boot_function=BOOT_OUT_OD`；`led_connector_pin=J1-6`；`led_controller_pin=U7-5`；`led_function=LED_EN_PP`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 左侧 BOOT_OUT_OD(15)、LED_EN_PP(5)；Stamp Hole Pinmap J1 第 5/6 脚

### U5 / J1

U5 的 CHRG(7) 形成 CHRG_STAT，经 R11=1M/1% 接 PY_3V3，并连接到 J1 第 2 脚；DONE(6) 标为叉号未连接。

- 参数与网络：`chrg_pin=U5-7`；`status_net=CHRG_STAT`；`pullup=R11 1M/1%`；`pullup_rail=PY_3V3`；`connector_pin=J1-2`；`done_pin=U5-6 unconnected`
- 证据：图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5 CHRG/DONE、R11；Stamp Hole Pinmap J1-2

## 总线

### U7 / J1

U7 的 I2C_SCL_OD(9) 连接 I2C_SCL，I2C_SDA_OD(8) 连接 I2C_SDA；两条网络分别引到 J1 第 13、12 脚。

- 参数与网络：`controller_scl_pin=U7-9`；`controller_sda_pin=U7-8`；`connector_scl_pin=J1-13`；`connector_sda_pin=J1-12`；`scl_net=I2C_SCL`；`sda_net=I2C_SDA`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 右侧：8/9 脚；Stamp Hole Pinmap：J1 12/13 脚

## GPIO 与控制信号

### J1 / U7

J1 第 7~11 脚为 G0~G4：G0/G2 接 U7 的 3/20 脚，G3/G4 接 U7 的 13/12 脚，G1 接 U7 的 17 脚；U7 对应符号名为 G0_WAKEin(INT0/2)_IRQout_NEOPIXEL、G2_WAKEin(INT0/2)_IRQout_ADC、G3/G4_WAKEin(INT3/4)_IRQout_PWM、G1_IRQout_ADC。

- 参数与网络：`G0=J1-7, U7-3, NEOPIXEL/IRQ`；`G1=J1-8, U7-17, ADC/IRQ`；`G2=J1-9, U7-20, ADC/IRQ`；`G3=J1-10, U7-13, PWM/IRQ`；`G4=J1-11, U7-12, PWM/IRQ`；`wake_note=G0/G2 二选一，G3/G4 二选一`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 左侧 GPIO 组；Stamp Hole Pinmap J1 第 7~11 脚

## 复位

### PWR_BTN

J1 第 3 脚 PWR_BTN 接 U7 的 BTN_PU(7)，作为电源按键输入。

- 参数与网络：`connector_pin=J1-3`；`controller_pin=U7-7`；`controller_function=BTN_PU`
- 证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区 U7 左侧 BTN_PU(7)；Stamp Hole Pinmap J1-3

## 保护电路

### U1

U1 的 OVLO(C1) 经 R2=0R 接 5V_IN，R1=NC 与 R2 并联位置；nEN(A1) 接 5V_IN，GND(A4,B4,C4) 接地。

- 参数与网络：`ovlo_pin=C1`；`ovlo_resistor=R2 0R`；`alternate_resistor=R1 NC`；`nen_pin=A1`；`nen_net=5V_IN`；`gnd_pins=A4,B4,C4`
- 证据：图 566a5f4a5e33 / 第 1 页 / Input Protection 区：U1 OVLO、R1/R2、nEN 与 GND 引脚

## 关键网络

### 电源网络

原理图明确使用 5V_IN、SYS_5VIN、SYS_VBUS、Internal_5V、EXT_5V_INOUT、VBAT、PY_3V3、3V3_LDO_OUT、3V3_DCDC_OUT 与 BOOST_OUT 这组电源网络名。

- 参数与网络：`input=5V_IN`；`protected_5v=SYS_5VIN`；`main_bus=SYS_VBUS`；`internal_5v=Internal_5V`；`external_5v=EXT_5V_INOUT`；`battery=VBAT`；`pmic_3v3=PY_3V3`；`ldo_3v3=3V3_LDO_OUT`；`dcdc_3v3=3V3_DCDC_OUT`；`boost=BOOST_OUT`
- 证据：图 566a5f4a5e33 / 第 1 页 / 整页 Input Protection、Main PowerPath、DCDC OUT、BAT Charge、Logic Contor 与 Stamp Hole Pinmap 的网络名

## 其他事实

### Q2 / Q4

VBAT 接 Q4 的 2 脚，Q4 的 3 脚经 R9=1K/1% 接 BAT_ADC，BAT_ADC 再经 R10=1K/1% 接地并有 C26=100nF/16V；Q4 的 1 脚经 R7=100K 接 VBAT，并接 Q2 的 D(3)，Q2 的 S(2) 接地、G(1) 接 VBAT_ADC_EN 且由 R22=10K/1% 下拉。

- 参数与网络：`q4_pin2=VBAT`；`q4_pin3=R9 1K/1%`；`q4_pin1=R7 100K, Q2-D`；`divider=R9 1K/1%, R10 1K/1%`；`filter=C26 100nF/16V`；`q2_gate=VBAT_ADC_EN`；`q2_gate_pulldown=R22 10K/1%`
- 证据：图 566a5f4a5e33 / 第 1 页 / ADC Sample 区左侧：VBAT、Q4、Q2、R7/R9/R10/R22 与 C26

### SYS_5VIN

SYS_5VIN 经 R12=10K/1% 与 R13=10K/1% 分压得到 VIN_DETECT，节点并有 C16=100nF/25V 接地。

- 参数与网络：`input=SYS_5VIN`；`output=VIN_DETECT`；`upper=R12 10K/1%`；`lower=R13 10K/1%`；`filter=C16 100nF/25V`
- 证据：图 566a5f4a5e33 / 第 1 页 / ADC Sample 区右侧：R12/R13/C16 与 VIN_DETECT

### EXT_5V_INOUT

EXT_5V_INOUT 经 R23=10K/1% 与 R24=10K/1% 分压得到 EXT_5V_ADC，节点并有 C7=100nF/25V 接地。

- 参数与网络：`input=EXT_5V_INOUT`；`output=EXT_5V_ADC`；`upper=R23 10K/1%`；`lower=R24 10K/1%`；`filter=C7 100nF/25V`
- 证据：图 566a5f4a5e33 / 第 1 页 / ADC Sample 区右侧：R23/R24/C7 与 EXT_5V_ADC

### U5 / R17 / R8

U5 的 PROG(2) 接 R17=5.1K/1% 到地，并经 R8=2.2K/1% 连接 CHG_PROG；CHG_PROG 引到 J1 第 1 脚。

- 参数与网络：`prog_pin=U5-2`；`prog_resistor=R17 5.1K/1%`；`selection_resistor=R8 2.2K/1%`；`control_net=CHG_PROG`；`connector_pin=J1-1`
- 证据：图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5 PROG、R17、R8、CHG_PROG；Stamp Hole Pinmap J1-1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp Timer Power2 | `input_net=5V_IN`；`protected_net=SYS_5VIN`；`powerpath_net=SYS_VBUS`；`control_ic=U7` |
| 核心器件 | U7 | `part=PY32_PMIC`；`vcc_pin=6`；`gnd_pins=4,2`；`vcc_net=PY_3V3`；`decoupling=C15 100nF/10V, C14 4.7uF/6.3V` |
| 核心器件 | U7 | `pin14=DCDC3V3_EN_PP <- 3V3_DCDC_EN`；`pin18=LDO3V3_EN_PP <- 3V3_LDO_EN`；`pin10=BOOST5V_EN_PP <- EXT_5V_EN`；`pin2=CHG_EN_PP <- CHG_EN` |
| 核心器件 | U7 | `pin19=5VOUT_ADC_IN <- EXT_5V_ADC`；`pin16=5VIN_ADC_IN <- VIN_DETECT`；`pin11=BAT_ADC_IN <- BAT_ADC`；`pin1=BAT_ADC_EN_OD -> VBAT_ADC_EN` |
| 电源 | U1 | `input=5V_IN`；`output=SYS_5VIN`；`input_in_pins=B3,C2,C3`；`output_out_pins=A2,A3,B2`；`input_cap=C1 1uF/25V`；`output_cap=C21 1uF/10V` |
| 保护电路 | U1 | `ovlo_pin=C1`；`ovlo_resistor=R2 0R`；`alternate_resistor=R1 NC`；`nen_pin=A1`；`nen_net=5V_IN`；`gnd_pins=A4,B4,C4` |
| 电源 | U2 | `input=SYS_VBUS`；`output=3V3_LDO_OUT`；`enable=3V3_LDO_EN`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`input_cap=C3 1uF/10V`；`output_cap=C4 1uF/10V`；`en_option=R4 NC` |
| 电源 | U13 | `input=SYS_VBUS`；`output=PY_3V3`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`bypass=R16 NC`；`output_cap=C22 1uF/10V` |
| 电源 | U6 | `part=JW5712`；`input=SYS_VBUS`；`output=3V3_DCDC_OUT`；`enable=3V3_DCDC_EN`；`vin_pin=A2`；`en_pin=B1`；`sw_pin=A1`；`vos_pin=C2`；`inductor=L1 2.2uH`；`en_pulldown=R15 100K/1%` |
| 电源 | 3V3_DCDC_OUT | `output_caps=C11 10uF/10V, C12 10uF/10V, C13 100nF/10V`；`sw_cap=C10 1nF/50V`；`output_net=3V3_DCDC_OUT` |
| 电源 | U8 | `part=SY7088`；`input_net=SYS_VBUS`；`output=BOOST_OUT`；`enable=EXT_5V_EN`；`in_pin=6`；`en_pin=3`；`lx_pins=1,2`；`out_pins=8,7`；`fb_pin=5`；`inductor=L2 FTC201210S1R5MBCA`；`feedback=R19 10K/1%, R20 2.94K/1%`；`en_pulldown=R21 100K/1%` |
| 电源 | BOOST_OUT | `output_caps=C19 10uF/10V, C20 10uF/10V, C28 4.7uF/10V, C32 10uF/10V, C31 100nF/50V`；`input_caps=C29, C30, C23, C24, C17, C18 10uF/10V` |
| 电源 | U3 / U4 | `part=YHM2031W4T`；`input=VBAT`；`output=SYS_VBUS`；`en_pullups=R25 10K/1%, R27 10K/1%`；`input_caps=C35 4.7uF/10V, C36 4.7uF/10V`；`output_caps=C25 10uF/10V, C27 10uF/10V` |
| 电源 | U11 / U12 | `part=YHM2031W4T`；`input=Internal_5V`；`output=SYS_VBUS`；`en_pullups=R29 10K/1%, R30 10K/1%`；`input_caps=C42 4.7uF/10V, C43 4.7uF/10V`；`output_caps=C40 10uF/10V, C41 10uF/10V` |
| 电源 | U18 / U10 | `part=YHM2031W4T`；`input=SYS_5VIN`；`output=Internal_5V`；`en_pullups=R26 10K/1%, R28 10K/1%`；`input_caps=C37 4.7uF/10V, C2 4.7uF/10V`；`output_caps=C38 10uF/10V, C39 10uF/10V` |
| 电源 | U15 / U14 | `part=YHM2031W4T`；`input=EXT_5V_INOUT`；`output=Internal_5V`；`output_caps=C34 10uF/10V, C45 10uF/10V`；`other_caps=C46 10uF/10V, C44 10uF/10V` |
| 电源 | U9 | `part=MT9700`；`input=BOOST_OUT`；`output=EXT_5V_INOUT`；`enable=EXT_5V_EN`；`vin_pin=5`；`vout_pin=1`；`en_pin=4`；`set_pin=3`；`set_resistor=R14 4.7K/1%`；`output_cap=C33 10uF/10V`；`schematic_note=Im=6.8K/4.7K=1.4A` |
| 电源 | U5 | `part=LGS4056HDA`；`vcc=Internal_5V`；`battery=VBAT`；`vcc_pin=4`；`bat_pin=5`；`gnd_pins=3,9`；`ce_pin=8`；`ce_net=CHG_EN`；`vcc_cap=C6 100nF/16V`；`bat_cap=C5 100nF/16V` |
| 接口 | J1 | `pin1=CHG_PROG`；`pin2=CHRG_STAT`；`pin3=PWR_BTN`；`pin4=GND`；`pin5=BOOT_OUT`；`pin6=LED_PWR_EN`；`pin7=G0_WAKE(0/2)_NEOPIXEL`；`pin8=G1_ADC_IO`；`pin9=G2_WAKE(0/2)_ADC`；`pin10=G3_WAKE(3/4)_PWM`；`pin11=G4_WAKE(3/4)_PWM`；`pin12=I2C_SDA`；`pin13=I2C_SCL`；`pin14=GND` |
| 接口 | J2 | `pin15=GND`；`pin16=5V_IN`；`pin17=GND`；`pin18=EXT_5V_INOUT`；`pin19=GND`；`pin20=VBAT`；`pin21=GND`；`pin22=PY_3V3`；`pin23=GND`；`pin24=SYS_VBUS`；`pin25=GND`；`pin26=3V3_DCDC_OUT`；`pin27=GND`；`pin28=3V3_LDO_OUT` |
| 总线 | U7 / J1 | `controller_scl_pin=U7-9`；`controller_sda_pin=U7-8`；`connector_scl_pin=J1-13`；`connector_sda_pin=J1-12`；`scl_net=I2C_SCL`；`sda_net=I2C_SDA` |
| GPIO 与控制信号 | J1 / U7 | `G0=J1-7, U7-3, NEOPIXEL/IRQ`；`G1=J1-8, U7-17, ADC/IRQ`；`G2=J1-9, U7-20, ADC/IRQ`；`G3=J1-10, U7-13, PWM/IRQ`；`G4=J1-11, U7-12, PWM/IRQ`；`wake_note=G0/G2 二选一，G3/G4 二选一` |
| 复位 | PWR_BTN | `connector_pin=J1-3`；`controller_pin=U7-7`；`controller_function=BTN_PU` |
| 接口 | BOOT_OUT / LED_PWR_EN | `boot_connector_pin=J1-5`；`boot_controller_pin=U7-15`；`boot_function=BOOT_OUT_OD`；`led_connector_pin=J1-6`；`led_controller_pin=U7-5`；`led_function=LED_EN_PP` |
| 其他事实 | Q2 / Q4 | `q4_pin2=VBAT`；`q4_pin3=R9 1K/1%`；`q4_pin1=R7 100K, Q2-D`；`divider=R9 1K/1%, R10 1K/1%`；`filter=C26 100nF/16V`；`q2_gate=VBAT_ADC_EN`；`q2_gate_pulldown=R22 10K/1%` |
| 其他事实 | SYS_5VIN | `input=SYS_5VIN`；`output=VIN_DETECT`；`upper=R12 10K/1%`；`lower=R13 10K/1%`；`filter=C16 100nF/25V` |
| 其他事实 | EXT_5V_INOUT | `input=EXT_5V_INOUT`；`output=EXT_5V_ADC`；`upper=R23 10K/1%`；`lower=R24 10K/1%`；`filter=C7 100nF/25V` |
| 其他事实 | U5 / R17 / R8 | `prog_pin=U5-2`；`prog_resistor=R17 5.1K/1%`；`selection_resistor=R8 2.2K/1%`；`control_net=CHG_PROG`；`connector_pin=J1-1` |
| 接口 | U5 / J1 | `chrg_pin=U5-7`；`status_net=CHRG_STAT`；`pullup=R11 1M/1%`；`pullup_rail=PY_3V3`；`connector_pin=J1-2`；`done_pin=U5-6 unconnected` |
| 关键网络 | 电源网络 | `input=5V_IN`；`protected_5v=SYS_5VIN`；`main_bus=SYS_VBUS`；`internal_5v=Internal_5V`；`external_5v=EXT_5V_INOUT`；`battery=VBAT`；`pmic_3v3=PY_3V3`；`ldo_3v3=3V3_LDO_OUT`；`dcdc_3v3=3V3_DCDC_OUT`；`boost=BOOST_OUT` |
| 核心器件 | U7 / M5PM1 | `schematic_symbol=U7`；`visible_part_label=PY32_PMIC`；`product_documented_ic=M5PM1` |
| 其他事实 | LGS4056HDA | `prog_resistor=R17 5.1K/1%`；`selection_resistor=R8 2.2K/1%`；`documented_profiles=650mA/180mA`；`mapping=unresolved` |

## 待确认事项

- `component.u7-m5pm1-mapping`：原理图中的 U7 符号底部仅标注 PY32_PMIC，未在可见符号中标注 M5PM1；M5PM1 产品命名与 U7 器件标识的对应关系待确认。（证据：图 566a5f4a5e33 / 第 1 页 / Logic Contor 区：U7 符号与底部 PY32_PMIC 标注）
- `other.charge-current-profile`：原理图显示 PROG 端 R17=5.1K/1% 与 R8=2.2K/1% 组成可切换编程网络，但未标注 650mA/180mA 两档电流与 CHG_PROG 状态的对应关系，档位映射待确认。（证据：图 566a5f4a5e33 / 第 1 页 / BAT Charge 区：U5 PROG、R17、R8 与 CHG_PROG）
- `review.u7-part-identity`：U7 的 PY32_PMIC 标识与产品资料中的 M5PM1 是同一器件的不同命名，还是模块与内部 PMIC 的层级关系？；原因：原理图可见符号仅标注 PY32_PMIC，未显示 M5PM1 与 U7 的直接对应文字。
- `review.charge-current-mapping`：CHG_PROG 的两种状态分别对应 650mA 与 180mA 中的哪一档？；原因：原理图仅给出 R17=5.1K/1% 与 R8=2.2K/1% 的编程网络，未给出电流档位映射。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `566a5f4a5e3303e6fc0780206bec04ef053f739c427f43d19afbab3da7e27990` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1294/S021_Stamp_Timer_Power2_SCH_V0.7.1_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp_Timer_Power2.md`

源文档 SHA-256：`930f168740cb1c03a3fef8354fe3147e52ccd05b68567b1faf998051854e243c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
