# IoT Base Thermal Online CatM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | IoT Base Thermal Online CatM |
| SKU | K119 |
| 产品 ID | `iot-base-thermal-online-catm-d6c7a2ed64cc` |
| 源文档 | `zh_CN/base/thermalonline_catm.md` |

## 概述

IoT Base Thermal Online CatM 以 U1 SIM7080G 和 U1 MLX90640 为核心：SIM7080G 通过 CORE G0/G35 的双晶体管 UART 电平转换通信，CORE G12 控制 PWRKEY，ANT pin32 接 IPEX；MLX90640 由 HT7533 生成的 3.3V 供电并通过 G21/G22 I2C 连接主机。VIN_P240 经 U3 SY8205FCC 生成 CORE_P050，再由 U4 SY8089AAAC 生成 NB_P033；独立 BAT_IN 经 FU1/D1 接 CORE_BAT。U2 RS485 通道包含自动方向、偏置、DNP 终端位和三只 TVS，J1/J2/J3 提供 Grove 扩展，J4/J7 提供直流与 RS485/电源输入，J8 为 SIM 卡座。MLX90640 地址/测温性能、无线频段协议、U2 料号和电源/电池能力需结合 datasheet、BOM 与实测确认。

## 检索关键词

`IoT Base Thermal Online CatM`、`K119`、`SIM7080G`、`MLX90640`、`HT7533`、`SY8205FCC`、`SY8089AAAC`、`VIN_P240`、`CORE_P050`、`NB_P033`、`NB_P018`、`CORE_BAT`、`CORE_TXD`、`CORE_RXD`、`NB_TXD`、`NB_RXD`、`MOD_PWR`、`NB_KEY`、`NB_STAT`、`RS_TXD`、`RS_RXD`、`RS_A`、`RS_B`、`M5_BUS`、`P1 Header8`、`G21`、`G22`、`G0`、`G35`、`G12`、`G15`、`G13`、`G36`、`G26`、`G17`、`G16`、`I2C`、`RS485`、`MicroSIM`、`IPEX`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (主板) | SIM7080G | Cat-M/NB-IoT 通信模组，连接 UART、PWRKEY、状态 LED、IPEX 天线和 SIM 卡座 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页下中 U1 SIM7080G，UART1、PWRKEY、STATUS、ANT、VBAT/VDD_EXT 与 SIM 引脚 |
| U2 (主板) | 未标注 | NB_P033 供电的 RS485 收发器，连接 RS_TXD/RS_RXD、自动方向网络和 RS_A/RS_B | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 U2，RO/RE/DE/DI/A/B/VCC/GND 与 Q1、偏置和保护网络 |
| U3 (主板) | SY8205FCC | 将 VIN_P240 降压为 CORE_P050 的第一级开关稳压器 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右上 U3 SY8205FCC、FU2、L1 与 CORE_P050 |
| U4 (主板) | SY8089AAAC | 将 CORE_P050 降压为 NB_P033 的第二级开关稳压器 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右上 U4 SY8089AAAC、L2 10uH 与 NB_P033 |
| Q1,Q2,Q3,Q4 | S8050 | RS485 自动方向、CORE/NB UART 电平转换和 SIM7080G PWRKEY 下拉控制 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 Q1/Q2/Q3/Q4 S8050 |
| BUS1 | M5_BUS | 连接主机 GPIO、UART、RS485、模组控制、5V 和电池网络 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左上 BUS1 M5_BUS pin1-pin30 |
| J1,J2,J3 | GROVE 4P | 三组 CORE_P050 供电接口，分别引出 G21/G22、G36/G26 和 G17/G16 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左侧 J1/J2/J3 GROVE 的 IO2/IO1/5V/GND |
| J4 | DC5.5 | VIN_P240 直流输入接口 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 J4 DC5.5，PWR+ VIN_P240、PWR- GND |
| J5,J6 | MX1.25_2P / HT3.96_2P | BAT_IN 与 GND 电池输入接口 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 J5/J6、BAT_IN、FU1/D1/CORE_BAT |
| J7 | HT3.96_4P | 引出 RS_B、RS_A、VIN_P240 和 GND 的 RS485/电源接口 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 J7 pin4 RS_B、pin3 RS_A、pin2 VIN_P240、pin1 GND |
| J8 | CARD_SOCKET_SIM | 连接 SIM7080G 的 SIM_VDD、SIM_DATA、SIM_CLK、SIM_RST、GND 和检测线路 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右下 J8 CARD_SOCKET_SIM 与 U1 SIM 信号 |
| ANT1 | IPEX | SIM7080G ANT pin32 的外部射频天线接口 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页下中 U1 ANT pin32 到 ANT1 IPEX |
| P1 (主板) | Header 8 | 引出 GND、CORE_P050、NB_P033、CORE_BAT、G21、G22、G5、G2 到热成像板 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右中 P1 Header8 pin1-pin8 |
| FU1,D1,FU2 | SL0805200 / SOD4007 / BSMD0805-050-24V | CORE_BAT 与 VIN_P240 输入路径的保险和二极管保护器件 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 FU1/D1 及右上 FU2 |
| TVS1,TVS2,TVS3 | P6S05C-LF | RS_A/RS_B 线间及对地保护器件 | 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 U2 右侧 TVS1/TVS2/TVS3 P6S05C-LF |
| U1 (热成像板) | MLX90640 | 3.3V 供电、通过 G21/G22 I2C 通信的红外阵列传感器 | 图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页左上 U1 MLX90640，VDD/GND/SCL/SDA 四脚 |
| U2 (热成像板) | HT7533 | 将 P1 的 5V 转换为 MLX90640 使用的 3.3V | 图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页下方 U2 HT7533，VIN 5V、VOUT 3.3V、GND |
| P1 (热成像板) | Header 8 | 与主板 P1 对应的 GND、5V、3.3V、BAT+、G21、G22、G5、G2 接口 | 图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页右上 P1 Header8 pin1-pin8 |

## 系统结构

### IoT Base Thermal Online CatM 系统架构

BUS1 提供主机 UART、RS485、GPIO 和电源，SIM7080G 连接 UART 电平转换、PWRKEY、SIM、状态 LED 与 IPEX；P1 将主板电源和 G21/G22 等网络送到热成像板，HT7533 生成 3.3V，MLX90640 通过 G21/G22 I2C 工作。

- 参数与网络：`modem=SIM7080G`；`thermal_sensor=MLX90640`；`power=VIN_P240 -> SY8205FCC -> CORE_P050 -> SY8089AAAC -> NB_P033`；`thermal_power=P1 5V -> HT7533 -> 3.3V`；`thermal_bus=G21 SDA, G22 SCL`；`rs485=BUS1 <-> U2 <-> RS_A/RS_B`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页完整 IoT Base 主板; 图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页 P1、HT7533 与 MLX90640

## 电源

### VIN_P240 到 CORE_P050

VIN_P240 经 FU2 BSMD0805-050-24V 到 U3 SY8205FCC，U3 LX pin2 经 L1 2.2uH 生成 CORE_P050；FB 使用 R15 36K/1% 与 R16 5.1K/1%。

- 参数与网络：`input=VIN_P240`；`fuse=FU2 BSMD0805-050-24V`；`converter=U3 SY8205FCC`；`inductor=L1 2.2uH`；`output=CORE_P050`；`feedback=R15 36K/1%, R16 5.1K/1%`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右上 VIN_P240/FU2/U3/L1/R15/R16/CORE_P050

### CORE_P050 到 NB_P033

CORE_P050 连接 U4 IN pin4 与 EN pin1，U4 SW pin3 经 L2 10uH 形成 NB_P033，FB 使用 R18 22K/1% 与 R19 8.2K/1%，C11 226/16V 对地。

- 参数与网络：`input=CORE_P050`；`converter=U4 SY8089AAAC`；`inductor=L2 10uH`；`output=NB_P033`；`feedback=R18 22K/1%, R19 8.2K/1%`；`output_capacitor=C11 226/16V`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右上 CORE_P050/U4/L2/R18/R19/C11/NB_P033

### BAT_IN 到 CORE_BAT

J5 pin1 与 J6 pin2 接 BAT_IN，J5 pin2/SH 与 J6 pin1 接 GND；BAT_IN 经 FU1 SL0805200 到 CORE_BAT，D1 SOD4007 连接 CORE_BAT 与 GND，CORE_BAT 再连接 BUS1 pin1 和 P1 pin4。

- 参数与网络：`inputs=J5 pin1, J6 pin2 BAT_IN`；`fuse=FU1 SL0805200`；`diode=D1 SOD4007`；`output=CORE_BAT -> BUS1 pin1, P1 pin4`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 J5/J6、BAT_IN、FU1、D1、CORE_BAT

### SIM7080G 电源连接

U1 VBAT pins34/35 接 NB_P033，并由 C1/C2 两只 106/10V 电容对地去耦；VDD_EXT pin40 输出 NB_P018，多只 GND 引脚接 GND。

- 参数与网络：`vbat=pins34/35 NB_P033`；`caps=C1/C2 106/10V`；`logic_output=pin40 VDD_EXT NB_P018`；`ground=U1 GND pins`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 U1 VBAT/VDD_EXT/GND 与 NB_P033/NB_P018/C1/C2

### 热成像板 5V 到 3.3V

P1 pin2 的 5V 连接 U2 HT7533 VIN pin2，VOUT pin3 输出 3.3V；输入侧 C4 22uF/C2 100nF、输出侧 C3 22uF 对地，3.3V 通过 R3 0Ω 接 P1 pin3 并供给 MLX90640。

- 参数与网络：`input=P1 pin2 5V`；`regulator=U2 HT7533`；`output=3.3V`；`input_caps=C4 22uF,C2 100nF`；`output_cap=C3 22uF`；`header_link=3.3V -> R3 0Ω -> P1 pin3`
- 证据：图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页 U2 HT7533、C2/C3/C4、3.3V/5V 与 P1

## 接口

### BUS1 M5_BUS 已连接针脚

BUS1 已连接 pin30/28/26 GND、pin29 CORE_RXD、pin27 G36、pin21 G26、pin16 G16、pin15 G17、pin14 G21、pin13 G22、pin12 G2、pin11 G5、pin10 MOD_PWR、pin9 RS_TXD、pin8 RS_RXD、pin7 CORE_TXD、pin3 CORE_P050 和 pin1 CORE_BAT。

- 参数与网络：`modem_uart=pin29 CORE_RXD G35; pin7 CORE_TXD G0`；`rs485=pin9 RS_TXD G13; pin8 RS_RXD G15`；`control=pin10 MOD_PWR G12`；`grove=G21,G22,G36,G26,G17,G16`；`header_gpio=G2,G5`；`power=pin3 CORE_P050, pin1 CORE_BAT`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左上 BUS1 所有带外部网络名的针脚

### J1/J2/J3 Grove 接口

J1 pin4-pin1 连接 G22/G21/CORE_P050/GND；J2 连接 G36/G26/CORE_P050/GND；J3 连接 G16/G17/CORE_P050/GND。

- 参数与网络：`J1=pin4 G22, pin3 G21, pin2 CORE_P050, pin1 GND`；`J2=pin4 G36, pin3 G26, pin2 CORE_P050, pin1 GND`；`J3=pin4 G16, pin3 G17, pin2 CORE_P050, pin1 GND`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左侧 J1/J2/J3 GROVE pin1-pin4

### J4/J7 外部接口

J4 DC5.5 的 PWR+ 接 VIN_P240、PWR- 接 GND；J7 HT3.96_4P 的 pin4=RS_B、pin3=RS_A、pin2=VIN_P240、pin1=GND。

- 参数与网络：`J4=PWR+ VIN_P240, PWR- GND`；`J7=pin4 RS_B, pin3 RS_A, pin2 VIN_P240, pin1 GND`；`rs485_direction=bidirectional`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页左下 J4 DC5.5 与 J7 HT3.96_4P

### 主板与热成像板 P1 Header8

主板 P1 pins1-8 依次为 GND、CORE_P050、NB_P033、CORE_BAT、G21、G22、G5、G2；热成像板 P1 对应 pins1-8 为 GND、5V、经 R3 0Ω 的 3.3V、BAT+、G21、G22、G5、G2。

- 参数与网络：`main_P1=1 GND,2 CORE_P050,3 NB_P033,4 CORE_BAT,5 G21,6 G22,7 G5,8 G2`；`thermal_P1=1 GND,2 5V,3 3.3V via R3 0Ω,4 BAT+,5 G21,6 G22,7 G5,8 G2`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右中 P1 Header8; 图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页右上 P1 Header8

### SIM7080G 状态指示

U1 STATUS pin42 输出 NB_STAT，经 R13 5.1K/1% 和 LED1 RED 接 GND；NETLIGHT pin41 在本页未连接。

- 参数与网络：`status=pin42 NB_STAT -> R13 -> LED1 RED -> GND`；`netlight=pin41 unconnected`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 U1 STATUS/NETLIGHT、R13 与 LED1

### SIM7080G 与 J8 SIM 卡座

U1 SIM_VDD pin18、SIM_DATA pin15、SIM_CLK pin16、SIM_RST pin17 连接 J8 的 VCC、IO、CLK、RST；J8 GND/SHELL 接地，U1 SIM_DET pin14 连接卡座检测相关线路。

- 参数与网络：`vdd=pin18 -> VCC`；`data=pin15 <-> IO`；`clock=pin16 -> CLK`；`reset=pin17 -> RST`；`detect=pin14 SIM_DET`；`ground=J8 GND/SHELL`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右下 U1 SIM 信号与 J8 CARD_SOCKET_SIM

## 总线

### U2 RS485 收发与自动方向

U2 RO pin1 接 RS_TXD，A pin6/B pin7 接 RS_A/RS_B，VCC pin8 接 NB_P033、GND pin5 接地；RE pin2 与 DE pin3 相连并由 Q1 S8050 控制，RS_RXD 经 R2 2.2K 驱动 Q1，R7 2.2K 将 RE/DE 节点上拉到 NB_P033，DI pin4 接 GND。

- 参数与网络：`receiver=RO pin1 -> RS_TXD`；`bus=A pin6 RS_A; B pin7 RS_B`；`direction=RE/DE tied, controlled by Q1`；`control=RS_RXD through R2 2.2K`；`pullup=R7 2.2K to NB_P033`；`driver_input=DI pin4 GND`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 U2、Q1、R2/R7 与 RS_TXD/RS_RXD/RS_A/RS_B

### CORE 与 SIM7080G UART 电平转换

BUS1 pin7 CORE_TXD 经 Q2 S8050 转换到 NB_RXD/U1 UART1_RXD pin2；U1 UART1_TXD pin1 的 NB_TXD 经 Q4 S8050 转换到 CORE_RXD/BUS1 pin29，网络使用 NB_P018、NB_P033 和 R3-R6/R11/R12 5.1K/1%。

- 参数与网络：`core_to_modem=BUS1 pin7 CORE_TXD -> Q2 -> NB_RXD -> U1 pin2`；`modem_to_core=U1 pin1 -> NB_TXD -> Q4 -> CORE_RXD -> BUS1 pin29`；`rails=NB_P018,NB_P033`；`transistors=Q2,Q4 S8050`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 Q2/Q4 UART 电平转换与 U1 UART1_TXD/RXD

### MLX90640 I2C 连接

U1 MLX90640 SDA pin1 接 G21、SCL pin4 接 G22；R2 与 R1 各 4.7KΩ 分别将 SDA 与 SCL 上拉到 3.3V，G21/G22 经 P1 pin5/pin6 连接主板和 BUS1。

- 参数与网络：`controller=M5Stack host`；`device=U1 MLX90640`；`sda=pin1 G21, P1 pin5, BUS1 pin14`；`scl=pin4 G22, P1 pin6, BUS1 pin13`；`pullups=R2 SDA 4.7KΩ, R1 SCL 4.7KΩ to 3.3V`；`logic_level=3.3V`
- 证据：图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页 U1 MLX90640 SDA/SCL 与 R1/R2、P1 G21/G22; 图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 P1 G21/G22 与 BUS1 G21/G22

## GPIO 与控制信号

### SIM7080G PWRKEY 控制

BUS1 pin10 MOD_PWR 经 R9 5.1K/1% 驱动 Q3 S8050，R10 5.1K/1% 将控制节点接地；Q3 将 U1 PWRKEY pin39 的 NB_KEY 拉向 GND。

- 参数与网络：`host=BUS1 pin10 MOD_PWR G12`；`transistor=Q3 S8050`；`base_resistor=R9 5.1K/1%`；`pulldown=R10 5.1K/1%`；`modem_pin=U1 pin39 PWRKEY`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 MOD_PWR/R9/R10/Q3/NB_KEY 与 U1 PWRKEY

## 保护电路

### RS485 偏置、终端位与 TVS

R14 5.1K/1% 将 RS_A 拉向 NB_P033，R17 5.1K/1% 将 RS_B 拉向 GND；RX1 标 DNP 并跨接 RS_A/RS_B。TVS1/TVS2/TVS3 均标 P6S05C-LF，构成线间及对地保护。

- 参数与网络：`a_bias=R14 5.1K/1% to NB_P033`；`b_bias=R17 5.1K/1% to GND`；`termination=RX1 DNP`；`tvs=TVS1/TVS2/TVS3 P6S05C-LF`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 RS_A/RS_B 周围 R14/R17/RX1/TVS1-3

## 传感器

### MLX90640 电源和引脚

U1 MLX90640 VDD pin2 接 3.3V、GND pin3 接 GND，C1 100nF 跨接 3.3V 与 GND；SDA pin1 为 G21、SCL pin4 为 G22。

- 参数与网络：`part_number=MLX90640`；`vdd=pin2 3.3V`；`ground=pin3 GND`；`decoupling=C1 100nF`；`sda=pin1 G21`；`scl=pin4 G22`
- 证据：图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页左上 U1 MLX90640、C1 与四个引脚

## 射频

### SIM7080G 外部天线

U1 ANT pin32 直接连接 ANT1 IPEX，接口外壳接 GND；本页未显示射频匹配网络或切换器。

- 参数与网络：`modem_pin=U1 pin32 ANT`；`connector=ANT1 IPEX`；`shield=GND`；`matching_shown=false`
- 证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 U1 ANT pin32 到 ANT1 IPEX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | IoT Base Thermal Online CatM 系统架构 | `modem=SIM7080G`；`thermal_sensor=MLX90640`；`power=VIN_P240 -> SY8205FCC -> CORE_P050 -> SY8089AAAC -> NB_P033`；`thermal_power=P1 5V -> HT7533 -> 3.3V`；`thermal_bus=G21 SDA, G22 SCL`；`rs485=BUS1 <-> U2 <-> RS_A/RS_B` |
| 接口 | BUS1 M5_BUS 已连接针脚 | `modem_uart=pin29 CORE_RXD G35; pin7 CORE_TXD G0`；`rs485=pin9 RS_TXD G13; pin8 RS_RXD G15`；`control=pin10 MOD_PWR G12`；`grove=G21,G22,G36,G26,G17,G16`；`header_gpio=G2,G5`；`power=pin3 CORE_P050, pin1 CORE_BAT` |
| 电源 | VIN_P240 到 CORE_P050 | `input=VIN_P240`；`fuse=FU2 BSMD0805-050-24V`；`converter=U3 SY8205FCC`；`inductor=L1 2.2uH`；`output=CORE_P050`；`feedback=R15 36K/1%, R16 5.1K/1%` |
| 电源 | CORE_P050 到 NB_P033 | `input=CORE_P050`；`converter=U4 SY8089AAAC`；`inductor=L2 10uH`；`output=NB_P033`；`feedback=R18 22K/1%, R19 8.2K/1%`；`output_capacitor=C11 226/16V` |
| 电源 | BAT_IN 到 CORE_BAT | `inputs=J5 pin1, J6 pin2 BAT_IN`；`fuse=FU1 SL0805200`；`diode=D1 SOD4007`；`output=CORE_BAT -> BUS1 pin1, P1 pin4` |
| 接口 | J1/J2/J3 Grove 接口 | `J1=pin4 G22, pin3 G21, pin2 CORE_P050, pin1 GND`；`J2=pin4 G36, pin3 G26, pin2 CORE_P050, pin1 GND`；`J3=pin4 G16, pin3 G17, pin2 CORE_P050, pin1 GND` |
| 接口 | J4/J7 外部接口 | `J4=PWR+ VIN_P240, PWR- GND`；`J7=pin4 RS_B, pin3 RS_A, pin2 VIN_P240, pin1 GND`；`rs485_direction=bidirectional` |
| 接口 | 主板与热成像板 P1 Header8 | `main_P1=1 GND,2 CORE_P050,3 NB_P033,4 CORE_BAT,5 G21,6 G22,7 G5,8 G2`；`thermal_P1=1 GND,2 5V,3 3.3V via R3 0Ω,4 BAT+,5 G21,6 G22,7 G5,8 G2` |
| 总线 | U2 RS485 收发与自动方向 | `receiver=RO pin1 -> RS_TXD`；`bus=A pin6 RS_A; B pin7 RS_B`；`direction=RE/DE tied, controlled by Q1`；`control=RS_RXD through R2 2.2K`；`pullup=R7 2.2K to NB_P033`；`driver_input=DI pin4 GND` |
| 保护电路 | RS485 偏置、终端位与 TVS | `a_bias=R14 5.1K/1% to NB_P033`；`b_bias=R17 5.1K/1% to GND`；`termination=RX1 DNP`；`tvs=TVS1/TVS2/TVS3 P6S05C-LF` |
| 总线 | CORE 与 SIM7080G UART 电平转换 | `core_to_modem=BUS1 pin7 CORE_TXD -> Q2 -> NB_RXD -> U1 pin2`；`modem_to_core=U1 pin1 -> NB_TXD -> Q4 -> CORE_RXD -> BUS1 pin29`；`rails=NB_P018,NB_P033`；`transistors=Q2,Q4 S8050` |
| GPIO 与控制信号 | SIM7080G PWRKEY 控制 | `host=BUS1 pin10 MOD_PWR G12`；`transistor=Q3 S8050`；`base_resistor=R9 5.1K/1%`；`pulldown=R10 5.1K/1%`；`modem_pin=U1 pin39 PWRKEY` |
| 接口 | SIM7080G 状态指示 | `status=pin42 NB_STAT -> R13 -> LED1 RED -> GND`；`netlight=pin41 unconnected` |
| 射频 | SIM7080G 外部天线 | `modem_pin=U1 pin32 ANT`；`connector=ANT1 IPEX`；`shield=GND`；`matching_shown=false` |
| 接口 | SIM7080G 与 J8 SIM 卡座 | `vdd=pin18 -> VCC`；`data=pin15 <-> IO`；`clock=pin16 -> CLK`；`reset=pin17 -> RST`；`detect=pin14 SIM_DET`；`ground=J8 GND/SHELL` |
| 电源 | SIM7080G 电源连接 | `vbat=pins34/35 NB_P033`；`caps=C1/C2 106/10V`；`logic_output=pin40 VDD_EXT NB_P018`；`ground=U1 GND pins` |
| 电源 | 热成像板 5V 到 3.3V | `input=P1 pin2 5V`；`regulator=U2 HT7533`；`output=3.3V`；`input_caps=C4 22uF,C2 100nF`；`output_cap=C3 22uF`；`header_link=3.3V -> R3 0Ω -> P1 pin3` |
| 总线 | MLX90640 I2C 连接 | `controller=M5Stack host`；`device=U1 MLX90640`；`sda=pin1 G21, P1 pin5, BUS1 pin14`；`scl=pin4 G22, P1 pin6, BUS1 pin13`；`pullups=R2 SDA 4.7KΩ, R1 SCL 4.7KΩ to 3.3V`；`logic_level=3.3V` |
| 传感器 | MLX90640 电源和引脚 | `part_number=MLX90640`；`vdd=pin2 3.3V`；`ground=pin3 GND`；`decoupling=C1 100nF`；`sda=pin1 G21`；`scl=pin4 G22` |
| 核心器件 | U2 RS485 收发器型号 | `reference=U2`；`part_number=null`；`supply=NB_P033`；`pins=RO,RE,DE,DI,A,B,VCC,GND`；`package=null` |
| 射频 | 正文中的无线频段、速率、协议和认证 | `module=SIM7080G`；`documented_uart=115200 8N1`；`documented_modes=Cat-M,NB-IoT`；`documented_protocols=TCP,UDP,HTTP,HTTPS,TLS,DTLS,PING,LWM2M,COAP,MQTT`；`firmware=null`；`measured_throughput=null` |
| 电源 | CORE_P050 与 NB_P033 供电能力 | `rails=CORE_P050,NB_P033`；`converters=SY8205FCC,SY8089AAAC`；`tolerance=null`；`continuous_current=null`；`peak_current=null`；`startup_sequence=null` |
| 保护电路 | J5/J6 电池输入边界 | `connectors=J5 MX1.25_2P,J6 HT3.96_2P`；`path=BAT_IN -> FU1 -> CORE_BAT`；`diode=D1 SOD4007`；`voltage=null`；`chemistry=null`；`charge_path_shown=false` |
| 接口 | SIM 卡座机械规格 | `documented_size=MicroSIM`；`designator=J8 CARD_SOCKET_SIM`；`dimensions=null`；`orientation=null`；`hotplug=null`；`detect_default=null` |
| 总线地址 | MLX90640 I2C 地址 | `device=U1 MLX90640`；`documented_address=0x33`；`schematic_address=null`；`bus=G21 SDA,G22 SCL` |
| 传感器 | 正文中的 MLX90640 阵列与测温范围 | `part_number=MLX90640`；`documented_array=32x24`；`documented_range=-40°C to 300°C`；`accuracy=null`；`refresh_rate=null`；`field_of_view=null` |

## 待确认事项

- `component.rs485-transceiver-model`：原理图显示 U2 的八脚 RS485 收发器连接，但未标注完整器件型号；实际料号、封装、共模范围和失效保护特性无法由本页确认。（证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页中央 U2 只有位号和引脚名）
- `rf.documented-radio-capabilities`：正文列出 Cat-M/NB-IoT 频段、速率、RF 功率、协议、认证和 UART 115200 8N1；原理图只确认 SIM7080G 型号及物理连接，无法验证固件、区域配置、运营商认证状态和通信性能。（证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 U1 SIM7080G、UART1 与 ANT1，图中无频段/速率/协议/认证表）
- `power.rail-capability`：原理图给出两级稳压器、反馈和输出网络，但未标注输出容差、持续/峰值电流、启动时序、热设计或 SIM7080G 发射条件下的压降数据。（证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右上 U3/U4 两级电源与 U1 VBAT 负载）
- `protection.battery-input-limits`：原理图显示 BAT_IN 经 FU1 到 CORE_BAT，并有 D1 SOD4007 对地支路，但未标注允许电池电压、化学体系、极性、充电路径、FU1 额定含义或 D1 的具体保护动作。（证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页 J5/J6、BAT_IN、FU1、D1、CORE_BAT）
- `interface.sim-socket-mechanics`：正文称卡槽为 MicroSIM；原理图只标 J8 CARD_SOCKET_SIM 并展示电气端子，未给出机械尺寸、插卡方向、热插拔限制或 SIM_DET 默认状态。（证据：图 5fe5c54a461d / 第 1 页 / 第 1 张第 1 页右下 J8 CARD_SOCKET_SIM）
- `address.mlx90640`：正文标出 MLX90640 I2C 地址为 0x33；原理图只显示 G21/G22、4.7KΩ 上拉和器件型号，没有地址文字、地址选择脚或总线扫描结果。（证据：图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页 U1 MLX90640 与 I2C 网络，图中无地址标注）
- `sensor.documented-mlx90640-performance`：正文称 MLX90640 为 32x24 阵列且测温范围 -40°C 至 300°C；原理图仅确认型号、3.3V 和 I2C 连接，无法独立验证阵列分辨率、测温范围、精度、刷新率或视场角。（证据：图 bf1e77cc17a7 / 第 1 页 / 第 2 张第 1 页 U1 MLX90640 型号与四脚连接，图中无性能参数）
- `review.rs485-bom`：K119 当前 BOM 中 U2 的完整 RS485 收发器型号、封装和电气特性是什么？；原因：原理图未标 U2 料号。
- `review.radio-capabilities`：K119 的 SIM7080G 固件、区域配置、启用频段、UART 参数、协议栈和有效认证清单是什么？；原因：能力依赖模组固件、运营商和测试条件。
- `review.power-capability`：CORE_P050 与 NB_P033 的目标电压、容差、持续/峰值电流、启动时序和发射压降指标是什么？；原因：网络名与反馈阻值不足以证明整机供电能力。
- `review.battery-safety`：J5/J6 允许连接何种电池、电压与极性，FU1/D1 的额定和保护目的是什么，板上是否具备充电功能？；原因：原理图没有电池规格和充电器。
- `review.sim-socket`：J8 当前 BOM 是否确为 MicroSIM 卡座，插卡方向、SIM_DET 默认状态和热插拔限制是什么？；原因：CARD_SOCKET_SIM 符号不能证明机械规格。
- `review.mlx90640-address`：K119 的 MLX90640 实际 I2C 地址是否经 datasheet 或总线扫描确认为 0x33？；原因：0x33 只在正文出现，原理图没有地址字段。
- `review.mlx90640-performance`：请用 MLX90640 datasheet 和整机校准确认 32x24 阵列、-40°C 至 300°C 范围、精度、刷新率与视场角。；原因：这些性能参数不在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5fe5c54a461d0ba9d98f5bd423e24fd5843762985acde0ee1a6288b75238926a` | `https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_sch_01.webp` |
| 2 | 1 | `bf1e77cc17a7130a1c9816025b04c9bf9bf1ca92ae9da1d762b82fdd419ed013` | `https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_sch_02.webp` |

---

源文档：`zh_CN/base/thermalonline_catm.md`

源文档 SHA-256：`ec73d9ddb3e41578c02abee48cfccf4c2992a8363e8fa45b99ee258124132e06`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
