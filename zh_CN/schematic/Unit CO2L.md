# Unit CO2L 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CO2L |
| SKU | U104 |
| 产品 ID | `unit-co2l-f63045a68676` |
| 源文档 | `zh_CN/unit/CO2L.md` |

## 概述

Unit CO2L 是一块无板载主控的 SCD41 传感器单元，U2 通过 J1 HY-2.0_IIC 的 SCL/SDA 直接连接外部 I2C 主机。U1 VRH3301NLX 将 J1 的 +5V 转换为 +3.3V，并为 SCD41 的 VDD/VDDH 及 I2C 上拉供电。J1 电源串联 F1，SCL/SDA、+3.3V 与 5V VCC 分别配置 RLSD52A031V 或 LESD3Z5.0CMT1G 对地保护。

## 检索关键词

`Unit CO2L`、`U104`、`SCD41`、`U2`、`VRH3301NLX`、`U1`、`J1`、`HY-2.0_IIC`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`VDD`、`VDDH`、`+5V`、`+3.3V`、`R3 15KΩ`、`R4 15KΩ`、`F1 6V@1A`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`C1 1uF`、`C2 1uF`、`C5 100nF`、`C6 100nF`、`0x62`、`CO2 sensor`、`temperature sensor`、`humidity sensor`、`I2C pull-up`、`Grove Port A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SCD41 | CO₂/环境传感器，SCL/SDA 连接 I2C，总电源引脚 VDD/VDDH 接 +3.3V。 | 图 1c82ca74584a / 第 1 页 / 网格 C2，U2 SCD41，VDD/7、VDDH/19、SCL/9、SDA/10、GND/6 |
| U1 | VRH3301NLX | +5V 输入到 +3.3V 输出的稳压器，EN 接 +5V。 | 图 1c82ca74584a / 第 1 页 / 网格 B2，U1 VRH3301NLX，VIN/4、VOUT/1、VSS/2/5、EN/3 |
| J1 | HY-2.0_IIC | 四针 Grove I2C 与供电接口，引出 SCL、SDA、+5V 和 GND。 | 图 1c82ca74584a / 第 1 页 / 网格 B4，J1 HY-2.0_IIC 1-4 脚 |
| F1 | 6V@1A | +5V 到 J1 VCC 的串联保险器件。 | 图 1c82ca74584a / 第 1 页 / 网格 B3-B4，+5V-F1 6V@1A-J1.3 VCC |
| D1,D2 | RLSD52A031V | J1 SCL 与 SDA 的对地 ESD/瞬态保护器件。 | 图 1c82ca74584a / 第 1 页 / 网格 B3-B4，D1/D2 RLSD52A031V 分别跨接 SCL/SDA 与 GND |
| D3 | RLSD52A031V | +3.3V 电源轨的对地瞬态保护器件。 | 图 1c82ca74584a / 第 1 页 / 网格 B2，D3 RLSD52A031V 跨接 +3.3V 与 GND |
| D4 | LESD3Z5.0CMT1G | J1 VCC 5V 节点的对地保护器件。 | 图 1c82ca74584a / 第 1 页 / 网格 C3-C4，J1.3 VCC 节点至 D4 LESD3Z5.0CMT1G/GND |
| R3,R4 | 15KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻。 | 图 1c82ca74584a / 第 1 页 / 网格 C1-C2，R3 15KΩ 上拉 SCL，R4 15KΩ 上拉 SDA |
| C1,C2,C5,C6 | 1uF / 1uF / 100nF / 100nF | 稳压器输入输出与 SCD41 +3.3V 供电的滤波/去耦电容。 | 图 1c82ca74584a / 第 1 页 / 网格 B2 C1/C2 1uF 与网格 C2 C5/C6 100nF，均接 GND |

## 系统结构

### 整板架构

整板由 U2 SCD41、U1 VRH3301NLX、J1、I2C 上拉和保护/去耦器件构成；本页未显示 MCU、存储器、晶振、复位、调试或射频电路。

- 参数与网络：`sensor=U2 SCD41`；`regulator=U1 VRH3301NLX`；`host_interface=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示`
- 证据：图 1c82ca74584a / 第 1 页 / 第 1 页全图，U1/U2/J1 与所有阻容、保险和保护器件

## 电源

### U1 5V 到 3.3V 稳压

U1 VRH3301NLX 的 VIN（4 脚）与 EN（3 脚）接 +5V，VOUT（1 脚）输出 +3.3V，VSS（2、5 脚）接 GND。

- 参数与网络：`regulator=U1 VRH3301NLX`；`input=VIN pin4/+5V`；`enable=EN pin3/+5V`；`output=VOUT pin1/+3.3V`；`grounds=VSS pins2,5`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B2，U1 VIN/VOUT/VSS/EN 与 +5V/+3.3V/GND

### U1 输入输出滤波

C1 1uF 从 +5V/U1 VIN 接 GND，C2 1uF 从 +3.3V/U1 VOUT 接 GND。

- 参数与网络：`input_capacitor=C1 1uF +5V-to-GND`；`output_capacitor=C2 1uF +3.3V-to-GND`；`regulator=U1 VRH3301NLX`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B1-B2，U1 左右两侧 C1/C2

### SCD41 去耦

C5 与 C6 均为 100nF，分别从 +3.3V 接 GND，为 SCD41 电源区域提供去耦。

- 参数与网络：`capacitors=C5 100nF,C6 100nF`；`rail=+3.3V`；`return=GND`；`sensor=U2 SCD41`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 C2，U2 右侧 C5/C6 100nF 至 GND

## 接口

### J1 HY-2.0_IIC

J1.1-J1.4 分别为 IIC_SCL/SCL、IIC_SDA/SDA、VCC/+5V、GND。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B4，J1 1-4 脚双侧网络/功能标注

## 总线

### SCD41 I2C

J1.1 SCL 直接连接 U2 SCL（9 脚），J1.2 SDA 直接连接 U2 SDA（10 脚）；两条信号均工作在由 +3.3V 上拉定义的板侧电源域。

- 参数与网络：`bus=I2C`；`device=U2 SCD41`；`scl_path=J1.1 -> U2 SCL pin9`；`sda_path=J1.2 -> U2 SDA pin10`；`pullup_rail=+3.3V`；`level_shifter=原理图未显示`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B3-C4 的 J1 SCL/SDA 与网格 C1-C2 的 U2 SCL/SDA 同名网络

### I2C 上拉

R3 15KΩ将 SCL 上拉到 +3.3V，R4 15KΩ将 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R3 15KΩ to +3.3V`；`sda_pullup=R4 15KΩ to +3.3V`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 C1-C2，R3/R4 15KΩ 与 SCL/SDA/+3.3V

## 时钟

### 时钟与复位

原理图未显示 SCD41 外部晶振、时钟输入、复位引脚或调试连接器。

- 参数与网络：`external_crystal=原理图未显示`；`clock_input=原理图未显示`；`reset=原理图未显示`；`debug=原理图未显示`
- 证据：图 1c82ca74584a / 第 1 页 / 第 1 页全图与 U2 SCD41 可见引脚，无时钟/复位/调试网络

## 保护电路

### SCL/SDA 保护

D1 与 D2 均为 RLSD52A031V，分别从 SCL 和 SDA 接 GND，位于 J1 接口侧。

- 参数与网络：`scl_protection=D1 RLSD52A031V to GND`；`sda_protection=D2 RLSD52A031V to GND`；`connector=J1`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B3-B4，D1/D2 与 SCL/SDA/GND

### 5V 与 3.3V 电源保护

+5V 经 F1（6V@1A）串联到 J1.3 VCC，D4 LESD3Z5.0CMT1G 从该 VCC 节点接 GND；D3 RLSD52A031V 从 +3.3V 接 GND。

- 参数与网络：`fuse=F1 6V@1A`；`connector_power=J1.3 VCC`；`vcc_protection=D4 LESD3Z5.0CMT1G`；`rail_3v3_protection=D3 RLSD52A031V`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 B2 D3 与网格 B3-C4 +5V-F1-J1/D4

## 存储

### 主控与存储

本页未显示 MCU、外部 Flash、EEPROM、SD 卡或其他存储器，SCD41 直接通过 I2C 连接 J1。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> U2 SCD41`
- 证据：图 1c82ca74584a / 第 1 页 / 第 1 页全图，无主控或存储器位号

## 传感器

### U2 SCD41

U2 SCD41 的 VDD（7 脚）与 VDDH（19 脚）接 +3.3V，SCL（9 脚）接 SCL，SDA（10 脚）接 SDA，GND（6 脚）接地。

- 参数与网络：`reference=U2`；`part_number=SCD41`；`pin_7=VDD/+3.3V`；`pin_19=VDDH/+3.3V`；`pin_9=SCL`；`pin_10=SDA`；`pin_6=GND`
- 证据：图 1c82ca74584a / 第 1 页 / 网格 C2，U2 SCD41 五个可见功能引脚及网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `sensor=U2 SCD41`；`regulator=U1 VRH3301NLX`；`host_interface=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示` |
| 传感器 | U2 SCD41 | `reference=U2`；`part_number=SCD41`；`pin_7=VDD/+3.3V`；`pin_19=VDDH/+3.3V`；`pin_9=SCL`；`pin_10=SDA`；`pin_6=GND` |
| 电源 | U1 5V 到 3.3V 稳压 | `regulator=U1 VRH3301NLX`；`input=VIN pin4/+5V`；`enable=EN pin3/+5V`；`output=VOUT pin1/+3.3V`；`grounds=VSS pins2,5` |
| 电源 | U1 输入输出滤波 | `input_capacitor=C1 1uF +5V-to-GND`；`output_capacitor=C2 1uF +3.3V-to-GND`；`regulator=U1 VRH3301NLX` |
| 电源 | SCD41 去耦 | `capacitors=C5 100nF,C6 100nF`；`rail=+3.3V`；`return=GND`；`sensor=U2 SCD41` |
| 接口 | J1 HY-2.0_IIC | `reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/+5V`；`pin_4=GND` |
| 总线 | SCD41 I2C | `bus=I2C`；`device=U2 SCD41`；`scl_path=J1.1 -> U2 SCL pin9`；`sda_path=J1.2 -> U2 SDA pin10`；`pullup_rail=+3.3V`；`level_shifter=原理图未显示` |
| 总线 | I2C 上拉 | `scl_pullup=R3 15KΩ to +3.3V`；`sda_pullup=R4 15KΩ to +3.3V` |
| 保护电路 | SCL/SDA 保护 | `scl_protection=D1 RLSD52A031V to GND`；`sda_protection=D2 RLSD52A031V to GND`；`connector=J1` |
| 保护电路 | 5V 与 3.3V 电源保护 | `fuse=F1 6V@1A`；`connector_power=J1.3 VCC`；`vcc_protection=D4 LESD3Z5.0CMT1G`；`rail_3v3_protection=D3 RLSD52A031V` |
| 存储 | 主控与存储 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> U2 SCD41` |
| 时钟 | 时钟与复位 | `external_crystal=原理图未显示`；`clock_input=原理图未显示`；`reset=原理图未显示`；`debug=原理图未显示` |
| 总线地址 | SCD41 I2C 地址 | `device=U2 SCD41`；`documented_candidate=0x62`；`schematic_address=未标注`；`address_select=未显示` |
| 传感器 | SCD41 测量性能与低功耗模式 | `device=U2 SCD41`；`co2_range_candidate=400-5000ppm`；`accuracy_candidate=±(40ppm+5% of reading)`；`temperature_candidate=-10 to 60°C`；`humidity_candidate=0 to 95%RH`；`single_shot_mode=原理图未标注` |

## 待确认事项

- `address.i2c-address-undetermined`：原理图没有打印 I2C 地址或硬件地址选择网络，无法仅由本页确认产品正文中的 0x62。（证据：图 1c82ca74584a / 第 1 页 / U2 SCD41 与 SCL/SDA 路径，整页无 0x62 或地址配置文字）
- `sensor.measurement-performance-undetermined`：原理图只显示 SCD41 型号和电气连接，没有 CO₂/温度/湿度量程、精度、采样模式或功耗参数，不能由图纸确认 400-5000ppm、精度公式或单次测量模式。（证据：图 1c82ca74584a / 第 1 页 / U2 SCD41 符号仅含型号与 VDD/VDDH/SCL/SDA/GND 引脚）
- `review.i2c-address`：Unit CO2L 的 SCD41 I2C 地址是否固定为 0x62，是否存在地址配置方式？；原因：原理图没有地址文字或地址选择硬件。
- `review.measurement-performance`：该版本确认的 CO₂/温湿度量程、精度、采样周期和单次测量功耗分别是多少？；原因：这些属于传感器规格或工作模式，原理图没有给出数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1c82ca74584a3b9d13217288bf1edf55bca463b5a11e8aec6a094e674ad90213` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/591/SCH_UNIT_CO2L_sch_01.png` |

---

源文档：`zh_CN/unit/CO2L.md`

源文档 SHA-256：`f56d059d9127ae4e0cc63bda803e1256dec6cca53140e1effad4b6d470d9f5c6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
