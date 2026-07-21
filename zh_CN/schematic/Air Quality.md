# Air Quality 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Air Quality |
| SKU | K131 |
| 产品 ID | `air-quality-1ff69f191246` |
| 源文档 | `zh_CN/core/Air_Quality.md` |

## 概述

Air Quality 以 M1 STAMP-S3-DIP-1.27 为主控，通过 G11/G12 的 SDA1/SCL1 I2C 总线连接 U5 RTC8563、U6 SCD40 和 P3 外接传感器接口；P3 的 VDD 由 U1 ME1502CM5G 负载开关受 AirPWREN/G10 控制。墨水屏通过 G1-G6 的 BUSY/RST/D-C/CS/SCK/MOSI 连接 J1 24 针 FPC，并配有独立正负压生成网络。+5VIN 经 U2 TP4057 充电到 VBAT_IN，Q2/Q3/Q4 与 WAKE/HOLD/RTC INT 构成断电保持和唤醒路径，U3 SY7088 生成 +5VOUT，U4 SY8089 生成 +3.3V。S2/S3/S4、S1、LS1 蜂鸣器和 J3 Grove 构成用户交互与扩展；传感器地址、屏幕型号/分辨率和电池容量需结合 datasheet、BOM 或实测确认。

## 检索关键词

`Air Quality`、`K131`、`STAMP-S3-DIP-1.27`、`ESP32-S3`、`RTC8563`、`SCD40`、`SEN55`、`TP4057`、`SY7088`、`SY8089`、`ME1502CM5G`、`SDA1`、`SCL1`、`G11`、`G12`、`AirPWREN`、`G10`、`HOLD`、`G46`、`WAKE`、`G42`、`G14`、`EPD_BUSY`、`EPD_RES`、`EPD_DC`、`EPD_CS`、`EPD_SCK`、`EPD_MOSI`、`GDEY0154D67`、`USER_A`、`USER_B`、`G0`、`G8`、`beep`、`G9`、`VBAT_IN`、`VBAT_OUT`、`+5VOUT`、`+3.3V`、`HY2.0_IIC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-DIP-1.27 | 主控模组，连接显示、I2C 传感器、按键、蜂鸣器、电源保持和扩展接口 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C2-D3，M1 STAMP-S3-DIP-1.27，左右 Header17/Header11 引脚 |
| U2 | TP4057 | +5VIN 输入、VBAT_IN 输出的电池充电器 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A1，U2 TP4057，VCC/BAT/PROG/CHRG/STDBY |
| U3 | SY7088 | 将 VBAT_OUT 升压为 +5VOUT 的转换器 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A3-A4 虚线框，U3 SY7088、L4、D8 与 +5VOUT |
| U4 | SY8089 | 由 VBAT_OUT 生成 +3.3V 的降压转换器 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B3-B4，U4 SY8089、L5、R27/R28 与 +3.3V |
| U5 | RTC8563 | VBAT_IN 供电的 RTC，连接 32.768kHz 晶振、SDA1/SCL1 和 INT 唤醒网络 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B1，U5 RTC8563 与 OSCI/OSCO/INT/SCL/SDA/VDD |
| U6 | SCD40 | 3.3V 供电、挂接 SDA1/SCL1 的 CO2 传感器 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3-D3，U6 SCD40，SCL/SDA/VDD/VDDH/GND |
| U1 | ME1502CM5G | 由 AirPwREN 控制 P3 传感器 VDD 的负载开关/限流器件 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3，U1 ME1502CM5G，VIN/EN/RSET/VOUT 与 AirPwREN |
| P3 | Header 6 | SEN55 类传感器接口，提供 VDD/GND/SDA1/SCL1/SEL/NC | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3，P3 Header6 pin1 VDD、2 GND、3 SDA、4 SCL、5 SEL、6 NC |
| J1 | FPC-0.5-24P | 电子纸显示器 24 针接口，连接 SPI/控制、逻辑电源和门极正负压网络 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C4-D4，J1 FPC-0.5-24P pin1-pin24 |
| J3,SW1 | HY-2.0_IIC / SW-SPDT | Grove 四针 SCL/SDA/VCC/GND 接口，VCC 可在 +5VOUT 与 +5VIN 间选择 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C4，J3 HY-2.0_IIC 与 SW1 SPDT |
| P1 | Header 2 | VBAT_IN/GND 电池接口 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A1，P1 Header2 pin1 VBAT_IN、pin2 GND |
| S1,S2,S3,S4 | SW-PB | WAKE、USER_A、USER_B 和 RST 按键 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B1-C1，S1 WAKE 与 S2/S3/S4 USER_A/USER_B/RST |
| LS1,Q5 | Buzzer / SS8050 Y1 | GPIO9 beep 控制的无源蜂鸣器与低侧驱动晶体管 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C1-D1，LS1 Buzzer、Q5 SS8050 Y1、R25/C27/D7 |
| Y2 | 32.768kHz ±20ppm 12.5pF | RTC8563 OSCI/OSCO 外部晶振 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C2，Y2 32.768kHz、C28/C29 6pF 与 OSCI/OSCO |
| Q2,Q3 | LP3218DT1G | +5VIN/VBAT_IN 至 VBAT_OUT 的电源路径 MOSFET | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A1-A3，Q2/Q3 LP3218DT1G 与 VBAT_IN/VBAT_OUT |
| U7 | CN809J | +5VIN 供电的复位监控器，参与 Q2 电源路径控制 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A2，U7 CN809J VCC/RESET/GND 与 Q2 gate |
| Q4 | LN2324DT2AG | HOLD 网络控制的电源保持 MOSFET | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B2，Q4 LN2324DT2AG、HOLD、R23 与 GND |
| Q1,L1,D9,D10,D11 | LN2324DT2AG / 10uH / B5819WT | 电子纸 PEGH/PEGL 正负压生成网络 | 图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3-D4，Q1/L1/D9-D11/C8-C14 与 GDR/RESE/PEGH/PEGL |

## 系统结构

### Air Quality 系统架构

M1 StampS3 通过 SDA1/SCL1 连接 RTC8563、SCD40 和 P3 传感器接口，通过 G1-G6 控制 J1 电子纸，通过 AirPwREN 控制 P3 电源，并连接按键、蜂鸣器、HOLD/WAKE 与 Grove。电池/USB 电源经 TP4057、Q2/Q3/Q4、SY7088、SY8089 形成 VBAT_IN/VBAT_OUT、+5VOUT 和 +3.3V。

- 参数与网络：`controller=M1 STAMP-S3-DIP-1.27`；`i2c=SDA1/SCL1`；`rtc=RTC8563`；`co2=SCD40`；`sensor_header=P3`；`display=J1 FPC-0.5-24P`；`power=TP4057,Q2/Q3/Q4,SY7088,SY8089`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 电源

### +5VIN 到 VBAT_IN 充电

+5VIN 经 R11 0.8Ω 接 U2 TP4057 VCC pin4，U2 BAT pin3 接 VBAT_IN，PROG pin6 经 R17 2.3KΩ 接 GND；C15 10uF 位于输入侧，C21 10uF 位于 VBAT_IN 侧，P1 pin1 引出 VBAT_IN、pin2 为 GND。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program=R17 2.3KΩ`；`caps=C15/C21 10uF`；`connector=P1 pin1 VBAT_IN,pin2 GND`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A1，TP4057、R11/R17、C15/C21 与 P1

### VBAT_OUT 电源保持与唤醒

VBAT_IN 经 Q2/Q3 LP3218DT1G 形成 VBAT_OUT，+5VIN 通过 D1 SS34 汇入中间节点；RTC INT 经 D3、WAKE/S1 经 D4/D15 接控制节点，HOLD 控制 Q4 LN2324DT2AG，R23 100KΩ 下拉。

- 参数与网络：`path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`usb_or=+5VIN via D1 SS34`；`rtc_wake=INT via D3 B5819WT`；`button_wake=WAKE via D4/D15 B5819WT`；`hold=HOLD -> Q4 LN2324DT2AG`；`pulldown=R23 100KΩ`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A1-B3，Q2/Q3/U7/D1/D3/D4/D15/Q4 与 WAKE/HOLD/INT

### VBAT_OUT 到 +5VOUT

VBAT_OUT 经 R12 0Ω、L4 1.5uH 进入 U3 SY7088，U3 OUT pins7/8 经 D8 SS34 输出 +5VOUT；FB 使用 R16 52.3KΩ 与 R18 15KΩ，C18 22uF 对地。

- 参数与网络：`input=VBAT_OUT`；`converter=U3 SY7088`；`inductor=L4 1.5uH`；`diode=D8 SS34`；`output=+5VOUT`；`feedback=R16 52.3KΩ,R18 15KΩ`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 A3-A4 虚线 Boost 区

### VBAT_OUT 到 +3.3V

VBAT_OUT 连接 U4 SY8089 IN pin4，3V3EN 经 R26 100KΩ 接 EN pin1；LX pin3 经 L5 4.7uH 输出 +3.3V，FB 使用 R27 68KΩ/R28 15KΩ，C30 22uF/C31 100nF 对地。

- 参数与网络：`input=VBAT_OUT`；`converter=U4 SY8089`；`enable=3V3EN via R26 100KΩ`；`inductor=L5 4.7uH`；`output=+3.3V`；`feedback=R27 68KΩ,R28 15KΩ`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B3-B4 U4 SY8089 电源区

### P3 传感器电源开关

+5VOUT 经 C1 22uF 接 U1 ME1502CM5G VIN pin5，AirPwREN/G10 控制 EN pin4，R1 27KΩ 设置 RSET pin3；VOUT pin1 经 C2 22uF/C3 100nF 后接 P3 pin1 VDD，P3 pin2 为 GND、pin5 SEL 接 GND、pin6 NC。

- 参数与网络：`input=+5VOUT`；`switch=U1 ME1502CM5G`；`enable=AirPwREN GPIO10`；`rset=R1 27KΩ`；`output=P3 pin1 VDD`；`header=pin2 GND,pin3 SDA1,pin4 SCL1,pin5 SEL GND,pin6 NC`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3 U1 ME1502CM5G 与 P3

### 电子纸高低压网络

J1 逻辑电源 pin15 VDDIO、pin16 VCI 接 +3.3V，pin17 VSS 接 GND；Q1/L1/D9-D11 与 C8-C14 生成 PEGH/PEGL 并连接 J1 VGH/VGL/VSH/VSL/PREVGH/PREVGL/VCOM 等模拟电源引脚。

- 参数与网络：`logic=J1 pin15/16 +3.3V,pin17 GND`；`driver=Q1 LN2324DT2AG,L1 10uH,D9-D11 B5819WT`；`positive=PEGH`；`negative=PEGL`；`display_rails=VGL,VGH,VSH,VSL,PREVGH,PREVGL,VCOM`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3-D4 电子纸泵电源与 J1 pin1-pin24

## 接口

### J3 Grove I2C 接口

J3 HY-2.0_IIC 的 pin1=SCL、pin2=SDA、pin3=VCC、pin4=GND；SCL/SDA 对应 M1 G15/G13，SW1 SPDT 在 +5VOUT 与 +5VIN 之间选择 VCC 来源。

- 参数与网络：`pin1=SCL GPIO15`；`pin2=SDA GPIO13`；`pin3=VCC selected`；`pin4=GND`；`selector=SW1 +5VOUT/+5VIN`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C4 J3 HY-2.0_IIC 与 SW1

## 总线

### SDA1/SCL1 共享 I2C 总线

M1 G11 接 SDA1、G12 接 SCL1；同名网络连接 U5 RTC8563 SDA/SCL、U6 SCD40 SDA/SCL 和 P3 pin3 SDA/pin4 SCL。U6 使用 R2/R3 各 15KΩ 上拉到 +3.3V。

- 参数与网络：`controller=M1 StampS3`；`sda=G11 SDA1`；`scl=G12 SCL1`；`devices=U5 RTC8563,U6 SCD40,P3 sensor`；`pullups=R2/R3 15KΩ to +3.3V`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页 U5/U6/P3 与 M1 的 SDA1/SCL1 同名网络

### 电子纸 SPI 与控制映射

M1 G1/G2/G3/G4/G5/G6 分别连接 EPD_BUSY、EPD_RES、EPD_DC、EPD_CS、EPD_SCK、EPD_MOSI；这些网络进入 J1 pin9 BUSY、pin10 RES、pin11 D/C、pin12 CS、pin13 D0、pin14 D1。

- 参数与网络：`busy=G1 -> J1 pin9`；`reset=G2 -> pin10`；`dc=G3 -> pin11`；`chip_select=G4 -> pin12`；`clock=G5 -> pin13 D0`；`mosi=G6 -> pin14 D1`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页 M1 左侧 EPD_* 与 J1 pin9-pin14

## GPIO 与控制信号

### 用户按键、唤醒与复位

S2 将 USER_A/G0 按下接 GND，S3 将 USER_B/G8 按下接 GND，S4 将 RST/StampS3 EN 按下接 GND；S1 WAKE 通过 D4/D15 进入唤醒控制，USER_A/USER_B 分别带 D12/D13 PESDNC2FD3V3B 对地保护。

- 参数与网络：`user_a=S2 USER_A GPIO0`；`user_b=S3 USER_B GPIO8`；`reset=S4 RST -> EN`；`wake=S1 WAKE -> D4/D15`；`esd=D12/D13 PESDNC2FD3V3B`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B1-C1 S1-S4 与 D12/D13/D15

## 时钟

### RTC8563 32.768kHz 时钟

U5 OSCI/OSCO 连接 Y2 32.768kHz ±20ppm 12.5pF 晶振，C28/C29 各 6pF 接 GND；U5 VDD 接 VBAT_IN，INT 输出进入电源唤醒网络。

- 参数与网络：`rtc=U5 RTC8563`；`crystal=Y2 32.768kHz ±20ppm 12.5pF`；`load_caps=C28/C29 6pF`；`supply=VBAT_IN`；`interrupt=INT`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 B1-C2 U5、Y2、C28/C29

## 音频

### 无源蜂鸣器驱动

M1 G9 的 beep 网络经 R25 470Ω、C27 10uF 驱动 Q5 SS8050 Y1，Q5 低侧控制 LS1 Buzzer；D7 1N4148WT 跨接驱动节点与 GND。

- 参数与网络：`host_gpio=G9 beep`；`base_network=R25 470Ω,C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`diode=D7 1N4148WT`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C1-D1 beep/LS1/Q5

## 传感器

### SCD40 电源与 I2C

U6 SCD40 的 SCL pin9 接 SCL1、SDA pin10 接 SDA1、GND pin6 接 GND，VDD/VDDH 接 +3.3V；C4 100nF、C24 1uF、C7 22uF 为 3.3V 去耦。

- 参数与网络：`part_number=SCD40`；`scl=pin9 SCL1`；`sda=pin10 SDA1`；`supply=+3.3V`；`ground=pin6 GND`；`caps=C4 100nF,C24 1uF,C7 22uF`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C3-D3 U6 SCD40

## 模拟电路

### VBAT_IN 电池检测

VBAT_IN 通过 R7/R8 各 1MΩ 分压形成 G14 电池检测网络，C25 100nF 从 G14 接 GND；M1 G14 连接该节点。

- 参数与网络：`input=VBAT_IN`；`divider=R7 1MΩ,R8 1MΩ`；`filter=C25 100nF`；`host_gpio=G14`
- 证据：图 d729b8d15c0f / 第 1 页 / 第 1 页网格 C1-D2 VBAT_IN/R7/R8/C25/G14 与 M1 G14

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Air Quality 系统架构 | `controller=M1 STAMP-S3-DIP-1.27`；`i2c=SDA1/SCL1`；`rtc=RTC8563`；`co2=SCD40`；`sensor_header=P3`；`display=J1 FPC-0.5-24P`；`power=TP4057,Q2/Q3/Q4,SY7088,SY8089` |
| 电源 | +5VIN 到 VBAT_IN 充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program=R17 2.3KΩ`；`caps=C15/C21 10uF`；`connector=P1 pin1 VBAT_IN,pin2 GND` |
| 电源 | VBAT_OUT 电源保持与唤醒 | `path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`usb_or=+5VIN via D1 SS34`；`rtc_wake=INT via D3 B5819WT`；`button_wake=WAKE via D4/D15 B5819WT`；`hold=HOLD -> Q4 LN2324DT2AG`；`pulldown=R23 100KΩ` |
| 电源 | VBAT_OUT 到 +5VOUT | `input=VBAT_OUT`；`converter=U3 SY7088`；`inductor=L4 1.5uH`；`diode=D8 SS34`；`output=+5VOUT`；`feedback=R16 52.3KΩ,R18 15KΩ` |
| 电源 | VBAT_OUT 到 +3.3V | `input=VBAT_OUT`；`converter=U4 SY8089`；`enable=3V3EN via R26 100KΩ`；`inductor=L5 4.7uH`；`output=+3.3V`；`feedback=R27 68KΩ,R28 15KΩ` |
| 总线 | SDA1/SCL1 共享 I2C 总线 | `controller=M1 StampS3`；`sda=G11 SDA1`；`scl=G12 SCL1`；`devices=U5 RTC8563,U6 SCD40,P3 sensor`；`pullups=R2/R3 15KΩ to +3.3V` |
| 时钟 | RTC8563 32.768kHz 时钟 | `rtc=U5 RTC8563`；`crystal=Y2 32.768kHz ±20ppm 12.5pF`；`load_caps=C28/C29 6pF`；`supply=VBAT_IN`；`interrupt=INT` |
| 传感器 | SCD40 电源与 I2C | `part_number=SCD40`；`scl=pin9 SCL1`；`sda=pin10 SDA1`；`supply=+3.3V`；`ground=pin6 GND`；`caps=C4 100nF,C24 1uF,C7 22uF` |
| 电源 | P3 传感器电源开关 | `input=+5VOUT`；`switch=U1 ME1502CM5G`；`enable=AirPwREN GPIO10`；`rset=R1 27KΩ`；`output=P3 pin1 VDD`；`header=pin2 GND,pin3 SDA1,pin4 SCL1,pin5 SEL GND,pin6 NC` |
| 总线 | 电子纸 SPI 与控制映射 | `busy=G1 -> J1 pin9`；`reset=G2 -> pin10`；`dc=G3 -> pin11`；`chip_select=G4 -> pin12`；`clock=G5 -> pin13 D0`；`mosi=G6 -> pin14 D1` |
| 电源 | 电子纸高低压网络 | `logic=J1 pin15/16 +3.3V,pin17 GND`；`driver=Q1 LN2324DT2AG,L1 10uH,D9-D11 B5819WT`；`positive=PEGH`；`negative=PEGL`；`display_rails=VGL,VGH,VSH,VSL,PREVGH,PREVGL,VCOM` |
| GPIO 与控制信号 | 用户按键、唤醒与复位 | `user_a=S2 USER_A GPIO0`；`user_b=S3 USER_B GPIO8`；`reset=S4 RST -> EN`；`wake=S1 WAKE -> D4/D15`；`esd=D12/D13 PESDNC2FD3V3B` |
| 音频 | 无源蜂鸣器驱动 | `host_gpio=G9 beep`；`base_network=R25 470Ω,C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`diode=D7 1N4148WT` |
| 接口 | J3 Grove I2C 接口 | `pin1=SCL GPIO15`；`pin2=SDA GPIO13`；`pin3=VCC selected`；`pin4=GND`；`selector=SW1 +5VOUT/+5VIN` |
| 模拟电路 | VBAT_IN 电池检测 | `input=VBAT_IN`；`divider=R7 1MΩ,R8 1MΩ`；`filter=C25 100nF`；`host_gpio=G14` |
| 总线地址 | SEN55、SCD40 与 RTC8563 I2C 地址 | `documented_sen55=0x69`；`documented_scd40=0x62`；`rtc8563=null`；`schematic_addresses=null` |
| 传感器 | 正文中的 SEN55/SCD40 测量能力 | `documented_sensors=SEN55,SCD40`；`documented_measurements=PM1.0,PM2.5,PM4,PM10,temperature,humidity,VOC,CO2`；`sen55_reference=null`；`accuracy=null`；`range=null`；`calibration=null` |
| 接口 | 电子纸型号与分辨率 | `documented_model=GDEY0154D67`；`documented_size=1.54 inch`；`documented_resolution=200x200`；`schematic_connector=J1 FPC-0.5-24P`；`refresh_time=null` |
| 电源 | 电池容量与充电边界 | `documented_battery=600mAh@3.7V`；`connector=P1`；`charger=TP4057`；`chemistry=null`；`protection=null`；`charge_current=null`；`termination_voltage=null` |
| 内存与 Flash | StampS3 Flash 容量 | `module=M1 STAMP-S3-DIP-1.27`；`documented_soc=ESP32S3FN8`；`documented_flash=8MB`；`module_internal_schematic=null` |

## 待确认事项

- `address.i2c-devices`：正文列出 SEN55 为 0x69、SCD40 为 0x62；原理图只显示 P3 传感器接口、U6 SCD40 和 U5 RTC8563 共享 SDA1/SCL1，没有任何 I2C 地址文字或总线扫描结果，RTC8563 地址也未标注。（证据：图 d729b8d15c0f / 第 1 页 / 第 1 页 U5 RTC8563、U6 SCD40、P3 与 SDA1/SCL1，图中无地址）
- `sensor.documented-air-measurements`：正文称 SEN55/SCD40 可测 PM1.0、PM2.5、PM4、PM10、温度、湿度、VOC 和 CO2；原理图只确认 SCD40 型号及 P3 接口，没有 SEN55 位号或测量范围、精度、响应时间和校准参数。（证据：图 d729b8d15c0f / 第 1 页 / 第 1 页 U6 SCD40 与 P3 Header6，图中无 SEN55 器件符号或性能表）
- `interface.documented-display`：正文称显示器为 GDEY0154D67、1.54 英寸、200x200；原理图只给出 J1 FPC-0.5-24P 的电气连接和电源网络，未标显示器型号、尺寸、分辨率、刷新时间或温度范围。（证据：图 d729b8d15c0f / 第 1 页 / 第 1 页右下 J1 FPC-0.5-24P，无显示器型号或分辨率文字）
- `power.documented-battery-capacity`：正文称电池为 600mAh@3.7V；原理图只显示 P1、VBAT_IN、TP4057 和电源路径，未标电池容量、化学体系、保护板、允许极性、充电电流、终止电压或温度监测。（证据：图 d729b8d15c0f / 第 1 页 / 第 1 页左上 P1/U2/VBAT_IN，图中无电池规格）
- `memory.documented-stamps3-flash`：正文称 StampS3 使用 ESP32S3FN8 和 8MB Flash；板级原理图只将 M1 标为 STAMP-S3-DIP-1.27，没有展开模组内部 SoC、Flash、时钟、射频或 USB 连接。（证据：图 d729b8d15c0f / 第 1 页 / 第 1 页 M1 仅显示 STAMP-S3-DIP-1.27 模组接口）
- `review.i2c-addresses`：请通过 datasheet 或总线扫描确认 SEN55=0x69、SCD40=0x62 以及 RTC8563 的实际地址。；原因：原理图未标任何从地址。
- `review.sensor-performance`：K131 当前 SEN55/SCD40 BOM、测量范围、精度、响应时间、校准和维护要求是什么？；原因：P3 接口和 SCD40 型号不能证明整机测量性能。
- `review.display-model`：J1 当前连接的电子纸是否确为 GDEY0154D67 1.54 英寸 200x200，其刷新和温度规格是什么？；原因：原理图只显示 FPC 电气接口。
- `review.battery-safety`：K131 量产电池的化学体系、600mAh@3.7V 容量、极性、保护板及 TP4057 充电参数是什么？；原因：原理图没有电池规格与充电安全边界。
- `review.stamps3-internals`：请用 StampS3 模组原理图或实机确认 ESP32S3FN8、8MB Flash、USB 和射频实现。；原因：本页只展示 StampS3 模组引脚，没有内部电路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d729b8d15c0f45734cb6e9509410c26ea3f520643065aa76ad8f0ed4c842daf1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0_sch_01.png` |

---

源文档：`zh_CN/core/Air_Quality.md`

源文档 SHA-256：`431f6ba26249458cc38b6f7acec59d7b5599cf9c03fef12d0bc3a3e99fe59c40`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
