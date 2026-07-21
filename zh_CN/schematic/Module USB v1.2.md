# Module USB v1.2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module USB v1.2 |
| SKU | M020-V12 |
| 产品 ID | `module-usb-v1-2-696c7d48b650` |
| 源文档 | `zh_CN/module/USB v1.2 Module.md` |

## 概述

Module USB v1.2 以 U1 MAX3421 为 USB/SPI 控制器，通过固定 MOSI/MISO/SCLK 与 J2 M5Stack_BUS 通信，SS 由 SW1 在 GPIO13/GPIO5/GPIO0 中选择，INT 由 SW2 在 GPIO35/GPIO34 中选择。J1 USB Type-A 的 D+/D- 经 33 Ω 电阻连接 U1，VBUS 经 D1 B5819W SL 供给接口；U1 由 M5-Bus +3.3 V 供电并使用 Y1 12 MHz 晶振。P1/P2 分别引出五路 GPIN/GPOUT、GND、3.3 V 和 VBUS，J3 提供 BAT/GND 两针电池座但页面未显示电池充电或负载路径。

## 检索关键词

`Module USB v1.2`、`M020-V12`、`MAX3421`、`MAX3421E`、`MAX3421EETJ+`、`USB_TYPE_A`、`USB_P`、`USB_N`、`VBUS`、`SPI`、`MOSI`、`MISO`、`SCLK`、`SS`、`INT`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO13`、`GPIO5`、`GPIO0`、`GPIO35`、`GPIO34`、`SW1`、`SW2`、`GPIN0`、`GPIN4`、`GPOUT0`、`GPOUT4`、`P1 Header 8`、`P2 Header 8`、`J3 BAT`、`12MHz`、`B5819W SL`、`R2/R4 33Ω`、`+3.3V`、`M5Stack_BUS`、`USB 2.0`、`USB host`、`USB peripheral`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX3421 | USB 控制器与 SPI 从设备，提供 USB D+/D-、GPIN/GPOUT、SS、INT/GPX 与 12 MHz 时钟接口 | 图 b233a8712e61 / 第 1 页 / B2-C3 U1 MAX3421 pins1-32 |
| J1 | USB_TYPE_A | VBUS、D-、D+ 与 GND 的标准 USB Type-A 连接器 | 图 b233a8712e61 / 第 1 页 / B1-C2 J1 USB_TYPE_A pins1-4 |
| SW1 | 未标注 | SS 到 GPIO13、GPIO5 或 GPIO0 的三路选择开关 | 图 b233a8712e61 / 第 1 页 / D2-D3 SW1 SS/GPIO13/GPIO5/GPIO0 |
| SW2 | 未标注 | INT 到 GPIO35 或 GPIO34 的两路选择开关 | 图 b233a8712e61 / 第 1 页 / D2-D3 SW2 INT/GPIO35/GPIO34 |
| P1 | Header 8 | GPIN0-GPIN4、GND、+3.3 V 与 VBUS 输入扩展排针 | 图 b233a8712e61 / 第 1 页 / A4 P1 Header 8 pins1-8 |
| P2 | Header 8 | GPOUT0-GPOUT4、GND、+3.3 V 与 VBUS 输出扩展排针 | 图 b233a8712e61 / 第 1 页 / B4 P2 Header 8 pins1-8 |
| J2 | M5Stack_BUS | 30 针主机接口，提供 VBUS、3.3 V、EN、SPI 及可选 SS/INT GPIO | 图 b233a8712e61 / 第 1 页 / C4-D4 J2 M5Stack_BUS pins1-30 |
| J3 | 未标注 | BAT 与 GND 两针锂电池座 | 图 b233a8712e61 / 第 1 页 / D4 J3 pins1 BAT/2 GND |
| Y1/C8/C9 | 12MHz / 18pF / 18pF | MAX3421 XI/XO 外部 12 MHz 晶振与负载电容 | 图 b233a8712e61 / 第 1 页 / C2-C3 U1 XI/XO/Y1/C8/C9 |
| D1 | B5819W SL | VBUS 电源轨到 USB Type-A pin1 的串联肖特基二极管 | 图 b233a8712e61 / 第 1 页 / B1-B2 VBUS/D1 B5819W SL/J1 pin1 |
| R2/R4 | 33Ω / 33Ω | USB D-/D+ 的串联阻尼电阻 | 图 b233a8712e61 / 第 1 页 / B1-C2 J1 D-/D+ through R2/R4 to USB_P/USB_N |

## 系统结构

### Module USB v1.2 系统架构

U1 MAX3421 通过 SPI 连接 J2 主机并控制 J1 USB Type-A，SW1/SW2 选择 SS/INT GPIO，P1/P2 扩展输入输出，J3 提供电池座。

- 参数与网络：`controller=U1 MAX3421`；`usb=J1 USB_TYPE_A`；`host=J2 M5Stack_BUS`；`bus=SPI`；`chip_select=SW1`；`interrupt=SW2`；`gpio=P1 GPIN; P2 GPOUT`；`battery=J3 BAT/GND`
- 证据：图 b233a8712e61 / 第 1 页 / 整页 U1/J1/SW1/SW2/P1/P2/J2/J3

## 核心器件

### MAX3421 主要引脚分组

U1 GPIN0-GPIN7 为 pins26-32/1，GPOUT0-GPOUT7 为 pins4-11，D-/D+ pins20/21，XI/XO pins24/25，VCC/VL pins23/2，SPI SCLK/SS/MISO/MOSI pins13/14/15/16，INT pin18、GPX pin17、RES pin12。

- 参数与网络：`inputs=GPIN0-7 pins26-32/1`；`outputs=GPOUT0-7 pins4-11`；`usb=D- pin20; D+ pin21`；`clock=XI pin24; XO pin25`；`power=VCC pin23; VL pin2`；`spi=SCLK13; SS14; MISO15; MOSI16`；`control=INT18; GPX17; RES12`
- 证据：图 b233a8712e61 / 第 1 页 / U1 MAX3421 pin labels

## 电源

### USB Type-A VBUS 供电

M5-Bus J2 pin28 的 VBUS 经 D1 B5819W SL 串联到 J1 USB Type-A VBUS pin1；VBUS 配置 C6 100 nF、C7 2.2 uF、C5 100 uF 对地。

- 参数与网络：`source=J2 pin28 VBUS`；`diode=D1 B5819W SL`；`load=J1 pin1 VBUS`；`decoupling=C6 100nF; C7 2.2uF; C5 100uF`；`current_limit_switch=not shown`
- 证据：图 b233a8712e61 / 第 1 页 / B1-C2 VBUS/C5-C7/D1/J1 and J2 pin28

### MAX3421 3.3 V 供电

U1 VCC pin23 与 VL pin2 接 +3.3 V，C10 2.2 uF/C11 100 nF 去耦；页面没有板载 3.3 V 稳压器，电源来自 J2 pin12。

- 参数与网络：`vcc=U1 pin23 +3.3V`；`vl=U1 pin2 +3.3V`；`decoupling=C10 2.2uF; C11 100nF`；`source=J2 pin12 +3.3V`；`regulator=not shown`
- 证据：图 b233a8712e61 / 第 1 页 / C2-C3 U1 VCC/VL/C10/C11 and J2 +3.3V

## 接口

### 两针锂电池座

J3 pin1 接 BAT、pin2 接 GND；页面未显示 BAT 到 VBUS、3.3 V、充电器或 M5-Bus pin30 的有效连接。

- 参数与网络：`connector=J3`；`pin1=BAT`；`pin2=GND`；`charger=not shown`；`load_path=not shown`；`m5bus_battery=J2 pin30 marked no-connect`
- 证据：图 b233a8712e61 / 第 1 页 / D4 J3 BAT/GND and J2 pin30 BAT no-connect

### M5Stack_BUS 使用网络

J2 使用 pins1/3/5 GND、pin6 EN、pin7 GPIO23/MOSI、pin9 GPIO19/MISO、pin11 GPIO18/SCLK、pin12 +3.3 V、pins20/22/24 GPIO5/GPIO13/GPIO0 为 SS 候选、pins2/26 GPIO35/GPIO34 为 INT 候选、pin28 VBUS；pin30 BAT 未连接。

- 参数与网络：`ground=pins1/3/5`；`reset=pin6 EN`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 SCLK`；`3v3=pin12`；`ss=pin20 GPIO5; pin22 GPIO13; pin24 GPIO0`；`int=pin2 GPIO35; pin26 GPIO34`；`power=pin28 VBUS`；`battery=pin30 no-connect`
- 证据：图 b233a8712e61 / 第 1 页 / C4-D4 J2 M5Stack_BUS pins1-30

## 总线

### MAX3421 SPI 固定信号

U1 MOSI pin16 连接 J2 pin7/GPIO23，MISO pin15 连接 J2 pin9/GPIO19，SCLK pin13 连接 J2 pin11/GPIO18；SS 由 SW1 选择。

- 参数与网络：`device=U1 MAX3421`；`mosi=J2 pin7 GPIO23 -> U1 pin16`；`miso=U1 pin15 -> J2 pin9 GPIO19`；`clock=J2 pin11 GPIO18 -> U1 pin13`；`chip_select=U1 SS pin14 via SW1`；`level=+3.3V`
- 证据：图 b233a8712e61 / 第 1 页 / B3 U1 SPI pins and C4 J2 MOSI/MISO/SCLK

### MAX3421 USB D+/D-

J1 D- pin2 经 R2 33 Ω 形成 USB_P 并连接 U1 D- pin20；J1 D+ pin3 经 R4 33 Ω 形成 USB_N 并连接 U1 D+ pin21，网络命名与 D+/D- 极性文字相反。

- 参数与网络：`connector_dm=J1 pin2 D- -> R2 33Ω -> net USB_P -> U1 D- pin20`；`connector_dp=J1 pin3 D+ -> R4 33Ω -> net USB_N -> U1 D+ pin21`；`note=USB_P/USB_N net names do not match printed D-/D+ polarity`；`direction=bidirectional`
- 证据：图 b233a8712e61 / 第 1 页 / B1-C2 J1/R2/R4/USB_P/USB_N/U1 pins20/21

## GPIO 与控制信号

### SPI SS GPIO 选择

U1 SS pin14 连接 SW1 公共侧，可选择 GPIO13/J2 pin22、GPIO5/J2 pin20 或 GPIO0/J2 pin24。

- 参数与网络：`source=U1 SS pin14`；`switch=SW1`；`options=GPIO13 pin22; GPIO5 pin20; GPIO0 pin24`；`direction=host-to-controller`
- 证据：图 b233a8712e61 / 第 1 页 / D2-D3 SW1 SS/GPIO13/GPIO5/GPIO0 and J2

### USB 控制器 INT GPIO 选择

U1 INT pin18 连接 SW2 公共侧，可选择 GPIO35/J2 pin2 或 GPIO34/J2 pin26；INT 由 R3 2.2 kΩ 上拉至 3.3 V。

- 参数与网络：`source=U1 INT pin18`；`switch=SW2`；`options=GPIO35 pin2; GPIO34 pin26`；`pullup=R3 2.2KΩ to +3.3V`；`direction=controller-to-host`
- 证据：图 b233a8712e61 / 第 1 页 / B3 U1 INT/R3 and D2-D3 SW2/J2 GPIO35/GPIO34

### 五路 GPIN 扩展

P1 Header 8 pins1-5 分别连接 U1 GPIN0-GPIN4，pin6 GND、pin7 +3.3 V、pin8 VBUS；GPIN5-GPIN7 未引到 P1。

- 参数与网络：`connector=P1 Header 8`；`inputs=pins1-5 GPIN0-GPIN4`；`ground=pin6`；`3v3=pin7`；`vbus=pin8`；`internal_only=GPIN5-GPIN7`
- 证据：图 b233a8712e61 / 第 1 页 / A4 P1 and U1 GPIN0..7 bus

### 五路 GPOUT 扩展

P2 Header 8 pins1-5 分别连接 U1 GPOUT0-GPOUT4，pin6 GND、pin7 +3.3 V、pin8 VBUS；GPOUT5-GPOUT7 未引到 P2。

- 参数与网络：`connector=P2 Header 8`；`outputs=pins1-5 GPOUT0-GPOUT4`；`ground=pin6`；`3v3=pin7`；`vbus=pin8`；`internal_only=GPOUT5-GPOUT7`
- 证据：图 b233a8712e61 / 第 1 页 / B4 P2 and U1 GPOUT0..7 bus

## 时钟

### MAX3421 12 MHz 时钟

U1 XO pin25 与 XI pin24 连接 Y1 12 MHz 晶振，C8/C9 各 18 pF 对地。

- 参数与网络：`xo=U1 pin25`；`xi=U1 pin24`；`crystal=Y1 12MHz`；`load_caps=C8/C9 18pF to GND`
- 证据：图 b233a8712e61 / 第 1 页 / C2-C3 U1 XO/XI/Y1/C8/C9

## 复位

### MAX3421 复位

U1 RES pin12 连接 EN 网络与 J2 pin6，R1 10 kΩ 将 RES/EN 上拉到 +3.3 V。

- 参数与网络：`target=U1 RES pin12`；`net=EN`；`host=J2 pin6`；`pullup=R1 10KΩ to +3.3V`
- 证据：图 b233a8712e61 / 第 1 页 / B3 U1 RES/R1/EN and J2 pin6

## 保护电路

### USB 接口保护与限流

J1 USB D+/D- 路径只画 33 Ω 串联电阻，VBUS 只画 D1 肖特基；页面未显示 USB ESD/TVS 或专用限流负载开关。

- 参数与网络：`data_series=R2/R4 33Ω`；`vbus_diode=D1 B5819W SL`；`esd_tvs=not shown`；`current_limit=not shown`；`load_switch=not shown`
- 证据：图 b233a8712e61 / 第 1 页 / J1 USB data/VBUS paths

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module USB v1.2 系统架构 | `controller=U1 MAX3421`；`usb=J1 USB_TYPE_A`；`host=J2 M5Stack_BUS`；`bus=SPI`；`chip_select=SW1`；`interrupt=SW2`；`gpio=P1 GPIN; P2 GPOUT`；`battery=J3 BAT/GND` |
| 核心器件 | MAX3421 主要引脚分组 | `inputs=GPIN0-7 pins26-32/1`；`outputs=GPOUT0-7 pins4-11`；`usb=D- pin20; D+ pin21`；`clock=XI pin24; XO pin25`；`power=VCC pin23; VL pin2`；`spi=SCLK13; SS14; MISO15; MOSI16`；`control=INT18; GPX17; RES12` |
| 总线 | MAX3421 SPI 固定信号 | `device=U1 MAX3421`；`mosi=J2 pin7 GPIO23 -> U1 pin16`；`miso=U1 pin15 -> J2 pin9 GPIO19`；`clock=J2 pin11 GPIO18 -> U1 pin13`；`chip_select=U1 SS pin14 via SW1`；`level=+3.3V` |
| GPIO 与控制信号 | SPI SS GPIO 选择 | `source=U1 SS pin14`；`switch=SW1`；`options=GPIO13 pin22; GPIO5 pin20; GPIO0 pin24`；`direction=host-to-controller` |
| GPIO 与控制信号 | USB 控制器 INT GPIO 选择 | `source=U1 INT pin18`；`switch=SW2`；`options=GPIO35 pin2; GPIO34 pin26`；`pullup=R3 2.2KΩ to +3.3V`；`direction=controller-to-host` |
| 复位 | MAX3421 复位 | `target=U1 RES pin12`；`net=EN`；`host=J2 pin6`；`pullup=R1 10KΩ to +3.3V` |
| 时钟 | MAX3421 12 MHz 时钟 | `xo=U1 pin25`；`xi=U1 pin24`；`crystal=Y1 12MHz`；`load_caps=C8/C9 18pF to GND` |
| 总线 | MAX3421 USB D+/D- | `connector_dm=J1 pin2 D- -> R2 33Ω -> net USB_P -> U1 D- pin20`；`connector_dp=J1 pin3 D+ -> R4 33Ω -> net USB_N -> U1 D+ pin21`；`note=USB_P/USB_N net names do not match printed D-/D+ polarity`；`direction=bidirectional` |
| 电源 | USB Type-A VBUS 供电 | `source=J2 pin28 VBUS`；`diode=D1 B5819W SL`；`load=J1 pin1 VBUS`；`decoupling=C6 100nF; C7 2.2uF; C5 100uF`；`current_limit_switch=not shown` |
| 电源 | MAX3421 3.3 V 供电 | `vcc=U1 pin23 +3.3V`；`vl=U1 pin2 +3.3V`；`decoupling=C10 2.2uF; C11 100nF`；`source=J2 pin12 +3.3V`；`regulator=not shown` |
| GPIO 与控制信号 | 五路 GPIN 扩展 | `connector=P1 Header 8`；`inputs=pins1-5 GPIN0-GPIN4`；`ground=pin6`；`3v3=pin7`；`vbus=pin8`；`internal_only=GPIN5-GPIN7` |
| GPIO 与控制信号 | 五路 GPOUT 扩展 | `connector=P2 Header 8`；`outputs=pins1-5 GPOUT0-GPOUT4`；`ground=pin6`；`3v3=pin7`；`vbus=pin8`；`internal_only=GPOUT5-GPOUT7` |
| 接口 | 两针锂电池座 | `connector=J3`；`pin1=BAT`；`pin2=GND`；`charger=not shown`；`load_path=not shown`；`m5bus_battery=J2 pin30 marked no-connect` |
| 接口 | M5Stack_BUS 使用网络 | `ground=pins1/3/5`；`reset=pin6 EN`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 SCLK`；`3v3=pin12`；`ss=pin20 GPIO5; pin22 GPIO13; pin24 GPIO0`；`int=pin2 GPIO35; pin26 GPIO34`；`power=pin28 VBUS`；`battery=pin30 no-connect` |
| 保护电路 | USB 接口保护与限流 | `data_series=R2/R4 33Ω`；`vbus_diode=D1 B5819W SL`；`esd_tvs=not shown`；`current_limit=not shown`；`load_switch=not shown` |
| 核心器件 | MAX3421EETJ+ 完整型号 | `schematic_marking=MAX3421`；`document_variant=MAX3421EETJ+`；`previous_variant=MAX3421EEHJ+`；`confirmed_full_variant=null` |
| 总线 | USB 2.0 主机/外设模式 | `document_standard=USB 2.0`；`document_modes=host/peripheral`；`schematic_connector=USB Type-A`；`speed=not printed`；`mode_control=not shown` |
| 电源 | 锂电池供电功能 | `document_connector=1.25mm-2P lithium battery seat`；`schematic_connector=J3 BAT/GND`；`charger=not shown`；`system_power_path=not shown`；`protection=not shown` |
| 接口 | USB_P/USB_N 网络命名极性 | `printed_dm=J1 D- -> USB_P -> U1 D-`；`printed_dp=J1 D+ -> USB_N -> U1 D+`；`electrical_pin_pairing=D- to D-; D+ to D+`；`net_name_pairing=P/N reversed` |

## 待确认事项

- `component.full-variant`：产品版本说明称 v1.1 后使用 MAX3421EETJ+，原理图 U1 只标 MAX3421，未打印 EETJ+ 后缀或封装料号。（证据：图 b233a8712e61 / 第 1 页 / U1 marking MAX3421 only）
- `bus.usb-standard-modes`：产品正文称标准 USB 2.0 并支持主机/外设模式，原理图可确认 MAX3421 与 Type-A D+/D-，但未印协议版本、速度或模式配置。（证据：图 b233a8712e61 / 第 1 页 / U1/J1 USB path lacks mode/standard labels）
- `power.battery-function`：产品正文称板载锂电池座提升移动供电灵活性，但原理图 J3 BAT 只连接到座子本身，没有充电、升降压、保护或系统供电路径。（证据：图 b233a8712e61 / 第 1 页 / J3 isolated BAT/GND connector）
- `interface.usb-net-polarity`：页面把 J1 D- 经 R2 标为 USB_P、J1 D+ 经 R4 标为 USB_N，同时 U1 D-/D+ 分别接这两网；需要确认是网络命名笔误还是绘图极性错误。（证据：图 b233a8712e61 / 第 1 页 / J1 D-/D+, R2/R4, USB_P/USB_N, U1 pins20/21）
- `review.full-variant`：请用 v1.2 BOM 或 U1 丝印确认完整型号为 MAX3421EETJ+。；原因：原理图仅标 MAX3421，未给订货后缀。
- `review.usb-standard-modes`：请用确认后的 MAX3421E 规格与固件配置复核 USB 2.0 速度和主机/外设模式。；原因：原理图未标 USB 版本、速度或模式。
- `review.battery-function`：请用 PCB/BOM/完整电源图确认 J3 1.25 mm 电池座如何连接系统供电及是否具备充电保护。；原因：当前页面中 BAT 网络没有后续路径。
- `review.usb-net-polarity`：请用 PCB 网表或通断测量确认 USB_P/USB_N 只是命名互换，实际 D+/D- 极性未颠倒。；原因：原理图引脚连接与网络 P/N 名称相反。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b233a8712e61c4b1097264a25e7346d0e1a9362a9933ece4ce96f8ae2e322afb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/544/SCH_USBHost_V1.2_sch_01.png` |

---

源文档：`zh_CN/module/USB v1.2 Module.md`

源文档 SHA-256：`d70b5c7cc5c7ac9d2a6e668fee93ae85344bd45340ee19daf18fd682831699e1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
