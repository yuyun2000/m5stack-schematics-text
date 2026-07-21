# Hat Vibrator 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Vibrator |
| SKU | U159 |
| 产品 ID | `hat-vibrator-f6de18d5539b` |
| 源文档 | `zh_CN/hat/HAT-Vibrator.md` |

## 概述

Hat Vibrator 是由 StickIO 接口驱动的离散式振动电机电路，P1 的 G26 信号经 R1 送入 Q1 LN2324DT2AG，形成 BAT 供电电机的低侧开关。R2 将 Q1 控制端下拉到 GND，D1 1N4148WS T4 与 C1 100 nF 跨接在电机两端，分别构成反向电动势钳位和端口抑噪路径。原理图未包含主控、通信总线或电源转换器，电机直接使用 StickIO 的 BAT 网络。

## 检索关键词

`Hat Vibrator`、`U159`、`STICKIO`、`P1`、`G26`、`Motor`、`BAT`、`Vibrator Motor`、`B1`、`3.ED.022.0024`、`Z3OC1T8219731`、`Q1`、`LN2324DT2AG`、`D1`、`1N4148WS T4`、`C1 100nF`、`R1 1KΩ`、`R2 51KΩ`、`low-side switch`、`flyback diode`、`G36/G25`、`M5StickC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | STICKIO | 连接 M5Stick 主机，提供 G26 电机控制、BAT 电源和 GND | 图 e00d5b811a5d / 第 1 页 / B1-C1，P1 STICKIO pins 1-8，pin3 G26 接 Motor、pin6 BAT 接 BAT |
| B1 | 3.ED.022.0024 | BAT 供电的振动电机负载，由 Q1 低侧开关控制 | 图 e00d5b811a5d / 第 1 页 / B2-C3，B1 Vibrator Motor，上方标注 3.ED.022.0024 |
| Q1 | LN2324DT2AG | 振动电机低侧开关，控制端由 G26 经 R1 驱动，源极接 GND | 图 e00d5b811a5d / 第 1 页 / C2-C3，Q1 LN2324DT2AG，栅极接 R1、上端接 B1、下端接 GND |
| D1 | 1N4148WS T4 | 跨接 BAT 与 Q1 开关节点，为电机感性反向电动势提供钳位路径 | 图 e00d5b811a5d / 第 1 页 / B3-C3，D1 1N4148WS T4 跨接 B1 上下两端 |
| C1 | 100nF | 跨接振动电机两端的抑噪电容 | 图 e00d5b811a5d / 第 1 页 / B3-C3，C1 100nF 跨接 BAT 与 Q1 开关节点 |
| R1/R2 | 1KΩ / 51KΩ | Q1 控制端串联限流/阻尼和对地默认下拉网络 | 图 e00d5b811a5d / 第 1 页 / C2，Motor-R1 1KΩ-Q1 控制端，R2 51KΩ 从 Motor 侧节点到 GND |

## 系统结构

### 振动电机驱动架构

P1 G26 经 R1 驱动 Q1，Q1 作为低侧开关控制 BAT 供电的 B1 振动电机；D1 与 C1 均跨接电机两端。

- 参数与网络：`connector=P1 STICKIO`；`control_gpio=G26`；`switch=Q1 LN2324DT2AG`；`motor=B1 Vibrator Motor`；`supply=BAT`；`topology=low-side switch`
- 证据：图 e00d5b811a5d / 第 1 页 / 整页 B1-C3：P1、R1/R2、Q1、B1、D1、C1

## 核心器件

### 原理图电机标识

振动电机位号为 B1，名称为 Vibrator Motor，页面上方标注 3.ED.022.0024。

- 参数与网络：`reference=B1`；`name=Vibrator Motor`；`schematic_marking=3.ED.022.0024`
- 证据：图 e00d5b811a5d / 第 1 页 / B2-B3，B1 Vibrator Motor 与 3.ED.022.0024 标记

## 电源

### 电机 BAT 供电路径

P1 pin6 BAT 直接连接 B1 电机上端；B1 下端连接 Q1，Q1 下端连接 GND。

- 参数与网络：`source=P1 pin6 BAT`；`rail=BAT`；`load=B1`；`return_switch=Q1`；`return=GND`；`converter=none shown`
- 证据：图 e00d5b811a5d / 第 1 页 / B1-C3，P1 BAT 网络到 B1 上端，B1 下端经 Q1 到 GND

## 接口

### StickIO 引脚使用情况

P1 pin1 GND、pin3 G26 和 pin6 BAT 被电路使用；pin2 5VOUT、pin4 G36/G25、pin5 G0、pin7 3V3、pin8 5VIN 标为未连接。

- 参数与网络：`pin1=GND`；`pin2=5VOUT NC`；`pin3=G26 Motor`；`pin4=G36/G25 NC`；`pin5=G0 NC`；`pin6=BAT`；`pin7=3V3 NC`；`pin8=5VIN NC`
- 证据：图 e00d5b811a5d / 第 1 页 / B1-C1，P1 STICKIO pins 1-8 的连线与红色 NC 标记

## GPIO 与控制信号

### G26 电机控制

P1 pin3 的 G26 网络在原理图中命名为 Motor，并经 R1 1 kΩ 串联连接到 Q1 控制端。

- 参数与网络：`gpio=G26`；`connector_pin=P1 pin3`；`net=Motor`；`series_resistor=R1 1KΩ`；`destination=Q1 control terminal`
- 证据：图 e00d5b811a5d / 第 1 页 / C1-C2，P1 pin3 G26/Motor 到 R1 1KΩ，再到 Q1

## 保护电路

### 电机反向电动势钳位

D1 1N4148WS T4 跨接在 BAT 与 Q1 开关节点之间，并与 B1 电机并联。

- 参数与网络：`reference=D1`；`part_number=1N4148WS T4`；`upper_net=BAT`；`lower_net=Q1 drain / motor low terminal`；`parallel_load=B1`
- 证据：图 e00d5b811a5d / 第 1 页 / B3-C3，D1 与 B1 并联的上下连线

### 电机端抑噪电容

C1 100 nF 跨接在 B1 电机的 BAT 端和 Q1 开关端之间，与电机并联。

- 参数与网络：`reference=C1`；`capacitance=100nF`；`upper_net=BAT`；`lower_net=Q1 drain / motor low terminal`；`parallel_load=B1`
- 证据：图 e00d5b811a5d / 第 1 页 / B3-C3，C1 100nF 与 B1 并联

## 关键网络

### Motor 控制网络默认状态

R2 51 kΩ 从 R1 输入侧的 Motor 网络连接到 GND，为 G26/Motor 控制网络提供对地下拉。

- 参数与网络：`net=Motor`；`pulldown=R2 51KΩ`；`reference=GND`；`position=before R1`
- 证据：图 e00d5b811a5d / 第 1 页 / C2，Motor/R1 左端节点经 R2 51KΩ 到 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 振动电机驱动架构 | `connector=P1 STICKIO`；`control_gpio=G26`；`switch=Q1 LN2324DT2AG`；`motor=B1 Vibrator Motor`；`supply=BAT`；`topology=low-side switch` |
| 接口 | StickIO 引脚使用情况 | `pin1=GND`；`pin2=5VOUT NC`；`pin3=G26 Motor`；`pin4=G36/G25 NC`；`pin5=G0 NC`；`pin6=BAT`；`pin7=3V3 NC`；`pin8=5VIN NC` |
| GPIO 与控制信号 | G26 电机控制 | `gpio=G26`；`connector_pin=P1 pin3`；`net=Motor`；`series_resistor=R1 1KΩ`；`destination=Q1 control terminal` |
| 关键网络 | Motor 控制网络默认状态 | `net=Motor`；`pulldown=R2 51KΩ`；`reference=GND`；`position=before R1` |
| 电源 | 电机 BAT 供电路径 | `source=P1 pin6 BAT`；`rail=BAT`；`load=B1`；`return_switch=Q1`；`return=GND`；`converter=none shown` |
| 核心器件 | 原理图电机标识 | `reference=B1`；`name=Vibrator Motor`；`schematic_marking=3.ED.022.0024` |
| 保护电路 | 电机反向电动势钳位 | `reference=D1`；`part_number=1N4148WS T4`；`upper_net=BAT`；`lower_net=Q1 drain / motor low terminal`；`parallel_load=B1` |
| 保护电路 | 电机端抑噪电容 | `reference=C1`；`capacitance=100nF`；`upper_net=BAT`；`lower_net=Q1 drain / motor low terminal`；`parallel_load=B1` |
| 核心器件 | 电机型号对应关系 | `document_model=Z3OC1T8219731`；`schematic_marking=3.ED.022.0024`；`correlation=not established by schematic` |
| 核心器件 | 电机额定与环境参数 | `claimed_rated_voltage=3.0V`；`claimed_rated_current=85mA`；`claimed_speed=12000RPM`；`claimed_operating_voltage=2.3V-4.5V`；`claimed_direction=clockwise`；`claimed_humidity_temperature=0-95% RH, 0-40C`；`claimed_vibration_frequency=10-55Hz` |

## 待确认事项

- `component.motor-model-correlation`：产品正文给出电机型号 Z3OC1T8219731，但原理图只标 3.ED.022.0024，现有原理图证据无法确认两个标识是否对应同一物料。（证据：图 e00d5b811a5d / 第 1 页 / B2-B3，B1 上方仅标 3.ED.022.0024）
- `component.motor-ratings`：产品正文列出 3.0 V、85 mA、12000 RPM、2.3-4.5 V、顺时针旋转及环境/振动频率参数，但这些数值未印在原理图页面中。（证据：图 e00d5b811a5d / 第 1 页 / B2-B3，B1 电机符号未标电压、电流、转速、方向或环境参数）
- `review.motor-model-correlation`：请用 BOM 或电机标签确认 3.ED.022.0024 与 Z3OC1T8219731 的物料对应关系。；原因：原理图标识与产品正文型号不同，页面未提供交叉映射。
- `review.motor-ratings`：请用对应电机 datasheet 或实测复核额定电压、电流、转速、工作范围、转向和环境参数。；原因：这些规格来自产品正文，原理图未直接标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e00d5b811a5d726a92273a771b012921279ab5713f765a80096adbd0918bfece` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/614/Sch_HAT-Vibrator_sch_01.png` |

---

源文档：`zh_CN/hat/HAT-Vibrator.md`

源文档 SHA-256：`b96bc48c9ec2a3c3be1feaf1f033ff0fe69a5313e91a802f76cff881036b3952`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
