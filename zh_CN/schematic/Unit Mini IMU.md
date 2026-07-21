# Unit Mini IMU 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini IMU |
| SKU | U095 |
| 产品 ID | `unit-mini-imu-09095c14c090` |
| 源文档 | `zh_CN/unit/imu.md` |

## 概述

Unit Mini IMU 以 U2 MPU-6886 为惯性传感器，通过 I2C_SCL、I2C_SDA 通信。J1 提供 5 V 侧 SCL、SDA、+5V、GND，Q1/Q2 BSS138 与两侧 4.7 kΩ 上拉构成 5 V 到 3.3 V 的双向 I2C 电平转换。U1 HT7533 将 +5V 转为 +3.3V，供 U2 的 VDD/VDDIO 和低压侧总线上拉；AD0/SDO 由 R6 下拉。

## 检索关键词

`Unit Mini IMU`、`U095`、`MPU-6886`、`MPU6886`、`HT7533`、`BSS138`、`I2C`、`0x68`、`SCL`、`SDA`、`I2C_SCL`、`I2C_SDA`、`AD0`、`AD0/SDO`、`SCL/SCLK`、`SDA/SDI`、`VDD`、`VDDIO`、`REGOUT`、`FSYNC`、`+5V`、`+3.3V`、`R1 4.7K`、`R2 4.7K`、`R3 4.7K`、`R4 4.7K`、`R6 4.7K`、`HY-2.0_IIC`、`6-axis IMU`、`accelerometer`、`gyroscope`、`1KB FIFO`、`16-bit ADC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | MPU-6886 | I2C 六轴惯性传感器 | 图 26acfd387f3b / 第 1 页 / 页 1 下中部 U2 器件框下方标注 MPU-6886 |
| U1 | HT7533 | +5V 至 +3.3V 线性稳压器 | 图 26acfd387f3b / 第 1 页 / 页 1 上中部 U1 标注 HT7533，VIN/VOUT 分别连接 +5V/+3.3V |
| Q1 | BSS138 | SDA 双向电平转换 MOSFET | 图 26acfd387f3b / 第 1 页 / 页 1 左上 Q1 标注 BSS138，连接 SDA 与 I2C_SDA，两侧分别上拉到 +5V/+3.3V |
| Q2 | BSS138 | SCL 双向电平转换 MOSFET | 图 26acfd387f3b / 第 1 页 / 页 1 左中 Q2 标注 BSS138，连接 SCL 与 I2C_SCL，两侧分别上拉到 +5V/+3.3V |
| J1 | HY-2.0_IIC | 四针 I2C 与 +5V 主机接口 | 图 26acfd387f3b / 第 1 页 / 页 1 右上 J1 标注 HY-2.0_IIC，针脚为 IIC_SCL、IIC_SDA、VCC、GND |

## 系统结构

### U2

U2 的器件型号为 MPU-6886，通过 SCL/SCLK 与 SDA/SDI 引脚接入低压侧 I2C 总线。

- 参数与网络：`reference=U2`；`part_number=MPU-6886`；`host_bus=I2C`；`scl_network=I2C_SCL`；`sda_network=I2C_SDA`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 下中部 U2 型号及左侧 SCL/SCLK、SDA/SDI 网络

## 电源

### U1 HT7533

U1 HT7533 的 VIN 引脚 2 接 +5V，VOUT 引脚 3 输出 +3.3V，GND 引脚 1 接地。

- 参数与网络：`reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 上中部 U1 HT7533 引脚号及 +5V/+3.3V/GND 网络

### U1 输入输出电容

C1、C2 均为 10 uF，分别连接在 U1 的 +5V 输入、+3.3V 输出与 GND 之间。

- 参数与网络：`input_capacitor=C1 10uF`；`output_capacitor=C2 10uF`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 U1 左右两侧 C1/C2 10uF 与 GND

### U2 供电

U2 的 VDD 引脚 13 和 VDDIO 引脚 8 连接 +3.3V，GND 引脚 18 接地；C4 100 nF 跨接 +3.3V 与 GND。

- 参数与网络：`supply_pins=VDD/pin 13,VDDIO/pin 8`；`rail=+3.3V`；`ground_pin=GND/pin 18`；`decoupling=C4 100nF`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 右侧 VDD/VDDIO 与 C4 100nF、左下 GND pin 18

## 接口

### J1 I2C 接口

J1 的 1 至 4 脚依次连接 SCL、SDA、+5V、GND，连接器内针脚名为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`；`logic_side=+5V pull-up domain`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 右上 J1 的脚号、外部网络与内部针脚文字

## 总线

### U2 低压侧 I2C

I2C_SCL 连接 U2 的 SCL/SCLK 引脚 23，I2C_SDA 连接 U2 的 SDA/SDI 引脚 24。

- 参数与网络：`device=U2 MPU-6886`；`scl=I2C_SCL -> SCL/SCLK pin 23`；`sda=I2C_SDA -> SDA/SDI pin 24`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 左侧 I2C_SCL/I2C_SDA 与 SCL/SCLK pin 23、SDA/SDI pin 24

### Q1/Q2 I2C 电平转换

Q1 BSS138 串接 SDA 与 I2C_SDA，Q2 BSS138 串接 SCL 与 I2C_SCL；两只 MOSFET 的栅极连接 +3.3V，形成双向开漏总线电平转换。

- 参数与网络：`sda_shifter=Q1 BSS138:SDA<->I2C_SDA`；`scl_shifter=Q2 BSS138:SCL<->I2C_SCL`；`gate_rail=+3.3V`；`high_side_rail=+5V`；`low_side_rail=+3.3V`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 左侧 Q1/Q2、SDA/SCL 与 I2C_SDA/I2C_SCL 的完整电平转换电路

### I2C 两侧上拉

R1、R2 均为 4.7 kΩ，分别将 SDA、SCL 上拉至 +5V；R3、R4 均为 4.7 kΩ，分别将 I2C_SDA、I2C_SCL 上拉至 +3.3V。

- 参数与网络：`host_sda_pullup=R1 4.7k to +5V`；`host_scl_pullup=R2 4.7k to +5V`；`sensor_sda_pullup=R3 4.7k to +3.3V`；`sensor_scl_pullup=R4 4.7k to +3.3V`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 左上 R1-R4 4.7KΩ 与两侧总线、电源标签

## GPIO 与控制信号

### U2 AD0/SDO

U2 的 AD0/SDO 引脚 9 通过 R6 4.7 kΩ 下拉至 GND；R5 标注 NC，位于 +3.3V 与该地址网络之间，图示不装。

- 参数与网络：`address_pin=AD0/SDO pin 9`；`pulldown=R6 4.7k to GND`；`optional_pullup=R5 NC to +3.3V`；`logic_state=low when R5 not populated`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 左侧 AD0/SDO pin 9、R5 NC 与 R6 4.7KΩ 下拉

### U2 REGOUT 与 FSYNC

U2 的 REGOUT 引脚 10 与 FSYNC 引脚 7 在本页标为未连接。

- 参数与网络：`unconnected_pins=REGOUT/pin 10,FSYNC/pin 7`
- 证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 右下 REGOUT/FSYNC 引脚末端的未连接标记

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | U2 | `reference=U2`；`part_number=MPU-6886`；`host_bus=I2C`；`scl_network=I2C_SCL`；`sda_network=I2C_SDA` |
| 接口 | J1 I2C 接口 | `reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`；`logic_side=+5V pull-up domain` |
| 总线 | U2 低压侧 I2C | `device=U2 MPU-6886`；`scl=I2C_SCL -> SCL/SCLK pin 23`；`sda=I2C_SDA -> SDA/SDI pin 24` |
| 总线 | Q1/Q2 I2C 电平转换 | `sda_shifter=Q1 BSS138:SDA<->I2C_SDA`；`scl_shifter=Q2 BSS138:SCL<->I2C_SCL`；`gate_rail=+3.3V`；`high_side_rail=+5V`；`low_side_rail=+3.3V` |
| 总线 | I2C 两侧上拉 | `host_sda_pullup=R1 4.7k to +5V`；`host_scl_pullup=R2 4.7k to +5V`；`sensor_sda_pullup=R3 4.7k to +3.3V`；`sensor_scl_pullup=R4 4.7k to +3.3V` |
| GPIO 与控制信号 | U2 AD0/SDO | `address_pin=AD0/SDO pin 9`；`pulldown=R6 4.7k to GND`；`optional_pullup=R5 NC to +3.3V`；`logic_state=low when R5 not populated` |
| 总线地址 | MPU-6886 I2C 地址 | `documented_address=0x68`；`address_pin=AD0/SDO pin 9`；`schematic_address_pin_state=low`；`schematic_address_text=null` |
| 电源 | U1 HT7533 | `reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1` |
| 电源 | U1 输入输出电容 | `input_capacitor=C1 10uF`；`output_capacitor=C2 10uF` |
| 电源 | U2 供电 | `supply_pins=VDD/pin 13,VDDIO/pin 8`；`rail=+3.3V`；`ground_pin=GND/pin 18`；`decoupling=C4 100nF` |
| GPIO 与控制信号 | U2 REGOUT 与 FSYNC | `unconnected_pins=REGOUT/pin 10,FSYNC/pin 7` |
| 传感器 | MPU-6886 传感器能力 | `documented_axes=6`；`documented_accelerometer_axes=3`；`documented_gyroscope_axes=3`；`documented_temperature_sensor=true`；`documented_adc_bits=16`；`documented_filter=programmable digital filter`；`schematic_capabilities=null` |
| 内存与 Flash | MPU-6886 FIFO | `documented_fifo_bytes=1024`；`schematic_fifo_capacity=null` |
| 模拟电路 | 加速度计与陀螺仪量程 | `documented_accelerometer_ranges_g=2,4,8,16`；`documented_gyroscope_ranges_dps=250,500,1000,2000`；`schematic_ranges=null` |

## 待确认事项

- `address.i2c`：产品正文标注 I2C 地址 0x68；原理图确认 AD0/SDO 被下拉为低，但页面本身没有打印 0x68 地址值。（证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 AD0/SDO 与 R6 下拉区域没有地址数值标注）
- `sensor.capabilities`：产品正文描述三轴加速度计、三轴陀螺仪、片上温度传感器、16 位 ADC 和可编程数字滤波器；这些功能参数未在本页原理图中标注。（证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 仅显示 MPU-6886 型号、引脚和外围连接，未显示内部传感器功能框图）
- `memory.fifo`：产品正文标注 1 KB FIFO，但本页原理图没有 FIFO 容量或存储结构标注。（证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 MPU-6886 器件框未标注 FIFO 或容量）
- `analog.measurement_ranges`：产品正文列出加速度计 ±2/4/8/16 g 与陀螺仪 ±250/500/1000/2000 dps 量程，但这些量程未在原理图中标注。（证据：图 26acfd387f3b / 第 1 页 / 页 1 U2 与外围电路未出现加速度或角速度量程数值）
- `review.i2c_address`：AD0/SDO 下拉配置下，当前 MPU-6886 器件的 7 位 I2C 地址是否为 0x68？；原因：原理图只给出地址脚状态，没有打印地址数值。
- `review.sensor_capabilities`：六轴、温度传感器、16 位 ADC 与滤波功能对应的具体 MPU-6886 版本和配置限制是什么？；原因：这些属于芯片内部功能，原理图没有功能框图或参数。
- `review.fifo`：当前 MPU-6886 的可用 FIFO 容量是否为 1 KB，是否受工作模式影响？；原因：原理图没有内部存储容量信息。
- `review.measurement_ranges`：正文列出的加速度和陀螺仪量程是否全部由当前器件与驱动支持？；原因：量程由芯片寄存器配置决定，原理图未提供。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `26acfd387f3b35736bcbbb7a8bba7a53941bd0ae7103a014be5becb5885cc69b` | `https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_sch_01.webp` |

---

源文档：`zh_CN/unit/imu.md`

源文档 SHA-256：`0bd70658217d43886abebd1ada7bf767f531e1409670c50843e9af943a72e594`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
