# Unit NeoHEX 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NeoHEX |
| SKU | A045-B |
| 产品 ID | `unit-neohex-95295c2bb825` |
| 源文档 | `zh_CN/unit/neohex.md` |

## 概述

Unit NeoHEX（A045-B）由 U1~U37 共 37 颗 WS2812C-2020 可寻址 RGB LED 串联组成，数据从 S-IN 进入 U1 DI，经过全部灯珠后由 U37 DO 输出 S-OUT。J1 Grove 和 J3 Header 4 并联提供 S-IN、VCC_5V 与 GND 输入，J2 Grove 提供 S-OUT、VCC_5V 与 GND 级联输出；所有 LED 直接使用 VCC_5V。C1~C13 共 13 只 100nF/50V 电容并联在 VCC_5V 与 GND 之间，第 2 张图显示 LED 按 4-5-6-7-6-5-4 的六边形行列排布。原理图未标注 LED 的 -V1 完整后缀、额定供电范围、功耗或刷新/亮度参数。

## 检索关键词

`Unit NeoHEX`、`A045-B`、`NeoHEX`、`WS2812C-2020`、`U1-U37`、`37 RGB LED`、`S-IN`、`S-OUT`、`S6-OUT`、`S12-OUT`、`S18-OUT`、`S24-OUT`、`S30-OUT`、`S36-OUT`、`VCC_5V`、`GND`、`J1 GROVE`、`J2 GROVE`、`J3 Header 4`、`IO1`、`IO2`、`DI`、`DO`、`VDD`、`C1-C13`、`100nF/50V`、`single-wire RGB`、`LED cascade`、`4-5-6-7-6-5-4`、`WS2812C-2020-V1`、`Grove input`、`Grove output`、`级联灯板`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1-U37 | WS2812C-2020 | 37 颗串行级联的可寻址 RGB LED，每颗含 DI、DO、VDD 和 GND | 图 77156c238ead / 第 1 页 / 第 1 张第 1 页 B1:D4 区域 U1~U37，全部标 WS2812C-2020，pin 1 DO、pin 2 GND、pin 3 DI、pin 4 VDD; 图 5a335794b0fc / 第 1 页 / 第 2 张第 1 页六边形板轮廓内 U1~U37 的物理位置 |
| J1 | GROVE | 主数据/电源输入接口，IO1 接 S-IN、5V 接 VCC_5V、GND 接地，IO2 未连接 | 图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1 左上 J1 GROVE，IO2 未连接叉号、IO1 S-IN、5V VCC_5V、GND |
| J2 | GROVE | 数据/电源级联输出接口，IO1 接 S-OUT、5V 接 VCC_5V、GND 接地，IO2 未连接 | 图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1 左上 J2 GROVE，IO2 未连接叉号、IO1 S-OUT、5V VCC_5V、GND |
| J3 | Header 4 | 第二组数据/电源输入接口，pin 3 S-IN、pin 2 VCC_5V、pin 1 GND，pin 4 未连接 | 图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A2 J3 Header 4，pins 4~1 对应 NC/S-IN/VCC_5V/GND |
| C1-C13 | 100nF/50V | VCC_5V 到 GND 的 13 只并联电源去耦电容 | 图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A3:A4，C1~C13 均标 100nF/50V 并联在 VCC_5V 与 GND 母线之间 |

## 系统结构

### Unit NeoHEX 系统架构

U1~U37 形成 37 级 WS2812C-2020 串行 RGB LED 链；J1/J3 提供并联输入，J2 提供级联输出，C1~C13 对 VCC_5V 去耦。

- 参数与网络：`leds=U1-U37 WS2812C-2020`；`input_connectors=J1 GROVE,J3 Header 4`；`output_connector=J2 GROVE`；`data_path=S-IN -> U1...U37 -> S-OUT`；`power=VCC_5V`；`decoupling=C1-C13 100nF/50V`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页完整接口、LED 链和去耦电容网络

## 核心器件

### WS2812C-2020 引脚映射

每颗 U1~U37 的 pin 1 为 DO、pin 2 为 GND、pin 3 为 DI、pin 4 为 VDD；VDD 接 VCC_5V，GND 接公共地。

- 参数与网络：`pin_1=DO`；`pin_2=GND`；`pin_3=DI`；`pin_4=VDD VCC_5V`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 U1~U37 重复符号内 DO/GND/DI/VDD 与 pins 1~4

## 电源

### VCC_5V 公共电源轨

J1 5V、J2 5V、J3 pin 2 和 U1~U37 VDD 全部连接 VCC_5V；本页没有稳压器、LDO、DC/DC、负载开关、充电器、电池或电源监测器。

- 参数与网络：`rail=VCC_5V`；`inputs=J1 5V,J3 pin 2`；`cascade_output=J2 5V`；`loads=U1-U37 pin 4 VDD`；`converter=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页所有 VCC_5V 同名网络与 LED VDD，整页无电源转换器件

### LED 电源去耦

C1~C13 均为 100nF/50V，并联在 VCC_5V 和 GND 母线之间；图中注释 RGB*37,C*13 与 37 颗 LED/13 颗电容数量相符。

- 参数与网络：`capacitors=C1-C13`；`value=100nF`；`rating=50V`；`rail=VCC_5V`；`return=GND`；`count=13`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A3:A4 C1~C13 标注 100nF/50V 与 A2 RGB*37,C*13 注释

## 接口

### J1 Grove 输入接口

J1 的 IO1 触点接 S-IN，5V 触点接 VCC_5V，GND 触点接地，IO2 触点以未连接标记结束。

- 参数与网络：`IO1=S-IN，数据输入`；`IO2=NC`；`5V=VCC_5V，电源输入`；`GND=GND`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1 J1 GROVE 四个逻辑触点及网络

### J2 Grove 级联输出接口

J2 的 IO1 触点接 S-OUT，5V 触点接 VCC_5V，GND 触点接地，IO2 触点以未连接标记结束。

- 参数与网络：`IO1=S-OUT，数据输出`；`IO2=NC`；`5V=VCC_5V，级联电源`；`GND=GND`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1 J2 GROVE 四个逻辑触点及网络

### J3 Header 4 输入接口

J3 pin 1 为 GND，pin 2 为 VCC_5V，pin 3 为 S-IN，pin 4 未连接；S-IN 和 VCC_5V 与 J1 对应网络并联。

- 参数与网络：`pin_1=GND`；`pin_2=VCC_5V`；`pin_3=S-IN`；`pin_4=NC`；`parallel_with=J1 S-IN/VCC_5V/GND`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A2 J3 pins 1~4 与同名网络，J1 同名 S-IN/VCC_5V/GND

## 总线

### 37 级单线 LED 数据链

S-IN 接 U1 DI，前一级 DO 逐级接后一级 DI，U37 DO 输出 S-OUT；链中每 6 颗在图上以 S6-OUT、S12-OUT、S18-OUT、S24-OUT、S30-OUT、S36-OUT 标记边界。

- 参数与网络：`input=S-IN -> U1 pin 3 DI`；`chain=U1 DO -> U2 DI -> ... -> U37 DI`；`output=U37 pin 1 DO -> S-OUT`；`boundary_nets=S6-OUT,S12-OUT,S18-OUT,S24-OUT,S30-OUT,S36-OUT`；`device_count=37`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 D1:D4 底行与 B1:B4 顶行串行连线及 S6/S12/S18/S24/S30/S36 边界网络

### 其他标准总线与地址

原理图未显示 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S，也没有器件地址或片选网络。

- 参数与网络：`led_serial=S-IN/S-OUT`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null`；`chip_select=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页全部网络仅 S-IN/S-OUT/中间级联/VCC_5V/GND

## 时钟

### 时钟、复位与调试

本页未显示独立晶振/时钟、RESET、BOOT、EN、中断或调试接口；LED 控制仅通过 S-IN 串行数据链。

- 参数与网络：`clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`control=S-IN`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页全部接口与 LED 网络，无时钟/复位/调试信号

## 保护电路

### 数据与电源保护

S-IN、S-OUT 和 VCC_5V 接口路径未显示 TVS/ESD、保险丝、限流、反接或过压保护器件。

- 参数与网络：`data_tvs=null`；`power_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 J1/J2/J3 到 LED/电源母线的直接连接，无保护器件位号

## 关键网络

### S-IN 并联输入

J1 IO1 与 J3 pin 3 使用同一 S-IN 网络并直接连接 U1 DI，页面未显示输入选择开关、缓冲器、串联电阻或电平转换器。

- 参数与网络：`sources=J1 IO1,J3 pin 3`；`destination=U1 pin 3 DI`；`selector=null`；`buffer=null`；`series_resistor=null`；`level_shifter=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1:A2 J1/J3 S-IN 与 D1 U1 DI 同名网络

### S-OUT 级联输出

U37 DO 连接 S-OUT，S-OUT 直接引到 J2 IO1；页面未显示输出缓冲或保护器件。

- 参数与网络：`source=U37 pin 1 DO`；`net=S-OUT`；`connector=J2 IO1`；`buffer=null`；`protection=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A4 U37 DO S-OUT 与 A1 J2 IO1 S-OUT

## 存储

### 外部存储与内存

两张图均未显示独立 Flash、EEPROM、RAM、SD 卡或其他外部存储器件。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页仅连接器、U1~U37 和 C1~C13; 图 5a335794b0fc / 第 1 页 / 第 2 张第 1 页仅显示 U1~U37 物理布局

## 其他事实

### 37 颗 LED 物理排布

第 2 张图将 U1~U37 排成七行，逐行数量为 4、5、6、7、6、5、4，位于六边形板轮廓内。

- 参数与网络：`rows=4,5,6,7,6,5,4`；`total=37`；`shape=hexagonal`；`references=U1-U37`
- 证据：图 5a335794b0fc / 第 1 页 / 第 2 张第 1 页完整六边形板图，U1~U37 七行物理布局

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NeoHEX 系统架构 | `leds=U1-U37 WS2812C-2020`；`input_connectors=J1 GROVE,J3 Header 4`；`output_connector=J2 GROVE`；`data_path=S-IN -> U1...U37 -> S-OUT`；`power=VCC_5V`；`decoupling=C1-C13 100nF/50V` |
| 核心器件 | WS2812C-2020 引脚映射 | `pin_1=DO`；`pin_2=GND`；`pin_3=DI`；`pin_4=VDD VCC_5V` |
| 总线 | 37 级单线 LED 数据链 | `input=S-IN -> U1 pin 3 DI`；`chain=U1 DO -> U2 DI -> ... -> U37 DI`；`output=U37 pin 1 DO -> S-OUT`；`boundary_nets=S6-OUT,S12-OUT,S18-OUT,S24-OUT,S30-OUT,S36-OUT`；`device_count=37` |
| 接口 | J1 Grove 输入接口 | `IO1=S-IN，数据输入`；`IO2=NC`；`5V=VCC_5V，电源输入`；`GND=GND` |
| 接口 | J2 Grove 级联输出接口 | `IO1=S-OUT，数据输出`；`IO2=NC`；`5V=VCC_5V，级联电源`；`GND=GND` |
| 接口 | J3 Header 4 输入接口 | `pin_1=GND`；`pin_2=VCC_5V`；`pin_3=S-IN`；`pin_4=NC`；`parallel_with=J1 S-IN/VCC_5V/GND` |
| 关键网络 | S-IN 并联输入 | `sources=J1 IO1,J3 pin 3`；`destination=U1 pin 3 DI`；`selector=null`；`buffer=null`；`series_resistor=null`；`level_shifter=null` |
| 关键网络 | S-OUT 级联输出 | `source=U37 pin 1 DO`；`net=S-OUT`；`connector=J2 IO1`；`buffer=null`；`protection=null` |
| 电源 | VCC_5V 公共电源轨 | `rail=VCC_5V`；`inputs=J1 5V,J3 pin 2`；`cascade_output=J2 5V`；`loads=U1-U37 pin 4 VDD`；`converter=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null` |
| 电源 | LED 电源去耦 | `capacitors=C1-C13`；`value=100nF`；`rating=50V`；`rail=VCC_5V`；`return=GND`；`count=13` |
| 其他事实 | 37 颗 LED 物理排布 | `rows=4,5,6,7,6,5,4`；`total=37`；`shape=hexagonal`；`references=U1-U37` |
| 保护电路 | 数据与电源保护 | `data_tvs=null`；`power_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null` |
| 时钟 | 时钟、复位与调试 | `clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`control=S-IN` |
| 存储 | 外部存储与内存 | `flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他标准总线与地址 | `led_serial=S-IN/S-OUT`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null`；`chip_select=null` |
| 核心器件 | LED 完整型号后缀 | `schematic_part_number=WS2812C-2020`；`candidate_from_product_doc=WS2812C-2020-V1`；`confirmed_suffix=null` |
| 接口 | J1/J2 数字针号 | `J1_contacts=IO2 NC,IO1 S-IN,5V VCC_5V,GND`；`J2_contacts=IO2 NC,IO1 S-OUT,5V VCC_5V,GND`；`numeric_pin_order=null` |
| 电源 | LED 电源与性能额定参数 | `rail_label=VCC_5V`；`voltage_range=null`；`maximum_current=null`；`full_white_power=null`；`brightness_levels=null`；`color_count=null`；`refresh_rate=null` |

## 待确认事项

- `component.led-full-part-number`：原理图中 U1~U37 均标 WS2812C-2020，未显示 -V1 后缀，因此不能仅凭图纸确认完整订货型号为 WS2812C-2020-V1。（证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 U1~U37 符号下均标 WS2812C-2020）
- `interface.grove-numeric-pinout`：J1/J2 符号明确给出 IO2、IO1、5V、GND 四个触点及网络，但没有显示数字针号，无法仅凭本页把这些触点无歧义映射到 pin 1~4。（证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 A1 J1/J2 GROVE 符号，显示触点名但无 pin 1~4 数字）
- `power.performance-ratings`：原理图只将电源轨命名为 VCC_5V，没有标注允许供电范围、最大电流、全亮功耗、亮度级数、颜色数或刷新速率。（证据：图 77156c238ead / 第 1 页 / 第 1 张第 1 页 VCC_5V 母线、LED 和接口；整页无额定范围或性能数字）
- `review.led-full-part-number`：U1~U37 的完整订货型号是否为 WS2812C-2020-V1？；原因：图纸只标 WS2812C-2020，版本后缀需 BOM、采购资料或实物丝印确认。
- `review.grove-numeric-pinout`：J1 和 J2 的 IO2、IO1、5V、GND 分别对应数字 pin 1~4 的哪一针？；原因：GROVE 符号未显示数字针号；需连接器封装、PCB 或装配图确认。
- `review.power-performance-ratings`：该硬件版本的允许供电范围、最大/全亮电流、亮度级数和刷新能力是什么？；原因：这些是 LED 版本与系统性能参数，原理图仅给 VCC_5V 网络名。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `77156c238eadb7f29026bc3dbc259ea8a81acbb337f8749e588dae16d55044fa` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/Sch_NeoHex_V1.1_sch_01.png` |
| 2 | 1 | `5a335794b0fc4b2d6b1bf7021f26ba6fef4b425b5bcda1d39bf10064f1380e5a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/Sch_NeoHex_V1.1_sch_02.jpg` |

---

源文档：`zh_CN/unit/neohex.md`

源文档 SHA-256：`550ba8628fc28f677e24f1527cbf0e70689a4c98a269443d8149f540f2b82f74`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
