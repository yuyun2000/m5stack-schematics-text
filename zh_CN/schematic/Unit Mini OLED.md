# Unit Mini OLED 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini OLED |
| SKU | U166 |
| 产品 ID | `unit-mini-oled-da4ed5824b0e` |
| 源文档 | `zh_CN/unit/MiniOLED Unit.md` |

## 概述

Unit Mini OLED 通过 J1、J2 两个并联 HY-2.0_IIC 接口接入 SCL、SDA、+5V 和 GND，R1/R2 各 4.7 kΩ 将 SDA/SCL 上拉至 +3.3V。U1 HT7533 将 +5V 转为 +3.3V，供 FPC2 `0.5K-HX-16PWB` 16 针 OLED 接口。FPC2 使用 D0/D1/D2 连接 I2C，C4/C5 构成 C2P/C2N、C1P/C1N 电荷泵电容，另有 RES、VCOMH、VCC 和电源去耦网络。

## 检索关键词

`Unit Mini OLED`、`U166`、`0.5K-HX-16PWB`、`SSD1315`、`HT7533`、`OLED`、`0.42 inch`、`72x40`、`I2C`、`0x3C`、`SCL`、`SDA`、`D0`、`D1`、`D2`、`J1`、`J2`、`HY-2.0_IIC`、`+5V`、`+3.3V`、`R1 4.7K`、`R2 4.7K`、`C1P`、`C1N`、`C2P`、`C2N`、`VBAT`、`VDD`、`VCC`、`VCOMH`、`BS1`、`CS`、`RES`、`DC`、`white OLED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| FPC2 | 0.5K-HX-16PWB | 16 针 OLED 面板/控制接口 | 图 7a4c500b581d / 第 1 页 / 页 1 网格 B3-C3，FPC2 16 针器件下方标注 0.5K-HX-16PWB |
| U1 | HT7533 | +5V 至 +3.3V 线性稳压器 | 图 7a4c500b581d / 第 1 页 / 页 1 网格 B2，U1 下方标注 HT7533，VIN/VOUT 接 +5V/+3.3V |
| J1 | HY-2.0_IIC | 第一组 I2C 与 +5V 接口 | 图 7a4c500b581d / 第 1 页 / 页 1 网格 A2，J1 标注 HY-2.0_IIC，针脚为 GND、VCC、IIC_SDA、IIC_SCL |
| J2 | HY-2.0_IIC | 第二组 I2C 与 +5V 菊花链接口 | 图 7a4c500b581d / 第 1 页 / 页 1 网格 A3，J2 标注 HY-2.0_IIC，针脚为 GND、VCC、IIC_SDA、IIC_SCL |

## 系统结构

### FPC2 OLED 接口

FPC2 型号标注 0.5K-HX-16PWB，是 16 针 OLED 接口，连接电荷泵、电源、模式控制、复位和 I2C 数据网络。

- 参数与网络：`reference=FPC2`；`part_number=0.5K-HX-16PWB`；`pins=16`；`host_bus=I2C`；`charge_pump_pins=C2P,C2N,C1P,C1N`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 FPC2 型号与 1 至 16 脚完整列表

## 电源

### U1 HT7533

U1 HT7533 的 VIN pin 2 接 +5V，VOUT pin 3 输出 +3.3V，GND pin 1 接地。

- 参数与网络：`reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 B2 U1 引脚号与 +5V/+3.3V/GND 网络

### U1 输入输出电容

C2、C3 均为 10 uF (106) ±10% 10V，分别连接在 U1 的 +5V 输入、+3.3V 输出与 GND 之间。

- 参数与网络：`input_capacitor=C2 10uF (106) +/-10% 10V`；`output_capacitor=C3 10uF (106) +/-10% 10V`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 B1-B2 U1 两侧 C2/C3

### +5V 接口去耦

C1 为 100 nF (104) ±10%，连接在 J1/J2 共用的 +5V 与 GND 网络之间。

- 参数与网络：`capacitor=C1 100nF (104) +/-10%`；`rail=+5V`；`return=GND`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 A2 J1 左侧 C1 与 +5V/GND

### FPC2 3.3V 供电

FPC2 VBAT pin 5 和 VDD pin 7 连接 +3.3V，VSS pin 6 接 GND；C6 10 uF 与 C7 100 nF 并联在 +3.3V 与 GND 之间。

- 参数与网络：`supply_pins=VBAT/pin 5,VDD/pin 7`；`rail=+3.3V`；`ground_pin=VSS/pin 6`；`decoupling=C6 10uF,C7 100nF`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 B3-C3 FPC2 VBAT/VSS/VDD 与 C6/C7 网络

### FPC2 电荷泵电容

C4 1 uF/50V 跨接 FPC2 C2P pin 1 与 C2N pin 2；C5 1 uF/50V 跨接 C1P pin 3 与 C1N pin 4。

- 参数与网络：`c2_pump=C4 1uF/50V between C2P/pin 1 and C2N/pin 2`；`c1_pump=C5 1uF/50V between C1P/pin 3 and C1N/pin 4`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 B3 FPC2 pins 1-4 与 C4/C5

## 接口

### J1 I2C 接口

J1 的 1 至 4 脚依次连接 SCL、SDA、+5V、GND，内部针脚名为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 A2 J1 脚号、内外网络名与电源

### J2 I2C 接口

J2 的 1 至 4 脚依次连接 SCL、SDA、+5V、GND，内部针脚名为 IIC_SCL、IIC_SDA、VCC、GND。

- 参数与网络：`reference=J2`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 A3 J2 脚号、内外网络名与电源

## 总线

### J1/J2 并联 I2C

J1 与 J2 的 SCL、SDA、+5V、GND 对应针脚直接并联，两个接口电气等价并支持总线菊花链。

- 参数与网络：`connectors=J1,J2`；`shared_nets=SCL,SDA,+5V,GND`；`topology=direct parallel`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 J1 至 J2 的四条连续对应网络

### I2C 上拉

R1、R2 均为 4.7 kΩ (4701) ±1%，分别将 SDA、SCL 上拉至 +3.3V。

- 参数与网络：`sda_pullup=R1 4.7k (4701) +/-1% to +3.3V`；`scl_pullup=R2 4.7k (4701) +/-1% to +3.3V`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 A2-A3 R1/R2 与 SDA/SCL、+3.3V 网络

### FPC2 I2C 数据连接

SCL 连接 FPC2 D0 引脚 12；SDA 连接 D1 引脚 13，并在接口处连接 D2 引脚 14。

- 参数与网络：`scl=FPC2 D0/pin 12`；`sda=FPC2 D1/pin 13 and D2/pin 14`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 C3 FPC2 D0/D1/D2 pins 12-14 与 SCL/SDA 网络

## GPIO 与控制信号

### FPC2 模式配置

FPC2 BS1 pin 8 通过 R3 4.7 kΩ 上拉至 +3.3V；CS pin 9 与 DC pin 11 连接 GND。

- 参数与网络：`BS1=pin 8,R3 4.7k to +3.3V`；`CS=pin 9 to GND`；`DC=pin 11 to GND`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 C3 FPC2 BS1/CS/DC 与 R3、+3.3V、GND 网络

## 复位

### FPC2 RES

FPC2 RES pin 10 通过 R4 4.7 kΩ 上拉至 +3.3V，并通过 C8 1 uF 连接 GND。

- 参数与网络：`reset_pin=FPC2 RES/pin 10`；`pullup=R4 4.7k to +3.3V`；`capacitor=C8 1uF to GND`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 C2-C3 R4、RES pin 10 与 C8

## 保护电路

### 接口与电源保护

本页未显示 TVS/ESD、保险丝、反接保护或负载开关器件。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 全图仅含连接器、LDO、FPC2、阻容与直接连线

## 模拟电路

### FPC2 VCOMH 与 VCC

FPC2 VCOMH pin 15 通过 C9 4.7 uF 连接 GND；VCC pin 16 使用 C10 4.7 uF 与 C11 100 nF 对 GND 去耦。

- 参数与网络：`vcomh=pin 15,C9 4.7uF to GND`；`vcc=pin 16,C10 4.7uF and C11 100nF to GND`
- 证据：图 7a4c500b581d / 第 1 页 / 页 1 网格 C2-C3 FPC2 VCOMH/VCC pins 15/16 与 C9/C10/C11

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | FPC2 OLED 接口 | `reference=FPC2`；`part_number=0.5K-HX-16PWB`；`pins=16`；`host_bus=I2C`；`charge_pump_pins=C2P,C2N,C1P,C1N` |
| 接口 | J1 I2C 接口 | `reference=J1`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional` |
| 接口 | J2 I2C 接口 | `reference=J2`；`pinout=1:SCL/IIC_SCL,2:SDA/IIC_SDA,3:+5V/VCC,4:GND`；`signal_direction=SCL/SDA bidirectional` |
| 总线 | J1/J2 并联 I2C | `connectors=J1,J2`；`shared_nets=SCL,SDA,+5V,GND`；`topology=direct parallel` |
| 总线 | I2C 上拉 | `sda_pullup=R1 4.7k (4701) +/-1% to +3.3V`；`scl_pullup=R2 4.7k (4701) +/-1% to +3.3V` |
| 总线 | FPC2 I2C 数据连接 | `scl=FPC2 D0/pin 12`；`sda=FPC2 D1/pin 13 and D2/pin 14` |
| 总线地址 | OLED I2C 地址 | `documented_address=0x3C`；`schematic_address=null`；`address_select=null` |
| 电源 | U1 HT7533 | `reference=U1`；`part_number=HT7533`；`input=VIN/pin 2/+5V`；`output=VOUT/pin 3/+3.3V`；`ground=GND/pin 1` |
| 电源 | U1 输入输出电容 | `input_capacitor=C2 10uF (106) +/-10% 10V`；`output_capacitor=C3 10uF (106) +/-10% 10V` |
| 电源 | +5V 接口去耦 | `capacitor=C1 100nF (104) +/-10%`；`rail=+5V`；`return=GND` |
| 电源 | FPC2 3.3V 供电 | `supply_pins=VBAT/pin 5,VDD/pin 7`；`rail=+3.3V`；`ground_pin=VSS/pin 6`；`decoupling=C6 10uF,C7 100nF` |
| 电源 | FPC2 电荷泵电容 | `c2_pump=C4 1uF/50V between C2P/pin 1 and C2N/pin 2`；`c1_pump=C5 1uF/50V between C1P/pin 3 and C1N/pin 4` |
| GPIO 与控制信号 | FPC2 模式配置 | `BS1=pin 8,R3 4.7k to +3.3V`；`CS=pin 9 to GND`；`DC=pin 11 to GND` |
| 复位 | FPC2 RES | `reset_pin=FPC2 RES/pin 10`；`pullup=R4 4.7k to +3.3V`；`capacitor=C8 1uF to GND` |
| 模拟电路 | FPC2 VCOMH 与 VCC | `vcomh=pin 15,C9 4.7uF to GND`；`vcc=pin 16,C10 4.7uF and C11 100nF to GND` |
| 核心器件 | OLED 控制器型号 | `documented_controller=SSD1315`；`schematic_connector=FPC2 0.5K-HX-16PWB`；`schematic_controller=null` |
| 其他事实 | OLED 面板参数 | `documented_size_inch=0.42`；`documented_resolution=72x40`；`documented_color=white monochrome`；`documented_active_area_mm=9.196x5.18`；`schematic_panel_parameters=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false` |

## 待确认事项

- `address.i2c`：产品正文标注 I2C 地址 0x3C，但本页原理图没有地址值、SA0 引脚或地址选择网络。（证据：图 7a4c500b581d / 第 1 页 / 页 1 J1/J2 SCL/SDA 至 FPC2 D0-D2 的完整链路未打印地址）
- `component.controller`：产品正文标注 SSD1315 控制器，但本页原理图只标出 FPC2 `0.5K-HX-16PWB`，没有 SSD1315 字样。（证据：图 7a4c500b581d / 第 1 页 / 页 1 FPC2 仅标注 0.5K-HX-16PWB，页面无 SSD1315 字样）
- `other.display_parameters`：产品正文描述 0.42 英寸、72×40、单色白色、9.196×5.18 mm 显示区；这些几何和光学参数未在本页原理图中标注。（证据：图 7a4c500b581d / 第 1 页 / 页 1 FPC2 针脚与外围电路未打印尺寸、分辨率或颜色）
- `review.i2c_address`：当前 OLED 控制器的 7 位 I2C 地址是否固定为 0x3C？；原因：原理图没有地址值或地址选择网络。
- `review.controller`：FPC2 面板内部控制器是否确实为 SSD1315，完整面板料号是什么？；原因：原理图只给出 16 针 FPC 连接器料号，没有控制器型号。
- `review.display_parameters`：0.42 英寸、72×40、白色和显示区域参数是否适用于当前 FPC2 面板版本？；原因：原理图没有面板几何或光学参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7a4c500b581dcf041742059170ccf86aa553afc4f86db4dc648e29a9daf93908` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/621/Sch_UNIT-MiniOLED_sch_01.png` |

---

源文档：`zh_CN/unit/MiniOLED Unit.md`

源文档 SHA-256：`cef12fa1b4267ea06a27cc83e4b963bb548b45fb663cf851c27170e5f717d682`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
