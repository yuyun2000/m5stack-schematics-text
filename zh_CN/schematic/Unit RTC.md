# Unit RTC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RTC |
| SKU | U126 |
| 产品 ID | `unit-rtc-b22b49da279c` |
| 源文档 | `zh_CN/unit/UNIT RTC.md` |

## 概述

Unit RTC 的原理图使用 HT7533（U3）把 Grove 输入的 +5V 转换为 +3.3V，并通过 BAV74（D1）将 +3.3V 与电池 BT1 二极管或接到 RTC 供电节点。图中 U1、U2 均标为 RTC8563，二者共享 SCL/SDA、32.768KHz 晶振 Y1 和同一 VDD 电源。SCL、SDA 由 4.7KΩ 电阻上拉到 +3.3V，J1 同时引出 I2C、+5V 与 GND。

## 检索关键词

`Unit RTC`、`U126`、`RTC8563`、`HYM8563`、`HT7533`、`BAV74`、`32.768KHz`、`Y1`、`OSCI`、`OSCO`、`SCL`、`SDA`、`I2C`、`CLKOUT`、`INT`、`+5V`、`+3.3V`、`BT1`、`Battery`、`HY-2.0_IIC`、`4.7KΩ`、`7pF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | RTC8563 | I2C 实时时钟器件之一，共享晶振、电源和 I2C 网络 | 图 d88f469e0cc3 / 第 1 页 / 页面上部中央 U1：RTC8563，OSCI/OSCO/INT/VSS/VDD/CLKOUT/SCL/SDA 引脚 |
| U2 | RTC8563 | I2C 实时时钟器件之一，共享晶振、电源和 I2C 网络 | 图 d88f469e0cc3 / 第 1 页 / 页面中央 U2：RTC8563，OSCI/OSCO/INT/VSS/VDD/CLKOUT/SCL/SDA 引脚 |
| U3 | HT7533 | 将 J1 输入的 +5V 转换为 +3.3V | 图 d88f469e0cc3 / 第 1 页 / 页面下部中央 U3：HT7533，VIN 接 +5V、VOUT 接 +3.3V、GND 接地 |
| Y1 | 32.768KHz ±20ppm 7pF | U1/U2 共用的 RTC 低频晶振 | 图 d88f469e0cc3 / 第 1 页 / 页面左上部 Y1：标注 32.768KHz ±20ppm 7pF，跨接 OSCI 与 OSCO |
| D1 | BAV74 | 将 +3.3V 与 BT1 正极或接至 RTC VDD 电源节点的双二极管 | 图 d88f469e0cc3 / 第 1 页 / 页面右上部 D1：BAV74，1 脚接 +3.3V、2 脚接 BT1、3 脚接 U1/U2 VDD 公共节点 |
| BT1 | Battery | RTC 后备电源，正极经 D1.2 接 VDD 电源节点，负极接 GND | 图 d88f469e0cc3 / 第 1 页 / 页面右上部 BT1 Battery：上端连接 D1.2，下端连接 GND |
| J1 | HY-2.0_IIC | 4 Pin I2C 与电源接口 | 图 d88f469e0cc3 / 第 1 页 / 页面右下部 J1 HY-2.0_IIC：1~4 脚为 IIC_SCL、IIC_SDA、VCC、GND |
| R1 | 4.7KΩ | SCL 到 +3.3V 的 I2C 上拉电阻 | 图 d88f469e0cc3 / 第 1 页 / 页面右中部 R1：4.7KΩ，从 +3.3V 接至 SCL |
| R2 | 4.7KΩ | SDA 到 +3.3V 的 I2C 上拉电阻 | 图 d88f469e0cc3 / 第 1 页 / 页面右中部 R2：4.7KΩ，从 +3.3V 接至 SDA |
| C2/C3 | 7pF | Y1 两端 OSCI/OSCO 对 GND 的负载电容 | 图 d88f469e0cc3 / 第 1 页 / 页面左上部：C2 7pF 从 OSCI 接 GND，C3 7pF 从 OSCO 接 GND |
| C1/C4 | 100nF | U1/U2 VDD 公共节点对 GND 的去耦电容 | 图 d88f469e0cc3 / 第 1 页 / 页面上部与中部 U1/U2 右侧：C1、C4 均为 100nF，跨接 VDD 公共节点与 GND |
| C5/C6 | 10uF | HT7533 输出 +3.3V 与输入 +5V 的滤波电容 | 图 d88f469e0cc3 / 第 1 页 / 页面下部 U3 两侧：C5 10uF 跨接 +3.3V/GND，C6 10uF 跨接 +5V/GND |

## 系统结构

### Unit RTC

J1 提供 +5V、GND、SCL 和 SDA；U3 将 +5V 转换为 +3.3V，D1 将 +3.3V 与 BT1 后备电源或接到 RTC VDD 公共节点，U1/U2 共享 I2C 与 32.768KHz 晶振。

- 参数与网络：`rtc_devices=U1 RTC8563,U2 RTC8563`；`regulator=U3 HT7533`；`power_or=D1 BAV74`；`backup_source=BT1`；`clock=Y1 32.768KHz ±20ppm 7pF`；`interface=J1 HY-2.0_IIC`
- 证据：图 d88f469e0cc3 / 第 1 页 / 整页：J1/U3/D1/BT1 电源路径及 U1/U2/Y1/SCL/SDA 网络

## 电源

### U3 HT7533

U3 的 2 脚 VIN 接 +5V，3 脚 VOUT 输出 +3.3V，GND 引脚接地；C6 10uF 位于 +5V 输入侧，C5 10uF 位于 +3.3V 输出侧。

- 参数与网络：`input=U3.2 +5V`；`output=U3.3 +3.3V`；`ground=GND`；`input_capacitor=C6 10uF`；`output_capacitor=C5 10uF`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面下部中央 U3：VIN/VOUT/GND 引脚及 C6/C5、+5V/+3.3V 网络

### D1 BAV74 RTC 供电或接

D1 的 1 脚接 +3.3V，2 脚接 BT1 正极，3 脚接 U1/U2 的 VDD 公共节点；BT1 负极接 GND。

- 参数与网络：`main_source=D1.1 +3.3V`；`backup_source=D1.2 BT1+`；`rtc_supply=D1.3 to U1.8/U2.8 VDD`；`battery_return=BT1- GND`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面右上部 D1/BT1：BAV74 1/2/3 脚、+3.3V、BT1 与 U1/U2 VDD 水平网络

### U1/U2 VDD 去耦

C1 100nF 和 C4 100nF 均跨接 U1/U2 VDD 公共节点与 GND。

- 参数与网络：`capacitors=C1 100nF,C4 100nF`；`supply_node=U1.8/U2.8 VDD`；`return=GND`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面上部 U1/U2 右侧：C1/C4 从 VDD 公共线接 GND

## 接口

### J1 HY-2.0_IIC

J1 的 1 脚 IIC_SCL 接 SCL，2 脚 IIC_SDA 接 SDA，3 脚 VCC 接 +5V，4 脚 GND 接地。

- 参数与网络：`pin_1=IIC_SCL SCL`；`pin_2=IIC_SDA SDA`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面右下部 J1：1~4 脚数字、IIC_SCL/IIC_SDA/VCC/GND 字段及左侧 SCL/SDA/+5V/GND 网络

## 总线

### SCL/SDA

R1 4.7KΩ 将 SCL 上拉到 +3.3V，R2 4.7KΩ 将 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面右中部：R1/R2 上端 +3.3V，下端分别连接 SCL/SDA

### U1 RTC8563

U1 的 1 脚 OSCI 接 OSCI，2 脚 OSCO 接 OSCO，3 脚 INT 标记不连接，4 脚 VSS 接 GND，5 脚 SDA 接 SDA，6 脚 SCL 接 SCL，7 脚 CLKOUT 在本页无外接线，8 脚 VDD 接 RTC 电源公共节点。

- 参数与网络：`pin_1=OSCI`；`pin_2=OSCO`；`pin_3=INT NC`；`pin_4=VSS GND`；`pin_5=SDA`；`pin_6=SCL`；`pin_7=CLKOUT unconnected`；`pin_8=VDD`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面上部中央 U1：1~8 脚号、引脚名、红色 NC 标记和外部网络

### U2 RTC8563

U2 的 1 脚 OSCI 接 OSCI，2 脚 OSCO 接 OSCO，3 脚 INT 标记不连接，4 脚 VSS 接 GND，5 脚 SDA 接 SDA，6 脚 SCL 接 SCL，7 脚 CLKOUT 在本页无外接线，8 脚 VDD 接 RTC 电源公共节点。

- 参数与网络：`pin_1=OSCI`；`pin_2=OSCO`；`pin_3=INT NC`；`pin_4=VSS GND`；`pin_5=SDA`；`pin_6=SCL`；`pin_7=CLKOUT unconnected`；`pin_8=VDD`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面中央 U2：1~8 脚号、引脚名、红色 NC 标记和外部网络

## GPIO 与控制信号

### U1/U2 INT 与 CLKOUT

U1 和 U2 的 3 脚 INT 均显示红色不连接标记；两器件的 7 脚 CLKOUT 在本页均无外接连线。

- 参数与网络：`U1_INT=U1.3 NC`；`U2_INT=U2.3 NC`；`U1_CLKOUT=U1.7 unconnected`；`U2_CLKOUT=U2.7 unconnected`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面上部 U1/U2：INT 端红色 X 与 CLKOUT 端短引脚无外接网络

## 时钟

### Y1 与 U1/U2

Y1 标注 32.768KHz ±20ppm 7pF，跨接 OSCI 与 OSCO；C2 7pF 从 OSCI 接 GND，C3 7pF 从 OSCO 接 GND；OSCI/OSCO 同时连接 U1 和 U2 的 1/2 脚。

- 参数与网络：`crystal=Y1 32.768KHz ±20ppm 7pF`；`osci_capacitor=C2 7pF`；`osco_capacitor=C3 7pF`；`connected_devices=U1,U2`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面左上部 Y1/C2/C3 与页面上中部 U1/U2 OSCI/OSCO 网络

## 关键网络

### U1/U2 共用网络

U1 和 U2 的 SCL、SDA、OSCI、OSCO、VDD 与 GND 分别直接并联到同名网络。

- 参数与网络：`clock_input=U1.1,U2.1 OSCI`；`clock_output=U1.2,U2.2 OSCO`；`scl=U1.6,U2.6 SCL`；`sda=U1.5,U2.5 SDA`；`supply=U1.8,U2.8 VDD`；`ground=U1.4,U2.4 GND`
- 证据：图 d88f469e0cc3 / 第 1 页 / 页面上部 U1/U2：两器件对应引脚间的垂直/同名网络连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RTC | `rtc_devices=U1 RTC8563,U2 RTC8563`；`regulator=U3 HT7533`；`power_or=D1 BAV74`；`backup_source=BT1`；`clock=Y1 32.768KHz ±20ppm 7pF`；`interface=J1 HY-2.0_IIC` |
| 接口 | J1 HY-2.0_IIC | `pin_1=IIC_SCL SCL`；`pin_2=IIC_SDA SDA`；`pin_3=VCC +5V`；`pin_4=GND` |
| 电源 | U3 HT7533 | `input=U3.2 +5V`；`output=U3.3 +3.3V`；`ground=GND`；`input_capacitor=C6 10uF`；`output_capacitor=C5 10uF` |
| 电源 | D1 BAV74 RTC 供电或接 | `main_source=D1.1 +3.3V`；`backup_source=D1.2 BT1+`；`rtc_supply=D1.3 to U1.8/U2.8 VDD`；`battery_return=BT1- GND` |
| 电源 | U1/U2 VDD 去耦 | `capacitors=C1 100nF,C4 100nF`；`supply_node=U1.8/U2.8 VDD`；`return=GND` |
| 总线 | SCL/SDA | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V` |
| 总线 | U1 RTC8563 | `pin_1=OSCI`；`pin_2=OSCO`；`pin_3=INT NC`；`pin_4=VSS GND`；`pin_5=SDA`；`pin_6=SCL`；`pin_7=CLKOUT unconnected`；`pin_8=VDD` |
| 总线 | U2 RTC8563 | `pin_1=OSCI`；`pin_2=OSCO`；`pin_3=INT NC`；`pin_4=VSS GND`；`pin_5=SDA`；`pin_6=SCL`；`pin_7=CLKOUT unconnected`；`pin_8=VDD` |
| 关键网络 | U1/U2 共用网络 | `clock_input=U1.1,U2.1 OSCI`；`clock_output=U1.2,U2.2 OSCO`；`scl=U1.6,U2.6 SCL`；`sda=U1.5,U2.5 SDA`；`supply=U1.8,U2.8 VDD`；`ground=U1.4,U2.4 GND` |
| 时钟 | Y1 与 U1/U2 | `crystal=Y1 32.768KHz ±20ppm 7pF`；`osci_capacitor=C2 7pF`；`osco_capacitor=C3 7pF`；`connected_devices=U1,U2` |
| GPIO 与控制信号 | U1/U2 INT 与 CLKOUT | `U1_INT=U1.3 NC`；`U2_INT=U2.3 NC`；`U1_CLKOUT=U1.7 unconnected`；`U2_CLKOUT=U2.7 unconnected` |
| 系统结构 | U1/U2 RTC8563 装配关系 | `devices=U1 RTC8563,U2 RTC8563`；`schematic_relation=parallel`；`population_marker=null` |
| 总线地址 | RTC8563 I2C 地址 | `schematic_address_label=null`；`address_straps=null`；`devices=U1,U2` |

## 待确认事项

- `system.dual-rtc-population`：原理图同时绘制 U1 和 U2 两个 RTC8563 且网络完全并联，但本页没有 DNP、二选一或装配版本标注，无法仅据此页确定实际是否同时装配。（证据：图 d88f469e0cc3 / 第 1 页 / 页面上部 U1/U2：两个独立位号、相同 RTC8563 型号及完全并联网络，周边无 DNP/ALT 文字）
- `address.rtc-i2c`：本页显示 U1/U2 的 SCL/SDA 连接，但没有地址值或地址配置引脚标注，因此单凭该原理图页面无法确认 I2C 地址。（证据：图 d88f469e0cc3 / 第 1 页 / 页面上部 U1/U2 与右下部 J1：仅显示 SCL/SDA，总页无十六进制地址或 A0/A1 配置标注）
- `review.dual-rtc-population`：U1 与 U2 是否为不同封装/供应商的二选一料位，实际 BOM 中装配哪一个？；原因：两个 RTC8563 位号共享全部关键网络，但原理图未标 DNP 或装配选项；同时装配与二选一会产生不同的硬件解释。
- `review.rtc-i2c-address`：请用 RTC8563/HYM8563 数据手册或已确认 BOM 验证该产品的固定 I2C 地址。；原因：原理图页面未直接标注地址，项目规则不允许用器件常识或产品正文替代原理图证据写成 confirmed。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d88f469e0cc373dd00ec32c8ff38051a4dc450ddd471b70f829a47e141fc63a8` | `https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT RTC/img-6f0baa97-c15f-4c85-be56-12078e7a7dd2.webp` |

---

源文档：`zh_CN/unit/UNIT RTC.md`

源文档 SHA-256：`9c97860d79dc5a862c764779cbadfdd6509970c35a3022caad6e83f0b1f5ff10`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
