# DinMeter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | DinMeter |
| SKU | K134 |
| 产品 ID | `dinmeter-375ebdfc5925` |
| 源文档 | `zh_CN/core/M5DinMeter.md` |

## 概述

DinMeter 以 M1 STAMP-S3-SMD 为控制核心，GPIO 驱动 RTC8563、旋转编码器/按键、蜂鸣器、SPI LCD 及两路 HY2.0-4P。J1 标注 6V~36V，经 D13/SD36 保护后由 U1 ME3116AM6G 生成 +5VIN；U2 TP4057 充电到 VBAT_IN，Q3/Q6/Q4 与 CN809J、RTC INT、WAKE/BTN、HOLD 形成供电选择和保持。U3 SY7088 从 VBAT_OUT 生成 +5VOUT，U4 BL8075CB5TR33 生成 +3.3V，U6 AW35122FDR 控制 LCD 背光。原理图未直接标 ST7789V2/135×240、RTC 7位地址、250mAh/100mA/待机与 Grove 带载性能，也未展开 Stamp-S3 内部 ESP32-S3FN8/Flash/射频/USB。

## 检索关键词

`DinMeter`、`K134`、`STAMP-S3-SMD`、`ESP32-S3FN8`、`ME3116AM6G`、`TP4057`、`CN809J`、`AP40P05`、`LN2324DT2AG`、`SY7088`、`BL8075CB5TR33`、`RTC8563`、`BM8563`、`AW35122FDR`、`ST7789V2`、`6V~36V`、`+VIN`、`+5VIN`、`+5VOUT`、`+3.3V`、`VBAT_IN`、`VBAT_OUT`、`BATADC`、`HOLD GPIO46`、`WAKE GPIO42`、`RTC INT`、`IN_SCL GPIO12`、`IN_SDA GPIO11`、`IN_A GPIO41`、`IN_B GPIO40`、`beep GPIO3`、`LCD_CS GPIO7`、`LCD_SCK GPIO6`、`LCD_RS GPIO4`、`LCD_MOSI GPIO5`、`LCD_RESET GPIO8`、`LCD_BL GPIO9`、`PORT.A`、`PORT.B`、`32.768KHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-SMD | 主控模组接口，连接 RTC、编码器、蜂鸣器、LCD、电源保持和 Grove GPIO | 图 4ce24ae8fe29 / 第 1 页 / 网格 C2-D3，M1 STAMP-S3-SMD pins1-31 |
| J1 | Header 2 | 标注 6V~36V 的直流输入接口 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A1，J1 Header 2、6V~36V、D13/D12/C7 |
| U1 | ME3116AM6G | +VIN 输入、+5VIN 输出的宽压降压转换器 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A2-A3，U1 ME3116AM6G、L1、D9/D11、R5/R6 |
| U2 | TP4057 | +5VIN 输入、VBAT_IN 输出的锂电池充电器 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A1-B2，U2 TP4057、R11/R17、C15/C21、VBAT_IN |
| U7 | CN809J | 监测 +5VIN 并通过 RESET 控制输入电源路径 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A1-A2，U7 CN809J、+5VIN、RESET、Q3 |
| Q3,Q6 | AP40P05 | VBAT_IN 到 VBAT_OUT 的高侧电源选择与保持开关 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A2-B3，Q3/Q6 AP40P05、VBAT_IN/VBAT_OUT、INT/BTN/HOLD |
| Q4 | LN2324DT2AG | HOLD 控制 Q6 栅极的电源保持 MOSFET | 图 4ce24ae8fe29 / 第 1 页 / 网格 B2-C3，Q4 LN2324DT2AG、HOLD、R23、Q6 栅极 |
| U3 | SY7088 | VBAT_OUT 输入、+5VOUT 输出的升压转换器 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A3-B4 虚线框，U3 SY7088、L4、R16/R18、D8 |
| U4 | BL8075CB5TR33 | VBAT_OUT 输入、+3.3V 输出的线性稳压器 | 图 4ce24ae8fe29 / 第 1 页 / 网格 B3-C4，U4 BL8075CB5TR33、C32/C33/C30/C31 |
| J2,Q1 | Header 2 / LP3218DT1G | 电池接口、反向/开关路径及 BATADC 分压 | 图 4ce24ae8fe29 / 第 1 页 / 网格 A4，J2/Q1/R7/R8/VBAT_IN/BATADC |
| U5 | RTC8563 | IN_SCL/IN_SDA I2C、32.768kHz 晶振与 INT 唤醒的 RTC | 图 4ce24ae8fe29 / 第 1 页 / 网格 B1-C2，U5 RTC8563、Y2、INT、IN_SCL/IN_SDA |
| Y2 | 32.768KHz±20ppm 12.5pF | RTC8563 时钟晶振 | 图 4ce24ae8fe29 / 第 1 页 / 网格 C1，Y2、C28/C29、OSCI/OSCO |
| J5 | Rotary encoder | WAKE/BTN 按压和 IN_A/IN_B 正交旋转输入 | 图 4ce24ae8fe29 / 第 1 页 / 网格 C2-C3，J5 Rotary encoder、R1-R3、C1-C3 |
| LS1,Q5 | Buzzer / SS8050 Y1 | GPIO3 beep 控制的低侧蜂鸣器驱动 | 图 4ce24ae8fe29 / 第 1 页 / 网格 C1-D2，LS1、Q5、R24/R25、C27、D6/D7 |
| FPC1 | FPC-0.5-8P | SPI LCD 电源、背光、复位和数据接口 | 图 4ce24ae8fe29 / 第 1 页 / 网格 C3-D4，FPC1 pins1-8、LCD_CS/SCK/MOSI/RS/RESET/BL |
| U6 | AW35122FDR | +3.3V 到 FPC_LCD_BL 的显示背光负载开关，EN 由 LCD_BL 控制 | 图 4ce24ae8fe29 / 第 1 页 / 网格 D3，U6 AW35122FDR、LCD_BL、FPC_LCD_BL |
| J3 | HY-2.0_IIC | SCL/SDA/+5VOUT/GND 的 PORT.A I2C Grove 接口 | 图 4ce24ae8fe29 / 第 1 页 / 网格 C4-D4，J3 HY-2.0_IIC |
| J4 | HY-2.0_IO | G1/G0/+5VOUT/GND 的 PORT.B GPIO Grove 接口 | 图 4ce24ae8fe29 / 第 1 页 / 网格 D4，J4 HY-2.0_IO |
| S4 | SW-PB | Stamp-S3 G0/Boot 低有效按键 | 图 4ce24ae8fe29 / 第 1 页 / 网格 D2-D3，S4 与 M1 G0/Boot pin20 |

## 系统结构

### DinMeter 系统架构

M1 STAMP-S3-SMD 连接 RTC8563、J5 旋转编码器、蜂鸣器、SPI LCD、两路 Grove 和电源保持网络；J1 宽压输入经 ME3116AM6G 生成 +5VIN，TP4057/Q3/Q6/Q4 管理电池，SY7088/BL8075 分别生成 +5VOUT/+3.3V。

- 参数与网络：`controller=M1 STAMP-S3-SMD`；`rtc=U5 RTC8563`；`encoder=J5`；`display=FPC1 + U6 AW35122FDR`；`buzzer=LS1/Q5`；`wide_input=J1 + U1 ME3116AM6G`；`charger=U2 TP4057`；`rails=U3 +5VOUT,U4 +3.3V`；`ports=J3 PORT.A,J4 PORT.B`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 完整单页 A1-D4 全部功能分区

## 电源

### 6V~36V 直流输入

J1 pin1 标注 6V~36V，经 D13 B5819W SL 串联形成 +VIN；D12 SD36 对输入钳位，C7 100nF、C24 10uF/35V 与 C8 100nF 对地滤波，J1 pin2 接 GND。

- 参数与网络：`connector=J1 Header 2`；`range_label=6V~36V`；`positive=pin1 -> D13 B5819W SL -> +VIN`；`negative=pin2 GND`；`tvs=D12 SD36`；`caps=C7 100nF,C24 10uF/35V,C8 100nF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A1-A2，J1/D13/D12/C7/C24/C8/+VIN

### +VIN 到 +5VIN

U1 ME3116AM6G 的 VIN 接 +VIN，EN 经 R4 100KΩ 接 +VIN，LX 经 L1 3015 10uH 输出 +5VIN；D9/D11 B5819W SL 构成开关/输出二极管，反馈为 R5 56KΩ 与 R6 10KΩ。

- 参数与网络：`converter=U1 ME3116AM6G`；`input=+VIN`；`enable=R4 100KΩ to +VIN`；`inductor=L1 3015 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R5 56KΩ,R6 10KΩ`；`output=+5VIN`；`output_caps=C10 22uF,C25 10uF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A2-A3，U1/L1/D9/D11/R4-R6/+5VIN

### +5VIN 到 VBAT_IN 充电

+5VIN 经 R11 0.8Ω 接 U2 TP4057 VCC，BAT pin3 输出 VBAT_IN；PROG pin6 经 R17 10KΩ 接 GND，C15/C21 各 10uF 分别位于输入和 VBAT_IN 侧。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program_resistor=R17 10KΩ`；`status=CHRG,STDBY`；`caps=C15 10uF,C21 10uF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A1-B2，U2/R11/R17/C15/C21/VBAT_IN

### +5VIN 与 VBAT_IN 电源汇合

VBAT_IN 经 Q3 AP40P05 接入中间电源节点，+5VIN 经 D1 SS34 接同一节点；U7 CN809J RESET 控制 Q3 栅极并由 R19 100KΩ 下拉。

- 参数与网络：`battery_path=VBAT_IN -> Q3 AP40P05`；`external_path=+5VIN -> D1 SS34`；`supervisor=U7 CN809J`；`gate_pulldown=R19 100KΩ`；`merged_node=Q6 input rail`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A1-B2，U7/Q3/D1/R19/VBAT_IN/+5VIN

### RTC/按键唤醒与 HOLD 保持

RTC INT 经 D3、按键 BTN 经 D4、WAKE 经 D10 汇合到 Q6 AP40P05 控制节点；M1 GPIO46 形成 HOLD，驱动 Q4 LN2324DT2AG 并保持 Q6 导通，R23 100KΩ 将 HOLD 下拉。

- 参数与网络：`rtc_wake=INT -> D3 B5819WT`；`button_wake=BTN -> D4 B5819WT`；`wake_net=WAKE -> D10 B5819WT`；`high_side=Q6 AP40P05`；`hold_gpio=M1 GPIO46 HOLD`；`hold_switch=Q4 LN2324DT2AG`；`pulldown=R23 100KΩ`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 B2-C3，INT/BTN/WAKE/D3/D4/D10/Q6/Q4/HOLD

### VBAT_OUT 到 +5VOUT

VBAT_OUT 经 R12 0Ω 与 L4 3015 1.5uH 进入 U3 SY7088，反馈网络为 R16 52.3KΩ/R18 15KΩ，输出经 D8 SS34 形成 +5VOUT；C19/C18 各 22uF。

- 参数与网络：`input=VBAT_OUT`；`converter=U3 SY7088`；`series=R12 0Ω`；`inductor=L4 3015 1.5uH`；`feedback=R16 52.3KΩ,R18 15KΩ`；`diode=D8 SS34`；`output=+5VOUT`；`caps=C19 22uF,C18 22uF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A3-B4，U3/L4/R12/R16/R18/D8/+5VOUT

### VBAT_OUT 到 +3.3V

U4 BL8075CB5TR33 的 VIN/EN 接 VBAT_OUT，VOUT 输出 +3.3V；输入 C32 100nF/C33 22uF，输出 C30 22uF/C31 100nF。

- 参数与网络：`regulator=U4 BL8075CB5TR33`；`input=VBAT_OUT`；`enable=VBAT_OUT`；`output=+3.3V`；`input_caps=C32 100nF,C33 22uF`；`output_caps=C30 22uF,C31 100nF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 B3-C4，U4/C32/C33/C30/C31/+3.3V

### LCD 背光负载开关

U6 AW35122FDR 以 +3.3V 为 VIN，VOUT 输出 FPC_LCD_BL，EN 由 M1 GPIO9 的 LCD_BL 控制，C4 100nF 为输入去耦。

- 参数与网络：`switch=U6 AW35122FDR`；`input=+3.3V`；`output=FPC_LCD_BL`；`enable=LCD_BL / GPIO9`；`decoupling=C4 100nF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 D3，U6/C4/LCD_BL/FPC_LCD_BL

## 接口

### PORT.A I2C Grove

J3 HY-2.0_IIC pin1=SCL/M1 GPIO12、pin2=SDA/M1 GPIO11、pin3=+5VOUT、pin4=GND。

- 参数与网络：`connector=J3 HY-2.0_IIC`；`pin1=SCL / GPIO12`；`pin2=SDA / GPIO11`；`pin3=+5VOUT`；`pin4=GND`；`direction=I2C bidirectional`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C4-D4，J3 SCL/SDA/+5VOUT/GND

### PORT.B GPIO Grove

J4 HY-2.0_IO pin1=G1、pin2=G0、pin3=+5VOUT、pin4=GND，G1/G0 对应 M1 pins1/2。

- 参数与网络：`connector=J4 HY-2.0_IO`；`pin1=G1 bidirectional`；`pin2=G0 bidirectional`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 D4，J4 G1/G0/+5VOUT/GND 与 M1 pins1/2

## 总线

### RTC8563 I2C 与中断

U5 RTC8563 SCL pin6 接 IN_SCL/M1 GPIO12，SDA pin5 接 IN_SDA/M1 GPIO11，INT pin3 输出 INT 到唤醒网络；VDD 接 VBAT_IN。

- 参数与网络：`rtc=U5 RTC8563`；`scl=IN_SCL / M1 GPIO12`；`sda=IN_SDA / M1 GPIO11`；`interrupt=INT`；`supply=VBAT_IN`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 B1-C2，U5/IN_SCL/IN_SDA/INT/VBAT_IN

### LCD SPI 与控制映射

FPC1 pin1 LCD_CS=M1 GPIO7、pin3 LCD_SCK=GPIO6、pin4 LCD_MOSI=GPIO5、pin5 LCD_RS=GPIO4、pin6 LCD_RESET=GPIO8、pin8 FPC_LCD_BL；pin2 +3.3V、pin7 GND。

- 参数与网络：`connector=FPC1 FPC-0.5-8P`；`cs=GPIO7`；`sck=GPIO6`；`mosi=GPIO5`；`dc=GPIO4`；`reset=GPIO8`；`backlight=FPC_LCD_BL`；`supply=+3.3V`；`ground=GND`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C3-D4，M1 LCD nets 与 FPC1 pins1-8

## GPIO 与控制信号

### 旋转编码器与按压唤醒

J5 A/B 分别形成 IN_A/IN_B，连接 M1 GPIO41/GPIO40；R2/R3 各 10KΩ 上拉到 +3.3V，C2/C3 各 100nF 对地。编码器按压 b1/b2 形成 WAKE/BTN，R1 10KΩ 上拉且 C1 100nF 对地。

- 参数与网络：`encoder=J5 Rotary encoder`；`a=IN_A / GPIO41`；`b=IN_B / GPIO40`；`pullups=R2/R3 10KΩ`；`filters=C2/C3 100nF`；`button=WAKE/BTN`；`button_pullup=R1 10KΩ`；`button_filter=C1 100nF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C2-C3，J5/R1-R3/C1-C3/IN_A/IN_B/WAKE/BTN

## 时钟

### RTC 32.768kHz 时钟

Y2 标注 32.768KHz±20ppm 12.5pF，连接 U5 OSCI/OSCO，两端分别以 C28/C29 6.0pF 对地。

- 参数与网络：`crystal=Y2 32.768KHz±20ppm 12.5pF`；`rtc=U5 RTC8563`；`pins=OSCI/OSCO`；`caps=C28/C29 6.0pF`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C1，Y2/C28/C29/OSCI/OSCO

## 复位

### Stamp-S3 Boot 按键

S4 SW-PB 按下将 M1 G0/Boot pin20 接 GND，用于低电平 Boot/下载控制。

- 参数与网络：`button=S4 SW-PB`；`controller_pin=M1 pin20 G0/Boot`；`active_level=low`；`return=GND`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 D2-D3，S4 与 M1 G0/Boot

## 保护电路

### 输入、电池和控制保护

宽压输入使用 D13 B5819W SL 反向串联和 D12 SD36 钳位；电池接口通过 Q1 LP3218DT1G；RTC/WAKE/BTN 使用 D3/D4/D10 B5819WT 隔离；D5 PESDNC2FD3V3B 保护 +3.3V/控制节点，蜂鸣器使用 D6/D7 钳位。

- 参数与网络：`wide_input=D13 B5819W SL,D12 SD36`；`battery=Q1 LP3218DT1G`；`wake_or=D3/D4/D10 B5819WT`；`esd=D5 PESDNC2FD3V3B`；`buzzer=D6/D7 1N4148WT`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 完整单页 D3-D13/Q1 等保护器件

## 音频

### GPIO3 蜂鸣器驱动

M1 GPIO3 的 beep 网络经 R25 470Ω 与 C27 10uF 驱动 Q5 SS8050 Y1，Q5 低侧开关 LS1 Buzzer；R24 10Ω 从 +3.3V 向蜂鸣器供电，D6/D7 1N4148WT 用于钳位。

- 参数与网络：`gpio=M1 GPIO3`；`net=beep`；`base=R25 470Ω,C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`diodes=D6/D7 1N4148WT`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C1-D2，M1 beep/R25/C27/Q5/LS1/R24/D6/D7

## 模拟电路

### BATADC 电池采样

J2 电池正端经 Q1 LP3218DT1G 形成 VBAT_IN；VBAT_IN 经 R7/R8 各 1MΩ 分压到 BATADC，BATADC 连接 M1 pin10。

- 参数与网络：`connector=J2 Header 2`；`switch=Q1 LP3218DT1G`；`battery_net=VBAT_IN`；`divider=R7 1MΩ high,R8 1MΩ low`；`adc_net=BATADC`；`controller_pin=M1 pin10`
- 证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A4 与 C2-D2，J2/Q1/R7/R8/BATADC/M1 pin10

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | DinMeter 系统架构 | `controller=M1 STAMP-S3-SMD`；`rtc=U5 RTC8563`；`encoder=J5`；`display=FPC1 + U6 AW35122FDR`；`buzzer=LS1/Q5`；`wide_input=J1 + U1 ME3116AM6G`；`charger=U2 TP4057`；`rails=U3 +5VOUT,U4 +3.3V`；`ports=J3 PORT.A,J4 PORT.B` |
| 电源 | 6V~36V 直流输入 | `connector=J1 Header 2`；`range_label=6V~36V`；`positive=pin1 -> D13 B5819W SL -> +VIN`；`negative=pin2 GND`；`tvs=D12 SD36`；`caps=C7 100nF,C24 10uF/35V,C8 100nF` |
| 电源 | +VIN 到 +5VIN | `converter=U1 ME3116AM6G`；`input=+VIN`；`enable=R4 100KΩ to +VIN`；`inductor=L1 3015 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R5 56KΩ,R6 10KΩ`；`output=+5VIN`；`output_caps=C10 22uF,C25 10uF` |
| 电源 | +5VIN 到 VBAT_IN 充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program_resistor=R17 10KΩ`；`status=CHRG,STDBY`；`caps=C15 10uF,C21 10uF` |
| 电源 | +5VIN 与 VBAT_IN 电源汇合 | `battery_path=VBAT_IN -> Q3 AP40P05`；`external_path=+5VIN -> D1 SS34`；`supervisor=U7 CN809J`；`gate_pulldown=R19 100KΩ`；`merged_node=Q6 input rail` |
| 电源 | RTC/按键唤醒与 HOLD 保持 | `rtc_wake=INT -> D3 B5819WT`；`button_wake=BTN -> D4 B5819WT`；`wake_net=WAKE -> D10 B5819WT`；`high_side=Q6 AP40P05`；`hold_gpio=M1 GPIO46 HOLD`；`hold_switch=Q4 LN2324DT2AG`；`pulldown=R23 100KΩ` |
| 电源 | VBAT_OUT 到 +5VOUT | `input=VBAT_OUT`；`converter=U3 SY7088`；`series=R12 0Ω`；`inductor=L4 3015 1.5uH`；`feedback=R16 52.3KΩ,R18 15KΩ`；`diode=D8 SS34`；`output=+5VOUT`；`caps=C19 22uF,C18 22uF` |
| 电源 | VBAT_OUT 到 +3.3V | `regulator=U4 BL8075CB5TR33`；`input=VBAT_OUT`；`enable=VBAT_OUT`；`output=+3.3V`；`input_caps=C32 100nF,C33 22uF`；`output_caps=C30 22uF,C31 100nF` |
| 模拟电路 | BATADC 电池采样 | `connector=J2 Header 2`；`switch=Q1 LP3218DT1G`；`battery_net=VBAT_IN`；`divider=R7 1MΩ high,R8 1MΩ low`；`adc_net=BATADC`；`controller_pin=M1 pin10` |
| 总线 | RTC8563 I2C 与中断 | `rtc=U5 RTC8563`；`scl=IN_SCL / M1 GPIO12`；`sda=IN_SDA / M1 GPIO11`；`interrupt=INT`；`supply=VBAT_IN` |
| 时钟 | RTC 32.768kHz 时钟 | `crystal=Y2 32.768KHz±20ppm 12.5pF`；`rtc=U5 RTC8563`；`pins=OSCI/OSCO`；`caps=C28/C29 6.0pF` |
| GPIO 与控制信号 | 旋转编码器与按压唤醒 | `encoder=J5 Rotary encoder`；`a=IN_A / GPIO41`；`b=IN_B / GPIO40`；`pullups=R2/R3 10KΩ`；`filters=C2/C3 100nF`；`button=WAKE/BTN`；`button_pullup=R1 10KΩ`；`button_filter=C1 100nF` |
| 音频 | GPIO3 蜂鸣器驱动 | `gpio=M1 GPIO3`；`net=beep`；`base=R25 470Ω,C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`diodes=D6/D7 1N4148WT` |
| 总线 | LCD SPI 与控制映射 | `connector=FPC1 FPC-0.5-8P`；`cs=GPIO7`；`sck=GPIO6`；`mosi=GPIO5`；`dc=GPIO4`；`reset=GPIO8`；`backlight=FPC_LCD_BL`；`supply=+3.3V`；`ground=GND` |
| 电源 | LCD 背光负载开关 | `switch=U6 AW35122FDR`；`input=+3.3V`；`output=FPC_LCD_BL`；`enable=LCD_BL / GPIO9`；`decoupling=C4 100nF` |
| 接口 | PORT.A I2C Grove | `connector=J3 HY-2.0_IIC`；`pin1=SCL / GPIO12`；`pin2=SDA / GPIO11`；`pin3=+5VOUT`；`pin4=GND`；`direction=I2C bidirectional` |
| 接口 | PORT.B GPIO Grove | `connector=J4 HY-2.0_IO`；`pin1=G1 bidirectional`；`pin2=G0 bidirectional`；`pin3=+5VOUT`；`pin4=GND` |
| 复位 | Stamp-S3 Boot 按键 | `button=S4 SW-PB`；`controller_pin=M1 pin20 G0/Boot`；`active_level=low`；`return=GND` |
| 保护电路 | 输入、电池和控制保护 | `wide_input=D13 B5819W SL,D12 SD36`；`battery=Q1 LP3218DT1G`；`wake_or=D3/D4/D10 B5819WT`；`esd=D5 PESDNC2FD3V3B`；`buzzer=D6/D7 1N4148WT` |
| 核心器件 | RTC8563/BM8563 名称与地址 | `schematic_part=RTC8563`；`documented_part=BM8563`；`address=null`；`bus=IN_SCL/IN_SDA`；`production_part=null` |
| 核心器件 | ST7789V2 屏幕规格 | `documented_driver=ST7789V2`；`documented_size=1.14 inch`；`documented_resolution=135x240`；`schematic_connector=FPC1 FPC-0.5-8P`；`schematic_driver=null`；`schematic_resolution=null` |
| 电源 | 250mAh 电池、充电电流与待机 | `documented_capacity=250mAh`；`documented_charge_current=100mA`；`documented_standby=DC4.2V@38.4uA`；`charger=TP4057 with R17 10KΩ`；`cell_part_number=null`；`protection=null`；`termination=null`；`measurement_conditions=null` |
| 电源 | PORT.A/PORT.B 5V 带载能力 | `documented_port_a=DC5V Max220mA`；`documented_port_b=DC5V Max220mA`；`source=+5VOUT via U3 SY7088`；`current_limit_device=null`；`combined_limit=null`；`efficiency=null`；`thermal_limit=null` |
| 系统结构 | Stamp-S3 内部 SoC、Flash、Wi-Fi 与 USB | `documented_soc=ESP32-S3FN8`；`documented_flash=8MB`；`documented_wifi=2.4GHz`；`documented_usb=USB OTG,USB Serial/JTAG`；`schematic_module=M1 STAMP-S3-SMD interface only`；`internal_schematic=null` |

## 待确认事项

- `component.rtc-name-address`：原理图 U5 标注 RTC8563，正文数据手册链接称 BM8563；原理图确认 IN_SCL/IN_SDA 拓扑但未写 7 位 I2C 地址，量产正式料号和地址需确认。（证据：图 4ce24ae8fe29 / 第 1 页 / 网格 B1-C2，U5 标注 RTC8563，无地址文字）
- `component.documented-display`：正文称屏幕为 ST7789V2、1.14英寸、135×240；原理图只显示 FPC1 八针接口、SPI/控制和背光开关，没有面板位号、驱动 IC、尺寸或分辨率标注。（证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C3-D4，FPC1/U6 显示接口，无 ST7789V2/分辨率文字）
- `power.documented-battery-performance`：包装/正文称配套 250mAh 电池、充电电流 100mA、4.2V 电池待机 38.4uA；原理图只显示 J2、TP4057/R17 10KΩ、电源路径和 BATADC，未标电芯型号/容量、保护板、终止条件或这些测量值的测试条件。（证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A1-B4，J2/U2/VBAT/BATADC 路径，无电池与性能表）
- `power.documented-grove-load`：正文称 PORT.A 与 PORT.B 均为 5V/Max 220mA；原理图确认两口由 +5VOUT 供电及 SY7088 反馈网络，但未标端口限流器、额定 220mA、效率、温升或两口同时带载边界。（证据：图 4ce24ae8fe29 / 第 1 页 / 网格 A3-D4，U3 +5VOUT 与 J3/J4，无 220mA 标注）
- `system.documented-stamp-internals`：正文称 Stamp-S3 使用 ESP32-S3FN8、8MB Flash、2.4GHz Wi-Fi、USB OTG/Serial-JTAG；当前 DinMeter 原理图仅画 M1 STAMP-S3-SMD 外部针脚，没有模组内部 SoC、Flash、天线、时钟或 USB 连接。（证据：图 4ce24ae8fe29 / 第 1 页 / 网格 C2-D3，M1 仅模块外部符号，D-/D+ 未连接到本页外部接口）
- `review.rtc-part-address`：K134 量产 RTC 的正式料号是 RTC8563 还是 BM8563，其 7 位 I2C 地址是什么？；原因：原理图和正文命名不一致且图中未标地址。
- `review.display-panel`：请用量产屏幕 BOM/丝印确认 ST7789V2、1.14英寸、135×240 及初始化参数。；原因：原理图只有 FPC1 接口与背光。
- `review.battery-performance`：请确认 250mAh 电芯型号、保护配置、TP4057 充电电流/终止条件，以及 38.4uA 待机测试条件。；原因：电池规格和性能测量未标在原理图。
- `review.grove-load`：PORT.A/PORT.B 各 220mA 及同时带载时的总电流、效率、温升和保护边界是什么？；原因：原理图未标端口限流或额定电流。
- `review.stamp-internals`：请用对应 Stamp-S3 模组原理图/datasheet 确认 ESP32-S3FN8、8MB Flash、天线、USB 和时钟连接。；原因：本页只显示 STAMP-S3-SMD 外部接口。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4ce24ae8fe296cae5800e5e4c3b8851d8aaa5cb7024cdf5ae5b976bfde3bdb5d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/DIN_Meter_v1.0_sch_01.png` |

---

源文档：`zh_CN/core/M5DinMeter.md`

源文档 SHA-256：`72295da997ce7cf15863c7a56a51da3ee0ce7b2fb627ed311a7e35a68a642ae8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
