# Hat Finger 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Finger |
| SKU | U074 |
| 产品 ID | `hat-finger-06fd21063c9c` |
| 源文档 | `zh_CN/hat/hat-finger.md` |

## 概述

Hat Finger 的本地电气资源只给出指纹模块与主机之间的 UART 方向：主机 G0 作为 TX 指向 Finger，Finger 返回信号由主机 G26 接收。另一份资源是机械尺寸图，未给出模块内部电路、器件位号、电源或完整连接器针脚。因而指纹传感器具体型号、UART 格式、供电和识别性能均需由模块 BOM/协议资料复核。

## 检索关键词

`Hat Finger`、`U074`、`FINGER`、`UART`、`TX`、`RX`、`G0`、`G26`、`M5StickC`、`FPC1020SC`、`FPC1020A`、`19200bps`、`8N1`、`指纹识别`、`电容式指纹`、`24mm`、`67mm`、`16mm sensor window`、`150 fingerprints`、`193Byte template`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| FINGER | 未标注 | UART 指纹识别模块；本地接口图未标具体料号 | 图 bf4ce7ac78c9 / 第 1 页 / 左侧 FINGER 模块图标与 TX/RX 信号 |
| HOST G0/G26 | M5StickC HAT UART interface | 主机侧 UART TX/RX 信号连接 | 图 bf4ce7ac78c9 / 第 1 页 / 右侧 G0/G26 括号与 TX/RX 方向箭头 |
| Fingerprint sensing window | 未标注 | 机械图中的圆形指纹感测窗口，标注直径 16 mm | 图 9862da56e393 / 第 1 页 / 正视图顶部圆形窗口，标注 Ø16 |

## 系统结构

### 模块接口架构

Hat Finger 作为独立指纹模块，通过两线 UART 与 StickC 主机通信；本地资源未展开模块内部处理、存储或电源电路。

- 参数与网络：`module=FINGER`；`host=M5StickC`；`interface=UART`；`signals=TX/G0; RX/G26`；`internal_circuit=not shown`
- 证据：图 bf4ce7ac78c9 / 第 1 页 / FINGER 到 G0/G26 的两条 TX/RX 连接

## 总线

### UART 信号映射

接口图标注 TX 使用主机 G0，箭头由主机指向 Finger；RX 使用主机 G26，箭头由 Finger 指向主机。

- 参数与网络：`host_tx=G0 -> FINGER`；`host_rx=G26 <- FINGER`；`direction=full-duplex UART signal pair`
- 证据：图 bf4ce7ac78c9 / 第 1 页 / 上方 TX 左向箭头/G0；下方 RX 右向箭头/G26

## GPIO 与控制信号

### 主机 GPIO 映射

主机 G0 用作发送方向信号，G26 用作接收方向信号。

- 参数与网络：`G0=UART TX from host`；`G26=UART RX to host`
- 证据：图 bf4ce7ac78c9 / 第 1 页 / G0/G26 与 TX/RX 标签

## 其他事实

### 机械图可见尺寸

机械图正视宽度标注 24 mm、总高标注 67 mm，指纹窗口标注直径 16 mm；侧视上部深度标注 20.7 mm。

- 参数与网络：`front_width=24mm`；`drawing_height=67mm`；`sensor_window=Ø16mm`；`upper_depth=20.7mm`；`unit=mm`
- 证据：图 9862da56e393 / 第 1 页 / 机械正视/侧视尺寸标注 24、67、Ø16、20.7，UNIT:mm

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 模块接口架构 | `module=FINGER`；`host=M5StickC`；`interface=UART`；`signals=TX/G0; RX/G26`；`internal_circuit=not shown` |
| 总线 | UART 信号映射 | `host_tx=G0 -> FINGER`；`host_rx=G26 <- FINGER`；`direction=full-duplex UART signal pair` |
| GPIO 与控制信号 | 主机 GPIO 映射 | `G0=UART TX from host`；`G26=UART RX to host` |
| 其他事实 | 机械图可见尺寸 | `front_width=24mm`；`drawing_height=67mm`；`sensor_window=Ø16mm`；`upper_depth=20.7mm`；`unit=mm` |
| 核心器件 | 指纹传感器型号 | `document_model=FPC1020SC`；`datasheet_name=FPC1020A`；`schematic_marking=not shown` |
| 总线 | UART 波特率与帧格式 | `claimed_default_baud=19200bps`；`claimed_range=9600-115200bps`；`claimed_format=1 start; 1 stop; no parity` |
| 电源 | 模块供电 | `supply_voltage=not shown`；`power_pins=not shown`；`regulator=not shown` |
| 接口 | 完整 HAT 针脚 | `confirmed_signals=G0 TX; G26 RX`；`missing=connector reference; GND; power; remaining pins` |
| 传感器 | 指纹容量与识别能力 | `claimed_capacity=150`；`claimed_template=193Byte`；`claimed_gray_levels=256`；`claimed_matching=1:N and 1:1`；`claimed_rotation=360 degrees`；`claimed_security_levels=0-9` |
| 其他事实 | 产品高度尺寸一致性 | `drawing_height=67mm`；`document_height=65mm`；`document_size=24x65x20mm` |

## 待确认事项

- `component.sensor-model`：产品正文称内部模组为 FPC1020SC，数据手册链接名称为 FPC1020A；本地接口图和机械图均未标传感器型号。（证据：图 bf4ce7ac78c9 / 第 1 页 / 接口图只标 FINGER; 图 9862da56e393 / 第 1 页 / 机械图无器件型号）
- `bus.uart-format`：本地接口图只标 TX/RX 和 G0/G26，未直接标注默认 19200 bps、1 个起始位、1 个停止位、无校验或 9600–115200 可配置范围。（证据：图 bf4ce7ac78c9 / 第 1 页 / TX/RX 接口图无波特率或帧格式文本）
- `power.interface`：两份本地资源均未显示 Hat Finger 的电源电压、供电引脚、稳压或去耦电路。（证据：图 bf4ce7ac78c9 / 第 1 页 / 接口图仅有 TX/RX; 图 9862da56e393 / 第 1 页 / 机械图无电源信息）
- `interface.full-pinout`：本地接口图只确认 G0/G26 UART 信号，未显示 StickIO 连接器位号、GND、电源或其余 HAT 引脚。（证据：图 bf4ce7ac78c9 / 第 1 页 / 右侧仅列 G0/G26）
- `sensor.capabilities`：本地资源未直接标注 150 枚指纹容量、193 字节模板、256 灰度、1:N/1:1、360° 识别或安全等级 0–9。（证据：图 bf4ce7ac78c9 / 第 1 页 / 接口图无功能参数; 图 9862da56e393 / 第 1 页 / 机械图无功能参数）
- `other.dimension-conflict`：机械图总高标注 67 mm，而产品正文尺寸写 24×65×20 mm，高度数值不一致，需确认量产外壳版本。（证据：图 9862da56e393 / 第 1 页 / 正视图左侧总高 67 mm）
- `review.sensor-model`：Hat Finger U074 实际指纹模组是 FPC1020SC、FPC1020A 还是其他型号？；原因：正文与数据手册名称不同，本地图纸未标型号。
- `review.uart-format`：请用 Finger 串口协议复核默认波特率、范围和帧格式。；原因：接口图只显示方向和 GPIO。
- `review.power-interface`：请提供电气原理图/BOM，确认模块供电电压、引脚与电源电路。；原因：现有资源无电源信息。
- `review.full-pinout`：请提供 StickIO 连接器电气图，确认电源、GND 与完整针脚顺序。；原因：本地接口图只列 G0/G26。
- `review.sensor-capabilities`：请用已确认模组 datasheet 复核容量、模板、灰度、识别模式和安全等级。；原因：这些性能参数未出现在本地资源。
- `review.dimension-conflict`：量产 Hat Finger 总高是机械图 67 mm 还是正文 65 mm？；原因：两处尺寸不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `bf4ce7ac78c9ddaeaf0ce236c419806255cbae477f982d1bfc74c5f465f53614` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_sch_01.webp` |
| 2 | 1 | `9862da56e3936e1dc2c31b592a0228b23b390c6fa08a67a06115108093d84ae5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/hatfinger_page_01.webp` |

---

源文档：`zh_CN/hat/hat-finger.md`

源文档 SHA-256：`db42f6b165ce8ceceb5028ee98393db99014d748e7c11004c8bea9fd2b46ea44`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
