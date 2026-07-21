# Faces Gamepad 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces Gamepad |
| SKU | A004 |
| 产品 ID | `faces-gamepad-9d8f13459df2` |
| 源文档 | `zh_CN/module/faces_gameboy.md` |

## 概述

Faces Gamepad 以 U1 ATmega328P-AU 为控制器，S1 至 S8 八个按键分别连接 PB0 至 PB7，并在按下时接至 GND。BUS1 M5_BUS 24 针连接器提供 3V3、GND、SDA/SCL、G5 以及两条 16/17 串口网络；U1 PC4/PC5 连接 I2C，PD0/PD1 经 10kΩ 电阻连接串口网络。电路未绘出外部晶振，PB6/PB7 原晶振复用引脚用于 SELECT/START 按键，P1 Header 6 另引出 RIGHT、A、B、RESET 等信号。

## 检索关键词

`Faces Gamepad`、`A004`、`ATmega328P-AU`、`ATmega328`、`I2C`、`0x08`、`SDA`、`SCL`、`UP`、`DOWN`、`LEFT`、`RIGHT`、`SELECT`、`START`、`A`、`B`、`PB0`、`PB1`、`PB2`、`PB3`、`PB4`、`PB5`、`PB6`、`PB7`、`G5`、`RXD`、`TXD`、`RESET`、`M5_BUS 24 PIN`、`Header 6`、`ISP`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ATmega328P-AU | 八按键扫描、I2C 和串口通信控制器 | 图 e3dbc484d0f5 / 第 1 页 / 页面左中 U1 方框，器件值 ATmega328P-AU，标注 PC0-PC6、PD0-PD7、PB0-PB7、VCC/AVCC/GND |
| BUS1 | M5_BUS 24 PIN | FACES 面板电源、I2C、串口与 GPIO 总线接口 | 图 e3dbc484d0f5 / 第 1 页 / 页面左上 BUS1 M5_BUS，pin 1-22 可见，板内连线接 GND、3V3、16、17、SDA、SCL、G5 |
| S1-S8 | 未标注 | UP、DOWN、LEFT、RIGHT、A、B、SELECT、START 八个对地按键 | 图 e3dbc484d0f5 / 第 1 页 / 页面下半 S1 UP、S2 DOWN、S3 LEFT、S4 RIGHT、S5 A、S6 B、S7 SELECT、S8 START 与公共 GND |
| P1 | Header 6 | 六针辅助连接器，可见引出 RIGHT、A、B 和 RESET 相关线路 | 图 e3dbc484d0f5 / 第 1 页 / 页面下方中部 P1 Header 6，pin 1-4 接右侧按键/RESET 线路，pin 5-6 无可见外部连线 |
| R1 | 10K | U1 PC0/G5 网络到 3V3 的上拉电阻 | 图 e3dbc484d0f5 / 第 1 页 / U1 右上 PC0/pin 23 的 G5 网络经 R1 10K 接 3V3 |
| R2,R3 | 10K; 10K | U1 PD0/PD1 到 BUS1 16/17 串口网络的串联电阻 | 图 e3dbc484d0f5 / 第 1 页 / U1 右侧 PD0/pin 30、PD1/pin 31 经 R2/R3 10K 分别连接网络 16、17 |

## 系统结构

### Faces Gamepad 系统架构

U1 ATmega328P-AU 直接采集八个对地按键，通过 BUS1 提供的 3V3/GND 供电，并经 SDA/SCL I2C、16/17 串口网络和 G5 GPIO 与 FACES 底座连接。

- 参数与网络：`controller=U1 ATmega328P-AU`；`buttons=S1-S8`；`button_count=8`；`host_connector=BUS1 M5_BUS`；`host_buses=I2C,UART`；`auxiliary_gpio=G5`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 完整单页 BUS1、U1、S1-S8、P1 与 R1-R3 功能区

## 电源

### U1 3V3 供电

BUS1 pin 4 的 3V3 连接 U1 VCC pin 4、pin 6 与 AVCC pin 18；U1 GND pin 3、pin 5、pin 21 连接 GND，BUS1 pin 1 也连接 GND。

- 参数与网络：`rail=3V3`；`bus_pin=BUS1 pin 4`；`mcu_supply_pins=U1 VCC pin 4,6; AVCC pin 18`；`ground_pins=U1 pin 3,5,21; BUS1 pin 1`
- 证据：图 e3dbc484d0f5 / 第 1 页 / BUS1 3V3/GND 与 U1 左侧 VCC/AVCC/GND 引脚布线

## 接口

### P1 Header 6 可见连接

P1 pin 1、2、3 分别接与 RIGHT、A、B 按键同网的 PB3、PB4、PB5 线路，pin 4 接 RESET，pin 5、6 在本页无外部连线。

- 参数与网络：`reference=P1 Header 6`；`visible_pinout=1:PB3/RIGHT,2:PB4/A,3:PB5/B,4:RESET,5:NC,6:NC`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 页面下方 P1 pin 1-6 与左侧 PB3/PB4/PB5/RESET 线路和右侧 S4/S5/S6

### BUS1 已用针脚

BUS1 pin 1 连接 GND，pin 4 连接 3V3，pin 12、14 分别连接 16、17 串口网络，pin 16 连接 SDA，pin 18 连接 SCL，pin 22 连接 G5；其余可见针脚在本页无板内连线。

- 参数与网络：`used_pinout=1:GND,4:3V3,12:R2/16,14:T2/17,16:SDA,18:SCL,22:G5`；`connector=BUS1 M5_BUS 24 PIN`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 页面左上 BUS1 的外部蓝色网络连线与 pin 1/4/12/14/16/18/22

## 总线

### U1 与 BUS1 的 I2C

U1 PC4/ADC4/SDA/pin 27 连接 BUS1 pin 16 SDA，U1 PC5/ADC5/SCL/pin 28 连接 BUS1 pin 18 SCL；本页未绘出 SDA/SCL 上拉电阻。

- 参数与网络：`controller=U1`；`sda_mcu_pin=PC4/pin 27`；`sda_bus_pin=BUS1 pin 16`；`scl_mcu_pin=PC5/pin 28`；`scl_bus_pin=BUS1 pin 18`；`logic_rail=3V3`；`pullups_visible=false`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 PC4/SDA、PC5/SCL 与 BUS1 pin 16 SDA、pin 18 SCL

### U1 UART 到 BUS1 16/17 网络

U1 PD0/RXD/pin 30 经 R2 10K 连接网络 16，对应 BUS1 pin 12 R2/16；U1 PD1/TXD/pin 31 经 R3 10K 连接网络 17，对应 BUS1 pin 14 T2/17。

- 参数与网络：`rx_path=U1 PD0/RXD pin 30 -> R2 10K -> net 16 -> BUS1 pin 12`；`tx_path=U1 PD1/TXD pin 31 -> R3 10K -> net 17 -> BUS1 pin 14`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 PD0/PD1、R2/R3、16/17 网络与 BUS1 pin 12/pin 14

## GPIO 与控制信号

### 八按键 GPIO 映射

U1 PB0/pin 12 接 S1 UP，PB1/pin 13 接 S2 DOWN，PB2/pin 14 接 S3 LEFT，PB3/pin 15 接 S4 RIGHT，PB4/pin 16 接 S5 A，PB5/pin 17 接 S6 B，PB6/pin 7 接 S7 SELECT，PB7/pin 8 接 S8 START；每个按键另一端接 GND。

- 参数与网络：`UP=S1/PB0 pin 12`；`DOWN=S2/PB1 pin 13`；`LEFT=S3/PB2 pin 14`；`RIGHT=S4/PB3 pin 15`；`A=S5/PB4 pin 16`；`B=S6/PB5 pin 17`；`SELECT=S7/PB6 pin 7`；`START=S8/PB7 pin 8`；`active_connection=GND`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 页面下半 U1 PB0-PB7 至 S1-S8 及左右公共 GND 连线

### G5 GPIO

U1 PC0/ADC0/PCINT8/pin 23 连接 G5，G5 引至 BUS1 pin 22，并由 R1 10K 上拉至 3V3。

- 参数与网络：`mcu_pin=U1 PC0/pin 23`；`net=G5`；`bus_pin=BUS1 pin 22`；`pullup=R1 10K to 3V3`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 PC0/G5、R1 10K/3V3 与 BUS1 pin 22 G5

### U1 PC1-PC3 网络

U1 PC1/pin 24、PC2/pin 25、PC3/pin 26 分别引出标注为 01、03、02 的网络，本页未显示这些网络的其他连接。

- 参数与网络：`PC1=pin 24/net 01`；`PC2=pin 25/net 03`；`PC3=pin 26/net 02`；`additional_connections_visible=false`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 右侧 PC1-PC3 pin 24-26 与 01/03/02 短网络标注

## 时钟

### U1 时钟源可见性

U1 PB6/XTAL1/pin 7 和 PB7/XTAL2/pin 8 分别用于 SELECT、START 按键，原理图未绘出独立晶体、谐振器或外部振荡器。

- 参数与网络：`xtal1_pin=PB6/pin 7 -> S7 SELECT`；`xtal2_pin=PB7/pin 8 -> S8 START`；`external_clock_visible=false`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 PB6/XTAL1、PB7/XTAL2 到 S7/S8 按键线路，完整单页无 Y/X 位号

## 复位

### U1 RESET

U1 PC6/RESET/pin 29 连接 RESET 网络，RESET 引至 P1 Header 6 pin 4；本页未绘出 RESET 上拉电阻或对地电容。

- 参数与网络：`mcu_pin=U1 PC6/RESET pin 29`；`net=RESET`；`connector_pin=P1 pin 4`；`pullup_visible=false`；`capacitor_visible=false`
- 证据：图 e3dbc484d0f5 / 第 1 页 / U1 PC6/RESET pin 29 到 P1 pin 4 的 RESET 水平线路

## 保护电路

### 电源和外部接口保护可见性

该页未绘出保险丝、TVS、ESD、反接或其他专用保护器件。

- 参数与网络：`fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 完整单页 BUS1、U1、按键和 P1 外围器件

## 其他事实

### 其他功能分区可见性

该页未绘出独立存储器、外部存储、音频器件、传感器、射频器件或专用模拟前端；ADC6/pin 19、ADC7/pin 22 和 AREF/pin 20 无外部连线。

- 参数与网络：`external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`analog_frontend_visible=false`；`unused_analog_pins=ADC6 pin 19,ADC7 pin 22,AREF pin 20`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 完整单页及 U1 ADC6/ADC7/AREF 悬空引脚

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces Gamepad 系统架构 | `controller=U1 ATmega328P-AU`；`buttons=S1-S8`；`button_count=8`；`host_connector=BUS1 M5_BUS`；`host_buses=I2C,UART`；`auxiliary_gpio=G5` |
| 电源 | U1 3V3 供电 | `rail=3V3`；`bus_pin=BUS1 pin 4`；`mcu_supply_pins=U1 VCC pin 4,6; AVCC pin 18`；`ground_pins=U1 pin 3,5,21; BUS1 pin 1` |
| 总线 | U1 与 BUS1 的 I2C | `controller=U1`；`sda_mcu_pin=PC4/pin 27`；`sda_bus_pin=BUS1 pin 16`；`scl_mcu_pin=PC5/pin 28`；`scl_bus_pin=BUS1 pin 18`；`logic_rail=3V3`；`pullups_visible=false` |
| 总线地址 | I2C 从机地址 | `documented_address=0x08`；`schematic_address_visible=false` |
| GPIO 与控制信号 | 八按键 GPIO 映射 | `UP=S1/PB0 pin 12`；`DOWN=S2/PB1 pin 13`；`LEFT=S3/PB2 pin 14`；`RIGHT=S4/PB3 pin 15`；`A=S5/PB4 pin 16`；`B=S6/PB5 pin 17`；`SELECT=S7/PB6 pin 7`；`START=S8/PB7 pin 8`；`active_connection=GND` |
| 总线 | U1 UART 到 BUS1 16/17 网络 | `rx_path=U1 PD0/RXD pin 30 -> R2 10K -> net 16 -> BUS1 pin 12`；`tx_path=U1 PD1/TXD pin 31 -> R3 10K -> net 17 -> BUS1 pin 14` |
| GPIO 与控制信号 | G5 GPIO | `mcu_pin=U1 PC0/pin 23`；`net=G5`；`bus_pin=BUS1 pin 22`；`pullup=R1 10K to 3V3` |
| GPIO 与控制信号 | U1 PC1-PC3 网络 | `PC1=pin 24/net 01`；`PC2=pin 25/net 03`；`PC3=pin 26/net 02`；`additional_connections_visible=false` |
| 复位 | U1 RESET | `mcu_pin=U1 PC6/RESET pin 29`；`net=RESET`；`connector_pin=P1 pin 4`；`pullup_visible=false`；`capacitor_visible=false` |
| 接口 | P1 Header 6 可见连接 | `reference=P1 Header 6`；`visible_pinout=1:PB3/RIGHT,2:PB4/A,3:PB5/B,4:RESET,5:NC,6:NC` |
| 调试与烧录 | P1 与 ISP 下载接口关系 | `documented_function=Mega328 ISP download`；`schematic_connector=P1 Header 6`；`visible_signals=PB3/RIGHT,PB4/A,PB5/B,RESET,NC,NC`；`standard_isp_labels_visible=false` |
| 时钟 | U1 时钟源可见性 | `xtal1_pin=PB6/pin 7 -> S7 SELECT`；`xtal2_pin=PB7/pin 8 -> S8 START`；`external_clock_visible=false` |
| 接口 | BUS1 已用针脚 | `used_pinout=1:GND,4:3V3,12:R2/16,14:T2/17,16:SDA,18:SCL,22:G5`；`connector=BUS1 M5_BUS 24 PIN` |
| 保护电路 | 电源和外部接口保护可见性 | `fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`analog_frontend_visible=false`；`unused_analog_pins=ADC6 pin 19,ADC7 pin 22,AREF pin 20` |

## 待确认事项

- `address.documented-i2c`：原理图未打印 I2C 从机地址；产品正文记载 0x08，但无法仅由本页硬件图确认固件地址。（证据：图 e3dbc484d0f5 / 第 1 页 / U1 PC4/PC5 与 BUS1 SDA/SCL 区域未见地址数值或地址配置器件）
- `debug.isp-identity`：产品正文提到 Mega328 ISP 下载接口，但本地原理图中的 P1 Header 6 可见连接为 RIGHT、A、B、RESET 等，未显示标准名称的 MOSI、MISO、SCK、VCC、GND 六线 ISP 定义。（证据：图 e3dbc484d0f5 / 第 1 页 / 页面下方 P1 Header 6 与其 pin 1-6 可见线路）
- `review.i2c-address`：Faces Gamepad 当前固件的 I2C 从机地址是否确认为产品正文记载的 0x08？；原因：原理图只显示 SDA/SCL 物理连接，没有地址数值、地址拨码或固件定义。
- `review.isp-connector`：ISP 下载接口是否为本页 P1，若是，其正确 MOSI/MISO/SCK/VCC/GND/RESET 针脚映射是什么？；原因：本页 P1 的可见线路与标准六线 ISP 标注不一致，产品正文所示 ISP 图并未包含在本地原理图资源中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e3dbc484d0f5e689549aa58c2e59c8aaeffb51489be197ffd2d8bf68ec463743` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_sch_01.webp` |

---

源文档：`zh_CN/module/faces_gameboy.md`

源文档 SHA-256：`88d9f356978950e6e496bb284f525b05240b5d5daa21118af9e478b888b10b90`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
