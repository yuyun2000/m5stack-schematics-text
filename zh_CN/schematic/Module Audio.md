# Module Audio 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Audio |
| SKU | M144 |
| 产品 ID | `module-audio-156e2a4470b4` |
| 源文档 | `zh_CN/module/Module-Audio.md` |

## 概述

Module Audio 以 U7 ES8388 完成 I2S 音频编解码，以 U2 STM32G030F6P6 管理耳机检测、接口模式和三颗 WS2812C_2020，并与主机共享 I2C 总线。J1 为麦克风输入链路，J2 提供 HPOUT_L/HPOUT_R、麦克风与检测连接，U6 FSUSB42MUX 在 HP_MODE_SET 控制下交换复合插孔的两条触点网络。S1 在 M5-Bus G0/G19 之间切换 I2S_MCLK 与 I2S_SCLK，板上从 SYS_3.3V 经 3.3 Ω 隔离形成 AUDIO_VDD，并分离 GND/AGND。

## 检索关键词

`Module Audio`、`M144`、`ES8388`、`STM32G030F6P6`、`FSUSB42MUX`、`WS2812C_2020`、`PJ-342B`、`I2S`、`I2C`、`0x10`、`0x33`、`I2S_MCLK`、`I2S_SCLK`、`I2S_LRCK`、`I2S_MAIN_DOUT`、`I2S_MAIN_DIN`、`HPOUT_L`、`HPOUT_R`、`MIC_MONO_IN`、`LIN_MIC_PIN`、`LIN_MIC_PU_EN`、`HP_MODE_SET`、`HP_DET`、`HP_P1`、`HP_P2`、`CTIA`、`OMTP`、`TRS`、`TRRS`、`LED_DAT`、`SYS_3.3V`、`AUDIO_VDD`、`AGND`、`SWDIO`、`SWCLK`、`SYS_RST`、`M5_BUS_Core2`、`GPIO0`、`GPIO19`、`GPIO34`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7 | ES8388 | 立体声音频编解码器，连接 I2S、I2C、四路模拟输入与左右耳机输出 | 图 65f7a4066400 / 第 1 页 / C3-D4 U7 ES8388 pins0-28 |
| U2 | STM32G030F6P6 | 板载控制 MCU，管理 I2C、耳机检测、模式选择、麦克风偏置使能、RGB 与 SWD | 图 65f7a4066400 / 第 1 页 / C1-D2 U2 STM32G030F6P6 pins1-20 |
| U6 | FSUSB42MUX | 由 HP_MODE_SET 控制的双通道模拟开关，交换 HP_P1/HP_P2 与麦克风/地触点路径 | 图 65f7a4066400 / 第 1 页 / B2-B3 U6 FSUSB42MUX pins1-10 |
| U4/U3/U5 | WS2812C_2020 | 三颗串联的 3.3 V 可编程 RGB 状态灯 | 图 65f7a4066400 / 第 1 页 / A1-A2 U4/U3/U5 WS2812C_2020 |
| J1 | PJ-342B | 连接 CODEC_RIN1/CODEC_LIN1 的 3.5 mm 麦克风输入插孔 | 图 65f7a4066400 / 第 1 页 / A4 J1 PJ-342B、AGND/LIN_MIC_PIN/MIC_MONO_IN |
| J2 | PJ-342B | 连接左右耳机输出、麦克风复合触点和 HP_DET 的 3.5 mm 插孔 | 图 65f7a4066400 / 第 1 页 / B4 J2 PJ-342B、HPOUT_R/HPOUT_L/HP_DET/HP_P1/HP_P2 |
| S1 | MK-22D14-G020 | 在 G0/G19 两组 M5-Bus 网络之间切换 I2S_MCLK 与 I2S_SCLK | 图 65f7a4066400 / 第 1 页 / B2 S1 MK-22D14-G020、G0/G19/I2S_MCLK/I2S_SCLK |
| BUS1 | M5_BUS_Core2 | 30 针主机接口，提供 3.3 V/5 V、I2C、I2S 与复位网络 | 图 65f7a4066400 / 第 1 页 / A1-B2 BUS1 M5_BUS_Core2 pins1-30 |
| J3 | CON5 | STM32 的 3.3 V、SWCLK、SWDIO、SYS_RST 与 GND 调试接口 | 图 65f7a4066400 / 第 1 页 / C1 J3 CON5 pins1-5 |
| Q1/Q2 | CJ3401 / 2NMOS | 由 LIN_MIC_PU_EN 控制的麦克风偏置开关网络 | 图 65f7a4066400 / 第 1 页 / A2-A3 Q1 CJ3401、Q2 2NMOS、R10/R12/R16 |
| C15/C16 | 220uF/6.3V | ES8388 ROUT1/LOUT1 到 HPOUT_R/HPOUT_L 的串联输出耦合电容 | 图 65f7a4066400 / 第 1 页 / C3-D3 U7 ROUT1/LOUT1 与 C15/C16 |
| R3/C6/C8/R4 | 3R3/1% / 100nF/50V / 220uF/6.3V / 0R | SYS_3.3V 到 AUDIO_VDD 的隔离去耦及 GND-AGND 单点连接网络 | 图 65f7a4066400 / 第 1 页 / B1-C2 SYS_3.3V/R3/AUDIO_VDD/C6/C8 与 R4 GND-AGND |
| LED1/R17 | LED_GREEN / 22K/1% | SYS_3.3V 电源绿色指示灯 | 图 65f7a4066400 / 第 1 页 / D1 LED1 LED_GREEN、R17 22K/1% |

## 系统结构

### Module Audio 系统架构

U7 ES8388 负责 I2S/I2C 音频编解码，U2 STM32G030F6P6 负责插孔检测、模式控制与 RGB；U6 FSUSB42MUX 切换复合插孔触点，BUS1 提供主机电源、I2C、I2S 与复位。

- 参数与网络：`codec=U7 ES8388`；`controller=U2 STM32G030F6P6`；`audio_mux=U6 FSUSB42MUX`；`host=BUS1 M5_BUS_Core2`；`jacks=J1/J2 PJ-342B`；`rgb=U4/U3/U5 WS2812C_2020`；`debug=J3 SWD`
- 证据：图 65f7a4066400 / 第 1 页 / 整页 BUS1/U2/U6/U7/J1/J2/RGB 分区

## 核心器件

### 三颗 WS2812C_2020

U2 LED_DAT 进入 U4 DIN，U4 DOUT 级联 U3 DIN，U3 DOUT 级联 U5 DIN；三颗灯均由 SYS_3.3V 供电并各有 100 nF 去耦。

- 参数与网络：`count=3`；`part_number=WS2812C_2020`；`data=LED_DAT -> U4 -> U3 -> U5`；`supply=SYS_3.3V`；`decoupling=C? 100nF/50V per LED`；`data_pulldown=R1 5.1K/1% to GND`
- 证据：图 65f7a4066400 / 第 1 页 / A1-A2 U4/U3/U5 RGB chain and R1

## 电源

### SYS_3.3V、SYS_5V 与 AUDIO_VDD

BUS1 pin12 提供 SYS_3.3V，pin28 提供 SYS_5V；SYS_3.3V 经 R3 3.3 Ω/1% 形成 AUDIO_VDD，C6 100 nF 与 C8 220 uF 对 AUDIO_VDD 去耦。

- 参数与网络：`3v3_source=BUS1 pin12 SYS_3.3V`；`5v_source=BUS1 pin28 SYS_5V`；`audio_series=R3 3R3/1%`；`audio_rail=AUDIO_VDD`；`audio_caps=C6 100nF/50V; C8 220uF/6.3V`
- 证据：图 65f7a4066400 / 第 1 页 / B1 BUS1 pins12/28；B1-C2 R3/C6/C8/AUDIO_VDD

### ES8388 供电与参考去耦

U7 DVDD pin2、PVDD pin3、AVDD pin17 与 HPVDD pin16 接 AUDIO_VDD；DGND pin4、AGND pin18 与 EP_GND 接 AGND，并配置 C10/C11、C22/C23 及 VREF/VMID/ADCVREF 电容。

- 参数与网络：`supply_pins=DVDD2; PVDD3; AVDD17; HPVDD16 -> AUDIO_VDD`；`grounds=DGND4; AGND18; EP_GND0 -> AGND`；`digital_caps=C10 10uF/50V; C11 100nF/50V`；`analog_caps=C22 100nF/50V; C23 10uF/10V`；`references=VREF C12 4.7uF/10V; VMID C20 4.7uF/10V; ADCVREF C21 4.7uF/10V`
- 证据：图 65f7a4066400 / 第 1 页 / C3-D4 U7 power/reference pins and C10-C12/C20-C23

### 数字地与模拟地

数字 GND 与音频 AGND 作为独立网络绘制，并由 R4 0 Ω 单点连接；音频插孔、U6 和 U7 模拟部分使用 AGND。

- 参数与网络：`digital_ground=GND`；`analog_ground=AGND`；`link=R4 0R`；`analog_loads=U6, U7 analog grounds, J1/J2 audio ground`
- 证据：图 65f7a4066400 / 第 1 页 / C1-C2 R4 GND-to-AGND；右半页 AGND symbols

## 接口

### M5-Bus 已用网络

BUS1 使用 pins1/3/5 GND、pin6 SYS_RST、pin12 SYS_3.3V、pin17 BUS_SDA、pin18 BUS_SCL、pin21 I2S_LRCK、pin22 G19、pin23 I2S_MAIN_DOUT、pin24 G0、pin26 I2S_MAIN_DIN 与 pin28 SYS_5V。

- 参数与网络：`ground=pins1/3/5`；`reset=pin6 G25/DAC SYS_RST`；`3v3=pin12 SYS_3.3V`；`i2c=pin17 G21 BUS_SDA; pin18 G22 BUS_SCL`；`i2s=pin21 G27 LRCK; pin23 G2 DOUT; pin26 G34 DIN; pins22/24 G19/G0 clocks via S1`；`5v=pin28 SYS_5V`
- 证据：图 65f7a4066400 / 第 1 页 / A1-B2 BUS1 M5_BUS_Core2 pins1-30

## 总线

### ES8388 I2S 数字音频

U7 MCLK pin1 接 I2S_MCLK，SCLK pin5 接 I2S_SCLK，DSDIN pin6 接 I2S_MAIN_DOUT，LRCK pin7 接 I2S_LRCK，ASDOUT pin8 接 I2S_MAIN_DIN。

- 参数与网络：`codec=U7 ES8388`；`mclk=pin1 I2S_MCLK`；`bit_clock=pin5 I2S_SCLK`；`host_to_codec=I2S_MAIN_DOUT -> DSDIN pin6`；`frame_clock=I2S_LRCK -> pin7`；`codec_to_host=ASDOUT pin8 -> I2S_MAIN_DIN`
- 证据：图 65f7a4066400 / 第 1 页 / C3 U7 pins1/5/6/7/8 I2S labels

### I2S 到 M5-Bus 映射

BUS1 pin21/G27 接 I2S_LRCK，pin23/G2 接 I2S_MAIN_DOUT，pin26/G34/ADC 接 I2S_MAIN_DIN；I2S_MCLK 与 I2S_SCLK 由 S1 在 G0/pin24 与 G19/pin22 之间切换。

- 参数与网络：`lrck=BUS1 pin21 G27`；`data_out=BUS1 pin23 G2`；`data_in=BUS1 pin26 G34/ADC`；`clock_candidates=BUS1 pin24 G0; BUS1 pin22 G19`；`clock_switch=S1 MK-22D14-G020`
- 证据：图 65f7a4066400 / 第 1 页 / B1-B2 BUS1 pins21-26；B2 S1 G0/G19/I2S clocks

### 共享 I2C 控制总线

BUS1 pin17/G21/SYS_SDA 与 pin18/G22/SYS_SCL 形成 BUS_SDA/BUS_SCL，同时连接 U7 CDATA pin27/CCLK pin28 和 U2 PA12/PA11。

- 参数与网络：`controller=host via BUS1`；`sda=BUS1 pin17 G21 -> BUS_SDA -> U7 CDATA pin27; U2 PA12 pin17`；`scl=BUS1 pin18 G22 -> BUS_SCL -> U7 CCLK pin28; U2 PA11 pin16`；`devices=U7 ES8388; U2 STM32G030F6P6`；`level=SYS_3.3V domain`
- 证据：图 65f7a4066400 / 第 1 页 / B1 BUS1 pins17/18；C1-D2 U2 PA12/PA11；C4 U7 pins27/28

## GPIO 与控制信号

### MCLK/SCLK 机械切换拓扑

S1 的公共端连接 I2S_MCLK 与 I2S_SCLK，两侧连接 G0 和 G19 交叉网络，使两个时钟可按开关位置交换到 BUS1 的 GPIO0/GPIO19。

- 参数与网络：`switch=S1 MK-22D14-G020`；`common=I2S_MCLK and I2S_SCLK`；`host_nets=G0 and G19`；`bus_pins=G0 pin24; G19 pin22`；`function=clock route selection`
- 证据：图 65f7a4066400 / 第 1 页 / B2 S1 pins1-6 and four net labels

### STM32 控制网络

U2 PA7 连接 LED_DAT，PA2 连接 HP_MODE_SET，PA1 连接 HP_DET，PB7/PB8 侧连接 LIN_MIC_PU_EN，PA12/PA11 连接 I2C。

- 参数与网络：`rgb=PA7 pin14 LED_DAT`；`headset_mode=PA2 pin8 HP_MODE_SET`；`headset_detect=PA1 pin7 HP_DET`；`mic_bias_enable=PB7/PB8 side pin1 LIN_MIC_PU_EN`；`i2c=PA12 pin17 BUS_SDA; PA11 pin16 BUS_SCL`
- 证据：图 65f7a4066400 / 第 1 页 / C1-D2 U2 STM32G030F6P6 signal labels

## 复位

### STM32 系统复位

BUS1 pin6/G25/DAC 的 SYS_RST 连接 U2 NRST pin6 和 J3 pin4；NRST 配置 C2 100 nF/50 V 对地。

- 参数与网络：`host=BUS1 pin6 G25/DAC`；`net=SYS_RST`；`target=U2 NRST pin6`；`debug=J3 pin4`；`capacitor=C2 100nF/50V to GND`
- 证据：图 65f7a4066400 / 第 1 页 / A1 BUS1 pin6；C1 J3 pin4；D1 U2 NRST/C2

## 音频

### ES8388 模拟输入

U7 LIN1 pin24、RIN1 pin23、LIN2 pin22、RIN2 pin21 分别连接 CODEC_LIN1、CODEC_RIN1、CODEC_LIN2、CODEC_RIN2，前端通过 100 nF 耦合电容和 22 kΩ/3.3 kΩ 电阻接入插孔与 U6。

- 参数与网络：`lin1=U7 pin24 CODEC_LIN1`；`rin1=U7 pin23 CODEC_RIN1`；`lin2=U7 pin22 CODEC_LIN2`；`rin2=U7 pin21 CODEC_RIN2`；`coupling=C9/C13/C14 and related 100nF capacitors`；`input_resistors=R6/R8/R9 and related 3.3K/22K`
- 证据：图 65f7a4066400 / 第 1 页 / A3-B3 codec input network；C4 U7 pins21-24

### J1 麦克风输入链路

J1 的 MIC_MONO_IN 与 LIN_MIC_PIN 经 R9/R8 22 kΩ 和 C14/C13 100 nF 分别接 CODEC_LIN1/CODEC_RIN1，插孔地触点接 AGND。

- 参数与网络：`connector=J1 PJ-342B`；`path_1=MIC_MONO_IN -> R9 22K/1% -> C14 100nF/50V -> CODEC_LIN1`；`path_2=LIN_MIC_PIN -> R8 22K/1% -> C13 100nF/50V -> CODEC_RIN1`；`ground=AGND`
- 证据：图 65f7a4066400 / 第 1 页 / A3-A4 J1/R8/R9/C13/C14/CODEC_LIN1/RIN1

### 麦克风偏置使能

LIN_MIC_PU_EN 经 R10 5.1 kΩ 控制 Q2，Q2 与 Q1 CJ3401、R12 22 kΩ、R16 3.3 kΩ 构成从 AUDIO_VDD 向 LIN_MIC_PIN 提供可控偏置的开关网络。

- 参数与网络：`control=LIN_MIC_PU_EN`；`gate_resistor=R10 5.1K/1%`；`transistors=Q2 2NMOS; Q1 CJ3401`；`bias_source=AUDIO_VDD`；`output=LIN_MIC_PIN via R16 3.3K/1%`；`bias_resistor=R12 22K/1%`
- 证据：图 65f7a4066400 / 第 1 页 / A2-A3 Q1/Q2/R10/R12/R16/LIN_MIC_PIN

### 立体声耳机输出

U7 ROUT1 pin11 经 C15 220 uF/6.3 V 形成 HPOUT_R，LOUT1 pin12 经 C16 220 uF/6.3 V 形成 HPOUT_L；两路再分别经 R18/R21 22 Ω 接 J2。

- 参数与网络：`right=U7 ROUT1 pin11 -> C15 220uF/6.3V -> HPOUT_R -> R18 22R/1% -> J2`；`left=U7 LOUT1 pin12 -> C16 220uF/6.3V -> HPOUT_L -> R21 22R/1% -> J2`；`direction=codec-to-headphone`；`other_outputs=ROUT2/LOUT2 not externally connected on page`
- 证据：图 65f7a4066400 / 第 1 页 / B4 J2/R18/R21；C3-D3 U7 ROUT1/LOUT1/C15/C16

### 耳机插拔检测

J2 的开关触点通过 R19 100 kΩ 与 R20 10 kΩ 连接 HP_DET，HP_DET 返回 U2 PA1；HPOUT_R/HPOUT_L 另由 R11/R13 5.1 kΩ 下拉到 AGND。

- 参数与网络：`connector=J2`；`detect_net=HP_DET`；`mcu=U2 PA1 pin7`；`detect_resistors=R19 100K/1%; R20 10K/1%`；`output_pulldowns=R11/R13 5.1K/1% to AGND`
- 证据：图 65f7a4066400 / 第 1 页 / B3-B4 HP_DET/R19/R20/J2/R11/R13；C1 U2 PA1

### 复合插孔触点切换

U6 FSUSB42MUX 的 D+/D- 输出为 HP_P1/HP_P2，HSD1+/HSD2+ 与 HSD1-/HSD2- 分别连接 MIC_MONO_IN 和 AGND 两组路径；HP_MODE_SET 控制选择，OE# 由 R7 5.1 kΩ 下拉。

- 参数与网络：`mux=U6 FSUSB42MUX`；`outputs=D+ pin3 HP_P1; D- pin4 HP_P2`；`inputs=HSD1+/HSD2+ and HSD1-/HSD2- between MIC_MONO_IN/AGND`；`select=HP_MODE_SET`；`enable=OE# pin10 via R7 5.1K/1% to AGND`；`supply=AUDIO_VDD`
- 证据：图 65f7a4066400 / 第 1 页 / B2-B3 U6/R6/C9/R7/HP_MODE_SET/HP_P1/HP_P2

## 调试与烧录

### STM32 SWD 接口

J3 CON5 pin1 为 SYS_3.3V、pin2 SWCLK、pin3 SWDIO、pin4 SYS_RST、pin5 GND；SWCLK/SWDIO 分别连接 U2 PA14/PA13。

- 参数与网络：`connector=J3 CON5`；`pin1=SYS_3.3V`；`pin2=SWCLK -> U2 PA14 pin19`；`pin3=SWDIO -> U2 PA13 pin18`；`pin4=SYS_RST`；`pin5=GND`
- 证据：图 65f7a4066400 / 第 1 页 / C1 J3 pins1-5；C2 U2 PA14/PA13

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Audio 系统架构 | `codec=U7 ES8388`；`controller=U2 STM32G030F6P6`；`audio_mux=U6 FSUSB42MUX`；`host=BUS1 M5_BUS_Core2`；`jacks=J1/J2 PJ-342B`；`rgb=U4/U3/U5 WS2812C_2020`；`debug=J3 SWD` |
| 电源 | SYS_3.3V、SYS_5V 与 AUDIO_VDD | `3v3_source=BUS1 pin12 SYS_3.3V`；`5v_source=BUS1 pin28 SYS_5V`；`audio_series=R3 3R3/1%`；`audio_rail=AUDIO_VDD`；`audio_caps=C6 100nF/50V; C8 220uF/6.3V` |
| 电源 | ES8388 供电与参考去耦 | `supply_pins=DVDD2; PVDD3; AVDD17; HPVDD16 -> AUDIO_VDD`；`grounds=DGND4; AGND18; EP_GND0 -> AGND`；`digital_caps=C10 10uF/50V; C11 100nF/50V`；`analog_caps=C22 100nF/50V; C23 10uF/10V`；`references=VREF C12 4.7uF/10V; VMID C20 4.7uF/10V; ADCVREF C21 4.7uF/10V` |
| 电源 | 数字地与模拟地 | `digital_ground=GND`；`analog_ground=AGND`；`link=R4 0R`；`analog_loads=U6, U7 analog grounds, J1/J2 audio ground` |
| 总线 | ES8388 I2S 数字音频 | `codec=U7 ES8388`；`mclk=pin1 I2S_MCLK`；`bit_clock=pin5 I2S_SCLK`；`host_to_codec=I2S_MAIN_DOUT -> DSDIN pin6`；`frame_clock=I2S_LRCK -> pin7`；`codec_to_host=ASDOUT pin8 -> I2S_MAIN_DIN` |
| 总线 | I2S 到 M5-Bus 映射 | `lrck=BUS1 pin21 G27`；`data_out=BUS1 pin23 G2`；`data_in=BUS1 pin26 G34/ADC`；`clock_candidates=BUS1 pin24 G0; BUS1 pin22 G19`；`clock_switch=S1 MK-22D14-G020` |
| GPIO 与控制信号 | MCLK/SCLK 机械切换拓扑 | `switch=S1 MK-22D14-G020`；`common=I2S_MCLK and I2S_SCLK`；`host_nets=G0 and G19`；`bus_pins=G0 pin24; G19 pin22`；`function=clock route selection` |
| 总线 | 共享 I2C 控制总线 | `controller=host via BUS1`；`sda=BUS1 pin17 G21 -> BUS_SDA -> U7 CDATA pin27; U2 PA12 pin17`；`scl=BUS1 pin18 G22 -> BUS_SCL -> U7 CCLK pin28; U2 PA11 pin16`；`devices=U7 ES8388; U2 STM32G030F6P6`；`level=SYS_3.3V domain` |
| GPIO 与控制信号 | STM32 控制网络 | `rgb=PA7 pin14 LED_DAT`；`headset_mode=PA2 pin8 HP_MODE_SET`；`headset_detect=PA1 pin7 HP_DET`；`mic_bias_enable=PB7/PB8 side pin1 LIN_MIC_PU_EN`；`i2c=PA12 pin17 BUS_SDA; PA11 pin16 BUS_SCL` |
| 复位 | STM32 系统复位 | `host=BUS1 pin6 G25/DAC`；`net=SYS_RST`；`target=U2 NRST pin6`；`debug=J3 pin4`；`capacitor=C2 100nF/50V to GND` |
| 调试与烧录 | STM32 SWD 接口 | `connector=J3 CON5`；`pin1=SYS_3.3V`；`pin2=SWCLK -> U2 PA14 pin19`；`pin3=SWDIO -> U2 PA13 pin18`；`pin4=SYS_RST`；`pin5=GND` |
| 核心器件 | 三颗 WS2812C_2020 | `count=3`；`part_number=WS2812C_2020`；`data=LED_DAT -> U4 -> U3 -> U5`；`supply=SYS_3.3V`；`decoupling=C? 100nF/50V per LED`；`data_pulldown=R1 5.1K/1% to GND` |
| 音频 | ES8388 模拟输入 | `lin1=U7 pin24 CODEC_LIN1`；`rin1=U7 pin23 CODEC_RIN1`；`lin2=U7 pin22 CODEC_LIN2`；`rin2=U7 pin21 CODEC_RIN2`；`coupling=C9/C13/C14 and related 100nF capacitors`；`input_resistors=R6/R8/R9 and related 3.3K/22K` |
| 音频 | J1 麦克风输入链路 | `connector=J1 PJ-342B`；`path_1=MIC_MONO_IN -> R9 22K/1% -> C14 100nF/50V -> CODEC_LIN1`；`path_2=LIN_MIC_PIN -> R8 22K/1% -> C13 100nF/50V -> CODEC_RIN1`；`ground=AGND` |
| 音频 | 麦克风偏置使能 | `control=LIN_MIC_PU_EN`；`gate_resistor=R10 5.1K/1%`；`transistors=Q2 2NMOS; Q1 CJ3401`；`bias_source=AUDIO_VDD`；`output=LIN_MIC_PIN via R16 3.3K/1%`；`bias_resistor=R12 22K/1%` |
| 音频 | 立体声耳机输出 | `right=U7 ROUT1 pin11 -> C15 220uF/6.3V -> HPOUT_R -> R18 22R/1% -> J2`；`left=U7 LOUT1 pin12 -> C16 220uF/6.3V -> HPOUT_L -> R21 22R/1% -> J2`；`direction=codec-to-headphone`；`other_outputs=ROUT2/LOUT2 not externally connected on page` |
| 音频 | 耳机插拔检测 | `connector=J2`；`detect_net=HP_DET`；`mcu=U2 PA1 pin7`；`detect_resistors=R19 100K/1%; R20 10K/1%`；`output_pulldowns=R11/R13 5.1K/1% to AGND` |
| 音频 | 复合插孔触点切换 | `mux=U6 FSUSB42MUX`；`outputs=D+ pin3 HP_P1; D- pin4 HP_P2`；`inputs=HSD1+/HSD2+ and HSD1-/HSD2- between MIC_MONO_IN/AGND`；`select=HP_MODE_SET`；`enable=OE# pin10 via R7 5.1K/1% to AGND`；`supply=AUDIO_VDD` |
| 接口 | M5-Bus 已用网络 | `ground=pins1/3/5`；`reset=pin6 G25/DAC SYS_RST`；`3v3=pin12 SYS_3.3V`；`i2c=pin17 G21 BUS_SDA; pin18 G22 BUS_SCL`；`i2s=pin21 G27 LRCK; pin23 G2 DOUT; pin26 G34 DIN; pins22/24 G19/G0 clocks via S1`；`5v=pin28 SYS_5V` |
| 总线地址 | STM32 与 ES8388 I2C 地址 | `document_stm32=0x33`；`document_es8388=0x10`；`schematic_bus=BUS_SDA/BUS_SCL`；`schematic_numeric_address=not printed` |
| 音频 | TRS 与 TRRS 插孔类型 | `document_j1=TRS microphone input`；`document_j2=TRRS microphone and stereo output`；`schematic_j1=PJ-342B mic paths`；`schematic_j2=PJ-342B headphone/mic/detect paths` |
| 音频 | CTIA/OMTP 模式语义 | `control=HP_MODE_SET`；`mux=U6 FSUSB42MUX`；`switched_nets=HP_P1/HP_P2 between MIC_MONO_IN and AGND`；`mode_0=not labeled`；`mode_1=not labeled`；`document_modes=CTIA/OMTP` |
| 音频 | 音频性能与工作电流 | `document_working=3.3V@23.53mA`；`document_standby=3.3V@8.58mA`；`document_quality=high fidelity`；`schematic_measurement=not shown`；`load_condition=not shown` |

## 待确认事项

- `address.i2c-claims`：产品正文声明 STM32G030F6P6 为 0x33、ES8388 为 0x10；原理图显示二者共享 BUS_SDA/BUS_SCL，但没有打印数值地址或 STM32 固件地址配置。（证据：图 65f7a4066400 / 第 1 页 / U2 PA12/PA11 and U7 CDATA/CCLK without address labels）
- `audio.jack-types`：产品正文称 J1 为仅麦克风输入的 TRS、J2 为麦克风加立体声输出的 TRRS；原理图可确认两者功能网络，但两只器件都标为 PJ-342B，未直接打印 TRS/TRRS 名称。（证据：图 65f7a4066400 / 第 1 页 / A4 J1 PJ-342B and B4 J2 PJ-342B）
- `audio.ctia-omtp`：原理图确认 HP_MODE_SET 控制 U6 交换 HP_P1/HP_P2 的麦克风与地路径，但页面未把两个逻辑状态分别标为 CTIA 或 OMTP。（证据：图 65f7a4066400 / 第 1 页 / B2-B3 U6 FSUSB42MUX/HP_MODE_SET lacks CTIA/OMTP labels）
- `audio.performance-power`：产品正文称高保真音频并给出 3.3 V 工作 23.53 mA、待机 8.58 mA，但原理图没有音频性能指标、负载条件或电流测量数据。（证据：图 65f7a4066400 / 第 1 页 / SYS_3.3V/AUDIO_VDD power network lacks performance/current annotations）
- `review.i2c-addresses`：请用 STM32 内置固件协议与 ES8388 地址配置复核 0x33 和 0x10。；原因：原理图仅显示共享 I2C 网络，没有打印数值地址。
- `review.jack-types`：请用 J1/J2 BOM 型号、装配图或实物确认 J1 的 TRS 与 J2 的 TRRS 机械触点规格。；原因：两只插孔在原理图中均标 PJ-342B，未直接写 TRS/TRRS。
- `review.ctia-omtp`：请用 STM32 固件寄存器定义或实测确认 HP_MODE_SET 两个状态分别对应 CTIA 还是 OMTP。；原因：原理图只显示换向拓扑，没有模式名称与逻辑真值表。
- `review.performance-power`：请按明确耳机负载、采样配置与固件状态复核音频性能及工作/待机电流。；原因：原理图未提供性能指标和电流测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `65f7a4066400e7d04efedbd4778755b01fdaa6164474a0fa5fb6a97554ac66ec` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_sch_moduleaudio_v10_page_01.png` |

---

源文档：`zh_CN/module/Module-Audio.md`

源文档 SHA-256：`c0cc28cdb54bac9fcfbde5ddef65b1fc8ea696fa82516b1032b1a7dc8297e9a6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
