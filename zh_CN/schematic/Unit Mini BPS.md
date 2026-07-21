# Unit Mini BPS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini BPS |
| SKU | U090 |
| 产品 ID | `unit-mini-bps-50b079f537c4` |
| 源文档 | `zh_CN/unit/bps.md` |

## 概述

Unit Mini BPS 是一款由外部 I2C 控制器访问的 BMP280 气压/温度传感单元，J1 Grove 接口提供 SCL、SDA、+5V 和 GND。U1 HT7533 将 +5V 转为 +3.3V，为 U2 BMP280 供电；Q1/Q2 BSS138 与四个 4.7KΩ 上拉构成 5V 与 3.3V 域之间的 SDA/SCL 双向电平转换。BMP280 的 CSB 接 +3.3V、SDO 接 GND；正文所列 0x76 地址及量程/精度未直接印在原理图上，需结合器件资料或实测确认。

## 检索关键词

`Unit Mini BPS`、`U090`、`BMP280`、`HT7533`、`BSS138`、`HY-2.0_IIC`、`Grove I2C`、`I2C`、`0x76`、`SDA`、`SCL`、`IIC_SDA`、`IIC_SCL`、`+5V`、`+3.3V`、`CSB`、`SDO`、`SDI`、`SCK`、`Q1`、`Q2`、`U1`、`U2`、`J1`、`4.7KΩ`、`气压传感器`、`温度传感器`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | BMP280 | +3.3V 供电的气压/温度传感器，通过 SCK/SDI 引脚连接板上 SCL/SDA，CSB 上拉且 SDO 下拉 | 图 c1bee9d562a5 / 第 1 页 / 第 1 页中下部 U2 BMP280，pin4 SCK、pin3 SDI、pin2 CSB、pin5 SDO、pin8 Vdd、pin6 Vddio、pin1/pin7 GND |
| U1 | HT7533 | 将 J1 输入的 +5V 线性稳压为传感器与低压 I2C 域使用的 +3.3V | 图 c1bee9d562a5 / 第 1 页 / 第 1 页上中部 U1 HT7533，VIN pin2 接 +5V、VOUT pin3 接 +3.3V、GND 接地 |
| Q1,Q2 | BSS138 | 分别用于 SDA 与 SCL 的 5V/3.3V 双向电平转换，栅极连接 +3.3V | 图 c1bee9d562a5 / 第 1 页 / 第 1 页左中部，Q1 BSS138 串接 SDA、Q2 BSS138 串接 SCL，两管 gate 共接 +3.3V |
| J1 | HY-2.0_IIC | 四针 Grove I2C 外部接口，引出 SCL、SDA、+5V 和 GND | 图 c1bee9d562a5 / 第 1 页 / 第 1 页右侧 J1 HY-2.0_IIC，pin1 IIC_SCL、pin2 IIC_SDA、pin3 VCC、pin4 GND |
| R1,R2,R3,R4 | 4.7KΩ | I2C 上拉网络；R1/R2 将接口侧 SDA/SCL 上拉至 +5V，R3/R4 将传感器侧 SDA/SCL 上拉至 +3.3V | 图 c1bee9d562a5 / 第 1 页 / 第 1 页左侧 R1-R4：R1/R2 4.7KΩ 顶端 +5V，R3/R4 4.7KΩ 顶端 +3.3V |
| C1,C2,C4 | 10uF / 10uF / 100nF | HT7533 输入、输出滤波以及 BMP280 +3.3V 电源去耦 | 图 c1bee9d562a5 / 第 1 页 / 第 1 页上中部 C1 10uF 从 +5V 到 GND、C2 10uF 从 +3.3V 到 GND；右中部 C4 100nF 从 +3.3V 到 GND |

## 系统结构

### Unit Mini BPS 系统架构

J1 从外部主机引入 +5V、GND、SCL 和 SDA；U1 HT7533 生成 +3.3V，Q1/Q2 将接口侧 5V I2C 信号转换到 3.3V 域，U2 BMP280 是总线上的唯一传感器。原理图未包含本地主控、协处理器、外部存储器、晶振、射频、音频、电池或充电电路。

- 参数与网络：`external_controller=via J1 IIC_SCL/IIC_SDA`；`sensor=U2 BMP280`；`regulator=U1 HT7533`；`level_shifters=Q1/Q2 BSS138`；`local_controller=null`；`storage=null`；`battery=null`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页完整单页原理图：J1、U1、Q1/Q2、U2 及 R1-R4/C1/C2/C4

## 电源

### +5V 至 +3.3V 稳压路径

J1 pin3 VCC 接 +5V；+5V 进入 U1 HT7533 VIN pin2，U1 VOUT pin3 输出 +3.3V，U1 GND 接地。C1 10uF 跨接 +5V/GND，C2 10uF 跨接 +3.3V/GND。原理图未显示稳压器使能、负载开关、电源监测、充电或电池路径。

- 参数与网络：`input_connector=J1 pin3 VCC`；`input_rail=+5V`；`regulator=U1 HT7533`；`vin=pin2 +5V`；`vout=pin3 +3.3V`；`input_capacitor=C1 10uF`；`output_capacitor=C2 10uF`；`enable=null`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页 J1 pin3 +5V 与上中部 U1 HT7533、C1/C2 电源网络

## 接口

### J1 Grove I2C 接口针脚

J1 HY-2.0_IIC 的 pin1 为 IIC_SCL 并连接 SCL 网络，pin2 为 IIC_SDA 并连接 SDA 网络，pin3 VCC 接 +5V，pin4 GND 接地。SCL/SDA 是经 MOSFET 电平转换的开漏总线信号，接口侧由 R2/R1 上拉到 +5V；外部主机提供 I2C 控制。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=IIC_SCL -> SCL, interface side +5V pull-up, bidirectional bus clock path`；`pin2=IIC_SDA -> SDA, interface side +5V pull-up, bidirectional data`；`pin3=VCC -> +5V, power input`；`pin4=GND -> GND, power return`；`host=external I2C controller`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页右侧 J1 pin1-pin4 标注及左侧 SDA/SCL 的 R1/R2 +5V 上拉

## 总线

### SDA/SCL I2C 电平转换与上拉

SDA 通过 Q1 BSS138、SCL 通过 Q2 BSS138 跨接 5V 接口域与 3.3V 传感器域，两管 gate 共接 +3.3V。R1/R2 各 4.7KΩ 分别将接口侧 SDA/SCL 上拉到 +5V，R3/R4 各 4.7KΩ 分别将传感器侧 SDA/SCL 上拉到 +3.3V。

- 参数与网络：`sda_shift=J1 SDA -> Q1 BSS138 -> U2 SDI pin3`；`scl_shift=J1 SCL -> Q2 BSS138 -> U2 SCK pin4`；`mosfet_gates=+3.3V`；`high_side_pullups=R1 SDA,R2 SCL,4.7KΩ to +5V`；`low_side_pullups=R3 SDA,R4 SCL,4.7KΩ to +3.3V`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页左中部 SDA/SCL、Q1/Q2 BSS138、R1-R4 4.7KΩ 与 +5V/+3.3V 网络

## GPIO 与控制信号

### BMP280 CSB 与 SDO 绑带

U2 CSB pin2 与 Vdd/Vddio 一同连接 +3.3V；U2 SDO pin5 与 GND pin1/pin7 一同连接 GND。原理图因此明确给出 CSB 高电平和 SDO 低电平的硬件绑带，但未在图中标注由此对应的协议模式或数值地址。

- 参数与网络：`csb=U2 pin2 -> +3.3V`；`sdo=U2 pin5 -> GND`；`address_select_level=low`；`numeric_address_on_schematic=null`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页 U2 左侧 CSB pin2 接 +3.3V，右侧 SDO pin5 与 GND pin1/pin7 共接地

## 保护电路

### 外部接口保护配置

完整单页原理图在 J1 的 +5V、SCL、SDA 和 GND 路径上未显示 TVS/ESD 二极管、保险丝、反接保护或串联限流器件；可见的 Q1/Q2 BSS138 用于电平转换。

- 参数与网络：`connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_current_limit=null`；`level_shift=Q1/Q2 BSS138`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页完整单页，J1 至 U1/Q1/Q2 的所有可见输入和信号路径

## 关键网络

### 关键网络索引

关键网络为 +5V、+3.3V、GND、SDA 和 SCL。+5V 来自 J1 pin3并供给 U1 与接口侧上拉；+3.3V 由 U1 输出并供给 U2、Q1/Q2 gate 和传感器侧上拉；SDA/SCL 经 Q1/Q2 从 J1 连接至 U2。

- 参数与网络：`+5V=J1 pin3,U1 VIN pin2,C1,R1,R2`；`+3.3V=U1 VOUT pin3,C2,C4,U2 Vdd/Vddio/CSB,Q1/Q2 gate,R3,R4`；`GND=J1 pin4,U1 GND,U2 pin1/pin7/SDO,C1/C2/C4`；`SDA=J1 pin2,R1,Q1,R3,U2 SDI pin3`；`SCL=J1 pin1,R2,Q2,R4,U2 SCK pin4`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页全部同名 +5V/+3.3V/GND/SDA/SCL 网络与连接点

## 传感器

### BMP280 电源与数字接口连接

U2 BMP280 的 Vdd pin8 与 Vddio pin6 接 +3.3V，GND pin1/pin7 接地；SCK pin4 接转换后的 SCL，SDI pin3 接转换后的 SDA。C4 100nF 从 +3.3V 接 GND，作为传感器电源去耦。

- 参数与网络：`part_number=U2 BMP280`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`ground=pin1,pin7 GND`；`scl=pin4 SCK`；`sda=pin3 SDI`；`decoupling=C4 100nF +3.3V-to-GND`
- 证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页中下部 U2 BMP280 各标注引脚与右中部 C4 100nF

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini BPS 系统架构 | `external_controller=via J1 IIC_SCL/IIC_SDA`；`sensor=U2 BMP280`；`regulator=U1 HT7533`；`level_shifters=Q1/Q2 BSS138`；`local_controller=null`；`storage=null`；`battery=null` |
| 电源 | +5V 至 +3.3V 稳压路径 | `input_connector=J1 pin3 VCC`；`input_rail=+5V`；`regulator=U1 HT7533`；`vin=pin2 +5V`；`vout=pin3 +3.3V`；`input_capacitor=C1 10uF`；`output_capacitor=C2 10uF`；`enable=null` |
| 接口 | J1 Grove I2C 接口针脚 | `connector=J1 HY-2.0_IIC`；`pin1=IIC_SCL -> SCL, interface side +5V pull-up, bidirectional bus clock path`；`pin2=IIC_SDA -> SDA, interface side +5V pull-up, bidirectional data`；`pin3=VCC -> +5V, power input`；`pin4=GND -> GND, power return`；`host=external I2C controller` |
| 总线 | SDA/SCL I2C 电平转换与上拉 | `sda_shift=J1 SDA -> Q1 BSS138 -> U2 SDI pin3`；`scl_shift=J1 SCL -> Q2 BSS138 -> U2 SCK pin4`；`mosfet_gates=+3.3V`；`high_side_pullups=R1 SDA,R2 SCL,4.7KΩ to +5V`；`low_side_pullups=R3 SDA,R4 SCL,4.7KΩ to +3.3V` |
| 传感器 | BMP280 电源与数字接口连接 | `part_number=U2 BMP280`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`ground=pin1,pin7 GND`；`scl=pin4 SCK`；`sda=pin3 SDI`；`decoupling=C4 100nF +3.3V-to-GND` |
| GPIO 与控制信号 | BMP280 CSB 与 SDO 绑带 | `csb=U2 pin2 -> +3.3V`；`sdo=U2 pin5 -> GND`；`address_select_level=low`；`numeric_address_on_schematic=null` |
| 关键网络 | 关键网络索引 | `+5V=J1 pin3,U1 VIN pin2,C1,R1,R2`；`+3.3V=U1 VOUT pin3,C2,C4,U2 Vdd/Vddio/CSB,Q1/Q2 gate,R3,R4`；`GND=J1 pin4,U1 GND,U2 pin1/pin7/SDO,C1/C2/C4`；`SDA=J1 pin2,R1,Q1,R3,U2 SDI pin3`；`SCL=J1 pin1,R2,Q2,R4,U2 SCK pin4` |
| 保护电路 | 外部接口保护配置 | `connector=J1`；`esd_tvs=null`；`fuse=null`；`reverse_polarity=null`；`series_current_limit=null`；`level_shift=Q1/Q2 BSS138` |
| 总线地址 | BMP280 I2C 地址 | `documented_address=0x76`；`device=U2 BMP280`；`address_select=SDO pin5 -> GND`；`schematic_numeric_address=null` |
| 传感器 | 正文中的压力与温度测量规格 | `documented_measurements=pressure,temperature`；`documented_pressure_range=300-1100hPa`；`documented_relative_accuracy=0.12hPa`；`schematic_performance_parameters=null`；`sampling_rate=null`；`calibration=null` |

## 待确认事项

- `address.documented-0x76`：产品正文将 BMP280 I2C 地址列为 0x76；原理图可确认 U2 SDO pin5 接 GND，但图中没有直接标注 0x76，也没有 datasheet 地址表或总线扫描结果。（证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页 U2 SDO pin5 接 GND，整页未出现 0x76 地址文字）
- `sensor.documented-performance`：产品正文称本单元可测气压和温度，压力范围为 300-1100hPa、相对精度为 0.12hPa；原理图只确认 BMP280 型号及其电气连接，没有印出测量范围、精度、温度范围、采样率或校准条件。（证据：图 c1bee9d562a5 / 第 1 页 / 第 1 页 U2 标为 BMP280，整页无量程、精度、采样率或校准参数）
- `review.bmp280-address`：请用 BMP280 datasheet 或上电总线扫描确认 SDO 接地时本单元的 7 位 I2C 地址是否为 0x76。；原因：原理图只显示 SDO 低电平绑带，没有直接标注数值地址。
- `review.bmp280-performance`：请以当前 BOM 对应的 BMP280 datasheet 或校准测试确认 300-1100hPa 量程、0.12hPa 相对精度及适用条件。；原因：这些性能参数只见于产品正文，未在原理图中给出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c1bee9d562a5a0af4b4248a9adf318e831eab291d23eed43d57e319f2a0a25f3` | `https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_sch_01.webp` |

---

源文档：`zh_CN/unit/bps.md`

源文档 SHA-256：`f9844ad139af48f5505648624e50af2ba9dd02f9bc6ed35e872c9bae79bc72d6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
