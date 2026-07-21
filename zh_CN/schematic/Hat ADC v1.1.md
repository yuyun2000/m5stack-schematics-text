# Hat ADC v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ADC v1.1 |
| SKU | U069-V11 |
| 产品 ID | `hat-adc-v1-1-d69fd0bf927a` |
| 源文档 | `zh_CN/hat/HAT-ADC-V11.md` |

## 概述

Hat ADC v1.1 以 ADS1110（U1）完成差分模拟输入到 I2C 的转换，P2 两针端子通过 R3、R4、R5 网络连接 VIN+ 与 VIN-。U1 使用 P1 STICKIO 引入的 +3.3V 供电，SCL/SDA 分别连接 G26/G0，并由 R1、R2 各 4.7KΩ 上拉至 +3.3V。原理图未显示电源转换器、外部时钟或专用输入保护器件，也未标注产品正文所述的 0x48 地址和 0~12V 额定输入范围。

## 检索关键词

`Hat ADC v1.1`、`U069-V11`、`ADS1110`、`U1`、`STICKIO`、`P1`、`P2`、`VIN+`、`VIN-`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 510KΩ`、`R4 100KΩ`、`R5 0Ω`、`C1 100nF`、`0x48`、`0~12V`、`差分输入`、`模拟采样`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ADS1110 | 差分输入 I2C 模数转换器，连接 VIN+/VIN-、SCL/SDA、+3.3V 和 GND | 图 5cf49dc14fe1 / 第 1 页 / B2-B3 区域 U1：ADS1110，1 VIN+、2 GND、3 SCL、4 SDA、5 VDD、6 VIN- |
| P1 | STICKIO | 8 针主机接口，向 ADC 提供 +3.3V、GND、SCL/G26 与 SDA/G0 | 图 5cf49dc14fe1 / 第 1 页 / B3-B4 区域 P1 STICKIO：1~8 脚及 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN 标注 |
| P2 | Header 2 | 两针模拟输入端子，1 脚经 R3 接 VIN+ 衰减节点，2 脚连接 VIN- 参考节点 | 图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 P2 Header 2：1 脚连接 R3 左端，2 脚连接 U1.6 VIN- 水平网络 |
| R1 | 4.7KΩ | 将 SCL 上拉至 +3.3V | 图 5cf49dc14fe1 / 第 1 页 / B3 区域 U1.3 SCL 上方：R1 4.7KΩ 连接 SCL 与 +3.3V |
| R2 | 4.7KΩ | 将 SDA 上拉至 +3.3V | 图 5cf49dc14fe1 / 第 1 页 / B3 区域 U1.4 SDA 上方：R2 4.7KΩ 连接 SDA 与 +3.3V |
| R3 | 510KΩ | P2.1 至 U1 VIN+ 节点的输入串联电阻 | 图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 P2.1 右侧：R3 510KΩ 串接至 U1.1 VIN+ 节点 |
| R4 | 100KΩ | 跨接 U1 VIN+ 与 VIN- 节点的差分输入电阻 | 图 5cf49dc14fe1 / 第 1 页 / B2 区域 R4 100KΩ：左端接 R3 后的 VIN+ 节点，右端接 P2.2/U1.6 VIN- 节点 |
| R5 | 0Ω | 将 VIN- 与 P2.2 所在参考节点接至 GND | 图 5cf49dc14fe1 / 第 1 页 / B2 区域 U1.6 VIN- 左下：R5 0Ω 从 VIN-/P2.2 节点接 GND |
| C1 | 100nF | U1 +3.3V VDD 对 GND 的去耦电容 | 图 5cf49dc14fe1 / 第 1 页 / B2 区域 U1.5 VDD 左侧：C1 100nF 跨接 +3.3V 与 GND |

## 系统结构

### Hat ADC v1.1

P2 模拟输入经 R3/R4/R5 网络连接 U1 ADS1110 的 VIN+/VIN-；U1 通过 SCL/SDA 与 P1 STICKIO 通信，并由 P1 的 +3.3V/GND 供电。

- 参数与网络：`adc=U1 ADS1110`；`analog_input=P2 Header 2`；`input_network=R3 510KΩ; R4 100KΩ; R5 0Ω`；`host_interface=P1 STICKIO SCL/SDA`；`supply=+3.3V`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B1-B4 区域：P2、R3/R4/R5、U1、R1/R2 与 P1 的完整信号和供电连接

## 核心器件

### U1 ADS1110

U1.1 为 VIN+，U1.6 为 VIN-，U1.5 VDD 接 +3.3V，U1.2 GND 接地，U1.3/U1.4 分别为 SCL/SDA。

- 参数与网络：`pin_1=VIN+`；`pin_2=GND`；`pin_3=SCL`；`pin_4=SDA`；`pin_5=VDD +3.3V`；`pin_6=VIN-`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B2-B3 区域 U1 ADS1110 符号周围的 1~6 脚编号、名称和网络

## 电源

### U1 +3.3V 供电

P1.7 3V3 引入 +3.3V 并连接 U1.5 VDD；U1.2 GND 接地，C1 100nF 跨接 +3.3V 与 GND。

- 参数与网络：`supply_input=P1.7 3V3`；`adc_supply=U1.5 VDD +3.3V`；`adc_ground=U1.2 GND`；`decoupling=C1 100nF`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B2-B4 区域 P1.7 +3.3V、U1.5 VDD、U1.2 GND 与 C1 的同名电源连接

### 板载电源结构

原理图中 U1 直接使用 P1 引入的 +3.3V，页面未显示 LDO、DC-DC、负载开关、充电或电池监测电路。

- 参数与网络：`adc_rail=+3.3V`；`source=P1.7 3V3`；`ldo=not shown`；`dc_dc=not shown`；`load_switch=not shown`；`charger=not shown`
- 证据：图 5cf49dc14fe1 / 第 1 页 / 全页 P1.7 至 U1.5 VDD 的 +3.3V 供电路径，未见电源转换或充电器件

## 接口

### P1 STICKIO

P1.1 接 GND，P1.2 标为 5VOUT 且外侧网络名为 VCC，P1.3 G26 接 SCL，P1.5 G0 接 SDA，P1.7 3V3 接 +3.3V；P1.4 G36、P1.6 BAT 与 P1.8 5VIN 标为未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT VCC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B3-B4 区域 P1：1~8 脚、符号内名称、左侧网络标签及 4/6/8 脚未连接标记

### P2 Header 2

P2.1 经 R3 510KΩ 接至 VIN+ 节点；P2.2 直接连接 VIN- 节点，并经 R5 0Ω 接 GND。

- 参数与网络：`pin_1=via R3 510KΩ to U1.1 VIN+`；`pin_2=U1.6 VIN- and via R5 0Ω to GND`；`direction=analog input`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 P2 两脚至 R3、R5、U1.1/U1.6 的连线和连接点

## 总线

### I2C SCL/SDA

U1.3 SCL 连接 P1.3 G26，U1.4 SDA 连接 P1.5 G0；两条信号线未显示串联电阻或电平转换器。

- 参数与网络：`scl=U1.3 SCL to P1.3 G26`；`sda=U1.4 SDA to P1.5 G0`；`direction=bidirectional`；`level_shifter=not shown`；`series_resistors=not shown`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B3 区域 U1.3/U1.4 至 P1.3/P1.5 的 SCL/SDA 同名网络

### I2C 上拉网络

R1 4.7KΩ 将 SCL 上拉至 +3.3V，R2 4.7KΩ 将 SDA 上拉至 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`pullup_rail=+3.3V`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B3 区域 R1/R2 上端 +3.3V 与下端 SCL/SDA 连接

## 时钟

### U1 时钟

该页 ADS1110 符号没有外部时钟引脚连接，页面也未显示晶振、谐振器或外部时钟源。

- 参数与网络：`external_crystal=not shown`；`external_clock_net=not shown`
- 证据：图 5cf49dc14fe1 / 第 1 页 / 全页 U1 六脚符号及周边器件：仅 VIN+/VIN-/VDD/GND/SCL/SDA，无时钟器件

## 保护电路

### P2 模拟输入保护

P2 至 U1 的输入路径仅显示 R3、R4、R5，未显示 TVS、钳位二极管、保险丝或其他专用浪涌/反接保护器件。

- 参数与网络：`series_network=R3/R4/R5`；`tvs=not shown`；`clamp_diodes=not shown`；`fuse=not shown`；`reverse_protection=not shown`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 P2 到 U1 VIN+/VIN- 的完整可见路径

## 模拟电路

### VIN+ / VIN- 输入网络

R3 510KΩ 从 P2.1 串接到 VIN+；R4 100KΩ 跨接 VIN+ 与 VIN-；VIN- 与 P2.2 同节点，并通过 R5 0Ω 接地。

- 参数与网络：`series_resistor=R3 510KΩ`；`differential_resistor=R4 100KΩ`；`vin_minus_ground_link=R5 0Ω`；`positive_input=U1.1 VIN+`；`negative_input=U1.6 VIN-`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域：R3/R4/R5、P2 与 U1 VIN+/VIN- 的全部连接点

### R3/R4 输入衰减

在 R5 0Ω 将 VIN- 接地的图示配置下，R3=510KΩ 与 R4=100KΩ 构成从 P2.1 到 VIN+ 的标称电阻分压，分压关系为 100KΩ/(510KΩ+100KΩ)。

- 参数与网络：`upper_resistor=R3 510KΩ`；`lower_resistor=R4 100KΩ`；`nominal_ratio_expression=100KΩ/(510KΩ+100KΩ)`；`vin_minus_reference=GND via R5 0Ω`
- 证据：图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 R3 510KΩ、R4 100KΩ 串联路径及 R5 0Ω 对地连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat ADC v1.1 | `adc=U1 ADS1110`；`analog_input=P2 Header 2`；`input_network=R3 510KΩ; R4 100KΩ; R5 0Ω`；`host_interface=P1 STICKIO SCL/SDA`；`supply=+3.3V` |
| 核心器件 | U1 ADS1110 | `pin_1=VIN+`；`pin_2=GND`；`pin_3=SCL`；`pin_4=SDA`；`pin_5=VDD +3.3V`；`pin_6=VIN-` |
| 接口 | P1 STICKIO | `pin_1=GND`；`pin_2=5VOUT VCC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC` |
| 接口 | P2 Header 2 | `pin_1=via R3 510KΩ to U1.1 VIN+`；`pin_2=U1.6 VIN- and via R5 0Ω to GND`；`direction=analog input` |
| 模拟电路 | VIN+ / VIN- 输入网络 | `series_resistor=R3 510KΩ`；`differential_resistor=R4 100KΩ`；`vin_minus_ground_link=R5 0Ω`；`positive_input=U1.1 VIN+`；`negative_input=U1.6 VIN-` |
| 模拟电路 | R3/R4 输入衰减 | `upper_resistor=R3 510KΩ`；`lower_resistor=R4 100KΩ`；`nominal_ratio_expression=100KΩ/(510KΩ+100KΩ)`；`vin_minus_reference=GND via R5 0Ω` |
| 总线 | I2C SCL/SDA | `scl=U1.3 SCL to P1.3 G26`；`sda=U1.4 SDA to P1.5 G0`；`direction=bidirectional`；`level_shifter=not shown`；`series_resistors=not shown` |
| 总线 | I2C 上拉网络 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`pullup_rail=+3.3V` |
| 总线地址 | ADS1110 I2C 地址 | `documented_address=0x48`；`schematic_address_label=not shown`；`part_marking=ADS1110 only` |
| 电源 | U1 +3.3V 供电 | `supply_input=P1.7 3V3`；`adc_supply=U1.5 VDD +3.3V`；`adc_ground=U1.2 GND`；`decoupling=C1 100nF` |
| 电源 | 板载电源结构 | `adc_rail=+3.3V`；`source=P1.7 3V3`；`ldo=not shown`；`dc_dc=not shown`；`load_switch=not shown`；`charger=not shown` |
| 模拟电路 | P2 输入量程 | `documented_range=DC 0~12V`；`schematic_resistors=R3 510KΩ; R4 100KΩ; R5 0Ω`；`rated_range_label=not shown`；`input_clamp=not shown` |
| 时钟 | U1 时钟 | `external_crystal=not shown`；`external_clock_net=not shown` |
| 保护电路 | P2 模拟输入保护 | `series_network=R3/R4/R5`；`tvs=not shown`；`clamp_diodes=not shown`；`fuse=not shown`；`reverse_protection=not shown` |

## 待确认事项

- `address.i2c-0x48`：产品正文标注 I2C 地址为 0x48，但本地原理图页面未标注 0x48 或器件订货后缀，因此无法仅由该页确认地址。（证据：图 5cf49dc14fe1 / 第 1 页 / 全页 U1 与 I2C 区域：U1 仅标注 ADS1110，未见 0x48 或地址选择/订货后缀）
- `analog.input-range-0-12v`：产品正文声明输入范围为 DC 0~12V；原理图给出 510KΩ/100KΩ/0Ω 输入网络，但未标注额定量程、容差、保护钳位或最大输入电压，无法仅由该页完整确认 0~12V 额定范围。（证据：图 5cf49dc14fe1 / 第 1 页 / B1-B2 区域 P2 至 U1 VIN+/VIN- 的模拟输入网络，未见 0~12V 或额定值标注）
- `review.i2c-address-0x48`：该板所装 ADS1110 的确切订货型号是否固定对应 7 位 I2C 地址 0x48？；原因：产品正文给出 0x48，但原理图仅标注 ADS1110，未给出地址文本、地址选择连接或完整订货后缀。
- `review.input-range-0-12v`：P2 的 DC 0~12V 额定范围是否有器件规格、容差和保护设计资料支持？；原因：原理图可确认 510KΩ/100KΩ/0Ω 网络，但没有标注 0~12V、阻值容差、最大额定值或输入钳位条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5cf49dc14fe1c9d21a0d7745b322b074886e96b425380805d42fbae5cf996edf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/582/StickHat_ADC_v1.1_sch_01.png` |

---

源文档：`zh_CN/hat/HAT-ADC-V11.md`

源文档 SHA-256：`2b940e86bfd5b7c6cd3ed15789a155f505c265251a31e6edb13d09cd59f46efe`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
