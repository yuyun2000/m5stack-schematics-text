# StickC-Plus Watch Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC-Plus Watch Kit |
| SKU | K016-H |
| 产品 ID | `stickc-plus-watch-kit-cf5757c3c407` |
| 源文档 | `zh_CN/accessory/M5StickC Plus with Watch Accessories.md` |

## 概述

该本地资源展示一套以 ESP32-PICO-V3-02（U1）为主控、CH9102F（U2）负责 USB-UART 的 M5StickC PLUS2 电路。板上集成 TP4057 充电、电池路径、SY7088 升压 5V、SY8089 降压 3.3V、RTC8563、MPU-6886、SPM1423 数字麦克风、LCD FPC、蜂鸣器和红外发射链路。资源 URL 指向 M5StickC PLUS2，而产品清单名称为 StickC-Plus Watch Kit，因此该原理图与套装内实际主机版本的对应关系需要人工确认。

## 检索关键词

`StickC-Plus Watch Kit`、`K016-H`、`M5StickC PLUS2`、`ESP32-PICO-V3-02`、`CH9102F`、`TP4057`、`SY7088`、`SY8089`、`RTC8563`、`MPU-6886`、`0x68`、`SPM1423HM4H-B`、`USB_DU_P`、`USB_DU_N`、`UART_TXD`、`UART_RXD`、`SCL`、`SDA`、`VBAT_IN`、`VBAT_OUT`、`+5VOUT`、`+3V3OUT`、`GPIO39`、`GPIO37`、`GPIO19`、`GPIO34`、`GPIO0`、`32.768KHz`、`FPC0.5-8P`、`STICKIO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-V3-02 | 主控、Wi-Fi 射频和板级 GPIO 控制器 | 图 3cf5d67ad133 / 第 1 页 / 页面左上部 U1：ESP32-PICO-V3-02，LNA_IN、EN、GPIO0~39、UART、MTDI/MTCK/MTDO 等引脚 |
| E1 | Antenna | ESP32 2.4GHz 射频天线 | 图 3cf5d67ad133 / 第 1 页 / 页面左上角 E1 Antenna：经 L1 与 C1/C2 匹配网络连接 U1 LNA_IN |
| U2 | CH9102F | USB 到 UART 转换器，连接 USB_DU_P/USB_DU_N 与 UART_TXD/UART_RXD/DTR/RTS | 图 3cf5d67ad133 / 第 1 页 / 页面上部中央 U2：CH9102F，D+/D-、TXD/RXD、DTR/RTS、VBUS/REGIN/VDD 引脚 |
| Q1 | LMBT3904DW1T1G | CH9102F DTR/RTS 到 EN/IO0 的自动下载双晶体管 | 图 3cf5d67ad133 / 第 1 页 / 页面上部 U2 左侧 Q1：LMBT3904DW1T1G，输入 DTR/RTS，输出 EN/IO0 |
| U3 | FPC0.5-8P | LCD 屏幕 FPC 接口，承载 CS、SCK、MOSI、D/C、RST 与 VLED | 图 3cf5d67ad133 / 第 1 页 / 页面中部 U3：FPC0.5-8P，左侧 GPIO5/GPIO15/GPIO14/GPIO12 等网络，符号内 CS/SCK/MOSI/D-C/RST/VLED |
| U5 | TP4057 | +5VIN 到 VBAT_IN 的单节电池充电控制器 | 图 3cf5d67ad133 / 第 1 页 / 页面上部中右 U5：TP4057，VCC/BAT/CHRG/STDBY/PROG/GND 与 +5VIN、VBAT_IN 网络 |
| U6 | SY7088 | 由 VBAT_OUT 升压生成 +5VOUT 的开关电源 IC | 图 3cf5d67ad133 / 第 1 页 / 页面右上虚线框 U6：SY7088，VBAT_OUT 输入、LX/EN/FB/GND 与 5.3V-D20-+5VOUT 输出 |
| U7 | SY8089 | 由电池电源路径生成 +3V3OUT 的降压稳压器 | 图 3cf5d67ad133 / 第 1 页 / 页面右中虚线框 U7：SY8089，IN/EN/LX/FB/GND、L3 和 +3V3OUT 输出网络 |
| U9 | RTC8563 | I2C 实时时钟，使用 32.768KHz 晶振并由 VBAT_IN 供电 | 图 3cf5d67ad133 / 第 1 页 / 页面右下部 U9：RTC8563，OSCI/OSCO/INT/VSS/VDD/CLKOUT/SCL/SDA，引脚 8 接 VBAT_IN |
| Y1 | 32.768KHz ±20ppm 12.5pF | RTC8563 的低频时钟晶振 | 图 3cf5d67ad133 / 第 1 页 / 页面右下部 U9 左侧 Y1：32.768KHz ±20ppm 12.5pF，跨接 OSCI/OSCO |
| U10 | MPU-6886 | I2C 六轴惯性传感器，原理图标注 7-bit 地址 0x68 | 图 3cf5d67ad133 / 第 1 页 / 页面下部中央 U10：MPU-6886，SCL/SDA/INT/VDD/VDDIO，文字 I2C Addr(7-bit):0x68 |
| U11 | SPM1423HM4H-B | 数字麦克风，DAT 接 GPIO34、CLK 接 GPIO0 | 图 3cf5d67ad133 / 第 1 页 / 页面底部中央 U11：SPM1423HM4H-B，DAT-GPIO34、CLK-GPIO0、3V3/GND |
| LS1/Q2 | Buzzer / SS8050 Y1 | 由 GPIO2 控制的蜂鸣器驱动链路 | 图 3cf5d67ad133 / 第 1 页 / 页面中下部 LS1 Buzzer 与 Q2 SS8050 Y1：GPIO2 经驱动器件控制蜂鸣器到 GND |
| IR1/Q5 | IR LED / SS8050 Y1 | 由 GPIO19 控制的红外发射链路 | 图 3cf5d67ad133 / 第 1 页 / 页面上部中右 IR1、R30、Q5 SS8050 Y1：VBAT_OUT 经 R30/IR1/Q5 至 GND，Q5 受 GPIO19 控制 |
| S1/S2 | SW-PB | 分别连接 GPIO39 和 GPIO37 的用户按键 | 图 3cf5d67ad133 / 第 1 页 / 页面中左部 S1/S2：SW-PB 分别连接 GPIO39/GPIO37 与 GND，并配 D5/D6 防护 |
| S3/Q7 | SW-PB / SI2302 N SOT-23 | WAKE/HOLD 电源保持与按键控制网络 | 图 3cf5d67ad133 / 第 1 页 / 页面中右部 S3、D23/D25、Q7：WAKE、HOLD 和 SI2302 N SOT-23 电源控制网络 |
| P1 | STICKIO | 6 Pin 扩展接口，引出 GND、+5VOUT、GPIO26、GPIO0、VBAT_N、3V3 | 图 3cf5d67ad133 / 第 1 页 / 页面上部中左 P1 STICKIO：1~6 脚与 GND/+5VOUT/GPIO26/GPIO0/VBAT_N/3V3 |
| P2 | Header 4 | Grove/I2C 接口，引出 SCL、SDA、+5VOUT、GND | 图 3cf5d67ad133 / 第 1 页 / 页面中部 P2 Header 4：1~4 脚对应 SCL/SDA/+5VOUT/GND |
| J1 | PH2.0-4P | 4 Pin 扩展接口，引出 GPIO33、GPIO32、+5VOUT、GND | 图 3cf5d67ad133 / 第 1 页 / 页面中部 J1 PH2.0-4P：1~4 脚对应 GPIO33/GPIO32/+5VOUT/GND |
| J2 | Header 2 | 电池输入连接器，连接 VBAT_IN 与 GND | 图 3cf5d67ad133 / 第 1 页 / 页面中部 J2 Header 2：1 脚 VBAT_IN，2 脚 GND |

## 系统结构

### 本地原理图硬件架构

该页以 U1 ESP32-PICO-V3-02 为主控，集成 U2 CH9102F、U5 TP4057、U6 SY7088、U7 SY8089、U9 RTC8563、U10 MPU-6886、U11 数字麦克风以及 LCD、蜂鸣器和红外接口。

- 参数与网络：`mcu=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`charger=U5 TP4057`；`power=U6 SY7088,U7 SY8089`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`microphone=U11 SPM1423HM4H-B`
- 证据：图 3cf5d67ad133 / 第 1 页 / 整页：U1/U2/U5/U6/U7/U9/U10/U11 与外设功能块

## 电源

### U5 TP4057

U5 VCC 接 +5VIN，BAT 输出 VBAT_IN，PROG 经 R26 3KΩ 接 GND，C20 10uF 从 VBAT_IN 接 GND；CHRG/STDBY 引脚连接状态网络。

- 参数与网络：`input=+5VIN`；`battery_node=VBAT_IN`；`program_resistor=R26 3KΩ`；`battery_capacitor=C20 10uF`；`status=CHRG,STDBY`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面上部中右 U5 TP4057：VCC/BAT/PROG/CHRG/STDBY 与 R26/C20

### U6 SY7088

U6 的输入连接 VBAT_OUT，开关网络经 L2 3015 1.5uH 升压到标注 5.3V 的节点，再经 D20 SS34 输出 +5VOUT。

- 参数与网络：`input=VBAT_OUT`；`inductor=L2 3015 1.5uH`；`intermediate=5.3V`；`diode=D20 SS34`；`output=+5VOUT`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面右上 U6 虚线框：VBAT_OUT、L2、U6 SY7088、5.3V、D20、+5VOUT

### U7 SY8089

U7 的开关输出经 L3 3015 4.7uH 形成 +3V3OUT，R32 68KΩ 与 R33 15KΩ 构成反馈分压，C21 22uF 和 C22 100nF 接在输出与 GND 之间。

- 参数与网络：`regulator=U7 SY8089`；`inductor=L3 3015 4.7uH`；`feedback=R32 68KΩ,R33 15KΩ`；`output_caps=C21 22uF,C22 100nF`；`output=+3V3OUT`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面右中 U7 虚线框：SY8089、L3、R32/R33、C21/C22 与 +3V3OUT

### J2 电池接口

J2 Header 2 的 1 脚连接 VBAT_IN，2 脚连接 GND；C35 10uF 从 VBAT_IN 接 GND。

- 参数与网络：`pin_1=VBAT_IN`；`pin_2=GND`；`capacitor=C35 10uF`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中部 J2 Header 2 与 C35：VBAT_IN/GND

## 接口

### P1 STICKIO

P1 的 1 脚接 GND，2 脚接 +5VOUT，3 脚接 GPIO26，4 脚接 GPIO0，5 脚接 VBAT_N，6 脚接 3V3。

- 参数与网络：`pin_1=GND`；`pin_2=+5VOUT`；`pin_3=GPIO26`；`pin_4=GPIO0`；`pin_5=VBAT_N`；`pin_6=3V3`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面上部中左 P1 STICKIO：1~6 脚与左侧网络标注

### P2 Header 4

P2 的 1 脚接 SCL，2 脚接 SDA，3 脚接 +5VOUT，4 脚接 GND。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VOUT`；`pin_4=GND`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中部 P2 Header 4：SCL/SDA/+5VOUT/GND 与 1~4 脚

### J1 PH2.0-4P

J1 的 1 脚接 GPIO33，2 脚接 GPIO32，3 脚接 +5VOUT，4 脚接 GND。

- 参数与网络：`pin_1=GPIO33`；`pin_2=GPIO32`；`pin_3=+5VOUT`；`pin_4=GND`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中部 J1 PH2.0-4P：GPIO33/GPIO32/+5VOUT/GND 与 1~4 脚

### U3 LCD FPC

U3 FPC0.5-8P 的显示控制网络包含 GPIO5-CS、GPIO15-SCK、GPIO14-MOSI、GPIO12-D/C，并引出 RST 和 VLED。

- 参数与网络：`CS=GPIO5`；`SCK=GPIO15`；`MOSI=GPIO14`；`D_C=GPIO12`；`other=RST,VLED`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中部 U3 FPC0.5-8P：左侧 GPIO 网络与符号内 CS/SCK/MOSI/D-C/RST/VLED

## 总线

### SCL/SDA I2C 总线

SCL/SDA 同名网络连接 P2、U9 RTC8563 和 U10 MPU-6886。

- 参数与网络：`external_port=P2`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`signals=SCL,SDA`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中部 P2、右下 U9、下部 U10 的 SCL/SDA 同名网络

## 总线地址

### U10 MPU-6886

原理图明确标注 MPU-6886 的 7-bit I2C 地址为 0x68。

- 参数与网络：`address=0x68`；`bus=SCL/SDA`；`format=7-bit`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面下部 U10 下方蓝色文字：I2C Addr(7-bit): 0x68

## GPIO 与控制信号

### S1/S2 用户按键

S1 将 GPIO39 按下接至 GND，S2 将 GPIO37 按下接至 GND；D5、D6 分别并接对应按键网络到 GND。

- 参数与网络：`button_1=S1 GPIO39-GND`；`button_2=S2 GPIO37-GND`；`protection=D5,D6`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中左部 S1/S2 与 D5/D6：GPIO39/GPIO37 到 GND

### WAKE/HOLD 电源控制

S3 SW-PB 连接 WAKE 控制网络；HOLD 经 D25 与 Q7 SI2302 N SOT-23 形成电源保持路径，Q7 另有 R34 100KΩ 到 GND。

- 参数与网络：`button=S3 SW-PB`；`wake_net=WAKE`；`hold_net=HOLD`；`mosfet=Q7 SI2302 N SOT-23`；`pulldown=R34 100KΩ`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中右部 S3/D23/D25/Q7/R34：WAKE/HOLD 电源控制网络

## 时钟

### U9 RTC8563

Y1 32.768KHz ±20ppm 12.5pF 跨接 U9 OSCI/OSCO，C26 和 C28 各 6.0pF 从 OSCI/OSCO 接 GND；U9 VDD 接 VBAT_IN。

- 参数与网络：`crystal=Y1 32.768KHz ±20ppm 12.5pF`；`load_caps=C26 6.0pF,C28 6.0pF`；`rtc=U9 RTC8563`；`supply=VBAT_IN`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面右下部 U9/Y1/C26/C28：OSCI/OSCO、VBAT_IN 与晶振负载网络

## 复位

### EN/IO0 自动下载

CH9102F 的 DTR/RTS 连接 Q1 LMBT3904DW1T1G，Q1 输出 EN 和 IO0；C3 10uF 从 EN 接 GND。

- 参数与网络：`inputs=DTR,RTS`；`transistor=Q1 LMBT3904DW1T1G`；`outputs=EN,IO0`；`en_capacitor=C3 10uF`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面上部 U1/U2 之间：Q1 交叉晶体管、DTR/RTS、EN/IO0 和 C3

## 音频

### LS1 Buzzer

LS1 蜂鸣器通过 Q2 SS8050 Y1 低侧驱动到 GND，Q2 控制路径来自 GPIO2。

- 参数与网络：`buzzer=LS1`；`driver=Q2 SS8050 Y1`；`control=GPIO2`；`return=GND`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面中下部 LS1/Q2/D14/D19：GPIO2 控制 Q2，Q2 驱动 Buzzer

### U11 SPM1423HM4H-B

U11 的 DAT 接 GPIO34，CLK 接 GPIO0，3V3 接 +3.3V，GND 引脚接地；SELECT 端接地。

- 参数与网络：`data=GPIO34`；`clock=GPIO0`；`supply=+3.3V`；`select=GND`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面底部 U11：DAT/CLK/3V3/GND/SELECT 引脚和 GPIO34/GPIO0/+3.3V/GND 网络

## 射频

### E1 到 U1 LNA_IN

E1 Antenna 经 L1 1.8nH 串联连接 U1 LNA_IN，C1 2.0pF 和 C2 2.4pF 分别在串联路径两侧对 GND。

- 参数与网络：`antenna=E1`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF,C2 2.4pF`；`mcu_pin=U1 LNA_IN`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面左上角 E1-C1-L1-C2-U1 LNA_IN 匹配网络

### IR1 红外发射

VBAT_OUT 经 R30 300R、IR1 和 Q5 SS8050 Y1 串联到 GND，Q5 控制网络连接 GPIO19。

- 参数与网络：`supply=VBAT_OUT`；`resistor=R30 300R`；`emitter=IR1`；`driver=Q5 SS8050 Y1`；`control=GPIO19`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面上部中右 VBAT_OUT-R30-IR1-Q5-GND 与 GPIO19 控制线

## 调试与烧录

### U2 CH9102F

U2 的 D+、D- 连接 USB_DU_P、USB_DU_N，UART_TXD/UART_RXD 连接 U1 UART0RXD/UART0TXD，DTR/RTS 进入 Q1 自动下载网络。

- 参数与网络：`usb=USB_DU_P,USB_DU_N`；`uart=UART_TXD,UART_RXD`；`handshake=DTR,RTS`；`auto_download=Q1 LMBT3904DW1T1G`
- 证据：图 3cf5d67ad133 / 第 1 页 / 页面上部中央 U2 与左侧 U1 UART0RXD/UART0TXD、Q1 EN/IO0 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 本地原理图硬件架构 | `mcu=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`charger=U5 TP4057`；`power=U6 SY7088,U7 SY8089`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`microphone=U11 SPM1423HM4H-B` |
| 射频 | E1 到 U1 LNA_IN | `antenna=E1`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF,C2 2.4pF`；`mcu_pin=U1 LNA_IN` |
| 调试与烧录 | U2 CH9102F | `usb=USB_DU_P,USB_DU_N`；`uart=UART_TXD,UART_RXD`；`handshake=DTR,RTS`；`auto_download=Q1 LMBT3904DW1T1G` |
| 复位 | EN/IO0 自动下载 | `inputs=DTR,RTS`；`transistor=Q1 LMBT3904DW1T1G`；`outputs=EN,IO0`；`en_capacitor=C3 10uF` |
| 接口 | P1 STICKIO | `pin_1=GND`；`pin_2=+5VOUT`；`pin_3=GPIO26`；`pin_4=GPIO0`；`pin_5=VBAT_N`；`pin_6=3V3` |
| 接口 | P2 Header 4 | `pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VOUT`；`pin_4=GND` |
| 接口 | J1 PH2.0-4P | `pin_1=GPIO33`；`pin_2=GPIO32`；`pin_3=+5VOUT`；`pin_4=GND` |
| 接口 | U3 LCD FPC | `CS=GPIO5`；`SCK=GPIO15`；`MOSI=GPIO14`；`D_C=GPIO12`；`other=RST,VLED` |
| GPIO 与控制信号 | S1/S2 用户按键 | `button_1=S1 GPIO39-GND`；`button_2=S2 GPIO37-GND`；`protection=D5,D6` |
| 音频 | LS1 Buzzer | `buzzer=LS1`；`driver=Q2 SS8050 Y1`；`control=GPIO2`；`return=GND` |
| 射频 | IR1 红外发射 | `supply=VBAT_OUT`；`resistor=R30 300R`；`emitter=IR1`；`driver=Q5 SS8050 Y1`；`control=GPIO19` |
| 音频 | U11 SPM1423HM4H-B | `data=GPIO34`；`clock=GPIO0`；`supply=+3.3V`；`select=GND` |
| 总线 | SCL/SDA I2C 总线 | `external_port=P2`；`rtc=U9 RTC8563`；`imu=U10 MPU-6886`；`signals=SCL,SDA` |
| 总线地址 | U10 MPU-6886 | `address=0x68`；`bus=SCL/SDA`；`format=7-bit` |
| 时钟 | U9 RTC8563 | `crystal=Y1 32.768KHz ±20ppm 12.5pF`；`load_caps=C26 6.0pF,C28 6.0pF`；`rtc=U9 RTC8563`；`supply=VBAT_IN` |
| 电源 | U5 TP4057 | `input=+5VIN`；`battery_node=VBAT_IN`；`program_resistor=R26 3KΩ`；`battery_capacitor=C20 10uF`；`status=CHRG,STDBY` |
| 电源 | U6 SY7088 | `input=VBAT_OUT`；`inductor=L2 3015 1.5uH`；`intermediate=5.3V`；`diode=D20 SS34`；`output=+5VOUT` |
| 电源 | U7 SY8089 | `regulator=U7 SY8089`；`inductor=L3 3015 4.7uH`；`feedback=R32 68KΩ,R33 15KΩ`；`output_caps=C21 22uF,C22 100nF`；`output=+3V3OUT` |
| 电源 | J2 电池接口 | `pin_1=VBAT_IN`；`pin_2=GND`；`capacitor=C35 10uF` |
| GPIO 与控制信号 | WAKE/HOLD 电源控制 | `button=S3 SW-PB`；`wake_net=WAKE`；`hold_net=HOLD`；`mosfet=Q7 SI2302 N SOT-23`；`pulldown=R34 100KΩ` |
| 系统结构 | 产品与原理图版本对应关系 | `manifest_product=StickC-Plus Watch Kit`；`sku=K016-H`；`asset_path_product=M5StickC PLUS2`；`schematic_title_block=null` |

## 待确认事项

- `system.product-schematic-version`：产品清单名称为 StickC-Plus Watch Kit，但资源 URL 位于 M5StickC PLUS2 路径；该页未提供能把此原理图明确归属到 K016-H 套装内主机版本的标题栏信息。（证据：图 3cf5d67ad133 / 第 1 页 / 整页：原理图包含 PLUS2 架构器件但无产品型号/版本标题栏；资源 URL 中包含 M5StickC PLUS2）
- `review.product-schematic-version`：K016-H StickC-Plus Watch Kit 实际随附的是哪一代 M5StickC Plus，当前 M5StickC PLUS2 原理图是否适用于该 SKU？；原因：产品清单名称/SKU 与资源 URL 的产品代际不一致；错误套用 PLUS2 电路会导致主控、电源和外设描述与实物不符。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3cf5d67ad13358536fbb624fecf0e3cc6f67a0ddb4d0bf91c82a73506160c741` | `https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC PLUS2/img-7381263f-5e60-48c2-8275-924b46e698f3.png` |

---

源文档：`zh_CN/accessory/M5StickC Plus with Watch Accessories.md`

源文档 SHA-256：`069049ea841eef1aa6644c7655d71b34dbecbd369ffd52a9616f72215cf211c1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
