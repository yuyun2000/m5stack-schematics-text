# Atom DTU NBIoT2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom DTU NBIoT2 |
| SKU | K059-B |
| 产品 ID | `atom-dtu-nbiot2-30888e04c136` |
| 源文档 | `zh_CN/atom/Atom DTU_NB_IoT2.md` |

## 概述

Atom DTU NBIoT2 以 SIM7028 蜂窝通信模块为核心，通过 UART1 的 NB_TX/NB_RX 连接 Atom 5Pin 接口，并使用 Micro SIM 卡座和 SMA 外置天线。+VIN 经 1.5A/24V 保险丝和 MP1584EN 降压生成 +5V，Atom 接口提供的 +3.3V 为 SIM7028 VBAT、RS485 收发器和逻辑电路供电。SP3485EN-L/TR 采用 TX 驱动 Q4 的自动方向控制，RS485 A/B 端具有偏置、可选终端和 SP4021 防护。板上还引出 +5V I2C Grove、RS485/电源四针端子、SIM7028 UART0 测试点，以及 STATUS 红灯和 NETLIGHT 蓝灯。

## 检索关键词

`Atom DTU NBIoT2`、`K059-B`、`SIM7028`、`MP1584EN`、`SP3485EN-L/TR`、`SMF05CT1G`、`SP4021-01FTG-C`、`ANT_SMA-KWE`、`Micro SIM`、`NB_TX`、`NB_RX`、`UART1_TXD`、`UART1_RXD`、`UART0_TXD`、`UART0_RXD`、`STATUS`、`NETLIGHT`、`RS485_A`、`RS485_B`、`+VIN`、`+5V`、`+3.3V`、`+1.8V`、`Atom-4Pin`、`Atom-5Pin`、`G21 I2C SCL`、`G25 I2C SDA`、`G19 NB_TX`、`G22 NB_RX`、`G23 RS485_TX`、`G33 RS485_RX`、`HY-2.0_IIC`、`HDR_4P`、`RS485 auto direction`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7028 | NB-IoT 通信模块，提供 UART、SIM 卡接口、状态输出和 SMA 天线连接 | 图 c540d12b63c8 / 第 1 页 / 网格 2B-3C，M1 SIM7028 的 UART1/UART0、SIM、VBAT/VDD_EXT、STATUS/NETLIGHT、ANT 和控制引脚 |
| U1 | MP1584EN | +VIN 到 +5V 的降压转换器 | 图 c540d12b63c8 / 第 1 页 / 网格 1A-2B，U1 MP1584EN、F1、L1、反馈和输入/输出保护网络 |
| U3 | SIM | Micro SIM 卡座，连接 SIM_DATA、SIM_CLK、SIM_RST 和 SIM_VCC | 图 c540d12b63c8 / 第 1 页 / 网格 1C-2C，U3 SIM 卡座、R13-R15、C8-C11 与 M1 SIM 引脚 |
| U2 | SMF05CT1G | SIM 卡信号线的多路 ESD 防护阵列 | 图 c540d12b63c8 / 第 1 页 / 网格 2B-C，U2 SMF05CT1G 与 SIM_DATA/SIM_CLK/SIM_RST 信号支路 |
| E1 | ANT_SMA-KWE | SIM7028 ANT 引脚的 SMA 外置天线连接器 | 图 c540d12b63c8 / 第 1 页 / 网格 3B-C，M1 pin32 ANT 到 E1 ANT_SMA-KWE，外壳多点接地 |
| Q1, D1 | SS8050 Y1 / RED LED | 由 STATUS 网络驱动的红色状态指示灯 | 图 c540d12b63c8 / 第 1 页 / 网格 3A，STATUS、R3/R5、Q1 SS8050 Y1、D1 RED 与 R1 |
| Q2, D2 | SS8050 Y1 / BLUE LED | 由 NETLIGHT 网络驱动的蓝色网络状态指示灯 | 图 c540d12b63c8 / 第 1 页 / 网格 4A，NETLIGHT、R4/R6、Q2 SS8050 Y1、D2 BLUE 与 R2 |
| U4 | SP3485EN-L/TR | 3.3V RS485 半双工收发器 | 图 c540d12b63c8 / 第 1 页 / 网格 1D-2D，U4 SP3485EN-L/TR、RO/RE/DE/DI、A/B 与 3.3V |
| Q4 | SS8050 Y1 | 由 TX 控制 U4 /RE 与 DE 的 RS485 自动方向晶体管 | 图 c540d12b63c8 / 第 1 页 / 网格 1D，TX、R24、Q4、R21 与 U4 pin2/pin3 |
| P1 | HDR_4P | RS485 A/B 与 +VIN/GND 电源四针端子 | 图 c540d12b63c8 / 第 1 页 / 网格 4B，P1 HDR_4P 的 B/A/12V+/12V- 与 RS485_B/RS485_A/+VIN/GND |
| J1 | HY-2.0_IIC | G21/G25、+5V 和 GND 的 I2C Grove 接口 | 图 c540d12b63c8 / 第 1 页 / 网格 4C，J1 HY-2.0_IIC、G21/G25/+5V/GND 与 C12 |
| P3 | Atom-4Pin | Atom 主机的 G21/G25/+5V/GND 接口 | 图 c540d12b63c8 / 第 1 页 / 网格 4C-D，P3 Atom-4Pin 的 G21/G25/5V/GND |
| P2 | Atom-5Pin | Atom 主机的 3.3V、NB-IoT UART 和 RS485 UART 接口 | 图 c540d12b63c8 / 第 1 页 / 网格 4C-D，P2 Atom-5Pin 的 3V3/G22/G19/G23/G33 与 NB_RX/NB_TX/TX/RX |
| F1 | 1.5A/24V | +VIN 输入串联保险丝 | 图 c540d12b63c8 / 第 1 页 / 网格 1A，+VIN 与 U1 VIN 之间的 F1 1.5A/24V |

## 系统结构

### Atom DTU NBIoT2 架构

M1 SIM7028 通过 NB_TX/NB_RX 与 Atom-5Pin 接口通信，连接 Micro SIM 卡座和 SMA 天线；板上另含 MP1584EN 5V 电源、SP3485EN-L/TR RS485、I2C Grove 和两路状态 LED。

- 参数与网络：`cellular_module=M1 SIM7028`；`host_uart=NB_TX/NB_RX via P2 Atom-5Pin`；`sim_holder=U3 SIM`；`antenna=E1 ANT_SMA-KWE`；`dc_converter=U1 MP1584EN`；`rs485=U4 SP3485EN-L/TR`
- 证据：图 c540d12b63c8 / 第 1 页 / 全图电源、SIM7028、SIM/SMA、RS485、Atom 与 Grove 接口

## 电源

### +VIN 到 +5V 降压

+VIN 经 F1 1.5A/24V 进入 U1 MP1584EN，SW 经 L1 10uH 输出 +5V；反馈分压为 R7 210kΩ 与 R8 40.2kΩ，输出配置 C3-C5 各 22uF。

- 参数与网络：`input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`feedback=R7 210kΩ, R8 40.2kΩ`；`output=+5V`；`output_capacitors=C3, C4, C5 each 22uF`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 1A-3B，+VIN/F1/U1/L1/R7/R8/C3-C5/+5V

### SIM7028 电源

M1 VBAT pin34/pin35 接 +3.3V，VDD_EXT pin40 输出 +1.8V 并配置 C7 22uF；SIM_VCC 从 M1 SIM_VDD pin18 供给卡座。

- 参数与网络：`module_vbat=+3.3V at pin34/pin35`；`vdd_ext=+1.8V at pin40`；`vdd_ext_capacitor=C7 22uF`；`sim_supply=SIM_VCC from pin18 SIM_VDD`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 2B-C-3B，M1 VBAT/VDD_EXT/SIM_VDD、+3.3V/+1.8V/SIM_VCC 和 C7

## 接口

### Atom-5Pin 映射

P2 pin1=+3.3V、pin2=G22/NB_RX、pin3=G19/NB_TX、pin4=G23/TX、pin5=G33/RX。

- 参数与网络：`connector=P2 Atom-5Pin`；`pin1=+3.3V`；`pin2=G22 / NB_RX`；`pin3=G19 / NB_TX`；`pin4=G23 / TX`；`pin5=G33 / RX`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4C-D，P2 Atom-5Pin 五个引脚和对应红色网络

### Micro SIM 卡接口

M1 SIM_DATA/SIM_CLK/SIM_RST 经 R13/R14/R15 各 22Ω 连接 U3 SIM 卡座 IO/CLK/RST，M1 SIM_VDD 形成 SIM_VCC 连接卡座 VCC；VPP 未连接。

- 参数与网络：`holder=U3 SIM`；`data=M1 pin15 SIM_DATA via R13 22Ω`；`clock=M1 pin16 SIM_CLK via R14 22Ω`；`reset=M1 pin17 SIM_RST via R15 22Ω`；`supply=SIM_VCC from M1 pin18`；`vpp=NC`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 1C-2C，U3、R13-R15 与 M1 pin15-pin18

### P1 RS485 与电源端子

P1 HDR_4P 的 B 端接 RS485_B、A 端接 RS485_A、12V+ 端接 +VIN、12V- 端接 GND。

- 参数与网络：`connector=P1 HDR_4P`；`B=RS485_B`；`A=RS485_A`；`12V+=+VIN`；`12V-=GND`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4B，P1 HDR_4P 四个端子与左侧网络

### P3 Atom-4Pin 映射

P3 pin1=G21、pin2=G25、pin3=+5V、pin4=GND。

- 参数与网络：`connector=P3 Atom-4Pin`；`pin1=G21`；`pin2=G25`；`pin3=+5V`；`pin4=GND`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4C-D，P3 Atom-4Pin 四个引脚

### J1 I2C Grove 接口

J1 pin1 IIC_SCL 接 G21、pin2 IIC_SDA 接 G25、pin3 VCC 接 +5V、pin4 GND 接地，+5V 侧配置 C12 100nF。

- 参数与网络：`connector=J1 HY-2.0_IIC`；`pin1=G21 / IIC_SCL`；`pin2=G25 / IIC_SDA`；`pin3=+5V`；`pin4=GND`；`decoupling=C12 100nF`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4C，J1、G21/G25/+5V/GND 与 C12

## 总线

### SIM7028 主 UART

M1 UART1_TXD pin1 连接 NB_TX/U1_TX，M1 UART1_RXD pin2 连接 NB_RX/U1_RX；UART1 RTS/CTS/DCD/DTR/RI 均标记未连接。

- 参数与网络：`tx=M1 pin1 UART1_TXD to NB_TX`；`rx=M1 pin2 UART1_RXD to NB_RX`；`unused_flow_control=RTS, CTS, DCD, DTR, RI NC`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 2B，M1 UART1 pin1-pin7 与 NB_TX/NB_RX

### SP3485 RS485 数据路径

U4 RO 经 R20 1kΩ 输出 RX，DI 固定接 GND，/RE 与 DE 并接同一方向控制节点；A/B 分别连接 RS485_A/RS485_B。

- 参数与网络：`transceiver=U4 SP3485EN-L/TR`；`receiver_output=RO-R20 1kΩ-RX`；`driver_input=DI to GND`；`direction_pins=/RE and DE tied`；`bus=A=RS485_A, B=RS485_B`；`supply=+3.3V`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 1D-2D，U4 pin1-pin8、RX、GND、方向节点与 RS485_A/B

### RS485 自动方向控制

TX 经 R24 1kΩ 驱动 Q4 SS8050 Y1，Q4 集电极连接 U4 /RE 与 DE，方向节点由 R21 4.7kΩ 上拉到 +3.3V。

- 参数与网络：`input=TX`；`base_resistor=R24 1kΩ`；`transistor=Q4 SS8050 Y1`；`controlled_pins=U4 /RE and DE`；`pullup=R21 4.7kΩ to +3.3V`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 1D，TX/R24/Q4/R21 与 U4 pin2/pin3

## GPIO 与控制信号

### STATUS 红色 LED

M1 STATUS pin42 经 R3 1kΩ 驱动 Q1 SS8050 Y1，R5 100kΩ 将基极网络下拉；Q1 控制由 +5V、R1 1kΩ 和 D1 RED 构成的指示支路。

- 参数与网络：`module_output=M1 pin42 STATUS`；`base_resistor=R3 1kΩ`；`base_pulldown=R5 100kΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 RED with R1 1kΩ`；`supply=+5V`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 3A，STATUS、R3/R5、Q1、D1、R1 和 +5V

### NETLIGHT 蓝色 LED

M1 NETLIGHT pin41 经 R4 1kΩ 驱动 Q2 SS8050 Y1，R6 100kΩ 将基极网络下拉；Q2 控制由 +5V、R2 1kΩ 和 D2 BLUE 构成的指示支路。

- 参数与网络：`module_output=M1 pin41 NETLIGHT`；`base_resistor=R4 1kΩ`；`base_pulldown=R6 100kΩ`；`transistor=Q2 SS8050 Y1`；`led=D2 BLUE with R2 1kΩ`；`supply=+5V`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4A，NETLIGHT、R4/R6、Q2、D2、R2 和 +5V

### SIM7028 WAKEUP 固定电平

M1 WAKEUP pin39 通过 R11 0Ω 接 GND。

- 参数与网络：`module_pin=M1 pin39 WAKEUP`；`resistor=R11 0Ω`；`level=GND`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 3B，M1 WAKEUP、R11 0Ω 与 GND

## 保护电路

### 5V 电源保护

MP1584EN 输入节点由 D5 SS54 对地保护并配置 C2 10uF，输出 +5V 由 D4 TVS 5V 对地钳位；BST/SW 网络使用 C1 100nF 和 D3 SS54。

- 参数与网络：`input_diode=D5 SS54`；`input_capacitor=C2 10uF`；`output_tvs=D4 TVS 5V`；`bootstrap=C1 100nF and D3 SS54`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 1A-3A，D5/C2 输入支路、D4 输出支路和 C1/D3 BST 网络

### SIM 卡信号防护与滤波

U2 SMF05CT1G 连接 SIM 数据、时钟和复位线路并对地防护，三条线路另分别配置 C9/C10/C11 33pF 对地，SIM_VCC 配置 C8 100nF。

- 参数与网络：`array=U2 SMF05CT1G`；`signal_capacitors=C9, C10, C11 each 33pF`；`supply_capacitor=C8 100nF`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 2B-C，U2、C8-C11 与 SIM_DATA/SIM_CLK/SIM_RST/SIM_VCC

### RS485 A/B 偏置与浪涌防护

RS485_B 通过 R19 4.7kΩ 接 GND，RS485_A 通过 R25 4.7kΩ 接 +3.3V，R22 NC 预留跨线终端；D6、D7、D8 SP4021-01FTG-C 分别形成 B 对地、B-A 跨线和 A 对地保护。

- 参数与网络：`b_bias=R19 4.7kΩ to GND`；`a_bias=R25 4.7kΩ to +3.3V`；`termination=R22 NC across A/B`；`b_to_ground=D6 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C`；`a_to_ground=D8 SP4021-01FTG-C`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 2D-3D，RS485_A/B、R19/R25/R22 与 D6-D8

## 关键网络

### Atom 主机信号映射

G21/G25 分别连接 I2C SCL/SDA，G22/G19 分别连接 NB_RX/NB_TX，G23/G33 分别连接 RS485 TX/RX。

- 参数与网络：`G21=I2C SCL`；`G25=I2C SDA`；`G22=NB_RX`；`G19=NB_TX`；`G23=RS485 TX`；`G33=RS485 RX`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 4C-D，P2/P3 Atom 接口和 J1 I2C 网络标注

## 射频

### SIM7028 SMA 天线

M1 ANT pin32 直接连接 E1 ANT_SMA-KWE 的中心导体，SMA 外壳多点接 GND。

- 参数与网络：`module_pin=M1 pin32 ANT`；`connector=E1 ANT_SMA-KWE`；`shield=GND`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 3B-C，M1 ANT 到 E1 中心线及外壳接地

## 调试与烧录

### SIM7028 BOOT 与 UART0 测试点

M1 BOOT pin10 引出到 JP1，UART0_RXD pin23 引出 U0R/JP2，UART0_TXD pin22 引出 U0T/JP3，附近另设接地测试点 JP4。

- 参数与网络：`boot=M1 pin10 to JP1`；`uart0_rx=M1 pin23 U0R to JP2`；`uart0_tx=M1 pin22 U0T to JP3`；`ground=JP4`
- 证据：图 c540d12b63c8 / 第 1 页 / 网格 2B-C-3C，M1 BOOT/UART0_RXD/UART0_TXD 与 JP1-JP4

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom DTU NBIoT2 架构 | `cellular_module=M1 SIM7028`；`host_uart=NB_TX/NB_RX via P2 Atom-5Pin`；`sim_holder=U3 SIM`；`antenna=E1 ANT_SMA-KWE`；`dc_converter=U1 MP1584EN`；`rs485=U4 SP3485EN-L/TR` |
| 电源 | +VIN 到 +5V 降压 | `input=+VIN`；`fuse=F1 1.5A/24V`；`converter=U1 MP1584EN`；`inductor=L1 10uH`；`feedback=R7 210kΩ, R8 40.2kΩ`；`output=+5V`；`output_capacitors=C3, C4, C5 each 22uF` |
| 保护电路 | 5V 电源保护 | `input_diode=D5 SS54`；`input_capacitor=C2 10uF`；`output_tvs=D4 TVS 5V`；`bootstrap=C1 100nF and D3 SS54` |
| 电源 | SIM7028 电源 | `module_vbat=+3.3V at pin34/pin35`；`vdd_ext=+1.8V at pin40`；`vdd_ext_capacitor=C7 22uF`；`sim_supply=SIM_VCC from pin18 SIM_VDD` |
| 总线 | SIM7028 主 UART | `tx=M1 pin1 UART1_TXD to NB_TX`；`rx=M1 pin2 UART1_RXD to NB_RX`；`unused_flow_control=RTS, CTS, DCD, DTR, RI NC` |
| 接口 | Atom-5Pin 映射 | `connector=P2 Atom-5Pin`；`pin1=+3.3V`；`pin2=G22 / NB_RX`；`pin3=G19 / NB_TX`；`pin4=G23 / TX`；`pin5=G33 / RX` |
| 接口 | Micro SIM 卡接口 | `holder=U3 SIM`；`data=M1 pin15 SIM_DATA via R13 22Ω`；`clock=M1 pin16 SIM_CLK via R14 22Ω`；`reset=M1 pin17 SIM_RST via R15 22Ω`；`supply=SIM_VCC from M1 pin18`；`vpp=NC` |
| 保护电路 | SIM 卡信号防护与滤波 | `array=U2 SMF05CT1G`；`signal_capacitors=C9, C10, C11 each 33pF`；`supply_capacitor=C8 100nF` |
| 射频 | SIM7028 SMA 天线 | `module_pin=M1 pin32 ANT`；`connector=E1 ANT_SMA-KWE`；`shield=GND` |
| GPIO 与控制信号 | STATUS 红色 LED | `module_output=M1 pin42 STATUS`；`base_resistor=R3 1kΩ`；`base_pulldown=R5 100kΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 RED with R1 1kΩ`；`supply=+5V` |
| GPIO 与控制信号 | NETLIGHT 蓝色 LED | `module_output=M1 pin41 NETLIGHT`；`base_resistor=R4 1kΩ`；`base_pulldown=R6 100kΩ`；`transistor=Q2 SS8050 Y1`；`led=D2 BLUE with R2 1kΩ`；`supply=+5V` |
| GPIO 与控制信号 | SIM7028 WAKEUP 固定电平 | `module_pin=M1 pin39 WAKEUP`；`resistor=R11 0Ω`；`level=GND` |
| 调试与烧录 | SIM7028 BOOT 与 UART0 测试点 | `boot=M1 pin10 to JP1`；`uart0_rx=M1 pin23 U0R to JP2`；`uart0_tx=M1 pin22 U0T to JP3`；`ground=JP4` |
| 总线 | SP3485 RS485 数据路径 | `transceiver=U4 SP3485EN-L/TR`；`receiver_output=RO-R20 1kΩ-RX`；`driver_input=DI to GND`；`direction_pins=/RE and DE tied`；`bus=A=RS485_A, B=RS485_B`；`supply=+3.3V` |
| 总线 | RS485 自动方向控制 | `input=TX`；`base_resistor=R24 1kΩ`；`transistor=Q4 SS8050 Y1`；`controlled_pins=U4 /RE and DE`；`pullup=R21 4.7kΩ to +3.3V` |
| 保护电路 | RS485 A/B 偏置与浪涌防护 | `b_bias=R19 4.7kΩ to GND`；`a_bias=R25 4.7kΩ to +3.3V`；`termination=R22 NC across A/B`；`b_to_ground=D6 SP4021-01FTG-C`；`line_to_line=D7 SP4021-01FTG-C`；`a_to_ground=D8 SP4021-01FTG-C` |
| 接口 | P1 RS485 与电源端子 | `connector=P1 HDR_4P`；`B=RS485_B`；`A=RS485_A`；`12V+=+VIN`；`12V-=GND` |
| 接口 | P3 Atom-4Pin 映射 | `connector=P3 Atom-4Pin`；`pin1=G21`；`pin2=G25`；`pin3=+5V`；`pin4=GND` |
| 接口 | J1 I2C Grove 接口 | `connector=J1 HY-2.0_IIC`；`pin1=G21 / IIC_SCL`；`pin2=G25 / IIC_SDA`；`pin3=+5V`；`pin4=GND`；`decoupling=C12 100nF` |
| 关键网络 | Atom 主机信号映射 | `G21=I2C SCL`；`G25=I2C SDA`；`G22=NB_RX`；`G19=NB_TX`；`G23=RS485 TX`；`G33=RS485 RX` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c540d12b63c84a9da6bb3ad142154a76071e893d4fecda3daa6e0ed0d6915263` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/542/SCH_AtomNB-DTU2_V1.0_sch_01.png` |

---

源文档：`zh_CN/atom/Atom DTU_NB_IoT2.md`

源文档 SHA-256：`49fe38a2de69a7d2279d23bdfd08f37a85f2e819e4a7a5ff06b071909e312f73`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
