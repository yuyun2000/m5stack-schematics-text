# Stamp-C5 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-C5 |
| SKU | S016 |
| 产品 ID | `stamp-c5-cb6d75715d18` |
| 源文档 | `zh_CN/core/Stamp-C5.md` |

## 概述

Stamp-C5 以 ESP32-C5HF4 为主控，USB Type-C 数据经 ICMF062P900MFR 滤波后直连片上 USB；TPS2116DRLR 在 USB_IN 与 VBAT 间进行电源选择，JW5712 生成 3.3V，SGM40567-4.2XG/TR 提供约 200mA 充电。2.4GHz 与 5GHz 射频经 LFD182G45DCHD481 双工器复用至 IPEX-1，11 路焊盘 GPIO 和 8 路 JP3/FPC GPIO 均有明确引出。资源文件名标 V0.3，但可见标题栏为 Revision V0.2。

## 检索关键词

`Stamp-C5`、`S016`、`ESP32-C5HF4`、`ESP32-C5`、`4MB Flash`、`USB Type-C`、`TYPEC-302-BRP16SC08`、`ICMF062P900MFR`、`TPS2116DRLR`、`JW5712`、`600mA`、`SGM40567-4.2XG/TR`、`200mA charge`、`LFD182G45DCHD481`、`2.4GHz`、`5GHz`、`IPEX-1`、`JP3 FPC 12P`、`G28_BOOT`、`G11_TXD`、`G12_RXD`、`CHG_STA`、`VSYS_3V3`、`VBAT`、`USB_IN`、`V0.2`、`V0.3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-C5HF4 | Stamp-C5 主控制器，集成 USB 与双频射频端口 | 图 c9956a9984d7 / 第 1 页 / B1-D5 ESP32-C5HF4 区域 U3 主控符号 |
| J1 | TYPEC-302-BRP16SC08 | USB Type-C 电源与数据接口 | 图 c9956a9984d7 / 第 1 页 / A1-A2 USBC IN 区域 J1 TYPEC-302-BRP16SC08 |
| FT1 | ICMF062P900MFR | USB D+/D- 共模滤波器 | 图 c9956a9984d7 / 第 1 页 / A1-A3 USBC_P/N 至 USB_P/N 之间 FT1 ICMF062P900MFR |
| U1 | TPS2116DRLR | USB_IN/VBAT 双输入电源选择器 | 图 c9956a9984d7 / 第 1 页 / A3-A4 U1 TPS2116DRLR、VIN1/VIN2 与 VBUS |
| U2 | JW5712 | VBUS 至 VSYS_3V3 降压转换器，图面标最大 600mA | 图 c9956a9984d7 / 第 1 页 / A5-A6 POWER 3V3 区域 U2 JW5712 与 MAX OUT I=600mA |
| U5 | SGM40567-4.2XG/TR | USB_IN 至 VBAT 单节电池充电器 | 图 c9956a9984d7 / 第 1 页 / A7-A8 Charge 区域 U5 SGM40567-4.2XG/TR |
| X1 | TJ1148000HYFBC | ESP32-C5 主晶振 | 图 c9956a9984d7 / 第 1 页 / B3-B4 X1 TJ1148000HYFBC 与 XTAL_P/N |
| U4 | LFD182G45DCHD481 | 2.4GHz/5GHz 双频双工器 | 图 c9956a9984d7 / 第 1 页 / C5-C7 U4 LFD182G45DCHD481，H_PORT/L_PORT 至 COM |
| J2 | IPEX_1 | 双频外部天线连接器 | 图 c9956a9984d7 / 第 1 页 / C7-C8 U4 COM 经 50R 网络连接 J2 IPEX_1 |
| JP1/JP2 | Stamp edge pads | 2.54mm 焊盘 GPIO、电源与 USB_IN 引出 | 图 c9956a9984d7 / 第 1 页 / B6-B7 CELL Header 区域 JP1/JP2 七针定义 |
| JP3 | 12-pin extension header/FPC footprint | 背部 12 针扩展接口电气定义 | 图 c9956a9984d7 / 第 1 页 / B7-B8 CELL Header 区域 JP3 1-12 脚 |
| D1/D2 | BLUE_LED/RED_LED | G28/BOOT 与充电状态指示灯 | 图 c9956a9984d7 / 第 1 页 / B7-C8 D1 BLUE_LED 与 D2 RED_LED 指示支路 |

## 系统结构

### Stamp-C5 主控制器

U3 原理图器件型号为 ESP32-C5HF4，集成 USB_D-/USB_D+ 引脚、ANT_2G 与 ANT_5G 双射频端口，并引出 GPIO0-12、GPIO14、GPIO23-28。

- 参数与网络：`reference=U3`；`part_number=ESP32-C5HF4`；`usb=USB_D-,USB_D+`；`rf=ANT_2G,ANT_5G`；`exposed_gpio=GPIO0-12,GPIO14,GPIO23-28`
- 证据：图 c9956a9984d7 / 第 1 页 / B1-D5 U3 ESP32-C5HF4 主控符号与全部外部网络

## 电源

### USB 与电池电源选择

U1 TPS2116DRLR 的 VIN1 接 USB_IN、VIN2 接 VBAT，VOUT 输出 VBUS；USB_IN 经 R7/R8 两只 10 kΩ 分压连接 PR1。

- 参数与网络：`mux=U1 TPS2116DRLR`；`vin1=USB_IN`；`vin2=VBAT`；`output=VBUS`；`priority_divider=R7=10k,R8=10k to PR1`
- 证据：图 c9956a9984d7 / 第 1 页 / A3-A4 U1 TPS2116DRLR、USB_IN/VBAT/VBUS 与 R7/R8

### JW5712 系统 3.3V

U2 JW5712 以 VBUS 为 VIN，VSEL1/VSEL2/VSEL3 均接 VBUS，图面注记 Set output Voltage = 3.3V、MAX OUT I = 600mA；SW 经 L1 FTC121065S2R2MBCA 输出 VSYS_3V3。

- 参数与网络：`converter=U2 JW5712`；`input=VBUS`；`vsel=VSEL1=1,VSEL2=1,VSEL3=1`；`output=VSYS_3V3`；`output_voltage_v=3.3`；`max_output_current_ma=600`；`inductor=L1 FTC121065S2R2MBCA`
- 证据：图 c9956a9984d7 / 第 1 页 / A5-A6 POWER 3V3 区域 U2、L1 与 3.3V/600mA 注记

### SGM40567 电池充电

U5 SGM40567-4.2XG/TR 的 VIN 接 USB_IN、BAT 接 VBAT、nCHG 输出 CHG_STA，IREF 经 R9 10 kΩ 接地；图面明确标注 Charge current = 200mA。

- 参数与网络：`charger=U5 SGM40567-4.2XG/TR`；`input=USB_IN`；`battery=VBAT`；`status=CHG_STA`；`iref=R9 10k`；`charge_current_ma=200`
- 证据：图 c9956a9984d7 / 第 1 页 / A7-A8 Charge 区域 U5、R9、USB_IN/VBAT/CHG_STA 与 200mA 注记

## 接口

### USB Type-C 输入

J1 TYPEC-302-BRP16SC08 的 VBUS 输出 USB_IN，A6/B6 并接 USBC_P，A7/B7 并接 USBC_N，CC1/CC2 分别经 R2/R3 5.1 kΩ 下拉到 GND。

- 参数与网络：`connector=J1 TYPEC-302-BRP16SC08`；`power=USB_IN`；`d_plus=A6,B6 USBC_P`；`d_minus=A7,B7 USBC_N`；`cc1_pulldown=R2 5.1k`；`cc2_pulldown=R3 5.1k`
- 证据：图 c9956a9984d7 / 第 1 页 / A1-A2 USBC IN 区域 J1、USB_IN、USBC_P/N 与 R2/R3

### ESP32-C5 原生 USB

滤波后的 USB_N 与 USB_P 分别直接连接 U3 ESP32-C5HF4 的 USB_D- 和 USB_D+ 引脚，未绘制独立 USB-UART 芯片。

- 参数与网络：`d_minus=USB_N to U3 USB_D-`；`d_plus=USB_P to U3 USB_D+`；`usb_uart_bridge=not shown`
- 证据：图 c9956a9984d7 / 第 1 页 / C1-D4 USB_N/P 网络直连 U3 pin22/pin23 USB_D-/USB_D+

### JP1/JP2 Stamp 焊盘

JP1 的 1-7 脚为 G1、G2、G3、G4、VBAT、USB_IN、GND；JP2 的 1-7 脚为 G5、G6、G7、G8、G9、G10、G28_BOOT。

- 参数与网络：`jp1=1:G1,2:G2,3:G3,4:G4,5:VBAT,6:USB_IN,7:GND`；`jp2=1:G5,2:G6,3:G7,4:G8,5:G9,6:G10,7:G28_BOOT`
- 证据：图 c9956a9984d7 / 第 1 页 / B6-B7 CELL Header 区域 JP1/JP2 1-7 脚

### JP3 12 针扩展接口

JP3 的 1-12 脚依次为 VSYS_3V3、VSYS_3V3、G23、G0、G24、G25、GND、G26、G27、G11_TXD、GND、G12_RXD。

- 参数与网络：`pinout=1:VSYS_3V3,2:VSYS_3V3,3:G23,4:G0,5:G24,6:G25,7:GND,8:G26,9:G27,10:G11_TXD,11:GND,12:G12_RXD`
- 证据：图 c9956a9984d7 / 第 1 页 / B7-B8 CELL Header 区域 JP3 1-12 脚网络

## GPIO 与控制信号

### 19 路外部 GPIO

JP1/JP2 焊盘引出 G1-G10 与 G28 共 11 路 GPIO，JP3 引出 G23、G0、G24、G25、G26、G27、G11、G12 共 8 路 GPIO，合计 19 路。

- 参数与网络：`edge_pad_gpio=G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G28`；`jp3_gpio=G23,G0,G24,G25,G26,G27,G11,G12`；`total=19`
- 证据：图 c9956a9984d7 / 第 1 页 / B6-B8 CELL Header 区域 JP1/JP2/JP3 全部 GPIO 网络

### 充电与 Boot 指示灯

D2 RED_LED 从 VBAT 经 D2、R10 1 kΩ 连接 CHG_STA；D1 BLUE_LED 从 VSYS_3V3 经 D1、R1 1 kΩ 连接 G28_BOOT。

- 参数与网络：`charge_led=VBAT-D2 RED_LED-R10 1k-CHG_STA`；`boot_led=VSYS_3V3-D1 BLUE_LED-R1 1k-G28_BOOT`
- 证据：图 c9956a9984d7 / 第 1 页 / B7-C8 D2/R10/CHG_STA 与 D1/R1/G28_BOOT

## 时钟

### ESP32-C5 晶振网络

X1 标为 TJ1148000HYFBC，连接 XTAL_P/N；XTAL_P 侧串联 L2 24 nH，并由 C6 10 pF 接地，XTAL_N 侧由 C7 12 pF 接地。

- 参数与网络：`reference=X1`；`part_number=TJ1148000HYFBC`；`series_inductor=L2 24nH LQP03TN24NH02D`；`xtal_p_capacitor=C6 10pF`；`xtal_n_capacitor=C7 12pF`
- 证据：图 c9956a9984d7 / 第 1 页 / B3-B5 X1、L2、C6/C7 与 U3 XTAL_P/N

## 复位

### CHIP_EN 复位网络

CHIP_EN 由 R4 10 kΩ 上拉至 VSYS_3V3、C19 1 µF 对地，并引出 TP7 测试点。

- 参数与网络：`signal=CHIP_EN`；`pullup=R4 10k`；`capacitor=C19 1uF`；`testpoint=TP7`
- 证据：图 c9956a9984d7 / 第 1 页 / C1-C2 TP7 CHIP_EN、R4 与 C19

### G28_BOOT 启动网络

G28_BOOT 由 R6 10 kΩ 上拉至 VSYS_3V3、C23 10 pF 对地，并引出 TP8；将该网络接地后上电可形成低电平启动条件。

- 参数与网络：`signal=G28_BOOT`；`gpio=GPIO28`；`pullup=R6 10k`；`capacitor=C23 10pF`；`testpoint=TP8`
- 证据：图 c9956a9984d7 / 第 1 页 / C1-D2 TP8 G28_BOOT、R6/C23 与 U3 GPIO28

## 保护电路

### USB 数据滤波与保护

USBC_P/N 通过 FT1 ICMF062P900MFR 输出 USB_P/N，连接器侧的两路数据线分别由 DR1/DR2 对地保护。

- 参数与网络：`filter=FT1 ICMF062P900MFR`；`input=USBC_P,USBC_N`；`output=USB_P,USB_N`；`esd=DR1,DR2`
- 证据：图 c9956a9984d7 / 第 1 页 / A2-A3 FT1、DR1/DR2 与 USBC_P/N/USB_P/N

## 射频

### 2.4GHz 与 5GHz 天线复用

U3 ANT_5G 经 L3 0 Ω 和 C17/C18 NC 匹配位连接 U4 H_PORT；ANT_2G 经 L4 2 nH 和 C20 2.2 pF/C21 2.4 pF 连接 U4 L_PORT；U4 LFD182G45DCHD481 的 COM 经 50 Ω 受控阻抗网络连接 J2 IPEX_1，DR3 为 NC。

- 参数与网络：`diplexer=U4 LFD182G45DCHD481`；`high_band=ANT_5G-L3 0R-C17/C18 NC-H_PORT`；`low_band=ANT_2G-L4 2nH-C20 2.2pF/C21 2.4pF-L_PORT`；`common=COM to J2 IPEX_1 via 50R controlled impedance`；`optional_esd=DR3 NC`
- 证据：图 c9956a9984d7 / 第 1 页 / C4-D8 U3 ANT_5G/ANT_2G、匹配网络、U4 与 J2 IPEX_1

## 调试与烧录

### USB、UART、EN 与 Boot 测试点

TP3=USBC_P、TP4=USBC_N、TP5=G11_TXD、TP6=G12_RXD、TP7=CHIP_EN、TP8=G28_BOOT。

- 参数与网络：`mapping=TP3:USBC_P,TP4:USBC_N,TP5:G11_TXD,TP6:G12_RXD,TP7:CHIP_EN,TP8:G28_BOOT`
- 证据：图 c9956a9984d7 / 第 1 页 / C1-D2 左侧 TP3-TP8 网络标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-C5 主控制器 | `reference=U3`；`part_number=ESP32-C5HF4`；`usb=USB_D-,USB_D+`；`rf=ANT_2G,ANT_5G`；`exposed_gpio=GPIO0-12,GPIO14,GPIO23-28` |
| 接口 | USB Type-C 输入 | `connector=J1 TYPEC-302-BRP16SC08`；`power=USB_IN`；`d_plus=A6,B6 USBC_P`；`d_minus=A7,B7 USBC_N`；`cc1_pulldown=R2 5.1k`；`cc2_pulldown=R3 5.1k` |
| 保护电路 | USB 数据滤波与保护 | `filter=FT1 ICMF062P900MFR`；`input=USBC_P,USBC_N`；`output=USB_P,USB_N`；`esd=DR1,DR2` |
| 电源 | USB 与电池电源选择 | `mux=U1 TPS2116DRLR`；`vin1=USB_IN`；`vin2=VBAT`；`output=VBUS`；`priority_divider=R7=10k,R8=10k to PR1` |
| 电源 | JW5712 系统 3.3V | `converter=U2 JW5712`；`input=VBUS`；`vsel=VSEL1=1,VSEL2=1,VSEL3=1`；`output=VSYS_3V3`；`output_voltage_v=3.3`；`max_output_current_ma=600`；`inductor=L1 FTC121065S2R2MBCA` |
| 电源 | SGM40567 电池充电 | `charger=U5 SGM40567-4.2XG/TR`；`input=USB_IN`；`battery=VBAT`；`status=CHG_STA`；`iref=R9 10k`；`charge_current_ma=200` |
| 接口 | ESP32-C5 原生 USB | `d_minus=USB_N to U3 USB_D-`；`d_plus=USB_P to U3 USB_D+`；`usb_uart_bridge=not shown` |
| 复位 | CHIP_EN 复位网络 | `signal=CHIP_EN`；`pullup=R4 10k`；`capacitor=C19 1uF`；`testpoint=TP7` |
| 复位 | G28_BOOT 启动网络 | `signal=G28_BOOT`；`gpio=GPIO28`；`pullup=R6 10k`；`capacitor=C23 10pF`；`testpoint=TP8` |
| 调试与烧录 | USB、UART、EN 与 Boot 测试点 | `mapping=TP3:USBC_P,TP4:USBC_N,TP5:G11_TXD,TP6:G12_RXD,TP7:CHIP_EN,TP8:G28_BOOT` |
| 时钟 | ESP32-C5 晶振网络 | `reference=X1`；`part_number=TJ1148000HYFBC`；`series_inductor=L2 24nH LQP03TN24NH02D`；`xtal_p_capacitor=C6 10pF`；`xtal_n_capacitor=C7 12pF` |
| 射频 | 2.4GHz 与 5GHz 天线复用 | `diplexer=U4 LFD182G45DCHD481`；`high_band=ANT_5G-L3 0R-C17/C18 NC-H_PORT`；`low_band=ANT_2G-L4 2nH-C20 2.2pF/C21 2.4pF-L_PORT`；`common=COM to J2 IPEX_1 via 50R controlled impedance`；`optional_esd=DR3 NC` |
| 接口 | JP1/JP2 Stamp 焊盘 | `jp1=1:G1,2:G2,3:G3,4:G4,5:VBAT,6:USB_IN,7:GND`；`jp2=1:G5,2:G6,3:G7,4:G8,5:G9,6:G10,7:G28_BOOT` |
| 接口 | JP3 12 针扩展接口 | `pinout=1:VSYS_3V3,2:VSYS_3V3,3:G23,4:G0,5:G24,6:G25,7:GND,8:G26,9:G27,10:G11_TXD,11:GND,12:G12_RXD` |
| GPIO 与控制信号 | 19 路外部 GPIO | `edge_pad_gpio=G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G28`；`jp3_gpio=G23,G0,G24,G25,G26,G27,G11,G12`；`total=19` |
| GPIO 与控制信号 | 充电与 Boot 指示灯 | `charge_led=VBAT-D2 RED_LED-R10 1k-CHG_STA`；`boot_led=VSYS_3V3-D1 BLUE_LED-R1 1k-G28_BOOT` |
| 系统结构 | 原理图版本标识 | `resource_filename_revision=V0.3`；`visible_title_revision=V0.2`；`visible_page=2/2`；`visible_date=2/07/2026` |
| 存储 | 4MB Flash 实现方式 | `source_document_capacity=4MB`；`schematic_soc=ESP32-C5HF4`；`external_flash=not shown` |
| 接口 | Stamp-C5 的 FPC 座装配状态 | `schematic=JP3 12-pin electrical interface`；`source_document_stamp_c5=FPC connector not populated by default`；`source_document_stamp_c5_dip=FPC connector populated` |
| 电源 | 电池深度休眠功耗 | `source_document=3.7V@13uA deep sleep`；`power_path=VBAT-TPS2116DRLR-JW5712-VSYS_3V3`；`test_conditions=not specified` |

## 待确认事项

- `system.schematic-revision`：资源 URL 与 PDF 文件名标为 StampC5 V0.3，但当前本地页面标题栏写 StampC5、页码 2/2、Revision V0.2、Date 2/07/2026；无法仅凭这一页确认 V0.3 文件是否仍包含 V0.2 页面或资源命名有误。（证据：图 c9956a9984d7 / 第 1 页 / D6-D8 标题栏 StampC5、2/2、Revision V0.2、Date 2/07/2026）
- `storage.integrated-flash`：源文档标注 4MB Flash，原理图只绘制 U3 ESP32-C5HF4 且没有独立 Flash 器件；Flash 是否集成于该封装及实际容量需由器件资料或 BOM 确认。（证据：图 c9956a9984d7 / 第 1 页 / B1-D5 ESP32-C5HF4 区域无独立 Flash 器件）
- `interface.fpc-assembly`：原理图给出 JP3 12 针扩展接口电气定义，源文档产品对比表说明 Stamp-C5 默认不焊 FPC 座、Stamp-C5 DIP 默认焊接；当前 S016 单品的 JP3 是裸焊盘还是未装连接器需由 BOM 或实物确认。（证据：图 c9956a9984d7 / 第 1 页 / B7-B8 CELL Header 区域 JP3 12 针符号，未提供装配属性）
- `power.deep-sleep-current`：源文档标注电池供电深度休眠为 3.7V@13µA，原理图显示 TPS2116DRLR、JW5712、SGM40567 和 LED 支路，但没有功耗测试状态、测量点、温度或器件关断配置，无法从图面复核 13µA 指标。（证据：图 c9956a9984d7 / 第 1 页 / A3-C8 VBAT 电源路径与 LED 支路，未标功耗测试条件）
- `review.schematic-revision`：S016 当前正式原理图版本是 V0.3 还是页面标题栏所示 V0.2？；原因：资源文件名/URL 与页面可见 Revision 字段不一致，且当前清单只收录 PDF 第 2 页。
- `review.integrated-flash`：U3 ESP32-C5HF4 是否集成源文档所述 4MB Flash，实际容量如何由 BOM 或器件资料确认？；原因：原理图没有独立 Flash，也未直接标注容量。
- `review.fpc-assembly`：普通 Stamp-C5 的 JP3 实物是裸焊盘、未装 FPC 座还是其他连接形式？；原因：原理图只给出电气符号，源文档说明普通版默认不焊 FPC 座。
- `review.deep-sleep-current`：3.7V@13µA 深度休眠指标的测量点、温度、射频状态、LED 状态和电源器件配置是什么？；原因：原理图无法给出性能测试边界。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c9956a9984d780e970e779dac5371128f78093a1f37a53756714d0c2b29cfc19` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/S016_StampC5_V0.3_SCH_PDF_20260207_2026_02_07_11_34_57_page_02.png` |

---

源文档：`zh_CN/core/Stamp-C5.md`

源文档 SHA-256：`afbc68b69387a70a16d132ab2c96eac9fd1de3ee1d5e904914baee58bfb49ba4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
