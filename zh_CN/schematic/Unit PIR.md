# Unit PIR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PIR |
| SKU | U004 |
| 产品 ID | `unit-pir-4c2bd1465db8` |
| 源文档 | `zh_CN/unit/PIR.md` |

## 概述

Unit PIR（U004）以 U1 PIR_AS312 被动红外传感模组为核心，U2 HT7533 将 J1 输入的 VCC 转换为 3.3V 供给 U1。U1 OUT pin 2 经 R1 1KΩ 串联形成 out 网络并连接 J1 pin 1；J1 pin 2 未连接，pin 3/4 为 VCC/GND。VCC 输入由 C1 100nF 和 C4 10uF 去耦，3.3V 输出由 C2 100nF 和 C3 10uF 去耦。原理图未给输入电压数值、运动触发逻辑、延时/重复触发模式或检测距离与角度。

## 检索关键词

`Unit PIR`、`U004`、`PIR`、`PIR_AS312`、`AS312`、`U1`、`HT7533`、`U2`、`J1 Grove`、`Digital Output`、`out`、`VCC`、`3.3V`、`GND`、`R1 1KΩ`、`C1 100nF`、`C2 100nF`、`C3 10uF`、`C4 10uF`、`pin 1 output`、`pin 2 NC`、`pin 3 VCC`、`pin 4 GND`、`被动红外`、`人体运动检测`、`2秒延时`、`可重复触发`、`500cm`、`100度`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PIR_AS312 | 三针被动红外运动传感模组，使用 3.3V 供电并输出数字检测信号 | 图 027b8ee27738 / 第 1 页 / 页面 C1:C2 U1 PIR_AS312，pin 1 VCC、pin 2 OUT、pin 3 GND |
| U2 | HT7533 | 把 J1 VCC 输入转换为 3.3V 的三端稳压器 | 图 027b8ee27738 / 第 1 页 / 页面 C2 U2 HT7533，pin 2 VIN 接 VCC、pin 3 VOUT 接 3.3V、pin 1 GND |
| J1 | Grove | 四针数字输出与电源接口 | 图 027b8ee27738 / 第 1 页 / 页面 C3 J1 Grove，pin 1 I/out、pin 2 O/NC、pin 3 VCC、pin 4 GND |
| R1 | 1KΩ | U1 OUT 与 J1 pin 1 之间的串联输出电阻 | 图 027b8ee27738 / 第 1 页 / 页面 U1 pin 2 OUT-R1 1KΩ-out-J1 pin 1 |
| C1 | 100nF | J1 VCC 输入轨的高频去耦电容 | 图 027b8ee27738 / 第 1 页 / 页面 J1 右侧 VCC-C1 100nF-GND |
| C4 | 10uF | HT7533 VIN/VCC 输入侧储能电容 | 图 027b8ee27738 / 第 1 页 / 页面 U2 VIN/VCC 节点-C4 10uF-GND |
| C2/C3 | 100nF/10uF | HT7533 3.3V 输出侧并联去耦与储能电容 | 图 027b8ee27738 / 第 1 页 / 页面 U2 VOUT/3.3V 节点-C2 100nF/C3 10uF-GND |

## 系统结构

### Unit PIR 系统架构

电路由 U1 PIR_AS312 传感模组、U2 HT7533 3.3V 稳压器、J1 Grove、R1 输出串联电阻和 C1~C4 电源电容组成。

- 参数与网络：`sensor=U1 PIR_AS312`；`regulator=U2 HT7533`；`connector=J1 Grove`；`output_series=R1 1KΩ`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 C1:C3 区域完整 U1/U2/J1/R1/C1~C4 电路

## 电源

### VCC 输入路径

J1 pin 3 VCC 直接连接 U2 VIN pin 2，并通过 C1 100nF 与 C4 10uF 对地去耦。

- 参数与网络：`connector=J1 pin 3 VCC`；`regulator_input=U2 pin 2 VIN`；`capacitors=C1 100nF,C4 10uF`；`return=GND`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 C2:C3 U2 VIN/VCC、J1 VCC 与 C1/C4

### VCC 到 3.3V 稳压

U2 HT7533 pin 2 VIN 接 VCC，pin 3 VOUT 输出 3.3V，pin 1 GND 接地；3.3V 供给 U1 pin 1。

- 参数与网络：`input=U2 pin 2 VIN VCC`；`output=U2 pin 3 VOUT 3.3V`；`ground=U2 pin 1 GND`；`load=U1 pin 1 VCC`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U2 HT7533 与 3.3V/VCC/GND，U1 VCC 接 3.3V

### 3.3V 输出去耦

U2 VOUT 的 3.3V 电源轨通过 C2 100nF 和 C3 10uF 并联接地。

- 参数与网络：`rail=3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U2 VOUT/3.3V 旁 C2/C3 到 GND

### 电源控制、充电与监测

本页未显示稳压器使能、负载开关、充电器、电池连接、电源良好信号或电压/电流监测器。

- 参数与网络：`enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页电源部分仅 U2 VIN/VOUT/GND 与 C1~C4

## 接口

### J1 Grove 针脚

J1 pin 1 标注 I 并连接 out，pin 2 标注 O 且以未连接标记结束，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`pin_1=I-out，传感器到主机输出`；`pin_2=O-NC`；`pin_3=VCC，电源输入`；`pin_4=GND`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 C3 J1 Grove pins 1~4 与 out/NC/VCC/GND

## 总线

### 外部总线

本页只有单路 out 数字信号，未显示 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`digital_output=out`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页外部 J1 仅 out/VCC/GND，pin 2 NC

## GPIO 与控制信号

### PIR 数字输出路径

U1 OUT pin 2 经 R1 1KΩ 串联后形成 out 网络并连接 J1 pin 1；信号方向为传感模组到外部主机。

- 参数与网络：`source=U1 pin 2 OUT`；`series=R1 1KΩ`；`net=out`；`destination=J1 pin 1 I`；`direction=unit to host`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U1 OUT-R1-out 与 J1 pin 1 同名网络

## 时钟

### 时钟、复位与调试

本页未显示晶振/时钟、RESET、BOOT、EN、中断或调试接口。

- 参数与网络：`clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页全部器件与网络，无时钟/控制/调试信号

## 保护电路

### 接口与电源保护

J1 的 out 和 VCC 路径未显示 TVS/ESD、保险丝、反接、过压或浪涌保护器件；R1 是输出串联电阻。

- 参数与网络：`output_series=R1 1KΩ`；`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`surge=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 J1 到 U1/U2 的完整信号和电源路径，无保护器件位号

## 存储

### 存储器与内存

本页未显示主控、Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页仅 U1 PIR 模组、U2 稳压器、J1、R1 和 C1~C4

## 传感器

### U1 PIR_AS312 引脚

U1 pin 1 VCC 接 3.3V，pin 2 OUT 经 R1 接 out，pin 3 GND 接地。

- 参数与网络：`pin_1=VCC 3.3V`；`pin_2=OUT -> R1 1KΩ -> out`；`pin_3=GND`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 C1 U1 PIR_AS312 pins 1~3 与 3.3V/out/GND 网络

## 模拟电路

### 输出调理

输出线上只有 R1 1KΩ 串联电阻，页面未显示外部上拉、下拉、RC 滤波、比较器、电平转换或输出缓冲器。

- 参数与网络：`series_resistor=R1 1KΩ`；`pullup=null`；`pulldown=null`；`filter=null`；`comparator=null`；`level_shifter=null`；`buffer=null`
- 证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U1 OUT 到 J1 pin 1 的完整路径仅含 R1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PIR 系统架构 | `sensor=U1 PIR_AS312`；`regulator=U2 HT7533`；`connector=J1 Grove`；`output_series=R1 1KΩ`；`input_caps=C1 100nF,C4 10uF`；`output_caps=C2 100nF,C3 10uF` |
| 传感器 | U1 PIR_AS312 引脚 | `pin_1=VCC 3.3V`；`pin_2=OUT -> R1 1KΩ -> out`；`pin_3=GND` |
| 接口 | J1 Grove 针脚 | `pin_1=I-out，传感器到主机输出`；`pin_2=O-NC`；`pin_3=VCC，电源输入`；`pin_4=GND` |
| GPIO 与控制信号 | PIR 数字输出路径 | `source=U1 pin 2 OUT`；`series=R1 1KΩ`；`net=out`；`destination=J1 pin 1 I`；`direction=unit to host` |
| 模拟电路 | 输出调理 | `series_resistor=R1 1KΩ`；`pullup=null`；`pulldown=null`；`filter=null`；`comparator=null`；`level_shifter=null`；`buffer=null` |
| 电源 | VCC 输入路径 | `connector=J1 pin 3 VCC`；`regulator_input=U2 pin 2 VIN`；`capacitors=C1 100nF,C4 10uF`；`return=GND` |
| 电源 | VCC 到 3.3V 稳压 | `input=U2 pin 2 VIN VCC`；`output=U2 pin 3 VOUT 3.3V`；`ground=U2 pin 1 GND`；`load=U1 pin 1 VCC` |
| 电源 | 3.3V 输出去耦 | `rail=3.3V`；`capacitors=C2 100nF,C3 10uF`；`return=GND` |
| 电源 | 电源控制、充电与监测 | `enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`power_good=null`；`monitor=null` |
| 保护电路 | 接口与电源保护 | `output_series=R1 1KΩ`；`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`surge=null` |
| 总线 | 外部总线 | `digital_output=out`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 时钟 | 时钟、复位与调试 | `clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null` |
| 存储 | 存储器与内存 | `controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 电源 | J1 VCC 数值 | `net=VCC`；`schematic_voltage=null`；`candidate_from_product_doc=5V`；`allowed_range=null` |
| GPIO 与控制信号 | 运动检测输出逻辑 | `motion_level=null`；`idle_level=null`；`high_voltage=null`；`low_voltage=null`；`output_structure=null`；`host_threshold=null` |
| 传感器 | 触发延时与重复触发 | `hold_time=null`；`delay=null`；`retriggerable=null`；`retrigger_condition=null`；`candidate_from_product_doc=2 seconds,retriggerable` |
| 传感器 | PIR 检测性能 | `distance=null`；`field_of_view=null`；`quiescent_current=null`；`temperature_range=null`；`response_time=null`；`lens=null`；`wavelength=null` |

## 待确认事项

- `power.vcc-voltage`：原理图仅标 VCC，没有给 J1 输入电压数值或允许范围，因此不能仅凭本页确认 VCC 为 5V。（证据：图 027b8ee27738 / 第 1 页 / 第 1 页 J1 pin 3 与 U2 VIN 仅标 VCC，无电压数字）
- `gpio.motion-output-logic`：原理图确认 U1 OUT 经 R1 输出，但没有说明检测到运动与无运动时 out 的高低电平、电压值、输出结构或主机阈值。（证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U1 OUT-R1-out-J1，没有逻辑真值表或电平参数）
- `sensor.trigger-timing`：本页未标注触发保持时间、延时电路、可重复触发模式或重触发条件，不能仅凭原理图确认固定 2 秒行为。（证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U1 PIR_AS312 仅显示 VCC/OUT/GND，无定时/模式引脚或参数）
- `sensor.detection-performance`：原理图未标注检测距离、视场角、静态电流、工作温度、响应时间、透镜型号或红外波段。（证据：图 027b8ee27738 / 第 1 页 / 第 1 页 U1 PIR_AS312 模组符号与外围连接，无性能参数）
- `review.vcc-voltage`：Unit PIR 的 J1 VCC 额定输入电压和允许范围是什么？；原因：原理图只标 VCC；需电气规格、HT7533 输入条件或实测确认。
- `review.motion-output-logic`：运动与静止状态下 out 的逻辑、电压和输出结构分别是什么？；原因：图中只有 U1 OUT 引脚与串联电阻，没有逻辑真值表或电平规范。
- `review.trigger-timing`：触发保持时间是否固定为 2 秒，重复触发的延时刷新规则是什么？；原因：这些行为由 PIR_AS312 内部实现决定，原理图没有定时或模式参数。
- `review.detection-performance`：该版本的检测距离、视场角、静态电流、温度范围和透镜型号是什么？；原因：机械、光学和性能参数未在原理图中标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `027b8ee2773884eb95e20171afbcc165f0e7e871941f6f949804b65a04a1beec` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/701/UNIT_PIR_page_01.png` |

---

源文档：`zh_CN/unit/PIR.md`

源文档 SHA-256：`c0bc4666dce8e29b6250a102d211974b119f5a5454428eadc323941c809a4a08`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
