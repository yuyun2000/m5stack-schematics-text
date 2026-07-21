# Unit MIC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit MIC |
| SKU | U096 |
| 产品 ID | `unit-mic-20ab34202cb7` |
| 源文档 | `zh_CN/unit/mic.md` |

## 概述

Unit MIC 以 U4 MIC 为声电转换器，信号经偏置与 C3 耦合进入 U2 MAX4466 前置放大器，放大后的 AIn 直接引出到 J1。AIn 同时送入 U1A LM393DR2G，与 R2 10 kΩ 可调阈值比较，输出由 R1 10 kΩ 上拉至 3.3 V 的 Din。U3 HT7533 将 J1 VCC 转为 3.3 V，供麦克风偏置、放大器和比较器使用。

## 检索关键词

`Unit MIC`、`U096`、`MAX4466`、`LM393DR2G`、`LM393`、`HT7533`、`MIC`、`electret microphone`、`AIn`、`Din`、`analog output`、`digital output`、`R2 RPot 10K`、`threshold`、`R1 10K pull-up`、`R3 1K`、`R5 1K`、`R4 1M`、`R6 1M`、`R7 100K`、`C7 100pF`、`R8 1K`、`C8 1uF`、`C3 10nF`、`AD_Socket_4P`、`VCC`、`3.3V`、`5V`、`52dB`、`40dB SNR`、`omnidirectional`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | MIC | 模拟声音输入麦克风 | 图 d77f8f978e51 / 第 1 页 / 页 1 左侧 U4 标注 MIC，一端连接偏置/耦合网络，另一端接 GND |
| U2 | MAX4466 | 麦克风低噪声前置放大器 | 图 d77f8f978e51 / 第 1 页 / 页 1 左中 U2 器件框下方标注 max4466，OUT 连接 AIn |
| U1A | LM393DR2G | AIn 与可调阈值比较并生成 Din | 图 d77f8f978e51 / 第 1 页 / 页 1 上中 U1A 标注 LM393DR2G，输入为 R2 阈值与 AIn，输出为 Din |
| U3 | HT7533 | VCC 至 3.3 V 线性稳压器 | 图 d77f8f978e51 / 第 1 页 / 页 1 下中 U3 标注 HT7533，VIN 接 VCC、VOUT 接 +3.3V |
| R2 | RPot 10K | 数字声音检测比较阈值调节电位器 | 图 d77f8f978e51 / 第 1 页 / 页 1 上中 R2 标注 RPot 10K，跨接 +3.3V/GND，滑动端连接 U1A pin 2 |
| J1 | AD_Socket_4P | 模拟输出、数字输出与电源接口 | 图 d77f8f978e51 / 第 1 页 / 页 1 右上 J1 标注 AD_Socket_4P，针脚为 Ain、Din、VCC、GND |

## 系统结构

### Unit MIC 信号链

U4 MIC 经偏置和 C3 交流耦合进入 U2 MAX4466，U2 输出 AIn；AIn 一路引出 J1，一路进入 U1A LM393DR2G 生成 Din。

- 参数与网络：`sensor=U4 MIC`；`preamplifier=U2 MAX4466`；`analog_output=AIn`；`comparator=U1A LM393DR2G`；`digital_output=Din`；`connector=J1`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 从左侧 U4 经 U2/AIn/U1A 到右侧 J1 的完整模拟与数字路径

## 电源

### U1A 供电

LM393DR2G 的供电 pin 8 连接 +3.3V，GND pin 4 连接 GND。

- 参数与网络：`reference=U1A`；`part_number=LM393DR2G`；`supply=pin 8/+3.3V`；`ground=pin 4/GND`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 U1A 上下供电引脚 8/4 与 +3.3V/GND

### U3 HT7533

U3 HT7533 的 VIN pin 2 接 VCC，VOUT pin 3 输出 +3.3V，GND pin 1 接地。

- 参数与网络：`reference=U3`；`part_number=HT7533`；`input=VIN/pin 2/VCC`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 下中 U3 引脚号与 VCC/+3.3V/GND 网络

### U3 输入输出电容

U3 输入侧 C6 10 uF 连接在 VCC 与 GND 之间；输出侧 C4 100 nF 与 C5 10 uF 并联在 +3.3V 与 GND 之间。

- 参数与网络：`input_capacitor=C6 10uF`；`output_capacitors=C4 100nF,C5 10uF`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 U3 左侧 C4/C5 与右侧 C6

### J1 VCC 去耦

C1 100 nF 连接在 J1 VCC pin 3 与 GND pin 4 所在网络之间。

- 参数与网络：`capacitor=C1 100nF`；`rail=VCC`；`return=GND`；`connector=J1`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 右上 J1 旁 C1 100nF 与 VCC/GND

## 接口

### J1 模拟/数字接口

J1 的 1 至 4 脚依次连接 Ain、Din、VCC、GND。

- 参数与网络：`reference=J1`；`pinout=1:Ain,2:Din,3:VCC,4:GND`；`Ain_direction=analog output from unit`；`Din_direction=digital output from unit`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 右上 J1 脚号和 Ain/Din/VCC/GND 标签

## GPIO 与控制信号

### Din 数字输出

U1A 输出 pin 1 连接 Din；R1 10 kΩ 将 Din 上拉至 +3.3V，Din 引出到 J1 pin 2。

- 参数与网络：`comparator=U1A LM393DR2G`；`output_pin=1`；`network=Din`；`pullup=R1 10k to +3.3V`；`connector=J1 pin 2`；`logic_rail=+3.3V`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 上中 U1A output pin 1、R1 10K、Din 与右侧 J1 pin 2

## 保护电路

### 接口与传感器保护

本页未显示 TVS/ESD、保险丝、反接保护、输入钳位或过压保护器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`input_clamp_visible=false`；`overvoltage_protection_visible=false`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 全图仅含麦克风、放大、比较、稳压和阻容网络

## 音频

### U4 麦克风偏置

U4 MIC 正端通过 R5 1 kΩ 与 R3 1 kΩ 串联偏置到 +3.3V；R3/R5 中点由 C2 100 nF 旁路至 GND，U4 负端接 GND。

- 参数与网络：`microphone=U4 MIC`；`bias_resistors=R3 1k,R5 1k`；`bias_rail=+3.3V`；`bypass=C2 100nF from R3/R5 midpoint to GND`；`negative_terminal=GND`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 左侧 U4、R3/R5、C2 与 +3.3V/GND 网络

## 模拟电路

### U4 至 U2 输入

U4 麦克风信号经 C3 10 nF 交流耦合到 U2 IN+ 引脚 1；该节点由 R4 1 MΩ 接 +3.3V、R6 1 MΩ 接 GND 建立中点偏置。

- 参数与网络：`coupling_capacitor=C3 10nF`；`destination=U2 IN+/pin 1`；`upper_bias=R4 1M to +3.3V`；`lower_bias=R6 1M to GND`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 左中 C3、R4/R6 与 U2 IN+ pin 1

### U2 MAX4466 连接

U2 VCC 引脚 5 接 +3.3V、GND 引脚 2 接地、OUT 引脚 4 输出 AIn；IN- 引脚 3 连接反馈与增益网络。

- 参数与网络：`reference=U2`；`part_number=MAX4466`；`supply=VCC/pin 5/+3.3V`；`ground=GND/pin 2`；`non_inverting_input=IN+/pin 1`；`inverting_input=IN-/pin 3`；`output=OUT/pin 4/AIn`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 U2 MAX4466 全部五个引脚及网络

### U2 反馈与低频网络

R7 100 kΩ 与 C7 100 pF 并联在 U2 OUT/AIn 与 IN- 之间；IN- 再经 R8 1 kΩ、C8 1 uF 串联到 GND。

- 参数与网络：`feedback_resistor=R7 100k`；`feedback_capacitor=C7 100pF`；`ground_leg=R8 1k in series with C8 1uF to GND`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 U2 下方 R7/C7 反馈与 R8/C8 对地支路

### AIn 模拟输出

AIn 由 U2 OUT 引脚 4 直接驱动，连接 J1 pin 1 和 U1A 非反相输入 pin 3；C9 10 uF 从 AIn 连接到 GND。

- 参数与网络：`source=U2 OUT/pin 4`；`connector=J1 pin 1`；`comparator_input=U1A pin 3`；`shunt_capacitor=C9 10uF to GND`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 U2 OUT/AIn 到 U1A pin 3、C9 与 J1 pin 1 的网络

### R2 比较阈值

R2 为 10 kΩ 电位器，跨接 +3.3V 与 GND，滑动端连接 U1A 反相输入 pin 2，用于调节与 AIn 比较的阈值。

- 参数与网络：`reference=R2`；`part_number=RPot 10K`；`endpoints=+3.3V,GND`；`wiper_destination=U1A pin 2`；`compared_signal=AIn at U1A pin 3`
- 证据：图 d77f8f978e51 / 第 1 页 / 页 1 上中 R2 RPot 10K 与 U1A pin 2 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit MIC 信号链 | `sensor=U4 MIC`；`preamplifier=U2 MAX4466`；`analog_output=AIn`；`comparator=U1A LM393DR2G`；`digital_output=Din`；`connector=J1` |
| 接口 | J1 模拟/数字接口 | `reference=J1`；`pinout=1:Ain,2:Din,3:VCC,4:GND`；`Ain_direction=analog output from unit`；`Din_direction=digital output from unit` |
| 音频 | U4 麦克风偏置 | `microphone=U4 MIC`；`bias_resistors=R3 1k,R5 1k`；`bias_rail=+3.3V`；`bypass=C2 100nF from R3/R5 midpoint to GND`；`negative_terminal=GND` |
| 模拟电路 | U4 至 U2 输入 | `coupling_capacitor=C3 10nF`；`destination=U2 IN+/pin 1`；`upper_bias=R4 1M to +3.3V`；`lower_bias=R6 1M to GND` |
| 模拟电路 | U2 MAX4466 连接 | `reference=U2`；`part_number=MAX4466`；`supply=VCC/pin 5/+3.3V`；`ground=GND/pin 2`；`non_inverting_input=IN+/pin 1`；`inverting_input=IN-/pin 3`；`output=OUT/pin 4/AIn` |
| 模拟电路 | U2 反馈与低频网络 | `feedback_resistor=R7 100k`；`feedback_capacitor=C7 100pF`；`ground_leg=R8 1k in series with C8 1uF to GND` |
| 模拟电路 | AIn 模拟输出 | `source=U2 OUT/pin 4`；`connector=J1 pin 1`；`comparator_input=U1A pin 3`；`shunt_capacitor=C9 10uF to GND` |
| 模拟电路 | R2 比较阈值 | `reference=R2`；`part_number=RPot 10K`；`endpoints=+3.3V,GND`；`wiper_destination=U1A pin 2`；`compared_signal=AIn at U1A pin 3` |
| GPIO 与控制信号 | Din 数字输出 | `comparator=U1A LM393DR2G`；`output_pin=1`；`network=Din`；`pullup=R1 10k to +3.3V`；`connector=J1 pin 2`；`logic_rail=+3.3V` |
| 电源 | U1A 供电 | `reference=U1A`；`part_number=LM393DR2G`；`supply=pin 8/+3.3V`；`ground=pin 4/GND` |
| 电源 | U3 HT7533 | `reference=U3`；`part_number=HT7533`；`input=VIN/pin 2/VCC`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1` |
| 电源 | U3 输入输出电容 | `input_capacitor=C6 10uF`；`output_capacitors=C4 100nF,C5 10uF` |
| 电源 | J1 VCC 去耦 | `capacitor=C1 100nF`；`rail=VCC`；`return=GND`；`connector=J1` |
| 保护电路 | 接口与传感器保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`input_clamp_visible=false`；`overvoltage_protection_visible=false` |
| 音频 | 麦克风声学参数 | `documented_directivity=omnidirectional`；`documented_sensitivity_db=52`；`documented_snr_db=40`；`schematic_microphone_part=MIC`；`schematic_acoustic_parameters=null` |
| 电源 | J1 VCC 输入电压 | `documented_input_voltage_v=5`；`schematic_input_rail=VCC`；`schematic_voltage=null` |

## 待确认事项

- `audio.acoustic_parameters`：产品正文描述全指向、52 dB 灵敏度与 40 dB 信噪比，但原理图只标注通用 MIC，没有声学型号或性能参数。（证据：图 d77f8f978e51 / 第 1 页 / 页 1 U4 仅标注 MIC，未打印灵敏度、信噪比或指向性）
- `power.input_voltage`：产品正文标注输入电压 5 V，但本页原理图只将 J1 pin 3 与 U3 VIN 网络标为 VCC，没有打印 5V 数值。（证据：图 d77f8f978e51 / 第 1 页 / 页 1 J1 VCC pin 3 至 U3 VIN pin 2 的电源网络仅标注 VCC）
- `review.acoustic_parameters`：当前 U4 麦克风的完整料号、灵敏度定义、40 dB 信噪比和全指向规格是什么？；原因：原理图使用通用 MIC 标注，没有声学料号与测试条件。
- `review.input_voltage`：J1 VCC 的额定输入范围是否为固定 5 V，允许的容差和瞬态范围是什么？；原因：原理图使用 VCC 网络名，没有标注输入电压数值或范围。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d77f8f978e51d1eb65c9aafb1be66ad44c1fb45d151d04687fac52f16ceb9df1` | `https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_sch_01.webp` |

---

源文档：`zh_CN/unit/mic.md`

源文档 SHA-256：`3a04e3304ead443325eb9dcd62a970cedc159989e7937fea765aeac4c22b2a47`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
