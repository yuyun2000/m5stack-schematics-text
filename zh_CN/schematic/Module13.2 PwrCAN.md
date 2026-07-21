# Module13.2 PwrCAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 PwrCAN |
| SKU | M139 |
| 产品 ID | `module13-2-pwrcan-de2c622a3f3f` |
| 源文档 | `zh_CN/module/Module13.2-PwrCAN.md` |

## 概述

Module13.2 PwrCAN 将 HPWR 宽压总线经 U2 ME3116 变换为 ISO_5V，再由 U4 F0505S-2WR3 隔离为 BUS_5V，U5 ME6211A3BM3G 生成主机侧 +3.3V。U3 CA-IS3050G 提供隔离 CAN，两组 XT30 接口并联 CAN_H/CAN_L/HPWR/ISO_GND，并配置多级浪涌保护和可切换 120R；U1 CA-IS3082 提供隔离 RS485，HT3.96 接口含偏置、三 TVS 和可切换 120R。P5/P6 与 SW1/SW2 将 CAN/RS485 TX/RX 分配到多个 M5-Bus GPIO；速率、节点数、带载能力和 CA-IS3082W 后缀需结合器件/测试资料确认。

## 检索关键词

`Module13.2 PwrCAN`、`M139`、`CA-IS3050G`、`CA-IS3082`、`CA-IS3082W`、`ME3116`、`F0505S-2WR3`、`ME6211A3BM3G`、`CAN_H`、`CAN_L`、`CAN_TX`、`CAN_RX`、`RS485_A`、`RS485_B`、`485_TX`、`485_RX`、`HPWR`、`ISO_5V`、`BUS_5V`、`+3.3V`、`ISO_GND`、`120R`、`SMAJ6.8CA`、`PESD5V0L1BA`、`P0080TA`、`SMD4532-075`、`XT30PW(2+2)-M`、`HT3.96 4P`、`M5Stack_BUS`、`SW1`、`SW2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ME3116 | 将 HPWR 输入降压为 ISO_5V | 图 122fe8e39a98 / 第 1 页 / 第 1 页 A1-A2 U2 ME3116，HPWR/ISO_5V/L1/反馈网络 |
| U4 | F0505S-2WR3 | 将 ISO_5V 电气隔离为 BUS_5V | 图 122fe8e39a98 / 第 1 页 / 第 1 页 A3 U4 F0505S-2WR3，VIN/GND 与 0V/+VO |
| U5 | ME6211A3BM3G | 由 BUS_5V 生成 +3.3V | 图 122fe8e39a98 / 第 1 页 / 第 1 页 A3-A4 U5 ME6211A3BM3G |
| U3 | CA-IS3050G | 主机侧 +3.3V 与隔离侧 ISO_5V 之间的隔离 CAN 收发器 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 B2-B3 U3 CA-IS3050G，RxD/TxD/CANH/CANL/VCC1/VCC2/GND1/GND2 |
| U1 | CA-IS3082 | 主机侧 +3.3V 与隔离侧 ISO_5V 之间的隔离 RS485 收发器 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 C2-D3 U1 CA-IS3082，RO/RE#/DE/DI/A/B/VDDA/VDDB/GNDA/GNDB |
| P3/P4 | XT30PW(2+2)-M | 两组并联 PwrCAN 接口，引出 HPWR、ISO_GND、CAN_L、CAN_H | 图 122fe8e39a98 / 第 1 页 / 第 1 页 B4 P3/P4 XT30PW(2+2)-M |
| P1 | HT3.96 4P | Pwr485 接口，引出 RS485_B、RS485_A、HPWR、ISO_GND | 图 122fe8e39a98 / 第 1 页 / 第 1 页 C4 P1 HT3.96 4P |
| P2 | DC050 | HPWR 外部直流输入接口 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 A1 P2 DC050 与 HPWR/ISO_GND |
| J1 | M5Stack_BUS | 30 针主机堆叠接口，引出可选 CAN/RS485 GPIO、BUS_5V、+3.3V 与 GND | 图 122fe8e39a98 / 第 1 页 / 第 1 页 C4-D4 J1 M5Stack_BUS |
| SW1/SW2 | 未标注 | CAN 与 RS485 TX/RX 的 GPIO 选择拨码开关 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 B1 红框 Block diagram of 2F internal connection，SW1/SW2 |
| S1/S2 | SW-SPST | CAN 与 RS485 120R 终端电阻使能开关 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 B3 S1/R7 CAN 终端与 D3 S2/R6 RS485 终端 |
| Q2 | BSS138 | 由 485_TX 驱动 U1 RE#/DE 共节点的自动方向控制 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 C1-D2 Q2 BSS138、R3/R5、U1 RE#/DE |
| Q3 | AP40P04Q | P1 HPWR 电源线上的高边开关器件 | 图 122fe8e39a98 / 第 1 页 / 第 1 页 C4 Q3 AP40P04Q，HPWR 至 P1.2 |

## 系统结构

### Module13.2 PwrCAN

模块包含 HPWR→ISO_5V→隔离 BUS_5V/+3.3V 电源链、U3 隔离 CAN、U1 隔离 RS485、GPIO 选择拨码、两组 CAN 与一组 RS485 外部接口。

- 参数与网络：`power=U2 ME3116 -> U4 F0505S-2WR3 -> U5 ME6211A3BM3G`；`can=U3 CA-IS3050G`；`rs485=U1 CA-IS3082`；`can_ports=P3,P4`；`rs485_port=P1`；`selectors=SW1,SW2`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页完整原理图所有功能分区

## 电源

### P2 HPWR 输入

P2 DC050 将正端接 HPWR、负端接 ISO_GND；D5 SMAJ30CA、C6 22uF、C5 100nF 均跨接 HPWR 与 ISO_GND。

- 参数与网络：`connector=P2 DC050`；`positive=HPWR`；`negative=ISO_GND`；`tvs=D5 SMAJ30CA`；`capacitors=C6 22uF,C5 100nF`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 A1 P2/D5/C5/C6

### U2 ME3116

U2 VIN 接 HPWR，LX 经 L1 68uH 输出 ISO_5V；R10 210K/R11 40.2K 构成反馈，R9 100K 将 EN 接 HPWR。

- 参数与网络：`input=HPWR`；`output=ISO_5V`；`inductor=L1 68uH`；`feedback=R10 210K,R11 40.2K`；`enable=R9 100K to HPWR`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 A1-A2 U2/L1/反馈网络

### U4 F0505S-2WR3

U4 输入侧由 ISO_5V/ISO_GND 供电，输出侧 +VO/0V 形成 BUS_5V/GND，实现两地之间电源隔离。

- 参数与网络：`input_supply=ISO_5V`；`input_ground=ISO_GND`；`output_supply=BUS_5V`；`output_ground=GND`；`isolation_module=F0505S-2WR3`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 A3 U4 两侧网络

### U5 ME6211A3BM3G

U5 VIN 接 BUS_5V，VOUT 输出 +3.3V，输入 C20 10uF，输出 C21 100nF/C22 10uF。

- 参数与网络：`input=BUS_5V`；`output=+3.3V`；`input_cap=C20 10uF`；`output_caps=C21 100nF,C22 10uF`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 A4 U5/C20-C22

## 接口

### P3/P4 PwrCAN

P3 与 P4 针脚相同：4=HPWR，3=ISO_GND，2=CAN_L，1=CAN_H；两接口使用同名网络并联。

- 参数与网络：`pin_4=HPWR`；`pin_3=ISO_GND`；`pin_2=CAN_L`；`pin_1=CAN_H`；`ports=P3,P4 parallel`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 B4 P3/P4 网络与针脚号

### P1 HT3.96 4P

P1.4=RS485_B，P1.3=RS485_A，P1.2 经 Q3 接 HPWR，P1.1=ISO_GND。

- 参数与网络：`pin_4=RS485_B`；`pin_3=RS485_A`；`pin_2=HPWR via Q3 AP40P04Q`；`pin_1=ISO_GND`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 C4 P1/Q3

### J1 M5Stack_BUS

J1.1/.3/.5 接 GND，2/15/16/21/22/23/24/26 对应可选 GPIO35/16/17/12/13/15/0/34，12 为 +3.3V，28 为 BUS_5V，30 为 BAT。

- 参数与网络：`ground=pins1,3,5`；`selectable_gpio=pin2 GPIO35,pin15 GPIO16,pin16 GPIO17,pin21 GPIO12,pin22 GPIO13,pin23 GPIO15,pin24 GPIO0,pin26 GPIO34`；`3v3=pin12`；`5v=pin28 BUS_5V`；`battery=pin30 BAT`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 C4-D4 J1 外部网络

## 总线

### U3 CA-IS3050G

U3 逻辑侧 VCC1/GND1 使用 +3.3V/GND，RxD/TxD 接 CAN_RX/CAN_TX；隔离侧 VCC2/GND2 使用 ISO_5V/ISO_GND，CANH/CANL 接 CAN_H/CAN_L。

- 参数与网络：`logic_supply=+3.3V/GND`；`logic_rx=CAN_RX -> U3.2 RxD`；`logic_tx=CAN_TX -> U3.3 TxD`；`isolated_supply=ISO_5V/ISO_GND`；`physical=U3.7 CANH CAN_H,U3.6 CANL CAN_L`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 B2 U3 两侧引脚和供电

### CAN 120R 终端

R7 120R 与 S1 SW-SPST 串联跨接 CAN_H 与 CAN_L，可选择启用终端。

- 参数与网络：`resistor=R7 120R`；`switch=S1 SW-SPST`；`terminal_1=CAN_H`；`terminal_2=CAN_L`；`switchable=true`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 B3 R7/S1 跨 CAN_H/L

### U1 CA-IS3082 与方向控制

U1 RO 输出经 R13 1K 到 485_RX，DI 接 485_TX；RE# 与 DE 共节点由 Q2 BSS138、R3 4.7K、R5 1K 随 485_TX 控制。

- 参数与网络：`receive=U1.3 RO -> R13 1K -> 485_RX`；`transmit=485_TX -> U1.6 DI`；`enable_node=U1.4 RE# + U1.5 DE`；`control=Q2 BSS138,R3 4.7K,R5 1K`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 C1-D2 U1/Q2/R3/R5/R13

### U1 隔离侧 RS485

U1 VDDB/GNDB 使用 ISO_5V/ISO_GND，B/A 分别接 RS485_B/RS485_A；R4 4.7K 将 B 接 ISO_GND，R8 4.7K 将 A 接 ISO_5V。

- 参数与网络：`supply=ISO_5V/ISO_GND`；`B=U1.13 RS485_B`；`A=U1.12 RS485_A`；`B_bias=R4 4.7K to ISO_GND`；`A_bias=R8 4.7K to ISO_5V`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 C2-D3 U1 隔离侧与 R4/R8

### RS485 120R 终端

R6 120R 与 S2 SW-SPST 串联跨接 RS485_B 与 RS485_A，可选择启用终端。

- 参数与网络：`resistor=R6 120R`；`switch=S2 SW-SPST`；`terminal_1=RS485_B`；`terminal_2=RS485_A`；`switchable=true`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 D3 R6/S2

## GPIO 与控制信号

### CAN/RS485 GPIO 选择

SW1/SW2 将 CAN_TX/CAN_RX 与 485_TX/485_RX 连接到 GPIO17、GPIO15、GPIO12、GPIO0、GPIO16、GPIO13、GPIO34、GPIO35 等候选；P5/P6 六针头引出相应逻辑网络用于内部连接。

- 参数与网络：`can_header=P5 CAN_TX,CAN_RX,GPIO13,GPIO17,GPIO16,GPIO35`；`rs485_header=P6 GPIO34,GPIO0,GPIO15,GPIO12,485_TX,485_RX`；`selectors=SW1 CAN,SW2 RS485`；`warning=simultaneous selection conflicts are not electrically prevented`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 B1 红框 SW1/SW2 block diagram 与 P5/P6

## 保护电路

### CAN_H/CAN_L 多级保护

CAN_H/L 各串 F1/F2 60V 100mA/JK-NSMD010；配置 DZ1/DZ2 PESD5V0L1BA、TSS1/TSS3 P0080TA、GDT1/GDT2 SMD4532-075，并将 GDT 中点接 SHIELD。

- 参数与网络：`series_fuses=F1,F2 60V 100mA/JK-NSMD010`；`esd=DZ1,DZ2 PESD5V0L1BA`；`tss=TSS1,TSS3 P0080TA`；`gdt=GDT1,GDT2 SMD4532-075`；`reference=ISO_GND/SHIELD`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 B3 U3 右侧 CAN 保护网络

### RS485 TVS

D1 SMAJ6.8CA 跨 ISO_GND-RS485_B，D2 跨 RS485_B-RS485_A，D3 跨 RS485_A-ISO_GND。

- 参数与网络：`B_to_ground=D1 SMAJ6.8CA`；`B_to_A=D2 SMAJ6.8CA`；`A_to_ground=D3 SMAJ6.8CA`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 C3-D3 D1/D2/D3

## 其他事实

### 时钟与存储

本页未展示主控 MCU、CAN 控制器、晶振或外部存储器；模块只提供 CAN/RS485 物理层隔离收发。

- 参数与网络：`mcu_shown=false`；`can_controller_shown=false`；`crystal_shown=false`；`external_storage_shown=false`
- 证据：图 122fe8e39a98 / 第 1 页 / 第 1 页完整原理图器件范围

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 PwrCAN | `power=U2 ME3116 -> U4 F0505S-2WR3 -> U5 ME6211A3BM3G`；`can=U3 CA-IS3050G`；`rs485=U1 CA-IS3082`；`can_ports=P3,P4`；`rs485_port=P1`；`selectors=SW1,SW2` |
| 电源 | P2 HPWR 输入 | `connector=P2 DC050`；`positive=HPWR`；`negative=ISO_GND`；`tvs=D5 SMAJ30CA`；`capacitors=C6 22uF,C5 100nF` |
| 电源 | U2 ME3116 | `input=HPWR`；`output=ISO_5V`；`inductor=L1 68uH`；`feedback=R10 210K,R11 40.2K`；`enable=R9 100K to HPWR` |
| 电源 | U4 F0505S-2WR3 | `input_supply=ISO_5V`；`input_ground=ISO_GND`；`output_supply=BUS_5V`；`output_ground=GND`；`isolation_module=F0505S-2WR3` |
| 电源 | U5 ME6211A3BM3G | `input=BUS_5V`；`output=+3.3V`；`input_cap=C20 10uF`；`output_caps=C21 100nF,C22 10uF` |
| 总线 | U3 CA-IS3050G | `logic_supply=+3.3V/GND`；`logic_rx=CAN_RX -> U3.2 RxD`；`logic_tx=CAN_TX -> U3.3 TxD`；`isolated_supply=ISO_5V/ISO_GND`；`physical=U3.7 CANH CAN_H,U3.6 CANL CAN_L` |
| 保护电路 | CAN_H/CAN_L 多级保护 | `series_fuses=F1,F2 60V 100mA/JK-NSMD010`；`esd=DZ1,DZ2 PESD5V0L1BA`；`tss=TSS1,TSS3 P0080TA`；`gdt=GDT1,GDT2 SMD4532-075`；`reference=ISO_GND/SHIELD` |
| 总线 | CAN 120R 终端 | `resistor=R7 120R`；`switch=S1 SW-SPST`；`terminal_1=CAN_H`；`terminal_2=CAN_L`；`switchable=true` |
| 接口 | P3/P4 PwrCAN | `pin_4=HPWR`；`pin_3=ISO_GND`；`pin_2=CAN_L`；`pin_1=CAN_H`；`ports=P3,P4 parallel` |
| 总线 | U1 CA-IS3082 与方向控制 | `receive=U1.3 RO -> R13 1K -> 485_RX`；`transmit=485_TX -> U1.6 DI`；`enable_node=U1.4 RE# + U1.5 DE`；`control=Q2 BSS138,R3 4.7K,R5 1K` |
| 总线 | U1 隔离侧 RS485 | `supply=ISO_5V/ISO_GND`；`B=U1.13 RS485_B`；`A=U1.12 RS485_A`；`B_bias=R4 4.7K to ISO_GND`；`A_bias=R8 4.7K to ISO_5V` |
| 保护电路 | RS485 TVS | `B_to_ground=D1 SMAJ6.8CA`；`B_to_A=D2 SMAJ6.8CA`；`A_to_ground=D3 SMAJ6.8CA` |
| 总线 | RS485 120R 终端 | `resistor=R6 120R`；`switch=S2 SW-SPST`；`terminal_1=RS485_B`；`terminal_2=RS485_A`；`switchable=true` |
| 接口 | P1 HT3.96 4P | `pin_4=RS485_B`；`pin_3=RS485_A`；`pin_2=HPWR via Q3 AP40P04Q`；`pin_1=ISO_GND` |
| GPIO 与控制信号 | CAN/RS485 GPIO 选择 | `can_header=P5 CAN_TX,CAN_RX,GPIO13,GPIO17,GPIO16,GPIO35`；`rs485_header=P6 GPIO34,GPIO0,GPIO15,GPIO12,485_TX,485_RX`；`selectors=SW1 CAN,SW2 RS485`；`warning=simultaneous selection conflicts are not electrically prevented` |
| 接口 | J1 M5Stack_BUS | `ground=pins1,3,5`；`selectable_gpio=pin2 GPIO35,pin15 GPIO16,pin16 GPIO17,pin21 GPIO12,pin22 GPIO13,pin23 GPIO15,pin24 GPIO0,pin26 GPIO34`；`3v3=pin12`；`5v=pin28 BUS_5V`；`battery=pin30 BAT` |
| 核心器件 | CA-IS3082/CA-IS3082W | `documented_model=CA-IS3082W`；`schematic_label=CA-IS3082`；`assembly_model=null` |
| 总线 | 正文中的总线能力 | `documented_can_rate=1Mbps`；`documented_can_nodes=110`；`documented_rs485_rate=500Kbps`；`documented_rs485_nodes=256`；`parameters_on_schematic=null` |
| 电源 | 正文中的 9-24V 与带载 | `documented_input=9-24V`；`documented_isolated_output=4.70V@218mA`；`documented_nonisolated_output=4.70V@1.1A`；`ratings_on_schematic=null` |
| 其他事实 | 时钟与存储 | `mcu_shown=false`；`can_controller_shown=false`；`crystal_shown=false`；`external_storage_shown=false` |

## 待确认事项

- `component.rs485-model-suffix`：产品正文列出 CA-IS3082W，原理图 U1 文本为 CA-IS3082；当前页面无法确认量产器件是否带 W 后缀。（证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 U1 底部 CA-IS3082）
- `bus.documented-rates-nodes`：正文列出 CAN 1Mbps/110 节点与 RS485 500Kbps/256 节点及距离测试；原理图未标速率、节点数或测试条件，需由收发器 datasheet 和实测确认。（证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 U3/U1 与接口，无速率/节点标注）
- `power.documented-input-load`：正文给出 9-24V 输入和隔离/非隔离输出带载测试；原理图显示 SMAJ30CA、ME3116 与 F0505S-2WR3 拓扑，但未标完整输入额定范围或输出电流能力。（证据：图 122fe8e39a98 / 第 1 页 / 第 1 页 P2/U2/U4/U5 电源链）
- `review.rs485-model`：请用 M139 当前 BOM/丝印确认 U1 是 CA-IS3082 还是 CA-IS3082W。；原因：正文与原理图后缀不一致。
- `review.rates-nodes`：请以器件 datasheet、线缆/终端条件和测试报告确认 CAN/RS485 最大速率、节点数与距离。；原因：这些系统指标未标在图纸。
- `review.power-ratings`：请确认 HPWR 9-24V 额定范围、各接口直通限制、隔离/非隔离输出电流与热限制。；原因：原理图拓扑不能替代额定值和测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `122fe8e39a988f62179404919dda8fb4804df821a5a099ec60a6727604b04972` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/565/SCH_Module_PwrCan_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/Module13.2-PwrCAN.md`

源文档 SHA-256：`ac0dbc87d20caccfdb004a1c9761e31d3b740abd9e9b6b4faa9b7d360bd1eaa7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
