# Module ASR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module ASR |
| SKU | M147 |
| 产品 ID | `module-asr-9df8acfba584` |
| 源文档 | `zh_CN/module/Module_ASR.md` |

## 概述

Module ASR V0.4 原理图以 U4 CI1302 为核心，MK1 模拟麦克风经 MICBIAS/MICPL/MICNL 接入语音芯片，HPOUT_L 经 U1 BE8002D 驱动 P2 差分扬声器。BUS_5V 与 USB_5V 经二极管合路和 Q1 形成 VDD_5V；Type-C 通过 U2 CH340N 与 U3 高速开关连接 CI1302 UART0，SW1/SW2 可从 M5-Bus 多组 GPIO 选择 UART_RXD/UART_TXD。原理图确认硬件音频与烧录路径，但 AEC、命令词数量、语言、唤醒距离、功耗和默认串口格式属于固件或性能声明，仍需专项资料与测试确认。

## 检索关键词

`Module ASR`、`M147`、`CI1302`、`offline voice recognition`、`AEC`、`GMI4527P-2C-32db`、`BE8002D`、`SPK+`、`SPK-`、`HPOUT_L`、`MICBIAS`、`MICPL`、`MICNL`、`CH340N`、`FSW7227YMS10G/TR`、`USB Type-C`、`serial upgrade`、`UART_RXD`、`UART_TXD`、`SW1`、`SW2`、`M5_BUS`、`EXTIO`、`BUS_5V`、`USB_5V`、`VDD_5V`、`VDD_3V3`、`VDD_1V1`、`AGND`、`V0.4`、`115200 8N1`、`53 commands`、`300 commands`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | CI1302 | 离线语音处理芯片，连接麦克风、音频输出、UART、GPIO 与内部电源轨 | 图 7f3de88f0265 / 第 1 页 / B2，U4 CI1302 pins1-24 |
| MK1 | GMI4527P-2C-32db | 差分模拟麦克风，经 MIC1+/MIC1- 偏置与交流耦合连接 CI1302 | 图 7f3de88f0265 / 第 1 页 / B3，MK1 GMI4527P-2C-32db 与 MIC1+/MIC1- |
| U1 | BE8002D | 由 HPOUT_L 驱动的差分扬声器功放 | 图 7f3de88f0265 / 第 1 页 / A2，U1 BE8002D、HPOUT_L、PA6/SPK_SD、SPK+/SPK- |
| P2 | SPK | 两针差分扬声器，连接 SPK+ 与 SPK- | 图 7f3de88f0265 / 第 1 页 / A3，P2 Speaker/SPK pins1-2 |
| J1 | TYPE-C 16P | USB 供电与数据入口，用于 CH340N 串口升级路径 | 图 7f3de88f0265 / 第 1 页 / C1，J1 TYPE-C 16P、F1、R8/R9、USB_D_P/USB_D_N |
| U2 | CH340N | USB 到 UART 的串口升级桥接器 | 图 7f3de88f0265 / 第 1 页 / D2-D3，U2 CH340N、USB_D_P/USB_D_N、CH340_RXD/CH340_TXD |
| U3 | FSW7227YMS10G/TR | 在 M5-Bus UART 与 CH340 UART 之间选择 CI1302 UART0 路径 | 图 7f3de88f0265 / 第 1 页 / C3，U3 FSW7227YMS10G/TR、PB6/RX0、PB5/TX0、UART/CH340 TXD/RXD |
| Q1 | CJ3401 | BUS_5V/USB_5V 合路后到 VDD_5V 的高侧电源开关 | 图 7f3de88f0265 / 第 1 页 / C2，Q1 CJ3401、D1/D3、R7/R10、D2 与电源复位按键 |
| D1/D3 | 1N5819WS / DSK34 | USB_5V 与 BUS_5V 向 VDD_5V 前级节点的二极管合路与反灌隔离 | 图 7f3de88f0265 / 第 1 页 / C2，D1 1N5819WS、D3 DSK34 与 BUS_5V/USB_5V/Q1 |
| SW1/SW2 | 未标注 | 四选一 UART_RXD 与 UART_TXD M5-Bus GPIO 路由拨码 | 图 7f3de88f0265 / 第 1 页 / A4，SW1/SW2 Serial IO Selection |
| P1 | Header 8 | EXTIO 扩展接口，引出 CI1302 UART1/GPIO 与 BUS_3V3/BUS_5V | 图 7f3de88f0265 / 第 1 页 / B4，P1 Header 8 EXTIO pins1-8 |
| J3 | M5_BUS | 30 针主机总线，提供 5V/3.3V/GND、HPWR 与 UART 选择候选 GPIO | 图 7f3de88f0265 / 第 1 页 / D4，J3 M5_BUS pins1-30 |
| D4 | Blue 0603 | 连接 PA6/SPK_SD 的蓝色状态指示 LED | 图 7f3de88f0265 / 第 1 页 / A1，VDD_3V3、R2 10K、D4 Blue 0603、PA6/SPK_SD |

## 系统结构

### Module ASR 架构

U4 CI1302 连接 MK1 模拟麦克风、U1 BE8002D/P2 扬声器链、UART0 串口选择与 Type-C/CH340N 升级链；J3 M5_BUS 和 P1 EXTIO 提供主机及扩展接口。

- 参数与网络：`voice_chip=U4 CI1302`；`microphone=MK1 GMI4527P-2C-32db`；`speaker_amplifier=U1 BE8002D`；`speaker=P2 SPK`；`usb_uart=J1/U2 CH340N/U3`；`host_bus=J3 M5_BUS`；`extension=P1 EXTIO`
- 证据：图 7f3de88f0265 / 第 1 页 / 整页：CI1302、MIC、Speaker、Serial upgrade、Serial IO Selection、EXTIO、M5_BUS

### V0.4 电源回路版本

页面电源区印有“V0.4迭代说明”，说明 BUS_5V 已并入 Q1 MOS 电源回路，并由复位操作断开 BUS_5V 与 USB_5V 供电。

- 参数与网络：`schematic_revision=V0.4`；`revision_note=BUS_5V merged into Q1 MOS power path; reset disconnects BUS_5V and USB_5V supply`
- 证据：图 7f3de88f0265 / 第 1 页 / C2 电源框内 V0.4迭代说明文字

## 核心器件

### U4 CI1302 外围引脚

U4 标为 CI1302；pins1-4 为 AVDD/VIN5V/VDD33/VDD11，pins5/8/24 接地，pins9-13 引出 PA2/PA3/PA5/PA4/PA6，pins14/15 为 PB5/TX0、PB6/RX0，pin16 为 PC4，pin17 为 HPOUT，pins18-22 为 MICPR/MICNR/MICNL/MICPL/MICBIAS，pin23 为 VCM。

- 参数与网络：`reference=U4`；`part_number=CI1302`；`uart1=pin9 PA2/TX1; pin10 PA3/RX1`；`uart0=pin14 PB5/TX0; pin15 PB6/RX0`；`audio_output=pin17 HPOUT_L`；`microphone=pins18-22`；`power=pins1-4; pin23`；`ground=pins5/8/24`
- 证据：图 7f3de88f0265 / 第 1 页 / B2，U4 CI1302 pins1-24 与网络标签

## 电源

### BUS_5V 与 USB_5V 合路

BUS_5V 经 D3 DSK34、USB_5V 经 D1 1N5819WS 以相同方向汇入 Q1 前级节点，Q1 CJ3401 再向 VDD_5V 供电；二极管方向阻止 VDD_5V 向 BUS_5V 或 USB_5V 反向回送。

- 参数与网络：`bus_path=BUS_5V -> D3 DSK34`；`usb_path=USB_5V -> D1 1N5819WS`；`switch=Q1 CJ3401`；`output=VDD_5V`；`reverse_isolation=true`
- 证据：图 7f3de88f0265 / 第 1 页 / C2，BUS_5V/D3 与 USB_5V/D1 汇合到 Q1/VDD_5V

### CI1302 电源轨与去耦

VDD_5V 经 R16 4.7Ω 连接 U4 pin2 VIN5V，C14 4.7uF 与 C15 10uF 对 AGND；U4 pin1 AVDD 配 C13 4.7uF，pin3 VDD33 连接 VDD_3V3 并配 C19 4.7uF，pin4 VDD11 连接 VDD_1V1 并配 C20 4.7uF，pin23 VCM 配 C18 10uF，VDD_5V 另由 C3 10uF 去耦。

- 参数与网络：`vin5v=VDD_5V -> R16 4.7Ω -> U4 pin2`；`vin5v_caps=C14 4.7uF; C15 10uF`；`avdd_cap=C13 4.7uF`；`vdd33=U4 pin3 VDD_3V3; C19 4.7uF`；`vdd11=U4 pin4 VDD_1V1; C20 4.7uF`；`vcm_cap=C18 10uF`；`vdd5_cap=C3 10uF`
- 证据：图 7f3de88f0265 / 第 1 页 / B1-B2，U4 pins1-5/23 与 R16、C3、C13-C15、C18-C20

### GND 与 AGND 连接

数字地 GND 与模拟地 AGND 通过 R11 0Ω 单点连接；CI1302、麦克风和功放的模拟回路使用 AGND，USB/UART 与 M5_BUS 使用 GND。

- 参数与网络：`bridge=R11 0Ω`；`digital_ground=GND`；`analog_ground=AGND`
- 证据：图 7f3de88f0265 / 第 1 页 / B1，R11 0R 连接 GND 与 AGND；全页地网络标注

### USB_5V 与 M5-Bus 5V 边界

D3 的方向为 BUS_5V 向 Q1/VDD_5V 前级节点导通，原理图没有从 USB_5V 或 VDD_5V 返回 J3 BUS_5V 的反向供电路径，因此 Type-C 不能向 M5-Bus pin27 输出 5V。

- 参数与网络：`bus_input=J3 pin27 BUS_5V -> D3`；`usb_input=J1/F1 USB_5V -> D1`；`local_output=VDD_5V`；`usb_to_bus_path=false`
- 证据：图 7f3de88f0265 / 第 1 页 / C2 与 D4，D3 BUS_5V 输入方向、D1 USB_5V 输入方向及 J3 pin27

## 接口

### USB Type-C 电源与数据

J1 的两组 DP 接 USB_D_P、两组 DN 接 USB_D_N，CC1/CC2 分别通过 R8/R9 5.1KΩ 接 GND，GND/SHELL 接地；VBUS 经 F1 0805 1A/6V 保险丝形成 USB_5V。

- 参数与网络：`connector=J1 TYPE-C 16P`；`usb_dp=DP1/DP2 -> USB_D_P`；`usb_dn=DN1/DN2 -> USB_D_N`；`cc_resistors=R8/R9 5.1KΩ to GND`；`vbus_fuse=F1 0805 1A/6V`；`rail=USB_5V`
- 证据：图 7f3de88f0265 / 第 1 页 / C1，J1/F1/R8/R9/USB_D_P/USB_D_N/USB_5V

### U2 CH340N 升级串口

U2 CH340N pins1/2 接 USB_D_P/USB_D_N，pin5 由 USB_5V 供电并配 C9 100nF/C10 10uF，pin8 V3 配 C8 100nF；pins7/6 RXD/TXD 分别经 R5/R6 100Ω 形成 CH340_RXD/CH340_TXD，pins3/4 GND/RTS# 接地。

- 参数与网络：`usb=pins1/2 USB_D_P/USB_D_N`；`supply=pin5 USB_5V`；`supply_caps=C9 100nF; C10 10uF`；`v3_cap=C8 100nF`；`uart=pin7 RXD via R5 100Ω; pin6 TXD via R6 100Ω`；`ground=pins3/4`
- 证据：图 7f3de88f0265 / 第 1 页 / D2-D3，U2 CH340N、R5/R6、C8-C10 与 USB/UART 网络

### CI1302 UART0 数据源切换

U3 D+/pin3 与 D-/pin4 分别连接 U4 PB6/RX0、PB5/TX0；HSD1+/HSD1- 接 UART_TXD/UART_RXD，HSD2+/HSD2- 接 CH340_TXD/CH340_RXD。U3 由 VDD_3V3 供电、OE#/pin10 接地，S/pin2 由 R12 10KΩ 接 USB_5V并由 R13 100KΩ 下拉，USB_5V 状态选择主机 UART 或 CH340 升级 UART。

- 参数与网络：`common_rx=U4 PB6/RX0 -> U3 D+`；`common_tx=U4 PB5/TX0 -> U3 D-`；`host_pair=UART_TXD/UART_RXD`；`usb_pair=CH340_TXD/CH340_RXD`；`selector=U3 pin2 S via R12 10KΩ USB_5V and R13 100KΩ GND`；`enable=OE# pin10 GND`；`supply=VDD_3V3`
- 证据：图 7f3de88f0265 / 第 1 页 / C3，U3 FSW7227YMS10G/TR 全部 UART 与控制引脚

### SW1/SW2 UART GPIO 选择

SW1 将 UART_RXD 公共网络选择连接 GPIO34、GPIO13、GPIO16 或 GPIO3；SW2 将 UART_TXD 公共网络选择连接 GPIO12、GPIO15、GPIO17 或 GPIO1。

- 参数与网络：`rx_options=SW1-1 GPIO34; SW1-2 GPIO13; SW1-3 GPIO16; SW1-4 GPIO3`；`tx_options=SW2-1 GPIO12; SW2-2 GPIO15; SW2-3 GPIO17; SW2-4 GPIO1`
- 证据：图 7f3de88f0265 / 第 1 页 / A4，SW1 UART_RXD/GPIO34/13/16/3 与 SW2 UART_TXD/GPIO12/15/17/1

### J3 UART 候选与电源针脚

SW1/SW2 候选网络对应 J3 pin25 GPIO34、pin21 GPIO13、pin16 GPIO16、pin14 GPIO3、pin22 GPIO12、pin24 GPIO15、pin15 GPIO17、pin13 GPIO1；J3 pins2/4/6 接 GND，pin11 接 BUS_3V3，pin27 接 BUS_5V，pins26/28/30 接 HPWR。

- 参数与网络：`uart_candidates=13 GPIO1; 14 GPIO3; 15 GPIO17; 16 GPIO16; 21 GPIO13; 22 GPIO12; 24 GPIO15; 25 GPIO34`；`ground=pins2/4/6`；`bus_3v3=pin11`；`bus_5v=pin27`；`hpwr=pins26/28/30`
- 证据：图 7f3de88f0265 / 第 1 页 / D4，J3 M5_BUS 外部网络 GPIO1/3/12/13/15/16/17/34、BUS_3V3/BUS_5V/GND/HPWR

### P1 EXTIO 逐针映射

P1 Header 8 pins1-8 依次为 PA2/TX1、PA3/RX1、PA5、PA4、PC4、GND、BUS_3V3、BUS_5V。

- 参数与网络：`pin1=PA2/TX1`；`pin2=PA3/RX1`；`pin3=PA5`；`pin4=PA4`；`pin5=PC4`；`pin6=GND`；`pin7=BUS_3V3`；`pin8=BUS_5V`
- 证据：图 7f3de88f0265 / 第 1 页 / B4，P1 Header 8 EXTIO pins1-8

## GPIO 与控制信号

### PA6/SPK_SD 功放控制与蓝色 LED

U4 pin13 PA6/SPK_SD 连接 U1 SHUTDOWN/pin1，并由 R1 10KΩ 上拉到 VDD_3V3；同一网络通过 D4 Blue 0603 与 R2 10KΩ 连接 VDD_3V3。

- 参数与网络：`mcu_pin=U4 pin13 PA6/SPK_SD`；`amplifier_pin=U1 pin1 SHUTDOWN`；`pullup=R1 10KΩ to VDD_3V3`；`indicator=VDD_3V3 -> R2 10KΩ -> D4 Blue 0603 -> PA6/SPK_SD`
- 证据：图 7f3de88f0265 / 第 1 页 / A1-A2，U4 PA6/SPK_SD、R1、U1 SHUTDOWN 与 R2/D4

## 时钟

### CI1302 外部时钟可见性

U4 pins6/7 XIN/XOUT 在本页没有外部连线，页面未绘制晶体、谐振器或外部振荡器，也未标工作频率。

- 参数与网络：`xin=U4 pin6 no external connection`；`xout=U4 pin7 no external connection`；`external_clock_visible=false`；`frequency_visible=false`
- 证据：图 7f3de88f0265 / 第 1 页 / B2，U4 XIN/XOUT pins6/7 与整页无时钟器件

## 复位

### Q1 电源复位断电

Q1 栅极由 R10 100KΩ 下拉到 GND并由 D2 LESD5Z5.0T1G 钳位；复位按键按下时经 R7 10KΩ 将 Q1 前级电压送到栅极，从而断开 VDD_5V，页面 V0.4 注释明确将其描述为断开 BUS_5V 与 USB_5V 供电。

- 参数与网络：`mosfet=Q1 CJ3401`；`gate_pulldown=R10 100KΩ`；`gate_protection=D2 LESD5Z5.0T1G`；`button_series_resistor=R7 10KΩ`；`effect=disconnect VDD_5V input sources`
- 证据：图 7f3de88f0265 / 第 1 页 / C2，Q1 栅极、R7、SW 3x4x2.5、R10、D2 与 V0.4 注释

## 保护电路

### USB 与电源保护

USB VBUS 配 F1 0805 1A/6V 保险丝，CC1/CC2 配 R8/R9 5.1KΩ 下拉，Q1 栅极配 D2 LESD5Z5.0T1G；页面未显示 USB_D_P/USB_D_N 专用 ESD 阵列或 M5-Bus 信号 ESD 器件。

- 参数与网络：`vbus_fuse=F1 0805 1A/6V`；`cc_resistors=R8/R9 5.1KΩ`；`gate_protection=D2 LESD5Z5.0T1G`；`usb_data_esd_visible=false`；`m5bus_signal_esd_visible=false`
- 证据：图 7f3de88f0265 / 第 1 页 / C1-C2 USB/电源保护器件与整页接口外围

## 内存与 Flash

### 外部存储器可见性

页面未显示 CI1302 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器件及存储总线。

- 参数与网络：`external_flash_visible=false`；`external_eeprom_visible=false`；`external_ram_visible=false`；`sd_interface_visible=false`
- 证据：图 7f3de88f0265 / 第 1 页 / 完整原理图器件范围，无外部存储器或存储连接器

## 音频

### MK1 模拟麦克风链

MK1 型号为 GMI4527P-2C-32db；U4 pin22 MICBIAS 经 R14 2.2KΩ 偏置 MIC1+，pin21 MICPL 经 C6 100nF 交流耦合到 MIC1+，pin20 MICNL 经 C7 100nF 交流耦合到 MIC1-，MIC1- 由 R17 2.2KΩ 接 AGND。

- 参数与网络：`microphone=MK1 GMI4527P-2C-32db`；`positive_path=MICPL -> C6 100nF -> MIC1+`；`bias=MICBIAS -> R14 2.2KΩ -> MIC1+`；`negative_path=MICNL -> C7 100nF -> MIC1-`；`negative_bias=MIC1- -> R17 2.2KΩ -> AGND`
- 证据：图 7f3de88f0265 / 第 1 页 / B3，MICBIAS/MICPL/MICNL、R14/R17、C6/C7 与 MK1

### MICPR/MICNR 可见性

U4 pins18/19 的 MICPR/MICNR 在本页未连接到 MK1 或其他麦克风器件，实际麦克风使用 MICPL/MICNL。

- 参数与网络：`used_inputs=MICPL pin21; MICNL pin20`；`unused_on_page=MICPR pin18; MICNR pin19`
- 证据：图 7f3de88f0265 / 第 1 页 / U4 pins18-21 与右侧单只 MK1 麦克风路径

### HPOUT_L 到差分扬声器

U4 pin17 HPOUT_L 经 C4 100nF、R3 4.7KΩ 接 U1 -IN/pin4，R4 33KΩ 从 SPK- 反馈到 -IN；U1 BYPASS/pin2 与 +IN/pin3 共用 C1 1uF 到 AGND，U1 由 VDD_5V 供电并从 SPK+/SPK- 驱动 P2。

- 参数与网络：`source=U4 pin17 HPOUT_L`；`input_network=C4 100nF; R3 4.7KΩ`；`feedback=R4 33KΩ from SPK-`；`bypass=C1 1uF to AGND`；`amplifier=U1 BE8002D`；`supply=VDD_5V`；`output=P2 SPK+/SPK-`
- 证据：图 7f3de88f0265 / 第 1 页 / A2-A3，HPOUT_L、C4/R3、U1 BE8002D、R4、SPK+/SPK-、P2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module ASR 架构 | `voice_chip=U4 CI1302`；`microphone=MK1 GMI4527P-2C-32db`；`speaker_amplifier=U1 BE8002D`；`speaker=P2 SPK`；`usb_uart=J1/U2 CH340N/U3`；`host_bus=J3 M5_BUS`；`extension=P1 EXTIO` |
| 系统结构 | V0.4 电源回路版本 | `schematic_revision=V0.4`；`revision_note=BUS_5V merged into Q1 MOS power path; reset disconnects BUS_5V and USB_5V supply` |
| 核心器件 | U4 CI1302 外围引脚 | `reference=U4`；`part_number=CI1302`；`uart1=pin9 PA2/TX1; pin10 PA3/RX1`；`uart0=pin14 PB5/TX0; pin15 PB6/RX0`；`audio_output=pin17 HPOUT_L`；`microphone=pins18-22`；`power=pins1-4; pin23`；`ground=pins5/8/24` |
| 电源 | BUS_5V 与 USB_5V 合路 | `bus_path=BUS_5V -> D3 DSK34`；`usb_path=USB_5V -> D1 1N5819WS`；`switch=Q1 CJ3401`；`output=VDD_5V`；`reverse_isolation=true` |
| 复位 | Q1 电源复位断电 | `mosfet=Q1 CJ3401`；`gate_pulldown=R10 100KΩ`；`gate_protection=D2 LESD5Z5.0T1G`；`button_series_resistor=R7 10KΩ`；`effect=disconnect VDD_5V input sources` |
| 电源 | CI1302 电源轨与去耦 | `vin5v=VDD_5V -> R16 4.7Ω -> U4 pin2`；`vin5v_caps=C14 4.7uF; C15 10uF`；`avdd_cap=C13 4.7uF`；`vdd33=U4 pin3 VDD_3V3; C19 4.7uF`；`vdd11=U4 pin4 VDD_1V1; C20 4.7uF`；`vcm_cap=C18 10uF`；`vdd5_cap=C3 10uF` |
| 电源 | GND 与 AGND 连接 | `bridge=R11 0Ω`；`digital_ground=GND`；`analog_ground=AGND` |
| 音频 | MK1 模拟麦克风链 | `microphone=MK1 GMI4527P-2C-32db`；`positive_path=MICPL -> C6 100nF -> MIC1+`；`bias=MICBIAS -> R14 2.2KΩ -> MIC1+`；`negative_path=MICNL -> C7 100nF -> MIC1-`；`negative_bias=MIC1- -> R17 2.2KΩ -> AGND` |
| 音频 | MICPR/MICNR 可见性 | `used_inputs=MICPL pin21; MICNL pin20`；`unused_on_page=MICPR pin18; MICNR pin19` |
| 音频 | HPOUT_L 到差分扬声器 | `source=U4 pin17 HPOUT_L`；`input_network=C4 100nF; R3 4.7KΩ`；`feedback=R4 33KΩ from SPK-`；`bypass=C1 1uF to AGND`；`amplifier=U1 BE8002D`；`supply=VDD_5V`；`output=P2 SPK+/SPK-` |
| GPIO 与控制信号 | PA6/SPK_SD 功放控制与蓝色 LED | `mcu_pin=U4 pin13 PA6/SPK_SD`；`amplifier_pin=U1 pin1 SHUTDOWN`；`pullup=R1 10KΩ to VDD_3V3`；`indicator=VDD_3V3 -> R2 10KΩ -> D4 Blue 0603 -> PA6/SPK_SD` |
| 接口 | USB Type-C 电源与数据 | `connector=J1 TYPE-C 16P`；`usb_dp=DP1/DP2 -> USB_D_P`；`usb_dn=DN1/DN2 -> USB_D_N`；`cc_resistors=R8/R9 5.1KΩ to GND`；`vbus_fuse=F1 0805 1A/6V`；`rail=USB_5V` |
| 接口 | U2 CH340N 升级串口 | `usb=pins1/2 USB_D_P/USB_D_N`；`supply=pin5 USB_5V`；`supply_caps=C9 100nF; C10 10uF`；`v3_cap=C8 100nF`；`uart=pin7 RXD via R5 100Ω; pin6 TXD via R6 100Ω`；`ground=pins3/4` |
| 接口 | CI1302 UART0 数据源切换 | `common_rx=U4 PB6/RX0 -> U3 D+`；`common_tx=U4 PB5/TX0 -> U3 D-`；`host_pair=UART_TXD/UART_RXD`；`usb_pair=CH340_TXD/CH340_RXD`；`selector=U3 pin2 S via R12 10KΩ USB_5V and R13 100KΩ GND`；`enable=OE# pin10 GND`；`supply=VDD_3V3` |
| 接口 | SW1/SW2 UART GPIO 选择 | `rx_options=SW1-1 GPIO34; SW1-2 GPIO13; SW1-3 GPIO16; SW1-4 GPIO3`；`tx_options=SW2-1 GPIO12; SW2-2 GPIO15; SW2-3 GPIO17; SW2-4 GPIO1` |
| 接口 | J3 UART 候选与电源针脚 | `uart_candidates=13 GPIO1; 14 GPIO3; 15 GPIO17; 16 GPIO16; 21 GPIO13; 22 GPIO12; 24 GPIO15; 25 GPIO34`；`ground=pins2/4/6`；`bus_3v3=pin11`；`bus_5v=pin27`；`hpwr=pins26/28/30` |
| 接口 | P1 EXTIO 逐针映射 | `pin1=PA2/TX1`；`pin2=PA3/RX1`；`pin3=PA5`；`pin4=PA4`；`pin5=PC4`；`pin6=GND`；`pin7=BUS_3V3`；`pin8=BUS_5V` |
| 电源 | USB_5V 与 M5-Bus 5V 边界 | `bus_input=J3 pin27 BUS_5V -> D3`；`usb_input=J1/F1 USB_5V -> D1`；`local_output=VDD_5V`；`usb_to_bus_path=false` |
| 时钟 | CI1302 外部时钟可见性 | `xin=U4 pin6 no external connection`；`xout=U4 pin7 no external connection`；`external_clock_visible=false`；`frequency_visible=false` |
| 内存与 Flash | 外部存储器可见性 | `external_flash_visible=false`；`external_eeprom_visible=false`；`external_ram_visible=false`；`sd_interface_visible=false` |
| 保护电路 | USB 与电源保护 | `vbus_fuse=F1 0805 1A/6V`；`cc_resistors=R8/R9 5.1KΩ`；`gate_protection=D2 LESD5Z5.0T1G`；`usb_data_esd_visible=false`；`m5bus_signal_esd_visible=false` |
| 接口 | 默认 UART 115200@8N1 | `documented_baud=115200`；`documented_format=8N1`；`hardware_uarts=UART0; UART1; CH340 UART`；`firmware_version=null` |
| 接口 | M5-Bus UART 管脚表方向与针脚冲突 | `schematic_rx_pins=25; 21; 16; 14`；`schematic_tx_pins=22; 24; 15; 13`；`documented_rx_pins=13; 15; 22; 26`；`documented_tx_pins=14; 16; 21; 23` |
| 音频 | 扬声器 8Ω@0.8W 规格 | `documented_impedance=8Ω`；`documented_power=0.8W`；`schematic_reference=P2 SPK`；`speaker_part_number=null` |
| 音频 | AEC、语音打断与离线识别性能 | `documented_aec=true`；`documented_noise_reduction=true`；`documented_barge_in=true`；`algorithm_version=null`；`test_conditions=null` |
| 其他事实 | 命令词、语言与唤醒方式 | `documented_factory_commands=53`；`documented_max_commands=300`；`documented_languages=Chinese; English; Japanese; Korean`；`documented_wake_methods=voice keyword; UART`；`firmware_image=not identified on schematic` |
| 音频 | 唤醒距离 | `documented_40db_distance=6.4m`；`documented_54db_distance=1.8m`；`test_method_visible=false` |
| 电源 | 5V 工作电流 | `documented_standby=5V@52.14mA`；`documented_low_volume=5V@43.38mA`；`documented_mid_volume=5V@85.26mA`；`documented_high_volume=5V@161.34mA` |
| 其他事实 | 尺寸与重量 | `documented_product_size=54.0 x 54.0 x 13.1mm`；`documented_product_weight=15.2g`；`documented_package_size=132.0 x 95.0 x 13.1mm`；`documented_gross_weight=28.9g` |
| 其他事实 | V0.4 与 M147 量产版本对应关系 | `schematic_revision=V0.4`；`schematic_date=2025-07-10`；`sku=M147`；`pcb_revision=null`；`bom_revision=null` |

## 待确认事项

- `interface.documented-uart-format`：产品正文给出默认 UART 115200@8N1；原理图确认 UART0、UART1、CH340N、U3 和 SW1/SW2 的硬件路径，但未标波特率、数据位、校验位、停止位或固件版本。（证据：图 7f3de88f0265 / 第 1 页 / U4 UART0/UART1、U2/U3 与 SW1/SW2，无串口格式文本）
- `interface.documented-uart-pin-direction`：原理图 SW1/SW2 明确把 UART_RXD 连接 pins25/21/16/14，把 UART_TXD 连接 pins22/24/15/13；产品管脚表则把 UART_RX 标在 pins13/15/22/26、UART_TX 标在 pins14/16/21/23。两者既存在收发视角差异，也在第四组候选针脚上不一致。（证据：图 7f3de88f0265 / 第 1 页 / A4 SW1/SW2 与 D4 J3 pin13/14/15/16/21/22/24/25 网络）
- `audio.documented-speaker-rating`：规格表称腔体喇叭为 8Ω@0.8W，原理图 P2 只标 SPK 并给出 SPK+/SPK-，没有阻抗、额定功率、腔体型号或声学参数。（证据：图 7f3de88f0265 / 第 1 页 / A3，P2 仅标 Speaker/SPK 与 SPK+/SPK-）
- `audio.documented-aec-behavior`：产品正文宣称 AEC 回声消除、降噪和识别过程中的中途语音打断；原理图确认麦克风与扬声器硬件链，但没有算法配置、AEC 参考信号、模型版本、噪声条件或打断时序。（证据：图 7f3de88f0265 / 第 1 页 / CI1302、MK1 与 Speaker 硬件链，无算法或性能参数）
- `other.documented-command-firmware`：产品正文称出厂预设 53 条英文命令、最多支持 300 条命令词、可自定义中英日韩识别词，并可由语音关键词或 UART 唤醒；这些均未由原理图中的器件连接直接定义。（证据：图 7f3de88f0265 / 第 1 页 / U4 CI1302 与 UART/USB 升级硬件，无命令词或语言文本）
- `audio.documented-wake-distance`：规格表给出环境噪音 40dB 时 6.4m、54dB 时 1.8m 的唤醒距离；原理图没有声场、麦克风安装、固件阈值或测试方法，不能由电路连接确认这些距离。（证据：图 7f3de88f0265 / 第 1 页 / MK1/CI1302 电路无声学距离或测试条件）
- `power.documented-consumption`：规格表给出待机 5V@52.14mA，以及小/中/大音量 5V@43.38mA、85.26mA、161.34mA；原理图只确认供电拓扑，没有测试点、固件状态、扬声器负载、音量定义或测量条件。（证据：图 7f3de88f0265 / 第 1 页 / BUS_5V/USB_5V/VDD_5V 与音频电路，无电流或测试条件）
- `other.documented-mechanics`：产品正文列出产品尺寸 54.0 x 54.0 x 13.1mm、产品重量 15.2g、包装尺寸 132.0 x 95.0 x 13.1mm 和毛重 28.9g；当前电气原理图未包含这些机械参数。（证据：图 7f3de88f0265 / 第 1 页 / 电气原理图整页未标机械尺寸或重量）
- `other.revision-applicability`：资源文件和页内注释标识 V0.4，文件名含 20250710，但页面没有 BOM 版本、PCB 版本、量产批次或工程变更编号，V0.4 对当前 M147 量产硬件的适用范围需要版本化资料确认。（证据：图 7f3de88f0265 / 第 1 页 / C2 V0.4迭代说明与整页无 PCB/BOM/量产批次对应表）
- `review.uart-format`：请用 M147 当前固件和 UART 协议确认默认 115200@8N1、流控与可配置范围。；原因：原理图只确认 UART 硬件链，不包含串口格式或固件版本。
- `review.uart-pin-direction`：请以 PCB 网表和主机/模块方向约定复核 M5-Bus UART 收发命名，并确认第四组候选是 pins24/25 还是正文所列 pins23/26。；原因：原理图与产品管脚表的收发方向和第四组针脚不一致。
- `review.speaker-rating`：请用 P2 扬声器 BOM、声学结构图和 BE8002D 设计资料确认 8Ω@0.8W 规格及安全驱动条件。；原因：原理图只标 P2 SPK 与差分网络，不列阻抗或额定功率。
- `review.aec-behavior`：请用 CI1302 固件配置、模型版本和测试报告确认 AEC、降噪及中途语音打断能力与适用条件。；原因：硬件图没有算法版本、AEC 参考配置或测试条件。
- `review.command-firmware`：请用 M147 出厂固件、命令表和自定义固件工具确认 53/300 条命令、四种语言及语音/UART 唤醒范围。；原因：这些属于固件内容，原理图没有命令词或语言配置。
- `review.wake-distance`：请提供 40dB/54dB 环境下 6.4m/1.8m 唤醒距离的测试方法、麦克风安装、声源和固件阈值。；原因：电气原理图无法验证声学距离性能。
- `review.power-consumption`：请用量产 M147、规定扬声器负载和固件状态复测待机及三档音量的 5V 电流。；原因：原理图没有定义测量边界、工作状态或音量测试条件。
- `review.mechanics`：请用 M147 正式尺寸图、称重记录和包装规范复核产品与包装尺寸、重量。；原因：当前证据为电气原理图，不包含机械规格。
- `review.revision-applicability`：请用版本化 PCB、BOM 和工程变更记录确认 V0.4/2025-07-10 图纸适用的 M147 量产批次。；原因：页面没有 V0.4 与 PCB/BOM/量产批次的对应表。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7f3de88f0265df4ddf2dfa6d767f9b04f1caddc0c0eee80fe73e0ab6d1e0e833` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/SCH_Module_ASR_SCH_Main_V0.4_20250710_2025_07_10_10_30_34_page_01.png` |

---

源文档：`zh_CN/module/Module_ASR.md`

源文档 SHA-256：`223c409c3f50fa8574197e5fb9cb16d4a1138e1a644a96e38e4d0085eadb8090`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
