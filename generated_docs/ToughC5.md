# ToughC5 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | ToughC5 |
| SKU | K162 |
| 产品 ID | `toughc5-79d51395fbd2` |
| 源文档 | `zh_CN/core/ToughC5.md` |

## 概述

ToughC5 以 ESP32-C5HR8 为主控，外置 XM25UH128DHIQT 16MB SPI Flash，并配置 StampTimerPower2 电源管理、IO_EXP 扩展器、RX8130CE RTC 与 microSD。USB-C 的 5V_IN 与电池 VBAT 汇入 M1 电源管理，M1 提供 5V_INOUT 以及 3V3_L0、3V3_L2、3V3_L2_LDO 等分级电源轨，再由 M5BUS、LCD、TF 和 GROVE 各自的 LDO 或负载开关生成域电源。2.4GHz 与 5GHz 射频经 U4 合路到 IPEX-4 天线座，显示与触控分别通过 10Pin LCD FPC 和 6Pin 触控 FPC 接入。主要数字连接包括 G2_SDA/G3_SCL 的 I2C、G7_MOSI/G8_MISO/G9_SCK 的 SPI、USB_P/USB_N、UART0 信号 G11_PC_TX/G12_PC_RX 以及 30Pin M5BUS 扩展接口。

## 检索关键词

`ToughC5`、`K162`、`ESP32-C5HR8`、`XM25UH128DHIQT`、`StampTimerPower2`、`M5PM1`、`IO_EXP`、`M5IOE1`、`RX8130CE`、`LFD182G45DCHD481`、`TXB0104RUTR`、`MTXS0102DQER`、`MT9700-N`、`TPAP7343D-33FS4`、`USB_C_16P_Horizontal`、`ICMF062P900MFR`、`HC-FPC-0.5-10P-FH20`、`IPEX_4`、`M5BUS`、`3V3_L0`、`3V3_L2`、`3V3_L2_LDO`、`5V_IN`、`5V_INOUT`、`VBAT`、`G2_SDA`、`G3_SCL`、`G7_MOSI`、`G8_MISO`、`G9_SCK`、`G11_PC_TX`、`G12_PC_RX`、`G23_RX`、`G24_TX`、`PM_RTC_INT`、`PYB_LCD_EN`、`PYB_TF_EN`、`PM_BUZZER_EN`、`USB_P`、`USB_N`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-C5HR8 | 主控 SoC，提供 2.4GHz/5GHz 射频端口、SPI、I2C、UART、USB 与 GPIO | 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区：U3 型号 ESP32-C5HR8，ANT_5G/ANT_2G、XTAL_P/XTAL_N 与 GPIO 引脚 |
| U6 | XM25UH128DHIQT | 16MB SPI Flash | 图 7462e5815f4a / 第 1 页 / 16MB Flash 区：U6 型号 XM25UH128DHIQT 与 8 脚 SPI 引脚 |
| M1 | StampTimerPower2 | 电源管理芯片，I2C 地址 0x6E，产生多级 3.3V 与 5V_INOUT 电源 | 图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 型号 StampTimerPower2、IIC Address:0X6E 与电源引脚 |
| U5 | 未标注 | IO_EXP 扩展器，I2C 地址 0x4F，控制 LCD、背光、TF、充电与复位信号 | 图 7462e5815f4a / 第 1 页 / PYB IOEXP 区：U5、IIC Address:0X4F 与 IO_EXP 符号 |
| U4 | LFD182G45DCHD481 | 双频射频前端器件，将 H_PORT/L_PORT 合路到 CM 并接天线座 | 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区右侧：U4 型号 LFD182G45DCHD481 与 H_PORT/L_PORT/CM 引脚 |
| U8 | RX8130CE:B3 | I2C 实时时钟，带独立 VBAT 与中断输出 | 图 577c50e9cbeb / 第 1 页 / RTC 区：U8 型号 RX8130CE:B3 与 VIO/VDD/VBAT/SCL/SDA/nIRQ 引脚 |
| U11 | TXB0104RUTR | microSD 四路电平转换器 | 图 577c50e9cbeb / 第 1 页 / TF CARD 区：U11 TXB0104RUTR 与 VCCB/VCCA、B1-B3/A1-A3、OE 引脚 |
| U2 | MTXS0102DQER | GROVE I2C 双向电平转换器 | 图 577c50e9cbeb / 第 1 页 / GROVE 区：U2 MTXS0102DQER 与 GROVE_SCL/GROVE_SDA、G3_SCL/G2_SDA |
| U12 | MTXS0102DQER | M5BUS I2C 双向电平转换器 | 图 5ca658961967 / 第 1 页 / M5BUS 区：U12 MTXS0102DQER 与 MBUS_SCL/MBUS_SDA |
| U13 | MTXS0102DQER | M5BUS GPIO 电平转换器 | 图 5ca658961967 / 第 1 页 / M5BUS 区：U13 MTXS0102DQER 与 G27/G28_BOOT6、MBUS_G27/MBUS_G28 |
| U9 | MT9700-N | LCD 电源负载开关，限流设定为 340mA | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区：U9 MT9700-N、VIN/VOUT/EN/SET 与 340mA 标注 |
| U7 | MT9700-N | microSD 电源负载开关，限流设定为 340mA | 图 577c50e9cbeb / 第 1 页 / TF CARD 区：U7 MT9700-N、VIN/VOUT/EN/SET 与 340mA 标注 |
| U10 | TPAP7343D-33FS4 | M5BUS 3.3V LDO | 图 5ca658961967 / 第 1 页 / M5BUS 区右侧：U10 TPAP7343D-33FS4、VIN/OUT/EN、C3/C2 |
| U1 | TPAP7343D-33FS4 | GROVE 3.3V LDO | 图 577c50e9cbeb / 第 1 页 / GROVE 区：U1 TPAP7343D-33FS4、VIN/OUT/EN、C64/C63 |
| Q1 | HL2301A | LCD 背光 P-MOS 高侧开关 | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区背光：Q1 HL2301A 与 BL_3V3_L3B、R60、R50 |
| Q2 | 2N7002W | LCD 背光使能 N-MOS 驱动 | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区背光：Q2 2N7002W、PYB_BL_EN、R52 |
| Q3 | 2N7002W | 蜂鸣器低边开关 | 图 577c50e9cbeb / 第 1 页 / BUZZER 区：Q3 2N7002W、PM_BUZZER_EN、R53 |
| Q4 | 2N7002DW | 触摸 I2C SCL 双向电平转换 MOS | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区：Q4A/Q4B 2N7002DW、G3_SCL 与 TP_SCL |
| Q5 | 2N7002DW | 触摸 I2C SDA 双向电平转换 MOS | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区：Q5A/Q5B 2N7002DW、G2_SDA 与 TP_SDA |
| D5 | TPBT4148-1006 | 充电状态信号二极管 | 图 7462e5815f4a / 第 1 页 / PYB IOEXP 区下方：D5 TPBT4148-1006、PYB_CHG_STAT 与 CHG_STAT |
| D6 | 1N4148W | 蜂鸣器续流二极管 | 图 577c50e9cbeb / 第 1 页 / BUZZER 区：D6 1N4148W 并联于蜂鸣器两端 |
| BUZZER1 | MLT-8530 | 板载无源蜂鸣器 | 图 577c50e9cbeb / 第 1 页 / BUZZER 区：BUZZER1 MLT-8530 及 1/2 脚 |
| X1 | CN4048M000B17A822001 | 主控晶振，连接 XTAL_P/XTAL_N | 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区顶部：X1 CN4048M000B17A822001、C19/C20、L1 |
| J1 | USB_C_16P_Horizontal | USB Type-C 输入与数据连接器 | 图 5ca658961967 / 第 1 页 / USB C IN 区：J1 USB_C_16P_Horizontal |
| JP1 | 未标注 | 4Pin USB 扩展点：5V_IN、GND、USB_N、USB_P | 图 5ca658961967 / 第 1 页 / USB C IN 区右侧：JP1 与 1~4 脚网络 |
| JP2 | 未标注 | 2Pin 电池输入/输出接口，连接 VBAT | 图 5ca658961967 / 第 1 页 / BAT IN/OUT 区：JP2 2/1 脚与 VBAT |
| S1 | 未标注 | 电源按键，产生 PWR_BTN 信号 | 图 5ca658961967 / 第 1 页 / KEY 区：S1、PWR_BTN、C6、DR3 |
| JP3 | 未标注 | 30Pin M5BUS 扩展接口 | 图 5ca658961967 / 第 1 页 / M5BUS 区：JP3 30Pin 与 1~30 脚网络 |
| JP4 | HC-FPC-0.5-10P-FH20 | 10Pin LCD FPC 连接器 | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区：JP4 HC-FPC-0.5-10P-FH20 与 1~10/SH 脚 |
| JP5 | 未标注 | 6Pin C-TP 触控 FPC 连接器 | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区右下方：JP5 C-TP 与 1~6/SH 脚 |
| JP6 | 未标注 | 4Pin GROVE/I2C 扩展接口 | 图 577c50e9cbeb / 第 1 页 / GROVE 区：JP6 1~4 脚与 GND、5V_INOUT、GROVE_SDA、GROVE_SCL |
| JP7 | 未标注 | 2Pin RTC 备用电池接口 | 图 577c50e9cbeb / 第 1 页 / RTC 区：JP7 与 RTC_BAT、GND |
| J2 | TF_Card | microSD 卡座 | 图 577c50e9cbeb / 第 1 页 / TF CARD 区右侧：J2 TF_Card 与 DATA/CMD/VDD/CLK/VSS/DET 引脚 |
| J3 | IPEX_4 | 2.4GHz/5GHz 天线连接器 | 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区右侧：J3 IPEX_4 与 U4 CM 输出 |
| BAT1 | C80909/MS621FE-FL11E | RTC 备用电池 | 图 577c50e9cbeb / 第 1 页 / RTC 区：BAT1 C80909/MS621FE-FL11E 与 RTC_BAT |
| D1 / D2 / D4 | ESD0524P | M5BUS GPIO 与 UART/SPI 信号的多路 ESD 保护 | 图 5ca658961967 / 第 1 页 / M5BUS 区：D2/D4/D1 均为 ESD0524P，IN1~IN4 接对应信号 |
| D7 | ESD0524P | 触控中断、I2C 与复位信号 ESD 保护 | 图 577c50e9cbeb / 第 1 页 / LCD & TP 区左下方：D7 ESD0524P 与 PM_TP_INT/TP_SDA/TP_SCL/PM_TP_RST |
| DR1-DR13 | ESD5311 | USB、按键、M5BUS、microSD、触控与 GROVE 信号 TVS 保护 | 图 5ca658961967 / 第 1 页 / 第 2 页：DR1~DR6、DR13 为 ESD5311; 图 577c50e9cbeb / 第 1 页 / 第 4 页：DR7~DR12 为 ESD5311 |

## 系统结构

### ToughC5

系统定义 L0 Shipping、L1 Standby、L2 DeepSleep、L3A CORE ACTIVE、L3B ALL ACTIVE 五个电源状态；ESP32-C5 与 PY B 从 L2 起有效，TP 从 L3A 起有效，M5BUS、LCD、蜂鸣器与 GROVE 位于 L3B。

- 参数与网络：`states=L0/L1/L2/L3A/L3B`；`l2=ESP32-C5,PY B`；`l3a=TP`；`l3b=M5BUS,LCD,BUZZER,GROVE`
- 证据：图 65f28dc6f899 / 第 1 页 / 右上 PowerMode 表与 Power Mode Switch 区：L0/L1/L2/L3A/L3B

### ToughC5

L1 上电后自动开启；PWR_BTN 或 CHG_STAT 触发 L2，随后开启 L3A 与 L3B；软件睡眠关闭 L2、L3A、L3B，TP_INT 用于退出睡眠。

- 参数与网络：`entry=PWR_BTN,CHG_STAT`；`sleep_exit=TP_INT`；`levels=L1->L2->L3A->L3B`
- 证据：图 65f28dc6f899 / 第 1 页 / 左下 Power Mode Switch：L0~L3B 状态与转换文字

## 核心器件

### U3

U3 为 ESP32-C5HR8，CHIP_PU 为第 9 脚，XTAL_P/XTAL_N 为第 6/5 脚，ANT_5G/ANT_2G 为第 48/42 脚。

- 参数与网络：`part=ESP32-C5HR8`；`chip_pu_pin=9`；`xtal_p_pin=6`；`xtal_n_pin=5`；`ant_5g_pin=48`；`ant_2g_pin=42`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区：U3 ESP32-C5HR8 与 5/6/9/42/48 脚

### M1

M1 为 StampTimerPower2 电源管理器件，I2C 地址为 0x6E，负责 5V、VBAT、系统 VBUS 与多路 3.3V 电源。

- 参数与网络：`part=StampTimerPower2`；`i2c_address=0x6E`
- 证据：图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 StampTimerPower2、IIC Address:0X6E

### U5

U5 为 IO_EXP 扩展器，I2C 地址 0x4F，VCC 接 3V3_L2，VSS 接地。

- 参数与网络：`schematic_name=IO_EXP`；`i2c_address=0x4F`；`vcc=3V3_L2`
- 证据：图 7462e5815f4a / 第 1 页 / PYB IOEXP 区：U5 IO_EXP、IIC Address:0X4F、VCC/VSS

### U4

U4 为 LFD182G45DCHD481，H_PORT 接 ANT_5G 匹配网络，L_PORT 接 ANT_2G 匹配网络，CM 经 L3(0R) 接 J3 IPEX_4。

- 参数与网络：`part=LFD182G45DCHD481`；`high_port=H_PORT`；`low_port=L_PORT`；`combined=CM`；`antenna=J3 IPEX_4`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区右侧：U4、L2/L4、L3 与 J3

### U8

U8 为 RX8130CE:B3 RTC，VIO(1) 与 VDD(8) 接 3V3_L0，VBAT(10) 经 R64(0R) 接 RTC_BAT，SCL(2)/SDA(3) 接 G3_SCL/G2_SDA。

- 参数与网络：`part=RX8130CE:B3`；`vio_pin=1`；`vdd_pin=8`；`vbat_pin=10`；`scl_pin=2`；`sda_pin=3`
- 证据：图 577c50e9cbeb / 第 1 页 / RTC 区：U8 与 1/8/10/2/3 脚

### U11 / U12 / U13 / U2

U11 为 TXB0104RUTR 四路转换器，U12/U13/U2 为 MTXS0102DQER 两路转换器，分别服务 microSD、M5BUS I2C、M5BUS GPIO 与 GROVE I2C。

- 参数与网络：`sd=U11 TXB0104RUTR`；`m5bus_i2c=U12 MTXS0102DQER`；`m5bus_gpio=U13 MTXS0102DQER`；`grove_i2c=U2 MTXS0102DQER`
- 证据：图 5ca658961967 / 第 1 页 / M5BUS 区：U12/U13 MTXS0102DQER; 图 577c50e9cbeb / 第 1 页 / TF CARD 区 U11 TXB0104RUTR；GROVE 区 U2 MTXS0102DQER

## 电源

### M1

M1 的 5V_IN(16)、EXT_5V_INOUT(18)、VBAT(20)、SYS_VBUS(24) 分别连接对应电源网络；DCDC_3V3_OUT(26) 输出 3V3_L2，LDO_3V3_OUT(28) 输出 3V3_L2_LDO，3V3_ALWAYS_ON(22) 输出 3V3_L0。

- 参数与网络：`5v_in_pin=16`；`ext_5v_inout_pin=18`；`vbat_pin=20`；`sys_vbus_pin=24`；`dcdc_3v3_pin=26`；`ldo_3v3_pin=28`；`always_3v3_pin=22`
- 证据：图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 16/18/20/24/26/28/22 脚与输出网络

### J1

J1 的 VBUS 由 A4/B9 与 B4/A9 并联引出 5V_IN；CC1(A5)、CC2(B5) 分别经 R2、R3(5.1K) 下拉到 GND。

- 参数与网络：`vbus_pins=A4/B9,B4/A9`；`cc1_pin=A5`；`cc2_pin=B5`；`cc_pulldown=R2/R3 5.1K`
- 证据：图 5ca658961967 / 第 1 页 / USB C IN 区：J1 VBUS、CC1/CC2、R2/R3

### JP2

JP2 第 2 脚接 VBAT，第 1 脚接 GND；VBAT 由 C4(100nF/16V) 与 C5(10uF/10V) 对地滤波。

- 参数与网络：`pin2=VBAT`；`pin1=GND`；`c4=100nF/16V`；`c5=10uF/10V`
- 证据：图 5ca658961967 / 第 1 页 / BAT IN/OUT 区：JP2、VBAT、C4/C5

### U10 / U1

U10 将 5V_INOUT 转为 M5BUS_3V3_L3B，U1 将 5V_INOUT 转为 GROVE_3V3_L3B；两者的 EN 脚均接各自 VIN，C3/C63(10uF) 接输入，C2/C64(1uF) 接输出。

- 参数与网络：`m5bus_ldo=U10 TPAP7343D-33FS4`；`grove_ldo=U1 TPAP7343D-33FS4`；`input=5V_INOUT`；`outputs=M5BUS_3V3_L3B,GROVE_3V3_L3B`
- 证据：图 5ca658961967 / 第 1 页 / M5BUS 区右侧：U10、C2/C3、5V_INOUT; 图 577c50e9cbeb / 第 1 页 / GROVE 区：U1、C63/C64、5V_INOUT

### U9 / U7

U9 以 3V3_L2_LDO 为输入生成 LCD_3V3_L3B，U7 以 3V3_L2 为输入生成 TF_3V3_L3B；两路 MT9700-N 的 SET 脚分别接 R47/R35(20K) 到地并标注 340mA，EN 脚分别由 R49/R37(100K) 下拉。

- 参数与网络：`lcd_switch=U9 MT9700-N`；`sd_switch=U7 MT9700-N`；`current_limit=340mA`；`lcd_output=LCD_3V3_L3B`；`sd_output=TF_3V3_L3B`
- 证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区 U9；TF CARD 区 U7；两处 340mA 标注

### Q1 / Q2

3V3_L2_LDO 经 R60(4.7R/5%) 接 Q1(HL2301A) 源极，Q1 漏极输出 BL_3V3_L3B；Q2(2N7002W) 的栅极接 PYB_BL_EN，R50/R52 均为 100K，C56 为 100nF/16V。

- 参数与网络：`pmos=Q1 HL2301A`；`nmos=Q2 2N7002W`；`series_r=R60 4.7R 5%`；`enable=PYB_BL_EN`；`output=BL_3V3_L3B`
- 证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区背光：R60、Q1、Q2、R50/R52、C56

### M1

M1 引出的电源网络配置 C7(10uF/25V)、C8(1uF/100V)、C9(10uF/100V)、C10/C11(100nF/16V)，3V3_L2 与 3V3_L2_LDO 另配 C58/C59(22uF/16V)、C12/C14(100nF/16V)、C13(10uF/16V)、C1/C15(1uF/16V)。

- 参数与网络：`input_caps=C7,C8,C9,C10,C11`；`dcdc_caps=C58,C59,C12,C14`；`ldo_caps=C13,C1,C15`
- 证据：图 5ca658961967 / 第 1 页 / TimerPower2 区左侧：C7~C11、C58/C59、C12~C15

## 接口

### J1 / JP1

J1 的 DP1/DP2(A6/B6) 与 DM1/DM2(A7/B7) 汇合为 USB_P/USB_N，经 FT1(ICMF062P900MFR) 连接 JP1 的 USB_P/USB_N；JP1 第 1/2/3/4 脚依次为 5V_IN、GND、USB_N、USB_P。

- 参数与网络：`dp=A6/B6`；`dm=A7/B7`；`filter=FT1 ICMF062P900MFR`；`jp1_pin1_4=5V_IN,GND,USB_N,USB_P`
- 证据：图 5ca658961967 / 第 1 页 / USB C IN 区：J1、FT1、USB_P/USB_N 与 JP1

### JP3

JP3 30Pin M5BUS 的奇数脚 1/3/5 为 GND，7/9/11 为 G7_MOSI/G8_MISO/G9_SCK，13/15 为 G12_PC_RX，17/19 为 MBUS_SDA，21/23 为 G23_RX/MBUS_G27；偶数脚 2/4/6 为 G0/G1/CHIP_EN，8/10/12 为 G4/G6/M5BUS_3V3_L3B，14/16 为 G11_PC_TX，18/20 为 MBUS_SCL，22/24 为 G24_TX/MBUS_G28，26/28/30 为 G5/5V_INOUT/VBAT。

- 参数与网络：`connector=JP3 30Pin`；`i2c=MBUS_SDA/MBUS_SCL`；`spi=G7_MOSI/G8_MISO/G9_SCK`；`uart=G11_PC_TX/G12_PC_RX,G23_RX/G24_TX`；`power=M5BUS_3V3_L3B,5V_INOUT,VBAT`
- 证据：图 5ca658961967 / 第 1 页 / M5BUS 区：JP3 与 1~30 脚网络名

### JP6

JP6 第 4、3、2、1 脚依次为 GROVE_SCL、GROVE_SDA、5V_INOUT、GND；GROVE_SCL/SDA 经 U2 转换到 G3_SCL/G2_SDA。

- 参数与网络：`pin4=GROVE_SCL`；`pin3=GROVE_SDA`；`pin2=5V_INOUT`；`pin1=GND`；`translator=U2 MTXS0102DQER`
- 证据：图 577c50e9cbeb / 第 1 页 / GROVE 区：JP6 与 U2

### JP4

JP4 10Pin LCD FPC：1=G7_MOSI，2=G8_MISO，3=G9_SCK，4=G25_LCD_CS，5=PYB_LCD_RST，6=G26_LCD_DC，7=LCD_3V3_L3B，8=GND，9=BL_3V3_L3B，10=GND，SH=GND；数据引脚 1~4 与 6 各串 0R 电阻。

- 参数与网络：`connector=JP4 HC-FPC-0.5-10P-FH20`；`spi=G7_MOSI,G8_MISO,G9_SCK`；`control=G25_LCD_CS,PYB_LCD_RST,G26_LCD_DC`；`power=LCD_3V3_L3B,BL_3V3_L3B`
- 证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区：JP4 与 1~10/SH 脚、R43~R48

### JP5

JP5 C-TP：1=3V3_L2_LDO，2=PM_TP_RST，3=TP_SCL，4=TP_SDA，5=PM_TP_INT，SH=GND；第 1 脚经 R62(0R) 供电，2~5 脚各串 0R 电阻。

- 参数与网络：`connector=JP5 C-TP`；`pin1=3V3_L2_LDO`；`pin2=PM_TP_RST`；`pin3=TP_SCL`；`pin4=TP_SDA`；`pin5=PM_TP_INT`
- 证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区右下方：JP5 C-TP、R62、R56~R59

### J2 / J3

J2 microSD 的 TF_CMD/TF_CLK/TF_D0 分别来自 U11 的 A1/A2/A3，VDD 接 TF_3V3_L3B，PYB_TF_DET 接卡检测脚；J3 为 IPEX_4 天线座，经 L3(0R) 接 U4 的 CM。

- 参数与网络：`sd_cmd=TF_CMD`；`sd_clk=TF_CLK`；`sd_d0=TF_D0`；`sd_detect=PYB_TF_DET`；`antenna=J3 IPEX_4`
- 证据：图 577c50e9cbeb / 第 1 页 / TF CARD 区右侧 J2；RTC/TF 区上方 U11; 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区右侧：U4 CM、L3、J3 IPEX_4

## 总线

### G2_SDA / G3_SCL

G2_SDA/G3_SCL 连接 M1(0x6E)、U5(0x4F)、U8 RTC 及 U2/Q4/Q5 触控转换链路，并由 R20/R21(2.2K) 上拉到 3V3_L2。

- 参数与网络：`sda=G2_SDA`；`scl=G3_SCL`；`pullups=R20/R21 2.2K`；`devices=M1 0x6E,U5 0x4F,U8,U2/Q4/Q5`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区左侧：R20/R21、G2_SDA/G3_SCL；U5 I2C 脚; 图 5ca658961967 / 第 1 页 / TimerPower2 区：G3_SCL/G2_SDA 与 M1; 图 577c50e9cbeb / 第 1 页 / RTC 区 U8；GROVE 区 U2；LCD & TP 区 Q4/Q5

### U3

U3 第 16~18 脚为 G7_MOSI/G8_MISO/G9_SCK，直接接 LCD JP4 并经 U11 转成 TF 信号；U6 Flash 使用独立的 FLASH_CS0/SPIQ/SPIWP/SPIHD/SPICLK/SPID，经 R18/R19/R22/R23/R24 接到 U3 第 26~31 脚。

- 参数与网络：`lcd_sd_spi=G7_MOSI,G8_MISO,G9_SCK`；`mcu_pins=16,17,18`；`flash_spi=FLASH_CS0,FLASH_SPIQ,FLASH_SPIWP,FLASH_SPIHD,FLASH_SPICLK,FLASH_SPID`；`flash_resistors=R18,R19,R22,R23,R24`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区：U3 16~18、26~31 脚与 FLASH SPI 网络

### U3

U3 的 U0TXD(20)/U0RXD(21) 形成 G11_PC_TX/G12_PC_RX，TXD 串联 R16(499R)，两路信号同时引到 JP3 的 13/15 与 14/16 脚；G23_RX/G24_TX 接 JP3 的 21/22 脚。

- 参数与网络：`uart0_tx=U0TXD/G11_PC_TX`；`uart0_rx=U0RXD/G12_PC_RX`；`series_resistor=R16 499R`；`rs485_uart=G23_RX/G24_TX`；`m5bus_pins=13,14,15,16,21,22`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区：U3 20/21/33/34 脚、R16; 图 5ca658961967 / 第 1 页 / M5BUS 区：JP3 13/14/15/16/21/22 脚

### U3 / U4

ANT_5G(48) 经 L2(0.8nH)、C31/C32(0.2pF) 接 U4 H_PORT；ANT_2G(42) 经 L4(2.7nH)、C35(0.5pF)、C36(1pF) 接 U4 L_PORT。

- 参数与网络：`ant_5g_pin=48`；`ant_2g_pin=42`；`5g_match=L2 0.8nH,C31 0.2pF,C32 0.2pF`；`2g_match=L4 2.7nH,C35 0.5pF,C36 1pF`；`frontend=U4 LFD182G45DCHD481`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区右侧：ANT_5G/ANT_2G 匹配网络与 U4

## GPIO 与控制信号

### U5

U5 的 PYG10_PWM4=PYB_BL_EN，PYG4_ADC2=PYB_LCD_RST，PYG5_ADC3=PYB_LCD_EN，PYG1=PYB_CHG_PROG，PYG3=PYB_CHG_STAT，PYG6=PYB_TF_EN，PYG14=PYB_TF_DET。

- 参数与网络：`pyg10=PYB_BL_EN`；`pyg4=PYB_LCD_RST`；`pyg5=PYB_LCD_EN`；`pyg1=PYB_CHG_PROG`；`pyg3=PYB_CHG_STAT`；`pyg6=PYB_TF_EN`；`pyg14=PYB_TF_DET`
- 证据：图 7462e5815f4a / 第 1 页 / PYB IOEXP 区：U5 PYG1/PYG3/PYG4/PYG5/PYG6/PYG10/PYG14 网络

### Q4 / Q5

G3_SCL 经 Q4A/Q4B 转成 TP_SCL，G2_SDA 经 Q5A/Q5B 转成 TP_SDA；TP_SCL/TP_SDA 侧由 R12/R65(2.2K) 上拉到 3V3_L2_LDO。

- 参数与网络：`scl=G3_SCL <-> TP_SCL`；`sda=G2_SDA <-> TP_SDA`；`pullups=R12/R65 2.2K`；`rail=3V3_L2_LDO`
- 证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区左侧：Q4A/Q4B、Q5A/Q5B、R12/R65

### Q3

PM_BUZZER_EN 驱动 Q3(2N7002W) 栅极，栅极由 R53(100K) 下拉；Q3 漏极接 BUZZER1 第 2 脚，源极接地，R51(10R) 串在 3V3_L2 与蜂鸣器第 1 脚之间。

- 参数与网络：`enable=PM_BUZZER_EN`；`nmos=Q3 2N7002W`；`gate_pulldown=R53 100K`；`series_r=R51 10R`；`buzzer=BUZZER1 MLT-8530`
- 证据：图 577c50e9cbeb / 第 1 页 / BUZZER 区：PM_BUZZER_EN、Q3、R51/R53、BUZZER1

## 时钟

### X1

X1(CN4048M000B17A822001) 的 1/3 脚接 XTAL_P/XTAL_N，2/4 脚接地；XTAL_P 与 XTAL_N 分别通过 C19/C20(15pF/50V) 到地，XTAL_P 路径串接 L1(24nH)。

- 参数与网络：`part=CN4048M000B17A822001`；`load_caps=C19/C20 15pF/50V`；`series_l=L1 24nH`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区顶部：X1、C19/C20、L1、XTAL_P/XTAL_N

## 复位

### U3

CHIP_EN 网络由 R14(10K) 上拉到 3V3_L2，并由 C30(1uF/16V) 对地，同时连接到 U3 的 CHIP_PU(9) 与 U5 的 NRST(1)。

- 参数与网络：`pullup=R14 10K`；`cap=C30 1uF/16V`；`mcu_pin=CHIP_PU/9`；`ioexp_pin=NRST/1`
- 证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区左侧 CHIP_EN/R14/C30；PYB IOEXP 区 R26

### U5

U5 的 NRST(1) 经 R26(0R) 接 CHIP_EN，OD_INTOUT(2) 悬空。

- 参数与网络：`nrst_pin=1`；`series_r=R26 0R`；`reset_net=CHIP_EN`；`od_intout=NC`
- 证据：图 7462e5815f4a / 第 1 页 / PYB IOEXP 区：U5 NRST、R26、OD_INTOUT

## 保护电路

### ESD arrays

USB_P/USB_N 由 DR1/DR2(ESD5311) 保护；M5BUS 信号由 D2/D4/D1(ESD0524P) 与 DR4/DR5/DR13 保护；microSD 由 DR9~DR12、触控由 D7(ESD0524P)、GROVE 由 DR7/DR8 保护。

- 参数与网络：`usb=DR1/DR2 ESD5311`；`m5bus=D1/D2/D4 ESD0524P`；`sd=DR9-DR12 ESD5311`；`touch=D7 ESD0524P`；`grove=DR7/DR8 ESD5311`
- 证据：图 5ca658961967 / 第 1 页 / USB C IN 区 DR1/DR2；M5BUS 区 D1/D2/D4/DR4/DR5/DR13; 图 577c50e9cbeb / 第 1 页 / GROVE 区 DR7/DR8；TF CARD 区 DR9~DR12；LCD & TP 区 D7

## 关键网络

### 3V3_L0

3V3_L0 由 M1 的 3V3_ALWAYS_ON(22) 产生，供 U8 RTC 的 VIO/VDD 与 R33 上拉使用。

- 参数与网络：`source=M1 pin22`；`loads=U8 VIO/VDD,R33`
- 证据：图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 22 脚 3V3_ALWAYS_ON/3V3_L0; 图 577c50e9cbeb / 第 1 页 / RTC 区：3V3_L0、U8 VIO/VDD、R33

### 3V3_L2

3V3_L2 由 M1 的 DCDC_3V3_OUT(26) 产生，连接 U3 电源脚、U5 VCC、U11/U12/U13 的 VCCB、U2 的 VCCA、TF/U7 输入以及 I2C 上拉。

- 参数与网络：`source=M1 pin26`；`loads=U3,U5,U11,U12,U13,U2,U7,R20/R21`
- 证据：图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 26 脚 DCDC_3V3_OUT/3V3_L2; 图 7462e5815f4a / 第 1 页 / 03 MCU Core 区与 PYB IOEXP 区：3V3_L2 电源网络

## 存储

### U6

U6(XM25UH128DHIQT) 的 VCC(8) 接 VDD_SPI 并用 C47(1uF/16V) 去耦，VSS(4) 接地；CS#/SO/WP#/HOLD#/SCLK/SI 分别接 FLASH_CS0/SPIQ/SPIWP/SPIHD/SPICLK/SPID。

- 参数与网络：`part=XM25UH128DHIQT`；`size=128Mbit/16MB`；`vcc_pin=8`；`vss_pin=4`；`decoupling=C47 1uF/16V`
- 证据：图 7462e5815f4a / 第 1 页 / 16MB Flash 区：U6、C47 与 1~8 脚网络

### J2

microSD J2 的 TF_CMD/TF_CLK/TF_D0 来自 U11 转换侧 A1/A2/A3，PYB_TF_DET 接卡检测脚并由 R63(10K) 下拉、C51(1uF) 对地；TF_3V3_L3B 由 U7 负载开关产生并用 C50(100nF) 去耦。

- 参数与网络：`connector=J2 TF_Card`；`cmd=TF_CMD`；`clk=TF_CLK`；`data0=TF_D0`；`detect=PYB_TF_DET`；`detect_pulldown=R63 10K`；`rail=TF_3V3_L3B`
- 证据：图 577c50e9cbeb / 第 1 页 / TF CARD 区：U11、U7、J2、R63、C50/C51

## 其他事实

### U8

U8 的 nIRQ(6) 为 PM_RTC_INT，并由 R33(100K) 上拉到 3V3_L0；VBAT(10) 经 R64(0R) 接 RTC_BAT 与 BAT1，C16(1nF/10V) 对地；nRSTO(5) 与 FOUT(4) 悬空。

- 参数与网络：`irq_pin=6`；`irq_net=PM_RTC_INT`；`pullup=R33 100K`；`backup_battery=BAT1`；`vbat_r=R64 0R`；`vbat_c=C16 1nF/10V`
- 证据：图 577c50e9cbeb / 第 1 页 / RTC 区：U8 4/5/6/10 脚、R33、R64、C16、BAT1

### BUZZER1

BUZZER1(MLT-8530) 由 3V3_L2 经 R51(10R) 供电，D6(1N4148W) 反向并联于蜂鸣器两端，Q3(2N7002W) 作为低边开关。

- 参数与网络：`buzzer=BUZZER1 MLT-8530`；`series_r=R51 10R`；`flyback=D6 1N4148W`；`switch=Q3 2N7002W`
- 证据：图 577c50e9cbeb / 第 1 页 / BUZZER 区：BUZZER1、R51、D6、Q3

### LED1 / LED2

LED1 为红色充电状态灯，VBAT 经 R27(1K) 接其阳极、CHG_STAT 接其阴极；LED2 为绿色电源灯，LED_PWR_GREEN 经 R9(4.7K) 接其阳极、阴极接地。

- 参数与网络：`led1=RED,CHG_STAT`；`led1_resistor=R27 1K`；`led2=GREEN,LED_PWR_GREEN`；`led2_resistor=R9 4.7K`；`r8=NC`
- 证据：图 5ca658961967 / 第 1 页 / LED 区：R27/R8、LED1 RED、R9、LED2 GREEN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ToughC5 | `states=L0/L1/L2/L3A/L3B`；`l2=ESP32-C5,PY B`；`l3a=TP`；`l3b=M5BUS,LCD,BUZZER,GROVE` |
| 系统结构 | ToughC5 | `entry=PWR_BTN,CHG_STAT`；`sleep_exit=TP_INT`；`levels=L1->L2->L3A->L3B` |
| 核心器件 | U3 | `part=ESP32-C5HR8`；`chip_pu_pin=9`；`xtal_p_pin=6`；`xtal_n_pin=5`；`ant_5g_pin=48`；`ant_2g_pin=42` |
| 核心器件 | M1 | `part=StampTimerPower2`；`i2c_address=0x6E` |
| 核心器件 | M1 | `schematic_name=StampTimerPower2`；`document_name=M5PM1`；`i2c_address=0x6E` |
| 核心器件 | U5 | `schematic_name=IO_EXP`；`i2c_address=0x4F`；`vcc=3V3_L2` |
| 核心器件 | U5 | `schematic_name=IO_EXP`；`document_name=M5IOE1`；`i2c_address=0x4F` |
| 核心器件 | U4 | `part=LFD182G45DCHD481`；`high_port=H_PORT`；`low_port=L_PORT`；`combined=CM`；`antenna=J3 IPEX_4` |
| 核心器件 | U8 | `part=RX8130CE:B3`；`vio_pin=1`；`vdd_pin=8`；`vbat_pin=10`；`scl_pin=2`；`sda_pin=3` |
| 核心器件 | U11 / U12 / U13 / U2 | `sd=U11 TXB0104RUTR`；`m5bus_i2c=U12 MTXS0102DQER`；`m5bus_gpio=U13 MTXS0102DQER`；`grove_i2c=U2 MTXS0102DQER` |
| 电源 | M1 | `5v_in_pin=16`；`ext_5v_inout_pin=18`；`vbat_pin=20`；`sys_vbus_pin=24`；`dcdc_3v3_pin=26`；`ldo_3v3_pin=28`；`always_3v3_pin=22` |
| 电源 | J1 | `vbus_pins=A4/B9,B4/A9`；`cc1_pin=A5`；`cc2_pin=B5`；`cc_pulldown=R2/R3 5.1K` |
| 电源 | JP2 | `pin2=VBAT`；`pin1=GND`；`c4=100nF/16V`；`c5=10uF/10V` |
| 电源 | U10 / U1 | `m5bus_ldo=U10 TPAP7343D-33FS4`；`grove_ldo=U1 TPAP7343D-33FS4`；`input=5V_INOUT`；`outputs=M5BUS_3V3_L3B,GROVE_3V3_L3B` |
| 电源 | U9 / U7 | `lcd_switch=U9 MT9700-N`；`sd_switch=U7 MT9700-N`；`current_limit=340mA`；`lcd_output=LCD_3V3_L3B`；`sd_output=TF_3V3_L3B` |
| 电源 | Q1 / Q2 | `pmos=Q1 HL2301A`；`nmos=Q2 2N7002W`；`series_r=R60 4.7R 5%`；`enable=PYB_BL_EN`；`output=BL_3V3_L3B` |
| 电源 | M1 | `input_caps=C7,C8,C9,C10,C11`；`dcdc_caps=C58,C59,C12,C14`；`ldo_caps=C13,C1,C15` |
| 接口 | J1 / JP1 | `dp=A6/B6`；`dm=A7/B7`；`filter=FT1 ICMF062P900MFR`；`jp1_pin1_4=5V_IN,GND,USB_N,USB_P` |
| 接口 | JP3 | `connector=JP3 30Pin`；`i2c=MBUS_SDA/MBUS_SCL`；`spi=G7_MOSI/G8_MISO/G9_SCK`；`uart=G11_PC_TX/G12_PC_RX,G23_RX/G24_TX`；`power=M5BUS_3V3_L3B,5V_INOUT,VBAT` |
| 接口 | JP6 | `pin4=GROVE_SCL`；`pin3=GROVE_SDA`；`pin2=5V_INOUT`；`pin1=GND`；`translator=U2 MTXS0102DQER` |
| 接口 | JP4 | `connector=JP4 HC-FPC-0.5-10P-FH20`；`spi=G7_MOSI,G8_MISO,G9_SCK`；`control=G25_LCD_CS,PYB_LCD_RST,G26_LCD_DC`；`power=LCD_3V3_L3B,BL_3V3_L3B` |
| 接口 | JP5 | `connector=JP5 C-TP`；`pin1=3V3_L2_LDO`；`pin2=PM_TP_RST`；`pin3=TP_SCL`；`pin4=TP_SDA`；`pin5=PM_TP_INT` |
| 接口 | J2 / J3 | `sd_cmd=TF_CMD`；`sd_clk=TF_CLK`；`sd_d0=TF_D0`；`sd_detect=PYB_TF_DET`；`antenna=J3 IPEX_4` |
| 接口 | RS485 | `uart_nets=G23_RX,G24_TX`；`document_transceiver=SP485EEN-L/TR`；`schematic_presence=not shown on four pages` |
| 接口 | JP4 | `connector=JP4`；`document_controller=ILI9342C`；`schematic_label=not shown` |
| 接口 | JP5 | `connector=JP5 C-TP`；`document_controller=CHSC6540`；`schematic_label=not shown` |
| 总线 | G2_SDA / G3_SCL | `sda=G2_SDA`；`scl=G3_SCL`；`pullups=R20/R21 2.2K`；`devices=M1 0x6E,U5 0x4F,U8,U2/Q4/Q5` |
| 总线 | U3 | `lcd_sd_spi=G7_MOSI,G8_MISO,G9_SCK`；`mcu_pins=16,17,18`；`flash_spi=FLASH_CS0,FLASH_SPIQ,FLASH_SPIWP,FLASH_SPIHD,FLASH_SPICLK,FLASH_SPID`；`flash_resistors=R18,R19,R22,R23,R24` |
| 总线 | U3 | `uart0_tx=U0TXD/G11_PC_TX`；`uart0_rx=U0RXD/G12_PC_RX`；`series_resistor=R16 499R`；`rs485_uart=G23_RX/G24_TX`；`m5bus_pins=13,14,15,16,21,22` |
| 总线 | U3 / U4 | `ant_5g_pin=48`；`ant_2g_pin=42`；`5g_match=L2 0.8nH,C31 0.2pF,C32 0.2pF`；`2g_match=L4 2.7nH,C35 0.5pF,C36 1pF`；`frontend=U4 LFD182G45DCHD481` |
| GPIO 与控制信号 | U5 | `pyg10=PYB_BL_EN`；`pyg4=PYB_LCD_RST`；`pyg5=PYB_LCD_EN`；`pyg1=PYB_CHG_PROG`；`pyg3=PYB_CHG_STAT`；`pyg6=PYB_TF_EN`；`pyg14=PYB_TF_DET` |
| GPIO 与控制信号 | Q4 / Q5 | `scl=G3_SCL <-> TP_SCL`；`sda=G2_SDA <-> TP_SDA`；`pullups=R12/R65 2.2K`；`rail=3V3_L2_LDO` |
| GPIO 与控制信号 | Q3 | `enable=PM_BUZZER_EN`；`nmos=Q3 2N7002W`；`gate_pulldown=R53 100K`；`series_r=R51 10R`；`buzzer=BUZZER1 MLT-8530` |
| 时钟 | X1 | `part=CN4048M000B17A822001`；`load_caps=C19/C20 15pF/50V`；`series_l=L1 24nH` |
| 复位 | U3 | `pullup=R14 10K`；`cap=C30 1uF/16V`；`mcu_pin=CHIP_PU/9`；`ioexp_pin=NRST/1` |
| 复位 | U5 | `nrst_pin=1`；`series_r=R26 0R`；`reset_net=CHIP_EN`；`od_intout=NC` |
| 保护电路 | ESD arrays | `usb=DR1/DR2 ESD5311`；`m5bus=D1/D2/D4 ESD0524P`；`sd=DR9-DR12 ESD5311`；`touch=D7 ESD0524P`；`grove=DR7/DR8 ESD5311` |
| 关键网络 | 3V3_L0 | `source=M1 pin22`；`loads=U8 VIO/VDD,R33` |
| 关键网络 | 3V3_L2 | `source=M1 pin26`；`loads=U3,U5,U11,U12,U13,U2,U7,R20/R21` |
| 存储 | U6 | `part=XM25UH128DHIQT`；`size=128Mbit/16MB`；`vcc_pin=8`；`vss_pin=4`；`decoupling=C47 1uF/16V` |
| 存储 | J2 | `connector=J2 TF_Card`；`cmd=TF_CMD`；`clk=TF_CLK`；`data0=TF_D0`；`detect=PYB_TF_DET`；`detect_pulldown=R63 10K`；`rail=TF_3V3_L3B` |
| 其他事实 | U8 | `irq_pin=6`；`irq_net=PM_RTC_INT`；`pullup=R33 100K`；`backup_battery=BAT1`；`vbat_r=R64 0R`；`vbat_c=C16 1nF/10V` |
| 其他事实 | BUZZER1 | `buzzer=BUZZER1 MLT-8530`；`series_r=R51 10R`；`flyback=D6 1N4148W`；`switch=Q3 2N7002W` |
| 其他事实 | LED1 / LED2 | `led1=RED,CHG_STAT`；`led1_resistor=R27 1K`；`led2=GREEN,LED_PWR_GREEN`；`led2_resistor=R9 4.7K`；`r8=NC` |

## 待确认事项

- `component.pmic-identity`：原理图仅将 M1 标为 StampTimerPower2，未在该符号旁直接标注产品文档中的 M5PM1 名称。（证据：图 5ca658961967 / 第 1 页 / TimerPower2 区：M1 与 StampTimerPower2 标注）
- `component.ioexp-identity`：原理图仅标注 U5 为 IO_EXP 与地址 0x4F，未在器件符号处标注完整型号。（证据：图 7462e5815f4a / 第 1 页 / PYB IOEXP 区：U5、IO_EXP 与 IIC Address:0X4F）
- `interface.rs485-transceiver`：四页主原理图直接引出 G23_RX/G24_TX 到 M5BUS，但未画出产品文档所述 SP485EEN-L/TR 收发器。（证据：图 7462e5815f4a / 第 1 页 / 03 MCU Core 区：U3 的 G23/G24 GPIO; 图 5ca658961967 / 第 1 页 / M5BUS 区：JP3 的 G23_RX/G24_TX）
- `interface.lcd-driver`：JP4 仅给出 LCD 的 SPI、复位、DC、电源与背光接口，未在主板原理图中标注 ILI9342C 控制器型号。（证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区：JP4 与 LCD 接口网络）
- `interface.touch-controller`：JP5 仅给出触控 I2C、复位、中断与电源接口，未在主板原理图中标注 CHSC6540 控制器型号。（证据：图 577c50e9cbeb / 第 1 页 / LCD & TP 区：JP5 C-TP 与 TP_SCL/TP_SDA/PM_TP_INT/PM_TP_RST）
- `nr-1`：请依据 BOM 确认 M1(StampTimerPower2) 是否对应产品文档中的 M5PM1。；原因：原理图在 M1 符号处标注 StampTimerPower2 与 0x6E，但未直接标注 M5PM1。
- `nr-2`：请确认 U5(IO_EXP, 0x4F) 是否对应产品文档中的 M5IOE1。；原因：原理图只显示 IO_EXP 通用符号名和 I2C 地址，完整型号由产品文档给出。
- `nr-3`：请确认 SP485EEN-L/TR 收发器所在原理图页或接口扩展板，并补齐其 UART/方向控制连接。；原因：四页主板原理图仅显示 G23_RX/G24_TX 的 M5BUS 引出，未出现 SP485EEN-L/TR。
- `nr-4`：请确认 JP4 所接 LCD 面板内置的控制器型号是否为 ILI9342C，并核对 FPC 引脚定义。；原因：主板原理图只给出 JP4 接口网络，未标注面板控制器型号。
- `nr-5`：请确认 JP5 所接触控面板的控制器型号是否为 CHSC6540。；原因：主板原理图只给出 JP5 的 I2C、复位、中断与电源接口，未标注控制器型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `65f28dc6f899b53d540a5fde2c3f75b7e54e5e7480e356a2e97482b92884a9c6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1275/K162_ToughC5_sche_page_01.png` |
| 2 | 1 | `5ca6589619677cb92305aedccaf2f401bc7bc3689c39c7eb58d8eecbdaa41c5e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1275/K162_ToughC5_sche_page_02.png` |
| 3 | 1 | `7462e5815f4a7b77d8908909ae0b23a5c955aa269bb5684aee46e2f3ebf2a5c9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1275/K162_ToughC5_sche_page_03.png` |
| 4 | 1 | `577c50e9cbeb765827ad3f58861619024b8e44fffbcc94d1c98810e9ec887e6b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1275/K162_ToughC5_sche_page_04.png` |

---

源文档：`zh_CN/core/ToughC5.md`

源文档 SHA-256：`8b9618d4d405f5591bad74c37a42e68533440f3f901a8935b759df6a6e16027d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
