# Module13.2 4Relay v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 4Relay v1.1 |
| SKU | M121-V11 |
| 产品 ID | `module13-2-4relay-v1-1-965327c80c46` |
| 源文档 | `zh_CN/module/4Relay Module 13.2_V1.1.md` |

## 概述

Module13.2 4Relay v1.1 以 STM32F030F4P6（U1）通过 I2C 接收控制，并以 PA1~PA4 驱动四组 SS8050 Y1 低边晶体管和 5V 继电器线圈。HPWR 经 AOZ1282CI（U2）降压为 3.3V_VCC，再由 SY7088（U3）升压为 +5V；HPWR 还通过 210K/30K 分压送入 PA0 进行电压采样。四路 Kx/KxCOM 触点由 P2/P4/P6/P8 引出，并通过 P3/P5/P7/P9 与 VIN/GND 模式母线配置；P10/P11 提供 HPWR/GND 与外部 VIN/GND 的选择和输入路径。

## 检索关键词

`Module13.2 4Relay v1.1`、`M121-V11`、`STM32F030F4P6`、`STM32G030F6`、`AOZ1282CI`、`SY7088`、`Relay-SPDT`、`SS8050 Y1`、`1N4148WS T4`、`I2C`、`0x26`、`SCL`、`SDA`、`Relay1`、`Relay2`、`Relay3`、`Relay4`、`K1COM`、`K2COM`、`K3COM`、`K4COM`、`HPWR`、`VIN`、`3.3V_VCC`、`+5V`、`PA0`、`M5Stack_BUS`、`SMF30CA`、`DSS34`、`DC5521`、`SWD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 主控 MCU，处理 I2C、四路继电器控制、HPWR 电压采样和 SWD | 图 e9746e2be7b2 / 第 1 页 / B1-C2 区域 U1 STM32F030F4P6：PA0、Relay1~4、SCL/SDA、SWDIO/SWCLK、BOOT0/NRST |
| U2 | AOZ1282CI | 将 HPWR 降压生成 3.3V_VCC 的开关转换器 | 图 e9746e2be7b2 / 第 1 页 / D1-D2 区域 U2 AOZ1282CI 与 C5/L1/D5/R7/R8 输入输出网络 |
| U3 | SY7088 | 由 3.3V_VCC 生成 +5V 的升压转换器 | 图 e9746e2be7b2 / 第 1 页 / D3 区域 U3 SY7088 与 L2/R9/R17/C9/C12/C13/D6 网络 |
| K1/K2/K3/K4 | Relay-SPDT | 四路 5V 线圈机械继电器，分别提供 K1~K4 与 K1COM~K4COM 触点 | 图 e9746e2be7b2 / 第 1 页 / A1-A4 顶部四组 K1~K4 Relay-SPDT 线圈与触点 |
| Q1/Q2/Q3/Q4 | SS8050 Y1 | 四路继电器线圈的 NPN 低边驱动晶体管 | 图 e9746e2be7b2 / 第 1 页 / A1-A4 各继电器线圈下方 Q1~Q4 SS8050 Y1，发射极接 GND |
| D1/D2/D3/D4 | 1N4148WS T4 | 分别跨接四个继电器线圈的续流二极管 | 图 e9746e2be7b2 / 第 1 页 / A1-A4 四个线圈左侧 D1~D4 1N4148WS T4 跨线圈连接 |
| J1 | M5Stack_BUS | 30 针 M5-Bus 主机接口，使用 GND、3.3V、SDA/GPIO21、SCL/GPIO22、HPWR 和 +5V | 图 e9746e2be7b2 / 第 1 页 / B3-C3 区域 J1 M5Stack_BUS 1~30 脚及 GPIO/电源标注 |
| P1 | SWD_5p | MCU SWD 调试接口，引出 3.3V、SWCLK、SWDIO、RST 和 GND | 图 e9746e2be7b2 / 第 1 页 / B2 区域 P1 SWD_5p：VCC/SWCLK/SWDIO/RST/GND |
| P2/P4/P6/P8 | Header 2 | 四路继电器输出端，分别引出 K1/K1COM 至 K4/K4COM | 图 e9746e2be7b2 / 第 1 页 / B4-C4 区域 P2/P4/P6/P8 Header 2 与 K1/K1COM、K2/K2COM、K3/K3COM、K4/K4COM |
| P3/P5/P7/P9 | Header 2X2 | 四路继电器有源/无源模式跳线接口，将 Kx/KxCOM 与 VIN/GND 母线配置连接 | 图 e9746e2be7b2 / 第 1 页 / B4-C4 区域 P3/P5/P7/P9 左侧 Kx/KxCOM、右侧两条 VIN/GND 纵向母线 |
| P10/P11 | Header 2X2 / Header 2 | HPWR/GND 到模式母线的跳线选择与外部 VIN/GND 输入接口 | 图 e9746e2be7b2 / 第 1 页 / C4-D4 区域 P10 Header 2X2 的 HPWR/GND 与 P11 Header 2 的 VIN/GND 母线连接 |
| D7 | SMF30CA | VIN 对 GND 的瞬态电压抑制器 | 图 e9746e2be7b2 / 第 1 页 / D4 区域 P11 左侧 D7 SMF30CA 跨接 VIN 与 GND |
| R16/R18/R19 | 210K / 1K / 30K | HPWR 到 PA0 的电压采样分压与串联限流网络 | 图 e9746e2be7b2 / 第 1 页 / C1-C2 区域 HPWR-R16 210K-R19 30K-GND 分压节点，经 R18 1K 到 PA0 |
| L1/D5 | 6.8uH / DSS34 | AOZ1282CI 降压级输出电感与开关节点二极管 | 图 e9746e2be7b2 / 第 1 页 / D2 区域 U2.6 LX 至 3.3V_VCC 的 L1 6.8uH 与 LX-GND 的 D5 DSS34 |
| L2 | 2.2uH/3015 | SY7088 升压级从 3.3V_VCC 到 LX 的储能电感 | 图 e9746e2be7b2 / 第 1 页 / D3 区域 3.3V_VCC 与 U3 LX 之间 L2 2.2uH/3015 |

## 系统结构

### Module13.2 4Relay v1.1

U1 STM32F030F4P6 通过 I2C 控制四路继电器驱动；HPWR 经 U2 生成 3.3V_VCC，再经 U3 生成 +5V；VIN/GND 模式母线通过跳线连接继电器触点。

- 参数与网络：`controller=U1 STM32F030F4P6`；`relay_channels=4`；`buck=U2 AOZ1282CI HPWR to 3.3V_VCC`；`boost=U3 SY7088 3.3V_VCC to +5V`；`mode_bus=VIN/GND`；`host=J1 M5Stack_BUS`
- 证据：图 e9746e2be7b2 / 第 1 页 / 全页四路继电器、U1/J1、U2/U3 与右侧模式跳线/输入母线

## 核心器件

### U1 STM32F030F4P6

U1.6 PA0 接电压采样，U1.7~U1.10 PA1~PA4 分别接 Relay1~Relay4，U1.17 PA9 接 SCL，U1.18 PA10 接 SDA，U1.19/U1.20 接 SWDIO/SWCLK。

- 参数与网络：`pin_6=PA0 voltage sample`；`pin_7=PA1 Relay1`；`pin_8=PA2 Relay2`；`pin_9=PA3 Relay3`；`pin_10=PA4 Relay4`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 SWDIO`；`pin_20=PA14 SWCLK`
- 证据：图 e9746e2be7b2 / 第 1 页 / B1-C2 区域 U1 引脚编号、GPIO 名称与网络标签

## 电源

### U2 AOZ1282CI 降压级

U2 VIN 接 HPWR，EN 经 R14 100K 接 HPWR；LX 经 L1 6.8uH 输出 3.3V_VCC，D5 DSS34 接在 LX 与 GND 之间，R7 200K/R8 62K 构成反馈。

- 参数与网络：`input=HPWR`；`enable=R14 100K to HPWR`；`switch=U2.6 LX`；`inductor=L1 6.8uH`；`diode=D5 DSS34`；`output=3.3V_VCC`；`feedback=R7 200K / R8 62K`；`feedforward=C8 DNP`
- 证据：图 e9746e2be7b2 / 第 1 页 / D1-D2 U2 输入、BST/LX/L1/D5、FB/R7/R8/C8 与输出电容

### U3 SY7088 升压级

3.3V_VCC 经 L2 2.2uH/3015 连接 U3 LX，U3 OUT 产生 +5V；R9 15K 与 R17 4.7K 形成 FB 分压，C12/C13 与 C15 为输出储能，D6 跨接 +5V 与 GND。

- 参数与网络：`input=3.3V_VCC`；`inductor=L2 2.2uH/3015`；`converter=U3 SY7088`；`output=+5V`；`feedback=R9 15K / R17 4.7K`；`output_caps=C12/C13 22uF/6.3V; C15 100uF/16V`；`clamp=D6 +5V-GND`
- 证据：图 e9746e2be7b2 / 第 1 页 / D3-D4 U3/L2/R9/R17/C12/C13/D6/C15 的 3.3V_VCC 至 +5V 电路

### 3.3V 与 +5V 分配

3.3V_VCC 连接 U1 3.3V 供电和 J1.12 +3.3V；+5V 连接四个继电器线圈、J1.28 +5V 和输出滤波网络。

- 参数与网络：`3v3_loads=U1 VDD/VDDA; J1.12`；`5v_loads=K1-K4 coils; J1.28`；`mcu_decoupling=C2/C3 100nF; C4 10uF`
- 证据：图 e9746e2be7b2 / 第 1 页 / 全页 +3.3V/3.3V_VCC 与 +5V 同名网络在 U1/J1/K1~K4/U3 上的分配

## 接口

### J1 M5Stack_BUS

J1.1/3/5 接 GND，J1.12 接 +3.3V，J1.17 接 SDA，J1.18 接 SCL，J1.25/27/29 接 HPWR，J1.28 接 +5V；其余图示 GPIO 与 BATTERY 脚未连接。

- 参数与网络：`ground=pins 1,3,5`；`3v3=pin 12`；`sda=pin 17 GPIO21`；`scl=pin 18 GPIO22`；`hpwr=pins 25,27,29`；`5v=pin 28`；`battery_pin_30=NC`
- 证据：图 e9746e2be7b2 / 第 1 页 / B3-C3 区域 J1 1~30 脚的网络、连接点和未连接短线

### 四路继电器输出

P2 引出 K1/K1COM，P4 引出 K2/K2COM，P6 引出 K3/K3COM，P8 引出 K4/K4COM。

- 参数与网络：`P2=K1, K1COM`；`P4=K2, K2COM`；`P6=K3, K3COM`；`P8=K4, K4COM`
- 证据：图 e9746e2be7b2 / 第 1 页 / B4-C4 P2/P4/P6/P8 Header 2 与对应 Kx/KxCOM 网络

### P3/P5/P7/P9 模式跳线

每路 2×2 跳线的左侧连接 Kx 与 KxCOM，右侧连接两条 VIN/GND 纵向母线，用于配置触点是否带入外部电源。

- 参数与网络：`channel_1=P3 K1/K1COM to VIN/GND`；`channel_2=P5 K2/K2COM to VIN/GND`；`channel_3=P7 K3/K3COM to VIN/GND`；`channel_4=P9 K4/K4COM to VIN/GND`
- 证据：图 e9746e2be7b2 / 第 1 页 / B4-C4 P3/P5/P7/P9 的四针网络与右侧两条纵向母线

### P10/P11 外部电源

P10 将 HPWR/GND 通过 2×2 跳线连接到右侧 VIN/GND 母线，P11 Header 2 直接连接该两条母线；D7 SMF30CA 跨接 VIN 与 GND。

- 参数与网络：`source_selection=P10 HPWR/GND to VIN/GND`；`external_input=P11 Header 2`；`protection=D7 SMF30CA VIN-GND`
- 证据：图 e9746e2be7b2 / 第 1 页 / C4-D4 P10/P11、HPWR/GND、VIN/GND 母线与 D7

## 总线

### SCL/SDA

J1.17 GPIO21/SDA 连接 U1.18 PA10，J1.18 GPIO22/SCL 连接 U1.17 PA9；页面未显示 I2C 上拉或电平转换。

- 参数与网络：`sda=J1.17 GPIO21 to U1.18 PA10`；`scl=J1.18 GPIO22 to U1.17 PA9`；`pullups=not shown`；`level_shifter=not shown`
- 证据：图 e9746e2be7b2 / 第 1 页 / B2-B3 区域 U1 SCL/SDA 与 J1.17/J1.18 同名网络

## GPIO 与控制信号

### Relay1~Relay4

Relay1~Relay4 各经 R1~R4 1K 驱动 Q1~Q4 SS8050 Y1 基极，R10~R13 10K 将基极下拉至 GND；晶体管发射极接地、集电极接继电器线圈低端。

- 参数与网络：`channel_1=Relay1-R1-Q1-K1`；`channel_2=Relay2-R2-Q2-K2`；`channel_3=Relay3-R3-Q3-K3`；`channel_4=Relay4-R4-Q4-K4`；`base_resistors=R1-R4 1K`；`base_pulldowns=R10-R13 10K`
- 证据：图 e9746e2be7b2 / 第 1 页 / A1-A4 四组 Relayx/Rx/Qx/R10~R13/线圈完全对称电路

## 时钟

### U1 时钟

U1.2 PF0/OSC_IN 与 U1.3 PF1/OSC_OUT 未连接，页面未显示外部晶振或谐振器。

- 参数与网络：`osc_in=U1.2 NC`；`osc_out=U1.3 NC`；`external_crystal=not shown`
- 证据：图 e9746e2be7b2 / 第 1 页 / B1-B2 U1.2/U1.3 PF0/OSC_IN、PF1/OSC_OUT 未连接标记

## 复位

### BOOT0、NRST 与 SWD

U1.1 BOOT0 通过 R5 10K 接 GND；NRST 由 R6 10K 上拉到 +3.3V、C1 100nF 对地，并引至 P1 RST；P1 还引出 SWCLK/SWDIO。

- 参数与网络：`boot0=U1.1 via R5 10K to GND`；`nrst_pullup=R6 10K to +3.3V`；`nrst_cap=C1 100nF to GND`；`debug=P1 SWCLK/SWDIO/RST`
- 证据：图 e9746e2be7b2 / 第 1 页 / B1-B2 U1 BOOT0/RST、R5/R6/C1 与 P1 SWD_5p

## 保护电路

### 继电器线圈续流

D1~D4 1N4148WS T4 分别跨接 K1~K4 的 +5V 线圈两端。

- 参数与网络：`K1=D1 1N4148WS T4`；`K2=D2 1N4148WS T4`；`K3=D3 1N4148WS T4`；`K4=D4 1N4148WS T4`
- 证据：图 e9746e2be7b2 / 第 1 页 / A1-A4 D1~D4 与四个继电器线圈并联

### VIN 输入保护

D7 SMF30CA 跨接 VIN 与 GND，位于 P11 外部输入母线旁。

- 参数与网络：`protector=D7 SMF30CA`；`protected_net=VIN`；`reference=GND`
- 证据：图 e9746e2be7b2 / 第 1 页 / D4 D7 SMF30CA 的 VIN-GND 跨接

## 模拟电路

### HPWR 电压采样

HPWR 经 R16 210K 与 R19 30K 分压，分压节点再经 R18 1K 连接 U1.6 PA0。

- 参数与网络：`input=HPWR`；`upper_resistor=R16 210K`；`lower_resistor=R19 30K`；`series_resistor=R18 1K`；`adc_pin=U1.6 PA0`；`nominal_divider=30K/(210K+30K)`
- 证据：图 e9746e2be7b2 / 第 1 页 / C1-C2 HPWR-R16/R19 分压与 R18-PA0 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 4Relay v1.1 | `controller=U1 STM32F030F4P6`；`relay_channels=4`；`buck=U2 AOZ1282CI HPWR to 3.3V_VCC`；`boost=U3 SY7088 3.3V_VCC to +5V`；`mode_bus=VIN/GND`；`host=J1 M5Stack_BUS` |
| 核心器件 | U1 STM32F030F4P6 | `pin_6=PA0 voltage sample`；`pin_7=PA1 Relay1`；`pin_8=PA2 Relay2`；`pin_9=PA3 Relay3`；`pin_10=PA4 Relay4`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 SWDIO`；`pin_20=PA14 SWCLK` |
| 核心器件 | MCU 版本 | `schematic_model=STM32F030F4P6`；`document_feature_model=STM32G030F6`；`production_model=not confirmed` |
| 总线 | SCL/SDA | `sda=J1.17 GPIO21 to U1.18 PA10`；`scl=J1.18 GPIO22 to U1.17 PA9`；`pullups=not shown`；`level_shifter=not shown` |
| 总线地址 | 模块 I2C 地址 | `documented_address=0x26`；`schematic_address_label=not shown`；`address_straps=not shown`；`firmware_evidence=not shown` |
| 接口 | J1 M5Stack_BUS | `ground=pins 1,3,5`；`3v3=pin 12`；`sda=pin 17 GPIO21`；`scl=pin 18 GPIO22`；`hpwr=pins 25,27,29`；`5v=pin 28`；`battery_pin_30=NC` |
| GPIO 与控制信号 | Relay1~Relay4 | `channel_1=Relay1-R1-Q1-K1`；`channel_2=Relay2-R2-Q2-K2`；`channel_3=Relay3-R3-Q3-K3`；`channel_4=Relay4-R4-Q4-K4`；`base_resistors=R1-R4 1K`；`base_pulldowns=R10-R13 10K` |
| 保护电路 | 继电器线圈续流 | `K1=D1 1N4148WS T4`；`K2=D2 1N4148WS T4`；`K3=D3 1N4148WS T4`；`K4=D4 1N4148WS T4` |
| 接口 | 四路继电器输出 | `P2=K1, K1COM`；`P4=K2, K2COM`；`P6=K3, K3COM`；`P8=K4, K4COM` |
| 接口 | P3/P5/P7/P9 模式跳线 | `channel_1=P3 K1/K1COM to VIN/GND`；`channel_2=P5 K2/K2COM to VIN/GND`；`channel_3=P7 K3/K3COM to VIN/GND`；`channel_4=P9 K4/K4COM to VIN/GND` |
| 接口 | P10/P11 外部电源 | `source_selection=P10 HPWR/GND to VIN/GND`；`external_input=P11 Header 2`；`protection=D7 SMF30CA VIN-GND` |
| 接口 | 外部电源连接器 | `documented_connector=DC5521 5.5x2.1mm`；`schematic_connector=P11 Header 2`；`production_connector=not confirmed` |
| 模拟电路 | HPWR 电压采样 | `input=HPWR`；`upper_resistor=R16 210K`；`lower_resistor=R19 30K`；`series_resistor=R18 1K`；`adc_pin=U1.6 PA0`；`nominal_divider=30K/(210K+30K)` |
| 电源 | U2 AOZ1282CI 降压级 | `input=HPWR`；`enable=R14 100K to HPWR`；`switch=U2.6 LX`；`inductor=L1 6.8uH`；`diode=D5 DSS34`；`output=3.3V_VCC`；`feedback=R7 200K / R8 62K`；`feedforward=C8 DNP` |
| 电源 | U3 SY7088 升压级 | `input=3.3V_VCC`；`inductor=L2 2.2uH/3015`；`converter=U3 SY7088`；`output=+5V`；`feedback=R9 15K / R17 4.7K`；`output_caps=C12/C13 22uF/6.3V; C15 100uF/16V`；`clamp=D6 +5V-GND` |
| 电源 | 3.3V 与 +5V 分配 | `3v3_loads=U1 VDD/VDDA; J1.12`；`5v_loads=K1-K4 coils; J1.28`；`mcu_decoupling=C2/C3 100nF; C4 10uF` |
| 其他事实 | 继电器负载额定值 | `documented_rating=DC 24V@1A, 24W`；`schematic_relay_label=Relay-SPDT`；`relay_part_number=not shown`；`contact_rating=not shown` |
| 复位 | BOOT0、NRST 与 SWD | `boot0=U1.1 via R5 10K to GND`；`nrst_pullup=R6 10K to +3.3V`；`nrst_cap=C1 100nF to GND`；`debug=P1 SWCLK/SWDIO/RST` |
| 时钟 | U1 时钟 | `osc_in=U1.2 NC`；`osc_out=U1.3 NC`；`external_crystal=not shown` |
| 保护电路 | VIN 输入保护 | `protector=D7 SMF30CA`；`protected_net=VIN`；`reference=GND` |

## 待确认事项

- `component.mcu-version-conflict`：原理图 U1 明确标注 STM32F030F4P6，产品正文特性却写 STM32G030F6；无法确认 M121-V11 量产板最终装配型号。（证据：图 e9746e2be7b2 / 第 1 页 / B1-C2 区域 U1 器件底部明确标注 STM32F030F4P6）
- `address.i2c-0x26`：产品正文标注 I2C 地址为 0x26，但原理图未标注地址、地址选择网络或固件版本，无法仅由该页确认。（证据：图 e9746e2be7b2 / 第 1 页 / 全页 U1 与 SCL/SDA 网络，未见 0x26 或地址配置）
- `interface.external-connector-type-conflict`：产品正文规格声明 DC5521 5.5×2.1mm 输入座，但原理图对应外部 VIN/GND 的 P11 标注为 Header 2，无法确认量产板连接器型号。（证据：图 e9746e2be7b2 / 第 1 页 / D4 区域外部电源母线末端 P11 明确标注 Header 2）
- `other.relay-load-rating`：产品正文声明四通道最大负载为 DC 24V@1A/24W，但原理图中的 K1~K4 仅标注 Relay-SPDT，未给出继电器完整型号或触点额定值。（证据：图 e9746e2be7b2 / 第 1 页 / A1-A4 K1~K4 均只标注 Relay-SPDT，无触点额定参数）
- `review.mcu-version`：M121-V11 量产板实际使用 STM32F030F4P6 还是 STM32G030F6？；原因：正式原理图 U1 标注 STM32F030F4P6，产品正文特性标注 STM32G030F6。
- `review.i2c-address-0x26`：模块 I2C 地址 0x26 是否由 MCU 固件固定实现？；原因：原理图仅显示 SCL/SDA，不含地址或固件信息。
- `review.external-connector`：外部 5~24V 输入的量产连接器是 DC5521 还是 P11 两针端子？；原因：正文规格和原理图连接器类型不一致。
- `review.relay-rating`：K1~K4 实际继电器料号及 DC 24V@1A 触点额定条件是什么？；原因：原理图只写 Relay-SPDT，无法核对正文的负载额定值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e9746e2be7b233efcace061df02a1452df1e1f1c3159da21066d1be2fd02b1d0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/548/Sch_4Relay_13.2_Module_V1.1_sch_01.png` |

---

源文档：`zh_CN/module/4Relay Module 13.2_V1.1.md`

源文档 SHA-256：`4cbec29cb53f1e76e43e121155f381a40553765936a09339a343e286ade901c6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
