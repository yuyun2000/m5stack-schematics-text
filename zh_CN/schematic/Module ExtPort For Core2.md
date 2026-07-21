# Module ExtPort For Core2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module ExtPort For Core2 |
| SKU | M123 |
| 产品 ID | `module-extport-for-core2-0e97ef7bee82` |
| 源文档 | `zh_CN/module/extport_for_core2.md` |

## 概述

Module ExtPort For Core2 是无源 M5-Bus 转 Grove 扩展板，CN6 将 Core2 GPIO、电源和地直接引出到 CN1-CN5 与 J1。CN1 PortA、CN2 PortB、CN3 PortC 使用固定 GPIO；CN4 PortD 与 CN5 PortE 的两根信号线分别通过 SW1-SW4 三位拨码开关在三组 GPIO 之间选择。所有 Grove 端口使用 +5V 与 GND，J1 额外导出 +5V、3V3、G36、G26、GND；页面未显示缓冲、限流、ESD 或电平转换。

## 检索关键词

`Module ExtPort For Core2`、`M123`、`MBUS_Bottom`、`CN6`、`PortA`、`PortB`、`PortC`、`PortD`、`PortE`、`Grove`、`EXT_G33`、`EXT_G32`、`EXT_G36`、`EXT_G26`、`EXT_G13`、`EXT_G14`、`EXT_G34`、`EXT_G35`、`EXT_G22`、`EXT_G21`、`EXT_G3`、`EXT_G1`、`EXT_G27`、`EXT_G19`、`EXT_G2`、`EXT_G0`、`EXT_G25`、`SW1`、`SW2`、`SW3`、`SW4`、`+5V`、`3V3`、`J1 Conn_01x05`、`Core2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| CN6 | MBUS_Bottom | Core2 M5-Bus 30 针底部接口，提供 GPIO、5V、3V3 与 GND | 图 45433f0fe27e / 第 1 页 / 中央，CN6 MBUS_Bottom pins1-30 |
| CN1 | CON_GROVE | 固定映射 EXT_G33/EXT_G32 的 PortA Grove 接口 | 图 45433f0fe27e / 第 1 页 / 左上，CN1 PortA，EXT_G33/EXT_G32/+5V/GND |
| CN2 | CON_GROVE | 固定映射 EXT_G36/EXT_G26 的 PortB Grove 接口 | 图 45433f0fe27e / 第 1 页 / 左上，CN2 PortB，EXT_G36/EXT_G26/+5V/GND |
| CN3 | CON_GROVE | 固定映射 EXT_G13/EXT_G14 的 PortC Grove 接口 | 图 45433f0fe27e / 第 1 页 / 左中，CN3 PortC，EXT_G13/EXT_G14/+5V/GND |
| CN4 | CON_GROVE | 由 SW1/SW2 选择 PD1/PD2 GPIO 的 PortD Grove 接口 | 图 45433f0fe27e / 第 1 页 / 左中，CN4 PortD，PD1/PD2/+5V/GND |
| CN5 | CON_GROVE | 由 SW3/SW4 选择 PE1/PE2 GPIO 的 PortE Grove 接口 | 图 45433f0fe27e / 第 1 页 / 左下，CN5 PortE，PE1/PE2/+5V/GND |
| SW1/SW2 | SW_DIP_x03 | PortD 两根信号线的三选一 GPIO 路由 | 图 45433f0fe27e / 第 1 页 / 中左，SW1 PD1->G34/G22/G3，SW2 PD2->G35/G21/G1 |
| SW3/SW4 | SW_DIP_x03 | PortE 两根信号线的三选一 GPIO 路由 | 图 45433f0fe27e / 第 1 页 / 中下，SW3 PE1->G27/G2/G0，SW4 PE2->G19/G25/G2 |
| J1 | Conn_01x05 | 导出 +5V、3V3、EXT_G36、EXT_G26 与 GND 的 5 针排针 | 图 45433f0fe27e / 第 1 页 / 右上，J1 Conn_01x05 pins1-5 |

## 系统结构

### 无源端口扩展架构

CN6 M5-Bus 的 GPIO 与电源直接连接到五个 Grove 接口和一个 5 针排针；PortD/PortE 使用四组拨码开关选择 GPIO，页面没有 MCU、存储、时钟、电源转换或主动缓冲器件。

- 参数与网络：`bus=CN6 MBUS_Bottom`；`grove_connectors=CN1-CN5`；`configurable_ports=CN4 PortD; CN5 PortE`；`switches=SW1-SW4`；`header=J1`；`active_ic=none shown`
- 证据：图 45433f0fe27e / 第 1 页 / 整页 CN1-CN6、SW1-SW4、J1

## 电源

### 电源直通

CN6 pin28 5V 直接供给所有 Grove pin3 和 J1 pin1；CN6 pin12 3V3 直接供给 J1 pin2；CN6 pins1/3/5 GND 连接所有 Grove pin4 与 J1 pin5。

- 参数与网络：`5v_source=CN6 pin28`；`5v_loads=CN1-CN5 pin3; J1 pin1`；`3v3_source=CN6 pin12`；`3v3_load=J1 pin2`；`ground=CN6 pins1/3/5 -> CN1-CN5 pin4 and J1 pin5`；`converter=none shown`
- 证据：图 45433f0fe27e / 第 1 页 / CN6 +5V/3V3/GND 与 CN1-CN5/J1

## 接口

### PortA Grove

CN1 pin1 SCL/RX 接 EXT_G33，pin2 SDA/TX 接 EXT_G32，pin3 接 +5V，pin4 接 GND。

- 参数与网络：`reference=CN1`；`pin1=EXT_G33 SCL/RX`；`pin2=EXT_G32 SDA/TX`；`pin3=+5V`；`pin4=GND`
- 证据：图 45433f0fe27e / 第 1 页 / CN1 PortA pins1-4

### PortB Grove

CN2 pin1 SCL/RX 接 EXT_G36，pin2 SDA/TX 接 EXT_G26，pin3 接 +5V，pin4 接 GND。

- 参数与网络：`reference=CN2`；`pin1=EXT_G36 SCL/RX`；`pin2=EXT_G26 SDA/TX`；`pin3=+5V`；`pin4=GND`
- 证据：图 45433f0fe27e / 第 1 页 / CN2 PortB pins1-4

### PortC Grove

CN3 pin1 SCL/RX 接 EXT_G13，pin2 SDA/TX 接 EXT_G14，pin3 接 +5V，pin4 接 GND。

- 参数与网络：`reference=CN3`；`pin1=EXT_G13 SCL/RX`；`pin2=EXT_G14 SDA/TX`；`pin3=+5V`；`pin4=GND`
- 证据：图 45433f0fe27e / 第 1 页 / CN3 PortC pins1-4

### CN6 M5-Bus GPIO 映射

CN6 将 G1 pin14、G3 pin13、G14 pin16、G13 pin15、G22 pin18、G21 pin17、G0 pin24、G32 pin19、G33 pin20、G27 pin21、G19 pin22、G2 pin23、G25 pin8、G26 pin10、G34 pin26、G35 pin2、G36 pin4 引为 EXT_Gx。

- 参数与网络：`pin14=EXT_G1`；`pin13=EXT_G3`；`pin16=EXT_G14`；`pin15=EXT_G13`；`pin18=EXT_G22`；`pin17=EXT_G21`；`pin24=EXT_G0`；`pin19=EXT_G32`；`pin20=EXT_G33`；`pin21=EXT_G27`；`pin22=EXT_G19`；`pin23=EXT_G2`；`pin8=EXT_G25`；`pin10=EXT_G26`；`pin26=EXT_G34`；`pin2=EXT_G35`；`pin4=EXT_G36`
- 证据：图 45433f0fe27e / 第 1 页 / CN6 MBUS_Bottom pins2-26 GPIO labels

### J1 5 针排针

J1 pin1 为 +5V、pin2 为 3V3、pin3 为 EXT_G36、pin4 为 EXT_G26、pin5 为 GND，与 PortB 的两根信号及两路电源并行引出。

- 参数与网络：`reference=J1`；`pin1=+5V`；`pin2=3V3`；`pin3=EXT_G36`；`pin4=EXT_G26`；`pin5=GND`
- 证据：图 45433f0fe27e / 第 1 页 / 右上 J1 Conn_01x05

## 总线

### 可选内部总线功能

拨码可将 PortD 切到 G22/G21 内部 I2C SCL/SDA 或 G3/G1 RXD0/TXD0；PortE 可切到 G0/G2 的 NS4168 LRCK/DATA 或 G25 自由 GPIO。

- 参数与网络：`i2c=PortD G22 SCL / G21 SDA`；`uart0=PortD G3 RXD0 / G1 TXD0`；`audio=PortE G0 NS4168-LRCK / G2 NS4168-DATA`；`free_gpio=PortE G25`
- 证据：图 45433f0fe27e / 第 1 页 / CN6 signal labels与下方 Assignable GPIOs 注释

## GPIO 与控制信号

### PortD GPIO 选择

CN4 pin1 PD1 通过 SW1 可接 EXT_G34、EXT_G22 或 EXT_G3；pin2 PD2 通过 SW2 可接 EXT_G35、EXT_G21 或 EXT_G1；pin3/4 为 +5V/GND。

- 参数与网络：`port=CN4 PortD`；`white_pin1_PD1=SW1 -> G34/G22/G3`；`yellow_pin2_PD2=SW2 -> G35/G21/G1`；`power=+5V`；`ground=GND`；`default=G34/G35 per schematic note`
- 证据：图 45433f0fe27e / 第 1 页 / CN4 PD1/PD2 与 SW1/SW2

### PortE GPIO 选择

CN5 pin1 PE1 通过 SW3 可接 EXT_G27、EXT_G2 或 EXT_G0；pin2 PE2 通过 SW4 可接 EXT_G19、EXT_G25 或 EXT_G2；pin3/4 为 +5V/GND。

- 参数与网络：`port=CN5 PortE`；`white_pin1_PE1=SW3 -> G27/G2/G0`；`yellow_pin2_PE2=SW4 -> G19/G25/G2`；`power=+5V`；`ground=GND`；`default=G27/G19 per schematic note`
- 证据：图 45433f0fe27e / 第 1 页 / CN5 PE1/PE2 与 SW3/SW4

## 保护电路

### 端口保护边界

原理图从 CN6 到 Grove/J1 仅画直接连线与机械开关，未显示串联限流、电平转换、ESD、保险丝或负载开关。

- 参数与网络：`series_resistors=none shown`；`level_shifter=none shown`；`esd=none shown`；`fuse=none shown`；`load_switch=none shown`
- 证据：图 45433f0fe27e / 第 1 页 / 整页仅连接器与 SW_DIP_x03

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 无源端口扩展架构 | `bus=CN6 MBUS_Bottom`；`grove_connectors=CN1-CN5`；`configurable_ports=CN4 PortD; CN5 PortE`；`switches=SW1-SW4`；`header=J1`；`active_ic=none shown` |
| 接口 | PortA Grove | `reference=CN1`；`pin1=EXT_G33 SCL/RX`；`pin2=EXT_G32 SDA/TX`；`pin3=+5V`；`pin4=GND` |
| 接口 | PortB Grove | `reference=CN2`；`pin1=EXT_G36 SCL/RX`；`pin2=EXT_G26 SDA/TX`；`pin3=+5V`；`pin4=GND` |
| 接口 | PortC Grove | `reference=CN3`；`pin1=EXT_G13 SCL/RX`；`pin2=EXT_G14 SDA/TX`；`pin3=+5V`；`pin4=GND` |
| GPIO 与控制信号 | PortD GPIO 选择 | `port=CN4 PortD`；`white_pin1_PD1=SW1 -> G34/G22/G3`；`yellow_pin2_PD2=SW2 -> G35/G21/G1`；`power=+5V`；`ground=GND`；`default=G34/G35 per schematic note` |
| GPIO 与控制信号 | PortE GPIO 选择 | `port=CN5 PortE`；`white_pin1_PE1=SW3 -> G27/G2/G0`；`yellow_pin2_PE2=SW4 -> G19/G25/G2`；`power=+5V`；`ground=GND`；`default=G27/G19 per schematic note` |
| 总线 | 可选内部总线功能 | `i2c=PortD G22 SCL / G21 SDA`；`uart0=PortD G3 RXD0 / G1 TXD0`；`audio=PortE G0 NS4168-LRCK / G2 NS4168-DATA`；`free_gpio=PortE G25` |
| 接口 | CN6 M5-Bus GPIO 映射 | `pin14=EXT_G1`；`pin13=EXT_G3`；`pin16=EXT_G14`；`pin15=EXT_G13`；`pin18=EXT_G22`；`pin17=EXT_G21`；`pin24=EXT_G0`；`pin19=EXT_G32`；`pin20=EXT_G33`；`pin21=EXT_G27`；`pin22=EXT_G19`；`pin23=EXT_G2`；`pin8=EXT_G25`；`pin10=EXT_G26`；`pin26=EXT_G34`；`pin2=EXT_G35`；`pin4=EXT_G36` |
| 电源 | 电源直通 | `5v_source=CN6 pin28`；`5v_loads=CN1-CN5 pin3; J1 pin1`；`3v3_source=CN6 pin12`；`3v3_load=J1 pin2`；`ground=CN6 pins1/3/5 -> CN1-CN5 pin4 and J1 pin5`；`converter=none shown` |
| 接口 | J1 5 针排针 | `reference=J1`；`pin1=+5V`；`pin2=3V3`；`pin3=EXT_G36`；`pin4=EXT_G26`；`pin5=GND` |
| 保护电路 | 端口保护边界 | `series_resistors=none shown`；`level_shifter=none shown`；`esd=none shown`；`fuse=none shown`；`load_switch=none shown` |
| 核心器件 | Grove 端口数量差异 | `document_ports=PortB/PortC/PortD/PortE = 4`；`schematic_ports=CN1 PortA plus CN2-CN5 PortB-E = 5`；`porta_population=not confirmed` |
| 保护电路 | 多档同时闭合风险 | `switches=SW1-SW4`；`topology=multiple throws directly join GPIOs`；`claimed_rule=one ON position per switch`；`damage_threshold=not printed` |

## 待确认事项

- `component.port-count`：产品正文称提供 PortB/C/D/E 共 4 路 Grove，但原理图还明确画出 CN1 PortA，因此量产板上 PortA 的装配和对外可访问状态需要确认。（证据：图 45433f0fe27e / 第 1 页 / 左侧 CN1 PortA 与 CN2-CN5 PortB-E）
- `protection.switch-warning`：产品正文警告每组拨码只能一位 ON，否则可能损坏设备；原理图显示多位同时闭合会把多个 EXT_GPIO 直接短接到同一 PD/PE 网络，但未标电流限制或损坏阈值。（证据：图 45433f0fe27e / 第 1 页 / SW1-SW4 三路触点直接连接多个 EXT_Gx）
- `review.port-count`：请用 M123 BOM、装配图或实物确认 CN1 PortA 是否实际装配并可由用户使用。；原因：产品正文列 4 个 Grove，原理图列 5 个。
- `review.switch-warning`：请用 Core2 GPIO 绝对额定值和硬件测试规范确认多档同时 ON 的损坏边界与操作限制。；原因：原理图能确认 GPIO 会被直连，但没有电气损坏阈值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5fae073308391c2f6a7820e8424d2a5b12032b4d60c87248505be7195f4580be` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/typec2grove/@akita.webp` |
| 2 | 1 | `45433f0fe27ed059b72a2a26ef3a33d78f2aa8bc137216e93678d65a0d4905c4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/550/module_ext_port_for_core2_sch_sch_01.png` |

---

源文档：`zh_CN/module/extport_for_core2.md`

源文档 SHA-256：`2212d40aa560c77d93a76d72fd3d8ecafddd84a27a8592bda3fb696da51143e7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
