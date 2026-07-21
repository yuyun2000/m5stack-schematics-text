# Base BTC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base BTC |
| SKU | A011 |
| 产品 ID | `base-btc-74e915409827` |
| 源文档 | `zh_CN/base/btc_base.md` |

## 概述

Base BTC v2.1 是一块无主控的温湿度传感器底座，核心器件 U1 明确标为 SHT30-DIS-B，以 3.3V 供电并通过 G21/G22 I2C 网络连接外部主控。J1 USB-C 的 VBUS 汇入 VIN，经 F1 保险器件形成 +5V 并送到 P1；3.3V 则从 P1 引入，板上未显示稳压器、充电器或电池。Rp1 四联 5.1K 电阻网络为 CC1/CC2 提供对地下拉，并为 G21/G22 提供到 3.3V 的 I2C 上拉。

## 检索关键词

`Base BTC`、`A011`、`BTC v2.1`、`SHT30-DIS-B`、`SHT30`、`temperature humidity`、`I2C`、`G21`、`G22`、`SDA`、`SCL`、`0x44`、`USB-C`、`VBUS`、`VIN`、`+5V`、`+3.3V`、`CC1`、`CC2`、`Rp1`、`5.1KΩ`、`F1`、`Header 8`、`ALERT`、`nRESET`、`ADDR`、`C1 100nF`、`G23`、`G19`、`G18`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 数字温湿度传感器，通过 SDA/SCL 与外部主控通信 | 图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 SHT30-DIS-B，SDA/SCL/VDD/VSS/ADDR/ALERT/nRESET |
| J1 | USB-C | 5V 电源输入连接器，VBUS 接 VIN，CC1/CC2 接配置下拉，未画 USB 数据线 | 图 a7b0c57b0c94 / 第 1 页 / 网格 B1-B2，J1 USB-C pins1-10，VBUS/VIN/CC1/CC2/GND |
| P1 | Header 8 | 底座到主控/Bottom 的八针接口，引出 5V、3.3V、GND、G21、G22、G23、G19、G18 | 图 a7b0c57b0c94 / 第 1 页 / 网格 B3，P1 Header 8 pins1-8 |
| Rp1 | 5.1KΩ (512) ±5% resistor array | 四联电阻网络，为 CC1/CC2 提供对地下拉，为 G21/G22 提供 3.3V 上拉 | 图 a7b0c57b0c94 / 第 1 页 / 网格 B2，Rp1 pins1-8，标注 5.1KΩ(512)±5% |
| F1 | Fuse | VIN 到 +5V 的串联保险器件 | 图 a7b0c57b0c94 / 第 1 页 / 网格 B2-B3，VIN-F1 Fuse-+5V |
| C1 | 100nF | SHT30 3.3V 电源去耦电容 | 图 a7b0c57b0c94 / 第 1 页 / 网格 C1，C1 100nF 跨接 +3.3V 与 GND |

## 系统结构

### Base BTC v2.1 架构

电路由 U1 SHT30-DIS-B 温湿度传感器、J1 USB-C 电源入口、F1 保险器件、P1 八针接口与 Rp1 电阻网络组成；板上没有主控。

- 参数与网络：`sensor=U1 SHT30-DIS-B`；`power_input=J1 USB-C`；`fuse=F1`；`host_connector=P1 Header 8`；`resistor_array=Rp1`；`mcu=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，全部器件与网络

## 核心器件

### v2.1 传感器型号

当前 v2.1 原理图的环境传感器是 U1 SHT30-DIS-B，页内没有 DHT12 器件。

- 参数与网络：`schematic_version=v2.1`；`current_sensor=U1 SHT30-DIS-B`；`dht12=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，唯一传感器 U1 标 SHT30-DIS-B

## 电源

### USB-C 到 +5V 电源路径

J1 VBUS 形成 VIN，VIN 经 F1 Fuse 串联后成为 +5V，并连接 P1 pin1；该路径没有显示稳压转换器或负载开关。

- 参数与网络：`source=J1 VBUS pins2,5`；`input_net=VIN`；`protection=F1 Fuse`；`output=+5V`；`destination=P1 pin1`；`converter=null`；`load_switch=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B1-B3，J1 VBUS/VIN、F1、+5V、P1 pin1

### SHT30 3.3V 供电

P1 pin2 的 +3.3V 直接供给 U1 VDD pin5、Rp1 I2C 上拉端和 C1 100nF；板上没有从 +5V 生成 +3.3V 的转换器。

- 参数与网络：`source=P1 pin2 +3.3V`；`sensor=U1 pin5 VDD`；`pullups=Rp1 pins5,6`；`decoupling=C1 100nF`；`3v3_regulator=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B2-C3，+3.3V 从 P1 到 Rp1/U1/C1；无转换器

## 接口

### P1 八针接口

P1 Header 8 pin1 为 +5V、pin2 +3.3V、pin3 GND、pin4 G21、pin5 G22、pin6 G23、pin7 G19、pin8 G18。

- 参数与网络：`reference=P1`；`pin1=+5V`；`pin2=+3.3V`；`pin3=GND`；`pin4=G21/SDA`；`pin5=G22/SCL`；`pin6=G23`；`pin7=G19`；`pin8=G18`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B3，P1 Header 8 网络标注

### J1 USB-C 电源接口

J1 的 VBUS pins2/5 汇入 VIN，CC1 pin3 与 CC2 pin4 接 Rp1，下列 GND pins1/6/7/8/9/10 接地；原理图未显示 D+、D- 或高速数据线。

- 参数与网络：`reference=J1`；`vbus=pins2,5 -> VIN`；`cc1=pin3 CC1`；`cc2=pin4 CC2`；`ground=pins1,6,7,8,9,10`；`usb_data=null`；`direction=power input`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B1-B2，J1 USB-C pin1-10

## 总线

### SHT30 I2C 总线

P1 pin4 G21 连接 U1 SDA pin1，P1 pin5 G22 连接 U1 SCL pin4；Rp1 中两路 5.1K 电阻分别将 G21 与 G22 上拉到 +3.3V。

- 参数与网络：`controller_connector=P1`；`device=U1 SHT30-DIS-B`；`sda=P1.4 G21 -> U1.1 SDA`；`scl=P1.5 G22 -> U1.4 SCL`；`sda_pullup=Rp1 pin3-pin6 5.1K to +3.3V`；`scl_pullup=Rp1 pin4-pin5 5.1K to +3.3V`；`level=3.3V`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B2-C3，P1 G21/G22、Rp1 与 U1 SDA/SCL

## 总线地址

### SHT30 地址选择

U1 ADDR pin2 接 GND；当前页未标注该绑带对应的数值 I2C 地址。

- 参数与网络：`device=U1 SHT30-DIS-B`；`address_pin=pin2 ADDR`；`strap=GND`；`numeric_address=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 ADDR pin2 接 GND

## GPIO 与控制信号

### P1 非 I2C GPIO

P1 引出 G23、G19 与 G18，但这三条网络在本页没有连接 U1 或其他器件。

- 参数与网络：`signals=G23,G19,G18`；`pins=P1.6,P1.7,P1.8`；`board_load=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B3，P1 pins6-8 网络止于连接器

## 时钟

### 板级时钟

本页未显示晶振、振荡器或外部时钟网络；SHT30 的内部时钟未展开。

- 参数与网络：`crystal=null`；`oscillator=null`；`clock_net=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无 X/Y/CLK 器件或网络

## 复位

### SHT30 复位与告警引脚

U1 nRESET pin6 与 ALERT pin3 在本页均未连接，板上没有外部硬件复位或告警线路。

- 参数与网络：`reset=U1 pin6 nRESET NC`；`alert=U1 pin3 ALERT NC`；`external_reset=null`；`interrupt_line=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 ALERT/nRESET 引脚短线无网络

## 保护电路

### USB 输入保险保护

F1 标为 Fuse，串联在 VIN 与 +5V 之间；原理图未标注 F1 的额定电流、具体型号或可恢复属性。

- 参数与网络：`reference=F1`；`marking=Fuse`；`input=VIN`；`output=+5V`；`rating=null`；`part_number=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B2-B3，VIN-F1 Fuse-+5V

### USB-C CC 配置

CC1 经 Rp1 pin7-pin2 的 5.1K 电阻接 GND，CC2 经 Rp1 pin8-pin1 的 5.1K 电阻接 GND。

- 参数与网络：`cc1=J1 pin3 CC1 -> Rp1 pin7; Rp1 pin2 -> GND`；`cc2=J1 pin4 CC2 -> Rp1 pin8; Rp1 pin1 -> GND`；`resistance=5.1KΩ ±5% each`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 B1-B2，J1 CC1/CC2 到 Rp1 上两路 5.1K 对地下拉

## 关键网络

### 电源与数据关键网络

电源路径为 J1 VBUS -> VIN -> F1 -> +5V -> P1 pin1；传感器路径为 P1 pin2 +3.3V -> U1 VDD，P1 G21/G22 -> U1 SDA/SCL。

- 参数与网络：`5v_path=J1 VBUS -> VIN -> F1 -> +5V -> P1.1`；`3v3_path=P1.2 -> +3.3V -> U1.5`；`sda_path=P1.4 G21 -> U1.1`；`scl_path=P1.5 G22 -> U1.4`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网络追踪：J1/F1/P1/Rp1/U1

## 存储

### 板级存储

本页未显示 Flash、EEPROM、eMMC 或存储卡接口。

- 参数与网络：`flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无存储器件

## 内存与 Flash

### 外部内存

本页未显示 MCU、RAM、PSRAM 或 DDR 器件。

- 参数与网络：`mcu=null`；`ram=null`；`psram=null`；`ddr=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，仅 SHT30 与无源/连接器

## 音频

### 音频电路

本页未显示音频编解码器、麦克风、扬声器或 I2S 网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无 Audio/I2S 器件或网络

## 传感器

### SHT30-DIS-B 温湿度传感器

U1 明确标为 SHT30-DIS-B，VDD pin5 接 +3.3V，VSS pin8、R pin7 与 dpad pin9 接 GND，SDA pin1 接 G21，SCL pin4 接 G22。

- 参数与网络：`reference=U1`；`part_number=SHT30-DIS-B`；`vdd=pin5 +3.3V`；`ground=pin8 VSS,pin7 R,pin9 dpad`；`sda=pin1 SDA/G21`；`scl=pin4 SCL/G22`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 SHT30-DIS-B pins1-9

## 射频

### 射频电路

本页未显示射频芯片、天线或射频匹配网络。

- 参数与网络：`rf_ic=null`；`antenna=null`；`matching=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无 RF/ANT 分区

## 调试与烧录

### 调试接口

本页未显示测试点、SWD、JTAG、UART 调试口或编程连接器。

- 参数与网络：`test_points=null`；`swd=null`；`jtag=null`；`uart=null`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无 TP/Debug 接口

## 模拟电路

### 传感器模拟测量链

SHT30 在本页以数字传感器封装表示，内部温湿度敏感元件、ADC 与校准链未展开；板外只见 I2C、电源和地。

- 参数与网络：`device=U1 SHT30-DIS-B`；`external_analog_input=null`；`internal_adc=not shown`；`external_interface=I2C`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 单一数字符号与 SDA/SCL

## 其他事实

### 电池与充电路径

本页没有 BAT 网络、电池连接器、充电管理 IC 或电量监测器；USB-C 电源仅经 F1 引到 +5V。

- 参数与网络：`battery=null`；`charger=null`；`fuel_gauge=null`；`usb_power_path=VIN -> F1 -> +5V`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 整页网格 A1-D4，无 BAT/charger；仅 J1/F1 电源路径

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base BTC v2.1 架构 | `sensor=U1 SHT30-DIS-B`；`power_input=J1 USB-C`；`fuse=F1`；`host_connector=P1 Header 8`；`resistor_array=Rp1`；`mcu=null` |
| 传感器 | SHT30-DIS-B 温湿度传感器 | `reference=U1`；`part_number=SHT30-DIS-B`；`vdd=pin5 +3.3V`；`ground=pin8 VSS,pin7 R,pin9 dpad`；`sda=pin1 SDA/G21`；`scl=pin4 SCL/G22` |
| 核心器件 | v2.1 传感器型号 | `schematic_version=v2.1`；`current_sensor=U1 SHT30-DIS-B`；`dht12=null` |
| 总线 | SHT30 I2C 总线 | `controller_connector=P1`；`device=U1 SHT30-DIS-B`；`sda=P1.4 G21 -> U1.1 SDA`；`scl=P1.5 G22 -> U1.4 SCL`；`sda_pullup=Rp1 pin3-pin6 5.1K to +3.3V`；`scl_pullup=Rp1 pin4-pin5 5.1K to +3.3V`；`level=3.3V` |
| 接口 | P1 八针接口 | `reference=P1`；`pin1=+5V`；`pin2=+3.3V`；`pin3=GND`；`pin4=G21/SDA`；`pin5=G22/SCL`；`pin6=G23`；`pin7=G19`；`pin8=G18` |
| GPIO 与控制信号 | P1 非 I2C GPIO | `signals=G23,G19,G18`；`pins=P1.6,P1.7,P1.8`；`board_load=null` |
| 接口 | J1 USB-C 电源接口 | `reference=J1`；`vbus=pins2,5 -> VIN`；`cc1=pin3 CC1`；`cc2=pin4 CC2`；`ground=pins1,6,7,8,9,10`；`usb_data=null`；`direction=power input` |
| 电源 | USB-C 到 +5V 电源路径 | `source=J1 VBUS pins2,5`；`input_net=VIN`；`protection=F1 Fuse`；`output=+5V`；`destination=P1 pin1`；`converter=null`；`load_switch=null` |
| 电源 | SHT30 3.3V 供电 | `source=P1 pin2 +3.3V`；`sensor=U1 pin5 VDD`；`pullups=Rp1 pins5,6`；`decoupling=C1 100nF`；`3v3_regulator=null` |
| 保护电路 | USB 输入保险保护 | `reference=F1`；`marking=Fuse`；`input=VIN`；`output=+5V`；`rating=null`；`part_number=null` |
| 保护电路 | USB-C CC 配置 | `cc1=J1 pin3 CC1 -> Rp1 pin7; Rp1 pin2 -> GND`；`cc2=J1 pin4 CC2 -> Rp1 pin8; Rp1 pin1 -> GND`；`resistance=5.1KΩ ±5% each` |
| 总线地址 | SHT30 地址选择 | `device=U1 SHT30-DIS-B`；`address_pin=pin2 ADDR`；`strap=GND`；`numeric_address=null` |
| 复位 | SHT30 复位与告警引脚 | `reset=U1 pin6 nRESET NC`；`alert=U1 pin3 ALERT NC`；`external_reset=null`；`interrupt_line=null` |
| 模拟电路 | 传感器模拟测量链 | `device=U1 SHT30-DIS-B`；`external_analog_input=null`；`internal_adc=not shown`；`external_interface=I2C` |
| 关键网络 | 电源与数据关键网络 | `5v_path=J1 VBUS -> VIN -> F1 -> +5V -> P1.1`；`3v3_path=P1.2 -> +3.3V -> U1.5`；`sda_path=P1.4 G21 -> U1.1`；`scl_path=P1.5 G22 -> U1.4` |
| 时钟 | 板级时钟 | `crystal=null`；`oscillator=null`；`clock_net=null` |
| 调试与烧录 | 调试接口 | `test_points=null`；`swd=null`；`jtag=null`；`uart=null` |
| 存储 | 板级存储 | `flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null` |
| 内存与 Flash | 外部内存 | `mcu=null`；`ram=null`；`psram=null`；`ddr=null` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s=null` |
| 射频 | 射频电路 | `rf_ic=null`；`antenna=null`；`matching=null` |
| 其他事实 | 电池与充电路径 | `battery=null`；`charger=null`；`fuel_gauge=null`；`usb_power_path=VIN -> F1 -> +5V` |
| 总线地址 | SHT30 数值 I2C 地址 | `device=U1 SHT30-DIS-B`；`documented_address=0x44`；`schematic_strap=ADDR=GND`；`schematic_numeric_address=null` |
| 传感器 | 温湿度量程与精度 | `documented_temperature_range=-40~120°C`；`documented_temperature_accuracy=±0.2°C at 0~60°C`；`documented_humidity_range=10~90%RH`；`documented_humidity_accuracy=±2%RH`；`schematic_performance=null` |

## 待确认事项

- `address.documented-sht30`：正文称 SHT30 地址为 0x44；原理图确认 ADDR pin2 接 GND，但页内未直接标注 0x44，需由 SHT30 datasheet 或总线扫描确认数值。（证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 ADDR pin2 接 GND，无数值地址注记）
- `sensor.documented-performance`：正文列出温度 -40~120°C、0~60°C 内最高 ±0.2°C，以及湿度 10~90%RH/±2%；原理图只给出 SHT30-DIS-B 型号与连接，不包含量程、精度或测试条件。（证据：图 a7b0c57b0c94 / 第 1 页 / 网格 C1-C2，U1 SHT30-DIS-B 符号，无测量规格表）
- `review.sht30-address`：请依据 SHT30-DIS-B datasheet 或 I2C 总线扫描确认 ADDR 接 GND 时地址为 0x44。；原因：原理图只显示 ADDR 绑带，没有直接标注数值地址。
- `review.sensor-performance`：请用 SHT30-DIS-B datasheet 与产品测试条件确认温湿度量程和精度指标。；原因：原理图不包含传感器性能参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a7b0c57b0c9411ae8a60e8f0b359b1f784805d2e1ceef453ea9729bb7f968b24` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-Sch_BTC_v2.1_page_01.png` |

---

源文档：`zh_CN/base/btc_base.md`

源文档 SHA-256：`d253fdbcf21f255f1f6d8aa0ba6d23a96217db3131dee534f36f6c6088ca0705`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
