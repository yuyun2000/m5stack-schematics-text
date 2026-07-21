# Atom Fly 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Fly |
| SKU | K040 |
| 产品 ID | `atom-fly-1336978a00b2` |
| 源文档 | `zh_CN/atom/atomfly.md` |

## 概述

Atom Fly 通过 J1 Atom_PIN 连接 Atom 主控，G21/G25 组成带 4.7kΩ 上拉的 I2C 总线，并同时连接 MPU6886、BMP280 和 VL53L0X。G22/G19/G23/G33 分别输出 PWM1-PWM4，经四颗 AO3400A 低边 MOSFET 控制 B1-B4 电机，每路配置续流二极管、抑制电容、栅极串联电阻和下拉。外部电池经 F1 形成 +BAT，SX1308 将 +BAT 升压为 5V 供 Atom，传感器和控制信号使用 Atom 提供的 3.3V。

## 检索关键词

`Atom Fly`、`K040`、`MPU6886`、`BMP280`、`VL53L0X`、`SX1308`、`AO3400A`、`I2C`、`SCL`、`SDA`、`G21`、`G25`、`G22`、`G19`、`G23`、`G33`、`PWM1`、`PWM2`、`PWM3`、`PWM4`、`B1`、`B2`、`B3`、`B4`、`+BAT`、`+5V`、`+3.3V`、`1N4007WS`、`B5819WS`、`SS54`、`XSHUT`、`GPIO1`、`SDO/A0`、`200mAh`、`25C`、`31000RPM`、`quadrotor`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MPU6886 | 连接 SCL/SDA 的惯性传感器，使用 3.3V VDD/VDDIO，并保留 INT 与 SDO/A0 配置 | 图 12457ddd08cc / 第 1 页 / 第 1 页左中 U1 MPU6886，SCL/SDA/INT/VDDIO/SENB/SDO-A0/VDD/GND |
| U2 | BMP280 | 连接 SCL/SDA 的气压传感器，VDD/VDDIO/CSB 使用 3.3V | 图 12457ddd08cc / 第 1 页 / 第 1 页左上 U2 BMP280，SCK/SDI/SDO/CSB/VDD/VDDIO/GND |
| U3 | VL53L0X | 连接 SCL/SDA 的 ToF 传感器，带 XSHUT/GPIO1 上拉和 AVDD/AVSS 去耦 | 图 12457ddd08cc / 第 1 页 / 第 1 页中上 U3 VL53L0X，XSHUT/GPIO1/SDA/SCL/AVDD/AVSS/GND/DNC |
| U4 | SX1308 | 将 +BAT 经 L1/D7 升压为 +5V 的开关转换器 | 图 12457ddd08cc / 第 1 页 / 第 1 页左下 U4 SX1308、L1 4.7uH、D7 B5819WS、R12/R15/R16 与 +BAT/+5V |
| Q1-Q4 | AO3400A | PWM1-PWM4 驱动的四路电机低边 MOSFET | 图 12457ddd08cc / 第 1 页 / 第 1 页右上/右中 Q1-Q4 AO3400A，分别连接 PWM1-PWM4、B1-B4 和 GND |
| B1-B4 | Motor | 四路从 +BAT 到 Q1-Q4 低边开关的直流电机负载 | 图 12457ddd08cc / 第 1 页 / 第 1 页右侧 B1-B4 Motor，正端 +BAT、负端至 Q1-Q4 |
| D1-D4 | 1N4007WS | 分别跨接 B1-B4 的电机续流二极管 | 图 12457ddd08cc / 第 1 页 / 第 1 页右侧 D1-D4 1N4007WS，跨接各电机 +BAT 与开关节点 |
| P1 | Header 2 | 外部电池输入连接器，正端经 F1 到 +BAT，负端接 GND | 图 12457ddd08cc / 第 1 页 / 第 1 页中部 P1 Header 2、F1 Fuse、+BAT 和 GND |
| J1 | Atom_PIN | Atom 主控的 SCL/SDA/5V/GND/3V3 和 PWM1-PWM4 接口 | 图 12457ddd08cc / 第 1 页 / 第 1 页下中 J1 Atom_PIN，G21/G25/5V/GND/3V3/G22/G19/G23/G33 |
| F1,D5 | Fuse / SS54 | 电池输入的串联保险和 +BAT 对地保护二极管 | 图 12457ddd08cc / 第 1 页 / 第 1 页中部 P1 正端经 F1 到 +BAT，D5 SS54 从 +BAT 接 GND |
| D6 | LED | 由 +5V 经 R11 1kΩ 驱动的电源指示灯 | 图 12457ddd08cc / 第 1 页 / 第 1 页右下 +5V/R11 1K/D6 LED/GND |

## 系统结构

### Atom Fly 电气架构

Atom 通过四路 PWM 直接控制四颗电机 MOSFET，并通过共享 I2C 总线连接 MPU6886、BMP280 和 VL53L0X；外部电池形成 +BAT，SX1308 生成 Atom 5V，Atom 再提供 3.3V 传感器电源。

- 参数与网络：`host=J1 Atom_PIN`；`motor_channels=4`；`motor_switches=Q1-Q4 AO3400A`；`sensors=MPU6886, BMP280, VL53L0X`；`sensor_bus=I2C SCL/SDA`；`battery_rail=+BAT`；`five_volt_converter=U4 SX1308`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页完整单页原理图，传感器、电池/升压、Atom 与四路电机区

## 核心器件

### 四路 AO3400A 低边电机驱动

B1-B4 正端连接 +BAT，负端分别连接 Q1-Q4 AO3400A 漏极，Q1-Q4 源极接 GND；PWM 栅极信号控制各电机回路导通。

- 参数与网络：`channel_1=+BAT -> B1 -> Q1 -> GND`；`channel_2=+BAT -> B2 -> Q2 -> GND`；`channel_3=+BAT -> B3 -> Q3 -> GND`；`channel_4=+BAT -> B4 -> Q4 -> GND`；`mosfet=AO3400A`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页右上/右中 B1-B4 与 Q1-Q4 AO3400A

## 电源

### 外部电池到 +BAT

P1 pin2 正端经 F1 Fuse 连接 +BAT，pin1 接 GND；D5 SS54 和 C10 100nF 从 +BAT 接 GND，+BAT 直接供四路电机并作为 SX1308 输入。

- 参数与网络：`connector=P1 Header 2`；`positive_path=pin2 -> F1 -> +BAT`；`negative=pin1 GND`；`shunt_diode=D5 SS54`；`capacitor=C10 100nF`；`loads=B1-B4 motors and U4 SX1308`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页中部 P1/F1/D5/C10/+BAT 与右侧 B1-B4、左下 U4

### +BAT 到 +5V 升压

U4 SX1308 以 +BAT 为输入，L1 4.7uH 连接 IN/SW，SW 经 D7 B5819WS 到 +5V；R15 73.2kΩ/R16 10kΩ 构成反馈分压，R12 100kΩ 将 EN 拉到 +BAT。

- 参数与网络：`converter=U4 SX1308`；`input=+BAT`；`output=+5V`；`inductor=L1 4.7uH`；`rectifier=D7 B5819WS`；`feedback=R15 73.2K, R16 10K`；`enable_pull=R12 100K to +BAT`；`capacitors=C13/C14 22uF, C16 100nF`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页左下 U4/L1/D7/R12/R15/R16/C13/C14/C16 与 +BAT/+5V

### 5V、3.3V 和 +BAT 分配

+5V 连接 J1 Atom 5V、D6 电源指示和 C11/C15；3.3V 从 J1 Atom 3V3 供三颗传感器及 I2C/XSHUT/GPIO1 上拉；+BAT 直接连接四路电机正端。

- 参数与网络：`+5V=J1 pin3, D6/R11, C11/C15`；`+3.3V=U1/U2/U3 sensor supplies and pullups`；`+BAT=B1-B4 motor positive terminals`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页 J1、三颗传感器、D6 和 B1-B4 的同名电源网络

## 总线

### 共享传感器 I2C 总线

J1 pin1 G21 连接 SCL，pin2 G25 连接 SDA；R13/R14 各 4.7kΩ 将 SCL/SDA 上拉到 3.3V，U1 MPU6886、U2 BMP280 和 U3 VL53L0X 并联在该总线。

- 参数与网络：`host_scl=J1 pin1 G21`；`host_sda=J1 pin2 G25`；`pullups=R13/R14 4.7K to 3.3V`；`devices=U1 MPU6886, U2 BMP280, U3 VL53L0X`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页 J1 G21/G25、R13/R14 与 U1/U2/U3 SCL/SDA

## GPIO 与控制信号

### Atom 四路电机 PWM 映射

J1 G22/G19/G23/G33 分别连接 PWM1/PWM2/PWM3/PWM4，并经 R3/R4/R7/R8 各 10Ω 到 Q1/Q2/Q3/Q4 栅极；R5/R6/R9/R10 各 51kΩ 将栅极下拉到 GND。

- 参数与网络：`G22=PWM1 -> R3 -> Q1`；`G19=PWM2 -> R4 -> Q2`；`G23=PWM3 -> R7 -> Q3`；`G33=PWM4 -> R8 -> Q4`；`gate_series=10R each`；`gate_pulldowns=51K each`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页下中 J1 PWM1-PWM4 与右侧 Q1-Q4/R3-R10

### 5V 电源指示灯

+5V 经 R11 1kΩ 和 D6 LED 串联到 GND，形成 5V 电源指示。

- 参数与网络：`supply=+5V`；`resistor=R11 1K`；`indicator=D6`；`return=GND`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页右下 +5V/R11/D6/GND

## 保护电路

### 四路电机反灌与噪声抑制

D1-D4 1N4007WS 分别反向跨接 B1-B4，C1/C2/C6/C7 各 100nF 分别跨接对应电机端子。

- 参数与网络：`flyback_diodes=D1-D4 1N4007WS`；`motor_capacitors=C1/C2/C6/C7 100nF`；`channels=B1, B2, B3, B4`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页右侧各电机旁 D1-D4 与 C1/C2/C6/C7

## 传感器

### MPU6886 惯性传感器连接

U1 MPU6886 的 SCL pin23、SDA pin24 接共享总线，VDDIO pin8、SENB pin22、VDD pin13 接 3.3V，GND pin18 接地，C8/C9 各 100nF 去耦；INT pin12 未连接。

- 参数与网络：`part=MPU6886`；`scl=pin23 SCL`；`sda=pin24 SDA`；`power=VDDIO/SENB/VDD 3.3V`；`ground=pin18 GND`；`decoupling=C8/C9 100nF`；`interrupt=pin12 INT NC`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页左中 U1 MPU6886 与 C8/C9

### BMP280 气压传感器连接

U2 BMP280 的 SCK pin4 接 SCL、SDI pin3 接 SDA，VDD pin8/VDDIO pin6/CSB pin2 接 3.3V，GND pin1/pin7 接地，C3 100nF 去耦。

- 参数与网络：`part=BMP280`；`scl=pin4 SCK/SCL`；`sda=pin3 SDI/SDA`；`power=VDD/VDDIO/CSB 3.3V`；`ground=pin1/pin7 GND`；`decoupling=C3 100nF`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页左上 U2 BMP280 与 C3

### VL53L0X ToF 传感器连接

U3 VL53L0X 的 SDA pin9/SCL pin10 接共享总线，AVDD pin11/pin1 接 3.3V，AVSS/GND 引脚接地；XSHUT pin5 和 GPIO1 pin7 各由 4.7kΩ 上拉到 3.3V，DNC pin8 未连接。

- 参数与网络：`part=VL53L0X`；`sda=pin9 SDA`；`scl=pin10 SCL`；`power=pin11/pin1 AVDD 3.3V`；`control_pullups=XSHUT/GPIO1 4.7K to 3.3V`；`decoupling=C4/C5 100nF`；`dnc=pin8 NC`
- 证据：图 12457ddd08cc / 第 1 页 / 第 1 页中上 U3 VL53L0X、R1/R2 与 C4/C5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom Fly 电气架构 | `host=J1 Atom_PIN`；`motor_channels=4`；`motor_switches=Q1-Q4 AO3400A`；`sensors=MPU6886, BMP280, VL53L0X`；`sensor_bus=I2C SCL/SDA`；`battery_rail=+BAT`；`five_volt_converter=U4 SX1308` |
| 电源 | 外部电池到 +BAT | `connector=P1 Header 2`；`positive_path=pin2 -> F1 -> +BAT`；`negative=pin1 GND`；`shunt_diode=D5 SS54`；`capacitor=C10 100nF`；`loads=B1-B4 motors and U4 SX1308` |
| 电源 | +BAT 到 +5V 升压 | `converter=U4 SX1308`；`input=+BAT`；`output=+5V`；`inductor=L1 4.7uH`；`rectifier=D7 B5819WS`；`feedback=R15 73.2K, R16 10K`；`enable_pull=R12 100K to +BAT`；`capacitors=C13/C14 22uF, C16 100nF` |
| 电源 | 5V、3.3V 和 +BAT 分配 | `+5V=J1 pin3, D6/R11, C11/C15`；`+3.3V=U1/U2/U3 sensor supplies and pullups`；`+BAT=B1-B4 motor positive terminals` |
| 总线 | 共享传感器 I2C 总线 | `host_scl=J1 pin1 G21`；`host_sda=J1 pin2 G25`；`pullups=R13/R14 4.7K to 3.3V`；`devices=U1 MPU6886, U2 BMP280, U3 VL53L0X` |
| 传感器 | MPU6886 惯性传感器连接 | `part=MPU6886`；`scl=pin23 SCL`；`sda=pin24 SDA`；`power=VDDIO/SENB/VDD 3.3V`；`ground=pin18 GND`；`decoupling=C8/C9 100nF`；`interrupt=pin12 INT NC` |
| 传感器 | BMP280 气压传感器连接 | `part=BMP280`；`scl=pin4 SCK/SCL`；`sda=pin3 SDI/SDA`；`power=VDD/VDDIO/CSB 3.3V`；`ground=pin1/pin7 GND`；`decoupling=C3 100nF` |
| 传感器 | VL53L0X ToF 传感器连接 | `part=VL53L0X`；`sda=pin9 SDA`；`scl=pin10 SCL`；`power=pin11/pin1 AVDD 3.3V`；`control_pullups=XSHUT/GPIO1 4.7K to 3.3V`；`decoupling=C4/C5 100nF`；`dnc=pin8 NC` |
| GPIO 与控制信号 | Atom 四路电机 PWM 映射 | `G22=PWM1 -> R3 -> Q1`；`G19=PWM2 -> R4 -> Q2`；`G23=PWM3 -> R7 -> Q3`；`G33=PWM4 -> R8 -> Q4`；`gate_series=10R each`；`gate_pulldowns=51K each` |
| 核心器件 | 四路 AO3400A 低边电机驱动 | `channel_1=+BAT -> B1 -> Q1 -> GND`；`channel_2=+BAT -> B2 -> Q2 -> GND`；`channel_3=+BAT -> B3 -> Q3 -> GND`；`channel_4=+BAT -> B4 -> Q4 -> GND`；`mosfet=AO3400A` |
| 保护电路 | 四路电机反灌与噪声抑制 | `flyback_diodes=D1-D4 1N4007WS`；`motor_capacitors=C1/C2/C6/C7 100nF`；`channels=B1, B2, B3, B4` |
| GPIO 与控制信号 | 5V 电源指示灯 | `supply=+5V`；`resistor=R11 1K`；`indicator=D6`；`return=GND` |
| 电源 | 产品正文中的电池规格 | `documented_capacity=200mAh`；`documented_series=1S`；`documented_rate=25C`；`documented_connector=JST`；`schematic_connector=P1 Header 2` |
| 核心器件 | 产品正文中的电机与螺旋桨规格 | `documented_speed=31000 +/-10% RPM`；`documented_propeller=2 inch`；`schematic_motors=B1-B4 Motor` |

## 待确认事项

- `power.documented-battery-pack`：产品正文给出 200mAh/1S/25C/JST 电池，但原理图只显示 P1 Header 2、Fuse、+BAT 和 GND，未标注容量、倍率、电芯串数或 JST 型号。（证据：图 12457ddd08cc / 第 1 页 / 第 1 页中部 P1 Header 2/F1/+BAT/GND，图中无电池规格）
- `component.documented-motor-performance`：产品正文给出电机负载转速 31000±10% RPM 和 2 英寸螺旋桨，但原理图只将 B1-B4 标为 Motor，未给出电机型号、转速、旋向或螺旋桨参数。（证据：图 12457ddd08cc / 第 1 页 / 第 1 页右侧 B1-B4 仅标 Motor）
- `review.battery-pack`：K040 配套电池是否固定为 200mAh/1S/25C/JST，JST 的具体系列和极性是什么？；原因：原理图只给出二针电池接口和 +BAT/GND，容量、倍率、串数和连接器型号需 BOM 或实物确认。
- `review.motor-performance`：B1-B4 的准确料号、CW/CCW 分配、31000RPM 测试条件和 2 英寸螺旋桨型号是什么？；原因：这些动力系统参数未在原理图标注，需要电机/螺旋桨 BOM 和实测条件确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `12457ddd08cce6c3534b1dc31d05b5861dcc3b53945dd6bc13171f8dd2168f8a` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_sch_01.webp` |

---

源文档：`zh_CN/atom/atomfly.md`

源文档 SHA-256：`f0a269e2c24cd9f7f1ee7452ad4caf98db0454acb5a1ca13c83c4b98379e65bc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
