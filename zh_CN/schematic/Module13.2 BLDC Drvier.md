# Module13.2 BLDC Drvier 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 BLDC Drvier |
| SKU | M036 |
| 产品 ID | `module13-2-bldc-drvier-6121c64a1745` |
| 源文档 | `zh_CN/module/odrive.md` |

## 概述

两张原理图页面展示基于 STM32F405RGT6 与 DRV8301 的单路三相电机驱动：24V INPUT 经大容量去耦送入六颗 NTMFS5C430NLT1G 组成的三相桥，U2 SY8303A 生成 5V，U3 SPX3819 生成 3.3V。MCU 通过六路栅极控制、SPI、FAULT 和两路电流采样连接 DRV8301，并连接增量编码器、NTC 温度、母线电压、USB Type-C、SWD、M5-Bus UART/STEP-DIR 跳线和电机/电源端子。图面未直接给出 12-24V 完整范围、5A 峰值能力、ODrive 版本或控制性能。

## 检索关键词

`Module13.2 BLDC Drvier`、`M036`、`ODrive`、`ODrive v3.5-24V`、`STM32F405RGT6`、`DRV8301`、`NTMFS5C430NLT1G`、`SY8303A`、`SPX3819M5-L-3-3/TR`、`SDNT1608X103F3450FTF`、`PBUS_P240`、`24V INPUT`、`CORE_P050`、`MCU_P033`、`OUT_A`、`OUT_B`、`OUT_C`、`CS_BH`、`CS_BL`、`CS_CH`、`CS_CL`、`M0_SO1`、`M0_SO2`、`M0_FAULT`、`M0_EN_GATE`、`M0_ENC_A`、`M0_ENC_B`、`M0_ENC_Z`、`M0_TEMP`、`VBUS_SEN`、`TXD/STEP`、`RXD/DIR`、`M5 BUS`、`USB Type-C`、`SWD`、`5A`、`12-24V`、`UART`、`ODriveTool`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F405RGT6 | 运动控制 MCU，连接栅极驱动、编码器、温度、母线采样、UART、USB 与调试接口 | 图 c91ea6c0be88 / 第 1 页 / 上中 U1 STM32F405RGT6 pins1-64 |
| U4 | DRV8301 | 三相 MOSFET 栅极驱动、SPI 配置、故障与电流采样前端 | 图 233966d06f16 / 第 1 页 / 右下 U4 DRV8301 |
| Q1-Q6 | NTMFS5C430NLT1G | OUT_A/OUT_B/OUT_C 三相功率桥的六颗 N 沟道 MOSFET | 图 233966d06f16 / 第 1 页 / 右上 Q1-Q6 NTMFS5C430NLT1G 三组半桥 |
| U2 | SY8303A | PBUS_P240 到 CORE_P050 的 5V 降压转换器 | 图 233966d06f16 / 第 1 页 / 左中 U2 SY8303A、L1 10uH 与 FU1 0.5A |
| U3 | SPX3819M5-L-3-3/TR | CORE_P050 到 MCU_P033 的 3.3V LDO | 图 233966d06f16 / 第 1 页 / 左下 U3 SPX3819M5-L-3-3/TR |
| R12 | SDNT1608X103F3450FTF | M0_TEMP 温度检测 NTC | 图 c91ea6c0be88 / 第 1 页 / 下中 R12 SDNT1608X103F3450FTF、R14/C3 与 M0_TEMP |
| J1 | KF128-2.54-5P | 增量编码器 A/B/I、GND 与 5V 接口 | 图 c91ea6c0be88 / 第 1 页 / 中左 J1 KF128-2.54-5P 与 EXT_ENC_A/B/I |
| J3,J4,J5 | TYPEC / HT3.96-2P / CON3 | USB、24V 电源输入和三相电机输出连接器 | 图 c91ea6c0be88 / 第 1 页 / 中左 J3 TYPEC; 图 233966d06f16 / 第 1 页 / 左上 J4 HT3.96-2P 与 J5 CON3 |
| BUS1,J2,CON6 | M5 BUS / SWD / 1x6 debug header | M5-Bus 主机接口、SWD 和 SPI/GPIO 调试连接 | 图 c91ea6c0be88 / 第 1 页 / 左上 BUS1、左下 J2 SWD、右上 CON6 |

## 系统结构

### STM32F405RGT6 与 DRV8301 控制架构

U1 STM32F405RGT6 通过 M0_AH/AL、M0_BH/BL、M0_CH/CL、M0_EN_GATE、M0_FAULT、M0_SCS/SCK/MOSI/MISO 和 M0_SO1/SO2 连接 U4 DRV8301，构成单轴三相电机控制核心。

- 参数与网络：`mcu=STM32F405RGT6`；`gate_driver=DRV8301`；`axes=1`
- 证据：图 233966d06f16 / 第 1 页 / 右下 U4 DRV8301 控制与采样网络; 图 c91ea6c0be88 / 第 1 页 / 右侧 U1 对应 M0_* 信号

## 电源

### 名义 24V 电机母线输入

J4 HT3.96-2P 的 pin2 连接 PBUS_P240、pin1 接 GND，页面将该接口标为 24V INPUT；C20 220uF/35V 与 C21-C24 22uF/35V 对母线进行去耦。

- 参数与网络：`connector=HT3.96-2P`；`schematic_label=24V INPUT`；`bus_net=PBUS_P240`
- 证据：图 233966d06f16 / 第 1 页 / 左上 J4 与右上 PBUS_P240/C20-C24

### 5V 与 3.3V 辅助电源

U2 SY8303A 以 PBUS_P240 为输入，经 L1 10uH 生成 CORE_P050，并通过 FU1 0.5A；U3 SPX3819M5-L-3-3/TR 再生成 MCU_P033，R19 120ohm 与 C18 22uF 形成 AVCC 滤波。

- 参数与网络：`five_v_net=CORE_P050`；`three_v3_net=MCU_P033`；`analog_net=AVCC`；`fuse_a=0.5`
- 证据：图 233966d06f16 / 第 1 页 / 左中/左下 U2/L1/FU1/U3/R19

### 六 MOSFET 三相功率桥

Q1-Q6 六颗 NTMFS5C430NLT1G 组成 A/B/C 三组上下桥臂，桥臂中点分别为 OUT_A、OUT_B、OUT_C，并连接 J5 三针电机端子。

- 参数与网络：`mosfets=6`；`phases=3`；`outputs=OUT_A,OUT_B,OUT_C`
- 证据：图 233966d06f16 / 第 1 页 / 右上 Q1-Q6 与左中 J5 OUT_A/B/C

## 接口

### 增量编码器 A/B/I 输入

J1 五针接口引出 CORE_P050、GND、EXT_ENC_A、EXT_ENC_B、EXT_ENC_I；三路信号经上拉和 R7/R8/R9 1K 串联电阻连接 MCU 的 M0_ENC_A/B/Z。

- 参数与网络：`connector=KF128-2.54-5P`；`channels=A,B,index`；`mcu_nets=M0_ENC_A,M0_ENC_B,M0_ENC_Z`
- 证据：图 c91ea6c0be88 / 第 1 页 / 中左 J1、R4-R9 与 U1 PB4/PB5/PC6

### UART 与 STEP/DIR 复用跳线

U1 PA0 连接 TXD/STEP，PA1 连接 RXD/DIR；JP1 0R 将 G13 接 TXD/STEP，JP2 0R 将 G5 接 RXD/DIR，JP3-JP6 对 G26/G0/G12/G15 标为 DNP 备用选择。

- 参数与网络：`default_tx_step=G13`；`default_rx_dir=G5`；`alternate_labels=G26,G0,G12,G15`
- 证据：图 c91ea6c0be88 / 第 1 页 / U1 PA0/PA1 与左下 JP1-JP6

### M5-Bus 控制与电源接口

BUS1 30-pin M5 BUS 提供 CORE_P050 5V、MCU_P033 3.3V、EN/RST、UART/I2C/SPI GPIO；产品管脚表将多个 M5-Bus 位置标为 TXD/STEP 与 RXD/DIR，以配合 JP1-JP6 跳线选择。

- 参数与网络：`connector_pins=30`；`connector=M5 BUS`；`shared_functions=TXD/STEP,RXD/DIR`
- 证据：图 c91ea6c0be88 / 第 1 页 / 左上 BUS1 M5 BUS 与左下 JP1-JP6

### USB Type-C 配置与数据

J3 TYPEC 的 USB_DP/USB_DM 经 R10/R11 22ohm 连接 U1 PA12/PA11，CC1/CC2 各通过 5.1K 电阻接地，形成 USB 设备侧连接。

- 参数与网络：`connector=USB Type-C`；`data_nets=USB_DP,USB_DM`；`cc_resistors_kohm=5.1`
- 证据：图 c91ea6c0be88 / 第 1 页 / 中左 J3/R1/R2/R10/R11 与 U1 PA11/PA12

## 时钟

### STM32 外部 8MHz 时钟

U1 PH0-OSC_IN/PH1-OSC_OUT 连接 X1 8MHz 晶体，并配置 C5/C6 各 20pF 负载电容。

- 参数与网络：`frequency_mhz=8`；`load_cap_pf=20`
- 证据：图 c91ea6c0be88 / 第 1 页 / U1 pins5/6、X1 与 C5/C6

## 传感器

### 板载 NTC 温度检测

R12 SDNT1608X103F3450FTF 与 R14 3.3K 构成从 MCU_P033 到 GND 的分压，节点 M0_TEMP 接 U1 PC4，C3 1uF 对该节点滤波。

- 参数与网络：`thermistor=SDNT1608X103F3450FTF`；`adc_net=M0_TEMP`；`mcu_pin=PC4`
- 证据：图 c91ea6c0be88 / 第 1 页 / 下中 R12/R14/C3/M0_TEMP 与 U1 pin24 PC4

## 调试与烧录

### SWD 与 SPI/GPIO 调试接口

J2 五针 SWD 接口引出 SYS_RST、SWCLK、SWDIO、MCU_P033 和 GND；CON6 引出 GND、GPIO4、M0_SCK、M0_MISO、M0_MOSI 及第六脚。

- 参数与网络：`swd=RST,CLK,DIO,VCC,GND`；`debug_spi=M0_SCK,M0_MISO,M0_MOSI`
- 证据：图 c91ea6c0be88 / 第 1 页 / 左下 J2 SWD 与右上 CON6

## 模拟电路

### B/C 两相低侧电流采样

B 相与 C 相低侧分别使用 R31/R36 0.5mohm 分流电阻，Kelvin 网络 CS_BH/CS_BL 与 CS_CH/CS_CL 接入 DRV8301 SN1/SP1 和 SN2/SP2，放大输出为 M0_SO1/M0_SO2。

- 参数与网络：`sense_phases=B,C`；`shunt_resistance_mohm=0.5`；`outputs=M0_SO1,M0_SO2`
- 证据：图 233966d06f16 / 第 1 页 / 右上 R31/R36 与右下 U4 SN1/SP1/SN2/SP2/SO1/SO2

### 电机母线电压采样

PBUS_P240 经 R13 10K 与 R15 1K 分压形成 VBUS_SEN，并由 C4 270pF 滤波后接 U1 PA5 ADC 输入。

- 参数与网络：`source=PBUS_P240`；`sense_net=VBUS_SEN`；`mcu_pin=PA5`
- 证据：图 c91ea6c0be88 / 第 1 页 / 下中 R13/R15/C4 与 U1 PA5 VBUS_SEN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | STM32F405RGT6 与 DRV8301 控制架构 | `mcu=STM32F405RGT6`；`gate_driver=DRV8301`；`axes=1` |
| 电源 | 名义 24V 电机母线输入 | `connector=HT3.96-2P`；`schematic_label=24V INPUT`；`bus_net=PBUS_P240` |
| 电源 | 5V 与 3.3V 辅助电源 | `five_v_net=CORE_P050`；`three_v3_net=MCU_P033`；`analog_net=AVCC`；`fuse_a=0.5` |
| 电源 | 六 MOSFET 三相功率桥 | `mosfets=6`；`phases=3`；`outputs=OUT_A,OUT_B,OUT_C` |
| 模拟电路 | B/C 两相低侧电流采样 | `sense_phases=B,C`；`shunt_resistance_mohm=0.5`；`outputs=M0_SO1,M0_SO2` |
| 接口 | 增量编码器 A/B/I 输入 | `connector=KF128-2.54-5P`；`channels=A,B,index`；`mcu_nets=M0_ENC_A,M0_ENC_B,M0_ENC_Z` |
| 传感器 | 板载 NTC 温度检测 | `thermistor=SDNT1608X103F3450FTF`；`adc_net=M0_TEMP`；`mcu_pin=PC4` |
| 模拟电路 | 电机母线电压采样 | `source=PBUS_P240`；`sense_net=VBUS_SEN`；`mcu_pin=PA5` |
| 接口 | UART 与 STEP/DIR 复用跳线 | `default_tx_step=G13`；`default_rx_dir=G5`；`alternate_labels=G26,G0,G12,G15` |
| 接口 | M5-Bus 控制与电源接口 | `connector_pins=30`；`connector=M5 BUS`；`shared_functions=TXD/STEP,RXD/DIR` |
| 接口 | USB Type-C 配置与数据 | `connector=USB Type-C`；`data_nets=USB_DP,USB_DM`；`cc_resistors_kohm=5.1` |
| 调试与烧录 | SWD 与 SPI/GPIO 调试接口 | `swd=RST,CLK,DIO,VCC,GND`；`debug_spi=M0_SCK,M0_MISO,M0_MOSI` |
| 时钟 | STM32 外部 8MHz 时钟 | `frequency_mhz=8`；`load_cap_pf=20` |
| 电源 | DC 12-24V 输入范围与适配器要求 | `documented_input_v=12-24`；`documented_adapter_a=5`；`schematic_label=24V INPUT` |
| 电源 | 5A 峰值电机驱动电流 | `documented_peak_a=5` |
| 系统结构 | ODrive v3.5-24V 与固件 0.5.1 | `documented_hardware=ODrive v3.5-24V`；`documented_firmware=0.5.1` |
| 接口 | ODrive UART 协议与 ODriveTool 兼容 | `documented_interface=UART`；`documented_tool=ODriveTool 0.5.1` |
| 系统结构 | 单电机伺服与高精度定位能力 | `documented_motors=1`；`documented_control=servo,high speed,high precision positioning` |

## 待确认事项

- `power.documented-input-range`：正文称输入允许 DC 12-24V，且适配器输出电流需达到 5A；原理图仅将 J4 标为 24V INPUT 并使用 35V 母线电容，没有标最小输入、欠压门限、线缆压降或适配器额定条件。（证据：图 233966d06f16 / 第 1 页 / J4/PBUS_P240 仅标 24V INPUT）
- `power.documented-peak-current`：正文称峰值驱动电流为 5A；原理图确认 MOSFET、DRV8301 和 0.5mohm 分流器件，但没有铜厚、散热、保护阈值、持续时间或温升条件，无法验证整机 5A 峰值能力。（证据：图 233966d06f16 / 第 1 页 / Q1-Q6、U4、R31/R36，无整机电流测试条件）
- `system.documented-odrive-versions`：正文称硬件基于 ODrive v3.5-24V、固件版本为 0.5.1；原理图没有版本栏、板号、固件标识或构建哈希，实际硬件派生关系和出厂固件需由 BOM、PCB 标识与镜像确认。（证据：图 c91ea6c0be88 / 第 1 页 / 图面无 ODrive 硬件或固件版本栏）
- `interface.documented-odrive-uart`：正文称 UART 兼容 ODrive 官方协议与配置工具；原理图只确认 TXD/STEP、RXD/DIR 和 USB/SWD 物理连接，不包含 UART 波特率、协议版本、命令集或 ODriveTool 识别机制。（证据：图 c91ea6c0be88 / 第 1 页 / TXD/STEP 与 RXD/DIR 仅为物理网络）
- `system.documented-servo-control`：正文称模块支持单个三相伺服电机、高转速控制和高精度定位；原理图确认一组三相桥和 A/B/I 编码器输入，但闭环算法、速度范围、定位精度和适配电机参数由固件与调试配置决定。（证据：图 233966d06f16 / 第 1 页 / 单组三相桥与 J5; 图 c91ea6c0be88 / 第 1 页 / J1 编码器接口，无控制性能参数）
- `review.input-range`：量产模块的 DC 12-24V 允许范围、欠压条件和 5A 适配器要求如何定义；原因：图面只标 24V INPUT，没有完整输入范围与适配器条件。
- `review.peak-current`：5A 峰值电流的持续时间、散热、铜厚、保护阈值和环境条件是什么；原因：原理图没有整机热设计与额定条件。
- `review.odrive-versions`：M036 的 ODrive 硬件派生版本与出厂固件构建版本是什么；原因：原理图没有版本栏或固件信息。
- `review.odrive-uart`：UART 波特率、协议版本、命令集与 ODriveTool 兼容矩阵是什么；原因：图面只确认串口物理网络。
- `review.servo-control`：支持的电机类型、速度范围、定位精度、编码器条件与控制模式是什么；原因：控制性能由固件、电机、编码器和调参共同决定。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `233966d06f16b9109f8c326e2a0ffb639131535f6aa8ed0faae9c075b145cac3` | `https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_sch_01.webp` |
| 2 | 1 | `c91ea6c0be8833a0aed5eb3fca0a555ca8e32280ec20a64fe776c52eddd893fe` | `https://static-cdn.m5stack.com/resource/docs/products/module/odrive/odrive_sch_02.webp` |

---

源文档：`zh_CN/module/odrive.md`

源文档 SHA-256：`c744e7e517157356437ab6682ce3488aad74d33e8d0d92245c05244306e8816f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
