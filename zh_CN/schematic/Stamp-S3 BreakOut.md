# Stamp-S3 BreakOut 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3 BreakOut |
| SKU | A129 |
| 产品 ID | `stamp-s3-breakout-3a05e8fd268c` |
| 源文档 | `zh_CN/stamp/StampS3BreakOut.md` |

## 概述

Stamp-S3 BreakOut 是一块无源信号转接板，原理图未显示主控、协处理器、存储器、电源转换器或其他功能 IC。P2 与 P4 汇集 Stamp-S3 侧的 GPIO、电源、EN 和 GND 网络，P1、P3、P5 将这些网络引出，J1 提供标注为 IIC_SCL/IIC_SDA 的四针接口。S1 将 G0 按下接地，S2 将 EN 按下接地；板上可见 +5 V、+3.3 V 与 GND 直接分配路径，没有画出电源转换或接口保护器件。

## 检索关键词

`Stamp-S3 BreakOut`、`A129`、`Stamp-S3`、`P1`、`P2`、`P3`、`P4`、`P5`、`J1`、`HY-2.0_IIC`、`IIC_SCL`、`IIC_SDA`、`G15`、`G13`、`G0`、`EN`、`G43`、`G44`、`G46`、`G42`、`G41`、`G40`、`G39`、`+5`、`+3.3V`、`GND`、`S1`、`S2`、`SW-PB`、`Header 6`、`Header 17`、`Header 12`、`Header 11`、`Grove`、`I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 6 | 六针扩展连接器，引出 +3.3V、G43、G44、EN、G0 和 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 B3，P1（Header 6）及 1-6 脚网络标注 |
| P2 | Header 17 | 十七针板内连接器，汇集 G1-G15 中的多个 GPIO、+5 和 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 C2，P2（Header 17）及 1-17 脚网络标注 |
| P3 | Header 12 | 十二针扩展连接器，引出 G1-G7、G13、G15、+5 和两个 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 C2，P3（Header 12）及 1-12 脚网络标注 |
| P4 | Header 11 | 十一针板内连接器，汇集 +3.3V、G46、G43、G42、G44、G41、EN、G40、G0、G39 和 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 C3，P4（Header 11）及 1-11 脚网络标注 |
| P5 | Header 12 | 十二针扩展连接器，引出 G8-G12、G14、G46、G42、G41、G40、G39 和 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 C3，P5（Header 12）及 1-12 脚网络标注 |
| J1 | HY-2.0_IIC | 四针 IIC 接口，针脚依次为 IIC_SCL/G15、IIC_SDA/G13、VCC/+5、GND。 | 图 90d7865bc11c / 第 1 页 / 网格 D3，J1（HY-2.0_IIC）1-4 脚及双侧网络/功能标注 |
| S1 | SW-PB | G0 瞬时按键，闭合时把 G0 接到 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 D2，S1（SW-PB）两端网络 G0 与 GND |
| S2 | SW-PB | EN 瞬时按键，闭合时把 EN 接到 GND。 | 图 90d7865bc11c / 第 1 页 / 网格 D3，S2（SW-PB）两端网络 EN 与 GND |

## 系统结构

### 整板架构

原理图由 P1-P5、J1、S1 和 S2 构成，完成 GPIO、电源、EN、GND 与 IIC 标注信号的连接器转接；本页未显示主控、协处理器、存储器、晶振、传感器、射频、音频或模拟功能 IC。

- 参数与网络：`connectors=P1,P2,P3,P4,P5,J1`；`switches=S1,S2`；`active_ic=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示`
- 证据：图 90d7865bc11c / 第 1 页 / 第 1 页全图，全部可见位号为 P1-P5、J1、S1、S2

## 电源

### +5 电源网络

+5 网络在 P2.13、P3.9 和 J1.3 之间直接分配，J1.3 的功能标注为 VCC；原理图未显示该路径上的转换器、负载开关或保护器件。

- 参数与网络：`rail=+5`；`p2_pin=13`；`p3_pin=9`；`j1_pin=3`；`j1_function=VCC`；`conversion=原理图未显示`；`protection=原理图未显示`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C2 的 P2.13/P3.9 与网格 D3 的 J1.3，均标注 +5

### +3.3V 电源网络

+3.3V 网络在 P4.1 与 P1.1 之间直接引出；原理图未显示该路径上的 LDO、转换器、负载开关或保护器件。

- 参数与网络：`rail=+3.3V`；`p4_pin=1`；`p1_pin=1`；`conversion=原理图未显示`；`load_switch=原理图未显示`；`protection=原理图未显示`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 B3 的 P1.1 与网格 C3 的 P4.1，均标注 +3.3V

### GND 网络

GND 分布到 P1.6、P2.11、P3.8、P3.12、P4.11、P5.12、J1.4，并连接 S1 与 S2 的按键接地端。

- 参数与网络：`connector_pins=P1.6,P2.11,P3.8,P3.12,P4.11,P5.12,J1.4`；`switch_connections=S1,S2`；`net=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 第 1 页各 P1-P5、J1、S1、S2 旁的 GND 网络标注

## 接口

### P2 Header 17

P2 的 17 个针脚依次连接 G1、G2、G3、G4、G5、G6、G7、G8、G9、G10、GND、G11、+5、G12、G13、G14、G15。

- 参数与网络：`reference=P2`；`part_number=Header 17`；`pin_1=G1`；`pin_2=G2`；`pin_3=G3`；`pin_4=G4`；`pin_5=G5`；`pin_6=G6`；`pin_7=G7`；`pin_8=G8`；`pin_9=G9`；`pin_10=G10`；`pin_11=GND`；`pin_12=G11`；`pin_13=+5`；`pin_14=G12`；`pin_15=G13`；`pin_16=G14`；`pin_17=G15`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C2，P2 针脚 1-17

### P4 Header 11

P4 的 11 个针脚依次连接 +3.3V、G46、G43、G42、G44、G41、EN、G40、G0、G39、GND。

- 参数与网络：`reference=P4`；`part_number=Header 11`；`pin_1=+3.3V`；`pin_2=G46`；`pin_3=G43`；`pin_4=G42`；`pin_5=G44`；`pin_6=G41`；`pin_7=EN`；`pin_8=G40`；`pin_9=G0`；`pin_10=G39`；`pin_11=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C3，P4 针脚 1-11

### P1 Header 6

P1 的 6 个针脚依次连接 +3.3V、G43、G44、EN、G0、GND。

- 参数与网络：`reference=P1`；`part_number=Header 6`；`pin_1=+3.3V`；`pin_2=G43`；`pin_3=G44`；`pin_4=EN`；`pin_5=G0`；`pin_6=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 B3，P1 针脚 1-6

### P3 Header 12

P3 的 12 个针脚依次连接 G1、G2、G3、G4、G5、G6、G7、GND、+5、G13、G15、GND。

- 参数与网络：`reference=P3`；`part_number=Header 12`；`pin_1=G1`；`pin_2=G2`；`pin_3=G3`；`pin_4=G4`；`pin_5=G5`；`pin_6=G6`；`pin_7=G7`；`pin_8=GND`；`pin_9=+5`；`pin_10=G13`；`pin_11=G15`；`pin_12=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C2，P3 针脚 1-12

### P5 Header 12

P5 的 12 个针脚依次连接 G8、G9、G10、G11、G12、G14、G46、G42、G41、G40、G39、GND。

- 参数与网络：`reference=P5`；`part_number=Header 12`；`pin_1=G8`；`pin_2=G9`；`pin_3=G10`；`pin_4=G11`；`pin_5=G12`；`pin_6=G14`；`pin_7=G46`；`pin_8=G42`；`pin_9=G41`；`pin_10=G40`；`pin_11=G39`；`pin_12=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C3，P5 针脚 1-12

### J1 HY-2.0_IIC

J1 针脚 1-4 分别标注为 IIC_SCL、IIC_SDA、VCC、GND，并分别连接 G15、G13、+5、GND 网络。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IIC`；`pin_1_function=IIC_SCL`；`pin_1_net=G15`；`pin_2_function=IIC_SDA`；`pin_2_net=G13`；`pin_3_function=VCC`；`pin_3_net=+5`；`pin_4_function=GND`；`pin_4_net=GND`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 D3，J1 针脚 1-4，左侧 G15/G13/+5/GND 与右侧 IIC_SCL/IIC_SDA/VCC/GND 标注

## 总线

### J1 IIC 总线

J1 的 IIC_SCL 信号由 G15 网络引出，IIC_SDA 信号由 G13 网络引出；原理图未画出板载 IIC 设备或上拉电阻。

- 参数与网络：`bus=IIC`；`connector=J1`；`scl_net=G15`；`sda_net=G13`；`onboard_device=原理图未显示`；`pull_up_resistors=原理图未显示`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 D3，J1 的 IIC_SCL/G15 与 IIC_SDA/G13；第 1 页全图无 IIC 设备或上拉电阻位号

## GPIO 与控制信号

### S1 与 G0

S1 是连接在 G0 与 GND 之间的 SW-PB 瞬时按键，闭合时将 G0 拉到 GND。

- 参数与网络：`reference=S1`；`part_number=SW-PB`；`signal=G0`；`active_connection=GND`；`action=按下闭合`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 D2，S1 左端 GND、右端 G0

### G0 与 EN 网络引出

G0 在 P4.9、P1.5 和 S1 之间连接；EN 在 P4.7、P1.4 和 S2 之间连接。

- 参数与网络：`g0_connections=P4.9,P1.5,S1`；`en_connections=P4.7,P1.4,S2`；`g0_switch=S1`；`en_switch=S2`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 B3/C3/D2-D3 的 P1、P4、S1、S2 上 G0 与 EN 标注

## 复位

### S2 与 EN

S2 是连接在 EN 与 GND 之间的 SW-PB 瞬时按键，闭合时将 EN 拉到 GND。

- 参数与网络：`reference=S2`；`part_number=SW-PB`；`signal=EN`；`active_connection=GND`；`action=按下闭合`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 D3，S2 左端 EN、右端 GND

## 关键网络

### G13 网络

G13 同时连接 P2.15、P3.10 和 J1.2，J1 侧功能标注为 IIC_SDA。

- 参数与网络：`net=G13`；`connections=P2.15,P3.10,J1.2`；`j1_function=IIC_SDA`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C2 的 P2.15/P3.10 与网格 D3 的 J1.2，均标注 G13

### G15 网络

G15 同时连接 P2.17、P3.11 和 J1.1，J1 侧功能标注为 IIC_SCL。

- 参数与网络：`net=G15`；`connections=P2.17,P3.11,J1.1`；`j1_function=IIC_SCL`
- 证据：图 90d7865bc11c / 第 1 页 / 网格 C2 的 P2.17/P3.11 与网格 D3 的 J1.1，均标注 G15

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `connectors=P1,P2,P3,P4,P5,J1`；`switches=S1,S2`；`active_ic=原理图未显示`；`storage=原理图未显示`；`clock=原理图未显示` |
| 接口 | P2 Header 17 | `reference=P2`；`part_number=Header 17`；`pin_1=G1`；`pin_2=G2`；`pin_3=G3`；`pin_4=G4`；`pin_5=G5`；`pin_6=G6`；`pin_7=G7`；`pin_8=G8`；`pin_9=G9`；`pin_10=G10`；`pin_11=GND`；`pin_12=G11`；`pin_13=+5`；`pin_14=G12`；`pin_15=G13`；`pin_16=G14`；`pin_17=G15` |
| 接口 | P4 Header 11 | `reference=P4`；`part_number=Header 11`；`pin_1=+3.3V`；`pin_2=G46`；`pin_3=G43`；`pin_4=G42`；`pin_5=G44`；`pin_6=G41`；`pin_7=EN`；`pin_8=G40`；`pin_9=G0`；`pin_10=G39`；`pin_11=GND` |
| 接口 | P1 Header 6 | `reference=P1`；`part_number=Header 6`；`pin_1=+3.3V`；`pin_2=G43`；`pin_3=G44`；`pin_4=EN`；`pin_5=G0`；`pin_6=GND` |
| 接口 | P3 Header 12 | `reference=P3`；`part_number=Header 12`；`pin_1=G1`；`pin_2=G2`；`pin_3=G3`；`pin_4=G4`；`pin_5=G5`；`pin_6=G6`；`pin_7=G7`；`pin_8=GND`；`pin_9=+5`；`pin_10=G13`；`pin_11=G15`；`pin_12=GND` |
| 接口 | P5 Header 12 | `reference=P5`；`part_number=Header 12`；`pin_1=G8`；`pin_2=G9`；`pin_3=G10`；`pin_4=G11`；`pin_5=G12`；`pin_6=G14`；`pin_7=G46`；`pin_8=G42`；`pin_9=G41`；`pin_10=G40`；`pin_11=G39`；`pin_12=GND` |
| 接口 | J1 HY-2.0_IIC | `reference=J1`；`part_number=HY-2.0_IIC`；`pin_1_function=IIC_SCL`；`pin_1_net=G15`；`pin_2_function=IIC_SDA`；`pin_2_net=G13`；`pin_3_function=VCC`；`pin_3_net=+5`；`pin_4_function=GND`；`pin_4_net=GND` |
| 总线 | J1 IIC 总线 | `bus=IIC`；`connector=J1`；`scl_net=G15`；`sda_net=G13`；`onboard_device=原理图未显示`；`pull_up_resistors=原理图未显示` |
| GPIO 与控制信号 | S1 与 G0 | `reference=S1`；`part_number=SW-PB`；`signal=G0`；`active_connection=GND`；`action=按下闭合` |
| 复位 | S2 与 EN | `reference=S2`；`part_number=SW-PB`；`signal=EN`；`active_connection=GND`；`action=按下闭合` |
| 电源 | +5 电源网络 | `rail=+5`；`p2_pin=13`；`p3_pin=9`；`j1_pin=3`；`j1_function=VCC`；`conversion=原理图未显示`；`protection=原理图未显示` |
| 电源 | +3.3V 电源网络 | `rail=+3.3V`；`p4_pin=1`；`p1_pin=1`；`conversion=原理图未显示`；`load_switch=原理图未显示`；`protection=原理图未显示` |
| 电源 | GND 网络 | `connector_pins=P1.6,P2.11,P3.8,P3.12,P4.11,P5.12,J1.4`；`switch_connections=S1,S2`；`net=GND` |
| 关键网络 | G13 网络 | `net=G13`；`connections=P2.15,P3.10,J1.2`；`j1_function=IIC_SDA` |
| 关键网络 | G15 网络 | `net=G15`；`connections=P2.17,P3.11,J1.1`；`j1_function=IIC_SCL` |
| GPIO 与控制信号 | G0 与 EN 网络引出 | `g0_connections=P4.9,P1.5,S1`；`en_connections=P4.7,P1.4,S2`；`g0_switch=S1`；`en_switch=S2` |
| 总线 | J1 IIC 方向与电平 | `connector=J1`；`scl_net=G15`；`sda_net=G13`；`controller=未标注`；`device=未标注`；`signal_voltage=未标注` |

## 待确认事项

- `bus.iic-role-level-undetermined`：原理图仅给出 J1 的 IIC_SCL/IIC_SDA 功能名及 G15/G13 网络映射，不能从该页确定总线控制器、外设方向或 SCL/SDA 信号电平。（证据：图 90d7865bc11c / 第 1 页 / 网格 D3，J1 仅标注 IIC_SCL/IIC_SDA/VCC/GND 和 G15/G13/+5/GND）
- `review.iic-role-level`：J1 的 IIC_SCL/IIC_SDA 由哪一控制器驱动，信号方向和电平是多少？；原因：该原理图只显示网络映射，没有画出 Stamp-S3 内部控制器、电平规格、外设或上拉配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `90d7865bc11c3d578693aa1f8ebffb7c7dac4689d69a24e7d380158f5c8b45d5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/534/Sch_StampS3BreakOut_sch_01.png` |

---

源文档：`zh_CN/stamp/StampS3BreakOut.md`

源文档 SHA-256：`ef036c9d77340e3daf726f4273d90080b8608e79c0c49885863270cd4fb0aa69`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
