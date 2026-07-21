# Unit Power 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Power |
| SKU | U125 |
| 产品 ID | `unit-power-2f15cdb873cb` |
| 源文档 | `zh_CN/unit/power.md` |

## 概述

Unit Power 由 J1（PWR3.5）接入直流电源，输入端配置 SD24 对地保护及 100uF/35V、100nF 去耦。ME3116AM6G（U1）配合 B5819W SL 肖特基二极管、10uH 电感和 52.3KΩ/10KΩ 反馈网络产生标注为 5V 的输出。J2（HY-2.0_IO）仅使用 VCC 与 GND 两脚输出电源，另有 1KΩ 串联红色 0603 LED 指示支路。

## 检索关键词

`Unit Power`、`U125`、`ME3116AM6G`、`U1`、`PWR3.5`、`J1`、`HY-2.0_IO`、`J2`、`DC-015`、`SD24`、`D2`、`B5819W SL`、`D1`、`L1`、`10uH`、`5V`、`6~24V`、`5V@1A`、`VIN`、`EN`、`BST`、`LX`、`FB`、`R1`、`52.3KΩ`、`R2`、`10KΩ`、`R3`、`100KΩ`、`C2`、`100uF 35V`、`C4`、`22uF`、`D3`、`红灯 0603`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME3116AM6G | 降压转换控制器，使用 VIN、EN、BST、LX、FB 与 GND 引脚构成 5V 电源 | 图 27cce1792c8d / 第 1 页 / 页面中央：U1 标注 ME3116AM6G，1~6 脚为 BST/GND/FB/EN/VIN/LX |
| J1 | PWR3.5 | 直流电源输入插座，输入正极网络接转换器，回路接 GND | 图 27cce1792c8d / 第 1 页 / 页面左侧：J1 PWR3.5 三脚符号，1/3 脚所在输入网络与 2 脚 GND |
| J2 | HY-2.0_IO | 5V/GND 输出连接器，1/2 脚未连接 | 图 27cce1792c8d / 第 1 页 / 页面右侧：J2 HY-2.0_IO，1/2 脚带未连接标记，3 脚 VCC 接 5V，4 脚 GND |
| D2 | SD24 | 输入电源网络到 GND 的瞬态/浪涌钳位保护器件 | 图 27cce1792c8d / 第 1 页 / 页面左侧：D2 标注 SD24，跨接 J1 输入正极网络与 GND |
| D1 | B5819W SL | ME3116AM6G 降压功率级的肖特基续流二极管 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：D1 标注 B5819W SL，连接 LX/BST 开关节点与 GND |
| L1 | 10uH | 降压转换器输出储能电感，连接 U1.LX 开关节点与 5V 输出 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：L1 标注 10uH，左接 U1.LX.6，右接 5V 输出节点 |
| R1 | 52.3KΩ | 5V 输出到 U1.FB 的上侧反馈电阻 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：R1 52.3KΩ 连接 5V 输出与 FB 节点 |
| R2 | 10KΩ | U1.FB 到 GND 的下侧反馈电阻 | 图 27cce1792c8d / 第 1 页 / 页面中央下方：R2 10KΩ 从 FB 节点连接 GND |
| R3 | 100KΩ | 从输入电源网络到 U1.EN 的使能上拉电阻 | 图 27cce1792c8d / 第 1 页 / 页面中央：R3 100KΩ 连接输入正极网络与 U1.EN.4 |
| C1 | 100nF | U1.BST 与 LX 开关节点之间的自举电容 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：C1 100nF 连接 U1.BST.1 与 LX/D1/L1 开关节点 |
| C2, C3 | 100uF 35V / 100nF | J1 输入电源的大容量与高频去耦电容 | 图 27cce1792c8d / 第 1 页 / 页面左中：C2 100uf 35V 与 C3 100nF 均跨接输入正极网络和 GND |
| C4 | 22uF | 5V 输出到 GND 的滤波电容 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：C4 22uF 从 5V 输出连接 GND |
| C5 | 100pF | 跨接 R1 的反馈前馈电容 | 图 27cce1792c8d / 第 1 页 / 页面中央偏右：C5 100pF 与 R1 并联在 FB 和 5V 输出之间 |
| D3 | 红灯 0603 | 5V 输出电源指示 LED | 图 27cce1792c8d / 第 1 页 / 页面右中：5V-R4(1KΩ)-D3(红灯 0603)-GND 串联支路 |

## 系统结构

### Unit Power

J1 输入直流电源经 U1 ME3116AM6G 降压电路转换为 5V，并由 J2 的 VCC/GND 两脚输出；D3 提供 5V 电源指示。

- 参数与网络：`input=J1 PWR3.5`；`converter=U1 ME3116AM6G`；`output_rail=5V`；`output=J2 HY-2.0_IO`；`indicator=D3 红灯 0603`
- 证据：图 27cce1792c8d / 第 1 页 / 全页：J1-D2/C2/C3-U1/D1/L1-R1/R2/C4-J2 与 D3 的完整电源路径

## 核心器件

### U1 ME3116AM6G

U1.VIN.5 接输入正极，EN.4 经 R3 接输入正极，GND.2 接地，LX.6 接开关节点，BST.1 经 C1 接开关节点，FB.3 接反馈分压节点。

- 参数与网络：`VIN=pin 5 input positive`；`EN=pin 4 via R3 100KΩ to input`；`GND=pin 2 GND`；`LX=pin 6 switching node`；`BST=pin 1 via C1 100nF to switching node`；`FB=pin 3 feedback node`
- 证据：图 27cce1792c8d / 第 1 页 / 页面中央：U1 六个引脚及 R3/C1/D1/L1/R1/R2 相邻网络

## 电源

### J1 输入电源

C2（100uF 35V）和 C3（100nF）均从输入正极网络连接至 GND。

- 参数与网络：`bulk_capacitor=C2 100uF 35V`；`high_frequency_capacitor=C3 100nF`；`rail=J1 input positive`
- 证据：图 27cce1792c8d / 第 1 页 / 页面左中：C2/C3 与输入正极、GND 的连线

### U1 EN

R3（100KΩ）把 U1.EN.4 连接到输入正极网络，原理图未显示外部开关或控制器控制 EN。

- 参数与网络：`enable_pin=U1.4 EN`；`pullup=R3 100KΩ to input positive`；`external_control=none shown`
- 证据：图 27cce1792c8d / 第 1 页 / 页面中央：输入正极-R3(100KΩ)-U1.EN.4 支路

### U1 LX 功率级

U1.LX.6 连接 D1（B5819W SL）与 L1（10uH）的开关节点，L1 另一端连接 5V 输出；C1（100nF）连接 BST.1 与该节点。

- 参数与网络：`switch_pin=U1.6 LX`；`catch_diode=D1 B5819W SL to GND`；`inductor=L1 10uH to 5V`；`bootstrap=C1 100nF between BST and LX node`
- 证据：图 27cce1792c8d / 第 1 页 / 页面中央偏右：U1.LX/BST、C1、D1、L1 与 5V/GND 网络

### 5V 输出

L1 后端网络标注为 5V，C4（22uF）从该输出连接到 GND。

- 参数与网络：`rail=5V`；`inductor=L1 10uH`；`output_capacitor=C4 22uF`；`load_connector=J2.3 VCC`
- 证据：图 27cce1792c8d / 第 1 页 / 页面中央偏右至右侧：L1 后端、5V 标签、C4 和 J2.3

### D3 指示支路

5V 经 R4（1KΩ）和 D3（红灯 0603）串联至 GND，构成输出电源指示支路。

- 参数与网络：`supply=5V`；`resistor=R4 1KΩ`；`indicator=D3 红灯 0603`；`return=GND`
- 证据：图 27cce1792c8d / 第 1 页 / 页面右中：5V-R4(1KΩ)-D3(红灯 0603)-GND 支路

### 电池与充电路径

本页未显示电池连接器、充电 IC、负载开关或电源监测 IC。

- 参数与网络：`battery=none shown`；`charger=none shown`；`load_switch=none shown`；`monitor=none shown`
- 证据：图 27cce1792c8d / 第 1 页 / 全页：唯一电源路径为 J1 输入、U1 降压与 J2 输出，未见电池/充电/监测器件

## 接口

### J1

J1 标为 PWR3.5；1 脚和 3 脚接入同一输入正极网络，2 脚连接 GND。

- 参数与网络：`connector=PWR3.5`；`pin_1=DC input positive`；`pin_2=GND`；`pin_3=DC input positive / switched contact tied to input net`
- 证据：图 27cce1792c8d / 第 1 页 / 页面左侧：J1.1/J1.3 与输入正极节点连线，J1.2 向下连接 GND

### J2

J2.1 与 J2.2 未连接，J2.3 VCC 接 5V，J2.4 GND 接地。

- 参数与网络：`connector=HY-2.0_IO`；`pin_1=NC`；`pin_2=NC`；`pin_3=VCC / 5V`；`pin_4=GND`；`power_direction=output from board`
- 证据：图 27cce1792c8d / 第 1 页 / 页面右侧：J2.1/J2.2 的未连接标记、J2.3 的 5V 网络与 J2.4 GND

## 保护电路

### J1 输入

D2（SD24）跨接输入正极与 GND，构成输入侧对地钳位保护。

- 参数与网络：`device=D2 SD24`；`protected_net=J1 input positive`；`return=GND`；`topology=shunt clamp`
- 证据：图 27cce1792c8d / 第 1 页 / 页面左侧：输入正极-D2(SD24)-GND 垂直支路

## 模拟电路

### U1 FB

R1（52.3KΩ）从 5V 输出连接 FB，R2（10KΩ）从 FB 连接 GND，C5（100pF）与 R1 并联。

- 参数与网络：`upper_resistor=R1 52.3KΩ`；`lower_resistor=R2 10KΩ`；`feedforward_capacitor=C5 100pF`；`feedback_pin=U1.3 FB`；`output_net=5V`
- 证据：图 27cce1792c8d / 第 1 页 / 页面中央偏右：5V-R1-FB-R2-GND 反馈分压及并联 C5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Power | `input=J1 PWR3.5`；`converter=U1 ME3116AM6G`；`output_rail=5V`；`output=J2 HY-2.0_IO`；`indicator=D3 红灯 0603` |
| 接口 | J1 | `connector=PWR3.5`；`pin_1=DC input positive`；`pin_2=GND`；`pin_3=DC input positive / switched contact tied to input net` |
| 接口 | J2 | `connector=HY-2.0_IO`；`pin_1=NC`；`pin_2=NC`；`pin_3=VCC / 5V`；`pin_4=GND`；`power_direction=output from board` |
| 保护电路 | J1 输入 | `device=D2 SD24`；`protected_net=J1 input positive`；`return=GND`；`topology=shunt clamp` |
| 电源 | J1 输入电源 | `bulk_capacitor=C2 100uF 35V`；`high_frequency_capacitor=C3 100nF`；`rail=J1 input positive` |
| 核心器件 | U1 ME3116AM6G | `VIN=pin 5 input positive`；`EN=pin 4 via R3 100KΩ to input`；`GND=pin 2 GND`；`LX=pin 6 switching node`；`BST=pin 1 via C1 100nF to switching node`；`FB=pin 3 feedback node` |
| 电源 | U1 EN | `enable_pin=U1.4 EN`；`pullup=R3 100KΩ to input positive`；`external_control=none shown` |
| 电源 | U1 LX 功率级 | `switch_pin=U1.6 LX`；`catch_diode=D1 B5819W SL to GND`；`inductor=L1 10uH to 5V`；`bootstrap=C1 100nF between BST and LX node` |
| 模拟电路 | U1 FB | `upper_resistor=R1 52.3KΩ`；`lower_resistor=R2 10KΩ`；`feedforward_capacitor=C5 100pF`；`feedback_pin=U1.3 FB`；`output_net=5V` |
| 电源 | 5V 输出 | `rail=5V`；`inductor=L1 10uH`；`output_capacitor=C4 22uF`；`load_connector=J2.3 VCC` |
| 电源 | D3 指示支路 | `supply=5V`；`resistor=R4 1KΩ`；`indicator=D3 红灯 0603`；`return=GND` |
| 电源 | 电池与充电路径 | `battery=none shown`；`charger=none shown`；`load_switch=none shown`；`monitor=none shown` |
| 接口 | J1 输入规格 | `documented_connector=DC-015`；`schematic_connector=PWR3.5`；`documented_input_range=DC 6~24V`；`schematic_input_range=未标注` |
| 电源 | 5V 输出额定能力 | `confirmed_voltage_label=5V`；`documented_tolerance=±5%`；`documented_current=1A`；`schematic_current_rating=未标注` |

## 待确认事项

- `interface.input-rating-unconfirmed`：产品正文称 J1 为 DC-015 且支持 DC 6~24V 输入；原理图仅标 PWR3.5，并未标出 DC-015 或 6~24V 范围。（证据：图 27cce1792c8d / 第 1 页 / 页面左侧：J1 仅标 PWR3.5，输入网络无电压范围文字）
- `power.output-rating-unconfirmed`：原理图确认输出网络名为 5V，但没有标注产品正文所列的 ±5% 精度和 1A 额定电流。（证据：图 27cce1792c8d / 第 1 页 / 页面中央偏右至 J2：输出仅标 5V，未见 1A 或 ±5% 标注）
- `review.input-connector-and-range`：J1 的量产物料是否为 DC-015，且整机保证 DC 6~24V 输入范围？；原因：原理图只标 PWR3.5 并显示 35V 输入电容，没有连接器 BOM 型号和明确输入额定范围；需查 BOM、ME3116 数据手册或实物。
- `review.output-current-tolerance`：该电路在规定输入与热条件下是否保证 5V（±5%）@1A 输出？；原因：原理图给出 5V 网络与元件值，但没有电流额定、效率、热限制或容差说明，需以器件规格、BOM 与负载测试确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `27cce1792c8d64e880bb778cb53c87bdc65beb92989fec2dfd70efc7c70a2162` | `https://static-cdn.m5stack.com/resource/docs/products/unit/power/power_sch_01.webp` |

---

源文档：`zh_CN/unit/power.md`

源文档 SHA-256：`1945a286892a827c89ff5ccb202b62ed02e493759cc67368ae8df7e01963bd8b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
