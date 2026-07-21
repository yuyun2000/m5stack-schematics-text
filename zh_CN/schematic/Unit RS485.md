# Unit RS485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RS485 |
| SKU | U034 |
| 产品 ID | `unit-rs485-ba5717526e3a` |
| 源文档 | `zh_CN/unit/rs485.md` |

## 概述

Unit RS485 使用 SP485EEN-L/TR（U1）实现 UART RX/TX 与半双工 RS-485 A/B 的转换，并由 Q1（SS8050 Y1）和 R3/R4 自动控制 /RE 与 DE。J1 四针端子引出 RS485_B、RS485_A、12V+、12V-，A/B 各带 4.7KΩ 偏置但没有可见的 120Ω 终端电阻。+12V 经未标型号的 U2 降压级生成 +5V，为收发器和 J2 UART 接口供电。

## 检索关键词

`Unit RS485`、`U034`、`SP485EEN-L/TR`、`SP485EEN`、`MAX485`、`U1`、`SS8050 Y1`、`Q1`、`RS485_A`、`RS485_B`、`A`、`B`、`RX`、`TX`、`RO`、`RE`、`DE`、`DI`、`J1`、`HDR_4P_3.96`、`J2`、`UART_Socket_4P`、`+12V`、`12V+`、`12V-`、`+5V`、`R1`、`R5`、`4.7KΩ`、`R2`、`R4`、`1KΩ`、`L1`、`22uH`、`B5819W SL`、`D4`、`automatic direction`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SP485EEN-L/TR | UART/TTL 到半双工 RS-485 的收发器 | 图 adc94e7b95ad / 第 1 页 / 页面上中：U1 标注 SP485EEN-L/TR，1~8 脚为 RO、/RE、DE、DI、GND、A、B、VCC |
| Q1 | SS8050 Y1 | 由 TX 驱动的 /RE 与 DE 自动方向控制晶体管 | 图 adc94e7b95ad / 第 1 页 / 页面上左：Q1 SS8050 Y1，基极经 R4 接 TX，集电极接 U1./RE/DE，发射极接 GND |
| U2 | 未标注 | 将 +12V 降压为 +5V 的六脚开关稳压器，原理图未标型号 | 图 adc94e7b95ad / 第 1 页 / 页面左下：U2 六脚 VIN/EN/GND/BST/LX/FB 符号，无可见型号文字 |
| J1 | HDR_4P_3.96 | RS-485 A/B 与 12V+/12V- 电源端子 | 图 adc94e7b95ad / 第 1 页 / 页面右上：J1 HDR_4P_3.96，1~4 脚标注 B、A、12V+、12V- |
| J2 | UART_Socket_4P | RX、TX、+5V、GND UART/Grove 接口 | 图 adc94e7b95ad / 第 1 页 / 页面右中：J2 UART_Socket_4P，1~4 脚为 RX、TX、VCC、GND |
| R1, R5 | 4.7KΩ | RS485_B 到 GND 与 RS485_A 到 +5V 的总线偏置电阻 | 图 adc94e7b95ad / 第 1 页 / 页面上中偏右：R1 4.7KΩ 从 RS485_B 接 GND；R5 4.7KΩ 从 RS485_A 接 +5V |
| R2 | 1KΩ | U1.RO 到 RX 的串联电阻 | 图 adc94e7b95ad / 第 1 页 / 页面上中：U1.RO.1 经 R2 1KΩ 连接 RX |
| R3 | 4.7KΩ | U1./RE/DE 与 Q1 集电极控制节点到 +5V 的上拉 | 图 adc94e7b95ad / 第 1 页 / 页面上左：R3 4.7KΩ 从 +5V 接 Q1 集电极和 U1./RE/DE 节点 |
| R4 | 1KΩ | TX 到 Q1 基极的串联电阻 | 图 adc94e7b95ad / 第 1 页 / 页面上左：TX-R4(1KΩ)-Q1 基极 |
| L1 | 22uH | U2 降压输出储能电感，连接 LX 与 +5V | 图 adc94e7b95ad / 第 1 页 / 页面下中：L1 22uH 位于 U2.LX 开关节点与 +5V 输出之间 |
| D4 | B5819W SL | U2 降压开关节点到 GND 的肖特基续流二极管 | 图 adc94e7b95ad / 第 1 页 / 页面下中：D4 B5819W SL 连接 U2.LX/L1 开关节点与 GND |
| R7, R8 | 51KΩ / 10KΩ | +5V 输出到 U2.FB 的反馈分压电阻 | 图 adc94e7b95ad / 第 1 页 / 页面下中：R7 51KΩ 从 +5V 接 FB，R8 10KΩ 从 FB 接 GND |
| C1, C2 | 100nF | U1 与 J2 的 +5V 去耦电容 | 图 adc94e7b95ad / 第 1 页 / 页面上中 C1 与右中 C2，均跨接 +5V/GND |

## 系统结构

### Unit RS485

J2 的 RX/TX 通过 U1 SP485EEN-L/TR 和 Q1 自动方向电路转换为 J1 的 RS485_A/RS485_B；J1 的 +12V 经 U2 降压生成 +5V。

- 参数与网络：`uart=J2 RX/TX`；`transceiver=U1 SP485EEN-L/TR`；`direction_control=Q1 SS8050 Y1`；`rs485=J1 RS485_A/RS485_B`；`power=+12V -> U2 -> +5V`
- 证据：图 adc94e7b95ad / 第 1 页 / 全页：J2-RX/TX-U1/Q1-RS485_A/B-J1 及 J1 +12V-U2-+5V

## 电源

### +12V

J1.3 的 12V+ 网络直接连接 U2.VIN.5，并经 R6（100KΩ）连接 U2.EN.4；J1.4 12V- 接 GND。

- 参数与网络：`input_positive=J1.3 12V+ / +12V`；`input_return=J1.4 12V- / GND`；`converter_input=U2.5 VIN`；`enable=U2.4 EN via R6 100KΩ to +12V`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面右上 J1 +12V/GND 与左下 +12V-U2.VIN/R6-EN 同名网络

### U2 降压级

U2 与 D4（B5819W SL）、L1（22uH）构成 +12V 到 +5V 的降压路径；C4（4.7uF）位于输入端，C5（10uF）位于输出端。

- 参数与网络：`input=+12V`；`output=+5V`；`switch_pin=U2.6 LX`；`diode=D4 B5819W SL`；`inductor=L1 22uH`；`input_cap=C4 4.7uF`；`output_cap=C5 10uF`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面左下至下中：+12V、U2、D4、L1、+5V、C4/C5

### +5V

U2 生成的 +5V 供给 U1.VCC.8、J2.VCC.3、R3/R5 上拉，并由 C1/C2（100nF）对地去耦。

- 参数与网络：`source=U2/L1 output`；`loads=U1.8, J2.3, R3, R5`；`decoupling=C1 100nF, C2 100nF`
- 证据：图 adc94e7b95ad / 第 1 页 / 全页 +5V 同名网络：U2 输出、U1、J2、R3/R5、C1/C2

## 接口

### J1

J1.1 B 接 RS485_B，J1.2 A 接 RS485_A，J1.3 12V+ 接 +12V，J1.4 12V- 接 GND。

- 参数与网络：`connector=HDR_4P_3.96`；`pin_1=B / RS485_B`；`pin_2=A / RS485_A`；`pin_3=12V+ / +12V`；`pin_4=12V- / GND`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面右上：J1.1~J1.4 与 RS485_B、RS485_A、+12V、GND 网络

### J2

J2.1 接 RX，J2.2 接 TX，J2.3 VCC 接 +5V，J2.4 GND 接地。

- 参数与网络：`connector=UART_Socket_4P`；`pin_1=RX`；`pin_2=TX`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_direction=RX output from unit; TX input to unit`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面右中：J2.1~J2.4 的 RX/TX/+5V/GND 标注

## 总线

### U1 SP485EEN-L/TR

U1.RO.1 经 R2 接 RX，/RE.2 与 DE.3 短接为方向控制节点，DI.4 接 GND，GND.5 接地，A.6 接 RS485_A，B.7 接 RS485_B，VCC.8 接 +5V。

- 参数与网络：`RO=pin 1 via R2 1KΩ to RX`；`nRE_DE=pins 2/3 tied`；`DI=pin 4 GND`；`GND=pin 5`；`A=pin 6 RS485_A`；`B=pin 7 RS485_B`；`VCC=pin 8 +5V`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面上中：U1 的 1~8 脚及 R2/RX、Q1 方向节点、GND、RS485_A/B、+5V 连线

### TX 与 U1 /RE/DE

TX 经 R4（1KΩ）驱动 Q1 基极；Q1 发射极接 GND，集电极连接 U1./RE.2 与 DE.3，并由 R3（4.7KΩ）上拉至 +5V。

- 参数与网络：`tx_drive=TX -> R4 1KΩ -> Q1 base`；`transistor=Q1 SS8050 Y1`；`direction_node=Q1 collector -> U1 pins 2/3`；`pullup=R3 4.7KΩ to +5V`；`emitter=GND`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面上左至上中：TX/R4/Q1/R3 与 U1./RE/DE 连线

### RS485_A 与 RS485_B

RS485_B 经 R1（4.7KΩ）连接 GND，RS485_A 经 R5（4.7KΩ）连接 +5V。

- 参数与网络：`B_bias=R1 4.7KΩ to GND`；`A_bias=R5 4.7KΩ to +5V`；`nets=RS485_B, RS485_A`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面上中偏右：RS485_B-R1-GND 与 RS485_A-R5-+5V

## 保护电路

### RS485_A/B 外部总线

本页未显示跨接 A/B 的 120Ω 终端电阻，也未显示 A/B 到地或电源的 TVS/ESD 器件。

- 参数与网络：`termination=none shown`；`tvs_esd=none shown`；`visible_bias=R1/R5 4.7KΩ only`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面上中至 J1：RS485_A/B 完整路径仅包含 U1、R1/R5 和端子

### +12V 输入

本页未显示 +12V 输入的保险丝、反接二极管、TVS 或浪涌限流器件。

- 参数与网络：`fuse=none shown`；`reverse_polarity=none shown`；`tvs=none shown`；`inrush_limit=none shown`
- 证据：图 adc94e7b95ad / 第 1 页 / J1.3 +12V 至 U2.VIN 的完整路径，仅有 C4 与 R6

## 模拟电路

### U2 FB

R7（51KΩ）从 +5V 输出连接 U2.FB.3，R8（10KΩ）从 FB 连接 GND。

- 参数与网络：`upper_resistor=R7 51KΩ`；`lower_resistor=R8 10KΩ`；`feedback_pin=U2.3 FB`；`output=+5V`
- 证据：图 adc94e7b95ad / 第 1 页 / 页面下中：+5V-R7-FB-R8-GND 分压网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RS485 | `uart=J2 RX/TX`；`transceiver=U1 SP485EEN-L/TR`；`direction_control=Q1 SS8050 Y1`；`rs485=J1 RS485_A/RS485_B`；`power=+12V -> U2 -> +5V` |
| 接口 | J1 | `connector=HDR_4P_3.96`；`pin_1=B / RS485_B`；`pin_2=A / RS485_A`；`pin_3=12V+ / +12V`；`pin_4=12V- / GND` |
| 接口 | J2 | `connector=UART_Socket_4P`；`pin_1=RX`；`pin_2=TX`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_direction=RX output from unit; TX input to unit` |
| 总线 | U1 SP485EEN-L/TR | `RO=pin 1 via R2 1KΩ to RX`；`nRE_DE=pins 2/3 tied`；`DI=pin 4 GND`；`GND=pin 5`；`A=pin 6 RS485_A`；`B=pin 7 RS485_B`；`VCC=pin 8 +5V` |
| 总线 | TX 与 U1 /RE/DE | `tx_drive=TX -> R4 1KΩ -> Q1 base`；`transistor=Q1 SS8050 Y1`；`direction_node=Q1 collector -> U1 pins 2/3`；`pullup=R3 4.7KΩ to +5V`；`emitter=GND` |
| 总线 | RS485_A 与 RS485_B | `B_bias=R1 4.7KΩ to GND`；`A_bias=R5 4.7KΩ to +5V`；`nets=RS485_B, RS485_A` |
| 保护电路 | RS485_A/B 外部总线 | `termination=none shown`；`tvs_esd=none shown`；`visible_bias=R1/R5 4.7KΩ only` |
| 电源 | +12V | `input_positive=J1.3 12V+ / +12V`；`input_return=J1.4 12V- / GND`；`converter_input=U2.5 VIN`；`enable=U2.4 EN via R6 100KΩ to +12V` |
| 电源 | U2 降压级 | `input=+12V`；`output=+5V`；`switch_pin=U2.6 LX`；`diode=D4 B5819W SL`；`inductor=L1 22uH`；`input_cap=C4 4.7uF`；`output_cap=C5 10uF` |
| 模拟电路 | U2 FB | `upper_resistor=R7 51KΩ`；`lower_resistor=R8 10KΩ`；`feedback_pin=U2.3 FB`；`output=+5V` |
| 电源 | +5V | `source=U2/L1 output`；`loads=U1.8, J2.3, R3, R5`；`decoupling=C1 100nF, C2 100nF` |
| 核心器件 | U2 降压转换器型号 | `reference=U2`；`visible_pins=VIN, EN, GND, BST, LX, FB`；`input=+12V`；`output=+5V`；`part_number=未标注` |
| 保护电路 | +12V 输入 | `fuse=none shown`；`reverse_polarity=none shown`；`tvs=none shown`；`inrush_limit=none shown` |

## 待确认事项

- `component.u2-model-unconfirmed`：原理图显示 U2 的 VIN、EN、GND、BST、LX、FB 六脚及完整外围，但没有标注器件型号。（证据：图 adc94e7b95ad / 第 1 页 / 页面左下：U2 符号与引脚，器件下方无型号文字）
- `review.u2-part-number`：U2 的量产器件型号是什么，其输入范围、输出电流和保护能力为何？；原因：原理图没有 U2 型号，无法仅从外围连接确定具体 IC 或额定边界；需查 BOM、丝印或原始设计文件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `adc94e7b95ad3654e202ceb8758472441500e49b13069a97899f9f96e4500fd9` | `https://static-cdn.m5stack.com/resource/docs/products/unit/rs485/rs485_sch_01.webp` |

---

源文档：`zh_CN/unit/rs485.md`

源文档 SHA-256：`310f22141d6a8dca4f747996313bc672d261b218e31235fbbcd189387184d9c2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
