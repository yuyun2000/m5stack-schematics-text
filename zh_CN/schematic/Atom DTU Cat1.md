# Atom DTU Cat1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU Cat1 |
| SKU | K120 |
| 产品 ID | `atom-dtu-cat1-e0915fd91516` |
| 源文档 | `zh_CN/atom/atom_dtu_cat1.md` |

## 概述

Atom DTU Cat1 由两块通过 BTB1/BTB2 连接的电路组成：底板以 MP1584EN 将端子 +VIN 转换为 +5V，并提供 SP3485EN-L/TR RS485、A/B 保护和电源/总线引出；上板以 SY8003ADFC 将 +5V 转换为 +3.8V，为 M1 SIM-A7680C 的 VBAT 供电。Atom-5Pin 的 G22/G19 经 Q3/Q5 电平转换连接蜂窝模组 UART，G23/G33 连接 RS485 发送/接收，Atom-4Pin 的 G21/G25 连接 I2C 接口。SIM-A7680C 还连接 Micro SIM、SMA 主天线、PWRKEY 0Ω 下拉以及 STATUS/NETLIGHT 指示电路。

## 检索关键词

`Atom DTU Cat1`、`K120`、`A120`、`SIM-A7680C`、`LTE CAT1`、`SY8003ADFC`、`MP1584EN`、`SP3485EN-L/TR`、`SS8050 Y1`、`Micro SIM`、`ANT_SMA-KWE`、`STATUS`、`NETLIGHT`、`PWRKEY`、`SIM_VCC`、`USIM_DATA`、`USIM_CLK`、`USIM_RST`、`NB_RX`、`NB_TX`、`U1_RX`、`U1_TX`、`485_RX`、`485_TX`、`RS485_A`、`RS485_B`、`SDA`、`SCL`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`、`+VIN`、`+5V`、`+3.8V`、`+3.3V`、`+1.8V`、`BTB-MALE`、`BTB-FEMALE`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM-A7680C | 蜂窝通信模组，连接 UART、SIM 卡、主天线、状态信号与 3.8V 电源 | 图 c0f0e61d2582 / 第 1 页 / 下部中央 M1 SIM-A7680C：TXD/RXD、USIM、STATUS/NETLIGHT/VDD_EXT/PWRKEY/VBAT/ANT_MAIN |
| U5 | SY8003ADFC | +5V 到 +3.8V 的降压转换器，为蜂窝模组 VBAT 电源域供电 | 图 c0f0e61d2582 / 第 1 页 / 左上 U5 SY8003ADFC：IN/EN/LX/FB/PG/PGND/SGND、L2、R12/R28 与 +3.8V |
| U1 | MP1584EN | +VIN 到 +5V 的降压转换器 | 图 a684a5f8edc5 / 第 1 页 / 左上 U1 MP1584EN：VIN/SW/BST/FB/FREQ/COMP/GND 与 F1/L1/D3/D5/R7~R10 |
| U4 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 485_RX/485_TX 与 RS485_A/RS485_B | 图 a684a5f8edc5 / 第 1 页 / 左下 U4 SP3485EN-L/TR：RO/nRE/DE/DI/A/B/VCC/GND |
| U3 | SIM | Micro SIM 卡座，连接 SIM_VCC、USIM_DATA、USIM_CLK、USIM_RST 与 GND | 图 c0f0e61d2582 / 第 1 页 / 左下 U3 SIM 卡座 IO/CLK/RST/VCC/VPP/GND 与 M1 USIM 网络 |
| U2 | SMF05CT1G | SIM_VCC 与三路 USIM 信号的多通道保护器件 | 图 c0f0e61d2582 / 第 1 页 / 左下 U2 SMF05CT1G，连接 SIM_VCC、USIM_DATA/CLK/RST 与 GND |
| E1 | ANT_SMA-KWE | SIM-A7680C ANT_MAIN 外部天线连接器 | 图 c0f0e61d2582 / 第 1 页 / 中下 E1 ANT_SMA-KWE 中心端接 M1 ANT_MAIN pin 32，外壳接 GND |
| Q3/Q5 | SS8050 Y1 | Atom 3.3V UART 与 SIM-A7680C 1.8V UART 之间的双向电平转换 | 图 c0f0e61d2582 / 第 1 页 / 右中 Q3/Q5 SS8050 与 R16/R17/R18、R23/R26/R27 的 NB_RX/U1_RX、NB_TX/U1_TX |
| D1/D2/Q1/Q2 | 0603 LED / SS8050 Y1 | STATUS 与 NETLIGHT 的 5V 指示灯驱动电路 | 图 c0f0e61d2582 / 第 1 页 / 右上 +5V-R1-D1-Q1-STATUS 与 +5V-R2-D2-Q2-NETLIGHT |
| Q4 | SS8050 Y1 | 由 485_TX 驱动的 RS485 nRE/DE 自动方向控制晶体管 | 图 a684a5f8edc5 / 第 1 页 / 左下 485_TX-R24 1KΩ-Q4，集电极接 U4 pins 2/3，发射极接 GND |
| D6/D7/D8 | SP4021-01FTG-C | RS485 A/B 对地与线间保护器件 | 图 a684a5f8edc5 / 第 1 页 / 下部 D6 从 RS485_B 到 GND、D7 跨 A/B、D8 从 RS485_A 到 GND |
| BTB1 | BTB-MALE | 蜂窝模组上板的 20 Pin 板间连接器 | 图 c0f0e61d2582 / 第 1 页 / 中央 BTB1 BTB-MALE，双排 SDA/SCL/RS485/485_UART/3.3V/5V/GND/Vin |
| BTB2 | BTB-FEMALE | 电源与 RS485 底板的 20 Pin 板间连接器 | 图 a684a5f8edc5 / 第 1 页 / 右上 BTB2 BTB-FEMALE，双排 Vin/GND/5V/3.3V/485_UART/RS485/SCL/SDA |
| J1 | HY-2.0_IIC | G21/G25 对应 SCL/SDA 的 5V I2C 接口 | 图 c0f0e61d2582 / 第 1 页 / 右下 J1 HY-2.0_IIC，pins 1~4 为 IIC_SCL/IIC_SDA/VCC/GND |
| P2/P3 | Atom-5Pin / Atom-4Pin | Atom 主控到蜂窝 UART、RS485 UART、I2C 与电源的连接器 | 图 c0f0e61d2582 / 第 1 页 / 右下 P2 Atom-5Pin 与 P3 Atom-4Pin 的 3V3/G22/G19/G23/G33/G21/G25/5V/GND |
| P1 | HDR_4P | RS485_B、RS485_A、12V+ 与 12V- 接线端子 | 图 a684a5f8edc5 / 第 1 页 / 右下 P1 HDR_4P，B/A/12V+/12V- 接 RS485_B/RS485_A/+VIN/GND |
| P4 | Header 6 | SCL、SDA、5V、3.3V、VIN 与 GND 综合引出接口 | 图 a684a5f8edc5 / 第 1 页 / 右中 P4 Header 6，pins 1~6 为 SCL/SDA/+5V/+3.3V/+VIN/GND |

## 系统结构

### Atom DTU Cat1 双板结构

BTB1/BTB2 连接蜂窝模组上板与电源/RS485 底板，共享 Vin、+5V、+3.3V、SDA、SCL、RS485_A/B 和 485_RX/TX；上板包含 SIM-A7680C 与 3.8V 电源，底板包含 12V 到 5V 电源和 RS485。

- 参数与网络：`upper_board=M1 SIM-A7680C,U5 SY8003ADFC,BTB1`；`lower_board=U1 MP1584EN,U4 SP3485EN-L/TR,BTB2`；`interconnect=Vin,+5V,+3.3V,SDA,SCL,RS485_A,RS485_B,485_RX,485_TX`
- 证据：图 c0f0e61d2582 / 第 1 页 / source_001 全页 M1/U5/BTB1/Atom 接口; 图 a684a5f8edc5 / 第 1 页 / source_002 全页 U1/U4/BTB2/P1/P4

## 电源

### +VIN 到 +5V

P1 12V+ 连接 +VIN，+VIN 经 F1 1.5A/24V 到 Vin 输入节点；D5 SS54 与 C2 10uF 从 Vin 接地，U1 MP1584EN 经 L1 10uH 和 D3 SS54 生成 +5V。

- 参数与网络：`terminal=P1 12V+`；`input=+VIN`；`fuse=F1 1.5A/24V`；`input_protection=D5 SS54 to GND`；`input_capacitor=C2 10uF`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D3 SS54`；`output=+5V`
- 证据：图 a684a5f8edc5 / 第 1 页 / P1 +VIN 与左上 +VIN-F1-D5-C2-U1-L1-D3-C3/C4/C5-+5V

### MP1584EN 反馈与补偿

U1 FB pin 4 接 R7 51KΩ 与 R8 10KΩ 分压点，FREQ pin 6 经 R9 100KΩ 接地，COMP pin 3 经 C6 150pF 与 R10 100KΩ 串联接地，EN pin 2 标为未连接。

- 参数与网络：`feedback=R7 51KΩ,R8 10KΩ`；`frequency=R9 100KΩ`；`compensation=C6 150pF,R10 100KΩ`；`enable=U1 pin 2 no-connect`；`output_caps=C3/C4/C5 22uF`
- 证据：图 a684a5f8edc5 / 第 1 页 / 左上 U1 FB/FREQ/COMP/EN 与 R7/R8/R9/C6/R10/C3~C5

### +5V 到 +3.8V

U5 IN pin 3 与 EN pin 7 接 +5V，LX pin 6 经 L2 WPN3012H2R2MT 输出 +3.8V；FB pin 1 接 R12 82KΩ 与 R28 15KΩ 分压点，C18 22pF 跨接反馈支路。

- 参数与网络：`converter=U5 SY8003ADFC`；`input=+5V`；`inductor=L2 WPN3012H2R2MT`；`output=+3.8V`；`feedback=R12 82KΩ,R28 15KΩ,C18 22pF`；`input_cap=C17 22uF`；`output_caps=C19/C20 22uF,C14/C15 100uF,C16 100nF`
- 证据：图 c0f0e61d2582 / 第 1 页 / 左上 +5V-C17-U5-L2-R12/R28/C18-C19/C20-C14/C15/C16-+3.8V

### SIM-A7680C 电源引脚

M1 VBAT pins 34/35 接 +3.8V，VDD_EXT pin 40 输出 +1.8V 并由 C7 22uF 接地，USIM_VDD pin 19 形成 SIM_VCC 并由 C8 100nF 接地。

- 参数与网络：`vbat=M1 pins 34,35 +3.8V`；`vdd_ext=M1 pin 40 +1.8V`；`vdd_ext_cap=C7 22uF`；`sim_supply=M1 pin 19 USIM_VDD SIM_VCC`；`sim_supply_cap=C8 100nF`
- 证据：图 c0f0e61d2582 / 第 1 页 / M1 right pins 34/35/40 与 left pin 19，+3.8V/+1.8V/SIM_VCC 及 C7/C8

## 接口

### BTB1/BTB2 板间连接

BTB1 与 BTB2 两排重复传递 Vin、GND、+5V、+3.3V、485_TX、485_RX、RS485_B、RS485_A、SCL 与 SDA；上板 BTB1 还将 SDA/SCL 标为 G25/G21。

- 参数与网络：`power=Vin,GND,+5V,+3.3V`；`rs485_uart=485_TX,485_RX`；`rs485_bus=RS485_B,RS485_A`；`i2c=SCL,SDA`；`atom_aliases=SDA=G25,SCL=G21`；`male=BTB1`；`female=BTB2`
- 证据：图 c0f0e61d2582 / 第 1 页 / 中央 BTB1 pins 1~20 的双排网络; 图 a684a5f8edc5 / 第 1 页 / 右上 BTB2 pins 1~20 的双排网络

### P2 Atom-5Pin

P2 pins 1~5 依次为 +3.3V、G22/NB_RX、G19/NB_TX、G23/485_TX、G33/485_RX。

- 参数与网络：`pin_1=+3.3V`；`pin_2=G22 NB_RX`；`pin_3=G19 NB_TX`；`pin_4=G23 485_TX`；`pin_5=G33 485_RX`
- 证据：图 c0f0e61d2582 / 第 1 页 / 右下 P2 Atom-5Pin pins 1~5 与 NB_RX/NB_TX/485_TX/485_RX

### P3 Atom-4Pin 到 J1 I2C

P3 pins 1~4 的 G21、G25、+5V、GND 分别连接 J1 pins 1~4 的 IIC_SCL、IIC_SDA、VCC、GND；C12 100nF 接在 +5V 与 GND 之间。

- 参数与网络：`scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C12 100nF`
- 证据：图 c0f0e61d2582 / 第 1 页 / 右下 P3 Atom-4Pin、J1 HY-2.0_IIC 与 C12

### U3 SIM 卡接口

M1 USIM_DATA/USIM_CLK/USIM_RST pins 16/17/18 通过三只 22Ω 串联电阻连接 U3 SIM 的 IO/CLK/RST，M1 USIM_VDD pin 19 连接 SIM_VCC 与 U3 VCC，SIM 卡座 GND 接地。

- 参数与网络：`data=M1 pin 16 USIM_DATA via 22Ω to U3 IO`；`clock=M1 pin 17 USIM_CLK via 22Ω to U3 CLK`；`reset=M1 pin 18 USIM_RST via 22Ω to U3 RST`；`supply=M1 pin 19 USIM_VDD-SIM_VCC-U3 VCC`；`signal_caps=C9/C10/C11 33pF to GND`
- 证据：图 c0f0e61d2582 / 第 1 页 / 左下 U3 SIM、三只 22Ω 电阻、C9/C10/C11 与 M1 USIM_DATA/CLK/RST/VDD

### SP3485EN RS485 A/B

U4 B pin 7 连接 RS485_B 并由 R19 4.7KΩ 接 GND，A pin 6 连接 RS485_A 并由 R25 4.7KΩ 接 +3.3V；R22 标为 120Ω/NC 并跨接 A/B。

- 参数与网络：`B=U4 pin 7-RS485_B-R19 4.7KΩ-GND`；`A=U4 pin 6-RS485_A-R25 4.7KΩ-+3.3V`；`termination=R22 120Ω/NC across A/B`
- 证据：图 a684a5f8edc5 / 第 1 页 / 下部 U4 pins 7/6、R19/R25/R22 与 RS485_B/RS485_A

### P1 与 P4 外部接口

P1 的 B/A/12V+/12V- 分别连接 RS485_B/RS485_A/+VIN/GND；P4 pins 1~6 依次为 SCL、SDA、+5V、+3.3V、+VIN、GND。

- 参数与网络：`p1=B=RS485_B,A=RS485_A,12V+=+VIN,12V-=GND`；`p4_pin_1=SCL`；`p4_pin_2=SDA`；`p4_pin_3=+5V`；`p4_pin_4=+3.3V`；`p4_pin_5=+VIN`；`p4_pin_6=GND`
- 证据：图 a684a5f8edc5 / 第 1 页 / 右侧 P1 HDR_4P 与 P4 Header 6 的全部引脚网络

## 总线

### Atom 到 SIM-A7680C UART

Atom G22 的 NB_RX 与 M1 RXD pin 2 的 U1_RX 通过 Q3 SS8050 和 R16/R17/R18 4.7KΩ 电平转换；Atom G19 的 NB_TX 与 M1 TXD pin 1 的 U1_TX 通过 Q5 SS8050 和 R23/R26/R27 4.7KΩ 电平转换，Atom 侧为 +3.3V、模组侧为 +1.8V。

- 参数与网络：`receive_path=P2 G22 NB_RX-Q3-U1_RX-M1 pin 2 RXD`；`receive_resistors=R16/R17/R18 4.7KΩ`；`transmit_path=P2 G19 NB_TX-Q5-U1_TX-M1 pin 1 TXD`；`transmit_resistors=R23/R26/R27 4.7KΩ`；`host_domain=+3.3V`；`modem_domain=+1.8V`
- 证据：图 c0f0e61d2582 / 第 1 页 / 右中 Q3/Q5 电平转换、右下 P2 G22/G19 与 M1 pins 2/1 U1_RX/U1_TX

### Atom 到 SP3485EN 自动方向控制

U4 RO pin 1 经 R20 1KΩ 到 485_RX；485_TX 经 R24 1KΩ 驱动 Q4 基极，Q4 集电极连接 U4 nRE/DE pins 2/3 并由 R21 4.7KΩ 上拉到 +3.3V，U4 DI pin 4 接 GND。

- 参数与网络：`receive=U4 pin 1 RO-R20 1KΩ-485_RX-P2 G33`；`direction_drive=P2 G23-485_TX-R24 1KΩ-Q4 base`；`direction_node=Q4 collector-U4 pins 2/3-R21 4.7KΩ to +3.3V`；`driver_input=U4 pin 4 DI to GND`
- 证据：图 a684a5f8edc5 / 第 1 页 / 左下 U4/R20/R21/R24/Q4 的 485_RX/485_TX/nRE/DE/DI; 图 c0f0e61d2582 / 第 1 页 / 右下 P2 G23/G33 对应 485_TX/485_RX

## GPIO 与控制信号

### STATUS 与 NETLIGHT 指示灯

M1 STATUS pin 42 经 STATUS、R3 1KΩ 驱动 Q1，Q1 控制 +5V-R1 1KΩ-D1 0603 指示支路，STATUS 由 R5 10KΩ 下拉；M1 NETLIGHT pin 41 以相同结构连接 R4/Q2/R2/D2，并由 R6 10KΩ 下拉。

- 参数与网络：`status=M1 pin 42-R3 1KΩ-Q1 SS8050-D1 with R1 1KΩ to +5V`；`status_pulldown=R5 10KΩ`；`netlight=M1 pin 41-R4 1KΩ-Q2 SS8050-D2 with R2 1KΩ to +5V`；`netlight_pulldown=R6 10KΩ`
- 证据：图 c0f0e61d2582 / 第 1 页 / 右上 STATUS/NETLIGHT-R3/R4/R5/R6-Q1/Q2-D1/D2 与 M1 pins 42/41

## 保护电路

### SIM 卡信号保护

U2 SMF05CT1G 连接 SIM_VCC 与三路 USIM_DATA/USIM_CLK/USIM_RST，并以公共端接 GND，为 SIM 卡电源和信号提供保护支路。

- 参数与网络：`device=U2 SMF05CT1G`；`protected_nets=SIM_VCC,USIM_DATA,USIM_CLK,USIM_RST`；`reference=GND`
- 证据：图 c0f0e61d2582 / 第 1 页 / 左下 U2 SMF05CT1G 与 SIM_VCC/USIM 三信号/GND

### RS485 A/B 保护

D6 SP4021-01FTG-C 连接 RS485_B 与 GND，D8 同型号连接 RS485_A 与 GND，D7 同型号跨接 RS485_B 与 RS485_A。

- 参数与网络：`B_to_ground=D6 SP4021-01FTG-C`；`A_to_ground=D8 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C`
- 证据：图 a684a5f8edc5 / 第 1 页 / 下部 D6/D7/D8 围绕 RS485_B/RS485_A 的三器件保护网络

### +5V 与 +3.3V 电源保护

D9 LESD3Z5.0CMT1G 连接 +5V 与 GND，D4 RLSD52A031V 连接 +3.3V 与 GND，D10 LESD3Z5.0CMT1G 连接底板 +5V 与 GND。

- 参数与网络：`upper_5v=D9 LESD3Z5.0CMT1G`；`upper_3v3=D4 RLSD52A031V`；`lower_5v=D10 LESD3Z5.0CMT1G`
- 证据：图 c0f0e61d2582 / 第 1 页 / 右下 D9 +5V-GND 与 D4 +3.3V-GND; 图 a684a5f8edc5 / 第 1 页 / 上部 D10 +5V-GND

## 关键网络

### SIM-A7680C PWRKEY

M1 PWRKEY pin 39 经 R11 0Ω 连接 GND。

- 参数与网络：`modem_pin=M1 pin 39 PWRKEY`；`resistor=R11 0Ω`；`destination=GND`
- 证据：图 c0f0e61d2582 / 第 1 页 / M1 pin 39 PWRKEY-R11 0Ω-GND

## 射频

### SIM-A7680C 主天线

M1 ANT_MAIN pin 32 直接连接 E1 ANT_SMA-KWE 中心端，E1 的四个外壳端连接 GND。

- 参数与网络：`modem_pin=M1 pin 32 ANT_MAIN`；`connector=E1 ANT_SMA-KWE`；`shield=GND`
- 证据：图 c0f0e61d2582 / 第 1 页 / M1 pin 32 ANT_MAIN 到 E1 ANT_SMA-KWE 与外壳 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU Cat1 双板结构 | `upper_board=M1 SIM-A7680C,U5 SY8003ADFC,BTB1`；`lower_board=U1 MP1584EN,U4 SP3485EN-L/TR,BTB2`；`interconnect=Vin,+5V,+3.3V,SDA,SCL,RS485_A,RS485_B,485_RX,485_TX` |
| 电源 | +VIN 到 +5V | `terminal=P1 12V+`；`input=+VIN`；`fuse=F1 1.5A/24V`；`input_protection=D5 SS54 to GND`；`input_capacitor=C2 10uF`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D3 SS54`；`output=+5V` |
| 电源 | MP1584EN 反馈与补偿 | `feedback=R7 51KΩ,R8 10KΩ`；`frequency=R9 100KΩ`；`compensation=C6 150pF,R10 100KΩ`；`enable=U1 pin 2 no-connect`；`output_caps=C3/C4/C5 22uF` |
| 电源 | +5V 到 +3.8V | `converter=U5 SY8003ADFC`；`input=+5V`；`inductor=L2 WPN3012H2R2MT`；`output=+3.8V`；`feedback=R12 82KΩ,R28 15KΩ,C18 22pF`；`input_cap=C17 22uF`；`output_caps=C19/C20 22uF,C14/C15 100uF,C16 100nF` |
| 电源 | SIM-A7680C 电源引脚 | `vbat=M1 pins 34,35 +3.8V`；`vdd_ext=M1 pin 40 +1.8V`；`vdd_ext_cap=C7 22uF`；`sim_supply=M1 pin 19 USIM_VDD SIM_VCC`；`sim_supply_cap=C8 100nF` |
| 接口 | BTB1/BTB2 板间连接 | `power=Vin,GND,+5V,+3.3V`；`rs485_uart=485_TX,485_RX`；`rs485_bus=RS485_B,RS485_A`；`i2c=SCL,SDA`；`atom_aliases=SDA=G25,SCL=G21`；`male=BTB1`；`female=BTB2` |
| 接口 | P2 Atom-5Pin | `pin_1=+3.3V`；`pin_2=G22 NB_RX`；`pin_3=G19 NB_TX`；`pin_4=G23 485_TX`；`pin_5=G33 485_RX` |
| 总线 | Atom 到 SIM-A7680C UART | `receive_path=P2 G22 NB_RX-Q3-U1_RX-M1 pin 2 RXD`；`receive_resistors=R16/R17/R18 4.7KΩ`；`transmit_path=P2 G19 NB_TX-Q5-U1_TX-M1 pin 1 TXD`；`transmit_resistors=R23/R26/R27 4.7KΩ`；`host_domain=+3.3V`；`modem_domain=+1.8V` |
| 接口 | P3 Atom-4Pin 到 J1 I2C | `scl=P3 pin 1 G21-J1 pin 1 IIC_SCL`；`sda=P3 pin 2 G25-J1 pin 2 IIC_SDA`；`power=P3 pin 3 +5V-J1 pin 3 VCC`；`ground=P3 pin 4 GND-J1 pin 4 GND`；`decoupling=C12 100nF` |
| 接口 | U3 SIM 卡接口 | `data=M1 pin 16 USIM_DATA via 22Ω to U3 IO`；`clock=M1 pin 17 USIM_CLK via 22Ω to U3 CLK`；`reset=M1 pin 18 USIM_RST via 22Ω to U3 RST`；`supply=M1 pin 19 USIM_VDD-SIM_VCC-U3 VCC`；`signal_caps=C9/C10/C11 33pF to GND` |
| 保护电路 | SIM 卡信号保护 | `device=U2 SMF05CT1G`；`protected_nets=SIM_VCC,USIM_DATA,USIM_CLK,USIM_RST`；`reference=GND` |
| 射频 | SIM-A7680C 主天线 | `modem_pin=M1 pin 32 ANT_MAIN`；`connector=E1 ANT_SMA-KWE`；`shield=GND` |
| 关键网络 | SIM-A7680C PWRKEY | `modem_pin=M1 pin 39 PWRKEY`；`resistor=R11 0Ω`；`destination=GND` |
| GPIO 与控制信号 | STATUS 与 NETLIGHT 指示灯 | `status=M1 pin 42-R3 1KΩ-Q1 SS8050-D1 with R1 1KΩ to +5V`；`status_pulldown=R5 10KΩ`；`netlight=M1 pin 41-R4 1KΩ-Q2 SS8050-D2 with R2 1KΩ to +5V`；`netlight_pulldown=R6 10KΩ` |
| 总线 | Atom 到 SP3485EN 自动方向控制 | `receive=U4 pin 1 RO-R20 1KΩ-485_RX-P2 G33`；`direction_drive=P2 G23-485_TX-R24 1KΩ-Q4 base`；`direction_node=Q4 collector-U4 pins 2/3-R21 4.7KΩ to +3.3V`；`driver_input=U4 pin 4 DI to GND` |
| 接口 | SP3485EN RS485 A/B | `B=U4 pin 7-RS485_B-R19 4.7KΩ-GND`；`A=U4 pin 6-RS485_A-R25 4.7KΩ-+3.3V`；`termination=R22 120Ω/NC across A/B` |
| 保护电路 | RS485 A/B 保护 | `B_to_ground=D6 SP4021-01FTG-C`；`A_to_ground=D8 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C` |
| 接口 | P1 与 P4 外部接口 | `p1=B=RS485_B,A=RS485_A,12V+=+VIN,12V-=GND`；`p4_pin_1=SCL`；`p4_pin_2=SDA`；`p4_pin_3=+5V`；`p4_pin_4=+3.3V`；`p4_pin_5=+VIN`；`p4_pin_6=GND` |
| 保护电路 | +5V 与 +3.3V 电源保护 | `upper_5v=D9 LESD3Z5.0CMT1G`；`upper_3v3=D4 RLSD52A031V`；`lower_5v=D10 LESD3Z5.0CMT1G` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c0f0e61d2582738a9c34fd2a6d32b2c34c2c720a9776a2973ed34ea5dfc1327b` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_sch_01.webp` |
| 2 | 1 | `a684a5f8edc50737a7f9c446aed37f2e673635a0b705cf33adec49195a8a44b5` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_sch_02.webp` |

---

源文档：`zh_CN/atom/atom_dtu_cat1.md`

源文档 SHA-256：`2cbba3a529822518872c21fec8ea6bf25e063d5af2f4317e7597f364d4d076d5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
