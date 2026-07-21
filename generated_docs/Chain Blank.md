# Chain Blank 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Blank |
| SKU | U210 |
| 产品 ID | `chain-blank-7c4fc41115c9` |
| 源文档 | `zh_CN/chain/Chain_Blank.md` |

## 概述

Chain Blank V0.1 是一块无源 Chain/Grove 四线直通节点，J1 与 J2 均引出 IO2、IO1、VCC_5V 和 GND。IO2 经 R1 0Ω 串联直通，IO1 经 R2 0Ω 串联直通，VCC_5V 与 GND 则在两连接器之间直接相连；原理图没有任何 IC、电源转换、保护或协议相关器件。

## 检索关键词

`Chain Blank`、`U210`、`V0.1`、`GROVE_IO`、`HY2.0-4P`、`J1`、`J2`、`IO1`、`IO2`、`VCC_5V`、`GND`、`R1 0Ω`、`R2 0Ω`、`pass-through`、`proto board`、`Chain series`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 第一组四针 Chain/Grove 接口，引出 IO2、IO1、VCC_5V、GND | 图 92c256599899 / 第 1 页 / 网格 B2，J1 GROVE_IO，IO2/IO1/VCC/GND 四针 |
| J2 | GROVE_IO | 第二组四针 Chain/Grove 接口，引出 IO2、IO1、VCC_5V、GND | 图 92c256599899 / 第 1 页 / 网格 B2-B3，J2 GROVE_IO，IO2/IO1/VCC/GND 四针 |
| R1 | 0Ω | J1 IO2 与 J2 IO2 之间的可拆改串联跳线 | 图 92c256599899 / 第 1 页 / 网格 B2，IO2 水平网络中的 R1 0R |
| R2 | 0Ω | J1 IO1 与 J2 IO1 之间的可拆改串联跳线 | 图 92c256599899 / 第 1 页 / 网格 B2，IO1 水平网络中的 R2 0R |

## 系统结构

### Chain Blank 电路架构

电路仅由两组 GROVE_IO 连接器与两颗 0Ω 串联电阻组成，四条线路在 J1/J2 之间直通，没有主控或其他有源器件。

- 参数与网络：`connectors=J1,J2 GROVE_IO`；`series_links=R1,R2 0Ω`；`signals=IO2,IO1,VCC_5V,GND`；`active_components=null`；`mcu=null`
- 证据：图 92c256599899 / 第 1 页 / 整页网格 A1-D4，唯一电路为 J1/R1/R2/J2

## 核心器件

### IO2 串联跳线

R1 标为 0R，串联在 J1 IO2 与 J2 IO2 之间。

- 参数与网络：`reference=R1`；`value=0Ω`；`left=J1 IO2/pin1`；`right=J2 IO2/pin1`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，上方 IO2 网络 R1 0R

### IO1 串联跳线

R2 标为 0R，串联在 J1 IO1 与 J2 IO1 之间。

- 参数与网络：`reference=R2`；`value=0Ω`；`left=J1 IO1/pin2`；`right=J2 IO1/pin2`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，下方 IO1 网络 R2 0R

## 电源

### VCC_5V 电源直通

J1 VCC pin3 与 J2 VCC pin3 通过 VCC_5V 网络直接相连，中间没有保险丝、二极管、负载开关或稳压器。

- 参数与网络：`rail=VCC_5V`；`left=J1 pin3 VCC`；`right=J2 pin3 VCC`；`series_component=null`；`converter=null`；`load_switch=null`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2-B3，J1/J2 VCC 水平直连并标 VCC_5V

### GND 直通

J1 GND pin4 与 J2 GND pin4 直接连接公共地网络。

- 参数与网络：`left=J1 pin4 GND`；`right=J2 pin4 GND`；`net=GND`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2-B3，J1/J2 GND 直接接公共地符号

## 接口

### J1 四针接口

J1 GROVE_IO 从上至下标为 IO2、IO1、VCC、GND；VCC 网络名为 VCC_5V。

- 参数与网络：`reference=J1`；`pin1=IO2`；`pin2=IO1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`direction=pass-through/bidirectional signals`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，J1 GROVE_IO 四个引脚标签

### J2 四针接口

J2 GROVE_IO pin1 为 IO2、pin2 为 IO1、pin3 为 VCC/VCC_5V、pin4 为 GND。

- 参数与网络：`reference=J2`；`pin1=IO2`；`pin2=IO1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`direction=pass-through/bidirectional signals`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2-B3，J2 GROVE_IO pin1-4

### J1 到 J2 针脚对应

J1 pin1 IO2 对应 J2 pin1，J1 pin2 IO1 对应 J2 pin2，J1 pin3 VCC 对应 J2 pin3，J1 pin4 GND 对应 J2 pin4。

- 参数与网络：`io2=J1.1 -> R1 -> J2.1`；`io1=J1.2 -> R2 -> J2.2`；`power=J1.3 -> VCC_5V -> J2.3`；`ground=J1.4 -> GND -> J2.4`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2-B3，四条 J1-J2 水平连线

## 总线

### IO1/IO2 通信线路

IO1 与 IO2 是两个无方向标注的直通信号，原理图没有指定其为 I2C、UART、模拟或其他协议。

- 参数与网络：`signals=IO1,IO2`；`topology=point-to-point pass-through`；`protocol=null`；`direction=not annotated`；`level=null`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，IO1/IO2 仅连接 J1、R1/R2、J2，无协议器件

## 总线地址

### 总线地址

板上没有可寻址 IC，也没有原理图可见的 I2C、SPI 或其他设备地址。

- 参数与网络：`addressed_device=null`；`i2c_address=null`；`spi_chip_select=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无 IC 或地址标注

## GPIO 与控制信号

### 可断开 IO 路径

R1/R2 是 IO2/IO1 的唯一串联元件；移除对应 0Ω 电阻会在该位置断开 J1 与 J2 的对应信号通路。

- 参数与网络：`io2_disconnect=remove R1`；`io1_disconnect=remove R2`；`power_unchanged=VCC_5V direct`；`ground_unchanged=GND direct`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，IO1/IO2 各只有一颗 0Ω 串联器件

## 时钟

### 时钟电路

板上没有晶振、振荡器、时钟发生器或时钟网络。

- 参数与网络：`crystal=null`；`oscillator=null`；`clock_generator=null`；`clock_net=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无 X/Y/CLK 器件或网络

## 复位

### 复位与使能

板上没有 RESET、BOOT、EN 或其他控制网络。

- 参数与网络：`reset=null`；`boot=null`；`enable=null`
- 证据：图 92c256599899 / 第 1 页 / 整页仅 IO1/IO2/VCC/GND 网络

## 保护电路

### 接口保护

原理图未显示 ESD/TVS、保险丝、限流、反接保护或过压保护器件。

- 参数与网络：`esd_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_protection=null`；`ovp=null`
- 证据：图 92c256599899 / 第 1 页 / 整页仅 J1/J2/R1/R2，无保护器件

## 关键网络

### Chain 四线关键网络

完整网络映射为 J1.IO2 -> R1 0Ω -> J2.IO2；J1.IO1 -> R2 0Ω -> J2.IO1；J1.VCC -> VCC_5V -> J2.VCC；J1.GND -> GND -> J2.GND。

- 参数与网络：`signal_1=J1.IO2 > R1 0Ω > J2.IO2`；`signal_2=J1.IO1 > R2 0Ω > J2.IO1`；`power=J1.VCC > VCC_5V > J2.VCC`；`ground=J1.GND > GND > J2.GND`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2-B3，全部四条网络

## 存储

### 存储器

板上没有 Flash、EEPROM、eMMC 或存储卡接口。

- 参数与网络：`flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无存储器件

## 内存与 Flash

### 内存与主控

板上没有 MCU、SoC、RAM、PSRAM 或 DDR 器件。

- 参数与网络：`mcu=null`；`soc=null`；`ram=null`；`psram=null`；`ddr=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无有源 IC

## 音频

### 音频电路

板上没有音频编解码器、麦克风、扬声器或 I2S 网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无音频器件或网络

## 传感器

### 传感器

板上没有传感器器件或传感器专用接口标注。

- 参数与网络：`sensor_ic=null`；`sensor_bus=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无 Sensor 器件

## 射频

### 射频电路

板上没有射频芯片、天线或射频匹配网络。

- 参数与网络：`rf_ic=null`；`antenna=null`；`matching=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无 RF/ANT 器件或网络

## 调试与烧录

### 调试接口

板上没有 SWD、JTAG、UART 调试连接器或测试点。

- 参数与网络：`swd=null`；`jtag=null`；`uart_debug=null`；`test_points=null`
- 证据：图 92c256599899 / 第 1 页 / 整页无 Debug/TP 接口

## 模拟电路

### 模拟调理

IO1/IO2 路径没有分压、滤波、放大、ADC 或 DAC 电路。

- 参数与网络：`divider=null`；`filter=null`；`amplifier=null`；`adc=null`；`dac=null`
- 证据：图 92c256599899 / 第 1 页 / 网格 B2，IO1/IO2 仅串联 R1/R2 0Ω

## 其他事实

### 电池与充电路径

板上没有电池、充电器或电量监测器，VCC_5V 仅在两连接器之间直通。

- 参数与网络：`battery=null`；`charger=null`；`fuel_gauge=null`；`power_path=J1 VCC -> J2 VCC`
- 证据：图 92c256599899 / 第 1 页 / 整页无 BAT/charger，只有 VCC_5V 直通

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Blank 电路架构 | `connectors=J1,J2 GROVE_IO`；`series_links=R1,R2 0Ω`；`signals=IO2,IO1,VCC_5V,GND`；`active_components=null`；`mcu=null` |
| 接口 | J1 四针接口 | `reference=J1`；`pin1=IO2`；`pin2=IO1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`direction=pass-through/bidirectional signals` |
| 接口 | J2 四针接口 | `reference=J2`；`pin1=IO2`；`pin2=IO1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`direction=pass-through/bidirectional signals` |
| 接口 | J1 到 J2 针脚对应 | `io2=J1.1 -> R1 -> J2.1`；`io1=J1.2 -> R2 -> J2.2`；`power=J1.3 -> VCC_5V -> J2.3`；`ground=J1.4 -> GND -> J2.4` |
| 总线 | IO1/IO2 通信线路 | `signals=IO1,IO2`；`topology=point-to-point pass-through`；`protocol=null`；`direction=not annotated`；`level=null` |
| 核心器件 | IO2 串联跳线 | `reference=R1`；`value=0Ω`；`left=J1 IO2/pin1`；`right=J2 IO2/pin1` |
| 核心器件 | IO1 串联跳线 | `reference=R2`；`value=0Ω`；`left=J1 IO1/pin2`；`right=J2 IO1/pin2` |
| GPIO 与控制信号 | 可断开 IO 路径 | `io2_disconnect=remove R1`；`io1_disconnect=remove R2`；`power_unchanged=VCC_5V direct`；`ground_unchanged=GND direct` |
| 电源 | VCC_5V 电源直通 | `rail=VCC_5V`；`left=J1 pin3 VCC`；`right=J2 pin3 VCC`；`series_component=null`；`converter=null`；`load_switch=null` |
| 电源 | GND 直通 | `left=J1 pin4 GND`；`right=J2 pin4 GND`；`net=GND` |
| 关键网络 | Chain 四线关键网络 | `signal_1=J1.IO2 > R1 0Ω > J2.IO2`；`signal_2=J1.IO1 > R2 0Ω > J2.IO1`；`power=J1.VCC > VCC_5V > J2.VCC`；`ground=J1.GND > GND > J2.GND` |
| 保护电路 | 接口保护 | `esd_tvs=null`；`fuse=null`；`current_limit=null`；`reverse_protection=null`；`ovp=null` |
| 模拟电路 | 模拟调理 | `divider=null`；`filter=null`；`amplifier=null`；`adc=null`；`dac=null` |
| 总线地址 | 总线地址 | `addressed_device=null`；`i2c_address=null`；`spi_chip_select=null` |
| 时钟 | 时钟电路 | `crystal=null`；`oscillator=null`；`clock_generator=null`；`clock_net=null` |
| 复位 | 复位与使能 | `reset=null`；`boot=null`；`enable=null` |
| 调试与烧录 | 调试接口 | `swd=null`；`jtag=null`；`uart_debug=null`；`test_points=null` |
| 存储 | 存储器 | `flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null` |
| 内存与 Flash | 内存与主控 | `mcu=null`；`soc=null`；`ram=null`；`psram=null`；`ddr=null` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s=null` |
| 传感器 | 传感器 | `sensor_ic=null`；`sensor_bus=null` |
| 射频 | 射频电路 | `rf_ic=null`；`antenna=null`；`matching=null` |
| 其他事实 | 电池与充电路径 | `battery=null`；`charger=null`；`fuel_gauge=null`；`power_path=J1 VCC -> J2 VCC` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `92c256599899d5d615176fcd50056b23c899c6d1a9c5f24087373f9fd77076d1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1206/U210_SCH_UNIT-Chain-Blank_V0.1_2024_11_29_20_14_27_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Blank.md`

源文档 SHA-256：`8d48f546951c2d30313c134fed40a127c7665a304c9fbf06618aeebd24329845`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
