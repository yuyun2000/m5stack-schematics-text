# Unit EXT.IO 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit EXT.IO |
| SKU | U011 |
| 产品 ID | `unit-ext-io-9b18ce60fe27` |
| 源文档 | `zh_CN/unit/extio.md` |

## 概述

Unit EXT.IO 以 U1 PCA9554PW 作为 I2C GPIO 扩展器，将 IO0-IO7 八路信号引至 P1 2x5 排针，并由 INT 网络提供中断测试点。J1 提供 SCL、SDA、VCC、GND，U2 HT7533 将 VCC 稳压为 +3.3V，供 U1、I2C 上拉、INT 上拉和地址绑带使用。A0-A2 均通过 0Ω 接 +3.3V、同时由 10KΩ 下拉，图示装配形成高电平绑带；正文所列 0x27 地址仍需结合 PCA9554PW 数据手册或实测确认。图中未显示独立时钟、复位、存储器或接口瞬态保护器件。

## 检索关键词

`Unit EXT.IO`、`U011`、`PCA9554PW`、`HT7533`、`I2C`、`0x27`、`SCL`、`SDA`、`INT`、`A0`、`A1`、`A2`、`IO0`、`IO1`、`IO2`、`IO3`、`IO4`、`IO5`、`IO6`、`IO7`、`VCC`、`+3.3V`、`IIC_Socket_4P`、`Header 5X2`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R6-R8 0Ω`、`R9-R11 10KΩ`、`JP1 test`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PCA9554PW | I2C 控制的 8 位 GPIO 扩展器，连接 SCL/SDA/INT、A0-A2 和 IO0-IO7 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页上部中央 U1 PCA9554PW 及全部引脚 |
| U2 | HT7533 | 将 J1 输入的 VCC 稳压为 +3.3V | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页下部中央 U2 HT7533，VIN/VOUT/GND |
| J1 | IIC_Socket_4P | 外部 I2C 与电源接口，针脚为 SCL、SDA、VCC、GND | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页下部右侧 J1 IIC_Socket_4P |
| P1 | Header 5X2 | 引出 IO0-IO7、VCC 和 GND 的 2x5 排针 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页右上 P1 Header 5X2 |
| JP1 | test | 连接 INT 网络的测试点 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页左上 JP1 test 与 INT 水平网络 |
| R1/R2/R3 | 4.7KΩ | 分别将 SDA、SCL、INT 上拉到 +3.3V | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页左上 R1-R3 4.7KΩ 与 SDA/SCL/INT 网络 |
| R6/R7/R8 | 0Ω | 分别把 U1 A0、A1、A2 地址脚连接到 +3.3V 的配置电阻 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页左中 R6-R8 0Ω 至 U1 A0-A2 |
| R9/R10/R11 | 10KΩ | 分别将 U1 A0、A1、A2 地址脚下拉到 GND | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页左中 R9-R11 10KΩ 至 GND |
| C1/C2/C3 | 100nF | U1 +3.3V、本板 VCC 和 HT7533 输出 +3.3V 的高频去耦 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页 C1、C2、C3 100nF |
| C4/C5 | 10uF | HT7533 输出和输入侧的电源滤波电容 | 图 72a8b5e42cc0 / 第 1 页 / 第 1 页下部 C4 10uF（+3.3V）与 C5 10uF（VCC） |

## 系统结构

### Unit EXT.IO 系统结构

J1 接入 I2C 和 VCC，U2 生成 +3.3V，U1 PCA9554PW 通过 I2C 控制 IO0-IO7 并将八路 IO 引至 P1；INT 仅引到 JP1 测试点。

- 参数与网络：`controller=外部 I2C 主机，经 J1`；`device=U1 PCA9554PW`；`regulator=U2 HT7533`；`gpio_connector=P1`；`interrupt_testpoint=JP1`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页完整原理图：J1、U2、U1、P1、JP1

## 核心器件

### U1 PCA9554PW

U1 的 VDD pin16 接 +3.3V、VSS pin8 接 GND；INT/SCL/SDA 分别为 pin13/pin14/pin15，A0/A1/A2 为 pin1/pin2/pin3，IO0-IO7 为 pin4-pin7 与 pin9-pin12。

- 参数与网络：`vdd=pin16 +3.3V`；`vss=pin8 GND`；`int=pin13 INT`；`scl=pin14 SCL`；`sda=pin15 SDA`；`address_pins=A0 pin1,A1 pin2,A2 pin3`；`io_pins=IO0 pin4,IO1 pin5,IO2 pin6,IO3 pin7,IO4 pin9,IO5 pin10,IO6 pin11,IO7 pin12`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 U1 PCA9554PW 引脚编号与网络名

## 电源

### U2 HT7533 电源转换

U2 VIN pin2 接 VCC，VOUT pin3 输出 +3.3V，GND pin1 接地；VCC 直接来自 J1 pin3，并同时送到 P1 pin9。

- 参数与网络：`input=VCC at U2 pin2`；`output=+3.3V at U2 pin3`；`ground=U2 pin1 GND`；`vcc_source=J1 pin3`；`vcc_export=P1 pin9`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页下部 J1 VCC、U2 HT7533 与上部 P1 VCC

### VCC 与 +3.3V 去耦

VCC 侧配置 C2 100nF 和 C5 10uF 到 GND；+3.3V 侧配置 C3 100nF 和 C4 10uF 到 GND，U1 VDD 邻近另有 C1 100nF 到 GND。

- 参数与网络：`vcc_caps=C2 100nF,C5 10uF`；`3v3_caps=C3 100nF,C4 10uF,C1 100nF`；`return=GND`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 U1 C1 与下部 U2/C2-C5 电源网络

## 接口

### J1 IIC_Socket_4P

J1.1=SCL、J1.2=SDA、J1.3=VCC、J1.4=GND；SCL/SDA 从外部主机方向进入本板 I2C 设备，电源 VCC 进入 U2。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC`；`pin_4=GND`；`bus_direction=SCL host-to-device; SDA bidirectional`；`power_direction=VCC input`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页下部右侧 J1 pin1-pin4 网络标注

### P1 Header 5X2

P1 奇数脚依次为 pin1 IO0、pin3 IO2、pin5 IO4、pin7 IO6、pin9 VCC；偶数脚依次为 pin2 IO1、pin4 IO3、pin6 IO5、pin8 IO7、pin10 GND。

- 参数与网络：`pin_1=IO0`；`pin_2=IO1`；`pin_3=IO2`；`pin_4=IO3`；`pin_5=IO4`；`pin_6=IO5`；`pin_7=IO6`；`pin_8=IO7`；`pin_9=VCC`；`pin_10=GND`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页右上 P1 Header 5X2 pin1-pin10

## 总线

### SCL/SDA I2C 总线

J1 SCL/SDA 直接连接 U1 SCL pin14/SDA pin15；R2/R1 分别以 4.7KΩ 将 SCL/SDA 上拉至 +3.3V，图中未设置电平转换器。

- 参数与网络：`controller=外部 I2C 主机`；`device=U1 PCA9554PW`；`scl=J1.1 to U1.14, R2 4.7KΩ to +3.3V`；`sda=J1.2 to U1.15, R1 4.7KΩ to +3.3V`；`level_shifter_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 J1 SCL/SDA 至 U1 pin14/pin15 及 R1/R2

## 总线地址

### U1 A0-A2 地址绑带

A0、A1、A2 分别经 R6、R7、R8 0Ω 接 +3.3V，同时分别经 R9、R10、R11 10KΩ 接 GND；按图示元件值三个位均由 0Ω 路径强上拉。

- 参数与网络：`a0=R6 0Ω to +3.3V; R9 10KΩ to GND`；`a1=R7 0Ω to +3.3V; R10 10KΩ to GND`；`a2=R8 0Ω to +3.3V; R11 10KΩ to GND`；`shown_state=A0=A1=A2=high`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页左中 U1 A0-A2、R6-R8 与 R9-R11

## GPIO 与控制信号

### U1 IO0-IO7

U1 的八路 IO 网络按同名一一连接 P1：IO0-IO7 分别到 P1 pin1-pin8 的交错排列针脚。原理图未固定各路运行时输入或输出模式。

- 参数与网络：`count=8`；`mapping=IO0=P1.1,IO1=P1.2,IO2=P1.3,IO3=P1.4,IO4=P1.5,IO5=P1.6,IO6=P1.7,IO7=P1.8`；`runtime_direction_fixed=false`；`supply_domain=U1 VDD +3.3V`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 U1 IO0-IO7 与 P1 IO0-IO7 同名网络

### U1 INT

U1 INT pin13 连接 INT 网络，由 R3 4.7KΩ 上拉至 +3.3V，并连接 JP1 test；INT 未引到 J1 或 P1。

- 参数与网络：`source=U1 pin13`；`net=INT`；`pullup=R3 4.7KΩ to +3.3V`；`testpoint=JP1`；`external_connector=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页左上 JP1/R3/INT 至 U1 pin13

## 时钟

### 时钟电路

完整原理图未显示晶振、振荡器或外部时钟网络。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页完整图无时钟器件或时钟网络

## 复位

### 复位与使能

完整原理图未显示复位按键、RESET 网络、BOOT 网络或电源使能控制；U2 图示器件仅有 VIN、VOUT、GND。

- 参数与网络：`reset_switch_shown=false`；`reset_net_shown=false`；`boot_net_shown=false`；`enable_net_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页完整图及 U2 VIN/VOUT/GND 引脚

## 保护电路

### J1 与 P1 接口保护

完整原理图未在 J1 或 P1 的电源与信号路径画出 TVS、ESD 阵列、保险丝、反接保护或串联限流器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_current_limiter_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 J1/P1 至 U1/U2 的全部连接路径

## 关键网络

### VCC 与 +3.3V

VCC 是 J1 输入并在 P1 pin9 原样引出的外部电源网；+3.3V 是 U2 输出，供 U1 VDD、R1-R3 上拉、R6-R8 地址绑带及去耦电容使用，两电源网不短接。

- 参数与网络：`vcc_nodes=J1.3,U2 VIN,P1.9,C2,C5`；`3v3_nodes=U2 VOUT,U1.16,R1-R3,R6-R8,C1,C3,C4`；`ground_nodes=J1.4,P1.10,U1.8,U2.1`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页完整 VCC、+3.3V 与 GND 网络

## 内存与 Flash

### 存储器

完整原理图未显示 Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页完整图无存储器件或存储接口

## 调试与烧录

### JP1 test

JP1 是 INT 网络上的单点测试连接，用于接触或测量中断网络；图中没有 JTAG、SWD 或 UART 调试连接器。

- 参数与网络：`reference=JP1`；`net=INT`；`jtag_shown=false`；`swd_shown=false`；`uart_debug_shown=false`
- 证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页左上 JP1 test；完整页无其他调试连接器

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit EXT.IO 系统结构 | `controller=外部 I2C 主机，经 J1`；`device=U1 PCA9554PW`；`regulator=U2 HT7533`；`gpio_connector=P1`；`interrupt_testpoint=JP1` |
| 核心器件 | U1 PCA9554PW | `vdd=pin16 +3.3V`；`vss=pin8 GND`；`int=pin13 INT`；`scl=pin14 SCL`；`sda=pin15 SDA`；`address_pins=A0 pin1,A1 pin2,A2 pin3`；`io_pins=IO0 pin4,IO1 pin5,IO2 pin6,IO3 pin7,IO4 pin9,IO5 pin10,IO6 pin11,IO7 pin12` |
| 电源 | U2 HT7533 电源转换 | `input=VCC at U2 pin2`；`output=+3.3V at U2 pin3`；`ground=U2 pin1 GND`；`vcc_source=J1 pin3`；`vcc_export=P1 pin9` |
| 电源 | VCC 与 +3.3V 去耦 | `vcc_caps=C2 100nF,C5 10uF`；`3v3_caps=C3 100nF,C4 10uF,C1 100nF`；`return=GND` |
| 接口 | J1 IIC_Socket_4P | `pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC`；`pin_4=GND`；`bus_direction=SCL host-to-device; SDA bidirectional`；`power_direction=VCC input` |
| 接口 | P1 Header 5X2 | `pin_1=IO0`；`pin_2=IO1`；`pin_3=IO2`；`pin_4=IO3`；`pin_5=IO4`；`pin_6=IO5`；`pin_7=IO6`；`pin_8=IO7`；`pin_9=VCC`；`pin_10=GND` |
| 总线 | SCL/SDA I2C 总线 | `controller=外部 I2C 主机`；`device=U1 PCA9554PW`；`scl=J1.1 to U1.14, R2 4.7KΩ to +3.3V`；`sda=J1.2 to U1.15, R1 4.7KΩ to +3.3V`；`level_shifter_shown=false` |
| GPIO 与控制信号 | U1 IO0-IO7 | `count=8`；`mapping=IO0=P1.1,IO1=P1.2,IO2=P1.3,IO3=P1.4,IO4=P1.5,IO5=P1.6,IO6=P1.7,IO7=P1.8`；`runtime_direction_fixed=false`；`supply_domain=U1 VDD +3.3V` |
| GPIO 与控制信号 | U1 INT | `source=U1 pin13`；`net=INT`；`pullup=R3 4.7KΩ to +3.3V`；`testpoint=JP1`；`external_connector=false` |
| 调试与烧录 | JP1 test | `reference=JP1`；`net=INT`；`jtag_shown=false`；`swd_shown=false`；`uart_debug_shown=false` |
| 总线地址 | U1 A0-A2 地址绑带 | `a0=R6 0Ω to +3.3V; R9 10KΩ to GND`；`a1=R7 0Ω to +3.3V; R10 10KΩ to GND`；`a2=R8 0Ω to +3.3V; R11 10KΩ to GND`；`shown_state=A0=A1=A2=high` |
| 总线地址 | PCA9554PW I2C 地址 | `documented_address=0x27`；`address_width=7-bit`；`strap=A0=A1=A2=high`；`address_printed_on_schematic=false` |
| 电源 | J1 VCC 输入范围 | `documented_range=2.3-5.5V`；`input_net=VCC`；`regulator=U2 HT7533`；`range_printed_on_schematic=false` |
| 关键网络 | VCC 与 +3.3V | `vcc_nodes=J1.3,U2 VIN,P1.9,C2,C5`；`3v3_nodes=U2 VOUT,U1.16,R1-R3,R6-R8,C1,C3,C4`；`ground_nodes=J1.4,P1.10,U1.8,U2.1` |
| 保护电路 | J1 与 P1 接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_current_limiter_shown=false` |
| 时钟 | 时钟电路 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 复位 | 复位与使能 | `reset_switch_shown=false`；`reset_net_shown=false`；`boot_net_shown=false`；`enable_net_shown=false` |
| 内存与 Flash | 存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |

## 待确认事项

- `address.documented-0x27`：产品正文列出默认 7 位 I2C 地址 0x27；原理图确认 A0=A1=A2 为高电平绑带，但页面未打印基地址或地址表，因此 0x27 需结合 PCA9554PW 数据手册或 I2C 扫描复核。（证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 U1 A0-A2 及 R6-R11；页面无地址数值标注）
- `power.documented-vcc-range`：产品正文描述 2.3-5.5V VCC 使用范围，但原理图仅显示 VCC 进入 HT7533 并输出 +3.3V，没有标注允许输入范围，需核对 HT7533 与整板电气规格。（证据：图 72a8b5e42cc0 / 第 1 页 / 第 1 页 J1 VCC 至 U2 VIN，图中无输入电压范围）
- `review.i2c-address`：请依据 PCA9554PW 数据手册或 I2C 扫描确认 A0=A1=A2=高对应 7 位地址 0x27。；原因：原理图显示地址脚绑带，但未直接标出地址基值或地址表。
- `review.vcc-range`：请依据 HT7533 数据手册和整板规格确认 J1 VCC 的 2.3-5.5V 允许范围。；原因：该范围来自产品正文，原理图页未标注输入电压上下限。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `72a8b5e42cc0b3a052e9859537196730bcdbcde689a1db6586ad48da4d09baca` | `https://static-cdn.m5stack.com/resource/docs/products/unit/extio/extio_sch_01.webp` |

---

源文档：`zh_CN/unit/extio.md`

源文档 SHA-256：`384eb1b155b515a039b915a31e030fc85953c4978a623ac3233ad3e7c9d80ad5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
