# Atom GPS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom GPS |
| SKU | K043 |
| 产品 ID | `atom-gps-a32cc93b32a0` |
| 源文档 | `zh_CN/atom/atomicgps.md` |

## 概述

当前唯一原理图页只覆盖 Atom GPS 的 TF-015 microSD 与排针子电路。U1 由 3.3V 供电，MOSI/CLK/MISO 引至 P1；CS 仅经 Rp1 4.7KΩ 下拉到 GND，没有主机 CS 连接。Rp1 还将 MISO/CLK/MOSI 上拉到 3.3V。P1/P3 之间只有 GPS_T 同名网络，页面没有显示 GPS 接收器、GPS_RX、天线、PPS、Flash、纽扣电池、状态灯或 GPS 电源主电路。因此 M8030-KT、卫星系统/精度灵敏度、NMEA/9600bps/更新与启动时间、TX/PPS 指示和自弹卡槽均不能由当前资源确认。

## 检索关键词

`Atom GPS`、`K043`、`TF-015`、`microSD`、`MOSI`、`CLK`、`MISO`、`CS`、`GPS_T`、`+3.3V`、`+5VIN`、`Rp1 4.7KΩ`、`P1 Header 5`、`P2 Header 4`、`P3 Header 4`、`M8030-KT`、`NMEA-0183`、`9600bps`、`72 channels`、`GPS subsystem not shown`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TF-015 | microSD 卡座，连接 CS、MOSI、CLK、MISO、3.3V 和 GND | 图 8484b4e774d1 / 第 1 页 / 第 1 页左侧 U1 TF-015，pins2-7 为 CS/MOSI/VCC/CLK/GND/MISO |
| Rp1 | 4 x 4.7KΩ (472) ±5% | MISO/CLK/MOSI 的 3.3V 上拉与 CS 的 GND 下拉电阻阵列 | 图 8484b4e774d1 / 第 1 页 / 第 1 页左上 Rp1：top pins8/7/6 接 +3.3V、top pin5 接 GND，bottom pins1/2/3/4 接 MISO/CLK/MOSI/CS |
| P1 | Header 5 | 引出 +3.3V、GPS_T、MOSI、CLK 和 MISO | 图 8484b4e774d1 / 第 1 页 / 第 1 页右上 P1 Header5，pins1-5 为 +3.3V/GPS_T/MOSI/CLK/MISO |
| P2 | Header 4 | 引出 +5VIN 与 GND，pins1/2 未连接 | 图 8484b4e774d1 / 第 1 页 / 第 1 页右上 P2 Header4，pins1/2 NC、pin3 +5VIN、pin4 GND |
| P3 | Header 4 | 引出 +5VIN、GPS_T 与 GND，pin2 未连接 | 图 8484b4e774d1 / 第 1 页 / 第 1 页右下 P3 Header4，pin1 +5VIN、pin2 NC、pin3 GPS_T、pin4 GND |
| C1,C2 | 100nF (104) 10% 50V | 3.3V 与 5VIN 的对地去耦 | 图 8484b4e774d1 / 第 1 页 / 第 1 页右侧 C1 从 +3.3V 到 GND，C2 从 +5VIN 到 GND |

## 系统结构

### Atom GPS 当前原理图覆盖范围

当前唯一页面包含 U1 TF-015 microSD、Rp1、P1/P2/P3 和 C1/C2；没有显示 GPS 接收器、天线/RF、GPS_RX、PPS、Flash、纽扣电池、指示灯或 GPS 电源主电路。

- 参数与网络：`storage_shown=true`；`headers_shown=true`；`gps_receiver_shown=false`；`rf_path_shown=false`；`gps_rx_shown=false`；`pps_shown=false`；`flash_shown=false`；`backup_battery_shown=false`；`gps_power_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页整页仅有 TF-015、Rp1、P1/P2/P3 与 C1/C2

## 核心器件

### GPS 主电路可见性

当前页面没有显示 M8030-KT 或其他 GPS 接收器、天线/RF、PPS、Flash、纽扣电池、GPS_RX、TX/PPS LED 或 GPS 电源转换。

- 参数与网络：`m8030_kt_shown=false`；`antenna_shown=false`；`pps_shown=false`；`flash_shown=false`；`coin_cell_shown=false`；`gps_rx_shown=false`；`indicators_shown=false`；`gps_power_conversion_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页整页只出现 TF-015、Rp1、P1/P2/P3 和 C1/C2

### P1/P2/P3 排针角色

P1/P2/P3 只标 Header5/Header4，没有在本页标出各自对应 Atom 主机、GPS 子板或板间连接方向。

- 参数与网络：`p1_role_shown=false`；`p2_role_shown=false`；`p3_role_shown=false`；`mating_orientation_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 P1/P2/P3 下方仅标 Header5/Header4

## 电源

### microSD 3.3V 供电

U1 VCC pin4 连接 +3.3V，GND pin6 连接 GND；C1 100nF 从 +3.3V 接地。

- 参数与网络：`supply=U1 pin4 +3.3V`；`ground=U1 pin6 GND`；`decoupling=C1 100nF (104) 10% 50V`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 U1 pins4/6 与右上 C1 +3.3V-GND

### +5VIN 排针去耦

C2 100nF (104) 10% 50V 从 +5VIN 接 GND；+5VIN 连接 P2 pin3 与 P3 pin1，但当前页没有显示 GPS 主电路的 5V 消费路径。

- 参数与网络：`capacitor=C2 100nF (104) 10% 50V`；`p2=pin3 +5VIN`；`p3=pin1 +5VIN`；`gps_power_consumer_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 P2/P3 +5VIN 与 C2 +5VIN-GND

## 接口

### P1 五针排针

P1 pins1-5 依次为 +3.3V、GPS_T、MOSI、CLK、MISO。

- 参数与网络：`pin1=+3.3V`；`pin2=GPS_T`；`pin3=MOSI`；`pin4=CLK`；`pin5=MISO`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页右上 P1 Header5 与 pins1-5 网络

### P2 四针排针

P2 pins1/2 未连接，pin3 接 +5VIN，pin4 接 GND。

- 参数与网络：`pin1=NC`；`pin2=NC`；`pin3=+5VIN`；`pin4=GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页右上 P2 Header4 与 NC/+5VIN/GND

### P3 四针排针

P3 pin1 接 +5VIN，pin2 未连接，pin3 接 GPS_T，pin4 接 GND。

- 参数与网络：`pin1=+5VIN`；`pin2=NC`；`pin3=GPS_T`；`pin4=GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页右下 P3 Header4 与 +5VIN/NC/GPS_T/GND

## 总线

### microSD 主机信号

U1 MOSI pin3、CLK pin5、MISO pin7 分别连接 P1 pins3/4/5；U1 CS pin2 只连接 Rp1 下拉，没有连接 P1/P2/P3。

- 参数与网络：`controller_to_card=P1 pin3 MOSI -> U1 pin3`；`clock=P1 pin4 CLK -> U1 pin5`；`card_to_controller=P1 pin5 MISO -> U1 pin7`；`chip_select=U1 pin2 CS -> Rp1 only`；`host_cs_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 U1/P1 的 MOSI/CLK/MISO 同名网络与 U1 CS-Rp1 局部连线

## GPIO 与控制信号

### microSD 信号偏置

Rp1 pins1/2/3 分别把 MISO、CLK、MOSI 经 4.7KΩ 上拉到 +3.3V，pin4 把 CS 经 4.7KΩ 下拉到 GND。

- 参数与网络：`miso=Rp1 pins1-8, 4.7KΩ pull-up to +3.3V`；`clk=Rp1 pins2-7, 4.7KΩ pull-up to +3.3V`；`mosi=Rp1 pins3-6, 4.7KΩ pull-up to +3.3V`；`cs=Rp1 pins4-5, 4.7KΩ pull-down to GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 Rp1 top pins8/7/6 +3.3V、top pin5 GND，bottom pins1/2/3/4 MISO/CLK/MOSI/CS

## 关键网络

### GPS_T 排针网络

GPS_T 同时标在 P1 pin2 和 P3 pin3；当前页没有显示 GPS_T 的源器件或 GPS_RX 对应网络。

- 参数与网络：`p1=pin2`；`p3=pin3`；`source_component_shown=false`；`gps_rx_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页右侧 P1 pin2 与 P3 pin3 的 GPS_T 标签及整页网络范围

## 存储

### TF-015 microSD 引脚

U1 pin2 为 CS，pin3 为 MOSI，pin4 接 +3.3V，pin5 为 CLK，pin6 接 GND，pin7 为 MISO。

- 参数与网络：`pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO`
- 证据：图 8484b4e774d1 / 第 1 页 / 第 1 页左侧 U1 TF-015 方框内 pins2-7 标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom GPS 当前原理图覆盖范围 | `storage_shown=true`；`headers_shown=true`；`gps_receiver_shown=false`；`rf_path_shown=false`；`gps_rx_shown=false`；`pps_shown=false`；`flash_shown=false`；`backup_battery_shown=false`；`gps_power_shown=false` |
| 存储 | TF-015 microSD 引脚 | `pin2=CS`；`pin3=MOSI`；`pin4=+3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO` |
| 电源 | microSD 3.3V 供电 | `supply=U1 pin4 +3.3V`；`ground=U1 pin6 GND`；`decoupling=C1 100nF (104) 10% 50V` |
| 总线 | microSD 主机信号 | `controller_to_card=P1 pin3 MOSI -> U1 pin3`；`clock=P1 pin4 CLK -> U1 pin5`；`card_to_controller=P1 pin5 MISO -> U1 pin7`；`chip_select=U1 pin2 CS -> Rp1 only`；`host_cs_shown=false` |
| GPIO 与控制信号 | microSD 信号偏置 | `miso=Rp1 pins1-8, 4.7KΩ pull-up to +3.3V`；`clk=Rp1 pins2-7, 4.7KΩ pull-up to +3.3V`；`mosi=Rp1 pins3-6, 4.7KΩ pull-up to +3.3V`；`cs=Rp1 pins4-5, 4.7KΩ pull-down to GND` |
| 接口 | P1 五针排针 | `pin1=+3.3V`；`pin2=GPS_T`；`pin3=MOSI`；`pin4=CLK`；`pin5=MISO` |
| 接口 | P2 四针排针 | `pin1=NC`；`pin2=NC`；`pin3=+5VIN`；`pin4=GND` |
| 接口 | P3 四针排针 | `pin1=+5VIN`；`pin2=NC`；`pin3=GPS_T`；`pin4=GND` |
| 关键网络 | GPS_T 排针网络 | `p1=pin2`；`p3=pin3`；`source_component_shown=false`；`gps_rx_shown=false` |
| 电源 | +5VIN 排针去耦 | `capacitor=C2 100nF (104) 10% 50V`；`p2=pin3 +5VIN`；`p3=pin1 +5VIN`；`gps_power_consumer_shown=false` |
| 核心器件 | GPS 主电路可见性 | `m8030_kt_shown=false`；`antenna_shown=false`；`pps_shown=false`；`flash_shown=false`；`coin_cell_shown=false`；`gps_rx_shown=false`；`indicators_shown=false`；`gps_power_conversion_shown=false` |
| 核心器件 | P1/P2/P3 排针角色 | `p1_role_shown=false`；`p2_role_shown=false`；`p3_role_shown=false`；`mating_orientation_shown=false` |
| 存储 | TF-015 实际存储协议模式 | `documented_bus=SPI`；`host_signals=MOSI,CLK,MISO`；`host_cs=null`；`card_cs=Rp1 4.7KΩ pull-down to GND`；`mode=null` |
| 核心器件 | 正文中的 GPS 模组与定位能力 | `documented_receiver=M8030-KT`；`documented_storage=internal Flash`；`documented_backup=coin cell`；`documented_systems=GPS,GLONASS,GALILEO,BDS,SBAS,QZSS`；`documented_channels=72`；`documented_horizontal_accuracy=2m`；`documented_sensitivity=tracking -167dBm; acquisition -160dBm; cold -148dBm; hot -156dBm`；`schematic_receiver=null` |
| 总线 | 正文中的 GPS UART 与输出指标 | `documented_uart=9600bps, 1 start, 1 stop, no parity`；`documented_protocol=NMEA-0183`；`documented_sentences=RMC,VTG,GGA,GSA,GSV,GLL`；`documented_update=1-10Hz`；`documented_start=cold 26s, warm 25s, hot 1s`；`visible_tx_net=GPS_T`；`visible_rx_net=null` |
| 其他事实 | 正文中的卡槽与 GPS 指示功能 | `documented_slot=self-eject microSD`；`documented_tx_led=flashes on power/data output`；`documented_pps_led=flashes after 3D fix`；`mechanical_detail_shown=false`；`led_circuit_shown=false` |

## 待确认事项

- `storage.card-interface-mode`：正文将 MOSI/CLK/MISO 描述为 SPI，但当前页未引出主机 CS，卡座 CS 只经 4.7KΩ 下拉到 GND；无法由该页确认软件使用标准 SPI、固定片选方案还是其他 SD 模式。（证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 U1 CS-Rp1 下拉与 P1/P2/P3 网络范围）
- `component.documented-gps-capabilities`：正文称使用 M8030-KT，内置 Flash 和纽扣电池，支持 GPS/GLONASS/GALILEO/BDS/SBAS/QZSS、72 搜索通道、2m 水平精度及多组灵敏度；当前页没有 GPS 主电路，无法验证这些器件和指标。（证据：图 8484b4e774d1 / 第 1 页 / 第 1 页无 M8030-KT、Flash、纽扣电池或 RF/GNSS 器件）
- `bus.documented-gps-uart-output`：正文给出 9600bps、1 起始位、1 停止位、无校验、NMEA-0183、RMC/VTG/GGA/GSA/GSV/GLL、1-10Hz 和冷/温/热启动时间；当前页只显示 GPS_T 排针网络，没有 GPS 接收器 UART 或 GPS_RX，无法验证这些配置。（证据：图 8484b4e774d1 / 第 1 页 / 第 1 页仅 P1/P3 GPS_T，同页无 GPS_RX、UART 器件、协议或波特率文字）
- `other.documented-mechanical-indicators`：正文称 TF 卡槽为自弹式，并有 TX 上电闪烁和 PPS 定位后闪烁指示；当前页只显示 TF-015 电气符号，没有机械结构、TX/PPS 来源或 LED。（证据：图 8484b4e774d1 / 第 1 页 / 第 1 页 U1 仅为 TF-015 电气符号，整页无 TX/PPS 或 LED 器件）
- `review.full-gps-schematic`：是否有 K043 当前版本的完整 GPS 主电路页面，可确认 M8030-KT、RF/天线、Flash、纽扣电池、UART/PPS、LED 与电源？；原因：当前唯一资源只覆盖 microSD 与排针子电路，无法完成 GPS 功能链器件级核对。
- `review.header-roles`：P1/P2/P3 分别连接 Atom 主机还是 GPS 子板，实际配对方向与完整针脚定义是什么？；原因：页面只给本地针号和网络，没有连接器用途与板间关系。
- `review.storage-interface-mode`：K043 的 TF-015 实际使用标准 SPI、固定片选还是其他 SD 模式，软件如何处理未引出的 CS？；原因：图纸只有 MOSI/CLK/MISO 主机线，CS 仅 4.7KΩ 下拉，不能按常规四线 SPI 假定。
- `review.gps-module-and-performance`：K043 当前 GPS 模组/BOM 和正式 datasheet 是否确认 M8030-KT、Flash、纽扣电池、卫星系统、72 通道、精度与灵敏度？；原因：这些正文事实的主电路在当前资源中完全缺失，无法建立器件级证据。
- `review.gps-uart-output`：量产模组是否固定为 9600bps NMEA-0183，并支持正文语句、1-10Hz 与启动时间？；原因：当前页只有来源不明的 GPS_T，缺少 GPS 接收器 UART 与 GPS_RX，无法验证固件输出。
- `review.slot-and-indicators`：当前 TF-015 BOM 是否为自弹式，TX 与 PPS 指示灯的完整电路在哪一页？；原因：本页没有机械结构或 LED 电路，无法确认正文描述。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8484b4e774d1e545bf2222560052662d903c68f5f2d50ba71d36fc8fcaf011f8` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_sch_01.webp` |

---

源文档：`zh_CN/atom/atomicgps.md`

源文档 SHA-256：`f8c3a7511600c0d4387006759f01d8c72fba5969104fa59b53c9af766a024a3e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
