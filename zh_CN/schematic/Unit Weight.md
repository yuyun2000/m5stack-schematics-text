# Unit Weight 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Weight |
| SKU | U030 |
| 产品 ID | `unit-weight-b35adfabb254` |
| 源文档 | `zh_CN/unit/WEIGHT.md` |

## 概述

Unit Weight V1.0 以 U1 HX711 为唯一转换器，J2 Socket_3.96x4p 引出 E+/E-/A-/A+ 负载传感器接口，通道 A 的 INPA/INNA 接收差分信号，通道 B INPB/INNB 接地。Q1 SS8550 Y2 与 HX711 BASE/VFB、R3/R4 构成模拟供电调节路径，AVDD 向 J2 E+ 提供激励，AGND 连接 E-。J1 Header4 引出 DOUT、PD_SCK、VCC、GND，DOUT/PD_SCK 各由 4.7K 上拉至 VCC；RATE 接地，页面未显示外部主控、存储、外部晶振、电池或保护器件。正文中的 ADC 位数、增益、满量程与采样率需要 datasheet 或实测确认。

## 检索关键词

`Unit Weight`、`U030`、`HX711`、`SS8550 Y2`、`Socket_3.96x4p`、`E+`、`E-`、`A+`、`A-`、`INPA`、`INNA`、`INPB`、`INNB`、`DOUT`、`PD_SCK`、`RATE`、`AVDD`、`AGND`、`VFB`、`VBG`、`VSUP`、`DVDD`、`VCC`、`24bit ADC`、`PGA 128`、`PGA 64`、`10SPS`、`load cell`、`strain gauge`、`Grove CLK DAT`、`UNIT-WEIGHT V1.0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | HX711 | 负载传感器差分信号 ADC，使用通道 A，提供 DOUT/PD_SCK 数字接口和模拟电源控制 | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B2-C3，U1 HX711 pins1-16，VSUP/BASE/AVDD/VFB/AGND/VBG/INNA/INPA/INNB/INPB/DOUT/PD_SCK/XI/XO/RATE/DVDD |
| Q1 | SS8550 Y2 | 由 HX711 BASE 控制的外部模拟电源调节晶体管，VCC 侧向 AVDD 供电 | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B2，Q1 SS8550 Y2 与 VCC/U1 BASE/AVDD |
| J2 | Socket_3.96x4p | 四针负载传感器接口，提供 E+、E-、A-、A+ | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B1-C2，J2 Socket_3.96x4p pin4 E+、pin3 E-、pin2 A-、pin1 A+ |
| J1 | Header 4 | 四针主机接口，引出 DOUT、PD_SCK、VCC 与 GND | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B3-C3，J1 Header4 pin1 DOUT、pin2 PD_SCK、pin3 VCC、pin4 GND |
| R3,R4 | 20KΩ / 8.2KΩ | AVDD 到 AGND 的反馈分压，中心点连接 HX711 VFB | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B2-C2，AVDD-R3 20K-VFB-R4 8.2K-AGND |
| R1,R2 | 4.7KΩ / 4.7KΩ | DOUT 与 PD_SCK 分别上拉到 VCC | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B3，R1 4.7KΩ 上拉 DOUT、R2 4.7KΩ 上拉 PD_SCK |
| R5,C5 | 1KΩ / 100nF | A+ 到 INPA 的串联电阻与 INPA/INNA 差分滤波电容 | 图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 C1-C2，J2 A+/A-、R5 1KΩ、C5 100nF 与 U1 INPA/INNA |
| C1,C2,C3,C4 | 1uF / 1uF / 100nF / 1uF | VCC、AVDD、数字接口和 VBG 的去耦/滤波电容 | 图 c5e1e853e9fd / 第 1 页 / 第 1 页 C1 VCC、C2 AVDD、C3 VCC、C4 VBG 电容 |

## 系统结构

### Unit Weight 系统架构

U1 HX711 通过 J2 接收称重桥式传感器的 A+/A- 差分信号并提供 E+/E- 激励，通过 J1 的 DOUT/PD_SCK 与外部主机通信；Q1/R3/R4 构成 AVDD 调节路径。

- 参数与网络：`adc=U1 HX711`；`load_cell=J2 E+/E-/A-/A+`；`digital_interface=J1 DOUT/PD_SCK`；`analog_supply=Q1 SS8550 Y2 with R3/R4`；`power=VCC/DVDD/AVDD/AGND`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页完整 UNIT-WEIGHT V1.0 原理图

### 本页未包含的子系统

本页未显示 MCU、协处理器、存储、复位/BOOT、调试、I2C/SPI/UART/CAN/RS-485/USB、射频、音频、电池或充电电路；控制由 J1 外部主机承担。

- 参数与网络：`mcu=null`；`storage=null`；`reset_debug=null`；`standard_buses=null`；`rf=null`；`audio=null`；`battery_charger=null`；`external_host=J1 DOUT/PD_SCK`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页完整 UNIT-WEIGHT V1.0

## 电源

### HX711 AVDD 调节与桥式激励

VCC 连接 Q1 一端与 HX711 VSUP pin1，HX711 BASE pin2 控制 Q1，Q1 输出形成 AVDD；R3 20KΩ/R4 8.2KΩ 从 AVDD 到 AGND 分压，中心接 VFB pin4，AVDD 同时连接 J2 E+。

- 参数与网络：`input=VCC`；`transistor=Q1 SS8550 Y2`；`control=U1 pin2 BASE`；`output=AVDD`；`feedback=AVDD -> R3 20KΩ -> VFB pin4 -> R4 8.2KΩ -> AGND`；`excitation_positive=J2 E+=AVDD`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B2-C2，VCC/Q1/U1 BASE/AVDD/VFB/R3/R4/J2 E+

### HX711 数字与接口供电

U1 DVDD pin16 接 VCC，J1 pin3 接 VCC，C1 1uF 与 C3 100nF 分别从 VCC 接 GND；J1 pin4 接 GND。

- 参数与网络：`adc_digital=U1 pin16 DVDD=VCC`；`interface_power=J1 pin3=VCC`；`interface_ground=J1 pin4=GND`；`decoupling=C1 1uF,C3 100nF`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 DVDD/VCC、J1 pin3/4 与 C1/C3

## 接口

### J2 负载传感器针脚映射

J2 pin4=E+、pin3=E-、pin2=A-、pin1=A+；E+ 连接 AVDD，E- 连接 AGND，A- 连接 HX711 INNA pin7，A+ 经 R5 1KΩ 连接 INPA pin8。

- 参数与网络：`connector=J2 Socket_3.96x4p`；`pin4=E+ -> AVDD`；`pin3=E- -> AGND`；`pin2=A- -> U1 pin7 INNA`；`pin1=A+ -> R5 1KΩ -> U1 pin8 INPA`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B1-C2，J2 与 U1 AVDD/AGND/INNA/INPA

### J1 数据/时钟针脚

J1 pin1 连接 U1 DOUT pin12，pin2 连接 U1 PD_SCK pin11，pin3=VCC，pin4=GND；R1/R2 各 4.7KΩ 分别把 DOUT/PD_SCK 上拉到 VCC。

- 参数与网络：`pin1=DOUT/DAT from U1 pin12`；`pin2=PD_SCK/CLK to U1 pin11`；`pin3=VCC`；`pin4=GND`；`pullups=R1/R2 4.7KΩ to VCC`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 B3-C3，U1 DOUT/PD_SCK、R1/R2 与 J1

## 总线

### HX711 DOUT/PD_SCK 两线接口

U1 以 DOUT 输出数据/就绪状态，以 PD_SCK 接收时钟/控制，二者连接 J1；页面没有 I2C 地址、SDA/SCL、SPI CS 或寄存器总线。

- 参数与网络：`device=U1 HX711`；`data=DOUT pin12 -> J1 pin1`；`clock_control=PD_SCK pin11 <- J1 pin2`；`i2c_address=null`；`spi_chip_select=null`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 DOUT/PD_SCK 与 J1，无 I2C/SPI 总线标记

## 时钟

### RATE 与时钟配置

U1 RATE pin15 接 GND；页面未显示外部晶振、谐振器或有源时钟，XI/XO 位于接地侧网络。

- 参数与网络：`rate_pin=U1 pin15=GND`；`external_crystal=null`；`xi_xo_external_source=null`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 RATE/XI/XO 右侧网络，无外部时钟器件

## 保护电路

### 外部接口保护

J1 与 J2 外部连接路径未显示 TVS、专用 ESD 阵列、保险丝、反接或过压保护器件。

- 参数与网络：`tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 J1/J2 全部外部路径，无保护器件符号

## 模拟电路

### HX711 通道 A 输入

J2 A- 直接进入 U1 INNA pin7，J2 A+ 经 R5 1KΩ 进入 INPA pin8，C5 100nF 跨接 INNA/INPA 形成差分滤波。

- 参数与网络：`negative=J2 pin2 A- -> U1 pin7 INNA`；`positive=J2 pin1 A+ -> R5 1KΩ -> U1 pin8 INPA`；`filter=C5 100nF across INNA/INPA`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页网格 C1-C2，A+/A-/R5/C5/INPA/INNA

### HX711 通道 B 未使用

U1 INPB pin10 与 INNB pin9 在页面上共同接 GND，J2 没有通道 B 输入，因此本板只外接通道 A。

- 参数与网络：`inpb=U1 pin10=GND`；`innb=U1 pin9=GND`；`external_channel_b=null`；`used_channel=A`
- 证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 pins9/10 INNB/INPB 到 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Weight 系统架构 | `adc=U1 HX711`；`load_cell=J2 E+/E-/A-/A+`；`digital_interface=J1 DOUT/PD_SCK`；`analog_supply=Q1 SS8550 Y2 with R3/R4`；`power=VCC/DVDD/AVDD/AGND` |
| 接口 | J2 负载传感器针脚映射 | `connector=J2 Socket_3.96x4p`；`pin4=E+ -> AVDD`；`pin3=E- -> AGND`；`pin2=A- -> U1 pin7 INNA`；`pin1=A+ -> R5 1KΩ -> U1 pin8 INPA` |
| 模拟电路 | HX711 通道 A 输入 | `negative=J2 pin2 A- -> U1 pin7 INNA`；`positive=J2 pin1 A+ -> R5 1KΩ -> U1 pin8 INPA`；`filter=C5 100nF across INNA/INPA` |
| 模拟电路 | HX711 通道 B 未使用 | `inpb=U1 pin10=GND`；`innb=U1 pin9=GND`；`external_channel_b=null`；`used_channel=A` |
| 电源 | HX711 AVDD 调节与桥式激励 | `input=VCC`；`transistor=Q1 SS8550 Y2`；`control=U1 pin2 BASE`；`output=AVDD`；`feedback=AVDD -> R3 20KΩ -> VFB pin4 -> R4 8.2KΩ -> AGND`；`excitation_positive=J2 E+=AVDD` |
| 电源 | HX711 数字与接口供电 | `adc_digital=U1 pin16 DVDD=VCC`；`interface_power=J1 pin3=VCC`；`interface_ground=J1 pin4=GND`；`decoupling=C1 1uF,C3 100nF` |
| 接口 | J1 数据/时钟针脚 | `pin1=DOUT/DAT from U1 pin12`；`pin2=PD_SCK/CLK to U1 pin11`；`pin3=VCC`；`pin4=GND`；`pullups=R1/R2 4.7KΩ to VCC` |
| 总线 | HX711 DOUT/PD_SCK 两线接口 | `device=U1 HX711`；`data=DOUT pin12 -> J1 pin1`；`clock_control=PD_SCK pin11 <- J1 pin2`；`i2c_address=null`；`spi_chip_select=null` |
| 时钟 | RATE 与时钟配置 | `rate_pin=U1 pin15=GND`；`external_crystal=null`；`xi_xo_external_source=null` |
| 保护电路 | 外部接口保护 | `tvs=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null` |
| 系统结构 | 本页未包含的子系统 | `mcu=null`；`storage=null`；`reset_debug=null`；`standard_buses=null`；`rf=null`；`audio=null`；`battery_charger=null`；`external_host=J1 DOUT/PD_SCK` |
| 模拟电路 | 正文 ADC 位数、PGA 增益与满量程 | `documented_resolution=24bit`；`documented_gain_a=128 or 64`；`documented_full_scale=+/-20mV at 128; +/-40mV at 64`；`documented_gain_32=true`；`schematic_gain=null` |
| 其他事实 | 正文 10SPS 输出率 | `documented_rate=10SPS`；`rate_pin=GND`；`clock_frequency=null`；`rate_tolerance=null`；`filter_latency=null` |
| 电源 | 正文 Grove 5V 供电 | `documented_nominal=5V`；`schematic_rail=VCC`；`input_range=null`；`current=null`；`avdd_voltage=null`；`logic_thresholds=null` |
| 传感器 | 外部应变片量程与称重性能 | `connector=J2 E+/E-/A-/A+`；`included_load_cell=null`；`capacity=null`；`sensitivity=null`；`bridge_resistance=null`；`calibration=null`；`accuracy=null`；`temperature_drift=null` |

## 待确认事项

- `analog.documented-adc-gain-range`：正文称 HX711 为24位 ADC，通道 A 增益128/64分别对应±20mV/±40mV，并列出增益32；原理图只确认型号和通道连接，没有 ADC 位数、增益选择脉冲、参考条件或满量程文字。（证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 HX711 与通道 A/B，无 ADC 性能文字）
- `other.documented-output-rate`：正文称输出数据率为10SPS；原理图确认 RATE pin15 接 GND，但未标该电平对应的采样率、内部时钟频率、容差或滤波延迟。（证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 U1 RATE=GND，无 SPS 标注）
- `power.documented-input-voltage`：正文管脚表将 J1 电源标为5V；原理图仅使用 VCC 网络，没有标允许输入范围、工作/峰值电流、AVDD 实际电压或逻辑门限。（证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 J1/VCC/Q1/U1 电源路径，无电压额定值）
- `sensor.load-cell-performance`：原理图提供通用 E+/E-/A+/A- 接口但没有随板负载传感器；称重量程、灵敏度、桥阻、校准系数、零点漂移、噪声、精度和温度性能取决于外部传感器及系统标定。（证据：图 c5e1e853e9fd / 第 1 页 / 第 1 页 J2 为外部 Socket，无负载传感器符号或性能表）
- `review.adc-gain-range`：请用 HX711 datasheet 和驱动时序确认24位、A通道64/128、增益32适用通道及±20/±40mV条件。；原因：板级原理图未标 ADC/PGA 性能。
- `review.output-rate`：请确认 RATE=GND 时的10SPS、时钟源、数据就绪周期、滤波延迟和容差。；原因：原理图没有 RATE 电平到 SPS 的映射说明。
- `review.input-voltage`：请确认 J1 VCC 允许范围、典型/峰值电流、AVDD 激励电压和 DOUT/PD_SCK 逻辑门限。；原因：原理图只标 VCC。
- `review.load-cell-performance`：请针对目标应变片确认接线、量程、灵敏度、桥阻、校准、精度、漂移、噪声和机械安装要求。；原因：U030 不含可由本页确认的具体负载传感器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c5e1e853e9fd8c1c2648d68f60047f23c879ceba913a25eb27251c61d381248f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/704/U030-UNIT_WEIGHT-weight_page_01.png` |

---

源文档：`zh_CN/unit/WEIGHT.md`

源文档 SHA-256：`c83f8b6a6cf59fd9866ab58f8322a787d01e1241a7df3c54187da605b97ca852`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
