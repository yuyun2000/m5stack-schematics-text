# Paper v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Paper v1.1 |
| SKU | K049-B |
| 产品 ID | `paper-v1-1-791f70ff5573` |
| 源文档 | `zh_CN/core/m5paper_v1.1.md` |

## 概述

Paper v1.1 以 U1 ESP32 为主控，配套 ESPSRAM64H、W25Q128、FM24C02B，并通过 SPI 驱动 IT8951E-64 电子墨水屏控制器和 ED047TC1 面板。板上包含 SHT30、PCF8563 RTC、MicroSD、CP2104 USB-UART、三组 HY2.0-4P 扩展口以及独立触摸 I2C 接口。电源由 USB/电池汇合形成 VSYS，经 SY7088、SY8003 和受控负载开关生成 5 V、3.3 V 与 EPD 电源，TPS65185 负责面板高压轨。

## 检索关键词

`Paper v1.1`、`K049-B`、`ESP32`、`IT8951E-64`、`ED047TC1`、`TPS65185`、`ESPSRAM64H`、`W25Q128`、`W25Q32`、`FM24C02B-DN-T-G`、`SHT30`、`SE95D`、`PCF8563`、`CP2104`、`SY7088`、`SY8003`、`SLM6600`、`SGM3167`、`USB Type-C`、`MicroSD`、`HY2.0-4P`、`I2C_SCL`、`I2C_SDA`、`IT_SPI_SCK`、`IT_SPI_MOSI`、`IT_SPI_MISO`、`EPD_VCOM`、`VEPD_5V`、`VCC_3V3`、`VBUS_5V`、`VBAT_S`、`GPIO36`、`GPIO34`、`RTC_ALM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 系统主控，连接外部存储、传感器、IT8951 SPI、MicroSD、按键和电源控制信号 | 图 1442b3537acb / 第 1 页 / U1 主控及 GPIO 网络区域 |
| U2 | FM24C02B-DN-T-G | I2C 非易失存储器，A0/A1/A2 接地 | 图 1442b3537acb / 第 1 页 / U2 FM24C02B-DN-T-G 与 I2C_SCL/I2C_SDA |
| U3 | ESPSRAM64H | ESP32 外部伪静态 RAM | 图 1442b3537acb / 第 1 页 / U3 ESPSRAM64H 存储器区域 |
| U4 | W25Q128 | ESP32 外部 SPI Flash | 图 1442b3537acb / 第 1 页 / U4 W25Q128 存储器区域 |
| U22 | SHT30 | 系统 I2C 温湿度传感器，ADDR 接地 | 图 1442b3537acb / 第 1 页 / U22 SHT30 与 I2C_SCL/I2C_SDA |
| ANT1 | PROANT_440 | ESP32 射频天线 | 图 1442b3537acb / 第 1 页 / ANT1 PROANT_440 与 RF 匹配网络 |
| U5 | IT8951E-64 | 电子墨水屏控制器，连接 ESP32 SPI、专用存储器、PMIC 和并行面板总线 | 图 f320feda5dae / 第 1 页 / U5A/U5C IT8951E-64 控制与存储接口; 图 90ad5fabab87 / 第 1 页 / U5B/U5D IT8951E-64 EPD 并行接口 |
| U6 | W25Q32 | IT8951 专用 SPI Flash | 图 f320feda5dae / 第 1 页 / U6 W25Q32 与 U5 存储接口 |
| U10 | SGM3167 | EPD VCOM 控制信号调理器件 | 图 f320feda5dae / 第 1 页 / U10 SGM3167 与 EPD_VCOM_CTRL |
| U11 | SE95D | IT8951 侧 I2C 温度传感器 | 图 f320feda5dae / 第 1 页 / U11 SE95D 与 IT_I2C_SCL/IT_I2C_SDA |
| U18 | SY8003 | 将 VEPD_5V 降压为 VEPD_1V8 | 图 b9201c64714c / 第 1 页 / U18 SY8003，VEPD_5V 输入与 VEPD_1V8 输出 |
| U19 | SY8003 | 将 VEPD_5V 降压为 VEPD_3V3 | 图 b9201c64714c / 第 1 页 / U19 SY8003，VEPD_5V 输入与 VEPD_3V3 输出 |
| U20 | SGM803-SXN3/TR | 2.93 V 复位监控器，生成 IT_RST# | 图 b9201c64714c / 第 1 页 / U20 2.93V/SGM803-SXN3/TR 与 IT_RST# |
| J1 | EPD_ED047TC1 | ED047TC1 电子墨水屏面板连接器 | 图 90ad5fabab87 / 第 1 页 / J1 EPD_ED047TC1 与 EPD1_D0-D7、栅源驱动网络 |
| U7 | TPS65185 | 电子纸电源管理器，产生和控制 VNEG、VPOS、VEE、VDDH 与 VCOM | 图 69bd3e2f206a / 第 1 页 / U7 TPS65185 及 EPD 高压电源网络 |
| U8 | SY7088 | 由 VSYS 升压生成 VBUS_5V | 图 8e0e8eeb66e9 / 第 1 页 / A1-A2，U8 SY7088，VSYS 输入与 VBUS_5V 输出 |
| U9 | SLM6600 | USB 输入锂电池充电管理器，连接 VUSB_VIN 与 VBAT_IN | 图 8e0e8eeb66e9 / 第 1 页 / A3，U9 SLM6600 充电路径 |
| U17 | SY8003 | 由 VBUS_5V 降压生成 VCC_3V3 | 图 8e0e8eeb66e9 / 第 1 页 / C1-C2，U17 SY8003，VBUS_5V 输入与 VCC_3V3 输出 |
| U23 | PCF8563 | 电池供电 I2C RTC，RTC_ALM 输出参与唤醒/电源控制 | 图 8e0e8eeb66e9 / 第 1 页 / C4-D4，U23 PCF8563、Y1 与 RTC_ALM |
| J3 | USB-TYPEC | 主 USB Type-C 电源和 USB 2.0 数据接口 | 图 c85e5e48676f / 第 1 页 / A2，J3 USB-TYPEC，VUSB_VIN 与 USB_D_P/USB_D_N |
| U14 | CP2104 | USB 转 UART 下载与调试桥接器 | 图 c85e5e48676f / 第 1 页 / C3，U14 CP2104，USB_D_P/N 与 CP_TXD/CP_RXD/CP_RTS/CP_DTR |
| U21 | 5033981892 | MicroSD 卡连接器，带 CARD_CD 检测 | 图 c85e5e48676f / 第 1 页 / A4，U21 卡座，SD_CS/SD_SCK/IT_SPI_MOSI/IT_SPI_MISO/CARD_CD |
| J2 | K1-1502SA-02 | 左、按压、右三路拨轮开关连接器 | 图 c85e5e48676f / 第 1 页 / A1，J2 KEY_LEFT/KEY_PUSH/KEY_RIGHT |
| J5/J6/J7 | PH2.0_4P_SMT | 三组 5 V GPIO 扩展连接器 | 图 c85e5e48676f / 第 1 页 / B1-D1，J5 GPIO32/25、J6 GPIO33/26、J7 GPIO19/18 与 VEXT_5V |
| J11 | TOUCH_I2C | 触摸面板 I2C、电源、中断和复位连接器 | 图 c85e5e48676f / 第 1 页 / B1-B2，J11 TOUCH_I2C，I2C_SDA/I2C_SCL/TOUCH_INT/ESP32_EN |
| U12/U13/U15/U16 | SRV05-4 | USB 数据线和外部 GPIO 扩展口 ESD 保护阵列 | 图 c85e5e48676f / 第 1 页 / A3 U12 及 B2-D2 U13/U15/U16 SRV05-4 |

## 系统结构

### 系统架构

ESP32 负责系统控制并通过 SPI 连接 IT8951E-64；IT8951E-64 再通过并行 EPD 总线和 TPS65185 电源控制链路驱动 ED047TC1 面板。

- 参数与网络：`main_controller=U1 ESP32`；`display_controller=U5 IT8951E-64`；`panel=J1 EPD_ED047TC1`；`display_pmic=U7 TPS65185`
- 证据：图 1442b3537acb / 第 1 页 / U1 与 IT_SPI_* 网络; 图 90ad5fabab87 / 第 1 页 / U5B/U5D 到 J1 EPD_ED047TC1; 图 69bd3e2f206a / 第 1 页 / U7 TPS65185 面板电源网络

## 电源

### 系统电源汇合

D9 与 D12 两只 DSK34 肖特基二极管分别将 VBAT 和 VUSB_VIN 汇合到 VSYS。

- 参数与网络：`battery_input=VBAT via D9 DSK34`；`usb_input=VUSB_VIN via D12 DSK34`；`output=VSYS`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / C2，D9/D12 DSK34 到 VSYS

### 系统 5 V

U8 SY7088 以 VSYS 为输入，经 L4 WPN3012H2R2MT 升压生成 VBUS_5V。

- 参数与网络：`reference=U8`；`part_number=SY7088`；`input=VSYS`；`output=VBUS_5V`；`inductor=L4 WPN3012H2R2MT`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / A1-A2，U8/L4/R30/R33，VSYS 到 VBUS_5V

### 系统 3.3 V

U17 SY8003 将 VBUS_5V 降压为 VCC_3V3。

- 参数与网络：`reference=U17`；`part_number=SY8003`；`input=VBUS_5V`；`output=VCC_3V3`；`inductor=L6 WPN3012H2R2MT`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / C1-C2，U17/L6/R36/R38，VBUS_5V 到 VCC_3V3

### 电池充电路径

U9 SLM6600 由 VUSB_VIN 供电，BAT 端连接 VBAT_IN；PROG 端通过 R31 1 kΩ 接地。

- 参数与网络：`reference=U9`；`part_number=SLM6600`；`input=VUSB_VIN`；`battery_net=VBAT_IN`；`program_resistor=R31 1K`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / A3，U9 SLM6600、R31、VBAT_IN/VUSB_VIN

### 电池电源保持

VBAT_UFUSED 经 FUSE1 6V/2A Poly 和 FET1 PMOS 到 VBAT；FET2 NMOS 受 PWR_EN 控制，KEY_PUSH_IO 与 RTC_ALM 通过二极管网络参与 PWR_EN。

- 参数与网络：`input=VBAT_UFUSED`；`fuse=FUSE1 6V/2A/Poly`；`high_side=FET1 CJ2301-PMOS`；`control_fet=FET2 CJ2302-NMOS`；`enable=PWR_EN`；`wake_sources=KEY_PUSH_IO; RTC_ALM`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / B3-B4，FUSE1/FET1/FET2/D7/D8/D10/D11 电源保持电路

### 受控 5 V 输出

EXT_PWR_EN 控制 FET5/FET3 高边路径向 VEXT_5V 供电，EPD_PWR_EN 控制 FET6/FET4 高边路径向 VEPD_5V 供电。

- 参数与网络：`external_enable=EXT_PWR_EN`；`external_output=VEXT_5V`；`external_fets=FET5 CJ3134KW/SC70; FET3 SE7401U/SC70`；`epd_enable=EPD_PWR_EN`；`epd_output=VEPD_5V`；`epd_fets=FET6 CJ3134KW/SC70; FET4 SE7401U/SC70`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / D1-D3，EXT_PWR_EN/FET5/FET3/FUSE2 与 EPD_PWR_EN/FET6/FET4

### EPD 低压电源

U18 与 U19 两颗 SY8003 分别由 VEPD_5V 生成 VEPD_1V8 和 VEPD_3V3；磁珠进一步分隔模拟与数字子电源域。

- 参数与网络：`u18_input=VEPD_5V`；`u18_output=VEPD_1V8`；`u19_input=VEPD_5V`；`u19_output=VEPD_3V3`；`separated_rails=VEPD_1V8A; VEPD_3V3A; VEPD_3V3A_U20; VEPD_3V3A_HSRT`
- 证据：图 b9201c64714c / 第 1 页 / U18/U19 SY8003 及 VEPD_1V8/VEPD_3V3 磁珠分区

### EPD 高压电源

U7 TPS65185 配合 L2/L3 和 BAS3010 二极管产生或控制 EPD_VNEG、EPD_VPOS、EPD_VEE、EPD_VDDH 与 EPD_VCOM。

- 参数与网络：`reference=U7`；`part_number=TPS65185`；`rails=EPD_VNEG; EPD_VPOS; EPD_VEE; EPD_VDDH; EPD_VCOM`；`inductors=L2; L3`；`control=TPS_WAKEUP; TPS_PWRUP; TPS_INT; TPS_PG; EPD_VCOM_CTRL`
- 证据：图 69bd3e2f206a / 第 1 页 / U7 TPS65185、L2/L3、BAS3010 与 EPD 高压网络

## 接口

### MicroSD 接口

U21 卡座使用 SD_CS、SD_SCK、IT_SPI_MOSI、IT_SPI_MISO，CARD_CD 由 10 kΩ 上拉到 VCC_3V3。

- 参数与网络：`reference=U21`；`part_number=5033981892`；`cs=SD_CS`；`clock=SD_SCK`；`mosi=IT_SPI_MOSI`；`miso=IT_SPI_MISO`；`detect=CARD_CD`；`voltage=VCC_3V3`
- 证据：图 c85e5e48676f / 第 1 页 / A4，U21 DAT2/CD-DAT3/CMD/VDD/CLK/DAT0/CD 引脚

### 触摸接口

J11 提供 VCC_3V3、GND、I2C_SDA、I2C_SCL、TOUCH_INT 和 ESP32_EN；其余两针未连接。

- 参数与网络：`pin1=VCC_3V3`；`pin2=GND`；`pin3=I2C_SDA`；`pin4=I2C_SCL`；`pin5=TOUCH_INT`；`pin6=ESP32_EN`；`pin7=NC`；`pin8=NC`
- 证据：图 c85e5e48676f / 第 1 页 / B1-B2，J11 TOUCH_I2C pins 1-8

### HY2.0-4P 扩展口

J5、J6、J7 均提供两路 GPIO、VEXT_5V 和 GND，信号组合依次为 GPIO32/GPIO25、GPIO33/GPIO26、GPIO19/GPIO18。

- 参数与网络：`J5=pin1 GPIO32; pin2 GPIO25; pin3 VEXT_5V; pin4 GND`；`J6=pin1 GPIO33; pin2 GPIO26; pin3 VEXT_5V; pin4 GND`；`J7=pin1 GPIO19; pin2 GPIO18; pin3 VEXT_5V; pin4 GND`
- 证据：图 c85e5e48676f / 第 1 页 / B1-D1，J5/J6/J7 PH2.0_4P_SMT 引脚

### 主 USB Type-C

J3 将 VUSB_VIN、USB_D_P 和 USB_D_N 引入系统，CC1 与 CC2 各通过 5.1 kΩ 电阻接地。

- 参数与网络：`reference=J3`；`vbus=VUSB_VIN`；`dp=USB_D_P`；`dn=USB_D_N`；`cc1=R40 5.1k to GND`；`cc2=R44 5.1k to GND`
- 证据：图 c85e5e48676f / 第 1 页 / A2，J3 USB-TYPEC、R40/R44

### 电子墨水屏面板接口

J1 EPD_ED047TC1 接收 EPD1_D0-D7 并行数据、X/Y 栅源控制时钟和锁存信号，以及 VCOM、VNEG、VPOS、VDDH、VEE、BORDER 等电源/驱动网络。

- 参数与网络：`reference=J1`；`panel=ED047TC1`；`data_bus=EPD1_D0-D7`；`power_nets=EPD_VCOM; EPD_VNEG; EPD_VPOS; EPD_VDDH; EPD_VEE`；`other=BORDER; X/Y latch/strobe/clock nets`
- 证据：图 90ad5fabab87 / 第 1 页 / J1 EPD_ED047TC1 全部面板信号及 U5B/U5D

## 总线

### ESP32 到 IT8951 SPI

ESP32 通过 IT_SPI_SCK、IT_SPI_MOSI、IT_SPI_MISO 和 IT_SPI_CS# 与 IT8951E-64 通信。

- 参数与网络：`controller=U1 ESP32`；`device=U5 IT8951E-64`；`sck=IT_SPI_SCK/GPIO14`；`mosi=IT_SPI_MOSI/GPIO12`；`miso=IT_SPI_MISO/GPIO13`；`cs=IT_SPI_CS#/GPIO15`
- 证据：图 1442b3537acb / 第 1 页 / U1 GPIO12-GPIO15 与 IT_SPI_*; 图 f320feda5dae / 第 1 页 / U5A/U5C IT_SPI_SCK/MOSI/MISO/CS#

### 系统 I2C

GPIO22/I2C_SCL 与 GPIO21/I2C_SDA 连接 FM24C02B、SHT30、PCF8563 和 J11 触摸接口。

- 参数与网络：`controller=U1 ESP32`；`scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`devices=U2 FM24C02B; U22 SHT30; U23 PCF8563; J11 TOUCH_I2C`
- 证据：图 1442b3537acb / 第 1 页 / U1 GPIO22/GPIO21、U2、U22 的 I2C_SCL/I2C_SDA; 图 8e0e8eeb66e9 / 第 1 页 / U23 PCF8563 SCL/SDA; 图 c85e5e48676f / 第 1 页 / J11 TOUCH_I2C 的 I2C_SDA/I2C_SCL

### IT8951 I2C

IT8951E-64 使用 IT_I2C_SCL/IT_I2C_SDA 连接 U11 SE95D 和 U7 TPS65185。

- 参数与网络：`controller=U5 IT8951E-64`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA`；`devices=U11 SE95D; U7 TPS65185`
- 证据：图 f320feda5dae / 第 1 页 / U5/U11 IT_I2C_SCL/IT_I2C_SDA; 图 69bd3e2f206a / 第 1 页 / U7 TPS65185 IT_I2C_SCL/IT_I2C_SDA

## GPIO 与控制信号

### MicroSD GPIO 映射

MicroSD 的 SD_CS 对应 GPIO4，CARD_CD 对应 GPIO34；SPI 时钟、MOSI、MISO 分别对应 GPIO14、GPIO12、GPIO13。

- 参数与网络：`sd_cs=GPIO4`；`card_cd=GPIO34`；`sd_sck=GPIO14`；`mosi=GPIO12`；`miso=GPIO13`
- 证据：图 1442b3537acb / 第 1 页 / U1 GPIO4/GPIO34/GPIO12-GPIO14 网络映射; 图 c85e5e48676f / 第 1 页 / U21 SD_CS/SD_SCK/IT_SPI_MOSI/IT_SPI_MISO/CARD_CD

### 拨轮按键 GPIO

KEY_RIGHT、KEY_PUSH_IO、KEY_LEFT 分别连接 GPIO37、GPIO38、GPIO39。

- 参数与网络：`right=GPIO37/KEY_RIGHT`；`push=GPIO38/KEY_PUSH_IO`；`left=GPIO39/KEY_LEFT`
- 证据：图 1442b3537acb / 第 1 页 / U1 GPIO37-GPIO39 按键网络; 图 c85e5e48676f / 第 1 页 / J2 KEY_LEFT/KEY_PUSH/KEY_RIGHT 与 R41-R43 上拉

### 触摸中断

J11 的 TOUCH_INT 通过 R87 10 kΩ 串联到 ESP32 GPIO36。

- 参数与网络：`connector=J11 pin 5`；`net=TOUCH_INT`；`gpio=GPIO36`；`series_resistor=R87 10k`
- 证据：图 1442b3537acb / 第 1 页 / U1 GPIO36 TOUCH_INT; 图 c85e5e48676f / 第 1 页 / B2，J11 pin 5 TOUCH_INT、R87 10K

## 时钟

### IT8951 主时钟

X2 为 IT8951E-64 提供 12 MHz、20 ppm 晶体时钟。

- 参数与网络：`reference=X2`；`frequency=12MHz`；`tolerance=20ppm`；`device=U5 IT8951E-64`
- 证据：图 f320feda5dae / 第 1 页 / X2 12MHz/20ppm 与 U5 时钟引脚

### RTC 时钟

Y1 为 U23 PCF8563 提供 32.768 kHz 时钟，负载电容 C124/C125 均标注 6 pF。

- 参数与网络：`reference=Y1`；`frequency=32.768K`；`load_capacitors=C124 6pF; C125 6pF`；`rtc=U23 PCF8563`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / C4，Y1 32.768K/6pF、C124/C125、U23 OSCI/OSCO

## 复位

### IT8951 复位

U20 2.93 V SGM803-SXN3/TR 监控 EPD 3.3 V 域并输出 IT_RST#。

- 参数与网络：`reference=U20`；`part_number=SGM803-SXN3/TR`；`threshold_marking=2.93V`；`output=IT_RST#`；`supply=VEPD_3V3A_U20`
- 证据：图 b9201c64714c / 第 1 页 / U20 2.93V/SGM803-SXN3/TR、IT_RST#

### ESP32 复位与自动下载

OS1 可将 ESP32_EN 拉低复位；CP_RTS/CP_DTR 通过 VT1/VT2 和 D13/R54 控制 ESP32_EN 与 GPIO0 以支持自动下载。

- 参数与网络：`manual_switch=OS1 SMT_SW_PTS_820`；`enable=ESP32_EN`；`boot=GPIO0`；`uart_controls=CP_RTS; CP_DTR`
- 证据：图 c85e5e48676f / 第 1 页 / B2 OS1 ESP32_EN；C4 VT1/VT2/D13/R54 自动下载电路

## 保护电路

### 扩展口 ESD 保护

J5、J6、J7 的六路 GPIO 分别经 47 Ω 串联电阻和 U13/U15/U16 SRV05-4 阵列保护。

- 参数与网络：`arrays=U13/U15/U16 SRV05-4`；`series_resistors=R45/R46/R49/R51/R53/R55 47R`；`clamp_rail=VEXT_5V`
- 证据：图 c85e5e48676f / 第 1 页 / B2-D2，R45/R46/U13、R49/R51/U15、R53/R55/U16

### USB ESD 保护

USB_D_P 和 USB_D_N 经 U12 SRV05-4 保护，阵列钳位到 VUSB_VIN 和 GND。

- 参数与网络：`reference=U12`；`part_number=SRV05-4`；`signals=USB_D_P; USB_D_N`；`rails=VUSB_VIN; GND`
- 证据：图 c85e5e48676f / 第 1 页 / A3，U12 SRV05-4

### 电池与外部 5 V 保护

电池输入使用 FUSE1 6V/2A Poly，自外部接口输出的 VEXT_5V 使用 FUSE2 6V/2A Poly。

- 参数与网络：`battery_fuse=FUSE1 6V/2A/Poly`；`external_5v_fuse=FUSE2 6V/2A/Poly`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / B3 FUSE1；D1-D2 FUSE2

## 关键网络

### IT8951 到 EPD PMIC 控制

IT8951E-64 使用 TPS_WAKEUP、TPS_PWRUP、TPS_INT、TPS_PG 和 EPD_VCOM_CTRL 管理 TPS65185 电源时序与状态。

- 参数与网络：`controller=U5 IT8951E-64`；`pmic=U7 TPS65185`；`signals=TPS_WAKEUP; TPS_PWRUP; TPS_INT; TPS_PG; EPD_VCOM_CTRL`
- 证据：图 f320feda5dae / 第 1 页 / U5 控制网络 TPS_WAKEUP/TPS_PWRUP/TPS_INT/TPS_PG/EPD_VCOM_CTRL; 图 69bd3e2f206a / 第 1 页 / U7 TPS65185 对应控制引脚

## 存储

### ESP32 启动 Flash

U4 W25Q128 是 ESP32 外部 Flash。

- 参数与网络：`reference=U4`；`part_number=W25Q128`
- 证据：图 1442b3537acb / 第 1 页 / U4 W25Q128 与 ESP32 存储总线

### IT8951 Flash

U6 W25Q32 连接到 IT8951E-64 的专用串行存储接口。

- 参数与网络：`reference=U6`；`part_number=W25Q32`；`controller=U5 IT8951E-64`
- 证据：图 f320feda5dae / 第 1 页 / U6 W25Q32 与 U5A/U5C

### I2C 非易失存储

U2 FM24C02B-DN-T-G 接在系统 I2C 总线上，地址选择脚 A0、A1、A2 均接地。

- 参数与网络：`reference=U2`；`part_number=FM24C02B-DN-T-G`；`scl=I2C_SCL`；`sda=I2C_SDA`；`a0=GND`；`a1=GND`；`a2=GND`
- 证据：图 1442b3537acb / 第 1 页 / U2 引脚 SCL/SDA/A0/A1/A2

## 内存与 Flash

### ESP32 外部 PSRAM

U3 标注为 ESPSRAM64H，并连接 ESP32 的外部存储接口。

- 参数与网络：`reference=U3`；`part_number=ESPSRAM64H`
- 证据：图 1442b3537acb / 第 1 页 / U3 ESPSRAM64H

## 传感器

### 环境温湿度传感器

U22 SHT30 接入系统 I2C，总线地址选择脚 ADDR 接地，ALERT 与 NRST 未连接。

- 参数与网络：`reference=U22`；`part_number=SHT30`；`scl=I2C_SCL`；`sda=I2C_SDA`；`addr_strap=GND`；`alert=NC`；`nrst=NC`
- 证据：图 1442b3537acb / 第 1 页 / U22 SHT30 引脚 ADDR/ALERT/NRST/SCL/SDA

### EPD 温度传感器

U11 SE95D 位于 IT8951 侧 I2C 总线上，为 EPD 控制域提供温度测量接口。

- 参数与网络：`reference=U11`；`part_number=SE95D`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA`
- 证据：图 f320feda5dae / 第 1 页 / U11 SE95D 与 IT_I2C_SCL/IT_I2C_SDA

## 射频

### ESP32 天线

ESP32 射频端连接 ANT1 PROANT_440，串并联匹配器件位置包含 TBD/NC 标注。

- 参数与网络：`reference=ANT1`；`part_number=PROANT_440`；`matching=TBD/NC positions`
- 证据：图 1442b3537acb / 第 1 页 / ANT1 PROANT_440 与天线匹配网络

## 调试与烧录

### USB-UART 下载接口

U14 CP2104 将 USB_D_P/N 转换为 CP_TXD/CP_RXD，并用 CP_RTS/CP_DTR 驱动 ESP32 自动下载/复位电路。

- 参数与网络：`reference=U14`；`part_number=CP2104`；`uart_tx=CP_TXD -> R56 47R -> ESP32_U0RXD`；`uart_rx=CP_RXD -> R57 47R -> ESP32_U0TXD`；`control=CP_RTS; CP_DTR`
- 证据：图 c85e5e48676f / 第 1 页 / C3-C4，U14 CP2104、R56/R57、VT1/VT2 自动下载电路

### IT8951 USB 调试口

J8 是标为 NC 的可选 USB Type-C 接口，连接 IT_DBG_P 和 IT_DBG_N。

- 参数与网络：`reference=J8`；`population=NC`；`dp=IT_DBG_P`；`dn=IT_DBG_N`
- 证据：图 f320feda5dae / 第 1 页 / J8 USB Type-C 可选调试接口与 IT_DBG_P/N

## 模拟电路

### 电池电压采样

VBAT 经 R83 3 kΩ 与 R86 11 kΩ 分压生成 VBAT_S，VBAT_S 连接 ESP32 GPIO35。

- 参数与网络：`source=VBAT`；`sense_net=VBAT_S`；`upper_resistor=R83 3K`；`lower_resistor=R86 11K`；`gpio=GPIO35`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / D3，R83/R86，VBAT_S; 图 1442b3537acb / 第 1 页 / U1 GPIO35 VBAT_S

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 系统架构 | `main_controller=U1 ESP32`；`display_controller=U5 IT8951E-64`；`panel=J1 EPD_ED047TC1`；`display_pmic=U7 TPS65185` |
| 内存与 Flash | ESP32 外部 PSRAM | `reference=U3`；`part_number=ESPSRAM64H` |
| 存储 | ESP32 启动 Flash | `reference=U4`；`part_number=W25Q128` |
| 存储 | IT8951 Flash | `reference=U6`；`part_number=W25Q32`；`controller=U5 IT8951E-64` |
| 存储 | I2C 非易失存储 | `reference=U2`；`part_number=FM24C02B-DN-T-G`；`scl=I2C_SCL`；`sda=I2C_SDA`；`a0=GND`；`a1=GND`；`a2=GND` |
| 总线 | ESP32 到 IT8951 SPI | `controller=U1 ESP32`；`device=U5 IT8951E-64`；`sck=IT_SPI_SCK/GPIO14`；`mosi=IT_SPI_MOSI/GPIO12`；`miso=IT_SPI_MISO/GPIO13`；`cs=IT_SPI_CS#/GPIO15` |
| 总线 | 系统 I2C | `controller=U1 ESP32`；`scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`devices=U2 FM24C02B; U22 SHT30; U23 PCF8563; J11 TOUCH_I2C` |
| 总线 | IT8951 I2C | `controller=U5 IT8951E-64`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA`；`devices=U11 SE95D; U7 TPS65185` |
| 接口 | MicroSD 接口 | `reference=U21`；`part_number=5033981892`；`cs=SD_CS`；`clock=SD_SCK`；`mosi=IT_SPI_MOSI`；`miso=IT_SPI_MISO`；`detect=CARD_CD`；`voltage=VCC_3V3` |
| GPIO 与控制信号 | MicroSD GPIO 映射 | `sd_cs=GPIO4`；`card_cd=GPIO34`；`sd_sck=GPIO14`；`mosi=GPIO12`；`miso=GPIO13` |
| GPIO 与控制信号 | 拨轮按键 GPIO | `right=GPIO37/KEY_RIGHT`；`push=GPIO38/KEY_PUSH_IO`；`left=GPIO39/KEY_LEFT` |
| GPIO 与控制信号 | 触摸中断 | `connector=J11 pin 5`；`net=TOUCH_INT`；`gpio=GPIO36`；`series_resistor=R87 10k` |
| 接口 | 触摸接口 | `pin1=VCC_3V3`；`pin2=GND`；`pin3=I2C_SDA`；`pin4=I2C_SCL`；`pin5=TOUCH_INT`；`pin6=ESP32_EN`；`pin7=NC`；`pin8=NC` |
| 接口 | HY2.0-4P 扩展口 | `J5=pin1 GPIO32; pin2 GPIO25; pin3 VEXT_5V; pin4 GND`；`J6=pin1 GPIO33; pin2 GPIO26; pin3 VEXT_5V; pin4 GND`；`J7=pin1 GPIO19; pin2 GPIO18; pin3 VEXT_5V; pin4 GND` |
| 保护电路 | 扩展口 ESD 保护 | `arrays=U13/U15/U16 SRV05-4`；`series_resistors=R45/R46/R49/R51/R53/R55 47R`；`clamp_rail=VEXT_5V` |
| 接口 | 主 USB Type-C | `reference=J3`；`vbus=VUSB_VIN`；`dp=USB_D_P`；`dn=USB_D_N`；`cc1=R40 5.1k to GND`；`cc2=R44 5.1k to GND` |
| 保护电路 | USB ESD 保护 | `reference=U12`；`part_number=SRV05-4`；`signals=USB_D_P; USB_D_N`；`rails=VUSB_VIN; GND` |
| 调试与烧录 | USB-UART 下载接口 | `reference=U14`；`part_number=CP2104`；`uart_tx=CP_TXD -> R56 47R -> ESP32_U0RXD`；`uart_rx=CP_RXD -> R57 47R -> ESP32_U0TXD`；`control=CP_RTS; CP_DTR` |
| 调试与烧录 | IT8951 USB 调试口 | `reference=J8`；`population=NC`；`dp=IT_DBG_P`；`dn=IT_DBG_N` |
| 传感器 | 环境温湿度传感器 | `reference=U22`；`part_number=SHT30`；`scl=I2C_SCL`；`sda=I2C_SDA`；`addr_strap=GND`；`alert=NC`；`nrst=NC` |
| 传感器 | EPD 温度传感器 | `reference=U11`；`part_number=SE95D`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA` |
| 射频 | ESP32 天线 | `reference=ANT1`；`part_number=PROANT_440`；`matching=TBD/NC positions` |
| 时钟 | IT8951 主时钟 | `reference=X2`；`frequency=12MHz`；`tolerance=20ppm`；`device=U5 IT8951E-64` |
| 时钟 | RTC 时钟 | `reference=Y1`；`frequency=32.768K`；`load_capacitors=C124 6pF; C125 6pF`；`rtc=U23 PCF8563` |
| 复位 | IT8951 复位 | `reference=U20`；`part_number=SGM803-SXN3/TR`；`threshold_marking=2.93V`；`output=IT_RST#`；`supply=VEPD_3V3A_U20` |
| 复位 | ESP32 复位与自动下载 | `manual_switch=OS1 SMT_SW_PTS_820`；`enable=ESP32_EN`；`boot=GPIO0`；`uart_controls=CP_RTS; CP_DTR` |
| 电源 | 系统电源汇合 | `battery_input=VBAT via D9 DSK34`；`usb_input=VUSB_VIN via D12 DSK34`；`output=VSYS` |
| 电源 | 系统 5 V | `reference=U8`；`part_number=SY7088`；`input=VSYS`；`output=VBUS_5V`；`inductor=L4 WPN3012H2R2MT` |
| 电源 | 系统 3.3 V | `reference=U17`；`part_number=SY8003`；`input=VBUS_5V`；`output=VCC_3V3`；`inductor=L6 WPN3012H2R2MT` |
| 电源 | 电池充电路径 | `reference=U9`；`part_number=SLM6600`；`input=VUSB_VIN`；`battery_net=VBAT_IN`；`program_resistor=R31 1K` |
| 电源 | 电池电源保持 | `input=VBAT_UFUSED`；`fuse=FUSE1 6V/2A/Poly`；`high_side=FET1 CJ2301-PMOS`；`control_fet=FET2 CJ2302-NMOS`；`enable=PWR_EN`；`wake_sources=KEY_PUSH_IO; RTC_ALM` |
| 保护电路 | 电池与外部 5 V 保护 | `battery_fuse=FUSE1 6V/2A/Poly`；`external_5v_fuse=FUSE2 6V/2A/Poly` |
| 电源 | 受控 5 V 输出 | `external_enable=EXT_PWR_EN`；`external_output=VEXT_5V`；`external_fets=FET5 CJ3134KW/SC70; FET3 SE7401U/SC70`；`epd_enable=EPD_PWR_EN`；`epd_output=VEPD_5V`；`epd_fets=FET6 CJ3134KW/SC70; FET4 SE7401U/SC70` |
| 模拟电路 | 电池电压采样 | `source=VBAT`；`sense_net=VBAT_S`；`upper_resistor=R83 3K`；`lower_resistor=R86 11K`；`gpio=GPIO35` |
| 电源 | EPD 低压电源 | `u18_input=VEPD_5V`；`u18_output=VEPD_1V8`；`u19_input=VEPD_5V`；`u19_output=VEPD_3V3`；`separated_rails=VEPD_1V8A; VEPD_3V3A; VEPD_3V3A_U20; VEPD_3V3A_HSRT` |
| 电源 | EPD 高压电源 | `reference=U7`；`part_number=TPS65185`；`rails=EPD_VNEG; EPD_VPOS; EPD_VEE; EPD_VDDH; EPD_VCOM`；`inductors=L2; L3`；`control=TPS_WAKEUP; TPS_PWRUP; TPS_INT; TPS_PG; EPD_VCOM_CTRL` |
| 接口 | 电子墨水屏面板接口 | `reference=J1`；`panel=ED047TC1`；`data_bus=EPD1_D0-D7`；`power_nets=EPD_VCOM; EPD_VNEG; EPD_VPOS; EPD_VDDH; EPD_VEE`；`other=BORDER; X/Y latch/strobe/clock nets` |
| 关键网络 | IT8951 到 EPD PMIC 控制 | `controller=U5 IT8951E-64`；`pmic=U7 TPS65185`；`signals=TPS_WAKEUP; TPS_PWRUP; TPS_INT; TPS_PG; EPD_VCOM_CTRL` |
| 存储 | ESP32 Flash 容量 | `reference=U4`；`schematic_marking=W25Q128`；`claimed_capacity=16MB` |
| 内存与 Flash | PSRAM 容量 | `reference=U3`；`schematic_marking=ESPSRAM64H`；`claimed_capacity=8MB` |
| 接口 | 面板显示规格 | `confirmed_panel=ED047TC1`；`unverified_claims=4.7 inch; 540x960; 16 grayscale; flexible panel; refresh modes` |
| 核心器件 | 触摸控制器 | `connector=J11 TOUCH_I2C`；`unverified_model=GT911`；`unverified_capabilities=two-point touch; gestures; I2C address` |
| 核心器件 | RTC 型号一致性 | `schematic_reference=U23`；`schematic_model=PCF8563`；`document_model=BM8563` |
| 电源 | 内置电池容量 | `battery_connector=J4`；`battery_net=VBAT_UFUSED`；`unverified_claims=1150mAh@3.7V; RTC-only 10uA` |
| 调试与烧录 | USB-UART 物料变体 | `schematic_model=CP2104`；`unverified_alternate=CH9102` |
| 总线地址 | I2C 设备地址 | `system_devices=U2 FM24C02B; U22 SHT30; U23 PCF8563; J11 touch`；`it_devices=U11 SE95D; U7 TPS65185`；`address_text=not printed` |

## 待确认事项

- `component.flash-capacity`：原理图仅明确 U4 型号为 W25Q128；将其写成产品容量 16 MB 需要用器件资料或 BOM 复核。（证据：图 1442b3537acb / 第 1 页 / U4 仅标注 W25Q128）
- `component.psram-capacity`：原理图仅明确 U3 型号为 ESPSRAM64H；将其写成产品容量 8 MB 需要用器件资料或 BOM 复核。（证据：图 1442b3537acb / 第 1 页 / U3 仅标注 ESPSRAM64H）
- `interface.display-specification`：原理图确认面板型号 ED047TC1，但未直接标注 4.7 英寸、540×960、16 级灰度、柔性面板或刷新模式性能。（证据：图 90ad5fabab87 / 第 1 页 / J1 仅标注 EPD_ED047TC1 和电气网络）
- `component.touch-controller`：原理图只显示 J11 TOUCH_I2C 接口，未显示触摸控制器本体，因此 GT911 型号、两点触控、手势能力和 I2C 地址无法由这些页面确认。（证据：图 c85e5e48676f / 第 1 页 / J11 仅给出触摸电源、I2C、INT、复位信号）
- `component.rtc-model-conflict`：当前原理图 U23 明确标注 PCF8563，与产品正文所称 BM8563 不一致，发布硬件型号前需确认本版本 BOM。（证据：图 8e0e8eeb66e9 / 第 1 页 / C4-D4，U23 丝印 PCF8563）
- `power.battery-capacity`：原理图给出电池连接与充电/保护网络，但未标注 1150 mAh、3.7 V 容量规格或 RTC-only 10 µA 功耗。（证据：图 c85e5e48676f / 第 1 页 / B1，J4 仅标注 VBAT_UFUSED 与 GND; 图 8e0e8eeb66e9 / 第 1 页 / 充电、电源保持与 RTC 电源路径未标容量或静态电流）
- `debug.usb-uart-variant`：当前原理图 U14 只标注 CP2104，未显示产品正文提到的 CH9102 替代版本。（证据：图 c85e5e48676f / 第 1 页 / C3，U14 明确标注 CP2104）
- `address.i2c-addresses`：原理图显示 FM24C02B 和 SHT30 的地址脚接法，但未以十六进制直接标注 FM24C02B、SHT30、PCF8563、SE95D 或触摸设备的 I2C 地址。（证据：图 1442b3537acb / 第 1 页 / U2/U22 地址脚与 I2C 网络，未见十六进制地址; 图 f320feda5dae / 第 1 页 / U11/IT I2C 网络未见十六进制地址; 图 8e0e8eeb66e9 / 第 1 页 / U23 PCF8563 未标 I2C 地址）
- `review.flash-capacity`：U4 W25Q128 在本产品 BOM 中是否对应 16 MB 可用 Flash？；原因：原理图只给出器件型号，没有直接写容量单位。
- `review.psram-capacity`：U3 ESPSRAM64H 在本产品 BOM 中是否对应 8 MB PSRAM？；原因：原理图只给出器件型号，没有直接写容量单位。
- `review.display-specification`：请用 ED047TC1 datasheet 或本版本 BOM 确认面板尺寸、分辨率、灰度级、柔性结构和刷新模式。；原因：这些性能参数未印在原理图页面上。
- `review.touch-controller`：请用触摸 FPC/BOM 确认 GT911 型号、能力和 I2C 地址。；原因：七张原理图仅出现触摸连接器，没有控制器本体。
- `review.rtc-model-conflict`：Paper v1.1 K049-B 实际装配的 RTC 是 PCF8563 还是 BM8563？；原因：原理图 U23 标注 PCF8563，产品正文标注 BM8563。
- `review.battery-capacity`：请用电池标签或 BOM 确认 1150 mAh@3.7 V 及 RTC-only 10 µA 指标。；原因：原理图未给出电池容量和整机休眠电流。
- `review.usb-uart-variant`：是否存在装配 CH9102 的 K049-B 物料变体？；原因：当前原理图只显示 CP2104，无法证明替代物料。
- `review.i2c-addresses`：请用各器件 datasheet 与地址脚接法复核所有 I2C 7-bit 地址。；原因：原理图未直接印出十六进制地址，不能仅凭经验补全。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1442b3537acb90c9b2471c567deab75ef670c6114c6f056076248ddc21c0dfd9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_01.png` |
| 2 | 1 | `f320feda5dae5addb3fed1291d4e9c369a0ca2fb7cd4f717971e91eba6fd5b37` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_02.png` |
| 3 | 1 | `b9201c64714c766a6a7f80fb63166c2acb89a3861e6d36ef98b29b1f1752e012` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_03.png` |
| 4 | 1 | `90ad5fabab872ab75a365519ef9c18e21cef7df7f36f146067b7166486302622` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_04.png` |
| 5 | 1 | `69bd3e2f206a7f3f90237cafd9f14dd1c020aec29c01cb68eedd5367ecfc907f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_05.png` |
| 6 | 1 | `8e0e8eeb66e99385c815ec314022bb28a1f32ef6f0be47082964422998209f92` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_06.png` |
| 7 | 1 | `c85e5e48676fdb02936967f5b27a0bddea7d14845d955bb4c29cff1c629309ca` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_07.png` |

---

源文档：`zh_CN/core/m5paper_v1.1.md`

源文档 SHA-256：`53eb62ff889f6c99d06e9926c6aca731883bbf9b312db5750e10070a8f7a8d40`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
