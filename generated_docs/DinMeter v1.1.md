# DinMeter v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | DinMeter v1.1 |
| SKU | K134-V11 |
| 产品 ID | `dinmeter-v1-1-1be53f587107` |
| 源文档 | `zh_CN/core/DinMeter_v1.1.md` |

## 概述

DinMeter v1.1 的单页 K134-V11 DIN Meter v1.0 原理图以 M1 STAMP-S3-SMD 为主控，集成 6V~36V 直流输入、ME3116 降压、TP4057 电池充电、VBAT/+5VIN 电源选择与 HOLD/WAKE 控制、SY7088 5V 升压、BL8075 3.3V 稳压、RTC8563、旋转编码器、蜂鸣器、LCD FPC/背光驱动以及 PORT.A/PORT.B。页面能确认 GPIO46 HOLD、GPIO42 WAKE、GPIO41/40 编码器 A/B、GPIO3 蜂鸣器、LCD G4-G9 与 RTC G12/G11 等连接。正文声明 Stamp-S3A、ESP32-S3FN8/8MB、ST7789P3 135x240、250mAh/100mA、Grove 220mA 和 38.4uA 待机，但这些型号或额定值未在单页中完整标注，已保留待确认。

## 检索关键词

`DinMeter v1.1`、`K134-V11`、`DIN Meter v1.0`、`STAMP-S3-SMD`、`Stamp-S3A`、`ESP32-S3FN8`、`8MB Flash`、`ME3116AM6G`、`TP4057`、`CN809J`、`SY7088`、`BL8075CB5TR33`、`RTC8563`、`32.768KHz`、`ST7789P3`、`AW35122FDR`、`Rotary encoder`、`Buzzer`、`6V~36V`、`+VIN`、`+5VIN`、`+5VOUT`、`+3.3V`、`VBAT_IN`、`VBAT_OUT`、`BATADC`、`WAKE`、`HOLD`、`GPIO46`、`GPIO42`、`GPIO41`、`GPIO40`、`GPIO3`、`GPIO4`、`GPIO5`、`GPIO6`、`GPIO7`、`GPIO8`、`GPIO9`、`GPIO11`、`GPIO12`、`PORT.A`、`PORT.B`、`HY-2.0_IIC`、`HY-2.0_IO`、`FPC_LCD_BL`、`LCD_RESET`、`LCD_MOSI`、`LCD_SCK`、`LCD_CS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-SMD | 页面中的主控模组，连接 LCD、RTC、编码器、蜂鸣器、WAKE/HOLD、ADC 和扩展接口 | 图 9419d0013cd9 / 第 1 页 / 网格 C2-D3，M1 STAMP-S3-SMD 全部引脚 |
| U1 | ME3116AM6G | 6V~36V 输入到 +5VIN 的降压转换器 | 图 9419d0013cd9 / 第 1 页 / 网格 A1-B3，J1/D13/D12/U1/L1/D11 输入降压区 |
| U2 | TP4057 | +5VIN 到 VBAT_IN 的锂电池充电器 | 图 9419d0013cd9 / 第 1 页 / 网格 A1-B2，U2 TP4057 与 R17/C15/C21 |
| U3 | SY7088 | VBAT_OUT 到 +5VOUT 的升压转换器 | 图 9419d0013cd9 / 第 1 页 / 网格 A3-B4，虚线框 U3 SY7088 |
| U4 | BL8075CB5TR33 | VBAT_OUT 到 +3.3V 的线性稳压器 | 图 9419d0013cd9 / 第 1 页 / 网格 B3-C4，U4 BL8075CB5TR33 |
| U5 | RTC8563 | VBAT_IN 供电的 I2C RTC，INT 参与唤醒 | 图 9419d0013cd9 / 第 1 页 / 网格 B1-C2，U5 RTC8563 与 Y2 |
| U6 | AW35122FDR | GPIO9/LCD_BL 控制的 LCD 背光驱动器 | 图 9419d0013cd9 / 第 1 页 / 网格 D3-D4，U6 AW35122FDR 与 FPC_LCD_BL |
| U7 | CN809J | +5VIN 电源监控/复位器件 | 图 9419d0013cd9 / 第 1 页 / 网格 A1，U7 CN809J |
| Q3,Q6 | AP40P05 | VBAT_IN/+5VIN 到 VBAT_OUT 的电源路径开关 | 图 9419d0013cd9 / 第 1 页 / 网格 A1-B3，Q3/Q6、D1 与 VBAT_OUT |
| Q4 | LN2324DT2AG | GPIO46/HOLD 控制的电源保持 MOSFET | 图 9419d0013cd9 / 第 1 页 / 网格 B2-C3，Q4、HOLD 与 R23 |
| Q1 | LP3218DT1G | J2 外接电池到 VBAT_IN 的输入开关 | 图 9419d0013cd9 / 第 1 页 / 网格 A4，J2/Q1 与 BATADC 分压 |
| J5 | Rotary encoder | A/B 正交编码与 BTN/WAKE 按键输入 | 图 9419d0013cd9 / 第 1 页 / 网格 C2-D3，J5 Rotary encoder 与 R1-R3/C1-C3 |
| LS1,Q5 | Buzzer / SS8050 Y1 | GPIO3/beep 经低端晶体管驱动的 3.3V 蜂鸣器 | 图 9419d0013cd9 / 第 1 页 / 网格 C1-D2，LS1/Q5 蜂鸣器区 |
| FPC1 | FPC-0.5-8P | LCD 子板接口，承载 SPI、复位、3.3V、GND 与背光 | 图 9419d0013cd9 / 第 1 页 / 网格 C3-D4，FPC1 LCD 接口 |
| J3,J4 | HY-2.0_IIC / HY-2.0_IO | PORT.A I2C 与 PORT.B 双 GPIO 5V 扩展接口 | 图 9419d0013cd9 / 第 1 页 / 网格 C4-D4，J3/J4 |
| J1,J2 | Header 2 / Header 2 | 6V~36V 直流输入和外接电池接口 | 图 9419d0013cd9 / 第 1 页 / 网格 A1 的 J1 与网格 A4 的 J2 |

## 系统结构

### DinMeter v1.1 电路架构

单页资源以 M1 STAMP-S3-SMD 为主控，连接 6V~36V 输入降压、电池充电与电源保持、5V 升压、3.3V 稳压、RTC8563、旋转编码器、蜂鸣器、LCD FPC/背光及两路 HY2.0 扩展接口。

- 参数与网络：`controller=M1 STAMP-S3-SMD`；`dc_input=6V~36V -> U1 ME3116AM6G`；`charger=U2 TP4057`；`boost=U3 SY7088`；`regulator=U4 BL8075CB5TR33`；`rtc=U5 RTC8563`；`ui=J5 encoder,LS1,FPC1`；`ports=J3/J4`
- 证据：图 9419d0013cd9 / 第 1 页 / 完整 K134-V11 DIN Meter 单页原理图

## 电源

### +VIN 到 +5VIN 降压

U1 ME3116AM6G VIN 接 +VIN，EN 由 R4 100K 连接输入，LX 经 D9 B5819W、L1 10uH 和 D11 B5819W 形成输出路径，R5 56K/R6 10K 为反馈分压，输出为 +5VIN。

- 参数与网络：`converter=U1 ME3116AM6G`；`input=+VIN`；`enable=R4 100K`；`inductor=L1 3015 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R5 56K,R6 10K`；`output=+5VIN`；`output_caps=C10 22uF,C25 10uF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A2-B3，U1/L1/D9/D11/R5/R6

### TP4057 电池充电

+5VIN 经 R11 0.8Ω接 U2 TP4057 VCC，BAT pin3 接 VBAT_IN，PROG pin6 经 R17 10K 接地；C15 10uF 位于输入，C21 10uF 位于 VBAT_IN。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8R`；`battery=VBAT_IN`；`program_resistor=R17 10K`；`input_capacitor=C15 10uF`；`battery_capacitor=C21 10uF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A1-B2，U2 TP4057

### +5VIN 与电池电源选择

VBAT_IN 经 Q3 AP40P05 接入中间节点，+5VIN 经 D1 SS34 接入同一节点，该节点再经 Q6 AP40P05 输出 VBAT_OUT；C16/C17 各 10uF 分别位于 Q6 前后。

- 参数与网络：`battery_path=VBAT_IN -> Q3 AP40P05`；`external_path=+5VIN -> D1 SS34`；`output_switch=Q6 AP40P05 -> VBAT_OUT`；`capacitors=C16=10uF,C17=10uF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A1-B3，VBAT_IN/Q3/D1/Q6/VBAT_OUT

### RTC/按键唤醒与 HOLD 保持

RTC INT 经 D3 B5819WT、BTN 经 D4 B5819WT、WAKE 经 D10 B5819WT 接入 Q6 控制节点；HOLD/GPIO46 驱动 Q4 LN2324DT2AG，R23 100K 将 HOLD 下拉到 GND。

- 参数与网络：`rtc_wake=INT via D3`；`button_wake=BTN via D4`；`wake_net=WAKE via D10`；`hold=GPIO46/HOLD`；`hold_switch=Q4 LN2324DT2AG`；`hold_pulldown=R23 100K`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 B1-C3，INT/BTN/WAKE/D3/D4/D10/Q4/HOLD

### SY7088 5V 升压

U3 SY7088 从 VBAT_OUT 取电，L4 为 1.5uH，OUT 经 D8 SS34 输出 +5VOUT；反馈分压为 R16 52.3K 与 R18 15K，C18 22uF 位于输出。

- 参数与网络：`converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 3015 1.5uH`；`output=+5VOUT via D8 SS34`；`feedback=R16 52.3K,R18 15K`；`output_capacitor=C18 22uF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A3-B4，虚线框 U3 SY7088

### BL8075 3.3V 稳压

U4 BL8075CB5TR33 的 VIN/EN 接 VBAT_OUT，VOUT 输出 +3.3V；C32 100nF/C33 22uF 为输入去耦，C30 22uF/C31 100nF 为输出去耦。

- 参数与网络：`regulator=U4 BL8075CB5TR33`；`input=VBAT_OUT`；`enable=VBAT_OUT`；`output=+3.3V`；`input_caps=C32 100nF,C33 22uF`；`output_caps=C30 22uF,C31 100nF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 B3-C4，U4 与 C30-C33

### LCD 背光驱动

U6 AW35122FDR 由 +3.3V 供电，EN 接 LCD_BL/G9，VOUT 输出 FPC_LCD_BL 到 FPC1 pin8，C4 100nF 为输入去耦。

- 参数与网络：`driver=U6 AW35122FDR`；`input=+3.3V`；`enable=LCD_BL/G9`；`output=FPC_LCD_BL`；`connector=FPC1 pin8`；`decoupling=C4 100nF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 D3-D4，U6/C4/FPC_LCD_BL

## 接口

### 6V~36V 直流输入

J1 Header 2 pin1 接 6V~36V 输入、pin2 接 GND；输入经 D13 B5819W SL 串联到 +VIN，并由 C7 100nF、D12 SD36、C24 10uF/35V 和 C8 100nF 进行滤波与保护。

- 参数与网络：`connector=J1 Header 2`；`pin1=6V~36V`；`pin2=GND`；`series_diode=D13 B5819W SL`；`protection=D12 SD36`；`capacitors=C7 100nF,C24 10uF/35V,C8 100nF`；`rail=+VIN`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A1-A2，J1/D13/D12/C7/C24/C8

### LCD FPC SPI 与控制映射

FPC1 pins1-8 分别连接 LCD_CS、+3.3V、LCD_SCK、LCD_MOSI、LCD_RS、LCD_RESET、GND、FPC_LCD_BL；M1 将 LCD_CS/SCK/MOSI/RS/RESET/BL 映射到 G7/G6/G5/G4/G8/G9。

- 参数与网络：`connector=FPC1 FPC-0.5-8P`；`pin1=LCD_CS/G7`；`pin2=+3.3V`；`pin3=LCD_SCK/G6`；`pin4=LCD_MOSI/G5`；`pin5=LCD_RS/G4`；`pin6=LCD_RESET/G8`；`pin7=GND`；`pin8=FPC_LCD_BL`；`backlight_control=LCD_BL/G9`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 C3-D4，FPC1 与 M1 LCD_* 引脚

### PORT.A I2C 接口

J3 HY-2.0_IIC pins1-4 分别连接 SCL、SDA、+5VOUT、GND；M1 将 SCL/SDA 映射到 G15/G13。

- 参数与网络：`connector=J3 HY-2.0_IIC`；`pin1=SCL/G15`；`pin2=SDA/G13`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 C4-D4，J3 与 M1 G15/G13

### PORT.B 双 GPIO 接口

J4 HY-2.0_IO pins1-4 分别连接 M1 G1、M1 G2、+5VOUT、GND。

- 参数与网络：`connector=J4 HY-2.0_IO`；`pin1=M1 G1`；`pin2=M1 G2`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 D2-D4，M1 pins1/2 与 J4 pins1/2

## 总线

### RTC8563 I2C 与中断

U5 RTC8563 SCL/SDA 分别连接 IN_SCL/IN_SDA，M1 将 IN_SCL/IN_SDA 映射到 G12/G11；INT 输出进入电源唤醒网络，VDD 接 VBAT_IN。

- 参数与网络：`rtc=U5 RTC8563`；`scl=G12/IN_SCL`；`sda=G11/IN_SDA`；`interrupt=INT -> D3 wake network`；`supply=VBAT_IN`；`address=null`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 B1-C2，U5 IN_SCL/IN_SDA/INT 与 M1 G12/G11

## GPIO 与控制信号

### 旋转编码器与按键

J5 A/B 端分别连接 IN_A/IN_B，M1 将 IN_A/IN_B 映射到 G41/G40；R2/R3 各 10K 上拉到 +3.3V，C2/C3 各 100nF 对地。编码器按键端 BTN/WAKE 由 R1 10K 上拉、C1 100nF 对地并连接 M1 G42/WAKE。

- 参数与网络：`encoder_a=G41/IN_A`；`encoder_b=G40/IN_B`；`pullups=R2/R3 10K`；`filters=C2/C3 100nF`；`button=BTN/WAKE`；`button_gpio=G42`；`button_pullup=R1 10K`；`button_filter=C1 100nF`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 C2-D3，J5/R1-R3/C1-C3 与 M1 G41/G40/G42

## 时钟

### RTC 32.768KHz 晶振

Y2 标注 32.768KHz ±20ppm 12.5pF，连接 OSCI/OSCO，C28/C29 各 6.0pF 接地。

- 参数与网络：`reference=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load_annotation=12.5pF`；`capacitors=C28=6.0pF,C29=6.0pF`；`nets=OSCI,OSCO`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 C1，Y2/C28/C29

## 复位

### EN 复位按键

S4 是从 M1 EN pin22 到 GND 的常开按键，按下将 EN 拉低。

- 参数与网络：`button=S4 SW-PB`；`target=M1 EN pin22`；`other_terminal=GND`；`active_level=low`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 D2-D3，M1 EN 到 S4/GND

## 音频

### GPIO3 蜂鸣器驱动

+3.3V 经 R24 10Ω和 LS1 蜂鸣器接 Q5 SS8050 Y1 集电极，Q5 发射极接地；M1 G3/beep 经 R25 470Ω、C27 10uF 驱动基极，D6 跨接蜂鸣器支路，D7 从基极节点接地。

- 参数与网络：`gpio=G3/beep`；`buzzer=LS1`；`driver=Q5 SS8050 Y1`；`supply_path=+3.3V -> R24 10R -> LS1`；`base_path=beep -> R25 470R -> C27 10uF`；`diodes=D6/D7 1N4148WT`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 C1-D2，LS1/Q5/R24/R25/C27/D6/D7

## 模拟电路

### 电池电压 BATADC 分压

J2 电池正端经 Q1 LP3218DT1G 接 VBAT_IN，VBAT_IN 通过 R7 1MΩ与 R8 1MΩ分压到 BATADC，BATADC 连接 M1 G10。

- 参数与网络：`connector=J2`；`switch=Q1 LP3218DT1G`；`source=VBAT_IN`；`upper_resistor=R7 1M`；`lower_resistor=R8 1M`；`adc_net=BATADC`；`gpio=M1 G10`
- 证据：图 9419d0013cd9 / 第 1 页 / 网格 A4，J2/Q1/R7/R8/BATADC；网格 D2，M1 G10

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | DinMeter v1.1 电路架构 | `controller=M1 STAMP-S3-SMD`；`dc_input=6V~36V -> U1 ME3116AM6G`；`charger=U2 TP4057`；`boost=U3 SY7088`；`regulator=U4 BL8075CB5TR33`；`rtc=U5 RTC8563`；`ui=J5 encoder,LS1,FPC1`；`ports=J3/J4` |
| 接口 | 6V~36V 直流输入 | `connector=J1 Header 2`；`pin1=6V~36V`；`pin2=GND`；`series_diode=D13 B5819W SL`；`protection=D12 SD36`；`capacitors=C7 100nF,C24 10uF/35V,C8 100nF`；`rail=+VIN` |
| 电源 | +VIN 到 +5VIN 降压 | `converter=U1 ME3116AM6G`；`input=+VIN`；`enable=R4 100K`；`inductor=L1 3015 10uH`；`diodes=D9/D11 B5819W SL`；`feedback=R5 56K,R6 10K`；`output=+5VIN`；`output_caps=C10 22uF,C25 10uF` |
| 电源 | TP4057 电池充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8R`；`battery=VBAT_IN`；`program_resistor=R17 10K`；`input_capacitor=C15 10uF`；`battery_capacitor=C21 10uF` |
| 电源 | +5VIN 与电池电源选择 | `battery_path=VBAT_IN -> Q3 AP40P05`；`external_path=+5VIN -> D1 SS34`；`output_switch=Q6 AP40P05 -> VBAT_OUT`；`capacitors=C16=10uF,C17=10uF` |
| 电源 | RTC/按键唤醒与 HOLD 保持 | `rtc_wake=INT via D3`；`button_wake=BTN via D4`；`wake_net=WAKE via D10`；`hold=GPIO46/HOLD`；`hold_switch=Q4 LN2324DT2AG`；`hold_pulldown=R23 100K` |
| 电源 | SY7088 5V 升压 | `converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 3015 1.5uH`；`output=+5VOUT via D8 SS34`；`feedback=R16 52.3K,R18 15K`；`output_capacitor=C18 22uF` |
| 电源 | BL8075 3.3V 稳压 | `regulator=U4 BL8075CB5TR33`；`input=VBAT_OUT`；`enable=VBAT_OUT`；`output=+3.3V`；`input_caps=C32 100nF,C33 22uF`；`output_caps=C30 22uF,C31 100nF` |
| 模拟电路 | 电池电压 BATADC 分压 | `connector=J2`；`switch=Q1 LP3218DT1G`；`source=VBAT_IN`；`upper_resistor=R7 1M`；`lower_resistor=R8 1M`；`adc_net=BATADC`；`gpio=M1 G10` |
| 总线 | RTC8563 I2C 与中断 | `rtc=U5 RTC8563`；`scl=G12/IN_SCL`；`sda=G11/IN_SDA`；`interrupt=INT -> D3 wake network`；`supply=VBAT_IN`；`address=null` |
| 时钟 | RTC 32.768KHz 晶振 | `reference=Y2`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load_annotation=12.5pF`；`capacitors=C28=6.0pF,C29=6.0pF`；`nets=OSCI,OSCO` |
| GPIO 与控制信号 | 旋转编码器与按键 | `encoder_a=G41/IN_A`；`encoder_b=G40/IN_B`；`pullups=R2/R3 10K`；`filters=C2/C3 100nF`；`button=BTN/WAKE`；`button_gpio=G42`；`button_pullup=R1 10K`；`button_filter=C1 100nF` |
| 复位 | EN 复位按键 | `button=S4 SW-PB`；`target=M1 EN pin22`；`other_terminal=GND`；`active_level=low` |
| 音频 | GPIO3 蜂鸣器驱动 | `gpio=G3/beep`；`buzzer=LS1`；`driver=Q5 SS8050 Y1`；`supply_path=+3.3V -> R24 10R -> LS1`；`base_path=beep -> R25 470R -> C27 10uF`；`diodes=D6/D7 1N4148WT` |
| 接口 | LCD FPC SPI 与控制映射 | `connector=FPC1 FPC-0.5-8P`；`pin1=LCD_CS/G7`；`pin2=+3.3V`；`pin3=LCD_SCK/G6`；`pin4=LCD_MOSI/G5`；`pin5=LCD_RS/G4`；`pin6=LCD_RESET/G8`；`pin7=GND`；`pin8=FPC_LCD_BL`；`backlight_control=LCD_BL/G9` |
| 电源 | LCD 背光驱动 | `driver=U6 AW35122FDR`；`input=+3.3V`；`enable=LCD_BL/G9`；`output=FPC_LCD_BL`；`connector=FPC1 pin8`；`decoupling=C4 100nF` |
| 接口 | PORT.A I2C 接口 | `connector=J3 HY-2.0_IIC`；`pin1=SCL/G15`；`pin2=SDA/G13`；`pin3=+5VOUT`；`pin4=GND` |
| 接口 | PORT.B 双 GPIO 接口 | `connector=J4 HY-2.0_IO`；`pin1=M1 G1`；`pin2=M1 G2`；`pin3=+5VOUT`；`pin4=GND` |
| 系统结构 | DinMeter v1.1 主控版本 | `documented_controller=Stamp-S3A`；`schematic_controller=STAMP-S3-SMD`；`resource_sku=K134-V11`；`difference_bom=null` |
| 内存与 Flash | ESP32-S3FN8 与 8MB Flash | `documented_soc=ESP32-S3FN8`；`documented_flash=8MB`；`schematic_module=STAMP-S3-SMD`；`internal_soc=null`；`flash_part=null`；`flash_bus=null` |
| 核心器件 | ST7789P3 屏幕与分辨率 | `documented_controller=ST7789P3`；`documented_size=1.14 inch`；`documented_resolution=135x240`；`schematic=FPC1 connector only`；`panel_bom=null` |
| 电源 | 250mAh 电池与 100mA 充电 | `documented_battery=250mAh LiPo`；`documented_charge_current=100mA`；`documented_connector=1.25mm-2P`；`schematic_connector=J2 Header 2`；`charger=U2 TP4057`；`program_resistor=R17 10K`；`battery_part=null` |
| 电源 | PORT.A/PORT.B 5V@220mA 带载 | `documented_port_a=5V@220mA`；`documented_port_b=5V@220mA`；`shared_rail=+5VOUT`；`converter=U3 SY7088`；`per_port_limit=null`；`protection=null`；`test_conditions=null` |
| 电源 | 电池待机电流 | `documented_standby=DC 4.2V@38.4uA`；`power_control=WAKE/HOLD/Q4/Q6`；`measurement_point=null`；`module_state=null`；`peripheral_state=null`；`temperature=null` |
| 系统结构 | 产品 v1.1 与 DIN Meter v1.0 图纸版本 | `product_version=v1.1`；`sku=K134-V11`；`drawing_filename_version=v1.0`；`title_block=null`；`revision_history=null` |

## 待确认事项

- `system.v11-controller-version`：产品正文称 v1.1 已从 Stamp-S3 升级为 Stamp-S3A，资源文件名含 K134-V11 但图中 M1 仍标 STAMP-S3-SMD，未出现 Stamp-S3A 型号或差异 BOM，当前模组版本需确认。（证据：图 9419d0013cd9 / 第 1 页 / M1 STAMP-S3-SMD 标注）
- `memory.v11-soc-flash`：正文规格列 ESP32-S3FN8 和 8MB Flash；原理图只给出封装级 M1 STAMP-S3-SMD，没有模组内部 SoC/Flash 器件、容量或总线，v1.1 配置需确认。（证据：图 9419d0013cd9 / 第 1 页 / M1 模组符号，无内部 SoC/Flash）
- `component.documented-st7789`：正文称 1.14英寸 ST7789P3、分辨率 135x240；原理图只给 FPC1 和 SPI/复位/背光网络，没有 LCD 控制器、面板型号、尺寸或分辨率，显示子板需确认。（证据：图 9419d0013cd9 / 第 1 页 / FPC1 仅为 LCD 接口，无 ST7789P3 器件）
- `power.documented-battery-charge`：包装与规格称 250mAh 聚合物锂电池、100mA 充电和 1.25mm-2P 电池座；原理图只显示 J2 Header 2、TP4057 与 R17 10K，没有电池料号、容量、连接器具体型号或充电电流标注。（证据：图 9419d0013cd9 / 第 1 页 / J2/Q1 与 U2/R17，无电池料号和电流标注）
- `power.documented-grove-load`：正文称 PORT.A 和 PORT.B 各支持 DC 5V@220mA；原理图只显示两接口共用 +5VOUT 和 SY7088 升压网络，没有每端口限流、独立保护、220mA 标注或测试条件。（证据：图 9419d0013cd9 / 第 1 页 / U3 +5VOUT 到 J3/J4，无端口限流和 220mA 标注）
- `power.documented-standby-current`：正文称电池供电 DC 4.2V@38.4uA 待机电流；原理图显示 WAKE/HOLD 电源切换拓扑，但没有电池电压范围、测量点、模块状态、外设状态或 38.4uA 测试条件。（证据：图 9419d0013cd9 / 第 1 页 / WAKE/HOLD 电源控制网络，无待机测量条件）
- `system.resource-drawing-version`：产品名和 SKU 为 DinMeter v1.1/K134-V11，资源文件名为 K134-V11_DIN_Meter_v1.0；页面没有标题栏或版本变更表，v1.0 图纸版本号与 v1.1 产品版本号的对应规则需确认。（证据：图 9419d0013cd9 / 第 1 页 / 单页无标题栏/Revision 表；资源文件名含 DIN_Meter_v1.0）
- `review.controller-version`：请提供 DinMeter v1.1 的 Stamp-S3A BOM 或模组变更说明，确认 M1 实际版本。；原因：图中仍标 STAMP-S3-SMD。
- `review.soc-flash`：请确认 Stamp-S3A 内部 ESP32-S3FN8、8MB Flash 的实际料号与存储配置。；原因：原理图没有模组内部器件。
- `review.display`：请提供显示子板原理图或 BOM，确认 ST7789P3、1.14英寸、135x240 与背光额定参数。；原因：主板页只有 FPC1 接口。
- `review.battery-charge`：请确认 250mAh 电池料号、1.25mm-2P 连接器、极性及 TP4057 100mA 充电配置。；原因：图中没有电池料号和充电电流文字。
- `review.grove-load`：请确认两路 Grove 各 5V@220mA 的限流、保护、同时带载能力和测试条件。；原因：两接口共用 +5VOUT，图中无单口 220mA 限制。
- `review.standby-current`：请确认 4.2V@38.4uA 待机电流的测量点、固件状态、外设状态、温度和仪器条件。；原因：原理图只给出电源拓扑。
- `review.drawing-version`：请确认 K134-V11 产品 v1.1 与 DIN_Meter_v1.0 图纸版本号的对应关系。；原因：文件名版本与产品版本不同，页面无修订表。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9419d0013cd9b47a54a320f3bfc45d13464e6af484245ba741326f9870ff7006` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1211/K134-V11_DIN_Meter_v1.0_2025_11_25_17_15_58_page_01.png` |

---

源文档：`zh_CN/core/DinMeter_v1.1.md`

源文档 SHA-256：`85eabb68671282134155cd94ee394a2359b253b1108bc39a5f9fc4149865fbb0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
