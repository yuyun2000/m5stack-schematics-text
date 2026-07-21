# Unit ENV-III 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ENV-III |
| SKU | U001-C |
| 产品 ID | `unit-env-iii-b7aa03a7c9e8` |
| 源文档 | `zh_CN/unit/envIII.md` |

## 概述

Unit ENV-III 是一块无板载主控的双传感器环境单元，U1 SHT30-DIS-B 与 U2 QMP6988 共用 J1 的 SCL/SDA。U3 HT7533 将 J1 VCC 转换为 +3.3V，为两颗传感器供电。SHT30 的 ADDR 接 GND、QMP6988 的 SDO 接 GND；R1/R2 各以 4.7KΩ将 SCL/SDA 上拉到 VCC。

## 检索关键词

`Unit ENV-III`、`U001-C`、`SHT30-DIS-B`、`SHT30`、`U1`、`QMP6988`、`U2`、`HT7533`、`U3`、`J1`、`IIC_Socket_4P`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`ADDR`、`SDO`、`CSB`、`Vdd`、`Vddio`、`VCC`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`C4 10uF`、`C5 10uF`、`0x44`、`0x70`、`temperature`、`humidity`、`barometric pressure`、`Grove Port A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 温湿度传感器，使用 SDA/SCL I2C，ADDR 接 GND，ALERT/nRESET 未连接。 | 图 769464424fb8 / 第 1 页 / 页面左上 U1 SHT30-DIS-B，ALERT/nRESET/ADDR/R/VSS/dpad/VDD/SDA/SCL |
| U2 | QMP6988 | 气压传感器，SCK/SDI 连接 SCL/SDA，CSB/Vdd/Vddio 接 +3.3V，SDO 接 GND。 | 图 769464424fb8 / 第 1 页 / 页面左下 U2 QMP6988，SCK/SDI/CSB/Vdd/Vddio/SDO/GND |
| U3 | HT7533 | VCC 输入到 +3.3V 输出的三端 LDO。 | 图 769464424fb8 / 第 1 页 / 页面右下 U3 HT7533，VIN/2、VOUT/3、GND/1 与 VCC/+3.3V |
| J1 | IIC_Socket_4P | 四针 I2C 与供电接口，引出 SCL、SDA、VCC、GND。 | 图 769464424fb8 / 第 1 页 / 页面右上 J1 IIC_Socket_4P 1-4 脚 |
| R1,R2 | 4.7KΩ | SCL 与 SDA 到 VCC 的 I2C 上拉电阻。 | 图 769464424fb8 / 第 1 页 / 页面上中 R1/R2 4.7KΩ，分别从 SCL/SDA 接 VCC |
| C1-C5 | 100nF / 100nF / 100nF / 10uF / 10uF | 传感器、电源输入与 HT7533 输出的去耦/滤波电容。 | 图 769464424fb8 / 第 1 页 / C1 +3.3V 100nF、C2 VCC 100nF、C3 +3.3V 100nF、C4 +3.3V 10uF、C5 VCC 10uF |

## 系统结构

### 整板架构

整板由 U1 SHT30-DIS-B、U2 QMP6988、U3 HT7533、J1 与上拉/去耦器件构成；本页未显示 MCU、存储器、晶振、复位、调试或射频电路。

- 参数与网络：`temperature_humidity=U1 SHT30-DIS-B`；`pressure=U2 QMP6988`；`regulator=U3 HT7533`；`host_interface=J1 IIC_Socket_4P`；`controller=原理图未显示`；`storage=原理图未显示`
- 证据：图 769464424fb8 / 第 1 页 / 第 1 页全图，U1/U2/U3/J1/R1-R2/C1-C5

## 电源

### U3 VCC 到 3.3V 稳压

U3 HT7533 的 VIN（2 脚）接 VCC，VOUT（3 脚）输出 +3.3V，GND（1 脚）接地。

- 参数与网络：`regulator=U3 HT7533`；`input=VIN pin2/VCC`；`output=VOUT pin3/+3.3V`；`ground=pin1/GND`
- 证据：图 769464424fb8 / 第 1 页 / 页面右下 U3 HT7533 与 VCC/+3.3V/GND

### VCC 与 3.3V 去耦

C2 100nF 与 C5 10uF 从 VCC 接 GND；C1/C3 各 100nF、C4 10uF 从 +3.3V 接 GND。

- 参数与网络：`vcc_caps=C2 100nF,C5 10uF`；`vcc_3v3_caps=C1 100nF,C3 100nF,C4 10uF`
- 证据：图 769464424fb8 / 第 1 页 / C1-C5 的 VCC/+3.3V 对地连接

## 接口

### J1 IIC_Socket_4P

J1.1-J1.4 分别为 IIC_SCL/SCL、IIC_SDA/SDA、VCC、GND。

- 参数与网络：`reference=J1`；`part_number=IIC_Socket_4P`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 769464424fb8 / 第 1 页 / 页面右上 J1 1-4 脚与双侧标注

## 总线

### 共享 I2C 总线

J1.1 SCL 同时连接 U1 SCL/4 与 U2 SCK/4；J1.2 SDA 同时连接 U1 SDA/1 与 U2 SDI/3。

- 参数与网络：`scl=J1.1 -> U1.4 SCL,U2.4 SCK`；`sda=J1.2 -> U1.1 SDA,U2.3 SDI`；`devices=U1 SHT30-DIS-B,U2 QMP6988`
- 证据：图 769464424fb8 / 第 1 页 / U1/U2/J1 三处同名 SCL/SDA 网络

### I2C 上拉

R1 4.7KΩ将 SCL 上拉到 VCC，R2 4.7KΩ将 SDA 上拉到 VCC；原理图未显示电平转换器。

- 参数与网络：`scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC`；`level_shifter=原理图未显示`
- 证据：图 769464424fb8 / 第 1 页 / 页面上中 R1/R2 与 VCC/SCL/SDA

### QMP6988 I2C 模式

U2 CSB（2 脚）接 +3.3V，SDI/SCK 接 SDA/SCL，因此本板使用 QMP6988 的 I2C 连接。

- 参数与网络：`device=U2 QMP6988`；`csb=+3.3V`；`sda=SDI pin3`；`scl=SCK pin4`；`interface=I2C`
- 证据：图 769464424fb8 / 第 1 页 / U2 CSB/2、SDI/3、SCK/4 与 +3.3V/SDA/SCL

## GPIO 与控制信号

### SHT30 ALERT 与 nRESET

U1 ALERT（3 脚）与 nRESET（6 脚）在原理图中没有可见外部连接，板上未将中断或复位引出到 J1。

- 参数与网络：`alert_pin=U1.3/no visible connection`；`reset_pin=U1.6/no visible connection`；`connector=not routed to J1`
- 证据：图 769464424fb8 / 第 1 页 / U1 ALERT/3 与 nRESET/6 左侧短线无网络标注

## 保护电路

### J1 接口保护

J1 的 SCL、SDA、VCC、GND 直接进入上拉、稳压与地网络，本页未显示 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`connector=J1`；`signals=SCL,SDA,VCC,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`
- 证据：图 769464424fb8 / 第 1 页 / J1 至 R1/R2/U3 的直接路径

## 存储

### 主控与存储

本页未显示 MCU、Flash、EEPROM、SD 卡或其他存储器，两颗传感器直接共享外部 I2C。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`devices=SHT30-DIS-B,QMP6988`
- 证据：图 769464424fb8 / 第 1 页 / 第 1 页全图，无主控或存储器位号

## 传感器

### U1 SHT30-DIS-B

U1.1 SDA 接 SDA，U1.4 SCL 接 SCL，U1.5 VDD 接 +3.3V，U1.2 ADDR 与 U1.7 R、U1.8 VSS、U1.9 dpad 接 GND；ALERT/3 与 nRESET/6 无可见连接。

- 参数与网络：`pin_1=SDA`；`pin_2=ADDR/GND`；`pin_3=ALERT/no visible connection`；`pin_4=SCL`；`pin_5=VDD/+3.3V`；`pin_6=nRESET/no visible connection`；`pin_7=R/GND`；`pin_8=VSS/GND`；`pin_9=dpad/GND`
- 证据：图 769464424fb8 / 第 1 页 / 页面左上 U1 1-9 脚与网络

### U2 QMP6988

U2.4 SCK 接 SCL，U2.3 SDI 接 SDA，U2.2 CSB、U2.8 Vdd、U2.6 Vddio 接 +3.3V，U2.5 SDO、U2.1/7 GND 接地。

- 参数与网络：`pin_1=GND`；`pin_2=CSB/+3.3V`；`pin_3=SDI/SDA`；`pin_4=SCK/SCL`；`pin_5=SDO/GND`；`pin_6=Vddio/+3.3V`；`pin_7=GND`；`pin_8=Vdd/+3.3V`
- 证据：图 769464424fb8 / 第 1 页 / 页面左下 U2 QMP6988 1-8 脚与网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `temperature_humidity=U1 SHT30-DIS-B`；`pressure=U2 QMP6988`；`regulator=U3 HT7533`；`host_interface=J1 IIC_Socket_4P`；`controller=原理图未显示`；`storage=原理图未显示` |
| 传感器 | U1 SHT30-DIS-B | `pin_1=SDA`；`pin_2=ADDR/GND`；`pin_3=ALERT/no visible connection`；`pin_4=SCL`；`pin_5=VDD/+3.3V`；`pin_6=nRESET/no visible connection`；`pin_7=R/GND`；`pin_8=VSS/GND`；`pin_9=dpad/GND` |
| 传感器 | U2 QMP6988 | `pin_1=GND`；`pin_2=CSB/+3.3V`；`pin_3=SDI/SDA`；`pin_4=SCK/SCL`；`pin_5=SDO/GND`；`pin_6=Vddio/+3.3V`；`pin_7=GND`；`pin_8=Vdd/+3.3V` |
| 总线 | 共享 I2C 总线 | `scl=J1.1 -> U1.4 SCL,U2.4 SCK`；`sda=J1.2 -> U1.1 SDA,U2.3 SDI`；`devices=U1 SHT30-DIS-B,U2 QMP6988` |
| 总线 | I2C 上拉 | `scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC`；`level_shifter=原理图未显示` |
| 总线 | QMP6988 I2C 模式 | `device=U2 QMP6988`；`csb=+3.3V`；`sda=SDI pin3`；`scl=SCK pin4`；`interface=I2C` |
| 电源 | U3 VCC 到 3.3V 稳压 | `regulator=U3 HT7533`；`input=VIN pin2/VCC`；`output=VOUT pin3/+3.3V`；`ground=pin1/GND` |
| 电源 | VCC 与 3.3V 去耦 | `vcc_caps=C2 100nF,C5 10uF`；`vcc_3v3_caps=C1 100nF,C3 100nF,C4 10uF` |
| 接口 | J1 IIC_Socket_4P | `reference=J1`；`part_number=IIC_Socket_4P`；`pin_1=IIC_SCL/SCL`；`pin_2=IIC_SDA/SDA`；`pin_3=VCC`；`pin_4=GND` |
| GPIO 与控制信号 | SHT30 ALERT 与 nRESET | `alert_pin=U1.3/no visible connection`；`reset_pin=U1.6/no visible connection`；`connector=not routed to J1` |
| 保护电路 | J1 接口保护 | `connector=J1`；`signals=SCL,SDA,VCC,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示` |
| 存储 | 主控与存储 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`devices=SHT30-DIS-B,QMP6988` |
| 总线地址 | SHT30 I2C 地址 | `device=U1 SHT30-DIS-B`；`address_pin=ADDR pin2`；`address_pin_level=GND`；`documented_candidate=0x44`；`schematic_address=未标注` |
| 总线地址 | QMP6988 I2C 地址 | `device=U2 QMP6988`；`address_pin=SDO pin5`；`address_pin_level=GND`；`documented_candidate=0x70`；`schematic_address=未标注` |
| 电源 | VCC 与 I2C 上拉绝对电平 | `regulator_input=VCC`；`sensor_supply=+3.3V`；`i2c_pullup_rail=VCC`；`documented_vcc_candidate=5V`；`schematic_vcc_voltage=未标注`；`io_tolerance=未标注` |
| 传感器 | 温湿度与气压性能 | `temperature_humidity_sensor=SHT30-DIS-B`；`pressure_sensor=QMP6988`；`temperature_range_candidate=-40 to 120°C`；`humidity_candidate=10 to 90%RH`；`pressure_candidate=300 to 1100hPa`；`schematic_performance=未标注` |

## 待确认事项

- `address.sht30-undetermined`：原理图确认 U1 ADDR（2 脚）接 GND，但没有打印地址对照表；无法仅由本页确认正文中的 0x44。（证据：图 769464424fb8 / 第 1 页 / U1 ADDR/2 接 GND，整页无地址文字）
- `address.qmp6988-undetermined`：原理图确认 U2 SDO（5 脚）接 GND，但没有打印地址对照表；无法仅由本页确认正文中的 0x70。（证据：图 769464424fb8 / 第 1 页 / U2 SDO/5 接 GND，整页无地址文字）
- `power.vcc-i2c-level-undetermined`：U3 将 VCC 转换为 +3.3V，而 R1/R2 将 SCL/SDA 上拉到 VCC；图中未打印 VCC 绝对电压或传感器 I/O 容限，无法仅由原理图确认正文 5V 供电时的总线电平兼容性。（证据：图 769464424fb8 / 第 1 页 / J1.3/R1/R2 VCC、U3 HT7533 VCC→+3.3V、U1/U2 +3.3V 供电）
- `sensor.performance-undetermined`：原理图只显示 SHT30-DIS-B 与 QMP6988 型号和连接，没有温度、湿度、气压量程、精度、分辨率、采样率或功耗参数，不能由图纸确认正文数值。（证据：图 769464424fb8 / 第 1 页 / U1/U2 传感器符号无量程、精度或功耗文字）
- `review.sht30-address`：ADDR 接 GND 时，该板 SHT30-DIS-B 的确认 7 位 I2C 地址是否为 0x44？；原因：原理图没有地址表，地址值需由 datasheet 或实机确认。
- `review.qmp6988-address`：SDO 接 GND 时，该板 QMP6988 的确认 7 位 I2C 地址是否为 0x70？；原因：原理图没有地址表，地址值需由 datasheet 或实机确认。
- `review.vcc-i2c-level`：J1 VCC 的额定电压以及 R1/R2 上拉后的 SCL/SDA 实际高电平是多少，是否满足两颗 3.3V 传感器 I/O 容限？；原因：图中上拉接 VCC、传感器供电为 +3.3V，但没有 VCC 数值或电平转换。
- `review.sensor-performance`：该版本确认的温度、湿度、气压量程、精度、分辨率与功耗分别是多少？；原因：这些属于器件规格，原理图没有给出数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `769464424fb86102da7dadb5b8f9246c685eff19efd77b73cd72826e6c2af675` | `https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_sch_01.webp` |

---

源文档：`zh_CN/unit/envIII.md`

源文档 SHA-256：`b0db533b71fe82f584c436f6df75931f6ec02ffc3bc69d1fc40f0d5768e72e0a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
