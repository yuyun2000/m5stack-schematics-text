# Atom Voice 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Voice |
| SKU | C008-C |
| 产品 ID | `atom-voice-b618de616492` |
| 源文档 | `zh_CN/atom/atomecho.md` |

## 概述

Atom Voice C008-C 的本地资源是一张 ATOM ECHO 音频连接框图，显示 ESP32 方框连接 NS4168、麦克风方框与扬声器符号。功放侧映射为 G22=AMP DATA、G19=AMP BCLK、G33=AMP LRCK，麦克风侧映射为 G33=SYS LRCK/MIC CLK、G23=MIC DATA，因此 G33 是播放与采集共用的音频时钟网络。图中还出现 ESP32 的 3V3、5V、GND 标签，但没有器件位号、阻容、电源转换、保护、晶振、Flash、射频、Grove、RGB、按键或复位电路。正文所列 ESP32-PICO-D4、SPM1423、4MB Flash、0.8W、I2S/PDM 和无线/HMI 参数均需完整原理图或 datasheet 复核。

## 检索关键词

`Atom Voice`、`ATOM ECHO`、`C008-C`、`ESP32`、`ESP32-PICO-D4`、`NS4168`、`SPM1423`、`MIC`、`speaker`、`AMP DATA`、`AMP BCLK`、`AMP LRCK`、`SYS LRCK`、`MIC CLK`、`MIC DATA`、`G22`、`G19`、`G33`、`G23`、`I2S`、`PDM`、`3V3`、`5V`、`GND`、`SK6812`、`G27`、`G39`、`G26`、`G32`、`4MB Flash`、`Wi-Fi`、`A2DP`、`BLE 4.0`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ESP32 block | ESP32 | 音频信号控制方框，标出 3V3、G22、G19、G33、G23、5V 与 GND | 图 8b8748788a42 / 第 1 页 / 第 1 页右侧红色 ESP 32 方框及 3V3/G22/G19/G33/G23/5V/GND 标签 |
| NS4168 block | NS4168 | 数字音频功放方框，连接 SADTA/AMP DATA、BCLK/AMP BCLK、LRCK/AMP LRCK 并驱动扬声器符号 | 图 8b8748788a42 / 第 1 页 / 第 1 页左上 NS4168 方框、SADTA/BCLK/LRCK 与扬声器连接 |
| MIC block | 未标注 | 数字麦克风方框，以 CLK 和 DATA 接入 ESP32 音频网络 | 图 8b8748788a42 / 第 1 页 / 第 1 页左下 MIC 方框、CLK/DATA、SYS LRCK/MIC DATA |
| speaker symbol | 未标注 | 连接 NS4168 输出的扬声器负载，图中未给位号、阻抗或额定功率 | 图 8b8748788a42 / 第 1 页 / 第 1 页最左侧扬声器符号与 NS4168 输出连线 |

## 系统结构

### 音频框图架构

资源图显示 ESP32 通过三条功放音频网络连接 NS4168，NS4168 再连接扬声器；ESP32 还通过 CLK/DATA 两条网络连接 MIC 方框。

- 参数与网络：`controller=ESP32 block`；`playback=ESP32 -> NS4168 -> speaker symbol`；`capture=MIC block <-> ESP32`；`product_mark=ATOM ECHO C008-C`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整 ATOM ECHO C008-C 音频连接框图

### 本地资源详细程度

本地资源为单页功能连接图，产品标记 ATOM ECHO C008-C；页面未给任何标准位号、阻容值、封装、引脚号、器件电源脚或完整网名表。

- 参数与网络：`asset_type=functional connection diagram`；`pages=1`；`product_mark=ATOM ECHO C008-C`；`reference_designators=null`；`passive_values=null`；`packages=null`；`device_pin_numbers=null`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整页面，只有 ESP32/NS4168/MIC/扬声器功能块

## 电源

### 框图可见电源标签

ESP32 方框上可见 3V3、5V 和 GND 标签，但页面没有画出它们到 NS4168、MIC 或扬声器的供电连线，也没有电源输入连接器或转换器。

- 参数与网络：`labels=3V3,5V,GND`；`amplifier_supply_connection=null`；`microphone_supply_connection=null`；`converter=null`；`input_connector=null`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页 ESP32 方框的 3V3/5V/GND 标签及全图无电源器件

## 关键网络

### G33 共用音频时钟

NS4168 的 AMP LRCK 与 MIC 的 SYS LRCK/CLK 汇入同一网络并连接 ESP32 G33，因此 G33 在框图中同时服务功放帧时钟与麦克风时钟。

- 参数与网络：`gpio=G33`；`amplifier_signal=AMP LRCK`；`microphone_signal=SYS LRCK/MIC CLK`；`shared=true`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页中部 AMP LRCK 与 SYS LRCK 汇合后连接 ESP32 G33

## 音频

### NS4168 音频信号映射

NS4168 SADTA 标为 AMP DATA 并连接 ESP32 G22，BCLK 标为 AMP BCLK 并连接 G19，LRCK 标为 AMP LRCK 并连接 G33。

- 参数与网络：`amplifier=NS4168`；`data=SADTA/AMP DATA <-> G22`；`bit_clock=BCLK/AMP BCLK <-> G19`；`frame_clock=LRCK/AMP LRCK <-> G33`；`direction_marked=false`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页 NS4168 SADTA/BCLK/LRCK 到 ESP32 G22/G19/G33 连线

### 麦克风音频信号映射

MIC CLK 网络标为 SYS LRCK 并连接 ESP32 G33，MIC DATA 网络连接 ESP32 G23；框图未标麦克风型号和信号方向箭头。

- 参数与网络：`microphone=MIC block`；`clock=CLK/SYS LRCK <-> G33`；`data=DATA/MIC DATA <-> G23`；`direction_marked=false`；`part_number=null`
- 证据：图 8b8748788a42 / 第 1 页 / 第 1 页 MIC CLK/DATA、SYS LRCK/MIC DATA 到 ESP32 G33/G23 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 音频框图架构 | `controller=ESP32 block`；`playback=ESP32 -> NS4168 -> speaker symbol`；`capture=MIC block <-> ESP32`；`product_mark=ATOM ECHO C008-C` |
| 音频 | NS4168 音频信号映射 | `amplifier=NS4168`；`data=SADTA/AMP DATA <-> G22`；`bit_clock=BCLK/AMP BCLK <-> G19`；`frame_clock=LRCK/AMP LRCK <-> G33`；`direction_marked=false` |
| 音频 | 麦克风音频信号映射 | `microphone=MIC block`；`clock=CLK/SYS LRCK <-> G33`；`data=DATA/MIC DATA <-> G23`；`direction_marked=false`；`part_number=null` |
| 关键网络 | G33 共用音频时钟 | `gpio=G33`；`amplifier_signal=AMP LRCK`；`microphone_signal=SYS LRCK/MIC CLK`；`shared=true` |
| 电源 | 框图可见电源标签 | `labels=3V3,5V,GND`；`amplifier_supply_connection=null`；`microphone_supply_connection=null`；`converter=null`；`input_connector=null` |
| 系统结构 | 本地资源详细程度 | `asset_type=functional connection diagram`；`pages=1`；`product_mark=ATOM ECHO C008-C`；`reference_designators=null`；`passive_values=null`；`packages=null`；`device_pin_numbers=null` |
| 核心器件 | 正文 SoC 与麦克风型号 | `documented_soc=ESP32-PICO-D4`；`schematic_soc_label=ESP 32`；`documented_microphone=SPM1423`；`schematic_microphone_label=MIC`；`soc_package=null`；`microphone_package=null` |
| 总线 | 正文 I2S/PDM 音频协议 | `documented_amplifier_bus=I2S`；`documented_microphone_bus=PDM`；`schematic_signal_set=AMP DATA/BCLK/LRCK; MIC CLK/DATA`；`master=null`；`directions=null`；`sample_rate=null`；`bit_width=null`；`channel_format=null`；`clock_frequency=null` |
| 音频 | 正文扬声器与功放参数 | `documented_power=0.8W`；`amplifier=NS4168`；`speaker_impedance=null`；`amplifier_supply=null`；`gain=null`；`enable=null`；`output_topology=null`；`filter=null`；`overcurrent_protection=null` |
| 内存与 Flash | 正文 4MB Flash | `documented_capacity=4MB`；`flash_part_number=null`；`flash_bus=null`；`flash_voltage=null`；`partition_layout=null` |
| 射频 | 正文无线能力 | `documented_wifi=IEEE 802.11b/g/n`；`documented_bluetooth=A2DP,BLE 4.0`；`antenna=null`；`matching_network=null`；`rf_clock=null`；`module_certification=null` |
| 接口 | 正文 Grove 接口 | `documented_connector=HY2.0-4P`；`documented_black=GND`；`documented_red=5V`；`documented_yellow=G26`；`documented_white=G32`；`schematic_connector=null`；`directions=null`；`protection=null` |
| GPIO 与控制信号 | 正文 RGB 与按键映射 | `documented_rgb=SK6812 data=G27`；`documented_button=G39 input`；`documented_reset_button=true`；`schematic_rgb=null`；`button_active_level=null`；`button_bias=null`；`debounce=null`；`reset_net=null` |
| 电源 | 电源转换与保护实现 | `visible_labels=3V3,5V,GND`；`input_source=null`；`regulator=null`；`amplifier_supply=null`；`microphone_supply=null`；`enable=null`；`decoupling=null`；`overcurrent=null`；`overvoltage=null`；`reverse_polarity=null`；`esd=null`；`current_budget=null` |
| 调试与烧录 | 复位、BOOT 与编程接口 | `reset=null`；`boot=null`；`uart=null`；`usb=null`；`jtag=null`；`programming_connector=null`；`debug_protection=null` |

## 待确认事项

- `component.documented-soc-and-mic`：正文规格称 SoC 为 ESP32-PICO-D4、麦克风为 SPM1423；资源图只写 ESP 32 与 MIC，无法由该页确认 PICO-D4 子型号、麦克风型号、封装或硬件版本。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页 ESP 32 与 MIC 方框，无 PICO-D4/SPM1423 字样）
- `bus.documented-audio-protocols`：正文称 NS4168 使用 I2S、SPM1423 使用 PDM；资源图只标 SADTA/BCLK/LRCK 与 CLK/DATA，没有标协议名称、主从关系、方向、采样率、位宽、声道格式或时钟频率。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页音频信号标签，无 I2S/PDM 或时序参数文字）
- `audio.documented-speaker-performance`：正文规格列出 0.8W/NS4168；资源图确认 NS4168 与扬声器符号相连，但没有扬声器阻抗、额定功率、NS4168 供电电压、增益、使能、输出拓扑、滤波或保护。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页 NS4168 到扬声器符号，仅信号框图）
- `memory.documented-flash`：正文规格列出 4MB Flash；资源图没有 Flash 器件、位号、总线、容量、电压或分区信息，也未展开 ESP32 模组内部存储。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页 ESP32 方框，无 Flash 或存储连接）
- `rf.documented-wireless`：正文称支持 2.4GHz Wi-Fi 802.11b/g/n、A2DP 与 BLE 4.0；资源图没有射频引脚、天线、匹配网络、晶振、认证模组或无线协议标注。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页 ESP32 方框及全图，无 RF/天线电路）
- `interface.documented-grove`：正文管脚表将 HY2.0-4P 定义为 GND、5V、G26、G32；本地资源页没有 Grove 连接器、针脚、G26/G32 网络、电平、方向或保护。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整框图，无 Grove/HY2.0/G26/G32）
- `gpio.documented-hmi`：正文管脚表称 SK6812 RGB 数据连接 G27、按键输入连接 G39，并列出 Reset Button；资源图没有 SK6812、按键、复位开关、上拉/下拉、有效电平或去抖网络。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整框图，无 RGB/按键/复位电路）
- `power.implementation-and-protection`：框图仅在 ESP32 方框上列出 3V3、5V、GND，未显示 5V 输入来源、3.3V 转换器、NS4168/MIC 供电、电源使能、去耦、过流/过压/反接/ESD 保护或电流预算。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整框图，只有 3V3/5V/GND 标签，无电源与保护元件）
- `debug.reset-boot-programming`：正文提到 Reset Button 与固件烧录，但资源图没有 EN/RESET、BOOT strap、UART、USB、JTAG、下载按键、调试连接器或相关保护。（证据：图 8b8748788a42 / 第 1 页 / 第 1 页完整框图，无 reset/boot/UART/USB/JTAG 网络）
- `review.soc-and-mic`：请用完整 BOM/原理图确认 ESP32-PICO-D4 与 SPM1423 的准确型号、封装、版本和引脚连接。；原因：框图只标 ESP 32 和 MIC。
- `review.audio-protocols`：请由 NS4168/SPM1423 datasheet 与固件确认 I2S/PDM 主从方向、GPIO 模式、采样率、位宽、声道格式和时钟频率。；原因：框图只有信号名，没有协议及时序参数。
- `review.speaker-performance`：请确认扬声器阻抗/功率、NS4168 供电、增益、使能、输出拓扑、滤波、热保护和安全音频幅度。；原因：框图没有功放外围与扬声器参数。
- `review.flash`：请确认 4MB Flash 的型号、总线、电压、频率和固件可用分区。；原因：框图未展开主控存储。
- `review.wireless`：请确认无线 SoC、天线形式、匹配网络、射频时钟、Wi-Fi/Bluetooth 版本与认证信息。；原因：框图没有射频和天线证据。
- `review.grove`：请用完整原理图确认 HY2.0-4P 位号、G26/G32 GPIO 方向、电平、5V 供电能力和接口保护。；原因：Grove 接口未出现在资源图。
- `review.hmi`：请确认 SK6812、G27、G39 按键、Reset Button 的位号、有效电平、偏置与去抖/复位路径。；原因：HMI 电路未出现在资源图。
- `review.power-protection`：请提供完整电源页，确认输入范围、3.3V 转换、音频器件供电、去耦、使能、功耗和保护器件。；原因：页面只有电源标签，没有电源电路。
- `review.debug-programming`：请确认复位、BOOT、UART/USB/JTAG、下载按键和编程连接器的实际实现。；原因：框图不含调试与烧录网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8b8748788a42bdc25777f83e7e7b1f47b91cbb9e6a1944c2f5fdf97a61b1ddd7` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomecho/atomecho_sch_01.webp` |

---

源文档：`zh_CN/atom/atomecho.md`

源文档 SHA-256：`72ed0abf69f25968d4b50e3537d5da57bf44484ccaff7c29cf6700818ea16534`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
