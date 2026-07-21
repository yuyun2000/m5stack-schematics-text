# Unit ZigBee 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ZigBee |
| SKU | U110 |
| 产品 ID | `unit-zigbee-ddec232a18a5` |
| 源文档 | `zh_CN/unit/zigbee.md` |

## 概述

Unit ZigBee 原理图以 DRF1609H（M1）无线通信模组为核心，通过 J1 HY-2.0_UART 的 RX/TX 与外部主机通信。SPX3819M5-L-3-3（U1）将 J1 的 +5V 转换为 +3.3V，为 M1 供电；M1 KEY 接 S1 按键到地，RESET_N 使用 10KΩ 上拉和 100nF 对地电容。M1 LED_STA 经 R2 1KΩ 驱动 D1 绿色 0603 LED，LED_DAT、TMS、TCK 未连接。图面未展开 DRF1609H 内部 CC2630F128、射频/天线、协议栈、UART 默认速率或无线性能。

## 检索关键词

`Unit ZigBee`、`U110`、`DRF1609H`、`CC2630F128`、`SPX3819M5-L-3-3`、`HY-2.0_UART`、`UART`、`38400bps 8N1`、`G_TXD`、`G_RXD`、`TX`、`RX`、`KEY`、`RESET_N`、`LED_STA`、`LED_DAT`、`TMS`、`TCK`、`S1 SW-PB`、`D1 green LED 0603`、`R1 10KΩ`、`R2 1KΩ`、`+5V`、`+3.3V`、`Zigbee`、`2.4GHz`、`250Kbps`、`1km`、`SMA antenna`、`mesh network`、`C1 22uF`、`C2 22uF`、`C3 10uF`、`C4 100nF`、`C5 100nF`、`C6 100nF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | DRF1609H | UART 无线通信模组，提供 TX/RX、KEY、RESET_N 与状态 LED 接口 | 图 38688ae749cc / 第 1 页 / 页 1 中部 M1 DRF1609H，pins 1~10 与 TX/RX/KEY/RESET_N/LED_DAT/LED_STA/TMS/TCK/VCC/GND |
| U1 | SPX3819M5-L-3-3 | 将 +5V 稳压为 +3.3V 的 LDO | 图 38688ae749cc / 第 1 页 / 页 1 左上 U1 SPX3819M5-L-3-3，IN/EN/GND/BYP-ADJ/OUT pins 1~5 与 +5V/+3.3V |
| J1 | HY-2.0_UART | 外部 RX、TX、+5V 与 GND Grove UART 接口 | 图 38688ae749cc / 第 1 页 / 页 1 右中 J1 HY-2.0_UART pins 1~4 与 G_TXD/G_RXD/+5V/GND |
| S1 | SW-PB | 按下时将 M1 KEY pin 4 接 GND 的按键 | 图 38688ae749cc / 第 1 页 / 页 1 中部 M1 KEY pin 4-S1 SW-PB-GND |
| D1/R2 | 绿灯 0603 / 1KΩ | 由 M1 LED_STA pin 8 驱动的绿色状态 LED 支路 | 图 38688ae749cc / 第 1 页 / 页 1 左中 M1 LED_STA pin 8-R2 1KΩ-D1 绿灯0603-GND |
| R1/C5 | 10KΩ / 100nF | M1 RESET_N 的 +3.3V 上拉与对地复位电容 | 图 38688ae749cc / 第 1 页 / 页 1 中部 M1 RESET_N pin 3-R1 10KΩ-+3.3V 与 C5 100nF-GND |
| C1/C2 | 22uF / 22uF | U1 +5V 输入与 +3.3V 输出侧储能电容 | 图 38688ae749cc / 第 1 页 / 页 1 左上 C1 22uF 跨 +5V/GND，C2 22uF 跨 +3.3V/GND |
| C3/C4 | 10uF / 100nF | M1 +3.3V 供电去耦与储能 | 图 38688ae749cc / 第 1 页 / 页 1 中部 M1 VCC pin 1 的 +3.3V 节点经 C3 10uF/C4 100nF 接 GND |
| C6 | 100nF | J1 +5V 接口电源去耦 | 图 38688ae749cc / 第 1 页 / 页 1 右中 J1 VCC/+5V 旁 C6 100nF 到 GND |

## 系统结构

### Unit ZigBee

M1 DRF1609H 通过 J1 UART 与外部主机通信，由 U1 将 +5V 转为 +3.3V 供电，并连接 KEY 按键、RESET_N RC 与 LED_STA 绿色指示灯。

- 参数与网络：`module=M1 DRF1609H`；`host_interface=J1 HY-2.0_UART`；`power=+5V->U1 SPX3819M5-L-3-3->+3.3V`；`button=M1 KEY-S1-GND`；`reset=M1 RESET_N-R1/C5`；`indicator=M1 LED_STA-R2-D1-GND`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 完整单页 U1/M1/J1/S1/D1 与 +5V/+3.3V/UART/KEY/RESET_N/LED_STA 网络

## 核心器件

### M1 DRF1609H 引脚

M1 pin 1 VCC 接 +3.3V，pin 2 GND 接地，pin 3 RESET_N 接复位网络，pin 4 KEY 接 S1，pin 5 TX 接 G_TXD，pin 6 RX 接 G_RXD，pin 7 LED_DAT 未连接，pin 8 LED_STA 接 R2/D1，pins 9/10 TMS/TCK 未连接。

- 参数与网络：`pin_1=VCC,+3.3V`；`pin_2=GND`；`pin_3=RESET_N`；`pin_4=KEY,S1`；`pin_5=TX,G_TXD`；`pin_6=RX,G_RXD`；`pin_7=LED_DAT no-connect`；`pin_8=LED_STA,R2/D1`；`pin_9=TMS no-connect`；`pin_10=TCK no-connect`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 中部 M1 左右两侧 pins 1~10、网络名与未连接标记

## 电源

### U1 SPX3819M5-L-3-3

U1 IN pin 1 与 EN pin 3 接 +5V，OUT pin 5 输出 +3.3V，GND pin 2 接地，BYP/ADJ pin 4 在页面未连接。

- 参数与网络：`input=IN pin 1,+5V`；`enable=EN pin 3,+5V`；`output=OUT pin 5,+3.3V`；`ground=pin 2,GND`；`bypass_adjust=pin 4 no-connect`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 左上 U1 pins 1~5 与 +5V/+3.3V/GND/未连接标记

### U1 输入输出电容

C1 22uF 跨接 U1 输入 +5V 与 GND，C2 22uF 跨接 U1 输出 +3.3V 与 GND。

- 参数与网络：`input_capacitor=C1 22uF`；`output_capacitor=C2 22uF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 左上 C1/C2 与 U1 输入输出电源轨

### M1 +3.3V 供电

M1 VCC pin 1 接 +3.3V，GND pin 2 接地；C3 10uF 与 C4 100nF 从 +3.3V 接 GND。

- 参数与网络：`vcc=M1 pin 1,+3.3V`；`ground=M1 pin 2,GND`；`decoupling=C3 10uF,C4 100nF`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 中部 M1 VCC/GND pins 1/2 与 C3/C4

### 电池、充电与电源监测

本页未绘出电池、充电器、负载开关、电量计或电源监测器；+5V 经固定使能 LDO 直接生成 +3.3V。

- 参数与网络：`battery=null`；`charger=null`；`load_switch=null`；`fuel_gauge=null`；`power_monitor=null`；`ldo_enable=tied to +5V`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 整页电源部分仅 U1 与 C1~C4/C6

## 接口

### J1 HY-2.0_UART

J1 pin 1 标 RX 并接 G_TXD/M1 TX pin 5，pin 2 标 TX 并接 G_RXD/M1 RX pin 6，pin 3 标 VCC 并接 +5V，pin 4 接 GND。

- 参数与网络：`pin_1=RX,G_TXD,M1 TX pin 5`；`pin_2=TX,G_RXD,M1 RX pin 6`；`pin_3=VCC,+5V`；`pin_4=GND`；`connector=HY-2.0_UART`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 右中 J1 pins 1~4 与 G_TXD/G_RXD/+5V/GND，同名网络到 M1 pins 5/6

## 总线

### J1 与 M1 UART

M1 TX pin 5 的 G_TXD 网络直接连接 J1 RX pin 1，M1 RX pin 6 的 G_RXD 网络直接连接 J1 TX pin 2；中间未绘出串联电阻或电平转换器。

- 参数与网络：`module_tx=M1.5 TX/G_TXD->J1.1 RX`；`module_rx=M1.6 RX/G_RXD<-J1.2 TX`；`level_shifter=null`；`series_resistor=null`；`module_logic_supply=+3.3V`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 M1 TX/RX 与 J1 RX/TX 的 G_TXD/G_RXD 同名网络

## 总线地址

### 总线地址

本页只显示 UART 点对点连接，没有 I2C/SPI 地址、节点地址、PAN ID 或硬件地址选择网络。

- 参数与网络：`i2c_address=null`；`spi_address=null`；`node_address=null`；`pan_id=null`；`hardware_selector=null`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 整页 UART 与模组控制连接，无 ADDR/0x/PAN 标注

## GPIO 与控制信号

### M1 KEY/S1

M1 KEY pin 4 连接 S1 SW-PB，按键另一端接 GND，因此按下时 KEY 被接地；页面未绘出外部上拉电阻。

- 参数与网络：`module_pin=M1 pin 4 KEY`；`switch=S1 SW-PB`；`pressed_connection=GND`；`external_pullup=null`；`active_state=grounded when pressed`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 中部 M1 KEY pin 4-S1-GND

### D1 绿色状态 LED

M1 LED_STA pin 8 经 R2 1KΩ 连接 D1 绿色 0603 LED，D1 另一端接 GND；M1 LED_DAT pin 7 未连接。

- 参数与网络：`status_pin=M1 pin 8 LED_STA`；`resistor=R2 1KΩ`；`led=D1 绿灯 0603`；`return=GND`；`unused_data_pin=M1 pin 7 LED_DAT no-connect`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 左中 M1 LED_STA/LED_DAT pins 8/7 与 R2/D1/GND/未连接标记

## 时钟

### 时钟网络

本页未绘出外部晶振、谐振器、振荡器或时钟网络；M1 内部时钟未展开。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`clock_net=null`；`module_internal_clock=not expanded`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 整页无 X/Y/OSC/CLK 器件或网络，M1 为黑盒模组

## 复位

### M1 RESET_N

M1 RESET_N pin 3 由 R1 10KΩ 上拉到 +3.3V，并由 C5 100nF 接 GND；本页没有独立复位按键。

- 参数与网络：`reset_pin=M1 pin 3 RESET_N`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C5 100nF to GND`；`reset_button=null`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 中部 M1 RESET_N-R1/C5/+3.3V/GND

## 保护电路

### J1、电源与射频保护

本页未绘出 J1 UART/+5V 的 TVS、ESD 阵列、保险丝、反接保护、过压保护或天线 ESD 器件。

- 参数与网络：`uart_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`antenna_esd=null`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 J1 到 M1/U1 的 UART 与电源路径，无专用保护器件

## 关键网络

### Unit ZigBee 关键网络索引

关键路径为 J1 +5V→U1→+3.3V→M1，M1 TX/G_TXD→J1 RX，J1 TX/G_RXD→M1 RX，M1 KEY→S1→GND，M1 RESET_N→R1/C5，以及 M1 LED_STA→R2→D1→GND。

- 参数与网络：`power=J1 +5V-U1-+3.3V-M1`；`uart_tx=M1.5 G_TXD-J1.1 RX`；`uart_rx=J1.2 TX-G_RXD-M1.6`；`key=M1.4-S1-GND`；`reset=M1.3-R1/C5`；`status_led=M1.8-R2-D1-GND`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 完整单页全部 +5V/+3.3V/G_TXD/G_RXD/KEY/RESET_N/LED_STA 同名网络

## 内存与 Flash

### 外部存储器

本页未绘出独立 Flash、EEPROM、RAM、存储卡或存储总线；M1 内部存储未展开。

- 参数与网络：`external_flash=null`；`eeprom=null`；`external_ram=null`；`storage_card=null`；`storage_bus=null`；`module_internal_memory=not expanded`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 整页无存储器件或存储连接器，M1 为黑盒

## 调试与烧录

### M1 TMS/TCK

M1 TMS pin 9 与 TCK pin 10 在页面标记未连接，整页没有 JTAG/SWD 调试连接器或测试点。

- 参数与网络：`tms=M1 pin 9 no-connect`；`tck=M1 pin 10 no-connect`；`debug_connector=null`；`test_points=null`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 M1 左下 TMS/TCK pins 9/10 未连接标记，整页无调试头

## 其他事实

### 音频、传感器与模拟链路

本页未绘出音频器件、独立传感器、ADC/DAC 或模拟采样链路。

- 参数与网络：`audio=null`；`sensor=null`；`adc=null`；`dac=null`；`analog_front_end=null`
- 证据：图 38688ae749cc / 第 1 页 / 页 1 整页仅电源、UART、模组控制、按键与 LED

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ZigBee | `module=M1 DRF1609H`；`host_interface=J1 HY-2.0_UART`；`power=+5V->U1 SPX3819M5-L-3-3->+3.3V`；`button=M1 KEY-S1-GND`；`reset=M1 RESET_N-R1/C5`；`indicator=M1 LED_STA-R2-D1-GND` |
| 核心器件 | M1 DRF1609H 引脚 | `pin_1=VCC,+3.3V`；`pin_2=GND`；`pin_3=RESET_N`；`pin_4=KEY,S1`；`pin_5=TX,G_TXD`；`pin_6=RX,G_RXD`；`pin_7=LED_DAT no-connect`；`pin_8=LED_STA,R2/D1`；`pin_9=TMS no-connect`；`pin_10=TCK no-connect` |
| 核心器件 | DRF1609H 内部主控与存储 | `schematic_module=DRF1609H`；`internal_mcu=null`；`flash=null`；`ram=null`；`crystal=null`；`rf_front_end=null`；`protocol_stack=null`；`product_document_mcu=CC2630F128` |
| 接口 | J1 HY-2.0_UART | `pin_1=RX,G_TXD,M1 TX pin 5`；`pin_2=TX,G_RXD,M1 RX pin 6`；`pin_3=VCC,+5V`；`pin_4=GND`；`connector=HY-2.0_UART` |
| 总线 | J1 与 M1 UART | `module_tx=M1.5 TX/G_TXD->J1.1 RX`；`module_rx=M1.6 RX/G_RXD<-J1.2 TX`；`level_shifter=null`；`series_resistor=null`；`module_logic_supply=+3.3V` |
| 总线 | UART 默认通信参数 | `schematic_baud=null`；`schematic_frame=null`；`flow_control=null`；`protocol=null`；`product_document_baud=38400bps`；`product_document_frame=8N1` |
| 电源 | U1 SPX3819M5-L-3-3 | `input=IN pin 1,+5V`；`enable=EN pin 3,+5V`；`output=OUT pin 5,+3.3V`；`ground=pin 2,GND`；`bypass_adjust=pin 4 no-connect` |
| 电源 | U1 输入输出电容 | `input_capacitor=C1 22uF`；`output_capacitor=C2 22uF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | M1 +3.3V 供电 | `vcc=M1 pin 1,+3.3V`；`ground=M1 pin 2,GND`；`decoupling=C3 10uF,C4 100nF` |
| 电源 | 电池、充电与电源监测 | `battery=null`；`charger=null`；`load_switch=null`；`fuel_gauge=null`；`power_monitor=null`；`ldo_enable=tied to +5V` |
| GPIO 与控制信号 | M1 KEY/S1 | `module_pin=M1 pin 4 KEY`；`switch=S1 SW-PB`；`pressed_connection=GND`；`external_pullup=null`；`active_state=grounded when pressed` |
| 复位 | M1 RESET_N | `reset_pin=M1 pin 3 RESET_N`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C5 100nF to GND`；`reset_button=null` |
| GPIO 与控制信号 | D1 绿色状态 LED | `status_pin=M1 pin 8 LED_STA`；`resistor=R2 1KΩ`；`led=D1 绿灯 0603`；`return=GND`；`unused_data_pin=M1 pin 7 LED_DAT no-connect` |
| 调试与烧录 | M1 TMS/TCK | `tms=M1 pin 9 no-connect`；`tck=M1 pin 10 no-connect`；`debug_connector=null`；`test_points=null` |
| 射频 | Zigbee 射频与天线 | `module=M1 DRF1609H`；`rf_pin=null`；`matching_network=null`；`antenna_connector=null`；`frequency=null`；`data_rate=null`；`range=null`；`power_current=null`；`routing_depth=null`；`product_document_values=2.4GHz,250Kbps,1km,25mA active,5uA sleep,200-level routing,SMA antenna` |
| 射频 | Zigbee 协议与组网模式 | `schematic_protocol=null`；`zigbee_version=null`；`device_role=null`；`mesh=null`；`broadcast=null`；`p2p=null`；`transparent_uart=null`；`security=null` |
| 总线地址 | 总线地址 | `i2c_address=null`；`spi_address=null`；`node_address=null`；`pan_id=null`；`hardware_selector=null` |
| 时钟 | 时钟网络 | `external_crystal=null`；`external_oscillator=null`；`clock_net=null`；`module_internal_clock=not expanded` |
| 保护电路 | J1、电源与射频保护 | `uart_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`antenna_esd=null` |
| 内存与 Flash | 外部存储器 | `external_flash=null`；`eeprom=null`；`external_ram=null`；`storage_card=null`；`storage_bus=null`；`module_internal_memory=not expanded` |
| 其他事实 | 音频、传感器与模拟链路 | `audio=null`；`sensor=null`；`adc=null`；`dac=null`；`analog_front_end=null` |
| 关键网络 | Unit ZigBee 关键网络索引 | `power=J1 +5V-U1-+3.3V-M1`；`uart_tx=M1.5 G_TXD-J1.1 RX`；`uart_rx=J1.2 TX-G_RXD-M1.6`；`key=M1.4-S1-GND`；`reset=M1.3-R1/C5`；`status_led=M1.8-R2-D1-GND` |

## 待确认事项

- `component.module-internals-not-shown`：原理图只以 DRF1609H 模组表示 M1，没有展开内部 MCU、Flash、RAM、晶振、射频前端或协议栈。（证据：图 38688ae749cc / 第 1 页 / 页 1 M1 DRF1609H 黑盒模组，只显示 10 个外部引脚）
- `bus.uart-default-not-shown`：原理图确认 TX/RX 物理连接，但未打印波特率、数据位、停止位、校验、流控或透明传输协议。（证据：图 38688ae749cc / 第 1 页 / 页 1 M1 TX/RX 与 J1 UART 区域，无 baud/8N1/时序文字）
- `rf.zigbee-antenna-performance-not-shown`：本页没有绘出 DRF1609H 的 RF 引脚、匹配网络、天线连接器或 SMA 天线路径，也未打印工作频段、信道、速率、距离、功耗、接收灵敏度或路由深度。（证据：图 38688ae749cc / 第 1 页 / 页 1 M1 DRF1609H 仅显示 UART/控制/LED/电源引脚，整页无 RF/ANT/SMA 网络）
- `rf.protocol-stack-not-shown`：原理图未标注 Zigbee 协议版本、Coordinator/Router/End Device 角色、MESH、广播、P2P、透明传输或安全配置。（证据：图 38688ae749cc / 第 1 页 / 页 1 原理图只标 DRF1609H 与电气连接，无协议文字）
- `review.module-internals`：DRF1609H 当前硬件版本内部是否使用 CC2630F128，其 Flash/RAM、晶振和射频前端配置是什么？；原因：板级原理图仅显示 DRF1609H 黑盒模组，正文型号不能替代内部器件证据。
- `review.uart-default`：当前模组固件的默认 UART 参数是否为 38400bps 8N1，是否支持流控或其他串口模式？；原因：原理图只确认 TX/RX 连线，串口参数由模组固件决定。
- `review.rf-antenna-performance`：DRF1609H 的频段、信道、速率、通信距离、功耗、灵敏度、路由深度及 SMA 天线连接/匹配是什么？；原因：本页未绘出 RF/ANT/SMA 网络或任何射频性能参数。
- `review.protocol-stack`：模组内置的 Zigbee 协议版本、设备角色、MESH/广播/P2P/透明传输与安全配置是什么？；原因：原理图只能证明 DRF1609H 的电气接口，无法证明固件协议能力。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `38688ae749cceb8974a0bf2432c7a112d5990f897a0720ced4708fd3da14377e` | `https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_sch_01.webp` |

---

源文档：`zh_CN/unit/zigbee.md`

源文档 SHA-256：`d0c3998f46e04670e99ee580a4ae66a5c10da4daabbd04ed8a06dddf576065b4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
