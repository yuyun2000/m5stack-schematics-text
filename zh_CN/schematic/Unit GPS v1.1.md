# Unit GPS v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit GPS v1.1 |
| SKU | U032-V11 |
| 产品 ID | `unit-gps-v1-1-798281308d46` |
| 源文档 | `zh_CN/unit/Unit-GPS v1.1.md` |

## 概述

当前 Unit GPS v1.1 资源页以 M1 GP-02 为 GNSS 模组，通过 J2 UART 的 TXD1/RXD1 与主机通信，并以 1PPS 驱动板载 LED、BT1 维持 VBAT。VCC 经 U1 SPX3819M5-L-3-3 生成 +3.3V，供 GP-02 与 U2 MAX2659；J1 ANT181804 经 C5 470pF、L1 6.8nH 和 MAX2659 连接 M1 ANT。该页图框仍为 UNIT-GPS、V1.0、2018-10-16，且没有 ATGM336H-6N 或 AT6668 标识，因此它与 U032-V11 正文的模组、多模 GNSS、UART 和性能声明存在关键版本冲突。

## 检索关键词

`Unit GPS v1.1`、`U032-V11`、`GP-02`、`ATGM336H-6N`、`AT6668`、`MAX2659`、`SPX3819M5-L-3-3`、`ANT181804`、`UART_Socket_4P`、`TXD1`、`RXD1`、`UART`、`115200bps 8N1`、`1PPS`、`ON/OFF`、`NRST`、`VBAT`、`BT1 Battery`、`ANT`、`RFIN`、`RFOUT`、`L1 6.8nH`、`C5 470pF`、`+3.3V`、`VCC`、`GPS`、`QZSS`、`BD2`、`BD3`、`GALILEO`、`GLONASS`、`NMEA0183 4.1`、`10Hz`、`50 channels`、`UNIT-GPS V1.0`、`ceramic antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | GP-02 | GNSS 模组，提供 UART、1PPS、ON/OFF、VBAT、NRST、ANT、SCL/SDA 与电源脚 | 图 782a31cf2827 / 第 1 页 / 第1页网格 B2-C2，M1 GP-02 pins1-18 |
| U1 | SPX3819M5-L-3-3 | 将输入 VCC 稳压为 +3.3V 的低压差稳压器 | 图 782a31cf2827 / 第 1 页 / 第1页网格 A1-A2，U1 SPX3819M5-L-3-3 pins1-5 |
| U2 | MAX2659 | 3.3V 供电并常态使能的 GNSS 射频低噪声放大器，连接陶瓷天线与 M1 ANT | 图 782a31cf2827 / 第 1 页 / 第1页网格 B3，U2 MAX2659 RFIN/RFOUT/VCC/SHDN/GND |
| J2 | UART_Socket_4P | 四针 Grove UART 与供电接口 | 图 782a31cf2827 / 第 1 页 / 第1页网格 B1，J2 UART_Socket_4P pins1-4 |
| J1 | ANT181804 | 板载 GNSS 陶瓷天线，经 C5/L1 接 MAX2659 RFIN | 图 782a31cf2827 / 第 1 页 / 第1页网格 B3-B4，J1 ANT181804、C5、L1 与 U2 RFIN |
| BT1 | Battery | 连接 M1 VBAT 的 GNSS 备用电源 | 图 782a31cf2827 / 第 1 页 / 第1页网格 C1-C2，BT1 Battery 到 M1 pin6 VBAT |
| D1/R3 | 0603 / 1KΩ | M1 1PPS 到 GND 的 LED 指示支路 | 图 782a31cf2827 / 第 1 页 / 第1页网格 C1-B2，M1 pin4 1PPS、R3 1KΩ、D1 0603、GND |
| R4 | 10KΩ | 将 M1 ON/OFF pin5 上拉至 +3.3V | 图 782a31cf2827 / 第 1 页 / 第1页网格 B1-B2，R4 10KΩ、+3.3V 与 M1 ON/OFF pin5 |
| L1/C5 | 6.8nH 5% / 470pF | ANT181804 到 MAX2659 RFIN 的串联射频匹配/耦合链 | 图 782a31cf2827 / 第 1 页 / 第1页网格 B3-B4，J1-C5-L1-U2 RFIN |
| C1/C2/C3/C4 | 10uF / 100uF(107)±10% 6.3V / 470pF / 100nF | U1 输入、输出与 BYP/ADJ 的滤波和旁路电容 | 图 782a31cf2827 / 第 1 页 / 第1页网格 A1-A2，U1 周围 C1-C4 |
| C6/C7/C8/C9 | 100nF / 33nF / 10uF / 100nF | MAX2659 主电源及 GP-02 VCC/VBAT 域的去耦电容 | 图 782a31cf2827 / 第 1 页 / 第1页网格 B2-C3，C6/C7 与 U2、C8/C9 与 M1/BT1 |

## 系统结构

### Unit GPS v1.1 当前资源架构

当前页由 M1 GP-02、J2 UART、U1 3.3V LDO、BT1 备用电池、1PPS LED，以及 J1 ANT181804/U2 MAX2659 射频链构成；没有独立 MCU 或外部存储器。

- 参数与网络：`gnss_module=M1 GP-02`；`host=J2 UART_Socket_4P`；`regulator=U1 SPX3819M5-L-3-3`；`backup=BT1 -> VBAT`；`timing=1PPS -> R3/D1`；`rf=J1 ANT181804 -> U2 MAX2659 -> M1 ANT`；`mcu=not shown`；`storage=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页完整单页 U1/U2/M1/J1/J2/BT1

## 核心器件

### M1 GP-02 针脚

M1 pins1-9 为 GND、TXD1、RXD1、1PPS、ON/OFF、VBAT、NC、VCC、NRST；pins10-18 为 GND、ANT、GND、NC、VCC_RF、NC、SDA、SCL、NC。

- 参数与网络：`pin1=GND`；`pin2=TXD1`；`pin3=RXD1`；`pin4=1PPS`；`pin5=ON/OFF`；`pin6=VBAT`；`pin7=NC`；`pin8=VCC / +3.3V`；`pin9=NRST`；`pin10=GND`；`pin11=ANT`；`pin12=GND`；`pin13=NC`；`pin14=VCC_RF`；`pin15=NC`；`pin16=SDA`；`pin17=SCL`；`pin18=NC`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 B2-C2，M1 GP-02 pins1-18

## 电源

### VCC 到 +3.3V LDO

U1 IN pin1 与 EN pin3 接 VCC，OUT pin5 输出 +3.3V，GND pin2 接地，BYP/ADJ pin4 经 C3 470pF 接地；C1 10uF 位于输入，C4 100nF/C2 100uF 位于输出。

- 参数与网络：`regulator=U1 SPX3819M5-L-3-3`；`input=pin1 IN / VCC`；`enable=pin3 EN / VCC`；`output=pin5 OUT / +3.3V`；`ground=pin2`；`bypass=pin4 / C3 470pF`；`input_cap=C1 10uF`；`output_caps=C4 100nF; C2 100uF 6.3V`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 A1-A2，U1/C1-C4/VCC/+3.3V

### GP-02 主电源

M1 VCC pin8 接 +3.3V，并由 C8 10uF/C9 100nF 对地去耦；M1 VCC_RF pin14 在本页未连接。

- 参数与网络：`module=M1 GP-02`；`main_supply=pin8 VCC / +3.3V`；`decoupling=C8 10uF; C9 100nF`；`vcc_rf_pin=pin14 unconnected`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 C2，M1 pin8/C8/C9/+3.3V 与 pin14 VCC_RF

### GP-02 VBAT 备用域

M1 VBAT pin6 接 BT1 Battery 正端，BT1 负端接 GND；页面未标电池化学体系、额定电压、容量、可充电性或充电路径。

- 参数与网络：`module_pin=M1 pin6 VBAT`；`battery=BT1 Battery`；`negative=GND`；`chemistry=not shown`；`voltage=not shown`；`capacity=not shown`；`charger=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 C1-C2，M1 VBAT/BT1/GND

### MAX2659 电源去耦

U2 VCC/SHDN 的 +3.3V 节点配置 C6 100nF 与 C7 33nF 对地。

- 参数与网络：`load=U2 MAX2659 pins4/5`；`rail=+3.3V`；`capacitors=C6 100nF; C7 33nF`；`return=GND`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 B2-B3，U2/C6/C7/+3.3V

## 接口

### J2 Grove UART 针脚

J2 pin1 标 RX 并接 M1 TXD1 pin2，pin2 标 TX 并接 M1 RXD1 pin3，pin3 接 VCC，pin4 接 GND。

- 参数与网络：`connector=J2 UART_Socket_4P`；`pin1=RX <- M1 TXD1`；`pin2=TX -> M1 RXD1`；`pin3=VCC`；`pin4=GND`；`direction_reference=external host`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 B1-B2，J2 pins1-4 与 M1 TXD1/RXD1

## 总线

### GP-02 UART 路由

M1 TXD1/RXD1 直接连接 J2 RX/TX；页面未显示串联电阻、电平转换、ESD、硬件流控或收发器。

- 参数与网络：`transmit=M1 pin2 TXD1 -> J2 pin1 RX`；`receive=J2 pin2 TX -> M1 pin3 RXD1`；`series_resistors=not shown`；`level_shifter=not shown`；`flow_control=not shown`；`esd=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页 J2 与 M1 之间 TXD1/RXD1 完整直连路径

## GPIO 与控制信号

### 1PPS LED

M1 1PPS pin4 经 R3 1KΩ和 D1 0603 LED 接 GND，该信号未引到 J2。

- 参数与网络：`source=M1 pin4 1PPS`；`series=R3 1KΩ`；`indicator=D1 0603`；`return=GND`；`external_breakout=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 C1-B2，M1 pin4/R3/D1/GND

### ON/OFF 控制

M1 ON/OFF pin5 通过 R4 10KΩ上拉到 +3.3V，未连接外部开关或 J2。

- 参数与网络：`module_pin=M1 pin5 ON/OFF`；`pullup=R4 10KΩ to +3.3V`；`switch=not shown`；`external_breakout=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 B1-B2，R4 与 M1 ON/OFF pin5

### 未连接的 GP-02 引脚

M1 NRST pin9、VCC_RF pin14、SDA pin16、SCL pin17 以及 NC pins7/13/15/18 在本页未连接；没有复位按键或 I2C 接口。

- 参数与网络：`nrst=pin9 unconnected`；`vcc_rf=pin14 unconnected`；`sda=pin16 unconnected`；`scl=pin17 unconnected`；`nc=pins7,13,15,18`；`reset_switch=not shown`；`i2c_connector=not shown`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页 M1 GP-02 未连接短线与 NC 标记

## 保护电路

### 外部接口保护

J2 VCC/UART 与 J1 天线链路未显示保险丝、反接保护、TVS 或 ESD 器件；L1/C5 为串联射频匹配/耦合元件。

- 参数与网络：`power_fuse=not shown`；`reverse_protection=not shown`；`uart_esd=not shown`；`antenna_esd=not shown`；`rf_elements=L1 6.8nH; C5 470pF`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页完整 J2、电源与天线路径

## 射频

### 陶瓷天线与 MAX2659 链路

J1 ANT181804 经 C5 470pF 和 L1 6.8nH 5% 串联到 U2 RFIN pin3；U2 RFOUT pin6 接 M1 ANT pin11。U2 VCC pin4 与 SHDN pin5 接 +3.3V，GND pins1/2 接地。

- 参数与网络：`antenna=J1 ANT181804`；`coupling=C5 470pF`；`inductor=L1 6.8nH 5%`；`lna_input=U2 pin3 RFIN`；`lna_output=U2 pin6 RFOUT -> M1 pin11 ANT`；`supply=U2 pin4 +3.3V`；`enable=U2 pin5 SHDN / +3.3V`；`ground=U2 pins1,2`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 B2-B4，M1 ANT/U2/L1/C5/J1

## 其他事实

### 当前资源图框版本

图框标注 Project Title UNIT-GPS.PrjPCB、Sheet Title UNIT-GPS.SchDoc、Revised V1.0、Date 10/16/2018、Sheet 1 of 1。

- 参数与网络：`project=UNIT-GPS.PrjPCB`；`sheet_title=UNIT-GPS.SchDoc`；`revision=V1.0`；`date=10/16/2018`；`sheet=1 of 1`
- 证据：图 782a31cf2827 / 第 1 页 / 第1页网格 D3-D4 右下图框

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit GPS v1.1 当前资源架构 | `gnss_module=M1 GP-02`；`host=J2 UART_Socket_4P`；`regulator=U1 SPX3819M5-L-3-3`；`backup=BT1 -> VBAT`；`timing=1PPS -> R3/D1`；`rf=J1 ANT181804 -> U2 MAX2659 -> M1 ANT`；`mcu=not shown`；`storage=not shown` |
| 核心器件 | M1 GP-02 针脚 | `pin1=GND`；`pin2=TXD1`；`pin3=RXD1`；`pin4=1PPS`；`pin5=ON/OFF`；`pin6=VBAT`；`pin7=NC`；`pin8=VCC / +3.3V`；`pin9=NRST`；`pin10=GND`；`pin11=ANT`；`pin12=GND`；`pin13=NC`；`pin14=VCC_RF`；`pin15=NC`；`pin16=SDA`；`pin17=SCL`；`pin18=NC` |
| 电源 | VCC 到 +3.3V LDO | `regulator=U1 SPX3819M5-L-3-3`；`input=pin1 IN / VCC`；`enable=pin3 EN / VCC`；`output=pin5 OUT / +3.3V`；`ground=pin2`；`bypass=pin4 / C3 470pF`；`input_cap=C1 10uF`；`output_caps=C4 100nF; C2 100uF 6.3V` |
| 电源 | GP-02 主电源 | `module=M1 GP-02`；`main_supply=pin8 VCC / +3.3V`；`decoupling=C8 10uF; C9 100nF`；`vcc_rf_pin=pin14 unconnected` |
| 电源 | GP-02 VBAT 备用域 | `module_pin=M1 pin6 VBAT`；`battery=BT1 Battery`；`negative=GND`；`chemistry=not shown`；`voltage=not shown`；`capacity=not shown`；`charger=not shown` |
| 接口 | J2 Grove UART 针脚 | `connector=J2 UART_Socket_4P`；`pin1=RX <- M1 TXD1`；`pin2=TX -> M1 RXD1`；`pin3=VCC`；`pin4=GND`；`direction_reference=external host` |
| 总线 | GP-02 UART 路由 | `transmit=M1 pin2 TXD1 -> J2 pin1 RX`；`receive=J2 pin2 TX -> M1 pin3 RXD1`；`series_resistors=not shown`；`level_shifter=not shown`；`flow_control=not shown`；`esd=not shown` |
| GPIO 与控制信号 | 1PPS LED | `source=M1 pin4 1PPS`；`series=R3 1KΩ`；`indicator=D1 0603`；`return=GND`；`external_breakout=not shown` |
| GPIO 与控制信号 | ON/OFF 控制 | `module_pin=M1 pin5 ON/OFF`；`pullup=R4 10KΩ to +3.3V`；`switch=not shown`；`external_breakout=not shown` |
| 射频 | 陶瓷天线与 MAX2659 链路 | `antenna=J1 ANT181804`；`coupling=C5 470pF`；`inductor=L1 6.8nH 5%`；`lna_input=U2 pin3 RFIN`；`lna_output=U2 pin6 RFOUT -> M1 pin11 ANT`；`supply=U2 pin4 +3.3V`；`enable=U2 pin5 SHDN / +3.3V`；`ground=U2 pins1,2` |
| 电源 | MAX2659 电源去耦 | `load=U2 MAX2659 pins4/5`；`rail=+3.3V`；`capacitors=C6 100nF; C7 33nF`；`return=GND` |
| GPIO 与控制信号 | 未连接的 GP-02 引脚 | `nrst=pin9 unconnected`；`vcc_rf=pin14 unconnected`；`sda=pin16 unconnected`；`scl=pin17 unconnected`；`nc=pins7,13,15,18`；`reset_switch=not shown`；`i2c_connector=not shown` |
| 保护电路 | 外部接口保护 | `power_fuse=not shown`；`reverse_protection=not shown`；`uart_esd=not shown`；`antenna_esd=not shown`；`rf_elements=L1 6.8nH; C5 470pF` |
| 其他事实 | 当前资源图框版本 | `project=UNIT-GPS.PrjPCB`；`sheet_title=UNIT-GPS.SchDoc`；`revision=V1.0`；`date=10/16/2018`；`sheet=1 of 1` |
| 核心器件 | v1.1 模组与 SoC 身份 | `document_module=ATGM336H-6N`；`document_soc=AT6668`；`schematic_module=GP-02`；`schematic_revision=V1.0`；`product_sku=U032-V11`；`mapping=not confirmed` |
| 电源 | Grove 5V 与 UART 电平 | `document_supply=5V`；`schematic_net=VCC`；`connector=J2 pin3`；`uart_level=not shown`；`input_range=not shown` |
| 总线 | 默认 UART 参数 | `document_baud=115200bps`；`document_frame=8N1`；`schematic_baud=not shown`；`schematic_frame=not shown`；`flow_control=not shown` |
| 射频 | 多系统多频 GNSS 支持 | `document_systems=GPS; QZSS; BD2; BD3; GALILEO; GLONASS`；`document_frequencies=B1I; B1C; L1; E1; R1`；`schematic_systems=not shown`；`schematic_frequencies=not shown` |
| 射频 | 通道、精度、更新率、灵敏度与启动时间 | `document_channels=50`；`document_accuracy=<1.5m CEP50`；`document_update=10Hz max`；`document_sensitivity=tracking -162dBm; acquisition -160dBm; cold -148dBm`；`document_startup=cold 23s; hot 1s`；`schematic_performance=not shown` |
| 总线 | NMEA0183 4.1 协议 | `document_protocol=NMEA0183 4.1`；`firmware=not shown`；`sentences=not shown`；`configuration=not shown` |
| 电源 | 整机功耗 | `document_consumption=DC 5V/31.64mA`；`measurement_point=not shown`；`gnss_state=not shown`；`rf_conditions=not shown`；`lna_state=U2 SHDN tied +3.3V in schematic` |

## 待确认事项

- `component.v11-module-identity`：正文称 ATGM336H-6N 模组内含 AT6668，但当前资源 M1 只标 GP-02，图框又为 UNIT-GPS V1.0；本页无法证明 U032-V11 实装模组或内部 SoC。（证据：图 782a31cf2827 / 第 1 页 / 第1页 M1 GP-02 与右下 UNIT-GPS V1.0 图框）
- `power.documented-five-volt`：正文管脚表称 J2 供电为 5V；原理图只标 VCC，且 TXD1/RXD1 直连，没有标输入范围或 UART 逻辑电平。（证据：图 782a31cf2827 / 第 1 页 / 第1页 J2 VCC/TXD1/RXD1 与 U1/M1）
- `bus.documented-uart-settings`：正文称默认 115200bps@8N1；原理图只显示 TXD1/RXD1，未标波特率、数据位、校验、停止位或消息格式。（证据：图 782a31cf2827 / 第 1 页 / 第1页 M1 TXD1/RXD1 与 J2，无 UART 参数）
- `rf.documented-constellations`：正文列 GPS/QZSS/BD2/BD3/GALILEO/GLONASS 及 B1I/B1C/L1/E1/R1 频点；当前页仅显示 GP-02、MAX2659 和陶瓷天线，没有卫星系统或频点表。（证据：图 782a31cf2827 / 第 1 页 / 第1页 M1/U2/J1 RF 链，无 GNSS 系统表）
- `rf.documented-performance`：正文给出 50通道、<1.5m CEP50、最大10Hz、跟踪-162dBm/捕捉-160dBm/冷启动-148dBm及冷23s/热1s；原理图没有这些性能或测试条件。（证据：图 782a31cf2827 / 第 1 页 / 第1页 M1 GP-02/MAX2659/ANT181804，无性能字段）
- `bus.documented-nmea`：正文声明 NMEA0183 4.1；原理图没有固件、消息句型、协议版本或配置接口信息。（证据：图 782a31cf2827 / 第 1 页 / 第1页 UART 电气路径，无协议注记）
- `power.documented-consumption`：正文给出 DC 5V/31.64mA；原理图没有测量点、GNSS状态、卫星条件、LNA状态或测试方法。（证据：图 782a31cf2827 / 第 1 页 / 第1页 J2 VCC/U1/M1/U2 电源链，无电流数据）
- `review.v11-module-identity`：请用 U032-V11 专用原理图、BOM 与实装丝印确认量产模组为 ATGM336H-6N、内部 SoC 为 AT6668，并确认当前 GP-02/V1.0 页面是否误配或沿用旧图。；原因：产品版本与图纸模组/修订信息直接冲突。
- `review.input-uart-voltage`：请确认 J2 VCC 的 5V 额定范围及 TXD1/RXD1 的逻辑电平兼容边界。；原因：原理图只标 VCC，UART 又无电平转换。
- `review.uart-settings`：请以 v1.1 实装模组固件或串口实测确认默认 115200bps@8N1。；原因：原理图不包含 UART 配置。
- `review.constellations`：请用 ATGM336H-6N/AT6668 对应资料和固件配置确认支持的卫星系统、频点及联合/独立定位模式。；原因：当前 GP-02 原理图页没有系统或频点信息。
- `review.gnss-performance`：请以 v1.1 实装模组、天线/LNA组合及明确测试条件复核通道数、定位精度、更新率、灵敏度和启动时间。；原因：这些性能参数未印在图纸中。
- `review.nmea-protocol`：请用 v1.1 发布固件或协议输出确认 NMEA0183 4.1、默认句型与配置方式。；原因：协议版本属于固件行为，原理图没有描述。
- `review.power-consumption`：请按明确 GNSS/LNA 状态、卫星环境与 5V 输入点复测 31.64mA 整机功耗。；原因：图纸没有测试状态或电流测量数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `782a31cf28270c1c34428a3e0ce50820af4cb49ee9c79738d122ef4178e95695` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/849/U032-V11-UNIT_GPS_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/Unit-GPS v1.1.md`

源文档 SHA-256：`c038045f0ede29736438d52a40572e2864b2520236bc4f514e84f64dd57d5a6f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
