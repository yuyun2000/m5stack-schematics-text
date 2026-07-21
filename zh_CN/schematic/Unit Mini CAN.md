# Unit Mini CAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini CAN |
| SKU | U179 |
| 产品 ID | `unit-mini-can-51ef4fa38658` |
| 源文档 | `zh_CN/unit/Unit-Mini CAN.md` |

## 概述

Unit Mini CAN 以 TJA1051T/3（U3）在 Grove 侧的 CAN_Tx/CAN_Rx 与端子侧的 CAN_H/CAN_L 之间完成 CAN 物理层转换，收发器主电源为 VCC_5V，VIO 为 VCC_3V3。外部 HPWR+ 经 SMF30CA 防护和 ME3116 降压产生 VCC_5V，MST5333 再由 VCC_5V 生成 VCC_3V3。CAN_H/CAN_L 在 JP1 引出，并配置 120R 跨线电阻和两路 PESD5V0L1BA 对地保护。

## 检索关键词

`Unit Mini CAN`、`U179`、`TJA1051T/3`、`ME3116`、`MST5333`、`CAN`、`CAN_Tx`、`CAN_Rx`、`CAN_H`、`CAN_L`、`HPWR+`、`VCC_5V`、`VCC_3V3`、`GROVE`、`JP1`、`SMF30CA`、`PESD5V0L1BA`、`LESD3Z5.0CMT1G`、`B5819W SL`、`DSS34`、`120R`、`36.8uH`、`White LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME3116 | 将 HPWR+ 降压为 VCC_5V 的开关稳压器 | 图 848eb0125f17 / 第 1 页 / B2 区域 U1：ME3116，VIN/EN/GND/BST/LX/FB 引脚及其外围电路 |
| U2 | MST5333 | 将 VCC_5V 转换为 VCC_3V3 的三脚稳压器 | 图 848eb0125f17 / 第 1 页 / B4 区域 U2：MST5333，VIN 接 VCC_5V，VOUT 输出 VCC_3V3，GND 接地 |
| U3 | TJA1051T/3 | CAN 收发器，连接 CAN_Tx/CAN_Rx 与 CAN_H/CAN_L | 图 848eb0125f17 / 第 1 页 / C2 区域 U3：TJA1051T/3，TXD/RXD、CANH/CANL、VCC/VIO、GND/S 引脚 |
| GROVE | 未标注 | 4 Pin 逻辑与 5V 电源接口，引出 CAN_Rx、CAN_Tx、VCC_5V 和 GND | 图 848eb0125f17 / 第 1 页 / C1 区域 GROVE 符号：IO2/IO1/5V/GND 对应 CAN_Rx/CAN_Tx/VCC_5V/GND |
| JP1 | 未标注 | 4 Pin CAN 与宽压电源端子，引出 CAN_H、CAN_L、HPWR+ 和 GND | 图 848eb0125f17 / 第 1 页 / C4 区域 JP1：4/3/2/1 脚分别连接 CAN_H/CAN_L/HPWR+/GND |
| D3 | SMF30CA | HPWR+ 输入对 GND 的瞬态电压抑制器件 | 图 848eb0125f17 / 第 1 页 / B1 区域 HPWR+ 输入：D3 SMF30CA 跨接 HPWR+ 与 GND |
| C8 | 4.7uF/35V | HPWR+ 输入滤波电容 | 图 848eb0125f17 / 第 1 页 / B1 区域 U1 左侧：C8 4.7uF/35V 跨接 HPWR+ 与 GND |
| R2 | 100K | 从 HPWR+ 到 U1 EN 的使能上拉电阻 | 图 848eb0125f17 / 第 1 页 / B1-B2 区域：R2 100K 位于 HPWR+ 与 U1.4 EN 之间 |
| C7 | 100nF | U1 BST 与 LX 开关节点之间的自举电容 | 图 848eb0125f17 / 第 1 页 / B2 区域 U1 右上：C7 100nF 连接 U1.1 BST 与 LX/L1 左侧节点 |
| D2 | B5819W SL | ME3116 开关节点对 GND 的二极管 | 图 848eb0125f17 / 第 1 页 / B2 区域 C7 右侧：D2 B5819W SL 位于 LX/L1 左侧节点与 GND 之间 |
| L1 | 36.8uH/3012 | ME3116 降压级输出电感 | 图 848eb0125f17 / 第 1 页 / B2 区域 U1.6 LX 与 VCC_5V 之间：L1 标注 36.8uH/3012 |
| D4 | DSS34 | ME3116 降压输出网络中的 DSS34 二极管 | 图 848eb0125f17 / 第 1 页 / B2 区域 L1 右侧 VCC_5V 节点上方：D4 标注 DSS34 |
| R3 | 52.3K | VCC_5V 到 U1 FB 的反馈上臂电阻 | 图 848eb0125f17 / 第 1 页 / B2 区域 U1.3 FB 右侧：R3 52.3K 连接 FB 与 VCC_5V |
| R4 | 10K | U1 FB 到 GND 的反馈下臂电阻 | 图 848eb0125f17 / 第 1 页 / B2-C2 区域 U1.3 FB 下方：R4 10K 接 GND |
| C10 | 100pF | 并联在 U1 反馈上臂的补偿电容 | 图 848eb0125f17 / 第 1 页 / B2-C2 区域：C10 100pF 与 R3 并联在 FB 和 VCC_5V 之间 |
| C9 | 10uF | VCC_5V 降压输出滤波电容 | 图 848eb0125f17 / 第 1 页 / B2-C2 区域 L1 右侧：C9 10uF 跨接 VCC_5V 与 GND |
| C6 | 10uF/16V | VCC_5V 对 GND 的滤波电容 | 图 848eb0125f17 / 第 1 页 / B3 区域：C6 10uF/16V 跨接 VCC_5V 与 GND |
| D1 | LESD3Z5.0CMT1G | VCC_5V 对 GND 的 ESD/瞬态保护器件 | 图 848eb0125f17 / 第 1 页 / B3 区域 C6 右侧：D1 LESD3Z5.0CMT1G 跨接 VCC_5V 与 GND |
| C3 | 10uF | U2 VIN 的 VCC_5V 输入电容 | 图 848eb0125f17 / 第 1 页 / B3-B4 区域 U2 左侧：C3 10uF 跨接 VCC_5V 与 GND |
| C4 | 10uF | U2 VOUT 的 VCC_3V3 输出电容 | 图 848eb0125f17 / 第 1 页 / B4 区域 U2 右侧：C4 10uF 跨接 VCC_3V3 与 GND |
| LED1 | White | VCC_3V3 白色电源指示 LED | 图 848eb0125f17 / 第 1 页 / B4 区域 U2 输出右侧：LED1 标注 White，位于 VCC_3V3 指示支路 |
| R5 | 1K | LED1 的串联限流电阻 | 图 848eb0125f17 / 第 1 页 / B4 区域：R5 1K 与 LED1 串联在 VCC_3V3 和 GND 之间 |
| C1 | 100nF | U3 VCC 的 VCC_5V 去耦电容 | 图 848eb0125f17 / 第 1 页 / C2 区域 U3 左上：C1 100nF 跨接 VCC_5V 与 GND |
| C2 | 100nF | U3 VIO 的 VCC_3V3 去耦电容 | 图 848eb0125f17 / 第 1 页 / C3 区域 U3 右上：C2 100nF 跨接 VCC_3V3 与 GND |
| R1 | 120R | CAN_H 与 CAN_L 之间的固定终端电阻 | 图 848eb0125f17 / 第 1 页 / C3 区域 CAN 保护网络：R1 120R 竖直跨接 CAN_H 与 CAN_L |
| DZ1 | PESD5V0L1BA | CAN_H 对 GND 的 ESD 保护器件 | 图 848eb0125f17 / 第 1 页 / C3 区域 R1 右侧：DZ1 PESD5V0L1BA 连接 CAN_H 与 GND |
| DZ2 | PESD5V0L1BA | CAN_L 对 GND 的 ESD 保护器件 | 图 848eb0125f17 / 第 1 页 / C3 区域 R1 右侧：DZ2 PESD5V0L1BA 连接 CAN_L 与 GND |

## 系统结构

### Unit Mini CAN

U3 TJA1051T/3 连接 Grove 侧 CAN_Tx/CAN_Rx 与 JP1 侧 CAN_H/CAN_L；HPWR+ 经 U1 生成 VCC_5V，U2 再由 VCC_5V 生成 VCC_3V3。

- 参数与网络：`can_transceiver=U3 TJA1051T/3`；`buck_regulator=U1 ME3116`；`3v3_regulator=U2 MST5333`；`logic_interface=GROVE`；`bus_interface=JP1`
- 证据：图 848eb0125f17 / 第 1 页 / B1-B4 与 C1-C4：U1/U2 电源链、U3 收发器、GROVE 和 JP1 的同名网络

## 电源

### U1 ME3116 输入与使能

U1 的 5 脚 VIN 接 HPWR+，2 脚 GND 接地；4 脚 EN 通过 R2 100K 接 HPWR+。

- 参数与网络：`vin=U1.5 HPWR+`；`ground=U1.2 GND`；`enable=U1.4 EN via R2 100K to HPWR+`
- 证据：图 848eb0125f17 / 第 1 页 / B1-B2 区域 U1 左侧：VIN/EN/GND 引脚及 HPWR+、R2 100K、GND 连接

### U1 ME3116 开关级

U1 的 6 脚 LX 经 L1 36.8uH/3012 连接 VCC_5V；C7 100nF 连接 U1.1 BST 与 LX 节点，D2 B5819W SL 连接 LX 节点与 GND。

- 参数与网络：`switch_pin=U1.6 LX`；`output_inductor=L1 36.8uH/3012`；`bootstrap_capacitor=C7 100nF`；`switch_diode=D2 B5819W SL`；`output_net=VCC_5V`
- 证据：图 848eb0125f17 / 第 1 页 / B2 区域 U1 右侧：BST/C7、LX/D2/L1 以及 L1 右端 VCC_5V

### U1 FB 反馈网络

R3 52.3K 从 VCC_5V 接至 U1.3 FB，R4 10K 从 FB 接至 GND；C10 100pF 与 R3 并联。

- 参数与网络：`upper_resistor=R3 52.3K`；`lower_resistor=R4 10K`；`feedforward_capacitor=C10 100pF`；`feedback_pin=U1.3 FB`
- 证据：图 848eb0125f17 / 第 1 页 / B2-C2 区域 U1.3 FB 右侧：R3/C10 至 VCC_5V，R4 至 GND

### VCC_5V 电源轨

C9 10uF 和 C6 10uF/16V 分别跨接 VCC_5V 与 GND；D1 LESD3Z5.0CMT1G 也跨接 VCC_5V 与 GND。

- 参数与网络：`buck_output_capacitor=C9 10uF`；`rail_capacitor=C6 10uF/16V`；`rail_protector=D1 LESD3Z5.0CMT1G`
- 证据：图 848eb0125f17 / 第 1 页 / B2-B3 区域：C9、C6、D1 的 VCC_5V-GND 跨接关系

### U2 MST5333

U2 的 3 脚 VIN 接 VCC_5V，1 脚 GND 接地，2 脚 VOUT 输出 VCC_3V3；C3 10uF 位于输入侧，C4 10uF 位于输出侧。

- 参数与网络：`input=U2.3 VCC_5V`；`ground=U2.1 GND`；`output=U2.2 VCC_3V3`；`input_capacitor=C3 10uF`；`output_capacitor=C4 10uF`
- 证据：图 848eb0125f17 / 第 1 页 / B3-B4 区域 U2：VIN/GND/VOUT 引脚和 C3/C4 的输入输出连接

### VCC_3V3 指示支路

LED1（White）与 R5 1K 串联在 VCC_3V3 和 GND 之间。

- 参数与网络：`led=LED1 White`；`series_resistor=R5 1K`；`supply=VCC_3V3`；`return=GND`
- 证据：图 848eb0125f17 / 第 1 页 / B4 区域 U2 输出右侧：VCC_3V3、LED1 White、R5 1K、GND 串联支路

### U3 双电源去耦

C1 100nF 跨接 U3 VCC 使用的 VCC_5V 与 GND，C2 100nF 跨接 U3 VIO 使用的 VCC_3V3 与 GND。

- 参数与网络：`vcc_decoupling=C1 100nF VCC_5V-GND`；`vio_decoupling=C2 100nF VCC_3V3-GND`
- 证据：图 848eb0125f17 / 第 1 页 / C2-C3 区域 U3 上方：C1 位于 VCC_5V/GND，C2 位于 VCC_3V3/GND

## 接口

### GROVE

GROVE 的 IO2 接 CAN_Rx，IO1 接 CAN_Tx，5V 接 VCC_5V，GND 接 GND。

- 参数与网络：`IO2=CAN_Rx`；`IO1=CAN_Tx`；`5V=VCC_5V`；`GND=GND`
- 证据：图 848eb0125f17 / 第 1 页 / C1 区域 GROVE 符号右侧：IO2/IO1/5V/GND 与 CAN_Rx/CAN_Tx/VCC_5V/GND

### JP1

JP1 的 4 脚接 CAN_H，3 脚接 CAN_L，2 脚接 HPWR+，1 脚接 GND。

- 参数与网络：`pin_4=CAN_H`；`pin_3=CAN_L`；`pin_2=HPWR+`；`pin_1=GND`
- 证据：图 848eb0125f17 / 第 1 页 / C4 区域 JP1：4/3/2/1 数字与左侧 CAN_H/CAN_L/HPWR+/GND 网络

## 总线

### U3 逻辑侧

U3 的 1 脚 TXD 接 CAN_Tx，2 脚 GND 接地，3 脚 VCC 接 VCC_5V，4 脚 RXD 接 CAN_Rx。

- 参数与网络：`pin_1=TXD CAN_Tx`；`pin_2=GND`；`pin_3=VCC VCC_5V`；`pin_4=RXD CAN_Rx`
- 证据：图 848eb0125f17 / 第 1 页 / C2 区域 U3 左侧 1~4 脚：TXD/GND/VCC/RXD 与 CAN_Tx/GND/VCC_5V/CAN_Rx

### U3 CAN 与 VIO 侧

U3 的 5 脚 VIO 接 VCC_3V3，6 脚 CANL 接 CAN_L，7 脚 CANH 接 CAN_H，8 脚 S 接 GND。

- 参数与网络：`pin_5=VIO VCC_3V3`；`pin_6=CANL CAN_L`；`pin_7=CANH CAN_H`；`pin_8=S GND`
- 证据：图 848eb0125f17 / 第 1 页 / C2-C3 区域 U3 右侧 5~8 脚：VIO/CANL/CANH/S 与 VCC_3V3/CAN_L/CAN_H/GND

### CAN_H/CAN_L 终端

R1 120R 固定跨接在 CAN_H 与 CAN_L 之间。

- 参数与网络：`resistor=R1`；`resistance=120R`；`terminal_1=CAN_H`；`terminal_2=CAN_L`
- 证据：图 848eb0125f17 / 第 1 页 / C3 区域：R1 120R 竖直连接上方 CAN_H 与下方 CAN_L

## 保护电路

### HPWR+ 输入

D3 SMF30CA 和 C8 4.7uF/35V 均跨接在 HPWR+ 与 GND 之间，位于 U1 VIN 输入之前。

- 参数与网络：`transient_suppressor=D3 SMF30CA`；`input_capacitor=C8 4.7uF/35V`；`protected_net=HPWR+`
- 证据：图 848eb0125f17 / 第 1 页 / B1 区域：HPWR+ 水平输入线上并接 D3 和 C8 到 GND，随后进入 U1 VIN

### CAN_H/CAN_L ESD 网络

DZ1 PESD5V0L1BA 连接 CAN_H 与 GND，DZ2 PESD5V0L1BA 连接 CAN_L 与 GND。

- 参数与网络：`high_line_protector=DZ1 PESD5V0L1BA`；`low_line_protector=DZ2 PESD5V0L1BA`；`reference=GND`
- 证据：图 848eb0125f17 / 第 1 页 / C3 区域 R1 右侧：DZ1 位于 CAN_H-GND，DZ2 位于 CAN_L-GND

## 关键网络

### VCC_5V

VCC_5V 同名网络连接 U1 降压输出、GROVE 的 5V 端、U3.3 VCC、U2.3 VIN 及其滤波/保护器件。

- 参数与网络：`buck_output=U1 stage`；`external_port=GROVE 5V`；`can_supply=U3.3 VCC`；`3v3_regulator_input=U2.3 VIN`
- 证据：图 848eb0125f17 / 第 1 页 / B2-B4 与 C1-C2：各节点均标注 VCC_5V，包括 L1 输出、GROVE、U3 VCC 和 U2 VIN

### CAN_Tx/CAN_Rx

GROVE IO1 的 CAN_Tx 连接 U3.1 TXD；GROVE IO2 的 CAN_Rx 连接 U3.4 RXD。

- 参数与网络：`transmit_path=GROVE IO1 CAN_Tx to U3.1 TXD`；`receive_path=GROVE IO2 CAN_Rx to U3.4 RXD`
- 证据：图 848eb0125f17 / 第 1 页 / C1-C2 区域 GROVE 与 U3：同名 CAN_Tx/CAN_Rx 网络连接对应 IO 和 TXD/RXD

### CAN_H/CAN_L

U3.7 CANH 的 CAN_H 网络连接 JP1.4，U3.6 CANL 的 CAN_L 网络连接 JP1.3。

- 参数与网络：`high_path=U3.7 CAN_H to JP1.4`；`low_path=U3.6 CAN_L to JP1.3`
- 证据：图 848eb0125f17 / 第 1 页 / C2-C4 区域 U3、保护网络与 JP1：同名 CAN_H/CAN_L 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini CAN | `can_transceiver=U3 TJA1051T/3`；`buck_regulator=U1 ME3116`；`3v3_regulator=U2 MST5333`；`logic_interface=GROVE`；`bus_interface=JP1` |
| 接口 | GROVE | `IO2=CAN_Rx`；`IO1=CAN_Tx`；`5V=VCC_5V`；`GND=GND` |
| 接口 | JP1 | `pin_4=CAN_H`；`pin_3=CAN_L`；`pin_2=HPWR+`；`pin_1=GND` |
| 保护电路 | HPWR+ 输入 | `transient_suppressor=D3 SMF30CA`；`input_capacitor=C8 4.7uF/35V`；`protected_net=HPWR+` |
| 电源 | U1 ME3116 输入与使能 | `vin=U1.5 HPWR+`；`ground=U1.2 GND`；`enable=U1.4 EN via R2 100K to HPWR+` |
| 电源 | U1 ME3116 开关级 | `switch_pin=U1.6 LX`；`output_inductor=L1 36.8uH/3012`；`bootstrap_capacitor=C7 100nF`；`switch_diode=D2 B5819W SL`；`output_net=VCC_5V` |
| 电源 | U1 FB 反馈网络 | `upper_resistor=R3 52.3K`；`lower_resistor=R4 10K`；`feedforward_capacitor=C10 100pF`；`feedback_pin=U1.3 FB` |
| 电源 | VCC_5V 电源轨 | `buck_output_capacitor=C9 10uF`；`rail_capacitor=C6 10uF/16V`；`rail_protector=D1 LESD3Z5.0CMT1G` |
| 关键网络 | VCC_5V | `buck_output=U1 stage`；`external_port=GROVE 5V`；`can_supply=U3.3 VCC`；`3v3_regulator_input=U2.3 VIN` |
| 电源 | U2 MST5333 | `input=U2.3 VCC_5V`；`ground=U2.1 GND`；`output=U2.2 VCC_3V3`；`input_capacitor=C3 10uF`；`output_capacitor=C4 10uF` |
| 电源 | VCC_3V3 指示支路 | `led=LED1 White`；`series_resistor=R5 1K`；`supply=VCC_3V3`；`return=GND` |
| 总线 | U3 逻辑侧 | `pin_1=TXD CAN_Tx`；`pin_2=GND`；`pin_3=VCC VCC_5V`；`pin_4=RXD CAN_Rx` |
| 总线 | U3 CAN 与 VIO 侧 | `pin_5=VIO VCC_3V3`；`pin_6=CANL CAN_L`；`pin_7=CANH CAN_H`；`pin_8=S GND` |
| 电源 | U3 双电源去耦 | `vcc_decoupling=C1 100nF VCC_5V-GND`；`vio_decoupling=C2 100nF VCC_3V3-GND` |
| 关键网络 | CAN_Tx/CAN_Rx | `transmit_path=GROVE IO1 CAN_Tx to U3.1 TXD`；`receive_path=GROVE IO2 CAN_Rx to U3.4 RXD` |
| 关键网络 | CAN_H/CAN_L | `high_path=U3.7 CAN_H to JP1.4`；`low_path=U3.6 CAN_L to JP1.3` |
| 总线 | CAN_H/CAN_L 终端 | `resistor=R1`；`resistance=120R`；`terminal_1=CAN_H`；`terminal_2=CAN_L` |
| 保护电路 | CAN_H/CAN_L ESD 网络 | `high_line_protector=DZ1 PESD5V0L1BA`；`low_line_protector=DZ2 PESD5V0L1BA`；`reference=GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `848eb0125f177a254232fdf9c289d6e2841e04a0c4131c4e08d00754a4fc91a8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/631/SCH_UNIT_Mini_CAN_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-Mini CAN.md`

源文档 SHA-256：`660926dfcab3d67b32333d206398141f3cec385ecd7ad0edebfb0830739e66fe`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
