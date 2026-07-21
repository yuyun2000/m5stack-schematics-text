# Hat Yun 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Yun |
| SKU | U070 |
| 产品 ID | `hat-yun-e8e5bb044b49` |
| 源文档 | `zh_CN/hat/hat-yun.md` |

## 概述

Hat Yun 的本地资源是一张云朵形系统连线框图：STM32 连接光敏元件、BMP280、SHT20 和外围 14 个 LED 功能块。STICKIO 的 G26/SCL 与 G0/SDA 连接传感器总线，3V3 连接 STM32，5VI 连接独立的 5V POWER 功能块。该页没有器件位号、完整 STM32 型号、LED 料号、I2C 地址、被动器件或电源转换细节，因此相关产品正文参数列为待确认。

## 检索关键词

`Hat Yun`、`U070`、`STM32`、`STM32F030F4P6`、`BMP280`、`SHT20`、`光敏电阻`、`LED`、`14 x LED`、`SK6812 4020`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`GND`、`3V3`、`5VI`、`5V POWER`、`STICKIO`、`0x40`、`0x76`、`0x38`、`环境传感器`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| STM32 | STM32 | 框图中央控制器，连接光敏元件、SCL/SDA 传感器总线、3V3/GND 和外围 LED 链 | 图 6422fad12ee8 / 第 1 页 / 页面中央偏左 STM32 方框：左接光敏元件，下接 GND/3V3，右接传感器连线，周围为 LED 链 |
| BMP280 | BMP280 | 环境气压传感器功能块，连接共享传感器信号线 | 图 6422fad12ee8 / 第 1 页 / 页面中央偏右黑色小矩形，顶部标注 BMP280，下端连接两条水平传感器信号线 |
| SHT20 | SHT20 | 温湿度传感器功能块，连接共享传感器信号线 | 图 6422fad12ee8 / 第 1 页 / 页面中央偏右黑色方块，右侧标注 SHT20，下端连接传感器信号线 |
| Photoresistor | 未标注 | 光敏输入功能块，通过单条信号线连接 STM32 | 图 6422fad12ee8 / 第 1 页 / 页面中央偏左 STM32 左侧的圆形光敏元件图标及其水平连线 |
| LED x14 | 未标注 | 沿云朵外轮廓布置的 14 个 LED 功能块，形成外围灯链 | 图 6422fad12ee8 / 第 1 页 / 整页云朵灰色外围连线上分布 14 个分别标注 LED 的方块/箭头符号 |
| 5V POWER | 未标注 | 由 STICKIO 5VI 蓝色电源线连接的独立 5V POWER 功能块 | 图 6422fad12ee8 / 第 1 页 / 页面右下黑色方块，右侧竖排标注 5V POWER，左接来自 5VI 的蓝色线 |
| STICKIO | 未标注 | 主机侧 8 信号功能接口，标注 GND、5VO、G26、G36、G0、BAT、3V3、5VI | 图 6422fad12ee8 / 第 1 页 / 页面左下八行绿色标签：GND/5VO/G26/G36/G0/BAT/3V3/5VI |

## 系统结构

### Hat Yun

框图以 STM32 为控制器，连接 BMP280、SHT20、光敏元件和 14 个外围 LED；主机侧提供 GND、SCL、SDA、3V3 与 5VI 连接。

- 参数与网络：`controller=STM32`；`sensors=BMP280; SHT20; photoresistor`；`lighting=14 x LED`；`host_signals=GND; G26/SCL; G0/SDA; 3V3; 5VI`
- 证据：图 6422fad12ee8 / 第 1 页 / 全页云朵框图：中央 STM32/传感器、外围 LED 链与左下 STICKIO 信号

## 电源

### STM32 3V3 供电

STICKIO 的 3V3 通过红色连线连接 STM32；GND 通过黑色连线连接 STM32。

- 参数与网络：`supply=3V3 to STM32`；`ground=GND to STM32`；`decoupling=not shown`；`regulator=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面左下 3V3 红线与 GND 黑线连接中央 STM32

### 5VI 外部电源路径

STICKIO 的 5VI 通过蓝色连线连接右侧 5V POWER 功能块；框图未显示转换器、开关、保护或 5V POWER 到负载的具体连接。

- 参数与网络：`input=STICKIO 5VI`；`destination=5V POWER block`；`converter=not shown`；`switch=not shown`；`protection=not shown`；`loads=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面下方从 5VI 标签到右侧 5V POWER 方块的蓝色连线

## 接口

### STICKIO

框图标注 GND 连接 STM32 地线，G26 连接 SCL，G0 连接 SDA，3V3 连接 STM32 电源，5VI 连接 5V POWER；5VO、G36 和 BAT 未画出功能连接。

- 参数与网络：`GND=STM32 ground`；`5VO=no functional connection shown`；`G26=SCL`；`G36=no functional connection shown`；`G0=SDA`；`BAT=no functional connection shown`；`3V3=STM32 supply`；`5VI=5V POWER`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面左下八个 STICKIO 标签及黑色/红色/蓝色连线终点

## 总线

### SCL/SDA 传感器总线

G26 的 SCL 与 G0 的 SDA 沿框图连接 BMP280 和 SHT20，并与 STM32 传感器连线汇合。

- 参数与网络：`scl_host=G26`；`sda_host=G0`；`devices=BMP280; SHT20`；`controller=STM32`；`pullups=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面中部两条标注 SCL/SDA 的主机线及 BMP280/SHT20 下端连接点

## GPIO 与控制信号

### 外围 LED 链

云朵轮廓的灰色链路上显示 14 个分别标注 LED 的功能块；框图未标注控制 GPIO、数据方向或供电连接。

- 参数与网络：`count=14`；`label=LED`；`controller_gpio=not shown`；`data_direction=not shown`；`power_connection=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 整页云朵外轮廓灰色连线上逐个计数的 14 个 LED 标签

## 传感器

### BMP280 与 SHT20

框图明确标出 BMP280 和 SHT20 两个传感器功能块，两者连接共享的 SCL/SDA 信号路径。

- 参数与网络：`pressure_sensor=BMP280`；`temperature_humidity_sensor=SHT20`；`bus=SCL/SDA`；`power_pins=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面中央偏右 BMP280/SHT20 标注及下方连接点

### 光敏输入

光敏元件图标通过一条水平信号线直接连接 STM32；该页未标注其位号、阻值、分压网络或 STM32 引脚。

- 参数与网络：`sensor=photoresistor symbol`；`controller=STM32`；`controller_pin=not shown`；`resistance=not shown`；`divider=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 页面中央偏左光敏元件图标至 STM32 左侧的黑色水平线

## 其他事实

### 本地资源详细程度

该页为系统功能框图，不包含器件位号、芯片引脚号、被动器件值、连接器针脚编号、时钟、复位、BOOT、调试、存储或保护电路。

- 参数与网络：`asset_type=system functional block diagram`；`reference_designators=not shown`；`chip_pin_numbers=not shown`；`passives=not shown`；`clock_reset_debug=not shown`；`storage=not shown`；`protection=not shown`
- 证据：图 6422fad12ee8 / 第 1 页 / 整页仅包含功能块、传感器名称、LED 标签和彩色系统连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Yun | `controller=STM32`；`sensors=BMP280; SHT20; photoresistor`；`lighting=14 x LED`；`host_signals=GND; G26/SCL; G0/SDA; 3V3; 5VI` |
| 接口 | STICKIO | `GND=STM32 ground`；`5VO=no functional connection shown`；`G26=SCL`；`G36=no functional connection shown`；`G0=SDA`；`BAT=no functional connection shown`；`3V3=STM32 supply`；`5VI=5V POWER` |
| 总线 | SCL/SDA 传感器总线 | `scl_host=G26`；`sda_host=G0`；`devices=BMP280; SHT20`；`controller=STM32`；`pullups=not shown` |
| 传感器 | BMP280 与 SHT20 | `pressure_sensor=BMP280`；`temperature_humidity_sensor=SHT20`；`bus=SCL/SDA`；`power_pins=not shown` |
| 传感器 | 光敏输入 | `sensor=photoresistor symbol`；`controller=STM32`；`controller_pin=not shown`；`resistance=not shown`；`divider=not shown` |
| 核心器件 | STM32 控制器型号 | `documented_model=STM32F030F4P6`；`schematic_label=STM32`；`reference_designator=not shown`；`package=not shown` |
| 总线地址 | SHT20/BMP280 I2C 地址 | `documented_sht20_address=0x40`；`documented_bmp280_address=0x76`；`schematic_address_labels=not shown`；`address_configuration=not shown` |
| 总线地址 | Hat Yun 控制器 I2C 地址 | `documented_address=0x38`；`schematic_address_label=not shown`；`address_straps=not shown`；`firmware_evidence=not shown` |
| GPIO 与控制信号 | 外围 LED 链 | `count=14`；`label=LED`；`controller_gpio=not shown`；`data_direction=not shown`；`power_connection=not shown` |
| 核心器件 | RGB LED 型号 | `documented_type=SK6812 4020 RGB`；`documented_count=14`；`schematic_label=LED`；`reference_designators=not shown` |
| 电源 | STM32 3V3 供电 | `supply=3V3 to STM32`；`ground=GND to STM32`；`decoupling=not shown`；`regulator=not shown` |
| 电源 | 5VI 外部电源路径 | `input=STICKIO 5VI`；`destination=5V POWER block`；`converter=not shown`；`switch=not shown`；`protection=not shown`；`loads=not shown` |
| 其他事实 | 本地资源详细程度 | `asset_type=system functional block diagram`；`reference_designators=not shown`；`chip_pin_numbers=not shown`；`passives=not shown`；`clock_reset_debug=not shown`；`storage=not shown`；`protection=not shown` |

## 待确认事项

- `component.controller-exact-model`：产品正文给出 STM32F030F4P6，但本地框图只标注 STM32，没有完整型号、位号、封装或引脚名，无法由该页确认。（证据：图 6422fad12ee8 / 第 1 页 / 页面中央控制器方框仅标注 STM32）
- `address.sensor-i2c-addresses`：产品正文标注 SHT20 为 0x40、BMP280 为 0x76，但框图未显示任何地址文本、地址引脚或配置网络，无法由该页确认。（证据：图 6422fad12ee8 / 第 1 页 / 页面 BMP280/SHT20 与 SCL/SDA 区域，无 0x40、0x76 或地址配置）
- `address.yun-controller-0x38`：产品正文标注 YUN 地址为 0x38，但框图没有 0x38、地址选择网络或固件信息，无法由该页确认。（证据：图 6422fad12ee8 / 第 1 页 / 全页 STM32 与 SCL/SDA 网络，无 0x38 或地址配置标注）
- `component.led-type-sk6812`：产品正文声明使用 14 颗 SK6812 4020 RGB LED，但框图仅标注 LED，未显示 SK6812、4020、RGB、位号或级联引脚，无法由该页确认完整料号。（证据：图 6422fad12ee8 / 第 1 页 / 外围 14 个功能块均只标注 LED，无型号或封装）
- `review.controller-model`：Hat Yun 所装控制器完整型号是否为 STM32F030F4P6？；原因：产品正文给出完整型号，但本地框图仅标注 STM32。
- `review.sensor-addresses`：SHT20 的 0x40 与 BMP280 的 0x76 地址在该硬件版本上如何确认？；原因：框图只显示器件名称和共享信号线，没有地址或配置标注。
- `review.yun-address-0x38`：YUN 控制接口地址 0x38 是否由 STM32 固件固定实现？；原因：框图没有地址选择或固件版本依据。
- `review.led-part-number`：外围 14 颗 LED 的完整料号和封装是否为 SK6812 4020 RGB？；原因：框图确认数量为 14，但每个功能块只标注 LED。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6422fad12ee8e930c5c043ffab4c6f5d0e7b3370f3538f51da2cc8554b44fd36` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-yun.md`

源文档 SHA-256：`5966cdea3fe8c846d5ae27f4e350aa78e9f48a5026b9039f859cc5aa8145ce75`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
