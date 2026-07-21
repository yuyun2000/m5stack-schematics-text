# Unit Watering 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Watering |
| SKU | U101 |
| 产品 ID | `unit-watering-9305c7e679f8` |
| 源文档 | `zh_CN/unit/watering.md` |

## 概述

Unit Watering 由水泵驱动板和电容传感板两部分组成。资源 1 的 P1 引出 CAP/MOT/VIN/GND，MOT 控制 Q1 SI2302 低侧开关，D1 1N4148 跨接 Motor+/Motor-，P2 传递 GND/VIN/CAP。资源 2 以 U2 XC6206 将 VCC 转为 3V3，U1 TLC555I 产生 PAD 激励，D1 4148 将 PAD 信号传至 CAP，R4/C4 与 D2 ZMM3V3 对 CAP 进行负载、滤波和钳位。两页没有 MCU 或数字总线；CAP 是模拟输出，MOT 是水泵开关输入。

## 检索关键词

`Unit Watering`、`U101`、`SI2302-N-Ch-MOSFET`、`TLC555I`、`XC6206`、`1N4148`、`ZMM3V3`、`PUMP_EN`、`Analog Output`、`CAP`、`MOT`、`VIN`、`VCC`、`Motor+`、`Motor-`、`PAD`、`3V3`、`GND`、`P1 Header 4`、`P2 Header 3H`、`R1 10KΩ`、`C1 22uF`、`R3 3300`、`R2 162`、`C3 681`、`R1 103`、`R4 105`、`C4 105`、`D2`、`capacitive soil moisture`、`water pump`、`5W`、`Grove PORT.B`、`low-side MOSFET`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| Q1 | SI2302-N-Ch-MOSFET | 由 MOT 控制的水泵低侧 N 沟道 MOSFET | 图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页网格 B2-C2，Q1 SI2302-N-Ch-MOSFET、MOT、Motor-、GND |
| D1 | 1N4148 | 跨接 Motor+ VIN 与 Motor- 的水泵续流/反电动势钳位二极管 | 图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页网格 B2-C2，D1 1N4148 位于 Motor+ VIN 与 Motor- 之间 |
| P1 | Header 4 | 四针外部接口，pin1 CAP、pin2 MOT、pin3 VIN、pin4 GND | 图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页网格 B2-C3，P1 Header 4 pin1-pin4 |
| P2 | Header 3H | 主板侧三针传感板接口，pin1 GND、pin2 VIN、pin3 CAP | 图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页网格 C3，P2 Header 3H pin1 GND、pin2 VIN、pin3 CAP |
| C1 | 22uF | 资源 1 中 CAP 至 GND 的附加模拟输出滤波电容 | 图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页网格 B2-C3，P1 CAP/GND 之间的 C1 22uF |
| U2 | XC6206 | 传感板 VCC 至 3V3 的 LDO | 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页网格 B2，U2 XC6206、C1/C2/C5/C6 |
| U1 | TLC555I | 产生电容式测量 PAD 激励的 555 定时器/振荡器 | 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页网格 C2-D2，U1 TLC555I pin1-pin8 |
| D1,D2 | 4148 / ZMM3V3 | 传感板 PAD 到 CAP 的整流二极管与 CAP 对地 3.3V 稳压钳位 | 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页网格 C2-C3，D1 4148 与 D2 ZMM3V3 |
| Header 3H | 未标注 | 传感板三针接口，pin1 CAP、pin2 VCC、pin3 GND | 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页网格 C3，Header 3H pin1 CAP、pin2 VCC、pin3 GND |
| R1,R2,R3,C3 | 103 / 162 / 3300 / 681±5% | TLC555I 的输出串阻与定时网络 | 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页网格 C2-D2，R3/R2/C3 定时网络及 OUT-R1-PAD |

## 系统结构

### Unit Watering 双板架构

资源 1 展开水泵低侧驱动、P1 外部接口和 P2 传感板接口；资源 2 展开 VCC/3V3 电源、TLC555I PAD 激励和 CAP 模拟输出。系统没有 MCU，外部主机直接读取 CAP 并驱动 MOT。

- 参数与网络：`pump_board=P1/P2,Q1,D1,C1`；`sensor_board=U2 XC6206,U1 TLC555I,PAD/CAP`；`control_input=MOT`；`analog_output=CAP`；`controller=null`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页完整泵驱动电路; 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页完整传感电路

### 数字与通信子系统

两页均未画 MCU、协处理器、存储器、I2C、SPI、UART、CAN、RS-485、USB、射频、音频、数字地址、复位或调试接口；唯一主动时基为 U1 TLC555I。

- 参数与网络：`mcu=null`；`coprocessor=null`；`storage=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`rf=null`；`audio=null`；`address=null`；`debug=null`；`timer=U1 TLC555I`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页完整原理图; 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页完整原理图

## 电源

### 水泵功率路径

Motor+ 与 VIN 同网，Motor- 接 Q1 漏极，Q1 源极接 GND，形成 VIN/Motor+ 至 Motor-、Q1、GND 的低侧开关路径；实际水泵符号未画在页内。

- 参数与网络：`high_side=Motor+ VIN`；`low_side=Motor- -> Q1 drain`；`return=Q1 source -> GND`；`pump_symbol=null`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 Motor+ VIN、Motor- 与 Q1

### 传感板 VCC 至 3V3

U2 XC6206 VIN pin3 接 VCC，OUT pin2 输出 3V3，GND pin1 接地；C1 226/C2 104 位于输入端，C5 104/C6 226 位于输出端。

- 参数与网络：`input=VCC`；`regulator=U2 XC6206`；`output=3V3`；`input_caps=C1 226,C2 104`；`output_caps=C5 104,C6 226`
- 证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 U2 XC6206、C1/C2/C5/C6

## 接口

### P1 四针外部接口

P1 Header4 pin1=CAP 模拟输出、pin2=MOT 水泵控制输入、pin3=VIN 电源输入、pin4=GND。CAP/MOT/VIN/GND 分别对应产品的 Analog Output/PUMP_EN/电源/地功能。

- 参数与网络：`connector=P1 Header 4`；`pin1=CAP analog output`；`pin2=MOT pump control input`；`pin3=VIN power input`；`pin4=GND`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 P1 CAP/MOT/VIN/GND

## GPIO 与控制信号

### MOT 水泵使能输入

P1 pin2 MOT 直接连接 Q1 SI2302 栅极，R1 10KΩ将 MOT/Q1 栅极下拉至 GND；MOT 高电平使 Q1 低侧开关导通，默认由 R1 保持关断。

- 参数与网络：`input=P1 pin2 MOT`；`mosfet=Q1 SI2302-N-Ch-MOSFET`；`pulldown=R1 10KΩ to GND`；`active_level=high`；`default=off`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 MOT、Q1 gate、R1 10KΩ

## 时钟

### TLC555I PAD 激励振荡器

U1 TLC555I VCC pin8 与 RST pin4 接 3V3，DIS pin7 连接 R3/R2 定时节点，THR pin6 与 TRI pin2 并接 R2/C3 节点；R3 标 3300、R2 标 162、C3 标 681±5%，CON pin5 经 C7 103 接 GND。

- 参数与网络：`timer=U1 TLC555I`；`supply=pin8 3V3`；`reset=pin4 3V3`；`discharge=pin7 R3/R2`；`threshold_trigger=pins6/2 R2/C3`；`timing=R3 3300,R2 162,C3 681±5%`；`control_cap=C7 103`
- 证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 U1 TLC555I 与 R2/R3/C3/C7

## 保护电路

### 水泵续流二极管

D1 1N4148 跨接 Motor+ VIN 与 Motor-，为感性水泵负载提供关断续流/反电动势钳位路径。

- 参数与网络：`device=D1 1N4148`；`connections=Motor+ VIN to Motor-`；`protected_path=pump/Q1`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 D1 跨接 Motor+ VIN/Motor-

### CAP 3.3V 钳位

D2 ZMM3V3 从 CAP 接至 GND，对 CAP 模拟输出提供 3.3V 稳压钳位；图中未画 VIN/VCC 输入保险丝、反接保护或外部接口 ESD。

- 参数与网络：`clamp=D2 ZMM3V3 CAP-GND`；`input_fuse=null`；`reverse_protection=null`；`esd=null`
- 证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 D2 ZMM3V3 与完整输入接口

## 模拟电路

### 主板 CAP 输出滤波

P1 pin1 CAP 与 P2 pin3 CAP 同网，C1 22uF 从 CAP 接至 GND，对模拟输出提供附加滤波。

- 参数与网络：`network=CAP`；`external_pin=P1 pin1`；`sensor_header=P2 pin3`；`capacitor=C1 22uF to GND`
- 证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 P1/P2 CAP 与 C1 22uF

### PAD 电容极板激励

U1 OUT pin3 经 R1 103 串联后驱动 PAD；PAD 同时连接 D1 4148 一端，构成电容式测量激励节点。

- 参数与网络：`source=U1 OUT pin3`；`series=R1 103`；`network=PAD`；`rectifier=D1 4148`
- 证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 U1 OUT-R1-PAD-D1

### CAP 整流滤波输出

D1 4148 连接 PAD 与 CAP；CAP 通过 R4 105 与 C4 105 接 GND，并引出至传感板 Header3H pin1，形成经整流、负载和滤波后的模拟输出。

- 参数与网络：`input=PAD`；`diode=D1 4148`；`output=CAP`；`load=R4 105 to GND`；`filter=C4 105 to GND`；`connector=Header3H pin1`
- 证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 PAD/D1/CAP/R4/C4/Header3H

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Watering 双板架构 | `pump_board=P1/P2,Q1,D1,C1`；`sensor_board=U2 XC6206,U1 TLC555I,PAD/CAP`；`control_input=MOT`；`analog_output=CAP`；`controller=null` |
| 系统结构 | 数字与通信子系统 | `mcu=null`；`coprocessor=null`；`storage=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`rf=null`；`audio=null`；`address=null`；`debug=null`；`timer=U1 TLC555I` |
| 接口 | P1 四针外部接口 | `connector=P1 Header 4`；`pin1=CAP analog output`；`pin2=MOT pump control input`；`pin3=VIN power input`；`pin4=GND` |
| GPIO 与控制信号 | MOT 水泵使能输入 | `input=P1 pin2 MOT`；`mosfet=Q1 SI2302-N-Ch-MOSFET`；`pulldown=R1 10KΩ to GND`；`active_level=high`；`default=off` |
| 电源 | 水泵功率路径 | `high_side=Motor+ VIN`；`low_side=Motor- -> Q1 drain`；`return=Q1 source -> GND`；`pump_symbol=null` |
| 保护电路 | 水泵续流二极管 | `device=D1 1N4148`；`connections=Motor+ VIN to Motor-`；`protected_path=pump/Q1` |
| 模拟电路 | 主板 CAP 输出滤波 | `network=CAP`；`external_pin=P1 pin1`；`sensor_header=P2 pin3`；`capacitor=C1 22uF to GND` |
| 电源 | 传感板 VCC 至 3V3 | `input=VCC`；`regulator=U2 XC6206`；`output=3V3`；`input_caps=C1 226,C2 104`；`output_caps=C5 104,C6 226` |
| 时钟 | TLC555I PAD 激励振荡器 | `timer=U1 TLC555I`；`supply=pin8 3V3`；`reset=pin4 3V3`；`discharge=pin7 R3/R2`；`threshold_trigger=pins6/2 R2/C3`；`timing=R3 3300,R2 162,C3 681±5%`；`control_cap=C7 103` |
| 模拟电路 | PAD 电容极板激励 | `source=U1 OUT pin3`；`series=R1 103`；`network=PAD`；`rectifier=D1 4148` |
| 模拟电路 | CAP 整流滤波输出 | `input=PAD`；`diode=D1 4148`；`output=CAP`；`load=R4 105 to GND`；`filter=C4 105 to GND`；`connector=Header3H pin1` |
| 保护电路 | CAP 3.3V 钳位 | `clamp=D2 ZMM3V3 CAP-GND`；`input_fuse=null`；`reverse_protection=null`；`esd=null` |
| 接口 | 主板 P2 与传感板 Header3H 配接 | `main_header=P2: 1 GND,2 VIN,3 CAP`；`sensor_header=Header3H: 1 CAP,2 VCC,3 GND`；`vin_vcc_alias=null`；`mating_orientation=null` |
| 电源 | 外部供电电压 | `documented_voltage=5V`；`schematic_names=VIN,VCC,Motor+`；`input_range=null`；`startup_current=null`；`continuous_current=null` |
| 核心器件 | 集成水泵额定功率 | `documented_power=5W`；`schematic_nets=Motor+,Motor-`；`pump_reference=null`；`model=null`；`rated_voltage=null`；`current=null`；`flow=null`；`head=null`；`stall=null` |
| 传感器 | 电容式土壤湿度测量性能 | `documented_method=capacitive soil moisture`；`excitation=TLC555I -> PAD`；`output=CAP`；`plate=null`；`frequency=null`；`output_range=null`；`accuracy=null`；`temperature_drift=null`；`calibration=null` |

## 待确认事项

- `interface.sensor-board-link`：资源 1 P2 标为 pin1 GND、pin2 VIN、pin3 CAP；资源 2 Header3H 标为 pin1 CAP、pin2 VCC、pin3 GND。两页未显示连接器朝向、针号翻转或 VIN/VCC 同名连接，无法仅凭页内网络确认物理配接针序。（证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 P2 pin1-pin3; 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 Header3H pin1-pin3）
- `power.documented-5v`：产品正文管脚表将电源标为 5V；原理图仅使用 VIN/VCC/Motor+ 网络名，没有直接标注 5V、允许输入范围、启动电流或最大持续电流。（证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 VIN/Motor+; 图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 VCC/U2）
- `component.documented-pump`：产品正文称集成 5W 水泵；资源 1 只显示 Motor+/Motor- 网络和驱动电路，没有水泵位号、型号、额定功率、电压、电流、流量、扬程或堵转参数。（证据：图 e67c0de97d0f / 第 1 页 / 资源 1 第 1 页 Motor+/Motor-，无泵器件符号）
- `sensor.documented-capacitive`：产品正文称采用电容式土壤湿度极板并输出湿度信号；原理图确认 PAD 激励与 CAP 模拟链，但未标极板尺寸/材料、振荡频率、CAP 电压范围、湿度换算、精度、温漂或校准方法。（证据：图 a6175c7f6853 / 第 1 页 / 资源 2 第 1 页 TLC555I/PAD/CAP 链路，无传感性能参数）
- `review.board-link`：请通过 PCB 网表、连接器实物朝向或导通测试确认 P2 与传感板 Header3H 的 GND/VIN-VCC/CAP 配接针序。；原因：两页针号顺序相反且 VIN/VCC 名称不同。
- `review.input-rating`：请依据当前产品规格和实测确认 VIN/VCC 的 5V 额定值、允许范围及水泵启动/持续电流边界。；原因：原理图没有输入电压和电流额定值。
- `review.pump`：请用量产 BOM、水泵标签或测试报告确认 5W 水泵型号、额定电流、启动/堵转电流、流量和扬程。；原因：原理图未画水泵器件，仅有 Motor+/Motor- 网络。
- `review.moisture-calibration`：请通过传感极板设计、标定数据和实测确认振荡频率、CAP 输出范围、湿度换算、精度与温漂。；原因：原理图只给出 TLC555I/PAD/CAP 电路，不能证明整机测量性能。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e67c0de97d0f98cb0406fe437f74484e7a44d6e1cc97945a30de6be6618c6cfe` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101_Unit-Watering_SCH_page_01.png` |
| 2 | 1 | `a6175c7f6853e3491809b16bddfe10a62f99b1814b2f1f568ad9ab8d5185002c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101_Unit-Watering_SCH_page_02.png` |

---

源文档：`zh_CN/unit/watering.md`

源文档 SHA-256：`369613ef47e6c5be10c252e411cba3b3fdfeb27ac84abd172db7ebaa2ba46fc8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
