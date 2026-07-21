# Atomic QRCode2 Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic QRCode2 Base |
| SKU | A133-B |
| 产品 ID | `atomic-qrcode2-base-06fd4484ce87` |
| 源文档 | `zh_CN/atom/Atomic QRCode2 Base.md` |

## 概述

Atomic QRCode2 Base 通过 U1 FPC-12P 连接二维码模块，模块使用 +5V/GND 供电，并以 RX/TX、TRIG、DLED 和 BEEP 信号连接 Atom 及板载蜂鸣器电路。P1 Header 5 接出 +3.3V、TX、RX、TRIG 和经 R5 0Ω 串联的 DLED，P2 Header 4 只使用 +5V 与 GND。BEEP 经 R1 驱动 Q1 SS8050 Y1，Q1 低侧控制 LS1 Buzzer，D1 1N4007WS 跨接蜂鸣器两端。

## 检索关键词

`Atomic QRCode2 Base`、`A133-B`、`QRCode V2.0`、`FPC-12P`、`QR_RX`、`QR_TX`、`RX`、`TX`、`TRIG`、`DLED`、`BEEP`、`BUZ`、`LS1 Buzzer`、`SS8050 Y1`、`1N4007WS`、`UART`、`+5V`、`+3.3V`、`P1 Header 5`、`P2 Header 4`、`R5 0R`、`R3 10K`、`R4 4.7R`、`DM-`、`DP+`、`buzzer driver`、`flyback diode`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | FPC-12P | 连接二维码模块电源、串行通信、触发、照明和蜂鸣器控制信号 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C1，U1 FPC-12P 的 pin1-pin12 与 TRIG/LED/BUZ/DP+/DM-/QR_TX/QR_RX/GND/VCC/NC |
| LS1 | Buzzer | 由 Q1 低侧开关控制的板载蜂鸣器 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，LS1 Buzzer 位于 R4/+3.3V 与 Q1 集电极之间 |
| Q1 | SS8050 Y1 | 接收 BEEP 基极控制并将蜂鸣器下端切换至 GND 的晶体管 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，Q1 SS8050 Y1，基极接 R1/R2 节点、发射极接 GND、集电极接 LS1 |
| D1 | 1N4007WS | 跨接 LS1 蜂鸣器两端的二极管 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，D1 1N4007WS 与 LS1 并联，连接 R4 后电源节点和 Q1 集电极节点 |
| P1 | Header 5 | Atom 侧 +3.3V、TX、RX、TRIG 和 DLED 接口 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C3，P1 Header 5，pin1 +3.3V、pin2 TX、pin3 RX、pin4 TRIG、pin5 经 R5 接 DLED |
| P2 | Header 4 | Atom 侧 +5V 和 GND 电源接口，pin1/pin2 未连接 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C3，P2 Header 4，pin1/pin2 no-connect、pin3 +5V、pin4 GND |
| R1,R2 | 1KΩ / 10KΩ | Q1 基极串联电阻和下拉电阻 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，BEEP 经 R1 1K 到 Q1 基极，R2 10K 从基极节点接 GND |
| R3,R5 | 10KΩ / 0Ω | DLED 的 +3.3V 上拉与 P1 串联跳线 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C1/C3，R3 10K 从 DLED 到 +3.3V，R5 0R 串联 P1 pin5 与 DLED |
| R4 | 4.7Ω | +3.3V 到 LS1 蜂鸣器上端的串联电阻 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，+3.3V 经 R4 4.7R 接 LS1 上端和 D1 上端 |
| C1,C2,C3,C4 | 100nF / 100nF / 100nF / 10uF | +3.3V 与 +5V 电源去耦 | 图 ed3022bc3065 / 第 1 页 / 第 1 页 C1-C3，C1/C2 100nF 从 +3.3V 到 GND，C3 100nF 与 C4 10uF 从 +5V 到 GND |

## 系统结构

### Atomic QRCode2 Base 模块连接架构

U1 FPC-12P 将二维码模块的 +5V/GND、RX/TX、TRIG、DLED 和 BEEP 接入底板；P1/P2 与 Atom 连接，BEEP 另经 Q1 驱动 LS1 蜂鸣器。

- 参数与网络：`module_connector=U1 FPC-12P`；`host_connectors=P1 Header 5, P2 Header 4`；`serial_signals=RX, TX`；`control_signals=TRIG, DLED, BEEP`；`buzzer_driver=Q1 SS8050 Y1`；`buzzer=LS1 Buzzer`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1-C3，U1、蜂鸣器驱动、P1/P2 和全部同名网络

## 电源

### 二维码模块 +5V 供电

P2 pin3 的 +5V 连接 U1 VCC pin11，C3 100nF 与 C4 10uF 并联连接 +5V 和 GND；U1 GND pin10 接 GND。

- 参数与网络：`input=P2 pin3 +5V`；`module_vcc=U1 pin11 VCC`；`module_ground=U1 pin10 GND`；`decoupling=C3 100nF, C4 10uF`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1/C3，P2 +5V/GND 与 U1 VCC/GND、C3/C4

### +3.3V 控制和蜂鸣器电源

P1 pin1 提供 +3.3V，C1/C2 两个 100nF 电容连接 +3.3V 与 GND；该电源还连接 R3 DLED 上拉和 R4 蜂鸣器供电电阻。

- 参数与网络：`input=P1 pin1 +3.3V`；`decoupling=C1 100nF, C2 100nF`；`DLED_pullup=R3 10K`；`buzzer_supply=R4 4.7R`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1-C3，P1 +3.3V、C1/C2、R3 与 R4 的同名电源网络

## 接口

### U1 FPC-12P 针脚映射

U1 pin12=NC、pin11=VCC/+5V、pin10=GND、pin9=QR_RX/RX、pin8=QR_TX/TX、pin7=DM-、pin6=DP+、pin5=NC、pin4=BUZ/BEEP、pin3=LED/DLED、pin2=NC、pin1=TRIG。

- 参数与网络：`pin12=NC`；`pin11=VCC +5V`；`pin10=GND`；`pin9=QR_RX RX`；`pin8=QR_TX TX`；`pin7=DM-`；`pin6=DP+`；`pin5=NC`；`pin4=BUZ BEEP`；`pin3=LED DLED`；`pin2=NC`；`pin1=TRIG`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1，U1 FPC-12P pin1-pin12 的逐行标签和网络

### P1/P2 Atom 连接器映射

P1 Header 5 的 pin1=+3.3V、pin2=TX、pin3=RX、pin4=TRIG、pin5 经 R5 0Ω 接 DLED；P2 Header 4 的 pin1/pin2 未连接、pin3=+5V、pin4=GND。

- 参数与网络：`P1=pin1 +3.3V, pin2 TX, pin3 RX, pin4 TRIG, pin5 R5 0R to DLED`；`P2=pin1 NC, pin2 NC, pin3 +5V, pin4 GND`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C3，P1 Header 5、P2 Header 4 与 R5 0R

### FPC 未接针脚

U1 pin12、pin5 和 pin2 标为 NC；DM- pin7 与 DP+ pin6 在当前原理图中未连接到其他器件或连接器。

- 参数与网络：`NC_pins=pin12, pin5, pin2`；`unrouted_signals=pin7 DM-, pin6 DP+`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1，U1 NC/DM-/DP+ 行及其无外部连线的端点

## 总线

### 二维码模块 RX/TX 串行连接

U1 QR_RX pin9 连接 RX 网络并到达 P1 pin3，U1 QR_TX pin8 连接 TX 网络并到达 P1 pin2。

- 参数与网络：`RX=U1 QR_RX pin9 -> P1 pin3`；`TX=U1 QR_TX pin8 -> P1 pin2`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1/C3，U1 QR_RX/QR_TX 与 P1 RX/TX 的同名网络

## GPIO 与控制信号

### TRIG 与 DLED 控制信号

TRIG 直接连接 U1 pin1 与 P1 pin4；DLED 连接 U1 LED pin3，由 R3 10KΩ 上拉到 +3.3V，并经 R5 0Ω 连接 P1 pin5。

- 参数与网络：`TRIG=U1 pin1 <-> P1 pin4`；`DLED=U1 pin3 <-> R5 0R <-> P1 pin5`；`DLED_pullup=R3 10K to +3.3V`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1/C3，U1 TRIG/LED、R3、R5 与 P1 pin4/pin5

## 保护电路

### 蜂鸣器并联二极管

D1 1N4007WS 跨接 LS1 两端，一端连接 R4 后的蜂鸣器电源节点，另一端连接 Q1 集电极和 LS1 下端。

- 参数与网络：`device=D1 1N4007WS`；`upper_node=R4 output / LS1 upper terminal`；`lower_node=Q1 collector / LS1 lower terminal`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C2，D1 1N4007WS 与 LS1 Buzzer 的并联连接

## 音频

### BEEP 蜂鸣器驱动

U1 BUZ pin4 的 BEEP 网络经 R1 1KΩ 接 Q1 基极，R2 10KΩ 将基极节点下拉到 GND；Q1 SS8050 Y1 发射极接 GND、集电极接 LS1 下端，LS1 上端经 R4 4.7Ω 接 +3.3V。

- 参数与网络：`control=U1 BUZ pin4 BEEP`；`base_resistor=R1 1K`；`base_pulldown=R2 10K to GND`；`switch=Q1 SS8050 Y1`；`load=LS1 Buzzer`；`supply_path=+3.3V -> R4 4.7R -> LS1 -> Q1 -> GND`
- 证据：图 ed3022bc3065 / 第 1 页 / 第 1 页 C1-C2，U1 BUZ/BEEP 到 R1/R2/Q1/LS1/R4/GND 的完整链路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic QRCode2 Base 模块连接架构 | `module_connector=U1 FPC-12P`；`host_connectors=P1 Header 5, P2 Header 4`；`serial_signals=RX, TX`；`control_signals=TRIG, DLED, BEEP`；`buzzer_driver=Q1 SS8050 Y1`；`buzzer=LS1 Buzzer` |
| 接口 | U1 FPC-12P 针脚映射 | `pin12=NC`；`pin11=VCC +5V`；`pin10=GND`；`pin9=QR_RX RX`；`pin8=QR_TX TX`；`pin7=DM-`；`pin6=DP+`；`pin5=NC`；`pin4=BUZ BEEP`；`pin3=LED DLED`；`pin2=NC`；`pin1=TRIG` |
| 总线 | 二维码模块 RX/TX 串行连接 | `RX=U1 QR_RX pin9 -> P1 pin3`；`TX=U1 QR_TX pin8 -> P1 pin2` |
| 接口 | P1/P2 Atom 连接器映射 | `P1=pin1 +3.3V, pin2 TX, pin3 RX, pin4 TRIG, pin5 R5 0R to DLED`；`P2=pin1 NC, pin2 NC, pin3 +5V, pin4 GND` |
| GPIO 与控制信号 | TRIG 与 DLED 控制信号 | `TRIG=U1 pin1 <-> P1 pin4`；`DLED=U1 pin3 <-> R5 0R <-> P1 pin5`；`DLED_pullup=R3 10K to +3.3V` |
| 音频 | BEEP 蜂鸣器驱动 | `control=U1 BUZ pin4 BEEP`；`base_resistor=R1 1K`；`base_pulldown=R2 10K to GND`；`switch=Q1 SS8050 Y1`；`load=LS1 Buzzer`；`supply_path=+3.3V -> R4 4.7R -> LS1 -> Q1 -> GND` |
| 保护电路 | 蜂鸣器并联二极管 | `device=D1 1N4007WS`；`upper_node=R4 output / LS1 upper terminal`；`lower_node=Q1 collector / LS1 lower terminal` |
| 电源 | 二维码模块 +5V 供电 | `input=P2 pin3 +5V`；`module_vcc=U1 pin11 VCC`；`module_ground=U1 pin10 GND`；`decoupling=C3 100nF, C4 10uF` |
| 电源 | +3.3V 控制和蜂鸣器电源 | `input=P1 pin1 +3.3V`；`decoupling=C1 100nF, C2 100nF`；`DLED_pullup=R3 10K`；`buzzer_supply=R4 4.7R` |
| 接口 | FPC 未接针脚 | `NC_pins=pin12, pin5, pin2`；`unrouted_signals=pin7 DM-, pin6 DP+` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ed3022bc30657f5d0916ed3f38e9a579463b1c76b952688c5fa3ef7191227c68` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/SCH_AtomicQRCode_V2.0pdf_sch_01.png` |

---

源文档：`zh_CN/atom/Atomic QRCode2 Base.md`

源文档 SHA-256：`3a06ebf188040465b8fb0a0087eb3ae708040683c11298489f80223b64968f3f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
