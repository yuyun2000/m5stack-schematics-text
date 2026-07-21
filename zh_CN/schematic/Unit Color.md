# Unit Color 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Color |
| SKU | U009 |
| 产品 ID | `unit-color-c738d15370d3` |
| 源文档 | `zh_CN/unit/COLOR.md` |

## 概述

Unit Color（U009）以 U1 TCS34725FN 颜色/环境光传感器为核心，通过 J1 的 SCL/SDA 接入外部 I2C 主机；R3/R4 各 4.7KΩ 将总线拉到 +3.3V。J1 的 VCC 经 U2 HT7533 生成 +3.3V，为传感器供电，同时 VCC 直接经 R1/R2 各 1KΩ 驱动两只白色 0603 补光 LED。U1 INT pin5 只连接 jp1 test，未引到 Grove；图中没有本地主控、地址选择、总线电平转换或专用接口保护。正文所列 VCC=5V、I2C 地址 0x29、RGBC 四通道和工作温度范围未直接印在原理图上，需结合 datasheet 或实测确认。

## 检索关键词

`Unit Color`、`U009`、`UNIT_COLOR V1.0`、`TCS34725FN`、`TCS3472`、`HT7533`、`IIC_Socket_4P`、`Grove I2C`、`I2C`、`0x29`、`SCL`、`SDA`、`IIC_SCL`、`IIC_SDA`、`INT`、`jp1 test`、`VCC`、`+3.3V`、`R3 4.7KΩ`、`R4 4.7KΩ`、`白灯 0603`、`D1`、`D2`、`RGB`、`RGBC`、`颜色传感器`、`环境光`、`补光 LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TCS34725FN | +3.3V 供电的 I2C 颜色/光传感器，连接 SCL、SDA，并将 INT 引到测试点 | 图 01245e56e695 / 第 1 页 / 第 1 页网格 B2，U1 TCS34725FN，pin1 VDD、pin2 SCL、pin3 GND、pin4 NC、pin5 INT、pin6 SDA |
| U2 | HT7533 | 将连接器 VCC 稳压为 U1 和 I2C 上拉使用的 +3.3V | 图 01245e56e695 / 第 1 页 / 第 1 页网格 C2，U2 HT7533，VIN pin2 接 VCC、VOUT pin3 接 +3.3V、GND pin1 接地 |
| J1 | IIC_Socket_4P | 四针 Grove I2C 接口，引出 IIC_SCL、IIC_SDA、VCC 和 GND | 图 01245e56e695 / 第 1 页 / 第 1 页网格 C3，J1 IIC_Socket_4P，pin1 IIC_SCL、pin2 IIC_SDA、pin3 VCC、pin4 GND |
| jp1 | test | U1 INT pin5 的单线测试点/测试连接 | 图 01245e56e695 / 第 1 页 / 第 1 页网格 B2，U1 INT pin5 右侧短线标注 jp1、test |
| D1,D2 | 白灯 0603 | 两只由 VCC 常供电的白色补光 LED | 图 01245e56e695 / 第 1 页 / 第 1 页网格 A1，D1/D2 均标注 白灯 0603，下端接 GND |
| R1,R2 | 1KΩ | D1/D2 白色补光 LED 的 VCC 侧串联限流电阻 | 图 01245e56e695 / 第 1 页 / 第 1 页网格 A1，VCC-R1 1KΩ-D1-GND 与 VCC-R2 1KΩ-D2-GND |
| R3,R4 | 4.7KΩ | 分别将 SCL 与 SDA 上拉到 +3.3V 的 I2C 上拉电阻 | 图 01245e56e695 / 第 1 页 / 第 1 页网格 C3，R3 4.7KΩ 从 +3.3V 到 SCL，R4 4.7KΩ 从 +3.3V 到 SDA |
| C1,C2,C3,C4 | 100nF / 100nF / 10uF / 10uF | VCC 与 +3.3V 电源轨的旁路和储能电容 | 图 01245e56e695 / 第 1 页 / 第 1 页网格 C2-C3，C1 100nF 与 C4 10uF 跨接 VCC-GND，C2 100nF 与 C3 10uF 跨接 +3.3V-GND |

## 系统结构

### Unit Color 系统架构

J1 从外部主机引入 VCC、GND、SCL 和 SDA；U2 HT7533 生成 +3.3V，U1 TCS34725FN 作为唯一 I2C 设备连接 SCL/SDA，D1/D2 构成 VCC 供电的双白灯补光。完整单页没有本地主控、协处理器、存储器、晶振、射频、音频、电池或充电电路。

- 参数与网络：`external_controller=via J1 IIC_SCL/IIC_SDA`；`sensor=U1 TCS34725FN`；`regulator=U2 HT7533`；`illumination=D1/D2 white 0603`；`local_controller=null`；`storage=null`；`clock=null`；`battery=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页完整网格 A1-C3，D1/D2、U1、U2、J1 与全部无源器件

## 电源

### VCC 至 +3.3V 稳压路径

J1 pin3 的 VCC 连接 U2 HT7533 VIN pin2，U2 VOUT pin3 输出 +3.3V，GND pin1 接地。输入侧 C1 100nF 与 C4 10uF 跨接 VCC-GND，输出侧 C2 100nF 与 C3 10uF 跨接 +3.3V-GND；原理图未显示稳压器使能、负载开关或电源监测。

- 参数与网络：`input=J1 pin3 VCC`；`regulator=U2 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`ground=pin1 GND`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`；`enable=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 C2-C3，J1 VCC、U2 HT7533 与 C1-C4

### 双白色补光 LED 供电

D1 与 D2 均标为 白灯 0603；每条支路从 VCC 经独立 1KΩ 电阻 R1/R2、再经 LED 接 GND。两条支路没有开关、晶体管或 GPIO 控制，因此图示状态下随 VCC 供电。

- 参数与网络：`led1=VCC -> R1 1KΩ -> D1 white 0603 -> GND`；`led2=VCC -> R2 1KΩ -> D2 white 0603 -> GND`；`control_gpio=null`；`switch=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 A1，两条完整 VCC-R1/R2-D1/D2-GND 支路

## 接口

### J1 Grove I2C 接口针脚

J1 IIC_Socket_4P 的 pin1 标为 IIC_SCL 并连接 SCL，pin2 标为 IIC_SDA 并连接 SDA，pin3 为 VCC 电源输入，pin4 为 GND。SCL/SDA 在板上由 R3/R4 上拉到 +3.3V，图中没有把 U1 INT 引到 J1。

- 参数与网络：`connector=J1 IIC_Socket_4P`；`pin1=IIC_SCL -> SCL, bidirectional I2C clock line`；`pin2=IIC_SDA -> SDA, bidirectional I2C data`；`pin3=VCC power input`；`pin4=GND return`；`interrupt_pin=null`；`signal_pullup_voltage=+3.3V`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 C3，J1 pin1-pin4 与 R3/R4；网格 B2 U1 INT 仅到 jp1

## 总线

### SCL/SDA I2C 总线连接

外部 I2C 控制器经 J1 pin1 SCL 和 pin2 SDA 直接连接 U1 SCL pin2 与 SDA pin6；R3/R4 各 4.7KΩ 分别把 SCL/SDA 上拉至 +3.3V。页面未显示电平转换器、串联电阻、总线复用器或其他 I2C 设备。

- 参数与网络：`controller=external via J1`；`scl=J1 pin1 -> U1 pin2`；`sda=J1 pin2 -> U1 pin6`；`pullups=R3/R4 4.7KΩ to +3.3V`；`level_shifter=null`；`other_devices=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 B2-C3，U1 SCL/SDA 同名网络、R3/R4 与 J1

## GPIO 与控制信号

### U1 INT 测试点

U1 INT pin5 通过一段独立网络连接标为 jp1、test 的单线测试点；该 INT 网络未连接 J1，也未显示上拉、下拉、滤波或保护器件。

- 参数与网络：`source=U1 INT pin5`；`destination=jp1 test`；`grove_connection=null`；`pullup=null`；`pulldown=null`；`filter=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 B2，U1 pin5 INT 右侧 jp1 test

## 复位

### 复位、BOOT、使能、时钟与调试

本页没有本地主控，未显示 RESET、BOOT、片选、总线使能、调试连接器或外部晶振/振荡器。U2 未画独立使能脚，U1 INT 仅连接测试点。

- 参数与网络：`reset=null`；`boot=null`；`chip_select=null`；`bus_enable=null`；`debug_connector=null`；`external_clock=null`；`regulator_enable=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页完整单页，U1/U2/J1/jp1 及全部器件

## 保护电路

### Grove 接口保护配置

完整单页原理图在 J1 的 VCC、SCL、SDA 和 GND 路径上未显示 TVS/ESD 阵列、保险丝、反接保护或串联限流器件；R3/R4 是接 +3.3V 的 I2C 上拉，不能从图中归类为专用接口保护。

- 参数与网络：`connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`i2c_pullups=R3/R4 4.7KΩ`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页完整 J1 至 U1/U2 的 VCC/SCL/SDA/GND 路径

## 关键网络

### 关键网络索引

VCC 连接 J1 pin3、U2 VIN、C1/C4 和两条白灯支路；+3.3V 连接 U2 VOUT、U1 VDD、C2/C3 与 R3/R4；SCL 连接 J1 pin1、R3 与 U1 pin2；SDA 连接 J1 pin2、R4 与 U1 pin6；GND 连接 J1 pin4、U1/U2、所有电容和 LED 回路。

- 参数与网络：`VCC=J1 pin3,U2 VIN,C1,C4,R1,R2`；`+3.3V=U2 VOUT,U1 VDD,C2,C3,R3,R4`；`SCL=J1 pin1,R3,U1 pin2`；`SDA=J1 pin2,R4,U1 pin6`；`GND=J1 pin4,U1 pin3,U2 pin1,C1-C4,D1,D2`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页全部 VCC/+3.3V/GND/SCL/SDA 同名网络与连接点

## 传感器

### TCS34725FN 电源与信号连接

U1 TCS34725FN 的 VDD pin1 接 +3.3V，SCL pin2 接 SCL，GND pin3 接 GND，NC pin4 明确未连接，INT pin5 接 jp1 test，SDA pin6 接 SDA。原理图没有展开芯片内部光学通道或寄存器。

- 参数与网络：`part_number=U1 TCS34725FN`；`pin1=VDD +3.3V`；`pin2=SCL`；`pin3=GND`；`pin4=NC`；`pin5=INT -> jp1 test`；`pin6=SDA`；`internal_channels=null`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页网格 B2，U1 pin1-pin6 与 +3.3V/SCL/GND/jp1/SDA

## 其他事实

### 原理图版本元数据

图框标注 Project Title 为 UNIT_COLOR.PrjPCB、Sheet Title 为 UNIT_COLOR.SchDoc、Revised 为 V1.0、日期为 07/19/2018，且 Sheet 1 of 1。

- 参数与网络：`project_title=UNIT_COLOR.PrjPCB`；`sheet_title=UNIT_COLOR.SchDoc`；`revision=V1.0`；`date=07/19/2018`；`sheet=1 of 1`
- 证据：图 01245e56e695 / 第 1 页 / 第 1 页右下图框 Project Title/Sheet Title/Revised/Date/Sheet 字段

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Color 系统架构 | `external_controller=via J1 IIC_SCL/IIC_SDA`；`sensor=U1 TCS34725FN`；`regulator=U2 HT7533`；`illumination=D1/D2 white 0603`；`local_controller=null`；`storage=null`；`clock=null`；`battery=null` |
| 传感器 | TCS34725FN 电源与信号连接 | `part_number=U1 TCS34725FN`；`pin1=VDD +3.3V`；`pin2=SCL`；`pin3=GND`；`pin4=NC`；`pin5=INT -> jp1 test`；`pin6=SDA`；`internal_channels=null` |
| 电源 | VCC 至 +3.3V 稳压路径 | `input=J1 pin3 VCC`；`regulator=U2 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`ground=pin1 GND`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`；`enable=null` |
| 电源 | 双白色补光 LED 供电 | `led1=VCC -> R1 1KΩ -> D1 white 0603 -> GND`；`led2=VCC -> R2 1KΩ -> D2 white 0603 -> GND`；`control_gpio=null`；`switch=null` |
| 接口 | J1 Grove I2C 接口针脚 | `connector=J1 IIC_Socket_4P`；`pin1=IIC_SCL -> SCL, bidirectional I2C clock line`；`pin2=IIC_SDA -> SDA, bidirectional I2C data`；`pin3=VCC power input`；`pin4=GND return`；`interrupt_pin=null`；`signal_pullup_voltage=+3.3V` |
| 总线 | SCL/SDA I2C 总线连接 | `controller=external via J1`；`scl=J1 pin1 -> U1 pin2`；`sda=J1 pin2 -> U1 pin6`；`pullups=R3/R4 4.7KΩ to +3.3V`；`level_shifter=null`；`other_devices=null` |
| GPIO 与控制信号 | U1 INT 测试点 | `source=U1 INT pin5`；`destination=jp1 test`；`grove_connection=null`；`pullup=null`；`pulldown=null`；`filter=null` |
| 关键网络 | 关键网络索引 | `VCC=J1 pin3,U2 VIN,C1,C4,R1,R2`；`+3.3V=U2 VOUT,U1 VDD,C2,C3,R3,R4`；`SCL=J1 pin1,R3,U1 pin2`；`SDA=J1 pin2,R4,U1 pin6`；`GND=J1 pin4,U1 pin3,U2 pin1,C1-C4,D1,D2` |
| 保护电路 | Grove 接口保护配置 | `connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`i2c_pullups=R3/R4 4.7KΩ` |
| 复位 | 复位、BOOT、使能、时钟与调试 | `reset=null`；`boot=null`；`chip_select=null`；`bus_enable=null`；`debug_connector=null`；`external_clock=null`；`regulator_enable=null` |
| 其他事实 | 原理图版本元数据 | `project_title=UNIT_COLOR.PrjPCB`；`sheet_title=UNIT_COLOR.SchDoc`；`revision=V1.0`；`date=07/19/2018`；`sheet=1 of 1` |
| 电源 | 正文中的 Grove 5V 输入 | `documented_voltage=5V`；`schematic_net=VCC`；`connector=J1 pin3`；`regulator=U2 HT7533`；`schematic_numeric_voltage=null` |
| 总线地址 | TCS34725FN I2C 地址 | `documented_address=0x29`；`device=U1 TCS34725FN`；`address_select=null`；`schematic_numeric_address=null` |
| 传感器 | 正文中的 RGBC 测量与工作温度 | `documented_channels=R,G,B,clear/ambient light`；`documented_output=RGB data`；`documented_temperature=-40 to 85°C`；`range=null`；`accuracy=null`；`integration_time=null`；`spectral_response=null` |

## 待确认事项

- `power.documented-five-volt-input`：产品正文的 HY2.0-4P 映射将红线标为 5V；原理图仅把 J1 pin3 标为 VCC，并显示其进入 HT7533 与白灯支路，没有在网络名或电源符号中直接标出 5V 数值。（证据：图 01245e56e695 / 第 1 页 / 第 1 页 J1 pin3 VCC、U2 VIN 和 D1/D2 VCC 支路，整页无 5V 文字）
- `address.documented-0x29`：产品正文将 I2C 地址列为 0x29；原理图只显示 U1 TCS34725FN 直接连接 SCL/SDA，没有地址文字、地址选择引脚/绑带、datasheet 地址表或总线扫描结果。（证据：图 01245e56e695 / 第 1 页 / 第 1 页 U1 TCS34725FN 与 SCL/SDA，整页未出现 0x29）
- `sensor.documented-rgbc-performance`：产品正文称 U1 支持红、绿、蓝、环境光 RGBC 四通道测量并将环境光转换为 RGB 数据，工作温度范围为 -40 至 85°C；原理图只确认 TCS34725FN 型号、电源、I2C、INT 与双白灯连接，没有印出光学通道、量程、精度、积分时间、光谱响应或温度额定值。（证据：图 01245e56e695 / 第 1 页 / 第 1 页 U1 TCS34725FN 与 D1/D2 白灯，整页无 RGBC 性能或温度参数）
- `review.grove-input-voltage`：请结合当前 U009 BOM、接口规范或实板测量确认 J1 pin3 VCC 的额定输入是否为 5V 及允许范围。；原因：原理图只标 VCC，没有直接标注输入电压数值或范围。
- `review.tcs34725-address`：请用 TCS34725FN datasheet 或上电总线扫描确认本单元的 7 位 I2C 地址是否为 0x29。；原因：原理图没有地址文字或扫描结果。
- `review.rgbc-performance`：请以当前 TCS34725FN datasheet 或整机测试确认 RGBC 通道、工作温度、量程、精度、积分时间、光谱响应及双白灯条件。；原因：原理图没有光学性能或环境额定值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `01245e56e695e1d7de3713bbacf1d9c6a82c2f45883eade6631eeef22dfefe02` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/707/U009-UNIT_COLOR-SCHE_page_01.png` |

---

源文档：`zh_CN/unit/COLOR.md`

源文档 SHA-256：`59c5d499aa0b7f7e52ec4ef6c1403fe5d03d71119a7cb3e367cf0dffba4e21ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
