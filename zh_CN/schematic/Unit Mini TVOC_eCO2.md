# Unit Mini TVOC/eCO2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini TVOC/eCO2 |
| SKU | U088 |
| 产品 ID | `unit-mini-tvoc-eco2-eb6f13365a1f` |
| 源文档 | `zh_CN/unit/tvoc.md` |

## 概述

Unit Mini TVOC/eCO2（U088）以 U2 SGP30 数字气体传感器为核心，通过 J1 HY-2.0_IIC 提供 SCL、SDA、+5V 和 GND。U1 RT9193-1.8V 将 +5V 转换为 +1.8V，供 SGP30 VDD/VDDH 及传感器侧 I2C 上拉使用。Q1/Q2 BSS138 对 SDA/SCL 进行双向电平转换，主机侧 R1/R2 4.7KΩ 上拉到 +5V，传感器侧 R3/R4 4.7KΩ 上拉到 +1.8V。原理图未标注 0x58 地址、TVOC/eCO2 量程、采样率、精度、湿度补偿或校准功能。

## 检索关键词

`Unit Mini TVOC/eCO2`、`U088`、`SGP30`、`U2`、`RT9193-1.8V`、`U1`、`BSS138`、`Q1`、`Q2`、`I2C level shifter`、`HY-2.0_IIC`、`J1`、`SCL`、`SDA`、`+5V`、`+1.8V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 4.7KΩ`、`C1 1uF`、`C2 1uF`、`C3 22nF`、`C4 100nF`、`0x58`、`TVOC`、`eCO2`、`VOC`、`H2`、`air quality`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SGP30 | 数字多像素气体传感器，通过 1.8V I2C 接口通信 | 图 e3e857fea653 / 第 1 页 / 页面右下 U2 SGP30，pins 1/5 VDD/VDDH、pin2 VSS、pin3 SDA、pin6 SCL、pin7 diePad |
| U1 | RT9193-1.8V | 将 +5V 稳压为 +1.8V 的 LDO，带 EN 与 BP 引脚 | 图 e3e857fea653 / 第 1 页 / 页面左上 U1 RT9193-1.8V，pins 1~5 IN/GND/EN/BP/OUT |
| J1 | HY-2.0_IIC | 四针 Grove I2C 与 +5V 电源接口 | 图 e3e857fea653 / 第 1 页 / 页面右上 J1 pins 1~4 IIC_SCL/IIC_SDA/VCC(+5V)/GND |
| Q1/Q2 | BSS138 | SDA/SCL 的双向 MOSFET 电平转换器 | 图 e3e857fea653 / 第 1 页 / 页面下部 Q1/Q2 BSS138 分别串接 SDA/SCL，栅极接 +1.8V |
| R1/R2 | 4.7KΩ | 主机侧 SDA/SCL 到 +5V 的上拉电阻 | 图 e3e857fea653 / 第 1 页 / 页面左下 R1 4.7KΩ SDA-+5V、R2 4.7KΩ SCL-+5V |
| R3/R4 | 4.7KΩ | 传感器侧 SDA/SCL 到 +1.8V 的上拉电阻 | 图 e3e857fea653 / 第 1 页 / 页面下中 R3 4.7KΩ SDA-+1.8V、R4 4.7KΩ SCL-+1.8V |
| C1/C2 | 1uF/1uF | RT9193 输入 +5V 与输出 +1.8V 的电源电容 | 图 e3e857fea653 / 第 1 页 / 页面上部 U1 输入 C1 1uF、输出 C2 1uF 到 GND |
| C3 | 22nF | RT9193 BP pin 4 到 GND 的旁路电容 | 图 e3e857fea653 / 第 1 页 / 页面 U1 pin4 BP-C3 22nF-GND |
| C4 | 100nF | SGP30 +1.8V 电源的本地去耦电容 | 图 e3e857fea653 / 第 1 页 / 页面 U2 右侧 +1.8V-C4 100nF-GND |

## 系统结构

### Unit Mini TVOC/eCO2 架构

U2 SGP30 通过 Q1/Q2 BSS138 电平转换连接 J1 I2C，U1 RT9193-1.8V 从 +5V 生成传感器 +1.8V。

- 参数与网络：`sensor=U2 SGP30`；`regulator=U1 RT9193-1.8V`；`level_shifter=Q1/Q2 BSS138`；`interface=J1 HY-2.0_IIC`；`host_power=+5V`；`sensor_power=+1.8V`
- 证据：图 e3e857fea653 / 第 1 页 / 整页 U1/U2/J1/Q1/Q2/R1~R4/C1~C4

## 电源

### +5V 到 +1.8V 稳压

U1 RT9193-1.8V IN pin1 与 EN pin3 接 +5V，GND pin2 接地，OUT pin5 输出 +1.8V，BP pin4 经 C3 22nF 接地。

- 参数与网络：`input=pin1 +5V`；`enable=pin3 +5V always enabled`；`ground=pin2`；`output=pin5 +1.8V`；`bypass=pin4-C3 22nF-GND`
- 证据：图 e3e857fea653 / 第 1 页 / 页面左上 U1 RT9193-1.8V

### LDO 输入输出电容

C1 1uF 从 +5V 接地，C2 1uF 从 +1.8V 接地；C4 100nF 为 SGP30 本地去耦。

- 参数与网络：`input=C1 1uF`；`output=C2 1uF`；`sensor=C4 100nF`
- 证据：图 e3e857fea653 / 第 1 页 / 页面 C1/C2/C4 电源电容

### 电源控制与电池

除固定使能 LDO 外，本页未显示负载开关、充电器、电池、电源良好或电压/电流监测。

- 参数与网络：`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null`
- 证据：图 e3e857fea653 / 第 1 页 / 整页电源仅 RT9193 与电容

## 接口

### J1 HY-2.0_IIC

J1 pins 1~4 依次为 IIC_SCL、IIC_SDA、VCC/+5V、GND。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 e3e857fea653 / 第 1 页 / 页面右上 J1 pins 1~4

## 总线

### I2C 双向电平转换

主机 SDA/SCL 分别经 Q1/Q2 BSS138 连接 U2 SDA/SCL，MOSFET 栅极接 +1.8V。

- 参数与网络：`sda=J1 SDA -> Q1 -> U2 pin3`；`scl=J1 SCL -> Q2 -> U2 pin6`；`gate_rail=+1.8V`
- 证据：图 e3e857fea653 / 第 1 页 / 页面下部 SDA/SCL-Q1/Q2-U2

### I2C 两侧上拉

主机 SDA/SCL 侧由 R1/R2 4.7KΩ 上拉到 +5V，SGP30 SDA/SCL 侧由 R3/R4 4.7KΩ 上拉到 +1.8V。

- 参数与网络：`host_sda=R1 4.7KΩ to +5V`；`host_scl=R2 4.7KΩ to +5V`；`sensor_sda=R3 4.7KΩ to +1.8V`；`sensor_scl=R4 4.7KΩ to +1.8V`
- 证据：图 e3e857fea653 / 第 1 页 / 页面 R1~R4 与 SDA/SCL 双电平域

### 其他外部总线

本页仅显示 I2C，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 e3e857fea653 / 第 1 页 / J1 仅 IIC_SCL/IIC_SDA/VCC/GND

## GPIO 与控制信号

### 控制与中断

SGP30 符号只连接电源与 SDA/SCL，本页没有 RESET、EN、INT、ALERT、BOOT 或其他 GPIO。

- 参数与网络：`reset=null`；`enable=null`；`interrupt=null`；`alert=null`；`boot=null`；`other_gpio=null`
- 证据：图 e3e857fea653 / 第 1 页 / U2 SGP30 仅电源/I2C 引脚

## 时钟

### 时钟与存储

本页未显示外部晶振、主控、Flash、EEPROM、RAM 或 SD 卡；SCL 为 I2C 总线时钟。

- 参数与网络：`external_clock=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 e3e857fea653 / 第 1 页 / 整页仅传感器/LDO/电平转换/接口/阻容

## 保护电路

### 接口保护

J1 SCL/SDA/+5V 未显示 TVS/ESD、保险丝、反接或过压保护；Q1/Q2 是电平转换器。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`level_shifter=Q1/Q2 BSS138`
- 证据：图 e3e857fea653 / 第 1 页 / 整页 J1 到 U1/U2 路径

## 传感器

### SGP30 引脚

U2 VDD pin1 与 VDDH pin5 接 +1.8V，VSS pin2 与 diePad pin7 接 GND，SDA pin3 和 SCL pin6 接传感器侧 I2C。

- 参数与网络：`vdd=pin1 +1.8V`；`vddh=pin5 +1.8V`；`vss=pin2 GND`；`diepad=pin7 GND`；`sda=pin3`；`scl=pin6`
- 证据：图 e3e857fea653 / 第 1 页 / 页面右下 U2 pins 1/2/3/5/6/7

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini TVOC/eCO2 架构 | `sensor=U2 SGP30`；`regulator=U1 RT9193-1.8V`；`level_shifter=Q1/Q2 BSS138`；`interface=J1 HY-2.0_IIC`；`host_power=+5V`；`sensor_power=+1.8V` |
| 传感器 | SGP30 引脚 | `vdd=pin1 +1.8V`；`vddh=pin5 +1.8V`；`vss=pin2 GND`；`diepad=pin7 GND`；`sda=pin3`；`scl=pin6` |
| 接口 | J1 HY-2.0_IIC | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC +5V`；`pin_4=GND` |
| 总线 | I2C 双向电平转换 | `sda=J1 SDA -> Q1 -> U2 pin3`；`scl=J1 SCL -> Q2 -> U2 pin6`；`gate_rail=+1.8V` |
| 总线 | I2C 两侧上拉 | `host_sda=R1 4.7KΩ to +5V`；`host_scl=R2 4.7KΩ to +5V`；`sensor_sda=R3 4.7KΩ to +1.8V`；`sensor_scl=R4 4.7KΩ to +1.8V` |
| 电源 | +5V 到 +1.8V 稳压 | `input=pin1 +5V`；`enable=pin3 +5V always enabled`；`ground=pin2`；`output=pin5 +1.8V`；`bypass=pin4-C3 22nF-GND` |
| 电源 | LDO 输入输出电容 | `input=C1 1uF`；`output=C2 1uF`；`sensor=C4 100nF` |
| 电源 | 电源控制与电池 | `load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null` |
| 保护电路 | 接口保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`level_shifter=Q1/Q2 BSS138` |
| GPIO 与控制信号 | 控制与中断 | `reset=null`；`enable=null`；`interrupt=null`；`alert=null`；`boot=null`；`other_gpio=null` |
| 时钟 | 时钟与存储 | `external_clock=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 总线地址 | SGP30 I2C 地址 | `device=SGP30`；`address=null`；`candidate_from_product_doc=0x58` |
| 传感器 | 气体测量性能 | `ethanol_range=null`；`h2_range=null`；`tvoc_range=null`；`eco2_range=null`；`accuracy=null`；`resolution=null`；`sample_rate=null`；`stability=null` |
| 传感器 | 湿度补偿与校准 | `humidity_sensor=null`；`humidity_compensation=null`；`baseline_calibration=null`；`eco2_algorithm=null` |
| 总线 | I2C 速率 | `pullups=4.7KΩ`；`level_shifter=BSS138`；`frequency=null`；`bus_capacitance=null`；`timing=null` |

## 待确认事项

- `address.sgp30`：原理图未标注 I2C 地址或地址选择电路，不能仅凭本页确认 0x58。（证据：图 e3e857fea653 / 第 1 页 / U2/J1 I2C 网络，无地址文字）
- `sensor.measurement-performance`：原理图未标注 Ethanol/H2/TVOC/eCO2 量程、精度、分辨率、1Hz 采样率或长期稳定性。（证据：图 e3e857fea653 / 第 1 页 / U2 SGP30 仅型号/连接，无性能文字）
- `sensor.compensation-calibration`：原理图未显示外部湿度传感器，也未描述片上湿度补偿、baseline 校准或 eCO2 算法行为。（证据：图 e3e857fea653 / 第 1 页 / 整页只有 SGP30，无湿度传感器或算法说明）
- `bus.i2c-speed`：原理图给出 4.7KΩ 上拉和 BSS138 电平转换，但未标注 I2C 频率、总线电容或时序。（证据：图 e3e857fea653 / 第 1 页 / SCL/SDA 转换与上拉，无时序文字）
- `review.i2c-address`：SGP30 的 I2C 地址是否固定为 0x58？；原因：原理图无地址说明或选择网络。
- `review.measurement-performance`：各气体/TVOC/eCO2 的量程、精度、分辨率和采样率是什么？；原因：性能参数未在原理图中标注。
- `review.compensation-calibration`：湿度补偿、baseline 校准和 eCO2 推算的固件流程是什么？；原因：原理图只给硬件连接，不含算法或外部湿度源。
- `review.i2c-speed`：推荐和允许的 I2C 频率/时序范围是什么？；原因：图纸只有电平转换和上拉参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e3e857fea653e05cdf1e8ea35a56fd112ec09adc9c5041462b186a8d0a9367eb` | `https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_sch_01.webp` |

---

源文档：`zh_CN/unit/tvoc.md`

源文档 SHA-256：`fba51488a3e0082cea0e10aeaa01f0d5f1ddd04d7397f9d29bc3cce31c5915bd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
