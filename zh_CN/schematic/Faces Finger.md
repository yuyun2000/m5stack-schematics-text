# Faces Finger 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces Finger |
| SKU | A066 |
| 产品 ID | `faces-finger-91bac52e5220` |
| 源文档 | `zh_CN/module/faces_finger.md` |

## 概述

Faces Finger 由 Faces 22 针总线转接板与 6 针指纹模组接口板组成，主机 UART2_RX/UART2_TX 分别连接指纹板 TX/RX。J1 还引出 DA26、AD35 与 G5，Q1/Q2 SS8050 Y1 配合 Tout/VT 网络形成两路晶体管辅助控制。指纹板由 +3.3V/GND 供电，未显示独立稳压、时钟、存储、ESD 或具体指纹传感器内部电路。

## 检索关键词

`Faces Finger`、`A066`、`FPC1020A`、`Finger`、`UART2`、`UART2_RX`、`UART2_TX`、`GPIO16`、`GPIO17`、`R2/16`、`T2/17`、`DA26`、`AD35`、`AD35_Tout`、`G5`、`Tout`、`VT`、`TX`、`RX`、`SS8050 Y1`、`M5_BUS_22P`、`Faces Panel Bus`、`+3.3V`、`P1`、`P2`、`P3`、`P4`、`P5`、`160x160`、`508DPI`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | M5_BUS_22P | Faces 面板 22 针主机接口，提供 3.3V、GND、UART2、DA26、AD35 与 G5 | 图 e9b37d266cf8 / 第 1 页 / 右侧 J1 M5_BUS_22P pins1-22 |
| Q1/Q2 | SS8050 Y1 | DA26/AD35_Tout 与 G5/VT 相关的两路 3.3 V 晶体管辅助控制 | 图 e9b37d266cf8 / 第 1 页 / 左侧 Q1/Q2 SS8050 Y1，+3.3V/DA26/G5/P1/P3 |
| P1-P4 | Header 2 | 主板侧 3.3V、UART/Tout/VT 与 GND 板间连接器 | 图 e9b37d266cf8 / 第 1 页 / 左侧 P1-P4 Header2 |
| P2 | Finger 6-pin connector | 指纹模组 6 针接口，提供 3.3V、TX、RX 与 GND | 图 9c5c8116c1ac / 第 1 页 / 左侧 P2 Finger pins1-6 |
| P1/P3/P4/P5 | Header 2 | 指纹板侧 3.3V、TX/Tout、RX/VT 与 GND 板间连接器 | 图 9c5c8116c1ac / 第 1 页 / 右侧 P1/P3/P4/P5 Header2 |

## 系统结构

### 指纹面板架构

J1 Faces 总线通过板间 Header2 连接 P2 Finger 6 针接口，提供 UART2、3.3 V、GND 以及 Tout/VT 辅助控制；页面没有画指纹模组内部 IC。

- 参数与网络：`host=J1 M5_BUS_22P`；`sensor_connector=P2 Finger`；`communication=UART2`；`power=+3.3V/GND`；`auxiliary=Tout/VT via Q1/Q2`；`internal_sensor_circuit=not shown`
- 证据：图 e9b37d266cf8 / 第 1 页 / 整页 Faces 总线转接板; 图 9c5c8116c1ac / 第 1 页 / 整页 Finger 连接板

## 电源

### 指纹模组 3.3 V 供电

J1 pin3 3V3 连接 +3.3V；指纹板 P2 pin3 接 +3.3V、pin6 接 GND，P1 两针均为 +3.3V，P5 两针均为 GND。

- 参数与网络：`host_supply=J1 pin3 +3.3V`；`finger_vcc=P2 pin3`；`finger_ground=P2 pin6`；`board_power_header=P1 pins1/2 +3.3V`；`board_ground_header=P5 pins1/2 GND`；`regulator=none shown`
- 证据：图 e9b37d266cf8 / 第 1 页 / J1 3V3/GND; 图 9c5c8116c1ac / 第 1 页 / P2/P1/P5 电源连接

## 接口

### Faces 22 针总线已用引脚

J1 已用 pin2 GND、pin3 3V3、pin4 AD35、pin10 DA26、pin11 UART2_RX/R2/16、pin13 UART2_TX/T2/17、pin21 G5；其余可见 5V、MOSI、AD36、MISO、DA25、SCK、SK、WS、SDA、OUT、SCL、MK、G2、IN、HRR 未连接。

- 参数与网络：`pin2=GND`；`pin3=3V3`；`pin4=AD35`；`pin10=DA26`；`pin11=UART2_RX R2/16`；`pin13=UART2_TX T2/17`；`pin21=G5`；`unused_visible=5V/MOSI/AD36/MISO/DA25/SCK/SK/WS/SDA/OUT/SCL/MK/G2/IN/HRR`
- 证据：图 e9b37d266cf8 / 第 1 页 / J1 M5_BUS_22P pins1-22

## 总线

### 指纹模组 UART2

指纹板 P2 pin4 TX 经 P3 pin1/主板 P2 pin1 连接 UART2_RX/J1 pin11 R2/16；P2 pin5 RX 经 P4 pin1/主板 P3 pin1 连接 UART2_TX/J1 pin13 T2/17。

- 参数与网络：`controller=external host`；`device=Finger module`；`finger_tx=P2 pin4 TX -> host UART2_RX`；`host_rx=J1 pin11 R2/16`；`host_tx=J1 pin13 T2/17 -> finger RX`；`finger_rx=P2 pin5 RX`；`direction=full duplex UART`
- 证据：图 e9b37d266cf8 / 第 1 页 / J1 UART2_RX/UART2_TX 与 P2/P3; 图 9c5c8116c1ac / 第 1 页 / P2 Finger TX/RX 与 P3/P4

## GPIO 与控制信号

### 主机 UART GPIO 映射

J1 pin11 标为 R2/16 并连接 UART2_RX，J1 pin13 标为 T2/17 并连接 UART2_TX，对应主机 GPIO16 接收与 GPIO17 发送。

- 参数与网络：`gpio16=J1 pin11 R2/16 UART2_RX`；`gpio17=J1 pin13 T2/17 UART2_TX`
- 证据：图 e9b37d266cf8 / 第 1 页 / J1 pins11/13 与 UART2_RX/UART2_TX

### DA26/AD35/G5 辅助控制

J1 pin10 DA26 连接 Q1 控制网络，J1 pin4 AD35 连接主板 P2 pin2 AD35_Tout，J1 pin21 G5 连接 Q2 控制网络。

- 参数与网络：`da26=J1 pin10 -> Q1`；`ad35=J1 pin4 -> P2 pin2 AD35_Tout`；`g5=J1 pin21 -> Q2`；`transistors=Q1/Q2 SS8050 Y1`
- 证据：图 e9b37d266cf8 / 第 1 页 / J1 DA26/AD35/G5 与左侧 Q1/Q2/P2

## 保护电路

### 接口保护边界

两页原理图未显示 UART 串联电阻、ESD 阵列、保险丝或独立电平转换 IC；仅有 Q1/Q2 分立晶体管辅助网络。

- 参数与网络：`uart_series_resistors=none shown`；`esd=none shown`；`fuse=none shown`；`level_shifter_ic=none shown`；`discrete_transistors=Q1/Q2`
- 证据：图 e9b37d266cf8 / 第 1 页 / 整页主板电路; 图 9c5c8116c1ac / 第 1 页 / 整页指纹连接板

## 关键网络

### 两板板间网络

主板 P2 的 UART2_RX/AD35_Tout 对接指纹板 P3 的 TX/Tout；主板 P3 的 UART2_TX/VT 对接指纹板 P4 的 RX/VT；两板还通过双针 3.3V 与 GND 排针对接。

- 参数与网络：`tx_path=Finger P3 TX -> host P2 UART2_RX`；`tout_path=Finger P3 Tout -> host P2 AD35_Tout`；`rx_path=host P3 UART2_TX -> Finger P4 RX`；`vt_path=host P3 VT -> Finger P4 VT`；`power=P1 +3.3V`；`ground=host P4 / finger P5`
- 证据：图 e9b37d266cf8 / 第 1 页 / P1-P4 Header2 net labels; 图 9c5c8116c1ac / 第 1 页 / P1/P3/P4/P5 Header2 net labels

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 指纹面板架构 | `host=J1 M5_BUS_22P`；`sensor_connector=P2 Finger`；`communication=UART2`；`power=+3.3V/GND`；`auxiliary=Tout/VT via Q1/Q2`；`internal_sensor_circuit=not shown` |
| 总线 | 指纹模组 UART2 | `controller=external host`；`device=Finger module`；`finger_tx=P2 pin4 TX -> host UART2_RX`；`host_rx=J1 pin11 R2/16`；`host_tx=J1 pin13 T2/17 -> finger RX`；`finger_rx=P2 pin5 RX`；`direction=full duplex UART` |
| GPIO 与控制信号 | 主机 UART GPIO 映射 | `gpio16=J1 pin11 R2/16 UART2_RX`；`gpio17=J1 pin13 T2/17 UART2_TX` |
| 电源 | 指纹模组 3.3 V 供电 | `host_supply=J1 pin3 +3.3V`；`finger_vcc=P2 pin3`；`finger_ground=P2 pin6`；`board_power_header=P1 pins1/2 +3.3V`；`board_ground_header=P5 pins1/2 GND`；`regulator=none shown` |
| GPIO 与控制信号 | DA26/AD35/G5 辅助控制 | `da26=J1 pin10 -> Q1`；`ad35=J1 pin4 -> P2 pin2 AD35_Tout`；`g5=J1 pin21 -> Q2`；`transistors=Q1/Q2 SS8050 Y1` |
| 关键网络 | 两板板间网络 | `tx_path=Finger P3 TX -> host P2 UART2_RX`；`tout_path=Finger P3 Tout -> host P2 AD35_Tout`；`rx_path=host P3 UART2_TX -> Finger P4 RX`；`vt_path=host P3 VT -> Finger P4 VT`；`power=P1 +3.3V`；`ground=host P4 / finger P5` |
| 接口 | Faces 22 针总线已用引脚 | `pin2=GND`；`pin3=3V3`；`pin4=AD35`；`pin10=DA26`；`pin11=UART2_RX R2/16`；`pin13=UART2_TX T2/17`；`pin21=G5`；`unused_visible=5V/MOSI/AD36/MISO/DA25/SCK/SK/WS/SDA/OUT/SCL/MK/G2/IN/HRR` |
| 保护电路 | 接口保护边界 | `uart_series_resistors=none shown`；`esd=none shown`；`fuse=none shown`；`level_shifter_ic=none shown`；`discrete_transistors=Q1/Q2` |
| 核心器件 | 指纹模组型号 | `claimed_model=FPC1020A`；`schematic_marking=Finger`；`internal_part_number=not printed` |
| 传感器 | 指纹成像与识别参数 | `claimed_array=160x160 pixels`；`claimed_gray=256 levels/8-bit`；`claimed_resolution=508DPI`；`claimed_security=levels 0-9, default 5` |
| 总线 | 串口速率与帧格式 | `bus=UART2`；`baud=not printed`；`frame_format=not printed` |

## 待确认事项

- `component.fingerprint-model`：产品正文称内部为 FPC1020A，但原理图只将 6 针接口标为 Finger，没有印出 FPC1020A 料号或模组内部芯片。（证据：图 9c5c8116c1ac / 第 1 页 / P2 仅标 Finger）
- `sensor.performance`：产品正文列出 160×160 像素、256 灰度级、508 DPI 与安全等级 0-9，但这些性能参数未印在两页原理图中。（证据：图 9c5c8116c1ac / 第 1 页 / Finger connector page has no performance specifications）
- `bus.uart-settings`：原理图确认 UART2 TX/RX 连线，但没有印出波特率、数据位、校验位或停止位。（证据：图 e9b37d266cf8 / 第 1 页 / UART2_RX/UART2_TX nets）
- `review.fingerprint-model`：请用 A066 BOM、模组标签或采购规格确认实际指纹模组为 FPC1020A。；原因：原理图仅标 Finger。
- `review.performance`：请用已确认指纹模组 datasheet 或测试规范复核像素、灰度、DPI 与安全等级。；原因：这些参数未出现在原理图中。
- `review.uart-settings`：请用指纹模组串口协议确认 UART2 波特率和帧格式。；原因：原理图只包含 TX/RX 网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e9b37d266cf8548f6bca13f50fad2b8b5668f6e762b6790be00b5f62c23ea92b` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_sch_01.webp` |
| 2 | 1 | `9c5c8116c1ac4bc30056860584979c66dcfe2d7464e45514dc36c8a9b3fb9c5d` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_sch_02.webp` |

---

源文档：`zh_CN/module/faces_finger.md`

源文档 SHA-256：`3827608b6ee8c4a6e358e44c8ad3857f99c82c3b0c76f5d2c150271252548ca2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
