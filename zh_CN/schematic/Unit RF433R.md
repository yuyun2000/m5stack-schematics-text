# Unit RF433R 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RF433R |
| SKU | U113 |
| 产品 ID | `unit-rf433r-7245b9cbf66d` |
| 源文档 | `zh_CN/unit/rf433_r.md` |

## 概述

Unit RF433R（U113）以 U1 SYN531R 射频接收器为核心，直接使用 +5V，并由 Y1 13.51783MHz 谐振器提供参考频率；图内标注工作频率 433.92MHz 和 1KHz Baud Rate。射频输入从 E1 ANT_IPEX 经 L1 27nH、C3 5pF、C2 3.7pF、L2 33nH 匹配网络进入 U1 ANT，数字输出 DO 经 R1 22Ω 送到 J1 pin 1。J1 pin 2 未连接，pin 3/4 为 +5V/GND；原理图未显示主控、标准串行总线、保护或存储器。图纸的 IPEX 天线接口与产品正文的 PCB 天线描述存在冲突，调制方式、灵敏度/距离和输出逻辑也未由本页确认。

## 检索关键词

`Unit RF433R`、`U113`、`RF433R`、`SYN531R`、`U1`、`433.92MHz`、`1KHz Baud Rate`、`13.51783MHz`、`Y1`、`ANT_IPEX`、`E1`、`RF matching`、`L1 27nH`、`C3 5pF`、`C2 3.7pF`、`L2 33nH`、`DO`、`R1 22Ω`、`SHDN`、`R2 1KΩ`、`C_AGC`、`CTH`、`C11 100nF`、`C4 1uF`、`J1 HY-2.0_IO`、`+5V`、`GND`、`pin 1 RF_RX`、`pin 2 NC`、`ASK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SYN531R | 433.92MHz 射频接收器，连接天线匹配、参考谐振器、AGC/CTH、关断与数字输出 | 图 fdb0b1f0cb57 / 第 1 页 / 页面中央 U1 SYN531R，pins 1~8 ANT/GND/VDD/SHDN/DO/CTH/C_AGC/RO |
| E1 | ANT_IPEX | 外部射频天线连接器 | 图 fdb0b1f0cb57 / 第 1 页 / 页面左侧 E1 ANT_IPEX，信号端连接匹配网络 |
| Y1 | 13.51783MHz | SYN531R RO pin 8 的参考谐振器，另一端接地 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 右上 pin 8 RO-Y1 13.51783MHz-GND |
| J1 | HY-2.0_IO | 四针接收数据输出与 +5V 电源接口 | 图 fdb0b1f0cb57 / 第 1 页 / 页面右下 J1 HY-2.0_IO，pin 1 I、pin 2 O/NC、pin 3 VCC/+5V、pin 4 GND |
| L1 | 27nH ±5% | E1 天线节点到 GND 的并联射频电感 | 图 fdb0b1f0cb57 / 第 1 页 / 页面左侧 E1 后 L1 27nH ±5% 到 GND |
| C3 | 5pF (5R0) 0.25pF | E1 天线节点到 GND 的并联射频电容 | 图 fdb0b1f0cb57 / 第 1 页 / 页面天线节点 C3 5pF (5R0) 0.25pF 到 GND |
| C2 | 3.7pF (3R7) 0.25pF | 射频输入匹配路径的串联电容 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 E1/C3 节点与 U1 ANT 之间 C2 3.7pF (3R7) 0.25pF |
| L2 | 33nH ±5% | C2 后、U1 ANT 前节点到 GND 的并联射频电感 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 C2 后射频节点 L2 33nH ±5% 到 GND，节点连接 U1 pin1 ANT |
| R1 | 22Ω | U1 DO 到 J1 pin 1 的串联数字输出电阻 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 pin5 DO-R1 22Ω-J1 pin1 |
| R2 | 1KΩ | U1 SHDN pin 4 到 GND 的下拉电阻 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 pin4 SHDN-R2 1KΩ-GND |
| C11/C4 | 100nF/1uF | U1 CTH 与 C_AGC 引脚的对地定时/AGC 电容 | 图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 pins 6/7 CTH/C_AGC 到 C11 100nF、C4 1uF，再接 GND |
| C10/C1 | 100nF/10uF | +5V 输入轨的并联去耦与储能电容 | 图 fdb0b1f0cb57 / 第 1 页 / 页面右下 J1 旁 +5V-C10 100nF/C1 10uF-GND |

## 系统结构

### Unit RF433R 系统架构

U1 SYN531R 接收 E1 ANT_IPEX 经四元件匹配网络输入的射频信号，使用 Y1 13.51783MHz 参考，并将 DO 经 R1 输出到 J1；全板直接使用 +5V。

- 参数与网络：`receiver=U1 SYN531R`；`antenna=E1 ANT_IPEX`；`matching=L1/C3/C2/L2`；`reference=Y1 13.51783MHz`；`output=U1 DO -> R1 22Ω -> J1 pin1`；`power=+5V`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 整页 E1/L1/C2/C3/L2/U1/Y1/R1/J1 与 +5V/GND

## 核心器件

### U1 SYN531R 引脚

U1 pins 1~8 依次为 ANT、GND、VDD、SHDN、DO、CTH、C_AGC、RO。

- 参数与网络：`pin_1=ANT`；`pin_2=GND`；`pin_3=VDD +5V`；`pin_4=SHDN`；`pin_5=DO`；`pin_6=CTH`；`pin_7=C_AGC`；`pin_8=RO`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面中央 U1 SYN531R pins 1~8 名称与网络

## 电源

### +5V 电源路径

J1 pin 3 +5V 直接连接 U1 VDD pin 3，并由 C10 100nF 与 C1 10uF 对地去耦；本页没有稳压器、DC/DC 或负载开关。

- 参数与网络：`input=J1 pin3 +5V`；`load=U1 pin3 VDD`；`capacitors=C10 100nF,C1 10uF`；`regulator=null`；`dc_dc=null`；`load_switch=null`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 J1 +5V、U1 VDD 与 C10/C1，同页无电源转换器

## 接口

### J1 HY-2.0_IO 针脚

J1 pin 1 标注 I 并连接 U1 DO 输出，pin 2 标注 O 且未连接，pin 3 为 VCC/+5V，pin 4 为 GND。

- 参数与网络：`pin_1=I-RF_RX`；`pin_2=O-NC`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面右下 J1 pins 1~4 与 I/NC/+5V/GND

## 总线

### 外部总线

本页对外仅有单路 DO 数据输出，未显示 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`data_output=DO`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 整页 J1 只有 DO/+5V/GND，pin2 NC

## GPIO 与控制信号

### SHDN 配置

U1 SHDN pin 4 通过 R2 1KΩ 下拉到 GND，页面没有外部主机控制或切换器件。

- 参数与网络：`pin=U1 pin4 SHDN`；`pulldown=R2 1KΩ to GND`；`external_control=null`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 pin4 SHDN-R2 1KΩ-GND

### 接收数据输出

U1 DO pin 5 经 R1 22Ω 串联到 J1 pin 1 I，信号方向为接收器到外部主机。

- 参数与网络：`source=U1 pin5 DO`；`series=R1 22Ω`；`destination=J1 pin1 I`；`direction=unit to host`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 DO-R1-J1 pin1 连线

## 时钟

### SYN531R 参考谐振器

U1 RO pin 8 连接 Y1 pin 1，Y1 标注 13.51783MHz，Y1 pin 2 接 GND。

- 参数与网络：`receiver_pin=U1 pin8 RO`；`resonator=Y1 13.51783MHz`；`return=GND`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 右上 RO-Y1 13.51783MHz-GND

## 保护电路

### 天线、输出与电源保护

E1 射频输入、J1 DO 输出和 +5V 电源路径未显示 TVS/ESD、保险丝、反接或过压保护器件。

- 参数与网络：`rf_tvs=null`；`output_tvs=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 整页 E1/U1/J1 路径，无保护器件符号或位号

## 存储

### 存储、复位与调试

本页未显示主控、Flash、EEPROM、RAM、SD 卡、RESET、BOOT 或调试接口。

- 参数与网络：`controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`；`reset=null`；`boot=null`；`debug=null`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 整页仅接收器、匹配/阻容、谐振器与连接器

## 射频

### 天线到 SYN531R 匹配网络

E1 信号节点并联 L1 27nH 和 C3 5pF 到 GND，经 C2 3.7pF 串联后，在 U1 ANT 前并联 L2 33nH 到 GND。

- 参数与网络：`connector=E1 ANT_IPEX`；`first_shunt=L1 27nH,C3 5pF`；`series=C2 3.7pF`；`second_shunt=L2 33nH`；`destination=U1 pin1 ANT`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面左侧完整 E1-L1/C3-C2-L2-U1 ANT 射频路径

### 工作频率与数据率标注

原理图在 U1 下方明确标注 433.92MHz, 1KHz Baud Rate。

- 参数与网络：`frequency=433.92MHz`；`baud_annotation=1KHz Baud Rate`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 SYN531R 下方文字 433.92MHz, 1KHz Baud Rate

## 模拟电路

### AGC 与 CTH 外围

U1 CTH pin 6 和 C_AGC pin 7 分别连接对地电容 C11 100nF 与 C4 1uF。

- 参数与网络：`cth=U1 pin6 -> C11 100nF -> GND`；`agc=U1 pin7 -> C4 1uF -> GND`
- 证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 右侧 pins 6/7 到 C11/C4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RF433R 系统架构 | `receiver=U1 SYN531R`；`antenna=E1 ANT_IPEX`；`matching=L1/C3/C2/L2`；`reference=Y1 13.51783MHz`；`output=U1 DO -> R1 22Ω -> J1 pin1`；`power=+5V` |
| 核心器件 | U1 SYN531R 引脚 | `pin_1=ANT`；`pin_2=GND`；`pin_3=VDD +5V`；`pin_4=SHDN`；`pin_5=DO`；`pin_6=CTH`；`pin_7=C_AGC`；`pin_8=RO` |
| 射频 | 天线到 SYN531R 匹配网络 | `connector=E1 ANT_IPEX`；`first_shunt=L1 27nH,C3 5pF`；`series=C2 3.7pF`；`second_shunt=L2 33nH`；`destination=U1 pin1 ANT` |
| 射频 | 工作频率与数据率标注 | `frequency=433.92MHz`；`baud_annotation=1KHz Baud Rate` |
| 时钟 | SYN531R 参考谐振器 | `receiver_pin=U1 pin8 RO`；`resonator=Y1 13.51783MHz`；`return=GND` |
| 模拟电路 | AGC 与 CTH 外围 | `cth=U1 pin6 -> C11 100nF -> GND`；`agc=U1 pin7 -> C4 1uF -> GND` |
| GPIO 与控制信号 | SHDN 配置 | `pin=U1 pin4 SHDN`；`pulldown=R2 1KΩ to GND`；`external_control=null` |
| GPIO 与控制信号 | 接收数据输出 | `source=U1 pin5 DO`；`series=R1 22Ω`；`destination=J1 pin1 I`；`direction=unit to host` |
| 接口 | J1 HY-2.0_IO 针脚 | `pin_1=I-RF_RX`；`pin_2=O-NC`；`pin_3=VCC +5V`；`pin_4=GND` |
| 电源 | +5V 电源路径 | `input=J1 pin3 +5V`；`load=U1 pin3 VDD`；`capacitors=C10 100nF,C1 10uF`；`regulator=null`；`dc_dc=null`；`load_switch=null` |
| 保护电路 | 天线、输出与电源保护 | `rf_tvs=null`；`output_tvs=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null` |
| 总线 | 外部总线 | `data_output=DO`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 存储 | 存储、复位与调试 | `controller=null`；`flash=null`；`eeprom=null`；`ram=null`；`sd=null`；`reset=null`；`boot=null`；`debug=null` |
| 射频 | 天线实现 | `schematic=E1 ANT_IPEX`；`pcb_antenna_visible=false`；`conflicting_product_doc=PCB antenna`；`assembled_antenna=null` |
| 射频 | 调制与接收性能 | `frequency=433.92MHz`；`baud_annotation=1KHz Baud Rate`；`modulation=null`；`sensitivity=null`；`distance=null`；`current=null`；`selectivity=null`；`noise_rejection=null` |
| GPIO 与控制信号 | DO 输出逻辑与电平 | `idle_level=null`；`active_level=null`；`output_structure=null`；`encoding=null`；`voltage_range=null`；`host_threshold=null` |
| GPIO 与控制信号 | SHDN 有效极性 | `strap=R2 1KΩ to GND`；`active_level=null`；`resulting_state=null`；`shutdown_current=null` |

## 待确认事项

- `rf.antenna-implementation`：原理图明确显示 E1 ANT_IPEX 外部天线连接器，没有绘制 PCB 天线；源产品文字称为 PCB 天线，实际装配实现存在冲突。（证据：图 fdb0b1f0cb57 / 第 1 页 / 页面左侧 E1 ANT_IPEX 与匹配网络，整页无 PCB 天线图形/网络）
- `rf.modulation-performance`：原理图标注 433.92MHz 和 1KHz Baud Rate，但未标注 ASK 调制、接收灵敏度、稳定距离、工作电流、选择性或噪声抑制指标。（证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 下方仅 433.92MHz, 1KHz Baud Rate，无其他射频性能文字）
- `gpio.output-logic`：原理图未说明 DO 的空闲/接收高低电平、输出结构、脉冲编码、电压范围或主机阈值。（证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 DO-R1-J1 pin1，仅有电气连接，无逻辑说明）
- `gpio.shutdown-polarity`：SHDN 通过 R2 1KΩ 固定下拉到 GND，但本页没有标注 SHDN 的有效极性、启动状态或关断电流。（证据：图 fdb0b1f0cb57 / 第 1 页 / 页面 U1 pin4 SHDN-R2-GND，无极性符号或说明）
- `review.antenna-implementation`：U113 实际使用 IPEX 外接天线还是 PCB 天线，E1 是否装配？；原因：原理图显示 ANT_IPEX，产品正文称 PCB 天线，需 PCB/BOM/实物消除冲突。
- `review.modulation-performance`：该版本的调制方式、灵敏度、通信距离、工作电流和选择性指标是什么？；原因：原理图只标频率和速率，其他性能需 datasheet 与整机测试确认。
- `review.output-logic`：DO 的空闲/有效逻辑、电压、输出结构和解码格式是什么？；原因：图中只有 DO 物理路径，没有逻辑或接口电平定义。
- `review.shutdown-polarity`：SYN531R SHDN 的有效极性是什么，R2 下拉对应正常工作还是关断？；原因：原理图只显示下拉连接，没有有效电平说明。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fdb0b1f0cb57b34286c54e8c9e2388d218931466f1abe306540354129b13e7c9` | `https://static-cdn.m5stack.com/resource/docs/products/unit/rf433_r/rf433_r_sch_01.webp` |

---

源文档：`zh_CN/unit/rf433_r.md`

源文档 SHA-256：`0358e5b6ca124e126466fdf20b86c6260df4d78601ca6658677fc949a16658e8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
