# Unit Synth 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Synth |
| SKU | U178 |
| 产品 ID | `unit-synth-ae301994d0ec` |
| 源文档 | `zh_CN/unit/Unit-Synth.md` |

## 概述

Unit Synth 以 U4 SAM2695 为音频合成核心，J1 将 5V_IN、DGND 和单向 SYS_MIDI 输入引入，SYS_MIDI 经上拉、指示 LED 和 R2 后进入 U4 MIDI_IN。U4 的 AOUTL/AOUTR 经 C11/C12 和 R11/R12 汇合为 AMP_IN，U2 NS4150B 将该信号放大后通过 FB2/FB3 差分输出到 J2。U1 ME6211A33M3G-N 由 5V_IN 生成 DVDD，DVDD 经 FB1 隔离为 AVDD；U3 CN809R 产生 SYS_RST，X1 与 C5/C6 构成 U4 外部时钟网络。本页未包含 MCU、外部存储、I2C/SPI/CAN/USB、射频、传感器、电池或充电电路。

## 检索关键词

`Unit Synth`、`U178`、`SAM2695`、`NS4150B`、`ME6211A33M3G-N`、`CN809R`、`MIDI`、`SYS_MIDI`、`MIDI_IN`、`UART_RX`、`AOUTL`、`AOUTR`、`SYN_L`、`SYN_R`、`AMP_IN`、`VOP`、`VON`、`5V_IN`、`DVDD`、`AVDD`、`DGND`、`AGND`、`SYS_RST`、`X1`、`J1`、`J2`、`FB1 BLM15PD121SN1D`、`FB2 BLM15PD121SN1D`、`FB3 BLM15PD121SN1D`、`audio synthesizer`、`class-D amplifier`、`speaker output`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | SAM2695 | 音频合成核心，接收 SYS_MIDI，输出 AOUTL/AOUTR，并连接外部时钟、复位与电源网络 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 C2-D3，U4 SAM2695 pins1-48，MIDI_IN/AOUTL/AOUTR/X1/X2/RSTA/PD#/VD33/VA33 |
| U2 | NS4150B | 由 5V_IN 供电的音频功率放大器，将 AMP_IN 放大为 VOP/VON 差分扬声器输出 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B3-B4，U2 NS4150B，INP/INN/CTRL/BYPASS/VOP/VON/VCC/GND |
| U1 | ME6211A33M3G-N | 将 5V_IN 转换为 DVDD 的三引脚稳压器 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B1，U1 ME6211A33M3G-N，VIN pin3、OUT pin2、GND pin1 |
| U3 | CN809R | DVDD 供电的复位监控器，RST 输出形成 SYS_RST | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 C2-D2，U3 CN809R，VIN pin3、RST pin2、GND pin1 |
| X1 | TXM12M000 系列字样（完整后缀待确认） | 连接 U4 X1/X2 的外部晶体，与 C5/C6 负载电容构成时钟网络 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 D2，X1 型号字样、U4 pin39 X1/pin40 X2 与 C5/C6 20pF/50V |
| J1 | 4P connector | 外部 Grove 类输入接口，引出 SYS_MIDI、5V_IN、DGND，pin4 未连接 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 A1，J1 pins1-4，pin3 SYS_MIDI、pin2 5V_IN、pin1 DGND、pin4 无网络 |
| J2 | 1.25mm 2P 卧贴 | NS4150B VOP/VON 经磁珠后的两针差分扬声器输出连接器，外壳 SH 接 DGND | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B4，J2 pins1-2/SH 与 FB2/FB3/DGND |
| FB1,FB2,FB3 | BLM15PD121SN1D | FB1 隔离 DVDD/AVDD，FB2/FB3 串联在功放差分输出与 J2 之间 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B1/B4，FB1 DVDD-AVDD 与 FB2/FB3 VOP/VON-J2 |
| LED2,LED3 | 未标注 | LED2 位于 SYS_MIDI 活动网络，LED3 位于 DVDD 电源指示支路 | 图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 A2/C2，LED3-R10 与 LED2-R9/R6/SYS_MIDI |

## 系统结构

### Unit Synth 系统架构

J1 输入 5V_IN、DGND 和 SYS_MIDI；U1 生成 DVDD，FB1 形成 AVDD，U3 生成 SYS_RST，X1 为 U4 SAM2695 提供外部时钟。U4 左右声道输出混合为 AMP_IN，经 U2 NS4150B 放大后送 J2 扬声器接口。

- 参数与网络：`synthesizer=U4 SAM2695`；`amplifier=U2 NS4150B`；`regulator=U1 ME6211A33M3G-N`；`reset_monitor=U3 CN809R`；`input=J1 SYS_MIDI/5V_IN/DGND`；`output=J2 differential speaker`；`power=5V_IN -> DVDD -> AVDD`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 本页未包含的子系统

该页未显示独立 MCU/协处理器、I2C、SPI、CAN、RS-485、USB、SDIO、MIPI、I2S、射频、传感器、电池、充电或外部调试接口。

- 参数与网络：`mcu=null`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`usb=null`；`i2s=null`；`rf=null`；`sensor=null`；`battery=null`；`charger=null`；`debug=null`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页完整原理图，仅含电源、SAM2695、复位/时钟、音频放大、LED 与连接器

## 核心器件

### DVDD 电源指示

DVDD 经 R10 10K/1% 与 LED3 串联到 DGND，构成电源指示支路。

- 参数与网络：`path=DVDD -> R10 10K/1% -> LED3 -> DGND`；`reference=LED3`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 A2，DVDD/R10/LED3/DGND

## 电源

### 5V_IN 至 DVDD 稳压

5V_IN 经 R1 4.7R/1% 接 U1 VIN pin3，U1 OUT pin2 输出 DVDD、GND pin1 接 DGND；C1 10uF/10V 位于输入侧，C2 10uF/10V 位于 DVDD 输出侧。

- 参数与网络：`input=5V_IN via R1 4.7R/1%`；`regulator=U1 ME6211A33M3G-N`；`vin=pin3`；`output=pin2 DVDD`；`ground=pin1 DGND`；`input_cap=C1 10uF/10V`；`output_cap=C2 10uF/10V`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B1，5V_IN/R1/U1/C1/C2/DVDD

### 数字与模拟电源/地分区

DVDD 经 FB1 BLM15PD121SN1D 形成 AVDD；AVDD 侧配置 C7 10uF/10V，R8 0R 将 DGND 与 AGND 连接。U4 数字电源 pins8/11/20/31/35/41/46 接 DVDD，VA33 pin6 接 AVDD。

- 参数与网络：`digital_supply=DVDD`；`analog_supply=DVDD -> FB1 BLM15PD121SN1D -> AVDD`；`analog_cap=C7 10uF/10V`；`ground_link=R8 0R DGND-AGND`；`sam_digital_pins=8,11,20,31,35,41,46`；`sam_analog_pin=6 VA33`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B1-C3，FB1/C7/R8 与 U4 VD33/VA33 电源引脚

### NS4150B 5V_IN 供电

U2 VCC pin6 接 5V_IN、GND pin7 接 DGND；C9 10uF/16V 与 C10 220uF/6.3V 从 5V_IN 接 DGND。

- 参数与网络：`amplifier=U2 NS4150B`；`supply=pin6 VCC=5V_IN`；`ground=pin7 GND=DGND`；`decoupling=C9 10uF/16V,C10 220uF/6.3V`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B3-B4，U2 VCC/GND 与 C9/C10/5V_IN/DGND

## 接口

### J1 四针接口

J1 pin1 接 DGND、pin2 接 5V_IN、pin3 接 SYS_MIDI、pin4 未连接；SYS_MIDI 相对本单元为进入 U4 MIDI_IN 的输入信号。

- 参数与网络：`reference=J1`；`pin1=DGND`；`pin2=5V_IN power input`；`pin3=SYS_MIDI input`；`pin4=NC`；`direction=host to Unit Synth`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 A1，J1 pin1-pin4 与 SYS_MIDI/5V_IN/DGND

### J2 差分扬声器输出

U2 VOP pin8 与 VON pin5 分别经 FB2/FB3 BLM15PD121SN1D 连接 J2 pins1/2，J2 屏蔽端 SH 接 DGND；输出端未接地，为两线差分输出。

- 参数与网络：`connector=J2 1.25mm 2P`；`pin1=U2 VOP via FB2`；`pin2=U2 VON via FB3`；`shield=SH=DGND`；`topology=differential two-wire`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B3-B4，U2 VOP/VON、FB2/FB3 与 J2 pin1/pin2/SH

## 总线

### SYS_MIDI 串行输入路径

J1 pin3 的 SYS_MIDI 经 R2 1K/1% 进入 U4 MIDI_IN pin16；R6 2.2K/1% 将 SYS_MIDI 上拉到 DVDD，LED2 与 R9 1K/1% 也连接在 DVDD 与 SYS_MIDI 之间。

- 参数与网络：`source=J1 pin3 SYS_MIDI`；`destination=U4 pin16 MIDI_IN`；`series_resistor=R2 1K/1%`；`pullup=R6 2.2K/1% to DVDD`；`indicator=DVDD -> LED2 -> R9 1K/1% -> SYS_MIDI`；`direction=input`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 A1-C2，J1 SYS_MIDI 与 R2/R6/R9/LED2/U4 pin16

## GPIO 与控制信号

### SAM2695 并行接口与模式绑带

U4 D0-D7 pins24/26/27/28/29/30/32/33 与 IRQ pin42 在本页未连接；WR# pin12 接 DVDD，CS# pin14、RD# pin15 与 A0 pin10 接 DGND。

- 参数与网络：`data_bus=D0-D7 unconnected`；`irq=pin42 unconnected`；`wr=pin12 WR#=DVDD`；`cs=pin14 CS#=DGND`；`rd=pin15 RD#=DGND`；`a0=pin10 A0=DGND`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 C2-D2，U4 左侧 D0-D7/IRQ/WR#/CS#/RD#/A0 引脚

## 时钟

### SAM2695 外部晶体网络

X1 跨接 U4 X1 pin39 与 X2 pin40，C5/C6 各 20pF/50V 从两端接 DGND；本页型号字样以 TXM12M000 开头，但没有独立打印频率值。

- 参数与网络：`controller=U4 SAM2695`；`pins=pin39 X1,pin40 X2`；`crystal_reference=X1`；`visible_prefix=TXM12M000`；`load_caps=C5/C6 20pF/50V`；`printed_frequency=null`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 D2，X1、C5/C6 与 U4 pins39/40

## 复位

### SAM2695 复位路径

U3 CN809R 的 VIN pin3 接 DVDD、GND pin1 接 DGND，RST pin2 输出 SYS_RST；SYS_RST 连接 U4 RSTA/PD# pin38，并经 R3 5.1K/1% 连接 U2 CTRL pin1。

- 参数与网络：`monitor=U3 CN809R`；`supply=DVDD`；`reset_net=SYS_RST`；`synth_reset=U4 pin38 RSTA/PD#`；`amplifier_control=SYS_RST -> R3 5.1K/1% -> U2 pin1 CTRL`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B3-D2，U3 SYS_RST 至 U4 pin38 与 U2 CTRL

## 保护电路

### 接口与音频输出保护/滤波

J2 两路功放输出分别串联 FB2/FB3 磁珠，5V_IN 进入 U1 前串联 R1 4.7R/1%；J1 与 J2 路径未显示 TVS、专用 ESD 阵列、保险丝或反接保护器件。

- 参数与网络：`speaker_filter=FB2/FB3 BLM15PD121SN1D`；`power_series=R1 4.7R/1%`；`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页 J1/5V_IN/U1 与 U2/FB2/FB3/J2 全路径，无专用保护符号

## 内存与 Flash

### 外部存储器

本页未显示独立 Flash、EEPROM、SRAM、SD 卡或其他存储器件，U4 的内部存储结构也未在板级原理图展开。

- 参数与网络：`external_flash=null`；`eeprom=null`；`external_sram=null`；`sd_card=null`；`sam_internal_memory=null`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页完整器件区，无存储器或存储连接器

## 音频

### SAM2695 左右声道输出与混合

U4 AOUTL pin1 经 C11 4.7uF/10V 形成 SYN_L，再经 R11 1K/1% 接 AMP_IN；AOUTR pin2 经 C12 4.7uF/10V 形成 SYN_R，再经 R12 1K/1% 接同一 AMP_IN，R14 5.1K/1% 将 AMP_IN 接 AGND。

- 参数与网络：`left=U4 pin1 AOUTL -> C11 4.7uF/10V -> SYN_L -> R11 1K/1% -> AMP_IN`；`right=U4 pin2 AOUTR -> C12 4.7uF/10V -> SYN_R -> R12 1K/1% -> AMP_IN`；`bias=R14 5.1K/1% AMP_IN-AGND`；`mix=SYN_L and SYN_R summed at AMP_IN`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 C2-C3，U4 AOUTL/AOUTR、C11/C12、SYN_L/SYN_R、R11/R12/R14、AMP_IN

### NS4150B 输入与控制

AMP_IN 经 C3 100nF/50V 接 U2 INP pin3；AGND 经 C4 100nF/50V 与 R4 30K/1% 接 INN pin4，R5 30K/1% 位于 INN/输出反馈网络；SYS_RST 经 R3 5.1K/1% 控制 U2 CTRL pin1。

- 参数与网络：`positive_input=AMP_IN -> C3 100nF/50V -> pin3 INP`；`negative_input=AGND -> C4 100nF/50V -> R4 30K/1% -> pin4 INN`；`feedback=R5 30K/1%`；`control=SYS_RST -> R3 5.1K/1% -> pin1 CTRL`；`bypass=pin2 BYPASS with C8/C9 network`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 B3，U2 pins1-4 与 C3/C4/R3-R5/AMP_IN/SYS_RST

## 模拟电路

### SAM2695 模拟参考去耦

U4 VA33 pin6 接 AVDD 并由 C19 4.7uF/10V 对 AGND去耦，VCM pin5 由 C20 4.7uF/10V 对 AGND去耦，AGND pin4 接 AGND。

- 参数与网络：`analog_supply=pin6 VA33=AVDD`；`supply_cap=C19 4.7uF/10V`；`common_mode=pin5 VCM`；`vcm_cap=C20 4.7uF/10V`；`ground=pin4 AGND`
- 证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 C3，U4 pins4-6 与 C19/C20/AVDD/AGND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Synth 系统架构 | `synthesizer=U4 SAM2695`；`amplifier=U2 NS4150B`；`regulator=U1 ME6211A33M3G-N`；`reset_monitor=U3 CN809R`；`input=J1 SYS_MIDI/5V_IN/DGND`；`output=J2 differential speaker`；`power=5V_IN -> DVDD -> AVDD` |
| 接口 | J1 四针接口 | `reference=J1`；`pin1=DGND`；`pin2=5V_IN power input`；`pin3=SYS_MIDI input`；`pin4=NC`；`direction=host to Unit Synth` |
| 电源 | 5V_IN 至 DVDD 稳压 | `input=5V_IN via R1 4.7R/1%`；`regulator=U1 ME6211A33M3G-N`；`vin=pin3`；`output=pin2 DVDD`；`ground=pin1 DGND`；`input_cap=C1 10uF/10V`；`output_cap=C2 10uF/10V` |
| 电源 | 数字与模拟电源/地分区 | `digital_supply=DVDD`；`analog_supply=DVDD -> FB1 BLM15PD121SN1D -> AVDD`；`analog_cap=C7 10uF/10V`；`ground_link=R8 0R DGND-AGND`；`sam_digital_pins=8,11,20,31,35,41,46`；`sam_analog_pin=6 VA33` |
| 总线 | SYS_MIDI 串行输入路径 | `source=J1 pin3 SYS_MIDI`；`destination=U4 pin16 MIDI_IN`；`series_resistor=R2 1K/1%`；`pullup=R6 2.2K/1% to DVDD`；`indicator=DVDD -> LED2 -> R9 1K/1% -> SYS_MIDI`；`direction=input` |
| GPIO 与控制信号 | SAM2695 并行接口与模式绑带 | `data_bus=D0-D7 unconnected`；`irq=pin42 unconnected`；`wr=pin12 WR#=DVDD`；`cs=pin14 CS#=DGND`；`rd=pin15 RD#=DGND`；`a0=pin10 A0=DGND` |
| 复位 | SAM2695 复位路径 | `monitor=U3 CN809R`；`supply=DVDD`；`reset_net=SYS_RST`；`synth_reset=U4 pin38 RSTA/PD#`；`amplifier_control=SYS_RST -> R3 5.1K/1% -> U2 pin1 CTRL` |
| 时钟 | SAM2695 外部晶体网络 | `controller=U4 SAM2695`；`pins=pin39 X1,pin40 X2`；`crystal_reference=X1`；`visible_prefix=TXM12M000`；`load_caps=C5/C6 20pF/50V`；`printed_frequency=null` |
| 音频 | SAM2695 左右声道输出与混合 | `left=U4 pin1 AOUTL -> C11 4.7uF/10V -> SYN_L -> R11 1K/1% -> AMP_IN`；`right=U4 pin2 AOUTR -> C12 4.7uF/10V -> SYN_R -> R12 1K/1% -> AMP_IN`；`bias=R14 5.1K/1% AMP_IN-AGND`；`mix=SYN_L and SYN_R summed at AMP_IN` |
| 模拟电路 | SAM2695 模拟参考去耦 | `analog_supply=pin6 VA33=AVDD`；`supply_cap=C19 4.7uF/10V`；`common_mode=pin5 VCM`；`vcm_cap=C20 4.7uF/10V`；`ground=pin4 AGND` |
| 音频 | NS4150B 输入与控制 | `positive_input=AMP_IN -> C3 100nF/50V -> pin3 INP`；`negative_input=AGND -> C4 100nF/50V -> R4 30K/1% -> pin4 INN`；`feedback=R5 30K/1%`；`control=SYS_RST -> R3 5.1K/1% -> pin1 CTRL`；`bypass=pin2 BYPASS with C8/C9 network` |
| 电源 | NS4150B 5V_IN 供电 | `amplifier=U2 NS4150B`；`supply=pin6 VCC=5V_IN`；`ground=pin7 GND=DGND`；`decoupling=C9 10uF/16V,C10 220uF/6.3V` |
| 接口 | J2 差分扬声器输出 | `connector=J2 1.25mm 2P`；`pin1=U2 VOP via FB2`；`pin2=U2 VON via FB3`；`shield=SH=DGND`；`topology=differential two-wire` |
| 核心器件 | DVDD 电源指示 | `path=DVDD -> R10 10K/1% -> LED3 -> DGND`；`reference=LED3` |
| 保护电路 | 接口与音频输出保护/滤波 | `speaker_filter=FB2/FB3 BLM15PD121SN1D`；`power_series=R1 4.7R/1%`；`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null` |
| 内存与 Flash | 外部存储器 | `external_flash=null`；`eeprom=null`；`external_sram=null`；`sd_card=null`；`sam_internal_memory=null` |
| 系统结构 | 本页未包含的子系统 | `mcu=null`；`i2c=null`；`spi=null`；`can=null`；`rs485=null`；`usb=null`；`i2s=null`；`rf=null`；`sensor=null`；`battery=null`；`charger=null`；`debug=null` |
| 音频 | 正文 MIDI 合成与音效能力 | `documented_protocol=MIDI`；`documented_features=multi-channel instruments,audio synthesis,mixing,4-band EQ,reverb`；`channel_count=null`；`polyphony=null`；`sound_set=null`；`effect_parameters=null` |
| 总线 | MIDI 串口电气与协议参数 | `documented_signal=UART_RX / MIDI`；`schematic_net=SYS_MIDI`；`baud_rate=null`；`logic_thresholds=null`；`frame_format=null`；`isolation=null`；`din_adapter=null` |
| 音频 | 正文扬声器规格 | `documented_impedance=8 ohm`；`documented_power=1W`；`connector=J2`；`speaker_reference=null`；`frequency_response=null` |
| 音频 | NS4150B 功放性能边界 | `amplifier=U2 NS4150B`；`supply=5V_IN`；`output=VOP/VON`；`output_power=null`；`load_range=null`；`gain=null`；`efficiency=null`；`thd=null`；`thermal_limit=null` |
| 时钟 | X1 准确频率与规格 | `reference=X1`；`visible_prefix=TXM12M000`；`frequency=null`；`tolerance=null`；`specified_load_capacitance=null`；`esr=null`；`full_part_number=null` |
| 其他事实 | 正文工作温度 | `documented_working_temperature=0-40C`；`schematic_temperature_rating=null` |

## 待确认事项

- `audio.documented-synthesis-features`：正文称支持标准 MIDI、多通道乐器音源、音频合成/混音、四段 EQ 和混响；原理图只确认 SYS_MIDI 输入、SAM2695 型号和模拟音频输出，未标协议版本、通道数、音色、复音数或 DSP 参数。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页 U4 SAM2695 与 SYS_MIDI/AOUTL/AOUTR，图中无功能参数）
- `bus.documented-midi-uart`：正文将 J1 pin3 描述为 UART_RX 并称接收标准 MIDI；原理图只标 SYS_MIDI 至 U4 MIDI_IN，未给 UART 波特率、逻辑门限、帧格式、隔离方式或 5P-DIN 到 Grove 的适配电路。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页 J1 pin3 SYS_MIDI、R2/R6/LED2 与 U4 MIDI_IN，无串口参数或 DIN 接口）
- `audio.documented-speaker-rating`：正文标称扬声器为 8Ω@1W；原理图只显示 J2 两针差分输出，没有扬声器位号、阻抗、额定功率、频响或声学参数。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页 U2/FB2/FB3/J2 输出路径，无扬声器规格）
- `audio.amplifier-performance`：原理图确认 U2 NS4150B、5V_IN 供电与差分输出连接，但未标输出功率、负载范围、增益、效率、失真、热限制或关断逻辑电平。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页 U2 NS4150B 及外围，无性能数值）
- `clock.crystal-frequency`：X1 型号字样以 TXM12M000 开头，但本页未独立打印频率、容差、负载电容规格或 ESR，完整料号后缀也不够清晰。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页网格 D2，X1 型号字样及 C5/C6 20pF/50V）
- `other.documented-temperature`：正文给出工作温度 0 至 40°C；原理图未标整机或各器件温度等级和验证条件。（证据：图 dcc7377f05d2 / 第 1 页 / 第 1 页完整原理图，无温度规格）
- `review.synthesis-features`：请用 SAM2695 datasheet、固件和测试确认 MIDI 版本、通道数、音色/复音数、四段 EQ、混响及混音参数。；原因：板级连线不能证明合成器内部功能与参数。
- `review.midi-uart`：请确认 SYS_MIDI/UART_RX 的波特率、逻辑电平、帧格式以及 MIDI 5P-DIN 到 J1 的适配和隔离要求。；原因：原理图只有数字输入网络，没有协议或外部 DIN 接口。
- `review.speaker-rating`：请用扬声器 BOM 或实物确认 8Ω@1W、极性、频响和允许连续功率。；原因：原理图只显示 J2 差分输出。
- `review.amplifier-performance`：请用 NS4150B datasheet 和整机测试确认 5V_IN 下的输出功率、负载、增益、THD、效率、热边界及 CTRL 门限。；原因：板级原理图未列功放性能值。
- `review.crystal-frequency`：请用 BOM 或高清源文件确认 X1 完整料号、准确频率、容差、负载电容与 ESR。；原因：当前页面仅能稳定辨认 TXM12M000 前缀，未单列频率。
- `review.temperature`：请确认 0 至 40°C 是工作、性能保证还是建议使用范围，并给出验证条件。；原因：原理图未给温度等级。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dcc7377f05d2d6eed3a1d62edb831b0d45281d2bff0699b969252150fa903ada` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/630/Sch_Unit_Synth_V1.1_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-Synth.md`

源文档 SHA-256：`61972ddc9ffcc1fc89e7f2aec9b92bd042f4d0b2e5caa25e296d51c1518c49db`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
