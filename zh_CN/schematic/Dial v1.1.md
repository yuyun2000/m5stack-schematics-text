# Dial v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Dial v1.1 |
| SKU | K130-V11 |
| 产品 ID | `dial-v1-1-2c1d18834bdd` |
| 源文档 | `zh_CN/core/M5Dial V1.1.md` |

## 概述

Dial v1.1 原理图以 M1 STAMP-S3-DIP-1.27 为主控模组接口，连接 WS1850S RFID、RTC8563、圆形 LCD/触摸模组、EC30 编码器、蜂鸣器和两路 HY2.0 扩展口。RFID、RTC 与触摸共享 TP_SDA/TP_SCL，总线由 GPIO11/GPIO12 控制；LCD 使用 GPIO4-GPIO9 的单向 SPI/控制信号。电源支持外部 +VIN 与电池路径，依次由 ME3116、TP4057、电源锁存、SY7088 和 SY8089 形成 +5VIN、VBAT_OUT、+5VOUT 与 +3.3V。

## 检索关键词

`Dial v1.1`、`K130-V11`、`STAMP-S3-DIP-1.27`、`Stamp-S3A`、`ESP32-S3FN8`、`WS1850S`、`RTC8563`、`TP4057`、`ME3116AM6G`、`SY7088`、`SY8089`、`EC30-16bit`、`OK-24M024-04`、`GC9A01`、`FT3267`、`RC522_SDA`、`RC522_SCL`、`RC522_INT`、`TP_SDA`、`TP_SCL`、`TP_INT`、`LCD_MOSI`、`LCD_SCK`、`LCD_CS`、`LCD_RESET`、`LCD_BL`、`VBAT_IN`、`VBAT_OUT`、`+5VIN`、`+5VOUT`、`+3.3V`、`HOLD GPIO46`、`WAKE GPIO42`、`PORT.A`、`PORT.B`、`HY2.0-4P`、`27.12MHz`、`32.768KHz`、`ANT_Hole`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-DIP-1.27 | 主控模组接口，向 LCD、触摸、RFID、RTC、编码器、蜂鸣器和扩展口分配 GPIO | 图 0528f589274c / 第 1 页 / 第2图 C2-D2，M1 STAMP-S3-DIP-1.27，G1-G15 与 G39-G46 |
| U1 | WS1850S | RFID/NFC 前端，使用 SDA/SCL/IRQ/NRSTPD 数字接口并驱动天线匹配网络 | 图 1d8705f9d82d / 第 1 页 / 第1图 A2-B2，U1 WS1850S，RX/TX1/TX2、RC522_SDA/SCL/IRQ、Y1 |
| U2 | TP4057 | 电池充电控制器，从 +5VIN 为 VBAT_IN 充电 | 图 0528f589274c / 第 1 页 / 第2图 A1-B1，U2 TP4057、R11 0.8Ω、R17 10KΩ、JP1/JP2 |
| U3 | SY7088 | 从 VBAT_OUT 生成 +5VOUT 的升压转换器 | 图 0528f589274c / 第 1 页 / 第2图 A3-B4 虚线框，U3 SY7088、L4 1.5uH、R16/R18、D8 |
| U4 | SY8089 | 从 VBAT_OUT 生成 +3.3V 的降压转换器 | 图 0528f589274c / 第 1 页 / 第2图 B3-C3，U4 SY8089、L5 4.7uH、R27/R28 |
| U5 | RTC8563 | 电池供电实时时钟，通过 TP_SDA/TP_SCL 连接主控并输出 INT | 图 0528f589274c / 第 1 页 / 第2图 C2-C3，U5 RTC8563、Y2 32.768KHz、INT/TP_SDA/TP_SCL |
| U6 | CN809J | +5VIN 供电复位/电源控制监控器，RESET 输出接电源选择网络 | 图 0528f589274c / 第 1 页 / 第2图 B1，U6 CN809J，VCC +5VIN、RESET、R19 |
| U7 | ME3116AM6G | 外部 +VIN 至 +5VIN 的降压转换器 | 图 0528f589274c / 第 1 页 / 第2图 A2-A3，U7 ME3116AM6G、L6 10uH、R33/R34、D9/D11 |
| BTB1 | OK-24M024-04 | 24 针 LCD 与触摸模组连接器，承载背光、SPI、触摸 I2C、复位和电源 | 图 1d8705f9d82d / 第 1 页 / 第1图 C4-D4，BTB1 OK-24M024-04，pins 1-24 |
| J5 | EC30-16bit | 增量旋转编码器，A/B 相接 GPIO41/GPIO40，公共端接地 | 图 0528f589274c / 第 1 页 / 第2图 C3-D3，J5 EC30-16bit、A/B、R21/R22、C22/C23 |
| L2 | ANT_Hole | WS1850S RFID 天线线圈/天线孔，经 TX1/TX2 差分匹配网络连接 | 图 1d8705f9d82d / 第 1 页 / 第1图 B3，L2 ANT_Hole 与 R4/R5、C8/C11/C13/C14 |
| LS1/Q5 | Buzzer/SS8050 Y1 | GPIO3 beep 控制的晶体管低边蜂鸣器驱动 | 图 0528f589274c / 第 1 页 / 第2图 C1-D1，LS1 Buzzer、Q5 SS8050 Y1、D6/D7、R24/R25 |
| Q2/Q3 | LP3218DT1G | VBAT_IN、+5VIN 与 VBAT_OUT 之间的电源选择/隔离开关 | 图 0528f589274c / 第 1 页 / 第2图 A1-B3，Q2/Q3 LP3218DT1G、D1、VBAT_IN/VBAT_OUT |
| Q1/Q4 | LN2324DT2AG | Q1 控制 LCD 背光阴极，Q4 由 HOLD 控制电源锁存节点 | 图 1d8705f9d82d / 第 1 页 / 第1图 C3-C4，Q1 LN2324DT2AG、LCD_BL、LEDK; 图 0528f589274c / 第 1 页 / 第2图 B2，Q4 LN2324DT2AG、HOLD |
| P5 | Header 2 | 外部直流输入连接器，1 脚经 D13 接 +VIN，2 脚接 GND | 图 0528f589274c / 第 1 页 / 第2图 A1，P5 Header 2、D13 B5819W SL、+VIN |
| P6 | Header 2 | 两针电池连接器，1 脚 VBAT_IN、2 脚 GND | 图 0528f589274c / 第 1 页 / 第2图 B1，P6 Header 2，VBAT_IN/GND |
| J2 | HY-2.0_IO | PORT.B GPIO 扩展口，提供 GI、GO、+5VOUT 与 GND | 图 0528f589274c / 第 1 页 / 第2图 D4，J2 HY-2.0_IO pins 1-4 |
| J3 | HY-2.0_IIC | PORT.A I2C 扩展口，提供 SCL、SDA、+5VOUT 与 GND | 图 0528f589274c / 第 1 页 / 第2图 C4-D4，J3 HY-2.0_IIC pins 1-4 |
| P1/P3 | 6X2@2.54 排母/排针 | LCD/触摸信号的 12 针板间连接器对 | 图 1d8705f9d82d / 第 1 页 / 第1图 D4，P1 6X2@2.54 排母; 图 0528f589274c / 第 1 页 / 第2图 D3-D4，P3 6X2@2.54 排针 |
| S1/S4 | SW-PB | WAKE 唤醒按钮与主控 EN 复位按钮 | 图 0528f589274c / 第 1 页 / 第2图 B2 S1 SW-PB 与 D4/D10；D2 S4 SW-PB 接 EN/GND |
| D12/D5 | SD36/PESDNC2FD3V3B | 外部 +VIN 与 WAKE 按键节点的浪涌/ESD 保护 | 图 0528f589274c / 第 1 页 / 第2图 A2 D12 SD36 接 +VIN；B2 D5 PESDNC2FD3V3B 接 WAKE/S1 |

## 系统结构

### Dial v1.1 系统架构

M1 主控模组连接 WS1850S RFID、RTC8563、LCD/触摸、EC30 编码器、蜂鸣器和两路 HY2.0 接口；外部直流与电池经充电、选择、5V/3.3V 转换和 HOLD/WAKE 锁存电路供电。

- 参数与网络：`controller_interface=M1 STAMP-S3-DIP-1.27`；`rfid=U1 WS1850S`；`rtc=U5 RTC8563`；`display=BTB1 OK-24M024-04`；`encoder=J5 EC30-16bit`；`power=U7 ME3116AM6G + U2 TP4057 + U3 SY7088 + U4 SY8089`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图完整页，RFID 与 LCD/触摸分区; 图 0528f589274c / 第 1 页 / 第2图完整页，主控接口、电源、RTC、编码器和扩展口

## 核心器件

### M1 主控模组

原理图将主控模组接口标为 M1 STAMP-S3-DIP-1.27，并展示 G1-G15、G39-G46、EN、3V3、5V 与 GND 引脚。

- 参数与网络：`reference=M1`；`schematic_part=STAMP-S3-DIP-1.27`；`power=+3.3V / M5V`；`reset=EN`；`boot=G0/Boot`
- 证据：图 0528f589274c / 第 1 页 / 第2图 C2-D2，M1 STAMP-S3-DIP-1.27

### U1 WS1850S

U1 WS1850S 以 +3.3V 供电，RC522_SDA、RC522_SCL、RC522_IRQ 和 NRSTPD 接数字控制网络，TX1/TX2/RX 接天线匹配网络。

- 参数与网络：`reference=U1`；`part_number=WS1850S`；`supply=+3.3V`；`digital=RC522_SDA/RC522_SCL/RC522_IRQ/NRSTPD`；`rf=TX1/TX2/RX`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 A2-B2 U1 WS1850S

## 电源

### P5 外部直流输入

P5 1 脚经 D13 B5819W SL 串联进入 +VIN，2 脚接 GND；D12 SD36 从 +VIN 对地钳位，C34 10uF/35V 与 C35 100nF 滤波。

- 参数与网络：`connector=P5 Header 2`；`positive=pin 1 -> D13 -> +VIN`；`negative=pin 2 -> GND`；`series_diode=D13 B5819W SL`；`tvs=D12 SD36`；`capacitors=C34 10uF/35V; C35 100nF`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A1-A2，P5、D13、D12、C34/C35、+VIN

### U7 +5VIN 转换

U7 ME3116AM6G 以 +VIN 为输入，经 L6 10uH、D9/D11 B5819W SL 与 R33 56KΩ/R34 10KΩ 反馈生成 +5VIN。

- 参数与网络：`reference=U7`；`input=+VIN`；`output=+5VIN`；`inductor=L6 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R33 56KΩ; R34 10KΩ`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A2-A3，U7 ME3116AM6G 至 +5VIN

### U2 TP4057 充电

U2 TP4057 的 VCC 经 R11 0.8Ω 接 +5VIN，BAT 经 JP1 接 VBAT_IN，PROG 经 R17 10KΩ 与 JP2 接地。

- 参数与网络：`reference=U2`；`part_number=TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN via JP1`；`program=R17 10KΩ via JP2`；`status=CHRG/STDBY`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A1-B1，U2 TP4057

### P6 电池接口

P6 Header 2 的 1 脚接 VBAT_IN、2 脚接 GND；C21 10uF 跨接 VBAT_IN 与 GND。

- 参数与网络：`reference=P6`；`pin_1=VBAT_IN`；`pin_2=GND`；`capacitor=C21 10uF`
- 证据：图 0528f589274c / 第 1 页 / 第2图 B1，P6、VBAT_IN、C21

### 电池与 +5VIN 电源选择

VBAT_IN 经 Q2 LP3218DT1G 进入中间电源节点，+5VIN 经 D1 SS34 汇入同一节点，再经 Q3 LP3218DT1G 输出 VBAT_OUT。

- 参数与网络：`battery_path=VBAT_IN -> Q2 LP3218DT1G`；`external_path=+5VIN -> D1 SS34`；`output_switch=Q3 LP3218DT1G`；`output=VBAT_OUT`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A1-B3，Q2/D1/Q3 与 VBAT_IN/VBAT_OUT

### +5VOUT 电源轨

U3 SY7088 从 VBAT_OUT 经 R12 0Ω 输入，配合 L4 1.5uH 与 R16 150KΩ/R18 47KΩ 反馈升压，输出经 D8 SS34 标为 +5VOUT。

- 参数与网络：`reference=U3`；`input=VBAT_OUT`；`output=+5VOUT`；`inductor=L4 1.5uH`；`feedback=R16 150KΩ; R18 47KΩ`；`output_diode=D8 SS34`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A3-B4 虚线框 U3 SY7088

### +3.3V 电源轨

U4 SY8089 以 VBAT_OUT 为输入，经 L5 4.7uH 和 R27 68KΩ/R28 15KΩ 反馈生成 +3.3V，EN 由 3V3EN 网络控制。

- 参数与网络：`reference=U4`；`input=VBAT_OUT`；`output=+3.3V`；`enable=3V3EN via R26 50KΩ`；`inductor=L5 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ`
- 证据：图 0528f589274c / 第 1 页 / 第2图 B3-C3，U4 SY8089

### HOLD/WAKE 电源锁存

M1 GPIO46 输出 HOLD 控制 Q4 LN2324DT2AG；GPIO42 接 WAKE，S1、D4、D10 与 RTC INT/D3 汇入锁存节点，用于按键或 RTC 唤醒。

- 参数与网络：`hold=GPIO46 -> HOLD -> Q4`；`wake=GPIO42 -> WAKE`；`button=S1 SW-PB`；`rtc=U5 INT -> D3`；`diodes=D3/D4/D10 B5819WT`
- 证据：图 0528f589274c / 第 1 页 / 第2图 B2 HOLD/WAKE/Q4/S1/D3/D4/D10 与 D2 M1 GPIO42/GPIO46

## 接口

### J3 PORT.A

J3 HY-2.0_IIC 的 1 脚 SCL 接 M1 GPIO15，2 脚 SDA 接 GPIO13，3 脚 +5VOUT，4 脚 GND。

- 参数与网络：`reference=J3`；`pin_1=SCL / GPIO15`；`pin_2=SDA / GPIO13`；`pin_3=+5VOUT`；`pin_4=GND`；`bus=external I2C`；`signal_level=+3.3V logic`
- 证据：图 0528f589274c / 第 1 页 / 第2图 D2 M1 GPIO13/GPIO15 与 D4 J3 HY-2.0_IIC

### J2 PORT.B

J2 HY-2.0_IO 的 1 脚 GI 接 M1 GPIO1，2 脚 GO 接 GPIO2，3 脚 +5VOUT，4 脚 GND。

- 参数与网络：`reference=J2`；`pin_1=GI / GPIO1`；`pin_2=GO / GPIO2`；`pin_3=+5VOUT`；`pin_4=GND`；`signal_direction=GPIO configurable`；`signal_level=+3.3V logic`
- 证据：图 0528f589274c / 第 1 页 / 第2图 D2 M1 GI/GO 与 D4 J2 HY-2.0_IO

### P1/P3 显示板间连接

P1 排母与 P3 排针按同一 12 针信号组连接 GND、+3.3V、LCD_BL/RS/MOSI/SCK/CS/RESET、RC522_INT、TP_SDA/SCL/INT。

- 参数与网络：`connectors=P1/P3 6X2@2.54`；`signals=LCD_BL, LCD_RS, LCD_MOSI, LCD_SCK, LCD_CS, LCD_RESET, RC522_INT, TP_SDA, TP_SCL, TP_INT`；`power=+3.3V`；`ground=GND`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 D4 P1 6X2@2.54 排母; 图 0528f589274c / 第 1 页 / 第2图 D3-D4 P3 6X2@2.54 排针

## 总线

### RTC、触摸与 RFID 共享 I2C

M1 GPIO11 接 TP_SDA、GPIO12 接 TP_SCL；RTC8563 与触摸连接器直接使用 TP_SDA/TP_SCL，WS1850S 的 RC522_SDA/RC522_SCL 经 R9/R8 0Ω 接入同一总线。

- 参数与网络：`controller=M1`；`sda=GPIO11 / TP_SDA`；`scl=GPIO12 / TP_SCL`；`rtc=U5 RTC8563`；`touch=BTB1 pins 19/20`；`rfid=U1 WS1850S via R9/R8 0Ω`；`logic_level=+3.3V`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 C2-C4，R8/R9 0Ω 与 BTB1 TP_SCL/TP_SDA; 图 0528f589274c / 第 1 页 / 第2图 C2-D2，U5 TP_SDA/TP_SCL 与 M1 GPIO11/GPIO12

### LCD SPI 总线

M1 GPIO5/GPIO6/GPIO7 分别连接 LCD_MOSI/LCD_SCK/LCD_CS，GPIO4 为 LCD_RS；BTB1 的 SDO/NC 未接出，图中无 LCD MISO。

- 参数与网络：`controller=M1`；`mosi=GPIO5 -> LCD_MOSI -> BTB1-6`；`sck=GPIO6 -> LCD_SCK -> BTB1-8`；`cs=GPIO7 -> LCD_CS -> BTB1-9`；`dc=GPIO4 -> LCD_RS -> BTB1-5`；`miso=null`；`direction=MCU to LCD`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 C4-D4 BTB1 pins 5-9 与 P1; 图 0528f589274c / 第 1 页 / 第2图 C2-D2 M1 GPIO4-GPIO7

## 总线地址

### I2C 设备地址

两张原理图未标注 RTC8563、WS1850S 或触摸控制器的数值 I2C 地址。

- 参数与网络：`bus=TP_SDA/TP_SCL`；`devices=U5 RTC8563; U1 WS1850S; BTB1 touch`；`address_visible=false`；`addresses=null`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 U1 与 BTB1，未见地址标注; 图 0528f589274c / 第 1 页 / 第2图 U5 RTC8563，未见地址标注

## GPIO 与控制信号

### 显示与触摸控制 GPIO

GPIO8 驱动 LCD_RESET 并经 R7 0Ω 同时连接 WS1850S NRSTPD 和触摸 TP_RST；GPIO9 驱动 LCD_BL，GPIO14 接 TP_INT。

- 参数与网络：`reset=GPIO8 -> LCD_RESET -> BTB1-10/18; R7 0Ω -> NRSTPD`；`backlight=GPIO9 -> LCD_BL -> Q1`；`touch_interrupt=GPIO14 <- TP_INT`；`rfid_interrupt=GPIO10 <- RC522_INT`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 C2-C4，R7、Q1、BTB1 RESET/TP_RST/TP_INT; 图 0528f589274c / 第 1 页 / 第2图 M1 GPIO8/GPIO9/GPIO10/GPIO14

## 时钟

### WS1850S 参考时钟

U1 OSCIN/OSCOUT 连接 Y1 27.12MHz 晶振，两端各以 C6/C9 15pF 接地。

- 参数与网络：`device=U1 WS1850S`；`crystal=Y1`；`frequency=27.12MHz`；`load_caps=C6/C9 15pF`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 B1-B2，Y1 27.12MHz、C6/C9、U1 OSCIN/OSCOUT

### RTC8563 低速时钟

U5 OSCI/OSCO 连接 Y2 32.768KHz±20ppm、12.5pF 晶振，C28/C29 各 6.0pF 接地。

- 参数与网络：`rtc=U5 RTC8563`；`crystal=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load=12.5pF`；`capacitors=C28/C29 6.0pF`
- 证据：图 0528f589274c / 第 1 页 / 第2图 C1-C2，Y2、C28/C29 与 U5 OSCI/OSCO

## 复位

### 主控 EN 与 BOOT

M1 EN 引出到 P4 并由 S4 SW-PB 按下接地复位；M1 G0/Boot 同样在 P4 区域引出。

- 参数与网络：`reset_pin=M1 EN`；`reset_switch=S4 SW-PB to GND`；`boot_pin=M1 G0/Boot`；`connector=P4 Header 11`
- 证据：图 0528f589274c / 第 1 页 / 第2图 D2，M1 EN/G0/Boot、P4、S4

## 保护电路

### 输入和按键保护

D12 SD36 对 +VIN 提供对地钳位，D13 B5819W SL 串联在 P5 正输入；D5 PESDNC2FD3V3B 跨接 WAKE/S1 节点与 GND。

- 参数与网络：`input_tvs=D12 SD36`；`input_series_diode=D13 B5819W SL`；`wake_esd=D5 PESDNC2FD3V3B`；`protected_nets=+VIN; WAKE/S1`
- 证据：图 0528f589274c / 第 1 页 / 第2图 A1-A2 D12/D13；B2 D5

## 关键网络

### RTC INT 唤醒路径

U5 RTC8563 的 INT 接公共 INT 网络，该网络经 D3 B5819WT 接入 Q3/Q4 电源锁存节点。

- 参数与网络：`source=U5 INT`；`net=INT`；`diode=D3 B5819WT`；`destination=Q3/Q4 latch node`
- 证据：图 0528f589274c / 第 1 页 / 第2图 B2 INT/D3 与 C2 U5 INT

## 音频

### 蜂鸣器驱动

M1 GPIO3 的 beep 信号经 R25 470Ω、C27 10uF 驱动 Q5 SS8050 Y1，LS1 Buzzer 由 +3.3V 经 R24 10Ω 供电，并带 D6 1N4148 续流支路。

- 参数与网络：`gpio=GPIO3 / beep`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`drive=R25 470Ω + C27 10uF`；`diode=D6 1N4148`
- 证据：图 0528f589274c / 第 1 页 / 第2图 C1-D1 Buzzer 区与 M1 GPIO3

## 传感器

### J5 旋转编码器

J5 EC30-16bit 的 A 相接 GPIO41、B 相接 GPIO40，A/B 各以 10KΩ 上拉至 +3.3V 并以 100nF 对地滤波，公共端 C 接 GND。

- 参数与网络：`reference=J5`；`part_number=EC30-16bit`；`phase_a=A -> GPIO41`；`phase_b=B -> GPIO40`；`pullups=R21/R22 10KΩ`；`filters=C22/C23 100nF`；`common=GND`；`direction=input`
- 证据：图 0528f589274c / 第 1 页 / 第2图 C3-D3 J5、R21/R22、C22/C23 与 M1 A/B

## 射频

### RFID 天线匹配

WS1850S TX1/TX2 分别经 L1/L3 1uH、C8/C14 47pF、C10/C12 120pF、C11/C13 390pF 和 R4/R5 1.2Ω 驱动 L2 ANT_Hole；RX 经 R2/C7/R3 网络取样。

- 参数与网络：`antenna=L2 ANT_Hole`；`tx_inductors=L1/L3 1uH`；`series_caps=C8/C14 47pF`；`shunt_caps=C10/C12 120pF; C11/C13 390pF`；`series_resistors=R4/R5 1.2Ω`；`rx_network=R2 1KΩ; C7 1nF; R3 1.5KΩ`
- 证据：图 1d8705f9d82d / 第 1 页 / 第1图 B2-B3，U1 RX/TX1/TX2 至 L2 ANT_Hole

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Dial v1.1 系统架构 | `controller_interface=M1 STAMP-S3-DIP-1.27`；`rfid=U1 WS1850S`；`rtc=U5 RTC8563`；`display=BTB1 OK-24M024-04`；`encoder=J5 EC30-16bit`；`power=U7 ME3116AM6G + U2 TP4057 + U3 SY7088 + U4 SY8089` |
| 核心器件 | M1 主控模组 | `reference=M1`；`schematic_part=STAMP-S3-DIP-1.27`；`power=+3.3V / M5V`；`reset=EN`；`boot=G0/Boot` |
| 核心器件 | v1.1 与 Stamp-S3A 对应关系 | `product_version=Dial v1.1`；`documented_module=Stamp-S3A`；`documented_soc=ESP32-S3FN8`；`schematic_label=STAMP-S3-DIP-1.27`；`schematic_revision_visible=false` |
| 内存与 Flash | 主控 Flash | `documented_capacity=8MB`；`schematic_capacity_label=null`；`discrete_memory_reference=null`；`module=M1 STAMP-S3-DIP-1.27` |
| 核心器件 | U1 WS1850S | `reference=U1`；`part_number=WS1850S`；`supply=+3.3V`；`digital=RC522_SDA/RC522_SCL/RC522_IRQ/NRSTPD`；`rf=TX1/TX2/RX` |
| 射频 | RFID 天线匹配 | `antenna=L2 ANT_Hole`；`tx_inductors=L1/L3 1uH`；`series_caps=C8/C14 47pF`；`shunt_caps=C10/C12 120pF; C11/C13 390pF`；`series_resistors=R4/R5 1.2Ω`；`rx_network=R2 1KΩ; C7 1nF; R3 1.5KΩ` |
| 时钟 | WS1850S 参考时钟 | `device=U1 WS1850S`；`crystal=Y1`；`frequency=27.12MHz`；`load_caps=C6/C9 15pF` |
| 射频 | RFID 工作频率 | `documented_carrier=13.56MHz`；`schematic_clock=Y1 27.12MHz`；`carrier_label_visible=false` |
| 总线 | RTC、触摸与 RFID 共享 I2C | `controller=M1`；`sda=GPIO11 / TP_SDA`；`scl=GPIO12 / TP_SCL`；`rtc=U5 RTC8563`；`touch=BTB1 pins 19/20`；`rfid=U1 WS1850S via R9/R8 0Ω`；`logic_level=+3.3V` |
| 总线地址 | I2C 设备地址 | `bus=TP_SDA/TP_SCL`；`devices=U5 RTC8563; U1 WS1850S; BTB1 touch`；`address_visible=false`；`addresses=null` |
| 时钟 | RTC8563 低速时钟 | `rtc=U5 RTC8563`；`crystal=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load=12.5pF`；`capacitors=C28/C29 6.0pF` |
| 关键网络 | RTC INT 唤醒路径 | `source=U5 INT`；`net=INT`；`diode=D3 B5819WT`；`destination=Q3/Q4 latch node` |
| 核心器件 | LCD 与触摸控制器型号 | `connector=BTB1 OK-24M024-04`；`documented_lcd_driver=GC9A01`；`documented_touch_driver=FT3267`；`schematic_driver_labels_visible=false` |
| 总线 | LCD SPI 总线 | `controller=M1`；`mosi=GPIO5 -> LCD_MOSI -> BTB1-6`；`sck=GPIO6 -> LCD_SCK -> BTB1-8`；`cs=GPIO7 -> LCD_CS -> BTB1-9`；`dc=GPIO4 -> LCD_RS -> BTB1-5`；`miso=null`；`direction=MCU to LCD` |
| GPIO 与控制信号 | 显示与触摸控制 GPIO | `reset=GPIO8 -> LCD_RESET -> BTB1-10/18; R7 0Ω -> NRSTPD`；`backlight=GPIO9 -> LCD_BL -> Q1`；`touch_interrupt=GPIO14 <- TP_INT`；`rfid_interrupt=GPIO10 <- RC522_INT` |
| 传感器 | J5 旋转编码器 | `reference=J5`；`part_number=EC30-16bit`；`phase_a=A -> GPIO41`；`phase_b=B -> GPIO40`；`pullups=R21/R22 10KΩ`；`filters=C22/C23 100nF`；`common=GND`；`direction=input` |
| 音频 | 蜂鸣器驱动 | `gpio=GPIO3 / beep`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`drive=R25 470Ω + C27 10uF`；`diode=D6 1N4148` |
| 接口 | J3 PORT.A | `reference=J3`；`pin_1=SCL / GPIO15`；`pin_2=SDA / GPIO13`；`pin_3=+5VOUT`；`pin_4=GND`；`bus=external I2C`；`signal_level=+3.3V logic` |
| 接口 | J2 PORT.B | `reference=J2`；`pin_1=GI / GPIO1`；`pin_2=GO / GPIO2`；`pin_3=+5VOUT`；`pin_4=GND`；`signal_direction=GPIO configurable`；`signal_level=+3.3V logic` |
| 接口 | P1/P3 显示板间连接 | `connectors=P1/P3 6X2@2.54`；`signals=LCD_BL, LCD_RS, LCD_MOSI, LCD_SCK, LCD_CS, LCD_RESET, RC522_INT, TP_SDA, TP_SCL, TP_INT`；`power=+3.3V`；`ground=GND` |
| 电源 | P5 外部直流输入 | `connector=P5 Header 2`；`positive=pin 1 -> D13 -> +VIN`；`negative=pin 2 -> GND`；`series_diode=D13 B5819W SL`；`tvs=D12 SD36`；`capacitors=C34 10uF/35V; C35 100nF` |
| 电源 | 外部直流输入范围 | `documented_range=DC 6~36V`；`schematic_range_label=null`；`input_capacitor_rating=C34 35V`；`converter=U7 ME3116AM6G` |
| 电源 | U7 +5VIN 转换 | `reference=U7`；`input=+VIN`；`output=+5VIN`；`inductor=L6 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R33 56KΩ; R34 10KΩ` |
| 电源 | U2 TP4057 充电 | `reference=U2`；`part_number=TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN via JP1`；`program=R17 10KΩ via JP2`；`status=CHRG/STDBY` |
| 电源 | P6 电池接口 | `reference=P6`；`pin_1=VBAT_IN`；`pin_2=GND`；`capacitor=C21 10uF` |
| 电源 | 电池与 +5VIN 电源选择 | `battery_path=VBAT_IN -> Q2 LP3218DT1G`；`external_path=+5VIN -> D1 SS34`；`output_switch=Q3 LP3218DT1G`；`output=VBAT_OUT` |
| 电源 | +5VOUT 电源轨 | `reference=U3`；`input=VBAT_OUT`；`output=+5VOUT`；`inductor=L4 1.5uH`；`feedback=R16 150KΩ; R18 47KΩ`；`output_diode=D8 SS34` |
| 电源 | +3.3V 电源轨 | `reference=U4`；`input=VBAT_OUT`；`output=+3.3V`；`enable=3V3EN via R26 50KΩ`；`inductor=L5 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ` |
| 电源 | HOLD/WAKE 电源锁存 | `hold=GPIO46 -> HOLD -> Q4`；`wake=GPIO42 -> WAKE`；`button=S1 SW-PB`；`rtc=U5 INT -> D3`；`diodes=D3/D4/D10 B5819WT` |
| 复位 | 主控 EN 与 BOOT | `reset_pin=M1 EN`；`reset_switch=S4 SW-PB to GND`；`boot_pin=M1 G0/Boot`；`connector=P4 Header 11` |
| 保护电路 | 输入和按键保护 | `input_tvs=D12 SD36`；`input_series_diode=D13 B5819W SL`；`wake_esd=D5 PESDNC2FD3V3B`；`protected_nets=+VIN; WAKE/S1` |

## 待确认事项

- `component.version-controller-identity`：产品正文称 Dial v1.1 使用 Stamp-S3A/ESP32-S3FN8，但两张原理图未显示 v1.1 标题、Stamp-S3A 或 ESP32-S3FN8，仅显示 M1 STAMP-S3-DIP-1.27。（证据：图 1d8705f9d82d / 第 1 页 / 第1图完整页，未见产品版本或主控型号标题; 图 0528f589274c / 第 1 页 / 第2图 C2-D2，M1 仅标 STAMP-S3-DIP-1.27）
- `memory.flash-capacity`：产品正文标称 8MB Flash，但两张原理图未画出独立存储器，也未在 M1 上标注 Flash 容量。（证据：图 0528f589274c / 第 1 页 / 第2图 C2-D2 M1 与完整页，未见 Flash 位号或容量）
- `rf.rfid-operating-frequency`：产品正文标称 RFID 标签工作频率 13.56MHz；原理图仅标出 27.12MHz 参考晶振和天线匹配元件，未直接标注载波频率。（证据：图 1d8705f9d82d / 第 1 页 / 第1图 B1-B3，Y1 27.12MHz 与 L2 ANT_Hole；未见 13.56MHz 标注）
- `component.display-touch-models`：产品正文称屏幕驱动为 GC9A01、触摸驱动为 FT3267；原理图只给出 BTB1 OK-24M024-04 的 LCD/TP 引脚，未直接标出两颗控制器型号。（证据：图 1d8705f9d82d / 第 1 页 / 第1图 C4-D4 BTB1，仅标 LCD/TP 信号与连接器型号）
- `power.input-voltage-range`：产品正文标称 P5 支持 DC 6~36V；原理图显示 35V 输入电容、SD36 TVS 与 ME3116AM6G，但未直接标注 6~36V 范围。（证据：图 0528f589274c / 第 1 页 / 第2图 A1-A3，+VIN 输入、C34 10uF/35V、D12 SD36、U7）
- `review.version-controller-identity`：这两张 Sch_M5Dial 原理图是否确实对应 Dial v1.1 的 Stamp-S3A/ESP32-S3FN8 硬件版本？；原因：两页没有可见版本标题，主控只标 STAMP-S3-DIP-1.27，没有 Stamp-S3A 或 ESP32-S3FN8 标识。
- `review.flash-capacity`：Dial v1.1 当前主控模组的 Flash 容量是否确定为 8MB？；原因：容量来自产品正文，原理图未标注主控内部 Flash 容量。
- `review.display-touch-models`：BTB1 所接圆屏和触摸控制器是否分别固定为 GC9A01 与 FT3267？；原因：型号来自产品正文，原理图只显示 LCD/TP 信号和 OK-24M024-04 连接器。
- `review.rfid-frequency`：当前 WS1850S 与天线匹配网络的 RFID 载波是否确定为 13.56MHz？；原因：13.56MHz 来自产品正文，原理图只直接标出 Y1 27.12MHz 参考晶振。
- `review.input-voltage-range`：P5 外部输入的认证范围是否为 DC 6~36V？；原因：6~36V 来自产品正文，原理图只给出元件型号和额定值，未直接写输入范围。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1d8705f9d82d57055876ab9d3a01eb0ae8e4b1610880c99568b4b360f5b47c1f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_01.png` |
| 2 | 1 | `0528f589274c10708c0eb75b8f10f0cc9f0d02a4adef8b0e2d31747cd6252a88` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_02.png` |

---

源文档：`zh_CN/core/M5Dial V1.1.md`

源文档 SHA-256：`a5cf4290112b43b9bd5b5bc1fb8883b0401335f85adf9c91ca5939ebf727cf11`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
