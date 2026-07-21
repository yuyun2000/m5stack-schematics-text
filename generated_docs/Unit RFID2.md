# Unit RFID2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RFID2 |
| SKU | U031-B |
| 产品 ID | `unit-rfid2-f87703264348` |
| 源文档 | `zh_CN/unit/rfid2.md` |

## 概述

Unit RFID2 产品页提供一张 U031-B-Sch_Unit-RFID_v1.3 图面。该页以 U1 MFRC522 为 RFID 前端：J1 IIC_Socket_4P 输入 +5V，经 U2 HT7533 生成 +3.3V；RC522_SCL/RC522_SDA 各以 4.7KΩ 上拉，U1 的 I2C/EA 配置脚分别接 +3.3V/GND；NRSTPD 使用 10KΩ/100nF RC；Y1 27.12MHz 连接 OSCIN/OSCOUT；TX1/TX2/RX 接由 1uH、pF 电容和 1.2Ω 电阻组成的射频匹配网络。正文则称 U031-B 已把前代 RC522 替换为 WS1850S，而图面 U1 仍明确标 MFRC522，且未画出具名天线。因此实际量产 IC、图面版本归属、0x28 地址、13.56MHz/ISO A/B/MIFARE/NTAG、读距、天线实现、代际兼容与机械参数均需另行确认。

## 检索关键词

`Unit RFID2`、`U031-B`、`WS1850S`、`MFRC522`、`RC522`、`U031-B-Sch_Unit-RFID_v1.3`、`RFID`、`NFC`、`13.56MHz`、`27.12MHz`、`ISO/IEC 14443 Type A`、`ISO/IEC 14443 Type B`、`MIFARE`、`NTAG`、`I2C`、`0x28`、`RC522_SDA`、`RC522_SCL`、`NRSTPD`、`TX1`、`TX2`、`RX`、`HT7533`、`IIC_Socket_4P`、`HY2.0-4P`、`+5V`、`+3.3V`、`read distance 20mm`、`LEGO compatible`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MFRC522 | 图面中的 RFID 前端，连接 I2C、复位、27.12MHz 晶体与 TX1/TX2/RX 匹配网络 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1A-2B，U1 器件值 MFRC522 |
| U2 | HT7533 | 把 J1 的 +5V 输入稳压为 +3.3V | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2C-3D，U2 HT7533 |
| J1 | IIC_Socket_4P | 四针 I2C/电源接口，提供 IIC_SCL、IIC_SDA、+5V 和 GND | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 3C，J1 IIC_Socket_4P pins1-4 |
| Y1 | 27.12MHz | U1 OSCIN/OSCOUT 的参考晶体 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1B，Y1 27.12MHz 与 C3/C6 |
| L1/L2 | 1uH | U1 TX1/TX2 射频输出的两路串联电感 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2B-3B，TX1/TX2 后的 L1/L2 1uH |
| R4/R5 | 1.2Ω | TX1/TX2 差分匹配网络末端的两只串联电阻 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 3B，R4/R5 1.2Ω 与闭合末端网络 |
| R6/R7 | 4.7KΩ | RC522_SCL/RC522_SDA 到 +3.3V 的 I2C 上拉 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 3C，R6/R7 4.7KΩ |
| R1/C2 | 10KΩ / 100nF | U1 NRSTPD 的上拉与对地 RC 复位网络 | 图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1A-1B，R1/C2 与 NRSTPD |

## 系统结构

### Unit RFID2 页面所提供的单页图面

该页由 U1 MFRC522、U2 HT7533、J1 IIC_Socket_4P、Y1 27.12MHz、I2C/复位外围与 TX1/TX2/RX 射频匹配网络构成。

- 参数与网络：`rfid_frontend=U1 MFRC522`；`regulator=U2 HT7533`；`host_interface=J1 IIC_Socket_4P`；`clock=Y1 27.12MHz`；`rf=TX1/TX2/RX matching network`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页完整单页全部功能分区

## 核心器件

### 图面 U1 读写 IC

U1 器件值明确标为 MFRC522，数字侧包含 I2C、EA、NRSTPD、SDA/NSS/RX 与 D7/SCL/MISO/TX 复用引脚，模拟侧包含 OSCIN/OSCOUT、VMID、RX、TX1、TX2 与电源地。

- 参数与网络：`reference=U1`；`schematic_part_number=MFRC522`；`digital=I2C,EA,NRSTPD,SDA/NSS/RX,D7/SCL/MISO/TX`；`analog=OSCIN,OSCOUT,VMID,RX,TX1,TX2`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1A-2B，U1 MFRC522 pins1-32

## 电源

### +5V 到 +3.3V 稳压

J1 pin3 的 +5V 接 U2 HT7533 VIN pin2，U2 VOUT pin3 形成 +3.3V；C14 10uF 位于输入侧，C12 100nF 与 C13 10uF 位于输出侧。

- 参数与网络：`input=J1.3 +5V`；`regulator=U2 HT7533`；`output=+3.3V`；`input_cap=C14 10uF`；`output_caps=C12 100nF,C13 10uF`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2C-3D，J1.3/U2/C12-C14

### U1 3.3V 电源

U1 AVDD pin15、DVDD pin3、PVDD pin2、TVDD pin12 接 +3.3V；DVSS pin4、PVSS pin5、TVSS pins10/14 与 AVSS pin18 接 GND。

- 参数与网络：`supply_pins=AVDD15,DVDD3,PVDD2,TVDD12`；`ground_pins=DVSS4,PVSS5,TVSS10,TVSS14,AVSS18`；`rail=+3.3V`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 顶部 AVDD/DVDD/PVDD/TVDD 与底部电源地

### +3.3V 去耦电容组

C16/C17 各为 100nF，C15/C18 各为 10uF，四只电容跨接 +3.3V 与 GND。

- 参数与网络：`small_caps=C16,C17 100nF`；`bulk_caps=C15,C18 10uF`；`rail=+3.3V`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1D-2D，C15-C18

## 接口

### J1 IIC_Socket_4P

J1 pin1=IIC_SCL/RC522_SCL、pin2=IIC_SDA/RC522_SDA、pin3=+5V、pin4=GND。

- 参数与网络：`pin1=IIC_SCL / RC522_SCL`；`pin2=IIC_SDA / RC522_SDA`；`pin3=+5V`；`pin4=GND`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 3C，J1 pins1-4

## 总线

### U1 到 J1 的 I2C

U1 pin31 D7/SCL/MISO/TX 通过 RC522_SCL 接 J1 pin1，U1 pin24 SDA/NSS/RX 通过 RC522_SDA 接 J1 pin2；R6/R7 各 4.7KΩ 将两条总线上拉到 +3.3V。

- 参数与网络：`scl=U1.31 -> RC522_SCL -> J1.1`；`sda=U1.24 -> RC522_SDA -> J1.2`；`pullups=R6,R7 4.7KΩ to +3.3V`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 pins24/31、RC522_SDA/SCL、R6/R7 与 J1

### U1 I2C/EA 配置引脚

U1 I2C pin1 接 +3.3V，EA pin32 接 GND；图面以 RC522_SDA/RC522_SCL 网络连接主机接口。

- 参数与网络：`i2c_pin=U1.1 -> +3.3V`；`ea_pin=U1.32 -> GND`；`host_nets=RC522_SDA,RC522_SCL`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 左上 I2C/EA pins1/32

## 时钟

### U1 27.12MHz 参考时钟

Y1 27.12MHz 连接 U1 OSCIN pin21 与 OSCOUT pin22，C3/C6 各 15pF 对地。

- 参数与网络：`crystal=Y1 27.12MHz`；`pins=U1.OSCIN21,U1.OSCOUT22`；`load_caps=C3,C6 15pF`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1B，Y1/C3/C6 与 U1 OSCIN/OSCOUT

## 复位

### U1 NRSTPD

U1 NRSTPD pin6 连接 NRSTPD 网络，R1 10KΩ 将其上拉到 +3.3V，C2 100nF 对地。

- 参数与网络：`reset_pin=U1.NRSTPD pin6`；`pullup=R1 10KΩ`；`capacitor=C2 100nF`；`rail=+3.3V`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 1A-1B，NRSTPD/R1/C2

## 保护电路

### 外部接口保护

J1 的 +5V、IIC_SCL 与 IIC_SDA 在本页没有串联保险丝、ESD/TVS、反接保护或信号串联电阻；只显示 HT7533 输入/输出电容和 I2C 上拉。

- 参数与网络：`fuse_shown=false`；`esd_tvs_shown=false`；`reverse_protection_shown=false`；`i2c_series_resistors_shown=false`；`i2c_pullups=R6,R7`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 J1 至 U2/U1 外部接口路径

## 内存与 Flash

### 外部存储器

完整单页未显示 MCU、Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`mcu_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页完整器件范围

## 射频

### U1 TX1/TX2 差分匹配网络

U1 TX1 pin11 与 TX2 pin13 分别经 L1/L2 1uH、C5/C11 47pF、C7/C9 120pF、C8/C10 390pF 和 R4/R5 1.2Ω 形成对称射频网络。

- 参数与网络：`tx_pins=U1.TX1 pin11,U1.TX2 pin13`；`inductors=L1,L2 1uH`；`series_caps=C5,C11 47pF`；`shunt_caps=C7,C9 120pF;C8,C10 390pF`；`resistors=R4,R5 1.2Ω`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2B-3B，TX1/TX2 匹配网络

### U1 RX/VMID 耦合网络

U1 VMID pin16 由 C1 100nF 对地，并经 R2 1KΩ 接 RX 取样节点；U1 RX pin17 连接该节点，C4 1nF 与 R3 1.5KΩ 串联到标为 RX 的匹配网络。

- 参数与网络：`vmid=U1.VMID16 -> C1 100nF GND`；`bias_resistor=R2 1KΩ`；`rx_pin=U1.RX17`；`coupling=C4 1nF + R3 1.5KΩ`
- 证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2A-3B，VMID/RX/C1/R2/C4/R3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RFID2 页面所提供的单页图面 | `rfid_frontend=U1 MFRC522`；`regulator=U2 HT7533`；`host_interface=J1 IIC_Socket_4P`；`clock=Y1 27.12MHz`；`rf=TX1/TX2/RX matching network` |
| 核心器件 | 图面 U1 读写 IC | `reference=U1`；`schematic_part_number=MFRC522`；`digital=I2C,EA,NRSTPD,SDA/NSS/RX,D7/SCL/MISO/TX`；`analog=OSCIN,OSCOUT,VMID,RX,TX1,TX2` |
| 电源 | +5V 到 +3.3V 稳压 | `input=J1.3 +5V`；`regulator=U2 HT7533`；`output=+3.3V`；`input_cap=C14 10uF`；`output_caps=C12 100nF,C13 10uF` |
| 电源 | U1 3.3V 电源 | `supply_pins=AVDD15,DVDD3,PVDD2,TVDD12`；`ground_pins=DVSS4,PVSS5,TVSS10,TVSS14,AVSS18`；`rail=+3.3V` |
| 电源 | +3.3V 去耦电容组 | `small_caps=C16,C17 100nF`；`bulk_caps=C15,C18 10uF`；`rail=+3.3V` |
| 接口 | J1 IIC_Socket_4P | `pin1=IIC_SCL / RC522_SCL`；`pin2=IIC_SDA / RC522_SDA`；`pin3=+5V`；`pin4=GND` |
| 总线 | U1 到 J1 的 I2C | `scl=U1.31 -> RC522_SCL -> J1.1`；`sda=U1.24 -> RC522_SDA -> J1.2`；`pullups=R6,R7 4.7KΩ to +3.3V` |
| 总线 | U1 I2C/EA 配置引脚 | `i2c_pin=U1.1 -> +3.3V`；`ea_pin=U1.32 -> GND`；`host_nets=RC522_SDA,RC522_SCL` |
| 复位 | U1 NRSTPD | `reset_pin=U1.NRSTPD pin6`；`pullup=R1 10KΩ`；`capacitor=C2 100nF`；`rail=+3.3V` |
| 时钟 | U1 27.12MHz 参考时钟 | `crystal=Y1 27.12MHz`；`pins=U1.OSCIN21,U1.OSCOUT22`；`load_caps=C3,C6 15pF` |
| 射频 | U1 TX1/TX2 差分匹配网络 | `tx_pins=U1.TX1 pin11,U1.TX2 pin13`；`inductors=L1,L2 1uH`；`series_caps=C5,C11 47pF`；`shunt_caps=C7,C9 120pF;C8,C10 390pF`；`resistors=R4,R5 1.2Ω` |
| 射频 | U1 RX/VMID 耦合网络 | `vmid=U1.VMID16 -> C1 100nF GND`；`bias_resistor=R2 1KΩ`；`rx_pin=U1.RX17`；`coupling=C4 1nF + R3 1.5KΩ` |
| 内存与 Flash | 外部存储器 | `mcu_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |
| 保护电路 | 外部接口保护 | `fuse_shown=false`；`esd_tvs_shown=false`；`reverse_protection_shown=false`；`i2c_series_resistors_shown=false`；`i2c_pullups=R6,R7` |
| 核心器件 | U031-B 实际 RFID IC 与图面版本 | `documented_product=Unit RFID2 U031-B`；`documented_ic=WS1850S`；`schematic_ic=MFRC522`；`schematic_name=U031-B-Sch_Unit-RFID_v1.3`；`production_ic_confirmed=false` |
| 总线地址 | I2C 默认地址 | `documented_address_7bit=0x28`；`address_text_shown=false`；`address_adjustment_shown=false`；`schematic_ic=MFRC522` |
| 射频 | 13.56MHz、ISO/IEC 14443 A/B 与卡型 | `documented_frequency=13.56MHz`；`documented_protocols=ISO/IEC 14443 Type A,Type B`；`documented_cards=MIFARE,NTAG`；`schematic_reference_clock=27.12MHz`；`schematic_protocol_text=false` |
| 射频 | RFID 读写距离 | `documented_read_write_distance=<20mm`；`antenna_geometry_shown=false`；`card_type_tested=null`；`orientation=null`；`measurement_conditions=null` |
| 射频 | 实际 RFID 天线 | `matching_network_shown=true`；`antenna_reference=null`；`antenna_part_number=null`；`pcb_geometry_shown=false`；`external_connector_shown=false` |
| 其他事实 | 与前代 Unit RFID 的功能兼容 | `documented_change=RC522 -> WS1850S`；`documented_functional_difference=none`；`api_compatibility=null`；`register_compatibility=null`；`timing_compatibility=null`；`electrical_compatibility=null` |
| 其他事实 | 外形、重量与 LEGO 孔 | `documented_lego_holes=2`；`documented_product_size=48.0 x 24.0 x 8.0mm`；`documented_product_weight=5.9g`；`documented_package_size=138.0 x 93.0 x 16.0mm`；`documented_gross_weight=11.3g` |

## 待确认事项

- `component.documented-ws1850s-version`：正文称 Unit RFID2 使用 WS1850S，并说明相对前代仅把 RC522 替换为 WS1850S；当前 U031-B-Sch_Unit-RFID_v1.3 图面 U1 却明确标 MFRC522，无法据此确认 U031-B 量产 IC 或该页是否仍为前代电路。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 器件值 MFRC522）
- `address.documented-i2c-0x28`：正文规格表给出 I2C 地址 0x28，图面只显示 I2C/EA 绑带、RC522_SDA/RC522_SCL 和上拉，没有 0x28 文本或可调地址器件。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 I2C/EA、RC522_SDA/SCL 与 J1，无数值地址）
- `rf.documented-frequency-protocols-cards`：正文称工作频率 13.56MHz，兼容 ISO/IEC 14443 Type A/B，并支持 MIFARE、NTAG 等卡；图面只确认 27.12MHz 晶体与 MFRC522 匹配网络，没有载波、协议或卡型文字。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 Y1 27.12MHz 与 U1/RF 网络，无 13.56MHz/协议/卡型标注）
- `rf.documented-read-distance`：正文称读写距离小于 20mm，图面没有天线尺寸、卡片类型、场强、供电条件、方向或距离测试标注。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 RF 匹配网络无距离或测试条件）
- `rf.antenna-implementation`：图面绘制 TX1/TX2/RX 匹配网络并在 R4/R5 右端闭合，但没有天线位号、线圈型号、PCB 几何尺寸或外接天线连接器，无法确定 U031-B 的实际天线实现。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页网格 2B-3B，匹配网络止于 R4/R5，无 ANT 位号）
- `other.documented-predecessor-compatibility`：正文称 RFID2 相对前代只进行 RC522 到 WS1850S 的 IC 替换且功能无区别；当前图面仍标 MFRC522，无法确认固件 API、寄存器、时序、协议覆盖和电气兼容是否完全一致。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页 U1 MFRC522 与 RC522_SDA/RC522_SCL）
- `other.documented-mechanics`：正文列出两个 LEGO 兼容孔、产品尺寸 48.0 x 24.0 x 8.0mm、重量 5.9g、包装尺寸 138.0 x 93.0 x 16.0mm 和毛重 11.3g；当前电气图没有板框、孔位、尺寸或质量信息。（证据：图 8f4d9db180d4 / 第 1 页 / 第 1 页电气图无板框、孔位或机械参数）
- `review.ws1850s-version`：请依据 U031-B 正式原理图、量产 BOM 或 U1 丝印确认 RFID2 使用 WS1850S，并确认当前 v1.3 图是否仍是前代 MFRC522 图面。；原因：正文与图面 U1 型号直接冲突，不能把旧 RC522 拓扑当作 WS1850S 量产事实。
- `review.i2c-address`：请通过 U031-B 当前 WS1850S 料号资料和固件确认 7-bit I2C 地址是否固定为 0x28，以及是否可配置。；原因：图面未打印地址，且图面 IC 与正文 IC 不一致。
- `review.frequency-protocols-cards`：请依据 U031-B 实际 IC datasheet、认证资料和实测确认 13.56MHz、ISO/IEC 14443 Type A/B 及 MIFARE/NTAG 支持范围。；原因：图面只显示 MFRC522 与 27.12MHz 晶体，未给协议和卡型。
- `review.read-distance`：请在指定卡型、供电、姿态和外壳条件下实测 U031-B 读写距离，并确认 `<20mm` 的验收定义。；原因：距离取决于天线、卡片、匹配、功率和测试条件，电气图没有这些参数。
- `review.antenna-implementation`：请提供 U031-B PCB 天线层、天线位号或结构图，确认实际线圈几何、连接点和匹配版本。；原因：当前图面只有匹配网络，没有具名天线或 PCB 几何。
- `review.predecessor-compatibility`：请用 WS1850S/MFRC522 寄存器与时序对比、现有库兼容测试确认 RFID2 相对前代的 API、协议和电气兼容边界。；原因：“功能无区别”是产品正文结论，当前图面仍为 MFRC522，无法证明替换后的完整兼容性。
- `review.mechanics`：请用 U031-B 正式结构图、孔位图和称重记录复核 LEGO 孔、尺寸与重量参数。；原因：当前电气图没有板框、孔位、机械尺寸或质量信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8f4d9db180d4f5fb0e29f59e908bc6e6c8b55c3a83de4a98fe6e48412f7e22f8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-Sch_Unit-RFID_v1.3_page_01.png` |

---

源文档：`zh_CN/unit/rfid2.md`

源文档 SHA-256：`e9d90dd506d2ab3d8b2c2bd483683b5c372828ea9f754b7c7be28b93e8432327`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
