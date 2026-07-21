# Unit CO2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CO2 |
| SKU | U103 |
| 产品 ID | `unit-co2-0262cfa83a1c` |
| 源文档 | `zh_CN/unit/co2.md` |

## 概述

Unit CO2 以 SCD40（U2）为传感器，通过 J1 的 SCL/SDA 直接连接外部 I2C 主机，两条总线各由 15KΩ 上拉到 +3.3V。J1 输入的 +5V 经 SY8089AAAC（U1）、L1 4.7uH 和 R1/R2 反馈网络转换为 +3.3V，为 U2 的 VDD/VDDH 供电。SCL/SDA、+5V 与 +3.3V 均配置独立保护器件，输入电源另串接标注 6V@1A 的 F1。原理图未打印 I2C 地址或 SCD40 的 CO2、温度和湿度测量参数。

## 检索关键词

`Unit CO2`、`U103`、`SCD40`、`SY8089AAAC`、`L1 3015 4.7uH`、`HY-2.0_IIC`、`I2C`、`0x62`、`SCL`、`SDA`、`IIC_SCL`、`IIC_SDA`、`VDD`、`VDDH`、`+5V`、`+3.3V`、`R1 68KΩ`、`R2 15KΩ`、`R3 15KΩ`、`R4 15KΩ`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`6V@1A`、`CO2`、`temperature`、`humidity`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SCD40 | 通过 I2C 输出测量数据的 CO2 环境传感器 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 C2：U2 SCD40，VDD pin 7、VDDH pin 19、SCL pin 9、SDA pin 10、GND pin 6 |
| U1 | SY8089AAAC | 将 +5V 转换为 +3.3V 的降压转换器 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B2：U1 SY8089AAAC，IN pin 4、EN pin 1、LX pin 3、FB pin 5、GND pin 2 |
| L1/R1/R2 | 3015 4.7uH / 68KΩ / 15KΩ | U1 的降压输出电感和反馈分压网络 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1-B2：U1 LX-L1 3015 4.7uH-+3.3V，R1 68KΩ/R2 15KΩ 连接 FB pin 5 |
| C1-C4 | 100nF / 22uF / 22uF / 100nF | U1 +3.3V 输出与 +5V 输入去耦电容 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1-B2：C1 100nF/C2 22uF 跨 +3.3V-GND，C3 22uF/C4 100nF 跨 +5V-GND |
| R3/R4 | 15KΩ | SCL 与 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 C1-C2：R3/R4 均 15KΩ，上端接 +3.3V，下端接 SCL/SDA |
| C5/C6 | 100nF | +3.3V 传感器电源去耦电容 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-C2：C5/C6 各 100nF，跨接 +3.3V 与 GND |
| J1 | HY-2.0_IIC | 外部 I2C、+5V 与 GND 接口 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B4-C4：J1 HY-2.0_IIC，pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC、pin 4 GND |
| F1 | 6V@1A | J1 VCC 输入与 +5V 板内电源之间的串联保护器件 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-B4：+5V 到 J1 pin 3 路径上的 F1，标注 6V@1A |
| D1/D2 | RLSD52A031V | SCL 与 SDA 到 GND 的接口保护器件 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-B4：D1/D2 均标 RLSD52A031V，分别跨 SCL-GND 与 SDA-GND |
| D3 | RLSD52A031V | +3.3V 到 GND 的电源轨保护器件 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1：D3 RLSD52A031V 跨接 +3.3V 与 GND |
| D4 | LESD3Z5.0CMT1G | J1 VCC/+5V 输入到 GND 的保护器件 | 图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B4-C4：D4 LESD3Z5.0CMT1G 从 J1 pin 3 VCC/+5V 节点接至 GND |

## 系统结构

### Unit CO2

J1 输入 +5V 并引出 SCL/SDA，U1 SY8089AAAC 产生 +3.3V，U2 SCD40 由 +3.3V 供电并直接连接 I2C；接口和两条电源轨均配置保护器件。

- 参数与网络：`sensor=U2 SCD40`；`communication=J1 SCL/SDA`；`power=+5V->U1 SY8089AAAC->+3.3V`；`signal_protection=D1,D2`；`power_protection=F1,D3,D4`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 整页：U1/U2/J1、+5V/+3.3V、SCL/SDA 与 D1-D4/F1

## 电源

### U1 SY8089AAAC

U1 IN pin 4 与 EN pin 1 接 +5V，LX pin 3 经 L1 3015 4.7uH 输出 +3.3V，FB pin 5 由 R1 68KΩ 与 R2 15KΩ 分压，GND pin 2 接地。

- 参数与网络：`input=+5V at IN pin 4`；`enable=EN pin 1 to +5V`；`switch=LX pin 3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ,R2 15KΩ`；`ground=pin 2 GND`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1-B2：U1、L1、R1/R2 与 +5V/+3.3V/GND

### U1 输入/输出去耦

+5V 输入配置 C3 22uF 和 C4 100nF 到 GND；+3.3V 输出配置 C1 100nF 和 C2 22uF 到 GND。

- 参数与网络：`input_caps=C3 22uF,C4 100nF`；`output_caps=C1 100nF,C2 22uF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1-B2：U1 左右两侧 C1-C4

### SCL/SDA 上拉

R3 和 R4 均为 15KΩ，分别将 SCL 与 SDA 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R3 15KΩ`；`sda_pullup=R4 15KΩ`；`rail=+3.3V`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 C1-C2：+3.3V-R3-SCL 与 +3.3V-R4-SDA

### SCD40 +3.3V 供电

U2 VDD pin 7 和 VDDH pin 19 共接 +3.3V，GND pin 6 接地；C5/C6 均为 100nF，跨接 +3.3V 与 GND。

- 参数与网络：`supply_pins=VDD pin 7,VDDH pin 19`；`rail=+3.3V`；`ground_pin=pin 6`；`decoupling=C5 100nF,C6 100nF`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-C2：U2 VDD/VDDH/GND 与 C5/C6

## 接口

### J1 HY-2.0_IIC

J1 pin 1 标 IIC_SCL 并接 SCL，pin 2 标 IIC_SDA 并接 SDA，pin 3 标 VCC 并经 F1 接 +5V，pin 4 标 GND 并接地。

- 参数与网络：`pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC,+5V via F1`；`pin_4=GND`；`connector=HY-2.0_IIC`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B4-C4：J1 pins 1~4 与 SCL/SDA/F1/+5V/GND

## 总线

### SCD40 I2C

J1 pin 1 的 SCL 直接连接 U2 SCL pin 9，J1 pin 2 的 SDA 直接连接 U2 SDA pin 10；两条线均上拉到 +3.3V。

- 参数与网络：`device=U2 SCD40`；`scl=J1 pin 1 to U2 pin 9`；`sda=J1 pin 2 to U2 pin 10`；`pullup_rail=+3.3V`；`controller=external I2C host`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-C4：J1 与 U2 之间 SCL/SDA 同名网络

## 时钟

### 外部时钟

本页没有绘出晶振、振荡器或外部时钟网络，U2 对外仅显示电源、SCL、SDA 和 GND 引脚。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`clock_net=null`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 整页无晶振/振荡器位号；U2 符号无时钟引脚

## 保护电路

### D1/D2 I2C 保护

D1 RLSD52A031V 跨接 SCL 与 GND，D2 RLSD52A031V 跨接 SDA 与 GND，位置靠近 J1 接口。

- 参数与网络：`scl_protection=D1 RLSD52A031V to GND`；`sda_protection=D2 RLSD52A031V to GND`；`connector=J1`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-B4：D1/D2 上端 GND、下端分别接 SCL/SDA

### +5V 输入保护

J1 pin 3 VCC 与板内 +5V 之间串接 F1 6V@1A，D4 LESD3Z5.0CMT1G 从该 VCC/+5V 节点接至 GND。

- 参数与网络：`series_device=F1 6V@1A`；`shunt_device=D4 LESD3Z5.0CMT1G`；`connector_pin=J1 pin 3`；`rail=+5V`；`return=GND`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B3-C4：+5V-F1-J1 pin 3 路径及 D4 对地支路

### +3.3V 轨保护

D3 RLSD52A031V 跨接 U1 输出的 +3.3V 电源轨与 GND。

- 参数与网络：`device=D3 RLSD52A031V`；`rail=+3.3V`；`return=GND`；`location=buck output`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 B1：+3.3V-D3-GND 竖直支路

## 关键网络

### Unit CO2 关键网络索引

关键路径为 J1 pin 3→F1→+5V→U1→L1→+3.3V→U2 VDD/VDDH，以及 J1 pin 1 SCL→U2 pin 9、J1 pin 2 SDA→U2 pin 10。

- 参数与网络：`power_path=J1.3-F1-+5V-U1-L1-+3.3V-U2.7/U2.19`；`scl_path=J1.1-D1/R3-U2.9`；`sda_path=J1.2-D2/R4-U2.10`；`ground=J1.4,U1.2,U2.6`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 整页 +5V/+3.3V/SCL/SDA/GND 同名网络与直接连线

## 传感器

### U2 SCD40

U2 VDD pin 7 与 VDDH pin 19 接 +3.3V，SCL pin 9 接 SCL，SDA pin 10 接 SDA，GND pin 6 接地。

- 参数与网络：`vdd=pin 7 to +3.3V`；`vddh=pin 19 to +3.3V`；`scl=pin 9 SCL`；`sda=pin 10 SDA`；`ground=pin 6 GND`
- 证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 网格 C2：U2 SCD40 的 7/19/9/10/6 脚号、名称和网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CO2 | `sensor=U2 SCD40`；`communication=J1 SCL/SDA`；`power=+5V->U1 SY8089AAAC->+3.3V`；`signal_protection=D1,D2`；`power_protection=F1,D3,D4` |
| 传感器 | U2 SCD40 | `vdd=pin 7 to +3.3V`；`vddh=pin 19 to +3.3V`；`scl=pin 9 SCL`；`sda=pin 10 SDA`；`ground=pin 6 GND` |
| 电源 | U1 SY8089AAAC | `input=+5V at IN pin 4`；`enable=EN pin 1 to +5V`；`switch=LX pin 3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ,R2 15KΩ`；`ground=pin 2 GND` |
| 电源 | U1 输入/输出去耦 | `input_caps=C3 22uF,C4 100nF`；`output_caps=C1 100nF,C2 22uF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 接口 | J1 HY-2.0_IIC | `pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC,+5V via F1`；`pin_4=GND`；`connector=HY-2.0_IIC` |
| 总线 | SCD40 I2C | `device=U2 SCD40`；`scl=J1 pin 1 to U2 pin 9`；`sda=J1 pin 2 to U2 pin 10`；`pullup_rail=+3.3V`；`controller=external I2C host` |
| 电源 | SCL/SDA 上拉 | `scl_pullup=R3 15KΩ`；`sda_pullup=R4 15KΩ`；`rail=+3.3V` |
| 总线地址 | Unit CO2 I2C 地址 | `device=U2 SCD40`；`schematic_address=null`；`address_selection=null`；`address_source_needed=SCD40 datasheet or protocol documentation` |
| 电源 | SCD40 +3.3V 供电 | `supply_pins=VDD pin 7,VDDH pin 19`；`rail=+3.3V`；`ground_pin=pin 6`；`decoupling=C5 100nF,C6 100nF` |
| 保护电路 | D1/D2 I2C 保护 | `scl_protection=D1 RLSD52A031V to GND`；`sda_protection=D2 RLSD52A031V to GND`；`connector=J1` |
| 保护电路 | +5V 输入保护 | `series_device=F1 6V@1A`；`shunt_device=D4 LESD3Z5.0CMT1G`；`connector_pin=J1 pin 3`；`rail=+5V`；`return=GND` |
| 保护电路 | +3.3V 轨保护 | `device=D3 RLSD52A031V`；`rail=+3.3V`；`return=GND`；`location=buck output` |
| 传感器 | SCD40 测量范围与精度 | `sensor=SCD40`；`schematic_co2_range=null`；`schematic_co2_accuracy=null`；`schematic_temperature_range=null`；`schematic_humidity_range=null`；`specification_source_needed=sensor datasheet and product test conditions` |
| 时钟 | 外部时钟 | `external_crystal=null`；`external_oscillator=null`；`clock_net=null` |
| 关键网络 | Unit CO2 关键网络索引 | `power_path=J1.3-F1-+5V-U1-L1-+3.3V-U2.7/U2.19`；`scl_path=J1.1-D1/R3-U2.9`；`sda_path=J1.2-D2/R4-U2.10`；`ground=J1.4,U1.2,U2.6` |

## 待确认事项

- `address.i2c-not-shown`：原理图显示 SCD40 的 SCL/SDA 连接，但页面未打印 I2C 地址或地址选择网络，无法仅凭该页确认地址值。（证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 U2/J1 SCL/SDA 区域，整页无 0x 地址或 ADDR 引脚）
- `sensor.measurement-specs-not-shown`：原理图可确认传感器型号和 I2C/电源连接，但没有打印 CO2、温度或湿度的测量范围、精度、采样周期或校准条件。（证据：图 77ba68e0dbf5 / 第 1 页 / 页 1 U2 SCD40 符号仅含型号、I2C 和电源引脚，无量程/精度文字）
- `review.i2c-address`：Unit CO2 所用 SCD40 的 I2C 地址是否为 0x62？；原因：原理图只显示 SCL/SDA，未打印地址值或地址选择方式，需要 SCD40 数据手册或通信协议确认。
- `review.measurement-specs`：当前产品的 CO2、温度、湿度量程、精度和适用校准条件分别是什么？；原因：这些参数未印在原理图，且整机规格还受外壳、气流、固件和校准条件影响。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `77ba68e0dbf5ce0b00f129eaf071af3ad6a9d165a94c0e85504f2a76caae2ecd` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/590/SCH_UNIT_CO2_sch_01.png` |

---

源文档：`zh_CN/unit/co2.md`

源文档 SHA-256：`1f75a557c31e76d3ab0575f305213c6e88570eb81a8f9c40f009ea68ce0b27aa`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
