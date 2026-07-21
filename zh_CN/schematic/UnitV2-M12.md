# UnitV2-M12 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | UnitV2-M12 |
| SKU | U078-M12 |
| 产品 ID | `unitv2-m12-8d140c5aef60` |
| 源文档 | `zh_CN/unit/unitv2_m12.md` |

## 概述

UnitV2-M12 的本地资源是一张系统框图，而非含位号、引脚和电源网络的器件级原理图。框图以 SSD202 为中心，块内标注 128MB DDR3；SSD202 通过 QSPI 连接 256MB NAND Flash，通过 USB 连接 RTL8188FTV 和 USB ISP，通过 100M LAN 连接 10/100M USB LAN，并通过 UART 连接 Grove Port。USB ISP 通过 DVP 连接 GC2145 Sensor，USB Type-C 通过 USB 连接 10/100M USB LAN。框图与正文的 SSD202D、GC2053、512MB NAND 三项描述存在冲突，需要按硬件版本、BOM 或完整原理图确认。

## 检索关键词

`UnitV2-M12`、`U078-M12`、`SSD202`、`SSD202D`、`128MB DDR3`、`256MB NAND Flash`、`512MB NAND Flash`、`GC2145 Sensor`、`GC2053`、`USB ISP`、`DVP`、`RTL8188FTV`、`QSPI`、`Grove Port`、`UART`、`USB Type-C`、`10/100M USB LAN`、`100M LAN`、`SR9900`、`Wi-Fi 2.4GHz`、`M12 lens`、`FOV 85`、`FOV 150`、`Linux`、`microSD`、`microphone`、`active fan`、`AI camera`、`USB Ethernet`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| SoC block | SSD202 | 系统中心处理器块，连接 UART、USB、QSPI、100M LAN 与内存块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页中央 SSD202 方框，左右/上下连接 UART、USB、QSPI、100M LAN |
| Memory block | 128MB DDR3 | 绘制在 SSD202 块内部的 DDR3 系统内存 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页中央 SSD202 方框内部，128MB DDR3 子块 |
| NAND block | 256MB NAND Flash | 通过 QSPI 与 SSD202 连接的非易失存储块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页右中，256MB NAND Flash 方框与 QSPI 双向箭头 |
| Camera sensor block | GC2145 Sensor | 通过 DVP 连接 USB ISP 的图像传感器块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页右上，GC2145 Sensor 方框与 DVP 双向箭头 |
| ISP block | USB ISP | 在 GC2145 DVP 与 SSD202 USB 之间的图像处理/桥接块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页上中，USB ISP 方框，向右 DVP、向下 USB |
| Wi-Fi block | RTL8188FTV | 通过 USB 与 SSD202 连接的无线网络器件块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页右中上，RTL8188FTV 方框、Wi-Fi 图标与 USB 双向箭头 |
| Grove block | Grove Port | 通过 UART 与 SSD202 连接的外部接口块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页左中，Grove Port 方框与 UART 双向箭头 |
| Ethernet block | 10/100M USB LAN | USB Type-C 与 SSD202 100M LAN 之间的有线网络块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页下中，10/100M USB LAN 方框，左接 USB、上接 100M LAN |
| USB connector block | USB Type-C | 通过 USB 连接 10/100M USB LAN 的外部连接器块 | 图 c139d8ecf6b8 / 第 1 页 / 第 1 页左下，USB Type-C 方框与 USB 双向箭头 |

## 系统结构

### UnitV2-M12 系统框图架构

SSD202 是中心处理块，连接 128MB DDR3、QSPI NAND、USB Wi-Fi、USB ISP、UART Grove 和 100M LAN；USB ISP 再以 DVP 连接 GC2145，USB Type-C 通过 10/100M USB LAN 连接 SSD202。

- 参数与网络：`processor=SSD202`；`memory=128MB DDR3`；`storage=256MB NAND Flash via QSPI`；`camera=GC2145 via USB ISP/DVP`；`wifi=RTL8188FTV via USB`；`grove=UART`；`ethernet=USB Type-C -> 10/100M USB LAN -> 100M LAN`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页完整系统框图

### 资源为系统框图

本地页面只包含功能方框和总线名称，没有器件位号、芯片引脚、GPIO 映射、电源轨、电压转换、时钟、复位、BOOT、保护、调试、连接器针脚或无源器件。

- 参数与网络：`reference_designators=null`；`pins=null`；`gpio=null`；`power_rails=null`；`clock=null`；`reset_boot=null`；`protection=null`；`debug=null`；`passives=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页完整框图，仅有 9 个功能块与 UART/USB/DVP/QSPI/100M LAN 标签

## 接口

### Grove Port UART

Grove Port 与 SSD202 之间由 UART 双向箭头连接；框图未给连接器位号、针脚、电源、TX/RX 网络名、电平或波特率。

- 参数与网络：`connector_block=Grove Port`；`processor=SSD202`；`bus=UART`；`direction=bidirectional`；`pinout=null`；`voltage=null`；`baud=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页左中 Grove Port-UART-SSD202

### USB Type-C 有线网络路径

USB Type-C 通过 USB 双向箭头连接 10/100M USB LAN，该网络块再通过 100M LAN 双向箭头连接 SSD202。

- 参数与网络：`connector=USB Type-C`；`usb_device=10/100M USB LAN`；`processor_link=100M LAN`；`processor=SSD202`；`connector_pinout=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页下部 USB Type-C-USB-10/100M USB LAN-100M LAN-SSD202

## 总线

### 相机 DVP 与 ISP USB 链路

GC2145 Sensor 通过 DVP 双向箭头连接 USB ISP，USB ISP 再通过 USB 双向箭头连接 SSD202。

- 参数与网络：`sensor=GC2145 Sensor`；`sensor_bus=DVP`；`bridge=USB ISP`；`processor_bus=USB`；`processor=SSD202`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页上部 GC2145 Sensor-DVP-USB ISP-USB-SSD202 链

### RTL8188FTV USB 连接

RTL8188FTV 通过标注 USB 的双向箭头连接 SSD202；框图没有天线、晶振、电源、USB 引脚或射频匹配。

- 参数与网络：`controller=SSD202`；`device=RTL8188FTV`；`bus=USB`；`antenna=null`；`rf_matching=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页右中上 SSD202-USB-RTL8188FTV

## 存储

### QSPI NAND Flash

SSD202 通过标注 QSPI 的双向连接接入 256MB NAND Flash；框图未给具体 NAND 料号、引脚、总线宽度、时钟或 ECC。

- 参数与网络：`controller=SSD202`；`bus=QSPI`；`storage=256MB NAND Flash`；`part_number=null`；`clock=null`；`ecc=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页 SSD202 右侧 QSPI 双向箭头与 256MB NAND Flash

## 内存与 Flash

### 128MB DDR3

框图在 SSD202 方框内部明确标出 128MB DDR3，未给内存位号、厂商、料号、位宽、频率或走线拓扑。

- 参数与网络：`capacity=128MB`；`type=DDR3`；`reference=null`；`part_number=null`；`bus_width=null`；`frequency=null`
- 证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页 SSD202 内部 128MB DDR3 方框

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | UnitV2-M12 系统框图架构 | `processor=SSD202`；`memory=128MB DDR3`；`storage=256MB NAND Flash via QSPI`；`camera=GC2145 via USB ISP/DVP`；`wifi=RTL8188FTV via USB`；`grove=UART`；`ethernet=USB Type-C -> 10/100M USB LAN -> 100M LAN` |
| 内存与 Flash | 128MB DDR3 | `capacity=128MB`；`type=DDR3`；`reference=null`；`part_number=null`；`bus_width=null`；`frequency=null` |
| 存储 | QSPI NAND Flash | `controller=SSD202`；`bus=QSPI`；`storage=256MB NAND Flash`；`part_number=null`；`clock=null`；`ecc=null` |
| 总线 | 相机 DVP 与 ISP USB 链路 | `sensor=GC2145 Sensor`；`sensor_bus=DVP`；`bridge=USB ISP`；`processor_bus=USB`；`processor=SSD202` |
| 总线 | RTL8188FTV USB 连接 | `controller=SSD202`；`device=RTL8188FTV`；`bus=USB`；`antenna=null`；`rf_matching=null` |
| 接口 | Grove Port UART | `connector_block=Grove Port`；`processor=SSD202`；`bus=UART`；`direction=bidirectional`；`pinout=null`；`voltage=null`；`baud=null` |
| 接口 | USB Type-C 有线网络路径 | `connector=USB Type-C`；`usb_device=10/100M USB LAN`；`processor_link=100M LAN`；`processor=SSD202`；`connector_pinout=null` |
| 系统结构 | 资源为系统框图 | `reference_designators=null`；`pins=null`；`gpio=null`；`power_rails=null`；`clock=null`；`reset_boot=null`；`protection=null`；`debug=null`；`passives=null` |
| 核心器件 | SSD202 与正文 SSD202D 型号冲突 | `schematic_label=SSD202`；`documented_part=SigmaStar SSD202D`；`resolved_part_number=null` |
| 传感器 | GC2145 与正文 GC2053 型号冲突 | `schematic_sensor=GC2145`；`documented_sensor=GC2053`；`documented_resolution=1080P`；`resolved_sensor=null` |
| 存储 | 256MB 与正文 512MB NAND 冲突 | `schematic_capacity=256MB`；`documented_capacity=512MB`；`bus=QSPI`；`resolved_capacity=null` |
| 内存与 Flash | 正文双核 Cortex-A7 与 1.2GHz | `documented_cpu=dual Cortex-A7`；`documented_frequency=1.2GHz`；`schematic_cpu_detail=null`；`cache=null` |
| 传感器 | 正文双 M12 镜头与视场角 | `documented_lenses=2`；`documented_mount=M12`；`documented_normal_fov=85 degrees`；`documented_fisheye_fov=150 degrees`；`manual_focus=true`；`schematic_lens_blocks=null` |
| 核心器件 | 正文 SR9900 以太网芯片 | `documented_part=SR9900`；`schematic_block=10/100M USB LAN`；`confirmed_part_number=null` |
| 射频 | 正文 Wi-Fi 规格 | `wifi_chip=RTL8188FTV`；`documented_rate=150Mbps`；`documented_band=2.4GHz`；`documented_standards=802.11 b/g/n`；`antenna=null`；`test_conditions=null` |
| 接口 | 正文列出的 microSD、麦克风、风扇、按键与指示灯 | `documented_peripherals=TFCard,Button,Microphone,active fan,red LED,white LED`；`schematic_blocks=null`；`gpio=null`；`power_control=null` |
| 电源 | 正文 5V@500mA 输入 | `documented_input=5V@500mA`；`power_connector=USB Type-C block`；`schematic_power_path=null`；`regulators=null`；`protection=null` |
| 其他事实 | 正文 Linux 与 AI 软件能力 | `documented_os=Linux`；`documented_tools=OpenCV,SSH,JupyterNotebook,Web preview`；`documented_uart_output=JSON`；`documented_ai_functions=12`；`firmware_version=null`；`algorithm_performance=null` |

## 待确认事项

- `component.soc-identity-conflict`：框图中央明确标 SSD202，正文则称 SigmaStar SSD202D；当前资源无法判断二者是简写、同系列变体还是硬件版本差异。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页中央处理器块标 SSD202）
- `sensor.camera-model-conflict`：框图相机块明确标 GC2145 Sensor，正文称 UnitV2-M12 使用 GC2053 1080P Colored Sensor；两者型号不同，需确认当前 U078-M12 硬件版本。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页右上相机块标 GC2145 Sensor）
- `storage.nand-capacity-conflict`：框图存储块明确标 256MB NAND Flash，正文称 512MB NAND Flash；容量相差一倍，当前页面无法确认量产配置。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页右中存储块标 256MB NAND Flash）
- `memory.documented-soc-performance`：正文称 SSD202D 集成双核 Cortex-A7 1.2GHz；框图只标 SSD202，没有 CPU 核数、架构、频率、缓存或片内存储信息。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页 SSD202 方框，无 CPU 参数）
- `sensor.documented-dual-lenses`：正文称配备常规 FOV 85° 与鱼眼 FOV 150° 两个可手动调焦 M12 镜头；框图只显示单个 GC2145 Sensor 块，没有镜头数量、接口、焦距、FOV 或机械切换结构。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页仅有 GC2145 Sensor 方框，无镜头信息）
- `component.documented-ethernet-chip`：正文称以太网网卡为 SR9900；框图只标 10/100M USB LAN，没有 SR9900 型号、位号、晶振、PHY/MAC 引脚或磁性器件。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页下中仅标 10/100M USB LAN）
- `rf.documented-wifi-performance`：正文称 Wi-Fi 为 150Mbps、2.4GHz、802.11 b/g/n；框图确认 RTL8188FTV 通过 USB 连接，但没有天线、射频匹配、频段、速率或法规配置。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页 RTL8188FTV 方框与 Wi-Fi 图标）
- `interface.documented-missing-peripherals`：正文列出 TFCard、Button、Microphone、主动散热风扇及红/白指示灯；框图没有这些功能块、连接器、GPIO、电源或控制网络，因此无法由当前资源确认。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页完整框图，无 TFCard/按键/麦克风/风扇/LED）
- `power.documented-input`：正文给出输入电压 5V@500mA；框图没有 VBUS、电源输入方向、DC/DC/LDO、电源轨、功耗、保护或额定电流标注。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页 USB Type-C 仅标 USB 数据链路，无电源轨）
- `other.documented-linux-ai-features`：正文称内置 Linux、OpenCV、SSH、JupyterNotebook、Web 预览、UART JSON 和多种 AI 识别功能；系统框图只描述硬件块连接，无法确认软件镜像、版本、算法清单、模型性能或协议。（证据：图 c139d8ecf6b8 / 第 1 页 / 第 1 页系统框图，无软件版本或算法信息）
- `review.soc-identity`：U078-M12 当前量产 SoC 是框图标注的 SSD202 还是正文所述 SSD202D？；原因：两处型号文字不一致。
- `review.camera-model`：U078-M12 当前量产图像传感器是 GC2145 还是 GC2053，分辨率与 DVP/ISP 配置是什么？；原因：框图与正文型号冲突。
- `review.nand-capacity`：当前 NAND 容量是框图 256MB 还是正文 512MB，其具体料号与分区是什么？；原因：两处容量相差一倍。
- `review.soc-performance`：请用 SoC datasheet 与固件确认双 Cortex-A7、1.2GHz、缓存及可用片内资源。；原因：框图未展开处理器内部规格。
- `review.dual-lenses`：请确认两只 M12 镜头的焦距、85°/150° FOV、手动调焦范围及与单个传感器的机械切换方式。；原因：框图没有镜头或机械结构。
- `review.ethernet-chip`：请用 BOM 或 USB 枚举信息确认 10/100M USB LAN 是否为 SR9900 及其硬件版本。；原因：框图只给功能块名。
- `review.wifi-performance`：请用 RTL8188FTV 配置和整机测试确认 150Mbps、2.4GHz 802.11 b/g/n、天线与射频性能。；原因：框图没有射频电路或性能条件。
- `review.missing-peripherals`：请提供完整原理图或 BOM，确认 TFCard、按键、麦克风、风扇及红/白 LED 的型号、GPIO 和电源控制。；原因：当前框图完全未显示这些正文外围。
- `review.input-power`：请确认 USB Type-C 5V@500mA 输入范围、峰值电流、电源转换、保护和各电源轨。；原因：框图没有电源路径。
- `review.linux-ai-features`：请确认当前 Linux 镜像、工具版本、12项 AI 功能、UART JSON 协议与性能边界。；原因：系统框图不能证明软件能力。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c139d8ecf6b831adbcddb2a017ae780439d1e9345c9427e2bcb52e93c3edd40c` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_sch_01.webp` |

---

源文档：`zh_CN/unit/unitv2_m12.md`

源文档 SHA-256：`29fa62c613da9ba74dacfdf75f9e13ade905eb5be75b3e97fb36883485a0eb0a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
