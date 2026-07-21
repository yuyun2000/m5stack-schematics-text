# Unit Earth 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Earth |
| SKU | U019 |
| 产品 ID | `unit-earth-4cde6301f673` |
| 源文档 | `zh_CN/unit/earth.md` |

## 概述

Unit Earth（U019）是一款无本地主控的电阻式探针接口：U2 EARTH_PIN pin1 形成模拟网络 Ain，pin2 接 GND，R1 10KΩ 将 Ain 拉到 +3.3V，C2 100nF 对 Ain 滤波。U1A LM393DR2G 将 Ain 与 R3 10KΩ 电位器产生的阈值比较，输出 Din 并由 R2 10KΩ 拉到 +3.3V；J1 同时引出 Ain、Din、VCC 和 GND。U3 HT7533 将 VCC 转为 +3.3V，原理图未包含 ADC、MCU、数字总线、地址、时钟或复位。正文所列 VCC=5V、含水量/导电性解释、外部 ADC 使用方式及电极耐腐蚀警告未直接印在原理图上。

## 检索关键词

`Unit Earth`、`U019`、`UNIT_EARTH V1.0`、`LM393DR2G`、`HT7533`、`EARTH_PIN`、`AD_Socket_4P`、`Ain`、`Din`、`Analog Output`、`Digital Output`、`R3 RPot 10K`、`R1 10KΩ`、`R2 10KΩ`、`+3.3V`、`VCC`、`GND`、`土壤湿度`、`电阻式探针`、`比较器`、`阈值`、`模拟输出`、`数字输出`、`外部 ADC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1A | LM393DR2G | +3.3V 供电的比较器通道，将 Ain 与电位器阈值比较并输出 Din | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 A2-B2，U1A LM393DR2G，pin2 负输入、pin3 正输入、pin1 输出、pin8 +3.3V、pin4 GND |
| U2 | EARTH_PIN | 双电极土壤探针接口，pin1 接 Ain、pin2 接 GND | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 B1-B2，U2 EARTH_PIN，pin1 IN/Ain、pin2 GND |
| U3 | HT7533 | 将 J1 输入的 VCC 稳压为探针、比较器和阈值网络使用的 +3.3V | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 C1-C2，U3 HT7533，VIN pin2 VCC、VOUT pin3 +3.3V、GND pin1 |
| J1 | AD_Socket_4P | 四针模拟/数字输出接口，引出 Ain、Din、VCC 和 GND | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 B3，J1 AD_Socket_4P，pin1 Ain、pin2 Din、pin3 VCC、pin4 GND |
| R3 | RPot 10K | 跨接 +3.3V/GND 的可调阈值电位器，滑动端连接 U1A 负输入 pin2 | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 A1-B1，R3 RPot 10K 上端 +3.3V、下端 GND、wiper 至 U1A pin2 |
| R1,R2 | 10KΩ | R1 将 Ain 拉到 +3.3V，R2 将比较器输出 Din 拉到 +3.3V | 图 57110761f8d2 / 第 1 页 / 第 1 页网格 A2，R1 10KΩ 位于 +3.3V-Ain；R2 10KΩ 位于 +3.3V-Din |
| C1,C2,C3,C4,C5 | 100nF / 10uF | VCC、+3.3V 与 Ain 网络的电源去耦、储能和模拟滤波 | 图 57110761f8d2 / 第 1 页 / 第 1 页：C1/C2/C3 均 100nF，C4/C5 均 10uF；C2 跨 Ain-GND，其他跨 VCC 或 +3.3V-GND |

## 系统结构

### Unit Earth 系统架构

U2 EARTH_PIN 形成 Ain 模拟探针网络，U1A LM393DR2G 将 Ain 与 R3 可调阈值比较后生成 Din，J1 将 Ain/Din 直接交给外部主机。U3 HT7533 从 VCC 生成 +3.3V。完整单页没有 MCU、协处理器、板载 ADC、存储器、数字总线、地址逻辑、晶振、复位、射频、音频、电池或充电电路。

- 参数与网络：`probe=U2 EARTH_PIN`；`analog_output=Ain`；`comparator=U1A LM393DR2G`；`threshold=R3 RPot 10K`；`digital_output=Din`；`host_connector=J1 AD_Socket_4P`；`regulator=U3 HT7533`；`local_mcu=null`；`onboard_adc=null`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页完整网格 A1-C3，U1A/U2/U3/J1/R1-R3/C1-C5

## 核心器件

### LM393DR2G 比较器连接

U1A LM393DR2G 的非反相输入 pin3 接 Ain，反相输入 pin2 接 R3 wiper，输出 pin1 接 Din；pin8 接 +3.3V、pin4 接 GND。R2 10KΩ 将 Din 上拉到 +3.3V，页面只展示 U1A 通道，没有显示另一比较器通道的连接。

- 参数与网络：`positive_input=pin3 Ain`；`negative_input=pin2 R3 threshold`；`output=pin1 Din`；`supply=pin8 +3.3V,pin4 GND`；`output_pullup=R2 10KΩ to +3.3V`；`other_channel_shown=false`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页网格 A2-B2，U1A LM393DR2G、R2、Ain、Din 与阈值线

## 电源

### VCC 至 +3.3V 稳压

J1 pin3 VCC 连接 U3 HT7533 VIN pin2，U3 VOUT pin3 输出 +3.3V，GND pin1 接地。C1 100nF 与 C5 10uF 跨接 VCC-GND，C3 100nF 与 C4 10uF 跨接 +3.3V-GND；原理图未显示使能、负载开关、电源监测或电池路径。

- 参数与网络：`input=J1 pin3 VCC`；`regulator=U3 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`input_caps=C1 100nF,C5 10uF`；`output_caps=C3 100nF,C4 10uF`；`enable=null`；`battery=null`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页网格 B3-C2，J1 VCC、U3 HT7533 与 C1/C3/C4/C5

## 接口

### J1 模拟/数字输出接口

J1 AD_Socket_4P pin1=Ain，是探针分压的模拟输出；pin2=Din，是比较器数字输出；pin3=VCC，为本单元电源输入；pin4=GND。Ain/Din 均由单元输出给外部主机，外部主机负责采样或读取。

- 参数与网络：`connector=J1 AD_Socket_4P`；`pin1=Ain analog output`；`pin2=Din comparator digital output`；`pin3=VCC power input`；`pin4=GND return`；`onboard_adc=null`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页网格 B3，J1 pin1-pin4 及 Ain/Din/VCC/GND 网络来源

## 复位

### 数字控制、时钟与调试配置

本页没有 MCU 或数字总线器件，因此没有 RESET、BOOT、中断、片选、I2C/SPI/UART/CAN、调试连接器或时钟源；Din 是模拟比较器输出，不是总线信号。

- 参数与网络：`reset=null`；`boot=null`；`interrupt=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`debug=null`；`clock=null`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页完整单页，器件仅 U1A/U2/U3/J1 与无源网络

## 保护电路

### 探针与外部接口保护配置

完整单页在 EARTH_PIN 和 J1 的 Ain、Din、VCC、GND 路径上未显示 TVS/ESD 阵列、保险丝、反接保护或串联限流器件；R1/R2 是功能上拉，C2 是模拟滤波，不能从图中归类为专用浪涌保护。

- 参数与网络：`probe=U2 EARTH_PIN`；`connector=J1 AD_Socket_4P`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_current_limit=null`；`functional_passives=R1/R2 pull-ups,C2 filter`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页完整 U2/J1 输入输出与供电路径

## 关键网络

### 关键网络索引

VCC 连接 J1 pin3、U3 VIN、C1/C5；+3.3V 连接 U3 VOUT、U1A pin8、R1/R2/R3、C3/C4；Ain 连接 U2 pin1、R1、C2、U1A pin3、J1 pin1；Din 连接 U1A pin1、R2、J1 pin2；GND 连接 J1 pin4、U1A pin4、U2 pin2、U3 pin1 和全部回路。

- 参数与网络：`VCC=J1 pin3,U3 VIN,C1,C5`；`+3.3V=U3 VOUT,U1A pin8,R1,R2,R3,C3,C4`；`Ain=U2 pin1,R1,C2,U1A pin3,J1 pin1`；`Din=U1A pin1,R2,J1 pin2`；`GND=J1 pin4,U1A pin4,U2 pin2,U3 pin1,R3,C1-C5`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页全部 VCC/+3.3V/Ain/Din/GND 同名网络与连接点

## 模拟电路

### EARTH_PIN 探针模拟网络

U2 EARTH_PIN pin1 直接连接 Ain，pin2 接 GND；R1 10KΩ 从 +3.3V 上拉 Ain，C2 100nF 从 Ain 接 GND。探针两端导通时形成从 Ain 经探针到 GND 的路径，与 R1 构成电阻分压，C2 对 Ain 进行低通滤波。

- 参数与网络：`probe_signal=U2 pin1 IN -> Ain`；`probe_return=U2 pin2 -> GND`；`pullup=R1 10KΩ to +3.3V`；`filter=C2 100nF to GND`；`host_output=J1 pin1 Ain`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页网格 A1-B2，U2 EARTH_PIN、R1、C2 与 Ain/GND/+3.3V

### R3 10K 可调比较阈值

R3 RPot 10K 的固定两端分别接 +3.3V 与 GND，滑动端连接 U1A 反相输入 pin2，因此电位器在电源轨之间产生可调比较阈值。

- 参数与网络：`potentiometer=R3 RPot 10K`；`high_end=+3.3V`；`low_end=GND`；`wiper=U1A pin2 negative input`；`threshold_range_schematic=GND to +3.3V`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页网格 A1-B2，R3 全部三端与 U1A pin2

### ADC 所属边界

原理图将未经板载 ADC 转换的 Ain 直接输出到 J1 pin1，且页面没有 MCU 或 ADC IC；因此任何数模采样、校准和湿度换算均在外部主机或软件侧完成，不属于本页电路。Din 则已由 U1A 比较形成数字阈值结果。

- 参数与网络：`raw_analog=Ain -> J1 pin1`；`digital_threshold=U1A -> Din -> J1 pin2`；`onboard_adc=null`；`host_adc_required_for_ain=true`；`onboard_calibration=null`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页完整信号链 U2/R1/C2 -> Ain -> U1A/J1，整页无 ADC/MCU

## 其他事实

### 原理图版本元数据

图框标注 Project Title 为 UNIT_EARTH.PrjPCB、Sheet Title 为 UNIT_EARTH.SchDoc、Revised 为 V1.0、日期为 07/18/2018，且 Sheet 1 of 1。

- 参数与网络：`project_title=UNIT_EARTH.PrjPCB`；`sheet_title=UNIT_EARTH.SchDoc`；`revision=V1.0`；`date=07/18/2018`；`sheet=1 of 1`
- 证据：图 57110761f8d2 / 第 1 页 / 第 1 页右下图框 Project Title/Sheet Title/Revised/Date/Sheet

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Earth 系统架构 | `probe=U2 EARTH_PIN`；`analog_output=Ain`；`comparator=U1A LM393DR2G`；`threshold=R3 RPot 10K`；`digital_output=Din`；`host_connector=J1 AD_Socket_4P`；`regulator=U3 HT7533`；`local_mcu=null`；`onboard_adc=null` |
| 模拟电路 | EARTH_PIN 探针模拟网络 | `probe_signal=U2 pin1 IN -> Ain`；`probe_return=U2 pin2 -> GND`；`pullup=R1 10KΩ to +3.3V`；`filter=C2 100nF to GND`；`host_output=J1 pin1 Ain` |
| 模拟电路 | R3 10K 可调比较阈值 | `potentiometer=R3 RPot 10K`；`high_end=+3.3V`；`low_end=GND`；`wiper=U1A pin2 negative input`；`threshold_range_schematic=GND to +3.3V` |
| 核心器件 | LM393DR2G 比较器连接 | `positive_input=pin3 Ain`；`negative_input=pin2 R3 threshold`；`output=pin1 Din`；`supply=pin8 +3.3V,pin4 GND`；`output_pullup=R2 10KΩ to +3.3V`；`other_channel_shown=false` |
| 接口 | J1 模拟/数字输出接口 | `connector=J1 AD_Socket_4P`；`pin1=Ain analog output`；`pin2=Din comparator digital output`；`pin3=VCC power input`；`pin4=GND return`；`onboard_adc=null` |
| 电源 | VCC 至 +3.3V 稳压 | `input=J1 pin3 VCC`；`regulator=U3 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`input_caps=C1 100nF,C5 10uF`；`output_caps=C3 100nF,C4 10uF`；`enable=null`；`battery=null` |
| 模拟电路 | ADC 所属边界 | `raw_analog=Ain -> J1 pin1`；`digital_threshold=U1A -> Din -> J1 pin2`；`onboard_adc=null`；`host_adc_required_for_ain=true`；`onboard_calibration=null` |
| 关键网络 | 关键网络索引 | `VCC=J1 pin3,U3 VIN,C1,C5`；`+3.3V=U3 VOUT,U1A pin8,R1,R2,R3,C3,C4`；`Ain=U2 pin1,R1,C2,U1A pin3,J1 pin1`；`Din=U1A pin1,R2,J1 pin2`；`GND=J1 pin4,U1A pin4,U2 pin2,U3 pin1,R3,C1-C5` |
| 保护电路 | 探针与外部接口保护配置 | `probe=U2 EARTH_PIN`；`connector=J1 AD_Socket_4P`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_current_limit=null`；`functional_passives=R1/R2 pull-ups,C2 filter` |
| 复位 | 数字控制、时钟与调试配置 | `reset=null`；`boot=null`；`interrupt=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`debug=null`；`clock=null` |
| 其他事实 | 原理图版本元数据 | `project_title=UNIT_EARTH.PrjPCB`；`sheet_title=UNIT_EARTH.SchDoc`；`revision=V1.0`；`date=07/18/2018`；`sheet=1 of 1` |
| 电源 | 正文中的 5V 接口供电 | `documented_voltage=5V`；`schematic_net=VCC`；`connector=J1 pin3`；`regulator=U3 HT7533`；`schematic_numeric_voltage=null` |
| 传感器 | 正文中的土壤湿度与 ADC 解释 | `documented_quantity=soil moisture`；`documented_principle=higher moisture -> higher conductivity`；`schematic_signal=Ain resistance divider`；`documented_adc_destination=M5Core`；`calibration_curve=null`；`range=null`；`accuracy=null`；`temperature_compensation=null` |
| 传感器 | 正文中的电极耐久警告 | `documented_corrosion_protection=false`；`documented_waterproof=false`；`documented_use=proof of concept`；`electrode_material=null`；`coating=null`；`immersion_time=null`；`environment_rating=null` |

## 待确认事项

- `power.documented-five-volt`：产品正文的 HY2.0-4P 映射将红线标为 5V；原理图只把 J1 pin3 和 U3 VIN 网络标为 VCC，没有直接标注 5V 数值、输入范围或允许纹波。（证据：图 57110761f8d2 / 第 1 页 / 第 1 页 J1 pin3 VCC 与 U3 VIN，整页无 5V 文字）
- `sensor.documented-moisture-behavior`：产品正文称水分含量越高时探针间导电性越好，并描述通过探针电势差和 ADC 转换把结果发送给 M5Core；原理图确认探针电阻分压和 Ain 输出，但没有湿度到电阻/电压的标定曲线、量程、精度、温度补偿、土壤类型条件或板载 ADC。（证据：图 57110761f8d2 / 第 1 页 / 第 1 页 U2/R1/C2 Ain 探针网络与 J1，图中无湿度标定或 ADC）
- `sensor.documented-electrode-durability`：产品正文警告电极不防腐、不防水，仅用于概念验证且不应长时间置于潮湿环境；原理图只显示 U2 EARTH_PIN 电气连接，未给出电极材料、镀层、允许浸泡时间、腐蚀寿命或环境等级。（证据：图 57110761f8d2 / 第 1 页 / 第 1 页 U2 EARTH_PIN，图中无机械材料或环境等级）
- `review.input-voltage`：请结合当前 U019 BOM、接口规范或实板测量确认 J1 VCC 的额定输入是否为 5V 及允许范围。；原因：原理图只标 VCC，没有直接标注输入电压数值。
- `review.moisture-calibration`：请用指定土壤、温度、探针插入条件和外部 ADC 建立 Ain 与含水量的标定曲线，并确认量程、精度和 Din 阈值行为。；原因：原理图只证明电阻分压与比较器拓扑，不能证明土壤湿度性能或换算关系。
- `review.electrode-durability`：请确认当前电极材料、表面处理、防水/防腐等级、允许连续通电和潮湿暴露时间及推荐维护周期。；原因：这些机械与环境边界未在原理图中给出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `57110761f8d22af3651078c063d19e9ff143c6022ec586ffff48d7099e49805f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/728/U019_UNIT_EARTH_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/earth.md`

源文档 SHA-256：`ac399df0f0624eae2b2cc2369c3df515c3fe35411d468e614b6dc7139e49ac25`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
