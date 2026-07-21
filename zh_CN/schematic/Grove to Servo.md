# Grove to Servo 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Grove to Servo |
| SKU | A039 |
| 产品 ID | `grove-to-servo-9672db30be29` |
| 源文档 | `zh_CN/accessory/converter/Grove_to_Servo.md` |

## 概述

Grove to Servo 是一块纯无源三线转接板。J1 GROVE_IO 的 IO1 连接信号网络 S，VCC 与 GND 直接传递到 J2 1X3 2.54 的 pin2 与 pin3，S 连接 J2 pin1；J1 IO2 明确未连接。原理图未画电源转换、电平转换、缓冲、保护、滤波、地址或任何主动器件，因此输出电压与信号电平完全由外部 Grove 端决定。

## 检索关键词

`Grove to Servo`、`A039`、`GROVE_IO`、`J1`、`J2`、`1X3 2.54`、`HY2.0-4P`、`2.54-3P`、`IO1`、`IO2`、`S`、`Signal`、`VCC`、`GND`、`servo adapter`、`passive adapter`、`direct connection`、`IO2 NC`、`Grove VCC`、`servo signal`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J1 | GROVE_IO | 四针 Grove 输入连接器，使用 IO1/S、VCC 和 GND，IO2 未连接 | 图 2c64ac66aac6 / 第 1 页 / 第 1 页网格 B2-C2，J1 GROVE_IO 的 IO2/IO1/VCC/GND |
| J2 | 1X3 2.54 | 三针输出连接器，pin1 S、pin2 VCC、pin3 GND | 图 2c64ac66aac6 / 第 1 页 / 第 1 页网格 B3-C3，J2 1X3 2.54 pin1-pin3 |

## 系统结构

### Grove to Servo 无源转接架构

整页仅包含 J1 GROVE_IO 与 J2 1X3 2.54 两个连接器，S/VCC/GND 三线直接相连，IO2 悬空；板上没有主动器件。

- 参数与网络：`input=J1 GROVE_IO`；`output=J2 1X3 2.54`；`connected_nets=S,VCC,GND`；`unused=J1 IO2`；`active_components=null`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页完整原理图

### 数字、模拟和通信子系统

板上没有 MCU、存储器、时钟、复位、调试、I2C、SPI、UART、CAN、RS-485、USB、传感器、射频、音频或模拟调理器件；S 仅为未定义协议的直通信号。

- 参数与网络：`mcu=null`；`storage=null`；`clock=null`；`reset=null`；`debug=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sensor=null`；`rf=null`；`audio=null`；`analog=null`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页完整原理图

## 电源

### VCC 电源直通

J1 VCC 与 J2 pin2 VCC 通过同名网络直接相连，板上没有 LDO、DC-DC、负载开关、保险丝、限流或去耦电容。

- 参数与网络：`input=J1 VCC`；`output=J2 pin2 VCC`；`converter=null`；`switch=null`；`fuse=null`；`current_limit=null`；`decoupling=null`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J1/J2 VCC 同名网络与完整电源路径

## 接口

### J1 Grove 接口

J1 的 IO2 引脚带未连接标记；IO1 接 S，VCC 接 VCC，GND 接 GND。S 为从 Grove 侧进入转接板并送往 J2 的单线控制信号。

- 参数与网络：`connector=J1 GROVE_IO`；`io2=no connection`；`io1=S`；`power=VCC`；`ground=GND`；`signal_direction=input to J2`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页网格 B2-C2，J1 IO2 未连接标记与 IO1/S/VCC/GND

### J2 三针接口

J2 标为 1X3 2.54，pin1 接 S、pin2 接 VCC、pin3 接 GND。

- 参数与网络：`connector=J2 1X3 2.54`；`pin1=S signal`；`pin2=VCC`；`pin3=GND`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页网格 B3-C3，J2 pin1 S、pin2 VCC、pin3 GND

## 保护电路

### 保护与滤波器件

唯一原理图页面未画 ESD、TVS、保险丝、反接保护、过流保护、浪涌抑制、信号串阻或电源滤波器件。

- 参数与网络：`esd=null`；`tvs=null`；`fuse=null`；`reverse_protection=null`；`overcurrent=null`；`surge=null`；`signal_resistor=null`；`filter=null`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页完整原理图，仅 J1/J2

## 关键网络

### S 信号直通

J1 IO1 与 J2 pin1 通过同名网络 S 直接相连，中间没有串联电阻、缓冲器、电平转换器或反相器。

- 参数与网络：`source=J1 IO1`；`network=S`；`destination=J2 pin1`；`series_component=null`；`buffer=null`；`level_shifter=null`；`inversion=false`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J1 IO1-S 与 J2 pin1-S 同名网络

### GND 直通

J1 GND 与 J2 pin3 GND 通过同名网络直接相连。

- 参数与网络：`source=J1 GND`；`destination=J2 pin3`；`network=GND`
- 证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J1/J2 GND 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Grove to Servo 无源转接架构 | `input=J1 GROVE_IO`；`output=J2 1X3 2.54`；`connected_nets=S,VCC,GND`；`unused=J1 IO2`；`active_components=null` |
| 接口 | J1 Grove 接口 | `connector=J1 GROVE_IO`；`io2=no connection`；`io1=S`；`power=VCC`；`ground=GND`；`signal_direction=input to J2` |
| 接口 | J2 三针接口 | `connector=J2 1X3 2.54`；`pin1=S signal`；`pin2=VCC`；`pin3=GND` |
| 关键网络 | S 信号直通 | `source=J1 IO1`；`network=S`；`destination=J2 pin1`；`series_component=null`；`buffer=null`；`level_shifter=null`；`inversion=false` |
| 电源 | VCC 电源直通 | `input=J1 VCC`；`output=J2 pin2 VCC`；`converter=null`；`switch=null`；`fuse=null`；`current_limit=null`；`decoupling=null` |
| 关键网络 | GND 直通 | `source=J1 GND`；`destination=J2 pin3`；`network=GND` |
| 保护电路 | 保护与滤波器件 | `esd=null`；`tvs=null`；`fuse=null`；`reverse_protection=null`；`overcurrent=null`；`surge=null`；`signal_resistor=null`；`filter=null` |
| 系统结构 | 数字、模拟和通信子系统 | `mcu=null`；`storage=null`；`clock=null`；`reset=null`；`debug=null`；`i2c=null`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sensor=null`；`rf=null`；`audio=null`；`analog=null` |
| 接口 | J2 公针与弯脚结构 | `documented_gender=male`；`documented_pitch=2.54mm`；`documented_style=right-angle`；`schematic_label=1X3 2.54`；`pin_length=null`；`mating_cycles=null`；`tolerance=null` |
| GPIO 与控制信号 | 舵机控制信号协议 | `documented_role=servo Signal`；`network=S`；`input=J1 IO1`；`output=J2 pin1`；`pwm_frequency=null`；`pulse_width=null`；`logic_level=null`；`polarity=null` |
| 电源 | VCC 与信号电气额定值 | `vcc_voltage=null`；`max_current=null`；`contact_resistance=null`；`signal_tolerance=null`；`esd_rating=null`；`servo_power=null` |

## 待确认事项

- `interface.documented-mechanics`：产品正文称 J2 为 2.54-3P 公针并采用弯脚设计；原理图只标 J2 为 1X3 2.54，没有针座性别、弯角方向、引脚长度、额定插拔次数或机械公差。（证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J2 仅标 1X3 2.54）
- `gpio.documented-servo-signal`：产品正文将 S 描述为舵机 Signal；原理图只确认 J1 IO1 到 J2 pin1 的直通连接，没有标 PWM 频率、脉宽范围、逻辑电平、极性、刷新率或兼容的舵机协议。（证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J1 IO1-S-J2 pin1，无协议信息）
- `power.documented-ratings`：原理图未标 VCC 电压范围、最大电流、接触电阻、S 信号容限、ESD 等级或可驱动舵机功率；纯直通连接不能证明具体额定值。（证据：图 2c64ac66aac6 / 第 1 页 / 第 1 页 J1/J2 S/VCC/GND 直连，无额定值）
- `review.connector-mechanics`：请用量产 BOM、连接器料号或实物确认 J2 的公针性别、弯脚方向、针长与机械额定值。；原因：原理图只给出 1X3 2.54，不包含机械属性。
- `review.servo-protocol`：请依据目标舵机和主控平台确认 S 的逻辑电平、PWM 周期、脉宽、极性及兼容范围。；原因：原理图只显示信号直通，不定义舵机协议。
- `review.electrical-ratings`：请依据连接器 datasheet 和 PCB 设计确认 VCC 电压/电流、接触电阻、S 电平容限及 ESD 等级。；原因：原理图没有任何电气额定参数或保护器件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2c64ac66aac69af316fc7cdea9455a236cf7c70ed8cd56d920a66a4d440bc1ce` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1246/A039-sche_page_01.png` |

---

源文档：`zh_CN/accessory/converter/Grove_to_Servo.md`

源文档 SHA-256：`ac65dcc7083efc5e4f16d7aa92ff7e138f9eae1b5238dcb10d636ae9c73c6c38`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
