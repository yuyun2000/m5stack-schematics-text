# Unit Angle 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Angle |
| SKU | U005 |
| 产品 ID | `unit-angle-69efbab3ceb4` |
| 源文档 | `zh_CN/unit/angle.md` |

## 概述

Unit Angle 是由串联电阻 R1、10KΩ 电位器 R2 和 Grove 4 针连接器 J1 构成的无源模拟输入单元，R2 滑臂直接输出到 J1 pin 1。两张原理图都显示 J1 pin 2 不参与电路、pin 4 接 GND；第二张还将 pin 3 标为 5V，并给出基于 R1/R2 的输出公式。两张页面对 R1 的取值存在冲突：第一页为 4.7KΩ，第二页为 10KΩ，因此实际装配阻值和对应最大输出电压需要按硬件版本确认。

## 检索关键词

`Unit Angle`、`U005`、`ANGLE Unit`、`R1 4.7KΩ`、`R1 10KΩ`、`R2 10KΩ`、`potentiometer`、`Rp`、`Uo`、`Analog Output`、`Grove`、`J1`、`pin 1`、`pin 2 NC`、`pin 3 VCC`、`pin 3 5V`、`pin 4 GND`、`2500mV`、`5000mV`、`voltage divider`、`PORT.B`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| R1 | 4.7KΩ（source_001）/ 10KΩ（source_002） | VCC/5V 到 R2 上端的串联电阻；两张原理图标值不一致 | 图 874d0912c82b / 第 1 页 / source_001 页 1 左侧：VCC 下方 R1 标注 4.7KΩ，串接至 R2 上端; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 左侧 ANGLE Unit 框内：VCC-R1，R1 标注 10KΩ |
| R2 | 10KΩ potentiometer | 上端接 R1、下端接 GND、滑臂输出 Uo 的旋转电位器 | 图 874d0912c82b / 第 1 页 / source_001 页 1 左侧：R2 10KΩ 电位器，上端接 R1、下端 GND、滑臂接 J1 pin 1; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 左侧：R2 10KΩ potentiometer，滑臂网络标 Uo |
| J1 | Grove 4P | 引出电位器模拟输出、电源和地；pin 2 未接入内部电路 | 图 874d0912c82b / 第 1 页 / source_001 页 1 右侧：J1 Grove，pins 1/2/3/4 标 I/O/VCC/GND，pin 1 接滑臂、pin 2 线端悬空; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 中部：J1 Grove，pin 1 Uo、pin 3 5V、pin 4 GND，pin 2 无内部连接 |

## 系统结构

### Unit Angle

Unit Angle 的原理图只包含 R1、R2 和 J1：电源经 R1 加到 R2 电位器上端，R2 下端接 GND，滑臂作为模拟输出接 J1 pin 1。

- 参数与网络：`active_ic=null`；`series_resistor=R1`；`potentiometer=R2 10KΩ`；`output=R2 wiper to J1 pin 1`；`ground=R2 low terminal and J1 pin 4`
- 证据：图 874d0912c82b / 第 1 页 / source_001 整页：VCC-R1-R2-GND 与滑臂-J1 pin 1; 图 64d6af1fd1e6 / 第 1 页 / source_002 左半页：ANGLE Unit 框内 R1/R2/J1 完整拓扑

## 电源

### J1 pin 3 到 R1/R2

J1 pin 3 为单元供电输入，连接 R1 上端的电源网络；source_001 将其标为 VCC，source_002 明确标为 5V。

- 参数与网络：`connector_pin=J1 pin 3`；`source_001_rail=VCC`；`source_002_rail=5V`；`load=R1-R2 divider`；`ground_return=J1 pin 4 GND`
- 证据：图 874d0912c82b / 第 1 页 / source_001 页 1：J1 pin 3 VCC 与 R1 上端同名 VCC 网络; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1：J1 pin 3 标 5V，R1 上端标 VCC

## 接口

### J1 Grove 4P

J1 pin 1 为电位器滑臂模拟输出（source_001 标 I，source_002 标 Uo），pin 2 未接内部电路，pin 3 为 VCC/5V 输入，pin 4 为 GND。

- 参数与网络：`pin_1=analog output; I/Uo`；`pin_2=no internal connection; O label in source_001`；`pin_3=VCC in source_001; 5V in source_002`；`pin_4=GND`；`output_direction=Unit to host`；`power_direction=host to Unit`
- 证据：图 874d0912c82b / 第 1 页 / source_001 页 1 右侧 J1 pins 1~4、I/O/VCC/GND 标签与连线; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 中部 J1：pin 1 Uo、pin 3 5V、pin 4 GND，pin 2 无内部连线

### J1 pin 2

两张原理图都没有把 J1 pin 2 连接到 R1/R2 电路；source_001 在连接器内部将该位置标为 O。

- 参数与网络：`connector_pin=J1 pin 2`；`internal_connection=null`；`source_001_label=O`；`source_002_label=null`
- 证据：图 874d0912c82b / 第 1 页 / source_001 页 1：J1 pin 2 左侧短线悬空、内部字符 O; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1：J1 pin 2 横线无任何内部电路连接

## GPIO 与控制信号

### J1 pin 1 模拟输出

R2 的滑臂直接连接 J1 pin 1，不经过缓冲器、ADC、保护器或串联输出电阻；该针脚输出相对于 GND 的连续模拟电压。

- 参数与网络：`connector_pin=J1 pin 1`；`source=R2 wiper`；`net_name=Uo in source_002`；`reference=GND at J1 pin 4`；`buffer=null`；`series_output_component=null`
- 证据：图 874d0912c82b / 第 1 页 / source_001 页 1：R2 滑臂到 J1 pin 1 的直接水平连线; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1：R2 滑臂-J1 pin 1-Uo 直接路径

## 保护电路

### 模拟输出与电源保护

两张原理图均未绘出 TVS、ESD 阵列、保险丝、反接保护或输出限流器件；可见电路仅为 R1、R2 和 J1。

- 参数与网络：`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity_device=null`；`visible_components=R1,R2,J1`
- 证据：图 874d0912c82b / 第 1 页 / source_001 整页：仅 R1/R2/J1 与 VCC/GND; 图 64d6af1fd1e6 / 第 1 页 / source_002 左侧 ANGLE Unit 框：仅 R1/R2/J1

## 关键网络

### Unit Angle 关键连接

关键路径为 J1 pin 3 VCC/5V→R1→R2→GND/J1 pin 4，R2 滑臂→J1 pin 1 Uo；J1 pin 2 不连接。

- 参数与网络：`power_path=J1.3-R1-R2-J1.4/GND`；`signal_path=R2 wiper-J1.1/Uo`；`unused_pin=J1.2`；`reference=GND`
- 证据：图 874d0912c82b / 第 1 页 / source_001 整页直接连线; 图 64d6af1fd1e6 / 第 1 页 / source_002 左半页 ANGLE Unit 电路框

## 模拟电路

### R2 10KΩ 电位器

R2 总阻值标为 10KΩ，上端连接 R1，下端连接 GND，滑臂连接 J1 pin 1；source_002 将滑臂以下电阻记为 Rp。

- 参数与网络：`reference=R2`；`total_resistance=10KΩ`；`upper_terminal=R1 output`；`lower_terminal=GND`；`wiper=J1 pin 1,Uo`；`variable_segment_name=Rp in source_002`
- 证据：图 874d0912c82b / 第 1 页 / source_001 页 1：R2 10KΩ 符号、上下端与滑臂连线; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1：R2 10KΩ potentiometer、Rp 说明与 Uo 输出

### source_002 的 Uo 计算

source_002 印出的计算式为 Uo = 5000mV / (Rp + R1) × Rp，其中 R1=10KΩ、R2 总阻值=10KΩ、Rp 为旋转后滑臂至 GND 的电阻。

- 参数与网络：`asset_scope=source_002`；`formula=Uo = 5000mV / (Rp + R1) * Rp`；`r1=10KΩ`；`r2_total=10KΩ`；`rp_definition=wiper-to-GND segment after rotation`；`supply_in_formula=5000mV`
- 证据：图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 右侧：Total resistance/Rp/Scale 说明及 Output Voltage 公式

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Angle | `active_ic=null`；`series_resistor=R1`；`potentiometer=R2 10KΩ`；`output=R2 wiper to J1 pin 1`；`ground=R2 low terminal and J1 pin 4` |
| 核心器件 | R1 串联电阻 | `reference=R1`；`source_001_value=4.7KΩ`；`source_002_value=10KΩ`；`resolved_value=null`；`impact=output voltage transfer ratio` |
| 模拟电路 | R2 10KΩ 电位器 | `reference=R2`；`total_resistance=10KΩ`；`upper_terminal=R1 output`；`lower_terminal=GND`；`wiper=J1 pin 1,Uo`；`variable_segment_name=Rp in source_002` |
| 接口 | J1 Grove 4P | `pin_1=analog output; I/Uo`；`pin_2=no internal connection; O label in source_001`；`pin_3=VCC in source_001; 5V in source_002`；`pin_4=GND`；`output_direction=Unit to host`；`power_direction=host to Unit` |
| GPIO 与控制信号 | J1 pin 1 模拟输出 | `connector_pin=J1 pin 1`；`source=R2 wiper`；`net_name=Uo in source_002`；`reference=GND at J1 pin 4`；`buffer=null`；`series_output_component=null` |
| 电源 | J1 pin 3 到 R1/R2 | `connector_pin=J1 pin 3`；`source_001_rail=VCC`；`source_002_rail=5V`；`load=R1-R2 divider`；`ground_return=J1 pin 4 GND` |
| 模拟电路 | source_002 的 Uo 计算 | `asset_scope=source_002`；`formula=Uo = 5000mV / (Rp + R1) * Rp`；`r1=10KΩ`；`r2_total=10KΩ`；`rp_definition=wiper-to-GND segment after rotation`；`supply_in_formula=5000mV` |
| 模拟电路 | 最大模拟输出电压 | `source_002_maximum=2500mV`；`source_002_supply=5000mV`；`source_002_r1=10KΩ`；`source_001_r1=4.7KΩ`；`resolved_hardware_maximum=null` |
| 接口 | J1 pin 2 | `connector_pin=J1 pin 2`；`internal_connection=null`；`source_001_label=O`；`source_002_label=null` |
| 保护电路 | 模拟输出与电源保护 | `tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity_device=null`；`visible_components=R1,R2,J1` |
| 关键网络 | Unit Angle 关键连接 | `power_path=J1.3-R1-R2-J1.4/GND`；`signal_path=R2 wiper-J1.1/Uo`；`unused_pin=J1.2`；`reference=GND` |

## 待确认事项

- `component.r1-value-conflict`：source_001 将 R1 标为 4.7KΩ，而 source_002 将 R1 标为 10KΩ；资源中没有版本号或 BOM 信息可判定实际装配值。（证据：图 874d0912c82b / 第 1 页 / source_001 页 1 左上：R1 4.7KΩ; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1 左侧：R1 10KΩ）
- `analog.maximum-output-conflict`：source_002 的 5V、R1=10KΩ、R2=10KΩ 公式与曲线给出约 2500mV 最大输出；source_001 的 R1=4.7KΩ 不符合这一组参数，因此实际硬件最大输出依赖所装 R1 版本。（证据：图 874d0912c82b / 第 1 页 / source_001 页 1 左上：R1=4.7KΩ; 图 64d6af1fd1e6 / 第 1 页 / source_002 页 1：R1=10KΩ、5000mV 公式及曲线 2500mV 虚线）
- `review.r1-assembly-value`：当前 U005 硬件版本的 R1 实际装配值是 4.7KΩ 还是 10KΩ？；原因：两个产品清单内原理图资源对同一位号 R1 给出不同阻值，且页面没有硬件版本号可用于选择。
- `review.maximum-output`：当前硬件在 5V 供电、旋钮满量程时的实际 Uo 最大值是否为 2500mV？；原因：2500mV 曲线基于 source_002 的 R1=10KΩ，而 source_001 将 R1 标为 4.7KΩ；必须先确认硬件版本和装配值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `874d0912c82b1a0ce63d2bb1e3fee96f311a91832b47a07d64fd99cfaaeeeed2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/800/U005_Sche.jpg` |
| 2 | 1 | `64d6af1fd1e63f29c0b823ff634b2e935e65e5064f07ce9cc9aadb0a96cf72c6` | `https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_sch_02.webp` |

---

源文档：`zh_CN/unit/angle.md`

源文档 SHA-256：`99da27a95ec4cc8a4c344f79f534ddcd72f78fdc5fa6acdfd40cc3a407d94747`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
