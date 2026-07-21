# Unit Buzzer 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Buzzer |
| SKU | U132 |
| 产品 ID | `unit-buzzer-e992324e6a5f` |
| 源文档 | `zh_CN/unit/buzzer.md` |

## 概述

Unit Buzzer 是一块无板载主控的离散蜂鸣器驱动单元，J1 HY-2.0_IO 引入 BEEP、+5V 和 GND。U1 HT7533 将 +5V 转为 +3.3V，+3.3V 经 R3 10Ω供给 LS1 Buzzer 高端。BEEP 经 R1 1KΩ驱动 Q1 SS8050 Y1 低侧开关，R2 4.7KΩ提供下拉，D1 1N4007WS 跨接蜂鸣器两端用于感性回路钳位。

## 检索关键词

`Unit Buzzer`、`U132`、`LS1`、`Buzzer`、`U1`、`HT7533`、`Q1`、`SS8050 Y1`、`D1`、`1N4007WS`、`J1`、`HY-2.0_IO`、`BEEP`、`+5V`、`+3.3V`、`GND`、`R1`、`1KΩ(1001) ±1%`、`R2`、`4.7KΩ(4701) ±1%`、`R3`、`10Ω`、`C1 10uF`、`C2 10uF`、`C3 100nF`、`low-side buzzer drive`、`flyback diode`、`PWM buzzer`、`Grove Port B`、`4KHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LS1 | Buzzer | 发声器件，高端经 R3 接 +3.3V，低端连接 Q1 集电极。 | 图 e97555620a70 / 第 1 页 / 页面右上 LS1 Buzzer，连接 R3/+3.3V 与 Q1 集电极 |
| U1 | HT7533 | +5V 到 +3.3V 的三端 LDO，为蜂鸣器驱动侧供电。 | 图 e97555620a70 / 第 1 页 / 页面左上 U1 HT7533，VIN 2/VOUT 3/GND 1 与 +5V/+3.3V |
| Q1 | SS8050 Y1 | 蜂鸣器低侧驱动晶体管，基极由 BEEP 经 R1 驱动，发射极接 GND。 | 图 e97555620a70 / 第 1 页 / 页面右下 Q1 SS8050 Y1，R1 基极、LS1 集电极、GND 发射极 |
| D1 | 1N4007WS | 跨接 LS1 高低端的续流/钳位二极管。 | 图 e97555620a70 / 第 1 页 / 页面右上 D1 1N4007WS，跨接 R3/LS1 高端节点与 Q1/LS1 低端节点 |
| J1 | HY-2.0_IO | 四针 Grove IO/供电接口，2 脚接 BEEP、3 脚接 +5V、4 脚接 GND。 | 图 e97555620a70 / 第 1 页 / 页面左下 J1 HY-2.0_IO，1-4 脚 I/O/VCC/GND 与 BEEP/+5V/GND |
| R1 | 1KΩ(1001) ±1% | BEEP 到 Q1 基极的串联限流电阻。 | 图 e97555620a70 / 第 1 页 / 页面右下 BEEP-R1-Q1 基极，R1 标注 1KΩ(1001) ±1% |
| R2 | 4.7KΩ(4701) ±1% | BEEP 输入到 GND 的下拉电阻。 | 图 e97555620a70 / 第 1 页 / 页面右下 BEEP-R2-GND，R2 标注 4.7KΩ(4701) ±1% |
| R3 | 10Ω | +3.3V 到 LS1 高端的串联电阻。 | 图 e97555620a70 / 第 1 页 / 页面右上 +3.3V-R3-LS1 高端，R3 标注 10Ω |
| C1,C2,C3 | 10uF / 10uF / 100nF | U1 +5V 输入与 +3.3V 输出的滤波/去耦电容。 | 图 e97555620a70 / 第 1 页 / 页面左上 C1 10uF 位于 +5V，C2 10uF 与 C3 100nF 位于 +3.3V，均接 GND |

## 系统结构

### 整板架构

整板由 J1、U1、Q1、LS1、D1 和阻容构成，以外部 BEEP 信号控制蜂鸣器；本页未显示 MCU、存储器、晶振、复位、调试或数字通信 IC。

- 参数与网络：`input_connector=J1 HY-2.0_IO`；`regulator=U1 HT7533`；`driver=Q1 SS8050 Y1`；`sounder=LS1 Buzzer`；`flyback=D1 1N4007WS`；`controller=原理图未显示`；`storage=原理图未显示`
- 证据：图 e97555620a70 / 第 1 页 / 第 1 页全图，全部可见功能器件与 BEEP/+5V/+3.3V/GND 网络

## 电源

### U1 5V 到 3.3V LDO

U1 HT7533 的 VIN（2 脚）接 +5V，VOUT（3 脚）输出 +3.3V，GND（1 脚）接地；C1 10uF 位于输入侧，C2 10uF 与 C3 100nF 位于输出侧。

- 参数与网络：`regulator=U1 HT7533`；`input_pin=2`；`input_rail=+5V`；`output_pin=3`；`output_rail=+3.3V`；`ground_pin=1`；`input_capacitor=C1 10uF`；`output_capacitors=C2 10uF,C3 100nF`
- 证据：图 e97555620a70 / 第 1 页 / 页面左上 +5V-C1-U1 HT7533-C2/C3-+3.3V 电源链

### LS1 供电路径

+3.3V 经 R3（10Ω）串联连接 LS1 高端，LS1 低端连接 Q1 集电极，Q1 发射极接 GND。

- 参数与网络：`rail=+3.3V`；`series_resistor=R3 10Ω`；`load=LS1 Buzzer`；`low_side_switch=Q1 SS8050 Y1`；`return=GND`
- 证据：图 e97555620a70 / 第 1 页 / 页面右侧 +3.3V-R3-LS1-Q1-GND 串联路径

### 电源滤波

C1 10uF 跨接 +5V 与 GND，C2 10uF 和 C3 100nF 均跨接 +3.3V 与 GND。

- 参数与网络：`input_bulk=C1 10uF +5V-to-GND`；`output_bulk=C2 10uF +3.3V-to-GND`；`output_bypass=C3 100nF +3.3V-to-GND`
- 证据：图 e97555620a70 / 第 1 页 / 页面左上 C1/C2/C3 与 +5V/+3.3V/GND

## 接口

### J1 HY-2.0_IO

J1.1-J1.4 在符号内依次标注 I、O、VCC、GND；其中 J1.2 连接 BEEP，J1.3 连接 +5V，J1.4 连接 GND，J1.1 没有可见外部网络。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IO`；`pin_1=I/no visible net`；`pin_2=O/BEEP`；`pin_3=VCC/+5V`；`pin_4=GND`
- 证据：图 e97555620a70 / 第 1 页 / 页面左下 J1 1-4 脚与 I/O/VCC/GND、BEEP/+5V/GND 标注

## GPIO 与控制信号

### BEEP 控制输入

BEEP 从 J1.2 引入，经 R1（1KΩ(1001) ±1%）连接 Q1 基极，并由 R2（4.7KΩ(4701) ±1%）下拉到 GND。

- 参数与网络：`connector_pin=J1.2`；`net=BEEP`；`base_resistor=R1 1KΩ(1001) ±1%`；`pulldown=R2 4.7KΩ(4701) ±1%`；`driver=Q1 SS8050 Y1`；`direction=J1 to Q1`
- 证据：图 e97555620a70 / 第 1 页 / J1.2 BEEP 与页面右下 BEEP-R1/Q1、BEEP-R2-GND

## 保护电路

### LS1 续流钳位

D1 1N4007WS 反向跨接在 LS1 的 R3/+3.3V 高端节点与 Q1 集电极低端节点之间，为蜂鸣器驱动回路提供钳位路径。

- 参数与网络：`diode=D1 1N4007WS`；`high_node=R3/LS1 high side`；`low_node=LS1 low side/Q1 collector`；`topology=parallel across LS1`
- 证据：图 e97555620a70 / 第 1 页 / 页面右上 D1 跨接 LS1 上下两端节点

### J1 外部接口保护

J1 的 BEEP、+5V 和 GND 直接进入输入偏置、电源与地网络，本页未显示 TVS、保险丝、反接保护或串联输入保护器件。

- 参数与网络：`connector=J1`；`signals=BEEP,+5V,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`
- 证据：图 e97555620a70 / 第 1 页 / J1 至 BEEP/R1/R2 与 +5V/U1 的直接路径

## 关键网络

### LS1 低侧节点

LS1 低端、Q1 集电极和 D1 低端连接在同一节点；该节点由 Q1 向 GND 开关。

- 参数与网络：`connections=LS1 low,Q1 collector,D1 low`；`switch_to=GND`；`switch=Q1 SS8050 Y1`
- 证据：图 e97555620a70 / 第 1 页 / 页面右侧 LS1 下端/D1 下端/Q1 集电极公共节点

## 存储

### 主控与存储

本页未显示 MCU、Flash、EEPROM、SD 卡或其他存储器，声音波形必须由 J1.2 的外部 BEEP 信号提供。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`control_source=external BEEP on J1.2`
- 证据：图 e97555620a70 / 第 1 页 / 第 1 页全图，无主控或存储器位号

## 音频

### Q1/LS1 驱动

Q1 SS8050 Y1 的基极由 BEEP/R1 驱动，集电极连接 LS1 低端，发射极接 GND，构成蜂鸣器低侧开关。

- 参数与网络：`transistor=Q1 SS8050 Y1`；`base=BEEP via R1 1KΩ`；`collector=LS1 low side`；`emitter=GND`；`load_high_side=+3.3V via R3 10Ω`
- 证据：图 e97555620a70 / 第 1 页 / 页面右侧 Q1 三端与 BEEP/R1、LS1、GND 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `input_connector=J1 HY-2.0_IO`；`regulator=U1 HT7533`；`driver=Q1 SS8050 Y1`；`sounder=LS1 Buzzer`；`flyback=D1 1N4007WS`；`controller=原理图未显示`；`storage=原理图未显示` |
| 接口 | J1 HY-2.0_IO | `reference=J1`；`part_number=HY-2.0_IO`；`pin_1=I/no visible net`；`pin_2=O/BEEP`；`pin_3=VCC/+5V`；`pin_4=GND` |
| 电源 | U1 5V 到 3.3V LDO | `regulator=U1 HT7533`；`input_pin=2`；`input_rail=+5V`；`output_pin=3`；`output_rail=+3.3V`；`ground_pin=1`；`input_capacitor=C1 10uF`；`output_capacitors=C2 10uF,C3 100nF` |
| 电源 | LS1 供电路径 | `rail=+3.3V`；`series_resistor=R3 10Ω`；`load=LS1 Buzzer`；`low_side_switch=Q1 SS8050 Y1`；`return=GND` |
| GPIO 与控制信号 | BEEP 控制输入 | `connector_pin=J1.2`；`net=BEEP`；`base_resistor=R1 1KΩ(1001) ±1%`；`pulldown=R2 4.7KΩ(4701) ±1%`；`driver=Q1 SS8050 Y1`；`direction=J1 to Q1` |
| 音频 | Q1/LS1 驱动 | `transistor=Q1 SS8050 Y1`；`base=BEEP via R1 1KΩ`；`collector=LS1 low side`；`emitter=GND`；`load_high_side=+3.3V via R3 10Ω` |
| 保护电路 | LS1 续流钳位 | `diode=D1 1N4007WS`；`high_node=R3/LS1 high side`；`low_node=LS1 low side/Q1 collector`；`topology=parallel across LS1` |
| 关键网络 | LS1 低侧节点 | `connections=LS1 low,Q1 collector,D1 low`；`switch_to=GND`；`switch=Q1 SS8050 Y1` |
| 电源 | 电源滤波 | `input_bulk=C1 10uF +5V-to-GND`；`output_bulk=C2 10uF +3.3V-to-GND`；`output_bypass=C3 100nF +3.3V-to-GND` |
| 保护电路 | J1 外部接口保护 | `connector=J1`；`signals=BEEP,+5V,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示` |
| 存储 | 主控与存储 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`control_source=external BEEP on J1.2` |
| GPIO 与控制信号 | BEEP 驱动电气规格 | `input=BEEP`；`series_resistor=R1 1KΩ`；`pulldown=R2 4.7KΩ`；`frequency_candidate=4KHz`；`duty_candidate=1/2 duty`；`logic_voltage=未标注`；`dc_limit=未标注` |
| 音频 | LS1 类型与声学/功耗参数 | `reference=LS1`；`part_number=Buzzer`；`active_or_passive=未标注`；`sound_pressure_candidate=72dB`；`current_candidate=5V@86mA`；`resonant_frequency=未标注` |

## 待确认事项

- `gpio.drive-waveform-undetermined`：原理图给出 BEEP 到 Q1 的电阻网络，但未标注允许输入电压、逻辑阈值、推荐 PWM 频率、占空比或禁止直流高电平条件，不能由图纸确认正文中的 4KHz 1/2 duty 要求。（证据：图 e97555620a70 / 第 1 页 / BEEP-R1/R2-Q1 电路无频率、占空比或输入阈值文字）
- `audio.buzzer-performance-undetermined`：LS1 仅标注 Buzzer，没有具体型号、无源/有源类型、声压、谐振频率、额定电流或功耗，不能由本页确认正文中的 72dB 与 5V@86mA。（证据：图 e97555620a70 / 第 1 页 / LS1 符号仅标 Buzzer，无型号、声压、电流或频率文字）
- `review.drive-waveform`：BEEP 的允许逻辑电压、保证导通阈值、推荐 PWM 频率/占空比以及直流高电平限制是什么？；原因：原理图只显示 R1/R2/Q1 输入网络，没有波形或逻辑电气规格。
- `review.buzzer-performance`：LS1 的准确型号、无源/有源类型、额定电流、谐振频率与声压规格是什么？；原因：原理图仅标注 LS1 Buzzer，未给出器件型号和性能数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e97555620a70ba84cce99659111c43e89119c25b45636bbfbe075a6a30ae3173` | `https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_sch_01.webp` |

---

源文档：`zh_CN/unit/buzzer.md`

源文档 SHA-256：`7c9d41fed52706d1eff95bf6dac589d5691d9abb0935e33191aaea8ffbad0254`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
