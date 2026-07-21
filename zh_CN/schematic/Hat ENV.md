# Hat ENV 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ENV |
| SKU | U053 |
| 产品 ID | `hat-env-b52ddfec42a4` |
| 源文档 | `zh_CN/hat/hat-env.md` |

## 概述

Hat ENV 通过 P1 STICKIO 的 G26/SCL 与 G0/SDA 接入主机 I2C，总线由 R1/R2 4.7KΩ上拉到 +3.3V。U1 DHT12、U3 BMP280 和 U2 BMM150 共用该总线；BMP280 通过 CSB 拉高进入串行总线配置，BMM150 的 CSB/SDO 拉低并使用 SCK/SDI。三颗传感器均由 +3.3V 供电并配置本地 100nF 去耦。

## 检索关键词

`Hat ENV`、`U053`、`DHT12`、`BMP280`、`BMM150`、`I2C`、`DHT12 0x5C`、`BMM150 0x10`、`G26 SCL`、`G0 SDA`、`+3.3V`、`R1 4.7K`、`R2 4.7K`、`BMP280 CSB high`、`BMP280 SDO GND`、`BMM150 CSB GND`、`BMM150 SDO GND`、`STICKIO`、`temperature`、`humidity`、`pressure`、`magnetometer`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | DHT12 | I2C 温湿度传感器 | 图 5dc013de68a4 / 第 1 页 / 第1页网格 B2：U1 DHT12 pins1-4 |
| U3 | BMP280 | I2C 气压传感器 | 图 5dc013de68a4 / 第 1 页 / 第1页网格 C2：U3 BMP280 pins1-8 |
| U2 | BMM150 | I2C 三轴磁力传感器 | 图 5dc013de68a4 / 第 1 页 / 第1页网格 C3：U2 BMM150 A1-E5 |
| P1 | STICKIO | 主机 I2C、3.3V 与 GND 接口 | 图 5dc013de68a4 / 第 1 页 / 第1页网格 B3：P1 STICKIO pins1-8 |
| R1,R2 | 4.7KΩ | SCL 与 SDA 上拉到 +3.3V | 图 5dc013de68a4 / 第 1 页 / 第1页网格 A2：R1/R2 4.7KΩ |

## 系统结构

### Hat ENV 架构

P1 提供 +3.3V、GND、SCL 和 SDA，U1 DHT12、U3 BMP280、U2 BMM150 共用 I2C 总线并分别配置本地去耦。

- 参数与网络：`host=P1 STICKIO`；`sensors=U1 DHT12; U3 BMP280; U2 BMM150`；`bus=I2C SCL/SDA`；`rail=+3.3V`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页完整单页

## 电源

### 传感器 3.3V 供电

P1 pin7 提供 +3.3V，供给 DHT12、BMP280、BMM150 以及 I2C 上拉；C1-C4 均为 100nF 对地去耦。

- 参数与网络：`input=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1,U2,U3,R1,R2`；`decoupling=C1,C2,C3,C4 100nF`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 +3.3V rails and C1-C4

## 接口

### P1 STICKIO 接口

P1 pin1 为 GND、pin3 G26 为 SCL、pin5 G0 为 SDA、pin7 3V3 接 +3.3V；pins2 5VOUT、4 G36、6 BAT、8 5VIN 未接入本页功能网络。

- 参数与网络：`pin1=GND`；`pin2=5VOUT unused`；`pin3=G26 / SCL`；`pin4=G36 unused`；`pin5=G0 / SDA`；`pin6=BAT unused`；`pin7=3V3 / +3.3V`；`pin8=5VIN unused`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 B3：P1 pins1-8

## 总线

### 共享 I2C 总线

P1 pin3/G26 形成 SCL，P1 pin5/G0 形成 SDA；DHT12、BMP280 和 BMM150 均连接这两条网络，R1/R2 4.7KΩ分别上拉到 +3.3V。

- 参数与网络：`controller_connector=P1`；`scl=P1 pin3 G26`；`sda=P1 pin5 G0`；`devices=DHT12,BMP280,BMM150`；`pullup_scl=R1 4.7KΩ`；`pullup_sda=R2 4.7KΩ`；`logic_level=+3.3V`；`direction=bidirectional`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 P1 G26/G0、R1/R2 与 U1/U2/U3

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟输入器件。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### 接口保护可见性

本页未画 P1、SCL、SDA 或传感器电源上的 TVS、ESD、保险丝或串联保护器件。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页完整单页保护器件范围

## 传感器

### DHT12 连接

U1 DHT12 pin1 接 +3.3V，pin2 接 SDA，pin3 接 GND，pin4 接 SCL；C1 100nF 从 +3.3V 对地。

- 参数与网络：`device=U1 DHT12`；`pin1=+3.3V`；`pin2=SDA`；`pin3=GND`；`pin4=SCL`；`decoupling=C1 100nF`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 B2：U1/C1

### BMP280 I2C 配置

U3 BMP280 SCK pin4 接 SCL、SDI pin3 接 SDA；CSB pin2、Vdd pin8、Vddio pin6 接 +3.3V，SDO pin5 与 GND pins1/7 接地。

- 参数与网络：`device=U3 BMP280`；`scl=SCK pin4`；`sda=SDI pin3`；`csb=pin2 +3.3V`；`sdo=pin5 GND`；`supply=Vdd pin8; Vddio pin6 -> +3.3V`；`ground=pins1/7`；`decoupling=C2 100nF`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 C2：U3/C2

### BMM150 I2C 配置

U2 BMM150 SCK A3 接 SCL、SDI B4 接 SDA；CSB A5 与 SDO C1 接地，PS A1、VDDIO B2、VDD E5 接 +3.3V，INT D2 与 DRDY D4 未连接。

- 参数与网络：`device=U2 BMM150`；`scl=SCK A3`；`sda=SDI B4`；`csb=A5 GND`；`sdo=C1 GND`；`supply=PS A1; VDDIO B2; VDD E5 -> +3.3V`；`interrupt=INT D2 NC`；`data_ready=DRDY D4 NC`；`grounds=E1,E3,C5`；`decoupling=C3/C4 100nF`
- 证据：图 5dc013de68a4 / 第 1 页 / 第1页 C3：U2/C3/C4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat ENV 架构 | `host=P1 STICKIO`；`sensors=U1 DHT12; U3 BMP280; U2 BMM150`；`bus=I2C SCL/SDA`；`rail=+3.3V` |
| 总线 | 共享 I2C 总线 | `controller_connector=P1`；`scl=P1 pin3 G26`；`sda=P1 pin5 G0`；`devices=DHT12,BMP280,BMM150`；`pullup_scl=R1 4.7KΩ`；`pullup_sda=R2 4.7KΩ`；`logic_level=+3.3V`；`direction=bidirectional` |
| 传感器 | DHT12 连接 | `device=U1 DHT12`；`pin1=+3.3V`；`pin2=SDA`；`pin3=GND`；`pin4=SCL`；`decoupling=C1 100nF` |
| 传感器 | BMP280 I2C 配置 | `device=U3 BMP280`；`scl=SCK pin4`；`sda=SDI pin3`；`csb=pin2 +3.3V`；`sdo=pin5 GND`；`supply=Vdd pin8; Vddio pin6 -> +3.3V`；`ground=pins1/7`；`decoupling=C2 100nF` |
| 传感器 | BMM150 I2C 配置 | `device=U2 BMM150`；`scl=SCK A3`；`sda=SDI B4`；`csb=A5 GND`；`sdo=C1 GND`；`supply=PS A1; VDDIO B2; VDD E5 -> +3.3V`；`interrupt=INT D2 NC`；`data_ready=DRDY D4 NC`；`grounds=E1,E3,C5`；`decoupling=C3/C4 100nF` |
| 总线地址 | DHT12 与 BMM150 I2C 地址 | `DHT12=0x5C`；`BMM150=0x10`；`explicit_address_text_on_schematic=false`；`bmm150_sdo=GND` |
| 接口 | P1 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT unused`；`pin3=G26 / SCL`；`pin4=G36 unused`；`pin5=G0 / SDA`；`pin6=BAT unused`；`pin7=3V3 / +3.3V`；`pin8=5VIN unused` |
| 电源 | 传感器 3.3V 供电 | `input=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1,U2,U3,R1,R2`；`decoupling=C1,C2,C3,C4 100nF` |
| 保护电路 | 接口保护可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- `address.documented-sensors`：产品正文标称 DHT12 地址 0x5C、BMM150 地址 0x10；原理图显示两器件的总线及 BMM150 地址选择连接，但未打印地址数值。（证据：图 5dc013de68a4 / 第 1 页 / 第1页 U1 DHT12 与 U2 BMM150 SDO/CSB）
- `review.sensor-addresses`：U053 当前 DHT12 与 BMM150 的 I2C 地址是否分别固定为 0x5C 和 0x10？；原因：地址来自产品正文，原理图未打印地址数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5dc013de68a40d38e6cc019f62c41d7c5d6f2e96f9e9ad096b27a1674694554e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/857/StickHat_ENV_page_01.png` |

---

源文档：`zh_CN/hat/hat-env.md`

源文档 SHA-256：`3c6c481b7b231e92c4423979794aceeba7aa39f28104c59c464c74fe196ab04f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
