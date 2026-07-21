# Hat Servo 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Servo |
| SKU | U075 |
| 产品 ID | `hat-servo-35c2561dfa31` |
| 源文档 | `zh_CN/hat/hat-servo.md` |

## 概述

Hat Servo 的电气资源是一张三线功能映射图，明确显示 SERVO 的 G、V、S 分别连接 StickC 的 GND、5V、G26。第二张资源是单位为 mm 的机械尺寸图，给出外形高度、主体长度、舵机局部尺寸和安装孔距。两页均未显示器件位号、舵机完整型号、PWM 波形、驱动器、电源调节、保护或去耦电路，因此正文中的 ES9251II、PWM 控制与 145°±10°行程不能作为原理图确认事实。

## 检索关键词

`Hat Servo`、`U075`、`SERVO`、`StickC`、`G`、`V`、`S`、`GND`、`5V`、`G26`、`ES9251II`、`PWM`、`145°±10°`、`34.94mm`、`29.9mm`、`21.3mm`、`18.3mm`、`13.7mm`、`10.7mm`、`15.9mm`、`12.7mm`、`舵机`、`信号线`、`机械尺寸`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| SERVO | 未标注 | 三线舵机功能块，G/V/S 分别连接 GND/5V/G26 | 图 ccf74e453732 / 第 1 页 / 页面左侧 SERVO 方框：三条端子自上而下标注 G、V、S |
| StickC | 未标注 | 主机功能块，向舵机提供 GND、5V 与 G26 控制信号 | 图 ccf74e453732 / 第 1 页 / 页面右侧橙色 StickC 方框：三条端子自上而下标注 GND、5V、G26 |
| Hat Servo mechanical assembly | 未标注 | 带舵机输出轴与 8 针 HAT 插接排针的机械装配体 | 图 646dfe4b5549 / 第 1 页 / 机械尺寸页的正视、侧视、后视和俯视投影：可见舵机输出轴、壳体、安装孔与底部 8 针排针 |

## 系统结构

### Hat Servo

电气功能图显示 SERVO 与 StickC 之间仅有三条连接：G 到 GND、V 到 5V、S 到 G26。

- 参数与网络：`ground_path=SERVO G to StickC GND`；`power_path=SERVO V to StickC 5V`；`control_path=SERVO S to StickC G26`
- 证据：图 ccf74e453732 / 第 1 页 / 整页三线框图：三条水平线分别对齐 SERVO G/V/S 与 StickC GND/5V/G26

## 电源

### 舵机供电

StickC 的 5V 连接 SERVO 的 V，StickC GND 连接 SERVO 的 G；页面未显示稳压器、负载开关、滤波电容或保护器件。

- 参数与网络：`supply=StickC 5V to SERVO V`；`return=StickC GND to SERVO G`；`regulator=not shown`；`load_switch=not shown`；`decoupling=not shown`；`protection=not shown`
- 证据：图 ccf74e453732 / 第 1 页 / 页面上中与中部 G-GND、V-5V 两条连线；整页无其他电源器件

## 接口

### SERVO 三线接口

SERVO 侧 G、V、S 三个功能端分别映射为 GND、5V、G26。

- 参数与网络：`G=GND`；`V=5V`；`S=G26`；`connector_reference=not shown`；`physical_pin_numbers=not shown`
- 证据：图 ccf74e453732 / 第 1 页 / 页面左右两侧端子标签和中间三条一一对应的水平连线

## GPIO 与控制信号

### 舵机控制信号

StickC 的 G26 直接连接 SERVO 的 S 功能端。

- 参数与网络：`host_gpio=G26`；`servo_terminal=S`；`direction=from StickC to SERVO`；`waveform=not shown`
- 证据：图 ccf74e453732 / 第 1 页 / 页面下中 SERVO S 与 StickC G26 之间的水平连线

## 其他事实

### Hat Servo 外形尺寸

机械图以 mm 为单位，主体正视投影标注 34.94 和 29.9 两个纵向尺寸；上方侧视投影标注 21.3、18.3、13.7 三个高度尺寸。

- 参数与网络：`unit=mm`；`overall_body_dimension=34.94`；`inner_body_dimension=29.9`；`side_heights=21.3, 18.3, 13.7`
- 证据：图 646dfe4b5549 / 第 1 页 / 机械尺寸页左上侧视图的 21.3/18.3/13.7 与中央正视图左侧的 34.94/29.9 标注；右下角 UNIT:mm

### 输出轴与安装孔尺寸

机械图标注输出轴/舵机上部局部宽度 10.7 mm；后视投影的孔位水平间距为 15.9 mm、垂直间距为 12.7 mm。

- 参数与网络：`unit=mm`；`upper_feature_width=10.7`；`hole_horizontal_spacing=15.9`；`hole_vertical_spacing=12.7`
- 证据：图 646dfe4b5549 / 第 1 页 / 机械尺寸页中央上方 10.7 标注与右侧后视图 15.9 水平、12.7 垂直孔距标注

### 本地资源详细程度

第一张资源是三线功能映射图，第二张是机械尺寸图；两页均未提供器件位号、连接器针脚编号、舵机内部驱动、电源调节、保护、时钟、复位、存储或调试电路。

- 参数与网络：`electrical_asset=three-wire functional mapping`；`mechanical_asset=dimension drawing`；`reference_designators=not shown`；`internal_driver=not shown`；`clock_reset_debug=not shown`；`storage=not shown`
- 证据：图 ccf74e453732 / 第 1 页 / 整页仅包含 SERVO/StickC 方框与 G/V/S-GND/5V/G26 三线; 图 646dfe4b5549 / 第 1 页 / 整页仅包含机械投影、轮廓、孔位和 mm 尺寸标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Servo | `ground_path=SERVO G to StickC GND`；`power_path=SERVO V to StickC 5V`；`control_path=SERVO S to StickC G26` |
| 接口 | SERVO 三线接口 | `G=GND`；`V=5V`；`S=G26`；`connector_reference=not shown`；`physical_pin_numbers=not shown` |
| 电源 | 舵机供电 | `supply=StickC 5V to SERVO V`；`return=StickC GND to SERVO G`；`regulator=not shown`；`load_switch=not shown`；`decoupling=not shown`；`protection=not shown` |
| GPIO 与控制信号 | 舵机控制信号 | `host_gpio=G26`；`servo_terminal=S`；`direction=from StickC to SERVO`；`waveform=not shown` |
| 核心器件 | 舵机型号 | `documented_model=ES9251II`；`schematic_model=not shown`；`reference_designator=not shown` |
| GPIO 与控制信号 | G26 控制波形 | `documented_protocol=PWM`；`signal_path=G26 to S`；`frequency=not shown`；`period=not shown`；`pulse_width=not shown` |
| 其他事实 | 舵机运动角度 | `documented_travel=145°±10°`；`schematic_travel=not shown`；`mechanical_stop=not shown` |
| 其他事实 | Hat Servo 外形尺寸 | `unit=mm`；`overall_body_dimension=34.94`；`inner_body_dimension=29.9`；`side_heights=21.3, 18.3, 13.7` |
| 其他事实 | 输出轴与安装孔尺寸 | `unit=mm`；`upper_feature_width=10.7`；`hole_horizontal_spacing=15.9`；`hole_vertical_spacing=12.7` |
| 其他事实 | 本地资源详细程度 | `electrical_asset=three-wire functional mapping`；`mechanical_asset=dimension drawing`；`reference_designators=not shown`；`internal_driver=not shown`；`clock_reset_debug=not shown`；`storage=not shown` |

## 待确认事项

- `component.servo-model-es9251ii`：产品正文给出舵机型号 ES9251II，但两张本地资源均未出现 ES9251II 型号标注或器件铭牌，无法由原理图资源确认。（证据：图 ccf74e453732 / 第 1 页 / 电气页左侧仅标注 SERVO，无型号; 图 646dfe4b5549 / 第 1 页 / 机械尺寸页仅有轮廓与尺寸，无 ES9251II 文字或铭牌）
- `gpio.pwm-control-claim`：产品正文声明 G26 以 PWM 控制舵机角度，但电气页只显示 G26 到 S 的连接，未标注 PWM、频率、周期或脉宽范围。（证据：图 ccf74e453732 / 第 1 页 / 页面下方 G26-S 连线，仅标注端点名称，无 PWM 参数）
- `other.servo-travel-claim`：产品正文声明运动角度为 145°±10°，但两张本地资源没有角度范围或机械止挡标注，无法由这些页面确认。（证据：图 ccf74e453732 / 第 1 页 / 电气映射页无角度参数; 图 646dfe4b5549 / 第 1 页 / 机械尺寸页显示输出轴轮廓但无角度或旋转行程标注）
- `review.servo-model-es9251ii`：Hat Servo 实际装配的舵机型号是否为 ES9251II？；原因：产品正文给出该型号，但电气映射图与机械尺寸图均未显示型号或铭牌。
- `review.pwm-parameters`：G26 控制信号要求的 PWM 频率、周期和有效脉宽范围是什么？；原因：页面只确认 G26 到 S 的连接，没有 PWM 电气或时序参数。
- `review.servo-travel`：145°±10° 是机械极限、可控行程还是批次容差？；原因：两张本地资源均没有旋转角度、机械止挡或控制脉宽与角度关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ccf74e45373208e900f3db87d3abc917803531082ca0bca8145927480c3f5237` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-servo/hat-servo_sch_01.webp` |
| 2 | 1 | `646dfe4b554942ed96b1d1fbfcb41dd281ce226bee3a5caf9be294370490d842` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/870/hatservo_page_01.webp` |

---

源文档：`zh_CN/hat/hat-servo.md`

源文档 SHA-256：`ea2aa431c05bcf110e3bd0e95ca787ddf17cc7e5fdf54bd185ec830866b239f9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
