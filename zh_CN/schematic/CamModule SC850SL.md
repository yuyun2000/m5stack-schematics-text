# CamModule SC850SL 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CamModule SC850SL |
| SKU | A157 |
| 产品 ID | `cammodule-sc850sl-002eb6b0807b` |
| 源文档 | `zh_CN/accessory/CamModule_SC850SL.md` |

## 概述

CamModule SC850SL 以 U1 SC850SL 图像传感器为核心，通过 J1 30 针 FPC 引出四条 MIPI CSI-2 数据通道和一条差分时钟通道。控制侧包括 1.8V I2C、CAM_RSTN 和 CAM_MCLK，SID 通过 0Ω 电阻固定为低电平。传感器使用 AVDD_2V8、DOVDD_1V8 和 DVDD_1V3 三个电源域，其中 U2 TPS7A9101DSK 从 DOVDD_1V8 生成 DVDD_1V3；连接器另有 DVDD_1V2 引脚，但图中未显示其与核心电源相连。

## 检索关键词

`CamModule SC850SL`、`A157`、`SC850SL`、`TPS7A9101DSK`、`MIPI CSI-2`、`4 Lane`、`MIPI_RX0`、`MIPI_RX1`、`MIPI_RX2`、`MIPI_RX3`、`MIPI_RX4`、`CAM_SDA_1V8`、`CAM_SCL_1V8`、`CAM_RSTN`、`CAM_MCLK`、`AVDD_2V8`、`DOVDD_1V8`、`DVDD_1V3`、`DVDD_1V2`、`SID`、`XSHUTDN`、`EXTCLK`、`FPC 30P`、`FH34SRJ-30S-0.5SH`、`M0CP`、`M0D0P`、`M0D1P`、`M0D2P`、`M0D3P`、`VREFH`、`VREFN`、`TXVDD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SC850SL | CMOS 图像传感器，提供四通道 MIPI 输出、I2C 控制、复位和外部时钟接口 | 图 9efa49abd81c / 第 1 页 / 网格 1A-3D，U1A-U1E SC850SL 的电源、控制、参考和 MIPI 分部符号 |
| U2 | TPS7A9101DSK | DOVDD_1V8 到 DVDD_1V3 的低压差稳压器 | 图 9efa49abd81c / 第 1 页 / 网格 3A-4A，U2 TPS7A9101DSK、DOVDD_1V8 输入、DVDD_1V3 输出和反馈网络 |
| J1 | FPC-SMD_30P-FH34SRJ-30S-0.5SH | 30 针摄像头电源、控制和 MIPI CSI 接口 | 图 9efa49abd81c / 第 1 页 / 网格 5A-6B，J1 pin1-pin30、SH、五组 MIPI 差分对、控制线和三路外部电源 |
| R3 | 0R/1% | SC850SL SID 配置下拉电阻 | 图 9efa49abd81c / 第 1 页 / 网格 1C，U1C SID pin D10 经 R3 0R/1% 接 GND |
| R1,R2,C1 | 7.5K/1%, 12K/1%, 10nF/10V | TPS7A9101DSK 输出反馈与前馈网络 | 图 9efa49abd81c / 第 1 页 / 网格 4A，U2 FB pin3、R1 7.5K、R2 12K、C1 10nF 与 DVDD_1V3 |
| C2 | 100nF/10V | TPS7A9101DSK NR/SS 软启动/降噪电容 | 图 9efa49abd81c / 第 1 页 / 网格 3A-4A，U2 NR/SS pin8 经 C2 100nF 接 GND |
| C5-C9 | 1uF | SC850SL VREFH、VREFN2、VREFN、VREF3 和 TXVDD 参考/内部电源去耦 | 图 9efa49abd81c / 第 1 页 / 网格 1B-2B，U1B 的 VREFH/VREFN2/VREFN/VREF3/TXVDD 分别连接 C5-C9 到 GND |
| C10-C19 | AVDD_2V8 decoupling network | AVDD_2V8 模拟电源的分布式去耦 | 图 9efa49abd81c / 第 1 页 / 网格 3B-5B，AVDD_2V8 上 C10-C13 1uF、C14-C18 100nF、C19 10uF |
| C20-C28 | DOVDD_1V8 decoupling network | DOVDD_1V8 I/O 电源的分布式去耦 | 图 9efa49abd81c / 第 1 页 / 网格 3C-5C，DOVDD_1V8 上 C20-C22 1uF、C23-C27 100nF、C28 10uF |
| C29-C38 | DVDD_1V3 decoupling network | DVDD_1V3 核心电源的分布式去耦 | 图 9efa49abd81c / 第 1 页 / 网格 3C-5C，DVDD_1V3 上 C29-C32 1uF、C33-C37 100nF、C38 10uF |

## 系统结构

### SC850SL 摄像头模组架构

U1 SC850SL 由三路电源域供电，通过 1.8V I2C、复位和主时钟控制，并以四条数据通道加一条时钟通道的 MIPI 差分接口连接 J1。

- 参数与网络：`sensor=U1 SC850SL`；`connector=J1 30P FPC`；`power_domains=AVDD_2V8, DOVDD_1V8, DVDD_1V3`；`control=CAM_SDA_1V8, CAM_SCL_1V8, CAM_RSTN, CAM_MCLK`；`mipi_data_lanes=4`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1A-3D 的 U1 各分部、网格 5A-6B 的 J1 和网格 3A-4A 的 U2

## 核心器件

### SC850SL M1 差分接口

U1E 的 M1CP/M1CN 和 M1D0-M1D3 四组差分引脚均在原理图中标记为未连接。

- 参数与网络：`sensor_section=U1E`；`unused_pairs=M1CP/M1CN, M1D0P/N, M1D1P/N, M1D2P/N, M1D3P/N`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 2D，U1E 全部 M1 接口引脚右侧的未连接标记

## 电源

### SC850SL 模拟电源 AVDD_2V8

AVDD_2V8 连接 U1A 的 A2、A4、A7、A9、E1、E6、E10 七个 AVDD 引脚，并从 J1 pin9 输入。

- 参数与网络：`net=AVDD_2V8`；`sensor_pins=A2,A4,A7,A9,E1,E6,E10`；`connector_pin=9`；`domain=analog`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1A-2A 的 U1A AVDD 引脚与网格 5A-6B 的 J1 pin9 AVDD_2V8

### SC850SL I/O 电源 DOVDD_1V8

DOVDD_1V8 连接 U1A 的 A5、C4、C7、E2、E5、E9 六个 DOVDD 引脚，并从 J1 pin8 输入。

- 参数与网络：`net=DOVDD_1V8`；`sensor_pins=A5,C4,C7,E2,E5,E9`；`connector_pin=8`；`domain=digital_io`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1A-2A 的 U1A DOVDD 引脚与网格 5A-6B 的 J1 pin8 DOVDD_1V8

### SC850SL 核心电源 DVDD_1V3

DVDD_1V3 连接 U1A 的 B1、B10、D2、D3、D4、D7、D8、D9 八个 DVDD 引脚，并由 U2 TPS7A9101DSK 从 DOVDD_1V8 生成。

- 参数与网络：`net=DVDD_1V3`；`sensor_pins=B1,B10,D2,D3,D4,D7,D8,D9`；`regulator=U2 TPS7A9101DSK`；`regulator_input=DOVDD_1V8`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1A-2A U1A DVDD 引脚与网格 3A-4A U2 OUT/DVDD_1V3

### TPS7A9101DSK 配置

U2 IN pin9/10、SS_CTRL pin6 和 EN pin7 接 DOVDD_1V8，OUT pin1/2 输出 DVDD_1V3；FB 使用 R1 7.5kΩ、R2 12kΩ 和 C1 10nF，NR/SS 通过 C2 100nF 接地，PG pin5 未连接。

- 参数与网络：`reference=U2`；`input=DOVDD_1V8`；`output=DVDD_1V3`；`feedback_upper=R1 7.5kΩ`；`feedback_lower=R2 12kΩ`；`feedforward_capacitor=C1 10nF`；`nr_ss_capacitor=C2 100nF`；`power_good=NC`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 3A-4A，U2、R1、R2、C1、C2 及 DOVDD_1V8/DVDD_1V3

### 三路传感器电源去耦

AVDD_2V8 使用 C10-C19，DOVDD_1V8 使用 C20-C28，DVDD_1V3 使用 C29-C38 形成分布式 1uF、100nF 和 10uF 去耦网络。

- 参数与网络：`avdd_2v8=C10-C13 1uF, C14-C18 100nF, C19 10uF`；`dovdd_1v8=C20-C22 1uF, C23-C27 100nF, C28 10uF`；`dvdd_1v3=C29-C32 1uF, C33-C37 100nF, C38 10uF`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 3B-5C，AVDD_2V8、DOVDD_1V8、DVDD_1V3 三组电容阵列

## 接口

### J1 30 针 FPC 接口

J1 pin1-pin5 未连接，pin6/10/15/18/21/24/27/30 和 SH 接 GND，pin7=DVDD_1V2、pin8=DOVDD_1V8、pin9=AVDD_2V8、pin11-pin14 为 I2C/复位/时钟，pin16-pin29 承载五组 MIPI 差分对。

- 参数与网络：`reference=J1`；`part_number=FPC-SMD_30P-FH34SRJ-30S-0.5SH`；`unconnected_pins=1,2,3,4,5`；`ground_pins=6,10,15,18,21,24,27,30,SH`；`power_pins=7 DVDD_1V2, 8 DOVDD_1V8, 9 AVDD_2V8`；`control_pins=11 CAM_SDA_1V8, 12 CAM_SCL_1V8, 13 CAM_RSTN, 14 CAM_MCLK`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 5A-6B，J1 pin1-pin30 和 SH 的完整网络标注

## 总线

### SC850SL 1.8V I2C 控制总线

U1C SDA pin C1 连接 CAM_SDA_1V8，SCL pin B3 连接 CAM_SCL_1V8，并分别引到 J1 pin11 和 pin12。

- 参数与网络：`sensor=U1 SC850SL`；`sda_sensor_pin=C1`；`sda_net=CAM_SDA_1V8`；`sda_connector_pin=11`；`scl_sensor_pin=B3`；`scl_net=CAM_SCL_1V8`；`scl_connector_pin=12`；`io_voltage=1.8V`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1C-2C U1C SDA/SCL 与网格 5A-6B J1 pin11/pin12

### MIPI CSI 差分时钟通道

U1D M0CP/M0CN 形成 MIPI_RX2_P/N，并连接 J1 pin23/pin22；该差分对位于四条数据通道之间的时钟位置。

- 参数与网络：`sensor_pair=M0CP/M0CN`；`nets=MIPI_RX2_P, MIPI_RX2_N`；`connector_positive_pin=23`；`connector_negative_pin=22`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1D-2D U1D M0CP/M0CN 到 MIPI_RX2_P/N，网格 5A-6A J1 pin22/pin23

### 四条 MIPI CSI 数据通道

U1D M0D0、M0D1、M0D2、M0D3 四组差分输出分别映射到 MIPI_RX0、MIPI_RX1、MIPI_RX3、MIPI_RX4，并连接 J1 pin16/17、19/20、25/26、28/29。

- 参数与网络：`lane0=M0D0P/N -> MIPI_RX0_P/N -> J1 17/16`；`lane1=M0D1P/N -> MIPI_RX1_P/N -> J1 20/19`；`lane2=M0D2P/N -> MIPI_RX3_P/N -> J1 26/25`；`lane3=M0D3P/N -> MIPI_RX4_P/N -> J1 29/28`；`data_lane_count=4`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1D-2D U1D M0D0-M0D3 网络与网格 5A-6A J1 MIPI_RX0/RX1/RX3/RX4 引脚

## 总线地址

### SC850SL SID 配置

U1C SID pin D10 通过 R3 0Ω 固定连接 GND；原理图未标注该配置对应的数值 I2C 地址。

- 参数与网络：`sensor_pin=D10 SID`；`strap=GND`；`resistor=R3 0Ω`；`numeric_i2c_address=null`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1C-2C，U1C SID pin D10、R3 0R/1% 和 GND

## GPIO 与控制信号

### SC850SL 未使用同步与 GPIO 引脚

U1C EFSYNC pin C2、FSYNC pin C3 和 GPIO2 pin D1 均在原理图中标记为未连接。

- 参数与网络：`unconnected_pins=C2 EFSYNC, C3 FSYNC, D1 GPIO2`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1C-2C，U1C EFSYNC、FSYNC、GPIO2 网络末端的未连接标记

## 时钟

### SC850SL 外部主时钟

U1C EXTCLK pin B4 连接 CAM_MCLK，并引到 J1 pin14。

- 参数与网络：`sensor_pin=B4 EXTCLK`；`net=CAM_MCLK`；`connector_pin=14`；`frequency=null`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1C-2C U1C EXTCLK/CAM_MCLK 与网格 5A-6B J1 pin14

## 复位

### SC850SL 硬件复位

U1C XSHUTDN pin B2 连接 CAM_RSTN，并引到 J1 pin13。

- 参数与网络：`sensor_pin=B2 XSHUTDN`；`net=CAM_RSTN`；`connector_pin=13`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1C-2C U1C XSHUTDN/CAM_RSTN 与网格 5A-6B J1 pin13

## 模拟电路

### SC850SL 参考与内部电源去耦

U1B VREFH、VREFN2、VREFN、VREF3 和 TXVDD 分别通过 C5、C6、C7、C8、C9 的 1uF 电容接地。

- 参数与网络：`vrefh=C5 1uF`；`vrefn2=C6 1uF`；`vrefn=C7 1uF`；`vref3=C8 1uF`；`txvdd=C9 1uF`
- 证据：图 9efa49abd81c / 第 1 页 / 网格 1B-2B，U1B 与 C5-C9

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | SC850SL 摄像头模组架构 | `sensor=U1 SC850SL`；`connector=J1 30P FPC`；`power_domains=AVDD_2V8, DOVDD_1V8, DVDD_1V3`；`control=CAM_SDA_1V8, CAM_SCL_1V8, CAM_RSTN, CAM_MCLK`；`mipi_data_lanes=4` |
| 电源 | SC850SL 模拟电源 AVDD_2V8 | `net=AVDD_2V8`；`sensor_pins=A2,A4,A7,A9,E1,E6,E10`；`connector_pin=9`；`domain=analog` |
| 电源 | SC850SL I/O 电源 DOVDD_1V8 | `net=DOVDD_1V8`；`sensor_pins=A5,C4,C7,E2,E5,E9`；`connector_pin=8`；`domain=digital_io` |
| 电源 | SC850SL 核心电源 DVDD_1V3 | `net=DVDD_1V3`；`sensor_pins=B1,B10,D2,D3,D4,D7,D8,D9`；`regulator=U2 TPS7A9101DSK`；`regulator_input=DOVDD_1V8` |
| 电源 | TPS7A9101DSK 配置 | `reference=U2`；`input=DOVDD_1V8`；`output=DVDD_1V3`；`feedback_upper=R1 7.5kΩ`；`feedback_lower=R2 12kΩ`；`feedforward_capacitor=C1 10nF`；`nr_ss_capacitor=C2 100nF`；`power_good=NC` |
| 总线 | SC850SL 1.8V I2C 控制总线 | `sensor=U1 SC850SL`；`sda_sensor_pin=C1`；`sda_net=CAM_SDA_1V8`；`sda_connector_pin=11`；`scl_sensor_pin=B3`；`scl_net=CAM_SCL_1V8`；`scl_connector_pin=12`；`io_voltage=1.8V` |
| 复位 | SC850SL 硬件复位 | `sensor_pin=B2 XSHUTDN`；`net=CAM_RSTN`；`connector_pin=13` |
| 时钟 | SC850SL 外部主时钟 | `sensor_pin=B4 EXTCLK`；`net=CAM_MCLK`；`connector_pin=14`；`frequency=null` |
| 总线地址 | SC850SL SID 配置 | `sensor_pin=D10 SID`；`strap=GND`；`resistor=R3 0Ω`；`numeric_i2c_address=null` |
| 总线 | MIPI CSI 差分时钟通道 | `sensor_pair=M0CP/M0CN`；`nets=MIPI_RX2_P, MIPI_RX2_N`；`connector_positive_pin=23`；`connector_negative_pin=22` |
| 总线 | 四条 MIPI CSI 数据通道 | `lane0=M0D0P/N -> MIPI_RX0_P/N -> J1 17/16`；`lane1=M0D1P/N -> MIPI_RX1_P/N -> J1 20/19`；`lane2=M0D2P/N -> MIPI_RX3_P/N -> J1 26/25`；`lane3=M0D3P/N -> MIPI_RX4_P/N -> J1 29/28`；`data_lane_count=4` |
| 接口 | J1 30 针 FPC 接口 | `reference=J1`；`part_number=FPC-SMD_30P-FH34SRJ-30S-0.5SH`；`unconnected_pins=1,2,3,4,5`；`ground_pins=6,10,15,18,21,24,27,30,SH`；`power_pins=7 DVDD_1V2, 8 DOVDD_1V8, 9 AVDD_2V8`；`control_pins=11 CAM_SDA_1V8, 12 CAM_SCL_1V8, 13 CAM_RSTN, 14 CAM_MCLK` |
| 核心器件 | SC850SL M1 差分接口 | `sensor_section=U1E`；`unused_pairs=M1CP/M1CN, M1D0P/N, M1D1P/N, M1D2P/N, M1D3P/N` |
| GPIO 与控制信号 | SC850SL 未使用同步与 GPIO 引脚 | `unconnected_pins=C2 EFSYNC, C3 FSYNC, D1 GPIO2` |
| 模拟电路 | SC850SL 参考与内部电源去耦 | `vrefh=C5 1uF`；`vrefn2=C6 1uF`；`vrefn=C7 1uF`；`vref3=C8 1uF`；`txvdd=C9 1uF` |
| 电源 | 三路传感器电源去耦 | `avdd_2v8=C10-C13 1uF, C14-C18 100nF, C19 10uF`；`dovdd_1v8=C20-C22 1uF, C23-C27 100nF, C28 10uF`；`dvdd_1v3=C29-C32 1uF, C33-C37 100nF, C38 10uF` |
| 电源 | J1 DVDD_1V2 引脚用途 | `connector_pin=7`；`connector_net=DVDD_1V2`；`sensor_core_net=DVDD_1V3`；`visible_connection_between_nets=false` |

## 待确认事项

- `power.connector-dvdd-1v2`：J1 pin7 标记为 DVDD_1V2，但图中 SC850SL 核心 DVDD 使用 U2 生成的 DVDD_1V3，原理图未显示 DVDD_1V2 与任何其他器件或网络的连接。（证据：图 9efa49abd81c / 第 1 页 / 网格 5A-6B J1 pin7 DVDD_1V2，与网格 1A-4A U1 DVDD_1V3 和 U2 DVDD_1V3 输出）
- `review.connector-dvdd-1v2`：J1 pin7 的 DVDD_1V2 是否为未使用预留，或应与传感器 DVDD_1V3 电源域存在未画出的连接？；原因：连接器标注 DVDD_1V2，而 SC850SL 核心电源和 U2 输出均标注 DVDD_1V3，当前原理图未显示两者关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9efa49abd81cc9c081eacf982273c1933baed00977dd86c2858fd35a1e0f1797` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/K157-CamModule-SC850SL_page_01.png` |

---

源文档：`zh_CN/accessory/CamModule_SC850SL.md`

源文档 SHA-256：`6aa8b7bc96b668b6294e74790a2728badfa484299704987255af99428e5fa491`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
