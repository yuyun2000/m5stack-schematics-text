# Hat NeoFlash 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat NeoFlash |
| SKU | U071 |
| 产品 ID | `hat-neoflash-93d4a8411d1c` |
| 源文档 | `zh_CN/hat/hat-neoflash.md` |

## 概述

Hat NeoFlash 的本地资源显示 126 个 RGB 像素按编号 1 至 126 串联，数据从 StickIO G26 输入到第 1 个像素并沿链传递。灯链使用 StickIO 的 5VO 与 GND 供电，G36、G0、BAT、3V3 和 5V1 未接入该功能图。资源未展开像素内部器件、去耦或保护电路，也未直接标注 WS2812 料号和 7×18 物理排列。

## 检索关键词

`Hat NeoFlash`、`U071`、`126 RGB`、`RGB1-RGB126`、`G26`、`DATA`、`5VO`、`GND`、`STICKIO`、`WS2812`、`7x18 matrix`、`daisy chain`、`single-wire RGB`、`G36`、`G0`、`BAT`、`3V3`、`5V1`、`24-bit RGB`、`LED matrix`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| RGB1-RGB126 | 未标注 | 126 个串联可寻址 RGB 像素；资源未标具体器件型号 | 图 80b8ac7a8a9d / 第 1 页 / 左上 RGB 像素链，编号 1、2、…、125、126 |
| HAT interface | StickIO 8-pin | 提供 G26 数据、5VO 电源与 GND | 图 80b8ac7a8a9d / 第 1 页 / 右侧 8 针括号 GND/5VO/G26/G36/G0/BAT/3V3/5V1 |

## 系统结构

### RGB 灯链架构

Hat NeoFlash 由 126 个 RGB 像素组成单向串联数据链，第 1 个像素接收 G26 数据，数据依次传递到第 126 个像素。

- 参数与网络：`pixel_count=126`；`first_pixel=RGB1`；`last_pixel=RGB126`；`data_input=G26`；`topology=daisy chain`
- 证据：图 80b8ac7a8a9d / 第 1 页 / RGB1→RGB2→…→RGB125→RGB126 串联图

## 核心器件

### RGB 像素数量

功能图明确标出像素编号从 1 到 126，共 126 个 RGB 元件。

- 参数与网络：`count=126`；`references=RGB1-RGB126`
- 证据：图 80b8ac7a8a9d / 第 1 页 / 顶部编号 126、125、…、2、1

## 电源

### LED 灯链供电

RGB 灯链电源连接 StickIO 5VO，回流连接 GND。

- 参数与网络：`supply=5VO`；`return=GND`；`consumers=RGB1-RGB126`
- 证据：图 80b8ac7a8a9d / 第 1 页 / RGB1 供电/地线连接右侧 5VO/GND

## 接口

### StickIO 使用情况

功能图列出 GND、5VO、G26、G36、G0、BAT、3V3、5V1 八个 HAT 位置，其中仅 GND、5VO 与 G26 连接灯链。

- 参数与网络：`used=GND; 5VO; G26`；`unused=G36; G0; BAT; 3V3; 5V1`
- 证据：图 80b8ac7a8a9d / 第 1 页 / 右侧八项 StickIO 标签及连线

## 总线

### RGB 单线数据

G26 连接 RGB1 的数据输入，RGB1 输出连接 RGB2，后续像素同样逐级串接。

- 参数与网络：`controller_pin=G26`；`entry=RGB1`；`direction=G26 -> RGB1 -> RGB2 -> ... -> RGB126`
- 证据：图 80b8ac7a8a9d / 第 1 页 / G26 线连接 RGB1，像素之间三线串接

## GPIO 与控制信号

### 数据 GPIO

Hat NeoFlash 唯一使用的主机控制信号为 G26。

- 参数与网络：`data_gpio=G26`；`unused_gpio_labels=G36; G0`
- 证据：图 80b8ac7a8a9d / 第 1 页 / 右侧 G26 有连线，G36/G0 为短引脚无功能连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | RGB 灯链架构 | `pixel_count=126`；`first_pixel=RGB1`；`last_pixel=RGB126`；`data_input=G26`；`topology=daisy chain` |
| 核心器件 | RGB 像素数量 | `count=126`；`references=RGB1-RGB126` |
| 总线 | RGB 单线数据 | `controller_pin=G26`；`entry=RGB1`；`direction=G26 -> RGB1 -> RGB2 -> ... -> RGB126` |
| GPIO 与控制信号 | 数据 GPIO | `data_gpio=G26`；`unused_gpio_labels=G36; G0` |
| 电源 | LED 灯链供电 | `supply=5VO`；`return=GND`；`consumers=RGB1-RGB126` |
| 接口 | StickIO 使用情况 | `used=GND; 5VO; G26`；`unused=G36; G0; BAT; 3V3; 5V1` |
| 核心器件 | RGB 像素型号 | `document_model=WS2812`；`schematic_marking=RGB`；`count=126` |
| 接口 | 7×18 物理矩阵 | `confirmed_count=126`；`claimed_geometry=7x18`；`row_column_mapping=not shown` |
| 总线 | 像素数据协议 | `claimed_frame=24-bit RGB`；`claimed_channel_bits=8 bits per color`；`timing=not shown`；`color_order=not shown` |
| 电源 | 整板功耗与去耦 | `decoupling=not shown`；`protection=not shown`；`maximum_current=not shown`；`supply_net=5VO` |

## 待确认事项

- `component.pixel-model`：产品正文称灯珠为 WS2812，但本地功能图只标 RGB，未显示具体型号、封装或订货料号。（证据：图 80b8ac7a8a9d / 第 1 页 / 像素图标下只写 RGB）
- `interface.matrix-geometry`：功能图确认 126 个串联像素，但未画出产品正文所述 7×18 行列物理排列或像素编号到行列的映射。（证据：图 80b8ac7a8a9d / 第 1 页 / 资源只画一维 RGB1-RGB126 链）
- `bus.pixel-protocol`：本地资源未直接标注 24 位 RGB 帧格式、每色 8 位、时序、电平阈值或颜色顺序。（证据：图 80b8ac7a8a9d / 第 1 页 / G26 到 RGB 链无协议或时序文本）
- `power.current-decoupling`：功能图未显示每颗 RGB 的去耦电容、电源走线分配、限流/保险丝或 126 颗全亮时的最大电流。（证据：图 80b8ac7a8a9d / 第 1 页 / 简化功能图只显示 RGB 链、5VO、GND、G26）
- `review.pixel-model`：请用 BOM/PCB 确认 126 颗 RGB 的具体 WS2812 型号与封装。；原因：本地资源只写 RGB。
- `review.matrix-geometry`：请用 PCB/编号图确认 7×18 排列和 RGB1-RGB126 行列映射。；原因：功能图仅画一维串联链。
- `review.pixel-protocol`：请用确认后的像素 datasheet 复核 24 位帧、颜色顺序和时序。；原因：资源未标协议细节。
- `review.power-design`：请用完整原理图/BOM 确认去耦、保护和最大电流预算。；原因：当前资源是简化功能图，不包含电源细节。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `80b8ac7a8a9d4932e486eef3a63d2a062847bbf5130159a766c4cd4535779cd4` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-neoflash.md`

源文档 SHA-256：`2be120a1cd8f1442d2c0662ff5a3915e9d6b720db0641b221ee77e6f7da82b36`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
