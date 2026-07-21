# Unit Glass2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Glass2 |
| SKU | U158-B |
| 产品 ID | `unit-glass2-f68c9376b2f6` |
| 源文档 | `zh_CN/unit/Glass2 Unit.md` |

## 概述

Unit Glass2 以 J3 AFC05-S24FIA-00/SSD1309 OLED 模组为显示核心，J1、J2 两个 HY-2.0_IIC 接口并联到 SCL、SDA、+5V 和 GND。U2 ME6210A33M3G 将 +5V 转为 +3.3V 供显示逻辑，U1 TPS61040DBVR 配合 L1、D1 与反馈网络将 +5V 升至 +12.5V 供 OLED VCC。Jumper1 与 R7 设置 SA0，原理图明确给出 SA0=0 时地址 0x3C、SA0=1 时地址 0x3D。

## 检索关键词

`Unit Glass2`、`U158-B`、`SSD1309`、`AFC05-S24FIA-00`、`TPS61040DBVR`、`ME6210A33M3G`、`I2C`、`0x3C`、`0x3D`、`SA0`、`Jumper1`、`SCL`、`SDA`、`HY-2.0_IIC`、`J1`、`J2`、`J3`、`+5V`、`+3.3V`、`+12.5V`、`L1 10uH 2520`、`1N4148WS T4`、`RES`、`D0`、`D1`、`D2`、`IREF`、`VCOMH`、`VLED`、`R5 910K`、`R6 4.7K`、`R7 4.7K`、`128x64`、`transparent OLED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J3 | AFC05-S24FIA-00 / SSD1309 | 24 针透明 OLED 显示模组与 SSD1309 控制器 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 A3-B3，J3 24 针器件下方标注 AFC05-S24FIA-00 和 SSD1309 |
| U1 | TPS61040DBVR | +5V 至 +12.5V OLED 升压控制器 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 A1，U1 下方标注 TPS61040DBVR，外围连接 L1、D1 和反馈分压 |
| U2 | ME6210A33M3G | +5V 至 +3.3V 显示逻辑电源 LDO | 图 6009f3092c08 / 第 1 页 / 页 1 网格 B1，U2 下方标注 ME6210A33M3G，Vin/Vout 接 +5V/+3.3V |
| J1 | HY-2.0_IIC | 第一组四针 I2C 与 +5V 接口 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 C2，J1 标注 HY-2.0_IIC，针脚为 IIC_SCL、IIC_SDA、VCC、GND |
| J2 | HY-2.0_IIC | 第二组四针 I2C 与 +5V 菊花链接口 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 C2-C3，J2 标注 HY-2.0_IIC，针脚为 IIC_SCL、IIC_SDA、VCC、GND |
| Jumper1 | SA0 solder jumper | SSD1309 I2C 地址位 SA0 选择焊盘 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 A2，Jumper1 位于 +3.3V 与 SA0 之间，旁注 SA0=0 0x3C、SA0=1 0x3D |
| L1 | 10uH 2520 | TPS61040 升压储能电感 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 A1，L1 标注 10uH 2520，连接 +5V 与 U1 SW/D1 开关节点 |
| D1 | 1N4148WS T4 | 升压电路整流二极管 | 图 6009f3092c08 / 第 1 页 / 页 1 网格 A1，D1 标注 1N4148WS T4，位于 SW 节点与 +12.5V 之间 |

## 系统结构

### J3 OLED 显示模组

J3 标注 AFC05-S24FIA-00 和 SSD1309，是本电路的 24 针 OLED 显示模组。

- 参数与网络：`reference=J3`；`module=AFC05-S24FIA-00`；`controller=SSD1309`；`pins=24`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A3-B3，J3 针脚列表及 AFC05-S24FIA-00/SSD1309 标注

## 电源

### U2 逻辑电源

U2 ME6210A33M3G 的 Vin 引脚 3 接 +5V，Vout 引脚 2 输出 +3.3V，GND 引脚 1 接地。

- 参数与网络：`reference=U2`；`part_number=ME6210A33M3G`；`input=Vin/pin 3/+5V`；`output=Vout/pin 2/+3.3V`；`ground=GND/pin 1`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 B1，U2 引脚号及 +5V/+3.3V/GND 网络

### U2 输入输出去耦

C6、C7 均为 4.7 uF，分别连接在 U2 的 +5V 输入、+3.3V 输出与 GND 之间。

- 参数与网络：`input_capacitor=C6 4.7uF`；`output_capacitor=C7 4.7uF`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 B1，U2 两侧 C6/C7 与电源网络

### U1 OLED 升压电源

U1 TPS61040DBVR 的 Vin 引脚 5 与 EN 引脚 4 接 +5V，SW 引脚 1 连接 L1/D1 开关节点，FB 引脚 3 接反馈分压，GND 引脚 2 接地，输出网络标为 +12.5V。

- 参数与网络：`reference=U1`；`part_number=TPS61040DBVR`；`input_enable=Vin/pin 5 and EN/pin 4 to +5V`；`switch_pin=SW/pin 1`；`feedback_pin=FB/pin 3`；`output_rail=+12.5V`；`ground=GND/pin 2`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A1，U1 全部引脚、L1/D1 与 +5V/+12.5V 网络

### U1 升压外围

L1 为 10 uH 2520，D1 为 1N4148WS T4；R1 1.1 MΩ 与 R2 120 kΩ 构成 +12.5V 至 GND 的反馈分压，C1 22 pF 跨接输出与 FB，C5 22 uF 为输入电容，C4 1 uF 为输出电容。

- 参数与网络：`inductor=L1 10uH 2520`；`diode=D1 1N4148WS T4`；`upper_feedback=R1 1.1M`；`lower_feedback=R2 120k`；`feedforward_capacitor=C1 22pF`；`input_capacitor=C5 22uF`；`output_capacitor=C4 1uF`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A1，TPS61040 周围 L1、D1、R1/R2、C1/C4/C5

### J3 VDD

J3 的 VDD 引脚 5 连接 +3.3V，C2 4.7 uF 与 C3 100 nF 并联在该电源与 GND 之间。

- 参数与网络：`supply_pin=J3 VDD/pin 5`；`rail=+3.3V`；`capacitors=C2 4.7uF,C3 100nF`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A3，J3 VDD 引脚 5、+3.3V 与 C2/C3

### J3 VCC

J3 的 VCC 引脚 23 连接 +12.5V，C9 10 uF 与 C10 100 nF 并联在该电源与 GND 之间。

- 参数与网络：`supply_pin=J3 VCC/pin 23`；`rail=+12.5V`；`capacitors=C9 10uF,C10 100nF`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 B3，J3 VCC 引脚 23、+12.5V 与 C9/C10

## 接口

### J1 I2C 接口

J1 的 1 至 4 脚依次连接 SCL、SDA、+5V 和 GND，内部针脚名为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 C2，J1 脚号、内外网络名与 +5V/GND

### J2 I2C 接口

J2 的 1 至 4 脚依次连接 SCL、SDA、+5V 和 GND，内部针脚名为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J2`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 C2-C3，J2 脚号、内外网络名与 +5V/GND

## 总线

### J1 与 J2 并联 I2C 总线

J1 与 J2 的 1、2、3、4 脚分别共用 SCL、SDA、+5V、GND，因此两个接口在电气上并联。

- 参数与网络：`connectors=J1,J2`；`shared_nets=SCL,SDA,+5V,GND`；`topology=parallel/daisy-chain`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 C2-C3，J1/J2 对应针脚之间的连续 SCL、SDA 与电源网络

### I2C 上拉

R3、R4 均为 4.7 kΩ，分别将 SCL、SDA 上拉至 +3.3V。

- 参数与网络：`scl_pullup=R3 4.7k to +3.3V`；`sda_pullup=R4 4.7k to +3.3V`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 C2，J2 左侧 R3/R4 与 SCL/SDA、+3.3V 网络

### SSD1309 I2C 数据连接

SCL 连接 J3 的 D0 引脚 13；SDA 连接 J3 的 D1 引脚 14，并在连接器处与 D2 引脚 15相连。

- 参数与网络：`scl=J3 D0/pin 13`；`sda=J3 D1/pin 14 and D2/pin 15`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A3，J3 D0/D1/D2 引脚 13-15 与 SCL/SDA 连线

## 总线地址

### SSD1309 I2C 地址选择

原理图旁注明 SA0=0 时 I2C 地址为 0x3C，SA0=1 时为 0x3D；SA0 连接 J3 的 DC 引脚 10。

- 参数与网络：`address_sa0_low=0x3C`；`address_sa0_high=0x3D`；`address_pin=J3 DC/pin 10`；`network=SA0`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A2-A3，I2C ADD 文字、SA0 网络及 J3 DC 引脚 10

### Jumper1 与 R7

R7 4.7 kΩ 将 SA0 下拉至 GND；Jumper1 闭合时把 SA0 连接至 +3.3V，构成地址位选择。

- 参数与网络：`pulldown=R7 4.7k to GND`；`jumper=Jumper1 between +3.3V and SA0`；`open_state=SA0=0/0x3C`；`closed_state=SA0=1/0x3D`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A2，Jumper1 两端 +3.3V/SA0 与 R7 4.7K 下拉

## GPIO 与控制信号

### J3 接口模式配置

J3 的 VLSS、VSS、BS1、BS2 和 CS 引脚在本页连接 GND；D0/D1/D2 用于 SCL/SDA，构成图示串行接口配置。

- 参数与网络：`grounded_config_pins=VLSS/pin 2,VSS/pin 3,BS1/pin 6,BS2/pin 7,CS/pin 8`；`serial_pins=D0/pin 13 SCL,D1/pin 14 SDA,D2/pin 15 SDA`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A3，J3 上半部配置引脚接地与 D0-D2 串行网络

## 复位

### J3 RES

J3 的 RES 引脚 9 连接 RES 网络；R6 4.7 kΩ 将 RES 上拉至 +3.3V，C11 4.7 uF 将其连接至 GND。

- 参数与网络：`reset_pin=J3 RES/pin 9`；`pullup=R6 4.7k to +3.3V`；`capacitor=C11 4.7uF to GND`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 A3-B2，J3 RES 引脚 9 与 R6/C11 复位网络

## 模拟电路

### J3 IREF 与 VCOMH

J3 的 IREF 引脚 21 通过 R5 910 kΩ 连接 GND；VCOMH 引脚 22 通过 C8 4.7 uF 连接 GND。

- 参数与网络：`iref=J3 pin 21,R5 910k to GND`；`vcomh=J3 pin 22,C8 4.7uF to GND`
- 证据：图 6009f3092c08 / 第 1 页 / 页 1 网格 B3，J3 IREF/VCOMH 引脚 21/22 与 R5/C8

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | J3 OLED 显示模组 | `reference=J3`；`module=AFC05-S24FIA-00`；`controller=SSD1309`；`pins=24` |
| 接口 | J1 I2C 接口 | `reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional` |
| 接口 | J2 I2C 接口 | `reference=J2`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | J1 与 J2 并联 I2C 总线 | `connectors=J1,J2`；`shared_nets=SCL,SDA,+5V,GND`；`topology=parallel/daisy-chain` |
| 总线 | I2C 上拉 | `scl_pullup=R3 4.7k to +3.3V`；`sda_pullup=R4 4.7k to +3.3V` |
| 总线 | SSD1309 I2C 数据连接 | `scl=J3 D0/pin 13`；`sda=J3 D1/pin 14 and D2/pin 15` |
| 总线地址 | SSD1309 I2C 地址选择 | `address_sa0_low=0x3C`；`address_sa0_high=0x3D`；`address_pin=J3 DC/pin 10`；`network=SA0` |
| 总线地址 | Jumper1 与 R7 | `pulldown=R7 4.7k to GND`；`jumper=Jumper1 between +3.3V and SA0`；`open_state=SA0=0/0x3C`；`closed_state=SA0=1/0x3D` |
| 电源 | U2 逻辑电源 | `reference=U2`；`part_number=ME6210A33M3G`；`input=Vin/pin 3/+5V`；`output=Vout/pin 2/+3.3V`；`ground=GND/pin 1` |
| 电源 | U2 输入输出去耦 | `input_capacitor=C6 4.7uF`；`output_capacitor=C7 4.7uF` |
| 电源 | U1 OLED 升压电源 | `reference=U1`；`part_number=TPS61040DBVR`；`input_enable=Vin/pin 5 and EN/pin 4 to +5V`；`switch_pin=SW/pin 1`；`feedback_pin=FB/pin 3`；`output_rail=+12.5V`；`ground=GND/pin 2` |
| 电源 | U1 升压外围 | `inductor=L1 10uH 2520`；`diode=D1 1N4148WS T4`；`upper_feedback=R1 1.1M`；`lower_feedback=R2 120k`；`feedforward_capacitor=C1 22pF`；`input_capacitor=C5 22uF`；`output_capacitor=C4 1uF` |
| 电源 | J3 VDD | `supply_pin=J3 VDD/pin 5`；`rail=+3.3V`；`capacitors=C2 4.7uF,C3 100nF` |
| 电源 | J3 VCC | `supply_pin=J3 VCC/pin 23`；`rail=+12.5V`；`capacitors=C9 10uF,C10 100nF` |
| 复位 | J3 RES | `reset_pin=J3 RES/pin 9`；`pullup=R6 4.7k to +3.3V`；`capacitor=C11 4.7uF to GND` |
| 模拟电路 | J3 IREF 与 VCOMH | `iref=J3 pin 21,R5 910k to GND`；`vcomh=J3 pin 22,C8 4.7uF to GND` |
| GPIO 与控制信号 | J3 接口模式配置 | `grounded_config_pins=VLSS/pin 2,VSS/pin 3,BS1/pin 6,BS2/pin 7,CS/pin 8`；`serial_pins=D0/pin 13 SCL,D1/pin 14 SDA,D2/pin 15 SDA` |
| 其他事实 | OLED 面板参数 | `documented_size_inch=1.51`；`documented_resolution=128x64`；`documented_color=blue`；`documented_color_depth_bits=1`；`schematic_panel_parameters=null` |

## 待确认事项

- `other.display_parameters`：产品正文描述 1.51 英寸透明蓝色 OLED、128×64 像素和 1 位颜色深度，但这些面板参数未在本页原理图中标注。（证据：图 6009f3092c08 / 第 1 页 / 页 1 J3 仅标注 AFC05-S24FIA-00/SSD1309 与针脚，未标注尺寸、分辨率、颜色或透明属性）
- `review.display_parameters`：AFC05-S24FIA-00 面板在该产品版本中的尺寸、分辨率、颜色和透明属性是否与正文参数一致？；原因：原理图只提供模组型号和电气连接，未打印面板光学与几何参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6009f3092c087806c48be87e810ad5e6a7549d631b5d23946c430dac5ddb71ae` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/613/SCH_UNIT_GLASS2_sch_01.png` |

---

源文档：`zh_CN/unit/Glass2 Unit.md`

源文档 SHA-256：`8733c8d78408358430071319db41e89ee832757f2480a158b8e189348d34f3e3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
