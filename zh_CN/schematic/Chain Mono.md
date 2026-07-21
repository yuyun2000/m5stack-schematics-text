# Chain Mono 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Mono |
| SKU | U217 |
| 产品 ID | `chain-mono-a83ce201f248` |
| 源文档 | `zh_CN/chain/Chain_Mono.md` |

## 概述

Chain Mono V0.1 以 U2 STM32G031G8U6 为核心，VCC_5V 经 U1 TPAP7343D 生成 VCC_3V3，J1/J3 两组 GROVE_IO 分别连接 MCU 的 USART1 与 USART2 以实现链式通信。第二页显示 LED1~LED64 构成单色 8×8 点阵，由 PA0、PA1、PA4、PA5、PA6、PA7、PA8、PA11、PA12 九个 GPIO 和 R1~R9 47Ω/1% 电阻直接复用驱动。板上还提供 JP1 的 RST/SWDIO/SWCLK 调试接口、复位 RC 网络及两组 PESDNC2FD5VB 接口防护。

## 检索关键词

`Chain Mono`、`U217`、`STM32G031G8U6`、`TPAP7343D`、`8x8 LED matrix`、`LED1-LED64`、`PESDNC2FD5VB`、`USART1`、`USART2`、`U1_TX`、`U1_RX`、`U2_TX`、`U2_RX`、`PB6`、`PB7`、`PA2`、`PA3`、`PA0`、`PA1`、`PA4`、`PA5`、`PA6`、`PA7`、`PA8`、`PA11`、`PA12`、`SWDIO`、`SWCLK`、`BOOT0`、`RST`、`VCC_5V`、`VCC_3V3`、`GROVE_IO`、`47R/1%`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32G031G8U6 | 主控 MCU，处理双 UART 链式通信、64 点 LED 矩阵扫描和 SWD 调试 | 图 72fe63674ce8 / 第 1 页 / 网格 A3-B4，U2 STM32G031G8U6，PA/PB/SWD/RST/电源引脚 |
| U1 | TPAP7343D | VCC_5V 至 VCC_3V3 的线性稳压器 | 图 72fe63674ce8 / 第 1 页 / 网格 A1-B2，U1 TPAP7343D，VIN/EN/OUT/GND/EP |
| J1 | GROVE_IO | 第一组 Chain 四针接口，IO2/IO1 分别连接 U1_TX/U1_RX，另有 VCC_5V/GND | 图 72fe63674ce8 / 第 1 页 / 网格 C2-D3，J1 GROVE_IO，U1_TX/U1_RX/VCC/GND |
| J3 | GROVE_IO | 第二组 Chain 四针接口，IO2/IO1 分别连接 U2_RX/U2_TX，另有 VCC_5V/GND | 图 72fe63674ce8 / 第 1 页 / 网格 C4-D4，J3 GROVE_IO，U2_RX/U2_TX/VCC/GND |
| JP1 | 5-pin debug header | 3.3V、RST、SWDIO、SWCLK、GND 调试/烧录接口 | 图 72fe63674ce8 / 第 1 页 / 网格 C1-C2，JP1 pins1-5，VCC_3V3/RST/SWDIO/SWCLK/GND |
| D68,D69 | PESDNC2FD5VB | 两组 GROVE_IO 周边的 ESD/瞬态保护器件 | 图 72fe63674ce8 / 第 1 页 / 网格 C2-D4，J1 旁 D69 与 J3 旁 D68 PESDNC2FD5VB |
| LED1-LED64 | 未标注 | 64 颗单色 LED，组成 8×8 显示矩阵 | 图 70dbaec8a75a / 第 1 页 / 整页 LEDMatrix，LED1~LED64 |
| R1-R9 | 47Ω/1% | 九路 MCU LED 扫描网络的串联限流电阻 | 图 70dbaec8a75a / 第 1 页 / 网格 B2-D3，PA0/PA1/PA4/PA5/PA6/PA7/PA8/PA11/PA12 各串 R1~R9 47R/1% |

## 系统结构

### Chain Mono 系统架构

系统由 STM32G031G8U6、5V 转 3.3V LDO、双 Chain UART 接口、SWD 调试口和 64 颗直接复用驱动的 LED 点阵组成。

- 参数与网络：`mcu=U2 STM32G031G8U6`；`regulator=U1 TPAP7343D`；`chain_ports=J1,J3 GROVE_IO`；`debug=JP1`；`display=LED1-LED64`；`protection=D68,D69`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控/电源/接口整页; 图 70dbaec8a75a / 第 1 页 / LEDMatrix 整页

### 链式通信方向

图面蓝色箭头从 J1 指向 J3；J1 使用 USART1，J3 使用 USART2，硬件没有将两端 UART 信号直接短接。

- 参数与网络：`diagram_direction=J1 -> J3`；`upstream_uart=USART1 PB6/PB7`；`downstream_uart=USART2 PA2/PA3`；`direct_pass_through=false`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 C2-C4，J1/J3 上方蓝色右向箭头与不同 UART 网络

## 核心器件

### STM32G031G8U6 主控

U2 明确标为 STM32G031G8U6，VDD/VDDA pin3 接 VCC_3V3，VSS/VSSA pin4 接 GND，使用 PA/PB GPIO、两组 UART、SWD 与 PF2 RST。

- 参数与网络：`reference=U2`；`part_number=STM32G031G8U6`；`supply=pin3 VDD/VDDA VCC_3V3`；`ground=pin4 VSS/VSSA`；`uart1=PB6/PB7`；`uart2=PA2/PA3`；`debug=PA13 SWDIO,PA14 SWCLK`；`reset=PF2 pin5`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 A3-B4，U2 全部引脚

### 64 点 LED 矩阵

第二页逐个标出 LED1 到 LED64，器件连接在九条横向 GPIO 驱动线与八条纵向 GPIO 网络之间，组成 64 点矩阵。

- 参数与网络：`references=LED1-LED64`；`count=64`；`horizontal_lines=9`；`vertical_lines=8`；`control_gpio=PA0,PA1,PA4,PA5,PA6,PA7,PA8,PA11,PA12`；`part_number=null`
- 证据：图 70dbaec8a75a / 第 1 页 / 整页 LEDMatrix，LED1~LED64 与 PA 网络

## 电源

### 5V 到 3.3V 稳压

U1 TPAP7343D 的 VIN pin4 与 EN pin3 接 VCC_5V，OUT pin1 生成 VCC_3V3，GND pin2 与 EP pin5 接地；输入/输出各有 1uF/25V 电容。

- 参数与网络：`regulator=U1 TPAP7343D`；`input=VCC_5V`；`enable=VCC_5V`；`output=VCC_3V3`；`ground=pins2,5`；`input_cap=C1 1uF/25V`；`output_cap=C2 1uF/25V`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 A1-B2，U1/C1/C2/VCC_5V/VCC_3V3

### 5V 与 3.3V 电源轨

VCC_5V 在 J1/J3 VCC 间直通并供 U1；VCC_3V3 供给 U2、JP1 与复位/启动网络。LED 页未显示单独电源轨。

- 参数与网络：`5v=J1/J3 VCC and U1 input`；`3v3=U1 output -> U2/JP1/R11`；`led_supply_rail=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页 VCC_5V/VCC_3V3 网络; 图 70dbaec8a75a / 第 1 页 / LED 页仅 GPIO/电阻/LED，无电源网标签

## 接口

### J1 Chain 接口

J1 GROVE_IO pin1 IO2=U1_TX、pin2 IO1=U1_RX、pin3 VCC=VCC_5V、pin4 GND。

- 参数与网络：`reference=J1`；`pin1=IO2/U1_TX`；`pin2=IO1/U1_RX`；`pin3=VCC/VCC_5V`；`pin4=GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 C2-D3，J1 GROVE_IO

### J3 Chain 接口

J3 GROVE_IO pin1 IO2=U2_RX、pin2 IO1=U2_TX、pin3 VCC=VCC_5V、pin4 GND。

- 参数与网络：`reference=J3`；`pin1=IO2/U2_RX`；`pin2=IO1/U2_TX`；`pin3=VCC/VCC_5V`；`pin4=GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 C4-D4，J3 GROVE_IO

## 总线

### USART1 与 J1

U2 PB6 pin26 输出 U1_TX 到 J1 IO2，PB7 pin27 接收 U1_RX 自 J1 IO1。

- 参数与网络：`controller=U2 STM32G031G8U6`；`tx=PB6 pin26/U1_TX -> J1 IO2`；`rx=J1 IO1/U1_RX -> PB7 pin27`；`connector=J1 GROVE_IO`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 A3-D3，U2 PB6/PB7 与 J1 U1_TX/U1_RX

### USART2 与 J3

U2 PA2 pin8 输出 U2_TX 到 J3 IO1，PA3 pin9 接收 U2_RX 自 J3 IO2。

- 参数与网络：`controller=U2 STM32G031G8U6`；`tx=PA2 pin8/U2_TX -> J3 IO1`；`rx=J3 IO2/U2_RX -> PA3 pin9`；`connector=J3 GROVE_IO`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 A3-D4，U2 PA2/PA3 与 J3 U2_TX/U2_RX

## 总线地址

### 设备地址

板上未显示 I2C、SPI 从设备或硬件地址绑带；Chain 通信使用 UART 网络。

- 参数与网络：`i2c_address=null`；`spi_chip_select=null`；`uart=USART1,USART2`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页无 I2C/SPI 外设或地址标注

## GPIO 与控制信号

### SWCLK/BOOT0 绑带

U2 PA14-BOOT0 pin21 连接 SWCLK，并通过 R10 10K/1% 下拉到 GND。

- 参数与网络：`pin=U2 pin21 PA14-BOOT0`；`debug_net=SWCLK`；`strap=R10 10K/1% to GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 B3，U2 PA14-BOOT0/SWCLK 与 R10

### LED 矩阵 GPIO 映射

LED 页使用 PA0、PA1、PA4、PA5、PA6、PA7、PA8、PA11、PA12 九条 GPIO 网络；它们分别经 R1~R9 47Ω/1% 进入 LED 复用网络。

- 参数与网络：`gpio=PA0,PA1,PA4,PA5,PA6,PA7,PA8,PA11,PA12`；`resistors=R1-R9`；`value=47Ω/1%`；`mcu_pins=PA0.6,PA1.7,PA4.10,PA5.11,PA6.12,PA7.13,PA8.16,PA11.18,PA12.19`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页 U2 PA0/1/4/5/6/7/8/11/12 sheet nets; 图 70dbaec8a75a / 第 1 页 / LED 页 PA nets 与 R1-R9

## 时钟

### MCU 时钟

U2 PC14-OSC32 IN pin1 与 PC15-OSC32 OUT pin2 均未连接，原理图没有外部晶振或振荡器。

- 参数与网络：`lse_in=U2 pin1 NC`；`lse_out=U2 pin2 NC`；`external_crystal=null`；`oscillator=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 A4-B4，U2 PC14/PC15 红色 NC 标记

## 复位

### STM32 复位网络

U2 PF2 RST pin5 连接 RST 网络与 JP1 pin2；R11 1K 将 RST 上拉到 VCC_3V3，C8 1uF/50V 从 RST 接 GND。

- 参数与网络：`target=U2 pin5 PF2 RST`；`debug_pin=JP1 pin2`；`pullup=R11 1K to VCC_3V3`；`capacitor=C8 1uF/50V to GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 B4/C1-C2，U2 RST 与 R11/C8/JP1

## 保护电路

### Chain 接口 ESD 保护

J1 旁配置 D69 PESDNC2FD5VB，J3 旁配置 D68 PESDNC2FD5VB，均连接接口局部网络与 GND。

- 参数与网络：`j1_protection=D69 PESDNC2FD5VB`；`j3_protection=D68 PESDNC2FD5VB`；`ground=GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 C2-D4，D69/D68 与 J1/J3

## 关键网络

### 通信与显示关键路径

上游链路 J1 -> USART1，MCU 内部处理后由 USART2 -> J3；显示由 U2 九个 PA GPIO -> R1~R9 -> LED1~LED64。

- 参数与网络：`upstream=J1 U1_TX/U1_RX <-> U2 PB6/PB7`；`downstream=U2 PA2/PA3 <-> J3 U2_TX/U2_RX`；`display=U2 PA GPIO -> R1-R9 -> LED1-LED64`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页双 UART 与 LED sheet nets; 图 70dbaec8a75a / 第 1 页 / LED 页完整矩阵

## 存储

### 外部存储

原理图未显示外部 Flash、EEPROM、eMMC 或存储卡；STM32 内部 Flash 容量未在图中标注。

- 参数与网络：`external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`internal_flash_capacity=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页仅 U2 MCU，无外部存储

## 内存与 Flash

### 外部内存

原理图未显示外部 RAM、PSRAM 或 DDR；STM32 内部 RAM 容量未在图中标注。

- 参数与网络：`external_ram=null`；`psram=null`；`ddr=null`；`internal_ram_capacity=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页无外部内存器件

## 音频

### 音频电路

两页原理图未显示音频编解码器、麦克风、扬声器或 I2S 网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页无音频; 图 70dbaec8a75a / 第 1 页 / LED 页无音频

## 传感器

### 传感器

两页原理图未显示传感器器件。

- 参数与网络：`sensor_ic=null`；`sensor_bus=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页无 Sensor; 图 70dbaec8a75a / 第 1 页 / LED 页仅 LED

## 射频

### 射频电路

两页原理图未显示射频芯片、天线或射频匹配网络。

- 参数与网络：`rf_ic=null`；`antenna=null`；`matching=null`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页无 RF; 图 70dbaec8a75a / 第 1 页 / LED 页无 RF

## 调试与烧录

### JP1 SWD 调试接口

JP1 pin1 为 VCC_3V3、pin2 RST、pin3 SWDIO、pin4 SWCLK、pin5 GND；SWDIO/SWCLK 分别连接 U2 PA13 pin20 与 PA14-BOOT0 pin21。

- 参数与网络：`reference=JP1`；`pin1=VCC_3V3`；`pin2=RST`；`pin3=SWDIO/U2 PA13`；`pin4=SWCLK/U2 PA14-BOOT0`；`pin5=GND`
- 证据：图 72fe63674ce8 / 第 1 页 / 网格 B3-C2，JP1 到 U2 SWDIO/SWCLK

## 模拟电路

### LED 限流网络

九条横向驱动网络分别串联 R1~R9，所有电阻均标 47R/1%；每颗 LED 未配置独立串联电阻。

- 参数与网络：`shared_resistors=R1-R9`；`value=47Ω`；`tolerance=1%`；`per_led_resistor=null`
- 证据：图 70dbaec8a75a / 第 1 页 / 网格 B2-D3，R1~R9 47R/1% 与 LED 网络

## 其他事实

### 电池与充电路径

板上没有电池、充电管理器或电量监测器，电源由 Chain 接口的 VCC_5V 提供。

- 参数与网络：`battery=null`；`charger=null`；`fuel_gauge=null`；`input=VCC_5V via J1/J3`
- 证据：图 72fe63674ce8 / 第 1 页 / 主控页电源仅 VCC_5V->U1->VCC_3V3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Mono 系统架构 | `mcu=U2 STM32G031G8U6`；`regulator=U1 TPAP7343D`；`chain_ports=J1,J3 GROVE_IO`；`debug=JP1`；`display=LED1-LED64`；`protection=D68,D69` |
| 核心器件 | STM32G031G8U6 主控 | `reference=U2`；`part_number=STM32G031G8U6`；`supply=pin3 VDD/VDDA VCC_3V3`；`ground=pin4 VSS/VSSA`；`uart1=PB6/PB7`；`uart2=PA2/PA3`；`debug=PA13 SWDIO,PA14 SWCLK`；`reset=PF2 pin5` |
| 电源 | 5V 到 3.3V 稳压 | `regulator=U1 TPAP7343D`；`input=VCC_5V`；`enable=VCC_5V`；`output=VCC_3V3`；`ground=pins2,5`；`input_cap=C1 1uF/25V`；`output_cap=C2 1uF/25V` |
| 电源 | 5V 与 3.3V 电源轨 | `5v=J1/J3 VCC and U1 input`；`3v3=U1 output -> U2/JP1/R11`；`led_supply_rail=null` |
| 总线 | USART1 与 J1 | `controller=U2 STM32G031G8U6`；`tx=PB6 pin26/U1_TX -> J1 IO2`；`rx=J1 IO1/U1_RX -> PB7 pin27`；`connector=J1 GROVE_IO` |
| 总线 | USART2 与 J3 | `controller=U2 STM32G031G8U6`；`tx=PA2 pin8/U2_TX -> J3 IO1`；`rx=J3 IO2/U2_RX -> PA3 pin9`；`connector=J3 GROVE_IO` |
| 接口 | J1 Chain 接口 | `reference=J1`；`pin1=IO2/U1_TX`；`pin2=IO1/U1_RX`；`pin3=VCC/VCC_5V`；`pin4=GND` |
| 接口 | J3 Chain 接口 | `reference=J3`；`pin1=IO2/U2_RX`；`pin2=IO1/U2_TX`；`pin3=VCC/VCC_5V`；`pin4=GND` |
| 系统结构 | 链式通信方向 | `diagram_direction=J1 -> J3`；`upstream_uart=USART1 PB6/PB7`；`downstream_uart=USART2 PA2/PA3`；`direct_pass_through=false` |
| 保护电路 | Chain 接口 ESD 保护 | `j1_protection=D69 PESDNC2FD5VB`；`j3_protection=D68 PESDNC2FD5VB`；`ground=GND` |
| 调试与烧录 | JP1 SWD 调试接口 | `reference=JP1`；`pin1=VCC_3V3`；`pin2=RST`；`pin3=SWDIO/U2 PA13`；`pin4=SWCLK/U2 PA14-BOOT0`；`pin5=GND` |
| 复位 | STM32 复位网络 | `target=U2 pin5 PF2 RST`；`debug_pin=JP1 pin2`；`pullup=R11 1K to VCC_3V3`；`capacitor=C8 1uF/50V to GND` |
| GPIO 与控制信号 | SWCLK/BOOT0 绑带 | `pin=U2 pin21 PA14-BOOT0`；`debug_net=SWCLK`；`strap=R10 10K/1% to GND` |
| 时钟 | MCU 时钟 | `lse_in=U2 pin1 NC`；`lse_out=U2 pin2 NC`；`external_crystal=null`；`oscillator=null` |
| GPIO 与控制信号 | LED 矩阵 GPIO 映射 | `gpio=PA0,PA1,PA4,PA5,PA6,PA7,PA8,PA11,PA12`；`resistors=R1-R9`；`value=47Ω/1%`；`mcu_pins=PA0.6,PA1.7,PA4.10,PA5.11,PA6.12,PA7.13,PA8.16,PA11.18,PA12.19` |
| 核心器件 | 64 点 LED 矩阵 | `references=LED1-LED64`；`count=64`；`horizontal_lines=9`；`vertical_lines=8`；`control_gpio=PA0,PA1,PA4,PA5,PA6,PA7,PA8,PA11,PA12`；`part_number=null` |
| 模拟电路 | LED 限流网络 | `shared_resistors=R1-R9`；`value=47Ω`；`tolerance=1%`；`per_led_resistor=null` |
| 关键网络 | 通信与显示关键路径 | `upstream=J1 U1_TX/U1_RX <-> U2 PB6/PB7`；`downstream=U2 PA2/PA3 <-> J3 U2_TX/U2_RX`；`display=U2 PA GPIO -> R1-R9 -> LED1-LED64` |
| 总线地址 | 设备地址 | `i2c_address=null`；`spi_chip_select=null`；`uart=USART1,USART2` |
| 存储 | 外部存储 | `external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`internal_flash_capacity=null` |
| 内存与 Flash | 外部内存 | `external_ram=null`；`psram=null`；`ddr=null`；`internal_ram_capacity=null` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s=null` |
| 传感器 | 传感器 | `sensor_ic=null`；`sensor_bus=null` |
| 射频 | 射频电路 | `rf_ic=null`；`antenna=null`；`matching=null` |
| 其他事实 | 电池与充电路径 | `battery=null`；`charger=null`；`fuel_gauge=null`；`input=VCC_5V via J1/J3` |
| 核心器件 | LED 型号与颜色 | `references=LED1-LED64`；`documented_color=white`；`part_number=null`；`schematic_color=null`；`forward_voltage=null` |
| 总线 | UART 波特率与帧格式 | `documented_baud=115200bps`；`documented_frame=8N1`；`hardware_uart=USART1 PB6/PB7,USART2 PA2/PA3`；`firmware_configuration=null` |
| 电源 | 待机与全亮功耗 | `documented_standby=5V@8.13mA`；`documented_full_on=5V@22.29mA`；`schematic_current=null`；`measurement_conditions=null` |

## 待确认事项

- `component.documented-led-color`：正文称 LED 颜色为白色；原理图只给出 LED1~LED64 的通用 LED 符号，没有料号、颜色、正向电压或亮度分档。（证据：图 70dbaec8a75a / 第 1 页 / 整页 LED1~LED64 通用符号，无型号/颜色）
- `bus.documented-uart-format`：正文称 Chain UART 为 115200bps@8N1；原理图确认 USART1/USART2 引脚与方向，但不包含波特率或帧格式配置。（证据：图 72fe63674ce8 / 第 1 页 / U2/J1/J3 UART 网络，无波特率/帧格式注记）
- `power.documented-consumption`：正文称待机 5V@8.13mA、最大亮度全亮 5V@22.29mA；原理图只显示 LDO、MCU 与 LED 限流网络，没有测量条件或电流标注。（证据：图 72fe63674ce8 / 第 1 页 / 主控/电源页无电流注记; 图 70dbaec8a75a / 第 1 页 / LED 页仅 R1-R9 47R 与 LED 矩阵）
- `review.led-color`：请用量产 BOM、LED 丝印或光学检查确认 LED1~LED64 的具体型号与白色发光规格。；原因：原理图只使用通用 LED 符号，没有颜色或料号。
- `review.uart-format`：请用内置固件配置或串口抓包确认 Chain UART 为 115200bps 8N1。；原因：波特率和帧格式属于固件运行配置，不在原理图中。
- `review.power-consumption`：请按产品定义的待机和最大亮度全亮场景实测 5V 输入电流，确认 8.13mA 与 22.29mA。；原因：原理图不能证明整机动态功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `72fe63674ce821521e89fa1c203feb50e663a8b517a596b9d6bd87bf36f3e4c8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/SCH_Chain_MONO_SCH_V0.1_2026_01_04_09_51_33_page_01.png` |
| 2 | 1 | `70dbaec8a75a5b964ecffda68b5f01a4bf86311f458b4a7c05d2281e60aeb8e6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/SCH_Chain_MONO_SCH_V0.1_2026_01_04_09_51_33_page_02.png` |

---

源文档：`zh_CN/chain/Chain_Mono.md`

源文档 SHA-256：`3c2af0733a308dc7b49d5cc3bb5396c78fb900bcb51ed703b0064015ff74ae2b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
