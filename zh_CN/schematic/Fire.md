# Fire 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Fire |
| SKU | K007 |
| 产品 ID | `fire-2b6395d25b50` |
| 源文档 | `zh_CN/core/fire.md` |

## 概述

Fire 清单关联的是 2017 年 M5 STACK CORE Rev A 六页电路：U1 ESP32-D0WDQ6 配 U2 GD25Q32C SPI Flash 和 40MHz 晶振，U4 EA3036 生成 VCC_3V3、VDD_3V3 与 AMP_PWR，U10 IP5306 管理 USB、电池、5V 升压并以 0x75 接入 I2C；其余页面包含 CP2104 USB-UART、自动下载、三按键、LCD、microSD、30针 M5-Bus 和 U9 NS4148 功放。Fire 产品页还描述 M5GO 底座、IMU/磁力计、麦克风、RGB LED、电池及更大存储，但这些均未包含在当前六页资源中，因此不以旧核心板图推定整套 Fire 量产版本。

## 检索关键词

`Fire`、`K007`、`M5 STACK CORE`、`Rev A`、`A13`、`ESP32-D0WDQ6`、`GD25Q32C`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`CH9102`、`NS4148`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`M5-Bus`、`M5GO`、`MPU6886`、`SH200Q`、`BMM150`、`BSE3729`、`SK6812`、`USB Type-C`、`USB_DP`、`USB_DN`、`VIN_USB`、`VCC_5V`、`VCC_3V3`、`VDD_3V3`、`AMP_PWR`、`VBAT`、`GPIO15`、`GPIO16`、`GPIO17`、`GPIO21`、`GPIO22`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO25`、`GPIO37`、`GPIO38`、`GPIO39`、`AUDIO_OUT_P`、`AUDIO_OUT_N`、`40MHz`、`SPI`、`I2C`、`UART`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 主控 SoC，连接 Flash、晶振、RF、LCD、microSD、按键、UART、音频和 M5-Bus | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 |
| U2 | GD25Q32C | ESP32 外部 SPI Flash | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| X1 | 40MHz/+-10ppm/22pF | ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / 网格 C1，X1 与 C21/C22 |
| ANT1 | 未标注 | ESP_LNA 射频天线端与 L1/C1/C9 匹配位 | 图 d81402da2106 / 第 1 页 / 网格 A2，ANT1 与 ESP_LNA |
| U4 | EA3036 | VCC_5V 至三路 3.3V 电源的同步降压转换器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 |
| U10 | IP5306 | USB 输入、电池充电和 5V 同步升压电源管理器，定制 I2C 地址 0x75 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 与 0x75 注记 |
| U3 | CP2104 | USB 转 UART 与自动下载信号源 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 | USB_Micro | Type-C USB 分区中的 USB 电源与数据连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5/FUSE1/D1/D2 |
| U6 | M5-LCD | LCD 模组接口，包含背光、复位、寄存器选择和 SPI 信号 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD |
| U8 | MicroSD-SPI | microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1,S2,S3,S4 | SMT-3x6-SWC / SMT_SW_TS_015 | GPIO37/38/39 三个用户按键与 PWR 按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，Button 分区 S1-S4 |
| P1 | Header 15X2 | 30 针 M5-Bus，提供 GPIO、SPI、UART、I2C、音频、电源、电池和复位 | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| U9 | NS4148 | GPIO25 模拟音频输入的差分 D 类功放 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 |
| FET1 | AO3402 | GPIO32 控制的 LCD 背光低端开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1 AO3402 |

## 系统结构

### 原理图来源版本

封面将该六页设计标为 M5 STACK CORE，修订记录为 A13 OFFICIAL RELEASE VERSION，日期 10/11/2017，标题栏 Revision A、Date 2017/12/6。

- 参数与网络：`design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 A1-A3 修订表与 D3-D4 标题栏

### 六页功能分区

封面目录依次列出 COVER PAGE、POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINITION 和 AUDIO AMPLIFIER。

- 参数与网络：`pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 B3-C4，PAGE NO./SCHEMATIC PAGE 表

## 核心器件

### ESP32-D0WDQ6

U1 明确标为 ESP32-D0WDQ6，供电网络为 VCC_3V3/VDD_SDIO，CHIP_PU 接 EN，RF 接 ESP_LNA，Flash 接 SD_CMD/SD_CLK/SD_DATA0~3。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 器件名、电源、RF 与 SDIO

## 电源

### EA3036 三路 3.3V 电源

U4 EA3036 的 VIN1~3 与 VCC 接 VCC_5V，SW1/SW2/SW3 经 L2/L3/L5 输出 VCC_3V3、VDD_3V3、AMP_PWR；三路反馈均为 510K/110K。

- 参数与网络：`reference=U4`；`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5 MLP2016H1R5MT0S1`；`feedback=510K/110K`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4/L2/L3/L5 与反馈网络

### AMP_PWR 关闭测试点

EA3036 EN3 由 R23 10K 上拉到 VCC_5V，T1 为接地 0R 测试断点，图面标注用于关闭音频功放。

- 参数与网络：`enable=U4 EN3`；`pullup=R23 10K`；`test_break=T1 0R to GND`；`rail=AMP_PWR`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1，T1/R23/U4 EN3

### IP5306 电池与 5V 管理

U10 IP5306 的 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY；图面标注 5V 2.4A Sync Boost 和 2.1A Sync Buck Charger。

- 参数与网络：`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_label=5V 2.4A`；`charger_label=2.1A`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306

## 接口

### USB 电源与数据

U5 VCC 经 FUSE1 2A 接 VIN_USB，D-/D+ 分别经 R9/R11 22R 接 USB_DN/USB_DP，并由 D1/D2 RLSD52A031V 对地保护。

- 参数与网络：`power=VCC->FUSE1 2A->VIN_USB`；`data_minus=R9 22R USB_DN`；`data_plus=R11 22R USB_DP`；`esd=D1/D2 RLSD52A031V`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5/FUSE1/R9/R11/D1/D2

### M5-LCD SPI

U6 #RST、R/S、MOSI、SCK、CS 分别连接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14，电源接 VDD_3V3。

- 参数与网络：`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD

### M5-Bus 功能别名

M5-Bus 表将 GPIO35/36 标为 ADC1/ADC2，GPIO23/19/18 标为 MOSI/MISO/SCK，GPIO25/26 标为 DAC0/AUDIO_L 与 DAC1/AUDIO_R，GPIO3/1、GPIO16/17、GPIO21/22 分别标为两组 UART 与 SDA/SCL。

- 参数与网络：`adc=GPIO35,GPIO36`；`spi=GPIO23,GPIO19,GPIO18`；`dac=GPIO25,GPIO26`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A2-B3，M5-Bus 功能表

### M5-Bus I2S

M5-Bus 表将 GPIO12、GPIO13、GPIO15、GPIO0、GPIO34 标为 IIS_SCLK、IIS_WS、IIS_OUT、IIS_MCLK/BOOT、IIS_IN。

- 参数与网络：`sclk=GPIO12`；`ws=GPIO13`；`out=GPIO15`；`mclk=GPIO0`；`in=GPIO34`
- 证据：图 72aa5b4d2f89 / 第 1 页 / M5-Bus pins21-26 I2S 功能

## 总线

### LCD 与 microSD 共用 SPI

LCD 与 microSD 共用 GPIO23 MOSI 和 GPIO18 SCK；microSD 另用 GPIO19 MISO/GPIO4 CS，LCD 另用 GPIO14 CS。

- 参数与网络：`mosi=GPIO23`；`clock=GPIO18`；`sd_miso=GPIO19`；`sd_cs=GPIO4`；`lcd_cs=GPIO14`
- 证据：图 2f5b17c1e346 / 第 1 页 / U6 LCD 与 U8 microSD

### 30 针 M5-Bus

P1 引出 GND、GPIO35/36、EN、GPIO23/25、GPIO19/26、GPIO18、VDD_3V3、GPIO3/1、GPIO16/17、GPIO21/22、GPIO2/5、GPIO12/13、GPIO15/0、HPWR、GPIO34、VCC_5V 与 VBAT。

- 参数与网络：`pins_1_6=GND,G35,GND,G36,GND,EN`；`pins_7_12=G23,G25,G19,G26,G18,3V3`；`pins_13_18=G3,G1,G16,G17,G21,G22`；`pins_19_24=G2,G5,G12,G13,G15,G0`；`pins_25_30=HPWR,G34,HPWR,VCC_5V,HPWR,VBAT`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 pins1-30

## 总线地址

### 定制 IP5306 I2C 地址

原理图注释明确说明定制 IP5306 通过 IIC 与 ESP32 通信，IIC 地址为 0x75。

- 参数与网络：`device=IP5306`；`address=0x75`；`sda=GPIO21`；`scl=GPIO22`
- 证据：图 91b865957940 / 第 1 页 / 网格 D1-D2，IP5306 IIC address 0x75 注释; 图 72aa5b4d2f89 / 第 1 页 / M5-Bus GPIO21 SDA/GPIO22 SCL

## GPIO 与控制信号

### Btn A/Btn B/Btn C

S3 Btn A、S2 Btn B、S1 Btn C 按下时分别将 GPIO39、GPIO38、GPIO37 接地；各 GPIO 有 100K 上拉与 RLSD52A031V 钳位。

- 参数与网络：`button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`pullups=100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，S1/S2/S3

### LCD 背光

U6 三个 BL 引脚并联后由 FET1 AO3402 开关到地，FET1 栅极接 GPIO32，并由 R15 100K 下拉。

- 参数与网络：`switch=FET1 AO3402`；`control=GPIO32`；`pulldown=R15 100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4，U6 BL/FET1/R15

## 时钟

### ESP32 40MHz 主晶振

X1 标注 40MHz/+-10ppm/22pF，连接 ESP_XTAL_N/P，两端各以 C21/C22 22pF 接地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21/C22 22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1/C21/C22

## 复位

### EN 与启动保持网络

GPIO0 由 R5 12K 上拉到 VCC_3V3；EN 由 R12 12K 上拉并以 C25 1nF 接地，PWR 经 12K 电阻连接 EN。

- 参数与网络：`gpio0_pullup=R5 12K`；`en_pullup=R12 12K`；`en_cap=C25 1nF`；`pwr_to_en=12K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-B2，GPIO0/EN/PWR

### PWR 按键

S4 按下时将 PWR 接地，PWR 有 R13 100K 上拉、C7 1nF 对地和 D28 保护。

- 参数与网络：`switch=S4`；`net=PWR`；`pullup=R13 100K`；`cap=C7 1nF`；`protection=D28`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B1，S4/PWR/R13/C7/D28

## 保护电路

### USB CC 下拉

USB_CC_1 与 USB_CC_2 各通过 5.10K 电阻接地，分区注释为 For USB-PD Recognition。

- 参数与网络：`cc1=5.10K to GND`；`cc2=5.10K to GND`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3，USB_CC_1/USB_CC_2

### M5-Bus 信号钳位

P1 多路 GPIO/EN/EXT_SCK 配置 RLSD52A031V 阵列至 GND，EXT_SCK 经 R2 22R 串联到 GPIO18。

- 参数与网络：`device=RLSD52A031V`；`series=R2 22R EXT_SCK/GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-D1，D2-D23 与 R2

## 存储

### GD25Q32C SPI Flash

U2 标为 GD25Q32C，nCS/CLK/DI-IO0/DO-IO1/nWP-IO2/nHOLD-IO3 接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2，VCC 接 VCC_3V3。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C

### microSD SPI

U8 CS、DI、SCLK、DO 连接 SPI_SDCS、SPI_SDDI、SPI_CLK、SPI_SDDO，对应 GPIO4、GPIO23、GPIO18、GPIO19。

- 参数与网络：`cs=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`supply=VDD_3V3`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 C1-D2，U8 MicroSD-SPI

## 音频

### NS4148 扬声器功放

U9 NS4148 INP 经 C43 100nF 接 GPIO25，INN 经 C44 100nF 接 PGND，VCC 接 AMP_PWR，CTRL 经 R37 10K 接 AMP_PWR。

- 参数与网络：`input=GPIO25 through C43`；`negative=PGND through C44`；`supply=AMP_PWR`；`control=R37 10K`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148

### 差分扬声器输出

NS4148 VOP/VON 经 FB1/FB2 600R@100M 成为 AUDIO_OUT_P/N，两路各以 C42/C45 1nF 接地。

- 参数与网络：`positive=FB1 600R@100M,C42 1nF`；`negative=FB2 600R@100M,C45 1nF`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-A2，FB1/FB2/C42/C45

## 射频

### ESP_LNA 天线匹配

ESP_LNA 经 L1/C1/C9 匹配位连接 ANT1，三只元件值均标 TBD，并注明依实际阻抗匹配结果决定。

- 参数与网络：`antenna=ANT1`；`rf_net=ESP_LNA`；`matching=L1/C1/C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ANT1/L1/C1/C9

## 调试与烧录

### CP2104 USB-UART

U3 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD 经 R8 470R 接 RXD0/GPIO3，RXD 接 TXD0/GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`part_number=CP2104`；`usb=USB_DP,USB_DN`；`tx=GPIO3`；`rx=GPIO1`；`control=RTS,DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104

### ESP32 自动下载

DTR/RTS 通过 R16/R19 12K 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0。

- 参数与网络：`inputs=DTR,RTS`；`resistors=R16/R19 12K`；`transistors=2x NPN-S8050`；`outputs=EN,GPIO0`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D2-D3，Auto-Download 分区

## 模拟电路

### ESP_CAP1/ESP_CAP2 网络

ESP_CAP1 与 ESP_CAP2 间并联 R1 20K 与 C19 3nF，ESP_CAP1 经 C20 10nF 接地；图面注释制造时使用 3.3nF。

- 参数与网络：`between=R1 20K parallel C19 3nF`；`to_ground=C20 10nF`；`note=Use 3.3nF for Manufacture`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C2，ESP_CAP1/ESP_CAP2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 原理图来源版本 | `design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6` |
| 系统结构 | 六页功能分区 | `pages=cover,power,ESP32,USB-UART/accessory,M5-Bus,audio` |
| 核心器件 | ESP32-D0WDQ6 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3` |
| 存储 | GD25Q32C SPI Flash | `reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`signals=SD_CMD,SD_CLK,SD_DATA0~3` |
| 时钟 | ESP32 40MHz 主晶振 | `reference=X1`；`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21/C22 22pF` |
| 射频 | ESP_LNA 天线匹配 | `antenna=ANT1`；`rf_net=ESP_LNA`；`matching=L1/C1/C9 TBD` |
| 电源 | EA3036 三路 3.3V 电源 | `reference=U4`；`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5 MLP2016H1R5MT0S1`；`feedback=510K/110K` |
| 电源 | AMP_PWR 关闭测试点 | `enable=U4 EN3`；`pullup=R23 10K`；`test_break=T1 0R to GND`；`rail=AMP_PWR` |
| 电源 | IP5306 电池与 5V 管理 | `input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_label=5V 2.4A`；`charger_label=2.1A` |
| 总线地址 | 定制 IP5306 I2C 地址 | `device=IP5306`；`address=0x75`；`sda=GPIO21`；`scl=GPIO22` |
| 接口 | USB 电源与数据 | `power=VCC->FUSE1 2A->VIN_USB`；`data_minus=R9 22R USB_DN`；`data_plus=R11 22R USB_DP`；`esd=D1/D2 RLSD52A031V` |
| 保护电路 | USB CC 下拉 | `cc1=5.10K to GND`；`cc2=5.10K to GND` |
| 调试与烧录 | CP2104 USB-UART | `part_number=CP2104`；`usb=USB_DP,USB_DN`；`tx=GPIO3`；`rx=GPIO1`；`control=RTS,DTR` |
| 调试与烧录 | ESP32 自动下载 | `inputs=DTR,RTS`；`resistors=R16/R19 12K`；`transistors=2x NPN-S8050`；`outputs=EN,GPIO0` |
| 复位 | EN 与启动保持网络 | `gpio0_pullup=R5 12K`；`en_pullup=R12 12K`；`en_cap=C25 1nF`；`pwr_to_en=12K` |
| GPIO 与控制信号 | Btn A/Btn B/Btn C | `button_a=GPIO39`；`button_b=GPIO38`；`button_c=GPIO37`；`pullups=100K` |
| 复位 | PWR 按键 | `switch=S4`；`net=PWR`；`pullup=R13 100K`；`cap=C7 1nF`；`protection=D28` |
| 接口 | M5-LCD SPI | `reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3` |
| GPIO 与控制信号 | LCD 背光 | `switch=FET1 AO3402`；`control=GPIO32`；`pulldown=R15 100K` |
| 存储 | microSD SPI | `cs=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`supply=VDD_3V3` |
| 总线 | LCD 与 microSD 共用 SPI | `mosi=GPIO23`；`clock=GPIO18`；`sd_miso=GPIO19`；`sd_cs=GPIO4`；`lcd_cs=GPIO14` |
| 总线 | 30 针 M5-Bus | `pins_1_6=GND,G35,GND,G36,GND,EN`；`pins_7_12=G23,G25,G19,G26,G18,3V3`；`pins_13_18=G3,G1,G16,G17,G21,G22`；`pins_19_24=G2,G5,G12,G13,G15,G0`；`pins_25_30=HPWR,G34,HPWR,VCC_5V,HPWR,VBAT` |
| 接口 | M5-Bus 功能别名 | `adc=GPIO35,GPIO36`；`spi=GPIO23,GPIO19,GPIO18`；`dac=GPIO25,GPIO26`；`uart=GPIO3/1,GPIO16/17`；`i2c=GPIO21/22` |
| 接口 | M5-Bus I2S | `sclk=GPIO12`；`ws=GPIO13`；`out=GPIO15`；`mclk=GPIO0`；`in=GPIO34` |
| 保护电路 | M5-Bus 信号钳位 | `device=RLSD52A031V`；`series=R2 22R EXT_SCK/GPIO18` |
| 音频 | NS4148 扬声器功放 | `input=GPIO25 through C43`；`negative=PGND through C44`；`supply=AMP_PWR`；`control=R37 10K` |
| 音频 | 差分扬声器输出 | `positive=FB1 600R@100M,C42 1nF`；`negative=FB2 600R@100M,C45 1nF` |
| 模拟电路 | ESP_CAP1/ESP_CAP2 网络 | `between=R1 20K parallel C19 3nF`；`to_ground=C20 10nF`；`note=Use 3.3nF for Manufacture` |
| 系统结构 | 2017 Core 图对 Fire 的适用范围 | `schematic=M5 STACK CORE 2017 Rev A`；`target=Fire K007`；`missing=M5GO base and charging base` |
| 存储 | Fire 16MB Flash | `source_document=16MB`；`schematic=GD25Q32C` |
| 内存与 Flash | Fire 8MB PSRAM | `source_document=8MB Quad PSRAM on GPIO16/17`；`schematic=no PSRAM device` |
| 调试与烧录 | Fire USB-TTL 版本 | `source_document=CP2104 or CH9102`；`schematic=CP2104` |
| 核心器件 | Fire LCD 控制器 | `source_document=ILI9342C 320x240 IPS`；`schematic=M5-LCD` |
| 传感器 | Fire IMU 与磁力计 | `source_document=BMM150 + SH200Q/MPU6886`；`documented_addresses=BMM150 0x10,MPU6886 0x68`；`schematic=devices absent` |
| 系统结构 | M5GO 底座外设 | `microphone=BSE3729`；`rgb=10x SK6812 on GPIO15`；`ports=A I2C,B GPIO,C UART`；`charging_base=present in product` |
| 电源 | Fire 电池与充电底座 | `source_document=3.7V 500mAh`；`schematic=VBAT/IP5306 only`；`charging_base=not shown` |
| 音频 | Fire 扬声器规格 | `source_document=1W-0928`；`schematic=NS4148/AUDIO_OUT_P/N` |
| 系统结构 | Fire 主频与 Wi-Fi 规格 | `cpu=240MHz`；`wifi=2.4GHz`；`schematic=ESP32-D0WDQ6 and antenna path` |

## 待确认事项

- `system.fire-applicability`：当前资源仅显示 2017 M5 STACK CORE Rev A，未显示 Fire、K007、M5GO 底座或充电底座；该六页对完整 Fire 套件和后续量产版本的适用范围需确认。（证据：图 a44d9e10f49e / 第 1 页 / 封面修订记录与 M5 STACK CORE 标题）
- `storage.fire-flash`：产品源文档标注 16MB Flash，而所给原理图 U2 为 GD25Q32C；无法用该旧图确认 Fire 量产 16MB Flash 的器件与连接。（证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C）
- `memory.fire-psram`：产品源文档标注 8MB Quad PSRAM 并说明 GPIO16/17 占用；所给六页原理图没有 PSRAM 器件，且 GPIO16/17 仅作为普通 GPIO/M5-Bus 信号显示。（证据：图 d81402da2106 / 第 1 页 / ESP32 页未画 PSRAM，GPIO16/17 直接引出; 图 72aa5b4d2f89 / 第 1 页 / M5-Bus pins15/16 GPIO16/17）
- `debug.fire-usb-uart`：产品源文档说明 Fire 存在 CP2104 与 CH9102 版本，所给原理图只显示 CP2104；当前设备版本的 USB-TTL 器件需确认。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104）
- `component.fire-display`：产品源文档标注 ILI9342C 320x240 IPS，原理图仅将 U6 标为 M5-LCD，未显示控制器型号或面板参数。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD）
- `sensor.fire-imu`：产品源文档列出 BMM150 与 SH200Q/MPU6886，当前六页 M5 CORE 原理图未显示这些传感器或地址绑定位。（证据：图 a44d9e10f49e / 第 1 页 / 六页目录不含传感器页; 图 72aa5b4d2f89 / 第 1 页 / M5-Bus 仅引出 GPIO/I2C）
- `system.fire-m5go-base`：产品源文档描述 BSE3729 麦克风、GPIO15 的 10 颗 SK6812 RGB LED、Port A/B/C 与 M5GO 充电底座；当前资源没有 M5GO 底座或充电底座原理图。（证据：图 72aa5b4d2f89 / 第 1 页 / 主机 M5-Bus 只给接口，未画 M5GO 底座）
- `power.fire-battery`：产品源文档标注 3.7V 500mAh 电池并包含 M5GO 充电底座；原理图只显示 VBAT/IP5306 与 M5-Bus 电池网络，没有电池料号、容量或充电底座电路。（证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，IP5306/VBAT; 图 72aa5b4d2f89 / 第 1 页 / M5-Bus VBAT）
- `audio.fire-speaker`：产品源文档标注 1W-0928 扬声器，所给功放页只显示 NS4148 与 AUDIO_OUT_P/N，未显示扬声器器件、阻抗或额定功率。（证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 与 AUDIO_OUT_P/N）
- `system.fire-operating-specs`：产品源文档标注 240MHz 与 2.4GHz Wi-Fi，原理图显示 ESP32-D0WDQ6 与天线网络，但未直接给出运行频率或无线协议参数。（证据：图 d81402da2106 / 第 1 页 / ESP32 与天线网络，未标运行规格）
- `review.fire-applicability`：这套 2017 M5 STACK CORE Rev A 六页图对 Fire K007 主机和完整 M5GO 套件的适用范围是什么？；原因：资源没有 Fire/K007/M5GO 标识或底座页面。
- `review.fire-flash`：Fire 量产 16MB Flash 的具体型号和连接是什么？；原因：产品源文档标 16MB，原理图却为 GD25Q32C。
- `review.fire-psram`：Fire 8MB Quad PSRAM 的器件型号和 GPIO16/17 连接是什么？；原因：当前原理图未画 PSRAM，GPIO16/17 直接引出。
- `review.fire-usb-uart`：目标 Fire 硬件的 USB-TTL 芯片是 CP2104 还是 CH9102？；原因：产品源文档说明存在两个版本，当前图只显示 CP2104。
- `review.fire-display`：Fire 的 LCD 是否确认为 ILI9342C 320x240 IPS？；原因：原理图只标 M5-LCD。
- `review.fire-imu`：目标 Fire 版本使用 SH200Q 还是 MPU6886，并搭配哪一版 BMM150 电路？；原因：产品历史包含传感器变更，当前资源没有传感器页。
- `review.fire-m5go-base`：M5GO 底座中麦克风、10颗 SK6812、Port A/B/C 与充电触点的准确电路是什么？；原因：当前资源只有 M5 CORE 主机图。
- `review.fire-battery`：Fire 主电池是否为 3.7V 500mAh，其料号和充电底座参数是什么？；原因：原理图未显示容量、料号或充电底座。
- `review.fire-speaker`：Fire 扬声器是否为 1W-0928，其阻抗和额定功率条件是什么？；原因：功放页未画扬声器负载。
- `review.fire-operating-specs`：Fire 量产固件的主频与无线规格是否确认为 240MHz 和 2.4GHz Wi-Fi？；原因：这些参数来自产品源文档，原理图未直接给出。

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

源文档：`zh_CN/core/fire.md`

源文档 SHA-256：`91122437466681ae996404a2277efcffe57f02441ebca626cabb42e26bb9dcbd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
