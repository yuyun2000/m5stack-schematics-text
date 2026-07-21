# M5GO IoT Kit v2.6 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5GO IoT Kit v2.6 |
| SKU | K006-V26 |
| 产品 ID | `m5go-iot-kit-v2-6-398b26645492` |
| 源文档 | `zh_CN/core/m5go_v2.6.md` |

## 概述

M5GO IoT Kit v2.6 的资源包含一张早期 M5GO 单页电路和 2017 年 M5 STACK CORE Rev A 六页电路。单页图采用 ESP32-WROOM32、ZJY-6428TSW0G01、GPIO26 晶体管扬声器和可选 MPU9250；六页 Core 图采用 ESP32-D0WDQ6、GD25Q32C、EA3036、IP5306、CP2104、M5-LCD、microSD、M5-Bus 和 NS4148。两套资源均未标识 M5GO IoT Kit v2.6 或 K006-V26，且与产品源文档所述 16MB Flash、CH9102F、MPU6886、取消 BMM150、ILI9342C、底座 RGB/麦克风和 500mAh 电池存在覆盖缺口或版本差异，因此这些量产配置均列为待确认。

## 检索关键词

`M5GO IoT Kit v2.6`、`K006-V26`、`M5GO`、`ESP32-WROOM32`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`ZJY-6428TSW0G01`、`ILI9342C`、`MPU9250`、`MPU6886`、`BMM150`、`GD25Q32C`、`16MB Flash`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`CH9102F`、`NS4148`、`DET402-G-1`、`BSE3729`、`SK6812`、`M5-Bus`、`USB Type-C`、`USB_Micro`、`MicroSD-SPI`、`GPIO15`、`GPIO17`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO26`、`GPIO34`、`VCC_3V3`、`VCC_5V`、`VDD_3V3`、`AMP_PWR`、`VBAT`、`AUDIO_OUT_P`、`AUDIO_OUT_N`、`40MHz`、`SPI`、`I2C`、`UART`、`ENV-III`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 [aux] | ESP32-WROOM32 | 单页资源中的 ESP32 模组，连接显示、LED、扬声器和可选 MPU9250 | 图 87dd78652b8f / 第 1 页 / 页面左上，U1 ESP32-WROOM32 |
| U2 [aux] | ZJY-6428TSW0G01 | 单页资源中的显示模组接口，连接 SPI 控制和双电源 | 图 87dd78652b8f / 第 1 页 / 页面左下，U2 ZJY-6428TSW0G01 |
| LS1,VT3 [aux] | DET402-G-1 / NPN-S8050 | 单页资源中由 GPIO26 控制的晶体管扬声器支路 | 图 87dd78652b8f / 第 1 页 / 页面右上，GPIO26/R21/VT3/LS1 |
| LED1,LED2 [aux] | BLUE_LED / IR_LED | 单页资源中的 GPIO19 蓝色 LED 与 GPIO17 红外 LED | 图 87dd78652b8f / 第 1 页 / 页面右上，LED1/LED2/R19/R20 |
| U8 [aux] | MPU9250 | 单页资源中标为 Optional For Gray Version 的 I2C 传感器位 | 图 87dd78652b8f / 第 1 页 / 页面右下红框 Optional For Gray Version，U8 MPU9250 |
| U1 [core] | ESP32-D0WDQ6 | 六页 Core 图主控 SoC | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 |
| U2 [core] | GD25Q32C | 六页 Core 图外部 SPI Flash | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| X1 [core] | 40MHz/+-10ppm/22pF | 六页 Core 图 ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22 |
| ANT1 [core] | 未标注 | 六页 Core 图 ESP_LNA 射频天线端与匹配位 | 图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/ESP_LNA |
| U4 [core] | EA3036 | VCC_5V 至三路电源的同步降压转换器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 |
| U10 [core] | IP5306 | USB、电池和 5V 电源管理器，图面标注定制 I2C 地址 0x75 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 |
| U3 [core] | CP2104 | 六页 Core 图 USB 转 UART 与自动下载信号源 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 [core] | USB_Micro | 六页 Core 图 Type-C 分区中标为 USB_Micro 的连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，Type-C 标题与 U5 USB_Micro |
| U6 [core] | M5-LCD | 六页 Core 图 LCD 模组接口 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD |
| U8 [core] | MicroSD-SPI | 六页 Core 图 SPI microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1,S2,S3,S4 [core] | SMT-3x6-SWC / SMT_SW_TS_015 | 六页 Core 图三个用户按键与电源按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S4 |
| FET1 [core] | AO3402 | 六页 Core 图 GPIO32 控制的 LCD 背光开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1 AO3402 |
| P1 [core] | Header 15X2 | 六页 Core 图 30 针 M5-Bus | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| D2-D23,R2 [core] | RLSD52A031V / 22R | 六页 Core 图 M5-Bus 多信号保护阵列与 EXT_SCK 串联电阻 | 图 72aa5b4d2f89 / 第 1 页 / 网格 B1-C1，R2 与 RLSD52A031V 阵列 |
| U9 [core] | NS4148 | 六页 Core 图 GPIO25 输入的差分 D 类功放 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 |

## 系统结构

### 单页资源架构

单页资源以 U1 ESP32-WROOM32 为主控，连接 U2 显示接口、GPIO26 扬声器、GPIO19 蓝色 LED、GPIO17 红外 LED，并画出标为 Optional For Gray Version 的 U8 MPU9250。

- 参数与网络：`soc=ESP32-WROOM32`；`display=ZJY-6428TSW0G01`；`speaker=GPIO26`；`blue_led=GPIO19`；`ir_led=GPIO17`；`optional_sensor=MPU9250`
- 证据：图 87dd78652b8f / 第 1 页 / 单页整图

### 六页 Core 图来源版本

六页封面标 M5 STACK CORE，修订记录 A13 OFFICIAL RELEASE VERSION、日期 10/11/2017，标题栏 Revision A、Date 2017/12/6。

- 参数与网络：`design=M5 STACK CORE`；`revision=A13/A`；`dates=10/11/2017,2017/12/6`
- 证据：图 a44d9e10f49e / 第 1 页 / 修订表与标题栏

### 六页 Core 功能分区

封面目录列出 COVER PAGE、POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINITION 和 AUDIO AMPLIFIER。

- 参数与网络：`pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio`
- 证据：图 a44d9e10f49e / 第 1 页 / 页面目录

## 核心器件

### ESP32-WROOM32 单页主控

U1 标为 ESP32-WROOM32，VCC_3V3 接 3V3，EN、TXD0/RXD0 和多路 GPIO 引出，SD0-SD3、CMD 与 CLK 标记未连接。

- 参数与网络：`reference=U1 [aux]`；`part_number=ESP32-WROOM32`；`supply=VCC_3V3`；`uart=TXD0,RXD0`；`sdio=NC`
- 证据：图 87dd78652b8f / 第 1 页 / 页面左上，U1 ESP32-WROOM32

### ESP32-D0WDQ6

六页 Core 图 U1 标为 ESP32-D0WDQ6，CHIP_PU 接 EN，RF 接 ESP_LNA，Flash 接 SD_CMD、SD_CLK 与 SD_DATA0-SD_DATA3。

- 参数与网络：`reference=U1 [core]`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0-SD_DATA3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1

## 电源

### EA3036 三路电源

U4 EA3036 以 VCC_5V 供电，SW1、SW2、SW3 经 L2、L3、L5 输出 VCC_3V3、VDD_3V3、AMP_PWR，三路反馈均为 510K/110K。

- 参数与网络：`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`feedback=510K/110K`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4

### AMP_PWR 关闭测试点

EA3036 EN3 由 R23 10K 上拉，T1 为接地 0R 测试断点，图面注释用于关闭功放。

- 参数与网络：`enable=EN3`；`pullup=R23 10K`；`test_break=T1 0R`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1，T1/R23/EN3 注释

### IP5306 电源管理

U10 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY，图面标注 5V 2.4A Sync Boost 与 2.1A Sync Buck Charger。

- 参数与网络：`input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`annotation=5V 2.4A Sync Boost / 2.1A Sync Buck Charger`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306

## 接口

### ZJY-6428TSW0G01 显示接口

U2 CS、RES、DC、D0、D1 分别连接 GPIO14、GPIO33、GPIO27、GPIO18、GPIO23，VDD 接 VCC_3V3，VPP/VCOMH 电源网络另接 VCC_9V 与滤波电容。

- 参数与网络：`cs=GPIO14`；`reset=GPIO33`；`dc=GPIO27`；`clock=GPIO18`；`data=GPIO23`；`logic_supply=VCC_3V3`；`panel_supply=VCC_9V`
- 证据：图 87dd78652b8f / 第 1 页 / 页面左下，U2 与 C3-C5/R2

### 六页 Core USB 电路

U5 VCC 经 FUSE1 2A 接 VIN_USB，D- 与 D+ 经 R9、R11 22R 接 USB_DN、USB_DP，并由 D1、D2 保护；USB_CC_1 与 USB_CC_2 各通过 5.10K 电阻接地。

- 参数与网络：`fuse=FUSE1 2A`；`data_series=R9/R11 22R`；`cc_pulldown=R6/R7 5.10K`；`protection=D1/D2`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A4，Type-C/U5 USB_Micro

### M5-LCD SPI 接口

U6 的 #RST、R/S、MOSI、SCK、CS 分别接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14；背光由 GPIO32 控制 FET1 AO3402。

- 参数与网络：`reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14`；`backlight=GPIO32`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6/FET1

## 总线

### 30 针 M5-Bus

P1 引出 GND、GPIO35/36、EN、GPIO23/25、GPIO19/26、GPIO18、3.3V、GPIO3/1、GPIO16/17、GPIO21/22、GPIO2/5、GPIO12/13、GPIO15/0、HPWR、GPIO34、5V 与 VBAT。

- 参数与网络：`connector=P1 Header 15X2`；`spi=GPIO23,GPIO19,GPIO18`；`uart0=GPIO3,GPIO1`；`uart2=GPIO16,GPIO17`；`i2c=GPIO21,GPIO22`；`i2s=GPIO12,GPIO13,GPIO15,GPIO0,GPIO34`；`power=3.3V,5V,VBAT,HPWR,GND`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B3，P1 与 M5-Bus 定义表

## 总线地址

### IP5306 I2C 地址

原理图注释明确说明定制 IP5306 的 IIC 地址为 0x75，GPIO21 与 GPIO22 分别连接 SDA 与 SCL。

- 参数与网络：`address=0x75`；`sda=GPIO21`；`scl=GPIO22`
- 证据：图 91b865957940 / 第 1 页 / 网格 C2，CUSTOM IIC IP5306 注释

## GPIO 与控制信号

### 蓝色与红外 LED

GPIO19 经 R19 330R 驱动 LED1 BLUE_LED，GPIO17 经 R20 330R 驱动 LED2 IR_LED，两路 LED 另一端接地。

- 参数与网络：`blue=GPIO19,R19 330R`；`infrared=GPIO17,R20 330R`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右上，LED1/LED2

### Core 按键映射

S3、S2、S1 按下分别将 GPIO39、GPIO38、GPIO37 接地；S4 按下将 PWR 接地，各节点带上拉与钳位或 RC。

- 参数与网络：`button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`power=PWR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S4

## 时钟

### ESP32 40MHz 晶振

X1 标注 40MHz/+-10ppm/22pF，连接 ESP_XTAL_N/P，C21 与 C22 各为 22pF 接地。

- 参数与网络：`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22

## 保护电路

### M5-Bus 信号保护

P1 多路 GPIO、EN 与 EXT_SCK 配置 RLSD52A031V 阵列至 GND，EXT_SCK 经 R2 22R 到 GPIO18。

- 参数与网络：`array=RLSD52A031V`；`protected_signals=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34`；`series=EXT_SCK-R2 22R-GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-C1，R2 与 D2-D23

## 存储

### GD25Q32C SPI Flash

U2 标为 GD25Q32C，nCS、CLK、DI、DO、nWP、nHOLD 接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2。

- 参数与网络：`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0-SD_DATA3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2

### MicroSD-SPI 接口

U8 的 CS、DI、SCLK、DO 分别接 GPIO4、GPIO23、GPIO18、GPIO19；LCD 与 microSD 共用 GPIO23 MOSI 和 GPIO18 SCK。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19`；`shared_with_lcd=GPIO23,GPIO18`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI

## 音频

### GPIO26 晶体管扬声器

GPIO26 经 R21 330R 驱动 VT3 NPN-S8050，VT3 低端开关控制接 VCC_3V3 的 LS1 DET402-G-1。

- 参数与网络：`control=GPIO26`；`base_resistor=R21 330R`；`transistor=VT3 NPN-S8050`；`load=LS1 DET402-G-1`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右上，GPIO26/R21/VT3/LS1

### NS4148 差分功放

U9 INP 经 C43 100nF 接 GPIO25，INN 经 C44 100nF 接 PGND，VCC 与 CTRL 接 AMP_PWR，VOP/VON 经 FB1/FB2 形成 AUDIO_OUT_P/N。

- 参数与网络：`part_number=NS4148`；`input=GPIO25`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`ferrite_beads=FB1/FB2 600R@100M`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9/FB1/FB2

## 传感器

### 可选 MPU9250

U8 MPU9250 被红框标为 Optional For Gray Version，SCL/SDA 接 GPIO21/GPIO22，VDD/VDDIO 接 VCC_3V3，AD0/SDO 接地，其余多路标 NC。

- 参数与网络：`status=Optional For Gray Version`；`scl=GPIO21`；`sda=GPIO22`；`supply=VCC_3V3`；`address_strap=AD0/SDO=GND`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右下红框，U8 MPU9250

## 射频

### ESP_LNA 天线匹配

ESP_LNA 经 L1、C1、C9 匹配位连接 ANT1，三个元件值均标 TBD。

- 参数与网络：`antenna=ANT1`；`matching=L1/C1/C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/L1/C1/C9

## 调试与烧录

### CP2104 USB-UART

U3 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD/RXD 接 GPIO3/GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`part_number=CP2104`；`usb=USB_DP,USB_DN`；`uart=GPIO3,GPIO1`；`control=RTS,DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104

### 自动下载电路

DTR 与 RTS 通过 R16、R19 12K 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0。

- 参数与网络：`inputs=DTR,RTS`；`outputs=EN,GPIO0`；`base_resistors=R16/R19 12K`；`transistors=NPN-S8050 x2`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B2，DTR/RTS 自动下载支路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 单页资源架构 | `soc=ESP32-WROOM32`；`display=ZJY-6428TSW0G01`；`speaker=GPIO26`；`blue_led=GPIO19`；`ir_led=GPIO17`；`optional_sensor=MPU9250` |
| 核心器件 | ESP32-WROOM32 单页主控 | `reference=U1 [aux]`；`part_number=ESP32-WROOM32`；`supply=VCC_3V3`；`uart=TXD0,RXD0`；`sdio=NC` |
| 接口 | ZJY-6428TSW0G01 显示接口 | `cs=GPIO14`；`reset=GPIO33`；`dc=GPIO27`；`clock=GPIO18`；`data=GPIO23`；`logic_supply=VCC_3V3`；`panel_supply=VCC_9V` |
| 音频 | GPIO26 晶体管扬声器 | `control=GPIO26`；`base_resistor=R21 330R`；`transistor=VT3 NPN-S8050`；`load=LS1 DET402-G-1` |
| GPIO 与控制信号 | 蓝色与红外 LED | `blue=GPIO19,R19 330R`；`infrared=GPIO17,R20 330R` |
| 传感器 | 可选 MPU9250 | `status=Optional For Gray Version`；`scl=GPIO21`；`sda=GPIO22`；`supply=VCC_3V3`；`address_strap=AD0/SDO=GND` |
| 系统结构 | 六页 Core 图来源版本 | `design=M5 STACK CORE`；`revision=A13/A`；`dates=10/11/2017,2017/12/6` |
| 系统结构 | 六页 Core 功能分区 | `pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio` |
| 核心器件 | ESP32-D0WDQ6 | `reference=U1 [core]`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0-SD_DATA3` |
| 存储 | GD25Q32C SPI Flash | `part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0-SD_DATA3` |
| 时钟 | ESP32 40MHz 晶振 | `frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF` |
| 射频 | ESP_LNA 天线匹配 | `antenna=ANT1`；`matching=L1/C1/C9 TBD` |
| 电源 | EA3036 三路电源 | `input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`feedback=510K/110K` |
| 电源 | AMP_PWR 关闭测试点 | `enable=EN3`；`pullup=R23 10K`；`test_break=T1 0R` |
| 电源 | IP5306 电源管理 | `input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`annotation=5V 2.4A Sync Boost / 2.1A Sync Buck Charger` |
| 总线地址 | IP5306 I2C 地址 | `address=0x75`；`sda=GPIO21`；`scl=GPIO22` |
| 接口 | 六页 Core USB 电路 | `fuse=FUSE1 2A`；`data_series=R9/R11 22R`；`cc_pulldown=R6/R7 5.10K`；`protection=D1/D2` |
| 调试与烧录 | CP2104 USB-UART | `part_number=CP2104`；`usb=USB_DP,USB_DN`；`uart=GPIO3,GPIO1`；`control=RTS,DTR` |
| 调试与烧录 | 自动下载电路 | `inputs=DTR,RTS`；`outputs=EN,GPIO0`；`base_resistors=R16/R19 12K`；`transistors=NPN-S8050 x2` |
| GPIO 与控制信号 | Core 按键映射 | `button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`power=PWR` |
| 接口 | M5-LCD SPI 接口 | `reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14`；`backlight=GPIO32` |
| 存储 | MicroSD-SPI 接口 | `cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19`；`shared_with_lcd=GPIO23,GPIO18` |
| 总线 | 30 针 M5-Bus | `connector=P1 Header 15X2`；`spi=GPIO23,GPIO19,GPIO18`；`uart0=GPIO3,GPIO1`；`uart2=GPIO16,GPIO17`；`i2c=GPIO21,GPIO22`；`i2s=GPIO12,GPIO13,GPIO15,GPIO0,GPIO34`；`power=3.3V,5V,VBAT,HPWR,GND` |
| 保护电路 | M5-Bus 信号保护 | `array=RLSD52A031V`；`protected_signals=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34`；`series=EXT_SCK-R2 22R-GPIO18` |
| 音频 | NS4148 差分功放 | `part_number=NS4148`；`input=GPIO25`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`ferrite_beads=FB1/FB2 600R@100M` |
| 系统结构 | 资源与 K006-V26 的版本关系 | `target=M5GO IoT Kit v2.6 / K006-V26`；`aux_page=ESP32-WROOM32,GPIO26,MPU9250`；`core_pages=ESP32-D0WDQ6,GPIO25,GD25Q32C,CP2104` |
| 核心器件 | v2.6 主控版本 | `source_document=ESP32-D0WDQ6-V3`；`aux_page=ESP32-WROOM32`；`core_page=ESP32-D0WDQ6` |
| 存储 | v2.6 16MB Flash | `source_document=16MB Flash`；`aux_page=external flash not shown`；`core_page=GD25Q32C` |
| 调试与烧录 | v2.6 CH9102F USB-UART | `source_document=CH9102F`；`version_change=CP2104 -> CH9102`；`core_page=CP2104`；`aux_page=USB-UART absent` |
| 接口 | v2.6 USB Type-C 接口 | `source_document=USB Type-C`；`section_title=Type-C`；`symbol_value=USB_Micro`；`cc_pulldown=5.10K x2` |
| 核心器件 | v2.6 LCD 控制器与面板 | `source_document=2 inch 320x240 IPS ILI9342C`；`aux_page=ZJY-6428TSW0G01`；`core_page=M5-LCD` |
| 传感器 | v2.6 MPU6886 与取消 BMM150 | `source_document=MPU6886`；`version_change=BMM150 removed`；`aux_page=Optional MPU9250 for Gray`；`core_pages=sensor page absent` |
| 系统结构 | v2.6 M5GO 底座外设 | `microphone=BSE3729 on GPIO34`；`rgb=10x SK6812 on GPIO15`；`ports=A I2C,B GPIO,C UART`；`schematics=base circuits absent` |
| 电源 | v2.6 500mAh 电池 | `source_document=3.7V 500mAh`；`history=600mAh -> 500mAh`；`schematic=IP5306/VBAT only` |
| 音频 | v2.6 扬声器规格与拓扑 | `source_document=1W-0928`；`aux_page=GPIO26 S8050/DET402-G-1`；`core_page=GPIO25 NS4148/AUDIO_OUT_P/N` |
| 电源 | v2.6 IP5306 电源管理 | `source_document=IP5306 0x75`；`core_page=custom IIC IP5306 0x75`；`applicability=K006-V26 unverified` |
| 系统结构 | v2.6 套件扩展单元 | `source_document=ENV-III,PIR,Angle,IR,RGB,Hub`；`version_change=ENV Unit -> ENV-III`；`schematics=unit circuits absent` |
| 系统结构 | v2.6 主频与无线规格 | `source_document=dual-core 240MHz,2.4GHz Wi-Fi`；`schematic=ESP32 and antenna path` |

## 待确认事项

- `system.resource-version-relationship`：单页图使用 ESP32-WROOM32、GPIO26 扬声器与可选 MPU9250，六页图使用 ESP32-D0WDQ6、GPIO25 NS4148、GD25Q32C 与 CP2104；两套图均未标 M5GO IoT Kit v2.6 或 K006-V26，无法确认它们对 v2.6 量产硬件的适用范围。（证据：图 87dd78652b8f / 第 1 页 / 单页整图; 图 a44d9e10f49e / 第 1 页 / M5 STACK CORE 封面与 2017 修订记录）
- `component.v26-soc`：产品源文档标注 ESP32-D0WDQ6-V3，单页图标 ESP32-WROOM32，六页图标 ESP32-D0WDQ6；K006-V26 量产硬件的主控封装与版本无法由现有图确认。（证据：图 87dd78652b8f / 第 1 页 / U1 ESP32-WROOM32; 图 d81402da2106 / 第 1 页 / U1 ESP32-D0WDQ6）
- `storage.v26-flash`：产品源文档标注 16MB Flash，单页图未显示独立 Flash，六页图使用 GD25Q32C；K006-V26 的 16MB Flash 具体器件与连接无法由现有图确认。（证据：图 87dd78652b8f / 第 1 页 / U1 ESP32-WROOM32，未画独立 Flash; 图 d81402da2106 / 第 1 页 / U2 GD25Q32C）
- `debug.v26-usb-uart`：产品源文档规格标注 CH9102F，版本记录说明 v2.6 将 CP2104 更改为 CH9102；六页图只显示 CP2104，单页图未画 USB-UART，因此 v2.6 的 CH9102F 电路无法由现有图确认。（证据：图 2f5b17c1e346 / 第 1 页 / U3 CP2104; 图 87dd78652b8f / 第 1 页 / 单页未画 USB-UART）
- `interface.v26-usb-connector`：产品源文档标注 USB Type-C；六页图 USB 分区标题写 Type-C 且画出 CC1/CC2 下拉，但连接器 U5 的器件值标为 USB_Micro，图面内部标记及其与 v2.6 的对应关系需确认。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 A4，Type-C 标题、U5 USB_Micro、CC1/CC2）
- `component.v26-display`：产品源文档标注 2 英寸 320x240 IPS ILI9342C，单页图标 ZJY-6428TSW0G01，六页图仅标 M5-LCD；K006-V26 的 LCD 控制器和面板版本无法由现有图确认。（证据：图 87dd78652b8f / 第 1 页 / U2 ZJY-6428TSW0G01; 图 2f5b17c1e346 / 第 1 页 / U6 M5-LCD）
- `sensor.v26-imu`：产品源文档规格标注 6 轴 MPU6886，版本记录说明 v2.6 取消 BMM150；单页图只画 Optional For Gray Version 的 MPU9250，六页 Core 图目录没有传感器页，因此 MPU6886 电路及 BMM150 取消状态无法由现有图确认。（证据：图 87dd78652b8f / 第 1 页 / Optional For Gray Version U8 MPU9250; 图 a44d9e10f49e / 第 1 页 / 六页目录不含传感器页）
- `system.v26-base`：产品源文档描述 GPIO15 的 10 颗 SK6812、GPIO34 的 BSE3729 麦克风和 Port A/B/C；七张资源均未显示这些 M5GO 底座电路，无法确认其器件连接和供电。（证据：图 87dd78652b8f / 第 1 页 / 单页无麦克风与 RGB 灯条; 图 72aa5b4d2f89 / 第 1 页 / Core 图仅给出 M5-Bus）
- `power.v26-battery`：产品源文档标注 3.7V 500mAh，并记录 600mAh 至 500mAh 的历史变更；原理图只显示 IP5306、VBAT 与 M5-Bus 电池网络，未标容量、料号或保护参数。（证据：图 91b865957940 / 第 1 页 / U10 IP5306 与 VBAT; 图 72aa5b4d2f89 / 第 1 页 / P1 pin 30 VBAT）
- `audio.v26-speaker`：产品源文档标注 1W-0928，单页图画 GPIO26、S8050 与 DET402-G-1，六页图画 GPIO25、NS4148 与差分输出；K006-V26 的实际拓扑、阻抗和额定条件无法由现有图确认。（证据：图 87dd78652b8f / 第 1 页 / GPIO26/VT3/LS1; 图 8d7498c3a5a7 / 第 1 页 / U9 NS4148/AUDIO_OUT_P/N）
- `power.v26-ip5306`：产品源文档管脚映射标注 IP5306 地址 0x75，六页 2017 Core 图也显示定制 IP5306 0x75；由于六页图未标 K006-V26，无法确认该电源拓扑在 v2.6 上是否保持不变。（证据：图 91b865957940 / 第 1 页 / U10 IP5306 与 0x75 注释; 图 a44d9e10f49e / 第 1 页 / M5 STACK CORE 2017 封面）
- `system.v26-kit-units`：产品源文档列出 ENV-III、PIR、Angle、IR、RGB 与 Hub 六个 Unit，并记录 v2.6 将 ENV Unit 更改为 ENV-III；现有七张资源只覆盖早期 M5GO/Core，不包含这些 Unit 的电路，无法从原理图核对套件版本。（证据：图 87dd78652b8f / 第 1 页 / 单页仅覆盖 Core 相关电路; 图 a44d9e10f49e / 第 1 页 / 六页目录不含 Unit 电路）
- `system.v26-operating-specs`：产品源文档标注双核 240MHz 与 2.4GHz Wi-Fi；图面显示 ESP32 器件和天线路径，但未直接给出运行主频或无线协议参数，且硬件版本适用性未确认。（证据：图 d81402da2106 / 第 1 页 / U1 ESP32-D0WDQ6 与 ANT1 路径）
- `review.resource-version-relationship`：早期单页 M5GO 电路与 2017 Core 六页图分别对应哪一版硬件，它们对 K006-V26 的适用范围是什么？；原因：两套图的主控、Flash、USB-UART、扬声器与传感器拓扑不同，且均未标 M5GO IoT Kit v2.6 或 K006-V26。
- `review.v26-soc`：K006-V26 量产主控是 ESP32-D0WDQ6-V3、ESP32-D0WDQ6 还是 ESP32-WROOM32 模组？；原因：产品源文档与两套原理图的器件标记不一致。
- `review.v26-flash`：K006-V26 的 16MB Flash 具体器件、容量标记和连接是什么？；原因：六页图只显示 GD25Q32C，单页图未显示独立 Flash。
- `review.v26-usb-uart`：K006-V26 的 CH9102F USB-UART 原理图和自动下载连接是什么？；原因：产品页说明 v2.6 改为 CH9102，现有资源只显示 CP2104。
- `review.v26-usb-connector`：六页图 Type-C 标题与 U5 USB_Micro 器件值的冲突如何解释，哪一接口实现适用于 K006-V26？；原因：图面内部标记不一致，且未标目标产品版本。
- `review.v26-display`：K006-V26 是否使用 ILI9342C 320x240 IPS，ZJY-6428TSW0G01 与 M5-LCD 各对应什么硬件版本？；原因：产品源文档与两套图的显示标记不同。
- `review.v26-imu`：K006-V26 的 MPU6886 电路在哪里，BMM150 是否确已从该版本硬件移除？；原因：现有单页只画 Gray 版本可选 MPU9250，六页图没有传感器页。
- `review.v26-base`：K006-V26 底座的 BSE3729、10 颗 SK6812 和 Port A/B/C 的完整电路、供电与保护是什么？；原因：七张资源均未显示产品页所述底座电路。
- `review.v26-battery`：K006-V26 电池是否为 3.7V 500mAh，其料号、保护参数和底座连接是什么？；原因：原理图仅显示 VBAT 网络，未标电池容量或料号。
- `review.v26-speaker`：K006-V26 使用 GPIO26 晶体管扬声器还是 GPIO25 NS4148，1W-0928 的阻抗和额定条件是什么？；原因：产品源文档与两套图的扬声器标记和拓扑不同。
- `review.v26-ip5306`：2017 Core 图中的 IP5306 0x75 电源拓扑是否原样适用于 K006-V26？；原因：产品页与旧图均提到 IP5306 0x75，但旧图未标 K006-V26。
- `review.v26-kit-units`：K006-V26 套件是否固定包含 ENV-III、PIR、Angle、IR、RGB 和 Hub，其各自硬件版本是什么？；原因：产品源文档列出套件内容，但当前原理图资源不包含六个 Unit。
- `review.v26-operating-specs`：K006-V26 的量产配置是否确认为双核 240MHz 和 2.4GHz Wi-Fi？；原因：这些参数来自产品源文档，现有原理图未直接给出且版本关系未确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `87dd78652b8ffd0385aeedaeb82945065e88b8e1c870367a302911adf0fac712` | `https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_sch_01.webp` |
| 2 | 1 | `a44d9e10f49eba739a7d1b57e10ddb75ee06740af6339dda71801119e0ff3e95` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_01.png` |
| 3 | 1 | `91b865957940b7595eb4abcbb1d34ab61b82753b0035267d860ef1a3cfd453bb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_02.png` |
| 4 | 1 | `d81402da2106664255e50b82ad9e519d7f0f6b1844ddefc24b5aecc28a7ccdbf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_03.png` |
| 5 | 1 | `2f5b17c1e346f2498049eb882140037528b100afbf6854879dbc91605c44a0f6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_04.png` |
| 6 | 1 | `72aa5b4d2f89ab1e81f41d1b5916bfa3b7a527a19c21ca6ee946c882f6d8ce5c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_05.png` |
| 7 | 1 | `8d7498c3a5a7fd1010952eda7a2742715f09a8abc789055f9d1e77f7900af32f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_06.png` |

---

源文档：`zh_CN/core/m5go_v2.6.md`

源文档 SHA-256：`0d96d106342208d71db827f3dfe6e4cc56a4cbc16235fe8fbf8b1e88386dadf3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
