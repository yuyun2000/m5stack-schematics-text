# M5GO IoT Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5GO IoT Kit |
| SKU | K006 |
| 产品 ID | `m5go-iot-kit-7548fd87ca51` |
| 源文档 | `zh_CN/core/m5go.md` |

## 概述

M5GO IoT Kit 清单包含一张早期单页电路和 2017 年 M5 STACK CORE Rev A 六页电路。单页画出 ESP32-WROOM32、ZJY-6428TSW0G01 显示接口、GPIO26 晶体管扬声器、蓝/红外 LED 以及标为 Optional For Gray Version 的 MPU9250；六页 Core 图则以 ESP32-D0WDQ6、GD25Q32C、EA3036、IP5306、CP2104、M5-LCD、microSD、M5-Bus 和 NS4148 构成另一套核心架构。当前产品页声明 ESP32-D0WDQ6-V3、16MB Flash、MPU6886+BMM150、M5GO 底座麦克风/10颗 RGB LED/500mAh 电池，但这些与两套图并不完全一致，因此版本关系和底座功能单列为待确认。

## 检索关键词

`M5GO IoT Kit`、`K006`、`M5GO`、`ESP32-WROOM32`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`ZJY-6428TSW0G01`、`MPU9250`、`MPU6886`、`BMM150`、`GD25Q32C`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`CH9102`、`NS4148`、`ILI9342C`、`BSE3729`、`SK6812`、`M5-Bus`、`USB Type-C`、`MicroSD-SPI`、`GPIO15`、`GPIO17`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO26`、`GPIO34`、`VCC_3V3`、`VCC_5V`、`VDD_3V3`、`AMP_PWR`、`VBAT`、`AUDIO_OUT_P`、`AUDIO_OUT_N`、`40MHz`、`SPI`、`I2C`、`UART`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 [aux] | ESP32-WROOM32 | 单页资源中的 ESP32 模组，连接显示、LED、扬声器和可选 MPU9250 | 图 87dd78652b8f / 第 1 页 / 页面左上，U1 ESP32-WROOM32 |
| U2 [aux] | ZJY-6428TSW0G01 | 单页资源中的显示模组接口，连接 SPI 控制和双电源 | 图 87dd78652b8f / 第 1 页 / 页面左下，U2 ZJY-6428TSW0G01 |
| LS1,VT3 [aux] | DET402-G-1 / NPN-S8050 | GPIO26 控制的晶体管扬声器支路 | 图 87dd78652b8f / 第 1 页 / 页面右上，GPIO26/R21/VT3/LS1 |
| LED1,LED2 [aux] | BLUE_LED / IR_LED | GPIO19 蓝色 LED 与 GPIO17 红外 LED | 图 87dd78652b8f / 第 1 页 / 页面右上，LED1/LED2/R19/R20 |
| U8 [aux] | MPU9250 | 标为 Optional For Gray Version 的 I2C 九轴传感器位 | 图 87dd78652b8f / 第 1 页 / 页面右下红框 Optional For Gray Version，U8 MPU9250 |
| U1 [core] | ESP32-D0WDQ6 | 六页 Core 图主控 SoC | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 |
| U2 [core] | GD25Q32C | 六页 Core 图外部 SPI Flash | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| X1 [core] | 40MHz/+-10ppm/22pF | ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22 |
| ANT1 [core] | 未标注 | ESP_LNA 射频天线端与匹配位 | 图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/ESP_LNA |
| U4 [core] | EA3036 | VCC_5V 至三路 3.3V 电源的同步降压转换器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 |
| U10 [core] | IP5306 | USB、电池和 5V 电源管理器，定制 I2C 地址 0x75 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 |
| U3 [core] | CP2104 | USB 转 UART 与自动下载信号源 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 [core] | USB_Micro | Type-C USB 分区中的连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5/FUSE1/D1/D2 |
| U6 [core] | M5-LCD | LCD 模组接口 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD |
| U8 [core] | MicroSD-SPI | SPI microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1,S2,S3,S4 [core] | SMT-3x6-SWC / SMT_SW_TS_015 | 三个用户按键与 PWR 按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S4 |
| P1 [core] | Header 15X2 | 30 针 M5-Bus | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| U9 [core] | NS4148 | GPIO25 输入的差分 D 类功放 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 |
| FET1 [core] | AO3402 | GPIO32 控制的 LCD 背光开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1 AO3402 |

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

U1 标为 ESP32-WROOM32，VCC_3V3 接 3V3，EN、TXD0/RXD0 和 GPIO0~39 多路引出，SD0~SD3/CMD/CLK 标未连接。

- 参数与网络：`reference=U1 [aux]`；`part_number=ESP32-WROOM32`；`supply=VCC_3V3`；`uart=TXD0,RXD0`；`sdio=NC`
- 证据：图 87dd78652b8f / 第 1 页 / 页面左上，U1 ESP32-WROOM32

### ESP32-D0WDQ6

六页 Core 图 U1 标为 ESP32-D0WDQ6，CHIP_PU 接 EN，RF 接 ESP_LNA，Flash 接 SD_CMD/SD_CLK/SD_DATA0~3。

- 参数与网络：`reference=U1 [core]`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1

## 电源

### EA3036 三路电源

U4 EA3036 以 VCC_5V 供电，SW1/SW2/SW3 经 L2/L3/L5 输出 VCC_3V3、VDD_3V3、AMP_PWR，反馈均为 510K/110K。

- 参数与网络：`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`feedback=510K/110K`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4

### AMP_PWR 关闭测试点

EA3036 EN3 由 R23 10K 上拉，T1 为接地 0R 测试断点，图面标注用于关闭功放。

- 参数与网络：`enable=EN3`；`pullup=10K`；`test_break=T1 0R`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1，T1/R23

### IP5306 电源管理

U10 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY，图面标注 5V 2.4A Sync Boost 与 2.1A Sync Buck Charger。

- 参数与网络：`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10

## 接口

### ZJY-6428TSW0G01 显示接口

U2 CS/RES/DC/D0/D1 分别连接 GPIO14、GPIO33、GPIO27、GPIO18、GPIO23，VDD 接 VCC_3V3，VPP/VCOMH 电源网络另接 VCC_9V 与滤波电容。

- 参数与网络：`cs=GPIO14`；`reset=GPIO33`；`dc=GPIO27`；`clock=GPIO18`；`data=GPIO23`；`logic_supply=VCC_3V3`；`panel_supply=VCC_9V`
- 证据：图 87dd78652b8f / 第 1 页 / 页面左下，U2 与 C3-C5/R2

### USB 电源与数据

U5 VCC 经 FUSE1 2A 接 VIN_USB，D-/D+ 经 R9/R11 22R 接 USB_DN/USB_DP，并由 D1/D2 保护；USB_CC_1/2 各以 5.10K 接地。

- 参数与网络：`fuse=2A`；`data=USB_DN/USB_DP`；`series=22R`；`cc=2x 5.10K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，USB 分区

### M5-LCD SPI

U6 #RST、R/S、MOSI、SCK、CS 接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14；背光由 GPIO32 控制 FET1 AO3402。

- 参数与网络：`reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14`；`backlight=GPIO32`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6/FET1

## 总线

### 30 针 M5-Bus

P1 引出 GND、GPIO35/36、EN、GPIO23/25、GPIO19/26、GPIO18、3.3V、GPIO3/1、GPIO16/17、GPIO21/22、GPIO2/5、GPIO12/13、GPIO15/0、HPWR、GPIO34、5V 与 VBAT。

- 参数与网络：`spi=GPIO23/19/18`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22`；`i2s=GPIO12/13/15/0/34`；`power=3V3,HPWR,5V,VBAT`
- 证据：图 72aa5b4d2f89 / 第 1 页 / P1 pins1-30 与功能表

## 总线地址

### IP5306 I2C 地址

原理图注释明确说明定制 IP5306 IIC 地址为 0x75，GPIO21/GPIO22 为 SDA/SCL。

- 参数与网络：`address=0x75`；`sda=GPIO21`；`scl=GPIO22`
- 证据：图 91b865957940 / 第 1 页 / 0x75 注释; 图 72aa5b4d2f89 / 第 1 页 / GPIO21 SDA/GPIO22 SCL

## GPIO 与控制信号

### 蓝色与红外 LED

GPIO19 经 R19 330R 驱动 LED1 BLUE_LED，GPIO17 经 R20 330R 驱动 LED2 IR_LED，两路 LED 另一端接地。

- 参数与网络：`blue=GPIO19,R19 330R`；`infrared=GPIO17,R20 330R`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右上，LED1/LED2

### 用户与电源按键

S3/S2/S1 按下分别将 GPIO39/GPIO38/GPIO37 接地；S4 按下将 PWR 接地，各节点有上拉与钳位/RC。

- 参数与网络：`button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`power=PWR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S4

## 时钟

### ESP32 40MHz 晶振

X1 标注 40MHz/+-10ppm/22pF，连接 ESP_XTAL_N/P，C21/C22 各 22pF 接地。

- 参数与网络：`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22

## 保护电路

### M5-Bus 信号保护

P1 多路 GPIO/EN/EXT_SCK 配置 RLSD52A031V 阵列至 GND，EXT_SCK 经 R2 22R 到 GPIO18。

- 参数与网络：`device=RLSD52A031V`；`series=R2 22R`
- 证据：图 72aa5b4d2f89 / 第 1 页 / D2-D23/R2

## 存储

### GD25Q32C SPI Flash

U2 标为 GD25Q32C，nCS/CLK/DI/DO/nWP/nHOLD 接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2。

- 参数与网络：`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2

### microSD SPI

U8 CS、DI、SCLK、DO 对应 GPIO4、GPIO23、GPIO18、GPIO19；LCD 与 microSD 共用 GPIO23 MOSI 与 GPIO18 SCK。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 C1-D2，U8 与 SPI 保护网络

## 音频

### GPIO26 晶体管扬声器

GPIO26 经 R21 330R 驱动 VT3 NPN-S8050，VT3 低端开关控制接 VCC_3V3 的 LS1 DET402-G-1。

- 参数与网络：`control=GPIO26`；`base_resistor=R21 330R`；`transistor=VT3 NPN-S8050`；`load=LS1 DET402-G-1`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右上，GPIO26/R21/VT3/LS1

### NS4148 功放

U9 INP 经 C43 接 GPIO25，VCC/CTRL 接 AMP_PWR，VOP/VON 经 FB1/FB2 形成 AUDIO_OUT_P/N。

- 参数与网络：`input=GPIO25`；`supply=AMP_PWR`；`output=AUDIO_OUT_P/N`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9/FB1/FB2

## 传感器

### 可选 MPU9250

U8 MPU9250 被红框标为 Optional For Gray Version，SCL/SDA 接 GPIO21/GPIO22，VDD/VDDIO 接 VCC_3V3，AD0/SDO 接地，其余多路标 NC。

- 参数与网络：`status=Optional For Gray Version`；`scl=GPIO21`；`sda=GPIO22`；`supply=VCC_3V3`；`address_strap=AD0/SDO=GND`
- 证据：图 87dd78652b8f / 第 1 页 / 页面右下红框，U8 MPU9250

## 射频

### ESP_LNA 天线匹配

ESP_LNA 经 L1/C1/C9 匹配位连接 ANT1，元件值均标 TBD。

- 参数与网络：`antenna=ANT1`；`matching=L1/C1/C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/L1/C1/C9

## 调试与烧录

### CP2104 USB-UART

U3 CP2104 DP/DM 接 USB_DP/USB_DN，TXD/RXD 接 GPIO3/GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`part=CP2104`；`uart=GPIO3/GPIO1`；`control=RTS/DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3

### 自动下载

DTR/RTS 通过 R16/R19 12K 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0。

- 参数与网络：`inputs=DTR/RTS`；`outputs=EN/GPIO0`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D2-D3，Auto-Download

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
| 核心器件 | ESP32-D0WDQ6 | `reference=U1 [core]`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3` |
| 存储 | GD25Q32C SPI Flash | `part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3` |
| 时钟 | ESP32 40MHz 晶振 | `frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF` |
| 射频 | ESP_LNA 天线匹配 | `antenna=ANT1`；`matching=L1/C1/C9 TBD` |
| 电源 | EA3036 三路电源 | `input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`feedback=510K/110K` |
| 电源 | AMP_PWR 关闭测试点 | `enable=EN3`；`pullup=10K`；`test_break=T1 0R` |
| 电源 | IP5306 电源管理 | `input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY` |
| 总线地址 | IP5306 I2C 地址 | `address=0x75`；`sda=GPIO21`；`scl=GPIO22` |
| 接口 | USB 电源与数据 | `fuse=2A`；`data=USB_DN/USB_DP`；`series=22R`；`cc=2x 5.10K` |
| 调试与烧录 | CP2104 USB-UART | `part=CP2104`；`uart=GPIO3/GPIO1`；`control=RTS/DTR` |
| 调试与烧录 | 自动下载 | `inputs=DTR/RTS`；`outputs=EN/GPIO0` |
| GPIO 与控制信号 | 用户与电源按键 | `button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`power=PWR` |
| 接口 | M5-LCD SPI | `reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14`；`backlight=GPIO32` |
| 存储 | microSD SPI | `cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19` |
| 总线 | 30 针 M5-Bus | `spi=GPIO23/19/18`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22`；`i2s=GPIO12/13/15/0/34`；`power=3V3,HPWR,5V,VBAT` |
| 保护电路 | M5-Bus 信号保护 | `device=RLSD52A031V`；`series=R2 22R` |
| 音频 | NS4148 功放 | `input=GPIO25`；`supply=AMP_PWR`；`output=AUDIO_OUT_P/N` |
| 系统结构 | 单页图、Core 六页图与当前 M5GO 的关系 | `aux_page=ESP32-WROOM32/GPIO26/MPU9250 option`；`core_pages=ESP32-D0WDQ6/GPIO25 NS4148/GD25Q32C`；`target=M5GO IoT Kit K006` |
| 核心器件 | M5GO 当前 SoC | `source_document=ESP32-D0WDQ6-V3`；`aux_page=ESP32-WROOM32`；`core_page=ESP32-D0WDQ6` |
| 存储 | M5GO 16MB Flash | `source_document=16MB`；`aux_page=no discrete Flash`；`core_page=GD25Q32C` |
| 调试与烧录 | M5GO USB-TTL 版本 | `source_document=CP2104 or CH9102`；`core_page=CP2104` |
| 核心器件 | M5GO LCD 控制器 | `source_document=ILI9342C 320x240 IPS`；`aux_page=ZJY-6428TSW0G01`；`core_page=M5-LCD` |
| 传感器 | M5GO MPU6886 与 BMM150 | `source_document=MPU6886 0x68,BMM150 0x10`；`aux_page=optional MPU9250 for Gray`；`core_pages=sensors absent` |
| 系统结构 | M5GO 底座外设 | `microphone=BSE3729 on GPIO34`；`rgb=10x SK6812 on GPIO15`；`ports=A I2C,B GPIO,C UART`；`charging=magnetic charging base` |
| 电源 | M5GO 500mAh 电池 | `source_document=3.7V 500mAh`；`history=600mAh -> 500mAh`；`schematic=IP5306/VBAT` |
| 音频 | M5GO 扬声器规格与拓扑 | `source_document=1W-0928`；`aux_page=GPIO26 S8050/DET402-G-1`；`core_page=GPIO25 NS4148` |
| 存储 | microSD 最大容量 | `source_document=16GB max`；`schematic=MicroSD-SPI` |
| 系统结构 | M5GO 主频与 Wi-Fi | `cpu=240MHz`；`wifi=2.4GHz`；`schematic=ESP32 and antenna path` |

## 待确认事项

- `system.resource-version-relationship`：单页图使用 ESP32-WROOM32、GPIO26 扬声器与可选 MPU9250，六页图使用 ESP32-D0WDQ6、GPIO25 NS4148 与 GD25Q32C；两套图均未标 M5GO/K006，当前产品版本对应关系需确认。（证据：图 87dd78652b8f / 第 1 页 / 单页整图; 图 a44d9e10f49e / 第 1 页 / M5 STACK CORE 封面）
- `component.current-soc`：产品源文档标注 ESP32-D0WDQ6-V3，单页图标 ESP32-WROOM32，六页图标 ESP32-D0WDQ6；当前量产 M5GO 的 SoC/模组版本需确认。（证据：图 87dd78652b8f / 第 1 页 / U1 ESP32-WROOM32; 图 d81402da2106 / 第 1 页 / U1 ESP32-D0WDQ6）
- `storage.current-flash`：产品源文档标注 16MB Flash，单页图未显示独立 Flash，六页图使用 GD25Q32C；当前 16MB 器件与连接需确认。（证据：图 87dd78652b8f / 第 1 页 / ESP32-WROOM32 页无独立 Flash; 图 d81402da2106 / 第 1 页 / U2 GD25Q32C）
- `debug.current-usb-uart`：产品源文档说明存在 CP2104 与 CH9102 版本，六页图只显示 CP2104，单页图没有 USB-UART；目标硬件版本需确认。（证据：图 2f5b17c1e346 / 第 1 页 / U3 CP2104）
- `component.current-display`：产品源文档标注 ILI9342C 320x240 IPS，单页图标 ZJY-6428TSW0G01，六页图仅标 M5-LCD；控制器与面板版本需确认。（证据：图 87dd78652b8f / 第 1 页 / U2 ZJY-6428TSW0G01; 图 2f5b17c1e346 / 第 1 页 / U6 M5-LCD）
- `sensor.current-imu`：产品源文档标注 MPU6886 0x68 与 BMM150 0x10，单页图只画 Optional For Gray Version 的 MPU9250，六页图没有传感器页；当前传感器电路需确认。（证据：图 87dd78652b8f / 第 1 页 / Optional For Gray Version U8 MPU9250; 图 a44d9e10f49e / 第 1 页 / 六页目录不含传感器页）
- `system.m5go-base`：产品源文档描述 BSE3729 麦克风、GPIO15 的 10颗 SK6812、Port A/B/C、磁吸充电与底座电池；七张资源均未显示这些 M5GO 底座电路。（证据：图 87dd78652b8f / 第 1 页 / 单页无麦克风/LED条/充电底座; 图 72aa5b4d2f89 / 第 1 页 / Core 图仅给 M5-Bus）
- `power.current-battery`：产品源文档标注 3.7V 500mAh 并记录 600mAh 至 500mAh 变更；原理图只显示 IP5306/VBAT 与 M5-Bus 电池网络，没有容量或料号。（证据：图 91b865957940 / 第 1 页 / IP5306/VBAT）
- `audio.current-speaker`：产品源文档标注 1W-0928，单页图画 GPIO26 晶体管扬声器，六页图画 GPIO25 NS4148 差分功放；当前量产拓扑与扬声器参数需确认。（证据：图 87dd78652b8f / 第 1 页 / GPIO26/VT3/LS1; 图 8d7498c3a5a7 / 第 1 页 / U9 NS4148）
- `storage.microsd-limit`：产品源文档称 microSD 最大支持 16GB，原理图只显示 SPI 卡座与信号，未标介质容量或文件系统限制。（证据：图 2f5b17c1e346 / 第 1 页 / U8 MicroSD-SPI）
- `system.operating-specs`：产品源文档标注 240MHz 与 2.4GHz Wi-Fi，图面显示 ESP32 器件与天线路径，但未直接给出运行频率或无线协议参数。（证据：图 d81402da2106 / 第 1 页 / ESP32 与天线网络）
- `review.resource-relationship`：单页 ESP32-WROOM32 电路与 2017 Core 六页图分别对应哪一版 M5GO/K006 硬件？；原因：两套图的主控、扬声器与传感器拓扑不同，且均未标 M5GO/K006。
- `review.current-soc`：M5GO 当前量产主控是 ESP32-D0WDQ6-V3、ESP32-D0WDQ6 还是 ESP32-WROOM32 模组？；原因：产品页与两套图的标记不一致。
- `review.current-flash`：M5GO 16MB Flash 的具体器件与连接是什么？；原因：六页图为 GD25Q32C，单页图未画独立 Flash。
- `review.current-usb-uart`：目标 M5GO 硬件的 USB-TTL 是 CP2104 还是 CH9102？；原因：产品页说明存在两个版本，资源只显示 CP2104。
- `review.current-display`：M5GO 当前 LCD 是否为 ILI9342C 320x240 IPS，单页 ZJY-6428TSW0G01 与它是什么关系？；原因：两套图与产品页标记不同。
- `review.current-imu`：M5GO 当前是否使用 MPU6886 0x68 与 BMM150 0x10，其原理图在哪里？；原因：现有单页只画 Gray 可选 MPU9250，Core 六页无传感器。
- `review.m5go-base`：M5GO 底座的 BSE3729、10颗 SK6812、Port A/B/C、电池和磁吸充电电路是什么？；原因：七张资源均未显示产品页所述底座电路。
- `review.current-battery`：M5GO 当前电池是否为 3.7V 500mAh，具体料号和保护参数是什么？；原因：原理图未显示容量或料号。
- `review.current-speaker`：M5GO 当前使用 GPIO26 晶体管扬声器还是 GPIO25 NS4148，1W-0928 的阻抗与额定条件是什么？；原因：两套图的音频拓扑不同。
- `review.microsd-limit`：M5GO 的 16GB microSD 上限来自硬件、固件还是文件系统？；原因：原理图只显示 SPI 卡座。
- `review.operating-specs`：M5GO 量产固件主频与无线规格是否确认为 240MHz 和 2.4GHz Wi-Fi？；原因：参数来自产品页，原理图未直接给出。

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

源文档：`zh_CN/core/m5go.md`

源文档 SHA-256：`cafee0092e01f543f0eaaa5eb2d3e98012379809b4c2e3507b37bc8e57664d1f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
