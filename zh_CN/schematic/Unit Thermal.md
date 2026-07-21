# Unit Thermal 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Thermal |
| SKU | U016 |
| 产品 ID | `unit-thermal-cc672b6b369c` |
| 源文档 | `zh_CN/unit/THERMAL.md` |

## 概述

Unit Thermal（U016）以 U1 MLX90640 红外热电堆阵列为核心，通过 J1 IIC_Socket_4P 提供 SCL、SDA、VCC 和 GND。U2 HT7533 将 J1 VCC 转换为 +3.3V 给 U1 VDD 供电，SCL/SDA 则分别经 R1/R2 4.7KΩ 上拉到 VCC。C1 100nF 为传感器本地去耦，C2 100nF/C3 10uF 位于 +3.3V 输出，C4 10uF 位于 VCC 输入。原理图未标注 I2C 地址、VCC 数值、成像分辨率、刷新率、视场角、温度范围或精度。

## 检索关键词

`Unit Thermal`、`U016`、`MLX90640`、`U1`、`HT7533`、`U2`、`IIC_Socket_4P`、`J1`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`R1 4.7KΩ`、`R2 4.7KΩ`、`VCC`、`+3.3V`、`C1 100nF`、`C2 100nF`、`C3 10uF`、`C4 10uF`、`0x33`、`32x24`、`768 pixels`、`64Hz`、`110x75 FOV`、`thermal imaging`、`红外热成像`、`热电堆阵列`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MLX90640 | 红外热电堆成像传感器，通过 I2C 接口通信并由 +3.3V 供电 | 图 18b13428c26c / 第 1 页 / 第 1 页 B2 U1 MLX90640，pin 1 SDA、pin 2 VDD、pin 3 GND、pin 4 SCL |
| U2 | HT7533 | 把 J1 VCC 输入转换为 +3.3V 的三端稳压器 | 图 18b13428c26c / 第 1 页 / 第 1 页 C2 U2 HT7533，pin 2 VIN 接 VCC、pin 3 VOUT 接 +3.3V、pin 1 GND |
| J1 | IIC_Socket_4P | 四针 Grove I2C 与电源接口 | 图 18b13428c26c / 第 1 页 / 第 1 页 B3 J1 IIC_Socket_4P，pins 1~4 IIC_SCL/IIC_SDA/VCC/GND |
| R1/R2 | 4.7KΩ | SCL/SDA 到 VCC 的 I2C 上拉电阻 | 图 18b13428c26c / 第 1 页 / 第 1 页 B3 R1 4.7KΩ 从 SCL 到 VCC，R2 4.7KΩ 从 SDA 到 VCC |
| C1 | 100nF | U1 +3.3V 电源的本地去耦电容 | 图 18b13428c26c / 第 1 页 / 第 1 页 B2 U1 VDD/+3.3V-C1 100nF-GND |
| C2/C3 | 100nF/10uF | HT7533 +3.3V 输出侧并联去耦与储能电容 | 图 18b13428c26c / 第 1 页 / 第 1 页 C2 U2 VOUT/+3.3V-C2 100nF/C3 10uF-GND |
| C4 | 10uF | HT7533 VIN/VCC 输入侧储能电容 | 图 18b13428c26c / 第 1 页 / 第 1 页 C2 U2 VIN/VCC-C4 10uF-GND |

## 系统结构

### Unit Thermal 系统架构

电路由 U1 MLX90640 热成像传感器、U2 HT7533 3.3V 稳压器、J1 四针 I2C 接口、R1/R2 I2C 上拉和 C1~C4 电源电容组成。

- 参数与网络：`sensor=U1 MLX90640`；`regulator=U2 HT7533`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`input_power=VCC`；`sensor_power=+3.3V`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B2:C3 完整 U1/U2/J1/R1/R2/C1~C4 电路

## 电源

### VCC 输入路径

J1 pin 3 VCC 连接 U2 VIN pin 2，并通过 C4 10uF 接地。

- 参数与网络：`connector=J1 pin3 VCC`；`regulator_input=U2 pin2 VIN`；`capacitor=C4 10uF`；`return=GND`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B3/C2 J1 VCC、U2 VIN 与 C4

### VCC 到 +3.3V 稳压

U2 HT7533 pin 2 VIN 接 VCC，pin 3 VOUT 输出 +3.3V，pin 1 GND 接地；+3.3V 供给 U1 VDD。

- 参数与网络：`input=U2 pin2 VIN VCC`；`output=U2 pin3 VOUT +3.3V`；`ground=U2 pin1 GND`；`load=U1 pin2 VDD`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 C2 U2 与 B2 U1 +3.3V 电源网络

### +3.3V 输出滤波

U2 VOUT 的 +3.3V 轨通过 C2 100nF 和 C3 10uF 并联接地。

- 参数与网络：`rail=+3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 C2 +3.3V-C2/C3-GND

### MLX90640 本地去耦

U1 VDD 的 +3.3V 节点通过 C1 100nF 接 GND。

- 参数与网络：`device=U1 MLX90640`；`rail=+3.3V`；`capacitor=C1 100nF`；`return=GND`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B2 U1 VDD/+3.3V-C1-GND

### 电源控制、充电与监测

本页未显示 U2 使能、负载开关、充电器、电池、电源良好信号或电压/电流监测器。

- 参数与网络：`enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页电源部分仅 U2 VIN/VOUT/GND 与 C1~C4

## 接口

### J1 IIC_Socket_4P 针脚

J1 pins 1~4 依次为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B3 J1 pins 1~4 与 IIC_SCL/IIC_SDA/VCC/GND

## 总线

### MLX90640 I2C 总线

J1 SCL/SDA 分别直连 U1 SCL/SDA，页面没有总线复用器、电平转换器或其他 I2C 设备。

- 参数与网络：`controller_connector=J1`；`device=U1 MLX90640`；`scl=J1 pin1 -> U1 pin4`；`sda=J1 pin2 -> U1 pin1`；`mux=null`；`level_shifter=null`；`other_devices=null`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B2:B3 U1 SCL/SDA 到 J1 pins 1/2 的直接连线

### I2C 上拉网络

SCL 经 R1 4.7KΩ 上拉到 VCC，SDA 经 R2 4.7KΩ 上拉到 VCC；传感器自身由独立 +3.3V 轨供电。

- 参数与网络：`scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC`；`pullup_rail=VCC`；`sensor_supply=+3.3V`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B3 R1/R2 至 VCC 与 B2 U1 VDD +3.3V

### 其他外部总线

本页仅显示 I2C，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 J1 仅 IIC_SCL/IIC_SDA/VCC/GND

## GPIO 与控制信号

### 中断与控制信号

U1 只引出 SDA、VDD、GND、SCL，本页没有 INT、ALERT、RESET、BOOT、EN 或其他 GPIO。

- 参数与网络：`interrupt=null`；`alert=null`；`reset=null`；`boot=null`；`enable=null`；`other_gpio=null`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 U1 MLX90640 四针符号与整页网络

## 时钟

### 时钟电路

本页未显示晶振、谐振器或外部时钟；SCL 是 I2C 总线时钟。

- 参数与网络：`crystal=null`；`oscillator=null`；`external_clock=null`；`bus_clock=IIC_SCL`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页无时钟器件，仅 U1/J1 SCL 网络

## 保护电路

### 接口与电源保护

J1 的 SCL、SDA、VCC 路径未显示 TVS/ESD、保险丝、反接、过压或独立限流保护；R1/R2 仅为 I2C 上拉。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`current_limit=null`；`pullups=R1/R2 4.7KΩ`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 J1 到 U1/U2 的完整路径，无保护器件

## 存储

### 外部存储器与内存

本页未显示主控、Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页仅 U1/U2/J1/R1/R2/C1~C4

## 传感器

### U1 MLX90640 引脚

U1 pin 1 SDA 连接 J1 IIC_SDA，pin 2 VDD 接 +3.3V，pin 3 GND 接地，pin 4 SCL 连接 J1 IIC_SCL。

- 参数与网络：`pin_1=SDA -> J1 pin2 IIC_SDA`；`pin_2=VDD +3.3V`；`pin_3=GND`；`pin_4=SCL -> J1 pin1 IIC_SCL`
- 证据：图 18b13428c26c / 第 1 页 / 第 1 页 B2 U1 MLX90640 pins 1~4 与 J1/电源网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Thermal 系统架构 | `sensor=U1 MLX90640`；`regulator=U2 HT7533`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`input_power=VCC`；`sensor_power=+3.3V` |
| 传感器 | U1 MLX90640 引脚 | `pin_1=SDA -> J1 pin2 IIC_SDA`；`pin_2=VDD +3.3V`；`pin_3=GND`；`pin_4=SCL -> J1 pin1 IIC_SCL` |
| 接口 | J1 IIC_Socket_4P 针脚 | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | MLX90640 I2C 总线 | `controller_connector=J1`；`device=U1 MLX90640`；`scl=J1 pin1 -> U1 pin4`；`sda=J1 pin2 -> U1 pin1`；`mux=null`；`level_shifter=null`；`other_devices=null` |
| 总线 | I2C 上拉网络 | `scl_pullup=R1 4.7KΩ to VCC`；`sda_pullup=R2 4.7KΩ to VCC`；`pullup_rail=VCC`；`sensor_supply=+3.3V` |
| 电源 | VCC 输入路径 | `connector=J1 pin3 VCC`；`regulator_input=U2 pin2 VIN`；`capacitor=C4 10uF`；`return=GND` |
| 电源 | VCC 到 +3.3V 稳压 | `input=U2 pin2 VIN VCC`；`output=U2 pin3 VOUT +3.3V`；`ground=U2 pin1 GND`；`load=U1 pin2 VDD` |
| 电源 | +3.3V 输出滤波 | `rail=+3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND` |
| 电源 | MLX90640 本地去耦 | `device=U1 MLX90640`；`rail=+3.3V`；`capacitor=C1 100nF`；`return=GND` |
| 电源 | 电源控制、充电与监测 | `enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`current_limit=null`；`pullups=R1/R2 4.7KΩ` |
| GPIO 与控制信号 | 中断与控制信号 | `interrupt=null`；`alert=null`；`reset=null`；`boot=null`；`enable=null`；`other_gpio=null` |
| 时钟 | 时钟电路 | `crystal=null`；`oscillator=null`；`external_clock=null`；`bus_clock=IIC_SCL` |
| 存储 | 外部存储器与内存 | `controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 总线地址 | MLX90640 I2C 地址 | `device=U1 MLX90640`；`schematic_address=null`；`candidate_from_product_doc=0x33`；`address_select=null` |
| 电源 | VCC 输入电压 | `net=VCC`；`input_voltage=null`；`allowed_range=null`；`i2c_pullup_voltage=null`；`candidate_from_product_doc=5V` |
| 传感器 | 热成像与测温性能 | `resolution=null`；`measurement_points=null`；`field_of_view=null`；`temperature_range=null`；`accuracy=null`；`refresh_rate=null`；`operating_temperature=null`；`current=null` |
| 总线 | I2C 速率与时序 | `pullups=4.7KΩ to VCC`；`frequency=null`；`maximum_rate=null`；`bus_capacitance=null`；`timing=null` |

## 待确认事项

- `address.mlx90640-i2c`：原理图没有标注 U1 的 I2C 地址或地址选择电路，不能仅凭本页确认 0x33。（证据：图 18b13428c26c / 第 1 页 / 第 1 页 U1/J1 I2C 网络，无十六进制地址或地址配置）
- `power.vcc-voltage`：原理图只标 VCC，没有标注 J1 输入电压数值或允许范围，也不能确认 I2C 上拉电平是否为 5V。（证据：图 18b13428c26c / 第 1 页 / 第 1 页 J1 pin3/U2 VIN/R1/R2 仅标 VCC，无电压数字）
- `sensor.imaging-performance`：原理图确认 U1 为 MLX90640，但未标注 32×24 分辨率、测温点数、视场角、测温范围、精度、刷新率、工作温度或工作电流。（证据：图 18b13428c26c / 第 1 页 / 第 1 页 U1 MLX90640 符号仅给型号和电气连接，无性能参数）
- `bus.i2c-speed`：原理图显示 SCL/SDA 和 4.7KΩ 上拉，但未标注工作频率、最大速率、总线电容或时序参数。（证据：图 18b13428c26c / 第 1 页 / 第 1 页 U1-J1 SCL/SDA 与 R1/R2，无频率/时序文字）
- `review.i2c-address`：U1 的 I2C 地址是否固定为 0x33，是否存在可配置地址方式？；原因：当前原理图没有地址或地址选择电路。
- `review.vcc-voltage`：Unit Thermal 的 VCC 输入范围和 I2C 上拉电平是多少？；原因：原理图只标 VCC，传感器则由 +3.3V 供电；需电气规范确认接口兼容性。
- `review.imaging-performance`：该 MLX90640 版本的分辨率、视场角、温度范围、精度、刷新率和电流参数是什么？；原因：这些器件/整机性能参数未在原理图中标注。
- `review.i2c-speed`：推荐和允许的 I2C 总线频率与时序范围是什么？；原因：原理图只给上拉阻值，没有总线时序参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `18b13428c26c9d3c3155d47aca8f0dface250362abdaf1ee7f726acbf96ad966` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/708/U016-UNIT_THERMAL-SCHE_page_01.png` |

---

源文档：`zh_CN/unit/THERMAL.md`

源文档 SHA-256：`15d1d22e5ce5e3f1d8b858a179130486c86fd8efa76f4d58e5fb57c98be13dde`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
