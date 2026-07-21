# Unit Puzzle 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Puzzle |
| SKU | U193 |
| 产品 ID | `unit-puzzle-916715c42dc0` |
| 源文档 | `zh_CN/unit/Unit-Puzzle.md` |

## 概述

Unit Puzzle 是由 D1-D64 共 64 颗 WS2812E-1313 组成的 8×8 串行 RGB 灯阵，SIG_IN 进入 D1 DIN，数据沿编号顺序传递，D64 DOUT 输出 SIG_OUT。J2 输入 Grove 与 J1 输出 Grove 分别提供 SIG_IN/SIG_OUT、VCC_5V 和 GND，灯珠 VDD/GND 全部并接公共电源轨。板上没有主控、电源转换器、存储、时钟、复位或专用保护器件；底部电容组为 5V 灯阵去耦。

## 检索关键词

`Unit Puzzle`、`U193`、`WS2812E-1313`、`WS2812E`、`D1-D64`、`8x8 RGB matrix`、`64 pixel`、`SIG_IN`、`SIG_OUT`、`DIN`、`DOUT`、`VCC_5V`、`GND`、`J1 GROVE IO`、`J2 GROVE IO`、`Grove input`、`Grove output`、`IO1`、`IO2`、`single-wire LED`、`serial cascade`、`WS2812 chain`、`C1-C8`、`M2-Hole`、`H1`、`5V RGB LED`、`brightness 8%`、`10% brightness`、`93.99mA`、`14.27mA`、`1677万色`、`Port B`、`LED Signal`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| D1-D64 | WS2812E-1313 | 64 颗串联可寻址 RGB LED，排列为 8 行×8 列，使用公共 5V/GND 电源 | 图 6dc4261259de / 第 1 页 / 第 1 页中央至右侧，D1-D64 分为 8 行，每行 8 颗，器件值均为 WS2812E-1313 |
| J2 | GROVE IO | 灯阵输入接口，IO1 接 SIG_IN，VCC 接 VCC_5V，GND 接地，IO2 未接 | 图 6dc4261259de / 第 1 页 / 第 1 页左上 J2 GROVE IO，IO2/IO1/VCC/GND，其中 IO1 标 SIG_IN |
| J1 | GROVE IO | 灯阵级联输出接口，IO1 接 SIG_OUT，VCC 接 VCC_5V，GND 接地，IO2 未接 | 图 6dc4261259de / 第 1 页 / 第 1 页左上 J1 GROVE IO，IO2/IO1/VCC/GND，其中 IO1 标 SIG_OUT |
| C1-C8 | 10uF / 100nF / NC（按图装配组合） | VCC_5V 到 GND 的灯阵去耦/储能电容组，部分位置标 NC | 图 6dc4261259de / 第 1 页 / 第 1 页底部 VCC_5V 公共线上 C1-C8 电容组，标有 10uF、100nF 与 NC |
| H1 | M2-Hole | 机械固定孔 | 图 6dc4261259de / 第 1 页 / 第 1 页左中 H1 M2-Hole |

## 系统结构

### Unit Puzzle 系统架构

整板由 J2 输入 Grove、J1 输出 Grove、D1-D64 WS2812E-1313 串行灯链、5V 去耦电容组和 H1 固定孔构成；本页没有主控、协处理器、独立存储、电源转换器、晶振、复位或调试电路。

- 参数与网络：`pixels=D1-D64 WS2812E-1313`；`input=J2 SIG_IN`；`output=J1 SIG_OUT`；`power=VCC_5V/GND`；`controller=null`；`memory=null`；`converter=null`；`clock=null`；`reset=null`；`debug=null`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页完整原理图，J1/J2/D1-D64/C1-C8/H1 全部器件

## 核心器件

### 8×8 WS2812E-1313 灯阵

D1-D64 共 64 颗，原理图按 D1-D8、D9-D16、D17-D24、D25-D32、D33-D40、D41-D48、D49-D56、D57-D64 排成 8 行，每行 8 颗；每颗均标 WS2812E-1313。

- 参数与网络：`part_number=WS2812E-1313`；`references=D1-D64`；`rows=8`；`columns=8`；`count=64`；`row_groups=D1-D8;D9-D16;D17-D24;D25-D32;D33-D40;D41-D48;D49-D56;D57-D64`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页中央 8 行灯珠阵列及 D1-D64 位号

## 电源

### 灯阵公共 5V 电源

J1/J2 VCC 均连接 VCC_5V；D1-D64 的 VDD pin1 全部接 VCC_5V，GND pin3 全部接公共 GND。板上没有 5V 稳压、升降压或负载开关。

- 参数与网络：`rail=VCC_5V`；`connectors=J1 VCC,J2 VCC`；`pixel_supply=D1-D64 pin1 VDD`；`pixel_ground=D1-D64 pin3 GND`；`converter=null`；`load_switch=null`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页 J1/J2 VCC_5V 与所有 D1-D64 VDD/GND 公共网络

### VCC_5V 去耦电容组

页面底部 C1-C8 跨接 VCC_5V 与 GND，器件值组合包含 10uF、100nF 与 NC 装配位，为灯阵电源提供集中去耦和储能。

- 参数与网络：`references=C1-C8`；`rail=VCC_5V`；`return=GND`；`values_visible=10uF,100nF,NC`；`role=bulk and high-frequency decoupling`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页底部 C1-C8 与 VCC_5V/GND 公共线

## 接口

### J2 输入 Grove

J2 的 IO1 接 SIG_IN、VCC 接 VCC_5V、GND 接 GND；IO2 引脚只有短桩，没有网络名或到其他器件的连线。

- 参数与网络：`connector=J2 GROVE IO`；`io1=SIG_IN`；`io2=unconnected`；`vcc=VCC_5V`；`ground=GND`；`direction=LED chain input`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页左上 J2 IO2/IO1/VCC/GND 与 SIG_IN

### J1 输出 Grove

J1 的 IO1 接 SIG_OUT、VCC 接 VCC_5V、GND 接 GND；IO2 引脚只有短桩，没有网络名或到其他器件的连线。

- 参数与网络：`connector=J1 GROVE IO`；`io1=SIG_OUT`；`io2=unconnected`；`vcc=VCC_5V`；`ground=GND`；`direction=LED chain output`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页左上 J1 IO2/IO1/VCC/GND 与 SIG_OUT

## 总线

### WS2812 单线串行级联

SIG_IN 连接 D1 DIN pin4；各 WS2812E-1313 的 DOUT pin2 连接下一颗 DIN pin4，形成 D1 到 D64 的串行级联；D64 DOUT pin2 形成 SIG_OUT。

- 参数与网络：`protocol_wire=single data wire`；`input=SIG_IN -> D1 pin4 DIN`；`chain=D1 DOUT -> D2 DIN -> ... -> D64 DIN`；`output=D64 pin2 DOUT -> SIG_OUT`；`pixel_count=64`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页 D1 左侧 SIG_IN、各灯 DIN/DOUT 连线与 D64 右侧 SIG_OUT

## 保护电路

### Grove 与灯阵保护边界

J1/J2 的 VCC_5V、SIG_IN、SIG_OUT 直接连接灯阵或电源轨；本页没有显示保险丝、反接保护、TVS/ESD 二极管、信号串阻或过流保护器件。

- 参数与网络：`interfaces=J1,J2`；`fuse=null`；`reverse_protection=null`；`tvs_esd=null`；`signal_series_resistor=null`；`overcurrent_protection=null`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页完整 J1/J2 至 D1-D64 和 VCC_5V 路径，未见专用保护符号

## 关键网络

### SIG_IN 与 SIG_OUT

SIG_IN 仅连接 J2 IO1 和 D1 DIN；SIG_OUT 仅连接 D64 DOUT 和 J1 IO1。两端没有电平转换器、串联电阻、缓冲器或方向控制器。

- 参数与网络：`input_net=J2 IO1 <-> SIG_IN <-> D1 DIN`；`output_net=D64 DOUT <-> SIG_OUT <-> J1 IO1`；`level_shifter=null`；`series_resistor=null`；`buffer=null`；`direction_control=null`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页左上 J2/SIG_IN/D1 与右下 D64/SIG_OUT/J1 同名网络

## 其他事实

### H1 M2 固定孔

H1 标为 M2-Hole，是本页唯一机械固定孔符号，不连接任何电气网络。

- 参数与网络：`reference=H1`；`type=M2-Hole`；`electrical_connection=null`
- 证据：图 6dc4261259de / 第 1 页 / 第 1 页左中 H1 M2-Hole

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Puzzle 系统架构 | `pixels=D1-D64 WS2812E-1313`；`input=J2 SIG_IN`；`output=J1 SIG_OUT`；`power=VCC_5V/GND`；`controller=null`；`memory=null`；`converter=null`；`clock=null`；`reset=null`；`debug=null` |
| 核心器件 | 8×8 WS2812E-1313 灯阵 | `part_number=WS2812E-1313`；`references=D1-D64`；`rows=8`；`columns=8`；`count=64`；`row_groups=D1-D8;D9-D16;D17-D24;D25-D32;D33-D40;D41-D48;D49-D56;D57-D64` |
| 总线 | WS2812 单线串行级联 | `protocol_wire=single data wire`；`input=SIG_IN -> D1 pin4 DIN`；`chain=D1 DOUT -> D2 DIN -> ... -> D64 DIN`；`output=D64 pin2 DOUT -> SIG_OUT`；`pixel_count=64` |
| 接口 | J2 输入 Grove | `connector=J2 GROVE IO`；`io1=SIG_IN`；`io2=unconnected`；`vcc=VCC_5V`；`ground=GND`；`direction=LED chain input` |
| 接口 | J1 输出 Grove | `connector=J1 GROVE IO`；`io1=SIG_OUT`；`io2=unconnected`；`vcc=VCC_5V`；`ground=GND`；`direction=LED chain output` |
| 电源 | 灯阵公共 5V 电源 | `rail=VCC_5V`；`connectors=J1 VCC,J2 VCC`；`pixel_supply=D1-D64 pin1 VDD`；`pixel_ground=D1-D64 pin3 GND`；`converter=null`；`load_switch=null` |
| 电源 | VCC_5V 去耦电容组 | `references=C1-C8`；`rail=VCC_5V`；`return=GND`；`values_visible=10uF,100nF,NC`；`role=bulk and high-frequency decoupling` |
| 关键网络 | SIG_IN 与 SIG_OUT | `input_net=J2 IO1 <-> SIG_IN <-> D1 DIN`；`output_net=D64 DOUT <-> SIG_OUT <-> J1 IO1`；`level_shifter=null`；`series_resistor=null`；`buffer=null`；`direction_control=null` |
| 保护电路 | Grove 与灯阵保护边界 | `interfaces=J1,J2`；`fuse=null`；`reverse_protection=null`；`tvs_esd=null`；`signal_series_resistor=null`；`overcurrent_protection=null` |
| 其他事实 | H1 M2 固定孔 | `reference=H1`；`type=M2-Hole`；`electrical_connection=null` |
| 接口 | 正文中的输出 Grove 预留 IO | `documented_feature=output Grove spare IO for Port B sensor`；`output_io2=J1 IO2 unconnected in schematic`；`input_io2=J2 IO2 unconnected in schematic`；`passthrough=null` |
| 电源 | 正文中的亮度与电流参数 | `documented_recommended_brightness=10%`；`documented_test_brightness=8% white`；`documented_pixel_power=6mW`；`documented_operating=DC 5V@93.99mA`；`documented_standby=DC 5V@14.27mA`；`schematic_current=null`；`test_pattern=null` |
| 核心器件 | 正文中的 1677 万色 | `pixels=D1-D64 WS2812E-1313`；`documented_colors=1677万色`；`channel_depth=null`；`pwm_frequency=null`；`timing=null` |

## 待确认事项

- `interface.documented-spare-io`：产品正文称输出 Grove 预留一个 IO 可连接 Port B 传感器；原理图中 J1 IO2 与 J2 IO2 均为未命名短桩，未显示两者直通或连接到其他电路，因此预留 IO 的实际导通路径无法由本页确认。（证据：图 6dc4261259de / 第 1 页 / 第 1 页左上 J1/J2 IO2 均无网络名和外接连线）
- `power.documented-brightness-current`：正文建议长期使用 10% 亮度，并标称 8% 白光时单灯约 6mW、整机工作 DC 5V@93.99mA、待机 DC 5V@14.27mA；原理图只显示灯珠和 5V 电源连接，没有亮度、PWM 数据、整机电流或测试条件。（证据：图 6dc4261259de / 第 1 页 / 第 1 页 D1-D64 与 VCC_5V/GND，图中无亮度或功耗文字）
- `component.documented-color-depth`：正文称灯阵支持 1677 万色；原理图仅确认 D1-D64 型号为 WS2812E-1313，没有打印通道位深、PWM 频率、刷新时序或颜色数量。（证据：图 6dc4261259de / 第 1 页 / 第 1 页灯阵器件仅标 WS2812E-1313 与 DIN/DOUT/VDD/GND）
- `review.spare-io`：请用 PCB 网表或导通实测确认 J1 IO2 是否与 J2 IO2 直通，以及输出 Grove 预留 IO 的实际接法。；原因：正文称有预留 IO，但原理图中两个 IO2 均显示为未连接。
- `review.brightness-current`：请用量产规格或实测确认 10% 建议亮度、8% 白光单灯功耗、待机/工作电流及测试图案。；原因：原理图不能证明亮度设置和整机功耗。
- `review.color-depth`：请用 WS2812E-1313 数据手册确认通道位深、颜色数量、PWM/刷新参数与级联时序。；原因：板级原理图只给出器件型号和连线。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6dc4261259dedebe96aa59ff5eb1227b1a6dce00c7f4bb4d7d13df9f2b385d88` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/schematic.png` |

---

源文档：`zh_CN/unit/Unit-Puzzle.md`

源文档 SHA-256：`5a70fe5ca71427574e402a22c3a6dcfe1b9235ca59a959de8fcae990f9dfda83`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
