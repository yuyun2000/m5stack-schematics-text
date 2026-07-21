# Unit Button 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Button |
| SKU | U027 |
| 产品 ID | `unit-button-15587bbf1a6f` |
| 源文档 | `zh_CN/unit/button.md` |

## 概述

Unit Button 是由按键 S1、R1/R2 分压网络、C1 滤波电容和 Grove 连接器 J1 组成的无源数字输入单元。S1 按下时将 J1 pin 1 信号节点直接连接 GND；释放时 R1=10KΩ 与 R2=20KΩ 将节点偏置到理论空载值 2/3×VCC。J1 pin 2 不连接、pin 3 输入 VCC、pin 4 接 GND；原理图没有标注 VCC 的额定电压。

## 检索关键词

`Unit Button`、`U027`、`SW-BUTTON`、`S1`、`R1 10KΩ`、`R2 20KΩ`、`C1 100nF`、`Grove`、`J1`、`Digital Output`、`active low`、`pin 1 I`、`pin 2 NC`、`pin 3 VCC`、`pin 4 GND`、`VCC`、`GND`、`2/3 VCC`、`voltage divider`、`debounce filter`、`PORT.B`、`V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| S1 | SW-BUTTON | 按下时把数字输出节点短接到 GND 的常开按键 | 图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：S1 SW-BUTTON，左端接 GND、右端接 J1 pin 1 信号节点 |
| R1 | 10KΩ | VCC 到按键信号节点的上侧偏置电阻 | 图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：R1 10KΩ 竖直接在 VCC 与 J1 pin 1 节点之间 |
| R2 | 20KΩ | 按键信号节点到 GND 的下侧偏置电阻 | 图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：R2 20KΩ 竖直接在 J1 pin 1 节点与 GND 之间 |
| C1 | 100nF | 按键信号节点到 GND 的滤波电容 | 图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：C1 100nF 从 S1/R1/R2/J1 pin 1 共节点接至 GND |
| J1 | Grove 4P | 引出按键数字输出、VCC 和 GND，pin 2 未接 | 图 fef08e7908c5 / 第 1 页 / 页 1 网格 B3：J1 Grove，pin 1 接信号，pin 2 悬空，pin 3 VCC，pin 4 GND |

## 系统结构

### Unit Button

S1、R1、R2 和 C1 共用 J1 pin 1 信号节点：R1 从 VCC 上拉该节点，R2 与 C1 接 GND，S1 按下时也将节点接 GND。

- 参数与网络：`active_ic=null`；`button=S1 SW-BUTTON`；`signal_pin=J1 pin 1`；`upper_resistor=R1 10KΩ`；`lower_resistor=R2 20KΩ`；`capacitor=C1 100nF`；`return=GND`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2-B3：S1/R1/R2/C1/J1 的完整直接连线

## 核心器件

### S1 SW-BUTTON

S1 符号为未按下时断开的瞬时按键，一端接 GND，另一端接 J1 pin 1 与 R1/R2/C1 共节点。

- 参数与网络：`reference=S1`；`part_number=SW-BUTTON`；`contact_state_drawn=open`；`terminal_1=GND`；`terminal_2=J1 pin 1 signal node`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：S1 的开路触点符号和两端网络

## 电源

### J1 VCC/GND

J1 pin 3 输入 VCC，并通过同名网络连接 R1 上端；J1 pin 4 接 GND，与 S1、R2 和 C1 的地端共地。

- 参数与网络：`power_pin=J1 pin 3 VCC`；`ground_pin=J1 pin 4 GND`；`vcc_load=R1 10KΩ`；`ground_loads=S1,R2,C1`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2-B3：J1 pin 3/VCC 与 R1，同页各 GND 符号及 J1 pin 4

## 接口

### J1 Grove 4P

J1 pin 1 为按键数字输出，连接器内标 I；pin 2 标 O 但未接内部电路；pin 3 接 VCC；pin 4 接 GND。

- 参数与网络：`pin_1=digital output; I`；`pin_2=no internal connection; O`；`pin_3=VCC`；`pin_4=GND`；`output_direction=Unit to host`；`power_direction=host to Unit`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B3：J1 pins 1~4、I/O/VCC/GND 字符及外部连线

### J1 pin 2

J1 pin 2 左侧没有连接线，未接入 S1/R1/R2/C1 电路；连接器内部该位置标为 O。

- 参数与网络：`connector_pin=J1 pin 2`；`label=O`；`internal_connection=null`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B3：J1 pin 2 数字、O 字符与无外部连线的端点

## GPIO 与控制信号

### J1 pin 1 按键输出

S1 按下时闭合 J1 pin 1 信号节点到 GND 的路径，因此按下状态在原理图拓扑上为低电平。

- 参数与网络：`signal_pin=J1 pin 1`；`button=S1`；`pressed_connection=GND`；`pressed_logic=low`；`polarity=active low`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：S1 右端接输出节点、左端接 GND

## 保护电路

### 按键接口保护

本页没有绘出 TVS、ESD 阵列、反接保护、保险丝或专用输入钳位器件；可见器件仅为 S1、R1、R2、C1 和 J1。

- 参数与网络：`tvs=null`；`esd_array=null`；`reverse_polarity_device=null`；`fuse=null`；`visible_components=S1,R1,R2,C1,J1`
- 证据：图 fef08e7908c5 / 第 1 页 / 整页：唯一电路区域包含 S1/R1/R2/C1/J1，无其他保护位号

## 关键网络

### 按键信号关键连接

关键网络为 J1 pin 3 VCC→R1→J1 pin 1，J1 pin 1→R2/C1/S1→GND，J1 pin 4→GND；J1 pin 2 不连接。

- 参数与网络：`upper_path=J1.3 VCC-R1-J1.1`；`ground_paths=J1.1-R2/C1/S1-GND`；`ground_pin=J1.4`；`unused_pin=J1.2`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2-B3：所有同节点连线和 J1 pinout

## 模拟电路

### 释放状态偏置

S1 释放时，R1 10KΩ 与 R2 20KΩ 在 VCC 和 GND 之间构成分压，J1 pin 1 位于两电阻中点；忽略外部负载时节点电压为 20K/(10K+20K)×VCC，即 2/3×VCC。

- 参数与网络：`upper_resistor=R1 10KΩ`；`lower_resistor=R2 20KΩ`；`output_node=J1 pin 1`；`unloaded_ratio=20K/(10K+20K)=2/3`；`unloaded_voltage=2/3 * VCC`；`button_state=released`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：VCC-R1 10KΩ-输出节点-R2 20KΩ-GND 分压路径

### C1 输出滤波

C1 100nF 从 J1 pin 1 输出节点接至 GND，与 R1/R2 偏置网络并联在按键输出上。

- 参数与网络：`capacitor=C1 100nF`；`signal=J1 pin 1`；`return=GND`；`associated_resistors=R1 10KΩ,R2 20KΩ`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2：C1 100nF 上端接按键信号节点、下端接 GND

## 其他事实

### UNIT_BUTTON 原理图版本

图框标注 Project Title 为 UNIT_BUTTON.PrjPCB、Sheet Title 为 UNIT_BUTTON.SchDoc、Revised 为 V1.0、日期为 07/18/2018，Sheet 1 of 1。

- 参数与网络：`project_title=UNIT_BUTTON.PrjPCB`；`sheet_title=UNIT_BUTTON.SchDoc`；`revision=V1.0`；`date=07/18/2018`；`sheet=1 of 1`
- 证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 D3-D4：右下角图框 Project Title/Sheet Title/Revised/Date/Sheet

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Button | `active_ic=null`；`button=S1 SW-BUTTON`；`signal_pin=J1 pin 1`；`upper_resistor=R1 10KΩ`；`lower_resistor=R2 20KΩ`；`capacitor=C1 100nF`；`return=GND` |
| 接口 | J1 Grove 4P | `pin_1=digital output; I`；`pin_2=no internal connection; O`；`pin_3=VCC`；`pin_4=GND`；`output_direction=Unit to host`；`power_direction=host to Unit` |
| GPIO 与控制信号 | J1 pin 1 按键输出 | `signal_pin=J1 pin 1`；`button=S1`；`pressed_connection=GND`；`pressed_logic=low`；`polarity=active low` |
| 核心器件 | S1 SW-BUTTON | `reference=S1`；`part_number=SW-BUTTON`；`contact_state_drawn=open`；`terminal_1=GND`；`terminal_2=J1 pin 1 signal node` |
| 模拟电路 | 释放状态偏置 | `upper_resistor=R1 10KΩ`；`lower_resistor=R2 20KΩ`；`output_node=J1 pin 1`；`unloaded_ratio=20K/(10K+20K)=2/3`；`unloaded_voltage=2/3 * VCC`；`button_state=released` |
| 模拟电路 | C1 输出滤波 | `capacitor=C1 100nF`；`signal=J1 pin 1`；`return=GND`；`associated_resistors=R1 10KΩ,R2 20KΩ` |
| 电源 | J1 VCC/GND | `power_pin=J1 pin 3 VCC`；`ground_pin=J1 pin 4 GND`；`vcc_load=R1 10KΩ`；`ground_loads=S1,R2,C1` |
| 电源 | J1 pin 3 VCC 额定值 | `connector_pin=J1 pin 3`；`net=VCC`；`schematic_voltage=null`；`released_output_ratio=2/3 VCC`；`absolute_output_voltage=null` |
| 接口 | J1 pin 2 | `connector_pin=J1 pin 2`；`label=O`；`internal_connection=null` |
| 保护电路 | 按键接口保护 | `tvs=null`；`esd_array=null`；`reverse_polarity_device=null`；`fuse=null`；`visible_components=S1,R1,R2,C1,J1` |
| 关键网络 | 按键信号关键连接 | `upper_path=J1.3 VCC-R1-J1.1`；`ground_paths=J1.1-R2/C1/S1-GND`；`ground_pin=J1.4`；`unused_pin=J1.2` |
| 其他事实 | UNIT_BUTTON 原理图版本 | `project_title=UNIT_BUTTON.PrjPCB`；`sheet_title=UNIT_BUTTON.SchDoc`；`revision=V1.0`；`date=07/18/2018`；`sheet=1 of 1` |

## 待确认事项

- `power.vcc-rating-not-shown`：原理图将 J1 pin 3 和 R1 上端标为 VCC，但未给出该电源的数值，因此无法仅凭原理图确认额定供电电压和释放态的绝对输出电压。（证据：图 fef08e7908c5 / 第 1 页 / 页 1 网格 B2-B3：R1 与 J1 pin 3 的 VCC 标签，整页未见电压数值）
- `review.vcc-rating`：J1 pin 3 的 VCC 额定输入电压是多少，释放状态 J1 pin 1 的标称高电平是多少？；原因：原理图只给出 R1/R2 的 2/3 分压比例，没有打印 VCC 数值；绝对输出电平取决于外部供电。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fef08e7908c51192d85f36fc2093aa9c7c0e11bc7b35b900281072814a8ac694` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/804/U027_UNIT_BUTTON_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/button.md`

源文档 SHA-256：`4fef84e5c8294eee1aefcfad4d5289ea6eb625433f8168926d752b31d54bcc9c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
