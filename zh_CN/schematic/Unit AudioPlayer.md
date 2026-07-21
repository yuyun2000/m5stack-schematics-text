# Unit AudioPlayer 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit AudioPlayer |
| SKU | U197 |
| 产品 ID | `unit-audioplayer-948669ca7509` |
| 源文档 | `zh_CN/unit/Unit_AudioPlayer.md` |

## 概述

Unit AudioPlayer 以 U1 N9301 为音频解码与播放核心，通过 J1 Grove 的 S_RX/S_TX UART 网络接收控制并回传数据。U2 microSD 卡座通过 SD_CLK、SD_CMD、SD_DAT 连接 U1，VDDIO 经 R3 向卡座供电；U1 的 DAC_L/DAC_R 经 C5/C6 隔直后输出到 CN1 PJ-342 3.5mm 插座。U1 直接由 +5 供电并生成 VDDIO，BUSY 网络在播放时为低、待机时为高，同时驱动 D1 蓝色指示 LED。本页未显示独立 MCU、外部晶振、复位、I2C/CAN/USB、射频、传感器、电池、充电或调试电路。

## 检索关键词

`Unit AudioPlayer`、`U197`、`N9301`、`microSD`、`5033981892`、`UART`、`S_RX`、`S_TX`、`9600bps`、`8N1`、`SD_CLK`、`SD_CMD`、`SD_DAT`、`SPI_CLK`、`SPI_CMD`、`SPI_DAT`、`DAC_L`、`DAC_R`、`AUDIO_L`、`AUDIO_R`、`BUSY`、`PJ-342`、`3.5mm stereo`、`VDDIO`、`+5`、`MP3`、`WAV`、`FAT16`、`FAT32`、`32GB`、`BLUE 0603`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | N9301 | 音频解码与播放核心，连接 UART、microSD、左右声道 DAC、BUSY 状态和电源网络 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 A2-B3，U1 N9301 pins1-16，RX/TX/SPI_CLK/SPI_CMD/SPI_DAT/DAC_L/DAC_R/BUSY/VCC/VDDIO |
| U2 | 5033981892 | microSD 卡座，连接 SD_CMD、SD_CLK、SD_DAT、VDDIO/GND 与卡检测网络 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 A3-B3，U2 5033981892，DAT2/CD-DAT3/CMD/VDD/CLK/VSS/DAT0/DAT1/CD/EH |
| J1 | Grove | 四针 UART 与 +5/GND 电源接口 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 C2，J1 Grove pin1 S_TX、pin2 S_RX、pin3 +5、pin4 GND |
| CN1 | PJ-342 | AUDIO_L/AUDIO_R 经隔直电容后的 3.5mm 立体声音频输出插座 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 C3-C4，CN1 PJ-342 与 C5/C6、R5/R6、AUDIO_L/AUDIO_R/GND |
| D1 | BLUE 0603 | BUSY 播放状态指示 LED，由 VDDIO 经 R7 供电 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 C2，VDDIO-R7 470R/1%-D1 BLUE 0603-BUSY 支路 |
| R1,R2 | 470R/1% | S_RX/S_TX 与 U1 RX/TX 之间的串联电阻 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 B1-B2，R1/R2 470R/1% 与 U1 pins1/2 |
| C5,C6,R5,R6 | 1uF/50V / 1uF/50V / 2K/1% / 2K/1% | 左右音频输出的隔直与对地负载网络 | 图 0340c05253ef / 第 1 页 / 第 1 页网格 C3，AUDIO_L/AUDIO_R、C5/C6、R5/R6 与 CN1 |

## 系统结构

### Unit AudioPlayer 系统架构

U1 N9301 通过 J1 的 S_RX/S_TX UART 接口受控，通过 SD_CLK/SD_CMD/SD_DAT 访问 U2 microSD 卡座，并将 DAC_L/DAC_R 模拟音频经隔直网络输出到 CN1 PJ-342；BUSY 网络提供播放状态并驱动 D1。

- 参数与网络：`decoder=U1 N9301`；`control=J1 S_RX/S_TX UART`；`storage=U2 microSD`；`storage_bus=SD_CLK/SD_CMD/SD_DAT`；`audio_output=DAC_L/DAC_R -> CN1 PJ-342`；`status=BUSY -> D1`；`power=+5 and VDDIO`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 本页未包含的子系统

该原理图页未显示独立 MCU/协处理器、外部晶振、复位/BOOT、调试、I2C/CAN/RS-485/USB/I2S、射频、传感器、电池或充电电路；U1 DP/DM pins9/10 与 1WIRE pin12 标记未用。

- 参数与网络：`mcu=null`；`external_clock=null`；`reset_boot=null`；`debug=null`；`other_buses=null`；`rf=null`；`sensor=null`；`battery_charger=null`；`unused_n9301=pin9 DP,pin10 DM,pin12 1WIRE`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页完整原理图及 U1 pins9/10/12 未用标记

## 核心器件

### BUSY 蓝色指示 LED

VDDIO 经 R7 470R/1% 和 D1 BLUE 0603 串联到 BUSY；结合图内 BUSY 电平注释，播放低电平时该支路具备导通条件。

- 参数与网络：`path=VDDIO -> R7 470R/1% -> D1 BLUE 0603 -> BUSY`；`playback=BUSY low`；`standby=BUSY high`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 C2，R7/D1/BUSY 与上方 BUSY 电平注释

## 电源

### N9301 +5 与 VDDIO 供电

U1 VCC pin4 直接接 +5，GND pin3 接 GND；VDDIO pin5 形成 VDDIO 网络，C2 0.1uF/50V 位于 +5 侧，C4 1uF/50V 从 VDDIO 接 GND，VCOM pin16 由 C1 1uF/50V 对地去耦。

- 参数与网络：`main_supply=U1 pin4 VCC=+5`；`ground=U1 pin3 GND`；`io_supply=U1 pin5 VDDIO`；`main_cap=C2 0.1uF/50V`；`io_cap=C4 1uF/50V`；`vcom=U1 pin16 VCOM with C1 1uF/50V`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B1-B2，U1 VCC/GND/VDDIO/VCOM 与 C1/C2/C4

### microSD 卡座供电

VDDIO 经 R3 2R2/1% 连接 U2 VDD pin4，C3 1uF/50V 从卡座供电节点接 GND；U2 CD pin9 连接 R4 2K/1% 网络。

- 参数与网络：`source=VDDIO`；`series_resistor=R3 2R2/1%`；`destination=U2 pin4 VDD`；`decoupling=C3 1uF/50V`；`card_detect=U2 pin9 CD with R4 2K/1%`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B3，VDDIO/R3/C3/U2 VDD 与 U2 CD/R4

## 接口

### J1 Grove UART 针脚映射

J1 pin1=S_TX、pin2=S_RX、pin3=+5、pin4=GND；S_RX 经 R1 进入 U1 RX，S_TX 由 U1 TX 经 R2 引出。

- 参数与网络：`reference=J1 Grove`；`pin1=S_TX, output from unit`；`pin2=S_RX, input to unit`；`pin3=+5 power input`；`pin4=GND`；`receive_path=J1 pin2 S_RX -> R1 -> U1 pin1 RX`；`transmit_path=U1 pin2 TX -> R2 -> J1 pin1 S_TX`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B1-C2，J1、R1/R2 与 U1 RX/TX 同名网络

### CN1 3.5mm 立体声输出

CN1 标为 PJ-342，连接 C5/C6 后的左右音频节点与 GND，并带成组切换触点；原理图未标耳机检测信号或功放。

- 参数与网络：`reference=CN1`；`part_number=PJ-342`；`left_source=AUDIO_L via C5`；`right_source=AUDIO_R via C6`；`ground=GND`；`switch_contacts=true`；`detect_net=null`；`amplifier=null`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 C3-C4，CN1 PJ-342 pins2-7 与左右声道/GND

## 总线

### N9301 UART 控制总线

S_RX 通过 R1 470R/1% 连接 U1 RX pin1，S_TX 通过 R2 470R/1% 连接 U1 TX pin2；原理图确认全双线 UART 拓扑，但没有打印波特率或帧格式。

- 参数与网络：`device_rx=S_RX -> R1 470R/1% -> U1 pin1 RX`；`device_tx=U1 pin2 TX -> R2 470R/1% -> S_TX`；`physical_wires=2`；`baud_rate_printed=null`；`frame_format_printed=null`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B1-B2，S_RX/S_TX、R1/R2 与 U1 pins1/2

### N9301 至 microSD 三线 SPI 类连接

U1 SPI_CLK pin6、SPI_CMD pin7、SPI_DAT pin8 分别通过 SD_CLK、SD_CMD、SD_DAT 连接 U2 CLK pin5、CMD pin3、DAT0 pin7。

- 参数与网络：`controller=U1 N9301`；`clock=U1 pin6 SPI_CLK -> SD_CLK -> U2 pin5 CLK`；`command=U1 pin7 SPI_CMD -> SD_CMD -> U2 pin3 CMD`；`data=U1 pin8 SPI_DAT -> SD_DAT -> U2 pin7 DAT0`；`chip_select_net=SD_CMD as labeled by schematic`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B2-B3，U1 pins6-8 与 U2 pins3/5/7 同名 SD_* 网络

## GPIO 与控制信号

### BUSY 播放状态输出

U1 BUSY pin11 连接 BUSY 网络；图内注释明确 BUSY 在播放时为低、待机时为高，因此该信号是从播放器输出的低有效播放状态。

- 参数与网络：`source=U1 pin11 BUSY`；`net=BUSY`；`playback_level=low`；`standby_level=high`；`direction=output from N9301`；`external_connector=null`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 A2-B2，英文注释 'playback is low, standby is high' 与 U1 pin11 BUSY

## 保护电路

### 外部接口保护

J1 UART/+5、U2 microSD 与 CN1 音频路径未显示 TVS、专用 ESD 阵列、保险丝、反接或过压保护器件；可见串联器件为 UART 的 R1/R2、卡供电 R3 和音频隔直 C5/C6。

- 参数与网络：`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`uart_series=R1/R2 470R/1%`；`sd_supply_series=R3 2R2/1%`；`audio_coupling=C5/C6 1uF/50V`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页 J1/U2/CN1 全部外部接口路径，无专用保护符号

## 关键网络

### 关键接口网络映射

S_RX/S_TX 连接 J1 与 U1 UART，SD_CLK/SD_CMD/SD_DAT 连接 U1 与 U2，AUDIO_L/AUDIO_R 连接 U1 DAC 与 CN1，BUSY 连接 U1 与 D1 指示支路。

- 参数与网络：`S_RX=J1 pin2,R1,U1 pin1`；`S_TX=U1 pin2,R2,J1 pin1`；`SD_CLK=U1 pin6,U2 pin5`；`SD_CMD=U1 pin7,U2 pin3`；`SD_DAT=U1 pin8,U2 pin7`；`AUDIO_L=U1 pin14,C5,CN1`；`AUDIO_R=U1 pin13,C6,CN1`；`BUSY=U1 pin11,D1`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页全部同名 UART/SD/audio/BUSY 网络

## 存储

### U2 microSD 卡座连接

U2 CMD pin3 接 SD_CMD、CLK pin5 接 SD_CLK、DAT0 pin7 接 SD_DAT、VSS pin6 和 EH pins11 接 GND；DAT2 pin1、CD/DAT3 pin2 与 DAT1 pin8 标记未用。

- 参数与网络：`socket=U2 5033981892`；`command=pin3 CMD=SD_CMD`；`clock=pin5 CLK=SD_CLK`；`data=pin7 DAT0=SD_DAT`；`ground=pin6 VSS,pins11 EH`；`unused=pin1 DAT2,pin2 CD/DAT3,pin8 DAT1`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 A3-B3，U2 pins1-11 与 SD_CMD/SD_CLK/SD_DAT/GND

## 音频

### N9301 左右声道 DAC 输出

U1 DAC_L pin14 形成 AUDIO_L，U1 DAC_R pin13 形成 AUDIO_R；AUDIO_L/AUDIO_R 分别经 C5/C6 1uF/50V 隔直后进入 CN1，两个隔直后节点分别由 R5/R6 2K/1% 接 GND。

- 参数与网络：`left=U1 pin14 DAC_L -> AUDIO_L -> C5 1uF/50V -> CN1`；`right=U1 pin13 DAC_R -> AUDIO_R -> C6 1uF/50V -> CN1`；`left_load=R5 2K/1% to GND`；`right_load=R6 2K/1% to GND`
- 证据：图 0340c05253ef / 第 1 页 / 第 1 页网格 B2-C4，U1 DAC_L/DAC_R、AUDIO_L/AUDIO_R、C5/C6、R5/R6 与 CN1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit AudioPlayer 系统架构 | `decoder=U1 N9301`；`control=J1 S_RX/S_TX UART`；`storage=U2 microSD`；`storage_bus=SD_CLK/SD_CMD/SD_DAT`；`audio_output=DAC_L/DAC_R -> CN1 PJ-342`；`status=BUSY -> D1`；`power=+5 and VDDIO` |
| 接口 | J1 Grove UART 针脚映射 | `reference=J1 Grove`；`pin1=S_TX, output from unit`；`pin2=S_RX, input to unit`；`pin3=+5 power input`；`pin4=GND`；`receive_path=J1 pin2 S_RX -> R1 -> U1 pin1 RX`；`transmit_path=U1 pin2 TX -> R2 -> J1 pin1 S_TX` |
| 总线 | N9301 UART 控制总线 | `device_rx=S_RX -> R1 470R/1% -> U1 pin1 RX`；`device_tx=U1 pin2 TX -> R2 470R/1% -> S_TX`；`physical_wires=2`；`baud_rate_printed=null`；`frame_format_printed=null` |
| 电源 | N9301 +5 与 VDDIO 供电 | `main_supply=U1 pin4 VCC=+5`；`ground=U1 pin3 GND`；`io_supply=U1 pin5 VDDIO`；`main_cap=C2 0.1uF/50V`；`io_cap=C4 1uF/50V`；`vcom=U1 pin16 VCOM with C1 1uF/50V` |
| 存储 | U2 microSD 卡座连接 | `socket=U2 5033981892`；`command=pin3 CMD=SD_CMD`；`clock=pin5 CLK=SD_CLK`；`data=pin7 DAT0=SD_DAT`；`ground=pin6 VSS,pins11 EH`；`unused=pin1 DAT2,pin2 CD/DAT3,pin8 DAT1` |
| 总线 | N9301 至 microSD 三线 SPI 类连接 | `controller=U1 N9301`；`clock=U1 pin6 SPI_CLK -> SD_CLK -> U2 pin5 CLK`；`command=U1 pin7 SPI_CMD -> SD_CMD -> U2 pin3 CMD`；`data=U1 pin8 SPI_DAT -> SD_DAT -> U2 pin7 DAT0`；`chip_select_net=SD_CMD as labeled by schematic` |
| 电源 | microSD 卡座供电 | `source=VDDIO`；`series_resistor=R3 2R2/1%`；`destination=U2 pin4 VDD`；`decoupling=C3 1uF/50V`；`card_detect=U2 pin9 CD with R4 2K/1%` |
| 音频 | N9301 左右声道 DAC 输出 | `left=U1 pin14 DAC_L -> AUDIO_L -> C5 1uF/50V -> CN1`；`right=U1 pin13 DAC_R -> AUDIO_R -> C6 1uF/50V -> CN1`；`left_load=R5 2K/1% to GND`；`right_load=R6 2K/1% to GND` |
| 接口 | CN1 3.5mm 立体声输出 | `reference=CN1`；`part_number=PJ-342`；`left_source=AUDIO_L via C5`；`right_source=AUDIO_R via C6`；`ground=GND`；`switch_contacts=true`；`detect_net=null`；`amplifier=null` |
| GPIO 与控制信号 | BUSY 播放状态输出 | `source=U1 pin11 BUSY`；`net=BUSY`；`playback_level=low`；`standby_level=high`；`direction=output from N9301`；`external_connector=null` |
| 核心器件 | BUSY 蓝色指示 LED | `path=VDDIO -> R7 470R/1% -> D1 BLUE 0603 -> BUSY`；`playback=BUSY low`；`standby=BUSY high` |
| 关键网络 | 关键接口网络映射 | `S_RX=J1 pin2,R1,U1 pin1`；`S_TX=U1 pin2,R2,J1 pin1`；`SD_CLK=U1 pin6,U2 pin5`；`SD_CMD=U1 pin7,U2 pin3`；`SD_DAT=U1 pin8,U2 pin7`；`AUDIO_L=U1 pin14,C5,CN1`；`AUDIO_R=U1 pin13,C6,CN1`；`BUSY=U1 pin11,D1` |
| 保护电路 | 外部接口保护 | `tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`uart_series=R1/R2 470R/1%`；`sd_supply_series=R3 2R2/1%`；`audio_coupling=C5/C6 1uF/50V` |
| 系统结构 | 本页未包含的子系统 | `mcu=null`；`external_clock=null`；`reset_boot=null`；`debug=null`；`other_buses=null`；`rf=null`；`sensor=null`；`battery_charger=null`；`unused_n9301=pin9 DP,pin10 DM,pin12 1WIRE` |
| 总线 | 正文 UART 默认设置 | `documented_baud=9600bps`；`documented_frame=8N1`；`schematic_baud=null`；`logic_thresholds=null`；`protocol_frames=null` |
| 存储 | 正文 microSD 文件系统、容量与初始化要求 | `documented_filesystems=FAT16,FAT32`；`documented_capacity=32GB max`；`documented_initialization=insert card before power-on`；`card_type=null`；`hotplug=null`；`timing=null` |
| 音频 | 正文音频格式与播放功能 | `documented_formats=MP3,WAV`；`documented_modes=loop playback,combined playback`；`sample_rates=null`；`bit_depths=null`；`channel_modes=null`；`playlist_rules=null` |
| 电源 | 正文工作、待机与休眠功耗 | `documented_active=5.01V@25.17mA`；`documented_standby=5.01V@7.33mA`；`documented_sleep=5.02V@871.24uA`；`audio_load=null`；`sd_state=null`；`tolerance=null` |
| 音频 | 3.5mm 音频输出电气性能 | `connector=CN1 PJ-342`；`coupling=C5/C6 1uF/50V`；`loads=R5/R6 2K/1%`；`output_level=null`；`load_impedance=null`；`frequency_response=null`；`thd_noise=null`；`headphone_drive=null` |

## 待确认事项

- `bus.documented-uart-settings`：正文称 UART 默认使用 9600bps@8N1；原理图只确认 RX/TX 电气连接，没有波特率、数据位、校验位、停止位、逻辑门限或指令帧定义。（证据：图 0340c05253ef / 第 1 页 / 第 1 页 J1 S_RX/S_TX 与 U1 RX/TX，无 UART 参数）
- `storage.documented-card-capabilities`：正文称支持 FAT16/FAT32、最大 32GB，并要求上电前插入 microSD；原理图只确认卡座及三线连接，未标容量、文件系统、卡类型、初始化时序或热插拔行为。（证据：图 0340c05253ef / 第 1 页 / 第 1 页 U1/U2 SD_CLK/SD_CMD/SD_DAT 与卡检测网络，无文件系统或容量文字）
- `audio.documented-codecs-playback`：正文称支持 MP3/WAV、循环播放和组合播放；原理图确认 N9301、microSD 与立体声 DAC 输出，但未标编解码格式、采样率、位深、声道限制、播放列表或循环行为。（证据：图 0340c05253ef / 第 1 页 / 第 1 页 U1 N9301、U2 microSD 与 DAC_L/DAC_R，无格式表）
- `power.documented-consumption`：正文给出工作 5.01V@25.17mA、待机 5.01V@7.33mA、休眠 5.02V@871.24uA；原理图没有测试条件、音量/负载、卡状态、模式定义或容差。（证据：图 0340c05253ef / 第 1 页 / 第 1 页 +5/VDDIO 供电网络，无功耗或测试条件标注）
- `audio.output-electrical-performance`：原理图确认 DAC_L/DAC_R 经 1uF 隔直和 2K 对地后输出到 PJ-342，但未标输出电平、负载阻抗范围、频率响应、噪声、失真、声道串扰或是否适合直接驱动耳机。（证据：图 0340c05253ef / 第 1 页 / 第 1 页 U1 DAC_L/DAC_R 至 CN1 PJ-342 输出链路，无性能值）
- `review.uart-settings`：请用当前固件或协议确认默认 9600bps@8N1、逻辑电平、命令帧、响应与超时规则。；原因：原理图只显示 UART 物理连线。
- `review.card-capabilities`：请确认支持的 microSD/SDHC 类型、FAT16/FAT32 限制、32GB 上限、格式化参数、上电插卡与热插拔行为。；原因：板级卡座连接不能证明文件系统和容量。
- `review.codecs-playback`：请用 N9301 资料和固件确认 MP3/WAV 编码约束、采样率/位深/声道、文件命名、循环与组合播放规则。；原因：原理图未列解码和播放功能参数。
- `review.power-consumption`：请确认工作、待机、休眠电流的测试电压、音量与负载、microSD 状态、固件模式、温度和容差。；原因：原理图无法确认整机动态功耗。
- `review.audio-output`：请用 datasheet 或实测确认 3.5mm 输出电平、推荐负载、频响、THD+N、串扰及耳机直驱能力。；原因：原理图只提供模拟连接拓扑。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0340c05253ef425e196b3b4ecd9667a0ca7bfdbf22564415227dd8243f4e7115` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/Unit_AudioPlayer_U197_page_01.png` |

---

源文档：`zh_CN/unit/Unit_AudioPlayer.md`

源文档 SHA-256：`8a51940d62012f56f8742266b4b588b29ef65c369bcd4cb5a78202f3de11b98b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
