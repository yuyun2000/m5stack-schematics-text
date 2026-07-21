# Unit UHF-RFID 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit UHF-RFID |
| SKU | U107 |
| 产品 ID | `unit-uhf-rfid-e13e5fc00641` |
| 源文档 | `zh_CN/unit/uhf_rfid.md` |

## 概述

Unit UHF-RFID 的单页原理图只展开射频模块侧 P1 五针排针与主机侧 J1 HY2.0 UART 接口。P1 TXD/RXD 分别交叉连接 J1 RX/TX，两个接口共享 +5V 和 GND；P1 EN 由 R1 10K 上拉至 +5V，C1 100nF 与 C2 22uF 跨接在 +5V 与 GND 之间。图面没有 JRD-4035 模块内部、陶瓷天线、射频链路或固件协议，因此频段、功率、距离、空中协议、UART 参数、标签缓存和机械规格仍需结合正式模块资料确认。

## 检索关键词

`Unit UHF-RFID`、`U107`、`UHF RFID`、`JRD-4035`、`840-960MHz`、`922MHz`、`18-26dBm`、`EPCglobal UHF Class 1 Gen 2`、`ISO/IEC 18000-6C`、`UART`、`115200bps`、`HY2.0-4P`、`PORT.C`、`Header 5`、`P1`、`J1`、`TXD`、`RXD`、`EN`、`+5V`、`R1 10K`、`C1 100nF`、`C2 22uF`、`ceramic antenna`、`200 tags`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 5 | 射频模块侧的 +5V、TXD、RXD、EN、GND 五针连接器 | 图 1ab6b15636fa / 第 1 页 / 左侧 P1 Header 5 pins1-5 |
| J1 | HY-2.0_UART | 主机侧 +5V、GND 与 UART RX/TX 四针接口 | 图 1ab6b15636fa / 第 1 页 / 中右 J1 HY-2.0_UART pins1-4 |
| R1 | 10Kohm | P1 EN 到 +5V 的上拉电阻 | 图 1ab6b15636fa / 第 1 页 / P1 pin2 EN 右侧 R1 10Kohm |
| C1,C2 | 100nF / 22uF | 跨接 +5V 与 GND 的电容 | 图 1ab6b15636fa / 第 1 页 / 右侧 +5V 到 GND 的 C1 100nF 与 C2 22uF |

## 电源

### +5V 与 GND 分配

+5V 网络连接 P1 pin5 VCC、J1 pin3 VCC、R1 上拉端以及 C1/C2 上端；P1 pin1、J1 pin4 与 C1/C2 下端均接 GND。

- 参数与网络：`supply=+5V`；`supply_pins=P1.5,J1.3`；`ground_pins=P1.1,J1.4`；`decoupling=C1,C2`
- 证据：图 1ab6b15636fa / 第 1 页 / +5V 与 GND 电源符号及 P1/J1/C1/C2 网络

### +5V 对地电容

C1 100nF 与 C2 22uF 均跨接在 +5V 与 GND 之间。

- 参数与网络：`rail=+5V`；`capacitor_1=C1 100nF`；`capacitor_2=C2 22uF`
- 证据：图 1ab6b15636fa / 第 1 页 / 右侧 C1 100nF、C2 22uF 与 +5V/GND

## 接口

### P1 五针模块接口

P1 标为 Header 5，pin5 为 VCC 并接 +5V，pin4 为 TXD，pin3 为 RXD，pin2 为 EN，pin1 为 GND。

- 参数与网络：`connector=P1 Header 5`；`pin5=VCC/+5V`；`pin4=TXD`；`pin3=RXD`；`pin2=EN`；`pin1=GND`
- 证据：图 1ab6b15636fa / 第 1 页 / 左侧 P1 Header 5 pins1-5

### J1 HY2.0 UART 接口

J1 标为 HY-2.0_UART，pin1 为 RX，pin2 为 TX，pin3 为 VCC 并接 +5V，pin4 为 GND。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pin1=RX`；`pin2=TX`；`pin3=VCC/+5V`；`pin4=GND`
- 证据：图 1ab6b15636fa / 第 1 页 / 中右 J1 HY-2.0_UART pins1-4

## 总线

### P1 与 J1 的 UART 交叉连接

P1 pin4 TXD 直接连接 J1 pin1 RX，P1 pin3 RXD 直接连接 J1 pin2 TX。

- 参数与网络：`module_tx=P1.4 TXD`；`host_rx=J1.1 RX`；`module_rx=P1.3 RXD`；`host_tx=J1.2 TX`
- 证据：图 1ab6b15636fa / 第 1 页 / P1 TXD/RXD 到 J1 RX/TX 的两条水平网络

## 复位

### P1 EN 默认上拉

P1 pin2 EN 通过 R1 10Kohm 上拉到 +5V。

- 参数与网络：`enable_pin=P1.2 EN`；`pullup=R1 10Kohm`；`rail=+5V`
- 证据：图 1ab6b15636fa / 第 1 页 / P1 pin2 EN、R1 10Kohm 与 +5V

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 接口 | P1 五针模块接口 | `connector=P1 Header 5`；`pin5=VCC/+5V`；`pin4=TXD`；`pin3=RXD`；`pin2=EN`；`pin1=GND` |
| 接口 | J1 HY2.0 UART 接口 | `connector=J1 HY-2.0_UART`；`pin1=RX`；`pin2=TX`；`pin3=VCC/+5V`；`pin4=GND` |
| 总线 | P1 与 J1 的 UART 交叉连接 | `module_tx=P1.4 TXD`；`host_rx=J1.1 RX`；`module_rx=P1.3 RXD`；`host_tx=J1.2 TX` |
| 电源 | +5V 与 GND 分配 | `supply=+5V`；`supply_pins=P1.5,J1.3`；`ground_pins=P1.1,J1.4`；`decoupling=C1,C2` |
| 复位 | P1 EN 默认上拉 | `enable_pin=P1.2 EN`；`pullup=R1 10Kohm`；`rail=+5V` |
| 电源 | +5V 对地电容 | `rail=+5V`；`capacitor_1=C1 100nF`；`capacitor_2=C2 22uF` |
| 系统结构 | JRD-4035 UHF RFID 模块与陶瓷天线 | `documented_module=JRD-4035`；`documented_antenna=integrated ceramic antenna`；`schematic_boundary=P1 Header 5` |
| 射频 | UHF 频段、天线、功率、距离与空中协议 | `documented_band_mhz=840-960`；`documented_antenna_mhz=922`；`documented_output_dbm=18-26`；`documented_distance_m=1`；`documented_protocols=EPCglobal UHF Class 1 Gen 2,ISO/IEC 18000-6C` |
| 总线 | UART 波特率、AT 指令与标签缓存 | `documented_baud=115200`；`documented_command_set=AT`；`documented_tag_cache=200` |
| 系统结构 | 外壳、尺寸与重量 | `documented_material=Plastic PC`；`documented_product_size_mm=56.0x48.0x11.5`；`documented_product_weight_g=41.0`；`documented_package_size_mm=88.0x61.0x21.0`；`documented_gross_weight_g=58.8` |

## 待确认事项

- `system.documented-jrd4035-module`：源文档称 Unit UHF-RFID 采用 JRD-4035 模块方案并内置陶瓷天线；当前原理图只画到 P1 Header 5，没有 JRD-4035 型号、模块内部电路或天线连接。（证据：图 1ab6b15636fa / 第 1 页 / 左侧 P1 Header 5，页面无 JRD-4035 或天线图符）
- `rf.documented-band-power-protocol`：源文档称工作频谱为 840-960MHz、天线频率固定 922MHz、输出功率 18-26dBm、标称检测距离 1m，并支持 EPCglobal UHF Class 1 Gen 2 与 ISO/IEC 18000-6C；当前接口原理图没有 RF 收发器、匹配网络、天线或测试条件。（证据：图 1ab6b15636fa / 第 1 页 / 页面仅有 P1/J1 UART 与电源，无 RF 器件和天线）
- `bus.documented-uart-protocol`：源文档称 UART 默认波特率为 115200bps、模块封装 AT 指令集且标签缓存最多容纳 200 个标签；原理图仅确认 TXD/RXD 连线，不包含波特率、数据格式、命令集或缓存实现。（证据：图 1ab6b15636fa / 第 1 页 / P1 TXD/RXD 到 J1 RX/TX，仅显示物理网络）
- `system.documented-mechanical`：源文档称外壳为 Plastic PC，产品尺寸 56.0x48.0x11.5mm、重量 41.0g，包装尺寸 88.0x61.0x21.0mm、毛重 58.8g；当前电气原理图没有板框、外壳、机械公差或质量信息。（证据：图 1ab6b15636fa / 第 1 页 / 电气原理图无板框、外壳与机械尺寸）
- `review.jrd4035-module`：确认当前 U107 量产版本的 UHF 模块具体型号及内置陶瓷天线连接；原因：原理图只到 P1 接口，没有 JRD-4035 或天线图符。
- `review.rf-performance-protocol`：以 JRD-4035 正式规格和量产测试确认频段、922MHz 天线、输出功率、读取距离及空中协议；原因：当前图面没有 RF 器件、匹配网络、天线或测量条件。
- `review.uart-protocol`：确认 UART 帧格式、默认 115200bps、AT 指令版本与 200 标签缓存上限；原因：原理图只能确认 TXD/RXD 网络，不能确认软件协议和缓存。
- `review.mechanical`：确认当前量产外壳材质、56.0x48.0x11.5mm 外形与 41.0g 重量；原因：当前电气原理图没有外壳和机械信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1ab6b15636fa568a56d6457d30203e14aeb3ec7629af0dd0c5666a72a8da5110` | `https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_sch_01.webp` |

---

源文档：`zh_CN/unit/uhf_rfid.md`

源文档 SHA-256：`e679299aa582c74e9f977e559cc50e069dd75abc0c3789e21442bb984f8c4328`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
