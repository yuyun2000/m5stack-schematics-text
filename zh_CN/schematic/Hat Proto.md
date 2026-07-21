# Hat Proto 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Proto |
| SKU | U060 |
| 产品 ID | `hat-proto-1360162c8e23` |
| 源文档 | `zh_CN/hat/hat-proto.md` |

## 概述

Hat Proto 是一块无预设功能电路的 StickC 原型转接板。原理图仅包含 P1 STICKIO 与 P2 Header 8，两者按相同针号 1:1 连接 GND、5VOUT、G26、G36、G0、BAT、3V3 和 5VIN。图中未配置有源器件、保护、滤波、去耦或固定总线功能，用户电路需自行设计。

## 检索关键词

`Hat Proto`、`U060`、`STICKIO`、`Header 8`、`P1`、`P2`、`GND`、`5VOUT`、`G26`、`G36`、`G0`、`BAT`、`3V3`、`5VIN`、`1:1 pass-through`、`prototype board`、`40 holes`、`2.54mm pitch`、`1mm hole`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | STICKIO | 连接 M5StickC 主机的 8 针 HAT 接口 | 图 457618cb5be8 / 第 1 页 / B1-B2，P1 STICKIO pins 1-8 |
| P2 | Header 8 | 与 P1 同针号直通的 8 针原型板排针接口 | 图 457618cb5be8 / 第 1 页 / B2，P2 Header 8 pins 1-8 |

## 系统结构

### 无源原型转接

Hat Proto 原理图只包含 P1 STICKIO 与 P2 Header 8，并以八条网络完成 1:1 直通。

- 参数与网络：`host_connector=P1 STICKIO`；`prototype_connector=P2 Header 8`；`topology=pin-for-pin pass-through`；`pin_count=8`
- 证据：图 457618cb5be8 / 第 1 页 / P1 与 P2 之间八条同编号直连网络

## 电源

### 电源轨引出

原型板直通引出 GND、5VOUT、BAT、3V3 与 5VIN，不进行转换或选择。

- 参数与网络：`ground=pin1 GND`；`host_5v_output=pin2 5VOUT`；`battery=pin6 BAT`；`3v3=pin7 3V3`；`5v_input=pin8 5VIN`；`conversion=none shown`
- 证据：图 457618cb5be8 / 第 1 页 / P1/P2 电源网络 pins 1/2/6/7/8

## 接口

### 8 针直通映射

P1/P2 pins 1-8 依次为 GND、5VOUT、G26、G36、G0、BAT、3V3、5VIN。

- 参数与网络：`pin1=GND`；`pin2=5VOUT`；`pin3=G26`；`pin4=G36`；`pin5=G0`；`pin6=BAT`；`pin7=3V3`；`pin8=5VIN`
- 证据：图 457618cb5be8 / 第 1 页 / P1/P2 pins 1-8 与网络标签

### 预设总线功能

G26、G36、G0 在原理图中仅以 GPIO 网络名直通，未预设 I2C、UART、SPI 或模拟功能方向。

- 参数与网络：`signals=G26; G36; G0`；`preassigned_bus=none`；`direction=not fixed`
- 证据：图 457618cb5be8 / 第 1 页 / GPIO 网络标签仅为 G26/G36/G0

## GPIO 与控制信号

### GPIO 引出

原型板直通引出 G26、G36 和 G0 三路主机 GPIO。

- 参数与网络：`gpios=G26; G36; G0`；`pins=3; 4; 5`
- 证据：图 457618cb5be8 / 第 1 页 / P1/P2 pin3 G26、pin4 G36、pin5 G0

## 保护电路

### 保护与调理

该原理图未在 P1 与 P2 之间显示保险丝、ESD、限流、滤波、去耦、稳压或电平转换器件。

- 参数与网络：`fuse=not shown`；`esd=not shown`；`filter=not shown`；`decoupling=not shown`；`regulator=not shown`；`level_shifter=not shown`
- 证据：图 457618cb5be8 / 第 1 页 / 整页仅 P1/P2 和直连网络，无其他器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 无源原型转接 | `host_connector=P1 STICKIO`；`prototype_connector=P2 Header 8`；`topology=pin-for-pin pass-through`；`pin_count=8` |
| 接口 | 8 针直通映射 | `pin1=GND`；`pin2=5VOUT`；`pin3=G26`；`pin4=G36`；`pin5=G0`；`pin6=BAT`；`pin7=3V3`；`pin8=5VIN` |
| GPIO 与控制信号 | GPIO 引出 | `gpios=G26; G36; G0`；`pins=3; 4; 5` |
| 电源 | 电源轨引出 | `ground=pin1 GND`；`host_5v_output=pin2 5VOUT`；`battery=pin6 BAT`；`3v3=pin7 3V3`；`5v_input=pin8 5VIN`；`conversion=none shown` |
| 保护电路 | 保护与调理 | `fuse=not shown`；`esd=not shown`；`filter=not shown`；`decoupling=not shown`；`regulator=not shown`；`level_shifter=not shown` |
| 接口 | 预设总线功能 | `signals=G26; G36; G0`；`preassigned_bus=none`；`direction=not fixed` |
| 其他事实 | 原型孔数量与规格 | `claimed_holes=40`；`claimed_pitch=2.54mm`；`claimed_diameter=1mm`；`schematic_geometry=not shown` |
| 其他事实 | 产品机械尺寸 | `claimed_size=35.0x24.0x13.7mm`；`schematic_dimensions=not shown` |
| 电源 | 电源轨额定电流 | `rails=5VOUT; BAT; 3V3; 5VIN`；`maximum_current=not shown`；`maximum_voltage=not shown` |

## 待确认事项

- `other.prototype-holes`：产品正文称原型区有 40 孔、2.54 mm 孔距和 1 mm 孔径，但当前原理图未画原型孔阵列或尺寸标注。（证据：图 457618cb5be8 / 第 1 页 / 原理图只显示连接器，未画孔阵列）
- `other.mechanical-size`：当前原理图未直接标注产品正文所述 35.0×24.0×13.7 mm 尺寸。（证据：图 457618cb5be8 / 第 1 页 / 图纸页面无产品尺寸标注）
- `power.current-rating`：原理图确认 5VOUT、BAT、3V3、5VIN 直通，但未给出连接器、铜箔或原型孔的最大电流与电压额定值。（证据：图 457618cb5be8 / 第 1 页 / P1/P2 电源网络无额定值）
- `review.prototype-holes`：请用 PCB/机械图确认 40 孔、2.54 mm 孔距和 1 mm 孔径。；原因：当前原理图未画原型孔阵列。
- `review.mechanical-size`：请用机械图确认 35.0×24.0×13.7 mm 外形尺寸。；原因：电气原理图无尺寸。
- `review.power-rating`：请用 PCB 铜厚、连接器和孔焊盘规格确认各电源轨额定电流/电压。；原因：原理图仅显示直通网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `457618cb5be8cc0f4cb5d1904b0bd9648ff339c85b020d11f526928c473786d7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/862/StickHat_PROTO_page_01.png` |

---

源文档：`zh_CN/hat/hat-proto.md`

源文档 SHA-256：`328f4fdec3331bc5778a18e95bba8284c13d6508dbd3275a91ef9d9b39d54c42`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
