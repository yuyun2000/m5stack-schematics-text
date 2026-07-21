# Unit Accel 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Accel |
| SKU | U056 |
| 产品 ID | `unit-accel-b0c92dda0614` |
| 源文档 | `zh_CN/unit/accel.md` |

## 概述

Unit Accel 以 U1 ADXL345 为三轴加速度传感器，CS 接 +3.3V 选择 I2C 接口，SDO/ALT ADDRESS 接 GND，INT1/INT2 未引出。Grove J1 的 SCL/SDA 通过 Q1/Q2 AO3400A 双向电平转换到传感器侧，两侧分别由 4.7K 上拉到 VCC 和 +3.3V。U2 HT7533 将 Grove VCC 稳压为 +3.3V，为 ADXL345 VDD/VS 和 I2C 传感器侧供电。正文给出的 0x53 地址、±16g/13 位和低功耗/事件检测参数需结合 ADXL345 数据手册或实测确认。

## 检索关键词

`Unit Accel`、`U056`、`ADXL345`、`HT7533`、`AO3400A`、`I2C`、`0x53`、`SCL`、`SDA`、`SDO`、`ALT ADDRESS`、`CS`、`INT1`、`INT2`、`VDD`、`VS`、`VCC`、`+3.3V`、`R1 4.7K`、`R2 4.7K`、`R5 4.7K`、`R6 4.7K`、`Grove`、`HY2.0-4P`、`3-axis accelerometer`、`16g`、`13-bit`、`level shifter`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ADXL345 | 三轴数字加速度传感器，配置为 I2C 接口 | 图 17fb043a5777 / 第 1 页 / 第 1 页右上 U1 ADXL345 |
| U2 | HT7533 | VCC 到 +3.3V 的线性稳压器 | 图 17fb043a5777 / 第 1 页 / 第 1 页下部 U2 HT7533 |
| Q1/Q2 | AO3400A | SCL/SDA 的 VCC 与 +3.3V 双向电平转换 MOSFET | 图 17fb043a5777 / 第 1 页 / 第 1 页左上 Q1/Q2 AO3400A |
| J1 | IIC_Socket_4P | SCL、SDA、VCC、GND Grove I2C 接口 | 图 17fb043a5777 / 第 1 页 / 第 1 页下部 J1 IIC_Socket_4P |
| R1/R2/R5/R6 | 4.7KΩ | I2C +3.3V 侧和 VCC 侧上拉电阻 | 图 17fb043a5777 / 第 1 页 / 第 1 页左上 R1/R2/R5/R6 |
| C1/C2/C3/C4 | 100nF/100nF/10uF/10uF | VCC 与 +3.3V 电源去耦和稳压器输入输出滤波 | 图 17fb043a5777 / 第 1 页 / 第 1 页下部 C1-C4 |

## 系统结构

### Unit Accel

U1 ADXL345 通过 Q1/Q2 电平转换后的 I2C 连接 J1，U2 由 VCC 生成 +3.3V，地址脚和 CS 固定配置，未使用中断输出。

- 参数与网络：`sensor=U1 ADXL345`；`bus=I2C`；`level_shifter=Q1/Q2 AO3400A`；`regulator=U2 HT7533`；`connector=J1`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页完整功能分区

## 电源

### U2 HT7533

U2 VIN 接 J1 VCC、VOUT 输出 +3.3V、GND 接地；VCC 由 C1 100nF/C4 10uF 去耦，+3.3V 由 C2 100nF/C3 10uF 去耦。

- 参数与网络：`input=VCC`；`output=+3.3V`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页下部 U2/C1-C4

## 接口

### J1 IIC_Socket_4P

J1.1=SCL、J1.2=SDA、J1.3=VCC、J1.4=GND。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页下部 J1

## 总线

### SCL/SDA 双向电平转换

外部 SCL/SDA 由 R5/R6 各 4.7K 上拉至 VCC，经 Q1/Q2 AO3400A 到传感器侧；传感器侧由 R1/R2 各 4.7K 上拉至 +3.3V。

- 参数与网络：`external_pullups=R5 SCL,R6 SDA 4.7K to VCC`；`mosfets=Q1 SCL,Q2 SDA AO3400A`；`sensor_pullups=R1 SCL,R2 SDA 4.7K to +3.3V`；`device=U1`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页左上 SCL/SDA 网络

## GPIO 与控制信号

### U1 CS 与 SDO/ALT ADDRESS

U1 CS pin7 接 +3.3V，SDO/ALT ADDRESS pin12 接 GND，形成固定的 I2C 与地址配置；图中没有地址跳线。

- 参数与网络：`cs=U1.7 +3.3V`；`sdo_alt_address=U1.12 GND`；`address_jumper_shown=false`；`interface=I2C`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页 U1 pin7/pin12

### U1 INT1/INT2

U1 INT1 pin8 与 INT2 pin9 均标未连接，J1 不提供中断针脚。

- 参数与网络：`int1=U1.8 NC`；`int2=U1.9 NC`；`connector_interrupt=false`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页 U1 INT1/INT2 红叉

## 时钟

### 外部时钟

完整原理图未显示晶振、振荡器或外部时钟网络。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页完整图无时钟器件

## 保护电路

### Grove/I2C 保护

J1 VCC/GND/SCL/SDA 未画 TVS、ESD 阵列、保险丝或反接保护；I2C 线上仅有上拉与 Q1/Q2 电平转换。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_protection_shown=false`；`i2c_components=pullups and AO3400A level shifters`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页 J1 到 U1/U2 全路径

## 内存与 Flash

### 外部存储器

完整原理图未展示 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页完整图无存储器

## 传感器

### U1 ADXL345

U1 VDD 和 VS 接 +3.3V，GND 引脚接地，SCL/SDA 连接传感器侧 I2C；RESERVED/NC 引脚未外接。

- 参数与网络：`part=ADXL345`；`supply=VDD/VS +3.3V`；`ground=GND`；`data=SCL/SDA`；`reserved=NC`
- 证据：图 17fb043a5777 / 第 1 页 / 第 1 页右上 U1 电源与总线引脚

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Accel | `sensor=U1 ADXL345`；`bus=I2C`；`level_shifter=Q1/Q2 AO3400A`；`regulator=U2 HT7533`；`connector=J1` |
| 传感器 | U1 ADXL345 | `part=ADXL345`；`supply=VDD/VS +3.3V`；`ground=GND`；`data=SCL/SDA`；`reserved=NC` |
| 总线 | SCL/SDA 双向电平转换 | `external_pullups=R5 SCL,R6 SDA 4.7K to VCC`；`mosfets=Q1 SCL,Q2 SDA AO3400A`；`sensor_pullups=R1 SCL,R2 SDA 4.7K to +3.3V`；`device=U1` |
| GPIO 与控制信号 | U1 CS 与 SDO/ALT ADDRESS | `cs=U1.7 +3.3V`；`sdo_alt_address=U1.12 GND`；`address_jumper_shown=false`；`interface=I2C` |
| 总线地址 | ADXL345 I2C 地址 | `documented_address=0x53`；`strap=SDO/ALT ADDRESS low`；`address_printed_on_schematic=false` |
| 接口 | J1 IIC_Socket_4P | `pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC`；`pin_4=GND` |
| 电源 | U2 HT7533 | `input=VCC`；`output=+3.3V`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF` |
| GPIO 与控制信号 | U1 INT1/INT2 | `int1=U1.8 NC`；`int2=U1.9 NC`；`connector_interrupt=false` |
| 保护电路 | Grove/I2C 保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_protection_shown=false`；`i2c_components=pullups and AO3400A level shifters` |
| 其他事实 | 正文测量与功耗参数 | `documented_range=+/-16g`；`documented_resolution=up to 13-bit`；`documented_output=16-bit two's complement`；`documented_features=activity,inactivity,tap,double tap,free fall`；`configuration_on_schematic=null` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x53`：正文列出地址 0x53，原理图确认 SDO/ALT ADDRESS 接 GND，但页面未直接打印 0x53；地址值需由 ADXL345 数据手册或总线扫描复核。（证据：图 17fb043a5777 / 第 1 页 / 第 1 页 U1 SDO/ALT ADDRESS 接 GND）
- `other.documented-measurement`：正文列出 ±16g、最高 13 位、16 位补码、低功耗及活动/自由落体检测；原理图只确认 ADXL345 硬件连接，未标量程、分辨率、输出格式、功耗或寄存器配置。（证据：图 17fb043a5777 / 第 1 页 / 第 1 页 U1 无测量参数标注）
- `review.i2c-address`：请依据 ADXL345 数据手册或 I2C 扫描确认 SDO=0 对应地址 0x53。；原因：原理图显示地址脚电平但未直接标地址值。
- `review.measurement-spec`：请依据 ADXL345 数据手册和驱动配置确认量程、分辨率、输出格式、功耗及事件检测参数。；原因：这些功能参数不在原理图页标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `17fb043a577760d8da3d2ea4b19bf6702e27df7a5ed7cbb9fc5415344753c8ef` | `https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_sch_01.webp` |

---

源文档：`zh_CN/unit/accel.md`

源文档 SHA-256：`9320691b4c36cd484dabb79421dafa293d4c28a0012571e1f3dd0c2b00a70174`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
