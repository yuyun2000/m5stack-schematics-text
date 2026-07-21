# Atom Socket-CN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Socket-CN |
| SKU | K055-CN |
| 产品 ID | `atom-socket-cn-7f11d3b719f7` |
| 源文档 | `zh_CN/atom/atom_socket_cn.md` |

## 概述

两张原理图分别覆盖 Atom Socket-CN 的低压控制板和市电计量/继电器板。控制板由 RPD5W05E102SR 电源模块生成 VCC，ATOM 的 G22 接 RX、G23 经 R1 驱动 Relay，S1 提供 SW 输入，Q1/LED1 形成继电器驱动状态链，并通过 J1、J3 引出信号。市电板由 K1 切换 AC_L_IN 到 AC_L_OUT，HLW8032 通过中性线分流与火线高阻分压采样，TX 经 EL357N 光耦送到 VCC_MCU 域；U2 MP150GJ-Z 生成以 GND_8032/AC_N_IN 为参考的 VCC_8032。

## 检索关键词

`Atom Socket-CN`、`K055-CN`、`HLW8032`、`RPD5W05E102SR`、`MP150GJ-Z`、`EL357N(C)(TA)-G`、`932-5VDC-SL-AHG`、`AC_L_IN`、`AC_L_OUT`、`AC_N_IN`、`AC_N_OUT`、`L_SLP`、`VCC`、`VCC_MCU`、`VCC_8032`、`GND_8032`、`Relay`、`RX`、`SW`、`G22`、`G23`、`ATOM`、`S8050`、`TS-1157-B-B`、`A1002WR-S-4P`、`GROVE`、`current shunt`、`470K voltage divider`、`optocoupler UART`、`FUSE 15A250V`、`EARTH`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| PWR1 (control board) | RPD5W05E102SR | 从 AC_L_IN/AC_N_IN 取电并向低压控制板输出 VCC/GND 的电源模块 | 图 d75ab747fba6 / 第 1 页 / 第一页左中 PWR1 RPD5W05E102SR 电源模块，1/2 脚 AC_L_IN/AC_N_IN，3/4 脚输出 |
| ATOM (control board) | 未标注 | 九针 Atom 主控插座，连接 3.3V、VCC、GND、RX 和 Relay | 图 d75ab747fba6 / 第 1 页 / 第一页右中蓝色 ATOM 4P+5P 排针，1-9 脚及 G21/G25/5V/GND/G33/G23/G19/G22/3V3 |
| S1 | TS-1157-B-B | 将 SW 输入按下接地的本地按键 | 图 d75ab747fba6 / 第 1 页 / 第一页上中 S1 TS-1157-B-B，左接 GND，右接 SW |
| Q1/LED1 (control board) | S8050 / 翠绿色 LED | Relay 控制输入驱动的晶体管与 VCC 侧状态指示电路，并连接板间 J1 | 图 d75ab747fba6 / 第 1 页 / 第一页中下 Relay-R2-Q1 S8050 与 VCC-R4-LED1 绿色指示支路 |
| J1 (control board) | A1002WR-S-4P | 控制板四针板间接口，引出 GND、VCC、Q1 集电极节点与 RX | 图 d75ab747fba6 / 第 1 页 / 第一页中央 J1 A1002WR-S-4P，1 GND、2 VCC、3 Q1/LED 节点、4 RX |
| J3 (control board) | GROVE | 外部 SW、Relay、VCC、GND 四针控制接口 | 图 d75ab747fba6 / 第 1 页 / 第一页右下 J3 黑色立式直插 GROVE，IO2/IO1/5V/GND |
| FUSE (meter board) | 2009T15A250V | AC_L_IN 到 L_SLP 的火线串联保险丝 | 图 d7d943bc4ec3 / 第 1 页 / 第二页顶部 AC_L_IN 后的 FUSE，标注 2009T15A250V |
| K1 | 932-5VDC-SL-AHG | 由 Relay/VCC_MCU 线圈控制，将 L_SLP 切换到 AC_L_OUT | 图 d7d943bc4ec3 / 第 1 页 / 第二页顶部 K1 932-5VDC-SL-AHG，触点位于 L_SLP-AC_L_OUT，线圈位于 Relay-VCC_MCU |
| U1 (meter board) | HLW8032 | 市电电流、电压采样与 TX 串口输出的电能计量 IC | 图 d7d943bc4ec3 / 第 1 页 / 第二页中央 U1 HLW8032，VDD/I_P/I_N/V_P/RX/PF/TX/GND 八脚 |
| R1 (meter board) | MMS251230FR001MZ | 串接 AC_N_OUT 与 AC_N_IN 的电流采样分流器 | 图 d7d943bc4ec3 / 第 1 页 / 第二页左中 R1 垂直跨接 AC_N_OUT/AC_N_IN，标注 MMS251230FR001MZ |
| IC1 | EL357N(C)(TA)-G | 隔离 HLW8032 TX 与 VCC_MCU/GND 低压接口域 | 图 d7d943bc4ec3 / 第 1 页 / 第二页右中 IC1 EL357N(C)(TA)-G，输入接 VCC_8032/TX，输出接 VCC_MCU/GND/J1 |
| U2 (meter board) | MP150GJ-Z | 从 AC_L_IN/AC_N_IN 生成 VCC_8032 的非隔离离线电源控制器 | 图 d7d943bc4ec3 / 第 1 页 / 第二页左下 U2 MP150GJ-Z，DRAIN/VCC/FB/SOURCE 与离线降压外围 |
| P2 (meter board) | PAD DNP | 连接两处 EARTH 的可选接地焊盘 | 图 d7d943bc4ec3 / 第 1 页 / 第二页左上 P2 PAD，标注 DNP，下接两处 EARTH |
| J1 (meter board) | A1002WR-S-4P | 计量板四针接口，引出光耦输出、Relay、VCC_MCU 与 GND | 图 d7d943bc4ec3 / 第 1 页 / 第二页右中 J1 A1002WR-S-4P，1 光耦输出、2 Relay、3 VCC_MCU、4 GND |

## 系统结构

### 双板系统结构

第一页覆盖 ATOM、按键、Grove、控制板 AC-DC 电源和晶体管驱动；第二页覆盖市电继电器、HLW8032 计量、光耦串口与 VCC_8032 非隔离电源，两页各自使用 J1 四针接口。

- 参数与网络：`control_board_asset=d75ab747fba6839907d0caa106c7f55450b37941dc4be724cfae6320d5d90f93`；`meter_board_asset=d7d943bc4ec374357096b395fc6218fc428a99ecdc50c46b6bf89c90637e28f3`；`interconnect_designator=J1`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页整页低压控制板功能与 J1; 图 d7d943bc4ec3 / 第 1 页 / 第二页整页计量/继电器板功能与 J1

## 核心器件

### K1 触点额定值可见性

第二页给出 K1 料号 932-5VDC-SL-AHG 和 5VDC 线圈标识，但没有在原理图上标注触点的电压、电流或负载类别额定值。

- 参数与网络：`relay=K1 932-5VDC-SL-AHG`；`coil_marking=5VDC`；`contact_voltage_rating_shown=false`；`contact_current_rating_shown=false`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页顶部 K1 符号与 932-5VDC-SL-AHG 文字

## 电源

### 控制板 VCC 电源

PWR1 RPD5W05E102SR 的输出 3 脚经 D1 SS34 连接 VCC，4 脚接 GND，R6 3.3k 从 VCC 接 GND；VCC 连接 ATOM 5V 3 脚。

- 参数与网络：`module=PWR1 RPD5W05E102SR`；`positive_output=pin 3 -> D1 SS34 -> VCC`；`negative_output=pin 4 -> GND`；`bleeder=R6 3.3k`；`atom_power=VCC -> ATOM pin 3 5V`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页 PWR1 3/4 脚、D1、R6、VCC 与 ATOM 5V

### 火线保险与继电器触点

第二页 AC_L_IN 先经过 FUSE 2009T15A250V 形成 L_SLP，L_SLP 再经 K1 常开触点输出 AC_L_OUT。

- 参数与网络：`input=AC_L_IN`；`fuse=2009T15A250V`；`protected_live=L_SLP`；`switch=K1 contact`；`output=AC_L_OUT`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页顶部 AC_L_IN-FUSE-L_SLP-K1-AC_L_OUT

### HLW8032 供电

U1 HLW8032 VDD 1 脚接 VCC_8032，GND 5 脚接 GND_8032，C10 100nF/50V/10% 跨接 VCC_8032 与 GND_8032。

- 参数与网络：`vdd=pin 1 -> VCC_8032`；`ground=pin 5 -> GND_8032`；`decoupling=C10 100nF/50V/10%`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页中央 U1 VDD/GND 与 C10

### MP150GJ-Z 市电输入

AC_L_IN 经 R11 47R/1%/1W 和 D1 US1JW 进入 U2 DRAIN 5 脚，C4 EGD2GM3R3E120T 跨接 DRAIN 节点与 AC_N_IN；U2 SOURCE 3/4 脚以 GND_8032/AC_N_IN 为参考。

- 参数与网络：`live_path=AC_L_IN -> R11 47R/1%/1W -> D1 US1JW -> U2 DRAIN pin 5`；`input_component=C4 EGD2GM3R3E120T across drain and AC_N_IN`；`source_pins=3,4`；`reference=GND_8032 / AC_N_IN`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页左下 AC_L_IN-R11-D1-U2 与 C4/AC_N_IN

### VCC_8032 非隔离电源输出

U2 MP150GJ-Z 的外围通过 D3 US1JW、D4 S1MD3、L1 CD43YP0403-102M、C8 100uF/10V/5X7、C9 与 R14 1.6K/0603/1% 形成 VCC_8032 输出，回路参考 GND_8032。

- 参数与网络：`controller=U2 MP150GJ-Z`；`diodes=D3 US1JW; D4 S1MD3`；`inductor=L1 CD43YP0403-102M`；`bulk_capacitor=C8 100uF/10V/5X7`；`load_resistor=R14 1.6K/0603/1%`；`output=VCC_8032 referenced to GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页下部 U2 外围、D3/D4、L1、C8/C9、R14 与 VCC_8032

### 计量电源域参考

GND_8032 在第二页直接连接 AC_N_IN，VCC_8032、HLW8032 采样和 MP150GJ-Z 电源均以该节点为参考；IC1 位于 VCC_8032/GND_8032 与 VCC_MCU/GND 之间。

- 参数与网络：`meter_ground=GND_8032`；`mains_connection=GND_8032 -> AC_N_IN`；`isolating_component=IC1 EL357N(C)(TA)-G`；`low_voltage_domain=VCC_MCU/GND`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页 AC_N_IN/GND_8032、U1/U2 与 IC1 两侧供电域

## 接口

### 控制板 AC 输入

第一页 P1 的 1 脚接 AC_N_IN，2 脚接 AC_L_IN；PWR1 的 1 脚接 AC_L_IN，2 脚接 AC_N_IN。

- 参数与网络：`p1_pin1=AC_N_IN`；`p1_pin2=AC_L_IN`；`pwr1_pin1=AC_L_IN`；`pwr1_pin2=AC_N_IN`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页左侧 P1 与 PWR1 的 AC_N_IN/AC_L_IN 引脚

### 控制板 J1

第一页 J1 A1002WR-S-4P 的 1 脚接 GND，2 脚接 VCC，3 脚接 Q1 集电极/LED1 节点，4 脚接 RX。

- 参数与网络：`pin1=GND`；`pin2=VCC`；`pin3=Q1 collector / LED1 node`；`pin4=RX`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页中央 J1 1-4 脚四条网络

### J3 Grove 外部控制

J3 的 4 脚 IO2 接 SW，3 脚 IO1 经 R5 1k/1% 接 Relay，2 脚 5V 接 VCC，1 脚接 GND。

- 参数与网络：`pin4=IO2 -> SW`；`pin3=IO1 -> R5 1k/1% -> Relay`；`pin2=5V -> VCC`；`pin1=GND`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页右下 J3 GROVE 与 SW/Relay/VCC/GND

### 计量板 J1

第二页 J1 A1002WR-S-4P 的 1 脚接 IC1 隔离输出，2 脚接 Relay，3 脚接 VCC_MCU，4 脚接 GND。

- 参数与网络：`pin1=IC1 isolated output`；`pin2=Relay`；`pin3=VCC_MCU`；`pin4=GND`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页右中 J1 1-4 脚与光耦输出/Relay/VCC_MCU/GND

### 两页 J1 针脚定义

控制板 J1 定义为 1 GND、2 VCC、3 Q1 集电极、4 RX；计量板 J1 定义为 1 光耦输出、2 Relay、3 VCC_MCU、4 GND。当前两页没有单独给出线束端到端针号映射图。

- 参数与网络：`control_board=1 GND; 2 VCC; 3 Q1 collector; 4 RX`；`meter_board=1 optocoupler output; 2 Relay; 3 VCC_MCU; 4 GND`；`cable_mapping_shown=false`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页 J1 本地 1-4 脚; 图 d7d943bc4ec3 / 第 1 页 / 第二页 J1 本地 1-4 脚

## 总线

### HLW8032 TX 光耦隔离

U1 TX 6 脚连接 IC1 输入 2 脚，IC1 输入 1 脚经 R4 470R/1% 接 VCC_8032；输出 4 脚连接 J1 1 脚并经 R15 1.6K/1% 上拉到 VCC_MCU，输出 3 脚经 R5 3.3K/1% 接 GND。

- 参数与网络：`meter_tx=U1 TX pin 6 -> IC1 pin 2`；`input_supply=VCC_8032 -> R4 470R/1% -> IC1 pin 1`；`isolated_output=IC1 pin 4 -> J1 pin 1; R15 1.6K/1% to VCC_MCU`；`emitter_path=IC1 pin 3 -> R5 3.3K/1% -> GND`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页 U1 TX-R4-IC1 EL357N-R15/R5-J1 pin 1

## GPIO 与控制信号

### ATOM 控制映射

第一页 ATOM 9 脚接 3.3V，8 脚 G22 接 RX，4 脚 G23 经 R1 1k/1% 接 Relay，3 脚 5V 接 VCC，1 脚接 GND；G21、G25、G19、G33 在该页 ATOM 方框处未连接。

- 参数与网络：`pin9=3V3 -> 3.3V`；`pin8=G22 -> RX`；`pin4=G23 -> R1 1k/1% -> Relay`；`pin3=5V -> VCC`；`pin1=GND`；`unconnected=G21/G25/G19/G33`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页右中 ATOM 1-9 脚及 RX/Relay/VCC/3.3V/GND 网络

### 本地 SW 按键

S1 TS-1157-B-B 按键连接 SW 与 GND，R3 3.3K/1% 将 SW 上拉到 3.3V，C1 100nF/50V/10% 从 SW 接 GND。

- 参数与网络：`switch=S1 TS-1157-B-B`；`signal=SW`；`pullup=R3 3.3K/1% to 3.3V`；`capacitor=C1 100nF/50V/10% to GND`；`active_connection=GND`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页上中 S1、R3、C1 与 SW/GND/3.3V

## 保护电路

### EARTH 可选焊盘

第二页 P2 标注 PAD 和 DNP，并连接两处 EARTH 符号。

- 参数与网络：`reference=P2`；`population=DNP`；`connection=two EARTH pads`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页左上 P2 PAD DNP 与两个 EARTH

## 关键网络

### 控制板 Relay 晶体管链路

Relay 网络连接 Q1 S8050 基极并由 R2 3.3K/1% 下拉到 GND；Q1 发射极接 GND，集电极连接 J1 3 脚和 LED1 负端，LED1 正端经 R4 3.3K/1% 接 VCC。

- 参数与网络：`input=Relay`；`transistor=Q1 S8050`；`base_pulldown=R2 3.3K/1%`；`collector_outputs=J1 pin 3; LED1 cathode`；`indicator_supply=VCC -> R4 3.3K/1% -> LED1`
- 证据：图 d75ab747fba6 / 第 1 页 / 第一页中下 Relay-R2-Q1 与 VCC-R4-LED1-J1 pin 3

### K1 线圈与续流

K1 932-5VDC-SL-AHG 线圈连接 Relay 与 VCC_MCU，D2 S1MD3 跨接在线圈两端。

- 参数与网络：`relay=K1 932-5VDC-SL-AHG`；`coil_end_a=Relay`；`coil_end_b=VCC_MCU`；`flyback_diode=D2 S1MD3`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页顶部 K1 线圈、Relay/VCC_MCU 与 D2

## 模拟电路

### 中性线电流分流器

R1 MMS251230FR001MZ 跨接 AC_N_OUT 与 AC_N_IN，AC_N_IN 侧节点同时作为 GND_8032。

- 参数与网络：`component=R1 MMS251230FR001MZ`；`high_side=AC_N_OUT`；`low_side=AC_N_IN / GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页左中 AC_N_OUT-R1-AC_N_IN/GND_8032

### HLW8032 电流差分采样

AC_N_OUT 经 R2 1K/1% 连接 U1 I_P 2 脚，AC_N_IN 经 R3 1K/1% 连接 I_N 3 脚；C1/C2 各 33nF/16V/10% 分别从两条采样线接 GND_8032。

- 参数与网络：`positive_input=AC_N_OUT -> R2 1K/1% -> I_P pin 2`；`negative_input=AC_N_IN -> R3 1K/1% -> I_N pin 3`；`filters=C1/C2 33nF/16V/10% to GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页左中 R2/R3、C1/C2 到 U1 I_P/I_N

### HLW8032 火线电压采样

L_SLP 经 R6、R7、R8、R9 四只 470K/1% 串联到 U1 V_P 4 脚节点，该节点通过 R10 1K/1% 与 C3 100nF/50V/10% 接 GND_8032。

- 参数与网络：`source=L_SLP`；`high_side_divider=R6-R9 470K/1% series`；`input=U1 V_P pin 4`；`low_side=R10 1K/1% to GND_8032`；`filter=C3 100nF/50V/10% to GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 第二页左中下 L_SLP-R6/R7/R8/R9-V_P 与 R10/C3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 双板系统结构 | `control_board_asset=d75ab747fba6839907d0caa106c7f55450b37941dc4be724cfae6320d5d90f93`；`meter_board_asset=d7d943bc4ec374357096b395fc6218fc428a99ecdc50c46b6bf89c90637e28f3`；`interconnect_designator=J1` |
| 接口 | 控制板 AC 输入 | `p1_pin1=AC_N_IN`；`p1_pin2=AC_L_IN`；`pwr1_pin1=AC_L_IN`；`pwr1_pin2=AC_N_IN` |
| 电源 | 控制板 VCC 电源 | `module=PWR1 RPD5W05E102SR`；`positive_output=pin 3 -> D1 SS34 -> VCC`；`negative_output=pin 4 -> GND`；`bleeder=R6 3.3k`；`atom_power=VCC -> ATOM pin 3 5V` |
| GPIO 与控制信号 | ATOM 控制映射 | `pin9=3V3 -> 3.3V`；`pin8=G22 -> RX`；`pin4=G23 -> R1 1k/1% -> Relay`；`pin3=5V -> VCC`；`pin1=GND`；`unconnected=G21/G25/G19/G33` |
| GPIO 与控制信号 | 本地 SW 按键 | `switch=S1 TS-1157-B-B`；`signal=SW`；`pullup=R3 3.3K/1% to 3.3V`；`capacitor=C1 100nF/50V/10% to GND`；`active_connection=GND` |
| 关键网络 | 控制板 Relay 晶体管链路 | `input=Relay`；`transistor=Q1 S8050`；`base_pulldown=R2 3.3K/1%`；`collector_outputs=J1 pin 3; LED1 cathode`；`indicator_supply=VCC -> R4 3.3K/1% -> LED1` |
| 接口 | 控制板 J1 | `pin1=GND`；`pin2=VCC`；`pin3=Q1 collector / LED1 node`；`pin4=RX` |
| 接口 | J3 Grove 外部控制 | `pin4=IO2 -> SW`；`pin3=IO1 -> R5 1k/1% -> Relay`；`pin2=5V -> VCC`；`pin1=GND` |
| 电源 | 火线保险与继电器触点 | `input=AC_L_IN`；`fuse=2009T15A250V`；`protected_live=L_SLP`；`switch=K1 contact`；`output=AC_L_OUT` |
| 关键网络 | K1 线圈与续流 | `relay=K1 932-5VDC-SL-AHG`；`coil_end_a=Relay`；`coil_end_b=VCC_MCU`；`flyback_diode=D2 S1MD3` |
| 保护电路 | EARTH 可选焊盘 | `reference=P2`；`population=DNP`；`connection=two EARTH pads` |
| 模拟电路 | 中性线电流分流器 | `component=R1 MMS251230FR001MZ`；`high_side=AC_N_OUT`；`low_side=AC_N_IN / GND_8032` |
| 模拟电路 | HLW8032 电流差分采样 | `positive_input=AC_N_OUT -> R2 1K/1% -> I_P pin 2`；`negative_input=AC_N_IN -> R3 1K/1% -> I_N pin 3`；`filters=C1/C2 33nF/16V/10% to GND_8032` |
| 模拟电路 | HLW8032 火线电压采样 | `source=L_SLP`；`high_side_divider=R6-R9 470K/1% series`；`input=U1 V_P pin 4`；`low_side=R10 1K/1% to GND_8032`；`filter=C3 100nF/50V/10% to GND_8032` |
| 电源 | HLW8032 供电 | `vdd=pin 1 -> VCC_8032`；`ground=pin 5 -> GND_8032`；`decoupling=C10 100nF/50V/10%` |
| 总线 | HLW8032 TX 光耦隔离 | `meter_tx=U1 TX pin 6 -> IC1 pin 2`；`input_supply=VCC_8032 -> R4 470R/1% -> IC1 pin 1`；`isolated_output=IC1 pin 4 -> J1 pin 1; R15 1.6K/1% to VCC_MCU`；`emitter_path=IC1 pin 3 -> R5 3.3K/1% -> GND` |
| 接口 | 计量板 J1 | `pin1=IC1 isolated output`；`pin2=Relay`；`pin3=VCC_MCU`；`pin4=GND` |
| 电源 | MP150GJ-Z 市电输入 | `live_path=AC_L_IN -> R11 47R/1%/1W -> D1 US1JW -> U2 DRAIN pin 5`；`input_component=C4 EGD2GM3R3E120T across drain and AC_N_IN`；`source_pins=3,4`；`reference=GND_8032 / AC_N_IN` |
| 电源 | VCC_8032 非隔离电源输出 | `controller=U2 MP150GJ-Z`；`diodes=D3 US1JW; D4 S1MD3`；`inductor=L1 CD43YP0403-102M`；`bulk_capacitor=C8 100uF/10V/5X7`；`load_resistor=R14 1.6K/0603/1%`；`output=VCC_8032 referenced to GND_8032` |
| 电源 | 计量电源域参考 | `meter_ground=GND_8032`；`mains_connection=GND_8032 -> AC_N_IN`；`isolating_component=IC1 EL357N(C)(TA)-G`；`low_voltage_domain=VCC_MCU/GND` |
| 接口 | 两页 J1 针脚定义 | `control_board=1 GND; 2 VCC; 3 Q1 collector; 4 RX`；`meter_board=1 optocoupler output; 2 Relay; 3 VCC_MCU; 4 GND`；`cable_mapping_shown=false` |
| 核心器件 | K1 触点额定值可见性 | `relay=K1 932-5VDC-SL-AHG`；`coil_marking=5VDC`；`contact_voltage_rating_shown=false`；`contact_current_rating_shown=false` |

## 待确认事项

- `review.interboard_cable_mapping`：控制板 J1 与计量板 J1 的实际线束是 1↔4、2↔3 的反向连接，还是采用其他针号映射？；原因：两页分别给出本地 J1 针脚，但没有端到端线束图，不能仅按同名连接器假定同针直连。
- `review.relay_contact_rating`：K1 实装继电器的 AC/DC 触点额定值、负载类别和安全降额要求是什么？；原因：原理图只给出继电器料号与 5VDC 线圈信息，未给出触点额定值；市电负载能力必须由当前料号资料和硬件版本确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d75ab747fba6839907d0caa106c7f55450b37941dc4be724cfae6320d5d90f93` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_01.webp` |
| 2 | 1 | `d7d943bc4ec374357096b395fc6218fc428a99ecdc50c46b6bf89c90637e28f3` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_02.webp` |

---

源文档：`zh_CN/atom/atom_socket_cn.md`

源文档 SHA-256：`ebf27ce15bc032873be2d370a5673c2f665f1c3bff670a13f7d2a96d24b11707`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
