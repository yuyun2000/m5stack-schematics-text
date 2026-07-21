# Scales Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Scales Kit |
| SKU | K121 |
| 产品 ID | `scales-kit-1d6fff1475ba` |
| 源文档 | `zh_CN/app/scales_kit.md` |

## 概述

Scales Kit 的电子电路以 U1 HX711 作为桥式称重传感器模数转换前端，J2 引出 E+/E-/A-/A+ 四线传感器接口，J1 引出 DOUT、PD_SCK、VCC 和 GND。Q1 SS8550 Y2 与 HX711 的 BASE/AVDD/VFB 引脚构成模拟电源调节路径，通道 A 接传感器并配置差分滤波，通道 B 接地未使用。产品正文给出的主机 GPIO 映射和 10SPS 数据率未在当前原理图中明确标注，已列为待确认。

## 检索关键词

`Scales Kit`、`K121`、`HX711`、`24-bit ADC`、`SS8550 Y2`、`load cell`、`bridge sensor`、`E+`、`E-`、`A+`、`A-`、`DOUT`、`PD_SCK`、`VSUP`、`DVDD`、`AVDD`、`VFB`、`INPA`、`INNA`、`INPB`、`INNB`、`VCC`、`GND`、`G36`、`G26`、`10SPS`、`Socket_3.96x4p`、`Header 4`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | HX711 | 桥式称重传感器模拟前端和串行输出 ADC，连接传感器通道 A、未用通道 B、模拟电源调节及 DOUT/PD_SCK | 图 9043dc2106c5 / 第 1 页 / 第 1 页中央 U1 hx711，VSUP/BASE/AVDD/VFB/AGND/VBG/INNA/INPA、DVDD/RATE/XI/XO/DOUT/PD_SCK/INPB/INNB |
| Q1 | SS8550 Y2 | 受 HX711 BASE 控制的模拟电源调整管，为 AVDD 和传感器 E+ 路径供电 | 图 9043dc2106c5 / 第 1 页 / 第 1 页左上 Q1 SS8550 Y2，连接 VCC、U1 BASE 和 AVDD/E+ 节点 |
| J2 | Socket_3.96x4p | 四线桥式称重传感器接口，依次引出 A+、A-、E-、E+ | 图 9043dc2106c5 / 第 1 页 / 第 1 页左侧 Connect to Sensor，J2 Socket_3.96x4p 的 pin1 A+、pin2 A-、pin3 E-、pin4 E+ |
| J1 | Header 4 | 连接 M5Core 的 DOUT、PD_SCK、VCC 和 GND 四针接口 | 图 9043dc2106c5 / 第 1 页 / 第 1 页右侧 Connect to M5Core，J1 Header 4 与 U1 DOUT/PD_SCK、VCC、GND |
| R1,R2 | 4.7KΩ | 分别将 DOUT 与 PD_SCK 上拉到 VCC | 图 9043dc2106c5 / 第 1 页 / 第 1 页右中，R1/R2 4.7KΩ 从 VCC 接到 DOUT/PD_SCK |
| R3,R4 | 20KΩ / 8.2KΩ | HX711 AVDD 到 AGND 的反馈分压，中心点连接 VFB | 图 9043dc2106c5 / 第 1 页 / 第 1 页中央左侧，R3 20KΩ、R4 8.2KΩ 与 U1 VFB |
| R5,C5 | 1KΩ / 100nF | 通道 A 输入串联与差分滤波网络 | 图 9043dc2106c5 / 第 1 页 / 第 1 页左下，J2 A+ 经 R5 1KΩ 到 INPA，C5 100nF 跨接 INPA/INNA |
| C1,C2,C3,C4 | 1uF / 1uF / 100nF / 1uF | VCC、AVDD、接口电源和 VBG/模拟节点的去耦电容 | 图 9043dc2106c5 / 第 1 页 / 第 1 页 C1 1uF、C2 1uF、C3 100nF、C4 1uF 各去耦支路 |

## 系统结构

### Scales Kit 称重采集架构

Scales Kit 电路由 J2 四线桥式传感器接口、U1 HX711 模拟前端与 ADC、Q1 模拟电源调节、通道 A 滤波和 J1 主机串行接口组成。

- 参数与网络：`adc=U1 HX711`；`sensor_connector=J2 Socket_3.96x4p`；`host_connector=J1 Header 4`；`analog_pass_device=Q1 SS8550 Y2`；`used_channel=A`；`unused_channel=B`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页完整单页原理图，Connect to Sensor、U1 hx711 与 Connect to M5Core

## 电源

### HX711 数字与输入电源

VCC 直接连接 U1 VSUP pin1 和 DVDD pin16，并由 C1 1uF 去耦到 GND；J1 pin3 同样引出 VCC，附近 C3 100nF 接地去耦。

- 参数与网络：`rail=VCC`；`hx711_pins=VSUP pin1, DVDD pin16`；`host_pin=J1 pin3`；`decoupling=C1 1uF, C3 100nF`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页 U1 顶部 VCC/VSUP/DVDD/C1 与 J1 pin3/C3

### HX711 模拟电源调节与反馈

U1 BASE 驱动 Q1 SS8550 Y2，Q1 从 VCC 向 AVDD/E+ 节点供电；R3 20kΩ 与 R4 8.2kΩ 从 AVDD 到 AGND 分压，中点连接 U1 VFB。

- 参数与网络：`input=VCC`；`pass_device=Q1 SS8550 Y2`；`control=U1 BASE pin2`；`output=U1 AVDD pin3 and J2 E+`；`feedback=R3 20K, R4 8.2K to U1 VFB pin4`；`return=U1 AGND pin5`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页左上至中央，Q1、U1 BASE/AVDD/VFB/AGND 与 R3/R4

## 接口

### J2 传感器激励连接

J2 pin4 E+ 连接 U1 AVDD 模拟电源节点，J2 pin3 E- 连接 U1 AGND/GND 返回路径。

- 参数与网络：`connector=J2`；`pin4=E+ to AVDD`；`pin3=E- to AGND/GND`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页左侧 J2 E+/E- 到 U1 AVDD/AGND 的连线

### J1 主机数据与时钟接口

U1 DOUT pin12 连接 J1 pin1，PD_SCK pin11 连接 J1 pin2，J1 pin3 为 VCC、pin4 为 GND；R1/R2 各 4.7kΩ 分别将 DOUT/PD_SCK 上拉到 VCC。

- 参数与网络：`pin1=DOUT`；`pin2=PD_SCK`；`pin3=VCC`；`pin4=GND`；`pullups=R1/R2 4.7K to VCC`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页右侧 U1 DOUT/PD_SCK、R1/R2 与 J1 Header 4

## 关键网络

### 模拟地与公共地连接

U1 AGND pin5、通道 B INPB/INNB、J1 GND、J2 E- 及各去耦返回均使用图中同一 GND 网络。

- 参数与网络：`analog_ground=U1 AGND pin5`；`host_ground=J1 pin4`；`sensor_return=J2 pin3 E-`；`channel_b=INPB/INNB`；`net=GND`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页 AGND、J1、J2、INPB/INNB 和 C1-C5 返回路径的 GND 符号

## 模拟电路

### HX711 通道 A 差分输入

J2 pin2 A- 连接 U1 INNA pin7；J2 pin1 A+ 经 R5 1kΩ 连接 U1 INPA pin8，C5 100nF 跨接 INNA 与 INPA 形成差分滤波。

- 参数与网络：`negative_input=J2 pin2 A- to U1 INNA pin7`；`positive_input=J2 pin1 A+ via R5 1K to U1 INPA pin8`；`differential_capacitor=C5 100nF`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页左下 J2 A-/A+、R5、C5 与 U1 INNA/INPA

### HX711 通道 B 未使用

U1 INPB pin10 与 INNB pin9 在当前原理图中短接并连接 GND，未引出到传感器连接器。

- 参数与网络：`INPB=GND`；`INNB=GND`；`external_connector=null`
- 证据：图 9043dc2106c5 / 第 1 页 / 第 1 页 U1 右下 INPB/INNB 公共节点到 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Scales Kit 称重采集架构 | `adc=U1 HX711`；`sensor_connector=J2 Socket_3.96x4p`；`host_connector=J1 Header 4`；`analog_pass_device=Q1 SS8550 Y2`；`used_channel=A`；`unused_channel=B` |
| 电源 | HX711 数字与输入电源 | `rail=VCC`；`hx711_pins=VSUP pin1, DVDD pin16`；`host_pin=J1 pin3`；`decoupling=C1 1uF, C3 100nF` |
| 电源 | HX711 模拟电源调节与反馈 | `input=VCC`；`pass_device=Q1 SS8550 Y2`；`control=U1 BASE pin2`；`output=U1 AVDD pin3 and J2 E+`；`feedback=R3 20K, R4 8.2K to U1 VFB pin4`；`return=U1 AGND pin5` |
| 接口 | J2 传感器激励连接 | `connector=J2`；`pin4=E+ to AVDD`；`pin3=E- to AGND/GND` |
| 模拟电路 | HX711 通道 A 差分输入 | `negative_input=J2 pin2 A- to U1 INNA pin7`；`positive_input=J2 pin1 A+ via R5 1K to U1 INPA pin8`；`differential_capacitor=C5 100nF` |
| 模拟电路 | HX711 通道 B 未使用 | `INPB=GND`；`INNB=GND`；`external_connector=null` |
| 接口 | J1 主机数据与时钟接口 | `pin1=DOUT`；`pin2=PD_SCK`；`pin3=VCC`；`pin4=GND`；`pullups=R1/R2 4.7K to VCC` |
| GPIO 与控制信号 | 产品正文中的 M5Core GPIO 映射 | `documented_data_gpio=G36`；`documented_clock_gpio=G26`；`schematic_data_net=DOUT`；`schematic_clock_net=PD_SCK` |
| 其他事实 | 产品正文中的 10SPS 输出速率 | `documented_rate=10SPS`；`rate_pin=U1 RATE pin15`；`schematic_rate_label=null` |
| 关键网络 | 模拟地与公共地连接 | `analog_ground=U1 AGND pin5`；`host_ground=J1 pin4`；`sensor_return=J2 pin3 E-`；`channel_b=INPB/INNB`；`net=GND` |

## 待确认事项

- `gpio.documented-host-map`：产品正文将 DOUT/DAT 映射到 G36、PD_SCK/CLK 映射到 G26，但当前原理图的 J1 仅标注 DOUT、PD_SCK、VCC、GND，没有出现 G36 或 G26 网络名，无法从原理图独立确认该 GPIO 映射。（证据：图 9043dc2106c5 / 第 1 页 / 第 1 页右侧 Connect to M5Core，J1 仅标 DOUT/PD_SCK/VCC/GND）
- `other.documented-output-rate`：产品正文给出 10SPS 输出数据率，但当前原理图未为 RATE pin15 标注 10SPS、逻辑电平或速率选择说明，因此该速率不能仅凭原理图确认。（证据：图 9043dc2106c5 / 第 1 页 / 第 1 页 U1 右上 RATE pin15，未标注速率或明确速率选择网络名）
- `review.host-gpio-map`：Scales Kit 的目标主控与线缆是否固定将 DOUT 接 G36、PD_SCK 接 G26？；原因：当前原理图只给出 J1 功能名，没有 G36/G26 网络名；GPIO 映射来自产品正文，可能依赖目标主控或转接线。
- `review.output-rate`：当前硬件版本的 HX711 RATE 配置是否确认为 10SPS？；原因：产品正文写 10SPS，但原理图未清晰标注 RATE pin15 的选择电平或速率说明。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9043dc2106c5c38879d045175e84f198358cb75617b848085864aab946a0faf2` | `https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_sch_01.webp` |

---

源文档：`zh_CN/app/scales_kit.md`

源文档 SHA-256：`ec4f5979711083766eb14aea40302187f284953b5226fc5b220404432ef78c4f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
