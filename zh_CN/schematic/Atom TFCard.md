# Atom TFCard 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom TFCard |
| SKU | K044 |
| 产品 ID | `atom-tfcard-5266b3dbdf9d` |
| 源文档 | `zh_CN/atom/atomictf.md` |

## 概述

Atom TFCard 是由 U1 TF-015 卡座、Rp1 四联 4.7KΩ偏置阵列、P1/P2 Atom 接口和 C1 100nF 去耦组成的直接连接电路。卡座 MOSI、CLK、MISO 分别连接 P1 pins3/4/5；CS 只经 Rp1 上拉到 3.3V，没有连接 Atom GPIO。P1 pin2 另标 GPS_T，但未接 U1，因此本页只能确认三条存储信号、3.3V 供电与 GND，不能确认实际协议模式、CS 初始化或正文中的 GPIO 编号。正文中的最高 16G、FAT/FAT32 和自弹结构不属于本页电气证据，需要软件、BOM 或结构资料确认。

## 检索关键词

`Atom TFCard`、`K044`、`TF-015`、`TF card`、`microSD`、`MOSI`、`CLK`、`MISO`、`CS`、`GPS_T`、`G19`、`G23`、`G33`、`3.3V`、`5VIN`、`Rp1 4.7KΩ`、`C1 100nF`、`16G`、`FAT`、`FAT32`、`self-eject`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TF-015 | TF/microSD 卡座，连接 CS、MOSI、CLK、MISO、3.3V 和 GND | 图 3d4abface7a9 / 第 1 页 / 第 1 页左侧 U1 TF-015，pins2-7 为 CS/MOSI/VCC/CLK/GND/MISO |
| Rp1 | 4 x 4.7KΩ (472) ±5% | U1 CS/MOSI/CLK/MISO 的上拉或下拉电阻阵列 | 图 3d4abface7a9 / 第 1 页 / 第 1 页左上 Rp1，top pins8/7/6 接 +3.3V、top pin5 接 GND，bottom pins1-4 接 U1 CS/MOSI/CLK/MISO |
| P1,P2 | Header 5 / Header 4 | Atom 主机的 3.3V、5VIN、GPS_T、MOSI、CLK、MISO 与 GND 接口 | 图 3d4abface7a9 / 第 1 页 / 第 1 页中右 P2 Header4 与 P1 Header5，P2 pins1/2 NC、pin3 +5VIN、pin4 GND，P1 pins1-5 为 +3.3V/GPS_T/MOSI/CLK/MISO |
| C1 | 100nF (104) 10% 50V | 3.3V 到 GND 的本地去耦电容 | 图 3d4abface7a9 / 第 1 页 / 第 1 页右侧 C1 100nF (104) 10% 50V，连接 +3.3V 与 GND |

## 系统结构

### Atom TFCard 直接连接架构

U1 TF-015 的 VCC 接 P1 +3.3V，GND 接系统 GND，MOSI、CLK、MISO 三线直接连接 P1；电路未显示控制器、电平转换器或主机 CS 连线。

- 参数与网络：`card_socket=U1 TF-015`；`host_signals=MOSI,CLK,MISO`；`card_select_host_line=null`；`supply=+3.3V`；`ground=GND`；`controller_present=false`；`level_shifter_present=false`
- 证据：图 3d4abface7a9 / 第 1 页 / 第 1 页完整单页：U1/Rp1/P1/P2/C1 全部器件与连线

## 电源

### Atom TFCard 电源连接

P1 pin1 的 +3.3V 直接连接 U1 VCC pin4，并由 C1 100nF 去耦到 GND；P2 pin4 提供系统 GND，P2 pin3 的 +5VIN 在本页没有连接其他负载。

- 参数与网络：`card_supply=P1 pin1 +3.3V -> U1 pin4 VCC`；`decoupling=C1 100nF (104) 10% 50V`；`ground=P2 pin4 GND and U1 pin6 GND`；`five_volt_input=P2 pin3 +5VIN`；`five_volt_consumers=none shown`
- 证据：图 3d4abface7a9 / 第 1 页 / 第 1 页 U1 VCC/GND、P1 +3.3V、P2 +5VIN/GND 与 C1

## 接口

### P1/P2 Atom 主机接口

P1 pins1-5 依次连接 +3.3V、GPS_T、MOSI、CLK、MISO；P2 pins1/2 标为未连接，pin3 接 +5VIN，pin4 接 GND。

- 参数与网络：`P1_pin1=+3.3V`；`P1_pin2=GPS_T`；`P1_pin3=MOSI`；`P1_pin4=CLK`；`P1_pin5=MISO`；`P2_pin1=NC`；`P2_pin2=NC`；`P2_pin3=+5VIN`；`P2_pin4=GND`
- 证据：图 3d4abface7a9 / 第 1 页 / 第 1 页中右 P2 Header4、P1 Header5 的 pin1-pin5 网络与 NC 标记

## 存储

### U1 TF-015 卡座引脚

U1 pin2 为 CS，pin3 为 MOSI，pin4 接 +3.3V，pin5 为 CLK，pin6 接 GND，pin7 为 MISO；图中未显示该符号的其他卡信号。

- 参数与网络：`pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO`
- 证据：图 3d4abface7a9 / 第 1 页 / 第 1 页左侧 U1 pins2-7 的文字与网络标签

### TF-015 信号偏置

Rp1 为四联 4.7KΩ阵列：CS、MOSI、CLK 三路分别通过电阻接 +3.3V，MISO 通过第四路电阻接 GND。

- 参数与网络：`array=Rp1 4 x 4.7KΩ (472) ±5%`；`CS=4.7KΩ to +3.3V`；`MOSI=4.7KΩ to +3.3V`；`CLK=4.7KΩ to +3.3V`；`MISO=4.7KΩ to GND`
- 证据：图 3d4abface7a9 / 第 1 页 / 第 1 页左上 Rp1 top/bottom pins 与 +3.3V/GND、U1 CS/MOSI/CLK/MISO

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom TFCard 直接连接架构 | `card_socket=U1 TF-015`；`host_signals=MOSI,CLK,MISO`；`card_select_host_line=null`；`supply=+3.3V`；`ground=GND`；`controller_present=false`；`level_shifter_present=false` |
| 存储 | U1 TF-015 卡座引脚 | `pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO` |
| 存储 | TF-015 信号偏置 | `array=Rp1 4 x 4.7KΩ (472) ±5%`；`CS=4.7KΩ to +3.3V`；`MOSI=4.7KΩ to +3.3V`；`CLK=4.7KΩ to +3.3V`；`MISO=4.7KΩ to GND` |
| 接口 | P1/P2 Atom 主机接口 | `P1_pin1=+3.3V`；`P1_pin2=GPS_T`；`P1_pin3=MOSI`；`P1_pin4=CLK`；`P1_pin5=MISO`；`P2_pin1=NC`；`P2_pin2=NC`；`P2_pin3=+5VIN`；`P2_pin4=GND` |
| 电源 | Atom TFCard 电源连接 | `card_supply=P1 pin1 +3.3V -> U1 pin4 VCC`；`decoupling=C1 100nF (104) 10% 50V`；`ground=P2 pin4 GND and U1 pin6 GND`；`five_volt_input=P2 pin3 +5VIN`；`five_volt_consumers=none shown` |
| 存储 | TF-015 存储接口协议模式 | `documented_bus=SPI`；`host_signals=MOSI,CLK,MISO`；`host_cs=null`；`card_cs=Rp1 4.7KΩ pull-up to +3.3V`；`unused_host_signal=P1 pin2 GPS_T`；`mode=null` |
| GPIO 与控制信号 | 正文中的 Atom GPIO 映射 | `documented_G19=MOSI`；`documented_G23=CLK`；`documented_G33=MISO`；`schematic_pins=P1 pin3 MOSI, pin4 CLK, pin5 MISO`；`gpio_labels_on_schematic=null` |
| 存储 | 正文中的容量与文件系统 | `documented_max_capacity=16G`；`documented_filesystems=FAT,FAT32`；`schematic_socket=U1 TF-015`；`schematic_capacity=null`；`schematic_filesystem=null` |
| 存储 | 正文中的自弹式卡槽 | `documented_mechanism=self-eject`；`schematic_designator=U1 TF-015`；`mechanical_detail_visible=false` |

## 待确认事项

- `storage.card-interface-mode`：正文与管脚表把 MOSI/CLK/MISO 描述为 SPI，但原理图没有从 Atom 引出 CS；U1 CS 仅经 4.7KΩ上拉到 3.3V，P1 pin2 的 GPS_T 也未连接卡座，因此无法确认实际协议模式和初始化方式。（证据：图 3d4abface7a9 / 第 1 页 / 第 1 页 U1 CS 仅连接 Rp1 上拉；P1 MOSI/CLK/MISO 直连 U1，GPS_T 未接 U1）
- `gpio.documented-atom-map`：正文管脚表给出 G19=MOSI、G23=CLK、G33=MISO；原理图只在 P1 pins3/4/5 标出 MOSI/CLK/MISO 网络名，没有显示 G19/G23/G33，因此 GPIO 编号需由主机针脚定义或实测确认。（证据：图 3d4abface7a9 / 第 1 页 / 第 1 页 P1 pins3/4/5 仅标 MOSI/CLK/MISO，图中无 G19/G23/G33）
- `storage.documented-capacity-filesystem`：正文称最高支持 16G，并支持 FAT/FAT32；原理图只显示 TF-015 卡座和三条存储信号，没有容量、卡标准或文件系统标注，无法单独确认这些软件与介质兼容性。（证据：图 3d4abface7a9 / 第 1 页 / 第 1 页 U1 仅标 TF-015 与电气引脚，图中无 16G、FAT 或 FAT32）
- `storage.documented-self-eject-slot`：正文称采用自弹式卡槽，但原理图符号只标 U1 TF-015，没有机械机构、料号版本或结构尺寸，无法由本页确认自弹机制。（证据：图 3d4abface7a9 / 第 1 页 / 第 1 页 U1 TF-015 仅为电气符号，无卡槽机械剖面或 BOM 型号）
- `review.storage-interface-mode`：K044 的 TF-015 实际使用 SPI 还是其他三线 SD 模式，软件初始化如何处理未引出的 CS？；原因：图纸只有 MOSI/CLK/MISO 主机线，CS 仅 4.7KΩ上拉，不能据此确认协议模式和片选策略。
- `review.atom-gpio-map`：K044 当前适配的 Atom 主机是否均把 P1 pins3/4/5 定义为 G19/G23/G33，且分别承载 MOSI/CLK/MISO？；原因：原理图只给出 P1 物理针脚和网络名，GPIO 编号来自产品正文，需要主机版本针脚表或实测确认。
- `review.capacity-filesystem-support`：最高 16G 与 FAT/FAT32 支持由哪些主机固件、库版本和卡类型测试确认？；原因：容量和文件系统由卡介质及软件栈共同决定，原理图卡座连接不能证明兼容边界。
- `review.self-eject-bom`：K044 当前量产卡座的完整 BOM 型号是否确认具备自弹机构？；原因：TF-015 电气符号不足以证明机械结构，需要 BOM、结构图或实物确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3d4abface7a9b356c8350c26f1ae7deb1e5cda1f7ba2f24212b3f67fea0a67d2` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_sch_01.webp` |

---

源文档：`zh_CN/atom/atomictf.md`

源文档 SHA-256：`e93ca8aa32461fec969f16c259e6db0688cfa6448e462c8472d1d75e5662bc4a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
