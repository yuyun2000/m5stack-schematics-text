# Unit RollerCAN-Lite 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit RollerCAN-Lite |
| SKU | U188-Lite |
| 产品 ID | `unit-rollercan-lite-e7b0b6e3f917` |
| 源文档 | `zh_CN/unit/Unit-RollerCAN Lite.md` |

## 概述

Unit RollerCAN-Lite 以 U6 STM32G431CBU6 为主控，通过 PWM_A/B/C、PWM_EN、DRV_EN、DRV_FLT 和三路电流采样连接 U9 DRV8311HRRWR 三相电机驱动器，并通过 ENC_CS/SCK/MISO/MOSI 连接 U7 TLE5012BE1000 磁角度传感器。U8 SIT1044QTK/3 将 MCU 的 FDCAN_TX/FDCAN_RX/CAN_STB 转换为 CANH/CANL，J5 Grove 提供 SYS_I2C_SDA/SCL 与 VIN。PVIN 经 U1 降压为 SYS_5V，再由 U2/U3 生成 MCU_VDD 与 OLED_VDD；J2 OLED、U4/U5 RGB、S1 按键和 J1/J6 SWD/SWO 接口构成交互与调试部分。原理图未直接确认 I2C 地址、MCU 内存/频率、OLED 尺寸/分辨率、电机与 FOC 性能或整机供电性能边界。

## 检索关键词

`Unit RollerCAN-Lite`、`U188-Lite`、`STM32G431CBU6`、`DRV8311HRRWR`、`TLE5012BE1000`、`SIT1044QTK/3`、`FDCAN_TX`、`FDCAN_RX`、`CAN_STB`、`CANH`、`CANL`、`EXT_CANH`、`EXT_CANL`、`SYS_I2C_SCL`、`SYS_I2C_SDA`、`0x64`、`PWM_A`、`PWM_B`、`PWM_C`、`PWM_EN`、`DRV_EN`、`DRV_FLT`、`DRV_CSA`、`DRV_CSB`、`DRV_CSC`、`ENC_CS`、`ENC_SCK`、`ENC_MISO`、`ENC_MOSI`、`OLED_MOSI`、`OLED_SCK`、`OLED_DC`、`OLED_RST`、`OLED_CS`、`WS2812C 2020`、`LED_DAT`、`SYS_SW`、`PVIN`、`SYS_5V`、`MCU_VDD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | STM32G431CBU6 | 主控 MCU，连接电机驱动、角度传感器、CAN、I2C、OLED、RGB、按键和调试接口 | 图 930210237083 / 第 1 页 / 第 1 页网格 A2-B3，U6 STM32G431CBU6 pins1-48 与 ADC/DRV/ENC/FDCAN/I2C/OLED/SWD 网络 |
| U9 | DRV8311HRRWR | 三相无刷电机驱动器，输出 OUTA/OUTB/OUTC，并提供三路电流检测、故障和睡眠控制 | 图 930210237083 / 第 1 页 / 第 1 页网格 B3-B4，U9 DRV8311HRRWR，INHA/B/C、INLA/B/C、OUTA/B/C、nFAULT、nSLEEP、SOA/B/C、VM |
| U7 | TLE5012BE1000 | 磁角度传感器，通过 ENC_CS/SCK/MISO/MOSI 网络连接主控 | 图 930210237083 / 第 1 页 / 第 1 页网格 C3，U7 TLE5012BE1000，IFC/SCK/CSQ/DATA/IFA/VDD/DGND/IFB |
| U8 | SIT1044QTK/3 | FDCAN_TX/FDCAN_RX 与 CANH/CANL 之间的 CAN 收发器，CAN_STB 控制待机 | 图 930210237083 / 第 1 页 / 第 1 页网格 A3-A4，U8 SIT1044QTK/3，TXD/RXD/STB/CANH/CANL/VCC/VIO/GND |
| U1 | LGS(字符待确认)5124 | PVIN 至 SYS_5V 的六引脚降压转换器 | 图 930210237083 / 第 1 页 / 第 1 页网格 A1，U1 型号字样及 BST/EN/IN/GND/SW/FB 引脚 |
| U2,U3 | SE8533X2-H | 分别由 SYS_5V 生成 MCU_VDD 与 OLED_VDD | 图 930210237083 / 第 1 页 / 第 1 页网格 B1，U2/U3 SE8533X2-H，VIN/OUT/GND 与 C2/C3/C5/C6 |
| J5 | CON_HY2.0_4P_DIP_HOR_RED | Grove I2C 与 VIN/GND 四针接口 | 图 930210237083 / 第 1 页 / 第 1 页网格 B4，J5 pins1-4 与 GND/VIN/SYS_I2C_SDA/SYS_I2C_SCL |
| J4 | CON3 | 三相电机 OUT_C/OUT_B/OUT_A 输出接口 | 图 930210237083 / 第 1 页 / 第 1 页网格 B4，J4 CON3 pin3 OUT_C、pin2 OUT_B、pin1 OUT_A |
| J2 | FH43SRJ-20S-0.5SH | OLED 20 针 FPC，连接 OLED_MOSI/SCK/DC/RST/CS、电源与电容网络 | 图 930210237083 / 第 1 页 / 第 1 页网格 C4-D4，J2 FH43SRJ-20S-0.5SH pins1-20 与 OLED_*、OLED_VDD、GND、C22-C26/R17 |
| U4,U5 | WS2812C 2020 | 两颗级联 RGB LED，由 LED_DAT 控制 | 图 930210237083 / 第 1 页 / 第 1 页网格 C1-C2，U4/U5 WS2812C 2020，DIN/DOUT/VDD/VSS |
| S1 | SW | SYS_SW 到 GND 的功能按键 | 图 930210237083 / 第 1 页 / 第 1 页网格 B2，S1 SW、SYS_SW、C15 1uF/16V 与 GND |
| J1,J6 | SIP_5P(NC) / HC-1.25-5AW | SWD/SWO 调试接口，提供 MCU_VDD、GND、SWCLK、SWDIO、SYS_RST 或 SWO | 图 930210237083 / 第 1 页 / 第 1 页网格 C2-C3，J1/J6 五针接口与 MCU_VDD/GND/SWCLK/SWDIO/SYS_RST/SWO |
| FU1,FU2 | 600/20mA | CANH/CANL 至 EXT_CANH/EXT_CANL 的串联保护器件 | 图 930210237083 / 第 1 页 / 第 1 页网格 A4，FU1/FU2 600/20mA 分别串联 CANH 与 CANL |
| D2 | SM24CANA | CANH/CANL 差分线保护器件 | 图 930210237083 / 第 1 页 / 第 1 页网格 A3-A4，D2 SM24CANA 位于 CANH/CANL 与 GND 周围 |

## 系统结构

### Unit RollerCAN-Lite 系统架构

U6 STM32G431CBU6 控制 U9 DRV8311HRRWR 三相驱动器并读取 U7 TLE5012BE1000 角度传感器；U8 提供 CAN，J5 提供 I2C，J2/U4/U5/S1 提供 OLED、RGB 和按键交互。PVIN 经 U1 生成 SYS_5V，再生成 MCU_VDD/OLED_VDD。

- 参数与网络：`controller=U6 STM32G431CBU6`；`motor_driver=U9 DRV8311HRRWR`；`encoder=U7 TLE5012BE1000`；`can=U8 SIT1044QTK/3`；`i2c=J5`；`display=J2`；`rgb=U4,U5`；`power=PVIN -> SYS_5V -> MCU_VDD/OLED_VDD`
- 证据：图 930210237083 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 电源

### PVIN 至 SYS_5V 降压

PVIN 经 R1 0.1R/1% 进入 U1 输入网络，U1 SW 经 L1 WPN3012H4R7MT 与 D1 DSK34 形成 SYS_5V；R24/R25/R26 与 C4/C7 构成使能和反馈网络，SYS_5V 经 F3 输出 VEXT_5V。

- 参数与网络：`input=PVIN via R1 0.1R/1%`；`converter=U1 six-pin buck`；`inductor=L1 WPN3012H4R7MT`；`diode=D1 DSK34`；`output=SYS_5V`；`external_5v=SYS_5V -> F3 -> VEXT_5V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A1，PVIN/R1/U1/L1/D1/R24-R26/C4/C7/F3/SYS_5V/VEXT_5V

### MCU_VDD 与 OLED_VDD

SYS_5V 分别输入 U2/U3 SE8533X2-H，U2 输出 MCU_VDD，U3 输出 OLED_VDD；两路输入和输出均配置 10uF/16V 电容。

- 参数与网络：`mcu_ldo=U2 SE8533X2-H -> MCU_VDD`；`display_ldo=U3 SE8533X2-H -> OLED_VDD`；`input=SYS_5V`；`caps=C2/C5 and C3/C6 10uF/16V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B1，U2/U3 与 SYS_5V/MCU_VDD/OLED_VDD

### PVIN 与 Grove VIN 电源路径

PVIN 直接供给 U9 VM/VIN_AVDD 并进入 U1 降压；J5 pin2 VIN 经 D4 DSS34 连接 VEXT_5V，SYS_5V 也经 F3 连接 VEXT_5V。

- 参数与网络：`motor_input=PVIN -> U9 VM pin8 and VIN_AVDD pin7`；`buck_input=PVIN -> U1`；`grove_input=J5 pin2 VIN -> D4 DSS34 -> VEXT_5V`；`sys5v_path=SYS_5V -> F3 -> VEXT_5V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A1-B4，PVIN/U1/U9、SYS_5V/F3/VEXT_5V 与 J5 VIN/D4

### DRV8311 电源与模拟地

U9 VM pin8 与 VIN_AVDD pin7 接 PVIN，C19 1uF/16V 跨接 CP pin6 与 PVIN，C20/C21 各 10uF/25V 从 PVIN 对地；AVDD pin17 形成 DRV_VDDO 并由 C16 1uF/16V 对 AGND 去耦。

- 参数与网络：`driver=U9 DRV8311HRRWR`；`motor_supply=VM pin8=PVIN`；`analog_input=VIN_AVDD pin7=PVIN`；`charge_pump=C19 1uF/16V`；`bulk_caps=C20/C21 10uF/25V`；`analog_output=pin17 AVDD=DRV_VDDO`；`analog_ground=AGND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B3-B4，U9 pins6-9/16-17、PVIN、C16/C19-C21 与 AGND/GND

## 接口

### 外部 CAN 与 PVIN 网络

原理图右上引出 GND、PVIN、EXT_CANH 和 EXT_CANL；CANH/CANL 分别经 FU1/FU2 600/20mA 串联成为 EXT_CANH/EXT_CANL。该页未给这些外部网络标注连接器位号或针脚号。

- 参数与网络：`power=GND,PVIN`；`can_high=CANH -> FU1 -> EXT_CANH`；`can_low=CANL -> FU2 -> EXT_CANL`；`connector_reference=null`；`pin_numbers=null`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A4，GND/PVIN/EXT_CANH/EXT_CANL 与 FU1/FU2；无连接器符号位号

### J5 Grove I2C 接口

J5 pin1=GND、pin2=VIN、pin3=SYS_I2C_SDA、pin4=SYS_I2C_SCL；SDA/SCL 分别连接 U6 PB7 pin45 与 PA15 pin38，并经 R8/R9 各 5.1K/1% 上拉到 MCU_VDD。

- 参数与网络：`connector=J5 CON_HY2.0_4P_DIP_HOR_RED`；`pin1=GND`；`pin2=VIN`；`pin3=SYS_I2C_SDA -> U6 PB7 pin45`；`pin4=SYS_I2C_SCL -> U6 PA15 pin38`；`pullups=R8/R9 5.1K/1% to MCU_VDD`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-B4，U6 SYS_I2C_*、R8/R9 与 J5 pins1-4

### J4 三相电机输出

U9 OUTA pin10、OUTB pin11、OUTC pin12 分别形成 OUT_A、OUT_B、OUT_C，并连接 J4 pin1、pin2、pin3。

- 参数与网络：`phase_a=U9 pin10 OUTA -> J4 pin1 OUT_A`；`phase_b=U9 pin11 OUTB -> J4 pin2 OUT_B`；`phase_c=U9 pin12 OUTC -> J4 pin3 OUT_C`；`connector=J4 CON3`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B3-B4，U9 OUTA/B/C 与 J4 pins1-3

## 总线

### STM32 FDCAN 与 U8 CAN 收发器

U6 PA12 pin34 的 FDCAN_TX 接 U8 TXD pin1，U8 RXD pin4 通过 FDCAN_RX 接 U6 PA11 pin33；U6 PB4 pin42 的 CAN_STB 接 U8 STB pin8。U8 CANH pin7 与 CANL pin6 进入外部差分网络。

- 参数与网络：`controller_tx=U6 PA12 pin34 FDCAN_TX -> U8 pin1 TXD`；`controller_rx=U8 pin4 RXD -> U6 PA11 pin33 FDCAN_RX`；`standby=U6 PB4 pin42 CAN_STB -> U8 pin8 STB`；`differential=U8 pin7 CANH,pin6 CANL`；`logic_supply=U8 pin5 VIO=MCU_VDD`；`bus_supply=U8 pin3 VCC=VEXT_5V`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-A4，U6 FDCAN_TX/FDCAN_RX/CAN_STB 与 U8 pins1-8

### TLE5012BE1000 编码器串行连接

U6 的 ENC_SCK、ENC_CS、ENC_MISO、ENC_MOSI 连接 U7 的 SCK/CSQ/DATA 接口；时钟和片选分别串联 R3/R4 各 100R/1%，ENC_MOSI 经 R5 2.2K/1% 接 DATA 节点，U7 VDD 接 MCU_VDD。

- 参数与网络：`sensor=U7 TLE5012BE1000`；`clock=ENC_SCK -> R3 100R/1% -> U7 pin2 SCK`；`select=ENC_CS -> R4 100R/1% -> U7 pin3 CSQ`；`data_out=U7 pin4 DATA -> ENC_MISO`；`data_in=ENC_MOSI -> R5 2.2K/1% -> DATA`；`supply=pin6 VDD=MCU_VDD`；`ground=pin7 DGND,pin8 IFB=GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-C3，U6 ENC_* 与 U7/R3-R5/R12/R13/C17

### OLED SPI 与控制映射

U6 PB15/PB13/PB14/PB11/PB12 分别形成 OLED_MOSI/OLED_SCK/OLED_DC/OLED_RST/OLED_CS，并连接 J2 pins15/14/13/12/11。

- 参数与网络：`mosi=U6 PB15 pin28 -> J2 pin15`；`clock=U6 PB13 pin26 -> J2 pin14`；`dc=U6 PB14 pin27 -> J2 pin13`；`reset=U6 PB11 pin24 -> J2 pin12`；`chip_select=U6 PB12 pin25 -> J2 pin11`；`connector=J2 FH43SRJ-20S-0.5SH`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B2-C4，U6 OLED_* 与 J2 pins11-15

## GPIO 与控制信号

### DRV8311 控制、故障与电流采样

U6 PWM_A/B/C pins32/31/30 接 U9 INHA/INHB/INHC，PWM_EN pin19 共接 INLA/INLB/INLC；DRV_EN pin18 接 nSLEEP，DRV_FLT pin17 接 nFAULT，DRV_CSA/B/C pins9/10/11 分别接 U9 SOA/SOB/SOC。

- 参数与网络：`high_pwm=PWM_A->INHA,PWM_B->INHB,PWM_C->INHC`；`low_inputs=PWM_EN -> INLA/INLB/INLC`；`sleep=DRV_EN -> nSLEEP`；`fault=nFAULT -> DRV_FLT`；`current_sense=SOA/SOB/SOC -> DRV_CSA/CSB/CSC`；`adc_filters=C28/C29/C30 10pF/50V to GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-B4，U6 PWM/DRV_*、C28-C30 与 U9 pins1-5/13-24

### 双 WS2812C RGB LED

U6 PB5 pin43 的 LED_DAT 连接 U4 DIN，U4 DOUT 连接 U5 DIN；两颗 WS2812C 2020 均由 OLED_VDD 供电并接 GND。

- 参数与网络：`controller=U6 PB5 pin43 LED_DAT`；`first=U4 WS2812C 2020`；`second=U5 WS2812C 2020`；`chain=U4 DOUT -> U5 DIN`；`supply=OLED_VDD`；`ground=GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-C2，U6 LED_DAT 与 U4/U5

### S1 功能按键

U6 PC6 pin29 的 SYS_SW 连接 S1，按下时接 GND；C15 1uF/16V 从 SYS_SW 接 GND。

- 参数与网络：`mcu_pin=U6 PC6 pin29 SYS_SW`；`switch=S1 to GND`；`capacitor=C15 1uF/16V to GND`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 B2，U6 SYS_SW 与 S1/C15/GND

### BOOT0 引脚

U6 PB8/BOOT0 pin46 在本页未连接外部上拉、下拉、按键或连接器。

- 参数与网络：`controller_pin=U6 PB8/BOOT0 pin46`；`external_connection=null`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2，U6 右上 PB8/BOOT0 pin46 无外接网络

## 时钟

### U6 外部时钟连接

U6 PC14/OSC32_I、PC15/OSC32_O、PF0/OSC_IN、PF1/OSC_OUT 在本页未连接外部晶振或负载电容。

- 参数与网络：`low_speed=PC14/PC15 unconnected`；`high_speed=PF0/PF1 unconnected`；`external_crystal=null`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2，U6 pins3-6 OSC32/OSC 引脚无外接线路

## 复位

### STM32 复位网络

U6 PG10/NRST pin7 连接 SYS_RST，C10 1uF/16V 从 SYS_RST 接 GND，SYS_RST 同时引至 J1 pin4。

- 参数与网络：`controller_pin=U6 PG10/NRST pin7`；`net=SYS_RST`；`capacitor=C10 1uF/16V to GND`；`debug_connector=J1 pin4`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-C2，U6 pin7 SYS_RST、C10 与 J1 pin4

## 保护电路

### CAN 偏置、终端与浪涌保护

CANH/CANL 网络配置 R14/R15 各 5.1K/1% 偏置、R16 120R 差分终端、D2 SM24CANA 保护，并分别串联 FU1/FU2 600/20mA 后引出 EXT_CANH/EXT_CANL。

- 参数与网络：`bias=R14/R15 5.1K/1%`；`termination=R16 120R`；`tvs=D2 SM24CANA`；`series_protection=FU1/FU2 600/20mA`；`external_nets=EXT_CANH,EXT_CANL`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 A3-A4，U8 CANH/CANL、R14-R16、D2、FU1/FU2

## 内存与 Flash

### 外部存储器

本页未显示独立 Flash、EEPROM、SRAM、SD 卡或其他外部存储器件；存储资源仅能由 U6 型号进一步查询，不能由板级连线确认。

- 参数与网络：`external_flash=null`；`eeprom=null`；`external_sram=null`；`sd_card=null`
- 证据：图 930210237083 / 第 1 页 / 第 1 页完整原理图器件区，无独立存储器或存储连接器

## 调试与烧录

### J1/J6 SWD 与 SWO 调试接口

J1 引出 MCU_VDD、SWCLK、SWDIO、SYS_RST、GND；J6 引出 GND、MCU_VDD、SWCLK、SWDIO、SWO，均连接 U6 对应调试网络。

- 参数与网络：`J1=pin1 MCU_VDD,pin2 SWCLK,pin3 SWDIO,pin4 SYS_RST,pin5 GND`；`J6=pin1 GND,pin2 MCU_VDD,pin3 SWCLK,pin4 SWDIO,pin5 SWO`；`controller=U6 STM32G431CBU6`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 C2-C3，J1/J6 与 U6 SWCLK/SWDIO/SWO/SYS_RST 网络

## 模拟电路

### PVIN 电压采样

PVIN 经 R18 82K/1% 与 R19 22K/1% 分压形成 ADC_VIN，C27 1uF/16V 从 ADC_VIN 接 GND；ADC_VIN 连接 U6 PA0 pin8。

- 参数与网络：`input=PVIN`；`divider=R18 82K/1%,R19 22K/1%`；`filter=C27 1uF/16V`；`sense_net=ADC_VIN`；`controller_pin=U6 PA0 pin8`
- 证据：图 930210237083 / 第 1 页 / 第 1 页网格 C1，PVIN/R18/R19/C27/ADC_VIN；网格 A2 U6 pin8

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit RollerCAN-Lite 系统架构 | `controller=U6 STM32G431CBU6`；`motor_driver=U9 DRV8311HRRWR`；`encoder=U7 TLE5012BE1000`；`can=U8 SIT1044QTK/3`；`i2c=J5`；`display=J2`；`rgb=U4,U5`；`power=PVIN -> SYS_5V -> MCU_VDD/OLED_VDD` |
| 电源 | PVIN 至 SYS_5V 降压 | `input=PVIN via R1 0.1R/1%`；`converter=U1 six-pin buck`；`inductor=L1 WPN3012H4R7MT`；`diode=D1 DSK34`；`output=SYS_5V`；`external_5v=SYS_5V -> F3 -> VEXT_5V` |
| 电源 | MCU_VDD 与 OLED_VDD | `mcu_ldo=U2 SE8533X2-H -> MCU_VDD`；`display_ldo=U3 SE8533X2-H -> OLED_VDD`；`input=SYS_5V`；`caps=C2/C5 and C3/C6 10uF/16V` |
| 电源 | PVIN 与 Grove VIN 电源路径 | `motor_input=PVIN -> U9 VM pin8 and VIN_AVDD pin7`；`buck_input=PVIN -> U1`；`grove_input=J5 pin2 VIN -> D4 DSS34 -> VEXT_5V`；`sys5v_path=SYS_5V -> F3 -> VEXT_5V` |
| 电源 | DRV8311 电源与模拟地 | `driver=U9 DRV8311HRRWR`；`motor_supply=VM pin8=PVIN`；`analog_input=VIN_AVDD pin7=PVIN`；`charge_pump=C19 1uF/16V`；`bulk_caps=C20/C21 10uF/25V`；`analog_output=pin17 AVDD=DRV_VDDO`；`analog_ground=AGND` |
| 接口 | 外部 CAN 与 PVIN 网络 | `power=GND,PVIN`；`can_high=CANH -> FU1 -> EXT_CANH`；`can_low=CANL -> FU2 -> EXT_CANL`；`connector_reference=null`；`pin_numbers=null` |
| 总线 | STM32 FDCAN 与 U8 CAN 收发器 | `controller_tx=U6 PA12 pin34 FDCAN_TX -> U8 pin1 TXD`；`controller_rx=U8 pin4 RXD -> U6 PA11 pin33 FDCAN_RX`；`standby=U6 PB4 pin42 CAN_STB -> U8 pin8 STB`；`differential=U8 pin7 CANH,pin6 CANL`；`logic_supply=U8 pin5 VIO=MCU_VDD`；`bus_supply=U8 pin3 VCC=VEXT_5V` |
| 保护电路 | CAN 偏置、终端与浪涌保护 | `bias=R14/R15 5.1K/1%`；`termination=R16 120R`；`tvs=D2 SM24CANA`；`series_protection=FU1/FU2 600/20mA`；`external_nets=EXT_CANH,EXT_CANL` |
| 接口 | J5 Grove I2C 接口 | `connector=J5 CON_HY2.0_4P_DIP_HOR_RED`；`pin1=GND`；`pin2=VIN`；`pin3=SYS_I2C_SDA -> U6 PB7 pin45`；`pin4=SYS_I2C_SCL -> U6 PA15 pin38`；`pullups=R8/R9 5.1K/1% to MCU_VDD` |
| 总线 | TLE5012BE1000 编码器串行连接 | `sensor=U7 TLE5012BE1000`；`clock=ENC_SCK -> R3 100R/1% -> U7 pin2 SCK`；`select=ENC_CS -> R4 100R/1% -> U7 pin3 CSQ`；`data_out=U7 pin4 DATA -> ENC_MISO`；`data_in=ENC_MOSI -> R5 2.2K/1% -> DATA`；`supply=pin6 VDD=MCU_VDD`；`ground=pin7 DGND,pin8 IFB=GND` |
| GPIO 与控制信号 | DRV8311 控制、故障与电流采样 | `high_pwm=PWM_A->INHA,PWM_B->INHB,PWM_C->INHC`；`low_inputs=PWM_EN -> INLA/INLB/INLC`；`sleep=DRV_EN -> nSLEEP`；`fault=nFAULT -> DRV_FLT`；`current_sense=SOA/SOB/SOC -> DRV_CSA/CSB/CSC`；`adc_filters=C28/C29/C30 10pF/50V to GND` |
| 接口 | J4 三相电机输出 | `phase_a=U9 pin10 OUTA -> J4 pin1 OUT_A`；`phase_b=U9 pin11 OUTB -> J4 pin2 OUT_B`；`phase_c=U9 pin12 OUTC -> J4 pin3 OUT_C`；`connector=J4 CON3` |
| 模拟电路 | PVIN 电压采样 | `input=PVIN`；`divider=R18 82K/1%,R19 22K/1%`；`filter=C27 1uF/16V`；`sense_net=ADC_VIN`；`controller_pin=U6 PA0 pin8` |
| 总线 | OLED SPI 与控制映射 | `mosi=U6 PB15 pin28 -> J2 pin15`；`clock=U6 PB13 pin26 -> J2 pin14`；`dc=U6 PB14 pin27 -> J2 pin13`；`reset=U6 PB11 pin24 -> J2 pin12`；`chip_select=U6 PB12 pin25 -> J2 pin11`；`connector=J2 FH43SRJ-20S-0.5SH` |
| GPIO 与控制信号 | 双 WS2812C RGB LED | `controller=U6 PB5 pin43 LED_DAT`；`first=U4 WS2812C 2020`；`second=U5 WS2812C 2020`；`chain=U4 DOUT -> U5 DIN`；`supply=OLED_VDD`；`ground=GND` |
| GPIO 与控制信号 | S1 功能按键 | `mcu_pin=U6 PC6 pin29 SYS_SW`；`switch=S1 to GND`；`capacitor=C15 1uF/16V to GND` |
| 调试与烧录 | J1/J6 SWD 与 SWO 调试接口 | `J1=pin1 MCU_VDD,pin2 SWCLK,pin3 SWDIO,pin4 SYS_RST,pin5 GND`；`J6=pin1 GND,pin2 MCU_VDD,pin3 SWCLK,pin4 SWDIO,pin5 SWO`；`controller=U6 STM32G431CBU6` |
| 复位 | STM32 复位网络 | `controller_pin=U6 PG10/NRST pin7`；`net=SYS_RST`；`capacitor=C10 1uF/16V to GND`；`debug_connector=J1 pin4` |
| 时钟 | U6 外部时钟连接 | `low_speed=PC14/PC15 unconnected`；`high_speed=PF0/PF1 unconnected`；`external_crystal=null` |
| GPIO 与控制信号 | BOOT0 引脚 | `controller_pin=U6 PB8/BOOT0 pin46`；`external_connection=null` |
| 内存与 Flash | 外部存储器 | `external_flash=null`；`eeprom=null`；`external_sram=null`；`sd_card=null` |
| 总线地址 | 正文 I2C 地址 0x64 | `documented_address=0x64`；`controller=U6 STM32G431CBU6`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`schematic_address=null` |
| 内存与 Flash | 正文 MCU 内存、内核与频率 | `mcu=U6 STM32G431CBU6`；`documented_core=Cortex-M4`；`documented_flash=128KB`；`documented_sram=32KB`；`documented_clock=170MHz`；`schematic_internal_memory=null` |
| 接口 | 正文 OLED 规格 | `connector=J2 FH43SRJ-20S-0.5SH`；`documented_size=0.66 inch`；`documented_resolution=64x48`；`bus=SPI`；`display_controller=null` |
| 核心器件 | 正文电机与 FOC 控制性能 | `documented_motor=D3504 200KV`；`documented_control=FOC current/speed/position loops`；`driver=U9 DRV8311HRRWR`；`encoder=U7 TLE5012BE1000`；`firmware_parameters=null` |
| 电源 | 正文供电与负载性能 | `documented_can_supply=6-16V`；`documented_grove=5V`；`documented_phase_current=0.5A continuous,1A short`；`documented_max_load=500g`；`documented_torque=0.021Nm@5V;0.065Nm@CAN supply`；`schematic_rating=null` |
| 接口 | 正文 CAN 连接器数量与类型 | `documented_count=2`；`documented_type=XT30 (2+2) PW-M`；`schematic_nets=GND,PVIN,EXT_CANH,EXT_CANL`；`connector_references=null`；`pinout=null` |
| 总线 | CAN 协议参数 | `controller_bus=FDCAN_TX,FDCAN_RX`；`transceiver=U8 SIT1044QTK/3`；`nominal_bitrate=null`；`data_bitrate=null`；`identifier=null`；`node_address=null`；`protocol=null` |
| 其他事实 | U1 降压芯片型号字样 | `reference=U1`；`visible_marking=LGS(字符待确认)5124`；`function=PVIN to SYS_5V buck`；`confirmed_part_number=null` |

## 待确认事项

- `address.documented-i2c-address`：正文标称 I2C 地址为 0x64；原理图只显示 U6 与 J5 的 SYS_I2C_SCL/SDA 连接，没有地址选择电阻、地址文字或固件寄存器。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6/J5 I2C 网络，图中无 0x64）
- `memory.documented-mcu-spec`：正文称 STM32G431CBU6 为 Cortex-M4、128KB Flash、32KB SRAM、170MHz；原理图仅确认 U6 型号，没有展开片内存储、内核或时钟频率。（证据：图 930210237083 / 第 1 页 / 第 1 页网格 A2-B3，U6 型号字段与外部引脚）
- `interface.documented-oled`：正文称 OLED 为 0.66 英寸、64×48、SPI；原理图确认 J2 的 SPI/控制与 OLED_VDD，但未标显示器控制器、尺寸或分辨率。（证据：图 930210237083 / 第 1 页 / 第 1 页 J2 与 OLED_* 网络，无型号、尺寸或分辨率文字）
- `component.documented-motor-control`：正文称采用 D3504 200KV 电机、FOC 闭环及电流/速度/位置三环控制；原理图确认 MCU、DRV8311 与 TLE5012 连接，但未标电机型号、FOC 算法、控制环参数或机械角度误差。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6/U9/U7 与 J4 电机接口）
- `power.documented-ratings`：正文称 CAN 供电为 6-16V、Grove 供电为 5V，并给出相电流、转速、负载、扭矩、待机电流和过压行为；原理图显示 PVIN/VIN 和电源路径，但未打印这些范围、性能或测试条件。（证据：图 930210237083 / 第 1 页 / 第 1 页 PVIN/VIN/U1/U9/J5 电源与驱动路径，无性能表）
- `interface.documented-can-connectors`：正文称有 2 个 XT30 (2+2) PW-M CAN 接口；原理图只引出 GND、PVIN、EXT_CANH、EXT_CANL 网络，没有显示两个连接器的位号、型号或针脚编号。（证据：图 930210237083 / 第 1 页 / 第 1 页网格 A4，外部 CAN/电源网络标签，无 XT30 连接器符号）
- `bus.documented-can-parameters`：原理图确认 FDCAN_TX/FDCAN_RX、CAN_STB 和 CANH/CANL 电气连接，但未给 CAN nominal/data bitrate、标识符格式、节点地址、帧协议或终端启停方式。（证据：图 930210237083 / 第 1 页 / 第 1 页 U6/U8 CAN 网络及 R16 120R，图中无通信参数）
- `other.regulator-marking`：原理图 U1 型号文字在本地页面中只能辨认为 LGS(字符待确认)5124；其降压功能可由 BST/EN/IN/SW/FB 与外围连接确认，但完整料号需 BOM 或高清源文件确认。（证据：图 930210237083 / 第 1 页 / 第 1 页网格 A1，U1 型号文字与 BST/EN/IN/SW/FB 引脚）
- `review.i2c-address`：请用 U188-Lite 当前固件、协议或总线扫描确认默认 I2C 地址 0x64 及修改规则。；原因：原理图未标地址或硬件地址选择。
- `review.mcu-spec`：请用 STM32G431CBU6 资料确认 Cortex-M4、128KB Flash、32KB SRAM 和 170MHz。；原因：板级原理图未展开 MCU 内部资源。
- `review.oled-spec`：请用 OLED BOM 或规格确认 0.66 英寸、64×48、控制器型号和 FPC 引脚定义。；原因：原理图只显示 J2 电气接口。
- `review.motor-control`：请用电机 BOM、固件和控制参数确认 D3504 200KV、FOC 三环实现、编码器标定与位置误差。；原因：板级连线不能证明电机机械规格或控制算法。
- `review.power-ratings`：请用量产规格和测试记录确认 6-16V/5V 供电边界、相电流、负载、转速、扭矩、待机与过压行为。；原因：原理图未标这些性能值和热边界。
- `review.can-connectors`：请用 PCB、BOM 或装配图确认两个 XT30 (2+2) PW-M 连接器的位号、针脚和并联关系。；原因：当前原理图页只显示外部网络标签，没有连接器符号。
- `review.can-parameters`：请用当前固件和 CAN 协议确认 nominal/data bitrate、标识符格式、节点地址、帧定义及 R16 终端策略。；原因：原理图只确认物理层电路。
- `review.regulator-part`：请用 BOM 或高清源文件确认 U1 降压芯片完整型号。；原因：本地原理图型号文字无法无歧义辨认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `930210237083c8f1754136113800c39b332c601db47644194b4ae6b8c4d5817c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/778/sch_Unit-RollerCAN_V1.0_page_01.png` |

---

源文档：`zh_CN/unit/Unit-RollerCAN Lite.md`

源文档 SHA-256：`45b052756df41820ec21955530cfc6dfc2916e4bdc8e7c896bc4b67c73b6c80d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
