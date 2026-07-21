# Tab5 Keyboard 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Tab5 Keyboard |
| SKU | A164 |
| 产品 ID | `tab5-keyboard-d4c3f4783ca5` |
| 源文档 | `zh_CN/tab5/Tab5_Keyboard.md` |

## 概述

Tab5 Keyboard 以 U1 STM32F030C8T6 为控制器，连接 S1-S70 共 70 个开关。图面标题为 Keyboard matrix 5x14；其中 68 个按键通过 D1-D56、D58-D69 接入 ROW0-ROW7 与 COL0-COL8 的电气扫描网络，S57/S70 两个 Fn 开关分别从 COL9/COL10 接地。U1 通过 P1 的 SDA_G0/SCL_G1 与主机通信，INT_G50 独立引出并上拉；PB15 的 RGB_DATA 经 R7 驱动两颗级联 WS2812E-1313。P1 输入 VCC_3V3，板上包含 MCU 去耦、NRST RC、BOOT0 下拉和五针 SWD 接口。原理图未标 I2C 地址、固件报文模式、多键上报上限、功耗、连接器节距或 Tab5 机械兼容信息，这些正文参数需结合固件、BOM、机械资料和实测确认。

## 检索关键词

`Tab5 Keyboard`、`A164`、`STM32F030C8T6`、`70 keys`、`Keyboard matrix 5x14`、`14x5 keyboard`、`ROW0`、`ROW7`、`COL0`、`COL10`、`S1-S70`、`D1-D69`、`S57`、`S70`、`FNx2`、`SPCx4`、`I2C`、`0x6D`、`SDA_G0`、`SCL_G1`、`INT_G50`、`WS2812E-1313`、`RGB_DATA`、`VCC_3V3`、`Header 5X2`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`normal mode`、`HID mode`、`character mode`、`Tab5 Ext.Port1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030C8T6 | 扫描 ROW0-ROW7/COL0-COL10 键盘网络，通过 I2C 与中断连接主机，并驱动 RGB_DATA | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1B-3D，U1A/U1B STM32F030C8T6 |
| P1 | Header 5X2 | 主机接口，引出 SDA_G0、SCL_G1、INT_G50、VCC_3V3 与 GND | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1A-2B，P1 Header 5X2 |
| U2/U3 | WS2812E-1313 | 由 U1 PB15/RGB_DATA 串行驱动的两颗级联 RGB LED | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 3C-4D，U2/U3 WS2812E-1313 |
| P2 | SWD | 五针 MCU 调试接口，提供 VCC_3V3、SWCLK、SWDIO、NRST 与 GND | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 2D，P2 SWD pins1-5 |
| S1-S70 | 未标注 | 70 个键盘开关；68 个接入行列矩阵，S57/S70 为独立 Fn 开关 | 图 436646db9d99 / 第 1 页 / 资源 1 第 1 页完整 Keyboard matrix 5x14，S1-S70 |
| D1-D56/D58-D69 | Diode | 68 个矩阵按键各自串联的隔离二极管 | 图 436646db9d99 / 第 1 页 / 资源 1 第 1 页 S1-S56、S58-S69 下方 D1-D56、D58-D69 |
| R1/R2/R3 | 4.7K, 4.7K, 10K | SCL_G1、SDA_G0 与 INT_G50 到 VCC_3V3 的上拉电阻 | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 MCU 区 R1/R2 4.7K 与 R3 10K |
| R4/R5/C4 | 10K, 10K, 100nF | U1 NRST 上拉/滤波与 BOOT0 下拉网络 | 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1D-2D，U1B NRST/BOOT0 与 R4/R5/C4 |

## 系统结构

### Tab5 Keyboard 硬件架构

U1 STM32F030C8T6 扫描 S1-S70 键盘网络，通过 P1 的 SDA_G0/SCL_G1 与 INT_G50 连接主机，并以 PB15/RGB_DATA 驱动 U2/U3 两颗 WS2812E-1313；整板由 VCC_3V3 供电并提供 P2 SWD。

- 参数与网络：`controller=U1 STM32F030C8T6`；`keys=70`；`host_interface=P1 I2C + INT`；`rgb=U2/U3 WS2812E-1313`；`supply=VCC_3V3`；`debug=P2 SWD`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页完整键盘矩阵; 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页完整 Interface/MCU/RGB 分区

## 核心器件

### U1 微控制器

主控制器位号为 U1，原理图器件值明确标为 STM32F030C8T6。

- 参数与网络：`reference=U1`；`part_number=STM32F030C8T6`；`pin_count=48`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1A/U1B 底部 STM32F030C8T6

### 双 WS2812E-1313

U1 PB15 pin28 的 RGB_DATA 经 R7 1K 连接 U2 DIN pin4；U2 DOUT pin2 连接 U3 DIN pin4，U3 DOUT pin2 在本页无后级连接；U2/U3 均由 VCC_3V3 供电。

- 参数与网络：`driver=U1.PB15 pin28 RGB_DATA`；`series_resistor=R7 1K`；`first_pixel=U2 WS2812E-1313`；`second_pixel=U3 WS2812E-1313`；`chain=U2.DOUT -> U3.DIN`；`supply=VCC_3V3`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 3C-4D，RGB_DATA/R7/U2/U3

## 电源

### P1 与 VCC_3V3

P1 pin5 接 VCC_3V3，pins2/3/4 接 GND；pins1 SYS_VIN、6 SYS_EXT5V 和 10 G9 在图面标记未连接，页面没有本地稳压器或其他电源输入路径。

- 参数与网络：`supply_pin=P1.5 VCC_3V3`；`ground_pins=P1.2,P1.3,P1.4`；`not_connected=P1.1 SYS_VIN,P1.6 SYS_EXT5V,P1.10 G9`；`local_regulator_shown=false`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1A-2B，P1 pins1-10

### MCU 与 RGB 3.3V 供电

VCC_3V3 接 U1 VDD pins1/24/48 和 VDDA pin9，U1 VSS pins23/47 与 VSSA pin8 接 GND；U2/U3 VDD pin1 也接 VCC_3V3，GND pin3 接地。

- 参数与网络：`mcu_vdd=U1 pins1,24,48`；`mcu_vdda=U1 pin9`；`mcu_ground=U1 pins8,23,47`；`rgb_supply=U2/U3 pin1 VCC_3V3`；`rgb_ground=U2/U3 pin3 GND`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1B 电源单元与 U2/U3 VDD/GND

### VCC_3V3 去耦

C1、C2、C5 均标 100nF，跨接 VCC_3V3 与 GND；U3 附近的 C3 标 NC。

- 参数与网络：`decoupling=C1 100nF,C2 100nF,C5 100nF`；`optional_rgb_cap=C3 NC`；`rail=VCC_3V3`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 2C-4D，C1/C2/C5 100nF 与 C3 NC

## 接口

### P1 Header 5X2

P1 pin7=SCL_G1、pin8=SDA_G0、pin9=INT_G50、pin5=VCC_3V3、pins2/3/4=GND；pins1 SYS_VIN、6 SYS_EXT5V、10 G9 标未连接。

- 参数与网络：`pin1=SYS_VIN NC`；`pin2=GND`；`pin3=GND`；`pin4=GND`；`pin5=VCC_3V3`；`pin6=SYS_EXT5V NC`；`pin7=SCL_G1`；`pin8=SDA_G0`；`pin9=INT_G50`；`pin10=G9 NC`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1A-2B，P1 Header 5X2 逐针网络

### 70 键拓扑

键盘页标题标为 Keyboard matrix 5x14，开关位号覆盖 S1-S70；其中 S1-S56、S58-S69 共 68 个开关连接 ROW0-ROW7 与 COL0-COL8，S57/S70 为另外两路 Fn 输入。

- 参数与网络：`schematic_title=Keyboard matrix 5x14`；`total_switches=70`；`matrix_switches=68`；`matrix_rows=ROW0-ROW7`；`matrix_columns=COL0-COL8`；`direct_fn_switches=S57,S70`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页完整 5x14 键盘页，S1-S70 与 ROW0-7/COL0-10

### S57/S70 Fn 输入

S57 将 COL9 接 GND，S70 将 COL10 接 GND；两只开关位于 FNx2 分区，不连接 ROW0-ROW7。

- 参数与网络：`S57=COL9 -> GND`；`S70=COL10 -> GND`；`matrix_row_connection=false`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页网格 4A，FNx2 的 S57/S70、COL9/COL10 与 GND

### 主要键位分组

图面键名覆盖数字 0-9、字母 A-Z、标点、ESC、CTRL、CAPS、TAB、BS、RET、SFT、GRPH、KANA、STOP、SEL、四方向键，以及 S61/S62/S65/S66 四个 SPC 开关。

- 参数与网络：`alphanumeric=0-9,A-Z`；`modifiers=CTRL,CAPS,SFT,GRPH,KANA`；`navigation=ESC,TAB,BS,RET,STOP,SEL,left,up,down,right`；`space_switches=S61,S62,S65,S66`；`space_count=4`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页全部橙色键名与 SPCx4 标注

## 总线

### U1 到 P1 的 I2C

U1 PB10 pin21 通过 SCL_G1 接 P1 pin7，并由 R1 4.7K 上拉到 VCC_3V3；U1 PB11 pin22 通过 SDA_G0 接 P1 pin8，并由 R2 4.7K 上拉到 VCC_3V3。

- 参数与网络：`scl=U1.PB10 pin21 -> SCL_G1 -> P1.7`；`sda=U1.PB11 pin22 -> SDA_G0 -> P1.8`；`scl_pullup=R1 4.7K to VCC_3V3`；`sda_pullup=R2 4.7K to VCC_3V3`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1 PB10/PB11、R1/R2 与 P1 pins7/8

## GPIO 与控制信号

### INT_G50 中断网络

U1 PA15 pin38 连接 INT_G50 和 P1 pin9，R3 10K 将该网络上拉到 VCC_3V3。

- 参数与网络：`mcu_pin=U1.PA15 pin38`；`net=INT_G50`；`host_pin=P1.9`；`pullup=R3 10K to VCC_3V3`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1 PA15/INT_G50、R3 与 P1 pin9

### 键盘 ROW/COL 到 U1 映射

COL0-COL7 分别连接 U1 PA0-PA7 pins10-17，COL8/COL9/COL10 分别连接 PA8/PA9/PA10 pins29/30/31；ROW0-ROW7 分别连接 PB0-PB7 pins18/19/20/39/40/41/42/43。

- 参数与网络：`columns_0_7=COL0-7 -> PA0-7 pins10-17`；`column_8=COL8 -> PA8 pin29`；`column_9=COL9 -> PA9 pin30`；`column_10=COL10 -> PA10 pin31`；`rows=ROW0-7 -> PB0-7 pins18,19,20,39,40,41,42,43`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1A 左侧 COL0-COL10 与右侧 ROW0-ROW7

### U1 未连接引脚

U1 PA11/PA12、PB8/PB9、PB12/PB13/PB14、PC13/PC14/PC15、PF0/PF1/PF6/PF7 在本页均无外部连接。

- 参数与网络：`port_a=PA11,PA12`；`port_b=PB8,PB9,PB12,PB13,PB14`；`port_c=PC13,PC14,PC15`；`port_f=PF0,PF1,PF6,PF7`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1A 未接引脚短线

## 时钟

### 外部时钟源

U1 PF0-OSC_IN pin5、PF1-OSC_OUT pin6、PC14-OSC32_IN pin3 和 PC15-OSC32_OUT pin4 均无外部连接，两个原理图资源未显示晶振、谐振器或外部振荡器。

- 参数与网络：`high_speed_osc_pins=PF0 pin5,PF1 pin6 unconnected`；`low_speed_osc_pins=PC14 pin3,PC15 pin4 unconnected`；`external_clock_shown=false`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1A PF0/PF1/PC14/PC15 无外部连线

## 复位

### U1 NRST 与 BOOT0

U1 NRST pin7 连接 P2 pin4，由 R4 10K 上拉到 VCC_3V3，并由 C4 100nF 对地；BOOT0 pin44 由 R5 10K 下拉到 GND。

- 参数与网络：`reset_pin=U1.NRST pin7`；`reset_header=P2.4`；`reset_pullup=R4 10K`；`reset_capacitor=C4 100nF`；`boot0=U1.BOOT0 pin44 -> R5 10K -> GND`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页网格 1D-2D，U1B NRST/BOOT0 与 P2

## 保护电路

### 矩阵按键隔离二极管

68 个行列矩阵开关各串联一只二极管，位号为 D1-D56 和 D58-D69；S57/S70 两个 Fn 开关没有串联二极管。

- 参数与网络：`diode_count=68`；`references=D1-D56,D58-D69`；`protected_switches=S1-S56,S58-S69`；`no_diode_switches=S57,S70`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页逐键 S/D 支路与右上 FNx2

## 内存与 Flash

### 外部存储器

两个原理图资源未展示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`
- 证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页仅键盘开关与二极管; 图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 Interface/MCU/RGB 无外部存储器

## 调试与烧录

### P2 SWD 接口

P2 pin1=VCC_3V3、pin2=SWCLK、pin3=SWDIO、pin4=NRST、pin5=GND；U1 PA13 pin34 接 SWDIO，PA14 pin37 接 SWCLK。

- 参数与网络：`pin1=VCC_3V3`；`pin2=SWCLK -> U1.PA14 pin37`；`pin3=SWDIO -> U1.PA13 pin34`；`pin4=NRST`；`pin5=GND`
- 证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1 PA13/PA14 与 P2 SWD pins1-5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Tab5 Keyboard 硬件架构 | `controller=U1 STM32F030C8T6`；`keys=70`；`host_interface=P1 I2C + INT`；`rgb=U2/U3 WS2812E-1313`；`supply=VCC_3V3`；`debug=P2 SWD` |
| 核心器件 | U1 微控制器 | `reference=U1`；`part_number=STM32F030C8T6`；`pin_count=48` |
| 电源 | P1 与 VCC_3V3 | `supply_pin=P1.5 VCC_3V3`；`ground_pins=P1.2,P1.3,P1.4`；`not_connected=P1.1 SYS_VIN,P1.6 SYS_EXT5V,P1.10 G9`；`local_regulator_shown=false` |
| 电源 | MCU 与 RGB 3.3V 供电 | `mcu_vdd=U1 pins1,24,48`；`mcu_vdda=U1 pin9`；`mcu_ground=U1 pins8,23,47`；`rgb_supply=U2/U3 pin1 VCC_3V3`；`rgb_ground=U2/U3 pin3 GND` |
| 电源 | VCC_3V3 去耦 | `decoupling=C1 100nF,C2 100nF,C5 100nF`；`optional_rgb_cap=C3 NC`；`rail=VCC_3V3` |
| 接口 | P1 Header 5X2 | `pin1=SYS_VIN NC`；`pin2=GND`；`pin3=GND`；`pin4=GND`；`pin5=VCC_3V3`；`pin6=SYS_EXT5V NC`；`pin7=SCL_G1`；`pin8=SDA_G0`；`pin9=INT_G50`；`pin10=G9 NC` |
| 总线 | U1 到 P1 的 I2C | `scl=U1.PB10 pin21 -> SCL_G1 -> P1.7`；`sda=U1.PB11 pin22 -> SDA_G0 -> P1.8`；`scl_pullup=R1 4.7K to VCC_3V3`；`sda_pullup=R2 4.7K to VCC_3V3` |
| GPIO 与控制信号 | INT_G50 中断网络 | `mcu_pin=U1.PA15 pin38`；`net=INT_G50`；`host_pin=P1.9`；`pullup=R3 10K to VCC_3V3` |
| GPIO 与控制信号 | 键盘 ROW/COL 到 U1 映射 | `columns_0_7=COL0-7 -> PA0-7 pins10-17`；`column_8=COL8 -> PA8 pin29`；`column_9=COL9 -> PA9 pin30`；`column_10=COL10 -> PA10 pin31`；`rows=ROW0-7 -> PB0-7 pins18,19,20,39,40,41,42,43` |
| 接口 | 70 键拓扑 | `schematic_title=Keyboard matrix 5x14`；`total_switches=70`；`matrix_switches=68`；`matrix_rows=ROW0-ROW7`；`matrix_columns=COL0-COL8`；`direct_fn_switches=S57,S70` |
| 保护电路 | 矩阵按键隔离二极管 | `diode_count=68`；`references=D1-D56,D58-D69`；`protected_switches=S1-S56,S58-S69`；`no_diode_switches=S57,S70` |
| 接口 | S57/S70 Fn 输入 | `S57=COL9 -> GND`；`S70=COL10 -> GND`；`matrix_row_connection=false` |
| 接口 | 主要键位分组 | `alphanumeric=0-9,A-Z`；`modifiers=CTRL,CAPS,SFT,GRPH,KANA`；`navigation=ESC,TAB,BS,RET,STOP,SEL,left,up,down,right`；`space_switches=S61,S62,S65,S66`；`space_count=4` |
| 核心器件 | 双 WS2812E-1313 | `driver=U1.PB15 pin28 RGB_DATA`；`series_resistor=R7 1K`；`first_pixel=U2 WS2812E-1313`；`second_pixel=U3 WS2812E-1313`；`chain=U2.DOUT -> U3.DIN`；`supply=VCC_3V3` |
| 调试与烧录 | P2 SWD 接口 | `pin1=VCC_3V3`；`pin2=SWCLK -> U1.PA14 pin37`；`pin3=SWDIO -> U1.PA13 pin34`；`pin4=NRST`；`pin5=GND` |
| 复位 | U1 NRST 与 BOOT0 | `reset_pin=U1.NRST pin7`；`reset_header=P2.4`；`reset_pullup=R4 10K`；`reset_capacitor=C4 100nF`；`boot0=U1.BOOT0 pin44 -> R5 10K -> GND` |
| 时钟 | 外部时钟源 | `high_speed_osc_pins=PF0 pin5,PF1 pin6 unconnected`；`low_speed_osc_pins=PC14 pin3,PC15 pin4 unconnected`；`external_clock_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false` |
| GPIO 与控制信号 | U1 未连接引脚 | `port_a=PA11,PA12`；`port_b=PB8,PB9,PB12,PB13,PB14`；`port_c=PC13,PC14,PC15`；`port_f=PF0,PF1,PF6,PF7` |
| 总线地址 | I2C 默认地址 | `documented_address_7bit=0x6D`；`address_printed_on_schematic=false`；`address_straps_shown=false` |
| 其他事实 | 普通/HID/字符模式 | `documented_modes=normal,HID,character`；`normal_payload=key state and row/column`；`hid_payload=HID report`；`character_payload=key name string and Ctrl/Alt state`；`schematic_confirms_firmware=false` |
| 接口 | 多键同时按压能力 | `documented_multikey=true`；`matrix_diodes=68`；`maximum_rollover=null`；`scan_period=null`；`debounce=null`；`conflict_policy=null` |
| 接口 | INT_G50 中断行为 | `documented_host_pin=G50`；`schematic_net=INT_G50`；`pullup=R3 10K`；`direction=null`；`active_level=null`；`trigger=null`；`latency=null` |
| 电源 | 正文待机与工作功耗 | `documented_standby=3.3V@14.5mA`；`documented_rgb_white_max=3.3V@21.5mA`；`documented_input_rgb_off=3.3V@14.5mA`；`measurement_conditions_shown=false` |
| 核心器件 | 双 RGB 状态指示 | `documented_role=full-color status indication`；`schematic_pixels=U2/U3 WS2812E-1313`；`status_mapping=null`；`brightness=null`；`refresh_timing=null` |
| 其他事实 | Tab5 Ext.Port1 与连接器机械规格 | `documented_host=Tab5 Ext.Port1`；`documented_connector=2x5 PIN,2.54mm pitch`；`documented_retention=side latches`；`schematic_label=P1 Header 5X2`；`host_revision=null` |

## 待确认事项

- `address.documented-i2c-0x6d`：正文规格表给出默认 I2C 地址 0x6D，原理图只显示 SDA_G0/SCL_G1 连线和上拉，没有 0x6D 文本、地址跳线或地址配置电阻。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1 PB10/PB11 与 P1 I2C，无地址配置）
- `other.documented-firmware-modes`：正文称预置固件提供普通、HID、字符三种数据报文模式，并描述行列坐标、HID 报文、键名字符串和修饰符状态；原理图不包含协议寄存器、报文格式或固件状态机。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页仅 MCU 电气连接，无协议或固件模式标注）
- `interface.documented-multikey-capability`：正文称键盘支持多键同时按压；原理图确认 68 个矩阵键各有串联二极管，但未标固件扫描周期、去抖策略、最大同时上报键数或冲突处理规则。（证据：图 436646db9d99 / 第 1 页 / 资源 1 第 1 页 68 路带二极管矩阵，未标扫描与上报参数）
- `interface.documented-interrupt-semantics`：正文将 G50 描述为按键事件低延迟实时上报的独立中断；原理图确认 PA15-INT_G50-P1.9 与 10K 上拉，但未说明输出方向、有效电平、触发方式、脉宽或延迟。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 U1 PA15/INT_G50、R3 与 P1.9，无时序文本）
- `power.documented-consumption`：正文列出待机 3.3V@14.5mA、RGB 白色最大亮度 3.3V@21.5mA、RGB 关闭输入时 3.3V@14.5mA；原理图未给测量边界、固件状态、LED 亮度设定或电流标注。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 VCC_3V3、U1/U2/U3，无电流或测试条件标注）
- `component.documented-rgb-behavior`：正文称两颗 RGB LED 用于全彩状态指示；原理图确认 U2/U3 型号和级联数据链，但未标颜色含义、亮度、刷新时序或状态映射。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 RGB_DATA/R7/U2/U3，仅有电气连接）
- `other.documented-host-mechanics`：正文称键盘通过 Tab5 Ext.Port1 即插即用，接口为 2×5 PIN、2.54mm 间距，并由侧边卡扣锁紧；原理图仅将 P1 标为 Header 5X2，没有节距、配对连接器、Tab5 版本或机械卡扣信息。（证据：图 9ee76efb3ec8 / 第 1 页 / 资源 2 第 1 页 P1 仅标 Header 5X2，无节距或机械结构）
- `review.i2c-address`：请通过 A164 当前量产固件或 I2C 协议确认 7-bit 默认地址是否为 0x6D，以及是否可配置。；原因：地址属于固件行为，原理图只有 SDA/SCL 连线和上拉。
- `review.firmware-modes`：请依据 A164 内置固件版本和通信协议确认普通、HID、字符模式的选择方式、寄存器与完整报文格式。；原因：三种模式及报文语义来自正文，原理图不能证明固件实现。
- `review.multikey-capability`：请用 A164 固件和键盘测试确认最大同时按键数、去抖、冲突处理与三种模式下的上报限制。；原因：逐键二极管可由图面确认，但完整多键能力取决于扫描和报文实现。
- `review.interrupt-semantics`：请通过 A164 固件和逻辑分析确认 INT_G50 的方向、有效电平、触发方式、脉宽及按键到中断延迟。；原因：原理图只确认 PA15、10K 上拉和 P1.9，未给出中断时序。
- `review.power-consumption`：请在指定固件、输入状态与 RGB 亮度下实测并确认 14.5mA/21.5mA 功耗参数及其统计边界。；原因：正文给出电流数值，原理图没有工作状态或测量条件。
- `review.rgb-behavior`：请依据 A164 固件和 WS2812E-1313 配置确认两颗 RGB 的状态含义、亮度限制与刷新时序。；原因：原理图只确认器件型号和级联链路，不包含状态策略。
- `review.host-mechanics`：请用 A164 BOM、结构图和对应 Tab5 版本确认 P1 的 2.54mm 节距、Ext.Port1 配对、侧边卡扣和版本兼容范围。；原因：原理图只标 Header 5X2，不包含连接器完整料号或机械结构。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `436646db9d99db5e3c77c2cf16edefbfc5e7f9ee362005c69385db9a653d1386` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/SCH_Tab5_Keyboard_SCH_V1.0_20251109_2026_05_06_16_24_34_page_01.png` |
| 2 | 1 | `9ee76efb3ec8284d2f60050757119d30ff56fa11ec33bf082438ada9f339088d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/SCH_Tab5_Keyboard_SCH_V1.0_20251109_2026_05_06_16_24_34_page_02.png` |

---

源文档：`zh_CN/tab5/Tab5_Keyboard.md`

源文档 SHA-256：`56df9ea36ed13b9a961bec5c77e85b3d3fe1ec589302b1cb5c8c8b4d53c231a2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
