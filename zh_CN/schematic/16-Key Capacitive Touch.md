# 16-Key Capacitive Touch 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | 16-Key Capacitive Touch |
| SKU | U026 |
| 产品 ID | `16-key-capacitive-touch-ff4446a15faf` |
| 源文档 | `zh_CN/unit/makey.md` |

## 概述

该单页原理图显示 U3 ATMEGA328 由 8 MHz 晶振提供时钟，P1/P2 引出数字、模拟和电源网络，J1 提供 ISP 下载连接，J2 通过 SCL、SDA、VCC 和 GND 与 Core 相连。

## 检索关键词

`16-Key Capacitive Touch`、`U026`、`ATMEGA328`、`8MHz`、`I2C`、`IIC_SCL`、`IIC_SDA`、`ISP`、`RESET`、`PC4`、`PC5`、`P1`、`P2`、`J1`、`J2`、`470Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ATMEGA328 | 主控制器 | 图 62f6b72d6aa3 / 第 1 页 / 页面中央 U3 方框，器件值标注为 ATMEGA328 |
| Y1 | 8MHz | 主控制器晶振 | 图 62f6b72d6aa3 / 第 1 页 / 页面左上 Y1，连接 XTAL1/XTAL2，器件值标注 8MHz |
| J1 | ISP_Download | 六针 ISP 下载接口 | 图 62f6b72d6aa3 / 第 1 页 / 页面右上 J1，接口值标注 ISP_Download |
| J2 | IIC_Socket_4P | 连接 Core 的四针 IIC 接口 | 图 62f6b72d6aa3 / 第 1 页 / 页面右下 Connected to Core 区域的 J2，接口值标注 IIC_Socket_4P |
| P1 | Header 10 | D9 至 D0 网络引出排针 | 图 62f6b72d6aa3 / 第 1 页 / 页面左下 P1 Header 10 |
| P2 | Header 10 | 10 至 13、A0 至 A3、VCC 和 GND 网络引出排针 | 图 62f6b72d6aa3 / 第 1 页 / 页面左下 P2 Header 10 |

## 系统结构

### U3

U3 的器件型号标注为 ATMEGA328。

- 参数与网络：`reference=U3`；`part_number=ATMEGA328`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面中央 U3 方框及下方 ATMEGA328 标注

## 电源

### U3 供电

U3 的 AVCC 引脚 18 与 VCC 引脚 4、6 连接 VCC；GND 引脚 3、5、21 连接 GND。

- 参数与网络：`vcc_pins=18,4,6`；`ground_pins=3,5,21`；`rail=VCC`
- 证据：图 62f6b72d6aa3 / 第 1 页 / U3 右侧 AVCC/VCC/GND 引脚与 VCC、GND 网络

### J2 接口供电去耦

C3 为 100 nF，连接在 J2 所在 VCC 与 GND 网络之间。

- 参数与网络：`capacitor_reference=C3`；`capacitance_nf=100`；`rail=VCC`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面最右侧 J2 旁的 C3 100nF、VCC 与 GND 网络

## 接口

### J1 ISP 下载接口

J1 引出 VCC、RESET、SCK、MISO、MOSI 和 GND 六个网络。

- 参数与网络：`reference=J1`；`signals=VCC,RESET,SCK,MISO,MOSI,GND`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面右上 J1 ISP_Download 六条网络标注

### P1 排针

P1 的 1 至 10 脚依次连接 D9、D8、D7、D6、D5、D4、D3、D2、D1、D0。

- 参数与网络：`reference=P1`；`pinout=1:D9,2:D8,3:D7,4:D6,5:D5,6:D4,7:D3,8:D2,9:D1,10:D0`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面左下 P1 Header 10 的脚号和左侧网络标注

### P2 排针

P2 的 1 至 10 脚依次连接 10、11、12、13、A0、A1、A2、A3、VCC、GND 网络。

- 参数与网络：`reference=P2`；`pinout=1:10,2:11,3:12,4:13,5:A0,6:A1,7:A2,8:A3,9:VCC,10:GND`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面左下 P2 Header 10 的脚号和左侧网络标注

## 总线

### U3 与 J2 的 I2C 连接

U3 的 SCL 为 PC5/ADC5/SCL/PCINT13 引脚 28，SDA 为 PC4/ADC4/SDA/PCINT12 引脚 27；两条网络各经 470 Ω 串联电阻到 J2 的 IIC_SCL 与 IIC_SDA，J2 另外连接 VCC 和 GND。

- 参数与网络：`scl_mcu_pin=PC5/pin 28`；`sda_mcu_pin=PC4/pin 27`；`series_resistance_ohm=470`；`connector=J2`；`connector_pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND`
- 证据：图 62f6b72d6aa3 / 第 1 页 / U3 左侧 SDA/SCL 引脚标注及页面右下两只 470Ω 电阻和 J2 引脚标注

## 时钟

### Y1 与 U3

Y1 为 8 MHz 晶振，连接 U3 的 XTAL1 和 XTAL2；C1 与 C4 均为 22 pF，并分别从两条晶振网络接至 GND。

- 参数与网络：`crystal_reference=Y1`；`frequency_hz=8000000`；`capacitor_references=C1,C4`；`capacitance_pf=22`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面左上 XTAL1/XTAL2、Y1、C1、C4 与 GND 连接区域

## 复位

### U3 RESET

RESET 网络通过 R1 10 kΩ 连接 VCC，并通过 C2 100 nF 连接 GND。

- 参数与网络：`pullup_reference=R1`；`pullup_ohm=10000`；`capacitor_reference=C2`；`capacitance_nf=100`
- 证据：图 62f6b72d6aa3 / 第 1 页 / 页面中右 R1、RESET、C2、VCC 与 GND 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | U3 | `reference=U3`；`part_number=ATMEGA328` |
| 时钟 | Y1 与 U3 | `crystal_reference=Y1`；`frequency_hz=8000000`；`capacitor_references=C1,C4`；`capacitance_pf=22` |
| 复位 | U3 RESET | `pullup_reference=R1`；`pullup_ohm=10000`；`capacitor_reference=C2`；`capacitance_nf=100` |
| 电源 | U3 供电 | `vcc_pins=18,4,6`；`ground_pins=3,5,21`；`rail=VCC` |
| 接口 | J1 ISP 下载接口 | `reference=J1`；`signals=VCC,RESET,SCK,MISO,MOSI,GND` |
| 总线 | U3 与 J2 的 I2C 连接 | `scl_mcu_pin=PC5/pin 28`；`sda_mcu_pin=PC4/pin 27`；`series_resistance_ohm=470`；`connector=J2`；`connector_pinout=1:IIC_SCL,2:IIC_SDA,3:VCC,4:GND` |
| 总线 | I2C 从机地址 | `address=null` |
| 电源 | J2 接口供电去耦 | `capacitor_reference=C3`；`capacitance_nf=100`；`rail=VCC` |
| 接口 | P1 排针 | `reference=P1`；`pinout=1:D9,2:D8,3:D7,4:D6,5:D5,6:D4,7:D3,8:D2,9:D1,10:D0` |
| 接口 | P2 排针 | `reference=P2`；`pinout=1:10,2:11,3:12,4:13,5:A0,6:A1,7:A2,8:A3,9:VCC,10:GND` |

## 待确认事项

- `bus.i2c_address`：原理图未标注 I2C 从机地址，无法仅据本页确定地址值。（证据：图 62f6b72d6aa3 / 第 1 页 / 页面右下 J2 IIC_Socket_4P 区域仅标注 IIC_SCL、IIC_SDA、VCC、GND）
- `review.i2c_address`：当前固件实现的 I2C 从机地址是否为产品正文中的 0x51？；原因：原理图只给出 I2C 物理连接，没有地址选择网络或固件地址定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `62f6b72d6aa327063de5b1dfb5c80cd42b9668a8ddd8560dc9b841aef51627db` | `https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_sch_01.webp` |

---

源文档：`zh_CN/unit/makey.md`

源文档 SHA-256：`f44804bb62fefee5c285f62f224981bb1a08a3f15cda28ed6eae5263ca220403`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
