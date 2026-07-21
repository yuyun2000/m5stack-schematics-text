# Unit NCIR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NCIR |
| SKU | U028 |
| 产品 ID | `unit-ncir-d867e38eced1` |
| 源文档 | `zh_CN/unit/ncir.md` |

## 概述

Unit NCIR（U028）以 U1 MLX90614 非接触红外温度传感器为核心，通过 J1 IIC_Socket_4P 提供 SCL、SDA、VCC 和 GND。J1 的 VCC 与 +5V 为同一输入轨，U2 HT7533 将其转换为 +3.3V 给 U1 VDD 供电；SCL/SDA 则分别由 R1/R2 4.7KΩ 上拉到 VCC/+5V。原理图未显示主控、存储、外部时钟、复位、保护或中断线路，也未标注 I2C 地址、速率、传感器完整后缀与测量性能。

## 检索关键词

`Unit NCIR`、`U028`、`NCIR`、`MLX90614`、`U1`、`HT7533`、`U2`、`IIC_Socket_4P`、`J1`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`R1 4.7KΩ`、`R2 4.7KΩ`、`VCC`、`+5V`、`+3.3V`、`C1 100nF`、`C2 100nF`、`C3 10uF`、`C4 10uF`、`C5 100nF`、`0x5A`、`红外测温`、`非接触温度传感器`、`Grove I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MLX90614 | 非接触红外温度传感器，通过 SCL/SDA 连接 I2C 接口并由 +3.3V 供电 | 图 58c822aa1181 / 第 1 页 / 页面上中 U1 MLX90614，VDD/GND/SCL/SDA 四个引脚 |
| U2 | HT7533 | 把 VCC/+5V 转换为 +3.3V 的三端稳压器 | 图 58c822aa1181 / 第 1 页 / 页面下中 U2 HT7533，pin 2 VIN 接 +5V/VCC、pin 3 VOUT 接 +3.3V、pin 1 GND |
| J1 | IIC_Socket_4P | 四针 Grove I2C 与电源接口 | 图 58c822aa1181 / 第 1 页 / 页面右上 J1 IIC_Socket_4P，pins 1~4 标注 IIC_SCL/IIC_SDA/VCC/GND |
| R1/R2 | 4.7KΩ | SCL 与 SDA 到 VCC/+5V 的 I2C 上拉电阻 | 图 58c822aa1181 / 第 1 页 / 页面右上 R1 4.7KΩ 从 SCL 到 VCC，R2 4.7KΩ 从 SDA 到 VCC |
| C1 | 100nF | U1 +3.3V 电源的本地去耦电容 | 图 58c822aa1181 / 第 1 页 / 页面 U1 左侧 +3.3V-C1 100nF-GND |
| C2/C3 | 100nF/10uF | HT7533 +3.3V 输出侧的并联去耦和储能电容 | 图 58c822aa1181 / 第 1 页 / 页面左下 U2 VOUT/+3.3V 侧 C2 100nF、C3 10uF 到 GND |
| C4/C5 | 10uF/100nF | HT7533 VCC/+5V 输入侧的并联储能和去耦电容 | 图 58c822aa1181 / 第 1 页 / 页面右下 U2 VIN/+5V/VCC 侧 C4 10uF、C5 100nF 到 GND |

## 系统结构

### Unit NCIR 系统架构

电路由 U1 MLX90614 红外温度传感器、U2 HT7533 3.3V 稳压器、J1 四针 I2C 接口、两只 I2C 上拉电阻和五只电源电容组成。

- 参数与网络：`sensor=U1 MLX90614`；`regulator=U2 HT7533`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`input_power=VCC/+5V`；`sensor_power=+3.3V`
- 证据：图 58c822aa1181 / 第 1 页 / 整页 U1/U2/J1/R1/R2/C1~C5 与同名网络

## 电源

### VCC/+5V 输入

J1 pin 3 VCC 连接 U2 VIN pin 2，电源线上同时标注 VCC 与 +5V，并由 C4 10uF、C5 100nF 对地滤波。

- 参数与网络：`connector=J1 pin 3 VCC`；`rail=+5V/VCC`；`regulator_input=U2 pin 2 VIN`；`capacitors=C4 10uF,C5 100nF`
- 证据：图 58c822aa1181 / 第 1 页 / 页面下部 U2 VIN 连线上的 +5V/VCC 标签及 C4/C5；页面右上 J1 pin 3 VCC

### +5V 到 +3.3V 稳压

U2 HT7533 pin 2 VIN 接 VCC/+5V，pin 3 VOUT 输出 +3.3V，pin 1 接 GND；+3.3V 供给 U1 VDD。

- 参数与网络：`input=U2 pin 2 VIN +5V/VCC`；`output=U2 pin 3 VOUT +3.3V`；`ground=U2 pin 1 GND`；`load=U1 VDD`
- 证据：图 58c822aa1181 / 第 1 页 / 页面下中 U2 HT7533 三个引脚与 +5V/+3.3V/GND 网络，页面上部 U1 VDD +3.3V

### +3.3V 输出滤波

U2 VOUT 的 +3.3V 轨通过 C2 100nF 和 C3 10uF 并联接地。

- 参数与网络：`rail=+3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND`
- 证据：图 58c822aa1181 / 第 1 页 / 页面左下 +3.3V-U2 VOUT 与 C2/C3 到 GND

### U1 本地去耦

U1 VDD 的 +3.3V 节点通过 C1 100nF 接 GND。

- 参数与网络：`device=U1 MLX90614`；`rail=+3.3V`；`capacitor=C1 100nF`；`return=GND`
- 证据：图 58c822aa1181 / 第 1 页 / 页面 U1 左侧 +3.3V-C1 100nF-GND

### 电源控制与监测

本页未显示 U2 使能脚、负载开关、充电器、电池连接、电源良好信号或电压/电流监测器。

- 参数与网络：`enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null`
- 证据：图 58c822aa1181 / 第 1 页 / 整页 U2 仅有 VIN/VOUT/GND，且无其他电源控制、充电或监测器件

## 接口

### J1 IIC_Socket_4P 针脚

J1 pins 1~4 依次为 IIC_SCL、IIC_SDA、VCC、GND；pin 3 VCC 与 +5V 输入轨同网。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 58c822aa1181 / 第 1 页 / 页面右上 J1 pins 1~4；页面下部 U2 VIN 连续网络同时标 +5V 与 VCC

## 总线

### MLX90614 I2C 总线

U1 SCL/SDA 分别直连 J1 IIC_SCL/IIC_SDA，构成两线 I2C 接口；原理图中没有总线复用器、电平转换器或其他 I2C 从设备。

- 参数与网络：`controller_connector=J1`；`device=U1 MLX90614`；`scl=J1 pin 1 IIC_SCL -> U1 SCL`；`sda=J1 pin 2 IIC_SDA -> U1 SDA`；`level_shifter=null`；`mux=null`；`other_devices=null`
- 证据：图 58c822aa1181 / 第 1 页 / 页面上部 U1 SCL/SDA 到 J1 pins 1/2 的直接连线

### I2C 上拉网络

SCL 经 R1 4.7KΩ 上拉到 VCC，SDA 经 R2 4.7KΩ 上拉到 VCC；VCC 在电源部分与 +5V 同网，因此两根总线均被上拉至 +5V 轨。

- 参数与网络：`scl_pullup=R1 4.7KΩ to VCC/+5V`；`sda_pullup=R2 4.7KΩ to VCC/+5V`；`pullup_voltage=+5V`；`sensor_supply=+3.3V`
- 证据：图 58c822aa1181 / 第 1 页 / 页面右上 R1/R2 至 VCC；页面下部 VCC 与 +5V 同一连续输入网络

### 其他外部总线

本页仅显示 I2C，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S 接口。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 58c822aa1181 / 第 1 页 / 整页外部接口 J1 仅 IIC_SCL/IIC_SDA/VCC/GND

## GPIO 与控制信号

### 中断与控制信号

U1 只引出 VDD、GND、SCL、SDA，本页没有 ALERT、INT、RESET、BOOT、EN 或其他 GPIO/控制网络。

- 参数与网络：`interrupt=null`；`alert=null`；`reset=null`；`boot=null`；`enable=null`；`other_gpio=null`
- 证据：图 58c822aa1181 / 第 1 页 / 页面上中 U1 MLX90614 仅有四个已标引脚；整页无其他控制网络

## 时钟

### 时钟电路

本页未显示晶振、谐振器或外部时钟输入；SCL 是 I2C 总线时钟而非板载晶振网络。

- 参数与网络：`crystal=null`；`oscillator=null`；`external_clock=null`；`bus_clock=IIC_SCL`
- 证据：图 58c822aa1181 / 第 1 页 / 整页元件与网络，无晶振/振荡器；仅 J1/U1 的 SCL 总线线

## 保护电路

### 接口与电源保护

J1 的 SCL、SDA、VCC 路径未显示 TVS/ESD、保险丝、限流、反接或过压保护器件；R1/R2 仅作为 I2C 上拉。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`pullups=R1/R2 4.7KΩ`
- 证据：图 58c822aa1181 / 第 1 页 / 整页 J1 到 U1/U2 路径，无保护器件符号或位号

## 存储

### 存储器与外部内存

本页未显示 Flash、EEPROM、RAM、SD 卡或其他外部存储/内存器件。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 58c822aa1181 / 第 1 页 / 整页仅 U1/U2/J1、R1/R2 与 C1~C5，无存储器件

## 传感器

### U1 MLX90614 连接

U1 VDD 接 +3.3V，GND 接地，SCL 连接 J1 pin 1 IIC_SCL，SDA 连接 J1 pin 2 IIC_SDA。

- 参数与网络：`vdd=+3.3V`；`ground=GND`；`clock=SCL -> J1 pin 1 IIC_SCL`；`data=SDA -> J1 pin 2 IIC_SDA`
- 证据：图 58c822aa1181 / 第 1 页 / 页面上部 U1 MLX90614 的 VDD/GND/SCL/SDA 与 J1 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NCIR 系统架构 | `sensor=U1 MLX90614`；`regulator=U2 HT7533`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`input_power=VCC/+5V`；`sensor_power=+3.3V` |
| 传感器 | U1 MLX90614 连接 | `vdd=+3.3V`；`ground=GND`；`clock=SCL -> J1 pin 1 IIC_SCL`；`data=SDA -> J1 pin 2 IIC_SDA` |
| 接口 | J1 IIC_Socket_4P 针脚 | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC +5V`；`pin_4=GND` |
| 总线 | MLX90614 I2C 总线 | `controller_connector=J1`；`device=U1 MLX90614`；`scl=J1 pin 1 IIC_SCL -> U1 SCL`；`sda=J1 pin 2 IIC_SDA -> U1 SDA`；`level_shifter=null`；`mux=null`；`other_devices=null` |
| 总线 | I2C 上拉网络 | `scl_pullup=R1 4.7KΩ to VCC/+5V`；`sda_pullup=R2 4.7KΩ to VCC/+5V`；`pullup_voltage=+5V`；`sensor_supply=+3.3V` |
| 电源 | VCC/+5V 输入 | `connector=J1 pin 3 VCC`；`rail=+5V/VCC`；`regulator_input=U2 pin 2 VIN`；`capacitors=C4 10uF,C5 100nF` |
| 电源 | +5V 到 +3.3V 稳压 | `input=U2 pin 2 VIN +5V/VCC`；`output=U2 pin 3 VOUT +3.3V`；`ground=U2 pin 1 GND`；`load=U1 VDD` |
| 电源 | +3.3V 输出滤波 | `rail=+3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND` |
| 电源 | U1 本地去耦 | `device=U1 MLX90614`；`rail=+3.3V`；`capacitor=C1 100nF`；`return=GND` |
| 电源 | 电源控制与监测 | `enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`pullups=R1/R2 4.7KΩ` |
| GPIO 与控制信号 | 中断与控制信号 | `interrupt=null`；`alert=null`；`reset=null`；`boot=null`；`enable=null`；`other_gpio=null` |
| 时钟 | 时钟电路 | `crystal=null`；`oscillator=null`；`external_clock=null`；`bus_clock=IIC_SCL` |
| 存储 | 存储器与外部内存 | `flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 总线地址 | MLX90614 I2C 地址 | `device=U1 MLX90614`；`schematic_address=null`；`candidate_from_product_doc=0x5A`；`address_select=null` |
| 核心器件 | U1 完整型号后缀 | `schematic_part_number=MLX90614`；`candidate_from_product_doc=MLX90614ESF-AAA`；`confirmed_suffix=null` |
| 总线 | I2C 速率 | `pullups=4.7KΩ to +5V`；`schematic_speed=null`；`candidate_from_product_doc=100Kbps` |
| 传感器 | 红外测温性能 | `object_range=null`；`ambient_range=null`；`accuracy=null`；`field_of_view=null`；`response_time=null` |

## 待确认事项

- `address.mlx90614-i2c`：原理图没有标注 U1 的 I2C 地址，也没有地址选择电阻或地址配置引脚；因此不能仅凭本页确认 0x5A。（证据：图 58c822aa1181 / 第 1 页 / 页面 U1/J1 I2C 网络及整页文字，无 0x 地址或地址选择电路）
- `component.sensor-full-part-number`：原理图器件文字仅为 MLX90614，未标注封装/视场/温度等级等后缀，因此无法仅凭本页确认 MLX90614ESF-AAA。（证据：图 58c822aa1181 / 第 1 页 / 页面上中 U1 下方仅标 MLX90614）
- `bus.i2c-speed`：原理图显示 SCL/SDA 与 4.7KΩ 上拉，但未标注 I2C 工作速率或最大速率，不能仅凭本页确认 100Kbps。（证据：图 58c822aa1181 / 第 1 页 / 页面 U1-J1 SCL/SDA 与 R1/R2，上方及整页无频率/速率文字）
- `sensor.measurement-performance`：原理图确认 U1 为 MLX90614，但未标注物体/环境测温范围、精度、视场角或响应时间，无法由本页确认这些性能参数。（证据：图 58c822aa1181 / 第 1 页 / 页面 U1 MLX90614 符号仅给器件名和电气连接，无测量性能文字）
- `review.i2c-address`：本产品硬件版本 U1 的 I2C 地址是否为 0x5A，且是否可重编程？；原因：原理图没有地址或地址配置说明，需要对应传感器 datasheet、EEPROM 配置或实测确认。
- `review.sensor-full-part-number`：U1 的完整订货型号是否为 MLX90614ESF-AAA？；原因：原理图只标 MLX90614，后缀需 BOM、实物丝印或采购资料确认。
- `review.i2c-speed`：Unit NCIR 推荐和允许的 I2C 总线速率范围是什么？；原因：本页只给出连接和上拉阻值，没有时序或速率参数。
- `review.measurement-performance`：该 U1 具体版本的物体/环境测温范围、精度和视场角分别是多少？；原因：这些是器件版本和应用性能参数，原理图未提供。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `58c822aa1181f12d26052c1334a2a672f84754e708d44a8385e92d37b504820a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/U028-unit-ncir.jpg` |

---

源文档：`zh_CN/unit/ncir.md`

源文档 SHA-256：`0fe50061d2c52540f20aee63508ff6ddb56b2a7a266ca5c31a12be02fc4bc93f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
