# Hat RS485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat RS485 |
| SKU | U067 |
| 产品 ID | `hat-rs485-9c47adff6d40` |
| 源文档 | `zh_CN/hat/hat-rs485.md` |

## 概述

Hat RS485 以 U1 SP485EEN-L/TR 为 RS-485 收发器，RO 通过 G26 返回主机，G0 经 Q1 控制 RE/DE 自动收发节点，A/B 侧配置偏置、可选终端和浪涌保护。P1 引出 RS485_B、RS485_A、+12V 和 GND；U2 AOZ1282CI 将 +12V 降为 +5VIN，经 P2 送入 M5StickC。收发器本身由 P2 5VOUT/+5V 供电。

## 检索关键词

`Hat RS485`、`U067`、`SP485EEN-L/TR`、`SP485EEN`、`AOZ1282CI`、`SS8050 Y1`、`RS485_A`、`RS485_B`、`G26 RO`、`G0 auto direction`、`+12V`、`+5V`、`+5VIN`、`R4 120R NC`、`R1 4.7K`、`R6 4.7K`、`SMAJ6.5CA-E3`、`B5819W SL`、`L1 4.7uH`、`P1 Header 4`、`P2 STICKIO`、`R2 1K`、`R5 4.7K`、`115200`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SP485EEN-L/TR | RS-485 差分收发器 | 图 45f014af0cc3 / 第 1 页 / 第1页上部：U1 SP485EEN-L/TR pins1-8 |
| U2 | AOZ1282CI | +12V 到 +5VIN 的降压转换器 | 图 45f014af0cc3 / 第 1 页 / 第1页左中：U2 AOZ1282CI |
| Q1 | SS8050 Y1 | 由 G0/T0 驱动的 RS-485 RE/DE 自动收发控制晶体管 | 图 45f014af0cc3 / 第 1 页 / 第1页左上：Q1 SS8050 Y1、R3/R5 |
| P1 | Header 4 | RS485_B、RS485_A、+12V 与 GND 外部端子 | 图 45f014af0cc3 / 第 1 页 / 第1页右上：P1 Header 4 |
| P2 | STICKIO | 主机 5V、5VIN、G26、G0 与 GND 接口 | 图 45f014af0cc3 / 第 1 页 / 第1页右下：P2 STICKIO pins1-8 |
| D1-D3 | SMAJ6.5CA-E3 | RS485_A/B 对地与线间浪涌钳位 | 图 45f014af0cc3 / 第 1 页 / 第1页右上：D1-D3 SMAJ6.5CA-E3 |
| D4 | B5819W SL | AOZ1282CI 降压续流二极管 | 图 45f014af0cc3 / 第 1 页 / 第1页中部：D4 B5819W SL |
| L1 | 4.7uH | AOZ1282CI LX 到 +5VIN 的储能电感 | 图 45f014af0cc3 / 第 1 页 / 第1页中部：L1 4.7uH |

## 系统结构

### Hat RS485 架构

P2 提供主机 G26/G0 与 +5V，U1 SP485EEN-L/TR 完成 RS-485 收发，Q1 控制 RE/DE；P1 引出 A/B 和 +12V，U2 将 +12V 降为 +5VIN。

- 参数与网络：`transceiver=U1 SP485EEN-L/TR`；`auto_control=Q1 SS8050 Y1`；`buck=U2 AOZ1282CI`；`field_connector=P1`；`host=P2`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页完整单页

## 电源

### +12V 到 +5VIN

U2 AOZ1282CI VIN pin5 接 +12V，EN pin4 由 R7 100KΩ上拉；LX pin6 经 L1 4.7uH 与 D4 B5819W SL 输出 +5VIN，FB 使用 R8 51KΩ/R9 10KΩ。

- 参数与网络：`converter=U2 AOZ1282CI`；`input=+12V`；`enable=R7 100KΩ to +12V`；`inductor=L1 4.7uH`；`diode=D4 B5819W SL`；`output=+5VIN`；`feedback=R8 51KΩ; R9 10KΩ`；`caps=C3/C4/C5 10uF`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页中部：U2/R7-R9/L1/D4/C3-C5

### +5V 与 +5VIN 电源路径

P2 pin2/5VOUT 提供 +5V，为 U1 VCC pin8、Q1 控制上拉和偏置网络供电；U2 生成的 +5VIN 连接 P2 pin8/5VIN。

- 参数与网络：`host_5v=P2 pin2 5VOUT -> +5V`；`loads=U1 VCC,Q1/R3,R6,C1,C6`；`buck_output=+5VIN -> P2 pin8 5VIN`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页 U1 +5V/P2 pin2 与 U2 +5VIN/P2 pin8

## 接口

### P1 RS-485 与电源端子

P1 Header 4 pins1-4 依次为 RS485_B、RS485_A、+12V、GND。

- 参数与网络：`connector=P1 Header 4`；`pin1=RS485_B`；`pin2=RS485_A`；`pin3=+12V`；`pin4=GND`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页右上：P1 pins1-4

### P2 STICKIO 接口

P2 pin1 为 GND、pin2 为 5VOUT/+5V、pin3 G26 为 R0、pin5 G0 为 T0、pin8 5VIN 为 +5VIN；pins4 G36、6 BAT、7 3V3 未接入本页功能网络。

- 参数与网络：`pin1=GND`；`pin2=5VOUT/+5V`；`pin3=G26/R0`；`pin4=G36 unused`；`pin5=G0/T0`；`pin6=BAT unused`；`pin7=3V3 unused`；`pin8=5VIN/+5VIN`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页右下：P2 pins1-8

## 总线

### RS-485 接收路径

U1 RO pin1 经 R2 1KΩ形成 R0，并连接 P2 pin3/G26；R3 4.7KΩ将 R0 上拉到 +5V。

- 参数与网络：`source=U1 RO pin1`；`series=R2 1KΩ`；`net=R0`；`host=P2 pin3 / G26`；`pullup=R3 4.7KΩ to +5V`；`direction=transceiver output to host input`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页 U1 RO/R2/R3 与 P2 G26

### RS-485 自动收发控制

P2 pin5/G0 形成 T0，经 R5 4.7KΩ驱动 Q1 SS8050 Y1；Q1 集电极连接 U1 RE pin2 与 DE pin3，U1 DI pin4 在图中接 GND。

- 参数与网络：`host=P2 pin5 / G0`；`net=T0`；`base_resistor=R5 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U1 RE pin2; DE pin3`；`data_input=U1 DI pin4 -> GND`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页 U1 pins2-4、Q1/R5 与 P2 G0

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟输入。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### RS-485 偏置与终端

R1 4.7KΩ将 RS485_B 下拉到 GND，R6 4.7KΩ将 RS485_A 上拉到 +5V，R4 120Ω/NC 跨接 A/B 作为未装终端位。

- 参数与网络：`bias_b=R1 4.7KΩ to GND`；`bias_a=R6 4.7KΩ to +5V`；`termination=R4 120Ω/NC`；`lines=RS485_A,RS485_B`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页上部：R1/R4/R6

### RS-485 浪涌保护

D1 SMAJ6.5CA-E3 从 RS485_B 对地，D3 从 RS485_A 对地，D2 跨接 RS485_A/B。

- 参数与网络：`b_to_ground=D1 SMAJ6.5CA-E3`；`a_to_ground=D3 SMAJ6.5CA-E3`；`line_to_line=D2 SMAJ6.5CA-E3`
- 证据：图 45f014af0cc3 / 第 1 页 / 第1页右上：D1-D3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat RS485 架构 | `transceiver=U1 SP485EEN-L/TR`；`auto_control=Q1 SS8050 Y1`；`buck=U2 AOZ1282CI`；`field_connector=P1`；`host=P2` |
| 总线 | RS-485 接收路径 | `source=U1 RO pin1`；`series=R2 1KΩ`；`net=R0`；`host=P2 pin3 / G26`；`pullup=R3 4.7KΩ to +5V`；`direction=transceiver output to host input` |
| 总线 | RS-485 自动收发控制 | `host=P2 pin5 / G0`；`net=T0`；`base_resistor=R5 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`controlled_pins=U1 RE pin2; DE pin3`；`data_input=U1 DI pin4 -> GND` |
| 接口 | P1 RS-485 与电源端子 | `connector=P1 Header 4`；`pin1=RS485_B`；`pin2=RS485_A`；`pin3=+12V`；`pin4=GND` |
| 保护电路 | RS-485 偏置与终端 | `bias_b=R1 4.7KΩ to GND`；`bias_a=R6 4.7KΩ to +5V`；`termination=R4 120Ω/NC`；`lines=RS485_A,RS485_B` |
| 保护电路 | RS-485 浪涌保护 | `b_to_ground=D1 SMAJ6.5CA-E3`；`a_to_ground=D3 SMAJ6.5CA-E3`；`line_to_line=D2 SMAJ6.5CA-E3` |
| 电源 | +12V 到 +5VIN | `converter=U2 AOZ1282CI`；`input=+12V`；`enable=R7 100KΩ to +12V`；`inductor=L1 4.7uH`；`diode=D4 B5819W SL`；`output=+5VIN`；`feedback=R8 51KΩ; R9 10KΩ`；`caps=C3/C4/C5 10uF` |
| 电源 | +5V 与 +5VIN 电源路径 | `host_5v=P2 pin2 5VOUT -> +5V`；`loads=U1 VCC,Q1/R3,R6,C1,C6`；`buck_output=+5VIN -> P2 pin8 5VIN` |
| 接口 | P2 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT/+5V`；`pin3=G26/R0`；`pin4=G36 unused`；`pin5=G0/T0`；`pin6=BAT unused`；`pin7=3V3 unused`；`pin8=5VIN/+5VIN` |
| 总线 | 标称波特率 | `documented_bitrate=115200`；`explicit_bitrate_on_schematic=false`；`transceiver=SP485EEN-L/TR` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- `bus.documented-bitrate`：产品正文标称波特率 115200；原理图显示收发与自动方向电路，但未打印波特率。（证据：图 45f014af0cc3 / 第 1 页 / 第1页 U1/Q1 RS-485 circuit）
- `review.bitrate`：U067 默认或推荐 RS-485 波特率是否固定为 115200？；原因：115200 来自产品正文，原理图未打印波特率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `45f014af0cc3d3da440dc5de05daab196335905e8b32f98e79a0c52398bb9708` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-rs485/hat-rs485_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-rs485.md`

源文档 SHA-256：`830a7ef17b6de8384b9ee00d3c96dacdbd0ad75f097c91335d1e4a98a694ee0f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
