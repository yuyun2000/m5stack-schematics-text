# Atomic GPS Base v2.0 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic GPS Base v2.0 |
| SKU | A134-V2 |
| 产品 ID | `atomic-gps-base-v2-0-3fdbfd29ae64` |
| 源文档 | `zh_CN/atom/Atomic_GPS_Base_v2.0.md` |

## 概述

Atomic GPS Base v2.0 的本地原理图包含完整 GNSS 主链路。U5 天线经 C1/LB2 进入 U3 AT2659 低噪放，U3 RFOUT 连接 CN1 ATGM336H-6N-74 的 RF_IN。CN1 由 SYS_3V3 供电，TXD0/RXD0 经 22Ω 电阻形成 GPS_TX/GPS_RX，nRESET 引出为 nRST，1PPS 经 1KΩ 驱动 LED1，VBAT 连接 SYS_BAT 与 U1 33000uF 储能。U2 TPAP7343D-33FS4 从 5V 生成 3V3，再经 LB1 形成 SYS_3V3。正文中的 MAX2659 与图纸 AT2659 型号冲突；AT6668、多系统频点、精度灵敏度、NMEA/波特率、更新启动时间和功耗均不是本页直接标注的电气事实。

## 检索关键词

`Atomic GPS Base v2.0`、`A134-V2`、`ATGM336H-6N-74`、`AT6668`、`AT2659`、`MAX2659`、`BWGNSCNX15-15W4`、`GNSS`、`RF_IN`、`GPS_TX`、`GPS_RX`、`nRST`、`1PPS`、`SYS_3V3`、`SYS_BAT`、`TPAP7343D-33FS4`、`33000uF`、`UART`、`NMEA0183`、`115200bps`、`10Hz`、`GPS`、`BDS`、`GLONASS`、`GALILEO`、`QZSS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| CN1 | ATGM336H-6N-74 | GNSS 接收模组，连接 RF、UART、复位、1PPS、主电源与后备电源 | 图 cc705599f70e / 第 1 页 / 第 1 页 B2-B3 区 CN1 ATGM336H-6N-74，RF_IN/VCC/VBAT/nRESET/1PPS/RXD0/TXD0/GND |
| U3 | AT2659 | 天线与 CN1 RF_IN 之间的射频低噪声放大器 | 图 cc705599f70e / 第 1 页 / 第 1 页 B1-B2 区 U3 AT2659，SHDN/RFIN/VCC/GND/RFOUT |
| U5 | BWGNSCNX15-15W4 | 板载 GNSS 天线，经 C1 与 LB2 接入 U3 RFIN | 图 cc705599f70e / 第 1 页 / 第 1 页 B1 区 U5 BWGNSCNX15-15W4 天线符号与 C1 300pF/50V、LB2 6.8nH |
| U2 | TPAP7343D-33FS4 | 5V 到 3V3 的低压差稳压器 | 图 cc705599f70e / 第 1 页 / 第 1 页 C1-C2 区 U2 TPAP7343D-33FS4，VIN/EN/VOUT/GND/EP 与输入输出电容 |
| U1 | 33000uF | CN1 VBAT 的 SYS_BAT 对地储能器件 | 图 cc705599f70e / 第 1 页 / 第 1 页 C1-D2 区 U1 33000uF，pin2 SYS_BAT、pin1 GND |
| LED1 | 未标注 | 由 CN1 1PPS 经 R3 1KΩ 驱动的对地状态指示灯 | 图 cc705599f70e / 第 1 页 / 第 1 页 B3 区 CN1 1PPS pin4-R3 1K/1%-LED1-GND |
| J1,J2 | 5P_Header / 4P_Header | Atom 主机的 GPS_TX、GPS_RX、nRST、5V 与 GND 接口 | 图 cc705599f70e / 第 1 页 / 第 1 页 C3 区 J1/J2，J1 pins2-4 GPS_TX/GPS_RX/nRST，J2 pin3 5V、pin4 GND |
| LB1,LB3 | 100R@100MHz | 3V3 到 SYS_3V3 以及 3V3 到 AT2659 VCC 的电源滤波磁珠 | 图 cc705599f70e / 第 1 页 / 第 1 页 B1 区 LB3 与 C3/C4，D1-D2 区 LB1 与 C7/C8，均标 100R@100MHz |
| C1,LB2 | 300pF/50V / 6.8nH | U5 天线到 U3 RFIN 的串联射频匹配网络 | 图 cc705599f70e / 第 1 页 / 第 1 页 B1 区 U5-C1 300pF/50V-LB2 6.8nH-U3 RFIN |

## 系统结构

### Atomic GPS Base v2.0 系统架构

U5 天线经 C1/LB2 和 U3 AT2659 接入 CN1 ATGM336H-6N-74 RF_IN；CN1 通过 GPS_TX/GPS_RX 与 Atom 通信，并引出 nRST，1PPS 驱动 LED1；5V 经 U2 生成 3V3/SYS_3V3，SYS_BAT 由 U1 33000uF 对地储能。

- 参数与网络：`gnss_module=CN1 ATGM336H-6N-74`；`antenna=U5 BWGNSCNX15-15W4`；`lna=U3 AT2659`；`host_bus=UART GPS_TX/GPS_RX`；`reset=nRST`；`pulse_output=1PPS -> LED1`；`main_power=5V -> U2 -> 3V3 -> LB1 -> SYS_3V3`；`backup_power=CN1 VBAT -> SYS_BAT -> U1 33000uF`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页完整单页：U5/U3/CN1、U2/U1、J1/J2 与全部同名网络

## 核心器件

### CN1 ATGM336H-6N-74 连接

CN1 VCC pin8 接 SYS_3V3，VBAT pin6 接 SYS_BAT，nRESET pin9 接 nRST，1PPS pin4 接 R3，RXD0 pin3 接 R2，TXD0 pin2 接 R1，RF_IN pin11 接 U3 RFOUT；GND pins1/10/12 接地。

- 参数与网络：`main_supply=pin8 VCC SYS_3V3`；`backup_supply=pin6 VBAT SYS_BAT`；`reset=pin9 nRESET nRST`；`pulse=pin4 1PPS`；`uart_rx=pin3 RXD0`；`uart_tx=pin2 TXD0`；`rf_input=pin11 RF_IN`；`grounds=pins1,10,12`；`reserved_nc=pins13,15,18`；`secondary_uart_unrouted=pins16 RXD1,17 TXD1`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B2-B3 区 CN1 pins1-18 与网络、NC 标记

## 电源

### U2 5V 到 3V3 稳压

U2 TPAP7343D-33FS4 的 VIN pin4 与 EN pin3 接 5V，VOUT pin1 输出 3V3，GND pin2 与 EP pin5 接地；输入使用 C9 10uF/10V 和 C5 0.1uF/10V，输出 C6 10uF/10V，C2 标为 NC。

- 参数与网络：`input=5V`；`vin=pin4`；`enable=pin3 tied to 5V`；`output=pin1 3V3`；`ground=pin2 GND, pin5 EP GND`；`input_caps=C9 10uF/10V, C5 0.1uF/10V`；`output_caps=C6 10uF/10V, C2 NC`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 C1-C2 区 U2 pins1-5、C5/C9/C2/C6 与 5V/3V3/GND

### 3V3 到 SYS_3V3 滤波

3V3 经 LB1 100R@100MHz 形成 SYS_3V3，C7 10uF/10V 与 C8 0.1uF/50V 从 SYS_3V3 接 GND；SYS_3V3 供 CN1 VCC 并上拉 ON/OFF。

- 参数与网络：`input=3V3`；`ferrite=LB1 100R@100MHz`；`output=SYS_3V3`；`decoupling=C7 10uF/10V, C8 0.1uF/50V`；`consumers=CN1 VCC pin8, R4 to ON/OFF`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 D1-D2 区 LB1/C7/C8 与 B3 区 SYS_3V3 网络

### CN1 VBAT 后备储能

CN1 VBAT pin6 连接 SYS_BAT；SYS_BAT 接 U1 pin2，U1 标注 33000uF，另一端 pin1 接 GND。

- 参数与网络：`module_pin=CN1 pin6 VBAT`；`net=SYS_BAT`；`storage=U1 33000uF`；`positive=pin2 SYS_BAT`；`negative=pin1 GND`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B3 区 CN1 VBAT/SYS_BAT 与 C1-D2 区 U1 33000uF

## 接口

### J1/J2 Atom 接口

J1 pins1/5 未连接，pin2 为 GPS_TX，pin3 为 GPS_RX，pin4 为 nRST；J2 pins1/2 未连接，pin3 为 5V，pin4 为 GND。

- 参数与网络：`J1_pin1=NC`；`J1_pin2=GPS_TX`；`J1_pin3=GPS_RX`；`J1_pin4=nRST`；`J1_pin5=NC`；`J2_pin1=NC`；`J2_pin2=NC`；`J2_pin3=5V`；`J2_pin4=GND`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 C3 区 J1 5P_Header 与 J2 4P_Header 的 pins1-5、网络和 NC 线端

## 总线

### CN1 到 Atom 的 UART

CN1 TXD0 pin2 经 R1 22Ω/1% 形成 GPS_TX，RXD0 pin3 经 R2 22Ω/1% 形成 GPS_RX；两网络分别连接 J1 pins2/3。

- 参数与网络：`module_tx=CN1 TXD0 pin2 -> R1 22R/1% -> GPS_TX -> J1 pin2`；`module_rx=CN1 RXD0 pin3 -> R2 22R/1% -> GPS_RX -> J1 pin3`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B3 区 CN1 pins2/3-R1/R2-GPS_TX/GPS_RX 与 C3 区 J1

## GPIO 与控制信号

### CN1 1PPS 指示灯

CN1 1PPS pin4 经 R3 1KΩ/1% 和 LED1 接 GND，图中未把 1PPS 引出到 J1/J2。

- 参数与网络：`pulse_source=CN1 pin4 1PPS`；`series_resistor=R3 1K/1%`；`indicator=LED1`；`return=GND`；`header_output=false`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B3 区 CN1 pin4-R3-LED1-GND 与 J1/J2 信号范围

## 复位

### CN1 复位与 ON/OFF

CN1 nRESET pin9 直接形成 nRST 并连接 J1 pin4；ON/OFF pin5 经 R4 10KΩ/1% 上拉到 SYS_3V3。

- 参数与网络：`reset=CN1 pin9 nRESET -> nRST -> J1 pin4`；`on_off=CN1 pin5 -> R4 10K/1% -> SYS_3V3`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B3 区 CN1 pins9/5、nRST、R4/SYS_3V3 与 C3 区 J1 pin4

## 射频

### U5 天线到 AT2659 RFIN

U5 BWGNSCNX15-15W4 天线经串联 C1 300pF/50V 和 LB2 6.8nH 到 U3 RFIN pin3。

- 参数与网络：`antenna=U5 BWGNSCNX15-15W4`；`series_capacitor=C1 300pF/50V`；`series_inductor=LB2 6.8nH`；`lna_input=U3 RFIN pin3`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B1 区 U5-C1-LB2-U3 RFIN 连线

### U3 AT2659 射频与供电

U3 RFOUT pin6 直接连接 CN1 RF_IN pin11；VCC pin4 与 SHDN pin5 同接经 LB3 100R@100MHz 滤波的 3V3 节点，C4 10uF/10V 与 C3 0.1uF/50V 对地去耦，GND pins1/2 接地。

- 参数与网络：`input=RFIN pin3`；`output=RFOUT pin6 -> CN1 RF_IN pin11`；`supply=3V3 -> LB3 100R@100MHz -> VCC pin4 and SHDN pin5`；`decoupling=C4 10uF/10V, C3 0.1uF/50V`；`grounds=pins1,2`
- 证据：图 cc705599f70e / 第 1 页 / 第 1 页 B1-B2 区 U3/LB3/C3/C4 与 CN1 RF_IN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic GPS Base v2.0 系统架构 | `gnss_module=CN1 ATGM336H-6N-74`；`antenna=U5 BWGNSCNX15-15W4`；`lna=U3 AT2659`；`host_bus=UART GPS_TX/GPS_RX`；`reset=nRST`；`pulse_output=1PPS -> LED1`；`main_power=5V -> U2 -> 3V3 -> LB1 -> SYS_3V3`；`backup_power=CN1 VBAT -> SYS_BAT -> U1 33000uF` |
| 核心器件 | CN1 ATGM336H-6N-74 连接 | `main_supply=pin8 VCC SYS_3V3`；`backup_supply=pin6 VBAT SYS_BAT`；`reset=pin9 nRESET nRST`；`pulse=pin4 1PPS`；`uart_rx=pin3 RXD0`；`uart_tx=pin2 TXD0`；`rf_input=pin11 RF_IN`；`grounds=pins1,10,12`；`reserved_nc=pins13,15,18`；`secondary_uart_unrouted=pins16 RXD1,17 TXD1` |
| 射频 | U5 天线到 AT2659 RFIN | `antenna=U5 BWGNSCNX15-15W4`；`series_capacitor=C1 300pF/50V`；`series_inductor=LB2 6.8nH`；`lna_input=U3 RFIN pin3` |
| 射频 | U3 AT2659 射频与供电 | `input=RFIN pin3`；`output=RFOUT pin6 -> CN1 RF_IN pin11`；`supply=3V3 -> LB3 100R@100MHz -> VCC pin4 and SHDN pin5`；`decoupling=C4 10uF/10V, C3 0.1uF/50V`；`grounds=pins1,2` |
| 总线 | CN1 到 Atom 的 UART | `module_tx=CN1 TXD0 pin2 -> R1 22R/1% -> GPS_TX -> J1 pin2`；`module_rx=CN1 RXD0 pin3 -> R2 22R/1% -> GPS_RX -> J1 pin3` |
| 复位 | CN1 复位与 ON/OFF | `reset=CN1 pin9 nRESET -> nRST -> J1 pin4`；`on_off=CN1 pin5 -> R4 10K/1% -> SYS_3V3` |
| GPIO 与控制信号 | CN1 1PPS 指示灯 | `pulse_source=CN1 pin4 1PPS`；`series_resistor=R3 1K/1%`；`indicator=LED1`；`return=GND`；`header_output=false` |
| 电源 | U2 5V 到 3V3 稳压 | `input=5V`；`vin=pin4`；`enable=pin3 tied to 5V`；`output=pin1 3V3`；`ground=pin2 GND, pin5 EP GND`；`input_caps=C9 10uF/10V, C5 0.1uF/10V`；`output_caps=C6 10uF/10V, C2 NC` |
| 电源 | 3V3 到 SYS_3V3 滤波 | `input=3V3`；`ferrite=LB1 100R@100MHz`；`output=SYS_3V3`；`decoupling=C7 10uF/10V, C8 0.1uF/50V`；`consumers=CN1 VCC pin8, R4 to ON/OFF` |
| 电源 | CN1 VBAT 后备储能 | `module_pin=CN1 pin6 VBAT`；`net=SYS_BAT`；`storage=U1 33000uF`；`positive=pin2 SYS_BAT`；`negative=pin1 GND` |
| 接口 | J1/J2 Atom 接口 | `J1_pin1=NC`；`J1_pin2=GPS_TX`；`J1_pin3=GPS_RX`；`J1_pin4=nRST`；`J1_pin5=NC`；`J2_pin1=NC`；`J2_pin2=NC`；`J2_pin3=5V`；`J2_pin4=GND` |
| 射频 | 正文与原理图的 LNA 型号冲突 | `documented_model=MAX2659`；`schematic_model=AT2659`；`reference=U3`；`conflict=true` |
| 核心器件 | 正文中的 GNSS 接收能力 | `documented_soc=AT6668`；`documented_systems=GPS,QZSS,BD2,BD3,GALILEO,GLONASS`；`documented_frequencies=BDS B1/B1C; GPS/QZSS L1; GALILEO E1; GLONASS L1`；`documented_channels=50`；`documented_accuracy=<1.5m CEP50`；`documented_sensitivity=tracking -167dBm; reacquisition -160dBm; cold -148dBm; hot -156dBm`；`schematic_module=CN1 ATGM336H-6N-74` |
| 总线 | 正文中的 GNSS 输出协议与时间指标 | `documented_protocol=NMEA0183`；`documented_uart=115200bps 8N1`；`documented_update=1Hz default, 10Hz max`；`documented_cold_start=23s`；`documented_hot_start=1s`；`documented_reacquisition=1s`；`schematic_bus=GPS_TX/GPS_RX UART` |
| 电源 | 正文中的整机电流 | `documented_standby=5.01V@4.95mA`；`documented_active=5.02V@35.07mA`；`schematic_input=J2 pin3 5V`；`test_conditions=null` |

## 待确认事项

- `rf.documented-lna-model-conflict`：产品描述称内置 MAX2659，但原理图 U3 明确标注 AT2659，数据手册链接也命名为 AT2659；无法在没有 BOM 和变更记录的情况下把两者视为同一量产器件。（证据：图 cc705599f70e / 第 1 页 / 第 1 页 B1-B2 区 U3 器件名明确为 AT2659）
- `component.documented-gnss-capabilities`：正文称模组基于 AT6668，支持 GPS/QZSS/BDS/GALILEO/GLONASS 多系统多频点、50 通道、<1.5m 精度及多组灵敏度；原理图只确认 CN1 型号与 RF/UART/电源连接，不能单独证明这些内部能力和指标。（证据：图 cc705599f70e / 第 1 页 / 第 1 页 CN1 只标 ATGM336H-6N-74 与引脚，图中无 AT6668、卫星系统、频点、通道、精度或灵敏度文字）
- `bus.documented-gnss-output-timing`：正文给出 NMEA0183、115200bps@8N1、默认 1Hz/最大 10Hz，以及冷启动 23s、热启动 1s、重捕捉 1s；原理图只有 UART 电气连接和 1PPS LED，无法验证固件协议、波特率、更新率或启动时间。（证据：图 cc705599f70e / 第 1 页 / 第 1 页 CN1 TXD0/RXD0、R1/R2 与 GPS_TX/GPS_RX，图中无协议、波特率、更新率或启动时间）
- `power.documented-current-consumption`：正文给出待机 DC 5.01V@4.95mA、工作 DC 5.02V@35.07mA；原理图确认 5V 输入、LDO、LNA 和 GNSS 模组连接，但没有整机电流或测试条件标注。（证据：图 cc705599f70e / 第 1 页 / 第 1 页 J2 5V、U2 3V3、U3 与 CN1 电源连接，图中无 mA 指标或测试状态）
- `review.lna-model-conflict`：A134-V2 当前量产 BOM 使用 AT2659 还是 MAX2659，二者是否为经过批准的替代料？；原因：正文写 MAX2659，原理图写 AT2659；器件型号冲突会影响 RF 性能和 datasheet 追溯。
- `review.gnss-module-datasheet-capabilities`：当前 ATGM336H-6N-74/AT6668 datasheet 和固件版本是否确认正文所列系统、频点、50 通道、<1.5m 精度与灵敏度？；原因：这些是模组内部和测试指标，原理图不能单独证明，需绑定正式 datasheet 与固件版本。
- `review.gnss-output-and-timing`：量产固件是否固定为 NMEA0183、115200bps@8N1，并支持 1Hz/10Hz 与正文启动时间？；原因：协议、波特率、更新率和启动时间由模组配置、固件与测试环境决定，原理图仅给出 UART 物理连接。
- `review.current-consumption-tests`：待机 4.95mA 和工作 35.07mA 的 GNSS 配置、卫星状态、输入电压与测试方法是什么？；原因：整机电流需要测试记录；原理图不能推导具体 mA 数值和状态定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cc705599f70efaaea9a62a4eace6d89f19d08ffb1241d24ab5e4fddbbc6b851d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/SCH-A134-V2.png` |

---

源文档：`zh_CN/atom/Atomic_GPS_Base_v2.0.md`

源文档 SHA-256：`adb46300fe5b03ffba5db7f525d68a3ea60a399f2603e8b16a6614cdaf3718aa`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
