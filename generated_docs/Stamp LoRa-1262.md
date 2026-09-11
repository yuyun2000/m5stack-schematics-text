# Stamp LoRa-1262 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp LoRa-1262 |
| SKU | S014 |
| 产品 ID | `stamp-lora-1262-f672554cdfb9` |
| 源文档 | `zh_CN/stamp/Stamp_LoRa-1262.md` |

## 概述

该单页器件级原理图以 U1 SX1262 为收发核心，主机侧通过 SPI_MISO、SPI_MOSI、SPI_CLK、SX_NSS 以及 LORA_IRQ、SX_BUSY、SX_NRST 与 J2 引出连接。U3 0900FM15K0039 位于 SX1262 的差分接收端和单端收发路径之间，U2 FM8625H 由 SX_DIO2 控制，在 SX_SRFI、SX_SRFO 与公共 RFC 天线通道之间切换。VIN_3V3 经 FB2 形成 VDD_3V3，X1 由 VDD_OCXO 供电并连接 SX_32M_REF；J1、J2 及多处射频器件在图面值字段中标为 NC 或 TBD，实际装配需按具体 SKU 确认。

## 检索关键词

`Stamp LoRa-1262`、`S014`、`LoRa`、`SX1262`、`0900FM15K0039`、`FM8625H`、`X1G0041310042`、`SPI_MISO`、`SPI_MOSI`、`SPI_CLK`、`SX_NSS`、`LORA_IRQ`、`SX_BUSY`、`SX_NRST`、`SX_DIO2`、`SX_DIO3`、`SX_32M_REF`、`SX_RFO`、`SX_RFI_P`、`SX_RFI_N`、`SX_SRFI`、`SX_SRFO`、`SX_ANT_SW`、`RF_50R`、`RF_PAD`、`VIN_3V3`、`VDD_3V3`、`VDD_OCXO`、`SX_VREG`、`SX_PAVDD`、`J1`、`J2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SX1262 | LoRa 射频收发核心，连接主机 SPI/控制信号、差分接收端、单端发射端及多个电源域。 | 图 33b8e69d7e7a / 第 1 页 / 页1左上 A1-A2，U1 方框下方标注 SX1262，符号两侧列出电源、SPI、DIO 与 RF 引脚。 |
| U3 | 0900FM15K0039 | 连接 U1 差分接收端与单端收发网络的射频前端器件。 | 图 33b8e69d7e7a / 第 1 页 / 页1上部 A3，U3 下方标注 0900FM15K0039，端口为 RFO、RFI_P、RFI_N、SW_RFI、SW_RFO。 |
| U2 | FM8625H | 在 SX_SRFI、SX_SRFO 与公共 RFC 天线通道之间进行选择的射频开关。 | 图 33b8e69d7e7a / 第 1 页 / 页1上部 A5-A6，U2 下方标注 FM8625H，符号引脚标为 RF2、RF1、RFC、VDD、CTRL、GND。 |
| X1 | X1G0041310042 | 由 VDD_OCXO 供电、经 R3/C6 向 SX_32M_REF 输出的有源参考时钟器件。 | 图 33b8e69d7e7a / 第 1 页 / 页1中左 B2-B3，X1 上方标注 X1G0041310042 和 VDD: 3.0V，3 脚经 R3、C6 接 SX_32M_REF。 |
| J2 | NC | 12 针主机接口焊盘/连接器，图面值字段标为 NC，仍明确给出电源、SPI、复位、中断和状态网络映射。 | 图 33b8e69d7e7a / 第 1 页 / 页1左下 C1-C2，J2 为 PIN1 至 PIN12，符号下方标注 NC。 |
| J1 | NC | 两针射频连接器焊盘，1 脚接 RF_50R、2 脚接 GND，图面值字段标为 NC。 | 图 33b8e69d7e7a / 第 1 页 / 页1右上 A8，J1 符号上方标注 NC，1 脚位于 RF_50R 水平网络，2 脚下接 GND。 |
| FB2 | BLM15AX601SN1D | VIN_3V3 与 VDD_3V3 之间的串联磁珠。 | 图 33b8e69d7e7a / 第 1 页 / 页1左中 B1-C1，FB2 旁标注 BLM15AX601SN1D，上端为 VIN_3V3，下端进入 VDD_3V3 去耦母线。 |
| FB1 | 600R/0201 | SX_DIO3 与 VDD_OCXO 之间的串联滤波器件。 | 图 33b8e69d7e7a / 第 1 页 / 页1中左 B1-B2，FB1 串接在 SX_DIO3 与 VDD_OCXO 之间，值标注 600R/0201。 |
| L1 | LQW15AN47NJ00D/47nH/HQ | 连接 SX_PAVDD 与 SX_RFO 节点的射频电感。 | 图 33b8e69d7e7a / 第 1 页 / 页1上部 A3，L1 竖接于 SX_PAVDD 与 SX_RFO 节点之间，旁注 LQW15AN47NJ00D/47nH/HQ。 |
| L3 | NC | U1 DCC_SW 与 SX_VREG 节点之间、图面值字段标为 NC 的电感焊盘。 | 图 33b8e69d7e7a / 第 1 页 / 页1左上 A1-A2，L3 位于 U1 左侧 VREG/DCC_SW 支路，器件值标注 NC。 |
| L4 | 0R/TBD | 从 C1 后射频节点串接至 RF_PAD 的跳线/匹配位置，图面值标注 0R/TBD。 | 图 33b8e69d7e7a / 第 1 页 / 页1右上 A7，L4 从 C1 后节点向上分支至 RF_PAD，值标注 0R/TBD。 |
| R1, C4 | 未标注 | U2 VDD 支路的 100R/1% 串联电阻和 100pF/25V 对地电容。 | 图 33b8e69d7e7a / 第 1 页 / 页1上部 A5，SX_ANT_SW 经 R1 100R/1% 到 U2 VDD，R1 后节点由 C4 100pF/25V 接地。 |
| R2, C5 | 未标注 | U2 CTRL 支路的 100R/1% 串联电阻和 100pF/25V 对地电容。 | 图 33b8e69d7e7a / 第 1 页 / 页1上部 A6，U2 CTRL 经 R2 100R/1% 接 SX_DIO2，CTRL 节点由 C5 100pF/25V 接地。 |
| C1, L2, C2, C3 | 未标注 | U2 RFC 后的串联/并联射频匹配网络；L2、C2、C3 在图面值字段中标为 NC。 | 图 33b8e69d7e7a / 第 1 页 / 页1右上 A6-A7，RFC 水平通道依次经过 C1 和 L2，C2/C3 分别从相邻节点对地；L2、C2、C3 均标 NC。 |
| D1 | NC | RF_50R 至 GND 的并联二极管焊盘，图面值字段标为 NC。 | 图 33b8e69d7e7a / 第 1 页 / 页1右上 A7-A8，D1 从 RF_50R 节点并联至 GND，器件值标注 NC。 |
| C7-C9 | 未标注 | SX_DIO3/VDD_OCXO 电源支路的对地滤波电容组。 | 图 33b8e69d7e7a / 第 1 页 / 页1中左 B1-B2，C7 位于 FB1 前，C8/C9 位于 VDD_OCXO 侧，三者均接 GND。 |
| C10-C18 | 未标注 | VDD_3V3、SX_VREG 和 SX_PAVDD 电源轨的分组去耦电容。 | 图 33b8e69d7e7a / 第 1 页 / 页1中左 B1-C3，C18/C10-C14 接 VDD_3V3，C15 接 SX_VREG，C16/C17 接 SX_PAVDD。 |

## 系统结构

### Stamp LoRa-1262 原理图架构

第 1 页画出以 U1 SX1262 为核心、由 U3 射频前端和 U2 射频开关连接天线输出，并通过 J2 引出主机接口的单页电路。

- 参数与网络：`transceiver=U1 SX1262`；`rf_front_end=U3 0900FM15K0039`；`rf_switch=U2 FM8625H`；`clock_source=X1 X1G0041310042`；`host_interface=J2`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1整页；A1-A8 为收发及 RF 通道，B1-B3 为时钟/供电，C1-C2 为 J2 主机引出。

## 核心器件

### U1

U1 的器件型号在图面中标为 SX1262。

- 参数与网络：`reference=U1`；`part_number=SX1262`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1左上 A1-A2，U1 符号下方型号文字 SX1262。

### U3

U3 的器件型号在图面中标为 0900FM15K0039。

- 参数与网络：`reference=U3`；`part_number=0900FM15K0039`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1上部 A3，U3 符号下方型号文字 0900FM15K0039。

### U2

U2 的器件型号在图面中标为 FM8625H。

- 参数与网络：`reference=U2`；`part_number=FM8625H`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1上部 A5-A6，U2 符号下方型号文字 FM8625H。

## 电源

### U1 3.3 V 与接地连接

U1 VDD_IN 1 脚、VBAT 10 脚和 VBAT_IO 11 脚连接 VDD_3V3，GND 2/5/8/20/25 脚连接 GND。

- 参数与网络：`supply_pins=VDD_IN pin 1; VBAT pin 10; VBAT_IO pin 11`；`supply_net=VDD_3V3`；`ground_pins=2, 5, 8, 20, 25`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1左上 A1-A2，U1 左侧 VDD_IN/VBAT/VBAT_IO 与下部 GND 引脚连接。

### SX_VREG 电源节点

U1 VREG 7 脚连接 SX_VREG，SX_VREG 由 C15 1uF/10V 对地；L3 位于 SX_VREG 与 U1 DCC_SW 9 脚之间且值字段标为 NC。

- 参数与网络：`vreg_pin=U1 pin 7`；`net=SX_VREG`；`decoupling=C15 1uF/10V to GND`；`dcc_path=L3 NC -> U1 DCC_SW pin 9`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A1-A2 的 U1 VREG/DCC_SW/L3 支路及 B3 的 SX_VREG-C15 去耦。

### SX_PAVDD 电源节点

U1 VR_PA 24 脚连接 SX_PAVDD，SX_PAVDD 由 C16 47nF/25V 和 C17 47pF/25V 对地，并经 L1 接至 SX_RFO 节点。

- 参数与网络：`u1_pin=VR_PA pin 24`；`net=SX_PAVDD`；`decoupling=C16 47nF/25V; C17 47pF/25V`；`rf_feed=L1 LQW15AN47NJ00D/47nH/HQ -> SX_RFO`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2-A3 的 VR_PA/SX_PAVDD/L1 与 B3 的 C16/C17 去耦支路。

### U2 VDD 供电支路

SX_ANT_SW 经 R1 100R/1% 接 U2 VDD 4 脚，R1 后的 VDD 节点由 C4 100pF/25V 对地。

- 参数与网络：`source_net=SX_ANT_SW`；`series_resistor=R1 100R/1%`；`switch_pin=U2 VDD pin 4`；`shunt_capacitor=C4 100pF/25V to GND`；`connector_pin=J2 pin 3`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A5 的 SX_ANT_SW-R1-C4-U2 VDD 支路；C1-C2 的 J2 pin 3 标注 SX_ANT_SW。

### 3.3 V 输入滤波

VIN_3V3 经 FB2 BLM15AX601SN1D 串联后形成 VDD_3V3，VIN_3V3 同时连接 J2 的 1、2 脚。

- 参数与网络：`input_net=VIN_3V3`；`filter=FB2 BLM15AX601SN1D`；`output_net=VDD_3V3`；`connector_pins=J2 pins 1 and 2`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 B1-C2，VIN_3V3-FB2-VDD_3V3 支路及 J2 pin 1/2。

### VDD_3V3 去耦

VDD_3V3 母线由 C18、C10、C11、C12、C13、C14 对地去耦，图面值依次为 10uF/10V、10uF/10V、1uF/10V、1uF/10V、100nF/25V、100nF/25V。

- 参数与网络：`bulk=C18 10uF/10V; C10 10uF/10V`；`mid_value=C11 1uF/10V; C12 1uF/10V`；`high_frequency=C13 100nF/25V; C14 100nF/25V`；`rail=VDD_3V3`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 B1-C3，FB2 后水平电源母线上的 C18、C10-C14 与 VDD_3V3 标签。

### VDD_OCXO 滤波支路

SX_DIO3 一侧由 C7 100nF/25V 对地，经 FB1 600R/0201 后形成 VDD_OCXO；VDD_OCXO 由 C8 100nF/25V 和 C9 10nF/25V 对地。

- 参数与网络：`source_net=SX_DIO3`；`pre_filter=C7 100nF/25V to GND`；`series_filter=FB1 600R/0201`；`output_net=VDD_OCXO`；`post_filter=C8 100nF/25V; C9 10nF/25V to GND`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1中左 B1-B2，SX_DIO3-C7-FB1-VDD_OCXO-C8/C9 完整支路。

## 接口

### J2 12 针接口

J2 的 1/2 脚同接 VIN_3V3，3 至 6 脚依次接 SX_ANT_SW、LORA_IRQ、SX_BUSY、SX_NRST，7/11 脚接 GND，8/9/10/12 脚依次接 SPI_MISO、SPI_MOSI、SX_NSS、SPI_CLK。

- 参数与网络：`pin_1=VIN_3V3`；`pin_2=VIN_3V3`；`pin_3=SX_ANT_SW`；`pin_4=LORA_IRQ`；`pin_5=SX_BUSY`；`pin_6=SX_NRST`；`pin_7=GND`；`pin_8=SPI_MISO`；`pin_9=SPI_MOSI`；`pin_10=SX_NSS`；`pin_11=GND`；`pin_12=SPI_CLK`；`value_marking=NC`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1左下 C1-C2，J2 PIN1-PIN12 右侧逐脚网络标签及 pin 1/2 汇合连接。

### J1 射频连接器焊盘

J1 1 脚连接 RF_50R，2 脚连接 GND，J1 的图面值字段标为 NC。

- 参数与网络：`pin_1=RF_50R`；`pin_2=GND`；`value_marking=NC`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1右上 A8，J1 两针连接与 NC 标注。

## 总线

### SX1262 主机 SPI

U1 的 MISO、MOSI、SCK、NSS 分别连接 SPI_MISO、SPI_MOSI、SPI_CLK、SX_NSS，并分别引至 J2 的 8、9、12、10 脚。

- 参数与网络：`u1_miso=pin 16 -> SPI_MISO -> J2 pin 8`；`u1_mosi=pin 17 -> SPI_MOSI -> J2 pin 9`；`u1_sck=pin 18 -> SPI_CLK -> J2 pin 12`；`u1_nss=pin 19 -> SX_NSS -> J2 pin 10`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2 的 U1 右侧 SPI 引脚与 C1-C2 的 J2 pin 8/9/10/12 网络标签逐名对应。

## GPIO 与控制信号

### SX1262 中断与忙状态

U1 DIO1 13 脚连接 LORA_IRQ 并引至 J2 4 脚；U1 BUSY 14 脚连接 SX_BUSY 并引至 J2 5 脚。

- 参数与网络：`irq=U1 DIO1 pin 13 -> LORA_IRQ -> J2 pin 4`；`busy=U1 BUSY pin 14 -> SX_BUSY -> J2 pin 5`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2 的 U1 DIO1/BUSY 网络与 C1-C2 的 J2 pin 4/5 标签。

### U2 CTRL 控制

U1 DIO2 12 脚连接 SX_DIO2；SX_DIO2 经 R2 100R/1% 接 U2 CTRL 6 脚，CTRL 节点由 C5 100pF/25V 对地。

- 参数与网络：`source=U1 DIO2 pin 12`；`net=SX_DIO2`；`series_resistor=R2 100R/1%`；`switch_pin=U2 CTRL pin 6`；`shunt_capacitor=C5 100pF/25V to GND`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2 的 U1 DIO2/SX_DIO2 与 A6 的 R2-C5-U2 CTRL 支路。

### U1 DIO2

U1 DIO2 12 脚网络名为 SX_DIO2，该网络经 R2 接 U2 CTRL。

- 参数与网络：`u1_pin=DIO2 pin 12`；`net=SX_DIO2`；`destination=R2 -> U2 CTRL pin 6`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2 与 A6，U1 DIO2/SX_DIO2 及 R2-U2 CTRL 同名网络。

### U1 DIO3

U1 DIO3 6 脚网络名为 SX_DIO3，该网络连接 C7 并经 FB1 进入 VDD_OCXO 支路。

- 参数与网络：`u1_pin=DIO3 pin 6`；`net=SX_DIO3`；`destination=C7 and FB1 -> VDD_OCXO`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2 与 B1-B2，U1 DIO3/SX_DIO3 及同名 OCXO 滤波支路。

## 时钟

### X1 参考时钟链路

X1 4 脚接 VDD_OCXO、2 脚接 GND、1 脚画有无连接标记，3 脚输出经 R3 220R/1% 与 C6 10nF/10% 串联后连接 SX_32M_REF；图面另标注 VDD: 3.0V。

- 参数与网络：`part_number=X1G0041310042`；`supply=pin 4 VDD_OCXO`；`ground=pin 2 GND`；`no_connect=pin 1`；`output=pin 3 -> R3 220R/1% -> C6 10nF/10% -> SX_32M_REF`；`voltage_note=VDD: 3.0V`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1中左 B2-B3，X1 四脚符号、VDD: 3.0V 注记及 R3/C6/SX_32M_REF 输出链。

### U1 时钟输入

SX_32M_REF 连接 U1 XTA 3 脚，U1 XTB 4 脚画有无连接标记。

- 参数与网络：`clock_net=SX_32M_REF`；`input_pin=U1 XTA pin 3`；`no_connect_pin=U1 XTB pin 4`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1左上 A1-A2，U1 XTA/XTB 引脚及 SX_32M_REF 标签、XTB 无连接标记。

## 复位

### SX1262 复位

U1 NRESET 15 脚连接 SX_NRST，SX_NRST 同时引至 J2 6 脚。

- 参数与网络：`u1_pin=NRESET pin 15`；`net=SX_NRST`；`connector_pin=J2 pin 6`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A1-A2 的 U1 NRESET/SX_NRST 与 C1-C2 的 J2 pin 6。

## 关键网络

### RF_50R 标注

原理图在 U1/U3/U2 收发路径及 U2 RFC 后天线通道的多个节点旁重复标注 RF_50R。

- 参数与网络：`annotation=RF_50R`；`locations=SX_RFO; SX_RFI_P/N; SX_SRFI; SX_SRFO; U2 RFC/C1; L2/J1 path`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1上部 A2-A8，各 RF 通道旁的红色 RF_50R 信息标注。

## 射频

### U1 射频端口

U1 RFO 23 脚连接 SX_RFO，RFI_P 21 脚连接 SX_RFI_P，RFI_N 22 脚连接 SX_RFI_N。

- 参数与网络：`tx=RFO pin 23 -> SX_RFO`；`rx_positive=RFI_P pin 21 -> SX_RFI_P`；`rx_negative=RFI_N pin 22 -> SX_RFI_N`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1左上 A2，U1 右上侧 RFO、RFI_P、RFI_N 引脚及相邻网络标签。

### 射频发射通道

U1 RFO 23 脚通过 SX_RFO 接 U3 RFO 1 脚，U3 SW_RFO 8 脚通过 SX_SRFO 接 U2 RF2 1 脚。

- 参数与网络：`path=U1 RFO pin 23 -> SX_RFO -> U3 RFO pin 1 -> U3 SW_RFO pin 8 -> SX_SRFO -> U2 RF2 pin 1`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2-A6，沿 SX_RFO 与 SX_SRFO 标签从 U1 经 U3 至 U2。

### 射频接收通道

U2 RF1 3 脚通过 SX_SRFI 接 U3 SW_RFI 6 脚，U3 RFI_P 4 脚和 RFI_N 3 脚再分别通过 SX_RFI_P、SX_RFI_N 接 U1 的 21、22 脚。

- 参数与网络：`single_ended=U2 RF1 pin 3 -> SX_SRFI -> U3 SW_RFI pin 6`；`differential_positive=U3 RFI_P pin 4 -> SX_RFI_P -> U1 RFI_P pin 21`；`differential_negative=U3 RFI_N pin 3 -> SX_RFI_N -> U1 RFI_N pin 22`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A2-A6，沿 SX_SRFI、SX_RFI_P、SX_RFI_N 标签核对 U2、U3、U1 引脚。

### L1 射频供电支路

L1 竖接于 SX_PAVDD 与 SX_RFO 节点之间，图面标注 LQW15AN47NJ00D/47nH/HQ。

- 参数与网络：`reference=L1`；`marking=LQW15AN47NJ00D/47nH/HQ`；`from=SX_PAVDD`；`to=SX_RFO`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1上部 A3，L1 上端 SX_PAVDD、下端/节点 SX_RFO。

### U2 射频端口映射

U2 RF2 1 脚接 SX_SRFO，RF1 3 脚接 SX_SRFI，公共端 RFC 5 脚接后级天线匹配通道。

- 参数与网络：`rf2=pin 1 -> SX_SRFO`；`rf1=pin 3 -> SX_SRFI`；`common=RFC pin 5 -> RF_50R/C1 antenna path`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A5-A6，U2 左侧 RF2/RF1 网络标签与右侧 RFC 水平通道。

### RF_PAD 输出路径

U2 RFC 5 脚经标注 RF_50R 的通道和串联 C1 到达分支节点，该节点再经 L4 接 RF_PAD；L4 的图面值为 0R/TBD。

- 参数与网络：`path=U2 RFC pin 5 -> RF_50R -> C1 -> L4 -> RF_PAD`；`l4_marking=0R/TBD`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1右上 A6-A7，从 U2 RFC 沿 C1 至 L4/RF_PAD 分支。

### J1 可选射频通道

C1 后节点还通过 L2 到达 J1 1 脚所在 RF_50R 节点，C2、C3 与 D1 分别从相关节点对地；L2、C2、C3、D1 和 J1 的值字段均标为 NC。

- 参数与网络：`series_element=L2 NC`；`shunt_elements=C2 NC; C3 NC; D1 NC`；`connector=J1 NC`；`connector_signal=J1 pin 1 RF_50R`；`connector_ground=J1 pin 2 GND`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1右上 A7-A8，C1 后的 L2/C2/C3/D1/J1 支路及各 NC 标注。

## 其他事实

### NC 与 TBD 图面标记

图面值字段将 L3、L2、C2、C3、D1、J1、J2 标为 NC，并将 L4 标为 0R/TBD；这些标记不能作为已装配器件值使用。

- 参数与网络：`nc_references=L3, L2, C2, C3, D1, J1, J2`；`tbd_reference=L4 0R/TBD`
- 证据：图 33b8e69d7e7a / 第 1 页 / 页1 A1-A8 与 C1-C2，逐项核对 L3、L2、C2、C3、D1、J1、J2 的 NC 和 L4 的 0R/TBD 标注。

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp LoRa-1262 原理图架构 | `transceiver=U1 SX1262`；`rf_front_end=U3 0900FM15K0039`；`rf_switch=U2 FM8625H`；`clock_source=X1 X1G0041310042`；`host_interface=J2` |
| 核心器件 | U1 | `reference=U1`；`part_number=SX1262` |
| 总线 | SX1262 主机 SPI | `u1_miso=pin 16 -> SPI_MISO -> J2 pin 8`；`u1_mosi=pin 17 -> SPI_MOSI -> J2 pin 9`；`u1_sck=pin 18 -> SPI_CLK -> J2 pin 12`；`u1_nss=pin 19 -> SX_NSS -> J2 pin 10` |
| 接口 | J2 12 针接口 | `pin_1=VIN_3V3`；`pin_2=VIN_3V3`；`pin_3=SX_ANT_SW`；`pin_4=LORA_IRQ`；`pin_5=SX_BUSY`；`pin_6=SX_NRST`；`pin_7=GND`；`pin_8=SPI_MISO`；`pin_9=SPI_MOSI`；`pin_10=SX_NSS`；`pin_11=GND`；`pin_12=SPI_CLK`；`value_marking=NC` |
| GPIO 与控制信号 | SX1262 中断与忙状态 | `irq=U1 DIO1 pin 13 -> LORA_IRQ -> J2 pin 4`；`busy=U1 BUSY pin 14 -> SX_BUSY -> J2 pin 5` |
| 复位 | SX1262 复位 | `u1_pin=NRESET pin 15`；`net=SX_NRST`；`connector_pin=J2 pin 6` |
| 射频 | U1 射频端口 | `tx=RFO pin 23 -> SX_RFO`；`rx_positive=RFI_P pin 21 -> SX_RFI_P`；`rx_negative=RFI_N pin 22 -> SX_RFI_N` |
| 电源 | U1 3.3 V 与接地连接 | `supply_pins=VDD_IN pin 1; VBAT pin 10; VBAT_IO pin 11`；`supply_net=VDD_3V3`；`ground_pins=2, 5, 8, 20, 25` |
| 电源 | SX_VREG 电源节点 | `vreg_pin=U1 pin 7`；`net=SX_VREG`；`decoupling=C15 1uF/10V to GND`；`dcc_path=L3 NC -> U1 DCC_SW pin 9` |
| 电源 | SX_PAVDD 电源节点 | `u1_pin=VR_PA pin 24`；`net=SX_PAVDD`；`decoupling=C16 47nF/25V; C17 47pF/25V`；`rf_feed=L1 LQW15AN47NJ00D/47nH/HQ -> SX_RFO` |
| 核心器件 | U3 | `reference=U3`；`part_number=0900FM15K0039` |
| 射频 | 射频发射通道 | `path=U1 RFO pin 23 -> SX_RFO -> U3 RFO pin 1 -> U3 SW_RFO pin 8 -> SX_SRFO -> U2 RF2 pin 1` |
| 射频 | 射频接收通道 | `single_ended=U2 RF1 pin 3 -> SX_SRFI -> U3 SW_RFI pin 6`；`differential_positive=U3 RFI_P pin 4 -> SX_RFI_P -> U1 RFI_P pin 21`；`differential_negative=U3 RFI_N pin 3 -> SX_RFI_N -> U1 RFI_N pin 22` |
| 射频 | L1 射频供电支路 | `reference=L1`；`marking=LQW15AN47NJ00D/47nH/HQ`；`from=SX_PAVDD`；`to=SX_RFO` |
| 核心器件 | U2 | `reference=U2`；`part_number=FM8625H` |
| 射频 | U2 射频端口映射 | `rf2=pin 1 -> SX_SRFO`；`rf1=pin 3 -> SX_SRFI`；`common=RFC pin 5 -> RF_50R/C1 antenna path` |
| GPIO 与控制信号 | U2 CTRL 控制 | `source=U1 DIO2 pin 12`；`net=SX_DIO2`；`series_resistor=R2 100R/1%`；`switch_pin=U2 CTRL pin 6`；`shunt_capacitor=C5 100pF/25V to GND` |
| 电源 | U2 VDD 供电支路 | `source_net=SX_ANT_SW`；`series_resistor=R1 100R/1%`；`switch_pin=U2 VDD pin 4`；`shunt_capacitor=C4 100pF/25V to GND`；`connector_pin=J2 pin 3` |
| 射频 | RF_PAD 输出路径 | `path=U2 RFC pin 5 -> RF_50R -> C1 -> L4 -> RF_PAD`；`l4_marking=0R/TBD` |
| 射频 | J1 可选射频通道 | `series_element=L2 NC`；`shunt_elements=C2 NC; C3 NC; D1 NC`；`connector=J1 NC`；`connector_signal=J1 pin 1 RF_50R`；`connector_ground=J1 pin 2 GND` |
| 接口 | J1 射频连接器焊盘 | `pin_1=RF_50R`；`pin_2=GND`；`value_marking=NC` |
| 关键网络 | RF_50R 标注 | `annotation=RF_50R`；`locations=SX_RFO; SX_RFI_P/N; SX_SRFI; SX_SRFO; U2 RFC/C1; L2/J1 path` |
| 电源 | 3.3 V 输入滤波 | `input_net=VIN_3V3`；`filter=FB2 BLM15AX601SN1D`；`output_net=VDD_3V3`；`connector_pins=J2 pins 1 and 2` |
| 电源 | VDD_3V3 去耦 | `bulk=C18 10uF/10V; C10 10uF/10V`；`mid_value=C11 1uF/10V; C12 1uF/10V`；`high_frequency=C13 100nF/25V; C14 100nF/25V`；`rail=VDD_3V3` |
| 电源 | VDD_OCXO 滤波支路 | `source_net=SX_DIO3`；`pre_filter=C7 100nF/25V to GND`；`series_filter=FB1 600R/0201`；`output_net=VDD_OCXO`；`post_filter=C8 100nF/25V; C9 10nF/25V to GND` |
| 时钟 | X1 参考时钟链路 | `part_number=X1G0041310042`；`supply=pin 4 VDD_OCXO`；`ground=pin 2 GND`；`no_connect=pin 1`；`output=pin 3 -> R3 220R/1% -> C6 10nF/10% -> SX_32M_REF`；`voltage_note=VDD: 3.0V` |
| 时钟 | U1 时钟输入 | `clock_net=SX_32M_REF`；`input_pin=U1 XTA pin 3`；`no_connect_pin=U1 XTB pin 4` |
| GPIO 与控制信号 | U1 DIO2 | `u1_pin=DIO2 pin 12`；`net=SX_DIO2`；`destination=R2 -> U2 CTRL pin 6` |
| GPIO 与控制信号 | U1 DIO3 | `u1_pin=DIO3 pin 6`；`net=SX_DIO3`；`destination=C7 and FB1 -> VDD_OCXO` |
| 其他事实 | NC 与 TBD 图面标记 | `nc_references=L3, L2, C2, C3, D1, J1, J2`；`tbd_reference=L4 0R/TBD` |
| 射频 | 工作频段 | `source_claim=868~923 MHz`；`schematic_marking=not shown` |
| 射频 | 调制与射频性能 | `modulation_claim=FSK/GFSK/MSK/GMSK/LoRa/OOK`；`bit_rate_claim=up to 300 kbps`；`tx_power_claim=+22 dBm`；`sensitivity_claim=-147 dBm`；`schematic_marking=not shown` |
| 接口 | S014/S014-I/S014-IF 装配差异 | `variants=S014; S014-I; S014-IF`；`schematic_connector_marking=J1 NC; J2 NC`；`direct_output=RF_PAD` |
| 射频 | L4 最终装配值 | `reference=L4`；`schematic_marking=0R/TBD`；`path=C1 output node -> RF_PAD` |

## 待确认事项

- `rf.operating_band`：源文档声明工作频段为 868~923 MHz，但第 1 页器件级原理图未直接标注工作频段或频段版本。（证据：图 33b8e69d7e7a / 第 1 页 / 页1整页；可见 SX1262、0900FM15K0039 与射频网络，但未见 868~923 MHz 频段文字。）
- `rf.performance_claims`：源文档给出 FSK/GFSK/MSK/GMSK/LoRa/OOK、最高 300 kbps、+22 dBm 与 -147 dBm 等规格，但这些性能值未在第 1 页原理图中标注。（证据：图 33b8e69d7e7a / 第 1 页 / 页1整页；图面提供器件、网络和无源值，未见调制、码率、发射功率或灵敏度参数表。）
- `interface.sku_population`：源文档描述 S014、S014-I、S014-IF 的天线座和 12 针接口装配差异；第 1 页仅画出 RF_PAD、J1、J2 并将 J1/J2 标为 NC，未给出三种 SKU 的分别装配表。（证据：图 33b8e69d7e7a / 第 1 页 / 页1 A7-A8 的 RF_PAD/J1 NC 与 C1-C2 的 J2 NC；图面未出现按 S014/S014-I/S014-IF 分列的装配说明。）
- `rf.l4_final_value`：L4 的图面值为 0R/TBD，因此该页不能确定量产装配时采用 0 欧姆还是后续确定的其他值。（证据：图 33b8e69d7e7a / 第 1 页 / 页1右上 A7，L4 旁明确标注 0R/TBD。）
- `review.rf.operating_band`：当前 S014 硬件版本的实际工作频段是否为 868~923 MHz，U3 与天线匹配料值是否覆盖该范围？；原因：频段来自源文档，原理图第 1 页未标注频段版本或射频验证范围。
- `review.rf.performance_claims`：调制方式、最高码率、发射功率和接收灵敏度应以哪一版器件规格与整机射频测试结果为准？；原因：这些数值属于源文档性能声明，器件级连接图无法直接证明。
- `review.interface.sku_population`：S014、S014-I、S014-IF 分别装配 J1、J2、L2/C2/C3/D1 和 RF_PAD/L4 路径中的哪些器件？；原因：原理图把 J1/J2 及多处射频器件标为 NC，未提供按 SKU 区分的 BOM 或装配选项表。
- `review.rf.l4_final_value`：L4 在当前量产版本中的最终装配值和物料号是什么？；原因：图面仅标注 0R/TBD，仍保留待定状态。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `33b8e69d7e7a687563509e02a330982de90bd05f9a50b88042629e265e39e3d6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1279/S014_Stamp_LoRa-1262_Sche_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp_LoRa-1262.md`

源文档 SHA-256：`372dedb6afbe4890df5bf31131eab920a8b41044575af7434a59e01545906dc3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
