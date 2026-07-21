# Unit PaHub v2.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PaHub v2.1 |
| SKU | U040-B-V21 |
| 产品 ID | `unit-pahub-v2-1-3cae2bc62d83` |
| 源文档 | `zh_CN/unit/Unit-PaHub v2.1.md` |

## 概述

Unit PaHub v2.1 以 U1 PCA9548AP 将 J7 上游 I2C 分配到 J1-J6 六个下游 Grove 端口，芯片通道 6、7 未使用。S1 三位拨码可将 A0/A1/A2 分别接地，R19-R21 则将三位上拉到 +3.3V。U2 HT7533 将入口 VCC 转换为 +3.3V，U1 与全部 I2C 上拉使用 +3.3V，而 J1-J6 的供电脚直通 VCC。上游 SCL/SDA、RESET 及十二条下游 SCx/SDx 均配置 10KΩ 上拉。

## 检索关键词

`Unit PaHub v2.1`、`U040-B-V21`、`PCA9548AP`、`HT7533`、`I2C multiplexer`、`I2C switch`、`six-channel I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`SC0`、`SD0`、`SC1`、`SD1`、`SC2`、`SD2`、`SC3`、`SD3`、`SC4`、`SD4`、`SC5`、`SD5`、`A0`、`A1`、`A2`、`RESET`、`0x70`、`0x77`、`J1-J6`、`J7`、`GROVE_I2C`、`VCC`、`+3.3V`、`10KΩ pull-up`、`SW 1.27-3P TPPT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PCA9548AP | 8 通道 I2C 多路开关，本板使用通道 0-5并保留 A0-A2 与 RESET | 图 8c2b0c966ffe / 第 1 页 / 第 1 页中央 U1 PCA9548AP，SCL/SDA/RESET、SD0-SD7、SC0-SC7、A0-A2、VCC/GND |
| U2 | HT7533 | 入口 VCC 至 +3.3V 线性稳压器 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页左下 U2 HT7533，VIN pin 2、VOUT pin 3、GND pin 1 |
| S1 | SW 1.27-3P TPPT | A0/A1/A2 三位地址拨码开关，闭合时接 GND | 图 8c2b0c966ffe / 第 1 页 / 第 1 页左中 S1 SW 1.27-3P TPPT，pins 1-3 共接 GND，pins 6/5/4 接 A0/A1/A2 |
| J7 | GROVE_I2C | 上游 I2C 与 VCC/GND 输入端口 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页左上 J7 GROVE_I2C，pins 1-4 IIC_SCL/IIC_SDA/VCC/GND |
| J1-J6 | GROVE_I2C | U1 通道 0-5 的六个下游 I2C 与 VCC/GND 端口 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页中右 J1-J6 GROVE_I2C，SC0/SD0 至 SC5/SD5、VCC、GND |
| R1,R2,R3 | 10KΩ (103) ±5% resistor array | 十二条下游 SC0-SC5、SD0-SD5 到 +3.3V 的上拉阵列 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页右侧 R1-R3，每组四路 10KΩ(103)±5% 上拉到 +3.3V |
| R5,R6,R7 | 10KΩ | 上游 SCL、SDA 和 U1 RESET 到 +3.3V 的上拉 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页 U1 左上 R5/R6/R7 10KΩ，上端 +3.3V，下端分别为 SCL/SDA/RESET |
| R19,R20,R21 | 10KΩ | A0/A1/A2 到 +3.3V 的地址上拉 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页左中 R19/R20/R21 10KΩ 与 A0/A1/A2、+3.3V |
| C1,C3,C5,C6,C7,C8,C9,C10 | 100nF / 10uF | 入口、下游端口和 HT7533 输入输出电源去耦 | 图 8c2b0c966ffe / 第 1 页 / 第 1 页 C3/J7、C1/J1、C5/J2、C7/J5、C8/J6 100nF 及 U2 周围 C6 100nF、C9/C10 10uF |

## 系统结构

### Unit PaHub v2.1

U1 PCA9548AP 将一组上游 IIC_SCL/IIC_SDA 多路连接到六组下游 I2C 端口；通道 6、7 未使用，S1 提供三位地址选择，U2 提供 +3.3V 逻辑电源。

- 参数与网络：`switch=U1 PCA9548AP`；`upstream=J7 IIC_SCL/IIC_SDA`；`downstream_ports=J1-J6`；`used_channels=0,1,2,3,4,5`；`unused_channels=6,7`；`address_switch=S1`；`regulator=U2 HT7533`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页完整 J7-U1-J1至J6 总线结构、S1 地址与 U2 电源区

### 其他功能分区

本页未绘制 MCU、协处理器、存储器、晶振、调试口、音频、传感器、射频、电池或充电器；控制逻辑全部位于 PCA9548AP 内部。

- 参数与网络：`controller=false`；`coprocessor=false`；`memory=false`；`storage=false`；`clock=false`；`debug=false`；`audio=false`；`sensor=false`；`rf=false`；`battery=false`；`charger=false`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页全部器件与功能分区

## 核心器件

### U1 PCA9548AP

U1 上游 SCL/SDA 分别为 pin 22/pin 23，RESET 为 pin 3，VCC 为 pin 24，GND 为 pin 12，A0/A1/A2 分别为 pin 1/pin 2/pin 21。

- 参数与网络：`SCL=pin 22`；`SDA=pin 23`；`RESET=pin 3`；`VCC=pin 24`；`GND=pin 12`；`A0=pin 1`；`A1=pin 2`；`A2=pin 21`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页中央 U1 左侧 SCL/SDA/RESET/A0-A2/VCC/GND pin 编号

## 电源

### VCC 至 +3.3V 稳压

入口 VCC 连接 U2 HT7533 VIN pin 2，VOUT pin 3 输出 +3.3V，GND pin 1 接地；输入 C10 10uF，输出 C6 100nF 与 C9 10uF 接地。

- 参数与网络：`input=VCC -> U2 pin 2 VIN`；`output=U2 pin 3 VOUT -> +3.3V`；`ground=U2 pin 1`；`input_capacitor=C10 10uF`；`output_capacitors=C6 100nF,C9 10uF`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页左下 U2 HT7533、C6/C9/C10、VCC/+3.3V/GND

### +3.3V 逻辑与 VCC 端口电源

U1 VCC pin 24、R1-R3、R5-R7 和 R19-R21 使用 +3.3V；J7 pin 3 输入的 VCC 直接分配到 J1-J6 pin 3，并作为 U2 输入，两条电源网络由 U2 分隔。

- 参数与网络：`logic_rail=+3.3V`；`logic_consumers=U1,R1-R3,R5-R7,R19-R21`；`raw_rail=VCC`；`raw_distribution=J7 pin3 -> J1-J6 pin3 and U2 VIN`；`conversion=U2 VCC to +3.3V`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页全部 +3.3V 与 VCC 电源标记及 U2 转换路径

### 端口 VCC 去耦

J7 旁 C3、J1 旁 C1、J2 旁 C5、J5 旁 C7、J6 旁 C8 均为 100nF 并跨接 VCC/GND；本页未在 J3/J4 旁绘制对应电容。

- 参数与网络：`upstream=C3 100nF`；`channel_0=C1 100nF`；`channel_1=C5 100nF`；`channel_2=null`；`channel_3=null`；`channel_4=C7 100nF`；`channel_5=C8 100nF`；`connection=VCC to GND`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 J7/J1/J2/J5/J6 旁 C3/C1/C5/C7/C8 100nF，J3/J4 周围无电容

## 接口

### J7 上游 Grove

J7 pin 1=IIC_SCL、pin 2=IIC_SDA、pin 3=VCC、pin 4=GND。

- 参数与网络：`reference=J7`；`part_number=GROVE_I2C`；`pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页左上 J7 GROVE_I2C pin 1-4 标签

### J1-J6 下游 Grove

六个下游端口采用相同 pinout：pin 1 为对应 SCx，pin 2 为对应 SDx，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`J1=1:SC0,2:SD0,3:VCC,4:GND`；`J2=1:SC1,2:SD1,3:VCC,4:GND`；`J3=1:SC2,2:SD2,3:VCC,4:GND`；`J4=1:SC3,2:SD3,3:VCC,4:GND`；`J5=1:SC4,2:SD4,3:VCC,4:GND`；`J6=1:SC5,2:SD5,3:VCC,4:GND`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页中右 J1-J6 每个 GROVE_I2C 符号的 pins 1-4

## 总线

### J7 至 U1 上游 I2C

J7 IIC_SCL pin 1 连接 U1 SCL pin 22，J7 IIC_SDA pin 2 连接 U1 SDA pin 23；SCL、SDA 分别由 R5、R6 10KΩ 上拉到 +3.3V。

- 参数与网络：`scl=J7 pin1 IIC_SCL -> U1 pin22 SCL`；`sda=J7 pin2 IIC_SDA -> U1 pin23 SDA`；`scl_pullup=R5 10K to +3.3V`；`sda_pullup=R6 10K to +3.3V`；`direction=bidirectional`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页左上 J7、R5/R6 与 U1 SCL/SDA pins 22/23

### U1 通道 0-2

U1 SD0 pin 4/SC0 pin 5 连接 J1 pin 2/pin 1，SD1 pin 6/SC1 pin 7 连接 J2 pin 2/pin 1，SD2 pin 8/SC2 pin 9 连接 J3 pin 2/pin 1。

- 参数与网络：`channel_0=SD0 pin4->J1 pin2;SC0 pin5->J1 pin1`；`channel_1=SD1 pin6->J2 pin2;SC1 pin7->J2 pin1`；`channel_2=SD2 pin8->J3 pin2;SC2 pin9->J3 pin1`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 U1 SD0/SC0-SD2/SC2 与 J1-J3 同名网络

### U1 通道 3-5

U1 SD3 pin 10/SC3 pin 11 连接 J4 pin 2/pin 1，SD4 pin 13/SC4 pin 14 连接 J5 pin 2/pin 1，SD5 pin 15/SC5 pin 16 连接 J6 pin 2/pin 1。

- 参数与网络：`channel_3=SD3 pin10->J4 pin2;SC3 pin11->J4 pin1`；`channel_4=SD4 pin13->J5 pin2;SC4 pin14->J5 pin1`；`channel_5=SD5 pin15->J6 pin2;SC5 pin16->J6 pin1`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 U1 SD3/SC3-SD5/SC5 与 J4-J6 同名网络

### SC0-SC5/SD0-SD5 上拉

R1 将 SD0、SC0、SD1、SC1 上拉至 +3.3V，R2 将 SD2、SC2、SD3、SC3 上拉至 +3.3V，R3 将 SD4、SC4、SD5、SC5 上拉至 +3.3V；每路均标 10KΩ (103) ±5%。

- 参数与网络：`R1=SD0,SC0,SD1,SC1`；`R2=SD2,SC2,SD3,SC3`；`R3=SD4,SC4,SD5,SC5`；`resistance_ohm_each=10000`；`tolerance=±5%`；`rail=+3.3V`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页右侧 R1-R3 网络标签、公共 +3.3V 与 10KΩ(103)±5%

### U1 通道 6 和 7

U1 SD6 pin 17、SC6 pin 18、SD7 pin 19、SC7 pin 20 均带未连接叉号，因此本板只实现六个下游通道。

- 参数与网络：`SD6=pin17 NC`；`SC6=pin18 NC`；`SD7=pin19 NC`；`SC7=pin20 NC`；`implemented_channels=6`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 U1 右下 SD6/SC6/SD7/SC7 pins 17-20 的红色叉号

## 总线地址

### A0-A2 地址拨码

U1 A0 pin 1、A1 pin 2、A2 pin 21 分别由 R19、R20、R21 10KΩ 上拉到 +3.3V，并连接 S1 pins 6、5、4；S1 对应的 pins 1、2、3 共接 GND，开关闭合时将相应地址位拉低。

- 参数与网络：`A0=U1 pin1/R19 10K to +3.3V/S1 pin6 to pin1 GND`；`A1=U1 pin2/R20 10K to +3.3V/S1 pin5 to pin2 GND`；`A2=U1 pin21/R21 10K to +3.3V/S1 pin4 to pin3 GND`；`open_level=high`；`closed_level=low`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页左中 S1、R19-R21、A0/A1/A2 与 +3.3V/GND

## 复位

### U1 RESET

U1 RESET pin 3 由 R7 10KΩ 上拉到 +3.3V，本页未连接外部复位开关或连接器。

- 参数与网络：`pin=U1 pin 3 RESET`；`pullup=R7 10K to +3.3V`；`external_reset=null`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 U1 RESET pin 3 与 R7 10KΩ/+3.3V

## 保护电路

### I2C 与电源接口保护

上游和六路下游 I2C 直接连接 U1 并上拉到 +3.3V；本页未显示电平转换器、TVS/ESD、保险丝、反接保护、过压保护或端口负载开关。

- 参数与网络：`level_shifter=null`；`tvs_esd=null`；`fuse=null`；`reverse_protection=null`；`overvoltage_protection=null`；`per_port_load_switch=null`
- 证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 J7-U1-J1至J6 直接总线、电源和上拉路径

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PaHub v2.1 | `switch=U1 PCA9548AP`；`upstream=J7 IIC_SCL/IIC_SDA`；`downstream_ports=J1-J6`；`used_channels=0,1,2,3,4,5`；`unused_channels=6,7`；`address_switch=S1`；`regulator=U2 HT7533` |
| 核心器件 | U1 PCA9548AP | `SCL=pin 22`；`SDA=pin 23`；`RESET=pin 3`；`VCC=pin 24`；`GND=pin 12`；`A0=pin 1`；`A1=pin 2`；`A2=pin 21` |
| 电源 | VCC 至 +3.3V 稳压 | `input=VCC -> U2 pin 2 VIN`；`output=U2 pin 3 VOUT -> +3.3V`；`ground=U2 pin 1`；`input_capacitor=C10 10uF`；`output_capacitors=C6 100nF,C9 10uF` |
| 电源 | +3.3V 逻辑与 VCC 端口电源 | `logic_rail=+3.3V`；`logic_consumers=U1,R1-R3,R5-R7,R19-R21`；`raw_rail=VCC`；`raw_distribution=J7 pin3 -> J1-J6 pin3 and U2 VIN`；`conversion=U2 VCC to +3.3V` |
| 接口 | J7 上游 Grove | `reference=J7`；`part_number=GROVE_I2C`；`pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND` |
| 总线 | J7 至 U1 上游 I2C | `scl=J7 pin1 IIC_SCL -> U1 pin22 SCL`；`sda=J7 pin2 IIC_SDA -> U1 pin23 SDA`；`scl_pullup=R5 10K to +3.3V`；`sda_pullup=R6 10K to +3.3V`；`direction=bidirectional` |
| 复位 | U1 RESET | `pin=U1 pin 3 RESET`；`pullup=R7 10K to +3.3V`；`external_reset=null` |
| 总线地址 | A0-A2 地址拨码 | `A0=U1 pin1/R19 10K to +3.3V/S1 pin6 to pin1 GND`；`A1=U1 pin2/R20 10K to +3.3V/S1 pin5 to pin2 GND`；`A2=U1 pin21/R21 10K to +3.3V/S1 pin4 to pin3 GND`；`open_level=high`；`closed_level=low` |
| 总线 | U1 通道 0-2 | `channel_0=SD0 pin4->J1 pin2;SC0 pin5->J1 pin1`；`channel_1=SD1 pin6->J2 pin2;SC1 pin7->J2 pin1`；`channel_2=SD2 pin8->J3 pin2;SC2 pin9->J3 pin1` |
| 总线 | U1 通道 3-5 | `channel_3=SD3 pin10->J4 pin2;SC3 pin11->J4 pin1`；`channel_4=SD4 pin13->J5 pin2;SC4 pin14->J5 pin1`；`channel_5=SD5 pin15->J6 pin2;SC5 pin16->J6 pin1` |
| 接口 | J1-J6 下游 Grove | `J1=1:SC0,2:SD0,3:VCC,4:GND`；`J2=1:SC1,2:SD1,3:VCC,4:GND`；`J3=1:SC2,2:SD2,3:VCC,4:GND`；`J4=1:SC3,2:SD3,3:VCC,4:GND`；`J5=1:SC4,2:SD4,3:VCC,4:GND`；`J6=1:SC5,2:SD5,3:VCC,4:GND` |
| 总线 | SC0-SC5/SD0-SD5 上拉 | `R1=SD0,SC0,SD1,SC1`；`R2=SD2,SC2,SD3,SC3`；`R3=SD4,SC4,SD5,SC5`；`resistance_ohm_each=10000`；`tolerance=±5%`；`rail=+3.3V` |
| 总线 | U1 通道 6 和 7 | `SD6=pin17 NC`；`SC6=pin18 NC`；`SD7=pin19 NC`；`SC7=pin20 NC`；`implemented_channels=6` |
| 电源 | 端口 VCC 去耦 | `upstream=C3 100nF`；`channel_0=C1 100nF`；`channel_1=C5 100nF`；`channel_2=null`；`channel_3=null`；`channel_4=C7 100nF`；`channel_5=C8 100nF`；`connection=VCC to GND` |
| 保护电路 | I2C 与电源接口保护 | `level_shifter=null`；`tvs_esd=null`；`fuse=null`；`reverse_protection=null`；`overvoltage_protection=null`；`per_port_load_switch=null` |
| 系统结构 | 其他功能分区 | `controller=false`；`coprocessor=false`；`memory=false`；`storage=false`；`clock=false`；`debug=false`；`audio=false`；`sensor=false`；`rf=false`；`battery=false`；`charger=false` |
| 总线地址 | I2C 地址范围与默认值 | `documented_range=0x70-0x77`；`documented_default=0x70`；`address_pins=A2,A1,A0`；`open_level=1`；`closed_level=0`；`factory_switch_state=null`；`schematic_base_address=null` |
| 电源 | 入口与下游 VCC 标称电压 | `schematic_raw_rail=VCC`；`documented_voltage_v=5`；`regulated_rail=+3.3V`；`affected_connectors=J7,J1-J6` |
| 接口 | Grove 线色映射 | `upstream_pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND`；`downstream_pinout=1:SCx,2:SDx,3:VCC,4:GND`；`color_labels=null` |
| 总线 | I2C 通信速率 | `bus=I2C`；`upstream_pullups=10K to +3.3V`；`downstream_pullups=10K each to +3.3V`；`clock_rate=null`；`mode=null`；`bus_capacitance=null` |

## 待确认事项

- `address.documented-range-default`：产品正文称地址范围为 0x70-0x77、默认 0x70；原理图只确认 A0-A2 上拉和拨码接地拓扑，没有基地址编码表，也未标出 S1 出厂开关位置。（证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 S1/R19-R21/A0-A2 区域，无十六进制地址或出厂位置标注）
- `power.documented-vcc-voltage`：产品正文 Grove 表将 VCC 写为 5V，但原理图仅标 VCC，并显示其经 HT7533 生成 +3.3V；本页未直接标注 VCC 的具体电压。（证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 J7/J1-J6 与 U2 输入均标 VCC，无数值）
- `interface.grove-color-mapping`：原理图给出 J7 与 J1-J6 的 pin 1-4 电气网络，但没有 Black/Red/Yellow/White 线色，无法仅据本页验证正文线色映射。（证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页全部 GROVE_I2C 符号仅显示网络和 pin 编号）
- `bus.i2c-speed`：原理图确认 I2C 拓扑和 10KΩ 上拉，但未给出支持模式、最高时钟速率、线缆长度或总线电容限制。（证据：图 8c2b0c966ffe / 第 1 页 / 第 1 页 IIC_SCL/IIC_SDA 与 SC0-SC5/SD0-SD5，无速率或模式注释）
- `review.address-range-default`：请结合 PCA9548AP 数据手册和 S1 出厂位置确认 0x70-0x77 地址编码及默认 0x70。；原因：原理图只显示地址位电气状态选择，没有基地址表和出厂开关位置。
- `review.vcc-voltage`：请用硬件规格或实板测量确认 J7/J1-J6 的 VCC 标称电压是否为 5V。；原因：原理图将原始电源统一标为 VCC，仅明确稳压后为 +3.3V。
- `review.grove-color-mapping`：请结合 Grove 线缆规范与连接器方向确认 Black/Red/Yellow/White 对应关系。；原因：原理图没有线色信息。
- `review.i2c-speed`：请结合 PCA9548AP 数据手册、总线电容和线缆长度确定支持的 I2C 模式与最高可靠速率。；原因：10KΩ 上拉和拓扑不足以证明具体速率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8c2b0c966ffedd769e4bc96bb82eea9e03b0e26740986f4dd3c133a42820a7e3` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-PaHub2.1/img-103440a9-d7e4-4aab-b784-825aa9b35614.png` |

---

源文档：`zh_CN/unit/Unit-PaHub v2.1.md`

源文档 SHA-256：`25cd8804fc4b50588e90ea4cb5c132e5419d7000b4fa77515beccaf53e624f61`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
