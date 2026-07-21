# Hat DLight 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat DLight |
| SKU | U134 |
| 产品 ID | `hat-dlight-620edc6f0f90` |
| 源文档 | `zh_CN/hat/hat_dlight.md` |

## 概述

Hat DLight 以 U1 BH1750FVI-TR 实现数字照度检测，原理图标注检测范围为 1 至 65535 lx。传感器由 +3.3V 供电，SCL 与 SDA 构成 I2C 信号，ADDR 接 GND；SCL、DVI、SDA 各通过 4.7 kΩ 电阻上拉到 +3.3V。C1 100 nF 与 C2 22 µF 用于 3.3 V 电源去耦，JP1、JP2、JP3 分别呈现传感器侧与 HAT 侧连接网络。

## 检索关键词

`Hat DLight`、`U134`、`BH1750FVI-TR`、`BH1750FVI`、`U1`、`I2C`、`SCL_3V3`、`SDA_3V3`、`SCL_HAT`、`SDA_HAT`、`ADDR`、`0x23`、`+3.3V`、`VCC_3V3`、`VCC_3V3_HAT`、`GND_HAT`、`INT_HAT`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`C1 100nF`、`C2 22uF`、`JP1`、`JP2`、`JP3`、`1-65535 lx`、`G0 SDA`、`G26 SCL`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | BH1750FVI-TR | I2C 数字环境光照度传感器，原理图标注 1 至 65535 lx | 图 834748f51da5 / 第 1 页 / 左上，U1 BH1750FVI-TR pins 1-7，下方标注 1~65535 lx |
| JP1 | 5-pin connector | 传感器侧 5 针连接器，导出 VCC_3V3、GND、SCL_3V3 与 SDA_3V3 | 图 834748f51da5 / 第 1 页 / 中下，JP1 pins 1-5 与 VCC_3V3/GND/SCL_3V3/SDA_3V3 |
| JP2 | 5-pin connector | HAT 侧 5 针连接器，导出 VCC_3V3_HAT、GND_HAT、SCL_HAT 与 SDA_HAT | 图 834748f51da5 / 第 1 页 / 中上，JP2 pins 1-5 与 VCC_3V3_HAT/GND_HAT/SCL_HAT/SDA_HAT |
| JP3 | 8-pin connector | HAT 主机接口，承载 VCC_3V3_HAT、GND_HAT、SCL_HAT、SDA_HAT 与 INT_HAT | 图 834748f51da5 / 第 1 页 / 右侧，JP3 pins 1-8 与 HAT 网络标签 |
| R1/R2/R3 | 4.7KΩ / 4.7KΩ / 4.7KΩ | 分别将 SCL、DVI、SDA 信号上拉到 +3.3V | 图 834748f51da5 / 第 1 页 / 左上，U1 pins 6/5/4 右侧 R1/R2/R3 均标 4.7KΩ，共接 +3.3V |
| C1 | 100nF (104) 10% 50V | +3.3V 对 GND 的高频去耦电容 | 图 834748f51da5 / 第 1 页 / 左下，C1 100nF (104) 10% 50V 跨接 +3.3V 与 GND |
| C2 | 22uF (226) 20% 6.3V | +3.3V 对 GND 的储能/低频去耦电容 | 图 834748f51da5 / 第 1 页 / 左下，C2 22uF (226) 20% 6.3V 跨接 +3.3V 与 GND |

## 系统结构

### 数字照度检测架构

U1 BH1750FVI-TR 通过 SCL_3V3/SDA_3V3 提供 I2C 照度数据，使用 +3.3V 电源，并经 JP1、JP2、JP3 连接器网络引出。

- 参数与网络：`sensor=U1 BH1750FVI-TR`；`bus=I2C`；`sensor_nets=SCL_3V3/SDA_3V3`；`supply=+3.3V`；`connectors=JP1/JP2/JP3`
- 证据：图 834748f51da5 / 第 1 页 / 整页：U1、R1/R2/R3、C1/C2、JP1/JP2/JP3

## 电源

### 传感器 3.3 V 供电

U1 pin1 VCC 连接 +3.3V，pin3 GND 与 EP pin7 接 GND；C1 100 nF 和 C2 22 µF 均跨接 +3.3V 与 GND。

- 参数与网络：`vcc=U1 pin1 +3.3V`；`ground=U1 pin3 GND`；`exposed_pad=U1 pin7 EP to GND`；`decoupling_1=C1 100nF (104) 10% 50V`；`decoupling_2=C2 22uF (226) 20% 6.3V`；`regulator=none shown`
- 证据：图 834748f51da5 / 第 1 页 / 左侧，U1 VCC/GND/EP 及下方 C1/C2 电源网络

## 接口

### JP1 传感器侧连接器

JP1 pin5 为 VCC_3V3、pin4 为 GND、pin3 为 SCL_3V3、pin2 为 SDA_3V3，pin1 未连接。

- 参数与网络：`reference=JP1`；`pin1=NC`；`pin2=SDA_3V3`；`pin3=SCL_3V3`；`pin4=GND`；`pin5=VCC_3V3`
- 证据：图 834748f51da5 / 第 1 页 / 中下，JP1 pins 1-5 与左侧网络标签

### JP2 HAT 侧连接器

JP2 pin5 为 VCC_3V3_HAT、pin4 为 GND_HAT、pin3 为 SCL_HAT、pin2 为 SDA_HAT，pin1 未连接。

- 参数与网络：`reference=JP2`；`pin1=NC`；`pin2=SDA_HAT`；`pin3=SCL_HAT`；`pin4=GND_HAT`；`pin5=VCC_3V3_HAT`
- 证据：图 834748f51da5 / 第 1 页 / 中上，JP2 pins 1-5 与左侧网络标签

### JP3 HAT 主机接口

JP3 pin8 为 GND_HAT、pin7 为 SCL_HAT、pin6 为 INT_HAT、pin5 为 SDA_HAT、pin3 为 VCC_3V3_HAT；pins 1、2、4 未连接。

- 参数与网络：`reference=JP3`；`pin1=NC`；`pin2=NC`；`pin3=VCC_3V3_HAT`；`pin4=NC`；`pin5=SDA_HAT`；`pin6=INT_HAT`；`pin7=SCL_HAT`；`pin8=GND_HAT`
- 证据：图 834748f51da5 / 第 1 页 / 右侧，JP3 pins 1-8 与 GND_HAT/SCL_HAT/INT_HAT/SDA_HAT/VCC_3V3_HAT

## 总线

### 传感器 I2C 总线

U1 pin6 SCL 连接 SCL_3V3，pin4 SDA 连接 SDA_3V3；两条信号分别通过 R1 与 R3 4.7 kΩ 上拉到 +3.3V。

- 参数与网络：`controller=external host`；`device=U1 BH1750FVI-TR`；`scl_pin=U1 pin6`；`scl_net=SCL_3V3`；`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pin=U1 pin4`；`sda_net=SDA_3V3`；`sda_pullup=R3 4.7KΩ to +3.3V`
- 证据：图 834748f51da5 / 第 1 页 / 左上，U1 SCL/SDA 至 SCL_3V3/SDA_3V3 与 R1/R3

## GPIO 与控制信号

### BH1750 地址选择脚

U1 pin2 ADDR 与 pin3 GND 共接 GND；原理图未画出可切换地址的跳线或开关。

- 参数与网络：`reference=U1`；`pin=pin2 ADDR`；`level=GND`；`configuration_control=fixed wiring`；`jumper=none shown`
- 证据：图 834748f51da5 / 第 1 页 / 左上，U1 pins 2 ADDR 与 3 GND 的共同接地连线

## 关键网络

### BH1750 DVI 网络

U1 pin5 DVI 通过 R2 4.7 kΩ 连接到 +3.3V。

- 参数与网络：`reference=U1`；`pin=pin5 DVI`；`pullup=R2 4.7KΩ`；`rail=+3.3V`
- 证据：图 834748f51da5 / 第 1 页 / 左上，U1 pin5 DVI-R2 4.7KΩ-+3.3V

## 传感器

### BH1750FVI-TR 照度传感器

U1 型号为 BH1750FVI-TR，原理图在器件下方明确标注照度范围 1 至 65535 lx。

- 参数与网络：`reference=U1`；`part_number=BH1750FVI-TR`；`schematic_range=1-65535 lx`
- 证据：图 834748f51da5 / 第 1 页 / 左上，U1 BH1750FVI-TR 与下方 1~65535 lx

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 数字照度检测架构 | `sensor=U1 BH1750FVI-TR`；`bus=I2C`；`sensor_nets=SCL_3V3/SDA_3V3`；`supply=+3.3V`；`connectors=JP1/JP2/JP3` |
| 传感器 | BH1750FVI-TR 照度传感器 | `reference=U1`；`part_number=BH1750FVI-TR`；`schematic_range=1-65535 lx` |
| 总线 | 传感器 I2C 总线 | `controller=external host`；`device=U1 BH1750FVI-TR`；`scl_pin=U1 pin6`；`scl_net=SCL_3V3`；`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pin=U1 pin4`；`sda_net=SDA_3V3`；`sda_pullup=R3 4.7KΩ to +3.3V` |
| GPIO 与控制信号 | BH1750 地址选择脚 | `reference=U1`；`pin=pin2 ADDR`；`level=GND`；`configuration_control=fixed wiring`；`jumper=none shown` |
| 关键网络 | BH1750 DVI 网络 | `reference=U1`；`pin=pin5 DVI`；`pullup=R2 4.7KΩ`；`rail=+3.3V` |
| 电源 | 传感器 3.3 V 供电 | `vcc=U1 pin1 +3.3V`；`ground=U1 pin3 GND`；`exposed_pad=U1 pin7 EP to GND`；`decoupling_1=C1 100nF (104) 10% 50V`；`decoupling_2=C2 22uF (226) 20% 6.3V`；`regulator=none shown` |
| 接口 | JP1 传感器侧连接器 | `reference=JP1`；`pin1=NC`；`pin2=SDA_3V3`；`pin3=SCL_3V3`；`pin4=GND`；`pin5=VCC_3V3` |
| 接口 | JP2 HAT 侧连接器 | `reference=JP2`；`pin1=NC`；`pin2=SDA_HAT`；`pin3=SCL_HAT`；`pin4=GND_HAT`；`pin5=VCC_3V3_HAT` |
| 接口 | JP3 HAT 主机接口 | `reference=JP3`；`pin1=NC`；`pin2=NC`；`pin3=VCC_3V3_HAT`；`pin4=NC`；`pin5=SDA_HAT`；`pin6=INT_HAT`；`pin7=SCL_HAT`；`pin8=GND_HAT` |
| 总线地址 | BH1750 I2C 地址 | `claimed_address=0x23`；`schematic_addr_level=GND`；`address_table=not printed` |
| GPIO 与控制信号 | M5StickC I2C GPIO 映射 | `claimed_sda_gpio=G0`；`claimed_scl_gpio=G26`；`schematic_sda_net=SDA_HAT`；`schematic_scl_net=SCL_HAT` |
| 传感器 | 传感器分辨率、波长与电流 | `claimed_adc_depth=16bit`；`claimed_peak_wavelength=560nm typical`；`claimed_current=<0.3mA at 3.3V` |

## 待确认事项

- `address.i2c-0x23`：产品正文给出 I2C 地址 0x23；原理图只显示 ADDR 接 GND，未印出地址值或地址真值表。（证据：图 834748f51da5 / 第 1 页 / 左上，U1 ADDR 接 GND，但页面无 0x23 标注）
- `gpio.host-mapping`：产品正文将 SDA/SCL 映射为 G0/G26，但原理图只标 SDA_HAT 与 SCL_HAT，未直接印出主机 GPIO 号。（证据：图 834748f51da5 / 第 1 页 / JP2/JP3 仅标 SDA_HAT 与 SCL_HAT，未标 G0/G26）
- `sensor.performance`：产品正文列出 16-bit AD 转换、560 nm 峰值灵敏度和 3.3 V 下小于 0.3 mA 工作电流，但这些性能参数未印在原理图中。（证据：图 834748f51da5 / 第 1 页 / U1 区域只标器件型号、引脚和 1~65535 lx）
- `review.i2c-address`：请用 BH1750FVI datasheet 确认 ADDR=GND 时的 7-bit I2C 地址是否为 0x23。；原因：原理图没有地址真值表或 0x23 标注。
- `review.host-gpio-mapping`：请用 HAT 接口定义或主板原理图确认 SDA_HAT/SCL_HAT 分别映射到 G0/G26。；原因：本页仅保留 HAT 网络名，没有主机 GPIO 编号。
- `review.sensor-performance`：请用 BH1750FVI datasheet 复核 16-bit 转换、560 nm 峰值灵敏度和工作电流指标。；原因：这些器件性能参数未在原理图上标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `834748f51da5a31c80e9f47d2b7042b012aee527a05f1db7f5176f5777f5cf9e` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_sch_01.webp` |

---

源文档：`zh_CN/hat/hat_dlight.md`

源文档 SHA-256：`03b264c52a9d87039f5fc50cb57ddec3c5d08a131f45c5b67d1ed061938b1a1d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
