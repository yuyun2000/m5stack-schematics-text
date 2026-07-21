# Unit UWB 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit UWB |
| SKU | U100 |
| 产品 ID | `unit-uwb-066371890460` |
| 源文档 | `zh_CN/unit/uwb.md` |

## 概述

Unit UWB 的控制页以 U1 STM32F103C8 为主控，PA4-PA7 提供 SPI_CSN/SPI_SCK/SPI_MISO/SPI_MOSI，PB0/PB12/PB13/PB14 分别连接 IRQ/RST/WAKEUP/EXTON，PA9/PA10 提供 UART_TX/UART_RX。控制板通过 JP1/JP2 引出上述信号，载板页以对应 JP3/JP4 接口承接，并由 IC1 SY8089 将 VCC_5V 降压为 VCC_3V3。Grove 接口提供 RXD、TXD、VCC_5V 与 GND，主控另有 16MHz 晶振、nRST、BOOT0/BOOT1 和 ISP1 SWD。两页均未显示 BU01/DW1000 器件、天线或 RF 网络，且 Grove RXD/TXD 与 UART_RX/UART_TX 使用不同网络名，不能仅凭本页确认跨板连接。

## 检索关键词

`Unit UWB`、`U100`、`STM32F103C8`、`BU01`、`DW1000`、`SY8089`、`VCC_5V`、`VCC_3V3`、`GROVE`、`RXD`、`TXD`、`UART_RX`、`UART_TX`、`SPI_CSN`、`SPI_SCK`、`SPI_MISO`、`SPI_MOSI`、`IRQ`、`RST`、`nRST`、`WAKEUP`、`EXTON`、`PA4`、`PA5`、`PA6`、`PA7`、`PA9`、`PA10`、`PB0`、`PB12`、`PB13`、`PB14`、`SWDIO`、`SWCLK`、`BOOT0`、`BOOT1`、`16M CL20pF`、`JP1`、`JP2`、`ISP1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F103C8 | 控制 MCU，连接 UWB 外设 SPI/UART/IRQ/RST/WAKEUP/EXTON 以及 SWD | 图 65dd38507eae / 第 1 页 / 资源 1 第 1 页左侧，U1 STM32F103C8 pin1-pin48 |
| X1 | 16M CL20pF | STM32F103C8 的 16MHz 外部主晶振 | 图 65dd38507eae / 第 1 页 / 资源 1 第 1 页右上，X1 16M CL20pF、C1/C2 20pF 与 XI/XO |
| JP1,JP2 | Header 6 | 控制板与外设/载板之间的两组六针接口，承载电源、UART、SPI 和控制信号 | 图 65dd38507eae / 第 1 页 / 资源 1 第 1 页右侧，JP1/JP2 pin1-pin6 |
| ISP1 | 未标注 | 四针 SWD 接口，提供 VCC_3V3、SWCLK、SWDIO 和 GND | 图 65dd38507eae / 第 1 页 / 资源 1 第 1 页右下，ISP1 VCC_3V3/SWCLK/SWDIO/GND |
| IC1 | SY8089 | 将载板 VCC_5V 降压为 VCC_3V3 的开关稳压器 | 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页左下，IC1 SY8089、L1、R2/R3 与 VCC_5V/VCC_3V3 |
| L1 | 4.7uH | SY8089 VCC_3V3 降压级电感 | 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页左下，IC1 LX 与 VCC_3V3 之间 L1 4.7uH |
| GROVE | 未标注 | 四针外部 UART/电源接口，提供 RXD、TXD、VCC_5V 和 GND | 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页右下，GROVE pin4 RXD、pin3 TXD、pin2 VCC_5V、pin1 GND |
| JP3,JP4 | Header 6 | 载板侧两组六针对接接口，网络名称与控制板 JP1/JP2 对应 | 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页上方，JP3/JP4 pin1-pin6 |
| R1,C3 | 10K / 104 | STM32 nRST 上拉与复位电容 | 图 65dd38507eae / 第 1 页 / 资源 1 第 1 页右上，VCC_3V3-R1 10K-nRST-C3 104-GND |

## 系统结构

### Unit UWB 控制与载板架构

资源 1 展开 U1 STM32F103C8、16MHz 时钟、复位、SWD 和 JP1/JP2 外设连接；资源 2 展开 JP3/JP4 对接接口、VCC_5V 至 VCC_3V3 电源以及 Grove。两页通过相同的 EXTON/WAKEUP/RST/VCC_3V3/GND/UART_TX 与 IRQ/SPI/UART_RX 网络定义形成控制板接口。

- 参数与网络：`controller=U1 STM32F103C8`；`control_headers=JP1/JP2`；`carrier_headers=JP3/JP4`；`power=VCC_5V -> IC1 SY8089 -> VCC_3V3`；`external_port=GROVE RXD/TXD`；`module_bus=SPI/UART/control`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页完整控制电路; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页完整载板电路

### 未展开的 UWB、存储与其他子系统

两页均未画 BU01、DW1000、天线、RF 匹配或射频供电，也未画独立存储器、音频、传感器、USB 收发器、CAN、RS-485 或 I2C 设备。

- 参数与网络：`uwb_transceiver=null`；`antenna=null`；`rf_matching=null`；`external_storage=null`；`audio=null`；`sensor=null`；`usb_transceiver=null`；`can=null`；`rs485=null`；`i2c_device=null`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页完整原理图; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页完整原理图

## 电源

### VCC_5V 至 VCC_3V3 降压

VCC_5V 同时接 IC1 SY8089 IN pin4 与 EN pin1，LX pin3 经 L1 4.7uH 输出 VCC_3V3；FB pin5 使用 R2 100K 与 R3 22K 分压。C9 104/C7 226 位于输入端，C8 226 位于输出端。

- 参数与网络：`input=VCC_5V`；`converter=IC1 SY8089`；`enable=EN pin1 tied VCC_5V`；`inductor=L1 4.7uH`；`output=VCC_3V3`；`feedback=R2 100K,R3 22K`；`caps=C9 104,C7 226,C8 226`
- 证据：图 94eefef30433 / 第 1 页 / 资源 2 第 1 页左下，IC1/L1/R2/R3/C7-C9

### STM32F103C8 3.3V 供电

U1 VDD_1/VDD_2/VDD_3 pins24/36/48 与 VDDA pin9 接 VCC_3V3，VSS_1/VSS_2/VSS_3 pins23/35/47 与 VSSA pin8 接 GND；C4/C5/C6 各 104 为 VCC_3V3 去耦。

- 参数与网络：`device=U1 STM32F103C8`；`digital_supply=pins24/36/48 VCC_3V3`；`analog_supply=pin9 VCC_3V3`；`grounds=pins23/35/47/8 GND`；`decoupling=C4/C5/C6 104`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 VDD/VDDA/VSS/VSSA 与 C4-C6

## 接口

### Grove UART/电源接口

GROVE pin4=RXD/IO2、pin3=TXD/IO1、pin2=VCC_5V/5V、pin1=GND；RXD/TXD 为载板上的串口命名网络，VCC_5V 为板上电源输入。

- 参数与网络：`connector=GROVE`；`pin4=RXD IO2`；`pin3=TXD IO1`；`pin2=VCC_5V`；`pin1=GND`；`power_direction=input`
- 证据：图 94eefef30433 / 第 1 页 / 资源 2 第 1 页右下 GROVE pin1-pin4

### JP1/JP2 与 JP3/JP4 对接针脚

JP1 与 JP3 均为 pin1 UART_TX、pin2 GND、pin3 VCC_3V3、pin4 RST、pin5 WAKEUP、pin6 EXTON；JP2 与 JP4 均为 pin1 IRQ、pin2 SPI_SCK、pin3 SPI_MISO、pin4 SPI_MOSI、pin5 SPI_CSN、pin6 UART_RX。

- 参数与网络：`jp1_jp3=1 UART_TX,2 GND,3 VCC_3V3,4 RST,5 WAKEUP,6 EXTON`；`jp2_jp4=1 IRQ,2 SPI_SCK,3 SPI_MISO,4 SPI_MOSI,5 SPI_CSN,6 UART_RX`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页右侧 JP1/JP2; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页上方 JP3/JP4

## 总线

### STM32 至外设 SPI 总线

U1 PA4 pin14 接 SPI_CSN，PA5 pin15 接 SPI_SCK，PA6 pin16 接 SPI_MISO，PA7 pin17 接 SPI_MOSI；四线经 JP2 pins5/2/3/4 和对应 JP4 pins5/2/3/4 引出。

- 参数与网络：`controller=U1 STM32F103C8`；`chip_select=PA4 pin14 SPI_CSN -> JP2/JP4 pin5`；`clock=PA5 pin15 SPI_SCK -> pin2`；`miso=PA6 pin16 SPI_MISO -> pin3`；`mosi=PA7 pin17 SPI_MOSI -> pin4`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 PA4-PA7 与 JP2; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 JP4 SPI pins

### STM32 外设 UART

U1 PA9/USART1_TX pin30 连接 UART_TX 并引出至 JP1/JP3 pin1；U1 PA10/USART1_RX pin31 连接 UART_RX 并引出至 JP2/JP4 pin6。

- 参数与网络：`controller=U1 STM32F103C8 USART1`；`tx=PA9 pin30 UART_TX -> JP1/JP3 pin1`；`rx=PA10 pin31 UART_RX -> JP2/JP4 pin6`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 PA9/PA10 与 JP1/JP2; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 JP3 UART_TX 与 JP4 UART_RX

## GPIO 与控制信号

### UWB 外设控制与中断映射

U1 PB0 pin18 接 IRQ 并引出 JP2/JP4 pin1；PB12 pin25 接 RST 并引出 JP1/JP3 pin4；PB13 pin26 接 WAKEUP 并引出 pin5；PB14 pin27 接 EXTON 并引出 pin6。

- 参数与网络：`irq=PB0 pin18 -> JP2/JP4 pin1`；`reset=PB12 pin25 -> JP1/JP3 pin4`；`wakeup=PB13 pin26 -> JP1/JP3 pin5`；`exton=PB14 pin27 -> JP1/JP3 pin6`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 PB0/PB12/PB13/PB14 与 JP1/JP2; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 JP3/JP4 控制网络

### STM32 BOOT0/BOOT1 配置

U1 BOOT0 pin44 接 GND，PB2/BOOT1 pin20 也接 GND。

- 参数与网络：`boot0=U1 pin44 GND`；`boot1=U1 PB2 pin20 GND`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 BOOT0 pin44 与 PB2/BOOT1 pin20

## 时钟

### STM32 16MHz 外部晶振

U1 OSC_IN/PD0 pin5 的 XI 与 OSC_OUT/PD1 pin6 的 XO 连接 X1 16M CL20pF，XI/XO 分别经 C2/C1 20pF 接 GND。PC14/PC15 低速晶振引脚未接外部晶振。

- 参数与网络：`controller=U1 STM32F103C8`；`crystal=X1 16M CL20pF`；`osc_in=pin5 XI`；`osc_out=pin6 XO`；`load_caps=C2/C1 20pF`；`lse=null`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 XI/XO 与 X1/C1/C2

## 复位

### STM32 nRST 网络

U1 NRST pin7 接 nRST，R1 10K 将 nRST 上拉至 VCC_3V3，C3 104 将 nRST 接 GND；该 nRST 与外设接口网络 RST 是不同网络。

- 参数与网络：`mcu_pin=U1 NRST pin7`；`network=nRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C3 104 to GND`；`external_reset_network=RST on PB12`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 NRST 与右上 R1/C3/nRST

## 保护电路

### 电源去耦与接口保护

VCC_5V 输入配置 C9 104/C7 226，VCC_3V3 输出配置 C8 226，MCU 侧配置 C4-C6 104；两页未画 Grove 输入保险丝、反接保护、浪涌/ESD 抑制或 UART/SPI 串联保护。

- 参数与网络：`input_caps=C9 104,C7 226`；`output_cap=C8 226`；`mcu_caps=C4/C5/C6 104`；`fuse=null`；`reverse_protection=null`；`esd=null`；`signal_protection=null`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 MCU 去耦与接口; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 VCC_5V/VCC_3V3 与 Grove

## 调试与烧录

### ISP1 SWD 调试接口

U1 PA13/JTMS/SWDIO pin34 接 SWDIO，PA14/JTCK/SWCLK pin37 接 SWCLK；ISP1 引出 VCC_3V3、SWCLK、SWDIO、GND。

- 参数与网络：`swdio=U1 PA13 pin34 -> ISP1 SWDIO`；`swclk=U1 PA14 pin37 -> ISP1 SWCLK`；`vref=VCC_3V3`；`ground=GND`
- 证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 PA13/PA14 与 ISP1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit UWB 控制与载板架构 | `controller=U1 STM32F103C8`；`control_headers=JP1/JP2`；`carrier_headers=JP3/JP4`；`power=VCC_5V -> IC1 SY8089 -> VCC_3V3`；`external_port=GROVE RXD/TXD`；`module_bus=SPI/UART/control` |
| 系统结构 | 未展开的 UWB、存储与其他子系统 | `uwb_transceiver=null`；`antenna=null`；`rf_matching=null`；`external_storage=null`；`audio=null`；`sensor=null`；`usb_transceiver=null`；`can=null`；`rs485=null`；`i2c_device=null` |
| 电源 | VCC_5V 至 VCC_3V3 降压 | `input=VCC_5V`；`converter=IC1 SY8089`；`enable=EN pin1 tied VCC_5V`；`inductor=L1 4.7uH`；`output=VCC_3V3`；`feedback=R2 100K,R3 22K`；`caps=C9 104,C7 226,C8 226` |
| 电源 | STM32F103C8 3.3V 供电 | `device=U1 STM32F103C8`；`digital_supply=pins24/36/48 VCC_3V3`；`analog_supply=pin9 VCC_3V3`；`grounds=pins23/35/47/8 GND`；`decoupling=C4/C5/C6 104` |
| 接口 | Grove UART/电源接口 | `connector=GROVE`；`pin4=RXD IO2`；`pin3=TXD IO1`；`pin2=VCC_5V`；`pin1=GND`；`power_direction=input` |
| 接口 | JP1/JP2 与 JP3/JP4 对接针脚 | `jp1_jp3=1 UART_TX,2 GND,3 VCC_3V3,4 RST,5 WAKEUP,6 EXTON`；`jp2_jp4=1 IRQ,2 SPI_SCK,3 SPI_MISO,4 SPI_MOSI,5 SPI_CSN,6 UART_RX` |
| 总线 | STM32 至外设 SPI 总线 | `controller=U1 STM32F103C8`；`chip_select=PA4 pin14 SPI_CSN -> JP2/JP4 pin5`；`clock=PA5 pin15 SPI_SCK -> pin2`；`miso=PA6 pin16 SPI_MISO -> pin3`；`mosi=PA7 pin17 SPI_MOSI -> pin4` |
| 总线 | STM32 外设 UART | `controller=U1 STM32F103C8 USART1`；`tx=PA9 pin30 UART_TX -> JP1/JP3 pin1`；`rx=PA10 pin31 UART_RX -> JP2/JP4 pin6` |
| GPIO 与控制信号 | UWB 外设控制与中断映射 | `irq=PB0 pin18 -> JP2/JP4 pin1`；`reset=PB12 pin25 -> JP1/JP3 pin4`；`wakeup=PB13 pin26 -> JP1/JP3 pin5`；`exton=PB14 pin27 -> JP1/JP3 pin6` |
| 时钟 | STM32 16MHz 外部晶振 | `controller=U1 STM32F103C8`；`crystal=X1 16M CL20pF`；`osc_in=pin5 XI`；`osc_out=pin6 XO`；`load_caps=C2/C1 20pF`；`lse=null` |
| 复位 | STM32 nRST 网络 | `mcu_pin=U1 NRST pin7`；`network=nRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C3 104 to GND`；`external_reset_network=RST on PB12` |
| GPIO 与控制信号 | STM32 BOOT0/BOOT1 配置 | `boot0=U1 pin44 GND`；`boot1=U1 PB2 pin20 GND` |
| 调试与烧录 | ISP1 SWD 调试接口 | `swdio=U1 PA13 pin34 -> ISP1 SWDIO`；`swclk=U1 PA14 pin37 -> ISP1 SWCLK`；`vref=VCC_3V3`；`ground=GND` |
| 保护电路 | 电源去耦与接口保护 | `input_caps=C9 104,C7 226`；`output_cap=C8 226`；`mcu_caps=C4/C5/C6 104`；`fuse=null`；`reverse_protection=null`；`esd=null`；`signal_protection=null` |
| 接口 | Grove RXD/TXD 与 MCU UART 的连接 | `grove=RXD/TXD`；`module_headers=UART_TX/UART_RX`；`explicit_connection=null`；`expected_crossing=null` |
| 射频 | BU01/DW1000 UWB 模组 | `documented_module=Ai-Thinker BU01`；`documented_transceiver=DW1000`；`schematic_reference=null`；`antenna=null`；`rf_matching=null` |
| 射频 | UWB 测距与射频性能 | `documented_accuracy=10cm`；`documented_band=3.5~6.5GHz,6 bands`；`documented_rates=110kbit/s,850kbit/s,6.8Mbit/s`；`documented_power=-14dBm/-10dBm`；`documented_standard=IEEE 802.15.4-2011`；`documented_modes=TWR,TDOA`；`schematic_rf_parameters=null` |
| 总线 | AT UART 固件协议 | `documented_baud=115200`；`documented_protocol=AT commands`；`mcu_uart=USART1 PA9/PA10`；`baud_in_schematic=null`；`frame_format=null`；`firmware_version=null` |

## 待确认事项

- `interface.grove-uart-link`：资源 2 Grove 信号命名为 RXD/TXD，而 JP3/JP4 与资源 1 MCU 信号命名为 UART_TX/UART_RX；提供的两页没有同名网络、导线、跳线或器件明确连接这两组网络。（证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 U1 UART_TX/UART_RX 与 JP1/JP2; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 Grove RXD/TXD 与 JP3/JP4 UART_TX/UART_RX，页内无连接）
- `rf.documented-module`：产品正文称采用 Ai-Thinker BU01、基于 DW1000；两页原理图均未画 BU01/DW1000 位号、模组边界、天线、RF 匹配或具体 SPI/控制引脚对应的收发器器件。（证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页仅显示通往 JP1/JP2 的接口; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页仅显示 JP3/JP4、电源和 Grove）
- `rf.documented-performance`：产品正文称定位精度 10cm、3.5~6.5GHz 六频段、110/850kbit/s/6.8Mbit/s、-14/-10dBm、IEEE 802.15.4-2011、双向测距与 TDOA；两页原理图没有 RF 器件或性能参数表，无法由电路页确认这些指标。（证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页无 RF 器件或参数; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页无 RF 器件或参数）
- `bus.documented-at-uart`：产品正文称串口默认 115200 并支持 AT 指令；原理图只确认 USART1 UART_TX/UART_RX 与 Grove RXD/TXD 网络名称，没有波特率、8N1、AT 帧格式、固件版本或命令能力。（证据：图 65dd38507eae / 第 1 页 / 资源 1 第 1 页 USART1 UART_TX/UART_RX; 图 94eefef30433 / 第 1 页 / 资源 2 第 1 页 Grove RXD/TXD）
- `review.grove-uart-link`：请通过 PCB 网表、跨页层次网络或实物导通确认 Grove RXD/TXD 与 UART_TX/UART_RX 的实际交叉连接。；原因：两页使用不同网络名且未显示显式连接。
- `review.uwb-module`：请用完整 BU01 原理图、BOM 或模组标签确认 UWB 器件为 Ai-Thinker BU01/DW1000，并确认 JP1-JP4 对应的模组引脚。；原因：当前两页没有 BU01/DW1000 器件符号。
- `review.uwb-performance`：请依据当前模组 datasheet、固件和整机射频测试确认频段、速率、功率、标准、测距模式与 10cm 精度。；原因：原理图没有射频实现或性能依据。
- `review.at-uart`：请通过当前固件与 AT 文档确认 UART 默认 115200、帧格式、命令集和固件版本。；原因：串口参数与协议属于固件行为，原理图未标。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `65dd38507eaeddf75f81d54386d63849c0b893207ac0576970f7387c2bea19c4` | `https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_sch_01.webp` |
| 2 | 1 | `94eefef3043322b9e549903ddc2036e15dc03e484c836a8c98ece8ee1c92d6e0` | `https://static-cdn.m5stack.com/resource/docs/products/unit/uwb/uwb_sch_02.webp` |

---

源文档：`zh_CN/unit/uwb.md`

源文档 SHA-256：`e96799b4e4516a454a102ee9dd9ef91eed2010b02373031641986296c45fdb25`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
