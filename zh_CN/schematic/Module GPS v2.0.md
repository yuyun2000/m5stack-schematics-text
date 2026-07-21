# Module GPS v2.0 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module GPS v2.0 |
| SKU | M003-V2 |
| 产品 ID | `module-gps-v2-0-5fb55f2eda3d` |
| 源文档 | `zh_CN/module/Module GPS v2.0.md` |

## 概述

Module GPS v2.0 以 U2 ATGM336H-6N-74 GNSS 模组为核心，GNSS_TX/GNSS_RX 经 22Ω 串联电阻形成 M5-RXD/M5-TXD，再由 SW1 DIP-8 选择连接到 J2 M5Stack_BUS 的多组 GPIO；PPS 由 SW2 DIP-3 选择 GPIO25/GPIO35/GPIO36，并驱动蓝色指示灯。J2 pin 28 的 +5V 经 U1 VRH3301NLX 转换为 +3.3V，BAT1 为 U2 VBAT 提供备份电源，FB1 与 C5/C6 构成 U2 主电源滤波。U2 的 ANT 与 VCC_RF 经 L1 汇合到 J1 IPEX 有源天线端，D1 LXES15AAA1-153 对射频节点提供对地保护；原理图未展开产品正文所述 AT6668 内部 SoC。

## 检索关键词

`Module GPS v2.0`、`M003-V2`、`ATGM336H-6N-74`、`AT6668`、`VRH3301NLX`、`GNSS`、`GPS`、`BeiDou`、`GLONASS`、`GALILEO`、`QZSS`、`M5Stack_BUS`、`UART`、`GNSS_TX`、`GNSS_RX`、`M5-TXD`、`M5-RXD`、`PPS`、`SW1 DIP-8`、`SW2 DIP-3`、`GPIO17`、`GPIO15`、`GPIO12`、`GPIO0`、`GPIO16`、`GPIO13`、`GPIO34`、`GPIO35`、`GPIO25`、`GPIO36`、`+5V`、`+3.3V`、`VBAT`、`BAT1`、`IPEX`、`VCC_RF`、`LXES15AAA1-153`、`nRESET`、`NMEA0183`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATGM336H-6N-74 | GNSS 接收模组，提供 UART、PPS、备份电源和有源天线接口 | 图 4e509d311830 / 第 1 页 / 页面中央 U2 方框，器件值 ATGM336H-6N-74，pin 1-18 标注 TXD0、RXD0、1PPS、VBAT、VCC、nRESET、ANT、VCC_RF 等 |
| U1 | VRH3301NLX | +5V 至 +3.3V 的线性稳压器 | 图 4e509d311830 / 第 1 页 / 页面左上 U1 VRH3301NLX，VIN pin 4 接 +5V，VOUT pin 1 接 +3.3V，EN pin 3 接 +5V |
| SW1 | SW DIP-8 | M5-TXD/M5-RXD 到八个 M5-Bus GPIO 的 UART 路由选择开关 | 图 4e509d311830 / 第 1 页 / 页面上方中央 SW1 SW DIP-8，左侧 GPIO17/GPIO15/GPIO12/GPIO0/GPIO16/GPIO13/GPIO34/GPIO35，右侧分组接 M5-TXD/M5-RXD |
| SW2 | SW DIP-3 | PPS 到 GPIO25、GPIO35 或 GPIO36 的路由选择开关 | 图 4e509d311830 / 第 1 页 / 页面上方中央 SW2 SW DIP-3，左侧 GPIO25/GPIO35/GPIO36，右侧 pin 4-6 共接 PPS |
| J2 | M5Stack_BUS | 30 针主机堆叠总线，提供可选 UART/PPS GPIO、电源、EN 和辅助 GPIO | 图 4e509d311830 / 第 1 页 / 页面右侧 J2 M5Stack_BUS，pin 1-30 网络名完整可见 |
| J1 | IPEX | GNSS 外部有源天线射频连接器 | 图 4e509d311830 / 第 1 页 / 页面中央偏右 J1 IPEX，pin 1 接 ANT/VCC_RF 汇合节点，pin 2、3 接 GND |
| BAT1 | Battery_SMD | U2 VBAT 备份电源 | 图 4e509d311830 / 第 1 页 / 页面左侧中部 BAT1 Battery_SMD，上端 VBAT、下端 GND，VBAT 连接 U2 pin 6 |
| D1 | LXES15AAA1-153 | IPEX 射频节点到 GND 的保护器件 | 图 4e509d311830 / 第 1 页 / 页面中央偏右 D1 LXES15AAA1-153，连接 ANT/IPEX 节点与 GND |
| L1 | 47nH ±5% | U2 VCC_RF 到天线节点的射频偏置电感 | 图 4e509d311830 / 第 1 页 / 页面 U2 右侧 L1 47nH ±5%，串联在 pin 14/VCC_RF 与 ANT/IPEX 节点之间 |
| FB1 | 120Ω/MB | +3.3V 到 U2 VCC 的磁珠滤波器 | 图 4e509d311830 / 第 1 页 / 页面 U2 左下 FB1，值标 120Ω/MB，连接 +3.3V 与 U2 pin 8/VCC |
| R1,R3 | 22Ω; 22Ω | GNSS UART TX/RX 串联阻尼电阻 | 图 4e509d311830 / 第 1 页 / 页面 U2 左侧 R1 22Ω 位于 M5-RXD/GNSS_TX，R3 22Ω 位于 M5-TXD/GNSS_RX |
| R2 | 10KΩ | PPS 到 +3.3V 的上拉电阻 | 图 4e509d311830 / 第 1 页 / 页面 U2 左侧 R2 10KΩ，上端 +3.3V，下端连接 PPS/U2 pin 4 |
| D2,R5 | Blue 0603; 1KΩ | PPS 脉冲状态指示支路 | 图 4e509d311830 / 第 1 页 / 页面左下 PPS 经 R5 1KΩ、D2 Blue 0603 串联到 GND |
| C1,C2,C3,C4,C5,C6 | 22uF; 100nF; 22uF; 100nF; 22uF; 100nF | +5V、+3.3V 和 U2 VCC 的电源去耦与储能 | 图 4e509d311830 / 第 1 页 / 页面左上 U1 周围 C1-C4 与页面 U2 左下 FB1 后 C5/C6，均接相应电源轨与 GND |

## 系统结构

### Module GPS v2.0 系统架构

U2 ATGM336H-6N-74 完成 GNSS 接收，U1 VRH3301NLX 生成 +3.3V，BAT1 提供 VBAT 备份，SW1/SW2 将 UART 与 PPS 路由到 J2 M5Stack_BUS，J1 IPEX、L1 与 D1 构成有源天线接口。

- 参数与网络：`gnss_module=U2 ATGM336H-6N-74`；`regulator=U1 VRH3301NLX`；`host_bus=J2 M5Stack_BUS`；`uart_selector=SW1 SW DIP-8`；`pps_selector=SW2 SW DIP-3`；`backup_supply=BAT1 VBAT`；`antenna=J1 IPEX`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页：左上 U1，中央 U2/SW1/SW2/J1，右侧 J2，左侧 BAT1

## 核心器件

### U2 ATGM336H-6N-74 引脚

U2 pin 1 GND、2 TXD0、3 RXD0、4 1PPS、5 ON/OFF、6 VBAT、7 NC、8 VCC、9 nRESET、10 GND、11 ANT、12 GND、13 NC、14 VCC_RF、15 NC、16 RXD1、17 TXD1、18 NC。图上已连接 TXD0、RXD0、1PPS、VBAT、VCC、ANT、VCC_RF 与 GND；ON/OFF、nRESET、RXD1、TXD1 及 NC 针脚未外接。

- 参数与网络：`reference=U2`；`part_number=ATGM336H-6N-74`；`pins_1_9=1:GND,2:TXD0,3:RXD0,4:1PPS,5:ON/OFF,6:VBAT,7:NC,8:VCC,9:nRESET`；`pins_10_18=10:GND,11:ANT,12:GND,13:NC,14:VCC_RF,15:NC,16:RXD1,17:TXD1,18:NC`；`unused_function_pins=5:ON/OFF,9:nRESET,16:RXD1,17:TXD1`
- 证据：图 4e509d311830 / 第 1 页 / 页面中央 U2 方框左右 pin 1-18 名称及外部连线

## 电源

### +5V 至 +3.3V 稳压

J2 pin 28 引出 +5V；+5V 连接 U1 pin 4/VIN 与 pin 3/EN，U1 pin 1/VOUT 输出 +3.3V，pin 2、5/VSS 接 GND。C1 22uF、C2 100nF 并联在 +5V 与 GND，C3 22uF、C4 100nF 并联在 +3.3V 与 GND。

- 参数与网络：`input=J2 pin 28/+5V`；`regulator=U1 VRH3301NLX`；`vin=pin 4 -> +5V`；`enable=pin 3 -> +5V`；`output=pin 1 -> +3.3V`；`ground=pins 2,5/VSS`；`input_caps=C1 22uF,C2 100nF`；`output_caps=C3 22uF,C4 100nF`
- 证据：图 4e509d311830 / 第 1 页 / 页面左上 U1/C1-C4 与右侧 J2 pin 28/+5V 同名网络

### U2 VCC 电源滤波

+3.3V 经 FB1 120Ω/MB 连接 U2 pin 8/VCC；FB1 后的 VCC 节点由 C5 22uF 与 C6 100nF 并联到 GND。

- 参数与网络：`source_rail=+3.3V`；`filter=FB1 120Ω/MB`；`load=U2 pin 8/VCC`；`decoupling=C5 22uF,C6 100nF`；`return=GND`
- 证据：图 4e509d311830 / 第 1 页 / 页面 U2 左下 +3.3V-FB1-VCC pin 8 与 C5/C6/GND

### GNSS 备份电源 VBAT

BAT1 Battery_SMD 上端连接 VBAT、下端连接 GND；VBAT 同名网络连接 U2 pin 6/VBAT。该页未标 BAT1 的电压、容量、化学体系或充电路径。

- 参数与网络：`battery=BAT1 Battery_SMD`；`positive_net=VBAT`；`module_pin=U2 pin 6/VBAT`；`negative=GND`；`voltage_visible=false`；`capacity_visible=false`；`charging_path_visible=false`
- 证据：图 4e509d311830 / 第 1 页 / 页面左侧 BAT1 VBAT/GND 与 U2 左侧 pin 6/VBAT 同名网络

### J2 M5Stack_BUS 电源轨

J2 pin 1、3、5 为 GND，pin 12 为 +3.3V，pin 25、27、29 为 HPWR，pin 28 为 +5V，pin 30 标 BATTERY 并引出 BAT 网络；本页只显示 +5V 参与 U1 稳压，BAT 与 HPWR 未连接到其他负载。

- 参数与网络：`ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY -> BAT`；`used_supply=+5V -> U1`
- 证据：图 4e509d311830 / 第 1 页 / 页面右侧 J2 pin 1-5、12、25-30 与 +5V/BAT 外部网络

## 接口

### J2 M5Stack_BUS 完整针脚

J2 奇数针为 1 GND、3 GND、5 GND、7 GPIO23、9 GPIO19、11 GPIO18、13 GPIO3、15 GPIO16、17 GPIO21、19 GPIO2、21 GPIO12、23 GPIO15、25 HPWR、27 HPWR、29 HPWR；偶数针为 2 GPIO35、4 GPIO36、6 EN、8 GPIO25、10 GPIO26、12 +3.3V、14 GPIO1、16 GPIO17、18 GPIO22、20 GPIO5、22 GPIO13、24 GPIO0、26 GPIO34、28 +5V、30 BATTERY。

- 参数与网络：`reference=J2 M5Stack_BUS`；`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY`
- 证据：图 4e509d311830 / 第 1 页 / 页面右侧 J2 M5Stack_BUS 内部 pin 1-30 与网络名

## 总线

### GNSS 主 UART

U2 pin 2/TXD0 经 GNSS_TX 网络与 R1 22Ω 连接 M5-RXD；U2 pin 3/RXD0 经 GNSS_RX 网络与 R3 22Ω 连接 M5-TXD。信号命名表明 GNSS 发送端接主机接收网络，GNSS 接收端接主机发送网络。

- 参数与网络：`device=U2 ATGM336H-6N-74`；`device_tx=pin 2/TXD0 -> GNSS_TX -> R1 22Ω -> M5-RXD`；`device_rx=pin 3/RXD0 -> GNSS_RX -> R3 22Ω -> M5-TXD`；`controller_rx_net=M5-RXD`；`controller_tx_net=M5-TXD`；`electrical_rail=+3.3V`
- 证据：图 4e509d311830 / 第 1 页 / 页面 U2 左侧 pin 2/3、GNSS_TX/GNSS_RX、R1/R3 22Ω 与 M5-RXD/M5-TXD

### SW1 UART GPIO 路由

SW1 pin 16、15、14、13 共接 M5-TXD，分别可通过开关连接 pin 1/GPIO17、2/GPIO15、3/GPIO12、4/GPIO0；pin 12、11、10、9 共接 M5-RXD，分别可通过开关连接 pin 5/GPIO16、6/GPIO13、7/GPIO34、8/GPIO35。

- 参数与网络：`m5_txd_routes=16-1:GPIO17,15-2:GPIO15,14-3:GPIO12,13-4:GPIO0`；`m5_rxd_routes=12-5:GPIO16,11-6:GPIO13,10-7:GPIO34,9-8:GPIO35`；`switch=SW1 SW DIP-8`；`selection_rule=each route independently switched`
- 证据：图 4e509d311830 / 第 1 页 / 页面上方 SW1，pin 1-8 左侧 GPIO 与 pin 9-16 右侧 M5-RXD/M5-TXD 分组母线

## 总线地址

### 总线地址可见性

原理图使用 UART 与 PPS 接口，没有 I2C 或 SPI 外设连接，也未标出任何设备地址。

- 参数与网络：`uart_address_visible=false`；`i2c_bus_visible=false`；`spi_bus_visible=false`；`device_address_visible=false`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页所有 U2、SW1/SW2 与 J2 信号，无 I2C/SPI 或地址标注

## GPIO 与控制信号

### U2 PPS 输出与上拉

U2 pin 4/1PPS 连接 PPS 网络；R2 10KΩ 将 PPS 上拉到 +3.3V，PPS 同时连接 SW2 与 R5/D2 指示支路。

- 参数与网络：`source=U2 pin 4/1PPS`；`net=PPS`；`pullup=R2 10KΩ to +3.3V`；`selector=SW2`；`indicator=R5 1KΩ,D2 Blue 0603`
- 证据：图 4e509d311830 / 第 1 页 / 页面 U2 左侧 pin 4/PPS、R2 10KΩ，页面上方 SW2 与左下 R5/D2

### SW2 PPS GPIO 路由

SW2 pin 6、5、4 共接 PPS，分别可通过三位开关连接 pin 1/GPIO25、pin 2/GPIO35、pin 3/GPIO36；这些 GPIO 对应 J2 pin 8、2、4。

- 参数与网络：`switch=SW2 SW DIP-3`；`routes=6-1:GPIO25/J2 pin 8,5-2:GPIO35/J2 pin 2,4-3:GPIO36/J2 pin 4`；`source_net=PPS`
- 证据：图 4e509d311830 / 第 1 页 / 页面上方 SW2 pin 1-6 与右侧 PPS 母线，右侧 J2 GPIO25/GPIO35/GPIO36 针脚

### PPS 蓝色指示灯

PPS 经 R5 1KΩ 与 D2 Blue 0603 串联到 GND，形成 PPS 高电平驱动的指示支路。

- 参数与网络：`path=PPS -> R5 1KΩ -> D2 Blue 0603 -> GND`；`led_reference=D2`；`led_color=Blue`；`package=0603`
- 证据：图 4e509d311830 / 第 1 页 / 页面左下 PPS-R5-D2-GND 串联支路

## 时钟

### 时钟源可见性

单页原理图未绘出独立晶体、谐振器或振荡器；ATGM336H-6N-74 内部 GNSS 时钟未展开，外部只提供 1PPS 时序输出。

- 参数与网络：`external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false`；`timing_output=U2 pin 4/1PPS`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页无 Y/X 时钟器件；U2 pin 4 标 1PPS

## 复位

### U2 nRESET 与 ON/OFF

U2 pin 9/nRESET 与 pin 5/ON/OFF 均未连接外部网络；J2 pin 6/EN 也未画到 U2，因此本页没有主机复位、开关机按键或复位 RC 网络。

- 参数与网络：`nreset=U2 pin 9 unconnected`；`on_off=U2 pin 5 unconnected`；`host_enable=J2 pin 6/EN unconnected`；`reset_rc_visible=false`；`power_button_visible=false`
- 证据：图 4e509d311830 / 第 1 页 / 页面 U2 左侧 pin 5/ON/OFF、pin 9/nRESET 与右侧 J2 pin 6/EN，均无外部连接

## 保护电路

### IPEX 天线节点保护

D1 LXES15AAA1-153 跨接 ANT/IPEX 射频节点与 GND，为外部天线端提供对地保护；图中未显示其他 UART、电源或 M5-Bus 专用 TVS/ESD 器件。

- 参数与网络：`protector=D1 LXES15AAA1-153`；`protected_node=ANT/J1 pin 1`；`return=GND`；`other_interface_protection_visible=false`
- 证据：图 4e509d311830 / 第 1 页 / 页面中央偏右 D1 从 ANT/IPEX 节点接至 GND；完整页面无其他 TVS/ESD 位号

## 内存与 Flash

### 存储器与内存可见性

原理图没有独立 Flash、EEPROM、RAM、SD 卡或其他存储器件；U2 内部存储结构未展开。

- 参数与网络：`external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页全部器件，无存储器或存储连接器位号

## 射频

### GNSS 有源天线射频与偏置路径

U2 pin 11/ANT 直接连接 J1 pin 1 的射频节点；U2 pin 14/VCC_RF 经 L1 47nH ±5% 注入同一节点。J1 pin 2、3 接 GND，形成带 VCC_RF 偏置的 IPEX 天线接口。

- 参数与网络：`rf_input=U2 pin 11/ANT`；`bias_output=U2 pin 14/VCC_RF`；`bias_inductor=L1 47nH ±5%`；`connector_signal=J1 pin 1`；`connector_ground=J1 pins 2,3`
- 证据：图 4e509d311830 / 第 1 页 / 页面 U2 右侧 pin 11/ANT、pin 14/VCC_RF、L1 与 J1 IPEX pin 1-3

## 调试与烧录

### 调试接口可见性

原理图未绘出 SWD、JTAG、测试排针或专用调试连接器；U2 第二组 UART TXD1/RXD1 也未外接。

- 参数与网络：`swd_visible=false`；`jtag_visible=false`；`test_header_visible=false`；`secondary_uart=U2 pin 17/TXD1 and pin 16/RXD1 unconnected`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页器件与连接器；U2 右上 TXD1/RXD1 未连线

## 其他事实

### 音频、传感器与其他总线可见性

原理图未绘出音频器件、独立传感器、模拟采样前端、CAN、RS-485、USB、SDIO、MIPI 或 I2S 电路。

- 参数与网络：`audio_visible=false`；`sensor_visible=false`；`analog_frontend_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`
- 证据：图 4e509d311830 / 第 1 页 / 完整单页全部功能分区，仅含 GNSS、电源、UART/PPS、天线与 M5-Bus

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module GPS v2.0 系统架构 | `gnss_module=U2 ATGM336H-6N-74`；`regulator=U1 VRH3301NLX`；`host_bus=J2 M5Stack_BUS`；`uart_selector=SW1 SW DIP-8`；`pps_selector=SW2 SW DIP-3`；`backup_supply=BAT1 VBAT`；`antenna=J1 IPEX` |
| 核心器件 | U2 ATGM336H-6N-74 引脚 | `reference=U2`；`part_number=ATGM336H-6N-74`；`pins_1_9=1:GND,2:TXD0,3:RXD0,4:1PPS,5:ON/OFF,6:VBAT,7:NC,8:VCC,9:nRESET`；`pins_10_18=10:GND,11:ANT,12:GND,13:NC,14:VCC_RF,15:NC,16:RXD1,17:TXD1,18:NC`；`unused_function_pins=5:ON/OFF,9:nRESET,16:RXD1,17:TXD1` |
| 核心器件 | ATGM336H-6N-74 内部 SoC | `documented_soc=AT6668`；`schematic_module=U2 ATGM336H-6N-74`；`internal_soc_visible=false` |
| 电源 | +5V 至 +3.3V 稳压 | `input=J2 pin 28/+5V`；`regulator=U1 VRH3301NLX`；`vin=pin 4 -> +5V`；`enable=pin 3 -> +5V`；`output=pin 1 -> +3.3V`；`ground=pins 2,5/VSS`；`input_caps=C1 22uF,C2 100nF`；`output_caps=C3 22uF,C4 100nF` |
| 电源 | U2 VCC 电源滤波 | `source_rail=+3.3V`；`filter=FB1 120Ω/MB`；`load=U2 pin 8/VCC`；`decoupling=C5 22uF,C6 100nF`；`return=GND` |
| 电源 | GNSS 备份电源 VBAT | `battery=BAT1 Battery_SMD`；`positive_net=VBAT`；`module_pin=U2 pin 6/VBAT`；`negative=GND`；`voltage_visible=false`；`capacity_visible=false`；`charging_path_visible=false` |
| 电源 | J2 M5Stack_BUS 电源轨 | `ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY -> BAT`；`used_supply=+5V -> U1` |
| 接口 | J2 M5Stack_BUS 完整针脚 | `reference=J2 M5Stack_BUS`；`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY` |
| 总线 | GNSS 主 UART | `device=U2 ATGM336H-6N-74`；`device_tx=pin 2/TXD0 -> GNSS_TX -> R1 22Ω -> M5-RXD`；`device_rx=pin 3/RXD0 -> GNSS_RX -> R3 22Ω -> M5-TXD`；`controller_rx_net=M5-RXD`；`controller_tx_net=M5-TXD`；`electrical_rail=+3.3V` |
| 总线 | SW1 UART GPIO 路由 | `m5_txd_routes=16-1:GPIO17,15-2:GPIO15,14-3:GPIO12,13-4:GPIO0`；`m5_rxd_routes=12-5:GPIO16,11-6:GPIO13,10-7:GPIO34,9-8:GPIO35`；`switch=SW1 SW DIP-8`；`selection_rule=each route independently switched` |
| 总线 | GNSS UART 参数与协议 | `documented_baud=115200`；`documented_frame=8N1`；`documented_protocol=NMEA0183 4.1`；`schematic_parameters_visible=false` |
| GPIO 与控制信号 | U2 PPS 输出与上拉 | `source=U2 pin 4/1PPS`；`net=PPS`；`pullup=R2 10KΩ to +3.3V`；`selector=SW2`；`indicator=R5 1KΩ,D2 Blue 0603` |
| GPIO 与控制信号 | SW2 PPS GPIO 路由 | `switch=SW2 SW DIP-3`；`routes=6-1:GPIO25/J2 pin 8,5-2:GPIO35/J2 pin 2,4-3:GPIO36/J2 pin 4`；`source_net=PPS` |
| GPIO 与控制信号 | PPS 蓝色指示灯 | `path=PPS -> R5 1KΩ -> D2 Blue 0603 -> GND`；`led_reference=D2`；`led_color=Blue`；`package=0603` |
| 射频 | GNSS 有源天线射频与偏置路径 | `rf_input=U2 pin 11/ANT`；`bias_output=U2 pin 14/VCC_RF`；`bias_inductor=L1 47nH ±5%`；`connector_signal=J1 pin 1`；`connector_ground=J1 pins 2,3` |
| 保护电路 | IPEX 天线节点保护 | `protector=D1 LXES15AAA1-153`；`protected_node=ANT/J1 pin 1`；`return=GND`；`other_interface_protection_visible=false` |
| 复位 | U2 nRESET 与 ON/OFF | `nreset=U2 pin 9 unconnected`；`on_off=U2 pin 5 unconnected`；`host_enable=J2 pin 6/EN unconnected`；`reset_rc_visible=false`；`power_button_visible=false` |
| 射频 | 支持的卫星系统与频点 | `documented_systems=GPS,QZSS,BD2,BD3,GALILEO,GLONASS`；`documented_frequencies=BDS:B1I+B1C; GPS/QZSS/SBAS:L1; GALILEO:E1; GLONASS:R1`；`schematic_systems_visible=false`；`schematic_frequencies_visible=false` |
| 总线地址 | 总线地址可见性 | `uart_address_visible=false`；`i2c_bus_visible=false`；`spi_bus_visible=false`；`device_address_visible=false` |
| 时钟 | 时钟源可见性 | `external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false`；`timing_output=U2 pin 4/1PPS` |
| 调试与烧录 | 调试接口可见性 | `swd_visible=false`；`jtag_visible=false`；`test_header_visible=false`；`secondary_uart=U2 pin 17/TXD1 and pin 16/RXD1 unconnected` |
| 内存与 Flash | 存储器与内存可见性 | `external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false` |
| 其他事实 | 音频、传感器与其他总线可见性 | `audio_visible=false`；`sensor_visible=false`；`analog_frontend_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false` |

## 待确认事项

- `component.internal-soc`：产品正文将 SoC 写为 AT6668，但原理图只显示 U2 ATGM336H-6N-74 模组，没有 AT6668 的独立位号、供电、时钟或内部连接。（证据：图 4e509d311830 / 第 1 页 / 页面中央 U2 仅标 ATGM336H-6N-74，未出现 AT6668 位号）
- `bus.uart-format`：产品正文记载 UART 为 115200bps、8N1，并使用 NMEA0183 4.1；本地原理图仅显示 UART 网络与路由，没有打印波特率、帧格式或协议版本。（证据：图 4e509d311830 / 第 1 页 / 页面 U2 TXD0/RXD0 与 SW1 UART 路由区，未标 UART 参数或 NMEA 版本）
- `rf.documented-gnss-systems`：产品正文记载 GPS/QZSS/BD2/BD3/GALILEO/GLONASS，并列出 BDS B1I+B1C、GPS/QZSS/SBAS L1、GALILEO E1、GLONASS R1；原理图只标 U2 模组型号和 ANT 接口，未打印系统或频点。（证据：图 4e509d311830 / 第 1 页 / 页面 U2 ATGM336H-6N-74 与 ANT/IPEX 区域，无卫星系统或频点文字）
- `review.internal-soc`：U2 ATGM336H-6N-74 内部 SoC 是否确认为产品正文记载的 AT6668？；原因：本地原理图只显示完整 GNSS 模组型号，没有展开内部 SoC 位号或连接。
- `review.uart-format`：Module GPS v2.0 的默认 UART 是否确认为 115200bps、8N1，并输出 NMEA0183 4.1？；原因：这些参数来自产品正文，本地原理图未打印波特率、帧格式或协议版本。
- `review.gnss-systems`：当前 U2 物料版本正式支持的卫星系统与频点是否与产品正文列表完全一致？；原因：本地原理图只标 U2 ATGM336H-6N-74 和天线连接，没有系统、频点或固件配置信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4e509d31183091f6adcf716c3b0f4ce73e242929deff071f8ade5b7e87f8732f` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/schematic.png` |

---

源文档：`zh_CN/module/Module GPS v2.0.md`

源文档 SHA-256：`c6497f619960ca146c026693c7ac0a6c00f276410815a3e2c48a3e792015c24c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
