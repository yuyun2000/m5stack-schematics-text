# Stamp UWB F 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp UWB F |
| SKU | S017-F |
| 产品 ID | `stamp-uwb-f-c5fdb11e08a9` |
| 源文档 | `zh_CN/stamp/Stamp_UWB_F.md` |

## 概述

该单页原理图以 U1（QM33120WTR13）为核心，画出了 SPI、唤醒、复位、中断、GPIO7、时钟和两路射频网络。U2（JW5712）由 VCC_3V3 生成 VCC_1V8，VCCA_3V3 则由 VCC_3V3 经 FB1 滤波得到。J1 与页内 PINMAP 给出 12 针电源、控制和 SPI 信号映射，但图面未标出 J1 的具体物理连接器型号，也未直接显示天线结构。

## 检索关键词

`Stamp UWB F`、`S017-F`、`QM33120WTR13`、`QM33120W`、`JW5712`、`VCC_3V3`、`VCCA_3V3`、`VCC_1V8`、`DW_EXTON`、`DW_WAKEUP`、`DW_RSTn`、`DW_IRQ`、`DW_CLK`、`DW_CDI`、`DW_CDO`、`DW_CSn`、`DW_GP7`、`DW_XTI`、`DW_XTO`、`DW_RF1`、`DW_RF2`、`DW_RF1_ANT`、`SPI`、`J1`、`PINMAP`、`12-pin`、`SX0B38.400F0810F30`、`FTC121065S2R2MBCA`、`GJM1555C1H2R0B`、`RF_50R`、`FB1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | QM33120WTR13 | UWB 收发器核心，连接 SPI、控制、时钟、供电和 RF1/RF2 网络 | 图 d8a1261888ed / 第 1 页 / 第1页 A1-B2，U1A 器件框底部标注 QM33120WTR13；第1页 D2 为 U1B 接地引脚单元 |
| U2 | JW5712 | 由 DW_EXTON 使能的 VCC_3V3 至 VCC_1V8 开关电源级 | 图 d8a1261888ed / 第 1 页 / 第1页 A3，U2 器件框底部标注 JW5712，周围可见 EN、VIN、SW、VOS、VSEL1/2/3 和 GND |
| J1 | 未标注 | 12 针外部连接器符号，引出电源、控制和 SPI 网络；图面未标具体连接器料号 | 图 d8a1261888ed / 第 1 页 / 第1页 D3，J1 符号列出 PIN1 至 PIN12；第1页 D4 PINMAP 给出对应网络 |
| X1 | SX0B38.400F0810F30 | 连接 U1 的 DW_XTI 与 DW_XTO 时钟网络，两端各接 3.3pF 对地电容 | 图 d8a1261888ed / 第 1 页 / 第1页 D1，X1 标注 SX0B38.400F0810F30，1/3 脚接 DW_XTI/DW_XTO，2/4 脚接 GND |
| L1 | FTC121065S2R2MBCA | U2 SW 输出至 VCC_1V8 的串联电感 | 图 d8a1261888ed / 第 1 页 / 第1页 A3-A4，L1 位于 U2 SW 与 VCC_1V8 之间，标注 FTC121065S2R2MBCA |
| FB1 | 600R@100MHz | VCC_3V3 至 VCCA_3V3 的串联磁珠 | 图 d8a1261888ed / 第 1 页 / 第1页 C1，FB1 串接 VCC_3V3 与 VCCA_3V3，标注 600R@100MHz |
| R1 | 10K/1% | DW_RSTn 至 VCC_3V3 的上拉电阻 | 图 d8a1261888ed / 第 1 页 / 第1页 A1-B1，R1 标注 10K/1%，上端接 VCC_3V3，下端接 DW_RSTn |
| R2 | 10K/1% | DW_IRQ 至 VCC_3V3 的上拉电阻 | 图 d8a1261888ed / 第 1 页 / 第1页 C1，R2 标注 10K/1%，上端接 VCC_3V3，下端接 DW_IRQ |
| C5, C12 | GJM1555C1H2R0B | 分别串联在 DW_RF1 与 DW_RF2 射频路径中的元件 | 图 d8a1261888ed / 第 1 页 / 第1页 B3，C5 位于 DW_RF1 路径；第1页 C3，C12 位于 DW_RF2 路径；两者均标注 GJM1555C1H2R0B |
| C21 | 1.5PF | DW_RF1 匹配网络中的对地支路 | 图 d8a1261888ed / 第 1 页 / 第1页 B3，C21 从 C5/C20 之间节点接至 GND，标注 1.5PF |
| C24 | 49.9R | DW_RF2 串联 C12 后节点的对地元件；保留图面位号与数值原文 | 图 d8a1261888ed / 第 1 页 / 第1页 C3，C24 从 DW_RF2 路径末端节点接至 GND，图面数值标注 49.9R |
| C6, C7 | 10uF/10V; 100nF/25V | U2 VIN 侧 VCC_3V3 输入去耦 | 图 d8a1261888ed / 第 1 页 / 第1页 A2-A3，C6=10uF/10V、C7=100nF/25V，均从 VCC_3V3 接至 GND |
| C2, C3, C4 | 10uF/10V; 10uF/10V; 100nF/25V | VCC_1V8 输出轨对地去耦 | 图 d8a1261888ed / 第 1 页 / 第1页 A3-A4，C2/C3=10uF/10V、C4=100nF/25V，均从 VCC_1V8 接至 GND |
| C8, C9, C10, C11, C16, C17 | 100nF/25V; 4.7nF/50V; 4.7nF/50V; 4.7nF/50V; 100nF/25V; 220nF/25V | U1 的 VDD1、VDD2a、VDD2b、VDD3、VIO_D 和 VTX_D 供电去耦 | 图 d8a1261888ed / 第 1 页 / 第1页 B2，U1A 右侧 C8-C11；第1页 B2-C2，C16、C17，均画为对应供电脚至 GND |
| C13, C14 | 100nF/25V | FB1 两侧 VCC_3V3 与 VCCA_3V3 的对地去耦 | 图 d8a1261888ed / 第 1 页 / 第1页 C1，C13 位于 VCC_3V3 侧、C14 位于 VCCA_3V3 侧，均标注 100nF/25V 并接 GND |
| C15 | 1uF/10V | DW_RSTn 网络的对地电容 | 图 d8a1261888ed / 第 1 页 / 第1页 B1，C15 标注 1uF/10V，从 DW_RSTn 接至 GND |
| C18, C19 | 3.3pF | X1 两端 DW_XTI 与 DW_XTO 的对地负载电容 | 图 d8a1261888ed / 第 1 页 / 第1页 D1，C18 从 DW_XTI 接 GND，C19 从 DW_XTO 接 GND，均标注 3.3pF |
| R3, C22 | NC | 图面明确标注 NC 的可选位置，不据此认定已装配 | 图 d8a1261888ed / 第 1 页 / 第1页 A4，R3 标注 NC；第1页 B3，C22 标注 NC |

## 系统结构

### 单页电路架构

图面由 U1 UWB 收发器、U2 供电级、X1 时钟网络、RF1/RF2 网络以及 J1/PINMAP 外部引脚组成。

- 参数与网络：`core=U1 QM33120WTR13`；`power_stage=U2 JW5712`；`clock=X1 SX0B38.400F0810F30`；`external_connector=J1 PIN1-PIN12`；`rf_nets=DW_RF1, DW_RF2, DW_RF1_ANT`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页全页，U1/U2 位于 A-B 区，RF 网络位于 B-C3，X1/J1/PINMAP 位于 D 区

### 页内 PINMAP 标识

第1页右下 PINMAP 图的模块中心文字为 Stamp UWB。

- 参数与网络：`panel_title=PINMAP`；`module_text=Stamp UWB`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 D4，PINMAP 框内模块图形中央文字 Stamp UWB

## 核心器件

### U1

U1A 器件标注为 QM33120WTR13，符号分组包含控制、SPI、GPIO、时钟、射频和多路供电脚。

- 参数与网络：`reference=U1`；`part_number=QM33120WTR13`；`symbol_units=U1A, U1B`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A1-B2，U1A 框及底部型号标注；第1页 D2，U1B 接地引脚单元

### U1B 接地引脚

U1B 将图中列出的两列封装引脚全部连接至 GND。

- 参数与网络：`left_column=E6,E10,E12,F7,F9,G6,G10,H1,H3,H7,H9,H13,D11`；`right_column=E14,C12,D13,A14,B11,C8,C10,D9,A2,B3,C6,D5,D7`；`net=GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 D2，U1B/DW3120 接地引脚单元，两侧引脚总线均落到 GND

## 电源

### U1 VDD1

U1A VDD1(B13) 连接 VCC_3V3，并由 C8 100nF/25V 对地去耦。

- 参数与网络：`pin=B13`；`rail=VCC_3V3`；`decoupling=C8 100nF/25V to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B2，U1A VDD1(B13)、VCC_3V3 与 C8

### U1 VDD2a

U1A VDD2a(F15) 连接 VCCA_3V3，并由 C9 4.7nF/50V 对地去耦。

- 参数与网络：`pin=F15`；`rail=VCCA_3V3`；`decoupling=C9 4.7nF/50V to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B2，U1A VDD2a(F15)、VCCA_3V3 与 C9

### U1 VDD2b

U1A VDD2b(B15) 连接 VCCA_3V3，并由 C10 4.7nF/50V 对地去耦。

- 参数与网络：`pin=B15`；`rail=VCCA_3V3`；`decoupling=C10 4.7nF/50V to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B2，U1A VDD2b(B15)、VCCA_3V3 与 C10

### U1 VDD3

U1A VDD3(D15) 连接 VCC_1V8，并由 C11 4.7nF/50V 对地去耦。

- 参数与网络：`pin=D15`；`rail=VCC_1V8`；`decoupling=C11 4.7nF/50V to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B2，U1A VDD3(D15)、VCC_1V8 与 C11

### U1 VIO_D 与 VTX_D

U1A VIO_D(A4) 由 C16 100nF/25V 接地，VTX_D(C14) 由 C17 220nF/25V 接地。

- 参数与网络：`VIO_D_A4=C16 100nF/25V to GND`；`VTX_D_C14=C17 220nF/25V to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B2-C2，U1A 右下 VIO_D/VTX_D 与 C16/C17

### VCCA_3V3

VCCA_3V3 由 VCC_3V3 经 FB1 600R@100MHz 串联滤波得到，FB1 两侧分别由 C13 和 C14 100nF/25V 接地。

- 参数与网络：`source_rail=VCC_3V3`；`filter=FB1 600R@100MHz`；`destination_rail=VCCA_3V3`；`source_cap=C13 100nF/25V`；`destination_cap=C14 100nF/25V`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 C1，VCC_3V3-C13-FB1-C14-VCCA_3V3 滤波网络

### U2 输入与使能

U2 的 VIN(A2) 接 VCC_3V3，EN(B1) 接 DW_EXTON，GND(B2) 接地。

- 参数与网络：`VIN_A2=VCC_3V3`；`EN_B1=DW_EXTON`；`GND_B2=GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A2-A3，U2 左侧 EN/VIN/GND 引脚及网络

### U2 电压选择脚

U2 的 VSEL1(C1)、VSEL2(D1) 和 VSEL3(D2) 在图面上汇接后连接 GND。

- 参数与网络：`VSEL1=C1 to GND`；`VSEL2=D1 to GND`；`VSEL3=D2 to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A3，U2 右下 VSEL1/VSEL2/VSEL3 共用走线与 GND 符号

### VCC_1V8 生成路径

U2 SW(A1) 经 L1 串联到 VCC_1V8，U2 VOS(C2) 接 VCC_1V8；C1 1nF/50V 跨接 SW 节点与 VCC_1V8。

- 参数与网络：`switch_pin=SW A1`；`inductor=L1 FTC121065S2R2MBCA`；`output_rail=VCC_1V8`；`sense_pin=VOS C2`；`coupling_cap=C1 1nF/50V between SW and VCC_1V8`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A3-A4，U2 SW/VOS、C1、L1 与 VCC_1V8 网络

### U2 输入输出去耦

VCC_3V3 输入侧使用 C6 10uF/10V 与 C7 100nF/25V 对地，VCC_1V8 输出侧使用 C2/C3 各 10uF/10V 与 C4 100nF/25V 对地。

- 参数与网络：`input_caps=C6=10uF/10V; C7=100nF/25V`；`output_caps=C2=10uF/10V; C3=10uF/10V; C4=100nF/25V`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A2-A4，U2 输入侧 C6/C7 和输出侧 C2/C3/C4

### R3 可选电源连接

R3 位于 VCC_3V3 与 VCC_1V8 输出节点之间并标注 NC；图面明确表示该位置不作为已装电阻确认。

- 参数与网络：`reference=R3`；`marking=NC`；`endpoint_1=VCC_3V3`；`endpoint_2=VCC_1V8 output node`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A4，R3 上端 VCC_3V3、下端接 L1 后输出节点，数值标注 NC

## 接口

### 12 针 PINMAP 电源脚

PINMAP 明确标出 1、8、12 脚为 GND，2 脚为 VCC_3V3。

- 参数与网络：`pin_1=GND`；`pin_2=VCC_3V3`；`pin_8=GND`；`pin_12=GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 D4，PINMAP 图左侧 1/2 脚和右侧 8/12 脚标注

### 12 针 PINMAP 控制脚

PINMAP 明确标出 3=DW_WAKEUP、4=DW_IRQ、5=DW_GP7、6=DW_RSTn。

- 参数与网络：`pin_3=DW_WAKEUP`；`pin_4=DW_IRQ`；`pin_5=DW_GP7`；`pin_6=DW_RSTn`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 D4，PINMAP 图左侧 3 至 6 脚网络标注

### 12 针 PINMAP SPI 脚

PINMAP 明确标出 7=DW_CDO、9=DW_CDI、10=DW_CSn、11=DW_CLK。

- 参数与网络：`pin_7=DW_CDO`；`pin_9=DW_CDI`；`pin_10=DW_CSn`；`pin_11=DW_CLK`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 D4，PINMAP 图右侧 7、9、10、11 脚网络标注

## 总线

### U1 SPI

U1A 的 SPICLK(A8)、SPICDI(B7)、SPICDO(A6) 和 SPICSn(B5) 分别连接 DW_CLK、DW_CDI、DW_CDO 和 DW_CSn。

- 参数与网络：`SPICLK_A8=DW_CLK`；`SPICDI_B7=DW_CDI`；`SPICDO_A6=DW_CDO`；`SPICSn_B5=DW_CSn`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B1，U1A 左侧 SPI 引脚 SPICLK/SPICDI/SPICDO/SPICSn

## GPIO 与控制信号

### U1 控制信号

U1A 的 EXTON(A12)、WAKEUP(B9)、RSTn(A10) 和 IRQ/GPIO9(B1) 分别连接 DW_EXTON、DW_WAKEUP、DW_RSTn 和 DW_IRQ。

- 参数与网络：`EXTON_A12=DW_EXTON`；`WAKEUP_B9=DW_WAKEUP`；`RSTn_A10=DW_RSTn`；`IRQ_GPIO9_B1=DW_IRQ`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A1，U1A 左上控制引脚与网络名

### U1 GPIO7/SYNC

U1A 的 GPIO7/SYNC(G2) 连接网络 DW_GP7。

- 参数与网络：`pin=G2`；`function_label=GPIO7/SYNC`；`net=DW_GP7`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B1-B2，U1A GPIO7/SYNC(G2) 左侧网络 DW_GP7

### U1 GPIO0 至 GPIO6

图面在 U1A 的 GPIO0/RXOKLED、GPIO1/SFDLED、GPIO2/RXLED、GPIO3/TXLED、GPIO4/EXTTA、GPIO5/EXTTXE/SPIPOL 和 GPIO6/EXTRXE/SPIPHA 引脚外侧均画有 no-connect 标记。

- 参数与网络：`GPIO0=C2 no-connect`；`GPIO1=D3 no-connect`；`GPIO2=E4 no-connect`；`GPIO3=E2 no-connect`；`GPIO4=F1 no-connect`；`GPIO5=D1 no-connect`；`GPIO6=C4 no-connect`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B1，U1A GPIO0-GPIO6 左侧红色交叉 no-connect 标记

### DW_IRQ

DW_IRQ 由 R2 10K/1% 上拉至 VCC_3V3，并连接 U1A 的 IRQ/GPIO9(B1)。

- 参数与网络：`pullup=R2 10K/1% to VCC_3V3`；`u1_pin=IRQ/GPIO9 B1`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 C1，R2 与 DW_IRQ；第1页 A1，DW_IRQ 接 U1A IRQ/GPIO9(B1)

## 时钟

### U1 外部时钟网络

U1A XTI(H15) 和 XTO(G14) 分别经 DW_XTI 与 DW_XTO 接到 X1 的 1 脚和 3 脚，C18 与 C19 各以 3.3pF 接地，X1 的 2 脚和 4 脚接 GND。

- 参数与网络：`u1_xti=H15 -> DW_XTI -> X1 pin 1`；`u1_xto=G14 -> DW_XTO -> X1 pin 3`；`x1_part=SX0B38.400F0810F30`；`load_caps=C18=3.3pF, C19=3.3pF`；`ground_pins=X1 pins 2 and 4`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B1-B2，U1A XTI/XTO；第1页 D1，X1、C18、C19 与 DW_XTI/DW_XTO

## 复位

### DW_RSTn

DW_RSTn 由 R1 10K/1% 上拉至 VCC_3V3，并由 C15 1uF/10V 接至 GND。

- 参数与网络：`pullup=R1 10K/1% to VCC_3V3`；`capacitor=C15 1uF/10V to GND`；`u1_pin=RSTn A10`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A1-B1，R1/C15 围绕 DW_RSTn；第1页 A1，DW_RSTn 接 U1A RSTn(A10)

## 关键网络

### DW_EXTON

DW_EXTON 同时连接 U1A 的 EXTON(A12) 与 U2 的 EN(B1)，构成 U1 至 1.8V 电源级的可见使能联系。

- 参数与网络：`source_pin=U1A EXTON A12`；`destination_pin=U2 EN B1`；`net=DW_EXTON`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A1，U1A EXTON(A12) 网络；第1页 A3，U2 EN(B1) 使用同名 DW_EXTON

## 射频

### U1 RF1 与 RF2

U1A RF1(H11) 和 RF2(J5) 分别连接 DW_RF1 与 DW_RF2，两个网络入口均标有 RF_50R。

- 参数与网络：`RF1_H11=DW_RF1`；`RF2_J5=DW_RF2`；`impedance_callout=RF_50R`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A2，U1A RF1(H11)/RF2(J5) 至 DW_RF1/DW_RF2 及 RF_50R 标注

### DW_RF1 输入段

DW_RF1 先串联 C5，C5 的器件标注为 GJM1555C1H2R0B。

- 参数与网络：`input_net=DW_RF1`；`series_component=C5`；`component_marking=GJM1555C1H2R0B`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B3，DW_RF1 左侧入口至 C5 及其型号标注

### DW_RF1 中间匹配节点

C5 后、C20 前的节点由 C21 1.5PF 接至 GND，并在该节点标有 RF_50R。

- 参数与网络：`shunt_component=C21`；`value=1.5PF`；`destination=GND`；`node_callout=RF_50R`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B3，C5/C20 之间节点、C21 1.5PF 对地支路和 RF_50R 标注

### DW_RF1_ANT

C20 后节点命名为 DW_RF1_ANT，并有 C22 对地支路；C22 标注 NC，输出节点另标 RF_50R。

- 参数与网络：`series_component=C20`；`output_net=DW_RF1_ANT`；`optional_shunt=C22 NC to GND`；`node_callout=RF_50R`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 B3，C20、DW_RF1_ANT、C22 NC 对地支路及右侧 RF_50R 标注

### DW_RF2 输入段

DW_RF2 串联 C12，C12 的器件标注为 GJM1555C1H2R0B，路径两侧节点均标有 RF_50R。

- 参数与网络：`input_net=DW_RF2`；`series_component=C12`；`component_marking=GJM1555C1H2R0B`；`impedance_callout=RF_50R at input and output node`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 C3，DW_RF2、C12 及两处 RF_50R 标注

### DW_RF2 对地终端

C12 后节点通过位号 C24 的元件接至 GND，图面为 C24 标注数值 49.9R。

- 参数与网络：`reference=C24`；`shown_value=49.9R`；`connection=post-C12 node to GND`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 C3，C12 右侧节点至 C24 49.9R 和 GND

### RF_50R 标注

图面在 DW_RF1 入口、RF1 中间节点、DW_RF1_ANT 输出、DW_RF2 入口和 RF2 末端节点共画出 RF_50R 标注。

- 参数与网络：`rf1_callouts=3`；`rf2_callouts=2`；`label=RF_50R`
- 证据：图 d8a1261888ed / 第 1 页 / 第1页 A2、B3、C3，各射频网络上方红色 RF_50R 圆形信息标记

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 单页电路架构 | `core=U1 QM33120WTR13`；`power_stage=U2 JW5712`；`clock=X1 SX0B38.400F0810F30`；`external_connector=J1 PIN1-PIN12`；`rf_nets=DW_RF1, DW_RF2, DW_RF1_ANT` |
| 核心器件 | U1 | `reference=U1`；`part_number=QM33120WTR13`；`symbol_units=U1A, U1B` |
| GPIO 与控制信号 | U1 控制信号 | `EXTON_A12=DW_EXTON`；`WAKEUP_B9=DW_WAKEUP`；`RSTn_A10=DW_RSTn`；`IRQ_GPIO9_B1=DW_IRQ` |
| 总线 | U1 SPI | `SPICLK_A8=DW_CLK`；`SPICDI_B7=DW_CDI`；`SPICDO_A6=DW_CDO`；`SPICSn_B5=DW_CSn` |
| GPIO 与控制信号 | U1 GPIO7/SYNC | `pin=G2`；`function_label=GPIO7/SYNC`；`net=DW_GP7` |
| GPIO 与控制信号 | U1 GPIO0 至 GPIO6 | `GPIO0=C2 no-connect`；`GPIO1=D3 no-connect`；`GPIO2=E4 no-connect`；`GPIO3=E2 no-connect`；`GPIO4=F1 no-connect`；`GPIO5=D1 no-connect`；`GPIO6=C4 no-connect` |
| 复位 | DW_RSTn | `pullup=R1 10K/1% to VCC_3V3`；`capacitor=C15 1uF/10V to GND`；`u1_pin=RSTn A10` |
| GPIO 与控制信号 | DW_IRQ | `pullup=R2 10K/1% to VCC_3V3`；`u1_pin=IRQ/GPIO9 B1` |
| 关键网络 | DW_EXTON | `source_pin=U1A EXTON A12`；`destination_pin=U2 EN B1`；`net=DW_EXTON` |
| 时钟 | U1 外部时钟网络 | `u1_xti=H15 -> DW_XTI -> X1 pin 1`；`u1_xto=G14 -> DW_XTO -> X1 pin 3`；`x1_part=SX0B38.400F0810F30`；`load_caps=C18=3.3pF, C19=3.3pF`；`ground_pins=X1 pins 2 and 4` |
| 电源 | U1 VDD1 | `pin=B13`；`rail=VCC_3V3`；`decoupling=C8 100nF/25V to GND` |
| 电源 | U1 VDD2a | `pin=F15`；`rail=VCCA_3V3`；`decoupling=C9 4.7nF/50V to GND` |
| 电源 | U1 VDD2b | `pin=B15`；`rail=VCCA_3V3`；`decoupling=C10 4.7nF/50V to GND` |
| 电源 | U1 VDD3 | `pin=D15`；`rail=VCC_1V8`；`decoupling=C11 4.7nF/50V to GND` |
| 电源 | U1 VIO_D 与 VTX_D | `VIO_D_A4=C16 100nF/25V to GND`；`VTX_D_C14=C17 220nF/25V to GND` |
| 电源 | VCCA_3V3 | `source_rail=VCC_3V3`；`filter=FB1 600R@100MHz`；`destination_rail=VCCA_3V3`；`source_cap=C13 100nF/25V`；`destination_cap=C14 100nF/25V` |
| 电源 | U2 输入与使能 | `VIN_A2=VCC_3V3`；`EN_B1=DW_EXTON`；`GND_B2=GND` |
| 电源 | U2 电压选择脚 | `VSEL1=C1 to GND`；`VSEL2=D1 to GND`；`VSEL3=D2 to GND` |
| 电源 | VCC_1V8 生成路径 | `switch_pin=SW A1`；`inductor=L1 FTC121065S2R2MBCA`；`output_rail=VCC_1V8`；`sense_pin=VOS C2`；`coupling_cap=C1 1nF/50V between SW and VCC_1V8` |
| 电源 | U2 输入输出去耦 | `input_caps=C6=10uF/10V; C7=100nF/25V`；`output_caps=C2=10uF/10V; C3=10uF/10V; C4=100nF/25V` |
| 电源 | R3 可选电源连接 | `reference=R3`；`marking=NC`；`endpoint_1=VCC_3V3`；`endpoint_2=VCC_1V8 output node` |
| 射频 | U1 RF1 与 RF2 | `RF1_H11=DW_RF1`；`RF2_J5=DW_RF2`；`impedance_callout=RF_50R` |
| 射频 | DW_RF1 输入段 | `input_net=DW_RF1`；`series_component=C5`；`component_marking=GJM1555C1H2R0B` |
| 射频 | DW_RF1 中间匹配节点 | `shunt_component=C21`；`value=1.5PF`；`destination=GND`；`node_callout=RF_50R` |
| 射频 | DW_RF1_ANT | `series_component=C20`；`output_net=DW_RF1_ANT`；`optional_shunt=C22 NC to GND`；`node_callout=RF_50R` |
| 射频 | DW_RF2 输入段 | `input_net=DW_RF2`；`series_component=C12`；`component_marking=GJM1555C1H2R0B`；`impedance_callout=RF_50R at input and output node` |
| 射频 | DW_RF2 对地终端 | `reference=C24`；`shown_value=49.9R`；`connection=post-C12 node to GND` |
| 射频 | RF_50R 标注 | `rf1_callouts=3`；`rf2_callouts=2`；`label=RF_50R` |
| 接口 | 12 针 PINMAP 电源脚 | `pin_1=GND`；`pin_2=VCC_3V3`；`pin_8=GND`；`pin_12=GND` |
| 接口 | 12 针 PINMAP 控制脚 | `pin_3=DW_WAKEUP`；`pin_4=DW_IRQ`；`pin_5=DW_GP7`；`pin_6=DW_RSTn` |
| 接口 | 12 针 PINMAP SPI 脚 | `pin_7=DW_CDO`；`pin_9=DW_CDI`；`pin_10=DW_CSn`；`pin_11=DW_CLK` |
| 核心器件 | U1B 接地引脚 | `left_column=E6,E10,E12,F7,F9,G6,G10,H1,H3,H7,H9,H13,D11`；`right_column=E14,C12,D13,A14,B11,C8,C10,D9,A2,B3,C6,D5,D7`；`net=GND` |
| 系统结构 | 页内 PINMAP 标识 | `panel_title=PINMAP`；`module_text=Stamp UWB` |
| 接口 | J1 物理连接器类型 | `reference=J1`；`visible_pin_count=12`；`part_number=null`；`pitch=null`；`physical_type=null` |
| 射频 | C20 数值 | `reference=C20`；`position=between C21 node and DW_RF1_ANT`；`shown_value=null` |
| 射频 | DW_RF1_ANT 后级实现 | `visible_output_net=DW_RF1_ANT`；`antenna_symbol=null`；`rf_connector=null`；`antenna_geometry=null` |
| 系统结构 | 产品变体图面标识 | `visible_marking=Stamp UWB`；`missing_marking=Stamp UWB F / S017-F`；`scope=schematic page identity only` |

## 待确认事项

- `interface.j1-physical-type`：当前原理图只显示 J1 的 PIN1 至 PIN12 符号和网络，未标注连接器料号、间距、触点方向或物理封装类型。（证据：图 d8a1261888ed / 第 1 页 / 第1页 D3，J1 仅标 J1、PIN1-PIN12 与网络，器件旁无料号或封装说明）
- `rf.c20-value`：C20 位于 RF1 路径中并有位号，但当前图面未显示其电容值或具体料号。（证据：图 d8a1261888ed / 第 1 页 / 第1页 B3，C20 位号位于串联元件上方，位号下方未见数值或型号文本）
- `rf.antenna-implementation`：图面仅将 RF1 匹配网络输出命名为 DW_RF1_ANT，当前页未画出天线元件、天线几何结构或射频连接器。（证据：图 d8a1261888ed / 第 1 页 / 第1页 B3，DW_RF1_ANT 网络终止于页内网络标号，整页未见天线或射频连接器符号）
- `system.variant-marking`：当前资源页的 PINMAP 中心标为 Stamp UWB，图面未出现 Stamp UWB F 或 S017-F 标识，因此该页本身不能证明 F 变体专属的物理实现差异。（证据：图 d8a1261888ed / 第 1 页 / 第1页 D4，PINMAP 中央仅见 Stamp UWB；全页未见 Stamp UWB F 或 S017-F 文本）
- `review.j1-physical-type`：J1 的具体连接器料号、间距、触点方向和物理封装是什么？；原因：当前原理图仅提供 12 针逻辑符号与网络映射，无法由该页确定连接器机械实现。
- `review.c20-value`：RF1 路径中 C20 的设计值和实际装配值是什么？；原因：当前页画出 C20 串联位置，但没有可见数值或料号，不能从相邻 RF 元件推断。
- `review.antenna-implementation`：DW_RF1_ANT 后连接的天线或射频结构具体是什么？；原因：当前原理图在 DW_RF1_ANT 网络名处结束，没有展示后级天线元件、PCB 结构或连接器。
- `review.variant-marking`：该 Stamp UWB 标识原理图与 Stamp UWB F / S017-F 变体之间的版本和装配对应关系是什么？；原因：产品清单将资源关联到 Stamp UWB F，但图面自身只标 Stamp UWB，且未画出可识别的 F 变体专属标记。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d8a1261888ed7f8bea3935fb2a0bf34e77a16578d205e0f7bcef6ba98e049933` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1262/SCH_UWB_MODULE_SCH_main_V0.2_20251128_2026_06_01_11_54_35_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp_UWB_F.md`

源文档 SHA-256：`60acce4bd3a22aaee72412d606a20102a9bf2aa7bdc7d3d9885f467da69907ca`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
