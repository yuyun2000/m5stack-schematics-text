# Atom DTU NBIoT 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU NBIoT |
| SKU | K059 |
| 产品 ID | `atom-dtu-nbiot-7c62c876adb9` |
| 源文档 | `zh_CN/atom/atom_dtu_nb.md` |

## 概述

Atom DTU NBIoT 以 P1 的 +VIN 为输入，经 F1、SS54 与 U1 MP1584EN 生成 +5V；图中另有 +3.3V 为 M1 SIM7020G/SIM7020C 模组、U4 SP3485EN-L/TR 和接口电路供电。M1 连接 Micro SIM、SMF05CT1G 防护、SMA 天线和 STATUS/NETLIGHT 指示灯，其 UART1 通过 Q3/Q5 在 +1.8V 与 +3.3V 网络间转换后接 Atom-5Pin。RS485 由 TX 经 Q4 自动控制 /RE/DE，A/B 端带偏置、120Ω/NC 可选终端和三只 SP4021-01FTG-C 防护器件，并与 +VIN/GND 一起引到 P1。

## 检索关键词

`Atom DTU NBIoT`、`K059`、`SIM7020G`、`SIM7020C`、`Micro SIM`、`SMF05CT1G`、`SIM_VCC`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`MP1584EN`、`SP3485EN-L/TR`、`SP4021-01FTG-C`、`ANT_SMA-KWE`、`STATUS`、`NETLIGHT`、`U1_TX`、`U1_RX`、`NB_TX`、`NB_RX`、`RS485_A`、`RS485_B`、`+VIN`、`+5V`、`+3.3V`、`+1.8V`、`Atom-4Pin`、`Atom-5Pin`、`HY-2.0_IIC`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| F1 | 1.5A/24V | +VIN 输入串联保护器件 | 图 5b62a55c7039 / 第 1 页 / 左上电源区：+VIN 后串联 F1，标注 1.5A/24V |
| U1 | MP1584EN | 将受保护的 +VIN 降压为 +5V 的开关稳压器 | 图 5b62a55c7039 / 第 1 页 / 左上黄色 U1 MP1584EN 及 VIN/SW/FB/BST/COMP/FREQ 引脚 |
| D3/D5 | SS54 | MP1584EN 开关节点续流与输入节点对地防护 | 图 5b62a55c7039 / 第 1 页 / 左上 D3 SS54 位于 SW 节点与 GND，D5 SS54 位于 F1 后输入节点与 GND |
| M1 | SIM7020G/SIM7020C | NB-IoT 通信模组，连接 UART1、SIM 卡、天线、状态指示和多路电源 | 图 5b62a55c7039 / 第 1 页 / 页面中央 M1，底部型号标注 SIM7020G/SIM7020C，左右共 42 脚 |
| U3 | SIM | Micro SIM 卡座，连接 IO、CLK、RST、VCC 与 GND | 图 5b62a55c7039 / 第 1 页 / 页面中央偏左 U3 SIM 卡座，IO/VPP/GND/CLK/RST/VCC 引脚 |
| U2 | SMF05CT1G | SIM_VCC、SIM_DATA、SIM_CLK 和 SIM_RST 周边的 SIM 线路防护阵列 | 图 5b62a55c7039 / 第 1 页 / M1 左侧 U2 SMF05CT1G，连接 SIM_VCC、GND 与三条 SIM 信号线 |
| E1 | ANT_SMA-KWE | 连接 M1 ANT 的外部 SMA 天线座 | 图 5b62a55c7039 / 第 1 页 / 页面中央偏右 E1 ANT_SMA-KWE，中心端接 M1 ANT 32 脚，外壳接地 |
| D1/Q1 | 0603 / SS8050 Y1 | 由 M1 STATUS 驱动的 +5V 侧状态指示电路 | 图 5b62a55c7039 / 第 1 页 / 右上 STATUS-R3-Q1 与 +5V-R1-D1 链路，D1 标注 0603，Q1 标注 SS8050 Y1 |
| D2/Q2 | 0603 / SS8050 Y1 | 由 M1 NETLIGHT 驱动的 +5V 侧网络指示电路 | 图 5b62a55c7039 / 第 1 页 / 右上 NETLIGHT-R4-Q2 与 +5V-R2-D2 链路，D2 标注 0603，Q2 标注 SS8050 Y1 |
| Q3/Q5 | SS8050 Y1 | U1_RX/U1_TX 与 NB_RX/NB_TX 之间的 +1.8V/+3.3V UART 电平转换 | 图 5b62a55c7039 / 第 1 页 / 页面下中右 Q3/Q5 SS8050 Y1，左右分别为 NB_RX/NB_TX 与 U1_RX/U1_TX |
| U4 | SP3485EN-L/TR | 3.3V RS485 收发器，连接 RX/TX 控制逻辑与 RS485_A/RS485_B | 图 5b62a55c7039 / 第 1 页 / 左下黄色 U4 SP3485EN-L/TR，RO-/RE/DE/DI、A/B、VCC/GND 引脚 |
| Q4 | SS8050 Y1 | 由 TX 经 R24 驱动，控制 U4 的 /RE 与 DE 共节点 | 图 5b62a55c7039 / 第 1 页 / 左下 Q4 SS8050 Y1；基极经 R24 1KΩ 接 TX，集电极接 /RE/DE |
| D6-D8 | SP4021-01FTG-C | RS485_B 对地、A/B 之间和 RS485_A 对地的三级防护 | 图 5b62a55c7039 / 第 1 页 / 页面下中 D6、D7、D8 SP4021-01FTG-C，分别跨 GND-B、B-A、A-GND |
| R22 | 120Ω/NC | 跨接 RS485_B 与 RS485_A 的可选终端电阻 | 图 5b62a55c7039 / 第 1 页 / 页面下中 R22 120Ω/NC，跨接 RS485_B 与 RS485_A |
| P1 | HDR_4P | 引出 RS485_B、RS485_A、+VIN 与 GND 的四针端子 | 图 5b62a55c7039 / 第 1 页 / 页面右中 P1 HDR_4P，端子标注 B、A、12V+、12V- |
| J1/P2/P3 | HY-2.0_IIC / Atom-5Pin / Atom-4Pin | I2C Grove 与 Atom 控制器互连接口 | 图 5b62a55c7039 / 第 1 页 / 页面右侧 J1 HY-2.0_IIC、P2 Atom-5Pin、P3 Atom-4Pin |

## 系统结构

### 系统功能分区

原理图包含 MP1584EN +5V 电源、SIM7020G/SIM7020C 通信模组、Micro SIM 与防护、UART 电平转换、状态指示、SMA 天线、SP3485EN-L/TR RS485 以及 Atom/I2C/四针端子接口。

- 参数与网络：`modem=M1 SIM7020G/SIM7020C`；`buck_converter=U1 MP1584EN`；`rs485=U4 SP3485EN-L/TR`；`sim_socket=U3 SIM`；`antenna=E1 ANT_SMA-KWE`
- 证据：图 5b62a55c7039 / 第 1 页 / 整页原理图：左上电源、中央 M1/SIM、右上指示、左下 RS485、右侧接口

## 电源

### +VIN 到 +5V 电源链

+VIN 经 F1 1.5A/24V 进入 U1 MP1584EN，U1 SW 1 脚经 L1 10uH 输出 +5V；C3、C4、C5 三只 22uF 电容对 +5V 滤波。

- 参数与网络：`input=+VIN`；`series_protection=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`output=+5V`；`output_capacitors=C3/C4/C5 22uF`
- 证据：图 5b62a55c7039 / 第 1 页 / 左上 +VIN-F1-U1 SW-L1-+5V 电源路径

### MP1584EN 反馈与补偿

U1 FB 4 脚连接 R7 51KΩ 与 R8 10KΩ 的 +5V 对地分压节点；FREQ 6 脚经 R9 100KΩ 接地，COMP 3 脚经 C6 150pF 和 R10 100KΩ 串联接地，EN 2 脚标为未连接。

- 参数与网络：`feedback=R7 51KΩ to +5V; R8 10KΩ to GND`；`frequency=R9 100KΩ to GND`；`compensation=C6 150pF + R10 100KΩ to GND`；`enable_connected=false`
- 证据：图 5b62a55c7039 / 第 1 页 / 左上 U1 FB/FREQ/COMP/EN 外围网络

### M1 VBAT 供电

M1 的 VBAT 34 脚和 35 脚并联连接 +3.3V。

- 参数与网络：`component=M1`；`pins=34,35`；`rail=+3.3V`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 右侧 VBAT 34/35 脚并接 +3.3V

### M1 +1.8V 网络

M1 VDD_EXT 40 脚连接 +1.8V，C7 22uF 从 +1.8V 接 GND；该 +1.8V 还用于 Q3/Q5 UART 电平转换的上拉与基极网络。

- 参数与网络：`source_pin=M1 VDD_EXT pin 40`；`rail=+1.8V`；`capacitor=C7 22uF`；`consumers=Q3/Q5 level translation pull-ups and base resistors`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 右侧 VDD_EXT 40 脚、+1.8V/C7，以及下方 Q3/Q5 的 +1.8V 网络

### SIM_VCC 网络

M1 SIM_VDD 18 脚连接 SIM_VCC，SIM_VCC 为 U3 VCC 1 脚供电，并由 C8 100nF 对地去耦。

- 参数与网络：`source=M1 SIM_VDD pin 18`；`net=SIM_VCC`；`destination=U3 VCC pin 1`；`decoupling=C8 100nF`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 SIM_VDD 18 脚、SIM_VCC、U3 VCC 与 C8 100nF

### U4 3.3V 供电

U4 SP3485EN-L/TR 的 VCC 8 脚连接 +3.3V，GND 5 脚接地，C13 100nF 跨接 +3.3V 与 GND。

- 参数与网络：`vcc_pin=8`；`gnd_pin=5`；`rail=+3.3V`；`decoupling=C13 100nF`
- 证据：图 5b62a55c7039 / 第 1 页 / 左下 U4 VCC/GND 与 C13 100nF

### +3.3V 储能与去耦

C14 100uF、C15 100uF 和 C16 100nF 均跨接 +3.3V 与 GND。

- 参数与网络：`capacitors=C14 100uF; C15 100uF; C16 100nF`；`rail=+3.3V`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面右下 C14/C15/C16 从 +3.3V 接 GND

### +3.3V 来源可见性

当前页面显示 +3.3V 连接 M1、U4、P2 和多个电容，但没有显示从 +5V 或 +VIN 生成 +3.3V 的稳压器。

- 参数与网络：`rail=+3.3V`；`generation_circuit_shown=false`；`visible_connections=M1 VBAT; U4 VCC; P2 pin 1; C14/C15/C16`
- 证据：图 5b62a55c7039 / 第 1 页 / 整页电源网络：U1 只生成 +5V，另有多个独立 +3.3V 电源标号但无 3.3V 稳压器

## 接口

### Atom-4Pin 与 I2C 接口

P3 Atom-4Pin 的 1-4 脚为 G21、G25、5V、GND；J1 HY-2.0_IIC 的 1-4 脚为 IIC_SCL、IIC_SDA、VCC、GND，并分别连接 G21、G25、+5V、GND。

- 参数与网络：`p3=1 G21; 2 G25; 3 5V; 4 GND`；`j1=1 IIC_SCL/G21; 2 IIC_SDA/G25; 3 VCC/+5V; 4 GND`；`j1_decoupling=C12 100nF from +5V to GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面右侧 P3 Atom-4Pin、J1 HY-2.0_IIC 与 C12

### Micro SIM 卡接口

U3 SIM 卡座的 VCC 1 脚接 SIM_VCC，RST 2 脚经 R15 22Ω 接 M1 SIM_RST 17 脚，CLK 3 脚经 R14 22Ω 接 M1 SIM_CLK 16 脚，IO 7 脚经 R13 22Ω 接 M1 SIM_DATA 15 脚，GND 5 脚接地，VPP 6 脚未连接。

- 参数与网络：`vcc=U3 pin 1 -> SIM_VCC`；`reset=U3 pin 2 -> R15 22Ω -> M1 pin 17 SIM_RST`；`clock=U3 pin 3 -> R14 22Ω -> M1 pin 16 SIM_CLK`；`data=U3 pin 7 -> R13 22Ω -> M1 pin 15 SIM_DATA`；`ground=U3 pin 5 -> GND`；`vpp_connected=false`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面中央偏左 U3、R13/R14/R15 22Ω 与 M1 SIM_DATA/SIM_CLK/SIM_RST/SIM_VDD

### P1 四针端子

P1 HDR_4P 从上到下标注 B、A、12V+、12V-，分别连接 RS485_B、RS485_A、+VIN 与 GND。

- 参数与网络：`terminal_b=RS485_B`；`terminal_a=RS485_A`；`terminal_12v_plus=+VIN`；`terminal_12v_minus=GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面右中 P1 HDR_4P 及左侧四条网络

## 总线

### M1 UART1

M1 UART1_TXD 1 脚连接 U1_TX，UART1_RXD 2 脚连接 U1_RX；UART1_RTS/CTS/DCD/DTR/RI 3-7 脚在图中标为未连接。

- 参数与网络：`tx=M1 pin 1 UART1_TXD -> U1_TX`；`rx=M1 pin 2 UART1_RXD -> U1_RX`；`unused_handshake_pins=3,4,5,6,7`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 左上 UART1_TXD/UART1_RXD 与 U1_TX/U1_RX；3-7 脚 no-connect 标记

### U1_RX 到 NB_RX 电平转换

Q3 SS8050 Y1 连接 U1_RX 与 NB_RX；U1_RX 由 R18 4.7KΩ 上拉到 +1.8V，NB_RX 由 R17 4.7KΩ 上拉到 +3.3V，Q3 基极经 R16 4.7KΩ 接 +1.8V。

- 参数与网络：`transistor=Q3 SS8050 Y1`；`modem_side=U1_RX / R18 4.7KΩ to +1.8V`；`atom_side=NB_RX / R17 4.7KΩ to +3.3V`；`base_bias=R16 4.7KΩ to +1.8V`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面下中右上半 Q3、R16/R17/R18 与 U1_RX/NB_RX

### U1_TX 到 NB_TX 电平转换

Q5 SS8050 Y1 连接 U1_TX 与 NB_TX；U1_TX 由 R27 4.7KΩ 上拉到 +1.8V，NB_TX 由 R26 4.7KΩ 上拉到 +3.3V，Q5 基极经 R23 4.7KΩ 接 +1.8V。

- 参数与网络：`transistor=Q5 SS8050 Y1`；`modem_side=U1_TX / R27 4.7KΩ to +1.8V`；`atom_side=NB_TX / R26 4.7KΩ to +3.3V`；`base_bias=R23 4.7KΩ to +1.8V`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面下中右下半 Q5、R23/R26/R27 与 U1_TX/NB_TX

### RS485 A/B 与偏置

U4 B 7 脚连接 RS485_B，A 6 脚连接 RS485_A；RS485_B 经 R19 4.7KΩ 接 GND，RS485_A 经 R25 4.7KΩ 接 +3.3V，两条网络分别引到 P1 的 B、A 端子。

- 参数与网络：`b_path=U4 pin 7 -> RS485_B -> P1 B`；`a_path=U4 pin 6 -> RS485_A -> P1 A`；`b_bias=R19 4.7KΩ to GND`；`a_bias=R25 4.7KΩ to +3.3V`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面下中 U4 A/B、R19/R25 偏置与右中 P1 B/A

### RS485 可选终端

R22 标注 120Ω/NC，并跨接 RS485_B 与 RS485_A。

- 参数与网络：`component=R22`；`value=120Ω/NC`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面下中 R22 120Ω/NC 跨接 RS485_B 与 RS485_A

## GPIO 与控制信号

### Atom-5Pin 映射

P2 Atom-5Pin 的 1-5 脚依次为 3V3、G22、G19、G23、G33；G22 接 NB_RX，G19 接 NB_TX，G23 接 TX，G33 接 RX。

- 参数与网络：`pin1=3V3`；`pin2=G22 -> NB_RX`；`pin3=G19 -> NB_TX`；`pin4=G23 -> TX`；`pin5=G33 -> RX`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面右下 P2 Atom-5Pin 与 NB_RX/NB_TX/TX/RX 网络

### STATUS 指示电路

M1 STATUS 42 脚连接 STATUS；STATUS 经 R3 1KΩ 驱动 Q1 SS8050 Y1，R5 10KΩ 将 STATUS 下拉到 GND，Q1 集电极连接由 +5V 经 R1 1KΩ 和 D1 0603 构成的指示支路。

- 参数与网络：`source_pin=M1 STATUS pin 42`；`base_resistor=R3 1KΩ`；`pulldown=R5 10KΩ`；`transistor=Q1 SS8050 Y1`；`indicator=+5V -> R1 1KΩ -> D1 0603 -> Q1`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 STATUS 42 脚及页面右上 STATUS-R3/R5-Q1-D1-R1

### NETLIGHT 指示电路

M1 NETLIGHT 41 脚连接 NETLIGHT；NETLIGHT 经 R4 1KΩ 驱动 Q2 SS8050 Y1，R6 10KΩ 将 NETLIGHT 下拉到 GND，Q2 集电极连接由 +5V 经 R2 1KΩ 和 D2 0603 构成的指示支路。

- 参数与网络：`source_pin=M1 NETLIGHT pin 41`；`base_resistor=R4 1KΩ`；`pulldown=R6 10KΩ`；`transistor=Q2 SS8050 Y1`；`indicator=+5V -> R2 1KΩ -> D2 0603 -> Q2`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 NETLIGHT 41 脚及页面右上 NETLIGHT-R4/R6-Q2-D2-R2

## 保护电路

### +VIN 与开关节点防护

F1 后输入节点通过 D5 SS54 和 C2 10uF 接 GND；U1 SW 节点通过 D3 SS54 接 GND，BST 8 脚通过 C1 100nF 接 SW 节点。

- 参数与网络：`input_diode=D5 SS54`；`input_capacitor=C2 10uF`；`switch_diode=D3 SS54`；`bootstrap_capacitor=C1 100nF`
- 证据：图 5b62a55c7039 / 第 1 页 / 左上 D5/C2 输入支路与 C1/D3 开关节点支路

### SIM 信号防护与滤波

U2 SMF05CT1G 的信号端连接 SIM_DATA、SIM_CLK、SIM_RST，供电端接 SIM_VCC、接地端接 GND；C9、C10、C11 各 33pF 分别从三条 SIM 信号线接 GND。

- 参数与网络：`array=U2 SMF05CT1G`；`protected_signals=SIM_DATA; SIM_CLK; SIM_RST`；`rail=SIM_VCC`；`shunt_capacitors=C9/C10/C11 33pF to GND`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 左侧 U2 SMF05CT1G 与下方 C9/C10/C11 33pF

### RS485 防护网络

D6、D7、D8 均标注 SP4021-01FTG-C；D6 跨 GND 与 RS485_B，D7 跨 RS485_B 与 RS485_A，D8 跨 RS485_A 与 GND。

- 参数与网络：`d6=GND to RS485_B`；`d7=RS485_B to RS485_A`；`d8=RS485_A to GND`；`part_number=SP4021-01FTG-C`
- 证据：图 5b62a55c7039 / 第 1 页 / 页面下中 D6-D8 与 RS485_B/RS485_A/GND 三节点

## 关键网络

### M1 PWRKEY

M1 PWRKEY 39 脚通过 R11 0Ω 连接 GND。

- 参数与网络：`pin=39`；`signal=PWRKEY`；`resistor=R11 0Ω`；`connection=GND`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 右上 PWRKEY 39 脚经 R11 0Ω 下接 GND

### RS485 方向控制

TX 经 R24 1KΩ 驱动 Q4 SS8050 Y1 基极；Q4 发射极接 GND，集电极连接 U4 的 /RE 2 脚和 DE 3 脚共节点，该节点由 R21 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`control_net=TX`；`base_resistor=R24 1KΩ`；`transistor=Q4 SS8050 Y1`；`controlled_pins=U4 /RE pin 2 and DE pin 3`；`pullup=R21 4.7KΩ to +3.3V`
- 证据：图 5b62a55c7039 / 第 1 页 / 左下 TX-R24-Q4 与 U4 /RE/DE 共节点、R21 上拉

### U4 数据引脚

U4 RO 1 脚经 R20 1KΩ 连接 RX，RX 再接 P2 G33；U4 DI 4 脚直接连接 GND。

- 参数与网络：`receiver=U4 RO pin 1 -> R20 1KΩ -> RX -> P2 G33`；`driver_input=U4 DI pin 4 -> GND`
- 证据：图 5b62a55c7039 / 第 1 页 / 左下 U4 RO-R20-RX 与 DI 对地连接，右下 P2 G33-RX

## 射频

### M1 天线通路

M1 ANT 32 脚直接连接 E1 ANT_SMA-KWE 中心端，E1 外壳端接 GND。

- 参数与网络：`source=M1 ANT pin 32`；`connector=E1 ANT_SMA-KWE`；`series_component=null`
- 证据：图 5b62a55c7039 / 第 1 页 / M1 右侧 ANT 32 脚到 E1 ANT_SMA-KWE 的水平连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统功能分区 | `modem=M1 SIM7020G/SIM7020C`；`buck_converter=U1 MP1584EN`；`rs485=U4 SP3485EN-L/TR`；`sim_socket=U3 SIM`；`antenna=E1 ANT_SMA-KWE` |
| 电源 | +VIN 到 +5V 电源链 | `input=+VIN`；`series_protection=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`output=+5V`；`output_capacitors=C3/C4/C5 22uF` |
| 保护电路 | +VIN 与开关节点防护 | `input_diode=D5 SS54`；`input_capacitor=C2 10uF`；`switch_diode=D3 SS54`；`bootstrap_capacitor=C1 100nF` |
| 电源 | MP1584EN 反馈与补偿 | `feedback=R7 51KΩ to +5V; R8 10KΩ to GND`；`frequency=R9 100KΩ to GND`；`compensation=C6 150pF + R10 100KΩ to GND`；`enable_connected=false` |
| 电源 | M1 VBAT 供电 | `component=M1`；`pins=34,35`；`rail=+3.3V` |
| 电源 | M1 +1.8V 网络 | `source_pin=M1 VDD_EXT pin 40`；`rail=+1.8V`；`capacitor=C7 22uF`；`consumers=Q3/Q5 level translation pull-ups and base resistors` |
| 关键网络 | M1 PWRKEY | `pin=39`；`signal=PWRKEY`；`resistor=R11 0Ω`；`connection=GND` |
| 总线 | M1 UART1 | `tx=M1 pin 1 UART1_TXD -> U1_TX`；`rx=M1 pin 2 UART1_RXD -> U1_RX`；`unused_handshake_pins=3,4,5,6,7` |
| 总线 | U1_RX 到 NB_RX 电平转换 | `transistor=Q3 SS8050 Y1`；`modem_side=U1_RX / R18 4.7KΩ to +1.8V`；`atom_side=NB_RX / R17 4.7KΩ to +3.3V`；`base_bias=R16 4.7KΩ to +1.8V` |
| 总线 | U1_TX 到 NB_TX 电平转换 | `transistor=Q5 SS8050 Y1`；`modem_side=U1_TX / R27 4.7KΩ to +1.8V`；`atom_side=NB_TX / R26 4.7KΩ to +3.3V`；`base_bias=R23 4.7KΩ to +1.8V` |
| GPIO 与控制信号 | Atom-5Pin 映射 | `pin1=3V3`；`pin2=G22 -> NB_RX`；`pin3=G19 -> NB_TX`；`pin4=G23 -> TX`；`pin5=G33 -> RX` |
| 接口 | Atom-4Pin 与 I2C 接口 | `p3=1 G21; 2 G25; 3 5V; 4 GND`；`j1=1 IIC_SCL/G21; 2 IIC_SDA/G25; 3 VCC/+5V; 4 GND`；`j1_decoupling=C12 100nF from +5V to GND` |
| 接口 | Micro SIM 卡接口 | `vcc=U3 pin 1 -> SIM_VCC`；`reset=U3 pin 2 -> R15 22Ω -> M1 pin 17 SIM_RST`；`clock=U3 pin 3 -> R14 22Ω -> M1 pin 16 SIM_CLK`；`data=U3 pin 7 -> R13 22Ω -> M1 pin 15 SIM_DATA`；`ground=U3 pin 5 -> GND`；`vpp_connected=false` |
| 电源 | SIM_VCC 网络 | `source=M1 SIM_VDD pin 18`；`net=SIM_VCC`；`destination=U3 VCC pin 1`；`decoupling=C8 100nF` |
| 保护电路 | SIM 信号防护与滤波 | `array=U2 SMF05CT1G`；`protected_signals=SIM_DATA; SIM_CLK; SIM_RST`；`rail=SIM_VCC`；`shunt_capacitors=C9/C10/C11 33pF to GND` |
| 射频 | M1 天线通路 | `source=M1 ANT pin 32`；`connector=E1 ANT_SMA-KWE`；`series_component=null` |
| GPIO 与控制信号 | STATUS 指示电路 | `source_pin=M1 STATUS pin 42`；`base_resistor=R3 1KΩ`；`pulldown=R5 10KΩ`；`transistor=Q1 SS8050 Y1`；`indicator=+5V -> R1 1KΩ -> D1 0603 -> Q1` |
| GPIO 与控制信号 | NETLIGHT 指示电路 | `source_pin=M1 NETLIGHT pin 41`；`base_resistor=R4 1KΩ`；`pulldown=R6 10KΩ`；`transistor=Q2 SS8050 Y1`；`indicator=+5V -> R2 1KΩ -> D2 0603 -> Q2` |
| 电源 | U4 3.3V 供电 | `vcc_pin=8`；`gnd_pin=5`；`rail=+3.3V`；`decoupling=C13 100nF` |
| 关键网络 | RS485 方向控制 | `control_net=TX`；`base_resistor=R24 1KΩ`；`transistor=Q4 SS8050 Y1`；`controlled_pins=U4 /RE pin 2 and DE pin 3`；`pullup=R21 4.7KΩ to +3.3V` |
| 关键网络 | U4 数据引脚 | `receiver=U4 RO pin 1 -> R20 1KΩ -> RX -> P2 G33`；`driver_input=U4 DI pin 4 -> GND` |
| 总线 | RS485 A/B 与偏置 | `b_path=U4 pin 7 -> RS485_B -> P1 B`；`a_path=U4 pin 6 -> RS485_A -> P1 A`；`b_bias=R19 4.7KΩ to GND`；`a_bias=R25 4.7KΩ to +3.3V` |
| 总线 | RS485 可选终端 | `component=R22`；`value=120Ω/NC`；`endpoint_a=RS485_B`；`endpoint_b=RS485_A` |
| 保护电路 | RS485 防护网络 | `d6=GND to RS485_B`；`d7=RS485_B to RS485_A`；`d8=RS485_A to GND`；`part_number=SP4021-01FTG-C` |
| 接口 | P1 四针端子 | `terminal_b=RS485_B`；`terminal_a=RS485_A`；`terminal_12v_plus=+VIN`；`terminal_12v_minus=GND` |
| 电源 | +3.3V 储能与去耦 | `capacitors=C14 100uF; C15 100uF; C16 100nF`；`rail=+3.3V` |
| 电源 | +3.3V 来源可见性 | `rail=+3.3V`；`generation_circuit_shown=false`；`visible_connections=M1 VBAT; U4 VCC; P2 pin 1; C14/C15/C16` |

## 待确认事项

- `review.modem_variant`：K059 当前硬件版本实际装配的是 SIM7020G 还是 SIM7020C？；原因：M1 在原理图中并列标为 SIM7020G/SIM7020C，无法仅凭该页区分实装型号。
- `review.3v3_source`：+3.3V 是由 Atom 经 P2 提供，还是由当前页面未展示的其他电源电路提供？；原因：当前原理图只显示 +3.3V 负载与 P2 连接，没有画出该电源轨的生成或供电方向。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5b62a55c7039274af90a41bc3cd61c1b1b7b6d24ea41ea1b133f40f4c95c647c` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb/atom_dtu_nb_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_dtu_nb.md`

源文档 SHA-256：`900e536c0c0ab6799919c3fd8b37dde03fe7efde55cb7ae528077b5e5ec4b9ce`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
