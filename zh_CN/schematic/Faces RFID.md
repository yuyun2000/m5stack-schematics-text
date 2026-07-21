# Faces RFID 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces RFID |
| SKU | A067 |
| 产品 ID | `faces-rfid-a8dde6d671f3` |
| 源文档 | `zh_CN/module/faces_rfid.md` |

## 概述

Faces RFID 的现有资源是一页两连接器直连图：J1 M5_BUS_22P 的 SDA/SCL 通过 RC522_SDA/RC522_SCL 网络连接 P1 Header 4，J1 的 3V3 与 GND 同时送到 P1。页面没有绘制 RFID 控制器、天线、射频匹配、复位、中断、时钟、保护或电源转换器。产品正文所述 MFRC522、I2C 地址 0x28、13.56 MHz、I2C 速率和支持协议无法由本页独立确认。

## 检索关键词

`Faces RFID`、`A067`、`J1`、`M5_BUS_22P`、`P1`、`Header 4`、`RC522_SDA`、`RC522_SCL`、`SDA`、`SCL`、`I2C`、`3V3`、`+3.3V`、`GND`、`MFRC522`、`0x28`、`13.56MHz`、`ISO14443A`、`MIFARE`、`NTAG`、`400Kbit/s`、`3400Kbit/s`、`RFID`、`RF antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | M5_BUS_22P | Faces 面板总线连接器；本页使用 GND、3V3、SDA 和 SCL 连接 P1 | 图 f6f1dfb8edf3 / 第 1 页 / 第 1 页左侧 J1 M5_BUS_22P，1~22 脚及 RC522_SDA/RC522_SCL、+3.3V、GND 外部连线 |
| P1 | Header 4 | 四针 RFID 子板接口，引出 RC522_SCL、RC522_SDA、+3.3V 和 GND | 图 f6f1dfb8edf3 / 第 1 页 / 第 1 页右侧 P1 Header 4，1~4 脚与四条外部网络 |

## 系统结构

### Faces RFID 连接架构

当前页面仅展示 J1 M5_BUS_22P 到 P1 Header 4 的 I2C 与电源直连，不包含 RFID 芯片或天线电路。

- 参数与网络：`host_connector=J1 M5_BUS_22P`；`rfid_connector=P1 Header 4`；`signals=RC522_SCL,RC522_SDA,+3.3V,GND`；`rfid_ic_shown=false`；`antenna_shown=false`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页全图，仅有 J1、P1 及四条同名网络

## 电源

### +3.3V 供电

J1.3 的 3V3 网络标为 +3.3V，P1.3 同样接 +3.3V；J1.2 与 P1.4 均接 GND。页面未显示稳压器、负载开关、充电器或电池路径。

- 参数与网络：`source=J1.3 3V3`；`destination=P1.3 +3.3V`；`ground_host=J1.2`；`ground_device=P1.4`；`local_regulator_shown=false`；`load_switch_shown=false`；`charger_shown=false`；`battery_path_shown=false`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 J1.3 +3.3V、J1.2 GND 与 P1.3 +3.3V、P1.4 GND；全图无电源 IC

## 接口

### J1 已用针脚

J1.2 接 GND，J1.3 接 +3.3V，J1.15 的 SDA 接 RC522_SDA，J1.17 的 SCL 接 RC522_SCL。

- 参数与网络：`pin_2=GND`；`pin_3=+3.3V`；`pin_15=SDA / RC522_SDA`；`pin_17=SCL / RC522_SCL`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 J1：2 GND、3 3V3 的外部电源符号，以及 15 SDA/RC522_SDA、17 SCL/RC522_SCL

### P1 Header 4

P1.1 接 RC522_SCL，P1.2 接 RC522_SDA，P1.3 接 +3.3V，P1.4 接 GND。

- 参数与网络：`pin_1=RC522_SCL`；`pin_2=RC522_SDA`；`pin_3=+3.3V`；`pin_4=GND`；`signal_level=3.3V supply shown; I2C logic level not separately annotated`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 P1 左侧由上至下 RC522_SCL、RC522_SDA、+3.3V、GND 对应 1~4 脚

## 总线

### RC522 I2C 网络

RC522_SDA 将 J1.15 SDA 与 P1.2 相连，RC522_SCL 将 J1.17 SCL 与 P1.1 相连；页面未显示上拉电阻或其他 I2C 设备。

- 参数与网络：`controller_side=J1`；`device_side=P1`；`sda_path=J1.15 SDA -> RC522_SDA -> P1.2`；`scl_path=J1.17 SCL -> RC522_SCL -> P1.1`；`pullups_shown=false`；`other_devices_shown=false`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 J1 右侧与 P1 左侧的 RC522_SDA/RC522_SCL 同名网络

## GPIO 与控制信号

### RFID 复位、中断与片选

P1 仅有 SCL、SDA、+3.3V、GND 四线，页面未展示 RFID RESET、IRQ、NSS/CS、使能或其他 GPIO 控制线。

- 参数与网络：`reset_shown=false`；`irq_shown=false`；`chip_select_shown=false`；`enable_shown=false`；`p1_signals=RC522_SCL,RC522_SDA,+3.3V,GND`
- 证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 P1 Header 4 的全部四脚与全图网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces RFID 连接架构 | `host_connector=J1 M5_BUS_22P`；`rfid_connector=P1 Header 4`；`signals=RC522_SCL,RC522_SDA,+3.3V,GND`；`rfid_ic_shown=false`；`antenna_shown=false` |
| 接口 | J1 已用针脚 | `pin_2=GND`；`pin_3=+3.3V`；`pin_15=SDA / RC522_SDA`；`pin_17=SCL / RC522_SCL` |
| 接口 | P1 Header 4 | `pin_1=RC522_SCL`；`pin_2=RC522_SDA`；`pin_3=+3.3V`；`pin_4=GND`；`signal_level=3.3V supply shown; I2C logic level not separately annotated` |
| 总线 | RC522 I2C 网络 | `controller_side=J1`；`device_side=P1`；`sda_path=J1.15 SDA -> RC522_SDA -> P1.2`；`scl_path=J1.17 SCL -> RC522_SCL -> P1.1`；`pullups_shown=false`；`other_devices_shown=false` |
| 电源 | +3.3V 供电 | `source=J1.3 3V3`；`destination=P1.3 +3.3V`；`ground_host=J1.2`；`ground_device=P1.4`；`local_regulator_shown=false`；`load_switch_shown=false`；`charger_shown=false`；`battery_path_shown=false` |
| 总线地址 | 正文中的 I2C 地址 | `documented_address=0x28`；`address_on_schematic=null`；`address_straps_shown=false`；`device_ic_shown=false` |
| 核心器件 | 正文中的 MFRC522 | `documented_part=MFRC522`；`schematic_part_number=null`；`reference=null`；`package=null`；`visible_relation=RC522_SDA/RC522_SCL net names only` |
| 射频 | 正文中的 RFID 射频参数 | `documented_frequency=13.56MHz`；`documented_protocols=ISO14443A,MIFARE,NTAG`；`antenna_shown=false`；`matching_network_shown=false`；`rf_clock_shown=false` |
| 总线 | 正文中的 I2C 速率 | `documented_fast_mode=400Kbit/s`；`documented_high_speed_mode=3400Kbit/s`；`speed_on_schematic=null`；`pullup_resistance=null`；`bus_capacitance=null` |
| GPIO 与控制信号 | RFID 复位、中断与片选 | `reset_shown=false`；`irq_shown=false`；`chip_select_shown=false`；`enable_shown=false`；`p1_signals=RC522_SCL,RC522_SDA,+3.3V,GND` |
| 保护电路 | I2C、电源与射频保护 | `i2c_esd_shown=false`；`series_resistors_shown=false`；`decoupling_shown=false`；`power_protection_shown=false`；`antenna_protection_shown=false` |
| 时钟 | RFID 时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net=null`；`frequency=null` |
| 内存与 Flash | 存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`storage_interface_shown=false`；`storage_part_number=null` |

## 待确认事项

- `address.documented-0x28`：产品正文给出 I2C 地址 0x28，但页面没有 RFID 控制器、地址配置引脚、电阻或 0x28 标注，因此地址无法由本页确认。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页仅有 J1/P1 与 RC522_SDA/RC522_SCL 网络，无 0x28 或地址电路）
- `component.documented-mfrc522`：产品正文称模块内置 MFRC522，但当前页面没有 MFRC522 器件符号、位号、封装或引脚，仅以 RC522_SDA/RC522_SCL 网络名指向 P1。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页全图无 IC，仅 J1 与 P1；网络名含 RC522）
- `rf.documented-frequency-protocols`：产品正文列出 13.56MHz，并声称支持 ISO14443A、MIFARE 和 NTAG；当前页面没有射频振荡器、天线、匹配网络或协议标注，无法从原理图证实这些参数。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页全图无天线、线圈、射频匹配器件或 13.56MHz 标注）
- `bus.documented-i2c-speeds`：产品正文列出快速模式最高 400Kbit/s、高速模式最高 3400Kbit/s；当前页面只有 SDA/SCL 直连，未给出控制器能力、上拉阻值、总线电容或速率标注。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页 RC522_SDA/RC522_SCL 仅为无外围元件的连接线）
- `protection.interface-not-visible`：页面未展示 SDA/SCL ESD、串联电阻、电源去耦、反接/过流保护、天线 ESD 或射频限幅器件，无法判断 RFID 子板是否另有这些电路。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页完整图仅有两连接器和直连网络，无无源或保护器件）
- `clock.rfid-clock-not-visible`：页面未显示晶振、谐振器、外部时钟网络或任何时钟频率，RFID 控制器的数字时钟实现无法确认。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页全图无时钟器件或时钟网络）
- `storage-memory.not-visible`：页面未展示独立 Flash、EEPROM、RAM 或存储接口；产品正文的数据保存时间描述无法映射到本页中的任何存储器件。（证据：图 f6f1dfb8edf3 / 第 1 页 / 第 1 页完整图无存储器件或存储总线）
- `review.i2c-address`：请通过 A067 当前固件、协议或 RFID 子板原理图确认 7-bit I2C 地址是否为 0x28，是否可配置。；原因：当前连接图没有地址标注或地址配置电路。
- `review.rfid-controller`：请提供 RFID 子板正式原理图或 BOM，确认控制器是否为 MFRC522，以及位号、封装和接口模式。；原因：当前页面未画 RFID 控制器，仅网络名含 RC522。
- `review.rf-parameters`：请确认 A067 当前射频频率、天线与匹配网络，以及 ISO14443A、MIFARE、NTAG 的实际支持范围。；原因：当前页面没有任何射频前端或协议证据。
- `review.i2c-speeds`：请通过控制器 datasheet、固件和总线设计确认 400Kbit/s 与 3400Kbit/s 模式是否均受支持。；原因：仅凭 SDA/SCL 直连无法证明设备协议能力和板级信号完整性。
- `review.interface-protection`：请确认 RFID 子板是否包含 I2C 上拉/保护、电源去耦与保护、天线 ESD 和射频限幅器件。；原因：当前连接页可能省略 P1 之后的整个 RFID 子板电路。
- `review.rfid-clock`：请确认 RFID 控制器的晶振或时钟源、频率和连接网络。；原因：当前页面完全未展示 RFID 芯片及时钟电路。
- `review.storage`：正文中的数据保存时间对应 RFID 标签特性还是板载存储器，A067 是否存在独立存储器件？；原因：当前页面无任何存储器，无法把数据保存参数归属到具体硬件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f6f1dfb8edf32487a2d03f4edb0c9d892c7e2538601b81098c111c191cffe00b` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_rfid/faces_rfid_sch_01.webp` |

---

源文档：`zh_CN/module/faces_rfid.md`

源文档 SHA-256：`39389de80ff93f0ec07bcba1da85c568f1a11a1c307e7a25cda463ab1e10e132`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
