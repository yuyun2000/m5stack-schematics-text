# Atomic Audio-3.5 Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Audio-3.5 Base |
| SKU | A166 |
| 产品 ID | `atomic-audio-3-5-base-1cc81796eb02` |
| 源文档 | `zh_CN/atom/Atomic_Audio-3.5_Base.md` |

## 概述

Atomic Audio-3.5 Base 以 ES8311 完成 I2S 数字音频与模拟麦克风/线路信号转换，NS4150B 驱动差分扬声器输出，CN1 提供 3.5mm 音频与插入检测。PI4IOE5V6408ZTAEX 通过 I2C 控制功放使能路径，TPS7A2033PDQNR 将 5V 转为 3.3V，并通过 10Ω/22uF 网络派生 AVDD 模拟电源。第二张资源绘制 LMA3526B381-OAK03 麦克风、MIC_OUT 测试点和电源保护，但 MIC_OUT 到第一页主音频网络的跨页连接未画出。

## 检索关键词

`Atomic Audio-3.5 Base`、`A166`、`ES8311`、`0x18`、`0x19`、`NS4150B`、`PI4IOE5V6408ZTAEX`、`0x43`、`SN74LVC1G126DBVR`、`TPS7A2033PDQNR`、`ME1502AM5G`、`LMA3526B381-OAK03`、`PJ-342`、`MSK12C02`、`I2C`、`I2S`、`SCL`、`SDA`、`SCLK`、`LRCK`、`DSDIN`、`ASDOUT`、`DACP`、`MIC_JACK`、`MIC_P`、`MIC_OUT`、`HP_DET`、`4150_CTRL`、`PW_AMP`、`SPK+`、`SPK-`、`AVDD`、`VDD_MIC`、`3.5mm TRRS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ES8311 | I2S 单声道音频编解码器，连接数字音频、麦克风输入和 DACP 模拟输出 | 图 90ef07f879d5 / 第 1 页 / A1-B2：U2 ES8311、SCL/SDA、I2S、MIC1P/MIC1N、OUTP/OUTN |
| U3 | NS4150B | 5V 单声道差分功率放大器，输出 SPK+ 与 SPK- | 图 90ef07f879d5 / 第 1 页 / B1-C2：U3 NS4150B、INN/INP/CTRL、VoN/VoP |
| U4 | PI4IOE5V6408ZTAEX | I2C 八位 GPIO 扩展器，P0 用于 PW_AMP 功放控制链 | 图 90ef07f879d5 / 第 1 页 / C1-D2：U4 PI4IOE5V6408ZTAEX、SCL/SDA、P0~P7、I2C Addr 0x43 |
| U6A/U6B | SN74LVC1G126DBVR | 带三态使能的逻辑缓冲器，将 4150_CTRL 经 PW_AMP 门控后送至功放 CTRL | 图 90ef07f879d5 / 第 1 页 / C1-D2：U6A 逻辑门、U6B 电源单元、PW_AMP/4150_CTRL 与 U3 CTRL 连线 |
| U7 | TPS7A2033PDQNR | 5V 输入、3.3V 输出的低压差稳压器 | 图 90ef07f879d5 / 第 1 页 / C2-D3：U7 TPS7A2033PDQNR、IN/EN/OUT、C27/C18 |
| U5 | ME1502AM5G | 由 AVDD 生成 VDD_MIC 的高电平使能电源开关 | 图 90ef07f879d5 / 第 1 页 / A3-A4：U5 ME1502AM5G（EN高使能）、VIN=AVDD、VOUT=VDD_MIC、EN=4150_CTRL |
| U1（麦克风页） | LMA3526B381-OAK03 | 独立麦克风页上的模拟麦克风器件，输出 MIC_OUT | 图 0a60f7a14e18 / 第 1 页 / B2-C3：U1 LMA3526B381-OAK03、OUT/VDD/GND |
| CN1 | PJ-342 | 3.5mm 多触点音频插座，连接麦克风、DACP、AGND 与插入检测网络 | 图 90ef07f879d5 / 第 1 页 / B4-C4：CN1 PJ-342 2/3/4/5/6/7 脚及 MIC_JACK、DACP、HP_DET 周边网络 |
| SW1 | MSK12C02 | 麦克风线路选择开关，与 VDD_MIC、MIC_P 和 GND 网络相邻连接 | 图 90ef07f879d5 / 第 1 页 / A4：SW1 MSK12C02 1~5 脚及 VDD_MIC/MIC_P/GND 连线 |
| H1 | SpeakHeader | 两针差分扬声器连接器，H1.1=SPK-、H1.2=SPK+ | 图 90ef07f879d5 / 第 1 页 / B2：H1 SpeakHeader、SPK-/SPK+ |
| J1 | Atom_5P@2.54 | Atom 数字音频连接器，提供 3.3V 和四线 I2S 信号 | 图 90ef07f879d5 / 第 1 页 / D2-D3：J1 Atom_5P@2.54、3.3V/DSDIN/LRCK/ASDOUT/SCLK |
| J2 | Atom_4P@2.54 | Atom I2C 与电源连接器，提供 SCL、SDA、5V、GND | 图 90ef07f879d5 / 第 1 页 / D2：J2 Atom_4P@2.54、SCL/SDA/5V/GND |
| Q1 | 未标注 | 由 HP_DET 控制、下拉 4150_CTRL 的 N 沟道 MOSFET | 图 90ef07f879d5 / 第 1 页 / D4：Q1、HP_DET 栅极、4150_CTRL 漏极、GND 源极 |
| D1（主板页） | 1N4148WT | CN1 插入检测网络中的小信号二极管 | 图 90ef07f879d5 / 第 1 页 / C3-C4：HP_DET、D1 1N4148WT 与 CN1 检测触点 |
| D1（麦克风页） | PESD3V3S1UB | 麦克风页 VDD 对 GND 的瞬态保护器件 | 图 0a60f7a14e18 / 第 1 页 / B3-C3：D1 PESD3V3S1UB 跨接 VDD 与 GND |
| LED1 | 绿色 | VDD_MIC 电源状态指示 LED，串联 R20 1KΩ | 图 90ef07f879d5 / 第 1 页 / A3：GND-LED1（绿色）-R20 1K-VDD_MIC 支路 |

## 系统结构

### Atomic Audio-3.5 Base 音频架构

ES8311 连接 Atom 的 I2S/I2C 总线并输出 DACP，NS4150B 将 DACP 放大为 SPK+/SPK-；CN1 提供 3.5mm 音频接口，第二页另绘制带 MIC_OUT 的麦克风电路。

- 参数与网络：`codec=U2 ES8311`；`amplifier=U3 NS4150B`；`audio_jack=CN1 PJ-342`；`speaker=H1 SPK-/SPK+`；`microphone=U1 LMA3526B381-OAK03`
- 证据：图 90ef07f879d5 / 第 1 页 / A1-D4：U2/U3/CN1/H1 与总线接口; 图 0a60f7a14e18 / 第 1 页 / B2-C3：U1 麦克风与 MIC_OUT

## 电源

### U7 TPS7A2033PDQNR

U7 的 IN 和 EN 接 5V，OUT 产生 3.3V；输入 C27 和输出 C18 均为 22uF。

- 参数与网络：`input=5V`；`enable=5V`；`output=3.3V`；`input_capacitor=C27 22uF/10V`；`output_capacitor=C18 22uF/10V`
- 证据：图 90ef07f879d5 / 第 1 页 / C2-D3：5V-C27-U7 IN/EN、U7 OUT-C18-3.3V

### AVDD 模拟电源

3.3V 经 R23 10Ω 串联形成 AVDD，C4 22uF 对 AGND 去耦；R26 0Ω 将 GND 与 AGND 相连。

- 参数与网络：`source=3.3V`；`series_resistor=R23 10R`；`rail=AVDD`；`decoupling=C4 22uF/10V`；`ground_link=R26 0R, GND-AGND`
- 证据：图 90ef07f879d5 / 第 1 页 / B3-B4 虚线框：3.3V-R23-AVDD、C4、R26 GND/AGND

### VDD_MIC 电源路径

U5 以 AVDD 为 VIN，EN 接 4150_CTRL，VOUT 形成 VDD_MIC；RESET 通过 R8 120KΩ 接 AGND，VDD_MIC 还驱动 LED1/R20 指示支路。

- 参数与网络：`device=U5 ME1502AM5G`；`input=AVDD`；`enable=4150_CTRL`；`output=VDD_MIC`；`reset_bias=R8 120KΩ to AGND`；`indicator=LED1 green + R20 1KΩ`
- 证据：图 90ef07f879d5 / 第 1 页 / A3-A4：U5 VIN/VOUT/EN/RESET、VDD_MIC、LED1/R20

## 接口

### J1 Atom_5P@2.54

J1.1=3.3V，J1.2=DSDIN，J1.3=LRCK，J1.4=ASDOUT，J1.5 经 R4 33Ω 连接 SCLK。

- 参数与网络：`pin_1=3.3V`；`pin_2=DSDIN`；`pin_3=LRCK`；`pin_4=ASDOUT`；`pin_5=SCLK through R4 33R`
- 证据：图 90ef07f879d5 / 第 1 页 / D2-D3：J1 1~5 脚与 R4 33R

### J2 Atom_4P@2.54

J2.1=SCL，J2.2=SDA，J2.3=5V，J2.4=GND。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=5V`；`pin_4=GND`
- 证据：图 90ef07f879d5 / 第 1 页 / D2：J2 1~4 脚网络标注

### CN1 PJ-342

CN1 的图面连接包含 MIC_JACK 经 R27 10KΩ、C14 1uF、R25 10Ω 到插座上部触点，DACP 经 R14 0Ω 到音频触点，AGND 经 R3 1KΩ 到接地触点，并包含与 HP_DET 相连的切换触点。

- 参数与网络：`microphone_path=MIC_JACK-R27 10KΩ-C14 1uF/25V-R25 10Ω-CN1`；`mic_bias=R24 3.3KΩ from AVDD`；`audio_path=DACP-R14 0R-CN1`；`ground_path=AGND-R3 1KΩ-CN1`；`detect=HP_DET through D1 1N4148WT to CN1 switch contact`
- 证据：图 90ef07f879d5 / 第 1 页 / B4-C4：R24/R27/C14/R25、R14、R9、R3、CN1 与 HP_DET/D1

## 总线

### ES8311 I2S

U2.6=SCLK、U2.7=ASDOUT、U2.8=LRCK、U2.9=DSDIN；这些网络由 J1 引出，MCLK 位于 U2.2。

- 参数与网络：`sclk=U2.6 / J1.5 via R4`；`as dout=U2.7 / J1.4`；`lrck=U2.8 / J1.3`；`dsdin=U2.9 / J1.2`；`mclk=U2.2 MCLK`
- 证据：图 90ef07f879d5 / 第 1 页 / A1-B2：U2.2、U2.6~9；D2-D3：J1 I2S 网络

### SCL/SDA 总线

J2 的 SCL/SDA 同名网络连接 U2 ES8311 和 U4 PI4IOE5V6408ZTAEX；U2 侧由 R12/R1 各 4.7KΩ 上拉到 3.3V。

- 参数与网络：`controller_port=J2.1 SCL, J2.2 SDA`；`devices=U2 ES8311; U4 PI4IOE5V6408ZTAEX`；`scl_pullup=R12 4.7KΩ to 3.3V`；`sda_pullup=R1 4.7KΩ to 3.3V`
- 证据：图 90ef07f879d5 / 第 1 页 / A1：U2 SCL/SDA 与 R12/R1；D1-D2：U4/J2 SCL/SDA

## 总线地址

### U2 ES8311

图面注释给出 CE 低电平地址 0x18、CE 高电平地址 0x19；U2.20 CE 接 GND，因此本图配置为 0x18。

- 参数与网络：`ce_low=0x18`；`ce_high=0x19`；`ce_pin=U2.20`；`ce_strap=GND`；`configured_address=0x18`
- 证据：图 90ef07f879d5 / 第 1 页 / A1-A2：文字 ES8311 address: CE pin low - 0x18, CE pin high - 0x19；U2.20 CE 接 GND

### U4 PI4IOE5V6408ZTAEX

原理图在 U4 下方明确标注 I2C Addr: 0x43。

- 参数与网络：`address=0x43`；`bus=SCL/SDA`
- 证据：图 90ef07f879d5 / 第 1 页 / D1：U4 下方蓝字 I2C Addr: 0x43

## GPIO 与控制信号

### PW_AMP / 4150_CTRL

U4.P0 经 R21 0Ω 形成 PW_AMP 并连接 U6A 使能端；4150_CTRL 进入 U6A 数据端，U6A 输出连接 U3 CTRL。

- 参数与网络：`expander_pin=U4.P0 pin12`；`enable_net=PW_AMP through R21 0R`；`data_net=4150_CTRL`；`buffer=U6A SN74LVC1G126DBVR`；`destination=U3.1 CTRL`
- 证据：图 90ef07f879d5 / 第 1 页 / C1-D2：U4.P0-R21-PW_AMP-U6A、4150_CTRL-U6A、U6A 输出到 U3 CTRL

### HP_DET / Q1

HP_DET 由 R13 100KΩ 上拉到 3.3V、C26 4.7uF 对 GND，并通过 D1 1N4148WT 连接 CN1 检测触点；HP_DET 驱动 Q1 栅极，Q1 将 4150_CTRL 下拉到 GND，R19 2KΩ 将 4150_CTRL 上拉到 3.3V。

- 参数与网络：`detect_net=HP_DET`；`pullup=R13 100KΩ to 3.3V`；`filter=C26 4.7uF/25V to GND`；`diode=D1 1N4148WT`；`transistor=Q1`；`controlled_net=4150_CTRL`；`control_pullup=R19 2KΩ to 3.3V`
- 证据：图 90ef07f879d5 / 第 1 页 / C3-D4：R13/C26/HP_DET/D1/CN1 与 R19/Q1/4150_CTRL

## 时钟

### 音频时钟

U2 使用 MCLK、SCLK 和 LRCK 音频时钟网络；SCLK 与 LRCK 由 J1 引出，图中未绘制晶振或有源时钟源。

- 参数与网络：`mclk=U2.2 MCLK`；`sclk=U2.6 SCLK / J1.5 via R4`；`lrck=U2.8 LRCK / J1.3`；`oscillator=none shown`
- 证据：图 90ef07f879d5 / 第 1 页 / A1-B1：U2 MCLK/SCLK/LRCK；D2-D3：J1 SCLK/LRCK；全页无晶振

## 复位

### U4 RESET

U4 RESET 网络由 R11 4.7KΩ 上拉到 3.3V，并由 C23 100nF 对 GND。

- 参数与网络：`reset_pin=U4.10 RESET`；`pullup=R11 4.7KΩ to 3.3V`；`capacitor=C23 100nF/50V to GND`
- 证据：图 90ef07f879d5 / 第 1 页 / D1：U4.10 RESET、R11、C23

## 保护电路

### 麦克风页 VDD

D1 PESD3V3S1UB 跨接麦克风 VDD 与 GND，为该电源节点提供瞬态保护。

- 参数与网络：`device=D1 PESD3V3S1UB`；`protected_net=VDD`；`return=GND`
- 证据：图 0a60f7a14e18 / 第 1 页 / B3-C3：D1 PESD3V3S1UB 接在 VDD 与 GND 之间

## 存储

### 存储器

两张原理图资源中未绘制 Flash、EEPROM、SD 卡或其他独立存储器。

- 参数与网络：`flash=none shown`；`eeprom=none shown`；`sd=none shown`
- 证据：图 90ef07f879d5 / 第 1 页 / 主板全页器件检查：音频、电源、GPIO 扩展和接口，无存储器; 图 0a60f7a14e18 / 第 1 页 / 麦克风页仅 U1、C1/C2、D1、TP1~TP4

## 内存与 Flash

### 易失性存储

两张原理图资源中未绘制独立 RAM 或其他易失性存储器件。

- 参数与网络：`ram=none shown`
- 证据：图 90ef07f879d5 / 第 1 页 / 主板全页器件检查，无 RAM 器件; 图 0a60f7a14e18 / 第 1 页 / 麦克风页全页器件检查，无 RAM 器件

## 音频

### ES8311 麦克风输入

MIC_JACK 经 C2 1uF/25V 耦合到 MIC_P，并进入 U2 的 MIC1P 输入；U2 的 MIC1N、VMID、ADCVREF 和 DACVREF 周围配置 C5/C6/C7/C10 等 1uF 电容到 AGND。

- 参数与网络：`input_net=MIC_JACK`；`coupling=C2 1uF/25V`；`codec_input=U2.18 MIC1P / MIC_P`；`other_analog_pins=U2.17 MIC1N,U2.16 VMID,U2.15 ADCVREF,U2.14 DACVREF`；`capacitors=C5,C6,C7,C10 1uF/25V`
- 证据：图 90ef07f879d5 / 第 1 页 / A2-B3：U2 MIC1P/MIC1N/VMID/ADCVREF/DACVREF 与 C2/C5/C6/C7/C10

### ES8311 DAC 输出

U2.12 OUTP 经 C12 1uF/25V 形成 DACP，U2.13 OUTN 在图中标记未连接。

- 参数与网络：`positive_output=U2.12 OUTP through C12 1uF/25V to DACP`；`negative_output=U2.13 OUTN no-connect`；`supply=U2.11 AVDD`
- 证据：图 90ef07f879d5 / 第 1 页 / B2-B3：U2 OUTN/OUTP/AVDD、C12 与 DACP

### U3 NS4150B 输入级

DACP 经 C17 100nF 和 R7 47KΩ 接 U3.3 INP；AGND 经 C16 100nF 和 R5 47KΩ 接 U3.4 INN；BYPASS 由 C22 1uF 对 AGND 去耦。

- 参数与网络：`positive_input=DACP-C17 100nF-R7 47KΩ-U3.3 INP`；`negative_input=AGND-C16 100nF-R5 47KΩ-U3.4 INN`；`bypass=U3.2-C22 1uF-AGND`
- 证据：图 90ef07f879d5 / 第 1 页 / B1-C2：C16/R5、C17/R7、C22 与 U3 INN/INP/BYPASS

### SPK+/SPK- 差分输出

U3.5 VoN 经 R6 600Ω@100MHz 形成 SPK-，U3.8 VoP 经 R10 600Ω@100MHz 形成 SPK+；H1.1=SPK-、H1.2=SPK+，C11/C24 各 1nF 对 AGND。

- 参数与网络：`negative=U3.5 VoN-R6 600R@100MHz-SPK-/H1.1`；`positive=U3.8 VoP-R10 600R@100MHz-SPK+/H1.2`；`shunt_caps=C11 1nF from SPK- to AGND; C24 1nF from SPK+ to AGND`；`supply=U3.6=5V`
- 证据：图 90ef07f879d5 / 第 1 页 / B2-C3：U3 VoN/VoP、R6/R10、C11/C24、H1

### U1 LMA3526B381-OAK03

第二页 U1 由 VDD 供电，OUT 输出 MIC_OUT；C1 10uF 与 C2 100nF 对 GND 去耦，TP1=VDD、TP2=MIC_OUT、TP3/TP4=GND。

- 参数与网络：`supply=U1.4 VDD`；`output=U1.1 MIC_OUT`；`grounds=U1.2/U1.3/U1.5 to GND`；`bulk_capacitor=C1 10uF`；`decoupling=C2 100nF`；`test_points=TP1 VDD, TP2 MIC_OUT, TP3 GND, TP4 GND`
- 证据：图 0a60f7a14e18 / 第 1 页 / B2-C3：TP1~TP4、U1、C1/C2、VDD/MIC_OUT/GND

## 射频

### 射频电路

两张资源中未绘制天线、射频收发器或射频匹配网络。

- 参数与网络：`antenna=none shown`；`rf_transceiver=none shown`；`matching_network=none shown`
- 证据：图 90ef07f879d5 / 第 1 页 / 主板全页器件检查：仅音频/电源/数字接口; 图 0a60f7a14e18 / 第 1 页 / 麦克风页全页器件检查：无射频网络

## 调试与烧录

### 测试点

主板页在 MIC_P/AGND 附近提供 TP1、TP2、TP3；麦克风页提供 TP1=VDD、TP2=MIC_OUT、TP3/TP4=GND。图中未见专用 JTAG/SWD 接口。

- 参数与网络：`main_sheet=TP1/TP2/TP3 around MIC_P and AGND`；`microphone_sheet=TP1=VDD,TP2=MIC_OUT,TP3=GND,TP4=GND`；`jtag=none shown`；`swd=none shown`
- 证据：图 90ef07f879d5 / 第 1 页 / A3：TP1/TP2/TP3；全页无 JTAG/SWD; 图 0a60f7a14e18 / 第 1 页 / B2-C2：TP1~TP4 网络标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Audio-3.5 Base 音频架构 | `codec=U2 ES8311`；`amplifier=U3 NS4150B`；`audio_jack=CN1 PJ-342`；`speaker=H1 SPK-/SPK+`；`microphone=U1 LMA3526B381-OAK03` |
| 电源 | U7 TPS7A2033PDQNR | `input=5V`；`enable=5V`；`output=3.3V`；`input_capacitor=C27 22uF/10V`；`output_capacitor=C18 22uF/10V` |
| 电源 | AVDD 模拟电源 | `source=3.3V`；`series_resistor=R23 10R`；`rail=AVDD`；`decoupling=C4 22uF/10V`；`ground_link=R26 0R, GND-AGND` |
| 电源 | VDD_MIC 电源路径 | `device=U5 ME1502AM5G`；`input=AVDD`；`enable=4150_CTRL`；`output=VDD_MIC`；`reset_bias=R8 120KΩ to AGND`；`indicator=LED1 green + R20 1KΩ` |
| 接口 | J1 Atom_5P@2.54 | `pin_1=3.3V`；`pin_2=DSDIN`；`pin_3=LRCK`；`pin_4=ASDOUT`；`pin_5=SCLK through R4 33R` |
| 接口 | J2 Atom_4P@2.54 | `pin_1=SCL`；`pin_2=SDA`；`pin_3=5V`；`pin_4=GND` |
| 总线 | ES8311 I2S | `sclk=U2.6 / J1.5 via R4`；`as dout=U2.7 / J1.4`；`lrck=U2.8 / J1.3`；`dsdin=U2.9 / J1.2`；`mclk=U2.2 MCLK` |
| 总线 | SCL/SDA 总线 | `controller_port=J2.1 SCL, J2.2 SDA`；`devices=U2 ES8311; U4 PI4IOE5V6408ZTAEX`；`scl_pullup=R12 4.7KΩ to 3.3V`；`sda_pullup=R1 4.7KΩ to 3.3V` |
| 总线地址 | U2 ES8311 | `ce_low=0x18`；`ce_high=0x19`；`ce_pin=U2.20`；`ce_strap=GND`；`configured_address=0x18` |
| 总线地址 | U4 PI4IOE5V6408ZTAEX | `address=0x43`；`bus=SCL/SDA` |
| 音频 | ES8311 麦克风输入 | `input_net=MIC_JACK`；`coupling=C2 1uF/25V`；`codec_input=U2.18 MIC1P / MIC_P`；`other_analog_pins=U2.17 MIC1N,U2.16 VMID,U2.15 ADCVREF,U2.14 DACVREF`；`capacitors=C5,C6,C7,C10 1uF/25V` |
| 音频 | ES8311 DAC 输出 | `positive_output=U2.12 OUTP through C12 1uF/25V to DACP`；`negative_output=U2.13 OUTN no-connect`；`supply=U2.11 AVDD` |
| 音频 | U3 NS4150B 输入级 | `positive_input=DACP-C17 100nF-R7 47KΩ-U3.3 INP`；`negative_input=AGND-C16 100nF-R5 47KΩ-U3.4 INN`；`bypass=U3.2-C22 1uF-AGND` |
| 音频 | SPK+/SPK- 差分输出 | `negative=U3.5 VoN-R6 600R@100MHz-SPK-/H1.1`；`positive=U3.8 VoP-R10 600R@100MHz-SPK+/H1.2`；`shunt_caps=C11 1nF from SPK- to AGND; C24 1nF from SPK+ to AGND`；`supply=U3.6=5V` |
| GPIO 与控制信号 | PW_AMP / 4150_CTRL | `expander_pin=U4.P0 pin12`；`enable_net=PW_AMP through R21 0R`；`data_net=4150_CTRL`；`buffer=U6A SN74LVC1G126DBVR`；`destination=U3.1 CTRL` |
| GPIO 与控制信号 | HP_DET / Q1 | `detect_net=HP_DET`；`pullup=R13 100KΩ to 3.3V`；`filter=C26 4.7uF/25V to GND`；`diode=D1 1N4148WT`；`transistor=Q1`；`controlled_net=4150_CTRL`；`control_pullup=R19 2KΩ to 3.3V` |
| 接口 | CN1 PJ-342 | `microphone_path=MIC_JACK-R27 10KΩ-C14 1uF/25V-R25 10Ω-CN1`；`mic_bias=R24 3.3KΩ from AVDD`；`audio_path=DACP-R14 0R-CN1`；`ground_path=AGND-R3 1KΩ-CN1`；`detect=HP_DET through D1 1N4148WT to CN1 switch contact` |
| 复位 | U4 RESET | `reset_pin=U4.10 RESET`；`pullup=R11 4.7KΩ to 3.3V`；`capacitor=C23 100nF/50V to GND` |
| 音频 | U1 LMA3526B381-OAK03 | `supply=U1.4 VDD`；`output=U1.1 MIC_OUT`；`grounds=U1.2/U1.3/U1.5 to GND`；`bulk_capacitor=C1 10uF`；`decoupling=C2 100nF`；`test_points=TP1 VDD, TP2 MIC_OUT, TP3 GND, TP4 GND` |
| 保护电路 | 麦克风页 VDD | `device=D1 PESD3V3S1UB`；`protected_net=VDD`；`return=GND` |
| 关键网络 | MIC_OUT 与主板麦克风路径 | `microphone_output=MIC_OUT`；`main_sheet_nets=MIC_JACK,MIC_P,VDD_MIC`；`explicit_cross_page_link=not shown` |
| 时钟 | 音频时钟 | `mclk=U2.2 MCLK`；`sclk=U2.6 SCLK / J1.5 via R4`；`lrck=U2.8 LRCK / J1.3`；`oscillator=none shown` |
| 存储 | 存储器 | `flash=none shown`；`eeprom=none shown`；`sd=none shown` |
| 内存与 Flash | 易失性存储 | `ram=none shown` |
| 调试与烧录 | 测试点 | `main_sheet=TP1/TP2/TP3 around MIC_P and AGND`；`microphone_sheet=TP1=VDD,TP2=MIC_OUT,TP3=GND,TP4=GND`；`jtag=none shown`；`swd=none shown` |
| 射频 | 射频电路 | `antenna=none shown`；`rf_transceiver=none shown`；`matching_network=none shown` |

## 待确认事项

- `key_net.microphone-cross-page`：第二页麦克风输出名为 MIC_OUT，而第一页编解码器/切换电路使用 MIC_JACK、MIC_P 和 VDD_MIC；两页未画出 MIC_OUT 到这些网络的连接或连接器，因此跨页映射无法由现有资源确认。（证据：图 0a60f7a14e18 / 第 1 页 / U1.1 仅标 MIC_OUT，页面无外部连接器或 MIC_JACK/MIC_P/VDD_MIC; 图 90ef07f879d5 / 第 1 页 / 主板页麦克风相关网络标为 MIC_JACK、MIC_P、VDD_MIC，未见 MIC_OUT）
- `review.microphone-cross-page`：请确认第二页 U1 的 MIC_OUT 在装配或 PCB 上如何连接到第一页 SW1、MIC_P 或 MIC_JACK。；原因：现有两页使用不同网络名，且未绘制跨页端口或连接器，无法从原理图闭合板载麦克风信号路径。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `90ef07f879d5f1fa030eeb2a82c7c1dd99931b69161fe89b539f1958c9f6acbc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_SCHE_Atomic_Audio-3.5_page_01.png` |
| 2 | 1 | `0a60f7a14e1837646f093eaa8767a9680695b5268a824fb5a20bb3259a32ab9b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_SCHE_Atomic_Audio-3.5_page_02.png` |

---

源文档：`zh_CN/atom/Atomic_Audio-3.5_Base.md`

源文档 SHA-256：`4942ee2a94f0c059a24232e2394b4f15dad2909a66aa545873cb21118027da19`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
