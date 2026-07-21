# Hat Joystick 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Joystick |
| SKU | U073 |
| 产品 ID | `hat-joystick-35079aeb568e` |
| 源文档 | `zh_CN/hat/hat-joystick.md` |

## 概述

Hat Joystick 的本地原理图资源是一张功能框图：StickC 侧的 sda/scl 连接 STM32 F030，控制器的 PA5、PA6、PA7 分别连接 X 轴、Button 和 Y 轴功能块。该页没有器件位号、封装、电源、连接器、上拉、时钟、复位、调试或保护电路细节。产品正文所述 STM32F030F4P6、I2C 地址 0x38 以及 G0/G26/3.3V/GND 映射无法由该框图独立确认，均列入待确认事项。

## 检索关键词

`Hat Joystick`、`U073`、`STM32 F030`、`STM32F030F4P6`、`StickC`、`sda`、`scl`、`I2C`、`0x38`、`PA5`、`PA6`、`PA7`、`X`、`Y`、`Button`、`X轴`、`Y轴`、`中心按键`、`G0`、`G26`、`3.3V`、`GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| STM32 | STM32 F030 | 框图中央控制器，连接 StickC 的 sda/scl，并连接 X、Button、Y 三个输入功能块 | 图 d4bf7f87313d / 第 1 页 / 页面中央黑色控制器方框：文字 STM32 F030，左接 sda/scl，右接 PA5/PA6/PA7 |
| StickC | 未标注 | 主机侧功能块，向 STM32 F030 提供 sda 与 scl 两条信号连接 | 图 d4bf7f87313d / 第 1 页 / 页面左侧橙色 StickC 方框：右边标注 sda 和 scl，并连向中央 STM32 F030 |
| X | 未标注 | 摇杆 X 轴功能块，连接 STM32 F030 的 PA5 | 图 d4bf7f87313d / 第 1 页 / 页面右上 X 双向箭头功能框：左侧 PA5 连线来自 STM32 F030 |
| Button | 未标注 | 摇杆中心按键功能块，连接 STM32 F030 的 PA6 | 图 d4bf7f87313d / 第 1 页 / 页面右中 Button 圆点功能框：左侧 PA6 连线来自 STM32 F030 |
| Y | 未标注 | 摇杆 Y 轴功能块，连接 STM32 F030 的 PA7 | 图 d4bf7f87313d / 第 1 页 / 页面右下 Y 双向箭头功能框：左侧 PA7 连线来自 STM32 F030 |

## 系统结构

### Hat Joystick

功能框图以 STM32 F030 为中央控制器，左侧通过 sda/scl 连接 StickC，右侧通过 PA5、PA6、PA7 分别连接 X、Button、Y。

- 参数与网络：`controller=STM32 F030`；`host_block=StickC`；`host_signals=sda, scl`；`input_blocks=X, Button, Y`；`gpio_mapping=PA5=X; PA6=Button; PA7=Y`
- 证据：图 d4bf7f87313d / 第 1 页 / 全页功能框图：左侧 StickC、中央 STM32 F030、右侧 X/Button/Y 及全部标注连线

## 总线

### StickC 与 STM32 F030

StickC 功能块与 STM32 F030 之间显示两条信号，分别标注 sda 和 scl。

- 参数与网络：`data_signal=sda`；`clock_signal=scl`；`stickc_pin_numbers=not shown`；`controller_pin_names=not shown`；`pullups=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 页面左中 StickC 与中央 STM32 F030 之间两条水平线，文字分别为 sda、scl

## GPIO 与控制信号

### X 轴

STM32 F030 的 PA5 在框图中连接 X 轴功能块。

- 参数与网络：`controller_gpio=PA5`；`function=X`；`signal_type=not shown`；`direction=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 页面中央至右上：STM32 F030 右侧顶端连线标注 PA5，并终止于 X 双向箭头框

### 中心按键

STM32 F030 的 PA6 在框图中连接 Button 功能块。

- 参数与网络：`controller_gpio=PA6`；`function=Button`；`active_level=not shown`；`pull_resistor=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 页面中央至右中：STM32 F030 右侧中间连线标注 PA6，并终止于 Button 圆点框

### Y 轴

STM32 F030 的 PA7 在框图中连接 Y 轴功能块。

- 参数与网络：`controller_gpio=PA7`；`function=Y`；`signal_type=not shown`；`direction=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 页面中央至右下：STM32 F030 右侧底端连线标注 PA7，并终止于 Y 双向箭头框

## 传感器

### 摇杆输入功能

框图显示两个方向轴 X、Y 和一个 Button 输入功能，分别由 PA5、PA7 和 PA6 连接。

- 参数与网络：`x_axis=PA5`；`y_axis=PA7`；`button=PA6`；`axis_circuit=not shown`；`button_circuit=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 页面右侧三组功能框：X 双向箭头、Button 圆点、Y 双向箭头及对应 PA5/PA6/PA7

## 其他事实

### 本地原理图资源详细程度

该本地页面是系统功能框图，不包含器件位号、被动器件、连接器针脚、电源网络、时钟、复位、BOOT、SWD、保护或存储电路。

- 参数与网络：`asset_type=functional block diagram`；`reference_designators=not shown`；`passives=not shown`；`connector_pinout=not shown`；`clock_reset_debug=not shown`；`protection=not shown`；`storage=not shown`
- 证据：图 d4bf7f87313d / 第 1 页 / 全页仅由 StickC、STM32 F030、X/Button/Y 功能块和六个信号标签构成

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Joystick | `controller=STM32 F030`；`host_block=StickC`；`host_signals=sda, scl`；`input_blocks=X, Button, Y`；`gpio_mapping=PA5=X; PA6=Button; PA7=Y` |
| 总线 | StickC 与 STM32 F030 | `data_signal=sda`；`clock_signal=scl`；`stickc_pin_numbers=not shown`；`controller_pin_names=not shown`；`pullups=not shown` |
| GPIO 与控制信号 | X 轴 | `controller_gpio=PA5`；`function=X`；`signal_type=not shown`；`direction=not shown` |
| GPIO 与控制信号 | 中心按键 | `controller_gpio=PA6`；`function=Button`；`active_level=not shown`；`pull_resistor=not shown` |
| GPIO 与控制信号 | Y 轴 | `controller_gpio=PA7`；`function=Y`；`signal_type=not shown`；`direction=not shown` |
| 传感器 | 摇杆输入功能 | `x_axis=PA5`；`y_axis=PA7`；`button=PA6`；`axis_circuit=not shown`；`button_circuit=not shown` |
| 核心器件 | STM32 控制器型号 | `documented_model=STM32F030F4P6`；`schematic_label=STM32 F030`；`reference_designator=not shown`；`package=not shown` |
| 总线地址 | Hat Joystick I2C 地址 | `documented_address=0x38`；`schematic_address_label=not shown`；`address_straps=not shown`；`firmware_evidence=not shown` |
| 接口 | StickC 主机接口映射 | `documented_sda=G0`；`documented_scl=G26`；`connector_reference=not shown`；`pin_numbers=not shown` |
| 电源 | Hat Joystick 供电 | `documented_supply=3.3V`；`documented_ground=GND`；`schematic_power_net=not shown`；`regulator=not shown`；`decoupling=not shown` |
| 其他事实 | 本地原理图资源详细程度 | `asset_type=functional block diagram`；`reference_designators=not shown`；`passives=not shown`；`connector_pinout=not shown`；`clock_reset_debug=not shown`；`protection=not shown`；`storage=not shown` |

## 待确认事项

- `component.controller-exact-model`：产品正文给出 STM32F030F4P6，但本地框图仅标注 STM32 F030，未显示 F4P6 后缀、器件位号或封装，无法由该页确认完整型号。（证据：图 d4bf7f87313d / 第 1 页 / 页面中央控制器方框仅显示 STM32 F030，无完整订货型号或位号）
- `address.i2c-0x38`：产品正文标注 I2C 地址为 0x38，但本地框图只显示 sda/scl，未标注地址、地址选择网络或固件信息，无法由该页确认 0x38。（证据：图 d4bf7f87313d / 第 1 页 / 全页 StickC-sda/scl-STM32 F030 框图，未见 0x38 或地址配置标注）
- `interface.stickc-pin-mapping`：产品正文将 SDA/SCL 映射到 G0/G26，但框图仅显示 sda/scl 信号名，没有连接器位号、针脚编号或 G0/G26 标签，无法由该页确认针脚映射。（证据：图 d4bf7f87313d / 第 1 页 / 页面左侧 StickC 方框仅标注 sda/scl，无 G0、G26、连接器位号或针脚编号）
- `power.stickc-supply-mapping`：产品正文管脚映射包含 3.3V 与 GND，但本地框图未画出任何电源线、电源引脚、去耦、稳压器或电池路径，无法由该页确认供电连接。（证据：图 d4bf7f87313d / 第 1 页 / 全页功能框图只显示 sda/scl 与 PA5/PA6/PA7，无电源或地网络）
- `review.controller-exact-model`：Hat Joystick 所装 MCU 的完整订货型号是否为 STM32F030F4P6？；原因：产品正文给出完整型号，但本地框图只标注 STM32 F030，缺少后缀、封装和位号。
- `review.i2c-address-0x38`：I2C 从设备地址 0x38 是否由 STM32 固件固定实现？；原因：框图只有 sda/scl 连接，没有地址标注、硬件地址选择或固件版本依据。
- `review.stickc-pin-mapping`：SDA/SCL 在实际 HAT 连接器上的针脚与 G0/G26 映射是什么？；原因：产品正文给出 G0/G26，但本地框图没有连接器位号、针脚编号或 GPIO 标签。
- `review.power-mapping`：实际 HAT 连接器如何向控制器和摇杆电路分配 3.3V 与 GND？；原因：本地资源没有任何电源或地网络，无法核对正文中的 3.3V/GND 映射及去耦路径。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d4bf7f87313d8b8d2f6bbac8ecbfaf41d4774d3253f86e5c557c3a8854a0f207` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-joystick.md`

源文档 SHA-256：`dc8475261c1c9b14325c1b9997d2eb0fe06c84569052bc917238599dc509ea81`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
