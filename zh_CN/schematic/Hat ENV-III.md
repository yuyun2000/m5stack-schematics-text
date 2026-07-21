# Hat ENV-III 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ENV-III |
| SKU | U053-D |
| 产品 ID | `hat-env-iii-5c419dff5145` |
| 源文档 | `zh_CN/hat/hat_envIII.md` |

## 概述

Hat ENV-III 原理图将 SHT30-DIS-B（U1）、BMM150（U2）和 QMP6988（U3）并接到 P1 STICKIO 的 SCL/G26 与 SDA/G0，总线通过 R1/R2 各 4.7KΩ 上拉至 +3.3V。SHT30 ADDR 接 GND，QMP6988 CSB 接 +3.3V 且 SDO 接 GND，BMM150 PS/VDDIO 接 +3.3V 且 CSB 接 GND。产品正文仅列 SHT30 与 QMP6988，未提及原理图中的 BMM150，因此 BMM150 的实际装配状态需要确认；页面也未直接标注 0x44 和 0x56。

## 检索关键词

`Hat ENV-III`、`U053-D`、`SHT30-DIS-B`、`QMP6988`、`BMM150`、`U1`、`U2`、`U3`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`+3.3V`、`STICKIO`、`ADDR`、`CSB`、`SDO`、`PS`、`VDDIO`、`0x44`、`0x56`、`R1 4.7KΩ`、`R2 4.7KΩ`、`温湿度`、`气压`、`磁力计`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 温湿度传感器，使用 +3.3V 与 SCL/SDA，ADDR 接 GND | 图 6ceea6784152 / 第 1 页 / 页面左上 U1 SHT30-DIS-B：SDA/SCL/VDD/GND/ADDR/ALERT/nRESET 引脚 |
| U2 | BMM150 | 原理图中绘制的磁力计，使用 +3.3V 与 SCL/SDA，PS/VDDIO 接 +3.3V、CSB 接 GND | 图 6ceea6784152 / 第 1 页 / 页面右下 U2 BMM150：GND/INT/DRDY/VDD/PS/VDDIO/SCK/SDI/CSB 球位 |
| U3 | QMP6988 | 气压传感器，使用 +3.3V 与 SCL/SDA，CSB 接 +3.3V、SDO 接 GND | 图 6ceea6784152 / 第 1 页 / 页面左下 U3 QMP6988：SCK/SDI/CSB/SDO/Vdd/Vddio/GND 引脚 |
| P1 | STICKIO | 8 针主机接口，使用 GND、G26/SCL、G0/SDA 和 3V3/+3.3V | 图 6ceea6784152 / 第 1 页 / 页面右上 P1 STICKIO：1~8 脚 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN |
| R1/R2 | 4.7KΩ / 4.7KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 6ceea6784152 / 第 1 页 / 页面上中 R1/R2：上端 +3.3V，下端分别连接 SCL/SDA |
| C1/C2/C3/C4 | 100nF / 100nF / 100nF / 100nF | 三颗传感器 +3.3V 供电的对地去耦电容 | 图 6ceea6784152 / 第 1 页 / 页面 C1~C4 均标注 100nF 并跨接 +3.3V 与 GND，分布在 U1/U3/U2 周围 |

## 系统结构

### Hat ENV-III

原理图中 U1 SHT30-DIS-B、U2 BMM150、U3 QMP6988 共享 SCL/SDA 与 +3.3V/GND，并通过 P1 STICKIO 连接主机。

- 参数与网络：`temperature_humidity=U1 SHT30-DIS-B`；`magnetometer_shown=U2 BMM150`；`pressure=U3 QMP6988`；`bus=SCL/SDA`；`supply=+3.3V`；`host=P1 STICKIO`
- 证据：图 6ceea6784152 / 第 1 页 / 全页 U1/U2/U3/P1 的 SCL/SDA/+3.3V/GND 同名网络

## 电源

### +3.3V 供电

P1.7 3V3 引入 +3.3V，供 U1 VDD、U3 Vdd/Vddio/CSB、U2 VDD/VDDIO/PS、R1/R2 与 C1~C4 使用。

- 参数与网络：`source=P1.7 3V3`；`SHT30=U1.5 VDD`；`QMP6988=U3.8 Vdd; U3.6 Vddio; U3.2 CSB`；`BMM150=U2.E5 VDD; U2.B2 VDDIO; U2.A1 PS`；`decoupling=C1/C2/C3/C4 100nF`
- 证据：图 6ceea6784152 / 第 1 页 / 全页 +3.3V 同名网络在 P1、U1、U2、U3、R1/R2、C1~C4 上的连接

## 接口

### P1 STICKIO

P1.1 接 GND，P1.3 G26 接 SCL，P1.5 G0 接 SDA，P1.7 3V3 接 +3.3V；P1.2 5VOUT、P1.4 G36、P1.6 BAT、P1.8 5VIN 标为未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC`
- 证据：图 6ceea6784152 / 第 1 页 / 页面右上 P1 引脚编号、名称、左侧网络及 2/4/6/8 脚未连接标记

## 总线

### SCL/SDA

SCL 连接 P1.3 G26、U1.4、U3.4 和 U2.A3；SDA 连接 P1.5 G0、U1.1、U3.3 和 U2.B4。

- 参数与网络：`scl=P1.3 G26; U1.4; U3.4; U2.A3`；`sda=P1.5 G0; U1.1; U3.3; U2.B4`；`direction=bidirectional`
- 证据：图 6ceea6784152 / 第 1 页 / 全页 P1/U1/U2/U3 的 SCL/SDA 同名网络

### I2C 上拉

R1 4.7KΩ 将 SCL 上拉至 +3.3V，R2 4.7KΩ 将 SDA 上拉至 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`
- 证据：图 6ceea6784152 / 第 1 页 / 页面上中 R1/R2 与 SCL/SDA 连接点

## 时钟

### 时钟、复位与调试

该页未显示外部晶振、BOOT 或调试接口；U1 nRESET 未连接，U2 INT/DRDY 未连接。

- 参数与网络：`external_clock=not shown`；`boot=not shown`；`debug=not shown`；`SHT30_nRESET=U1.6 NC`；`BMM150_INT=U2.D2 NC`；`BMM150_DRDY=U2.D4 NC`
- 证据：图 6ceea6784152 / 第 1 页 / 全页无晶振/BOOT/调试；U1 nRESET 与 U2 INT/DRDY 旁为未连接短线

## 保护电路

### 接口保护

P1 到传感器的电源与 I2C 路径上未显示 TVS、保险丝、串联电阻或电平转换器。

- 参数与网络：`tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown`
- 证据：图 6ceea6784152 / 第 1 页 / 全页 P1/U1/U2/U3 的完整 +3.3V/GND/SCL/SDA 路径，仅见上拉与去耦

## 传感器

### U1 SHT30-DIS-B

U1.1 SDA、U1.4 SCL、U1.5 VDD 接 +3.3V；U1.2 ADDR、U1.7 R、U1.8 VSS、U1.9 dpad 接 GND，U1.3 ALERT 与 U1.6 nRESET 未连接。

- 参数与网络：`pin_1=SDA`；`pin_2=ADDR GND`；`pin_3=ALERT NC`；`pin_4=SCL`；`pin_5=VDD +3.3V`；`pin_6=nRESET NC`；`pin_7=R GND`；`pin_8=VSS GND`；`pin_9=dpad GND`
- 证据：图 6ceea6784152 / 第 1 页 / 页面左上 U1 各引脚、+3.3V/GND 连接及 ALERT/nRESET 短线

### U3 QMP6988

U3.4 SCK 接 SCL，U3.3 SDI 接 SDA；U3.2 CSB、U3.8 Vdd、U3.6 Vddio 接 +3.3V，U3.5 SDO、U3.1/U3.7 GND 接地。

- 参数与网络：`pin_1=GND`；`pin_2=CSB +3.3V`；`pin_3=SDI SDA`；`pin_4=SCK SCL`；`pin_5=SDO GND`；`pin_6=Vddio +3.3V`；`pin_7=GND`；`pin_8=Vdd +3.3V`
- 证据：图 6ceea6784152 / 第 1 页 / 页面左下 U3 QMP6988 的 1~8 脚与 +3.3V/GND/SCL/SDA 连接

### U2 BMM150

原理图明确绘制 U2 BMM150：A3 SCK 接 SCL、B4 SDI 接 SDA、A1 PS/B2 VDDIO/E5 VDD 接 +3.3V、A5 CSB 接 GND，INT/DRDY 未连接。

- 参数与网络：`part=BMM150`；`SCK=A3 SCL`；`SDI=B4 SDA`；`PS=A1 +3.3V`；`VDDIO=B2 +3.3V`；`VDD=E5 +3.3V`；`CSB=A5 GND`；`INT=D2 NC`；`DRDY=D4 NC`
- 证据：图 6ceea6784152 / 第 1 页 / 页面右下 U2 BMM150 球位名称、坐标与所有连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat ENV-III | `temperature_humidity=U1 SHT30-DIS-B`；`magnetometer_shown=U2 BMM150`；`pressure=U3 QMP6988`；`bus=SCL/SDA`；`supply=+3.3V`；`host=P1 STICKIO` |
| 接口 | P1 STICKIO | `pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC` |
| 总线 | SCL/SDA | `scl=P1.3 G26; U1.4; U3.4; U2.A3`；`sda=P1.5 G0; U1.1; U3.3; U2.B4`；`direction=bidirectional` |
| 总线 | I2C 上拉 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V` |
| 传感器 | U1 SHT30-DIS-B | `pin_1=SDA`；`pin_2=ADDR GND`；`pin_3=ALERT NC`；`pin_4=SCL`；`pin_5=VDD +3.3V`；`pin_6=nRESET NC`；`pin_7=R GND`；`pin_8=VSS GND`；`pin_9=dpad GND` |
| 传感器 | U3 QMP6988 | `pin_1=GND`；`pin_2=CSB +3.3V`；`pin_3=SDI SDA`；`pin_4=SCK SCL`；`pin_5=SDO GND`；`pin_6=Vddio +3.3V`；`pin_7=GND`；`pin_8=Vdd +3.3V` |
| 传感器 | U2 BMM150 | `part=BMM150`；`SCK=A3 SCL`；`SDI=B4 SDA`；`PS=A1 +3.3V`；`VDDIO=B2 +3.3V`；`VDD=E5 +3.3V`；`CSB=A5 GND`；`INT=D2 NC`；`DRDY=D4 NC` |
| 核心器件 | BMM150 装配状态 | `schematic_component=U2 BMM150`；`product_document_components=SHT30; QMP6988`；`population_status=not confirmed` |
| 总线地址 | SHT30 I2C 地址 | `documented_address=0x44`；`address_strap=U1.2 ADDR to GND`；`schematic_address_label=not shown` |
| 总线地址 | QMP6988 I2C 地址 | `documented_address=0x56`；`address_strap=U3.5 SDO to GND`；`schematic_address_label=not shown` |
| 电源 | +3.3V 供电 | `source=P1.7 3V3`；`SHT30=U1.5 VDD`；`QMP6988=U3.8 Vdd; U3.6 Vddio; U3.2 CSB`；`BMM150=U2.E5 VDD; U2.B2 VDDIO; U2.A1 PS`；`decoupling=C1/C2/C3/C4 100nF` |
| 保护电路 | 接口保护 | `tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown` |
| 时钟 | 时钟、复位与调试 | `external_clock=not shown`；`boot=not shown`；`debug=not shown`；`SHT30_nRESET=U1.6 NC`；`BMM150_INT=U2.D2 NC`；`BMM150_DRDY=U2.D4 NC` |

## 待确认事项

- `component.bmm150-population-status`：原理图包含完整的 U2 BMM150 电路，但产品正文的 ENV-III 功能与规格仅列 SHT30 和 QMP6988，无法确认量产 U053-D 是否实际装配 BMM150。（证据：图 6ceea6784152 / 第 1 页 / 页面右下完整 U2 BMM150 符号、供电、I2C 与 strap 电路）
- `address.sht30-0x44`：产品正文标注 SHT30 地址为 0x44；原理图确认 U1.2 ADDR 接 GND，但未直接标注 0x44，无法仅由该页确认数值映射。（证据：图 6ceea6784152 / 第 1 页 / 页面左上 U1.2 ADDR 接 GND，未见 0x44 文本）
- `address.qmp6988-0x56`：产品正文标注 QMP6988 地址为 0x56；原理图确认 U3.5 SDO 接 GND，但未直接标注 0x56，无法仅由该页确认数值映射。（证据：图 6ceea6784152 / 第 1 页 / 页面左下 U3.5 SDO 接 GND，未见 0x56 文本）
- `review.bmm150-population`：U053-D 量产板是否实际装配原理图中的 U2 BMM150？；原因：原理图包含完整 BMM150 电路，但产品正文和 ENV-III 功能规格未列出磁力计。
- `review.sht30-address`：U1 ADDR 接 GND 时对应的 SHT30 7 位地址是否为 0x44？；原因：原理图确认 strap，但未标注地址数值。
- `review.qmp6988-address`：U3 SDO 接 GND 时对应的 QMP6988 7 位地址是否为 0x56？；原因：原理图确认 SDO strap，但未标注地址数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6ceea678415280776abf6f158ac72f81855105f5aa3226425207d17db24e37ae` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_sch_01.webp` |

---

源文档：`zh_CN/hat/hat_envIII.md`

源文档 SHA-256：`aae4ca4ace933bef43a4a16e38db45d39e126712766c597ab8c2a680d3365c64`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
