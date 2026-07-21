# Unit RGB 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RGB |
| SKU | U003 |
| 产品 ID | `unit-rgb-c8ad97af0ab8` |
| 源文档 | `zh_CN/unit/rgb.md` |

## 概述

Unit RGB（U003）由 LED1~LED3 三颗 SK6812 可寻址 RGB LED 串行连接。DI 网络同时引到 J1 pin 1 和 J2 pin 1，并由 R1 4.7KΩ 上拉到 VCC；数据从 LED3 DIN 进入，依次经过 LED3、LED2、LED1，最终由 LED1 DOUT 送到 J1 pin 2 O。J1 提供 DI、级联输出、VCC、GND，J2 提供并联 DI、VCC、GND且 pin 2 未连接；全部 LED 直接使用 VCC。原理图未标注 VCC 数值、SK6812 的 3535 封装后缀、串行协议时序或亮度/颜色性能，也未显示电源去耦或接口保护。

## 检索关键词

`Unit RGB`、`U003`、`SK6812`、`LED1`、`LED2`、`LED3`、`RGB LED`、`DI`、`DIN`、`DOUT`、`VDD`、`VSS`、`J1 Grove`、`J2 Grove`、`R1 4.7KΩ`、`VCC`、`GND`、`single-wire RGB`、`LED cascade`、`DI pull-up`、`J1 pin 1 DI`、`J1 pin 2 DOUT`、`J2 pin 1 DI`、`J2 pin 2 NC`、`SK6812 3535`、`5V`、`256 brightness levels`、`3 RGB LEDs`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED3 | SK6812 | 三颗串行级联的可寻址 RGB LED，每颗包含 DOUT、VSS、DIN、VDD | 图 e295890e1675 / 第 1 页 / 第 1 页 B2:B3 LED1/LED2/LED3，均标 SK6812，pins 1~4 DOUT/VSS/DIN/VDD |
| J1 | Grove | 包含 DI 输入、LED 链 DOUT 输出、VCC 与 GND 的四针接口 | 图 e295890e1675 / 第 1 页 / 第 1 页 B1 J1 Grove，pin 1 I/DI、pin 2 O/LED1 DOUT、pin 3 VCC、pin 4 GND |
| J2 | Grove | 第二组 DI/VCC/GND 输入接口，pin 2 未连接 | 图 e295890e1675 / 第 1 页 / 第 1 页 B3 J2 Grove，pin 1 I/DI、pin 2 O/NC、pin 3 VCC、pin 4 GND |
| R1 | 4.7KΩ | DI 输入网络到 VCC 的上拉电阻 | 图 e295890e1675 / 第 1 页 / 第 1 页 B3 VCC-R1 4.7KΩ-DI/J2 pin1/LED3 DIN 节点 |

## 系统结构

### Unit RGB 系统架构

LED1~LED3 三颗 SK6812 形成串行 RGB 链，J1/J2 并联提供 DI 和电源，J1 额外引出链末 DOUT，R1 将 DI 上拉到 VCC。

- 参数与网络：`leds=LED1-LED3 SK6812`；`input=DI via J1 pin1 and J2 pin1`；`output=LED1 DOUT -> J1 pin2`；`pullup=R1 4.7KΩ to VCC`；`power=VCC`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 B1:B3 完整 J1-LED1/2/3-J2-R1 电路

## 核心器件

### SK6812 引脚映射

LED1~LED3 的 pin 1 为 DOUT、pin 2 为 VSS/GND、pin 3 为 DIN、pin 4 为 VDD/VCC。

- 参数与网络：`pin_1=DOUT`；`pin_2=VSS GND`；`pin_3=DIN`；`pin_4=VDD VCC`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页三个 SK6812 符号的 DOUT/VSS/DIN/VDD 与 pins 1~4

## 电源

### VCC 公共电源轨

J1 pin 3、J2 pin 3 和 LED1~LED3 pin 4 VDD 全部连接 VCC；LED VSS pin 2 与连接器 pin 4 全部接 GND。

- 参数与网络：`rail=VCC`；`connector_inputs=J1 pin3,J2 pin3`；`loads=LED1-LED3 pin4 VDD`；`return=LED1-LED3 pin2 VSS,J1/J2 pin4 GND`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页所有 VCC/GND 同名网络与三个 LED VDD/VSS

### 电源转换与去耦

本页未显示稳压器、LDO、DC/DC、负载开关、充电器、电池、电源监测器或任何 VCC 去耦电容。

- 参数与网络：`regulator=null`；`ldo=null`；`dc_dc=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null`；`decoupling=null`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页仅 J1/J2/LED1~LED3/R1，无电源转换或电容

## 接口

### J1 Grove 针脚

J1 pin 1 标注 I 并连接 DI，pin 2 标注 O 并连接 LED1 DOUT，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`pin_1=I-DI，数据输入`；`pin_2=O-LED1 DOUT，级联输出`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 B1 J1 pins 1~4 与 DI/DOUT/VCC/GND

### J2 Grove 针脚

J2 pin 1 标注 I 并连接 DI，pin 2 标注 O 且未连接，pin 3 为 VCC，pin 4 为 GND。

- 参数与网络：`pin_1=I-DI，数据输入`；`pin_2=O-NC`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 B3 J2 pins 1~4 与 DI/NC/VCC/GND

## 总线

### 三颗 LED 串行数据链

DI 连接 LED3 pin 3 DIN，LED3 DOUT 连接 LED2 DIN，LED2 DOUT 连接 LED1 DIN，LED1 pin 1 DOUT 连接 J1 pin 2 O。

- 参数与网络：`input=DI -> LED3 pin3 DIN`；`stage_1=LED3 pin1 DOUT -> LED2 pin3 DIN`；`stage_2=LED2 pin1 DOUT -> LED1 pin3 DIN`；`output=LED1 pin1 DOUT -> J1 pin2 O`；`count=3`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 B1:B3 LED3->LED2->LED1 串行连线及 J1 输出

### 其他总线与地址

原理图未显示 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S，也没有器件地址或片选网络。

- 参数与网络：`led_serial=DI/DOUT`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页全部数据网络仅 DI 与逐级 DOUT

## GPIO 与控制信号

### DI 默认偏置

R1 4.7KΩ 将 DI 上拉到 VCC，页面未显示下拉或主动方向控制。

- 参数与网络：`net=DI`；`pullup=R1 4.7KΩ to VCC`；`pulldown=null`；`direction_control=null`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 B3 VCC-R1 4.7KΩ-DI 节点

## 时钟

### 时钟、复位与调试

本页未显示独立晶振/时钟、RESET、BOOT、EN、中断或调试接口；LED 仅通过 DI/DOUT 串行链控制。

- 参数与网络：`clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`control=DI/DOUT`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页全部网络仅 DI/DOUT/VCC/GND

## 保护电路

### 数据与电源保护

DI、DOUT 和 VCC 接口路径未显示 TVS/ESD、保险丝、限流、反接或过压保护；R1 仅是 DI 上拉电阻。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`pullup=R1 4.7KΩ`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页完整接口/LED 路径，无保护器件符号或位号

## 关键网络

### DI 并联输入

J1 pin 1 和 J2 pin 1 通过同名 DI 网络并联，并共同连接 LED3 DIN；页面没有输入选择器、缓冲器、串联电阻或电平转换器。

- 参数与网络：`sources=J1 pin1,J2 pin1`；`net=DI`；`destination=LED3 pin3 DIN`；`selector=null`；`buffer=null`；`series=null`；`level_shifter=null`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页 J1/J2 pin1 DI 同名网络与 LED3 DIN

## 存储

### 外部存储与内存

本页未显示主控、Flash、EEPROM、RAM、SD 卡或其他外部存储器件。

- 参数与网络：`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`
- 证据：图 e295890e1675 / 第 1 页 / 第 1 页仅三个 SK6812、两个 Grove 与一只电阻

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RGB 系统架构 | `leds=LED1-LED3 SK6812`；`input=DI via J1 pin1 and J2 pin1`；`output=LED1 DOUT -> J1 pin2`；`pullup=R1 4.7KΩ to VCC`；`power=VCC` |
| 核心器件 | SK6812 引脚映射 | `pin_1=DOUT`；`pin_2=VSS GND`；`pin_3=DIN`；`pin_4=VDD VCC` |
| 总线 | 三颗 LED 串行数据链 | `input=DI -> LED3 pin3 DIN`；`stage_1=LED3 pin1 DOUT -> LED2 pin3 DIN`；`stage_2=LED2 pin1 DOUT -> LED1 pin3 DIN`；`output=LED1 pin1 DOUT -> J1 pin2 O`；`count=3` |
| 接口 | J1 Grove 针脚 | `pin_1=I-DI，数据输入`；`pin_2=O-LED1 DOUT，级联输出`；`pin_3=VCC`；`pin_4=GND` |
| 接口 | J2 Grove 针脚 | `pin_1=I-DI，数据输入`；`pin_2=O-NC`；`pin_3=VCC`；`pin_4=GND` |
| 关键网络 | DI 并联输入 | `sources=J1 pin1,J2 pin1`；`net=DI`；`destination=LED3 pin3 DIN`；`selector=null`；`buffer=null`；`series=null`；`level_shifter=null` |
| GPIO 与控制信号 | DI 默认偏置 | `net=DI`；`pullup=R1 4.7KΩ to VCC`；`pulldown=null`；`direction_control=null` |
| 电源 | VCC 公共电源轨 | `rail=VCC`；`connector_inputs=J1 pin3,J2 pin3`；`loads=LED1-LED3 pin4 VDD`；`return=LED1-LED3 pin2 VSS,J1/J2 pin4 GND` |
| 电源 | 电源转换与去耦 | `regulator=null`；`ldo=null`；`dc_dc=null`；`load_switch=null`；`charger=null`；`battery=null`；`monitor=null`；`decoupling=null` |
| 保护电路 | 数据与电源保护 | `tvs_esd=null`；`fuse=null`；`current_limit=null`；`reverse_polarity=null`；`overvoltage=null`；`pullup=R1 4.7KΩ` |
| 时钟 | 时钟、复位与调试 | `clock=null`；`reset=null`；`boot=null`；`enable=null`；`interrupt=null`；`debug=null`；`control=DI/DOUT` |
| 存储 | 外部存储与内存 | `controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null` |
| 总线 | 其他总线与地址 | `led_serial=DI/DOUT`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`；`address=null` |
| 电源 | VCC 电压 | `net=VCC`；`schematic_voltage=null`；`candidate_from_product_doc=DC 5V`；`allowed_range=null`；`maximum_current=null` |
| 核心器件 | SK6812 完整封装型号 | `schematic_part=SK6812`；`package=null`；`version=null`；`candidate_from_product_doc=SK6812 (3535)` |
| 其他事实 | LED 协议与显示性能 | `timing=null`；`bit_order=null`；`refresh_rate=null`；`reset_time=null`；`logic_threshold=null`；`brightness_levels=null`；`color_count=null`；`power=null` |
| 接口 | J1/J2 预期级联用法 | `J1=DI input and DOUT output`；`J2=DI input, pin2 NC`；`mechanical_orientation=null`；`intended_role=null`；`simultaneous_input_allowed=null` |

## 待确认事项

- `power.vcc-voltage`：原理图仅使用 VCC 网络名，没有标注电压数值、允许范围或最大电流，不能仅凭本页确认 DC 5V。（证据：图 e295890e1675 / 第 1 页 / 第 1 页 J1/J2/LED 的 VCC 标签，无电压数字）
- `component.led-package`：原理图只标 SK6812，没有标注 3535 封装、版本或完整订货型号。（证据：图 e295890e1675 / 第 1 页 / 第 1 页 LED1~LED3 下方仅标 SK6812）
- `other.led-protocol-performance`：原理图未标注 DI/DOUT 时序、位序、刷新率、复位时间、逻辑阈值、亮度级数、颜色数或单灯/全板功耗。（证据：图 e295890e1675 / 第 1 页 / 第 1 页仅 SK6812 型号与 DI/DOUT 电气连接，无协议/性能参数）
- `interface.connector-role`：电气连接确认 J1/J2 pin 1 都接 DI、只有 J1 pin 2 接链末 DOUT；原理图没有说明两接口的机械方向、命名为输入/输出的产品用法或同时接入时的限制。（证据：图 e295890e1675 / 第 1 页 / 第 1 页 J1/J2 DI 并联与 J1-only DOUT 连接，接口旁无角色说明）
- `review.vcc-voltage`：Unit RGB 的 VCC 允许范围和最大供电电流是什么？；原因：原理图只标 VCC，需 LED datasheet 与整机电气规范确认。
- `review.led-package`：LED1~LED3 的完整 SK6812 型号和封装是否为 3535？；原因：原理图只标 SK6812，需 BOM 或实物确认。
- `review.led-protocol-performance`：该 LED 版本的单线时序、逻辑阈值、亮度/颜色能力和功耗参数是什么？；原因：这些参数不在原理图中，需对应 SK6812 datasheet 和整板测试确认。
- `review.connector-role`：J1 与 J2 的预期输入/输出和机械方向是什么，是否允许同时向两个 DI 端送信号？；原因：原理图显示 DI 并联且 DOUT 仅在 J1，但没有产品级接口角色说明。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e295890e167567c6eafc62f1e2fec8199d7c5a70f958ee20a3d318a713cdca81` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003-UNIT_RGB-SCHE_page_01.png` |

---

源文档：`zh_CN/unit/rgb.md`

源文档 SHA-256：`125060340cb04140672218705e1dd341969023d6793efad2439ce36af0461fa9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
