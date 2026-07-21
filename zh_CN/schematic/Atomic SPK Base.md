# Atomic SPK Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic SPK Base |
| SKU | A098 |
| 产品 ID | `atomic-spk-base-f156fbb512e7` |
| 源文档 | `zh_CN/atom/Atomic SPK Base.md` |

## 概述

Atomic SPK Base 由 U1 TF-015 卡座和 U2 NS4168 音频功放组成。卡座的 MOSI、CLK、MISO 连接 Atom，CS 只经 Rp1 4.7KΩ 下拉到 GND；图中没有主机 CS 线，因此存储接口的实际协议模式需要确认。NS4168 由 3.3V 供电，以 LRCLK、BCLK、DATA 接收数字音频，VON/VOP 差分输出同时连接 P5 两针扬声器头和 J1 3.5mm 插座。P1/P2 构成 Atom 接口，P3/P4 重复引出 I2S 与 3.3V。正文中的 8kHz~96kHz、自适应检测、1W 输出和 1W@8Ω 扬声器参数不直接出现在原理图上。

## 检索关键词

`Atomic SPK Base`、`A098`、`NS4168`、`TF-015`、`microSD`、`I2S`、`LRCLK`、`BCLK`、`DATA`、`MOSI`、`CLK`、`MISO`、`CS`、`VON`、`VOP`、`3.3V`、`5VIN`、`P5 Header2`、`3.5mm jack`、`8kHz~96kHz`、`1W@8Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TF-015 | 存储卡座，连接 CS、MOSI、CLK、MISO、3.3V 和 GND | 图 6350bd8032e5 / 第 1 页 / 第 1 页左上 U1 TF-015，pins2-7 为 CS/MOSI/VCC/CLK/GND/MISO |
| Rp1 | 4 x 4.7KΩ (472) ±5% | TF-015 CS/MOSI/CLK/MISO 的上拉或下拉电阻阵列 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左上 Rp1，top pins8/7/6 接 +3.3V、top pin5 接 GND，bottom pins1/2/3/4 接 U1 MISO/CLK/MOSI/CS |
| U2 | NS4168 | I2S 数字音频功放，输出 VON/VOP 差分音频 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 NS4168，CTRL/LRCLK/BCLK/SDATA/GND/VDD/VON/VOP |
| P5 | Header 2 | VON/VOP 差分扬声器输出接口 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 P5 Header2，pin2 接 VON、pin1 接 VOP |
| J1 | 3.5mm_jack | VON/VOP 差分音频的 3.5mm 输出插座 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右中 J1 3.5mm_jack，pins2/3 接 VON/VOP，pins1/4 未连接 |
| P1,P2 | Header 5 / Header 4 | Atom 主机的 3.3V、5VIN、I2S、存储信号与 GND 接口 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P2 Header4 与 P1 Header5，LRCLK/DATA/+5VIN/GND/+3.3V/BCLK/MOSI/CLK/MISO |
| P3,P4 | Header 2X2 | 两组重复的 DATA/LRCLK/BCLK/+3.3V 数字音频扩展头 | 图 6350bd8032e5 / 第 1 页 / 第 1 页中部 P3/P4 Header2X2，pins1-4 为 DATA/BCLK/LRCLK/+3.3V |
| C1,C2,C3 | 100nF / 100nF / 10uF | 3.3V、5VIN 与 NS4168 供电去耦 | 图 6350bd8032e5 / 第 1 页 / 第 1 页 C1 100nF 从 +3.3V 到 GND、C2 100nF 从 +5VIN 到 GND、C3 10uF 从 U2 VDD/+3.3V 到 GND |

## 系统结构

### Atomic SPK Base 系统架构

U1 TF-015 通过 MOSI/CLK/MISO 连接 Atom 存储信号，U2 NS4168 通过 LRCLK/BCLK/DATA 接收数字音频并以 VON/VOP 驱动 P5 与 J1；两部分均使用 Atom 提供的 3.3V/GND。

- 参数与网络：`storage=U1 TF-015`；`storage_signals=MOSI,CLK,MISO`；`amplifier=U2 NS4168`；`audio_bus=LRCLK,BCLK,DATA`；`audio_outputs=VON,VOP`；`speaker_output=P5 Header2`；`headphone_output=J1 3.5mm_jack`；`logic_supply=+3.3V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页完整单页：U1/Rp1/P1/P2 与 U2/P5/J1/P3/P4 的信号和电源连接

## 电源

### Atom 3.3V 与 5VIN 电源

P1 pin1 提供 +3.3V，P2 pin3 提供 +5VIN，P2 pin4 为 GND；C1 100nF 从 +3.3V 接 GND，C2 100nF 从 +5VIN 接 GND。U1 和 U2 使用 +3.3V，图中未显示 +5VIN 的其他负载。

- 参数与网络：`three_volt_input=P1 pin1 +3.3V`；`five_volt_input=P2 pin3 +5VIN`；`ground=P2 pin4 GND`；`three_volt_decoupling=C1 100nF (104) 10% 50V`；`five_volt_decoupling=C2 100nF (104) 10% 50V`；`three_volt_consumers=U1 VCC, U2 CTRL/VDD, P3/P4 pin4`；`five_volt_consumers=C2 only on this page`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P1/P2/C1/C2 与 U1/U2/P3/P4 的 +3.3V/+5VIN/GND 网络

## 接口

### P1/P2 Atom 主机接口

P2 pins1-4 依次为 LRCLK、DATA、+5VIN、GND；P1 pins1-5 依次为 +3.3V、BCLK、MOSI、CLK、MISO。

- 参数与网络：`P2_pin1=LRCLK`；`P2_pin2=DATA`；`P2_pin3=+5VIN`；`P2_pin4=GND`；`P1_pin1=+3.3V`；`P1_pin2=BCLK`；`P1_pin3=MOSI`；`P1_pin4=CLK`；`P1_pin5=MISO`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P2 Header4 与 P1 Header5 的 pin1-pin5 网络标签

### P3/P4 I2S 扩展头

P3 和 P4 的 pin1 为 DATA、pin2 为 BCLK、pin3 为 LRCLK、pin4 为 +3.3V，两组 Header2X2 电气映射相同。

- 参数与网络：`P3=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`；`P4=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页中左 P3 与右下 P4 Header2X2 的 pin1-pin4 标号和网络

## 总线

### NS4168 数字音频总线

U2 LRCLK pin2、BCLK pin3、SDATA pin4 分别连接 LRCLK、BCLK、DATA 网络，并通过 P2/P1 连接 Atom，同时由 P3/P4 两组 Header2X2 重复引出。

- 参数与网络：`LRCLK=U2 pin2 -> P2 pin1 -> P3/P4 pin3`；`BCLK=U2 pin3 -> P1 pin2 -> P3/P4 pin2`；`DATA=U2 pin4 SDATA -> P2 pin2 -> P3/P4 pin1`；`breakout_supply=P3/P4 pin4 +3.3V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页 U2 pins2-4、P1/P2 与 P3/P4 的 LRCLK/BCLK/DATA 同名网络

## 存储

### U1 TF-015 卡座连接

U1 pin2 为 CS，pin3 为 MOSI，pin4 接 +3.3V，pin5 为 CLK，pin6 接 GND，pin7 为 MISO；图中未使用该符号的其他卡信号。

- 参数与网络：`pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左上 U1 pins2-7 与右侧文字、网络标签

### TF-015 信号偏置

Rp1 为四联 4.7KΩ 阵列：MISO、CLK、MOSI 三路通过对应电阻接 +3.3V，CS 通过第四路电阻接 GND。

- 参数与网络：`array=Rp1 4 x 4.7KΩ (472) ±5%`；`MISO=4.7KΩ to +3.3V`；`CLK=4.7KΩ to +3.3V`；`MOSI=4.7KΩ to +3.3V`；`CS=4.7KΩ to GND`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左上 Rp1 top pins8/7/6 接 +3.3V、top pin5 接 GND，bottom pins1/2/3/4 接 MISO/CLK/MOSI/CS

## 音频

### NS4168 供电与控制

U2 CTRL pin1 与 VDD pin6 均接 +3.3V，GND pin7 接地；C3 10uF/10V 从 +3.3V 接 GND。

- 参数与网络：`control=CTRL pin1 +3.3V`；`supply=VDD pin6 +3.3V`；`ground=GND pin7`；`decoupling=C3 10uF (106) 10% 10V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 pins1/6/7 与 +3.3V/GND、C3

### P5 差分扬声器输出

U2 VON pin5 连接 P5 pin2，VOP pin8 连接 P5 pin1，P5 标注为 Header 2；输出两端没有在图中接地。

- 参数与网络：`negative_output=U2 VON pin5 -> P5 pin2`；`positive_output=U2 VOP pin8 -> P5 pin1`；`connector=P5 Header 2`；`grounded_output=false`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 pins5/8 与 P5 pins2/1

### J1 3.5mm 插座输出

J1 标注 3.5mm_jack，pins2/3 分别连接 VON/VOP，pins1/4 未连接；该插座与 P5 并联在同一差分输出网络。

- 参数与网络：`connector=J1 3.5mm_jack`；`pin2=VON`；`pin3=VOP`；`pin1=NC`；`pin4=NC`；`parallel_output=P5`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右中 J1 pins1-4 与来自 U2/P5 的 VON/VOP 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic SPK Base 系统架构 | `storage=U1 TF-015`；`storage_signals=MOSI,CLK,MISO`；`amplifier=U2 NS4168`；`audio_bus=LRCLK,BCLK,DATA`；`audio_outputs=VON,VOP`；`speaker_output=P5 Header2`；`headphone_output=J1 3.5mm_jack`；`logic_supply=+3.3V` |
| 存储 | U1 TF-015 卡座连接 | `pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO` |
| 存储 | TF-015 信号偏置 | `array=Rp1 4 x 4.7KΩ (472) ±5%`；`MISO=4.7KΩ to +3.3V`；`CLK=4.7KΩ to +3.3V`；`MOSI=4.7KΩ to +3.3V`；`CS=4.7KΩ to GND` |
| 存储 | TF-015 存储接口协议模式 | `documented_bus=SPI`；`host_signals=MOSI,CLK,MISO`；`host_cs=null`；`card_cs=Rp1 4.7KΩ pull-down to GND`；`mode=null` |
| 总线 | NS4168 数字音频总线 | `LRCLK=U2 pin2 -> P2 pin1 -> P3/P4 pin3`；`BCLK=U2 pin3 -> P1 pin2 -> P3/P4 pin2`；`DATA=U2 pin4 SDATA -> P2 pin2 -> P3/P4 pin1`；`breakout_supply=P3/P4 pin4 +3.3V` |
| 音频 | NS4168 供电与控制 | `control=CTRL pin1 +3.3V`；`supply=VDD pin6 +3.3V`；`ground=GND pin7`；`decoupling=C3 10uF (106) 10% 10V` |
| 音频 | P5 差分扬声器输出 | `negative_output=U2 VON pin5 -> P5 pin2`；`positive_output=U2 VOP pin8 -> P5 pin1`；`connector=P5 Header 2`；`grounded_output=false` |
| 音频 | J1 3.5mm 插座输出 | `connector=J1 3.5mm_jack`；`pin2=VON`；`pin3=VOP`；`pin1=NC`；`pin4=NC`；`parallel_output=P5` |
| 电源 | Atom 3.3V 与 5VIN 电源 | `three_volt_input=P1 pin1 +3.3V`；`five_volt_input=P2 pin3 +5VIN`；`ground=P2 pin4 GND`；`three_volt_decoupling=C1 100nF (104) 10% 50V`；`five_volt_decoupling=C2 100nF (104) 10% 50V`；`three_volt_consumers=U1 VCC, U2 CTRL/VDD, P3/P4 pin4`；`five_volt_consumers=C2 only on this page` |
| 接口 | P1/P2 Atom 主机接口 | `P2_pin1=LRCLK`；`P2_pin2=DATA`；`P2_pin3=+5VIN`；`P2_pin4=GND`；`P1_pin1=+3.3V`；`P1_pin2=BCLK`；`P1_pin3=MOSI`；`P1_pin4=CLK`；`P1_pin5=MISO` |
| 接口 | P3/P4 I2S 扩展头 | `P3=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`；`P4=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V` |
| 音频 | 正文中的 NS4168 采样能力 | `documented_sample_rate=8kHz~96kHz`；`documented_auto_detection=true`；`documented_adaptation=true`；`schematic_part=U2 NS4168` |
| 音频 | 正文中的输出功率与扬声器规格 | `documented_amplifier_output=1W at VDD=3.3V`；`documented_speaker=1W@8Ω`；`documented_connector=1.25mm-2P`；`schematic_supply=U2 VDD +3.3V`；`schematic_connector=P5 Header 2` |

## 待确认事项

- `storage.card-interface-mode`：正文与管脚表把 MOSI/CLK/MISO 描述为 SPI，但原理图没有从 Atom 引出 CS，U1 CS 仅经 4.7KΩ 下拉到 GND；无法由该页确认实际使用标准 SPI 还是其他三线 SD 模式。（证据：图 6350bd8032e5 / 第 1 页 / 第 1 页 U1 CS 只连接 Rp1 下拉；P1/P2 仅引出 MOSI/CLK/MISO，没有 CS 网络）
- `audio.documented-ns4168-capabilities`：正文称 NS4168 支持 8kHz~96kHz、自动采样率检测和自适应功能；原理图只确认芯片型号及 LRCLK/BCLK/SDATA 电气连接，无法单独证明这些数据手册能力。（证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 仅标 NS4168 与引脚，不含采样率或自动检测文字）
- `audio.documented-output-ratings`：正文给出功放输出 1W@VDD 3.3V、配套扬声器 1W@8Ω、扬声器接口 1.25mm-2P；原理图确认 VDD 3.3V 和 P5 Header2，但没有负载、功率、阻抗或接口间距标注。（证据：图 6350bd8032e5 / 第 1 页 / 第 1 页 U2 VDD/VON/VOP 与 P5 Header2，图中无 1W、8Ω 或 1.25mm 标注）
- `review.storage-interface-mode`：Atomic SPK Base 的 TF-015 实际使用 SPI 还是 1-bit SD 模式，软件初始化时如何处理未引出的 CS？；原因：图纸只有 MOSI/CLK/MISO 主机线，CS 仅 4.7KΩ 下拉；旧文档关于主机 CS 路径的说法缺少图纸证据。
- `review.ns4168-datasheet-capabilities`：当前 NS4168 datasheet 版本是否确认 8kHz~96kHz、自动采样率检测和自适应能力？；原因：这些是芯片数据手册能力，原理图只能确认 NS4168 型号和 I2S 引脚连接。
- `review.audio-output-ratings`：1W@3.3V、1W@8Ω 与 P5 1.25mm-2P 是否由当前 BOM、NS4168 datasheet 和整机测试确认？；原因：原理图没有标扬声器负载、输出功率或 P5 间距，需 BOM/规格书/测试记录补证。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6350bd8032e5d535e15fc3d932e6d4f4358a99329bec122f73380497fed9f133` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-315f8e96-ce32-4861-809c-cb02f5def6b5.webp` |

---

源文档：`zh_CN/atom/Atomic SPK Base.md`

源文档 SHA-256：`d3502fdda63dfbf8dfea82e365bbb0bc2137421113abd914c1c2afd0cdae0a2d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
