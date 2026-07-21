# Unit Mini BPS v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini BPS v1.1 |
| SKU | U090-B |
| 产品 ID | `unit-mini-bps-v1-1-64ad14dd1681` |
| 源文档 | `zh_CN/unit/BPS(QMP6988).md` |

## 概述

Unit Mini BPS v1.1 以 U2 QMP6988 为气压传感器，使用 J1 HY-2.0_IIC 与主机通信，没有板载主控或存储器。U1 HT7533 将 J1 的 +5V 转换为 +3.3V，分别以 C1/C2 10uF 进行输入输出滤波。SCL/SDA 通过 Q2/Q1 BSS138 双向电平转换，Grove 侧上拉到 +5V，QMP6988 侧上拉到 +3.3V。

## 检索关键词

`Unit Mini BPS v1.1`、`U090-B`、`Mini BPS`、`QMP6988`、`U2`、`HT7533`、`U1`、`BSS138`、`Q1`、`Q2`、`J1`、`HY-2.0_IIC`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`SCK`、`SDI`、`SDO`、`CSB`、`Vdd`、`Vddio`、`+5V`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 4.7KΩ`、`C1 10uF`、`C2 10uF`、`C4 100nF`、`0x56`、`I2C level shifter`、`barometric pressure sensor`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | QMP6988 | 数字气压传感器；SCK/SDI 连接板内 SCL/SDA，CSB、Vdd、Vddio 接 +3.3V。 | 图 ac8c812a1999 / 第 1 页 / 页面中下部 U2 QMP6988，SCK/SDI/SDO/CSB/Vdd/Vddio/GND 引脚 |
| U1 | HT7533 | +5V 输入到 +3.3V 输出的三端 LDO，GND 接地。 | 图 ac8c812a1999 / 第 1 页 / 页面上中部 U1 HT7533，VIN 2、VOUT 3、GND 1 与 +5V/+3.3V |
| Q1 | BSS138 | SDA 的 +5V 与 +3.3V 两侧双向电平转换 MOSFET。 | 图 ac8c812a1999 / 第 1 页 / 页面左中部 Q1 BSS138，位于 SDA 外部侧与 U2 SDI 内部侧之间 |
| Q2 | BSS138 | SCL 的 +5V 与 +3.3V 两侧双向电平转换 MOSFET。 | 图 ac8c812a1999 / 第 1 页 / 页面左下部 Q2 BSS138，位于 SCL 外部侧与 U2 SCK 内部侧之间 |
| J1 | HY-2.0_IIC | 四针 Grove I2C 与供电接口，引出 SCL、SDA、+5V 和 GND。 | 图 ac8c812a1999 / 第 1 页 / 页面右侧 J1 HY-2.0_IIC，1-4 脚及 IIC_SCL/IIC_SDA/VCC/GND 标注 |
| R1,R2 | 4.7KΩ | Grove 外部侧 SDA/SCL 到 +5V 的 I2C 上拉电阻。 | 图 ac8c812a1999 / 第 1 页 / 页面左侧 R1 4.7KΩ 从 SDA 到 +5V，R2 4.7KΩ 从 SCL 到 +5V |
| R3,R4 | 4.7KΩ | 传感器内部侧 SDA/SCL 到 +3.3V 的 I2C 上拉电阻。 | 图 ac8c812a1999 / 第 1 页 / 页面中部 R3 4.7KΩ 从 Q1/U2 SDI 侧到 +3.3V，R4 4.7KΩ 从 Q2/U2 SCK 侧到 +3.3V |
| C1,C2 | 10uF | HT7533 的 +5V 输入与 +3.3V 输出对地电容。 | 图 ac8c812a1999 / 第 1 页 / 页面上中部 U1 两侧 C1/C2，均标注 10uF 并接 GND |
| C4 | 100nF | QMP6988 +3.3V 电源对地去耦电容。 | 图 ac8c812a1999 / 第 1 页 / 页面右中部 C4 100nF，跨接 +3.3V 与 GND |

## 系统结构

### 整板架构

整板由 U2 QMP6988 传感器、U1 HT7533 LDO、Q1/Q2 BSS138 I2C 电平转换和 J1 HY-2.0_IIC 构成；原理图未显示板载主控、存储器、晶振、复位、调试或射频电路。

- 参数与网络：`sensor=U2 QMP6988`；`regulator=U1 HT7533`；`level_shifters=Q1,Q2 BSS138`；`connector=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示`
- 证据：图 ac8c812a1999 / 第 1 页 / 第 1 页全图，全部可见功能器件为 U1/U2/Q1/Q2/J1 及阻容

## 电源

### U1 5V 到 3.3V LDO

U1 HT7533 的 VIN（2 脚）接 +5V，VOUT（3 脚）输出 +3.3V，GND（1 脚）接地；C1 与 C2 各 10uF，分别从输入和输出接 GND。

- 参数与网络：`regulator=U1 HT7533`；`input_pin=2`；`input_rail=+5V`；`output_pin=3`；`output_rail=+3.3V`；`ground_pin=1`；`input_capacitor=C1 10uF`；`output_capacitor=C2 10uF`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面上中部 +5V-C1-U1 HT7533-C2-+3.3V 电源链

### +3.3V 电源轨

+3.3V 供给 U2 的 CSB、Vdd、Vddio，连接 Q1/Q2 栅极侧参考，并通过 R3/R4 上拉内部 SDA/SCL；C4 100nF 从 +3.3V 接 GND。

- 参数与网络：`rail=+3.3V`；`sensor_pins=U2.2 CSB,U2.8 Vdd,U2.6 Vddio`；`internal_pullups=R3,R4 4.7KΩ`；`level_shifter_gate_reference=Q1,Q2`；`decoupling=C4 100nF`
- 证据：图 ac8c812a1999 / 第 1 页 / U2 电源脚、Q1/Q2 栅极参考、R3/R4 与 C4 的 +3.3V 标注

### 电源滤波与去耦

C1 10uF 跨接 +5V 与 GND，C2 10uF 跨接 +3.3V 与 GND，C4 100nF 也跨接 +3.3V 与 GND。

- 参数与网络：`input_bulk=C1 10uF +5V-to-GND`；`output_bulk=C2 10uF +3.3V-to-GND`；`sensor_decoupling=C4 100nF +3.3V-to-GND`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面上部 U1 两侧 C1/C2 与页面右中部 C4

## 接口

### J1 HY-2.0_IIC

J1.1-J1.4 分别为 IIC_SCL/SCL、IIC_SDA/SDA、VCC/+5V、GND。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面右侧 J1 1-4 脚，左侧 SCL/SDA/+5V/GND 与右侧 IIC_SCL/IIC_SDA/VCC/GND

## 总线

### QMP6988 I2C 总线

外部 SCL 经 Q2 BSS138 电平转换后连接 U2 SCK（4 脚），外部 SDA 经 Q1 BSS138 电平转换后连接 U2 SDI（3 脚）。

- 参数与网络：`bus=I2C`；`device=U2 QMP6988`；`external_scl=J1.1 SCL`；`scl_level_shifter=Q2 BSS138`；`sensor_scl=U2.4 SCK`；`external_sda=J1.2 SDA`；`sda_level_shifter=Q1 BSS138`；`sensor_sda=U2.3 SDI`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面左至中部 SCL-Q2-U2.SCK 与 SDA-Q1-U2.SDI 两条路径

### I2C 双电源域

SDA/SCL 的 Grove 外部侧分别由 R1/R2（4.7KΩ）上拉到 +5V，QMP6988 内部侧分别由 R3/R4（4.7KΩ）上拉到 +3.3V，Q1/Q2 BSS138 位于两侧之间。

- 参数与网络：`external_voltage=+5V`；`external_sda_pullup=R1 4.7KΩ`；`external_scl_pullup=R2 4.7KΩ`；`internal_voltage=+3.3V`；`internal_sda_pullup=R3 4.7KΩ`；`internal_scl_pullup=R4 4.7KΩ`；`sda_mosfet=Q1 BSS138`；`scl_mosfet=Q2 BSS138`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面左半部 R1/R2 +5V 上拉、Q1/Q2、R3/R4 +3.3V 上拉

## 保护电路

### J1 外部接口保护

J1 的 +5V、SCL、SDA 和 GND 直接进入 LDO、电平转换与地网络，本页未显示 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`connector=J1`；`signals=+5V,SCL,SDA,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`
- 证据：图 ac8c812a1999 / 第 1 页 / 第 1 页 J1 至 U1/Q1/Q2 的直接连接路径

## 关键网络

### SDA 网络路径

J1.2 的 SDA 与 R1 4.7KΩ/+5V 位于 Q1 外侧；Q1 内侧由 R3 4.7KΩ 上拉至 +3.3V，并连接 U2 SDI（3 脚）。

- 参数与网络：`connector=J1.2`；`external_net=SDA`；`external_pullup=R1 4.7KΩ to +5V`；`translator=Q1 BSS138`；`internal_pullup=R3 4.7KΩ to +3.3V`；`sensor_pin=U2 SDI pin3`
- 证据：图 ac8c812a1999 / 第 1 页 / SDA-R1-Q1-R3-U2.SDI 完整水平路径

### SCL 网络路径

J1.1 的 SCL 与 R2 4.7KΩ/+5V 位于 Q2 外侧；Q2 内侧由 R4 4.7KΩ 上拉至 +3.3V，并连接 U2 SCK（4 脚）。

- 参数与网络：`connector=J1.1`；`external_net=SCL`；`external_pullup=R2 4.7KΩ to +5V`；`translator=Q2 BSS138`；`internal_pullup=R4 4.7KΩ to +3.3V`；`sensor_pin=U2 SCK pin4`
- 证据：图 ac8c812a1999 / 第 1 页 / SCL-R2-Q2-R4-U2.SCK 完整水平路径

## 存储

### 存储器与主控

本页未显示 MCU、外部 Flash、EEPROM、SD 卡或其他存储器；传感器直接通过 I2C 暴露给 J1。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> Q1/Q2 -> U2`
- 证据：图 ac8c812a1999 / 第 1 页 / 第 1 页全图，未出现 MCU 或存储器位号

## 传感器

### U2 QMP6988

U2 的 SCK（4 脚）连接板内 SCL，SDI（3 脚）连接板内 SDA；CSB（2 脚）、Vdd（8 脚）和 Vddio（6 脚）均接 +3.3V，GND（1、7 脚）接地。

- 参数与网络：`reference=U2`；`part_number=QMP6988`；`pin_4=SCK/internal SCL`；`pin_3=SDI/internal SDA`；`pin_2=CSB/+3.3V`；`pin_8=Vdd/+3.3V`；`pin_6=Vddio/+3.3V`；`pins_1_7=GND`；`pin_5=SDO/no visible connection`
- 证据：图 ac8c812a1999 / 第 1 页 / 页面中下部 U2 QMP6988 的 1-8 脚网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `sensor=U2 QMP6988`；`regulator=U1 HT7533`；`level_shifters=Q1,Q2 BSS138`；`connector=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示` |
| 传感器 | U2 QMP6988 | `reference=U2`；`part_number=QMP6988`；`pin_4=SCK/internal SCL`；`pin_3=SDI/internal SDA`；`pin_2=CSB/+3.3V`；`pin_8=Vdd/+3.3V`；`pin_6=Vddio/+3.3V`；`pins_1_7=GND`；`pin_5=SDO/no visible connection` |
| 电源 | U1 5V 到 3.3V LDO | `regulator=U1 HT7533`；`input_pin=2`；`input_rail=+5V`；`output_pin=3`；`output_rail=+3.3V`；`ground_pin=1`；`input_capacitor=C1 10uF`；`output_capacitor=C2 10uF` |
| 电源 | +3.3V 电源轨 | `rail=+3.3V`；`sensor_pins=U2.2 CSB,U2.8 Vdd,U2.6 Vddio`；`internal_pullups=R3,R4 4.7KΩ`；`level_shifter_gate_reference=Q1,Q2`；`decoupling=C4 100nF` |
| 接口 | J1 HY-2.0_IIC | `reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND` |
| 总线 | QMP6988 I2C 总线 | `bus=I2C`；`device=U2 QMP6988`；`external_scl=J1.1 SCL`；`scl_level_shifter=Q2 BSS138`；`sensor_scl=U2.4 SCK`；`external_sda=J1.2 SDA`；`sda_level_shifter=Q1 BSS138`；`sensor_sda=U2.3 SDI` |
| 总线 | I2C 双电源域 | `external_voltage=+5V`；`external_sda_pullup=R1 4.7KΩ`；`external_scl_pullup=R2 4.7KΩ`；`internal_voltage=+3.3V`；`internal_sda_pullup=R3 4.7KΩ`；`internal_scl_pullup=R4 4.7KΩ`；`sda_mosfet=Q1 BSS138`；`scl_mosfet=Q2 BSS138` |
| 关键网络 | SDA 网络路径 | `connector=J1.2`；`external_net=SDA`；`external_pullup=R1 4.7KΩ to +5V`；`translator=Q1 BSS138`；`internal_pullup=R3 4.7KΩ to +3.3V`；`sensor_pin=U2 SDI pin3` |
| 关键网络 | SCL 网络路径 | `connector=J1.1`；`external_net=SCL`；`external_pullup=R2 4.7KΩ to +5V`；`translator=Q2 BSS138`；`internal_pullup=R4 4.7KΩ to +3.3V`；`sensor_pin=U2 SCK pin4` |
| 电源 | 电源滤波与去耦 | `input_bulk=C1 10uF +5V-to-GND`；`output_bulk=C2 10uF +3.3V-to-GND`；`sensor_decoupling=C4 100nF +3.3V-to-GND` |
| 保护电路 | J1 外部接口保护 | `connector=J1`；`signals=+5V,SCL,SDA,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示` |
| 总线地址 | QMP6988 I2C 地址 | `device=U2 QMP6988`；`documented_candidate=0x56`；`address_pin=U2 SDO pin5`；`visible_sdo_connection=未显示`；`schematic_address=未标注` |
| 传感器 | QMP6988 测量性能 | `device=U2 QMP6988`；`pressure_range_candidate=30kPa to 110kPa`；`pressure_resolution_candidate=0.06Pa`；`temperature_range_candidate=-40 to 80°C`；`current_candidate=21.4uA`；`schematic_performance_values=未标注` |
| 存储 | 存储器与主控 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> Q1/Q2 -> U2` |

## 待确认事项

- `address.i2c-address-undetermined`：原理图没有打印 I2C 地址，且 U2 SDO（5 脚）没有可见连接；无法仅由本页确认正文中的 0x56 或地址选择状态。（证据：图 ac8c812a1999 / 第 1 页 / U2 SDO/5 脚右侧无连线，整页无 0x56 或地址文字）
- `sensor.performance-undetermined`：原理图只标出 QMP6988 型号及连接，不包含压力/温度量程、分辨率、精度、采样率或工作电流，不能由图纸确认正文中的相关数值。（证据：图 ac8c812a1999 / 第 1 页 / U2 QMP6988 符号仅有型号和引脚，无量程、精度或功耗文字）
- `review.i2c-address`：U2 SDO 实际焊接状态是什么，Unit Mini BPS v1.1 的 I2C 地址是否固定为 0x56？；原因：原理图中 SDO/5 脚没有可见连接，也没有地址文字，无法确定地址选择状态。
- `review.sensor-performance`：该版本 QMP6988 的确认量程、精度、分辨率、温度范围和典型工作电流分别是多少？；原因：这些是器件规格或固件配置参数，原理图没有给出数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ac8c812a1999404d0464121f62fbd7f91099f73feccffa05ab893348dc314f3e` | `https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-4e77d8e1-09d6-43d6-a0da-d7e15d171c79.png` |

---

源文档：`zh_CN/unit/BPS(QMP6988).md`

源文档 SHA-256：`5c09a7a51af15428dd28e0861fff779c9c9049fe2e569983ad13c46dca22640e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
