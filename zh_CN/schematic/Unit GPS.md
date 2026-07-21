# Unit GPS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit GPS |
| SKU | U032 |
| 产品 ID | `unit-gps-14a75f276fa6` |
| 源文档 | `zh_CN/unit/gps.md` |

## 概述

Unit GPS（U032）以 M1 GP-02 导航模块为核心，通过 J2 的 TXD1/RXD1 与外部主机进行 UART 通信；M1 还提供 1PPS、VBAT、ON/OFF、NRST、SCL/SDA 和 ANT 引脚。VCC 经 U1 SPX3819M5-L-3-3 生成 +3.3V，为 GP-02 和 U2 MAX2659 供电；BT1 为 VBAT 备份域供电，D1/R3/R4 构成 1PPS 指示支路。M1 ANT 连接 MAX2659 RFOUT，外部 ANT18104 经 C5 47pF、L1 6.8nH 接 MAX2659 RFIN。原理图没有直接标注 AT6558、UART 波特率或 GNSS 性能，因此正文中的芯片、协议和定位指标需结合模块资料或实测确认。

## 检索关键词

`Unit GPS`、`U032`、`GP-02`、`AT6558`、`MAX2659`、`SPX3819M5-L-3-3`、`ANT18104`、`UART_Socket_4P`、`TXD1`、`RXD1`、`UART`、`9600bps`、`1PPS`、`ON/OFF`、`NRST`、`VBAT`、`BT1`、`ANT`、`RFIN`、`RFOUT`、`L1 6.8nH`、`C5 47pF`、`+3.3V`、`VCC`、`BDS`、`GPS`、`GNSS`、`56 channels`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | GP-02 | +3.3V 供电的 GNSS 模块，提供 UART、1PPS、VBAT、控制、I2C 保留脚和 ANT 射频接口 | 图 9dafcf744567 / 第 1 页 / 第 1 页中下部 M1 GP-02，pin1-pin18 的 GND/TXD1/RXD1/1PPS/ON-OFF/VBAT/VCC/NRST/ANT/SCL/SDA/NC |
| U1 | SPX3819M5-L-3-3 | 将输入 VCC 稳压为 GP-02 与 MAX2659 使用的 +3.3V | 图 9dafcf744567 / 第 1 页 / 第 1 页左上 U1 SPX3819M5-L-3-3，IN pin1、EN pin3、GND pin2、BYP/ADJ pin4、OUT pin5 |
| U2 | MAX2659 | +3.3V 供电的 GNSS 射频低噪声放大链路，连接外部天线和 M1 ANT | 图 9dafcf744567 / 第 1 页 / 第 1 页右中 U2 MAX2659，pin3 RFIN、pin6 RFOUT、pin4 VCC、pin5 SHDN、pin1/pin2 GND |
| J2 | UART_Socket_4P | 四针 Grove UART 接口，交叉引出模块 TXD1/RXD1，并提供 VCC/GND | 图 9dafcf744567 / 第 1 页 / 第 1 页左中 J2 UART_Socket_4P，pin1 RX/TXD1、pin2 TX/RXD1、pin3 VCC、pin4 GND |
| BT1 | Battery | M1 VBAT 备用电源域，配合 C8/C9 对地去耦 | 图 9dafcf744567 / 第 1 页 / 第 1 页左下 BT1 Battery 连接 M1 pin6 VBAT，C8 10uF/C9 100nF 接 GND |
| D1,R3,R4 | 0603 / 1KΩ / 10KΩ | M1 1PPS 输出的 LED 指示与 +3.3V 上拉支路 | 图 9dafcf744567 / 第 1 页 / 第 1 页 M1 左侧 pin4 1PPS 网络，R4 10KΩ 到 +3.3V，R3 1KΩ 与 D1 0603 到 GND |
| Antenna,L1,C5 | ANT18104 / 6.8nH 5% / 47pF | MAX2659 RFIN 至外部天线的串联匹配/耦合链路 | 图 9dafcf744567 / 第 1 页 / 第 1 页右上 U2 RFIN pin3 经 L1 6.8nH 5%、C5 47pF 到 ANT18104 |
| C1,C2,C3,C4,C6,C7,C8,C9 | 10uF / 100uF / 470pF / 100nF / 33nF | LDO、MAX2659 与 VBAT 电源域的输入、输出、旁路和去耦电容 | 图 9dafcf744567 / 第 1 页 / 第 1 页 C1 10uF、C2 100uF/6.3V、C3 470pF、C4/C6/C9 100nF、C7 33nF、C8 10uF |

## 系统结构

### Unit GPS 系统架构

M1 GP-02 通过 J2 的 TXD1/RXD1 与外部主机通信，1PPS 驱动指示支路，VBAT 接备用电池，ANT 经 U2 MAX2659 连接外部天线。U1 从 VCC 生成 +3.3V。完整单页没有独立 MCU、外部存储器、板级晶振、USB、充电器或数字总线连接器。

- 参数与网络：`gnss_module=M1 GP-02`；`host_interface=J2 UART TXD1/RXD1`；`timing=1PPS`；`backup=BT1 -> VBAT`；`rf_amplifier=U2 MAX2659`；`antenna=ANT18104`；`regulator=U1 SPX3819M5-L-3-3`；`external_storage=null`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页完整单页，U1/U2/M1/J2/BT1/天线与所有无源器件

## 核心器件

### GP-02 模块引脚映射

M1 pin1 GND、pin2 TXD1、pin3 RXD1、pin4 1PPS、pin5 ON/OFF、pin6 VBAT、pin7 NC、pin8 VCC、pin9 NRST、pin10 GND、pin11 ANT、pin12 GND、pin13 NC、pin14 VCC、pin15 NC、pin16 SDA、pin17 SCL、pin18 NC。

- 参数与网络：`pin1=GND`；`pin2=TXD1`；`pin3=RXD1`；`pin4=1PPS`；`pin5=ON/OFF`；`pin6=VBAT`；`pin7=NC`；`pin8=VCC +3.3V`；`pin9=NRST`；`pin10=GND`；`pin11=ANT`；`pin12=GND`；`pin13=NC`；`pin14=VCC +3.3V`；`pin15=NC`；`pin16=SDA`；`pin17=SCL`；`pin18=NC`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页中下 M1 GP-02 pin1-pin18 全部标注

## 电源

### VCC 至 +3.3V LDO

U1 SPX3819M5-L-3-3 IN pin1 与 EN pin3 一同接 VCC，OUT pin5 输出 +3.3V，GND pin2 接地，BYP/ADJ pin4 经 C3 470pF 接 GND。C1 10uF 位于 VCC 输入侧，C4 100nF 与 C2 100uF(107)±10% 6.3V 位于 +3.3V 输出侧。

- 参数与网络：`regulator=U1 SPX3819M5-L-3-3`；`input=pin1 VCC`；`enable=pin3 tied VCC`；`output=pin5 +3.3V`；`bypass=pin4 C3 470pF to GND`；`input_cap=C1 10uF`；`output_caps=C4 100nF,C2 100uF/6.3V`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页左上 U1/C1-C4 与 VCC/+3.3V

### GP-02 VBAT 备用电源

M1 VBAT pin6 连接 BT1 Battery 正端，并由 C8 10uF 与 C9 100nF 对地去耦；BT1 负端接 GND。原理图没有标电池化学体系、额定电压、容量、可充电性或充电路径。

- 参数与网络：`module_pin=M1 pin6 VBAT`；`battery=BT1`；`ground=BT1 negative GND`；`caps=C8 10uF,C9 100nF`；`chemistry=null`；`voltage=null`；`capacity=null`；`charger=null`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页左下 M1 pin6 VBAT、BT1、C8/C9

## 接口

### J2 Grove UART 接口

J2 UART_Socket_4P pin1 标 RX 并连接模块 TXD1，pin2 标 TX 并连接模块 RXD1，pin3 VCC 接输入 VCC，pin4 GND 接地；因此 UART 数据线按外部主机视角交叉连接。

- 参数与网络：`connector=J2 UART_Socket_4P`；`pin1=RX <- M1 TXD1 output`；`pin2=TX -> M1 RXD1 input`；`pin3=VCC power input`；`pin4=GND`；`direction_reference=external host`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页左中 J2 pin1-pin4 与 M1 TXD1/RXD1 同名网络

## 总线

### GP-02 UART 直连路径

M1 TXD1 pin2 直接连接 J2 RX pin1，M1 RXD1 pin3 直接连接 J2 TX pin2；页面没有串联电阻、电平转换器、收发器、ESD 阵列或流控线。

- 参数与网络：`transmit=M1 pin2 TXD1 -> J2 pin1 RX`；`receive=J2 pin2 TX -> M1 pin3 RXD1`；`level_shifter=null`；`series_resistors=null`；`flow_control=null`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页 J2-M1 TXD1/RXD1 两条完整路径

## GPIO 与控制信号

### 1PPS 指示网络

M1 1PPS pin4 连接 R4 10KΩ 到 +3.3V，并通过 R3 1KΩ 与 D1 0603 LED 接 GND；该 1PPS 信号未引到 J2。

- 参数与网络：`source=M1 pin4 1PPS`；`pullup=R4 10KΩ to +3.3V`；`indicator=R3 1KΩ + D1 0603 to GND`；`external_connector=null`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1 pin4 1PPS 左侧 R4/R3/D1 网络

### 未连接控制与辅助引脚

M1 ON/OFF pin5、NRST pin9、SDA pin16、SCL pin17 在本页均只有未连接短线；NC pins7/13/15/18 也未连接。板上没有开关、复位电路或 I2C 接口使用这些引脚。

- 参数与网络：`on_off=pin5 NC`；`reset=pin9 NRST NC`；`sda=pin16 NC`；`scl=pin17 NC`；`declared_nc=pins7/13/15/18`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1 GP-02 pin5/pin7/pin9/pin13/pin15-pin18 未连接标线

## 保护电路

### UART、电源与天线保护配置

完整单页未显示 J2 VCC/UART 的 TVS、保险丝、反接保护或串联限流，也未显示天线口 ESD/浪涌保护；L1/C5 属于射频匹配链路。

- 参数与网络：`uart_esd=null`；`power_fuse=null`；`reverse_polarity=null`；`antenna_esd=null`；`rf_matching=L1 6.8nH,C5 47pF`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页完整 J2、电源与天线路径

## 关键网络

### 关键网络索引

VCC 连接 J2 pin3 与 U1 IN/EN；+3.3V 连接 U1 OUT、M1 VCC pins8/14、U2 VCC/SHDN、R4 与去耦；TXD1/RXD1 连接 M1 与 J2；VBAT 连接 M1/BT1/C8/C9；1PPS 连接 M1/R4/R3/D1；ANT 连接 M1 与 MAX2659 RFOUT，RFIN 经 L1/C5 到 ANT18104。

- 参数与网络：`VCC=J2 pin3,U1 IN/EN,C1`；`+3.3V=U1 OUT,M1 pins8/14,U2 pins4/5,R4,C2/C4/C6/C7`；`UART=TXD1,RXD1`；`backup=VBAT,BT1,C8,C9`；`timing=1PPS,R4,R3,D1`；`rf=ANT,RFOUT,RFIN,L1,C5,ANT18104`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页全部 VCC/+3.3V/TXD1/RXD1/VBAT/1PPS/ANT 网络

## 射频

### MAX2659 天线放大链路

M1 ANT pin11 连接 U2 MAX2659 RFOUT pin6；U2 RFIN pin3 经 L1 6.8nH 5% 和 C5 47pF 串联连接 ANT18104。U2 VCC pin4 与 SHDN pin5 接 +3.3V，GND pins1/2 接地，C6 100nF/C7 33nF 从 +3.3V 接 GND。

- 参数与网络：`module=M1 pin11 ANT`；`amplifier_output=U2 pin6 RFOUT`；`amplifier_input=U2 pin3 RFIN`；`matching=L1 6.8nH 5%,C5 47pF series`；`antenna=ANT18104`；`supply=pin4 VCC +3.3V`；`enable=pin5 SHDN +3.3V`；`decoupling=C6 100nF,C7 33nF`
- 证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1 ANT、U2 MAX2659、L1/C5/ANT18104 与 C6/C7

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit GPS 系统架构 | `gnss_module=M1 GP-02`；`host_interface=J2 UART TXD1/RXD1`；`timing=1PPS`；`backup=BT1 -> VBAT`；`rf_amplifier=U2 MAX2659`；`antenna=ANT18104`；`regulator=U1 SPX3819M5-L-3-3`；`external_storage=null` |
| 核心器件 | GP-02 模块引脚映射 | `pin1=GND`；`pin2=TXD1`；`pin3=RXD1`；`pin4=1PPS`；`pin5=ON/OFF`；`pin6=VBAT`；`pin7=NC`；`pin8=VCC +3.3V`；`pin9=NRST`；`pin10=GND`；`pin11=ANT`；`pin12=GND`；`pin13=NC`；`pin14=VCC +3.3V`；`pin15=NC`；`pin16=SDA`；`pin17=SCL`；`pin18=NC` |
| 电源 | VCC 至 +3.3V LDO | `regulator=U1 SPX3819M5-L-3-3`；`input=pin1 VCC`；`enable=pin3 tied VCC`；`output=pin5 +3.3V`；`bypass=pin4 C3 470pF to GND`；`input_cap=C1 10uF`；`output_caps=C4 100nF,C2 100uF/6.3V` |
| 电源 | GP-02 VBAT 备用电源 | `module_pin=M1 pin6 VBAT`；`battery=BT1`；`ground=BT1 negative GND`；`caps=C8 10uF,C9 100nF`；`chemistry=null`；`voltage=null`；`capacity=null`；`charger=null` |
| 接口 | J2 Grove UART 接口 | `connector=J2 UART_Socket_4P`；`pin1=RX <- M1 TXD1 output`；`pin2=TX -> M1 RXD1 input`；`pin3=VCC power input`；`pin4=GND`；`direction_reference=external host` |
| 总线 | GP-02 UART 直连路径 | `transmit=M1 pin2 TXD1 -> J2 pin1 RX`；`receive=J2 pin2 TX -> M1 pin3 RXD1`；`level_shifter=null`；`series_resistors=null`；`flow_control=null` |
| GPIO 与控制信号 | 1PPS 指示网络 | `source=M1 pin4 1PPS`；`pullup=R4 10KΩ to +3.3V`；`indicator=R3 1KΩ + D1 0603 to GND`；`external_connector=null` |
| 射频 | MAX2659 天线放大链路 | `module=M1 pin11 ANT`；`amplifier_output=U2 pin6 RFOUT`；`amplifier_input=U2 pin3 RFIN`；`matching=L1 6.8nH 5%,C5 47pF series`；`antenna=ANT18104`；`supply=pin4 VCC +3.3V`；`enable=pin5 SHDN +3.3V`；`decoupling=C6 100nF,C7 33nF` |
| GPIO 与控制信号 | 未连接控制与辅助引脚 | `on_off=pin5 NC`；`reset=pin9 NRST NC`；`sda=pin16 NC`；`scl=pin17 NC`；`declared_nc=pins7/13/15/18` |
| 关键网络 | 关键网络索引 | `VCC=J2 pin3,U1 IN/EN,C1`；`+3.3V=U1 OUT,M1 pins8/14,U2 pins4/5,R4,C2/C4/C6/C7`；`UART=TXD1,RXD1`；`backup=VBAT,BT1,C8,C9`；`timing=1PPS,R4,R3,D1`；`rf=ANT,RFOUT,RFIN,L1,C5,ANT18104` |
| 保护电路 | UART、电源与天线保护配置 | `uart_esd=null`；`power_fuse=null`；`reverse_polarity=null`；`antenna_esd=null`；`rf_matching=L1 6.8nH,C5 47pF` |
| 电源 | 正文中的 Grove 5V 输入 | `documented_voltage=5V`；`schematic_net=VCC`；`connector=J2 pin3`；`regulator=U1 SPX3819M5-L-3-3`；`uart_logic_level=null` |
| 核心器件 | 正文中的 AT6558 导航芯片 | `module=M1 GP-02`；`documented_internal_chip=AT6558`；`internal_schematic=null`；`internal_flash=null`；`internal_clock=null` |
| 总线 | 正文中的 UART 参数 | `documented_baud=9600bps`；`documented_start_bits=1`；`documented_stop_bits=1`；`documented_parity=none`；`data_bits=null`；`logic_level=null`；`protocol=null` |
| 射频 | 正文中的 GNSS 系统与定位性能 | `documented_systems=BDS,GPS,multi-GNSS`；`documented_channels=56`；`documented_accuracy=2.5m`；`documented_update_rate=1-10Hz`；`documented_max_speed=515m/s`；`documented_max_acceleration=<=4g`；`documented_sensitivity=tracking -162dBm,capture -148dBm,cold -146dBm`；`documented_startup=cold 35s,warm 32s,hot 1s`；`schematic_performance_table=null` |

## 待确认事项

- `power.documented-five-volt-input`：产品正文 HY2.0-4P 表将红线标为 5V；原理图只把 J2 pin3 与 U1 输入网络标为 VCC，没有直接标注 5V 数值、范围或 UART 逻辑电平。（证据：图 9dafcf744567 / 第 1 页 / 第 1 页 J2 pin3 VCC 与 U1 输入，整页无 5V 文字）
- `component.documented-at6558`：产品正文称 GP-02 内部集成 AT6558；原理图板级模块只标 M1 GP-02，没有展开模块内部芯片、Flash、时钟、电源、协议处理或 AT6558 位号，因此无法从本页直接确认内部实现。（证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1 仅标 GP-02 模块接口，无 AT6558 文字）
- `bus.documented-uart-settings`：产品正文列出默认 9600bps、1 个起始位、1 个停止位、无校验；原理图只显示 TXD1/RXD1 电气连接，没有波特率、数据位、帧格式、电平标准或协议报文。（证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1 TXD1/RXD1 与 J2，图中无 UART 参数）
- `rf.documented-gnss-performance`：正文称支持 BDS/GPS 及多系统联合定位、56 通道、2.5m 精度、1-10Hz 更新、最大速度 515m/s、最大加速度 <=4g，并列跟踪 -162dBm、捕捉 -148dBm、冷启动 -146dBm及冷/温/热启动 35s/32s/1s；原理图只确认 GP-02、MAX2659 和天线链路，没有任何这些系统级性能或测试条件。（证据：图 9dafcf744567 / 第 1 页 / 第 1 页 M1/U2/L1/C5/ANT18104，图中无 GNSS 性能参数）
- `review.input-uart-voltage`：请用当前 U032 接口规范或实板测量确认 J2 VCC 是否为 5V、允许范围，以及 TXD1/RXD1 的逻辑电平兼容边界。；原因：原理图只标 VCC，且 UART 直接连接没有电平转换。
- `review.gp02-internals`：请用 GP-02 BOM/内部原理图或模组规格确认量产版本内部是否为 AT6558 及其存储、时钟和固件配置。；原因：板级原理图只显示 GP-02 模块接口。
- `review.uart-settings`：请用 GP-02 协议资料或串口实测确认默认 9600bps、数据位、1 个起始位、1 个停止位、无校验及消息格式。；原因：原理图不包含 UART 配置。
- `review.gnss-performance`：请以当前 GP-02/AT6558/MAX2659/天线组合及明确测试条件确认卫星系统、通道数、精度、更新率、动态性能、灵敏度和启动时间。；原因：这些性能值未印在原理图上。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9dafcf7445679fe463f133b891d226a1fa74d9c1fa052f46e19b3987f3bc7fa4` | `https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_sch_01.webp` |

---

源文档：`zh_CN/unit/gps.md`

源文档 SHA-256：`747ed3748ca3d0aee2c285d2f82a8384b8b2c90ebe52b1375ddd3f0ec46a3eb2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
