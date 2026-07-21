# Faces Calculator 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces Calculator |
| SKU | A005 |
| 产品 ID | `faces-calculator-ac468d2b86a6` |
| 源文档 | `zh_CN/module/faces_calculator.md` |

## 概述

Faces Calculator 以 U1 ATmega328P-AU 扫描 4×5 按键矩阵：PC0~PC3 连接 O1~O4 四条行线，PD2~PD6 连接 A~E 五条列线。U1 的 PC4/SDA 与 PC5/SCL 直接连接 BUS1 的 SDA/SCL，PB0 经 G5 网络连接 BUS1.22；U1 由 BUS1 的 3V3 与 GND 供电。页面还画出 P1 六针接口、RESET 网络及两条经 10K 电阻引出的 PD0/PD1 路径，但 I2C 地址 0x08、P1 完整针序和 10K 电阻位号未能从该页可靠确认。

## 检索关键词

`Faces Calculator`、`A005`、`ATmega328P-AU`、`ATmega328P`、`BUS1`、`M5_BUS`、`3V3`、`SDA`、`SCL`、`I2C`、`0x08`、`G5`、`RESET`、`P1 Header 6`、`4x5 key matrix`、`O1`、`O2`、`O3`、`O4`、`A`、`B`、`C`、`D`、`E`、`PC0`、`PC1`、`PC2`、`PC3`、`PC4 SDA`、`PC5 SCL`、`PD2`、`PD3`、`PD4`、`PD5`、`PD6`、`PB0`、`20 keys`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ATmega328P-AU | 扫描 4×5 按键矩阵并通过 SDA/SCL 与面板总线通信的主控制器 | 图 9698c28b8392 / 第 1 页 / 第 1 页左下 U1，器件标注 ATmega328P-AU，显示 PC/PD/PB、ADC、VCC/AVCC/AREF/GND 引脚 |
| BUS1 | M5_BUS | 22 针 Faces 面板接口，引出 3V3、GND、SDA、SCL、G5 及其他面板总线信号 | 图 9698c28b8392 / 第 1 页 / 第 1 页左上 BUS1 M5_BUS，1~22 脚与 GND/3V3/SDA/SCL/G5 等标签 |
| P1 | Header 6 | 连接 U1 PB 端口、RESET 和 GND 的六针接口；完整针脚对应需复核 | 图 9698c28b8392 / 第 1 页 / 第 1 页下部中右 P1 Header 6，1~6 脚，左侧多条 U1 PB 端口连线及 RESET/GND 标注 |
| S1/S4/S7/S10/S13 | 未标注 | O1 行的五个按键，分别连接列 A/B/C/D/E，图示键值 AC/7/4/1/小数点 | 图 9698c28b8392 / 第 1 页 / 第 1 页右下 O1 行，五个开关 S1/S4/S7/S10/S13 与 A~E 列 |
| S2/S5/S8/S11/S14 | 未标注 | O2 行的五个按键，分别连接列 A/B/C/D/E，图示键值 M/8/5/2/0 | 图 9698c28b8392 / 第 1 页 / 第 1 页右中下 O2 行，五个开关 S2/S5/S8/S11/S14 与 A~E 列 |
| S3/S6/S9/S12/S15 | 未标注 | O3 行的五个按键，分别连接列 A/B/C/D/E，图示键值 %/9/6/3/+/- | 图 9698c28b8392 / 第 1 页 / 第 1 页右中 O3 行，五个开关 S3/S6/S9/S12/S15 与 A~E 列 |
| O4 row switches (5, references unclear) | 未标注 | O4 行连接 A~E 五列的五个运算功能按键 | 图 9698c28b8392 / 第 1 页 / 第 1 页右上 O4 行，共五个开关分别落到 A/B/C/D/E；位号与键面字符在当前图像中不清晰 |
| Two 10K resistors (references unclear) | 10K | 串联在 U1 PD0/PD1 向右引出的两条路径上，末端标注 16 与 17 | 图 9698c28b8392 / 第 1 页 / 第 1 页 U1 右侧 PD0/PD1 两条线上各一只位号不清、阻值 10K 的电阻，右端标 16/17 |

## 系统结构

### Faces Calculator

U1 ATmega328P-AU 通过 PC0~PC3 和 PD2~PD6 扫描 O1~O4、A~E 组成的 4×5 按键矩阵，并以 PC4/SDA、PC5/SCL 接入 BUS1；PB0/G5 另接 BUS1.22。

- 参数与网络：`controller=U1 ATmega328P-AU`；`matrix=4 rows x 5 columns`；`row_nets=O1,O2,O3,O4`；`column_nets=A,B,C,D,E`；`bus=SDA,SCL`；`extra_net=G5`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页全图：U1、BUS1、右侧四行五列按键矩阵及同名网络

## 核心器件

### U1

主控制器位号 U1，原理图料号标为 ATmega328P-AU。

- 参数与网络：`reference=U1`；`part_number=ATmega328P-AU`；`package_suffix=AU`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页左下 U1 符号底部 ATmega328P-AU 标注

## 电源

### U1 3V3 供电

U1.4 VCC、U1.6 VCC 和 U1.18 AVCC 连接 3V3；U1.3、U1.5、U1.21 三个 GND 引脚接 GND。

- 参数与网络：`VCC_pin_4=3V3`；`VCC_pin_6=3V3`；`AVCC_pin_18=3V3`；`GND_pins=3,5,21`；`ground_net=GND`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 左侧 VCC/AVCC 三引脚汇接 3V3，底部 GND 三引脚汇接 GND

### BUS1 电源输入

BUS1.4 的 3V3 网络连接 U1 电源，BUS1.1 接 GND；BUS1.2 标为 5V，但图中未画出该脚向 U1 或其他负载的连线。

- 参数与网络：`BUS1_pin_4=3V3`；`BUS1_pin_1=GND`；`BUS1_pin_2_label=5V`；`5V_load_connection_shown=false`；`local_regulator_shown=false`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 BUS1.1 GND、BUS1.4 3V3 外部连线与 BUS1.2 5V 仅符号内标签

## 接口

### 4×5 键盘矩阵

右侧按键区包含 O1、O2、O3、O4 四条水平行线，每条各有五个开关分别连接 A、B、C、D、E 五条列线，共 20 个按键位置。

- 参数与网络：`rows=4`；`columns=5`；`key_positions=20`；`row_nets=O1,O2,O3,O4`；`column_nets=A,B,C,D,E`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页整个右半部，四组 O1~O4 水平行，每组五个开关落到 A~E

### O1 行按键

O1 行中 S1/S4/S7/S10/S13 分别接 A/B/C/D/E，键面标注依次为 AC、7、4、1 和小数点。

- 参数与网络：`A=S1 AC`；`B=S4 7`；`C=S7 4`；`D=S10 1`；`E=S13 decimal point`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页右下 O1 行，位号、键面字符与 A~E 列标注

### O2 行按键

O2 行中 S2/S5/S8/S11/S14 分别接 A/B/C/D/E，键面标注依次为 M、8、5、2、0。

- 参数与网络：`A=S2 M`；`B=S5 8`；`C=S8 5`；`D=S11 2`；`E=S14 0`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页右中下 O2 行，位号、键面字符与 A~E 列标注

### O3 行按键

O3 行中 S3/S6/S9/S12/S15 分别接 A/B/C/D/E，键面标注依次为 %、9、6、3、+/−。

- 参数与网络：`A=S3 %`；`B=S6 9`；`C=S9 6`；`D=S12 3`；`E=S15 +/-`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页右中 O3 行，位号、键面字符与 A~E 列标注

## 总线

### U1 到 BUS1 的 I2C

U1.27 PC4(ADC4/SDA/PCINT12) 通过 SDA 网络连接 BUS1.16，U1.28 PC5(ADC5/SCL/PCINT13) 通过 SCL 网络连接 BUS1.18。

- 参数与网络：`controller_device=U1 ATmega328P-AU`；`sda_pin=U1.27 PC4`；`sda_net=SDA`；`sda_connector=BUS1.16`；`scl_pin=U1.28 PC5`；`scl_net=SCL`；`scl_connector=BUS1.18`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1.27/U1.28 的 SDA/SCL 标签与 BUS1.16/BUS1.18 同名网络

## GPIO 与控制信号

### 按键矩阵行线

U1.23 PC0 接 O1，U1.24 PC1 接 O2，U1.25 PC2 接 O3，U1.26 PC3 接 O4。

- 参数与网络：`O1=U1.23 PC0`；`O2=U1.24 PC1`；`O3=U1.25 PC2`；`O4=U1.26 PC3`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 右上 PC0~PC3 四引脚与 O1~O4 网络标签

### 按键矩阵列线

U1.32 PD2 接 A，U1.1 PD3 接 B，U1.2 PD4 接 C，U1.9 PD5 接 D，U1.10 PD6 接 E。

- 参数与网络：`A=U1.32 PD2`；`B=U1.1 PD3`；`C=U1.2 PD4`；`D=U1.9 PD5`；`E=U1.10 PD6`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 右中 PD2~PD6 与 A~E 网络标签

### G5 网络

U1.12 PB0(PCINT0/CLKO/ICP1) 连接 G5 网络，BUS1.22 也标注并引出 G5。

- 参数与网络：`mcu_pin=U1.12 PB0`；`net=G5`；`connector_pin=BUS1.22`；`direction=not specified by schematic`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1.12 右侧 G5 网络标签与 BUS1.22 外部 G5 标签

## 时钟

### U1 时钟引脚

U1.7 PB6(XTAL1/TOSC1) 与 U1.8 PB7(XTAL2/TOSC2) 在图中标为未连接，页面未显示晶振、谐振器或外部时钟网络。

- 参数与网络：`XTAL1=U1.7 not connected`；`XTAL2=U1.8 not connected`；`external_crystal_shown=false`；`clock_frequency=null`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 右下 PB6/PB7 的 7/8 脚均有未连接波浪标记

## 复位

### U1 RESET

U1.29 PC6(RESET/PCINT14) 接 RESET 网络，RESET 同名网络连接 P1.5；图中未画出上拉电阻、复位按钮或其他复位源。

- 参数与网络：`mcu_pin=U1.29 PC6/RESET`；`net=RESET`；`header_pin=P1.5`；`pullup_shown=false`；`reset_switch_shown=false`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1.29 RESET 标签与下方 P1.5 左侧 RESET 网络；全图无复位上拉或开关

## 内存与 Flash

### 外部存储器

页面未显示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器件及总线。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_interface_shown=false`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页完整原理图，无独立存储器或存储连接器

## 模拟电路

### U1 未用模拟引脚

U1.19 ADC6 与 U1.22 ADC7 在图中标为未连接，U1.20 AREF 也未画外部连接。

- 参数与网络：`ADC6=U1.19 not connected`；`ADC7=U1.22 not connected`；`AREF=U1.20 no external connection shown`
- 证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 上部 ADC6/ADC7 的未连接标记及左侧 AREF 无连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces Calculator | `controller=U1 ATmega328P-AU`；`matrix=4 rows x 5 columns`；`row_nets=O1,O2,O3,O4`；`column_nets=A,B,C,D,E`；`bus=SDA,SCL`；`extra_net=G5` |
| 核心器件 | U1 | `reference=U1`；`part_number=ATmega328P-AU`；`package_suffix=AU` |
| 电源 | U1 3V3 供电 | `VCC_pin_4=3V3`；`VCC_pin_6=3V3`；`AVCC_pin_18=3V3`；`GND_pins=3,5,21`；`ground_net=GND` |
| 电源 | BUS1 电源输入 | `BUS1_pin_4=3V3`；`BUS1_pin_1=GND`；`BUS1_pin_2_label=5V`；`5V_load_connection_shown=false`；`local_regulator_shown=false` |
| 总线 | U1 到 BUS1 的 I2C | `controller_device=U1 ATmega328P-AU`；`sda_pin=U1.27 PC4`；`sda_net=SDA`；`sda_connector=BUS1.16`；`scl_pin=U1.28 PC5`；`scl_net=SCL`；`scl_connector=BUS1.18` |
| 总线地址 | 正文中的 I2C 地址 | `documented_address=0x08`；`address_on_schematic=null`；`address_straps_shown=false`；`address_source=firmware not shown` |
| GPIO 与控制信号 | 按键矩阵行线 | `O1=U1.23 PC0`；`O2=U1.24 PC1`；`O3=U1.25 PC2`；`O4=U1.26 PC3` |
| GPIO 与控制信号 | 按键矩阵列线 | `A=U1.32 PD2`；`B=U1.1 PD3`；`C=U1.2 PD4`；`D=U1.9 PD5`；`E=U1.10 PD6` |
| 接口 | 4×5 键盘矩阵 | `rows=4`；`columns=5`；`key_positions=20`；`row_nets=O1,O2,O3,O4`；`column_nets=A,B,C,D,E` |
| 接口 | O1 行按键 | `A=S1 AC`；`B=S4 7`；`C=S7 4`；`D=S10 1`；`E=S13 decimal point` |
| 接口 | O2 行按键 | `A=S2 M`；`B=S5 8`；`C=S8 5`；`D=S11 2`；`E=S14 0` |
| 接口 | O3 行按键 | `A=S3 %`；`B=S6 9`；`C=S9 6`；`D=S12 3`；`E=S15 +/-` |
| 接口 | O4 行运算键 | `row=O4`；`columns=A,B,C,D,E`；`switch_count=5`；`references=null`；`legends=null` |
| GPIO 与控制信号 | G5 网络 | `mcu_pin=U1.12 PB0`；`net=G5`；`connector_pin=BUS1.22`；`direction=not specified by schematic` |
| 接口 | 正文中的 INT 映射 | `schematic_net=G5`；`schematic_pin=BUS1.22`；`mcu_pin=U1.12 PB0`；`documented_name=INT`；`polarity=null`；`direction=null` |
| 复位 | U1 RESET | `mcu_pin=U1.29 PC6/RESET`；`net=RESET`；`header_pin=P1.5`；`pullup_shown=false`；`reset_switch_shown=false` |
| 时钟 | U1 时钟引脚 | `XTAL1=U1.7 not connected`；`XTAL2=U1.8 not connected`；`external_crystal_shown=false`；`clock_frequency=null` |
| 模拟电路 | U1 未用模拟引脚 | `ADC6=U1.19 not connected`；`ADC7=U1.22 not connected`；`AREF=U1.20 no external connection shown` |
| 接口 | U1 PD0/PD1 外引路径 | `PD0=U1.30 RXD via 10K to label 16`；`PD1=U1.31 TXD via 10K to label 17`；`resistor_references=null`；`connector_mapping=null` |
| 调试与烧录 | P1 Header 6 | `reference=P1`；`part_number=Header 6`；`pin_count=6`；`reset_visible=P1.5 RESET`；`ground_visible=true`；`complete_pin_map=null`；`isp_standard_pinout_confirmed=false` |
| 保护电路 | 接口保护与电源去耦 | `i2c_protection_shown=false`；`key_debounce_components_shown=false`；`power_protection_shown=false`；`decoupling_capacitors_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_interface_shown=false` |

## 待确认事项

- `address.documented-i2c-0x08`：产品正文给出 I2C 从机地址 0x08，但当前原理图只显示 SDA/SCL 硬件连线，没有地址跳线、地址电阻或 0x08 标注；地址需由固件或配置资料确认。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 与 BUS1 的 SDA/SCL 范围，无 0x08 或地址配置器件）
- `interface.row-o4-keys`：O4 行明确包含五个开关并分别连接 A~E，但当前图像中的五个位号和键面字符无法可靠逐项辨认。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页右上 O4 行五个开关，位号与键面文字在 1179×922 页面中不清晰）
- `interface.documented-int-name`：产品正文将 Faces Panel Bus Pin 22 标为 INT，而原理图在 BUS1.22 和 U1.12 PB0 处使用网络名 G5；INT 的有效极性、方向与固件语义无法从原理图确认。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页 BUS1.22 与 U1.12 均标 G5，页面无 INT 字样或极性标记）
- `interface.pd0-pd1-resistor-paths`：U1.30 PD0(RXD) 与 U1.31 PD1(TXD) 各经一只标注 10K 的串联电阻向右引出，末端分别标注 16 和 17；电阻位号及 16/17 与 BUS1 的准确连接方式在当前页面中不够清楚。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页 U1 右侧 PD0/PD1 两条 10K 电阻路径，电阻位号不清，右端数字 16/17）
- `debug.p1-header-pinout`：P1 是六针接口，图中可见其连接 U1 PB 端口、RESET 与 GND，但多条水平线在当前图像中难以可靠对应到 P1.1~P1.6，不能据产品正文直接补成标准 ISP 针序。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页下部中右 P1 Header 6 与 U1 PB1~PB5、RESET、GND 连线交汇区域）
- `protection.filtering-not-shown`：本页未展示 SDA/SCL/G5 的 ESD 或串联保护、按键去抖器件、电源反接/过流保护以及 VCC/AVCC 去耦电容；不能据此确认量产板是否另有未展示器件。（证据：图 9698c28b8392 / 第 1 页 / 第 1 页完整原理图仅含 BUS1、U1、P1、两只 10K 电阻和按键矩阵，未见保护或电容器件）
- `review.i2c-address`：请通过 A005 当前固件或协议资料确认 I2C 7-bit 从机地址是否固定为 0x08，是否存在可配置方式。；原因：I2C 地址属于固件行为，当前原理图只有 SDA/SCL 连线，没有地址标注或硬件配置。
- `review.o4-switch-labels`：请用更高分辨率原理图或 BOM/键帽图确认 O4 行五个开关的位号和 A~E 对应键面字符。；原因：当前 WebP 中 O4 行的位号与运算符文字无法可靠转录。
- `review.g5-int-semantics`：BUS1.22 的 G5 是否由固件作为 INT 使用，其方向、有效电平和触发条件是什么？；原因：原理图只给出 PB0-G5-BUS1.22 连接，INT 名称仅见于产品正文。
- `review.pd0-pd1-paths`：请确认 PD0/PD1 两只 10K 电阻的位号，以及右端 16/17 是否对应 BUS1 的 GPIO16/GPIO17 或其他测试节点。；原因：当前页面可见数值与端点数字，但电阻位号和跨区域网络连接不够清晰。
- `review.p1-pinout`：请提供 P1 六针接口的逐针定义和观察方向，并确认其是否为 Mega328 ISP 下载接口。；原因：当前图像的多条 PB 端口线与 P1 针脚难以逐一辨认，不能用标准 ISP 经验补全。
- `review.protection-decoupling`：请确认 A005 量产板是否包含原理图本页未展示的去耦、I2C/按键接口保护或其他电源保护器件。；原因：当前单页资源未画这些器件，无法区分设计省略与实际不存在。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9698c28b8392f366835b47e6ee943835d02229ee7aa23d007464511885ff8915` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_sch_01.webp` |

---

源文档：`zh_CN/module/faces_calculator.md`

源文档 SHA-256：`6aa012baff1638339db9f8417db11300eab1690107c5b0b8061241642f93581e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
