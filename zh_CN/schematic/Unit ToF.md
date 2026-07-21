# Unit ToF 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ToF |
| SKU | U010 |
| 产品 ID | `unit-tof-03243b056d52` |
| 源文档 | `zh_CN/unit/TOF.md` |

## 概述

Unit ToF（U010）以 U1 VL53L0X 激光测距传感器为核心，通过 J1 IIC_Socket_4P 提供 SCL、SDA、VCC 和 GND。U2 HT7533 将 VCC 转换为 +3.3V，供 U1 AVDD 以及 XSHUT/GPIO1/I2C 传感器侧上拉使用。Q1/Q2 BSS138 对 SDA/SCL 进行双向电平转换，主机侧上拉到 VCC，传感器侧上拉到 +3.3V；XSHUT 和 GPIO1 还通过 JP1/JP2 测试点引出。原理图未标注 0x29 地址、VCC 数值、测距范围、精度、分辨率、响应时间或 940nm 波长。

## 检索关键词

`Unit ToF`、`U010`、`VL53L0X`、`U1`、`HT7533`、`U2`、`BSS138`、`Q1`、`Q2`、`I2C level shifter`、`IIC_Socket_4P`、`J1`、`SCL`、`SDA`、`XSHUT`、`GPIO1`、`JP1`、`JP2`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 4.7KΩ`、`R5 4.7KΩ`、`R6 4.7KΩ`、`VCC`、`+3.3V`、`0x29`、`Time-of-Flight`、`940nm VCSEL`、`SPAD`、`laser ranging`、`3cm 200cm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | VL53L0X | ToF 激光测距传感器，连接 I2C、XSHUT、GPIO1 与 +3.3V | 图 c7d7e18b3a2c / 第 1 页 / 页面右上 U1 VL53L0X，pins 1~12 AVDD/AVSS/GND/XSHUT/GPIO1/SDA/SCL/DNC |
| U2 | HT7533 | 将 J1 VCC 转换为 +3.3V 的三端稳压器 | 图 c7d7e18b3a2c / 第 1 页 / 页面下中 U2 HT7533，pin2 VIN VCC、pin3 VOUT +3.3V、pin1 GND |
| J1 | IIC_Socket_4P | 四针 Grove I2C 与电源接口 | 图 c7d7e18b3a2c / 第 1 页 / 页面右下 J1 pins 1~4 IIC_SCL/IIC_SDA/VCC/GND |
| Q1/Q2 | BSS138 | SDA/SCL 的双向 MOSFET 电平转换器 | 图 c7d7e18b3a2c / 第 1 页 / 页面左中 Q1/Q2 BSS138，分别串接 SDA/SCL，栅极接 +3.3V |
| R5/R6 | 4.7KΩ | 主机侧 SDA/SCL 到 VCC 的上拉电阻 | 图 c7d7e18b3a2c / 第 1 页 / 页面左上 R5 4.7KΩ SDA-VCC、R6 4.7KΩ SCL-VCC |
| R1/R2 | 4.7KΩ | 传感器侧 SCL/SDA 到 +3.3V 的上拉电阻 | 图 c7d7e18b3a2c / 第 1 页 / 页面上中 R1 4.7KΩ 到 U1 SCL、R2 4.7KΩ 到 U1 SDA |
| R3/R4 | 4.7KΩ | U1 GPIO1 与 XSHUT 到 +3.3V 的上拉电阻 | 图 c7d7e18b3a2c / 第 1 页 / 页面上中 R3 4.7KΩ-GPIO1、R4 4.7KΩ-XSHUT |
| JP1/JP2 | 未标注 | XSHUT 与 GPIO1 控制/中断测试点 | 图 c7d7e18b3a2c / 第 1 页 / 页面上中 jp1/jp2 test 测试点分别接 U1 XSHUT/GPIO1 网络 |
| C2/C3 | 100nF/10uF | HT7533 +3.3V 输出侧去耦与储能电容 | 图 c7d7e18b3a2c / 第 1 页 / 页面左下 +3.3V-C2 100nF/C3 10uF-GND |
| C1/C4 | 100nF/10uF | VCC 输入侧去耦与储能电容 | 图 c7d7e18b3a2c / 第 1 页 / 页面右下 VCC-C1 100nF/C4 10uF-GND |

## 系统结构

### Unit ToF 系统架构

U1 VL53L0X 通过 Q1/Q2 BSS138 电平转换连接 J1 I2C，U2 HT7533 生成 +3.3V，XSHUT/GPIO1 由 JP1/JP2 引出。

- 参数与网络：`sensor=U1 VL53L0X`；`regulator=U2 HT7533`；`level_shifter=Q1/Q2 BSS138`；`interface=J1 IIC_Socket_4P`；`control=JP1 XSHUT,JP2 GPIO1`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 整页 U1/U2/J1/Q1/Q2/R1~R6/JP1/JP2/C1~C4

## 电源

### VCC 输入

J1 pin3 VCC 连接 U2 VIN pin2，并由 C1 100nF 与 C4 10uF 对地滤波。

- 参数与网络：`input=J1 pin3 VCC`；`regulator=U2 pin2 VIN`；`capacitors=C1 100nF,C4 10uF`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面右下 J1 VCC/U2 VIN/C1/C4

### VCC 到 +3.3V

U2 HT7533 pin2 VIN 接 VCC、pin3 VOUT 输出 +3.3V、pin1 GND；输出由 C2 100nF/C3 10uF 去耦。

- 参数与网络：`input=VCC`；`output=+3.3V`；`ground=GND`；`output_caps=C2 100nF,C3 10uF`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面下中 U2/C2/C3

### 电源控制与电池

本页未显示稳压使能、负载开关、充电器、电池或电源监测器。

- 参数与网络：`enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 整页电源部分仅 HT7533 与电容

## 接口

### J1 I2C 针脚

J1 pins 1~4 依次为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面右下 J1 pins 1~4

## 总线

### I2C 双向电平转换

J1 SDA/SCL 分别经 Q1/Q2 BSS138 连接 U1 SDA/SCL，MOSFET 栅极接 +3.3V。

- 参数与网络：`sda=J1 SDA -> Q1 BSS138 -> U1 pin9`；`scl=J1 SCL -> Q2 BSS138 -> U1 pin10`；`gate_rail=+3.3V`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面左中 SDA/SCL-Q1/Q2-U1

### I2C 两侧上拉

主机 SDA/SCL 侧由 R5/R6 4.7KΩ 上拉到 VCC，传感器 SDA/SCL 侧由 R2/R1 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`host_sda=R5 4.7KΩ to VCC`；`host_scl=R6 4.7KΩ to VCC`；`sensor_sda=R2 4.7KΩ to +3.3V`；`sensor_scl=R1 4.7KΩ to +3.3V`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面 R1/R2/R5/R6 与 SDA/SCL 两侧网络

### 其他外部总线

本页仅显示 I2C，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 c7d7e18b3a2c / 第 1 页 / J1 仅 IIC_SCL/IIC_SDA/VCC/GND

## GPIO 与控制信号

### XSHUT 控制

U1 XSHUT pin5 由 R4 4.7KΩ 上拉到 +3.3V，并连接 JP1 test 测试点。

- 参数与网络：`pin=U1 pin5 XSHUT`；`pullup=R4 4.7KΩ to +3.3V`；`test_point=JP1`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面 U1 pin5/R4/JP1 top network

### GPIO1 中断/状态输出

U1 GPIO1 pin7 由 R3 4.7KΩ 上拉到 +3.3V，并连接 JP2 test 测试点；未引到 J1。

- 参数与网络：`pin=U1 pin7 GPIO1`；`pullup=R3 4.7KΩ to +3.3V`；`test_point=JP2`；`grove_connection=null`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面 U1 pin7/R3/JP2 second network

## 时钟

### 时钟与存储

本页未显示外部晶振、主控、Flash、EEPROM、RAM 或 SD 卡；SCL 是 I2C 总线时钟。

- 参数与网络：`external_clock=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 整页仅传感器、电平转换、稳压、接口与阻容

## 保护电路

### 接口保护

J1 SCL/SDA/VCC 未显示 TVS/ESD、保险丝、反接或过压保护；Q1/Q2 是电平转换器。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`level_shifter=Q1/Q2 BSS138`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 整页 J1 到 U1/U2 路径

## 传感器

### VL53L0X 引脚

U1 XSHUT pin5、GPIO1 pin7、SDA pin9、SCL pin10；AVDD pins1/11 接 +3.3V，AVSS/GND pins2/3/4/6/12 接地，DNC pin8 未连接。

- 参数与网络：`xshut=pin5`；`gpio1=pin7`；`sda=pin9`；`scl=pin10`；`avdd=pins1,11 +3.3V`；`ground=pins2,3,4,6,12`；`dnc=pin8 NC`
- 证据：图 c7d7e18b3a2c / 第 1 页 / 页面右上 U1 pins 1~12 与网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ToF 系统架构 | `sensor=U1 VL53L0X`；`regulator=U2 HT7533`；`level_shifter=Q1/Q2 BSS138`；`interface=J1 IIC_Socket_4P`；`control=JP1 XSHUT,JP2 GPIO1` |
| 传感器 | VL53L0X 引脚 | `xshut=pin5`；`gpio1=pin7`；`sda=pin9`；`scl=pin10`；`avdd=pins1,11 +3.3V`；`ground=pins2,3,4,6,12`；`dnc=pin8 NC` |
| 接口 | J1 I2C 针脚 | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | I2C 双向电平转换 | `sda=J1 SDA -> Q1 BSS138 -> U1 pin9`；`scl=J1 SCL -> Q2 BSS138 -> U1 pin10`；`gate_rail=+3.3V` |
| 总线 | I2C 两侧上拉 | `host_sda=R5 4.7KΩ to VCC`；`host_scl=R6 4.7KΩ to VCC`；`sensor_sda=R2 4.7KΩ to +3.3V`；`sensor_scl=R1 4.7KΩ to +3.3V` |
| GPIO 与控制信号 | XSHUT 控制 | `pin=U1 pin5 XSHUT`；`pullup=R4 4.7KΩ to +3.3V`；`test_point=JP1` |
| GPIO 与控制信号 | GPIO1 中断/状态输出 | `pin=U1 pin7 GPIO1`；`pullup=R3 4.7KΩ to +3.3V`；`test_point=JP2`；`grove_connection=null` |
| 电源 | VCC 输入 | `input=J1 pin3 VCC`；`regulator=U2 pin2 VIN`；`capacitors=C1 100nF,C4 10uF` |
| 电源 | VCC 到 +3.3V | `input=VCC`；`output=+3.3V`；`ground=GND`；`output_caps=C2 100nF,C3 10uF` |
| 电源 | 电源控制与电池 | `enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null` |
| 保护电路 | 接口保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`level_shifter=Q1/Q2 BSS138` |
| 时钟 | 时钟与存储 | `external_clock=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 总线地址 | VL53L0X I2C 地址 | `device=VL53L0X`；`address=null`；`candidate_from_product_doc=0x29` |
| 电源 | VCC 电压 | `host_rail=VCC`；`sensor_rail=+3.3V`；`input_voltage=null`；`candidate_from_product_doc=5V` |
| 传感器 | 测距性能 | `range=null`；`accuracy=null`；`resolution=null`；`response_time=null`；`fov=null`；`wavelength=null`；`long_range=null` |
| 总线 | I2C 速率 | `pullups=4.7KΩ`；`level_shifter=BSS138`；`frequency=null`；`bus_capacitance=null`；`timing=null` |

## 待确认事项

- `address.vl53l0x`：原理图未标注 I2C 地址或地址选择电路，不能仅凭本页确认 0x29。（证据：图 c7d7e18b3a2c / 第 1 页 / U1/J1 I2C 网络，无地址文字）
- `power.vcc-voltage`：原理图只标 VCC，没有给输入数值或允许范围；Q1/Q2 说明 VCC 与 +3.3V 为独立 I2C 电平域。（证据：图 c7d7e18b3a2c / 第 1 页 / VCC/+3.3V 两侧上拉和 HT7533，无 VCC 数字）
- `sensor.ranging-performance`：原理图未标注测距范围、精度、分辨率、响应时间、视场角、940nm 波长或 Long Range 条件。（证据：图 c7d7e18b3a2c / 第 1 页 / U1 VL53L0X 仅型号/连接，无性能文字）
- `bus.i2c-speed`：原理图给出 4.7KΩ 上拉和 BSS138 电平转换，但未标注工作频率、总线电容或时序。（证据：图 c7d7e18b3a2c / 第 1 页 / SCL/SDA 电平转换与上拉，无时序文字）
- `review.i2c-address`：VL53L0X 地址是否为 0x29，是否可通过 XSHUT 实现多器件改址？；原因：原理图无地址说明。
- `review.vcc-voltage`：J1 VCC 输入范围和主机 I2C 电平是多少？；原因：图中仅标 VCC，并通过 MOSFET 转换到 3.3V。
- `review.ranging-performance`：该硬件/配置的范围、精度、分辨率、响应、FoV 和激光波长是什么？；原因：这些性能参数未在原理图中标注。
- `review.i2c-speed`：推荐和允许的 I2C 频率/时序范围是什么？；原因：图纸只有电平转换和上拉参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c7d7e18b3a2cab89793723ea45da351eaeb7b2ae663b2c135046fa0b2cd1c5f5` | `https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-5d9d3c7d-dd82-47e9-8917-f8d6733fcfb5.webp` |

---

源文档：`zh_CN/unit/TOF.md`

源文档 SHA-256：`82b6c6f4e17857fb48ebe63d09caf8b7a39fad5599d2c6eb3367d7c579c13d73`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
