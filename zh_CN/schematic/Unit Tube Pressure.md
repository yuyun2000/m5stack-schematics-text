# Unit Tube Pressure 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Tube Pressure |
| SKU | U130 |
| 产品 ID | `unit-tube-pressure-c550b29fbc78` |
| 源文档 | `zh_CN/unit/tube_pressure.md` |

## 概述

Unit Tube Pressure 使用 MCP-H10-B200KPPN（U2）压力传感器，将 VOUT.3 直接引到 J1.1 模拟输出，并以 C3 100nF 对地滤波。J1.3 输入 +5V，HT7533（U1）生成 +3.3V 供传感器 VDD.5；输入和输出各有 22uF 电容。J1.2 未连接、J1.4 接 GND，传感器 DNC.1/DNC.6 也未连接，VDDF.4 配置独立 100nF 对地电容。

## 检索关键词

`Unit Tube Pressure`、`U130`、`MCP-H10-B200KPPN`、`U2`、`HT7533`、`U1`、`VOUT`、`VDDF`、`VDD`、`DNC`、`analog output`、`HY-2.0_IO`、`J1`、`+5V`、`+3.3V`、`C1`、`C2`、`22uF`、`C3`、`C4`、`C5`、`100nF`、`-100~200Kpa`、`0.1~3.1V`、`1.5Kpa`、`K=100`、`B=-110`、`gas pressure`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | MCP-H10-B200KPPN | +3.3V 供电的管路压力传感器，VOUT 输出至 J1.1 | 图 a7fbec77b895 / 第 1 页 / 页面中央偏右：U2 标注 MCP-H10-B200KPPN，1~6 脚为 DNC/GND/VOUT/VDDF/VDD/DNC |
| U1 | HT7533 | 将 +5V 转换为 +3.3V，为 U2 VDD 供电 | 图 a7fbec77b895 / 第 1 页 / 页面上中：U1 HT7533，VIN.2 接 +5V、VOUT.3 接 +3.3V、GND.1 接地 |
| J1 | HY-2.0_IO | 模拟输出、+5V 与 GND 外部连接器，2 脚未连接 | 图 a7fbec77b895 / 第 1 页 / 页面左下：J1 HY-2.0_IO，1~4 脚标注 I/O/VCC/GND，2 脚带未连接标记 |
| C1 | 22uF | HT7533 +5V 输入去耦电容 | 图 a7fbec77b895 / 第 1 页 / 页面上中偏左：C1 22uF 从 +5V/U1.VIN 接 GND |
| C2 | 22uF | HT7533 +3.3V 输出去耦电容 | 图 a7fbec77b895 / 第 1 页 / 页面上中偏右：C2 22uF 从 +3.3V/U1.VOUT 接 GND |
| C3 | 100nF | U2 VOUT/J1.1 模拟输出到 GND 的滤波电容 | 图 a7fbec77b895 / 第 1 页 / 页面下中：C3 100nF 从 U2.VOUT.3/J1.1 网络接 GND |
| C4, C5 | 100nF | U2 VDDF.4 与 VDD.5 的对地去耦电容 | 图 a7fbec77b895 / 第 1 页 / 页面右下：C4 100nF 从 U2.VDDF.4 接 GND，C5 100nF 从 U2.VDD.5/+3.3V 接 GND |

## 系统结构

### Unit Tube Pressure

J1 输入 +5V，U1 HT7533 生成 +3.3V 为 U2 MCP-H10-B200KPPN 供电，U2.VOUT 作为模拟信号直接输出到 J1.1。

- 参数与网络：`sensor=U2 MCP-H10-B200KPPN`；`input=J1.3 +5V`；`regulator=U1 HT7533`；`sensor_supply=+3.3V`；`analog_output=U2.3 VOUT -> J1.1`
- 证据：图 a7fbec77b895 / 第 1 页 / 全页：J1-U1-U2 的 +5V/+3.3V/VOUT/GND 完整连接

## 电源

### U1 HT7533

U1.VIN.2 接 +5V，GND.1 接地，VOUT.3 输出 +3.3V；C1/C2（均 22uF）分别位于输入与输出。

- 参数与网络：`input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C1 22uF`；`output_capacitor=C2 22uF`
- 证据：图 a7fbec77b895 / 第 1 页 / 页面上半：U1 HT7533、C1/C2 与 +5V/+3.3V/GND

### U2 VDD/VDDF

U2.VDD.5 由 +3.3V 供电并由 C5（100nF）对地去耦；U2.VDDF.4 仅连接 C4（100nF）到 GND。

- 参数与网络：`VDD=+3.3V with C5 100nF`；`VDDF=C4 100nF to GND`；`ground=U2.2`
- 证据：图 a7fbec77b895 / 第 1 页 / 页面右下：U2.4/U2.5 与 C4/C5/+3.3V/GND

## 接口

### J1

J1.1（符号名 I）接 U2.VOUT.3，J1.2（符号名 O）未连接，J1.3 VCC 接 +5V，J1.4 GND 接地。

- 参数与网络：`connector=HY-2.0_IO`；`pin_1=I / analog output / U2.3 VOUT`；`pin_2=O / NC`；`pin_3=VCC / +5V input`；`pin_4=GND`；`signal_direction=pin1 output from unit`
- 证据：图 a7fbec77b895 / 第 1 页 / 页面左下至中部：J1.1~J1.4 与 U2.VOUT、未连接标记、+5V、GND

## 保护电路

### J1 外部接口

本页未显示 J1 的 TVS、保险丝、反接保护、串联限流或模拟过压钳位器件。

- 参数与网络：`tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown`；`analog_clamp=none shown`
- 证据：图 a7fbec77b895 / 第 1 页 / 全页：J1 至 U1/U2 的完整电源和模拟路径，仅有去耦电容

## 传感器

### U2 MCP-H10-B200KPPN

U2.1 与 U2.6 为 DNC 且未连接，U2.2 接 GND，U2.3 VOUT 接模拟输出，U2.4 VDDF 接 C4，U2.5 VDD 接 +3.3V。

- 参数与网络：`pin_1=DNC / NC`；`pin_2=GND`；`pin_3=VOUT / J1.1`；`pin_4=VDDF / C4 100nF to GND`；`pin_5=VDD / +3.3V`；`pin_6=DNC / NC`
- 证据：图 a7fbec77b895 / 第 1 页 / 页面中央偏右：U2 六脚名称、网络和 DNC 未连接标记

## 模拟电路

### VOUT 模拟输出

U2.VOUT.3 与 J1.1 直接连接，C3（100nF）从该网络接 GND；中间没有运放、分压器、串联电阻或 ADC。

- 参数与网络：`source=U2.3 VOUT`；`connector=J1.1`；`shunt_capacitor=C3 100nF`；`series_resistor=none shown`；`amplifier=none shown`；`adc=none shown`
- 证据：图 a7fbec77b895 / 第 1 页 / 页面左下至中央：J1.1-U2.VOUT.3 直连及 C3-GND 分支

## 其他事实

### 数字通信与控制

本页未显示 MCU、I2C、SPI、UART、地址、复位、时钟、存储或调试接口；对外数据仅为 J1.1 模拟电压。

- 参数与网络：`mcu=none shown`；`digital_bus=none shown`；`address=not applicable in schematic`；`clock_reset_storage_debug=none shown`；`external_data=analog VOUT only`
- 证据：图 a7fbec77b895 / 第 1 页 / 完整单页仅含 J1、U1 HT7533、U2 压力传感器和电容

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Tube Pressure | `sensor=U2 MCP-H10-B200KPPN`；`input=J1.3 +5V`；`regulator=U1 HT7533`；`sensor_supply=+3.3V`；`analog_output=U2.3 VOUT -> J1.1` |
| 接口 | J1 | `connector=HY-2.0_IO`；`pin_1=I / analog output / U2.3 VOUT`；`pin_2=O / NC`；`pin_3=VCC / +5V input`；`pin_4=GND`；`signal_direction=pin1 output from unit` |
| 传感器 | U2 MCP-H10-B200KPPN | `pin_1=DNC / NC`；`pin_2=GND`；`pin_3=VOUT / J1.1`；`pin_4=VDDF / C4 100nF to GND`；`pin_5=VDD / +3.3V`；`pin_6=DNC / NC` |
| 模拟电路 | VOUT 模拟输出 | `source=U2.3 VOUT`；`connector=J1.1`；`shunt_capacitor=C3 100nF`；`series_resistor=none shown`；`amplifier=none shown`；`adc=none shown` |
| 电源 | U1 HT7533 | `input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C1 22uF`；`output_capacitor=C2 22uF` |
| 电源 | U2 VDD/VDDF | `VDD=+3.3V with C5 100nF`；`VDDF=C4 100nF to GND`；`ground=U2.2` |
| 传感器 | MCP-H10-B200KPPN 性能 | `documented_medium=gas`；`documented_range=-100~200Kpa`；`documented_output=0.1~3.1V`；`documented_accuracy=±1.5Kpa at 0~85°C`；`schematic_values=未标注` |
| 模拟电路 | VOUT 到压力换算 | `documented_formula=P[kPa] = 100 * Vout[V] - 110`；`K=100`；`B=-110`；`hardware_calibration=none shown` |
| 保护电路 | J1 外部接口 | `tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown`；`analog_clamp=none shown` |
| 其他事实 | 数字通信与控制 | `mcu=none shown`；`digital_bus=none shown`；`address=not applicable in schematic`；`clock_reset_storage_debug=none shown`；`external_data=analog VOUT only` |

## 待确认事项

- `sensor.range-output-accuracy-unconfirmed`：正文称测量气体、范围 -100~200Kpa、输出 0.1~3.1V、精度 ±1.5Kpa（0~85°C）；这些参数未在原理图中标注。（证据：图 a7fbec77b895 / 第 1 页 / 页面中央偏右：U2 仅标器件型号和引脚，没有量程、介质、输出范围或精度文字）
- `analog.pressure-conversion-unconfirmed`：正文给出 P=100×Vout-110（K=100、B=-110）的换算关系；原理图只显示 VOUT 直连，没有系数、偏移或校准网络。（证据：图 a7fbec77b895 / 第 1 页 / J1.1-U2.VOUT.3 直连路径，仅有 C3 100nF 对地）
- `review.sensor-performance`：MCP-H10-B200KPPN 的量产规格是否为气体介质、-100~200Kpa、0.1~3.1V、±1.5Kpa（0~85°C）？；原因：原理图确认型号但不含性能参数，需要传感器规格书、BOM 或标定/实测数据。
- `review.pressure-formula`：P=100×Vout-110 是否适用于当前 U2 批次、供电和温度范围，是否还需要零点/增益校准？；原因：换算系数不在硬件图中，且 VOUT 未经过板级校准电路，需以传感器规格与标定数据确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a7fbec77b8955dc32bb560c807371e29141b9496b46b8c5d587551cd4e66c4c5` | `https://static-cdn.m5stack.com/resource/docs/products/unit/tube_pressure/tube_pressure_sch_01.webp` |

---

源文档：`zh_CN/unit/tube_pressure.md`

源文档 SHA-256：`3a98113bd9b3a6db5d668b7f6b26714c13ca3e913fdae65b23bc511fe26141f8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
