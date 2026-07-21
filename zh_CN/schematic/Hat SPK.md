# Hat SPK 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat SPK |
| SKU | U055 |
| 产品 ID | `hat-spk-360caf2204fc` |
| 源文档 | `zh_CN/hat/hat-spk.md` |

## 概述

Hat SPK 以 U1 PAM8303 单声道桥接音频功放驱动 LS1 Speaker，原理图标注增益为 2。主机 G26 经 C1/R1 输入到 IN-，IN+ 经 C2/R2 交流参考到 GND；G0 经 R4 控制 SD，并由 R3 上拉到 3.3 V。功放 VDD/PVDD 使用 StickIO 5VOUT，输出为 OUT+/OUT- 差分桥接，不与地相连。

## 检索关键词

`Hat SPK`、`U055`、`PAM8303`、`LS1 Speaker`、`G26`、`G0`、`IN-`、`IN+`、`OUT+`、`OUT-`、`SD`、`Gain=2`、`5VOUT`、`+5V`、`+3.3V`、`C1 10nF`、`C2 10nF`、`R1 150K`、`R2 150K`、`R3 10K`、`R4 0R`、`bridge-tied load`、`audio amplifier`、`STICKIO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PAM8303 | 单声道差分输入、桥接输出音频功率放大器 | 图 5c9959fd855a / 第 1 页 / B2-C3，U1 PAM8303、IN-/IN+/SD/OUT+/OUT-/VDD/PVDD |
| LS1 | Speaker | 连接 PAM8303 OUT+/OUT- 的扬声器负载 | 图 5c9959fd855a / 第 1 页 / B3，LS1 Speaker 跨接 OUT+/OUT- |
| P1 | STICKIO | 主机 HAT 接口，提供 G26 音频、G0 关断控制、5 V、3.3 V 与 GND | 图 5c9959fd855a / 第 1 页 / B1-C1，P1 STICKIO pins 1-8 |
| C1/R1 | 10nF / 150KΩ | G26 到 PAM8303 IN- 的交流耦合和输入电阻 | 图 5c9959fd855a / 第 1 页 / B1-B2，G26-C1 10nF-R1 150KΩ-U1 IN- |
| C2/R2 | 10nF / 150KΩ | GND 到 PAM8303 IN+ 的交流参考和匹配输入电阻 | 图 5c9959fd855a / 第 1 页 / B1-C2，GND-C2 10nF-R2 150KΩ-U1 IN+ |
| R3/R4 | 10KΩ / 0Ω | PAM8303 SD 上拉及 G0 控制连接 | 图 5c9959fd855a / 第 1 页 / C2，+3.3V-R3 10KΩ-SD 与 G0-R4 0Ω-SD |
| C3/C4 | 1uF / 1uF | PAM8303 5 V 供电去耦电容 | 图 5c9959fd855a / 第 1 页 / C3，C3/C4 1uF 从 +5V 到 GND |

## 系统结构

### 扬声器 HAT 架构

G26 单端音频经匹配的差分输入网络送入 PAM8303，PAM8303 以 OUT+/OUT- 桥接方式驱动 LS1；G0 控制 SD。

- 参数与网络：`amplifier=U1 PAM8303`；`audio_gpio=G26`；`shutdown_gpio=G0`；`load=LS1 Speaker`；`output_topology=OUT+/OUT- bridge`
- 证据：图 5c9959fd855a / 第 1 页 / 整页：P1、C1/R1、C2/R2、U1、LS1、R3/R4

## 电源

### 功放 5 V 电源

P1 pin2 5VOUT 连接 +5V，并为 U1 VDD/PVDD 供电；C3/C4 各 1 µF 对地去耦。

- 参数与网络：`source=P1 pin2 5VOUT`；`net=+5V`；`pins=U1 pin3 VDD; U1 pin2 PVDD`；`decoupling=C3 1uF; C4 1uF`
- 证据：图 5c9959fd855a / 第 1 页 / P1 5VOUT/+5V 到 U1 VDD/PVDD 与 C3/C4

## 接口

### StickIO 使用情况

P1 pin1 GND、pin2 5VOUT、pin3 G26、pin5 G0、pin7 3V3 被使用；G36、BAT、5VIN 未连接。

- 参数与网络：`pin1=GND`；`pin2=5VOUT`；`pin3=G26 audio`；`pin4=G36 NC`；`pin5=G0 SD`；`pin6=BAT NC`；`pin7=3V3 SD pullup`；`pin8=5VIN NC`
- 证据：图 5c9959fd855a / 第 1 页 / P1 STICKIO pins 1-8 与连接/NC 标记

## GPIO 与控制信号

### 功放 SD 控制

G0 经 R4 0 Ω 连接 U1 SD pin 6，SD 还由 R3 10 kΩ 上拉到 +3.3 V。

- 参数与网络：`gpio=G0`；`series_resistor=R4 0Ω`；`control_pin=U1 pin6 SD`；`pullup=R3 10KΩ to +3.3V`
- 证据：图 5c9959fd855a / 第 1 页 / G0-R4-SD 与 +3.3V-R3-SD

## 音频

### PAM8303 功放

U1 为 PAM8303，原理图明确标注 Gain = 2，输出 pins 1/8 分别为 OUT+/OUT-。

- 参数与网络：`reference=U1`；`part_number=PAM8303`；`gain=2`；`out_plus=pin1`；`out_minus=pin8`
- 证据：图 5c9959fd855a / 第 1 页 / U1 PAM8303 下方 Gain = 2 与 OUT+/OUT-

### 反相音频输入

StickIO G26 经 C1 10 nF 与 R1 150 kΩ 串联到 U1 IN- pin 4。

- 参数与网络：`source=P1 pin3 G26`；`coupling=C1 10nF`；`input_resistor=R1 150KΩ`；`destination=U1 pin4 IN-`
- 证据：图 5c9959fd855a / 第 1 页 / G26-C1-R1-IN- 连线

### 同相输入参考

GND 经 C2 10 nF 与 R2 150 kΩ 串联到 U1 IN+ pin 5，与反相输入使用匹配阻容值。

- 参数与网络：`source=GND`；`coupling=C2 10nF`；`input_resistor=R2 150KΩ`；`destination=U1 pin5 IN+`
- 证据：图 5c9959fd855a / 第 1 页 / GND-C2-R2-IN+ 连线

### 桥接扬声器输出

LS1 扬声器跨接 U1 OUT+ 与 OUT-，扬声器任一端均未连接 GND。

- 参数与网络：`load=LS1 Speaker`；`terminal_1=U1 pin1 OUT+`；`terminal_2=U1 pin8 OUT-`；`grounded_terminal=false`
- 证据：图 5c9959fd855a / 第 1 页 / U1 OUT+/OUT- 到 LS1 两端

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 扬声器 HAT 架构 | `amplifier=U1 PAM8303`；`audio_gpio=G26`；`shutdown_gpio=G0`；`load=LS1 Speaker`；`output_topology=OUT+/OUT- bridge` |
| 音频 | PAM8303 功放 | `reference=U1`；`part_number=PAM8303`；`gain=2`；`out_plus=pin1`；`out_minus=pin8` |
| 音频 | 反相音频输入 | `source=P1 pin3 G26`；`coupling=C1 10nF`；`input_resistor=R1 150KΩ`；`destination=U1 pin4 IN-` |
| 音频 | 同相输入参考 | `source=GND`；`coupling=C2 10nF`；`input_resistor=R2 150KΩ`；`destination=U1 pin5 IN+` |
| GPIO 与控制信号 | 功放 SD 控制 | `gpio=G0`；`series_resistor=R4 0Ω`；`control_pin=U1 pin6 SD`；`pullup=R3 10KΩ to +3.3V` |
| 音频 | 桥接扬声器输出 | `load=LS1 Speaker`；`terminal_1=U1 pin1 OUT+`；`terminal_2=U1 pin8 OUT-`；`grounded_terminal=false` |
| 电源 | 功放 5 V 电源 | `source=P1 pin2 5VOUT`；`net=+5V`；`pins=U1 pin3 VDD; U1 pin2 PVDD`；`decoupling=C3 1uF; C4 1uF` |
| 接口 | StickIO 使用情况 | `pin1=GND`；`pin2=5VOUT`；`pin3=G26 audio`；`pin4=G36 NC`；`pin5=G0 SD`；`pin6=BAT NC`；`pin7=3V3 SD pullup`；`pin8=5VIN NC` |
| 核心器件 | 扬声器阻抗与额定功率 | `reference=LS1`；`schematic_marking=Speaker`；`impedance=not printed`；`power=not printed`；`part_number=not printed` |
| 音频 | 3 W 输出与失真 | `claimed_supply=5V`；`claimed_load=4Ω`；`claimed_power=3W`；`claimed_thd=10%` |
| 电源 | 供电范围与保护能力 | `schematic_supply=+5V`；`claimed_range=2.8-5.5V`；`claimed_protection=short-circuit protection`；`claimed_other=high PSRR; low EMI; low idle noise` |

## 待确认事项

- `component.speaker-rating`：原理图仅将 LS1 标为 Speaker，未标注阻抗、额定功率、频响或具体料号。（证据：图 5c9959fd855a / 第 1 页 / LS1 仅标 Speaker）
- `audio.output-performance`：产品正文称 5 V、4 Ω 负载下输出 3 W 且 THD 10%，但原理图未直接标注这些性能条件。（证据：图 5c9959fd855a / 第 1 页 / U1/LS1 电路未列输出功率或 THD）
- `power.operating-range-protection`：原理图使用 +5 V 电源，但未直接标注 PAM8303 的 2.8–5.5 V 工作范围、短路保护、PSRR、EMI 或无输入噪声性能。（证据：图 5c9959fd855a / 第 1 页 / U1 PAM8303 电路只标供电与 Gain=2）
- `review.speaker-rating`：请用 LS1 BOM/扬声器标签确认阻抗、额定功率和料号。；原因：原理图只标 Speaker。
- `review.output-performance`：请用 PAM8303 datasheet/实测复核 5 V、4 Ω、3 W、10% THD 条件。；原因：原理图不包含性能曲线或额定条件。
- `review.operating-range-protection`：请用 PAM8303 datasheet 复核供电范围、短路保护、PSRR、EMI 和噪声指标。；原因：这些器件规格未印在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5c9959fd855a196d2e4289d0ad50f777b1d7f5116886fad1d5eaa0f990c38aef` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/861/StickHat_SPK_page_01.png` |

---

源文档：`zh_CN/hat/hat-spk.md`

源文档 SHA-256：`75beaa643a6189c4cb467051bbd3a09d3b887203e5e8f2fd6c552ee911c0f612`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
