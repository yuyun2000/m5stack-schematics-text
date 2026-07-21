# Module13.2 RS232M 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 RS232M |
| SKU | M131 |
| 产品 ID | `module13-2-rs232m-43012a76a175` |
| 源文档 | `zh_CN/module/RS232M Module 13.2.md` |

## 概述

Module13.2 RS232M 以 U2 TD301D232H 完成 3.3V UART 与隔离侧 RS-232 的全双工转换，RS-232 端通过自恢复保险丝、SMAJ18CA、气体放电管及 EARTH 耦合网络连接 HT3.96 端子和 DB9 公头。P1 外部 DC/HPWR 经 U3 ME3116 生成 ISO_5V，再由 U1 F0505S-2WR3 隔离为 BUS_5V，U4 HX6306P332MR 生成 VCC_3V3。S1 可在 DB9 上切换直通/交叉线序，SW1/SW2 分别把逻辑 RX/TX 选择到五组 M5-Bus GPIO。默认拨码位置、9-24V/115200bps 正文额定值和 M5-Bus 5V 针号标注差异无法仅凭本页确定，均列为待确认。

## 检索关键词

`Module13.2 RS232M`、`M131`、`TD301D232H`、`F0505S-2WR3`、`ME3116`、`HX6306P332MR`、`RS-232`、`DB9 Male`、`HT3.96 4P`、`DC050-T`、`ISO_5V`、`BUS_5V`、`VCC_3V3`、`ISO_GND`、`EARTH`、`R_IN`、`T_OUT`、`RXD1`、`TXD1`、`SMAJ30CA`、`SMAJ18CA`、`DSS34`、`JK-NSMD010`、`GDT1`、`GDT2`、`GPIO35`、`GPIO34`、`GPIO13`、`GPIO16`、`GPIO3`、`GPIO0`、`GPIO12`、`GPIO15`、`GPIO17`、`GPIO1`、`Passthrough`、`Cross`、`HPWR`、`115200bps`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | TD301D232H | VCC_3V3 逻辑 UART 与 ISO_GND 参考 RS-232 RIN/TOUT 之间的隔离式收发器 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B1-B2 U2 TD301D232H |
| U1 | F0505S-2WR3 | ISO_5V/ISO_GND 到 BUS_5V/GND 的 5V 隔离 DC/DC 模块 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 A3 U1 F0505S-2WR3 |
| U3 | ME3116 | 把 HPWR 外部输入降压为 ISO_5V 的开关稳压器 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 A1-A2 U3 ME3116 |
| U4 | HX6306P332MR | 把 BUS_5V 稳压为 VCC_3V3 的 LDO | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 A3-A4 U4 HX6306P332MR |
| P1 | DC050-T | HPWR/ISO_GND 外部 DC 圆孔电源输入 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 A1 P1 DC050-T |
| P2 | HT3.96 4P | R_IN、T_OUT、HPWR、ISO_GND 四针现场端子 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 C3 P2 HT3.96 4P |
| J1 | DB9 Male | 可经 S1 选择直通或交叉 RXD1/TXD1 的 RS-232 公头 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B4-C4 J1 DB9 Male |
| J3 | M5_BUS | M5Stack 主机接口，连接可选 UART GPIO、BUS_5V 和 GND | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 C4-D4 J3 M5_BUS |
| S1 | SS-1260 | R_IN/T_OUT 到 DB9 RXD1/TXD1 的直通/交叉双刀切换开关 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B3 S1 SS-1260 Passthrough/Cross |
| SW1/SW2 | 未标注 | 分别为 RX 和 TX 选择 M5-Bus GPIO 的五路编码/拨码开关 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 C2-D3 SW1/SW2 |
| F1/F2 | 60V 100mA/JK-NSMD010 | R_IN 与 T_OUT 串联自恢复保险丝 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2 F1/F2 |
| D3/D5 | SMAJ18CA | RS-232 RIN/TOUT 到 ISO_GND 的双向浪涌抑制器 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2-C2 D3/D5 SMAJ18CA |
| GDT1/GDT2 | 未标注 | R_IN/T_OUT 到 EARTH 的气体放电保护器件 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2-C2 GDT1/GDT2 |
| D6 | SMAJ30CA | HPWR 输入对 ISO_GND 的浪涌/瞬态抑制器 | 图 d5aa90af83e8 / 第 1 页 / 第 1 页 A1 D6 SMAJ30CA |

## 系统结构

### Module13.2 RS232M

U2 TD301D232H 在 VCC_3V3/GND 主机逻辑域和 ISO_GND RS-232 域之间转换 RX/TX；U1 F0505S-2WR3 提供电源隔离，S1、SW1、SW2 分别选择 DB9 线序和主机 GPIO。

- 参数与网络：`transceiver=U2 TD301D232H`；`isolated_dcdc=U1 F0505S-2WR3`；`line_switch=S1 SS-1260`；`gpio_switches=SW1/SW2`；`logic_domain=VCC_3V3/GND`；`field_domain=ISO_GND`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页完整功能分区

## 电源

### P1 HPWR 输入

P1 DC050-T 将正端接 HPWR、负端接 ISO_GND；D6 SMAJ30CA 跨接输入，C1/C5 各 10uF、C4 100nF 对 ISO_GND 滤波。

- 参数与网络：`connector=P1 DC050-T`；`positive=HPWR`；`negative=ISO_GND`；`tvs=D6 SMAJ30CA`；`capacitors=C1 10uF,C5 10uF,C4 100nF`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 A1 P1/D6/C1/C5/C4

### U3 ME3116

U3 VIN 接 HPWR，EN 经 R1 100K 接 HPWR，LX 经 L1 6.8uH 与 D4 DSS34 形成降压级，输出网为 ISO_5V；R2 210K、R3 40.2K 和 C9 100pF 构成反馈补偿网络。

- 参数与网络：`input=HPWR`；`output=ISO_5V`；`enable=R1 100K to HPWR`；`inductor=L1 6.8uH`；`diode=D4 DSS34`；`feedback=R2 210K,R3 40.2K,C9 100pF`；`output_caps=C10 10uF,C11 100nF`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 A1-A3 U3 降压网络

### U1 F0505S-2WR3

U1 输入侧接 ISO_5V/ISO_GND，输出侧 +VO/0V 形成 BUS_5V/GND；C2 10uF、C6 100nF 和 D2 跨接 BUS_5V/GND。

- 参数与网络：`input=ISO_5V/ISO_GND`；`output=BUS_5V/GND`；`output_caps=C2 10uF,C6 100nF`；`output_clamp=D2`；`galvanic_domains=ISO_GND vs GND`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 A3 U1 与 BUS_5V

### U4 HX6306P332MR

U4 VIN 接 BUS_5V、VOUT 输出 VCC_3V3、GND 接主机侧 GND，C12/C13 各 10uF 分别位于输入和输出。

- 参数与网络：`input=BUS_5V`；`output=VCC_3V3`；`ground=GND`；`input_cap=C12 10uF`；`output_cap=C13 10uF`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 A4 U4

## 接口

### P2 HT3.96 4P

P2.4=R_IN，P2.3=T_OUT，P2.2=HPWR，P2.1=ISO_GND；同一端子同时提供隔离侧 RS-232 和外部电源输入。

- 参数与网络：`pin_4=R_IN`；`pin_3=T_OUT`；`pin_2=HPWR`；`pin_1=ISO_GND`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 C3 P2

### J1 DB9 Male

J1.2 连接 RXD1，J1.3 连接 TXD1，J1.5 连接 ISO_GND，外壳 10/11 连接 EARTH，其余 DB9 信号针未连接。

- 参数与网络：`pin_2=RXD1`；`pin_3=TXD1`；`pin_5=ISO_GND`；`shell_10_11=EARTH`；`unused=1,4,6,7,8,9`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B4-C4 J1 DB9

### S1 线序切换

S1 的 Passthrough 位置把 R_IN 接 RXD1、T_OUT 接 TXD1；Cross 位置把 R_IN 接 TXD1、T_OUT 接 RXD1。

- 参数与网络：`passthrough=R_IN->RXD1,T_OUT->TXD1`；`cross=R_IN->TXD1,T_OUT->RXD1`；`switch=S1 SS-1260`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B3 S1 Passthrough/Cross

### J3 M5_BUS

J3 引出 SW1/SW2 所用 GPIO35、GPIO34、GPIO13、GPIO16、GPIO3、GPIO0、GPIO12、GPIO15、GPIO17、GPIO1；GND 接连接器地针，BUS_5V 接原理图右下 5V 端。

- 参数与网络：`rx_gpio=GPIO35,GPIO34,GPIO13,GPIO16,GPIO3`；`tx_gpio=GPIO0,GPIO12,GPIO15,GPIO17,GPIO1`；`ground=GND`；`power=BUS_5V`；`hpwr_pin_labels=26,28,30 HPWR`；`battery=BAT NC`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 C4-D4 J3 与 SW1/SW2

## 总线

### U2 RX/TX 逻辑侧

U2.4 RXD 输出连接 RX，U2.3 TXD 输入连接 TX，U2.1 VCC 接 VCC_3V3，U2.2 GND 接主机侧 GND；C7 100nF 为 VCC_3V3 去耦。

- 参数与网络：`receive_output=U2.4 RXD -> RX`；`transmit_input=TX -> U2.3 TXD`；`supply=U2.1 VCC_3V3`；`ground=U2.2 GND`；`decoupling=C7 100nF`；`logic_level_rail=3.3V`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B1 U2 左侧 RX/TX/VCC

### U2 RS-232 侧

U2.6 RIN 经 F1 到 R_IN，U2.7 TOUT 经 F2 到 T_OUT，U2.8 RGND 接 ISO_GND；R_IN 为外部接收输入，T_OUT 为模块发送输出。

- 参数与网络：`receive=R_IN -> F1 -> U2.6 RIN`；`transmit=U2.7 TOUT -> F2 -> T_OUT`；`reference=U2.8 RGND ISO_GND`；`fuses=F1/F2 60V 100mA/JK-NSMD010`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2 U2 RIN/TOUT/RGND

## GPIO 与控制信号

### SW1 RX 选择

SW1 将公共 RX 分别通过五个独立开关连接 GPIO35、GPIO34、GPIO13、GPIO16、GPIO3。

- 参数与网络：`common=RX`；`position_1=GPIO35`；`position_2=GPIO34`；`position_3=GPIO13`；`position_4=GPIO16`；`position_5=GPIO3`；`switch_pins=10,9,8,7,6`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 C2-D3 SW1

### SW2 TX 选择

SW2 将公共 TX 分别通过五个独立开关连接 GPIO0、GPIO12、GPIO15、GPIO17、GPIO1。

- 参数与网络：`common=TX`；`position_1=GPIO0`；`position_2=GPIO12`；`position_3=GPIO15`；`position_4=GPIO17`；`position_5=GPIO1`；`switch_pins=10,9,8,7,6`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 D2-D3 SW2

## 时钟

### 外部时钟

完整原理图未显示晶振、振荡器或时钟网络。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页完整图无时钟器件

## 保护电路

### R_IN/T_OUT 多级保护

R_IN/T_OUT 各经 F1/F2 60V 100mA 自恢复保险丝；收发器侧分别由 D3/D5 SMAJ18CA 对 ISO_GND 钳位，外部侧分别由 GDT1/GDT2 向 EARTH 泄放。

- 参数与网络：`series=F1/F2 60V 100mA/JK-NSMD010`；`tvs=D3/D5 SMAJ18CA to ISO_GND`；`gdt=GDT1/GDT2 to EARTH`；`protected_nets=R_IN,T_OUT`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2-C2 F1/F2/D3/D5/GDT1/GDT2

### EARTH 与 ISO_GND

EARTH 通过 R8 1MΩ 与 C8 1nF/2KV 并联网络耦合到 ISO_GND，并连接 DB9 外壳 10/11 和 GDT1/GDT2。

- 参数与网络：`resistor=R8 1MΩ`；`capacitor=C8 1nF/2KV`；`earth_nodes=DB9 shell 10/11,GDT1,GDT2`；`isolated_ground=ISO_GND`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 B2-C2 R8/C8/EARTH

## 关键网络

### GND/ISO_GND/EARTH

原理图明确区分主机侧 GND、RS-232/外部电源侧 ISO_GND 和机壳浪涌节点 EARTH；U1 隔离 DC/DC 跨越 GND 与 ISO_GND，R8/C8 仅把 EARTH 耦合到 ISO_GND。

- 参数与网络：`logic_ground=GND`；`field_ground=ISO_GND`；`chassis_node=EARTH`；`isolation_barrier=U1 F0505S-2WR3`；`earth_coupling=R8/C8`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页全图 GND/ISO_GND/EARTH 网络

## 内存与 Flash

### 外部存储器

完整原理图未展示主控、Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`local_mcu_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页完整图无主控或存储器

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 RS232M | `transceiver=U2 TD301D232H`；`isolated_dcdc=U1 F0505S-2WR3`；`line_switch=S1 SS-1260`；`gpio_switches=SW1/SW2`；`logic_domain=VCC_3V3/GND`；`field_domain=ISO_GND` |
| 电源 | P1 HPWR 输入 | `connector=P1 DC050-T`；`positive=HPWR`；`negative=ISO_GND`；`tvs=D6 SMAJ30CA`；`capacitors=C1 10uF,C5 10uF,C4 100nF` |
| 电源 | U3 ME3116 | `input=HPWR`；`output=ISO_5V`；`enable=R1 100K to HPWR`；`inductor=L1 6.8uH`；`diode=D4 DSS34`；`feedback=R2 210K,R3 40.2K,C9 100pF`；`output_caps=C10 10uF,C11 100nF` |
| 电源 | U1 F0505S-2WR3 | `input=ISO_5V/ISO_GND`；`output=BUS_5V/GND`；`output_caps=C2 10uF,C6 100nF`；`output_clamp=D2`；`galvanic_domains=ISO_GND vs GND` |
| 电源 | U4 HX6306P332MR | `input=BUS_5V`；`output=VCC_3V3`；`ground=GND`；`input_cap=C12 10uF`；`output_cap=C13 10uF` |
| 总线 | U2 RX/TX 逻辑侧 | `receive_output=U2.4 RXD -> RX`；`transmit_input=TX -> U2.3 TXD`；`supply=U2.1 VCC_3V3`；`ground=U2.2 GND`；`decoupling=C7 100nF`；`logic_level_rail=3.3V` |
| 总线 | U2 RS-232 侧 | `receive=R_IN -> F1 -> U2.6 RIN`；`transmit=U2.7 TOUT -> F2 -> T_OUT`；`reference=U2.8 RGND ISO_GND`；`fuses=F1/F2 60V 100mA/JK-NSMD010` |
| GPIO 与控制信号 | SW1 RX 选择 | `common=RX`；`position_1=GPIO35`；`position_2=GPIO34`；`position_3=GPIO13`；`position_4=GPIO16`；`position_5=GPIO3`；`switch_pins=10,9,8,7,6` |
| GPIO 与控制信号 | SW2 TX 选择 | `common=TX`；`position_1=GPIO0`；`position_2=GPIO12`；`position_3=GPIO15`；`position_4=GPIO17`；`position_5=GPIO1`；`switch_pins=10,9,8,7,6` |
| 其他事实 | SW1/SW2 默认位置 | `rx_options=GPIO35,GPIO34,GPIO13,GPIO16,GPIO3`；`tx_options=GPIO0,GPIO12,GPIO15,GPIO17,GPIO1`；`default_rx=null`；`default_tx=null`；`electrical_interlock_shown=false` |
| 接口 | P2 HT3.96 4P | `pin_4=R_IN`；`pin_3=T_OUT`；`pin_2=HPWR`；`pin_1=ISO_GND` |
| 接口 | J1 DB9 Male | `pin_2=RXD1`；`pin_3=TXD1`；`pin_5=ISO_GND`；`shell_10_11=EARTH`；`unused=1,4,6,7,8,9` |
| 接口 | S1 线序切换 | `passthrough=R_IN->RXD1,T_OUT->TXD1`；`cross=R_IN->TXD1,T_OUT->RXD1`；`switch=S1 SS-1260` |
| 保护电路 | R_IN/T_OUT 多级保护 | `series=F1/F2 60V 100mA/JK-NSMD010`；`tvs=D3/D5 SMAJ18CA to ISO_GND`；`gdt=GDT1/GDT2 to EARTH`；`protected_nets=R_IN,T_OUT` |
| 保护电路 | EARTH 与 ISO_GND | `resistor=R8 1MΩ`；`capacitor=C8 1nF/2KV`；`earth_nodes=DB9 shell 10/11,GDT1,GDT2`；`isolated_ground=ISO_GND` |
| 关键网络 | GND/ISO_GND/EARTH | `logic_ground=GND`；`field_ground=ISO_GND`；`chassis_node=EARTH`；`isolation_barrier=U1 F0505S-2WR3`；`earth_coupling=R8/C8` |
| 接口 | J3 M5_BUS | `rx_gpio=GPIO35,GPIO34,GPIO13,GPIO16,GPIO3`；`tx_gpio=GPIO0,GPIO12,GPIO15,GPIO17,GPIO1`；`ground=GND`；`power=BUS_5V`；`hpwr_pin_labels=26,28,30 HPWR`；`battery=BAT NC` |
| 接口 | M5-Bus 5V 针号 | `schematic_label=5V-27 / BUS_5V`；`document_table=pin 28 = 5V`；`resolved_pin=null` |
| 其他事实 | 正文额定输入与波特率 | `documented_input=9-24V DC`；`documented_baud=up to 115200bps`；`rating_on_schematic=null`；`test_conditions_on_schematic=null` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `local_mcu_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `other.selector-default`：原理图展示 RX/TX 各五个可闭合路径，但没有标注出厂默认开关位置，也没有阻止同时闭合多路的电气互锁。（证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 C2-D3 SW1/SW2 无默认标记）
- `interface.m5bus-5v-numbering`：原理图 J3 右下把 BUS_5V 接到标注为 5V-27 的端点，而产品正文针脚表列出 28=5V；两处针号表达不一致，需结合连接器封装确认。（证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 D4 J3 右下 BUS_5V）
- `other.documented-ratings`：正文给出 DC 输入 9-24V 和最高 115200bps；原理图展示 SMAJ30CA、ME3116 与 TD301D232H 电路，但未标注完整工作范围或波特率测试条件。（证据：图 d5aa90af83e8 / 第 1 页 / 第 1 页 P1/U3/U2 无输入范围或波特率标注）
- `review.selector-default`：请依据出厂配置或实物确认 SW1/SW2 的默认 RX/TX GPIO 位置，并确认是否允许同时闭合多路。；原因：原理图只给出五路选择关系，没有默认位置或互锁说明。
- `review.m5bus-5v-numbering`：请依据 J3 封装/PCB 确认 BUS_5V 的物理针号，并统一原理图与正文针脚表。；原因：原理图标注 5V-27，正文针脚表列 28=5V。
- `review.documented-ratings`：请依据 U3/U2 数据手册及产品测试报告确认 9-24V 输入范围和 115200bps 上限的条件。；原因：原理图未标完整额定范围和通信测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d5aa90af83e8c095902a8d6cbf5b6da1c4ff72bc404ada293f064e8aca98e7c0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/558/Sch_Module_13.2_RS232M_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/RS232M Module 13.2.md`

源文档 SHA-256：`4afc0b558f6598265da1e8ff03f36eb6b5354ecbb194ce94c92c60d884f15d8c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
