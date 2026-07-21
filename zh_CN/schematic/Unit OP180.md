# Unit OP180 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit OP180 |
| SKU | U058 |
| 产品 ID | `unit-op180-07ef3904e266` |
| 源文档 | `zh_CN/unit/OP180.md` |

## 概述

Unit OP180（U058）以 U1 ITR9606 红外发射/光电晶体管对为核心，发射 LED 由 VCC 经 R1 1KΩ 限流后接地。接收侧光电晶体管的集电极连接输出节点、发射极接地，输出节点同时连接 R3 10KΩ 上拉、R2 20KΩ 下拉和 C4 100nF 滤波，并送到 J1 pin 1 MISO；J1 pin 2 未连接，pin 3/4 为 VCC/GND。页面没有电源转换、保护、主控、总线控制器、时钟或存储器，也没有标明 VCC 数值和遮挡状态对应的最终逻辑定义。

## 检索关键词

`Unit OP180`、`U058`、`OP180`、`ITR9606`、`U1`、`红外光电开关`、`光电晶体管`、`红外发射 LED`、`J1`、`GROVE_IO`、`MISO`、`Digital Output`、`VCC`、`GND`、`R1 1KΩ`、`R2 20KΩ`、`R3 10KΩ`、`C4 100nF`、`C5 100nF`、`output pull-up`、`output pull-down`、`RC filter`、`槽型光电开关`、`object detection`、`pin 1 MISO`、`pin 2 NC`、`pin 3 VCC`、`pin 4 GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ITR9606 | 集成红外发射 LED 与光电晶体管接收器的非接触光电检测器 | 图 dc417b1afd7c / 第 1 页 / 页面中央 U1 ITR9606，左侧发光二极管与右侧光电晶体管符号 |
| J1 | GROVE_IO | 四针数字输出与电源接口 | 图 dc417b1afd7c / 第 1 页 / 页面右侧 J1 GROVE_IO，pin 1 MISO、pin 2 未连接、pin 3 VCC、pin 4 GND |
| R1 | 1KΩ | U1 红外发射 LED 的 VCC 侧串联限流电阻 | 图 dc417b1afd7c / 第 1 页 / 页面 U1 左上 VCC-R1 1KΩ-U1 发射 LED-GND 路径 |
| R2 | 20KΩ | MISO 输出节点到 GND 的下拉电阻 | 图 dc417b1afd7c / 第 1 页 / 页面 U1 右侧输出节点-R2 20KΩ-GND |
| R3 | 10KΩ | MISO 输出节点到 VCC 的上拉电阻 | 图 dc417b1afd7c / 第 1 页 / 页面 U1 右上 VCC-R3 10KΩ-输出节点 |
| C4 | 100nF | MISO 输出节点到 GND 的滤波电容 | 图 dc417b1afd7c / 第 1 页 / 页面输出节点-C4 100nF-GND |
| C5 | 100nF | VCC 到 GND 的电源去耦电容 | 图 dc417b1afd7c / 第 1 页 / 页面左侧 VCC-C5 100nF-GND |

## 系统结构

### Unit OP180 系统架构

电路由 U1 ITR9606 红外发射/接收器、发射限流 R1、输出偏置 R2/R3、输出滤波 C4、电源去耦 C5 和 J1 GROVE_IO 组成。

- 参数与网络：`sensor=U1 ITR9606`；`emitter_bias=R1 1KΩ`；`receiver_bias=R3 10KΩ pull-up,R2 20KΩ pull-down`；`output_filter=C4 100nF`；`decoupling=C5 100nF`；`connector=J1 GROVE_IO`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页 U1/J1/R1~R3/C4/C5 与 VCC/GND/MISO 网络

## 电源

### VCC 电源路径

J1 pin 3 VCC 直接供给 R1 发射支路、R3 输出上拉和 C5 去耦；本页没有稳压器、LDO、DC/DC 或负载开关。

- 参数与网络：`input=J1 pin 3 VCC`；`loads=R1,R3,C5`；`regulator=null`；`ldo=null`；`dc_dc=null`；`load_switch=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面各 VCC 同名节点及 J1 pin 3，整页无电源转换器件

### VCC 去耦

C5 100nF 直接连接在 VCC 与 GND 之间。

- 参数与网络：`capacitor=C5 100nF`；`rail=VCC`；`return=GND`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面左侧 VCC-C5 100nF-GND

### 充电、电池与监测

本页未显示充电器、电池连接、电源良好信号、电压/电流监测或电源使能控制。

- 参数与网络：`charger=null`；`battery=null`；`power_good=null`；`monitor=null`；`enable=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页仅 VCC 直供 R1/R3/C5，无其他电源器件

## 接口

### J1 GROVE_IO 针脚

J1 pin 1 标注 MISO 并连接检测输出，pin 2 以未连接标记结束，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`pin_1=MISO，数字/模拟检测输出`；`pin_2=NC`；`pin_3=VCC，电源输入`；`pin_4=GND`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面右侧 J1 pins 1~4 与 MISO/NC/VCC/GND

## 总线

### 外部总线

虽然输出网络名为 MISO，但本页没有 MOSI、SCK、CS 或任何控制器/从设备，不能构成 SPI；也未显示 I2C、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`digital_output=MISO`；`spi=null`；`i2c=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页仅 J1 pin 1 单路 MISO 输出，无配套总线信号

## GPIO 与控制信号

### 检测输出方向

J1 pin 1 MISO 是从 U1 接收支路输出到外部主机的信号；J1 pin 2 未使用，页面没有额外 GPIO、方向控制、中断、RESET、BOOT 或 EN 网络。

- 参数与网络：`output=J1 pin 1 MISO`；`direction=unit to host`；`unused=J1 pin 2`；`direction_control=null`；`interrupt=null`；`reset=null`；`boot=null`；`enable=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面 U1 接收节点到 J1 pin 1 MISO，J1 pin 2 NC，整页无其他控制网络

## 时钟

### 时钟、复位、调试与存储

本页未显示晶振/时钟、复位、调试接口、主控、Flash、EEPROM、RAM 或 SD 卡。

- 参数与网络：`clock=null`；`reset=null`；`debug=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页仅 U1/J1/R1~R3/C4/C5，无数字控制、时钟或存储器件

## 保护电路

### 接口与电源保护

J1 的 MISO 和 VCC 路径未显示 TVS/ESD、保险丝、反接、过压或独立限流保护；R1 是红外 LED 工作限流电阻。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`interface_current_limit=null`；`emitter_current_limit=R1 1KΩ`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页 J1-MISO/VCC 路径，无保护器件符号或位号

## 传感器

### U1 ITR9606 光电结构

U1 符号内左侧为向右发光的红外 LED，右侧为受光光电晶体管；两侧在电气上分别形成发射支路和接收输出支路。

- 参数与网络：`emitter=infrared LED`；`receiver=phototransistor`；`electrical_isolation_between_branches=true`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中央 U1 ITR9606 内部 LED、光箭头与光电晶体管符号

## 模拟电路

### 红外发射支路

VCC 经 R1 1KΩ 串联到 U1 红外 LED，LED 另一端接 GND；页面未显示发射使能、PWM 或开关晶体管。

- 参数与网络：`path=VCC -> R1 1KΩ -> U1 IR LED -> GND`；`enable=null`；`pwm=null`；`switch=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面 U1 左侧 VCC/R1/LED/GND 连续路径

### 光电晶体管输出

U1 光电晶体管的上端连接 MISO 输出节点、下端接 GND，因此晶体管导通时对输出节点提供下拉通路。

- 参数与网络：`collector_node=MISO output node`；`emitter_return=GND`；`conducting_action=pull output toward GND`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面 U1 右侧光电晶体管上端接输出横线、下端接 GND

### MISO 输出偏置

MISO 节点由 R3 10KΩ 上拉到 VCC，同时由 R2 20KΩ 下拉到 GND；在光电晶体管截止且外部高阻时，该电阻网络形成 VCC 到 GND 的分压。

- 参数与网络：`pull_up=R3 10KΩ to VCC`；`pull_down=R2 20KΩ to GND`；`unloaded_divider_ratio=20K/(10K+20K)=2/3 VCC`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面输出节点上方 R3 10KΩ 到 VCC、下方 R2 20KΩ 到 GND

### MISO 输出滤波

C4 100nF 从 MISO 输出节点接 GND，与 R2/R3 偏置网络共同形成输出低通滤波。

- 参数与网络：`capacitor=C4 100nF`；`node=MISO`；`return=GND`；`bias_resistors=R2 20KΩ,R3 10KΩ`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面输出节点-C4 100nF-GND，邻近 R2/R3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit OP180 系统架构 | `sensor=U1 ITR9606`；`emitter_bias=R1 1KΩ`；`receiver_bias=R3 10KΩ pull-up,R2 20KΩ pull-down`；`output_filter=C4 100nF`；`decoupling=C5 100nF`；`connector=J1 GROVE_IO` |
| 传感器 | U1 ITR9606 光电结构 | `emitter=infrared LED`；`receiver=phototransistor`；`electrical_isolation_between_branches=true` |
| 模拟电路 | 红外发射支路 | `path=VCC -> R1 1KΩ -> U1 IR LED -> GND`；`enable=null`；`pwm=null`；`switch=null` |
| 模拟电路 | 光电晶体管输出 | `collector_node=MISO output node`；`emitter_return=GND`；`conducting_action=pull output toward GND` |
| 模拟电路 | MISO 输出偏置 | `pull_up=R3 10KΩ to VCC`；`pull_down=R2 20KΩ to GND`；`unloaded_divider_ratio=20K/(10K+20K)=2/3 VCC` |
| 模拟电路 | MISO 输出滤波 | `capacitor=C4 100nF`；`node=MISO`；`return=GND`；`bias_resistors=R2 20KΩ,R3 10KΩ` |
| 接口 | J1 GROVE_IO 针脚 | `pin_1=MISO，数字/模拟检测输出`；`pin_2=NC`；`pin_3=VCC，电源输入`；`pin_4=GND` |
| GPIO 与控制信号 | 检测输出方向 | `output=J1 pin 1 MISO`；`direction=unit to host`；`unused=J1 pin 2`；`direction_control=null`；`interrupt=null`；`reset=null`；`boot=null`；`enable=null` |
| 电源 | VCC 电源路径 | `input=J1 pin 3 VCC`；`loads=R1,R3,C5`；`regulator=null`；`ldo=null`；`dc_dc=null`；`load_switch=null` |
| 电源 | VCC 去耦 | `capacitor=C5 100nF`；`rail=VCC`；`return=GND` |
| 电源 | 充电、电池与监测 | `charger=null`；`battery=null`；`power_good=null`；`monitor=null`；`enable=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`interface_current_limit=null`；`emitter_current_limit=R1 1KΩ` |
| 总线 | 外部总线 | `digital_output=MISO`；`spi=null`；`i2c=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 时钟 | 时钟、复位、调试与存储 | `clock=null`；`reset=null`；`debug=null`；`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 电源 | VCC 数值电压 | `net=VCC`；`schematic_voltage=null`；`candidate_from_product_doc=5V`；`allowed_range=null` |
| GPIO 与控制信号 | 遮挡状态与输出逻辑 | `transistor_on=MISO pulled toward GND`；`transistor_off=MISO biased by R3 10KΩ/R2 20KΩ`；`blocked_level=null`；`unblocked_level=null`；`host_threshold=null` |
| 传感器 | 检测几何与时序性能 | `angle=null`；`slot_width=null`；`distance=null`；`response_time=null`；`wavelength=null`；`ambient_light_immunity=null`；`temperature_range=null` |

## 待确认事项

- `power.vcc-voltage`：原理图仅使用 VCC 网络名，没有标注输入电压数值或允许范围，因此不能仅凭本页确认 J1 VCC 为 5V。（证据：图 dc417b1afd7c / 第 1 页 / 页面 J1 pin 3、R1/R3/C5 仅标 VCC，无电压数字）
- `gpio.blocked-state-logic`：电路可确认光电晶体管导通时下拉 MISO、截止时由 R2/R3 分压偏置，但原理图没有定义被遮挡/未遮挡分别对应高还是低，也没有给主机逻辑阈值。（证据：图 dc417b1afd7c / 第 1 页 / 页面 U1 光耦合符号与 MISO 偏置网络，无 BLOCK/UNBLOCK 或逻辑真值表）
- `sensor.detection-performance`：原理图未标注 180° 的机械含义、槽宽/检测距离、响应时间、发射波长、环境光抗扰度或工作温度范围。（证据：图 dc417b1afd7c / 第 1 页 / 整页仅 ITR9606 电路连接与阻容值，无机械或性能参数）
- `review.vcc-voltage`：Unit OP180 的 J1 VCC 额定输入电压和允许范围是什么？；原因：原理图仅标 VCC，需产品电气规范、BOM 或实测确认。
- `review.blocked-state-logic`：物体遮挡与未遮挡时，J1 pin 1 的稳定电压和主机读取逻辑分别是什么？；原因：图中没有遮挡状态真值表或主机输入阈值，且输出采用 10KΩ/20KΩ 分压偏置。
- `review.detection-performance`：180° 的具体结构定义、检测间距、响应时间和红外波长等参数是什么？；原因：这些机械/光学/时序参数未出现在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dc417b1afd7c43d6a5ab8846c96ad7d9edee711617c034f23e2d103ad748dc2a` | `https://static-cdn.m5stack.com/resource/docs/products/unit/OP180/img-14df8888-5109-4b25-a399-e6b236e85a50.webp` |

---

源文档：`zh_CN/unit/OP180.md`

源文档 SHA-256：`96bcfc2559c034bbbadd86d783c635dfefb0651b000124c58e6bb59089db0dfc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
