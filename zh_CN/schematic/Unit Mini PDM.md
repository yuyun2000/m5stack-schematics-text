# Unit Mini PDM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini PDM |
| SKU | U089 |
| 产品 ID | `unit-mini-pdm-2175a10d1184` |
| 源文档 | `zh_CN/unit/pdm.md` |

## 概述

Unit Mini PDM 以 U1 SPM1423HM4H-B 数字 MEMS 麦克风输出 PDM 音频，不含独立 MCU、存储器或晶振。J1 pin 1 的 CLK 直接输入 U1 pin 4，U1 pin 5 的 DAT 直接输出到 J1 pin 2，SELECT pin 2 与 GND 相连。J1 输入的 +5V 由 U3 HT7333 稳压为 +3.3V 给麦克风供电，C5、C6、C7 分别完成输入和输出去耦。

## 检索关键词

`Unit Mini PDM`、`U089`、`SPM1423HM4H-B`、`SPM1423`、`HT7333`、`U1`、`U3`、`J1`、`HY-2.0_A`、`PDM`、`CLK`、`DAT`、`SELECT`、`+5V`、`+3.3V`、`C5 1uF`、`C6 1uF`、`C7 100nF`、`digital MEMS microphone`、`PDM clock input`、`PDM data output`、`Grove PORT.B`、`LDO`、`audio capture`、`GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SPM1423HM4H-B | 数字 MEMS 麦克风，将声音转换为由 CLK 驱动的 DAT PDM 数据流 | 图 23bc130350bc / 第 1 页 / 页面中央 U1 SPM1423HM4H-B：pin 1/3 GND、pin 2 SELECT、pin 4 CLK、pin 5 DAT、pin 6 3V3 |
| U3 | HT7333 | 将 +5V 输入稳压为 +3.3V 的三引脚 LDO | 图 23bc130350bc / 第 1 页 / 页面上部 U3 HT7333：pin 2 VIN 接 +5V、pin 1 GND、pin 3 VOUT 接 +3.3V |
| J1 | HY-2.0_A | 4 针 Grove 接口，引入 PDM CLK 与 +5V/GND，并输出 DAT | 图 23bc130350bc / 第 1 页 / 页面下部 J1 HY-2.0_A：pin 1 CLK、pin 2 DAT、pin 3 VCC 接 +5V、pin 4 GND |
| C5/C6/C7 | 1uF / 1uF / 100nF | HT7333 输入与 +3.3V 输出的电源去耦和稳定电容 | 图 23bc130350bc / 第 1 页 / 页面上部 C5 1uF 接 +5V-GND，C6 1uF 与 C7 100nF 接 +3.3V-GND |

## 系统结构

### Unit Mini PDM

整板由 U1 数字 MEMS 麦克风、U3 3.3V LDO、一个 4 针接口和三颗去耦电容组成；原理图未显示 MCU、协处理器、存储器、外部晶振、复位或调试接口。

- 参数与网络：`microphone=U1 SPM1423HM4H-B`；`regulator=U3 HT7333`；`interface=J1 HY-2.0_A`；`controller=null`；`storage=null`；`external_clock_source=host via J1 CLK`；`reset=null`
- 证据：图 23bc130350bc / 第 1 页 / 整页 U3/C5-C7、U1、J1 构成全部可见电路，无其他 IC 或接口

## 电源

### U3 HT7333

U3 pin 2 VIN 接 +5V，pin 1 接 GND，pin 3 VOUT 生成 +3.3V，构成麦克风的本地 3.3V LDO 电源。

- 参数与网络：`reference=U3`；`part_number=HT7333`；`input=+5V at pin 2 VIN`；`ground=pin 1 GND`；`output=+3.3V at pin 3 VOUT`；`enable=null`
- 证据：图 23bc130350bc / 第 1 页 / 页面上部 U3 HT7333 的 VIN/VOUT/GND pin 编号及 +5V/+3.3V 网络

### C5/C6/C7

C5 1uF 从 +5V 接 GND；C6 1uF 与 C7 100nF 从 +3.3V 接 GND，分别为 HT7333 输入和输出提供去耦。

- 参数与网络：`input_capacitor=C5 1uF, +5V to GND`；`output_bulk=C6 1uF, +3.3V to GND`；`output_high_frequency=C7 100nF, +3.3V to GND`
- 证据：图 23bc130350bc / 第 1 页 / 页面上部 U3 两侧 C5 1uF、C6 1uF、C7 100nF 及电源/地连接

## 接口

### J1 HY-2.0_A

J1 pin 1 为 CLK，pin 2 为 DAT，pin 3 为接入板内 +5V 的 VCC，pin 4 为 GND。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_A`；`pin_1=CLK input`；`pin_2=DAT output`；`pin_3=+5V power input`；`pin_4=GND`
- 证据：图 23bc130350bc / 第 1 页 / 页面下部 J1 HY-2.0_A 的 CLK/DAT/VCC/GND 与 pin 1-4 标注，VCC 外部网络标 +5V

## 总线

### PDM CLK/DAT

CLK 从 J1 pin 1 输入并直接连接 U1 CLK pin 4，DAT 从 U1 DAT pin 5 输出并直接连接 J1 pin 2；两条信号均未经过缓冲或电平转换。

- 参数与网络：`clock=J1 pin 1 CLK -> U1 pin 4 CLK`；`data=U1 pin 5 DAT -> J1 pin 2 DAT`；`clock_direction=host to microphone`；`data_direction=microphone to host`；`buffer=null`；`level_shifter=null`
- 证据：图 23bc130350bc / 第 1 页 / 页面中央 U1 CLK/DAT 同名网络与页面下部 J1 pin 1/pin 2

## GPIO 与控制信号

### U1 SELECT

U1 SELECT pin 2 与 U1 的 pin 1、pin 3 共接 GND，板上没有用于更改 SELECT 电平的跳线或电阻。

- 参数与网络：`pin=U1 pin 2 SELECT`；`level=GND`；`strap=hard-wired low`；`configuration_jumper=null`
- 证据：图 23bc130350bc / 第 1 页 / 页面中央 U1 左侧 pin 1/2/3 公共接地连线和 GND 符号

## 时钟

### CLK

板上没有本地振荡器，PDM CLK 必须由外部主机从 J1 pin 1 提供给 U1 pin 4。

- 参数与网络：`net=CLK`；`source=external host via J1 pin 1`；`destination=U1 pin 4`；`local_oscillator=null`；`direction=input`
- 证据：图 23bc130350bc / 第 1 页 / 页面 U1 pin 4 CLK 与 J1 pin 1 CLK；整页无晶振或时钟发生器

## 保护电路

### J1 CLK/DAT/+5V

本页未显示 J1 的 CLK、DAT 或 +5V 上有 TVS/ESD 阵列、串联信号电阻、保险丝或反接保护；CLK/DAT 直接连接 U1，+5V 直接连接 U3。

- 参数与网络：`tv_esd=null`；`clock_series_resistor=null`；`data_series_resistor=null`；`fuse=null`；`reverse_polarity_protection=null`
- 证据：图 23bc130350bc / 第 1 页 / 整页 J1-U1/U3 信号与电源路径，无保护器件位号

## 关键网络

### +5V

+5V 网络从 J1 pin 3 连接 U3 VIN pin 2 和 C5 上端，不直接连接 U1。

- 参数与网络：`net=+5V`；`source=J1 pin 3`；`loads=U3 pin 2 VIN,C5 1uF`；`microphone_direct_supply=false`
- 证据：图 23bc130350bc / 第 1 页 / 页面 J1 pin 3 +5V 同名网络与页面上部 U3 VIN/C5

### +3.3V

+3.3V 由 U3 VOUT pin 3 生成，连接 U1 pin 6 3V3 以及 C6/C7 上端。

- 参数与网络：`net=+3.3V`；`source=U3 pin 3 VOUT`；`microphone_supply=U1 pin 6 3V3`；`decoupling=C6 1uF,C7 100nF`
- 证据：图 23bc130350bc / 第 1 页 / 页面上部 U3 VOUT/C6/C7 +3.3V 标签与中央 U1 pin 6 +3.3V 标签

## 音频

### U1 SPM1423HM4H-B

U1 pin 1 和 pin 3 标注 GND，pin 2 为 SELECT，pin 4 为 CLK，pin 5 为 DAT，pin 6 为 3V3。

- 参数与网络：`pin_1=GND`；`pin_2=SELECT`；`pin_3=GND`；`pin_4=CLK`；`pin_5=DAT`；`pin_6=+3.3V`
- 证据：图 23bc130350bc / 第 1 页 / 页面中央 U1 六引脚符号及 GND/SELECT/CLK/DAT/3V3 标签

### DAT

U1 pin 5 的 DAT 网络直连 J1 pin 2，是麦克风到外部主机的 PDM 音频数据输出。

- 参数与网络：`net=DAT`；`source=U1 pin 5`；`destination=J1 pin 2`；`direction=output`
- 证据：图 23bc130350bc / 第 1 页 / 页面中央 U1 pin 5 DAT 与页面下部 J1 pin 2 DAT 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini PDM | `microphone=U1 SPM1423HM4H-B`；`regulator=U3 HT7333`；`interface=J1 HY-2.0_A`；`controller=null`；`storage=null`；`external_clock_source=host via J1 CLK`；`reset=null` |
| 音频 | U1 SPM1423HM4H-B | `pin_1=GND`；`pin_2=SELECT`；`pin_3=GND`；`pin_4=CLK`；`pin_5=DAT`；`pin_6=+3.3V` |
| 总线 | PDM CLK/DAT | `clock=J1 pin 1 CLK -> U1 pin 4 CLK`；`data=U1 pin 5 DAT -> J1 pin 2 DAT`；`clock_direction=host to microphone`；`data_direction=microphone to host`；`buffer=null`；`level_shifter=null` |
| 时钟 | CLK | `net=CLK`；`source=external host via J1 pin 1`；`destination=U1 pin 4`；`local_oscillator=null`；`direction=input` |
| 音频 | DAT | `net=DAT`；`source=U1 pin 5`；`destination=J1 pin 2`；`direction=output` |
| GPIO 与控制信号 | U1 SELECT | `pin=U1 pin 2 SELECT`；`level=GND`；`strap=hard-wired low`；`configuration_jumper=null` |
| 接口 | J1 HY-2.0_A | `reference=J1`；`part_number=HY-2.0_A`；`pin_1=CLK input`；`pin_2=DAT output`；`pin_3=+5V power input`；`pin_4=GND` |
| 电源 | U3 HT7333 | `reference=U3`；`part_number=HT7333`；`input=+5V at pin 2 VIN`；`ground=pin 1 GND`；`output=+3.3V at pin 3 VOUT`；`enable=null` |
| 电源 | C5/C6/C7 | `input_capacitor=C5 1uF, +5V to GND`；`output_bulk=C6 1uF, +3.3V to GND`；`output_high_frequency=C7 100nF, +3.3V to GND` |
| 关键网络 | +5V | `net=+5V`；`source=J1 pin 3`；`loads=U3 pin 2 VIN,C5 1uF`；`microphone_direct_supply=false` |
| 关键网络 | +3.3V | `net=+3.3V`；`source=U3 pin 3 VOUT`；`microphone_supply=U1 pin 6 3V3`；`decoupling=C6 1uF,C7 100nF` |
| 保护电路 | J1 CLK/DAT/+5V | `tv_esd=null`；`clock_series_resistor=null`；`data_series_resistor=null`；`fuse=null`；`reverse_polarity_protection=null` |
| 音频 | SELECT=GND 的 PDM 时隙 | `select_level=GND`；`edge_or_slot=null`；`left_right_channel=null`；`requires_datasheet=SPM1423HM4H-B` |
| 时钟 | PDM CLK 工作区间 | `clock_net=CLK`；`active_frequency_range=null`；`sleep_threshold=null`；`power_down_threshold=null`；`startup_timing=null` |
| 音频 | SPM1423 音频性能 | `document_sensitivity=-22dBFS at 94dB SPL,1kHz typical`；`document_snr=61.4dB A-weighted typical`；`document_thd=1% at 100dB SPL,1kHz typical`；`document_current=600uA`；`schematic_performance_values=null` |
| 接口 | J1 Grove 线色映射 | `electrical_pinout=pin1 CLK,pin2 DAT,pin3 +5V,pin4 GND`；`color_labels_on_schematic=null`；`document_colors=Black,Red,Yellow,White` |

## 待确认事项

- `audio.select-slot-meaning`：原理图确认 SELECT pin 2 接 GND，但未标注该电平对应 DAT 的上升沿/下降沿、左/右声道或时隙定义，因此具体声道配置不能仅凭本页确定。（证据：图 23bc130350bc / 第 1 页 / 页面中央 U1 SELECT pin 2 接 GND；整页无 L/R 或时钟沿注释）
- `clock.pdm-operating-ranges`：产品正文描述时钟相关的断电、激活和休眠状态，但原理图未给出 CLK 频率范围、状态切换阈值或启动时序，不能由本页确定这些参数。（证据：图 23bc130350bc / 第 1 页 / 页面 U1 pin 4 CLK 与 J1 pin 1 CLK，无频率或功耗模式参数）
- `audio.performance-specifications`：正文列出灵敏度、信噪比、失真和工作电流，但原理图只给出型号与连接，未标注这些性能值或测试条件，因此不能作为原理图确认事实。（证据：图 23bc130350bc / 第 1 页 / 页面中央仅标 U1 SPM1423HM4H-B 及引脚连接，无灵敏度/SNR/THD/电流注释）
- `interface.grove-color-mapping`：原理图给出 J1 pin 1-4 的 CLK/DAT/+5V/GND 电气定义，但未标注 Black/Red/Yellow/White 线色，无法仅凭本页验证正文线色映射。（证据：图 23bc130350bc / 第 1 页 / 页面下部 J1 仅显示 CLK/DAT/VCC/GND 与 pin 编号，无线色文字）
- `review.select-slot-meaning`：请依据 SPM1423HM4H-B datasheet 确认 SELECT=GND 对应的 PDM 时钟沿、时隙或左右声道定义。；原因：原理图只证明 SELECT 电平，不包含协议时隙语义。
- `review.pdm-operating-ranges`：请用麦克风 datasheet 确认 CLK 的工作频率、休眠/断电阈值和启动时序。；原因：原理图没有任何 CLK 数值或模式切换参数。
- `review.audio-performance`：请依据对应批次 SPM1423HM4H-B datasheet 或测试报告复核灵敏度、SNR、THD 和工作电流。；原因：这些参数未出现在原理图，且需要明确测试条件。
- `review.grove-color-mapping`：请结合 Grove 线缆规范与连接器方向确认 Black/Red/Yellow/White 对应 J1 pin 1-4。；原因：原理图没有线色标签。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `23bc130350bc28c060e2f9dfda05405a6d02103782a569ef3978835eb6b78d28` | `https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_sch_01.webp` |

---

源文档：`zh_CN/unit/pdm.md`

源文档 SHA-256：`bc2f4c65c694a6817a0da60f94661def4f4f9efd4f549725e7bcb574a2140a31`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
