# Atom Socket 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Socket |
| SKU | K055 |
| 产品 ID | `atom-socket-296cfa94a291` |
| 源文档 | `zh_CN/atom/atom_socket.md` |

## 概述

Atom Socket 由低压 Atom 控制板和高压计量/继电器板组成。低压板使用 RPD5W05E102SR 从 AC_L_IN/AC_N_IN 生成 VCC/GND，为 Atom、按键、Grove 和继电器驱动提供电源；高压板以 K1 切换 AC_L_IN 到 AC_L_OUT，以 HLW8032 采集经 R1 分流器和电阻链得到的电流/电压信号。HLW8032 的 TX 通过 EL357N 光耦隔离后作为 RX 返回 Atom，MP150GJ-Z 为计量侧生成 VCC_8032/GND_8032；控制侧 GND 与计量侧 GND_8032 不直接连接。

## 检索关键词

`Atom Socket`、`K055`、`HLW8032`、`RPD5W05E102SR`、`MP150GJ-Z`、`EL357N(C)(TA)-G`、`932-5VDC-SL-AHG`、`S8050`、`AC_L_IN`、`AC_N_IN`、`AC_L_OUT`、`AC_N_OUT`、`L_SLP`、`Relay`、`RX`、`SW`、`G22`、`G23`、`VCC`、`VCC_MCU`、`VCC_8032`、`GND`、`GND_8032`、`SHIELD`、`FUSE 15A250V`、`current shunt`、`voltage divider`、`optocoupler`、`UART 4800bps 8E1`、`1000W`、`10A relay`、`Grove`、`TS-1157-B-B`、`SS34`、`US1JW`、`PSE socket`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| PWR1 | RPD5W05E102SR | 从 AC_L_IN/AC_N_IN 向低压控制板提供 VCC/GND 的电源模块 | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页左中 PWR1 RPD5W05E102SR，AC_L_IN/AC_N_IN 与 VCC/GND 输出 |
| ATOM | ATOM 4P+5P | Atom 主控连接器，使用 G22 接收计量 RX、G23 输出 Relay，并引入 3.3V/VCC/GND | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页中右 ATOM 4P+5P，G22/RX、G23/R1/Relay、3V3/VCC/GND |
| S1 | TS-1157-B-B | 低有效 SW 按键，配有 3.3V 上拉和对地电容 | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页上中 S1 TS-1157-B-B、R3 3.3K、C1 100nF 与 SW/GND/3.3V |
| Q1 | S8050 | 由 Atom Relay 信号驱动的低边开关，控制跨板继电器信号和 LED1 | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页中下 Q1 S8050、R2/R4/LED1、Relay 与 J1 |
| J3 | GROVE | 外部 SW 输入、Relay 输出、VCC 和 GND 控制接口 | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页右下 J3 黑色立式直插 GROVE，IO2=SW、IO1 经 R5 到 Relay、5V=VCC、GND |
| K1 | 932-5VDC-SL-AHG | 将 L_SLP 切换到 AC_L_OUT 的单路继电器，线圈由 VCC_MCU/Relay 驱动 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页上中 K1 932-5VDC-SL-AHG，L_SLP/AC_L_OUT 触点与 Relay/VCC_MCU 线圈 |
| U1 | HLW8032 | 交流电压、电流和功率计量 IC，连接差分电流输入、电压输入和隔离 UART 输出 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页中央 U1 HLW8032，VDD/I_P/I_N/V_P/GND/TX/PF/RX |
| IC1 | EL357N(C)(TA)-G | 隔离 HLW8032 TX 与 Atom RX 的光耦 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页中右 IC1 EL357N(C)(TA)-G，输入侧 VCC_8032/R4/U1 TX 与输出侧 VCC_MCU/R15/R5/J1 |
| U2 | MP150GJ-Z | 从交流输入侧为 HLW8032 计量域生成 VCC_8032/GND_8032 的离线电源控制器 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左下 U2 MP150GJ-Z、R11/D1/C4、D3/D4/L1/C8/R14 与 VCC_8032/GND_8032 |
| R1 | MA2512S3...001M | 串联在 AC_N_OUT 与 AC_N_IN 之间的电流采样分流器 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左中 R1 纵向连接 AC_N_OUT 与 AC_N_IN，旁接 R2/R3/C1/C2 到 U1 I_P/I_N |
| R6-R9 | 470KΩ each | 从 L_SLP 到 HLW8032 V_P 的串联交流电压采样电阻链 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页中左 L_SLP 经 R6/R7/R8/R9 470K 串联到 U1 V_P，R10/C3 对地 |
| FUSE | 2009T15A250V | 串联在 AC_L_IN 与继电器触点前 L_SLP 之间的交流保险丝 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页上方 AC_L_IN -> FUSE 2009T15A250V -> L_SLP -> K1 |
| D2 | S1MD3 | 跨接 K1 线圈的反向保护二极管 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页上中 D2 S1MD3 跨接 K1 Relay/VCC_MCU 线圈 |
| J1 | A1002WR-S-4P | 低压控制板与高压计量板之间的 Relay、隔离 RX、VCC_MCU 和 GND 连接器 | 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页中央 J1 A1002WR-S-4P，GND/VCC/继电器驱动/RX; 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页右中 J1 A1002WR-S-4P，Relay/光耦输出/VCC_MCU/GND |
| P2 | DNP PAD | 未装配的双 EARTH 焊盘/连接位 | 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左上 P2 DNP PAD，连接两处 EARTH |

## 系统结构

### Atom Socket 双板系统架构

资源 1 为 Atom 低压控制板，包含隔离电源、按键、Atom、继电器驱动和 Grove；资源 2 为高压计量/继电器板，包含 AC 通断、HLW8032、计量侧电源和光耦，两板通过 J1 的 Relay、RX、电源和地连接。

- 参数与网络：`controller_board=asset d75ab747fba6`；`metering_board=asset d7d943bc4ec3`；`interconnect=J1 A1002WR-S-4P`；`control_signals=Relay, RX`；`control_power=VCC/VCC_MCU, GND`；`metering_domain=VCC_8032, GND_8032`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页完整低压控制板; 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页完整高压计量/继电器板

## 核心器件

### HLW8032 电能计量核心

U1 HLW8032 由 VCC_8032/GND_8032 供电，I_P/I_N 接电流分流采样，V_P 接火线电压分压，TX 经光耦输出到控制侧；PF 与 RX 在当前图中未连接。

- 参数与网络：`part=HLW8032`；`supply=VCC_8032, GND_8032`；`current_inputs=I_P, I_N`；`voltage_input=V_P`；`telemetry=TX through IC1`；`unconnected=PF, RX`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页中央 U1 HLW8032 供电、采样和 TX/PF/RX 引脚

## 电源

### 低压控制板 AC 到 VCC 电源

PWR1 RPD5W05E102SR 以 AC_L_IN/AC_N_IN 为输入，输出经 D1 SS34 形成控制板 VCC，并以 GND 为低压返回；VCC 供 Atom 5V、J3 和 LED/继电器驱动。

- 参数与网络：`module=PWR1 RPD5W05E102SR`；`input=AC_L_IN, AC_N_IN`；`output=VCC, GND`；`series_diode=D1 SS34`；`loads=ATOM 5V, J3 VCC, LED1/Q1`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页左中 PWR1/D1/R6 与 ATOM/J1/J3 VCC/GND

### 交流火线保险与继电器切换

AC_L_IN 经 FUSE 2009T15A250V 形成 L_SLP，K1 常开触点将 L_SLP 切换到 AC_L_OUT；K1 线圈连接 VCC_MCU 与 Relay，D2 S1MD3 反向跨接线圈。

- 参数与网络：`input=AC_L_IN`；`fuse=2009T15A250V`；`protected_line=L_SLP`；`relay=K1 932-5VDC-SL-AHG`；`output=AC_L_OUT`；`coil=VCC_MCU to Relay`；`flyback=D2 S1MD3`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页上方 AC_L_IN/FUSE/L_SLP/K1/AC_L_OUT 与 Relay/VCC_MCU/D2

### HLW8032 计量侧电源

U2 MP150GJ-Z 从 AC_L_IN/AC_N_IN 侧通过 R11、D1、C4 及 D3/D4/L1/C8/R14 网络生成 VCC_8032，返回为 GND_8032，并由 C10 100nF 为 HLW8032 去耦。

- 参数与网络：`controller=U2 MP150GJ-Z`；`ac_input=AC_L_IN, AC_N_IN`；`output=VCC_8032, GND_8032`；`input_parts=R11 47R/1W, D1 US1JW, C4`；`output_parts=D3/D4 US1JW, L1, C8 100uF, R14 1.6K`；`meter_decoupling=C10 100nF`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左下 U2 MP150GJ-Z 离线电源区与中央 U1 VCC_8032/C10

## 接口

### Atom 主控信号映射

ATOM G22 连接 RX，G23 经 R1 1kΩ 连接 Relay，ATOM 3V3/VCC/GND 分别连接控制板 3.3V/VCC/GND；其余 G21/G25/G19/G33 在图中未使用。

- 参数与网络：`G22=RX`；`G23=Relay via R1 1K`；`pin9=3.3V`；`pin3=VCC/5V`；`pin1=GND`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页中右 ATOM 连接器与 RX/R1/Relay/3.3V/VCC/GND

### J3 外部控制 Grove

J3 IO2=SW，IO1 经 R5 1kΩ 连接 Relay，5V=VCC，GND=GND，使外部设备可读取按键网络并驱动继电器控制网络。

- 参数与网络：`connector=J3 GROVE`；`io2=SW`；`io1=Relay via R5 1K`；`power=VCC`；`ground=GND`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页右下 J3 GROVE 与 SW/Relay/R5/VCC/GND

### HLW8032 TX 到 Atom RX 隔离链路

U1 TX 驱动 IC1 EL357N 输入侧，输入 LED 由 VCC_8032 经 R4 470Ω 供电；IC1 输出侧参考 VCC_MCU/GND，经 J1 和低压板 RX 网络连接 ATOM G22。

- 参数与网络：`meter_tx=U1 TX`；`opto=IC1 EL357N(C)(TA)-G`；`input_supply=VCC_8032 via R4 470R`；`output_supply=VCC_MCU via R15 1.6K`；`output_return=GND via R5 3.3K`；`host_rx=J1 -> RX -> ATOM G22`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 U1 TX/R4/IC1/R15/R5/J1; 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页 J1 RX 到 ATOM G22

## GPIO 与控制信号

### 本地 SW 按键输入

SW 由 R3 3.3kΩ 上拉到 3.3V，S1 TS-1157-B-B 按下时将 SW 接 GND，C1 100nF 从 SW 接 GND。

- 参数与网络：`net=SW`；`pullup=R3 3.3K to 3.3V`；`switch=S1 TS-1157-B-B to GND`；`capacitor=C1 100nF to GND`；`active_level=low`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页上中 S1/R3/C1 与 SW/GND/3.3V

### Atom Relay 到继电器线圈驱动

Atom G23 经 R1 1kΩ 形成 Relay 控制，Relay 经 R2 3.3kΩ 驱动 Q1 S8050；Q1 低边节点同时控制 LED1 并通过 J1 连接高压板 K1 线圈的 Relay 端。

- 参数与网络：`host_gpio=G23`；`host_resistor=R1 1K`；`driver=Q1 S8050`；`base_resistor=R2 3.3K`；`indicator=VCC -> R4 3.3K -> LED1 -> Q1`；`coil_net=Relay via J1`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页 ATOM G23/R1、Relay/R2/Q1/LED1/J1; 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 J1 Relay 到 K1 线圈，D2 跨线圈

## 保护电路

### DNP EARTH 焊盘

高压板 P2 为 DNP PAD，连接两个 EARTH 焊盘；当前原理图没有显示它与低压 GND 或 GND_8032 的直接连接。

- 参数与网络：`reference=P2`；`population=DNP`；`nets=EARTH, EARTH`；`direct_ground_connection=false`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左上 P2 DNP PAD 与两处 EARTH

## 关键网络

### 控制地与计量地隔离边界

低压控制板和光耦输出侧使用 GND/VCC_MCU，HLW8032、采样网络和光耦输入侧使用 GND_8032/VCC_8032；两域之间的计量数据只通过 IC1 光耦跨越。

- 参数与网络：`control_domain=GND, VCC/VCC_MCU`；`metering_domain=GND_8032, VCC_8032`；`isolation_component=IC1 EL357N(C)(TA)-G`；`crossing_signal=HLW8032 TX to Atom RX`
- 证据：图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页 PWR1 低压 VCC/GND 与 ATOM/J1; 图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 U1/U2 GND_8032/VCC_8032 与 IC1 两侧

## 模拟电路

### HLW8032 电流采样路径

R1 分流器串联 AC_N_OUT 与 AC_N_IN；两端分别经 R2/R3 1kΩ 连接 U1 I_P/I_N，C1/C2 各 33nF 从差分输入侧接到 GND_8032。

- 参数与网络：`shunt=R1 between AC_N_OUT and AC_N_IN`；`positive_input=R2 1K to U1 I_P`；`negative_input=R3 1K to U1 I_N`；`filters=C1/C2 33nF to GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页左中 AC_N_OUT/R1/AC_N_IN、R2/R3/C1/C2 与 U1 I_P/I_N

### HLW8032 电压采样路径

L_SLP 经 R6/R7/R8/R9 四颗 470kΩ 串联到 U1 V_P，采样节点由 R10 1kΩ 与 C3 100nF 接到 GND_8032。

- 参数与网络：`source=L_SLP`；`series_chain=R6-R9 470K each`；`meter_pin=U1 V_P`；`lower_resistor=R10 1K`；`filter_capacitor=C3 100nF`；`reference=GND_8032`
- 证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页中左 L_SLP/R6-R9/R10/C3 到 U1 V_P

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom Socket 双板系统架构 | `controller_board=asset d75ab747fba6`；`metering_board=asset d7d943bc4ec3`；`interconnect=J1 A1002WR-S-4P`；`control_signals=Relay, RX`；`control_power=VCC/VCC_MCU, GND`；`metering_domain=VCC_8032, GND_8032` |
| 电源 | 低压控制板 AC 到 VCC 电源 | `module=PWR1 RPD5W05E102SR`；`input=AC_L_IN, AC_N_IN`；`output=VCC, GND`；`series_diode=D1 SS34`；`loads=ATOM 5V, J3 VCC, LED1/Q1` |
| 接口 | Atom 主控信号映射 | `G22=RX`；`G23=Relay via R1 1K`；`pin9=3.3V`；`pin3=VCC/5V`；`pin1=GND` |
| GPIO 与控制信号 | 本地 SW 按键输入 | `net=SW`；`pullup=R3 3.3K to 3.3V`；`switch=S1 TS-1157-B-B to GND`；`capacitor=C1 100nF to GND`；`active_level=low` |
| GPIO 与控制信号 | Atom Relay 到继电器线圈驱动 | `host_gpio=G23`；`host_resistor=R1 1K`；`driver=Q1 S8050`；`base_resistor=R2 3.3K`；`indicator=VCC -> R4 3.3K -> LED1 -> Q1`；`coil_net=Relay via J1` |
| 接口 | J3 外部控制 Grove | `connector=J3 GROVE`；`io2=SW`；`io1=Relay via R5 1K`；`power=VCC`；`ground=GND` |
| 电源 | 交流火线保险与继电器切换 | `input=AC_L_IN`；`fuse=2009T15A250V`；`protected_line=L_SLP`；`relay=K1 932-5VDC-SL-AHG`；`output=AC_L_OUT`；`coil=VCC_MCU to Relay`；`flyback=D2 S1MD3` |
| 模拟电路 | HLW8032 电流采样路径 | `shunt=R1 between AC_N_OUT and AC_N_IN`；`positive_input=R2 1K to U1 I_P`；`negative_input=R3 1K to U1 I_N`；`filters=C1/C2 33nF to GND_8032` |
| 模拟电路 | HLW8032 电压采样路径 | `source=L_SLP`；`series_chain=R6-R9 470K each`；`meter_pin=U1 V_P`；`lower_resistor=R10 1K`；`filter_capacitor=C3 100nF`；`reference=GND_8032` |
| 核心器件 | HLW8032 电能计量核心 | `part=HLW8032`；`supply=VCC_8032, GND_8032`；`current_inputs=I_P, I_N`；`voltage_input=V_P`；`telemetry=TX through IC1`；`unconnected=PF, RX` |
| 接口 | HLW8032 TX 到 Atom RX 隔离链路 | `meter_tx=U1 TX`；`opto=IC1 EL357N(C)(TA)-G`；`input_supply=VCC_8032 via R4 470R`；`output_supply=VCC_MCU via R15 1.6K`；`output_return=GND via R5 3.3K`；`host_rx=J1 -> RX -> ATOM G22` |
| 电源 | HLW8032 计量侧电源 | `controller=U2 MP150GJ-Z`；`ac_input=AC_L_IN, AC_N_IN`；`output=VCC_8032, GND_8032`；`input_parts=R11 47R/1W, D1 US1JW, C4`；`output_parts=D3/D4 US1JW, L1, C8 100uF, R14 1.6K`；`meter_decoupling=C10 100nF` |
| 关键网络 | 控制地与计量地隔离边界 | `control_domain=GND, VCC/VCC_MCU`；`metering_domain=GND_8032, VCC_8032`；`isolation_component=IC1 EL357N(C)(TA)-G`；`crossing_signal=HLW8032 TX to Atom RX` |
| 保护电路 | DNP EARTH 焊盘 | `reference=P2`；`population=DNP`；`nets=EARTH, EARTH`；`direct_ground_connection=false` |
| 总线 | 产品正文中的 HLW8032 UART 格式 | `documented_baud=4800bps`；`documented_format=8E1`；`schematic_path=HLW8032 TX -> IC1 -> RX -> G22` |
| 电源 | 产品正文中的继电器和负载额定值 | `documented_ac=100-120V 10A`；`documented_dc=28V 10A`；`documented_recommended_power=<=1000W`；`schematic_relay=K1 932-5VDC-SL-AHG`；`schematic_fuse=15A 250V` |
| 模拟电路 | 产品正文中的计量精度 | `documented_dynamic_range=1000:1`；`documented_active_power_error=0.2%`；`documented_current_error=0.5%`；`documented_voltage_error=0.5%` |

## 待确认事项

- `bus.documented-uart-format`：产品正文给出 HLW8032 UART 4800bps 8E1，但两张原理图只显示 TX 到光耦再到 RX/G22 的物理连接，没有波特率、校验位或帧格式标注。（证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 U1 TX/IC1/J1，图中无 UART 格式; 图 d75ab747fba6 / 第 1 页 / 资源 1 第 1 页 J1 RX 到 ATOM G22）
- `power.documented-relay-load`：产品正文给出 AC 100-120V@10A、DC 28V@10A 和建议负载不超过 1000W，但原理图只标 K1 料号与 15A/250V 保险，无法验证整机额定值、插座规范和使用条件。（证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 AC_L_IN/FUSE/K1/AC_L_OUT，图中无整机额定值表）
- `analog.documented-meter-accuracy`：产品正文给出 1000:1 动态范围、有功功率 0.2% 以及电流/电压 0.5% 误差，但原理图只定义 HLW8032 和采样网络，无法确认校准、容差、负载与温度条件下的整机精度。（证据：图 d7d943bc4ec3 / 第 1 页 / 资源 2 第 1 页 HLW8032、电流分流与电压分压网络，图中无精度条件）
- `review.uart-format`：当前 Atom Socket 所用 HLW8032 数据帧是否确认为 4800bps、8E1？；原因：UART 格式来自产品正文，原理图只能确认单向 TX 隔离链路。
- `review.relay-load-rating`：100-120V@10A、28V@10A 和不超过 1000W 的额定值是否已按 K1、插座、PCB 铜厚、温升和保险配置完成整机认证？；原因：原理图只给继电器和保险料号，无法证明整机安全额定条件。
- `review.meter-accuracy`：产品正文的 0.2%/0.5% 误差和 1000:1 动态范围对应哪些校准、负载、温度与器差条件？；原因：系统级计量精度不能仅由原理图确认，需要 HLW8032 数据手册、采样器件容差和校准测试记录。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d75ab747fba6839907d0caa106c7f55450b37941dc4be724cfae6320d5d90f93` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_01.webp` |
| 2 | 1 | `d7d943bc4ec374357096b395fc6218fc428a99ecdc50c46b6bf89c90637e28f3` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_02.webp` |

---

源文档：`zh_CN/atom/atom_socket.md`

源文档 SHA-256：`18ed767ac9f59f5eee4ca3024371081d2a9e5ab5ef4011e8d3d1d91151622b5a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
