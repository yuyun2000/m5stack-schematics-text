# Stamp-AddOn Cam3660 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-AddOn Cam3660 |
| SKU | A182 |
| 产品 ID | `stamp-addon-cam3660-5a49456d2fd0` |
| 源文档 | `zh_CN/stamp/Stamp-AddOn_Cam3660.md` |

## 概述

Stamp-AddOn Cam3660 的本地附件是一页摄像头模组机械与接口规格图，标出 OV3660 感光芯片、镜头参数、L 形 FPC、24Pin 连接器及完整针脚表。模组连接器引出 D0-D7、MCLK、PCLK、VS、HS、RESET、PWDN、SCL、SDA、VCC3.3V、GND 和 SYS。该页还给出 DVDD、AVDD、DOVDD 规格以及 FPC、钢片补强、背胶撕手和安装孔尺寸，但没有展示内部供电转换或信号电路拓扑。

## 检索关键词

`Stamp-AddOn Cam3660`、`A182`、`HZVS6049 V1.0`、`OV3660`、`OK-14GM024-04`、`2048X1536`、`1/5inch`、`2.41mm`、`F2.2`、`74 degree`、`24Pin B2B`、`8-bit parallel camera`、`DVP`、`SCCB`、`MCLK`、`PCLK`、`VS`、`HS`、`D0-D7`、`RESET`、`PWDN`、`SCL`、`SDA`、`VCC3.3V`、`DVDD`、`AVDD`、`DOVDD`、`SYS`、`FPC`、`steel reinforcement`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| OV3660 image sensor | OV3660 | 2048 x 1536 CMOS 感光芯片；本页模块规格表明确给出芯片型号和像素阵列。 | 图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表的 Chip Type 与 Array Size 行 |
| Lens & Holder | 未标注 | 摄像头镜头与镜座组件；本页给出焦距、光圈、视场角、畸变、对焦范围和镜头尺寸。 | 图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F3，Module Specification 表左半部及 Lens & Holder 标题 |
| EXP.B2B 24-pin connector | OK-14GM024-04 | 模组尾端 24Pin 板对板连接器，承载并行图像信号、控制、时钟和供电引脚。 | 图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D1，连接器外形图下方型号 OK-14GM024-04；网格 B8-D8 的 1-24 针表 |
| FPC camera assembly | HZVS6049 V1.0 | 承载镜头、安装孔、钢片补强、背胶撕手和尾端连接器的 L 形柔性摄像头组件。 | 图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B1-D6 的前视图、侧视图和 FPC 外形图；网格 F6-F8 图框 MODEL: HZVS6049 V1.0 |

## 系统结构

### Stamp-AddOn Cam3660 模组构成

本页描绘一体式摄像头镜头、L 形 FPC、侧边安装孔、背胶撕手和尾端 24Pin 连接器。

- 参数与网络：`drawing_type=camera module mechanical and interface specification`；`module_model=HZVS6049 V1.0`；`connector_positions=24`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B1-D6，摄像头前视图、侧视图、L 形 FPC 外形和尾端连接器视图

## 核心器件

### 模组型号

图框 MODEL 字段标注 HZVS6049 V1.0。

- 参数与网络：`model=HZVS6049 V1.0`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F6-F8，右下图框 MODEL: HZVS6049 V1.0

### 镜头组件工艺

Module Specification 表的工艺字段标为黑胶。

- 参数与网络：`process=黑胶`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3，Module Specification 表 工艺 行

## 电源

### 数字电路电压 DVDD

模块规格表将 DVDD 标为 1.5V ±5%。

- 参数与网络：`rail=DVDD`；`voltage_v=1.5`；`tolerance_percent=5`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3，Module Specification 表 DVDD 行

### 模拟电路电压 AVDD

模块规格表将 AVDD 标为 2.6V 至 3.3V。

- 参数与网络：`rail=AVDD`；`voltage_min_v=2.6`；`voltage_max_v=3.3`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3，Module Specification 表 AVDD 行

### 接口电路电压 DOVDD

模块规格表将 DOVDD 标为 1.8V / 2.8V。

- 参数与网络：`rail=DOVDD`；`voltage_options=1.8V / 2.8V`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3，Module Specification 表 DOVDD 行

### 连接器电源引脚

VCC3.3V 位于连接器 20 脚。

- 参数与网络：`net=VCC3.3V`；`connector_pin=20`；`nominal_voltage_v=3.3`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D8，NO./SYMBOL 针脚表第 20 行

### 连接器地

GND 位于连接器 13 脚和 21 脚。

- 参数与网络：`net=GND`；`connector_pins=13, 21`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 C8-D8，NO./SYMBOL 针脚表第 13 行和第 21 行

## 接口

### 尾端连接器

尾端连接器外形图标注 OK-14GM024-04，右侧针脚表覆盖 1 至 24 共 24 个位置。

- 参数与网络：`part_number=OK-14GM024-04`；`position_count=24`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D1 的连接器外形与型号；网格 B8-D8 的 NO./SYMBOL 针脚表

### 24Pin 连接器完整针脚映射

图纸按位置 1 至 24 列出 MCLK、D7、NC、D6、RESET、D5、NC、PCLK、VS、D4、PWDN、D3、GND、D2、HS、D1、NC、D0、SCL、VCC3.3V、GND、SYS、SDA、SYS。

- 参数与网络：`pin_1=MCLK`；`pin_2=D7`；`pin_3=NC`；`pin_4=D6`；`pin_5=RESET`；`pin_6=D5`；`pin_7=NC`；`pin_8=PCLK`；`pin_9=VS`；`pin_10=D4`；`pin_11=PWDN`；`pin_12=D3`；`pin_13=GND`；`pin_14=D2`；`pin_15=HS`；`pin_16=D1`；`pin_17=NC`；`pin_18=D0`；`pin_19=SCL`；`pin_20=VCC3.3V`；`pin_21=GND`；`pin_22=SYS`；`pin_23=SDA`；`pin_24=SYS`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8-D8，NO./SYMBOL 针脚表第 1-24 行

### 未连接位置

连接器 3、7、17 脚标为 NC。

- 参数与网络：`NC_pins=3, 7, 17`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8-D8，NO./SYMBOL 针脚表第 3、7、17 行

## 总线

### 并行图像数据线

连接器引出 D0 至 D7 共 8 根数据线，位置依次为 D0=18、D1=16、D2=14、D3=12、D4=10、D5=6、D6=4、D7=2。

- 参数与网络：`width_bits=8`；`D0_pin=18`；`D1_pin=16`；`D2_pin=14`；`D3_pin=12`；`D4_pin=10`；`D5_pin=6`；`D6_pin=4`；`D7_pin=2`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8-D8，NO./SYMBOL 针脚表中的 D0-D7 行

### SCL/SDA 控制信号

连接器将 SCL 映射到 19 脚，将 SDA 映射到 23 脚。

- 参数与网络：`SCL_pin=19`；`SDA_pin=23`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D8，NO./SYMBOL 针脚表第 19 行 SCL 和第 23 行 SDA

## 时钟

### MCLK

MCLK 位于连接器 1 脚。

- 参数与网络：`net=MCLK`；`connector_pin=1`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8，NO./SYMBOL 针脚表第 1 行

### PCLK

PCLK 位于连接器 8 脚。

- 参数与网络：`net=PCLK`；`connector_pin=8`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8，NO./SYMBOL 针脚表第 8 行

## 复位

### RESET

RESET 位于连接器 5 脚；本页未标注有效电平。

- 参数与网络：`net=RESET`；`connector_pin=5`；`active_level=null`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8，NO./SYMBOL 针脚表第 5 行

## 关键网络

### 图像同步信号

连接器将 VS 映射到 9 脚，将 HS 映射到 15 脚。

- 参数与网络：`VS_pin=9`；`HS_pin=15`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B8-C8，NO./SYMBOL 针脚表第 9 行 VS 和第 15 行 HS

### PWDN

PWDN 位于连接器 11 脚；本页未标注有效电平。

- 参数与网络：`net=PWDN`；`connector_pin=11`；`active_level=null`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 C8，NO./SYMBOL 针脚表第 11 行

### SYS

SYS 网络出现在连接器 22 脚和 24 脚。

- 参数与网络：`net=SYS`；`connector_pins=22, 24`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D8，NO./SYMBOL 针脚表第 22 行和第 24 行

## 传感器

### 感光芯片

Module Specification 表将感光芯片型号标为 OV3660。

- 参数与网络：`chip_type=OV3660`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 Chip Type 行

### 感光阵列

OV3660 的 Array Size 在本页标为 2048X1536。

- 参数与网络：`array_size=2048X1536`；`horizontal_pixels=2048`；`vertical_pixels=1536`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 Array Size 行

## 模拟电路

### 镜头焦距

镜头有效焦距 EFL 标为 2.41 mm，公差 ±5%。

- 参数与网络：`efl_mm=2.41`；`tolerance_percent=5`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 EFL 行

### 镜头光圈

镜头光圈 F.NO 标为 2.2，公差 ±5%。

- 参数与网络：`f_number=2.2`；`tolerance_percent=5`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 F.NO 行

### 镜头视场角

镜头 View Angle 标为 74°。

- 参数与网络：`view_angle_degrees=74`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 View Angle 行

### 镜头畸变

镜头 Distortion 标为小于 1.0%。

- 参数与网络：`distortion=<1.0%`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 Distortion 行

### 镜头对焦范围

Focusing Range 原文标注为 20CM ~ ∞ (AT60CM)。

- 参数与网络：`focusing_range=20CM ~ infinity (AT60CM)`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 Focusing Range 行

### 镜头规格

Lens Size 标为 1/5inch。

- 参数与网络：`lens_size=1/5inch`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F1-F2，Module Specification 表 Lens Size 行

### 镜头调焦与固定

调焦距离标为 60CM，并注明点胶固定。

- 参数与网络：`adjustment_distance_cm=60`；`locking_method=点胶`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3，Module Specification 表 调焦距离 行

## 其他事实

### 镜头端前视尺寸

镜头端前视图顶部水平尺寸标为 17.800±0.1 mm，镜头同心圆标有 Ø5 mm 和 Ø6.2 mm，安装孔补强外径标为 Ø4 mm。

- 参数与网络：`horizontal_dimension_mm=17.800±0.1`；`lens_diameter_callout_1_mm=5`；`lens_diameter_callout_2_mm=6.2`；`mount_reinforcement_outer_diameter_mm=4`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B1-B3，摄像头前视图的 17.800±0.1、Ø5、Ø6.2 和 Ø4 尺寸标注

### 镜头端侧视剖面

侧视图从 FPC 基准到镜头组件各轮廓给出 1.55±0.10 mm、2.7±0.10 mm 和 4.77±0.20 mm 三个尺寸。

- 参数与网络：`profile_dimension_1_mm=1.55±0.10`；`profile_dimension_2_mm=2.7±0.10`；`profile_dimension_3_mm=4.77±0.20`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B3-B4，镜头端侧视图顶部三组尺寸

### FPC 含胶厚度

侧视图文字标注 FPC 有胶厚度 0.12MM。

- 参数与网络：`fpc_with_adhesive_thickness_mm=0.12`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 C3-D4，侧视图中部文字 FPC有胶厚度0.12MM

### 钢片补强厚度

侧视图在镜头端和连接器端的钢片补强处均给出 0.30±0.05 mm 尺寸标注。

- 参数与网络：`reinforcement_thickness_mm=0.30±0.05`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B3-D4，侧视图上下两处 钢片补强 与 0.30±0.05 标注

### 镜头端背胶区域

背胶区域外形给出 17.800±0.1 mm 水平尺寸和 12.000±0.1 mm 垂直尺寸，内部轮廓给出 13.80 mm 与 11.50 mm。

- 参数与网络：`outer_width_mm=17.800±0.1`；`outer_height_mm=12.000±0.1`；`inner_width_mm=13.8`；`inner_height_mm=11.5`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B5-C7，钢片开窗/双面背胶带撕手外形图的 17.800±0.1、12.000±0.1、13.80、11.50 标注

### 钢片开窗与安装孔

背胶区域左侧注明钢片开窗，圆孔标为 Ø2.00 mm。

- 参数与网络：`feature=钢片开窗`；`hole_diameter_mm=2`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B5-B6，钢片开窗文字和 Ø2.00 圆孔标注

### 双面背胶撕手

外形图明确标注双面背胶带撕手，并用引线标出右下斜边处的撕手位；该区域另注钢片补强 0.3 mm。

- 参数与网络：`adhesive_feature=双面背胶带撕手`；`tear_position=右下斜边`；`steel_reinforcement_mm=0.3`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 B5-C7，双面背胶带撕手、撕手位和钢片补强0.3mm 标注

### 连接器端补强区域

连接器端钢片补强区域标出 8.20±0.1 mm 水平尺寸和 4.76±0.1 mm 垂直尺寸，并注明钢片补强 0.3 mm。

- 参数与网络：`width_mm=8.20±0.1`；`height_mm=4.76±0.1`；`steel_reinforcement_mm=0.3`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D5-E7，连接器端外形下方 8.20±0.1、4.76±0.1 和 钢片补强0.3mm 标注

### 拍摄方向

图纸左上角以 Capture Direction 图标标示镜头拍摄方向。

- 参数与网络：`annotation=Capture Direction`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 A1，Capture Direction 图标

### 图纸制图信息

图框使用第三角投影，单位为 mm，图幅为 A4，比例为 1:1。

- 参数与网络：`projection=3rd ANGLE`；`unit=mm`；`sheet_size=A4`；`scale=1:1`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F5-F8，右下图框的 3rd ANGLE、UNIT、SIZE 和 SCALE 字段

### 图纸修订记录

修订表列出 2026/01/26 的 Rev.1.0（First release）和 2026/02/26 的 Rev.2.0。

- 参数与网络：`rev_1_0_date=2026/01/26`；`rev_1_0_note=First release`；`rev_2_0_date=2026/02/26`
- 证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 A6-A8，Date/Rev./Revisions 修订表

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-AddOn Cam3660 模组构成 | `drawing_type=camera module mechanical and interface specification`；`module_model=HZVS6049 V1.0`；`connector_positions=24` |
| 核心器件 | 模组型号 | `model=HZVS6049 V1.0` |
| 传感器 | 感光芯片 | `chip_type=OV3660` |
| 传感器 | 感光阵列 | `array_size=2048X1536`；`horizontal_pixels=2048`；`vertical_pixels=1536` |
| 模拟电路 | 镜头焦距 | `efl_mm=2.41`；`tolerance_percent=5` |
| 模拟电路 | 镜头光圈 | `f_number=2.2`；`tolerance_percent=5` |
| 模拟电路 | 镜头视场角 | `view_angle_degrees=74` |
| 模拟电路 | 镜头畸变 | `distortion=<1.0%` |
| 模拟电路 | 镜头对焦范围 | `focusing_range=20CM ~ infinity (AT60CM)` |
| 模拟电路 | 镜头规格 | `lens_size=1/5inch` |
| 模拟电路 | 镜头调焦与固定 | `adjustment_distance_cm=60`；`locking_method=点胶` |
| 核心器件 | 镜头组件工艺 | `process=黑胶` |
| 电源 | 数字电路电压 DVDD | `rail=DVDD`；`voltage_v=1.5`；`tolerance_percent=5` |
| 电源 | 模拟电路电压 AVDD | `rail=AVDD`；`voltage_min_v=2.6`；`voltage_max_v=3.3` |
| 电源 | 接口电路电压 DOVDD | `rail=DOVDD`；`voltage_options=1.8V / 2.8V` |
| 接口 | 尾端连接器 | `part_number=OK-14GM024-04`；`position_count=24` |
| 接口 | 24Pin 连接器完整针脚映射 | `pin_1=MCLK`；`pin_2=D7`；`pin_3=NC`；`pin_4=D6`；`pin_5=RESET`；`pin_6=D5`；`pin_7=NC`；`pin_8=PCLK`；`pin_9=VS`；`pin_10=D4`；`pin_11=PWDN`；`pin_12=D3`；`pin_13=GND`；`pin_14=D2`；`pin_15=HS`；`pin_16=D1`；`pin_17=NC`；`pin_18=D0`；`pin_19=SCL`；`pin_20=VCC3.3V`；`pin_21=GND`；`pin_22=SYS`；`pin_23=SDA`；`pin_24=SYS` |
| 总线 | 并行图像数据线 | `width_bits=8`；`D0_pin=18`；`D1_pin=16`；`D2_pin=14`；`D3_pin=12`；`D4_pin=10`；`D5_pin=6`；`D6_pin=4`；`D7_pin=2` |
| 时钟 | MCLK | `net=MCLK`；`connector_pin=1` |
| 时钟 | PCLK | `net=PCLK`；`connector_pin=8` |
| 关键网络 | 图像同步信号 | `VS_pin=9`；`HS_pin=15` |
| 复位 | RESET | `net=RESET`；`connector_pin=5`；`active_level=null` |
| 关键网络 | PWDN | `net=PWDN`；`connector_pin=11`；`active_level=null` |
| 总线 | SCL/SDA 控制信号 | `SCL_pin=19`；`SDA_pin=23` |
| 电源 | 连接器电源引脚 | `net=VCC3.3V`；`connector_pin=20`；`nominal_voltage_v=3.3` |
| 电源 | 连接器地 | `net=GND`；`connector_pins=13, 21` |
| 关键网络 | SYS | `net=SYS`；`connector_pins=22, 24` |
| 接口 | 未连接位置 | `NC_pins=3, 7, 17` |
| 其他事实 | 镜头端前视尺寸 | `horizontal_dimension_mm=17.800±0.1`；`lens_diameter_callout_1_mm=5`；`lens_diameter_callout_2_mm=6.2`；`mount_reinforcement_outer_diameter_mm=4` |
| 其他事实 | 镜头端侧视剖面 | `profile_dimension_1_mm=1.55±0.10`；`profile_dimension_2_mm=2.7±0.10`；`profile_dimension_3_mm=4.77±0.20` |
| 其他事实 | FPC 含胶厚度 | `fpc_with_adhesive_thickness_mm=0.12` |
| 其他事实 | 钢片补强厚度 | `reinforcement_thickness_mm=0.30±0.05` |
| 其他事实 | 镜头端背胶区域 | `outer_width_mm=17.800±0.1`；`outer_height_mm=12.000±0.1`；`inner_width_mm=13.8`；`inner_height_mm=11.5` |
| 其他事实 | 钢片开窗与安装孔 | `feature=钢片开窗`；`hole_diameter_mm=2` |
| 其他事实 | 双面背胶撕手 | `adhesive_feature=双面背胶带撕手`；`tear_position=右下斜边`；`steel_reinforcement_mm=0.3` |
| 其他事实 | 连接器端补强区域 | `width_mm=8.20±0.1`；`height_mm=4.76±0.1`；`steel_reinforcement_mm=0.3` |
| 其他事实 | 拍摄方向 | `annotation=Capture Direction` |
| 其他事实 | 图纸制图信息 | `projection=3rd ANGLE`；`unit=mm`；`sheet_size=A4`；`scale=1:1` |
| 其他事实 | 图纸修订记录 | `rev_1_0_date=2026/01/26`；`rev_1_0_note=First release`；`rev_2_0_date=2026/02/26` |
| 总线 | SCL/SDA 协议与地址 | `SCL_pin=19`；`SDA_pin=23`；`protocol=null`；`device_address=null`；`pull_up=null` |
| 电源 | VCC3.3V 与内部电源轨关系 | `connector_supply=VCC3.3V on pin 20`；`listed_internal_rails=DVDD 1.5V±5%; AVDD 2.6V to 3.3V; DOVDD 1.8V/2.8V`；`regulator_topology=null` |
| 其他事实 | 本页适用修订号 | `model_field=HZVS6049 V1.0`；`latest_revision_table_entry=2.0 dated 2026/02/26`；`title_block_rev=null` |

## 待确认事项

- `bus.scl-sda-protocol-address`：本页只给出 SCL 和 SDA 的连接器位置，没有在图内标注总线协议、从设备地址、上拉电阻或电气时序。（证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 D8 的 SCL/SDA 针脚行；本页其余区域为机械与规格信息，未见协议、地址或上拉电路）
- `power.internal-rail-implementation`：本页同时列出连接器 VCC3.3V 和 DVDD/AVDD/DOVDD 规格，但没有内部电路图，无法确认这些电源轨由何种器件产生或如何连接。（证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 F2-F3 的 DVDD/AVDD/DOVDD 规格与网格 D8 的 VCC3.3V 针脚；本页未示电源电路）
- `other.applicable-drawing-revision`：图框 MODEL 写有 HZVS6049 V1.0，修订表又包含 Rev.2.0，而图框 REV. 字段为空，因此无法仅凭本页确定当前适用的图纸修订号。（证据：图 7d889bdb7d23 / 第 1 页 / 页 1 网格 A6-A8 修订表及网格 F6-F8 图框 MODEL/REV. 字段）
- `review.scl-sda-protocol-address`：SCL/SDA 的正式协议、设备地址、上拉位置与电气要求是什么？；原因：机械/接口规格页只提供信号名和针脚号，不能据此确认 SCCB/I2C 细节或地址。
- `review.internal-rail-implementation`：VCC3.3V 如何生成或连接 DVDD、AVDD 与 DOVDD，模组内是否包含稳压或电平转换器件？；原因：本页只有电压规格和一个 3.3V 连接器针脚，没有内部原理图或器件连接。
- `review.applicable-drawing-revision`：该附件正式适用的图纸修订号是 Rev.1.0 还是 Rev.2.0？；原因：MODEL 字段含 V1.0、修订表含 Rev.2.0，且图框 REV. 字段未填写。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7d889bdb7d231cdfee2d74f5f453a6424a04194added46101cc206da939d32b0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1266/A182_Stamp-AddOn_Cam3660_HZVS6049_V1.0_CS-Model_3660_2026_04_13_15_25_47_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp-AddOn_Cam3660.md`

源文档 SHA-256：`ef7f5aa818b7eac0fa5738fb72592402d11b0b25c2e10efbe33361fe10a766e1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
