# Unit QRCode 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit QRCode |
| SKU | U173 |
| 产品 ID | `unit-qrcode-3b010e4b3474` |
| 源文档 | `zh_CN/unit/Unit-QRCode.md` |

## 概述

Unit QRCode 以 U1 STM32F030F4P6 作为总线转换和控制 MCU，通过 FPC1 的 RX/TX、TRIG 与 BEEP 网络连接扫码引擎。J1 Grove 的 IO2/IO1 经 S1 在 UART 的 TX/RX 和 I2C 的 SCL/SDA 间切换；U1 PA2/PA3 连接 RX/TX，PA9/PA10 连接 SCL/SDA。U2 HX6306P332MR 将 VCC_5V 转换为 3V3，为 MCU 和 I2C 上拉供电。S2 将 TRIG 拉低以手动触发，FPC1 BEEP 经 Q1 SS8050 Y1 驱动蜂鸣器，P2 另引出 DM-/DP+、5V 和 GND。

## 检索关键词

`Unit QRCode`、`U173`、`STM32F030F4P6`、`HX6306P332MR`、`FPC-12P`、`M14`、`QR Code`、`Data Matrix`、`PDF417`、`I2C`、`UART`、`0x21`、`IO1`、`IO2`、`SCL`、`SDA`、`RX`、`TX`、`TRIG`、`BEEP`、`DM-`、`DP+`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`HY2.0-4P Grove`、`SWD_5P`、`Buzzer`、`SS8050 Y1`、`1N4148WS T4`、`VCC_5V`、`3V3`、`640x480 CMOS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 总线转换与控制 MCU，连接 UART、I2C、TRIG 和 SWD | 图 f8d8e7061f48 / 第 1 页 / 网格 C1-D2，U1 STM32F030F4P6 及 pins 1-20 |
| U2 | HX6306P332MR | VCC_5V 至 3V3 线性稳压器 | 图 f8d8e7061f48 / 第 1 页 / 网格 B2，U2 HX6306P332MR，VIN/VOUT/GND 与 VCC_5V/3V3 |
| FPC1 | FPC-12P | 扫码引擎的 12 针电源、UART、差分、蜂鸣、LED 与触发接口 | 图 f8d8e7061f48 / 第 1 页 / 网格 C3-D3，FPC1 FPC-12P pins 1-12 TRIG/NC/LED/BUZ/NC/DP+/DM-/TX/RX/GND/VCC/NC |
| J1 | GROVE 4P | 可切换 I2C/UART 的 5V Grove 主机接口 | 图 f8d8e7061f48 / 第 1 页 / 网格 B1，J1 GROVE 4P，SCL/SDA/5V/GND 与 IO2/IO1/VCC_5V/GND |
| S1 | DPDT mode switch | 将 J1 IO2/IO1 切换到 UART TX/RX 或 I2C SCL/SDA | 图 f8d8e7061f48 / 第 1 页 / 网格 B3，S1 pins 1-6 与 UP UART/Down I2C 方向注释 |
| J2 | SWD_5P | STM32 的五针 SWD 调试与复位接口 | 图 f8d8e7061f48 / 第 1 页 / 网格 D2-D3，J2 SWD_5P，VCC/SWCLK/SWDIO/NRST/GND |
| P2 | Header 4 | DM-、DP+、VCC_5V 和 GND 引出接口 | 图 f8d8e7061f48 / 第 1 页 / 网格 C3，P2 Header 4 pins 1-4 DM-/DP+/VCC_5V/GND |
| S2 | 6*6*5 | 将 TRIG 网络接地的手动扫描触发按键 | 图 f8d8e7061f48 / 第 1 页 / 网格 D3，S2 6*6*5 连接 TRIG 与 GND，旁有 R4 10K |
| P1,Q1,D1,R1,R2,R3 | Buzzer / SS8050 Y1 / 1N4148WS T4 / 47R / 1K / 10K | 由 BEEP 控制的 5V 低边蜂鸣器驱动与续流保护 | 图 f8d8e7061f48 / 第 1 页 / 网格 C4-D4，VCC_5V/R1/P1 Buzzer/D1/Q1/R2/R3/BEEP |
| R15,R16,R6,R7,C9,C10,C11 | 10K / 100nF / 10uF | I2C 上拉、BOOT0 下拉、NRST 上拉/滤波和 MCU 供电去耦 | 图 f8d8e7061f48 / 第 1 页 / 网格 C1-D2，R15/R16、R6、R7、C9-C11 与 U1 |

## 系统结构

### Unit QRCode 系统架构

U1 STM32F030F4P6 在 J1 可切换 I2C/UART 接口与 FPC1 扫码引擎之间提供通信和触发控制；U2 从 5V 生成 3V3，板上另含 SWD、DM-/DP+ 引出、触发按键与蜂鸣器驱动。

- 参数与网络：`controller=U1 STM32F030F4P6`；`scanner_interface=FPC1 FPC-12P`；`host_interface=J1 via S1`；`regulator=U2 HX6306P332MR`；`debug=J2 SWD_5P`；`trigger=S2/TRIG`；`buzzer=P1/Q1`
- 证据：图 f8d8e7061f48 / 第 1 页 / 第 1 页完整原理图，J1/S1/U1/U2/FPC1/J2/P2/S2/P1 功能分区

### 其他功能分区

本页未绘制外部存储器、存储卡、射频、独立音频编解码器、电池或充电器；图像采集与照明/瞄准功能位于未展开内部电路的 FPC1 扫码引擎。

- 参数与网络：`external_memory=false`；`storage=false`；`rf=false`；`audio_codec=false`；`battery=false`；`charger=false`；`scanner_internal_circuit=null`
- 证据：图 f8d8e7061f48 / 第 1 页 / 第 1 页全部器件与功能分区

## 核心器件

### U1 STM32F030F4P6 外部引脚

U1 PA2 pin 8=RX、PA3 pin 9=TX、PA9 pin 17=SCL、PA10 pin 18=SDA、PA13 pin 19=MCU_SWDIO、PA14 pin 20=MCU_SWCLK、PB1 pin 14=TRIG；BOOT0 pin 1、NRST pin 4、VDD pin 16、VDDA pin 5、VSS pin 15。

- 参数与网络：`uart=PA2/pin8 RX,PA3/pin9 TX`；`i2c=PA9/pin17 SCL,PA10/pin18 SDA`；`debug=PA13/pin19 MCU_SWDIO,PA14/pin20 MCU_SWCLK`；`trigger=PB1/pin14 TRIG`；`boot=pin1 BOOT0`；`reset=pin4 NRST`；`power=pin16 VDD,pin5 VDDA,pin15 VSS`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C1-D2，U1 pins 1-20 与 RX/TX/SCL/SDA/TRIG/SWD/电源网络

## 电源

### VCC_5V 至 3V3 稳压

VCC_5V 连接 U2 HX6306P332MR VIN pin 3，VOUT pin 2 输出 3V3，GND pin 1 接地；输入 C5 100nF，输出 C7 100nF 与 C8 10uF 对地。

- 参数与网络：`input=VCC_5V -> U2 pin3 VIN`；`output=U2 pin2 VOUT -> 3V3`；`ground=U2 pin1`；`input_capacitor=C5 100nF`；`output_capacitors=C7 100nF,C8 10uF`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 B2，U2/C5/C7/C8 与 VCC_5V/3V3/GND

### U1 供电与去耦

U1 VDD pin 16 与 VDDA pin 5 接 3V3，VSS pin 15 接 GND；C10 100nF 与 C11 10uF 跨接 3V3/GND。

- 参数与网络：`supply_pins=U1 pin16 VDD,pin5 VDDA`；`rail=3V3`；`ground_pin=U1 pin15 VSS`；`decoupling=C10 100nF,C11 10uF`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 D1-D2，U1 VDD/VDDA/VSS 与 C10/C11

## 接口

### J1 Grove 主机接口

J1 SCL、SDA、5V、GND 四触点分别连接 IO2、IO1、VCC_5V、GND；IO2/IO1 的功能由 S1 选择。

- 参数与网络：`connector=J1 GROVE 4P`；`pinout=SCL-row:IO2,SDA-row:IO1,5V:VCC_5V,GND:GND`；`mode_switch=S1`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 B1，J1 GROVE 4P 的 SCL/SDA/5V/GND 与 IO2/IO1/VCC_5V/GND

### FPC1 扫码引擎接口

FPC1 pin 1=TRIG、pin 2=NC、pin 3=LED、pin 4=BUZ/BEEP、pin 5=NC、pin 6=DP+、pin 7=DM-、pin 8=TX、pin 9=RX、pin 10=GND、pin 11=VCC/VCC_5V、pin 12=NC；C1 100nF 跨接 pin 11 与 pin 10。

- 参数与网络：`pinout=1:TRIG,2:NC,3:LED,4:BUZ/BEEP,5:NC,6:DP+,7:DM-,8:TX,9:RX,10:GND,11:VCC_5V,12:NC`；`decoupling=C1 100nF between VCC_5V and GND`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C3-D3，FPC1 FPC-12P pins 1-12 与 C1

### P2 DM-/DP+ 引出

P2 Header 4 pin 1=DM-、pin 2=DP+、pin 3=VCC_5V、pin 4=GND；DM-/DP+ 同名网络连接 FPC1 pins 7/6。

- 参数与网络：`connector=P2 Header 4`；`pinout=1:DM-,2:DP+,3:VCC_5V,4:GND`；`scanner_connection=DM- to FPC1 pin7,DP+ to FPC1 pin6`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C3，P2 pins 1-4 与 FPC1 DM-/DP+ 同名网络

## 总线

### S1 UART/I2C 模式切换

S1 的 IO2 公共端 pin 5 在上拨 UART 时接 pin 4 TX、下拨 I2C 时接 pin 6 SCL；IO1 公共端 pin 2 在上拨 UART 时接 pin 3 RX、下拨 I2C 时接 pin 1 SDA。

- 参数与网络：`uart_mode=UP:IO2->TX,IO1->RX`；`i2c_mode=Down:IO2->SCL,IO1->SDA`；`io2_common=pin5`；`io1_common=pin2`；`annotation=UP UART / Down I2C`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 B3，S1 pins 1-6 与右侧 UP UART/Down I2C 注释

### U1 与 FPC1 UART

U1 PA2 pin 8 的 RX 网络直接连接 FPC1 RX pin 9，U1 PA3 pin 9 的 TX 网络直接连接 FPC1 TX pin 8；同名 RX/TX 网络还连接 S1 UART 触点。

- 参数与网络：`rx=U1 pin8 PA2/RX <-> FPC1 pin9 RX <-> S1 pin3`；`tx=U1 pin9 PA3/TX <-> FPC1 pin8 TX <-> S1 pin4`；`series_resistors=null`；`level_shifter=null`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 B3-D3，S1 RX/TX、U1 PA2/PA3 与 FPC1 pins 9/8

### U1 I2C 与 S1

U1 PA9 pin 17 的 SCL 网络连接 S1 pin 6，U1 PA10 pin 18 的 SDA 网络连接 S1 pin 1；SCL、SDA 分别由 R15、R16 10KΩ 上拉到 3V3。

- 参数与网络：`scl=U1 pin17 PA9/SCL -> S1 pin6`；`sda=U1 pin18 PA10/SDA -> S1 pin1`；`scl_pullup=R15 10K to 3V3`；`sda_pullup=R16 10K to 3V3`；`bus_voltage_v=3.3`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 B3-C2，S1 SCL/SDA、U1 PA9/PA10 与 R15/R16

## GPIO 与控制信号

### TRIG 扫描触发

U1 PB1 pin 14、FPC1 TRIG pin 1、R4 10KΩ 上拉到 3V3及 S2 共用 TRIG 网络；按下 S2 时 TRIG 接 GND。

- 参数与网络：`controller_pin=U1 pin14 PB1`；`scanner_pin=FPC1 pin1 TRIG`；`pullup=R4 10K to 3V3`；`button=S2 6*6*5 to GND`；`active_button_level=low`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C2-D3，U1 PB1/TRIG、FPC1 pin1、R4、S2 与 GND

### BEEP 蜂鸣器驱动

FPC1 BUZ pin 4 连接 BEEP，BEEP 经 R2 1KΩ 驱动 Q1 SS8050 Y1，R3 10KΩ 下拉基极；Q1 低边控制 P1 Buzzer，蜂鸣器高侧经 R1 47R 接 VCC_5V。

- 参数与网络：`source=FPC1 pin4 BUZ/BEEP`；`base_resistor=R2 1K`；`base_pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`load=P1 Buzzer`；`high_side=VCC_5V through R1 47R`；`topology=low-side switch`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C3-D4，FPC1 BUZ/BEEP 与 R2/R3/Q1/P1/R1/VCC_5V

### U1 BOOT0

U1 BOOT0 pin 1 通过 R6 10KΩ 固定下拉到 GND，本页未绘制 BOOT 按键。

- 参数与网络：`module_pin=U1 pin1 BOOT0`；`pulldown=R6 10K to GND`；`boot_button=false`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C2，U1 BOOT0 pin1、R6 10K 与 GND

## 时钟

### U1 时钟

U1 PF0-OSC_IN pin 2 与 PF1-OSC_OUT pin 3 未连接，本页未绘制外部晶振或振荡器。

- 参数与网络：`osc_in=U1 pin2 PF0-OSC_IN unconnected`；`osc_out=U1 pin3 PF1-OSC_OUT unconnected`；`external_clock=null`；`frequency=null`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C2，U1 PF0/PF1 短线无外部连接，整页无晶振

## 复位

### U1 NRST

U1 NRST pin 4 由 R7 10KΩ 上拉到 3V3，并由 C9 100nF 接地；NRST 还引出到 J2 pin 4。

- 参数与网络：`module_pin=U1 pin4 NRST`；`pullup=R7 10K to 3V3`；`capacitor=C9 100nF to GND`；`debug_pin=J2 pin4 NRST`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 D2-D3，U1 NRST、R7/C9 与 J2 NRST

## 保护电路

### 蜂鸣器续流保护

D1 1N4148WS T4 跨接 P1 Buzzer 两端，与 Q1 低边驱动并联形成负载瞬态钳位支路。

- 参数与网络：`diode=D1 1N4148WS T4`；`protected_load=P1 Buzzer`；`driver=Q1 SS8050 Y1`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C4-D4，D1 跨接蜂鸣器高低端

### Grove 与 P2 接口保护

本页未显示 J1 IO1/IO2、P2 DM-/DP+ 或 VCC_5V 输入的 TVS/ESD、保险丝、反接保护、过压保护或电平转换器。

- 参数与网络：`grove_esd=null`；`differential_esd=null`；`fuse=null`；`reverse_protection=null`；`overvoltage_protection=null`；`level_shifter=null`
- 证据：图 f8d8e7061f48 / 第 1 页 / 第 1 页 J1/S1、P2/FPC1 与 VCC_5V 直接连接路径

## 调试与烧录

### J2 SWD 调试接口

J2 pin 1=VCC/3V3、pin 2=SWCLK/MCU_SWCLK、pin 3=SWDIO/MCU_SWDIO、pin 4=NRST、pin 5=GND；MCU_SWCLK/SWDIO 分别连接 U1 PA14 pin 20 与 PA13 pin 19。

- 参数与网络：`pinout=1:3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GND`；`swclk=U1 pin20 PA14`；`swdio=U1 pin19 PA13`
- 证据：图 f8d8e7061f48 / 第 1 页 / 网格 C2-D3，U1 PA13/PA14 与 J2 SWD_5P

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit QRCode 系统架构 | `controller=U1 STM32F030F4P6`；`scanner_interface=FPC1 FPC-12P`；`host_interface=J1 via S1`；`regulator=U2 HX6306P332MR`；`debug=J2 SWD_5P`；`trigger=S2/TRIG`；`buzzer=P1/Q1` |
| 核心器件 | U1 STM32F030F4P6 外部引脚 | `uart=PA2/pin8 RX,PA3/pin9 TX`；`i2c=PA9/pin17 SCL,PA10/pin18 SDA`；`debug=PA13/pin19 MCU_SWDIO,PA14/pin20 MCU_SWCLK`；`trigger=PB1/pin14 TRIG`；`boot=pin1 BOOT0`；`reset=pin4 NRST`；`power=pin16 VDD,pin5 VDDA,pin15 VSS` |
| 电源 | VCC_5V 至 3V3 稳压 | `input=VCC_5V -> U2 pin3 VIN`；`output=U2 pin2 VOUT -> 3V3`；`ground=U2 pin1`；`input_capacitor=C5 100nF`；`output_capacitors=C7 100nF,C8 10uF` |
| 电源 | U1 供电与去耦 | `supply_pins=U1 pin16 VDD,pin5 VDDA`；`rail=3V3`；`ground_pin=U1 pin15 VSS`；`decoupling=C10 100nF,C11 10uF` |
| 接口 | J1 Grove 主机接口 | `connector=J1 GROVE 4P`；`pinout=SCL-row:IO2,SDA-row:IO1,5V:VCC_5V,GND:GND`；`mode_switch=S1` |
| 总线 | S1 UART/I2C 模式切换 | `uart_mode=UP:IO2->TX,IO1->RX`；`i2c_mode=Down:IO2->SCL,IO1->SDA`；`io2_common=pin5`；`io1_common=pin2`；`annotation=UP UART / Down I2C` |
| 总线 | U1 与 FPC1 UART | `rx=U1 pin8 PA2/RX <-> FPC1 pin9 RX <-> S1 pin3`；`tx=U1 pin9 PA3/TX <-> FPC1 pin8 TX <-> S1 pin4`；`series_resistors=null`；`level_shifter=null` |
| 总线 | U1 I2C 与 S1 | `scl=U1 pin17 PA9/SCL -> S1 pin6`；`sda=U1 pin18 PA10/SDA -> S1 pin1`；`scl_pullup=R15 10K to 3V3`；`sda_pullup=R16 10K to 3V3`；`bus_voltage_v=3.3` |
| 接口 | FPC1 扫码引擎接口 | `pinout=1:TRIG,2:NC,3:LED,4:BUZ/BEEP,5:NC,6:DP+,7:DM-,8:TX,9:RX,10:GND,11:VCC_5V,12:NC`；`decoupling=C1 100nF between VCC_5V and GND` |
| 接口 | P2 DM-/DP+ 引出 | `connector=P2 Header 4`；`pinout=1:DM-,2:DP+,3:VCC_5V,4:GND`；`scanner_connection=DM- to FPC1 pin7,DP+ to FPC1 pin6` |
| GPIO 与控制信号 | TRIG 扫描触发 | `controller_pin=U1 pin14 PB1`；`scanner_pin=FPC1 pin1 TRIG`；`pullup=R4 10K to 3V3`；`button=S2 6*6*5 to GND`；`active_button_level=low` |
| GPIO 与控制信号 | BEEP 蜂鸣器驱动 | `source=FPC1 pin4 BUZ/BEEP`；`base_resistor=R2 1K`；`base_pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`load=P1 Buzzer`；`high_side=VCC_5V through R1 47R`；`topology=low-side switch` |
| 保护电路 | 蜂鸣器续流保护 | `diode=D1 1N4148WS T4`；`protected_load=P1 Buzzer`；`driver=Q1 SS8050 Y1` |
| 复位 | U1 NRST | `module_pin=U1 pin4 NRST`；`pullup=R7 10K to 3V3`；`capacitor=C9 100nF to GND`；`debug_pin=J2 pin4 NRST` |
| GPIO 与控制信号 | U1 BOOT0 | `module_pin=U1 pin1 BOOT0`；`pulldown=R6 10K to GND`；`boot_button=false` |
| 调试与烧录 | J2 SWD 调试接口 | `pinout=1:3V3,2:MCU_SWCLK,3:MCU_SWDIO,4:NRST,5:GND`；`swclk=U1 pin20 PA14`；`swdio=U1 pin19 PA13` |
| 时钟 | U1 时钟 | `osc_in=U1 pin2 PF0-OSC_IN unconnected`；`osc_out=U1 pin3 PF1-OSC_OUT unconnected`；`external_clock=null`；`frequency=null` |
| 保护电路 | Grove 与 P2 接口保护 | `grove_esd=null`；`differential_esd=null`；`fuse=null`；`reverse_protection=null`；`overvoltage_protection=null`；`level_shifter=null` |
| 系统结构 | 其他功能分区 | `external_memory=false`；`storage=false`；`rf=false`；`audio_codec=false`；`battery=false`；`charger=false`；`scanner_internal_circuit=null` |
| 总线地址 | I2C 从机地址 | `documented_address=0x21`；`schematic_address=null`；`address_straps=null` |
| 传感器 | 扫码引擎型号与分辨率 | `documented_module=M14`；`documented_sensor=640x480 CMOS`；`documented_illumination=white LED`；`documented_aiming=red LED`；`schematic_module_model=null`；`schematic_led_color=null` |
| 其他事实 | 支持码制与识读性能 | `documented_2d_codes=PDF417,QR Code,Data Matrix`；`documented_1d_code_count=14`；`documented_min_resolution_mil=5`；`documented_min_contrast_percent=20`；`documented_pitch_yaw_deg=±55`；`schematic_performance=null` |
| 接口 | 扫码引擎固件升级接口 | `physical_signals=DM-,DP+`；`header=P2`；`scanner_pins=FPC1 pins7/6`；`documented_use=firmware upgrade`；`protocol=null`；`speed=null` |

## 待确认事项

- `address.documented-i2c-address`：产品正文称 I2C 地址为 0x21，但原理图只有 MCU SCL/SDA 连接，没有地址绑带或固件常量。（证据：图 f8d8e7061f48 / 第 1 页 / 第 1 页 U1 PA9/PA10、R15/R16 和 S1 I2C 路径，无地址值）
- `sensor.documented-scanner-engine`：产品正文称传感器为 640x480 CMOS、M14 模组，并具有白光照明和红光瞄准；原理图仅显示通用 FPC1 FPC-12P 与 LED pin 3，没有扫码模组型号、图像分辨率或 LED 颜色。（证据：图 f8d8e7061f48 / 第 1 页 / 网格 C3-D3，FPC1 仅标 FPC-12P 和 pin3 LED）
- `other.documented-code-performance`：产品正文列出 3 类二维码、14 类一维码、至少 5mil 精度、至少 20% 对比度和 ±55° 扫描角；原理图没有解码固件、光学或性能参数。（证据：图 f8d8e7061f48 / 第 1 页 / 第 1 页 FPC1 扫码引擎接口，无码制、光学或识读性能文字）
- `interface.documented-upgrade-port`：产品正文称扫码引擎预留可升级固件接口；原理图确认 P2/FPC1 引出 DM-/DP+，但未标注 USB 协议、连接器用途、升级流程或电气速率。（证据：图 f8d8e7061f48 / 第 1 页 / 网格 C3，P2 DM-/DP+ 至 FPC1 pins 7/6，无 USB 或升级文字）
- `review.i2c-address`：当前 STM32 固件的 I2C 从机地址是否为 0x21？；原因：原理图没有地址绑带或固件地址定义。
- `review.scanner-engine`：请用当前扫码头 BOM 或模组资料确认 M14、640x480 CMOS、白光照明和红光瞄准。；原因：板级原理图只显示通用 FPC 接口，没有展开扫码引擎内部。
- `review.code-performance`：请用当前扫码引擎固件和测试报告确认支持码制、5mil、20% 对比度和 ±55° 指标。；原因：这些是解码和光学性能，原理图无法证明。
- `review.upgrade-port`：P2 的 DM-/DP+ 是否为 USB 固件升级接口，协议、速率和升级工具是什么？；原因：原理图只给出差分网络名，未标注具体协议和用途。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f8d8e7061f48734944f2b173d1528382085ba5e8de7b81ee209484c312117d0f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/627/SCH_UNIT_QRCODE_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-QRCode.md`

源文档 SHA-256：`54f9bfce1bfc2222c1f44abf8bc237e97adbdd909aac0d804f086c55a9c4179e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
