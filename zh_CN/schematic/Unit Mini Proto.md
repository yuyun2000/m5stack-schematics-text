# Unit Mini Proto 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini Proto |
| SKU | U064 |
| 产品 ID | `unit-mini-proto-eb1e36d8926b` |
| 源文档 | `zh_CN/unit/mini-proto.md` |

## 概述

Unit Mini Proto（U064）原理图是 P1 Header 4 与 J1 GROVE_IO 之间的四线无源直连。两路信号分别连接 P1 pin 1 到 J1 pin 1（I/MISO）以及 P1 pin 2 到 J1 pin 2（O/IO），P1/J1 pin 3 共用 VCC，pin 4 共用 GND。页面未显示主控、协处理器、存储器、电源转换、保护、时钟或复位器件；VCC 电压和两路信号的实际方向需由外接电路确定。

## 检索关键词

`Unit Mini Proto`、`U064`、`Mini Proto`、`P1`、`Header 4`、`J1`、`GROVE_IO`、`HY2.0-4P`、`MISO`、`IO`、`I`、`O`、`VCC`、`GND`、`P1 pin 1`、`P1 pin 2`、`P1 pin 3`、`P1 pin 4`、`J1 pin 1 MISO`、`J1 pin 2 IO`、`J1 pin 3 VCC`、`J1 pin 4 GND`、`无源直连`、`原型板`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 4 | 四针内部排针/焊接接口，逐针引出 I、O、VCC 和 GND | 图 30f934ab0454 / 第 1 页 / 页面左侧 P1 Header 4，pins 1~4 分别连接 I、O、VCC、GND |
| J1 | GROVE_IO | 四针外部 Grove 接口，针脚标注 MISO、IO、VCC 和 GND | 图 30f934ab0454 / 第 1 页 / 页面右侧 J1 GROVE_IO，pins 1~4 标注 MISO、IO、VCC、GND |

## 系统结构

### Unit Mini Proto 架构

原理图由 P1 Header 4 和 J1 GROVE_IO 两个四针连接器组成，四个对应针脚均为直接网络连接，页面内没有有源功能分区。

- 参数与网络：`internal_connector=P1 Header 4`；`external_connector=J1 GROVE_IO`；`connection_type=pin-to-pin passive breakout`；`active_devices=null`
- 证据：图 30f934ab0454 / 第 1 页 / 整页仅含 P1、J1、I/O/VCC/GND 直连网络和地符号

### 有源功能分区

本页未显示主控、协处理器、传感器、音频、射频、模拟采样或其他有源 IC/模块。

- 参数与网络：`controller=null`；`coprocessor=null`；`sensor=null`；`audio=null`；`rf=null`；`analog_frontend=null`
- 证据：图 30f934ab0454 / 第 1 页 / 整页仅见 P1 Header 4、J1 GROVE_IO、导线、电源符号和地符号

## 核心器件

### 连接器组成

P1 的型号文字为 Header 4，J1 的型号文字为 GROVE_IO；两者均编号为 1~4。

- 参数与网络：`P1=Header 4,pins 1-4`；`J1=GROVE_IO,pins 1-4`
- 证据：图 30f934ab0454 / 第 1 页 / 页面左侧 P1 Header 4 与右侧 J1 GROVE_IO 的位号、型号文字和针号

## 电源

### VCC 电源网络

P1 pin 3 与 J1 pin 3 通过同名 VCC 电源网络直连，本页没有稳压器、LDO、转换器、负载开关、充电、电池或电源监测路径。

- 参数与网络：`internal_pin=P1 pin 3`；`external_pin=J1 pin 3`；`net=VCC`；`regulator=null`；`load_switch=null`；`battery_charger=null`；`monitor=null`
- 证据：图 30f934ab0454 / 第 1 页 / 页面中部 P1 pin 3 与 J1 pin 3 的 VCC 同名电源符号；整页无其他电源器件

### GND 回流网络

P1 pin 4 和 J1 pin 4 均连接 GND 地符号，形成共同地网络。

- 参数与网络：`internal_pin=P1 pin 4`；`external_pin=J1 pin 4`；`net=GND`
- 证据：图 30f934ab0454 / 第 1 页 / 页面下方 P1 pin 4 与 J1 pin 4 各自连接同名 GND 地符号

## 接口

### P1 Header 4 针脚

P1 pins 1~4 依次连接网络 I、O、VCC、GND。

- 参数与网络：`pin_1=I`；`pin_2=O`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 30f934ab0454 / 第 1 页 / 页面左侧 P1 pins 1/2 的 I/O 网络文字、pin 3 VCC 电源符号、pin 4 GND 符号

### J1 GROVE_IO 针脚

J1 pins 1~4 依次标注 MISO、IO、VCC、GND，并分别直连 P1 pins 1~4。

- 参数与网络：`pin_1=MISO,I,P1 pin 1`；`pin_2=IO,O,P1 pin 2`；`pin_3=VCC,P1 pin 3`；`pin_4=GND,P1 pin 4`
- 证据：图 30f934ab0454 / 第 1 页 / 页面右侧 J1 pins 1~4 的 MISO/IO/VCC/GND 标注及到 P1 的横向连线

## 总线地址

### 总线地址

原理图没有带地址的设备，也未标注任何 I2C 地址、芯片选择地址或可配置地址。

- 参数与网络：`addressed_device=null`；`i2c_address=null`；`chip_select=null`
- 证据：图 30f934ab0454 / 第 1 页 / 整页仅有两个无源连接器与四条直连网络，无设备地址标注

## 时钟

### 时钟、复位与存储

本页没有晶振或时钟网络、RESET/EN/BOOT 网络、调试接口，也没有 Flash、EEPROM、SD 卡或其他存储器连接。

- 参数与网络：`clock=null`；`reset=null`；`enable=null`；`boot=null`；`debug=null`；`storage=null`
- 证据：图 30f934ab0454 / 第 1 页 / 整页 P1/J1 四线无源网络，无时钟、控制、调试或存储器件/网络

## 保护电路

### 板载保护

原理图在 I、O、VCC 和 GND 四条通道上均未显示 ESD/TVS、保险丝、限流、反接或过压保护器件。

- 参数与网络：`esd_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 30f934ab0454 / 第 1 页 / 整页 P1-J1 四条直接连接，无任何中间器件符号或保护器件位号

## 关键网络

### I/MISO 信号通道

P1 pin 1 与 J1 pin 1 直接相连，连线上标注 I，J1 pin 1 功能文字为 MISO，中间没有串联、上拉、下拉或保护器件。

- 参数与网络：`from=P1 pin 1`；`net=I`；`to=J1 pin 1 MISO`；`series_component=null`；`pull=null`；`protection=null`
- 证据：图 30f934ab0454 / 第 1 页 / 页面上方 P1 pin 1-I-J1 pin 1 MISO 的连续横线

### O/IO 信号通道

P1 pin 2 与 J1 pin 2 直接相连，连线上标注 O，J1 pin 2 功能文字为 IO，中间没有串联、上拉、下拉或保护器件。

- 参数与网络：`from=P1 pin 2`；`net=O`；`to=J1 pin 2 IO`；`series_component=null`；`pull=null`；`protection=null`
- 证据：图 30f934ab0454 / 第 1 页 / 页面中上 P1 pin 2-O-J1 pin 2 IO 的连续横线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini Proto 架构 | `internal_connector=P1 Header 4`；`external_connector=J1 GROVE_IO`；`connection_type=pin-to-pin passive breakout`；`active_devices=null` |
| 核心器件 | 连接器组成 | `P1=Header 4,pins 1-4`；`J1=GROVE_IO,pins 1-4` |
| 接口 | P1 Header 4 针脚 | `pin_1=I`；`pin_2=O`；`pin_3=VCC`；`pin_4=GND` |
| 接口 | J1 GROVE_IO 针脚 | `pin_1=MISO,I,P1 pin 1`；`pin_2=IO,O,P1 pin 2`；`pin_3=VCC,P1 pin 3`；`pin_4=GND,P1 pin 4` |
| 关键网络 | I/MISO 信号通道 | `from=P1 pin 1`；`net=I`；`to=J1 pin 1 MISO`；`series_component=null`；`pull=null`；`protection=null` |
| 关键网络 | O/IO 信号通道 | `from=P1 pin 2`；`net=O`；`to=J1 pin 2 IO`；`series_component=null`；`pull=null`；`protection=null` |
| 电源 | VCC 电源网络 | `internal_pin=P1 pin 3`；`external_pin=J1 pin 3`；`net=VCC`；`regulator=null`；`load_switch=null`；`battery_charger=null`；`monitor=null` |
| 电源 | GND 回流网络 | `internal_pin=P1 pin 4`；`external_pin=J1 pin 4`；`net=GND` |
| 保护电路 | 板载保护 | `esd_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null` |
| 系统结构 | 有源功能分区 | `controller=null`；`coprocessor=null`；`sensor=null`；`audio=null`；`rf=null`；`analog_frontend=null` |
| 时钟 | 时钟、复位与存储 | `clock=null`；`reset=null`；`enable=null`；`boot=null`；`debug=null`；`storage=null` |
| 总线地址 | 总线地址 | `addressed_device=null`；`i2c_address=null`；`chip_select=null` |
| 电源 | VCC 电压 | `net=VCC`；`voltage=null`；`allowed_range=null`；`current_rating=null` |
| GPIO 与控制信号 | I/O 信号方向 | `signal_1=P1 pin 1 I-J1 pin 1 MISO`；`signal_2=P1 pin 2 O-J1 pin 2 IO`；`direction_control=null`；`reference_side=null` |
| 总线 | MISO 与总线协议 | `visible_signal=J1 pin 1 MISO`；`mosi=null`；`sck=null`；`cs=null`；`spi_confirmed=false`；`i2c_confirmed=false`；`uart_confirmed=false` |

## 待确认事项

- `power.vcc-voltage`：P1 pin 3 和 J1 pin 3 只标注 VCC，原理图未给出该电源轨的数值电压、允许范围或电流能力。（证据：图 30f934ab0454 / 第 1 页 / 页面中部 P1 pin 3 与 J1 pin 3 之间仅有 VCC 标签，无电压数值）
- `gpio.signal-direction`：图中把 P1 pin 1 网络标为 I、J1 pin 1 标为 MISO，把 P1 pin 2 网络标为 O、J1 pin 2 标为 IO；由于电路是无源直连且没有方向器件，I/O 相对于主机还是原型电路的准确方向定义无法仅凭本页确定。（证据：图 30f934ab0454 / 第 1 页 / 页面上方两条信号线的 I/O 网络文字与 J1 MISO/IO 功能文字，无方向箭头或驱动器）
- `bus.miso-protocol`：J1 pin 1 使用 MISO 名称，但本页没有 MOSI、SCK、CS 或控制器/设备信息，因此不能仅凭该名称确认这两根信号构成完整 SPI，也无法确认 I2C、UART 或其他协议。（证据：图 30f934ab0454 / 第 1 页 / 页面右侧 J1 pin 1 MISO、pin 2 IO；整页无 MOSI/SCK/CS/SCL/SDA/TX/RX 标注）
- `review.vcc-voltage`：Unit Mini Proto 的 VCC 允许电压和电流范围是什么？；原因：原理图只标 VCC，未标数值或额定参数；电压由连接的外部端口决定。
- `review.signal-direction`：I 与 O 的方向命名是相对于 J1 主机端还是 P1 原型电路端？J1 pin 2 的 IO 是否允许双向使用？；原因：本页是无源直连，没有方向箭头、缓冲器或方向控制网络，I/O 文字的参考端未定义。
- `review.bus-protocol`：J1 的 MISO/IO 命名对应哪一种预期总线或具体端口用途？；原因：只有 MISO 和 IO 两个信号名，没有构成完整 SPI 或其他总线所需的控制器、设备与配套网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `30f934ab04541f931309dc75b2e8a3efd8f762b09046c26a73b4519df8f096e8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/810/U064_SCHE.jpg` |

---

源文档：`zh_CN/unit/mini-proto.md`

源文档 SHA-256：`98aed1f4e8ea5a2527db2bb6cbb70c6797f90d74969071cc4932181e6bd5ccd2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
