# Capsule v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Capsule v1.1 |
| SKU | K129-V11 |
| 产品 ID | `capsule-v1-1-45dc2708b826` |
| 源文档 | `zh_CN/core/Capsule_v1.1.md` |

## 概述

Capsule v1.1 的两页资源显示以 M1 STAMP-S3-SMD 为中心的电池充电、唤醒保持、5V/3.3V 转换、RTC8563、BMI270、SPM1423 麦克风、红外 LED、蜂鸣器、microSD、I2C Grove 与双侧扩展排针。BMI270 由 SA0 上拉配置为 0x69，SCL/SDA 映射 G10/G8；麦克风 CLK/DAT 映射 G40/G41；microSD 使用 G11/G12/G14/G39。产品正文声明 v1.1 已升级 Stamp-S3A，并列出 ESP32-S3FN8、8MB Flash、BM8563、250mAh、电流、天线优化和红外距离，但这些信息与页面型号不一致或缺少直接电路证据，已保留待确认。

## 检索关键词

`Capsule v1.1`、`K129-V11`、`M5Capsule`、`STAMP-S3-SMD`、`Stamp-S3A`、`ESP32-S3FN8`、`8MB Flash`、`TP4057`、`CN809J`、`SY7088`、`SY8089`、`RTC8563`、`BM8563`、`BMI270`、`BMI270 0x69`、`SPM1423HM4H-B`、`SPM1423`、`TF-015`、`microSD`、`HY-2.0_IIC`、`IR1`、`Buzzer`、`WAKE`、`HOLD`、`G46`、`G42`、`G40`、`G41`、`G10`、`G8`、`G11`、`G12`、`G14`、`G39`、`G4`、`G2`、`+5VIN`、`+5VOUT`、`VBAT_IN`、`VBAT_OUT`、`+3.3V`、`32.768KHz`、`Capsule Bus`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-SMD | 页面中的主控模组，连接电源、USB、GPIO、UART、I2C、microSD、音频和扩展排针 | 图 ac6e57f217e9 / 第 1 页 / 网格 C2-D3，M1 STAMP-S3-SMD 全部引脚 |
| U2 | TP4057 | +5VIN 到 VBAT_IN 的单节电池充电器 | 图 ac6e57f217e9 / 第 1 页 / 网格 A1-B1，U2 TP4057、R11/R17、C15/C21 |
| U1 | CN809J | +5VIN 供电的复位/监控器件，RESET 接入唤醒控制网络 | 图 ac6e57f217e9 / 第 1 页 / 网格 A1-B2，U1 CN809J |
| U3 | SY7088 | VBAT_OUT 到 +5VOUT 的升压转换器 | 图 ac6e57f217e9 / 第 1 页 / 网格 A3-B4，虚线框内 U3 SY7088、L4、D8 与反馈网络 |
| U4 | SY8089 | VBAT_OUT 到 +3.3V 的降压转换器 | 图 ac6e57f217e9 / 第 1 页 / 网格 B3-B4，U4 SY8089、L5 与反馈网络 |
| U5 | RTC8563 | VBAT_IN 供电的实时时钟，连接 SCL/SDA、INT 和 32.768KHz 晶振 | 图 ac6e57f217e9 / 第 1 页 / 网格 B1-C2，U5 RTC8563 与 Y2 |
| U7 | BMI270 | 0x69 I2C 六轴 IMU，SCL/SDA 连接 G10/G8 | 图 203c49dde3fb / 第 1 页 / 网格 B2-C3，U7 BMI270、R7-R9 与地址注释 |
| U9 | SPM1423HM4H-B | 3.3V 数字麦克风，DAT/CLK 连接 G41/G40 | 图 203c49dde3fb / 第 1 页 / 网格 B1-C2，U9 SPM1423HM4H-B |
| J1 | TF-015 | 3.3V microSD 卡槽，使用 G11/G12/G14/G39 四线 SPI | 图 ac6e57f217e9 / 第 1 页 / 网格 D3-D4，J1 TF-015、R10/R20-R22 与 D9-D14 |
| J3 | HY-2.0_IIC | G15/G13 I2C Grove 接口，可由 +5VOUT 或可选 +5VIN 供电 | 图 ac6e57f217e9 / 第 1 页 / 网格 C3-C4，J3 HY-2.0_IIC 与 R1/R2 |
| IR1,R3 | IR / 22R 1% | G4 直接驱动的红外发射支路 | 图 ac6e57f217e9 / 第 1 页 / 网格 C2-C3，G4、IR1、R3 |
| LS1,Q5 | Buzzer / SS8050 Y1 | G2 经低端晶体管驱动的 3.3V 蜂鸣器 | 图 ac6e57f217e9 / 第 1 页 / 网格 C1-D2，LS1、Q5、R24/R25、C27、D6/D7 |
| Q2,Q3 | LP3218DT1G | VBAT_IN/+5VIN 到 VBAT_OUT 的电源路径开关 | 图 ac6e57f217e9 / 第 1 页 / 网格 A1-B3，Q2/Q3、D1 与 VBAT_IN/VBAT_OUT |
| Q4 | LN2324DT2AG | HOLD 控制的电源保持 MOSFET，门极带 R23 100K 下拉 | 图 ac6e57f217e9 / 第 1 页 / 网格 B2，Q4、HOLD 与 R23 |
| P1,P2 | Header 9 / Header 9 | 主控两侧九针扩展接口，承载 GPIO、电源、UART、WAKE、EN 和 Boot | 图 ac6e57f217e9 / 第 1 页 / 网格 D1-D3，P2/M1/P1 三组九针映射 |

## 系统结构

### 所提供 Capsule 两页电路架构

两页资源以 M1 STAMP-S3-SMD 为主控，连接电池充电与电源保持、5V/3.3V 转换、RTC8563、BMI270、SPM1423、红外、蜂鸣器、microSD、I2C Grove 和两组九针扩展接口。

- 参数与网络：`controller=M1 STAMP-S3-SMD`；`power=TP4057/SY7088/SY8089`；`rtc=U5 RTC8563`；`imu=U7 BMI270`；`microphone=U9 SPM1423HM4H-B`；`storage=J1 TF-015`；`expansion=P1/P2/J3`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主控、电源、RTC、microSD 与扩展接口完整页; 图 203c49dde3fb / 第 1 页 / SPM1423 与 BMI270 完整页

## 核心器件

### M1 STAMP-S3-SMD 引脚

M1 左侧 pins1-17 依次为 G1、G2、G3、G4、G5、G6、G7、G8/SDA、G9、G10/SCL、GND、G11、+5VIN、G12、G13、G14、G15；右侧 pins28-18 为 +3.3、G46/HOLD、G43/Tx、G42、G44/Rx、G41/MTDI、EN、G40/MTDO、G0/Boot、G39/MTCK、GND，底部 pins29-31 为 D-、D+、PGND。

- 参数与网络：`reference=M1`；`part_number=STAMP-S3-SMD`；`left_pins=1 G1,2 G2,3 G3,4 G4,5 G5,6 G6,7 G7,8 G8/SDA,9 G9,10 G10/SCL,11 GND,12 G11,13 +5VIN,14 G12,15 G13,16 G14,17 G15`；`right_pins=28 +3.3,27 G46/HOLD,26 G43/Tx,25 G42,24 G44/Rx,23 G41/MTDI,22 EN,21 G40/MTDO,20 G0/Boot,19 G39/MTCK,18 GND`；`usb_pads=29 D-,30 D+,31 PGND`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C2-D3，M1 全部引脚

## 电源

### TP4057 电池充电

+5VIN 经 R11 0.8Ω 接 U2 TP4057 VCC pin4，BAT pin3 接 VBAT_IN，PROG pin6 经 R17 2.3K 接地；C15 10uF 为输入去耦，C21 10uF 位于 VBAT_IN。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8R`；`battery=VBAT_IN`；`program_resistor=R17 2.3K`；`input_capacitor=C15 10uF`；`battery_capacitor=C21 10uF`；`battery_header=J2 pin1 VBAT_IN,pin2 GND`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 A1-B1，U2、J2 与充电外围

### +5VIN 与电池电源路径

VBAT_IN 经 Q2 LP3218DT1G 接入中间电源节点，+5VIN 经 D1 SS34 接入同一节点，该节点再经 Q3 LP3218DT1G 输出 VBAT_OUT；C16/C17 各 10uF 分别位于 Q3 前后。

- 参数与网络：`battery_path=VBAT_IN -> Q2 LP3218DT1G`；`usb_path=+5VIN -> D1 SS34`；`output_switch=Q3 LP3218DT1G -> VBAT_OUT`；`capacitors=C16=10uF,C17=10uF`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 A1-B3，VBAT_IN/+5VIN/Q2/D1/Q3/VBAT_OUT

### WAKE 与 HOLD 电源保持网络

S1 按下将 WAKE 接地，WAKE 经 D4 B5819WT 接入 Q3 控制节点并由 D5 对地保护；RTC INT 经 D3 B5819WT 接同一控制节点，G42 经 D15 B5819WT 接 WAKE，HOLD/G46 驱动 Q4 LN2324DT2AG 且由 R23 100K 下拉。

- 参数与网络：`wake_button=S1 WAKE to GND`；`rtc_wake=INT via D3 B5819WT`；`gpio_wake=G42 via D15 B5819WT`；`wake_diode=D4 B5819WT`；`hold_gpio=G46/HOLD`；`hold_switch=Q4 LN2324DT2AG`；`hold_pulldown=R23 100K`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 A2-B3，S1/WAKE/INT/G42/HOLD/Q4 网络

### SY7088 5V 升压

U3 SY7088 从 VBAT_OUT 取电，L4 为 1.5uH，OUT 经 D8 SS34 输出 +5VOUT；反馈分压为 R16 52.3K 与 R18 15K，C18 为 22uF 输出电容。

- 参数与网络：`converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 1.5uH`；`output=+5VOUT via D8 SS34`；`feedback=R16 52.3K,R18 15K`；`output_capacitor=C18 22uF`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 A3-B4，虚线框 U3 SY7088

### SY8089 3.3V 降压

U4 SY8089 从 VBAT_OUT 取电，LX 经 L5 4.7uH 输出 +3.3V；反馈分压为 R27 68K 与 R28 15K，C30 22uF 和 C31 100nF 位于输出端。

- 参数与网络：`converter=U4 SY8089`；`input=VBAT_OUT`；`inductor=L5 4.7uH`；`output=+3.3V`；`feedback=R27 68K,R28 15K`；`output_capacitors=C30 22uF,C31 100nF`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 B3-B4，U4 SY8089 与输出网络

## 接口

### HY2.0 I2C 接口

J3 HY-2.0_IIC pin1/pin2 分别连接 G15/IIC_SCL 和 G13/IIC_SDA，pin3 VCC 默认经 R1 0Ω 接 +5VOUT，R2 标 0Ω/NC 可把 +5VIN 接入同一 VCC，pin4 接 GND。

- 参数与网络：`connector=J3 HY-2.0_IIC`；`pin1=G15/IIC_SCL`；`pin2=G13/IIC_SDA`；`pin3=VCC from +5VOUT via R1 0R`；`alternate_power=+5VIN via R2 0R/NC`；`pin4=GND`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C3-C4，J3、R1/R2 与保护器件

### P1/P2 九针扩展接口

P2 pins1-9 依次为 G1、G3、G5、G7、G9、GND、+5VIN、G13、G15；P1 pins1-9 依次为 +5VOUT、VBAT_IN、WAKE、+3.3V、G43、G44、EN、G0、GND。

- 参数与网络：`p2=1 G1,2 G3,3 G5,4 G7,5 G9,6 GND,7 +5VIN,8 G13,9 G15`；`p1=1 +5VOUT,2 VBAT_IN,3 WAKE,4 +3.3V,5 G43,6 G44,7 EN,8 G0,9 GND`；`uart=G43 Tx,G44 Rx`；`boot=G0`；`wake=WAKE`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 D1-D3，P2 与 P1

## 总线

### RTC8563 I2C 与中断

U5 RTC8563 的 SCL/SDA 连接同名网络，M1 将 SCL/SDA 分别映射为 G10/G8；U5 INT 接 INT 网络并通过 D3 进入唤醒控制，VDD 接 VBAT_IN。

- 参数与网络：`rtc=U5 RTC8563`；`scl=G10/SCL`；`sda=G8/SDA`；`interrupt=INT -> D3 wake network`；`supply=VBAT_IN`；`address=null`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 B1-C2，U5 SCL/SDA/INT 与 M1 G10/G8

## 总线地址

### BMI270 I2C 地址

U7 BMI270 SDO/SA0 由 R7 15K 上拉到 VDDIO；页面注明 SDO=GND 时 0x68、SDO=VDDIO 时 0x69，因此图示配置为 7-bit 地址 0x69。

- 参数与网络：`device=U7 BMI270`；`address_7bit=0x69`；`sdo_sa0=VDDIO via R7 15K`；`alternate=0x68 when SDO=GND`；`mode=I2C`
- 证据：图 203c49dde3fb / 第 1 页 / 网格 B2-C3，SA0/R7 与 SDO 地址注释

## GPIO 与控制信号

### G4 红外发射支路

G4 依次连接 IR1 和 R3 22R/1%，再接 GND。

- 参数与网络：`gpio=G4`；`emitter=IR1`；`series_resistor=R3 22R/1%`；`return=GND`；`driver_transistor=null`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C2-C3，G4/IR1/R3

## 时钟

### RTC 32.768KHz 晶振

Y2 标注 32.768KHz ±20ppm 12.5pF，连接 OSCI/OSCO，C28/C29 各 6.0pF 接地。

- 参数与网络：`reference=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load_annotation=12.5pF`；`capacitors=C28=6.0pF,C29=6.0pF`；`nets=OSCI,OSCO`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C2，Y2/C28/C29

## 复位

### EN 复位按键

S4 是从 EN 到 GND 的常开按键，按下将 M1 EN 拉低。

- 参数与网络：`button=S4 SW-PB`；`net=EN`；`other_terminal=GND`；`active_level=low`；`target=M1 pin22 EN`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C1，S4 EN 到 GND；网格 D2，M1 EN pin22

## 保护电路

### Grove 与 microSD ESD 保护

J3 的 VCC、IIC_SCL、IIC_SDA 分别有 D12/D13/D16 PESDNC2FD3V3B 对地保护，J1 的四条 SPI 信号分别有 D9/D10/D11/D14 同型号保护。

- 参数与网络：`grove=D12,D13,D16 PESDNC2FD3V3B`；`microsd=D9,D10,D11,D14 PESDNC2FD3V3B`；`return=GND`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C3-D4，J3/J1 保护二极管

## 存储

### microSD SPI 映射

J1 TF-015 的 CS、MOSI、CLK、MISO 分别经 R10/R20/R21/R22 各 33Ω 连接 G11/G12/G14/G39，VCC 接 +3.3V；四条信号各有 PESDNC2FD3V3B 对地保护。

- 参数与网络：`slot=J1 TF-015`；`cs=G11 via R10 33R`；`mosi=G12 via R20 33R`；`clock=G14 via R21 33R`；`miso=G39 via R22 33R`；`supply=+3.3V`；`esd=D9/D10/D11/D14 PESDNC2FD3V3B`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 D3-D4，J1 与 SPI/ESD 网络

## 音频

### SPM1423 数字麦克风

U9 SPM1423HM4H-B 由 +3.3V 供电，CLK pin4 接 G40，DAT pin5 接 G41，SELECT pin2 接 GND；C9 100nF/25V 为电源去耦。

- 参数与网络：`microphone=U9 SPM1423HM4H-B`；`clock=G40`；`data=G41`；`select=GND`；`supply=+3.3V`；`decoupling=C9 100nF/25V`
- 证据：图 203c49dde3fb / 第 1 页 / 网格 B1-C2，U9 与 C9

### G2 蜂鸣器驱动

+3.3V 经 R24 10Ω 和 LS1 蜂鸣器接 Q5 SS8050 Y1 集电极，Q5 发射极接地；G2 经 R25 470Ω、C27 10uF 驱动基极，D6 跨接蜂鸣器支路，D7 从基极节点接地。

- 参数与网络：`gpio=G2`；`buzzer=LS1`；`driver=Q5 SS8050 Y1`；`supply_path=+3.3V -> R24 10R -> LS1`；`base_path=G2 -> R25 470R -> C27 10uF`；`diodes=D6/D7 1N4148WT`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 C1-D2，Buzzer 区

## 传感器

### BMI270 I2C 与电源连接

U7 SDA pin14、SCL pin13 分别连接 SDA/SCL 并由 R8/R9 各 15K 上拉到 VDDIO；M1 映射 SDA=G8、SCL=G10。VDD、VDDIO、CSB 接 3.3V，INT1/INT2 和辅助接口未连接。

- 参数与网络：`sda=G8/SDA`；`scl=G10/SCL`；`pullups=R8/R9 15K to VDDIO`；`vdd=+3.3V`；`vddio=+3.3V`；`csb=VDDIO`；`interrupts=INT1/INT2 NC`；`aux=ASDX/ASCX/OSDO/OCSB NC`
- 证据：图 203c49dde3fb / 第 1 页 / U7 全部引脚、R7-R9、VDDIO 与 +3.3V 连接; 图 ac6e57f217e9 / 第 1 页 / M1 G8/SDA 与 G10/SCL

## 模拟电路

### VBAT_IN 分压采样

VBAT_IN 通过 R4 100K 与 R5 100K 分压到 G6，C1 100nF 从 G6 接地。

- 参数与网络：`input=VBAT_IN`；`adc_gpio=G6`；`upper_resistor=R4 100K`；`lower_resistor=R5 100K`；`filter_capacitor=C1 100nF`
- 证据：图 ac6e57f217e9 / 第 1 页 / 网格 B1-C1，VBAT_IN/R4/R5/C1/G6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 所提供 Capsule 两页电路架构 | `controller=M1 STAMP-S3-SMD`；`power=TP4057/SY7088/SY8089`；`rtc=U5 RTC8563`；`imu=U7 BMI270`；`microphone=U9 SPM1423HM4H-B`；`storage=J1 TF-015`；`expansion=P1/P2/J3` |
| 核心器件 | M1 STAMP-S3-SMD 引脚 | `reference=M1`；`part_number=STAMP-S3-SMD`；`left_pins=1 G1,2 G2,3 G3,4 G4,5 G5,6 G6,7 G7,8 G8/SDA,9 G9,10 G10/SCL,11 GND,12 G11,13 +5VIN,14 G12,15 G13,16 G14,17 G15`；`right_pins=28 +3.3,27 G46/HOLD,26 G43/Tx,25 G42,24 G44/Rx,23 G41/MTDI,22 EN,21 G40/MTDO,20 G0/Boot,19 G39/MTCK,18 GND`；`usb_pads=29 D-,30 D+,31 PGND` |
| 电源 | TP4057 电池充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8R`；`battery=VBAT_IN`；`program_resistor=R17 2.3K`；`input_capacitor=C15 10uF`；`battery_capacitor=C21 10uF`；`battery_header=J2 pin1 VBAT_IN,pin2 GND` |
| 电源 | +5VIN 与电池电源路径 | `battery_path=VBAT_IN -> Q2 LP3218DT1G`；`usb_path=+5VIN -> D1 SS34`；`output_switch=Q3 LP3218DT1G -> VBAT_OUT`；`capacitors=C16=10uF,C17=10uF` |
| 电源 | WAKE 与 HOLD 电源保持网络 | `wake_button=S1 WAKE to GND`；`rtc_wake=INT via D3 B5819WT`；`gpio_wake=G42 via D15 B5819WT`；`wake_diode=D4 B5819WT`；`hold_gpio=G46/HOLD`；`hold_switch=Q4 LN2324DT2AG`；`hold_pulldown=R23 100K` |
| 电源 | SY7088 5V 升压 | `converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 1.5uH`；`output=+5VOUT via D8 SS34`；`feedback=R16 52.3K,R18 15K`；`output_capacitor=C18 22uF` |
| 电源 | SY8089 3.3V 降压 | `converter=U4 SY8089`；`input=VBAT_OUT`；`inductor=L5 4.7uH`；`output=+3.3V`；`feedback=R27 68K,R28 15K`；`output_capacitors=C30 22uF,C31 100nF` |
| 模拟电路 | VBAT_IN 分压采样 | `input=VBAT_IN`；`adc_gpio=G6`；`upper_resistor=R4 100K`；`lower_resistor=R5 100K`；`filter_capacitor=C1 100nF` |
| 复位 | EN 复位按键 | `button=S4 SW-PB`；`net=EN`；`other_terminal=GND`；`active_level=low`；`target=M1 pin22 EN` |
| 总线 | RTC8563 I2C 与中断 | `rtc=U5 RTC8563`；`scl=G10/SCL`；`sda=G8/SDA`；`interrupt=INT -> D3 wake network`；`supply=VBAT_IN`；`address=null` |
| 时钟 | RTC 32.768KHz 晶振 | `reference=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load_annotation=12.5pF`；`capacitors=C28=6.0pF,C29=6.0pF`；`nets=OSCI,OSCO` |
| 总线地址 | BMI270 I2C 地址 | `device=U7 BMI270`；`address_7bit=0x69`；`sdo_sa0=VDDIO via R7 15K`；`alternate=0x68 when SDO=GND`；`mode=I2C` |
| 传感器 | BMI270 I2C 与电源连接 | `sda=G8/SDA`；`scl=G10/SCL`；`pullups=R8/R9 15K to VDDIO`；`vdd=+3.3V`；`vddio=+3.3V`；`csb=VDDIO`；`interrupts=INT1/INT2 NC`；`aux=ASDX/ASCX/OSDO/OCSB NC` |
| 音频 | SPM1423 数字麦克风 | `microphone=U9 SPM1423HM4H-B`；`clock=G40`；`data=G41`；`select=GND`；`supply=+3.3V`；`decoupling=C9 100nF/25V` |
| GPIO 与控制信号 | G4 红外发射支路 | `gpio=G4`；`emitter=IR1`；`series_resistor=R3 22R/1%`；`return=GND`；`driver_transistor=null` |
| 音频 | G2 蜂鸣器驱动 | `gpio=G2`；`buzzer=LS1`；`driver=Q5 SS8050 Y1`；`supply_path=+3.3V -> R24 10R -> LS1`；`base_path=G2 -> R25 470R -> C27 10uF`；`diodes=D6/D7 1N4148WT` |
| 存储 | microSD SPI 映射 | `slot=J1 TF-015`；`cs=G11 via R10 33R`；`mosi=G12 via R20 33R`；`clock=G14 via R21 33R`；`miso=G39 via R22 33R`；`supply=+3.3V`；`esd=D9/D10/D11/D14 PESDNC2FD3V3B` |
| 接口 | HY2.0 I2C 接口 | `connector=J3 HY-2.0_IIC`；`pin1=G15/IIC_SCL`；`pin2=G13/IIC_SDA`；`pin3=VCC from +5VOUT via R1 0R`；`alternate_power=+5VIN via R2 0R/NC`；`pin4=GND` |
| 接口 | P1/P2 九针扩展接口 | `p2=1 G1,2 G3,3 G5,4 G7,5 G9,6 GND,7 +5VIN,8 G13,9 G15`；`p1=1 +5VOUT,2 VBAT_IN,3 WAKE,4 +3.3V,5 G43,6 G44,7 EN,8 G0,9 GND`；`uart=G43 Tx,G44 Rx`；`boot=G0`；`wake=WAKE` |
| 保护电路 | Grove 与 microSD ESD 保护 | `grove=D12,D13,D16 PESDNC2FD3V3B`；`microsd=D9,D10,D11,D14 PESDNC2FD3V3B`；`return=GND` |
| 系统结构 | Capsule v1.1 主控版本 | `documented_controller=Stamp-S3A`；`schematic_controller=STAMP-S3-SMD`；`product_revision_on_schematic=null`；`sku_on_schematic=null` |
| 内存与 Flash | v1.1 ESP32-S3FN8 与 8MB Flash | `documented_soc=ESP32-S3FN8`；`documented_flash=8MB`；`schematic_module=STAMP-S3-SMD`；`internal_soc=null`；`flash_part=null`；`flash_bus=null` |
| 总线地址 | RTC 型号与 0x51 地址 | `documented_part=BM8563`；`documented_address=0x51`；`schematic_part=RTC8563`；`schematic_address=null`；`current_part=null` |
| 电源 | 250mAh 电池与工作/休眠电流 | `documented_capacity=250mAh`；`documented_sleep=DC 4.2V@35uA`；`documented_work=DC 4.2V@144mA`；`battery_part=null`；`measurement_conditions=null` |
| 射频 | Stamp-S3A 天线优化 | `documented=Stamp-S3A optimized antenna`；`antenna_part=null`；`matching_network=null`；`layout=null`；`test_result=null` |
| GPIO 与控制信号 | 红外遥控距离与角度 | `documented_180deg=330cm`；`documented_90deg=48cm`；`documented_45deg=134cm`；`schematic=G4 -> IR1 -> R3 22R -> GND`；`ir_part=null`；`drive_current=null`；`test_conditions=null` |

## 待确认事项

- `system.v11-controller-version`：正文称 Capsule v1.1 已由 Stamp-S3 升级为 Stamp-S3A，但所提供主控页 M1 仍标 STAMP-S3-SMD，页面没有 v1.1、K129-V11 或 Stamp-S3A 标识，当前版本对应关系需确认。（证据：图 ac6e57f217e9 / 第 1 页 / M1 STAMP-S3-SMD 标注，页面无 v1.1/K129-V11 标题栏）
- `memory.v11-soc-flash`：正文规格列 ESP32-S3FN8 和 8MB Flash；原理图只给出封装级 M1 STAMP-S3-SMD，没有模组内部 SoC/Flash 器件、容量或总线，当前 v1.1 配置需确认。（证据：图 ac6e57f217e9 / 第 1 页 / M1 模组符号，无内部 SoC/Flash）
- `address.v11-rtc-model`：正文规格与管脚表写 BM8563(0x51)，原理图 U5 标 RTC8563 且未标 I2C 地址；两种名称及 v1.1 当前 7-bit 地址需由正式 BOM 或 datasheet 确认。（证据：图 ac6e57f217e9 / 第 1 页 / U5 RTC8563、SCL/SDA，无地址标注）
- `power.v11-battery-current`：正文列内置 250mAh 电池、DC 4.2V@35uA 休眠电流和 DC 4.2V@144mA 工作电流；原理图只显示 VBAT_IN/J2/TP4057 与各电源轨，没有电池料号、容量或电流测试条件。（证据：图 ac6e57f217e9 / 第 1 页 / U2/J2/VBAT_IN 电源网络，无电池器件和测量条件）
- `rf.v11-antenna-optimization`：正文产品对比称 v1.1 使用 Stamp-S3A 并优化天线设计；两页原理图未显示射频天线、匹配网络、布局或测试结果，无法确认当前 v1.1 的天线实现。（证据：图 ac6e57f217e9 / 第 1 页 / M1 模组符号与整页，无 RF/天线网络; 图 203c49dde3fb / 第 1 页 / 传感器页，无 RF/天线网络）
- `gpio.v11-ir-distance`：正文列出 180°/90°/45° 条件下 330cm/48cm/134cm 红外距离；原理图只确认 G4、IR1 和 R3 22Ω支路，没有 IR 料号、驱动电流、光学角度或测试条件。（证据：图 ac6e57f217e9 / 第 1 页 / G4/IR1/R3 支路，无光学或距离参数）
- `review.controller-version`：请提供 Capsule v1.1/K129-V11 当前正式原理图或 BOM，确认主控已升级为 Stamp-S3A。；原因：页面 M1 仍标 STAMP-S3-SMD，且无 v1.1/SKU 标识。
- `review.soc-flash`：请确认 Stamp-S3A 内部 ESP32-S3FN8、8MB Flash 的实际料号和存储配置。；原因：原理图没有模组内部器件。
- `review.rtc-model`：请由 v1.1 BOM 确认 RTC 是 BM8563 还是 RTC8563，并确认 7-bit 地址 0x51。；原因：正文与图中型号名称不同，图中未标地址。
- `review.battery-current`：请确认 250mAh 电池料号、连接器、充电参数及 35uA/144mA 的测试条件。；原因：图中只有 VBAT 电源网络，没有容量与整机电流证据。
- `review.antenna`：请确认 Stamp-S3A 天线料号、匹配、PCB 布局及优化前后测试数据。；原因：两页未显示 RF 实现。
- `review.ir-distance`：请确认 IR1 料号、驱动电流、光学角度以及三组遥控距离的测试方法。；原因：原理图只有 G4/IR1/22Ω电气支路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ac6e57f217e95acd75ddb1dff39ab71ed9158a2a2bb9c953514d14b7499a8f11` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_01.png` |
| 2 | 1 | `203c49dde3fb6a1b938b43d2ce59fb2be4469ce919856555056e48c1e7afb471` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_02.png` |

---

源文档：`zh_CN/core/Capsule_v1.1.md`

源文档 SHA-256：`e861216c70ba04950d9a35ffad7e583cec2a4b9ad5a1f72fe8e5b4551b8566b7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
