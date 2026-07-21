# Unit RF433T 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RF433T |
| SKU | U114 |
| 产品 ID | `unit-rf433t-21f49a191358` |
| 源文档 | `zh_CN/unit/rf433_t.md` |

## 概述

Unit RF433T 以 U1 SYN115 为 ASK 射频发射器，不含本地主控、存储器或可编程逻辑。J1 pin 2 的外部数据经 R1 22Ω 进入 ASK pin 6，Y1 13.560MHz 与 C4/C5 构成参考时钟，PAOUT 经 L1 偏置及 C2/L2/C3 匹配后连接 E1 CA-S01。J1 输入 +5V 直接为 SYN115 供电，C1 10uF 与 C10 100nF 去耦；载波频率、数据率、功率、距离和天线形式未由本页完全确认。

## 检索关键词

`Unit RF433T`、`U114`、`SYN115`、`U1`、`ASK`、`PAOUT`、`XTLIN`、`XTLOUT`、`13.560MHz`、`Y1`、`RF_TX`、`J1`、`HY-2.0_IO`、`R1 22Ω`、`L1 680nH`、`L2 82nH`、`C2 10pF`、`C3 4.7pF`、`C4 18pF`、`C5 18pF`、`E1`、`CA-S01`、`+5V`、`C1 10uF`、`C10 100nF`、`433.92MHz`、`10kbps`、`10dBm`、`PCB antenna`、`RF transmitter`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SYN115 | ASK 射频发射器，接收外部 ASK 数据、晶体参考并从 PAOUT 输出射频信号 | 图 ca06d8335bad / 第 1 页 / 页面中央 U1 SYN115：pin1 PAOUT、pin2 VSS、pin3 VDD、pin4 XTLOUT、pin5 XTLIN、pin6 ASK |
| J1 | HY-2.0_IO | 四针 Grove 接口，提供 ASK 数据输入、+5V 和 GND，pin 1 未连接 | 图 ca06d8335bad / 第 1 页 / 页面右侧 J1 HY-2.0_IO：pin1 NC 叉号、pin2 接 R1、pin3 +5V、pin4 GND |
| Y1 | 13.560MHz | SYN115 XTLIN/XTLOUT 的外部参考晶体 | 图 ca06d8335bad / 第 1 页 / 页面中右 Y1 13.560MHz，连接 U1 XTLIN/XTL OUT 并配 C4/C5 18pF |
| E1 | CA-S01 | 射频输出端的天线器件或天线连接结构 | 图 ca06d8335bad / 第 1 页 / 页面左侧 E1 天线符号，器件值 CA-S01，与 L2/C3 匹配端连接 |
| L1/L2/C2/C3 | 680nH / 82nH / 10pF / 4.7pF | PAOUT 直流偏置与到 E1 的射频匹配网络 | 图 ca06d8335bad / 第 1 页 / 页面左中 U1 PAOUT、L1 680nH 到 +5V、串联 C2 10pF/L2 82nH、C3 4.7pF 对地与 E1 |
| R1 | 22Ω | J1 pin 2 到 U1 ASK pin 6 的数据串联电阻 | 图 ca06d8335bad / 第 1 页 / 页面中右 U1 ASK 与 J1 pin2 之间 R1 22Ω |
| C1/C10 | 10uF / 100nF | +5V 电源的低频储能与高频去耦 | 图 ca06d8335bad / 第 1 页 / 页面中上 C1 10uF 和右侧 C10 100nF，均跨接 +5V-GND |

## 系统结构

### Unit RF433T

整板由 SYN115 发射器、13.560MHz 晶体、ASK 数据接口、+5V 去耦、PA 偏置/匹配网络和天线器件组成；原理图未显示 MCU、协处理器、存储器、接收链、复位或调试接口。

- 参数与网络：`transmitter=U1 SYN115`；`data_input=J1 pin2 via R1 22Ω`；`reference_clock=Y1 13.560MHz`；`rf_output=U1 PAOUT to E1 CA-S01`；`controller=null`；`storage=null`；`receiver=null`；`reset=null`
- 证据：图 ca06d8335bad / 第 1 页 / 整页 U1、J1、Y1、E1 与电源/RF 外围组成全部电路

## 核心器件

### U1 SYN115

U1 pin 1 为 PAOUT，pin 2 为 VSS/GND，pin 3 为 VDD/+5V，pin 4 为 XTLOUT，pin 5 为 XTLIN，pin 6 为 ASK。

- 参数与网络：`pin_1=PAOUT`；`pin_2=VSS GND`；`pin_3=VDD +5V`；`pin_4=XTLOUT`；`pin_5=XTLIN`；`pin_6=ASK`
- 证据：图 ca06d8335bad / 第 1 页 / 页面中央 U1 六引脚符号及 PAOUT/VSS/VDD/XTLOUT/XTLIN/ASK 标签

## 电源

### +5V 电源轨

J1 pin 3 输入 +5V，直接连接 U1 VDD pin 3、L1 上端、C1 和 C10；板上未显示稳压器、LDO、负载开关、电池或充电电路。

- 参数与网络：`input=J1 pin 3`；`rail=+5V`；`loads=U1 VDD pin3,L1 PA bias,C1,C10`；`regulator=null`；`ldo=null`；`load_switch=null`；`battery=null`；`charger=null`
- 证据：图 ca06d8335bad / 第 1 页 / 整页 +5V 网络位于 J1、U1、L1、C1、C10，无电源 IC

### C1/C10 去耦

C1 10uF 与 C10 100nF 均跨接 +5V 和 GND，分别提供电源储能与高频去耦。

- 参数与网络：`bulk=C1 10uF +5V-to-GND`；`high_frequency=C10 100nF +5V-to-GND`
- 证据：图 ca06d8335bad / 第 1 页 / 页面中上 C1 10uF 与右侧 C10 100nF 的 +5V/GND 连接

## 接口

### J1 HY-2.0_IO

J1 pin 1 带未连接叉号，pin 2 经 R1 接 U1 ASK，pin 3 接 +5V，pin 4 接 GND。

- 参数与网络：`pin_1=NC`；`pin_2=ASK data via R1 22Ω`；`pin_3=+5V`；`pin_4=GND`；`connector=HY-2.0_IO`
- 证据：图 ca06d8335bad / 第 1 页 / 页面右侧 J1 pins1-4、NC 叉号、R1、+5V 和 GND

## GPIO 与控制信号

### ASK 数据输入

外部主机从 J1 pin 2 提供的数字信号经 R1 22Ω 串联后直接进入 U1 ASK pin 6；板上没有缓冲器、电平转换器、上拉或下拉。

- 参数与网络：`source=J1 pin 2`；`series_resistor=R1 22Ω`；`destination=U1 pin 6 ASK`；`direction=host to transmitter`；`buffer=null`；`level_shifter=null`；`pullup=null`；`pulldown=null`
- 证据：图 ca06d8335bad / 第 1 页 / 页面 U1 ASK-R1-J1 pin2 连续线路，无其他支路

## 时钟

### Y1 13.560MHz

Y1 13.560MHz 跨接 U1 XTLOUT pin 4 与 XTLIN pin 5，C4/C5 各 18pF 从晶体两端接 GND。

- 参数与网络：`crystal=Y1 13.560MHz`；`xtlout=U1 pin 4`；`xtlin=U1 pin 5`；`load_caps=C4 18pF,C5 18pF`；`return=GND`
- 证据：图 ca06d8335bad / 第 1 页 / 页面中右 U1 XTLOUT/XTLIN、Y1 与 C4/C5

## 保护电路

### J1 与天线接口保护

ASK 数据线上有 R1 22Ω 串联电阻，但本页未显示 J1 或 E1 上的 TVS/ESD 阵列、保险丝、反接保护或射频限幅器件。

- 参数与网络：`data_series_resistor=R1 22Ω`；`tv_esd=null`；`fuse=null`；`reverse_polarity_protection=null`；`rf_limiter=null`
- 证据：图 ca06d8335bad / 第 1 页 / 整页 J1-R1-U1 与 U1-E1 路径，未见专用保护器件

## 射频

### PAOUT 供电偏置

L1 680nH 从 +5V 连接 U1 PAOUT pin 1，为 PAOUT 提供直流馈电/射频扼流路径；C1 10uF 在该 +5V 节点对地。

- 参数与网络：`pa_pin=U1 pin 1 PAOUT`；`rf_choke=L1 680nH ±5% 0603`；`supply=+5V`；`supply_cap=C1 10uF to GND`
- 证据：图 ca06d8335bad / 第 1 页 / 页面左中 +5V-L1 680nH-U1 PAOUT 与 C1 10uF

### PAOUT 至 E1 匹配网络

U1 PAOUT 先经串联 C2 10pF，再经串联 L2 82nH 到 E1；E1 侧节点由 C3 4.7pF 对地，形成串联 C-L 加末端并联 C 的射频匹配链。

- 参数与网络：`source=U1 PAOUT pin 1`；`series_capacitor=C2 10pF`；`series_inductor=L2 82nH ±5%`；`shunt_capacitor=C3 4.7pF to GND`；`destination=E1 CA-S01`
- 证据：图 ca06d8335bad / 第 1 页 / 页面左侧 U1 PAOUT-C2-L2-E1 与 C3 对地支路

### E1 CA-S01

E1 标注 CA-S01，直接连接 L2/C3 匹配端，是原理图可见的唯一射频辐射端或天线结构。

- 参数与网络：`reference=E1`；`marking=CA-S01`；`feed=L2 82nH`；`shunt=C3 4.7pF`；`other_rf_connector=null`
- 证据：图 ca06d8335bad / 第 1 页 / 页面最左 E1 天线符号和 CA-S01 标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RF433T | `transmitter=U1 SYN115`；`data_input=J1 pin2 via R1 22Ω`；`reference_clock=Y1 13.560MHz`；`rf_output=U1 PAOUT to E1 CA-S01`；`controller=null`；`storage=null`；`receiver=null`；`reset=null` |
| 核心器件 | U1 SYN115 | `pin_1=PAOUT`；`pin_2=VSS GND`；`pin_3=VDD +5V`；`pin_4=XTLOUT`；`pin_5=XTLIN`；`pin_6=ASK` |
| 接口 | J1 HY-2.0_IO | `pin_1=NC`；`pin_2=ASK data via R1 22Ω`；`pin_3=+5V`；`pin_4=GND`；`connector=HY-2.0_IO` |
| GPIO 与控制信号 | ASK 数据输入 | `source=J1 pin 2`；`series_resistor=R1 22Ω`；`destination=U1 pin 6 ASK`；`direction=host to transmitter`；`buffer=null`；`level_shifter=null`；`pullup=null`；`pulldown=null` |
| 时钟 | Y1 13.560MHz | `crystal=Y1 13.560MHz`；`xtlout=U1 pin 4`；`xtlin=U1 pin 5`；`load_caps=C4 18pF,C5 18pF`；`return=GND` |
| 射频 | PAOUT 供电偏置 | `pa_pin=U1 pin 1 PAOUT`；`rf_choke=L1 680nH ±5% 0603`；`supply=+5V`；`supply_cap=C1 10uF to GND` |
| 射频 | PAOUT 至 E1 匹配网络 | `source=U1 PAOUT pin 1`；`series_capacitor=C2 10pF`；`series_inductor=L2 82nH ±5%`；`shunt_capacitor=C3 4.7pF to GND`；`destination=E1 CA-S01` |
| 射频 | E1 CA-S01 | `reference=E1`；`marking=CA-S01`；`feed=L2 82nH`；`shunt=C3 4.7pF`；`other_rf_connector=null` |
| 电源 | +5V 电源轨 | `input=J1 pin 3`；`rail=+5V`；`loads=U1 VDD pin3,L1 PA bias,C1,C10`；`regulator=null`；`ldo=null`；`load_switch=null`；`battery=null`；`charger=null` |
| 电源 | C1/C10 去耦 | `bulk=C1 10uF +5V-to-GND`；`high_frequency=C10 100nF +5V-to-GND` |
| 保护电路 | J1 与天线接口保护 | `data_series_resistor=R1 22Ω`；`tv_esd=null`；`fuse=null`；`reverse_polarity_protection=null`；`rf_limiter=null` |
| 射频 | 433.92MHz ASK 发射 | `documented_carrier=433.92MHz`；`documented_modulation=ASK`；`schematic_reference=13.560MHz`；`carrier_label_on_schematic=null`；`multiplier=null`；`modulation_depth=null` |
| 总线 | ASK 数据速率 | `documented_rate=10kbps`；`encoding=null`；`bit_timing=null`；`duty_cycle=null`；`schematic_rate_label=null` |
| 射频 | 输出功率、距离与工作电流 | `documented_output_power=10dBm`；`documented_distance=10m`；`documented_current=12mA`；`load_impedance=null`；`antenna_gain=null`；`test_conditions=null` |
| 射频 | 天线实现形式 | `documented_type=PCB antenna`；`schematic_reference=E1`；`schematic_marking=CA-S01`；`confirmed_physical_type=null` |
| 接口 | J1 Grove 线色映射 | `electrical_pinout=pin1 NC,pin2 ASK,pin3 +5V,pin4 GND`；`color_labels_on_schematic=null`；`document_colors=Black,Red,Yellow,White` |

## 待确认事项

- `rf.documented-carrier-modulation`：正文声称工作频率 433.92MHz 且采用 ASK 调制；原理图确认 ASK 引脚和 13.560MHz 晶体，但未标注最终载波频率、倍频关系或调制参数。（证据：图 ca06d8335bad / 第 1 页 / 页面 U1 ASK 与 Y1 13.560MHz，无 433.92MHz 或调制深度标注）
- `bus.documented-data-rate`：正文给出 10kbps 数据率，但原理图只显示 ASK 数据直连和 R1 22Ω，没有位时序、编码方式、占空比或速率限制。（证据：图 ca06d8335bad / 第 1 页 / 页面 J1 pin2-R1-U1 ASK，无数据速率或协议注释）
- `rf.documented-performance`：正文列出 10dBm 输出、10m 稳定距离和 12mA 工作电流；原理图没有功率、电流、负载、天线增益、测试距离或环境条件，不能仅凭本页确认这些性能。（证据：图 ca06d8335bad / 第 1 页 / 整页只有器件值和连接，无 dBm、mA、距离或测试条件）
- `rf.antenna-implementation`：正文称使用 PCB 天线，而原理图把射频端画为独立位号 E1、标注 CA-S01；仅凭该页无法确认量产件是 PCB 走线、弹簧天线还是其他 CA-S01 结构。（证据：图 ca06d8335bad / 第 1 页 / 页面左侧 E1 CA-S01 天线符号，无 PCB 天线文字或几何图形）
- `interface.grove-color-mapping`：原理图给出 J1 pin 1-4 的 NC/ASK/+5V/GND 电气定义，但未标注 Black/Red/Yellow/White 线色，无法仅凭本页验证正文映射。（证据：图 ca06d8335bad / 第 1 页 / 页面右侧 J1 仅显示 pin 编号和 I/O/VCC/GND，无线色文字）
- `review.carrier-modulation`：请依据 SYN115 datasheet、BOM 晶体规格和频谱实测确认 433.92MHz 载波及 ASK 调制参数。；原因：原理图只显示 13.560MHz 参考和 ASK 引脚，没有最终 RF 参数。
- `review.data-rate`：请用 SYN115 datasheet 与固件波形确认 10kbps、编码、占空比和允许时序。；原因：原理图没有协议或速率参数。
- `review.rf-performance`：请用器件资料和当前天线/匹配实测复核 10dBm、12mA 与 10m 稳定通信距离及其测试条件。；原因：这些性能值不在原理图中，且依赖负载、天线和环境。
- `review.antenna-implementation`：请用 PCB 布局、BOM 或实物确认 E1 CA-S01 的物理天线形式。；原因：正文 PCB 天线描述与原理图独立 E1 位号不足以互相证明。
- `review.grove-color-mapping`：请结合 Grove 线缆规范和连接器方向确认 Black/Red/Yellow/White 与 J1 pin 1-4 的对应关系。；原因：原理图不含线色标签。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ca06d8335badeb3b72d95eb8533e0a1a9e22d10b3d47a8a6ff969dfdb754940a` | `https://static-cdn.m5stack.com/resource/docs/products/unit/rf433_t/rf433_t_sch_01.webp` |

---

源文档：`zh_CN/unit/rf433_t.md`

源文档 SHA-256：`2f0eeb29d1805015d0c8b23739239ff58c7a32340d87eedb25d007d3480732ef`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
