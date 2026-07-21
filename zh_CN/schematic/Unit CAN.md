# Unit CAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CAN |
| SKU | U085 |
| 产品 ID | `unit-can-bcce96f7e852` |
| 源文档 | `zh_CN/unit/can.md` |

## 概述

Unit CAN（U085）以 U1 CA-IS3050G 隔离 CAN 收发器为核心，将 Grove 侧 CAN_Tx/CAN_Rx 转换为隔离侧 CAN_H/CAN_L，并由 JP1 引出 CAN_OUT_H、CAN_OUT_L 与 SHIELD。M1 B0505ST16-W5 将 HOST_5V 隔离转换为 VCC_5V，分别为 U1 的主机侧和总线侧供电；U2 MST5333 另生成 HOST_3V3 驱动白色电源指示灯。总线侧配置双路 ESD、三只 P0080TA、双 GDT、双串联保护器件及 GND-SHIELD 阻容耦合，主机侧 CAN_Tx/CAN_Rx 由 D3 SRV05-4 防护。原理图未显示板载 120Ω 终端电阻，正文中的 1Mbps、110 节点、1000V 隔离及保护额定值需结合 datasheet 或实测确认。

## 检索关键词

`Unit CAN`、`U085`、`SCH_UNIT_ISOCAN_v1.1`、`CA-IS3050G`、`B0505ST16-W5`、`MST5333`、`SRV05-4`、`PESD5V0L1BA`、`P0080TA`、`SMD4532-075`、`LESD3Z5.0CMT1G`、`CAN`、`CAN_Tx`、`CAN_Rx`、`CAN_H`、`CAN_L`、`CAN_OUT_H`、`CAN_OUT_L`、`HOST_5V`、`HOST_3V3`、`VCC_5V`、`HOST_GND`、`GND`、`SHIELD`、`Grove`、`JP1`、`60V 100mA/JK-NSMD010`、`1nF/2000V`、`120Ω`、`隔离 CAN`、`1Mbps`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | CA-IS3050G | 双电源域隔离 CAN 收发器，将主机侧 RxD/TxD 转换为隔离侧 CANH/CANL | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1-A2，U1 CA-IS3050G，pin1-pin8 的 VCC1/GND1/RxD/TxD 与 VCC2/GND2/CANH/CANL |
| M1 | B0505ST16-W5 | 由 HOST_5V 生成隔离 VCC_5V 的 5V-5V 隔离电源模块 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B1-B2，M1 B0505ST16-W5，VIN/GND/CTRL 与 VO/0V/TRIM |
| U2 | MST5333 | 将 HOST_5V 稳压为 HOST_3V3，供 LED1 电源指示支路使用 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B3，U2 MST5333，VIN pin3、VOUT pin2、GND 与 HOST_5V/HOST_3V3 |
| GROVE | 未标注 | 主机侧四针接口，提供 CAN_Rx、CAN_Tx、HOST_5V 与 HOST_GND | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A3，GROVE 符号 IO2/IO1/5V/GND 与 CAN_Rx/CAN_Tx/HOST_5V/HOST_GND |
| JP1 | 未标注 | 四针 CAN 输出连接器，引出 CAN_OUT_H、CAN_OUT_L、NC 与 SHIELD | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A3，JP1 pin4 CAN_OUT_H、pin3 CAN_OUT_L、pin2 未连接、pin1 SHIELD |
| D3 | SRV05-4 | 主机侧 CAN_Rx/CAN_Tx 四通道钳位保护阵列，VCC 接 HOST_5V、GND 接 HOST_GND | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1，D3 SRV05-4，IO1-IO4 跨接 CAN_Rx/CAN_Tx，VCC pin5 与 GND pin2 |
| DZ1,DZ2 | PESD5V0L1BA | 分别从 CAN_H、CAN_L 到隔离侧 GND 的 ESD/TVS 保护器件 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2 CAN Protector，DZ1/DZ2 PESD5V0L1BA 与 CAN_H/CAN_L/GND |
| TSS1,TSS2,TSS3 | P0080TA | CAN_H、CAN_L 与 SHIELD 保护网络中的三只双向浪涌抑制器件 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2，TSS1/TSS2/TSS3 均标注 P0080TA，位于 CAN_H/CAN_L/SHIELD 网络 |
| GDT1,GDT2 | SMD4532-075 | CAN_OUT_H、CAN_OUT_L 到 SHIELD 的双路气体放电管保护 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2，GDT1/GDT2 SMD4532-075，连接输出线与 SHIELD 中心节点 |
| F1,F2 | 60V 100mA/JK-NSMD010 | 分别串联在 CAN_H 到 CAN_OUT_H、CAN_L 到 CAN_OUT_L 路径中的保护器件 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2，F1/F2 均标注 60V 100mA/JK-NSMD010，串联于两条差分线 |
| R6,C12 | 1MΩ / 1nF/2000V | 在隔离侧 GND 与 SHIELD 之间提供并联的高阻直流泄放和高压电容耦合 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2，R6 1M 与 C12 1nF/2000V 并联跨接 GND-SHIELD |
| L1,C5,C6,C7 | 6.8uH / 10uF/16V | M1 隔离电源输入 LC 滤波与输出 VCC_5V 去耦 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B1-B2，L1 6.8uH，C5/C6/C7 各 10uF/16V |
| D1 | LESD3Z5.0CMT1G | VCC_5V 到隔离侧 GND 的电源轨保护器件 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B2，D1 LESD3Z5.0CMT1G 跨接 VCC_5V 与 GND |
| LED1,R3 | White / 1KΩ | HOST_3V3 电源指示灯及其串联限流电阻 | 图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B3，LED1 White 与 R3 1K 从 HOST_3V3 接至 HOST_GND |

## 系统结构

### Unit CAN 隔离架构

外部主机通过 GROVE 的 CAN_Tx/CAN_Rx 连接 U1 CA-IS3050G 的 TxD/RxD，U1 跨越 HOST_GND 与隔离 GND 两个电气域并输出 CAN_H/CAN_L。M1 B0505ST16-W5 提供隔离侧 VCC_5V，保护网络将差分信号变为 CAN_OUT_H/CAN_OUT_L 后由 JP1 引出；原理图没有本地主控、协处理器、存储器、晶振、射频、音频、传感器或电池。

- 参数与网络：`host_interface=GROVE CAN_Tx/CAN_Rx`；`transceiver=U1 CA-IS3050G`；`power_isolation=M1 B0505ST16-W5`；`bus_output=JP1 CAN_OUT_H/CAN_OUT_L/SHIELD`；`local_controller=null`；`storage=null`；`clock=null`；`battery=null`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页完整网格 A1-B3，Isolated CAN、CAN Protector、Isolated 5V Power、Grove LDO 与连接器

## 核心器件

### CA-IS3050G 引脚与电源域

U1 pin1 VCC1 接 HOST_5V，pin4 GND1 接 HOST_GND，pin2 RxD 接 CAN_Rx，pin3 TxD 接 CAN_Tx；隔离侧 pin8 VCC2 接 VCC_5V，pin5 GND2 接 GND，pin7 CANH 接 CAN_H，pin6 CANL 接 CAN_L。

- 参数与网络：`pin1=VCC1 HOST_5V`；`pin2=RxD CAN_Rx`；`pin3=TxD CAN_Tx`；`pin4=GND1 HOST_GND`；`pin5=GND2 GND`；`pin6=CANL CAN_L`；`pin7=CANH CAN_H`；`pin8=VCC2 VCC_5V`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1-A2，U1 CA-IS3050G pin1-pin8 标注与网络

## 电源

### HOST_5V 主机侧电源分配

HOST_5V 从 GROVE 5V 引入，直接供给 U1 VCC1 pin1 和 U2 MST5333 VIN pin3，并经 C5-L1-C6 输入滤波后进入 M1 VIN pin3。HOST_GND 连接 U1 GND1、U2 GND、M1 GND/CTRL 以及相关去耦。

- 参数与网络：`source=GROVE 5V`；`rail=HOST_5V`；`loads=U1 VCC1,U2 VIN,M1 VIN via L1`；`input_filter=C5 10uF/16V,L1 6.8uH,C6 10uF/16V`；`return=HOST_GND`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页 GROVE 5V/HOST_GND、U1 VCC1/GND1、M1 输入滤波与 U2 VIN/GND

### 隔离 VCC_5V 电源路径

HOST_5V 经 L1 6.8uH 与 C5/C6 各 10uF/16V 滤波后进入 M1 B0505ST16-W5 VIN pin3；M1 VO pin14 输出 VCC_5V，0V pins9/15/16 接隔离 GND。C7 10uF/16V 与 D1 LESD3Z5.0CMT1G 跨接 VCC_5V-GND，VCC_5V 为 U1 VCC2 pin8 供电。

- 参数与网络：`converter=M1 B0505ST16-W5`；`input=HOST_5V`；`input_filter=L1 6.8uH,C5/C6 10uF/16V`；`output=pin14 VO -> VCC_5V`；`output_return=pins9/15/16 0V -> GND`；`output_capacitor=C7 10uF/16V`；`protection=D1 LESD3Z5.0CMT1G`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B1-B2，Isolated 5V Power 的 L1/C5/C6/M1/R1/R2/C7/D1 与 VCC_5V

### HOST_3V3 与电源指示

U2 MST5333 VIN pin3 接 HOST_5V，VOUT pin2 生成 HOST_3V3，C3/C4 各 4.7uF/6.3V 分别为输入和输出去耦。HOST_3V3 只在本页连接 LED1 White，LED1 经 R3 1K 接 HOST_GND；未显示 U2 使能脚或其他 HOST_3V3 负载。

- 参数与网络：`ldo=U2 MST5333`；`input=pin3 HOST_5V`；`output=pin2 HOST_3V3`；`capacitors=C3/C4 4.7uF/6.3V`；`indicator=LED1 White + R3 1K to HOST_GND`；`enable=null`；`other_loads=null`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 B3 Grove LDO，U2/C3/C4/LED1/R3 与 HOST_5V/HOST_3V3/HOST_GND

## 接口

### GROVE 主机接口针脚

GROVE 四针符号依次标为 IO2、IO1、5V、GND；IO2 连接 CAN_Rx（U1 到主机的接收数据输出），IO1 连接 CAN_Tx（主机到 U1 的发送数据输入），5V 连接 HOST_5V 电源输入，GND 连接 HOST_GND。

- 参数与网络：`IO2=CAN_Rx, output from unit to host`；`IO1=CAN_Tx, input from host to unit`；`5V=HOST_5V power input`；`GND=HOST_GND return`；`logic_supply=HOST_5V`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A3，GROVE IO2/IO1/5V/GND 与四个同名网络

### JP1 CAN 输出连接器

JP1 pin4 接 CAN_OUT_H，pin3 接 CAN_OUT_L，pin2 在图中为未连接短线，pin1 接 SHIELD。JP1 没有引出隔离侧 GND 或电源。

- 参数与网络：`pin4=CAN_OUT_H bidirectional differential bus`；`pin3=CAN_OUT_L bidirectional differential bus`；`pin2=NC`；`pin1=SHIELD`；`power_pin=null`；`ground_pin=null`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A3，JP1 pin1-pin4 标注

## 总线

### 主机逻辑信号到 CAN 差分总线

GROVE IO1 的 CAN_Tx 进入 U1 TxD pin3，U1 CANH pin7/CANL pin6 产生 CAN_H/CAN_L；经过 CAN Protector 后形成 CAN_OUT_H/CAN_OUT_L。U1 RxD pin2 输出 CAN_Rx 到 GROVE IO2，供外部 CAN 控制器接收。

- 参数与网络：`controller=external CAN controller`；`tx_path=GROVE IO1 CAN_Tx -> U1 pin3 TxD -> pin7/pin6 CANH/CANL`；`rx_path=U1 pin2 RxD -> GROVE IO2 CAN_Rx`；`differential_output=CAN_H/CAN_L -> protection -> CAN_OUT_H/CAN_OUT_L`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1-A3，GROVE、U1 与 CAN Protector 的 CAN_Tx/CAN_Rx/CAN_H/CAN_L/CAN_OUT_H/CAN_OUT_L

### CAN 终端电阻配置

完整单页原理图从 U1 CANH/CANL 到 JP1 CAN_OUT_H/CAN_OUT_L 的全部路径中未显示跨接两条差分线的 120Ω 终端电阻、终端开关或跳线；产品正文只在包装内容中列出一只独立 120R 电阻。

- 参数与网络：`onboard_termination=null`；`termination_switch=null`；`differential_nets=CAN_H/CAN_L,CAN_OUT_H/CAN_OUT_L`；`documented_loose_resistor=120R`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1-A3，U1 至 JP1 的完整 CAN 差分与保护路径，无 120Ω 器件

## 复位

### 复位、BOOT、使能与调试电路

本页没有本地主控，因此未显示 RESET、BOOT、片选、中断、方向控制 GPIO、调试连接器或外部时钟。M1 CTRL pin1 接 HOST_GND，U2 未画出独立使能引脚，U1 也没有图示使能/待机控制网络。

- 参数与网络：`reset=null`；`boot=null`；`interrupt=null`；`debug_connector=null`；`external_clock=null`；`m1_ctrl=pin1 HOST_GND`；`transceiver_enable=null`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页完整单页；M1 CTRL pin1、U1 pin1-pin8 和 U2 三引脚电路

## 保护电路

### CAN_Tx/CAN_Rx 主机侧保护

D3 SRV05-4 的 IO1-IO4 成对连接 CAN_Rx 与 CAN_Tx，VCC pin5 接 HOST_5V、GND pin2 接 HOST_GND，对进入 U1 RxD/TxD 的主机侧逻辑线提供钳位保护。

- 参数与网络：`device=D3 SRV05-4`；`protected_nets=CAN_Rx,CAN_Tx`；`io_channels=IO1-IO4`；`positive_reference=pin5 HOST_5V`；`ground_reference=pin2 HOST_GND`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A1，D3 SRV05-4 与 CAN_Rx/CAN_Tx/HOST_5V/HOST_GND

### CAN_H/CAN_L 多级保护路径

CAN_H/CAN_L 各由 DZ1/DZ2 PESD5V0L1BA 对隔离 GND 钳位；TSS1/TSS2/TSS3 均为 P0080TA，覆盖线对 SHIELD 及线间浪涌路径；GDT1/GDT2 SMD4532-075 将两条输出线连接至 SHIELD；F1/F2 以 60V 100mA/JK-NSMD010 分别串联生成 CAN_OUT_H/CAN_OUT_L。

- 参数与网络：`esd=DZ1/DZ2 PESD5V0L1BA to GND`；`tss=TSS1/TSS2/TSS3 P0080TA`；`gdt=GDT1/GDT2 SMD4532-075 to SHIELD`；`series_h=F1 60V 100mA/JK-NSMD010`；`series_l=F2 60V 100mA/JK-NSMD010`；`input_nets=CAN_H,CAN_L`；`output_nets=CAN_OUT_H,CAN_OUT_L`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2 CAN Protector 全区，DZ1/DZ2、TSS1-TSS3、GDT1/GDT2、F1/F2

### 隔离 GND 与 SHIELD 耦合

R6 1MΩ 与 C12 1nF/2000V 并联跨接隔离侧 GND 和 SHIELD，在不直接短接两者的情况下形成直流泄放与交流耦合路径；JP1 pin1 连接 SHIELD。

- 参数与网络：`from=GND`；`to=SHIELD`；`resistor=R6 1MΩ`；`capacitor=C12 1nF/2000V`；`connector=JP1 pin1 SHIELD`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页网格 A2，R6/C12 并联于 GND-SHIELD；网格 A3 JP1 pin1

## 关键网络

### 电源、地与屏蔽域索引

主机域使用 HOST_5V/HOST_3V3/HOST_GND，隔离 CAN 域使用 VCC_5V/GND，屏蔽域为 SHIELD。M1 在 HOST_5V/HOST_GND 与 VCC_5V/GND 间提供隔离供电，U1 在主机逻辑域与隔离差分域间传输信号，SHIELD 仅经 R6/C12 与隔离 GND 耦合。

- 参数与网络：`host_domain=HOST_5V,HOST_3V3,HOST_GND`；`isolated_domain=VCC_5V,GND,CAN_H,CAN_L`；`shield_domain=SHIELD`；`power_barrier=M1 B0505ST16-W5`；`signal_barrier=U1 CA-IS3050G`；`shield_coupling=R6 1MΩ || C12 1nF/2000V`
- 证据：图 50d1f5c94399 / 第 1 页 / 第 1 页所有 HOST_5V/HOST_3V/HOST_GND/VCC_5V/GND/SHIELD 同名网络及 U1/M1 隔离边界

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CAN 隔离架构 | `host_interface=GROVE CAN_Tx/CAN_Rx`；`transceiver=U1 CA-IS3050G`；`power_isolation=M1 B0505ST16-W5`；`bus_output=JP1 CAN_OUT_H/CAN_OUT_L/SHIELD`；`local_controller=null`；`storage=null`；`clock=null`；`battery=null` |
| 核心器件 | CA-IS3050G 引脚与电源域 | `pin1=VCC1 HOST_5V`；`pin2=RxD CAN_Rx`；`pin3=TxD CAN_Tx`；`pin4=GND1 HOST_GND`；`pin5=GND2 GND`；`pin6=CANL CAN_L`；`pin7=CANH CAN_H`；`pin8=VCC2 VCC_5V` |
| 总线 | 主机逻辑信号到 CAN 差分总线 | `controller=external CAN controller`；`tx_path=GROVE IO1 CAN_Tx -> U1 pin3 TxD -> pin7/pin6 CANH/CANL`；`rx_path=U1 pin2 RxD -> GROVE IO2 CAN_Rx`；`differential_output=CAN_H/CAN_L -> protection -> CAN_OUT_H/CAN_OUT_L` |
| 接口 | GROVE 主机接口针脚 | `IO2=CAN_Rx, output from unit to host`；`IO1=CAN_Tx, input from host to unit`；`5V=HOST_5V power input`；`GND=HOST_GND return`；`logic_supply=HOST_5V` |
| 接口 | JP1 CAN 输出连接器 | `pin4=CAN_OUT_H bidirectional differential bus`；`pin3=CAN_OUT_L bidirectional differential bus`；`pin2=NC`；`pin1=SHIELD`；`power_pin=null`；`ground_pin=null` |
| 电源 | HOST_5V 主机侧电源分配 | `source=GROVE 5V`；`rail=HOST_5V`；`loads=U1 VCC1,U2 VIN,M1 VIN via L1`；`input_filter=C5 10uF/16V,L1 6.8uH,C6 10uF/16V`；`return=HOST_GND` |
| 电源 | 隔离 VCC_5V 电源路径 | `converter=M1 B0505ST16-W5`；`input=HOST_5V`；`input_filter=L1 6.8uH,C5/C6 10uF/16V`；`output=pin14 VO -> VCC_5V`；`output_return=pins9/15/16 0V -> GND`；`output_capacitor=C7 10uF/16V`；`protection=D1 LESD3Z5.0CMT1G` |
| 电源 | HOST_3V3 与电源指示 | `ldo=U2 MST5333`；`input=pin3 HOST_5V`；`output=pin2 HOST_3V3`；`capacitors=C3/C4 4.7uF/6.3V`；`indicator=LED1 White + R3 1K to HOST_GND`；`enable=null`；`other_loads=null` |
| 保护电路 | CAN_Tx/CAN_Rx 主机侧保护 | `device=D3 SRV05-4`；`protected_nets=CAN_Rx,CAN_Tx`；`io_channels=IO1-IO4`；`positive_reference=pin5 HOST_5V`；`ground_reference=pin2 HOST_GND` |
| 保护电路 | CAN_H/CAN_L 多级保护路径 | `esd=DZ1/DZ2 PESD5V0L1BA to GND`；`tss=TSS1/TSS2/TSS3 P0080TA`；`gdt=GDT1/GDT2 SMD4532-075 to SHIELD`；`series_h=F1 60V 100mA/JK-NSMD010`；`series_l=F2 60V 100mA/JK-NSMD010`；`input_nets=CAN_H,CAN_L`；`output_nets=CAN_OUT_H,CAN_OUT_L` |
| 保护电路 | 隔离 GND 与 SHIELD 耦合 | `from=GND`；`to=SHIELD`；`resistor=R6 1MΩ`；`capacitor=C12 1nF/2000V`；`connector=JP1 pin1 SHIELD` |
| 关键网络 | 电源、地与屏蔽域索引 | `host_domain=HOST_5V,HOST_3V3,HOST_GND`；`isolated_domain=VCC_5V,GND,CAN_H,CAN_L`；`shield_domain=SHIELD`；`power_barrier=M1 B0505ST16-W5`；`signal_barrier=U1 CA-IS3050G`；`shield_coupling=R6 1MΩ || C12 1nF/2000V` |
| 总线 | CAN 终端电阻配置 | `onboard_termination=null`；`termination_switch=null`；`differential_nets=CAN_H/CAN_L,CAN_OUT_H/CAN_OUT_L`；`documented_loose_resistor=120R` |
| 复位 | 复位、BOOT、使能与调试电路 | `reset=null`；`boot=null`；`interrupt=null`；`debug_connector=null`；`external_clock=null`；`m1_ctrl=pin1 HOST_GND`；`transceiver_enable=null` |
| 其他事实 | 正文中的 CAN 通信性能 | `documented_max_rate=1Mbps`；`documented_nodes=110`；`documented_long_distance=10km at <5Kbps`；`documented_1mbps_distance=<40m`；`documented_standard=ISO11898-2`；`schematic_performance_table=null` |
| 保护电路 | 正文中的隔离与保护额定值 | `documented_isolation=1000V`；`documented_common_mode=-12V to 12V`；`documented_ground_loss=-40V to 40V`；`documented_protections=current limit,overvoltage,dominant timeout,thermal shutdown`；`schematic_test_conditions=null` |

## 待确认事项

- `other.documented-can-performance`：产品正文称信号速率最高 1Mbps、最多支持 110 个节点，通信距离可在低于 5Kbps 时达到 10km、在 1Mbps 时小于 40m，并符合 ISO11898-2；原理图只确认 CA-IS3050G 型号与连接，没有印出这些性能边界。（证据：图 50d1f5c94399 / 第 1 页 / 第 1 页 U1 CA-IS3050G 与 CAN_H/CAN_L，整页无速率、节点数、距离或标准文字）
- `protection.documented-ratings`：产品正文列出 1000V 隔离耐压、-12V 至 12V 共模电压、限流、过压、接地损耗保护、主动态超时与热关断，并描述接地损耗保护范围为 -40V 至 40V；原理图显示隔离与保护器件拓扑，但没有直接给出这些系统级额定值或测试条件。（证据：图 50d1f5c94399 / 第 1 页 / 第 1 页 U1/M1 隔离边界与 CAN Protector 全区，图中无系统级隔离/共模/热关断额定表）
- `review.can-performance`：请结合 CA-IS3050G datasheet、总线拓扑和线缆条件确认 U085 的 1Mbps、110 节点、通信距离及 ISO11898-2 适用边界。；原因：原理图没有给出速率、节点负载、线缆、距离或标准符合性测试条件。
- `review.isolation-protection-ratings`：请用 U1、M1 与保护器件 datasheet 或整机测试报告确认 1000V 隔离、共模范围、接地损耗范围、限流、过压、主动态超时和热关断额定值。；原因：页面只显示器件型号和拓扑，未显示系统级额定值、持续时间、环境或测试方法。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `50d1f5c9439941d97c41061b94ea12996470e1694e1439395a987ff928838bf4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/586/SCH_UNIT_ISOCAN_v1.1_sch_01.png` |

---

源文档：`zh_CN/unit/can.md`

源文档 SHA-256：`356734b1d86f0d144345375a28ab04401f3d2066966ccc7a11751d11be57cfbc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
