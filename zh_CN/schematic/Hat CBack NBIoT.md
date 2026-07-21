# Hat CBack NBIoT 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat CBack NBIoT |
| SKU | A113 |
| 产品 ID | `hat-cback-nbiot-ddfc8e81e058` |
| 源文档 | `zh_CN/hat/C-BACK NB-IoT(SIM7020G).md` |

## 概述

Hat CBack NBIoT 以 IC1 SIM7020 蜂窝通信模组为核心，连接 Nano SIM 卡座、COM1 IPEX 射频座和主机 UART。VDD_BAT 经 U2 SY8003ADFC 降压为 VCC_3V0 供给模组 VBAT，U1 TXS0102DCUR 在模组 VDD_EXT 与主机 VCC_3V3 电平域之间转换 UART_TX/UART_RX。JP1 八针接口引出 UART 对应 GPIO26/GPIO36、PWRKEY/G0 及多路电源。

## 检索关键词

`Hat CBack NBIoT`、`A113`、`SIM7020`、`SIM7020G`、`SY8003ADFC`、`TXS0102DCUR`、`Nano SIM`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SIM_VCC`、`UART_TX`、`UART_RX`、`GROVE_IO1 G26`、`GROVE_IO2 G36`、`PWRKEY G0`、`VDD_BAT`、`VCC_3V0`、`VDD_EXT`、`VCC_3V3`、`VCC_5V_IN`、`VCC_5V`、`COM1 IPEX`、`L1 2.2uH`、`R3 52K`、`R5 12K`、`RP1 3R3`、`JP1`、`J1 SIM`、`NB-IoT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| IC1 | SIM7020 | NB-IoT 通信模组，连接 UART、SIM 卡、电源、PWRKEY 和射频接口 | 图 3f78fc9fa4cd / 第 1 页 / 第1页左上：IC1 SIM7020 pins1-42 |
| U2 | SY8003ADFC | VDD_BAT 到 VCC_3V0 的降压转换器 | 图 3f78fc9fa4cd / 第 1 页 / 第1页左下：U2 SY8003ADFC、L1、R2-R5 |
| U1 | TXS0102DCUR | VDD_EXT 与 VCC_3V3 电平域之间的双通道 UART 电平转换器 | 图 3f78fc9fa4cd / 第 1 页 / 第1页中右：U1 TXS0102DCUR |
| J1 | SIM | Nano SIM 卡座，连接 SIM_VCC/RST/DATA/CLK 与 GND | 图 3f78fc9fa4cd / 第 1 页 / 第1页右上：J1 SIM pins1-6 |
| JP1 | 未标注 | M5StickC 系列主机 8 针电源、UART 与 PWRKEY 接口 | 图 3f78fc9fa4cd / 第 1 页 / 第1页右上：JP1 pins1-8 |
| COM1 | IPEX座子 | SIM7020 ANT 射频天线接口 | 图 3f78fc9fa4cd / 第 1 页 / 第1页中央：COM1 IPEX座子与 IC1 ANT pin32 |
| RP1 | 3R3/1% | SIM_DATA/SIM_CLK/SIM_RST 三路串联电阻阵列 | 图 3f78fc9fa4cd / 第 1 页 / 第1页左中：RP1 3R3/1% |
| L1 | 2.2uH | U2 LX 到 VCC_3V0 的降压储能电感 | 图 3f78fc9fa4cd / 第 1 页 / 第1页左下：L1 2.2uH |

## 系统结构

### Hat CBack NBIoT 架构

IC1 SIM7020 连接 J1 SIM 卡座、COM1 IPEX 射频座、PWRKEY 和 UART；U2 生成 VCC_3V0，U1 将 UART 转换到 VCC_3V3 主机域，JP1 提供主机连接。

- 参数与网络：`modem=IC1 SIM7020`；`power=U2 SY8003ADFC`；`level_shifter=U1 TXS0102DCUR`；`sim=J1 SIM`；`rf=COM1 IPEX座子`；`host=JP1`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页完整单页

## 电源

### VDD_BAT 到 VCC_3V0

U2 SY8003ADFC IN pin3 接 VDD_BAT，LX pin6 经 L1 2.2uH 输出 VCC_3V0；FB 使用 R3 52KΩ/1% 与 R5 12KΩ/1%，输出并联 C5/C9 226/6.3V/10%。

- 参数与网络：`converter=U2 SY8003ADFC`；`input=VDD_BAT`；`inductor=L1 2.2uH`；`output=VCC_3V0`；`feedback_top=R3 52KΩ/1%`；`feedback_bottom=R5 12KΩ/1%`；`input_cap=C10 226/6.3V/10%`；`output_caps=C5/C9 226/6.3V/10%`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页左下：U2/L1/R2-R5/C1/C5/C9/C10

### SY8003 使能网络

U2 EN pin7 由 VCC_3V3 经 R2 10KΩ/1% 与 R4 22KΩ/1% 分压控制，PG pin2 与 EN 节点连接。

- 参数与网络：`enable=U2 EN pin7`；`pullup=R2 10KΩ/1% to VCC_3V3`；`pulldown=R4 22KΩ/1% to GND`；`power_good=U2 PG pin2 tied to enable node`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页左下：U2 pins2/7、R2/R4

### SIM7020 电源域

IC1 VBAT pins34/35 接 VCC_3V0，VDD_EXT pin40 输出 VDD_EXT，SIM_VDD pin18 形成 SIM_VCC；C6 104/6.3V/10% 从 SIM_VCC 对地。

- 参数与网络：`main_supply=IC1 VBAT pins34/35 -> VCC_3V0`；`io_supply=IC1 VDD_EXT pin40 -> VDD_EXT`；`sim_supply=IC1 SIM_VDD pin18 -> SIM_VCC`；`sim_decoupling=C6 104/6.3V/10%`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 pins18/34/35/40 与 C6

## 接口

### JP1 主机接口

JP1 pins1-8 依次为 VCC_5V_IN、VCC_3V3、VDD_BAT、PWRKEY/G0、GROVE_IO2/G36、GROVE_IO1/G26、VCC_5V、GND。

- 参数与网络：`pin1=VCC_5V_IN`；`pin2=VCC_3V3`；`pin3=VDD_BAT`；`pin4=PWRKEY / G0`；`pin5=GROVE_IO2 / G36`；`pin6=GROVE_IO1 / G26`；`pin7=VCC_5V`；`pin8=GND`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页右上：JP1 pins1-8

### Nano SIM 接口

J1 pins1-6 为 GND、SIM_VCC、VPP/NC、SIM_RST、SIM_DATA、SIM_CLK；SIM_RST/DATA/CLK 分别经 RP1 3.3Ω/1% 串联到 IC1 pins17/15/16。

- 参数与网络：`connector=J1 SIM`；`pin1=GND`；`pin2=SIM_VCC`；`pin3=VPP / NC`；`pin4=SIM_RST`；`pin5=SIM_DATA`；`pin6=SIM_CLK`；`series=RP1 3R3/1% on RST/DATA/CLK`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页左中/右上：IC1 SIM pins15-18、RP1、J1

## 总线

### 主机 UART 与电平转换

IC1 UART1_TXD pin1 形成 UART_TX，经 U1 A1/B1 连接 GROVE_IO2/G36；IC1 UART1_RXD pin2 形成 UART_RX，经 U1 A2/B2 连接 GROVE_IO1/G26。U1 A 侧由 VDD_EXT 供电，B 侧由 VCC_3V3 供电。

- 参数与网络：`modem_tx=IC1 pin1 UART_TX -> U1 A1/B1 -> GROVE_IO2 -> JP1 pin5 G36`；`modem_rx=JP1 pin6 G26 -> GROVE_IO1 -> U1 B2/A2 -> UART_RX -> IC1 pin2`；`a_level=VDD_EXT`；`b_level=VCC_3V3`；`direction=G36 receives modem TX; G26 drives modem RX`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 pins1/2、U1 A1/A2/B1/B2、JP1 pins5/6

## GPIO 与控制信号

### PWRKEY 控制

IC1 PWRKEY pin39 连接 PWRKEY 并引到 JP1 pin4/G0；R1 10KΩ/1% 与 C2 104/6.3V/10% 均从 PWRKEY 对地。

- 参数与网络：`modem_pin=IC1 PWRKEY pin39`；`host=JP1 pin4 / G0`；`resistor=R1 10KΩ/1% to GND`；`capacitor=C2 104/6.3V/10% to GND`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 pin39、JP1 pin4、R1/C2

### 未外接状态与控制脚

IC1 STATUS pin42、NETLIGHT pin41、RESET pin28、GPIO1 pin29、USB_DN/DP/VBUS pins26/25/24 和 UART2 pins23/22 在图中未连接到外部网络。

- 参数与网络：`unconnected=STATUS,NETLIGHT,RESET,GPIO1,USB_DN,USB_DP,USB_VBUS,UART2_RXD,UART2_TXD`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 right pins22-29/41-42

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟连接器。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_connector_shown=false`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页完整单页，无 X/Y 时钟器件位号

## 保护电路

### 外部接口保护可见性

本页未画 SIM、UART、JP1 或 COM1 信号上的 TVS/ESD 器件；可见串联器件仅为 SIM 信号 RP1 3.3Ω阵列。

- 参数与网络：`tvs_esd_shown=false`；`sim_series=RP1 3R3/1%`；`interfaces=J1,JP1,COM1`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页完整单页接口与保护器件范围

## 射频

### SIM7020 射频接口

IC1 ANT pin32 直接连接 COM1 pin2，COM1 标注 IPEX座子，COM1 pin1 接 GND。

- 参数与网络：`modem_pin=IC1 ANT pin32`；`connector=COM1 IPEX座子`；`signal_pin=COM1 pin2`；`ground=COM1 pin1`
- 证据：图 3f78fc9fa4cd / 第 1 页 / 第1页中央：IC1 ANT pin32/COM1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat CBack NBIoT 架构 | `modem=IC1 SIM7020`；`power=U2 SY8003ADFC`；`level_shifter=U1 TXS0102DCUR`；`sim=J1 SIM`；`rf=COM1 IPEX座子`；`host=JP1` |
| 电源 | VDD_BAT 到 VCC_3V0 | `converter=U2 SY8003ADFC`；`input=VDD_BAT`；`inductor=L1 2.2uH`；`output=VCC_3V0`；`feedback_top=R3 52KΩ/1%`；`feedback_bottom=R5 12KΩ/1%`；`input_cap=C10 226/6.3V/10%`；`output_caps=C5/C9 226/6.3V/10%` |
| 电源 | SY8003 使能网络 | `enable=U2 EN pin7`；`pullup=R2 10KΩ/1% to VCC_3V3`；`pulldown=R4 22KΩ/1% to GND`；`power_good=U2 PG pin2 tied to enable node` |
| 电源 | SIM7020 电源域 | `main_supply=IC1 VBAT pins34/35 -> VCC_3V0`；`io_supply=IC1 VDD_EXT pin40 -> VDD_EXT`；`sim_supply=IC1 SIM_VDD pin18 -> SIM_VCC`；`sim_decoupling=C6 104/6.3V/10%` |
| 总线 | 主机 UART 与电平转换 | `modem_tx=IC1 pin1 UART_TX -> U1 A1/B1 -> GROVE_IO2 -> JP1 pin5 G36`；`modem_rx=JP1 pin6 G26 -> GROVE_IO1 -> U1 B2/A2 -> UART_RX -> IC1 pin2`；`a_level=VDD_EXT`；`b_level=VCC_3V3`；`direction=G36 receives modem TX; G26 drives modem RX` |
| 接口 | JP1 主机接口 | `pin1=VCC_5V_IN`；`pin2=VCC_3V3`；`pin3=VDD_BAT`；`pin4=PWRKEY / G0`；`pin5=GROVE_IO2 / G36`；`pin6=GROVE_IO1 / G26`；`pin7=VCC_5V`；`pin8=GND` |
| 接口 | Nano SIM 接口 | `connector=J1 SIM`；`pin1=GND`；`pin2=SIM_VCC`；`pin3=VPP / NC`；`pin4=SIM_RST`；`pin5=SIM_DATA`；`pin6=SIM_CLK`；`series=RP1 3R3/1% on RST/DATA/CLK` |
| 射频 | SIM7020 射频接口 | `modem_pin=IC1 ANT pin32`；`connector=COM1 IPEX座子`；`signal_pin=COM1 pin2`；`ground=COM1 pin1` |
| GPIO 与控制信号 | PWRKEY 控制 | `modem_pin=IC1 PWRKEY pin39`；`host=JP1 pin4 / G0`；`resistor=R1 10KΩ/1% to GND`；`capacitor=C2 104/6.3V/10% to GND` |
| GPIO 与控制信号 | 未外接状态与控制脚 | `unconnected=STATUS,NETLIGHT,RESET,GPIO1,USB_DN,USB_DP,USB_VBUS,UART2_RXD,UART2_TXD` |
| 核心器件 | 通信模组型号后缀 | `schematic=SIM7020`；`documented=SIM7020G` |
| 接口 | 天线连接器描述差异 | `schematic=COM1 IPEX座子`；`documented=SMA antenna interface`；`sma_reference_shown=false` |
| 总线 | UART 波特率 | `documented_bitrate=115200bps`；`explicit_bitrate_on_schematic=false`；`interface=UART1_TXD/UART1_RXD` |
| 保护电路 | 外部接口保护可见性 | `tvs_esd_shown=false`；`sim_series=RP1 3R3/1%`；`interfaces=J1,JP1,COM1` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false`；`clock_connector_shown=false` |

## 待确认事项

- `component.modem-suffix`：原理图 IC1 打印 SIM7020，产品正文与产品名标称 SIM7020G；图中未打印 G 后缀。（证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 下方 SIM7020 标注）
- `interface.antenna-doc-conflict`：原理图将 COM1 标为 IPEX座子，产品正文标称 SMA 天线外部接口；图中未画 SMA 位号。（证据：图 3f78fc9fa4cd / 第 1 页 / 第1页中央：COM1 IPEX座子）
- `bus.uart-bitrate`：产品正文标称 UART 115200bps；原理图显示 UART 电气连接，但没有打印波特率。（证据：图 3f78fc9fa4cd / 第 1 页 / 第1页 IC1 UART1 pins1/2 与 U1 TXS0102DCUR）
- `review.modem-suffix`：A113 当前装配模组的完整型号是否为 SIM7020G？；原因：产品正文标称 SIM7020G，原理图 IC1 仅打印 SIM7020。
- `review.antenna-connector`：A113 对外天线连接路径是否由板上 IPEX 经转接形成 SMA？；原因：原理图仅显示 COM1 IPEX座子，产品正文描述 SMA 天线接口。
- `review.uart-bitrate`：A113 默认 UART 波特率是否固定为 115200bps？；原因：115200bps 来自产品正文，原理图未打印波特率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3f78fc9fa4cd495bedfffc0bc449fd78442b559bc42aa36e23cb60c785fa7b08` | `https://static-cdn.m5stack.com/resource/docs/products/hat/C-BACK NB-IoT(SIM7020G)/img-8181af47-822b-4626-b507-993b4fa955cb.webp` |

---

源文档：`zh_CN/hat/C-BACK NB-IoT(SIM7020G).md`

源文档 SHA-256：`b879492c6218efb66b609702d5f1e1836949316b92520b1a4322c36a18ce4b38`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
