# Stamp-S3 GroveBreakOut 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3 GroveBreakOut |
| SKU | A144 |
| 产品 ID | `stamp-s3-grovebreakout-1f94bdf41b56` |
| 源文档 | `zh_CN/accessory/StampS3 GroveBreakOut.md` |

## 概述

Stamp-S3 GroveBreakOut 为 Stamp-S3 提供六个 Grove 接口、复位按键和多组排母，同时集成双电池输入、TP4057 充电、电池电压检测和电源切换。BAT_OUT 分别进入 SY8089AAAC 生成 VCC_3V3，以及 SY7088 升压生成 5Vin/BUS_5V。SW2 通过两路 LP3218DT1G 在 BUS_5V 与外部 VIN_5V 之间选择 Grove_5V，六个 Grove 端口分别引出 G1/G2、G4/G3、G6/G5、G10/G11、G9/G7 和 G15/G13。

## 检索关键词

`Stamp-S3 GroveBreakOut`、`StampS3 GroveBreakOut`、`A144`、`TP4057`、`SY8089AAAC`、`SY7088`、`LP3218DT1G`、`2N7002W`、`DSS34`、`BAT+`、`BAT_OUT`、`BAT_ADC`、`VIN_5V`、`VCC_3V3`、`BUS_5V`、`Grove_5V`、`Grove I2C`、`Grove UART`、`G1`、`G2`、`G3`、`G4`、`G5`、`G6`、`G7`、`G8`、`G9`、`G10`、`G11`、`G13`、`G15`、`SW-PWR1`、`SW2`、`CHRG`、`Header 9`、`Header 6`、`Header 17`、`Header 11`、`EN`、`G0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | TP4057 | VIN_5V 输入的单节锂电池充电管理芯片 | 图 d83bf4e9759b / 第 1 页 / 网格 2A-3B，U3 TP4057、VIN_5V、BAT+、CHRG、STDBY 和 PROG |
| U1 | SY8089AAAC | BAT_OUT 到 VCC_3V3 的降压转换器 | 图 d83bf4e9759b / 第 1 页 / 网格 3A-4A，U1 SY8089AAAC、L1、反馈分压与 BAT_OUT/VCC_3V3 |
| U2 | SY7088 | BAT_OUT 到 5Vin 的升压转换器 | 图 d83bf4e9759b / 第 1 页 / 网格 3B-4B，U2 SY7088、L2、BAT_OUT、5Vin、反馈和输出电容 |
| P1 | 未标注 | 第一路电池输入连接器/电池座 | 图 d83bf4e9759b / 第 1 页 / 网格 1A，P1 正端经 Q1/F1 到 BAT+，负端接 GND |
| BT1 | Battery | 第二路电池输入 | 图 d83bf4e9759b / 第 1 页 / 网格 1B，BT1 正端经 Q2 到 BAT+，负端接 GND |
| Q1,Q2 | LP3218DT1G | 两路电池输入的高边路径器件 | 图 d83bf4e9759b / 第 1 页 / 网格 1A-B，Q1/Q2 LP3218DT1G 分别串联 P1/BT1 正端到 BAT+ 汇合节点 |
| Q5,Q6 | 2N7002W | 配合 Q1/Q2 的电池输入门极控制器件 | 图 d83bf4e9759b / 第 1 页 / 网格 1A-B，Q5/Q6 2N7002W、R15/R16 100K 与 Q1/Q2 门极网络 |
| F1 | Fuse 0805 2A/6V | P1 电池输入支路保险丝 | 图 d83bf4e9759b / 第 1 页 / 网格 1A，F1 串联 Q1 输出和 BAT+ |
| SW1 | SW-PWR1 | BAT+ 到 BAT_OUT 的电池电源开关 | 图 d83bf4e9759b / 第 1 页 / 网格 1A-2A，SW1 pin1=BAT+、pin2=BAT_OUT、pin3 未接 |
| SW2 | 未标注 | Grove_5V 供电来源选择开关 | 图 d83bf4e9759b / 第 1 页 / 网格 1C-D，SW2 common pin2 接 GND，pin3 控制 Q3，pin1 控制 Q4 |
| Q3,Q4 | LP3218DT1G | BUS_5V 与 VIN_5V 到 Grove_5V 的双路高边选择器件 | 图 d83bf4e9759b / 第 1 页 / 网格 1C-D，Q3 从 BUS_5V、Q4 从 VIN_5V/D4 输出到公共 Grove_5V |
| D3,D4 | DSS34 | 5Vin 到 BUS_5V 及 VIN_5V 到 Grove 供电支路的肖特基隔离二极管 | 图 d83bf4e9759b / 第 1 页 / 网格 4B D3 位于 5Vin/BUS_5V，网格 1D D4 位于 VIN_5V/Q4 输入 |
| J1,J2,J3,J4,J5,J6 | GROVE | 六组 Grove 信号与 Grove_5V/GND 接口 | 图 d83bf4e9759b / 第 1 页 / 网格 2C-3D，J1-J6 六个 GROVE 连接器及各自 IO1/IO2、5V、GND 网络 |
| P2,P3 | Header 9 / Header 6 | 一组 Stamp-S3 插接排母 | 图 d83bf4e9759b / 第 1 页 / 网格 3C-4C，P2 Header 9 与 P3 Header 6 的 GPIO、电源、EN 和 GND |
| P4,P5 | Header 17 / Header 11 | 另一组 Stamp-S3 GPIO 与电源排母 | 图 d83bf4e9759b / 第 1 页 / 网格 3C-4D，P4 Header 17 与 P5 Header 11 的完整引脚标注 |
| S1 | SW_TS_015 | Stamp-S3 EN 复位按键 | 图 d83bf4e9759b / 第 1 页 / 网格 4D，S1 按下将 EN 连接 GND |

## 系统结构

### Stamp-S3 GroveBreakOut 系统架构

扩展板由双电池输入与充电、电源开关、3.3V 降压、5V 升压、Grove_5V 来源选择、六个 Grove 端口、Stamp-S3 排母和 EN 复位按键组成。

- 参数与网络：`battery_inputs=2`；`charger=U3 TP4057`；`three_v_three_converter=U1 SY8089AAAC`；`five_volt_converter=U2 SY7088`；`grove_ports=6`；`reset_switch=S1`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1A-4D，完整单页原理图的电池、电源、BUS、Grove 和排母功能区

## 电源

### 双电池输入到 BAT+

P1 正端经 Q1 LP3218DT1G 和 F1 2A/6V 保险丝接 BAT+；BT1 正端经 Q2 LP3218DT1G 接同一 BAT+，两路负端均接 GND。

- 参数与网络：`input_1=P1 -> Q1 -> F1 -> BAT+`；`input_2=BT1 -> Q2 -> BAT+`；`fused_branch=P1`；`common_net=BAT+`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1A-B，P1、BT1、Q1、Q2、F1 与 BAT+ 汇合节点

### 电池输入门极控制

Q5/Q6 2N7002W 分别连接 Q1/Q2 的控制节点，R15/R16 各 100kΩ 连接到 BAT+ 汇合侧。

- 参数与网络：`branch_1=Q1 LP3218DT1G with Q5 2N7002W and R15 100kΩ`；`branch_2=Q2 LP3218DT1G with Q6 2N7002W and R16 100kΩ`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1A-B，Q1/Q5/R15 与 Q2/Q6/R16 两组电路

### BAT+ 到 BAT_OUT 开关

SW1 SW-PWR1 的 pin1 接 BAT+、pin2 接 BAT_OUT、pin3 未连接，用于接通或断开电池输出。

- 参数与网络：`switch=SW1 SW-PWR1`；`input_pin=1 BAT+`；`output_pin=2 BAT_OUT`；`unused_pin=3`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1A-2A，SW1 的 BAT+、BAT_OUT 和未连接端

### TP4057 充电路径

VIN_5V 经 R3 1Ω 进入 U3 TP4057 VCC pin4，BAT pin3 连接 BAT+，PROG pin6 通过 R7 2.2kΩ 接 GND，STDBY pin5 未连接。

- 参数与网络：`charger=U3 TP4057`；`input=VIN_5V via R3 1Ω`；`battery_output=BAT+`；`program_resistor=R7 2.2kΩ`；`standby_pin=NC`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2A-B，U3、R3、R7、VIN_5V、BAT+ 和 STDBY 未连接标记

### BAT_OUT 到 VCC_3V3

U1 SY8089AAAC 的 IN 与 EN 接 BAT_OUT，经 L1 2.2uH 输出 VCC_3V3；反馈网络为 R1 68kΩ、R2 15kΩ 和 C4 22pF。

- 参数与网络：`converter=U1 SY8089AAAC`；`input=BAT_OUT`；`output=VCC_3V3`；`inductor=L1 2.2uH/2520`；`feedback=R1 68kΩ, R2 15kΩ, C4 22pF`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3A-4A，U1、L1、BAT_OUT、VCC_3V3、R1、R2、C4

### BAT_OUT 到 5Vin 升压

U2 SY7088 由 BAT_OUT 供电，经 L2 1.5uH 升压到 5Vin；EN 通过 R6 100kΩ 接 BAT_OUT，反馈网络为 R5 51kΩ 与 R8 15kΩ。

- 参数与网络：`converter=U2 SY7088`；`input=BAT_OUT`；`output=5Vin`；`inductor=L2 1.5uH/2520`；`enable_pull=R6 100kΩ`；`feedback=R5 51kΩ, R8 15kΩ`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3B-4B，U2、L2、BAT_OUT、5Vin、R5、R6、R8

### 5Vin 到 BUS_5V

SY7088 输出 5Vin 经 D3 DSS34 串联二极管连接 BUS_5V。

- 参数与网络：`source=5Vin`；`diode=D3 DSS34`；`destination=BUS_5V`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 4B，5Vin、D3 DSS34 与 BUS_5V

### Grove_5V 双电源选择

Q3 将 BUS_5V 接到 Grove_5V，Q4 将经 D4 DSS34 隔离的 VIN_5V 接到 Grove_5V；SW2 通过把相应控制节点接地选择一路，R13/R14 各 100kΩ 提供偏置。

- 参数与网络：`battery_boost_source=BUS_5V -> Q3 -> Grove_5V`；`external_source=VIN_5V -> D4 DSS34 -> Q4 -> Grove_5V`；`selector=SW2`；`bias_resistors=R13 100kΩ, R14 100kΩ`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1C-D，BUS_5V/Q3、VIN_5V/D4/Q4、SW2、R13、R14 和 Grove_5V

## 接口

### J1 Grove 端口

J1 IO2=G1、IO1=G2、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J1`；`io2=G1`；`io1=G2`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2C-D，J1 GROVE 右侧 G1/G2/Grove_5V/GND

### J2 Grove 端口

J2 IO2=G4、IO1=G3、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J2`；`io2=G4`；`io1=G3`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2C-D，J2 GROVE 右侧 G4/G3/Grove_5V/GND

### J3 Grove 端口

J3 IO2=G9、IO1=G7、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J3`；`io2=G9`；`io1=G7`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2C-D，J3 GROVE 左侧 G9/G7/Grove_5V/GND

### J5 Grove 端口

J5 IO2=G6、IO1=G5、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J5`；`io2=G6`；`io1=G5`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3C-D，J5 GROVE 右侧 G6/G5/Grove_5V/GND

### J6 Grove 端口

J6 IO2=G10、IO1=G11、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J6`；`io2=G10`；`io1=G11`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3C-D，J6 GROVE 左侧 G10/G11/Grove_5V/GND

### P2/P3 Stamp-S3 排母

P2 Header 9 引出 G1、G3、G5、G7、G9、GND、VIN_5V、G13、G15；P3 Header 6 引出 VCC_3V3、G43、G44、EN、G0、GND。

- 参数与网络：`p2=1 G1, 2 G3, 3 G5, 4 G7, 5 G9, 6 GND, 7 VIN_5V, 8 G13, 9 G15`；`p3=1 VCC_3V3, 2 G43, 3 G44, 4 EN, 5 G0, 6 GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3C-4C，P2 Header 9 与 P3 Header 6 的逐针标注

### P4/P5 Stamp-S3 排母

P4 Header 17 引出 G1-G11、BAT_ADC/G8、VIN_5V、G13、G15 和 GND；P5 Header 11 引出 VCC_3V3、G43、G44、EN、G0、GND，并画有 G46、G42、G41、G40、G39 预留引脚。

- 参数与网络：`p4_key_pins=8 BAT_ADC/G8, 13 VIN_5V, 11 GND`；`p5_active_pins=1 VCC_3V3, 3 G43, 5 G44, 7 EN, 9 G0, 11 GND`；`p5_reserved_signals=G46, G42, G41, G40, G39`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 3C-4D，P4 Header 17 与 P5 Header 11 的逐针标注和预留网络

## 总线

### J4 Grove I2C 端口

J4 SCL=G15、SDA=G13、5V=Grove_5V、GND=GND。

- 参数与网络：`connector=J4`；`scl=G15`；`sda=G13`；`power=Grove_5V`；`ground=GND`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2D，J4 GROVE 明确标注 SCL/SDA，左侧 G15/G13

## GPIO 与控制信号

### 充电状态 LED

U3 CHRG pin1 连接 D2，D2 另一端通过 R4 2.2kΩ 接 VIN_5V，形成充电状态指示。

- 参数与网络：`charger_pin=U3 pin1 CHRG`；`indicator=D2`；`series_resistor=R4 2.2kΩ`；`supply=VIN_5V`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 2A，VIN_5V、R4、D2 与 U3 CHRG

## 复位

### Stamp-S3 EN 复位按键

S1 SW_TS_015 按下时将 EN 网络连接 GND；EN 同时引到 P3 pin4 和 P5 pin7。

- 参数与网络：`switch=S1 SW_TS_015`；`net=EN`；`active_level=low`；`header_pins=P3 pin4, P5 pin7`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 4D，S1/EN/GND 与 P3/P5 EN 引脚

## 模拟电路

### BAT_ADC 电池电压检测

BAT+ 通过 R9 1MΩ 与 R10 1MΩ 等值分压，中点形成 BAT_ADC 并引到 Stamp 接口的 G8。

- 参数与网络：`source=BAT+`；`upper_resistor=R9 1MΩ`；`lower_resistor=R10 1MΩ`；`output=BAT_ADC`；`stamp_gpio=G8`
- 证据：图 d83bf4e9759b / 第 1 页 / 网格 1A-B，R9/R10/BAT_ADC；网格 3C-D P4 pin8 BAT_ADC G8

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3 GroveBreakOut 系统架构 | `battery_inputs=2`；`charger=U3 TP4057`；`three_v_three_converter=U1 SY8089AAAC`；`five_volt_converter=U2 SY7088`；`grove_ports=6`；`reset_switch=S1` |
| 电源 | 双电池输入到 BAT+ | `input_1=P1 -> Q1 -> F1 -> BAT+`；`input_2=BT1 -> Q2 -> BAT+`；`fused_branch=P1`；`common_net=BAT+` |
| 电源 | 电池输入门极控制 | `branch_1=Q1 LP3218DT1G with Q5 2N7002W and R15 100kΩ`；`branch_2=Q2 LP3218DT1G with Q6 2N7002W and R16 100kΩ` |
| 电源 | BAT+ 到 BAT_OUT 开关 | `switch=SW1 SW-PWR1`；`input_pin=1 BAT+`；`output_pin=2 BAT_OUT`；`unused_pin=3` |
| 模拟电路 | BAT_ADC 电池电压检测 | `source=BAT+`；`upper_resistor=R9 1MΩ`；`lower_resistor=R10 1MΩ`；`output=BAT_ADC`；`stamp_gpio=G8` |
| 电源 | TP4057 充电路径 | `charger=U3 TP4057`；`input=VIN_5V via R3 1Ω`；`battery_output=BAT+`；`program_resistor=R7 2.2kΩ`；`standby_pin=NC` |
| GPIO 与控制信号 | 充电状态 LED | `charger_pin=U3 pin1 CHRG`；`indicator=D2`；`series_resistor=R4 2.2kΩ`；`supply=VIN_5V` |
| 电源 | BAT_OUT 到 VCC_3V3 | `converter=U1 SY8089AAAC`；`input=BAT_OUT`；`output=VCC_3V3`；`inductor=L1 2.2uH/2520`；`feedback=R1 68kΩ, R2 15kΩ, C4 22pF` |
| 电源 | BAT_OUT 到 5Vin 升压 | `converter=U2 SY7088`；`input=BAT_OUT`；`output=5Vin`；`inductor=L2 1.5uH/2520`；`enable_pull=R6 100kΩ`；`feedback=R5 51kΩ, R8 15kΩ` |
| 电源 | 5Vin 到 BUS_5V | `source=5Vin`；`diode=D3 DSS34`；`destination=BUS_5V` |
| 电源 | Grove_5V 双电源选择 | `battery_boost_source=BUS_5V -> Q3 -> Grove_5V`；`external_source=VIN_5V -> D4 DSS34 -> Q4 -> Grove_5V`；`selector=SW2`；`bias_resistors=R13 100kΩ, R14 100kΩ` |
| 接口 | J1 Grove 端口 | `connector=J1`；`io2=G1`；`io1=G2`；`power=Grove_5V`；`ground=GND` |
| 接口 | J2 Grove 端口 | `connector=J2`；`io2=G4`；`io1=G3`；`power=Grove_5V`；`ground=GND` |
| 接口 | J3 Grove 端口 | `connector=J3`；`io2=G9`；`io1=G7`；`power=Grove_5V`；`ground=GND` |
| 总线 | J4 Grove I2C 端口 | `connector=J4`；`scl=G15`；`sda=G13`；`power=Grove_5V`；`ground=GND` |
| 接口 | J5 Grove 端口 | `connector=J5`；`io2=G6`；`io1=G5`；`power=Grove_5V`；`ground=GND` |
| 接口 | J6 Grove 端口 | `connector=J6`；`io2=G10`；`io1=G11`；`power=Grove_5V`；`ground=GND` |
| 接口 | P2/P3 Stamp-S3 排母 | `p2=1 G1, 2 G3, 3 G5, 4 G7, 5 G9, 6 GND, 7 VIN_5V, 8 G13, 9 G15`；`p3=1 VCC_3V3, 2 G43, 3 G44, 4 EN, 5 G0, 6 GND` |
| 接口 | P4/P5 Stamp-S3 排母 | `p4_key_pins=8 BAT_ADC/G8, 13 VIN_5V, 11 GND`；`p5_active_pins=1 VCC_3V3, 3 G43, 5 G44, 7 EN, 9 G0, 11 GND`；`p5_reserved_signals=G46, G42, G41, G40, G39` |
| 复位 | Stamp-S3 EN 复位按键 | `switch=S1 SW_TS_015`；`net=EN`；`active_level=low`；`header_pins=P3 pin4, P5 pin7` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d83bf4e9759b68d490a26eca8ac44a3ead532462533e172737176f4d189ef92f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/538/SCH_StampS3GroveBreakOut_V1.0_sch_01.png` |

---

源文档：`zh_CN/accessory/StampS3 GroveBreakOut.md`

源文档 SHA-256：`cf4e94f7bff2dcf40b146f15ad5c4bff69be6fbad3ab83c1f5dd2ba0d91c2938`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
