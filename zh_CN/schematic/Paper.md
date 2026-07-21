# Paper 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Paper |
| SKU | K049 |
| 产品 ID | `paper-a89f57fad62a` |
| 源文档 | `zh_CN/core/m5paper.md` |

## 概述

Paper 以 U1 ESP32 为系统主控，外接 W25Q128 Flash、ESPPSRAM64H PSRAM、FM24C02B EEPROM、SHT30、PCF8563、microSD、触摸接口和 CP2104。ESP32 通过 SPI 控制 U5 IT8951E-64，后者配套 W25Q32、SE95D、TPS65185 和多路 SY8003 电源，最终以 8 位并行源极数据与时序信号驱动 J1 EPD_ED047TC1 面板。系统电源由电池/USB 合路、SLM6600 充电、SY7088 5V 升压、SY8003 3.3V 降压及受控 VEXT_5V/VEPD_5V 负载开关构成，并提供 USB Type-C、三路 PH2.0-4P、microSD 与拨轮按键接口。

## 检索关键词

`Paper`、`K049`、`ESP32`、`ESP32-D0WDQ6-V3`、`W25Q128`、`ESPPSRAM64H`、`FM24C02B-DN-T-G`、`SHT30`、`IT8951E-64`、`W25Q32`、`SE95D`、`TPS65185`、`EPD_ED047TC1`、`SY8003`、`SY7088`、`SLM6600`、`PCF8563`、`BM8563`、`CP2104`、`GT911`、`microSD`、`VCC_3V3`、`VDD_SDIO`、`VEPD_5V`、`VEPD_3V3`、`VEPD_1V8`、`EPD_VCOM`、`EPD_VPOS`、`EPD_VNEG`、`EPD_VDDH`、`EPD_VEE`、`IT_SPI`、`I2C_SDA`、`I2C_SCL`、`GPIO21`、`GPIO22`、`VEXT_5V`、`VBAT_IN`、`VBUS_5V`、`RTC_ALM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 系统主控，连接存储、I2C 设备、IT8951、microSD、按键和扩展接口 | 图 1442b3537acb / 第 1 页 / 第1资源 A1-B1，U1 ESP32，GPIO0-GPIO39、SDIO、UART、I2C |
| U2 | FM24C02B-DN-T-G | I2C 非易失 EEPROM，A0/A1/A2 接地 | 图 1442b3537acb / 第 1 页 / 第1资源 A4，U2 FM24C02B-DN-T-G |
| U3 | ESPPSRAM64H | 外部四线 PSRAM，复用 SD_DATA0-3 与独立 PSRAM_CS/PSRAM_CLK | 图 1442b3537acb / 第 1 页 / 第1资源 C2，U3 ESPPSRAM64H |
| U4 | W25Q128 | ESP32 外部 SPI Flash，连接 SD_CMD/SD_CLK/SD_DATA0-3 | 图 1442b3537acb / 第 1 页 / 第1资源 D2，U4 W25Q128 |
| U22 | SHT30 | I2C 温湿度传感器，ADDR 接地 | 图 1442b3537acb / 第 1 页 / 第1资源 B4，U22 SHT30 |
| ANT1 | PROANT_440 | ESP32 2.4GHz 射频天线，预留 L1/C1/C3 匹配网络 | 图 1442b3537acb / 第 1 页 / 第1资源 A2-A3，ESP_LNA 至 ANT1 PROANT_440 |
| U5A/U5B/U5C/U5D | IT8951E-64 | 电子墨水屏控制器，接收 ESP32 SPI 并输出面板并行数据、时序和电源控制 | 图 f320feda5dae / 第 1 页 / 第2资源 B1-C3，U5A/U5C IT8951E-64; 图 90ad5fabab87 / 第 1 页 / 第4资源 A1-B2，U5B/U5D IT8951E-64 |
| U6 | W25Q32 | IT8951 专用 SPI Flash | 图 f320feda5dae / 第 1 页 / 第2资源 A1，U6 W25Q32，IT_FLASH_CS#/SCK/SO/SI |
| U11 | SE95D | IT8951 子系统 I2C 温度传感器，A0/A1/A2 接地 | 图 f320feda5dae / 第 1 页 / 第2资源 D2-D3，U11 SE95D |
| U10 | SGM3167 | 在 SDCLK 与 SDCLK_EPD 之间进行受 EPD_VCOM_CTRL 控制的模拟开关 | 图 f320feda5dae / 第 1 页 / 第2资源 D4，U10 SGM3167 |
| U18/U19 | SY8003 | 从 VEPD_5V 分别生成 VEPD_1V8 与 VEPD_3V3 | 图 b9201c64714c / 第 1 页 / 第3资源 A1-B2，U18/U19 SY8003 |
| U20 | SGM803-SXN3/TR | VEPD_3V3 复位监控器，输出 IT_RST# | 图 b9201c64714c / 第 1 页 / 第3资源 C1，U20 2.93V/SGM803-SXN3/TR |
| J1 | EPD_ED047TC1 | 44 针电子墨水屏连接器，承载 8 位源极数据、门极时序和多路高压 | 图 90ad5fabab87 / 第 1 页 / 第4资源 A4-C4，J1 EPD_ED047TC1 pins 1-44 |
| U7 | TPS65185 | 电子墨水屏 PMIC，通过 I2C 控制 VPOS/VNEG/VEE/VDDH/VCOM 等高压轨 | 图 69bd3e2f206a / 第 1 页 / 第5资源 A1-B1，U7 TPS65185 |
| U8 | SY7088 | 从 VSYS 生成 VBUS_5V 的升压转换器 | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 A1-A2，U8 SY7088 |
| U9 | SLM6600 | VUSB_VIN 到 VBAT_IN 的开关型电池充电控制器 | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 A3，U9 SLM6600、L5、R31/R32 |
| U17 | SY8003 | 从 VBUS_5V 生成系统 VCC_3V3 | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C1-C2，U17 SY8003 |
| U23 | PCF8563 | 电池供电 RTC，通过 I2C 连接主控并输出 RTC_ALM | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C4-D4，U23 PCF8563 |
| U14 | CP2104 | USB-UART 下载调试桥及自动下载控制源 | 图 c85e5e48676f / 第 1 页 / 第7资源 B3-D3，U14 CP2104 |
| J3 | USB-TYPEC | 系统 USB Type-C 供电和 USB 2.0 数据接口 | 图 c85e5e48676f / 第 1 页 / 第7资源 A2-A3，J3 USB-TYPEC |
| U21 | 5033981892 | microSD 卡座，连接 SD_CS、IT_SPI_MOSI/MISO/SCK 和 CARD_CD | 图 c85e5e48676f / 第 1 页 / 第7资源 A4，U21 5033981892 |
| J5/J6/J7 | PH2.0_4P_SMT | 三路 4 针扩展口，分别引出 GPIO32/25、GPIO33/26、GPIO19/18 与 VEXT_5V | 图 c85e5e48676f / 第 1 页 / 第7资源 B1-D2，J5/J6/J7 PH2.0_4P_SMT |
| J2 | K1-1502SA-02 | 三向拨轮/按键，输出 KEY_LEFT/KEY_PUSH/KEY_RIGHT | 图 c85e5e48676f / 第 1 页 / 第7资源 A1，J2 K1-1502SA-02 |
| J4 | SMT_HDR_2x1.25mm | 电池连接器，连接 VBAT_UFUSED 与 GND | 图 c85e5e48676f / 第 1 页 / 第7资源 B1，J4 SMT_HDR_2x1.25mm |
| J11 | TOUCH_I2C | 触摸面板接口，提供 I2C、TOUCH_INT、ESP32_EN、3.3V 和 GND | 图 c85e5e48676f / 第 1 页 / 第7资源 B1-B2，J11 TOUCH_I2C |
| U12/U13/U15/U16 | SRV05-4 | USB 与三路外部 GPIO 接口的多通道 ESD 保护阵列 | 图 c85e5e48676f / 第 1 页 / 第7资源 A3 U12；B2-D2 U13/U15/U16 SRV05-4 |
| FET1/FET2 | CJ2301-PMOS/CJ2302-NMOS | 电池主电源锁存开关，由 PWR_EN/PS_ON/RTC_ALM/KEY_PUSH 控制 | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 B3-C4，FET1/FET2 与 FUSE1 |
| FET3-FET6 | CJ3134KW/SE7401U | 受 EXT_PWR_EN 与 EPD_PWR_EN 控制的 VEXT_5V 和 VEPD_5V 负载开关 | 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 D1-D3，FET3-FET6 |

## 系统结构

### Paper 系统架构

ESP32 主控连接外部 Flash/PSRAM、EEPROM、SHT30、RTC、microSD、触摸、USB-UART 和三路扩展口，并通过 SPI 控制 IT8951E-64；IT8951 配套独立 Flash、温度传感器、数字电源与 TPS65185 高压 PMIC 驱动 ED047TC1 面板。

- 参数与网络：`mcu=U1 ESP32`；`display_controller=U5 IT8951E-64`；`panel=J1 EPD_ED047TC1`；`system_flash=U4 W25Q128`；`psram=U3 ESPPSRAM64H`；`rtc=U23 PCF8563`；`usb_uart=U14 CP2104`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源完整页; 图 f320feda5dae / 第 1 页 / 第2资源 IT8951 子系统; 图 90ad5fabab87 / 第 1 页 / 第4资源 IT8951 至 EPD 面板; 图 8e0e8eeb66e9 / 第 1 页 / 第6资源系统电源与 RTC; 图 c85e5e48676f / 第 1 页 / 第7资源外部接口

## 核心器件

### U1 ESP32

U1 原理图型号仅标 ESP32，CHIP_PU 接 ESP32_EN，GPIO1/3 为 UART0，GPIO21/22 为内部 I2C，GPIO12-15 与 GPIO27 连接 IT8951 SPI/状态信号。

- 参数与网络：`reference=U1`；`schematic_part=ESP32`；`reset=ESP32_EN -> CHIP_PU`；`uart=GPIO1 U0TXD; GPIO3 U0RXD`；`i2c=GPIO21 SDA; GPIO22 SCL`；`it_spi=GPIO12/13/14/15/27`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 A1-B1，U1 ESP32

### U5 IT8951E-64

U5 IT8951E-64 通过 IT_SPI_CS/SCK/MOSI/MISO 与 ESP32 通信，并输出 EPD1_D0-D7、X/Y 时序、SDCLK 与高压电源控制。

- 参数与网络：`reference=U5A/U5B/U5C/U5D`；`part_number=IT8951E-64`；`host_spi=IT_SPI_CS/SCK/MOSI/MISO`；`panel_data=EPD1_D0-D7`；`panel_timing=EPD1_X_LATCH/X_OE/X_ST/Y_ST/Y_CLK; SDCLK_EPD`
- 证据：图 f320feda5dae / 第 1 页 / 第2资源 U5A/U5C; 图 90ad5fabab87 / 第 1 页 / 第4资源 U5B/U5D

### U23 RTC

原理图明确将 U23 标为 PCF8563，VDD 接 VBAT_IN，SDA/SCL 接内部 I2C，INT 输出 RTC_ALM。

- 参数与网络：`reference=U23`；`part_number=PCF8563`；`power=VBAT_IN`；`sda=I2C_SDA`；`scl=I2C_SCL`；`interrupt=RTC_ALM`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C4-D4 U23 PCF8563

## 电源

### IT8951 1.8V 与 3.3V 电源

U18/U19 两颗 SY8003 从 VEPD_5V 分别生成 VEPD_1V8 与 VEPD_3V3；FB1-FB4 600R 磁珠派生 VEPD_1V8A、VEPD_3V3A、VEPD_3V3A_U20 与 VEPD_3V3A_HSRT。

- 参数与网络：`u18_output=VEPD_1V8`；`u19_output=VEPD_3V3`；`enable=IT_3V3_EN`；`analog_rails=VEPD_1V8A; VEPD_3V3A; VEPD_3V3A_U20; VEPD_3V3A_HSRT`；`filters=FB1-FB4 600R/FB`
- 证据：图 b9201c64714c / 第 1 页 / 第3资源 A1-B4 U18/U19 与 FB1-FB4

### TPS65185 EPD 高压电源

U7 TPS65185 以 VEPD_5V/VEPD_3V3 供电，通过 IT_I2C 控制并生成 TPS_VNEG/VEE/VDDH/VPOS/VB/VCOM 等网络，经二极管、电感和反馈网络形成 EPD_VNEG/VEE/VDDH/VPOS/VCOM。

- 参数与网络：`reference=U7`；`part_number=TPS65185`；`control_bus=IT_I2C_SCL/IT_I2C_SDA`；`input=VEPD_5V; VEPD_3V3`；`outputs=EPD_VNEG; EPD_VEE; EPD_VDDH; EPD_VPOS; EPD_VCOM`；`status=TPS_PG; TPS_INT`
- 证据：图 69bd3e2f206a / 第 1 页 / 第5资源完整页，U7 TPS65185 与高压网络

### 电池与 USB 系统电源合路

D9/D12 两颗 DSK34 分别从 VBAT 与 VUSB_VIN 汇入 VSYS；VSYS 为 U8 SY7088 的输入。

- 参数与网络：`battery=VBAT -> D9 DSK34`；`usb=VUSB_VIN -> D12 DSK34`；`output=VSYS`；`converter=U8 SY7088`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C2 D9/D12 与 A1 U8

### U9 SLM6600 充电

U9 SLM6600 以 VUSB_VIN 为 VCC/TS 输入，经 L5 与 R32 1K 输出 VBAT_IN，PROG 通过 R31 1K 接地。

- 参数与网络：`reference=U9`；`part_number=SLM6600`；`input=VUSB_VIN`；`battery=VBAT_IN`；`inductor=L5 WPN3012H2R2MT`；`program_resistor=R31 1K`；`battery_series=R32 1K`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 A3 U9 SLM6600

### VBUS_5V 电源轨

U8 SY7088 从 VSYS 经 L4 升压生成 VBUS_5V，反馈网络为 R30 15K 与 R33 4.7K，EN 接 VSYS。

- 参数与网络：`reference=U8`；`input=VSYS`；`output=VBUS_5V`；`inductor=L4 WPN3012H2R2MT`；`feedback=R30 15K; R33 4.7K`；`enable=VSYS`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 A1-A2 U8 SY7088

### VCC_3V3 电源轨

U17 SY8003 从 VBUS_5V 经 L6 降压生成 VCC_3V3，反馈为 R36 68K/R38 15K。

- 参数与网络：`reference=U17`；`input=VBUS_5V`；`output=VCC_3V3`；`inductor=L6 WPN3012H2R2MT`；`feedback=R36 68K; R38 15K`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C1-C2 U17 SY8003

### 电池主电源锁存

VBAT_UFUSED 经 FUSE1 6V/2A Poly 和 FET1 CJ2301-PMOS 形成 VBAT；FET2 CJ2302-NMOS 由 PWR_EN/PS_ON 控制，RTC_ALM 与 KEY_PUSH 经 D7/D8/D10 汇入启动节点。

- 参数与网络：`input=VBAT_UFUSED`；`fuse=FUSE1 6V/2A/Poly`；`high_side=FET1 CJ2301-PMOS`；`control=FET2 CJ2302-NMOS; PWR_EN; PS_ON`；`wake_sources=RTC_ALM; KEY_PUSH_IO; KEY_PUSH`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 B3-C4 电源锁存区

### 扩展与 EPD 5V 负载开关

FET3/FET5 与 FUSE2 由 EXT_PWR_EN 控制 VEXT_5V；FET4/FET6 由 EPD_PWR_EN 控制 VEPD_5V，两路均从 VBUS_5V 派生。

- 参数与网络：`external_rail=VBUS_5V -> FET3/FET5/FUSE2 -> VEXT_5V`；`external_enable=EXT_PWR_EN`；`epd_rail=VBUS_5V -> FET4/FET6 -> VEPD_5V`；`epd_enable=EPD_PWR_EN`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 D1-D3 FET3-FET6

## 接口

### J1 ED047TC1 面板

J1 EPD_ED047TC1 接收 EPD1_D0-D7、XCL/XLE/XOE/XSTL、CKV/SPV、BORDER 与 EPD_VCOM/VDDH/VEE/VPOS/VNEG 电源，外壳接地。

- 参数与网络：`reference=J1`；`part_number=EPD_ED047TC1`；`data=pins 14-21 D0-D7`；`source_timing=pins 10-13 XCL/XLE/XOE/XSTL`；`gate_timing=pins 36-37 CKV/SPV`；`rails=VNEG, VPOS, EPD_3V3, EPD_VCOM, EPD_VDDH, EPD_VEE`；`shell=GND`
- 证据：图 90ad5fabab87 / 第 1 页 / 第4资源 A4-C4 J1 EPD_ED047TC1

### J3 USB Type-C

J3 VCC 接 VUSB_VIN，A6/B6 汇为 USB_D_P，A7/B7 汇为 USB_D_N，CC1/CC2 分别通过 R40/R44 5.1K 接 GND，数据经 U12 SRV05-4 保护后接 CP2104。

- 参数与网络：`reference=J3`；`power=VUSB_VIN`；`data_plus=A6/B6 USB_D_P`；`data_minus=A7/B7 USB_D_N`；`cc=R40/R44 5.1K to GND`；`protection=U12 SRV05-4`；`direction=USB data bidirectional; power input`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 A2-A3 J3/U12

### J11 触摸接口

J11 TOUCH_I2C 提供 VCC_3V3、GND、I2C_SDA、I2C_SCL、TOUCH_INT 与 ESP32_EN；TOUCH_INT 由 R87 10K 上拉并连接 ESP32 GPIO36。

- 参数与网络：`reference=J11`；`pin_1=VCC_3V3`；`pin_2=GND`；`pin_3=I2C_SDA`；`pin_4=I2C_SCL`；`pin_5=TOUCH_INT / GPIO36`；`pin_6=ESP32_EN`；`pullup=R87 10K`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 B1-B2 J11 TOUCH_I2C; 图 1442b3537acb / 第 1 页 / 第1资源 U1 GPIO36 TOUCH_INT

### 三路 PH2.0-4P 扩展口

J5 引出 GPIO32/GPIO25，J6 引出 GPIO33/GPIO26，J7 引出 GPIO19/GPIO18；每口 3 脚为 VEXT_5V、4 脚为 GND，信号经 47Ω 与 SRV05-4 保护。

- 参数与网络：`j5=pin1 GPIO32; pin2 GPIO25; pin3 VEXT_5V; pin4 GND`；`j6=pin1 GPIO33; pin2 GPIO26; pin3 VEXT_5V; pin4 GND`；`j7=pin1 GPIO19; pin2 GPIO18; pin3 VEXT_5V; pin4 GND`；`series=R45/R46/R49/R51/R53/R55 47Ω`；`protection=U13/U15/U16 SRV05-4`；`logic_level=VCC_3V3`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 B1-D2 J5/J6/J7 与 U13/U15/U16

## 总线

### ESP32 内部 I2C

ESP32 GPIO21/GPIO22 分别为 I2C_SDA/I2C_SCL，R88/R89 各 2K 上拉至 VCC_3V3；该总线连接 FM24C02B、SHT30、PCF8563 与触摸接口。

- 参数与网络：`controller=U1 ESP32`；`sda=GPIO21 / I2C_SDA`；`scl=GPIO22 / I2C_SCL`；`pullups=R88/R89 2K to VCC_3V3`；`devices=U2 FM24C02B; U22 SHT30; U23 PCF8563; J11 TOUCH_I2C`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 B1/D4 GPIO21/22 与 R88/R89; 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 U23 I2C; 图 c85e5e48676f / 第 1 页 / 第7资源 J11 TOUCH_I2C

### ESP32 至 IT8951 SPI

ESP32 GPIO15 为 IT_SPI_CS，GPIO14 经 R10 200Ω 为 IT_SPI_SCK，GPIO12 为 IT_SPI_MOSI，GPIO13 为 IT_SPI_MISO，GPIO27 接 IT_SPI_HRDY。

- 参数与网络：`controller=U1 ESP32`；`device=U5 IT8951E-64`；`cs=GPIO15 / IT_SPI_CS`；`sck=GPIO14 / IT_SPI_SCK via R10 200Ω`；`mosi=GPIO12 / IT_SPI_MOSI`；`miso=GPIO13 / IT_SPI_MISO`；`ready=GPIO27 / IT_SPI_HRDY`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 A1 U1 IT_SPI 信号; 图 f320feda5dae / 第 1 页 / 第2资源 U5C SPI2/HRDY

### IT8951 I2C 子总线

U5C I2C_SCL/I2C_SDA 网络标为 IT_I2C_SCL/IT_I2C_SDA，并连接 U11 SE95D；R15/R16 各 0Ω 从 VEPD_3V3 接到两线。

- 参数与网络：`controller=U5C IT8951E-64`；`device=U11 SE95D`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA`；`resistors=R15/R16 0Ω`
- 证据：图 f320feda5dae / 第 1 页 / 第2资源 B2 U5C 与 D2 U11

## 总线地址

### I2C 地址可见性

七张原理图未直接标注 GT911、SHT30、PCF8563/BM8563、FM24C02B、SE95D 或 TPS65185 的数值 I2C 地址。

- 参数与网络：`addresses_visible=false`；`devices=touch; U22 SHT30; U23 PCF8563; U2 FM24C02B; U11 SE95D; U7 TPS65185`；`address_values=null`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 I2C 器件，未见数值地址; 图 f320feda5dae / 第 1 页 / 第2资源 U11，未见数值地址; 图 69bd3e2f206a / 第 1 页 / 第5资源 U7，未见数值地址; 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 U23，未见数值地址

## GPIO 与控制信号

### 三向拨轮按键

J2 K1-1502SA-02 输出 KEY_LEFT、KEY_PUSH、KEY_RIGHT，分别连接 ESP32 GPIO39、GPIO38、GPIO37，R41/R42/R43 各 10K 上拉至 VCC_3V3。

- 参数与网络：`switch=J2 K1-1502SA-02`；`left=KEY_LEFT / GPIO39`；`push=KEY_PUSH / GPIO38`；`right=KEY_RIGHT / GPIO37`；`pullups=R41/R42/R43 10K`；`direction=input`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 A1-A2 J2 与 R41-R43; 图 1442b3537acb / 第 1 页 / 第1资源 U1 GPIO37/38/39

## 时钟

### ESP32 主晶振

U1 XTAL_P/XTAL_N 连接 X1 TXC/8Z40000017 晶振，两端各以 C17/C18 12pF 接地，ESP_XTAL_P 串联 R3 100Ω。

- 参数与网络：`crystal=X1 TXC/8Z40000017`；`load_caps=C17/C18 12pF`；`series_resistor=R3 100Ω`；`nets=ESP_XTAL_P/ESP_XTAL_N`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 C1 晶振区

### IT8951 晶振

IT8951 XSCI/XSCO 连接 X2 12MHz/20ppm 晶振，C45/C46 各 18pF 接地。

- 参数与网络：`device=U5 IT8951E-64`；`crystal=X2`；`frequency=12MHz`；`tolerance=20ppm`；`load_caps=C45/C46 18pF`
- 证据：图 f320feda5dae / 第 1 页 / 第2资源 B1 X2 与 U5A XSCI/XSCO

### RTC 32.768K 晶振

U23 OSCI/OSCO 连接 Y1 32.768K/6pF 晶振，C124/C125 各 6pF 接地。

- 参数与网络：`rtc=U23 PCF8563`；`crystal=Y1`；`frequency=32.768K`；`load_label=6pF`；`capacitors=C124/C125 6pF`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 C4-D4 Y1/C124/C125

## 复位

### IT8951 复位

U20 SGM803 监测 VEPD_3V3 并输出 IT_RST#，R82 10K 将 IT_RST# 上拉至 VEPD_3V3。

- 参数与网络：`supervisor=U20 SGM803-SXN3/TR`；`threshold_label=2.93V`；`input=VEPD_3V3`；`output=IT_RST#`；`pullup=R82 10K`
- 证据：图 b9201c64714c / 第 1 页 / 第3资源 C1 U20

### ESP32 自动下载复位

CP_RTS/CP_DTR 通过 VT1/VT2、R50/R52 与 D13 BAS3010 控制 ESP32_EN 和 GPIO0，GPIO0 由 R54 2.2K 上拉至 VCC_3V3；OS1 可将 ESP32_EN 手动拉低。

- 参数与网络：`reset=ESP32_EN`；`boot=GPIO0`；`sources=CP_RTS/CP_DTR`；`transistors=VT1/VT2`；`boot_pullup=R54 2.2K`；`manual_reset=OS1 SMT_SW_PTS_820`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 B2 OS1；B4-D4 VT1/VT2/D13

## 保护电路

### USB 与 GPIO ESD 保护

U12 SRV05-4 保护 USB_D_P/USB_D_N；U13/U15/U16 SRV05-4 分别保护 J5/J6/J7 的六路 GPIO，外部信号另串联 47Ω。

- 参数与网络：`usb=U12 SRV05-4`；`gpio=U13/U15/U16 SRV05-4`；`protected_gpio=GPIO32, GPIO25, GPIO33, GPIO26, GPIO19, GPIO18`；`series_resistors=47Ω`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 A3 与 B2-D2 SRV05-4 阵列

## 关键网络

### RTC 唤醒

U23 INT 输出 RTC_ALM，经 D7 1N4148 汇入电源锁存启动节点，与 KEY_PUSH_IO/KEY_PUSH 路径共同触发上电。

- 参数与网络：`source=U23 INT / RTC_ALM`；`diode=D7 1N4148`；`destination=PWR_EN/PS_ON latch node`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 B4 RTC_ALM/D7 与 U23 INT

## 存储

### U4 系统 Flash

U4 W25Q128 由 VDD_SDIO 供电，CLK/DI/DO/WP/HOLD 分别连接 SD_CLK、SD_CMD 与 SD_DATA0-3。

- 参数与网络：`reference=U4`；`part_number=W25Q128`；`power=VDD_SDIO`；`clock=SD_CLK`；`command=SD_CMD`；`data=SD_DATA0-3`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 D2 U4 W25Q128

### U2 I2C EEPROM

U2 FM24C02B-DN-T-G 连接 I2C_SCL/I2C_SDA，A0/A1/A2 接 GND，WP 接 GND，VCC 为 VCC_3V3。

- 参数与网络：`reference=U2`；`part_number=FM24C02B-DN-T-G`；`scl=I2C_SCL`；`sda=I2C_SDA`；`address_straps=A0=A1=A2=GND`；`write_protect=WP=GND`；`power=VCC_3V3`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 A4 U2 FM24C02B

### IT8951 专用 Flash

U6 W25Q32 由 VEPD_3V3 供电，连接 IT_FLASH_CS#/SCK/SO/SI，并预留 J9 六针测试/编程接口。

- 参数与网络：`reference=U6`；`part_number=W25Q32`；`power=VEPD_3V3`；`bus=IT_FLASH_CS#/SCK/SO/SI`；`header=J9`
- 证据：图 f320feda5dae / 第 1 页 / 第2资源 A1 U6 与 B3 J9

### U21 microSD

U21 卡座由 VCC_3V3 供电，CMD 接 SD_CS，CLK 接 IT_SPI_SCK，DAT3 接 IT_SPI_MOSI，DAT0 接 IT_SPI_MISO，CARD_CD 经 R84 10K 上拉。

- 参数与网络：`reference=U21`；`part_number=5033981892`；`power=VCC_3V3`；`cs=SD_CS`；`sck=IT_SPI_SCK`；`mosi=IT_SPI_MOSI`；`miso=IT_SPI_MISO`；`card_detect=CARD_CD via R84 10K`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 A4 U21 microSD

## 内存与 Flash

### U3 PSRAM

U3 ESPPSRAM64H 使用 SD_DATA0-3 作为 SIO0-3，PSRAM_CLK 接 SCLK，PSRAM_CS 接 nCS，并由 VDD_SDIO 供电。

- 参数与网络：`reference=U3`；`part_number=ESPPSRAM64H`；`bus_width=4-bit SIO0-3`；`chip_select=PSRAM_CS`；`clock=PSRAM_CLK`；`power=VDD_SDIO`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 C2 U3 ESPPSRAM64H

## 传感器

### U22 SHT30

U22 SHT30 由 VCC_3V3 供电，SDA/SCL 接内部 I2C，ADDR 接 GND；ALERT 与 NRST 未连接。

- 参数与网络：`reference=U22`；`part_number=SHT30`；`bus=I2C_SDA/I2C_SCL`；`address_strap=ADDR=GND`；`power=VCC_3V3`；`unused=ALERT; NRST`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 B4 U22 SHT30

### U11 SE95D

U11 SE95D 接 IT_I2C_SDA/IT_I2C_SCL，A0/A1/A2 接 GND，OS 经 R68 10K 上拉至 VEPD_3V3。

- 参数与网络：`reference=U11`；`part_number=SE95D`；`bus=IT_I2C`；`address_straps=A0=A1=A2=GND`；`alert=OS via R68 10K`；`power=VEPD_3V3`
- 证据：图 f320feda5dae / 第 1 页 / 第2资源 D2-D3 U11 SE95D

## 射频

### ESP32 天线路径

ESP_LNA 经预留 L1、串联 C1 与对地 C3 匹配位连接 ANT1 PROANT_440，L1/C1/C3 均标 TBD/NC。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`matching=L1 TBD/NC; C1 TBD/0R; C3 TBD/NC`
- 证据：图 1442b3537acb / 第 1 页 / 第1资源 A2-A3 RF 区

## 调试与烧录

### CP2104 下载串口

U14 CP2104 D+/D- 接 USB_D_P/N，TXD 经 R56 47Ω 接 ESP32_U0RXD，RXD 经 R57 47Ω 接 ESP32_U0TXD，DTR/RTS 驱动自动下载网络。

- 参数与网络：`bridge=U14 CP2104`；`usb=USB_D_P/USB_D_N`；`tx=CP_TXD -> R56 47Ω -> ESP32_U0RXD`；`rx=CP_RXD -> R57 47Ω -> ESP32_U0TXD`；`control=CP_DTR/CP_RTS`
- 证据：图 c85e5e48676f / 第 1 页 / 第7资源 B3-D3 U14 CP2104

## 模拟电路

### 电池电压采样

VBAT 通过 R83 3K 与 R86 11K 分压生成 VBAT_S，供 ESP32 GPIO35/VBAT_S 网络采样。

- 参数与网络：`input=VBAT`；`output=VBAT_S`；`divider=R83 3K; R86 11K`；`adc_gpio=GPIO35`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 D3 VBAT_S 分压; 图 1442b3537acb / 第 1 页 / 第1资源 U1 GPIO35/VBAT_S

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Paper 系统架构 | `mcu=U1 ESP32`；`display_controller=U5 IT8951E-64`；`panel=J1 EPD_ED047TC1`；`system_flash=U4 W25Q128`；`psram=U3 ESPPSRAM64H`；`rtc=U23 PCF8563`；`usb_uart=U14 CP2104` |
| 核心器件 | U1 ESP32 | `reference=U1`；`schematic_part=ESP32`；`reset=ESP32_EN -> CHIP_PU`；`uart=GPIO1 U0TXD; GPIO3 U0RXD`；`i2c=GPIO21 SDA; GPIO22 SCL`；`it_spi=GPIO12/13/14/15/27` |
| 核心器件 | ESP32 精确型号 | `documented_model=ESP32-D0WDQ6-V3`；`schematic_label=ESP32` |
| 存储 | U4 系统 Flash | `reference=U4`；`part_number=W25Q128`；`power=VDD_SDIO`；`clock=SD_CLK`；`command=SD_CMD`；`data=SD_DATA0-3` |
| 内存与 Flash | U3 PSRAM | `reference=U3`；`part_number=ESPPSRAM64H`；`bus_width=4-bit SIO0-3`；`chip_select=PSRAM_CS`；`clock=PSRAM_CLK`；`power=VDD_SDIO` |
| 内存与 Flash | Flash 与 PSRAM 容量 | `documented_flash=16MB`；`documented_psram=8MB Quad`；`schematic_flash=W25Q128`；`schematic_psram=ESPPSRAM64H` |
| 存储 | U2 I2C EEPROM | `reference=U2`；`part_number=FM24C02B-DN-T-G`；`scl=I2C_SCL`；`sda=I2C_SDA`；`address_straps=A0=A1=A2=GND`；`write_protect=WP=GND`；`power=VCC_3V3` |
| 传感器 | U22 SHT30 | `reference=U22`；`part_number=SHT30`；`bus=I2C_SDA/I2C_SCL`；`address_strap=ADDR=GND`；`power=VCC_3V3`；`unused=ALERT; NRST` |
| 射频 | ESP32 天线路径 | `source=ESP_LNA`；`antenna=ANT1 PROANT_440`；`matching=L1 TBD/NC; C1 TBD/0R; C3 TBD/NC` |
| 时钟 | ESP32 主晶振 | `crystal=X1 TXC/8Z40000017`；`load_caps=C17/C18 12pF`；`series_resistor=R3 100Ω`；`nets=ESP_XTAL_P/ESP_XTAL_N` |
| 总线 | ESP32 内部 I2C | `controller=U1 ESP32`；`sda=GPIO21 / I2C_SDA`；`scl=GPIO22 / I2C_SCL`；`pullups=R88/R89 2K to VCC_3V3`；`devices=U2 FM24C02B; U22 SHT30; U23 PCF8563; J11 TOUCH_I2C` |
| 总线地址 | I2C 地址可见性 | `addresses_visible=false`；`devices=touch; U22 SHT30; U23 PCF8563; U2 FM24C02B; U11 SE95D; U7 TPS65185`；`address_values=null` |
| 核心器件 | U5 IT8951E-64 | `reference=U5A/U5B/U5C/U5D`；`part_number=IT8951E-64`；`host_spi=IT_SPI_CS/SCK/MOSI/MISO`；`panel_data=EPD1_D0-D7`；`panel_timing=EPD1_X_LATCH/X_OE/X_ST/Y_ST/Y_CLK; SDCLK_EPD` |
| 总线 | ESP32 至 IT8951 SPI | `controller=U1 ESP32`；`device=U5 IT8951E-64`；`cs=GPIO15 / IT_SPI_CS`；`sck=GPIO14 / IT_SPI_SCK via R10 200Ω`；`mosi=GPIO12 / IT_SPI_MOSI`；`miso=GPIO13 / IT_SPI_MISO`；`ready=GPIO27 / IT_SPI_HRDY` |
| 存储 | IT8951 专用 Flash | `reference=U6`；`part_number=W25Q32`；`power=VEPD_3V3`；`bus=IT_FLASH_CS#/SCK/SO/SI`；`header=J9` |
| 时钟 | IT8951 晶振 | `device=U5 IT8951E-64`；`crystal=X2`；`frequency=12MHz`；`tolerance=20ppm`；`load_caps=C45/C46 18pF` |
| 总线 | IT8951 I2C 子总线 | `controller=U5C IT8951E-64`；`device=U11 SE95D`；`scl=IT_I2C_SCL`；`sda=IT_I2C_SDA`；`resistors=R15/R16 0Ω` |
| 传感器 | U11 SE95D | `reference=U11`；`part_number=SE95D`；`bus=IT_I2C`；`address_straps=A0=A1=A2=GND`；`alert=OS via R68 10K`；`power=VEPD_3V3` |
| 接口 | J1 ED047TC1 面板 | `reference=J1`；`part_number=EPD_ED047TC1`；`data=pins 14-21 D0-D7`；`source_timing=pins 10-13 XCL/XLE/XOE/XSTL`；`gate_timing=pins 36-37 CKV/SPV`；`rails=VNEG, VPOS, EPD_3V3, EPD_VCOM, EPD_VDDH, EPD_VEE`；`shell=GND` |
| 核心器件 | 电子墨水屏规格 | `schematic_panel=EPD_ED047TC1`；`controller=IT8951E-64`；`documented_resolution=540x960`；`documented_size=4.7 inch`；`documented_grayscale=16 levels` |
| 电源 | IT8951 1.8V 与 3.3V 电源 | `u18_output=VEPD_1V8`；`u19_output=VEPD_3V3`；`enable=IT_3V3_EN`；`analog_rails=VEPD_1V8A; VEPD_3V3A; VEPD_3V3A_U20; VEPD_3V3A_HSRT`；`filters=FB1-FB4 600R/FB` |
| 复位 | IT8951 复位 | `supervisor=U20 SGM803-SXN3/TR`；`threshold_label=2.93V`；`input=VEPD_3V3`；`output=IT_RST#`；`pullup=R82 10K` |
| 电源 | TPS65185 EPD 高压电源 | `reference=U7`；`part_number=TPS65185`；`control_bus=IT_I2C_SCL/IT_I2C_SDA`；`input=VEPD_5V; VEPD_3V3`；`outputs=EPD_VNEG; EPD_VEE; EPD_VDDH; EPD_VPOS; EPD_VCOM`；`status=TPS_PG; TPS_INT` |
| 电源 | 电池与 USB 系统电源合路 | `battery=VBAT -> D9 DSK34`；`usb=VUSB_VIN -> D12 DSK34`；`output=VSYS`；`converter=U8 SY7088` |
| 电源 | U9 SLM6600 充电 | `reference=U9`；`part_number=SLM6600`；`input=VUSB_VIN`；`battery=VBAT_IN`；`inductor=L5 WPN3012H2R2MT`；`program_resistor=R31 1K`；`battery_series=R32 1K` |
| 电源 | VBUS_5V 电源轨 | `reference=U8`；`input=VSYS`；`output=VBUS_5V`；`inductor=L4 WPN3012H2R2MT`；`feedback=R30 15K; R33 4.7K`；`enable=VSYS` |
| 电源 | VCC_3V3 电源轨 | `reference=U17`；`input=VBUS_5V`；`output=VCC_3V3`；`inductor=L6 WPN3012H2R2MT`；`feedback=R36 68K; R38 15K` |
| 电源 | 电池主电源锁存 | `input=VBAT_UFUSED`；`fuse=FUSE1 6V/2A/Poly`；`high_side=FET1 CJ2301-PMOS`；`control=FET2 CJ2302-NMOS; PWR_EN; PS_ON`；`wake_sources=RTC_ALM; KEY_PUSH_IO; KEY_PUSH` |
| 电源 | 扩展与 EPD 5V 负载开关 | `external_rail=VBUS_5V -> FET3/FET5/FUSE2 -> VEXT_5V`；`external_enable=EXT_PWR_EN`；`epd_rail=VBUS_5V -> FET4/FET6 -> VEPD_5V`；`epd_enable=EPD_PWR_EN` |
| 模拟电路 | 电池电压采样 | `input=VBAT`；`output=VBAT_S`；`divider=R83 3K; R86 11K`；`adc_gpio=GPIO35` |
| 核心器件 | U23 RTC | `reference=U23`；`part_number=PCF8563`；`power=VBAT_IN`；`sda=I2C_SDA`；`scl=I2C_SCL`；`interrupt=RTC_ALM` |
| 核心器件 | RTC 型号命名 | `documented_model=BM8563`；`schematic_model=PCF8563`；`reference=U23` |
| 时钟 | RTC 32.768K 晶振 | `rtc=U23 PCF8563`；`crystal=Y1`；`frequency=32.768K`；`load_label=6pF`；`capacitors=C124/C125 6pF` |
| 关键网络 | RTC 唤醒 | `source=U23 INT / RTC_ALM`；`diode=D7 1N4148`；`destination=PWR_EN/PS_ON latch node` |
| 接口 | J3 USB Type-C | `reference=J3`；`power=VUSB_VIN`；`data_plus=A6/B6 USB_D_P`；`data_minus=A7/B7 USB_D_N`；`cc=R40/R44 5.1K to GND`；`protection=U12 SRV05-4`；`direction=USB data bidirectional; power input` |
| 调试与烧录 | CP2104 下载串口 | `bridge=U14 CP2104`；`usb=USB_D_P/USB_D_N`；`tx=CP_TXD -> R56 47Ω -> ESP32_U0RXD`；`rx=CP_RXD -> R57 47Ω -> ESP32_U0TXD`；`control=CP_DTR/CP_RTS` |
| 复位 | ESP32 自动下载复位 | `reset=ESP32_EN`；`boot=GPIO0`；`sources=CP_RTS/CP_DTR`；`transistors=VT1/VT2`；`boot_pullup=R54 2.2K`；`manual_reset=OS1 SMT_SW_PTS_820` |
| 核心器件 | USB-UART 批次 | `schematic_part=CP2104`；`documented_variant=CH9102`；`variant_schematic_available=false` |
| 存储 | U21 microSD | `reference=U21`；`part_number=5033981892`；`power=VCC_3V3`；`cs=SD_CS`；`sck=IT_SPI_SCK`；`mosi=IT_SPI_MOSI`；`miso=IT_SPI_MISO`；`card_detect=CARD_CD via R84 10K` |
| 接口 | J11 触摸接口 | `reference=J11`；`pin_1=VCC_3V3`；`pin_2=GND`；`pin_3=I2C_SDA`；`pin_4=I2C_SCL`；`pin_5=TOUCH_INT / GPIO36`；`pin_6=ESP32_EN`；`pullup=R87 10K` |
| 传感器 | 触摸控制器型号 | `documented_model=GT911`；`schematic_interface=J11 TOUCH_I2C`；`device_reference=null` |
| GPIO 与控制信号 | 三向拨轮按键 | `switch=J2 K1-1502SA-02`；`left=KEY_LEFT / GPIO39`；`push=KEY_PUSH / GPIO38`；`right=KEY_RIGHT / GPIO37`；`pullups=R41/R42/R43 10K`；`direction=input` |
| 接口 | 三路 PH2.0-4P 扩展口 | `j5=pin1 GPIO32; pin2 GPIO25; pin3 VEXT_5V; pin4 GND`；`j6=pin1 GPIO33; pin2 GPIO26; pin3 VEXT_5V; pin4 GND`；`j7=pin1 GPIO19; pin2 GPIO18; pin3 VEXT_5V; pin4 GND`；`series=R45/R46/R49/R51/R53/R55 47Ω`；`protection=U13/U15/U16 SRV05-4`；`logic_level=VCC_3V3` |
| 保护电路 | USB 与 GPIO ESD 保护 | `usb=U12 SRV05-4`；`gpio=U13/U15/U16 SRV05-4`；`protected_gpio=GPIO32, GPIO25, GPIO33, GPIO26, GPIO19, GPIO18`；`series_resistors=47Ω` |
| 电源 | 内置电池容量 | `documented_capacity=1150mAh`；`documented_voltage=3.7V`；`connector=J4 SMT_HDR_2x1.25mm`；`schematic_capacity_label=null` |

## 待确认事项

- `component.mcu-exact-model`：产品正文称主控为 ESP32-D0WDQ6-V3，但原理图 U1 只标 ESP32，未显示 D0WDQ6-V3 后缀。（证据：图 1442b3537acb / 第 1 页 / 第1资源 U1 仅标 ESP32）
- `memory.documented-capacities`：产品正文标称 16MB Flash 与 8MB Quad PSRAM；原理图仅显示 W25Q128、ESPPSRAM64H 型号而未以字节数标注容量。（证据：图 1442b3537acb / 第 1 页 / 第1资源 U3/U4，未标字节容量）
- `component.panel-specification`：原理图明确标出 J1 EPD_ED047TC1 和 IT8951E-64，但未标注产品正文中的 540x960、4.7 英寸与 16 级灰度参数。（证据：图 90ad5fabab87 / 第 1 页 / 第4资源 J1/U5B/U5D，未见分辨率/尺寸/灰度标注）
- `component.rtc-name-conflict`：产品正文称 RTC 为 BM8563，当前原理图 U23 标为 PCF8563；两者在本地证据中的 BOM 对应关系无法确认。（证据：图 8e0e8eeb66e9 / 第 1 页 / 第6资源 U23 明确标 PCF8563）
- `component.usb-uart-variant`：本地原理图只画出 U14 CP2104；产品正文另称存在 CH9102 批次，但未提供对应本地电路页。（证据：图 c85e5e48676f / 第 1 页 / 第7资源 U14 明确标 CP2104）
- `sensor.touch-model`：产品正文称触摸控制器为 GT911，但七张原理图仅显示 J11 TOUCH_I2C，未标出 GT911 器件位号或型号。（证据：图 c85e5e48676f / 第 1 页 / 第7资源 J11，仅标 TOUCH_I2C）
- `power.battery-capacity`：产品正文称内置 1150mAh@3.7V 电池；原理图只显示 J4、VBAT_UFUSED/VBAT_IN/VBAT 网络，未标容量。（证据：图 c85e5e48676f / 第 1 页 / 第7资源 J4 电池口，未标容量; 图 8e0e8eeb66e9 / 第 1 页 / 第6资源 VBAT 电源路径，未标容量）
- `review.mcu-exact-model`：Paper K049 当前硬件的 U1 是否固定为 ESP32-D0WDQ6-V3？；原因：精确型号来自产品正文，原理图仅标 ESP32。
- `review.memory-capacities`：W25Q128 与 ESPPSRAM64H 在当前 BOM 中是否分别对应 16MB Flash 和 8MB Quad PSRAM？；原因：字节容量来自产品正文，原理图只给出器件型号。
- `review.panel-specification`：J1 ED047TC1 面板是否确定为 540x960、4.7 英寸、16 级灰度版本？；原因：型号可由原理图确认，但分辨率、尺寸和灰度只出现在产品正文。
- `review.rtc-name`：产品 BOM 中的 RTC 应标为 PCF8563 还是 BM8563，二者是否为不同批次替代料？；原因：正式原理图 U23 为 PCF8563，产品正文称 BM8563。
- `review.usb-uart-variant`：CH9102 批次是否有独立原理图，自动下载网络是否与当前 CP2104 图一致？；原因：七张本地原理图仅显示 CP2104。
- `review.touch-model`：J11 所接触摸控制器是否固定为 GT911？；原因：GT911 来自产品正文，原理图只画出 TOUCH_I2C 接口。
- `review.battery-capacity`：当前 Paper K049 内置电池是否为 1150mAh@3.7V？；原因：容量和标称电压来自产品正文，原理图未标注。

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

源文档：`zh_CN/core/m5paper.md`

源文档 SHA-256：`988ff141f0600f8aec99a745950368c575fd34d742283cd9d674e18c20b23ddb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
