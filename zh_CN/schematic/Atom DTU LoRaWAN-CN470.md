# Atom DTU LoRaWAN-CN470 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU LoRaWAN-CN470 |
| SKU | A152-CN470 |
| 产品 ID | `atom-dtu-lorawan-cn470-98a5914f1c4e` |
| 源文档 | `zh_CN/atom/Atom DTU LoRaWAN-CN470.md` |

## 概述

Atom DTU LoRaWAN-CN470 以 M1 RAK3172 为无线通信模组，通过 U2_RX/U2_TX 串口连接 Atom 主控，并经 E1 SMA 天线接口收发射频信号。P1 的 12V+/12V- 输入经 MP1584EN 降压为 +5V，SP3485EN-L/TR 提供另一组 RX/TX 到 RS485_A/RS485_B 的工业接口，同时配置偏置、可选终端和三颗浪涌保护器件。板上还引出 Atom 4Pin/5Pin、Grove I2C、SWD、RST 和 BOOT；原理图确认外部模组为 RAK3172，但未直接给出其内部 MCU 型号。

## 检索关键词

`Atom DTU LoRaWAN-CN470`、`A152-CN470`、`CN470`、`470MHz`、`RAK3172`、`STM32WLE5`、`MP1584EN`、`SP3485EN-L/TR`、`RS485`、`RS485_A`、`RS485_B`、`LoRaWAN`、`LoRa P2P`、`ANT_SMA-KWE`、`U2_RX`、`U2_TX`、`RX`、`TX`、`SWDIO`、`SWCLK`、`RST`、`BOOT`、`+VIN`、`+5V`、`+3.3V`、`G19`、`G22`、`G23`、`G33`、`G21`、`G25`、`HY-2.0_IIC`、`Atom-5Pin`、`Atom-4Pin`、`SMFJ5.0A`、`SP4021-01FTG-C`、`120Ω termination`、`SMA antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | RAK3172 | CN470 LoRaWAN 无线通信模组，连接 UART、射频、SWD、RST、BOOT 和 +3.3V 电源 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页中央 M1 RAK3172，U2_RX/U2_TX、SWDIO/SWCLK、RF、RST/BOOT、VDD/GND |
| U1 | MP1584EN | 从 +VIN 生成经 D7 输出的 +5V 降压电源 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页左上电源区，U1 MP1584EN、F1、L1、D1、R4/R5、D7 与 +VIN/+5V |
| U2 | SP3485EN-L/TR | 3.3V 逻辑侧 RX/TX 与 RS485_A/RS485_B 之间的半双工 RS485 收发器 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页左下 RS485 区，U2 SP3485EN-L/TR 的 RO/RE/DE/DI、A/B、VCC/GND |
| Q1 | S8050 Y1 | 由 TX 经 R15 驱动的 RS485 RE/DE 方向控制晶体管 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页左下 Q1 S8050 Y1、R15 1KΩ 与 U2 RE/DE 公共控制节点 |
| E1 | ANT_SMA-KWE | RAK3172 射频端口的 SMA 天线连接器 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页中左 RF 区，M1 RF 经 R9 0Ω 到 ANT/E1 ANT_SMA-KWE，C14/C15 NC |
| P1 | HDR_4P | RS485 B/A 与 12V+/12V- 电源接线端子 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页右中 P1 HDR_4P，B/A/12V+/12V- 与 RS485_B/RS485_A/+VIN/GND |
| J1 | HY-2.0_IIC | G21/G25 I2C 与 +5V/GND Grove 接口 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页右中 J1 HY-2.0_IIC，pin1 G21/IIC_SCL、pin2 G25/IIC_SDA、pin3 +5V、pin4 GND |
| P2 | Atom-5Pin | Atom 主控的 +3.3V、LoRa UART 和 RS485 UART 接口 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页右下 P2 Atom-5Pin，3V3/G22/G19/G23/G33 与 U2_RX/U2_TX/TX/RX |
| P3 | Atom-4Pin | Atom 主控的 G21/G25/+5V/GND 接口，与 J1 Grove 对应 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页右下 P3 Atom-4Pin，pin1 G21、pin2 G25、pin3 +5V、pin4 GND |
| JP1-JP6 | 未标注 | RAK3172 +3.3V、GND、SWCLK、SWDIO、RST 和 BOOT 调试测试点 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页左中 JP1-JP6，依次标注 +3.3V、GND、SWCLK、SWDIO、RST、BOOT |
| D3,D4,D5 | SP4021-01FTG-C | RS485_A/RS485_B 线对地及线间浪涌保护网络 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页下中 RS485 保护区，D3/D4/D5 SP4021-01FTG-C 与 RS485_B/RS485_A/GND |
| TVS1 | SMFJ5.0A | +5V 电源对地瞬态保护 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页下中右 TVS1 SMFJ5.0A，+5V 到 GND |
| R14 | 120Ω/NC | 跨接 RS485_A 与 RS485_B 的可选终端电阻 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页下中 R14 120Ω/NC，跨接 RS485_B 与 RS485_A |
| F1 | 1.5A/24V | +VIN 输入保险丝 | 图 70a4d5ed1c36 / 第 1 页 / 第 1 页左上 +VIN 串联 F1 1.5A/24V 到 U1 VIN |

## 系统结构

### Atom DTU LoRaWAN-CN470 系统架构

电路由 RAK3172 LoRaWAN 模组、SMA 天线、Atom UART 连接、SP3485EN RS485、12V 输入到 5V 降压、3.3V 模组电源、Grove I2C 以及 SWD/RST/BOOT 调试接口组成。

- 参数与网络：`radio_module=M1 RAK3172`；`radio_interface=U2_RX/U2_TX UART`；`antenna=E1 ANT_SMA-KWE`；`rs485=U2 SP3485EN-L/TR`；`power_converter=U1 MP1584EN`；`host_connectors=P2 Atom-5Pin, P3 Atom-4Pin`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页完整单页原理图，电源、M1、RF、RS485、Atom、Grove 与调试功能区

## 核心器件

### RAK3172 外部 LoRaWAN 模组

M1 型号明确标为 RAK3172，原理图引出 U2_RX/U2_TX、U1_TX/U1_RX、SWDIO/SWCLK、SCL/SDA、RF、SPI、RST、BOOT、ADC 和 GPIO 网络。

- 参数与网络：`reference=M1`；`part_number=RAK3172`；`uart2=pin1 U2_RX, pin2 U2_TX`；`uart1=pin4 U1_TX, pin5 U1_RX`；`debug=pin7 SWDIO, pin8 SWCLK`；`rf=pin12 RF`；`reset=pin22 RST`；`boot=pin21 BOOT`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页中央 M1 RAK3172 全部引脚标签

## 电源

### 12V 输入到 +5V 降压

P1 12V+ 连接 +VIN，+VIN 经 F1 1.5A/24V 进入 U1 MP1584EN；SW 经 L1 22uH 和 D1 SS54 形成降压输出，R4 56kΩ/R5 10kΩ 反馈，输出再经 D7 SS54 形成 +5V。

- 参数与网络：`terminal=P1 12V+ / 12V-`；`input_net=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 22uH`；`catch_diode=D1 SS54`；`feedback=R4 56K, R5 10K`；`output_diode=D7 SS54`；`output_net=+5V`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页左上 U1 电源区与右中 P1，+VIN/F1/MP1584EN/L1/D1/R4/R5/D7/+5V

### RAK3172 3.3V 电源

P2 Atom-5Pin pin1 引入 +3.3V，连接 M1 VDD pin24；C8 100nF、C9 22uF 和 C13 33pF 从该电源节点去耦到 GND。

- 参数与网络：`source=P2 pin1 3V3`；`rail=+3.3V`；`module_pin=M1 VDD pin24`；`decoupling=C8 100nF, C9 22uF, C13 33pF`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页中央 M1 VDD/+3.3V/C8/C9/C13 与右下 P2 pin1

## 接口

### Atom 与 RAK3172 UART 映射

P2 Atom-5Pin 的 G22 经 R18 22Ω 连接 M1 U2_RX，G19 经 R19 22Ω 连接 M1 U2_TX，构成 Atom-Lite/Matrix 引脚命名下的 LoRa UART。

- 参数与网络：`host_tx_pin=P2 pin2 G22`；`module_rx=M1 pin1 U2_RX`；`host_rx_pin=P2 pin3 G19`；`module_tx=M1 pin2 U2_TX`；`series_resistors=R18/R19 22R`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右下 P2 G22/G19、R18/R19 与 U2_RX/U2_TX，以及中央 M1 pin1/pin2

### Atom 与 RS485 收发器 UART 映射

P2 pin4 G23 连接 TX，pin5 G33 连接 RX；RX 经 R12 1kΩ 接 U2 RO 并由 R13 4.7kΩ 上拉，TX 同时参与 U2 数据发送与 Q1/R15 方向控制网络。

- 参数与网络：`host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U2 RO via R12 1K to RX`；`rx_pullup=R13 4.7K to +3.3V`；`direction_control=TX via R15 1K and Q1 S8050 Y1`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右下 P2 G23/G33/TX/RX 与左下 U2/R12/R13/Q1/R15

### P1 RS485 与电源端子

P1 HDR_4P 依次引出 RS485_B、RS485_A、+VIN 和 GND，丝印功能标注为 B、A、12V+、12V-。

- 参数与网络：`pin_b=RS485_B`；`pin_a=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右中 P1 HDR_4P 的 B/A/12V+/12V- 与左侧网络标签

### J1 Grove I2C 接口

J1 HY-2.0_IIC 的 pin1 IIC_SCL=G21、pin2 IIC_SDA=G25、pin3 VCC=+5V、pin4 GND=GND；同名网络连接 P3 Atom-4Pin。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右中 J1 与右下 P3 的 G21/G25/+5V/GND

## 复位

### RAK3172 复位网络

M1 RST pin22 连接 RST 网络，R8 10kΩ 将 RST 上拉到 +3.3V，C7 1uF 将 RST 接到 GND，并通过 JP5 引出。

- 参数与网络：`module_pin=M1 pin22 RST`；`pullup=R8 10K to +3.3V`；`capacitor=C7 1uF to GND`；`testpoint=JP5`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右上 R8/C7/RST、中央 M1 pin22 与左中 JP5

## 保护电路

### 电源输入与 +5V 保护

+VIN 侧由 F1 保险丝、D2 SS54 对地支路和 C2 22uF/35V 保护/滤波；+5V 侧由 TVS1 SMFJ5.0A 对地钳位，并配置 C12 100uF。

- 参数与网络：`input_fuse=F1 1.5A/24V`；`input_diode=D2 SS54`；`input_capacitor=C2 22uF/35V`；`five_volt_tvs=TVS1 SMFJ5.0A`；`five_volt_bulk=C12 100uF`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页左上 +VIN 输入支路与下中右 +5V TVS1/C12

### RS485 偏置和可选终端

RS485_B 由 R11 4.7kΩ 下拉到 GND，RS485_A 由 R16 4.7kΩ 上拉到 +3.3V；R14 120Ω/NC 跨接 A/B 作为可选终端。

- 参数与网络：`B_bias=R11 4.7K to GND`；`A_bias=R16 4.7K to +3.3V`；`termination=R14 120R/NC across A/B`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页下中 U2 A/B、R11/R16 偏置与 R14 120Ω/NC

### RS485 浪涌保护

D3/D4/D5 三颗 SP4021-01FTG-C 配置在 RS485_B、RS485_A 与 GND 周围，形成线对地及线间保护网络。

- 参数与网络：`devices=D3, D4, D5 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页下中 D3/D4/D5 与 RS485_B/RS485_A/GND

## 射频

### RAK3172 到 SMA 天线射频路径

M1 RF pin12 经 R9 0Ω 串联到 ANT 网络和 E1 ANT_SMA-KWE；C14/C15 为从射频路径到 GND 的 NC 匹配电容位。

- 参数与网络：`module_pin=M1 pin12 RF`；`series_element=R9 0R`；`antenna_net=ANT`；`connector=E1 ANT_SMA-KWE`；`matching_shunts=C14 NC, C15 NC`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页中左 M1 RF/R9/ANT/E1/C14/C15

### 470/868/915 MHz 装配选项

原理图装配表将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915；当前产品名称与 SKU 为 CN470 版本。

- 参数与网络：`R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`product_variant=CN470`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页右上装配选项表，R1 0Ω/470、R2 0Ω/868、R3 0Ω/915

## 调试与烧录

### RAK3172 调试测试点

JP1-JP6 依次引出 +3.3V、GND、SWCLK、SWDIO、RST 和 BOOT；SWCLK/SWDIO/RST/BOOT 分别连接 M1 pin8/pin7/pin22/pin21。

- 参数与网络：`JP1=+3.3V`；`JP2=GND`；`JP3=SWCLK -> M1 pin8`；`JP4=SWDIO -> M1 pin7`；`JP5=RST -> M1 pin22`；`JP6=BOOT -> M1 pin21`
- 证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页左中 JP1-JP6 与中央 M1 SWDIO/SWCLK/RST/BOOT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU LoRaWAN-CN470 系统架构 | `radio_module=M1 RAK3172`；`radio_interface=U2_RX/U2_TX UART`；`antenna=E1 ANT_SMA-KWE`；`rs485=U2 SP3485EN-L/TR`；`power_converter=U1 MP1584EN`；`host_connectors=P2 Atom-5Pin, P3 Atom-4Pin` |
| 电源 | 12V 输入到 +5V 降压 | `terminal=P1 12V+ / 12V-`；`input_net=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 22uH`；`catch_diode=D1 SS54`；`feedback=R4 56K, R5 10K`；`output_diode=D7 SS54`；`output_net=+5V` |
| 保护电路 | 电源输入与 +5V 保护 | `input_fuse=F1 1.5A/24V`；`input_diode=D2 SS54`；`input_capacitor=C2 22uF/35V`；`five_volt_tvs=TVS1 SMFJ5.0A`；`five_volt_bulk=C12 100uF` |
| 电源 | RAK3172 3.3V 电源 | `source=P2 pin1 3V3`；`rail=+3.3V`；`module_pin=M1 VDD pin24`；`decoupling=C8 100nF, C9 22uF, C13 33pF` |
| 核心器件 | RAK3172 外部 LoRaWAN 模组 | `reference=M1`；`part_number=RAK3172`；`uart2=pin1 U2_RX, pin2 U2_TX`；`uart1=pin4 U1_TX, pin5 U1_RX`；`debug=pin7 SWDIO, pin8 SWCLK`；`rf=pin12 RF`；`reset=pin22 RST`；`boot=pin21 BOOT` |
| 核心器件 | RAK3172 内部 MCU 型号 | `schematic_module=RAK3172`；`documented_internal_mcu=STM32WLE5`；`internal_schematic_available=false` |
| 射频 | RAK3172 到 SMA 天线射频路径 | `module_pin=M1 pin12 RF`；`series_element=R9 0R`；`antenna_net=ANT`；`connector=E1 ANT_SMA-KWE`；`matching_shunts=C14 NC, C15 NC` |
| 射频 | 470/868/915 MHz 装配选项 | `R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`product_variant=CN470` |
| 接口 | Atom 与 RAK3172 UART 映射 | `host_tx_pin=P2 pin2 G22`；`module_rx=M1 pin1 U2_RX`；`host_rx_pin=P2 pin3 G19`；`module_tx=M1 pin2 U2_TX`；`series_resistors=R18/R19 22R` |
| 接口 | Atom 与 RS485 收发器 UART 映射 | `host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U2 RO via R12 1K to RX`；`rx_pullup=R13 4.7K to +3.3V`；`direction_control=TX via R15 1K and Q1 S8050 Y1` |
| 接口 | P1 RS485 与电源端子 | `pin_b=RS485_B`；`pin_a=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-` |
| 保护电路 | RS485 偏置和可选终端 | `B_bias=R11 4.7K to GND`；`A_bias=R16 4.7K to +3.3V`；`termination=R14 120R/NC across A/B` |
| 保护电路 | RS485 浪涌保护 | `devices=D3, D4, D5 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin` |
| 调试与烧录 | RAK3172 调试测试点 | `JP1=+3.3V`；`JP2=GND`；`JP3=SWCLK -> M1 pin8`；`JP4=SWDIO -> M1 pin7`；`JP5=RST -> M1 pin22`；`JP6=BOOT -> M1 pin21` |
| 复位 | RAK3172 复位网络 | `module_pin=M1 pin22 RST`；`pullup=R8 10K to +3.3V`；`capacitor=C7 1uF to GND`；`testpoint=JP5` |

## 待确认事项

- `component.radio-internal-mcu`：产品正文将 LoRa 方案描述为 STM32WLE5，但当前原理图只将 M1 标为 RAK3172，未展示模组内部芯片或封装标识，因此无法仅凭原理图独立确认内部 MCU 的完整型号。（证据：图 70a4d5ed1c36 / 第 1 页 / 第 1 页中央 M1 型号字段仅标 RAK3172）
- `review.radio-internal-mcu`：当前 A152-CN470 所装 RAK3172 模组的内部 MCU 是否确认为产品正文所述 STM32WLE5，具体后缀和硬件版本是什么？；原因：当前原理图只给出模组料号 RAK3172，没有展开内部器件；需要模组 BOM、丝印或官方模组资料确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `70a4d5ed1c36f2e3667818970c8fb2db0e9d2b6af530d1a899ae3e0f768d03d3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1138/A152_CN470_Sch_page_01.png` |

---

源文档：`zh_CN/atom/Atom DTU LoRaWAN-CN470.md`

源文档 SHA-256：`0e7e9eb34840a86cf4c5679a54d11f6cc2cc6304a24732e0f119ed8ae87c282d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
