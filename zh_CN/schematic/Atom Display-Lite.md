# Atom Display-Lite 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Display-Lite |
| SKU | K115-B |
| 产品 ID | `atom-display-lite-0734246aa8a5` |
| 源文档 | `zh_CN/atom/atom_display_lite.md` |

## 概述

当前本地资源是一张 Atom Display-Lite 系统框图：M5Atom 通过 SPI 驱动 FPGA 内的 SPI Slave、命令和流式读写逻辑，并通过 I2C 控制 HDMI Transceiver IC。像素数据经嵌入式 SDRAM、AXI4、Frame Buffer Reader、Async FIFO 和 Video Signal Generator 形成视频链路，再由 HDMI Transceiver IC 通过 TMDS 输出到 HDMI Connector。框图同时给出两路晶振、GOWIN PLL、70 MHz 主时钟和 140 MHz SDRAM 时钟，但未提供物理位号、具体芯片型号、GPIO、电源轨或保护电路。

## 检索关键词

`Atom Display-Lite`、`K115-B`、`M5Atom`、`FPGA`、`HDMI Connector`、`HDMI Transceiver IC`、`TMDS`、`I2C`、`SPI`、`SPI Slave`、`Command`、`Stream Reader`、`Stream Writer`、`Pixel Data`、`AXI4`、`AXI SDRAM Controller`、`SDRAM Controller`、`Embedded SDRAM`、`Frame Buffer Reader`、`Async FIFO`、`Video Signal Generator`、`GOWIN PLL`、`GOWIN IP`、`Chisel`、`Video Clock`、`Main Clock`、`SDRAM Clock`、`SPI Clock`、`70 MHz`、`140 MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M5Atom | 未标注 | 框图中的外部主控模块，通过 SPI 连接 FPGA，并通过 I2C 控制 HDMI Transceiver IC | 图 0d5a11986a3c / 第 1 页 / 页面底部紫色 M5Atom 方框；向上标注 SPI，右侧回路标注 I2C |
| HDMI Connector | 未标注 | 接收 HDMI Transceiver IC 输出的 TMDS 信号 | 图 0d5a11986a3c / 第 1 页 / 页面顶部紫色 HDMI Connector 方框及其下方 TMDS 箭头 |
| HDMI Transceiver IC | 未标注 | 接收视频信号和 I2C 控制，并向 HDMI Connector 输出 TMDS | 图 0d5a11986a3c / 第 1 页 / 页面上部紫色 HDMI Transceiver IC 方框；下方 Video... 输入、右侧 I2C、上方 TMDS |
| Crystal (Video Clock) | 未标注 | 为图中 Video Clock... 时钟域提供外部晶振输入 | 图 0d5a11986a3c / 第 1 页 / 页面左上第一枚紫色 Crystal... 方框，箭头指向 Video Clock... 虚线框 |
| Crystal (PLL input) | 未标注 | 向 GOWIN PLL 提供外部晶振输入 | 图 0d5a11986a3c / 第 1 页 / 页面左侧第二枚紫色 Crystal... 方框，连线向下后进入 GOWIN PLL |
| GOWIN PLL | 未标注 | GOWIN IP 时钟模块，输出图示 70 MHz 和 140 MHz 时钟 | 图 0d5a11986a3c / 第 1 页 / 页面左中蓝灰色 GOWIN PLL 方框；输出支路旁标注 70[MHz] 和 140[MHz] |
| Embedded SDRAM | 未标注 | 由 SDRAM Controller 访问的帧数据存储硬件 | 图 0d5a11986a3c / 第 1 页 / 页面下部紫色 Embedded SDRAM 方框，与 SDRAM Controller 之间为双向 SDRAM... 连线 |
| SDRAM Controller | 未标注 | GOWIN IP 存储控制器，连接 AXI SDRAM 控制桥与 Embedded SDRAM | 图 0d5a11986a3c / 第 1 页 / 页面下部蓝灰色 SDRAM Controller 方框；上接 AXI SDRAM Controller B...，下接 Embedded SDRAM |
| AXI SDRAM Controller B... | 未标注 | Chisel 侧 AXI4 到 SDRAM Controller 接口的桥接模块 | 图 0d5a11986a3c / 第 1 页 / 页面中央偏下绿色 AXI SDRAM Controller B... 方框；上接 AXI4， 下接 SDRC s... |
| AXI4 interconnect (unlabeled) | 未标注 | 汇聚 Frame Buffer Reader、Stream Reader、Stream Writer 与 SDRAM 控制桥的 AXI4 通路 | 图 0d5a11986a3c / 第 1 页 / 页面中央绿色梯形总线符号；相邻三条客户端连线和向下桥接连线均标注 AXI4 |
| Frame Buffer Reader | 未标注 | 通过 AXI4 读取帧缓冲，并向 Async FIFO 输出视频数据 | 图 0d5a11986a3c / 第 1 页 / 页面中央绿色 Frame Buffer Reader 方框；下接 AXI4，上接 Video... 到 Async FIFO |
| Async FIFO | 未标注 | 位于主时钟与视频时钟链路之间的异步 FIFO | 图 0d5a11986a3c / 第 1 页 / 页面中上部竖向绿色 Async FIFO 方框，位于 Frame Buffer Reader 与 Video Signal Generator 之间 |
| Video Signal Generator | 未标注 | 接收 Async FIFO 的视频数据并输出 Video... 到 HDMI Transceiver IC | 图 0d5a11986a3c / 第 1 页 / 页面上部绿色 Video Signal Generator 方框；下接 Async FIFO，上接 HDMI Transceiver IC |
| Stream Reader | 未标注 | 接收 Command... 控制，通过 AXI4 访问存储通路，并返回 Pixel Data | 图 0d5a11986a3c / 第 1 页 / 页面右中绿色 Stream Reader 方框；左接 AXI4，底部接 Command，右侧回路标注 Pixel Data |
| Stream Writer | 未标注 | 接收 Command... 控制并通过 AXI4 向存储通路写入流数据 | 图 0d5a11986a3c / 第 1 页 / 页面右中绿色 Stream Writer 方框；左侧连线标注 AXI4，下方控制连线标注 Command |
| Command... | 未标注 | 在 SPI Slave 与 Stream Reader/Stream Writer 之间分发命令并接收像素数据 | 图 0d5a11986a3c / 第 1 页 / 页面右中下绿色 Command... 方框；下接 SPI Slave，上接两条 Command 支路，右侧接 Pixel Data 回路 |
| SPI Slave | 未标注 | 接收 M5Atom SPI，并与 Command... 模块交换命令通道 | 图 0d5a11986a3c / 第 1 页 / 页面右下绿色 SPI Slave 方框；下方连接标注 SPI，上方双向连接标注 Command... |

## 系统结构

### 端到端视频路径

框图显示 M5Atom 的 SPI 数据进入 FPGA 后，经命令与流式读写逻辑访问 Embedded SDRAM；显示读取链依次经过 Frame Buffer Reader、Async FIFO、Video Signal Generator 和 HDMI Transceiver IC，最终以 TMDS 到达 HDMI Connector。

- 参数与网络：`controller=M5Atom`；`input_bus=SPI`；`memory=Embedded SDRAM`；`output_signal=TMDS`；`output_connector=HDMI Connector`
- 证据：图 0d5a11986a3c / 第 1 页 / 整页框图：底部 M5Atom 到右侧 SPI/Command/Stream、中部 SDRAM/Frame Buffer、顶部视频与 TMDS 链路

### FPGA 功能分区

FPGA 虚线边界包含视频、帧缓冲、流式读写、命令、SPI、AXI/SDRAM 控制与 PLL 功能；M5Atom、两枚晶振、HDMI Transceiver IC、HDMI Connector 和 Embedded SDRAM 以硬件方框表示。

- 参数与网络：`boundary=FPGA...`；`external_controller=M5Atom`；`external_video_ic=HDMI Transceiver IC`；`external_memory=Embedded SDRAM`
- 证据：图 0d5a11986a3c / 第 1 页 / 整页最外层 FPGA... 虚线框、各子时钟域虚线框与紫/绿/蓝灰图例

### 框图颜色图例

图例把绿色方框标为 Chisel part、紫色方框标为 Hardware、蓝灰色方框标为 GOWIN IP。

- 参数与网络：`green=Chisel part`；`purple=Hardware`；`blue_gray=GOWIN IP`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右上图例：Chisel part、Hardware、GOWIN IP

## 核心器件

### 物理器件标识可见性

当前页面没有显示物理位号，也没有给出 M5Atom、HDMI Transceiver IC、Embedded SDRAM 或两枚晶振的具体料号。

- 参数与网络：`reference_designators_shown=false`；`physical_part_numbers_shown=false`
- 证据：图 0d5a11986a3c / 第 1 页 / 整页紫色硬件方框只显示功能名称，未见 U/J/Y 等位号或具体型号

## 电源

### 电源拓扑可见性

当前页面是系统框图，没有显示电源输入、电压轨、稳压器、负载开关、使能或保护器件。

- 参数与网络：`power_input_shown=false`；`rails_shown=false`；`regulators_shown=false`；`protection_shown=false`
- 证据：图 0d5a11986a3c / 第 1 页 / 整页框图仅显示功能、数据总线和时钟域，未见电源网络或电源器件

## 接口

### M5Atom 到 FPGA 的 SPI 接口

M5Atom 通过标注 SPI 的连接进入 FPGA 的 SPI Clock... 区域，并连接 SPI Slave。

- 参数与网络：`source=M5Atom`；`destination=SPI Slave`；`bus=SPI`；`clock_domain=SPI Clock...`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面底部 M5Atom 向上到 SPI Slave 的竖直连线，两处均标注 SPI

### TMDS 输出

HDMI Transceiver IC 向 HDMI Connector 输出标注 TMDS 的信号。

- 参数与网络：`source=HDMI Transceiver IC`；`destination=HDMI Connector`；`signal=TMDS`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面顶部 HDMI Transceiver IC 到 HDMI Connector 的向上箭头，旁标 TMDS

## 总线

### M5Atom 到 HDMI Transceiver IC 的 I2C

M5Atom 通过页面右侧回路连接 HDMI Transceiver IC，回路两端均标注 I2C。

- 参数与网络：`controller=M5Atom`；`device=HDMI Transceiver IC`；`bus=I2C`；`address=null`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面最右侧从 M5Atom 绕行到 HDMI Transceiver IC 的 I2C 连线

### SPI Slave 命令通道

SPI Slave 与 Command... 方框之间是双向连接，连线标注 Command...。

- 参数与网络：`endpoint_a=SPI Slave`；`endpoint_b=Command...`；`signal=Command...`；`direction=bidirectional`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右中下 Command... 与 SPI Slave 之间的上下双箭头

### Stream Writer AXI4 连接

Stream Writer 通过标注 AXI4 的连线连接中央 AXI4 汇聚通路。

- 参数与网络：`client=Stream Writer`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央偏右 Stream Writer 左侧至绿色梯形符号的连线，标注 AXI4

### Stream Reader AXI4 连接

Stream Reader 通过标注 AXI4 的连线连接中央 AXI4 汇聚通路。

- 参数与网络：`client=Stream Reader`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央偏右 Stream Reader 左侧至绿色梯形符号的连线，标注 AXI4

### Frame Buffer Reader AXI4 连接

Frame Buffer Reader 通过竖直 AXI4 连线连接中央 AXI4 汇聚通路。

- 参数与网络：`client=Frame Buffer Reader`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央 Frame Buffer Reader 下方竖直连线至绿色梯形符号，旁标 AXI4

## 时钟

### 视频时钟晶振输入

页面左上第一枚 Crystal... 通过箭头进入 Video Clock... 虚线时钟域。

- 参数与网络：`source=Crystal (Video Clock)`；`clock_domain=Video Clock...`；`frequency=null`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面左上第一枚 Crystal... 到 Video Clock... 虚线框的水平箭头

### GOWIN PLL 晶振输入

页面左侧第二枚 Crystal... 连接 GOWIN PLL 输入。

- 参数与网络：`source=Crystal (PLL input)`；`destination=GOWIN PLL`；`frequency=null`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面左侧第二枚 Crystal... 向下再向右进入 GOWIN PLL 的箭头

### 70 MHz 主时钟

GOWIN PLL 的一条输出进入 Main Clock... 虚线时钟域，旁边标注 70[MHz]。

- 参数与网络：`source=GOWIN PLL`；`clock_domain=Main Clock...`；`frequency_mhz=70`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面左中 GOWIN PLL 右下输出到 Main Clock... 虚线框，支路旁标注 70[MHz]

### 140 MHz SDRAM 时钟

GOWIN PLL 的另一条输出进入 SDRAM Clock... 虚线时钟域，旁边标注 140[MHz]。

- 参数与网络：`source=GOWIN PLL`；`clock_domain=SDRAM Clock...`；`frequency_mhz=140`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面左下 GOWIN PLL 输出沿左侧下行进入 SDRAM Clock... 虚线框，旁标 140[MHz]

### 视频时钟域跨越

Async FIFO 位于 Main Clock... 与 Video Clock... 区域之间的视频通路上，连接 Frame Buffer Reader 和 Video Signal Generator。

- 参数与网络：`source_domain=Main Clock...`；`destination_domain=Video Clock...`；`crossing_block=Async FIFO`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央 Frame Buffer Reader、Async FIFO、Video Signal Generator 及两层虚线时钟域边界

### SPI 时钟域

SPI Slave 单独位于标注 SPI Clock... 的虚线区域内，并由 M5Atom 的 SPI 连接进入。

- 参数与网络：`clock_domain=SPI Clock...`；`block=SPI Slave`；`external_source=M5Atom`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右下 SPI Clock... 虚线框、其中的 SPI Slave 与下方 M5Atom SPI 连线

## 关键网络

### Stream Writer 命令控制

Command... 方框向 Stream Writer 提供一条标注 Command 的控制连接。

- 参数与网络：`source=Command...`；`destination=Stream Writer`；`signal=Command`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右中 Command... 左上支路到 Stream Writer，支路旁标注 Command

### Stream Reader 命令控制

Command... 方框向 Stream Reader 提供另一条标注 Command 的控制连接。

- 参数与网络：`source=Command...`；`destination=Stream Reader`；`signal=Command`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右中 Command... 右上支路绕行至 Stream Reader 底部，支路旁标注 Command

### Stream Reader 像素数据回路

Stream Reader 的右侧回路标注 Pixel Data，并指向 Command... 方框。

- 参数与网络：`source=Stream Reader`；`destination=Command...`；`signal=Pixel Data`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面右中 Stream Reader 右侧向下回路，标注 Pixel Data，箭头进入 Command... 右侧

### 帧缓冲视频数据

Frame Buffer Reader 向上输出一条标注 Video... 的连接到 Async FIFO。

- 参数与网络：`source=Frame Buffer Reader`；`destination=Async FIFO`；`visible_signal_label=Video...`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中部 Frame Buffer Reader 到 Async FIFO 的向上箭头，旁标 Video...

### 异步 FIFO 视频输出

Async FIFO 的输出向上进入 Video Signal Generator。

- 参数与网络：`source=Async FIFO`；`destination=Video Signal Generator`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中上部 Async FIFO 到 Video Signal Generator 的向上箭头

### 视频发生器到转换芯片

Video Signal Generator 通过一条标注 Video... 的向上连接进入 HDMI Transceiver IC。

- 参数与网络：`source=Video Signal Generator`；`destination=HDMI Transceiver IC`；`visible_signal_label=Video...`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面上部 Video Signal Generator 到 HDMI Transceiver IC 的向上箭头，旁标 Video...

## 内存与 Flash

### AXI4 到 SDRAM 控制桥

中央 AXI4 汇聚通路通过双向 AXI4 连接 AXI SDRAM Controller B...。

- 参数与网络：`upstream=AXI4 interconnect (unlabeled)`；`bridge=AXI SDRAM Controller B...`；`bus=AXI4`；`direction=bidirectional`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央绿色梯形符号与 AXI SDRAM Controller B... 之间的上下双箭头，标注 AXI4

### SDRAM 控制器链路

AXI SDRAM Controller B... 与 SDRAM Controller 之间是双向连接，连线标签在图中显示为 SDRC s...。

- 参数与网络：`endpoint_a=AXI SDRAM Controller B...`；`endpoint_b=SDRAM Controller`；`visible_signal_label=SDRC s...`；`direction=bidirectional`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面中央偏下 AXI SDRAM Controller B... 与 SDRAM Controller 之间的上下双箭头

### Embedded SDRAM 接口

SDRAM Controller 与 Embedded SDRAM 之间是双向连接，框图在该通路旁标出 SDRAM... 和 Up to 280[MB/...。

- 参数与网络：`controller=SDRAM Controller`；`memory=Embedded SDRAM`；`visible_bus_label=SDRAM...`；`visible_throughput_label=Up to 280[MB/...`；`direction=bidirectional`
- 证据：图 0d5a11986a3c / 第 1 页 / 页面下部 SDRAM Controller 与 Embedded SDRAM 之间的上下双箭头及相邻截断标签

## 其他事实

### GPIO、地址和复位信息可见性

当前页面没有显示 SPI/I2C 的引脚号、HDMI Transceiver IC 的 I2C 地址、复位网络、启动模式或调试接口。

- 参数与网络：`gpio_shown=false`；`i2c_address_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_shown=false`
- 证据：图 0d5a11986a3c / 第 1 页 / 整页框图的接口只标注 SPI、I2C、AXI4、TMDS 等总线名称，未见引脚、地址、复位或调试标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 端到端视频路径 | `controller=M5Atom`；`input_bus=SPI`；`memory=Embedded SDRAM`；`output_signal=TMDS`；`output_connector=HDMI Connector` |
| 系统结构 | FPGA 功能分区 | `boundary=FPGA...`；`external_controller=M5Atom`；`external_video_ic=HDMI Transceiver IC`；`external_memory=Embedded SDRAM` |
| 系统结构 | 框图颜色图例 | `green=Chisel part`；`purple=Hardware`；`blue_gray=GOWIN IP` |
| 接口 | M5Atom 到 FPGA 的 SPI 接口 | `source=M5Atom`；`destination=SPI Slave`；`bus=SPI`；`clock_domain=SPI Clock...` |
| 总线 | M5Atom 到 HDMI Transceiver IC 的 I2C | `controller=M5Atom`；`device=HDMI Transceiver IC`；`bus=I2C`；`address=null` |
| 总线 | SPI Slave 命令通道 | `endpoint_a=SPI Slave`；`endpoint_b=Command...`；`signal=Command...`；`direction=bidirectional` |
| 关键网络 | Stream Writer 命令控制 | `source=Command...`；`destination=Stream Writer`；`signal=Command` |
| 关键网络 | Stream Reader 命令控制 | `source=Command...`；`destination=Stream Reader`；`signal=Command` |
| 关键网络 | Stream Reader 像素数据回路 | `source=Stream Reader`；`destination=Command...`；`signal=Pixel Data` |
| 总线 | Stream Writer AXI4 连接 | `client=Stream Writer`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)` |
| 总线 | Stream Reader AXI4 连接 | `client=Stream Reader`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)` |
| 总线 | Frame Buffer Reader AXI4 连接 | `client=Frame Buffer Reader`；`bus=AXI4`；`peer=AXI4 interconnect (unlabeled)` |
| 内存与 Flash | AXI4 到 SDRAM 控制桥 | `upstream=AXI4 interconnect (unlabeled)`；`bridge=AXI SDRAM Controller B...`；`bus=AXI4`；`direction=bidirectional` |
| 内存与 Flash | SDRAM 控制器链路 | `endpoint_a=AXI SDRAM Controller B...`；`endpoint_b=SDRAM Controller`；`visible_signal_label=SDRC s...`；`direction=bidirectional` |
| 内存与 Flash | Embedded SDRAM 接口 | `controller=SDRAM Controller`；`memory=Embedded SDRAM`；`visible_bus_label=SDRAM...`；`visible_throughput_label=Up to 280[MB/...`；`direction=bidirectional` |
| 关键网络 | 帧缓冲视频数据 | `source=Frame Buffer Reader`；`destination=Async FIFO`；`visible_signal_label=Video...` |
| 关键网络 | 异步 FIFO 视频输出 | `source=Async FIFO`；`destination=Video Signal Generator` |
| 关键网络 | 视频发生器到转换芯片 | `source=Video Signal Generator`；`destination=HDMI Transceiver IC`；`visible_signal_label=Video...` |
| 接口 | TMDS 输出 | `source=HDMI Transceiver IC`；`destination=HDMI Connector`；`signal=TMDS` |
| 时钟 | 视频时钟晶振输入 | `source=Crystal (Video Clock)`；`clock_domain=Video Clock...`；`frequency=null` |
| 时钟 | GOWIN PLL 晶振输入 | `source=Crystal (PLL input)`；`destination=GOWIN PLL`；`frequency=null` |
| 时钟 | 70 MHz 主时钟 | `source=GOWIN PLL`；`clock_domain=Main Clock...`；`frequency_mhz=70` |
| 时钟 | 140 MHz SDRAM 时钟 | `source=GOWIN PLL`；`clock_domain=SDRAM Clock...`；`frequency_mhz=140` |
| 时钟 | 视频时钟域跨越 | `source_domain=Main Clock...`；`destination_domain=Video Clock...`；`crossing_block=Async FIFO` |
| 时钟 | SPI 时钟域 | `clock_domain=SPI Clock...`；`block=SPI Slave`；`external_source=M5Atom` |
| 电源 | 电源拓扑可见性 | `power_input_shown=false`；`rails_shown=false`；`regulators_shown=false`；`protection_shown=false` |
| 核心器件 | 物理器件标识可见性 | `reference_designators_shown=false`；`physical_part_numbers_shown=false` |
| 其他事实 | GPIO、地址和复位信息可见性 | `gpio_shown=false`；`i2c_address_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_shown=false` |

## 待确认事项

- `review.physical_schematic_required`：是否有 Atom Display-Lite 对应硬件版本的完整电路原理图或网表，可用于确认物理位号、芯片料号、引脚、电源与保护电路？；原因：当前唯一资源是系统框图，无法从该页完成器件级和网络级核对。
- `review.truncated_labels`：能否提供未截断的原始框图，以确认 AXI SDRAM Controller B...、Command...、SDRC s...、Video... 等标签的完整名称？；原因：当前图片中的多个模块名和网络名以省略号显示，不能安全还原完整文本。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0d5a11986a3c2cf0d6c41bafeac81b18220623b371e82ed2ff6dc4711c8c1242` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_sch_03.webp` |

---

源文档：`zh_CN/atom/atom_display_lite.md`

源文档 SHA-256：`107059a77ed22aa30a89ef0fdc914fd96782498e1fc28e4a785b8241ea1129ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
