# Gray 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Gray |
| SKU | K002 |
| 产品 ID | `gray-23b722c20e0c` |
| 源文档 | `zh_CN/core/gray.md` |

## 概述

Gray 清单关联的是 2017 年 M5 STACK CORE Rev A 六页电路：ESP32-D0WDQ6 配 GD25Q32C SPI Flash 与 40MHz 晶振，EA3036 从 5V 生成 VCC_3V3、VDD_3V3、AMP_PWR，IP5306 负责 USB、电池、5V 升压并以 0x75 接入 I2C；其余电路包含 CP2104 USB-UART、自动下载、三按键、LCD、microSD、30针 M5-Bus 和 NS4148 功放。Gray 产品页还声称 16MB Flash、MPU6886+BMM150、110mAh 电池和具体显示/扬声器规格，但六页没有 Gray/K002 或传感器页，且正文另写 4MB Flash，因此版本与容量差异均保留待确认。

## 检索关键词

`Gray`、`K002`、`M5 STACK CORE`、`Rev A`、`A13`、`ESP32-D0WDQ6`、`GD25Q32C`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`CH9102`、`NS4148`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`M5-Bus`、`MPU6886`、`0x68`、`BMM150`、`0x10`、`USB Type-C`、`USB_DP`、`USB_DN`、`VIN_USB`、`VCC_5V`、`VCC_3V3`、`VDD_3V3`、`AMP_PWR`、`VBAT`、`GPIO21`、`GPIO22`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO25`、`GPIO32`、`GPIO33`、`GPIO37`、`GPIO38`、`GPIO39`、`AUDIO_OUT_P`、`AUDIO_OUT_N`、`40MHz`、`SPI`、`I2C`、`UART`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 主控 SoC，连接 Flash、晶振、RF、LCD、microSD、按键、UART、音频与 M5-Bus | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 |
| U2 | GD25Q32C | ESP32 外部 SPI Flash | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| X1 | 40MHz/+-10ppm/22pF | ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22 |
| ANT1 | 未标注 | ESP_LNA 射频天线端与匹配位 | 图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/ESP_LNA/L1/C1/C9 |
| U4 | EA3036 | VCC_5V 至三路 3.3V 电源的同步降压转换器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 |
| U10 | IP5306 | USB 输入、电池充电和 5V 同步升压管理器，定制 I2C 地址 0x75 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 |
| U3 | CP2104 | USB 转 UART 与自动下载信号源 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 | USB_Micro | Type-C USB 分区中的 USB 电源与数据连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5/FUSE1/D1/D2 |
| U6 | M5-LCD | LCD 模组接口，包含背光、复位、寄存器选择和 SPI | 图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD |
| U8 | MicroSD-SPI | SPI microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1,S2,S3,S4 | SMT-3x6-SWC / SMT_SW_TS_015 | 三个 GPIO 用户按键与 PWR 按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S4 |
| P1 | Header 15X2 | 30 针 M5-Bus | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| U9 | NS4148 | GPIO25 模拟音频输入的差分 D 类功放 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 |
| FET1 | AO3402 | GPIO32 控制的 LCD 背光低端开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1 AO3402 |

## 系统结构

### 原理图来源版本

封面将六页设计标为 M5 STACK CORE，修订记录为 A13 OFFICIAL RELEASE VERSION，日期 10/11/2017，标题栏 Revision A、Date 2017/12/6。

- 参数与网络：`design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 A1-A3 修订表与 D3-D4 标题栏

### 六页功能分区

封面目录依次列出 COVER PAGE、POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINITION 和 AUDIO AMPLIFIER。

- 参数与网络：`pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 B3-C4，页面目录

## 核心器件

### ESP32-D0WDQ6

U1 明确标为 ESP32-D0WDQ6，CHIP_PU 接 EN，RF 接 ESP_LNA，外部 Flash 接 SD_CMD/SD_CLK/SD_DATA0~3。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1

## 电源

### EA3036 三路电源

U4 EA3036 以 VCC_5V 供电，SW1/SW2/SW3 经 L2/L3/L5 输出 VCC_3V3、VDD_3V3、AMP_PWR；三路反馈为 510K/110K。

- 参数与网络：`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5`；`feedback=510K/110K`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 与三路反馈

### AMP_PWR 关闭测试点

EA3036 EN3 由 R23 10K 上拉到 VCC_5V，T1 为接地 0R 测试断点，图面标注用于关闭音频功放。

- 参数与网络：`enable=U4 EN3`；`pullup=R23 10K`；`test_break=T1 0R`；`rail=AMP_PWR`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1，T1/R23/U4 EN3

### IP5306 电池与 5V 管理

U10 IP5306 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY；图面标注 5V 2.4A Sync Boost 与 2.1A Sync Buck Charger。

- 参数与网络：`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`labels=5V 2.4A boost,2.1A charger`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10

## 接口

### USB 电源与数据

U5 VCC 经 FUSE1 2A 接 VIN_USB，D-/D+ 经 R9/R11 22R 接 USB_DN/USB_DP，并由 D1/D2 RLSD52A031V 保护。

- 参数与网络：`power=FUSE1 2A`；`data=USB_DN/USB_DP`；`series=R9/R11 22R`；`esd=D1/D2`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5/FUSE1/R9/R11/D1/D2

### M5-LCD SPI

U6 #RST、R/S、MOSI、SCK、CS 接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14，电源接 VDD_3V3。

- 参数与网络：`reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6

### M5-Bus 功能

M5-Bus 表将 GPIO35/36 标 ADC1/ADC2，GPIO23/19/18 标 MOSI/MISO/SCK，GPIO25/26 标 DAC0/AUDIO_L 与 DAC1/AUDIO_R，GPIO3/1、GPIO16/17、GPIO21/22 标两组 UART 与 SDA/SCL。

- 参数与网络：`adc=GPIO35/36`；`spi=GPIO23/19/18`；`dac=GPIO25/26`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A2-B3，功能表

### M5-Bus I2S

GPIO12、GPIO13、GPIO15、GPIO0、GPIO34 标为 IIS_SCLK、IIS_WS、IIS_OUT、IIS_MCLK/BOOT、IIS_IN。

- 参数与网络：`sclk=GPIO12`；`ws=GPIO13`；`out=GPIO15`；`mclk=GPIO0`；`in=GPIO34`
- 证据：图 72aa5b4d2f89 / 第 1 页 / M5-Bus pins21-26

## 总线

### LCD 与 microSD 共用 SPI

LCD 与 microSD 共用 GPIO23 MOSI 和 GPIO18 SCK；microSD 使用 GPIO19 MISO/GPIO4 CS，LCD 使用 GPIO14 CS。

- 参数与网络：`shared=GPIO23/GPIO18`；`sd=GPIO19/GPIO4`；`lcd=GPIO14`
- 证据：图 2f5b17c1e346 / 第 1 页 / LCD 与 TF Card 分区

### 30 针 M5-Bus

P1 引出 GND、GPIO35/36、EN、GPIO23/25、GPIO19/26、GPIO18、3.3V、GPIO3/1、GPIO16/17、GPIO21/22、GPIO2/5、GPIO12/13、GPIO15/0、HPWR、GPIO34、5V 与 VBAT。

- 参数与网络：`pins_1_6=GND,G35,GND,G36,GND,EN`；`pins_7_12=G23,G25,G19,G26,G18,3V3`；`pins_13_18=G3,G1,G16,G17,G21,G22`；`pins_19_24=G2,G5,G12,G13,G15,G0`；`pins_25_30=HPWR,G34,HPWR,5V,HPWR,VBAT`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 pins1-30

## 总线地址

### 定制 IP5306 I2C 地址

原理图注释明确说明定制 IP5306 通过 IIC 与 ESP32 通信，地址为 0x75。

- 参数与网络：`device=IP5306`；`address=0x75`；`sda=GPIO21`；`scl=GPIO22`
- 证据：图 91b865957940 / 第 1 页 / 网格 D1-D2，0x75 注释; 图 72aa5b4d2f89 / 第 1 页 / GPIO21 SDA/GPIO22 SCL

## GPIO 与控制信号

### 三个用户按键

S3 Btn A、S2 Btn B、S1 Btn C 按下时分别将 GPIO39、GPIO38、GPIO37 接地，各有 100K 上拉与钳位保护。

- 参数与网络：`button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1-S3

### LCD 背光

U6 BL 由 FET1 AO3402 开关到地，栅极接 GPIO32 并由 R15 100K 下拉。

- 参数与网络：`switch=AO3402`；`control=GPIO32`；`pulldown=100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1/U6 BL

## 时钟

### ESP32 40MHz 主晶振

X1 标注 40MHz/+-10ppm/22pF，连接 ESP_XTAL_N/P，C21/C22 各 22pF 接地。

- 参数与网络：`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21/C22 22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22

## 复位

### EN 与启动保持

GPIO0 由 R5 12K 上拉，EN 由 R12 12K 上拉并以 C25 1nF 接地，PWR 经 12K 电阻连接 EN。

- 参数与网络：`gpio0=R5 12K`；`en=R12 12K,C25 1nF`；`pwr_to_en=12K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-B2，GPIO0/EN/PWR

### PWR 按键

S4 按下将 PWR 接地，节点有 R13 100K 上拉、C7 1nF 与 D28 保护。

- 参数与网络：`switch=S4`；`net=PWR`；`pullup=100K`；`cap=1nF`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B1，S4/PWR

## 保护电路

### USB CC 下拉

USB_CC_1 与 USB_CC_2 各通过 5.10K 电阻接地，分区注释为 For USB-PD Recognition。

- 参数与网络：`cc1=5.10K to GND`；`cc2=5.10K to GND`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3，USB_CC_1/2

### M5-Bus 信号保护

P1 多路 GPIO/EN/EXT_SCK 配置 RLSD52A031V 阵列至 GND，EXT_SCK 经 R2 22R 到 GPIO18。

- 参数与网络：`device=RLSD52A031V`；`series=R2 22R`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-D1，D2-D23/R2

## 存储

### GD25Q32C SPI Flash

U2 标为 GD25Q32C，nCS/CLK/DI-IO0/DO-IO1/nWP-IO2/nHOLD-IO3 接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C

### microSD SPI

U8 CS、DI、SCLK、DO 对应 GPIO4、GPIO23、GPIO18、GPIO19，电源接 VDD_3V3。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8

## 音频

### NS4148 功放

U9 INP 经 C43 100nF 接 GPIO25，INN 经 C44 100nF 接 PGND，VCC/CTRL 接 AMP_PWR。

- 参数与网络：`input=GPIO25`；`negative=PGND`；`supply=AMP_PWR`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9

### 差分音频输出

NS4148 VOP/VON 经 FB1/FB2 600R@100M 成为 AUDIO_OUT_P/N，两路各以 C42/C45 1nF 接地。

- 参数与网络：`positive=FB1/C42`；`negative=FB2/C45`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-A2，输出滤波

## 射频

### ESP_LNA 天线匹配

ESP_LNA 经 L1/C1/C9 匹配位连接 ANT1，元件值均标 TBD，并注明依实际阻抗匹配决定。

- 参数与网络：`antenna=ANT1`；`rf_net=ESP_LNA`；`matching=L1/C1/C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/L1/C1/C9

## 调试与烧录

### CP2104 USB-UART

U3 CP2104 DP/DM 接 USB_DP/USB_DN，TXD 经 R8 470R 接 RXD0/GPIO3，RXD 接 TXD0/GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`part=CP2104`；`usb=USB_DP/USB_DN`；`uart=GPIO3/GPIO1`；`control=RTS/DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3

### ESP32 自动下载

DTR/RTS 通过 R16/R19 12K 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0。

- 参数与网络：`inputs=DTR/RTS`；`outputs=EN/GPIO0`；`transistors=2x S8050`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D2-D3，Auto-Download

## 模拟电路

### ESP_CAP1/ESP_CAP2 网络

ESP_CAP1 与 ESP_CAP2 间并联 R1 20K/C19 3nF，ESP_CAP1 经 C20 10nF 接地；图面注释制造时使用 3.3nF。

- 参数与网络：`between=R1 20K,C19 3nF`；`ground=C20 10nF`；`note=3.3nF manufacture`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C2，ESP_CAP1/2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 原理图来源版本 | `design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6` |
| 系统结构 | 六页功能分区 | `pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio` |
| 核心器件 | ESP32-D0WDQ6 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3` |
| 存储 | GD25Q32C SPI Flash | `reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3` |
| 时钟 | ESP32 40MHz 主晶振 | `frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21/C22 22pF` |
| 射频 | ESP_LNA 天线匹配 | `antenna=ANT1`；`rf_net=ESP_LNA`；`matching=L1/C1/C9 TBD` |
| 电源 | EA3036 三路电源 | `input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5`；`feedback=510K/110K` |
| 电源 | AMP_PWR 关闭测试点 | `enable=U4 EN3`；`pullup=R23 10K`；`test_break=T1 0R`；`rail=AMP_PWR` |
| 电源 | IP5306 电池与 5V 管理 | `input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`labels=5V 2.4A boost,2.1A charger` |
| 总线地址 | 定制 IP5306 I2C 地址 | `device=IP5306`；`address=0x75`；`sda=GPIO21`；`scl=GPIO22` |
| 接口 | USB 电源与数据 | `power=FUSE1 2A`；`data=USB_DN/USB_DP`；`series=R9/R11 22R`；`esd=D1/D2` |
| 保护电路 | USB CC 下拉 | `cc1=5.10K to GND`；`cc2=5.10K to GND` |
| 调试与烧录 | CP2104 USB-UART | `part=CP2104`；`usb=USB_DP/USB_DN`；`uart=GPIO3/GPIO1`；`control=RTS/DTR` |
| 调试与烧录 | ESP32 自动下载 | `inputs=DTR/RTS`；`outputs=EN/GPIO0`；`transistors=2x S8050` |
| 复位 | EN 与启动保持 | `gpio0=R5 12K`；`en=R12 12K,C25 1nF`；`pwr_to_en=12K` |
| GPIO 与控制信号 | 三个用户按键 | `button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37` |
| 复位 | PWR 按键 | `switch=S4`；`net=PWR`；`pullup=100K`；`cap=1nF` |
| 接口 | M5-LCD SPI | `reset=GPIO33`；`dc=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`cs=GPIO14` |
| GPIO 与控制信号 | LCD 背光 | `switch=AO3402`；`control=GPIO32`；`pulldown=100K` |
| 存储 | microSD SPI | `cs=GPIO4`；`mosi=GPIO23`；`sck=GPIO18`；`miso=GPIO19` |
| 总线 | LCD 与 microSD 共用 SPI | `shared=GPIO23/GPIO18`；`sd=GPIO19/GPIO4`；`lcd=GPIO14` |
| 总线 | 30 针 M5-Bus | `pins_1_6=GND,G35,GND,G36,GND,EN`；`pins_7_12=G23,G25,G19,G26,G18,3V3`；`pins_13_18=G3,G1,G16,G17,G21,G22`；`pins_19_24=G2,G5,G12,G13,G15,G0`；`pins_25_30=HPWR,G34,HPWR,5V,HPWR,VBAT` |
| 接口 | M5-Bus 功能 | `adc=GPIO35/36`；`spi=GPIO23/19/18`；`dac=GPIO25/26`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22` |
| 接口 | M5-Bus I2S | `sclk=GPIO12`；`ws=GPIO13`；`out=GPIO15`；`mclk=GPIO0`；`in=GPIO34` |
| 保护电路 | M5-Bus 信号保护 | `device=RLSD52A031V`；`series=R2 22R` |
| 音频 | NS4148 功放 | `input=GPIO25`；`negative=PGND`；`supply=AMP_PWR` |
| 音频 | 差分音频输出 | `positive=FB1/C42`；`negative=FB2/C45` |
| 模拟电路 | ESP_CAP1/ESP_CAP2 网络 | `between=R1 20K,C19 3nF`；`ground=C20 10nF`；`note=3.3nF manufacture` |
| 系统结构 | 2017 Core 图对 Gray 的适用范围 | `schematic=M5 STACK CORE 2017 Rev A`；`target=Gray K002`；`missing=IMU/magnetometer pages` |
| 存储 | Gray Flash 容量 | `document_description=4MB`；`document_spec_table=16MB`；`schematic=GD25Q32C` |
| 调试与烧录 | Gray USB-TTL 版本 | `source_document=CP2104 or CH9102`；`schematic=CP2104` |
| 核心器件 | Gray LCD 控制器 | `source_document=ILI9342C 320x240 IPS`；`schematic=M5-LCD` |
| 传感器 | Gray MPU6886 与 BMM150 | `imu=MPU6886 0x68`；`magnetometer=BMM150 0x10`；`history=MPU6050+MAG3110 -> MPU9250 -> MPU6886+BMM150` |
| 电源 | Gray 电池容量 | `source_document=3.7V 110mAh`；`history=150mAh -> 110mAh`；`schematic=VBAT/IP5306` |
| 音频 | Gray 扬声器规格 | `source_document=1W-0928`；`schematic=NS4148/AUDIO_OUT_P/N` |
| 存储 | microSD 最大容量 | `source_document=16GB max`；`schematic=MicroSD-SPI interface` |
| 电源 | Gray 充电电流测量值 | `charge_current=1.069A`；`full_on_current=0.073A`；`schematic=IP5306 only` |
| 系统结构 | Gray 主频与 Wi-Fi | `cpu=240MHz`；`wifi=2.4GHz`；`schematic=ESP32-D0WDQ6 and antenna` |

## 待确认事项

- `system.gray-applicability`：当前资源仅显示 2017 M5 STACK CORE Rev A，未显示 Gray、K002 或 IMU/磁力计页面；对后续 Gray 量产版本的完整适用范围需确认。（证据：图 a44d9e10f49e / 第 1 页 / 封面修订记录与页面目录）
- `storage.gray-flash`：产品源文档描述段写 4MB SPI Flash，规格表写 16MB，所给原理图 U2 为 GD25Q32C；Gray 当前量产容量和器件需确认。（证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C）
- `debug.gray-usb-uart`：产品源文档说明存在 CP2104 与 CH9102 版本，所给原理图只显示 CP2104；目标 Gray 硬件的 USB-TTL 器件需确认。（证据：图 2f5b17c1e346 / 第 1 页 / U3 CP2104）
- `component.gray-display`：产品源文档标注 ILI9342C 320x240 IPS，原理图只标 M5-LCD，未显示控制器型号或面板参数。（证据：图 2f5b17c1e346 / 第 1 页 / U6 M5-LCD）
- `sensor.gray-imu`：产品源文档标注 MPU6886 0x68 与 BMM150 0x10，并记录历史传感器变更；当前六页原理图未显示这些器件或地址绑定位。（证据：图 a44d9e10f49e / 第 1 页 / 页面目录不含传感器页; 图 72aa5b4d2f89 / 第 1 页 / M5-Bus 仅引出 I2C）
- `power.gray-battery`：产品源文档标注 3.7V 110mAh 并记录 150mAh 至 110mAh 变更；原理图只显示 VBAT/IP5306，没有电池型号或容量。（证据：图 91b865957940 / 第 1 页 / U10 IP5306/VBAT）
- `audio.gray-speaker`：产品源文档标注 1W-0928，功放页只显示 NS4148 与 AUDIO_OUT_P/N，未显示扬声器器件、阻抗或额定功率。（证据：图 8d7498c3a5a7 / 第 1 页 / U9 与 AUDIO_OUT_P/N）
- `storage.gray-microsd-limit`：产品源文档称 microSD 最大支持 16GB，原理图只显示 SPI 卡座与信号，未标介质容量或文件系统限制。（证据：图 2f5b17c1e346 / 第 1 页 / U8 MicroSD-SPI）
- `power.gray-charge-current`：产品源文档列出 1.069A 充电电流和 0.073A 满电开机电流，原理图只给 IP5306 电路，没有测试条件或这些测量值。（证据：图 91b865957940 / 第 1 页 / IP5306 电源管理页）
- `system.gray-operating-specs`：产品源文档标注 240MHz 与 2.4GHz Wi-Fi，原理图显示 ESP32-D0WDQ6 与天线网络，但未直接给出运行频率或无线协议参数。（证据：图 d81402da2106 / 第 1 页 / ESP32 与天线网络）
- `review.gray-applicability`：2017 M5 STACK CORE Rev A 六页图对 Gray K002 各量产版本的适用范围是什么？；原因：资源没有 Gray/K002 或传感器页。
- `review.gray-flash`：Gray 当前量产 Flash 是 4MB 还是 16MB，具体型号是什么？；原因：产品源文档内部冲突，原理图标 GD25Q32C。
- `review.gray-usb-uart`：目标 Gray 硬件的 USB-TTL 是 CP2104 还是 CH9102？；原因：产品页说明存在两个版本，当前图只显示 CP2104。
- `review.gray-display`：Gray 的 LCD 是否确认为 ILI9342C 320x240 IPS？；原因：原理图只标 M5-LCD。
- `review.gray-imu`：目标 Gray 版本是否使用 MPU6886 0x68 与 BMM150 0x10，其具体电路是什么？；原因：产品历史包含多次传感器更换，资源没有传感器页。
- `review.gray-battery`：Gray 当前主电池是否为 3.7V 110mAh，具体料号是什么？；原因：原理图没有电池容量或料号。
- `review.gray-speaker`：Gray 扬声器是否为 1W-0928，其阻抗和额定条件是什么？；原因：功放页未画扬声器负载。
- `review.gray-microsd`：Gray 的 16GB microSD 上限来自硬件、固件还是文件系统限制？；原因：原理图只显示 SPI 卡座。
- `review.gray-charge-current`：Gray 的 1.069A/0.073A 电流测量条件、硬件版本和测点是什么？；原因：原理图未记录这些测试信息。
- `review.gray-operating-specs`：Gray 量产固件的主频与无线规格是否确认为 240MHz 和 2.4GHz Wi-Fi？；原因：参数来自产品源文档，原理图未直接给出。

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

源文档：`zh_CN/core/gray.md`

源文档 SHA-256：`bf55d50cf8d07ff0c373cbde6f16c6381d65e539814ab92d7db063acc42740c4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
