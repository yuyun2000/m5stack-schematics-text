# Hat ENV-II 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ENV-II |
| SKU | U053-B |
| 产品 ID | `hat-env-ii-37219b0722b8` |
| 源文档 | `zh_CN/hat/hat_envII.md` |

## 概述

Hat ENV-II 将 SHT30-DIS-B（U1）、BMM150（U2）和 BMP280（U3）并接到由 P1 STICKIO 引出的 SCL/G26 与 SDA/G0 总线，R1/R2 各 4.7KΩ 将总线上拉至 +3.3V。三颗传感器均使用 +3.3V，并分别配置地址/接口 strap：SHT30 ADDR 接 GND、BMP280 CSB 接 +3.3V 且 SDO 接 GND、BMM150 PS/VDDIO 接 +3.3V 且 CSB 接 GND。页面未直接标注 0x44、0x76、0x10 地址值，也未显示电源转换、外部时钟或接口保护器件。

## 检索关键词

`Hat ENV-II`、`U053-B`、`SHT30-DIS-B`、`BMP280`、`BMM150`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`+3.3V`、`STICKIO`、`ADDR`、`CSB`、`SDO`、`PS`、`VDDIO`、`0x44`、`0x76`、`0x10`、`R1 4.7KΩ`、`R2 4.7KΩ`、`温湿度`、`气压`、`磁力计`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 温湿度传感器，使用 +3.3V 与 SCL/SDA，ADDR 接 GND | 图 2ead7f3643cc / 第 1 页 / 页面左上 U1 SHT30-DIS-B：SDA/SCL/VDD/GND/ADDR/ALERT/nRESET 引脚 |
| U2 | BMM150 | 磁力计，使用 +3.3V 与 SCL/SDA，PS/VDDIO 接 +3.3V、CSB 接 GND | 图 2ead7f3643cc / 第 1 页 / 页面右下 U2 BMM150：GND/INT/DRDY/VDD/PS/VDDIO/SCK/SDI/CSB 球位 |
| U3 | BMP280 | 气压传感器，使用 +3.3V 与 SCL/SDA，CSB 接 +3.3V、SDO 接 GND | 图 2ead7f3643cc / 第 1 页 / 页面左下 U3 BMP280：SCK/SDI/CSB/SDO/Vdd/Vddio/GND 引脚 |
| P1 | STICKIO | 8 针主机接口，使用 GND、G26/SCL、G0/SDA 和 3V3/+3.3V | 图 2ead7f3643cc / 第 1 页 / 页面右上 P1 STICKIO：1~8 脚 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN |
| R1/R2 | 4.7KΩ / 4.7KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 2ead7f3643cc / 第 1 页 / 页面上中 R1/R2：上端 +3.3V，下端分别连接 SCL/SDA |
| C1/C2/C3/C4 | 100nF / 100nF / 100nF / 100nF | 三颗传感器 +3.3V 供电的对地去耦电容 | 图 2ead7f3643cc / 第 1 页 / 页面 C1、C2、C3、C4 均标注 100nF 并跨接 +3.3V 与 GND，分布在 U1/U3/U2 周围 |

## 系统结构

### Hat ENV-II

U1 SHT30-DIS-B、U2 BMM150、U3 BMP280 共享 SCL/SDA 与 +3.3V/GND，并通过 P1 STICKIO 连接主机。

- 参数与网络：`temperature_humidity=U1 SHT30-DIS-B`；`magnetometer=U2 BMM150`；`pressure=U3 BMP280`；`bus=SCL/SDA`；`supply=+3.3V`；`host=P1 STICKIO`
- 证据：图 2ead7f3643cc / 第 1 页 / 全页 U1/U2/U3/P1 的 SCL/SDA/+3.3V/GND 同名网络

## 电源

### +3.3V 传感器供电

P1.7 3V3 引入 +3.3V，供 U1 VDD、U3 Vdd/Vddio/CSB、U2 VDD/VDDIO/PS、R1/R2 与 C1~C4 使用。

- 参数与网络：`source=P1.7 3V3`；`SHT30=U1.5 VDD`；`BMP280=U3.8 Vdd; U3.6 Vddio; U3.2 CSB`；`BMM150=U2.E5 VDD; U2.B2 VDDIO; U2.A1 PS`；`pullups=R1/R2`；`decoupling=C1/C2/C3/C4`
- 证据：图 2ead7f3643cc / 第 1 页 / 全页 +3.3V 同名网络在 P1、U1、U2、U3、R1/R2、C1~C4 上的连接

### 传感器去耦

C1、C2、C3、C4 均为 100nF，并分别布置在 SHT30、BMP280 及 BMM150 的 +3.3V 供电区域对地。

- 参数与网络：`C1=100nF +3.3V-GND`；`C2=100nF +3.3V-GND`；`C3=100nF VDDIO rail-GND`；`C4=100nF VDD rail-GND`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面中各 C1~C4 100nF 电容及其 +3.3V/GND 符号

## 接口

### P1 STICKIO

P1.1 接 GND，P1.3 G26 接 SCL，P1.5 G0 接 SDA，P1.7 3V3 接 +3.3V；P1.2 5VOUT、P1.4 G36、P1.6 BAT、P1.8 5VIN 标为未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面右上 P1 的引脚编号、名称、左侧网络及 2/4/6/8 脚未连接标记

## 总线

### SCL/SDA

SCL 连接 P1.3 G26、U1.4、U3.4 和 U2.A3；SDA 连接 P1.5 G0、U1.1、U3.3 和 U2.B4。

- 参数与网络：`scl=P1.3 G26; U1.4; U3.4; U2.A3`；`sda=P1.5 G0; U1.1; U3.3; U2.B4`；`direction=bidirectional`
- 证据：图 2ead7f3643cc / 第 1 页 / 全页 P1/U1/U2/U3 的 SCL/SDA 同名网络标签

### I2C 上拉网络

R1 4.7KΩ 将 SCL 上拉到 +3.3V，R2 4.7KΩ 将 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面上中 R1/R2 与 SCL/SDA 的连接点

## 时钟

### 时钟、复位与调试

该页未显示外部晶振、时钟源、BOOT 或调试接口；U1 nRESET 未连接，U2 INT/DRDY 未连接。

- 参数与网络：`external_clock=not shown`；`boot=not shown`；`debug=not shown`；`SHT30_nRESET=U1.6 NC`；`BMM150_INT=U2.D2 NC`；`BMM150_DRDY=U2.D4 NC`
- 证据：图 2ead7f3643cc / 第 1 页 / 全页无晶振/BOOT/调试；U1 nRESET 与 U2 INT/DRDY 旁为未连接短线

## 保护电路

### 外部接口保护

P1 到三颗传感器的电源与 I2C 路径上未显示 TVS、保险丝、串联电阻或电平转换器。

- 参数与网络：`tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown`
- 证据：图 2ead7f3643cc / 第 1 页 / 全页 P1/U1/U2/U3 的完整 +3.3V/GND/SCL/SDA 路径，仅见上拉和去耦

## 传感器

### U1 SHT30-DIS-B

U1.1 SDA、U1.4 SCL、U1.5 VDD 接 +3.3V；U1.2 ADDR、U1.7 R、U1.8 VSS、U1.9 dpad 接 GND，U1.3 ALERT 与 U1.6 nRESET 未连接。

- 参数与网络：`pin_1=SDA`；`pin_2=ADDR GND`；`pin_3=ALERT NC`；`pin_4=SCL`；`pin_5=VDD +3.3V`；`pin_6=nRESET NC`；`pin_7=R GND`；`pin_8=VSS GND`；`pin_9=dpad GND`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面左上 U1 各引脚、+3.3V/GND 连接及 ALERT/nRESET 短线

### U3 BMP280

U3.4 SCK 接 SCL，U3.3 SDI 接 SDA；U3.2 CSB、U3.8 Vdd、U3.6 Vddio 接 +3.3V，U3.5 SDO、U3.1/U3.7 GND 接地。

- 参数与网络：`pin_1=GND`；`pin_2=CSB +3.3V`；`pin_3=SDI SDA`；`pin_4=SCK SCL`；`pin_5=SDO GND`；`pin_6=Vddio +3.3V`；`pin_7=GND`；`pin_8=Vdd +3.3V`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面左下 U3 BMP280 的 1~8 脚与 +3.3V/GND/SCL/SDA 连接

### U2 BMM150

U2.A3 SCK 接 SCL，U2.B4 SDI 接 SDA；A1 PS 与 B2 VDDIO 接 +3.3V，A5 CSB 接 GND，E5 VDD 接 +3.3V；D2 INT、D4 DRDY 未连接，多路 GND 球位接地。

- 参数与网络：`A1=PS +3.3V`；`B2=VDDIO +3.3V`；`A3=SCK SCL`；`B4=SDI SDA`；`A5=CSB GND`；`E5=VDD +3.3V`；`D2=INT NC`；`D4=DRDY NC`；`ground_balls=C1, E1, E3, C5`
- 证据：图 2ead7f3643cc / 第 1 页 / 页面右下 U2 BMM150 球位名称、坐标与 +3.3V/GND/SCL/SDA/NC 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat ENV-II | `temperature_humidity=U1 SHT30-DIS-B`；`magnetometer=U2 BMM150`；`pressure=U3 BMP280`；`bus=SCL/SDA`；`supply=+3.3V`；`host=P1 STICKIO` |
| 接口 | P1 STICKIO | `pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC` |
| 总线 | SCL/SDA | `scl=P1.3 G26; U1.4; U3.4; U2.A3`；`sda=P1.5 G0; U1.1; U3.3; U2.B4`；`direction=bidirectional` |
| 总线 | I2C 上拉网络 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V` |
| 传感器 | U1 SHT30-DIS-B | `pin_1=SDA`；`pin_2=ADDR GND`；`pin_3=ALERT NC`；`pin_4=SCL`；`pin_5=VDD +3.3V`；`pin_6=nRESET NC`；`pin_7=R GND`；`pin_8=VSS GND`；`pin_9=dpad GND` |
| 传感器 | U3 BMP280 | `pin_1=GND`；`pin_2=CSB +3.3V`；`pin_3=SDI SDA`；`pin_4=SCK SCL`；`pin_5=SDO GND`；`pin_6=Vddio +3.3V`；`pin_7=GND`；`pin_8=Vdd +3.3V` |
| 传感器 | U2 BMM150 | `A1=PS +3.3V`；`B2=VDDIO +3.3V`；`A3=SCK SCL`；`B4=SDI SDA`；`A5=CSB GND`；`E5=VDD +3.3V`；`D2=INT NC`；`D4=DRDY NC`；`ground_balls=C1, E1, E3, C5` |
| 总线地址 | SHT30 I2C 地址 | `documented_address=0x44`；`address_strap=U1.2 ADDR to GND`；`schematic_address_label=not shown` |
| 总线地址 | BMP280 I2C 地址 | `documented_address=0x76`；`address_strap=U3.5 SDO to GND`；`schematic_address_label=not shown` |
| 总线地址 | BMM150 I2C 地址 | `documented_address=0x10`；`interface_straps=PS +3.3V; CSB GND`；`schematic_address_label=not shown` |
| 电源 | +3.3V 传感器供电 | `source=P1.7 3V3`；`SHT30=U1.5 VDD`；`BMP280=U3.8 Vdd; U3.6 Vddio; U3.2 CSB`；`BMM150=U2.E5 VDD; U2.B2 VDDIO; U2.A1 PS`；`pullups=R1/R2`；`decoupling=C1/C2/C3/C4` |
| 电源 | 传感器去耦 | `C1=100nF +3.3V-GND`；`C2=100nF +3.3V-GND`；`C3=100nF VDDIO rail-GND`；`C4=100nF VDD rail-GND` |
| 保护电路 | 外部接口保护 | `tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown` |
| 时钟 | 时钟、复位与调试 | `external_clock=not shown`；`boot=not shown`；`debug=not shown`；`SHT30_nRESET=U1.6 NC`；`BMM150_INT=U2.D2 NC`；`BMM150_DRDY=U2.D4 NC` |

## 待确认事项

- `address.sht30-0x44`：产品正文标注 SHT30 地址为 0x44；原理图可确认 U1.2 ADDR 接 GND，但页面未直接标注 0x44，无法仅由原理图确认数值映射。（证据：图 2ead7f3643cc / 第 1 页 / 页面左上 U1.2 ADDR 接 GND，未见 0x44 文本）
- `address.bmp280-0x76`：产品正文标注 BMP280 地址为 0x76；原理图可确认 U3.5 SDO 接 GND，但页面未直接标注 0x76，无法仅由原理图确认数值映射。（证据：图 2ead7f3643cc / 第 1 页 / 页面左下 U3.5 SDO 接 GND，未见 0x76 文本）
- `address.bmm150-0x10`：产品正文标注 BMM150 地址为 0x10；原理图显示其 I2C 接口 strap，但未标注 0x10 或地址选择数值，无法仅由该页确认地址。（证据：图 2ead7f3643cc / 第 1 页 / 页面右下 U2 PS/CSB/SCK/SDI 配置，未见 0x10 文本）
- `review.sht30-address`：U1 ADDR 接 GND 时对应的 SHT30 7 位地址是否为 0x44？；原因：原理图确认 strap，但未标注 strap 到地址数值的映射。
- `review.bmp280-address`：U3 SDO 接 GND 时对应的 BMP280 7 位地址是否为 0x76？；原因：原理图确认 SDO strap，但未标注地址数值。
- `review.bmm150-address`：BMM150 在图示 PS/CSB 配置下的 7 位 I2C 地址是否固定为 0x10？；原因：原理图显示 I2C 接口配置，但未标注地址数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2ead7f3643cc97ccf05873fc8a08725e17b7063561242581f9430264fa83dac4` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_sch_01.webp` |

---

源文档：`zh_CN/hat/hat_envII.md`

源文档 SHA-256：`c5ab34ff03203d77f18f0e6a1896cd0944f4bab016ee6e393d86c4f1d818870f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
