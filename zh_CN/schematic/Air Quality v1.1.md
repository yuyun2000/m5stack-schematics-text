# Air Quality v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Air Quality v1.1 |
| SKU | K131-V11 |
| 产品 ID | `air-quality-v1-1-46cfc56dec39` |
| 源文档 | `zh_CN/core/Air_Quality_v1.1.md` |

## 概述

Air Quality v1.1 主板以 M1 Stamp-S3-DIP-1.27 为控制核心，通过 SPI 驱动 24 针墨水屏，并在 SCL1/SDA1 上连接 U5 RTC8563、U6 SCD40 和 P3 空气传感器接口。电源路径包含 U2 TP4057 充电、U7/Q2-Q4 的 WAKE/RTC/HOLD 锁存、U3 SY7088 生成 +5VOUT、U4 SY8089 生成 +3.3V，以及 U1 ME1502CM5G 控制 AirPWREN 传感器电源。Stamp-S3A 模组页显示 U1 ESP32-S3FN8、40MHz 晶振、板载天线匹配、JW5712 5V-3.3V DC/DC、USB-C 保护、Boot 按键与 WS2812 RGB。

## 检索关键词

`Air Quality v1.1`、`K131-V11`、`Stamp-S3A`、`STAMP-S3-DIP-1.27`、`ESP32-S3FN8`、`TP4057`、`RTC8563`、`SCD40`、`SEN55`、`SY7088`、`SY8089`、`ME1502CM5G`、`CN809J`、`LP3218DT1G`、`LN2324DT2AG`、`JW5712`、`GDEY0154D67`、`EPD_BUSY`、`EPD_RES`、`EPD_DC`、`EPD_CS`、`EPD_SCK`、`EPD_MOSI`、`SCL1`、`SDA1`、`AirPWREN`、`HOLD GPIO46`、`WAKE GPIO42`、`G14 battery detect`、`USER_A GPIO0`、`USER_B GPIO8`、`beep GPIO9`、`32.768KHz`、`40MHz`、`USB_D_P`、`USB_D_N`、`HY2.0_IIC`、`+5VOUT`、`+3.3V`、`VBAT_OUT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-DIP-1.27 | AirQ 主板的 Stamp-S3A 控制模组，连接显示、I2C、按键、蜂鸣器、电源控制和扩展 GPIO | 图 d729b8d15c0f / 第 1 页 / 主板页 D2 M1 STAMP-S3-DIP-1.27，左右 17/11 针接口及 GPIO 网络 |
| U2 | TP4057 | 从 +5VIN 为 VBAT_IN 充电的单节锂电池充电器 | 图 d729b8d15c0f / 第 1 页 / 主板页 A1 U2 TP4057，VCC/+5VIN、BAT/VBAT_IN、PROG、CHRG、STDBY |
| U7 | CN809J | 参与电池电源启动/复位锁存控制的复位监控器 | 图 d729b8d15c0f / 第 1 页 / 主板页 A2 U7 CN809J，VCC、RESET、GND 与 Q2/R19 |
| Q2,Q3 | LP3218DT1G | VBAT_IN 到 VBAT_OUT 电源路径中的两个高边开关器件 | 图 d729b8d15c0f / 第 1 页 / 主板页 A1-A3 VBAT_IN-Q2-中间电源-Q3-VBAT_OUT 路径 |
| Q4 | LN2324DT2AG | 由 HOLD 控制并参与 Q3 栅极锁存的低边 MOSFET | 图 d729b8d15c0f / 第 1 页 / 主板页 B2 Q4 LN2324DT2AG，HOLD 栅极、R23 下拉、漏极到 Q3 控制节点 |
| U3 | SY7088 | 由 VBAT_OUT 经 L4 转换并通过 D8 输出 +5VOUT 的开关电源 | 图 d729b8d15c0f / 第 1 页 / 主板页 A3-A4 虚线框 U3 SY7088、L4 1.5uH、R16/R18、D8 SS34 |
| U4 | SY8089 | 由 VBAT_OUT 生成 +3.3V 的降压转换器 | 图 d729b8d15c0f / 第 1 页 / 主板页 B3 U4 SY8089、L5 4.7uH、R27/R28 与 +3.3V |
| U5 | RTC8563 | 32.768kHz RTC，通过 SCL1/SDA1 通信并以 INT 参与定时唤醒 | 图 d729b8d15c0f / 第 1 页 / 主板页 B1 U5 RTC8563，OSCI/OSCO/INT/SCL/SDA |
| Y2,C28,C29 | 32.768KHz ±20ppm 12.5pF / 6pF / 6pF | RTC8563 的低频晶振与负载电容 | 图 d729b8d15c0f / 第 1 页 / 主板页 C2 Y2 32.768KHz 与 C28/C29 6pF，连接 OSCI/OSCO |
| U1 | ME1502CM5G | 由 AirPWREN 使能、为 P3 空气传感器接口供电的限流/负载开关 | 图 d729b8d15c0f / 第 1 页 / 主板页 C3 U1 ME1502CM5G，VIN +5VOUT、EN AirPWREN、RSET/R1 27KΩ、VOUT 到 P3 |
| U6 | SCD40 | 连接 SCL1/SDA1 的 CO2 传感器 | 图 d729b8d15c0f / 第 1 页 / 主板页 D3 U6 SCD40，VDD/VDDH、SCL1、SDA1、GND |
| P3 | Header 6 | 空气传感器接口，引出受控 VDD、GND、SDA1、SCL1、SEL 和 NC | 图 d729b8d15c0f / 第 1 页 / 主板页 C3 P3 Header 6，pin1 VDD、pin2 GND、pin3 SDA、pin4 SCL、pin5 SEL、pin6 NC |
| J3,SW1 | HY2.0_IIC / SW-SPDT | SCL/SDA Grove 接口，SW1 在 +5VIN 与 +5VOUT 间选择 VCC 来源 | 图 d729b8d15c0f / 第 1 页 / 主板页 C4 J3 HY2.0_IIC 与 SW1，pin1 SCL、pin2 SDA、pin3 VCC、pin4 GND |
| J1 | FPC-0.5-24P | 24 针墨水屏连接器，承载 SPI/控制信号和门极/源极高压电源网络 | 图 d729b8d15c0f / 第 1 页 / 主板页 C4-D4 J1 FPC-0.5-24P，EPD_BUSY/RES/DC/CS/SCK/MOSI 与 PEGL/PEGH/VGL/VGH/VCOM |
| LS1,Q5 | Buzzer / SS8050 Y1 | 由 beep 网络经 NPN 晶体管驱动的无源蜂鸣器 | 图 d729b8d15c0f / 第 1 页 / 主板页 C1-D1 LS1 Buzzer、Q5 SS8050 Y1、R25/C27/D7 |
| U1 | ESP32-S3FN8 | Stamp-S3A 模组内主 SoC，集成 8MB Flash 标识并引出 GPIO、USB、射频与显示信号 | 图 1156e645de35 / 第 1 页 / Stamp 页 A2-C2 ESP32 区 U1 ESP32-S3FN8，GPIO0-46、USB_D_N/P、LNA_IN、晶振和电源引脚 |
| ANT1,L6,L1,C19,C2,C1 | PCB antenna matching network | ESP32-S3 LNA_IN 的板载 2.4GHz 天线与匹配网络 | 图 1156e645de35 / 第 1 页 / Stamp 页 A1 ANT1 到 ESP_LNA/LNA_IN，L6 0R、L1 2.7nH、C19/C2/C1 |
| X1,L3,C9,C14 | 40MHz / 10nH / 12pF / 12pF | ESP32-S3 40MHz 主晶振网络 | 图 1156e645de35 / 第 1 页 / Stamp 页 B1 X1 40MHz、L3 10nH、C9/C14 12pF 到 XTAL_40M_P/N |
| U4 | JW5712 | Stamp 模组 VIN_5V 到 VDD_3V3 的 DC/DC 转换器 | 图 1156e645de35 / 第 1 页 / Stamp 页 D1-D2 DCDC 区 U4 JW5712、L4 与 VIN_5V/VDD_3V3 |
| J2,F1,L5,D3,D4 | USB-TYPEC / 6V 1A PPTC / common-mode choke / PESDNC2FD3V3B | Stamp 模组 USB-C 电源和 USB_D_P/N 信号输入及保护 | 图 1156e645de35 / 第 1 页 / Stamp 页 D3-D4 Type-A USB 区 J2 USB-TYPEC、F1、L5、D3/D4、R1/R2 |
| U3 | WS2812 | Stamp 模组板载 RGB LED，DI 接 SK_DIN/GPIO21 | 图 1156e645de35 / 第 1 页 / Stamp 页 B3 RGB LED 区 U3 WS2812，DI SK_DIN、VDD BL_3V3、DO SK_DOUT |
| S1,D1 | SMT_SW_1TS026A / PESDNC2FD3V3B | Stamp 模组 GPIO0 Boot/用户按键及 ESD 保护 | 图 1156e645de35 / 第 1 页 / Stamp 页 C3 BTN-USER 区 GPIO0、S1 到 GND、D1 ESD、R4 10K 上拉 |

## 系统结构

### Air Quality v1.1 系统架构

M1 Stamp-S3A 控制墨水屏、RTC、SCD40、P3 空气传感器、Grove、按键和蜂鸣器；主板电源由充电/锁存、5V 和 3.3V 转换级组成，模组内部使用 ESP32-S3FN8。

- 参数与网络：`controller_module=M1 STAMP-S3-DIP-1.27`；`soc=ESP32-S3FN8`；`rtc=U5 RTC8563`；`co2_sensor=U6 SCD40`；`air_sensor_interface=P3 Header 6`；`display=J1 FPC-0.5-24P`；`power=TP4057 + SY7088 + SY8089`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页完整单页各功能区; 图 1156e645de35 / 第 1 页 / Stamp 页 ESP32/DCDC/USB/模组功能区

## 电源

### 电池充电路径

+5VIN 经 R11 0.8Ω 进入 U2 TP4057 VCC，BAT pin3 输出 VBAT_IN；PROG pin6 经 R17 2.3KΩ 接 GND，P1 Header 2 引出 VBAT_IN/GND。

- 参数与网络：`input=+5VIN`；`charger=U2 TP4057`；`series_resistor=R11 0.8Ω`；`battery_net=VBAT_IN`；`program_resistor=R17 2.3KΩ`；`battery_connector=P1 pin1 VBAT_IN; pin2 GND`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 A1 U2/R11/R17/P1/VBAT_IN

### WAKE/RTC/HOLD 电源锁存

VBAT_IN 经 Q2/Q3 LP3218DT1G 到 VBAT_OUT；S1 WAKE、RTC INT 经 D4/D3 B5819WT 汇合到 Q3 控制节点，Q4 LN2324DT2AG 由 HOLD 驱动并以 R23 100KΩ 下拉。

- 参数与网络：`path=VBAT_IN -> Q2 -> Q3 -> VBAT_OUT`；`wake_button=S1 SW-PB via D4 B5819WT`；`rtc_wake=INT via D3 B5819WT`；`hold=HOLD -> Q4 gate`；`hold_pulldown=R23 100KΩ`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 A2-B2 Q2/Q3/U7/S1/D3/D4/Q4/HOLD/INT

### VBAT_OUT 到 +5VOUT

VBAT_OUT 经 R12 0Ω 进入 U3 SY7088/L4 1.5uH 转换级，反馈 R16 52.3KΩ/R18 15KΩ，输出经 D8 SS34 形成 +5VOUT。

- 参数与网络：`input=VBAT_OUT`；`converter=U3 SY7088`；`inductor=L4 1.5uH`；`feedback=R16 52.3KΩ; R18 15KΩ`；`diode=D8 SS34`；`output=+5VOUT`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 A3-A4 U3/L4/R16/R18/D8 虚线框

### VBAT_OUT 到 +3.3V

VBAT_OUT 为 U4 SY8089 供电并使能，LX 经 L5 4.7uH 输出 +3.3V；反馈为 R27 68KΩ 与 R28 15KΩ。

- 参数与网络：`input=VBAT_OUT`；`converter=U4 SY8089`；`inductor=L5 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ`；`output=+3.3V`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 B3 U4/L5/R27/R28/+3.3V

### 空气传感器受控电源

U1 ME1502CM5G VIN 接 +5VOUT，EN 接 AirPWREN，RSET 通过 R1 27KΩ 接 GND，VOUT 为 P3 pin1 VDD 供电。

- 参数与网络：`input=+5VOUT`；`enable=AirPWREN`；`controller_gpio=M1 G10`；`rset=R1 27KΩ`；`output=P3 pin1 VDD`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 C3 U1/R1/P3 与 D2 M1 pin10 AirPWREN/G10

### 墨水屏高压电源网络

J1 的 GDR/RESE 控制 Q1 LN2324DT2AG 与 L1 10uH、D9-D11 B5819WT，形成 PEGH/PEGL 等墨水屏驱动电源；C5/C6/C8/C10-C14/C22/C23 为 1uF 储能电容。

- 参数与网络：`switch=Q1 LN2324DT2AG`；`inductor=L1 10uH`；`diodes=D9/D10/D11 B5819WT`；`positive_rail=PEGH`；`negative_rail=PEGL`；`connector=J1 FPC-0.5-24P`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 D3-D4 Q1/L1/D9-D11 与 J1 GDR/RESE/PEGH/PEGL 电源网络

### Stamp-S3A 5V 到 3.3V

U4 JW5712 VIN 接 VIN_5V，SW 经 L4 输出 VDD_3V3；ESP_EN 由 R7 10KΩ 上拉并由 C23 1uF 接 GND。

- 参数与网络：`converter=U4 JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWT201608S2R2`；`enable_rc=R7 10KΩ; C23 1uF`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 D1-D2 U4 JW5712/L4/VIN_5V/VDD_3V3 与 ESP_EN

## 接口

### HY2.0-4P I2C 接口

J3 pin1=SCL、pin2=SDA、pin3=VCC、pin4=GND；SW1 选择 +5VIN 或 +5VOUT 作为 VCC，SCL/SDA 连接 M1 的 G15/G13。

- 参数与网络：`pin1=SCL / M1 G15`；`pin2=SDA / M1 G13`；`pin3=VCC selected by SW1`；`pin4=GND`；`power_options=+5VIN or +5VOUT`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 C4 J3/SW1 与 M1 pin15 SDA/G13、pin17 SCL/G15

### Stamp-S3A USB-C 接口

J2 USB-TYPEC 的 DP1/DP2 与 DN1/DN2 经 L5 共模器件连接 USB_D_P/N；CC1/CC2 各由 R1/R2 5.1KΩ 下拉，VBUS 经 F1 6V/1A PPTC 形成 VIN_5V。

- 参数与网络：`connector=J2 USB-TYPEC`；`data=USB_D_P / USB_D_N`；`common_mode=L5`；`cc_resistors=R1/R2 5.1KΩ`；`vbus_protection=F1 6V/1A PPTC`；`output_power=VIN_5V`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 D3-D4 J2/L5/R1/R2/F1/USB_D_P/N/VIN_5V

## 总线

### 内部传感器 I2C 总线

M1 的 SCL1/SDA1 同时连接 U5 RTC8563、U6 SCD40 和 P3 pin4/pin3；R2/R3 各 15KΩ 将 SCL1/SDA1 上拉到 +3.3V。

- 参数与网络：`controller=M1 Stamp-S3A`；`scl=SCL1`；`sda=SDA1`；`devices=U5 RTC8563; U6 SCD40; P3 sensor header`；`pullups=R2/R3 15KΩ to +3.3V`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 U5/U6/P3/M1 的 SCL1/SDA1 同名网络与 R2/R3

### 墨水屏 SPI 与控制映射

M1 G1/G2/G3/G4/G5/G6 分别连接 EPD_BUSY、EPD_RES、EPD_DC、EPD_CS、EPD_SCK、EPD_MOSI，并进入 J1 对应引脚。

- 参数与网络：`busy=G1 EPD_BUSY`；`reset=G2 EPD_RES`；`dc=G3 EPD_DC`；`cs=G4 EPD_CS`；`sck=G5 EPD_SCK`；`mosi=G6 EPD_MOSI`；`connector=J1 FPC-0.5-24P`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 M1 pins1-6 EPD 网络与 J1 pins9-14

## GPIO 与控制信号

### 电源控制 GPIO

M1 G10 输出 AirPWREN，G46 输出 HOLD，G42 接 WAKE，G14 接电池分压检测网络。

- 参数与网络：`air_power=G10 -> AirPWREN`；`hold=G46 -> HOLD`；`wake=G42 -> WAKE`；`battery_detect=G14`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 M1 pin10 AirPWREN/G10、pin27 HOLD/G46、pin25 WAKE/G42、pin16 G14

### 用户按键和蜂鸣器 GPIO

S2 USER_A 连接 M1 G0/Boot，S3 USER_B 连接 G8，S4 RST 连接 EN/RST；M1 G9 的 beep 网络连接 Q5 蜂鸣器驱动级。

- 参数与网络：`user_a=M1 G0/Boot -> USER_A -> S2`；`user_b=M1 G8 -> USER_B -> S3`；`reset=M1 EN/RST -> S4`；`buzzer=M1 G9/beep -> Q5/LS1`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 C1 S2/S3/S4、D1 buzzer 与 M1 USER_A/G0、USER_B/G8、RST/EN、beep/G9

### Stamp-S3A 板载 RGB 与 Boot

U1 GPIO21 连接 SK_DIN 并驱动 U3 WS2812；GPIO0 由 R4 10KΩ 上拉并通过 S1 接 GND，作为 Boot/用户按键。

- 参数与网络：`rgb_gpio=GPIO21 -> SK_DIN -> U3 DI`；`boot_gpio=GPIO0`；`boot_pullup=R4 10KΩ`；`boot_switch=S1 to GND`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 U1 GPIO21/SK_DIN、RGB LED U3 与 BTN-USER GPIO0/S1/R4

## 时钟

### RTC 32.768kHz 时钟

U5 OSCI/OSCO 连接 Y2 32.768KHz ±20ppm 12.5pF 晶振，C28/C29 各 6pF 接 GND。

- 参数与网络：`rtc=U5 RTC8563`；`crystal=Y2 32.768KHz ±20ppm 12.5pF`；`load_capacitors=C28/C29 6pF`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 B1/C2 U5 OSCI/OSCO 与 Y2/C28/C29

### ESP32-S3 主时钟

U1 XTAL_P/N 连接 X1 40MHz 晶振，L3 10nH 位于 XTAL_40M_P，C9/C14 各 12pF 接 GND。

- 参数与网络：`crystal=X1 40MHz`；`inductor=L3 10nH`；`load_capacitors=C9/C14 12pF`；`soc_pins=XTAL_P pin54; XTAL_N pin53`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 B1 X1/L3/C9/C14 与 U1 XTAL_P/N

## 保护电路

### USB ESD 保护

USB_D_P 与 USB_D_N 分别由 D3/D4 PESDNC2FD3V3B 钳位到 GND，VIN_5V 由 D14 PESDNC2FD5VB 钳位。

- 参数与网络：`dp=D3 PESDNC2FD3V3B`；`dn=D4 PESDNC2FD3V3B`；`vbus=D14 PESDNC2FD5VB`；`return=GND`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 Type-A USB 区 D3/D4 与 F1 后 VIN_5V/D14

## 内存与 Flash

### ESP32-S3FN8 Flash

Stamp 模组使用 U1 ESP32-S3FN8；VDD_SPI 连接 FLASH_VCC，而 SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID 引脚标为未连接，页面未画出外部 Flash。

- 参数与网络：`soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`spi_flash_pins=SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID NC`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 U1 VDD_SPI/FLASH_VCC 与 pins30-35 未连接标记

## 音频

### 无源蜂鸣器驱动

beep 经 R25 470Ω 与 C27 10uF 到 Q5 SS8050 Y1 基极，Q5 低端驱动 LS1；LS1 上侧经 R24 10Ω 接 +3.3V，D6/D7 1N4148WT 提供钳位。

- 参数与网络：`input=beep`；`base_network=R25 470Ω; C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`diodes=D6/D7 1N4148WT`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 C1-D1 buzzer/R24/R25/C27/Q5/D6/D7

## 射频

### Stamp-S3A 板载射频天线

U1 LNA_IN 经 ESP_LNA 匹配网络连接 ANT1，网络包含 L6 0R、L1 2.7nH、C19、C2 2.2pF 与 C1 1.8pF。

- 参数与网络：`antenna=ANT1`；`soc_pin=U1 pin1 LNA_IN`；`series=L6 0R; L1 2.7nH`；`capacitors=C19; C2 2.2pF; C1 1.8pF`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 A1 ANT1/L6/L1/C19/C2/C1/ESP_LNA/LNA_IN

## 调试与烧录

### ESP32-S3 下载与串口信号

U1 GPIO19/GPIO20 分别连接 USB_D_N/USB_D_P；U0TXD/U0RXD 通过 TX/RX 网络引到 Stamp 模组 M1 的 G43/Tx 与 G44/Rx。

- 参数与网络：`usb_dn=GPIO19`；`usb_dp=GPIO20`；`uart_tx=U0TXD -> TX -> M1 G43/Tx`；`uart_rx=U0RXD -> RX -> M1 G44/Rx`
- 证据：图 1156e645de35 / 第 1 页 / Stamp 页 U1 GPIO19/20 USB 与 U0TXD/U0RXD TX/RX、M1 G43/G44

## 模拟电路

### 电池电压检测

VBAT_IN 经 R7 1MΩ/R8 1MΩ 分压到 G14，C25 100nF 从 G14 接 GND。

- 参数与网络：`source=VBAT_IN`；`upper=R7 1MΩ`；`lower=R8 1MΩ`；`adc_net=G14`；`filter=C25 100nF`
- 证据：图 d729b8d15c0f / 第 1 页 / 主板页 C1-D1 VBAT_IN/R7/G14/R8/C25

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Air Quality v1.1 系统架构 | `controller_module=M1 STAMP-S3-DIP-1.27`；`soc=ESP32-S3FN8`；`rtc=U5 RTC8563`；`co2_sensor=U6 SCD40`；`air_sensor_interface=P3 Header 6`；`display=J1 FPC-0.5-24P`；`power=TP4057 + SY7088 + SY8089` |
| 电源 | 电池充电路径 | `input=+5VIN`；`charger=U2 TP4057`；`series_resistor=R11 0.8Ω`；`battery_net=VBAT_IN`；`program_resistor=R17 2.3KΩ`；`battery_connector=P1 pin1 VBAT_IN; pin2 GND` |
| 电源 | WAKE/RTC/HOLD 电源锁存 | `path=VBAT_IN -> Q2 -> Q3 -> VBAT_OUT`；`wake_button=S1 SW-PB via D4 B5819WT`；`rtc_wake=INT via D3 B5819WT`；`hold=HOLD -> Q4 gate`；`hold_pulldown=R23 100KΩ` |
| 电源 | VBAT_OUT 到 +5VOUT | `input=VBAT_OUT`；`converter=U3 SY7088`；`inductor=L4 1.5uH`；`feedback=R16 52.3KΩ; R18 15KΩ`；`diode=D8 SS34`；`output=+5VOUT` |
| 电源 | VBAT_OUT 到 +3.3V | `input=VBAT_OUT`；`converter=U4 SY8089`；`inductor=L5 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ`；`output=+3.3V` |
| 电源 | 空气传感器受控电源 | `input=+5VOUT`；`enable=AirPWREN`；`controller_gpio=M1 G10`；`rset=R1 27KΩ`；`output=P3 pin1 VDD` |
| 总线 | 内部传感器 I2C 总线 | `controller=M1 Stamp-S3A`；`scl=SCL1`；`sda=SDA1`；`devices=U5 RTC8563; U6 SCD40; P3 sensor header`；`pullups=R2/R3 15KΩ to +3.3V` |
| 总线地址 | SEN55 与 SCD40 I2C 地址 | `documented_sen55_address=0x69`；`documented_scd40_address=0x62`；`schematic_address_shown=false` |
| 时钟 | RTC 32.768kHz 时钟 | `rtc=U5 RTC8563`；`crystal=Y2 32.768KHz ±20ppm 12.5pF`；`load_capacitors=C28/C29 6pF` |
| GPIO 与控制信号 | 电源控制 GPIO | `air_power=G10 -> AirPWREN`；`hold=G46 -> HOLD`；`wake=G42 -> WAKE`；`battery_detect=G14` |
| 模拟电路 | 电池电压检测 | `source=VBAT_IN`；`upper=R7 1MΩ`；`lower=R8 1MΩ`；`adc_net=G14`；`filter=C25 100nF` |
| 总线 | 墨水屏 SPI 与控制映射 | `busy=G1 EPD_BUSY`；`reset=G2 EPD_RES`；`dc=G3 EPD_DC`；`cs=G4 EPD_CS`；`sck=G5 EPD_SCK`；`mosi=G6 EPD_MOSI`；`connector=J1 FPC-0.5-24P` |
| 电源 | 墨水屏高压电源网络 | `switch=Q1 LN2324DT2AG`；`inductor=L1 10uH`；`diodes=D9/D10/D11 B5819WT`；`positive_rail=PEGH`；`negative_rail=PEGL`；`connector=J1 FPC-0.5-24P` |
| 接口 | HY2.0-4P I2C 接口 | `pin1=SCL / M1 G15`；`pin2=SDA / M1 G13`；`pin3=VCC selected by SW1`；`pin4=GND`；`power_options=+5VIN or +5VOUT` |
| GPIO 与控制信号 | 用户按键和蜂鸣器 GPIO | `user_a=M1 G0/Boot -> USER_A -> S2`；`user_b=M1 G8 -> USER_B -> S3`；`reset=M1 EN/RST -> S4`；`buzzer=M1 G9/beep -> Q5/LS1` |
| 音频 | 无源蜂鸣器驱动 | `input=beep`；`base_network=R25 470Ω; C27 10uF`；`transistor=Q5 SS8050 Y1`；`buzzer=LS1`；`supply=+3.3V via R24 10Ω`；`diodes=D6/D7 1N4148WT` |
| 内存与 Flash | ESP32-S3FN8 Flash | `soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`spi_flash_pins=SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID NC` |
| 时钟 | ESP32-S3 主时钟 | `crystal=X1 40MHz`；`inductor=L3 10nH`；`load_capacitors=C9/C14 12pF`；`soc_pins=XTAL_P pin54; XTAL_N pin53` |
| 射频 | Stamp-S3A 板载射频天线 | `antenna=ANT1`；`soc_pin=U1 pin1 LNA_IN`；`series=L6 0R; L1 2.7nH`；`capacitors=C19; C2 2.2pF; C1 1.8pF` |
| 电源 | Stamp-S3A 5V 到 3.3V | `converter=U4 JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWT201608S2R2`；`enable_rc=R7 10KΩ; C23 1uF` |
| 接口 | Stamp-S3A USB-C 接口 | `connector=J2 USB-TYPEC`；`data=USB_D_P / USB_D_N`；`common_mode=L5`；`cc_resistors=R1/R2 5.1KΩ`；`vbus_protection=F1 6V/1A PPTC`；`output_power=VIN_5V` |
| 保护电路 | USB ESD 保护 | `dp=D3 PESDNC2FD3V3B`；`dn=D4 PESDNC2FD3V3B`；`vbus=D14 PESDNC2FD5VB`；`return=GND` |
| GPIO 与控制信号 | Stamp-S3A 板载 RGB 与 Boot | `rgb_gpio=GPIO21 -> SK_DIN -> U3 DI`；`boot_gpio=GPIO0`；`boot_pullup=R4 10KΩ`；`boot_switch=S1 to GND` |
| 调试与烧录 | ESP32-S3 下载与串口信号 | `usb_dn=GPIO19`；`usb_dp=GPIO20`；`uart_tx=U0TXD -> TX -> M1 G43/Tx`；`uart_rx=U0RXD -> RX -> M1 G44/Rx` |
| 其他事实 | AirQ 主板原理图版本对应 | `product_version=v1.1`；`sku=K131-V11`；`main_schematic_resource_name=Sch_AirQ_v1.0_sch_01.png`；`visible_revision=null` |

## 待确认事项

- `address.documented-sensors`：产品正文给出 SEN55=0x69、SCD40=0x62，但两张原理图仅显示 P3/SCD40 与 SCL1/SDA1 连接，没有地址标注或地址选择配置。（证据：图 d729b8d15c0f / 第 1 页 / 主板页 P3 Header 6 与 U6 SCD40，仅见 SCL1/SDA1，无地址文本）
- `other.revision-alignment`：产品为 Air Quality v1.1/K131-V11，但资源清单中的整机主板图 URL 名为 Sch_AirQ_v1.0，当前图片未见可核对的标题栏版本号。（证据：图 d729b8d15c0f / 第 1 页 / 主板页完整单页，无标题栏版本；对应资源 URL 含 Sch_AirQ_v1.0）
- `review.sensor-addresses`：K131-V11 所装 SEN55 与 SCD40 的地址是否固定为 0x69 和 0x62，且 P3 SEL 不改变总线地址？；原因：地址来自产品正文，当前原理图只显示器件/接口及 I2C 网络，没有地址或 SEL 配置说明。
- `review.revision-alignment`：Sch_AirQ_v1.0 主板图是否是 K131-V11 Air Quality v1.1 的正式生产原理图，是否存在未收录的 v1.1 主板修订？；原因：产品版本与资源文件名不一致，图片本身没有可见标题栏版本号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d729b8d15c0f45734cb6e9509410c26ea3f520643065aa76ad8f0ed4c842daf1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0_sch_01.png` |
| 2 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |

---

源文档：`zh_CN/core/Air_Quality_v1.1.md`

源文档 SHA-256：`5a15b5710a48488b19ce2ef065b0586dd49f98e7f8f2bab5ed875fd11aa1bd98`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
