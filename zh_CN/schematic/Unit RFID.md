# Unit RFID 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RFID |
| SKU | U031 |
| 产品 ID | `unit-rfid-a52b2b4084a4` |
| 源文档 | `zh_CN/unit/rfid.md` |

## 概述

Unit RFID 由 M1（原理图标注 RC522）射频模块、HT7533 稳压器和四针 I2C 接口组成。J1 输入 +5V，HT7533 生成 +3.3V 为 M1 供电；J1 的 IIC_SCL/IIC_SDA 分别连接 M1.SCL/M1.SDA，并各由 4.7KΩ 电阻上拉到 +5V。M1 的 RST 与 IRQ 未接外部网络，原理图没有展开射频天线、匹配、时钟或地址配置。

## 检索关键词

`Unit RFID`、`U031`、`RC522`、`MFRC522`、`M1`、`HT7533`、`U1`、`I2C`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`0x28`、`13.56MHz`、`RST`、`IRQ`、`IIC_Socket_4P`、`J1`、`+5V`、`+3.3V`、`R1`、`R2`、`4.7KΩ`、`C1`、`100nF`、`C2`、`10uF`、`C3`、`ISO14443A`、`MIFARE`、`NTAG`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | RC522 | RFID 模块，使用 +3.3V/GND 供电并引出 RST、SCL、SDA、IRQ | 图 d2e0a9b51514 / 第 1 页 / 页面左上：M1 模块框内标注 RFID、下方 RC522，1~6 脚为 3.3V/GND/RST/SCL/SDA/IRQ |
| U1 | HT7533 | 将 J1 输入的 +5V 转换为 +3.3V 供 M1 | 图 d2e0a9b51514 / 第 1 页 / 页面下中：U1 HT7533，VIN.2 接 +5V、VOUT.3 接 +3.3V、GND.1 接地 |
| J1 | IIC_Socket_4P | 上游 I2C 与 +5V/GND 接口 | 图 d2e0a9b51514 / 第 1 页 / 页面右上：J1 IIC_Socket_4P，1~4 脚标注 IIC_SCL、IIC_SDA、VCC、GND |
| R1 | 4.7KΩ | IIC_SCL/SCL 到 +5V 的上拉电阻 | 图 d2e0a9b51514 / 第 1 页 / 页面上中：R1 4.7KΩ 从 +5V 接至 M1.SCL/J1.1 网络 |
| R2 | 4.7KΩ | IIC_SDA/SDA 到 +5V 的上拉电阻 | 图 d2e0a9b51514 / 第 1 页 / 页面上中：R2 4.7KΩ 从 +5V 接至 M1.SDA/J1.2 网络 |
| C1 | 100nF | +3.3V 输出高频去耦电容 | 图 d2e0a9b51514 / 第 1 页 / 页面左下：C1 100nF 从 +3.3V 接至 GND |
| C2 | 10uF | +3.3V 输出储能/滤波电容 | 图 d2e0a9b51514 / 第 1 页 / 页面下中偏左：C2 10uF 从 +3.3V 接至 GND |
| C3 | 10uF | +5V 输入滤波电容 | 图 d2e0a9b51514 / 第 1 页 / 页面下中偏右：C3 10uF 从 +5V 接至 GND |

## 系统结构

### Unit RFID

J1 提供 +5V 和 I2C 信号，U1 将 +5V 转为 +3.3V，M1 RC522 使用 +3.3V 供电并通过 SCL/SDA 连接 J1。

- 参数与网络：`module=M1 RC522`；`interface=J1 IIC_Socket_4P`；`input_rail=+5V`；`module_rail=+3.3V`；`regulator=U1 HT7533`；`bus=I2C`
- 证据：图 d2e0a9b51514 / 第 1 页 / 全页：J1-U1-M1 以及 +5V/+3.3V/SCL/SDA/GND 的完整连接

## 核心器件

### M1 RC522

M1.1 为 3.3V、M1.2 为 GND、M1.3 为 RST、M1.4 为 SCL、M1.5 为 SDA、M1.6 为 IRQ。

- 参数与网络：`pin_1=3.3V`；`pin_2=GND`；`pin_3=RST`；`pin_4=SCL`；`pin_5=SDA`；`pin_6=IRQ`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面左上：M1 右侧 1~6 脚及 3.3V/GND/RST/SCL/SDA/IRQ 名称

## 电源

### U1 HT7533

U1.VIN.2 接 +5V，U1.GND.1 接 GND，U1.VOUT.3 输出 +3.3V；+5V 端有 C3（10uF），+3.3V 端有 C1（100nF）和 C2（10uF）。

- 参数与网络：`input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C3 10uF`；`output_capacitors=C1 100nF, C2 10uF`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面下半：U1 HT7533、C1/C2/C3 与 +5V/+3.3V/GND 的连接

## 接口

### J1

J1.1 IIC_SCL 接 M1.SCL.4，J1.2 IIC_SDA 接 M1.SDA.5，J1.3 VCC 接 +5V，J1.4 GND 接地。

- 参数与网络：`connector=IIC_Socket_4P`；`pin_1=IIC_SCL / M1.4 SCL`；`pin_2=IIC_SDA / M1.5 SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面上半：J1.1~J1.4 与 M1.4/M1.5、+5V、GND 的连线

## 总线

### J1 与 M1

J1.IIC_SCL 与 M1.SCL 使用同一网络，J1.IIC_SDA 与 M1.SDA 使用同一网络，中间没有串联电阻或电平转换器。

- 参数与网络：`scl_path=J1.1 IIC_SCL -> M1.4 SCL`；`sda_path=J1.2 IIC_SDA -> M1.5 SDA`；`series_components=none shown`；`level_shifter=none shown`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面上半：J1.1/J1.2 至 M1.4/M1.5 的两条直接水平连线

### SCL 与 SDA

SCL 经 R1（4.7KΩ）上拉至 +5V，SDA 经 R2（4.7KΩ）上拉至 +5V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +5V`；`sda_pullup=R2 4.7KΩ to +5V`；`module_supply=+3.3V`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面上中：+5V-R1-SCL 与 +5V-R2-SDA 两条上拉支路；M1.1 标 +3.3V

## GPIO 与控制信号

### M1 IRQ

M1.IRQ.6 仅有短引线，未连接 J1 或其他器件。

- 参数与网络：`interrupt_pin=M1.6 IRQ`；`external_connection=none shown`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面左上：M1.6 IRQ 右侧短线悬空

## 复位

### M1 RST

M1.RST.3 仅有短引线，未连接 J1 或任何外部上拉、下拉、RC、控制器件。

- 参数与网络：`reset_pin=M1.3 RST`；`external_connection=none shown`；`pullup_pulldown=none shown`
- 证据：图 d2e0a9b51514 / 第 1 页 / 页面左上：M1.3 RST 右侧短线悬空

## 保护电路

### J1

本页未显示 J1 的 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown`
- 证据：图 d2e0a9b51514 / 第 1 页 / 全页：J1 至 M1/U1 的完整信号和电源路径，仅包含 R1/R2 上拉及电源电容

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RFID | `module=M1 RC522`；`interface=J1 IIC_Socket_4P`；`input_rail=+5V`；`module_rail=+3.3V`；`regulator=U1 HT7533`；`bus=I2C` |
| 接口 | J1 | `connector=IIC_Socket_4P`；`pin_1=IIC_SCL / M1.4 SCL`；`pin_2=IIC_SDA / M1.5 SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board` |
| 核心器件 | M1 RC522 | `pin_1=3.3V`；`pin_2=GND`；`pin_3=RST`；`pin_4=SCL`；`pin_5=SDA`；`pin_6=IRQ` |
| 总线 | J1 与 M1 | `scl_path=J1.1 IIC_SCL -> M1.4 SCL`；`sda_path=J1.2 IIC_SDA -> M1.5 SDA`；`series_components=none shown`；`level_shifter=none shown` |
| 总线 | SCL 与 SDA | `scl_pullup=R1 4.7KΩ to +5V`；`sda_pullup=R2 4.7KΩ to +5V`；`module_supply=+3.3V` |
| 接口 | M1 SCL/SDA 电平 | `module_supply=+3.3V`；`bus_pullup_rail=+5V`；`level_shifter=none shown`；`input_tolerance=未标注` |
| 电源 | U1 HT7533 | `input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C3 10uF`；`output_capacitors=C1 100nF, C2 10uF` |
| 复位 | M1 RST | `reset_pin=M1.3 RST`；`external_connection=none shown`；`pullup_pulldown=none shown` |
| GPIO 与控制信号 | M1 IRQ | `interrupt_pin=M1.6 IRQ`；`external_connection=none shown` |
| 总线地址 | M1 I2C 地址 | `documented_address=0x28`；`schematic_address=未标注`；`address_straps=none shown` |
| 射频 | M1 RFID 模块 | `schematic_marking=RC522`；`documented_ic=MFRC522`；`documented_frequency=13.56MHz`；`antenna_matching=not shown` |
| 射频 | RFID 性能与协议 | `documented_protocols=ISO14443A, MIFARE, NTAG`；`documented_read_distance=<20mm`；`documented_i2c_rates=400 Kbit/s fast; 3400 Kbit/s high-speed`；`documented_buffer=64 bytes` |
| 保护电路 | J1 | `tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown` |

## 待确认事项

- `interface.logic-level-compatibility-unconfirmed`：原理图确认 M1 由 +3.3V 供电而 SCL/SDA 上拉至 +5V，但没有给出 M1 输入耐压或电平转换说明，无法由本页确认该接口的 5V 电平兼容性。（证据：图 d2e0a9b51514 / 第 1 页 / 页面上半：M1.1 +3.3V 与 R1/R2 上端 +5V 的同时标注）
- `address.i2c-0x28-unconfirmed`：产品正文标注 I2C 地址为 0x28，但原理图没有地址数值、地址选择引脚或绑带，无法仅由本页确认。（证据：图 d2e0a9b51514 / 第 1 页 / 页面左上 M1 与 J1 的全部可见引脚/网络，仅有 3.3V/GND/RST/SCL/SDA/IRQ，无地址配置）
- `rf.module-model-frequency-unconfirmed`：原理图将 M1 标为 RC522；产品正文称内置 MFRC522 且工作于 13.56MHz，但本页没有 MFRC522 型号、频率、天线或匹配网络。（证据：图 d2e0a9b51514 / 第 1 页 / 页面左上：M1 模块只标 RFID/RC522；全页无天线、晶振或 RF 匹配器件）
- `rf.protocol-performance-unconfirmed`：正文列出的 ISO14443A/MIFARE/NTAG、读写距离小于 20mm、I2C 速率和 64-byte 缓冲等参数未在原理图中标注。（证据：图 d2e0a9b51514 / 第 1 页 / 全页仅显示模块接口、电源和上拉，没有协议、距离、速率或缓冲参数）
- `review.i2c-level-compatibility`：M1 的 SCL/SDA 引脚是否可直接承受 R1/R2 上拉形成的 +5V 高电平？；原因：模块由 +3.3V 供电且图中无电平转换，输入耐压需查 RC522 模块电路/BOM 或实测，不能从本页判断。
- `review.i2c-address`：该 RC522 模块硬件/固件的 7 位 I2C 地址是否为正文所列 0x28？；原因：原理图未显示地址脚、绑带或地址文字，需由模块资料或 I2C 扫描确认。
- `review.rf-chip-frequency`：M1 模块内部芯片是否为 MFRC522，载波频率是否固定为 13.56MHz？；原因：原理图只显示黑盒模块 RC522，没有内部芯片、晶振、天线和匹配网络，需查模块 BOM/规格或实物。
- `review.rf-protocol-performance`：量产模块是否满足正文列出的协议、读距、I2C 速率和缓冲参数？；原因：这些能力依赖模块内部 IC、天线与固件，原理图未提供可核验细节。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d2e0a9b5151454474b9d853dd1780b3835269a9a696e7270d08e7993cab99c86` | `https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_sch_01.webp` |

---

源文档：`zh_CN/unit/rfid.md`

源文档 SHA-256：`c5145647d89aea277debf57cf124a4b2fe08774e8db27c6711347f8c1f629ffb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
