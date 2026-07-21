# Module CC1101 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module CC1101 |
| SKU | M146 |
| 产品 ID | `module-cc1101-7382c678b783` |
| 源文档 | `zh_CN/module/Module_CC1101.md` |

## 概述

Module CC1101 以 U2 E07-900M10S 射频模组为核心，MOSI/MISO/SCK 固定连接 J1 M5Stack_BUS 的 GPIO23/GPIO19/GPIO18，SW1 DIP-4 将 CSN 选择到 GPIO25/GPIO15/GPIO12/GPIO0，SW2 DIP-6 将 GD00 与 GD02 分别选择到 GPIO35/GPIO13/GPIO5。J1 pin 28 的 +5V 经 U1 VRH3301NLX 转换为 +3.3V，再通过 FB1 供给 U2 VCC。原理图在 U2 下方打印 868MHz，但没有展开内部 CC1101、外部 SMA 连接器、内部时钟或 FIFO。

## 检索关键词

`Module CC1101`、`M146`、`E07-900M10S`、`CC1101`、`868MHz`、`855~925MHz`、`Sub-1 GHz`、`SPI`、`MOSI`、`MISO`、`SCK`、`CSN`、`GD00`、`GD01`、`GD02`、`SW1 DIP-4`、`SW2 DIP-6`、`M5Stack_BUS`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO25`、`GPIO15`、`GPIO12`、`GPIO0`、`GPIO35`、`GPIO13`、`GPIO5`、`VRH3301NLX`、`+5V`、`+3.3V`、`FB1 120Ω/MB`、`ANT`、`2-FSK`、`4-FSK`、`GFSK`、`MSK`、`ASK`、`OOK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | E07-900M10S | Sub-1 GHz 射频通信模组，提供 SPI、GD00/GD01/GD02 与 ANT 引脚 | 图 a58d1487433a / 第 1 页 / 页面 C1-C2 U2 E07-900M10S，pin 1-22 标注 GND、VCC、NC、CSN、SCK、MOSI、MISO/GD01、GD00、GD02、ANT |
| U1 | VRH3301NLX | +5V 至 +3.3V 的稳压器 | 图 a58d1487433a / 第 1 页 / 页面 A1 U1 VRH3301NLX，VIN pin 4 与 EN pin 3 接 +5V，VOUT pin 1 输出 +3.3V |
| SW1 | SW DIP-4 | CSN 到 GPIO25/GPIO15/GPIO12/GPIO0 的片选路由开关 | 图 a58d1487433a / 第 1 页 / 页面 B2-B3 SW1 SW DIP-4，左侧 pin 5-8 共接 CSN，右侧 pin 1-4 分别接 GPIO25/GPIO15/GPIO12/GPIO0 |
| SW2 | SW DIP-6 | GD02 与 GD00 到 GPIO35/GPIO13/GPIO5 的中断/通用数字路由开关 | 图 a58d1487433a / 第 1 页 / 页面 C2-C3 SW2 SW DIP-6，pin 10-12 共接 GD02、pin 7-9 共接 GD00，右侧两组三路 GPIO35/GPIO13/GPIO5 |
| J1 | M5Stack_BUS | 30 针主机堆叠接口，提供 SPI、可选控制 GPIO、HPWR、+5V 和 BATTERY | 图 a58d1487433a / 第 1 页 / 页面 B3-C4 J1 M5Stack_BUS，pin 1-30 网络名完整可见 |
| FB1 | 120Ω/MB | +3.3V 到 U2 VCC 的电源磁珠滤波 | 图 a58d1487433a / 第 1 页 / 页面 C1 U2 左侧 FB1 120Ω/MB，连接 +3.3V 与 U2 pin 9/VCC |
| C1,C2,C3,C4 | 22uF; 100nF; 22uF; 100nF | U1 +5V 输入与 +3.3V 输出的去耦和储能 | 图 a58d1487433a / 第 1 页 / 页面 A1 U1 两侧 C1/C2 接 +5V，C3/C4 接 +3.3V，均回到 GND |
| C5,C6 | 22uF; 100nF | FB1 后 U2 VCC 电源去耦 | 图 a58d1487433a / 第 1 页 / 页面 C1 FB1 后 VCC 节点的 C5 22uF 与 C6 100nF 到 GND |
| R1 | 10KΩ | GPIO0 到 +3.3V 的上拉电阻 | 图 a58d1487433a / 第 1 页 / 页面 B3 SW1 pin 4/GPIO0 网络经 R1 10K 接 +3.3V |

## 系统结构

### Module CC1101 系统架构

单页原理图由 U2 E07-900M10S 射频模组、U1 VRH3301NLX 3.3V 电源、SW1/SW2 GPIO 选择开关和 J1 M5Stack_BUS 构成；主机通过 SPI 与 U2 通信。

- 参数与网络：`radio_module=U2 E07-900M10S`；`power=U1 VRH3301NLX`；`host_bus=J1 M5Stack_BUS`；`bus=SPI`；`selectors=SW1 CSN,SW2 GD00/GD02`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页 A1-C4：U1、U2、SW1、SW2、J1

## 核心器件

### U2 E07-900M10S 引脚

U2 pin 1-5 为 GND，pin 6-8 为 NC，pin 9 VCC，pin 10 NC，pin 11 GND，pin 12 GND，pin 13 NC，pin 14 GD02，pin 15 GD00，pin 16 MISO/GD01，pin 17 MOSI，pin 18 SCK，pin 19 CSN，pin 20 GND，pin 21 ANT，pin 22 GND。

- 参数与网络：`reference=U2`；`part_number=E07-900M10S`；`pins_1_11=1:GND,2:GND,3:GND,4:GND,5:GND,6:NC,7:NC,8:NC,9:VCC,10:NC,11:GND`；`pins_12_22=12:GND,13:NC,14:GD02,15:GD00,16:MISO/GD01,17:MOSI,18:SCK,19:CSN,20:GND,21:ANT,22:GND`
- 证据：图 a58d1487433a / 第 1 页 / 页面 C1-C2 U2 方框左右 pin 1-22 名称与编号

## 电源

### +5V 至 +3.3V 稳压

J1 pin 28 引出 +5V；U1 pin 4/VIN 与 pin 3/EN 接 +5V，pin 1/VOUT 输出 +3.3V，pin 2/5 VSS 接 GND。C1 22uF、C2 100nF 位于输入侧，C3 22uF、C4 100nF 位于输出侧。

- 参数与网络：`input=J1 pin 28/+5V`；`regulator=U1 VRH3301NLX`；`vin=pin 4/+5V`；`enable=pin 3/+5V`；`output=pin 1/+3.3V`；`ground=pins 2,5/VSS`；`input_caps=C1 22uF,C2 100nF`；`output_caps=C3 22uF,C4 100nF`
- 证据：图 a58d1487433a / 第 1 页 / 页面 A1 U1/C1-C4 与 C4 J1 pin 28/+5V 同名网络

### U2 VCC 滤波供电

+3.3V 经 FB1 120Ω/MB 连接 U2 pin 9/VCC，FB1 后由 C5 22uF 与 C6 100nF 并联到 GND；U2 的多个 GND 引脚接系统地。

- 参数与网络：`source=+3.3V`；`filter=FB1 120Ω/MB`；`load=U2 pin 9/VCC`；`decoupling=C5 22uF,C6 100nF`；`ground_pins=1,2,3,4,5,11,12,20,22`
- 证据：图 a58d1487433a / 第 1 页 / 页面 C1 U2 VCC/FB1/C5/C6 与 U2 GND 引脚

### J1 M5Stack_BUS 电源针脚

J1 pin 1、3、5 为 GND，pin 12 为 +3.3V，pin 25、27、29 共接 HPWR，pin 28 接 +5V，pin 30 标 BATTERY 并引出 BAT；本页仅 +5V 参与 U1 稳压。

- 参数与网络：`ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY -> BAT`；`used_supply=+5V -> U1`
- 证据：图 a58d1487433a / 第 1 页 / 页面 B3-C4 J1 顶部 GND、中部 +3.3V、底部 HPWR/+5V/BATTERY

## 接口

### J1 M5Stack_BUS 完整针脚

J1 奇数针为 1 GND、3 GND、5 GND、7 GPIO23、9 GPIO19、11 GPIO18、13 GPIO3、15 GPIO16、17 GPIO21、19 GPIO2、21 GPIO12、23 GPIO15、25 HPWR、27 HPWR、29 HPWR；偶数针为 2 GPIO35、4 GPIO36、6 EN、8 GPIO25、10 GPIO26、12 +3.3V、14 GPIO1、16 GPIO17、18 GPIO22、20 GPIO5、22 GPIO13、24 GPIO0、26 GPIO34、28 +5V、30 BATTERY。

- 参数与网络：`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY`
- 证据：图 a58d1487433a / 第 1 页 / 页面 B3-C4 J1 M5Stack_BUS 内部 pin 1-30 与网络名

## 总线

### 固定 SPI 数据与时钟

U2 pin 17/MOSI 连接 J1 pin 7/GPIO23，pin 16/MISO/GD01 连接 J1 pin 9/GPIO19，pin 18/SCK 连接 J1 pin 11/GPIO18。主机为 SPI 控制器，U2 为 SPI 设备。

- 参数与网络：`controller=M5Stack host`；`device=U2 E07-900M10S`；`mosi=J1 pin 7/GPIO23 -> U2 pin 17/MOSI`；`miso=U2 pin 16/MISO/GD01 -> J1 pin 9/GPIO19`；`sck=J1 pin 11/GPIO18 -> U2 pin 18/SCK`；`level=+3.3V`
- 证据：图 a58d1487433a / 第 1 页 / 页面 U2 右侧 MOSI/MISO/SCK 网络与 J1 pin 7/9/11

### SW1 SPI CSN 路由

U2 pin 19/CSN 连接 SW1 pin 5、6、7、8 公共侧；四个开关分别连接 pin 1/GPIO25、pin 2/GPIO15、pin 3/GPIO12、pin 4/GPIO0，对应 J1 pin 8、23、21、24。

- 参数与网络：`device_csn=U2 pin 19/CSN`；`selector=SW1 SW DIP-4`；`routes=8-1:GPIO25/J1 pin 8,7-2:GPIO15/J1 pin 23,6-3:GPIO12/J1 pin 21,5-4:GPIO0/J1 pin 24`
- 证据：图 a58d1487433a / 第 1 页 / 页面 B2-B3 U2 CSN、SW1 pin 1-8 与 J1 选用 GPIO

## 总线地址

### SPI 地址可见性

U2 由 CSN 片选，不使用原理图可见的数值设备地址；页面没有 I2C、UART 或其他带地址外设。

- 参数与网络：`chip_select=CSN via SW1`；`numeric_address_visible=false`；`i2c_visible=false`；`uart_visible=false`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页 SPI 与所有外设，无十六进制地址

## GPIO 与控制信号

### SW2 GD02 路由

U2 pin 14/GD02 连接 SW2 pin 10、11、12 公共侧，可分别选择 pin 1/GPIO35、pin 2/GPIO13、pin 3/GPIO5，对应 J1 pin 2、22、20。

- 参数与网络：`source=U2 pin 14/GD02`；`selector=SW2 SW DIP-6`；`routes=12-1:GPIO35/J1 pin 2,11-2:GPIO13/J1 pin 22,10-3:GPIO5/J1 pin 20`
- 证据：图 a58d1487433a / 第 1 页 / 页面 C2-C3 SW2 上三位 GD02-GPIO35/GPIO13/GPIO5

### SW2 GD00 路由

U2 pin 15/GD00 连接 SW2 pin 7、8、9 公共侧，可分别选择 pin 4/GPIO35、pin 5/GPIO13、pin 6/GPIO5，对应 J1 pin 2、22、20；GD00 与 GD02 使用相同三组候选 GPIO。

- 参数与网络：`source=U2 pin 15/GD00`；`selector=SW2 SW DIP-6`；`routes=9-4:GPIO35/J1 pin 2,8-5:GPIO13/J1 pin 22,7-6:GPIO5/J1 pin 20`；`shared_candidates=GPIO35,GPIO13,GPIO5`
- 证据：图 a58d1487433a / 第 1 页 / 页面 C2-C3 SW2 下三位 GD00-GPIO35/GPIO13/GPIO5

### GPIO0 上拉

SW1 pin 4 的 GPIO0 网络经 R1 10KΩ 上拉到 +3.3V；该网络同时连接 J1 pin 24。

- 参数与网络：`net=GPIO0`；`pullup=R1 10KΩ to +3.3V`；`bus_pin=J1 pin 24`；`switch_pin=SW1 pin 4`
- 证据：图 a58d1487433a / 第 1 页 / 页面 B3 SW1 GPIO0 线与 R1 10K/+3.3V

## 时钟

### 时钟源可见性

单页原理图没有独立晶体、谐振器或振荡器；E07-900M10S 内部 CC1101 时钟未展开。

- 参数与网络：`external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页无 Y/X 时钟器件位号

## 保护电路

### 电源与接口保护可见性

单页原理图未绘出保险丝、TVS、ESD、反接保护或浪涌保护器件；+5V、M5-Bus 和 ANT 周围也没有专用保护位号。

- 参数与网络：`fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`antenna_protection_visible=false`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页电源、总线和射频接口外围

## 射频

### 原理图频点标记

U2 E07-900M10S 模组下方明确打印 868MHz；本页没有其他频率选择电阻、滤波器值或区域配置网络。

- 参数与网络：`module=U2 E07-900M10S`；`printed_frequency=868MHz`；`frequency_selector_visible=false`
- 证据：图 a58d1487433a / 第 1 页 / 页面 C1-C2 U2 下方蓝色 868MHz 文字

## 调试与烧录

### 复位、BOOT 与调试接口可见性

单页原理图没有 U2 复位网络、BOOT 开关、SWD/JTAG 或专用调试连接器。

- 参数与网络：`module_reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`；`debug_connector_visible=false`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页 U2、开关与 J1 接口，无 RESET/BOOT/SWD/JTAG 标注

## 其他事实

### 其他功能分区可见性

原理图未绘出独立外部存储器、音频器件、传感器、模拟采样、UART、I2C、CAN、RS-485、USB、SDIO、MIPI 或 I2S 电路。

- 参数与网络：`external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_visible=false`；`uart_visible=false`；`i2c_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`
- 证据：图 a58d1487433a / 第 1 页 / 完整单页功能分区仅含射频模组、电源、SPI、GPIO 选择与 M5-Bus

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module CC1101 系统架构 | `radio_module=U2 E07-900M10S`；`power=U1 VRH3301NLX`；`host_bus=J1 M5Stack_BUS`；`bus=SPI`；`selectors=SW1 CSN,SW2 GD00/GD02` |
| 核心器件 | U2 E07-900M10S 引脚 | `reference=U2`；`part_number=E07-900M10S`；`pins_1_11=1:GND,2:GND,3:GND,4:GND,5:GND,6:NC,7:NC,8:NC,9:VCC,10:NC,11:GND`；`pins_12_22=12:GND,13:NC,14:GD02,15:GD00,16:MISO/GD01,17:MOSI,18:SCK,19:CSN,20:GND,21:ANT,22:GND` |
| 核心器件 | E07-900M10S 内部收发器 | `documented_chip=CC1101`；`schematic_module=U2 E07-900M10S`；`internal_chip_visible=false` |
| 电源 | +5V 至 +3.3V 稳压 | `input=J1 pin 28/+5V`；`regulator=U1 VRH3301NLX`；`vin=pin 4/+5V`；`enable=pin 3/+5V`；`output=pin 1/+3.3V`；`ground=pins 2,5/VSS`；`input_caps=C1 22uF,C2 100nF`；`output_caps=C3 22uF,C4 100nF` |
| 电源 | U2 VCC 滤波供电 | `source=+3.3V`；`filter=FB1 120Ω/MB`；`load=U2 pin 9/VCC`；`decoupling=C5 22uF,C6 100nF`；`ground_pins=1,2,3,4,5,11,12,20,22` |
| 电源 | J1 M5Stack_BUS 电源针脚 | `ground_pins=1,3,5`；`three3_pin=12:+3.3V`；`hpwr_pins=25,27,29`；`five_volt_pin=28:+5V`；`battery_pin=30:BATTERY -> BAT`；`used_supply=+5V -> U1` |
| 接口 | J1 M5Stack_BUS 完整针脚 | `odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY` |
| 总线 | 固定 SPI 数据与时钟 | `controller=M5Stack host`；`device=U2 E07-900M10S`；`mosi=J1 pin 7/GPIO23 -> U2 pin 17/MOSI`；`miso=U2 pin 16/MISO/GD01 -> J1 pin 9/GPIO19`；`sck=J1 pin 11/GPIO18 -> U2 pin 18/SCK`；`level=+3.3V` |
| 总线 | SW1 SPI CSN 路由 | `device_csn=U2 pin 19/CSN`；`selector=SW1 SW DIP-4`；`routes=8-1:GPIO25/J1 pin 8,7-2:GPIO15/J1 pin 23,6-3:GPIO12/J1 pin 21,5-4:GPIO0/J1 pin 24` |
| GPIO 与控制信号 | SW2 GD02 路由 | `source=U2 pin 14/GD02`；`selector=SW2 SW DIP-6`；`routes=12-1:GPIO35/J1 pin 2,11-2:GPIO13/J1 pin 22,10-3:GPIO5/J1 pin 20` |
| GPIO 与控制信号 | SW2 GD00 路由 | `source=U2 pin 15/GD00`；`selector=SW2 SW DIP-6`；`routes=9-4:GPIO35/J1 pin 2,8-5:GPIO13/J1 pin 22,7-6:GPIO5/J1 pin 20`；`shared_candidates=GPIO35,GPIO13,GPIO5` |
| GPIO 与控制信号 | GPIO0 上拉 | `net=GPIO0`；`pullup=R1 10KΩ to +3.3V`；`bus_pin=J1 pin 24`；`switch_pin=SW1 pin 4` |
| 射频 | 原理图频点标记 | `module=U2 E07-900M10S`；`printed_frequency=868MHz`；`frequency_selector_visible=false` |
| 射频 | 天线接口可见性 | `module_pin=U2 pin 21/ANT`；`sma_connector_visible=false`；`matching_network_visible=false`；`antenna_protection_visible=false`；`documented_interface=external SMA` |
| 射频 | 射频工作范围与调制能力 | `documented_band=855-925MHz`；`documented_bitrate=0.6-500kbps`；`documented_tx_power=+10dBm`；`documented_modulations=2-FSK,4-FSK,GFSK,MSK,ASK,OOK`；`schematic_value=868MHz` |
| 内存与 Flash | CC1101 内部 RX/TX FIFO | `documented_rx_fifo=64 bytes`；`documented_tx_fifo=64 bytes`；`internal_memory_visible=false` |
| 总线地址 | SPI 地址可见性 | `chip_select=CSN via SW1`；`numeric_address_visible=false`；`i2c_visible=false`；`uart_visible=false` |
| 时钟 | 时钟源可见性 | `external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false` |
| 调试与烧录 | 复位、BOOT 与调试接口可见性 | `module_reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`；`debug_connector_visible=false` |
| 保护电路 | 电源与接口保护可见性 | `fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`antenna_protection_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_visible=false`；`uart_visible=false`；`i2c_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false` |

## 待确认事项

- `component.internal-cc1101`：产品正文记载 U2 内部采用 CC1101，但原理图只显示完整 E07-900M10S 模组，没有 CC1101 的独立位号、供电、晶体或内部射频连接。（证据：图 a58d1487433a / 第 1 页 / 页面 U2 仅标 E07-900M10S，模块内部未展开）
- `rf.antenna-visibility`：U2 pin 21 标 ANT，但单页原理图没有独立 SMA/IPEX 连接器位号、射频匹配网络或天线保护器件；产品正文所述外置 SMA 天线接口无法由该页连接器证据确认。（证据：图 a58d1487433a / 第 1 页 / 页面 U2 pin 21/ANT 与完整单页器件，无 SMA/IPEX 位号）
- `rf.documented-capabilities`：产品正文记载 855-925MHz、0.6-500kbps、+10dBm，并支持 2-FSK/4-FSK/GFSK/MSK/ASK/OOK；原理图仅打印 868MHz，没有这些范围或调制参数。（证据：图 a58d1487433a / 第 1 页 / 页面 U2 与 868MHz 标记，未打印频率范围、速率、功率或调制方式）
- `memory.internal-fifos`：产品正文记载独立 64 字节 RX FIFO 与 TX FIFO，但原理图未展开内部 CC1101 或存储结构，无法从本页确认 FIFO 容量。（证据：图 a58d1487433a / 第 1 页 / 页面 U2 E07-900M10S 模块方框，未展开内部存储）
- `review.internal-cc1101`：U2 E07-900M10S 内部射频收发器是否确认为产品正文记载的 CC1101？；原因：本地原理图只显示 E07-900M10S 模组边界，没有展开内部芯片位号或连接。
- `review.antenna-interface`：产品所述外置 SMA 天线接口位于 E07-900M10S 模组本体还是未包含在当前原理图页的底板部分？；原因：原理图仅显示 U2 pin 21/ANT，没有 SMA/IPEX 连接器、匹配或保护器件位号。
- `review.rf-capabilities`：当前 U2 物料版本的正式频段、速率、发射功率和调制能力是否与产品正文参数完全一致？；原因：本地原理图只打印 868MHz，未打印 855-925MHz、0.6-500kbps、+10dBm 或调制方式。
- `review.internal-fifos`：E07-900M10S 内部 CC1101 的 RX/TX FIFO 是否各为 64 字节？；原因：FIFO 容量来自产品正文，原理图未展开内部存储结构。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a58d1487433a9bc231c7dd890768982253e255f702754f22e578b9bf57013308` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/SCH_Module_CC1101_SCH_Main_V0.1_20241230_2025_07_04_19_47_33_page_01.png` |

---

源文档：`zh_CN/module/Module_CC1101.md`

源文档 SHA-256：`8d4dd871b7a0407bb61476a025d810397652f2516c7e008120ff0521771e9784`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
