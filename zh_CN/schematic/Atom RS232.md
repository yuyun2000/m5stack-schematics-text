# Atom RS232 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom RS232 |
| SKU | K046 |
| 产品 ID | `atom-rs232-86a93d2cd17b` |
| 源文档 | `zh_CN/atom/atomic232.md` |

## 概述

Atom RS232 由 U1 MAX3232ESE 电平转换电路和 U2 AOZ1282CI 降压电路组成。外部 J1 的 +12V 经 AOZ1282CI、D4 B5819W SL 和 L1 4.7uH 转换为 +5VIN，为 MAX3232ESE 和 Atom P2 供电。Atom P1 的 TX 经 R2 100Ω 到 TXD，再由 MAX3232ESE 第一发送通道转换为 RS232_R 并送到 J1 B；J1 A 的 RS232_T 经第一接收通道形成 RXD，再经 R1 100Ω返回 P1 RX。MAX3232ESE 第二路收发器未使用，J1 还引出 +12V 与 GND。

## 检索关键词

`Atom RS232`、`K046`、`MAX3232ESE`、`AOZ1282CI`、`RS232_R`、`RS232_T`、`TXD`、`RXD`、`TX`、`RX`、`T1IN`、`T1OUT`、`R1IN`、`R1OUT`、`+12V`、`+5VIN`、`+3.3V`、`B5819W SL`、`L1 4.7uH`、`HDR_4P_3.96`、`P1 Header 5`、`P2 Header 4`、`470nF charge pump`、`full duplex`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX3232ESE | 在 TXD/RXD TTL 网络与 RS232_R/RS232_T 外部电平之间进行全双工转换 | 图 786621d92c03 / 第 1 页 / 页面左上 U1 MAX3232ESE，C1±/C2±、T1/T2、R1/R2、VCC/VDD/VEE/GND 引脚 |
| C1/C7/C9/C10 | 470nF | MAX3232ESE 电荷泵电容网络 | 图 786621d92c03 / 第 1 页 / U1 周围 C7 跨 C1+/C1-、C9 跨 C2+/C2-、C1 接 VDD/+5VIN、C10 接 VEE/GND |
| J1 | HDR_4P_3.96 | 引出 RS232_R、RS232_T、+12V 和 GND 的四针外部端子 | 图 786621d92c03 / 第 1 页 / 页面右上 J1 HDR_4P_3.96，B/A/12V+/12V- |
| U2 | AOZ1282CI | 将 J1 +12V 降压为 +5VIN 的开关稳压器 | 图 786621d92c03 / 第 1 页 / 页面左下 U2 AOZ1282CI，VIN/EN/GND/BST/LX/FB 六脚与外围 |
| D4/L1 | B5819W SL / 4.7uH | AOZ1282CI 降压转换的肖特基续流二极管和输出电感 | 图 786621d92c03 / 第 1 页 / U2 右侧 LX 开关节点、D4 B5819W SL 与 L1 4.7uH |
| P1 | Header 5 | Atom 五针接口，引出 +3.3V、RX、TX，4/5 脚未连接 | 图 786621d92c03 / 第 1 页 / 页面右中 P1 Header 5，1 +3.3V、2 RX、3 TX、4/5 no-connect |
| P2 | Header 4 | Atom 四针供电接口，引出 +5VIN 和 GND，1/2 脚未连接 | 图 786621d92c03 / 第 1 页 / 页面右中 P2 Header 4，1/2 no-connect、3 +5VIN、4 GND |
| R1/R2 | 100Ω | 分别串联在 P1 RX-RXD 和 P1 TX-TXD 之间的 TTL 侧电阻 | 图 786621d92c03 / 第 1 页 / 页面右中 P1 RX/TX 右侧 R1/R2 100Ω 到 RXD/TXD |

## 系统结构

### 全双工 RS232 路径

P1 TX 经 R2 到 TXD，再由 MAX3232ESE 第一发送通道输出 RS232_R 到 J1 B；J1 A 的 RS232_T 经第一接收通道变为 RXD，再经 R1 返回 P1 RX。

- 参数与网络：`transmit=P1 TX -> R2 -> TXD -> U1 T1IN/T1OUT -> RS232_R -> J1 B`；`receive=J1 A -> RS232_T -> U1 R1IN/R1OUT -> RXD -> R1 -> P1 RX`
- 证据：图 786621d92c03 / 第 1 页 / 整页 P1/R1/R2、U1 第一通道与 J1 B/A 信号链

## 核心器件

### MAX3232ESE 第二通道

U1 T2IN 10 脚、T2OUT 7 脚、R2IN 8 脚和 R2OUT 9 脚均标为未连接。

- 参数与网络：`t2in=pin 10 not connected`；`t2out=pin 7 not connected`；`r2in=pin 8 not connected`；`r2out=pin 9 not connected`
- 证据：图 786621d92c03 / 第 1 页 / U1 第二通道四个引脚旁的 no-connect 标记

## 电源

### MAX3232ESE 供电

U1 VCC 16 脚连接 +5VIN，GND 15 脚接 GND，C8 470nF 从 +5VIN 接 GND。

- 参数与网络：`vcc=pin 16 -> +5VIN`；`ground=pin 15 -> GND`；`decoupling=C8 470nF`
- 证据：图 786621d92c03 / 第 1 页 / U1 VCC/GND 与 C8

### MAX3232ESE 电荷泵

C7 470nF 跨接 U1 C1+ 1 脚与 C1- 3 脚，C9 470nF 跨接 C2+ 4 脚与 C2- 5 脚，C1 470nF 连接 VDD 2 脚与 +5VIN，C10 470nF 从 VEE 6 脚接 GND。

- 参数与网络：`c1_pair=C7 470nF between pins 1 and 3`；`c2_pair=C9 470nF between pins 4 and 5`；`positive_pump=C1 470nF between VDD pin 2 and +5VIN`；`negative_pump=C10 470nF between VEE pin 6 and GND`
- 证据：图 786621d92c03 / 第 1 页 / U1 周围 C1/C7/C9/C10 四只 470nF

### AOZ1282CI 输入与使能

U2 VIN 5 脚连接 +12V，EN 4 脚经 R7 100KΩ连接 +12V，GND 2 脚接地；C3/C4 从 +12V 接 GND，C4 标注 10uF (106) 10% 35V。

- 参数与网络：`vin=pin 5 -> +12V`；`enable=pin 4 -> R7 100KΩ -> +12V`；`ground=pin 2 -> GND`；`input_capacitors=C3/C4 from +12V to GND; C4 10uF (106) 10% 35V`
- 证据：图 786621d92c03 / 第 1 页 / 页面左下 +12V、C3/C4、R7 与 U2 VIN/EN/GND；C3 标值左缘被页面裁切

### AOZ1282CI +5VIN 输出

U2 LX 6 脚经 L1 4.7uH 形成 +5VIN，D4 B5819W SL 从开关节点接 GND，C2 100nF 跨 BST 1 脚与开关节点，C5 10uF 与 C6 100nF 从 +5VIN 接 GND。

- 参数与网络：`switch=LX pin 6`；`inductor=L1 4.7uH`；`output=+5VIN`；`catch_diode=D4 B5819W SL`；`bootstrap=C2 100nF`；`output_capacitors=C5 10uF; C6 100nF`
- 证据：图 786621d92c03 / 第 1 页 / U2 右侧 BST/LX、C2/D4/L1/+5VIN/C5/C6

### AOZ1282CI 反馈

U2 FB 3 脚连接 R8 51KΩ与 R9 10KΩ的 +5VIN 对地分压节点。

- 参数与网络：`upper_resistor=R8 51KΩ to +5VIN`；`lower_resistor=R9 10KΩ to GND`；`feedback_pin=3`
- 证据：图 786621d92c03 / 第 1 页 / U2 FB 3 脚与 R8/R9 分压

## 接口

### J1 RS232/电源端子

J1 HDR_4P_3.96 从上到下标注 B、A、12V+、12V-；B 接 RS232_R，A 接 RS232_T，12V+ 接 +12V，12V- 接 GND。

- 参数与网络：`b=RS232_R`；`a=RS232_T`；`12v_plus=+12V`；`12v_minus=GND`
- 证据：图 786621d92c03 / 第 1 页 / 页面右上 J1 B/A/12V+/12V- 与四条网络

### P1 Atom 信号接口

P1 Header 5 的 1 脚接 +3.3V，2 脚接 RX，3 脚接 TX，4/5 脚标为未连接。

- 参数与网络：`pin1=+3.3V`；`pin2=RX`；`pin3=TX`；`pin4=not connected`；`pin5=not connected`
- 证据：图 786621d92c03 / 第 1 页 / 页面右中 P1 Header 5 与 +3.3V/RX/TX/no-connect

### P2 Atom 电源接口

P2 Header 4 的 1/2 脚标为未连接，3 脚接 +5VIN，4 脚接 GND。

- 参数与网络：`pin1=not connected`；`pin2=not connected`；`pin3=+5VIN`；`pin4=GND`
- 证据：图 786621d92c03 / 第 1 页 / 页面右中 P2 Header 4 与 no-connect/+5VIN/GND

## 总线

### TTL 到 RS232 发送路径

P1 3 脚 TX 经 R2 100Ω形成 TXD，TXD 进入 U1 T1IN 11 脚，U1 T1OUT 14 脚输出 RS232_R。

- 参数与网络：`atom_pin=P1 pin 3 TX`；`series_resistor=R2 100Ω`；`ttl_net=TXD`；`driver_input=U1 T1IN pin 11`；`rs232_output=U1 T1OUT pin 14 -> RS232_R`
- 证据：图 786621d92c03 / 第 1 页 / P1 TX-R2-TXD 与 U1 T1IN/T1OUT-RS232_R

### RS232 到 TTL 接收路径

RS232_T 进入 U1 R1IN 13 脚，U1 R1OUT 12 脚输出 RXD，RXD 经 R1 100Ω连接 P1 2 脚 RX。

- 参数与网络：`rs232_input=RS232_T -> U1 R1IN pin 13`；`receiver_output=U1 R1OUT pin 12 -> RXD`；`series_resistor=R1 100Ω`；`atom_pin=P1 pin 2 RX`
- 证据：图 786621d92c03 / 第 1 页 / U1 RS232_T/R1IN/R1OUT/RXD 与 R1-P1 RX

## 保护电路

### 外部 RS232 与 12V 防护可见性

当前页面没有在 J1 RS232_R/RS232_T 或 +12V 入口显示 TVS、保险丝、反接保护或共模滤波器件。

- 参数与网络：`rs232_tvs_shown=false`；`input_fuse_shown=false`；`reverse_polarity_protection_shown=false`；`common_mode_filter_shown=false`
- 证据：图 786621d92c03 / 第 1 页 / J1 四条网络直接进入 U1/U2 相关网络，未见输入防护器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 全双工 RS232 路径 | `transmit=P1 TX -> R2 -> TXD -> U1 T1IN/T1OUT -> RS232_R -> J1 B`；`receive=J1 A -> RS232_T -> U1 R1IN/R1OUT -> RXD -> R1 -> P1 RX` |
| 总线 | TTL 到 RS232 发送路径 | `atom_pin=P1 pin 3 TX`；`series_resistor=R2 100Ω`；`ttl_net=TXD`；`driver_input=U1 T1IN pin 11`；`rs232_output=U1 T1OUT pin 14 -> RS232_R` |
| 总线 | RS232 到 TTL 接收路径 | `rs232_input=RS232_T -> U1 R1IN pin 13`；`receiver_output=U1 R1OUT pin 12 -> RXD`；`series_resistor=R1 100Ω`；`atom_pin=P1 pin 2 RX` |
| 核心器件 | MAX3232ESE 第二通道 | `t2in=pin 10 not connected`；`t2out=pin 7 not connected`；`r2in=pin 8 not connected`；`r2out=pin 9 not connected` |
| 电源 | MAX3232ESE 供电 | `vcc=pin 16 -> +5VIN`；`ground=pin 15 -> GND`；`decoupling=C8 470nF` |
| 电源 | MAX3232ESE 电荷泵 | `c1_pair=C7 470nF between pins 1 and 3`；`c2_pair=C9 470nF between pins 4 and 5`；`positive_pump=C1 470nF between VDD pin 2 and +5VIN`；`negative_pump=C10 470nF between VEE pin 6 and GND` |
| 接口 | J1 RS232/电源端子 | `b=RS232_R`；`a=RS232_T`；`12v_plus=+12V`；`12v_minus=GND` |
| 接口 | P1 Atom 信号接口 | `pin1=+3.3V`；`pin2=RX`；`pin3=TX`；`pin4=not connected`；`pin5=not connected` |
| 接口 | P2 Atom 电源接口 | `pin1=not connected`；`pin2=not connected`；`pin3=+5VIN`；`pin4=GND` |
| 电源 | AOZ1282CI 输入与使能 | `vin=pin 5 -> +12V`；`enable=pin 4 -> R7 100KΩ -> +12V`；`ground=pin 2 -> GND`；`input_capacitors=C3/C4 from +12V to GND; C4 10uF (106) 10% 35V` |
| 电源 | AOZ1282CI +5VIN 输出 | `switch=LX pin 6`；`inductor=L1 4.7uH`；`output=+5VIN`；`catch_diode=D4 B5819W SL`；`bootstrap=C2 100nF`；`output_capacitors=C5 10uF; C6 100nF` |
| 电源 | AOZ1282CI 反馈 | `upper_resistor=R8 51KΩ to +5VIN`；`lower_resistor=R9 10KΩ to GND`；`feedback_pin=3` |
| 保护电路 | 外部 RS232 与 12V 防护可见性 | `rs232_tvs_shown=false`；`input_fuse_shown=false`；`reverse_polarity_protection_shown=false`；`common_mode_filter_shown=false` |

## 待确认事项

- `review.level_shifter_part_conflict`：K046 当前硬件实际装配的电平转换芯片是产品正文所述 MAX232，还是原理图 U1 标注的 MAX3232ESE？；原因：产品正文与原理图型号不一致，最终型号必须用当前 BOM、PCB 版本或实装器件确认。
- `review.terminal_labels_and_protection`：请确认 J1 的 B/A 丝印分别对应设备发送/接收方向，并确认量产板是否另有 RS232/12V 瞬态与反接保护。；原因：B/A 不是本页给出的方向名称，且当前页面未显示外部接口防护。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `786621d92c0338c26cd564e7b3cffb68da2c0e35951a3da7ca4dbd379d798aab` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomic232/atomic232_sch_01.webp` |

---

源文档：`zh_CN/atom/atomic232.md`

源文档 SHA-256：`be1269a22d3564f5b328de3999ef49b6d4349e5d384882ed4f42c408405bfb2e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
