# Fire v2.6 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Fire v2.6 |
| SKU | K007-V26 |
| 产品 ID | `fire-v2-6-4b8ab98411fc` |
| 源文档 | `zh_CN/core/fire_v2.6.md` |

## 概述

Fire v2.6 清单绑定的六页资源是 2017 年 M5 STACK CORE Revision A 主机原理图，图中包含 ESP32-D0WDQ6、GD25Q32C、IP5306、EA3036、CP2104、M5-LCD、MicroSD、M5-Bus 和 NS4148 音频链路。资源可确认主机电源、UART、按键、LCD/TF、扩展总线和扬声器功放连接，但没有 Fire/K007-V26、M5GO 底座、MPU6886、RGB LED、麦克风或 PSRAM 电路。正文所列 16MB Flash、8MB PSRAM、CH9102F、Type-C、MPU6886、10颗 SK6812、模拟麦克风、500mAh 电池和 1W 扬声器均与旧图不一致或缺少证据，已严格隔离为待确认。

## 检索关键词

`Fire v2.6`、`K007-V26`、`M5Stack FIRE`、`M5 STACK CORE`、`M5GO BOTTOM`、`Revision A`、`2017/12/6`、`ESP32-D0WDQ6`、`GD25Q32C`、`16MB Flash`、`8MB PSRAM`、`GPIO16`、`GPIO17`、`IP5306`、`IP5306 0x75`、`EA3036`、`CP2104`、`CH9102F`、`USB_Micro`、`USB Type-C`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`NS4148`、`M5-Bus`、`MPU6886`、`MPU6886 0x68`、`SK6812`、`Analog BSE3729 Microphone`、`GPIO15`、`GPIO34`、`GPIO25`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO14`、`GPIO4`、`GPIO32`、`GPIO33`、`GPIO37`、`GPIO38`、`GPIO39`、`GPIO21`、`GPIO22`、`VCC_5V`、`VCC_3V3`、`AMP_PWR`、`VIN_USB`、`VBAT`、`40MHz`、`ANT1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 2017 CORE 图中的主控，连接外部 Flash、RF、UART、LCD、TF 卡、按键与 M5-Bus | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 |
| U2 | GD25Q32C | ESP32 外部 SPI Flash | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| U4 | EA3036 | 从 VCC_5V 产生 VCC_3V3、VDD_3V3 和 AMP_PWR 的三路降压器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 |
| U10 | IP5306 | VIN_USB、VBAT 与 VCC_5V 之间的充放电及升压电源管理器 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 |
| ANT1,C1,L1,C9 | 未标注 | ESP_LNA 到 ANT1 的预留 T 型射频匹配网络 | 图 d81402da2106 / 第 1 页 / 网格 A2，ESP_LNA、TBD 匹配与 ANT1 |
| X1 | 40MHz/+/-10ppm/22pF | ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22 |
| U3 | CP2104 | 2017 图中的 USB-UART 桥和自动下载源 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 | USB_Micro | 图中 USB 电源与 D+/D- 连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5 USB_Micro |
| U6,FET1 | M5-LCD / AO3402 | SPI LCD 接口及 GPIO32 背光开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，U6/FET1 |
| U8 | MicroSD-SPI | GPIO4/23/18/19 SPI TF 卡槽 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1-S4 | SMT-3x6-SWC / SMT_SW_TS_015 | GPIO37/38/39 用户按键与 PWR 按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-C1，Button 区 |
| P1 | Header 15X2 | 30 针 M5-Bus GPIO/电源扩展 | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| U9 | NS4148 | GPIO25 输入的差分 Class-D 音频放大器 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 |
| D1,D2,FUSE1 | RLSD52A031V / 2A | USB D+/D- ESD 保护与 VIN_USB 保险丝 | 图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，D1/D2/FUSE1 |

## 系统结构

### 所提供 2017 CORE 主机图

六页封面列出 POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINATION 和 AUDIO AMPLIFER，图框日期为 2017/12/6、Revision A。

- 参数与网络：`title=M5 STACK CORE`；`revision=A`；`date=2017/12/6`；`cover_release=A13`；`pages=6`
- 证据：图 a44d9e10f49e / 第 1 页 / 封面修订表、PAGE NO. 与图框

## 核心器件

### U1 ESP32-D0WDQ6

U1 标注 ESP32-D0WDQ6，VCC_3V3 供电，VDD_SDIO 独立引出到外部 Flash，EN 接 CHIP_PU，ESP_LNA 为射频输出。

- 参数与网络：`reference=U1`；`part=ESP32-D0WDQ6`；`core_rail=VCC_3V3`；`flash_rail=VDD_SDIO`；`enable=EN`；`rf=ESP_LNA`
- 证据：图 d81402da2106 / 第 1 页 / U1 ESP32-D0WDQ6 电源/Flash/RF 引脚

## 电源

### IP5306 充放电路径

U10 IP5306 VIN 接 VIN_USB，VOUT 接 VCC_5V，BAT 与 SW 经电感接 VBAT，KEY 接 PWR_KEY；页面标注 5V 2.4A Sync Boost 和 2.1A Sync Buck Charger。

- 参数与网络：`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost=5V 2.4A annotation`；`charger=2.1A annotation`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 与电流能力注释

### EA3036 三路电源

U4 EA3036 从 VCC_5V 产生 VCC_3V3、VDD_3V3 和 AMP_PWR；三路反馈均为 510K/110K，输出分别配 C14/C28/C33 22uF/6.3V。

- 参数与网络：`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2,L3,L5`；`feedback=510K/110K each`；`caps=C14/C28/C33 22uF/6.3V`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 三路 SW/FB

## 接口

### 旧图 USB 连接器电路

U5 符号标 USB_Micro，VCC 经 FUSE1 2A 接 VIN_USB，D-/D+ 分别经 R9/R11 22Ω接 USB_DN/USB_DP，ID 未连接；另画 USB_CC_1/2 各 5.10K 下拉。

- 参数与网络：`symbol=USB_Micro`；`vbus=FUSE1 2A -> VIN_USB`；`dm=R9 22R`；`dp=R11 22R`；`id=NC`；`cc=two 5.10K pulldowns`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，U5/USB-PD Recognition

### M5-LCD 接口与背光

U6 #RST/R/S/MOSI/SCK/CS 分别连接 GPIO33/27/23/18/14；三个 BL 引脚由 FET1 AO3402 开关，GPIO32 驱动栅极并由 R15 100K 下拉。

- 参数与网络：`reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`cs=GPIO14`；`backlight=GPIO32/FET1`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，U6/FET1

### 30 针 M5-Bus

P1 pins1-10 为 GND/GPIO35、GND/GPIO36、GND/EN、GPIO23/GPIO25、GPIO19/GPIO26；pins11-20 为 EXT_SCK/VDD_3V3、GPIO3/GPIO1、GPIO16/GPIO17、GPIO21/GPIO22、GPIO2/GPIO5；pins21-30 为 GPIO12/GPIO13、GPIO15/GPIO0、HPWR/GPIO34、HPWR/VCC_5V、HPWR/VBAT。

- 参数与网络：`pins_1_10=GND/G35,GND/G36,GND/EN,G23/G25,G19/G26`；`pins_11_20=EXT_SCK/3V3,G3/G1,G16/G17,G21/G22,G2/G5`；`pins_21_30=G12/G13,G15/G0,HPWR/G34,HPWR/5V,HPWR/VBAT`；`ext_sck=R2 22R to GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / P1 Header 15X2 与功能表

## 总线地址

### 定制 IP5306 I2C 地址

电源页文字明确说明定制 IP5306 通过 IIC 与 ESP32 通信，IIC address is 0x75。

- 参数与网络：`device=U10 IP5306`；`address_7bit=0x75`；`bus=IIC`；`gpio_mapping=null`
- 证据：图 91b865957940 / 第 1 页 / IP5306 下方 0x75 文字

## GPIO 与控制信号

### 三个用户按键

S1/S2/S3 分别将 GPIO37/GPIO38/GPIO39 按下接地，对应 Btn C/Btn B/Btn A，R4/R7/R10 各 100K 上拉到 VDD_3V3。

- 参数与网络：`button_c=GPIO37`；`button_b=GPIO38`；`button_a=GPIO39`；`active=low`；`pullups=100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S3

## 时钟

### ESP32 40MHz 晶振

X1 标注 40MHz/+/-10ppm/22pF，连接 ESP_XTAL_N/P，C21/C22 各 22pF 接地。

- 参数与网络：`frequency=40MHz`；`tolerance=+/-10ppm`；`load=22pF`；`capacitors=C21/C22 22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22

## 复位

### EN/PWR 按键网络

EN 由 R12 12K 上拉并由 C25 1nF 对地，PWR 通过 12K 接 EN；S4 按下将 PWR 接地，PWR 另有 R13 100K、C7 1nF 和 D28。

- 参数与网络：`en_pullup=R12 12K`；`en_cap=C25 1nF`；`pwr_to_en=12K`；`button=S4`；`pwr_network=R13/C7/D28`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-C2，PWR/EN/S4

## 保护电路

### M5-Bus GPIO ESD

M5-Bus 页在 GPIO23/35、GPIO19/36、EXT_SCK/EN、GPIO3/25、GPIO16/26、GPIO21/1、GPIO2/17、GPIO12/22、GPIO15/5、GPIO13、GPIO0、GPIO34 上画有 RLSD52A031V 对地保护阵列。

- 参数与网络：`part=RLSD52A031V`；`protected_nets=GPIO23,35,19,36,EXT_SCK,EN,3,25,16,26,21,1,2,17,12,22,15,5,13,0,34`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-D1，D2-D23

## 存储

### GD25Q32C 外部 Flash

U2 GD25Q32C nCS/CLK/DI/DO/nHOLD/nWP 分别连接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA2、SD_DATA3，VCC 接 VCC_3V3。

- 参数与网络：`part=GD25Q32C`；`cs=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 与 SD_*

### TF 卡 SPI

U8 MicroSD-SPI 的 CS/DI/SCLK/DO 分别连接 GPIO4/GPIO23/GPIO18/GPIO19，VDD 接 VDD_3V3，四条信号各有 12K 上拉。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`supply=VDD_3V3`；`pullups=R17/R18/R20/R21 12K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 C1-D2，U8/上拉网络

## 音频

### NS4148 扬声器放大链路

GPIO25 经 C43 100nF 接 U9 NS4148 INP，INN 经 C44 100nF 接 PGND；VOP/VON 经 FB1/FB2 600R@100M 输出 AUDIO_OUT_P/N，U9 由 AMP_PWR 供电。

- 参数与网络：`input=GPIO25`；`amplifier=NS4148`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P/N`；`ferrites=FB1/FB2 600R@100M`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 音频链路

## 射频

### 旧图射频匹配

ESP_LNA 通过 C1 串联到 ANT1，L1 在输入侧对地、C9 在输出侧对地，L1/C1/C9 数值均标 TBD。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1`；`series=C1 TBD`；`shunt=L1/C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ESP_LNA/C1/L1/C9/ANT1

## 调试与烧录

### CP2104 UART0 与自动下载

U3 CP2104 TXD 经 R8 470Ω接 RXD0/GPIO3，RXD 接 TXD0/GPIO1；DTR/RTS 经 R16/R19 12K 和两只 NPN-S8050 驱动 EN/GPIO0。

- 参数与网络：`bridge=CP2104`；`tx=R8 470R -> GPIO3`；`rx=GPIO1`；`download_inputs=DTR,RTS`；`download_targets=EN,GPIO0`
- 证据：图 2f5b17c1e346 / 第 1 页 / U3 CP2104 与 Auto-Download 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 所提供 2017 CORE 主机图 | `title=M5 STACK CORE`；`revision=A`；`date=2017/12/6`；`cover_release=A13`；`pages=6` |
| 核心器件 | U1 ESP32-D0WDQ6 | `reference=U1`；`part=ESP32-D0WDQ6`；`core_rail=VCC_3V3`；`flash_rail=VDD_SDIO`；`enable=EN`；`rf=ESP_LNA` |
| 电源 | IP5306 充放电路径 | `input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost=5V 2.4A annotation`；`charger=2.1A annotation` |
| 总线地址 | 定制 IP5306 I2C 地址 | `device=U10 IP5306`；`address_7bit=0x75`；`bus=IIC`；`gpio_mapping=null` |
| 电源 | EA3036 三路电源 | `input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2,L3,L5`；`feedback=510K/110K each`；`caps=C14/C28/C33 22uF/6.3V` |
| 时钟 | ESP32 40MHz 晶振 | `frequency=40MHz`；`tolerance=+/-10ppm`；`load=22pF`；`capacitors=C21/C22 22pF` |
| 存储 | GD25Q32C 外部 Flash | `part=GD25Q32C`；`cs=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2` |
| 射频 | 旧图射频匹配 | `source=ESP_LNA`；`antenna=ANT1`；`series=C1 TBD`；`shunt=L1/C9 TBD` |
| 调试与烧录 | CP2104 UART0 与自动下载 | `bridge=CP2104`；`tx=R8 470R -> GPIO3`；`rx=GPIO1`；`download_inputs=DTR,RTS`；`download_targets=EN,GPIO0` |
| 接口 | 旧图 USB 连接器电路 | `symbol=USB_Micro`；`vbus=FUSE1 2A -> VIN_USB`；`dm=R9 22R`；`dp=R11 22R`；`id=NC`；`cc=two 5.10K pulldowns` |
| GPIO 与控制信号 | 三个用户按键 | `button_c=GPIO37`；`button_b=GPIO38`；`button_a=GPIO39`；`active=low`；`pullups=100K` |
| 复位 | EN/PWR 按键网络 | `en_pullup=R12 12K`；`en_cap=C25 1nF`；`pwr_to_en=12K`；`button=S4`；`pwr_network=R13/C7/D28` |
| 接口 | M5-LCD 接口与背光 | `reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`cs=GPIO14`；`backlight=GPIO32/FET1` |
| 存储 | TF 卡 SPI | `cs=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`supply=VDD_3V3`；`pullups=R17/R18/R20/R21 12K` |
| 接口 | 30 针 M5-Bus | `pins_1_10=GND/G35,GND/G36,GND/EN,G23/G25,G19/G26`；`pins_11_20=EXT_SCK/3V3,G3/G1,G16/G17,G21/G22,G2/G5`；`pins_21_30=G12/G13,G15/G0,HPWR/G34,HPWR/5V,HPWR/VBAT`；`ext_sck=R2 22R to GPIO18` |
| 保护电路 | M5-Bus GPIO ESD | `part=RLSD52A031V`；`protected_nets=GPIO23,35,19,36,EXT_SCK,EN,3,25,16,26,21,1,2,17,12,22,15,5,13,0,34` |
| 音频 | NS4148 扬声器放大链路 | `input=GPIO25`；`amplifier=NS4148`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P/N`；`ferrites=FB1/FB2 600R@100M` |
| 系统结构 | Fire v2.6 与 2017 CORE 资源对应关系 | `product=Fire v2.6`；`sku=K007-V26`；`schematic=2017 CORE Revision A`；`fire_marking=null`；`bottom_schematic=null` |
| 内存与 Flash | Fire v2.6 16MB Flash 与 8MB PSRAM | `documented_flash=16MB`；`documented_psram=8MB Quad`；`psram_gpios=GPIO16/GPIO17`；`schematic_flash=GD25Q32C`；`schematic_psram=null`；`legacy_bus=GPIO16/17 exported` |
| 调试与烧录 | v2.6 CH9102F USB-UART | `documented=CH9102F`；`change=CP2104 -> CH9102`；`schematic=CP2104`；`production_part=null` |
| 接口 | Fire v2.6 USB Type-C | `documented=USB Type-C`；`schematic_symbol=USB_Micro`；`cc=separate 5.10K pulldowns`；`connector_cc=null`；`c2c_pd=null` |
| 核心器件 | Fire v2.6 ILI9342C IPS 屏 | `documented=ILI9342C 2.0 inch 320x240 IPS 853nit`；`schematic=M5-LCD`；`panel_bom=null` |
| 总线 | IP5306 GPIO21/22 I2C 映射 | `documented_sda=GPIO21`；`documented_scl=GPIO22`；`address=0x75`；`u10_bus_pins=null` |
| 传感器 | MPU6886 六轴 IMU | `documented_imu=MPU6886`；`address=0x68`；`sda=GPIO21`；`scl=GPIO22`；`bmm150=removed in v2.6`；`schematic_imu=null` |
| 系统结构 | M5GO 底座 LED、麦克风与 Grove | `documented_leds=10x SK6812 on GPIO15`；`documented_microphone=Analog BSE3729 on GPIO34`；`port_b=GPIO26/GPIO36`；`port_c=GPIO17/GPIO16`；`bottom_schematic=null` |
| 音频 | 1W-0928 扬声器 | `documented=1W-0928`；`amplifier=NS4148`；`outputs=AUDIO_OUT_P/N`；`speaker_part=null`；`impedance=null` |
| 电源 | 500mAh 电池与 5V@500mA 输入 | `documented_battery=500mAh@3.7V`；`documented_input=5V@500mA`；`schematic_battery=VBAT net only`；`usb_fuse=2A`；`ip5306=2.4A boost/2.1A charger annotations`；`measurement_conditions=null` |
| 射频 | Fire v2.6 2.4G 3D 天线 | `documented=2.4G 3D antenna`；`schematic=ANT1 with TBD matching`；`part=null`；`matching=null`；`layout=null`；`test_result=null` |

## 待确认事项

- `system.fire-v26-resource-version`：产品为 Fire v2.6/K007-V26，版本表显示 2018-2021 多次硬件更改；所提供六页仅标 2017 M5 STACK CORE Revision A，没有 Fire、K007-V26、M5GO 底座或 v2.6 标识，当前适用范围需确认。（证据：图 a44d9e10f49e / 第 1 页 / 2017 M5 STACK CORE 封面，无 Fire/SKU）
- `memory.fire-v26-flash-psram`：正文称 16MB Flash+8MB Quad PSRAM，并警告 GPIO16/17 被 PSRAM 占用；旧图只画 U2 GD25Q32C，未画 PSRAM，且 M5-Bus 仍把 GPIO16/17 作为 RXD2/TXD2 引出，v2.6 存储及冲突边界需确认。（证据：图 d81402da2106 / 第 1 页 / U2 GD25Q32C，无 PSRAM; 图 72aa5b4d2f89 / 第 1 页 / P1 pins15/16 GPIO16/GPIO17）
- `debug.fire-v26-usb-bridge`：正文规格列 CH9102F，版本表称 v2.6 将 CP2104 更换为 CH9102；所提供页仍为 U3 CP2104，v2.6 桥接芯片和自动下载外围需确认。（证据：图 2f5b17c1e346 / 第 1 页 / U3 CP2104）
- `interface.fire-v26-typec`：正文称 USB Type-C；旧图标题写 Type-C USB 并画 CC 下拉，但 U5 实际符号为 USB_Micro 且 CC 未接连接器，v2.6 Type-C 与 C2C/PD 实现需确认。（证据：图 2f5b17c1e346 / 第 1 页 / Type-C USB/USB-PD/U5 区）
- `component.fire-v26-lcd`：正文称 2.0英寸 320x240 ILI9342C IPS、最高亮度 853nit；旧图 U6 只标 M5-LCD，没有面板型号、分辨率、亮度或 Fire 屏幕版本。（证据：图 2f5b17c1e346 / 第 1 页 / U6 M5-LCD）
- `bus.documented-ip5306`：正文将 IP5306 0x75 SDA/SCL 映射为 GPIO21/GPIO22；电源页只有地址文字且 U10 符号无 SDA/SCL，M5-Bus 页只显示 GPIO21/22 引出，无法从旧图闭合确认。（证据：图 91b865957940 / 第 1 页 / U10 无 I2C 引脚; 图 72aa5b4d2f89 / 第 1 页 / P1 GPIO21/GPIO22）
- `sensor.fire-v26-mpu6886`：正文称 v2.6 使用 MPU6886(0x68)，SDA/SCL 为 GPIO21/GPIO22，并在 v2.6 取消 BMM150；六页旧图没有 MPU6886、IMU 中断、电源、地址选择或 BMM150 电路。（证据：图 d81402da2106 / 第 1 页 / ESP32 主机页无 MPU6886/BMM150; 图 2f5b17c1e346 / 第 1 页 / 外设页无 IMU）
- `system.fire-bottom-peripherals`：正文称 M5GO 底座含 10颗 SK6812(GPIO15)、Analog BSE3729 麦克风(GPIO34)以及 PORT.B GPIO26/36、PORT.C GPIO17/16；六页只有主机 M5-Bus，没有底座原理图、LED 链、麦克风偏置/放大或 Grove 连接器。（证据：图 72aa5b4d2f89 / 第 1 页 / 仅 M5-Bus 引出 GPIO15/34/26/36/17/16，无底座器件）
- `audio.fire-v26-speaker`：正文称扬声器为 1W-0928；旧图只显示 NS4148 与 AUDIO_OUT_P/N，没有扬声器器件、阻抗、连接器或 1W 额定证据。（证据：图 8d7498c3a5a7 / 第 1 页 / AUDIO_OUT_P/N，无扬声器器件）
- `power.fire-v26-battery-input`：正文称 500mAh@3.7V 电池和 5V@500mA 输入；旧图只显示 VBAT 网络、FUSE1 2A、IP5306 2.4A/2.1A 注释，没有电池料号、容量或整机输入测试条件。（证据：图 91b865957940 / 第 1 页 / IP5306 VBAT 与电流能力注释; 图 2f5b17c1e346 / 第 1 页 / FUSE1 2A）
- `rf.fire-v26-antenna`：正文称经过专业调制的 2.4G 3D 天线；旧图仅画 ANT1 与 TBD 匹配，没有 v2.6 天线料号、最终匹配值、PCB 布局或射频测试结果。（证据：图 d81402da2106 / 第 1 页 / ANT1/L1/C1/C9 TBD）
- `review.resource-version`：请提供 Fire v2.6/K007-V26 主机与 M5GO 底座的正式原理图/BOM，确认 2017 CORE 页的适用范围。；原因：资源没有 Fire、v2.6 或底座标识。
- `review.flash-psram`：请确认 16MB Flash、8MB Quad PSRAM 的料号、总线和 GPIO16/17 冲突边界。；原因：旧图无 PSRAM且仍引出 GPIO16/17。
- `review.usb-bridge`：请确认 Fire v2.6 CH9102F 料号、引脚和自动下载外围。；原因：提供的页仍画 CP2104。
- `review.typec`：请确认 Fire v2.6 Type-C 连接器、CC 接法与 C2C/PD 兼容边界。；原因：旧图使用 USB_Micro 符号且 CC 未连接。
- `review.lcd`：请确认 Fire v2.6 ILI9342C IPS 面板料号、分辨率、亮度和背光参数。；原因：旧图只标 M5-LCD。
- `review.ip5306-bus`：请确认 IP5306 0x75 的 SDA/SCL 是否连接 GPIO21/GPIO22，并提供完整 U10 引脚图。；原因：旧图未画 I2C 引脚。
- `review.imu`：请提供 v2.6 IMU 电路，确认 MPU6886 0x68、电源、I2C、中断和 BMM150 取消情况。；原因：六页无 IMU 电路。
- `review.bottom`：请提供 M5GO BOTTOM 原理图/BOM，确认 10颗 SK6812、BSE3729 麦克风与 PORT.B/C。；原因：当前资源只有主机 M5-Bus。
- `review.speaker`：请确认 1W-0928 扬声器料号、阻抗、连接器与 NS4148 匹配。；原因：旧图没有扬声器器件。
- `review.battery-input`：请确认 500mAh 电池料号、连接器、保护及 5V@500mA 输入测试条件。；原因：旧图只有 VBAT 和不同层级的电流能力注释。
- `review.antenna`：请确认 v2.6 3D 天线料号、最终匹配、布局及射频测试。；原因：旧图匹配值均为 TBD。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a44d9e10f49eba739a7d1b57e10ddb75ee06740af6339dda71801119e0ff3e95` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_01.png` |
| 2 | 1 | `91b865957940b7595eb4abcbb1d34ab61b82753b0035267d860ef1a3cfd453bb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_02.png` |
| 3 | 1 | `d81402da2106664255e50b82ad9e519d7f0f6b1844ddefc24b5aecc28a7ccdbf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_03.png` |
| 4 | 1 | `2f5b17c1e346f2498049eb882140037528b100afbf6854879dbc91605c44a0f6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_04.png` |
| 5 | 1 | `72aa5b4d2f89ab1e81f41d1b5916bfa3b7a527a19c21ca6ee946c882f6d8ce5c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_05.png` |
| 6 | 1 | `8d7498c3a5a7fd1010952eda7a2742715f09a8abc789055f9d1e77f7900af32f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_06.png` |

---

源文档：`zh_CN/core/fire_v2.6.md`

源文档 SHA-256：`188c458071bc7b61d8aec3bab42134702ab63b206f0db596cbff6161196dadda`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
