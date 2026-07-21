# Unit Neco 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Neco |
| SKU | U163 |
| 产品 ID | `unit-neco-a68addc8d9ac` |
| 源文档 | `zh_CN/unit/Neco Unit.md` |

## 概述

Unit Neco 是由 U1-U35 共 35 颗 WS2812C 构成的 5 V 串行 RGB 灯链，不含独立主控或协处理器。J1 将 IN 数据、按键信号、+5 和 GND 接入，J2 将末级 OUT、+5 和 GND 引出以支持物理级联。S1 按下时把 J1 pin 1 接地，C1-C17 为 +5 电源轨提供 17 颗 100 nF 去耦电容。

## 检索关键词

`Unit Neco`、`U163`、`WS2812C`、`WS2812C-2020`、`U1-U35`、`35 RGB LED`、`HY-2.0-4P_SMD`、`HY2.0-4P`、`J1`、`J2`、`S1`、`SW-PB`、`IN`、`OUT`、`+5`、`GND`、`DI`、`DO`、`VDD`、`C1-C17`、`100nF`、`serial RGB chain`、`Grove input`、`Grove output`、`active-low button`、`P1`、`P2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1-U35 | WS2812C | 35 颗 5 V 串行 RGB LED，依位号顺序由 IN 级联到 OUT | 图 961e4437ab3f / 第 1 页 / 页面 A1-B4 区域 U1-U35，器件均标注 WS2812C，DI/DO 依次串接，VDD 接 +5、GND 接地 |
| J1 | HY-2.0-4P_SMD | 输入侧 4 针 Grove 连接器，接入按键信号、IN、+5 和 GND | 图 961e4437ab3f / 第 1 页 / 页面 C2 区域 J1 HY-2.0-4P_SMD：pin 1 接 S1 节点，pin 2 标注 IN，pin 3 为 5V，pin 4 为 GND，pin 5/6 接 GND |
| J2 | HY-2.0-4P_SMD | 输出侧 4 针 Grove 连接器，引出 OUT、+5 和 GND供后级连接 | 图 961e4437ab3f / 第 1 页 / 页面 C3 区域 J2 HY-2.0-4P_SMD：pin 2 标注 OUT，pin 3 为 5V，pin 4 为 GND，pin 5/6 接 GND，pin 1 未连接 |
| S1 | SW-PB | 轻触按键，按下时将 J1 pin 1 信号节点短接至 GND | 图 961e4437ab3f / 第 1 页 / 页面 C2 区域 S1 SW-PB，一端接 GND，另一端直接连接 J1 pin 1 |
| C1-C17 | 100nF | +5 电源轨对 GND 的分布式去耦电容组 | 图 961e4437ab3f / 第 1 页 / 页面 D1-D3 区域 C1-C17，全部标注 100nF，上端接 +5、下端接 GND |
| P1/P2 | 未标注 | 两个接地焊盘或测试点 | 图 961e4437ab3f / 第 1 页 / 页面 D4 区域 P1、P2 圆形单点符号，二者下端均接 GND |

## 系统结构

### Unit Neco

整板由 35 颗 WS2812C 串行 RGB LED、输入/输出连接器、一个接地按键和 +5 V 去耦网络组成；原理图未显示独立 MCU、协处理器、存储器、晶振或稳压器。

- 参数与网络：`rgb_leds=U1-U35 WS2812C`；`led_count=35`；`input_connector=J1 HY-2.0-4P_SMD`；`output_connector=J2 HY-2.0-4P_SMD`；`button=S1 SW-PB`；`local_controller=null`；`local_storage=null`
- 证据：图 961e4437ab3f / 第 1 页 / 整页：A1-B4 为 U1-U35，C2-C3 为 J1/J2/S1，D1-D4 为 C1-C17/P1/P2，无其他 IC 或时钟/存储器件

## 核心器件

### U1-U35 WS2812C

U1 至 U35 均标注 WS2812C，共 35 颗；每颗符号包含 DI pin 3、GND pin 2、DO pin 1 和 VDD pin 4。

- 参数与网络：`references=U1-U35`；`part_number=WS2812C`；`quantity=35`；`pin_1=DO`；`pin_2=GND`；`pin_3=DI`；`pin_4=VDD`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 A1-B4，U1-U35 的 WS2812C 器件符号及 1=DO、2=GND、3=DI、4=VDD 标注

## 电源

### +5 电源轨

J1 pin 3 与 J2 pin 3 共用 +5 电源轨，该电源轨直接连接 U1-U35 每颗 WS2812C 的 VDD pin 4；板上未显示电源转换器、LDO、负载开关、充电或电池电路。

- 参数与网络：`rail=+5`；`input=J1 pin 3`；`pass_through=J2 pin 3`；`loads=U1-U35 VDD pin 4`；`converter=null`；`ldo=null`；`load_switch=null`；`battery=null`
- 证据：图 961e4437ab3f / 第 1 页 / 整页 +5 网络：J1/J2 pin 3、U1-U35 VDD 和 C1-C17 上端；无其他电源 IC

### C1-C17 去耦

C1 至 C17 均为 100 nF，全部跨接在 +5 与 GND 之间，为 LED 电源提供分布式高频去耦。

- 参数与网络：`references=C1-C17`；`quantity=17`；`capacitance=100nF each`；`rail=+5`；`return=GND`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 D1-D3 C1-C17，17 个电容均标注 100nF 并连接 +5/GND

## 接口

### J1 输入连接器

J1 pin 1 连接 S1 按键信号节点，pin 2 连接 IN，pin 3 连接 +5，pin 4 连接 GND；外壳固定脚 pin 5 和 pin 6 也接 GND。

- 参数与网络：`reference=J1`；`part_number=HY-2.0-4P_SMD`；`pin_1=S1 button node, active low`；`pin_2=IN, input to U1 DI`；`pin_3=+5 power`；`pin_4=GND`；`pin_5=GND mounting pin`；`pin_6=GND mounting pin`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 C2 J1：pin 1 上接 S1，pin 2 标注 IN，pin 3 接 +5，pin 4/5/6 接 GND

### J2 输出连接器

J2 pin 1 在本页未连接，pin 2 连接 OUT，pin 3 连接 +5，pin 4 连接 GND；外壳固定脚 pin 5 和 pin 6 也接 GND。

- 参数与网络：`reference=J2`；`part_number=HY-2.0-4P_SMD`；`pin_1=NC on schematic`；`pin_2=OUT from U35 DO`；`pin_3=+5 power`；`pin_4=GND`；`pin_5=GND mounting pin`；`pin_6=GND mounting pin`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 C3 J2：pin 1 仅有短引线且无网络，pin 2 标注 OUT，pin 3 接 +5，pin 4/5/6 接 GND

### J1/J2 电源透传

J1 与 J2 的 pin 3 通过同一 +5 网络相连，pin 4 通过同一 GND 网络相连，因此输出连接器透传输入侧电源和地。

- 参数与网络：`power_path=J1 pin 3 +5 to J2 pin 3 +5`；`ground_path=J1 pin 4 GND to J2 pin 4 GND`；`voltage_label=+5`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 C2-C3 J1/J2 之间的 pin 3 连续 +5 线和 pin 4 连续 GND 线

## 总线

### U1-U35 单线串行链

IN 进入 U1 DI，随后每颗 LED 的 DO 连接下一位号 LED 的 DI，链路依次经过 U1、U2、直至 U35，最终由 U35 DO 形成 OUT。

- 参数与网络：`controller_side_net=IN`；`first_device=U1 DI pin 3`；`chain_order=U1->U2->U3->U4->U5->U6->U7->U8->U9->U10->U11->U12->U13->U14->U15->U16->U17->U18->U19->U20->U21->U22->U23->U24->U25->U26->U27->U28->U29->U30->U31->U32->U33->U34->U35`；`last_device=U35 DO pin 1`；`downstream_net=OUT`；`direction=J1 IN to J2 OUT`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 A1-B4 蓝色数据连线：IN-U1.DI，各行末端折返下一行首颗，U35.DO-OUT

## GPIO 与控制信号

### S1 按键信号

S1 是接地型瞬时按键：一端接 GND，另一端直连 J1 pin 1，因此按下时 J1 pin 1 被拉低；板上未显示该信号的上拉电阻或去抖电容。

- 参数与网络：`switch=S1 SW-PB`；`connector_pin=J1 pin 1`；`active_level=low`；`pressed_state=short to GND`；`onboard_pullup=null`；`onboard_debounce=null`；`direction=output from board to host input`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 C2 S1-J1 pin 1 直接连线；S1 另一端接 GND，周围无上拉或 RC 元件

## 保护电路

### J1/J2 与 LED 链保护

本页未显示 +5、IN、OUT 或按键信号上的保险丝、TVS/ESD 阵列、限流电阻、反接保护或数据串联电阻；这些网络均直接连接对应负载或连接器。

- 参数与网络：`power_fuse=null`；`esd_array=null`；`reverse_polarity_protection=null`；`data_series_resistor=null`；`visible_protection=none`
- 证据：图 961e4437ab3f / 第 1 页 / 整页 J1/J2、IN/OUT/+5 连接路径；连接器与 LED/电容间无保护器件位号

## 关键网络

### IN

IN 网络从 J1 pin 2 连接 U1 DI pin 3，是 35 颗 RGB LED 串行链的板级数据输入。

- 参数与网络：`net=IN`；`source=J1 pin 2`；`destination=U1 DI pin 3`；`direction=input`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 C2 J1 pin 2 的 IN 标签及页面 A1 U1 DI pin 3 的 IN 标签

### OUT

OUT 网络从 U35 DO pin 1 连接 J2 pin 2，是板上 35 颗 RGB LED 处理后的串行数据输出。

- 参数与网络：`net=OUT`；`source=U35 DO pin 1`；`destination=J2 pin 2`；`direction=output`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 B4 U35 DO pin 1 的 OUT 标签及页面 C3 J2 pin 2 的 OUT 标签

## 调试与烧录

### P1/P2

P1 和 P2 各为一个单点焊盘符号，二者均直接连接 GND；原理图未标注其他调试或测试信号。

- 参数与网络：`P1=GND`；`P2=GND`；`signal_test_points=null`；`debug_bus=null`
- 证据：图 961e4437ab3f / 第 1 页 / 页面 D4 P1/P2 圆形单点符号及共同 GND 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Neco | `rgb_leds=U1-U35 WS2812C`；`led_count=35`；`input_connector=J1 HY-2.0-4P_SMD`；`output_connector=J2 HY-2.0-4P_SMD`；`button=S1 SW-PB`；`local_controller=null`；`local_storage=null` |
| 核心器件 | U1-U35 WS2812C | `references=U1-U35`；`part_number=WS2812C`；`quantity=35`；`pin_1=DO`；`pin_2=GND`；`pin_3=DI`；`pin_4=VDD` |
| 总线 | U1-U35 单线串行链 | `controller_side_net=IN`；`first_device=U1 DI pin 3`；`chain_order=U1->U2->U3->U4->U5->U6->U7->U8->U9->U10->U11->U12->U13->U14->U15->U16->U17->U18->U19->U20->U21->U22->U23->U24->U25->U26->U27->U28->U29->U30->U31->U32->U33->U34->U35`；`last_device=U35 DO pin 1`；`downstream_net=OUT`；`direction=J1 IN to J2 OUT` |
| 接口 | J1 输入连接器 | `reference=J1`；`part_number=HY-2.0-4P_SMD`；`pin_1=S1 button node, active low`；`pin_2=IN, input to U1 DI`；`pin_3=+5 power`；`pin_4=GND`；`pin_5=GND mounting pin`；`pin_6=GND mounting pin` |
| 接口 | J2 输出连接器 | `reference=J2`；`part_number=HY-2.0-4P_SMD`；`pin_1=NC on schematic`；`pin_2=OUT from U35 DO`；`pin_3=+5 power`；`pin_4=GND`；`pin_5=GND mounting pin`；`pin_6=GND mounting pin` |
| GPIO 与控制信号 | S1 按键信号 | `switch=S1 SW-PB`；`connector_pin=J1 pin 1`；`active_level=low`；`pressed_state=short to GND`；`onboard_pullup=null`；`onboard_debounce=null`；`direction=output from board to host input` |
| 电源 | +5 电源轨 | `rail=+5`；`input=J1 pin 3`；`pass_through=J2 pin 3`；`loads=U1-U35 VDD pin 4`；`converter=null`；`ldo=null`；`load_switch=null`；`battery=null` |
| 电源 | C1-C17 去耦 | `references=C1-C17`；`quantity=17`；`capacitance=100nF each`；`rail=+5`；`return=GND` |
| 关键网络 | IN | `net=IN`；`source=J1 pin 2`；`destination=U1 DI pin 3`；`direction=input` |
| 关键网络 | OUT | `net=OUT`；`source=U35 DO pin 1`；`destination=J2 pin 2`；`direction=output` |
| 接口 | J1/J2 电源透传 | `power_path=J1 pin 3 +5 to J2 pin 3 +5`；`ground_path=J1 pin 4 GND to J2 pin 4 GND`；`voltage_label=+5` |
| 保护电路 | J1/J2 与 LED 链保护 | `power_fuse=null`；`esd_array=null`；`reverse_polarity_protection=null`；`data_series_resistor=null`；`visible_protection=none` |
| 调试与烧录 | P1/P2 | `P1=GND`；`P2=GND`；`signal_test_points=null`；`debug_bus=null` |
| 核心器件 | U1-U35 LED 完整型号 | `schematic_marking=WS2812C`；`document_marking=WS2812C-2020`；`confirmed_package=null`；`references=U1-U35` |
| 接口 | J1/J2 Grove 线色映射 | `electrical_pinout=J1: pin1 button,pin2 IN,pin3 +5,pin4 GND; J2: pin1 NC,pin2 OUT,pin3 +5,pin4 GND`；`color_labels_on_schematic=null`；`document_colors=Black,Red,Yellow,White` |
| 总线 | WS2812C 数据协议参数 | `physical_topology=single-wire DI/DO cascade`；`data_rate=null`；`bit_timing=null`；`reset_timing=null`；`color_order=null`；`logic_threshold=null` |

## 待确认事项

- `component.ws2812-package-variant`：产品正文将灯珠写为 WS2812C-2020，但原理图器件值仅标注 WS2812C，无法仅凭本页确认 -2020 封装后缀或具体料号版本。（证据：图 961e4437ab3f / 第 1 页 / 页面 A1-B4，U1-U35 下方器件值均只显示 WS2812C，无 -2020 后缀）
- `interface.grove-color-mapping`：原理图给出 J1/J2 的电气 pin 编号和网络，但未标注 Black/Red/Yellow/White 线色，因此无法仅凭原理图确认产品正文中的 Grove 线色映射。（证据：图 961e4437ab3f / 第 1 页 / 页面 C2-C3 J1/J2 仅有 pin 编号、IN/OUT、5V、GND 标注，无导线颜色文字）
- `bus.ws2812-protocol-details`：原理图仅证明 DI/DO 单线串行拓扑，未给出数据速率、位时序、复位时序、色序或逻辑阈值，相关固件参数不能由本页确定。（证据：图 961e4437ab3f / 第 1 页 / 页面 A1-B4 U1-U35 的 DI/DO 连线；整页无速率、时序、色序或电平阈值注释）
- `review.ws2812-package-variant`：请用 BOM、PCB 封装或采购料号确认 U1-U35 是否均为 WS2812C-2020。；原因：原理图只标注 WS2812C，不能证明 -2020 封装后缀和具体装配料号。
- `review.grove-color-mapping`：请结合连接线定义或 PCB 连接器方向确认 Black/Red/Yellow/White 与 J1/J2 pin 1-4 的对应关系。；原因：原理图未显示 Grove 线色，且仅凭符号方向无法证明成品线缆颜色顺序。
- `review.ws2812-protocol-details`：请依据实际装配 LED 的 datasheet 或驱动实现确认数据速率、位时序、复位时序、色序和逻辑阈值。；原因：这些参数属于器件协议定义，原理图只显示物理级联关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `961e4437ab3fdc5459927c17eedce6ffa812815533525785d8d94ed07f3094a2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/618/Sch_neco-unit_sch_01.png` |

---

源文档：`zh_CN/unit/Neco Unit.md`

源文档 SHA-256：`1486dcf630a0aa1130e83331a6a71c78d13566c6d3cd953adb916715881a6f70`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
