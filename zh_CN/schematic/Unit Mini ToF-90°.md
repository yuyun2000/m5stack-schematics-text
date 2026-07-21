# Unit Mini ToF-90° 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini ToF-90° |
| SKU | U196 |
| 产品 ID | `unit-mini-tof-90-aa3bfaada847` |
| 源文档 | `zh_CN/unit/Unit Mini ToF-90.md` |

## 概述

Unit Mini ToF-90° 由标为 Unit-ToF-90_1F 与 Unit-ToF-90_2F 的两块电路构成：1F 通过 J1 Grove 接收 I2C 与 5V，由 U1 ME6206A33XG 生成 3V3，并提供 I2C 上拉和红色电源灯。P1/P2 四针板间接口按 SCL、SDA、3.3V、GND 对应连接，2F 上的 U2 VL53L0CXV0DH/1 直接作为 I2C ToF 传感器，XSHUT/GPIO1 上拉并配置本地去耦。原理图未印 I2C 地址、光学性能、90°物理安装细节或功耗数据，且正文 VL53L0X 名称与图纸完整标识的对应关系需要 BOM/器件资料确认。

## 检索关键词

`Unit Mini ToF-90°`、`Unit Mini ToF-90`、`U196`、`Unit-ToF-90_1F`、`Unit-ToF-90_2F`、`VL53L0CXV0DH/1`、`VL53L0X`、`ME6206A33XG`、`Grove`、`HY2.0-4P`、`I2C`、`I2C_SCL`、`I2C_SDA`、`TOF_SCL`、`TOF_SDA`、`VCC_5V`、`3V3`、`TOF_3V3`、`TOF_GND`、`XSHUT`、`GPIO1`、`0x29`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 10KΩ`、`R4 10KΩ`、`P1 Header 4`、`P2 Header 4`、`D1 RED LED`、`R7 1KΩ`、`940nm VCSEL`、`25° FoV`、`3-200cm`、`ToF`、`Class 1 laser`、`90° installation`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | VL53L0CXV0DH/1 | 2F 板上的 ToF 传感器，连接 I2C、XSHUT、GPIO1、双 AVDD 与多脚接地 | 图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，U2 VL53L0CXV0DH/1 pins1-12 |
| U1 | ME6206A33XG | 1F 板上将 VCC_5V 稳压为 3V3 的三脚 LDO | 图 82039681f5a5 / 第 1 页 / 第1页网格 A2-A3，U1 ME6206A33XG、VIN/VOUT/GND |
| J1 | GROVE | 1F 外部 I2C 与 5V/GND 接口，四脚标 IO2、IO1、5V、GND | 图 82039681f5a5 / 第 1 页 / 第1页网格 A2，J1 GROVE 与 I2C_SCL/I2C_SDA/VCC_5V/GND |
| P1 | Header 4 | 1F 板间接口，引出 I2C_SCL、I2C_SDA、3V3、GND | 图 82039681f5a5 / 第 1 页 / 第1页网格 B2，P1 Header 4 pins1-4 |
| P2 | Header 4 | 2F 板间接口，引出 TOF_SCL、TOF_SDA、TOF_3V3、TOF_GND | 图 82039681f5a5 / 第 1 页 / 第1页网格 C2，P2 Header 4 pins1-4 |
| R1/R2 | 4.7KΩ / 4.7KΩ | 1F 板上 I2C_SCL/I2C_SDA 到 3V3 的上拉电阻 | 图 82039681f5a5 / 第 1 页 / 第1页网格 A2，R1/R2 4.7KΩ、3V3、I2C_SCL/I2C_SDA |
| R3/R4 | 10KΩ / 10KΩ | 2F 板上 U2 GPIO1 与 XSHUT 到 TOF_3V3 的上拉电阻 | 图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，R3/R4 10KΩ、TOF_3V3、U2 pins7/5 |
| D1/R7 | RED LED / 1KΩ | 1F 板上从 3V3 经 1KΩ 到 GND 的红色电源指示支路 | 图 82039681f5a5 / 第 1 页 / 第1页网格 B3，3V3/R7 1KΩ/D1 RED LED/GND |
| C1/C2/C3 | 10uF / 100nF / 10uF | U1 输入与输出的去耦/储能电容 | 图 82039681f5a5 / 第 1 页 / 第1页网格 A2-A3，U1 周围 C1/C2/C3 |
| C4/C5/C8 | 10uF / 100nF / NC | 2F 板上 TOF_3V3 的本地去耦与 P2 处预留未装电容 | 图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，C4 10uF/C5 100nF/C8 NC 与 TOF_3V3/TOF_GND |

## 系统结构

### 1F/2F 双板架构

原理图用虚线框分为 Unit-ToF-90_1F 和 Unit-ToF-90_2F：1F 包含 Grove、LDO、I2C 上拉、P1 与电源灯，2F 包含 P2、U2 ToF 传感器及其上拉/去耦。

- 参数与网络：`first_board=Unit-ToF-90_1F`；`first_board_blocks=J1,U1,R1/R2,P1,D1`；`second_board=Unit-ToF-90_2F`；`second_board_blocks=P2,U2,R3/R4,C4/C5/C8`；`controller=not shown`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页上下两个虚线框 Unit-ToF-90_1F/2F

### 未显示的控制与存储分区

该页未显示 MCU、协处理器、外部存储器、晶振、复位按键、调试接口、音频、射频或电池/充电电路；U2 由外部 I2C 主机直接访问。

- 参数与网络：`mcu=not shown`；`coprocessor=not shown`；`storage=not shown`；`clock=not shown`；`debug=not shown`；`audio=not shown`；`rf=not shown`；`battery=not shown`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页完整单页器件与功能分区

## 核心器件

### U2 ToF 传感器标识

2F 板 U2 的原理图型号明确标为 VL53L0CXV0DH/1，符号具有 12 脚。

- 参数与网络：`reference=U2`；`schematic_part_number=VL53L0CXV0DH/1`；`pins=12`；`interface=I2C`；`control=XSHUT; GPIO1`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C3，U2 型号和 pins1-12

## 电源

### VCC_5V 到 3V3

U1 ME6206A33XG VIN pin3 接 VCC_5V，VOUT pin2 输出 3V3，GND pin1 接地；输入 C1 10uF，输出 C2 100nF/C3 10uF。

- 参数与网络：`regulator=U1 ME6206A33XG`；`input=pin3 VIN / VCC_5V`；`output=pin2 VOUT / 3V3`；`ground=pin1 GND`；`input_cap=C1 10uF`；`output_caps=C2 100nF; C3 10uF`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 A2-A3，U1/C1/C2/C3/VCC_5V/3V3

### U2 TOF_3V3 供电

P2 pin3 的 TOF_3V3 连接 U2 AVDD pins1/11；C4 10uF 与 C5 100nF 从 TOF_3V3 对地，C8 为 P2 附近未装的对地电容位。

- 参数与网络：`source=P2 pin3 TOF_3V3`；`load=U2 AVDD pins1,11`；`decoupling=C4 10uF; C5 100nF`；`optional_cap=C8 NC`；`return=TOF_GND`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，P2 pin3/U2 AVDD/C4/C5/C8

### 3V3 红色指示灯

1F 板 3V3 经 R7 1KΩ 串联 D1 RED LED 到 GND，电路中没有 GPIO 开关或负载开关。

- 参数与网络：`rail=3V3`；`resistor=R7 1KΩ`；`led=D1 RED LED`；`return=GND`；`control=always connected`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 B3，3V3/R7/D1/GND

## 接口

### J1 Grove 针脚

J1 pin IO2 接 I2C_SCL，pin IO1 接 I2C_SDA，pin 5V 接 VCC_5V，pin GND 接 GND。

- 参数与网络：`connector=J1 GROVE`；`io2=I2C_SCL`；`io1=I2C_SDA`；`power=5V / VCC_5V`；`ground=GND`；`direction=SCL host output; SDA bidirectional`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 A2，J1 IO2/IO1/5V/GND 与网络名

### P1/P2 板间信号对应

P1 pins1-4 依次为 I2C_SCL、I2C_SDA、3V3、GND；P2 pins1-4 依次为 TOF_SCL、TOF_SDA、TOF_3V3、TOF_GND，形成同脚序的四线板间接口。

- 参数与网络：`P1_pin1=I2C_SCL`；`P1_pin2=I2C_SDA`；`P1_pin3=3V3`；`P1_pin4=GND`；`P2_pin1=TOF_SCL`；`P2_pin2=TOF_SDA`；`P2_pin3=TOF_3V3`；`P2_pin4=TOF_GND`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 B2 的 P1 与 C2 的 P2 pins1-4

## 总线

### 1F I2C 总线

J1 的 I2C_SCL/I2C_SDA 直接连到 P1 pins1/2，并分别由 R1/R2 4.7KΩ 上拉到 3V3。

- 参数与网络：`scl=J1 IO2/I2C_SCL -> P1 pin1`；`sda=J1 IO1/I2C_SDA -> P1 pin2`；`scl_pullup=R1 4.7KΩ to 3V3`；`sda_pullup=R2 4.7KΩ to 3V3`；`logic_voltage=3V3`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 A2-B2，J1/R1/R2/P1 与 I2C_SCL/I2C_SDA

### U2 I2C 连接

P2 pin1 TOF_SCL 连接 U2 SCL pin10，P2 pin2 TOF_SDA 连接 U2 SDA pin9；2F 注记说明 I2C pull-up resistors on 1F board。

- 参数与网络：`controller=external host through J1/P1/P2`；`device=U2 VL53L0CXV0DH/1`；`scl=P2 pin1 TOF_SCL -> U2 pin10`；`sda=P2 pin2 TOF_SDA -> U2 pin9`；`pullup_location=1F board R1/R2`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，P2/TOF_SCL/TOF_SDA/U2 pins9/10 与 pull-up 注记

## GPIO 与控制信号

### U2 XSHUT 与 GPIO1

U2 XSHUT pin5 与 GPIO1 pin7 分别通过 R4/R3 10KΩ 上拉到 TOF_3V3，页面没有把两信号引到 P2。

- 参数与网络：`xshut=U2 pin5 -> R4 10KΩ -> TOF_3V3`；`gpio1=U2 pin7 -> R3 10KΩ -> TOF_3V3`；`external_breakout=not shown`；`default_level=high`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，R3/R4、U2 XSHUT pin5/GPIO1 pin7

## 保护电路

### 外部接口保护

J1 的 VCC_5V、I2C_SCL 与 I2C_SDA 路径未显示保险丝、串联限流或专用 ESD/TVS 器件。

- 参数与网络：`power_fuse=not shown`；`i2c_series=not shown`；`esd=not shown`；`tvs=not shown`；`connector=J1 GROVE`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 A2-B2，J1 到 U1/P1 的全部接口线路

## 关键网络

### U2 接地与 DNC

U2 VSS pin2、GND pin3、GND2 pin4、GND3 pin6、GND4 pin12 接 TOF_GND，DNC pin8 标叉未连接。

- 参数与网络：`grounds=pins2,3,4,6,12 -> TOF_GND`；`dnc=pin8 not connected`；`ground_source=P2 pin4 TOF_GND`
- 证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C3，U2 right-side VSS/GND/GND2/GND3/GND4/DNC pins

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 1F/2F 双板架构 | `first_board=Unit-ToF-90_1F`；`first_board_blocks=J1,U1,R1/R2,P1,D1`；`second_board=Unit-ToF-90_2F`；`second_board_blocks=P2,U2,R3/R4,C4/C5/C8`；`controller=not shown` |
| 核心器件 | U2 ToF 传感器标识 | `reference=U2`；`schematic_part_number=VL53L0CXV0DH/1`；`pins=12`；`interface=I2C`；`control=XSHUT; GPIO1` |
| 接口 | J1 Grove 针脚 | `connector=J1 GROVE`；`io2=I2C_SCL`；`io1=I2C_SDA`；`power=5V / VCC_5V`；`ground=GND`；`direction=SCL host output; SDA bidirectional` |
| 电源 | VCC_5V 到 3V3 | `regulator=U1 ME6206A33XG`；`input=pin3 VIN / VCC_5V`；`output=pin2 VOUT / 3V3`；`ground=pin1 GND`；`input_cap=C1 10uF`；`output_caps=C2 100nF; C3 10uF` |
| 总线 | 1F I2C 总线 | `scl=J1 IO2/I2C_SCL -> P1 pin1`；`sda=J1 IO1/I2C_SDA -> P1 pin2`；`scl_pullup=R1 4.7KΩ to 3V3`；`sda_pullup=R2 4.7KΩ to 3V3`；`logic_voltage=3V3` |
| 接口 | P1/P2 板间信号对应 | `P1_pin1=I2C_SCL`；`P1_pin2=I2C_SDA`；`P1_pin3=3V3`；`P1_pin4=GND`；`P2_pin1=TOF_SCL`；`P2_pin2=TOF_SDA`；`P2_pin3=TOF_3V3`；`P2_pin4=TOF_GND` |
| 总线 | U2 I2C 连接 | `controller=external host through J1/P1/P2`；`device=U2 VL53L0CXV0DH/1`；`scl=P2 pin1 TOF_SCL -> U2 pin10`；`sda=P2 pin2 TOF_SDA -> U2 pin9`；`pullup_location=1F board R1/R2` |
| 电源 | U2 TOF_3V3 供电 | `source=P2 pin3 TOF_3V3`；`load=U2 AVDD pins1,11`；`decoupling=C4 10uF; C5 100nF`；`optional_cap=C8 NC`；`return=TOF_GND` |
| GPIO 与控制信号 | U2 XSHUT 与 GPIO1 | `xshut=U2 pin5 -> R4 10KΩ -> TOF_3V3`；`gpio1=U2 pin7 -> R3 10KΩ -> TOF_3V3`；`external_breakout=not shown`；`default_level=high` |
| 关键网络 | U2 接地与 DNC | `grounds=pins2,3,4,6,12 -> TOF_GND`；`dnc=pin8 not connected`；`ground_source=P2 pin4 TOF_GND` |
| 电源 | 3V3 红色指示灯 | `rail=3V3`；`resistor=R7 1KΩ`；`led=D1 RED LED`；`return=GND`；`control=always connected` |
| 保护电路 | 外部接口保护 | `power_fuse=not shown`；`i2c_series=not shown`；`esd=not shown`；`tvs=not shown`；`connector=J1 GROVE` |
| 系统结构 | 未显示的控制与存储分区 | `mcu=not shown`；`coprocessor=not shown`；`storage=not shown`；`clock=not shown`；`debug=not shown`；`audio=not shown`；`rf=not shown`；`battery=not shown` |
| 核心器件 | VL53L0X 与 VL53L0CXV0DH/1 名称对应 | `document_name=VL53L0X`；`schematic_marking=VL53L0CXV0DH/1`；`bom=not available on page`；`equivalence=not confirmed by schematic alone` |
| 总线地址 | U2 I2C 地址 | `document_address=0x29`；`address_width=7-bit stated by context`；`schematic_address=not shown`；`address_strap=not shown`；`device=U2` |
| 传感器 | 量程、分辨率、视场与激光 | `document_range=3-200cm`；`document_resolution=1mm`；`document_fov=25°`；`document_wavelength=940nm`；`document_laser_class=Class 1`；`document_accuracy=±3%`；`schematic_performance=not shown` |
| 传感器 | 测量速度与 Long Range 模式 | `document_measurement=23ms`；`document_minimum=8ms`；`document_response=<30ms`；`document_long_range=200cm in Long Range under dark/no IR interference`；`schematic_timing=not shown` |
| 传感器 | 90°传感器安装方向 | `document_rotation=90°`；`document_direction=horizontal forward`；`schematic_board_names=Unit-ToF-90_1F; Unit-ToF-90_2F`；`mechanical_evidence=not shown` |
| 电源 | 待机与工作功耗 | `document_standby_no_led=DC 5.03V@15.01uA`；`document_standby_with_led=DC 5.02V@1.92mA`；`document_working=DC 5.02V@10.99mA`；`schematic_measurement=not shown`；`led_branch=3V3 -> R7 1KΩ -> D1 -> GND` |
| 其他事实 | 整机工作温度 | `document_temperature=0-40°C`；`schematic_temperature=not shown`；`ldo_rating=not shown`；`sensor_conditions=not shown` |

## 待确认事项

- `component.sensor-name-equivalence`：产品正文把传感器称为 VL53L0X，原理图 U2 完整字段为 VL53L0CXV0DH/1；本页没有 BOM 或订货型号说明二者的精确对应关系。（证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C3，U2 标识 VL53L0CXV0DH/1）
- `address.i2c-0x29`：产品正文给出 7 位 I2C 地址 0x29，但原理图页面只显示 SDA/SCL 连接，没有打印地址或地址选择网络。（证据：图 82039681f5a5 / 第 1 页 / 第1页网格 C2-C3，U2 SDA/SCL 与上拉，无地址标注）
- `sensor.optical-performance`：产品正文给出 3-200cm、1mm、25° FoV、940nm VCSEL/Class 1 与 ±3% 等参数；原理图没有光学结构、标定条件或性能表。（证据：图 82039681f5a5 / 第 1 页 / 第1页 U2 电气连接，无光学性能字段）
- `sensor.timing-modes`：产品正文给出 23ms、最短 8ms、响应时间小于 30ms，并称 200cm 需要 Long Range 和暗环境；原理图没有时序、固件配置或环境条件。（证据：图 82039681f5a5 / 第 1 页 / 第1页 U2 I2C/XSHUT/GPIO1 电路，无时序或模式注记）
- `sensor.physical-rotation`：产品名和正文表示传感器旋转 90°、水平前向探测；原理图仅以 1F/2F 电路框表示两块板，没有机械视图或光轴方向。（证据：图 82039681f5a5 / 第 1 页 / 第1页上下 1F/2F 电气框，无机械安装视图）
- `power.consumption`：产品正文给出无 LED/含 LED 待机及工作电流，但原理图没有测试点、传感器模式、主机状态或测量条件。（证据：图 82039681f5a5 / 第 1 页 / 第1页 J1/U1/D1/U2 电源链路，无电流测量数据）
- `other.operating-temperature`：产品正文给出 0-40°C，原理图未标整机温度范围、LDO 额定负载或传感器工作条件。（证据：图 82039681f5a5 / 第 1 页 / 第1页完整单页，无温度或系统额定参数表）
- `review.sensor-name-equivalence`：请用 U196 BOM、实装丝印或 ST 订货资料确认图纸 VL53L0CXV0DH/1 与正文 VL53L0X 的精确器件/封装关系。；原因：正文通用型号与原理图完整字段不同，本页没有 BOM 解释。
- `review.i2c-address`：请用对应 U2 datasheet、驱动或总线实测确认默认 7 位地址为 0x29，并说明是否支持运行时改址。；原因：地址来自产品正文，原理图没有地址字段或选择网络。
- `review.optical-performance`：请用实装传感器 datasheet 与 U196 光学/标定测试确认量程、分辨率、FoV、波长、激光等级和精度。；原因：这些是器件与结构性能，原理图没有测试条件。
- `review.timing-modes`：请按驱动配置和环境条件实测 8ms/23ms/<30ms 时序及 200cm Long Range 模式。；原因：原理图没有固件时序、模式或环境条件。
- `review.physical-rotation`：请用 U196 PCB/结构图或实物确认传感器相对 Grove 板旋转 90°及实际光轴方向。；原因：原理图只有 1F/2F 电气分区，没有机械安装证据。
- `review.power-consumption`：请按 LED 状态、传感器模式和 5V 输入条件复测待机与工作电流。；原因：正文电流值没有对应的图纸测量方法。
- `review.operating-temperature`：请用整机规格、BOM 器件额定值和环境测试确认 0-40°C 工作范围。；原因：温度范围未印在原理图上。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `82039681f5a55c96648ce3c93b12f23b4628c2ce1c70ae6e55be4f3f0f3029ea` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_SCH.png` |

---

源文档：`zh_CN/unit/Unit Mini ToF-90.md`

源文档 SHA-256：`7156bd3d21a1eee49c5130db7dfcbf9140fa189b25318756b01ecfc1593e12d6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
