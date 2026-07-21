# Base AAA 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base AAA |
| SKU | A122 |
| 产品 ID | `base-aaa-4a99b42565c7` |
| 源文档 | `zh_CN/base/base_aaa.md` |

## 概述

Base AAA 由四节电池块、SW1 物理开关、F1/SI2301 输入路径和 U1 MP1470 降压电路组成，VIN 经 L1 4.7uH 生成 VCC_4V，再经 D2 DSS34 形成 BAT_4V 送入 M5-Bus 与 12P 扩展口。电路提供 J1/J2 两组 Grove、J4 Header12 和 J3 M5_BUS，并用 R6/R7 100K 分压将 BAT_6V_OUT 经 TP1 引到 GPIO35。J4 pin12 的 BAT_6V_OUT 位于 F1/Q1 下游，可作为外部电源接入点，但图中未给出该路径的允许电压与保护边界。电池块电压标注、GPIO35 焊点默认状态、M5-Bus 的 GPIO19/GPIO27 命名以及 BAT_4V 精确输出值需要结合 BOM、PCB 和实测确认。

## 检索关键词

`Base AAA`、`A122`、`MP1470`、`SI2301`、`SS-12D07-5`、`DSS34`、`BAT_6V_IN`、`BAT_6V_OUT`、`VIN`、`VCC_4V`、`BAT_4V`、`4x1.2V`、`4x AAA`、`F1 1A/12V`、`L1 4.7uH`、`GPIO35`、`TP1`、`100K divider`、`GPIO36`、`GPIO26`、`GPIO21`、`GPIO22`、`GPIO27`、`GPIO19`、`GPIO34`、`GPIO0`、`RXD`、`TXD`、`M5_BUS`、`Header 12`、`GROVE-B`、`5V`、`3V3`、`HPWR`、`RED 0603`、`external BAT supply`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| Battery block (unreferenced) | 未标注 | 四节电池块，输出 GND、BAT_6V_IN，并画出 1x/2x/3x 1.5V 分段抽头 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A1-B1 区绿色电池块，内部标 4x1.2V，外部标 1x1.5V、2x1.5V、3x1.5V、GND、BAT_6V_IN |
| SW1 | SS-12D07-5 | 将 BAT_6V_OUT 切换到 VIN，并将外壳/固定端接地的物理电源开关 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A1 区 SW1 SS-12D07-5，pin1 BAT_6V_OUT、pins2/3 VIN、pins4/5 GND |
| F1,Q1 | 1A/12V / SI2301 | BAT_6V_IN 与 BAT_6V_OUT 之间的串联保险和 MOSFET 输入路径 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A1-A2 区 BAT_6V_IN-Q1 SI2301-F1 1A/12V-BAT_6V_OUT，Q1 控制端接 GND |
| U1 | MP1470 | 从 VIN 生成 VCC_4V 的降压转换器 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A2 区 U1 MP1470，IN/EN/BS/LX/FB/GND 与输入、L1、反馈网络 |
| L1,D2 | 3015/4.7uH / DSS34 | MP1470 输出电感及 VCC_4V 到 BAT_4V 的串联二极管 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A2-A3 区 L1 3015/4.7uH、VCC_4V 输出电容组与 D2 DSS34-BAT_4V |
| D1,R1 | RED 0603 / 1.5K | VCC_4V 到 GND 的电源指示灯支路 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 B3 区 VCC_4V-R1 1.5K-D1 RED 0603-GND |
| R6,R7,TP1 | 100K / 100K / TP1 | BAT_6V_OUT 到 GPIO35 的等值分压与焊点/测试点 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 B1-C1 区 BAT_6V_OUT-R6 100K-TP1/GPIO35-R7 100K-GND |
| J4 | Header 12 | 引出 GND、5V、GPIO、RST、3V3、BAT_4V 和 BAT_6V_OUT 的 12 针扩展接口 | 图 23a1c26120c2 / 第 1 页 / 第 1 页 A4 区 J4 Header12 的 pin1-pin12 全部网络标签 |
| J1,J2 | GROVE-4P / GROVE-B 4P | 两组 5V Grove 扩展接口，分别连接 GPIO36/GPIO26 与 RXD/TXD | 图 23a1c26120c2 / 第 1 页 / 第 1 页 B4 区 J1 GROVE-4P 与 J2 GROVE-B 4P 的 IO2/IO1/5V/GND |
| J3 | M5_BUS | M5 主机总线，连接电源、GPIO、UART、复位和 HPWR | 图 23a1c26120c2 / 第 1 页 / 第 1 页 C3-D4 区 J3 M5_BUS，pin1-pin30 符号名和外部网络 |

## 系统结构

### Base AAA 电源与扩展架构

电池块的 BAT_6V_IN 经 Q1 SI2301、F1 1A/12V 形成 BAT_6V_OUT，SW1 将其接到 VIN；U1 MP1470 经 L1 生成 VCC_4V，再由 D2 形成 BAT_4V，并向 J3/J4 及两组 Grove 提供电源和信号扩展。

- 参数与网络：`raw_battery_path=BAT_6V_IN -> Q1 SI2301 -> F1 1A/12V -> BAT_6V_OUT`；`switch_path=BAT_6V_OUT -> SW1 -> VIN`；`converter=U1 MP1470`；`regulated_path=VIN -> U1/L1 -> VCC_4V -> D2 -> BAT_4V`；`interfaces=J3 M5_BUS, J4 Header12, J1/J2 Grove`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页完整单页：电池/开关、MP1470、电压分压、J1-J4 与 M5_BUS

## 电源

### 电池输入、保险、MOSFET 与开关

BAT_6V_IN 先经过 Q1 SI2301，再经过 F1 1A/12V 到 BAT_6V_OUT；Q1 控制端接 GND。SW1 pin1 接 BAT_6V_OUT，pins2/3 同接 VIN，pins4/5 接 GND。

- 参数与网络：`battery_input=BAT_6V_IN`；`series_mosfet=Q1 SI2301`；`fuse=F1 1A/12V`；`switched_input=BAT_6V_OUT -> SW1 pin1; SW1 pins2/3 -> VIN`；`switch_ground=SW1 pins4/5 -> GND`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A1-A2 区 BAT_6V_IN、Q1、F1、BAT_6V_OUT、SW1 与 VIN

### MP1470 输入与使能

U1 IN pin3 接 VIN，EN pin5 经 R2 100K 接 VIN，GND pin1 接地；VIN 使用 C3 22uF/10V、C4 100nF、C11/C10 各 47uF/10V 和 C9 22uF/10V 对地去耦。

- 参数与网络：`input=U1 IN pin3 -> VIN`；`enable=U1 EN pin5 -> R2 100K -> VIN`；`ground=U1 pin1 -> GND`；`input_caps=C3 22uF/10V, C4 100nF, C11/C10 47uF/10V, C9 22uF/10V`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A2-B2 区 VIN、U1 IN/EN/GND、R2 与 C3/C4/C9/C10/C11

### MP1470 输出与反馈网络

U1 LX pin2 经 L1 3015/4.7uH 形成 VCC_4V，C6 100nF 跨 BS pin6 与 LX；FB pin4 经 R5 75K 接到 R3 82K/R4 20K 分压节点。VCC_4V 使用 C7 100nF、C8 22uF/10V 和 C1/C2/C5 各 100uF 6.3V 对地滤波。

- 参数与网络：`switch_node=U1 LX pin2`；`inductor=L1 3015/4.7uH`；`output_net=VCC_4V`；`bootstrap=C6 100nF between BS pin6 and LX`；`feedback=FB pin4 -> R5 75K -> R3 82K/R4 20K junction`；`output_caps=C7 100nF, C8 22uF/10V, C1/C2/C5 100uF 6.3V`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A2-A3 区 U1 BS/LX/FB、C6/L1、R3/R4/R5 与 VCC_4V 电容组

### VCC_4V 到 BAT_4V

VCC_4V 经串联 D2 DSS34 形成 BAT_4V；BAT_4V 连接 J4 pin11 和 J3 M5_BUS pin29。

- 参数与网络：`source=VCC_4V`；`series_diode=D2 DSS34`；`output=BAT_4V`；`consumers=J4 pin11, J3 pin29 VBAT`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A3 区 VCC_4V-D2 DSS34-BAT_4V 及 A4/D4 的同名网络

### J4 BAT_6V_OUT 外部供电路径

J4 pin12 直接连接 BAT_6V_OUT；该节点位于电池侧 Q1/F1 之后，并经 SW1 接 VIN，因此从 J4 注入 BAT_6V_OUT 不经过 Q1 和 F1。

- 参数与网络：`external_pin=J4 pin12 BAT_6V_OUT`；`to_converter=BAT_6V_OUT -> SW1 -> VIN -> U1`；`bypasses=Q1 SI2301 and F1 1A/12V`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 J4 pin12 BAT_6V_OUT 与 A1 区同名网络、SW1、F1/Q1 相对位置

## 接口

### VCC_4V 红色电源指示灯

VCC_4V 经 R1 1.5K 和 D1 RED 0603 接 GND，构成固定连接的电源指示支路。

- 参数与网络：`source=VCC_4V`；`resistor=R1 1.5K`；`led=D1 RED 0603`；`return=GND`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B3 区 VCC_4V-R1-D1-GND

### J4 12 针扩展接口

J4 pins1-12 依次为 GND、5V、GPIO21、GPIO22、GPIO27、GPIO19、GPIO34、GPIO0、RST、3V3、BAT_4V、BAT_6V_OUT。

- 参数与网络：`pin1=GND`；`pin2=5V`；`pin3=GPIO21`；`pin4=GPIO22`；`pin5=GPIO27`；`pin6=GPIO19`；`pin7=GPIO34`；`pin8=GPIO0`；`pin9=RST`；`pin10=3V3`；`pin11=BAT_4V`；`pin12=BAT_6V_OUT`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A4 区 J4 Header12 的 pin1-pin12 标号和网络

### J1 Grove 接口

J1 GROVE-4P 的 IO2 连接 GPIO36，IO1 连接 GPIO26，另外两脚为 5V 和 GND。

- 参数与网络：`IO2=GPIO36`；`IO1=GPIO26`；`power=5V`；`ground=GND`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B4 区 J1 GROVE-4P 与 GPIO36/GPIO26/5V/GND

### J2 Grove-B UART 接口

J2 GROVE-B 4P 的 IO2 连接 RXD，IO1 连接 TXD，另外两脚为 5V 和 GND。

- 参数与网络：`IO2=RXD`；`IO1=TXD`；`power=5V`；`ground=GND`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B4 区 J2 GROVE-B 4P 与 RXD/TXD/5V/GND

### J3 M5_BUS 已连接针脚

J3 已接网络包括 pin1 GPIO35、pins2/4/6 GND、pin3 GPIO36、pin5 RST、pin9 GPIO26、pin11 3V3、pin15 TXD、pin16 RXD、pin17 GPIO22、pin18 GPIO21、pin21 GPIO19、pin22 GPIO27、pin23 GPIO0、pin25 GPIO34、pins26/28/30 HPWR、pin27 5V、pin29 BAT_4V。

- 参数与网络：`gpio=1 GPIO35; 3 GPIO36; 9 GPIO26; 17 GPIO22; 18 GPIO21; 21 GPIO19; 22 GPIO27; 23 GPIO0; 25 GPIO34`；`uart=15 TXD; 16 RXD`；`reset=5 RST`；`ground=2,4,6 GND`；`3V3=pin11`；`5V=pin27`；`BAT_4V=pin29`；`HPWR=pins26,28,30`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 C3-D4 区 J3 M5_BUS 所有带外部连线的 pin1-pin30

## 模拟电路

### BAT_6V_OUT 电压分压

R6 100K 从 BAT_6V_OUT 接到分压中点，R7 100K 从中点接 GND；该中点经 TP1 标记连接 GPIO35，构成 1:1 电阻分压。

- 参数与网络：`upper=R6 100K from BAT_6V_OUT`；`lower=R7 100K to GND`；`ratio=1/2`；`tap=TP1 -> GPIO35`
- 证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B1-C1 区 R6/R7/TP1/GPIO35 分压链

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base AAA 电源与扩展架构 | `raw_battery_path=BAT_6V_IN -> Q1 SI2301 -> F1 1A/12V -> BAT_6V_OUT`；`switch_path=BAT_6V_OUT -> SW1 -> VIN`；`converter=U1 MP1470`；`regulated_path=VIN -> U1/L1 -> VCC_4V -> D2 -> BAT_4V`；`interfaces=J3 M5_BUS, J4 Header12, J1/J2 Grove` |
| 电源 | 电池输入、保险、MOSFET 与开关 | `battery_input=BAT_6V_IN`；`series_mosfet=Q1 SI2301`；`fuse=F1 1A/12V`；`switched_input=BAT_6V_OUT -> SW1 pin1; SW1 pins2/3 -> VIN`；`switch_ground=SW1 pins4/5 -> GND` |
| 电源 | MP1470 输入与使能 | `input=U1 IN pin3 -> VIN`；`enable=U1 EN pin5 -> R2 100K -> VIN`；`ground=U1 pin1 -> GND`；`input_caps=C3 22uF/10V, C4 100nF, C11/C10 47uF/10V, C9 22uF/10V` |
| 电源 | MP1470 输出与反馈网络 | `switch_node=U1 LX pin2`；`inductor=L1 3015/4.7uH`；`output_net=VCC_4V`；`bootstrap=C6 100nF between BS pin6 and LX`；`feedback=FB pin4 -> R5 75K -> R3 82K/R4 20K junction`；`output_caps=C7 100nF, C8 22uF/10V, C1/C2/C5 100uF 6.3V` |
| 电源 | VCC_4V 到 BAT_4V | `source=VCC_4V`；`series_diode=D2 DSS34`；`output=BAT_4V`；`consumers=J4 pin11, J3 pin29 VBAT` |
| 接口 | VCC_4V 红色电源指示灯 | `source=VCC_4V`；`resistor=R1 1.5K`；`led=D1 RED 0603`；`return=GND` |
| 模拟电路 | BAT_6V_OUT 电压分压 | `upper=R6 100K from BAT_6V_OUT`；`lower=R7 100K to GND`；`ratio=1/2`；`tap=TP1 -> GPIO35` |
| 接口 | J4 12 针扩展接口 | `pin1=GND`；`pin2=5V`；`pin3=GPIO21`；`pin4=GPIO22`；`pin5=GPIO27`；`pin6=GPIO19`；`pin7=GPIO34`；`pin8=GPIO0`；`pin9=RST`；`pin10=3V3`；`pin11=BAT_4V`；`pin12=BAT_6V_OUT` |
| 接口 | J1 Grove 接口 | `IO2=GPIO36`；`IO1=GPIO26`；`power=5V`；`ground=GND` |
| 接口 | J2 Grove-B UART 接口 | `IO2=RXD`；`IO1=TXD`；`power=5V`；`ground=GND` |
| 接口 | J3 M5_BUS 已连接针脚 | `gpio=1 GPIO35; 3 GPIO36; 9 GPIO26; 17 GPIO22; 18 GPIO21; 21 GPIO19; 22 GPIO27; 23 GPIO0; 25 GPIO34`；`uart=15 TXD; 16 RXD`；`reset=5 RST`；`ground=2,4,6 GND`；`3V3=pin11`；`5V=pin27`；`BAT_4V=pin29`；`HPWR=pins26,28,30` |
| 电源 | J4 BAT_6V_OUT 外部供电路径 | `external_pin=J4 pin12 BAT_6V_OUT`；`to_converter=BAT_6V_OUT -> SW1 -> VIN -> U1`；`bypasses=Q1 SI2301 and F1 1A/12V` |
| 电源 | 电池块电压与电芯类型 | `diagram_internal_label=4x1.2V`；`diagram_taps=1x1.5V, 2x1.5V, 3x1.5V`；`output_net=BAT_6V_IN`；`documented_cells=4 x AAA dry batteries`；`resolved_chemistry=null`；`resolved_input_range=null` |
| 模拟电路 | GPIO35 电压采样焊点状态 | `documented_default=open`；`documented_action=solder to enable`；`schematic_marker=TP1`；`default_state_on_schematic=null` |
| 接口 | M5_BUS pin21/pin22 网络命名 | `pin21_symbol=G13/IIS_WS`；`pin21_external_net=GPIO19`；`pin22_symbol=G12/IIS_SK`；`pin22_external_net=GPIO27`；`resolved_host_map=null` |
| 电源 | BAT_4V 精确输出规格 | `pre_diode_net=VCC_4V`；`series_diode=D2 DSS34`；`post_diode_net=BAT_4V`；`tolerance=null`；`load_condition=null`；`measured_range=null` |
| 保护电路 | J4 外部 BAT/GND 供电边界 | `documented_external_input=J4 BAT/GND`；`schematic_input=J4 pin12 BAT_6V_OUT and pin1 GND`；`voltage_range=null`；`polarity_protection=not shown on J4 injection branch`；`overcurrent_protection=F1 bypassed`；`battery_parallel_rule=null` |
| 接口 | J1/J2 的 PORT.B/PORT.C 名称 | `J2_label=GROVE-B 4P`；`J2_signals=RXD,TXD`；`J1_label=GROVE-4P`；`J1_signals=GPIO36,GPIO26`；`J1_resolved_port=null` |

## 待确认事项

- `power.battery-pack-label-conflict`：电池块内部写有 4x1.2V，同时外部抽头写有 1x1.5V、2x1.5V、3x1.5V，主输出网络名为 BAT_6V_IN；正文称使用四节 AAA 干电池。当前资料无法确定量产产品允许的电芯化学体系和输入电压范围。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A1-B1 区电池块的 4x1.2V、分段 1.5V 与 BAT_6V_IN 标注）
- `analog.documented-gpio35-solder-state`：正文称 GPIO35 默认断开、焊接后才能读取电池电压；原理图在 R6/R7 中点与 GPIO35 之间标出 TP1，但没有给出焊桥封装、默认开短状态或装配选项。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B1-C1 区分压中点、TP1 与 GPIO35）
- `interface.m5-bus-label-conflict`：J3 符号内部将 pin21 标为 G13/IIS_WS、pin22 标为 G12/IIS_SK，但外部网络分别命名 GPIO19 和 GPIO27；对应主机 GPIO 映射无法仅由本页消除歧义。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 D4 区 J3 pin21/pin22 内部文字与右/左侧外部网络标签）
- `power.bat4-output-spec`：原理图用 VCC_4V 和 BAT_4V 命名转换器输出，并在两者之间串联 D2 DSS34；图中没有输出容差、负载条件或 D2 压降数据，因此 BAT_4V 的实际电压范围无法确定。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 A2-A3 区 MP1470 反馈、VCC_4V、D2 和 BAT_4V）
- `power.documented-external-supply-limits`：正文允许通过 12P 接口的 BAT/GND 外部供电，原理图确认 J4 pin12 BAT_6V_OUT 可进入 SW1/VIN，但没有标注允许电压、极性保护、过流保护或与电池并接时的操作限制。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 J4 pin12/pin1 与 A1 区 BAT_6V_OUT-SW1-VIN 及 Q1/F1 路径）
- `interface.grove-port-designation`：产品正文称提供 PORT.B 和 PORT.C；原理图明确把 J2 标为 GROVE-B 4P，但 J1 只标 GROVE-4P，没有明确写 PORT.C，因此 J1 的对外端口名称需由 PCB 丝印确认。（证据：图 23a1c26120c2 / 第 1 页 / 第 1 页 B4 区 J1 GROVE-4P 与 J2 GROVE-B 4P 标签）
- `review.battery-chemistry-input`：A122 量产产品允许使用 4x1.5V 一次性 AAA、4x1.2V 可充电 AAA，还是两者均可；MP1470 输入范围如何覆盖这些组合？；原因：电池块的 4x1.2V、分段 1.5V 和 BAT_6V_IN 标注彼此不一致，需要 BOM、结构和电气测试确认。
- `review.gpio35-solder-jumper`：TP1 在 PCB 上是测试点、焊桥还是 0Ω位，出厂默认状态是否确为开路？；原因：正文说明需要焊接，但原理图只给出 TP1，无法确定实际封装和默认装配状态。
- `review.m5-bus-host-map`：A122 面向的具体 M5 主机版本中，J3 pin21/pin22 应映射 G13/G12 还是 GPIO19/GPIO27？；原因：符号内部针脚名与外部网络名冲突，错误选择会影响 J4 和软件 GPIO 定义。
- `review.bat4-output-range`：A122 的 VCC_4V 设定值、D2 压降以及 BAT_4V 在空载和满载时的允许范围是什么？；原因：网络名不能替代额定值，原理图未给出容差、负载和测量条件。
- `review.external-supply-safety`：通过 J4 BAT_6V_OUT/GND 外部供电时，允许电压、极性、限流要求及是否必须移除电池或关闭 SW1？；原因：J4 注入支路绕过 Q1/F1，错误电压或与电池并接可能造成硬件风险。
- `review.grove-port-name`：J1 的板端丝印是否确认为 PORT.C，GPIO36/GPIO26 在目标主机上对应哪两个 Port C 信号？；原因：原理图只把 J2 明确标为 GROVE-B，J1 没有 PORT.C 标签。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `23a1c26120c242a6ed711a03afc7fa1b1db2a3b42bbdcbeefd8620c6c193fdd2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/533/SCH_Base_AAA_V1.0_sch_01.png` |

---

源文档：`zh_CN/base/base_aaa.md`

源文档 SHA-256：`7ba4fe4da562b492b63a9c258403e532430668b936ec693a6f1ef39b31a61c67`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
