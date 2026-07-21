# Unit Relay 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Relay |
| SKU | U023 |
| 产品 ID | `unit-relay-b14b02f11c3d` |
| 源文档 | `zh_CN/unit/relay.md` |

## 概述

Unit Relay 通过 J1 的 Din 输入控制 Q1（SS8050 Y1）低边开关，使 +5V 供电的 K1 SPDT 继电器线圈吸合或释放。R1 为 1KΩ 基极串联电阻，R2 为 10KΩ 控制输入下拉，D1（1N4148WS T4）跨接线圈提供续流路径。J2 将继电器触点引出为 COM、NO、NC；原理图没有直接给出继电器具体料号、负载额定值或状态指示灯。

## 检索关键词

`Unit Relay`、`U023`、`Relay-SPDT`、`HK4100F-DC5V-SHG`、`K1`、`SS8050 Y1`、`Q1`、`1N4148WS T4`、`D1`、`AD_Socket_4P`、`J1`、`Socket_3.96x3p`、`J2`、`Din`、`Ain`、`+5V`、`COM`、`NO`、`NC`、`SPDT`、`R1`、`1KΩ`、`R2`、`10KΩ`、`flyback diode`、`low-side drive`、`AC 220V`、`DC 30V`、`3A`、`5V@40mA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| K1 | Relay-SPDT | +5V 线圈驱动的单刀双掷继电器，触点引到 J2 的 COM/NO/NC | 图 53a2b49503f4 / 第 1 页 / B2-B3：K1 标注 Relay-SPDT，左侧线圈接 +5V/Q1，右侧三组触点接 J2 |
| Q1 | SS8050 Y1 | 继电器线圈的 NPN 低边驱动晶体管 | 图 53a2b49503f4 / 第 1 页 / B2-C2：Q1 标注 SS8050 Y1，基极经 R1 接 Din，集电极接线圈低端，发射极接 GND |
| D1 | 1N4148WS T4 | 跨接继电器线圈的续流二极管 | 图 53a2b49503f4 / 第 1 页 / B2：D1 标注 1N4148WS T4，与 K1 线圈并联在 +5V 和 Q1 集电极之间 |
| J1 | AD_Socket_4P | 低压控制与电源接口，引出 Ain、Din、VCC、GND | 图 53a2b49503f4 / 第 1 页 / B1-C2：J1 AD_Socket_4P，1~4 脚标注 Ain、Din、VCC、GND |
| J2 | Socket_3.96x3p | 继电器负载触点端子，1~3 脚为 COM、NO、NC | 图 53a2b49503f4 / 第 1 页 / B3：J2 Socket_3.96x3p，1/2/3 脚分别标注 COM/NO/NC 并连接 K1 触点 |
| R1 | 1KΩ | Din 到 Q1 基极的串联限流电阻 | 图 53a2b49503f4 / 第 1 页 / B2：R1 1KΩ 位于 Din 节点与 Q1 基极之间 |
| R2 | 10KΩ | Din 控制网络到 GND 的下拉电阻 | 图 53a2b49503f4 / 第 1 页 / B2-C2：R2 10KΩ 从 Din/R1 输入节点连接 GND |

## 系统结构

### Unit Relay

J1 的 Din 通过 Q1 驱动 K1 的 +5V 线圈，K1 的一组 SPDT 触点由 J2 引出为 COM、NO、NC。

- 参数与网络：`control_connector=J1`；`control_net=Din`；`driver=Q1 SS8050 Y1`；`relay=K1 Relay-SPDT`；`coil_supply=+5V`；`contact_connector=J2 COM/NO/NC`
- 证据：图 53a2b49503f4 / 第 1 页 / B1-C3：J1-Din-R1/Q1-K1-J2 的完整控制与触点路径

## 核心器件

### Q1 与 K1 线圈

K1 线圈上端接 +5V、下端接 Q1 集电极，Q1 发射极接 GND；Din 通过 R1 驱动 Q1 基极。

- 参数与网络：`coil_high=+5V`；`coil_low=Q1 collector`；`transistor=Q1 SS8050 Y1`；`emitter=GND`；`base=Din via R1 1KΩ`
- 证据：图 53a2b49503f4 / 第 1 页 / B2-C2：+5V-K1 线圈-Q1 集电极/发射极-GND 与 Din-R1-基极连线

## 电源

### +5V

J1.3 输入的 +5V 直接连接 K1 线圈高端；本页未显示稳压器、充电器、电池或电源监测器件。

- 参数与网络：`source=J1.3 VCC`；`rail=+5V`；`load=K1 coil`；`regulator=none shown`；`battery_charger_monitor=none shown`
- 证据：图 53a2b49503f4 / 第 1 页 / B1-C3：J1.3 +5V 与 K1 线圈连接；全页无其他电源管理器件

## 接口

### J1

J1.1 标为 Ain 且未连接，J1.2 Din 接驱动网络，J1.3 VCC 接 +5V，J1.4 GND 接地。

- 参数与网络：`connector=AD_Socket_4P`；`pin_1=Ain / NC`；`pin_2=Din / control input`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_direction=Din input to relay driver`
- 证据：图 53a2b49503f4 / 第 1 页 / B1-C2：J1.1 的悬空短线、J1.2 Din 至 R1/R2、J1.3 +5V、J1.4 GND

### J2

J2.1 为 COM，J2.2 为 NO，J2.3 为 NC，三脚分别连接 K1 的对应 SPDT 触点。

- 参数与网络：`connector=Socket_3.96x3p`；`pin_1=COM`；`pin_2=NO`；`pin_3=NC`；`contact_type=SPDT`
- 证据：图 53a2b49503f4 / 第 1 页 / B3：J2.1/J2.2/J2.3 的 COM/NO/NC 标注与 K1 触点连线

## GPIO 与控制信号

### Din

Din 节点经 R2（10KΩ）下拉至 GND，并经 R1（1KΩ）连接 Q1 基极。

- 参数与网络：`input=J1.2 Din`；`pulldown=R2 10KΩ to GND`；`base_resistor=R1 1KΩ to Q1 base`
- 证据：图 53a2b49503f4 / 第 1 页 / B2-C2：J1.2 Din 的分支到 R2/GND 与 R1/Q1 基极

## 保护电路

### K1 线圈

D1（1N4148WS T4）与 K1 线圈并联，连接在线圈的 +5V 端和 Q1 集电极端之间。

- 参数与网络：`diode=D1 1N4148WS T4`；`protected_load=K1 coil`；`high_side=+5V`；`low_side=Q1 collector`
- 证据：图 53a2b49503f4 / 第 1 页 / B2：D1 与 K1 线圈跨接在同一 +5V/低边节点之间

### K1 线圈与触点

原理图中 K1 线圈/驱动低压网络与 COM/NO/NC 触点网络之间仅以继电器机械关联表示，没有电气连线。

- 参数与网络：`control_side=+5V, Q1, GND, Din`；`contact_side=J2 COM, NO, NC`；`electrical_connection=none shown`；`insulation_rating=not shown`
- 证据：图 53a2b49503f4 / 第 1 页 / B2-B3：K1 左侧线圈与右侧 SPDT 触点的独立电气符号及机械虚线关联

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Relay | `control_connector=J1`；`control_net=Din`；`driver=Q1 SS8050 Y1`；`relay=K1 Relay-SPDT`；`coil_supply=+5V`；`contact_connector=J2 COM/NO/NC` |
| 接口 | J1 | `connector=AD_Socket_4P`；`pin_1=Ain / NC`；`pin_2=Din / control input`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_direction=Din input to relay driver` |
| 接口 | J2 | `connector=Socket_3.96x3p`；`pin_1=COM`；`pin_2=NO`；`pin_3=NC`；`contact_type=SPDT` |
| GPIO 与控制信号 | Din | `input=J1.2 Din`；`pulldown=R2 10KΩ to GND`；`base_resistor=R1 1KΩ to Q1 base` |
| 核心器件 | Q1 与 K1 线圈 | `coil_high=+5V`；`coil_low=Q1 collector`；`transistor=Q1 SS8050 Y1`；`emitter=GND`；`base=Din via R1 1KΩ` |
| 保护电路 | K1 线圈 | `diode=D1 1N4148WS T4`；`protected_load=K1 coil`；`high_side=+5V`；`low_side=Q1 collector` |
| 电源 | +5V | `source=J1.3 VCC`；`rail=+5V`；`load=K1 coil`；`regulator=none shown`；`battery_charger_monitor=none shown` |
| 保护电路 | K1 线圈与触点 | `control_side=+5V, Q1, GND, Din`；`contact_side=J2 COM, NO, NC`；`electrical_connection=none shown`；`insulation_rating=not shown` |
| 核心器件 | K1 具体型号 | `documented_part=HK4100F-DC5V-SHG`；`schematic_part=Relay-SPDT`；`coil_voltage_visible=+5V` |
| 接口 | J2 负载额定 | `documented_ac_rating=AC 220V@3A`；`documented_dc_rating=DC 30V@3A`；`schematic_rating=未标注`；`terminals=COM/NO/NC` |
| 其他事实 | 继电器动作参数 | `documented_coil_consumption=5V@40mA`；`documented_operate_time=6ms`；`documented_release_time=4ms`；`schematic_values=未标注` |
| GPIO 与控制信号 | 继电器状态指示灯 | `documented_indicator=relay status LED`；`schematic_led=none shown`；`schematic_series_resistor=none shown` |

## 待确认事项

- `component.relay-model-unconfirmed`：产品正文称继电器为 HK4100F-DC5V-SHG，但原理图 K1 仅标 Relay-SPDT，无法仅由本页确认具体料号。（证据：图 53a2b49503f4 / 第 1 页 / B2-B3：K1 旁仅显示 Relay-SPDT 和 +5V 线圈网络）
- `interface.contact-ratings-unconfirmed`：产品正文称触点支持 AC 220V@3A 或 DC 30V@3A；原理图只显示 COM/NO/NC 拓扑，没有电压、电流或绝缘额定值。（证据：图 53a2b49503f4 / 第 1 页 / B2-B3：K1 Relay-SPDT 与 J2 COM/NO/NC 区域，无额定参数文字）
- `other.timing-power-unconfirmed`：产品正文列出 5V@40mA 功耗、6ms 动作时间和 4ms 释放时间；这些参数未在原理图中标注。（证据：图 53a2b49503f4 / 第 1 页 / B2-B3：K1 线圈和触点符号仅含网络连接，无电流或时间参数）
- `gpio.status-indicator-unconfirmed`：产品正文声称带继电器状态指示灯，但本页原理图没有 LED 位号、LED 符号或相应限流电阻，无法确认其电路实现。（证据：图 53a2b49503f4 / 第 1 页 / 全页：仅有 K1、Q1、D1、R1、R2、J1、J2，未见 LED 器件）
- `review.relay-part-number`：K1 的量产料号是否为 HK4100F-DC5V-SHG？；原因：原理图只使用通用 Relay-SPDT 名称；需查 BOM、继电器丝印或规格书匹配。
- `review.contact-ratings`：该 K1/J2 组合是否保证 AC 220V@3A 或 DC 30V@3A，并满足相应绝缘要求？；原因：原理图无触点额定、PCB 间距和绝缘等级信息，需以实际继电器规格、BOM 与 PCB 资料确认。
- `review.relay-timing-power`：量产继电器的线圈功耗、动作时间和释放时间是否分别为 5V@40mA、6ms、4ms？；原因：这些动态/功耗参数不在原理图中，且依赖具体继电器料号，需要器件规格或实测。
- `review.status-led`：量产板是否另有未出现在本页原理图中的继电器状态 LED？；原因：正文声称有状态指示灯，但原理图器件清单和连线中没有 LED 或限流电阻。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `53a2b49503f4eac2799428e18114bfe7622bd6afed71af9d6288fe4ce8d85e43` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/577/UNIT-RELAY_sch_01.png` |

---

源文档：`zh_CN/unit/relay.md`

源文档 SHA-256：`c838fdedc36ba95c7e3403a205bb4f6c5af81223e779bb5139fa8a5ff81ebc06`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
