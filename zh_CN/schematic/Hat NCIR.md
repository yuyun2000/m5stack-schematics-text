# Hat NCIR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat NCIR |
| SKU | U061 |
| 产品 ID | `hat-ncir-bad0ce1008dc` |
| 源文档 | `zh_CN/hat/hat-ncir.md` |

## 概述

Hat NCIR 以 U1 MLX90614 红外温度传感器为核心，通过 P1 STICKIO 的 G26/SCL 与 G0/SDA 接入主机 I2C。U1 由 P1 pin7 的 +3.3V 供电，SCL/SDA 各由 4.7KΩ上拉，并配置 C1 100nF 去耦。图纸没有其他控制器、存储、时钟或外部保护器件。

## 检索关键词

`Hat NCIR`、`U061`、`MLX90614`、`MLX90614ESF-AAA`、`I2C`、`0x5A`、`G26 SCL`、`G0 SDA`、`+3.3V`、`STICKIO`、`R1 4.7K`、`R2 4.7K`、`C1 100nF`、`infrared temperature`、`non-contact temperature`、`U1 pin1 SCL`、`U1 pin2 SDA`、`U1 pin3 VDD`、`U1 pin4 GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MLX90614 | I2C 非接触式红外温度传感器 | 图 e06ab04bca58 / 第 1 页 / 第1页网格 B2：U1 MLX90614 pins1-4 |
| P1 | STICKIO | 主机 I2C、3.3V 与 GND 接口 | 图 e06ab04bca58 / 第 1 页 / 第1页网格 B3：P1 STICKIO pins1-8 |
| R1,R2 | 4.7KΩ | SCL 与 SDA 上拉到 +3.3V | 图 e06ab04bca58 / 第 1 页 / 第1页网格 B2：R1/R2 4.7KΩ |
| C1 | 100nF | MLX90614 3.3V 电源去耦 | 图 e06ab04bca58 / 第 1 页 / 第1页网格 B2：C1 100nF |

## 系统结构

### Hat NCIR 架构

P1 提供 +3.3V、GND、SCL 和 SDA，U1 MLX90614 直接连接 I2C 总线，R1/R2 提供上拉，C1 提供本地去耦。

- 参数与网络：`sensor=U1 MLX90614`；`host=P1 STICKIO`；`bus=I2C`；`rail=+3.3V`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页完整单页

## 电源

### MLX90614 3.3V 电源

P1 pin7/3V3 连接 +3.3V并供给 U1 VDD pin3、R1/R2 上拉；C1 100nF 从 +3.3V 对地去耦。

- 参数与网络：`input=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1 pin3,R1,R2`；`decoupling=C1 100nF`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页 P1 pin7、U1 VDD、C1

## 接口

### P1 STICKIO 接口

P1 pin1 为 GND、pin3 G26 为 SCL、pin5 G0 为 SDA、pin7 3V3 接 +3.3V；pins2 5VOUT、4 G36、6 BAT、8 5VIN 未接入本页功能网络。

- 参数与网络：`pin1=GND`；`pin2=5VOUT unused`；`pin3=G26/SCL`；`pin4=G36 unused`；`pin5=G0/SDA`；`pin6=BAT unused`；`pin7=3V3/+3.3V`；`pin8=5VIN unused`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页 B3：P1 pins1-8

## 总线

### MLX90614 I2C 总线

P1 pin3/G26 形成 SCL并连接 U1 pin1，P1 pin5/G0 形成 SDA并连接 U1 pin2；R1/R2 4.7KΩ分别将 SCL/SDA 上拉到 +3.3V。

- 参数与网络：`scl=P1 pin3 G26 -> U1 pin1`；`sda=P1 pin5 G0 -> U1 pin2`；`pullup_scl=R1 4.7KΩ`；`pullup_sda=R2 4.7KΩ`；`logic_level=+3.3V`；`direction=bidirectional`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页 P1 G26/G0、R1/R2、U1 SCL/SDA

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟输入器件。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### 接口保护可见性

本页未画 P1、SCL、SDA 或 +3.3V 上的 TVS、ESD、保险丝或串联保护器件。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页完整单页保护器件范围

## 传感器

### MLX90614 连接

U1 MLX90614 pin1 为 SCL、pin2 为 SDA、pin3/VDD 接 +3.3V、pin4/GND 接地。

- 参数与网络：`device=U1 MLX90614`；`pin1=SCL`；`pin2=SDA`；`pin3=VDD / +3.3V`；`pin4=GND`
- 证据：图 e06ab04bca58 / 第 1 页 / 第1页 B2：U1 pins1-4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat NCIR 架构 | `sensor=U1 MLX90614`；`host=P1 STICKIO`；`bus=I2C`；`rail=+3.3V` |
| 传感器 | MLX90614 连接 | `device=U1 MLX90614`；`pin1=SCL`；`pin2=SDA`；`pin3=VDD / +3.3V`；`pin4=GND` |
| 总线 | MLX90614 I2C 总线 | `scl=P1 pin3 G26 -> U1 pin1`；`sda=P1 pin5 G0 -> U1 pin2`；`pullup_scl=R1 4.7KΩ`；`pullup_sda=R2 4.7KΩ`；`logic_level=+3.3V`；`direction=bidirectional` |
| 总线地址 | MLX90614 I2C 地址 | `device=U1 MLX90614`；`documented_address=0x5A`；`explicit_address_on_schematic=false` |
| 核心器件 | MLX90614 完整型号 | `schematic=MLX90614`；`documented=MLX90614ESF-AAA` |
| 电源 | MLX90614 3.3V 电源 | `input=P1 pin7 3V3`；`rail=+3.3V`；`loads=U1 pin3,R1,R2`；`decoupling=C1 100nF` |
| 接口 | P1 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT unused`；`pin3=G26/SCL`；`pin4=G36 unused`；`pin5=G0/SDA`；`pin6=BAT unused`；`pin7=3V3/+3.3V`；`pin8=5VIN unused` |
| 保护电路 | 接口保护可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- `address.mlx90614`：产品正文标称 MLX90614 I2C 地址为 0x5A；原理图显示 I2C 连接但未打印地址数值。（证据：图 e06ab04bca58 / 第 1 页 / 第1页 U1 SCL/SDA pins1/2）
- `component.mlx90614-variant`：原理图 U1 仅打印 MLX90614，产品正文标称 MLX90614ESF-AAA；图中未打印 ESF-AAA 后缀。（证据：图 e06ab04bca58 / 第 1 页 / 第1页 U1 下方 MLX90614 标注）
- `review.i2c-address`：U061 当前 MLX90614 的 I2C 地址是否固定为 0x5A？；原因：地址来自产品正文，原理图未打印地址数值。
- `review.sensor-variant`：U061 当前装配的完整传感器型号是否为 MLX90614ESF-AAA？；原因：原理图仅打印 MLX90614，完整后缀来自产品正文。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e06ab04bca58a33ca60e9509e668b5b4608ea53d5525537636f38d5f365d4843` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061-StickHat_NCIR-SCHE_page_01.png` |

---

源文档：`zh_CN/hat/hat-ncir.md`

源文档 SHA-256：`e1ff52f2d69d4cf22e9a59c36f94b1f150473e2af2f48e398b74b16400d39d71`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
