# Module13.2 RCA 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 RCA |
| SKU | M125 |
| 产品 ID | `module13-2-rca-e64f78ddd7c5` |
| 源文档 | `zh_CN/module/RCA Module 13.2.md` |

## 概述

Module13.2 RCA 从 P1 DC050-T 的 12V/HPWR 输入经 U1 MP1584EN-LF-Z 降压产生 VCC_5V，再由 U2 生成 3V3。U3 PCM5102APWR 接收 DIN、BCK、LRCK 三线 I2S，左右模拟输出 OUTL/OUTR 同时连接 P5/P2 RCA 与 P3 3.5 mm 插孔。S1 在 GPIO25/GPIO26 间选择复合视频源，经可选 R7/C28、L2 与 75 Ω 端接送至 P4；J1 另提供 Port C UART。

## 检索关键词

`Module13.2 RCA`、`M125`、`MP1584EN-LF-Z`、`PCM5102APWR`、`DC050-T`、`12V`、`VCC_5V`、`3V3`、`I2S`、`DIN`、`BCK`、`LRCK`、`OUTL`、`OUTR`、`RCA`、`CVBS`、`GPIO25`、`GPIO26`、`S1 SW-PWR`、`L2 4.7R`、`R5 75R`、`P4 SIG`、`P5 OUTL`、`P2 OUTR`、`P3 headphone`、`GROVE 4P`、`RX`、`TX`、`GPIO16`、`GPIO17`、`M5_BUS`、`HPWR`、`SS34`、`L1 10uH`、`R17 0R`、`AGND`、`GND`、`9-24V`、`PAL`、`864x576`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | PCM5102APWR | I2S 立体声音频 DAC，接收 DIN/BCK/LRCK 并输出 OUTL/OUTR | 图 3161ea60c428 / 第 1 页 / C2-D3 U3 PCM5102APWR pins1-20 |
| U1 | MP1584EN-LF-Z | 将 12V 输入降压为 VCC_5V 的开关转换器 | 图 3161ea60c428 / 第 1 页 / A1-A3 U1 MP1584EN-LF-Z、L1、D1、R1-R6 |
| U2 | 未标注 | 从 VCC_5V 产生 3V3 的五针稳压器，带 EN/BYP 引脚 | 图 3161ea60c428 / 第 1 页 / A4 U2 VIN/VOUT/EN/BYP/GND 与 C7-C10 |
| P1 | DC050-T | 板载直流电源输入插座，正端进入 12V/HPWR 网络 | 图 3161ea60c428 / 第 1 页 / A1 P1 DC050-T pins1-3 and 12V |
| P5/P2 | 未标注 | OUTL 与 OUTR 左右声道 RCA 信号输出连接器，屏蔽/地端接 AGND | 图 3161ea60c428 / 第 1 页 / A4-B4 P5 OUTL/P2 OUTR SIG/G |
| P3 | 未标注 | OUTR/OUTL 经 1 uF 耦合电容连接的 3.5 mm 音频插孔 | 图 3161ea60c428 / 第 1 页 / C1-D1 P3/C11/C12/OUTR/OUTL/AGND |
| P4 | 未标注 | 经 GPIO25/26 选择与 75 Ω 网络驱动的复合视频 RCA 输出 | 图 3161ea60c428 / 第 1 页 / C3-C4 S1/L2/R5/P4 SIG/G |
| S1 | SW-PWR | 在 GPIO25 与 GPIO26 之间选择视频 DAC 信号源 | 图 3161ea60c428 / 第 1 页 / C3 S1 SW-PWR pins1-3/GPIO25/GPIO26 |
| J1 | GROVE 4P | RX、TX、VCC_5V 与 GND 的 Port C UART 接口 | 图 3161ea60c428 / 第 1 页 / B1 J1 GROVE 4P IO2/IO1/5V/GND |
| J3 | M5_BUS | 30 针主机接口，承载 12V/HPWR、VCC_5V、UART、I2S 与视频 GPIO | 图 3161ea60c428 / 第 1 页 / C4-D4 J3 M5_BUS pins1-30 |
| D1/L1 | SS34 / 10uH | MP1584EN 降压电路的续流肖特基二极管与输出电感 | 图 3161ea60c428 / 第 1 页 / A2-A3 U1 SW/D1 SS34/L1 10uH |
| R17 | 0R | AGND 与数字 GND 的单点连接电阻 | 图 3161ea60c428 / 第 1 页 / B3 R17 0R between AGND and GND |

## 系统结构

### Module13.2 RCA 系统架构

P1 输入经 U1 生成 VCC_5V、U2 再生成 3V3；U3 PCM5102APWR 把主机 I2S 转为左右模拟音频，S1 选择 GPIO25/26 视频信号，J3 提供 M5-Bus 连接。

- 参数与网络：`dc_input=P1 DC050-T / 12V`；`buck=U1 MP1584EN-LF-Z`；`5v=VCC_5V`；`3v3=U2`；`audio_dac=U3 PCM5102APWR`；`audio_outputs=P5/P2 RCA and P3 headphone`；`video=GPIO25/GPIO26 -> S1 -> P4`；`host=J3 M5_BUS`
- 证据：图 3161ea60c428 / 第 1 页 / 整页 P1/U1/U2/U3/S1/P2-P5/J3

## 电源

### 12V/HPWR 输入

P1 DC050-T 正端连接 12V 网络，12V 同时连接 J3 的 HPWR 组；输入配置 C1 100 uF/35 V 与 C3 100 nF 对地。

- 参数与网络：`connector=P1 DC050-T`；`rail=12V`；`host_power=J3 HPWR pins25/27/29`；`bulk=C1 100uF/35V`；`decoupling=C3 100nF`
- 证据：图 3161ea60c428 / 第 1 页 / A1 P1/12V/C1/C3；D4 J3 12V/HPWR

### MP1584EN 5 V 降压

U1 MP1584EN-LF-Z 从 12V 经 SW、D1 SS34 与 L1 10 uH 产生 VCC_5V；R1 210 kΩ/R2 39 kΩ 构成反馈分压，R3 100 kΩ 将 EN 上拉到 12V。

- 参数与网络：`input=12V`；`converter=U1 MP1584EN-LF-Z`；`switch_node=SW pin1`；`diode=D1 SS34`；`inductor=L1 10uH`；`output=VCC_5V`；`feedback=R1 210K; R2 39K`；`enable=R3 100K to 12V`
- 证据：图 3161ea60c428 / 第 1 页 / A2-A3 U1/D1/L1/R1-R3/VCC_5V

### MP1584EN 频率与补偿网络

U1 BST pin8 通过 C5 100 nF 接 SW，FREQ pin6 通过 R4 100 kΩ 接 GND，COMP pin3 通过 C4 150 pF 与 R6 100 kΩ 接 GND。

- 参数与网络：`bootstrap=C5 100nF BST-to-SW`；`frequency=R4 100K FREQ-to-GND`；`compensation=C4 150pF and R6 100K from COMP to GND`
- 证据：图 3161ea60c428 / 第 1 页 / A1-A2 U1 BST/FREQ/COMP/C5/R4/C4/R6

### VCC_5V 输出滤波

VCC_5V 配置 C2 10 uF、C6 100 nF、C22 100 uF/35 V 与 D2 对地；D2 的具体型号/作用文字未标。

- 参数与网络：`rail=VCC_5V`；`capacitors=C2 10uF; C6 100nF; C22 100uF/35V`；`diode=D2, part number not printed`
- 证据：图 3161ea60c428 / 第 1 页 / A3 VCC_5V/C2/C6/D2/C22

### VCC_5V 至 3V3

U2 从 VCC_5V 生成 3V3，输入配置 C7 10 uF/C8 100 nF，输出配置 C9 100 nF/C10 10 uF；U2 型号未印在页面。

- 参数与网络：`regulator=U2, part number not printed`；`input=VCC_5V`；`output=3V3`；`input_caps=C7 10uF; C8 100nF`；`output_caps=C9 100nF; C10 10uF`；`ground=pin2`
- 证据：图 3161ea60c428 / 第 1 页 / A4 U2/C7-C10/VCC_5V/3V3

### AGND 与 GND

音频/视频连接器和 PCM5102 模拟部分使用 AGND，数字电源使用 GND，两者由 R17 0 Ω 单点连接。

- 参数与网络：`analog_ground=AGND`；`digital_ground=GND`；`link=R17 0R`；`analog_loads=U3 analog, P2/P3/P4/P5`
- 证据：图 3161ea60c428 / 第 1 页 / B3 R17 AGND-GND and output ground symbols

## 接口

### Port C UART

J1 GROVE 4P 的 IO2 为 RX、IO1 为 TX、5V 为 VCC_5V、GND 接地；RX/TX 分别连接 J3 的 GPIO16/GPIO17。

- 参数与网络：`connector=J1 GROVE 4P`；`io2=RX / GPIO16`；`io1=TX / GPIO17`；`vcc=VCC_5V`；`ground=GND`
- 证据：图 3161ea60c428 / 第 1 页 / B1 J1 RX/TX/VCC_5V/GND；D4 J3 RX/TX

### M5-Bus 使用网络

J3 使用 GND 组、GPIO25/GPIO26 视频信号、GPIO16/GPIO17 Port C、GPIO13/BCK、GPIO15/DIN、GPIO0/LRCK、VCC_5V 与 12V/HPWR；VBAT/BAT_OUT 标为未连接。

- 参数与网络：`video=GPIO25 and GPIO26`；`uart=GPIO16 RX; GPIO17 TX`；`i2s=GPIO13 BCK; GPIO15 DIN; GPIO0 LRCK`；`5v=VCC_5V / bus pin28`；`high_power=12V / HPWR pins25/27/29`；`battery=VBAT/BAT_OUT no-connect`
- 证据：图 3161ea60c428 / 第 1 页 / C4-D4 J3 M5_BUS labels

## 总线

### PCM5102 I2S 输入

J3 的 DIN、BCK、LRCK 分别经 470 Ω 串联电阻连接 U3 DIN pin14、BCK pin13、LRCK pin15；U3 SCK pin12 通过 10 kΩ 接 GND。

- 参数与网络：`device=U3 PCM5102APWR`；`data=DIN -> 470R -> pin14`；`bit_clock=BCK -> 470R -> pin13`；`word_clock=LRCK -> 470R -> pin15`；`system_clock=SCK pin12 -> 10K -> GND`；`direction=host-to-DAC`
- 证据：图 3161ea60c428 / 第 1 页 / C3-D3 U3 pins12-15/R14-R16 and J3 DIN/BCK/LRCK

## 音频

### PCM5102 电源与电荷泵

U3 CPVDD pin1、DVDD pin20、AVDD pin8 接 3V3，CAPP/CAPM 使用 2.2 uF 电容，VNEG 配置 2.2 uF，LDO pin18 配置 C16 100 nF。

- 参数与网络：`supply=CPVDD pin1; DVDD pin20; AVDD pin8 -> 3V3`；`charge_pump=CAPP/CAPM with C15/C17 2.2uF`；`negative_rail=VNEG with 2.2uF`；`ldo_cap=C16 100nF`；`digital_caps=C13/C14 100nF`
- 证据：图 3161ea60c428 / 第 1 页 / C2-D3 U3 power pins/C13-C17

### PCM5102 配置脚

U3 FMT pin16 直接接 GND，XSMT pin17 由 R8 10 kΩ 上拉至 3V3并引到 TP2，DEMP pin10 与 FLT pin11 通过电阻/测试焊盘配置。

- 参数与网络：`format=FMT pin16 GND`；`mute=XSMT pin17; R8 10K to 3V3; TP2 to GND pad`；`deemphasis=DEMP pin10 via TP1/R13`；`filter=FLT pin11 via TP3/R12`
- 证据：图 3161ea60c428 / 第 1 页 / C2-D3 U3 DEMP/FLT/FMT/XSMT/TP1-TP3/R8/R12/R13

### PCM5102 左右模拟输出

U3 OUTL pin6 与 OUTR pin7 形成 OUTL/OUTR，经过 470 Ω 和 2.2 nF 对 AGND 的输出网络，同时直接连接 P5/P2 RCA 信号端。

- 参数与网络：`left=U3 OUTL pin6 -> OUTL -> P5 SIG`；`right=U3 OUTR pin7 -> OUTR -> P2 SIG`；`series=R9/R10 470R`；`shunt_caps=C18/C19 2.2nF to AGND`；`connector_ground=AGND`
- 证据：图 3161ea60c428 / 第 1 页 / B4 P5/P2；C1-D3 U3 OUTL/OUTR/R9/R10/C18/C19

### 3.5 mm 立体声输出

OUTR 经 C11 1 uF、OUTL 经 C12 1 uF 串联连接 P3 的两个音频触点，P3 地端接 AGND。

- 参数与网络：`connector=P3`；`right=OUTR via C11 1uF`；`left=OUTL via C12 1uF`；`ground=AGND`
- 证据：图 3161ea60c428 / 第 1 页 / C1-D1 P3/C11/C12/OUTR/OUTL

## 模拟电路

### GPIO25/GPIO26 视频选择

S1 SW-PWR 在 GPIO25 与 GPIO26 之间选择一路送到视频输出网络，公共端为 pin2。

- 参数与网络：`switch=S1 SW-PWR`；`option_1=GPIO25 / J3 video pin8`；`option_2=GPIO26 / J3 video pin10`；`common=S1 pin2`；`direction=host DAC-to-video-output`
- 证据：图 3161ea60c428 / 第 1 页 / C3 S1 GPIO25/GPIO26 and J3 corresponding nets

### 复合视频输出网络

S1 公共端经 L2 4.7R 串联到 P4 SIG，P4 端由 R5 75 Ω 对 AGND 终端；R7 与 C28 标 DNP，形成可选前级滤波。

- 参数与网络：`source=S1 common`；`optional_filter=R7 DNP; C28 DNP to AGND`；`series=L2 4.7R`；`termination=R5 75R to AGND`；`connector=P4 SIG/G`
- 证据：图 3161ea60c428 / 第 1 页 / C3-C4 S1/R7/C28/L2/R5/P4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 RCA 系统架构 | `dc_input=P1 DC050-T / 12V`；`buck=U1 MP1584EN-LF-Z`；`5v=VCC_5V`；`3v3=U2`；`audio_dac=U3 PCM5102APWR`；`audio_outputs=P5/P2 RCA and P3 headphone`；`video=GPIO25/GPIO26 -> S1 -> P4`；`host=J3 M5_BUS` |
| 电源 | 12V/HPWR 输入 | `connector=P1 DC050-T`；`rail=12V`；`host_power=J3 HPWR pins25/27/29`；`bulk=C1 100uF/35V`；`decoupling=C3 100nF` |
| 电源 | MP1584EN 5 V 降压 | `input=12V`；`converter=U1 MP1584EN-LF-Z`；`switch_node=SW pin1`；`diode=D1 SS34`；`inductor=L1 10uH`；`output=VCC_5V`；`feedback=R1 210K; R2 39K`；`enable=R3 100K to 12V` |
| 电源 | MP1584EN 频率与补偿网络 | `bootstrap=C5 100nF BST-to-SW`；`frequency=R4 100K FREQ-to-GND`；`compensation=C4 150pF and R6 100K from COMP to GND` |
| 电源 | VCC_5V 输出滤波 | `rail=VCC_5V`；`capacitors=C2 10uF; C6 100nF; C22 100uF/35V`；`diode=D2, part number not printed` |
| 电源 | VCC_5V 至 3V3 | `regulator=U2, part number not printed`；`input=VCC_5V`；`output=3V3`；`input_caps=C7 10uF; C8 100nF`；`output_caps=C9 100nF; C10 10uF`；`ground=pin2` |
| 电源 | AGND 与 GND | `analog_ground=AGND`；`digital_ground=GND`；`link=R17 0R`；`analog_loads=U3 analog, P2/P3/P4/P5` |
| 总线 | PCM5102 I2S 输入 | `device=U3 PCM5102APWR`；`data=DIN -> 470R -> pin14`；`bit_clock=BCK -> 470R -> pin13`；`word_clock=LRCK -> 470R -> pin15`；`system_clock=SCK pin12 -> 10K -> GND`；`direction=host-to-DAC` |
| 音频 | PCM5102 电源与电荷泵 | `supply=CPVDD pin1; DVDD pin20; AVDD pin8 -> 3V3`；`charge_pump=CAPP/CAPM with C15/C17 2.2uF`；`negative_rail=VNEG with 2.2uF`；`ldo_cap=C16 100nF`；`digital_caps=C13/C14 100nF` |
| 音频 | PCM5102 配置脚 | `format=FMT pin16 GND`；`mute=XSMT pin17; R8 10K to 3V3; TP2 to GND pad`；`deemphasis=DEMP pin10 via TP1/R13`；`filter=FLT pin11 via TP3/R12` |
| 音频 | PCM5102 左右模拟输出 | `left=U3 OUTL pin6 -> OUTL -> P5 SIG`；`right=U3 OUTR pin7 -> OUTR -> P2 SIG`；`series=R9/R10 470R`；`shunt_caps=C18/C19 2.2nF to AGND`；`connector_ground=AGND` |
| 音频 | 3.5 mm 立体声输出 | `connector=P3`；`right=OUTR via C11 1uF`；`left=OUTL via C12 1uF`；`ground=AGND` |
| 模拟电路 | GPIO25/GPIO26 视频选择 | `switch=S1 SW-PWR`；`option_1=GPIO25 / J3 video pin8`；`option_2=GPIO26 / J3 video pin10`；`common=S1 pin2`；`direction=host DAC-to-video-output` |
| 模拟电路 | 复合视频输出网络 | `source=S1 common`；`optional_filter=R7 DNP; C28 DNP to AGND`；`series=L2 4.7R`；`termination=R5 75R to AGND`；`connector=P4 SIG/G` |
| 接口 | Port C UART | `connector=J1 GROVE 4P`；`io2=RX / GPIO16`；`io1=TX / GPIO17`；`vcc=VCC_5V`；`ground=GND` |
| 接口 | M5-Bus 使用网络 | `video=GPIO25 and GPIO26`；`uart=GPIO16 RX; GPIO17 TX`；`i2s=GPIO13 BCK; GPIO15 DIN; GPIO0 LRCK`；`5v=VCC_5V / bus pin28`；`high_power=12V / HPWR pins25/27/29`；`battery=VBAT/BAT_OUT no-connect` |
| 电源 | DC 9–24 V 与 5 V/3 A 能力 | `document_input=DC9-24V`；`document_output=<5V, 3A`；`schematic_input=12V`；`schematic_current=not shown`；`thermal_conditions=not shown` |
| 音频 | 32 位立体声音频能力 | `document_bit_depth=32-bit`；`document_channels=stereo`；`schematic_bus=DIN/BCK/LRCK`；`sample_rate=not shown`；`clock_frequency=not shown` |
| 模拟电路 | PAL/PAL_M 与 864×576 视频 | `document_standards=PAL/PAL_M`；`document_resolution=up to 864x576`；`schematic_sources=GPIO25/GPIO26`；`termination=75R`；`waveform=not shown` |
| 核心器件 | U2 3.3 V 稳压器型号 | `reference=U2`；`input=VCC_5V`；`output=3V3`；`pins=VIN/VOUT/EN/BYP/GND`；`part_number=null` |

## 待确认事项

- `power.input-range-current`：产品正文声明 DC 9–24 V 输入、5 V 输出小于 3 A；原理图输入网络只标 12V，未印完整输入范围、最大输出电流或热设计条件。（证据：图 3161ea60c428 / 第 1 页 / P1/U1 network labeled 12V without range/current）
- `audio.digital-format`：产品正文称 PCM5102 可输出 32 位立体声音频，但原理图只显示 I2S 连线和 FMT 配置，没有位深、采样率或时钟参数。（证据：图 3161ea60c428 / 第 1 页 / U3 I2S pins and FMT without format timing table）
- `analog.video-standard`：产品正文称可生成 PAL/PAL_M、最高 864×576 的模拟视频，原理图只显示 GPIO25/26 与 75 Ω 输出网络，未记录制式、分辨率或波形参数。（证据：图 3161ea60c428 / 第 1 页 / S1/L2/R5/P4 analog output lacks video timing）
- `component.ldo-identity`：原理图可确认 U2 的 VIN/VOUT/EN/BYP/GND 拓扑及 5 V 到 3.3 V 功能，但页面没有印 U2 型号。（证据：图 3161ea60c428 / 第 1 页 / A4 U2 symbol without part marking）
- `review.input-range-current`：请用 MP1584EN 设计计算、BOM 和热测试复核 DC 9–24 V 输入范围与 5 V/3 A 输出边界。；原因：原理图只标 12V，未给最大电流或热条件。
- `review.digital-format`：请用 PCM5102 数据手册与主机 I2S 配置确认位深、采样率和时钟要求。；原因：原理图不包含数字音频格式参数。
- `review.video-standard`：请用主机视频生成固件与实测波形确认 PAL/PAL_M 及最大 864×576 输出。；原因：视频制式由软件波形决定，原理图只确认模拟输出网络。
- `review.ldo-identity`：请用 BOM 或器件丝印确认 U2 的完整 3.3 V 稳压器型号。；原因：U2 型号未印在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3161ea60c4286cbeaa95c580d5b9f32fafc7864418cc15ebe18b2f72416394dc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/552/SCH_Module_RCA_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/RCA Module 13.2.md`

源文档 SHA-256：`cb9199c6f0271409ea3943b9b4ce2e05763b98bb5fab16d5362ed384204e7e4b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
