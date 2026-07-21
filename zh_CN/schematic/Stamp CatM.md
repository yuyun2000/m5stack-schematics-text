# Stamp CatM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp CatM |
| SKU | S003 |
| 产品 ID | `stamp-catm-4363106b3648` |
| 源文档 | `zh_CN/stamp/stamp_catm.md` |

## 概述

Stamp CatM 以 M1 SIM7080G 蜂窝模组为核心，通过 UART1_TXD/RXD 与两组 SS8050 电平转换连接 Stamp 边缘接口 NB_TX/NB_RX。+5 V 经 U1 GM9308/HM8089 降压产生 +3.3 V，直接为 M1 VBAT、外部 Stamp 引脚和 SIM 接口供电；M1 VDD_EXT 另产生 +1.8 V 供 UART 低压侧使用。U2 SIM 卡座连接 SIM_DATA/CLK/RST/VDD，蜂窝 ANT 连接 E1 ANT_IPEX 并同时引出至 J1 pin1。

## 检索关键词

`Stamp CatM`、`S003`、`SIM7080G`、`GM9308/HM8089`、`Cat-M`、`NB-IoT`、`UART1_TXD`、`UART1_RXD`、`NB_TX`、`NB_RX`、`U1_TX`、`U1_RX`、`SS8050 Y1`、`+5V`、`+3.3V`、`+1.8V`、`VDD_EXT`、`VBAT`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SIM_VCC`、`MicroSIM`、`ANT`、`ANT_IPEX`、`IPEX`、`SMA`、`StampCatM_Pin`、`PWRKEY`、`STATUS`、`NETLIGHT`、`USB_DP`、`USB_DM`、`UART2`、`115200 8N1`、`AT Command`、`MQTT`、`TCP/UDP`、`Cat-M bands`、`NB-IoT bands`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7080G | Cat-M/NB-IoT 蜂窝通信模组，提供 UART、SIM、RF、状态、USB 与控制接口 | 图 55e21a6abc49 / 第 1 页 / B3-D4 M1 SIM7080G pins1-42 |
| U1 | GM9308/HM8089 | 从 +5 V 产生 +3.3 V 的开关降压转换器 | 图 55e21a6abc49 / 第 1 页 / A1-A2 U1 GM9308/HM8089/L1/R1/R2/C1-C4 |
| U2 | SIM | SIM 卡座，连接 SIM_DATA、SIM_CLK、SIM_RST、SIM_VCC 与 GND | 图 55e21a6abc49 / 第 1 页 / C2-C3 U2 SIM pins1-7 |
| Q1/Q2 | SS8050 Y1 | UART NB_RX/NB_TX 3.3 V 域与 U1_RX/U1_TX 1.8 V 域之间的晶体管电平转换 | 图 55e21a6abc49 / 第 1 页 / C1-C2 Q1/Q2 SS8050 Y1、R5-R10 |
| E1 | ANT_IPEX | SIM7080G ANT 的 IPEX 蜂窝天线接口 | 图 55e21a6abc49 / 第 1 页 / C4 E1 ANT_IPEX and M1 ANT pin32 |
| J1 | StampCatM_Pin | 六针边缘接口，引出 ANT、NB_TX、NB_RX、GND、3V3 与 5V | 图 55e21a6abc49 / 第 1 页 / A4-B4 J1 StampCatM_Pin pins1-6 |
| L1/R1/R2 | 3015 4.7uH / 68KΩ / 15KΩ | U1 输出电感与反馈分压网络 | 图 55e21a6abc49 / 第 1 页 / A1-A2 U1 SW/L1/R1/R2/+3.3V |
| D1/R3 | 红灯0603 / 1KΩ | +3.3 V 电源红色指示灯 | 图 55e21a6abc49 / 第 1 页 / A3-B3 +3.3V/D1 red/R3/GND |
| C5 | 22uF | SIM7080G VDD_EXT +1.8 V 输出去耦电容 | 图 55e21a6abc49 / 第 1 页 / B4 M1 VDD_EXT pin40/+1.8V/C5 |

## 系统结构

### Stamp CatM 系统架构

M1 SIM7080G 通过电平转换 UART 连接 J1 Stamp 接口，通过 U2 连接 SIM 卡，通过 E1 连接蜂窝天线；U1 从 +5 V 产生系统 +3.3 V。

- 参数与网络：`cellular=M1 SIM7080G`；`uart_level_shift=Q1/Q2 SS8050 Y1`；`sim=U2 SIM`；`antenna=E1 ANT_IPEX`；`edge=J1 StampCatM_Pin`；`power=+5V -> U1 GM9308/HM8089 -> +3.3V`；`low_voltage=M1 VDD_EXT -> +1.8V`
- 证据：图 55e21a6abc49 / 第 1 页 / 整页 U1/M1/U2/Q1/Q2/E1/J1

## 核心器件

### SIM7080G 主要引脚分组

M1 UART1_TXD/RXD pins1/2，SIM_DATA/CLK/RST/VDD pins15-18，USB_DM/DP/VBUS pins26/25/24，UART2_RXD/TXD pins23/22，ANT pin32，VBAT pins34/35，VDD_EXT pin40，NETLIGHT/STATUS pins41/42，PWRKEY pin39。

- 参数与网络：`uart1=TXD pin1; RXD pin2`；`sim=DATA15; CLK16; RST17; VDD18`；`usb=DM26; DP25; VBUS24`；`uart2=RXD23; TXD22`；`rf=ANT32`；`power=VBAT34/35; VDD_EXT40`；`status=NETLIGHT41; STATUS42`；`control=PWRKEY39`
- 证据：图 55e21a6abc49 / 第 1 页 / M1 SIM7080G pin labels

## 电源

### +5 V 至 +3.3 V 降压

U1 GM9308/HM8089 VIN pin4 与 EN pin1 接 +5 V，SW pin3 经 L1 4.7 uH 输出 +3.3 V，FB pin5 由 R1 68 kΩ/R2 15 kΩ 分压。

- 参数与网络：`input=+5V`；`converter=U1 GM9308/HM8089`；`enable=pin1 +5V`；`switch=pin3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ; R2 15KΩ`；`ground=pin2`
- 证据：图 55e21a6abc49 / 第 1 页 / A1-A2 U1/L1/R1/R2/+5V/+3.3V

### 降压输入输出去耦

+5 V 输入配置 C3 22 uF/C4 100 nF，+3.3 V 输出配置 C2 22 uF/C1 100 nF。

- 参数与网络：`input_caps=C3 22uF; C4 100nF`；`output_caps=C2 22uF; C1 100nF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 55e21a6abc49 / 第 1 页 / A1-A2 C1-C4 around U1

### SIM7080G 主供电

M1 VBAT pins34/35 在页面连接 +3.3 V，多个 GND pins8/13/19/21/27/30/31/33/36/37 接地。

- 参数与网络：`supply=+3.3V`；`vbat_pins=34/35`；`ground_pins=8/13/19/21/27/30/31/33/36/37`
- 证据：图 55e21a6abc49 / 第 1 页 / M1 VBAT pins34/35 and GND pin rails

### SIM7080G +1.8 V 输出

M1 VDD_EXT pin40 形成 +1.8 V 网络，C5 22 uF 对地去耦；该轨为 UART 模组侧上拉供电。

- 参数与网络：`source=M1 VDD_EXT pin40`；`rail=+1.8V`；`decoupling=C5 22uF`；`loads=R5/R7/R8/R10 UART-side pullups`
- 证据：图 55e21a6abc49 / 第 1 页 / B4 +1.8V/VDD_EXT/C5 and C1-C2 UART pullups

## 接口

### UART 1.8 V/3.3 V 电平转换

NB_RX 与 NB_TX 各由 4.7 kΩ 上拉到 +3.3 V，U1_RX 与 U1_TX 各由 4.7 kΩ 上拉到 +1.8 V，并通过 Q1/Q2 SS8050 Y1 交互。

- 参数与网络：`rx_external_pullup=R6 4.7KΩ to +3.3V`；`rx_module_pullup=R7 4.7KΩ to +1.8V`；`tx_external_pullup=R9 4.7KΩ to +3.3V`；`tx_module_pullup=R10 4.7KΩ to +1.8V`；`transistors=Q1/Q2 SS8050 Y1`
- 证据：图 55e21a6abc49 / 第 1 页 / C1-C2 R5-R10/Q1/Q2/NB_RX/NB_TX/U1_RX/U1_TX

### SIM 卡接口

U2 SIM VCC pin1 接 SIM_VCC/M1 SIM_VDD pin18，RST pin2 接 M1 pin17，CLK pin3 接 M1 pin16，IO pin7 接 M1 SIM_DATA pin15，GND pin5 接地，VPP pin6 未连接。

- 参数与网络：`vcc=U2 pin1 SIM_VCC -> M1 pin18 SIM_VDD`；`reset=U2 pin2 -> M1 pin17`；`clock=U2 pin3 -> M1 pin16`；`data=U2 pin7 -> M1 pin15`；`ground=U2 pin5`；`vpp=pin6 no-connect`
- 证据：图 55e21a6abc49 / 第 1 页 / C2-C3 U2-to-M1 SIM pins15-18

### StampCatM 六针接口

J1 pin1 ANT、pin2 NB_TX、pin3 NB_RX、pin4 GND、pin5 +3.3 V、pin6 +5 V。

- 参数与网络：`pin1=ANT`；`pin2=NB_TX`；`pin3=NB_RX`；`pin4=GND`；`pin5=+3.3V`；`pin6=+5V`
- 证据：图 55e21a6abc49 / 第 1 页 / A4-B4 J1 StampCatM_Pin pins1-6

### 3.3 V 电源指示灯

+3.3 V 经 D1 红灯0603 与 R3 1 kΩ 串联到 GND。

- 参数与网络：`supply=+3.3V`；`led=D1 红灯0603`；`resistor=R3 1KΩ`；`destination=GND`
- 证据：图 55e21a6abc49 / 第 1 页 / A3-B3 D1/R3

### 未使用的 SIM7080G 接口

UART1_RTS/CTS/DCD/DTR/RI、PCM_DIN/DOUT/CLK/SYNC、ADC、GPIO5、USB_DM/DP/VBUS、USB_BOOT 与 UART2_RXD/TXD 在页面标记未连接。

- 参数与网络：`uart1_modem=pins3-7 NC`；`pcm=pins9-12 NC`；`analog_gpio=ADC38; GPIO5 14 NC`；`usb=pins26/25/24 and USB_BOOT20 NC`；`uart2=pins23/22 NC`
- 证据：图 55e21a6abc49 / 第 1 页 / M1 red no-connect marks on pins3-7/9-12/14/20/22-26/38

## 总线

### SIM7080G UART1

M1 UART1_TXD pin1 为 U1_TX，UART1_RXD pin2 为 U1_RX；两信号经 Q2/Q1 晶体管网络分别转换到外部 NB_TX/NB_RX。

- 参数与网络：`module_tx=M1 pin1 U1_TX -> Q2 -> NB_TX`；`module_rx=NB_RX -> Q1 -> U1_RX -> M1 pin2`；`module_level=+1.8V pullups`；`external_level=+3.3V pullups`；`edge=J1 pins2/3`
- 证据：图 55e21a6abc49 / 第 1 页 / B3-C2 M1 UART1 pins1/2 and Q1/Q2 NB_TX/NB_RX

## 射频

### 蜂窝 IPEX 天线

M1 ANT pin32 连接 E1 ANT_IPEX 中心端并同时引出为 J1 pin1 ANT，E1 外壳接 GND；页面未画射频匹配或 ESD 网络。

- 参数与网络：`source=M1 ANT pin32`；`connector=E1 ANT_IPEX`；`edge=J1 pin1 ANT`；`shield=GND`；`matching=not shown`；`esd=not shown`
- 证据：图 55e21a6abc49 / 第 1 页 / C4 M1 ANT/E1 and A4 J1 ANT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp CatM 系统架构 | `cellular=M1 SIM7080G`；`uart_level_shift=Q1/Q2 SS8050 Y1`；`sim=U2 SIM`；`antenna=E1 ANT_IPEX`；`edge=J1 StampCatM_Pin`；`power=+5V -> U1 GM9308/HM8089 -> +3.3V`；`low_voltage=M1 VDD_EXT -> +1.8V` |
| 核心器件 | SIM7080G 主要引脚分组 | `uart1=TXD pin1; RXD pin2`；`sim=DATA15; CLK16; RST17; VDD18`；`usb=DM26; DP25; VBUS24`；`uart2=RXD23; TXD22`；`rf=ANT32`；`power=VBAT34/35; VDD_EXT40`；`status=NETLIGHT41; STATUS42`；`control=PWRKEY39` |
| 电源 | +5 V 至 +3.3 V 降压 | `input=+5V`；`converter=U1 GM9308/HM8089`；`enable=pin1 +5V`；`switch=pin3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R1 68KΩ; R2 15KΩ`；`ground=pin2` |
| 电源 | 降压输入输出去耦 | `input_caps=C3 22uF; C4 100nF`；`output_caps=C2 22uF; C1 100nF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | SIM7080G 主供电 | `supply=+3.3V`；`vbat_pins=34/35`；`ground_pins=8/13/19/21/27/30/31/33/36/37` |
| 电源 | SIM7080G +1.8 V 输出 | `source=M1 VDD_EXT pin40`；`rail=+1.8V`；`decoupling=C5 22uF`；`loads=R5/R7/R8/R10 UART-side pullups` |
| 总线 | SIM7080G UART1 | `module_tx=M1 pin1 U1_TX -> Q2 -> NB_TX`；`module_rx=NB_RX -> Q1 -> U1_RX -> M1 pin2`；`module_level=+1.8V pullups`；`external_level=+3.3V pullups`；`edge=J1 pins2/3` |
| 接口 | UART 1.8 V/3.3 V 电平转换 | `rx_external_pullup=R6 4.7KΩ to +3.3V`；`rx_module_pullup=R7 4.7KΩ to +1.8V`；`tx_external_pullup=R9 4.7KΩ to +3.3V`；`tx_module_pullup=R10 4.7KΩ to +1.8V`；`transistors=Q1/Q2 SS8050 Y1` |
| 接口 | SIM 卡接口 | `vcc=U2 pin1 SIM_VCC -> M1 pin18 SIM_VDD`；`reset=U2 pin2 -> M1 pin17`；`clock=U2 pin3 -> M1 pin16`；`data=U2 pin7 -> M1 pin15`；`ground=U2 pin5`；`vpp=pin6 no-connect` |
| 射频 | 蜂窝 IPEX 天线 | `source=M1 ANT pin32`；`connector=E1 ANT_IPEX`；`edge=J1 pin1 ANT`；`shield=GND`；`matching=not shown`；`esd=not shown` |
| 接口 | StampCatM 六针接口 | `pin1=ANT`；`pin2=NB_TX`；`pin3=NB_RX`；`pin4=GND`；`pin5=+3.3V`；`pin6=+5V` |
| 接口 | 3.3 V 电源指示灯 | `supply=+3.3V`；`led=D1 红灯0603`；`resistor=R3 1KΩ`；`destination=GND` |
| 接口 | 未使用的 SIM7080G 接口 | `uart1_modem=pins3-7 NC`；`pcm=pins9-12 NC`；`analog_gpio=ADC38; GPIO5 14 NC`；`usb=pins26/25/24 and USB_BOOT20 NC`；`uart2=pins23/22 NC` |
| 射频 | Cat-M/NB-IoT 频段与性能 | `document_modes=Cat-M and NB-IoT`；`document_catm_rate=1119Kbps uplink; 589Kbps downlink`；`document_nbiot_rate=150Kbps uplink; 136Kbps downlink`；`document_power=Class 5, typ. 21dBm`；`schematic_parameters=not shown` |
| 总线 | UART 115200 8N1 与 AT 协议 | `document_uart=115200bps 8N1`；`document_control=AT Command`；`document_protocols=TCP/UDP/HTTP/HTTPS/TLS/DTLS/PING/LWM2M/COAP/MQTT`；`schematic_uart=UART1_TXD/RXD only` |
| 接口 | MicroSIM 与 IPEX-to-SMA 配件 | `document_sim=MicroSIM`；`schematic_sim=U2 SIM`；`document_antenna=SMA antenna via IPEX cable`；`schematic_antenna=E1 ANT_IPEX`；`sma_reference=null` |
| 电源 | 待机与入网电流 | `document_standby=5V@46mA`；`document_network=5V@71mA`；`schematic_measurement=not shown`；`network_conditions=not shown` |

## 待确认事项

- `rf.modes-bands-performance`：产品正文列出 Cat-M、NB-IoT、多频段、上下行速率和 21 dBm 功率等级，但原理图只标 SIM7080G，未打印频段或射频性能。（证据：图 55e21a6abc49 / 第 1 页 / M1 SIM7080G block lacks RF table）
- `bus.uart-at-protocol`：产品正文称 UART 115200 8N1、AT Command 以及 TCP/UDP/HTTP/TLS/MQTT 等协议，原理图只确认 UART1 电气连接，未打印波特率或固件协议。（证据：图 55e21a6abc49 / 第 1 页 / M1 UART1/Q1/Q2 path lacks configuration labels）
- `interface.sim-antenna-form`：产品正文称卡槽为 MicroSIM 并随附 IPEX-to-SMA 馈线与 SMA 天线；原理图 U2 只标 SIM、E1 标 ANT_IPEX，没有 SIM 机械规格、SMA 或馈线位号。（证据：图 55e21a6abc49 / 第 1 页 / U2 generic SIM and E1 ANT_IPEX）
- `power.operating-current`：产品正文给出 5 V 待机 46 mA、入网 71 mA，但原理图未提供测试模式、网络条件或电流测量数据。（证据：图 55e21a6abc49 / 第 1 页 / +5V/U1/+3.3V/M1 power path lacks current annotations）
- `review.modes-bands-performance`：请用当前 SIM7080G 变体规格与运营商配置复核 Cat-M/NB-IoT 频段、速率和功率等级。；原因：射频参数未印在原理图。
- `review.uart-at-protocol`：请用模组固件版本、AT 手册和串口实测确认 115200 8N1 及协议支持。；原因：这些配置与能力未印在原理图。
- `review.sim-antenna-form`：请用 BOM、装配图和包装清单确认 MicroSIM 卡座、IPEX-to-SMA 馈线与 SMA 天线。；原因：原理图只显示通用 SIM 符号和 IPEX。
- `review.operating-current`：请按明确网络、信号强度、UART 状态和供电条件复测待机及入网电流。；原因：原理图没有电流测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `55e21a6abc49e25c9cf36339d713bc3080ff8b0e1de58c4a92b8145a281c426f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/569/Sch_StampCatM_sch_01.png` |

---

源文档：`zh_CN/stamp/stamp_catm.md`

源文档 SHA-256：`72254115fbd682fa4b9335dc711af1b0e2a02689faf8dbfbbe4a111feb6388cf`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
