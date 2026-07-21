# Hat SPK2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat SPK2 |
| SKU | U055-B |
| 产品 ID | `hat-spk2-bc9ad7479cc6` |
| 源文档 | `zh_CN/hat/Hat-SPK2.md` |

## 概述

Hat SPK2 以 U1 MAX98357AETE 数字音频功放为核心，通过 P1 STICKIO 接收 G26/BCLK、G36或G25/SDATA 与 G0/LRCLK 三条 I2S 信号。U1 由 +3.3V 供电，SD_MODE 上拉、GAIN_SLOT 下拉，OUTP/OUTN 分别经 FB2/FB1 0Ω送到 P2 两针差分输出。VDD 配置 10uF、1uF 与 100uF 去耦，两个输出各有 1nF 对地电容。

## 检索关键词

`Hat SPK2`、`U055-B`、`MAX98357AETE`、`MAX98357`、`I2S`、`BCLK G26`、`SDATA G36 G25`、`LRCLK G0`、`SD_MODE`、`GAIN_SLOT`、`OUTP`、`OUTN`、`P2 differential output`、`FB1 0R`、`FB2 0R`、`+3.3V`、`C1 10uF`、`C2 1uF`、`C5 100uF`、`STICKIO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX98357AETE | I2S 数字输入差分扬声器功率放大器 | 图 3a8a0f63cea8 / 第 1 页 / 第1页网格 C2-C3：U1 MAX98357AETE pins1-16 |
| P1 | STICKIO | 主机 I2S 与 3.3V/GND 接口 | 图 3a8a0f63cea8 / 第 1 页 / 第1页网格 C2：P1 STICKIO pins1-8 |
| P2 | Header 2 | OUTP/OUTN 差分扬声器输出接口 | 图 3a8a0f63cea8 / 第 1 页 / 第1页网格 C4：P2 Header 2 |
| FB1,FB2 | 0Ω | OUTN/OUTP 到 P2 的串联器件位 | 图 3a8a0f63cea8 / 第 1 页 / 第1页网格 C3-C4：FB1/FB2 0Ω |
| R1,R2 | 10KΩ marking | SD_MODE 上拉与 GAIN_SLOT 下拉配置网络 | 图 3a8a0f63cea8 / 第 1 页 / 第1页网格 C2：R1/R2 与 U1 pins4/2 |

## 系统结构

### Hat SPK2 架构

P1 提供 I2S 与 +3.3V，U1 MAX98357AETE 将数字音频转换为 OUTP/OUTN 差分功率输出，FB1/FB2 连接 P2。

- 参数与网络：`amplifier=U1 MAX98357AETE`；`host=P1 STICKIO`；`output=P2 Header 2`；`rail=+3.3V`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页完整单页

## 电源

### MAX98357 3.3V 供电

P1 pin7/3V3 连接 +3.3V并供给 U1 VDD pins7/8；C1 10uF、C2 1uF、C5 100uF 从 +3.3V 对地。

- 参数与网络：`input=P1 pin7 3V3`；`rail=+3.3V`；`amplifier_pins=U1 VDD pins7/8`；`decoupling=C1 10uF; C2 1uF; C5 100uF`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 U1 pins7/8、C1/C2/C5、P1 pin7

## 接口

### P2 扬声器接口

P2 Header 2 pin1 为 OUTP 经 FB2 的正向输出，pin2 为 OUTN 经 FB1 的负向输出；P2 不提供 GND 引脚。

- 参数与网络：`pin1=OUTP via FB2`；`pin2=OUTN via FB1`；`type=differential`；`ground_pin=false`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 C4：P2 pins1-2

### P1 STICKIO 接口

P1 pin1 为 GND、pin3 G26 为 BCLK、pin4 G36/G25 为 SDATA、pin5 G0 为 LRCLK、pin7 3V3 接 +3.3V；pins2 5VOUT、6 BAT、8 5VIN 未使用。

- 参数与网络：`pin1=GND`；`pin2=5VOUT unused`；`pin3=G26/BCLK`；`pin4=G36/G25/SDATA`；`pin5=G0/LRCLK`；`pin6=BAT unused`；`pin7=3V3/+3.3V`；`pin8=5VIN unused`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 C2：P1 pins1-8

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或额外外部时钟器件；音频时钟由 P1 BCLK/LRCLK 提供。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`audio_clocks=BCLK,LRCLK`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页完整单页与 P1 BCLK/LRCLK

## 保护电路

### 外部保护可见性

本页未画 P1、P2 或 I2S 信号上的 TVS、ESD、保险丝；输出串联器件为 FB1/FB2 0Ω。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`output_series=FB1/FB2 0Ω`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页完整单页保护器件范围

## 音频

### I2S 数字音频输入

P1 pin3/G26 形成 BCLK并连接 U1 pin16，P1 pin4/G36/G25 形成 SDATA并连接 U1 DIN pin1，P1 pin5/G0 形成 LRCLK并连接 U1 pin14。

- 参数与网络：`bclk=P1 pin3 G26 -> U1 pin16 BCLK`；`data=P1 pin4 G36/G25 -> U1 pin1 DIN`；`lrclk=P1 pin5 G0 -> U1 pin14 LRCLK`；`direction=host outputs to amplifier inputs`；`logic_level=+3.3V`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 P1 BCLK/SDATA/LRCLK 与 U1 pins16/1/14

### MAX98357 模式配置

U1 SD_MODE pin4 通过 R1 接 +3.3V，GAIN_SLOT pin2 通过 R2 接 GND；原理图在 R1/R2 旁标注 10KΩ。

- 参数与网络：`sd_mode=U1 pin4 -> R1 -> +3.3V`；`gain_slot=U1 pin2 -> R2 -> GND`；`value_marking=10KΩ`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 U1 pins4/2 与 R1/R2

### 差分扬声器输出

U1 OUTN pin10 经 FB1 0Ω连接 P2 pin2，OUTP pin9 经 FB2 0Ω连接 P2 pin1；C3/C4 各 1nF 从对应输出侧对地。

- 参数与网络：`negative=U1 OUTN pin10 -> FB1 0Ω -> P2 pin2`；`positive=U1 OUTP pin9 -> FB2 0Ω -> P2 pin1`；`negative_cap=C3 1nF to GND`；`positive_cap=C4 1nF to GND`；`direction=amplifier differential output`
- 证据：图 3a8a0f63cea8 / 第 1 页 / 第1页 U1 pins9/10、FB1/FB2、C3/C4、P2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat SPK2 架构 | `amplifier=U1 MAX98357AETE`；`host=P1 STICKIO`；`output=P2 Header 2`；`rail=+3.3V` |
| 音频 | I2S 数字音频输入 | `bclk=P1 pin3 G26 -> U1 pin16 BCLK`；`data=P1 pin4 G36/G25 -> U1 pin1 DIN`；`lrclk=P1 pin5 G0 -> U1 pin14 LRCLK`；`direction=host outputs to amplifier inputs`；`logic_level=+3.3V` |
| 音频 | MAX98357 模式配置 | `sd_mode=U1 pin4 -> R1 -> +3.3V`；`gain_slot=U1 pin2 -> R2 -> GND`；`value_marking=10KΩ` |
| 音频 | 差分扬声器输出 | `negative=U1 OUTN pin10 -> FB1 0Ω -> P2 pin2`；`positive=U1 OUTP pin9 -> FB2 0Ω -> P2 pin1`；`negative_cap=C3 1nF to GND`；`positive_cap=C4 1nF to GND`；`direction=amplifier differential output` |
| 接口 | P2 扬声器接口 | `pin1=OUTP via FB2`；`pin2=OUTN via FB1`；`type=differential`；`ground_pin=false` |
| 电源 | MAX98357 3.3V 供电 | `input=P1 pin7 3V3`；`rail=+3.3V`；`amplifier_pins=U1 VDD pins7/8`；`decoupling=C1 10uF; C2 1uF; C5 100uF` |
| 接口 | P1 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT unused`；`pin3=G26/BCLK`；`pin4=G36/G25/SDATA`；`pin5=G0/LRCLK`；`pin6=BAT unused`；`pin7=3V3/+3.3V`；`pin8=5VIN unused` |
| 保护电路 | 外部保护可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`output_series=FB1/FB2 0Ω` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false`；`audio_clocks=BCLK,LRCLK` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3a8a0f63cea8b1ceb2d15f2246509553e876b064a8a5a69d2bd45267f6136e2a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/580/Sch_Hat_SPK2_sch_01.png` |

---

源文档：`zh_CN/hat/Hat-SPK2.md`

源文档 SHA-256：`b955da437d8c23e750ee64e14be5b35aa4fea0634757a91159c9b176ace1c9c7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
