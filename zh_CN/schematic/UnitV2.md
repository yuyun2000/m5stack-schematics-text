# UnitV2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | UnitV2 |
| SKU | U078-D |
| 产品 ID | `unitv2-26188210094d` |
| 源文档 | `zh_CN/unit/unitv2.md` |

## 概述

UnitV2 系统框图以 SSD202 为核心，框内标出 128MB DDR3，并通过 QSPI 连接 256MB NAND Flash。GC2145 Sensor 通过 DVP 连接 USB ISP，USB ISP 再通过 USB 与 SSD202 相连；RTL8188FTV 无线模块也通过 USB 连接 SSD202。Grove Port 以 UART 连接核心，USB Type-C 经 USB 接入 10/100M USB LAN，再以 100M LAN 连接 SSD202。该资源是框图而非器件级原理图，未提供位号、引脚、电源、时钟、复位或保护细节，且 SSD202/SSD202D 与 256MB/512MB NAND 在框图和正文之间存在冲突。

## 检索关键词

`UnitV2`、`U078-D`、`SSD202`、`SSD202D`、`Cortex-A7`、`128MB DDR3`、`256MB NAND Flash`、`512MB NAND Flash`、`QSPI`、`GC2145 Sensor`、`GC2145`、`DVP`、`USB ISP`、`RTL8188FTV`、`Wi-Fi 2.4GHz`、`USB`、`USB Type-C`、`10/100M USB LAN`、`100M LAN`、`Grove Port`、`UART`、`Linux AI camera`、`1080P`、`FOV 68°`、`5V 500mA`、`microphone`、`microSD`、`NAND`、`DDR3`、`system block diagram`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| SSD202 block | SSD202 | 系统核心，连接 DDR3、NAND、摄像头 ISP、Wi-Fi、Grove UART 与 LAN | 图 c139d8ecf6b8 / 第 1 页 / 页 1 中央 SSD202 方框及其 USB/QSPI/UART/100M LAN 连线 |
| 128MB DDR3 block | 未标注 | 框图中嵌于 SSD202 区域的 128MB DDR3 内存 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 中央 SSD202 方框内部的 128MB DDR3 子框 |
| 256MB NAND Flash block | 未标注 | 通过 QSPI 连接 SSD202 的非易失存储 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 右中 256MB NAND Flash 方框与 QSPI 双向箭头 |
| GC2145 Sensor block | GC2145 | 通过 DVP 连接 USB ISP 的图像传感器 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 右上 GC2145 Sensor 方框与 DVP 双向箭头 |
| USB ISP block | 未标注 | 位于 GC2145 DVP 与 SSD202 USB 之间的图像处理模块 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 上中 USB ISP 方框，上接 DVP/GC2145，下接 USB/SSD202 |
| RTL8188FTV block | RTL8188FTV | 通过 USB 连接 SSD202 的无线网络模块 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 右上 RTL8188FTV 方框、无线图标与 USB 双向箭头 |
| 10/100M USB LAN block | 未标注 | 在 USB Type-C USB 链路与 SSD202 100M LAN 之间提供网络桥接 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 下中 10/100M USB LAN 方框，左接 USB Type-C/USB，上接 SSD202/100M LAN |
| USB Type-C block | 未标注 | 通过 USB 连接 10/100M USB LAN 的外部接口 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 左下 USB Type-C 方框与 USB 双向箭头 |
| Grove Port block | 未标注 | 通过 UART 与 SSD202 连接的外部 Grove 接口 | 图 c139d8ecf6b8 / 第 1 页 / 页 1 左中 Grove Port 方框与指向 SSD202 的 UART 双向箭头 |

## 系统结构

### UnitV2 系统框图

SSD202 核心连接 128MB DDR3、QSPI NAND、USB ISP/GC2145、USB/RTL8188FTV、UART/Grove Port，以及 100M LAN/USB LAN/USB Type-C 链路。

- 参数与网络：`controller=SSD202`；`memory=128MB DDR3`；`storage=256MB NAND Flash via QSPI`；`camera=GC2145 Sensor-DVP-USB ISP-USB-SSD202`；`wireless=RTL8188FTV via USB`；`serial=Grove Port via UART`；`host_network=SSD202-100M LAN-10/100M USB LAN-USB-Type-C`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整系统框图的全部方框与双向箭头

## 核心器件

### 系统核心标注

框图中央核心方框明确标为 SSD202，未带 D 后缀，也未展示 CPU 核心数或时钟频率。

- 参数与网络：`schematic_label=SSD202`；`variant_suffix=not shown`；`cpu_cores=not shown`；`clock_frequency=not shown`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 中央方框文字 SSD202

## 接口

### Grove Port

Grove Port 通过标注 UART 的双向箭头直接连接 SSD202。框图未展开连接器针脚、TX/RX 网络、电源或地。

- 参数与网络：`connector=Grove Port`；`interface=UART`；`peer=SSD202`；`direction=bidirectional arrow`；`pins=not expanded`；`power=not shown`；`ground=not shown`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 左中 Grove Port-UART-SSD202 双向箭头

### USB Type-C 与 USB LAN

USB Type-C 通过 USB 双向箭头连接 10/100M USB LAN；该网络模块再通过标注 100M LAN 的双向箭头连接 SSD202。

- 参数与网络：`external_connector=USB Type-C`；`connector_bus=USB`；`bridge=10/100M USB LAN`；`soc_bus=100M LAN`；`soc=SSD202`；`direction=bidirectional arrows`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 下部 USB Type-C-USB-10/100M USB LAN-100M LAN-SSD202 链路

## 总线

### SSD202 与 NAND 的 QSPI

SSD202 与 256MB NAND Flash 之间的连线标注 QSPI，并以双向箭头表示。框图未展开 CLK、CS、IO0~IO3 或电平。

- 参数与网络：`controller=SSD202`；`device=256MB NAND Flash`；`bus=QSPI`；`direction=bidirectional arrow`；`signals=not expanded`；`voltage=not shown`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 中右 SSD202-QSPI-256MB NAND Flash 箭头

### 摄像头到 SSD202 的数据路径

GC2145 Sensor 通过 DVP 连接 USB ISP，USB ISP 再通过 USB 双向箭头连接 SSD202。

- 参数与网络：`sensor=GC2145 Sensor`；`sensor_bus=DVP`；`processor=USB ISP`；`soc_bus=USB`；`soc=SSD202`；`signals=not expanded`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 上部 GC2145 Sensor-DVP-USB ISP-USB-SSD202 链路

### 框图中的 USB 链路

USB 标注分别用于 SSD202 与 USB ISP、SSD202 与 RTL8188FTV、以及 USB Type-C 与 10/100M USB LAN 之间；框图未给 USB 版本、速率、角色或 D+/D- 引脚。

- 参数与网络：`camera_usb=SSD202<->USB ISP`；`wifi_usb=SSD202<->RTL8188FTV`；`type_c_usb=USB Type-C<->10/100M USB LAN`；`usb_version=not shown`；`signals=not expanded`；`roles=not shown`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 三处 USB 双向箭头

### 100M LAN 路径

SSD202 与 10/100M USB LAN 之间的垂直双向箭头标为 100M LAN；框图未展开 RMII/MII 信号、PHY 地址或时钟。

- 参数与网络：`soc=SSD202`；`peer=10/100M USB LAN`；`label=100M LAN`；`direction=bidirectional arrow`；`rmii_mii=not shown`；`phy_address=not shown`；`clock=not shown`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 中下 SSD202-100M LAN-10/100M USB LAN 垂直链路

## 总线地址

### 总线地址

框图未打印 GC2145、RTL8188FTV、NAND、LAN 模块或其他设备的 I2C、USB、QSPI、PHY 地址。

- 参数与网络：`camera_address=null`；`wifi_address=null`；`nand_address=null`；`phy_address=null`；`address_selectors=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图，无 0x 地址、ADDR 或 PHY address 标注

## GPIO 与控制信号

### GPIO、时钟、复位与调试

该框图没有 GPIO 编号、BOOT、RESET、时钟/晶振、JTAG/SWD/UART 调试头或测试点信息。

- 参数与网络：`gpio_map=null`；`boot=null`；`reset=null`；`crystal=null`；`clock_frequency=null`；`jtag=null`；`swd=null`；`debug_header=null`；`test_points=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图，只有模块名和总线名，无引脚/时钟/复位/调试细节

## 保护电路

### 接口与电源保护

框图未显示 USB Type-C、Grove Port 或内部电源的 ESD、TVS、保险丝、过流、过压或反接保护。

- 参数与网络：`usb_esd=null`；`grove_esd=null`；`tvs=null`；`fuse=null`；`overcurrent=null`；`overvoltage=null`；`reverse_polarity=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图未出现保护器件或保护功能块

## 关键网络

### UnitV2 关键连接索引

关键链路为 Grove Port↔UART↔SSD202、GC2145↔DVP↔USB ISP↔USB↔SSD202、RTL8188FTV↔USB↔SSD202、NAND↔QSPI↔SSD202，以及 USB Type-C↔USB↔10/100M USB LAN↔100M LAN↔SSD202。

- 参数与网络：`grove=Grove Port-UART-SSD202`；`camera=GC2145-DVP-USB ISP-USB-SSD202`；`wifi=RTL8188FTV-USB-SSD202`；`storage=256MB NAND-QSPI-SSD202`；`type_c_network=USB Type-C-USB-10/100M USB LAN-100M LAN-SSD202`；`memory=128MB DDR3 inside SSD202 block`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整系统框图全部双向箭头与模块标签

## 存储

### 256MB NAND Flash

框图明确标出 256MB NAND Flash，并以 QSPI 双向箭头连接 SSD202。

- 参数与网络：`capacity=256MB`；`type=NAND Flash`；`bus=QSPI`；`controller=SSD202`；`part_number=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 右中 256MB NAND Flash 方框和 QSPI 箭头

## 内存与 Flash

### 128MB DDR3

框图在 SSD202 区域内部明确标出 128MB DDR3。

- 参数与网络：`type=DDR3`；`capacity=128MB`；`part_number=null`；`bus_width=null`；`frequency=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 中央 SSD202 方框内部 128MB DDR3 子框

## 传感器

### GC2145 Sensor

框图明确标出 GC2145 Sensor，并通过 DVP 双向箭头连接 USB ISP。

- 参数与网络：`sensor=GC2145`；`interface=DVP`；`peer=USB ISP`；`direction=bidirectional arrow`；`pin_map=not expanded`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 右上 GC2145 Sensor-DVP-USB ISP

## 射频

### RTL8188FTV 无线模块

框图明确标出 RTL8188FTV 和无线图标，并通过 USB 双向箭头连接 SSD202。

- 参数与网络：`device=RTL8188FTV`；`host=SSD202`；`interface=USB`；`direction=bidirectional arrow`；`antenna=not expanded`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 右上 SSD202-USB-RTL8188FTV 方框与无线图标

## 模拟电路

### 模拟采样链路

框图未展开模拟前端、ADC/DAC、传感器供电或模拟采样网络。

- 参数与网络：`analog_front_end=null`；`adc=null`；`dac=null`；`analog_sensor_supply=null`；`sampling_nets=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图，无模拟/ADC/DAC 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | UnitV2 系统框图 | `controller=SSD202`；`memory=128MB DDR3`；`storage=256MB NAND Flash via QSPI`；`camera=GC2145 Sensor-DVP-USB ISP-USB-SSD202`；`wireless=RTL8188FTV via USB`；`serial=Grove Port via UART`；`host_network=SSD202-100M LAN-10/100M USB LAN-USB-Type-C` |
| 核心器件 | 系统核心标注 | `schematic_label=SSD202`；`variant_suffix=not shown`；`cpu_cores=not shown`；`clock_frequency=not shown` |
| 核心器件 | SSD202/SSD202D 变体 | `schematic_value=SSD202`；`product_document_value=SigmaStar SSD202D`；`verification_source_needed=BOM, chip marking, or detailed schematic` |
| 内存与 Flash | 128MB DDR3 | `type=DDR3`；`capacity=128MB`；`part_number=null`；`bus_width=null`；`frequency=null` |
| 存储 | 256MB NAND Flash | `capacity=256MB`；`type=NAND Flash`；`bus=QSPI`；`controller=SSD202`；`part_number=null` |
| 存储 | NAND Flash 容量冲突 | `schematic_value=256MB NAND Flash`；`product_document_value=512MB NAND`；`bus=QSPI`；`verification_source_needed=revision-specific BOM or flash identification` |
| 总线 | SSD202 与 NAND 的 QSPI | `controller=SSD202`；`device=256MB NAND Flash`；`bus=QSPI`；`direction=bidirectional arrow`；`signals=not expanded`；`voltage=not shown` |
| 传感器 | GC2145 Sensor | `sensor=GC2145`；`interface=DVP`；`peer=USB ISP`；`direction=bidirectional arrow`；`pin_map=not expanded` |
| 总线 | 摄像头到 SSD202 的数据路径 | `sensor=GC2145 Sensor`；`sensor_bus=DVP`；`processor=USB ISP`；`soc_bus=USB`；`soc=SSD202`；`signals=not expanded` |
| 传感器 | GC2145 摄像头性能 | `sensor=GC2145`；`resolution=null`；`frame_rate=null`；`fov=null`；`dof=null`；`pixel_format=null`；`supply=null`；`product_document_resolution=1080P`；`product_document_fov=68°` |
| 射频 | RTL8188FTV 无线模块 | `device=RTL8188FTV`；`host=SSD202`；`interface=USB`；`direction=bidirectional arrow`；`antenna=not expanded` |
| 射频 | 无线网络规格 | `device=RTL8188FTV`；`band=null`；`standard=null`；`throughput=null`；`antenna=null`；`tx_power=null`；`product_document_value=150Mbps 2.4GHz 802.11 b/g/n` |
| 接口 | Grove Port | `connector=Grove Port`；`interface=UART`；`peer=SSD202`；`direction=bidirectional arrow`；`pins=not expanded`；`power=not shown`；`ground=not shown` |
| 总线 | Grove UART 电气与协议参数 | `tx_pin=null`；`rx_pin=null`；`logic_level=null`；`baud_rate=null`；`data_bits=null`；`stop_bits=null`；`parity=null`；`flow_control=null` |
| 接口 | USB Type-C 与 USB LAN | `external_connector=USB Type-C`；`connector_bus=USB`；`bridge=10/100M USB LAN`；`soc_bus=100M LAN`；`soc=SSD202`；`direction=bidirectional arrows` |
| 总线 | 框图中的 USB 链路 | `camera_usb=SSD202<->USB ISP`；`wifi_usb=SSD202<->RTL8188FTV`；`type_c_usb=USB Type-C<->10/100M USB LAN`；`usb_version=not shown`；`signals=not expanded`；`roles=not shown` |
| 总线 | 100M LAN 路径 | `soc=SSD202`；`peer=10/100M USB LAN`；`label=100M LAN`；`direction=bidirectional arrow`；`rmii_mii=not shown`；`phy_address=not shown`；`clock=not shown` |
| 总线地址 | 总线地址 | `camera_address=null`；`wifi_address=null`；`nand_address=null`；`phy_address=null`；`address_selectors=null` |
| 电源 | 输入电源与电源树 | `input_voltage=null`；`input_current=null`；`regulators=null`；`power_rails=null`；`enables=null`；`charger=null`；`battery=null`；`monitor=null`；`product_document_value=5V at 500mA` |
| 音频 | 麦克风与音频链路 | `product_document_microphone=integrated microphone`；`schematic_microphone=null`；`codec=null`；`i2s=null`；`pdm=null`；`analog_audio=null` |
| GPIO 与控制信号 | GPIO、时钟、复位与调试 | `gpio_map=null`；`boot=null`；`reset=null`；`crystal=null`；`clock_frequency=null`；`jtag=null`；`swd=null`；`debug_header=null`；`test_points=null` |
| 保护电路 | 接口与电源保护 | `usb_esd=null`；`grove_esd=null`；`tvs=null`；`fuse=null`；`overcurrent=null`；`overvoltage=null`；`reverse_polarity=null` |
| 模拟电路 | 模拟采样链路 | `analog_front_end=null`；`adc=null`；`dac=null`；`analog_sensor_supply=null`；`sampling_nets=null` |
| 关键网络 | UnitV2 关键连接索引 | `grove=Grove Port-UART-SSD202`；`camera=GC2145-DVP-USB ISP-USB-SSD202`；`wifi=RTL8188FTV-USB-SSD202`；`storage=256MB NAND-QSPI-SSD202`；`type_c_network=USB Type-C-USB-10/100M USB LAN-100M LAN-SSD202`；`memory=128MB DDR3 inside SSD202 block` |

## 待确认事项

- `component.controller-variant-conflict`：框图标为 SSD202，而产品正文标为 SigmaStar SSD202D；当前资源没有完整料号或位号可确认是否为 D 变体。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 中央核心仅标 SSD202）
- `storage.nand-capacity-conflict`：当前框图标注 256MB NAND Flash，而产品正文写 512MB NAND；资源未给出 NAND 料号或硬件版本说明以解释差异。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 右中方框文字 256MB NAND Flash）
- `sensor.camera-performance-not-shown`：框图确认 GC2145 型号，但未标注分辨率、帧率、FOV、DOF、像素格式、镜头参数或供电。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 GC2145 Sensor 方框仅有型号和 DVP 连接）
- `rf.wifi-performance-not-shown`：框图未标注无线频段、协议、吞吐率、天线类型、射频匹配或发射功率。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 RTL8188FTV 方框只标型号、USB 与无线图标）
- `bus.grove-uart-details-not-shown`：框图只给出 UART 名称，未标注 TX/RX 针脚映射、电平、波特率、数据位、停止位、校验或流控。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 Grove Port 与 SSD202 之间仅标 UART）
- `power.power-tree-not-shown`：框图未绘出输入电压、电源连接器供电脚、DC/DC、LDO、电源轨、使能、充电、电池或监测路径。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图仅显示数据/网络接口，无任何电源符号或电源模块）
- `audio.microphone-not-shown`：产品正文列出内置麦克风，但当前框图没有麦克风、音频 ADC/Codec、I2S/PDM 或模拟音频连接。（证据：图 c139d8ecf6b8 / 第 1 页 / 页 1 完整框图，无 MIC/audio/I2S/PDM 方框或连线）
- `review.controller-variant`：该硬件版本实际装配的是 SSD202 还是 SSD202D，完整订货型号是什么？；原因：当前框图标 SSD202，产品正文标 SigmaStar SSD202D，缺少 BOM、芯片丝印或详细原理图。
- `review.nand-capacity`：该硬件版本的 NAND Flash 容量是框图所示 256MB 还是产品正文所示 512MB？；原因：两个本地来源发生直接容量冲突，需版本化 BOM、Flash 丝印或系统容量读取确认。
- `review.camera-performance`：GC2145 模组的分辨率、帧率、FOV、DOF、像素格式、镜头和供电规格是什么？；原因：框图只确认 GC2145 和 DVP 连接，不能验证正文中的 1080P、FOV 68° 与 DOF 参数。
- `review.wifi-performance`：RTL8188FTV 的频段、802.11 模式、最大吞吐、天线形式与射频性能是否符合正文 150Mbps 2.4GHz 802.11 b/g/n？；原因：框图只有模块型号、USB 链路和无线图标，没有射频参数。
- `review.grove-uart-details`：Grove Port 的针脚顺序、TX/RX 方向、逻辑电平、波特率和帧格式是什么？；原因：框图仅以 UART 双向箭头表示，未展开连接器与电气参数。
- `review.power-tree`：UnitV2 的供电入口、额定 5V@500mA 条件、内部电源轨、转换器、使能和保护路径是什么？；原因：当前资源完全未绘出电源树，正文规格不能替代器件级电源证据。
- `review.microphone`：正文所述内置麦克风的型号、接口、供电和 SSD202 引脚连接是什么？；原因：当前框图未出现麦克风或任何音频链路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c139d8ecf6b831adbcddb2a017ae780439d1e9345c9427e2bcb52e93c3edd40c` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2/unitv2_sch_01.webp` |

---

源文档：`zh_CN/unit/unitv2.md`

源文档 SHA-256：`d280970c28ddd8496e805945e3471c141d5078bfa6ba1139edca8938544ab850`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
