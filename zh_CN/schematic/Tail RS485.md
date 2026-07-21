# Tail RS485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Tail RS485 |
| SKU | T002 |
| 产品 ID | `tail-rs485-35d2ba502abe` |
| 源文档 | `zh_CN/atom/tail485.md` |

## 概述

Tail RS485 的现有资源是一页功能框图，而不是带位号和引脚号的器件级原理图。框图确认外部 B/A 差分线进入 SP485 功能块，并在逻辑侧引出 TXD、RXD、5V 和 G；外部标为 12V、范围 9~24V 的电源经 DC/DC 功能块送到 USB 5V-IN。产品正文给出的 SP485EEN-L、AOZ1282CI 和 Atom G26/G32 映射无法由该图独立验证。图中也未展示收发方向控制、终端/偏置、浪涌保护、连接器针脚编号或完整接地路径，这些内容必须结合正式原理图、BOM 和板端丝印确认。

## 检索关键词

`Tail RS485`、`T002`、`RS485`、`SP485`、`SP485EEN-L`、`AOZ1282CI`、`B`、`A`、`TXD`、`RXD`、`G26`、`G32`、`9~24V`、`12V`、`5V`、`GND`、`USB 5V-IN`、`DC/DC`、`TTL-RS485`、`DE/RE`、`termination`、`bias network`、`VH-3.96 4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| SP485 block | SP485 | 在外部 B/A 差分侧与逻辑侧 TXD/RXD 之间进行 RS485 电平转换的功能块 | 图 394dab7fcba7 / 第 1 页 / 第 1 页左中黑色 SP485 功能块，左接 B/A，右连 G/5V/TXD/RXD |
| DC/DC block | 未标注 | 将左侧 12V（标注 9~24V）输入转换并送到 USB 5V-IN 的电源功能块 | 图 394dab7fcba7 / 第 1 页 / 第 1 页下方绿色 DC/DC 功能块，输入来自 12V/GND，输出箭头指向 USB 5V-IN |
| Field terminal (unreferenced) | 未标注 | 框图左侧的 B、A、12V 和 GND 外部接线端 | 图 394dab7fcba7 / 第 1 页 / 第 1 页最左侧自上而下 B、A、12V 9~24V、GND 四个色块 |
| Logic/USB side (unreferenced) | 未标注 | 框图右侧的 G、5V、TXD、RXD 逻辑接口和 USB 5V-IN 电源目标 | 图 394dab7fcba7 / 第 1 页 / 第 1 页右侧 G/5V/TXD/RXD 叠层色块及下方 USB 5V-IN 色块 |

## 系统结构

### Tail RS485 功能框图

外部 B/A 连接 SP485 功能块，SP485 逻辑侧引出 TXD、RXD、5V 和 G；外部 12V（图中同时标注 9~24V）与 GND 进入 DC/DC 功能块，其输出指向 USB 5V-IN。

- 参数与网络：`signal_path=B/A <-> SP485 block <-> TXD/RXD`；`transceiver_supply_labels=5V,G`；`power_path=12V (9~24V)/GND -> DC/DC -> USB 5V-IN`；`diagram_type=functional block diagram`
- 证据：图 394dab7fcba7 / 第 1 页 / 第 1 页完整框图的左侧端口、SP485、DC/DC 与右侧逻辑/USB 连接

## 电源

### 外部电源到 USB 5V-IN

标为 12V、范围 9~24V 的输入与 GND 进入 DC/DC 功能块，DC/DC 输出箭头直接指向 USB 5V-IN。

- 参数与网络：`input=12V label, 9~24V range`；`input_ground=GND`；`converter=DC/DC block`；`output_target=USB 5V-IN`
- 证据：图 394dab7fcba7 / 第 1 页 / 第 1 页下半部 12V/GND 到 DC/DC，再到 USB 5V-IN 的箭头

## 接口

### RS485 与外部电源端

框图左侧自上而下标出 B、A、12V 和 GND，其中 12V 色块下方明确标注 9~24V；B/A 进入 SP485，12V/GND 进入 DC/DC。

- 参数与网络：`signal_b=B -> SP485 block`；`signal_a=A -> SP485 block`；`power_label=12V`；`input_range_label=9~24V`；`ground=GND -> DC/DC`
- 证据：图 394dab7fcba7 / 第 1 页 / 第 1 页左侧 B/A/12V 9~24V/GND 色块及其到 SP485/DC/DC 的连线

### 逻辑侧接口标签

SP485 功能块右侧连接标为 G、5V、TXD 和 RXD 的四个逻辑侧端子，框图未给出这些端子的物理针脚编号。

- 参数与网络：`ground_label=G`；`supply_label=5V`；`transmit_label=TXD`；`receive_label=RXD`；`pin_numbers_shown=false`
- 证据：图 394dab7fcba7 / 第 1 页 / 第 1 页右侧 G/5V/TXD/RXD 色块与 SP485 的四条连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Tail RS485 功能框图 | `signal_path=B/A <-> SP485 block <-> TXD/RXD`；`transceiver_supply_labels=5V,G`；`power_path=12V (9~24V)/GND -> DC/DC -> USB 5V-IN`；`diagram_type=functional block diagram` |
| 接口 | RS485 与外部电源端 | `signal_b=B -> SP485 block`；`signal_a=A -> SP485 block`；`power_label=12V`；`input_range_label=9~24V`；`ground=GND -> DC/DC` |
| 接口 | 逻辑侧接口标签 | `ground_label=G`；`supply_label=5V`；`transmit_label=TXD`；`receive_label=RXD`；`pin_numbers_shown=false` |
| 电源 | 外部电源到 USB 5V-IN | `input=12V label, 9~24V range`；`input_ground=GND`；`converter=DC/DC block`；`output_target=USB 5V-IN` |
| 核心器件 | 正文中的收发器与稳压芯片型号 | `documented_transceiver=SP485EEN-L`；`diagram_transceiver_label=SP485`；`documented_converter=AOZ1282CI`；`diagram_converter_label=DC/DC`；`reference_designators=null` |
| 总线 | RS485 收发方向控制 | `logic_signals_shown=TXD,RXD`；`de_shown=false`；`re_shown=false`；`automatic_direction_shown=false`；`direction_method=null` |
| GPIO 与控制信号 | 正文中的 Atom GPIO 映射 | `documented_G26=TX`；`documented_G32=RX`；`diagram_labels=TXD,RXD`；`gpio_labels_on_diagram=null` |
| 保护电路 | RS485 终端、偏置与接口防护 | `termination_visible=false`；`bias_visible=false`；`tvs_visible=false`；`common_mode_filter_visible=false`；`fuse_visible=false`；`reverse_polarity_visible=false` |
| 接口 | 外部端子针脚与 B/A 定义 | `visual_order=B,A,12V,GND`；`connector_reference=null`；`pin_numbers=null`；`view_orientation=null`；`polarity_convention=null` |

## 待确认事项

- `component.documented-ic-models`：产品正文列出 SP485EEN-L 和 AOZ1282CI，但当前资源只显示 SP485 与 DC/DC 功能块，没有器件位号、完整料号或引脚，因此实际装配型号无法由本页确认。（证据：图 394dab7fcba7 / 第 1 页 / 第 1 页仅有 SP485 与 DC/DC 两个无位号功能块）
- `bus.rs485-direction-control`：框图只展示 TXD/RXD 与 SP485 功能块，没有 DE、RE、自动方向控制或收发使能网络，因此半双工方向切换方式无法确认。（证据：图 394dab7fcba7 / 第 1 页 / 第 1 页 SP485 与右侧 TXD/RXD 范围，无 DE/RE 或方向控制标注）
- `gpio.documented-atom-map`：产品正文管脚表给出 Atom Lite G26 对应 TX、G32 对应 RX；当前框图只标 TXD/RXD，没有 G26/G32 或物理针脚编号，因此该映射需由主机版本针脚表或实测确认。（证据：图 394dab7fcba7 / 第 1 页 / 第 1 页右侧只标 TXD/RXD，图中无 G26/G32）
- `protection.rs485-network-not-visible`：功能框图没有展示 B/A 终端电阻、失效保护偏置、TVS、共模滤波、保险或反接保护，无法判断量产电路是否包含这些器件。（证据：图 394dab7fcba7 / 第 1 页 / 第 1 页仅显示 B/A 到 SP485 及 12V/GND 到 DC/DC 的抽象功能连线）
- `interface.field-terminal-numbering`：框图以自上而下顺序展示 B、A、12V、GND，但没有连接器位号、针脚号、观察方向或板端丝印视角，实际接线顺序和 B/A 极性定义需要对照 PCB 丝印确认。（证据：图 394dab7fcba7 / 第 1 页 / 第 1 页左侧四个色块只给出 B/A/12V/GND 标签，没有连接器符号与针脚号）
- `review.ic-models`：T002 当前量产 BOM 的 RS485 收发器和 DC/DC 芯片是否分别为 SP485EEN-L 与 AOZ1282CI？；原因：现有资源只给出 SP485/DC/DC 功能块，无法验证完整料号、封装和版本。
- `review.rs485-direction`：T002 使用何种 DE/RE 或自动方向控制电路，TXD/RXD 的有效方向和时序要求是什么？；原因：功能框图未显示收发使能网络，不能从 TXD/RXD 标签推导半双工方向控制。
- `review.atom-gpio-map`：T002 当前适配的 Atom Lite 是否固定使用 G26=TX、G32=RX，其他 Atom 版本是否有不同映射？；原因：GPIO 编号只来自产品正文，框图没有主机型号、物理针脚或 GPIO 标签。
- `review.termination-bias-protection`：T002 量产电路是否包含 B/A 终端、偏置、TVS、共模滤波以及 9~24V 输入保护？；原因：现有资源是功能框图，不能据此判断器件级终端和保护设计。
- `review.field-terminal-pinout`：请用 T002 PCB 丝印或正式原理图确认 VH-3.96 4P 的针脚编号、观察方向以及 B/A 极性定义。；原因：色块顺序不是带针脚号和视角的连接器定义，直接据此接线存在反接风险。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `394dab7fcba7668172b929a0b5da6754bfc87bdb9e389d78660ad788815c1f48` | `https://static-cdn.m5stack.com/resource/docs/products/atom/tail485/tail485_sch_01.webp` |

---

源文档：`zh_CN/atom/tail485.md`

源文档 SHA-256：`11a05a0f801b70bba88dc04e8fdc6ff11bcdd281bed276482ea6b80a081c3519`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
