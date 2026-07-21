# Unit ENV-IV 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ENV-IV |
| SKU | U001-D |
| 产品 ID | `unit-env-iv-911c8353d3dd` |
| 源文档 | `zh_CN/unit/Unit_ENV-IV.md` |

## 概述

Unit ENV-IV 由 U1 SHT40-AD1B 与 U2 BMP280 两个传感器共享 SDA/SCL 总线，J1 负责引出 IIC_SCL、IIC_SDA、VCC 和 GND。U3 HT7533 将输入 VCC 转换为 +3.3V，为两个传感器及 I2C 上拉网络供电。SHT40 地址在图中明确标注为 0x44；BMP280 的 SDO 接 GND，但原理图没有直接写出对应地址值。

## 检索关键词

`Unit ENV-IV`、`U001-D`、`SHT40-AD1B`、`SHT40`、`0x44`、`BMP280`、`HT7533`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`VCC`、`+3.3V`、`IIC_Socket_4P`、`J1`、`R1 4.7KΩ`、`R2 4.7KΩ`、`BMP280 SDO`、`BMP280 CSB`、`温湿度传感器`、`气压传感器`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT40-AD1B | 共享 I2C 总线的温湿度传感器 | 图 40c5d4e292bb / 第 1 页 / 网格 B2，U1 四引脚器件，器件值标注 SHT40-AD1B，SDA/SCL 接同名网络 |
| U2 | BMP280 | 共享 I2C 总线的气压传感器 | 图 40c5d4e292bb / 第 1 页 / 网格 C2，U2 八引脚器件，器件值标注 BMP280，SCK 接 SCL、SDI 接 SDA |
| U3 | HT7533 | VCC 到 +3.3V 的线性稳压器 | 图 40c5d4e292bb / 第 1 页 / 网格 C3，U3 三引脚器件，器件值 HT7533，VIN 接 VCC、VOUT 接 +3.3V |
| J1 | IIC_Socket_4P | I2C、输入电源和地的四针外部接口 | 图 40c5d4e292bb / 第 1 页 / 网格 B3，J1 IIC_Socket_4P，pin1-pin4 标注 IIC_SCL、IIC_SDA、VCC、GND |

## 系统结构

### Unit ENV-IV 传感器架构

U1 SHT40-AD1B 与 U2 BMP280 共用 SCL、SDA 和 +3.3V，J1 引出 I2C 与 VCC/GND，U3 HT7533 从 VCC 生成 +3.3V。

- 参数与网络：`sensor_1=U1 SHT40-AD1B`；`sensor_2=U2 BMP280`；`bus=SCL,SDA`；`sensor_rail=+3.3V`；`regulator=U3 HT7533`；`connector=J1 IIC_Socket_4P`
- 证据：图 40c5d4e292bb / 第 1 页 / 整页 B2-C3，U1、U2、U3 与 J1 的总线和电源网络

## 电源

### U3 HT7533 稳压路径

U3 HT7533 的 VIN pin2 连接 VCC，VOUT pin3 连接 +3.3V，GND pin1 连接 GND。

- 参数与网络：`reference=U3`；`part_number=HT7533`；`pinout=1:GND,2:VIN/VCC,3:VOUT/+3.3V`；`input_rail=VCC`；`output_rail=+3.3V`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 C3，U3 HT7533 的 VOUT pin3、VIN pin2 与 GND pin1

### VCC 输入去耦

C2 100 nF 与 C5 10 uF 分别跨接 VCC 与 GND。

- 参数与网络：`rail=VCC`；`capacitors=C2 100nF,C5 10uF`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B3 的 C2 100nF 与网格 C3 的 C5 10uF，均连接 VCC 和 GND

### +3.3V 输出滤波

C3 100 nF 与 C4 10 uF 分别跨接 +3.3V 与 GND。

- 参数与网络：`rail=+3.3V`；`capacitors=C3 100nF,C4 10uF`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 C2-C3，U3 VOUT 左侧 +3.3V 网络上的 C3 100nF 与 C4 10uF

### SHT40 电源去耦

C1 100 nF 跨接 +3.3V 与 GND，位于 U1 SHT40-AD1B 电源区域。

- 参数与网络：`capacitor=C1 100nF`；`rail=+3.3V`；`device=U1 SHT40-AD1B`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B1-B2，U1 左侧 C1 100nF 的 +3.3V-GND 支路

## 接口

### J1 I2C 接口

J1 的 pin1 至 pin4 依次连接 IIC_SCL、IIC_SDA、VCC 和 GND；板内对应网络名为 SCL、SDA、VCC 和 GND。

- 参数与网络：`reference=J1`；`part_number=IIC_Socket_4P`；`pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC,4:GND`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B3，J1 四个脚号、内部端名及左侧 SCL/SDA/VCC/GND 网络

## 总线

### 共享 I2C 总线

SCL 网络同时连接 J1 pin1、U1 SCL pin2 与 U2 SCK pin4；SDA 网络同时连接 J1 pin2、U1 SDA pin1 与 U2 SDI pin3。

- 参数与网络：`scl_path=J1 pin1 -> SCL -> U1 pin2 SCL,U2 pin4 SCK`；`sda_path=J1 pin2 -> SDA -> U1 pin1 SDA,U2 pin3 SDI`；`devices=U1 SHT40-AD1B,U2 BMP280`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B2-B3 与 C2，SCL/SDA 网络在 J1、U1 和 U2 之间的连接

### I2C 上拉电阻

R1 4.7 kΩ 将 SCL 上拉到 +3.3V，R2 4.7 kΩ 将 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7kΩ to +3.3V`；`sda_pullup=R2 4.7kΩ to +3.3V`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B2-B3，J1 左上方 R1/R2 4.7KΩ 至 +3.3V 的上拉支路

### BMP280 I2C 接线模式

U2 CSB pin2 连接 +3.3V，SCK pin4 作为 SCL，SDI pin3 作为 SDA，SDO pin5 连接 GND。

- 参数与网络：`csb=pin2 -> +3.3V`；`scl=pin4 SCK -> SCL`；`sda=pin3 SDI -> SDA`；`sdo=pin5 -> GND`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 C2，U2 CSB/SCK/SDI/SDO 的脚号和网络连接

## 总线地址

### SHT40 I2C 地址

U1 下方明确标注 0x44 I2C addr。

- 参数与网络：`device=U1 SHT40-AD1B`；`address=0x44`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B2，U1 SHT40-AD1B 下方文字 0x44 I2C addr

## 传感器

### U1 SHT40-AD1B 引脚映射

U1 的 SDA pin1 连接 SDA，SCL pin2 连接 SCL，VDD pin3 连接 +3.3V，VSS pin4 连接 GND。

- 参数与网络：`reference=U1`；`part_number=SHT40-AD1B`；`pinout=1:SDA,2:SCL,3:VDD/+3.3V,4:VSS/GND`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 B2，U1 四侧脚号、引脚名与 SDA/SCL/+3.3V/GND 网络

### U2 BMP280 引脚映射

U2 的 SCK pin4 连接 SCL，SDI pin3 连接 SDA，CSB pin2、Vdd pin8 与 Vddio pin6 连接 +3.3V，SDO pin5、GND pin1 与 GND pin7 连接 GND。

- 参数与网络：`reference=U2`；`part_number=BMP280`；`pinout=1:GND,2:CSB/+3.3V,3:SDI/SDA,4:SCK/SCL,5:SDO/GND,6:Vddio/+3.3V,7:GND,8:Vdd/+3.3V`
- 证据：图 40c5d4e292bb / 第 1 页 / 网格 C2，U2 BMP280 全部脚号、引脚名及 SCL/SDA/+3.3V/GND 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ENV-IV 传感器架构 | `sensor_1=U1 SHT40-AD1B`；`sensor_2=U2 BMP280`；`bus=SCL,SDA`；`sensor_rail=+3.3V`；`regulator=U3 HT7533`；`connector=J1 IIC_Socket_4P` |
| 接口 | J1 I2C 接口 | `reference=J1`；`part_number=IIC_Socket_4P`；`pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC,4:GND` |
| 电源 | U3 HT7533 稳压路径 | `reference=U3`；`part_number=HT7533`；`pinout=1:GND,2:VIN/VCC,3:VOUT/+3.3V`；`input_rail=VCC`；`output_rail=+3.3V` |
| 电源 | VCC 输入去耦 | `rail=VCC`；`capacitors=C2 100nF,C5 10uF` |
| 电源 | 外部 VCC 标称电压 | `input_net=VCC`；`nominal_voltage_v=null`；`connector_pin=J1 pin3`；`regulator_pin=U3 pin2 VIN` |
| 电源 | +3.3V 输出滤波 | `rail=+3.3V`；`capacitors=C3 100nF,C4 10uF` |
| 总线 | 共享 I2C 总线 | `scl_path=J1 pin1 -> SCL -> U1 pin2 SCL,U2 pin4 SCK`；`sda_path=J1 pin2 -> SDA -> U1 pin1 SDA,U2 pin3 SDI`；`devices=U1 SHT40-AD1B,U2 BMP280` |
| 总线 | I2C 上拉电阻 | `scl_pullup=R1 4.7kΩ to +3.3V`；`sda_pullup=R2 4.7kΩ to +3.3V` |
| 传感器 | U1 SHT40-AD1B 引脚映射 | `reference=U1`；`part_number=SHT40-AD1B`；`pinout=1:SDA,2:SCL,3:VDD/+3.3V,4:VSS/GND` |
| 总线地址 | SHT40 I2C 地址 | `device=U1 SHT40-AD1B`；`address=0x44` |
| 电源 | SHT40 电源去耦 | `capacitor=C1 100nF`；`rail=+3.3V`；`device=U1 SHT40-AD1B` |
| 传感器 | U2 BMP280 引脚映射 | `reference=U2`；`part_number=BMP280`；`pinout=1:GND,2:CSB/+3.3V,3:SDI/SDA,4:SCK/SCL,5:SDO/GND,6:Vddio/+3.3V,7:GND,8:Vdd/+3.3V` |
| 总线 | BMP280 I2C 接线模式 | `csb=pin2 -> +3.3V`；`scl=pin4 SCK -> SCL`；`sda=pin3 SDI -> SDA`；`sdo=pin5 -> GND` |
| 总线地址 | BMP280 I2C 地址 | `device=U2 BMP280`；`sdo_configuration=pin5 -> GND`；`address=null` |

## 待确认事项

- `power.vcc_nominal_voltage`：原理图只将 J1 pin3 与 U3 VIN pin2 网络标为 VCC，没有在图内给出该输入电源的数值。（证据：图 40c5d4e292bb / 第 1 页 / 网格 B3-C3，J1 pin3、C2/C5 与 U3 VIN pin2 的 VCC 网络标注）
- `address.bmp280`：原理图确认 U2 SDO pin5 接 GND，但没有在图内直接标注 BMP280 的 I2C 地址值。（证据：图 40c5d4e292bb / 第 1 页 / 网格 C2，U2 SDO pin5 到 GND 的连线；该器件周边无地址文字标注）
- `review.vcc_nominal_voltage`：J1 pin3 的 VCC 标称输入电压是否为 5V？；原因：原理图只标注 VCC，未写明电压数值；需由产品接口定义或电源规格确认。
- `review.bmp280_address`：BMP280 在 SDO pin5 接 GND 配置下的 I2C 地址是否为产品正文中的 0x76？；原因：原理图未直接标注 BMP280 地址，需要用该器件 datasheet 或已验证通信记录确认 SDO 配置与地址的映射。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `40c5d4e292bb06fa81d5f26df0021b8a17f08d77e83231177ff63b2b43bda60f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/573/Sch_UNIT_ENVIV_sch_01.png` |

---

源文档：`zh_CN/unit/Unit_ENV-IV.md`

源文档 SHA-256：`53e2f09a420e320cb399e2ed5c0d7c2b62baa60d839aa58801057266fd4bc310`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
