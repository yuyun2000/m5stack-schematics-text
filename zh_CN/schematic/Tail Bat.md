# Tail Bat 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Tail Bat |
| SKU | T001 |
| 产品 ID | `tail-bat-8596aaaaa9a1` |
| 源文档 | `zh_CN/atom/tailbat.md` |

## 概述

Tail Bat 的现有资源是一页电源功能框图，而不是带位号和引脚号的器件级原理图。框图确认左、右两组 USB 接口的 D+/D- 直接贯通，左侧标为 5V-IN、右侧标为 5V-OUT，并由 IP5303 连接 LED 与标注 190mAh 的电池。两侧均标出 GND，但图中未展开完整地线、电池保护、充放电参数或 USB-C 端口实现。产品正文中的单击开机、双击关机、LED 充电状态以及仅允许 Type-C 充电等行为需要正式原理图、BOM、固件或实测确认。

## 检索关键词

`Tail Bat`、`T001`、`IP5303`、`190mAh`、`battery`、`LED`、`USB`、`USB Type-C`、`D+`、`D-`、`GND`、`5V-IN`、`5V-OUT`、`data pass-through`、`power bank`、`charging`、`boost`、`single click`、`double click`、`Grove`、`rechargeable lithium battery`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| IP5303 block | IP5303 | 连接 5V 输入、5V 输出、电池和 LED 的电源管理功能块 | 图 ee8dac113657 / 第 1 页 / 第 1 页中央左侧 IP5303 黑色功能块及其到 USB、电池、LED 的连线 |
| Battery block (unreferenced) | 190mAh (diagram label) | 连接 IP5303 的板载电池功能块 | 图 ee8dac113657 / 第 1 页 / 第 1 页中央蓝色电池图标，内部明确标注 190mAh |
| LED (unreferenced) | 未标注 | 连接 IP5303 与电池/输出侧节点的状态指示器 | 图 ee8dac113657 / 第 1 页 / 第 1 页中央上方 LED 标签与二极管图标，左接 IP5303、右接电池/输出侧支路 |
| USB input/output (unreferenced) | 未标注 | 左侧 D+/D-/GND/5V-IN 与右侧 D+/D-/GND/5V-OUT 接口 | 图 ee8dac113657 / 第 1 页 / 第 1 页左右两端 USB 色块，分别标 D+/D-、GND、5V-IN 与 D+/D-、GND、5V-OUT |

## 系统结构

### Tail Bat 功能框图架构

左侧 USB 的 D+/D- 直连右侧 USB 的 D+/D-；左侧 5V-IN 进入 IP5303，IP5303 连接 LED 和标注 190mAh 的电池，并连接右侧 5V-OUT。

- 参数与网络：`diagram_type=functional block diagram`；`power_manager=IP5303`；`battery_label=190mAh`；`indicator=LED`；`input=USB 5V-IN`；`output=USB 5V-OUT`；`data_path=USB D+/D- pass-through`
- 证据：图 ee8dac113657 / 第 1 页 / 第 1 页完整框图的左右 USB、IP5303、LED 和 190mAh 电池连接

## 电源

### 5V 输入、电源管理与输出

框图左侧 USB 电源端标为 5V-IN，右侧 USB 电源端标为 5V-OUT，IP5303 位于输入、电池和输出之间。

- 参数与网络：`input_label=5V-IN`；`manager=IP5303`；`output_label=5V-OUT`；`ground_labels=GND on both USB sides`
- 证据：图 ee8dac113657 / 第 1 页 / 第 1 页左侧 5V-IN/IP5303 与右侧 5V-OUT 连接区域

### 电池容量标注

连接 IP5303 的电池图标内部明确标注 190mAh；本页没有给出电芯型号、额定电压、化学体系或连接器信息。

- 参数与网络：`capacity_label=190mAh`；`cell_model_shown=false`；`nominal_voltage_shown=false`；`chemistry_shown=false`；`connector_shown=false`
- 证据：图 ee8dac113657 / 第 1 页 / 第 1 页中央蓝色电池图标及 190mAh 文字

## 接口

### USB D+/D- 数据直通

左侧 USB 的 D+/D- 通过顶部直线直接连接到右侧 USB 的 D+/D-，中间没有画出数据开关、集线器或协议控制器。

- 参数与网络：`left_signal=D+/D-`；`right_signal=D+/D-`；`connection=direct pass-through`；`data_switch_shown=false`；`hub_shown=false`
- 证据：图 ee8dac113657 / 第 1 页 / 第 1 页顶部左 USB D+/D- 到右 USB D+/D- 的连续水平线

### LED 指示连接

框图显示一个标为 LED 的指示器，左侧连接 IP5303，右侧连接电池/输出侧支路；没有画出位号、限流电阻或控制引脚。

- 参数与网络：`label=LED`；`source=IP5303 block`；`reference_designator=null`；`series_resistor_shown=false`；`control_pin_shown=false`
- 证据：图 ee8dac113657 / 第 1 页 / 第 1 页中央上方 LED 标签、二极管图标和两侧连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Tail Bat 功能框图架构 | `diagram_type=functional block diagram`；`power_manager=IP5303`；`battery_label=190mAh`；`indicator=LED`；`input=USB 5V-IN`；`output=USB 5V-OUT`；`data_path=USB D+/D- pass-through` |
| 接口 | USB D+/D- 数据直通 | `left_signal=D+/D-`；`right_signal=D+/D-`；`connection=direct pass-through`；`data_switch_shown=false`；`hub_shown=false` |
| 电源 | 5V 输入、电源管理与输出 | `input_label=5V-IN`；`manager=IP5303`；`output_label=5V-OUT`；`ground_labels=GND on both USB sides` |
| 电源 | 电池容量标注 | `capacity_label=190mAh`；`cell_model_shown=false`；`nominal_voltage_shown=false`；`chemistry_shown=false`；`connector_shown=false` |
| 接口 | LED 指示连接 | `label=LED`；`source=IP5303 block`；`reference_designator=null`；`series_resistor_shown=false`；`control_pin_shown=false` |
| 核心器件 | 正文中的电源按键与点击逻辑 | `documented_single_click=power on`；`documented_double_click=power off`；`button_shown=false`；`button_pin_shown=false`；`timing_shown=false` |
| 接口 | 正文中的 LED 颜色与状态语义 | `documented_color=red`；`documented_power_on=on`；`documented_charging=blinking`；`documented_full=steady on`；`diagram_label=LED`；`status_logic_shown=false` |
| 接口 | 正文中的 Type-C 与 Grove 充电限制 | `documented_charge_input=USB Type-C only`；`documented_grove_charge=false`；`diagram_usb_label=USB`；`type_c_cc_shown=false`；`grove_shown=false`；`full_pass_through_shown=false` |
| 保护电路 | 充放电参数与保护可见性 | `charge_current_shown=false`；`boost_current_shown=false`；`cutoff_voltage_shown=false`；`battery_protection_shown=false`；`temperature_monitor_shown=false`；`usb_esd_shown=false`；`fuse_shown=false` |
| 电源 | 正文中的可充电锂电池 | `documented_type=rechargeable lithium battery`；`diagram_capacity=190mAh`；`cell_bom=null`；`nominal_voltage=null`；`capacity_tolerance=null`；`protection_board=null` |

## 待确认事项

- `component.documented-button-control`：产品正文称正面带电源按键，并使用单击开机、双击关机；当前框图没有按键符号、按键引脚、去抖网络或点击时序，因此这些交互无法由本页确认。（证据：图 ee8dac113657 / 第 1 页 / 第 1 页仅有 USB、IP5303、LED 和电池，未显示按键）
- `interface.documented-led-behavior`：正文称红色 LED 在开机时点亮、充电时闪烁、充满后常亮；框图只标 LED，没有颜色料号、驱动引脚、闪烁逻辑或充满状态网络。（证据：图 ee8dac113657 / 第 1 页 / 第 1 页只有单个 LED 功能符号，没有颜色或状态表）
- `interface.documented-charge-source`：正文称内置电池只能通过 Type-C 充电、不能通过 Grove 充电，并声称其他接口保持直通；当前框图只写 USB、5V-IN/5V-OUT 和 D+/D-，没有 Type-C CC 引脚、Grove 接口或完整直通网络。（证据：图 ee8dac113657 / 第 1 页 / 第 1 页左右仅标 USB D+/D-/GND/5V-IN/5V-OUT，未显示 Type-C CC 或 Grove）
- `power.unshown-electrical-protection`：框图没有标注充电电流、升压能力、截止电压、过充/过放/短路保护、温度检测、USB ESD 或保险器件，因此这些电气边界无法从本页确定。（证据：图 ee8dac113657 / 第 1 页 / 第 1 页抽象框图没有器件级充放电外围和保护网络）
- `power.documented-battery-bom`：正文称内置 190mAh 可充电锂电池；框图确认 190mAh 标注和电池连接，但没有电芯 BOM、化学体系、额定电压、容量公差或保护板信息。（证据：图 ee8dac113657 / 第 1 页 / 第 1 页电池图标仅标 190mAh，无电芯型号与保护信息）
- `review.button-control`：T001 的电源按键连接到 IP5303 哪个引脚，单击开机和双击关机的有效时序及去抖要求是什么？；原因：按键和控制时序只出现在产品正文，功能框图没有对应电路。
- `review.led-status`：T001 当前 LED 的颜色、限流器件、IP5303 驱动引脚及开机/充电/充满状态定义是什么？；原因：框图只有 LED 功能符号，无法确认颜色、驱动网络和状态时序。
- `review.charge-source-and-pass-through`：请用正式原理图确认 T001 的 Type-C CC 配置、Grove 端口直通范围，以及为何 Grove 5V 不允许给电池充电。；原因：当前框图未画 Type-C CC、Grove 或完整接口网络，不能验证正文中的充电来源限制。
- `review.electrical-protection`：T001 的充电电流、5V 输出能力、截止电压、短路/过流/过温保护和 USB ESD 规格是什么？；原因：功能框图没有器件外围、额定值和保护网络，需要正式原理图、IP5303 具体版本及测试数据。
- `review.battery-bom`：T001 当前电芯的完整 BOM 型号、额定电压、190mAh 容量公差、化学体系和保护配置是什么？；原因：框图只给出 190mAh 容量文字，不能证明实际电芯和保护板规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ee8dac1136570f4050429f38881edeb8c397814b2c79367481af814405328596` | `https://static-cdn.m5stack.com/resource/docs/products/atom/tailbat/tailbat_sch_01.webp` |

---

源文档：`zh_CN/atom/tailbat.md`

源文档 SHA-256：`50cdbef7e87abdbc659d06d3e880ff275bf0eea9fbacf510e0b019018444f3d7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
