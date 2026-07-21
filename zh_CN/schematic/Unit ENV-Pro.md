# Unit ENV-Pro 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ENV-Pro |
| SKU | U169 |
| 产品 ID | `unit-env-pro-c6547e5b42d2` |
| 源文档 | `zh_CN/unit/ENV Pro Unit.md` |

## 概述

Unit ENV-Pro 是一块无板载主控的 BME688 环境传感器单元，U1 通过 J1 HY-2.0_IIC 的 SCL/SDA 直接连接外部主机。U2 VRH3301NLX 将 +5V 转换为 +3.3V，为 BME688 的 VDD/VDDIO 与 I2C 上拉供电。BME688 的 CSB 接 +3.3V 选择 I2C，SDO 接 GND；按原理图打印的地址表，该配置对应 7 位地址 0x76。

## 检索关键词

`Unit ENV-Pro`、`U169`、`BME688`、`U1`、`VRH3301NLX`、`U2`、`J1`、`HY-2.0_IIC`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`SDI`、`SCK`、`SDO`、`CSB`、`VDD`、`VDDIO`、`0x76`、`0x77`、`+5V`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`F1 6V@1A`、`PESDNC2FD3V3B`、`PESDNC2FD5VB`、`C1 10uF`、`C2 1uF`、`C3 100nF`、`C4 1uF`、`C5 10uF`、`C6 100nF`、`VOC`、`IAQ`、`temperature`、`humidity`、`barometric pressure`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | BME688 | 环境传感器，使用 I2C 的 SDI/SCK，引脚 SDO 接 GND 配置地址。 | 图 d90e69248f0c / 第 1 页 / 网格 B3-C3，U1 BME688，GND/CSB/SDI/SCK/VDD/GND/VDDIO/SDO 1-8 脚 |
| U2 | VRH3301NLX | +5V 输入到 +3.3V 输出的稳压器，EN 接 +5V。 | 图 d90e69248f0c / 第 1 页 / 网格 B2，U2 VRH3301NLX，VIN/4、VOUT/1、VSS/2/5、EN/3 |
| J1 | HY-2.0_IIC | 四针 Grove I2C 与供电接口，引出 SCL、SDA、VCC 和 GND。 | 图 d90e69248f0c / 第 1 页 / 网格 B1-B2，J1 HY-2.0_IIC 1-4 脚 |
| F1 | 6V@1A | J1 VCC 与 +5V 板内电源之间的串联保险器件。 | 图 d90e69248f0c / 第 1 页 / 网格 B1-B2，J1.3 VCC-F1 6V@1A-+5V |
| D1,D2 | PESDNC2FD3V3B | SCL 与 SDA 的对地 ESD/瞬态保护器件。 | 图 d90e69248f0c / 第 1 页 / 网格 B1，D1/D2 PESDNC2FD3V3B 分别跨接 SCL/SDA 与 GND |
| D3 | PESDNC2FD5VB | J1 VCC/5V 接口节点的对地保护器件。 | 图 d90e69248f0c / 第 1 页 / 网格 B1-B2，D3 PESDNC2FD5VB 跨接 J1.3/F1 前 VCC 节点与 GND |
| R1,R2 | 4.7KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻。 | 图 d90e69248f0c / 第 1 页 / 网格 B2-B3，R1/R2 4.7KΩ 从 SCL/SDA 上拉到 +3.3V |
| C1,C2,C4,C5 | 10uF / 1uF / 1uF / 10uF | U2 输入和输出侧的滤波电容。 | 图 d90e69248f0c / 第 1 页 / 网格 B2，U2 左侧 C1 10uF/C2 1uF 与右侧 C4 1uF/C5 10uF |
| C3,C6 | 100nF | BME688 VDDIO/VDD 的 +3.3V 对地去耦电容。 | 图 d90e69248f0c / 第 1 页 / 网格 C3，U1 右侧 C3/C6 100nF，跨接 +3.3V 与 GND |

## 系统结构

### 整板架构

整板由 U1 BME688、U2 VRH3301NLX、J1、I2C 上拉、保险与接口保护构成；本页未显示 MCU、存储器、晶振、复位、调试或射频电路。

- 参数与网络：`sensor=U1 BME688`；`regulator=U2 VRH3301NLX`；`host_interface=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示`
- 证据：图 d90e69248f0c / 第 1 页 / 第 1 页全图，U1/U2/J1/F1/D1-D3/R1-R2/C1-C6

## 电源

### U2 5V 到 3.3V 稳压

U2 VRH3301NLX 的 VIN（4 脚）与 EN（3 脚）接 +5V，VOUT（1 脚）输出 +3.3V，VSS（2、5 脚）接 GND。

- 参数与网络：`regulator=U2 VRH3301NLX`；`input=VIN pin4/+5V`；`enable=EN pin3/+5V`；`output=VOUT pin1/+3.3V`；`grounds=VSS pins2,5`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B2，U2 VIN/VOUT/VSS/EN 与 +5V/+3.3V/GND

### U2 输入输出滤波

C1 10uF 与 C2 1uF 从 +5V 接 GND；C4 1uF 与 C5 10uF 从 +3.3V 接 GND。

- 参数与网络：`input_caps=C1 10uF,C2 1uF`；`output_caps=C4 1uF,C5 10uF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B2，U2 左右 C1/C2/C4/C5 与 GND

### BME688 去耦

C3 与 C6 均为 100nF，分别从 BME688 的 +3.3V 电源区域接 GND。

- 参数与网络：`capacitors=C3 100nF,C6 100nF`；`rail=+3.3V`；`return=GND`；`sensor=U1 BME688`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 C3，U1 右侧 C3/C6 100nF 至 GND

## 接口

### J1 HY-2.0_IIC

J1.1-J1.4 分别为 IIC_SCL/SCL、IIC_SDA/SDA、VCC/5V 输入、GND。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/5V input`；`pin_4=GND`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B1，J1 1-4 脚与 SCL/SDA/F1/GND

## 总线

### BME688 I2C 模式

U1 CSB（2 脚）连接 +3.3V，SDI/SCK 分别连接 SDA/SCL，因此本板按图使用 BME688 的 I2C 接口而非 SPI 片选模式。

- 参数与网络：`device=U1 BME688`；`csb=+3.3V`；`sda=SDI pin3`；`scl=SCK pin4`；`interface=I2C`
- 证据：图 d90e69248f0c / 第 1 页 / U1 CSB/2、SDI/3、SCK/4 与 +3.3V/SDA/SCL

### I2C 信号与上拉

J1.1 SCL 直接连接 U1 SCK（4 脚），J1.2 SDA 直接连接 U1 SDI（3 脚）；R1/R2 各以 4.7KΩ上拉 SCL/SDA 到 +3.3V。

- 参数与网络：`scl_path=J1.1 -> U1 SCK pin4`；`sda_path=J1.2 -> U1 SDI pin3`；`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`level_shifter=原理图未显示`
- 证据：图 d90e69248f0c / 第 1 页 / J1 SCL/SDA、R1/R2 与 U1 SCK/SDI 同名网络

## 总线地址

### BME688 7 位 I2C 地址

原理图文字明确给出 SDO=0 时地址 0x76、SDO=1 时地址 0x77；当前 U1 SDO（5 脚）接 GND，因此本图配置地址为 0x76。

- 参数与网络：`device=U1 BME688`；`address_pin=SDO pin5`；`address_pin_level=GND/0`；`configured_address=0x76`；`alternate_address=0x77 when SDO=1`；`address_width=7-bit`
- 证据：图 d90e69248f0c / 第 1 页 / U1 SDO/5 到 GND 连接及其下方 7-bit device address 注释

## 时钟

### 时钟、复位与调试

原理图未显示 BME688 外部晶振、时钟输入、复位网络、中断线或调试连接器。

- 参数与网络：`external_crystal=原理图未显示`；`clock=原理图未显示`；`reset=原理图未显示`；`interrupt=原理图未显示`；`debug=原理图未显示`
- 证据：图 d90e69248f0c / 第 1 页 / 第 1 页全图与 U1 可见 1-8 脚，无时钟/复位/中断/调试网络

## 保护电路

### SCL/SDA 接口保护

D1 与 D2 均为 PESDNC2FD3V3B，分别从 SCL 和 SDA 接 GND，位于 J1 接口侧。

- 参数与网络：`scl_protection=D1 PESDNC2FD3V3B to GND`；`sda_protection=D2 PESDNC2FD3V3B to GND`；`connector=J1`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B1，D1/D2 与 SCL/SDA/GND

### 5V 输入保护

J1.3 VCC 经 F1（6V@1A）串联到板内 +5V，D3 PESDNC2FD5VB 从 F1 前的接口电源节点接 GND。

- 参数与网络：`connector_pin=J1.3`；`fuse=F1 6V@1A`；`board_rail=+5V`；`tvs=D3 PESDNC2FD5VB`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B1-B2，J1.3-D3/F1-+5V 路径

## 存储

### 主控与存储

本页未显示 MCU、外部 Flash、EEPROM、SD 卡或其他存储器，BME688 直接通过 I2C 连接主机。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> U1 BME688`
- 证据：图 d90e69248f0c / 第 1 页 / 第 1 页全图，无主控或存储器位号

## 传感器

### U1 BME688

U1.1 与 U1.7 为 GND，U1.2 CSB 接 +3.3V，U1.3 SDI 接 SDA，U1.4 SCK 接 SCL，U1.5 SDO 接 GND，U1.6 VDDIO 与 U1.8 VDD 接 +3.3V。

- 参数与网络：`pin_1=GND`；`pin_2=CSB/+3.3V`；`pin_3=SDI/SDA`；`pin_4=SCK/SCL`；`pin_5=SDO/GND`；`pin_6=VDDIO/+3.3V`；`pin_7=GND`；`pin_8=VDD/+3.3V`
- 证据：图 d90e69248f0c / 第 1 页 / 网格 B3-C3，U1 BME688 1-8 脚全部网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `sensor=U1 BME688`；`regulator=U2 VRH3301NLX`；`host_interface=J1 HY-2.0_IIC`；`controller=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示` |
| 传感器 | U1 BME688 | `pin_1=GND`；`pin_2=CSB/+3.3V`；`pin_3=SDI/SDA`；`pin_4=SCK/SCL`；`pin_5=SDO/GND`；`pin_6=VDDIO/+3.3V`；`pin_7=GND`；`pin_8=VDD/+3.3V` |
| 总线 | BME688 I2C 模式 | `device=U1 BME688`；`csb=+3.3V`；`sda=SDI pin3`；`scl=SCK pin4`；`interface=I2C` |
| 总线地址 | BME688 7 位 I2C 地址 | `device=U1 BME688`；`address_pin=SDO pin5`；`address_pin_level=GND/0`；`configured_address=0x76`；`alternate_address=0x77 when SDO=1`；`address_width=7-bit` |
| 总线地址 | 0x76 与正文 0x77 冲突 | `schematic_address=0x76`；`documented_address=0x77`；`sdo_connection=GND`；`resolution=需 PCB/实机确认` |
| 电源 | U2 5V 到 3.3V 稳压 | `regulator=U2 VRH3301NLX`；`input=VIN pin4/+5V`；`enable=EN pin3/+5V`；`output=VOUT pin1/+3.3V`；`grounds=VSS pins2,5` |
| 电源 | U2 输入输出滤波 | `input_caps=C1 10uF,C2 1uF`；`output_caps=C4 1uF,C5 10uF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | BME688 去耦 | `capacitors=C3 100nF,C6 100nF`；`rail=+3.3V`；`return=GND`；`sensor=U1 BME688` |
| 接口 | J1 HY-2.0_IIC | `reference=J1`；`part_number=HY-2.0_IIC`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC/5V input`；`pin_4=GND` |
| 总线 | I2C 信号与上拉 | `scl_path=J1.1 -> U1 SCK pin4`；`sda_path=J1.2 -> U1 SDI pin3`；`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`level_shifter=原理图未显示` |
| 保护电路 | SCL/SDA 接口保护 | `scl_protection=D1 PESDNC2FD3V3B to GND`；`sda_protection=D2 PESDNC2FD3V3B to GND`；`connector=J1` |
| 保护电路 | 5V 输入保护 | `connector_pin=J1.3`；`fuse=F1 6V@1A`；`board_rail=+5V`；`tvs=D3 PESDNC2FD5VB` |
| 存储 | 主控与存储 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_path=J1 I2C -> U1 BME688` |
| 时钟 | 时钟、复位与调试 | `external_crystal=原理图未显示`；`clock=原理图未显示`；`reset=原理图未显示`；`interrupt=原理图未显示`；`debug=原理图未显示` |
| 传感器 | BME688 测量与派生参数 | `device=U1 BME688`；`measurements_candidate=gas/VOC,temperature,humidity,pressure`；`derived_candidate=CO2 equivalent,IAQ`；`scan_speed_candidate=10.8s`；`performance_values=原理图未标注` |

## 待确认事项

- `address.documentation-conflict`：当前原理图的 SDO=0 配置对应 0x76，但产品正文写 0x77；需要通过 PCB/实机确认是原理图连接、装配版本还是正文地址存在偏差。（证据：图 d90e69248f0c / 第 1 页 / U1 SDO/5=GND 与地址表 SDO=0,ADDR 0x76）
- `sensor.performance-undetermined`：原理图只显示 BME688 型号和电气连接，没有 VOC、CO₂ 当量、IAQ 算法、温湿度/气压范围、精度、扫描周期或功耗数值，不能由图纸确认正文性能参数。（证据：图 d90e69248f0c / 第 1 页 / U1 BME688 符号仅含型号、接口和电源引脚，无性能文字）
- `review.address-conflict`：量产 PCB 上 BME688 SDO 实际接 GND 还是 +3.3V，实机 I2C 地址是 0x76 还是 0x77？；原因：原理图明确显示 SDO=0/0x76，但产品正文标记 0x77，二者冲突。
- `review.sensor-performance`：该产品确认输出哪些原始/派生环境参数，量程、精度、扫描周期和功耗分别是多少？；原因：这些属于 BME688 规格或上层算法行为，原理图没有给出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d90e69248f0c5ca35ff09097dae86df2bb1c742ca9b6d92ad08cb677be50ffb8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/622/Sch_UNIT-ENV_Pro_sch_01.png` |

---

源文档：`zh_CN/unit/ENV Pro Unit.md`

源文档 SHA-256：`edccc1af256514ad1f454ec0231c89dff2b00f4c7ae5eef46e01df0d4784858e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
