# Module GoPlus 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module GoPlus |
| SKU | M025 |
| 产品 ID | `module-goplus-140e3b5d1a2f` |
| 源文档 | `zh_CN/module/goplus.md` |

## 概述

Module GoPlus 以 U3 ATMEGA328 为控制器，通过 I2C 与 J2 M5Stack_BUS 通信，并连接四路舵机、三组 Port B、双路直流电机桥和红外收发电路。U1 LV8548MC 的四个输入由 U3 IN1-IN4 驱动，OUT1/OUT2 与 OUT3/OUT4 分别引至 P9、P10 电机端口；B0-B3 分别引至 P4-P7 舵机端口。P8 外部输入经 TPS54360 生成 +6V5，再由 MIC5219-5.0BMS 生成 +5V，VCC 执行器电源通过 D10/Q2/D11/D12 支路形成。

## 检索关键词

`Module GoPlus`、`M025`、`ATMEGA328`、`LV8548MC`、`TPS54360`、`MIC5219-5.0BMS`、`I2C`、`0x61`、`IN1`、`IN2`、`IN3`、`IN4`、`OUT1`、`OUT2`、`OUT3`、`OUT4`、`B0`、`B1`、`B2`、`B3`、`A0`、`A1`、`A2`、`IR_R`、`IR_S`、`CHQ0038H`、`IR12-21C`、`M5Stack_BUS`、`+6V5`、`+5V`、`VCC`、`IN4.5/24V`、`8MHz`、`ISP_Download`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ATMEGA328 | I2C 从机、双电机控制、四舵机控制、Port B 和红外控制器 | 图 273194532af5 / 第 1 页 / 网格 C2-D2 的 U3 ATMEGA328，周围标注 B0-B3、IN1-IN4、A0-A2、D5-D7、SDA/SCL、IR、ISP 与晶振引脚 |
| U1 | LV8548MC | 两路直流电机四输出 H 桥驱动器 | 图 273194532af5 / 第 1 页 / 网格 B3 的 U1 LV8548MC，IN1-IN4、OUT1-OUT4、VCC、GND 与 P9/P10 电机回路 |
| U2 | TPS54360 | IN+ 至 +6V5 的宽输入降压转换器 | 图 273194532af5 / 第 1 页 / 网格 A1-A2 的 U2 TPS54360，连接 P8/F1 输入、D9、L1、反馈补偿与 +6V5 |
| U4 | MIC5219-5.0BMS | +6V5 至 +5V 的线性稳压器 | 图 273194532af5 / 第 1 页 / 网格 A3 的 U4 MIC5219-5.0BMS，IN/EN 接 +6V5，OUT 接 +5V，BYP 接 C15 |
| P8,F1 | Header 2; PPTC-1812 | 外部 VIN/GND 输入和串联自恢复保险器件 | 图 273194532af5 / 第 1 页 / 网格 A1 的 P8 Header 2，pin 1 VIN 经 F1 PPTC-1812 到 IN+，pin 2 接 GND |
| Q2,D10,D11,D12,R9 | AO3401A; SS54; B5819W SL; B5819W SL; 10KΩ | +6V5/+5V 到执行器 VCC 的电源选择与隔离支路 | 图 273194532af5 / 第 1 页 / 网格 B2 的 +6V5-D10-VCC 与 +5V-Q2-D11/D12-VCC、R9 到 GND 电路 |
| P9,P10 | Header 2 | 两路直流电机输出连接器 | 图 273194532af5 / 第 1 页 / 网格 B4 的 P9、P10 Header 2，分别连接 U1 OUT1/OUT2 与 OUT3/OUT4 |
| D1-D8,C5,C6 | T4; 100nF; 100nF | 电机输出到 VCC/GND 的八二极管钳位阵列及端口抑制电容 | 图 273194532af5 / 第 1 页 / 网格 B3-B4 U1 输出周围 D1-D4 接 VCC、D5-D8 接 GND，P9/P10 旁 C5/C6 100nF |
| P4-P7 | Header 3 | B0-B3 四路舵机信号、VCC 和 GND 接口 | 图 273194532af5 / 第 1 页 / 网格 C1-D1 的 P4、P5、P6、P7 Header 3，pin 1 GND、pin 2 VCC、pin 3 分别 B0-B3 |
| P1-P3 | Header 4 | 三组 Port B 扩展接口，分别引出 A0/D5、A1/D6、A2/D7、+5V 和 GND | 图 273194532af5 / 第 1 页 / 网格 B1-C1 的 P1、P2、P3 Header 4，pin 1/2 为 Ax/Dx，pin 3 +5V，pin 4 GND |
| IR1,R10 | CHQ0038H; 4.7KΩ | 红外接收器及 IR_R 输出上拉 | 图 273194532af5 / 第 1 页 / 网格 A3 的 IR1 CHQ0038H，OUT 接 IR_R，R10 4.7KΩ 上拉至 +3.3V，VCC/GND 供电 |
| LED1,Q1,R2,R3,R4 | IR12-21C; AO3400A_N; 49.9Ω; 1KΩ; 10KΩ | 由 IR_S 控制的红外发射低侧驱动电路 | 图 273194532af5 / 第 1 页 / 网格 C3 的 +5V-LED1 IR12-21C-R2-Q1-AO3400A_N-GND 支路及 IR_S-R3/R4 栅极网络 |
| Y1,C3,C4 | 8MHz ±20ppm; 20pF; 20pF | U3 主时钟晶体和负载电容 | 图 273194532af5 / 第 1 页 / 网格 C1-D1 的 Y1 8MHz ±20ppm 与 C3/C4 20pF，连接 U3 XTAL1/XTAL2 |
| J1 | ISP_Download | ATMEGA328 六针 ISP 下载接口 | 图 273194532af5 / 第 1 页 / 网格 A4 的 J1 ISP_Download，pin 1-6 标注 VCC、RESET、SCK、MISO、MOSI、GND |
| J2 | M5Stack_BUS | 30 针主机、电源、I2C 和红外接口 | 图 273194532af5 / 第 1 页 / 网格 C4-D4 的 J2 M5Stack_BUS，板内使用 GND、IR_R、+3.3V、SDA、SCL、IR_S、+5V |

## 系统结构

### Module GoPlus 系统架构

U3 ATMEGA328 通过 J2 I2C 与主机通信，控制 U1 LV8548MC 两路直流电机、P4-P7 四路舵机、P1-P3 三组 Port B 和红外收发；TPS54360/MIC5219 电源链提供 +6V5、+5V 与执行器 VCC。

- 参数与网络：`controller=U3 ATMEGA328`；`motor_driver=U1 LV8548MC`；`dc_motor_ports=P9,P10`；`servo_ports=P4-P7`；`port_b=P1-P3`；`ir_receiver=IR1 CHQ0038H`；`ir_transmitter=LED1/Q1`；`host=J2 M5Stack_BUS`
- 证据：图 273194532af5 / 第 1 页 / 完整单页网格 A1-D4 的电源、控制器、电机、舵机、Port B、IR 与 M5-Bus 功能区

## 电源

### P8 至 +6V5 降压路径

页面电源区标注 IN4.5/24V；P8 pin 1 VIN 经 F1 PPTC-1812 形成 IN+，进入 U2 TPS54360 VIN/pin 2，SW/pin 8 经 L1 8.2uH 输出 +6V5，D9 B290B 从 SW 节点连接 GND。

- 参数与网络：`schematic_input_label=IN4.5/24V`；`connector=P8 Header 2`；`positive_pin=pin 1/VIN`；`return_pin=pin 2/GND`；`fuse=F1 PPTC-1812`；`converter=U2 TPS54360`；`inductor=L1 8.2uH`；`catch_diode=D9 B290B`；`output=+6V5`
- 证据：图 273194532af5 / 第 1 页 / 网格 A1-A3 的 IN4.5/24V、P8/F1、U2、D9、L1 与 +6V5 路径

### TPS54360 反馈与补偿

R6 71.5KΩ 从 +6V5 连接 U2 FB/pin 5，R8 10KΩ 从 FB 接 GND；COMP/pin 6 经 R5 12KΩ 与 C11 6.8nF 串联接 GND，RT/CLK pin 4 经 R7 160KΩ接 GND。

- 参数与网络：`feedback_upper=R6 71.5KΩ`；`feedback_lower=R8 10KΩ`；`compensation=R5 12KΩ series C11 6.8nF`；`frequency_resistor=R7 160KΩ`；`output_filter=C9 10uF,C10 10uF`
- 证据：图 273194532af5 / 第 1 页 / 网格 A2-A3 的 U2 FB/COMP/RT、R5/R6/R7/R8、C9/C10/C11

### U4 +5V 稳压

U4 MIC5219-5.0BMS 的 IN/pin 1 与 EN/pin 3 接 +6V5，OUT/pin 5 输出 +5V，BYP/pin 4 经 C15 470pF接 GND；C14 100nF 与 C16 2.2uF 分别用于输入和输出滤波。

- 参数与网络：`regulator=U4 MIC5219-5.0BMS`；`input=+6V5`；`enable=+6V5`；`output=+5V`；`bypass=C15 470pF`；`input_capacitor=C14 100nF`；`output_capacitor=C16 2.2uF`
- 证据：图 273194532af5 / 第 1 页 / 网格 A3 的 U4 MIC5219-5.0BMS、C14/C15/C16 与 +6V5/+5V/GND

### 执行器 VCC 电源支路

+6V5 经 D10 SS54 连接 VCC；+5V 经过 Q2 AO3401A、D11/D12 B5819W SL 支路连接 VCC，Q2 相关节点由 R9 10KΩ下拉至 GND。VCC 供给 LV8548MC 和 P4-P7 舵机端口。

- 参数与网络：`high_rail_path=+6V5 -> D10 SS54 -> VCC`；`five_volt_path=+5V -> Q2 AO3401A/D11/D12 B5819W SL -> VCC`；`bias=R9 10KΩ to GND`；`loads=U1 LV8548MC,P4-P7`
- 证据：图 273194532af5 / 第 1 页 / 网格 B2 的 D10/Q2/D11/D12/R9/VCC 与网格 B3-C1 的 U1、P4-P7 VCC

### U3 +5V 供电

U3 AVCC/pin 18 与 VCC pin 4、pin 6 连接 +5V，GND pin 3、pin 5、pin 21 接 GND；C8 100nF 连接 +5V 与 GND。

- 参数与网络：`rail=+5V`；`supply_pins=U3 AVCC pin 18,VCC pin 4,6`；`ground_pins=U3 pin 3,5,21`；`decoupling=C8 100nF`
- 证据：图 273194532af5 / 第 1 页 / 网格 C2-D3 的 U3 AVCC/VCC/GND 与 C8 100nF

## 接口

### P9/P10 双电机输出

U1 OUT1/pin 10 与 OUT2/pin 9 连接 P9 pin 1、pin 2；OUT3/pin 8 与 OUT4/pin 7 连接 P10 pin 1、pin 2。C5、C6 各 100nF，分别跨接 P9、P10 两端。

- 参数与网络：`motor1=P9 pin 1:OUT1,pin 2:OUT2,C5 100nF`；`motor2=P10 pin 1:OUT3,pin 2:OUT4,C6 100nF`；`driver=U1 LV8548MC`
- 证据：图 273194532af5 / 第 1 页 / 网格 B3-B4 U1 OUT1-OUT4 至 P9/P10 与 C5/C6

### P1-P3 三组 Port B

P1 pin 1-4 为 A0、D5、+5V、GND；P2 为 A1、D6、+5V、GND；P3 为 A2、D7、+5V、GND。A0-A2 对应 U3 PC0-PC2，D5-D7 对应 U3 PD5-PD7。

- 参数与网络：`P1=1:A0/U3 PC0 pin 23,2:D5/U3 PD5 pin 9,3:+5V,4:GND`；`P2=1:A1/U3 PC1 pin 24,2:D6/U3 PD6 pin 10,3:+5V,4:GND`；`P3=1:A2/U3 PC2 pin 25,2:D7/U3 PD7 pin 11,3:+5V,4:GND`
- 证据：图 273194532af5 / 第 1 页 / 网格 B1-C1 P1-P3 pin 1-4 与 U3 A0-A2/D5-D7 网络

### J2 M5Stack_BUS 已用针脚

J2 pin 1、3、5 连接 GND，pin 2 GPIO35 连接 IR_R，pin 12 连接 +3.3V，pin 17 GPIO21 连接 SDA，pin 18 GPIO22 连接 SCL，pin 22 GPIO13 连接 IR_S，pin 28 连接 +5V；其余针脚在本页无板内连线。

- 参数与网络：`used_pinout=1:GND,2:GPIO35/IR_R,3:GND,5:GND,12:+3.3V,17:GPIO21/SDA,18:GPIO22/SCL,22:GPIO13/IR_S,28:+5V`；`reference=J2 M5Stack_BUS`
- 证据：图 273194532af5 / 第 1 页 / 网格 C4-D4 J2 M5Stack_BUS 的外部蓝色/红色网络连线

## 总线

### U3 与 J2 的 I2C

U3 PC4/SDA/pin 27 连接 J2 pin 17 GPIO21/SDA，U3 PC5/SCL/pin 28 连接 J2 pin 18 GPIO22/SCL；本页未绘出 SDA/SCL 上拉电阻。

- 参数与网络：`controller=U3`；`sda_mcu_pin=PC4/pin 27`；`sda_bus_pin=J2 pin 17/GPIO21`；`scl_mcu_pin=PC5/pin 28`；`scl_bus_pin=J2 pin 18/GPIO22`；`pullups_visible=false`
- 证据：图 273194532af5 / 第 1 页 / U3 PC4/SDA、PC5/SCL 与 J2 pin 17 SDA、pin 18 SCL

## GPIO 与控制信号

### LV8548MC 输入映射

U3 PC3/pin 26 连接 IN1，PD2/pin 32 连接 IN2，PD3/pin 1 连接 IN3，PD4/pin 2 连接 IN4；四条网络分别连接 U1 IN1/pin 2 至 IN4/pin 5。

- 参数与网络：`IN1=U3 PC3/pin 26 -> U1 pin 2`；`IN2=U3 PD2/pin 32 -> U1 pin 3`；`IN3=U3 PD3/pin 1 -> U1 pin 4`；`IN4=U3 PD4/pin 2 -> U1 pin 5`
- 证据：图 273194532af5 / 第 1 页 / U3 PC3/PD2/PD3/PD4 的 IN1-IN4 标注与网格 B3 U1 IN1-IN4

### 四路舵机信号映射

U3 PB0/pin 12、PB1/pin 13、PB2/pin 14、PB3/pin 15 分别连接 B0、B1、B2、B3，并引至 P4、P5、P6、P7 pin 3；各舵机端口 pin 1 为 GND、pin 2 为 VCC。

- 参数与网络：`P4=1:GND,2:VCC,3:B0/U3 PB0 pin 12`；`P5=1:GND,2:VCC,3:B1/U3 PB1 pin 13`；`P6=1:GND,2:VCC,3:B2/U3 PB2 pin 14`；`P7=1:GND,2:VCC,3:B3/U3 PB3 pin 15`
- 证据：图 273194532af5 / 第 1 页 / U3 PB0-PB3/B0-B3 与网格 C1-D1 P4-P7 Header 3

### IR_S 红外发射驱动

J2 pin 22 GPIO13 的 IR_S 经 R3 1KΩ连接 Q1 AO3400A_N 栅极，R4 10KΩ将栅极下拉至 GND；Q1 低侧驱动 +5V 经 LED1 IR12-21C 和 R2 49.9Ω的发射支路。

- 参数与网络：`control=J2 pin 22/GPIO13/IR_S`；`gate_resistor=R3 1KΩ`；`gate_pulldown=R4 10KΩ`；`switch=Q1 AO3400A_N`；`led=LED1 IR12-21C`；`series_resistor=R2 49.9Ω`；`supply=+5V`
- 证据：图 273194532af5 / 第 1 页 / 网格 C3 IR_S-R3/R4-Q1-LED1/R2 与网格 C4 J2 pin 22 IR_S

## 时钟

### U3 8MHz 时钟

Y1 标注 8MHz ±20ppm，连接 U3 PB6/XTAL1 pin 7 与 PB7/XTAL2 pin 8；C3、C4 均为 20pF，并分别从两条晶振网络接至 GND。

- 参数与网络：`crystal=Y1`；`frequency=8MHz`；`tolerance=±20ppm`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C3 20pF,C4 20pF`
- 证据：图 273194532af5 / 第 1 页 / 网格 C1-D1 Y1、C3、C4 与 U3 XTAL1/XTAL2

## 复位

### U3 RESET 网络

U3 PC6/RESET pin 29 连接 RESET，R1 10KΩ将 RESET 上拉至 +5V，C2 100nF 将 RESET 连接至 GND，RESET 同时引至 J1 pin 2。

- 参数与网络：`mcu_pin=U3 PC6/RESET pin 29`；`pullup=R1 10KΩ to +5V`；`capacitor=C2 100nF to GND`；`isp_pin=J1 pin 2`
- 证据：图 273194532af5 / 第 1 页 / 网格 C1-C2 R1/C2/RESET/U3 pin 29 与网格 A4 J1 RESET

## 保护电路

### 电机输出钳位阵列

D1-D4 标注 T4，分别从四条电机输出连接 VCC；D5-D8 标注 T4，分别从四条电机输出连接 GND。

- 参数与网络：`upper_clamps=D1-D4 T4 to VCC`；`lower_clamps=D5-D8 T4 to GND`；`protected_nodes=OUT1,OUT2,OUT3,OUT4`
- 证据：图 273194532af5 / 第 1 页 / 网格 B3-B4 U1 输出外围 D1-D8 与 VCC/GND 母线

### 输入与外部端口保护可见性

F1 PPTC-1812 串联在 VIN 输入，电机输出有 D1-D8 钳位；本页未绘出 P1-P7、P9/P10 或 J2 信号端口的 TVS/ESD 器件。

- 参数与网络：`input_fuse=F1 PPTC-1812`；`motor_clamps=D1-D8`；`port_tvs_visible=false`；`signal_esd_visible=false`
- 证据：图 273194532af5 / 第 1 页 / 完整单页 P8/F1、D1-D8 与全部外部连接器外围

## 传感器

### IR1 红外接收

IR1 CHQ0038H OUT/pin 1 连接 IR_R，GND/pin 2 接 GND，VCC/pin 3 接 3.3V；R10 4.7KΩ 将 IR_R 上拉至 +3.3V，IR_R 引至 J2 pin 2 GPIO35。

- 参数与网络：`receiver=IR1 CHQ0038H`；`output=pin 1/IR_R`；`ground=pin 2/GND`；`supply=pin 3/3.3V`；`pullup=R10 4.7KΩ to +3.3V`；`bus_pin=J2 pin 2/GPIO35`
- 证据：图 273194532af5 / 第 1 页 / 网格 A3 IR1/R10/IR_R 与网格 C4 J2 pin 2 IR_R

## 调试与烧录

### J1 ISP 下载接口

J1 pin 1 连接 VCC/+5V，pin 2 连接 RESET，pin 3 连接 SCK，pin 4 连接 MISO，pin 5 连接 MOSI，pin 6 连接 GND；对应 U3 PB5/SCK、PB4/MISO、PB3/MOSI 和 PC6/RESET。

- 参数与网络：`pinout=1:VCC/+5V,2:RESET,3:SCK,4:MISO,5:MOSI,6:GND`；`mcu_mapping=SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15,RESET:PC6 pin 29`
- 证据：图 273194532af5 / 第 1 页 / 网格 A4 J1 ISP_Download 与 U3 SCK/MISO/MOSI/RESET 网络

## 其他事实

### 其他功能分区可见性

该页未绘出独立存储器、外部存储、音频器件或射频通信器件；红外收发由 IR1 与 LED1 分立电路承担。

- 参数与网络：`external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_radio_visible=false`；`infrared=IR1 CHQ0038H and LED1 IR12-21C`
- 证据：图 273194532af5 / 第 1 页 / 完整单页全部功能区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module GoPlus 系统架构 | `controller=U3 ATMEGA328`；`motor_driver=U1 LV8548MC`；`dc_motor_ports=P9,P10`；`servo_ports=P4-P7`；`port_b=P1-P3`；`ir_receiver=IR1 CHQ0038H`；`ir_transmitter=LED1/Q1`；`host=J2 M5Stack_BUS` |
| 电源 | P8 至 +6V5 降压路径 | `schematic_input_label=IN4.5/24V`；`connector=P8 Header 2`；`positive_pin=pin 1/VIN`；`return_pin=pin 2/GND`；`fuse=F1 PPTC-1812`；`converter=U2 TPS54360`；`inductor=L1 8.2uH`；`catch_diode=D9 B290B`；`output=+6V5` |
| 电源 | TPS54360 反馈与补偿 | `feedback_upper=R6 71.5KΩ`；`feedback_lower=R8 10KΩ`；`compensation=R5 12KΩ series C11 6.8nF`；`frequency_resistor=R7 160KΩ`；`output_filter=C9 10uF,C10 10uF` |
| 电源 | U4 +5V 稳压 | `regulator=U4 MIC5219-5.0BMS`；`input=+6V5`；`enable=+6V5`；`output=+5V`；`bypass=C15 470pF`；`input_capacitor=C14 100nF`；`output_capacitor=C16 2.2uF` |
| 电源 | 执行器 VCC 电源支路 | `high_rail_path=+6V5 -> D10 SS54 -> VCC`；`five_volt_path=+5V -> Q2 AO3401A/D11/D12 B5819W SL -> VCC`；`bias=R9 10KΩ to GND`；`loads=U1 LV8548MC,P4-P7` |
| 电源 | U3 +5V 供电 | `rail=+5V`；`supply_pins=U3 AVCC pin 18,VCC pin 4,6`；`ground_pins=U3 pin 3,5,21`；`decoupling=C8 100nF` |
| 总线 | U3 与 J2 的 I2C | `controller=U3`；`sda_mcu_pin=PC4/pin 27`；`sda_bus_pin=J2 pin 17/GPIO21`；`scl_mcu_pin=PC5/pin 28`；`scl_bus_pin=J2 pin 18/GPIO22`；`pullups_visible=false` |
| 总线地址 | I2C 从机地址 | `documented_address=0x61`；`schematic_address_visible=false` |
| GPIO 与控制信号 | LV8548MC 输入映射 | `IN1=U3 PC3/pin 26 -> U1 pin 2`；`IN2=U3 PD2/pin 32 -> U1 pin 3`；`IN3=U3 PD3/pin 1 -> U1 pin 4`；`IN4=U3 PD4/pin 2 -> U1 pin 5` |
| 接口 | P9/P10 双电机输出 | `motor1=P9 pin 1:OUT1,pin 2:OUT2,C5 100nF`；`motor2=P10 pin 1:OUT3,pin 2:OUT4,C6 100nF`；`driver=U1 LV8548MC` |
| 保护电路 | 电机输出钳位阵列 | `upper_clamps=D1-D4 T4 to VCC`；`lower_clamps=D5-D8 T4 to GND`；`protected_nodes=OUT1,OUT2,OUT3,OUT4` |
| GPIO 与控制信号 | 四路舵机信号映射 | `P4=1:GND,2:VCC,3:B0/U3 PB0 pin 12`；`P5=1:GND,2:VCC,3:B1/U3 PB1 pin 13`；`P6=1:GND,2:VCC,3:B2/U3 PB2 pin 14`；`P7=1:GND,2:VCC,3:B3/U3 PB3 pin 15` |
| 接口 | P1-P3 三组 Port B | `P1=1:A0/U3 PC0 pin 23,2:D5/U3 PD5 pin 9,3:+5V,4:GND`；`P2=1:A1/U3 PC1 pin 24,2:D6/U3 PD6 pin 10,3:+5V,4:GND`；`P3=1:A2/U3 PC2 pin 25,2:D7/U3 PD7 pin 11,3:+5V,4:GND` |
| 传感器 | IR1 红外接收 | `receiver=IR1 CHQ0038H`；`output=pin 1/IR_R`；`ground=pin 2/GND`；`supply=pin 3/3.3V`；`pullup=R10 4.7KΩ to +3.3V`；`bus_pin=J2 pin 2/GPIO35` |
| GPIO 与控制信号 | IR_S 红外发射驱动 | `control=J2 pin 22/GPIO13/IR_S`；`gate_resistor=R3 1KΩ`；`gate_pulldown=R4 10KΩ`；`switch=Q1 AO3400A_N`；`led=LED1 IR12-21C`；`series_resistor=R2 49.9Ω`；`supply=+5V` |
| 接口 | J2 M5Stack_BUS 已用针脚 | `used_pinout=1:GND,2:GPIO35/IR_R,3:GND,5:GND,12:+3.3V,17:GPIO21/SDA,18:GPIO22/SCL,22:GPIO13/IR_S,28:+5V`；`reference=J2 M5Stack_BUS` |
| 调试与烧录 | J1 ISP 下载接口 | `pinout=1:VCC/+5V,2:RESET,3:SCK,4:MISO,5:MOSI,6:GND`；`mcu_mapping=SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15,RESET:PC6 pin 29` |
| 时钟 | U3 8MHz 时钟 | `crystal=Y1`；`frequency=8MHz`；`tolerance=±20ppm`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C3 20pF,C4 20pF` |
| 复位 | U3 RESET 网络 | `mcu_pin=U3 PC6/RESET pin 29`；`pullup=R1 10KΩ to +5V`；`capacitor=C2 100nF to GND`；`isp_pin=J1 pin 2` |
| 保护电路 | 输入与外部端口保护可见性 | `input_fuse=F1 PPTC-1812`；`motor_clamps=D1-D8`；`port_tvs_visible=false`；`signal_esd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`rf_radio_visible=false`；`infrared=IR1 CHQ0038H and LED1 IR12-21C` |

## 待确认事项

- `address.documented-i2c`：原理图未打印 I2C 从机地址；产品正文记载 0x61，但无法仅由本页硬件图确认固件地址。（证据：图 273194532af5 / 第 1 页 / U3 SDA/SCL 与 J2 I2C 区域未见地址值或地址配置器件）
- `review.i2c-address`：Module GoPlus 当前固件的 I2C 从机地址是否确认为产品正文记载的 0x61？；原因：原理图只显示 SDA/SCL 物理连接，没有打印地址值、地址选择网络或固件定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `273194532af55cf9dac9d968980b9ce2ce80e6679a765b0d0c14d867af7b4234` | `https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_sch_01.webp` |

---

源文档：`zh_CN/module/goplus.md`

源文档 SHA-256：`17b8ca250bb12e6c15b2cacd6e421204f9a39f047df9058aeb7ef82e6a3d3a16`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
