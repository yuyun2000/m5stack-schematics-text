# Core Metal 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core Metal |
| SKU | C001-CNC |
| 产品 ID | `core-metal-5d62c0428d7c` |
| 源文档 | `zh_CN/core/CORE Metal.md` |

## 概述

Core Metal 清单绑定的六页资源是 2017 年 M5 STACK CORE Revision A 原理图，图中包含 ESP32-D0WDQ6、GD25Q32C、IP5306、EA3036、CP2104、M5-LCD、MicroSD、M5-Bus 与 NS4148 音频链路。图纸可确认电源、SPI、UART、按键、扩展总线和音频连接，但没有 Core Metal 或 C001-CNC 标识，并与正文的 ESP32-D0WDQ6-V3、16MB Flash、CH9102F、USB Type-C、ILI9342C、1W-0928、铝合金外壳和 2.4G 3D 天线等配置不一致或缺少直接证据，因此这些产品专属信息保留待确认。

## 检索关键词

`Core Metal`、`C001-CNC`、`M5 STACK CORE`、`Revision A`、`2017/12/6`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`GD25Q32C`、`16MB Flash`、`IP5306`、`IP5306 0x75`、`EA3036`、`CP2104`、`CH9102F`、`USB_Micro`、`USB Type-C`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`TF Card`、`NS4148`、`M5-Bus`、`GPIO25`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO14`、`GPIO4`、`GPIO32`、`GPIO33`、`GPIO37`、`GPIO38`、`GPIO39`、`GPIO21`、`GPIO22`、`VCC_5V`、`VCC_3V3`、`VDD_3V3`、`AMP_PWR`、`VIN_USB`、`VBAT`、`40MHz`、`ANT1`、`3D antenna`、`铝合金`、`Auto-Download`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 2017 原理图中的主控，连接外部 SPI Flash、RF、UART、LCD、TF 卡、按键与 M5-Bus | 图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 全部引脚 |
| U2 | GD25Q32C | ESP32 外部 SPI Flash，连接 SD_CMD、SD_CLK 与 SD_DATA0-3 | 图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C |
| U4 | EA3036 | 从 VCC_5V 产生 VCC_3V3、VDD_3V3 和 AMP_PWR 的三路降压器 | 图 91b865957940 / 第 1 页 / 网格 A1-B2，U4 EA3036 与三路 SW/FB 网络 |
| U10 | IP5306 | VIN_USB、VBAT 与 VCC_5V 之间的充放电及升压电源管理器 | 图 91b865957940 / 第 1 页 / 网格 C1-D2，U10 IP5306 与 0x75 注释 |
| ANT1,C1,L1,C9 | 未标注 | ESP_LNA 到 ANT1 的预留 T 型射频匹配网络 | 图 d81402da2106 / 第 1 页 / 网格 A2，ESP_LNA、L1/C1/C9 TBD 与 ANT1 |
| X1 | 40MHz/+/-10ppm/22pF | ESP32 主晶振，配 C21/C22 22pF | 图 d81402da2106 / 第 1 页 / 网格 C1，X1、ESP_XTAL_N/P、C21/C22 |
| U3 | CP2104 | 2017 原理图中的 USB-UART 桥，连接 ESP32 UART0 与自动下载电路 | 图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104 |
| U5 | USB_Micro | 图中 USB 电源与 D+/D- 连接器符号 | 图 2f5b17c1e346 / 第 1 页 / 网格 A4，U5 USB_Micro、FUSE1 与 D+/D- |
| U6,FET1 | M5-LCD / AO3402 | SPI LCD 接口及 GPIO32 控制的背光低端开关 | 图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，U6 M5-LCD 与 FET1 AO3402 |
| U8 | MicroSD-SPI | TF 卡槽，使用 GPIO4/23/18/19 的 SPI 接口 | 图 2f5b17c1e346 / 第 1 页 / 网格 D1-D2，U8 MicroSD-SPI |
| S1-S4 | SMT-3x6-SWC / SMT_SW_TS_015 | GPIO37/38/39 用户按键和 PWR 复位/电源按键 | 图 2f5b17c1e346 / 第 1 页 / 网格 A1-C1，Button 区 S1-S4 |
| P1 | Header 15X2 | 30 针 M5-Bus，承载 GPIO、UART、I2C、SPI、I2S、电源和电池网络 | 图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B1，P1 Header 15X2 |
| U9 | NS4148 | GPIO25 输入的差分 Class-D 音频放大器，输出 AUDIO_OUT_P/N | 图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148 音频电路 |
| D1,D2,FUSE1 | RLSD52A031V / 2A | USB D+/D- ESD 保护与 VIN_USB 过流保护 | 图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，D1/D2、R9/R11 与 FUSE1 |

## 系统结构

### 所提供 2017 CORE 原理图架构

六页资源封面列出 POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINATION 和 AUDIO AMPLIFER，图框日期为 2017/12/6、Revision A。

- 参数与网络：`title=M5 STACK CORE`；`drawing_revision=A`；`drawing_date=2017/12/6`；`cover_release=A13 OFFICIAL RELEASE VERSION`；`pages=6`
- 证据：图 a44d9e10f49e / 第 1 页 / 封面修订表、PAGE NO. 列表与右下图框

## 核心器件

### U1 ESP32 主控

U1 标注 ESP32-D0WDQ6，3.3V 连接 VDD3P3_RTC、VDD3P3_CPU、VDDA 和 VDD3P3，VDD_SDIO 独立引出到外部 Flash 供电域。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`core_rail=VCC_3V3`；`flash_rail=VDD_SDIO`；`enable=EN/CHIP_PU`；`rf_net=ESP_LNA`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A1-C2，U1 ESP32-D0WDQ6 电源、GPIO 与 SDIO 引脚

## 电源

### IP5306 充放电电源路径

U10 IP5306 的 VIN pin1 接 VIN_USB，VOUT pin8 接 VCC_5V，BAT pin6 与 SW pin7 经电感连接 VBAT，KEY pin5 接 PWR_KEY；页面标注 5V 2.4A Sync Boost 和 2.1A Sync Buck Charger。

- 参数与网络：`device=U10 IP5306`；`input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_annotation=5V 2.4A`；`charger_annotation=2.1A`
- 证据：图 91b865957940 / 第 1 页 / 网格 C1-D2，Power 区 U10 与 VIN_USB/VCC_5V/VBAT/PWR_KEY

### EA3036 三路 3.3V/放大器电源

U4 EA3036 从 VCC_5V 生成 VCC_3V3、VDD_3V3 和 AMP_PWR；三路反馈均使用 510K/110K 分压并各配 22uF/6.3V 输出电容。

- 参数与网络：`input=VCC_5V`；`output1=VCC_3V3 via L2`；`output2=VDD_3V3 via L3`；`output3=AMP_PWR via L5`；`feedback=510K/110K each`；`output_capacitors=C14/C28/C33 22uF/6.3V`
- 证据：图 91b865957940 / 第 1 页 / 网格 A1-B2，U4、L2/L3/L5、反馈分压与输出电容

### LCD 背光开关

U6 三个 BL 引脚汇合到 FET1 AO3402，GPIO32 驱动 FET1 栅极并由 R15 100K 下拉，构成背光开关。

- 参数与网络：`backlight_pins=U6 pins3/4/5`；`switch=FET1 AO3402`；`control=GPIO32`；`pulldown=R15 100K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，GPIO32/FET1/R15/U6 BL

## 接口

### 图中 USB 连接器网络

U5 符号标 USB_Micro：VCC pin1 经 FUSE1 2A 接 VIN_USB，D- pin2 和 D+ pin3 分别经 R9/R11 22R 接 USB_DN/USB_DP，ID pin4 未连接，GND pin5 与外壳接地。

- 参数与网络：`reference=U5`；`symbol=USB_Micro`；`vbus=FUSE1 2A -> VIN_USB`；`d_minus=R9 22R -> USB_DN`；`d_plus=R11 22R -> USB_DP`；`id=NC`；`ground=pin5,MH1,MH2`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，U5 USB_Micro

### M5-LCD 接口映射

U6 M5-LCD 的 #RST、R/S、MOSI、SCK、CS 分别连接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14，VCC 接 VDD_3V3。

- 参数与网络：`reference=U6 M5-LCD`；`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，LCD 区 U6

### 30 针 M5-Bus

P1 是 Header 15X2；pins1-10 为 GND/GPIO35、GND/GPIO36、GND/EN、GPIO23/GPIO25、GPIO19/GPIO26，pins11-20 为 EXT_SCK/VDD_3V3、GPIO3/GPIO1、GPIO16/GPIO17、GPIO21/GPIO22、GPIO2/GPIO5，pins21-30 为 GPIO12/GPIO13、GPIO15/GPIO0、HPWR/GPIO34、HPWR/VCC_5V、HPWR/VBAT。

- 参数与网络：`pins_1_10=1 GND,2 GPIO35,3 GND,4 GPIO36,5 GND,6 EN,7 GPIO23,8 GPIO25,9 GPIO19,10 GPIO26`；`pins_11_20=11 EXT_SCK,12 VDD_3V3,13 GPIO3,14 GPIO1,15 GPIO16,16 GPIO17,17 GPIO21,18 GPIO22,19 GPIO2,20 GPIO5`；`pins_21_30=21 GPIO12,22 GPIO13,23 GPIO15,24 GPIO0,25 HPWR,26 GPIO34,27 HPWR,28 VCC_5V,29 HPWR,30 VBAT`；`clock_link=EXT_SCK via R2 22R to GPIO18`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 A1-B2，P1 15X2 与 M5-Bus 功能表

## 总线

### LCD 与 TF 卡共享 SPI

LCD 和 TF 卡共享 GPIO23 MOSI 与 GPIO18 SCK；TF 卡使用 GPIO19 MISO 和 GPIO4 CS，LCD 使用 GPIO14 CS、GPIO27 R/S、GPIO33 #RST。

- 参数与网络：`shared_mosi=GPIO23`；`shared_clock=GPIO18`；`tf_miso=GPIO19`；`tf_cs=GPIO4`；`lcd_cs=GPIO14`；`lcd_dc=GPIO27`；`lcd_reset=GPIO33`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 B3-D4，LCD 与 TF Card 两区

## 总线地址

### 定制 IP5306 I2C 地址

电源页文字明确说明该定制 IP5306 通过 IIC 与 ESP32 通信，IIC address is 0x75。

- 参数与网络：`device=U10 IP5306`；`bus=IIC`；`address_7bit=0x75`；`gpio_mapping=null`
- 证据：图 91b865957940 / 第 1 页 / 网格 D1-D2，IP5306 下方定制 IIC 与 0x75 文字

## GPIO 与控制信号

### 三个用户按键

S1/S2/S3 分别把 GPIO37/GPIO38/GPIO39 按下接地，对应 Btn C/Btn B/Btn A；R4/R7/R10 各 100K 上拉到 VDD_3V3，并各有对地保护二极管。

- 参数与网络：`button_c=S1 GPIO37 active-low`；`button_b=S2 GPIO38 active-low`；`button_a=S3 GPIO39 active-low`；`pullups=R4/R7/R10 100K to VDD_3V3`；`protection=D24/D26/D27`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-B1，Button 区 S1-S3

## 时钟

### ESP32 40MHz 晶振

X1 标注 40MHz/+/-10ppm/22pF，连接 ESP_XTAL_N 与 ESP_XTAL_P，并由 C21、C22 各 22pF 接地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`tolerance=+/-10ppm`；`load_annotation=22pF`；`capacitors=C21=22pF,C22=22pF`；`nets=ESP_XTAL_N,ESP_XTAL_P`
- 证据：图 d81402da2106 / 第 1 页 / 网格 C1，X1 与 C21/C22

## 复位

### EN 与 PWR 按键网络

EN 由 R12 12K 上拉到 VCC_3V3 并由 C25 1nF 对地，PWR 通过一只 12K 电阻连接 EN；S4 按下将 PWR 接地，PWR 另有 R13 100K、C7 1nF 和 D28 对地网络。

- 参数与网络：`enable_pullup=R12 12K`；`enable_capacitor=C25 1nF`；`pwr_to_en=12K`；`button=S4 PWR to GND`；`pwr_network=R13 100K,C7 1nF,D28`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A1-C2，Btn Rst/PWR 与 EN 上拉 RC 区

## 保护电路

### USB 输入保护

USB D-/D+ 各由 D1/D2 RLSD52A031V 对地保护并串联 22R，VBUS 由 FUSE1 2A 串联到 VIN_USB；另画出 USB_CC_1/USB_CC_2 各经 5.10K 接地。

- 参数与网络：`data_esd=D1,D2 RLSD52A031V`；`series=R9=22R,R11=22R`；`vbus_fuse=FUSE1=2A`；`cc_pulldowns=USB_CC_1/USB_CC_2 each 5.10K to GND`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，USB-PD Recognition 与 U5 输入保护

### M5-Bus GPIO 对地保护

M5-Bus 页在 GPIO23/35、GPIO19/36、EXT_SCK/EN、GPIO3/25、GPIO16/26、GPIO21/1、GPIO2/17、GPIO12/22、GPIO15/5、GPIO13、GPIO0、GPIO34 网络上画有 RLSD52A031V 对地保护二极管阵列。

- 参数与网络：`part=RLSD52A031V`；`protected_nets=GPIO23,GPIO35,GPIO19,GPIO36,EXT_SCK,EN,GPIO3,GPIO25,GPIO16,GPIO26,GPIO21,GPIO1,GPIO2,GPIO17,GPIO12,GPIO22,GPIO15,GPIO5,GPIO13,GPIO0,GPIO34`；`ground=GND`
- 证据：图 72aa5b4d2f89 / 第 1 页 / 网格 B1-D1，D2-D23 保护阵列

## 存储

### GD25Q32C 外部 Flash 连接

U2 GD25Q32C 的 nCS、CLK、DI/IO0、DO/IO1、nHOLD/IO3、nWP/IO2 分别连接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA2、SD_DATA3，VCC 接 VCC_3V3。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`cs=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2`；`supply=VCC_3V3`
- 证据：图 d81402da2106 / 第 1 页 / 网格 B2，U2 GD25Q32C 引脚与 SD_* 网络

### TF 卡 SPI 映射

U8 MicroSD-SPI 的 CS、DI、SCLK、DO 分别连接 GPIO4、GPIO23、GPIO18、GPIO19；VDD 接 VDD_3V3，R17/R18/R20/R21 各 12K 上拉 SPI_SDCS、SPI_SDDI、SPI_CLK、SPI_SDDO。

- 参数与网络：`reference=U8`；`cs=GPIO4/SPI_SDCS`；`mosi=GPIO23/SPI_SDDI`；`clock=GPIO18/SPI_CLK via R22 22R`；`miso=GPIO19/SPI_SDDO`；`supply=VDD_3V3`；`pullups=R17/R18/R20/R21 12K`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 C1-D2，TF Card 区 U8、上拉与 R22

## 音频

### NS4148 音频放大链路

GPIO25 经 C43 100nF 接 U9 NS4148 INP，INN 经 C44 100nF 接 PGND；U9 由 AMP_PWR 供电，VOP/VON 分别经 FB1/FB2 600R@100M 输出 AUDIO_OUT_P/AUDIO_OUT_N，并各有 1nF 对地电容。

- 参数与网络：`amplifier=U9 NS4148`；`input=GPIO25 via C43 100nF to INP`；`negative_input=PGND via C44 100nF to INN`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`ferrites=FB1/FB2 600R@100M`；`output_capacitors=C42/C45 1nF`
- 证据：图 8d7498c3a5a7 / 第 1 页 / 网格 A1-B2，U9 NS4148、输入、供电与差分输出

## 射频

### ESP32 射频匹配与天线

ESP_LNA 通过 C1 串联到 ANT1，L1 在输入侧对地、C9 在天线侧对地；L1、C1、C9 数值均标 TBD，页面要求按实际阻抗匹配结果决定。

- 参数与网络：`source_net=ESP_LNA`；`antenna=ANT1`；`series=C1 TBD`；`shunt_input=L1 TBD`；`shunt_output=C9 TBD`；`topology=T matching`
- 证据：图 d81402da2106 / 第 1 页 / 网格 A2，Depend on Actual Impedance Matching Result 区

## 调试与烧录

### CP2104 到 ESP32 UART0

U3 CP2104 TXD pin21 经 R8 470R 接 RXD0/GPIO3，RXD pin20 接 TXD0/GPIO1；USB_DP/USB_DN 分别进入 DP/DM。

- 参数与网络：`bridge=U3 CP2104`；`bridge_txd=R8 470R -> RXD0/GPIO3`；`bridge_rxd=TXD0/GPIO1`；`usb_dp=U3 DP pin3`；`usb_dn=U3 DM pin4`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104、R8 与 GPIO1/GPIO3

### UART 自动下载控制

CP2104 的 DTR 与 RTS 通过 R16/R19 12K 和两只 NPN-S8050 晶体管驱动 EN 与 GPIO0，构成 Auto-download Circuit。

- 参数与网络：`control_inputs=DTR,RTS`；`resistors=R16=12K,R19=12K`；`transistors=two NPN-S8050`；`targets=EN,GPIO0`
- 证据：图 2f5b17c1e346 / 第 1 页 / 网格 D2-D3，Auto-Download 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 所提供 2017 CORE 原理图架构 | `title=M5 STACK CORE`；`drawing_revision=A`；`drawing_date=2017/12/6`；`cover_release=A13 OFFICIAL RELEASE VERSION`；`pages=6` |
| 核心器件 | U1 ESP32 主控 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`core_rail=VCC_3V3`；`flash_rail=VDD_SDIO`；`enable=EN/CHIP_PU`；`rf_net=ESP_LNA` |
| 电源 | IP5306 充放电电源路径 | `device=U10 IP5306`；`input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_annotation=5V 2.4A`；`charger_annotation=2.1A` |
| 总线地址 | 定制 IP5306 I2C 地址 | `device=U10 IP5306`；`bus=IIC`；`address_7bit=0x75`；`gpio_mapping=null` |
| 电源 | EA3036 三路 3.3V/放大器电源 | `input=VCC_5V`；`output1=VCC_3V3 via L2`；`output2=VDD_3V3 via L3`；`output3=AMP_PWR via L5`；`feedback=510K/110K each`；`output_capacitors=C14/C28/C33 22uF/6.3V` |
| 时钟 | ESP32 40MHz 晶振 | `reference=X1`；`frequency=40MHz`；`tolerance=+/-10ppm`；`load_annotation=22pF`；`capacitors=C21=22pF,C22=22pF`；`nets=ESP_XTAL_N,ESP_XTAL_P` |
| 存储 | GD25Q32C 外部 Flash 连接 | `reference=U2`；`part_number=GD25Q32C`；`cs=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2`；`supply=VCC_3V3` |
| 射频 | ESP32 射频匹配与天线 | `source_net=ESP_LNA`；`antenna=ANT1`；`series=C1 TBD`；`shunt_input=L1 TBD`；`shunt_output=C9 TBD`；`topology=T matching` |
| 调试与烧录 | CP2104 到 ESP32 UART0 | `bridge=U3 CP2104`；`bridge_txd=R8 470R -> RXD0/GPIO3`；`bridge_rxd=TXD0/GPIO1`；`usb_dp=U3 DP pin3`；`usb_dn=U3 DM pin4` |
| 调试与烧录 | UART 自动下载控制 | `control_inputs=DTR,RTS`；`resistors=R16=12K,R19=12K`；`transistors=two NPN-S8050`；`targets=EN,GPIO0` |
| 接口 | 图中 USB 连接器网络 | `reference=U5`；`symbol=USB_Micro`；`vbus=FUSE1 2A -> VIN_USB`；`d_minus=R9 22R -> USB_DN`；`d_plus=R11 22R -> USB_DP`；`id=NC`；`ground=pin5,MH1,MH2` |
| 保护电路 | USB 输入保护 | `data_esd=D1,D2 RLSD52A031V`；`series=R9=22R,R11=22R`；`vbus_fuse=FUSE1=2A`；`cc_pulldowns=USB_CC_1/USB_CC_2 each 5.10K to GND` |
| GPIO 与控制信号 | 三个用户按键 | `button_c=S1 GPIO37 active-low`；`button_b=S2 GPIO38 active-low`；`button_a=S3 GPIO39 active-low`；`pullups=R4/R7/R10 100K to VDD_3V3`；`protection=D24/D26/D27` |
| 复位 | EN 与 PWR 按键网络 | `enable_pullup=R12 12K`；`enable_capacitor=C25 1nF`；`pwr_to_en=12K`；`button=S4 PWR to GND`；`pwr_network=R13 100K,C7 1nF,D28` |
| 接口 | M5-LCD 接口映射 | `reference=U6 M5-LCD`；`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`chip_select=GPIO14`；`supply=VDD_3V3` |
| 电源 | LCD 背光开关 | `backlight_pins=U6 pins3/4/5`；`switch=FET1 AO3402`；`control=GPIO32`；`pulldown=R15 100K` |
| 存储 | TF 卡 SPI 映射 | `reference=U8`；`cs=GPIO4/SPI_SDCS`；`mosi=GPIO23/SPI_SDDI`；`clock=GPIO18/SPI_CLK via R22 22R`；`miso=GPIO19/SPI_SDDO`；`supply=VDD_3V3`；`pullups=R17/R18/R20/R21 12K` |
| 总线 | LCD 与 TF 卡共享 SPI | `shared_mosi=GPIO23`；`shared_clock=GPIO18`；`tf_miso=GPIO19`；`tf_cs=GPIO4`；`lcd_cs=GPIO14`；`lcd_dc=GPIO27`；`lcd_reset=GPIO33` |
| 接口 | 30 针 M5-Bus | `pins_1_10=1 GND,2 GPIO35,3 GND,4 GPIO36,5 GND,6 EN,7 GPIO23,8 GPIO25,9 GPIO19,10 GPIO26`；`pins_11_20=11 EXT_SCK,12 VDD_3V3,13 GPIO3,14 GPIO1,15 GPIO16,16 GPIO17,17 GPIO21,18 GPIO22,19 GPIO2,20 GPIO5`；`pins_21_30=21 GPIO12,22 GPIO13,23 GPIO15,24 GPIO0,25 HPWR,26 GPIO34,27 HPWR,28 VCC_5V,29 HPWR,30 VBAT`；`clock_link=EXT_SCK via R2 22R to GPIO18` |
| 保护电路 | M5-Bus GPIO 对地保护 | `part=RLSD52A031V`；`protected_nets=GPIO23,GPIO35,GPIO19,GPIO36,EXT_SCK,EN,GPIO3,GPIO25,GPIO16,GPIO26,GPIO21,GPIO1,GPIO2,GPIO17,GPIO12,GPIO22,GPIO15,GPIO5,GPIO13,GPIO0,GPIO34`；`ground=GND` |
| 音频 | NS4148 音频放大链路 | `amplifier=U9 NS4148`；`input=GPIO25 via C43 100nF to INP`；`negative_input=PGND via C44 100nF to INN`；`supply=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`ferrites=FB1/FB2 600R@100M`；`output_capacitors=C42/C45 1nF` |
| 系统结构 | Core Metal 与资源版本对应关系 | `product=Core Metal`；`sku=C001-CNC`；`schematic_title=M5 STACK CORE`；`schematic_date=2017/12/6`；`schematic_revision=A`；`core_metal_schematic=null` |
| 内存与 Flash | Core Metal SoC 与 16MB Flash | `documented_soc=ESP32-D0WDQ6-V3`；`schematic_soc=ESP32-D0WDQ6`；`documented_flash=16MB`；`schematic_flash=GD25Q32C`；`production_flash_part=null` |
| 调试与烧录 | Core Metal USB-UART 桥型号 | `documented=CH9102F`；`driver_family=CH9102`；`schematic=U3 CP2104`；`production_part=null` |
| 接口 | Core Metal USB Type-C 实现 | `documented_connector=USB Type-C`；`schematic_symbol=U5 USB_Micro`；`cc_network=two 5.10K pulldowns drawn separately`；`connector_cc_pins=null`；`c2c_pd_support=null` |
| 核心器件 | Core Metal LCD 面板 | `documented_part=ILI9342C`；`documented_size=2.0 inch`；`documented_resolution=320x240`；`documented_brightness=853nit`；`schematic_label=M5-LCD`；`production_panel=null` |
| 总线 | IP5306 I2C GPIO 映射 | `documented_scl=GPIO22`；`documented_sda=GPIO21`；`address=0x75`；`u10_bus_pins=null`；`schematic_connection=null` |
| 射频 | 铝合金外壳与 2.4G 天线 | `documented_enclosure=aluminum alloy CNC`；`documented_antenna=2.4G 3D antenna`；`schematic_antenna=ANT1`；`matching_values=TBD`；`enclosure_coupling=null`；`rf_test=null` |
| 音频 | Core Metal 1W-0928 扬声器 | `documented_speaker=1W-0928`；`amplifier=U9 NS4148`；`output=AUDIO_OUT_P/N`；`speaker_part=null`；`impedance=null`；`connector=null` |
| 电源 | Core Metal 输入额定值 | `documented_input=5V@500mA`；`usb_fuse=2A`；`boost_annotation=5V 2.4A`；`charger_annotation=2.1A`；`input_tolerance=null`；`system_max_current=null` |

## 待确认事项

- `system.core-metal-resource-version`：产品为 Core Metal/C001-CNC，正文描述铝合金 CNC 纪念版和后续 Core 配置；所提供六页仅标 2017 M5 STACK CORE Revision A，没有 Core Metal、C001-CNC、外壳或具体 PCB 版本标识，当前适用范围需确认。（证据：图 a44d9e10f49e / 第 1 页 / 封面与 2017 Revision A 图框，无 Core Metal/SKU）
- `memory.core-metal-soc-flash`：正文称 ESP32-D0WDQ6-V3 和 16MB Flash；旧图 U1 标 ESP32-D0WDQ6、U2 标 GD25Q32C，未显示 V3 后缀或 16MB Flash 料号，Core Metal 量产配置需确认。（证据：图 d81402da2106 / 第 1 页 / U1 ESP32-D0WDQ6 与 U2 GD25Q32C）
- `debug.core-metal-usb-bridge`：正文规格列 CH9102F，驱动章节也面向 CH9102；所提供 USB-UART 页仍为 U3 CP2104，Core Metal 实机桥接芯片及自动下载外围需确认。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 A2-C3，U3 CP2104）
- `interface.core-metal-usb-typec`：正文称 USB Type-C，页面标题框也写 Type-C USB 并画 USB_CC_1/USB_CC_2 下拉，但实际连接器 U5 符号标 USB_Micro 且未画 CC 引脚连接，Core Metal Type-C 与 C2C/PD 实现需确认。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 A3-A4，Type-C USB、USB-PD Recognition 与 U5 USB_Micro）
- `component.core-metal-lcd`：正文称 2.0 英寸 320x240 ILI9342C IPS 面板、最高亮度 853nit；旧图 U6 仅标 M5-LCD 并给出接口网络，没有面板型号、分辨率、亮度或 Core Metal 专属屏幕证据。（证据：图 2f5b17c1e346 / 第 1 页 / 网格 B3-C4，U6 M5-LCD）
- `bus.documented-ip5306-i2c`：正文把 IP5306 0x75 的 SCL/SDA 映射为 GPIO22/GPIO21；电源页只有 IIC 地址文字和不含 SCL/SDA 的 U10 符号，M5-Bus 页只显示 GPIO21/22 引出，无法从旧图闭合确认该 I2C 连接。（证据：图 91b865957940 / 第 1 页 / U10 IP5306 符号与 IIC 0x75 文字，无 SDA/SCL 引脚; 图 72aa5b4d2f89 / 第 1 页 / P1 pins17/18 GPIO21/GPIO22）
- `rf.core-metal-enclosure-antenna`：正文称铝合金 CNC 外壳、2.4G 3D 天线并提供天线信号强度说明；旧图只画 ANT1 和数值为 TBD 的匹配网络，没有 Core Metal 外壳耦合、天线料号、匹配值、布局或射频测试数据。（证据：图 d81402da2106 / 第 1 页 / 网格 A2，ANT1 与 L1/C1/C9 TBD；无外壳信息）
- `audio.core-metal-speaker`：正文规格称扬声器为 1W-0928；旧图只显示 U9 NS4148 和 AUDIO_OUT_P/N 网络，没有扬声器器件、连接器、阻抗或额定功率，实机料件需确认。（证据：图 8d7498c3a5a7 / 第 1 页 / 音频页 AUDIO_OUT_P/N 终止于网络标号，无扬声器器件）
- `power.core-metal-input-rating`：正文规格称输入 5V@500mA；旧图显示 FUSE1 2A、IP5306 的 5V 2.4A 升压和 2.1A 充电注释，但没有 USB 输入电压容差、整机最大电流或 500mA 测试条件。（证据：图 91b865957940 / 第 1 页 / 电源页 IP5306 5V 2.4A/2.1A 注释; 图 2f5b17c1e346 / 第 1 页 / USB 页 FUSE1 2A 到 VIN_USB）
- `review.resource-version`：请提供 Core Metal/C001-CNC 当前正式原理图、PCB 或 BOM，确认 2017 Revision A 六页资源的适用范围。；原因：资源没有 Core Metal、SKU 或金属版 PCB 标识。
- `review.soc-flash`：请由 Core Metal BOM 确认 ESP32-D0WDQ6-V3 与 16MB Flash 的实际料号和存储实现。；原因：旧图只显示 ESP32-D0WDQ6 与 GD25Q32C。
- `review.usb-bridge`：请确认 Core Metal 使用的 CH9102F 料号、引脚连接和自动下载外围。；原因：提供的页仍画 CP2104。
- `review.usb-typec`：请确认 Core Metal Type-C 连接器、CC1/CC2 接法及 C2C/PD 兼容边界。；原因：旧图 U5 是 USB_Micro 符号，CC 网络未连到连接器。
- `review.lcd`：请确认 Core Metal LCD 的 ILI9342C 料号、面板连接器、分辨率和背光额定参数。；原因：旧图只标 M5-LCD。
- `review.ip5306-bus`：请确认 IP5306 0x75 的 SDA/SCL 是否分别连接 GPIO21/GPIO22，并提供 U10 完整引脚图。；原因：电源页未画 U10 的 I2C 引脚或网络。
- `review.enclosure-antenna`：请提供 Core Metal 金属外壳下的天线料号、匹配值、布局约束与射频测试结果。；原因：旧图只画 ANT1/TBD 匹配，无法说明金属外壳对天线的影响。
- `review.speaker`：请确认 1W-0928 扬声器的料号、阻抗、连接器和 NS4148 匹配参数。；原因：旧图没有扬声器器件。
- `review.input-rating`：请确认 Core Metal USB 输入容差、500mA 额定定义、保险丝规格及最大充放电条件。；原因：正文输入额定与旧图 2A/2.4A/2.1A 注释不是同一测试条件。

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

源文档：`zh_CN/core/CORE Metal.md`

源文档 SHA-256：`6a4d32b441705d459da12fc5430754067c05a7a4be11b653c65270d134de511b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
