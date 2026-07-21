# Atom-Matrix 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom-Matrix |
| SKU | C008-B |
| 产品 ID | `atom-matrix-3eb9fc4ccc03` |
| 源文档 | `zh_CN/core/ATOM Matrix.md` |

## 概述

Atom-Matrix 的现有资源是一页功能框图：ESP32-PICO 连接 5x5 WS2812-2020 矩阵、MPU-6886、复位/用户按键、Grove、G21 扩展连接器和 USB-UART 自动下载。USB Type-C 的电源经二极管和 5V→3.3V DC-DC 为系统供电，DM/DP 进入 USB 2 UART；MPU-6886 通过 SDA/SCL 连接主控，图中直接标出地址 0x68。框图未给出位号、ESP32 完整后缀、USB-UART/DC-DC 料号、红外、天线、阻容参数或完整保护，不能据此确认器件级 BOM 和电气性能。

## 检索关键词

`Atom-Matrix`、`C008-B`、`M5 ATOM Matrix`、`ESP32-PICO`、`ESP32-PICO-D4`、`MPU-6886`、`0x68`、`WS2812-2020`、`5X5 Matrix`、`GPIO27`、`GPIO39`、`GPIO32`、`GPIO26`、`GPIO21`、`GPIO25`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO34`、`G33`、`USB Type-C`、`USB 2 UART`、`Auto Download`、`DM`、`DP`、`RESET`、`GPIO0`、`GPIO1`、`GPIO3`、`SDA`、`SCL`、`GROVE`、`G21 Connector`、`5V`、`3.3V`、`DC-DC`、`0.5A Fuse`、`100Ω`、`RGB Matrix`、`User Button`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ESP32-PICO block | ESP32-PICO | 中央主控功能块，连接按键、RGB、IMU、USB-UART、Grove 和扩展连接器 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页中央橙色 ESP32-PICO 功能块及周围箭头 |
| MPU-6886 block | MPU-6886 | 地址标为 0x68 的 I2C IMU 功能块 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页右上黄色 MPU-6886 IMU Addr:0x68 功能块，连接 SDA/SCL/GND |
| 5X5 Matrix block | WS2812-2020 | 5x5 可寻址 RGB LED 矩阵，连接 GPIO27、5V 和 GND | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左中蓝色 5X5 WS2812-2020 Matrix 功能块 |
| USB Type-C block | 未标注 | 提供电源、DM、DP 和 GND 的 USB Type-C 接口 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左下蓝色 USB Type-C 功能块与 Diode/DM/DP/GND |
| USB 2 UART & Auto Download block | 未标注 | 把 USB DM/DP 转为 ESP32 EN/GPIO0/TXD(GPIO1)/RXD(GPIO3) 下载与串口信号 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左下黄色 USB 2 UART & Auto Download 功能块 |
| DC-DC block | 未标注 | 将 USB/Grove 5V 电源转换为 3.3V 供给 ESP32-PICO | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左下黄色 DC-DC 5V To 3.3V 功能块 |
| GROVE block | 未标注 | 引出 GPIO32、GPIO26、5V 和 GND 的四线扩展接口 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左中 GROVE 功能块，GPIO32/GPIO26/5V/GND |
| G21 Connector block | 未标注 | 顶视图扩展连接器，引出 G21/G25/5V/GND/3V3/G22/G19/G23/G33 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页右下蓝色 G21 Connector (Top view) 功能块 |
| Reset Button block | 未标注 | 连接 RESET 网络的复位按键 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左上 Reset Button 到 RESET 的绿色网络 |
| User Button block | 未标注 | GPIO39 对 GND 的用户按键 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页左上 User Button，GPIO39/GND |
| Fuse/Diode blocks | 0.5A Fuse / Diode | Grove 5V 支路保险和 USB 电源路径二极管功能块 | 图 a54e7dd921c6 / 第 1 页 / 第 1 页 Grove 5V 下方 0.5A FUSE 与 USB Type-C 右侧 Diode |

## 系统结构

### Atom-Matrix 功能框图架构

ESP32-PICO 功能块连接 Reset Button、GPIO39 User Button、GPIO27 5x5 WS2812-2020 Matrix、MPU-6886 SDA/SCL、GPIO32/GPIO26 Grove、G21 Connector 和 USB 2 UART & Auto Download；USB/Grove 5V 经 DC-DC 生成 3.3V。

- 参数与网络：`diagram_type=functional block diagram`；`controller=ESP32-PICO`；`imu=MPU-6886`；`rgb=5X5 WS2812-2020`；`usb=USB Type-C -> USB 2 UART`；`power=5V -> DC-DC -> 3.3V`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页完整 M5 ATOM Matrix 功能框图

## 电源

### 5V 到 3.3V 电源路径

USB Type-C 电源经 Diode 进入 5V 电源网络，Grove 的 5V 支路串有 0.5A FUSE；5V 进入 DC-DC 5V To 3.3V 功能块，其 3.3V 输出连接 ESP32-PICO、MPU-6886 和扩展连接器 3V3。

- 参数与网络：`usb_path=USB Type-C -> Diode -> 5V`；`grove_protection=0.5A FUSE`；`converter=DC-DC 5V To 3.3V`；`output=3.3V`；`loads=ESP32-PICO,MPU-6886,G21 Connector 3V3`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左下 USB/Diode/DC-DC 与 Grove 0.5A Fuse、蓝色 3.3V 网络

## 接口

### Grove 接口映射

GROVE 功能块的四条网络依次标为 GPIO32、GPIO26、5V 和 GND；GPIO32/GPIO26 连接 ESP32-PICO，5V 支路包含 0.5A FUSE。

- 参数与网络：`signal1=GPIO32`；`signal2=GPIO26`；`power=5V via 0.5A FUSE`；`ground=GND`；`signal_direction=GPIO configurable`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左中 GROVE 方框与 GPIO32/GPIO26/5V/GND、0.5A FUSE

### G21 扩展连接器

G21 Connector (Top view) 功能块左侧标 G21、G25、5V、G，右侧标 3V3、G22、G19、G23、G33；外部网络分别标 GPIO21、GPIO25、GPIO22、GPIO19、GPIO23，底部 G33 路径与 GPIO34 侧网络及 100Ω 器件相连。

- 参数与网络：`left=G21 GPIO21,G25 GPIO25,5V,GND`；`right=3V3,G22 GPIO22,G19 GPIO19,G23 GPIO23,G33`；`g33_path=shown connected toward GPIO34 through 100Ω`；`view=top view`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页右下 G21 Connector (Top view) 与右侧 GPIO22/19/23/34、100Ω

## 总线

### USB-UART 与自动下载

USB Type-C 的 DM/DP 进入 USB 2 UART & Auto Download 功能块，该功能块向 ESP32-PICO 提供 EN、GPIO0、TXD(GPIO1) 和 RXD(GPIO3) 信号。

- 参数与网络：`usb_data=DM,DP`；`bridge=USB 2 UART & Auto Download`；`reset=EN`；`boot=GPIO0`；`uart_tx=GPIO1`；`uart_rx=GPIO3`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左下 USB Type-C、DM/DP、USB 2 UART & Auto Download 到 ESP32-PICO

### MPU-6886 I2C 连接

MPU-6886 功能块通过 SDA 与 SCL 两条网络连接 ESP32-PICO，并连接 3.3V 电源网络与 GND。

- 参数与网络：`controller=ESP32-PICO`；`device=MPU-6886`；`bus=I2C`；`signals=SDA,SCL`；`supply=3.3V`；`ground=GND`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页右上 MPU-6886 与 SDA/SCL、蓝色电源线和 GND

## 总线地址

### MPU-6886 I2C 地址

功能框图在 MPU-6886 模块内直接标注 IMU Addr:0x68。

- 参数与网络：`device=MPU-6886`；`seven_bit_address=0x68`；`bus=I2C`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页右上黄色 MPU-6886 IMU Addr:0x68 文本

## GPIO 与控制信号

### 用户按键

User Button 功能块连接 GPIO39 与 GND，按键输入由 ESP32-PICO 的 GPIO39 读取。

- 参数与网络：`gpio=GPIO39`；`other_terminal=GND`；`direction=input`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左上 User Button 的 GPIO39/GND 两线

### 5x5 RGB LED 矩阵

5X5 WS2812-2020 Matrix 功能块由 5V/GND 供电，数据控制网络为 GPIO27，并连接 ESP32-PICO。

- 参数与网络：`matrix=5x5`；`part_label=WS2812-2020`；`count=25`；`data_gpio=GPIO27`；`supply=5V`；`ground=GND`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左中 5X5 WS2812-2020 Matrix 与 GPIO27/5V/GND

## 复位

### 复位按键路径

Reset Button 功能块输出 RESET 网络，RESET 直接进入 ESP32-PICO 功能块。

- 参数与网络：`button=Reset Button`；`net=RESET`；`target=ESP32-PICO`
- 证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左上 Reset Button、RESET 绿色网络和向下箭头

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom-Matrix 功能框图架构 | `diagram_type=functional block diagram`；`controller=ESP32-PICO`；`imu=MPU-6886`；`rgb=5X5 WS2812-2020`；`usb=USB Type-C -> USB 2 UART`；`power=5V -> DC-DC -> 3.3V` |
| 电源 | 5V 到 3.3V 电源路径 | `usb_path=USB Type-C -> Diode -> 5V`；`grove_protection=0.5A FUSE`；`converter=DC-DC 5V To 3.3V`；`output=3.3V`；`loads=ESP32-PICO,MPU-6886,G21 Connector 3V3` |
| 总线 | USB-UART 与自动下载 | `usb_data=DM,DP`；`bridge=USB 2 UART & Auto Download`；`reset=EN`；`boot=GPIO0`；`uart_tx=GPIO1`；`uart_rx=GPIO3` |
| 复位 | 复位按键路径 | `button=Reset Button`；`net=RESET`；`target=ESP32-PICO` |
| GPIO 与控制信号 | 用户按键 | `gpio=GPIO39`；`other_terminal=GND`；`direction=input` |
| GPIO 与控制信号 | 5x5 RGB LED 矩阵 | `matrix=5x5`；`part_label=WS2812-2020`；`count=25`；`data_gpio=GPIO27`；`supply=5V`；`ground=GND` |
| 总线 | MPU-6886 I2C 连接 | `controller=ESP32-PICO`；`device=MPU-6886`；`bus=I2C`；`signals=SDA,SCL`；`supply=3.3V`；`ground=GND` |
| 总线地址 | MPU-6886 I2C 地址 | `device=MPU-6886`；`seven_bit_address=0x68`；`bus=I2C` |
| 接口 | Grove 接口映射 | `signal1=GPIO32`；`signal2=GPIO26`；`power=5V via 0.5A FUSE`；`ground=GND`；`signal_direction=GPIO configurable` |
| 接口 | G21 扩展连接器 | `left=G21 GPIO21,G25 GPIO25,5V,GND`；`right=3V3,G22 GPIO22,G19 GPIO19,G23 GPIO23,G33`；`g33_path=shown connected toward GPIO34 through 100Ω`；`view=top view` |
| 核心器件 | ESP32-PICO 完整型号 | `diagram_label=ESP32-PICO`；`documented_part=ESP32-PICO-D4`；`reference=null`；`package=null` |
| 内存与 Flash | Flash 与 SRAM 容量 | `documented_flash=4MB SPI Flash`；`documented_sram=520KB`；`memory_component=null`；`memory_bus=null` |
| 核心器件 | DC-DC 与 USB-UART 料号 | `dc_dc_part=null`；`usb_uart_part=null`；`reference_designators=null`；`auto_download_circuit=null` |
| 射频 | 2.4GHz 天线与射频 | `documented_radio=2.4GHz Wi-Fi`；`documented_antenna=2.4G 3D antenna`；`antenna_reference=null`；`matching_network=null`；`rf_test_point=null` |
| 其他事实 | 红外发射实现 | `documented_gpio=GPIO12`；`documented_function=IR_TX`；`ir_led=null`；`driver=null`；`resistor=null` |
| 电源 | 供电能力与 RGB 热边界 | `visible_fuse=0.5A`；`documented_input=5V@500mA`；`dc_dc_current=null`；`led_current=null`；`full_brightness_power=null`；`temperature_rise=null` |

## 待确认事项

- `component.esp32-exact-variant`：框图中央只标 ESP32-PICO，正文称 ESP32-PICO-D4；现有资源没有器件位号、完整后缀、封装或芯片丝印，无法由图面确认 D4 后缀。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页中央仅标 ESP32-PICO）
- `memory.documented-flash-sram`：正文列出 4MB SPI Flash 和 520KB SRAM；功能框图没有存储器模块、容量字段、SPI Flash 总线或内存位号，因此这些容量不能由本页独立验证。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页完整框图无存储器或容量标注）
- `component.power-usb-ic-models`：图中只显示 DC-DC 5V To 3.3V 和 USB 2 UART & Auto Download 功能块，没有位号、芯片型号、反馈/时序网络或封装。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页左下两个黄色功能块，无料号/位号）
- `rf.antenna-implementation`：正文称 2.4G 3D 天线和 Wi-Fi，功能框图没有天线、射频匹配、射频引脚、测试点或认证参数，无法确认具体天线实现。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页完整框图无天线或射频网络）
- `other.ir-implementation`：正文管脚表称 GPIO12 用于 IR_TX，但功能框图未显示红外发射管、驱动晶体管、限流电阻、保护器件或 GPIO12 网络。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页完整框图无 IR 或 GPIO12 标注）
- `power.electrical-thermal-limits`：框图只标 0.5A Fuse、5V 和 3.3V，未给出 USB 输入电流、DC-DC 输出能力、效率、纹波、LED 单颗电流、矩阵全亮功耗或温升；正文的 5V@500mA 与亮度/温度限制需由 BOM 和实测确认。（证据：图 a54e7dd921c6 / 第 1 页 / 第 1 页 Grove/USB/DC-DC 与 5X5 Matrix 功能块，图中无性能参数）
- `review.esp32-variant`：C008-B 当前 BOM 的主控完整型号是否为 ESP32-PICO-D4，封装和丝印是什么？；原因：框图只标 ESP32-PICO。
- `review.memory-capacity`：请用 ESP32-PICO-D4 datasheet 或实机确认 4MB Flash 与 520KB SRAM。；原因：本页没有存储器或容量标注。
- `review.power-usb-bom`：DC-DC、USB-UART 和自动下载电路的完整料号、位号及连接是什么？；原因：现有资源只有抽象功能块。
- `review.rf-antenna`：Atom-Matrix 的 2.4GHz 天线类型、匹配网络、布局和射频测试结果是什么？；原因：框图未展示射频电路。
- `review.ir-circuit`：请提供 GPIO12 红外发射的 LED、驱动、限流和保护电路。；原因：正文列出 IR_TX，但框图完全未显示。
- `review.power-thermal`：请确认 DC-DC 输出能力、LED 单颗/矩阵电流、全亮功耗、推荐亮度和外壳温升边界。；原因：功能框图没有器件参数和热测试数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a54e7dd921c64c85d3112f7ad819efca373861fda68a43699499b8b28ed3bbf3` | `https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-fa9922b3-727d-4598-8d16-84611248a3c6.webp` |

---

源文档：`zh_CN/core/ATOM Matrix.md`

源文档 SHA-256：`c1f363ac3b51f1cea5c91d150b7f7c7a3ab839e76855d4efc5e52539569b15be`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
