# Unit LoRaWAN-CN470 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaWAN-CN470 |
| SKU | U184-CN470 |
| 产品 ID | `unit-lorawan-cn470-6c30432ff630` |
| 源文档 | `zh_CN/unit/Unit LoRaWAN-CN470.md` |

## 概述

Unit LoRaWAN-CN470 以 M1 RAK3172 无线模组为核心，J1 HY-2.0_UART 通过 U2_RX/U2_TX 与模组通信，并引入受保险丝和浪涌器件保护的 +5V。U1 VRH3301NLX 将 +5V 转换为 +3.3V，为 RAK3172、复位上拉和 UART 偏置网络供电。模组的 RF pin12 经 R8/C8/C9 可选匹配网络连接 ANT/E1，板上另引出 SWD、RST、BOOT、I2C、UART1 与 SPI 测试点。原理图仅确认 RAK3172 外部模组及电气连接，未展开正文所述 STM32WLE5、256KB Flash、64KB RAM、协议栈和天线性能。

## 检索关键词

`Unit LoRaWAN-CN470`、`U184-CN470`、`RAK3172`、`STM32WLE5`、`CN470`、`470-510MHz`、`LoRaWAN 1.0.3`、`LoRa P2P`、`VRH3301NLX`、`HY-2.0_UART`、`U2_RX`、`U2_TX`、`UART_RX`、`UART_TX`、`115200`、`+5V`、`+3.3V`、`F1 6V@1A`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`SWDIO`、`SWCLK`、`RST`、`BOOT`、`U1_RX`、`U1_TX`、`SCL`、`SDA`、`MOSI`、`MISO`、`SCK`、`NSS`、`ANT`、`RF pin12`、`R1 470`、`R2 868`、`R3 915`、`R4 923`、`SMA antenna`、`AT command`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | RAK3172 | LoRa 无线通信模组，连接双 UART、SWD、I2C、SPI、RF、复位、BOOT、ADC/GPIO 和 3.3V 电源 | 图 6def63d71dca / 第 1 页 / 第 1 页中央 M1 RAK3172，pins1-32 的网络与功能标注 |
| U1 | VRH3301NLX | 将 +5V 转换为 +3.3V 的稳压器 | 图 6def63d71dca / 第 1 页 / 第 1 页左上 U1 VRH3301NLX，VIN pin4、VOUT pin1、VSS pins2/5、EN pin3 |
| J1 | HY-2.0_UART | 四针 Grove UART 与 5V 电源接口，依次引出 RX、TX、VCC、GND | 图 6def63d71dca / 第 1 页 / 第 1 页右中 J1 HY-2.0_UART，pin1 RX、pin2 TX、pin3 VCC、pin4 GND |
| E1,R8,C8,C9 | NC / NC / NC / NC | RAK3172 RF 到 ANT 的天线连接与可选 pi 型匹配位置 | 图 6def63d71dca / 第 1 页 / 第 1 页中央左侧 RF 区，M1 pin12 RF、R8 NC、ANT、E1 NC、C8/C9 NC 与 GND |
| F1 | 6V@1A | +5V 至 J1 VCC 的串联保险/限流器件 | 图 6def63d71dca / 第 1 页 / 第 1 页右中 +5V 与 J1 pin3 VCC 之间的 F1 6V@1A |
| D1 | RLSD52A031V | +3.3V 电源轨到 GND 的瞬态/ESD 保护器件 | 图 6def63d71dca / 第 1 页 / 第 1 页左上 +3.3V 旁 D1 RLSD52A031V 对 GND |
| D2,R6,R7 | 1N4148WS T4 / 10KΩ / 10KΩ | 两路 UART 信号经 R6/R7 汇接到 D2，再由 D2 接 +3.3V 的偏置/钳位网络 | 图 6def63d71dca / 第 1 页 / 第 1 页右中，D2 1N4148WS T4 接 +3.3V，R6/R7 10KΩ 分别接 TX/RX |
| D3,D4,D5 | LESD3Z5.0CMT1G / RLSD52A031V / RLSD52A031V | J1 VCC、TX、RX 对 GND 的接口瞬态保护 | 图 6def63d71dca / 第 1 页 / 第 1 页右下 J1 保护区，D3 位于 F1 后 VCC，D4/D5 位于 TX/RX，三者接 GND |
| R5,C4 | 10KΩ / 1uF | RAK3172 RST 的 3.3V 上拉与对地电容网络 | 图 6def63d71dca / 第 1 页 / 第 1 页左中 RST 网络，R5 10KΩ 到 +3.3V、C4 1uF 到 GND |
| JP1-JP14 | 未标注 | +3.3V、GND、SWD、复位、BOOT、I2C、UART1 与 SPI 测试点组 | 图 6def63d71dca / 第 1 页 / 第 1 页左侧和下方 JP1-JP14，标注 +3.3V/SWCLK/SWDIO/RST/GND/BOOT/SCL/SDA/U1_RX/U1_TX/MOSI/MISO/SCK/NSS |
| R1,R2,R3,R4 | 0Ω | 原理图右上 470/868/915/923 区域版本装配选项表 | 图 6def63d71dca / 第 1 页 / 第 1 页右上表格，R1 0Ω/470、R2 0Ω/868、R3 0Ω/915、R4 0Ω/923 |

## 系统结构

### Unit LoRaWAN-CN470 系统架构

单页电路由 M1 RAK3172、5V 至 3.3V 稳压器 U1、J1 UART Grove、RF 匹配/天线位置、接口保护及调试测试点构成；板上没有显示独立主控、协处理器、外部存储器、晶振、充电器或电池。

- 参数与网络：`radio_module=M1 RAK3172`；`host_interface=J1 HY-2.0_UART`；`power=+5V -> U1 VRH3301NLX -> +3.3V`；`rf=M1 pin12 RF -> R8/C8/C9 -> ANT/E1`；`debug=JP1-JP14`；`external_memory=null`；`crystal=null`；`battery=null`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页完整单页原理图，U1、M1、J1、RF、保护与 JP1-JP14 功能区

## 核心器件

### RAK3172 外部引脚映射

M1 左侧 pins1-16 依次标出 U2_RX、U2_TX、ADC5、U1_TX、U1_RX、PA1、SWDIO、SWCLK、SCL、SDA、GND、RF、MOSI、MISO、SCK、NSS；右侧 pins17-32 标出 GND、GND、PA8、PA9、BOOT、RST、GND、VDD、ADC4、ADC3、PB12、GND、PA0、PB5、ADC2、ADC1。

- 参数与网络：`module=M1 RAK3172`；`pins_1_8=1 U2_RX;2 U2_TX;3 ADC5;4 U1_TX;5 U1_RX;6 PA1;7 SWDIO;8 SWCLK`；`pins_9_16=9 SCL;10 SDA;11 GND;12 RF;13 MOSI;14 MISO;15 SCK;16 NSS`；`pins_17_24=17 GND;18 GND;19 PA8;20 PA9;21 BOOT;22 RST;23 GND;24 VDD`；`pins_25_32=25 ADC4;26 ADC3;27 PB12;28 GND;29 PA0;30 PB5;31 ADC2;32 ADC1`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页中央 M1 RAK3172 符号两侧 pins1-32

## 电源

### +5V 至 +3.3V 稳压

+5V 连接 U1 VRH3301NLX 的 VIN pin4 和 EN pin3，VOUT pin1 输出 +3.3V，VSS pins2/5 接 GND；输入侧配置 C1 22uF 和 C2 1uF，输出侧配置 C3 1uF。

- 参数与网络：`regulator=U1 VRH3301NLX`；`input=+5V -> VIN pin4`；`enable=+5V -> EN pin3`；`output=VOUT pin1 -> +3.3V`；`ground=VSS pins2,5`；`input_caps=C1 22uF,C2 1uF`；`output_cap=C3 1uF`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页左上 U1/C1/C2/C3 与 +5V/+3.3V/GND

### RAK3172 3.3V 电源域

+3.3V 连接 M1 VDD pin24，并由 C5 100nF、C6 22uF、C7 33pF 对地去耦；同名电源还连接 R5 复位上拉、D1 保护以及 D2/R6/R7 UART 偏置支路。

- 参数与网络：`rail=+3.3V`；`module_pin=M1 pin24 VDD`；`decoupling=C5 100nF,C6 22uF,C7 33pF`；`reset_pullup=R5 10K`；`rail_protection=D1 RLSD52A031V`；`uart_bias=D2,R6,R7`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页 M1 pin24/+3.3V/C5-C7，以及同名 +3.3V 的 R5、D1、D2 支路

## 接口

### J1 Grove UART 引脚

J1 HY-2.0_UART pin1 标 RX、pin2 标 TX、pin3 标 VCC、pin4 接 GND；pin3 由 +5V 经 F1 6V@1A 供电。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pin1=RX`；`pin2=TX`；`pin3=VCC <- F1 <- +5V`；`pin4=GND`；`logic_rail=+3.3V bias/protection network`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页右中 J1 pins1-4 与 F1/+5V/GND

## 总线

### J1 与 RAK3172 UART 映射

M1 U2_TX pin2 经 R9 22Ω 到 J1 pin1 RX；J1 pin2 TX 经 R10 22Ω 到 M1 U2_RX pin1。R7 10KΩ 接 RX 路，R6 10KΩ 接 TX 路，两路上端汇合并经 D2 1N4148WS T4 接 +3.3V。

- 参数与网络：`module_tx=M1 pin2 U2_TX -> R9 22R -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> R10 22R -> M1 pin1 U2_RX`；`rx_branch=R7 10K`；`tx_branch=R6 10K`；`diode=D2 1N4148WS T4 to +3.3V`；`direction=crossed UART TX/RX`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页 M1 pins1/2 U2_RX/U2_TX 与右中 R9/R10/R6/R7/D2/J1 RX/TX

## 复位

### RAK3172 复位网络

M1 RST pin22 连接 RST 网络；R5 10KΩ 将 RST 上拉到 +3.3V，C4 1uF 将 RST 接 GND，RST 同时引到 JP4。

- 参数与网络：`module_pin=M1 pin22 RST`；`pullup=R5 10K to +3.3V`；`capacitor=C4 1uF to GND`；`testpoint=JP4`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页左中 R5/C4/RST、中央 M1 pin22 与左侧 JP4

## 保护电路

### 电源与 UART 接口保护

+3.3V 由 D1 RLSD52A031V 对地保护；J1 VCC 由串联 F1 6V@1A 和 D3 LESD3Z5.0CMT1G 对地支路保护，C10 100nF 从 VCC 接 GND；J1 TX/RX 分别由 D4/D5 RLSD52A031V 对地保护，并串联 R10/R9 各 22Ω。

- 参数与网络：`three3=D1 RLSD52A031V`；`vcc_fuse=F1 6V@1A`；`vcc_tvs=D3 LESD3Z5.0CMT1G`；`vcc_filter=C10 100nF`；`tx_esd=D4 RLSD52A031V`；`rx_esd=D5 RLSD52A031V`；`series=R10/R9 22R`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页左上 D1 与右中/右下 F1、D3-D5、C10、R9/R10、J1

## 射频

### RAK3172 射频与天线路径

M1 RF pin12 经串联位置 R8 NC 到 ANT/E1 NC；C9 NC 从 RF 侧接 GND，C8 NC 从 ANT 侧接 GND，构成未给出装配值的可选 pi 型匹配网络。

- 参数与网络：`module_pin=M1 pin12 RF`；`series=R8 NC`；`module_side_shunt=C9 NC to GND`；`antenna_side_shunt=C8 NC to GND`；`antenna_net=ANT`；`antenna_reference=E1 NC`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页中央左侧 M1 RF/R8/C8/C9/ANT/E1/GND

### 470/868/915/923 区域选项表

原理图右上装配表明确列出 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915、R4 0Ω 对应 923；该表没有用装配标记显示本页实际焊接哪一项。

- 参数与网络：`R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`R4=0R -> 923`；`population_mark=null`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页右上独立表格 R1-R4 与 470/868/915/923

## 调试与烧录

### SWD、复位与 BOOT 测试点

JP1=+3.3V、JP2=SWCLK、JP3=SWDIO、JP4=RST、JP5=GND、JP6=BOOT；SWCLK、SWDIO、RST、BOOT 分别连接 M1 pins8、7、22、21。

- 参数与网络：`JP1=+3.3V`；`JP2=SWCLK -> M1 pin8`；`JP3=SWDIO -> M1 pin7`；`JP4=RST -> M1 pin22`；`JP5=GND`；`JP6=BOOT -> M1 pin21`；`debug_bus=SWD`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页左侧 JP1-JP6 与中央 M1 SWCLK/SWDIO/RST/BOOT 同名网络

### I2C、UART1 与 SPI 测试点

JP7=SCL、JP10=SDA、JP8=U1_RX、JP11=U1_TX、JP9=MOSI、JP12=MISO、JP13=SCK、JP14=NSS；对应网络连接 M1 pins9、10、5、4、13、14、15、16。

- 参数与网络：`i2c=JP7 SCL/M1 pin9; JP10 SDA/M1 pin10`；`uart1=JP8 U1_RX/M1 pin5; JP11 U1_TX/M1 pin4`；`spi=JP9 MOSI/pin13; JP12 MISO/pin14; JP13 SCK/pin15; JP14 NSS/pin16`
- 证据：图 6def63d71dca / 第 1 页 / 第 1 页左下 JP7-JP14 与中央 M1 SCL/SDA/U1_RX/U1_TX/MOSI/MISO/SCK/NSS

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit LoRaWAN-CN470 系统架构 | `radio_module=M1 RAK3172`；`host_interface=J1 HY-2.0_UART`；`power=+5V -> U1 VRH3301NLX -> +3.3V`；`rf=M1 pin12 RF -> R8/C8/C9 -> ANT/E1`；`debug=JP1-JP14`；`external_memory=null`；`crystal=null`；`battery=null` |
| 核心器件 | RAK3172 外部引脚映射 | `module=M1 RAK3172`；`pins_1_8=1 U2_RX;2 U2_TX;3 ADC5;4 U1_TX;5 U1_RX;6 PA1;7 SWDIO;8 SWCLK`；`pins_9_16=9 SCL;10 SDA;11 GND;12 RF;13 MOSI;14 MISO;15 SCK;16 NSS`；`pins_17_24=17 GND;18 GND;19 PA8;20 PA9;21 BOOT;22 RST;23 GND;24 VDD`；`pins_25_32=25 ADC4;26 ADC3;27 PB12;28 GND;29 PA0;30 PB5;31 ADC2;32 ADC1` |
| 电源 | +5V 至 +3.3V 稳压 | `regulator=U1 VRH3301NLX`；`input=+5V -> VIN pin4`；`enable=+5V -> EN pin3`；`output=VOUT pin1 -> +3.3V`；`ground=VSS pins2,5`；`input_caps=C1 22uF,C2 1uF`；`output_cap=C3 1uF` |
| 电源 | RAK3172 3.3V 电源域 | `rail=+3.3V`；`module_pin=M1 pin24 VDD`；`decoupling=C5 100nF,C6 22uF,C7 33pF`；`reset_pullup=R5 10K`；`rail_protection=D1 RLSD52A031V`；`uart_bias=D2,R6,R7` |
| 接口 | J1 Grove UART 引脚 | `connector=J1 HY-2.0_UART`；`pin1=RX`；`pin2=TX`；`pin3=VCC <- F1 <- +5V`；`pin4=GND`；`logic_rail=+3.3V bias/protection network` |
| 总线 | J1 与 RAK3172 UART 映射 | `module_tx=M1 pin2 U2_TX -> R9 22R -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> R10 22R -> M1 pin1 U2_RX`；`rx_branch=R7 10K`；`tx_branch=R6 10K`；`diode=D2 1N4148WS T4 to +3.3V`；`direction=crossed UART TX/RX` |
| 调试与烧录 | SWD、复位与 BOOT 测试点 | `JP1=+3.3V`；`JP2=SWCLK -> M1 pin8`；`JP3=SWDIO -> M1 pin7`；`JP4=RST -> M1 pin22`；`JP5=GND`；`JP6=BOOT -> M1 pin21`；`debug_bus=SWD` |
| 调试与烧录 | I2C、UART1 与 SPI 测试点 | `i2c=JP7 SCL/M1 pin9; JP10 SDA/M1 pin10`；`uart1=JP8 U1_RX/M1 pin5; JP11 U1_TX/M1 pin4`；`spi=JP9 MOSI/pin13; JP12 MISO/pin14; JP13 SCK/pin15; JP14 NSS/pin16` |
| 复位 | RAK3172 复位网络 | `module_pin=M1 pin22 RST`；`pullup=R5 10K to +3.3V`；`capacitor=C4 1uF to GND`；`testpoint=JP4` |
| 射频 | RAK3172 射频与天线路径 | `module_pin=M1 pin12 RF`；`series=R8 NC`；`module_side_shunt=C9 NC to GND`；`antenna_side_shunt=C8 NC to GND`；`antenna_net=ANT`；`antenna_reference=E1 NC` |
| 射频 | 470/868/915/923 区域选项表 | `R1=0R -> 470`；`R2=0R -> 868`；`R3=0R -> 915`；`R4=0R -> 923`；`population_mark=null` |
| 保护电路 | 电源与 UART 接口保护 | `three3=D1 RLSD52A031V`；`vcc_fuse=F1 6V@1A`；`vcc_tvs=D3 LESD3Z5.0CMT1G`；`vcc_filter=C10 100nF`；`tx_esd=D4 RLSD52A031V`；`rx_esd=D5 RLSD52A031V`；`series=R10/R9 22R` |
| 内存与 Flash | 正文中的 STM32WLE5 与存储容量 | `schematic_module=M1 RAK3172`；`documented_mcu=STM32WLE5`；`documented_flash=256KB`；`documented_ram=64KB`；`internal_schematic=null`；`clock=null` |
| 射频 | 正文中的 CN470 协议与射频性能 | `documented_band=CN470 470-510MHz`；`documented_protocol=LoRaWAN 1.0.3 Class A/B/C`；`documented_activation=OTAA,ABP`；`documented_mode=LoRaWAN,P2P`；`documented_sensitivity=-137dBm`；`documented_max_tx_power=22dBm`；`schematic_performance=null` |
| 射频 | 正文中的外接天线规格 | `schematic_reference=E1 NC`；`documented_type=胶棒天线`；`documented_impedance=50Ω`；`documented_gain=0.5dBi`；`documented_length=195mm`；`documented_connector=SMA 内针`；`schematic_connector_model=null` |

## 待确认事项

- `memory.documented-rak3172-internals`：产品正文称方案为 STM32WLE5、256KB Flash 和 64KB RAM；当前原理图只将 M1 标为 RAK3172，没有展开模组内部 MCU、Flash/RAM、时钟或射频收发器，因此这些内部规格不能由本页独立确认。（证据：图 6def63d71dca / 第 1 页 / 第 1 页中央 M1 型号仅标 RAK3172，符号内未展开 MCU、存储器或时钟）
- `rf.documented-protocol-performance`：产品正文称支持 CN470 470-510MHz、LoRaWAN 1.0.3 Class A/B/C、OTAA/ABP、P2P、-137dBm 灵敏度和最大 22dBm 发射功率；原理图仅显示 RAK3172、RF 网络和区域选项表，没有协议版本、频率范围、功率或灵敏度标注。（证据：图 6def63d71dca / 第 1 页 / 第 1 页 M1/RF 区与右上 470/868/915/923 表，未标协议或射频性能参数）
- `rf.documented-antenna`：产品正文称附带 50Ω、0.5dBi、总长 195mm、SMA 内针胶棒天线；原理图仅把 E1 标为 NC 并连接 ANT 匹配网络，没有给出连接器型号、阻抗、增益、长度或 SMA 极性。（证据：图 6def63d71dca / 第 1 页 / 第 1 页中央左侧 ANT/E1 NC/R8/C8/C9，未标天线机械与射频规格）
- `review.rak3172-internals`：请用当前 U184-CN470 所装 RAK3172 模组资料或 BOM 确认内部 STM32WLE5 完整型号、256KB Flash、64KB RAM 及内部时钟。；原因：板级原理图只给出 RAK3172 模组外部引脚，没有展开内部器件。
- `review.radio-protocol-performance`：请用量产固件版本、RAK3172 资料或射频测试报告确认 CN470 频段、LoRaWAN/P2P 功能、协议版本、灵敏度和最大发射功率。；原因：这些参数来自产品正文，原理图没有协议、固件或射频性能标注，也未显示 R1-R4 的实际装配项。
- `review.antenna-specification`：请用当前包装 BOM 或天线规格书确认胶棒天线的 50Ω、0.5dBi、195mm、SMA 内针及板端连接器型号。；原因：原理图中的 E1 仅标 NC，不能证明随附天线和连接器的射频或机械规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6def63d71dca037aa67dff4bd11dd51418f453e8fa9a1cc794867509b3166570` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/schematic.png` |

---

源文档：`zh_CN/unit/Unit LoRaWAN-CN470.md`

源文档 SHA-256：`512ea0ab7acb690d5cca6ed535212f3ad1b827e90bfc6a9de5b65eee3da09910`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
