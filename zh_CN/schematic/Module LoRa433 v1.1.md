# Module LoRa433 v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LoRa433 v1.1 |
| SKU | M005-V11 |
| 产品 ID | `module-lora433-v1-1-28fc5bde4e02` |
| 源文档 | `zh_CN/module/Module-LoRa433_V1.1.md` |

## 概述

Module LoRa433 v1.1 以 Ra-02 Module 为射频核心，固定 SPI 的 MOSI/MISO/SCK 分别连接 J1 M5Stack_BUS 的 GPIO23/GPIO19/GPIO18，S1 DIP-8 则将 RST、IRQ 与 NSS 选择到多组主机 GPIO。J1 pin 28 的 +5V 经 U1 RT9013_3.3V 转换为 +3.3V，C1-C5 为 Ra-02 供电提供跨频段去耦。射频区画出 E2 ANT_SMA 与 R1 0Ω，以及 E1 ANT_IPEX 与 R2/C8/C9 的 NC 选配网络；原理图未展开产品正文所述 SX1278 内部芯片。

## 检索关键词

`Module LoRa433 v1.1`、`M005-V11`、`Ra-02`、`SX1278`、`LoRa433`、`433MHz`、`410MHz~525MHz`、`SPI`、`MOSI`、`MISO`、`SCK`、`NSS`、`RST`、`IRQ`、`DIO0`、`S1 DIP-8`、`M5Stack_BUS`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO25`、`GPIO13`、`GPIO35`、`GPIO34`、`GPIO0`、`GPIO15`、`GPIO12`、`GPIO5`、`RT9013_3.3V`、`+5V`、`+3.3V`、`ANT_SMA`、`ANT_IPEX`、`R1 0Ω`、`R2 NC`、`R7 433M`、`R8 868M`、`R9 915M`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| Ra-02 Module | Ra-02 | LoRa 射频通信模组，提供 SPI、复位、中断、DIO 与天线端口 | 图 2864e140e987 / 第 1 页 / 页面中央 Ra-02 Module 方框，pin 1-16 标注 GND、3V3、RESET、DIO0-DIO5、SCK、MISO、MOSI、NSS |
| U1 | RT9013_3.3V | +5V 至 +3.3V 的低压差稳压器 | 图 2864e140e987 / 第 1 页 / 页面左下 U1 RT9013_3.3V，VIN pin 1 接 +5V，VOUT pin 5 接 +3.3V，EN pin 3 经 R6 接 +5V |
| S1 | SW DIP-8 | RST、IRQ 与 NSS 到八个 M5-Bus GPIO 的路由选择开关 | 图 2864e140e987 / 第 1 页 / 页面下方中央 S1 SW DIP-8，左侧 GPIO25/GPIO13/GPIO35/GPIO34/GPIO0/GPIO15/GPIO12/GPIO5，右侧分组接 RST/IRQ/NSS |
| J1 | M5Stack_BUS | 30 针主机堆叠接口，承载固定 SPI、可选控制 GPIO 和 +5V 电源 | 图 2864e140e987 / 第 1 页 / 页面右侧 J1 M5Stack_BUS，pin 1-30 网络名完整可见 |
| E2,R1 | ANT_SMA; 0Ω | SMA 天线及其串联 0Ω 配置支路 | 图 2864e140e987 / 第 1 页 / 页面左上 E2 ANT_SMA，信号端串联 R1 0Ω，外壳/回路接 GND |
| E1 | ANT_IPEX | 备选 IPEX 天线接口 | 图 2864e140e987 / 第 1 页 / 页面左上偏下 E1 ANT_IPEX，信号端连接 R2/C8 节点，回路接 GND |
| R2,C8,C9 | NC; NC; NC | IPEX 射频路径的未装串联/对地匹配元件位置 | 图 2864e140e987 / 第 1 页 / 页面 E1 右侧 R2 串联、C8/C9 对地的 π 型位置，三者均标 NC |
| C1,C2,C3,C4,C5 | 100uF; 1uF; 100nF; 10nF; 1nF | Ra-02 +3.3V 电源的并联储能与宽带去耦 | 图 2864e140e987 / 第 1 页 / 页面中央左侧 C1-C5 均并联在 +3.3V 与 GND 之间，数值依次 100uF/1uF/100nF/10nF/1nF |
| C6,C7,R6 | 1uF; 1uF; 100KΩ | U1 输入/输出滤波与使能上拉网络 | 图 2864e140e987 / 第 1 页 / 页面左下 U1 周围 C6 1uF 接 +5V、C7 1uF 接 +3.3V、R6 100KΩ 从 +5V 接 EN pin 3 |
| R7,R8,R9 | NC; NC; NC | 独立画出的 433M、868M、915M 未装配置电阻位置，连接关系未显示 | 图 2864e140e987 / 第 1 页 / 页面右下 R7/R8/R9 均标 NC，右侧文字分别为 433M、868M、915M，端点未连接 |

## 系统结构

### Module LoRa433 v1.1 系统架构

Ra-02 Module 通过固定 SPI 与 J1 M5Stack_BUS 通信，S1 DIP-8 选择 RST/IRQ/NSS GPIO，U1 RT9013_3.3V 从 +5V 生成 +3.3V；射频区提供 SMA 与 IPEX 选配元件位置。

- 参数与网络：`radio_module=Ra-02 Module`；`host_bus=J1 M5Stack_BUS`；`bus=SPI`；`selector=S1 SW DIP-8`；`regulator=U1 RT9013_3.3V`；`antenna_options=E2 ANT_SMA,E1 ANT_IPEX`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页：中央 Ra-02、右侧 J1、下方 U1/S1、左上 E1/E2

## 核心器件

### Ra-02 Module 引脚

Ra-02 pin 1 为未标名射频端，pin 2 GND、3 3V3、4 RESET、5 DIO0、6 DIO1、7 DIO2、8 DIO3、9 GND、10 DIO4、11 DIO5、12 SCK、13 MISO、14 MOSI、15 NSS、16 GND。RESET、DIO0、SCK、MISO、MOSI、NSS 与电源地已连接；DIO1-DIO5 带未连接标记。

- 参数与网络：`reference=Ra-02 Module`；`pins_1_8=1:unnamed RF,2:GND,3:3V3,4:RESET,5:DIO0,6:DIO1,7:DIO2,8:DIO3`；`pins_9_16=9:GND,10:DIO4,11:DIO5,12:SCK,13:MISO,14:MOSI,15:NSS,16:GND`；`unconnected_dio=DIO1 pin 6,DIO2 pin 7,DIO3 pin 8,DIO4 pin 10,DIO5 pin 11`
- 证据：图 2864e140e987 / 第 1 页 / 页面中央 Ra-02 Module pin 1-16 的名称、连线及 pin 6-8/10-11 红色未连接标记

## 电源

### +5V 至 +3.3V 稳压

J1 pin 28 的 +5V 连接 U1 pin 1/VIN，并经 R6 100KΩ 上拉 U1 pin 3/EN；U1 pin 5/VOUT 输出 +3.3V，pin 2/GND 接地，pin 4/NC 带未连接标记。C6 1uF 与 C7 1uF 分别为输入、输出滤波。

- 参数与网络：`input=J1 pin 28/+5V`；`regulator=U1 RT9013_3.3V`；`vin=pin 1`；`enable=pin 3 via R6 100KΩ to +5V`；`output=pin 5/+3.3V`；`ground=pin 2`；`input_cap=C6 1uF`；`output_cap=C7 1uF`；`nc=pin 4`
- 证据：图 2864e140e987 / 第 1 页 / 页面左下 +5V-C6-U1-R6-C7-+3.3V 电源链与右侧 J1 pin 28/+5V

### Ra-02 +3.3V 供电与去耦

+3.3V 直接连接 Ra-02 pin 3/3V3；C1 100uF、C2 1uF、C3 100nF、C4 10nF、C5 1nF 并联在 +3.3V 与 GND 之间。Ra-02 pin 2、9、16 接 GND。

- 参数与网络：`rail=+3.3V`；`module_pin=Ra-02 pin 3/3V3`；`ground_pins=2,9,16`；`decoupling=C1 100uF,C2 1uF,C3 100nF,C4 10nF,C5 1nF`
- 证据：图 2864e140e987 / 第 1 页 / 页面中央左侧 +3.3V/C1-C5 与 Ra-02 pin 2/3/9/16 电源地连接

### J1 M5Stack_BUS 电源针脚

J1 pin 1、3、5 接 GND，pin 12 标 +3.3V，pin 25、27、29 标 HPWR，pin 28 接 +5V，pin 30 标 BATTERY；本页只显示 +5V 网络连接 U1，HPWR、BATTERY 与 J1 +3.3V 未连接到其他电路。

- 参数与网络：`ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY`；`used_input=+5V -> U1`
- 证据：图 2864e140e987 / 第 1 页 / 页面右侧 J1 pin 1-5、12、25-30 与 +5V 外部网络

## 接口

### J1 M5Stack_BUS 完整针脚

J1 奇数针为 1 GND、3 GND、5 GND、7 GPIO23、9 GPIO19、11 GPIO18、13 GPIO3、15 GPIO16、17 GPIO21、19 GPIO2、21 GPIO12、23 GPIO15、25 HPWR、27 HPWR、29 HPWR；偶数针为 2 GPIO35、4 GPIO36、6 EN、8 GPIO25、10 GPIO26、12 +3.3V、14 GPIO1、16 GPIO17、18 GPIO22、20 GPIO5、22 GPIO13、24 GPIO0、26 GPIO34、28 +5V、30 BATTERY。

- 参数与网络：`reference=J1 M5Stack_BUS`；`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY`
- 证据：图 2864e140e987 / 第 1 页 / 页面右侧 J1 M5Stack_BUS 内部 pin 1-30 与网络名

## 总线

### Ra-02 固定 SPI 信号

Ra-02 pin 14/MOSI 通过 MOSI 网络连接 J1 pin 7/GPIO23；pin 13/MISO 通过 MISO 网络连接 J1 pin 9/GPIO19；pin 12/SCK 通过 SCK 网络连接 J1 pin 11/GPIO18。

- 参数与网络：`controller=M5Stack host via J1`；`device=Ra-02 Module`；`mosi=J1 pin 7/GPIO23 -> MOSI -> Ra-02 pin 14`；`miso=Ra-02 pin 13 -> MISO -> J1 pin 9/GPIO19`；`sck=J1 pin 11/GPIO18 -> SCK -> Ra-02 pin 12`；`level=+3.3V module rail`
- 证据：图 2864e140e987 / 第 1 页 / 页面 Ra-02 右侧 MOSI/MISO/SCK 网络与 J1 左侧 pin 7/9/11

### SPI NSS 片选路由

Ra-02 pin 15/NSS 连接 NSS 网络；S1 pin 13、14、15、16 共接 NSS，分别可通过开关连接 pin 4/GPIO0、3/GPIO15、2/GPIO12、1/GPIO5，对应 J1 pin 24、23、21、20。

- 参数与网络：`device_nss=Ra-02 pin 15/NSS`；`selector=S1 SW DIP-8`；`routes=13-4:GPIO0/J1 pin 24,14-3:GPIO15/J1 pin 23,15-2:GPIO12/J1 pin 21,16-1:GPIO5/J1 pin 20`
- 证据：图 2864e140e987 / 第 1 页 / 页面 Ra-02 pin 15/NSS 与下方 S1 pin 13-16 NSS 母线及 GPIO0/GPIO15/GPIO12/GPIO5

## 总线地址

### SPI 地址可见性

Ra-02 使用 NSS 片选而非原理图可见的数值设备地址；页面没有 I2C、UART、CAN 或其他带地址外设。

- 参数与网络：`spi_chip_select=NSS via S1`；`numeric_address_visible=false`；`i2c_visible=false`；`uart_visible=false`；`can_visible=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页 SPI MOSI/MISO/SCK/NSS 与所有器件，无设备地址字段

## GPIO 与控制信号

### Ra-02 DIO0 中断路由

Ra-02 pin 5/DIO0 连接 IRQ 网络；S1 pin 11、12 共接 IRQ，分别可通过开关连接 pin 6/GPIO35 与 pin 5/GPIO34，对应 J1 pin 2 与 pin 26。

- 参数与网络：`module_irq=Ra-02 pin 5/DIO0 -> IRQ`；`routes=S1 11-6:GPIO35/J1 pin 2,S1 12-5:GPIO34/J1 pin 26`；`direction=Ra-02 DIO0 output to host GPIO`
- 证据：图 2864e140e987 / 第 1 页 / 页面 Ra-02 左侧 DIO0/IRQ 与 S1 中间两位 IRQ-GPIO35/GPIO34

### 未使用的 Ra-02 DIO1-DIO5

Ra-02 pin 6/DIO1、7/DIO2、8/DIO3、10/DIO4、11/DIO5 均带未连接标记，没有引至 J1 或其他器件。

- 参数与网络：`dio1=pin 6 NC`；`dio2=pin 7 NC`；`dio3=pin 8 NC`；`dio4=pin 10 NC`；`dio5=pin 11 NC`
- 证据：图 2864e140e987 / 第 1 页 / 页面 Ra-02 左下 pin 6-8 与右下 pin 10-11 的红色未连接叉号

## 时钟

### 时钟源可见性

单页原理图未绘出独立晶体、谐振器或振荡器；Ra-02 内部射频时钟未展开。

- 参数与网络：`external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页无 Y/X 晶体、谐振器或振荡器位号

## 复位

### Ra-02 RESET 路由

Ra-02 pin 4/RESET 连接 RST 网络；S1 pin 9、10 共接 RST，分别可通过开关连接 pin 8/GPIO25 与 pin 7/GPIO13，对应 J1 pin 8 与 pin 22。图中没有复位按键、上拉或 RC 网络。

- 参数与网络：`module_reset=Ra-02 pin 4/RESET -> RST`；`routes=S1 9-8:GPIO25/J1 pin 8,S1 10-7:GPIO13/J1 pin 22`；`reset_button_visible=false`；`pullup_visible=false`；`rc_visible=false`
- 证据：图 2864e140e987 / 第 1 页 / 页面 Ra-02 左侧 RESET/RST 与 S1 上两位 RST-GPIO25/GPIO13

## 保护电路

### 电源、总线与天线保护可见性

单页原理图未绘出保险丝、TVS、ESD、反接保护或浪涌保护器件；J1、SPI 和 E1/E2 天线接口周围没有专用保护位号。

- 参数与网络：`fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_polarity_visible=false`；`antenna_protection_visible=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页电源、M5-Bus、SPI 与射频接口外围

## 内存与 Flash

### 存储器与内存可见性

原理图没有独立 Flash、EEPROM、RAM、SD 卡或其他存储器件；Ra-02 内部存储结构未展开。

- 参数与网络：`external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页全部器件，无存储器或存储连接器位号

## 调试与烧录

### 调试与 BOOT 接口可见性

原理图未绘出 SWD、JTAG、UART 调试排针、BOOT 开关或专用测试连接器。

- 参数与网络：`swd_visible=false`；`jtag_visible=false`；`debug_uart_visible=false`；`boot_switch_visible=false`；`test_header_visible=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页全部器件与连接器，无调试或 BOOT 标注

## 其他事实

### 音频、传感器与其他接口可见性

原理图未绘出音频器件、传感器、模拟采样前端、UART、I2C、CAN、RS-485、USB、SDIO、MIPI 或 I2S 电路。

- 参数与网络：`audio_visible=false`；`sensor_visible=false`；`analog_frontend_visible=false`；`uart_visible=false`；`i2c_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`
- 证据：图 2864e140e987 / 第 1 页 / 完整单页功能分区仅含 LoRa、SPI、电源、天线与 M5-Bus

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module LoRa433 v1.1 系统架构 | `radio_module=Ra-02 Module`；`host_bus=J1 M5Stack_BUS`；`bus=SPI`；`selector=S1 SW DIP-8`；`regulator=U1 RT9013_3.3V`；`antenna_options=E2 ANT_SMA,E1 ANT_IPEX` |
| 核心器件 | Ra-02 Module 引脚 | `reference=Ra-02 Module`；`pins_1_8=1:unnamed RF,2:GND,3:3V3,4:RESET,5:DIO0,6:DIO1,7:DIO2,8:DIO3`；`pins_9_16=9:GND,10:DIO4,11:DIO5,12:SCK,13:MISO,14:MOSI,15:NSS,16:GND`；`unconnected_dio=DIO1 pin 6,DIO2 pin 7,DIO3 pin 8,DIO4 pin 10,DIO5 pin 11` |
| 核心器件 | Ra-02 内部射频芯片 | `documented_chip=SX1278`；`schematic_module=Ra-02 Module`；`internal_chip_visible=false` |
| 电源 | +5V 至 +3.3V 稳压 | `input=J1 pin 28/+5V`；`regulator=U1 RT9013_3.3V`；`vin=pin 1`；`enable=pin 3 via R6 100KΩ to +5V`；`output=pin 5/+3.3V`；`ground=pin 2`；`input_cap=C6 1uF`；`output_cap=C7 1uF`；`nc=pin 4` |
| 电源 | Ra-02 +3.3V 供电与去耦 | `rail=+3.3V`；`module_pin=Ra-02 pin 3/3V3`；`ground_pins=2,9,16`；`decoupling=C1 100uF,C2 1uF,C3 100nF,C4 10nF,C5 1nF` |
| 电源 | J1 M5Stack_BUS 电源针脚 | `ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY`；`used_input=+5V -> U1` |
| 接口 | J1 M5Stack_BUS 完整针脚 | `reference=J1 M5Stack_BUS`；`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY` |
| 总线 | Ra-02 固定 SPI 信号 | `controller=M5Stack host via J1`；`device=Ra-02 Module`；`mosi=J1 pin 7/GPIO23 -> MOSI -> Ra-02 pin 14`；`miso=Ra-02 pin 13 -> MISO -> J1 pin 9/GPIO19`；`sck=J1 pin 11/GPIO18 -> SCK -> Ra-02 pin 12`；`level=+3.3V module rail` |
| 总线 | SPI NSS 片选路由 | `device_nss=Ra-02 pin 15/NSS`；`selector=S1 SW DIP-8`；`routes=13-4:GPIO0/J1 pin 24,14-3:GPIO15/J1 pin 23,15-2:GPIO12/J1 pin 21,16-1:GPIO5/J1 pin 20` |
| 复位 | Ra-02 RESET 路由 | `module_reset=Ra-02 pin 4/RESET -> RST`；`routes=S1 9-8:GPIO25/J1 pin 8,S1 10-7:GPIO13/J1 pin 22`；`reset_button_visible=false`；`pullup_visible=false`；`rc_visible=false` |
| GPIO 与控制信号 | Ra-02 DIO0 中断路由 | `module_irq=Ra-02 pin 5/DIO0 -> IRQ`；`routes=S1 11-6:GPIO35/J1 pin 2,S1 12-5:GPIO34/J1 pin 26`；`direction=Ra-02 DIO0 output to host GPIO` |
| GPIO 与控制信号 | 未使用的 Ra-02 DIO1-DIO5 | `dio1=pin 6 NC`；`dio2=pin 7 NC`；`dio3=pin 8 NC`；`dio4=pin 10 NC`；`dio5=pin 11 NC` |
| 射频 | SMA 与 IPEX 天线选配 | `sma=E2 ANT_SMA + R1 0Ω`；`ipex=E1 ANT_IPEX + R2 NC`；`ipex_shunts=C8 NC,C9 NC`；`radio_rf_pin=Ra-02 pin 1 unnamed`；`r1_to_radio_trace_clear=false` |
| 射频 | LoRa 工作频段 | `documented_range=410MHz~525MHz`；`documented_product_frequency=433MHz`；`schematic_markers=R7 NC/433M,R8 NC/868M,R9 NC/915M`；`confirmed_frequency=null` |
| 核心器件 | R7/R8/R9 频段标记电阻用途 | `r7=NC, label 433M`；`r8=NC, label 868M`；`r9=NC, label 915M`；`connections_visible=false`；`purpose_confirmed=false` |
| 总线地址 | SPI 地址可见性 | `spi_chip_select=NSS via S1`；`numeric_address_visible=false`；`i2c_visible=false`；`uart_visible=false`；`can_visible=false` |
| 时钟 | 时钟源可见性 | `external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false` |
| 保护电路 | 电源、总线与天线保护可见性 | `fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_polarity_visible=false`；`antenna_protection_visible=false` |
| 调试与烧录 | 调试与 BOOT 接口可见性 | `swd_visible=false`；`jtag_visible=false`；`debug_uart_visible=false`；`boot_switch_visible=false`；`test_header_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false` |
| 其他事实 | 音频、传感器与其他接口可见性 | `audio_visible=false`；`sensor_visible=false`；`analog_frontend_visible=false`；`uart_visible=false`；`i2c_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false` |

## 待确认事项

- `component.internal-radio`：产品正文将 Ra-02 内部芯片写为 SX1278，但原理图只显示完整 Ra-02 Module，没有 SX1278 的独立位号、供电、时钟或内部射频连接。（证据：图 2864e140e987 / 第 1 页 / 页面中央仅标 Ra-02 Module，未出现 SX1278 位号）
- `rf.antenna-population`：E2 标 ANT_SMA，其信号端串联 R1 0Ω；E1 标 ANT_IPEX，其信号端经 R2（NC）连接射频节点，C8、C9（均 NC）分别位于 R2 两侧对地。元件值显示 SMA 支路装 0Ω、IPEX π 网络默认不装，但该栅格页未清晰显示 R1 右端到 Ra-02 pin 1 的连续连线。（证据：图 2864e140e987 / 第 1 页 / 页面左上 E2/R1 与 E1/R2/C8/C9 射频区，以及 Ra-02 pin 1；R1 右端连接在栅格图中不可连续追踪）
- `rf.documented-band`：产品正文记载工作频率范围为 410MHz~525MHz，并以 433MHz 为产品频点；原理图仅在独立未连接位置标出 R7/433M、R8/868M、R9/915M，未打印 Ra-02 的已配置频率范围。（证据：图 2864e140e987 / 第 1 页 / 页面右下 R7/R8/R9 独立 NC 符号及 433M/868M/915M 文字，无连接到 Ra-02）
- `component.band-marker-purpose`：R7、R8、R9 均标 NC，旁边分别标 433M、868M、915M，但两端均未连接；仅凭本页不能确定它们是 BOM 变体标识、装配选项还是其他用途。（证据：图 2864e140e987 / 第 1 页 / 页面右下三个孤立电阻符号 R7/R8/R9 与频段文字）
- `review.internal-radio`：Ra-02 Module 内部射频芯片是否确认为产品正文记载的 SX1278？；原因：本地原理图只显示 Ra-02 模组边界，没有展开内部芯片位号或连接。
- `review.antenna-population`：当前 v1.1 PCB 的默认 SMA 天线支路如何从 R1 0Ω 连到 Ra-02 pin 1，IPEX 支路是否仅为未装选项？；原因：栅格原理图显示 R1=0Ω、R2/C8/C9=NC，但 R1 右端到模组 RF 节点的连续连线不清晰。
- `review.documented-band`：Module LoRa433 v1.1 的正式工作频率范围是否确认为 410MHz~525MHz，默认中心频点是否为 433MHz？；原因：频率范围来自产品正文；原理图只显示未连接的 433M/868M/915M 标记，未给出 Ra-02 配置参数。
- `review.band-marker-purpose`：R7/R8/R9 的 433M、868M、915M 未装电阻位置在设计和 BOM 中承担什么用途？；原因：三个位号在本页两端均未连接，无法由原理图确认其控制或标识关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2864e140e9871076a7bb825506bce08efe77a12e0dc2a743bd159fa16cc1fb3f` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/%E5%8E%9F%E7%90%86%E5%9B%BE1.png` |

---

源文档：`zh_CN/module/Module-LoRa433_V1.1.md`

源文档 SHA-256：`a14a5f26c5c2f1a73f3e5b47dae9c86b10db68d63c163514d672de580a76a5ee`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
