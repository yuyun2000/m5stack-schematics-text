# Unit ADC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ADC |
| SKU | U013 |
| 产品 ID | `unit-adc-9b141c912f2a` |
| 源文档 | `zh_CN/unit/adc.md` |

## 概述

Unit ADC 以 ADS1100（U2）作为差分模数转换器，P1 两针输入通过 R4/R5 分压网络和 LM358DR2G（U1A）电压跟随器连接 VIN+/VIN-。J1 四针接口引出 IIC_SCL、IIC_SDA、VCC 和 GND，SCL/SDA 由 R2/R3 上拉到 +3.3V。HT7533（U3）把 VCC 转换为 +3.3V，供 ADS1100 与 I2C 上拉使用；原理图没有标注 VCC 额定值、I2C 地址或 P1 允许输入范围。

## 检索关键词

`Unit ADC`、`U013`、`ADS1100`、`LM358DR2G`、`HT7533`、`IIC_Socket_4P`、`Header 2`、`I2C`、`0x48`、`IIC_SCL`、`IIC_SDA`、`VIN+`、`VIN-`、`VCC`、`+3.3V`、`R1 1KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 300KΩ`、`R5 100KΩ`、`R6 0Ω`、`C1 100nF`、`C2 100nF`、`C3 10uF`、`C4 10uF`、`V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ADS1100 | 将 VIN+/VIN- 差分模拟输入转换为 I2C 数据 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：U2 ADS1100，pin 1 VIN+、pin 6 VIN-、pin 5 VDD、pin 2 GND、pin 3 SCL、pin 4 SDA |
| U1A | LM358DR2G | 以输出回接反相端的电压跟随器缓冲 R4/R5 分压节点 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-B2：U1A LM358DR2G，pin 1 输出回接 pin 2，pin 3 接 R4/R5 节点，pin 8 VCC、pin 4 GND |
| U3 | HT7533 | 将 VCC 稳压为 +3.3V | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 C2-C3：U3 HT7533，VIN pin 2 接 VCC、VOUT pin 3 接 +3.3V、GND pin 1 接地 |
| J1 | IIC_Socket_4P | 外部 I2C 与电源接口 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B3：J1 IIC_Socket_4P，1~4 脚依次为 IIC_SCL、IIC_SDA、VCC、GND |
| P1 | Header 2 | 两针外部模拟输入连接器 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B1-B2：P1 Header 2，pin 1 经 R4 进入分压/缓冲路径，pin 2 接 VIN- 与 R6 |
| R4/R5 | 300KΩ / 100KΩ | P1 pin 1 到 P1 pin 2/VIN- 之间的模拟输入分压网络 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B1-B2：P1 pin 1-R4 300KΩ-缓冲节点-R5 100KΩ-P1 pin 2/VIN- |
| R1 | 1KΩ | U1A 输出到 ADS1100 VIN+ 的串联电阻 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2：U1A pin 1 输出经 R1 1KΩ 接 U2 VIN+ pin 1 |
| R6 | 0Ω | 将 P1 pin 2 与 ADS1100 VIN- 网络连接到 GND | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2：VIN-/P1 pin 2 节点经 R6 0Ω 接 GND |
| R2/R3 | 4.7KΩ | IIC_SCL 与 IIC_SDA 到 +3.3V 的上拉电阻 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：R2/R3 各 4.7KΩ，上端接 +3.3V，下端分别接 IIC_SCL/IIC_SDA |
| C1 | 100nF | ADS1100 +3.3V 电源去耦电容 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2：U2 VDD pin 5 的 +3.3V 节点经 C1 100nF 接 GND |
| C2/C3/C4 | 100nF / 10uF / 10uF | HT7533 输出和输入滤波电容 | 图 41b676c7fb81 / 第 1 页 / 页 1 网格 C1-C2：C2 100nF 与 C3 10uF 跨 +3.3V/GND，C4 10uF 跨 VCC/GND |

## 系统结构

### Unit ADC

P1 的模拟输入经 R4/R5 分压和 U1A LM358DR2G 电压跟随器缓冲后进入 U2 ADS1100 VIN+，VIN- 连接 P1 pin 2 并经 R6 接地；ADS1100 通过 J1 的 IIC_SCL/IIC_SDA 对外通信。

- 参数与网络：`input_connector=P1 Header 2`；`divider=R4 300KΩ,R5 100KΩ`；`buffer=U1A LM358DR2G`；`adc=U2 ADS1100`；`digital_interface=J1 IIC_SCL,IIC_SDA`；`regulator=U3 HT7533`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-C3：P1/R4/R5/U1A/R1/U2/J1 及 U3 电源路径

## 核心器件

### U2 ADS1100

U2 pin 1 为 VIN+，pin 6 为 VIN-，pin 5 VDD 接 +3.3V，pin 2 GND 接地，pin 3 SCL 接 IIC_SCL，pin 4 SDA 接 IIC_SDA。

- 参数与网络：`pin_1=VIN+`；`pin_2=GND`；`pin_3=SCL,IIC_SCL`；`pin_4=SDA,IIC_SDA`；`pin_5=VDD,+3.3V`；`pin_6=VIN-`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：U2 ADS1100 六个引脚号、功能名和外部网络

## 电源

### IIC_SCL/IIC_SDA 上拉

R2 和 R3 均为 4.7KΩ，分别将 IIC_SCL 与 IIC_SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=+3.3V`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：+3.3V-R2-IIC_SCL 与 +3.3V-R3-IIC_SDA 支路

### U3 HT7533

U3 VIN pin 2 接 VCC，VOUT pin 3 输出 +3.3V，GND pin 1 接地；C4 10uF 位于 VCC 输入侧，C2 100nF 与 C3 10uF 位于 +3.3V 输出侧。

- 参数与网络：`input_pin=pin 2 VIN`；`input_rail=VCC`；`output_pin=pin 3 VOUT`；`output_rail=+3.3V`；`ground_pin=pin 1 GND`；`input_capacitor=C4 10uF`；`output_capacitors=C2 100nF,C3 10uF`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 C1-C2：U3 HT7533、C2/C3/C4 与 VCC/+3.3V/GND

### U1A/U2 供电

U1A LM358DR2G 的 pin 8 接 VCC、pin 4 接 GND；U2 ADS1100 的 VDD pin 5 接 +3.3V、GND pin 2 接地，并由 C1 100nF 去耦。

- 参数与网络：`opamp_supply=U1A pin 8 VCC`；`opamp_ground=U1A pin 4 GND`；`adc_supply=U2 pin 5 +3.3V`；`adc_ground=U2 pin 2 GND`；`adc_decoupling=C1 100nF`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-B3：U1A pin 8/4 与 U2 pin 5/2/C1 的电源网络

## 接口

### P1 Header 2

P1 pin 1 经 R4 300KΩ进入分压与缓冲节点，P1 pin 2 直接连接 ADS1100 VIN- pin 6，并经 R6 0Ω接 GND。

- 参数与网络：`pin_1=analog input via R4 300KΩ`；`pin_2=VIN- node; U2 pin 6; R6 0Ω to GND`；`connector=Header 2`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B1-B2：P1 pins 1/2、R4/R5/R6 与 U2 VIN- pin 6

### J1 IIC_Socket_4P

J1 pin 1 接 IIC_SCL，pin 2 接 IIC_SDA，pin 3 接 VCC，pin 4 接 GND。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B3：J1 1~4 脚与 IIC_SCL/IIC_SDA/VCC/GND 标签

## 总线

### ADS1100 I2C

U2 SCL pin 3 通过 IIC_SCL 连接 J1 pin 1，U2 SDA pin 4 通过 IIC_SDA 连接 J1 pin 2；两条线均上拉至 +3.3V。

- 参数与网络：`device=U2 ADS1100`；`scl=U2 pin 3 to J1 pin 1 IIC_SCL`；`sda=U2 pin 4 to J1 pin 2 IIC_SDA`；`pullup_rail=+3.3V`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：U2 SCL/SDA、R2/R3 与 J1 同名网络

## 时钟

### ADC/运放时钟

本页原理图未绘出外部晶振、谐振器或时钟连接，ADS1100 仅显示 VIN+/VIN-/SCL/SDA/VDD/GND 六个引脚。

- 参数与网络：`external_clock_component=null`；`clock_net=null`；`adc_clock_pin_shown=false`
- 证据：图 41b676c7fb81 / 第 1 页 / 整页及页 1 网格 B2 的 U2 六引脚符号：无晶振位号或时钟网络

## 关键网络

### Unit ADC 关键网络

关键网络为 P1 pin 1→R4/R5→U1A pin 3，U1A pin 1→R1→U2 VIN+，P1 pin 2→U2 VIN-/R6→GND，U2 SCL/SDA→IIC_SCL/IIC_SDA→J1，以及 VCC→U3→+3.3V。

- 参数与网络：`analog_high_path=P1.1-R4-U1A.3; R5 to P1.2`；`buffered_path=U1A.1-R1-U2.VIN+`；`analog_reference=P1.2-U2.VIN--R6-GND`；`digital_path=U2.SCL/SDA-J1.1/J1.2`；`power_path=J1.3 VCC-U3-+3.3V`
- 证据：图 41b676c7fb81 / 第 1 页 / 整页：P1/R4/R5/U1A/R1/U2/J1/U3 之间的直接连线和同名网络

## 模拟电路

### R4/R5 分压网络

R4 300KΩ 从 P1 pin 1 接到 U1A 非反相输入节点，R5 100KΩ 从该节点接到 P1 pin 2/VIN- 节点。

- 参数与网络：`upper_resistor=R4 300KΩ`；`lower_resistor=R5 100KΩ`；`source=P1 pin 1`；`sense_node=U1A pin 3`；`reference_node=P1 pin 2,U2 VIN- pin 6`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B1-B2：R4/R5 串联拓扑及 U1A pin 3 分支

### U1A LM358DR2G

U1A pin 1 输出直接回接 pin 2 反相端，pin 3 非反相端接 R4/R5 节点，形成电压跟随连接；输出再经 R1 1KΩ进入 ADS1100 VIN+ pin 1。

- 参数与网络：`non_inverting_input=pin 3 to R4/R5 node`；`inverting_input=pin 2 tied to output`；`output=pin 1 via R1 1KΩ to U2 VIN+`；`supply=pin 8 VCC,pin 4 GND`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-B2：U1A pins 1/2/3/4/8、反馈线和 R1

### ADS1100 VIN+/VIN-

VIN+ 由 U1A 输出经 R1 1KΩ驱动，VIN- 连接 P1 pin 2 并通过 R6 0Ω接 GND；C1 不在模拟输入上，而是接在 U2 VDD 电源节点。

- 参数与网络：`vin_plus=U1A pin 1 via R1 1KΩ to U2 pin 1`；`vin_minus=P1 pin 2 to U2 pin 6`；`vin_minus_ground=R6 0Ω to GND`；`adc_decoupling=C1 100nF on VDD`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2：R1/U2 VIN+、P1 pin 2/U2 VIN-/R6 与 C1/VDD

## 其他事实

### UNIT_ADC 原理图版本

图框标注 Project Title 为 UNIT_ADC.PrjPCB、Sheet Title 为 UNIT_ADC.SchDoc、Revised 为 V1.0、日期为 07/19/2018，Sheet 1 of 1。

- 参数与网络：`project_title=UNIT_ADC.PrjPCB`；`sheet_title=UNIT_ADC.SchDoc`；`revision=V1.0`；`date=07/19/2018`；`sheet=1 of 1`
- 证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 D3-D4：右下角图框中的 Project Title、Sheet Title、Revised、Date、Sheet 字段

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ADC | `input_connector=P1 Header 2`；`divider=R4 300KΩ,R5 100KΩ`；`buffer=U1A LM358DR2G`；`adc=U2 ADS1100`；`digital_interface=J1 IIC_SCL,IIC_SDA`；`regulator=U3 HT7533` |
| 接口 | P1 Header 2 | `pin_1=analog input via R4 300KΩ`；`pin_2=VIN- node; U2 pin 6; R6 0Ω to GND`；`connector=Header 2` |
| 模拟电路 | R4/R5 分压网络 | `upper_resistor=R4 300KΩ`；`lower_resistor=R5 100KΩ`；`source=P1 pin 1`；`sense_node=U1A pin 3`；`reference_node=P1 pin 2,U2 VIN- pin 6` |
| 模拟电路 | U1A LM358DR2G | `non_inverting_input=pin 3 to R4/R5 node`；`inverting_input=pin 2 tied to output`；`output=pin 1 via R1 1KΩ to U2 VIN+`；`supply=pin 8 VCC,pin 4 GND` |
| 核心器件 | U2 ADS1100 | `pin_1=VIN+`；`pin_2=GND`；`pin_3=SCL,IIC_SCL`；`pin_4=SDA,IIC_SDA`；`pin_5=VDD,+3.3V`；`pin_6=VIN-` |
| 模拟电路 | ADS1100 VIN+/VIN- | `vin_plus=U1A pin 1 via R1 1KΩ to U2 pin 1`；`vin_minus=P1 pin 2 to U2 pin 6`；`vin_minus_ground=R6 0Ω to GND`；`adc_decoupling=C1 100nF on VDD` |
| 接口 | J1 IIC_Socket_4P | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | ADS1100 I2C | `device=U2 ADS1100`；`scl=U2 pin 3 to J1 pin 1 IIC_SCL`；`sda=U2 pin 4 to J1 pin 2 IIC_SDA`；`pullup_rail=+3.3V` |
| 电源 | IIC_SCL/IIC_SDA 上拉 | `scl_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=+3.3V` |
| 总线地址 | Unit ADC I2C 地址 | `device=U2 ADS1100`；`schematic_address=null`；`address_selection=null`；`address_source_needed=part ordering code or protocol documentation` |
| 电源 | U3 HT7533 | `input_pin=pin 2 VIN`；`input_rail=VCC`；`output_pin=pin 3 VOUT`；`output_rail=+3.3V`；`ground_pin=pin 1 GND`；`input_capacitor=C4 10uF`；`output_capacitors=C2 100nF,C3 10uF` |
| 电源 | U1A/U2 供电 | `opamp_supply=U1A pin 8 VCC`；`opamp_ground=U1A pin 4 GND`；`adc_supply=U2 pin 5 +3.3V`；`adc_ground=U2 pin 2 GND`；`adc_decoupling=C1 100nF` |
| 电源 | J1 VCC 额定值 | `connector_pin=J1 pin 3`；`net=VCC`；`loads=U3 VIN,U1A pin 8`；`schematic_voltage=null`；`generated_rail=+3.3V` |
| 模拟电路 | P1 允许输入范围 | `connector=P1 Header 2`；`divider=R4 300KΩ,R5 100KΩ`；`buffer=U1A LM358DR2G`；`adc=U2 ADS1100`；`schematic_input_range=null` |
| 时钟 | ADC/运放时钟 | `external_clock_component=null`；`clock_net=null`；`adc_clock_pin_shown=false` |
| 关键网络 | Unit ADC 关键网络 | `analog_high_path=P1.1-R4-U1A.3; R5 to P1.2`；`buffered_path=U1A.1-R1-U2.VIN+`；`analog_reference=P1.2-U2.VIN--R6-GND`；`digital_path=U2.SCL/SDA-J1.1/J1.2`；`power_path=J1.3 VCC-U3-+3.3V` |
| 其他事实 | UNIT_ADC 原理图版本 | `project_title=UNIT_ADC.PrjPCB`；`sheet_title=UNIT_ADC.SchDoc`；`revision=V1.0`；`date=07/19/2018`；`sheet=1 of 1` |

## 待确认事项

- `address.i2c-not-shown`：原理图显示 ADS1100 的 SCL/SDA 连接，但页面未印出 I2C 地址或地址选择网络，无法仅凭该原理图确认地址值。（证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 B2-B3：U2/J1 IIC_SCL/IIC_SDA 区域，页面无 0x 地址或 ADDR 引脚）
- `power.vcc-rating-not-shown`：J1 pin 3 与 U3 VIN、U1A 电源使用名为 VCC 的网络，但原理图没有为 VCC 标出数值，无法仅凭该页确认接口额定供电电压。（证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-C3：J1 pin 3、U1A pin 8 与 U3 VIN 上的 VCC 网络，未见电压数值）
- `analog.input-range-not-shown`：原理图给出 R4/R5 分压值和 U1A/ADS1100 连接，但没有标出 P1 的允许输入电压范围、极性限制或绝对最大值。（证据：图 41b676c7fb81 / 第 1 页 / 页 1 网格 A2-B2：P1/R4/R5/U1A/U2 模拟链，页面无输入量程或极性文字）
- `review.i2c-address`：本产品所装 ADS1100 的 I2C 地址是否为 0x48？；原因：原理图器件只标 ADS1100，未给出完整订货后缀、地址值或地址选择网络，需要 BOM、器件标记或协议资料确认。
- `review.vcc-rating`：J1 pin 3 的 VCC 额定输入电压是多少？；原因：原理图只标 VCC，并显示其进入 HT7533 和 LM358DR2G，没有打印电压数值。
- `review.input-range`：P1 两针端子的额定输入范围、允许极性和过压边界是什么？；原因：R4/R5 分压拓扑可见，但整机输入额定值取决于 LM358DR2G、ADS1100、电源 VCC 和器件耐压，原理图未直接给出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `41b676c7fb810dd2ad4d9420e7f3601763c9b8e3b4134c65b2f597928a87efd8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/736/U013_UNIT_ADC_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/adc.md`

源文档 SHA-256：`c602b4da7778ab3db83616bc674c0205b2df67cf1523f8afa77e744e60ffd1ca`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
