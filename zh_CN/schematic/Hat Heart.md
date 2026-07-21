# Hat Heart 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Heart |
| SKU | U118 |
| 产品 ID | `hat-heart-b9504abac304` |
| 源文档 | `zh_CN/hat/hat_heart_rate.md` |

## 概述

Hat Heart 以 U1 MAX30102EFD+ 完成光学心率/血氧传感，VLED+ 由 VCC_3V3 供电，数字核心由 U3 XC6206P182MR 产生的 VCC_1V8 供电。U2 TXS0102DCUR 在 SDA/SCL 的 1.8 V 与 3.3 V 网络之间进行电平转换，INT 通过 10 kΩ 上拉至 VCC_3V3。JP3 引出 HAT 侧电源、地、SCL、SDA 和 INT，JP1、JP2 另外提供五针信号引出。

## 检索关键词

`Hat Heart`、`U118`、`MAX30102EFD+`、`MAX30102`、`TXS0102DCUR`、`XC6206P182MR`、`I2C`、`0x57`、`SDA_1V8`、`SCL_1V8`、`SDA_3V3`、`SCL_3V3`、`SDA_HAT`、`SCL_HAT`、`INT`、`INT_HAT`、`VCC_1V8`、`VCC_3V3`、`VCC_3V3_HAT`、`GND`、`PGND`、`VLED+`、`JP1`、`JP2`、`JP3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX30102EFD+ | 光学心率和血氧传感器，连接 LED 电源、1.8 V 数字电源、I2C 与中断网络 | 图 42d1e5c11042 / 第 1 页 / 页面中央偏左 U1 方框，器件值 MAX30102EFD+，标有 VLED+、VDD、SCL、SDA、INT、PGND、GND 引脚 |
| U2 | TXS0102DCUR | SDA/SCL 的双通道 1.8 V 至 3.3 V 电平转换器 | 图 42d1e5c11042 / 第 1 页 / 页面左下 U2 TXS0102DCUR，A1/A2 连接 SDA_1V8/SCL_1V8，B1/B2 连接 SDA_3V3/SCL_3V3 |
| U3 | XC6206P182MR | 将 VCC_3V3 转换为 VCC_1V8 的稳压器 | 图 42d1e5c11042 / 第 1 页 / 页面左上 U3 XC6206P182MR，VDD pin 3 接 VCC_3V3，VOUT pin 2 接 VCC_1V8，GND pin 1 接 PGND |
| JP1 | 未标注 | VCC_3V3、GND、SCL_3V3、SDA_3V3 和 INT 五针引出接口 | 图 42d1e5c11042 / 第 1 页 / 页面中央偏右下 JP1 五针连接器，pin 1-5 旁标注 INT、SDA_3V3、SCL_3V3、GND、VCC_3V3 |
| JP2 | 未标注 | VCC_3V3_HAT、GND_HAT、SCL_HAT、SDA_HAT 和 INT_HAT 五针引出接口 | 图 42d1e5c11042 / 第 1 页 / 页面中央偏右上 JP2 五针连接器，pin 1-5 旁标注 INT_HAT、SDA_HAT、SCL_HAT、GND_HAT、VCC_3V3_HAT |
| JP3 | 未标注 | 八针 HAT 主机接口，引出 3.3 V 电源、地、I2C 和中断网络 | 图 42d1e5c11042 / 第 1 页 / 页面最右侧 JP3 八针连接器，标注 GND_HAT、SCL_HAT、INT_HAT、SDA_HAT、VCC_3V3_HAT，pin 1、3、7 无连接 |
| R1 | 10K/1% | INT 网络到 VCC_3V3 的上拉电阻 | 图 42d1e5c11042 / 第 1 页 / 页面上方 R1，左端 INT，右端 VCC_3V3，值 10K/1% |
| R2 | 0R/1% | GND 与 PGND 之间的零欧姆连接电阻 | 图 42d1e5c11042 / 第 1 页 / 页面上方 R2，左端 GND，右端 PGND，值 0R/1% |
| C1,C2,C5 | 104/6.3V/10% | VCC_1V8 到 GND 的电源去耦电容 | 图 42d1e5c11042 / 第 1 页 / 页面下方 C5、C1、C2 并联在 VCC_1V8 与 GND 之间，三者标注 104/6.3V/10% |
| C3,C4 | 106/6.3V/10% | U1 VLED+ 的 VCC_3V3 至 PGND 去耦电容 | 图 42d1e5c11042 / 第 1 页 / U1 左侧 C3、C4 并联在 VCC_3V3/VLED+ 与 PGND 之间，均标注 106/6.3V/10% |
| C6 | 104/6.3V/10% | U3 VCC_3V3 输入至 PGND 的去耦电容 | 图 42d1e5c11042 / 第 1 页 / 页面左上 U3 输入旁 C6，连接 VCC_3V3 与 PGND，值 104/6.3V/10% |

## 系统结构

### Hat Heart 系统架构

U1 MAX30102EFD+ 是传感器核心，U3 从 VCC_3V3 生成 VCC_1V8，U2 在 U1 的 1.8 V I2C 与 3.3 V I2C 网络之间转换电平，JP3 提供 HAT 侧电源、地、I2C 和中断连接。

- 参数与网络：`sensor=U1 MAX30102EFD+`；`level_shifter=U2 TXS0102DCUR`；`regulator=U3 XC6206P182MR`；`host_connector=JP3`；`digital_rails=VCC_1V8,VCC_3V3`
- 证据：图 42d1e5c11042 / 第 1 页 / 完整单页：中央 U1、左下 U2、左上 U3、右侧 JP1-JP3 功能区

## 电源

### U3 1.8 V 电源转换

U3 XC6206P182MR 的 VDD pin 3 接 VCC_3V3，VOUT pin 2 输出 VCC_1V8，GND pin 1 接 PGND；C6 104/6.3V/10% 从输入轨连接至 PGND。

- 参数与网络：`reference=U3`；`part_number=XC6206P182MR`；`input_pin=3/VDD`；`input_rail=VCC_3V3`；`output_pin=2/VOUT`；`output_rail=VCC_1V8`；`ground_pin=1/GND`；`ground_net=PGND`；`input_capacitor=C6 104/6.3V/10%`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面左上 U3、C6、VCC_3V3、VCC_1V8 和 PGND 区域

### U1 传感器供电

U1 的 VLED+ 由 VCC_3V3 供电，数字 VDD 由 VCC_1V8 供电；C3、C4 各为 106/6.3V/10%，并联在 VCC_3V3/VLED+ 与 PGND 之间。

- 参数与网络：`led_rail=VCC_3V3`；`led_pins=U1 pin 9,10`；`digital_rail=VCC_1V8`；`digital_pin=U1 pin 11`；`led_decoupling=C3 106/6.3V/10%,C4 106/6.3V/10%`
- 证据：图 42d1e5c11042 / 第 1 页 / U1 上方 VDD/VCC_1V8 和左侧 VLED+/VCC_3V3、C3、C4、PGND 连接

### VCC_1V8 去耦

C1、C2、C5 均标注 104/6.3V/10%，三者并联连接在 VCC_1V8 与 GND 之间。

- 参数与网络：`rail=VCC_1V8`；`ground=GND`；`capacitors=C1,C2,C5`；`value=104/6.3V/10%`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面下方 VCC_1V8 至 GND 的 C5、C1、C2 并联电容组

## 接口

### JP1 五针接口

JP1 pin 1 至 pin 5 依次连接 INT、SDA_3V3、SCL_3V3、GND、VCC_3V3。

- 参数与网络：`reference=JP1`；`pinout=1:INT,2:SDA_3V3,3:SCL_3V3,4:GND,5:VCC_3V3`；`i2c_level=3.3V`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面中央偏右下 JP1 的 pin 1-5 与左侧网络标注

### JP2 HAT 侧五针接口

JP2 pin 1 至 pin 5 依次连接 INT_HAT、SDA_HAT、SCL_HAT、GND_HAT、VCC_3V3_HAT。

- 参数与网络：`reference=JP2`；`pinout=1:INT_HAT,2:SDA_HAT,3:SCL_HAT,4:GND_HAT,5:VCC_3V3_HAT`；`supply_level=3.3V`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面中央偏右上 JP2 的 pin 1-5 与右侧 HAT 网络标注

### JP3 八针 HAT 主机接口

JP3 pin 2 连接 VCC_3V3_HAT，pin 4 连接 SDA_HAT，pin 5 连接 INT_HAT，pin 6 连接 SCL_HAT，pin 8 连接 GND_HAT；pin 1、3、7 未连接。

- 参数与网络：`reference=JP3`；`pinout=1:NC,2:VCC_3V3_HAT,3:NC,4:SDA_HAT,5:INT_HAT,6:SCL_HAT,7:NC,8:GND_HAT`；`supply_level=3.3V`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面最右侧 JP3 的 pin 1-8 与左侧 GND_HAT、SCL_HAT、INT_HAT、SDA_HAT、VCC_3V3_HAT 网络

## 总线

### U1 与主机侧 I2C 电平转换

U2 VCCA pin 3 和 OE pin 6 接 VCC_1V8，VCCB pin 7 接 VCC_3V3，GND pin 2 接 GND；A1 pin 5/B1 pin 8 连接 SDA_1V8 与 SDA_3V3，A2 pin 4/B2 pin 1 连接 SCL_1V8 与 SCL_3V3。

- 参数与网络：`translator=U2 TXS0102DCUR`；`a_rail=VCC_1V8`；`b_rail=VCC_3V3`；`output_enable=pin 6/OE to VCC_1V8`；`sda_path=U1 SDA_1V8 -> U2 A1 pin 5/B1 pin 8 -> SDA_3V3`；`scl_path=U1 SCL_1V8 -> U2 A2 pin 4/B2 pin 1 -> SCL_3V3`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面左下 U2 TXS0102DCUR 的 VCCA/VCCB/OE/GND、A1/A2/B1/B2 与四条 I2C 网络

## GPIO 与控制信号

### INT 中断网络

U1 INT pin 13 连接 INT 网络，R1 10K/1% 将 INT 上拉至 VCC_3V3；INT 同时引至 JP1 pin 1。

- 参数与网络：`sensor_pin=U1 pin 13/INT`；`net=INT`；`pullup=R1 10K/1%`；`pullup_rail=VCC_3V3`；`connector_pin=JP1 pin 1`
- 证据：图 42d1e5c11042 / 第 1 页 / U1 右侧 INT pin 13、页面上方 R1 和 JP1 pin 1 INT 网络

## 时钟

### 外部时钟可见性

该单页原理图未绘出独立晶体、谐振器或外部振荡器。

- 参数与网络：`external_clock_component_visible=false`；`schematic_pages_checked=1`
- 证据：图 42d1e5c11042 / 第 1 页 / 完整单页全部器件区域，无 Y/X 晶体、谐振器或振荡器位号

## 复位

### 复位、启动与调试网络可见性

该单页原理图未绘出复位、BOOT 或专用调试接口网络。

- 参数与网络：`reset_visible=false`；`boot_visible=false`；`debug_interface_visible=false`；`schematic_pages_checked=1`
- 证据：图 42d1e5c11042 / 第 1 页 / 完整单页 U1-U3 与 JP1-JP3 网络，未见 RESET、RST、BOOT、SWD、JTAG 或 UART 调试标注

## 保护电路

### 接口保护器件可见性

该单页原理图未绘出 TVS、ESD 二极管、保险丝或串联限流保护器件。

- 参数与网络：`tvs_visible=false`；`esd_diode_visible=false`；`fuse_visible=false`；`series_protection_visible=false`；`schematic_pages_checked=1`
- 证据：图 42d1e5c11042 / 第 1 页 / 完整单页电源和 JP1-JP3 接口区域，仅见 R1 上拉、R2 地连接及去耦电容

## 关键网络

### GND 与 PGND

R2 0R/1% 串接在 GND 与 PGND 之间；U1 PGND 和 LED 去耦使用 PGND，U1 数字 GND、U2 及 VCC_1V8 去耦使用 GND。

- 参数与网络：`link=R2 0R/1%`；`nets=GND,PGND`；`pgnd_users=U1 pin 4,C3,C4,U3 pin 1,C6`；`gnd_users=U1 pin 12,U2 pin 2,C1,C2,C5`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面上方 R2 GND-PGND 连接及 U1/U2/U3 与各去耦电容的地网络标注

## 传感器

### U1 MAX30102EFD+

U1 VLED+ pin 9、10 连接 VCC_3V3，PGND pin 4 连接 PGND，VDD pin 11 连接 VCC_1V8，GND pin 12 连接 GND；SCL pin 2、SDA pin 3 和 INT pin 13 分别连接 SCL_1V8、SDA_1V8 和 INT。

- 参数与网络：`reference=U1`；`part_number=MAX30102EFD+`；`vled_pins=9,10`；`vled_rail=VCC_3V3`；`pgnd_pin=4`；`vdd_pin=11`；`digital_rail=VCC_1V8`；`gnd_pin=12`；`scl_pin=2/SCL_1V8`；`sda_pin=3/SDA_1V8`；`interrupt_pin=13/INT`；`unconnected_pins=1,5,6,7,8,14`
- 证据：图 42d1e5c11042 / 第 1 页 / 页面中央偏左 U1 MAX30102EFD+ 全部引脚与网络标注

## 其他事实

### 其他功能分区可见性

该单页原理图未绘出独立存储器、外部存储、音频器件、射频器件或主控制器。

- 参数与网络：`storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_visible=false`；`controller_visible=false`；`schematic_pages_checked=1`
- 证据：图 42d1e5c11042 / 第 1 页 / 完整单页器件清单由传感器、电平转换器、稳压器、接口、电阻和电容构成

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Heart 系统架构 | `sensor=U1 MAX30102EFD+`；`level_shifter=U2 TXS0102DCUR`；`regulator=U3 XC6206P182MR`；`host_connector=JP3`；`digital_rails=VCC_1V8,VCC_3V3` |
| 传感器 | U1 MAX30102EFD+ | `reference=U1`；`part_number=MAX30102EFD+`；`vled_pins=9,10`；`vled_rail=VCC_3V3`；`pgnd_pin=4`；`vdd_pin=11`；`digital_rail=VCC_1V8`；`gnd_pin=12`；`scl_pin=2/SCL_1V8`；`sda_pin=3/SDA_1V8`；`interrupt_pin=13/INT`；`unconnected_pins=1,5,6,7,8,14` |
| 电源 | U3 1.8 V 电源转换 | `reference=U3`；`part_number=XC6206P182MR`；`input_pin=3/VDD`；`input_rail=VCC_3V3`；`output_pin=2/VOUT`；`output_rail=VCC_1V8`；`ground_pin=1/GND`；`ground_net=PGND`；`input_capacitor=C6 104/6.3V/10%` |
| 电源 | U1 传感器供电 | `led_rail=VCC_3V3`；`led_pins=U1 pin 9,10`；`digital_rail=VCC_1V8`；`digital_pin=U1 pin 11`；`led_decoupling=C3 106/6.3V/10%,C4 106/6.3V/10%` |
| 电源 | VCC_1V8 去耦 | `rail=VCC_1V8`；`ground=GND`；`capacitors=C1,C2,C5`；`value=104/6.3V/10%` |
| 总线 | U1 与主机侧 I2C 电平转换 | `translator=U2 TXS0102DCUR`；`a_rail=VCC_1V8`；`b_rail=VCC_3V3`；`output_enable=pin 6/OE to VCC_1V8`；`sda_path=U1 SDA_1V8 -> U2 A1 pin 5/B1 pin 8 -> SDA_3V3`；`scl_path=U1 SCL_1V8 -> U2 A2 pin 4/B2 pin 1 -> SCL_3V3` |
| 总线地址 | MAX30102 I2C 地址 | `documented_address=0x57`；`schematic_address_visible=false` |
| GPIO 与控制信号 | INT 中断网络 | `sensor_pin=U1 pin 13/INT`；`net=INT`；`pullup=R1 10K/1%`；`pullup_rail=VCC_3V3`；`connector_pin=JP1 pin 1` |
| 接口 | JP1 五针接口 | `reference=JP1`；`pinout=1:INT,2:SDA_3V3,3:SCL_3V3,4:GND,5:VCC_3V3`；`i2c_level=3.3V` |
| 接口 | JP2 HAT 侧五针接口 | `reference=JP2`；`pinout=1:INT_HAT,2:SDA_HAT,3:SCL_HAT,4:GND_HAT,5:VCC_3V3_HAT`；`supply_level=3.3V` |
| 接口 | JP3 八针 HAT 主机接口 | `reference=JP3`；`pinout=1:NC,2:VCC_3V3_HAT,3:NC,4:SDA_HAT,5:INT_HAT,6:SCL_HAT,7:NC,8:GND_HAT`；`supply_level=3.3V` |
| 关键网络 | GND 与 PGND | `link=R2 0R/1%`；`nets=GND,PGND`；`pgnd_users=U1 pin 4,C3,C4,U3 pin 1,C6`；`gnd_users=U1 pin 12,U2 pin 2,C1,C2,C5` |
| 时钟 | 外部时钟可见性 | `external_clock_component_visible=false`；`schematic_pages_checked=1` |
| 复位 | 复位、启动与调试网络可见性 | `reset_visible=false`；`boot_visible=false`；`debug_interface_visible=false`；`schematic_pages_checked=1` |
| 保护电路 | 接口保护器件可见性 | `tvs_visible=false`；`esd_diode_visible=false`；`fuse_visible=false`；`series_protection_visible=false`；`schematic_pages_checked=1` |
| 其他事实 | 其他功能分区可见性 | `storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_visible=false`；`controller_visible=false`；`schematic_pages_checked=1` |

## 待确认事项

- `address.documented-i2c`：原理图未打印 I2C 地址；产品正文记载 0x57，但无法仅由本页电路图确认该地址。（证据：图 42d1e5c11042 / 第 1 页 / U1 SCL/SDA 与 U2 电平转换区域未见地址数值或地址选择网络）
- `review.i2c-address`：Hat Heart 所用 MAX30102 的 I2C 从机地址是否确认为产品正文记载的 0x57？；原因：原理图只显示 SCL/SDA 的物理连接和电平转换，没有打印地址值或地址选择网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `42d1e5c1104293db4490ae08342f929d93b24b2829892096c7fa2b84e853e420` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_sch_01.webp` |

---

源文档：`zh_CN/hat/hat_heart_rate.md`

源文档 SHA-256：`1505eb7a5167af3a120c4d28f2b31d465ca5a026cf9c2998e46bf9e6a4596625`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
