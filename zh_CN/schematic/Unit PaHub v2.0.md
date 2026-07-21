# Unit PaHub v2.0 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PaHub v2.0 |
| SKU | U040-B |
| 产品 ID | `unit-pahub-v2-0-52108d21a0fe` |
| 源文档 | `zh_CN/unit/pahub2.md` |

## 概述

Unit PaHub v2.0 以原理图标注的 U1 TCA9548A 将上游 IIC_SCL/IIC_SDA 分配到六组下游 SC0/SD0 至 SC5/SD5，总线通道 6 和 7 未使用。J7 是上游 Grove I2C 入口，J1-J6 是六个下游 Grove I2C 端口；所有端口共用 VCC/GND，每条 I2C 线均有 10KΩ 上拉。A0-A2 由 0Ω 上拉位和 10KΩ 下拉电阻配置，RESET 由 R7 10KΩ 上拉，实际装配地址和正文所称 PCA9548AP 型号需要进一步确认。

## 检索关键词

`Unit PaHub v2.0`、`U040-B`、`PaHub2`、`TCA9548A`、`PCA9548AP`、`U1`、`I2C multiplexer`、`I2C switch`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`SC0`、`SD0`、`SC1`、`SD1`、`SC2`、`SD2`、`SC3`、`SD3`、`SC4`、`SD4`、`SC5`、`SD5`、`A0`、`A1`、`A2`、`RESET`、`0x70`、`J1-J6`、`J7`、`GROVE_I2C`、`VCC`、`10KΩ pull-up`、`six-channel I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TCA9548A | 8 通道 I2C 多路开关，本板使用通道 0-5 并保留 A0-A2 地址配置与 RESET | 图 a16916708fe9 / 第 1 页 / 页面 B2-C2 U1，器件值 TCA9548A，SCL/SDA/RESET、SD0-SD7、SC0-SC7、A0-A2、VCC/GND 引脚 |
| J7 | GROVE_I2C | 上游 I2C 与 VCC/GND 输入连接器 | 图 a16916708fe9 / 第 1 页 / 页面 B1 左侧 J7 GROVE_I2C：pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC、pin 4 GND |
| J1-J6 | GROVE_I2C | 六组下游 I2C 端口，分别连接 U1 通道 0-5 并共用 VCC/GND | 图 a16916708fe9 / 第 1 页 / 页面 B3-C4 J1-J6 GROVE_I2C：SC0/SD0 至 SC5/SD5、VCC、GND |
| R1-R3 | 10KΩ (103) ±5% resistor array | 六路下游 SC0-SC5 与 SD0-SD5 的 VCC 上拉阵列 | 图 a16916708fe9 / 第 1 页 / 页面 B4-C4 R1/R2/R3，均标 10KΩ (103) ±5%，每组四路上拉到 VCC |
| R5/R6/R7 | 10KΩ | R5/R6 上拉上游 IIC_SCL/IIC_SDA，R7 上拉 U1 RESET | 图 a16916708fe9 / 第 1 页 / 页面 B1-B2 U1 左上方 R5/R6/R7 10KΩ，三者上端接 VCC，下端分别接 SCL、SDA、RESET |
| R12-R14/R19-R21 | 0Ω / 10KΩ | U1 A0-A2 地址脚的 VCC 上拉选配位与默认下拉网络 | 图 a16916708fe9 / 第 1 页 / 页面 C1-C2：R12/R13/R14 标 0Ω 接 VCC，R19/R20/R21 标 10KΩ 接 GND，中点分别连接 U1 A0/A1/A2 |
| C1-C5/C7/C8 | 100nF | 上游入口和六个下游端口附近的 VCC-GND 去耦电容 | 图 a16916708fe9 / 第 1 页 / 页面 B1-C4：C3 位于 J7，C1/C2/C4/C5/C7/C8 分别位于 J1-J6，全部 100nF 跨接 VCC-GND |

## 系统结构

### Unit PaHub v2.0

U1 将一组上游 IIC_SCL/IIC_SDA 多路连接到六组下游 I2C 端口；本板没有独立 MCU、存储器、晶振、充电器或电源转换器。

- 参数与网络：`switch=U1 TCA9548A`；`upstream=J7 IIC_SCL/IIC_SDA`；`downstream_ports=J1-J6`；`used_channels=0,1,2,3,4,5`；`unused_channels=6,7`；`controller=null`；`storage=null`；`clock=null`
- 证据：图 a16916708fe9 / 第 1 页 / 整页：J7-U1-J1至J6 组成总线分配结构，U1 通道 6/7 带 NC 叉号，无其他 IC

## 核心器件

### U1 TCA9548A

U1 上游 SCL/SDA 分别为 pin 22/pin 23，RESET 为 pin 3，VCC 为 pin 24，GND 为 pin 12，A0/A1/A2 分别为 pin 1/pin 2/pin 21。

- 参数与网络：`SCL=pin 22`；`SDA=pin 23`；`RESET=pin 3`；`VCC=pin 24`；`GND=pin 12`；`A0=pin 1`；`A1=pin 2`；`A2=pin 21`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B2-C2 U1 左侧 SCL/SDA/RESET/A0-A2/VCC/GND 的 pin 编号

## 电源

### VCC/GND 分配

J7 pin 3 输入的 VCC 直接连接 U1 pin 24、J1-J6 pin 3、全部总线上拉与去耦；J7 及 J1-J6 pin 4 和 U1 pin 12 共用 GND。板上未显示稳压器、LDO 或负载开关。

- 参数与网络：`input=J7 pin 3 VCC`；`switch_supply=U1 pin 24 VCC`；`downstream_power=J1-J6 pin 3 VCC`；`ground=J7/J1-J6 pin 4 and U1 pin 12`；`regulator=null`；`ldo=null`；`load_switch=null`
- 证据：图 a16916708fe9 / 第 1 页 / 整页 VCC/GND 标记：J7、U1、J1-J6、R/C 网络，无电源转换器件

### C1-C5/C7/C8

J7 旁 C3 以及 J1-J6 旁 C1、C2、C4、C5、C7、C8 均为 100nF，并分别跨接 VCC 与 GND。

- 参数与网络：`upstream=C3 100nF at J7`；`channel_0=C1 100nF at J1`；`channel_1=C2 100nF at J2`；`channel_2=C4 100nF at J3`；`channel_3=C5 100nF at J4`；`channel_4=C7 100nF at J5`；`channel_5=C8 100nF at J6`；`connection=VCC to GND`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B1-C4 各 Grove 端口旁的 C3/C1/C2/C4/C5/C7/C8 100nF

## 接口

### J7 GROVE_I2C

J7 pin 1 为 IIC_SCL，pin 2 为 IIC_SDA，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`reference=J7`；`part_number=GROVE_I2C`；`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B1 左侧 J7 GROVE_I2C 的 pin 1-4 标签

### J1-J6 GROVE_I2C

六个下游端口采用相同 pinout：pin 1 为对应 SCx，pin 2 为对应 SDx，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`J1=pin1 SC0,pin2 SD0,pin3 VCC,pin4 GND`；`J2=pin1 SC1,pin2 SD1,pin3 VCC,pin4 GND`；`J3=pin1 SC2,pin2 SD2,pin3 VCC,pin4 GND`；`J4=pin1 SC3,pin2 SD3,pin3 VCC,pin4 GND`；`J5=pin1 SC4,pin2 SD4,pin3 VCC,pin4 GND`；`J6=pin1 SC5,pin2 SD5,pin3 VCC,pin4 GND`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B3-C4 J1-J6，每个 GROVE_I2C 符号均显示 SCx/SDx/VCC/GND 对应 pin 1/2/3/4

## 总线

### J7 到 U1 上游 I2C

J7 pin 1 的 IIC_SCL 连接 U1 SCL pin 22，J7 pin 2 的 IIC_SDA 连接 U1 SDA pin 23；两条线上分别有 R5、R6 10KΩ 上拉至 VCC。

- 参数与网络：`controller_side_connector=J7`；`SCL=J7 pin 1 IIC_SCL to U1 pin 22 via same net`；`SDA=J7 pin 2 IIC_SDA to U1 pin 23 via same net`；`SCL_pullup=R5 10KΩ to VCC`；`SDA_pullup=R6 10KΩ to VCC`；`direction=bidirectional`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B1-B2 J7 IIC_SCL/IIC_SDA 到 U1 SCL/SDA，并接 R5/R6 10KΩ

### U1 通道 0-2

U1 SD0 pin 4/SC0 pin 5 连接 J1 pin 2/pin 1，SD1 pin 6/SC1 pin 7 连接 J2 pin 2/pin 1，SD2 pin 8/SC2 pin 9 连接 J3 pin 2/pin 1。

- 参数与网络：`channel_0=U1 SD0 pin4->J1 pin2; U1 SC0 pin5->J1 pin1`；`channel_1=U1 SD1 pin6->J2 pin2; U1 SC1 pin7->J2 pin1`；`channel_2=U1 SD2 pin8->J3 pin2; U1 SC2 pin9->J3 pin1`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B2-B4 U1 SD0/SC0、SD1/SC1、SD2/SC2 与 J1/J2/J3 同名网络和 pin 编号

### U1 通道 3-5

U1 SD3 pin 10/SC3 pin 11 连接 J4 pin 2/pin 1，SD4 pin 13/SC4 pin 14 连接 J5 pin 2/pin 1，SD5 pin 15/SC5 pin 16 连接 J6 pin 2/pin 1。

- 参数与网络：`channel_3=U1 SD3 pin10->J4 pin2; U1 SC3 pin11->J4 pin1`；`channel_4=U1 SD4 pin13->J5 pin2; U1 SC4 pin14->J5 pin1`；`channel_5=U1 SD5 pin15->J6 pin2; U1 SC5 pin16->J6 pin1`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B2-C4 U1 SD3/SC3、SD4/SC4、SD5/SC5 与 J4/J5/J6 同名网络和 pin 编号

### SC0-SC5/SD0-SD5 上拉

R1 将 SD0、SC0、SD1、SC1 上拉至 VCC，R2 将 SD2、SC2、SD3、SC3 上拉至 VCC，R3 将 SD4、SC4、SD5、SC5 上拉至 VCC；每路阻值标注 10KΩ (103) ±5%。

- 参数与网络：`R1=SD0,SC0,SD1,SC1; 10KΩ each to VCC`；`R2=SD2,SC2,SD3,SC3; 10KΩ each to VCC`；`R3=SD4,SC4,SD5,SC5; 10KΩ each to VCC`；`tolerance=±5%`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B4-C4 R1-R3 网络标签、公共 VCC 端和 10KΩ (103) ±5% 标注

### U1 通道 6 和 7

U1 的 SD6 pin 17、SC6 pin 18、SD7 pin 19、SC7 pin 20 均带未连接叉号，因此本板只实现六个下游通道。

- 参数与网络：`SD6=pin 17 NC`；`SC6=pin 18 NC`；`SD7=pin 19 NC`；`SC7=pin 20 NC`；`implemented_channels=6`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 C2 U1 右下 SD6/SC6/SD7/SC7 pin 17-20 的红色 NC 叉号

## 总线地址

### U1 A0-A2 地址绑带

A0、A1、A2 各自具有一条 0Ω 到 VCC 的上拉路径和一条 10KΩ 到 GND 的下拉路径：A0 对应 R12/R19，A1 对应 R13/R20，A2 对应 R14/R21。

- 参数与网络：`A0=R12 0Ω to VCC; R19 10KΩ to GND`；`A1=R13 0Ω to VCC; R20 10KΩ to GND`；`A2=R14 0Ω to VCC; R21 10KΩ to GND`；`address_pins=U1 pin1 A0,pin2 A1,pin21 A2`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 C1-C2 R12-R14/R19-R21 与 U1 A0/A1/A2 三条水平连接

## 复位

### U1 RESET

U1 RESET pin 3 由 R7 10KΩ 上拉至 VCC，未连接外部复位开关或连接器。

- 参数与网络：`pin=U1 pin 3 RESET`；`pullup=R7 10KΩ to VCC`；`external_reset=null`
- 证据：图 a16916708fe9 / 第 1 页 / 页面 B2 U1 RESET pin 3 与 R7 10KΩ-VCC 直接连接

## 保护电路

### I2C 与电源接口

上游和六路下游 I2C 均直接连接 U1 并上拉到同一 VCC；本页未显示电平转换器、TVS/ESD 阵列、保险丝、反接保护或端口负载开关。

- 参数与网络：`level_shifter=null`；`tv_esd=null`；`fuse=null`；`reverse_polarity_protection=null`；`per_port_load_switch=null`；`bus_voltage_domain=shared VCC`
- 证据：图 a16916708fe9 / 第 1 页 / 整页 J7-U1-J1至J6 直接总线和共享 VCC 路径，未见保护或电平转换器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PaHub v2.0 | `switch=U1 TCA9548A`；`upstream=J7 IIC_SCL/IIC_SDA`；`downstream_ports=J1-J6`；`used_channels=0,1,2,3,4,5`；`unused_channels=6,7`；`controller=null`；`storage=null`；`clock=null` |
| 核心器件 | U1 TCA9548A | `SCL=pin 22`；`SDA=pin 23`；`RESET=pin 3`；`VCC=pin 24`；`GND=pin 12`；`A0=pin 1`；`A1=pin 2`；`A2=pin 21` |
| 总线 | J7 到 U1 上游 I2C | `controller_side_connector=J7`；`SCL=J7 pin 1 IIC_SCL to U1 pin 22 via same net`；`SDA=J7 pin 2 IIC_SDA to U1 pin 23 via same net`；`SCL_pullup=R5 10KΩ to VCC`；`SDA_pullup=R6 10KΩ to VCC`；`direction=bidirectional` |
| 接口 | J7 GROVE_I2C | `reference=J7`；`part_number=GROVE_I2C`；`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | U1 通道 0-2 | `channel_0=U1 SD0 pin4->J1 pin2; U1 SC0 pin5->J1 pin1`；`channel_1=U1 SD1 pin6->J2 pin2; U1 SC1 pin7->J2 pin1`；`channel_2=U1 SD2 pin8->J3 pin2; U1 SC2 pin9->J3 pin1` |
| 总线 | U1 通道 3-5 | `channel_3=U1 SD3 pin10->J4 pin2; U1 SC3 pin11->J4 pin1`；`channel_4=U1 SD4 pin13->J5 pin2; U1 SC4 pin14->J5 pin1`；`channel_5=U1 SD5 pin15->J6 pin2; U1 SC5 pin16->J6 pin1` |
| 接口 | J1-J6 GROVE_I2C | `J1=pin1 SC0,pin2 SD0,pin3 VCC,pin4 GND`；`J2=pin1 SC1,pin2 SD1,pin3 VCC,pin4 GND`；`J3=pin1 SC2,pin2 SD2,pin3 VCC,pin4 GND`；`J4=pin1 SC3,pin2 SD3,pin3 VCC,pin4 GND`；`J5=pin1 SC4,pin2 SD4,pin3 VCC,pin4 GND`；`J6=pin1 SC5,pin2 SD5,pin3 VCC,pin4 GND` |
| 总线 | SC0-SC5/SD0-SD5 上拉 | `R1=SD0,SC0,SD1,SC1; 10KΩ each to VCC`；`R2=SD2,SC2,SD3,SC3; 10KΩ each to VCC`；`R3=SD4,SC4,SD5,SC5; 10KΩ each to VCC`；`tolerance=±5%` |
| 总线 | U1 通道 6 和 7 | `SD6=pin 17 NC`；`SC6=pin 18 NC`；`SD7=pin 19 NC`；`SC7=pin 20 NC`；`implemented_channels=6` |
| 复位 | U1 RESET | `pin=U1 pin 3 RESET`；`pullup=R7 10KΩ to VCC`；`external_reset=null` |
| 总线地址 | U1 A0-A2 地址绑带 | `A0=R12 0Ω to VCC; R19 10KΩ to GND`；`A1=R13 0Ω to VCC; R20 10KΩ to GND`；`A2=R14 0Ω to VCC; R21 10KΩ to GND`；`address_pins=U1 pin1 A0,pin2 A1,pin21 A2` |
| 电源 | VCC/GND 分配 | `input=J7 pin 3 VCC`；`switch_supply=U1 pin 24 VCC`；`downstream_power=J1-J6 pin 3 VCC`；`ground=J7/J1-J6 pin 4 and U1 pin 12`；`regulator=null`；`ldo=null`；`load_switch=null` |
| 电源 | C1-C5/C7/C8 | `upstream=C3 100nF at J7`；`channel_0=C1 100nF at J1`；`channel_1=C2 100nF at J2`；`channel_2=C4 100nF at J3`；`channel_3=C5 100nF at J4`；`channel_4=C7 100nF at J5`；`channel_5=C8 100nF at J6`；`connection=VCC to GND` |
| 保护电路 | I2C 与电源接口 | `level_shifter=null`；`tv_esd=null`；`fuse=null`；`reverse_polarity_protection=null`；`per_port_load_switch=null`；`bus_voltage_domain=shared VCC` |
| 核心器件 | U1 多路开关型号 | `schematic_model=TCA9548A`；`document_model=PCA9548AP`；`reference=U1`；`assembled_model=null` |
| 总线地址 | U1 默认 I2C 地址 | `document_default=0x70`；`address_pins=A2,A1,A0`；`high_straps=R12,R13,R14 0Ω to VCC`；`low_straps=R19,R20,R21 10KΩ to GND`；`population_marks=null`；`confirmed_address=null` |
| 电源 | VCC 标称电压 | `schematic_rail=VCC`；`schematic_voltage=null`；`document_voltage=5V`；`affected_interfaces=J7,J1-J6,U1,pullups` |
| 接口 | Grove 线色映射 | `upstream_pinout=J7 pin1 IIC_SCL,pin2 IIC_SDA,pin3 VCC,pin4 GND`；`downstream_pinout=J1-J6 pin1 SCx,pin2 SDx,pin3 VCC,pin4 GND`；`color_labels_on_schematic=null`；`document_colors=Black,Red,Yellow,White` |
| 总线 | I2C 通信速率 | `bus=I2C`；`upstream_pullups=10KΩ`；`downstream_pullups=10KΩ each line`；`clock_rate=null`；`mode=null`；`bus_capacitance=null` |

## 待确认事项

- `component.mux-model-conflict`：原理图 U1 明确标注 TCA9548A，而产品正文写 PCA9548AP；仅凭现有页面无法确认实际装配型号。（证据：图 a16916708fe9 / 第 1 页 / 页面 C2 U1 器件值清晰标注 TCA9548A）
- `address.default-i2c-address`：正文声称默认地址 0x70，但原理图同时画出 A0-A2 的 0Ω VCC 上拉位与 10KΩ GND 下拉，且未标注 DNP/装配状态，也未给出地址编码表，因此无法仅凭原理图确认默认地址。（证据：图 a16916708fe9 / 第 1 页 / 页面 C1-C2 A0-A2 的 R12-R14 0Ω 上拉与 R19-R21 10KΩ 下拉；无 DNP 或 0x70 标注）
- `power.vcc-voltage`：产品正文 Grove 表将电源写为 5V，但原理图只使用 VCC 网络名，没有标注具体电压，因此不能仅凭本页确认总线与下游端口电平为 5 V。（证据：图 a16916708fe9 / 第 1 页 / 整页电源节点均标 VCC，无 5V 或其他电压数值）
- `interface.grove-color-mapping`：原理图给出所有连接器的 pin 1-4 电气网络，但没有 Black/Red/Yellow/White 线色标注，无法仅凭原理图验证正文中的 Grove 线色映射。（证据：图 a16916708fe9 / 第 1 页 / 页面 J7 与 J1-J6 仅显示网络名和 pin 编号，无线色文字）
- `bus.i2c-speed`：原理图证明 I2C 物理拓扑和 10KΩ 上拉，但未给出 Standard/Fast/Fast-mode Plus 模式、最高速率或总线电容限制，通信速率不能由本页确定。（证据：图 a16916708fe9 / 第 1 页 / 整页 IIC_SCL/IIC_SDA 和 SC0-SC5/SD0-SD5 网络，无频率或模式注释）
- `review.mux-model-conflict`：请用 BOM、PCB 丝印或采购料号确认 U1 实际装配为 TCA9548A 还是 PCA9548AP。；原因：原理图与产品正文型号不一致，不能把两者视为同一已确认料号。
- `review.default-address`：请核对 R12-R14 与 R19-R21 的实际装配状态，并结合确认后的 U1 datasheet 确定出厂默认 I2C 地址。；原因：原理图没有 DNP 标记或地址编码表，无法证明正文所述 0x70。
- `review.vcc-voltage`：请用当前硬件版本电源规范或实板测量确认 J7/J1-J6 与 U1 的 VCC 标称电压。；原因：原理图只写 VCC，正文 5V 不能替代该页电压证据。
- `review.grove-color-mapping`：请结合 Grove 线缆规范和连接器方向确认 Black/Red/Yellow/White 与各 pin 的对应关系。；原因：原理图仅显示电气 pinout，没有线色。
- `review.i2c-speed`：请结合确认后的 U1 datasheet、总线电容和线缆长度确定支持的 I2C 模式与最高可靠速率。；原因：10KΩ 上拉和拓扑不足以单独证明具体通信速率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a16916708fe9e80f119e1a40b7e5a7cff1fecfe59a6187ca9f5811ce3aede87a` | `https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_sch_01.webp` |

---

源文档：`zh_CN/unit/pahub2.md`

源文档 SHA-256：`17786dc7d0e119af9a7f8b423aa08bf9bd989523fc0b0eee6c20d398b41285fd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
