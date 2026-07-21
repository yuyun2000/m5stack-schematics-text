# Unit Key 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Key |
| SKU | U144 |
| 产品 ID | `unit-key-643866be96b3` |
| 源文档 | `zh_CN/unit/key.md` |

## 概述

Unit Key 由 S1 常开按键和 U2 SK6812-3535 RGB LED 构成，两路信号分别以 KEY_OUT、RGB 从 J1 Grove 接口引出。KEY_OUT 由 R1 10 kΩ 上拉至 3V3，按下 S1 时接地，形成低有效数字输入。U1 HT7533 将 J1 的 5V 转为 3V3，供按键上拉和 SK6812-3535 使用。

## 检索关键词

`Unit Key`、`U144`、`SK6812-3535`、`SK6812`、`HT7533`、`SW-PB`、`S1`、`KEY_OUT`、`RGB`、`IO2`、`IO1`、`GROVE 4P`、`active low`、`10K pull-up`、`R1 10K`、`5V`、`3V3`、`DI`、`DO`、`VDD`、`C1 1uF/50V`、`C2 1uF/50V`、`push button`、`blue switch`、`256 brightness levels`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| S1 | SW-PB | KEY_OUT 低有效瞬时按键 | 图 c7d6fe491218 / 第 1 页 / 页 1 网格 B2，S1 标注 SW-PB，连接 KEY_OUT 与 GND |
| U2 | SK6812-3535 | 单线可编程 RGB LED | 图 c7d6fe491218 / 第 1 页 / 页 1 网格 C2，U2 器件框下方标注 SK6812-3535，针脚为 DO、GND、DI、VDD |
| U1 | HT7533 | 5V 至 3V3 线性稳压器 | 图 c7d6fe491218 / 第 1 页 / 页 1 网格 C1，U1 标注 HT7533，VIN/VOUT 分别连接 5V/3V3 |
| J1 | GROVE 4P | 按键、RGB 控制与 5V 电源接口 | 图 c7d6fe491218 / 第 1 页 / 页 1 网格 B1，J1 GROVE 4P，端子标注 IO2、IO1、5V、GND |

## 系统结构

### Unit Key 功能结构

J1 提供 KEY_OUT 按键输出与 RGB LED 控制输入；S1 构成按键，U2 SK6812-3535 构成 RGB LED，U1 生成 3V3 电源。

- 参数与网络：`connector=J1`；`button=S1 SW-PB`；`button_net=KEY_OUT`；`rgb_led=U2 SK6812-3535`；`rgb_net=RGB`；`regulator=U1 HT7533`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 完整电路，J1、S1、U1、U2 与 KEY_OUT/RGB/电源网络

## 核心器件

### U2 SK6812-3535

U2 的 DI 引脚 3 连接 RGB，VDD 引脚 4 连接 3V3，GND 引脚 2 接地；DO 引脚 1 在本页未连接。

- 参数与网络：`reference=U2`；`part_number=SK6812-3535`；`data_input=DI/pin 3/RGB`；`data_output=DO/pin 1 unconnected`；`supply=VDD/pin 4/3V3`；`ground=GND/pin 2`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 网格 C2，U2 DO/GND/DI/VDD 引脚号和 RGB/3V3/GND 网络

## 电源

### U1 HT7533

U1 HT7533 的 VIN 引脚 3 接 5V，VOUT 引脚 2 输出 3V3，GND 引脚 1 接地。

- 参数与网络：`reference=U1`；`part_number=HT7533`；`input=VIN/pin 3/5V`；`output=VOUT/pin 2/3V3`；`ground=GND/pin 1`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 网格 C1，U1 HT7533 引脚号与 5V/3V3/GND 网络

### 5V 与 3V3 电容

C1 1 uF/50V 连接在 5V 与 GND 之间；C2 1 uF/50V 连接在 U2 附近的 3V3 与 GND 之间。

- 参数与网络：`input_capacitor=C1 1uF/50V across 5V-GND`；`rgb_supply_capacitor=C2 1uF/50V across 3V3-GND`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 网格 C1-C3，U1 输入侧 C1 与 U2 供电侧 C2

### Unit Key 电平与供电域

J1 输入电源网络为 5V；U1 输出的 3V3 同时供 R1 按键上拉和 U2 VDD。

- 参数与网络：`connector_supply=5V`；`internal_rail=3V3`；`3v3_consumers=R1 pull-up,U2 VDD`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 J1 5V、U1 5V-to-3V3、R1 与 U2 VDD 网络

## 接口

### J1 Grove 接口

J1 的 IO2、IO1、5V、GND 四个端子分别连接 KEY_OUT、RGB、5V、GND。

- 参数与网络：`reference=J1`；`pinout=IO2:KEY_OUT,IO1:RGB,5V:5V,GND:GND`；`KEY_OUT_direction=output from unit`；`RGB_direction=input to unit`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 网格 B1，J1 四个端子与右侧 KEY_OUT、RGB、5V、GND 网络

## 总线

### RGB 单线数据

J1 IO1 的 RGB 网络直接连接 U2 DI 引脚 3，图中未显示串联数据电阻、电平转换器或级联输出接口。

- 参数与网络：`source=J1 IO1`；`network=RGB`；`destination=U2 DI/pin 3`；`series_resistor=null`；`level_shifter=null`；`cascade_output=null`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 J1 RGB 网络与 U2 DI 引脚 3，路径中无其他器件

## GPIO 与控制信号

### KEY_OUT 按键网络

R1 10 kΩ 将 KEY_OUT 上拉至 3V3，S1 按键闭合时将 KEY_OUT 接至 GND。

- 参数与网络：`network=KEY_OUT`；`pullup=R1 10k to 3V3`；`switch=S1 SW-PB to GND`；`active_level=low`；`released_level_rail=3V3`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 网格 B2，3V3、R1 10K、KEY_OUT、S1 与 GND 连线

## 保护电路

### 接口与负载保护

本页未显示 TVS/ESD、保险丝、反接保护、负载开关或过流保护器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`overcurrent_protection_visible=false`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 全图仅含 J1、S1、R1、U1、U2、C1、C2 及直接连线

## 关键网络

### KEY_OUT 逻辑状态

S1 释放时 KEY_OUT 由 R1 拉向 3V3；S1 按下时 KEY_OUT 被短接到 GND，因此主机应按低有效信号读取。

- 参数与网络：`released_state=high via R1 to 3V3`；`pressed_state=low via S1 to GND`；`host_signal=J1 IO2/KEY_OUT`
- 证据：图 c7d6fe491218 / 第 1 页 / 页 1 KEY_OUT 上拉与 S1 对地按键电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Key 功能结构 | `connector=J1`；`button=S1 SW-PB`；`button_net=KEY_OUT`；`rgb_led=U2 SK6812-3535`；`rgb_net=RGB`；`regulator=U1 HT7533` |
| 接口 | J1 Grove 接口 | `reference=J1`；`pinout=IO2:KEY_OUT,IO1:RGB,5V:5V,GND:GND`；`KEY_OUT_direction=output from unit`；`RGB_direction=input to unit` |
| GPIO 与控制信号 | KEY_OUT 按键网络 | `network=KEY_OUT`；`pullup=R1 10k to 3V3`；`switch=S1 SW-PB to GND`；`active_level=low`；`released_level_rail=3V3` |
| 关键网络 | KEY_OUT 逻辑状态 | `released_state=high via R1 to 3V3`；`pressed_state=low via S1 to GND`；`host_signal=J1 IO2/KEY_OUT` |
| 核心器件 | U2 SK6812-3535 | `reference=U2`；`part_number=SK6812-3535`；`data_input=DI/pin 3/RGB`；`data_output=DO/pin 1 unconnected`；`supply=VDD/pin 4/3V3`；`ground=GND/pin 2` |
| 总线 | RGB 单线数据 | `source=J1 IO1`；`network=RGB`；`destination=U2 DI/pin 3`；`series_resistor=null`；`level_shifter=null`；`cascade_output=null` |
| 电源 | U1 HT7533 | `reference=U1`；`part_number=HT7533`；`input=VIN/pin 3/5V`；`output=VOUT/pin 2/3V3`；`ground=GND/pin 1` |
| 电源 | 5V 与 3V3 电容 | `input_capacitor=C1 1uF/50V across 5V-GND`；`rgb_supply_capacitor=C2 1uF/50V across 3V3-GND` |
| 电源 | Unit Key 电平与供电域 | `connector_supply=5V`；`internal_rail=3V3`；`3v3_consumers=R1 pull-up,U2 VDD` |
| 保护电路 | 接口与负载保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`overcurrent_protection_visible=false` |
| 其他事实 | 按键机械轴体 | `documented_switch_type=blue mechanical switch`；`documented_replaceable_keycap=true`；`schematic_switch_label=SW-PB`；`schematic_mechanical_part=null` |
| 其他事实 | RGB 亮度与电流参数 | `documented_brightness_levels=256`；`documented_standby_current_ma=2`；`documented_operating_current_ma=13`；`documented_supply_v=5`；`schematic_ratings=null` |

## 待确认事项

- `other.switch_mechanics`：产品正文称 S1 使用青轴并支持更换键帽，但原理图仅标注 SW-PB，未提供机械轴体型号或键帽结构。（证据：图 c7d6fe491218 / 第 1 页 / 页 1 S1 仅标注 SW-PB，没有青轴或机械料号）
- `other.led_brightness_current`：产品正文描述 256 级亮度、5V@2mA 待机和 5V@13mA 工作电流；这些参数未在本页原理图中标注。（证据：图 c7d6fe491218 / 第 1 页 / 页 1 U2 SK6812-3535 与电源电路未标注亮度级数或电流值）
- `review.switch_mechanics`：S1 的实际青轴型号、触点额定值和可替换键帽规格是什么？；原因：原理图只给出通用 SW-PB 电气符号，没有机械料号。
- `review.led_brightness_current`：256 级亮度和 2mA/13mA 电流参数适用于哪些 RGB 值、刷新率与测量条件？；原因：原理图没有 SK6812 运行参数或电流测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c7d6fe491218b1f4bee366c075b0f0d7c0c526aded42dfc59aafe8d996ac5052` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/599/SCH_unitKey_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/key.md`

源文档 SHA-256：`dfd6b7871365c9cffe414e616e64ba1ea3910218031d4166deae9b23315b4816`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
