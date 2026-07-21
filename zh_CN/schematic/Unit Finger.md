# Unit Finger 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Finger |
| SKU | U008 |
| 产品 ID | `unit-finger-cb97ff2ea398` |
| 源文档 | `zh_CN/unit/finger.md` |

## 概述

Unit Finger 原理图由 P1 Finger 六针指纹传感器连接器、U1 HT7533 稳压器和 J1 Grove C 四针接口构成。J1 输入 +5V，经 U1 转换为 +3.3V 供 P1，输入输出两侧均配置 10 uF 与 100 nF 电容。P1 标出 TX、RX 串口网络，而 J1 标出 I、O 信号端，但本页未画出两组信号之间的可见连接。

## 检索关键词

`Unit Finger`、`U008`、`Finger Sensor`、`FPC1020A`、`P1 Finger`、`HT7533`、`GROVE C`、`J1 Grove`、`UART`、`UART_RX`、`UART_TX`、`TX`、`RX`、`I`、`O`、`19200bps`、`9600-115200`、`+5V`、`+3.3V`、`VCC`、`P1 pin 3`、`P1 pin 4`、`P1 pin 5`、`P1 pin 6`、`J1 pin 1`、`J1 pin 2`、`J1 pin 3`、`J1 pin 4`、`C1 100nF`、`C2 10uF`、`C3 10uF`、`C4 100nF`、`150 fingerprints`、`193Byte`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Finger | 六针指纹传感器模组连接器 | 图 d0f0f80b9729 / 第 1 页 / 页 1 左侧 Finger Sensor 方框内的 P1 六针连接器，器件值标注 Finger |
| U1 | HT7533 | +5V 至 +3.3V 线性稳压器 | 图 d0f0f80b9729 / 第 1 页 / 页 1 中央 U1，标注 HT7533，VIN/VOUT 分别连接 +5V/+3.3V |
| J1 | Grove | Grove C 电源与串口信号接口 | 图 d0f0f80b9729 / 第 1 页 / 页 1 右侧 GROVE C 区域的 J1，器件值标注 Grove，端子标注 I、O、VCC、GND |

## 系统结构

### Unit Finger 电路结构

本页电路包含 P1 Finger 指纹传感器连接器、U1 HT7533 稳压器和 J1 Grove 接口；J1 侧 +5V 经 U1 生成 P1 侧 +3.3V。

- 参数与网络：`sensor_connector=P1 Finger`；`regulator=U1 HT7533`；`host_connector=J1 Grove`；`input_rail=+5V`；`sensor_rail=+3.3V`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 全图，从左侧 P1 经中央 U1 至右侧 J1 的完整电路

## 电源

### U1 电源转换

U1 HT7533 的 VIN 引脚 2 接 +5V，VOUT 引脚 3 输出 +3.3V，GND 引脚 1 接地。

- 参数与网络：`reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 中央 U1 HT7533，VIN/VOUT/GND 引脚号与 +5V/+3.3V/GND 网络

### +5V 输入去耦

C3 10 uF 与 C4 100 nF 并联在 U1 的 +5V 输入网络和 GND 之间。

- 参数与网络：`rail=+5V`；`capacitors=C3 10uF,C4 100nF`；`return_net=GND`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 中右部 U1 VIN 与 J1 之间的 C3、C4 及 +5V/GND 网络

### +3.3V 输出去耦

C1 100 nF 与 C2 10 uF 并联在 U1 的 +3.3V 输出网络和 GND 之间。

- 参数与网络：`rail=+3.3V`；`capacitors=C1 100nF,C2 10uF`；`return_net=GND`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 中左部 P1 与 U1 VOUT 之间的 C1、C2 及 +3.3V/GND 网络

### P1 指纹传感器供电

P1 的 3 脚由 U1 VOUT 所在的 +3.3V 网络供电，P1 的 6 脚连接 GND。

- 参数与网络：`supply_pin=P1 pin 3`；`supply_rail=+3.3V`；`ground_pin=P1 pin 6`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 左侧 P1 第 3、6 脚与 +3.3V、GND 连线

### J1 Grove 输入供电

J1 的 VCC 第 3 脚连接 +5V 输入网络，GND 第 4 脚连接 GND。

- 参数与网络：`supply_pin=J1 pin 3/VCC`；`supply_rail=+5V`；`ground_pin=J1 pin 4/GND`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 右侧 J1 第 3、4 脚与 +5V、GND 网络

## 接口

### P1 Finger 连接器

P1 的 3 脚连接 +3.3V，4 脚连接 TX，5 脚连接 RX，6 脚连接 GND；1、2 脚在本页没有网络名。

- 参数与网络：`reference=P1`；`visible_pinout=3:+3.3V,4:TX,5:RX,6:GND`；`pin_1_network=null`；`pin_2_network=null`；`signal_direction=TX output from sensor side,RX input to sensor side`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 左侧 P1 的 1 至 6 脚及 +3.3V、TX、RX、GND 网络

### J1 Grove C 接口

J1 的 1 至 4 脚在器件内依次标注 I、O、VCC、GND；3 脚连接 +5V，4 脚连接 GND，1、2 脚的外部线段在本页没有网络名。

- 参数与网络：`reference=J1`；`pin_labels=1:I,2:O,3:VCC,4:GND`；`visible_power_pinout=3:+5V,4:GND`；`pin_1_external_net=null`；`pin_2_external_net=null`；`direction=I input to unit,O output from unit`
- 证据：图 d0f0f80b9729 / 第 1 页 / 页 1 右侧 J1 Grove，1 至 4 脚、I/O/VCC/GND 文字及 +5V/GND 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Finger 电路结构 | `sensor_connector=P1 Finger`；`regulator=U1 HT7533`；`host_connector=J1 Grove`；`input_rail=+5V`；`sensor_rail=+3.3V` |
| 核心器件 | P1 所接指纹传感器型号 | `reference=P1`；`schematic_label=Finger`；`documented_module=FPC1020A`；`schematic_part_number=null` |
| 接口 | P1 Finger 连接器 | `reference=P1`；`visible_pinout=3:+3.3V,4:TX,5:RX,6:GND`；`pin_1_network=null`；`pin_2_network=null`；`signal_direction=TX output from sensor side,RX input to sensor side` |
| 接口 | J1 Grove C 接口 | `reference=J1`；`pin_labels=1:I,2:O,3:VCC,4:GND`；`visible_power_pinout=3:+5V,4:GND`；`pin_1_external_net=null`；`pin_2_external_net=null`；`direction=I input to unit,O output from unit` |
| 总线 | P1 与 J1 的 UART 信号路径 | `bus=UART`；`sensor_signals=P1 pin 4 TX,P1 pin 5 RX`；`host_signals=J1 pin 1 I,J1 pin 2 O`；`tx_rx_to_io_mapping=null` |
| 总线 | UART 通信参数 | `documented_default_baud=19200`；`documented_baud_range=9600-115200`；`start_bits=1`；`stop_bits=1`；`parity=none`；`schematic_uart_parameters=null` |
| 电源 | U1 电源转换 | `reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1` |
| 电源 | +5V 输入去耦 | `rail=+5V`；`capacitors=C3 10uF,C4 100nF`；`return_net=GND` |
| 电源 | +3.3V 输出去耦 | `rail=+3.3V`；`capacitors=C1 100nF,C2 10uF`；`return_net=GND` |
| 电源 | P1 指纹传感器供电 | `supply_pin=P1 pin 3`；`supply_rail=+3.3V`；`ground_pin=P1 pin 6` |
| 电源 | J1 Grove 输入供电 | `supply_pin=J1 pin 3/VCC`；`supply_rail=+5V`；`ground_pin=J1 pin 4/GND` |
| 传感器 | 指纹识别能力 | `documented_sensor_type=capacitive fingerprint`；`documented_matching=1:N and 1:1`；`documented_rotation_degrees=360`；`schematic_capabilities=null` |
| 存储 | 指纹模板容量与特征值 | `documented_fingerprint_capacity=150`；`documented_feature_size_bytes=193`；`schematic_storage_device=null`；`schematic_capacity=null` |

## 待确认事项

- `component.sensor_model`：产品正文将内部指纹识别模组称为 FPC1020A，但原理图仅把 P1 标为 Finger，未打印 FPC1020A 型号。（证据：图 d0f0f80b9729 / 第 1 页 / 页 1 左侧 P1 下方仅标注 Finger，页面无 FPC1020A 字样）
- `bus.uart_path`：产品正文描述通过 UART 通信；原理图在 P1 标出 TX、RX，在 J1 标出 I、O，但本页没有可见连线或同名网络标签证明 TX/RX 与 I/O 的对应关系。（证据：图 d0f0f80b9729 / 第 1 页 / 页 1 全图，P1 TX/RX 线段与 J1 I/O 线段均终止且未共享网络标签）
- `bus.uart_parameters`：产品正文给出默认 19200 bps、1 个起始位、1 个停止位、无校验，并列出 9600 至 115200 的通信范围；这些参数未标注在原理图中。（证据：图 d0f0f80b9729 / 第 1 页 / 页 1 P1 TX/RX 与 J1 I/O 区域未出现波特率、帧格式或时钟参数）
- `sensor.capabilities`：产品正文描述电容式指纹采集、1:N 识别、1:1 验证和 360 度旋转识别；本页原理图只显示 Finger Sensor 连接器，未提供这些能力的电路级标注。（证据：图 d0f0f80b9729 / 第 1 页 / 页 1 左侧仅有 Finger Sensor 框与 P1 连接器，无传感器内部功能框图）
- `storage.fingerprint_capacity`：产品正文标注指纹容量 150、特征值大小 193 Byte，但本页原理图没有存储器器件或容量标注。（证据：图 d0f0f80b9729 / 第 1 页 / 页 1 全图未显示独立存储器或 Finger Sensor 内部存储结构）
- `review.sensor_model`：P1 所接实际指纹模组的完整型号和硬件版本是否为 FPC1020A？；原因：原理图仅标注 Finger，没有打印 FPC1020A 或模组版本。
- `review.uart_path`：J1 pin 1 I、pin 2 O 与 P1 TX、RX 的实际 PCB 网络对应关系是什么？；原因：本页图像没有显示两组信号之间的连线或共享网络标签。
- `review.uart_parameters`：当前模组固件的默认波特率和支持范围是否仍为正文所列 19200 bps 与 9600-115200？；原因：UART 参数属于模组固件配置，原理图没有相关标注。
- `review.sensor_capabilities`：电容式采集、1:N、1:1 和 360 度识别能力对应的具体模组版本与固件条件是什么？；原因：原理图没有传感器内部框图或功能参数。
- `review.fingerprint_capacity`：150 枚指纹容量和 193 Byte 特征值大小由哪一版模组固件或内部存储实现？；原因：原理图未显示存储器型号、容量或模组内部存储结构。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d0f0f80b97290d3eb2bbcc2d4aff6b11f30a52d324f2789cff8b109c94aca2c3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/U008_sche.png` |

---

源文档：`zh_CN/unit/finger.md`

源文档 SHA-256：`c406924d1b2fe52ef1506849dc511d0f184bc58aac25b61ce42c72a05f4e9851`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
