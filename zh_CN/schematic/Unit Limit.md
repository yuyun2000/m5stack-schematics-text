# Unit Limit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Limit |
| SKU | U145 |
| 产品 ID | `unit-limit-76279fe54f4f` |
| 源文档 | `zh_CN/unit/Unit Limit.md` |

## 概述

Unit Limit 是一块无主控的触点式限位开关单元，J1 Grove 4P 引入 VCC_5V，并从 IO2 引出 PROT1_OUT，IO1 未连接。U1 HT7533 将 VCC_5V 稳压为 VCC_3V3，R1 10K 将输出上拉至 3.3V；KF1 KW4A (S) 动作时把 PROT1_OUT 接到 GND。LED1 RED 与 R2 1K 串联在 VCC_3V3 和 PROT1_OUT 之间，随输出低电平形成点亮通路；原理图未显示主控、存储、通信总线或专用 ESD/过流保护器件。

## 检索关键词

`Unit Limit`、`U145`、`HT7533`、`KW4A (S)`、`KF1`、`J1`、`GROVE 4P`、`PROT1_OUT`、`VCC_5V`、`VCC_3V3`、`IO2`、`IO1 NC`、`Digital Output`、`limit switch`、`R1 10K`、`R2 1K`、`LED1 RED`、`C1 1uF/50V`、`C2 1uF/50V`、`5V to 3.3V`、`active low`、`GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE 4P | 四针 Grove 电源与数字输出接口，IO2 接 PROT1_OUT，IO1 未连接，另提供 VCC_5V 和 GND | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B1，J1 GROVE 4P，IO2/IO1/5V/GND 四个引脚及 PROT1_OUT、VCC_5V、GND 网络 |
| U1 | HT7533 | 将 J1 输入的 VCC_5V 稳压为 VCC_3V3，为输出上拉和状态 LED 供电 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 C1，U1 HT7533，VIN pin3、VOUT pin2、GND pin1 |
| KF1 | KW4A (S) | 三端机械限位开关，pin1 接 GND、pin3 接 PROT1_OUT，pin2 未连接 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B3，KF1 KW4A (S)，触点 pin1/pin2/pin3 与 GND、PROT1_OUT |
| LED1 | RED | 串联 R2 后跨接 VCC_3V3 与 PROT1_OUT 的红色状态指示灯 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B2-B3，LED1 RED 位于 R2 与 PROT1_OUT 之间 |
| R1 | 10K | 将 PROT1_OUT 上拉到 VCC_3V3 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B2，R1 10K 连接 VCC_3V3 与 PROT1_OUT |
| R2 | 1K | LED1 红色状态灯的串联限流电阻 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B2，R2 1K 串联在 VCC_3V3 与 LED1 RED 之间 |
| C1,C2 | 1uF/50V | HT7533 输出端与输入端的对地旁路电容 | 图 058f7b2378a3 / 第 1 页 / 第 1 页网格 C1-C2，C2 1uF/50V 从 VCC_5V 接 GND，C1 1uF/50V 从 VCC_3V3 接 GND |

## 系统结构

### Unit Limit 系统架构

该单元没有主控、协处理器、存储器或通信总线；J1 提供 5V 电源和数字输出，HT7533 生成 3.3V，KF1 机械触点产生低有效限位信号，LED1 显示输出状态。

- 参数与网络：`controller=null`；`coprocessor=null`；`memory=null`；`input_connector=J1 GROVE 4P`；`regulator=U1 HT7533`；`switch=KF1 KW4A (S)`；`output=PROT1_OUT`；`indicator=LED1 RED`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页完整网格 B1-C3，J1、U1、KF1、LED1 及全部网络

## 核心器件

### KF1 限位开关触点连接

KF1 标注 KW4A (S)，pin1 接 GND，pin3 接 PROT1_OUT，pin2 未接其他网络；触发闭合 pin1 与 pin3 时，PROT1_OUT 被拉到 GND。

- 参数与网络：`reference=KF1`；`part_number=KW4A (S)`；`pin1=GND`；`pin2=NC`；`pin3=PROT1_OUT`；`closed_result=PROT1_OUT -> GND`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B3，KF1 三个编号触点；pin1 走线到 GND，pin3 走线到 PROT1_OUT，pin2 悬空

### PROT1_OUT 状态指示灯

VCC_3V3 经 R2 1K 和 LED1 RED 串联后连接 PROT1_OUT；当 PROT1_OUT 被 KF1 拉到 GND 时，该支路形成从 VCC_3V3 到 GND 的电流通路。

- 参数与网络：`rail=VCC_3V3`；`resistor=R2 1K`；`led=LED1 RED`；`sense_net=PROT1_OUT`；`on_condition=PROT1_OUT low`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B2-B3，VCC_3V3-R2-LED1-PROT1_OUT 串联支路

## 电源

### VCC_5V 到 VCC_3V3 稳压

J1 的 5V 引脚形成 VCC_5V，连接 U1 HT7533 VIN pin3；U1 VOUT pin2 输出 VCC_3V3，GND pin1 接地。C2 1uF/50V 位于输入端对地，C1 1uF/50V 位于输出端对地。

- 参数与网络：`input=J1 5V / VCC_5V`；`regulator=U1 HT7533`；`vin_pin=pin3`；`vout_pin=pin2`；`ground_pin=pin1`；`output=VCC_3V3`；`input_capacitor=C2 1uF/50V`；`output_capacitor=C1 1uF/50V`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B1-C2，J1 VCC_5V、U1 HT7533 与 C1/C2

## 接口

### J1 Grove 4P 引脚映射

J1 从上到下标为 IO2、IO1、5V、GND：IO2 连接 PROT1_OUT，IO1 带未连接标记，5V 连接 VCC_5V，GND 接地。

- 参数与网络：`connector=J1 GROVE 4P`；`pin1=IO2 -> PROT1_OUT`；`pin2=IO1 -> NC`；`pin3=5V -> VCC_5V`；`pin4=GND -> GND`；`signal_direction=PROT1_OUT output from unit`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B1，J1 四针自上而下 IO2、IO1、5V、GND，IO1 右侧 NC 标记

## GPIO 与控制信号

### PROT1_OUT 数字输出电平

PROT1_OUT 通过 R1 10K 上拉到 VCC_3V3，并直接引到 J1 IO2；因此在 KF1 未把该节点接地时，输出由 R1 上拉。

- 参数与网络：`net=PROT1_OUT`；`connector_pin=J1 pin1 IO2`；`pullup=R1 10K`；`pullup_rail=VCC_3V3`；`direction=output`；`active_level=low`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B1-B3，J1 IO2、R1 10K、PROT1_OUT 同名网络

## 保护电路

### Grove 接口保护边界

本页原理图中 J1 的 VCC_5V、PROT1_OUT 和 GND 直接进入稳压器或信号节点，未画出保险丝、反接保护、TVS/ESD 二极管或输出限流/缓冲器。

- 参数与网络：`connector=J1`；`fuse=null`；`reverse_polarity_protection=null`；`tvs_esd=null`；`output_series_resistor=null`；`output_buffer=null`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页完整网格 B1-C3，J1 至 U1/KF1/LED1 的全部接口与电源路径

## 关键网络

### PROT1_OUT 关键网络连接

PROT1_OUT 同时连接 J1 IO2、R1 10K 下端、LED1 下端和 KF1 pin3；该节点没有经过缓冲器、反相器或串联电阻。

- 参数与网络：`net=PROT1_OUT`；`connector=J1 IO2`；`pullup=R1 10K to VCC_3V3`；`indicator=LED1 via R2 1K to VCC_3V3`；`switch_contact=KF1 pin3`；`buffer=null`
- 证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B1-B3，所有 PROT1_OUT 标注和连接节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Limit 系统架构 | `controller=null`；`coprocessor=null`；`memory=null`；`input_connector=J1 GROVE 4P`；`regulator=U1 HT7533`；`switch=KF1 KW4A (S)`；`output=PROT1_OUT`；`indicator=LED1 RED` |
| 接口 | J1 Grove 4P 引脚映射 | `connector=J1 GROVE 4P`；`pin1=IO2 -> PROT1_OUT`；`pin2=IO1 -> NC`；`pin3=5V -> VCC_5V`；`pin4=GND -> GND`；`signal_direction=PROT1_OUT output from unit` |
| 电源 | VCC_5V 到 VCC_3V3 稳压 | `input=J1 5V / VCC_5V`；`regulator=U1 HT7533`；`vin_pin=pin3`；`vout_pin=pin2`；`ground_pin=pin1`；`output=VCC_3V3`；`input_capacitor=C2 1uF/50V`；`output_capacitor=C1 1uF/50V` |
| GPIO 与控制信号 | PROT1_OUT 数字输出电平 | `net=PROT1_OUT`；`connector_pin=J1 pin1 IO2`；`pullup=R1 10K`；`pullup_rail=VCC_3V3`；`direction=output`；`active_level=low` |
| 核心器件 | KF1 限位开关触点连接 | `reference=KF1`；`part_number=KW4A (S)`；`pin1=GND`；`pin2=NC`；`pin3=PROT1_OUT`；`closed_result=PROT1_OUT -> GND` |
| 核心器件 | PROT1_OUT 状态指示灯 | `rail=VCC_3V3`；`resistor=R2 1K`；`led=LED1 RED`；`sense_net=PROT1_OUT`；`on_condition=PROT1_OUT low` |
| 关键网络 | PROT1_OUT 关键网络连接 | `net=PROT1_OUT`；`connector=J1 IO2`；`pullup=R1 10K to VCC_3V3`；`indicator=LED1 via R2 1K to VCC_3V3`；`switch_contact=KF1 pin3`；`buffer=null` |
| 保护电路 | Grove 接口保护边界 | `connector=J1`；`fuse=null`；`reverse_polarity_protection=null`；`tvs_esd=null`；`output_series_resistor=null`；`output_buffer=null` |
| 电源 | 正文标称工作电流 | `documented_standby=5V@2mA`；`documented_active=5V@3mA`；`schematic_current=null`；`test_condition=null`；`tolerance=null` |
| 其他事实 | 正文标称机械参数 | `documented_lever_length=16mm`；`documented_mechanical_life=400000 cycles`；`switch=KF1 KW4A (S)`；`contact_rating=null`；`actuation_force=null`；`test_condition=null` |

## 待确认事项

- `power.documented-current`：产品正文标称待机为 5V@2mA、工作为 5V@3mA；原理图仅显示 HT7533、上拉和 LED 支路，没有标注整机电流、测试条件或容差。（证据：图 058f7b2378a3 / 第 1 页 / 第 1 页完整电路，U1/R1/R2/LED1/KF1 周围无整机电流或测试条件标注）
- `other.documented-mechanical-rating`：产品正文标称开关柄长 16mm、机械寿命 40 万次；本页电气原理图只标出 KF1 KW4A (S)，没有尺寸、公差、动作力、触点额定值或寿命测试条件。（证据：图 058f7b2378a3 / 第 1 页 / 第 1 页网格 B3，KF1 仅标 KW4A (S) 与触点连接，未附机械规格）
- `review.operating-current`：请用量产规格或实测确认 5V@2mA 待机、5V@3mA 工作的测试条件与容差。；原因：原理图没有整机电流标注，且 LED 支路电流取决于器件压降和输出状态。
- `review.mechanical-rating`：请用 KF1 量产料号 datasheet 或机械图确认 16mm 柄长、40 万次寿命、动作力和触点额定值。；原因：电气原理图没有机械尺寸、寿命测试条件或触点额定参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `058f7b2378a39de5efc30f49af7528f7565a0df25372c173c1e3695e86605426` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/600/SCH_unitLimit_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit Limit.md`

源文档 SHA-256：`3eae9a88c05ccc479d29d290a461af3edd4458aabb74b28abbbb9823f8128c80`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
