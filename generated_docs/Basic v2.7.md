# Basic v2.7 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Basic v2.7 |
| SKU | K001-V27 |
| 产品 ID | `basic-v2-7-27c4169867b7` |
| 源文档 | `zh_CN/core/basic_v2.7.md` |

## 概述

Basic v2.7 清单关联的六页原理图是一套 2017 年 M5 STACK CORE Rev A 电路：U1 ESP32-D0WDQ6 配 U2 GD25Q32C SPI Flash 和 40MHz 晶振，U4 EA3036 生成 VCC_3V3、VDD_3V3 与 AMP_PWR，U10 IP5306 管理 USB、电池、5V 升压并以 0x75 接入 I2C；USB-UART、自动下载、三按键、LCD、microSD、30针 M5-Bus 和 U9 NS4148 音频功放分布在其余页面。该原理图的器件版本与 Basic v2.7 产品页中的 ESP32-D0WDQ6-V3、16MB Flash、CH9102F 等描述存在差异，当前版本适用性单列为待确认，不用旧图推定 v2.7 实物。

## 检索关键词

`Basic v2.7`、`K001-V27`、`M5 STACK CORE`、`Rev A`、`A13`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`GD25Q32C`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`CH9102F`、`NS4148`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`M5-Bus`、`USB Type-C`、`USB_DP`、`USB_DN`、`VIN_USB`、`VCC_5V`、`VCC_3V3`、`VDD_3V3`、`AMP_PWR`、`VBAT`、`GPIO21`、`GPIO22`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO14`、`GPIO27`、`GPIO32`、`GPIO33`、`GPIO37`、`GPIO38`、`GPIO39`、`AUDIO_OUT_P`、`AUDIO_OUT_N`、`40MHz`、`SPI`、`I2C`、`UART`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 主控 SoC，连接 SPI Flash、40MHz 晶振、RF、LCD、microSD、按键、UART、音频和 M5-Bus | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 及全部引脚 |
| U2 | GD25Q32C | ESP32 的外部 SPI Flash，连接 SD_CMD、SD_CLK 与 SD_DATA0~3 | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C 与 SD_CMD/SD_CLK/SD_DATA0~3 |
| X1 | 40MHz/+-10ppm/22pF | ESP32 主晶振，连接 ESP_XTAL_P 与 ESP_XTAL_N | 图 d81402da2106 / 第 1 页 / 网格 C1，X1 40MHz/+-10ppm/22pF、C21/C22 |
| ANT1 | 未标注 | ESP_LNA 射频天线端，前置 L1/C1/C9 匹配位 | 图 d81402da2106 / 第 1 页 / 网格 A2，ANT1 与 ESP_LNA、L1/C1/C9 |
| U4 | EA3036 | 三路同步降压转换器，由 VCC_5V 生成 VCC_3V3、VDD_3V3 和 AMP_PWR | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036、L2/L3/L5 与三路反馈网络 |
| U10 | IP5306 | USB 输入、电池充电和 5V 同步升压电源管理器，定制 I2C 地址 0x75 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306、VIN_USB/VCC_5V/VBAT/PWR_KEY 及 I2C 注释 |
| U3 | CP2104 | USB 转 UART，连接 ESP32 UART0，并提供 RTS/DTR 自动下载信号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104、USB_DP/USB_DN、TXD/RXD/RTS/DTR |
| U5 | USB_Micro | 原理图 Type-C USB 分区中的 USB 电源与数据连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，Type-C USB 分区内 U5 USB_Micro、FUSE1、D1/D2、USB_DP/USB_DN |
| U6 | M5-LCD | LCD 模组接口，包含背光、复位、寄存器选择和 SPI 信号 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD 与 FET1 AO3402 |
| U8 | MicroSD-SPI | microSD 卡座，使用 SPI_SDCS/SPI_SDDI/SPI_CLK/SPI_SDDO | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1,S2,S3,S4 | SMT-3x6-SWC / SMT_SW_TS_015 | GPIO37/38/39 三个用户按键与 PWR 电源/复位按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，Button 分区 S1~S4、D24/D26/D27/D28 |
| P1 | Header 15X2 | 30 针 M5-Bus，提供 GPIO、SPI、UART、I2C、音频、电源、电池和复位信号 | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 pins 1-30 |
| U9 | NS4148 | GPIO25 模拟音频输入的差分 D 类扬声器功放 | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148、GPIO25、AMP_PWR、AUDIO_OUT_P/N |
| FET1 | AO3402 | GPIO32 控制的 LCD 背光低端开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B4，FET1 AO3402、GPIO32、R15 与 U6 BL |

## 系统结构

### 原理图来源版本

封面将该六页设计标为 M5 STACK CORE，修订记录为 A13 OFFICIAL RELEASE VERSION，日期 10/11/2017，标题栏 Revision A、Date 2017/12/6。

- 参数与网络：`design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6`；`pages=6`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 A1-A3 修订表、B3-C4 页面目录、D3-D4 标题栏

### 六页功能分区

封面目录依次列出 COVER PAGE、POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINITION 和 AUDIO AMPLIFIER。

- 参数与网络：`page_1=COVER PAGE`；`page_2=POWER MANAGEMENT`；`page_3=ESP32 SUBSYSTEM`；`page_4=USB-UART & ACCESSORY`；`page_5=M.BUS DEFINITION`；`page_6=AUDIO AMPLIFIER`
- 证据：图 a44d9e10f49e / 第 1 页 / 网格 B3-C4，PAGE NO./SCHEMATIC PAGE 表

## 核心器件

### ESP32-D0WDQ6

U1 明确标为 ESP32-D0WDQ6，供电网络为 VCC_3V3、VDD_SDIO，CHIP_PU 接 EN，RF 引脚接 ESP_LNA，外部 Flash 接 SD_CMD/SD_CLK/SD_DATA0~3。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`supply=VCC_3V3,VDD_SDIO`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 器件名、电源、RF 与 SDIO 引脚

## 电源

### EA3036 三路 3.3V 电源

U4 EA3036 的 VIN1~3 与 VCC 接 VCC_5V，SW1/SW2/SW3 分别经 L2/L3/L5 输出 VCC_3V3、VDD_3V3、AMP_PWR；三路反馈均采用 510K/110K 分压并各配 22uF/6.3V 输出电容。

- 参数与网络：`reference=U4`；`part_number=EA3036`；`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5 MLP2016H1R5MT0S1`；`feedback=510K/110K`；`output_caps=C14/C28/C33 22uF/6.3V`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4、L2/L3/L5、R24/R27/R29/R31/R34/R36、C14/C28/C33

### AMP_PWR 关闭测试点

EA3036 的 EN3 由 R23 10K 上拉到 VCC_5V，T1 为接地的 0Ω 测试断点；图面将其标为 Test Break for Disabling Audio Amplifier。

- 参数与网络：`enable=U4 EN3`；`pullup=R23 10K to VCC_5V`；`test_break=T1 0R to GND`；`rail=AMP_PWR`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1，T1/R23/U4 EN3 与 disabling audio amplifier 注释

### IP5306 电池与 5V 管理

U10 IP5306 的 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY；图面标注 5V 2.4A Sync Boost 和 2.1A Sync Buck Charger。

- 参数与网络：`reference=U10`；`part_number=IP5306`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_label=5V 2.4A Sync Boost`；`charger_label=2.1A Sync Buck Charger`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 与 VIN_USB/VCC_5V/VBAT/PWR_KEY

## 接口

### USB 电源与数据路径

Type-C USB 分区的 U5 将 VCC 经 FUSE1 2A 接 VIN_USB，D-、D+ 分别经 R9、R11 22R 接 USB_DN、USB_DP，并分别配置 D1、D2 RLSD52A031V 到地。

- 参数与网络：`connector=U5`；`symbol=USB_Micro`；`power=VCC->FUSE1 2A->VIN_USB`；`data_minus=D-->R9 22R->USB_DN`；`data_plus=D+->R11 22R->USB_DP`；`esd=D1,D2 RLSD52A031V`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A4，Type-C USB 分区 U5/FUSE1/R9/R11/D1/D2

### M5-LCD SPI 接口

U6 M5-LCD 的 #RST、R/S、MOSI、SCK、CS 分别连接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14，电源接 VDD_3V3。

- 参数与网络：`reference=U6`；`reset=GPIO33`；`register_select=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 M5-LCD 引脚 5~14

### M5-Bus 功能别名

M5-Bus 表将 GPIO35/36 标为 ADC1/ADC2，GPIO23/19/18 标为 MOSI/MISO/SCK，GPIO25/26 标为 DAC0/AUDIO_L 与 DAC1/AUDIO_R，GPIO3/1 标为 RXD1/TXD1，GPIO16/17 标为 RXD2/TXD2，GPIO21/22 标为 SDA/SCL。

- 参数与网络：`adc=GPIO35 ADC1,GPIO36 ADC2`；`spi=GPIO23 MOSI,GPIO19 MISO,GPIO18 SCK`；`audio_dac=GPIO25 DAC0/AUDIO_L,GPIO26 DAC1/AUDIO_R`；`uart1=GPIO3 RXD1,GPIO1 TXD1`；`uart2=GPIO16 RXD2,GPIO17 TXD2`；`i2c=GPIO21 SDA,GPIO22 SCL`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A2-B3，彩色 M5-Bus 功能映射表

### M5-Bus I2S 信号

M5-Bus 表将 GPIO12、GPIO13、GPIO15、GPIO0、GPIO34 分别标为 IIS_SCLK、IIS_WS、IIS_OUT、IIS_MCLK/BOOT、IIS_IN。

- 参数与网络：`i2s_sclk=GPIO12`；`i2s_ws=GPIO13`；`i2s_out=GPIO15`；`i2s_mclk_boot=GPIO0`；`i2s_in=GPIO34`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A2-B3，M5-Bus pins 21~26 I2S 功能

## 总线

### LCD 与 microSD 共用 SPI

LCD 和 microSD 共用 GPIO23 MOSI 与 GPIO18 SCK；microSD 另用 GPIO19 MISO 和 GPIO4 CS，LCD 另用 GPIO14 CS。

- 参数与网络：`shared_mosi=GPIO23`；`shared_sck=GPIO18`；`microsd_miso=GPIO19`；`microsd_cs=GPIO4`；`lcd_cs=GPIO14`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4 U6 M5-LCD 与网格 C1-D2 U8 MicroSD-SPI

### 30 针 M5-Bus

P1 Header 15X2 将 GND、GPIO35/36、EN、GPIO23/25、GPIO19/26、GPIO18、VDD_3V3、GPIO3/1、GPIO16/17、GPIO21/22、GPIO2/5、GPIO12/13、GPIO15/0、HPWR、GPIO34、VCC_5V、VBAT 按 pins 1~30 引出。

- 参数与网络：`connector=P1 Header 15X2`；`pins_1_6=1 GND,2 GPIO35,3 GND,4 GPIO36,5 GND,6 EN`；`pins_7_12=7 GPIO23,8 GPIO25,9 GPIO19,10 GPIO26,11 EXT_SCK,12 VDD_3V3`；`pins_13_18=13 GPIO3,14 GPIO1,15 GPIO16,16 GPIO17,17 GPIO21,18 GPIO22`；`pins_19_24=19 GPIO2,20 GPIO5,21 GPIO12,22 GPIO13,23 GPIO15,24 GPIO0`；`pins_25_30=25 HPWR,26 GPIO34,27 HPWR,28 VCC_5V,29 HPWR,30 VBAT`；`ext_sck=EXT_SCK through R2 22R to GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 pins 1-30；网格 B1，R2 EXT_SCK-to-GPIO18

## 总线地址

### 定制 IP5306 I2C 地址

原理图注释明确说明该定制 IP5306 通过 IIC 与 ESP32 通信，IIC 地址为 0x75。

- 参数与网络：`device=IP5306`；`bus=I2C/IIC`；`address=0x75`；`sda_gpio=GPIO21`；`scl_gpio=GPIO22`
- 证据：图 91b865957940 / 第 1 页 / 网格 D1-D2，customized IP5306 IIC communication/address 0x75 注释; 图 72aa5b4d2f89 / 第 1 页 / 网格 A2-B3，M5-Bus 表 GPIO21 IO4/SDA、GPIO22 IO5/SCL

## GPIO 与控制信号

### Btn A/Btn B/Btn C

S3 Btn A、S2 Btn B、S1 Btn C 按下时分别将 GPIO39、GPIO38、GPIO37 接地；三个 GPIO 各有 100K 上拉到 VDD_3V3 和 RLSD52A031V 钳位器件。

- 参数与网络：`button_a=S3 GPIO39`；`button_b=S2 GPIO38`；`button_c=S1 GPIO37`；`pullups=R10/R7/R4 100K`；`protection=D27/D26/D24 RLSD52A031V`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，Button 分区 GPIO37/38/39 与 S1/S2/S3

### LCD 背光控制

U6 的三个 BL 引脚并联后由 FET1 AO3402 开关到地，FET1 栅极接 GPIO32，并由 R15 100K 下拉。

- 参数与网络：`backlight_pins=U6 pins 3,4,5`；`switch=FET1 AO3402`；`control=GPIO32`；`gate_pulldown=R15 100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4，U6 BL、FET1 AO3402、GPIO32、R15

## 时钟

### ESP32 40MHz 主晶振

X1 标注 40MHz/+-10ppm/22pF，连接 ESP_XTAL_N 和 ESP_XTAL_P，两端各以 C21、C22 22pF 接地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21 22pF,C22 22pF`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1、C21、C22、ESP_XTAL_N/P

## 复位

### EN 与启动保持网络

GPIO0 由 R5 12K 上拉到 VCC_3V3；EN 由 R12 12K 上拉并以 C25 1nF 接地，PWR 还经一只标称 12K 的电阻连接 EN。

- 参数与网络：`gpio0_pullup=R5 12K to VCC_3V3`；`en_pullup=R12 12K to VCC_3V3`；`en_cap=C25 1nF`；`pwr_to_en=12K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-B2，GPIO0/EN/PWR、R5/R12/C25

### PWR 按键

S4 Btn Rst 按下时将 PWR 接地，PWR 节点有 R13 100K 上拉到 VDD_3V3、C7 1nF 对地和 D28 保护。

- 参数与网络：`switch=S4 SMT_SW_TS_015`；`net=PWR`；`pullup=R13 100K`；`cap=C7 1nF`；`protection=D28`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B1，S4 Btn Rst、PWR、R13/C7/D28

## 保护电路

### USB CC 下拉

USB_CC_1 与 USB_CC_2 各通过一只标称 5.10K 的电阻接地，分区注释为 For USB-PD Recognition。

- 参数与网络：`cc1=5.10K to GND`；`cc2=5.10K to GND`；`note=For USB-PD Recognition`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3，USB_CC_1/USB_CC_2 与两个 5.10K 下拉

### M5-Bus 信号钳位

P1 的多路 GPIO/EN/EXT_SCK 信号在连接器侧配置 RLSD52A031V 阵列至 GND，EXT_SCK 还经 R2 22R 串联到 GPIO18。

- 参数与网络：`device_family=RLSD52A031V`；`protected_nets=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34`；`series=R2 22R on EXT_SCK/GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-D1，D2~D23 RLSD52A031V 阵列与 R2

## 存储

### GD25Q32C SPI Flash

U2 标为 GD25Q32C，nCS/CLK/DI-IO0/DO-IO1/nWP-IO2/nHOLD-IO3 分别接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2，VCC 接 VCC_3V3。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`chip_select=SD_CMD`；`clock=SD_CLK`；`data=SD_DATA0~3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C 引脚与网络

### microSD SPI 接口

U8 MicroSD-SPI 的 CS、DI、SCLK、DO 分别连接 SPI_SDCS、SPI_SDDI、SPI_CLK、SPI_SDDO，对应 GPIO4、GPIO23、GPIO18、GPIO19。

- 参数与网络：`reference=U8`；`cs=GPIO4`；`mosi_di=GPIO23`；`clock=GPIO18`；`miso_do=GPIO19`；`supply=VDD_3V3`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 C1-D2，SPI_SDCS/SDDI/CLK/SDDO 保护网络与 U8 MicroSD-SPI

## 音频

### NS4148 扬声器功放

U9 NS4148 的 INP 经 C43 100nF 接 GPIO25，INN 经 C44 100nF 接 PGND，VCC 接 AMP_PWR，CTRL 经 R37 10K 接 AMP_PWR，差分输出为 VOP/VON。

- 参数与网络：`reference=U9`；`part_number=NS4148`；`input_positive=GPIO25 through C43 100nF`；`input_negative=PGND through C44 100nF`；`supply=AMP_PWR`；`control=R37 10K to AMP_PWR`；`outputs=VOP,VON`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148、C43/C44/R37、GPIO25/AMP_PWR

### 差分扬声器输出滤波

NS4148 的 VOP、VON 分别经 FB1、FB2 600R@100M 磁珠成为 AUDIO_OUT_P、AUDIO_OUT_N，两路各以 C42、C45 1nF 接地。

- 参数与网络：`positive=VOP->FB1 600R@100M->AUDIO_OUT_P,C42 1nF to GND`；`negative=VON->FB2 600R@100M->AUDIO_OUT_N,C45 1nF to GND`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-A2，FB1/FB2/C42/C45 与 AUDIO_OUT_P/N

## 射频

### ESP_LNA 天线匹配网络

ESP_LNA 经 L1/C1/C9 组成的匹配位连接 ANT1，三只元件值均在图中标为 TBD，并注明依实际阻抗匹配结果决定。

- 参数与网络：`antenna=ANT1`；`rf_net=ESP_LNA`；`series=C1 TBD`；`shunt_input=L1 TBD`；`shunt_output=C9 TBD`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，ESP_LNA、L1/C1/C9、ANT1 与 impedance matching 注释

## 调试与烧录

### CP2104 USB-UART

U3 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD 经 R8 470R 接 RXD0/GPIO3，RXD 接 TXD0/GPIO1，RTS 与 DTR 引至自动下载电路。

- 参数与网络：`reference=U3`；`part_number=CP2104`；`usb=USB_DP,USB_DN`；`tx_path=TXD->R8 470R->RXD0 GPIO3`；`rx_path=RXD->TXD0 GPIO1`；`control=RTS,DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 及 UART/RTS/DTR 网络

### ESP32 自动下载电路

DTR 与 RTS 通过 R16、R19 12K 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0，构成自动下载电路。

- 参数与网络：`inputs=DTR,RTS`；`resistors=R16 12K,R19 12K`；`transistors=2x NPN-S8050`；`outputs=EN,GPIO0`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D2-D3，Auto-Download 分区 R16/R19 与两只 NPN-S8050

## 模拟电路

### ESP_CAP1/ESP_CAP2 网络

ESP_CAP1 与 ESP_CAP2 之间并联 R1 20K 和 C19 3nF，ESP_CAP1 另经 C20 10nF 接地；图面注释制造时使用 3.3nF。

- 参数与网络：`between_caps=R1 20K parallel C19 3nF`；`cap1_to_ground=C20 10nF`；`manufacturing_note=Use 3.3nF for Manufacture`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C2，ESP_CAP1/ESP_CAP2、R1/C19/C20 与制造注释

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 原理图来源版本 | `design=M5 STACK CORE`；`revision_record=A13`；`revision=A`；`release_date=10/11/2017`；`title_block_date=2017/12/6`；`pages=6` |
| 系统结构 | 六页功能分区 | `page_1=COVER PAGE`；`page_2=POWER MANAGEMENT`；`page_3=ESP32 SUBSYSTEM`；`page_4=USB-UART & ACCESSORY`；`page_5=M.BUS DEFINITION`；`page_6=AUDIO AMPLIFIER` |
| 核心器件 | ESP32-D0WDQ6 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`supply=VCC_3V3,VDD_SDIO`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0~3` |
| 存储 | GD25Q32C SPI Flash | `reference=U2`；`part_number=GD25Q32C`；`supply=VCC_3V3`；`chip_select=SD_CMD`；`clock=SD_CLK`；`data=SD_DATA0~3` |
| 时钟 | ESP32 40MHz 主晶振 | `reference=X1`；`frequency=40MHz`；`tolerance=+-10ppm`；`load=22pF`；`caps=C21 22pF,C22 22pF` |
| 射频 | ESP_LNA 天线匹配网络 | `antenna=ANT1`；`rf_net=ESP_LNA`；`series=C1 TBD`；`shunt_input=L1 TBD`；`shunt_output=C9 TBD` |
| 电源 | EA3036 三路 3.3V 电源 | `reference=U4`；`part_number=EA3036`；`input=VCC_5V`；`outputs=VCC_3V3,VDD_3V3,AMP_PWR`；`inductors=L2/L3/L5 MLP2016H1R5MT0S1`；`feedback=510K/110K`；`output_caps=C14/C28/C33 22uF/6.3V` |
| 电源 | AMP_PWR 关闭测试点 | `enable=U4 EN3`；`pullup=R23 10K to VCC_5V`；`test_break=T1 0R to GND`；`rail=AMP_PWR` |
| 电源 | IP5306 电池与 5V 管理 | `reference=U10`；`part_number=IP5306`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_label=5V 2.4A Sync Boost`；`charger_label=2.1A Sync Buck Charger` |
| 总线地址 | 定制 IP5306 I2C 地址 | `device=IP5306`；`bus=I2C/IIC`；`address=0x75`；`sda_gpio=GPIO21`；`scl_gpio=GPIO22` |
| 接口 | USB 电源与数据路径 | `connector=U5`；`symbol=USB_Micro`；`power=VCC->FUSE1 2A->VIN_USB`；`data_minus=D-->R9 22R->USB_DN`；`data_plus=D+->R11 22R->USB_DP`；`esd=D1,D2 RLSD52A031V` |
| 保护电路 | USB CC 下拉 | `cc1=5.10K to GND`；`cc2=5.10K to GND`；`note=For USB-PD Recognition` |
| 调试与烧录 | CP2104 USB-UART | `reference=U3`；`part_number=CP2104`；`usb=USB_DP,USB_DN`；`tx_path=TXD->R8 470R->RXD0 GPIO3`；`rx_path=RXD->TXD0 GPIO1`；`control=RTS,DTR` |
| 调试与烧录 | ESP32 自动下载电路 | `inputs=DTR,RTS`；`resistors=R16 12K,R19 12K`；`transistors=2x NPN-S8050`；`outputs=EN,GPIO0` |
| 复位 | EN 与启动保持网络 | `gpio0_pullup=R5 12K to VCC_3V3`；`en_pullup=R12 12K to VCC_3V3`；`en_cap=C25 1nF`；`pwr_to_en=12K` |
| GPIO 与控制信号 | Btn A/Btn B/Btn C | `button_a=S3 GPIO39`；`button_b=S2 GPIO38`；`button_c=S1 GPIO37`；`pullups=R10/R7/R4 100K`；`protection=D27/D26/D24 RLSD52A031V` |
| 复位 | PWR 按键 | `switch=S4 SMT_SW_TS_015`；`net=PWR`；`pullup=R13 100K`；`cap=C7 1nF`；`protection=D28` |
| 接口 | M5-LCD SPI 接口 | `reference=U6`；`reset=GPIO33`；`register_select=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3` |
| GPIO 与控制信号 | LCD 背光控制 | `backlight_pins=U6 pins 3,4,5`；`switch=FET1 AO3402`；`control=GPIO32`；`gate_pulldown=R15 100K` |
| 存储 | microSD SPI 接口 | `reference=U8`；`cs=GPIO4`；`mosi_di=GPIO23`；`clock=GPIO18`；`miso_do=GPIO19`；`supply=VDD_3V3` |
| 总线 | LCD 与 microSD 共用 SPI | `shared_mosi=GPIO23`；`shared_sck=GPIO18`；`microsd_miso=GPIO19`；`microsd_cs=GPIO4`；`lcd_cs=GPIO14` |
| 总线 | 30 针 M5-Bus | `connector=P1 Header 15X2`；`pins_1_6=1 GND,2 GPIO35,3 GND,4 GPIO36,5 GND,6 EN`；`pins_7_12=7 GPIO23,8 GPIO25,9 GPIO19,10 GPIO26,11 EXT_SCK,12 VDD_3V3`；`pins_13_18=13 GPIO3,14 GPIO1,15 GPIO16,16 GPIO17,17 GPIO21,18 GPIO22`；`pins_19_24=19 GPIO2,20 GPIO5,21 GPIO12,22 GPIO13,23 GPIO15,24 GPIO0`；`pins_25_30=25 HPWR,26 GPIO34,27 HPWR,28 VCC_5V,29 HPWR,30 VBAT`；`ext_sck=EXT_SCK through R2 22R to GPIO18` |
| 接口 | M5-Bus 功能别名 | `adc=GPIO35 ADC1,GPIO36 ADC2`；`spi=GPIO23 MOSI,GPIO19 MISO,GPIO18 SCK`；`audio_dac=GPIO25 DAC0/AUDIO_L,GPIO26 DAC1/AUDIO_R`；`uart1=GPIO3 RXD1,GPIO1 TXD1`；`uart2=GPIO16 RXD2,GPIO17 TXD2`；`i2c=GPIO21 SDA,GPIO22 SCL` |
| 接口 | M5-Bus I2S 信号 | `i2s_sclk=GPIO12`；`i2s_ws=GPIO13`；`i2s_out=GPIO15`；`i2s_mclk_boot=GPIO0`；`i2s_in=GPIO34` |
| 保护电路 | M5-Bus 信号钳位 | `device_family=RLSD52A031V`；`protected_nets=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34`；`series=R2 22R on EXT_SCK/GPIO18` |
| 音频 | NS4148 扬声器功放 | `reference=U9`；`part_number=NS4148`；`input_positive=GPIO25 through C43 100nF`；`input_negative=PGND through C44 100nF`；`supply=AMP_PWR`；`control=R37 10K to AMP_PWR`；`outputs=VOP,VON` |
| 音频 | 差分扬声器输出滤波 | `positive=VOP->FB1 600R@100M->AUDIO_OUT_P,C42 1nF to GND`；`negative=VON->FB2 600R@100M->AUDIO_OUT_N,C45 1nF to GND` |
| 模拟电路 | ESP_CAP1/ESP_CAP2 网络 | `between_caps=R1 20K parallel C19 3nF`；`cap1_to_ground=C20 10nF`；`manufacturing_note=Use 3.3nF for Manufacture` |
| 系统结构 | Basic v2.7 与 2017 Core 原理图的版本对应关系 | `schematic_design=M5 STACK CORE`；`schematic_date=2017`；`target_product=Basic v2.7`；`target_release=2023.4` |
| 核心器件 | Basic v2.7 主控具体版本 | `source_document=ESP32-D0WDQ6-V3`；`schematic=ESP32-D0WDQ6`；`reference=U1` |
| 存储 | Basic v2.7 Flash 容量 | `source_document_capacity=16MB`；`schematic_part=GD25Q32C`；`reference=U2` |
| 调试与烧录 | Basic v2.7 USB-UART 芯片 | `source_document=CH9102F`；`schematic=CP2104`；`reference=U3` |
| 核心器件 | Basic v2.7 LCD 控制器 | `source_document=ILI9342C`；`schematic_symbol=M5-LCD`；`reference=U6` |
| 电源 | Basic v2.7 内置电池容量 | `source_document=110mAh@3.7V`；`schematic=VBAT only`；`power_manager=U10 IP5306` |
| 音频 | Basic v2.7 扬声器规格 | `source_document=1W-0928`；`schematic_output=AUDIO_OUT_P,AUDIO_OUT_N`；`amplifier=U9 NS4148` |
| 电源 | Basic v2.7 Grove 5.1V 升压变更 | `source_document=Grove 5.1V boost`；`schematic_rail=VCC_5V`；`schematic_revision=2017 Rev A` |

## 待确认事项

- `system.v27-applicability`：当前资源仅显示 2017 年 M5 STACK CORE Rev A，无法由这些页面确认 2023 年 Basic v2.7 的全部硬件变更已包含在内。（证据：图 a44d9e10f49e / 第 1 页 / 网格 A1-A3 与 D3-D4，2017 修订记录和 M5 STACK CORE 标题栏）
- `component.soc-v27`：产品源文档标注 ESP32-D0WDQ6-V3，而所给原理图 U1 标注 ESP32-D0WDQ6；是否为 v2.7 实物所用的 -V3 版本需结合当前 PCB/BOM 确认。（证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 器件名 ESP32-D0WDQ6）
- `storage.flash-v27`：产品源文档标注 16MB Flash，而所给原理图 U2 为 GD25Q32C；无法用该旧图确认 v2.7 的 16MB Flash 器件与连接。（证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C）
- `debug.usb-uart-v27`：产品源文档标注 CH9102F，而所给原理图 U3 为 CP2104；无法由该页面确认 v2.7 的 CH9102F 电路及自动下载连接是否完全相同。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104）
- `component.display-v27`：产品源文档标注 ILI9342C，所给原理图仅将 U6 标为 M5-LCD，未显示面板控制器型号；ILI9342C 需由 v2.7 面板资料或 BOM 确认。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 B4-C4，U6 仅标 M5-LCD）
- `power.battery-v27`：产品源文档标注 110mAh@3.7V，但所给原理图只显示 VBAT 网络和 IP5306，未给出电池型号或容量。（证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 与 VBAT，未示电池器件）
- `audio.speaker-v27`：产品源文档标注 1W-0928 扬声器，所给原理图只显示 NS4148 与 AUDIO_OUT_P/N，未显示扬声器器件、阻抗或额定功率。（证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 与 AUDIO_OUT_P/N，未示扬声器负载）
- `power.grove-boost-v27`：产品源文档称 v2.7 Grove 口增加稳定 5.1V 输出，但所给原理图仅显示 VCC_5V、M5-Bus 和 2017 电源管理页，未显示该 v2.7 专用升压改动。（证据：图 91b865957940 / 第 1 页 / 网格 A1-D2，2017 POWER MANAGEMENT 页未示 v2.7 Grove 专用升压; 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B3，M5-Bus 仅列 VCC_5V）
- `review.v27-applicability`：这套 2017 M5 STACK CORE Rev A 六页原理图是否仍完整适用于 2023 年 Basic v2.7？；原因：原理图标题和日期早于 v2.7 上市，且多个器件与产品源文档不一致。
- `review.soc-v27`：Basic v2.7 实物的 SoC 是否为 ESP32-D0WDQ6-V3？；原因：源文档标注 -V3，所给原理图 U1 未带 -V3 后缀。
- `review.flash-v27`：Basic v2.7 的 16MB Flash 具体型号和连接是否有当前版本原理图或 BOM 可证实？；原因：源文档标注 16MB，所给原理图却使用 GD25Q32C。
- `review.usb-uart-v27`：Basic v2.7 的 CH9102F USB-UART 电路是否有当前版本原理图可替代这张 CP2104 页面？；原因：产品源文档与原理图 U3 的器件型号不同。
- `review.display-v27`：Basic v2.7 的 U6 面板是否确认为 ILI9342C？；原因：原理图只显示 M5-LCD 接口符号，没有控制器型号。
- `review.battery-v27`：Basic v2.7 内置电池是否为 110mAh@3.7V，具体型号是什么？；原因：原理图只有 VBAT 网络，未显示电池容量和型号。
- `review.speaker-v27`：Basic v2.7 的扬声器是否为 1W-0928，其阻抗和额定功率分别是多少？；原因：功放页未绘出实际扬声器器件或负载参数。
- `review.grove-boost-v27`：Basic v2.7 Grove 口 5.1V 升压电路的器件、网络与限流参数是什么？；原因：产品源文档声明有该变更，但 2017 原理图没有对应专用电路。

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

源文档：`zh_CN/core/basic_v2.7.md`

源文档 SHA-256：`d7803d137be2f2af8dc3cb610c4a3205e3aa7bd44d995fde438f92b4dab4a52e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
