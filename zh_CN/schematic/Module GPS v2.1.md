# Module GPS v2.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module GPS v2.1 |
| SKU | M003-V21 |
| 产品 ID | `module-gps-v2-1-ba8e2cd14583` |
| 源文档 | `zh_CN/module/Module_GPS_v2.1.md` |

## 概述

Module GPS v2.1 以 U2 ATGM336H-6N-74 GNSS 模组为核心，通过 SW1 十位拨码开关为 UART 提供五组 TX 与五组 RX 主机 GPIO 选择，并通过 SW2 三位拨码开关选择 PPS 输出 GPIO。J2 pin28 的 +5 V 经 U1 VRH3301NLX 转换为 +3.3 V，再由 FB1 滤波后供给 U2，VBAT 由 BAT1 提供备份。射频端由 U2 ANT 与 VCC_RF 经 L1 47 nH 合路，连接 J1 IPEX 并配置 D1 ESD 保护；PPS 另驱动蓝色 LED。

## 检索关键词

`Module GPS v2.1`、`M003-V21`、`ATGM336H-6N-74`、`AT6668`、`VRH3301NLX`、`M5Stack_BUS`、`GNSS`、`UART`、`GNSS_TX`、`GNSS_RX`、`M5-TXD`、`M5-RXD`、`PPS`、`1PPS`、`SW DIP-10`、`SW DIP-3`、`GPIO1`、`GPIO17`、`GPIO15`、`GPIO12`、`GPIO2`、`GPIO3`、`GPIO16`、`GPIO13`、`GPIO34`、`GPIO35`、`GPIO25`、`GPIO36`、`IPEX`、`SMA`、`VCC_RF`、`ANT`、`L1 47nH`、`LXES15AAA1-153`、`VBAT`、`Battery_SMD`、`20000uF`、`+5V`、`+3.3V`、`NMEA0183`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATGM336H-6N-74 | GNSS 接收模组，提供 UART0/UART1、1PPS、备份电源、RF 与复位接口 | 图 6b5cc6953e19 / 第 1 页 / B1-C3 U2 ATGM336H-6N-74 pins1-18 |
| U1 | VRH3301NLX | 将 M5-Bus +5 V 转换为板上 +3.3 V 的稳压器 | 图 6b5cc6953e19 / 第 1 页 / A1 U1 VRH3301NLX pins1-5 |
| SW1 | SW DIP-10 | M5-TXD 与 M5-RXD 各五组 GPIO 候选的十位拨码选择器 | 图 6b5cc6953e19 / 第 1 页 / A2-B3 SW1 SW DIP-10 pins1-20 |
| SW2 | SW DIP-3 | PPS 到 GPIO25、GPIO35 或 GPIO36 的三位拨码选择器 | 图 6b5cc6953e19 / 第 1 页 / B2-B3 SW2 SW DIP-3 pins1-6 |
| J1 | IPEX | GNSS 有源天线射频连接器，中心端接 ANT/VCC_RF 合路节点，外壳接地 | 图 6b5cc6953e19 / 第 1 页 / B3-C3 J1 IPEX pins1-3 |
| L1/D1 | 47nH ±5% / LXES15AAA1-153 | VCC_RF 天线偏置注入与天线节点 ESD 保护 | 图 6b5cc6953e19 / 第 1 页 / B2-C3 U2 VCC_RF/L1/ANT/D1/J1 |
| BAT1 | Battery_SMD | U2 VBAT pin6 的板载备份电源元件 | 图 6b5cc6953e19 / 第 1 页 / B1 BAT1 Battery_SMD/VBAT/GND |
| FB1/C5/C6 | 120Ω/MB / 22uF / 100nF | +3.3 V 到 U2 VCC 的滤波和去耦网络 | 图 6b5cc6953e19 / 第 1 页 / C1-C2 +3.3V/FB1/U2 VCC/C5/C6 |
| D2/R5 | Blue 0603 / 1K | PPS 输出状态指示灯 | 图 6b5cc6953e19 / 第 1 页 / C1 PPS/R5 1K/D2 Blue 0603 |
| J2 | M5Stack_BUS | 30 针主机接口，承载 +5 V、HPWR、BAT 和可选 UART/PPS GPIO | 图 6b5cc6953e19 / 第 1 页 / B4-C4 J2 M5Stack_BUS pins1-30 |

## 系统结构

### Module GPS v2.1 系统架构

U2 ATGM336H-6N-74 提供 GNSS、UART 与 PPS；U1 生成 +3.3 V，BAT1 提供 VBAT，SW1/SW2 完成 UART/PPS GPIO 选择，J1 IPEX 提供有源天线接口。

- 参数与网络：`gnss=U2 ATGM336H-6N-74`；`host=J2 M5Stack_BUS`；`uart_switch=SW1 DIP-10`；`pps_switch=SW2 DIP-3`；`power=+5V -> U1 VRH3301NLX -> +3.3V`；`backup=BAT1 -> VBAT`；`rf=U2 ANT/VCC_RF -> J1 IPEX`
- 证据：图 6b5cc6953e19 / 第 1 页 / 整页 U1/U2/SW1/SW2/J1/J2/BAT1

## 核心器件

### ATGM336H-6N-74 主要引脚

U2 pin1 GND、pin2 TXD0/GNSS_TX、pin3 RXD0/GNSS_RX、pin4 1PPS、pin5 ON/OFF、pin6 VBAT、pin8 VCC、pin9 nRESET、pins10/12 GND、pin11 ANT、pin14 VCC_RF、pins16/17 RXD1/TXD1；pins7/13/15/18 为 NC。

- 参数与网络：`uart0=pin2 TXD0; pin3 RXD0`；`timing=pin4 1PPS`；`control=pin5 ON/OFF; pin9 nRESET`；`power=pin6 VBAT; pin8 VCC`；`rf=pin11 ANT; pin14 VCC_RF`；`uart1=pin16 RXD1; pin17 TXD1`；`ground=pins1/10/12`；`nc=pins7/13/15/18`
- 证据：图 6b5cc6953e19 / 第 1 页 / B1-C3 U2 pins1-18 labels

## 电源

### +5 V 至 +3.3 V 稳压

J2 pin28 的 +5 V 连接 U1 VIN pin4 和 EN pin3，U1 VOUT pin1 形成 +3.3 V，VSS pins2/5 接地。

- 参数与网络：`input=+5V from J2 pin28`；`regulator=U1 VRH3301NLX`；`vin=pin4`；`enable=pin3 tied +5V`；`output=pin1 +3.3V`；`ground=pins2/5`
- 证据：图 6b5cc6953e19 / 第 1 页 / A1 +5V/U1/+3.3V；C4 J2 pin28

### 稳压与 GNSS VCC 去耦

U1 输入配置 C1 22 uF/C2 100 nF，输出配置 C3 22 uF/C4 100 nF；+3.3 V 再经 FB1 120 Ω/MB 到 U2 VCC，并由 C5 22 uF/C6 100 nF 去耦。

- 参数与网络：`regulator_input=C1 22uF; C2 100nF`；`regulator_output=C3 22uF; C4 100nF`；`filter=FB1 120Ω/MB`；`module_caps=C5 22uF; C6 100nF`；`load=U2 VCC pin8`
- 证据：图 6b5cc6953e19 / 第 1 页 / A1 C1-C4/U1；C1-C2 FB1/C5/C6/U2 VCC

### GNSS VBAT 备份电源

U2 VBAT pin6 连接 VBAT 网络，VBAT 由 BAT1 Battery_SMD 对地供电；页面没有给 BAT1 容量或电压值。

- 参数与网络：`target=U2 VBAT pin6`；`rail=VBAT`；`storage=BAT1 Battery_SMD`；`capacity=null`；`voltage=null`
- 证据：图 6b5cc6953e19 / 第 1 页 / B1 BAT1/VBAT；B2 U2 pin6

## 接口

### PPS 蓝色指示灯

PPS 网络经 R5 1 kΩ 和 D2 Blue 0603 串联到 GND，作为 PPS 活动指示。

- 参数与网络：`source=PPS`；`resistor=R5 1K`；`led=D2 Blue 0603`；`destination=GND`
- 证据：图 6b5cc6953e19 / 第 1 页 / C1 PPS/R5/D2/GND

### M5Stack_BUS 使用网络

J2 使用 pins1/3/5 GND、pin28 +5 V、pins25/27/29 HPWR，并提供 UART 候选 pins14/16/23/21/19 与 pins13/15/22/26/2，PPS 候选 pins8/2/4；pin30 BAT 为独立总线网络。

- 参数与网络：`ground=pins1/3/5`；`power=pin28 +5V; pins25/27/29 HPWR; pin30 BAT`；`host_tx_candidates=pin14 GPIO1; pin16 GPIO17; pin23 GPIO15; pin21 GPIO12; pin19 GPIO2`；`host_rx_candidates=pin13 GPIO3; pin15 GPIO16; pin22 GPIO13; pin26 GPIO34; pin2 GPIO35`；`pps_candidates=pin8 GPIO25; pin2 GPIO35; pin4 GPIO36`
- 证据：图 6b5cc6953e19 / 第 1 页 / B4-C4 J2 M5Stack_BUS pins1-30

## 总线

### GNSS UART0

U2 TXD0 pin2 的 GNSS_TX 经 R1 22 Ω 连接 M5-RXD；U2 RXD0 pin3 的 GNSS_RX 经 R3 22 Ω 连接 M5-TXD，随后由 SW1 选择主机 GPIO。

- 参数与网络：`gnss_tx=U2 TXD0 pin2 -> GNSS_TX -> R1 22R -> M5-RXD`；`gnss_rx=M5-TXD -> R3 22R -> GNSS_RX -> U2 RXD0 pin3`；`direction=GNSS_TX module-to-host; GNSS_RX host-to-module`；`routing=SW1`
- 证据：图 6b5cc6953e19 / 第 1 页 / B1-B2 M5-RXD/R1/GNSS_TX/U2 pin2 and M5-TXD/R3/GNSS_RX/U2 pin3

## GPIO 与控制信号

### 主机 TX 到 GNSS_RX 选择

SW1 将 M5-TXD 公共端连接五个候选：GPIO1/J2 pin14、GPIO17/pin16、GPIO15/pin23、GPIO12/pin21、GPIO2/pin19。

- 参数与网络：`target=M5-TXD -> U2 GNSS_RX`；`switch=SW1 pins16-20`；`options=GPIO1 pin14; GPIO17 pin16; GPIO15 pin23; GPIO12 pin21; GPIO2 pin19`；`direction=host-to-GNSS`
- 证据：图 6b5cc6953e19 / 第 1 页 / A2-B3 SW1 rows1-5/M5-TXD；J2 GPIO mapping

### GNSS_TX 到主机 RX 选择

SW1 将 M5-RXD 公共端连接五个候选：GPIO3/J2 pin13、GPIO16/pin15、GPIO13/pin22、GPIO34/pin26、GPIO35/pin2。

- 参数与网络：`source=U2 GNSS_TX -> M5-RXD`；`switch=SW1 pins11-15`；`options=GPIO3 pin13; GPIO16 pin15; GPIO13 pin22; GPIO34 pin26; GPIO35 pin2`；`direction=GNSS-to-host`
- 证据：图 6b5cc6953e19 / 第 1 页 / A2-B3 SW1 rows6-10/M5-RXD；J2 GPIO mapping

### PPS GPIO 选择

U2 1PPS pin4 的 PPS 网络连接 SW2 公共侧，可选择 GPIO25/J2 pin8、GPIO35/J2 pin2 或 GPIO36/J2 pin4。

- 参数与网络：`source=U2 1PPS pin4`；`net=PPS`；`switch=SW2`；`options=GPIO25 pin8; GPIO35 pin2; GPIO36 pin4`；`direction=GNSS-to-host`
- 证据：图 6b5cc6953e19 / 第 1 页 / B2 U2 PPS；B3 SW2 GPIO25/GPIO35/GPIO36；J2

## 保护电路

### 天线 ESD 保护

射频馈线节点通过 D1 LXES15AAA1-153 接地保护，器件位于 U2 ANT/L1 与 J1 IPEX 之间。

- 参数与网络：`device=D1 LXES15AAA1-153`；`protected_net=ANT/VCC_RF feed`；`connection=RF node to GND`；`connector=J1 IPEX`
- 证据：图 6b5cc6953e19 / 第 1 页 / C3 D1 on J1 antenna feed

## 射频

### IPEX 有源天线接口

U2 ANT pin11 连接 J1 IPEX 中心端；U2 VCC_RF pin14 经 L1 47 nH ±5% 注入同一射频节点，J1 外壳接 GND。

- 参数与网络：`rf_input=U2 ANT pin11`；`bias_source=U2 VCC_RF pin14`；`bias_inductor=L1 47nH ±5%`；`connector=J1 IPEX pin1`；`shield=J1 pins2/3 GND`
- 证据：图 6b5cc6953e19 / 第 1 页 / B2-C3 U2 ANT/VCC_RF/L1/J1 IPEX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module GPS v2.1 系统架构 | `gnss=U2 ATGM336H-6N-74`；`host=J2 M5Stack_BUS`；`uart_switch=SW1 DIP-10`；`pps_switch=SW2 DIP-3`；`power=+5V -> U1 VRH3301NLX -> +3.3V`；`backup=BAT1 -> VBAT`；`rf=U2 ANT/VCC_RF -> J1 IPEX` |
| 核心器件 | ATGM336H-6N-74 主要引脚 | `uart0=pin2 TXD0; pin3 RXD0`；`timing=pin4 1PPS`；`control=pin5 ON/OFF; pin9 nRESET`；`power=pin6 VBAT; pin8 VCC`；`rf=pin11 ANT; pin14 VCC_RF`；`uart1=pin16 RXD1; pin17 TXD1`；`ground=pins1/10/12`；`nc=pins7/13/15/18` |
| 电源 | +5 V 至 +3.3 V 稳压 | `input=+5V from J2 pin28`；`regulator=U1 VRH3301NLX`；`vin=pin4`；`enable=pin3 tied +5V`；`output=pin1 +3.3V`；`ground=pins2/5` |
| 电源 | 稳压与 GNSS VCC 去耦 | `regulator_input=C1 22uF; C2 100nF`；`regulator_output=C3 22uF; C4 100nF`；`filter=FB1 120Ω/MB`；`module_caps=C5 22uF; C6 100nF`；`load=U2 VCC pin8` |
| 电源 | GNSS VBAT 备份电源 | `target=U2 VBAT pin6`；`rail=VBAT`；`storage=BAT1 Battery_SMD`；`capacity=null`；`voltage=null` |
| 总线 | GNSS UART0 | `gnss_tx=U2 TXD0 pin2 -> GNSS_TX -> R1 22R -> M5-RXD`；`gnss_rx=M5-TXD -> R3 22R -> GNSS_RX -> U2 RXD0 pin3`；`direction=GNSS_TX module-to-host; GNSS_RX host-to-module`；`routing=SW1` |
| GPIO 与控制信号 | 主机 TX 到 GNSS_RX 选择 | `target=M5-TXD -> U2 GNSS_RX`；`switch=SW1 pins16-20`；`options=GPIO1 pin14; GPIO17 pin16; GPIO15 pin23; GPIO12 pin21; GPIO2 pin19`；`direction=host-to-GNSS` |
| GPIO 与控制信号 | GNSS_TX 到主机 RX 选择 | `source=U2 GNSS_TX -> M5-RXD`；`switch=SW1 pins11-15`；`options=GPIO3 pin13; GPIO16 pin15; GPIO13 pin22; GPIO34 pin26; GPIO35 pin2`；`direction=GNSS-to-host` |
| GPIO 与控制信号 | PPS GPIO 选择 | `source=U2 1PPS pin4`；`net=PPS`；`switch=SW2`；`options=GPIO25 pin8; GPIO35 pin2; GPIO36 pin4`；`direction=GNSS-to-host` |
| 接口 | PPS 蓝色指示灯 | `source=PPS`；`resistor=R5 1K`；`led=D2 Blue 0603`；`destination=GND` |
| 射频 | IPEX 有源天线接口 | `rf_input=U2 ANT pin11`；`bias_source=U2 VCC_RF pin14`；`bias_inductor=L1 47nH ±5%`；`connector=J1 IPEX pin1`；`shield=J1 pins2/3 GND` |
| 保护电路 | 天线 ESD 保护 | `device=D1 LXES15AAA1-153`；`protected_net=ANT/VCC_RF feed`；`connection=RF node to GND`；`connector=J1 IPEX` |
| 接口 | M5Stack_BUS 使用网络 | `ground=pins1/3/5`；`power=pin28 +5V; pins25/27/29 HPWR; pin30 BAT`；`host_tx_candidates=pin14 GPIO1; pin16 GPIO17; pin23 GPIO15; pin21 GPIO12; pin19 GPIO2`；`host_rx_candidates=pin13 GPIO3; pin15 GPIO16; pin22 GPIO13; pin26 GPIO34; pin2 GPIO35`；`pps_candidates=pin8 GPIO25; pin2 GPIO35; pin4 GPIO36` |
| 核心器件 | AT6668 内部 SoC | `schematic_module=ATGM336H-6N-74`；`document_soc=AT6668`；`soc_reference=not shown` |
| 电源 | 20000 uF 超级电容 | `document_capacity=20000uF`；`document_voltage=3.3V`；`schematic_reference=BAT1`；`schematic_marking=Battery_SMD`；`part_number=null` |
| 射频 | 外置 SMA 天线 | `schematic_connector=J1 IPEX`；`document_connector=SMA`；`document_antenna=active GPS/BD antenna, 1m`；`adapter_cable=not shown` |
| 射频 | GNSS 系统、精度、协议与 UART 参数 | `document_systems=GPS/QZSS/BD2/BD3/GAL/GLO`；`document_channels=50`；`document_accuracy=<1.5m CEP50`；`document_rate=10Hz max`；`document_protocol=NMEA0183 4.1`；`document_uart=115200bps 8N1`；`schematic_parameters=not shown` |

## 待确认事项

- `component.internal-soc`：产品正文称 SoC 为 AT6668，原理图板级位号 U2 仅标 ATGM336H-6N-74，没有展开内部 AT6668 芯片。（证据：图 6b5cc6953e19 / 第 1 页 / U2 ATGM336H-6N-74 module block）
- `power.backup-capacity`：产品正文称备份元件为 20000 uF、3.3 V 超级电容，原理图仅将 BAT1 标为 Battery_SMD，未给容量、电压或超级电容型号。（证据：图 6b5cc6953e19 / 第 1 页 / B1 BAT1 Battery_SMD without value）
- `rf.external-sma`：产品正文称默认搭载外置 SMA 有源天线，原理图板上只画 J1 IPEX；未显示 SMA 连接器或 IPEX-to-SMA 线缆。（证据：图 6b5cc6953e19 / 第 1 页 / J1 IPEX is only RF connector shown）
- `rf.gnss-performance`：产品正文列出 GPS/QZSS/BD2/BD3/GAL/GLO、50 通道、<1.5 m、10 Hz、NMEA0183 4.1 与 UART 115200 8N1 等参数，但原理图未印这些性能或协议配置。（证据：图 6b5cc6953e19 / 第 1 页 / U2 module block and UART nets lack performance/protocol labels）
- `review.internal-soc`：请用 ATGM336H-6N-74 BOM 或模组规格确认内部 GNSS SoC 为 AT6668。；原因：原理图只显示完整 GNSS 模组。
- `review.backup-capacity`：请用 BAT1 BOM、实物标识或测量确认其为 3.3 V、20000 uF 超级电容。；原因：原理图没有 BAT1 数值或类型细节。
- `review.external-sma`：请用包装/BOM/装配资料确认随附 SMA 有源天线及 IPEX-to-SMA 馈线。；原因：板级原理图只显示 IPEX。
- `review.gnss-performance`：请用当前 ATGM336H-6N-74 版本数据手册和固件配置复核星座、通道、精度、更新率、协议与 UART 参数。；原因：这些参数未印在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6b5cc6953e19fa707837be28604edc4f4de7856442d3948befd81292bfe9ebde` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/SCH_Module_GPS_v2.1_2025_06_18_16_45_23_page_01.png` |

---

源文档：`zh_CN/module/Module_GPS_v2.1.md`

源文档 SHA-256：`f6a4041867861e1372a2fa4c974bae82096da33af6c02a43925b404369759286`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
