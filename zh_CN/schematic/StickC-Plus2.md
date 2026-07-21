# StickC-Plus2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC-Plus2 |
| SKU | K016-P2 |
| 产品 ID | `stickc-plus2-84b7dafe0db8` |
| 源文档 | `zh_CN/core/M5StickC PLUS2.md` |

## 概述

StickC-Plus2 以 U1 ESP32-PICO-V3-02 为主控，连接 SPI TFT、MPU-6886、RTC8563、SPM1423 数字麦克风、蜂鸣器、红外/红 LED、按键和扩展接口。USB-C 同时提供电源及经 CH9102F 转换的下载 UART，GPIO0/EN 由 RTS/DTR 自动下载电路控制。电源链由 TP4057 充电器、电池/USB 电源汇合与保持电路、SY7088 5 V 升压和 SY8089 3.3 V 降压组成。

## 检索关键词

`StickC-Plus2`、`K016-P2`、`ESP32-PICO-V3-02`、`CH9102F`、`TP4057`、`SY7088`、`SY8089`、`MPU-6886`、`0x68`、`SPM1423HM4H-B`、`RTC8563`、`USB Type-C`、`GH2.0-4P`、`STICKIO`、`TFT_MOSI`、`TFT_CLK`、`TFT_DC`、`TFT_RST`、`TFT_CS`、`GPIO27`、`GPIO19`、`GPIO38`、`GPIO37`、`GPIO39`、`GPIO35`、`GPIO4 HOLD`、`SCL GPIO22`、`SDA GPIO21`、`+5VOUT`、`+3V3OUT`、`VBAT_IN`、`VBAT_OUT`、`WAKE`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-V3-02 | 系统主控，连接射频、显示、I2C 设备、麦克风、按键、UART 和电源控制 | 图 a44b23c200a4 / 第 1 页 / A2-B2，U1 ESP32-PICO-V3-02 及全部 GPIO 网络 |
| E1 | Antenna | ESP32 射频天线，带 L/C 匹配网络 | 图 a44b23c200a4 / 第 1 页 / A1，E1 Antenna、L1 1.8nH、C1 2.0pF、C2 2.4pF |
| U2 | CH9102F | USB 转 UART 下载与调试桥接器 | 图 a44b23c200a4 / 第 1 页 / A4-B4，U2 CH9102F、USB_DU_P/N、URX/UTX、DTR/RTS |
| J2 | USB-TYPEC | 主 USB-C 电源和 USB 2.0 数据连接器 | 图 a44b23c200a4 / 第 1 页 / D1-D2，J2 USB-TYPEC、VBUS、USB_DU_P/N、CC1/CC2 |
| Q1 | LMBT3904DW1T1G | 由 CH9102F DTR/RTS 控制 ESP32 EN/GPIO0 的自动下载双晶体管 | 图 a44b23c200a4 / 第 1 页 / A3，Q1 LMBT3904DW1T1G、DTR/RTS/EN/GPIO0 |
| P1 | STICKIO | 8 针 HAT 扩展接口，提供电源及 GPIO26/GPIO36/GPIO0 | 图 a44b23c200a4 / 第 1 页 / A3-B3，P1 STICKIO pins 1-8 |
| J1 | GH2.0-4P | 四针外设扩展接口，提供 GPIO33/GPIO32、5 V 和 GND | 图 a44b23c200a4 / 第 1 页 / C4，J1 GH2.0-4P，GPIO33/GPIO32/+5VOUT/GND |
| P2 | Header 4 | 四针 I2C 扩展接口，提供 SCL/SDA、5 V 和 GND | 图 a44b23c200a4 / 第 1 页 / C3，P2 Header 4，SCL/SDA/+5VOUT/GND |
| U3 | FPC-0.5-8P | TFT 显示屏 SPI、控制和背光连接器 | 图 a44b23c200a4 / 第 1 页 / C4-D4，U3 FPC-0.5-8P，CS/VCC/SCK/MOSI/D-C/RST/GND/VLED |
| U4 | SGM2578 / WS4622C-4/TR | GPIO27 控制的 TFT 背光负载开关 | 图 a44b23c200a4 / 第 1 页 / D4，U4 双行标注 SGM2578 与 WS4622C-4/TR，EN=GPIO27 |
| LS1/Q2 | Buzzer / SS8050 Y1 | GPIO2 驱动的无源蜂鸣器及低边晶体管 | 图 a44b23c200a4 / 第 1 页 / D3，LS1 Buzzer、Q2 SS8050 Y1、GPIO2 |
| S1/S2 | SW-PB | GPIO39 与 GPIO37 用户按键 | 图 a44b23c200a4 / 第 1 页 / C2，S1 GPIO39、S2 GPIO37 与 D5/D8 ESD |
| U5 | TP4057 | 由 +5VIN 供电的锂电池充电器 | 图 e56bc0b20196 / 第 1 页 / A1-B1，U5 TP4057、+5VIN、VBAT_IN、R26 3.3K |
| Q3/Q4 | LP3218DT1G | 电池输入隔离和系统上电保持 MOSFET | 图 e56bc0b20196 / 第 1 页 / A2-B2，Q3/Q4 LP3218DT1G，VBAT_IN/+VIN/VBAT_OUT |
| U6 | SY7088 | 由 VBAT_OUT 升压并经 D20 输出 +5VOUT | 图 e56bc0b20196 / 第 1 页 / A3-B4，U6 SY7088、L2、5.3V、D20、+5VOUT |
| U7 | SY8089 | 由 VBAT_OUT 降压生成 +3V3OUT | 图 e56bc0b20196 / 第 1 页 / B3-C4，U7 SY8089、L3、+3V3OUT |
| S3/Q7 | SW-PB / SI2302 N SOT-23 | WAKE 按键和 GPIO4 HOLD 电源保持控制 | 图 e56bc0b20196 / 第 1 页 / B2-C2，S3、WAKE、D22/D23、Q7、HOLD |
| D24/IR1/Q5 | LED / IR / SS8050 Y1 | GPIO19 共用的红色指示 LED 与红外发射驱动 | 图 e56bc0b20196 / 第 1 页 / A3-B3，D24、IR1、Q5 SS8050 Y1、GPIO19 |
| U8/LED1 | GS321 / GREEN | WAKE/5VOUT 比较与 3V3EN、绿色状态 LED 电路 | 图 e56bc0b20196 / 第 1 页 / D1-D2，U8 GS321、LED1 GREEN、WAKE、3V3EN |
| U9 | RTC8563 | 电池供电 I2C RTC，INT 参与唤醒 | 图 e56bc0b20196 / 第 1 页 / D4，U9 RTC8563、SCL/SDA/INT、VBAT_IN |
| Y1 | 32.768KHz ±20ppm 12.5pF | RTC 低速时钟晶体 | 图 e56bc0b20196 / 第 1 页 / D3，Y1 32.768KHz ±20ppm 12.5pF、C26/C28 6.0pF |
| U10 | MPU-6886 | I2C 惯性传感器，原理图标注 7-bit 地址 0x68 | 图 133d1dbcee40 / 第 1 页 / B2-B3，U10 MPU-6886，I2C Addr(7-bit): 0x68 |
| U11 | SPM1423HM4H-B | 数字麦克风，GPIO0 时钟、GPIO34 数据 | 图 133d1dbcee40 / 第 1 页 / C2-C3，U11 SPM1423HM4H-B、GPIO34 DAT、GPIO0 CLK |
| F1 | 6V/1A/PPTC | USB VBUS 输入过流保护 | 图 a44b23c200a4 / 第 1 页 / D2，F1 6V/1A/PPTC、VBUS、D15 SS34 |
| D3/D4/D6/D7/D9/D10/D11/D12/D13/D16/D17/D18/D25 | PESDNC2FD3V3B / PESDNC2FD5VB | 电源、USB、按键和外部 GPIO 的 ESD 保护器件 | 图 a44b23c200a4 / 第 1 页 / C1、C4、D1，PESDNC2F 系列保护器件; 图 e56bc0b20196 / 第 1 页 / B2，D25 PESDNC2FD3V3B 保护 WAKE |

## 系统结构

### 系统架构

U1 ESP32-PICO-V3-02 作为主控，连接 TFT、MPU-6886、RTC8563、SPM1423 数字麦克风、CH9102F、按键、蜂鸣器、红外/LED 和扩展接口。

- 参数与网络：`main_controller=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`imu=U10 MPU-6886`；`rtc=U9 RTC8563`；`microphone=U11 SPM1423HM4H-B`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 主控及显示、UART、GPIO 网络; 图 e56bc0b20196 / 第 1 页 / 电源、RTC、红外与唤醒电路; 图 133d1dbcee40 / 第 1 页 / U10 MPU-6886 与 U11 SPM1423HM4H-B

## 电源

### TFT 背光电源

U4 将 +3.3 V 切换到 U3 VLED，EN 由 GPIO27 控制。

- 参数与网络：`reference=U4`；`input=+3.3V`；`output=U3 pin 8 VLED`；`enable=GPIO27`
- 证据：图 a44b23c200a4 / 第 1 页 / D4，U4 VIN/VOUT/EN 到 U3 VLED

### USB 输入路径

J2 VBUS 经 F1 6V/1A/PPTC 和 D15 SS34 形成 +5VIN，D16 PESDNC2FD5VB 对 +5VIN 提供 ESD 钳位。

- 参数与网络：`input=VBUS`；`fuse=F1 6V/1A/PPTC`；`diode=D15 SS34`；`output=+5VIN`；`esd=D16 PESDNC2FD5VB`
- 证据：图 a44b23c200a4 / 第 1 页 / D2，F1/D15/D16，VBUS 到 +5VIN

### 电池充电

U5 TP4057 由 +5VIN 经 R21 0.8 Ω 供电，BAT 输出连接 VBAT_IN，PROG 通过 R26 3.3 kΩ 接地。

- 参数与网络：`reference=U5`；`part_number=TP4057`；`input=+5VIN`；`battery_net=VBAT_IN`；`input_resistor=R21 0.8R`；`program_resistor=R26 3.3K`
- 证据：图 e56bc0b20196 / 第 1 页 / A1-B1，U5/R21/R26/VBAT_IN

### USB/电池电源汇合

Q3 将 VBAT_IN 接入 +VIN，Q4 将 +VIN 接入 VBAT_OUT；USB +5VIN 还可经 D21 SS34 直接给 VBAT_OUT 供电。

- 参数与网络：`battery_path=VBAT_IN -> Q3 LP3218DT1G -> +VIN -> Q4 LP3218DT1G -> VBAT_OUT`；`usb_bypass=+5VIN -> D21 SS34 -> VBAT_OUT`
- 证据：图 e56bc0b20196 / 第 1 页 / A1-B3，Q3/Q4/D21，VBAT_IN/+VIN/VBAT_OUT/+5VIN

### 上电唤醒与保持

S3 产生 WAKE，RTC INT 经 D22、WAKE 经 D23 汇入 Q4 控制节点；GPIO4 HOLD 通过 Q7 维持或释放系统电源。

- 参数与网络：`button=S3/WAKE`；`rtc_alarm=INT via D22 B5819WT`；`wake_diode=D23 B5819WT`；`hold=GPIO4/HOLD via Q7 SI2302`；`power_switch=Q4 LP3218DT1G`
- 证据：图 e56bc0b20196 / 第 1 页 / B2-C2，INT/D22/S3/WAKE/D23/HOLD/Q7/Q4

### 5 V 输出

U6 SY7088 从 VBAT_OUT 升压到标注 5.3 V 的节点，再经 D20 SS34 生成 +5VOUT。

- 参数与网络：`reference=U6`；`part_number=SY7088`；`input=VBAT_OUT`；`inductor=L2 3015 1.5uH`；`pre_diode_voltage=5.3V`；`diode=D20 SS34`；`output=+5VOUT`
- 证据：图 e56bc0b20196 / 第 1 页 / A3-B4，U6/L2/R25/R27/D20

### 3.3 V 输出

U7 SY8089 从 VBAT_OUT 降压，经 L3 3015 4.7 µH 生成 +3V3OUT，EN 网络标为 3V3EN。

- 参数与网络：`reference=U7`；`part_number=SY8089`；`input=VBAT_OUT`；`enable=3V3EN`；`inductor=L3 3015 4.7uH`；`output=+3V3OUT`
- 证据：图 e56bc0b20196 / 第 1 页 / B3-C4，U7/L3/R31/R32/R33，3V3EN/+3V3OUT

## 接口

### TFT 接口

U3 八针 FPC 提供 CS、VCC、SCK、MOSI、D/C、RST、GND 和 VLED，逻辑电源为 +3.3 V。

- 参数与网络：`reference=U3`；`part_number=FPC-0.5-8P`；`pin1=GPIO5/CS`；`pin2=+3.3V/VCC`；`pin3=GPIO13/SCK`；`pin4=GPIO15/MOSI`；`pin5=GPIO14/D-C`；`pin6=GPIO12/RST`；`pin7=GND`；`pin8=VLED`
- 证据：图 a44b23c200a4 / 第 1 页 / C4-D4，U3 FPC-0.5-8P pins 1-8

### USB Type-C

J2 引出 USB_DU_P/N 和 VBUS，CC1/CC2 分别通过 R18/R20 5.1 kΩ 接地。

- 参数与网络：`reference=J2`；`dp=USB_DU_P`；`dn=USB_DU_N`；`vbus=VBUS`；`cc1=R18 5.1K/1% to GND`；`cc2=R20 5.1K/1% to GND`
- 证据：图 a44b23c200a4 / 第 1 页 / D1-D2，J2 USB-TYPEC、R18/R20

### STICKIO 扩展接口

P1 pins 1-8 依次为 GND、+5VOUT、GPIO26、GPIO36、GPIO0、VBAT_IN、+3.3V、+5VIN。

- 参数与网络：`pin1=GND`；`pin2=+5VOUT`；`pin3=GPIO26`；`pin4=GPIO36`；`pin5=GPIO0`；`pin6=VBAT_IN`；`pin7=+3.3V`；`pin8=+5VIN`
- 证据：图 a44b23c200a4 / 第 1 页 / A3-B3，P1 STICKIO pins 1-8

### GH2.0-4P 扩展接口

J1 pins 1-4 依次为 GPIO33、GPIO32、+5VOUT、GND，信号与电源均有邻近保护/去耦。

- 参数与网络：`reference=J1`；`pin1=GPIO33`；`pin2=GPIO32`；`pin3=+5VOUT`；`pin4=GND`；`gpio_protection=D12/D13 PESDNC2FD3V3B`；`power_protection=PESDNC2FD5VB`
- 证据：图 a44b23c200a4 / 第 1 页 / C4，J1、D12、D13 与 5V ESD 器件

### 外部 I2C 接口

P2 pins 1-4 依次为 SCL、SDA、+5VOUT、GND。

- 参数与网络：`reference=P2`；`pin1=SCL/GPIO22`；`pin2=SDA/GPIO21`；`pin3=+5VOUT`；`pin4=GND`
- 证据：图 a44b23c200a4 / 第 1 页 / C3，P2 Header 4

## 总线

### 系统 I2C

ESP32 GPIO22/SCL 与 GPIO21/SDA 连接 U9 RTC8563、U10 MPU-6886 和 P2 外部 I2C 接口。

- 参数与网络：`controller=U1 ESP32-PICO-V3-02`；`scl=GPIO22/SCL`；`sda=GPIO21/SDA`；`devices=U9 RTC8563; U10 MPU-6886; P2 Header 4`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 GPIO22 SCL、GPIO21 SDA 与 P2; 图 e56bc0b20196 / 第 1 页 / U9 RTC8563 SCL/SDA; 图 133d1dbcee40 / 第 1 页 / U10 MPU-6886 SCL/SDA

### TFT SPI 与控制信号

TFT 使用 GPIO15 MOSI、GPIO13 SCK、GPIO5 CS，并由 GPIO14 D/C、GPIO12 RST 控制。

- 参数与网络：`mosi=GPIO15`；`sck=GPIO13`；`cs=GPIO5`；`dc=GPIO14`；`reset=GPIO12`；`miso=null`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 GPIO5/12/13/14/15 与 U3 TFT FPC

## 总线地址

### MPU-6886 I2C 地址

原理图直接标注 U10 MPU-6886 的 7-bit I2C 地址为 0x68，AD0/SDO 接地。

- 参数与网络：`reference=U10`；`part_number=MPU-6886`；`address_7bit=0x68`；`ad0_sdo=GND`
- 证据：图 133d1dbcee40 / 第 1 页 / U10 下方 I2C Addr(7-bit): 0x68，pin 9 AD0/SDO 接地

## GPIO 与控制信号

### 用户按键 GPIO

S1 连接 GPIO39，S2 连接 GPIO37，S3 连接 WAKE；WAKE 对应 ESP32 GPIO35。

- 参数与网络：`S1=GPIO39`；`S2=GPIO37`；`S3=WAKE/GPIO35`；`pullups=R1/R2/R6 10K to +3.3V`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 GPIO35/37/39 与 S1/S2，D1 GPIO35-WAKE; 图 e56bc0b20196 / 第 1 页 / B2，S3 SW-PB 与 WAKE

### 电源保持 GPIO

ESP32 GPIO4 标为 HOLD，并驱动 Q7 SI2302 参与 Q4 系统电源保持控制。

- 参数与网络：`gpio=GPIO4`；`net=HOLD`；`transistor=Q7 SI2302 N SOT-23`；`controlled_switch=Q4 LP3218DT1G`
- 证据：图 a44b23c200a4 / 第 1 页 / U1 IO4/HOLD; 图 e56bc0b20196 / 第 1 页 / B2-C2，HOLD/Q7/Q4 电源保持链路

### 红外与红 LED 控制

GPIO19 驱动 Q5 SS8050 Y1，Q5 同时控制 D24 红 LED 与 IR1 红外发射器。

- 参数与网络：`gpio=GPIO19`；`transistor=Q5 SS8050 Y1`；`loads=D24 LED; IR1 IR`；`led_resistor=R30 300R`；`ir_resistor=R15 22R/1%`
- 证据：图 e56bc0b20196 / 第 1 页 / A3-B3，D24/IR1/R30/R15/Q5/GPIO19

## 时钟

### RTC 时钟

Y1 为 U9 RTC8563 提供 32.768 kHz、±20 ppm、12.5 pF 晶体时钟，C26/C28 均为 6.0 pF。

- 参数与网络：`reference=Y1`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load=12.5pF`；`capacitors=C26 6.0pF; C28 6.0pF`；`rtc=U9 RTC8563`
- 证据：图 e56bc0b20196 / 第 1 页 / D3-D4，Y1/C26/C28/U9 OSCI/OSCO

## 复位

### ESP32 复位与 BOOT

Q1 LMBT3904DW1T1G 接收 RTS/DTR，经 R3/R4 10 kΩ 驱动 EN 与 GPIO0，支持自动复位和下载模式选择。

- 参数与网络：`reference=Q1`；`part_number=LMBT3904DW1T1G`；`inputs=RTS; DTR`；`outputs=EN; GPIO0`；`resistors=R3 10K; R4 10K`
- 证据：图 a44b23c200a4 / 第 1 页 / A3，Q1/R3/R4/RTS/DTR/EN/GPIO0

## 保护电路

### 外部接口 ESD 保护

USB_DU_P/N、P1 外部电源/GPIO、J1 GPIO32/GPIO33 与 5 V、按键和 WAKE 均配置 PESDNC2F 系列保护器件。

- 参数与网络：`usb=D17/D18 PESDNC2FD3V3B`；`stickio=D3/D4/D6/D7/D9/D10/D11`；`grove=D12/D13 and PESDNC2FD5VB`；`buttons=D5/D8`；`wake=D25 PESDNC2FD3V3B`
- 证据：图 a44b23c200a4 / 第 1 页 / C1、C4、D1，PESDNC2FD3V3B/5VB 保护阵列; 图 e56bc0b20196 / 第 1 页 / D25 WAKE ESD 保护

## 音频

### 数字麦克风

U11 SPM1423HM4H-B 由 +3.3 V 供电，CLK 连接 GPIO0，DAT 连接 GPIO34，SELECT 接地。

- 参数与网络：`reference=U11`；`part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`select=GND`；`supply=+3.3V`
- 证据：图 133d1dbcee40 / 第 1 页 / C2-C3，U11 pins SELECT/DAT/CLK/3V3

### 蜂鸣器

GPIO2 经 R19 470 Ω 和 C12 10 µF 驱动 Q2 SS8050 Y1，Q2 低边开关控制 LS1 Buzzer。

- 参数与网络：`gpio=GPIO2`；`series_resistor=R19 470R`；`coupling_capacitor=C12 10uF`；`transistor=Q2 SS8050 Y1`；`load=LS1 Buzzer`
- 证据：图 a44b23c200a4 / 第 1 页 / D3，GPIO2/R19/C12/Q2/LS1

## 传感器

### 惯性传感器

U10 MPU-6886 由 +3.3 V 供电，通过 SCL/SDA 工作在 I2C 模式。

- 参数与网络：`reference=U10`；`part_number=MPU-6886`；`supply=+3.3V`；`scl=SCL`；`sda=SDA`
- 证据：图 133d1dbcee40 / 第 1 页 / B2-B3，U10 VDD/VDDIO/SCL/SDA/AD0

## 射频

### 主控射频天线

U1 LNA_IN 经 L1 1.8 nH 和 C1/C2 匹配网络连接 E1 Antenna。

- 参数与网络：`antenna=E1`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF; C2 2.4pF`；`soc_pin=U1 LNA_IN`
- 证据：图 a44b23c200a4 / 第 1 页 / A1-A2，E1/L1/C1/C2 到 U1 LNA_IN

## 调试与烧录

### USB-UART 下载接口

U2 CH9102F 将 USB_DU_P/N 转换为 URX/UTX，DTR/RTS 通过 Q1 控制 ESP32 EN 与 GPIO0。

- 参数与网络：`reference=U2`；`part_number=CH9102F`；`usb=USB_DU_P; USB_DU_N`；`uart=URX; UTX`；`handshake=DTR; RTS`；`auto_program=Q1 -> EN/GPIO0`
- 证据：图 a44b23c200a4 / 第 1 页 / A3-B4，U2 CH9102F 与 Q1 自动下载电路

## 模拟电路

### 电池电压采样

VBAT_IN 经 R40/R41 各 100 kΩ 分压到 GPIO38，并由 C42 100 nF 滤波。

- 参数与网络：`source=VBAT_IN`；`gpio=GPIO38`；`upper_resistor=R40 100K`；`lower_resistor=R41 100K`；`filter=C42 100nF`
- 证据：图 e56bc0b20196 / 第 1 页 / C1，VBAT_IN/R40/R41/GPIO38/C42

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统架构 | `main_controller=U1 ESP32-PICO-V3-02`；`usb_uart=U2 CH9102F`；`imu=U10 MPU-6886`；`rtc=U9 RTC8563`；`microphone=U11 SPM1423HM4H-B` |
| 射频 | 主控射频天线 | `antenna=E1`；`series_inductor=L1 1.8nH`；`shunt_capacitors=C1 2.0pF; C2 2.4pF`；`soc_pin=U1 LNA_IN` |
| 总线 | 系统 I2C | `controller=U1 ESP32-PICO-V3-02`；`scl=GPIO22/SCL`；`sda=GPIO21/SDA`；`devices=U9 RTC8563; U10 MPU-6886; P2 Header 4` |
| 总线地址 | MPU-6886 I2C 地址 | `reference=U10`；`part_number=MPU-6886`；`address_7bit=0x68`；`ad0_sdo=GND` |
| 传感器 | 惯性传感器 | `reference=U10`；`part_number=MPU-6886`；`supply=+3.3V`；`scl=SCL`；`sda=SDA` |
| 音频 | 数字麦克风 | `reference=U11`；`part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`select=GND`；`supply=+3.3V` |
| 音频 | 蜂鸣器 | `gpio=GPIO2`；`series_resistor=R19 470R`；`coupling_capacitor=C12 10uF`；`transistor=Q2 SS8050 Y1`；`load=LS1 Buzzer` |
| 接口 | TFT 接口 | `reference=U3`；`part_number=FPC-0.5-8P`；`pin1=GPIO5/CS`；`pin2=+3.3V/VCC`；`pin3=GPIO13/SCK`；`pin4=GPIO15/MOSI`；`pin5=GPIO14/D-C`；`pin6=GPIO12/RST`；`pin7=GND`；`pin8=VLED` |
| 总线 | TFT SPI 与控制信号 | `mosi=GPIO15`；`sck=GPIO13`；`cs=GPIO5`；`dc=GPIO14`；`reset=GPIO12`；`miso=null` |
| 电源 | TFT 背光电源 | `reference=U4`；`input=+3.3V`；`output=U3 pin 8 VLED`；`enable=GPIO27` |
| 接口 | USB Type-C | `reference=J2`；`dp=USB_DU_P`；`dn=USB_DU_N`；`vbus=VBUS`；`cc1=R18 5.1K/1% to GND`；`cc2=R20 5.1K/1% to GND` |
| 调试与烧录 | USB-UART 下载接口 | `reference=U2`；`part_number=CH9102F`；`usb=USB_DU_P; USB_DU_N`；`uart=URX; UTX`；`handshake=DTR; RTS`；`auto_program=Q1 -> EN/GPIO0` |
| 复位 | ESP32 复位与 BOOT | `reference=Q1`；`part_number=LMBT3904DW1T1G`；`inputs=RTS; DTR`；`outputs=EN; GPIO0`；`resistors=R3 10K; R4 10K` |
| 接口 | STICKIO 扩展接口 | `pin1=GND`；`pin2=+5VOUT`；`pin3=GPIO26`；`pin4=GPIO36`；`pin5=GPIO0`；`pin6=VBAT_IN`；`pin7=+3.3V`；`pin8=+5VIN` |
| 接口 | GH2.0-4P 扩展接口 | `reference=J1`；`pin1=GPIO33`；`pin2=GPIO32`；`pin3=+5VOUT`；`pin4=GND`；`gpio_protection=D12/D13 PESDNC2FD3V3B`；`power_protection=PESDNC2FD5VB` |
| 接口 | 外部 I2C 接口 | `reference=P2`；`pin1=SCL/GPIO22`；`pin2=SDA/GPIO21`；`pin3=+5VOUT`；`pin4=GND` |
| GPIO 与控制信号 | 用户按键 GPIO | `S1=GPIO39`；`S2=GPIO37`；`S3=WAKE/GPIO35`；`pullups=R1/R2/R6 10K to +3.3V` |
| GPIO 与控制信号 | 电源保持 GPIO | `gpio=GPIO4`；`net=HOLD`；`transistor=Q7 SI2302 N SOT-23`；`controlled_switch=Q4 LP3218DT1G` |
| GPIO 与控制信号 | 红外与红 LED 控制 | `gpio=GPIO19`；`transistor=Q5 SS8050 Y1`；`loads=D24 LED; IR1 IR`；`led_resistor=R30 300R`；`ir_resistor=R15 22R/1%` |
| 模拟电路 | 电池电压采样 | `source=VBAT_IN`；`gpio=GPIO38`；`upper_resistor=R40 100K`；`lower_resistor=R41 100K`；`filter=C42 100nF` |
| 电源 | USB 输入路径 | `input=VBUS`；`fuse=F1 6V/1A/PPTC`；`diode=D15 SS34`；`output=+5VIN`；`esd=D16 PESDNC2FD5VB` |
| 电源 | 电池充电 | `reference=U5`；`part_number=TP4057`；`input=+5VIN`；`battery_net=VBAT_IN`；`input_resistor=R21 0.8R`；`program_resistor=R26 3.3K` |
| 电源 | USB/电池电源汇合 | `battery_path=VBAT_IN -> Q3 LP3218DT1G -> +VIN -> Q4 LP3218DT1G -> VBAT_OUT`；`usb_bypass=+5VIN -> D21 SS34 -> VBAT_OUT` |
| 电源 | 上电唤醒与保持 | `button=S3/WAKE`；`rtc_alarm=INT via D22 B5819WT`；`wake_diode=D23 B5819WT`；`hold=GPIO4/HOLD via Q7 SI2302`；`power_switch=Q4 LP3218DT1G` |
| 电源 | 5 V 输出 | `reference=U6`；`part_number=SY7088`；`input=VBAT_OUT`；`inductor=L2 3015 1.5uH`；`pre_diode_voltage=5.3V`；`diode=D20 SS34`；`output=+5VOUT` |
| 电源 | 3.3 V 输出 | `reference=U7`；`part_number=SY8089`；`input=VBAT_OUT`；`enable=3V3EN`；`inductor=L3 3015 4.7uH`；`output=+3V3OUT` |
| 时钟 | RTC 时钟 | `reference=Y1`；`frequency=32.768KHz`；`tolerance=±20ppm`；`load=12.5pF`；`capacitors=C26 6.0pF; C28 6.0pF`；`rtc=U9 RTC8563` |
| 保护电路 | 外部接口 ESD 保护 | `usb=D17/D18 PESDNC2FD3V3B`；`stickio=D3/D4/D6/D7/D9/D10/D11`；`grove=D12/D13 and PESDNC2FD5VB`；`buttons=D5/D8`；`wake=D25 PESDNC2FD3V3B` |
| 存储 | 集成 Flash 容量 | `reference=U1`；`module=ESP32-PICO-V3-02`；`unverified_capacity=8MB Flash` |
| 内存与 Flash | 集成 PSRAM 容量 | `reference=U1`；`module=ESP32-PICO-V3-02`；`unverified_capacity=2MB Quad PSRAM` |
| 接口 | LCD 型号与显示规格 | `confirmed_connector=U3 FPC-0.5-8P`；`unverified_claims=ST7789V2; 1.14 inch; 135x240` |
| 电源 | 内置电池容量 | `battery_connector=J3 Header 2`；`battery_net=VBAT_IN`；`unverified_capacity=200mAh@3.7V` |
| 核心器件 | RTC 型号命名 | `reference=U9`；`schematic_marking=RTC8563`；`document_name=BM8563` |
| 总线地址 | RTC I2C 地址 | `reference=U9`；`part_marking=RTC8563`；`address=not printed` |
| 核心器件 | 背光开关料号 | `reference=U4`；`marking_1=SGM2578`；`marking_2=WS4622C-4/TR`；`function=TFT VLED load switch` |

## 待确认事项

- `storage.integrated-capacity`：原理图仅标注主控模块为 ESP32-PICO-V3-02，未直接标出产品正文所述 8 MB Flash 容量。（证据：图 a44b23c200a4 / 第 1 页 / U1 仅标 ESP32-PICO-V3-02，未分列 Flash）
- `memory.integrated-psram`：原理图未画出独立 PSRAM，也未直接标出产品正文所述 2 MB Quad PSRAM。（证据：图 a44b23c200a4 / 第 1 页 / U1 区域无独立 PSRAM 或容量标注）
- `interface.display-specification`：原理图只显示八针 TFT FPC 和信号，未直接标注 ST7789V2、1.14 英寸或 135×240 分辨率。（证据：图 a44b23c200a4 / 第 1 页 / U3 仅标 FPC-0.5-8P 及电气信号）
- `power.battery-capacity`：J3 和充电链路确认电池连接，但原理图未直接标注 200 mAh@3.7 V。（证据：图 e56bc0b20196 / 第 1 页 / C1，J3 Header 2 仅标 VBAT_IN/GND）
- `component.rtc-name`：原理图 U9 标注 RTC8563，而产品正文使用 BM8563 名称；具体厂牌/完整料号需由 BOM 复核。（证据：图 e56bc0b20196 / 第 1 页 / D4，U9 丝印 RTC8563）
- `address.rtc`：U9 RTC8563 接在 SCL/SDA 上，但原理图未直接印出其 7-bit I2C 地址。（证据：图 e56bc0b20196 / 第 1 页 / U9 SCL/SDA，未见十六进制地址）
- `component.backlight-switch`：U4 同时显示 SGM2578 和 WS4622C-4/TR 两行型号，无法仅由原理图确定实际装配料号。（证据：图 a44b23c200a4 / 第 1 页 / D4，U4 双行型号标注）
- `review.integrated-flash`：请用 ESP32-PICO-V3-02 模组 BOM 或采购料号确认 8 MB Flash。；原因：原理图未分列 Flash 器件或容量。
- `review.integrated-psram`：请用模组 BOM 或器件资料确认 2 MB Quad PSRAM。；原因：原理图未显示独立 PSRAM 或容量。
- `review.display-specification`：请用 LCD FPC/BOM 确认 ST7789V2、1.14 英寸和 135×240。；原因：原理图只给出 FPC 和信号映射。
- `review.battery-capacity`：请用电池标签或 BOM 确认 200 mAh@3.7 V。；原因：原理图只显示电池连接器与电气网络。
- `review.rtc-name`：U9 的正式 BOM 料号是否为 BM8563？；原因：原理图只标 RTC8563，正文写 BM8563。
- `review.rtc-address`：请用 U9 确认料号的 datasheet 复核 7-bit I2C 地址。；原因：原理图未直接标注地址，且型号命名待确认。
- `review.backlight-switch`：U4 实际装配的是 SGM2578 还是 WS4622C-4/TR？；原因：原理图在同一位号下保留两行型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a44b23c200a4052e33ff2e67e575176683c6335c25e093443e17e6628ebf0a36` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_01.png` |
| 2 | 1 | `e56bc0b20196c58678f9329745e939049a8df033794105dfc0965a88d05582e9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_02.png` |
| 3 | 1 | `133d1dbcee40c1d727b4f9c1969d5684a74b19959a8c16b1c759ebc97537137e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_03.png` |

---

源文档：`zh_CN/core/M5StickC PLUS2.md`

源文档 SHA-256：`cd74f38f2f4bf80d013e4db480332935b08c1d3e57a4e19335383d2a3ce28303`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
