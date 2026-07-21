# Unit DLight 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DLight |
| SKU | U136 |
| 产品 ID | `unit-dlight-ef874caa3331` |
| 源文档 | `zh_CN/unit/DLight Unit.md` |

## 概述

Unit DLight 以 BH1750FVI-TR（U1）作为数字环境光传感器，SCL_3V3 与 SDA_3V3 通过 J1 连接外部 I2C 主机，ADDR pin 2 接 GND。U1 的 SCL、SDA 与 DVI 三条网络均由 4.7KΩ 上拉到 +3.3V，原理图直接标注检测范围 1~65535 lx。J1 输入的 VCC 经 HT7533-3.3V（U2）稳压为 +3.3V，P1/P2 额外引出传感器信号和电源。页面未打印 VCC 数值、十六进制 I2C 地址或 ADC 深度、光谱灵敏度等性能参数。

## 检索关键词

`Unit DLight`、`U136`、`BH1750FVI-TR`、`BH1750FVI`、`HT7533-3.3V`、`IIC_Socket_4P`、`Header 4`、`I2C`、`0x23`、`SCL_3V3`、`SDA_3V3`、`DVI_3V3`、`ADDR`、`+3.3V`、`VCC`、`1~65535 lx`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`C1 100nF`、`C2 100nF`、`C3 22uF`、`C4 10uF`、`ambient light`、`16-bit ADC`、`560nm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | BH1750FVI-TR | 通过 I2C 输出环境光照度数据的数字光传感器 | 图 ea8db8f9b3de / 第 1 页 / 页 1 左上 U1 BH1750FVI-TR：VCC/ADDR/GND/SDA/DVI/SCL/EP pins 1~7 |
| U2 | HT7533-3.3V | 将 J1 VCC 稳压为 +3.3V | 图 ea8db8f9b3de / 第 1 页 / 页 1 下部 U2 HT7533-3.3V，VIN pin 2 接 VCC、VOUT pin 3 接 +3.3V、GND pin 1 接地 |
| J1 | IIC_Socket_4P | 外部 I2C、VCC 与 GND 接口 | 图 ea8db8f9b3de / 第 1 页 / 页 1 右下 J1 IIC_Socket_4P：pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC、pin 4 GND |
| P1 | Header 4 | 引出 SCL_3V3、SDA_3V3、DVI_3V3 的内部四针连接器 | 图 ea8db8f9b3de / 第 1 页 / 页 1 中左 P1 Header 4：pins 1/2/3 为 SCL_3V3/SDA_3V3/DVI_3V3，pin 4 未接 |
| P2 | Header 4 | 引出 +3.3V 与 GND 的内部四针连接器 | 图 ea8db8f9b3de / 第 1 页 / 页 1 中部 P2 Header 4：pin 1 接 +3.3V，pin 4 接 GND，pins 2/3 未接 |
| R1/R2/R3 | 4.7KΩ | SCL_3V3、DVI_3V3、SDA_3V3 到 +3.3V 的上拉电阻 | 图 ea8db8f9b3de / 第 1 页 / 页 1 上部：R1/R2/R3 均 4.7KΩ，左端分别接 SCL_3V3/DVI_3V3/SDA_3V3，右端共接 +3.3V |
| C1 | 100nF | J1 VCC 输入去耦电容 | 图 ea8db8f9b3de / 第 1 页 / 页 1 右下 C1 100nF 跨接 VCC 与 GND |
| C2/C3/C4 | 100nF / 22uF / 10uF | HT7533 的 +3.3V 输出与 VCC 输入滤波电容 | 图 ea8db8f9b3de / 第 1 页 / 页 1 下部：C2 100nF/C3 22uF 跨 +3.3V-GND，C4 10uF 跨 VCC-GND |

## 系统结构

### Unit DLight

J1 提供 VCC 和 I2C，U2 HT7533-3.3V 产生 +3.3V，U1 BH1750FVI-TR 由 +3.3V 供电并通过 SCL_3V3/SDA_3V3 与外部主机通信；P1/P2 引出传感器信号与电源。

- 参数与网络：`sensor=U1 BH1750FVI-TR`；`regulator=U2 HT7533-3.3V`；`external_interface=J1 IIC_Socket_4P`；`signal_header=P1`；`power_header=P2`；`power_path=VCC->U2->+3.3V`
- 证据：图 ea8db8f9b3de / 第 1 页 / 整页：U1/U2/J1/P1/P2 及 VCC/+3.3V/SCL_3V3/SDA_3V3

## 电源

### SCL/SDA/DVI 上拉

R1、R2、R3 均为 4.7KΩ，分别将 SCL_3V3、DVI_3V3、SDA_3V3 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ`；`dvi_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=+3.3V`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 上部 R1/R2/R3 与 SCL_3V3/DVI_3V3/SDA_3V3/+3.3V

### U2 HT7533-3.3V

U2 VIN pin 2 接 VCC，VOUT pin 3 输出 +3.3V，GND pin 1 接地；C4 10uF 位于输入侧，C2 100nF 与 C3 22uF 位于输出侧。

- 参数与网络：`input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C4 10uF`；`output_capacitors=C2 100nF,C3 22uF`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 下部 U2/C2/C3/C4 与 VCC/+3.3V/GND

### U1 +3.3V 供电

U1 VCC pin 1 接 +3.3V，GND pin 3 与 EP pin 7 接 GND；传感器周围没有单独画本地去耦电容，+3.3V 轨由 U2 输出侧 C2/C3 去耦。

- 参数与网络：`supply_pin=U1 pin 1`；`rail=+3.3V`；`ground_pins=U1 pins 3,7`；`rail_decoupling=C2 100nF,C3 22uF`；`local_sensor_capacitor=null`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 U1 VCC/GND/EP 与下部 +3.3V C2/C3 网络

## 接口

### J1 IIC_Socket_4P

J1 pin 1 接 SCL_3V3（连接器内标 IIC_SCL），pin 2 接 SDA_3V3（标 IIC_SDA），pin 3 接 VCC，pin 4 接 GND。

- 参数与网络：`pin_1=IIC_SCL,SCL_3V3`；`pin_2=IIC_SDA,SDA_3V3`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 右下 J1 pins 1~4 与 SCL_3V3/SDA_3V3/VCC/GND

### DVI_3V3

U1 DVI pin 5 连接 DVI_3V3，R2 4.7KΩ将该网拉至 +3.3V，P1 pin 3 将 DVI_3V3 引出；J1 不引出 DVI。

- 参数与网络：`sensor_pin=U1 DVI pin 5`；`net=DVI_3V3`；`pullup=R2 4.7KΩ to +3.3V`；`header=P1 pin 3`；`external_i2c_socket=not connected`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 上部 U1 pin 5/R2 与中左 P1 pin 3 的 DVI_3V3 同名网络

### P1 Header 4

P1 pin 1 接 SCL_3V3，pin 2 接 SDA_3V3，pin 3 接 DVI_3V3，pin 4 在原理图中未连接。

- 参数与网络：`pin_1=SCL_3V3`；`pin_2=SDA_3V3`；`pin_3=DVI_3V3`；`pin_4=no-connect`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 中左 P1 Header 4 的 pins 1~4 与三条信号及 pin 4 未连接标记

### P2 Header 4

P2 pin 1 接 +3.3V，pin 4 接 GND，pins 2/3 在原理图中未连接。

- 参数与网络：`pin_1=+3.3V`；`pin_2=no-connect`；`pin_3=no-connect`；`pin_4=GND`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 中部 P2 Header 4 的 +3.3V/GND 连线和 pins 2/3 未连接端点

## 总线

### BH1750FVI I2C

J1 pin 1 的 SCL_3V3 连接 U1 SCL pin 6，J1 pin 2 的 SDA_3V3 连接 U1 SDA pin 4；两线均由 4.7KΩ 上拉至 +3.3V。

- 参数与网络：`device=U1 BH1750FVI-TR`；`scl=J1.1 SCL_3V3 to U1.6`；`sda=J1.2 SDA_3V3 to U1.4`；`pullups=R1/R3 4.7KΩ`；`level_rail=+3.3V`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 U1/J1/P1 的 SCL_3V3/SDA_3V3 同名网络及 R1/R3

## GPIO 与控制信号

### U1 ADDR

U1 ADDR pin 2 与 GND pin 3 共接 GND，页面没有绘出地址跳线或可变选择器。

- 参数与网络：`pin=ADDR pin 2`；`strap=GND`；`shared_ground_pin=pin 3`；`configurable_selector=null`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 左上 U1 pins 2/3 的公共竖线、节点和 GND 符号

## 时钟

### 外部时钟

本页没有绘出晶振、振荡器或外部时钟网络，U1 对外仅有电源、ADDR、SCL、SDA、DVI 与 EP。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`clock_net=null`
- 证据：图 ea8db8f9b3de / 第 1 页 / 整页无晶振/振荡器位号；U1 七引脚符号无时钟输入

## 保护电路

### I2C 与电源保护

本页没有绘出 TVS、ESD 阵列、保险丝或反接保护器件。

- 参数与网络：`i2c_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`
- 证据：图 ea8db8f9b3de / 第 1 页 / 整页可见位号 U1/U2/J1/P1/P2/R1-R3/C1-C4，无保护器件位号

## 关键网络

### Unit DLight 关键网络索引

关键路径为 J1 pin 3 VCC→U2→+3.3V→U1 pin 1，J1 pin 1 SCL_3V3→U1 pin 6/P1 pin 1，J1 pin 2 SDA_3V3→U1 pin 4/P1 pin 2，以及 U1 DVI pin 5→P1 pin 3。

- 参数与网络：`power_path=J1.3-U2.2/U2.3-+3.3V-U1.1`；`scl_path=J1.1-U1.6-P1.1`；`sda_path=J1.2-U1.4-P1.2`；`dvi_path=U1.5-P1.3`；`address_strap=U1.2-GND`
- 证据：图 ea8db8f9b3de / 第 1 页 / 整页 VCC/+3.3V/SCL_3V3/SDA_3V3/DVI_3V3/GND 同名网络

## 传感器

### U1 BH1750FVI-TR

U1 VCC pin 1 接 +3.3V，ADDR pin 2 与 GND pin 3 接 GND，SDA pin 4 接 SDA_3V3，DVI pin 5 接 DVI_3V3，SCL pin 6 接 SCL_3V3，EP pin 7 接 GND。

- 参数与网络：`pin_1=VCC,+3.3V`；`pin_2=ADDR,GND`；`pin_3=GND`；`pin_4=SDA,SDA_3V3`；`pin_5=DVI,DVI_3V3`；`pin_6=SCL,SCL_3V3`；`pin_7=EP,GND`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 左上 U1 pins 1~7、功能名和各网络

### 照度检测范围

原理图在 U1 下方直接标注照度范围为 1~65535 lx。

- 参数与网络：`minimum=1 lx`；`maximum=65535 lx`；`printed_text=1～65535 lx`；`sensor=BH1750FVI-TR`
- 证据：图 ea8db8f9b3de / 第 1 页 / 页 1 左上 U1 BH1750FVI-TR 下方蓝色文字 1～65535 lx

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit DLight | `sensor=U1 BH1750FVI-TR`；`regulator=U2 HT7533-3.3V`；`external_interface=J1 IIC_Socket_4P`；`signal_header=P1`；`power_header=P2`；`power_path=VCC->U2->+3.3V` |
| 传感器 | U1 BH1750FVI-TR | `pin_1=VCC,+3.3V`；`pin_2=ADDR,GND`；`pin_3=GND`；`pin_4=SDA,SDA_3V3`；`pin_5=DVI,DVI_3V3`；`pin_6=SCL,SCL_3V3`；`pin_7=EP,GND` |
| 传感器 | 照度检测范围 | `minimum=1 lx`；`maximum=65535 lx`；`printed_text=1～65535 lx`；`sensor=BH1750FVI-TR` |
| 接口 | J1 IIC_Socket_4P | `pin_1=IIC_SCL,SCL_3V3`；`pin_2=IIC_SDA,SDA_3V3`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | BH1750FVI I2C | `device=U1 BH1750FVI-TR`；`scl=J1.1 SCL_3V3 to U1.6`；`sda=J1.2 SDA_3V3 to U1.4`；`pullups=R1/R3 4.7KΩ`；`level_rail=+3.3V` |
| 电源 | SCL/SDA/DVI 上拉 | `scl_pullup=R1 4.7KΩ`；`dvi_pullup=R2 4.7KΩ`；`sda_pullup=R3 4.7KΩ`；`rail=+3.3V` |
| GPIO 与控制信号 | U1 ADDR | `pin=ADDR pin 2`；`strap=GND`；`shared_ground_pin=pin 3`；`configurable_selector=null` |
| 总线地址 | Unit DLight I2C 地址 | `device=U1 BH1750FVI-TR`；`addr_pin=GND`；`schematic_address=null`；`address_rule_source_needed=BH1750FVI datasheet` |
| 接口 | DVI_3V3 | `sensor_pin=U1 DVI pin 5`；`net=DVI_3V3`；`pullup=R2 4.7KΩ to +3.3V`；`header=P1 pin 3`；`external_i2c_socket=not connected` |
| 接口 | P1 Header 4 | `pin_1=SCL_3V3`；`pin_2=SDA_3V3`；`pin_3=DVI_3V3`；`pin_4=no-connect` |
| 接口 | P2 Header 4 | `pin_1=+3.3V`；`pin_2=no-connect`；`pin_3=no-connect`；`pin_4=GND` |
| 电源 | U2 HT7533-3.3V | `input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C4 10uF`；`output_capacitors=C2 100nF,C3 22uF` |
| 电源 | U1 +3.3V 供电 | `supply_pin=U1 pin 1`；`rail=+3.3V`；`ground_pins=U1 pins 3,7`；`rail_decoupling=C2 100nF,C3 22uF`；`local_sensor_capacitor=null` |
| 电源 | J1 VCC 额定值 | `connector_pin=J1 pin 3`；`net=VCC`；`loads=U2 VIN,C1`；`schematic_voltage=null`；`generated_rail=+3.3V` |
| 传感器 | BH1750FVI 性能参数 | `printed_range=1~65535 lx`；`schematic_adc_bits=null`；`schematic_peak_wavelength=null`；`schematic_current=null`；`schematic_accuracy=null`；`schematic_conversion_time=null` |
| 时钟 | 外部时钟 | `external_crystal=null`；`external_oscillator=null`；`clock_net=null` |
| 保护电路 | I2C 与电源保护 | `i2c_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null` |
| 关键网络 | Unit DLight 关键网络索引 | `power_path=J1.3-U2.2/U2.3-+3.3V-U1.1`；`scl_path=J1.1-U1.6-P1.1`；`sda_path=J1.2-U1.4-P1.2`；`dvi_path=U1.5-P1.3`；`address_strap=U1.2-GND` |

## 待确认事项

- `address.i2c-not-printed`：原理图明确显示 ADDR pin 2 接 GND，但未打印十六进制 I2C 地址，数字地址需结合 BH1750FVI 的地址规则确认。（证据：图 ea8db8f9b3de / 第 1 页 / 页 1 U1 ADDR/SCL/SDA 区域，整页无 0x 地址文字）
- `power.vcc-rating-not-shown`：J1 pin 3、C1 和 U2 VIN 使用名为 VCC 的网络，但页面未打印 VCC 数值，无法仅凭该原理图确认接口额定供电电压。（证据：图 ea8db8f9b3de / 第 1 页 / 页 1 右下/下部 J1 pin 3-C1-U2 VIN 的 VCC 网络，无电压数值）
- `sensor.performance-not-shown`：原理图只明确标出 1~65535 lx 范围，没有打印 ADC 深度、峰值灵敏波长、工作电流、精度、分辨率或转换时间。（证据：图 ea8db8f9b3de / 第 1 页 / 页 1 U1 区域仅有型号、引脚及 1～65535 lx 文字，无其他性能参数）
- `review.i2c-address`：ADDR 接 GND 时，Unit DLight 的 I2C 地址是否为 0x23？；原因：原理图未打印数字地址，需要 BH1750FVI 数据手册的地址规则确认。
- `review.vcc-rating`：J1 pin 3 的 VCC 额定输入电压是多少？；原因：原理图只标 VCC，并显示 HT7533-3.3V 输出 +3.3V，没有打印输入电压数值。
- `review.sensor-performance`：当前产品的 ADC 深度、峰值灵敏波长、工作电流、测量精度与转换时间分别是多少？；原因：原理图只打印 1~65535 lx 范围，其余性能需用 BH1750FVI 数据手册与整机测试条件确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ea8db8f9b3de0579c82a612e6210f5859f063ca11fbd11a26bc4ba4d7eb6b326` | `https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-36ddf1b9-94ea-41d7-9162-0e31ee8f8130.webp` |

---

源文档：`zh_CN/unit/DLight Unit.md`

源文档 SHA-256：`a3852b46c76846aa561dcb964ff9016e8d265730b9fc9728537c292010af71a6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
