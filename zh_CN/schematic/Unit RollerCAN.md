# Unit RollerCAN 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RollerCAN |
| SKU | U188 |
| 产品 ID | `unit-rollercan-c1f9bc3acb1b` |
| 源文档 | `zh_CN/unit/Unit-RollerCAN.md` |

## 概述

Unit RollerCAN 以 U6 STM32G431CBU6 为主控，通过 PWM/使能/电流反馈连接 U9 DRV8311HRRWR 三相驱动器，并通过 ENC_CS/SCK/MISO/MOSI 连接 U7 TLI5012BE1000 磁角度传感器。U8 SIT1044QTK/3 将 FDCAN_TX/FDCAN_RX/CAN_STB 转换为 EXT_CANH/EXT_CANL，J5 提供 I2C；J2 OLED、U4/U5 RGB、S1 按键及 J1/J6 调试口提供交互维护。PVIN 经 U1 生成 SYS_5V，再由 U2/U3 生成 MCU_VDD/OLED_VDD。第二张顶部板原理图显示滑环四线连接 J1 的 GND/VIN/SDA/SCL，并配置红色电源 LED。

## 检索关键词

`Unit RollerCAN`、`U188`、`STM32G431CBU6`、`DRV8311HRRWR`、`TLI5012BE1000`、`SIT1044QTK/3`、`FDCAN_TX`、`FDCAN_RX`、`CAN_STB`、`EXT_CANH`、`EXT_CANL`、`SM24CANA`、`CAN bus`、`SYS_I2C_SCL`、`SYS_I2C_SDA`、`0x64`、`PWM_A`、`PWM_B`、`PWM_C`、`PWM_EN`、`DRV_EN`、`DRV_FLT`、`DRV_CSA`、`DRV_CSB`、`DRV_CSC`、`ENC_CS`、`ENC_SCK`、`ENC_MISO`、`ENC_MOSI`、`OLED_MOSI`、`OLED_SCK`、`OLED_DC`、`OLED_RST`、`OLED_CS`、`WS2812C-2020`、`LED_DAT`、`SYS_SW`、`PVIN`、`SYS_5V`、`slip ring Grove`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | STM32G431CBU6 | 主控 MCU，连接电机驱动、磁编码器、RS-485、I2C、OLED、RGB、按键和调试接口 | 图 930210237083 / 第 1 页 / 主板第 1 页网格 A2-B3，U6 STM32G431CBU6 pins1-48 与 ADC/DRV/ENC/FDCAN/I2C/OLED/SWD 网络 |
| U9 | DRV8311HRRWR | 三相无刷电机驱动器，输出 OUTA/OUTB/OUTC 并提供三路电流检测与故障状态 | 图 930210237083 / 第 1 页 / 第 1 页网格 B3-B4，U9 DRV8311HRRWR，INHA/B/C、INLA/B/C、OUTA/B/C、nFAULT/nSLEEP、CSA/B/C、VM |
| U7 | TLI5012BE1000 | 磁角度传感器，通过 ENC_CS/SCK/MISO/MOSI 接主控 | 图 930210237083 / 第 1 页 / 第 1 页网格 C3，U7 TLI5012BE1000，IFC/SCK/CSQ/DATA/IFA/VDD/DGND/IFB |
| U1 | LGS(字符待确认)5124 | PVIN 至 SYS_5V 的降压转换器 | 图 930210237083 / 第 1 页 / 第 1 页网格 A1，U1 六脚降压器，EN/IN/GND/SW/FB 与 L1/D1/R24-R26 |
| U2,U3 | SE8533X2-H | 分别从 SYS_5V 生成 MCU_VDD 与 OLED_VDD | 图 930210237083 / 第 1 页 / 第 1 页网格 B1，U2/U3 SE8533X2-H，VIN/OUT/GND 与各 10uF 电容 |
| J5 | CON_HY2.0_4P_DIP_HOR_RED | Grove I2C 与 VIN/GND 接口 | 图 930210237083 / 第 1 页 / 第 1 页网格 B4，J5 pins1-4 与 GND/VIN/SYS_I2C_SDA/SYS_I2C_SCL |
| J4 | CON3 | 三相电机 OUT_C/OUT_B/OUT_A 接口 | 图 930210237083 / 第 1 页 / 第 1 页网格 B4，J4 CON3 pin3 OUT_C、pin2 OUT_B、pin1 OUT_A |
| J2 | FPC_20P | OLED 20 针 FPC，连接 SPI 控制、电源和去耦网络 | 图 930210237083 / 第 1 页 / 第 1 页网格 C4，J2 FPC_20P，OLED_MOSI/SCK/DC/RST/CS、OLED_VDD/GND 与 C22-C26/R17 |
| U4,U5 | WS2812C 2020 | 两颗级联 RGB LED，由 LED_DAT 控制 | 图 930210237083 / 第 1 页 / 第 1 页网格 D1-D2，U4/U5 WS2812C 2020，DIN/DOUT/VDD/VSS |
| S1 | SW | SYS_SW 到 GND 的功能按键 | 图 930210237083 / 第 1 页 / 第 1 页网格 B2，S1 SW、SYS_SW、C15 1uF/16V 与 GND |
| J1,J6 | CON5 | SWD/SWO 调试接口，提供 MCU_VDD、GND、SWCLK、SWDIO、SYS_RST/SWO | 图 930210237083 / 第 1 页 / 第 1 页网格 D2-D3，J1/J6 CON5 与 MCU_VDD/GND/SWCLK/SWDIO/SYS_RST/SWO |
| U8 | SIT1044QTK/3 | MCU FDCAN 到 EXT_CANH/EXT_CANL 的 CAN 收发器 | 图 930210237083 / 第 1 页 / 主板第 1 页网格 A3-A4，U8 SIT1044QTK/3，TXD/RXD/VIO/STB/CANH/CANL/VCC/GND |
| D2,FU1,FU2,R16 | SM24CANA / 600mA / 600mA / 120R | CAN 差分线的浪涌钳位、串联保护与终端网络 | 图 930210237083 / 第 1 页 / 主板第 1 页网格 A4，CANH/CANL、D2 SM24CANA、FU1/FU2 600mA、R16 120R |
| J1 (top board) | CON4 | 顶部集电环侧 Grove 接口，pin1 GND、pin2 VIN、pin3 SDA、pin4 SCL | 图 b7c854e49da3 / 第 1 页 / 顶部板第 1 页网格 B3，J1 CON4 pins1-4 与 GND/VIN/SDA/SCL 及左侧四个滑环焊盘 |
| LED1,R1 (top board) | RED / 1K/1% | 顶部板 VIN 与 GND 之间的红色电源指示灯 | 图 b7c854e49da3 / 第 1 页 / 顶部板第 1 页网格 B2-B3，LED1 RED 与 R1 1K/1% 跨接 VIN/GND |

## 系统结构

### Unit RollerCAN 系统架构

U6 STM32G431CBU6 控制 U9 DRV8311HRRWR 三相驱动器并读取 U7 TLI5012BE1000；U8 提供 CAN，J5 和顶部板 J1 提供 I2C/Grove，J2/U4/U5/S1 提供 OLED、RGB 和按键。PVIN 经 U1 生成 SYS_5V，再生成 MCU_VDD/OLED_VDD。

- 参数与网络：`controller=U6 STM32G431CBU6`；`motor_driver=U9 DRV8311HRRWR`；`encoder=U7 TLI5012BE1000`；`can=U8 SIT1044QTK/3`；`i2c=main J5 and top-board J1`；`display=J2 FPC_20P`；`rgb=U4,U5`；`power=PVIN -> SYS_5V -> MCU_VDD/OLED_VDD`
- 证据：图 930210237083 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 电源

### PVIN 至 SYS_5V 降压

PVIN 经 R1 0.1R/1% 进入 U1 输入网络，U1 SW 经 L1 和 D1 DSK34 形成 SYS_5V；R24/R25/R26 与 C4/C7 构成使能/反馈网络，SYS_5V 经 F3 输出 EXT_5V。

- 参数与网络：`input=PVIN via R1 0.1R/1%`；`converter=U1 six-pin buck`；`inductor=L1 WPN3012H4R7MT`；`diode=D1 DSK34`；`output=SYS_5V`；`external_5v=SYS_5V -> F3 -> EXT_5V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A1，PVIN/R1/U1/L1/D1/R24-R26/C4/C7/F3/SYS_5V/EXT_5V

### MCU_VDD 与 OLED_VDD

SYS_5V 分别输入 U2/U3 SE8533X2-H，U2 输出 MCU_VDD，U3 输出 OLED_VDD；两路输入/输出均配置 10uF/16V 电容。

- 参数与网络：`mcu_ldo=U2 SE8533X2-H -> MCU_VDD`；`display_ldo=U3 SE8533X2-H -> OLED_VDD`；`input=SYS_5V`；`caps=C2/C5 and C3/C6 10uF/16V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B1，U2/U3 与 SYS_5V/MCU_VDD/OLED_VDD

## 接口

### J5 Grove I2C

J5 pin1=GND、pin2=VIN、pin3=SYS_I2C_SDA、pin4=SYS_I2C_SCL；SDA/SCL 分别连接 U6 pins45/38，并经 R8/R9 各 5.1K/1% 上拉到 MCU_VDD。D4 DSK34 位于 VIN 与 VEXT_5V 电源路径。

- 参数与网络：`pin1=GND`；`pin2=VIN`；`pin3=SYS_I2C_SDA -> U6 pin45`；`pin4=SYS_I2C_SCL -> U6 pin38`；`pullups=R8/R9 5.1K/1% to MCU_VDD`；`power_diode=D4 DSK34 to VEXT_5V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-B4，U6 SYS_I2C_*、R8/R9、D4 与 J5

### J4 三相电机输出

U9 OUTA pin10、OUTB pin11、OUTC pin12 分别形成 OUT_A、OUT_B、OUT_C，并连接 J4 pin1、pin2、pin3。

- 参数与网络：`phase_a=U9 pin10 OUTA -> J4 pin1 OUT_A`；`phase_b=U9 pin11 OUTB -> J4 pin2 OUT_B`；`phase_c=U9 pin12 OUTC -> J4 pin3 OUT_C`；`connector=J4 CON3`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B3-B4，U9 OUTA/B/C 与 J4

### 顶部集电环 Grove 接口

顶部板 J1 CON4 pin1=GND、pin2=VIN、pin3=SDA、pin4=SCL；四路分别直接连接左侧四个滑环焊盘，没有缓冲、转换或保护器件。

- 参数与网络：`connector=top-board J1 CON4`；`pin1=GND`；`pin2=VIN`；`pin3=SDA`；`pin4=SCL`；`slip_ring=four direct pads`；`buffer=null`；`protection=null`
- 证据：图 b7c854e49da3 / 第 1 页 / 顶部板第 1 页网格 B2-B3，四个左侧焊盘到 J1 GND/VIN/SDA/SCL

## 总线

### TLI5012BE1000 编码器总线

U6 ENC_SCK/ENC_CS/ENC_MISO/ENC_MOSI 分别连接 U7 SCK/CSQ/DATA 相关网络，串联 R3/R4 各 100R/1% 与 R5 2.2K/1%；U7 VDD 接 MCU_VDD，DGND 接 GND。

- 参数与网络：`sensor=U7 TLI5012BE1000`；`clock=ENC_SCK via R3 100R/1%`；`select=ENC_CS via R4 100R/1%`；`data=ENC_MISO/ENC_MOSI via DATA network and R5 2.2K/1%`；`supply=MCU_VDD`；`ground=GND`
- 证据：图 930210237083 / 第 1 页 / 主板第 1 页网格 A2-C3，U6 ENC_* 与 U7/R3/R4/R5/R12/R13/C17

### OLED SPI 与控制

U6 PB15/PB13/PB14/PB11/PB12 分别形成 OLED_MOSI/OLED_SCK/OLED_DC/OLED_RST/OLED_CS，并连接 J2 对应信号 pins15/14/13/12/11。

- 参数与网络：`mosi=U6 PB15 pin28 -> J2 pin15`；`clock=PB13 pin26 -> pin14`；`dc=PB14 pin27 -> pin13`；`reset=PB11 pin24 -> pin12`；`chip_select=PB12 pin25 -> pin11`；`connector=J2 FPC_20P`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B2-C4，U6 OLED_* 与 J2 pins11-15

### STM32 FDCAN 与 U8 CAN 收发器

U6 FDCAN_TX pin34 连接 U8 TXD pin1，U8 RXD pin4 经 FDCAN_RX 连接 U6 pin33，U6 CAN_STB pin42 连接 U8 STB pin8；U8 CANH/CANL pins7/6 形成 EXT_CANH/EXT_CANL。

- 参数与网络：`tx=U6 pin34 FDCAN_TX -> U8 pin1 TXD`；`rx=U8 pin4 RXD -> U6 pin33 FDCAN_RX`；`standby=U6 pin42 CAN_STB -> U8 pin8 STB`；`high=U8 pin7 CANH -> EXT_CANH`；`low=U8 pin6 CANL -> EXT_CANL`；`logic_supply=MCU_VDD via VIO pin5`
- 证据：图 930210237083 / 第 1 页 / 主板第 1 页网格 A2-A4，U6 FDCAN_TX/FDCAN_RX/CAN_STB 与 U8 pins1/4/8/7/6

## GPIO 与控制信号

### DRV8311 控制与状态映射

U6 PWM_A/B/C pins32/31/30 接 U9 INHA/INHB/INHC，PWM_EN pin19 同时接 INLA/INLB/INLC；DRV_EN pin18 接 nSLEEP，DRV_FLT pin17 接 nFAULT，DRV_CSA/B/C pins9/10/11 接 U9 SOA/SOB/SOC。

- 参数与网络：`high_pwm=PWM_A->INHA,PWM_B->INHB,PWM_C->INHC`；`low_enable=PWM_EN -> INLA/INLB/INLC`；`sleep=DRV_EN -> nSLEEP`；`fault=nFAULT -> DRV_FLT`；`current_sense=SOA/SOB/SOC -> DRV_CSA/CSB/CSC`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-B4，U6 PWM/DRV_* 与 U9 pins1-5/13-24

### 双 WS2812C RGB

U6 LED_DAT pin43 连接 U4 DIN，U4 DOUT 连接 U5 DIN；两颗 WS2812C 2020 均由 OLED_VDD 供电并接 GND。

- 参数与网络：`controller=U6 pin43 LED_DAT`；`first=U4 WS2812C 2020`；`second=U5 WS2812C 2020`；`chain=U4 DOUT -> U5 DIN`；`supply=OLED_VDD`；`ground=GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B2/D1-D2，U6 LED_DAT 与 U4/U5

### S1 功能按键

U6 SYS_SW pin29/PC6 连接 S1，按下时接 GND；C15 1uF/16V 从 SYS_SW 接 GND。

- 参数与网络：`mcu_pin=U6 pin29 PC6/SYS_SW`；`switch=S1 to GND`；`capacitor=C15 1uF/16V to GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B2，U6 SYS_SW 与 S1/C15/GND

### 顶部板红色电源 LED

顶部板 LED1 RED 与 R1 1K/1% 串联跨接 VIN 和 GND，作为旋转侧电源存在指示。

- 参数与网络：`rail=VIN`；`led=LED1 RED`；`resistor=R1 1K/1%`；`return=GND`；`board=top ring board`
- 证据：图 b7c854e49da3 / 第 1 页 / 顶部板第 1 页网格 B2-B3，VIN-R1-LED1-GND 支路

## 时钟

### U6 外部时钟

U6 PC14/OSC32_I、PC15/OSC32_O、PF0/OSC_IN、PF1/OSC_OUT 引脚在本页未连接外部晶振或负载电容。

- 参数与网络：`low_speed=PC14/PC15 unconnected`；`high_speed=PF0/PF1 unconnected`；`external_crystal=null`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2，U6 左上 OSC32/OSC 引脚无外接线路

## 保护电路

### CAN 终端与浪涌保护

EXT_CANH/EXT_CANL 经 FU1/FU2 各 600mA 串联引出，R16 120R 跨接 CANH/CANL，D2 SM24CANA 连接差分线与 GND；U8 侧另配置电源去耦。

- 参数与网络：`series_high=FU1 600mA`；`series_low=FU2 600mA`；`termination=R16 120R`；`tvs=D2 SM24CANA`；`protected_nets=EXT_CANH,EXT_CANL`；`return=GND`
- 证据：图 930210237083 / 第 1 页 / 主板第 1 页网格 A4，U8 CANH/CANL、R16、D2、FU1/FU2 与 EXT_CANH/EXT_CANL

## 调试与烧录

### J1/J6 调试接口

J1 引出 MCU_VDD、SWCLK、SWDIO、SYS_RST、GND；J6 引出 GND、MCU_VDD、SWCLK、SWDIO、SWO，连接 U6 对应调试网络。

- 参数与网络：`J1=MCU_VDD,SWCLK,SWDIO,SYS_RST,GND`；`J6=GND,MCU_VDD,SWCLK,SWDIO,SWO`；`controller=U6 STM32G431CBU6`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 D2-D3 J1/J6 与 A2 U6 SWCLK/SWDIO/SWO/SYS_RST

## 模拟电路

### PVIN 电压采样

PVIN 经上端电阻与下端分压电阻形成 ADC_VIN，节点由电容对地滤波并连接 U6 ADC_VIN pin8。

- 参数与网络：`input=PVIN`；`sense_net=ADC_VIN`；`controller_pin=U6 pin8 ADC_VIN`；`divider=two resistor divider to GND`；`filter=capacitor to GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 D1 PVIN/ADC_VIN 分压滤波与 A2 U6 ADC_VIN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RollerCAN 系统架构 | `controller=U6 STM32G431CBU6`；`motor_driver=U9 DRV8311HRRWR`；`encoder=U7 TLI5012BE1000`；`can=U8 SIT1044QTK/3`；`i2c=main J5 and top-board J1`；`display=J2 FPC_20P`；`rgb=U4,U5`；`power=PVIN -> SYS_5V -> MCU_VDD/OLED_VDD` |
| 电源 | PVIN 至 SYS_5V 降压 | `input=PVIN via R1 0.1R/1%`；`converter=U1 six-pin buck`；`inductor=L1 WPN3012H4R7MT`；`diode=D1 DSK34`；`output=SYS_5V`；`external_5v=SYS_5V -> F3 -> EXT_5V` |
| 电源 | MCU_VDD 与 OLED_VDD | `mcu_ldo=U2 SE8533X2-H -> MCU_VDD`；`display_ldo=U3 SE8533X2-H -> OLED_VDD`；`input=SYS_5V`；`caps=C2/C5 and C3/C6 10uF/16V` |
| 接口 | J5 Grove I2C | `pin1=GND`；`pin2=VIN`；`pin3=SYS_I2C_SDA -> U6 pin45`；`pin4=SYS_I2C_SCL -> U6 pin38`；`pullups=R8/R9 5.1K/1% to MCU_VDD`；`power_diode=D4 DSK34 to VEXT_5V` |
| 总线 | TLI5012BE1000 编码器总线 | `sensor=U7 TLI5012BE1000`；`clock=ENC_SCK via R3 100R/1%`；`select=ENC_CS via R4 100R/1%`；`data=ENC_MISO/ENC_MOSI via DATA network and R5 2.2K/1%`；`supply=MCU_VDD`；`ground=GND` |
| GPIO 与控制信号 | DRV8311 控制与状态映射 | `high_pwm=PWM_A->INHA,PWM_B->INHB,PWM_C->INHC`；`low_enable=PWM_EN -> INLA/INLB/INLC`；`sleep=DRV_EN -> nSLEEP`；`fault=nFAULT -> DRV_FLT`；`current_sense=SOA/SOB/SOC -> DRV_CSA/CSB/CSC` |
| 接口 | J4 三相电机输出 | `phase_a=U9 pin10 OUTA -> J4 pin1 OUT_A`；`phase_b=U9 pin11 OUTB -> J4 pin2 OUT_B`；`phase_c=U9 pin12 OUTC -> J4 pin3 OUT_C`；`connector=J4 CON3` |
| 模拟电路 | PVIN 电压采样 | `input=PVIN`；`sense_net=ADC_VIN`；`controller_pin=U6 pin8 ADC_VIN`；`divider=two resistor divider to GND`；`filter=capacitor to GND` |
| 总线 | OLED SPI 与控制 | `mosi=U6 PB15 pin28 -> J2 pin15`；`clock=PB13 pin26 -> pin14`；`dc=PB14 pin27 -> pin13`；`reset=PB11 pin24 -> pin12`；`chip_select=PB12 pin25 -> pin11`；`connector=J2 FPC_20P` |
| GPIO 与控制信号 | 双 WS2812C RGB | `controller=U6 pin43 LED_DAT`；`first=U4 WS2812C 2020`；`second=U5 WS2812C 2020`；`chain=U4 DOUT -> U5 DIN`；`supply=OLED_VDD`；`ground=GND` |
| GPIO 与控制信号 | S1 功能按键 | `mcu_pin=U6 pin29 PC6/SYS_SW`；`switch=S1 to GND`；`capacitor=C15 1uF/16V to GND` |
| 调试与烧录 | J1/J6 调试接口 | `J1=MCU_VDD,SWCLK,SWDIO,SYS_RST,GND`；`J6=GND,MCU_VDD,SWCLK,SWDIO,SWO`；`controller=U6 STM32G431CBU6` |
| 时钟 | U6 外部时钟 | `low_speed=PC14/PC15 unconnected`；`high_speed=PF0/PF1 unconnected`；`external_crystal=null` |
| 总线地址 | 正文中的 I2C 地址 0x64 | `documented_address=0x64`；`controller=U6 STM32G431CBU6`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`schematic_address=null` |
| 内存与 Flash | 正文中的 MCU 内存与频率 | `mcu=U6 STM32G431CBU6`；`documented_core=Cortex-M4`；`documented_flash=128KB`；`documented_sram=32KB`；`documented_clock=170MHz`；`schematic_internal_memory=null` |
| 接口 | 正文中的 OLED 规格 | `connector=J2 FPC_20P`；`documented_size=0.66 inch`；`documented_resolution=64x48`；`bus=SPI`；`display_controller=null` |
| 核心器件 | 正文中的 FOC、电机与控制性能 | `documented_motor=D3504 200KV`；`documented_control=FOC current/speed/position loops`；`driver=U9 DRV8311HRRWR`；`encoder=U7 TLI5012BE1000`；`firmware_parameters=null` |
| 电源 | 正文中的供电与负载性能 | `documented_can_supply=6-16V`；`documented_grove=5V`；`documented_phase_current=0.5A continuous,1A short`；`documented_max_load=500g`；`documented_slip_ring=DC 5V/300mA`；`schematic_rating=null` |
| 其他事实 | U1 降压芯片型号字样 | `reference=U1`；`visible_marking=LGS(字符待确认)5124`；`function=PVIN to SYS_5V buck`；`confirmed_part_number=null` |
| 总线 | STM32 FDCAN 与 U8 CAN 收发器 | `tx=U6 pin34 FDCAN_TX -> U8 pin1 TXD`；`rx=U8 pin4 RXD -> U6 pin33 FDCAN_RX`；`standby=U6 pin42 CAN_STB -> U8 pin8 STB`；`high=U8 pin7 CANH -> EXT_CANH`；`low=U8 pin6 CANL -> EXT_CANL`；`logic_supply=MCU_VDD via VIO pin5` |
| 保护电路 | CAN 终端与浪涌保护 | `series_high=FU1 600mA`；`series_low=FU2 600mA`；`termination=R16 120R`；`tvs=D2 SM24CANA`；`protected_nets=EXT_CANH,EXT_CANL`；`return=GND` |
| 接口 | 顶部集电环 Grove 接口 | `connector=top-board J1 CON4`；`pin1=GND`；`pin2=VIN`；`pin3=SDA`；`pin4=SCL`；`slip_ring=four direct pads`；`buffer=null`；`protection=null` |
| GPIO 与控制信号 | 顶部板红色电源 LED | `rail=VIN`；`led=LED1 RED`；`resistor=R1 1K/1%`；`return=GND`；`board=top ring board` |
| 接口 | 正文中的双 CAN XT30 接口 | `documented_connectors=2x CAN XT30 (2+2)`；`schematic_nets=EXT_CANH,EXT_CANL,PVIN,GND`；`connector_references=null`；`parallel_topology=null` |

## 待确认事项

- `address.documented-i2c-address`：正文标称 I2C 地址为 0x64；原理图只显示 U6 与 J5 的 SYS_I2C_SCL/SDA 连接，没有地址选择电阻、地址文字或固件寄存器。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6/J5 I2C 网络，图中无 0x64）
- `memory.documented-mcu-spec`：正文称 STM32G431CBU6 为 Cortex-M4、128KB Flash、32KB SRAM、170MHz；原理图仅确认 U6 型号，没有展开片内存储、内核或时钟频率。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6 型号字段与外部引脚）
- `interface.documented-oled`：正文称 OLED 为 0.66 英寸、64×48、SPI；原理图确认 J2 的 SPI/控制与 OLED_VDD，但未标显示器控制器、尺寸或分辨率。（证据：图 930210237083 / 第 1 页 / 第 1 页 J2 FPC_20P 与 OLED_* 网络，无型号/尺寸/分辨率）
- `component.documented-motor-control`：正文称采用 D3504 200KV 电机、FOC 闭环和电流/速度/位置三环控制；原理图确认 MCU、DRV8311 与 TLI5012 连接，但未标电机型号、FOC 算法、控制环参数或机械安装误差。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6/U9/U7 与 J4 电机接口）
- `power.documented-ratings`：正文称 CAN/XT30 供电支持 6-16V、Grove 支持 5V，并给出相电流、转速、负载、扭矩、待机电流、滑环 5V/300mA 和过压行为；原理图显示 PVIN/VIN 和电源路径，但未打印这些范围、性能或测试条件。（证据：图 930210237083 / 第 1 页 / 第 1 页 PVIN/VIN/U1/U9/J3/J5 电源与驱动路径，无性能表）
- `other.regulator-marking`：原理图 U1 型号文字在本地页面中只能辨认为 LGS(字符待确认)5124，字符不够清晰；电气功能可由 EN/IN/SW/FB 与外围确认，但完整料号需 BOM 或高清原图确认。（证据：图 930210237083 / 第 1 页 / 第 1 页网格 A1 U1 型号文字与 EN/IN/SW/FB 引脚）
- `interface.documented-dual-can`：正文称产品提供 2x CAN XT30（2+2）接口；主板原理图只显示一组 EXT_CANH/EXT_CANL/PVIN/GND 外部网络，没有画出两个带独立位号的 XT30 连接器，因此接口数量与具体并联方式需结合 PCB/线束确认。（证据：图 930210237083 / 第 1 页 / 主板第 1 页右上 EXT_CANH/EXT_CANL/PVIN/GND 端点，无 XT30 位号）
- `review.i2c-address`：请用 U188 当前固件、协议或总线扫描确认默认 I2C 地址 0x64 及修改规则。；原因：原理图未标地址或硬件地址选择。
- `review.mcu-spec`：请用 STM32G431CBU6 资料确认 Cortex-M4、128KB Flash、32KB SRAM 和 170MHz。；原因：板级原理图未展开 MCU 内部资源。
- `review.oled-spec`：请用 OLED BOM/规格确认 0.66 英寸、64×48、控制器型号和 FPC 引脚定义。；原因：原理图只显示 J2 电气接口。
- `review.motor-control`：请用电机 BOM、固件和控制参数确认 D3504 200KV、FOC 三环实现、编码器标定与位置误差。；原因：板级连线不能证明电机机械规格或控制算法。
- `review.power-ratings`：请用量产规格和测试记录确认 6-16V/5V 供电边界、相电流、负载、转速、扭矩、待机与过压行为。；原因：原理图未标这些性能值和热边界。
- `review.regulator-part`：请用 BOM 或高清源文件确认 U1 降压芯片完整型号。；原因：本地原理图型号文字只能辨认为 LGS(字符待确认)5124。
- `review.dual-can-connectors`：请用 PCB、BOM 或线束图确认两个 XT30 CAN 接口的位号、引脚和并联/级联连接。；原因：主板原理图只显示一组外部网络端点，没有两个连接器符号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `930210237083c8f1754136113800c39b332c601db47644194b4ae6b8c4d5817c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/sch_Unit-RollerCAN_V1.0_page_01.png` |
| 2 | 1 | `b7c854e49da35b3b58efe63eea041493ea580ea8fff6a89cc2bd043f483a9015` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/sch_bldc_top_v1.0_page_01.png` |

---

源文档：`zh_CN/unit/Unit-RollerCAN.md`

源文档 SHA-256：`177d9e68148e2d6adda77e190370094f4a2a290d9e5d24cff441da2a59b33876`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
