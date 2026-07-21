# Stamp ISP 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp ISP |
| SKU | S006 |
| 产品 ID | `stamp-isp-c565fe0a6c4b` |
| 源文档 | `zh_CN/module/StampISP.md` |

## 概述

Stamp ISP 以 U1 CH9102F 完成 USB D+/D- 到 TXD/RXD UART 转换，USB1 Type-C 的 VBUS 经 F1 1 A/6 V 保险丝形成 +5 V。U3 SY8089 把 +5 V 降压为 +3.3 V，为 CH9102F、J1 和状态灯供电；U2 SRV05-4-P-T7 保护 USB/电源信号。Q1 双 NPN 在 DTR/RTS 控制下生成 BOOT 与 EN 自动下载信号，J1 StampISP_Pin 同时引出 5 V、3.3 V、USB、UART、BOOT、EN 和双 GND。

## 检索关键词

`Stamp ISP`、`S006`、`CH9102F`、`SY8089`、`SRV05-4-P-T7`、`TYPEC-304S-ACP16`、`USB Type-C`、`USB_P`、`USB_N`、`VBUS_USB`、`+5V`、`+3.3V`、`UART`、`TXD`、`RXD`、`DTR`、`RTS`、`BOOT`、`EN`、`LMBT3904DW1T1G`、`StampISP_Pin`、`F1 1A/6V`、`CC1`、`CC2`、`5.1KΩ`、`D+`、`D-`、`D1 blue`、`D2 blue`、`D3 red`、`RLSD52A031V`、`L1 4.7uH`、`R9 68KΩ`、`R10 15KΩ`、`C2 10uF`、`ESP32 download`、`50bps-4Mbps`、`USB 2.0`、`±8kV ESD`、`3.3V output`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | CH9102F | USB 转全双工 UART 桥，提供 TXD/RXD、DTR/RTS 与 USB D+/D- | 图 5b8de1b83a47 / 第 1 页 / C2-D3 U1 CH9102F pins1-24 |
| U3 | SY8089 | 从 +5 V 产生 +3.3 V 的同步降压转换器 | 图 5b8de1b83a47 / 第 1 页 / B3-B4 U3 SY8089/L1/R9/R10/C3-C5/C7 |
| U2 | SRV05-4-P-T7 | USB_P、USB_N 与 VBUS 相关线路的多通道 ESD 保护阵列 | 图 5b8de1b83a47 / 第 1 页 / C3 U2 SRV05-4-P-T7 pins1-6 |
| USB1 | TYPEC-304S-ACP16 | USB Type-C 设备接口，提供 VBUS、CC1/CC2、DP/DM 与 GND | 图 5b8de1b83a47 / 第 1 页 / C4-D4 USB1 TYPEC-304S-ACP16 pinsA/B/13-16 |
| Q1 | LMBT3904DW1T1G | DTR/RTS 到 BOOT/EN 的双 NPN 自动下载控制器 | 图 5b8de1b83a47 / 第 1 页 / C1-C2 Q1 LMBT3904DW1T1G/R6/R8/BOOT/EN |
| J1 | StampISP_Pin | 十针边缘接口，引出 5 V、3.3 V、GND、D+/D-、TXD/RXD、BOOT 与 EN | 图 5b8de1b83a47 / 第 1 页 / B2 J1 StampISP_Pin pins1-10 |
| F1 | Fuse 1A/6V | VBUS_USB 到 +5 V 电源轨的串联保险丝 | 图 5b8de1b83a47 / 第 1 页 / B2-B3 VBUS_USB/F1 Fuse 1A/6V/+5V |
| D1/D2/D3 | 蓝灯0603 / 蓝灯0603 / 红灯0603 | TXD、RXD 活动指示和 3.3 V 电源指示 | 图 5b8de1b83a47 / 第 1 页 / D1-D2 D1/D2 blue/R1/R2 and D3 red/R3 |
| D4 | RLSD52A031V | +3.3 V 输出轨对地保护器件 | 图 5b8de1b83a47 / 第 1 页 / B4 +3.3V/D4 RLSD52A031V/GND |
| L1/R9/R10 | 3015 4.7uH / 68KΩ / 15KΩ | SY8089 输出电感与反馈分压网络 | 图 5b8de1b83a47 / 第 1 页 / B3-B4 U3 SW/L1/R9/R10/+3.3V |
| R4/R5 | 5.1KΩ / 5.1KΩ | USB Type-C CC1/CC2 下拉电阻，配置为设备端 | 图 5b8de1b83a47 / 第 1 页 / C4 USB1 CC1/R4 and CC2/R5 to GND |

## 系统结构

### Stamp ISP 系统架构

USB1 Type-C 连接 U1 CH9102F 的 USB_P/USB_N，U1 输出 UART 与 DTR/RTS；Q1 生成 BOOT/EN，U3 从 USB +5 V 产生 +3.3 V，J1 汇总全部烧录与供电信号。

- 参数与网络：`usb=USB1 TYPEC-304S-ACP16`；`bridge=U1 CH9102F`；`power=VBUS_USB -> F1 -> +5V -> U3 SY8089 -> +3.3V`；`auto_download=DTR/RTS -> Q1 -> BOOT/EN`；`output=J1 StampISP_Pin`；`protection=U2 SRV05-4-P-T7; D4 RLSD52A031V`
- 证据：图 5b8de1b83a47 / 第 1 页 / 整页 USB1/U1/U2/U3/Q1/J1

## 电源

### USB VBUS 与 5 V 轨

USB1 VBUS 形成 VBUS_USB，经 F1 Fuse 1A/6V 串联成为 +5 V；VBUS_USB 同时引出到 J1 pin1（接口内标 5V）。

- 参数与网络：`source=USB1 VBUS`；`raw_rail=VBUS_USB`；`fuse=F1 1A/6V`；`system_rail=+5V`；`edge_pin=J1 pin1 VBUS_USB/5V`
- 证据：图 5b8de1b83a47 / 第 1 页 / USB1 VBUS/VBUS_USB and B2-B3 F1/+5V/J1 pin1

### SY8089 3.3 V 降压

U3 SY8089 VIN pin4 接 +5 V、EN pin1 接 +5 V、SW pin3 经 L1 4.7 uH 输出 +3.3 V，FB pin5 使用 R9 68 kΩ/R10 15 kΩ 分压。

- 参数与网络：`input=+5V`；`converter=U3 SY8089`；`enable=pin1 tied +5V`；`switch=pin3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R9 68KΩ upper; R10 15KΩ lower`；`ground=pin2`
- 证据：图 5b8de1b83a47 / 第 1 页 / B3-B4 U3/L1/R9/R10/+5V/+3.3V

### SY8089 输入输出去耦

+5 V 输入配置 C5 22 uF/C7 100 nF，+3.3 V 输出配置 C4 22 uF/C3 100 nF。

- 参数与网络：`input_caps=C5 22uF; C7 100nF`；`output_caps=C4 22uF; C3 100nF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 5b8de1b83a47 / 第 1 页 / B3-B4 C3-C5/C7 around U3

### CH9102F 供电

U1 VIO pin6 接 +3.3 V，VBUS/REGIN 区域连接 VBUS，RST 由 R7 10 kΩ 上拉至 +3.3 V，C1 100 nF 为本地去耦。

- 参数与网络：`vio=U1 pin6 +3.3V`；`usb_supply=VBUS/REGIN pins7/8`；`reset_pullup=R7 10KΩ to +3.3V`；`decoupling=C1 100nF`
- 证据：图 5b8de1b83a47 / 第 1 页 / C2-C3 U1 VIO/REGIN/VBUS/RST/R7/C1

## 接口

### USB Type-C 连接

USB1 A4/B9 接 VBUS_USB，A6/B6 合并为 USB_P，A7/B7 合并为 USB_N，CC1 A5 与 CC2 B5 分别经 R4/R5 5.1 kΩ 接 GND，SBU1/SBU2 未连接。

- 参数与网络：`connector=USB1 TYPEC-304S-ACP16`；`vbus=A4/B9 VBUS_USB`；`dp=A6/B6 USB_P`；`dm=A7/B7 USB_N`；`cc1=A5 -> R4 5.1K -> GND`；`cc2=B5 -> R5 5.1K -> GND`；`sbu=A8/B8 no-connect`；`ground=A1/B12 and pins13-16`
- 证据：图 5b8de1b83a47 / 第 1 页 / C4-D4 USB1 pin labels/R4/R5/USB_P/USB_N

### 下载状态指示灯

D1 蓝灯由 +3.3 V 经 R1 1 kΩ 接 TXD，D2 蓝灯由 +3.3 V 经 R2 1 kΩ 接 RXD，D3 红灯由 +3.3 V 经 R3 1 kΩ 接 GND。

- 参数与网络：`tx=D1 蓝灯0603 / R1 1KΩ / TXD`；`rx=D2 蓝灯0603 / R2 1KΩ / RXD`；`power=D3 红灯0603 / R3 1KΩ / GND`；`supply=+3.3V`
- 证据：图 5b8de1b83a47 / 第 1 页 / D1-D2 D1-D3/R1-R3/TXD/RXD/+3.3V

### StampISP 十针接口

J1 pin1 为 5V/VBUS_USB、pin2 GND、pin3 D+、pin4 D-、pin5 3V3、pin6 RXD、pin7 TXD、pin8 EN、pin9 BOOT、pin10 GND。

- 参数与网络：`pin1=5V / VBUS_USB`；`pin2=GND`；`pin3=D+ / USB_P`；`pin4=D- / USB_N`；`pin5=3V3`；`pin6=RXD`；`pin7=TXD`；`pin8=EN`；`pin9=BOOT`；`pin10=GND`
- 证据：图 5b8de1b83a47 / 第 1 页 / B2 J1 StampISP_Pin pins1-10

## 总线

### CH9102F USB 数据

USB_P 连接 U1 D+ pin4，USB_N 连接 U1 D- pin5；两线同时引出到 J1 pins3/4，并通过 U2 保护阵列。

- 参数与网络：`device=U1 CH9102F`；`dp=USB_P -> U1 pin4 D+ -> J1 pin3 D+`；`dm=USB_N -> U1 pin5 D- -> J1 pin4 D-`；`protection=U2 SRV05-4-P-T7`；`direction=bidirectional USB`
- 证据：图 5b8de1b83a47 / 第 1 页 / C2-D4 USB_P/USB_N between USB1/U2/U1/J1

### CH9102F UART

U1 TXD pin21 连接 J1 pin7 TXD，RXD pin20 连接 J1 pin6 RXD；DTR pin23 与 RTS pin19 驱动自动下载网络，CTS/DSR/DCD 未连接。

- 参数与网络：`tx=U1 TXD pin21 -> J1 pin7`；`rx=J1 pin6 -> U1 RXD pin20`；`control=DTR pin23; RTS pin19`；`unused_modem=CTS pin18; DSR pin22; DCD pin24`；`direction=TXD bridge-to-target; RXD target-to-bridge`
- 证据：图 5b8de1b83a47 / 第 1 页 / D2-D3 U1 top UART/modem pins and B2 J1 TXD/RXD

## GPIO 与控制信号

### DTR/RTS 自动下载控制

Q1 LMBT3904DW1T1G 双 NPN 将 DTR 与 RTS 组合转换为 BOOT 和 EN；R6/R8 各 10 kΩ，EN 配置 C2 10 uF 对地。

- 参数与网络：`transistor=Q1 LMBT3904DW1T1G`；`inputs=DTR; RTS`；`outputs=BOOT -> J1 pin9; EN -> J1 pin8`；`resistors=R6/R8 10KΩ`；`reset_cap=C2 10uF EN-to-GND`
- 证据：图 5b8de1b83a47 / 第 1 页 / C1-C2 Q1/R6/R8/DTR/RTS/BOOT/EN/C2

## 保护电路

### USB ESD 保护

U2 SRV05-4-P-T7 位于 USB_P、USB_N 与 VBUS 相关路径，GND pin2 接地，作为多通道接口保护阵列。

- 参数与网络：`device=U2 SRV05-4-P-T7`；`protected=USB_P, USB_N, VBUS-related line`；`ground=pin2 GND`
- 证据：图 5b8de1b83a47 / 第 1 页 / C3 U2 connected to USB differential/VBUS nets

### 3.3 V 轨保护

+3.3 V 输出通过 D4 RLSD52A031V 接地保护。

- 参数与网络：`device=D4 RLSD52A031V`；`rail=+3.3V`；`connection=+3.3V to GND`
- 证据：图 5b8de1b83a47 / 第 1 页 / B4 D4 on +3.3V rail

## 调试与烧录

### 调制解调器控制测试点

JP1/JP2 位于 U1 顶部 DTR/TXD/RXD/RTS 网络区域，页面未给连接器型号或明确每个跳点对应关系。

- 参数与网络：`references=JP1/JP2`；`nearby_nets=DTR, TXD, RXD, RTS`；`part_number=not shown`；`exact_mapping=not labeled`
- 证据：图 5b8de1b83a47 / 第 1 页 / D2-D3 JP1/JP2 beside DTR/TXD/RXD/RTS

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp ISP 系统架构 | `usb=USB1 TYPEC-304S-ACP16`；`bridge=U1 CH9102F`；`power=VBUS_USB -> F1 -> +5V -> U3 SY8089 -> +3.3V`；`auto_download=DTR/RTS -> Q1 -> BOOT/EN`；`output=J1 StampISP_Pin`；`protection=U2 SRV05-4-P-T7; D4 RLSD52A031V` |
| 接口 | USB Type-C 连接 | `connector=USB1 TYPEC-304S-ACP16`；`vbus=A4/B9 VBUS_USB`；`dp=A6/B6 USB_P`；`dm=A7/B7 USB_N`；`cc1=A5 -> R4 5.1K -> GND`；`cc2=B5 -> R5 5.1K -> GND`；`sbu=A8/B8 no-connect`；`ground=A1/B12 and pins13-16` |
| 总线 | CH9102F USB 数据 | `device=U1 CH9102F`；`dp=USB_P -> U1 pin4 D+ -> J1 pin3 D+`；`dm=USB_N -> U1 pin5 D- -> J1 pin4 D-`；`protection=U2 SRV05-4-P-T7`；`direction=bidirectional USB` |
| 总线 | CH9102F UART | `tx=U1 TXD pin21 -> J1 pin7`；`rx=J1 pin6 -> U1 RXD pin20`；`control=DTR pin23; RTS pin19`；`unused_modem=CTS pin18; DSR pin22; DCD pin24`；`direction=TXD bridge-to-target; RXD target-to-bridge` |
| GPIO 与控制信号 | DTR/RTS 自动下载控制 | `transistor=Q1 LMBT3904DW1T1G`；`inputs=DTR; RTS`；`outputs=BOOT -> J1 pin9; EN -> J1 pin8`；`resistors=R6/R8 10KΩ`；`reset_cap=C2 10uF EN-to-GND` |
| 电源 | USB VBUS 与 5 V 轨 | `source=USB1 VBUS`；`raw_rail=VBUS_USB`；`fuse=F1 1A/6V`；`system_rail=+5V`；`edge_pin=J1 pin1 VBUS_USB/5V` |
| 电源 | SY8089 3.3 V 降压 | `input=+5V`；`converter=U3 SY8089`；`enable=pin1 tied +5V`；`switch=pin3`；`inductor=L1 3015 4.7uH`；`output=+3.3V`；`feedback=R9 68KΩ upper; R10 15KΩ lower`；`ground=pin2` |
| 电源 | SY8089 输入输出去耦 | `input_caps=C5 22uF; C7 100nF`；`output_caps=C4 22uF; C3 100nF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | CH9102F 供电 | `vio=U1 pin6 +3.3V`；`usb_supply=VBUS/REGIN pins7/8`；`reset_pullup=R7 10KΩ to +3.3V`；`decoupling=C1 100nF` |
| 保护电路 | USB ESD 保护 | `device=U2 SRV05-4-P-T7`；`protected=USB_P, USB_N, VBUS-related line`；`ground=pin2 GND` |
| 保护电路 | 3.3 V 轨保护 | `device=D4 RLSD52A031V`；`rail=+3.3V`；`connection=+3.3V to GND` |
| 接口 | 下载状态指示灯 | `tx=D1 蓝灯0603 / R1 1KΩ / TXD`；`rx=D2 蓝灯0603 / R2 1KΩ / RXD`；`power=D3 红灯0603 / R3 1KΩ / GND`；`supply=+3.3V` |
| 接口 | StampISP 十针接口 | `pin1=5V / VBUS_USB`；`pin2=GND`；`pin3=D+ / USB_P`；`pin4=D- / USB_N`；`pin5=3V3`；`pin6=RXD`；`pin7=TXD`；`pin8=EN`；`pin9=BOOT`；`pin10=GND` |
| 调试与烧录 | 调制解调器控制测试点 | `references=JP1/JP2`；`nearby_nets=DTR, TXD, RXD, RTS`；`part_number=not shown`；`exact_mapping=not labeled` |
| 总线 | USB 2.0 全速兼容性 | `document_claim=USB 2.0 compatible full-speed device`；`schematic=USB D+/D- only`；`speed=not printed`；`protocol_version=not printed` |
| 总线 | 50 bps–4 Mbps UART 波特率 | `document_min=50bps`；`document_max=4Mbps`；`schematic_uart=TXD/RXD`；`clock_conditions=not shown` |
| 保护电路 | ±8 kV 静电保护等级 | `document_rating=±8kV`；`devices=U2 SRV05-4-P-T7; D4 RLSD52A031V`；`test_model=not shown`；`polarity=not shown` |
| 电源 | 3.3 V 输出能力 | `output=J1 pin5 +3.3V`；`converter=U3 SY8089`；`maximum_current=not shown`；`ripple=not shown`；`efficiency=not shown` |

## 待确认事项

- `bus.usb-capability`：产品正文称 USB 2.0 兼容的全速设备，原理图只确认 Type-C 与 CH9102F D+/D- 连接，没有打印 USB 速度或协议版本。（证据：图 5b8de1b83a47 / 第 1 页 / USB1/U1 USB data path lacks speed labels）
- `bus.uart-baud-range`：产品正文声明 50 bps 至 4 Mbps，原理图只显示 TXD/RXD 和 CH9102F 型号，未列波特率范围或时钟条件。（证据：图 5b8de1b83a47 / 第 1 页 / U1 CH9102F UART pins without baud table）
- `protection.esd-rating`：产品正文声明 ±8 kV 静电保护，原理图可确认 U2 与 D4 保护器件，但未印测试模型、极性或 ±8 kV 数值。（证据：图 5b8de1b83a47 / 第 1 页 / U2/D4 lack ESD rating annotations）
- `power.output-capability`：原理图确认 J1 pin5 提供 +3.3 V，但没有标注最大输出电流、纹波、效率或温升条件。（证据：图 5b8de1b83a47 / 第 1 页 / U3 +3.3V-to-J1 pin5 without ratings）
- `review.usb-capability`：请用 CH9102F 数据手册和 USB 枚举结果确认 USB 2.0 全速兼容性。；原因：速度和协议版本未印在原理图。
- `review.uart-baud-range`：请用 CH9102F 规格与实测串口配置复核 50 bps–4 Mbps 范围。；原因：波特率能力未印在原理图。
- `review.esd-rating`：请按 U2/D4 器件规格和规定测试模型确认 ±8 kV ESD 等级。；原因：原理图只给器件型号，没有等级与测试条件。
- `review.output-capability`：请用 SY8089 设计计算和负载测试确认 J1 3.3 V 最大输出电流、纹波与温升。；原因：输出额定能力未标在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5b8de1b83a47ab692b36295b834110ed8e7039e57141b95f4122100f36d8e016` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/572/Sch_StampISP_sch_01.png` |

---

源文档：`zh_CN/module/StampISP.md`

源文档 SHA-256：`fcec4858e69db654ad3185d7b5b86f16acac88b800a55de26b975510073f6389`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
