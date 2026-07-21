# Unit Grove to Grove 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Grove to Grove |
| SKU | U148 |
| 产品 ID | `unit-grove-to-grove-011b18ade30e` |
| 源文档 | `zh_CN/unit/unit_grove2grove.md` |

## 概述

Unit Grove to Grove 使用 SGM2553D（U3）控制 `5V_VIN` 到 `5V_OUT` 的电源通断，并以 20mΩ 分流电阻 R3 和 INA199A1DCKR（U2）生成模拟 `Imeasure` 电流测量输出。J1/J2 的 IO2、IO1 直接贯通，J3 提供 Imeasure、EN、VCC_5V 与 GND；VCC_5V 还经 R1 0R 接到 5V_VIN。HT7533（U1）从 VCC_5V 生成 3V3，TL432（U4）与 R2 为 U2 REF 提供偏置参考。图面明确标注 R5 36K 对应 Imax=1A，但未给出 Imeasure 电压与负载电流的完整换算关系。

## 检索关键词

`Unit Grove to Grove`、`U148`、`SGM2553D`、`INA199A1DCKR`、`HT7533`、`TL432`、`GROVE 4P`、`J1`、`J2`、`J3`、`5V_VIN`、`5V_OUT`、`VCC_5V`、`3V3`、`EN`、`Imeasure`、`IO1`、`IO2`、`R1 0R`、`R2 330`、`R3 20mR/1206`、`R5 36K`、`R6 100K`、`Imax=1A`、`current sense`、`load switch`、`current limit`、`FAULT#`、`ILIM`、`INA199`、`analog output`、`5V 1A`、`0-1000mA`、`C1 1uF/50V`、`C2 1uF/50V`、`C3 0.1uF/50V`、`C4 0.1uF/50V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | SGM2553D | 由 EN 控制 5V 电源通断并通过 ILIM 实现 1A 限流的负载开关 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B2-B3，U3 SGM2553D pins 1~7、5V_VIN/EN/R5 36K/Imax=1A/FAULT# 网络 |
| U2 | INA199A1DCKR | 跨 R3 20mΩ 分流电阻测量负载电流并输出 Imeasure | 图 fb059620c11b / 第 1 页 / 页 1 网格 B1-B2，U2 INA199A1DCKR pins 1~6 与 REF/GND/V+/IN+/IN-/OUT/Imeasure |
| U1 | HT7533 | 将 VCC_5V 稳压为 3V3，为电流检测与参考电路供电 | 图 fb059620c11b / 第 1 页 / 页 1 网格 A2，U1 HT7533：VIN pin 3 接 VCC_5V、VOUT pin 2 接 3V3、GND pin 1 接地 |
| U4 | TL432 | 与 R2 组成 U2 REF 偏置参考支路 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B1，U4 TL432、R2 330、3V3、GND 与 U2 REF pin 1 共节点 |
| J1 | GROVE 4P | IO2、IO1、5V_VIN 与 GND 侧的 Grove 接口 | 图 fb059620c11b / 第 1 页 / 页 1 网格 A1，J1 GROVE 4P 从上到下标 IO2、IO1、5V、GND；5V 线标 5V_VIN |
| J2 | GROVE 4P | 与 J1 IO2/IO1 直通并提供 5V_OUT/GND 的 Grove 接口 | 图 fb059620c11b / 第 1 页 / 页 1 网格 A1-A2，J2 GROVE 4P 从上到下标 IO2、IO1、5V、GND；5V 线标 5V_OUT |
| J3 | GROVE 4P | 控制与测量接口，提供 Imeasure、EN、VCC_5V 与 GND | 图 fb059620c11b / 第 1 页 / 页 1 网格 A2，J3 GROVE 4P 从上到下为 IO2/Imeasure、IO1/EN、5V/VCC_5V、GND |
| R1 | 0R | 连接 VCC_5V 与 5V_VIN 的零欧电阻 | 图 fb059620c11b / 第 1 页 / 页 1 网格 A2，VCC_5V-R1 0R-5V_VIN |
| R3 | 20mR/1206 | 位于 U3 OUT 与 5V_OUT 之间的电流分流电阻 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B2，R3 20mR/1206 连接 U3 OUT/U2 IN+ 与 5V_OUT/U2 IN- |
| R5 | 36K | U3 ILIM pin 2 的对地限流设定电阻，图面标注 Imax=1A | 图 fb059620c11b / 第 1 页 / 页 1 网格 B2，U3 ILIM pin 2-R5 36K-GND 与 Imax=1A 标注 |
| R6 | 100K | U3 EN 到 GND 的下拉电阻 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B2-B3，U3 EN pin 4/EN 网络经 R6 100K 接 GND |
| R2 | 330 | 从 3V3 向 TL432/U2 REF 节点供电的电阻 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B1，3V3-R2 330-U4/U2 REF 节点 |
| C1 | 1uF/50V | HT7533 3V3 输出去耦电容 | 图 fb059620c11b / 第 1 页 / 页 1 网格 A2，U1 VOUT/3V3-C1 1uF/50V-GND |
| C2/C4 | 1uF/50V / 0.1uF/50V | U3 输出与 5V_VIN 输入侧对地滤波电容 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B2-B3，C2 1uF/50V 从 U3 OUT 接 GND，C4 0.1uF/50V 从 5V_VIN 接 GND |
| C3 | 0.1uF/50V | U2 3V3 供电去耦电容 | 图 fb059620c11b / 第 1 页 / 页 1 网格 B1，U2 V+ pin 3/3V3-C3 0.1uF/50V-GND |

## 系统结构

### Unit Grove to Grove

J1/J2 的 IO2 和 IO1 直接贯通，5V 路径由 U3 SGM2553D 控制并经 R3 20mΩ 输出为 5V_OUT；U2 INA199A1DCKR 将分流压差转换为 J3 的 Imeasure。

- 参数与网络：`input_side=J1 IO2,IO1,5V_VIN,GND`；`output_side=J2 IO2,IO1,5V_OUT,GND`；`control_measure=J3 Imeasure,EN,VCC_5V,GND`；`load_switch=U3 SGM2553D`；`current_sense=R3 20mR+U2 INA199A1DCKR`；`logic_supply=U1 HT7533 3V3`
- 证据：图 fb059620c11b / 第 1 页 / 整页：J1/J2/J3/U1/U2/U3/U4 与 IO1/IO2/5V_VIN/5V_OUT/EN/Imeasure/VCC_5V/3V3 网络

## 电源

### VCC_5V 与 5V_VIN

J3 的 VCC_5V 经 R1 0R 连接 5V_VIN；5V_VIN 同时连接 J1 5V、U3 IN pin 6 和 C4 0.1uF/50V。

- 参数与网络：`control_supply=J3 VCC_5V`；`link=R1 0R`；`input_rail=5V_VIN`；`consumers=J1 5V,U3 IN pin 6,C4 0.1uF/50V`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A1-B3，VCC_5V-R1-5V_VIN 与 J1/U3/C4 同名网络

### U3 5V 通断路径

5V_VIN 进入 U3 IN pin 6，U3 OUT pin 1 经 R3 20mR/1206 连接 5V_OUT，再到 J2 5V；U3 EP pin 7 与 GND pin 5 接地。

- 参数与网络：`input=5V_VIN,U3 pin 6`；`switch_output=U3 OUT pin 1`；`shunt=R3 20mR/1206`；`output=5V_OUT,J2 5V`；`grounds=U3 pins 5,7`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A1-B3，J1/5V_VIN/U3 OUT-IN/R3/5V_OUT/J2 完整路径

### U1 HT7533

U1 VIN pin 3 接 VCC_5V，VOUT pin 2 输出 3V3，GND pin 1 接地；C1 1uF/50V 跨接 3V3 与 GND。

- 参数与网络：`input=VIN pin 3,VCC_5V`；`output=VOUT pin 2,3V3`；`ground=pin 1,GND`；`output_capacitor=C1 1uF/50V`；`enable=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A2，U1 HT7533/VCC_5V/3V3/C1/GND

### U3 输入输出滤波

C4 0.1uF/50V 从 5V_VIN 接 GND；C2 1uF/50V 从 U3 OUT/R3 上游节点接 GND。

- 参数与网络：`input_capacitor=C4 0.1uF/50V on 5V_VIN`；`output_capacitor=C2 1uF/50V on U3 OUT`；`ground=GND`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 B2-B3，C2/C4 与 U3 OUT/5V_VIN/GND

## 接口

### J1 GROVE 4P

J1 从上到下标为 IO2、IO1、5V、GND；IO2/IO1 分别直连 J2 同名位置，5V 线属于 5V_VIN，GND 接地。图面未打印数字针脚号或 IO 方向。

- 参数与网络：`position_1_top=IO2->J2 IO2`；`position_2=IO1->J2 IO1`；`position_3=5V,5V_VIN`；`position_4_bottom=GND`；`pin_numbers=not shown`；`io_direction=not shown`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A1，J1 四条引线与 J2/5V_VIN/GND 连线

### J2 GROVE 4P

J2 从上到下标为 IO2、IO1、5V、GND；IO2/IO1 分别直连 J1，5V 线属于 5V_OUT，GND 接地。图面未打印数字针脚号或 IO 方向。

- 参数与网络：`position_1_top=IO2->J1 IO2`；`position_2=IO1->J1 IO1`；`position_3=5V,5V_OUT`；`position_4_bottom=GND`；`pin_numbers=not shown`；`io_direction=not shown`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A1-A2，J2 四条引线与 J1/5V_OUT/GND 连线

### J3 GROVE 4P

J3 从上到下为 IO2/Imeasure、IO1/EN、5V/VCC_5V、GND；Imeasure 由 U2 OUT pin 6 驱动，EN 连接 U3 EN pin 4，VCC_5V 经 R1 0R 接 5V_VIN。

- 参数与网络：`position_1_top=IO2,Imeasure,U2 OUT pin 6,analog output`；`position_2=IO1,EN,U3 pin 4,control input`；`position_3=5V,VCC_5V,R1->5V_VIN`；`position_4_bottom=GND`；`pin_numbers=not shown`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A2，J3 Imeasure/EN/VCC_5V/GND 与 U2/U3/R1 同名网络

### J1/J2 IO1/IO2

J1 IO2 与 J2 IO2 通过一条导线直连，J1 IO1 与 J2 IO1 通过另一条导线直连；两路不经过 U2/U3，也未绘出串联、上拉或保护器件。

- 参数与网络：`io2=J1 IO2<->J2 IO2 direct`；`io1=J1 IO1<->J2 IO1 direct`；`series_components=null`；`pullups=null`；`protection=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A1-A2，J1/J2 顶部两条水平 IO2/IO1 直通线

## 总线

### 数字通信总线

本页未绘出 I2C、SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S；J1/J2 IO1/IO2 是无协议标注的直通信号。

- 参数与网络：`pass_through=IO1,IO2`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页网络仅 IO1/IO2/EN/Imeasure 与电源，无串行总线名称

## 总线地址

### 总线地址

本页没有可寻址数字总线器件，也未打印任何 I2C/SPI 设备地址或地址选择网络。

- 参数与网络：`addressed_device=null`；`i2c_address=null`；`address_selector=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页器件与网络，无 SCL/SDA/ADDR/CS 或 0x 地址文字

## GPIO 与控制信号

### EN 通断控制

J3 IO1/EN 直接连接 U3 EN pin 4，并由 R6 100K 下拉到 GND；图面未绘出反相或电平转换器件。

- 参数与网络：`connector=J3 IO1`；`net=EN`；`device_pin=U3 pin 4`；`pulldown=R6 100K to GND`；`inverter=null`；`level_shifter=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 A2-B3，J3 EN-U3 pin 4-R6 100K-GND

## 时钟

### 时钟、复位与调试

本页未绘出晶振、振荡器、复位网络、BOOT 配置、测试点或调试连接器。

- 参数与网络：`crystal=null`；`oscillator=null`；`reset=null`；`boot=null`；`test_point=null`；`debug_connector=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页，仅模拟测流、负载开关、稳压与三只 Grove 连接器

## 保护电路

### U3 ILIM 与 1A 限流

U3 ILIM pin 2 经 R5 36K 接 GND，旁边明确标注 Imax=1A；FAULT# pin 3 在页面未连接。

- 参数与网络：`ilim_pin=U3 pin 2`；`ilim_resistor=R5 36K to GND`；`schematic_limit=Imax=1A`；`fault_pin=U3 pin 3 FAULT# no-connect`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 B2，U3 ILIM/FAULT# pins 2/3、R5 36K 与 Imax=1A 标注

### Grove 接口附加保护

除 U3 的限流/负载开关功能外，本页未绘出 J1/J2/J3 的 TVS、ESD 阵列、保险丝或反接保护器件。

- 参数与网络：`load_switch_current_limit=U3 SGM2553D`；`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页 J1/J2/J3 与电源路径，未见 TVS/ESD/FUSE/反接器件

## 关键网络

### Unit Grove to Grove 关键网络索引

关键路径为 J3 VCC_5V→R1→5V_VIN→U3 IN/OUT→R3→5V_OUT→J2，J3 EN→U3 EN，R3 两端→U2 IN+/IN-→Imeasure→J3；J1/J2 IO1 与 IO2 分别直通。

- 参数与网络：`power=J3 VCC_5V-R1-5V_VIN-U3-R3-5V_OUT-J2`；`enable=J3 EN-U3.4`；`measurement=R3-U2.4/U2.5-U2.6 Imeasure-J3`；`io1=J1-J2 direct`；`io2=J1-J2 direct`；`reference=3V3-R2-U4-U2 REF`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页全部 VCC_5V/5V_VIN/5V_OUT/EN/Imeasure/IO1/IO2/3V3 同名网络

## 存储

### 存储与存储器

本页未绘出 Flash、EEPROM、RAM、存储卡或其他存储器件/接口。

- 参数与网络：`flash=null`；`eeprom=null`；`ram=null`；`storage_card=null`；`storage_interface=null`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页器件清单中无存储器或存储连接器

## 模拟电路

### R3/U2 电流检测

U2 IN+ pin 4 接 R3 上游的 U3 OUT 节点，IN- pin 5 接 R3 下游的 5V_OUT；R3 为 20mR/1206，U2 OUT pin 6 输出 Imeasure。

- 参数与网络：`shunt=R3 20mR/1206`；`in_plus=U2 pin 4,U3 OUT side`；`in_minus=U2 pin 5,5V_OUT side`；`output=U2 pin 6,Imeasure`；`connector=J3 IO2`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 B1-B2，U2 IN+/IN-/OUT 与 R3/U3 OUT/5V_OUT/Imeasure

### U2 REF 偏置

U2 REF pin 1 接 U4 TL432 参考节点，该节点经 R2 330 接 3V3；U2 V+ pin 3 接 3V3，GND pin 2 接地，C3 0.1uF/50V 为供电去耦。

- 参数与网络：`ref_pin=U2 pin 1`；`reference_device=U4 TL432`；`reference_feed=R2 330 to 3V3`；`supply=U2 pin 3,3V3`；`ground=U2 pin 2,GND`；`decoupling=C3 0.1uF/50V`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 网格 B1，U2 REF/V+/GND pins 1/3/2 与 U4/R2/C3/3V3/GND

## 其他事实

### 音频、传感器与射频分区

本页未绘出音频器件、独立环境/运动传感器、射频收发器、天线或射频匹配网络；电流检测由 U2/R3 模拟链路实现。

- 参数与网络：`audio=null`；`sensor_ic=null`；`rf_transceiver=null`；`antenna=null`；`current_measurement=U2 INA199A1DCKR+R3`
- 证据：图 fb059620c11b / 第 1 页 / 页 1 整页功能区，无音频、环境/运动传感或 RF/ANT 器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Grove to Grove | `input_side=J1 IO2,IO1,5V_VIN,GND`；`output_side=J2 IO2,IO1,5V_OUT,GND`；`control_measure=J3 Imeasure,EN,VCC_5V,GND`；`load_switch=U3 SGM2553D`；`current_sense=R3 20mR+U2 INA199A1DCKR`；`logic_supply=U1 HT7533 3V3` |
| 接口 | J1 GROVE 4P | `position_1_top=IO2->J2 IO2`；`position_2=IO1->J2 IO1`；`position_3=5V,5V_VIN`；`position_4_bottom=GND`；`pin_numbers=not shown`；`io_direction=not shown` |
| 接口 | J2 GROVE 4P | `position_1_top=IO2->J1 IO2`；`position_2=IO1->J1 IO1`；`position_3=5V,5V_OUT`；`position_4_bottom=GND`；`pin_numbers=not shown`；`io_direction=not shown` |
| 接口 | J3 GROVE 4P | `position_1_top=IO2,Imeasure,U2 OUT pin 6,analog output`；`position_2=IO1,EN,U3 pin 4,control input`；`position_3=5V,VCC_5V,R1->5V_VIN`；`position_4_bottom=GND`；`pin_numbers=not shown` |
| 接口 | J1/J2 IO1/IO2 | `io2=J1 IO2<->J2 IO2 direct`；`io1=J1 IO1<->J2 IO1 direct`；`series_components=null`；`pullups=null`；`protection=null` |
| 电源 | VCC_5V 与 5V_VIN | `control_supply=J3 VCC_5V`；`link=R1 0R`；`input_rail=5V_VIN`；`consumers=J1 5V,U3 IN pin 6,C4 0.1uF/50V` |
| 电源 | U3 5V 通断路径 | `input=5V_VIN,U3 pin 6`；`switch_output=U3 OUT pin 1`；`shunt=R3 20mR/1206`；`output=5V_OUT,J2 5V`；`grounds=U3 pins 5,7` |
| GPIO 与控制信号 | EN 通断控制 | `connector=J3 IO1`；`net=EN`；`device_pin=U3 pin 4`；`pulldown=R6 100K to GND`；`inverter=null`；`level_shifter=null` |
| 保护电路 | U3 ILIM 与 1A 限流 | `ilim_pin=U3 pin 2`；`ilim_resistor=R5 36K to GND`；`schematic_limit=Imax=1A`；`fault_pin=U3 pin 3 FAULT# no-connect` |
| 模拟电路 | R3/U2 电流检测 | `shunt=R3 20mR/1206`；`in_plus=U2 pin 4,U3 OUT side`；`in_minus=U2 pin 5,5V_OUT side`；`output=U2 pin 6,Imeasure`；`connector=J3 IO2` |
| 模拟电路 | U2 REF 偏置 | `ref_pin=U2 pin 1`；`reference_device=U4 TL432`；`reference_feed=R2 330 to 3V3`；`supply=U2 pin 3,3V3`；`ground=U2 pin 2,GND`；`decoupling=C3 0.1uF/50V` |
| 模拟电路 | Imeasure 换算关系 | `shunt=R3 20mR`；`amplifier=U2 INA199A1DCKR`；`reference=U4 TL432`；`zero_current_voltage=null`；`gain=null`；`full_scale_voltage=null`；`measurement_error=null`；`product_document_range=0 to 1000mA` |
| 电源 | U1 HT7533 | `input=VIN pin 3,VCC_5V`；`output=VOUT pin 2,3V3`；`ground=pin 1,GND`；`output_capacitor=C1 1uF/50V`；`enable=null` |
| 电源 | U3 输入输出滤波 | `input_capacitor=C4 0.1uF/50V on 5V_VIN`；`output_capacitor=C2 1uF/50V on U3 OUT`；`ground=GND` |
| 保护电路 | Grove 接口附加保护 | `load_switch_current_limit=U3 SGM2553D`；`tvs_esd=null`；`fuse=null`；`reverse_polarity=null` |
| 总线 | 数字通信总线 | `pass_through=IO1,IO2`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 总线地址 | 总线地址 | `addressed_device=null`；`i2c_address=null`；`address_selector=null` |
| 时钟 | 时钟、复位与调试 | `crystal=null`；`oscillator=null`；`reset=null`；`boot=null`；`test_point=null`；`debug_connector=null` |
| 存储 | 存储与存储器 | `flash=null`；`eeprom=null`；`ram=null`；`storage_card=null`；`storage_interface=null` |
| 其他事实 | 音频、传感器与射频分区 | `audio=null`；`sensor_ic=null`；`rf_transceiver=null`；`antenna=null`；`current_measurement=U2 INA199A1DCKR+R3` |
| 关键网络 | Unit Grove to Grove 关键网络索引 | `power=J3 VCC_5V-R1-5V_VIN-U3-R3-5V_OUT-J2`；`enable=J3 EN-U3.4`；`measurement=R3-U2.4/U2.5-U2.6 Imeasure-J3`；`io1=J1-J2 direct`；`io2=J1-J2 direct`；`reference=3V3-R2-U4-U2 REF` |

## 待确认事项

- `analog.current-transfer-not-shown`：原理图确认 R3 20mΩ、U2 INA199A1DCKR 与 TL432 参考网络，但未打印 Imeasure 的零电流电压、增益、满量程电压、误差或从输出电压换算电流的公式。（证据：图 fb059620c11b / 第 1 页 / 页 1 U2/R3/U4/Imeasure 区域，无增益、V/A、满量程或误差文字）
- `review.current-transfer`：Imeasure 的零电流偏置、V/A 换算系数、满量程电压、误差以及 0~1000mA 有效测量范围是什么？；原因：原理图给出分流电阻、放大器和参考网络，但未打印 INA199 增益、TL432 节点电压或整机校准公式。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `fb059620c11b30f537caa9c11cd27cfee6e708d1e694e267985d441281af6257` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/602/Sch_Unit_Grove2Grove_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/unit_grove2grove.md`

源文档 SHA-256：`c6ec59442cb0278470f2b55a906e195491fed41f0ce328a75713a5db996a0277`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
