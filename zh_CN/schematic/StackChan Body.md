# StackChan Body 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StackChan Body |
| SKU | A180 |
| 产品 ID | `stackchan-body-b8923242348a` |
| 源文档 | `zh_CN/base/StackChan_Body.md` |

## 概述

StackChan Body 由 Adapter、Power、Ring 与 Touch 四块原理图资产组成：Adapter 汇聚 USB、电池与两路舵机，Power 板提供 TPS61088 5V 升压、舵机半双工串口、INA226 电池监测、PY32 IO 扩展和红外发射。Ring 板提供带 2A 保险丝的 USB Type-C 电源/数据及四圈旋转触点，Touch 板集成 IRM-56384 红外接收、12 颗 WS2812C、Si12T 三点触摸和 ST25R3916 NFC。系统 I2C 总线连接 INA226、PY32IO_EXP、Si12T 与 ST25R3916，原理图明确地址分别为 0x41、0x6F、0x68 与 0x50。正文所列 550mAh 电池、SCS0009 舵机反馈/角度、PY32L020 具体型号和 NFC 性能未在原理图中完整标注，保留待确认。

## 检索关键词

`StackChan Body`、`A180`、`TPS61088`、`FH9261-G3JZ`、`INA226AIDGSR`、`INA226 0x41`、`PY32IO_EXP`、`PY32 0x6F`、`Si12T`、`Si12T 0x68`、`ST25R3916-AQWT`、`ST25R3916 0x50`、`IRM-56384`、`WS2812C_4020`、`SN74LVC1G126DC`、`SN74LVC1G125DC`、`LP3218DT1G`、`AH20P30Q`、`S8050 Y1`、`SS8550 Y2`、`USB_5V`、`BUS_5V`、`BUS_3V3`、`BAT+`、`BAT_IN`、`VM`、`VM_EN`、`Servo_SIG`、`Servo_TX`、`Servo_RX`、`UART_RX`、`UART_TX`、`I2C_SCL`、`I2C_SDA`、`IR_SEND`、`IR_REC`、`Touch_IRQ`、`RGB`、`ANT_NFC`、`27.12MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | FH9261-G3JZ | Adapter 板单节电池保护控制器，配合 Q1/Q2 背靠背 NMOS 连接 BAT+/B-/GND/VM | 图 9db48f62a793 / 第 1 页 / Adapter 页网格 A3-B4，U1 FH9261-G3JZ、Q1/Q2、BAT+/B-/VM |
| CON1,CON2 | GT-BTP25004-0240A-010A | Adapter 板两组 USB/5V/地板间连接器 | 图 9db48f62a793 / 第 1 页 / Adapter 页网格 B1-C2，CON1/CON2 USB_DP/USB_DM/USB_5V/GND |
| CON3,CON4 | Header 1.25-2 / Header 1.25-7 | Adapter 板电池与主板连接器，传送 B-/BAT+ 及 USB/舵机/VM 网络 | 图 9db48f62a793 / 第 1 页 / Adapter 页网格 A2-C3，CON3/CON4 |
| S1,S2 | HC-5264-3A | 两路三针舵机接口，均提供 Servo_SIG、VM 与 GND | 图 9db48f62a793 / 第 1 页 / Adapter 页网格 C3，S1/S2 HC-5264-3A |
| U1 | TPS61088 | Power 板 BAT+ 到 5V 电机电源的升压转换器 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 B1-C3，U1 TPS61088、L1、反馈与 VM 开关 |
| Q3,Q4 | AH20P30Q / S8050 Y1 | TPS61088 输出到 VM 的高边开关及 VM_EN 驱动 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 B2-C3，Q3/Q4、VM_EN 与 VM Voltage:5V |
| U5,U4 | SN74LVC1G126DC / SN74LVC1G125DC | 舵机单线半双工串口的发送与接收缓冲/三态转换 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 D1-D3，Servo Serial port signal conversion |
| Q2 | SS8550 Y2 | 由 Servo_TX 经 R9 控制 TX_EN 的 PNP 晶体管 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 D2，Q2 SS8550 Y2、Servo_TX、TX_EN |
| U2 | INA226AIDGSR | 0x41 电池电流/电压监测器，采样 BAT_IN/BAT+ 及 10mΩ 分流路径 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 C3-D4，U2 INA226AIDGSR、0x41、BAT_IN/BAT+ |
| U3 | PY32IO_EXP | 0x6F I2C IO 扩展器，输出 VM_EN、RGB 并连接 NRST | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 B3-C4，U3 PY32IO_EXP 与地址注释 |
| Q1,D1 | S8050 Y1 / IR LED | IR_SEND 控制的红外发射驱动 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 A3-B3，Infrared Transmitter |
| J1,J2 | GROVE_C / GROVE_B | 两组 Grove 接口，分别提供 UART 与 GPIO8/GPIO9，均带 BUS_5V/GND | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 A1，J1/J2 Grove |
| BUS1 | M5Stack_BUS | 30 针 CoreS3/StackChan 主总线接口 | 图 a3c6b35ef1aa / 第 1 页 / Power 页网格 A4-B4，BUS1 CoreS3 PinMap |
| USB1,F1 | TYPE-C 16P / Fuse 0603 2A/6V | Ring 板 USB Type-C 电源/数据接口及 VBUS 保险丝 | 图 856c1ae467b5 / 第 1 页 / Ring 页网格 A1-B2，USB1/F1/R1/R2 |
| D1 | IRM-56384 | Touch 板 3.3V 红外接收器，输出 IR_REC | 图 4599f61bb443 / 第 1 页 / Touch 页网格 A1-B2，D1 IRM-56384 |
| U1-U12 | WS2812C_4020 | BUS_5V 供电的 12 颗串联 RGB LED | 图 4599f61bb443 / 第 1 页 / Touch 页网格 A2-B4，U1-U12 WS2812C_4020 |
| U14 | Si12T | 0x68 三区域电容触摸控制器，输出 Touch_IRQ | 图 4599f61bb443 / 第 1 页 / Touch 页网格 B1-D2，U14 Si12T、TP1-TP3、0x68 |
| U13 | ST25R3916-AQWT | 0x50 NFC 读写器，连接 27.12MHz 晶体和差分 NFC 天线匹配网络 | 图 4599f61bb443 / 第 1 页 / Touch 页网格 B2-D4，U13 ST25R3916-AQWT、0x50、Y1、ANT_NFC |
| Y1 | 27.12MHZ | ST25R3916 外部晶体时钟 | 图 4599f61bb443 / 第 1 页 / Touch 页网格 C2-D3，Y1 27.12MHZ、C16/C17 |
| ANT1,L1,L2 | ANT_NFC / 270nH 5% | ST25R3916 差分 NFC 天线与匹配网络 | 图 4599f61bb443 / 第 1 页 / Touch 页网格 B3-C4，RFI_P/N、L1/L2、ANT1 与 C1-C15 |

## 系统结构

### 四板系统架构

StackChan Body 由 Adapter、Power、Ring 与 Touch 四块板组成：Adapter 汇聚电池/USB/舵机，Power 负责供电、总线和监测，Ring 提供旋转 USB 接触，Touch 集成红外接收、RGB、触摸与 NFC。

- 参数与网络：`adapter=battery,USB,servo`；`power=boost,bus,monitor,IR TX`；`ring=USB-C and concentric contacts`；`touch=IR RX,12 RGB,Si12T,ST25R3916`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 全页; 图 a3c6b35ef1aa / 第 1 页 / Power 全页; 图 856c1ae467b5 / 第 1 页 / Ring 全页; 图 4599f61bb443 / 第 1 页 / Touch 全页

## 电源

### 电池保护路径

CON3 引入 BAT+ 与 B-，U1 FH9261-G3JZ 配合 Q1/Q2 背靠背 NMOS 控制受保护负端/VM 路径；R2、R3 与 C1 构成外围。

- 参数与网络：`battery_connector=CON3 pin1 B-,pin2 BAT+`；`controller=U1 FH9261-G3JZ`；`mosfets=Q1/Q2 NMOS`；`positive=BAT+`；`negative=B-/GND`；`motor_rail=VM`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 页网格 A2-B4，Battery protection

### BAT+ 到 5V VM 升压

TPS61088 以 BAT+ 为输入，L1 2.2uH 接 SW，R3 110KΩ/R4 33KΩ构成反馈；输出经 Q3 高边开关形成标注 VM Voltage:5V 的 VM。

- 参数与网络：`input=BAT+`；`converter=U1 TPS61088`；`inductor=L1 2.2uH`；`feedback=R3 110K,R4 33K`；`switch=Q3 AH20P30Q`；`output=VM 5V`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页网格 B1-C3，DCDC 区

## 接口

### Adapter CON4 针脚

CON4 pin1=USB_5V、pin2=USB_DM、pin3=USB_DP、pin4=GND、pin5=Servo_SIG、pin6=VM、pin7=BAT+。

- 参数与网络：`connector=CON4 Header 1.25-7`；`pin1=USB_5V`；`pin2=USB_DM`；`pin3=USB_DP`；`pin4=GND`；`pin5=Servo_SIG`；`pin6=VM`；`pin7=BAT+`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 页网格 B2-C3，CON4 pins1-7

### 双舵机接口

S1 与 S2 的 pin1=Servo_SIG、pin2=VM、pin3=GND，两路舵机共用信号与 5V VM 电源。

- 参数与网络：`connectors=S1,S2 HC-5264-3A`；`pin1=Servo_SIG`；`pin2=VM`；`pin3=GND`；`supply=VM 5V`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 页网格 C2-C3，S1/S2

### J1 Grove UART

J1 GROVE_C pin1=UART_RX、pin2=UART_TX、pin3=BUS_5V、pin4=GND。

- 参数与网络：`connector=J1 GROVE_C`；`pin1=UART_RX`；`pin2=UART_TX`；`pin3=BUS_5V`；`pin4=GND`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页网格 A1，J1

### J2 Grove GPIO

J2 GROVE_B pin1=GPIO8、pin2=GPIO9、pin3=BUS_5V、pin4=GND。

- 参数与网络：`connector=J2 GROVE_B`；`pin1=GPIO8`；`pin2=GPIO9`；`pin3=BUS_5V`；`pin4=GND`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页网格 A1，J2

### Touch FPC1 针脚

Touch 板 FPC1 pin8=IR_REC、pin7=Touch_IRQ、pin6=I2C_SDA、pin5=I2C_SCL、pin4=RGB、pin3=GND、pin2=VCC_3V3、pin1=BUS_5V。

- 参数与网络：`pin8=IR_REC`；`pin7=Touch_IRQ`；`pin6=I2C_SDA`；`pin5=I2C_SCL`；`pin4=RGB`；`pin3=GND`；`pin2=VCC_3V3`；`pin1=BUS_5V`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页网格 A1，FPC1 pins1-8

### Ring USB Type-C 接口

USB1 VCC 经 F1 2A/6V 保险丝连接 USB_5V，DP1/DP2 合并为 USB_DP，DN1/DN2 合并为 USB_DM，CC1/CC2 各由 5.1KΩ下拉。

- 参数与网络：`connector=USB1 TYPE-C 16P`；`vbus=F1 2A/6V -> USB_5V`；`dp=USB_DP`；`dm=USB_DM`；`cc=R1/R2 5.1K to GND`；`role=USB power and data`
- 证据：图 856c1ae467b5 / 第 1 页 / Ring 页网格 A1-B2，USB1/F1/R1/R2

### Ring 四圈触点

Ring 板四个同心触点分别连接 TP1=GND、TP2=USB_DP、TP3=USB_5V、TP4=USB_DM。

- 参数与网络：`TP1=GND`；`TP2=USB_DP`；`TP3=USB_5V`；`TP4=USB_DM`
- 证据：图 856c1ae467b5 / 第 1 页 / Ring 页网格 A3-C4，同心环 TP1-TP4

## 总线

### 舵机半双工串口

Servo_TX 经 U5 SN74LVC1G126DC 驱动 Servo_SIG，Servo_SIG 经 U4 SN74LVC1G125DC 返回 Servo_RX；Q2 SS8550 Y2 生成 TX_EN 控制三态方向。

- 参数与网络：`tx=Servo_TX -> U5 -> Servo_SIG`；`rx=Servo_SIG -> U4 -> Servo_RX`；`direction=TX_EN`；`direction_driver=Q2 SS8550 Y2`；`logic_supply=BUS_3V3`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页网格 D1-D3，Servo Serial port signal conversion

### 系统 I2C 总线

I2C_SCL/I2C_SDA 连接 BUS1、FPC1、PY32IO_EXP、INA226、Si12T 与 ST25R3916；Power 板 R19/R20 4.7KΩ 和 Touch 板 R4/R5 4.7KΩ提供 3.3V 上拉。

- 参数与网络：`scl=I2C_SCL`；`sda=I2C_SDA`；`devices=PY32IO_EXP,INA226,Si12T,ST25R3916`；`host=BUS1 pins18/17`；`pullups=R19/R20 and R4/R5 4.7K to 3.3V`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 BUS1/U2/U3 I2C 网络; 图 4599f61bb443 / 第 1 页 / Touch 页 U14/U13 I2C 网络

## 总线地址

### PY32IO_EXP 地址

U3 下方标注默认地址 0x6F，ADD_SEL=0 时为 0x6F、ADD_SEL=1 时为 0x71；R27 为 NC、R26 10KΩ下拉，故当前为 0x6F。

- 参数与网络：`device=U3 PY32IO_EXP`；`address_7bit=0x6F`；`alternate=0x71`；`add_sel=0 via R26 10K to GND,R27 NC`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 IO Expansion 区地址注释与 ADD_SEL

### INA226 地址

U2 下方明确标注 I2C Address:0x41 (default)，A0/A1 配置网络接地。

- 参数与网络：`device=U2 INA226AIDGSR`；`address_7bit=0x41`；`a0=GND`；`a1=GND`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 Battery Current and Voltage Monitor 区 0x41 注释

### Si12T 地址

Touch 页 U14 下方明确标注 I2C address:0x68。

- 参数与网络：`device=U14 Si12T`；`address_7bit=0x68`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 TOUCH 区 U14 下方 0x68

### ST25R3916 地址

Touch 页 U13 下方明确标注 I2C address:0x50。

- 参数与网络：`device=U13 ST25R3916-AQWT`；`address_7bit=0x50`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 NFC 区 U13 下方 0x50

## GPIO 与控制信号

### VM 电源使能

PY32IO_EXP IO1 输出 VM_EN，VM_EN 通过 R16 110KΩ 与 Q4 S8050 Y1 控制 Q3 高边开关。

- 参数与网络：`controller=U3 PY32IO_EXP IO1`；`net=VM_EN`；`resistor=R16 110K`；`driver=Q4 S8050 Y1`；`switch=Q3 AH20P30Q`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 DCDC 与 IO Expansion 区 VM_EN

### 红外发射

IR_SEND 经 R6 4.7KΩ驱动 Q1 S8050 Y1，Q1 下拉 D1 红外 LED；LED 上端经 R1 51Ω接 BUS_5V。

- 参数与网络：`control=IR_SEND`；`base_resistor=R6 4.7K`；`driver=Q1 S8050 Y1`；`led=D1 IR`；`current_resistor=R1 51R`；`supply=BUS_5V`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 Infrared Transmitter 区

### 12 颗 RGB LED 链

RGB 进入 U1 DIN，U1-U12 WS2812C_4020 逐级 DOUT 到下一颗 DIN，全部由 BUS_5V 供电并接 GND。

- 参数与网络：`input=RGB`；`count=12`；`parts=U1-U12 WS2812C_4020`；`supply=BUS_5V`；`topology=daisy chain`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 RGB 区 U1-U12

## 时钟

### NFC 27.12MHz 时钟

Y1 27.12MHZ 晶体连接 ST25R3916 XTO/XTI pins4/5，C16/C17 各 10pF 接地。

- 参数与网络：`device=U13 ST25R3916-AQWT`；`crystal=Y1 27.12MHZ`；`pins=XTO/XTI`；`load_caps=C16/C17 10pF`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 NFC 区 Y1/C16/C17/U13 XTO/XTI

## 传感器

### 红外接收

D1 IRM-56384 由 VCC_3V3 供电，OUT 输出 IR_REC，GND 接地并通过 FPC1 pin8 返回主板。

- 参数与网络：`receiver=D1 IRM-56384`；`supply=VCC_3V3`；`output=IR_REC`；`connector=FPC1 pin8`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 Infrared Receiver 区

### Si12T 三区触摸

U14 Si12T 连接 TP1、TP2、TP3 三个 680Ω串联触摸通道测试点，IRQ 输出 Touch_IRQ 并由 R10 10KΩ上拉到 VCC_3V3。

- 参数与网络：`controller=U14 Si12T`；`zones=TP1,TP2,TP3`；`series_resistors=R19/R20/R21 680R`；`interrupt=Touch_IRQ`；`irq_pullup=R10 10K to VCC_3V3`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 TOUCH 区 TP1-TP3、U14、Touch_IRQ

## 射频

### ST25R3916 NFC 天线

ST25R3916 RFO1/RFO2 经 L1/L2 270nH 5%、C1-C15 和 R1/R3 2.4Ω构成差分匹配网络，驱动 ANT1/ANT_NFC 线圈。

- 参数与网络：`reader=U13 ST25R3916-AQWT`；`outputs=RFO1/RFO2`；`inductors=L1/L2 270nH 5%`；`damping=R1/R3 2.4R`；`antenna=ANT1 ANT_NFC`；`sense=RFI_P/RFI_N`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 页 NFC 区 RFO/RFI、匹配网络与 ANT1

## 模拟电路

### 电池电流与电压监测

BAT+ 与 BAT_IN 之间串联 R18 10mΩ/0805 分流器；INA226 IN+/IN- 经 R22/R21 各 10Ω 接 BAT+/BAT_IN，VBUS 经 R23 4.7KΩ 接 BUS_3V3 侧监测网络，ALERT 引出。

- 参数与网络：`shunt=R18 10mR/0805`；`positive=BAT+ -> R22 10R -> IN+`；`negative=BAT_IN -> R21 10R -> IN-`；`monitor=U2 INA226AIDGSR`；`alert=ALERT`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 CON4/R18/Q5 与 INA226 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 四板系统架构 | `adapter=battery,USB,servo`；`power=boost,bus,monitor,IR TX`；`ring=USB-C and concentric contacts`；`touch=IR RX,12 RGB,Si12T,ST25R3916` |
| 接口 | Adapter CON4 针脚 | `connector=CON4 Header 1.25-7`；`pin1=USB_5V`；`pin2=USB_DM`；`pin3=USB_DP`；`pin4=GND`；`pin5=Servo_SIG`；`pin6=VM`；`pin7=BAT+` |
| 接口 | 双舵机接口 | `connectors=S1,S2 HC-5264-3A`；`pin1=Servo_SIG`；`pin2=VM`；`pin3=GND`；`supply=VM 5V` |
| 电源 | 电池保护路径 | `battery_connector=CON3 pin1 B-,pin2 BAT+`；`controller=U1 FH9261-G3JZ`；`mosfets=Q1/Q2 NMOS`；`positive=BAT+`；`negative=B-/GND`；`motor_rail=VM` |
| 电源 | BAT+ 到 5V VM 升压 | `input=BAT+`；`converter=U1 TPS61088`；`inductor=L1 2.2uH`；`feedback=R3 110K,R4 33K`；`switch=Q3 AH20P30Q`；`output=VM 5V` |
| GPIO 与控制信号 | VM 电源使能 | `controller=U3 PY32IO_EXP IO1`；`net=VM_EN`；`resistor=R16 110K`；`driver=Q4 S8050 Y1`；`switch=Q3 AH20P30Q` |
| 总线 | 舵机半双工串口 | `tx=Servo_TX -> U5 -> Servo_SIG`；`rx=Servo_SIG -> U4 -> Servo_RX`；`direction=TX_EN`；`direction_driver=Q2 SS8550 Y2`；`logic_supply=BUS_3V3` |
| 接口 | J1 Grove UART | `connector=J1 GROVE_C`；`pin1=UART_RX`；`pin2=UART_TX`；`pin3=BUS_5V`；`pin4=GND` |
| 接口 | J2 Grove GPIO | `connector=J2 GROVE_B`；`pin1=GPIO8`；`pin2=GPIO9`；`pin3=BUS_5V`；`pin4=GND` |
| 接口 | Touch FPC1 针脚 | `pin8=IR_REC`；`pin7=Touch_IRQ`；`pin6=I2C_SDA`；`pin5=I2C_SCL`；`pin4=RGB`；`pin3=GND`；`pin2=VCC_3V3`；`pin1=BUS_5V` |
| 总线 | 系统 I2C 总线 | `scl=I2C_SCL`；`sda=I2C_SDA`；`devices=PY32IO_EXP,INA226,Si12T,ST25R3916`；`host=BUS1 pins18/17`；`pullups=R19/R20 and R4/R5 4.7K to 3.3V` |
| 总线地址 | PY32IO_EXP 地址 | `device=U3 PY32IO_EXP`；`address_7bit=0x6F`；`alternate=0x71`；`add_sel=0 via R26 10K to GND,R27 NC` |
| 总线地址 | INA226 地址 | `device=U2 INA226AIDGSR`；`address_7bit=0x41`；`a0=GND`；`a1=GND` |
| 模拟电路 | 电池电流与电压监测 | `shunt=R18 10mR/0805`；`positive=BAT+ -> R22 10R -> IN+`；`negative=BAT_IN -> R21 10R -> IN-`；`monitor=U2 INA226AIDGSR`；`alert=ALERT` |
| 总线地址 | Si12T 地址 | `device=U14 Si12T`；`address_7bit=0x68` |
| 总线地址 | ST25R3916 地址 | `device=U13 ST25R3916-AQWT`；`address_7bit=0x50` |
| GPIO 与控制信号 | 红外发射 | `control=IR_SEND`；`base_resistor=R6 4.7K`；`driver=Q1 S8050 Y1`；`led=D1 IR`；`current_resistor=R1 51R`；`supply=BUS_5V` |
| 传感器 | 红外接收 | `receiver=D1 IRM-56384`；`supply=VCC_3V3`；`output=IR_REC`；`connector=FPC1 pin8` |
| GPIO 与控制信号 | 12 颗 RGB LED 链 | `input=RGB`；`count=12`；`parts=U1-U12 WS2812C_4020`；`supply=BUS_5V`；`topology=daisy chain` |
| 传感器 | Si12T 三区触摸 | `controller=U14 Si12T`；`zones=TP1,TP2,TP3`；`series_resistors=R19/R20/R21 680R`；`interrupt=Touch_IRQ`；`irq_pullup=R10 10K to VCC_3V3` |
| 时钟 | NFC 27.12MHz 时钟 | `device=U13 ST25R3916-AQWT`；`crystal=Y1 27.12MHZ`；`pins=XTO/XTI`；`load_caps=C16/C17 10pF` |
| 射频 | ST25R3916 NFC 天线 | `reader=U13 ST25R3916-AQWT`；`outputs=RFO1/RFO2`；`inductors=L1/L2 270nH 5%`；`damping=R1/R3 2.4R`；`antenna=ANT1 ANT_NFC`；`sense=RFI_P/RFI_N` |
| 接口 | Ring USB Type-C 接口 | `connector=USB1 TYPE-C 16P`；`vbus=F1 2A/6V -> USB_5V`；`dp=USB_DP`；`dm=USB_DM`；`cc=R1/R2 5.1K to GND`；`role=USB power and data` |
| 接口 | Ring 四圈触点 | `TP1=GND`；`TP2=USB_DP`；`TP3=USB_5V`；`TP4=USB_DM` |
| 电源 | 正文 550mAh 电池 | `documented_capacity=550mAh`；`cell_part_number=null`；`nominal_voltage=null`；`full_voltage=null`；`charger=null`；`temperature_monitor=null` |
| 核心器件 | 正文 SCS0009 舵机与运动范围 | `documented_model=SCS0009`；`documented_horizontal=360 degree continuous`；`documented_vertical=90 degree`；`documented_feedback=true`；`schematic_model=null`；`feedback_protocol=null`；`mechanical_limit=null` |
| 核心器件 | 正文 PY32L020 IO 扩展 | `documented_family=PY32L020`；`schematic_label=PY32IO_EXP`；`exact_part_number=null`；`flash=null`；`ram=null`；`clock=null`；`firmware_version=null` |
| 射频 | 正文全功能 NFC | `reader=ST25R3916-AQWT`；`address=0x50`；`protocols=null`；`output_power=null`；`read_range=null`；`card_types=null`；`antenna_tuning_result=null`；`certification=null` |

## 待确认事项

- `power.documented-battery-capacity`：正文称机身包含 550mAh 电池；原理图只显示 BAT+/B-/BAT_IN、电池保护、分流器和升压路径，没有电芯型号、容量、标称/满充电压、充电器或温度检测。（证据：图 9db48f62a793 / 第 1 页 / Adapter 页 BAT+/B- 与 Battery protection，无容量/充电; 图 a3c6b35ef1aa / 第 1 页 / Power 页 BAT+/BAT_IN 监测与升压，无电池规格）
- `component.documented-servos`：正文称使用 SCS0009，水平舵机 360 度无限旋转、垂直舵机 90 度且均带反馈；原理图只确认 S1/S2 三针 Servo_SIG/VM/GND 接口和半双工串口，没有舵机型号、角度、机械限位或反馈协议。（证据：图 9db48f62a793 / 第 1 页 / Adapter 页 S1/S2 Servo Interface; 图 a3c6b35ef1aa / 第 1 页 / Power 页 Servo Serial port signal conversion）
- `component.documented-py32l020`：正文数据手册指向 PY32L020，原理图器件仅标 U3 PY32IO_EXP，没有完整 MCU 型号、Flash/RAM、时钟、固件版本或启动配置。（证据：图 a3c6b35ef1aa / 第 1 页 / Power 页 U3 PY32IO_EXP）
- `rf.documented-nfc-performance`：原理图确认 ST25R3916、0x50 地址和差分天线匹配，但没有 NFC 协议模式、载波功率、读写距离、支持卡型、调谐值验证或认证信息。（证据：图 4599f61bb443 / 第 1 页 / Touch 页 ST25R3916 与 ANT_NFC 电路，无性能表）
- `review.battery`：请确认 550mAh 电芯型号、额定/满充电压、持续/峰值放电、电池保护阈值、充电器与温度保护。；原因：原理图没有电池 BOM 与充电电路参数。
- `review.servos`：请用 SCS0009 BOM/datasheet 与实机确认两路舵机型号、角度、反馈帧格式、波特率、电流和机械限位。；原因：原理图仅显示通用三针接口与半双工串口。
- `review.py32`：请确认 U3 的完整 PY32L020 料号、内部存储、时钟、固件版本、复位/升级方式和 GPIO 默认状态。；原因：原理图只标 PY32IO_EXP。
- `review.nfc-performance`：请用 ST25R3916 配置、天线调谐与实测确认 NFC 协议、卡型、读写距离、场强、功耗和认证。；原因：原理图只确认芯片与匹配网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9db48f62a793a225399111d25f773c77e1d816ec6c0fea3205ec0c05c3c4617f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Adapter.png` |
| 2 | 1 | `a3c6b35ef1aadbec775fdc0a0241130b374efa8b2d59cb5dd2b48eb063b4ebf6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Power.png` |
| 3 | 1 | `856c1ae467b59541b366e109c831b1d1054103d5ef5431e6986eb6fce4ee452f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Ring.png` |
| 4 | 1 | `4599f61bb443685aa5844104a12c968188342db6a6f71fe4b4da9c428890638f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Touch.png` |

---

源文档：`zh_CN/base/StackChan_Body.md`

源文档 SHA-256：`30ef710fe757a79cb904da4466233dd3d65f9a08fa5ee970b44a1f3ff8abfc28`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
