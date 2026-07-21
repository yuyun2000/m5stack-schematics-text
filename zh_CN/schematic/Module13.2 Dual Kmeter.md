# Module13.2 Dual Kmeter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 Dual Kmeter |
| SKU | M127 |
| 产品 ID | `module13-2-dual-kmeter-6688bfd97eaf` |
| 源文档 | `zh_CN/module/DualKmeter Module13.2.md` |

## 概述

Module13.2 Dual Kmeter 以 U5 STM32F030F4P6 为控制器，通过 U7 CA-IS3020S 隔离 I2C 与 M5-Bus 通信，并通过 TC_CS/TC_SCK/TC_MISO SPI 连接 U4 MAX6675/31855 热电偶转换器。继电器在 TC1、TC2 两组 K 型热电偶差分信号之间切换，Q1 SS8050 由 U5 RELAY 网络控制，D3 提供线圈钳位。电源从 12V 经 U1 ME3116AM6G 生成 5V_VCC，再由 U6 B0505LS-1WR2 建立隔离 5VISO，并通过 U2 MD5333、U3 HX6306P332 生成隔离侧 3.3V 电源。

## 检索关键词

`Module13.2 Dual Kmeter`、`M127`、`STM32F030F4P6`、`MAX6675/31855`、`MAX31855KASA`、`ME3116AM6G`、`B0505LS-1WR2`、`CA-IS3020S`、`HX6306P332`、`MD5333`、`AGQ200A4H`、`I2C`、`SPI`、`0x11`、`TC_CS`、`TC_SCK`、`TC_MISO`、`TC1_P`、`TC1_N`、`TC2_P`、`TC2_N`、`TC_P`、`TC_N`、`5V_VCC`、`5VISO`、`VCC_3V3`、`VCC_A3V3`、`CORE_3V3`、`GNDISO`、`RELAY`、`SW1`、`M5_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | STM32F030F4P6 | 隔离侧主控制器，管理 I2C、SPI、地址拨码、继电器和通道 LED | 图 33547cd3d7c5 / 第 1 页 / 网格 B1-C2 的 U5 STM32F030F4P6，标注 MCU_SCL/SDA、TC_CS/SCK/MISO、RELAY、LED_CTR、SWD 与 PA0-PA3 |
| U4 | MAX6675/31855 | K 型热电偶数字转换器，SPI 接口连接 U5，差分输入连接 TC_P/TC_N | 图 33547cd3d7c5 / 第 1 页 / 网格 C3 Thermocouple Converter 区的 U4，器件值 MAX6675/31855，标注 CS、SCK、MISO、T-、T+、VCC、GND |
| U7 | CA-IS3020S | M5-Bus SDA/SCL 与 MCU_SDA/MCU_SCL 之间的双通道 I2C 数字隔离器 | 图 33547cd3d7c5 / 第 1 页 / 网格 D1-D2 Isolated I2C 区的 U7 CA-IS3020S，A 侧接 CORE_3V3/GND/SDA/SCL，B 侧接 VCC_3V3/GNDISO/MCU_SDA/MCU_SCL |
| U1 | ME3116AM6G | 12V 至 5V_VCC 的非隔离降压转换器 | 图 33547cd3d7c5 / 第 1 页 / 网格 A1-A2 DCDC 区的 U1 ME3116AM6G，连接 12V、L1 6.8uH、D1 SS34、反馈网络和 5V_VCC |
| U6 | B0505LS-1WR2 | 5V_VCC 至隔离 5VISO 的隔离 DC-DC 模块 | 图 33547cd3d7c5 / 第 1 页 / 网格 A3 的 U6 B0505LS-1WR2，输入 +VIN/-VIN 接 5V_VCC/GND，输出 +VO/-VO 经 L2 接 5VISO/GNDISO |
| U2 | MD5333 | 5VISO 至 VCC_3V3 的隔离侧 MCU LDO | 图 33547cd3d7c5 / 第 1 页 / 网格 A4 MCU LDO 区的 U2 MD5333，VIN 接 5VISO，VOUT 接 VCC_3V3，GND 接 GNDISO |
| U3 | HX6306P332 | 5VISO 至热电偶转换器 VCC_A3V3 的隔离侧 LDO | 图 33547cd3d7c5 / 第 1 页 / 网格 B3 的 U3 HX6306P332，VIN 接 5VISO，VOUT 经 FB1 330R 磁珠接 VCC_A3V3，GND 接 GNDISO |
| P1 | DC-044 | 12V 外部电源输入连接器 | 图 33547cd3d7c5 / 第 1 页 / 网格 A1 左上 P1 DC-044，pin 1 接 12V，返回端接 GND，旁有 C1 100uF/35V |
| SW1,RP1 | 4 位拨码开关; 4.7KΩ(472)±5% | U5 PA0-PA3 的四位对地配置输入和上拉阵列 | 图 33547cd3d7c5 / 第 1 页 / 网格 B1 的 SW1 四位开关、RP1 四联 4.7KΩ 上拉至 VCC_3V3，以及 U5 PA0-PA3 |
| TC1,TC2 | 未标注 | 两路 K 型热电偶三端连接器，分别引出 T+、T- 和屏蔽地 | 图 33547cd3d7c5 / 第 1 页 / 网格 B4 的 TC1、TC2，pin 1 T+ 分别接 TC1_P/TC2_P，pin 2 T- 接 TC1_N/TC2_N，pin 0 SH 接 GNDISO |
| 未标注继电器位号 | 未标注 | 在 TC1 与 TC2 差分热电偶信号之间切换 TC_P/TC_N | 图 33547cd3d7c5 / 第 1 页 / 网格 B4-C4 Thermocouple Connector 区的四触点继电器符号，线圈接 5VISO/Q1，触点标注 TC1_P/N、TC2_P/N、TC_P/N |
| Q1,D3,R11,R12 | SS8050; 1N4148WS T4; 1KΩ; 10KΩ | 继电器线圈低侧驱动、钳位和基极偏置网络 | 图 33547cd3d7c5 / 第 1 页 / 网格 C4 的 RELAY-R11-Q1、R12 下拉、D3 1N4148WS T4 与 5VISO 线圈回路 |
| D4,D5,R13,R14 | Red 0603; Red 0603; 1.5KΩ; 1.5KΩ | TC1/TC2 通道状态指示电路 | 图 33547cd3d7c5 / 第 1 页 / 网格 D3 的 TC1 LED/TC2 LED 区，LED_CTR 接 D4/D5，R13 接 VCC_3V3，R14 接 GNDISO |
| J1 | SWD_5P | 隔离侧 MCU 的五针 SWD 调试与复位接口 | 图 33547cd3d7c5 / 第 1 页 / 网格 D2 的 J1 SWD_5P，连接 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GNDISO |
| J3 | M5_BUS | 30 针 M5-Bus 电源、I2C 和辅助信号接口 | 图 33547cd3d7c5 / 第 1 页 / 网格 D4 的 J3 M5_BUS，pin 1-30 标注 GND、GPIO、SDA、SCL、HPWR、5V、VBAT |

## 系统结构

### Module13.2 Dual Kmeter 系统架构

12V 经 U1 生成 5V_VCC，U6 建立隔离 5VISO，U2/U3 生成隔离侧 3.3V；U7 隔离 M5-Bus I2C，U5 通过 SPI 读取 U4，并驱动继电器在 TC1/TC2 差分输入间切换。

- 参数与网络：`controller=U5 STM32F030F4P6`；`thermocouple_converter=U4 MAX6675/31855`；`i2c_isolator=U7 CA-IS3020S`；`isolated_dc_dc=U6 B0505LS-1WR2`；`channel_selector=relay driven by Q1`；`inputs=TC1,TC2`；`host=J3 M5_BUS`
- 证据：图 33547cd3d7c5 / 第 1 页 / 完整单页各蓝框功能区：DCDC、MCU、Isolated I2C、Thermocouple Converter/Connector、M5_BUS

## 电源

### U1 12V 至 5V_VCC 降压

P1 pin 1 的 12V 连接 U1 VIN/pin 5，EN/pin 4 经 R1 100KΩ 上拉至 12V；LX/pin 6 经 L1 6.8uH 输出 5V_VCC，D1 SS34 连接 LX 节点与 GND。

- 参数与网络：`input_connector=P1 DC-044`；`input_rail=12V`；`converter=U1 ME3116AM6G`；`enable=R1 100KΩ to 12V`；`switch_pin=LX pin 6`；`inductor=L1 6.8uH`；`catch_diode=D1 SS34`；`output=5V_VCC`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 A1-A2 的 P1、U1、R1、D1、L1 与 12V/5V_VCC 路径

### 5V_VCC 反馈与滤波

R2 210KΩ 从 5V_VCC 连接 U1 FB/pin 3，R3 40.2KΩ 从 FB 接 GND，C4 标注 DNP 并联在 R2 两端；C5 10uF 与 C6 100nF 并联在 5V_VCC 与 GND 之间。

- 参数与网络：`upper_feedback=R2 210KΩ`；`lower_feedback=R3 40.2KΩ`；`feedforward=C4 DNP`；`output_filter=C5 10uF,C6 100nF`；`rail=5V_VCC`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 A2 的 U1 FB、R2/R3/C4 与 C5/C6 输出网络

### U6 隔离 5VISO 电源

U6 B0505LS-1WR2 输入 +VIN/-VIN 分别接 5V_VCC/GND，输出 +VO 经 L2 10uH 接 5VISO，-VO 接 GNDISO；非隔离地 GND 与隔离地 GNDISO 在该器件两侧分开。

- 参数与网络：`input=5V_VCC/GND`；`isolator=U6 B0505LS-1WR2`；`output_filter=L2 10uH,C22 100nF`；`output=5VISO/GNDISO`；`galvanic_domains=GND and GNDISO`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 A3 的 U6、C14、L2、C22 与 5V_VCC/GND、5VISO/GNDISO 网络

### 隔离侧 3.3V 电源轨

U2 MD5333 将 5VISO 转为 VCC_3V3；U3 HX6306P332 将 5VISO 转换后经 FB1 330R 磁珠形成 VCC_A3V3。两路 LDO 均以 GNDISO 为地。

- 参数与网络：`mcu_ldo=U2 MD5333`；`mcu_rail=VCC_3V3`；`analog_ldo=U3 HX6306P332`；`analog_filter=FB1 330R`；`analog_rail=VCC_A3V3`；`input=5VISO`；`ground=GNDISO`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 A4 的 U2 MD5333 与网格 B3 的 U3 HX6306P332、FB1 和各自滤波电容

## 接口

### TC1、TC2 热电偶接口

TC1 pin 1 T+ 接 TC1_P、pin 2 T- 接 TC1_N、pin 0 SH 接 GNDISO；TC2 pin 1 T+ 接 TC2_P、pin 2 T- 接 TC2_N、pin 0 SH 接 GNDISO。

- 参数与网络：`TC1=0:SH/GNDISO,1:T+/TC1_P,2:T-/TC1_N`；`TC2=0:SH/GNDISO,1:T+/TC2_P,2:T-/TC2_N`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B4 的 TC1、TC2 连接器引脚号、T+/T-/SH 与 TC1_P/N、TC2_P/N 网络

### J3 M5_BUS 已用针脚

J3 pin 2、4、6 连接 GND，pin 11 连接 CORE_3V3，pin 18 连接 SDA，pin 17 连接 SCL，pin 26、28、30 HPWR 连接 12V，pin 27 连接 5V_VCC，pin 29 连接 BAT_OUT；其余针脚在本页无外部连线。

- 参数与网络：`reference=J3 M5_BUS`；`used_pinout=2:GND,4:GND,6:GND,11:CORE_3V3,17:SCL,18:SDA,26:HPWR/12V,27:5V_VCC,28:HPWR/12V,29:BAT_OUT,30:HPWR/12V`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 D4 的 J3 M5_BUS pin 1-30 与 GND、CORE_3V3、SDA、SCL、12V、5V_VCC、BAT_OUT 外部网络

## 总线

### M5-Bus 至 U5 的隔离 I2C

U7 A 侧 VDDA/GNDA 接 CORE_3V3/GND，SDAA/SCLA 接 J3 SDA/SCL；B 侧 VDDB/GNDB 接 VCC_3V3/GNDISO，SDAB/SCLB 接 MCU_SDA/MCU_SCL，分别到 U5 PA10/pin 18 与 PA9/pin 17。

- 参数与网络：`isolator=U7 CA-IS3020S`；`host_side=CORE_3V3,GND,SDA,SCL`；`isolated_side=VCC_3V3,GNDISO,MCU_SDA,MCU_SCL`；`mcu_sda=U5 PA10/pin 18`；`mcu_scl=U5 PA9/pin 17`；`pullups=R6 10KΩ MCU_SDA,R4 10KΩ MCU_SCL to VCC_3V3`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 D1-D2 U7 CA-IS3020S、C25/C26、SDA/SCL/MCU_SDA/MCU_SCL 与网格 C1 U5/R4/R6

### U5 至 U4 SPI

U5 PA4/pin 10 的 TC_CS 连接 U4 CS/pin 6，PA5/pin 11 的 TC_SCK 连接 U4 SCK/pin 5，PA6/pin 12 的 TC_MISO 连接 U4 MISO/pin 7。

- 参数与网络：`controller=U5 STM32F030F4P6`；`device=U4 MAX6675/31855`；`chip_select=PA4/pin 10 -> TC_CS -> U4 pin 6`；`clock=PA5/pin 11 -> TC_SCK -> U4 pin 5`；`data_to_mcu=PA6/pin 12 <- TC_MISO <- U4 pin 7`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B1-C1 U5 TC_CS/TC_SCK/TC_MISO 与网格 C3 U4 CS/SCK/MISO

## GPIO 与控制信号

### 双热电偶继电器选择控制

U5 PF0-OSC_IN/pin 2 输出 RELAY，经 R11 1KΩ 驱动 Q1 SS8050 基极；R12 10KΩ将基极下拉至 GNDISO，Q1 低侧驱动 5VISO 继电器线圈，D3 1N4148WS T4 跨接线圈。

- 参数与网络：`mcu_pin=U5 PF0-OSC_IN/pin 2`；`control_net=RELAY`；`base_resistor=R11 1KΩ`；`pulldown=R12 10KΩ`；`transistor=Q1 SS8050`；`coil_supply=5VISO`；`flyback=D3 1N4148WS T4`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B2 U5 RELAY 与网格 B4-C4 RELAY-R11-Q1-R12-D3-5VISO 线圈回路

### TC1/TC2 通道 LED

U5 PB1/pin 14 的 LED_CTR 连接 D4、D5 两只 Red 0603；D4 经 R13 1.5KΩ接 VCC_3V3，D5 经 R14 1.5KΩ接 GNDISO，形成 TC1 LED 与 TC2 LED 指示支路。

- 参数与网络：`mcu_pin=U5 PB1/pin 14`；`control_net=LED_CTR`；`tc1_led=D4 Red 0603,R13 1.5KΩ to VCC_3V3`；`tc2_led=D5 Red 0603,R14 1.5KΩ to GNDISO`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B2 U5 LED_CTR 与网格 D3 D4/D5/R13/R14、TC1 LED/TC2 LED

## 时钟

### U5 外部时钟可见性

U5 PF1-OSC_OUT/pin 3 未连接，PF0-OSC_IN/pin 2 被用作 RELAY 控制，原理图未绘出外部晶体、谐振器或振荡器。

- 参数与网络：`osc_in_repurposed=U5 PF0-OSC_IN pin 2 -> RELAY`；`osc_out=U5 PF1-OSC_OUT pin 3 unconnected`；`external_clock_visible=false`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B2 U5 PF0-OSC_IN/RELAY 与 PF1-OSC_OUT 悬空引脚，完整单页无 Y/X 位号

## 复位

### U5 复位、BOOT0 与 SWD

U5 NRST/pin 4 由 R9 10KΩ上拉至 VCC_3V3、C18 100nF接 GNDISO，并引至 J1 pin 4；BOOT0/pin 1 经 R10 10KΩ下拉至 GNDISO。J1 另引出 MCU_SWCLK、MCU_SWDIO、VCC_3V3 和 GNDISO。

- 参数与网络：`reset=U5 NRST/pin 4,R9 10KΩ,C18 100nF,J1 pin 4`；`boot0=U5 pin 1 via R10 10KΩ to GNDISO`；`debug=J1 pin 1:VCC_3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GNDISO`；`swd_pins=U5 PA14/pin 20,PA13/pin 19`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 C2 的 R9/C18/NRST、R10/BOOT0 与网格 D2 的 J1 SWD_5P

## 保护电路

### 电源与接口保护可见性

D1 SS34 用于降压续流，D3 1N4148WS T4 跨接继电器线圈；除这些二极管及图中未标型号的 D2 外，本页未绘出热电偶端口或 M5-Bus 的 TVS/ESD 器件。

- 参数与网络：`buck_catch=D1 SS34`；`relay_flyback=D3 1N4148WS T4`；`output_diode=D2 part number not shown`；`thermocouple_tvs_visible=false`；`m5bus_esd_visible=false`
- 证据：图 33547cd3d7c5 / 第 1 页 / 完整单页 D1/D2/D3 与 TC1/TC2、J3 接口外围器件

## 关键网络

### TC1/TC2 到 TC_P/TC_N 的复用路径

继电器触点连接 TC1_P/TC1_N、TC2_P/TC2_N 与公共 TC_P/TC_N，U4 仅通过公共 TC_P/TC_N 接收被选中的差分热电偶信号。

- 参数与网络：`channel1_pair=TC1_P,TC1_N`；`channel2_pair=TC2_P,TC2_N`；`common_pair=TC_P,TC_N`；`converter_inputs=U4 T+,T-`；`selector=relay`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B4-C4 继电器触点的 TC1_P/N、TC2_P/N、TC_P/N 标注及网格 C3 U4 公共输入

## 模拟电路

### TC_P/TC_N 差分输入滤波

U4 T-/pin 2 与 T+/pin 3 分别经 FB2、FB3 的 330R 磁珠连接 TC_N、TC_P；C20、C21 各 10nF 分别从两输入线接 GNDISO，C15 10nF 跨接差分输入。

- 参数与网络：`negative_input=TC_N -> FB2 330R -> U4 T- pin 2`；`positive_input=TC_P -> FB3 330R -> U4 T+ pin 3`；`common_mode_caps=C20 10nF,C21 10nF to GNDISO`；`differential_cap=C15 10nF`
- 证据：图 33547cd3d7c5 / 第 1 页 / 网格 B3-C3 的 U4 T-/T+、FB2/FB3、C20/C15/C21 与 TC_N/TC_P 网络

## 其他事实

### 其他功能分区可见性

该单页未绘出独立存储器、外部存储、音频器件或射频器件；模拟采样由 U4 热电偶转换器承担。

- 参数与网络：`external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_visible=false`；`analog_frontend=U4 MAX6675/31855 thermocouple converter`
- 证据：图 33547cd3d7c5 / 第 1 页 / 完整单页全部功能区，未见存储、音频或 RF 位号

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 Dual Kmeter 系统架构 | `controller=U5 STM32F030F4P6`；`thermocouple_converter=U4 MAX6675/31855`；`i2c_isolator=U7 CA-IS3020S`；`isolated_dc_dc=U6 B0505LS-1WR2`；`channel_selector=relay driven by Q1`；`inputs=TC1,TC2`；`host=J3 M5_BUS` |
| 电源 | U1 12V 至 5V_VCC 降压 | `input_connector=P1 DC-044`；`input_rail=12V`；`converter=U1 ME3116AM6G`；`enable=R1 100KΩ to 12V`；`switch_pin=LX pin 6`；`inductor=L1 6.8uH`；`catch_diode=D1 SS34`；`output=5V_VCC` |
| 电源 | 5V_VCC 反馈与滤波 | `upper_feedback=R2 210KΩ`；`lower_feedback=R3 40.2KΩ`；`feedforward=C4 DNP`；`output_filter=C5 10uF,C6 100nF`；`rail=5V_VCC` |
| 电源 | U6 隔离 5VISO 电源 | `input=5V_VCC/GND`；`isolator=U6 B0505LS-1WR2`；`output_filter=L2 10uH,C22 100nF`；`output=5VISO/GNDISO`；`galvanic_domains=GND and GNDISO` |
| 电源 | 隔离侧 3.3V 电源轨 | `mcu_ldo=U2 MD5333`；`mcu_rail=VCC_3V3`；`analog_ldo=U3 HX6306P332`；`analog_filter=FB1 330R`；`analog_rail=VCC_A3V3`；`input=5VISO`；`ground=GNDISO` |
| 总线 | M5-Bus 至 U5 的隔离 I2C | `isolator=U7 CA-IS3020S`；`host_side=CORE_3V3,GND,SDA,SCL`；`isolated_side=VCC_3V3,GNDISO,MCU_SDA,MCU_SCL`；`mcu_sda=U5 PA10/pin 18`；`mcu_scl=U5 PA9/pin 17`；`pullups=R6 10KΩ MCU_SDA,R4 10KΩ MCU_SCL to VCC_3V3` |
| 总线地址 | I2C 地址拨码配置 | `switch=SW1 4-position`；`mcu_pins=PA0/pin 6,PA1/pin 7,PA2/pin 8,PA3/pin 9`；`pullups=RP1 4.7KΩ(472)±5%`；`documented_default=0x11`；`documented_range=0x11-0x20`；`schematic_mapping_visible=false` |
| 总线 | U5 至 U4 SPI | `controller=U5 STM32F030F4P6`；`device=U4 MAX6675/31855`；`chip_select=PA4/pin 10 -> TC_CS -> U4 pin 6`；`clock=PA5/pin 11 -> TC_SCK -> U4 pin 5`；`data_to_mcu=PA6/pin 12 <- TC_MISO <- U4 pin 7` |
| 核心器件 | U4 精确型号 | `schematic_value=MAX6675/31855`；`documented_part=MAX31855KASA+T`；`confirmed_part=null` |
| 模拟电路 | TC_P/TC_N 差分输入滤波 | `negative_input=TC_N -> FB2 330R -> U4 T- pin 2`；`positive_input=TC_P -> FB3 330R -> U4 T+ pin 3`；`common_mode_caps=C20 10nF,C21 10nF to GNDISO`；`differential_cap=C15 10nF` |
| 接口 | TC1、TC2 热电偶接口 | `TC1=0:SH/GNDISO,1:T+/TC1_P,2:T-/TC1_N`；`TC2=0:SH/GNDISO,1:T+/TC2_P,2:T-/TC2_N` |
| GPIO 与控制信号 | 双热电偶继电器选择控制 | `mcu_pin=U5 PF0-OSC_IN/pin 2`；`control_net=RELAY`；`base_resistor=R11 1KΩ`；`pulldown=R12 10KΩ`；`transistor=Q1 SS8050`；`coil_supply=5VISO`；`flyback=D3 1N4148WS T4` |
| 核心器件 | 通道选择继电器型号 | `documented_part=AGQ200A4H`；`schematic_reference=null`；`schematic_part_number=null`；`function=TC1/TC2 differential selector` |
| 关键网络 | TC1/TC2 到 TC_P/TC_N 的复用路径 | `channel1_pair=TC1_P,TC1_N`；`channel2_pair=TC2_P,TC2_N`；`common_pair=TC_P,TC_N`；`converter_inputs=U4 T+,T-`；`selector=relay` |
| 接口 | J3 M5_BUS 已用针脚 | `reference=J3 M5_BUS`；`used_pinout=2:GND,4:GND,6:GND,11:CORE_3V3,17:SCL,18:SDA,26:HPWR/12V,27:5V_VCC,28:HPWR/12V,29:BAT_OUT,30:HPWR/12V` |
| 复位 | U5 复位、BOOT0 与 SWD | `reset=U5 NRST/pin 4,R9 10KΩ,C18 100nF,J1 pin 4`；`boot0=U5 pin 1 via R10 10KΩ to GNDISO`；`debug=J1 pin 1:VCC_3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GNDISO`；`swd_pins=U5 PA14/pin 20,PA13/pin 19` |
| 时钟 | U5 外部时钟可见性 | `osc_in_repurposed=U5 PF0-OSC_IN pin 2 -> RELAY`；`osc_out=U5 PF1-OSC_OUT pin 3 unconnected`；`external_clock_visible=false` |
| GPIO 与控制信号 | TC1/TC2 通道 LED | `mcu_pin=U5 PB1/pin 14`；`control_net=LED_CTR`；`tc1_led=D4 Red 0603,R13 1.5KΩ to VCC_3V3`；`tc2_led=D5 Red 0603,R14 1.5KΩ to GNDISO` |
| 保护电路 | 电源与接口保护可见性 | `buck_catch=D1 SS34`；`relay_flyback=D3 1N4148WS T4`；`output_diode=D2 part number not shown`；`thermocouple_tvs_visible=false`；`m5bus_esd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_visible=false`；`analog_frontend=U4 MAX6675/31855 thermocouple converter` |

## 待确认事项

- `address.dip-switch`：SW1 四位开关分别将 U5 PA0-PA3 接至 GNDISO，RP1 四联 4.7KΩ 将这些网络上拉至 VCC_3V3；原理图未打印各组合对应的 I2C 地址或默认 0x11。（证据：图 33547cd3d7c5 / 第 1 页 / 网格 B1 的 SW1/RP1/U5 PA0-PA3 地址输入电路，未见地址数值表）
- `component.thermocouple-converter-model`：原理图把 U4 器件值写为 MAX6675/31855，产品正文记载 MAX31855KASA+T；仅凭本页无法确定装配的精确型号。（证据：图 33547cd3d7c5 / 第 1 页 / 网格 C3 U4 方框顶部器件值 MAX6675/31855）
- `component.relay-part-number`：原理图绘出用于 TC1/TC2 差分切换的继电器符号但未标位号或型号；产品正文记载 AGQ200A4H，无法由本页确认装配料号。（证据：图 33547cd3d7c5 / 第 1 页 / 网格 B4-C4 的继电器线圈与四触点符号，无可见位号或器件值）
- `review.i2c-address-map`：SW1 四位拨码的每种组合如何映射到 I2C 地址，默认地址是否确认为 0x11？；原因：原理图仅显示四位对地输入和上拉，没有打印地址真值表或默认组合。
- `review.converter-model`：U4 实际装配型号是 MAX31855KASA+T 还是 MAX6675 系列器件？；原因：原理图器件值同时写有 MAX6675/31855，无法唯一确定 BOM 料号。
- `review.relay-part-number`：通道选择继电器的实际装配型号是否为产品正文记载的 AGQ200A4H？；原因：原理图中的继电器符号未显示位号或型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `33547cd3d7c5479ba2bdcc75ef580bf886f0e4375fd57dfb2e82ba39ac652f64` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/554/SCH_Module13.2_Dualkmeter_V1.0._sch_01.png` |

---

源文档：`zh_CN/module/DualKmeter Module13.2.md`

源文档 SHA-256：`e3c50f1106e6d7553bdba3db5c4d23f939253e66158bcb48303cd70a67e0d715`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
