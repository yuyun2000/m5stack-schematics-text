# Atomic RS485 Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic RS485 Base |
| SKU | A131 |
| 产品 ID | `atomic-rs485-base-ad1ee8db9696` |
| 源文档 | `zh_CN/atom/Atomic RS485 Base.md` |

## 概述

Atomic RS485 Base 使用 U1 SP3485EN-L/TR 在 3.3V 侧 RX/TX 与 RS485_A/RS485_B 之间完成收发转换，TX 通过 Q1 控制 U1 的 /RE 与 DE，RS-485 端配置偏置、端接焊位和三只 TVS 保护器件。电源部分由 U2 AOZ1282CI 将 J1 输入的 +12V 降压为 +5VIN，并通过 P2 向上层模块供电；U1 的 +3.3V 则来自 P1。J1 为 3.96 mm 四位端子，集中引出 RS485_B、RS485_A、12V+ 和接地的 12V-。

## 检索关键词

`Atomic RS485 Base`、`A131`、`SP3485EN-L/TR`、`AOZ1282CI`、`SS8050 Y1`、`SMAJ6.5CA-E3`、`B5819W SL`、`RS-485`、`RS485_A`、`RS485_B`、`RX`、`TX`、`/RE`、`DE`、`DI`、`RO`、`+12V`、`+5VIN`、`+3.3V`、`HDR_4P_3.96`、`120Ω/NC`、`4.7uH`、`J1`、`P1`、`P2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SP3485EN-L/TR | 3.3V 逻辑侧与 RS-485 差分总线之间的收发器 | 图 72fa3f8f2f70 / 第 1 页 / 页面左上功能区中央 U1，器件值 SP3485EN-L/TR，标有 RO、/RE、DE、DI、A、B、VCC、GND |
| Q1 | SS8050 Y1 | 由 TX 驱动并控制 U1 的 /RE 与 DE 共用节点 | 图 72fa3f8f2f70 / 第 1 页 / 页面左上功能区 Q1，器件值 SS8050 Y1，基极经 R5 接 TX，发射极接 GND |
| U2 | AOZ1282CI | 将 +12V 降压为 +5VIN 的开关稳压器 | 图 72fa3f8f2f70 / 第 1 页 / 页面左下电源区 U2，器件值 AOZ1282CI，标有 VIN、EN、BST、LX、FB、GND |
| D1 | SMAJ6.5CA-E3 | RS485_B 对 GND 的浪涌/瞬态保护 | 图 72fa3f8f2f70 / 第 1 页 / 页面上部 RS-485 保护区 D1，位于 RS485_B 与 GND 之间 |
| D2 | SMAJ6.5CA-E3 | RS485_B 与 RS485_A 之间的差模瞬态保护 | 图 72fa3f8f2f70 / 第 1 页 / 页面上部 RS-485 保护区 D2，跨接 RS485_B 与 RS485_A |
| D3 | SMAJ6.5CA-E3 | RS485_A 对 GND 的浪涌/瞬态保护 | 图 72fa3f8f2f70 / 第 1 页 / 页面上部 RS-485 保护区 D3，位于 RS485_A 与 GND 之间 |
| D4 | B5819W SL | AOZ1282CI 降压转换器 LX 开关节点的肖特基续流二极管 | 图 72fa3f8f2f70 / 第 1 页 / 页面左下电源区 D4，器件值 B5819W SL，连接 LX 开关节点与 GND |
| L1 | 4.7uH | AOZ1282CI 降压输出电感 | 图 72fa3f8f2f70 / 第 1 页 / 页面左下电源区 L1，标注 4.7uH，位于 LX 与 +5VIN 之间 |
| R4 | 120Ω/NC | 跨接 RS485_B 与 RS485_A 的可选端接电阻位置 | 图 72fa3f8f2f70 / 第 1 页 / 页面上部 RS-485 总线区 R4，跨接 B/A，阻值标注 120Ω/NC |
| J1 | HDR_4P_3.96 | RS485_B、RS485_A、12V+、12V- 四位外部端子 | 图 72fa3f8f2f70 / 第 1 页 / 页面右上 J1，器件值 HDR_4P_3.96，内部针脚标注 B、A、12V+、12V- |
| P1 | Header 5 | 上层模块的 +3.3V、RX、TX 逻辑侧接口 | 图 72fa3f8f2f70 / 第 1 页 / 页面右中 P1 Header 5，1 脚 +3.3V、2 脚 RX、3 脚 TX，4/5 脚 NC |
| P2 | Header 4 | 向上层模块提供 +5VIN 和 GND 的电源接口 | 图 72fa3f8f2f70 / 第 1 页 / 页面右中 P2 Header 4，3 脚 +5VIN、4 脚 GND，1/2 脚 NC |

## 系统结构

### Atomic RS485 Base 系统结构

电路由 U1 SP3485EN-L/TR 的 3.3V 逻辑到 RS-485 收发链路，以及 U2 AOZ1282CI 的 +12V 到 +5VIN 降压链路组成；两条链路分别连接 P1/P2 与外部端子 J1。

- 参数与网络：`logic_interface=P1:+3.3V,RX,TX`；`power_output_interface=P2:+5VIN,GND`；`field_interface=J1:RS485_B,RS485_A,12V+,12V-`；`transceiver=U1 SP3485EN-L/TR`；`buck_converter=U2 AOZ1282CI`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 整页：左上 U1 收发器区、左下 U2 电源区、右侧 J1/P1/P2 接口区

## 核心器件

### U1 SP3485EN-L/TR

U1 引脚标注为 1=RO、2=/RE、3=DE、4=DI、5=GND、6=A、7=B、8=VCC。

- 参数与网络：`reference=U1`；`part_number=SP3485EN-L/TR`；`pinout=1:RO,2:/RE,3:DE,4:DI,5:GND,6:A,7:B,8:VCC`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左上 U1 符号两侧的引脚名称与脚号

## 电源

### U1 3.3V 供电

U1 的 VCC 引脚 8 连接 +3.3V，GND 引脚 5 连接 GND；C1 100 nF 跨接 +3.3V 与 GND 作为本地去耦。

- 参数与网络：`vcc_pin=U1 pin 8`；`rail=+3.3V`；`ground_pin=U1 pin 5`；`decoupling_capacitor=C1`；`decoupling_nf=100`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左上 U1 pin 8 VCC、pin 5 GND 与 C1 100nF

### +12V 输入路径

J1 的 12V+ 端连接 +12V 网络，12V- 端连接 GND；+12V 网络直接连接 U2 的 VIN 引脚 5。

- 参数与网络：`input_connector=J1`；`positive_terminal=12V+`；`negative_terminal=12V-/GND`；`input_rail=+12V`；`converter_input=U2 pin 5 VIN`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面右上 J1 12V+/12V- 与页面左下 +12V-U2 VIN pin 5 网络

### +12V 输入滤波

C3 与 C4 均标注 10 uF、10%、35V，并分别跨接 +12V 与 GND。

- 参数与网络：`capacitors=C3,C4`；`capacitance_uf=10`；`tolerance_percent=10`；`voltage_rating_v=35`；`rail=+12V`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左下 +12V 输入端的 C3、C4 及 10uF (106) 10% 35V 标注

### U2 使能

U2 的 EN 引脚 4 通过 R7 100 kΩ 连接 +12V。

- 参数与网络：`enable_pin=U2 pin 4 EN`；`pullup_resistor=R7`；`pullup_resistance_ohm=100000`；`pullup_rail=+12V`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左下 U2 EN pin 4 与 R7 100KΩ 到 +12V 的连接

### U2 降压开关级

U2 的 BST 引脚 1 通过 C2 100 nF 连接 LX 开关节点；LX 引脚 6 连接 D4 B5819W SL 与 L1 4.7 uH，L1 的另一端形成 +5VIN。

- 参数与网络：`bootstrap_pin=U2 pin 1 BST`；`bootstrap_capacitor=C2 100nF`；`switch_pin=U2 pin 6 LX`；`catch_diode=D4 B5819W SL`；`inductor=L1 4.7uH`；`output_rail=+5VIN`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左下 U2 BST/LX、C2、D4、L1 与 +5VIN 开关级

### U2 反馈分压

U2 的 FB 引脚 3 连接 R8 与 R9 的中点；R8 51 kΩ 连接到 +5VIN，R9 10 kΩ 连接到 GND。

- 参数与网络：`feedback_pin=U2 pin 3 FB`；`upper_resistor=R8 51kΩ`；`lower_resistor=R9 10kΩ`；`sense_rail=+5VIN`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左下 U2 FB pin 3、R8 51KΩ、R9 10KΩ 与 +5VIN/GND 网络

### +5VIN 输出滤波

C5 10 uF 与 C6 100 nF 分别跨接 +5VIN 与 GND。

- 参数与网络：`bulk_capacitor=C5 10uF`；`high_frequency_capacitor=C6 100nF`；`rail=+5VIN`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左下 +5VIN 输出端 C5 10uF 与 C6 100nF 到 GND

## 接口

### J1 外部端子

J1 为 HDR_4P_3.96 四位端子，按图中自上而下的端子标注依次为 B、A、12V+、12V-；对应网络为 RS485_B、RS485_A、+12V 和 GND。

- 参数与网络：`reference=J1`；`part_number=HDR_4P_3.96`；`pin_labels=B,A,12V+,12V-`；`nets=RS485_B,RS485_A,+12V,GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面右上 J1 HDR_4P_3.96 端子及左侧网络标号

### P1 逻辑接口

P1 为 Header 5：1 脚连接 +3.3V，2 脚连接 RX，3 脚连接 TX，4 脚和 5 脚标为未连接。

- 参数与网络：`reference=P1`；`pinout=1:+3.3V,2:RX,3:TX,4:NC,5:NC`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面右中 P1 Header 5 的脚号、网络和 NC 标记

### P2 电源接口

P2 为 Header 4：1 脚和 2 脚标为未连接，3 脚连接 +5VIN，4 脚连接 GND。

- 参数与网络：`reference=P2`；`pinout=1:NC,2:NC,3:+5VIN,4:GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面右中 P2 Header 4 的脚号、+5VIN、GND 和 NC 标记

## 总线

### RS-485 差分链路

U1 的 B 引脚 7 连接 RS485_B，A 引脚 6 连接 RS485_A；两条网络继续连接到 J1 的 B 与 A 端子。

- 参数与网络：`transceiver=U1`；`b_pin=7`；`b_net=RS485_B`；`a_pin=6`；`a_net=RS485_A`；`connector=J1`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面上部 U1 A/B 引脚、RS485_A/RS485_B 网络标号及右上 J1 B/A 端子

### RS-485 总线偏置

R1 4.7 kΩ 将 RS485_B 连接到 GND，R6 4.7 kΩ 将 RS485_A 连接到 +3.3V。

- 参数与网络：`b_bias=R1 4.7kΩ to GND`；`a_bias=R6 4.7kΩ to +3.3V`；`b_net=RS485_B`；`a_net=RS485_A`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面上部 U1 A/B 右侧，R1 从 RS485_B 接 GND，R6 从 RS485_A 接 +3.3V

## GPIO 与控制信号

### RX 接收路径

U1 的 RO 引脚 1 通过 R2 1 kΩ 串联到 RX 网络，RX 网络连接 P1 的 2 脚。

- 参数与网络：`source=U1 pin 1 RO`；`series_resistor=R2`；`series_resistance_ohm=1000`；`net=RX`；`connector_pin=P1 pin 2`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左上 U1 pin 1 RO-R2-RX 链路及页面右中 P1 pin 2 RX

### TX 与收发方向控制

TX 网络由 P1 的 3 脚引出，经 R5 1 kΩ 接 Q1 基极；Q1 发射极接 GND，集电极连接 U1 的 /RE 引脚 2 与 DE 引脚 3 共用节点，该节点由 R3 4.7 kΩ 上拉到 +3.3V。

- 参数与网络：`tx_connector_pin=P1 pin 3`；`base_resistor=R5`；`base_resistance_ohm=1000`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U1 pin 2 /RE,U1 pin 3 DE`；`pullup_resistor=R3`；`pullup_resistance_ohm=4700`；`pullup_rail=+3.3V`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左上 TX-R5-Q1-R3 与 U1 /RE、DE 共用节点，以及页面右中 P1 pin 3 TX

## 保护电路

### RS-485 三点 TVS 保护

D1、D2、D3 均标注 SMAJ6.5CA-E3；D1 连接 RS485_B 与 GND，D2 跨接 RS485_B 与 RS485_A，D3 连接 RS485_A 与 GND。

- 参数与网络：`part_number=SMAJ6.5CA-E3`；`d1_path=RS485_B-GND`；`d2_path=RS485_B-RS485_A`；`d3_path=RS485_A-GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面上部 RS485_B/RS485_A 右侧 D1、D2、D3 保护网络

## 关键网络

### U1 DI 输入

U1 的 DI 引脚 4 直接连接 GND。

- 参数与网络：`reference=U1`；`pin=4`；`signal=DI`；`connected_net=GND`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 页面左上 U1 左侧 pin 4 DI 向下连接 GND

### 板级电源分配

+12V 从 J1 进入 U2 并转换为 +5VIN 后连接 P2 的 3 脚；P1 的 1 脚连接 +3.3V，并由该电源轨为 U1 供电。

- 参数与网络：`input_path=J1 12V+ -> +12V -> U2 VIN`；`output_path=U2/L1 -> +5VIN -> P2 pin 3`；`logic_supply_path=P1 pin 1 -> +3.3V -> U1 VCC`
- 证据：图 72fa3f8f2f70 / 第 1 页 / 整页电源网络：J1 12V+、U2 降压区、+5VIN/P2 与 +3.3V/P1/U1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic RS485 Base 系统结构 | `logic_interface=P1:+3.3V,RX,TX`；`power_output_interface=P2:+5VIN,GND`；`field_interface=J1:RS485_B,RS485_A,12V+,12V-`；`transceiver=U1 SP3485EN-L/TR`；`buck_converter=U2 AOZ1282CI` |
| 核心器件 | U1 SP3485EN-L/TR | `reference=U1`；`part_number=SP3485EN-L/TR`；`pinout=1:RO,2:/RE,3:DE,4:DI,5:GND,6:A,7:B,8:VCC` |
| 总线 | RS-485 差分链路 | `transceiver=U1`；`b_pin=7`；`b_net=RS485_B`；`a_pin=6`；`a_net=RS485_A`；`connector=J1` |
| GPIO 与控制信号 | RX 接收路径 | `source=U1 pin 1 RO`；`series_resistor=R2`；`series_resistance_ohm=1000`；`net=RX`；`connector_pin=P1 pin 2` |
| GPIO 与控制信号 | TX 与收发方向控制 | `tx_connector_pin=P1 pin 3`；`base_resistor=R5`；`base_resistance_ohm=1000`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U1 pin 2 /RE,U1 pin 3 DE`；`pullup_resistor=R3`；`pullup_resistance_ohm=4700`；`pullup_rail=+3.3V` |
| 关键网络 | U1 DI 输入 | `reference=U1`；`pin=4`；`signal=DI`；`connected_net=GND` |
| 电源 | U1 3.3V 供电 | `vcc_pin=U1 pin 8`；`rail=+3.3V`；`ground_pin=U1 pin 5`；`decoupling_capacitor=C1`；`decoupling_nf=100` |
| 总线 | RS-485 总线偏置 | `b_bias=R1 4.7kΩ to GND`；`a_bias=R6 4.7kΩ to +3.3V`；`b_net=RS485_B`；`a_net=RS485_A` |
| 总线 | RS-485 端接电阻 R4 | `reference=R4`；`nominal_resistance_ohm=120`；`schematic_marking=120Ω/NC`；`population_state=null` |
| 保护电路 | RS-485 三点 TVS 保护 | `part_number=SMAJ6.5CA-E3`；`d1_path=RS485_B-GND`；`d2_path=RS485_B-RS485_A`；`d3_path=RS485_A-GND` |
| 接口 | J1 外部端子 | `reference=J1`；`part_number=HDR_4P_3.96`；`pin_labels=B,A,12V+,12V-`；`nets=RS485_B,RS485_A,+12V,GND` |
| 接口 | P1 逻辑接口 | `reference=P1`；`pinout=1:+3.3V,2:RX,3:TX,4:NC,5:NC` |
| 接口 | P2 电源接口 | `reference=P2`；`pinout=1:NC,2:NC,3:+5VIN,4:GND` |
| 电源 | +12V 输入路径 | `input_connector=J1`；`positive_terminal=12V+`；`negative_terminal=12V-/GND`；`input_rail=+12V`；`converter_input=U2 pin 5 VIN` |
| 电源 | +12V 输入滤波 | `capacitors=C3,C4`；`capacitance_uf=10`；`tolerance_percent=10`；`voltage_rating_v=35`；`rail=+12V` |
| 电源 | U2 使能 | `enable_pin=U2 pin 4 EN`；`pullup_resistor=R7`；`pullup_resistance_ohm=100000`；`pullup_rail=+12V` |
| 电源 | U2 降压开关级 | `bootstrap_pin=U2 pin 1 BST`；`bootstrap_capacitor=C2 100nF`；`switch_pin=U2 pin 6 LX`；`catch_diode=D4 B5819W SL`；`inductor=L1 4.7uH`；`output_rail=+5VIN` |
| 电源 | U2 反馈分压 | `feedback_pin=U2 pin 3 FB`；`upper_resistor=R8 51kΩ`；`lower_resistor=R9 10kΩ`；`sense_rail=+5VIN` |
| 电源 | +5VIN 输出滤波 | `bulk_capacitor=C5 10uF`；`high_frequency_capacitor=C6 100nF`；`rail=+5VIN` |
| 关键网络 | 板级电源分配 | `input_path=J1 12V+ -> +12V -> U2 VIN`；`output_path=U2/L1 -> +5VIN -> P2 pin 3`；`logic_supply_path=P1 pin 1 -> +3.3V -> U1 VCC` |

## 待确认事项

- `bus.rs485_termination`：R4 跨接 RS485_B 与 RS485_A，标注值为 120Ω/NC；原理图无法确定成品是否实际装配该电阻。（证据：图 72fa3f8f2f70 / 第 1 页 / 页面上部 R4，跨接 RS485_B 与 RS485_A，文字标注 120Ω/NC）
- `review.r4_population`：R4 的 120Ω 端接电阻在当前量产版本中是否实际装配？；原因：原理图将 R4 标注为 120Ω/NC，只能确认存在该跨线端接位置，无法据此确认 BOM 装配状态。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `72fa3f8f2f70f0097edc759aa4941778e213c6dfa1130aabdcf80b0b8019cefa` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic RS485 Base/img-1f833240-7458-4d92-8120-c60a936e1c04.webp` |

---

源文档：`zh_CN/atom/Atomic RS485 Base.md`

源文档 SHA-256：`9f6e136b1e9c56c9c4b0319249f46b9b21f936d2f44ce8ee883759a50dc1ece2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
