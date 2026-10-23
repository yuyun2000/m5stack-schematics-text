# Chain MIC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain MIC |
| SKU | U226 |
| 产品 ID | `chain-mic-7a26bc9bf2cb` |
| 源文档 | `zh_CN/chain/Chain_MIC.md` |

## 概述

Chain MIC 是以 STM32G031G8U6 为核心的链式麦克风节点：5V 经 TPA7343D-33FS4 LDO 得到 3.3V；GMI4015P-2C 驻极体经偏置与 RC 滤波后由 SGM321YC5/TR 运放放大约 100 倍送入 MCU 的 PA7/AIN；链路上下游各用一个 GROVE 接口，UART1/UART2 分别用于级联收发，另有 WS2812C-2020 状态灯和 5Pin SWD 调试口。

## 检索关键词

`Chain MIC`、`U226`、`STM32G031G8U6`、`TPA7343D-33FS4`、`SGM321YC5`、`WS2812C-2020`、`GMI4015P-2C`、`VCC_5V`、`VCC_3V3`、`AIN`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`SWD`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`GROVE_IO`、`RGB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控 MCU，处理麦克风采样、链路 UART 通信与 RGB 控制 | 图 8e80406304a6 / 第 1 页 / B/C 区：U1 符号与型号 STM32G031G8U6 |
| U2 | TPA7343D-33FS4 | 5V 转 3.3V LDO，为 MCU 与模拟电路供电 | 图 8e80406304a6 / 第 1 页 / A 区 LDO：U2 型号及 VIN/VOUT/EN 引脚 |
| U3 | WS2812C-2020 | 单线 RGB 状态指示灯 | 图 8e80406304a6 / 第 1 页 / B 区 RGB：U3 型号及 VDD/DI/DO/GND 引脚 |
| U4 | SGM321YC5/TR | 麦克风信号放大运放，输出至 MCU AIN | 图 8e80406304a6 / 第 1 页 / C/D 区 MIC：U4 型号及 +IN/-IN/OUT 引脚 |
| MK1 | GMI4015P-2C | 驻极体麦克风，1 脚为信号正端，2 脚接地 | 图 8e80406304a6 / 第 1 页 / C/D 区 MIC：MK1 型号与 1/2 脚 |
| J1 | GROVE_IO | 链路 IN 侧 GROVE 接口：IO2=TXD1、IO1=RXD1、VCC=VCC_5V、GND | 图 8e80406304a6 / 第 1 页 / A 区左侧：J1 GROVE_IO 及网络标注 |
| J2 | GROVE_IO | 链路 OUT 侧 GROVE 接口：IO2=RXD2、IO1=TXD2、VCC=VCC_5V、GND | 图 8e80406304a6 / 第 1 页 / A 区右侧：J2 GROVE_IO 及网络标注 |
| J4 | SWD_5P | 5 Pin 调试口：1=VCC_3V3、2=MCU_SWCLK、3=MCU_SWDIO、4=NRST、5=GND | 图 8e80406304a6 / 第 1 页 / B 区 RGB/SWD：J4 与 1~5 脚网络 |
| R2 | 10K | NRST 上拉到 VCC_3V3 | 图 8e80406304a6 / 第 1 页 / B 区 MCU 左侧：R2 10K |
| C1 | 1uF | NRST 对地滤波 | 图 8e80406304a6 / 第 1 页 / B 区 MCU 左侧：C1 1uF |
| R1 / R3 | 1K | 麦克风偏置分压/限流电阻 | 图 8e80406304a6 / 第 1 页 / C/D 区 MIC：R1、R3 均为 1K |
| C4 / C9 | 100nF / 10nF | 偏置滤波与麦克风信号耦合 | 图 8e80406304a6 / 第 1 页 / C/D 区 MIC：C4 100nF、C9 10nF |
| R4 / R7 | 1M | 运放同相端偏置分压 | 图 8e80406304a6 / 第 1 页 / C/D 区 MIC：R4 1M、R7 1M |
| R8 / C11 | 100K / 100pF | 运放反馈网络，决定约 100 倍增益 | 图 8e80406304a6 / 第 1 页 / D 区 MIC：R8 100K 与 C11 100pF 并联反馈 |
| R9 / C13 | 1K / 1uF | 运放反相端交流接地网络 | 图 8e80406304a6 / 第 1 页 / D 区 MIC：R9 1K 串 C13 1uF 到地 |

## 核心器件

### U1

U1 为 STM32G031G8U6，VDD/VDDA(3) 接 VCC_3V3，VSS/VSSA(4) 接地，PF2-NRST 为复位脚(5)。

- 参数与网络：`part=STM32G031G8U6`；`vdd_pin=3`；`vss_pin=4`；`nrst_pin=5`
- 证据：图 8e80406304a6 / 第 1 页 / B 区：U1 型号与 3/4/5 脚

## 电源

### U2

VCC_5V 输入 LDO U2 的 VIN(4) 与 EN(3)，VOUT(1) 输出 VCC_3V3，GND(2) 与 EP(5) 接地。

- 参数与网络：`input=VCC_5V`；`output=VCC_3V3`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`gnd_pin=2`；`ep_pin=5`
- 证据：图 8e80406304a6 / 第 1 页 / A 区 LDO：U2 引脚与电源网络

### C5-C8

LDO 输入侧 C6=100nF、C5=10uF，输出侧 C7=100nF、C8=10uF 均对地。

- 参数与网络：`input_100n=C6`；`input_10u=C5`；`output_100n=C7`；`output_10u=C8`
- 证据：图 8e80406304a6 / 第 1 页 / A 区 LDO：四个电容标注

### C12

C12(100nF) 跨接 VCC_3V3 与 GND，为 U3 去耦。

- 参数与网络：`cap=C12 100nF`
- 证据：图 8e80406304a6 / 第 1 页 / B 区 RGB 左侧

## 接口

### J1

J1(GROVE_IO, IN 方向)：IO2=TXD1，IO1=RXD1，VCC=VCC_5V，GND=GND。

- 参数与网络：`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 8e80406304a6 / 第 1 页 / A 区左侧 J1

### J2

J2(GROVE_IO, OUT 方向)：IO2=RXD2，IO1=TXD2，VCC=VCC_5V，GND=GND。

- 参数与网络：`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 8e80406304a6 / 第 1 页 / A 区右侧 J2

### U3

U3(WS2812C-2020)：VDD(4)=VCC_3V3，DI(3)=RGB 网络接 MCU PA8(16)，GND(2) 接地，DO(1) 悬空/级联输出。

- 参数与网络：`led=WS2812C-2020`；`vdd_pin=4`；`di_pin=3`；`gnd_pin=2`；`do_pin=1`；`data_net=RGB (PA8)`
- 证据：图 8e80406304a6 / 第 1 页 / B 区 RGB 与 U1 右侧

## 总线

### U1

UART1 使用 PB6(TXD1,26) 与 PB7(RXD1,27)，其中 TXD1/RXD1 引到 IN 侧 GROVE J1 的 IO2/IO1。

- 参数与网络：`tx=PB6`；`rx=PB7`；`connector=J1`
- 证据：图 8e80406304a6 / 第 1 页 / A 区 J1 与 B 区 U1 右侧

### U1

UART2 使用 PA2(TXD2,8) 与 PA3(RXD2,9)，TXD2/RXD2 引到 OUT 侧 GROVE J2 的 IO1/IO2。

- 参数与网络：`tx=PA2`；`rx=PA3`；`connector=J2`
- 证据：图 8e80406304a6 / 第 1 页 / A 区 J2 与 B 区 U1 左侧

## 复位

### U1

NRST 网络由 R2(10K) 上拉到 VCC_3V3，并由 C1(1uF) 对地；同时引到 SWD 接口 J4 第 4 脚。

- 参数与网络：`pullup=R2 10K`；`cap=C1 1uF`；`swd_pin=J4-4`
- 证据：图 8e80406304a6 / 第 1 页 / B 区 MCU 左侧与 J4

## 传感器

### MK1

MK1(GMI4015P-2C) 1 脚经 R3(1K) 接到偏置节点，偏置节点由 VCC_3V3 经 R1(1K) 供电并用 C4(100nF) 对地；2 脚接地。

- 参数与网络：`mic=GMI4015P-2C`；`bias_r=R1/R3 1K`；`bias_c=C4 100nF`
- 证据：图 8e80406304a6 / 第 1 页 / C/D 区 MIC 左侧

## 调试与烧录

### J4

J4(SWD_5P) 定义：1=VCC_3V3，2=MCU_SWCLK，3=MCU_SWDIO，4=NRST，5=GND。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND`
- 证据：图 8e80406304a6 / 第 1 页 / B 区 J4 与 1~5 脚

## 模拟电路

### U4

MK1 信号经 C9(10nF) 耦合到 U4(SGM321YC5/TR) 同相端(1)；同相端由 R4(1M) 上拉、R7(1M) 下拉偏置；U4 输出(4)=AIN 接 MCU PA7(13)。

- 参数与网络：`opamp=SGM321YC5/TR`；`in_plus=1`；`out=4`；`ain_pin=PA7/13`
- 证据：图 8e80406304a6 / 第 1 页 / C/D 区 MIC 与 U1 左侧

### U4

U4 反馈网络为 R8(100K) 并联 C11(100pF)，反相端经 R9(1K) 串 C13(1uF) 到地，构成约 100 倍同相放大。

- 参数与网络：`feedback_r=R8 100K`；`feedback_c=C11 100pF`；`gain_leg=R9 1K + C13 1uF`；`gain=约 100`
- 证据：图 8e80406304a6 / 第 1 页 / D 区 MIC 反馈网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 电源 | U2 | `input=VCC_5V`；`output=VCC_3V3`；`vin_pin=4`；`en_pin=3`；`vout_pin=1`；`gnd_pin=2`；`ep_pin=5` |
| 电源 | C5-C8 | `input_100n=C6`；`input_10u=C5`；`output_100n=C7`；`output_10u=C8` |
| 核心器件 | U1 | `part=STM32G031G8U6`；`vdd_pin=3`；`vss_pin=4`；`nrst_pin=5` |
| 复位 | U1 | `pullup=R2 10K`；`cap=C1 1uF`；`swd_pin=J4-4` |
| 调试与烧录 | J4 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND` |
| 总线 | U1 | `tx=PB6`；`rx=PB7`；`connector=J1` |
| 总线 | U1 | `tx=PA2`；`rx=PA3`；`connector=J2` |
| 接口 | J1 | `io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`gnd=GND` |
| 接口 | J2 | `io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`gnd=GND` |
| 传感器 | MK1 | `mic=GMI4015P-2C`；`bias_r=R1/R3 1K`；`bias_c=C4 100nF` |
| 模拟电路 | U4 | `opamp=SGM321YC5/TR`；`in_plus=1`；`out=4`；`ain_pin=PA7/13` |
| 模拟电路 | U4 | `feedback_r=R8 100K`；`feedback_c=C11 100pF`；`gain_leg=R9 1K + C13 1uF`；`gain=约 100` |
| 接口 | U3 | `led=WS2812C-2020`；`vdd_pin=4`；`di_pin=3`；`gnd_pin=2`；`do_pin=1`；`data_net=RGB (PA8)` |
| 电源 | C12 | `cap=C12 100nF` |

## 待确认事项

- `nr-1`：U3 的 DO(1) 是否在板上连接到下一颗 LED 或测试点？；原因：原理图该引脚仅画出短引线，未见明确网络名。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8e80406304a6c8519aecaf0fb0655399f0febb10a5d9dac1a7d53ecf6e901856` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1284/Chain_MIC_SCH_Main_V1.0_20250626_2026_07_10_13_59_52.png` |

---

源文档：`zh_CN/chain/Chain_MIC.md`

源文档 SHA-256：`975ee69dd4c51db85ec8694408c9dc24b11281eb1e3df2e39f81f24cc13e2513`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
