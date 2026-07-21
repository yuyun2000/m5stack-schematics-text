# Unit ENV 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ENV |
| SKU | U001 |
| 产品 ID | `unit-env-2ba151987edb` |
| 源文档 | `zh_CN/unit/env.md` |

## 概述

Unit ENV（U001）在同一 Grove I2C 总线上连接 U1 DHT12 与 U2 BMP280，外部主机通过 J1 的 SCL/SDA 访问两颗传感器。DHT12 直接使用 VCC，R1/R2 各 4.7KΩ 也将 SCL/SDA 上拉到 VCC；U3 HT7533 则把 VCC 转为 +3.3V，供 BMP280 的 Vdd/Vddio/CSB 使用。BMP280 的 SDO 接 GND，CSB 接 +3.3V；页面没有电平转换、本地主控、外部时钟或专用接口保护。正文所列 VCC=5V、DHT12=0x5C、BMP280=0x76 及温湿压性能未直接印在原理图上，且正文不同表格的精度值互相冲突，需结合 datasheet 或实测确认。

## 检索关键词

`Unit ENV`、`U001`、`UNIT_THP V1.0`、`DHT12`、`BMP280`、`HT7533`、`IIC_Socket_4P`、`I2C`、`0x5C`、`0x76`、`SCL`、`SDA`、`IIC_SCL`、`IIC_SDA`、`VCC`、`+3.3V`、`CSB`、`SDO`、`SDI`、`SCK`、`R1 4.7KΩ`、`R2 4.7KΩ`、`温度`、`湿度`、`大气压`、`环境传感器`、`Grove I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | DHT12 | VCC 供电、连接共享 SCL/SDA 的 I2C 环境传感器 | 图 33e669548c68 / 第 1 页 / 第 1 页网格 B2，U1 DHT12，pin1 VCC、pin2 SDA、pin3 GND、pin4 SCL |
| U2 | BMP280 | +3.3V 供电的 I2C 气压传感器，SCK/SDI 接共享 SCL/SDA，CSB 高、SDO 低绑带 | 图 33e669548c68 / 第 1 页 / 第 1 页网格 C1-C2，U2 BMP280，pin4 SCK、pin3 SDI、pin2 CSB、pin5 SDO、pin8 Vdd、pin6 Vddio、pin1/pin7 GND |
| U3 | HT7533 | 将 J1 输入 VCC 稳压为 BMP280 使用的 +3.3V | 图 33e669548c68 / 第 1 页 / 第 1 页网格 C3，U3 HT7533，VIN pin2 VCC、VOUT pin3 +3.3V、GND pin1 |
| J1 | IIC_Socket_4P | 四针 Grove I2C 接口，引出 IIC_SCL、IIC_SDA、VCC 和 GND | 图 33e669548c68 / 第 1 页 / 第 1 页网格 B3，J1 IIC_Socket_4P，pin1 IIC_SCL、pin2 IIC_SDA、pin3 VCC、pin4 GND |
| R1,R2 | 4.7KΩ | 分别将共享 SCL 与 SDA 上拉到 VCC 的 I2C 上拉电阻 | 图 33e669548c68 / 第 1 页 / 第 1 页网格 B2，R1 4.7KΩ 从 VCC 到 SCL、R2 4.7KΩ 从 VCC 到 SDA |
| C1,C2,C3,C4 | 100nF / 10uF | VCC 与 +3.3V 电源轨的去耦和储能电容 | 图 33e669548c68 / 第 1 页 / 第 1 页网格 B3-C3，C1 100nF 与 C4 10uF 跨 VCC-GND，C2 100nF 与 C3 10uF 跨 +3.3V-GND |

## 系统结构

### Unit ENV 系统架构

J1 从外部主机引入 VCC、GND、SCL 和 SDA，U1 DHT12 与 U2 BMP280 并联在同一 I2C 总线上；DHT12 使用 VCC，BMP280 使用 U3 HT7533 生成的 +3.3V。完整单页没有本地主控、协处理器、存储器、晶振、复位、射频、音频、电池或充电电路。

- 参数与网络：`external_controller=via J1 SCL/SDA`；`devices=U1 DHT12,U2 BMP280`；`bus=shared I2C`；`dht_supply=VCC`；`bmp_supply=+3.3V`；`regulator=U3 HT7533`；`local_controller=null`；`storage=null`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页完整网格 B2-C3，U1/U2/U3/J1/R1/R2/C1-C4

## 电源

### VCC 至 +3.3V 稳压

J1 pin3 VCC 连接 U3 HT7533 VIN pin2，U3 VOUT pin3 输出 +3.3V，GND pin1 接地。C1 100nF 与 C4 10uF 跨接 VCC-GND，C2 100nF 与 C3 10uF 跨接 +3.3V-GND；原理图未显示使能、负载开关、电源监测或电池路径。

- 参数与网络：`input=J1 pin3 VCC`；`regulator=U3 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`；`enable=null`；`battery=null`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 B3-C3，J1 VCC、U3 HT7533 与 C1-C4

## 接口

### J1 Grove I2C 接口

J1 IIC_Socket_4P pin1 标为 IIC_SCL 并连接 SCL，pin2 标为 IIC_SDA 并连接 SDA，pin3 为 VCC 电源输入，pin4 为 GND。SCL/SDA 是外部主机与两颗板载传感器之间的双向 I2C 总线。

- 参数与网络：`connector=J1 IIC_Socket_4P`；`pin1=IIC_SCL -> SCL`；`pin2=IIC_SDA -> SDA`；`pin3=VCC power input`；`pin4=GND return`；`devices=U1 DHT12,U2 BMP280`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 B3，J1 pin1-pin4 与 U1/U2 同名 SCL/SDA 网络

## 总线

### DHT12 与 BMP280 共享 I2C

外部 I2C 控制器经 J1 SCL/SDA 同时连接 U1 DHT12 pin4/pin2 和 U2 BMP280 SCK pin4/SDI pin3。R1/R2 各 4.7KΩ 将 SCL/SDA 上拉到 VCC；页面未显示总线复用器、串联电阻或其他 I2C 设备。

- 参数与网络：`controller=external via J1`；`scl=J1 pin1 -> U1 pin4,U2 pin4`；`sda=J1 pin2 -> U1 pin2,U2 pin3`；`pullups=R1/R2 4.7KΩ to VCC`；`devices=DHT12,BMP280`；`mux=null`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页 U1/U2/J1 的共享 SCL/SDA 同名网络与 R1/R2

### I2C 上拉与传感器供电域

原理图将 DHT12 VDD 和 R1/R2 上拉端接 VCC，而 BMP280 Vdd/Vddio 接 +3.3V；SCL/SDA 在两颗器件之间直接相连，完整页面没有 MOSFET、电平转换 IC 或其他电平隔离器件。

- 参数与网络：`pullup_rail=VCC`；`dht12_supply=VCC`；`bmp280_supply=+3.3V`；`direct_shared_bus=true`；`level_shifter=null`；`vcc_numeric_value_on_schematic=null`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 B2-C2，U1 VCC、R1/R2 VCC、U2 +3.3V 与直连 SCL/SDA

## GPIO 与控制信号

### BMP280 CSB 与 SDO 绑带

U2 CSB pin2 固定接 +3.3V，SDO pin5 固定接 GND。原理图明确给出 CSB 高电平和 SDO 低电平硬件绑带，但没有在图中标注由此对应的协议模式或数值地址。

- 参数与网络：`csb=U2 pin2 -> +3.3V`；`sdo=U2 pin5 -> GND`；`address_select_level=low`；`numeric_address_on_schematic=null`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 C1-C2，U2 CSB pin2 与 SDO pin5 连接

## 复位

### 复位、BOOT、时钟与调试配置

本页没有本地主控，未显示 RESET、BOOT、中断引出、片选控制、调试连接器或外部晶振/振荡器。BMP280 CSB/SDO 为固定硬件绑带，DHT12 仅有 VCC/SDA/GND/SCL 四线。

- 参数与网络：`reset=null`；`boot=null`；`interrupt=null`；`debug=null`；`external_clock=null`；`bmp_straps=CSB +3.3V,SDO GND`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页完整单页，U1/U2/U3/J1 与全部无源器件

## 保护电路

### Grove 接口保护配置

完整单页在 J1 的 VCC、SCL、SDA 和 GND 路径上未显示 TVS/ESD 阵列、保险丝、反接保护或串联限流器件；R1/R2 是 I2C 上拉，不是专用接口保护。

- 参数与网络：`connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`i2c_pullups=R1/R2 4.7KΩ`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页完整 J1 到 U1/U2/U3 的供电与信号路径

## 关键网络

### 关键网络索引

VCC 连接 J1 pin3、U1 pin1、R1/R2、U3 VIN、C1/C4；+3.3V 连接 U3 VOUT、U2 Vdd/Vddio/CSB、C2/C3；SCL 连接 J1 pin1、U1 pin4、U2 pin4、R1；SDA 连接 J1 pin2、U1 pin2、U2 pin3、R2；GND 连接 J1 pin4、U1 pin3、U2 pin1/pin5/pin7、U3 pin1 与全部电容。

- 参数与网络：`VCC=J1 pin3,U1 pin1,R1,R2,U3 VIN,C1,C4`；`+3.3V=U3 VOUT,U2 Vdd/Vddio/CSB,C2,C3`；`SCL=J1 pin1,U1 pin4,U2 pin4,R1`；`SDA=J1 pin2,U1 pin2,U2 pin3,R2`；`GND=J1 pin4,U1 pin3,U2 pin1/5/7,U3 pin1,C1-C4`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页全部 VCC/+3.3V/SCL/SDA/GND 同名网络与连接点

## 传感器

### DHT12 电源与 I2C 连接

U1 DHT12 pin1 接 VCC，pin2 接 SDA，pin3 接 GND，pin4 接 SCL。SCL/SDA 分别通过 R1/R2 4.7KΩ 上拉到 VCC，且直接连接 J1 与 BMP280。

- 参数与网络：`part_number=U1 DHT12`；`pin1=VCC`；`pin2=SDA`；`pin3=GND`；`pin4=SCL`；`scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 B2，U1 DHT12 pin1-pin4、R1/R2 与 VCC/SCL/SDA/GND

### BMP280 电源与 I2C 连接

U2 BMP280 的 SCK pin4 接 SCL，SDI pin3 接 SDA，CSB pin2、Vdd pin8、Vddio pin6 接 +3.3V；SDO pin5 与 GND pin1/pin7 接 GND。

- 参数与网络：`part_number=U2 BMP280`；`scl=pin4 SCK`；`sda=pin3 SDI`；`csb=pin2 +3.3V`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`sdo=pin5 GND`；`ground=pins1/7 GND`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页网格 C1-C2，U2 BMP280 全部 pin1-pin8 与网络

## 其他事实

### 原理图版本元数据

图框标注 Project Title 为 UNIT_THP.PrjPCB、Sheet Title 为 UNIT_THP.SchDoc、Revised 为 V1.0、Date 为 180418，且 Sheet 1 of 1。

- 参数与网络：`project_title=UNIT_THP.PrjPCB`；`sheet_title=UNIT_THP.SchDoc`；`revision=V1.0`；`date=180418`；`sheet=1 of 1`
- 证据：图 33e669548c68 / 第 1 页 / 第 1 页右下图框 Project Title/Sheet Title/Revised/Date/Sheet

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ENV 系统架构 | `external_controller=via J1 SCL/SDA`；`devices=U1 DHT12,U2 BMP280`；`bus=shared I2C`；`dht_supply=VCC`；`bmp_supply=+3.3V`；`regulator=U3 HT7533`；`local_controller=null`；`storage=null` |
| 传感器 | DHT12 电源与 I2C 连接 | `part_number=U1 DHT12`；`pin1=VCC`；`pin2=SDA`；`pin3=GND`；`pin4=SCL`；`scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC` |
| 传感器 | BMP280 电源与 I2C 连接 | `part_number=U2 BMP280`；`scl=pin4 SCK`；`sda=pin3 SDI`；`csb=pin2 +3.3V`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`sdo=pin5 GND`；`ground=pins1/7 GND` |
| 电源 | VCC 至 +3.3V 稳压 | `input=J1 pin3 VCC`；`regulator=U3 HT7533`；`vin=pin2 VCC`；`vout=pin3 +3.3V`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`；`enable=null`；`battery=null` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 IIC_Socket_4P`；`pin1=IIC_SCL -> SCL`；`pin2=IIC_SDA -> SDA`；`pin3=VCC power input`；`pin4=GND return`；`devices=U1 DHT12,U2 BMP280` |
| 总线 | DHT12 与 BMP280 共享 I2C | `controller=external via J1`；`scl=J1 pin1 -> U1 pin4,U2 pin4`；`sda=J1 pin2 -> U1 pin2,U2 pin3`；`pullups=R1/R2 4.7KΩ to VCC`；`devices=DHT12,BMP280`；`mux=null` |
| 总线 | I2C 上拉与传感器供电域 | `pullup_rail=VCC`；`dht12_supply=VCC`；`bmp280_supply=+3.3V`；`direct_shared_bus=true`；`level_shifter=null`；`vcc_numeric_value_on_schematic=null` |
| GPIO 与控制信号 | BMP280 CSB 与 SDO 绑带 | `csb=U2 pin2 -> +3.3V`；`sdo=U2 pin5 -> GND`；`address_select_level=low`；`numeric_address_on_schematic=null` |
| 关键网络 | 关键网络索引 | `VCC=J1 pin3,U1 pin1,R1,R2,U3 VIN,C1,C4`；`+3.3V=U3 VOUT,U2 Vdd/Vddio/CSB,C2,C3`；`SCL=J1 pin1,U1 pin4,U2 pin4,R1`；`SDA=J1 pin2,U1 pin2,U2 pin3,R2`；`GND=J1 pin4,U1 pin3,U2 pin1/5/7,U3 pin1,C1-C4` |
| 保护电路 | Grove 接口保护配置 | `connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_signal_resistors=null`；`i2c_pullups=R1/R2 4.7KΩ` |
| 复位 | 复位、BOOT、时钟与调试配置 | `reset=null`；`boot=null`；`interrupt=null`；`debug=null`；`external_clock=null`；`bmp_straps=CSB +3.3V,SDO GND` |
| 其他事实 | 原理图版本元数据 | `project_title=UNIT_THP.PrjPCB`；`sheet_title=UNIT_THP.SchDoc`；`revision=V1.0`；`date=180418`；`sheet=1 of 1` |
| 电源 | 正文中的 Grove 5V 供电 | `documented_voltage=5V`；`schematic_net=VCC`；`connector=J1 pin3`；`vcc_loads=DHT12,R1/R2,U3`；`schematic_numeric_voltage=null` |
| 总线地址 | DHT12 与 BMP280 I2C 地址 | `documented_dht12=0x5C`；`documented_bmp280=0x76`；`dht12_address_select=null`；`bmp280_address_select=SDO pin5 GND`；`schematic_numeric_addresses=null` |
| 传感器 | 正文中的温湿压量程与精度 | `documented_temperature_range=-20 to 60°C`；`documented_humidity_range=20 to 95%RH`；`documented_pressure_range=300 to 1100hPa`；`spec_table_accuracy=temperature ±0.2°C,humidity ±0.1%RH,pressure ±1hPa`；`comparison_accuracy=temperature ±0.5°C,humidity ±5%RH,pressure ±0.12hPa`；`documented_operating_temperature=0 to 60°C`；`schematic_performance_parameters=null` |

## 待确认事项

- `power.documented-five-volt`：产品正文的 HY2.0-4P 映射将红线标为 5V；原理图只把 J1 pin3、DHT12 电源、I2C 上拉和 U3 VIN 网络标为 VCC，没有直接标注 5V 数值或输入范围。（证据：图 33e669548c68 / 第 1 页 / 第 1 页全部 VCC 网络，整页无 5V 文字）
- `address.documented-i2c-addresses`：产品正文列出 DHT12 地址 0x5C、BMP280 地址 0x76；原理图没有地址文字或总线扫描结果，只确认 DHT12 无外部地址选择连接、BMP280 SDO pin5 接 GND。（证据：图 33e669548c68 / 第 1 页 / 第 1 页 U1/U2 共享 SCL/SDA 与 U2 SDO-GND，整页无 0x5C/0x76）
- `sensor.documented-measurement-specs`：正文规格表列出温度 -20~60°C/±0.2°C、湿度 20~95%RH/±0.1%RH、气压 300~1100hPa/±1hPa；同页产品对比表又列 Unit ENV 温度 ±0.5°C、湿度 ±5%RH、气压 ±0.12hPa。原理图只确认 DHT12/BMP280 型号及连接，没有量程、精度、响应时间、采样率、校准或工作温度参数，且两组精度互相冲突。（证据：图 33e669548c68 / 第 1 页 / 第 1 页 U1 DHT12 与 U2 BMP280，整页无性能参数）
- `review.input-and-pullup-voltage`：请结合当前 U001 BOM、接口规范或实板测量确认 VCC 是否为 5V，并确认 R1/R2 将共享 I2C 上拉到该电压时与 +3.3V BMP280 Vddio 的电气兼容边界。；原因：原理图只标 VCC 数值未知，同时明确显示 BMP280 Vddio 为 +3.3V 且无电平转换。
- `review.i2c-addresses`：请用 DHT12/BMP280 datasheet 或上电扫描确认 7 位地址 DHT12=0x5C、BMP280=0x76。；原因：数值地址未在原理图中标注。
- `review.measurement-spec-conflict`：请以当前 BOM 对应 datasheet 和整机测试统一确认温湿压量程、精度、工作温度、响应时间、采样率和校准条件，并修正文档中两组冲突精度。；原因：原理图没有性能参数，正文规格表与产品对比表的精度数值相互冲突。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `33e669548c680a595aee29cd1a280fee25fe942ec93a09bf84a2e1d31cdd3f8c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/721/U001_UNIT_ENV_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/env.md`

源文档 SHA-256：`7ec388296200ef75a417aa251aa5e199135151848fe4910b29267696d2c35ef9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
