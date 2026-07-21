# Unit TypeC to Grove 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit TypeC to Grove |
| SKU | U151 |
| 产品 ID | `unit-typec-to-grove-7849605a2401` |
| 源文档 | `zh_CN/unit/typec2grove.md` |

## 概述

Unit TypeC to Grove 是无主动 IC 的 USB Type-C 供电与 Grove 信号分配板。CN1 的两路 VBUS 合并为 +5V，CC1/CC2 各经 5.1KΩ 下拉；+5V 仅送到 CN3/CN4 的 VDD，CN2 VDD 明确未连接。CN2 的 SCL/RX、SDA/TX 和 GND 透传到两个输出端 CN3/CN4，页面未显示保险丝、开关、限流、ESD 或电源转换器。

## 检索关键词

`Unit TypeC to Grove`、`U151`、`USB Type-C`、`CN1`、`CN2`、`CN3`、`CN4`、`CON_GROVE`、`SCL/RX`、`SDA/TX`、`S1`、`S2`、`VBUS1`、`VBUS2`、`CC1`、`CC2`、`R1 5.1K`、`R2 5.1K`、`+5V`、`VDD`、`GND`、`power splitter`、`signal pass-through`、`Grove output`、`power-only USB`、`5V@3A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| CN1 | 未标注 | USB Type-C 电源输入插座，引出 VBUS1/VBUS2、CC1/CC2、GND1/GND2 与 FG | 图 35f784d7f629 / 第 1 页 / 原理图左下 CN1：VBUS1 A9、VBUS2 B9、CC1 A5、CC2 B5、GND1 A12、GND2 B12、FG |
| CN2 | CON_GROVE | 输入侧 Grove 信号端，接入 SCL/RX、SDA/TX 和 GND，VDD 未连接 | 图 35f784d7f629 / 第 1 页 / 原理图左上 CN2 CON_GROVE：pin1 SCL/RX、pin2 SDA/TX、pin3 VDD NC 叉号、pin4 GND |
| CN3 | CON_GROVE | 第一路合并输出，提供透传信号、USB +5V 和公共 GND | 图 35f784d7f629 / 第 1 页 / 原理图上部中央 CN3：pin1 SCL/RX、pin2 SDA/TX、pin3 VDD/+5V、pin4 GND |
| CN4 | CON_GROVE | 第二路合并输出，提供透传信号、USB +5V 和公共 GND | 图 35f784d7f629 / 第 1 页 / 原理图上部右侧 CN4：pin1 SCL/RX、pin2 SDA/TX、pin3 VDD/+5V、pin4 GND |
| R1/R2 | 5.1K / 5.1K | CN1 CC1/CC2 到 GND 的 Type-C 配置下拉电阻 | 图 35f784d7f629 / 第 1 页 / 原理图左下 CN1 CC1/CC2 旁 R1/R2，均标 5.1K 并接 GND |

## 系统结构

### Unit TypeC to Grove

整板由一个 USB Type-C 电源输入、一个 Grove 信号输入、两个 Grove 合并输出和两颗 CC 下拉电阻构成；没有 MCU、存储器、时钟、通信控制器、稳压器或负载开关。

- 参数与网络：`usb_input=CN1`；`signal_input=CN2`；`outputs=CN3,CN4`；`cc_resistors=R1,R2 5.1K`；`active_ic=null`；`controller=null`；`storage=null`；`regulator=null`；`load_switch=null`
- 证据：图 35f784d7f629 / 第 1 页 / 完整原理图仅含 CN1-CN4 与 R1/R2

## 电源

### CN1 VBUS 到 +5V

CN1 VBUS1 与 VBUS2 合并到同一 +5V 网络，该网络直接连接 CN3/CN4 pin 3 VDD；页面未显示保险丝、限流器件、反接保护或电源转换。

- 参数与网络：`source=CN1 VBUS1/VBUS2`；`rail=+5V`；`destinations=CN3 pin3 VDD,CN4 pin3 VDD`；`fuse=null`；`current_limit=null`；`reverse_protection=null`；`converter=null`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN1 VBUS1/VBUS2 +5V 标签与 CN3/CN4 pin3 公共 +5V 线

## 接口

### CN1 USB Type-C

CN1 只画出 VBUS1/VBUS2、CC1/CC2、GND1/GND2 和 FG，没有 D+、D-、SBU 或高速差分线，因此本页实现为纯供电 Type-C 接口。

- 参数与网络：`VBUS1=A9`；`VBUS2=B9`；`CC1=A5`；`CC2=B5`；`GND1=A12`；`GND2=B12`；`data_pins=null`；`role=power input only`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN1 全部可见引脚，无 USB D+/D-

### CC1/CC2

CN1 CC1 pin A5 经 R1 5.1K 接 GND，CC2 pin B5 经 R2 5.1K 接 GND。

- 参数与网络：`CC1=CN1 A5 via R1 5.1K to GND`；`CC2=CN1 B5 via R2 5.1K to GND`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN1 CC1/CC2 至 R1/R2 5.1K-GND

### CN2 输入 Grove

CN2 pin 1 接 SCL/RX，pin 2 接 SDA/TX，pin 3 VDD 带未连接叉号，pin 4 接公共 GND。

- 参数与网络：`pin_1=SCL/RX`；`pin_2=SDA/TX`；`pin_3=VDD NC`；`pin_4=GND`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN2 pins1-4，pin3 NC 叉号与 pin4 GND 连线

### CN3/CN4 输出 Grove

CN3 与 CN4 pinout 相同：pin 1=SCL/RX，pin 2=SDA/TX，pin 3=VDD/+5V，pin 4=GND。

- 参数与网络：`CN3=pin1 SCL/RX,pin2 SDA/TX,pin3 +5V,pin4 GND`；`CN4=pin1 SCL/RX,pin2 SDA/TX,pin3 +5V,pin4 GND`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN3/CN4 pins1-4 及 SCL/RX、SDA/TX、VDD、GND

## 保护电路

### USB/Grove 保护边界

除 CC1/CC2 的 R1/R2 外，页面未显示 VBUS、+5V、SCL/RX、SDA/TX 上的 TVS/ESD、保险丝、限流、反接、过压或浪涌保护。

- 参数与网络：`tv_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`surge=null`；`only_resistors=R1/R2 CC pulldowns`
- 证据：图 35f784d7f629 / 第 1 页 / 完整原理图仅含连接器与 CC 下拉，无保护器件

## 关键网络

### SCL/RX 与 SDA/TX

CN2 pin 1、CN3 pin 1、CN4 pin 1 共用 SCL/RX 网络；CN2 pin 2、CN3 pin 2、CN4 pin 2 共用 SDA/TX 网络，信号无缓冲、切换或串联器件。

- 参数与网络：`signal_1=CN2.1=CN3.1=CN4.1 SCL/RX`；`signal_2=CN2.2=CN3.2=CN4.2 SDA/TX`；`buffer=null`；`mux=null`；`series_resistor=null`；`direction=passive bidirectional`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图上部 CN2-CN3-CN4 两条连续信号线

### GND

CN1 GND1/GND2/FG、CN2 pin 4、CN3 pin 4 和 CN4 pin 4 均连接公共 GND。

- 参数与网络：`usb_ground=CN1 GND1,GND2,FG`；`input_ground=CN2 pin4`；`output_grounds=CN3 pin4,CN4 pin4`；`net=GND`
- 证据：图 35f784d7f629 / 第 1 页 / 原理图 CN1 与 CN2/CN3/CN4 公共 GND 符号和连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit TypeC to Grove | `usb_input=CN1`；`signal_input=CN2`；`outputs=CN3,CN4`；`cc_resistors=R1,R2 5.1K`；`active_ic=null`；`controller=null`；`storage=null`；`regulator=null`；`load_switch=null` |
| 接口 | CN1 USB Type-C | `VBUS1=A9`；`VBUS2=B9`；`CC1=A5`；`CC2=B5`；`GND1=A12`；`GND2=B12`；`data_pins=null`；`role=power input only` |
| 接口 | CC1/CC2 | `CC1=CN1 A5 via R1 5.1K to GND`；`CC2=CN1 B5 via R2 5.1K to GND` |
| 电源 | CN1 VBUS 到 +5V | `source=CN1 VBUS1/VBUS2`；`rail=+5V`；`destinations=CN3 pin3 VDD,CN4 pin3 VDD`；`fuse=null`；`current_limit=null`；`reverse_protection=null`；`converter=null` |
| 接口 | CN2 输入 Grove | `pin_1=SCL/RX`；`pin_2=SDA/TX`；`pin_3=VDD NC`；`pin_4=GND` |
| 接口 | CN3/CN4 输出 Grove | `CN3=pin1 SCL/RX,pin2 SDA/TX,pin3 +5V,pin4 GND`；`CN4=pin1 SCL/RX,pin2 SDA/TX,pin3 +5V,pin4 GND` |
| 关键网络 | SCL/RX 与 SDA/TX | `signal_1=CN2.1=CN3.1=CN4.1 SCL/RX`；`signal_2=CN2.2=CN3.2=CN4.2 SDA/TX`；`buffer=null`；`mux=null`；`series_resistor=null`；`direction=passive bidirectional` |
| 关键网络 | GND | `usb_ground=CN1 GND1,GND2,FG`；`input_ground=CN2 pin4`；`output_grounds=CN3 pin4,CN4 pin4`；`net=GND` |
| 保护电路 | USB/Grove 保护边界 | `tv_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`surge=null`；`only_resistors=R1/R2 CC pulldowns` |
| 接口 | INPUT CH GND | `document_mapping=INPUT CH Black=NC`；`schematic_mapping=CN2 pin4=GND`；`confirmed_hardware=null` |
| 总线 | S1/S2 与 SCL/RX/SDA/TX | `document_names=S1,S2`；`schematic_names=SCL/RX,SDA/TX`；`i2c_controller=null`；`uart_controller=null`；`confirmed_protocol=null` |
| 电源 | MAX 5V@3A | `documented_rating=MAX 5V@3A`；`schematic_voltage=+5V`；`current_rating_label=null`；`fuse=null`；`thermal_data=null`；`copper_width=null` |
| 接口 | Grove 线色映射 | `schematic_pinout=pin1 SCL/RX,pin2 SDA/TX,pin3 VDD,pin4 GND`；`color_labels=null`；`document_colors=Black,Red,Yellow,White` |

## 待确认事项

- `interface.input-ground-conflict`：正文表将 INPUT CH 的 Black/GND 标为 NC，但原理图明确把 CN2 pin 4 接到公共 GND；实际产品输入端地线是否连接存在资料冲突。（证据：图 35f784d7f629 / 第 1 页 / 原理图 CN2 pin4 绿色连线接 GND 并延伸到 CN3/CN4 pin4）
- `bus.signal-function`：正文把两条透传信号称为 S1/S2，原理图将其标为 SCL/RX 与 SDA/TX；没有控制器或协议器件，无法仅凭本页确定应按 I2C、UART 还是通用信号使用。（证据：图 35f784d7f629 / 第 1 页 / 原理图 CN2-CN4 信号标签 SCL/RX 与 SDA/TX，无协议 IC）
- `power.documented-current-rating`：正文标称 MAX 5V@3A；原理图只显示直接铜网连接，没有连接器额定值、铜宽、温升、保险丝或限流器件，不能由本页确认连续 3A 能力。（证据：图 35f784d7f629 / 第 1 页 / 原理图 VBUS-to-CN3/CN4 +5V 直连，无电流或热参数）
- `interface.grove-color-mapping`：原理图给出连接器 pin 1-4 与网络，但未标注 Black/Red/Yellow/White 线色，无法仅凭本页验证输出线色和输入线色。（证据：图 35f784d7f629 / 第 1 页 / 原理图 CN2/CN3/CN4 无颜色文字）
- `review.input-ground`：请用 PCB 连通性或实物测量确认 INPUT CH 的 GND 是否连接输出公共 GND。；原因：正文标 NC，而原理图明确接 GND。
- `review.signal-function`：请确认 S1/S2 与 SCL/RX/SDA/TX 的命名对应及支持的总线/信号用途。；原因：正文和原理图命名不同，板上无协议控制器。
- `review.current-rating`：请用连接器额定值、PCB 铜厚/线宽和温升测试确认 5V@3A 连续供电能力。；原因：原理图没有电流或热设计参数。
- `review.grove-colors`：请结合 Grove 连接器方向和线缆规范确认 Black/Red/Yellow/White 与各 pin 的对应。；原因：原理图不含线色。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5fae073308391c2f6a7820e8424d2a5b12032b4d60c87248505be7195f4580be` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/typec2grove/@akita.webp` |
| 2 | 1 | `35f784d7f629f505add1f9d2281910cc2ab08d52a00ed298e0d34d3990d551fb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/605/UNIT-TypeC2Grove_sch_sch_01.png` |

---

源文档：`zh_CN/unit/typec2grove.md`

源文档 SHA-256：`df4d047486dbb7a99e675930e23389c0365b634e9c282bfe657c9cd1f7ee83ef`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
