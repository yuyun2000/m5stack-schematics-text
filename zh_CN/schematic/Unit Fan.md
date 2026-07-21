# Unit Fan 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Fan |
| SKU | U063 |
| 产品 ID | `unit-fan-2ed411433320` |
| 源文档 | `zh_CN/unit/unit_fan.md` |

## 概述

Unit Fan 是一条由 Grove 控制的低侧直流电机驱动电路：J1 的 MOSI 网络经 R1 1KΩ驱动 Q1 AO3400A，Q1 控制接在 VCC 与漏极节点之间的 B1 Motor。R2 51KΩ将栅极下拉到 GND，D1 1N4148WS T4 与 C2 100nF 跨接电机两端，分别构成续流与高频抑制路径。J1 同时引入 VCC/GND，C1 100nF 为接口电源去耦；J1 MISO 未连接，原理图没有 MCU、电源转换器或通信协议器件。

## 检索关键词

`Unit Fan`、`U063`、`AO3400A`、`1N4148WS T4`、`B1 Motor`、`GROVE_IO`、`HY2.0-4P`、`MOSI`、`MISO`、`VCC`、`GND`、`Q1`、`R1 1KΩ`、`R2 51KΩ`、`C1 100nF`、`C2 100nF`、`D1`、`low-side drive`、`GPIO control`、`PWM`、`N20`、`8800 RPM`、`DIN`、`motor flyback`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 四针 Grove 接口，pin2 MOSI 为电机控制输入，pin3/pin4 提供 VCC/GND，pin1 MISO 未连接 | 图 b008603cddfd / 第 1 页 / 第 1 页右侧，J1 GROVE_IO pin1 MISO、pin2 MOSI、pin3 VCC、pin4 GND |
| B1 | Motor | 直流电机负载，一端接 VCC，另一端接 Q1 漏极开关节点 | 图 b008603cddfd / 第 1 页 / 第 1 页左上，B1 Motor 位于 VCC 与 Q1 漏极节点之间 |
| Q1 | AO3400A | 由 MOSI 控制的 N 沟道低侧电机开关，源极接 GND | 图 b008603cddfd / 第 1 页 / 第 1 页左下，Q1 AO3400A 的漏极接 B1、源极接 GND、栅极接 R1/R2 |
| D1 | 1N4148WS T4 | 跨接 B1 电机两端的续流/反电动势钳位二极管 | 图 b008603cddfd / 第 1 页 / 第 1 页左上，D1 1N4148WS T4 跨接 VCC 与 Q1 漏极/电机下端 |
| R1,R2 | 1KΩ / 51KΩ | R1 为 MOSI 至 Q1 栅极串联电阻，R2 将栅极下拉至 GND | 图 b008603cddfd / 第 1 页 / 第 1 页中央，MOSI-R1 1KΩ-Q1 gate 与 R2 51KΩ-GND |
| C1 | 100nF | J1 VCC 至 GND 的接口电源去耦电容 | 图 b008603cddfd / 第 1 页 / 第 1 页右侧，J1 VCC 旁 C1 100nF 至 GND |
| C2 | 100nF | 跨接 B1 电机两端的抑制电容 | 图 b008603cddfd / 第 1 页 / 第 1 页左侧，C2 100nF 跨接 VCC 与 B1/Q1 开关节点 |

## 系统结构

### Unit Fan 系统架构

J1 引入 VCC/GND 和 MOSI 控制，MOSI 经 R1/R2 驱动 Q1 AO3400A；Q1 作为低侧开关控制 B1 Motor，D1/C2 跨接电机，C1 为 VCC 去耦。

- 参数与网络：`connector=J1 GROVE_IO`；`control=MOSI`；`switch=Q1 AO3400A`；`load=B1 Motor`；`flyback=D1 1N4148WS T4`；`suppression=C2 100nF`；`decoupling=C1 100nF`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页完整原理图

### 主控、存储与通信器件

唯一原理图页面未画 MCU、协处理器、存储器、晶振、复位、调试、传感器、射频、音频、电源转换器或 I2C/UART/CAN/RS-485/USB 总线器件；MOSI/MISO 是 J1 针脚网络名，其中仅 MOSI 接入驱动电路。

- 参数与网络：`controller=null`；`coprocessor=null`；`storage=null`；`clock=null`；`reset=null`；`debug=null`；`sensor=null`；`rf=null`；`audio=null`；`converter=null`；`connected_signal=MOSI`；`unconnected_signal=MISO`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页完整原理图，唯一页面

## 电源

### VCC 至电机的供电路径

J1 pin3 将 VCC 引入板上，VCC 直接连接 B1 Motor 上端；B1 下端连接 Q1 漏极，Q1 源极接 GND，构成 VCC-B1-Q1-GND 串联功率路径。

- 参数与网络：`input=J1 pin3 VCC`；`path=VCC -> B1 Motor -> Q1 drain/source -> GND`；`switch=Q1 AO3400A`；`return=J1 pin4 GND`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 VCC/GND 同名网络与 B1/Q1 功率路径

## 接口

### J1 Grove 接口针脚

J1 GROVE_IO pin1=MISO、pin2=MOSI、pin3=VCC、pin4=GND；pin2 MOSI 为进入 Unit Fan 的控制输入，pin3 VCC 为电机和电路电源输入，pin4 为回流地，pin1 MISO 在图中悬空。

- 参数与网络：`connector=J1 GROVE_IO`；`pin1=MISO no connection`；`pin2=MOSI control input`；`pin3=VCC power input`；`pin4=GND`；`direction=MOSI/VCC input`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页右侧 J1 pin1-pin4

## GPIO 与控制信号

### MOSI 至 Q1 电机控制

J1 pin2 MOSI 经 R1 1KΩ串联后连接 Q1 栅极，R2 51KΩ从栅极节点接 GND；MOSI 为高电平时驱动 Q1 导通，未驱动时 R2 将栅极保持为低电平。

- 参数与网络：`input=J1 pin2 MOSI`；`series_resistor=R1 1KΩ`；`gate_pulldown=R2 51KΩ`；`mosfet=Q1 AO3400A`；`active_level=high`；`default=off via R2`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页中央，J1 MOSI、R1、R2 与 Q1 gate

## 保护电路

### 电机续流二极管

D1 1N4148WS T4 跨接在 VCC 与 B1/Q1 开关节点之间，与 B1 Motor 并联，构成电机断开时的反电动势续流/钳位路径。

- 参数与网络：`device=D1 1N4148WS T4`；`connections=VCC to B1 lower/Q1 drain`；`protected_load=B1 Motor`；`role=flyback clamp`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页左上，D1 与 B1 并联

### 电机与接口电源去耦

C2 100nF 与 B1 Motor 并联，C1 100nF 从 J1 VCC 接至 GND；原理图未画 VCC 输入保险丝、反接保护、ESD、过流检测或温度保护器件。

- 参数与网络：`motor_cap=C2 100nF across B1`；`supply_cap=C1 100nF VCC-GND`；`fuse=null`；`reverse_protection=null`；`esd=null`；`current_sense=null`；`thermal_protection=null`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页 C1/C2 及完整电源路径，唯一页面

## 关键网络

### B1/Q1 开关节点

B1 Motor 下端、Q1 漏极、D1 一端和 C2 一端连接到同一开关节点；该节点由 Q1 拉向 GND。

- 参数与网络：`members=B1 lower,Q1 drain,D1,C2`；`control=Q1 low-side switching`；`high_side=B1 upper VCC`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页左侧 B1/Q1/D1/C2 共节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Fan 系统架构 | `connector=J1 GROVE_IO`；`control=MOSI`；`switch=Q1 AO3400A`；`load=B1 Motor`；`flyback=D1 1N4148WS T4`；`suppression=C2 100nF`；`decoupling=C1 100nF` |
| 系统结构 | 主控、存储与通信器件 | `controller=null`；`coprocessor=null`；`storage=null`；`clock=null`；`reset=null`；`debug=null`；`sensor=null`；`rf=null`；`audio=null`；`converter=null`；`connected_signal=MOSI`；`unconnected_signal=MISO` |
| 接口 | J1 Grove 接口针脚 | `connector=J1 GROVE_IO`；`pin1=MISO no connection`；`pin2=MOSI control input`；`pin3=VCC power input`；`pin4=GND`；`direction=MOSI/VCC input` |
| 电源 | VCC 至电机的供电路径 | `input=J1 pin3 VCC`；`path=VCC -> B1 Motor -> Q1 drain/source -> GND`；`switch=Q1 AO3400A`；`return=J1 pin4 GND` |
| GPIO 与控制信号 | MOSI 至 Q1 电机控制 | `input=J1 pin2 MOSI`；`series_resistor=R1 1KΩ`；`gate_pulldown=R2 51KΩ`；`mosfet=Q1 AO3400A`；`active_level=high`；`default=off via R2` |
| 关键网络 | B1/Q1 开关节点 | `members=B1 lower,Q1 drain,D1,C2`；`control=Q1 low-side switching`；`high_side=B1 upper VCC` |
| 保护电路 | 电机续流二极管 | `device=D1 1N4148WS T4`；`connections=VCC to B1 lower/Q1 drain`；`protected_load=B1 Motor`；`role=flyback clamp` |
| 保护电路 | 电机与接口电源去耦 | `motor_cap=C2 100nF across B1`；`supply_cap=C1 100nF VCC-GND`；`fuse=null`；`reverse_protection=null`；`esd=null`；`current_sense=null`；`thermal_protection=null` |
| 电源 | Grove VCC 电压 | `documented_voltage=5V`；`schematic_network=VCC`；`voltage_range=null`；`max_current=null`；`power=null` |
| 核心器件 | 电机型号与机械性能 | `reference=B1`；`schematic_part=Motor`；`documented_type=N20 DC motor`；`documented_no_load_speed=8800 RPM`；`documented_direction=single direction`；`rated_voltage=null`；`rated_current=null`；`stall_current=null` |
| GPIO 与控制信号 | PWM 调速能力 | `documented_control=GPIO/PWM`；`input=J1 MOSI`；`driver=Q1 AO3400A`；`pwm_frequency=null`；`duty_range=null`；`speed_curve=null`；`thermal_limit=null` |
| 接口 | 正文 DIN 与原理图 MOSI 命名 | `documented_signal=DIN on Grove yellow`；`documented_nc=NC on Grove white`；`schematic_control=J1 pin2 MOSI`；`schematic_unconnected=J1 pin1 MISO`；`connector_orientation=null` |

## 待确认事项

- `power.documented-vcc`：产品正文管脚表将 J1 电源标为 5V；原理图只使用 VCC 网络名，没有在 J1 或 B1 旁标注具体电压、允许范围、最大电流或功耗。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 pin3 与 B1 上端仅标 VCC）
- `component.documented-motor`：产品正文称电机为 N20、单向旋转、空载转速 8800 RPM；原理图只将 B1 标为 Motor，没有具体型号、额定电压、电流、转速、转向、堵转参数或轴规格。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 B1 仅标 Motor）
- `gpio.documented-pwm`：产品正文称 MOSI/DIN 支持 GPIO 电平或 PWM 调速；原理图确认 MOSI 经 R1 驱动 Q1 栅极，但未标 PWM 频率、占空比范围、最小脉宽、转速曲线或热限制。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 MOSI-R1-Q1 gate 电路，无 PWM 参数）
- `interface.documented-din`：产品正文将 Grove 黄色线信号称为 DIN、白色线称为 NC；原理图中对应 J1 pin2 标为 MOSI、pin1 标为 MISO 且悬空。两套命名的针脚对应关系需要结合连接器方向或实物确认。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 GROVE_IO pin1 MISO/pin2 MOSI）
- `review.vcc-rating`：请依据当前产品规格或实测确认 J1 VCC 的额定 5V、允许范围、最大输入电流和功耗。；原因：原理图只标 VCC，未提供电气额定值。
- `review.motor-spec`：请用量产 BOM、电机标签或测试报告确认 B1 的 N20 型号、8800 RPM、转向、额定/堵转电流和轴规格。；原因：原理图仅标 B1 Motor。
- `review.pwm-limits`：请通过固件示例和硬件测试确认 MOSI/DIN 的 PWM 频率、占空比范围、调速曲线及连续工作热边界。；原因：电路只显示 MOSFET 栅极驱动，没有 PWM 性能参数。
- `review.grove-signal-name`：请结合实物连接器方向确认正文 DIN/NC 与原理图 J1 MOSI/MISO 的物理针脚对应。；原因：正文采用线色/PORT.B 命名，原理图采用 J1 pin1-pin4 与 MISO/MOSI 命名。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b008603cddfd4c1b55a4a2b8159c2e476e85a252484dfee1f800f1a72e389981` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_sch_01.webp` |

---

源文档：`zh_CN/unit/unit_fan.md`

源文档 SHA-256：`1c46c6bf64140309187c148664175da8f166f8dfa466a1d739b2837adf812b23`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
