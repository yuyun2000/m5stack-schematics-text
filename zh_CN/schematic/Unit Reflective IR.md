# Unit Reflective IR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Reflective IR |
| SKU | U175 |
| 产品 ID | `unit-reflective-ir-b9aa857e0a62` |
| 源文档 | `zh_CN/unit/Unit-Reflective IR.md` |

## 概述

Unit Reflective IR 由常亮红外发射支路、红外接收模拟节点 AO、LM393DR2G 比较器数字输出 DO 和阈值调节电位器构成。J1 Grove 将 5V、GND、AO 和 DO 引出，板上 U2 HX6306P332MR 将 5V 稳压为 3V3，供传感与比较器电路使用。AO 由红外接收器、10K 上拉和 100nF 滤波网络形成，DO 由 10K 上拉并连接红色状态 LED；本页未包含 MCU、通信总线、存储、时钟、电池、充电、射频、音频或调试电路。

## 检索关键词

`Unit Reflective IR`、`U175`、`Reflective IR Unit`、`HX6306P332MR`、`LM393DR2G`、`GROVE`、`J1`、`AO`、`DO`、`IO2`、`IO1`、`5V`、`3V3`、`R4`、`RES-ADJ-SMD_3313J-1U1B`、`D3 IR Receiver`、`D4 IR LED`、`D1 RED 0603`、`R3 10K`、`R1 10K`、`R5 100R`、`R2 470R`、`C3 100nF`、`analog output`、`digital output`、`infrared reflection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE | 四针外部接口，引出 AO、DO、5V 和 GND | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B2-C2，J1 GROVE，IO2/AO、IO1/DO、5V、GND 四个引脚 |
| U2 | HX6306P332MR | 将 5V 转换为 3V3 的三引脚稳压器 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B3，U2 HX6306P332MR，VIN pin3、VOUT pin2、GND pin1 |
| 位号未标注 | LM393DR2G | 比较 AO 与 R4 滑臂电压并输出 DO；图中使用 pin5、pin6、pin7、pin8 和 pin4 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，LM393DR2G 比较器符号；图中未显示 U 类位号 |
| R4 | RES-ADJ-SMD_3313J-1U1B | 比较器阈值调节电位器，上端接 3V3、下端接 AO、滑臂接比较器 pin6 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，R4 RES-ADJ-SMD_3313J-1U1B 与 LM393DR2G pin6 |
| D3 | IR Receiver | 红外接收器，连接 AO 与 GND，形成反射光模拟检测节点 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C2-C3，D3 IR Receiver，上端 AO、下端 GND |
| D4 | IR LED | 经 R5 从 3V3 固定供电的红外发射 LED | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C2，3V3-R5 100R-D4 IR LED-GND 串联支路 |
| D1 | RED 0603 | DO 状态指示 LED，经 R2 接至 3V3 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3-C4，3V3-R2 470R-D1 RED 0603-DO 支路 |
| R1,R3 | 10K | 分别把 DO 和 AO 上拉到 3V3 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，R1 10K 位于 3V3 与 DO 之间，R3 10K 位于 3V3 与 AO 之间 |
| C1,C2,C3,C4,C5 | 100pF / 10uF / 100nF / 100nF / 10uF | 3V3 旁路、U2 输入输出去耦以及 AO 滤波 | 图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B3-C3，C1 100pF、C2 10uF、C3 100nF、C4 100nF、C5 10uF |

## 系统结构

### Unit Reflective IR 系统架构

J1 提供 5V 输入并引出 AO/DO；U2 生成 3V3，D4 构成常亮红外发射支路，D3/R3/C3 形成 AO 接收节点，LM393DR2G 与 R4 形成阈值比较并输出 DO，D1 指示 DO 节点状态。

- 参数与网络：`connector=J1 GROVE`；`power=5V -> U2 HX6306P332MR -> 3V3`；`emitter=D4 IR LED`；`receiver=D3 IR Receiver`；`analog_output=AO`；`comparator=LM393DR2G`；`digital_output=DO`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B2-C4，完整功能电路

### 本页未包含的子系统

该原理图页未显示 MCU、协处理器、存储器、外部晶振、复位/BOOT、调试、I2C/SPI/UART/CAN/RS-485/USB/SDIO/MIPI/I2S 总线、电池、充电、射频或音频电路。

- 参数与网络：`mcu=null`；`coprocessor=null`；`storage=null`；`clock=null`；`reset_boot=null`；`debug=null`；`digital_bus=null`；`battery_charger=null`；`rf=null`；`audio=null`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页完整原理图，仅含 J1、U2、红外收发、比较器、LED 与无源网络

## 核心器件

### DO 红色指示 LED

3V3 经 R2 470R 和 D1 RED 0603 串联到 DO，构成数字输出状态指示支路。

- 参数与网络：`path=3V3 -> R2 -> D1 -> DO`；`resistor=R2 470R`；`led=D1 RED 0603`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3-C4，R2 470R 与 D1 RED 0603

## 电源

### 5V 到 3V3 稳压路径

U2 HX6306P332MR 的 VIN pin3 接 5V、VOUT pin2 输出 3V3、GND pin1 接地；输入侧 C2 10uF 与 C4 100nF 对地，输出侧 C5 10uF 对地。

- 参数与网络：`reference=U2`；`part_number=HX6306P332MR`；`input=pin3 VIN=5V`；`output=pin2 VOUT=3V3`；`ground=pin1 GND`；`input_caps=C2 10uF,C4 100nF`；`output_cap=C5 10uF`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B3，U2、C2、C4、C5 和 5V/3V3 网络

### 比较器供电与旁路

LM393DR2G pin8 接 3V3、pin4 接 GND；C1 100pF 跨接 3V3 与 GND。

- 参数与网络：`positive_supply=pin8=3V3`；`ground=pin4=GND`；`bypass=C1 100pF between 3V3 and GND`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，LM393DR2G pin8/pin4 与 C1 100pF

## 接口

### J1 Grove 引脚映射

J1 的 IO2 接 AO，IO1 接 DO，5V 接 5V 电源网，GND 接地。AO/DO 相对本单元分别为输出到外部主机的模拟与数字信号，5V/GND 为供电输入和回路。

- 参数与网络：`reference=J1`；`pin_io2=AO, output`；`pin_io1=DO, output`；`pin_5v=5V, power input`；`pin_gnd=GND`；`signal_level_supply=AO/DO circuitry powered by 3V3`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B2-C2，J1 GROVE 引脚文字和同名网络

## GPIO 与控制信号

### DO 数字输出网络

LM393DR2G 输出 pin7 连接 DO，R1 10K 将 DO 上拉至 3V3，DO 同时连接 J1 IO1 与 D1 状态指示支路。

- 参数与网络：`net=DO`；`source=LM393DR2G pin7`；`pullup=R1 10K to 3V3`；`connector=J1 IO1`；`indicator=D1 branch`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3-C4，比较器 pin7、R1、DO、J1 IO1 和 D1

## 保护电路

### 外部接口保护

本页 J1 的 5V、AO、DO 与 GND 路径未显示保险丝、TVS、专用 ESD 阵列或反接保护器件。

- 参数与网络：`connector=J1`；`fuse=null`；`tvs=null`；`esd_array=null`；`reverse_polarity=null`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页完整 J1 至 5V/AO/DO 电路路径，无专用保护符号或位号

## 关键网络

### 关键网络 AO 与 DO

AO 是 D3/R3/C3 的模拟检测节点并进入比较器 pin5；DO 是比较器 pin7 的上拉输出节点。两者分别由 J1 IO2 和 IO1 引出。

- 参数与网络：`AO=D3,R3,C3,LM393 pin5,J1 IO2`；`DO=LM393 pin7,R1,D1,J1 IO1`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 B2-C4，AO/DO 同名网络全路径

## 传感器

### 红外发射支路

3V3 经 R5 100R 串联 D4 IR LED 后接 GND；该页未显示 GPIO、晶体管或使能器件控制 D4。

- 参数与网络：`path=3V3 -> R5 -> D4 -> GND`；`resistor=R5 100R`；`emitter=D4 IR LED`；`enable=null`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C2，R5/D4 独立串联支路

## 模拟电路

### AO 红外接收模拟节点

R3 10K 将 AO 上拉到 3V3，D3 IR Receiver 从 AO 接至 GND，C3 100nF 从 AO 接至 GND；AO 同时连接 J1 IO2 和比较器非反相输入 pin5。

- 参数与网络：`net=AO`；`pullup=R3 10K to 3V3`；`receiver=D3 IR Receiver to GND`；`filter=C3 100nF to GND`；`connector=J1 IO2`；`comparator_input=LM393DR2G pin5 (+)`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C2-C3，AO、R3、D3、C3、J1 IO2 与比较器 pin5

### LM393DR2G 比较器输入

比较器非反相输入 pin5 接 AO，反相输入 pin6 接 R4 滑臂；R4 上端接 3V3、下端接 AO，图中没有打印 R4 阻值。

- 参数与网络：`part_number=LM393DR2G`；`non_inverting=pin5=AO`；`inverting=pin6=R4 wiper`；`pot_top=3V3`；`pot_bottom=AO`；`pot_value=null`
- 证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，R4 上下端、滑臂及 LM393DR2G pin5/pin6 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Reflective IR 系统架构 | `connector=J1 GROVE`；`power=5V -> U2 HX6306P332MR -> 3V3`；`emitter=D4 IR LED`；`receiver=D3 IR Receiver`；`analog_output=AO`；`comparator=LM393DR2G`；`digital_output=DO` |
| 接口 | J1 Grove 引脚映射 | `reference=J1`；`pin_io2=AO, output`；`pin_io1=DO, output`；`pin_5v=5V, power input`；`pin_gnd=GND`；`signal_level_supply=AO/DO circuitry powered by 3V3` |
| 电源 | 5V 到 3V3 稳压路径 | `reference=U2`；`part_number=HX6306P332MR`；`input=pin3 VIN=5V`；`output=pin2 VOUT=3V3`；`ground=pin1 GND`；`input_caps=C2 10uF,C4 100nF`；`output_cap=C5 10uF` |
| 传感器 | 红外发射支路 | `path=3V3 -> R5 -> D4 -> GND`；`resistor=R5 100R`；`emitter=D4 IR LED`；`enable=null` |
| 模拟电路 | AO 红外接收模拟节点 | `net=AO`；`pullup=R3 10K to 3V3`；`receiver=D3 IR Receiver to GND`；`filter=C3 100nF to GND`；`connector=J1 IO2`；`comparator_input=LM393DR2G pin5 (+)` |
| 模拟电路 | LM393DR2G 比较器输入 | `part_number=LM393DR2G`；`non_inverting=pin5=AO`；`inverting=pin6=R4 wiper`；`pot_top=3V3`；`pot_bottom=AO`；`pot_value=null` |
| 电源 | 比较器供电与旁路 | `positive_supply=pin8=3V3`；`ground=pin4=GND`；`bypass=C1 100pF between 3V3 and GND` |
| GPIO 与控制信号 | DO 数字输出网络 | `net=DO`；`source=LM393DR2G pin7`；`pullup=R1 10K to 3V3`；`connector=J1 IO1`；`indicator=D1 branch` |
| 核心器件 | DO 红色指示 LED | `path=3V3 -> R2 -> D1 -> DO`；`resistor=R2 470R`；`led=D1 RED 0603` |
| 关键网络 | 关键网络 AO 与 DO | `AO=D3,R3,C3,LM393 pin5,J1 IO2`；`DO=LM393 pin7,R1,D1,J1 IO1` |
| 保护电路 | 外部接口保护 | `connector=J1`；`fuse=null`；`tvs=null`；`esd_array=null`；`reverse_polarity=null` |
| 系统结构 | 本页未包含的子系统 | `mcu=null`；`coprocessor=null`；`storage=null`；`clock=null`；`reset_boot=null`；`debug=null`；`digital_bus=null`；`battery_charger=null`；`rf=null`；`audio=null` |
| 模拟电路 | 正文阈值比较电压 | `documented_default=1.65V`；`documented_range=0.3V-2.15V`；`potentiometer=R4`；`schematic_voltage_annotation=null` |
| 传感器 | 正文检测距离 | `targets=black,white,color,glossy`；`thresholds=1.65V,2.15V`；`documented_distances=black 0/6.5cm; white 13/28cm; color 14/25.5cm; glossy 31/43cm`；`test_conditions=null` |
| 模拟电路 | 正文 AO ADC 码值范围 | `documented_adc_codes=0-4096`；`documented_host=ESP32@12bit`；`net=AO`；`voltage_range=null`；`adc_reference=null` |
| GPIO 与控制信号 | 正文 DO TTL 电平与翻转行为 | `documented_level=TTL`；`net=DO`；`pullup=R1 10K to 3V3`；`vih_vil=null`；`voh_vol=null`；`active_polarity=null` |
| 核心器件 | R4 实装阻值 | `reference=R4`；`schematic_marking=RES-ADJ-SMD_3313J-1U1B`；`documented_value=10K`；`schematic_value=null` |
| 其他事实 | 正文工作温度 | `documented_working_temperature=0-40C`；`schematic_temperature_rating=null` |
| 传感器 | 红外收发器光学性能 | `emitter=D4 IR LED`；`receiver=D3 IR Receiver`；`wavelength=null`；`radiant_power=null`；`sensitivity=null`；`field_of_view=null`；`ambient_light_condition=null` |

## 待确认事项

- `analog.documented-threshold-range`：产品正文称出厂默认阈值为 1.65V、有效调节范围为 0.3V 至 2.15V；原理图只显示 R4 与比较器输入连接，没有标注这些电压、测试点或容差。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，R4 与 LM393DR2G pin6，图中无阈值电压文字）
- `sensor.documented-detection-distance`：产品正文列出黑色、白色、彩色和光泽目标在 1.65V/2.15V 阈值下的检测距离；原理图没有目标材质、距离、测试几何、环境光或重复性数据。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页 D3/D4 红外收发电路，无距离或测试条件标注）
- `analog.documented-adc-code`：正文将模拟输出写为 0-4096（ESP32@12bit），该值是外部主机 ADC 码值描述；原理图仅确认 AO 连接，未标 AO 最小/最大电压、源阻抗、ADC 参考电压或码值边界。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页 AO/R3/D3/C3/J1 IO2，图中无 ADC 或码值标注）
- `gpio.documented-do-level-behavior`：正文称 DO 为 TTL 数字输出并描述红灯与阈值状态；原理图确认 DO 被 R1 上拉至 3V3，但未标 VIH/VIL、VOH/VOL、输出电流、准确翻转条件或有效极性。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页 LM393DR2G pin7、R1、DO 与 D1，图中无逻辑门限或极性注释）
- `component.r4-populated-value`：正文称板载可调电位器为 10K；原理图将 R4 标为 RES-ADJ-SMD_3313J-1U1B，但未打印阻值，因此无法仅由本页确认实装为 10K。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C3，R4 标注只有 RES-ADJ-SMD_3313J-1U1B，无阻值文字）
- `other.documented-temperature`：正文给出工作温度 0 至 40°C；原理图没有温度等级、器件温度范围或整机环境条件。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页完整原理图标题栏与电路区，无温度规格）
- `sensor.ir-optical-performance`：原理图只将 D4 标为 IR LED、D3 标为 IR Receiver，未标发射波长、辐射功率、接收光谱响应、灵敏度、视场角或环境光工作条件。（证据：图 b4c5bf5e6d13 / 第 1 页 / 第 1 页网格 C2-C3，D4 IR LED 与 D3 IR Receiver，无光学参数）
- `review.threshold-range`：请通过测试记录或量产规范确认默认 1.65V、0.3V 至 2.15V 有效阈值范围及测量点。；原因：这些电压只见于正文，原理图没有标注。
- `review.detection-distance`：请确认各目标材质检测距离的测试几何、环境光、样品批次、阈值容差和重复性。；原因：电路连接不能证明整机检测距离。
- `review.ao-adc-range`：请确认 AO 的电气电压范围、允许负载以及 0-4096 码值采用的 ESP32 ADC 参考和换算方式。；原因：0-4096 是外部 ADC 码值，不是原理图给出的 AO 电气范围。
- `review.do-logic`：请用器件规格或实测确认 DO 的 VIH/VIL、VOH/VOL、有效极性、阈值翻转方向和 LED 对应状态。；原因：本页只有 3V3 上拉与连接拓扑，没有 TTL 门限和行为说明。
- `review.r4-value`：请通过 BOM、物料编码或实测确认 R4 的实装总阻值是否为 10K。；原因：原理图只显示电位器封装/型号字段，未打印阻值。
- `review.temperature`：请确认 0 至 40°C 是工作、性能保证还是建议使用温度范围，并给出验证条件。；原因：原理图未给器件或整机温度等级。
- `review.ir-optical-performance`：请通过 D3/D4 料号、datasheet 或光学测试确认波长、发射功率、接收灵敏度、视场角与环境光限制。；原因：原理图仅使用通用 IR LED/IR Receiver 标识。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b4c5bf5e6d13ec305fb244d91320392d4513bd5dc1c1ed80bcc5f68c70e37d9b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/628/SCH_UNIT_Reflective_IR_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-Reflective IR.md`

源文档 SHA-256：`4854d99987ae447b9b6702735b80edb15c6b031ea75646456ff6a6a35fe082ed`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
