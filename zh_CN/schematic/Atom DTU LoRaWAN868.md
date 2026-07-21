# Atom DTU LoRaWAN868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU LoRaWAN868 |
| SKU | K063 |
| 产品 ID | `atom-dtu-lorawan868-e296ebc8f834` |
| 源文档 | `zh_CN/atom/atom_dtu_lorawan868.md` |

## 概述

Atom DTU LoRaWAN868 以 M1 Ra-07/Ra-07H 无线模组为核心，通过 UTXD/URXD 串口连接 Atom G19/G22，并经 E1 SMA 天线接口连接外部天线。P1 的 12V+/12V- 输入经 MP1584EN 降压为 +5V，SP3485EN-L/TR 将 Atom G23/G33 的 TX/RX 转换为带偏置、可选 120Ω 终端和 SP4021 浪涌保护的 RS485_A/RS485_B。板上另有 Grove I2C、Atom 4Pin/5Pin、SWD/RESET 测试点和 470/868/915 MHz 装配选项；原理图未展开 Ra-07/Ra-07H 内部芯片和固件参数。

## 检索关键词

`Atom DTU LoRaWAN868`、`K063`、`868MHz`、`Ra-07`、`Ra-07H`、`ASR6501`、`MP1584EN`、`SP3485EN-L/TR`、`LoRaWAN`、`RS485`、`RS485_A`、`RS485_B`、`UTXD`、`URXD`、`TX`、`RX`、`ANT_SMA-KWE`、`SWCLK`、`SWDIO`、`RESET`、`+VIN`、`+5V`、`+3.3V`、`G19`、`G22`、`G23`、`G33`、`G21`、`G25`、`Atom-5Pin`、`Atom-4Pin`、`HY-2.0_IIC`、`SP4021-01FTG-C`、`120Ω termination`、`115200bps`、`LoRaWAN v1.0.1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | Ra-07/Ra-07H | 868 MHz 版本无线通信模组，连接 UART、射频、SWD、RESET、GPIO 和 +3.3V 电源 | 图 413dc7fd72ca / 第 1 页 / 第 1 页中部 M1 Ra-07/Ra-07H，GND/ADC/AUX/SETA/DIO3/SETB/SWCLK/SWDIO/VCC 与 ANT/RESET/Pxx/UTX/URX |
| U1 | MP1584EN | 从 +VIN 生成 +5V 的降压转换器 | 图 413dc7fd72ca / 第 1 页 / 第 1 页左上 U1 MP1584EN、F1、L1 10uH、R4/R5 与 +VIN/+5V |
| U2 | SP3485EN-L/TR | 3.3V 逻辑侧 TX/RX 与 RS485_A/RS485_B 之间的半双工收发器 | 图 413dc7fd72ca / 第 1 页 / 第 1 页左下 U2 SP3485EN-L/TR，RO/RE/DE/DI、A/B、VCC/GND |
| Q1 | SS8050 Y1 | 由 TX 经 R15 驱动的 RS485 RE/DE 方向控制晶体管 | 图 413dc7fd72ca / 第 1 页 / 第 1 页左下 Q1 SS8050 Y1、R15 1KΩ 与 U2 RE/DE |
| E1 | ANT_SMA-KWE | Ra-07/Ra-07H ANT 引脚的 SMA 天线接口 | 图 413dc7fd72ca / 第 1 页 / 第 1 页中右 M1 ANT pin18 经 R8 0Ω 到 E1 ANT_SMA-KWE |
| P1 | HDR_4P | RS485 B/A 与 12V+/12V- 电源端子 | 图 413dc7fd72ca / 第 1 页 / 第 1 页右中 P1 HDR_4P，RS485_B/RS485_A/+VIN/GND 与 B/A/12V+/12V- |
| J1 | HY-2.0_IIC | G21/G25 I2C 与 +5V/GND Grove 接口 | 图 413dc7fd72ca / 第 1 页 / 第 1 页右中 J1 HY-2.0_IIC，G21/IIC_SCL、G25/IIC_SDA、+5V、GND |
| P2 | Atom-5Pin | Atom 的 +3.3V、LoRa UART 和 RS485 UART 接口 | 图 413dc7fd72ca / 第 1 页 / 第 1 页右下 P2 Atom-5Pin，3V3/G22/G19/G23/G33 与 URXD/UTXD/TX/RX |
| P3 | Atom-4Pin | Atom 的 G21/G25/+5V/GND 接口，与 J1 Grove 对应 | 图 413dc7fd72ca / 第 1 页 / 第 1 页右下 P3 Atom-4Pin，G21/G25/+5V/GND |
| JP1-JP5 | 未标注 | +3.3V、GND、SWC、SWD 和 RESET 调试测试点 | 图 413dc7fd72ca / 第 1 页 / 第 1 页左中 JP1-JP5，依次标注 +3.3V、GND、SWC、SWD、RESET |
| D3,D4,D5 | SP4021-01FTG-C | RS485_A/RS485_B 线对地及线间浪涌保护网络 | 图 413dc7fd72ca / 第 1 页 / 第 1 页下中 D3/D4/D5 SP4021-01FTG-C 与 RS485_B/RS485_A/GND |
| R14 | 120Ω/NC | 跨接 RS485_A/RS485_B 的可选终端电阻 | 图 413dc7fd72ca / 第 1 页 / 第 1 页下中 R14 120Ω/NC，跨接 RS485_B 与 RS485_A |
| F1 | 1.5A/24V | +VIN 输入保险丝 | 图 413dc7fd72ca / 第 1 页 / 第 1 页左上 +VIN 串联 F1 1.5A/24V 到 U1 VIN |

## 系统结构

### Atom DTU LoRaWAN868 系统架构

电路由 Ra-07/Ra-07H 无线模组、SMA 天线、Atom UART、SP3485EN RS485、12V 输入到 5V 降压、Grove I2C 和 SWD/RESET 测试点组成。

- 参数与网络：`radio_module=M1 Ra-07/Ra-07H`；`radio_uart=UTXD/URXD`；`antenna=E1 ANT_SMA-KWE`；`rs485=U2 SP3485EN-L/TR`；`power_converter=U1 MP1584EN`；`host_connectors=P2 Atom-5Pin, P3 Atom-4Pin`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页完整单页原理图，电源、M1、RF、RS485、Atom、Grove 和调试区

## 核心器件

### Ra-07/Ra-07H 外部无线模组

M1 型号字段为 Ra-07/Ra-07H，原理图引出 ADC、AUX、SETA/SETB、DIO3、SWCLK/SWDIO、ANT、RESET、P07/P06/P01/P00、UTX/URX 和电源地。

- 参数与网络：`reference=M1`；`part_number=Ra-07/Ra-07H`；`uart=pin11 UTX, pin10 URX`；`debug=pin7 SWCLK, pin8 SWDIO`；`rf=pin18 ANT`；`reset=pin16 RESET`；`power=pin9 VCC`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页中部 M1 Ra-07/Ra-07H 全部引脚标签

## 电源

### 12V 输入到 +5V 降压

P1 12V+ 连接 +VIN，+VIN 经 F1 1.5A/24V 进入 U1 MP1584EN；SW 经 L1 10uH 和 D1 SS54 形成降压输出，R4 51kΩ/R5 10kΩ 反馈，输出网络为 +5V。

- 参数与网络：`terminal=P1 12V+ / 12V-`；`input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`feedback=R4 51K, R5 10K`；`output=+5V`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页左上 U1 电源区与右中 P1，+VIN/F1/MP1584EN/L1/R4/R5/+5V

### Ra-07/Ra-07H 3.3V 电源

P2 Atom-5Pin pin1 引入 +3.3V 并连接 M1 VCC pin9；C7 100nF、C8 10uF 和 C9 33pF 从该节点去耦到 GND。

- 参数与网络：`source=P2 pin1 3V3`；`module_pin=M1 VCC pin9`；`decoupling=C7 100nF, C8 10uF, C9 33pF`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页中部 M1 VCC/+3.3V/C7/C8/C9 与右下 P2 pin1

## 接口

### Atom 与无线模组 UART 映射

P2 pin2 G22 连接 URXD，并经 R10 22Ω 到 M1 URX pin10；P2 pin3 G19 连接 UTXD，并经 R9 22Ω 到 M1 UTX pin11。

- 参数与网络：`host_tx=P2 pin2 G22 -> URXD -> R10 -> M1 URX pin10`；`host_rx=P2 pin3 G19 -> UTXD -> R9 -> M1 UTX pin11`；`series_resistors=R9/R10 22R`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页中部 M1 UTX/URX/R9/R10 与右下 P2 G22/G19/URXD/UTXD

### Atom 与 RS485 UART 映射

P2 pin4 G23 连接 TX，pin5 G33 连接 RX；RX 经 R12 1kΩ 接 U2 RO 并由 R13 4.7kΩ 上拉，TX 经 R15 1kΩ 驱动 Q1 以控制 U2 RE/DE。

- 参数与网络：`host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U2 RO via R12 1K to RX`；`rx_pullup=R13 4.7K to +3.3V`；`direction_control=TX via R15 1K and Q1 SS8050 Y1`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页右下 P2 G23/G33/TX/RX 与左下 U2/R12/R13/Q1/R15

### P1 RS485 与电源端子

P1 HDR_4P 依次引出 RS485_B、RS485_A、+VIN 和 GND，端子功能标注为 B、A、12V+、12V-。

- 参数与网络：`B=RS485_B`；`A=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页右中 P1 HDR_4P 的 RS485_B/RS485_A/+VIN/GND

### J1 Grove I2C 接口

J1 HY-2.0_IIC 的 pin1 IIC_SCL=G21、pin2 IIC_SDA=G25、pin3 VCC=+5V、pin4 GND=GND；同名网络连接 P3 Atom-4Pin。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页右中 J1 与右下 P3 的 G21/G25/+5V/GND

## 保护电路

### +VIN 输入保护与滤波

+VIN 经 F1 串联保护，D2 SS54 和 C2 10uF 分别从保险后输入节点接到 GND，U1 EN pin2 在图中标为未连接。

- 参数与网络：`fuse=F1 1.5A/24V`；`shunt_diode=D2 SS54`；`input_capacitor=C2 10uF`；`enable_pin=U1 EN pin2 NC`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页左上 +VIN/F1/D2/C2/U1 EN

### RS485 偏置与可选终端

RS485_B 由 R11 4.7kΩ 下拉到 GND，RS485_A 由 R16 4.7kΩ 上拉到 +3.3V；R14 120Ω/NC 跨接 A/B 作为可选终端。

- 参数与网络：`B_bias=R11 4.7K to GND`；`A_bias=R16 4.7K to +3.3V`；`termination=R14 120R/NC across A/B`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页下中 U2 A/B、R11/R16 与 R14 120Ω/NC

### RS485 浪涌保护

D3/D4/D5 三颗 SP4021-01FTG-C 配置在 RS485_B、RS485_A 与 GND 周围，形成线对地及线间保护网络。

- 参数与网络：`devices=D3, D4, D5 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页下中 D3/D4/D5 与 RS485_B/RS485_A/GND

## 射频

### 无线模组到 SMA 天线路径

M1 ANT pin18 经 R8 0Ω 串联到 E1 ANT_SMA-KWE，E1 的屏蔽端接 GND。

- 参数与网络：`module_pin=M1 pin18 ANT`；`series_element=R8 0R`；`connector=E1 ANT_SMA-KWE`；`shield=GND`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页中右 M1 ANT/R8/E1 ANT_SMA-KWE/GND

### 470/868/915 MHz 装配选项

原理图装配表将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915；当前产品名称和 SKU 对应 868 版本。

- 参数与网络：`R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`product_variant=868`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页右上装配表，R1 0Ω/470、R2 0Ω/868、R3 0Ω/915

## 调试与烧录

### 无线模组调试与复位测试点

JP1-JP5 依次引出 +3.3V、GND、SWC、SWD 和 RESET；SWC/SWD/RESET 分别连接 M1 SWCLK pin7、SWDIO pin8 和 RESET pin16。

- 参数与网络：`JP1=+3.3V`；`JP2=GND`；`JP3=SWC -> M1 SWCLK pin7`；`JP4=SWD -> M1 SWDIO pin8`；`JP5=RESET -> M1 RESET pin16`
- 证据：图 413dc7fd72ca / 第 1 页 / 第 1 页左中 JP1-JP5 与中部 M1 SWCLK/SWDIO/RESET

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU LoRaWAN868 系统架构 | `radio_module=M1 Ra-07/Ra-07H`；`radio_uart=UTXD/URXD`；`antenna=E1 ANT_SMA-KWE`；`rs485=U2 SP3485EN-L/TR`；`power_converter=U1 MP1584EN`；`host_connectors=P2 Atom-5Pin, P3 Atom-4Pin` |
| 电源 | 12V 输入到 +5V 降压 | `terminal=P1 12V+ / 12V-`；`input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`feedback=R4 51K, R5 10K`；`output=+5V` |
| 保护电路 | +VIN 输入保护与滤波 | `fuse=F1 1.5A/24V`；`shunt_diode=D2 SS54`；`input_capacitor=C2 10uF`；`enable_pin=U1 EN pin2 NC` |
| 电源 | Ra-07/Ra-07H 3.3V 电源 | `source=P2 pin1 3V3`；`module_pin=M1 VCC pin9`；`decoupling=C7 100nF, C8 10uF, C9 33pF` |
| 核心器件 | Ra-07/Ra-07H 外部无线模组 | `reference=M1`；`part_number=Ra-07/Ra-07H`；`uart=pin11 UTX, pin10 URX`；`debug=pin7 SWCLK, pin8 SWDIO`；`rf=pin18 ANT`；`reset=pin16 RESET`；`power=pin9 VCC` |
| 核心器件 | Ra-07/Ra-07H 内部通信芯片 | `schematic_module=Ra-07/Ra-07H`；`documented_chip=ASR6501`；`internal_schematic_available=false` |
| 射频 | 无线模组到 SMA 天线路径 | `module_pin=M1 pin18 ANT`；`series_element=R8 0R`；`connector=E1 ANT_SMA-KWE`；`shield=GND` |
| 射频 | 470/868/915 MHz 装配选项 | `R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`product_variant=868` |
| 接口 | Atom 与无线模组 UART 映射 | `host_tx=P2 pin2 G22 -> URXD -> R10 -> M1 URX pin10`；`host_rx=P2 pin3 G19 -> UTXD -> R9 -> M1 UTX pin11`；`series_resistors=R9/R10 22R` |
| 接口 | Atom 与 RS485 UART 映射 | `host_tx=P2 pin4 G23 -> TX`；`host_rx=P2 pin5 G33 -> RX`；`receiver_output=U2 RO via R12 1K to RX`；`rx_pullup=R13 4.7K to +3.3V`；`direction_control=TX via R15 1K and Q1 SS8050 Y1` |
| 接口 | P1 RS485 与电源端子 | `B=RS485_B`；`A=RS485_A`；`power_positive=+VIN / 12V+`；`power_negative=GND / 12V-` |
| 保护电路 | RS485 偏置与可选终端 | `B_bias=R11 4.7K to GND`；`A_bias=R16 4.7K to +3.3V`；`termination=R14 120R/NC across A/B` |
| 保护电路 | RS485 浪涌保护 | `devices=D3, D4, D5 SP4021-01FTG-C`；`protected_nets=RS485_A, RS485_B`；`reference=GND` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 HY-2.0_IIC`；`pin1=G21 IIC_SCL`；`pin2=G25 IIC_SDA`；`pin3=+5V`；`pin4=GND`；`host_connector=P3 Atom-4Pin` |
| 调试与烧录 | 无线模组调试与复位测试点 | `JP1=+3.3V`；`JP2=GND`；`JP3=SWC -> M1 SWCLK pin7`；`JP4=SWD -> M1 SWDIO pin8`；`JP5=RESET -> M1 RESET pin16` |
| 总线 | 产品正文中的无线串口与协议参数 | `documented_baud=115200bps`；`documented_protocol=LoRaWAN v1.0.1`；`documented_control=AT commands`；`schematic_uart=UTX/URX` |

## 待确认事项

- `component.radio-internal-chip`：产品正文将通信芯片写为 ASR6501，但当前原理图只给出外部模组料号 Ra-07/Ra-07H，没有展开模组内部芯片，因此无法从原理图独立确认内部芯片和版本。（证据：图 413dc7fd72ca / 第 1 页 / 第 1 页中部 M1 型号字段仅标 Ra-07/Ra-07H）
- `bus.documented-radio-firmware`：产品正文给出 UART 115200bps、LoRaWAN v1.0.1 和 AT 指令控制，但当前原理图只显示 UTX/URX 物理连接，未标注波特率、协议栈版本或指令集。（证据：图 413dc7fd72ca / 第 1 页 / 第 1 页 M1 UTX/URX 与 P2 UART 连接，图中无波特率或协议版本标注）
- `review.radio-internal-chip`：K063 当前装配的 Ra-07/Ra-07H 模组内部芯片是否确认为 ASR6501，具体模组版本是什么？；原因：原理图仅给出模组料号，未展开内部芯片，需要 BOM、模组丝印或官方资料确认。
- `review.radio-firmware-parameters`：当前出货固件是否确认为 UART 115200bps、LoRaWAN v1.0.1 并使用产品正文所述 AT 指令集？；原因：这些是固件参数，无法从当前原理图的 UTX/URX 连线验证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `413dc7fd72cad70452238a33b69a91afd73bdebe5f386c378c1ecc754444247f` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan868/atom_dtu_lorawan868_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_dtu_lorawan868.md`

源文档 SHA-256：`94a24f7a1a0c5e61da6b0bbd8ad9a526a6b5bbfaa8a8d6d500fe956c5747327a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
