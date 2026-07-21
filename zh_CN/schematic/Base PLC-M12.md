# Base PLC-M12 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base PLC-M12 |
| SKU | K011-B |
| 产品 ID | `base-plc-m12-65acb1fdc778` |
| 源文档 | `zh_CN/base/plc_m12.md` |

## 概述

Base PLC-M12 的板载有源电路以 U6 TPS54360 降压电源为核心，J2 输入经 F1 PPTC-1812 后形成 IN+，再通过 D6 B290B、L1 8.2uH 和输出电容生成 +5V。+5V 送往 J1 M5Stack_BUS、J3 IIC 插座和 D5 电源指示灯，IN+ 同时出现在 J1 的 HPWR pin25。P1 标出 B-/A+/12V+/12V-，P2 标出 I/O1-I/O6，但当前原理图没有画出 RS-485 收发器或这些预留接口的板内连线。

## 检索关键词

`Base PLC-M12`、`K011-B`、`TPS54360`、`PPTC-1812`、`B290B`、`IN12/24V`、`IN+`、`+5V`、`HPWR`、`M5Stack_BUS`、`PWR3.5`、`HDR_4P`、`HDR_6P`、`B-`、`A+`、`12V+`、`12V-`、`I/O1`、`I/O6`、`IIC_Socket_4P`、`SDA`、`SCL`、`GPIO16`、`GPIO17`、`RS485`、`RS485_TX`、`RS485_RX`、`GPIO21`、`GPIO22`、`BATTERY`、`LED 0603`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | TPS54360 | 将 IN+ 宽压输入降压为 +5V 的开关降压转换器 | 图 acb19df9e443 / 第 1 页 / 第 1 页左上 U6 TPS54360，VIN/BOOT/SW/COMP/FB 与外围网络 |
| J2 | PWR3.5 | IN12/24V 与 GND 外部直流输入连接器 | 图 acb19df9e443 / 第 1 页 / 第 1 页最左上 J2 PWR3.5，正输入经 F1 形成 IN+，回路接 GND |
| F1 | PPTC-1812 | 串联在 J2 正输入与 IN+ 之间的自恢复保护器件 | 图 acb19df9e443 / 第 1 页 / 第 1 页左上 J2 与 IN+ 之间 F1 PPTC-1812 |
| D6 | B290B | TPS54360 SW 节点到 GND 的续流二极管 | 图 acb19df9e443 / 第 1 页 / 第 1 页 U6 右侧 D6 B290B，从 SW/L1 前节点接 GND |
| L1 | 8.2uH | TPS54360 降压级输出电感，连接 SW 节点与 +5V | 图 acb19df9e443 / 第 1 页 / 第 1 页上方 L1 8.2uH，左接 SW 节点，右接 +5V |
| C1,C2,C3,C5,C6 | 100nF / 10uF / 10uF / 2.2uF / 2.2uF | TPS54360 启动、输入和输出滤波电容 | 图 acb19df9e443 / 第 1 页 / 第 1 页电源区 C1 100nF BOOT-SW，C5/C6 2.2uF IN+-GND，C2/C3 10uF +5V-GND |
| R27,C4 | 12KΩ / 6.8nF | TPS54360 COMP 引脚补偿网络 | 图 acb19df9e443 / 第 1 页 / 第 1 页 U6 COMP pin6 右侧 R27 12KΩ 与 C4 6.8nF |
| R28,R30 | 51KΩ / 10KΩ | TPS54360 +5V 输出反馈分压网络 | 图 acb19df9e443 / 第 1 页 / 第 1 页 U6 FB pin5 周围 R28 51KΩ 接 +5V、R30 10KΩ 接 GND |
| R29 | 160KΩ | TPS54360 RT/CLK pin4 到 GND 的频率设定电阻 | 图 acb19df9e443 / 第 1 页 / 第 1 页 U6 RT/CLK pin4 下方 R29，标注 160KΩ，接 GND |
| P1 | HDR_4P | 标为 B-、A+、12V+、12V- 的四针预留端子 | 图 acb19df9e443 / 第 1 页 / 第 1 页左中 P1 HDR_4P，pin1 B-、pin2 A+、pin3 12V+、pin4 12V-，均为短引线 |
| P2 | HDR_6P | 标为 I/O1-I/O6 的六针预留转接接口 | 图 acb19df9e443 / 第 1 页 / 第 1 页左中 P2 HDR_6P，pin1-pin6 标注 I/O1-I/O6，均为短引线 |
| J3 | IIC_Socket_4P | 引出 SCL、SDA、+5V 与 GND 的四针 I2C 接口 | 图 acb19df9e443 / 第 1 页 / 第 1 页右中 J3 IIC_Socket_4P，pin1 SCL、pin2 SDA、pin3 VCC/+5V、pin4 GND |
| J1 | M5Stack_BUS | 30 针主机堆叠总线，提供 GPIO、SDA/SCL、IN+/HPWR、+3.3V、+5V 和 BATTERY 网络 | 图 acb19df9e443 / 第 1 页 / 第 1 页右下 J1 M5Stack_BUS，1-30 脚及外侧网络标签 |
| D5,R20 | LED 0603 / 4.7KΩ | +5V 电源指示 LED 和限流电阻 | 图 acb19df9e443 / 第 1 页 / 第 1 页右上 +5V-D5 LED 0603-R20 4.7KΩ-GND 支路 |

## 系统结构

### Base PLC-M12 系统架构

Base PLC-M12 主板以 U6 TPS54360 生成 +5V，并通过 J1 M5Stack_BUS 与主机堆叠；板上另有 J3 I2C 接口及 P1/P2 预留转接接口，当前页没有独立主控或 RS-485 收发器。

- 参数与网络：`power_converter=U6 TPS54360`；`host_connector=J1 M5Stack_BUS`；`i2c_connector=J3 IIC_Socket_4P`；`reserved_connectors=P1 HDR_4P; P2 HDR_6P`；`onboard_mcu_shown=false`；`rs485_transceiver_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页完整单页：左上电源、左中 P1/P2、右中 J3、右下 J1

## 电源

### IN+ 到 +5V 降压路径

U6 TPS54360 VIN pin2 接 IN+，SW pin8 连接 D6 B290B 与 L1 8.2uH，L1 后形成 +5V；C2/C3 各 10uF 从 +5V 接 GND。

- 参数与网络：`input=IN+`；`converter=U6 TPS54360`；`switch_pin=U6 pin8 SW`；`freewheel_diode=D6 B290B`；`inductor=L1 8.2uH`；`output=+5V`；`output_capacitors=C2/C3 10uF`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页左上 U6/D6/L1/C2/C3 与 IN+/+5V

### TPS54360 使能连接

U6 EN pin3 在当前原理图标记为未连接，没有画出外部使能控制网络。

- 参数与网络：`pin=U6 pin3 EN`；`connected=false`；`external_enable_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页 U6 左侧 EN pin3 短引线及未连接标记

### TPS54360 反馈与补偿

U6 FB pin5 使用 R28 51KΩ 与 R30 10KΩ 分压；COMP pin6 使用 R27 12KΩ 和 C4 6.8nF，BOOT 与 SW 之间连接 C1 100nF。

- 参数与网络：`feedback_upper=R28 51KΩ`；`feedback_lower=R30 10KΩ`；`compensation=R27 12KΩ; C4 6.8nF`；`bootstrap=C1 100nF between BOOT and SW`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页 U6 FB/COMP/BOOT 周围 R28/R30/R27/C4/C1

### +5V 电源分配

U6 产生的 +5V 连接 J1 M5Stack_BUS pin28、J3 pin3 VCC 和 D5 电源指示支路。

- 参数与网络：`source=U6/L1 output`；`host_bus=J1 pin28 +5V`；`i2c_connector=J3 pin3 VCC/+5V`；`indicator=D5 LED 0603 with R20 4.7KΩ`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页 +5V 全局网络：L1 输出、J3 pin3、D5、J1 pin28

### +5V 电源指示

D5 LED 0603 与 R20 4.7KΩ 串联在 +5V 和 GND 之间。

- 参数与网络：`rail=+5V`；`led=D5 LED 0603`；`resistor=R20 4.7KΩ`；`return=GND`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页右上 +5V-D5-R20-GND 支路

## 接口

### J3 I2C 接口

J3 IIC_Socket_4P pin1=SCL、pin2=SDA、pin3=VCC/+5V、pin4=GND；当前页面未画出 SDA/SCL 上拉电阻。

- 参数与网络：`pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND`；`pullups_shown=false`；`direction=SDA bidirectional; SCL clock line`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页右中 J3 IIC_Socket_4P 1-4 脚及完整页面，无 SDA/SCL 上拉

### J1 M5Stack_BUS

J1 是 2x15 的 30 针 M5Stack_BUS，图中标出 GND、GPIO35/36、EN、GPIO23/25/19/26/18/0/16/17/21/5/13/34、SDA、SCL、+3.3V、IN+/HPWR、+5V 与 BATTERY。

- 参数与网络：`connector=J1 M5Stack_BUS`；`pins=30`；`ground_pins=1,3,5`；`i2c=pin17 SDA/GPIO21; pin18 SCL/GPIO22`；`power=pin12 +3.3V; pin25 IN+/HPWR; pin27/pin29 HPWR; pin28 +5V; pin30 BATTERY`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页右下 J1 M5Stack_BUS 1-30 脚及外部网络

### P1 四针端子标签

P1 HDR_4P pin1-pin4 分别标为 B-、A+、12V+、12V-；四条引线在当前页面均未连接到命名网络。

- 参数与网络：`pin1=B-`；`pin2=A+`；`pin3=12V+`；`pin4=12V-`；`routing_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页左中 P1 HDR_4P，B-/A+/12V+/12V- 均为独立短引线

### P2 六针 I/O 标签

P2 HDR_6P pin1-pin6 分别标为 I/O1、I/O2、I/O3、I/O4、I/O5、I/O6；六条引线在当前页面均未连接到命名网络。

- 参数与网络：`pin1=I/O1`；`pin2=I/O2`；`pin3=I/O3`；`pin4=I/O4`；`pin5=I/O5`；`pin6=I/O6`；`routing_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页左中 P2 HDR_6P，I/O1-I/O6 均为独立短引线

## 总线

### J3 与 M5Bus I2C 路由

SDA 网络连接 J3 pin2 与 J1 M5Stack_BUS pin17/GPIO21，SCL 网络连接 J3 pin1 与 J1 pin18/GPIO22；本页没有板载 I2C 从设备或地址。

- 参数与网络：`controller=M5Stack host`；`sda=J1 pin17 GPIO21 -> SDA -> J3 pin2`；`scl=J1 pin18 GPIO22 -> SCL -> J3 pin1`；`onboard_address_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页 J3 SDA/SCL 与 J1 pin17 SDA/GPIO21、pin18 SCL/GPIO22

## 时钟

### TPS54360 开关频率设定

U6 RT/CLK pin4 通过 R29 160KΩ 接 GND；原理图未直接标出对应开关频率。

- 参数与网络：`pin=U6 pin4 RT/CLK`；`resistor=R29 160KΩ to GND`；`frequency_label_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页 U6 RT/CLK pin4 与 R29 160KΩ/GND

## 保护电路

### 外部电源输入保护

J2 的正电源输入先串联 F1 PPTC-1812 后形成 IN+，C5/C6 各 2.2uF 从 IN+ 接 GND。

- 参数与网络：`connector=J2 PWR3.5`；`positive_path=J2 -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C5/C6 2.2uF`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页左上 J2/F1/IN+/C5/C6

## 关键网络

### IN+ 与 M5Bus HPWR

F1 后的 IN+ 同时连接 U6 VIN 和 J1 pin25；J1 符号内 pin25 标为 HPWR，pin27/pin29 也标为 HPWR。

- 参数与网络：`input_net=IN+`；`buck_destination=U6 pin2 VIN`；`bus_destination=J1 pin25 HPWR`；`other_hpwr_pins=J1 pin27 and pin29`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页左上 IN+ 网络及右下 J1 pin25 外侧 IN+、符号内 HPWR

## 存储

### 板载存储

当前完整单页原理图未画出 Flash、PSRAM、EEPROM 或存储卡接口。

- 参数与网络：`flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页完整单页器件，仅有电源 IC、连接器和指示 LED，未见存储器件

## 调试与烧录

### 专用调试接口

当前完整单页原理图未画出 JTAG、SWD、USB-UART 或专用编程调试连接器。

- 参数与网络：`jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`debug_connector_shown=false`
- 证据：图 acb19df9e443 / 第 1 页 / 第 1 页完整连接器 J1-J3/P1/P2，无调试接口标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base PLC-M12 系统架构 | `power_converter=U6 TPS54360`；`host_connector=J1 M5Stack_BUS`；`i2c_connector=J3 IIC_Socket_4P`；`reserved_connectors=P1 HDR_4P; P2 HDR_6P`；`onboard_mcu_shown=false`；`rs485_transceiver_shown=false` |
| 保护电路 | 外部电源输入保护 | `connector=J2 PWR3.5`；`positive_path=J2 -> F1 PPTC-1812 -> IN+`；`return=GND`；`input_capacitors=C5/C6 2.2uF` |
| 电源 | IN+ 到 +5V 降压路径 | `input=IN+`；`converter=U6 TPS54360`；`switch_pin=U6 pin8 SW`；`freewheel_diode=D6 B290B`；`inductor=L1 8.2uH`；`output=+5V`；`output_capacitors=C2/C3 10uF` |
| 电源 | TPS54360 使能连接 | `pin=U6 pin3 EN`；`connected=false`；`external_enable_shown=false` |
| 电源 | TPS54360 反馈与补偿 | `feedback_upper=R28 51KΩ`；`feedback_lower=R30 10KΩ`；`compensation=R27 12KΩ; C4 6.8nF`；`bootstrap=C1 100nF between BOOT and SW` |
| 时钟 | TPS54360 开关频率设定 | `pin=U6 pin4 RT/CLK`；`resistor=R29 160KΩ to GND`；`frequency_label_shown=false` |
| 关键网络 | IN+ 与 M5Bus HPWR | `input_net=IN+`；`buck_destination=U6 pin2 VIN`；`bus_destination=J1 pin25 HPWR`；`other_hpwr_pins=J1 pin27 and pin29` |
| 电源 | +5V 电源分配 | `source=U6/L1 output`；`host_bus=J1 pin28 +5V`；`i2c_connector=J3 pin3 VCC/+5V`；`indicator=D5 LED 0603 with R20 4.7KΩ` |
| 电源 | +5V 电源指示 | `rail=+5V`；`led=D5 LED 0603`；`resistor=R20 4.7KΩ`；`return=GND` |
| 接口 | J3 I2C 接口 | `pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND`；`pullups_shown=false`；`direction=SDA bidirectional; SCL clock line` |
| 总线 | J3 与 M5Bus I2C 路由 | `controller=M5Stack host`；`sda=J1 pin17 GPIO21 -> SDA -> J3 pin2`；`scl=J1 pin18 GPIO22 -> SCL -> J3 pin1`；`onboard_address_shown=false` |
| 接口 | J1 M5Stack_BUS | `connector=J1 M5Stack_BUS`；`pins=30`；`ground_pins=1,3,5`；`i2c=pin17 SDA/GPIO21; pin18 SCL/GPIO22`；`power=pin12 +3.3V; pin25 IN+/HPWR; pin27/pin29 HPWR; pin28 +5V; pin30 BATTERY` |
| 接口 | P1 四针端子标签 | `pin1=B-`；`pin2=A+`；`pin3=12V+`；`pin4=12V-`；`routing_shown=false` |
| 接口 | P2 六针 I/O 标签 | `pin1=I/O1`；`pin2=I/O2`；`pin3=I/O3`；`pin4=I/O4`；`pin5=I/O5`；`pin6=I/O6`；`routing_shown=false` |
| 总线 | 可选 RS-485 转接板路由 | `documented_gpio=GPIO16/GPIO17`；`bus_pins_visible=J1 pin15 GPIO16; J1 pin16 GPIO17`；`transceiver_shown=false`；`p1_p2_routing_shown=false`；`direction_control_shown=false`；`termination_shown=false` |
| 电源 | P1 12V 端子供电来源 | `terminal_positive=P1 pin3 12V+`；`terminal_negative=P1 pin4 12V-`；`input_nets=J2 IN12/24V; IN+; GND`；`explicit_connection_shown=false` |
| 存储 | 板载存储 | `flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`memory_card_shown=false` |
| 调试与烧录 | 专用调试接口 | `jtag_shown=false`；`swd_shown=false`；`usb_uart_shown=false`；`debug_connector_shown=false` |

## 待确认事项

- `bus.documented-rs485-routing`：产品正文说明可选 TTL-RS485 转接板使用 G16/G17，但当前原理图没有画出 P1/P2 到 J1 GPIO16/GPIO17 的连接，也没有收发器、DE/RE、A/B 终端或保护电路。（证据：图 acb19df9e443 / 第 1 页 / 第 1 页 P1/P2 短引线与 J1 pin15/pin16，页面无连接线或 RS-485 收发器）
- `power.p1-12v-routing`：P1 pin3/pin4 标为 12V+/12V-，但当前页面未显示它们与 J2 IN12/24V、IN+、GND 或其他电源网络的连接。（证据：图 acb19df9e443 / 第 1 页 / 第 1 页 P1 12V+/12V- 短引线与左上 J2/IN+ 电源区，二者无连线或同名网络）
- `review.rs485-adapter-routing`：K011-B 配套 TTL-RS485 转接板的 P1/P2 针脚、收发器型号、GPIO16/GPIO17 方向及 DE/RE 控制关系是什么？；原因：当前主板原理图只显示 P1/P2 标签和 J1 GPIO16/GPIO17，没有转接板原理图或电气连接。
- `review.p1-12v-source`：P1 的 12V+ 与 12V- 在 PCB 或配套转接板上实际连接哪个电源输入和回路？；原因：P1 只显示 12V+/12V- 标签，当前页面没有到 J2、IN+ 或 GND 的可追踪连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `acb19df9e44355fa0186560215bdde2ea7ffd7e7676619f8d9abc61b1febf848` | `https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_sch_01.webp` |

---

源文档：`zh_CN/base/plc_m12.md`

源文档 SHA-256：`5fbaea585b834301419d761411c063402e007bc4b373fe633787b6dfb5d9573c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
