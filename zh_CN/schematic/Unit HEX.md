# Unit HEX 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit HEX |
| SKU | A045 |
| 产品 ID | `unit-hex-3391bac05f15` |
| 源文档 | `zh_CN/unit/hex.md` |

## 概述

Unit HEX 的本地资源为 HEX PIN Layout 连接布局图，显示 IN、OUT、PWR 三组接口以及首颗和末颗 LED 的数据方向。IN 的 DATA 进入 1st LED，Last LED 的数据输出到 OUT 的 DATA，从而支持数据级联。图中仅标注 VCC、GND、DATA，没有 LED 型号、数量、供电电压、保护或去耦电路。

## 检索关键词

`Unit HEX`、`A045`、`HEX PIN Layout`、`IN`、`OUT`、`PWR`、`DATA`、`VCC`、`GND`、`1st LED`、`Last LED`、`LED Signal`、`RGB LED`、`SK6812`、`SK6812 x 37`、`37 LEDs`、`5V`、`PORT.B`、`daisy-chain`、`cascade input`、`cascade output`、`single-wire LED data`、`16.7 million colors`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| IN | 未标注 | 四位电源与 LED 数据输入接口 | 图 3a1f41bc6f54 / 第 1 页 / 页 1 左侧标注 IN 的四位连接器，前三位文字为 GND、VCC、DATA |
| OUT | 未标注 | 四位 LED 数据级联输出与电源接口 | 图 3a1f41bc6f54 / 第 1 页 / 页 1 右侧标注 OUT 的四位连接器，后三位文字为 DATA、VCC、GND |
| PWR | 未标注 | 独立电源连接器 | 图 3a1f41bc6f54 / 第 1 页 / 页 1 下中部标注 PWR 的三位连接器，可见 GND、VCC 标签 |
| 1st LED ... Last LED | 未标注 | 板载串行 RGB LED 数据链 | 图 3a1f41bc6f54 / 第 1 页 / 页 1 六边形轮廓顶部与左下分别标注 1st LED、Last LED，并以红线表示数据链端点 |

## 系统结构

### Unit HEX LED 级联结构

连接布局图显示 IN、OUT、PWR 三组接口和从 1st LED 到 Last LED 的板载 LED 数据链。

- 参数与网络：`input_connector=IN`；`output_connector=OUT`；`power_connector=PWR`；`chain_start=1st LED`；`chain_end=Last LED`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 完整 HEX PIN Layout，IN/OUT/PWR 与首末 LED 标签

## 电源

### 接口电源网络

IN、OUT 均标注 VCC 和 GND；PWR 也标注 VCC 和 GND。布局图未给出 VCC 的数值、电源分配电路或电流额定值。

- 参数与网络：`connectors_with_vcc_gnd=IN,OUT,PWR`；`rail_name=VCC`；`voltage=null`；`current_rating=null`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 IN、OUT、PWR 三处 VCC/GND 标签

## 接口

### IN 输入接口

IN 为四位连接器；按图中从上到下的位置，前三位依次标注 GND、VCC、DATA，第四位未标注网络名。

- 参数与网络：`reference=IN`；`position_order_top_to_bottom=1:GND,2:VCC,3:DATA,4:unlabeled`；`data_direction=input to 1st LED`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 左侧 IN 四个触点及其右侧 GND、VCC、DATA 标签

### OUT 级联接口

OUT 为四位连接器；按图中从上到下的位置，第一位未标注网络名，后续三位依次标注 DATA、VCC、GND。

- 参数与网络：`reference=OUT`；`position_order_top_to_bottom=1:unlabeled,2:DATA,3:VCC,4:GND`；`data_direction=output from Last LED`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 右侧 OUT 四个触点及其右侧 DATA、VCC、GND 标签

### PWR 电源接口

PWR 为三位连接器，图中前两位分别标注 GND、VCC，第三位未标注网络名。

- 参数与网络：`reference=PWR`；`position_order_left_to_right=1:GND,2:VCC,3:unlabeled`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 下中部 PWR 三个触点及下方 GND、VCC 标签

## 总线

### 串行 LED DATA 路径

红色路径显示 IN 的 DATA 进入 1st LED；另一段红色路径从 Last LED 到 OUT 的 DATA，因此 OUT 可继续驱动下一级灯板。

- 参数与网络：`input_path=IN DATA -> 1st LED`；`output_path=Last LED -> OUT DATA`；`topology=serial daisy-chain`；`protocol=null`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 两条红色数据路径，分别连接 IN DATA 与 1st LED、Last LED 与 OUT DATA

## 其他事实

### 本地资源覆盖范围

本地页面标题为 HEX PIN Layout，未显示 IC/LED 位号、阻容、保护器件、去耦器件、时钟、复位或调试接口。

- 参数与网络：`resource_type=pin layout`；`component_designators_visible=false`；`passive_values_visible=false`；`protection_visible=false`；`debug_visible=false`
- 证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 完整 HEX PIN Layout 页面，仅含连接器、VCC/GND/DATA 与首末 LED 示意

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit HEX LED 级联结构 | `input_connector=IN`；`output_connector=OUT`；`power_connector=PWR`；`chain_start=1st LED`；`chain_end=Last LED` |
| 接口 | IN 输入接口 | `reference=IN`；`position_order_top_to_bottom=1:GND,2:VCC,3:DATA,4:unlabeled`；`data_direction=input to 1st LED` |
| 接口 | OUT 级联接口 | `reference=OUT`；`position_order_top_to_bottom=1:unlabeled,2:DATA,3:VCC,4:GND`；`data_direction=output from Last LED` |
| 接口 | PWR 电源接口 | `reference=PWR`；`position_order_left_to_right=1:GND,2:VCC,3:unlabeled` |
| 总线 | 串行 LED DATA 路径 | `input_path=IN DATA -> 1st LED`；`output_path=Last LED -> OUT DATA`；`topology=serial daisy-chain`；`protocol=null` |
| 电源 | 接口电源网络 | `connectors_with_vcc_gnd=IN,OUT,PWR`；`rail_name=VCC`；`voltage=null`；`current_rating=null` |
| 核心器件 | 板载 RGB LED 型号与数量 | `documented_part_number=SK6812`；`documented_quantity=37`；`schematic_part_number=null`；`schematic_quantity=null` |
| 电源 | Unit HEX 供电电压 | `documented_voltage_v=5`；`schematic_rail=VCC`；`schematic_voltage=null` |
| 其他事实 | RGB LED 色彩能力 | `documented_color_count_text=16.7 万色`；`schematic_color_depth=null`；`schematic_pwm_bits=null` |
| 其他事实 | 本地资源覆盖范围 | `resource_type=pin layout`；`component_designators_visible=false`；`passive_values_visible=false`；`protection_visible=false`；`debug_visible=false` |

## 待确认事项

- `component.led_array`：产品正文标注 SK6812 × 37，但连接布局图只显示 1st LED 和 Last LED 端点，没有 LED 型号、总数或逐颗位号。（证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 仅标注 1st LED 与 Last LED，未出现 SK6812、37 或 LED 位号）
- `power.documented_voltage`：产品正文的 Grove 管脚表将电源标为 5V，但布局图只使用 VCC 网络名，无法仅由该图确认电压值。（证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 IN、OUT、PWR 均只标注 VCC，未标注 5V）
- `other.color_capability`：产品正文称支持 16.7 万色，但连接布局图没有颜色深度、PWM 位数或 LED 电气参数。（证据：图 3a1f41bc6f54 / 第 1 页 / 页 1 HEX PIN Layout 仅显示连接关系，没有颜色或 PWM 参数）
- `review.led_array`：当前 A045 硬件版本是否确实装配 37 颗 SK6812，逐颗数据顺序是什么？；原因：布局图只给出首末 LED 和数据方向，没有型号、数量或完整排列。
- `review.supply_voltage`：IN、OUT、PWR 的 VCC 额定电压与允许电流是否均为 5V 电源域？；原因：布局图只标 VCC/GND，没有电压值、电流额定或保护电路。
- `review.color_capability`：正文中的“16.7 万色”对应的实际 RGB/PWM 位深和控制限制是什么？；原因：布局图不包含 LED 数据手册参数或颜色深度信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3a1f41bc6f54d3b8ac3a69f13186cc324fb246f26a9d1c26171c00fd2fbb12dc` | `https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_04.webp` |

---

源文档：`zh_CN/unit/hex.md`

源文档 SHA-256：`128ca49efdaba8c6ae91b77fd740021ccdbbc98fc237a849547650ea5618e60b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
