# Unit Proto 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Proto |
| SKU | U022 |
| 产品 ID | `unit-proto-342508bb9734` |
| 源文档 | `zh_CN/unit/proto.md` |

## 概述

Unit Proto（U022）原理图是 P1 Header 4 与 J1 Grove 之间的四针无源直连，P1 pins 1~4 分别对应 J1 的 I、O、VCC、GND。页面内没有主控、协处理器、传感器、电源转换、保护、时钟、复位、调试或存储器件。原理图未标注 VCC 电压、I/O 命名相对于哪一侧的方向，也未展示原型焊盘数量、孔径和孔距。

## 检索关键词

`Unit Proto`、`U022`、`Proto Unit`、`P1`、`Header 4`、`J1`、`Grove`、`I`、`O`、`VCC`、`GND`、`P1 pin 1`、`P1 pin 2`、`P1 pin 3`、`P1 pin 4`、`J1 pin 1 I`、`J1 pin 2 O`、`J1 pin 3 VCC`、`J1 pin 4 GND`、`无源直连`、`原型板`、`77 holes`、`2.54mm`、`1mm hole`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 4 | 四针内部排针/原型电路接口，逐针连接 J1 | 图 30fc13708a2c / 第 1 页 / 第 1 页 B2 中央 P1 Header 4，pins 1~4 四条横线连接 J1 |
| J1 | Grove | 四针外部 Grove 接口，功能为 I、O、VCC、GND | 图 30fc13708a2c / 第 1 页 / 第 1 页 B2 中央 J1 Grove，pins 1~4 标注 I/O/VCC/GND |

## 系统结构

### Unit Proto 架构

电路仅由 P1 Header 4 和 J1 Grove 组成，四个针脚一一直接相连，没有中间器件或有源功能分区。

- 参数与网络：`internal=P1 Header 4`；`external=J1 Grove`；`connection=pin-to-pin direct`；`active_devices=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页完整原理图仅 P1/J1 与四条直连线

### 有源功能分区

本页未显示主控、协处理器、传感器、模拟前端、射频、音频或其他 IC/模块。

- 参数与网络：`controller=null`；`coprocessor=null`；`sensor=null`；`analog=null`；`rf=null`；`audio=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页完整器件范围仅 P1 Header 4 与 J1 Grove

## 核心器件

### 连接器组成

P1 型号文字为 Header 4，J1 型号文字为 Grove；两者均明确编号 pins 1~4。

- 参数与网络：`P1=Header 4,pins 1-4`；`J1=Grove,pins 1-4`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 P1/J1 位号、型号文字和针号

## 电源

### VCC 电源通道

P1 pin 3 与 J1 pin 3 VCC 直接相连，本页没有稳压器、LDO、DC/DC、负载开关、充电器、电池或电源监测器。

- 参数与网络：`internal=P1 pin 3`；`external=J1 pin 3 VCC`；`regulator=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 P1 pin 3-J1 pin 3 VCC 直连，整页无电源器件

### GND 通道

P1 pin 4 与 J1 pin 4 GND 直接相连。

- 参数与网络：`internal=P1 pin 4`；`external=J1 pin 4 GND`；`net=GND`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 最下方 P1 pin 4-J1 pin 4 GND 连线

## 接口

### P1 Header 4 针脚

P1 pins 1~4 分别直连 J1 pins 1~4，对应功能依次为 I、O、VCC、GND。

- 参数与网络：`pin_1=J1 pin 1 I`；`pin_2=J1 pin 2 O`；`pin_3=J1 pin 3 VCC`；`pin_4=J1 pin 4 GND`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 P1 pins 1~4 到 J1 pins 1~4 的四条水平连线

### J1 Grove 针脚

J1 pin 1 为 I，pin 2 为 O，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`pin_1=I`；`pin_2=O`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 J1 Grove pins 1~4 与 I/O/VCC/GND 文字

## 总线

### 总线与地址

I/O 名称没有关联控制器或设备，本页未确认 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S，也没有地址、片选或协议参数。

- 参数与网络：`signals=I,O`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null`；`chip_select=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 J1 仅 I/O/VCC/GND，整页无控制器、设备或协议标注

## 时钟

### 时钟、复位、调试与存储

本页未显示晶振/时钟、RESET、BOOT、EN、中断、调试接口、Flash、EEPROM、RAM 或 SD 卡。

- 参数与网络：`clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页仅两个无源连接器与四条网络

## 保护电路

### 接口保护

I、O、VCC 和 GND 四条通道均未显示 TVS/ESD、保险丝、限流、反接或过压保护。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 P1-J1 四条直接连接，无保护器件符号或位号

## 关键网络

### I 信号通道

P1 pin 1 与 J1 pin 1 I 直接相连，中间没有串联电阻、上拉、下拉、滤波、缓冲、电平转换或保护器件。

- 参数与网络：`from=P1 pin 1`；`to=J1 pin 1 I`；`series=null`；`pull=null`；`filter=null`；`buffer=null`；`level_shifter=null`；`protection=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 最上方 P1 pin 1-J1 pin 1 I 连线

### O 信号通道

P1 pin 2 与 J1 pin 2 O 直接相连，中间没有串联电阻、上拉、下拉、滤波、缓冲、电平转换或保护器件。

- 参数与网络：`from=P1 pin 2`；`to=J1 pin 2 O`；`series=null`；`pull=null`；`filter=null`；`buffer=null`；`level_shifter=null`；`protection=null`
- 证据：图 30fc13708a2c / 第 1 页 / 第 1 页 B2 第二条 P1 pin 2-J1 pin 2 O 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Proto 架构 | `internal=P1 Header 4`；`external=J1 Grove`；`connection=pin-to-pin direct`；`active_devices=null` |
| 核心器件 | 连接器组成 | `P1=Header 4,pins 1-4`；`J1=Grove,pins 1-4` |
| 接口 | P1 Header 4 针脚 | `pin_1=J1 pin 1 I`；`pin_2=J1 pin 2 O`；`pin_3=J1 pin 3 VCC`；`pin_4=J1 pin 4 GND` |
| 接口 | J1 Grove 针脚 | `pin_1=I`；`pin_2=O`；`pin_3=VCC`；`pin_4=GND` |
| 关键网络 | I 信号通道 | `from=P1 pin 1`；`to=J1 pin 1 I`；`series=null`；`pull=null`；`filter=null`；`buffer=null`；`level_shifter=null`；`protection=null` |
| 关键网络 | O 信号通道 | `from=P1 pin 2`；`to=J1 pin 2 O`；`series=null`；`pull=null`；`filter=null`；`buffer=null`；`level_shifter=null`；`protection=null` |
| 电源 | VCC 电源通道 | `internal=P1 pin 3`；`external=J1 pin 3 VCC`；`regulator=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null` |
| 电源 | GND 通道 | `internal=P1 pin 4`；`external=J1 pin 4 GND`；`net=GND` |
| 保护电路 | 接口保护 | `tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null` |
| 系统结构 | 有源功能分区 | `controller=null`；`coprocessor=null`；`sensor=null`；`analog=null`；`rf=null`；`audio=null` |
| 时钟 | 时钟、复位、调试与存储 | `clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 总线与地址 | `signals=I,O`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null`；`chip_select=null` |
| 电源 | VCC 电压 | `net=VCC`；`voltage=null`；`allowed_range=null`；`current_rating=null` |
| GPIO 与控制信号 | I/O 信号方向 | `signal_1=J1 pin 1 I-P1 pin 1`；`signal_2=J1 pin 2 O-P1 pin 2`；`reference_side=null`；`direction_control=null` |
| 其他事实 | 原型焊盘机械参数 | `pad_count=null`；`hole_diameter=null`；`pitch=null`；`pad_connectivity=null`；`candidate_from_product_doc=77 holes,1mm,2.54mm` |

## 待确认事项

- `power.vcc-voltage`：原理图只标 J1 pin 3 为 VCC，未标注电压、允许范围或电流能力。（证据：图 30fc13708a2c / 第 1 页 / 第 1 页 J1 pin 3 仅标 VCC，无数值）
- `gpio.signal-direction`：J1 pins 1/2 标为 I/O，但电路是无源直连，原理图没有说明方向命名相对于 Grove 主机端还是 P1 原型电路端，也没有方向控制器件。（证据：图 30fc13708a2c / 第 1 页 / 第 1 页 J1 I/O 到 P1 的直连，无箭头、缓冲器或方向控制）
- `other.prototype-field`：当前原理图页没有绘制原型焊盘阵列，也未标注焊盘/孔数量、孔径、孔距或哪些孔与 P1 导通，因此不能由本页确认 77 holes、1mm 孔径和 2.54mm 孔距。（证据：图 30fc13708a2c / 第 1 页 / 第 1 页完整图纸仅 P1/J1，无焊盘阵列或机械尺寸）
- `review.vcc-voltage`：Unit Proto 的 VCC 允许电压和电流范围是什么？；原因：原理图只标 VCC，没有数值或额定参数。
- `review.signal-direction`：I 与 O 的方向定义是相对于 J1 主机端还是 P1 原型电路端？；原因：四条网络为无源直连，没有方向箭头或有源方向器件。
- `review.prototype-field`：原型区实际孔数、孔径、孔距及与 P1 的默认导通关系是什么？；原因：这些机械和 PCB 参数没有出现在当前原理图页。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `30fc13708a2c9f3a84b43d870bd0ea57f976928fc58e6917a9a9c5f47be8aceb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/809/U022_SCHE.jpg` |

---

源文档：`zh_CN/unit/proto.md`

源文档 SHA-256：`d645dbc3a0af392853ffcd8a45c32197f69c1057c099935a7070bace806eda17`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
