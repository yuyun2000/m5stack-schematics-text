# Module COMX NBIoT-CN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module COMX NBIoT-CN |
| SKU | M031-B2 |
| 产品 ID | `module-comx-nbiot-cn-388620d06d52` |
| 源文档 | `zh_CN/module/comx_nbiot_cn.md` |

## 概述

Module COMX NBIoT-CN 由 HCore 底座与 SIM7020 核心电路组成，M1 原理图料号标为 SIM7020G/SIM7020C，通过 UART1 与主机通信并连接 SIM 卡和 ANT_IPEX 射频接口。主机侧 M_TXD/M_RXD 经 Q3/Q2 SS8050 与 3.3 V/1.8 V 电阻网络转换到 U1_TX/U1_RX。VIN 经 U3 JW5033H 降压为 +5.4V，再由 VR1 AMS1117-3.3 生成 +3.3V；RST 经 Q4 反相后拉低模块 RESET。

## 检索关键词

`Module COMX NBIoT-CN`、`M031-B2`、`SIM7020C`、`SIM7020G`、`SIM7020G/SIM7020C`、`NB-IoT`、`UART1_TXD`、`UART1_RXD`、`U1_TX`、`U1_RX`、`M_TXD`、`M_RXD`、`115200bps`、`JW5033H`、`AMS1117-3.3`、`+5.4V`、`+3.3V`、`+1.8V`、`SIM_VCC`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SMF05CT1G`、`ANT_IPEX`、`NETLIGHT`、`PWRKEY`、`RESET`、`RST`、`SS8050 Y1`、`HCore`、`Nano SIM`、`B1/B3/B5/B8`、`SMA antenna`、`VIN 5-12V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7020G/SIM7020C | NB-IoT 蜂窝通信模组，提供 UART、SIM、射频、复位和状态信号 | 图 674520ab1fc9 / 第 1 页 / 中央，M1 SIM7020G/SIM7020C pins 1-42 |
| U2 | SIM | SIM 卡座，提供 IO/CLK/RST/VCC/GND/VPP | 图 674520ab1fc9 / 第 1 页 / 左下，U2 SIM pins IO/CLK/RST/VCC/GND/VPP |
| U1 | SMF05CT1G | SIM_DATA/SIM_CLK/SIM_RST 的多路 ESD 保护阵列 | 图 674520ab1fc9 / 第 1 页 / 左中，U1 SMF05CT1G 接 SIM_VCC/GND 与三路 SIM 信号 |
| E1 | ANT_IPEX | M1 ANT pin32 的 IPEX 射频天线连接器 | 图 674520ab1fc9 / 第 1 页 / 右中，M1 pin32 ANT 至 E1 ANT_IPEX，外壳接 GND |
| Q2/Q3 | SS8050 Y1 | 主机 3.3 V UART 与模组 1.8 V UART 的双路晶体管电平转换 | 图 674520ab1fc9 / 第 1 页 / 下方，Q2/Q3 SS8050 Y1 与 R8-R13、M_RXD/M_TXD/U1_RX/U1_TX |
| Q1/D1 | SS8050 Y1 / LED 0603 | NETLIGHT 控制的网络状态指示灯驱动 | 图 674520ab1fc9 / 第 1 页 / 右上，NETLIGHT-R2-Q1 与 +3.3V-R1-D1 |
| U3 | JW5033H | VIN 至 +5.4V 的降压转换器 | 图 b53ff3ed62ac / 第 1 页 / 左上，U3 JW5033H 与 L1/R16/R18/C5-C8 |
| VR1 | AMS1117-3.3 | +5.4V 至 +3.3V 的线性稳压器 | 图 b53ff3ed62ac / 第 1 页 / 上中，VR1 AMS1117-3.3，Vin=+5.4V、Vout=+3.3V |
| Q4 | SS8050 Y1 | 主机 RST 至模组 RESET 的反相开漏式下拉驱动 | 图 b53ff3ed62ac / 第 1 页 / 右上，RST-R17-Q4 与 RESET/R14/C10 |
| J1 | HCore | COMX 核心连接器，承载 UART、RST、VIN 与 GND | 图 b53ff3ed62ac / 第 1 页 / 右下，J1 HCore pins 1-23 |

## 系统结构

### NB-IoT 模块架构

HCore J1 提供 VIN、UART 与 RST；底座将 VIN 转换为 +5.4V 和 +3.3V，UART 经 3.3V/1.8V 电平转换连接 M1 SIM7020G/SIM7020C，M1 再连接 SIM 卡、IPEX 天线和 NETLIGHT 指示电路。

- 参数与网络：`cellular_module=M1 SIM7020G/SIM7020C`；`host_connector=J1 HCore`；`host_bus=UART`；`power=VIN -> JW5033H +5.4V -> AMS1117-3.3 +3.3V`；`sim=U2`；`rf=E1 ANT_IPEX`
- 证据：图 674520ab1fc9 / 第 1 页 / 整页 SIM7020 核心与 SIM/RF/UART; 图 b53ff3ed62ac / 第 1 页 / 整页 HCore、电源与复位

## 电源

### SIM7020 电源轨

M1 VBAT pins34/35 通过 R4 0 Ω 连接 +3.3V，VDD_EXT pin40 输出 +1.8V 并由 C1 22 µF 对地；PWRKEY pin39 通过同一 R4/VBAT 节点固定连接。

- 参数与网络：`vbat=M1 pins34/35 +3.3V via R4 0Ω`；`vdd_ext=M1 pin40 +1.8V`；`vdd_ext_cap=C1 22uF`；`pwrkey=M1 pin39 tied through R4/VBAT node`
- 证据：图 674520ab1fc9 / 第 1 页 / M1 right pins34-40、R4 0Ω、+3.3V、+1.8V/C1

### VIN 至 5.4 V 转换

HCore J1 pins13/14 的 VIN 接 U3 JW5033H；U3、L1 4.7 µH、R16 115 kΩ/R18 20 kΩ 与 C7 22 µF 形成标为 +5.4V 的降压输出。

- 参数与网络：`input=J1 pins13/14 VIN`；`converter=U3 JW5033H`；`inductor=L1 4.7uH`；`feedback=R16 115KΩ; R18 20KΩ`；`output_cap=C7 22uF`；`output=+5.4V`
- 证据：图 b53ff3ed62ac / 第 1 页 / 左上 VIN/U3/L1/R16/R18/C7/+5.4V 与右下 J1 VIN

### 3.3 V 线性稳压

VR1 AMS1117-3.3 将 +5.4V 转为 +3.3V，输入有 C8 100 nF，输出有 C9 22 µF，并另设 C11/C12 各 100 µF 的 3.3 V 大容量去耦。

- 参数与网络：`ldo=VR1 AMS1117-3.3`；`input=+5.4V`；`output=+3.3V`；`input_cap=C8 100nF`；`output_caps=C9 22uF; C11/C12 100uF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 上中 VR1/C8/C9 与中左 C11/C12

## 接口

### SIM 卡接口

U2 SIM 卡座的 IO、CLK、RST 通过 R5/R6/R7 各 22 Ω 连接 M1 SIM_DATA pin15、SIM_CLK pin16、SIM_RST pin17；每线有 33 pF 对地电容并由 U1 SMF05CT1G 保护，VCC 接 SIM_VCC/M1 SIM_VDD pin18。

- 参数与网络：`socket=U2 SIM`；`data=R5 22Ω; C2 33pF`；`clock=R6 22Ω; C3 33pF`；`reset=R7 22Ω; C4 33pF`；`supply=SIM_VCC/M1 pin18`；`esd=U1 SMF05CT1G`；`supply_cap=C13 1uF`
- 证据：图 674520ab1fc9 / 第 1 页 / 左下，U2/U1/R5-R7/C2-C4/C13 与 M1 pins15-18

### HCore 已用引脚

J1 HCore 使用 pin6 TXD、pin7 RXD、pin10 RST、pins11/12 GND、pins13/14 VIN；其余可见 SC/SD/SR/SV/STA/RTS/PEN/VEXT/VTTL/CTS/RI/RTR/TXD2/RXD2/VBAT/NET 未在本页连接。

- 参数与网络：`pin6=TXD M_TXD`；`pin7=RXD M_RXD`；`pin10=RST`；`pins11_12=GND`；`pins13_14=VIN`；`unused_visible=SC/SD/SR/SV/STA/RTS/PEN/VEXT/VTTL/CTS/RI/RTR/TXD2/RXD2/VBAT/NET`
- 证据：图 b53ff3ed62ac / 第 1 页 / 右下 J1 HCore pins1-23

## 总线

### 主 UART 通信

M1 UART1_TXD pin1 标为 U1_TX，UART1_RXD pin2 标为 U1_RX；经 Q3/Q2 电平转换后分别连接 HCore J1 pin6 TXD/M_TXD 与 pin7 RXD/M_RXD。

- 参数与网络：`controller=external host`；`device=M1`；`module_tx=M1 pin1 UART1_TXD/U1_TX`；`module_rx=M1 pin2 UART1_RXD/U1_RX`；`host_tx=J1 pin6 TXD/M_TXD`；`host_rx=J1 pin7 RXD/M_RXD`；`level_shift=Q3 TX path; Q2 RX path`
- 证据：图 674520ab1fc9 / 第 1 页 / M1 pins1/2 与 Q2/Q3 UART 网络; 图 b53ff3ed62ac / 第 1 页 / J1 pins6/7 TXD/RXD 与 M_TXD/M_RXD

### UART 电平转换

Q2/Q3 均为 SS8050 Y1；主机侧 M_RXD/M_TXD 由 R9/R12 4.7 kΩ 上拉到 +3.3V，模组侧 U1_RX/U1_TX 由 R10/R13 4.7 kΩ 上拉到 +1.8V，并使用 R8/R11 4.7 kΩ 偏置晶体管。

- 参数与网络：`host_level=3.3V`；`module_level=1.8V`；`rx_transistor=Q2 SS8050 Y1`；`tx_transistor=Q3 SS8050 Y1`；`resistors=R8-R13 all 4.7KΩ`
- 证据：图 674520ab1fc9 / 第 1 页 / 下方 Q2/Q3 与 R8-R13、+3.3V/+1.8V

## GPIO 与控制信号

### 网络状态灯

M1 NETLIGHT pin41 经 R2 1 kΩ 驱动 Q1 SS8050 Y1，Q1 下拉 D1 LED；D1 由 +3.3V 经 R1 1 kΩ 供电，R3 10 kΩ 将 NETLIGHT 控制节点下拉。

- 参数与网络：`source=M1 pin41 NETLIGHT`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 0603`；`led_resistor=R1 1KΩ to +3.3V`
- 证据：图 674520ab1fc9 / 第 1 页 / 右上 NETLIGHT/R1-R3/Q1/D1

## 复位

### 主机控制模组复位

HCore J1 pin10 RST 经 R17 1 kΩ 驱动 Q4 SS8050 Y1，Q4 导通时将 RESET/M1 pin28 拉低；RESET 由 R14 10 kΩ 上拉到 +3.3V，并由 C10 100 nF 对地。

- 参数与网络：`host_reset=J1 pin10 RST`；`base_resistor=R17 1KΩ`；`transistor=Q4 SS8050 Y1`；`module_reset=M1 pin28 RESET`；`pullup=R14 10KΩ to +3.3V`；`capacitor=C10 100nF`
- 证据：图 b53ff3ed62ac / 第 1 页 / 右上 RESET/R14/C10/Q4/R17/RST 与右下 J1 pin10; 图 674520ab1fc9 / 第 1 页 / M1 pin28 RESET

## 射频

### 蜂窝射频接口

M1 ANT pin32 直接连接 E1 ANT_IPEX，E1 接地端连接 GND；页面未画射频匹配元件或 SMA 连接器。

- 参数与网络：`module_pin=M1 pin32 ANT`；`connector=E1 ANT_IPEX`；`matching_network=none shown`；`sma=none shown`
- 证据：图 674520ab1fc9 / 第 1 页 / M1 pin32 ANT 至 E1 ANT_IPEX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | NB-IoT 模块架构 | `cellular_module=M1 SIM7020G/SIM7020C`；`host_connector=J1 HCore`；`host_bus=UART`；`power=VIN -> JW5033H +5.4V -> AMS1117-3.3 +3.3V`；`sim=U2`；`rf=E1 ANT_IPEX` |
| 总线 | 主 UART 通信 | `controller=external host`；`device=M1`；`module_tx=M1 pin1 UART1_TXD/U1_TX`；`module_rx=M1 pin2 UART1_RXD/U1_RX`；`host_tx=J1 pin6 TXD/M_TXD`；`host_rx=J1 pin7 RXD/M_RXD`；`level_shift=Q3 TX path; Q2 RX path` |
| 总线 | UART 电平转换 | `host_level=3.3V`；`module_level=1.8V`；`rx_transistor=Q2 SS8050 Y1`；`tx_transistor=Q3 SS8050 Y1`；`resistors=R8-R13 all 4.7KΩ` |
| 接口 | SIM 卡接口 | `socket=U2 SIM`；`data=R5 22Ω; C2 33pF`；`clock=R6 22Ω; C3 33pF`；`reset=R7 22Ω; C4 33pF`；`supply=SIM_VCC/M1 pin18`；`esd=U1 SMF05CT1G`；`supply_cap=C13 1uF` |
| 射频 | 蜂窝射频接口 | `module_pin=M1 pin32 ANT`；`connector=E1 ANT_IPEX`；`matching_network=none shown`；`sma=none shown` |
| GPIO 与控制信号 | 网络状态灯 | `source=M1 pin41 NETLIGHT`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led=D1 0603`；`led_resistor=R1 1KΩ to +3.3V` |
| 电源 | SIM7020 电源轨 | `vbat=M1 pins34/35 +3.3V via R4 0Ω`；`vdd_ext=M1 pin40 +1.8V`；`vdd_ext_cap=C1 22uF`；`pwrkey=M1 pin39 tied through R4/VBAT node` |
| 电源 | VIN 至 5.4 V 转换 | `input=J1 pins13/14 VIN`；`converter=U3 JW5033H`；`inductor=L1 4.7uH`；`feedback=R16 115KΩ; R18 20KΩ`；`output_cap=C7 22uF`；`output=+5.4V` |
| 电源 | 3.3 V 线性稳压 | `ldo=VR1 AMS1117-3.3`；`input=+5.4V`；`output=+3.3V`；`input_cap=C8 100nF`；`output_caps=C9 22uF; C11/C12 100uF` |
| 复位 | 主机控制模组复位 | `host_reset=J1 pin10 RST`；`base_resistor=R17 1KΩ`；`transistor=Q4 SS8050 Y1`；`module_reset=M1 pin28 RESET`；`pullup=R14 10KΩ to +3.3V`；`capacitor=C10 100nF` |
| 接口 | HCore 已用引脚 | `pin6=TXD M_TXD`；`pin7=RXD M_RXD`；`pin10=RST`；`pins11_12=GND`；`pins13_14=VIN`；`unused_visible=SC/SD/SR/SV/STA/RTS/PEN/VEXT/VTTL/CTS/RI/RTR/TXD2/RXD2/VBAT/NET` |
| 核心器件 | SIM7020 实际装配型号 | `document_model=SIM7020C`；`schematic_marking=SIM7020G/SIM7020C`；`population=not confirmed` |
| 总线 | UART 波特率 | `claimed_baud=115200bps`；`frame_format=not printed`；`schematic=TX/RX only` |
| 射频 | 蜂窝频段与协议能力 | `claimed_bands=B1/B3/B5/B8`；`claimed_protocols=TCP/UDP/LWM2M/COAP/MQTT/HTTP/HTTPS/TLS/DTLS/DNS/NTP/PING`；`schematic_bands=not printed` |
| 电源 | 外部 VIN 输入范围 | `claimed_range=5-12V`；`schematic_input=VIN`；`connector_spec=not printed` |
| 射频 | 外置 SMA 天线链路 | `schematic_connector=E1 ANT_IPEX`；`claimed_external=SMA antenna`；`cable=not shown`；`antenna_gain=not printed` |

## 待确认事项

- `component.module-variant`：产品正文指定 SIM7020C，但原理图 M1 料号同时标为 SIM7020G/SIM7020C，无法仅凭页面确认实际装配变体。（证据：图 674520ab1fc9 / 第 1 页 / M1 下方 SIM7020G/SIM7020C 标记）
- `bus.uart-baud`：产品正文称 UART 为 115200 bps，但两页原理图仅显示 TX/RX 电路，未印出波特率或帧格式。（证据：图 674520ab1fc9 / 第 1 页 / M1 UART1 与电平转换网络）
- `rf.bands-protocols`：产品正文列出 B1/B3/B5/B8 及多种网络协议，但原理图仅标蜂窝模组与 ANT_IPEX，不包含频段或协议能力表。（证据：图 674520ab1fc9 / 第 1 页 / M1 与 E1 ANT_IPEX 区域）
- `power.vin-range`：产品正文警告 DC 输入为 5-12 V，但底座原理图仅标 VIN，没有印出允许输入范围或 DC 插座规格。（证据：图 b53ff3ed62ac / 第 1 页 / J1 VIN 与 U3 JW5033H 输入，页面无范围）
- `rf.sma-chain`：产品正文称使用 SMA 外置天线，但原理图只显示 E1 ANT_IPEX，未画 IPEX-SMA 馈线、SMA 位号或天线参数。（证据：图 674520ab1fc9 / 第 1 页 / M1 ANT pin32 与 E1 ANT_IPEX）
- `review.module-variant`：请用 M031-B2 BOM 或模组标签确认实际装配为 SIM7020C。；原因：原理图兼容标注 SIM7020G/SIM7020C。
- `review.uart-baud`：请用 SIM7020C 默认配置或产品固件确认 UART 115200 bps 与帧格式。；原因：通信速率未印在原理图。
- `review.bands-protocols`：请用已确认 SIM7020C 变体 datasheet 与运营商认证资料复核 B1/B3/B5/B8 和协议能力。；原因：频段和协议不属于原理图可见电气事实。
- `review.vin-range`：请用 JW5033H 设计计算和底座测试规范确认 DC 输入 5-12 V。；原因：原理图只标 VIN。
- `review.sma-chain`：请用装配图/BOM 确认 IPEX 至 SMA 馈线和外置天线规格。；原因：原理图只画 E1 ANT_IPEX。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `674520ab1fc99396cd26a53d743d037424bb1d228dbbd4fe7aa78aacf62b7f9b` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_sch_01.webp` |
| 2 | 1 | `b53ff3ed62accdb8f8b109383f9d030b20b89e047e4514a76c7d475af61c2d42` | `https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_sch_02.webp` |

---

源文档：`zh_CN/module/comx_nbiot_cn.md`

源文档 SHA-256：`b795577cf911558ff904c05314a63f5f337155779531c7e6ac5117bd49bbc297`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
