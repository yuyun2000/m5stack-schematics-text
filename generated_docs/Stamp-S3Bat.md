# Stamp-S3Bat 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3Bat |
| SKU | S015 |
| 产品 ID | `stamp-s3bat-7601115a7f19` |
| 源文档 | `zh_CN/core/Stamp-S3Bat.md` |

## 概述

Stamp-S3Bat 单页原理图以 U1 ESP32_S3_PICO_1 与 U2 PY32_PMIC 为核心，USB-C、5VIN 和 VBAT 经 AW32901FCR 与四颗 CH213K 组成输入和电池 PowerPath。U3 LGS4056HDA 负责充电，U4 JW5712 生成 3V3_L2，U11 TPAP7343D-33FS4 生成 3V3_L1，U6 SY7088 生成 EXT_5V_OUT。图面同时给出 IPEX-4 射频匹配、原生 USB、NeoPixel、24 针 BTB、11 路半孔 GPIO、外部唤醒信号和 PMIC 的电源/ADC/充电控制映射。产品源文档声明 ESP32-S3-PICO-1-N8R8、8MB Flash、8MB PSRAM、M5PM1 0x6E、WS2812、SH1.0、FPC 天线、0.4mm BTB、充电电流和模式功耗，但这些精确型号或参数未在图面完整标注，均列为待确认。

## 检索关键词

`Stamp-S3Bat`、`S015`、`ESP32-S3-PICO-1`、`ESP32-S3-PICO-1-N8R8`、`8MB Flash`、`8MB PSRAM`、`PY32_PMIC`、`M5PM1`、`M5PM1 0x6E`、`LGS4056HDA`、`JW5712`、`SY7088`、`TPAP7343D-33FS4`、`AW32901FCR`、`CH213K`、`USB Type-C`、`IPEX-4`、`FPC antenna`、`NeoPixel`、`WS2812`、`H1 BTB 24P`、`BTB0.408-24PLBDR-M41`、`J2 CON2`、`SH1.0-2P`、`SYS_VIN`、`SYS_VBUS`、`USB_VIN`、`VUSBIN`、`5VIN`、`VBAT`、`3V3_L1`、`3V3_L2`、`EXT_5V_OUT`、`3V3_L2_EN`、`CHG_EN`、`PY_G2_CHG_STAT`、`PY_G3_CHG_PROG`、`PY_G4_WAKE`、`5VOUT_EN`、`VUSB_ADC`、`5VIN_ADC`、`BAT_ADC`、`BAT_ADC_EN`、`G47_SCL`、`G48_SDA`、`G0_BOOT_OUT`、`SOC_RESET`、`U0TX/G43`、`U0RX/G44`、`DVP`、`2.54mm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32_S3_PICO_1 | 主控 SiP，连接 GPIO、原生 USB、UART、I2C、启动复位、射频和 NeoPixel | 图 941fad0422cf / 第 1 页 / 网格 A3-C4，U1 ESP32_S3_PICO_1 |
| U2 | PY32_PMIC | I2C 电源管理控制器，管理 DCDC、充电、5V 输出、ADC、唤醒、按键与 NeoPixel 使能 | 图 941fad0422cf / 第 1 页 / 网格 C3-D4，U2 PY32_PMIC |
| U3 | LGS4056HDA | SYS_VIN 至 VBAT 的锂电池充电管理器 | 图 941fad0422cf / 第 1 页 / 网格 A2，U3 LGS4056HDA Charge |
| U4 | JW5712 | SYS_VBUS 至 3V3_L2 的受控 DC/DC | 图 941fad0422cf / 第 1 页 / 网格 B1-B2，U4 JW5712 DCDC |
| U6 | SY7088 | SYS_VBUS 至 EXT_5V_OUT 的受控升压转换器 | 图 941fad0422cf / 第 1 页 / 网格 D2，U6 SY7088 |
| U11 | TPAP7343D-33FS4 | SYS_VBUS 至 3V3_L1 的 3.3V LDO | 图 941fad0422cf / 第 1 页 / 网格 C2，U11 TPAP7343D-33FS4 |
| U12 | AW32901FCR | VUSBIN 至 USB_VIN 的 USB 输入保护/负载开关 | 图 941fad0422cf / 第 1 页 / 网格 A1-B1，U12 AW32901FCR USB_IN |
| U5,U7,U8,U9 | CH213K | USB、5VIN、VBAT 与 SYS_VIN/SYS_VBUS 之间的四路二极管 PowerPath | 图 941fad0422cf / 第 1 页 / 网格 A2-B3，U5/U7/U8/U9 CH213K PowerPath |
| J4,L1,L2,C12,C20,C24 | IPEX_4 / RF matching | ESP32-S3 LNA_IN 的外接天线座与 50Ω 匹配网络 | 图 941fad0422cf / 第 1 页 / 网格 A3-A4，J4 IPEX_4 至 U1 LNA_IN |
| USB_C_16P_Horizontal | USB_C_16P_Horizontal | USB Type-C 电源和 USB D+/D- 接口 | 图 941fad0422cf / 第 1 页 / 网格 A1，USB_C_16P_Horizontal |
| LED1 | NeoPixel | 由 PY_LED_EN 供电、NeoPixel 数据驱动的可编程 RGB LED | 图 941fad0422cf / 第 1 页 / 网格 B4-C4，LED1 NeoPixel |
| H1 | BTB 24P | 24 针 BTB GPIO、电源、UART 与 I2C 接口 | 图 941fad0422cf / 第 1 页 / 网格 C1，H1 BTB pins1-24 |
| J3,J5 | Header 9P x2 | 半孔 GPIO、供电、5V 输出与外部唤醒接口 | 图 941fad0422cf / 第 1 页 / 网格 D1，J3/J5 Hole |
| J2 | CON2 | VBAT 与 GND 两针电池接口 | 图 941fad0422cf / 第 1 页 / 网格 B2，J2 CON2 |
| S1,TVS3 | PWR switch / LXES15AAA1-153 | PWR_BTN 电源按键与对地保护 | 图 941fad0422cf / 第 1 页 / 网格 C2，KEY S1/TVS3 |

## 系统结构

### Stamp-S3Bat 系统架构

单页图以 U1 ESP32_S3_PICO_1 与 U2 PY32_PMIC 为核心，USB-C、5VIN 和 VBAT 经输入保护与 CH213K PowerPath 进入 SYS_VIN/SYS_VBUS，再由充电、3.3V DC/DC、3.3V LDO 与 5V 升压级供电。

- 参数与网络：`controller=U1 ESP32_S3_PICO_1`；`power_controller=U2 PY32_PMIC`；`inputs=VUSBIN,5VIN,VBAT`；`main_rails=SYS_VIN,SYS_VBUS,3V3_L1,3V3_L2,EXT_5V_OUT`
- 证据：图 941fad0422cf / 第 1 页 / 完整单页的 CORE、USB_IN、Charge、PowerPath、DCDC 与 PY32_PMIC 区

## 核心器件

### ESP32_S3_PICO_1 主控

U1 标为 ESP32_S3_PICO_1，引出 GPIO0-GPIO21、GPIO38-GPIO48、原生 USB、UART0、CHIP_PU 与 LNA_IN；GPIO0 连接 G0_BOOT_OUT，CHIP_PU 连接 SOC_RESET。

- 参数与网络：`reference=U1`；`part_number=ESP32_S3_PICO_1`；`boot=GPIO0/G0_BOOT_OUT`；`reset=CHIP_PU/SOC_RESET`；`usb=GPIO19/20`；`uart=GPIO44 RX,GPIO43 TX`；`i2c=GPIO47 SCL,GPIO48 SDA`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A3-C4，U1 全部引脚

## 电源

### ESP32-S3 3V3_L2 供电

U1 的 VDDA、VDD3P3、VDD3P3_CPU 与 VDD3P3_RTC 接 3V3_L2，L5 2nH 位于模拟/射频支路；图面分别标注 0.6A max 和 600mA MAX，并要求主电源走线至少 10mil。

- 参数与网络：`rail=3V3_L2`；`filter=L5 2nH`；`current_annotations=0.6A max,600mA MAX`；`layout=10mil min`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A3-B4，U1 电源引脚、L5 与电流/线宽注释

### VUSBIN 输入保护

U12 AW32901FCR 的三路 IN 接 VUSBIN、三路 OUT 接 USB_VIN，nEN 通过 R11 0R 接地，OVLO 周围预留 R4 NC，输入输出各有 1uF 电容。

- 参数与网络：`device=U12 AW32901FCR`；`input=VUSBIN`；`output=USB_VIN`；`enable=nEN via R11 0R to GND`；`ovlo=R4 NC`；`capacitors=C2/C25 1uF`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A1-B1，U12 USB_IN

### USB 与 5VIN PowerPath

U5 CH213K 将 USB_VIN 单向送至 SYS_VIN，U7 CH213K 将 5VIN 单向送至同一 SYS_VIN 网络。

- 参数与网络：`usb_path=USB_VIN -> U5 CH213K -> SYS_VIN`；`dc_path=5VIN -> U7 CH213K -> SYS_VIN`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A2-B2，U5/U7 PowerPath

### VBAT 与 SYS_VIN PowerPath

U8 CH213K 将 VBAT 单向送至 SYS_VBUS，U9 CH213K 将 SYS_VIN 单向送至 SYS_VBUS；R17 NC 预留 SYS_VBUS 至 3V3_L1 的跨接。

- 参数与网络：`battery_path=VBAT -> U8 CH213K -> SYS_VBUS`；`input_path=SYS_VIN -> U9 CH213K -> SYS_VBUS`；`optional_link=R17 NC to 3V3_L1`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B2-B3，U8/U9/R17 PowerPath

### LGS4056HDA 充电链路

U3 LGS4056HDA 以 SYS_VIN 供电并向 VBAT 充电，DONE/CHRG/PROG/CE 分别连接 PY_G2_CHG_STAT、充电状态网络、PY_G3_CHG_PROG 和 CHG_EN。

- 参数与网络：`input=SYS_VIN`；`battery=VBAT`；`done=PY_G2_CHG_STAT`；`program=PY_G3_CHG_PROG`；`enable=CHG_EN`；`resistors=R15 100K,R3 2K,R14 5.1K,R16 1M`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A2，U3 LGS4056HDA Charge

### JW5712 3V3_L2 DC/DC

U4 JW5712 以 SYS_VBUS 为输入，3V3_L2_EN 控制 EN，SW 经 L4 FTC121065S2R2MBCA 输出 3V3_L2，VSEL1-3 均连接 SYS_VBUS。

- 参数与网络：`input=SYS_VBUS`；`enable=3V3_L2_EN`；`output=3V3_L2`；`inductor=L4 FTC121065S2R2MBCA`；`vsel=VSEL1/VSEL2/VSEL3=SYS_VBUS`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B1-B2，U4 JW5712 DCDC

### 3V3_L1 LDO

U11 TPAP7343D-33FS4 的 VIN 与 EN 接 SYS_VBUS，OUT 生成 3V3_L1，输入输出各配置 4.7uF 电容。

- 参数与网络：`input=SYS_VBUS`；`enable=SYS_VBUS`；`output=3V3_L1`；`capacitors=C29/C28 4.7uF`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C2，U11 TPAP7343D-33FS4

### SY7088 EXT_5V_OUT 升压

U6 SY7088 以 SYS_VBUS 为输入，5VOUT_EN 控制 EN，经 L3 FTC201610S2R2MBCA 输出 EXT_5V_OUT，反馈分压为 R22 147K 与 R27 46.4K。

- 参数与网络：`input=SYS_VBUS`；`enable=5VOUT_EN`；`output=EXT_5V_OUT`；`inductor=L3 FTC201610S2R2MBCA`；`feedback=R22 147K/R27 46.4K`
- 证据：图 941fad0422cf / 第 1 页 / 网格 D2，U6 SY7088

## 接口

### USB Type-C 接口

USB_C_16P_Horizontal 的 VBUS 接 VUSBIN，DP1/DP2 合并为 USB_DP，DM1/DM2 合并为 USB_DM，CC1/CC2 分别通过 R1/R2 5.1K 接地，TVS1/TVS2 ESD5311 对 D+/D- 提供保护。

- 参数与网络：`vbus=VUSBIN`；`dp=USB_DP`；`dm=USB_DM`；`cc1=R1 5.1K`；`cc2=R2 5.1K`；`esd=TVS1/TVS2 ESD5311`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A1，USB_C_16P_Horizontal/R1/R2/TVS1/TVS2

### 24 针 BTB 电气映射

H1 pins1-24 依次引出 G40/G46、G38/G45、G12/G41、G13/U0TX-G43、G14/G42、G15/G39、G16/GND、G18/G17、G21/U0RX-G44、3V3_L2/G47_SCL、SYS_VBUS/GND、SYS_VBUS/G48_SDA。

- 参数与网络：`pins_1_8=1 G40,2 G46,3 G38,4 G45,5 G12,6 G41,7 G13,8 U0TX/G43`；`pins_9_16=9 G14,10 G42,11 G15,12 G39,13 G16,14 GND,15 G18,16 G17`；`pins_17_24=17 G21,18 U0RX/G44,19 3V3_L2,20 G47_SCL,21 SYS_VBUS,22 GND,23 SYS_VBUS,24 G48_SDA`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C1，H1 BTB 完整 pin map

### 半孔 GPIO 与电源映射

J3 pins1-9 为 G1、G2、G3、G4、G5、GND、EXT_5V_OUT、G6、G7；J5 pins1-9 为 5VIN、3V3_L2、VBAT、G8、G9、G10、G11、PY_G4_WAKE、GND。

- 参数与网络：`j3=G1,G2,G3,G4,G5,GND,EXT_5V_OUT,G6,G7`；`j5=5VIN,3V3_L2,VBAT,G8,G9,G10,G11,PY_G4_WAKE,GND`；`gpio_count=11`；`wake_count=1`
- 证据：图 941fad0422cf / 第 1 页 / 网格 D1，J3/J5 Hole

## 总线

### PY32_PMIC I2C 总线

U2 I2C_SCL_OD 与 I2C_SDA_OD 分别连接 G47_SCL 与 G48_SDA，R21/R23 各 2.2K 上拉到 3V3_L2；U1 GPIO47/GPIO48 连接同名网络。

- 参数与网络：`scl=U1 GPIO47/G47_SCL -> U2 I2C_SCL_OD`；`sda=U1 GPIO48/G48_SDA -> U2 I2C_SDA_OD`；`pullups=R21/R23 2.2K to 3V3_L2`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B3-D4，U1 G47/G48、R21/R23 与 U2 I2C pins

## GPIO 与控制信号

### PY32_PMIC 电源控制输出

U2 的 DCDC3V3_EN_PP、CHG_EN_PP、G1_IRQout_ADC、LED_EN_PP 和 BOOT_OUT_OD 分别连接 3V3_L2_EN、CHG_EN、5VOUT_EN、PY_LED_EN 与 G0_BOOT_OUT。

- 参数与网络：`dcdc_enable=3V3_L2_EN`；`charge_enable=CHG_EN`；`boost_enable=5VOUT_EN`；`led_enable=PY_LED_EN`；`boot_output=G0_BOOT_OUT`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C3-D4，U2 power/LED/boot outputs

### PMIC 唤醒与充电信号

U2 G0、G2、G4、G3 对应 NeoPixel、PY_G2_CHG_STAT、PY_G4_WAKE、PY_G3_CHG_PROG，其中图面将 G0/G2 与 G4/G3 分别标注为两组唤醒源二选一。

- 参数与网络：`g0=NeoPixel`；`g2=PY_G2_CHG_STAT`；`g4=PY_G4_WAKE`；`g3=PY_G3_CHG_PROG`；`annotation=two wake-source mux pairs`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C4-D4，U2 G0/G2/G4/G3 与唤醒源二选一注释

### 可编程 RGB LED

LED1 的 VDD 接 PY_LED_EN、GND 接地、DIN 接 NeoPixel，DOUT 标未连接；U2 以 LED_EN_PP 驱动 PY_LED_EN，并由 G0 信号连接 NeoPixel 数据。

- 参数与网络：`reference=LED1`；`power=PY_LED_EN`；`data=NeoPixel`；`dout=NC`；`controller=U2 LED_EN_PP/G0`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B4-C4，LED1 与 U2 NeoPixel/PY_LED_EN

### PWR_BTN 按键

S1 按下时将 PWR_BTN 接地，TVS3 LXES15AAA1-153 对 PWR_BTN 提供对地保护；U2 BTN_PU 连接 PWR_BTN，并注释内部上拉默认启用。

- 参数与网络：`button=S1 to GND`；`net=PWR_BTN`；`protection=TVS3 LXES15AAA1-153`；`pmic_pin=U2 BTN_PU`；`pullup=internal enabled by default`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C2-D4，KEY S1/TVS3 与 U2 BTN_PU

## 复位

### 主控复位与启动

SOC_RESET 由 R12 10K 上拉至 3V3_L2 并由 C1 1uF 接地，连接 U1 CHIP_PU；G0_BOOT_OUT 由 R13 100K 上拉至 3V3_L2，连接 U1 GPIO0。

- 参数与网络：`reset=SOC_RESET`；`reset_pullup=R12 10K`；`reset_capacitor=C1 1uF`；`boot=G0_BOOT_OUT`；`boot_pullup=R13 100K`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B3，SOC_RESET/G0_BOOT_OUT RC 与 U1

## 射频

### IPEX-4 射频匹配

J4 IPEX_4 经 C12、L2 与 C20/C24 匹配网络连接 U1 LNA_IN，L1 提供并联接地匹配；图面注释为 50Ω 阻抗匹配并给出两组元件靠近端口/芯片的布局要求。

- 参数与网络：`connector=J4 IPEX_4`；`soc_pin=U1 LNA_IN`；`series=C12,L2`；`shunt=L1,C20,C24`；`impedance=50 ohm`
- 证据：图 941fad0422cf / 第 1 页 / 网格 A3-A4，J4 至 U1 LNA_IN 与 50Ω 注释

## 调试与烧录

### ESP32-S3 原生 USB

USB_DM 与 USB_DP 分别经 R36/R35 33R 和 FT1 共模器件连接 U1 GPIO19/G19 与 GPIO20/G20，形成原生 USB 数据路径。

- 参数与网络：`dm=USB_DM -> R36 33R -> FT1 -> GPIO19`；`dp=USB_DP -> R35 33R -> FT1 -> GPIO20`；`filter=FT1 SDMM0806H-2-900T`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B3，USB_DM/DP、R35/R36、FT1 与 U1 G19/G20

### USB 与启动调试接口

JP1 引出 VUSBIN、USB_DM、USB_DP、G0_BOOT_OUT 与 GND；测试点另引出 PY_LED_EN、BAT_ADC_EN、G0_BOOT_OUT、U0RX/G44、U0TX/G43、SYS_VBUS 与 SYS_VIN。

- 参数与网络：`header=JP1`；`header_signals=VUSBIN,USB_DM,USB_DP,G0_BOOT_OUT,GND`；`testpoints=PY_LED_EN,BAT_ADC_EN,G0_BOOT_OUT,U0RX/G44,U0TX/G43,SYS_VBUS,SYS_VIN`
- 证据：图 941fad0422cf / 第 1 页 / 网格 B3-C4，JP1 与 TP1-TP8

## 模拟电路

### 输入与电池电压监测

U2 的 5VOUT_ADC_IN、5VIN_ADC_IN、BAT_ADC_IN 分别连接 VUSB_ADC、5VIN_ADC、BAT_ADC；5VIN 和 USB_VIN 通过 10K/10K 分压与 100nF 滤波形成 5VIN_ADC 和 VUSB_ADC。

- 参数与网络：`usb_adc=USB_VIN -> R5/R6 10K -> VUSB_ADC`；`dc_adc=5VIN -> R19/R20 10K -> 5VIN_ADC`；`battery_adc=BAT_ADC`；`filters=C5/C31 100nF`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C3-D4，ADC 分压与 U2 ADC inputs

### BAT_ADC 受控采样

VBAT 通过 Q1 与 R8/R7 分压形成 BAT_ADC，Q2 与 R10 由 BAT_ADC_EN 控制分压下端，U2 BAT_ADC_EN_OD 连接 BAT_ADC_EN。

- 参数与网络：`input=VBAT`；`switches=Q1/Q2 CJ3139K`；`divider=R8/R7 1K`；`enable=BAT_ADC_EN`；`output=BAT_ADC`
- 证据：图 941fad0422cf / 第 1 页 / 网格 C3，Q1/Q2/R7-R10 BAT_ADC 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3Bat 系统架构 | `controller=U1 ESP32_S3_PICO_1`；`power_controller=U2 PY32_PMIC`；`inputs=VUSBIN,5VIN,VBAT`；`main_rails=SYS_VIN,SYS_VBUS,3V3_L1,3V3_L2,EXT_5V_OUT` |
| 核心器件 | ESP32_S3_PICO_1 主控 | `reference=U1`；`part_number=ESP32_S3_PICO_1`；`boot=GPIO0/G0_BOOT_OUT`；`reset=CHIP_PU/SOC_RESET`；`usb=GPIO19/20`；`uart=GPIO44 RX,GPIO43 TX`；`i2c=GPIO47 SCL,GPIO48 SDA` |
| 复位 | 主控复位与启动 | `reset=SOC_RESET`；`reset_pullup=R12 10K`；`reset_capacitor=C1 1uF`；`boot=G0_BOOT_OUT`；`boot_pullup=R13 100K` |
| 射频 | IPEX-4 射频匹配 | `connector=J4 IPEX_4`；`soc_pin=U1 LNA_IN`；`series=C12,L2`；`shunt=L1,C20,C24`；`impedance=50 ohm` |
| 电源 | ESP32-S3 3V3_L2 供电 | `rail=3V3_L2`；`filter=L5 2nH`；`current_annotations=0.6A max,600mA MAX`；`layout=10mil min` |
| 接口 | USB Type-C 接口 | `vbus=VUSBIN`；`dp=USB_DP`；`dm=USB_DM`；`cc1=R1 5.1K`；`cc2=R2 5.1K`；`esd=TVS1/TVS2 ESD5311` |
| 调试与烧录 | ESP32-S3 原生 USB | `dm=USB_DM -> R36 33R -> FT1 -> GPIO19`；`dp=USB_DP -> R35 33R -> FT1 -> GPIO20`；`filter=FT1 SDMM0806H-2-900T` |
| 电源 | VUSBIN 输入保护 | `device=U12 AW32901FCR`；`input=VUSBIN`；`output=USB_VIN`；`enable=nEN via R11 0R to GND`；`ovlo=R4 NC`；`capacitors=C2/C25 1uF` |
| 电源 | USB 与 5VIN PowerPath | `usb_path=USB_VIN -> U5 CH213K -> SYS_VIN`；`dc_path=5VIN -> U7 CH213K -> SYS_VIN` |
| 电源 | VBAT 与 SYS_VIN PowerPath | `battery_path=VBAT -> U8 CH213K -> SYS_VBUS`；`input_path=SYS_VIN -> U9 CH213K -> SYS_VBUS`；`optional_link=R17 NC to 3V3_L1` |
| 电源 | LGS4056HDA 充电链路 | `input=SYS_VIN`；`battery=VBAT`；`done=PY_G2_CHG_STAT`；`program=PY_G3_CHG_PROG`；`enable=CHG_EN`；`resistors=R15 100K,R3 2K,R14 5.1K,R16 1M` |
| 电源 | JW5712 3V3_L2 DC/DC | `input=SYS_VBUS`；`enable=3V3_L2_EN`；`output=3V3_L2`；`inductor=L4 FTC121065S2R2MBCA`；`vsel=VSEL1/VSEL2/VSEL3=SYS_VBUS` |
| 电源 | 3V3_L1 LDO | `input=SYS_VBUS`；`enable=SYS_VBUS`；`output=3V3_L1`；`capacitors=C29/C28 4.7uF` |
| 电源 | SY7088 EXT_5V_OUT 升压 | `input=SYS_VBUS`；`enable=5VOUT_EN`；`output=EXT_5V_OUT`；`inductor=L3 FTC201610S2R2MBCA`；`feedback=R22 147K/R27 46.4K` |
| 总线 | PY32_PMIC I2C 总线 | `scl=U1 GPIO47/G47_SCL -> U2 I2C_SCL_OD`；`sda=U1 GPIO48/G48_SDA -> U2 I2C_SDA_OD`；`pullups=R21/R23 2.2K to 3V3_L2` |
| GPIO 与控制信号 | PY32_PMIC 电源控制输出 | `dcdc_enable=3V3_L2_EN`；`charge_enable=CHG_EN`；`boost_enable=5VOUT_EN`；`led_enable=PY_LED_EN`；`boot_output=G0_BOOT_OUT` |
| 模拟电路 | 输入与电池电压监测 | `usb_adc=USB_VIN -> R5/R6 10K -> VUSB_ADC`；`dc_adc=5VIN -> R19/R20 10K -> 5VIN_ADC`；`battery_adc=BAT_ADC`；`filters=C5/C31 100nF` |
| 模拟电路 | BAT_ADC 受控采样 | `input=VBAT`；`switches=Q1/Q2 CJ3139K`；`divider=R8/R7 1K`；`enable=BAT_ADC_EN`；`output=BAT_ADC` |
| GPIO 与控制信号 | PMIC 唤醒与充电信号 | `g0=NeoPixel`；`g2=PY_G2_CHG_STAT`；`g4=PY_G4_WAKE`；`g3=PY_G3_CHG_PROG`；`annotation=two wake-source mux pairs` |
| GPIO 与控制信号 | 可编程 RGB LED | `reference=LED1`；`power=PY_LED_EN`；`data=NeoPixel`；`dout=NC`；`controller=U2 LED_EN_PP/G0` |
| GPIO 与控制信号 | PWR_BTN 按键 | `button=S1 to GND`；`net=PWR_BTN`；`protection=TVS3 LXES15AAA1-153`；`pmic_pin=U2 BTN_PU`；`pullup=internal enabled by default` |
| 接口 | 24 针 BTB 电气映射 | `pins_1_8=1 G40,2 G46,3 G38,4 G45,5 G12,6 G41,7 G13,8 U0TX/G43`；`pins_9_16=9 G14,10 G42,11 G15,12 G39,13 G16,14 GND,15 G18,16 G17`；`pins_17_24=17 G21,18 U0RX/G44,19 3V3_L2,20 G47_SCL,21 SYS_VBUS,22 GND,23 SYS_VBUS,24 G48_SDA` |
| 接口 | 半孔 GPIO 与电源映射 | `j3=G1,G2,G3,G4,G5,GND,EXT_5V_OUT,G6,G7`；`j5=5VIN,3V3_L2,VBAT,G8,G9,G10,G11,PY_G4_WAKE,GND`；`gpio_count=11`；`wake_count=1` |
| 调试与烧录 | USB 与启动调试接口 | `header=JP1`；`header_signals=VUSBIN,USB_DM,USB_DP,G0_BOOT_OUT,GND`；`testpoints=PY_LED_EN,BAT_ADC_EN,G0_BOOT_OUT,U0RX/G44,U0TX/G43,SYS_VBUS,SYS_VIN` |
| 核心器件 | ESP32-S3-PICO-1-N8R8 与存储容量 | `documented_part=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB Octal`；`schematic_part=ESP32_S3_PICO_1`；`internal_memory_shown=false` |
| 核心器件 | M5PM1 电源管理器与地址 | `documented_name=M5PM1`；`alternate_spelling=M5MP1`；`documented_address=0x6E`；`schematic_label=PY32_PMIC`；`part_number=null`；`firmware=null` |
| 电源 | 可切换充电电流 | `documented_low=650mA`；`documented_float=200mA`；`control=PY_G3_CHG_PROG`；`schematic=U3 PROG/R3/R14` |
| 电源 | 3.7V 电池与 SH1.0 接口 | `documented_battery=3.7V Li-ion`；`documented_connector=SH1.0-2P`；`schematic_connector=J2 CON2`；`nets=VBAT,GND` |
| 接口 | BTB 料号、间距与 DVP 支持 | `documented_part=BTB0.408-24PLBDR-M41`；`documented_pitch=0.4mm`；`documented_function=DVP`；`schematic=H1 24-pin generic pin map` |
| 射频 | 2.4GHz Wi-Fi 与 FPC 天线 | `documented_radio=2.4GHz Wi-Fi`；`documented_antenna=FPC antenna`；`connector=J4 IPEX_4`；`schematic_frequency=null`；`antenna_part=null` |
| GPIO 与控制信号 | WS2812 RGB LED 型号 | `documented_part=WS2812`；`schematic_label=LED1 NeoPixel`；`data=NeoPixel`；`power=PY_LED_EN` |
| 系统结构 | CPU 主频与模式功耗 | `documented_cpu=dual-core Xtensa LX7 up to 240MHz`；`documented_power=13.43uA sleep,955.36uA standby,26.83mA light,27.49mA full at 4.2V`；`schematic_measurements=null` |
| 接口 | 2.54mm 半孔间距 | `documented_pitch=2.54mm`；`documented_assembly=SMT,DIP`；`schematic=J3/J5 electrical map only` |
| 电源 | 外部低功耗唤醒行为 | `signal=PY_G4_WAKE`；`pmic_pin=U2 G4_WAKEin`；`connector=J5 pin8`；`trigger_polarity=null`；`timing=null` |

## 待确认事项

- `component.documented-soc-memory`：产品源文档标注 ESP32-S3-PICO-1-N8R8、8MB Flash 和 8MB Octal PSRAM；图面 U1 只标 ESP32_S3_PICO_1，未打印 N8R8 后缀或内部 Flash/PSRAM 容量。（证据：图 941fad0422cf / 第 1 页 / U1 仅标 ESP32_S3_PICO_1，无 N8R8/容量字段）
- `component.documented-m5pm1`：产品源文档将电源控制器称为 M5PM1 并标注 I2C 地址 0x6E，正文另出现 M5MP1 拼写；图面 U2 只标 PY32_PMIC，未给芯片具体型号、固件版本或 I2C 地址。（证据：图 941fad0422cf / 第 1 页 / U2 PY32_PMIC 与 G47_SCL/G48_SDA，未标地址）
- `power.documented-charge-current`：产品源文档称 PY_G3_CHG_PROG 低电平对应 650mA、浮空对应 200mA；图面显示 U3 PROG 与 PY_G3_CHG_PROG/R3/R14 的连接，但未直接标出两档充电电流。（证据：图 941fad0422cf / 第 1 页 / U3 LGS4056HDA PROG 与 PY_G3_CHG_PROG）
- `power.documented-battery-interface`：产品源文档标注外接 3.7V 锂电池和 SH1.0-2P 电池座，图面 J2 只标 CON2 与 VBAT/GND，未标连接器系列、间距、电池电压范围或极性实物方向。（证据：图 941fad0422cf / 第 1 页 / J2 CON2 VBAT/GND）
- `interface.documented-btb-dvp`：产品源文档标注 BTB0.408-24PLBDR-M41、24P 0.4mm 接口并声明支持 DVP；图面 H1 只给 24 针 GPIO/电源映射，没有连接器料号、间距或 DVP 专用网络名。（证据：图 941fad0422cf / 第 1 页 / H1 BTB 仅标 pins1-24 与 GPIO/电源）
- `rf.documented-wireless-antenna`：产品源文档标注 2.4GHz Wi-Fi、IPEX-4 和 FPC 天线；图面确认 J4 IPEX_4 与 50Ω 匹配网络，但没有画出 FPC 天线本体，也未标频段、协议或射频性能。（证据：图 941fad0422cf / 第 1 页 / J4 IPEX_4 至 U1 LNA_IN，未画 FPC 天线）
- `gpio.documented-ws2812`：产品源文档标注 1 颗 WS2812，图面 LED1 只标 NeoPixel 并给出电源、DIN 与 DOUT，未标具体 LED 料号。（证据：图 941fad0422cf / 第 1 页 / LED1 NeoPixel，无 WS2812 料号）
- `system.documented-performance`：产品源文档标注双核 Xtensa LX7 最高 240MHz，并列出休眠、待机、轻载和满载电流；原理图未直接标 CPU 主频、测试条件、固件版本或整机模式功耗。（证据：图 941fad0422cf / 第 1 页 / U1 与完整电源图，无 CPU 主频或模式功耗标注）
- `interface.documented-half-hole-pitch`：产品源文档标注 2.54mm 标准间距并支持 SMT/DIP，图面 J3/J5 只给 9 针半孔电气映射，没有机械间距、封装尺寸或装配方式。（证据：图 941fad0422cf / 第 1 页 / J3/J5 Hole，无机械尺寸）
- `power.documented-external-wakeup`：产品源文档称主控休眠后可由外部 PY_G4_WAKE 重新启动电源；图面确认 PY_G4_WAKE 连接 U2 G4_WAKEin 并引到 J5，但未完整给出低功耗状态机、触发极性、时序或功耗边界。（证据：图 941fad0422cf / 第 1 页 / U2 PY_G4_WAKE 与 J5 pin8）
- `review.soc-memory`：请确认 S015 量产 U1 是否固定为 ESP32-S3-PICO-1-N8R8，并核对 8MB Flash 与 8MB Octal PSRAM。；原因：图面只标 ESP32_S3_PICO_1，未打印 N8R8 后缀或容量。
- `review.m5pm1`：请确认 U2 的具体 PY32 型号、M5PM1 固件版本与 7-bit 地址 0x6E，并统一 M5PM1/M5MP1 命名。；原因：图面仅标 PY32_PMIC 且无地址，产品源文档存在两种拼写。
- `review.charge-current`：请确认 PY_G3_CHG_PROG 低电平 650mA、浮空 200mA 的条件、容差与电池适用范围。；原因：两档电流只在产品源文档说明，图面未标数值。
- `review.battery-interface`：请确认 J2 是否为 SH1.0-2P、实物极性方向及支持的 3.7V 电池电压和容量范围。；原因：图面只标 J2 CON2 与 VBAT/GND。
- `review.btb-dvp`：请确认 H1 的 BTB0.408-24PLBDR-M41 料号、0.4mm 间距及 DVP 推荐 GPIO 映射。；原因：原理图仅提供通用 GPIO/电源电气映射。
- `review.wireless-antenna`：请确认配套 FPC 天线料号、2.4GHz 匹配值、装配约束与射频性能。；原因：图面仅显示 IPEX-4 与匹配网络，不含 FPC 天线和性能参数。
- `review.ws2812`：请确认 LED1 的具体 WS2812 系列料号、电气额定值与颜色顺序。；原因：图面仅标 NeoPixel。
- `review.performance`：请确认 240MHz 与四种模式功耗的固件、外设、电池电压、温度和测量条件。；原因：性能与功耗数据未在原理图中标注。
- `review.half-hole-pitch`：请用机械图或封装确认 J3/J5 半孔 2.54mm 间距、焊盘尺寸与 SMT/DIP 装配边界。；原因：原理图只给电气引脚。
- `review.external-wakeup`：请确认 PY_G4_WAKE 的有效电平、最小脉宽、低功耗状态机和重新上电时序。；原因：图面只显示 U2 与 J5 的信号连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `941fad0422cfd8c2d78b20c7ce9a11036dd887596524ce8c3577f7dc2796e0e7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1222/S015-SCH_Stamp-S3BAT_page_01.png` |

---

源文档：`zh_CN/core/Stamp-S3Bat.md`

源文档 SHA-256：`954acdc1ed0b6e69d2e7435232dd0bb39d5535a2d96f536f2a3aa09dc0983411`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
