# Stamp-S3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3 |
| SKU | S007 |
| 产品 ID | `stamp-s3-07ce7ee8d7e0` |
| 源文档 | `zh_CN/core/StampS3.md` |

## 概述

Stamp-S3 以 ESP32-S3FN8 为主控，配置 40MHz 晶体、PROANT440 板载天线、WS2812 RGB LED 和 GPIO0 用户/下载按键。USB Type-C 提供原生 USB D+/D- 与 VIN_5V，MUN3CAD01-SC 将 VIN_5V 转换为 VDD_3V3。STAMP-S3M 焊盘模块引出 23 路 GPIO、EN、UART TX/RX、5V、3.3V 和 GND；背面还提供由 GPIO33-GPIO38 驱动的 8 针 SPI 显示接口，并预留标注 NC 的 12 针替代接口。

## 检索关键词

`Stamp-S3`、`S007`、`ESP32-S3FN8`、`STAMP-S3M`、`MUN3CAD01-SC`、`SGM2578`、`WS4622C-4/TR`、`WS2812`、`PROANT440`、`40MHz`、`USB Type-C`、`USB_DU_P`、`USB_DU_N`、`VIN_5V`、`VDD_3V3`、`ESP_EN`、`GPIO0`、`GPIO21`、`GPIO33`、`GPIO34`、`GPIO35`、`GPIO36`、`GPIO37`、`GPIO38`、`GPIO43 TX`、`GPIO44 RX`、`GPIO46`、`SK_DIN`、`DISP_RST`、`DISP_RS`、`DISP_MOSI`、`DISP_SCK`、`DISP_CS`、`DISP_BL`、`PESDNC2FD3V3B`、`M5StampS3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | Stamp-S3 主控 SoC | 图 aaa7dbf40110 / 第 1 页 / 网格 2A-C，U1 ESP32-S3FN8 及全部电源、时钟、USB、GPIO 和 UART 网络 |
| M1 | STAMP-S3M | 28 焊盘 Stamp-S3 模组外部接口定义 | 图 aaa7dbf40110 / 第 1 页 / 网格 3C-4C，M1 STAMP-S3M pin1-pin28 的 GPIO、电源、EN、TX、RX 和 GND |
| M2 | MUN3CAD01-SC | VIN_5V 到 VDD_3V3 的 DC-DC 电源模块 | 图 aaa7dbf40110 / 第 1 页 / 网格 2D，M2 MUN3CAD01-SC、VIN_5V、VDD_3V3、EN 和反馈分压 |
| ANT1 | PROANT440 | 板载 2.4GHz 射频天线 | 图 aaa7dbf40110 / 第 1 页 / 网格 1A，ANT1 PROANT440 经 L1/C1/C2 匹配网络连接 ESP_LNA |
| X1 | 40MHz | ESP32-S3 主时钟晶体 | 图 aaa7dbf40110 / 第 1 页 / 网格 1B，X1 40MHz、L3、C9、C14 与 XTAL_40M_P/N |
| U3 | WS2812 | 可编程 RGB 状态 LED | 图 aaa7dbf40110 / 第 1 页 / 网格 3B-4B，U3 WS2812，DI=SK_DIN、DO=SK_DOUT、VDD=VDD_3V3 |
| S1 | SMT_SW_1TS026A | GPIO0 用户键和启动模式按键 | 图 aaa7dbf40110 / 第 1 页 / 网格 3C，S1 将 GPIO0 接地，R4 10kΩ 上拉并由 D1 防护 |
| U2 | SGM2578 / WS4622C-4/TR | 显示背光 3.3V 负载开关 | 图 aaa7dbf40110 / 第 1 页 / 网格 3A，U2 SGM2578/WS4622C-4/TR，VIN=VDD_3V3、EN=DISP_BL、VOUT 接显示背光引脚 |
| J3 | HDGC/0.5K-HX-8PWB | 8 针 SPI 显示 FPC 接口 | 图 aaa7dbf40110 / 第 1 页 / 网格 4A，J3 pin1 背光、pin2 GND、pin3-pin8 为 DISP_RST/RS/MOSI/SCK/VDD_3V3/CS |
| J1 | HDGC/0.5K-HX-12PWB/NC | 标注 NC 的 12 针显示 FPC 替代接口 | 图 aaa7dbf40110 / 第 1 页 / 网格 4A，J1 12 针接口，器件型号末尾明确标注 /NC |
| J2 | USB-TYPEC | USB 2.0 设备接口和 5V 电源入口 | 图 aaa7dbf40110 / 第 1 页 / 网格 4D，J2 USB-TYPEC、DP/DN、CC1/CC2、VBUS、GND 和外壳 |
| F1 | 6V/1A/PPTC | USB VBUS 到 VIN_5V 的自恢复保险丝 | 图 aaa7dbf40110 / 第 1 页 / 网格 4D，F1 6V/1A/PPTC 串联在 JP1/J2 VCC 与 VIN_5V 之间 |
| L5 | 未标注 | USB D+/D- 共模扼流圈 | 图 aaa7dbf40110 / 第 1 页 / 网格 3D，L5 串接 USB_DU_P/N 与 USB_D_P/N 两对差分网络 |
| D3,D4 | PESDNC2FD3V3B | USB D+/D- 静电防护器件 | 图 aaa7dbf40110 / 第 1 页 / 网格 3D，D3 接 USB_D_P、D4 接 USB_D_N，均对地 |
| D1 | PESDNC2FD3V3B | GPIO0 用户键网络静电防护 | 图 aaa7dbf40110 / 第 1 页 / 网格 3C，D1 PESDNC2FD3V3B 从 GPIO0 接地 |

## 系统结构

### ESP32-S3FN8 最小系统

U1 ESP32-S3FN8 连接板载射频、40MHz 晶体、VDD_3V3 电源、原生 USB、RGB LED、GPIO0 按键、SPI 显示接口和 STAMP-S3M 外部焊盘。

- 参数与网络：`reference=U1`；`part_number=ESP32-S3FN8`；`core_supply=VDD_3V3`；`enable_net=ESP_EN`；`rf_net=ESP_LNA`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 1A-2C 的 U1 及网格 3A-4D 的各功能区连接

## 电源

### USB VBUS 到 VIN_5V

J2 USB Type-C 的 VCC 经 JP1 测试点和 F1 6V/1A PPTC 自恢复保险丝连接 VIN_5V，VIN_5V 端由 D14 PESDNC2FD5VB 对地防护。

- 参数与网络：`connector=J2`；`testpoint=JP1`；`fuse=F1 6V/1A/PPTC`；`output_net=VIN_5V`；`protection=D14 PESDNC2FD5VB`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 4D，J2 VCC、JP1、F1、VIN_5V 与 D14

### VDD_3V3 电源转换

M2 MUN3CAD01-SC 以 VIN_5V 为输入并输出 VDD_3V3，反馈分压为 R6 100kΩ 与 R17 22.1kΩ，输出由 C21、C22 各 10uF 去耦。

- 参数与网络：`converter=M2 MUN3CAD01-SC`；`input=VIN_5V`；`output=VDD_3V3`；`feedback=R6 100kΩ, R17 22.1kΩ`；`output_capacitors=C21 10uF, C22 10uF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2D，M2、VIN_5V、VDD_3V3、R6、R17、C21、C22

## 接口

### USB Type-C 连接

J2 DP1/DP2 并接 USB_D_P，DN1/DN2 并接 USB_D_N；CC1 与 CC2 分别通过 R1、R2 5.1kΩ 接地。

- 参数与网络：`connector=J2 USB-TYPEC`；`dp_net=USB_D_P`；`dm_net=USB_D_N`；`cc1_pulldown=R1 5.1kΩ`；`cc2_pulldown=R2 5.1kΩ`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 4D，J2 DP/DN/CC 引脚与 R1/R2

### STAMP-S3M 电源和控制焊盘

M1 pin13 提供 VIN_5V，pin28 提供 VDD_3V3，pin11/pin18 为 GND，pin22 为 EN。

- 参数与网络：`connector=M1 STAMP-S3M`；`five_volt_pin=13`；`three_v_three_pin=28`；`ground_pins=11,18`；`enable_pin=22`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 3C-4C，M1 pin11、13、18、22、28

### STAMP-S3M 外部 GPIO

M1 引出 GPIO0-GPIO15 以及 GPIO39、GPIO40、GPIO41、GPIO42、GPIO43/TX、GPIO44/RX 和 GPIO46，共 23 路 GPIO。

- 参数与网络：`connector=M1 STAMP-S3M`；`gpio_count=23`；`gpio_list=GPIO0, GPIO1, GPIO2, GPIO3, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10, GPIO11, GPIO12, GPIO13, GPIO14, GPIO15, GPIO39, GPIO40, GPIO41, GPIO42, GPIO43, GPIO44, GPIO46`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 3C-4C，M1 左侧 pin1-pin17 与右侧 pin19-pin27 的 GPIO 标注

### J3 八针 SPI 显示接口

J3 pin1 接 U2 背光输出，pin2=GND，pin3=DISP_RST，pin4=DISP_RS，pin5=DISP_MOSI，pin6=DISP_SCK，pin7=VDD_3V3，pin8=DISP_CS。

- 参数与网络：`connector=J3 HDGC/0.5K-HX-8PWB`；`pin1=backlight output`；`pin2=GND`；`pin3=DISP_RST`；`pin4=DISP_RS`；`pin5=DISP_MOSI`；`pin6=DISP_SCK`；`pin7=VDD_3V3`；`pin8=DISP_CS`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 4A，J3 8 针连接器和每个网络标注

### J1 十二针显示接口预留

J1 为标注 /NC 的 12 针替代显示接口，除复用 J3 的背光、DISP_RST/RS/MOSI/SCK/CS、VDD_3V3 和 GND 外，还引出 VIN_5V、GPIO18、GPIO17、GPIO16。

- 参数与网络：`connector=J1 HDGC/0.5K-HX-12PWB/NC`；`assembly=NC`；`extra_signals=VIN_5V, GPIO18, GPIO17, GPIO16`；`shared_display_signals=backlight, DISP_RST, DISP_RS, DISP_MOSI, DISP_SCK, VDD_3V3, DISP_CS`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 4A，J1 pin1-pin12 及器件名末尾 /NC

## 总线

### ESP32-S3 原生 USB 差分链路

U1 GPIO19/GPIO20 分别形成 USB_DU_N/USB_DU_P，经 L5 共模扼流圈转换到连接器侧 USB_D_N/USB_D_P；JP2/JP3 为前级差分测试点。

- 参数与网络：`dm_gpio=19`；`dp_gpio=20`；`soc_nets=USB_DU_N, USB_DU_P`；`connector_nets=USB_D_N, USB_D_P`；`common_mode_choke=L5`；`testpoints=JP2, JP3`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2B U1 GPIO19/20 与网格 3D L5、JP2、JP3、USB_DU_P/N、USB_D_P/N

### UART0 到模组焊盘

U1 U0TXD 经 R5 510Ω 连接 TX，并引到 M1 pin26 G43/Tx；U1 U0RXD 直接连接 RX，并引到 M1 pin24 G44/Rx。

- 参数与网络：`tx_soc=U1 U0TXD`；`tx_net=TX`；`tx_gpio=43`；`tx_module_pin=26`；`tx_series_resistor=R5 510Ω`；`rx_soc=U1 U0RXD`；`rx_net=RX`；`rx_gpio=44`；`rx_module_pin=24`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2C U1 U0TXD/U0RXD、R5、TX/RX 与网格 4C M1 pin24/pin26

## GPIO 与控制信号

### GPIO0 用户与启动按键

S1 按下时将 GPIO0 拉低，R4 10kΩ 将 GPIO0 上拉到 VDD_3V3，D1 PESDNC2FD3V3B 从 GPIO0 对地防护；GPIO0 同时引到 M1 pin20。

- 参数与网络：`switch=S1 SMT_SW_1TS026A`；`net=GPIO0`；`active_level=low`；`pullup=R4 10kΩ`；`protection=D1 PESDNC2FD3V3B`；`module_pin=20`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 3C，R4、D1、GPIO0、S1；网格 4C M1 pin20 GPIO0

### WS2812 RGB LED

U3 WS2812 由 VDD_3V3 供电，DI 接 SK_DIN，SK_DIN 连接 U1 GPIO21；DO 输出为 SK_DOUT。

- 参数与网络：`reference=U3`；`data_gpio=21`；`data_in=SK_DIN`；`data_out=SK_DOUT`；`supply=VDD_3V3`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2B U1 GPIO21/SK_DIN 与网格 3B-4B U3 WS2812

### GPIO3 默认偏置

GPIO3 通过 R3 10kΩ 上拉到 VDD_3V3，并同时引到 M1 pin3。

- 参数与网络：`gpio=3`；`pullup=R3 10kΩ`；`module_pin=3`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2A，U1 GPIO3 与 R3；网格 3C M1 pin3 GPIO3

### SPI 显示 GPIO 映射

DISP_RST=GPIO33、DISP_RS=GPIO34、DISP_MOSI=GPIO35、DISP_SCK=GPIO36、DISP_CS=GPIO37、DISP_BL=GPIO38；U2 以 DISP_BL 控制背光电源。

- 参数与网络：`reset_gpio=33`；`rs_gpio=34`；`mosi_gpio=35`；`sck_gpio=36`；`cs_gpio=37`；`backlight_gpio=38`；`backlight_switch=U2 SGM2578 / WS4622C-4/TR`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 2B-C，U1 GPIO33-GPIO38 对应 DISP 网络；网格 3A U2 EN=DISP_BL

## 时钟

### ESP32-S3 主时钟

X1 40MHz 晶体连接 U1 XTAL_P/XTAL_N，XTAL_P 支路串联 L3 10nH，两个晶体端分别配置 C9 10pF 和 C14 12pF 对地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`series_inductor=L3 10nH`；`load_capacitors=C9 10pF, C14 12pF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 1B-2B，X1、L3、C9、C14 与 XTAL_40M_P/N

## 复位

### ESP_EN 与 DC-DC 使能

U1 CHIP_PU 连接 ESP_EN，ESP_EN 由 R7 10kΩ 上拉到 VDD_3V3、C23 1uF 对地，并通过 D6 1N4148WT 连接 M2 的 EN 网络；M2 EN 另由 R16 100kΩ 接 VIN_5V。

- 参数与网络：`soc_enable=ESP_EN`；`soc_pullup=R7 10kΩ`；`soc_capacitor=C23 1uF`；`isolation_diode=D6 1N4148WT`；`converter_enable_pull=R16 100kΩ to VIN_5V`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 1D-2D，ESP_EN、R7、C23、D6、EN、R16 与 M2 pin1

## 保护电路

### USB 数据线 ESD 防护

连接器侧 USB_D_P 和 USB_D_N 分别由 D3、D4 PESDNC2FD3V3B 对地防护。

- 参数与网络：`dp_protection=D3 PESDNC2FD3V3B`；`dm_protection=D4 PESDNC2FD3V3B`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 3D，D3 接 USB_D_P、D4 接 USB_D_N，二者均接 GND

## 内存与 Flash

### ESP32-S3FN8 Flash 供电

U1 VDD_SPI 由 FLASH_VCC 供电并配置 C4 1uF 去耦；SPIHD、SPIWP、SPICS0、SPICLK、SPIQ 和 SPID 均标记为未连接，原理图未放置独立外部 Flash 器件。

- 参数与网络：`flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`unconnected_pins=SPIHD, SPIWP, SPICS0, SPICLK, SPIQ, SPID`；`external_flash_component=null`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 1A-2B，U1 pin29 VDD_SPI、C4 与 pin30-pin35 未连接标记

## 射频

### 板载 2.4GHz 天线

U1 LNA_IN 通过 ESP_LNA、L1 2.2nH 连接 ANT1 PROANT440，射频匹配节点配置 C1 2.2pF 和 C2 2.0pF 对地。

- 参数与网络：`antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series_inductor=L1 2.2nH`；`shunt_capacitors=C1 2.2pF, C2 2.0pF`
- 证据：图 aaa7dbf40110 / 第 1 页 / 网格 1A-2A，ANT1、L1、C1、C2、ESP_LNA 与 U1 LNA_IN

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-S3FN8 最小系统 | `reference=U1`；`part_number=ESP32-S3FN8`；`core_supply=VDD_3V3`；`enable_net=ESP_EN`；`rf_net=ESP_LNA` |
| 内存与 Flash | ESP32-S3FN8 Flash 供电 | `flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`unconnected_pins=SPIHD, SPIWP, SPICS0, SPICLK, SPIQ, SPID`；`external_flash_component=null` |
| 时钟 | ESP32-S3 主时钟 | `reference=X1`；`frequency=40MHz`；`series_inductor=L3 10nH`；`load_capacitors=C9 10pF, C14 12pF` |
| 射频 | 板载 2.4GHz 天线 | `antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series_inductor=L1 2.2nH`；`shunt_capacitors=C1 2.2pF, C2 2.0pF` |
| 电源 | USB VBUS 到 VIN_5V | `connector=J2`；`testpoint=JP1`；`fuse=F1 6V/1A/PPTC`；`output_net=VIN_5V`；`protection=D14 PESDNC2FD5VB` |
| 电源 | VDD_3V3 电源转换 | `converter=M2 MUN3CAD01-SC`；`input=VIN_5V`；`output=VDD_3V3`；`feedback=R6 100kΩ, R17 22.1kΩ`；`output_capacitors=C21 10uF, C22 10uF` |
| 复位 | ESP_EN 与 DC-DC 使能 | `soc_enable=ESP_EN`；`soc_pullup=R7 10kΩ`；`soc_capacitor=C23 1uF`；`isolation_diode=D6 1N4148WT`；`converter_enable_pull=R16 100kΩ to VIN_5V` |
| 接口 | USB Type-C 连接 | `connector=J2 USB-TYPEC`；`dp_net=USB_D_P`；`dm_net=USB_D_N`；`cc1_pulldown=R1 5.1kΩ`；`cc2_pulldown=R2 5.1kΩ` |
| 总线 | ESP32-S3 原生 USB 差分链路 | `dm_gpio=19`；`dp_gpio=20`；`soc_nets=USB_DU_N, USB_DU_P`；`connector_nets=USB_D_N, USB_D_P`；`common_mode_choke=L5`；`testpoints=JP2, JP3` |
| 保护电路 | USB 数据线 ESD 防护 | `dp_protection=D3 PESDNC2FD3V3B`；`dm_protection=D4 PESDNC2FD3V3B` |
| GPIO 与控制信号 | GPIO0 用户与启动按键 | `switch=S1 SMT_SW_1TS026A`；`net=GPIO0`；`active_level=low`；`pullup=R4 10kΩ`；`protection=D1 PESDNC2FD3V3B`；`module_pin=20` |
| GPIO 与控制信号 | WS2812 RGB LED | `reference=U3`；`data_gpio=21`；`data_in=SK_DIN`；`data_out=SK_DOUT`；`supply=VDD_3V3` |
| 接口 | STAMP-S3M 电源和控制焊盘 | `connector=M1 STAMP-S3M`；`five_volt_pin=13`；`three_v_three_pin=28`；`ground_pins=11,18`；`enable_pin=22` |
| 接口 | STAMP-S3M 外部 GPIO | `connector=M1 STAMP-S3M`；`gpio_count=23`；`gpio_list=GPIO0, GPIO1, GPIO2, GPIO3, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10, GPIO11, GPIO12, GPIO13, GPIO14, GPIO15, GPIO39, GPIO40, GPIO41, GPIO42, GPIO43, GPIO44, GPIO46` |
| 总线 | UART0 到模组焊盘 | `tx_soc=U1 U0TXD`；`tx_net=TX`；`tx_gpio=43`；`tx_module_pin=26`；`tx_series_resistor=R5 510Ω`；`rx_soc=U1 U0RXD`；`rx_net=RX`；`rx_gpio=44`；`rx_module_pin=24` |
| GPIO 与控制信号 | GPIO3 默认偏置 | `gpio=3`；`pullup=R3 10kΩ`；`module_pin=3` |
| 接口 | J3 八针 SPI 显示接口 | `connector=J3 HDGC/0.5K-HX-8PWB`；`pin1=backlight output`；`pin2=GND`；`pin3=DISP_RST`；`pin4=DISP_RS`；`pin5=DISP_MOSI`；`pin6=DISP_SCK`；`pin7=VDD_3V3`；`pin8=DISP_CS` |
| GPIO 与控制信号 | SPI 显示 GPIO 映射 | `reset_gpio=33`；`rs_gpio=34`；`mosi_gpio=35`；`sck_gpio=36`；`cs_gpio=37`；`backlight_gpio=38`；`backlight_switch=U2 SGM2578 / WS4622C-4/TR` |
| 接口 | J1 十二针显示接口预留 | `connector=J1 HDGC/0.5K-HX-12PWB/NC`；`assembly=NC`；`extra_signals=VIN_5V, GPIO18, GPIO17, GPIO16`；`shared_display_signals=backlight, DISP_RST, DISP_RS, DISP_MOSI, DISP_SCK, VDD_3V3, DISP_CS` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `aaa7dbf40110a4ec90c6f2dae371394bafe3c0894ae255aca506aba1b636899f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2_sch_01.png` |

---

源文档：`zh_CN/core/StampS3.md`

源文档 SHA-256：`84c9ec1ad0e25c9610a4d6ced3a915a00fea9e68cac4d42b0b84f55ebe401327`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
