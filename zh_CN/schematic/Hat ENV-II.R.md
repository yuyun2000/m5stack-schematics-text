# Hat ENV-II.R 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ENV-II.R |
| SKU | U053-C |
| 产品 ID | `hat-env-ii-r-da72c940f235` |
| 源文档 | `zh_CN/hat/hat_envII.R.md` |

## 概述

Hat ENV-II.R 原理图包含 U1 SHT30-DIS-B 温湿度传感器、U3 BMP280 气压传感器，以及同页绘制的 U2 BMM150 磁传感器，三者共享 SCL/SDA。StickIO 的 G26 与 G0 分别承载 SCL 与 SDA，R1/R2 各 4.7 kΩ 将总线上拉到 +3.3V。所有器件使用 3.3 V，C1 至 C4 各 100 nF 分别为传感器电源去耦；SHT30 与 BMM150 的中断类引脚未接到主机。

## 检索关键词

`Hat ENV-II.R`、`U053-C`、`SHT30-DIS-B`、`SHT30`、`BMP280`、`BMM150`、`I2C`、`0x44`、`0x76`、`SCL`、`SDA`、`G26`、`G0`、`STICKIO`、`P1`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`C4 100nF`、`ADDR GND`、`SDO GND`、`CSB +3.3V`、`ALERT`、`nRESET`、`INT`、`DRDY`、`temperature humidity pressure`、`magnetometer`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 共享 I2C 总线的温湿度传感器，ADDR 固定接 GND | 图 0c8a00a90b53 / 第 1 页 / 左上，U1 SHT30-DIS-B，VDD/SDA/SCL/ADDR/VSS/dpad |
| U3 | BMP280 | 共享 I2C 总线的气压传感器，CSB 上拉、SDO 接地配置 | 图 0c8a00a90b53 / 第 1 页 / 左下，U3 BMP280，SCK/SDI/SDO/CSB/Vdd/Vddio/GND |
| U2 | BMM150 | 原理图中共享 I2C 总线的磁传感器，INT 与 DRDY 未连接 | 图 0c8a00a90b53 / 第 1 页 / 右下，U2 BMM150，SCK/SDI/SDO/PS/CSB/VDD/VDDIO/INT/DRDY |
| P1 | STICKIO | M5Stick HAT 接口，提供 G26/SCL、G0/SDA、3V3 与 GND | 图 0c8a00a90b53 / 第 1 页 / 右上，P1 STICKIO pins 1-8 与 SCL/SDA/+3.3V/GND |
| R1/R2 | 4.7KΩ / 4.7KΩ | SCL 与 SDA 的 3.3 V 上拉电阻 | 图 0c8a00a90b53 / 第 1 页 / 上中，R1 4.7KΩ 从 SCL 到 +3.3V，R2 4.7KΩ 从 SDA 到 +3.3V |
| C1/C2 | 100nF / 100nF | SHT30 与 BMP280 的 3.3 V 电源去耦 | 图 0c8a00a90b53 / 第 1 页 / 左侧，C1、C2 均为 100nF，跨接 +3.3V 与 GND |
| C3/C4 | 100nF / 100nF | BMM150 VDDIO/PS 与 VDD 电源去耦 | 图 0c8a00a90b53 / 第 1 页 / 右下，C3、C4 均为 100nF，分别连接 BMM150 3.3 V 电源节点到 GND |

## 系统结构

### 多传感器架构

原理图将 U1 SHT30-DIS-B、U3 BMP280 和 U2 BMM150 接到同一 SCL/SDA 总线，并由 P1 STICKIO 提供 3.3 V、GND 和主机 I2C 信号。

- 参数与网络：`temperature_humidity=U1 SHT30-DIS-B`；`pressure=U3 BMP280`；`magnetic=U2 BMM150`；`bus=shared I2C`；`connector=P1 STICKIO`；`supply=+3.3V`
- 证据：图 0c8a00a90b53 / 第 1 页 / 整页：U1/U2/U3/P1 及公共 SCL/SDA/+3.3V/GND

## 电源

### 3.3 V 传感器电源

P1 pin7 3V3 形成 +3.3V 电源轨，为 U1、U2、U3 及 I2C 上拉供电；原理图未显示电源转换器、LDO、负载开关或电池路径。

- 参数与网络：`source=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1/U2/U3/R1/R2`；`converter=none shown`；`ldo=none shown`；`load_switch=none shown`
- 证据：图 0c8a00a90b53 / 第 1 页 / 整页 +3.3V 网络与 P1 pin7

### 传感器去耦

C1、C2、C3、C4 均为 100 nF 并连接在相应 +3.3V 电源节点与 GND 之间。

- 参数与网络：`sht30=C1 100nF`；`bmp280=C2 100nF`；`bmm150_vddio_ps=C3 100nF`；`bmm150_vdd=C4 100nF`
- 证据：图 0c8a00a90b53 / 第 1 页 / C1/C2/C3/C4 各 100nF 的 +3.3V-GND 连线

## 接口

### StickIO 引脚映射

P1 pin1 GND、pin3 G26/SCL、pin5 G0/SDA、pin7 3V3/+3.3V 被使用；pin2 5VOUT、pin4 G36、pin6 BAT、pin8 5VIN 标为未连接。

- 参数与网络：`pin1=GND`；`pin2=5VOUT NC`；`pin3=G26 SCL`；`pin4=G36 NC`；`pin5=G0 SDA`；`pin6=BAT NC`；`pin7=3V3 +3.3V`；`pin8=5VIN NC`；`logic_level=3.3V`
- 证据：图 0c8a00a90b53 / 第 1 页 / 右上，P1 STICKIO pins 1-8 与连线/NC 标记

## 总线

### 共享 I2C 总线

SCL 同时连接 U1 pin4、U3 pin4 SCK、U2 A3 SCK 与 P1 pin3 G26；SDA 同时连接 U1 pin1、U3 pin3 SDI、U2 B4 SDI 与 P1 pin5 G0。

- 参数与网络：`controller=external M5Stick host`；`scl_net=SCL`；`scl_gpio=P1 pin3 G26`；`scl_devices=U1 pin4; U3 pin4; U2 A3`；`sda_net=SDA`；`sda_gpio=P1 pin5 G0`；`sda_devices=U1 pin1; U3 pin3; U2 B4`
- 证据：图 0c8a00a90b53 / 第 1 页 / U1/U3/U2 的 SCL/SDA 网络标签与 P1 G26/G0 连线

### I2C 上拉

R1 4.7 kΩ 将 SCL 上拉到 +3.3V，R2 4.7 kΩ 将 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`logic_level=3.3V`
- 证据：图 0c8a00a90b53 / 第 1 页 / 上中，R1/R2 与 SCL/SDA/+3.3V

## 复位

### 复位与中断引脚

SHT30 nRESET 与 ALERT 未连接；BMM150 INT 与 DRDY 未连接，P1 未引出这些信号。

- 参数与网络：`sht30_reset=U1 pin6 nRESET NC`；`sht30_alert=U1 pin3 ALERT NC`；`bmm150_int=U2 D2 INT NC`；`bmm150_drdy=U2 D4 DRDY NC`
- 证据：图 0c8a00a90b53 / 第 1 页 / U1 ALERT/nRESET 开路与 U2 INT/DRDY 红色 NC 标记

## 传感器

### SHT30 温湿度传感器配置

U1 为 SHT30-DIS-B，VDD pin5 接 +3.3V，VSS pin8、ADDR pin2、R pin7 与 dpad pin9 接 GND；ALERT pin3 和 nRESET pin6 未连接。

- 参数与网络：`reference=U1`；`part_number=SHT30-DIS-B`；`vdd=pin5 +3.3V`；`ground=pins 2/7/8/9 GND`；`addr_level=GND`；`alert=pin3 NC`；`reset=pin6 nRESET NC`；`decoupling=C1 100nF`
- 证据：图 0c8a00a90b53 / 第 1 页 / 左上，U1 SHT30-DIS-B 全部引脚与 C1

### BMP280 气压传感器配置

U3 为 BMP280，Vdd pin8、Vddio pin6 和 CSB pin2 接 +3.3V，GND pins 1/7 与 SDO pin5 接 GND，SCK/SDI 分别连接 SCL/SDA。

- 参数与网络：`reference=U3`；`part_number=BMP280`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`csb=pin2 +3.3V`；`sdo=pin5 GND`；`grounds=pins 1/7 GND`；`sck=pin4 SCL`；`sdi=pin3 SDA`；`decoupling=C2 100nF`
- 证据：图 0c8a00a90b53 / 第 1 页 / 左下，U3 BMP280 引脚、+3.3V/GND 与 C2

### BMM150 磁传感器电路

U2 为 BMM150，SCK A3 与 SDI B4 接 SCL/SDA，PS A1、VDDIO B2、VDD E5 接 +3.3V，CSB A5 与 SDO C1 接 GND；INT D2、DRDY D4 未连接。

- 参数与网络：`reference=U2`；`part_number=BMM150`；`sck=A3 SCL`；`sdi=B4 SDA`；`ps=A1 +3.3V`；`vddio=B2 +3.3V`；`vdd=E5 +3.3V`；`csb=A5 GND`；`sdo=C1 GND`；`interrupt=D2 INT NC`；`data_ready=D4 DRDY NC`；`decoupling=C3/C4 100nF`
- 证据：图 0c8a00a90b53 / 第 1 页 / 右下，U2 BMM150 全部可见引脚与 C3/C4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 多传感器架构 | `temperature_humidity=U1 SHT30-DIS-B`；`pressure=U3 BMP280`；`magnetic=U2 BMM150`；`bus=shared I2C`；`connector=P1 STICKIO`；`supply=+3.3V` |
| 总线 | 共享 I2C 总线 | `controller=external M5Stick host`；`scl_net=SCL`；`scl_gpio=P1 pin3 G26`；`scl_devices=U1 pin4; U3 pin4; U2 A3`；`sda_net=SDA`；`sda_gpio=P1 pin5 G0`；`sda_devices=U1 pin1; U3 pin3; U2 B4` |
| 总线 | I2C 上拉 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`logic_level=3.3V` |
| 传感器 | SHT30 温湿度传感器配置 | `reference=U1`；`part_number=SHT30-DIS-B`；`vdd=pin5 +3.3V`；`ground=pins 2/7/8/9 GND`；`addr_level=GND`；`alert=pin3 NC`；`reset=pin6 nRESET NC`；`decoupling=C1 100nF` |
| 传感器 | BMP280 气压传感器配置 | `reference=U3`；`part_number=BMP280`；`vdd=pin8 +3.3V`；`vddio=pin6 +3.3V`；`csb=pin2 +3.3V`；`sdo=pin5 GND`；`grounds=pins 1/7 GND`；`sck=pin4 SCL`；`sdi=pin3 SDA`；`decoupling=C2 100nF` |
| 传感器 | BMM150 磁传感器电路 | `reference=U2`；`part_number=BMM150`；`sck=A3 SCL`；`sdi=B4 SDA`；`ps=A1 +3.3V`；`vddio=B2 +3.3V`；`vdd=E5 +3.3V`；`csb=A5 GND`；`sdo=C1 GND`；`interrupt=D2 INT NC`；`data_ready=D4 DRDY NC`；`decoupling=C3/C4 100nF` |
| 接口 | StickIO 引脚映射 | `pin1=GND`；`pin2=5VOUT NC`；`pin3=G26 SCL`；`pin4=G36 NC`；`pin5=G0 SDA`；`pin6=BAT NC`；`pin7=3V3 +3.3V`；`pin8=5VIN NC`；`logic_level=3.3V` |
| 电源 | 3.3 V 传感器电源 | `source=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1/U2/U3/R1/R2`；`converter=none shown`；`ldo=none shown`；`load_switch=none shown` |
| 电源 | 传感器去耦 | `sht30=C1 100nF`；`bmp280=C2 100nF`；`bmm150_vddio_ps=C3 100nF`；`bmm150_vdd=C4 100nF` |
| 复位 | 复位与中断引脚 | `sht30_reset=U1 pin6 nRESET NC`；`sht30_alert=U1 pin3 ALERT NC`；`bmm150_int=U2 D2 INT NC`；`bmm150_drdy=U2 D4 DRDY NC` |
| 总线地址 | SHT30 I2C 地址 | `claimed_address=0x44`；`schematic_addr_level=GND`；`address_table=not printed` |
| 总线地址 | BMP280 I2C 地址 | `claimed_address=0x76`；`schematic_csb=+3.3V`；`schematic_sdo=GND`；`address_table=not printed` |
| 总线地址 | BMM150 I2C 地址 | `reference=U2`；`schematic_csb=GND`；`schematic_sdo=GND`；`address=not printed` |
| 核心器件 | BMM150 装配状态 | `schematic_component=U2 BMM150`；`schematic_connection=powered shared I2C`；`document_component_list=SHT30 and BMP280 only`；`physical_population=not confirmed` |
| 传感器 | 环境测量范围与精度 | `claimed_temperature_range=-40 to 120C`；`claimed_temperature_accuracy=0-60C +/-0.2C`；`claimed_humidity=10-90% RH +/-2%`；`claimed_pressure=300-1100hPa +/-1hPa` |

## 待确认事项

- `address.sht30`：产品正文给出 SHT30 地址 0x44；原理图仅显示 ADDR 接 GND，未印出地址值或地址真值表。（证据：图 0c8a00a90b53 / 第 1 页 / U1 pin2 ADDR 接 GND，页面无 0x44 标注）
- `address.bmp280`：产品正文给出 BMP280 地址 0x76；原理图显示 CSB 接 +3.3V、SDO 接 GND，但未印出地址值或地址真值表。（证据：图 0c8a00a90b53 / 第 1 页 / U3 CSB/SDO 配置，页面无 0x76 标注）
- `address.bmm150`：原理图显示 BMM150 的 CSB 与 SDO 接 GND，但页面和产品正文均未给出其 I2C 地址。（证据：图 0c8a00a90b53 / 第 1 页 / U2 BMM150 CSB A5 与 SDO C1 接 GND，页面无地址）
- `component.bmm150-population`：原理图明确画出 U2 BMM150 完整供电和 I2C 连接，但 Hat ENV-II.R 产品正文只列 SHT30 与 BMP280，现有资料无法确认 U053-C 实物是否装配或启用 BMM150。（证据：图 0c8a00a90b53 / 第 1 页 / 右下，U2 BMM150 完整电路）
- `sensor.measurement-ratings`：产品正文列出温度、湿度与气压测量范围和精度，但这些数值未印在原理图页面中。（证据：图 0c8a00a90b53 / 第 1 页 / U1/U3 区域仅标型号、引脚和外围电路，无量程/精度数值）
- `review.sht30-address`：请用 SHT30 datasheet 确认 ADDR=GND 时的 7-bit I2C 地址是否为 0x44。；原因：原理图没有地址真值表或 0x44 标注。
- `review.bmp280-address`：请用 BMP280 datasheet 确认 CSB=3.3V、SDO=GND 时的 7-bit I2C 地址是否为 0x76。；原因：原理图没有地址真值表或 0x76 标注。
- `review.bmm150-address`：请用 BMM150 datasheet 确认 CSB=GND、SDO=GND 配置下的 I2C 地址。；原因：原理图和产品正文均未直接列出 BMM150 地址。
- `review.bmm150-population`：请用 U053-C BOM、装配图或实物确认 U2 BMM150 是否实际装配并作为产品功能开放。；原因：正式原理图包含 BMM150，但产品正文只描述 SHT30 与 BMP280。
- `review.measurement-ratings`：请用 SHT30/BMP280 datasheet 或产品测试规范复核量程与精度参数。；原因：量程和精度未印在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0c8a00a90b539c3997825638a5da4501931b37a0c911a7d132d466e35caf9eeb` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_sch_01.webp` |

---

源文档：`zh_CN/hat/hat_envII.R.md`

源文档 SHA-256：`3b0210796605425b990aa5d99cf0d595d03b97c0424d355fd9600a0c4b74c510`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
