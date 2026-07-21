# Unit LCD 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LCD |
| SKU | U120 |
| 产品 ID | `unit-lcd-f6d3e8883759` |
| 源文档 | `zh_CN/unit/lcd.md` |

## 概述

Unit LCD 以 U2 ESP32_PICO_D4 为控制核心，通过 J2 的 GPIO22/GPIO21 I2C 接收外部命令，并以 GPIO5/GPIO13/GPIO15/GPIO23/GPIO18 驱动 J3 八针 LCD FPC 的 CS/SCK/MOSI/D-C/RST。U1 SPX3819M5-L-3.3 将 J2 输入的 +5V 稳压为 +3.3V，供 ESP32-PICO、LCD 逻辑与背光使用；Q1 AO3401A 构成 VLED 高边开关，由 GPIO4 控制。J1 DownloadSocket 引出 UART、EN、GPIO0 和电源，EN 配置 10KΩ/100nF RC，GPIO15 由 0Ω 下拉和 10KΩ 上拉形成绑带，LNA_IN 通过 49.9Ω 接 GND且没有天线。产品正文所述 ST7789V2、1.14英寸/135x240/RGB666、I2C 地址 0x3E/400kHz 与绘图固件协议未直接印在原理图上，需结合 LCD 模组资料与固件确认。

## 检索关键词

`Unit LCD`、`U120`、`ESP32_PICO_D4`、`SPX3819M5-L-3.3`、`ST7789V2`、`AO3401A`、`I2C`、`0x3E`、`400kHz`、`GPIO22 SCL`、`GPIO21 SDA`、`GPIO5 LCD CS`、`GPIO13 LCD SCK`、`GPIO15 LCD MOSI`、`GPIO23 LCD D/C`、`GPIO18 LCD RST`、`GPIO4 backlight`、`VLED`、`J3 FPC-0.5-8P`、`J1 DownloadSocket`、`UTX`、`URX`、`EN`、`GPIO0`、`+5V`、`+3.3V`、`VDD_SDIO`、`R5 10KΩ`、`R6 0Ω`、`R4 49.9Ω`、`135x240`、`RGB666`、`262144 colors`、`1.14 inch IPS`、`CHANGE_ADDR`、`M5UnitLCD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ESP32_PICO_D4 | I2C 设备主控、LCD 串行驱动、背光控制和 UART 下载核心 | 图 62838ae14f2f / 第 1 页 / 第 1 页中央 U2 ESP32_PICO_D4 pin1-pin49 |
| U1 | SPX3819M5-L-3.3 | 将 +5V 稳压为 +3.3V 的主电源 LDO | 图 62838ae14f2f / 第 1 页 / 第 1 页左下 U1 SPX3819M5-L-3.3，IN/EN/OUT/GND/BYP |
| J2 | HY-2.0_IIC | 外部 I2C、+5V 和 GND Grove 接口 | 图 62838ae14f2f / 第 1 页 / 第 1 页右上 J2 HY-2.0_IIC pin1-pin4 |
| J3 | FPC-0.5-8P | 引出 CS、VCC、SCK、MOSI、D/C、RST、GND、VLED 的 LCD FPC 接口 | 图 62838ae14f2f / 第 1 页 / 第 1 页右下 J3 FPC-0.5-8P pin1-pin8 |
| J1 | DownloadSocket | ESP32-PICO 的 3.3V、UART、EN、GPIO0、GND 下载接口 | 图 62838ae14f2f / 第 1 页 / 第 1 页右上 J1 DownloadSocket pin1-pin6 |
| Q1 | AO3401A | 由 GPIO4 控制的 LCD VLED 高边 P 沟道 MOSFET 开关 | 图 62838ae14f2f / 第 1 页 / 第 1 页右下 Q1 AO3401A 与 GPIO4/VLED/+3.3V |
| R2/R3 | 4.7KΩ | GPIO22 SCL 与 GPIO21 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 62838ae14f2f / 第 1 页 / 第 1 页右上 R2/R3 4.7KΩ 与 J2 SCL/SDA |
| R7/R8/R9 | 10Ω / 10Ω / 51KΩ | VLED 串联限流、GPIO4 栅极串联和 Q1 栅极到 +3.3V 上拉网络 | 图 62838ae14f2f / 第 1 页 / 第 1 页右下 R7/R8/R9 与 Q1/J3 VLED |
| R1/C3 | 10KΩ / 100nF | ESP32-PICO EN 的 +3.3V 上拉和对地复位延时网络 | 图 62838ae14f2f / 第 1 页 / 第 1 页左中 R1 10KΩ/C3 100nF 与 U2 EN |
| R5/R6 | 10KΩ / 0Ω | GPIO15 到 +3.3V/GND 的启动绑带电阻网络 | 图 62838ae14f2f / 第 1 页 / 第 1 页 U2 右下 GPIO15、R5 10KΩ 至 +3.3V、R6 0Ω 至 GND |
| R4 | 49.9Ω (49R9) ±1% | ESP32-PICO LNA_IN 到 GND 的射频终端电阻 | 图 62838ae14f2f / 第 1 页 / 第 1 页 U2 右上 LNA_IN 与 R4 49.9Ω/GND |
| C1/C2/C4-C9 | 22uF / 22uF / 1uF / 10uF / 10uF / 100nF / 100nF / 1uF | +5V、+3.3V、VDD_SDIO 和 LCD VCC 的滤波与去耦电容 | 图 62838ae14f2f / 第 1 页 / 第 1 页下部 C1/C2/C5-C9 与右侧 C4 |

## 系统结构

### Unit LCD 系统结构

U2 ESP32_PICO_D4 通过 J2 I2C 接收外部命令，以五路控制/数据网驱动 J3 LCD FPC，并通过 Q1 控制 VLED；U1 从 +5V 生成整板 +3.3V。

- 参数与网络：`controller=U2 ESP32_PICO_D4`；`host_interface=J2 I2C`；`display_interface=J3 FPC-0.5-8P`；`backlight_switch=Q1 AO3401A`；`regulator=U1 SPX3819M5-L-3.3`；`download=J1 DownloadSocket`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页完整原理图全部功能区

## 核心器件

### U2 ESP32_PICO_D4 关键 GPIO

U2 IO22=GPIO22/I2C SCL、IO21=GPIO21/I2C SDA、IO23=GPIO23 LCD D/C、IO18=GPIO18 LCD RST、IO5=GPIO5 LCD CS、IO4=GPIO4 背光控制、IO13=GPIO13 LCD SCK、IO15=GPIO15 LCD MOSI/绑带、IO0=GPIO0 下载启动。

- 参数与网络：`GPIO22=J2 SCL`；`GPIO21=J2 SDA`；`GPIO23=J3 D/C`；`GPIO18=J3 RST`；`GPIO5=J3 CS`；`GPIO4=Q1 backlight gate`；`GPIO13=J3 SCK`；`GPIO15=J3 MOSI and R5/R6 strap`；`GPIO0=J1 G0`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 U2 左右 GPIO 网络及 J1/J2/J3/Q1

## 电源

### U1 SPX3819M5-L-3.3

U1 IN pin1 与 EN pin3 接 +5V，OUT pin5 输出 +3.3V，GND pin2 接地，BYP/ADJ pin4 未外接；C1/C2 各 22uF 位于输入/输出。

- 参数与网络：`input=+5V at pin1`；`enable=+5V at pin3`；`output=+3.3V at pin5`；`ground=pin2 GND`；`bypass_adjust=pin4 no visible connection`；`input_cap=C1 22uF`；`output_cap=C2 22uF`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页左下 U1/C1/C2 与 +5V/+3.3V

### +3.3V 与 VDD_SDIO 去耦

C5/C6 各 10uF、C7/C8 各 100nF 跨接 +3.3V 与 GND，C9 1uF 跨接 VDD_SDIO 与 GND；J3 VCC 另由 C4 1uF 去耦。

- 参数与网络：`3v3_caps=C5 10uF,C6 10uF,C7 100nF,C8 100nF`；`vdd_sdio_cap=C9 1uF`；`lcd_vcc_cap=C4 1uF`；`return=GND`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页下部 C5-C9 与右侧 J3/C4

## 接口

### J2 HY-2.0_IIC

J2 pin1=IIC_SCL/GPIO22、pin2=IIC_SDA/GPIO21、pin3=VCC/+5V、pin4=GND；+5V 是 U1 输入电源。

- 参数与网络：`pin_1=IIC_SCL / GPIO22`；`pin_2=IIC_SDA / GPIO21`；`pin_3=+5V / power input`；`pin_4=GND`；`power_destination=U1 IN/EN`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页右上 J2 pin1-pin4 与 GPIO22/GPIO21/+5V

### J3 FPC-0.5-8P

J3 pin1=CS/GPIO5、pin2=VCC/+3.3V、pin3=SCK/GPIO13、pin4=MOSI/GPIO15、pin5=D/C/GPIO23、pin6=RST/GPIO18、pin7=GND、pin8=VLED。

- 参数与网络：`pin_1=CS / GPIO5`；`pin_2=+3.3V`；`pin_3=SCK / GPIO13`；`pin_4=MOSI / GPIO15`；`pin_5=D/C / GPIO23`；`pin_6=RST / GPIO18`；`pin_7=GND`；`pin_8=VLED`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页右下 J3 pin1-pin8 与 GPIO 标签

## 总线

### 外部主机 I2C 总线

外部主机通过 J2 SCL/SDA 直接连接 U2 GPIO22/GPIO21，R2/R3 各 4.7KΩ 将 SCL/SDA 上拉到 +3.3V；U2 固件为 I2C 设备端。

- 参数与网络：`controller=external host`；`device=U2 ESP32-PICO firmware`；`scl=J2.1 GPIO22,R2 4.7KΩ to +3.3V`；`sda=J2.2 GPIO21,R3 4.7KΩ to +3.3V`；`logic_rail=+3.3V`；`level_shifter_shown=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 J2/R2/R3 与 U2 GPIO22/GPIO21

### ESP32-PICO 到 LCD 串行总线

U2 GPIO5/GPIO13/GPIO15 分别连接 J3 CS/SCK/MOSI，GPIO23 连接 D/C，GPIO18 连接 RST；图中没有 LCD MISO 返回线。

- 参数与网络：`controller=U2 ESP32_PICO_D4`；`chip_select=GPIO5 -> J3.1 CS`；`clock=GPIO13 -> J3.3 SCK`；`data=GPIO15 -> J3.4 MOSI`；`data_command=GPIO23 -> J3.5 D/C`；`reset=GPIO18 -> J3.6 RST`；`miso_shown=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 U2 GPIO5/13/15/23/18 与 J3

## GPIO 与控制信号

### GPIO4/Q1 VLED 控制

GPIO4 经 R8 10Ω 连接 Q1 栅极，R9 51KΩ 将栅极上拉到 +3.3V；Q1 源极接 +3.3V、漏极经 R7 10Ω 供 J3 VLED，构成默认关断的 P 沟道高边开关。

- 参数与网络：`control=GPIO4 via R8 10Ω`；`gate_pullup=R9 51KΩ to +3.3V`；`switch=Q1 AO3401A P-channel`；`source=+3.3V`；`output=Q1 drain -> R7 10Ω -> J3 pin8 VLED`；`default_state=off with gate pulled high`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页右下 GPIO4/R8/R9/Q1/R7/VLED

### GPIO0 与 GPIO15 启动配置

GPIO0 直接引到 J1 G0 pin5；GPIO15 同时作为 LCD MOSI，并由 R5 10KΩ 接 +3.3V、R6 0Ω 接 GND，按图示阻值由 0Ω 路径固定为低电平。

- 参数与网络：`GPIO0=J1 pin5 G0`；`GPIO15_function=J3 MOSI`；`GPIO15_pullup=R5 10KΩ to +3.3V`；`GPIO15_pulldown=R6 0Ω to GND`；`shown_gpio15_state=low`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 U2 GPIO0/GPIO15、J1 G0、J3 MOSI、R5/R6

## 时钟

### 外部时钟

完整原理图未显示外部晶振、振荡器或时钟网络；ESP32_PICO_D4 封装内部时钟结构未展开。

- 参数与网络：`external_crystal_shown=false`；`external_oscillator_shown=false`；`clock_net_shown=false`；`package_internal_clock_expanded=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页完整图无外部时钟器件

## 复位

### U2 EN

U2 EN 由 R1 10KΩ 上拉到 +3.3V，并由 C3 100nF 对地；EN 同时引到 J1 pin4，图中没有独立复位按键。

- 参数与网络：`mcu_pin=U2 EN`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C3 100nF to GND`；`download_pin=J1 pin4`；`reset_switch_shown=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页左中 R1/C3/EN 与右上 J1 EN

## 保护电路

### J1/J2/J3 接口保护

完整原理图未显示 TVS、ESD 阵列、保险丝或反接保护；I2C 与 LCD 信号直接连接 U2，背光路径仅有 R7/R8 串联电阻和 Q1。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_signal_protection_shown=false`；`lcd_signal_protection_shown=false`；`backlight_series=R7/R8 10Ω`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 J1/J2/J3 至 U2/U1/Q1 全部路径

## 关键网络

### I2C 主机到 LCD 路径

关键路径为 J2 GPIO22/GPIO21→U2 I2C 固件→GPIO5/13/15/23/18→J3 CS/SCK/MOSI/D-C/RST，背光路径为 GPIO4→Q1→R7→J3 VLED，电源为 +5V→U1→+3.3V。

- 参数与网络：`host_path=J2 SCL/SDA->U2 GPIO22/GPIO21`；`display_path=U2 GPIO5/13/15/23/18->J3`；`backlight_path=U2 GPIO4->Q1->R7->J3 VLED`；`power_path=J2 +5V->U1->+3.3V`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页完整 J2/U2/J3/Q1/U1 路径

## 内存与 Flash

### 存储器

完整原理图未显示外部 Flash、PSRAM、EEPROM、RAM 或 SD 卡；ESP32_PICO_D4 封装内部存储容量未在页面标注。

- 参数与网络：`external_flash_shown=false`；`external_psram_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`package_capacity_printed=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页完整图无外部存储器件

## 射频

### ESP32-PICO LNA_IN

U2 LNA_IN 经 R4 49.9Ω ±1% 接 GND，完整原理图未显示天线、匹配网络或 RF 连接器。

- 参数与网络：`rf_pin=U2 LNA_IN`；`termination=R4 49.9Ω to GND`；`antenna_shown=false`；`matching_network_shown=false`；`rf_connector_shown=false`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页 U2 右上 LNA_IN/R4/GND 与完整图

## 调试与烧录

### J1 DownloadSocket

J1 pin1=+3.3V、pin2=TXD/UTX、pin3=RXD/URX、pin4=EN、pin5=G0/GPIO0、pin6=GND；UTX/URX 连接 U2 U0TXD/U0RXD。

- 参数与网络：`pin_1=+3.3V`；`pin_2=TXD / UTX / U2 U0TXD`；`pin_3=RXD / URX / U2 U0RXD`；`pin_4=EN`；`pin_5=G0 / GPIO0`；`pin_6=GND`
- 证据：图 62838ae14f2f / 第 1 页 / 第 1 页右上 J1 DownloadSocket 与 U2 UTX/URX/EN/GPIO0

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit LCD 系统结构 | `controller=U2 ESP32_PICO_D4`；`host_interface=J2 I2C`；`display_interface=J3 FPC-0.5-8P`；`backlight_switch=Q1 AO3401A`；`regulator=U1 SPX3819M5-L-3.3`；`download=J1 DownloadSocket` |
| 核心器件 | U2 ESP32_PICO_D4 关键 GPIO | `GPIO22=J2 SCL`；`GPIO21=J2 SDA`；`GPIO23=J3 D/C`；`GPIO18=J3 RST`；`GPIO5=J3 CS`；`GPIO4=Q1 backlight gate`；`GPIO13=J3 SCK`；`GPIO15=J3 MOSI and R5/R6 strap`；`GPIO0=J1 G0` |
| 接口 | J2 HY-2.0_IIC | `pin_1=IIC_SCL / GPIO22`；`pin_2=IIC_SDA / GPIO21`；`pin_3=+5V / power input`；`pin_4=GND`；`power_destination=U1 IN/EN` |
| 总线 | 外部主机 I2C 总线 | `controller=external host`；`device=U2 ESP32-PICO firmware`；`scl=J2.1 GPIO22,R2 4.7KΩ to +3.3V`；`sda=J2.2 GPIO21,R3 4.7KΩ to +3.3V`；`logic_rail=+3.3V`；`level_shifter_shown=false` |
| 总线地址 | Unit LCD I2C 地址 | `documented_initial_address=0x3E`；`address_width=7-bit`；`documented_change_command=CHANGE_ADDR 0xA0`；`address_printed_on_schematic=false`；`address_strap_shown=false` |
| 接口 | J3 FPC-0.5-8P | `pin_1=CS / GPIO5`；`pin_2=+3.3V`；`pin_3=SCK / GPIO13`；`pin_4=MOSI / GPIO15`；`pin_5=D/C / GPIO23`；`pin_6=RST / GPIO18`；`pin_7=GND`；`pin_8=VLED` |
| 总线 | ESP32-PICO 到 LCD 串行总线 | `controller=U2 ESP32_PICO_D4`；`chip_select=GPIO5 -> J3.1 CS`；`clock=GPIO13 -> J3.3 SCK`；`data=GPIO15 -> J3.4 MOSI`；`data_command=GPIO23 -> J3.5 D/C`；`reset=GPIO18 -> J3.6 RST`；`miso_shown=false` |
| GPIO 与控制信号 | GPIO4/Q1 VLED 控制 | `control=GPIO4 via R8 10Ω`；`gate_pullup=R9 51KΩ to +3.3V`；`switch=Q1 AO3401A P-channel`；`source=+3.3V`；`output=Q1 drain -> R7 10Ω -> J3 pin8 VLED`；`default_state=off with gate pulled high` |
| 电源 | U1 SPX3819M5-L-3.3 | `input=+5V at pin1`；`enable=+5V at pin3`；`output=+3.3V at pin5`；`ground=pin2 GND`；`bypass_adjust=pin4 no visible connection`；`input_cap=C1 22uF`；`output_cap=C2 22uF` |
| 电源 | +3.3V 与 VDD_SDIO 去耦 | `3v3_caps=C5 10uF,C6 10uF,C7 100nF,C8 100nF`；`vdd_sdio_cap=C9 1uF`；`lcd_vcc_cap=C4 1uF`；`return=GND` |
| 调试与烧录 | J1 DownloadSocket | `pin_1=+3.3V`；`pin_2=TXD / UTX / U2 U0TXD`；`pin_3=RXD / URX / U2 U0RXD`；`pin_4=EN`；`pin_5=G0 / GPIO0`；`pin_6=GND` |
| 复位 | U2 EN | `mcu_pin=U2 EN`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C3 100nF to GND`；`download_pin=J1 pin4`；`reset_switch_shown=false` |
| GPIO 与控制信号 | GPIO0 与 GPIO15 启动配置 | `GPIO0=J1 pin5 G0`；`GPIO15_function=J3 MOSI`；`GPIO15_pullup=R5 10KΩ to +3.3V`；`GPIO15_pulldown=R6 0Ω to GND`；`shown_gpio15_state=low` |
| 射频 | ESP32-PICO LNA_IN | `rf_pin=U2 LNA_IN`；`termination=R4 49.9Ω to GND`；`antenna_shown=false`；`matching_network_shown=false`；`rf_connector_shown=false` |
| 时钟 | 外部时钟 | `external_crystal_shown=false`；`external_oscillator_shown=false`；`clock_net_shown=false`；`package_internal_clock_expanded=false` |
| 其他事实 | LCD 型号与显示规格 | `documented_controller=ST7789V2`；`documented_size=1.14 inch`；`documented_resolution=135x240`；`documented_panel=IPS`；`documented_output_color=RGB666 / 262144 colors`；`specs_printed_on_schematic=false` |
| 其他事实 | I2C 最大速率 | `documented_max_speed=400kHz`；`pullups=R2/R3 4.7KΩ`；`speed_printed_on_schematic=false` |
| 其他事实 | Unit LCD 绘图与读取命令协议 | `documented_commands=FILLRECT,WRITE_RAW,WRITE_RLE,READ_ID,READ_BUFCOUNT,CHANGE_ADDR`；`firmware_endpoint=U2 ESP32_PICO_D4`；`protocol_visible_on_schematic=false`；`firmware_version_printed=false` |
| 关键网络 | I2C 主机到 LCD 路径 | `host_path=J2 SCL/SDA->U2 GPIO22/GPIO21`；`display_path=U2 GPIO5/13/15/23/18->J3`；`backlight_path=U2 GPIO4->Q1->R7->J3 VLED`；`power_path=J2 +5V->U1->+3.3V` |
| 保护电路 | J1/J2/J3 接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_signal_protection_shown=false`；`lcd_signal_protection_shown=false`；`backlight_series=R7/R8 10Ω` |
| 内存与 Flash | 存储器 | `external_flash_shown=false`；`external_psram_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`package_capacity_printed=false` |

## 待确认事项

- `address.documented-0x3e`：产品正文列出初始 7 位地址 0x3E 并称可由 CHANGE_ADDR 修改；原理图只显示 I2C 进入 U2，没有打印固件地址或硬件地址绑带。（证据：图 62838ae14f2f / 第 1 页 / 第 1 页 J2 I2C 至 U2 GPIO22/GPIO21，页面无地址标注）
- `other.documented-display-specs`：产品正文描述 ST7789V2、1.14英寸、135x240、RGB666/262144色 IPS 面板；原理图仅显示 J3 FPC-0.5-8P，没有打印 LCD 控制器型号、分辨率、尺寸或色深。（证据：图 62838ae14f2f / 第 1 页 / 第 1 页 J3 FPC-0.5-8P，无 LCD 型号或像素参数）
- `other.documented-i2c-speed`：产品正文声明 I2C 最大通信速度 400kHz；原理图显示 4.7KΩ 上拉和 ESP32-PICO 连接，但没有打印总线速率或时序限制。（证据：图 62838ae14f2f / 第 1 页 / 第 1 页 J2/R2/R3/U2 I2C 路径，无速率标注）
- `other.documented-firmware-protocol`：产品正文列出 FILLRECT、WRITE_RAW/RLE、READ_ID、READ_BUFCOUNT、CHANGE_ADDR 等固件命令和帧缓冲行为；这些寄存器/命令语义不在原理图中，需依据对应固件版本确认。（证据：图 62838ae14f2f / 第 1 页 / 第 1 页 U2/J2/J3 硬件连接，无固件命令标注）
- `review.i2c-address`：请依据 Unit LCD 固件或 I2C 扫描确认初始 7 位地址 0x3E 及 CHANGE_ADDR 行为。；原因：原理图未打印固件地址或地址修改逻辑。
- `review.display-specs`：请依据 LCD FPC 模组资料或实物确认 ST7789V2、1.14英寸、135x240、IPS 与 RGB666 参数。；原因：原理图只显示八针 FPC 接口，没有面板型号和显示参数。
- `review.i2c-speed`：请依据固件配置和总线实测确认 I2C 最大速度为 400kHz。；原因：原理图没有标注 I2C 时序或速率。
- `review.firmware-protocol`：请依据 M5UnitLCD_FirmWare 对应版本确认绘图、读取、RLE、缓冲区和地址修改命令。；原因：固件命令协议无法由原理图确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `62838ae14f2f8cc3e95663e7b8fd7d507c8620dcf50c51f2a2fbf0f55709e183` | `https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_sch_01.webp` |

---

源文档：`zh_CN/unit/lcd.md`

源文档 SHA-256：`5638f1e96974e868fcab7963eed8983544bf90630e24eccbcf12fb9507f915ac`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
