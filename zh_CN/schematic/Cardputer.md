# Cardputer 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cardputer |
| SKU | K132 |
| 产品 ID | `cardputer-ee2733259184` |
| 源文档 | `zh_CN/core/Cardputer.md` |

## 概述

Cardputer 由 Stamp-S3M/ESP32-S3FN8 主控页、两页 Cardputer 主板和独立电池 Base 组成，连接 56 键矩阵、SPI microSD、SPI LCD、PDM 麦克风、NS4168 I2S 功放、WS2812、红外和 Grove 接口。主板 TP4057 负责电池充电，SY7088 生成 +5VOUT，SY8089 生成 +3.3V，Stamp-S3 内部 MIUN3CAD01-SC 再从 VIN_5V 生成 VDD_3V3。Stamp-S3 页还包含原生 USB Type-C、40MHz 晶体、PROANT440 射频、LCD 背光开关和 BOOT/复位网络。

## 检索关键词

`Cardputer`、`K132`、`Stamp-S3M`、`ESP32-S3FN8`、`TP4057`、`CN809J`、`SY7088`、`SY8089`、`MIUN3CAD01-SC`、`SPM1423HM4H-B`、`NS4168`、`74HC138`、`WS2812`、`microSD`、`TF-015`、`SPI`、`I2S`、`PDM`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`PROANT440`、`40MHz`、`VBAT_IN`、`VBAT_OUT`、`+5VIN`、`+5VOUT`、`+3.3V`、`VDD_3V3`、`G10 battery ADC`、`G12 SD_CS`、`G14 SD_MOSI`、`G40 SD_CLK`、`G39 SD_MISO`、`G46 MIC_DAT`、`G43 MIC_CLK`、`G41 BCLK`、`G42 SDATA`、`G44 IR`、`G38 DISP_BL`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1/P1/P2 (main) | STAMP-S3-DIP-1.27 | Stamp-S3 主控模组与 Cardputer 主板的双排连接界面 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 D2-D3：M1 STAMP-S3-DIP-1.27 与 P1/P2 |
| U1 (charger) | TP4057 | 以 +5VIN 为输入的单节锂电池充电器 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A1：U1 TP4057、R1/R5、C1、VBAT_IN |
| U3 | CN809J | 监测 +5VIN 并控制 Q1 电源路径的复位监控器 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A2：U3 CN809J RESET 与 Q1 gate |
| Q1,Q2,Q3 | LP3218DT1G | 电池/USB 电源路径与滑动开关切换 MOSFET | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A2-B2：Q1/Q2/Q3 LP3218DT1G、SW1、VBAT_IN/OUT |
| U2 (boost) | SY7088 | VBAT_OUT 到 +5VOUT 的升压转换器 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A3-A4：U2 SY7088、L1、R4/R6、D2 |
| U4 | SY8089 | VBAT_OUT 到 +3.3V 的降压转换器 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 B3-B4：U4 SY8089、L2、R11/R13 |
| U5 | SPM1423HM4H-B | G46 数据、G43 时钟的 PDM 麦克风 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 C2-C3：U5 SPM1423HM4H-B、R16/R17 |
| U6 | NS4168 | G43/G41/G42 三线数字音频输入到差分扬声器输出的功放 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 D3-D4：U6 NS4168、FB1-FB3、J4 |
| U7 | 74HC138 | 56 键矩阵的 3 线到 8 线扫描译码器 | 图 1437934f56e6 / 第 1 页 / 主板第 2 页网格 B1：U7 74HC138、R27-R34、Y0-Y7 |
| S1-S56 | SW-PB | 8 行乘 7 列的 56 键键盘矩阵 | 图 1437934f56e6 / 第 1 页 / 主板第 2 页网格 B2-D4：S1-S56 完整矩阵 |
| J3 | TF-015 | SPI microSD 卡座 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 D1-D2：J3 TF-015、R19-R22、D9-D13 |
| J2 (Grove) | HY-2.0_IIC | G1/G0、可切换 5V 和 GND 的四针扩展接口 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 C4：J2 HY-2.0_IIC、SW2、D6-D8 |
| IR1,R14 | IR LED / 22R/1% | G44 驱动的红外发射支路 | 图 357b7181a648 / 第 1 页 / 主板第 1 页网格 C3：G44-IR1-R14-GND |
| P1,F1 (base) | 2P@1.25 / Fuse 0805 6V 2A | Base 电池输入、保险丝和 VBAT 输出 | 图 cc14296e8216 / 第 1 页 / Base 页网格 B2-B3：P1、F1、VBAT、JP1-JP4 |
| U1 (Stamp-S3) | ESP32-S3FN8 | Stamp-S3 主控 SoC | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 A2-C2：U1 ESP32-S3FN8 |
| M2 (Stamp-S3) | MIUN3CAD01-SC | VIN_5V 到 VDD_3V3 的 Stamp-S3 电源转换器 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 D1-D2：M2 MIUN3CAD01-SC、R6/R17、C21/C22 |
| X1 (Stamp-S3) | 40MHz | ESP32-S3 主时钟晶体 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 B1：X1 40MHz、L3、C9/C14 |
| ANT1 (Stamp-S3) | PROANT440 | ESP32-S3 板载射频天线 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 A1：ANT1 PROANT440、L1、C1/C2 |
| J2 (Stamp-S3) | USB-TYPEC | 原生 USB 数据、电源和下载调试接口 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 D3-D4：J2 USB-TYPEC、F1、R1/R2、D3/D4/D14 |
| U2 (LCD) | SGM2578 / WS4622C-4/TR | G38/DISP_BL 控制的 LCD 背光负载开关 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 A3-A4：LCD 区 U2、J3/J1 |
| U3 (Stamp-S3) | WS2812 | GPIO21/SK_DIN 控制的 RGB LED | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 B3-B4：RGB LED 区 U3 |
| S1 (Stamp-S3) | SMT_SW_1TS026A | GPIO0 低有效 BOOT/用户按键 | 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 C3：BTN-USER 区 S1/R4/D1 |

## 系统结构

### Cardputer 系统架构

Cardputer 由 Stamp-S3M/ESP32-S3FN8 主控、主板电源与外设、56 键矩阵、Base 电池接口组成；主控连接 LCD、microSD、PDM 麦克风、NS4168 音频、IR、RGB、USB 和 Grove。

- 参数与网络：`controller=Stamp-S3M / ESP32-S3FN8`；`keyboard=74HC138 + S1-S56`；`storage=J3 TF-015`；`audio=SPM1423HM4H-B + NS4168`；`power=TP4057 + SY7088 + SY8089 + MIUN3CAD01-SC`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页完整单页; 图 1437934f56e6 / 第 1 页 / 主板第 2 页完整键盘矩阵; 图 cc14296e8216 / 第 1 页 / Base 完整单页; 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 完整单页

## 电源

### TP4057 电池充电

U1 TP4057 VCC pin4 经 R1 0.8Ω 接 +5VIN，BAT pin3 接 VBAT_IN，PROG pin6 经 R5 3.3KΩ 接地；C1/C6 各 10uF 分别为输入和电池侧去耦。

- 参数与网络：`charger=U1 TP4057`；`input=+5VIN via R1 0.8Ω`；`battery=VBAT_IN`；`program=R5 3.3KΩ`；`input_cap=C1 10uF`；`battery_cap=C6 10uF`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A1：U1/R1/R5/C1/C6

### 电池开关与电源路径

J1 BAT+/BAT- 接入 Q2/Q3 与 SW1，形成 VBAT_IN；Q1 由 U3 CN809J RESET 控制，将 VBAT_IN 接到 VBAT_OUT，D1 SS34 提供 +5VIN 到 VBAT_OUT 的二极管路径。

- 参数与网络：`battery_connector=J1 Header 2`；`switch=SW1 SW-SPDT`；`mosfets=Q1/Q2/Q3 LP3218DT1G`；`supervisor=U3 CN809J`；`input=VBAT_IN`；`output=VBAT_OUT`；`usb_path=+5VIN via D1 SS34`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A1-B3：J1/SW1/Q1-Q3/U3/D1

### +5VOUT 升压轨

U2 SY7088 由 VBAT_OUT 供电，L1 3015 1.5uH、R4 150KΩ/R6 47KΩ 和 D2 SS34 构成升压电路并输出 +5VOUT。

- 参数与网络：`converter=U2 SY7088`；`input=VBAT_OUT`；`inductor=L1 3015 1.5uH`；`feedback=R4 150KΩ; R6 47KΩ`；`diode=D2 SS34`；`output=+5VOUT`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 A3-A4：U2/L1/R4/R6/D2

### 主板 +3.3V 降压轨

U4 SY8089 从 VBAT_OUT 降压，LX 经 L2 3015 4.7uH 输出 +3.3V，反馈为 R11 68KΩ 与 R13 15KΩ。

- 参数与网络：`converter=U4 SY8089`；`input=VBAT_OUT`；`output=+3.3V`；`inductor=L2 3015 4.7uH`；`feedback=R11 68KΩ; R13 15KΩ`；`caps=C11 100nF; C12 22uF; C8 22uF; C9 100nF`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 B3-B4：U4/L2/R11/R13/C8/C9/C11/C12

### Stamp-S3 VDD_3V3

Stamp-S3 M2 MIUN3CAD01-SC 以 VIN_5V 为输入、EN 由 ESP_EN/R7/C23/D6 网络控制，VOUT 输出 VDD_3V3；反馈为 R6 100KΩ 与 R17 22.1KΩ。

- 参数与网络：`converter=M2 MIUN3CAD01-SC`；`input=VIN_5V`；`enable=ESP_EN via D6/R16`；`output=VDD_3V3`；`feedback=R6 100KΩ; R17 22.1KΩ`；`output_caps=C21/C22 10uF`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 D1-D2：DCDC 区 M2/R6/R17/C21/C22

### Base 电池与保险丝

Base P1 pin1 经 F1 Fuse 0805 6V 2A 输出 VBAT，pin2 接 GND；JP1/JP3 为 VBAT 测试点，JP2/JP4 为 GND 测试点。

- 参数与网络：`connector=P1 2P@1.25`；`positive=pin1 -> F1 -> VBAT`；`negative=pin2 GND`；`fuse=F1 0805 6V 2A`；`testpoints=JP1/JP3 VBAT; JP2/JP4 GND`
- 证据：图 cc14296e8216 / 第 1 页 / Base 页网格 B2-B3：P1/F1/JP1-JP4

## 接口

### LCD SPI 与背光

Stamp-S3 J3 引出 DISP_RST=GPIO33、DISP_RS=GPIO34、DISP_MOSI=GPIO35、DISP_SCK=GPIO36、DISP_CS=GPIO37；GPIO38 形成 DISP_BL 控制 U2 背光开关。

- 参数与网络：`reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight_enable=GPIO38 / DISP_BL`；`connector=J3 HDGC/0.5K-HX-8PWB/NC`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 A3-A4：LCD 区 U2/J3/J1 与 U1 GPIO33-GPIO38

### J2 HY2.0-4P Grove

主板原理图 J2 pin1=IIC_SCL/G1、pin2=IIC_SDA/G0、pin3=VCC、pin4=GND；SW2 可在 +5VOUT 与 +5VIN 之间选择 VCC。

- 参数与网络：`pin1=G1 / IIC_SCL`；`pin2=G0 / IIC_SDA`；`pin3=VCC selected by SW2`；`pin4=GND`；`power_options=+5VOUT or +5VIN`；`protection=D6/D7/D8 PESDNC2FD3V3B`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 C4：J2/SW2/C14/D6-D8

## 总线

### Stamp-S3 原生 USB

J2 Type-C DP1/DP2 经共模器件形成 USB_D_P 并接 U1 GPIO20，DN1/DN2 形成 USB_D_N 并接 GPIO19；CC1/CC2 由 R1/R2 5.1KΩ 下拉。

- 参数与网络：`dp=J2 DP1/DP2 -> USB_D_P -> GPIO20`；`dm=J2 DN1/DN2 -> USB_D_N -> GPIO19`；`cc=R1/R2 5.1KΩ to GND`；`controller=ESP32-S3FN8 native USB`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 D3-D4：J2/R1/R2 与 U1 GPIO19/20

## GPIO 与控制信号

### 56 键矩阵扫描

U7 74HC138 的 A0/A1/A2 分别接 G8/G9/G11，Y0-Y7 各经 R34-R27 22Ω 驱动八条扫描线；七条检测线为 G7/G6/G5/G4/G3/G15/G13，共形成 8x7 的 S1-S56 矩阵。

- 参数与网络：`decoder=U7 74HC138`；`address=A0=G8; A1=G9; A2=G11`；`scan=Y0-Y7 via R34-R27 22Ω`；`sense=G7,G6,G5,G4,G3,G15,G13`；`keys=56`；`matrix=8x7`
- 证据：图 1437934f56e6 / 第 1 页 / 主板第 2 页完整 U7 与 S1-S56 矩阵

### IR、RGB 与按键

主板 G44 经 IR1/R14 22Ω 驱动红外；Stamp-S3 GPIO21 形成 SK_DIN 驱动 U3 WS2812；Stamp-S3 S1 将 GPIO0 拉低，主板 BTN1 将 EN 拉低、BTN2 将 G0 拉低。

- 参数与网络：`ir=G44 -> IR1 -> R14 22Ω -> GND`；`rgb=GPIO21 -> SK_DIN -> U3 WS2812`；`stamp_button=S1 GPIO0 low`；`main_reset=BTN1 EN low`；`main_boot=BTN2 G0 low`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页 BTN1/BTN2 与 IR1; 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页 U3 RGB 与 BTN-USER S1

## 时钟

### Stamp-S3 40MHz 时钟

X1 40MHz 连接 U1 XTAL_P/XTAL_N，XTAL_P 支路串 L3 10nH，C9 10pF 与 C14 12pF 对地。

- 参数与网络：`crystal=X1 40MHz`；`series=L3 10nH`；`loads=C9 10pF; C14 12pF`；`pins=U1 XTAL_P pin54; XTAL_N pin53`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 B1：X1/L3/C9/C14

## 保护电路

### 外部接口保护

microSD 信号使用 D9-D13 PESDNC2FD3V3B；Grove 使用 D6-D8；Stamp-S3 USB D+/D- 使用 D3/D4，VBUS 使用 D14，并由 F1 6V/1A/PPTC 过流保护。

- 参数与网络：`microsd=D9-D13 PESDNC2FD3V3B`；`grove=D6-D8 PESDNC2FD3V3B`；`usb_data=D3/D4 PESDNC2FD3V3B`；`usb_vbus=D14 PESDNC2FD5VB`；`usb_fuse=F1 6V/1A/PPTC`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页 J3/J2 周围 ESD 阵列; 图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页 Type-C USB 区 D3/D4/D14/F1

## 存储

### microSD SPI 连接

J3 TF-015 以 G12=CS、G14=MOSI、G40=CLK、G39=MISO 连接 Stamp-S3，各信号串 R19-R22 33Ω，卡座由 +3.3V 供电。

- 参数与网络：`socket=J3 TF-015`；`cs=G12 via R19 33Ω`；`mosi=G14 via R20 33Ω`；`clk=G40 via R21 33Ω`；`miso=G39 via R22 33Ω`；`supply=+3.3V`；`bus=SPI`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 D1-D2：J3/R19-R22/D9-D13

## 内存与 Flash

### ESP32-S3FN8 存储可见性

Stamp-S3 U1 标为 ESP32-S3FN8，VDD_SPI pin29 接 FLASH_VCC，SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID pins30-35 未连接，页面未画外部 Flash 或 PSRAM。

- 参数与网络：`soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`psram_shown=false`；`unused_pins=30-35`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页 U1 pin29 与 pins30-35

## 音频

### PDM 麦克风

U5 SPM1423HM4H-B DAT pin5 经 R16 33Ω 接 G46，CLK pin4 经 R17 33Ω 接 G43，3V3 pin6 接 +3.3V，SELECT 与 GND 接地。

- 参数与网络：`data=G46 via R16 33Ω`；`clock=G43 via R17 33Ω`；`supply=+3.3V`；`select=GND`；`interface=PDM`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 C2-C3：U5/R16/R17/C13

### NS4168 数字音频功放

U6 NS4168 LRCLK pin2 经 R23 33Ω 接 G43，BCLK pin3 经 R24 33Ω 接 G41，SDATA pin4 经 R25 33Ω 接 G42；VOP/VON 经 FB2/FB3 1000Ω/MB 输出到 J4。

- 参数与网络：`lrclk=G43 via R23 33Ω`；`bclk=G41 via R24 33Ω`；`sdata=G42 via R25 33Ω`；`amplifier=U6 NS4168`；`outputs=VON/VOP via FB2/FB3 to J4`；`supply=+3.3V via FB1 120Ω/MB`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 D3-D4：U6/R23-R26/FB1-FB3/J4

## 射频

### Stamp-S3 板载天线

U1 LNA_IN 经 L1 2.2nH 连接 ANT1 PROANT440，C1 2.2pF 与 C2 2.0pF 对地构成匹配网络。

- 参数与网络：`antenna=ANT1 PROANT440`；`series=L1 2.2nH`；`shunt=C1 2.2pF; C2 2.0pF`；`soc_pin=U1 LNA_IN`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 A1：ANT1/L1/C1/C2

## 调试与烧录

### Stamp-S3 UART0

U1 U0TXD pin49 经 R5 510Ω/1% 形成 TX，U0RXD pin50 形成 RX，并通过 Stamp-S3M M1 pins26/24 引出。

- 参数与网络：`tx=U0TXD pin49 -> R5 510Ω -> TX -> M1 pin26`；`rx=U0RXD pin50 -> RX -> M1 pin24`；`interface=UART0`
- 证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页网格 C2-C4：U1 TX/RX 与 M1

## 模拟电路

### G10 电池电压检测

VBAT_IN 经 R8 100KΩ 与 R12 100KΩ 分压，中心点形成 G10，并由 C10 100nF 对地滤波。

- 参数与网络：`source=VBAT_IN`；`adc_net=G10`；`divider=R8 100KΩ / R12 100KΩ`；`filter=C10 100nF`
- 证据：图 357b7181a648 / 第 1 页 / 主板第 1 页网格 B2：R8/R12/C10/G10

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cardputer 系统架构 | `controller=Stamp-S3M / ESP32-S3FN8`；`keyboard=74HC138 + S1-S56`；`storage=J3 TF-015`；`audio=SPM1423HM4H-B + NS4168`；`power=TP4057 + SY7088 + SY8089 + MIUN3CAD01-SC` |
| 电源 | TP4057 电池充电 | `charger=U1 TP4057`；`input=+5VIN via R1 0.8Ω`；`battery=VBAT_IN`；`program=R5 3.3KΩ`；`input_cap=C1 10uF`；`battery_cap=C6 10uF` |
| 电源 | 电池开关与电源路径 | `battery_connector=J1 Header 2`；`switch=SW1 SW-SPDT`；`mosfets=Q1/Q2/Q3 LP3218DT1G`；`supervisor=U3 CN809J`；`input=VBAT_IN`；`output=VBAT_OUT`；`usb_path=+5VIN via D1 SS34` |
| 模拟电路 | G10 电池电压检测 | `source=VBAT_IN`；`adc_net=G10`；`divider=R8 100KΩ / R12 100KΩ`；`filter=C10 100nF` |
| 电源 | +5VOUT 升压轨 | `converter=U2 SY7088`；`input=VBAT_OUT`；`inductor=L1 3015 1.5uH`；`feedback=R4 150KΩ; R6 47KΩ`；`diode=D2 SS34`；`output=+5VOUT` |
| 电源 | 主板 +3.3V 降压轨 | `converter=U4 SY8089`；`input=VBAT_OUT`；`output=+3.3V`；`inductor=L2 3015 4.7uH`；`feedback=R11 68KΩ; R13 15KΩ`；`caps=C11 100nF; C12 22uF; C8 22uF; C9 100nF` |
| 电源 | Stamp-S3 VDD_3V3 | `converter=M2 MIUN3CAD01-SC`；`input=VIN_5V`；`enable=ESP_EN via D6/R16`；`output=VDD_3V3`；`feedback=R6 100KΩ; R17 22.1KΩ`；`output_caps=C21/C22 10uF` |
| 电源 | Base 电池与保险丝 | `connector=P1 2P@1.25`；`positive=pin1 -> F1 -> VBAT`；`negative=pin2 GND`；`fuse=F1 0805 6V 2A`；`testpoints=JP1/JP3 VBAT; JP2/JP4 GND` |
| 电源 | 120mAh 与 1400mAh 电池容量 | `documented_main=120mAh`；`documented_base=1400mAh`；`capacity_shown=false` |
| 存储 | microSD SPI 连接 | `socket=J3 TF-015`；`cs=G12 via R19 33Ω`；`mosi=G14 via R20 33Ω`；`clk=G40 via R21 33Ω`；`miso=G39 via R22 33Ω`；`supply=+3.3V`；`bus=SPI` |
| 音频 | PDM 麦克风 | `data=G46 via R16 33Ω`；`clock=G43 via R17 33Ω`；`supply=+3.3V`；`select=GND`；`interface=PDM` |
| 音频 | NS4168 数字音频功放 | `lrclk=G43 via R23 33Ω`；`bclk=G41 via R24 33Ω`；`sdata=G42 via R25 33Ω`；`amplifier=U6 NS4168`；`outputs=VON/VOP via FB2/FB3 to J4`；`supply=+3.3V via FB1 120Ω/MB` |
| GPIO 与控制信号 | 56 键矩阵扫描 | `decoder=U7 74HC138`；`address=A0=G8; A1=G9; A2=G11`；`scan=Y0-Y7 via R34-R27 22Ω`；`sense=G7,G6,G5,G4,G3,G15,G13`；`keys=56`；`matrix=8x7` |
| 接口 | LCD SPI 与背光 | `reset=GPIO33`；`dc=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`cs=GPIO37`；`backlight_enable=GPIO38 / DISP_BL`；`connector=J3 HDGC/0.5K-HX-8PWB/NC` |
| 核心器件 | LCD 型号与分辨率 | `documented_driver=ST7789V2`；`documented_size=1.14 inch`；`documented_resolution=240x135`；`schematic_panel_model_shown=false` |
| 接口 | J2 HY2.0-4P Grove | `pin1=G1 / IIC_SCL`；`pin2=G0 / IIC_SDA`；`pin3=VCC selected by SW2`；`pin4=GND`；`power_options=+5VOUT or +5VIN`；`protection=D6/D7/D8 PESDNC2FD3V3B` |
| 接口 | Grove GPIO 文档映射冲突 | `schematic=pin1 G1; pin2 G0`；`document=G2/G1` |
| GPIO 与控制信号 | IR、RGB 与按键 | `ir=G44 -> IR1 -> R14 22Ω -> GND`；`rgb=GPIO21 -> SK_DIN -> U3 WS2812`；`stamp_button=S1 GPIO0 low`；`main_reset=BTN1 EN low`；`main_boot=BTN2 G0 low` |
| 总线 | Stamp-S3 原生 USB | `dp=J2 DP1/DP2 -> USB_D_P -> GPIO20`；`dm=J2 DN1/DN2 -> USB_D_N -> GPIO19`；`cc=R1/R2 5.1KΩ to GND`；`controller=ESP32-S3FN8 native USB` |
| 时钟 | Stamp-S3 40MHz 时钟 | `crystal=X1 40MHz`；`series=L3 10nH`；`loads=C9 10pF; C14 12pF`；`pins=U1 XTAL_P pin54; XTAL_N pin53` |
| 射频 | Stamp-S3 板载天线 | `antenna=ANT1 PROANT440`；`series=L1 2.2nH`；`shunt=C1 2.2pF; C2 2.0pF`；`soc_pin=U1 LNA_IN` |
| 内存与 Flash | ESP32-S3FN8 存储可见性 | `soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`psram_shown=false`；`unused_pins=30-35` |
| 内存与 Flash | 8MB Flash 容量 | `documented_capacity=8MB`；`soc=ESP32-S3FN8`；`capacity_text_shown=false` |
| 调试与烧录 | Stamp-S3 UART0 | `tx=U0TXD pin49 -> R5 510Ω -> TX -> M1 pin26`；`rx=U0RXD pin50 -> RX -> M1 pin24`；`interface=UART0` |
| 保护电路 | 外部接口保护 | `microsd=D9-D13 PESDNC2FD3V3B`；`grove=D6-D8 PESDNC2FD3V3B`；`usb_data=D3/D4 PESDNC2FD3V3B`；`usb_vbus=D14 PESDNC2FD5VB`；`usb_fuse=F1 6V/1A/PPTC` |

## 待确认事项

- `power.documented-battery-capacity`：产品正文写机身 120mAh、Base 1400mAh；四页原理图只显示 J1/P1 电池接口、电源路径和保险丝，没有容量字段。（证据：图 357b7181a648 / 第 1 页 / 主板第 1 页 J1 BAT+/BAT-，无容量字段; 图 cc14296e8216 / 第 1 页 / Base 页 P1/VBAT， 无容量字段）
- `component.lcd-panel-spec`：产品正文写 ST7789V2、1.14 inch、240x135；Stamp-S3 原理图只显示 J3/J1 显示连接器、SPI 网络和背光开关，未打印面板驱动器或分辨率。（证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页 LCD 区 J3/J1/U2，未见 ST7789V2 或 240x135）
- `interface.grove-document-conflict`：产品正文写 Grove 信号为 G2/G1，而主板原理图 J2 明确标为 G1/G0；当前硬件版本的软件映射需复核。（证据：图 357b7181a648 / 第 1 页 / 主板第 1 页 J2 IIC_SCL/IIC_SDA 与 G1/G0 标注）
- `memory.flash-capacity`：正文写 8MB Flash，原理图器件名为 ESP32-S3FN8，但未单独打印容量字段或存储 BOM。（证据：图 aaa7dbf40110 / 第 1 页 / Stamp-S3 页 U1/FLASH_VCC，未见独立容量字段）
- `review.battery-capacity`：K132 当前机身与 Base 电池容量是否固定为 120mAh 和 1400mAh？；原因：容量只出现在正文，原理图仅显示电池接口和保护路径。
- `review.lcd-spec`：K132 当前 LCD 是否固定为 ST7789V2、1.14 inch、240x135？；原因：Stamp-S3 原理图只画显示接口和背光电路，没有面板型号或分辨率。
- `review.grove-map`：K132 当前 Grove 软件映射应采用原理图 G1/G0 还是正文 G2/G1？；原因：产品正文与主板原理图的两根 Grove GPIO 标注冲突。
- `review.flash-capacity`：K132 当前 ESP32-S3FN8 的量产 Flash 容量是否固定为 8MB？；原因：原理图未单独打印容量字段或存储 BOM。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `357b7181a648833a1883c80e5e8602538ead24efac80074f1942f786b95b7d0a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer_sch_01.png` |
| 2 | 1 | `1437934f56e61ed90222d8a0ed70ed9f82264036223cdea685878320e4cacc12` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer_sch_02.png` |
| 3 | 1 | `cc14296e8216974859d827a0530ad8664109317a45da7f2a4a65ba35358fae35` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5cardputer_Base_01.png` |
| 4 | 1 | `aaa7dbf40110a4ec90c6f2dae371394bafe3c0894ae255aca506aba1b636899f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2_sch_01.png` |

---

源文档：`zh_CN/core/Cardputer.md`

源文档 SHA-256：`4e781f1bbc5b6ea5a18a7cb7bc2103b8db1c6a9350321b4ac12a3f3f36d595e8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
