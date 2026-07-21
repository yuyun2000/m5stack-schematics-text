# Unit Gesture 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Gesture |
| SKU | U127 |
| 产品 ID | `unit-gesture-b878d4a41acb` |
| 源文档 | `zh_CN/unit/Gesture.md` |

## 概述

Unit Gesture 以 U2 PAJ7620U2 为手势传感器，通过 J1 的 SCL、SDA 接入 I2C，总线由 R1、R2 各 4.7 kΩ 上拉至 +3.3V。U4 HT7533 从 VCC 生成 +3.3V，供 U2 的 VBUS/VDD；U1、U3 SPX3819M5-L-3-3 从 VCC 生成 3.3V，供 U2 的 VLED。U2 还引出未外接的 INT 网络，GPIO0 至 GPIO3 与 TESTMD 在本页未连接。

## 检索关键词

`Unit Gesture`、`U127`、`PAJ7620U2`、`SPX3819M5-L-3-3`、`HT7533`、`I2C`、`0x73`、`SCL`、`SDA`、`INT`、`INT_IN`、`VBUS`、`VDD`、`VLED`、`GPIO0`、`GPIO1`、`GPIO2`、`GPIO3`、`TESTMD`、`IIC_Socket_4P`、`J1`、`VCC`、`+3.3V`、`3.3V`、`R1 4.7K`、`R2 4.7K`、`C2 470pF`、`C5 470pF`、`120Hz`、`240Hz`、`5cm-15cm`、`2.2mA`、`9 gestures`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | PAJ7620U2 | I2C 三维手势传感器 | 图 4e53962fd154 / 第 1 页 / 页 1 上中部 U2 器件框下方标注 PAJ7620U2 |
| U1 | SPX3819M5-L-3-3 | VCC 至 3.3V 的传感器 VLED 电源稳压器之一 | 图 4e53962fd154 / 第 1 页 / 页 1 右上 U1，标注 SPX3819M5-L-3-3，IN/EN 接 VCC、OUT 接 3.3V |
| U3 | SPX3819M5-L-3-3 | VCC 至 3.3V 的传感器 VLED 电源稳压器之一 | 图 4e53962fd154 / 第 1 页 / 页 1 右中部 U3，标注 SPX3819M5-L-3-3，IN/EN 接 VCC、OUT 接 3.3V |
| U4 | HT7533 | VCC 至 +3.3V 的传感器逻辑电源稳压器 | 图 4e53962fd154 / 第 1 页 / 页 1 左下 U4，标注 HT7533，VIN 接 VCC、VOUT 接 +3.3V |
| J1 | IIC_Socket_4P | 四针 I2C 与 VCC 电源接口 | 图 4e53962fd154 / 第 1 页 / 页 1 下中部 J1，标注 IIC_Socket_4P，针脚为 IIC_SCL、IIC_SDA、VCC、GND |

## 系统结构

### U2

U2 的型号为 PAJ7620U2，连接 I2C 的 SCL/SDA、INT、两组供电网络及若干未使用 GPIO。

- 参数与网络：`reference=U2`；`part_number=PAJ7620U2`；`host_bus=I2C`；`interrupt_net=INT`；`logic_rail=+3.3V`；`led_rail=3.3V`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 上中部 U2 型号及全部引脚和网络标注

## 电源

### U2 VBUS 与 VDD

U2 的 VBUS 引脚 1 和 VDD 引脚 12 连接 +3.3V，GND 引脚 10、6 连接 GND。

- 参数与网络：`logic_supply_pins=VBUS/pin 1,VDD/pin 12`；`logic_rail=+3.3V`；`ground_pins=pin 10,pin 6`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 U2 的 VBUS/VDD、+3.3V 以及两个 GND 引脚

### U2 VLED

U2 的 VLED 引脚 11 连接名为 3.3V 的电源网络，与 VBUS/VDD 所用的 +3.3V 网络在图中采用不同网络名。

- 参数与网络：`vled_pin=U2 pin 11`；`vled_rail=3.3V`；`logic_rail=+3.3V`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 U2 右侧 VLED 引脚 11 的 3.3V 标签及 VBUS/VDD 的 +3.3V 标签

### U4 HT7533

U4 HT7533 的 VIN 引脚 2 接 VCC，VOUT 引脚 3 输出 +3.3V，GND 引脚 1 接地。

- 参数与网络：`reference=U4`；`part_number=HT7533`；`input=VIN/pin 2/VCC`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 左下 U4 的 VIN/VOUT/GND 引脚与 VCC/+3.3V/GND 网络

### U4 输入输出电容

U4 输入侧 C9 10 uF 连接在 VCC 与 GND 之间；输出侧 C7 100 nF 和 C8 10 uF 并联在 +3.3V 与 GND 之间。

- 参数与网络：`input_capacitor=C9 10uF`；`input_rail=VCC`；`output_capacitors=C7 100nF,C8 10uF`；`output_rail=+3.3V`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 左下 U4 两侧 C7、C8、C9 及电源网络

### U1 SPX3819M5-L-3-3

U1 的 IN 引脚 1 与 EN 引脚 3 接 VCC，OUT 引脚 5 输出 3.3V，GND 引脚 2 接地；BYP/ADJ 引脚 4 通过 C2 470 pF 接地。

- 参数与网络：`reference=U1`；`part_number=SPX3819M5-L-3-3`；`input_enable=IN/pin 1 and EN/pin 3 to VCC`；`output=OUT/pin 5/3.3V`；`bypass=BYP/ADJ pin 4,C2 470pF to GND`；`ground=GND/pin 2`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 右上 U1 全部引脚、VCC/3.3V 网络与 C2

### U1 输入输出电容

U1 输入侧 C1 10 uF 连接在 VCC 与 GND 之间；输出侧 C3 100 nF 和 C4 10 uF 并联在 3.3V 与 GND 之间。

- 参数与网络：`input_capacitor=C1 10uF`；`output_capacitors=C3 100nF,C4 10uF`；`input_rail=VCC`；`output_rail=3.3V`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 右上 U1 周围 C1、C3、C4 与电源网络

### U3 SPX3819M5-L-3-3

U3 的 IN 引脚 1 与 EN 引脚 3 接 VCC，OUT 引脚 5 输出 3.3V，GND 引脚 2 接地；BYP/ADJ 引脚 4 通过 C5 470 pF 接地，输出侧 C6 100 nF 接地。

- 参数与网络：`reference=U3`；`part_number=SPX3819M5-L-3-3`；`input_enable=IN/pin 1 and EN/pin 3 to VCC`；`output=OUT/pin 5/3.3V`；`bypass=BYP/ADJ pin 4,C5 470pF to GND`；`output_capacitor=C6 100nF`；`ground=GND/pin 2`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 右中部 U3 全部引脚、VCC/3.3V 网络及 C5/C6

## 接口

### J1 I2C 接口

J1 的 1 至 4 脚依次连接 SCL、SDA、VCC 和 GND，器件内针脚名称依次为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 下中部 J1 的 1 至 4 脚号、外部网络和内部针脚名称

## 总线

### U2 与 J1 的 I2C 总线

SCL、SDA 分别连接 U2 的 SCL 引脚 5、SDA 引脚 2，并连接 J1 的 1、2 脚。

- 参数与网络：`device=U2 PAJ7620U2`；`connector=J1`；`scl=U2 pin 5 -> J1 pin 1`；`sda=U2 pin 2 -> J1 pin 2`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 左侧 SCL/SDA 网络、U2 引脚 5/2 与下方 J1 引脚 1/2

### I2C 上拉

R1、R2 均为 4.7 kΩ，分别将 SCL、SDA 上拉至 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7k to +3.3V`；`sda_pullup=R2 4.7k to +3.3V`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 左侧 R1/R2 4.7KΩ 与 SCL/SDA、+3.3V 网络

## GPIO 与控制信号

### U2 INT

U2 的 INT_IN 引脚 3 连接 INT 网络；该网络在本页没有连接到 J1 或其他器件。

- 参数与网络：`device_pin=U2 INT_IN/pin 3`；`network=INT`；`external_connector=null`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 上中部 U2 左侧 INT 网络与 INT_IN 引脚 3，线段左端未外接

### U2 未使用引脚

U2 的 GPIO0 引脚 13、GPIO1 引脚 9、GPIO2 引脚 8、GPIO3 引脚 7 和 TESTMD 引脚 4 在本页标为未连接。

- 参数与网络：`unconnected_pins=GPIO0/pin 13,GPIO1/pin 9,GPIO2/pin 8,GPIO3/pin 7,TESTMD/pin 4`
- 证据：图 4e53962fd154 / 第 1 页 / 页 1 U2 右下 GPIO0-GPIO3 与 TESTMD 引脚末端的未连接叉号

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | U2 | `reference=U2`；`part_number=PAJ7620U2`；`host_bus=I2C`；`interrupt_net=INT`；`logic_rail=+3.3V`；`led_rail=3.3V` |
| 接口 | J1 I2C 接口 | `reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:VCC,4:GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | U2 与 J1 的 I2C 总线 | `device=U2 PAJ7620U2`；`connector=J1`；`scl=U2 pin 5 -> J1 pin 1`；`sda=U2 pin 2 -> J1 pin 2` |
| 总线 | I2C 上拉 | `scl_pullup=R1 4.7k to +3.3V`；`sda_pullup=R2 4.7k to +3.3V` |
| 总线地址 | PAJ7620U2 I2C 地址 | `documented_address=0x73`；`schematic_address=null`；`hardware_address_select=null` |
| GPIO 与控制信号 | U2 INT | `device_pin=U2 INT_IN/pin 3`；`network=INT`；`external_connector=null` |
| GPIO 与控制信号 | U2 未使用引脚 | `unconnected_pins=GPIO0/pin 13,GPIO1/pin 9,GPIO2/pin 8,GPIO3/pin 7,TESTMD/pin 4` |
| 电源 | U2 VBUS 与 VDD | `logic_supply_pins=VBUS/pin 1,VDD/pin 12`；`logic_rail=+3.3V`；`ground_pins=pin 10,pin 6` |
| 电源 | U2 VLED | `vled_pin=U2 pin 11`；`vled_rail=3.3V`；`logic_rail=+3.3V` |
| 电源 | U4 HT7533 | `reference=U4`；`part_number=HT7533`；`input=VIN/pin 2/VCC`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1` |
| 电源 | U4 输入输出电容 | `input_capacitor=C9 10uF`；`input_rail=VCC`；`output_capacitors=C7 100nF,C8 10uF`；`output_rail=+3.3V` |
| 电源 | U1 SPX3819M5-L-3-3 | `reference=U1`；`part_number=SPX3819M5-L-3-3`；`input_enable=IN/pin 1 and EN/pin 3 to VCC`；`output=OUT/pin 5/3.3V`；`bypass=BYP/ADJ pin 4,C2 470pF to GND`；`ground=GND/pin 2` |
| 电源 | U1 输入输出电容 | `input_capacitor=C1 10uF`；`output_capacitors=C3 100nF,C4 10uF`；`input_rail=VCC`；`output_rail=3.3V` |
| 电源 | U3 SPX3819M5-L-3-3 | `reference=U3`；`part_number=SPX3819M5-L-3-3`；`input_enable=IN/pin 1 and EN/pin 3 to VCC`；`output=OUT/pin 5/3.3V`；`bypass=BYP/ADJ pin 4,C5 470pF to GND`；`output_capacitor=C6 100nF`；`ground=GND/pin 2` |
| 电源 | U1 与 U3 的 3.3V 电源路径 | `regulators=U1,U3`；`input_rail=VCC`；`shared_output_rail=3.3V`；`assembly_population=null` |
| 传感器 | 手势识别性能 | `documented_gestures=9`；`documented_typical_rate_hz=120`；`documented_max_rate_hz=240`；`documented_distance_cm=5-15`；`documented_current_ma=2.2`；`schematic_performance=null` |

## 待确认事项

- `address.i2c`：产品正文标注 I2C 地址 0x73，但本页原理图没有地址值或地址选择网络。（证据：图 4e53962fd154 / 第 1 页 / 页 1 SCL/SDA 从 J1 至 U2 的完整链路未标注地址）
- `power.vled_parallel_population`：图中 U1 与 U3 均标为 SPX3819M5-L-3-3，输入均接 VCC、输出均接 3.3V；原理图未标明二者是否同时装配或为替代料位。（证据：图 4e53962fd154 / 第 1 页 / 页 1 右上与右中 U1/U3 两个同型号稳压器及相同 VCC、3.3V 网络）
- `sensor.performance`：产品正文描述 9 种手势、典型 120 Hz、最大 240 Hz、5 至 15 cm 距离和 2.2 mA 工作电流；本页原理图没有这些性能参数。（证据：图 4e53962fd154 / 第 1 页 / 页 1 U2 PAJ7620U2 器件框及外围电路未标注识别种类、频率、距离或电流）
- `review.i2c_address`：PAJ7620U2 在该产品中的 I2C 地址是否固定为 0x73？；原因：原理图没有地址标注或地址选择网络。
- `review.vled_regulator_population`：U1 与 U3 是否同时装配，还是不同硬件版本或替代 BOM 的二选一料位？；原因：两个同型号稳压器在图中具有相同输入与输出网，但没有 DNP 或装配选择标注。
- `review.sensor_performance`：9 种手势、120/240 Hz、5-15 cm 和 2.2 mA 参数适用于哪个工作模式与传感器配置？；原因：这些是传感器或固件性能参数，原理图未提供工作模式条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4e53962fd154778c4130c0deb103cc3d443ab50cd3fcf6a4a484612fc01bb0a7` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-023620e1-ce53-412b-a928-eb79681e0af6.webp` |

---

源文档：`zh_CN/unit/Gesture.md`

源文档 SHA-256：`800e2b0f89bebcbd88b66b57911fecb7b49574d715c401b70315c06aabf43d50`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
