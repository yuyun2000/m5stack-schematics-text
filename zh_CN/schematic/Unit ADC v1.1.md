# Unit ADC v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ADC v1.1 |
| SKU | U013-V11 |
| 产品 ID | `unit-adc-v1-1-4f4844dbea51` |
| 源文档 | `zh_CN/unit/Unit-ADC_V1.1.md` |

## 概述

Unit ADC v1.1 以 U2 ADS1110 将单端接地参考的模拟输入转换为 I2C 数据：P1 pin1 经 R4 510KΩ/R5 100KΩ 分压后，由 U1A LM358DR2G 电压跟随器缓冲，再经 R1 1KΩ送入 VIN+，VIN−与 P1 pin2 经 R6 0Ω接地。J1 提供 IIC_SCL、IIC_SDA、VCC、GND，U3/U4 两颗 HT7533 分别从 VCC 生成 ADC/模拟侧 +3.3V 与 I2C 上拉侧 D3.3V。原理图未印 VCC 电压、I2C 地址、量程、分辨率、PGA、采样率或基准参数，且产品正文对 ADS1110/ADS1100、采样率和基准描述存在冲突。

## 检索关键词

`Unit ADC v1.1`、`U013-V11`、`ADS1110`、`ADS1100`、`LM358DR2G`、`HT7533`、`IIC_Socket_4P`、`Header 2`、`I2C`、`0x48`、`IIC_SCL`、`IIC_SDA`、`VIN+`、`VIN-`、`VCC`、`+3.3V`、`D3.3V`、`R1 1KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 510KΩ`、`R5 100KΩ`、`R6 0Ω`、`C1 100nF`、`PGA`、`16-bit ADC`、`0-12V`、`2.048V reference`、`8 SPS`、`16 SPS`、`32 SPS`、`128 SPS`、`15 SPS`、`30 SPS`、`60 SPS`、`240 SPS`、`analog divider`、`voltage follower`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ADS1110 | 将 VIN+/VIN− 模拟输入转换为 I2C 数据的六脚 ADC | 图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，U2 ADS1110 pins1-6 |
| U1A | LM358DR2G | 以输出回接反相输入的电压跟随器，缓冲 R4/R5 分压节点 | 图 76f91ae9053e / 第 1 页 / 第1页网格 A2-B2，U1A LM358DR2G pins1/2/3/4/8 与反馈线 |
| U3 | HT7533 | 将 VCC 稳压为模拟/ADC 电源 +3.3V | 图 76f91ae9053e / 第 1 页 / 第1页网格 C2，U3 HT7533、VIN VCC、VOUT +3.3V |
| U4 | HT7533 | 将 VCC 稳压为 I2C 上拉电源 D3.3V | 图 76f91ae9053e / 第 1 页 / 第1页网格 C2-C3，U4 HT7533、VIN VCC、VOUT D3.3V |
| J1 | IIC_Socket_4P | 外部 I2C 与 VCC/GND 四针接口 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B3，J1 IIC_Socket_4P pins1-4 |
| P1 | Header 2 | 两针外部模拟输入端子 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B1-B2，P1 Header 2 pins1/2 |
| R4/R5 | 510KΩ / 100KΩ | P1 pin1 到接地参考 P1 pin2 之间的模拟输入分压网络 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B1-B2，P1.1-R4 510KΩ-采样节点-R5 100KΩ-P1.2 |
| R1/R6 | 1KΩ / 0Ω | R1 串联缓冲输出到 VIN+；R6 将 VIN−/P1 pin2 接地 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B2，U1A 输出/R1/U2 VIN+ 与 VIN−/R6/GND |
| R2/R3 | 4.7KΩ / 4.7KΩ | IIC_SCL/IIC_SDA 到 D3.3V 的上拉电阻 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，R2/R3 4.7KΩ、D3.3V、IIC_SCL/IIC_SDA |
| C1 | 100nF | U2 VDD +3.3V 的本地去耦电容 | 图 76f91ae9053e / 第 1 页 / 第1页网格 B2，U2 VDD pin5、C1 100nF、GND |
| C2/C3/C4/C5 | 100nF / 10uF / 10uF / 10uF | 双 HT7533 的输入 VCC 和两个 3.3V 输出域滤波电容 | 图 76f91ae9053e / 第 1 页 / 第1页网格 C1-C3，U3/U4 周围 C2-C5 |

## 系统结构

### Unit ADC v1.1 信号链

P1 模拟输入经 R4/R5 分压、U1A 电压跟随缓冲和 R1 串联后进入 U2 ADS1110 VIN+，VIN−接地；U2 通过 J1 I2C 通信，U3/U4 从 VCC 分别生成 +3.3V 与 D3.3V。

- 参数与网络：`input=P1 Header 2`；`divider=R4 510KΩ; R5 100KΩ`；`buffer=U1A LM358DR2G`；`adc=U2 ADS1110`；`host=J1 IIC_Socket_4P`；`analog_regulator=U3 HT7533`；`digital_regulator=U4 HT7533`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页完整单页 P1/U1A/U2/J1/U3/U4

### 未显示的系统分区

该页未显示 MCU、协处理器、外部存储器、电池、充电器、复位、调试、射频、音频或传感器；ADS1110 由外部 I2C 主机直接访问。

- 参数与网络：`mcu=not shown`；`storage=not shown`；`battery=not shown`；`reset=not shown`；`debug=not shown`；`rf=not shown`；`audio=not shown`；`sensor=not shown`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页完整单页功能与器件分区

## 核心器件

### U2 ADS1110 针脚

U2 pin1 为 VIN+、pin6 VIN−、pin5 VDD/+3.3V、pin2 GND、pin3 SCL/IIC_SCL、pin4 SDA/IIC_SDA。

- 参数与网络：`pin1=VIN+`；`pin2=GND`；`pin3=SCL / IIC_SCL`；`pin4=SDA / IIC_SDA`；`pin5=VDD / +3.3V`；`pin6=VIN-`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，U2 ADS1110 六个引脚号/名称/网络

## 电源

### I2C 上拉

R2/R3 均为 4.7KΩ，分别将 IIC_SCL 与 IIC_SDA 上拉到 D3.3V。

- 参数与网络：`scl_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=D3.3V`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，D3.3V/R2/R3/IIC_SCL/IIC_SDA

### U3 模拟 +3.3V

U3 HT7533 VIN pin2 接 VCC、VOUT pin3 输出 +3.3V、GND pin1 接地；输入 C4 10uF，输出 C2 100nF/C3 10uF。

- 参数与网络：`regulator=U3 HT7533`；`input=VCC / pin2`；`output=+3.3V / pin3`；`ground=pin1`；`input_cap=C4 10uF`；`output_caps=C2 100nF; C3 10uF`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 C1-C2，U3/C2/C3/C4/VCC/+3.3V

### U4 数字 D3.3V

U4 HT7533 VIN pin2 接 VCC、VOUT pin3 输出 D3.3V、GND pin1 接地；与 U3 共用 VCC 输入侧 C4 10uF，输出配置 C5 10uF。

- 参数与网络：`regulator=U4 HT7533`；`input=VCC / pin2`；`output=D3.3V / pin3`；`ground=pin1`；`shared_input_cap=C4 10uF`；`output_cap=C5 10uF`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 C2-C3，U4/C4/C5/VCC/D3.3V

### +3.3V 与 D3.3V 电源域

U3 与 U4 均从同一 VCC 输入，但输出使用不同网络名：+3.3V 供 U2 VDD 与相关模拟电路，D3.3V 只在图中供 R2/R3 I2C 上拉。

- 参数与网络：`common_input=VCC`；`analog_rail=+3.3V from U3`；`analog_loads=U2 VDD; C1; U3 output capacitors`；`digital_rail=D3.3V from U4`；`digital_loads=R2/R3 I2C pullups`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2-C3，U3 +3.3V、U4 D3.3V 与对应负载

### 运放与 ADC 供电

U1A LM358DR2G pin8 直接接 VCC、pin4 接 GND；U2 VDD pin5 接 +3.3V、GND pin2 接地，并由 C1 100nF 去耦。

- 参数与网络：`opamp_supply=U1A pin8 VCC`；`opamp_ground=U1A pin4 GND`；`adc_supply=U2 pin5 +3.3V`；`adc_ground=U2 pin2 GND`；`adc_decoupling=C1 100nF`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 A2-B3，U1A pin8/4 与 U2 pin5/2/C1

## 接口

### P1 模拟输入针脚

P1 pin1 经 R4 510KΩ进入分压节点，P1 pin2 连接 R5 下端、U2 VIN− pin6，并经 R6 0Ω接 GND。

- 参数与网络：`connector=P1 Header 2`；`pin1=analog high via R4 510KΩ`；`pin2=analog reference / U2 VIN- / R6 0Ω to GND`；`polarity=pin1 relative to grounded pin2`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B1-B2，P1/R4/R5/R6/U2 VIN−

### J1 四针接口

J1 IIC_Socket_4P pin1 接 IIC_SCL，pin2 接 IIC_SDA，pin3 接 VCC，pin4 接 GND。

- 参数与网络：`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`connector=IIC_Socket_4P`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B3，J1 pins1-4 与网络名

## 总线

### ADS1110 I2C 路由

U2 SCL pin3 通过 IIC_SCL 连接 J1 pin1，SDA pin4 通过 IIC_SDA 连接 J1 pin2；R2/R3 分别将两线拉到 D3.3V。

- 参数与网络：`controller=external host via J1`；`device=U2 ADS1110`；`scl=U2 pin3 -> J1 pin1`；`sda=U2 pin4 -> J1 pin2`；`pullup_rail=D3.3V`；`direction=SCL host output; SDA bidirectional`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，U2 SCL/SDA、R2/R3 与 J1

## 时钟

### 外部时钟

本页未显示晶振、振荡器或外部时钟网络，U2 符号只有 VIN+/VIN−、VDD/GND 与 SCL/SDA。

- 参数与网络：`crystal=not shown`；`oscillator=not shown`；`clock_net=not shown`；`adc_clock_pin=not shown`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页完整单页及 U2 六脚符号

## 保护电路

### 模拟与 I2C 接口保护

P1 模拟输入和 J1 I2C/VCC 路径未显示 TVS、ESD 二极管、保险丝或专用过压钳位；模拟输入仅有高阻分压、缓冲及接地电阻。

- 参数与网络：`analog_tvs=not shown`；`i2c_esd=not shown`；`power_fuse=not shown`；`clamp=not shown`；`visible_input_network=R4/R5/U1A/R1/R6`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页 P1 至 U2 及 J1 至 U2/U3/U4 全部路径

## 关键网络

### 关键网络索引

模拟路径为 P1.1→R4→R4/R5节点→U1A.3→U1A.1→R1→U2 VIN+；参考路径为 P1.2→U2 VIN−→R6→GND；数字路径为 U2 SCL/SDA→J1；电源为 VCC→U3/U4→+3.3V/D3.3V。

- 参数与网络：`analog=P1.1-R4-node-U1A.3/U1A.1-R1-U2.VIN+`；`reference=P1.2-U2.VIN--R6-GND`；`i2c=U2.SCL/SDA-J1.1/J1.2`；`power=J1.3 VCC-U3/U4-+3.3V/D3.3V`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页整页直接连线与同名网络

## 模拟电路

### R4/R5 分压器

R4 510KΩ 从 P1 pin1 接到 U1A pin3 采样节点，R5 100KΩ 从该节点接到 P1 pin2/VIN−；标称分压比为 100K/(510K+100K)。

- 参数与网络：`upper=R4 510KΩ`；`lower=R5 100KΩ`；`source=P1 pin1`；`sense=U1A pin3`；`reference=P1 pin2 / VIN- / GND`；`nominal_ratio=100/610 ≈ 0.1639`；`attenuation=≈6.1:1`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B1-B2，R4/R5 串联值与 U1A pin3 分支

### U1A LM358DR2G 缓冲

U1A pin1 输出直接反馈到 pin2 反相输入，pin3 非反相输入接分压节点，构成电压跟随连接；pin1 再经 R1 1KΩ驱动 U2 VIN+。

- 参数与网络：`non_inverting=pin3 / R4-R5 node`；`inverting=pin2 / tied to output`；`output=pin1 -> R1 1KΩ -> U2 VIN+`；`supply=pin8 VCC`；`ground=pin4 GND`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 A2-B2，U1A 反馈与 R1/U2 VIN+

### ADS1110 VIN+/VIN−连接

U2 VIN+ pin1 由 U1A 输出经 R1 1KΩ驱动；VIN− pin6 与 P1 pin2 共网并经 R6 0Ω接地，因此板级模拟测量以 GND 为参考。

- 参数与网络：`vin_plus=U1A pin1 -> R1 1KΩ -> U2 pin1`；`vin_minus=U2 pin6 -> P1 pin2`；`ground_link=R6 0Ω`；`measurement=single-ended board connection using differential ADC pins`
- 证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2，R1/U2 VIN+ 与 U2 VIN−/R6/GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ADC v1.1 信号链 | `input=P1 Header 2`；`divider=R4 510KΩ; R5 100KΩ`；`buffer=U1A LM358DR2G`；`adc=U2 ADS1110`；`host=J1 IIC_Socket_4P`；`analog_regulator=U3 HT7533`；`digital_regulator=U4 HT7533` |
| 核心器件 | U2 ADS1110 针脚 | `pin1=VIN+`；`pin2=GND`；`pin3=SCL / IIC_SCL`；`pin4=SDA / IIC_SDA`；`pin5=VDD / +3.3V`；`pin6=VIN-` |
| 接口 | P1 模拟输入针脚 | `connector=P1 Header 2`；`pin1=analog high via R4 510KΩ`；`pin2=analog reference / U2 VIN- / R6 0Ω to GND`；`polarity=pin1 relative to grounded pin2` |
| 模拟电路 | R4/R5 分压器 | `upper=R4 510KΩ`；`lower=R5 100KΩ`；`source=P1 pin1`；`sense=U1A pin3`；`reference=P1 pin2 / VIN- / GND`；`nominal_ratio=100/610 ≈ 0.1639`；`attenuation=≈6.1:1` |
| 模拟电路 | U1A LM358DR2G 缓冲 | `non_inverting=pin3 / R4-R5 node`；`inverting=pin2 / tied to output`；`output=pin1 -> R1 1KΩ -> U2 VIN+`；`supply=pin8 VCC`；`ground=pin4 GND` |
| 模拟电路 | ADS1110 VIN+/VIN−连接 | `vin_plus=U1A pin1 -> R1 1KΩ -> U2 pin1`；`vin_minus=U2 pin6 -> P1 pin2`；`ground_link=R6 0Ω`；`measurement=single-ended board connection using differential ADC pins` |
| 接口 | J1 四针接口 | `pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`connector=IIC_Socket_4P` |
| 总线 | ADS1110 I2C 路由 | `controller=external host via J1`；`device=U2 ADS1110`；`scl=U2 pin3 -> J1 pin1`；`sda=U2 pin4 -> J1 pin2`；`pullup_rail=D3.3V`；`direction=SCL host output; SDA bidirectional` |
| 电源 | I2C 上拉 | `scl_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=D3.3V` |
| 电源 | U3 模拟 +3.3V | `regulator=U3 HT7533`；`input=VCC / pin2`；`output=+3.3V / pin3`；`ground=pin1`；`input_cap=C4 10uF`；`output_caps=C2 100nF; C3 10uF` |
| 电源 | U4 数字 D3.3V | `regulator=U4 HT7533`；`input=VCC / pin2`；`output=D3.3V / pin3`；`ground=pin1`；`shared_input_cap=C4 10uF`；`output_cap=C5 10uF` |
| 电源 | +3.3V 与 D3.3V 电源域 | `common_input=VCC`；`analog_rail=+3.3V from U3`；`analog_loads=U2 VDD; C1; U3 output capacitors`；`digital_rail=D3.3V from U4`；`digital_loads=R2/R3 I2C pullups` |
| 电源 | 运放与 ADC 供电 | `opamp_supply=U1A pin8 VCC`；`opamp_ground=U1A pin4 GND`；`adc_supply=U2 pin5 +3.3V`；`adc_ground=U2 pin2 GND`；`adc_decoupling=C1 100nF` |
| 关键网络 | 关键网络索引 | `analog=P1.1-R4-node-U1A.3/U1A.1-R1-U2.VIN+`；`reference=P1.2-U2.VIN--R6-GND`；`i2c=U2.SCL/SDA-J1.1/J1.2`；`power=J1.3 VCC-U3/U4-+3.3V/D3.3V` |
| 保护电路 | 模拟与 I2C 接口保护 | `analog_tvs=not shown`；`i2c_esd=not shown`；`power_fuse=not shown`；`clamp=not shown`；`visible_input_network=R4/R5/U1A/R1/R6` |
| 时钟 | 外部时钟 | `crystal=not shown`；`oscillator=not shown`；`clock_net=not shown`；`adc_clock_pin=not shown` |
| 系统结构 | 未显示的系统分区 | `mcu=not shown`；`storage=not shown`；`battery=not shown`；`reset=not shown`；`debug=not shown`；`rf=not shown`；`audio=not shown`；`sensor=not shown` |
| 总线地址 | ADS1110 I2C 地址 | `document_address=0x48`；`schematic_address=null`；`part_marking=ADS1110`；`address_pin=not shown`；`ordering_suffix=not shown` |
| 电源 | J1 VCC 额定值 | `document_voltage=5V`；`schematic_net=VCC`；`connector=J1 pin3`；`loads=U1A pin8; U3 VIN; U4 VIN`；`tolerance=not shown` |
| 模拟电路 | P1 输入范围 | `document_range=DC 0-12V`；`divider=510KΩ/100KΩ`；`nominal_ratio=0.1639`；`schematic_rating=not shown`；`reverse_limit=not shown`；`overvoltage_protection=not shown` |
| 核心器件 | ADS1110/ADS1100 型号一致性 | `schematic=ADS1110`；`document_description=ADS1110`；`document_comparison=ADS1100`；`example_library=M5-ADS1100`；`bom=not shown` |
| 模拟电路 | 分辨率、PGA 与采样率 | `document_resolution=16-bit`；`document_pga=1;2;4;8`；`document_rates_table=8;16;32;128 SPS`；`document_rates_description=15;30;60;240 SPS`；`schematic_performance=not shown` |
| 模拟电路 | ADC 基准电压 | `document_internal_reference=2.048V`；`document_table_reference=VDD`；`schematic_vdd=+3.3V`；`external_reference=not shown`；`reference_pin=not shown` |
| 模拟电路 | 噪声、INL、漂移与基准精度 | `document_noise=10uVp-p`；`document_drift=5ppm/°C`；`document_inl=0.01% FS max`；`document_reference_accuracy=2.048V ±0.05%`；`resistor_tolerance=not shown`；`test_conditions=not shown` |
| 其他事实 | 整机工作温度 | `document_temperature=0-40°C`；`schematic_temperature=not shown`；`component_grade=not shown` |

## 待确认事项

- `address.i2c-0x48`：产品正文给出 0x48，但原理图只标 ADS1110，未打印地址、完整订货后缀或地址选择网络。（证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2-B3，U2/J1 I2C 区域无地址文字）
- `power.vcc-rating`：产品管脚表称 J1 供电为 5V，但原理图仅将 J1 pin3 标为 VCC，并连接 U1A 与 U3/U4 VIN，没有打印电压数值或容差。（证据：图 76f91ae9053e / 第 1 页 / 第1页 J1 pin3/U1A pin8/U3/U4 VIN 的 VCC 网络）
- `analog.input-range`：产品正文称 DC 0-12V；图纸给出 510KΩ/100KΩ 分压与 VCC 供电 LM358 缓冲，但未标 P1 额定范围、过压边界、输入阻抗公差或反向电压能力。（证据：图 76f91ae9053e / 第 1 页 / 第1页 P1/R4/R5/U1A/U2 模拟链，无量程文字）
- `component.ads-model-naming`：原理图 U2 与正文描述/数据手册链接写 ADS1110，但正文产品对比表和示例库名称写 ADS1100；当前页面不能解释二者是否为文档笔误、兼容型号或装配变体。（证据：图 76f91ae9053e / 第 1 页 / 第1页网格 B2，U2 型号字段 ADS1110）
- `analog.adc-performance`：产品正文列 16-bit、PGA 1/2/4/8，并在不同段落同时出现 8/16/32/128 SPS 与 15/30/60/240 SPS；原理图只标 ADS1110，没有性能或配置寄存器信息。（证据：图 76f91ae9053e / 第 1 页 / 第1页 U2 ADS1110 符号，无分辨率/PGA/SPS 标注）
- `analog.reference-source`：正文一处称内部 2.048V 基准，规格表又称 VDD 基准；原理图只显示 U2 VDD 接 +3.3V，没有 REF 引脚或外部基准器件，无法从页面判断内部基准实现。（证据：图 76f91ae9053e / 第 1 页 / 第1页 U2 VDD/+3.3V/C1 与六脚符号，无 REF 网络）
- `analog.accuracy-noise-drift`：正文给出 10uVp-p 噪声、5ppm/°C、满量程 0.01% INL 与 2.048V ±0.05%；原理图没有器件等级、测试条件、电阻精度或校准信息。（证据：图 76f91ae9053e / 第 1 页 / 第1页完整模拟链，无精度/噪声/温漂注记）
- `other.operating-temperature`：产品正文给出 0-40°C，原理图未标整机工作温度或 U1/U2/U3/U4 的具体温度等级。（证据：图 76f91ae9053e / 第 1 页 / 第1页完整单页，无温度参数）
- `review.i2c-address`：请用 U013-V11 BOM、实装标记或完整 ADS1110 订货型号确认 7 位 I2C 地址是否固定为 0x48。；原因：原理图未给地址或订货后缀。
- `review.vcc-rating`：请确认 J1 VCC 的额定电压、容差与允许供电范围是否为 Grove 5V。；原因：原理图只标 VCC，未打印电压数值。
- `review.input-range`：请结合 VCC、LM358DR2G 输入/输出范围、ADS1110 满量程及电阻公差确认 P1 的 DC 0-12V 额定范围和过压边界。；原因：分压拓扑可见，但图纸没有系统输入额定或保护限制。
- `review.ads-model-naming`：请用 BOM 与实装丝印确认 v1.1 实际器件为 ADS1110 还是 ADS1100，并修正文档冲突。；原因：原理图/描述与产品对比表/示例库使用不同型号名称。
- `review.adc-performance`：请依据确认后的 ADC 型号、数据手册和驱动配置核对 16-bit、PGA 1/2/4/8 及正确采样率组。；原因：正文同时列出两组不一致采样率，原理图不含性能参数。
- `review.reference-source`：请用确认后的 ADC datasheet 说明转换基准是内部 2.048V、VDD，或其他实现，并修正文档冲突。；原因：图纸无外部 REF，正文内部基准与 VDD 基准描述互相矛盾。
- `review.accuracy-noise-drift`：请按器件等级、增益/采样率和整板校准条件核对噪声、INL、温漂与基准精度。；原因：原理图没有器件等级、电阻精度或测试条件。
- `review.operating-temperature`：请用整机环境测试与 BOM 器件温度等级确认 0-40°C 工作范围。；原因：工作温度未印在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `76f91ae9053e41794bf1f266c0bede6ba7c198846c77d314be6d0131b7f37af5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/576/Sch_UNIT_ADC_v1.1_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-ADC_V1.1.md`

源文档 SHA-256：`61d10c75a0b927ae1b552df1cf4432e7525715fac87278c059c77149ea5aa8ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
