# Stamp Cat1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp Cat1 |
| SKU | S004 |
| 产品 ID | `stamp-cat1-ddeb053d5191` |
| 源文档 | `zh_CN/stamp/stamp_cat1.md` |

## 概述

Stamp Cat1 以 M2 SIM-A7680C 蜂窝通信模组为核心，U1 GM9308/HM8089 将 +5V 降压为 +3.8V 供给 M2 VBAT，M2 VDD_EXT 输出 +1.8V。Q1/Q2 SS8050 Y1 与 3.8V/1.8V 上拉网络在外部 NB_RX/NB_TX 和模组 U1_RX/U1_TX 之间进行 UART 电平转换。U2 SIM 卡座连接 USIM_DATA/CLK/RST/VDD，E1 ANT_IPEX 连接 M2 ANT_MAIN，J1 StampCat1_Pin 引出 ANT、NB_TX、NB_RX、GND、3V8 与 5V。

## 检索关键词

`Stamp Cat1`、`S004`、`SIM-A7680C`、`A7680C`、`LTE Cat1`、`GM9308`、`HM8089`、`UART`、`NB_TX`、`NB_RX`、`U1_TX`、`U1_RX`、`+5V`、`+3.8V`、`+1.8V`、`VBAT`、`VDD_EXT`、`USIM_DATA`、`USIM_CLK`、`USIM_RST`、`USIM_VDD`、`SIM_VCC`、`MicroSIM`、`ANT_MAIN`、`ANT_IPEX`、`E1`、`SS8050 Y1`、`LTE-TDD`、`LTE-FDD`、`B34`、`B38`、`B39`、`B40`、`B41`、`B1`、`B3`、`B5`、`B8`、`115200 8N1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M2 | SIM-A7680C | LTE Cat1 蜂窝通信模组，提供 UART、USIM、主天线与未使用的 USB/音频/控制接口 | 图 82e5a4281d94 / 第 1 页 / 页面 B3-D4 M2 SIM-A7680C，pin 1-42 全部名称与连接状态 |
| U1 | GM9308/HM8089 | +5V 至 +3.8V 的降压转换器 | 图 82e5a4281d94 / 第 1 页 / 页面 A1-A2 U1 GM9308/HM8089，VIN/EN/FB/SW/GND 与 L1、R1/R2 |
| L1 | 3015 4.7uH | U1 +3.8V 降压输出电感 | 图 82e5a4281d94 / 第 1 页 / 页面 A1 U1 SW 与 +3.8V 之间 L1 3015 4.7uH |
| Q1,Q2 | SS8050 Y1; SS8050 Y1 | NB_RX/U1_RX 与 NB_TX/U1_TX 的 3.8V/1.8V UART 电平转换 | 图 82e5a4281d94 / 第 1 页 / 页面 C1-C2 Q1/Q2 SS8050 Y1 与 R5-R10、NB_RX/NB_TX/U1_RX/U1_TX |
| U2 | SIM | USIM 卡座，连接 SIM_VCC、RST、CLK、IO 与 GND | 图 82e5a4281d94 / 第 1 页 / 页面 C2-D2 U2 SIM，pin 1 VCC、2 RST、3 CLK、5 GND、6 VPP、7 IO |
| E1 | ANT_IPEX | M2 ANT_MAIN 外部蜂窝天线接口 | 图 82e5a4281d94 / 第 1 页 / 页面 C4 E1 ANT_IPEX，射频端连接 ANT/M2 pin 32 ANT_MAIN，回路接 GND |
| J1 | StampCat1_Pin | 六针 Stamp 主接口，提供 ANT、UART、GND、3V8 和 5V | 图 82e5a4281d94 / 第 1 页 / 页面 A4-B4 J1 StampCat1_Pin，pin 1 ANT、2 NB_TX、3 NB_RX、4 GND、5 3V8、6 5V |
| D1,R3 | 红灯 0603; 1KΩ | +3.8V 电源指示支路 | 图 82e5a4281d94 / 第 1 页 / 页面 A3 +3.8V 经 D1 红灯 0603 与 R3 1KΩ 串联到 GND |

## 系统结构

### Stamp Cat1 系统架构

SIM-A7680C 模组通过电平转换 UART 与外部主机通信，USIM 卡座提供用户卡接口，ANT_MAIN 连接 IPEX 天线，GM9308/HM8089 由 5V 生成 3.8V 模组电源。

- 参数与网络：`cellular_module=M2 SIM-A7680C`；`power_converter=U1 GM9308/HM8089`；`uart_level_shift=Q1,Q2 SS8050 Y1`；`sim=U2 SIM`；`antenna=E1 ANT_IPEX`；`host_connector=J1 StampCat1_Pin`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页 U1/Q1/Q2/U2/M2/E1/J1 分区

## 电源

### U1 +3.8V 降压

U1 pin 4/VIN 与 pin 1/EN 接 +5V，pin 3/SW 经 L1 3015 4.7uH 输出 +3.8V；R1 52.3KΩ 与 R2 10KΩ 构成 FB 分压，C1 100nF/C2 22uF 位于输出，C3 22uF/C4 100nF 位于输入。

- 参数与网络：`input=+5V`；`converter=U1 GM9308/HM8089`；`inductor=L1 3015 4.7uH`；`output=+3.8V`；`feedback=R1 52.3KΩ,R2 10KΩ`；`output_caps=C1 100nF,C2 22uF`；`input_caps=C3 22uF,C4 100nF`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 A1-A2 U1/L1/R1/R2/C1-C4/+5V/+3.8V

### M2 SIM-A7680C 电源

M2 pin 34/35 VBAT 接 +3.8V，pin 40/VDD_EXT 输出 +1.8V；C5 22uF 滤波 +1.8V，C6 10uF 连接 VDD_EXT/PWRKEY 区域至 GND。

- 参数与网络：`main_supply=M2 pins 34,35/VBAT -> +3.8V`；`logic_output=M2 pin 40/VDD_EXT -> +1.8V`；`one8_cap=C5 22uF`；`module_cap=C6 10uF`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 B4-C4 M2 pins 34/35/40 与 C5/C6/+3.8V/+1.8V

## 接口

### J1 StampCat1_Pin 针脚

J1 pin 1 ANT、pin 2 NB_TX、pin 3 NB_RX、pin 4 GND、pin 5 3V8/+3.8V、pin 6 5V/+5V。

- 参数与网络：`pinout=1:ANT,2:NB_TX,3:NB_RX,4:GND,5:3V8/+3.8V,6:5V/+5V`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 A4-B4 J1 StampCat1_Pin pin 1-6

### U2 SIM 卡接口

U2 pin 1/VCC 接 SIM_VCC/USIM_VDD，pin 2/RST 接 USIM_RST，pin 3/CLK 接 USIM_CLK，pin 5/GND 接 GND，pin 6/VPP 未连接，pin 7/IO 接 USIM_DATA；M2 USIM_DET 未连接。

- 参数与网络：`vcc=U2 pin 1 -> SIM_VCC -> M2 pin 19/USIM_VDD`；`rst=U2 pin 2 -> M2 pin 18/USIM_RST`；`clk=U2 pin 3 -> M2 pin 17/USIM_CLK`；`io=U2 pin 7 -> M2 pin 16/USIM_DATA`；`ground=U2 pin 5`；`vpp=pin 6 unconnected`；`detect=M2 pin 15/USIM_DET unconnected`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 C2-D3 U2 SIM 与 M2 pins 15-19

## 总线

### 主 UART 电平转换

M2 pin 1/TXD 连接 U1_TX，pin 2/RXD 连接 U1_RX；Q2/R8-R10 在 NB_TX 与 U1_TX 间转换 3.8V/1.8V 电平，Q1/R5-R7 在 NB_RX 与 U1_RX 间转换，NB_TX/NB_RX 引至 J1 pin 2/3。

- 参数与网络：`module_tx=M2 pin 1/TXD -> U1_TX -> Q2 network -> NB_TX -> J1 pin 2`；`module_rx=M2 pin 2/RXD -> U1_RX -> Q1 network -> NB_RX -> J1 pin 3`；`external_rail=+3.8V`；`module_logic_rail=+1.8V`；`transistors=Q1,Q2 SS8050 Y1`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 C1-C3 Q1/Q2/R5-R10 与 M2 TXD/RXD、J1 NB_TX/NB_RX

### 未使用的 USB 与第三 UART

M2 USB_DN、USB_DP、USB_VBUS、USB_BOOT 以及 U3_RXD/U3_TXD 均未外接，单页没有 USB 连接器或第二主机 UART 接口。

- 参数与网络：`usb=pins 24-26 and 20 unconnected`；`uart3=pins 23/U3_RXD,22/U3_TXD unconnected`；`usb_connector_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 右下 pins 20、22-26 红色未连接标记

## 总线地址

### 总线地址可见性

原理图使用 UART 与 USIM 接口，没有 I2C、SPI 或数值设备地址。

- 参数与网络：`uart_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页所有总线与接口，无设备地址

## GPIO 与控制信号

### 未使用的 M2 控制与状态引脚

M2 RTS、CTS、DCD、DTR、RI、STATUS、NETLIGHT、PWRKEY、ADC、RESET 均未连接；因此本页未显示硬件流控、状态灯、上电按键或复位控制。

- 参数与网络：`uart_flow=pins 3/RTS,4/CTS unconnected`；`modem_status=pins 5/DCD,6/DTR,7/RI unconnected`；`indicators=pins 42/STATUS,41/NETLIGHT unconnected`；`powerkey=pin 39 unconnected`；`adc=pin 38 unconnected`；`reset=pin 29 unconnected`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 左上 pins 3-7 与右上 pins 38-42、pin 29 红色未连接标记

### +3.8V 红色电源灯

+3.8V 经 D1 红灯 0603 与 R3 1KΩ 串联到 GND，形成模组电源指示。

- 参数与网络：`path=+3.8V -> D1 red 0603 -> R3 1KΩ -> GND`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 A3 D1/R3/+3.8V/GND

## 时钟

### 外部时钟可见性

原理图没有独立晶体、谐振器或振荡器；SIM-A7680C 内部时钟未展开。

- 参数与网络：`external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页无 Y/X 时钟器件

## 保护电路

### 电源、UART、USIM 与天线保护可见性

单页原理图未绘出保险丝、TVS、ESD、反接保护或浪涌保护器件；UART、USIM 和 ANT 接口周围没有专用保护位号。

- 参数与网络：`fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`sim_protection_visible=false`；`antenna_protection_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页电源、UART、SIM 与 RF 外围

## 内存与 Flash

### 存储器与内存可见性

原理图没有独立 Flash、EEPROM、RAM、SD 卡或其他存储器；SIM-A7680C 内部存储结构未展开。

- 参数与网络：`external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页全部器件，无存储位号

## 音频

### M2 音频引脚可见性

M2 pin 9/MIC_P、10/MIC_N、11/SPK_P、12/SPK_N 均未连接，原理图没有麦克风、扬声器、编解码器或音频连接器。

- 参数与网络：`mic_p=pin 9 NC`；`mic_n=pin 10 NC`；`spk_p=pin 11 NC`；`spk_n=pin 12 NC`；`audio_peripherals_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 左侧 pins 9-12 红色未连接标记

## 射频

### LTE 主天线路径

M2 pin 32/ANT_MAIN 通过 ANT 网络直接连接 E1 ANT_IPEX 与 J1 pin 1/ANT；相邻 M2 pin 30、31、33 为 GND。图中没有分立匹配、天线开关或射频保护器件。

- 参数与网络：`module_pin=M2 pin 32/ANT_MAIN`；`net=ANT`；`connector=E1 ANT_IPEX`；`stamp_pin=J1 pin 1`；`ground_pins=M2 pins 30,31,33`；`matching_visible=false`；`rf_protection_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 页面 C4 M2 ANT_MAIN/ANT/E1 与 A4 J1 ANT

## 其他事实

### 其他功能分区可见性

原理图未绘出 I2C、SPI、CAN、RS-485、SDIO、MIPI、I2S 或独立传感器/模拟采样电路；核心功能为 LTE 模组、电源、UART 电平转换、SIM 与天线。

- 参数与网络：`i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`rs485_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 82e5a4281d94 / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp Cat1 系统架构 | `cellular_module=M2 SIM-A7680C`；`power_converter=U1 GM9308/HM8089`；`uart_level_shift=Q1,Q2 SS8050 Y1`；`sim=U2 SIM`；`antenna=E1 ANT_IPEX`；`host_connector=J1 StampCat1_Pin` |
| 电源 | U1 +3.8V 降压 | `input=+5V`；`converter=U1 GM9308/HM8089`；`inductor=L1 3015 4.7uH`；`output=+3.8V`；`feedback=R1 52.3KΩ,R2 10KΩ`；`output_caps=C1 100nF,C2 22uF`；`input_caps=C3 22uF,C4 100nF` |
| 电源 | M2 SIM-A7680C 电源 | `main_supply=M2 pins 34,35/VBAT -> +3.8V`；`logic_output=M2 pin 40/VDD_EXT -> +1.8V`；`one8_cap=C5 22uF`；`module_cap=C6 10uF` |
| 总线 | 主 UART 电平转换 | `module_tx=M2 pin 1/TXD -> U1_TX -> Q2 network -> NB_TX -> J1 pin 2`；`module_rx=M2 pin 2/RXD -> U1_RX -> Q1 network -> NB_RX -> J1 pin 3`；`external_rail=+3.8V`；`module_logic_rail=+1.8V`；`transistors=Q1,Q2 SS8050 Y1` |
| 总线 | UART 通讯参数 | `documented_baud=115200`；`documented_frame=8N1`；`schematic_parameters_visible=false` |
| 接口 | J1 StampCat1_Pin 针脚 | `pinout=1:ANT,2:NB_TX,3:NB_RX,4:GND,5:3V8/+3.8V,6:5V/+5V` |
| 接口 | U2 SIM 卡接口 | `vcc=U2 pin 1 -> SIM_VCC -> M2 pin 19/USIM_VDD`；`rst=U2 pin 2 -> M2 pin 18/USIM_RST`；`clk=U2 pin 3 -> M2 pin 17/USIM_CLK`；`io=U2 pin 7 -> M2 pin 16/USIM_DATA`；`ground=U2 pin 5`；`vpp=pin 6 unconnected`；`detect=M2 pin 15/USIM_DET unconnected` |
| 射频 | LTE 主天线路径 | `module_pin=M2 pin 32/ANT_MAIN`；`net=ANT`；`connector=E1 ANT_IPEX`；`stamp_pin=J1 pin 1`；`ground_pins=M2 pins 30,31,33`；`matching_visible=false`；`rf_protection_visible=false` |
| 射频 | LTE 频段与制式 | `documented_tdd=B34,B38,B39,B40,B41`；`documented_fdd=B1,B3,B5,B8`；`schematic_bands_visible=false` |
| 射频 | 蜂窝数据速率 | `documented_downlink=10Mbps`；`documented_uplink=5Mbps`；`schematic_rate_visible=false` |
| GPIO 与控制信号 | 未使用的 M2 控制与状态引脚 | `uart_flow=pins 3/RTS,4/CTS unconnected`；`modem_status=pins 5/DCD,6/DTR,7/RI unconnected`；`indicators=pins 42/STATUS,41/NETLIGHT unconnected`；`powerkey=pin 39 unconnected`；`adc=pin 38 unconnected`；`reset=pin 29 unconnected` |
| 音频 | M2 音频引脚可见性 | `mic_p=pin 9 NC`；`mic_n=pin 10 NC`；`spk_p=pin 11 NC`；`spk_n=pin 12 NC`；`audio_peripherals_visible=false` |
| 总线 | 未使用的 USB 与第三 UART | `usb=pins 24-26 and 20 unconnected`；`uart3=pins 23/U3_RXD,22/U3_TXD unconnected`；`usb_connector_visible=false` |
| GPIO 与控制信号 | +3.8V 红色电源灯 | `path=+3.8V -> D1 red 0603 -> R3 1KΩ -> GND` |
| 总线地址 | 总线地址可见性 | `uart_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false` |
| 时钟 | 外部时钟可见性 | `external_crystal_visible=false`；`external_oscillator_visible=false`；`module_internal_clock_expanded=false` |
| 保护电路 | 电源、UART、USIM 与天线保护可见性 | `fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`sim_protection_visible=false`；`antenna_protection_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`module_internal_memory_expanded=false` |
| 其他事实 | 其他功能分区可见性 | `i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`rs485_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `bus.documented-uart`：产品正文记载 UART 为 115200bps、8N1；原理图只显示 TXD/RXD 与电平转换，没有打印波特率或帧格式。（证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 TXD/RXD 与 Q1/Q2 UART 网络，无通信参数）
- `rf.documented-bands`：产品正文记载 LTE-TDD B34/B38/B39/B40/B41 与 LTE-FDD B1/B3/B5/B8；原理图只显示 SIM-A7680C 型号和 ANT_MAIN，没有打印频段或制式。（证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 SIM-A7680C 与 ANT_MAIN，未打印 LTE band）
- `rf.documented-throughput`：产品正文记载最大下行 10Mbps、上行 5Mbps；原理图未打印网络吞吐率。（证据：图 82e5a4281d94 / 第 1 页 / 页面 M2 SIM-A7680C 模组方框，无 Mbps 参数）
- `review.uart-format`：Stamp Cat1 的默认 UART 是否确认为 115200bps、8N1？；原因：参数来自产品正文，本地原理图没有打印波特率或帧格式。
- `review.lte-bands`：当前 SIM-A7680C 物料正式支持的 LTE-TDD/LTE-FDD 频段是否与产品正文列表完全一致？；原因：原理图未打印频段或区域配置。
- `review.throughput`：Stamp Cat1 的保证最大下行/上行速率是否为 10Mbps/5Mbps？；原因：速率来自产品正文，原理图没有网络吞吐参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `82e5a4281d94df7bb54fb14f2d95da6e457843b0f9f62e8fed462710b710c9cd` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/570/Sch_StampCat1_sch_01.png` |

---

源文档：`zh_CN/stamp/stamp_cat1.md`

源文档 SHA-256：`480fe79152decfd776f8ea588d0a2ee51429d8a931af1b6f8bbd3445568717f5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
