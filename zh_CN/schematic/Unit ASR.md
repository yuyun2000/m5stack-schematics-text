# Unit ASR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ASR |
| SKU | U194 |
| 产品 ID | `unit-asr-a8e654b97ac6` |
| 源文档 | `zh_CN/unit/Unit ASR.md` |

## 概述

Unit ASR 以 CI-03T1/2（M1）离线语音模组为核心，J1 Grove 口通过 TXD/RXD 网络连接模组 PB5/TX 与 PB6/RX。J1 输入的 5V 经 D1（1N5819）串联后形成模组 VCC_5V，模组 3V3 引脚为红色状态 LED 支路供电。MK1 模拟麦克风直接连接 MIC1+/MIC1-，P1 两针接口直接引出 SPK+/SPK-，其余多组模组 GPIO/麦克风脚未连接。

## 检索关键词

`Unit ASR`、`U194`、`CI-03T1/2`、`CI-03T`、`M1`、`UART`、`TXD`、`RXD`、`PB5/TX`、`PB6/RX`、`115200`、`8N1`、`GROVE`、`J1`、`VCC_5V`、`3V3`、`1V1`、`MIC1+`、`MIC1-`、`MK1`、`GM16027P-2C320DB`、`SPK+`、`SPK-`、`P1`、`1N5819`、`D1`、`RED LED`、`D4`、`R8 2K`、`AEC`、`42 commands`、`300 commands`、`8Ω@0.8W`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | CI-03T1/2 | 离线语音处理模组，连接 UART、模拟麦克风、扬声器和多路电源 | 图 2eb72cde9a1d / 第 1 页 / B2-C3：M1 标注 CI-03T1/2，1~22 脚含 VCC_5V/GND/3V3/1V1/PA/PB/PC/MIC/SPK |
| J1 | GROVE | TXD、RXD、5V、GND 外部 UART 与供电接口 | 图 2eb72cde9a1d / 第 1 页 / B2：J1 GROVE 四脚，IO2/TXD、IO1/RXD、5V、GND |
| MK1 | GM16027P-2C320DB | 连接 M1 MIC1+/MIC1- 的模拟麦克风 | 图 2eb72cde9a1d / 第 1 页 / C2：MK1 标注 GM16027P-2C320DB，pin1 MIC1+、pin2 MIC1- |
| P1 | SPK | M1 SPK+/SPK- 的两针扬声器接口 | 图 2eb72cde9a1d / 第 1 页 / B3-C3：P1 标注 SPK，pin1 SPK+、pin2 SPK- |
| D1 | 1N5819 | J1 5V 到 M1 VCC_5V 的串联肖特基二极管 | 图 2eb72cde9a1d / 第 1 页 / B2-C2：5V-D1(1N5819)-M1.VCC_5V.1 串联路径 |
| D4 | RED LED | M1 3V3 电源状态指示 LED | 图 2eb72cde9a1d / 第 1 页 / A2-B3：3V3-R8(2K)-D4(RED LED)-GND 支路 |
| C1, C4 | 22uF | M1 VCC_5V 与 J1 5V 输入的大容量去耦 | 图 2eb72cde9a1d / 第 1 页 / B2-C2：C4 22uF 跨接 J1 5V/GND，C1 22uF 跨接 D1 后 VCC_5V/GND |
| C5, C6 | 100nF / 22uF | J1 5V 高频去耦与 M1 3V3 输出去耦 | 图 2eb72cde9a1d / 第 1 页 / B2-C2：C5 100nF 跨接 5V/GND，C6 22uF 跨接 M1.3 3V3/GND |

## 系统结构

### Unit ASR

M1 CI-03T1/2 通过 J1 TXD/RXD 与外部主机通信，连接 MK1 模拟麦克风和 P1 SPK± 扬声器接口，并由 5V 输入供电。

- 参数与网络：`voice_module=M1 CI-03T1/2`；`host_interface=J1 UART TXD/RXD`；`microphone=MK1 GM16027P-2C320DB`；`speaker_interface=P1 SPK+/SPK-`；`input_power=5V`
- 证据：图 2eb72cde9a1d / 第 1 页 / B2-C3：J1、M1、MK1、P1 与电源/信号连接

## 电源

### J1 5V

J1 输入 5V 由 C4（22uF）和 C5（100nF）对地去耦，并经 D1（1N5819）串联后连接 M1.VCC_5V.1；D1 后由 C1（22uF）去耦。

- 参数与网络：`input=J1 5V`；`input_caps=C4 22uF, C5 100nF`；`series_diode=D1 1N5819`；`module_rail=VCC_5V / M1.1`；`module_cap=C1 22uF`
- 证据：图 2eb72cde9a1d / 第 1 页 / B2-C2：J1 5V/C4/C5-D1-M1.VCC_5V/C1 电源路径

### M1 3V3 与 D4

M1.3 的 3V3 网络由 C6（22uF）对地去耦，并经 R8（2K）和 D4（RED LED）串联至 GND。

- 参数与网络：`source=M1.3 3V3`；`decoupling=C6 22uF`；`indicator_resistor=R8 2K`；`indicator=D4 RED LED`；`return=GND`
- 证据：图 2eb72cde9a1d / 第 1 页 / A2-C2：M1.3 3V3、C6、R8、D4 与 GND

## 接口

### J1

J1.IO2 接 TXD，IO1 接 RXD，5V 脚接输入 5V，GND 脚接地。

- 参数与网络：`connector=GROVE`；`pin_io2=TXD`；`pin_io1=RXD`；`power=5V`；`ground=GND`；`signal_type=UART`
- 证据：图 2eb72cde9a1d / 第 1 页 / B2：J1 GROVE 的 IO2/IO1/5V/GND 标注与 TXD/RXD 网络

## 总线

### J1 与 M1 UART

J1 的 TXD 网络连接 M1.PB5/TX.18（CI-03T_TXD），J1 的 RXD 网络连接 M1.PB6/RX.19（CI-03T_RXD）。

- 参数与网络：`TXD=J1 IO2 -> CI-03T_TXD -> M1.18 PB5/TX`；`RXD=J1 IO1 -> CI-03T_RXD -> M1.19 PB6/RX`；`series_components=none shown`
- 证据：图 2eb72cde9a1d / 第 1 页 / B2-C3：J1 TXD/RXD 与 M1.18/M1.19 的同名 CI-03T_TXD/CI-03T_RXD 网络

## GPIO 与控制信号

### M1 未用引脚

M1.4 1V1、M1.5 PA1、M1.6 PA0、M1.7 PC4、M1.10~13（B1/B2/M2+/M2-）、M1.14 PA2、M1.15 PA3、M1.16 PA5、M1.17 PA4 和 M1.20 GND 未接外部功能网络。

- 参数与网络：`unused_left=pins 4-7`；`unused_bottom=pins 10-13`；`unused_right=pins 14-17 and pin20`；`used_audio=pins 8/9 and 21/22`；`used_uart=pins 18/19`
- 证据：图 2eb72cde9a1d / 第 1 页 / B2-C3：M1 各短线/未连接标记与实际连接的 UART/MIC/SPK 对比

## 保护电路

### J1 5V 与外部接口

电源路径包含 D1（1N5819）串联二极管；本页未显示 J1 TXD/RXD 的 TVS/ESD、电源保险丝或其他接口保护器件。

- 参数与网络：`power_series_diode=D1 1N5819`；`uart_tvs_esd=none shown`；`fuse=none shown`；`additional_input_protection=none shown`
- 证据：图 2eb72cde9a1d / 第 1 页 / 全页：J1 到 M1 的 UART/电源路径，仅电源含 D1

## 音频

### MK1 模拟麦克风

MK1.1 接 MIC1+ 并连接 M1.M1+.9，MK1.2 接 MIC1- 并连接 M1.M1-.8；中间没有可见外部放大器、偏置或滤波器。

- 参数与网络：`microphone=MK1 GM16027P-2C320DB`；`positive=MK1.1 MIC1+ -> M1.9 M1+`；`negative=MK1.2 MIC1- -> M1.8 M1-`；`external_amplifier=none shown`
- 证据：图 2eb72cde9a1d / 第 1 页 / C2：MK1 pin1/2 与 M1.8/M1.9 的 MIC1-/MIC1+ 直接连线

### P1 扬声器接口

M1.SPK+.22 直接连接 P1.1，M1.SPK-.21 直接连接 P1.2，原理图未显示外部功放或串联器件。

- 参数与网络：`positive=M1.22 SPK+ -> P1.1`；`negative=M1.21 SPK- -> P1.2`；`external_amplifier=none shown`；`connector=P1 SPK`
- 证据：图 2eb72cde9a1d / 第 1 页 / B3-C3：M1.21/M1.22 至 P1.2/P1.1 的 SPK-/SPK+ 直接连线

## 其他事实

### 模组外围实现

本页未显示 M1 的外部晶体、复位开关、启动脚、Flash/存储器或独立调试连接器。

- 参数与网络：`external_clock=none shown`；`reset_switch=none shown`；`boot_control=none shown`；`external_memory=none shown`；`debug_connector=none shown`
- 证据：图 2eb72cde9a1d / 第 1 页 / 完整单页仅含 M1/J1/MK1/P1、D1/D4、R8 和去耦电容

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ASR | `voice_module=M1 CI-03T1/2`；`host_interface=J1 UART TXD/RXD`；`microphone=MK1 GM16027P-2C320DB`；`speaker_interface=P1 SPK+/SPK-`；`input_power=5V` |
| 接口 | J1 | `connector=GROVE`；`pin_io2=TXD`；`pin_io1=RXD`；`power=5V`；`ground=GND`；`signal_type=UART` |
| 总线 | J1 与 M1 UART | `TXD=J1 IO2 -> CI-03T_TXD -> M1.18 PB5/TX`；`RXD=J1 IO1 -> CI-03T_RXD -> M1.19 PB6/RX`；`series_components=none shown` |
| 总线 | UART 帧格式 | `documented_baud=115200`；`documented_format=8N1`；`schematic_settings=未标注` |
| 音频 | MK1 模拟麦克风 | `microphone=MK1 GM16027P-2C320DB`；`positive=MK1.1 MIC1+ -> M1.9 M1+`；`negative=MK1.2 MIC1- -> M1.8 M1-`；`external_amplifier=none shown` |
| 音频 | P1 扬声器接口 | `positive=M1.22 SPK+ -> P1.1`；`negative=M1.21 SPK- -> P1.2`；`external_amplifier=none shown`；`connector=P1 SPK` |
| 音频 | 扬声器规格 | `documented_speaker=8Ω@0.8W cavity speaker`；`schematic_speaker=P1 connector only`；`impedance_power=未标注` |
| 电源 | J1 5V | `input=J1 5V`；`input_caps=C4 22uF, C5 100nF`；`series_diode=D1 1N5819`；`module_rail=VCC_5V / M1.1`；`module_cap=C1 22uF` |
| 电源 | M1 3V3 与 D4 | `source=M1.3 3V3`；`decoupling=C6 22uF`；`indicator_resistor=R8 2K`；`indicator=D4 RED LED`；`return=GND` |
| GPIO 与控制信号 | M1 未用引脚 | `unused_left=pins 4-7`；`unused_bottom=pins 10-13`；`unused_right=pins 14-17 and pin20`；`used_audio=pins 8/9 and 21/22`；`used_uart=pins 18/19` |
| 其他事实 | 离线语音固件能力 | `documented_aec=true`；`documented_factory_commands=42`；`documented_max_commands=300`；`documented_features=voiceprint, enhancement, detection, interruption`；`schematic_evidence=none` |
| 电源 | Unit ASR 功耗 | `documented_standby=5V / 47.73mA`；`documented_active=5V / 250.12mA`；`schematic_current=未标注` |
| 保护电路 | J1 5V 与外部接口 | `power_series_diode=D1 1N5819`；`uart_tvs_esd=none shown`；`fuse=none shown`；`additional_input_protection=none shown` |
| 其他事实 | 模组外围实现 | `external_clock=none shown`；`reset_switch=none shown`；`boot_control=none shown`；`external_memory=none shown`；`debug_connector=none shown` |

## 待确认事项

- `bus.uart-settings-unconfirmed`：产品正文称默认 UART 为 115200@8N1，但原理图仅显示 TXD/RXD 连线，没有波特率、数据位、校验位或停止位配置。（证据：图 2eb72cde9a1d / 第 1 页 / J1 TXD/RXD 到 M1 PB5/PB6 的硬件连线，无串口参数）
- `audio.speaker-rating-unconfirmed`：正文称内置腔体喇叭为 8Ω@0.8W；原理图只显示 P1 SPK 接口，没有扬声器器件、阻抗或功率标注。（证据：图 2eb72cde9a1d / 第 1 页 / B3-C3：P1 仅标 SPK，连接 M1 SPK±）
- `other.voice-capabilities-unconfirmed`：正文声称支持 AEC、声纹/语音增强/打断、42 条出厂命令和最多 300 条自定义命令；这些固件能力未在原理图中标注。（证据：图 2eb72cde9a1d / 第 1 页 / 全页仅显示 CI-03T1/2 模组电气接口，没有固件版本或算法参数）
- `power.current-consumption-unconfirmed`：正文称 5V 待机电流 47.73mA、工作电流 250.12mA；原理图没有电流、功耗、保险丝或限流参数。（证据：图 2eb72cde9a1d / 第 1 页 / J1 5V-D1-M1 VCC_5V 电源路径，无电流额定文字）
- `review.uart-settings`：量产固件的默认 UART 是否为 115200 baud、8N1，是否支持其他配置？；原因：硬件图只确认 TXD/RXD 连接，串口参数由固件决定，需要协议文档或串口实测。
- `review.speaker-rating`：P1 连接的量产腔体扬声器是否为 8Ω@0.8W，极性和允许功率为何？；原因：原理图只有 SPK± 接口，没有扬声器器件或额定参数，需 BOM/实物确认。
- `review.voice-firmware`：当前量产固件是否包含 42 条命令、支持 300 条自定义词和正文所列 AEC/打断/声纹能力？；原因：这些能力依赖 CI-03T 固件和模型版本，原理图不能证明。
- `review.current-consumption`：Unit ASR 在量产固件、扬声器音量和供电条件下的待机/工作电流是否为 47.73mA/250.12mA？；原因：原理图没有电流标注，工作电流取决于模组状态和音频负载，需要实测。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2eb72cde9a1db252b92a19b91e67fa2e2f7e14c0ae5ae308575066d2cd3cddae` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/SCH_UNIT_ASR_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit ASR.md`

源文档 SHA-256：`ec02d14879f03310c1eafb8b936730d81420aa35b827ad868eef131dda8f11bb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
