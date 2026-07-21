# Base Bottom v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base Bottom v1.1 |
| SKU | C001-C2 |
| 产品 ID | `base-bottom-v1-1-8ff41491e8be` |
| 源文档 | `zh_CN/base/BLACK-BOTTOM_V1.1.md` |

## 概述

Base Bottom v1.1 原理图是一页无有源芯片的 M5Stack_BUS 扩展与电池开关电路。J1 的电源、EN 和 GPIO 网络被选择性引到 P1/P2/P3/P4，其中 P1 与 P4、P2 与 P3 分别是同一组电气网络的不同功能标签。J2 两针电池接口的正端经 S1 SPDT 开关接 BAT，负端接 GND；图中未显示充电、保护或电量检测电路。源文档标注的 110mAh 锂电属性和部分 NC 映射不能由本页单独确认。

## 检索关键词

`Base Bottom v1.1`、`C001-C2`、`M5Stack_BUS`、`Header 8`、`Header 15`、`SW-SPDT`、`BAT`、`+5V`、`+3.3V`、`GND`、`EN`、`SDA`、`SCL`、`MOSI`、`MISO`、`SCK`、`GPIO21`、`GPIO22`、`GPIO23`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | M5Stack_BUS | 30 针 M5Stack 堆叠总线接口 | 图 9327655fc1c8 / 第 1 页 / 第 1 页右侧 J1，器件值标注 M5Stack_BUS，显示 pins1-30 |
| P1 | Header 8 | 5V、3V3、GND 与 GPIO21/22/23/19/18 的八针扩展排针 | 图 9327655fc1c8 / 第 1 页 / 第 1 页中上 P1 Header 8，标注 5V、3V3、G、21、22、23、19、18 |
| P4 | Header 8A | P1 同组网络的电源、I2C 与 SPI 功能标签排针 | 图 9327655fc1c8 / 第 1 页 / 第 1 页中下 P4 Header 8A，标注 5V、3V3、G、SDA、SCL、MOSI、MISO、SCK |
| P2 | Header 15 | 十路 GPIO、EN、BAT 与三路电源的十五针扩展排针 | 图 9327655fc1c8 / 第 1 页 / 第 1 页左中 P2 Header 15，右侧连接 G3/G1/G16/G17/G2/G5/G25/G26/G35/G36/EN/BAT/+3.3V/+5V/GND |
| P3 | Header 15A | P2 同组网络的串口、数字、模拟与电源功能标签排针 | 图 9327655fc1c8 / 第 1 页 / 第 1 页中右 P3 Header 15A，内部标注 R0/T0/R2/T2/G2/G5/DA/DA/AD/AD/RST/BAT/3V3/5V/G |
| S1 | SW-SPDT | J2 电池正端与 BAT 网络之间的三脚选择开关 | 图 9327655fc1c8 / 第 1 页 / 第 1 页下方 S1 SW-SPDT，pin2 接 BAT、pin1 接 J2 pin1、pin3 未接出 |
| J2 | Header 2 | 两针电池接口 | 图 9327655fc1c8 / 第 1 页 / 第 1 页下方 J2 Header 2，pin1 接 S1 pin1、pin2 接 GND |

## 系统结构

### Base Bottom v1.1 电路结构

本页由 J1 M5Stack_BUS、P1/P4 两组八针排针、P2/P3 两组十五针排针以及 S1/J2 电池开关接口组成，没有显示有源芯片或无源阻容器件。

- 参数与网络：`stack_bus=J1 M5Stack_BUS`；`eight_pin_headers=P1,P4`；`fifteen_pin_headers=P2,P3`；`battery_switch=S1 SW-SPDT`；`battery_connector=J2 Header 2`；`active_components_shown=false`；`passive_components_shown=false`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页全图，仅见 J1/J2、P1-P4 与 S1

## 电源

### S1 与 J2 电池连接

S1 pin2 接 BAT，pin1 接 J2 pin1，pin3 未接出；J2 pin2 接 GND。S1 切换到 pin1 时把 J2 pin1 接到 BAT，切换到 pin3 时断开该正端路径。

- 参数与网络：`switch=S1 SW-SPDT`；`common=pin2 BAT`；`switched_output=pin1 -> J2 pin1`；`open_throw=pin3 NC`；`battery_ground=J2 pin2 GND`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页下方 BAT-S1-J2-GND 连接区域，显示 S1 pins1/2/3 与 J2 pins1/2

### 电池辅助电路

本页没有显示电池充电器、保护器、保险丝、电量计或 BAT 电压采样器件，电池接口只通过 S1、BAT 与 GND 接入总线。

- 参数与网络：`charger_shown=false`；`protection_ic_shown=false`；`fuse_shown=false`；`fuel_gauge_shown=false`；`voltage_sense_shown=false`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页全图与下方 S1/J2 区域，除连接器和开关外无电池辅助器件

## 接口

### P1 Header 8

P1 左到右八个位置依次连接 +5V、+3.3V、GND、G21、G22、G23、G19、G18。

- 参数与网络：`order_left_to_right=+5V,+3.3V,GND,G21,G22,G23,G19,G18`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页中上 P1 Header 8 的八根垂直线及下方网络名

### P4 Header 8A

P4 左到右的 5V、3V3、G、SDA、SCL、MOSI、MISO、SCK 分别连接 +5V、+3.3V、GND、G21、G22、G23、G19、G18。

- 参数与网络：`pin_labels_left_to_right=5V,3V3,G,SDA,SCL,MOSI,MISO,SCK`；`nets_left_to_right=+5V,+3.3V,GND,G21,G22,G23,G19,G18`；`sda_gpio=21`；`scl_gpio=22`；`mosi_gpio=23`；`miso_gpio=19`；`sck_gpio=18`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页中下 P4 Header 8A 的内部功能标签、垂直线与上方 Gxx 网络名

### P1 与 P4 的网络对应

P1 与 P4 按相同的左到右顺序连接同一组八条网络；P4 将 G21/G22 标为 SDA/SCL，将 G23/G19/G18 标为 MOSI/MISO/SCK。

- 参数与网络：`shared_nets=+5V,+3.3V,GND,G21,G22,G23,G19,G18`；`functional_aliases=G21:SDA,G22:SCL,G23:MOSI,G19:MISO,G18:SCK`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页中部上下相对的 P1 与 P4，同列垂直线具有相同网络标签

### P2 Header 15

P2 自上而下依次连接 G3、G1、G16、G17、G2、G5、G25、G26、G35、G36、EN、BAT、+3.3V、+5V、GND；P2 内部第十一项标为 RST，但外部网络为 EN。

- 参数与网络：`nets_top_to_bottom=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND`；`internal_reset_label=RST`；`reset_net=EN`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页左中 P2 Header 15 的内部标签、右侧网络名及逐行连接

### P3 Header 15A

P3 自上而下的 R0、T0、R2、T2、G2、G5、DA、DA、AD、AD、RST、BAT、3V3、5V、G 分别连接 G3、G1、G16、G17、G2、G5、G25、G26、G35、G36、EN、BAT、+3.3V、+5V、GND。

- 参数与网络：`labels_top_to_bottom=R0,T0,R2,T2,G2,G5,DA,DA,AD,AD,RST,BAT,3V3,5V,G`；`nets_top_to_bottom=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND`；`serial_aliases=R0:G3,T0:G1,R2:G16,T2:G17`；`analog_aliases=DA:G25,DA:G26,AD:G35,AD:G36`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页中右 P3 Header 15A 的内部标签、左侧网络名及逐行连接

### P2 与 P3 的网络对应

P2 与 P3 按相同的自上而下顺序连接同一组十五条网络；P3 为其中的串口、数字、模拟、复位和电源信号提供功能别名。

- 参数与网络：`shared_nets=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页中部 P2 与 P3 各十五行的网络标签顺序对照

## 总线

### J1 电源、地与 EN

J1 pins1/3/5 接 GND，pin6 接 EN，pin12 接 +3.3V，pin28 接 +5V，pin30 接 BAT；pins25/27/29 标为 HPWR，但页面外侧没有连接线或网络标签。

- 参数与网络：`ground=1,3,5`；`enable=6:EN`；`three_volt_three=12:+3.3V`；`five_volt=28:+5V`；`battery=30:BAT`；`hpwr_without_external_net=25,27,29`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页右侧 J1 pins1/3/5/6/12/25/27/28/29/30 与外部网络标注

### J1 GPIO 引脚标注

J1 odd pins7/9/11/13/15/17/19/21/23 依次连接 G23/G19/G18/G3/G16/G21/G2/G12/G15；even pins2/4/8/10/14/16/18/20/22/24/26 依次连接 G35/G36/G25/G26/G1/G17/G22/G5/G13/G0/G34。

- 参数与网络：`odd_gpio_pins=7:G23,9:G19,11:G18,13:G3,15:G16,17:G21,19:G2,21:G12,23:G15`；`even_gpio_pins=2:G35,4:G36,8:G25,10:G26,14:G1,16:G17,18:G22,20:G5,22:G13,24:G0,26:G34`
- 证据：图 9327655fc1c8 / 第 1 页 / 第 1 页右侧 J1 两侧红色 Gxx 网络与对应 pin 编号

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base Bottom v1.1 电路结构 | `stack_bus=J1 M5Stack_BUS`；`eight_pin_headers=P1,P4`；`fifteen_pin_headers=P2,P3`；`battery_switch=S1 SW-SPDT`；`battery_connector=J2 Header 2`；`active_components_shown=false`；`passive_components_shown=false` |
| 总线 | J1 电源、地与 EN | `ground=1,3,5`；`enable=6:EN`；`three_volt_three=12:+3.3V`；`five_volt=28:+5V`；`battery=30:BAT`；`hpwr_without_external_net=25,27,29` |
| 总线 | J1 GPIO 引脚标注 | `odd_gpio_pins=7:G23,9:G19,11:G18,13:G3,15:G16,17:G21,19:G2,21:G12,23:G15`；`even_gpio_pins=2:G35,4:G36,8:G25,10:G26,14:G1,16:G17,18:G22,20:G5,22:G13,24:G0,26:G34` |
| 接口 | P1 Header 8 | `order_left_to_right=+5V,+3.3V,GND,G21,G22,G23,G19,G18` |
| 接口 | P4 Header 8A | `pin_labels_left_to_right=5V,3V3,G,SDA,SCL,MOSI,MISO,SCK`；`nets_left_to_right=+5V,+3.3V,GND,G21,G22,G23,G19,G18`；`sda_gpio=21`；`scl_gpio=22`；`mosi_gpio=23`；`miso_gpio=19`；`sck_gpio=18` |
| 接口 | P1 与 P4 的网络对应 | `shared_nets=+5V,+3.3V,GND,G21,G22,G23,G19,G18`；`functional_aliases=G21:SDA,G22:SCL,G23:MOSI,G19:MISO,G18:SCK` |
| 接口 | P2 Header 15 | `nets_top_to_bottom=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND`；`internal_reset_label=RST`；`reset_net=EN` |
| 接口 | P3 Header 15A | `labels_top_to_bottom=R0,T0,R2,T2,G2,G5,DA,DA,AD,AD,RST,BAT,3V3,5V,G`；`nets_top_to_bottom=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND`；`serial_aliases=R0:G3,T0:G1,R2:G16,T2:G17`；`analog_aliases=DA:G25,DA:G26,AD:G35,AD:G36` |
| 接口 | P2 与 P3 的网络对应 | `shared_nets=G3,G1,G16,G17,G2,G5,G25,G26,G35,G36,EN,BAT,+3.3V,+5V,GND` |
| 电源 | S1 与 J2 电池连接 | `switch=S1 SW-SPDT`；`common=pin2 BAT`；`switched_output=pin1 -> J2 pin1`；`open_throw=pin3 NC`；`battery_ground=J2 pin2 GND` |
| 电源 | 电池辅助电路 | `charger_shown=false`；`protection_ic_shown=false`；`fuse_shown=false`；`fuel_gauge_shown=false`；`voltage_sense_shown=false` |
| 电源 | 内置电池规格 | `source_document_capacity_mah=110`；`source_document_chemistry=lithium`；`schematic_capacity_mah=null`；`schematic_chemistry=null`；`schematic_nominal_voltage=null` |
| 接口 | 源文档 NC 表与 J1 标签差异 | `source_document_nc_pins=21,22,23,24,25,26,27,29`；`schematic_labeled_pins=21:G12,22:G13,23:G15,24:G0,26:G34`；`schematic_blank_hpwr_pins=25,27,29`；`other_consumers_of_labeled_nets=false`；`nc_meaning=null` |

## 待确认事项

- `power.battery_specification`：源文档称产品内置 110mAh 锂电池，但原理图只把 J2 画为 Header 2，未标注电芯化学体系、容量、额定电压或保护方式。（证据：图 9327655fc1c8 / 第 1 页 / 第 1 页下方 J2 仅标 Header 2，周围无容量、化学体系或电压文字）
- `interface.nc_mapping_difference`：源文档把 M5-Bus pins21-27 和 pin29 标为 NC，但图纸在 J1 pins21/22/23/24/26 分别标出 G12/G13/G15/G0/G34，且这些 Gxx 标签未连接到 P1-P4 或其他电路；仅据本页不能确定文档中的 NC 是指未布线、未引出还是未被底座功能占用。（证据：图 9327655fc1c8 / 第 1 页 / 第 1 页 J1 pins21-29 与 P1-P4 全部网络标签对照）
- `review.battery_specification`：Base Bottom v1.1 当前装配电池的电芯型号、额定电压、110mAh 容量和保护方案是什么？；原因：原理图只显示 J2 两针接口与 S1 开关，110mAh 和锂电属性只来自产品正文。
- `review.nc_mapping`：源文档 pins21-27/29 的 NC 应解释为 PCB 未布线、没有扩展排针引出，还是底座电路未占用？；原因：图纸仍在 J1 pins21/22/23/24/26 标出 G12/G13/G15/G0/G34，但这些网络未连接到 P1-P4；需要 PCB 网表或版图确认实际铜连线。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9327655fc1c8c37c8931903cf2018af5e6c2cd8d36fb5eb41e462c3d8085719f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/530/Sch_BOTTOM_v1.1_sch_01.png` |

---

源文档：`zh_CN/base/BLACK-BOTTOM_V1.1.md`

源文档 SHA-256：`6ac02adc70e242e2725ab8cdac5f2365e1245dba66fa74929f751607a8b0d12f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
