# Paper Comm Edition 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Paper Comm Edition |
| SKU | K049-C |
| 产品 ID | `paper-comm-edition-52a904d8e4ec` |
| 源文档 | `zh_CN/core/m5paper_comm.md` |

## 概述

Paper Comm Edition 以 U1 ESP32 为主控，配置 W25Q128 16MB Flash、ESPPSRAM64H 8MB PSRAM、FM24C02、SHT30、PCF8563、microSD 和 CP2104。电子纸子系统由 IT8951E-64、W25Q32、TPS65185、双 SY8003 和 EPD_ED047TC1 面板组成，ESP32 通过 SPI 控制 IT8951E。系统电源包含 SLM6600 充电、SY7088 5V 升压、SY8003 3.3V 降压及外设/EPD 负载开关，并提供 USB Type-C、三组 Grove、触摸 I2C 和拨轮按键。

## 检索关键词

`Paper Comm Edition`、`K049-C`、`ESP32`、`W25Q128`、`ESPPSRAM64H`、`FM24C02B-DN-T-G`、`SHT30`、`IT8951E-64`、`W25Q32`、`TPS65185`、`EPD_ED047TC1`、`SY8003`、`SY7088`、`SLM6600`、`PCF8563`、`CP2104`、`SE95D`、`SGM3167`、`USB Type-C`、`microSD`、`SPI`、`I2C`、`EPD`、`VEPD_5V`、`VEPD_3V3`、`VEPD_1V8`、`VCC_3V3`、`VBAT_IN`、`VSYS`、`VBUS_5V`、`GPIO21 SDA`、`GPIO22 SCL`、`GPIO13 MISO`、`GPIO12 MOSI`、`GPIO14 SCK`、`GPIO15 CS`、`GPIO4 SD_CS`、`GT911`、`BM8563`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 主控 SoC，连接存储、IT8951E、TF、I2C、按键、电源控制和扩展口 | 图 1442b3537acb / 第 1 页 / 第1页网格 A1-B1：U1 ESP32 |
| U4 | W25Q128 | ESP32 外部 SPI Flash | 图 1442b3537acb / 第 1 页 / 第1页网格 D2：U4 W25Q128 |
| U3 | ESPPSRAM64H | ESP32 外部 8线 PSRAM | 图 1442b3537acb / 第 1 页 / 第1页网格 C2：U3 ESPPSRAM64H |
| U2 | FM24C02B-DN-T-G | I2C 非易失 EEPROM | 图 1442b3537acb / 第 1 页 / 第1页网格 A4：U2 FM24C02B-DN-T-G |
| U22 | SHT30 | I2C 温湿度传感器 | 图 1442b3537acb / 第 1 页 / 第1页网格 B4：U22 SHT30 |
| U5 | IT8951E-64 | 电子纸显示控制器，连接 ESP32 SPI、专用 Flash、电源 PMIC 与 EPD 面板 | 图 f320feda5dae / 第 1 页 / 第2页 U5A/U5C IT8951E-64; 图 90ad5fabab87 / 第 1 页 / 第4页 U5B/U5D IT8951E-64 |
| U6 | W25Q32 | IT8951E 专用 SPI Flash | 图 f320feda5dae / 第 1 页 / 第2页网格 A1：U6 W25Q32 |
| X2 | 12MHz/20ppm | IT8951E 主时钟晶体 | 图 f320feda5dae / 第 1 页 / 第2页网格 B1：X2/C45/C46 |
| J1 (EPD) | EPD_ED047TC1 | 电子纸面板连接器，接收 IT8951E 数据/时序及高压轨 | 图 90ad5fabab87 / 第 1 页 / 第4页网格 A4-C4：J1 EPD_ED047TC1 |
| U7 | TPS65185 | 电子纸 VNEG/VPOS/VEE/VDDH/VCOM 电源管理器 | 图 69bd3e2f206a / 第 1 页 / 第5页网格 A1-B1：U7 TPS65185 |
| U18,U19 | SY8003 | VEPD_5V 到 VEPD_1V8/VEPD_3V3 的电子纸降压转换器 | 图 b9201c64714c / 第 1 页 / 第3页网格 A1-B2：U18/U19 SY8003 |
| U20 | SGM803-SXN3/TR | VEPD_3V3 监控并生成 IT_RST# | 图 b9201c64714c / 第 1 页 / 第3页网格 C1：U20 SGM803 |
| U8 | SY7088 | VSYS 到 VBUS_5V 的系统升压转换器 | 图 8e0e8eeb66e9 / 第 1 页 / 第6页网格 A1-A2：U8 SY7088 |
| U17 | SY8003 | VBUS_5V 到 VCC_3V3 的系统降压转换器 | 图 8e0e8eeb66e9 / 第 1 页 / 第6页网格 C1-C2：U17 SY8003 |
| U9 | SLM6600 | VUSB_VIN 到 VBAT_IN 的锂电池充电器 | 图 8e0e8eeb66e9 / 第 1 页 / 第6页网格 A3-A4：U9 SLM6600 |
| U23 | PCF8563 | I2C RTC 与 RTC_ALM 唤醒源 | 图 8e0e8eeb66e9 / 第 1 页 / 第6页网格 C4-D4：U23 PCF8563/Y1 |
| U14 | CP2104 | USB-UART 下载桥和自动复位控制 | 图 c85e5e48676f / 第 1 页 / 第7页网格 B3-C4：U14 CP2104/VT1/VT2 |
| U21 | 5033981892 | SPI microSD/TF 卡座 | 图 c85e5e48676f / 第 1 页 / 第7页网格 A4：U21 TF card socket |
| J5,J6,J7 | PH2.0_4P_SMT | GPIO25/32、GPIO26/33、GPIO18/19 三组 5V Grove 接口 | 图 c85e5e48676f / 第 1 页 / 第7页网格 B1-C2：J5/J6/J7 与 U13/U15/U16 |
| J2 | K1-1502SA-02 | KEY_LEFT/KEY_PUSH/KEY_RIGHT 拨轮开关 | 图 c85e5e48676f / 第 1 页 / 第7页网格 A1：J2 拨轮与 R41-R43 |

## 系统结构

### Paper Comm Edition 架构

ESP32 主控连接 16MB Flash、8MB PSRAM、I2C EEPROM/SHT30/RTC/触摸、SPI TF 与 IT8951E；IT8951E 通过独立电源和并行接口驱动 EPD_ED047TC1。

- 参数与网络：`mcu=U1 ESP32`；`flash=W25Q128`；`psram=ESPPSRAM64H`；`epd_controller=IT8951E-64`；`panel=EPD_ED047TC1`；`power=SLM6600/SY7088/SY8003/TPS65185`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 MCU/存储/I2C; 图 f320feda5dae / 第 1 页 / 第2页 IT8951E IO; 图 90ad5fabab87 / 第 1 页 / 第4页 IT8951E/EPD

## 核心器件

### IT8951E 专用 Flash 与时钟

IT8951E U5A 通过 IT_FLASH_CS#/SCK/SI/SO 连接 U6 W25Q32，X2 12MHz/20ppm 连接 XSCI/XSCO。

- 参数与网络：`controller=U5 IT8951E-64`；`flash=U6 W25Q32`；`crystal=X2 12MHz/20ppm`；`loads=C45/C46 18pF`
- 证据：图 f320feda5dae / 第 1 页 / 第2页 U5A/U6/X2

## 电源

### 电子纸 1.8V/3.3V 电源

U18 SY8003 从 VEPD_5V 生成 VEPD_1V8，U19 SY8003 生成 VEPD_3V3；FB1-FB4 分隔 VEPD_1V8A、VEPD_3V3A_U20 与 VEPD_3V3A_HSRT。

- 参数与网络：`u18=VEPD_5V -> VEPD_1V8`；`u19=VEPD_5V -> VEPD_3V3`；`filters=FB1-FB4 600R/FB`；`reset=U20 SGM803 -> IT_RST#`
- 证据：图 b9201c64714c / 第 1 页 / 第3页 U18/U19/U20/FB1-FB4

### TPS65185 EPD 高压电源

U7 TPS65185 由 VEPD_5V/VEPD_3V3 供电，通过 I2C 和 TPS_PWRUP/WAKEUP 控制生成 EPD_VNEG、EPD_VPOS、EPD_VEE、EPD_VDDH、EPD_VCOM，并输出 PWR_GOOD/INT。

- 参数与网络：`pmic=U7 TPS65185`；`inputs=VEPD_5V,VEPD_3V3`；`controls=TPS_PWRUP,TPS_WAKEUP,I2C`；`outputs=VNEG,VPOS,VEE,VDDH,VCOM`；`status=TPS_PG,TPS_INT`
- 证据：图 69bd3e2f206a / 第 1 页 / 第5页 U7 与全部高压生成网络

### 系统充电与 5V/3.3V

U9 SLM6600 以 VUSB_VIN 为输入给 VBAT_IN 充电；D9/D12 将 VBAT/VUSB_VIN 汇合为 VSYS；U8 SY7088 生成 VBUS_5V，U17 SY8003 再生成 VCC_3V3。

- 参数与网络：`charger=U9 SLM6600`；`battery=VBAT_IN`；`system_or=D9/D12 DSK34 -> VSYS`；`boost=U8 SY7088 -> VBUS_5V`；`buck=U17 SY8003 -> VCC_3V3`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6页 U8/U9/U17/D9/D12

### 外设与 EPD 5V 开关

EXT_PWR_EN 控制 FET5/FET3 将 VBUS_5V 接到 VEXT_5V；EPD_PWR_EN 控制 FET6/FET4 将 VBUS_5V 接到 VEPD_5V。

- 参数与网络：`external=EXT_PWR_EN -> VEXT_5V`；`epd=EPD_PWR_EN -> VEPD_5V`；`fets=FET3-FET6 CJ3134KW/SE7401U`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6页 D1-D3 load switch 区

## 接口

### IT8951E 到 EPD 面板

IT8951E U5B 输出 EPD1_D0-D7、X_LATCH、X_ST、X_OE、Y_ST、Y_CLK 和 SDCLK_EPD 到 J1 EPD_ED047TC1，并连接 VNEG/VPOS/VCOM/VDDH/VEE 高压轨。

- 参数与网络：`data=EPD1_D0-D7`；`timing=X_LATCH,X_ST,X_OE,Y_ST,Y_CLK,SDCLK_EPD`；`panel=J1 EPD_ED047TC1`；`rails=EPD_VNEG,EPD_VPOS,EPD_VCOM,EPD_VDDH,EPD_VEE`
- 证据：图 90ad5fabab87 / 第 1 页 / 第4页 U5B/U5D/J1

### USB Type-C 与 CP2104

J3 USB Type-C 提供 USB_D_P/N 与 VUSB_VIN，U12 SRV05-4 保护数据线；U14 CP2104 将 USB 转为 ESP32 U0RXD/U0TXD，并通过 DTR/RTS 晶体管网络控制 EN/GPIO0。

- 参数与网络：`usb=J3 USB-TYPEC`；`bridge=U14 CP2104`；`tx=CP_TXD -> ESP32_U0RXD via R56 47R`；`rx=CP_RXD -> ESP32_U0TXD via R57 47R`；`auto_boot=CP_DTR/CP_RTS -> VT1/VT2 -> EN/GPIO0`
- 证据：图 c85e5e48676f / 第 1 页 / 第7页 A2-A3 USB 与 B3-C4 CP2104

### 三组 Grove 接口

J5 引出 GPIO32/GPIO25/VEXT_5V/GND，J6 引出 GPIO33/GPIO26/VEXT_5V/GND，J7 引出 GPIO19/GPIO18/VEXT_5V/GND；各信号经 47Ω 与 SRV05-4 保护。

- 参数与网络：`J5=GPIO32,GPIO25,VEXT_5V,GND`；`J6=GPIO33,GPIO26,VEXT_5V,GND`；`J7=GPIO19,GPIO18,VEXT_5V,GND`；`protection=U13/U15/U16 SRV05-4`
- 证据：图 c85e5e48676f / 第 1 页 / 第7页 B1-C2 J5-J7/U13/U15/U16

## 总线

### 内部 I2C

ESP32 GPIO21=I2C_SDA、GPIO22=I2C_SCL，连接 FM24C02、SHT30、PCF8563、TPS65185 和触摸接口；R88/R89 2KΩ 上拉到 VCC_3V3。

- 参数与网络：`sda=GPIO21`；`scl=GPIO22`；`pullups=R88/R89 2KΩ`；`devices=FM24C02,SHT30,PCF8563,TPS65185,touch`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 U1/U2/U22/R88/R89; 图 69bd3e2f206a / 第 1 页 / 第5页 U7 I2C; 图 8e0e8eeb66e9 / 第 1 页 / 第6页 U23 I2C

### ESP32 到 IT8951E SPI

ESP32 GPIO14 经 R10 200Ω 为 IT_SPI_SCK，GPIO12 为 IT_SPI_MOSI，GPIO13 为 IT_SPI_MISO，GPIO15 为 IT_SPI_CS，GPIO27 为 IT_SPI_HRDY。

- 参数与网络：`controller=ESP32`；`device=IT8951E-64`；`sck=GPIO14`；`mosi=GPIO12`；`miso=GPIO13`；`cs=GPIO15`；`hrdy=GPIO27`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 U1 IT_SPI networks; 图 f320feda5dae / 第 1 页 / 第2页 U5C IT_SPI pins

## GPIO 与控制信号

### 拨轮开关

J2 KEY_LEFT/KEY_PUSH/KEY_RIGHT 分别连接 ESP32 GPIO39/GPIO38/GPIO37，各由 R41/R43/R42 10K 上拉到 VCC_3V3，公共端接 GND。

- 参数与网络：`left=GPIO39`；`push=GPIO38`；`right=GPIO37`；`pullups=R41-R43 10K`；`active=low`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 U1 KEY networks; 图 c85e5e48676f / 第 1 页 / 第7页 A1 J2/R41-R43

## 时钟

### PCF8563 RTC 时钟

U23 PCF8563 OSCI/OSCO 连接 Y1 32.768K/6pF 与 C124/C125 6pF，INT 输出 RTC_ALM，SDA/SCL 接内部 I2C。

- 参数与网络：`rtc=U23 PCF8563`；`crystal=Y1 32.768K/6pF`；`loads=C124/C125 6pF`；`interrupt=RTC_ALM`
- 证据：图 8e0e8eeb66e9 / 第 1 页 / 第6页 C4-D4 U23/Y1

## 保护电路

### USB 与 Grove 保护

U12 SRV05-4 保护 USB_D_P/N；U13/U15/U16 SRV05-4 保护三组 Grove GPIO 与 VEXT_5V，GPIO 串联 R45-R55 47Ω。

- 参数与网络：`usb=U12 SRV05-4`；`grove=U13/U15/U16 SRV05-4`；`series=R45-R55 47Ω`
- 证据：图 c85e5e48676f / 第 1 页 / 第7页 U12/U13/U15/U16

## 存储

### FM24C02 EEPROM

U2 FM24C02B-DN-T-G 的 A0/A1/A2 接地，SDA/SCL 接 I2C_SDA/I2C_SCL，VCC 接 VCC_3V3。

- 参数与网络：`device=FM24C02B-DN-T-G`；`address_straps=A0=A1=A2=GND`；`sda=GPIO21/I2C_SDA`；`scl=GPIO22/I2C_SCL`；`supply=VCC_3V3`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 A4 U2

### microSD SPI

U21 卡座使用 SD_CS=GPIO4、IT_SPI_MOSI=GPIO12、SD_SCK=GPIO14、IT_SPI_MISO=GPIO13，CARD_CD 由 R84 10K 上拉。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO12`；`sck=GPIO14`；`miso=GPIO13`；`card_detect=CARD_CD / R84 10K`
- 证据：图 c85e5e48676f / 第 1 页 / 第7页 A4 U21

## 内存与 Flash

### 主控 Flash 与 PSRAM

U4 W25Q128 连接 ESP32 SD_CMD/SD_CLK/SD_DATA0/SD_DATA1，U3 ESPPSRAM64H 连接 SD_DATA0-3、PSRAM_CS/CLK；两者由 VDD_SDIO 供电。

- 参数与网络：`flash=U4 W25Q128`；`flash_capacity=128Mbit part marking`；`psram=U3 ESPPSRAM64H`；`psram_capacity=64Mbit part marking`；`supply=VDD_SDIO`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 C2-D2 U3/U4

## 传感器

### SHT30 温湿度传感器

U22 SHT30 SDA/SCL 接内部 I2C，ADDR pin2 接 GND，VDD 接 VCC_3V3，ALERT/NRST 未连接。

- 参数与网络：`device=U22 SHT30`；`address_strap=ADDR GND`；`sda=I2C_SDA`；`scl=I2C_SCL`；`supply=VCC_3V3`
- 证据：图 1442b3537acb / 第 1 页 / 第1页 B4 U22

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Paper Comm Edition 架构 | `mcu=U1 ESP32`；`flash=W25Q128`；`psram=ESPPSRAM64H`；`epd_controller=IT8951E-64`；`panel=EPD_ED047TC1`；`power=SLM6600/SY7088/SY8003/TPS65185` |
| 内存与 Flash | 主控 Flash 与 PSRAM | `flash=U4 W25Q128`；`flash_capacity=128Mbit part marking`；`psram=U3 ESPPSRAM64H`；`psram_capacity=64Mbit part marking`；`supply=VDD_SDIO` |
| 存储 | FM24C02 EEPROM | `device=FM24C02B-DN-T-G`；`address_straps=A0=A1=A2=GND`；`sda=GPIO21/I2C_SDA`；`scl=GPIO22/I2C_SCL`；`supply=VCC_3V3` |
| 总线 | 内部 I2C | `sda=GPIO21`；`scl=GPIO22`；`pullups=R88/R89 2KΩ`；`devices=FM24C02,SHT30,PCF8563,TPS65185,touch` |
| 传感器 | SHT30 温湿度传感器 | `device=U22 SHT30`；`address_strap=ADDR GND`；`sda=I2C_SDA`；`scl=I2C_SCL`；`supply=VCC_3V3` |
| 总线 | ESP32 到 IT8951E SPI | `controller=ESP32`；`device=IT8951E-64`；`sck=GPIO14`；`mosi=GPIO12`；`miso=GPIO13`；`cs=GPIO15`；`hrdy=GPIO27` |
| 核心器件 | IT8951E 专用 Flash 与时钟 | `controller=U5 IT8951E-64`；`flash=U6 W25Q32`；`crystal=X2 12MHz/20ppm`；`loads=C45/C46 18pF` |
| 接口 | IT8951E 到 EPD 面板 | `data=EPD1_D0-D7`；`timing=X_LATCH,X_ST,X_OE,Y_ST,Y_CLK,SDCLK_EPD`；`panel=J1 EPD_ED047TC1`；`rails=EPD_VNEG,EPD_VPOS,EPD_VCOM,EPD_VDDH,EPD_VEE` |
| 电源 | 电子纸 1.8V/3.3V 电源 | `u18=VEPD_5V -> VEPD_1V8`；`u19=VEPD_5V -> VEPD_3V3`；`filters=FB1-FB4 600R/FB`；`reset=U20 SGM803 -> IT_RST#` |
| 电源 | TPS65185 EPD 高压电源 | `pmic=U7 TPS65185`；`inputs=VEPD_5V,VEPD_3V3`；`controls=TPS_PWRUP,TPS_WAKEUP,I2C`；`outputs=VNEG,VPOS,VEE,VDDH,VCOM`；`status=TPS_PG,TPS_INT` |
| 电源 | 系统充电与 5V/3.3V | `charger=U9 SLM6600`；`battery=VBAT_IN`；`system_or=D9/D12 DSK34 -> VSYS`；`boost=U8 SY7088 -> VBUS_5V`；`buck=U17 SY8003 -> VCC_3V3` |
| 电源 | 外设与 EPD 5V 开关 | `external=EXT_PWR_EN -> VEXT_5V`；`epd=EPD_PWR_EN -> VEPD_5V`；`fets=FET3-FET6 CJ3134KW/SE7401U` |
| 时钟 | PCF8563 RTC 时钟 | `rtc=U23 PCF8563`；`crystal=Y1 32.768K/6pF`；`loads=C124/C125 6pF`；`interrupt=RTC_ALM` |
| 存储 | microSD SPI | `cs=GPIO4`；`mosi=GPIO12`；`sck=GPIO14`；`miso=GPIO13`；`card_detect=CARD_CD / R84 10K` |
| 接口 | USB Type-C 与 CP2104 | `usb=J3 USB-TYPEC`；`bridge=U14 CP2104`；`tx=CP_TXD -> ESP32_U0RXD via R56 47R`；`rx=CP_RXD -> ESP32_U0TXD via R57 47R`；`auto_boot=CP_DTR/CP_RTS -> VT1/VT2 -> EN/GPIO0` |
| 接口 | 三组 Grove 接口 | `J5=GPIO32,GPIO25,VEXT_5V,GND`；`J6=GPIO33,GPIO26,VEXT_5V,GND`；`J7=GPIO19,GPIO18,VEXT_5V,GND`；`protection=U13/U15/U16 SRV05-4` |
| GPIO 与控制信号 | 拨轮开关 | `left=GPIO39`；`push=GPIO38`；`right=GPIO37`；`pullups=R41-R43 10K`；`active=low` |
| 总线地址 | I2C 地址可见性 | `devices=GT911,SHT30,PCF8563/BM8563,FM24C02,TPS65185`；`numeric_addresses_shown=false` |
| 核心器件 | 电子纸与触摸规格 | `schematic_panel=EPD_ED047TC1`；`schematic_controller=IT8951E-64`；`documented_resolution=540x960`；`documented_size=4.7 inch`；`documented_grayscale=16`；`documented_touch=GT911` |
| 电源 | 1150mAh 电池容量 | `documented_capacity=1150mAh`；`documented_voltage=3.7V`；`schematic_capacity_text=false` |
| 保护电路 | USB 与 Grove 保护 | `usb=U12 SRV05-4`；`grove=U13/U15/U16 SRV05-4`；`series=R45-R55 47Ω` |

## 待确认事项

- `address.documented-i2c`：正文将触摸、SHT30、BM8563 和 FM24C02 描述为内部 I2C 设备，但七页原理图未直接打印其数值地址；需按具体器件和绑定位确认。（证据：图 1442b3537acb / 第 1 页 / 第1页 U2/U22 I2C，无地址文字; 图 8e0e8eeb66e9 / 第 1 页 / 第6页 U23，无地址文字）
- `component.documented-panel-touch`：原理图明确面板连接器型号 EPD_ED047TC1 和控制器 IT8951E-64，但未打印 540x960、4.7 inch、16 灰阶或 GT911 型号；这些规格来自正文。（证据：图 90ad5fabab87 / 第 1 页 / 第4页 J1 EPD_ED047TC1; 图 c85e5e48676f / 第 1 页 / 第7页 J11 TOUCH_I2C，无触摸 IC 型号）
- `power.documented-battery`：正文写内置 1150mAh@3.7V 电池，原理图只显示 VBAT/VBAT_IN、J4 电池接口、保险丝与充电路径，没有容量字段。（证据：图 8e0e8eeb66e9 / 第 1 页 / 第6页 VBAT/VBAT_IN 电源路径; 图 c85e5e48676f / 第 1 页 / 第7页 J4 VBAT_UFUSED）
- `review.i2c-addresses`：K049-C 当前触摸、SHT30、RTC、FM24C02 与 TPS65185 的正式 7-bit 地址分别是什么？；原因：七页原理图未直接打印数值地址。
- `review.panel-touch-spec`：K049-C 当前面板是否固定为 540x960、4.7 inch、16 灰阶且触摸 IC 为 GT911？；原因：原理图只确认 EPD_ED047TC1、IT8951E 与触摸接口。
- `review.battery-capacity`：K049-C 当前内置电池容量是否固定为 1150mAh@3.7V？；原因：容量仅出现在正文，原理图未打印。

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

源文档：`zh_CN/core/m5paper_comm.md`

源文档 SHA-256：`1524b4bc60dd2dc72e6dd3b6c51057d07a671e671650df01076a4ea64c5ce369`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
