# Fire v2.7 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Fire v2.7 |
| SKU | K007-V27 |
| 产品 ID | `fire-v2-7-970c16a4d3f5` |
| 源文档 | `zh_CN/core/fire_v2.7.md` |

## 概述

Fire v2.7 条目随附的是 2017-12-06 通用 M5 Stack Core 六页原理图，而非 Fire v2.7 专属全套图。旧图确认 ESP32-D0WDQ6、GD25Q32C、EA3036、定制 I2C IP5306、CP2104、M5-LCD、microSD、30 Pin M5-Bus 与 NS4148 音频链；v2.7 的 PSRAM、CH9102、MPU6886、RGB、麦克风和 M5GO 底座需用当前版本资料复核。

## 检索关键词

`Fire v2.7`、`K007-V27`、`M5 Stack Core`、`2017 schematic`、`ESP32-D0WDQ6`、`GD25Q32C`、`EA3036`、`IP5306`、`0x75`、`CP2104`、`M5-LCD`、`MicroSD-SPI`、`NS4148`、`M5-Bus`、`GPIO25`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO14`、`GPIO4`、`GPIO37`、`GPIO38`、`GPIO39`、`VCC_3V3`、`VDD_3V3`、`AMP_PWR`、`VIN_USB`、`VBAT`、`version mismatch`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-D0WDQ6 | 随附旧版 Core 图中的主控制器 | 图 d81402da2106 / 第 1 页 / A1-C1 U1 主控符号，底部标注 ESP32-D0WDQ6 |
| U2 | GD25Q32C | 随附旧版 Core 图中的外部 SPI Flash | 图 d81402da2106 / 第 1 页 / B2 U2 GD25Q32C 与 SD_CMD/SD_CLK/SD_DATA 网络 |
| X1 | 40MHz/+/-10ppm/22pF | ESP32 主晶振 | 图 d81402da2106 / 第 1 页 / C1 X1 晶振及 ESP_XTAL_N/P |
| U4 | EA3036 | 三路同步降压转换器 | 图 91b865957940 / 第 1 页 / A1-B2 U4 EA3036 与三路 SW 输出 |
| U10 | IP5306 | 定制 I2C 充放电与 5 V 升压电源管理 | 图 91b865957940 / 第 1 页 / C1-D2 U10 IP5306，连接 VIN_USB、VCC_5V、VBAT、PWR_KEY |
| U3 | CP2104 | 随附旧版 Core 图中的 USB-UART 桥接器 | 图 2f5b17c1e346 / 第 1 页 / A2-C3 U3 CP2104，连接 USB_DP/USB_DN 与 TXD/RXD |
| U5 | USB connector | USB 电源与差分数据接口 | 图 2f5b17c1e346 / 第 1 页 / A3-A4 Type-C USB 区域 U5、FUSE1、USB_DP/USB_DN |
| U6 | M5-LCD | SPI LCD 模块 | 图 2f5b17c1e346 / 第 1 页 / B3-C4 U6 M5-LCD，引出 BL、#RST、R/S、MOSI、SCK、CS |
| U8 | MicroSD-SPI | microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / D1-D2 U8 MicroSD-SPI 卡座 |
| P1 | Header 15X2 | 30 Pin M5-Bus 扩展连接器 | 图 72aa5b4d2f89 / 第 1 页 / A1-B1 P1 Header 15X2 与中央 1-30 脚表 |
| U9 | NS4148 | Class-D 差分音频功率放大器 | 图 8d7498c3a5a7 / 第 1 页 / A1-B2 U9 NS4148 与 AUDIO_OUT_P/N |
| FET1 | AO3402 | LCD 背光低侧开关 | 图 2f5b17c1e346 / 第 1 页 / B3 LCD 区域 FET1 AO3402，栅极接 GPIO32 |
| S1/S2/S3/S4 | SMT switch | Button C、Button B、Button A 和复位按键 | 图 2f5b17c1e346 / 第 1 页 / A1-B1 Button 区域 S1/S2/S3/S4 |

## 系统结构

### 随附原理图版本

封面修订表列出 A13 Official Release Version，日期 10/11/2017；页标题栏标注 M5 STACK CORE、Revision A、日期 2017/12/6。

- 参数与网络：`release_revision=A13`；`release_date=10/11/2017`；`title_revision=A`；`title_date=2017/12/6`
- 证据：图 a44d9e10f49e / 第 1 页 / A1-A3 修订表及 D3-D4 标题栏

### 旧版 Core 主控制器

随附图 U1 的器件型号标注为 ESP32-D0WDQ6。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`scope=supplied 2017 Core schematic`
- 证据：图 d81402da2106 / 第 1 页 / A1-C1 U1 主控符号底部 ESP32-D0WDQ6 标注

## 电源

### EA3036 三路降压

U4 EA3036 由 VCC_5V 供电，SW1、SW2、SW3 分别经 L2、L3、L5 输出 VCC_3V3、VDD_3V3、AMP_PWR，三路反馈均为 510 kΩ/110 kΩ。

- 参数与网络：`reference=U4`；`input=VCC_5V`；`output_1=VCC_3V3`；`output_2=VDD_3V3`；`output_3=AMP_PWR`；`feedback=510k/110k`
- 证据：图 91b865957940 / 第 1 页 / A1-B2 U4 EA3036、L2/L3/L5 和三组反馈分压

### IP5306 充放电管理

U10 IP5306 的 VIN 接 VIN_USB、VOUT 接 VCC_5V、BAT/SW 连接 VBAT 与 1 µH 电感，KEY 接 PWR_KEY；图面标注 5 V 2.4 A 同步升压和 2.1 A 同步降压充电。

- 参数与网络：`reference=U10`；`input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_rating=5V 2.4A`；`charger_rating=2.1A`
- 证据：图 91b865957940 / 第 1 页 / C1-D2 U10 IP5306 与 5V 2.4A/2.1A 注记

## 接口

### 旧版 USB 接口

U5 的 VCC 经 FUSE1 2 A 接 VIN_USB，D-/D+ 分别经 R9/R11 22 Ω 连接 USB_DN/USB_DP，并由 D1/D2 RLSD52A031V 对地保护。

- 参数与网络：`reference=U5`；`supply=VIN_USB`；`fuse=FUSE1 2A`；`d_minus=USB_DN via R9 22R`；`d_plus=USB_DP via R11 22R`；`protection=D1,D2 RLSD52A031V`
- 证据：图 2f5b17c1e346 / 第 1 页 / A3-A4 Type-C USB 区域 U5、FUSE1、R9/R11、D1/D2

### 旧版 CP2104 USB-UART

U3 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD 经 R8 470 Ω 接 RXD0/GPIO3，RXD 接 TXD0/GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`reference=U3`；`part_number=CP2104`；`usb_dp=USB_DP`；`usb_dm=USB_DN`；`uart_tx=RXD0/GPIO3 via R8 470R`；`uart_rx=TXD0/GPIO1`；`control=RTS,DTR`
- 证据：图 2f5b17c1e346 / 第 1 页 / A2-C3 U3 CP2104 的 DP/DM、TXD/RXD、RTS/DTR

### 旧版 M5-LCD 接口

U6 M5-LCD 的 #RST=GPIO33、R/S=GPIO27、MOSI=GPIO23、SCK=GPIO18、CS=GPIO14；三只 BL 引脚由 FET1 AO3402 控制，栅极接 GPIO32 并由 R15 100 kΩ 下拉。

- 参数与网络：`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`backlight=GPIO32 via FET1 AO3402`；`pulldown=R15 100k`
- 证据：图 2f5b17c1e346 / 第 1 页 / B3-C4 LCD 区域 U6 与 FET1/R15

### 30 Pin M5-Bus

P1 的 1–30 脚依次为 GND、GPIO35、GND、GPIO36、GND、EN、GPIO23、GPIO25、GPIO19、GPIO26、EXT_SCK、VDD_3V3、GPIO3、GPIO1、GPIO16、GPIO17、GPIO21、GPIO22、GPIO2、GPIO5、GPIO12、GPIO13、GPIO15、GPIO0、HPWR、GPIO34、HPWR、VCC_5V、HPWR、VBAT。

- 参数与网络：`pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:EXT_SCK,12:VDD_3V3,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:VCC_5V,29:HPWR,30:VBAT`
- 证据：图 72aa5b4d2f89 / 第 1 页 / A1-B2 P1 Header 15X2 与中央 M5-Bus 1-30 脚表

## 总线

### LCD 与 microSD 共享 SPI

LCD 与 microSD 共享 GPIO23(MOSI) 和 GPIO18(SCK)，microSD 另用 GPIO19(MISO)，片选分别为 LCD GPIO14 与 microSD GPIO4。

- 参数与网络：`shared_mosi=GPIO23`；`shared_sck=GPIO18`；`microsd_miso=GPIO19`；`lcd_cs=GPIO14`；`microsd_cs=GPIO4`
- 证据：图 2f5b17c1e346 / 第 1 页 / 右侧 LCD U6 与左下 TF Card U8 的 GPIO23/GPIO18 和各自 CS

### M5-Bus EXT_SCK

M5-Bus 11 脚 EXT_SCK 经 R2 22 Ω 串联电阻连接 ESP32 GPIO18。

- 参数与网络：`bus_pin=11`；`signal=EXT_SCK`；`gpio=GPIO18`；`series_resistor=R2 22R`
- 证据：图 72aa5b4d2f89 / 第 1 页 / B1 EXT_SCK-R2 22R-GPIO18

## 总线地址

### 定制 IP5306 I2C 地址

图面说明定制 IP5306 通过 IIC 与 ESP32 通信，IIC 地址为 0x75。

- 参数与网络：`part_number=IP5306`；`i2c_address=0x75`
- 证据：图 91b865957940 / 第 1 页 / D1-D2 Power 区域下方 customized IP5306 ... IIC address is 0x75

## GPIO 与控制信号

### 三枚用户按键与复位按键

S1 Button C、S2 Button B、S3 Button A 分别连接 GPIO37、GPIO38、GPIO39，按下时接地；S4 Btn Rst 连接 PWR 网络，PWR 经 12 kΩ 电阻连接 EN。

- 参数与网络：`button_c=S1/GPIO37`；`button_b=S2/GPIO38`；`button_a=S3/GPIO39`；`reset_button=S4/PWR`；`reset_target=EN via 12k`
- 证据：图 2f5b17c1e346 / 第 1 页 / A1-B2 Button 区域 GPIO37/38/39、S1-S4 与 PWR-EN

## 时钟

### ESP32 主晶振

X1 为 40 MHz、±10 ppm、22 pF 负载晶振，连接 ESP_XTAL_N/P，C21、C22 均为 22 pF 并接地。

- 参数与网络：`reference=X1`；`frequency_hz=40000000`；`tolerance_ppm=10`；`load_capacitance_pf=22`；`capacitors=C21=22pF,C22=22pF`
- 证据：图 d81402da2106 / 第 1 页 / C1 X1、ESP_XTAL_N/P、C21/C22

## 复位

### 自动下载电路

DTR/RTS 分别经 R16/R19 两只 12 kΩ 电阻驱动 NPN-S8050 晶体管网络，以控制 EN 和 GPIO0。

- 参数与网络：`inputs=DTR,RTS`；`outputs=EN,GPIO0`；`resistors=R16=12k,R19=12k`；`transistors=NPN-S8050`
- 证据：图 2f5b17c1e346 / 第 1 页 / C2-D3 Auto-Download 区域

## 保护电路

### M5-Bus 信号保护

M5-Bus 引出的 GPIO23、GPIO19、EXT_SCK、GPIO3、GPIO16、GPIO21、GPIO2、GPIO12、GPIO15、GPIO35、GPIO36、EN、GPIO25、GPIO26、GPIO1、GPIO17、GPIO22、GPIO5、GPIO13、GPIO0、GPIO34 使用 RLSD52A031V 阵列对地保护。

- 参数与网络：`part_number=RLSD52A031V`；`signals=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34`
- 证据：图 72aa5b4d2f89 / 第 1 页 / B1-D1 D2-D23 RLSD52A031V 及两侧信号

## 存储

### 旧版 Core 外部 Flash

U2 为 GD25Q32C，nCS 接 SD_CMD，CLK 接 SD_CLK，DI/IO0 接 SD_DATA1，DO/IO1 接 SD_DATA0，nWP/IO2 接 SD_DATA3，nHOLD/IO3 接 SD_DATA2。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`chip_select=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2`
- 证据：图 d81402da2106 / 第 1 页 / B2 U2 GD25Q32C 六条 SD_* 连接

### microSD SPI 接口

U8 MicroSD-SPI 的 CS=GPIO4、DI/MOSI=GPIO23、SCLK=GPIO18、DO/MISO=GPIO19；SCLK 串联 R22 22 Ω，四路有 12 kΩ 上拉和 RLSD52A031V 对地保护。

- 参数与网络：`chip_select=GPIO4`；`mosi=GPIO23`；`sclk=GPIO18`；`miso=GPIO19`；`clock_resistor=R22 22R`；`pullups=R17,R18,R20,R21 12k`；`protection=D29-D32 RLSD52A031V`
- 证据：图 2f5b17c1e346 / 第 1 页 / C1-D2 TF Card 区域 U8、SPI 网络、上拉与保护

## 音频

### NS4148 音频放大器

GPIO25 经 C43 100 nF 交流耦合到 U9 NS4148 INP，INN 经 C44 100 nF 接 PGND；VOP/VON 分别经 FB1/FB2 600 Ω@100 MHz 磁珠输出 AUDIO_OUT_P/AUDIO_OUT_N。

- 参数与网络：`input_gpio=GPIO25`；`input_coupling=C43 100nF`；`negative_input=PGND via C44 100nF`；`supply=AMP_PWR`；`positive_output=AUDIO_OUT_P via FB1`；`negative_output=AUDIO_OUT_N via FB2`
- 证据：图 8d7498c3a5a7 / 第 1 页 / A1-B2 U9 NS4148、GPIO25、AMP_PWR、FB1/FB2 与 AUDIO_OUT_P/N

### 音频差分输出滤波

AUDIO_OUT_P/N 在 FB1/FB2 后分别通过 C42/C45 1 nF 接地；NS4148 CTRL 经 R37 10 kΩ 接 AMP_PWR，ByPass 通过 C47 1 µF 接地。

- 参数与网络：`positive_shunt=C42 1nF`；`negative_shunt=C45 1nF`；`control=AMP_PWR via R37 10k`；`bypass=C47 1uF`
- 证据：图 8d7498c3a5a7 / 第 1 页 / A1-B2 C42/C45、CTRL-R37 和 ByPass-C47 网络

## 射频

### ESP32 天线网络

ESP32 LNA 引脚经 ESP_LNA 网络和 L1/C1/C9 匹配位置连接 ANT1。

- 参数与网络：`signal=ESP_LNA`；`matching_positions=L1,C1,C9`；`antenna=ANT1`
- 证据：图 d81402da2106 / 第 1 页 / A1-A2 ESP_LNA 至 L1/C1/C9 和 ANT1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 随附原理图版本 | `release_revision=A13`；`release_date=10/11/2017`；`title_revision=A`；`title_date=2017/12/6` |
| 系统结构 | Fire v2.7 版本覆盖范围 | `schematic_scope=2017 M5 Core only`；`schematic_flash=GD25Q32C`；`schematic_usb_uart=CP2104`；`missing_from_assets=PSRAM,MPU6886,RGB LED,microphone,M5GO Bottom`；`source_version=Fire v2.7` |
| 系统结构 | 旧版 Core 主控制器 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`scope=supplied 2017 Core schematic` |
| 存储 | 旧版 Core 外部 Flash | `reference=U2`；`part_number=GD25Q32C`；`chip_select=SD_CMD`；`clock=SD_CLK`；`io0=SD_DATA1`；`io1=SD_DATA0`；`io2=SD_DATA3`；`io3=SD_DATA2` |
| 时钟 | ESP32 主晶振 | `reference=X1`；`frequency_hz=40000000`；`tolerance_ppm=10`；`load_capacitance_pf=22`；`capacitors=C21=22pF,C22=22pF` |
| 射频 | ESP32 天线网络 | `signal=ESP_LNA`；`matching_positions=L1,C1,C9`；`antenna=ANT1` |
| 射频 | 天线匹配元件值 | `inductor_l1=null`；`capacitor_c1=null`；`capacitor_c9=null`；`schematic_label=TBD` |
| 电源 | EA3036 三路降压 | `reference=U4`；`input=VCC_5V`；`output_1=VCC_3V3`；`output_2=VDD_3V3`；`output_3=AMP_PWR`；`feedback=510k/110k` |
| 电源 | IP5306 充放电管理 | `reference=U10`；`input=VIN_USB`；`boost_output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`boost_rating=5V 2.4A`；`charger_rating=2.1A` |
| 总线地址 | 定制 IP5306 I2C 地址 | `part_number=IP5306`；`i2c_address=0x75` |
| 接口 | 旧版 USB 接口 | `reference=U5`；`supply=VIN_USB`；`fuse=FUSE1 2A`；`d_minus=USB_DN via R9 22R`；`d_plus=USB_DP via R11 22R`；`protection=D1,D2 RLSD52A031V` |
| 接口 | 旧版 CP2104 USB-UART | `reference=U3`；`part_number=CP2104`；`usb_dp=USB_DP`；`usb_dm=USB_DN`；`uart_tx=RXD0/GPIO3 via R8 470R`；`uart_rx=TXD0/GPIO1`；`control=RTS,DTR` |
| 复位 | 自动下载电路 | `inputs=DTR,RTS`；`outputs=EN,GPIO0`；`resistors=R16=12k,R19=12k`；`transistors=NPN-S8050` |
| GPIO 与控制信号 | 三枚用户按键与复位按键 | `button_c=S1/GPIO37`；`button_b=S2/GPIO38`；`button_a=S3/GPIO39`；`reset_button=S4/PWR`；`reset_target=EN via 12k` |
| 接口 | 旧版 M5-LCD 接口 | `reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`sck=GPIO18`；`chip_select=GPIO14`；`backlight=GPIO32 via FET1 AO3402`；`pulldown=R15 100k` |
| 存储 | microSD SPI 接口 | `chip_select=GPIO4`；`mosi=GPIO23`；`sclk=GPIO18`；`miso=GPIO19`；`clock_resistor=R22 22R`；`pullups=R17,R18,R20,R21 12k`；`protection=D29-D32 RLSD52A031V` |
| 总线 | LCD 与 microSD 共享 SPI | `shared_mosi=GPIO23`；`shared_sck=GPIO18`；`microsd_miso=GPIO19`；`lcd_cs=GPIO14`；`microsd_cs=GPIO4` |
| 接口 | 30 Pin M5-Bus | `pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:EXT_SCK,12:VDD_3V3,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:VCC_5V,29:HPWR,30:VBAT` |
| 总线 | M5-Bus EXT_SCK | `bus_pin=11`；`signal=EXT_SCK`；`gpio=GPIO18`；`series_resistor=R2 22R` |
| 保护电路 | M5-Bus 信号保护 | `part_number=RLSD52A031V`；`signals=GPIO23,GPIO19,EXT_SCK,GPIO3,GPIO16,GPIO21,GPIO2,GPIO12,GPIO15,GPIO35,GPIO36,EN,GPIO25,GPIO26,GPIO1,GPIO17,GPIO22,GPIO5,GPIO13,GPIO0,GPIO34` |
| 音频 | NS4148 音频放大器 | `input_gpio=GPIO25`；`input_coupling=C43 100nF`；`negative_input=PGND via C44 100nF`；`supply=AMP_PWR`；`positive_output=AUDIO_OUT_P via FB1`；`negative_output=AUDIO_OUT_N via FB2` |
| 音频 | 音频差分输出滤波 | `positive_shunt=C42 1nF`；`negative_shunt=C45 1nF`；`control=AMP_PWR via R37 10k`；`bypass=C47 1uF` |

## 待确认事项

- `system.v27_scope`：随附六页资源仅为 2017 通用 M5 Core 图，显示 GD25Q32C、CP2104 且未显示 PSRAM、MPU6886、RGB LED、麦克风和 M5GO 底座；产品源文档描述 Fire v2.7 的 16 MB Flash、8 MB PSRAM、CH9102F、MPU6886 与 M5GO 底座，现有图面不能确认 v2.7 实物完整 BOM。（证据：图 a44d9e10f49e / 第 1 页 / 封面仅列 POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS、AUDIO AMPLIFIER; 图 d81402da2106 / 第 1 页 / ESP32 页 U2 仅标注 GD25Q32C，未出现 PSRAM; 图 2f5b17c1e346 / 第 1 页 / USB-UART 页 U3 标注 CP2104）
- `rf.antenna_matching`：L1、C1 和 C9 的元件值均标为 TBD，并注明取决于实际阻抗匹配结果。（证据：图 d81402da2106 / 第 1 页 / A2 Depend on Actual Impedance Matching Result 注记及 L1/C1/C9 TBD）
- `review.v27_schematic_scope`：能否提供 Fire v2.7 当前主板及 M5GO Bottom 的正式原理图/网表，以确认 16 MB Flash、8 MB PSRAM、CH9102F、MPU6886、RGB LED、麦克风和 Grove 5.1 V 升压的实际连接？；原因：当前资源是 2017 通用 M5 Core 图，早于 2023 年 Fire v2.7，且关键器件与产品版本说明不一致，底座电路也未包含。
- `review.antenna_matching_values`：量产版本中 ESP_LNA 至 ANT1 的 L1、C1、C9 实际装配值和 DNP 状态分别是什么？；原因：原理图把三处元件值均标为 TBD，并明确要求依据实际阻抗匹配结果确定。

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

源文档：`zh_CN/core/fire_v2.7.md`

源文档 SHA-256：`2a0f08ab2f717601fe54d49c7072197b4cc5930d41138753130330be03afb142`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
