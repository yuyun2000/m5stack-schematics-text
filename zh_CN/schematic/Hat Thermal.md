# Hat Thermal 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Thermal |
| SKU | U062 |
| 产品 ID | `hat-thermal-289aedfdfc7c` |
| 源文档 | `zh_CN/hat/hat-thermal.md` |

## 概述

Hat Thermal 以 MLX90640（U1）作为热成像传感器，VDD 使用 +3.3V，SCL/SDA 通过 R1/R2 各 4.7KΩ 上拉至 +3.3V。SCL 同时连接 P1 STICKIO 的 G26 与 P2.3，SDA 同时连接 P1 的 G0 与 P2.4；P2 还引出 +3.3V 和 GND。原理图未显示电源转换、外部时钟、复位、地址选择或保护电路，且未标注产品正文所述 I2C 地址 0x33。

## 检索关键词

`Hat Thermal`、`U062`、`MLX90640`、`U1`、`热成像`、`红外传感器`、`I2C`、`0x33`、`SCL`、`SDA`、`G26`、`G0`、`+3.3V`、`GND`、`STICKIO`、`P1`、`P2 Header 4`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 100nF`、`VDD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MLX90640 | 四针热成像传感器，使用 +3.3V/GND 供电并通过 SCL/SDA 通信 | 图 8509c45983b9 / 第 1 页 / B2 区域 U1 MLX90640：1 SDA、2 VDD、3 GND、4 SCL |
| P1 | STICKIO | 8 针主机接口，使用 GND、G26/SCL、G0/SDA 和 3V3/+3.3V | 图 8509c45983b9 / 第 1 页 / B3 区域 P1 STICKIO：1~8 脚 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN 与左侧网络 |
| P2 | Header 4 | 四针扩展接口，引出 +3.3V、GND、SCL 和 SDA | 图 8509c45983b9 / 第 1 页 / C2 区域 P2 Header 4：1 +3.3V、2 GND、3 SCL、4 SDA |
| R1 | 4.7KΩ | SCL 到 +3.3V 的 I2C 上拉电阻 | 图 8509c45983b9 / 第 1 页 / B2-B3 区域 R1 4.7KΩ：上端 +3.3V，下端 SCL |
| R2 | 4.7KΩ | SDA 到 +3.3V 的 I2C 上拉电阻 | 图 8509c45983b9 / 第 1 页 / B3 区域 R2 4.7KΩ：上端 +3.3V，下端 SDA |
| C1 | 100nF | U1 VDD 的 +3.3V 对地去耦电容 | 图 8509c45983b9 / 第 1 页 / B2 区域 U1 左侧 C1 100nF，跨接 +3.3V 与 GND |

## 系统结构

### Hat Thermal

U1 MLX90640 由 P1 的 +3.3V/GND 供电，通过 SCL/SDA 连接 P1 STICKIO 主机接口，并将相同总线与电源引出到 P2。

- 参数与网络：`sensor=U1 MLX90640`；`supply=+3.3V`；`host_interface=P1 STICKIO`；`expansion_interface=P2 Header 4`；`bus=SCL/SDA`
- 证据：图 8509c45983b9 / 第 1 页 / B2-C3 区域 U1、R1/R2、P1、P2 的全部同名电源与 I2C 网络

## 电源

### MLX90640 +3.3V 供电

P1.7 3V3 引入 +3.3V，连接 U1.2 VDD、R1/R2 上拉端、C1 和 P2.1；U1.3 与 P1.1/P2.2 接 GND。

- 参数与网络：`source=P1.7 3V3`；`sensor_supply=U1.2 VDD`；`pullup_supply=R1/R2 +3.3V`；`expansion_supply=P2.1 +3.3V`；`ground=U1.3; P1.1; P2.2`
- 证据：图 8509c45983b9 / 第 1 页 / B2-C3 区域所有 +3.3V/GND 同名网络及 U1/P1/P2 连接

### U1 去耦

C1 100nF 跨接 U1 VDD 使用的 +3.3V 与 GND。

- 参数与网络：`capacitor=C1 100nF`；`rail=+3.3V`；`return=GND`
- 证据：图 8509c45983b9 / 第 1 页 / B2 区域 U1 左侧 C1 100nF 的 +3.3V-GND 跨接

### 板载电源结构

U1 直接使用 P1 引入的 +3.3V；该页未显示 LDO、DC-DC、负载开关、电池或充电电路。

- 参数与网络：`sensor_rail=+3.3V`；`source=P1.7`；`ldo=not shown`；`dc_dc=not shown`；`load_switch=not shown`；`battery_charger=not shown`
- 证据：图 8509c45983b9 / 第 1 页 / 全页 P1.7 至 U1 VDD 的直接 +3.3V 路径，未见任何电源转换器

## 接口

### P1 STICKIO

P1.1 接 GND，P1.3 G26 接 SCL，P1.5 G0 接 SDA，P1.7 3V3 接 +3.3V；P1.2 5VOUT、P1.4 G36、P1.6 BAT、P1.8 5VIN 标为未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC`
- 证据：图 8509c45983b9 / 第 1 页 / B3 区域 P1：引脚编号、符号内名称、左侧网络及 2/4/6/8 脚未连接标记

### P2 Header 4

P2.1 接 +3.3V，P2.2 接 GND，P2.3 接 SCL，P2.4 接 SDA。

- 参数与网络：`pin_1=+3.3V`；`pin_2=GND`；`pin_3=SCL`；`pin_4=SDA`
- 证据：图 8509c45983b9 / 第 1 页 / C2 区域 P2 Header 4 的 1~4 脚与左侧 +3.3V/GND/SCL/SDA 网络

## 总线

### SCL/SDA

SCL 连接 U1.4、P1.3 G26 与 P2.3；SDA 连接 U1.1、P1.5 G0 与 P2.4。

- 参数与网络：`scl=U1.4 to P1.3 G26 to P2.3`；`sda=U1.1 to P1.5 G0 to P2.4`；`direction=bidirectional`
- 证据：图 8509c45983b9 / 第 1 页 / B2-C3 区域 U1/P1/P2 的 SCL 与 SDA 同名网络

### I2C 上拉网络

R1 4.7KΩ 将 SCL 上拉至 +3.3V，R2 4.7KΩ 将 SDA 上拉至 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`logic_rail=+3.3V`
- 证据：图 8509c45983b9 / 第 1 页 / B2-B3 区域 R1/R2 上端 +3.3V、下端 SCL/SDA 的连接

## 时钟

### 时钟、复位与调试

该页未显示外部晶振、时钟输入、复位、BOOT、中断或调试接口。

- 参数与网络：`external_clock=not shown`；`reset=not shown`；`boot=not shown`；`interrupt=not shown`；`debug=not shown`
- 证据：图 8509c45983b9 / 第 1 页 / 全页 U1 四针符号及 P1/P2 外围，仅显示电源、GND、SCL、SDA

## 保护电路

### 外部接口保护

P1、P2 与 U1 的电源和 I2C 路径上未显示 TVS、保险丝、串联电阻或专用电平转换器。

- 参数与网络：`tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown`
- 证据：图 8509c45983b9 / 第 1 页 / 全页 P1/P2 至 U1 的完整电源与 SCL/SDA 路径，仅见 R1/R2 上拉和 C1 去耦

## 传感器

### U1 MLX90640

U1.1 为 SDA，U1.2 VDD 接 +3.3V，U1.3 GND 接地，U1.4 为 SCL。

- 参数与网络：`pin_1=SDA`；`pin_2=VDD +3.3V`；`pin_3=GND`；`pin_4=SCL`
- 证据：图 8509c45983b9 / 第 1 页 / B2 区域 U1 MLX90640 符号四周的 1~4 脚编号、名称与网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Thermal | `sensor=U1 MLX90640`；`supply=+3.3V`；`host_interface=P1 STICKIO`；`expansion_interface=P2 Header 4`；`bus=SCL/SDA` |
| 传感器 | U1 MLX90640 | `pin_1=SDA`；`pin_2=VDD +3.3V`；`pin_3=GND`；`pin_4=SCL` |
| 接口 | P1 STICKIO | `pin_1=GND`；`pin_2=5VOUT NC`；`pin_3=G26 SCL`；`pin_4=G36 NC`；`pin_5=G0 SDA`；`pin_6=BAT NC`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC` |
| 接口 | P2 Header 4 | `pin_1=+3.3V`；`pin_2=GND`；`pin_3=SCL`；`pin_4=SDA` |
| 总线 | SCL/SDA | `scl=U1.4 to P1.3 G26 to P2.3`；`sda=U1.1 to P1.5 G0 to P2.4`；`direction=bidirectional` |
| 总线 | I2C 上拉网络 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`logic_rail=+3.3V` |
| 总线地址 | MLX90640 I2C 地址 | `documented_address=0x33`；`schematic_address_label=not shown`；`address_straps=not shown` |
| 电源 | MLX90640 +3.3V 供电 | `source=P1.7 3V3`；`sensor_supply=U1.2 VDD`；`pullup_supply=R1/R2 +3.3V`；`expansion_supply=P2.1 +3.3V`；`ground=U1.3; P1.1; P2.2` |
| 电源 | U1 去耦 | `capacitor=C1 100nF`；`rail=+3.3V`；`return=GND` |
| 电源 | 板载电源结构 | `sensor_rail=+3.3V`；`source=P1.7`；`ldo=not shown`；`dc_dc=not shown`；`load_switch=not shown`；`battery_charger=not shown` |
| 保护电路 | 外部接口保护 | `tvs=not shown`；`fuse=not shown`；`series_resistors=not shown`；`level_shifter=not shown` |
| 时钟 | 时钟、复位与调试 | `external_clock=not shown`；`reset=not shown`；`boot=not shown`；`interrupt=not shown`；`debug=not shown` |

## 待确认事项

- `address.i2c-0x33`：产品正文标注 I2C 地址为 0x33，但原理图未标注 0x33、地址选择引脚或地址配置器件，无法仅由该页确认地址。（证据：图 8509c45983b9 / 第 1 页 / 全页 U1 MLX90640 与 SCL/SDA 网络，未见 0x33 或地址配置）
- `review.i2c-address-0x33`：MLX90640 在 Hat Thermal 上使用的 7 位 I2C 地址是否固定为 0x33？；原因：产品正文给出 0x33，但原理图没有地址标注、地址引脚或配置网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8509c45983b9d30846aaee61146cef6073ebb2237955bdbf1008a08b6f0fb588` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/856/StickHat_THERMAL_page_01.png` |

---

源文档：`zh_CN/hat/hat-thermal.md`

源文档 SHA-256：`564f644983fa3efdb12506bc866e76d1c8386cc8d309b34de9055554727ab007`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
