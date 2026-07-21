# StopWatch 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StopWatch |
| SKU | C152 |
| 产品 ID | `stopwatch-1414a8f866be` |
| 源文档 | `zh_CN/core/StopWatch.md` |

## 概述

StopWatch C152 的四张原理图资源由 ESP32-S3R8、W25Q128JVPIQ、M5PM1 与 M5IOE1 构成核心，采用 L0/L1/L2/L3B 分层电源，集成 USB-C 充电、450mAh 电池、1.75 英寸 466×466 AMOLED 与 CST820 触摸、ES8311 音频、AW8737A 扬声器功放、BMI270、RX8130CE、震动电机、双向供电 Grove 及 USB/UART 可切换背部扩展总线。

## 检索关键词

`StopWatch`、`C152`、`ESP32-S3R8`、`ESP32-S3-R8N8`、`W25Q128JVPIQ`、`M5PM1`、`M5IOE1`、`PY32L020F15U6`、`LGS4056HDA`、`AW32901FCR`、`JW5712`、`SSP7615-33DFR`、`SY7088`、`AW35112FDR`、`AW35122FDR`、`AMOLED`、`466x466`、`CST820`、`CO5300`、`ES8311`、`AW8737A`、`BMI270`、`RX8130CE`、`CH442E`、`PYB_MUX_CTR`、`PYB_L3B_EN`、`PYB_AU_EN`、`PYB_MT_PWM`、`PYB_SPK_EN`、`PYB_TP_RST`、`PYB_OLED_RST`、`VBUS_L0`、`3V3_L0`、`3V3_L1`、`3V3_L2`、`3V3_L3B`、`AU_L3B`、`G47_SYS_SDA`、`G48_SYS_SCL`、`G19_USB_N`、`G20_USB_P`、`GROVE_5V`、`MUX_IO_1`、`MUX_IO_2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U16 | ESP32-S3R8 | 主控 SoC，连接 Flash、USB、OLED、触摸、音频、M5PM1、M5IOE1、IMU、RTC、按键和扩展 GPIO | 图 32ad59d9046e / 第 1 页 / 页 4 Core MCU 区 A2-D5，U16 ESP32_S3R8 |
| U17 | W25Q128JVPIQ | ESP32-S3R8 外部 NOR Flash | 图 32ad59d9046e / 第 1 页 / 页 4 D5-D6，U17 W25Q128JVPIQ |
| U9 | M5PM1 / PY32L020F15U6 | 多级电源管理、充电控制、ADC 检测、状态灯、按键和唤醒控制器 | 图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions 与 I/Os Map，M5PM1=PY32L020F15U6; 图 d351267c117d / 第 1 页 / 页 3 PMIC 区 B3-D4，U9 M5PM1 |
| U23 | M5IOE1 / PY32L020F15U6_IIC | I2C IO 扩展与外设控制器，管理显示、触摸、音频、扬声器、震动和扩展口复用 | 图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions 与 I/Os Map，M5IOE1=PY32L020F15U6_IIC; 图 635ac5af0356 / 第 1 页 / 页 5 PYB_IIC 区 B2-C3，U23 M5IOE1 |
| J1,U2 | USB Type-C / AW32901FCR | USB-C 电源与数据输入，以及 VUSB_IN 到 5V_IN 的过压保护 | 图 d351267c117d / 第 1 页 / 页 3 TYPEC/PROTECTION 区 A1-A2，J1 与 U2 AW32901FCR |
| U1 | LGS4056HDA | Internal_5V 到 VBAT_L0 的锂电池充电控制器 | 图 d351267c117d / 第 1 页 / 页 3 CHARGE 区 A2-A3，U1 LGS4056HDA |
| U3,U4,U5,U15,U27 | CH213K | 5V_IN、Internal_5V、VBAT_L0、VBUS_L0 与 Grove 输入之间的电源路径器件 | 图 d351267c117d / 第 1 页 / 页 3 A2-A3/D2-D3，U3/U4/U5/U15 CH213K; 图 635ac5af0356 / 第 1 页 / 页 5 Ext.Port 区 D2-D3，U27 CH213K |
| U6,U8,U12,U13 | SSP7615-33DFR | 从 VBUS_L0 生成 3V3_L0、3V3_L1、3V3_L3B 与 AU_L3B 的低静态电流 LDO | 图 d351267c117d / 第 1 页 / 页 3 L0/L1/L3_SW 区 B1-D2，U6/U8/U12/U13 |
| U10 | JW5712 | 由 PM_3V3_L2_EN 控制的 VBUS_L0 到 3V3_L2 电源转换器 | 图 d351267c117d / 第 1 页 / 页 3 L2_SW 区 C1-C2，U10 JW5712 |
| U7,U11,U14 | SY7088 / AW35112FDR / AW35122FDR | Grove 5V 双向供电路径的升压、输出和输入开关 | 图 d351267c117d / 第 1 页 / 页 3 GROVE 区 B2-D3，U7/U11/U14 |
| U18 | BMI270 | 0x68 I2C 六轴 IMU，提供 IMU_INT 唤醒信号 | 图 635ac5af0356 / 第 1 页 / 页 5 IMU&MAG 区 A1-A2，U18 BMI270，IIC Address 0x68 |
| U20 | RX8130CE | 0x32 I2C RTC，与 IMU 共同形成低功耗唤醒请求 | 图 635ac5af0356 / 第 1 页 / 页 5 RTC 区 A3，U20 RX8130CE，IIC Address 0x32 |
| U22 | ES8311 | 0x18 I2C/I2S 音频编解码器，连接 MEMS 麦克风与扬声器 DAC | 图 635ac5af0356 / 第 1 页 / 页 5 AUDIO 区 B1-C2，U22 ES8311，IIC Address 0x18 |
| U19 | LMA3729T381-0Y35 | AU_L3B 供电的模拟 MEMS 麦克风 | 图 635ac5af0356 / 第 1 页 / 页 5 MIC 区 A4，U19 与 MIC1_P/MIC1_N |
| U25,J7 | AW8737A / SPK 2-pin | 受 PYB_SPK_EN 控制的扬声器功放与差分扬声器接口 | 图 635ac5af0356 / 第 1 页 / 页 5 SPEAKER 区 D1-D2，U25 AW8737A 与 J7 |
| M1,Q4 | MOTOR_0610 / 2N7002KT | 由 PYB_MT_PWM 控制的震动电机与低侧驱动 | 图 635ac5af0356 / 第 1 页 / 页 5 MOTOR 区 A4，M1/Q4/D5 |
| J4,U24 | HC-FPC-03-10-31RLTAG / NC(AW35122FDR) | 31-pin 触摸与 AMOLED FPC 接口及预留显示电源开关 | 图 635ac5af0356 / 第 1 页 / 页 5 TP&OLED 区 B3-C4，J4 与 U24 NC(AW35122FDR) |
| U26 | CH442E | 由 PYB_MUX_CTR 控制的 UART0/USB 到 MUX_IO_1/2 双路复用器 | 图 635ac5af0356 / 第 1 页 / 页 5 Ext.Port&CH442E 区 D2-D3，U26 CH442E |
| S1,S2,S3 | SW | 一个 PWR_BTN 电源按键和两个低有效 KEY1/KEY2 用户按键 | 图 d351267c117d / 第 1 页 / 页 3 PMIC 区 B3，S1 PWR_BTN; 图 635ac5af0356 / 第 1 页 / 页 5 Button 区 D4，S2/S3 |
| J3 | HY2.0-4P | 双向 5V Grove 端口，信号为 EXT_GPIO11/EXT_GPIO10 | 图 d351267c117d / 第 1 页 / 页 3 GROVE 区 C2-C3，J3 pins1-4 |
| ANT1 | ANT_PIFA | ESP32-S3R8 板载天线及匹配网络 | 图 32ad59d9046e / 第 1 页 / 页 4 Core MCU 区 A1，ANT1/L3/L4/C39-C42/D4 |
| X1 | 40MHz/15pF/10ppm | ESP32-S3R8 主晶振 | 图 32ad59d9046e / 第 1 页 / 页 4 C5-C6，X1 40MHz/15pF/10ppm |

## 系统结构

### StopWatch 四页硬件架构

StopWatch 以 ESP32-S3R8、外部 NOR Flash、M5PM1 和 M5IOE1 为核心，集成分层电源、USB-C 充电、电池、AMOLED/触摸、ES8311 音频、AW8737A 扬声器、BMI270、RX8130CE、震动电机、Grove 与 USB/UART 可切换扩展总线。

- 参数与网络：`schematic_page_count=4`；`sku=C152`
- 证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions、Power Network、Power Mode 与 I/Os Map 全页; 图 d351267c117d / 第 1 页 / 页 3 电源与 Grove 全页; 图 32ad59d9046e / 第 1 页 / 页 4 Core MCU 全页; 图 635ac5af0356 / 第 1 页 / 页 5 IMU/RTC/Audio/Motor/TP&OLED/Ext.Port 全页

### L0/L1/L2/L3A/L3B 电源模式

系统图定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE、L3B All ACTIVE。M5PM1 与电池贯穿各状态；RTC/IMU 从 L1 起活动，ESP32-S3、按键、触摸、M5IOE1 与 CH442E 从 L2 起活动，OLED、震动、音频、麦克风与扬声器仅在 L3B 活动。

- 参数与网络：`shipping=L0`；`standby=L1`；`deep_sleep=L2`；`core_active=L3A`；`all_active=L3B`
- 证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions 区 A1-B3 与 Power Mode 区 C1-D3

## 电源

### USB 输入、充电与 450mAh 电池

J1 USB-C VBUS 形成 VUSB_IN，经 U2 AW32901FCR 输出 5V_IN，再由 U4 CH213K 形成 Internal_5V；U1 LGS4056HDA 从 Internal_5V 给 VBAT_L0 充电，J2 为电池接口。页 2 Functions 明确标注 450mAh Li-ion Battery。

- 参数与网络：`battery_capacity_mah=450`；`charger=LGS4056HDA`；`protected_input=5V_IN`
- 证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions/Power Network，450mAh 与 USB/Charge/Battery; 图 d351267c117d / 第 1 页 / 页 3 TYPEC/PROTECTION/CHARGE 区 A1-B3，J1/U2/U4/U1/J2

### 185mA/425mA 充电电流选择

U1 LGS4056HDA 的 PROG 由 PMG3_CHG_PROG 控制，图注给出默认充电电流 185mA，PYG3 低电平时为 425mA；CHRG 输出 PMG2_CHG_STAT，CE 接 PM_CHG_EN。

- 参数与网络：`default_current_ma=185`；`low_level_current_ma=425`；`program_net=PMG3_CHG_PROG`；`status_net=PMG2_CHG_STAT`
- 证据：图 d351267c117d / 第 1 页 / 页 3 CHARGE 区 A2-A3，U1 与 Charging Current 注记

### Internal_5V 与 VBAT_L0 汇入 VBUS_L0

U3 CH213K 将 Internal_5V 送到 VBUS_L0，U5 CH213K 将 VBAT_L0 送到同一 VBUS_L0，形成外部输入与电池供电的共享系统母线。

- 参数与网络：`input_a=Internal_5V`；`input_b=VBAT_L0`；`output=VBUS_L0`
- 证据：图 d351267c117d / 第 1 页 / 页 3 CHARGE 区 A2-B3，U3/U5 CH213K 与 VBUS_L0

### 3V3_L0/L1/L2/L3B 与 AU_L3B

U6 SSP7615-33DFR 从 VBUS_L0 常开输出 3V3_L0；U8 SSP7615-33DFR 由 PM_3V3_L1_EN 控制输出 3V3_L1；U10 JW5712 由 PM_3V3_L2_EN 控制输出 3V3_L2；U12/U13 SSP7615-33DFR 分别由 PYB_L3B_EN/PYB_AU_EN 控制 3V3_L3B/AU_L3B。

- 参数与网络：`always_on=3V3_L0`；`standby=3V3_L1`；`core=3V3_L2`；`display=3V3_L3B`；`audio=AU_L3B`
- 证据：图 d351267c117d / 第 1 页 / 页 3 L0_SW/L1_SW/L2_SW/L3_SW 区 B1-D2

### Grove 5V 双向供电

输出方向由 U7 SY7088 把 VBUS_L0 升压为 BOOST_OUT，再经 U11 AW35112FDR 送到 GROVE_5V；输入方向由 U14 AW35122FDR 把 GROVE_5V 送到 GRV_5VIN，再经 U15 CH213K 接 Internal_5V。PM_EXT_5V_EN 同时控制输出路径并经 Q3 反相控制输入路径。

- 参数与网络：`control=PM_EXT_5V_EN`；`port_power=GROVE_5V`；`system_input=Internal_5V`
- 证据：图 d351267c117d / 第 1 页 / 页 3 GROVE_OUTPUT/GROVE_INPUT 区 B2-D3，U7/U11/U14/U15/Q3/J3

## 接口

### ESP32-S3R8 原生 USB

U16 GPIO19/GPIO20 分别连接 G19_USB_N/G20_USB_P，经 R37/R38 22Ω 与 ICMF062P900MFR 共模滤波器形成 USB_N/USB_P，再连接 USB-C 接口与扩展复用器。

- 参数与网络：`dm_gpio=19`；`dp_gpio=20`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 D1-D3，U16 GPIO19/20、R37/R38、F1; 图 d351267c117d / 第 1 页 / 页 3 TYPEC 区 J1 USB_P/USB_N

### AMOLED 与 CST820 触摸接口

J4 31-pin FPC 引出 OLED_CS、OLED_SCK、OLED_D0-D3、OLED_TE、OLED_VBAT、3V3_L3B、PYB_OLED_RST，以及 G47_SYS_SDA、G48_SYS_SCL、G13_TP_INT、PYB_TP_RST 和 3V3_L2。页 2 Functions 明确标注 AMOLED 1.75英寸 466×466 与 TP=CST820。

- 参数与网络：`display_size_inch=1.75`；`resolution=466x466`；`touch_controller=CST820`；`display_connector_pins=31`
- 证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions/I/O Map，AMOLED 1.75 466x466、CST820 与 OLED/TP 信号; 图 635ac5af0356 / 第 1 页 / 页 5 TP&OLED 区 B3-C4，J4 31-pin FPC

### PWM 震动电机

M1 MOTOR_0610 由 VBUS_L0 供电，Q4 2N7002KT 作为低侧开关，PYB_MT_PWM 经 R42 0Ω 驱动栅极，D5 1N4148WT 提供续流保护。

- 参数与网络：`control=PYB_MT_PWM`；`supply=VBUS_L0`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 MOTOR 区 A4，M1/Q4/D5/R42

### USB/UART 扩展口复用

U26 CH442E 以 G43_U0TXD/G44_U0RXD 和 USB_P/USB_N 为两组输入，由 PYB_MUX_CTR 选择输出 MUX_IO_1/MUX_IO_2；图注明确低电平选择 UART0，高电平选择 USB。J5/J6 还引出 EXT_GPIO3-10、G0_BOOT、Int_5V、3V3_L2 与 GND，并注明 3V3_L2 外供尽量不超过 200mA。

- 参数与网络：`control=PYB_MUX_CTR`；`low_function=UART0`；`high_function=USB`；`suggested_3v3_max_ma=200`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 Ext.Port&CH442E 区 D2-D3，U26/J5/J6 与选择注记

### HY2.0-4P Grove 端口

J3 pins1-4 分别连接 GND、GROVE_5V、EXT_GPIO10、EXT_GPIO11，两路信号有 TVS1/TVS2 保护，GROVE_5V 支持前述双向电源路径。

- 参数与网络：`pin_count=4`；`power=GROVE_5V`；`signal_a=EXT_GPIO10`；`signal_b=EXT_GPIO11`
- 证据：图 d351267c117d / 第 1 页 / 页 3 GROVE 区 C2-C3，J3/TVS1/TVS2

## 总线

### G47_SYS_SDA/G48_SYS_SCL 系统 I2C

ESP32-S3R8 GPIO47/GPIO48 分别连接 G47_SYS_SDA/G48_SYS_SCL，R30/R31 各 2.2K 上拉到 3V3_L2；M5PM1、M5IOE1、BMI270、RX8130CE 与触摸接口共享该总线，音频侧经 2N7002DW 热插拔隔离电路连接 AUDIO_I2C_SDA/SCL。

- 参数与网络：`sda_gpio=47`；`scl_gpio=48`；`pullup_ohm=2200`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 B1-B2/C4，R30/R31 与 U16 GPIO47/48; 图 635ac5af0356 / 第 1 页 / 页 5 IMU/RTC/I2C HOT PLUG IN/PYB_IIC/TP&OLED

## GPIO 与控制信号

### M5PM1 电源与唤醒映射

M5PM1 DCDC3V3_EN_PP/LDO3V3_EN_PP/BOOST5V_EN_PP 分别连接 PM_3V3_L2_EN、PM_3V3_L1_EN、PM_EXT_5V_EN；G0/G2/G4/G3/G1 分别连接 PMG0_RTC&IMU_INT、PMG2_CHG_STAT、PMG4_PORT_INT、PMG3_CHG_PROG、G12_PY_IRQ；I2C_SCL/SDA 连接 G48_SYS_SCL/G47_SYS_SDA。

- 参数与网络：`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`esp_irq=G12_PY_IRQ`
- 证据：图 d351267c117d / 第 1 页 / 页 3 PMIC 区 C3-D4，U9 M5PM1 引脚网络

### M5IOE1 外设控制映射

U23 M5IOE1 的 PYG9/PYG8/PYG10/PYG4/PYG5/PYG1/PYG3 分别连接 PYB_MT_PWM、PYB_L3B_EN、PYB_SPK_EN、PYB_TP_RST、PYB_OLED_RST、PYB_MUX_CTR、PYB_AU_EN；PYG12/PYG13 引出 PYB_SWD/PYB_SWC，NRST 接 SOC_RESET。

- 参数与网络：`address_7bit=0x4F`；`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 PYB_IIC 区 B2-C3，U23 M5IOE1，IIC Address 0x4F

### KEY1 与 KEY2

S2/S3 分别把 G2_KEY1/G1_KEY2 按下接地，R61/R62 各 10K 上拉到 3V3_L2，C86/C92 各 100nF 对地并配 ESD5311；对应 ESP32-S3R8 GPIO2/GPIO1。

- 参数与网络：`key1_gpio=2`；`key2_gpio=1`；`active_low=true`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 Button 区 D4，S2/S3/R61/R62/C86/C92; 图 32ad59d9046e / 第 1 页 / 页 4 U16 GPIO1/GPIO2=G1_KEY2/G2_KEY1

### PWR_BTN 电源按键

S1 按下把 PWR_BTN 接地，R20 10K 将其上拉到 3V3_L0，C12 1uF 对地并配 D3；PWR_BTN 连接 M5PM1 BTN_PU，用于电源模式与唤醒控制。

- 参数与网络：`signal=PWR_BTN`；`controller_pin=M5PM1 BTN_PU`；`active_low=true`
- 证据：图 d351267c117d / 第 1 页 / 页 3 PMIC 区 B3-D4，S1/R20/C12/D3 与 U9 BTN_PU; 图 f2c2e1ff5c08 / 第 1 页 / 页 2 Power Mode，PwrBTN 状态转换

## 时钟

### ESP32-S3R8 40MHz 晶振

X1 标注 40MHz/15pF/10ppm，XTAL_P 侧串联 L7 10nH，C49/C54 各 24pF 对地并连接 XTAL_P/XTAL_N。

- 参数与网络：`frequency_mhz=40`；`load_pf=15`；`tolerance_ppm=10`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 C5-C6，X1/L7/C49/C54

### RX8130CE RTC 与联合唤醒

U20 RX8130CE 由 3V3_L1 供电并接系统 I2C，nIRQ 输出 PMG0_RTC&IMU_INT；IMU_INT 经 Q7 2N7002KT 也汇入同一网络，形成 RTC/IMU 联合唤醒请求。图区标注 IIC Address 0x32。

- 参数与网络：`address_7bit=0x32`；`supply=3V3_L1`；`wake_net=PMG0_RTC&IMU_INT`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 RTC 区 A3，U20/Q7/IMU_INT/PMG0_RTC&IMU_INT

## 复位

### SOC_RESET 与 G0_BOOT

SOC_RESET 由 R33 10K 上拉到 3V3_L2，C52 1uF 对地并经 L6 0R(TBD) 接 U16 CHIP_PU；G0_BOOT 由 R28 10K 上拉到 3V3_L2并连接 U16 GPIO0 strap 与扩展口。

- 参数与网络：`reset=SOC_RESET`；`boot=G0_BOOT`；`boot_gpio=0`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 B1-C2，R28/R33/C52/L6 与 U16 CHIP_PU/GPIO0; 图 635ac5af0356 / 第 1 页 / 页 5 Ext.Port 区 J6 G0_BOOT

## 存储

### W25Q128JVPIQ 外部 NOR Flash

U17 W25Q128JVPIQ 的 nCS/SO/SCLK/SI/nWP/HOLD 分别连接 NOR_CS、NOR_DO、NOR_SCK、NOR_DI、NOR_WP、NOR_HOLD，VCC 接 VDD_NOR；U16 对应 SPI Flash 引脚连接相同网络，NOR_SCK 串联 R36 22Ω。

- 参数与网络：`part_number=W25Q128JVPIQ`；`supply=VDD_NOR`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 C4-D6，U16 Flash 引脚与 U17 W25Q128JVPIQ

## 音频

### ES8311 音频编解码器

U22 ES8311 由 AU_L3B 供电，AUDIO_I2C_SCL/SDA 经热插拔隔离级连接系统 I2C；I2S 使用 G18_I2S_MCLK、G17_I2S_BCLK、G15_I2S_LRCK、G21_I2S_DDAC，MIC1_P/N 输入麦克风，DAC_L_P/N 输出扬声器信号。图区标注 IIC Address 0x18。

- 参数与网络：`address_7bit=0x18`；`power=AU_L3B`；`mclk_gpio=18`；`bclk_gpio=17`；`lrck_gpio=15`；`data_gpio=21`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 AUDIO/I2C HOT PLUG IN 区 A2-C2，U22 与 Q5/Q6

### 模拟 MEMS 麦克风

U19 麦克风由 AU_L3B 经 R40 100Ω 供电，差分输出经 R41/R43 0Ω 形成 MIC1_P/MIC1_N 并连接 ES8311 MIC1 输入。

- 参数与网络：`supply=AU_L3B`；`positive=MIC1_P`；`negative=MIC1_N`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 MIC 区 A4 与 AUDIO 区 U22 MIC1P/MIC1N

### AW8737A 与 8Ω 1W 扬声器

U25 AW8737A 从 VBUS_L0 供电，DAC_L_P/N 经 R57/R58 200K 输入，SHDN 由 PYB_SPK_EN 控制，VOP/VON 经 FB1/FB2 输出 SPK_P/N 到 J7；页 2 Functions 明确标注 Speaker 8Ω @ 1W。

- 参数与网络：`amplifier=AW8737A`；`impedance_ohm=8`；`rated_power_w=1`；`enable=PYB_SPK_EN`
- 证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions 区 Speaker 8Ω @ 1W; 图 635ac5af0356 / 第 1 页 / 页 5 SPEAKER 区 D1-D2，U25/J7

## 传感器

### BMI270 六轴 IMU

U18 BMI270 由 3V3_L1 供电，SCL/SDA 接 G48_SYS_SCL/G47_SYS_SDA，INT1 输出 IMU_INT，SDO 通过 R47 10K 下拉；图区明确标注 IIC Address 0x68。

- 参数与网络：`address_7bit=0x68`；`supply=3V3_L1`；`interrupt=IMU_INT`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 IMU&MAG 区 A1-A2，U18 BMI270

### BMM150 预留未实装

U21 连接 BMI270 辅助 A_SCL/A_SDA，但器件标注 NC(BMM150)，因此该磁力计位置为预留而非当前实装器件。

- 参数与网络：`part_number=BMM150`；`fitted=false`
- 证据：图 635ac5af0356 / 第 1 页 / 页 5 IMU&MAG 区 A1-A2，U21 标注 NC(BMM150)

## 射频

### ESP32-S3R8 板载 PIFA 天线

U16 LNA_IN 经 L3/L4 与 C39-C42 匹配网络连接 ANT1 ANT_PIFA，D4 对地提供射频端保护。

- 参数与网络：`antenna=ANT_PIFA`
- 证据：图 32ad59d9046e / 第 1 页 / 页 4 A1-A3，ANT1/D4/L3/L4/C39-C42/U16 LNA_IN

## 模拟电路

### 电池、USB 与 Grove 电压检测

Q1A/Q1B CJ3439KDW 在 PM_ADC_EN 控制下把 VBAT_L0 分压送到 PM_ADC；5V_IN 经 R14/R16 分压形成 PM_5VIN_ADC，GROVE_5V 经 R15/R17 分压形成 PM_EXT5V_ADC，三路均进入 M5PM1。

- 参数与网络：`battery_adc=PM_ADC`；`usb_adc=PM_5VIN_ADC`；`grove_adc=PM_EXT5V_ADC`
- 证据：图 d351267c117d / 第 1 页 / 页 3 ADC DET 区 A4，Q1A/Q1B 与三路 ADC 分压

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StopWatch 四页硬件架构 | `schematic_page_count=4`；`sku=C152` |
| 系统结构 | L0/L1/L2/L3A/L3B 电源模式 | `shipping=L0`；`standby=L1`；`deep_sleep=L2`；`core_active=L3A`；`all_active=L3B` |
| 核心器件 | ESP32-S3 exact variant | `overview_label=ESP32-S3-R8N8`；`detail_label=ESP32-S3R8`；`documented_label=ESP32-S3R8` |
| 电源 | USB 输入、充电与 450mAh 电池 | `battery_capacity_mah=450`；`charger=LGS4056HDA`；`protected_input=5V_IN` |
| 电源 | 185mA/425mA 充电电流选择 | `default_current_ma=185`；`low_level_current_ma=425`；`program_net=PMG3_CHG_PROG`；`status_net=PMG2_CHG_STAT` |
| 电源 | Internal_5V 与 VBAT_L0 汇入 VBUS_L0 | `input_a=Internal_5V`；`input_b=VBAT_L0`；`output=VBUS_L0` |
| 模拟电路 | 电池、USB 与 Grove 电压检测 | `battery_adc=PM_ADC`；`usb_adc=PM_5VIN_ADC`；`grove_adc=PM_EXT5V_ADC` |
| 电源 | 3V3_L0/L1/L2/L3B 与 AU_L3B | `always_on=3V3_L0`；`standby=3V3_L1`；`core=3V3_L2`；`display=3V3_L3B`；`audio=AU_L3B` |
| 电源 | Grove 5V 双向供电 | `control=PM_EXT_5V_EN`；`port_power=GROVE_5V`；`system_input=Internal_5V` |
| GPIO 与控制信号 | M5PM1 电源与唤醒映射 | `scl=G48_SYS_SCL`；`sda=G47_SYS_SDA`；`esp_irq=G12_PY_IRQ` |
| GPIO 与控制信号 | M5IOE1 外设控制映射 | `address_7bit=0x4F`；`scl=G48_SYS_SCL`；`sda=G47_SYS_SDA` |
| 总线 | G47_SYS_SDA/G48_SYS_SCL 系统 I2C | `sda_gpio=47`；`scl_gpio=48`；`pullup_ohm=2200` |
| 存储 | W25Q128JVPIQ 外部 NOR Flash | `part_number=W25Q128JVPIQ`；`supply=VDD_NOR` |
| 存储 | 16MB Flash 容量 | `documented_capacity_mb=16`；`schematic_part_number=W25Q128JVPIQ` |
| 内存与 Flash | 8MB PSRAM | `documented_capacity_mb=8`；`schematic_labels=ESP32-S3-R8N8 / ESP32-S3R8` |
| 时钟 | ESP32-S3R8 40MHz 晶振 | `frequency_mhz=40`；`load_pf=15`；`tolerance_ppm=10` |
| 射频 | ESP32-S3R8 板载 PIFA 天线 | `antenna=ANT_PIFA` |
| 复位 | SOC_RESET 与 G0_BOOT | `reset=SOC_RESET`；`boot=G0_BOOT`；`boot_gpio=0` |
| 接口 | ESP32-S3R8 原生 USB | `dm_gpio=19`；`dp_gpio=20` |
| 接口 | AMOLED 与 CST820 触摸接口 | `display_size_inch=1.75`；`resolution=466x466`；`touch_controller=CST820`；`display_connector_pins=31` |
| 核心器件 | AMOLED CO5300 控制器 | `documented_controller=CO5300`；`documented_interface=QSPI` |
| 传感器 | BMI270 六轴 IMU | `address_7bit=0x68`；`supply=3V3_L1`；`interrupt=IMU_INT` |
| 传感器 | BMM150 预留未实装 | `part_number=BMM150`；`fitted=false` |
| 时钟 | RX8130CE RTC 与联合唤醒 | `address_7bit=0x32`；`supply=3V3_L1`；`wake_net=PMG0_RTC&IMU_INT` |
| 音频 | ES8311 音频编解码器 | `address_7bit=0x18`；`power=AU_L3B`；`mclk_gpio=18`；`bclk_gpio=17`；`lrck_gpio=15`；`data_gpio=21` |
| 音频 | 模拟 MEMS 麦克风 | `supply=AU_L3B`；`positive=MIC1_P`；`negative=MIC1_N` |
| 音频 | AW8737A 与 8Ω 1W 扬声器 | `amplifier=AW8737A`；`impedance_ohm=8`；`rated_power_w=1`；`enable=PYB_SPK_EN` |
| 接口 | PWM 震动电机 | `control=PYB_MT_PWM`；`supply=VBUS_L0` |
| GPIO 与控制信号 | KEY1 与 KEY2 | `key1_gpio=2`；`key2_gpio=1`；`active_low=true` |
| GPIO 与控制信号 | PWR_BTN 电源按键 | `signal=PWR_BTN`；`controller_pin=M5PM1 BTN_PU`；`active_low=true` |
| 接口 | USB/UART 扩展口复用 | `control=PYB_MUX_CTR`；`low_function=UART0`；`high_function=USB`；`suggested_3v3_max_ma=200` |
| 接口 | HY2.0-4P Grove 端口 | `pin_count=4`；`power=GROVE_5V`；`signal_a=EXT_GPIO10`；`signal_b=EXT_GPIO11` |

## 待确认事项

- `component.soc-variant`：页 2 Functions 标注 ESP32-S3-R8N8，页 4 U16 标注 ESP32_S3R8，正文称 ESP32-S3R8；当前图面没有统一完整订购码，R8N8 与 R8 标注的量产对应关系需确认。（证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions 区 A1，ESP32-S3-R8N8; 图 32ad59d9046e / 第 1 页 / 页 4 U16 ESP32_S3R8）
- `storage.documented-flash-capacity`：正文称板载 Flash 为 16MB，原理图 U17 标注 W25Q128JVPIQ 并显示 NOR 连线，但图面没有单独写出 bit 或 byte 容量，需由器件 datasheet 或量产 BOM 确认。（证据：图 32ad59d9046e / 第 1 页 / 页 4 U17 W25Q128JVPIQ，未另标容量）
- `memory.documented-psram-capacity`：正文称主控配置 8MB PSRAM，页 2/页 4 分别标 ESP32-S3-R8N8 与 ESP32-S3R8；原理图没有独立 PSRAM 或容量字段，容量和集成方式需由 exact SoC datasheet 或 BOM 确认。（证据：图 f2c2e1ff5c08 / 第 1 页 / 页 2 Functions，ESP32-S3-R8N8; 图 32ad59d9046e / 第 1 页 / 页 4 U16 ESP32_S3R8，未画独立 PSRAM）
- `component.documented-co5300`：正文称 AMOLED 使用 CO5300 QSPI 控制器；原理图只画 ESP32-S3R8 QSPI 网络和 J4 FPC，没有 CO5300 器件、地址、供电或面板子板电路，控制器型号需由屏幕模组 BOM 确认。（证据：图 635ac5af0356 / 第 1 页 / 页 5 J4 仅给 OLED QSPI/FPC 网络，无 CO5300 器件）
- `review.soc-variant`：StopWatch C152 量产 SoC 的完整订购码是 ESP32-S3-R8N8 还是 ESP32-S3R8 对应的其他变体；原因：页 2 总览、页 4 详图与正文的型号标注不完全一致。
- `review.flash-capacity`：U17 W25Q128JVPIQ 对应的量产 Flash 容量是否为正文所述 16MB；原因：原理图给出完整器件型号和 NOR 连线，但未单独标注容量。
- `review.psram-capacity`：StopWatch 的 PSRAM 是否集成于量产 ESP32-S3 变体且容量为 8MB；原因：原理图没有独立 PSRAM、容量字段或统一完整 SoC 订购码。
- `review.co5300-controller`：J4 所接 AMOLED 模组的量产显示控制器是否为 CO5300；原因：主板原理图只有 QSPI/FPC 网络，没有 CO5300 器件或屏幕子板电路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f2c2e1ff5c08ee2b79e881560ebfa5a1b56f5cc8cf4e4ce37fb151181b34a9ae` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-SCH_Stopwatch_PRJ_Main_VA_20251201_2026_04_24_17_46_22_page_02.png` |
| 2 | 1 | `d351267c117dfad805270743bb8187ef50afbdbd218a1e34812c4115e2567e91` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-SCH_Stopwatch_PRJ_Main_VA_20251201_2026_04_24_17_46_22_page_03.png` |
| 3 | 1 | `32ad59d9046e84b8acf94e3d94246aea2f784b830b735af4c5033b22b943d141` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-SCH_Stopwatch_PRJ_Main_VA_20251201_2026_04_24_17_46_22_page_04.png` |
| 4 | 1 | `635ac5af035678155fbe2de68b9b3a570d19514dfd20f5220409275d66482852` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-SCH_Stopwatch_PRJ_Main_VA_20251201_2026_04_24_17_46_22_page_05.png` |

---

源文档：`zh_CN/core/StopWatch.md`

源文档 SHA-256：`421f393254ec795a262b408203b7e98fc11e0973ebb747efb0ef66f5d4962c31`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
