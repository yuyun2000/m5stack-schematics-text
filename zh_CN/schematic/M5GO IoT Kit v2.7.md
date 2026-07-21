# M5GO IoT Kit v2.7 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5GO IoT Kit v2.7 |
| SKU | K006-V27 |
| 产品 ID | `m5go-iot-kit-v2-7-566311c71a9f` |
| 源文档 | `zh_CN/core/m5go_v2.7.md` |

## 概述

M5GO IoT Kit v2.7 的专属 Bottom 图包含 10 颗 SK6812、SPQ2410/MAX4466 麦克风、TP4057 充电、红外发射、三组扩展插座和 M5-Bus 连接；配套六页 M5 Stack Core Rev A 2017 附图包含 ESP32-D0WDQ6、EA3036、IP5306、LCD、microSD、M5-Bus 和 NS4148 音频。旧 Core 图中的 GD25Q32C、CP2104 与 USB_Micro 和 v2.7 源文档的 16MB Flash、CH9102F 与 Type-C 存在版本冲突，均列为待确认。

## 检索关键词

`M5GO IoT Kit v2.7`、`K006-V27`、`K006-V27-A014`、`M5GO Bottom`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`SK6812 x10`、`SPQ2410`、`MAX4466`、`TP4057`、`AO3400A_N`、`EA3036`、`IP5306`、`0x75`、`GD25Q32C`、`16MB Flash`、`CP2104`、`CH9102F`、`USB Type-C`、`USB_Micro`、`M5-LCD`、`ILI9342C`、`MicroSD-SPI`、`M5-Bus`、`NS4148`、`MPU6886`、`0x68`、`GPIO15 SK6812`、`GPIO34 microphone`、`GPIO13 IR_S`、`I2C_SDA`、`I2C_SCL`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED10 [Bottom] | SK6812 | v2.7 Bottom 串联 RGB LED 灯带 | 图 257641dd1a48 / 第 1 页 / A1-A4 RGB LED * 10 区域 LED1-LED10 SK6812 串联链 |
| U1 [Bottom] | SPQ2410 | v2.7 Bottom 模拟麦克风 | 图 257641dd1a48 / 第 1 页 / B1-C2 Microphone & AP 区域 U1 SPQ2410 |
| U2 [Bottom] | MAX4466 | v2.7 Bottom 麦克风前置放大器，输出 GPIO34 | 图 257641dd1a48 / 第 1 页 / B1-C3 Microphone & AP 区域 U2 max4466 与 GPIO34 |
| U3 [Bottom] | TP4057 | v2.7 Bottom 单节电池线性充电器 | 图 257641dd1a48 / 第 1 页 / C1-D2 Power 区域 U3 TP4057、VIN 与 BAT+ |
| LED11/Q1 [Bottom] | IR12-21C/AO3400A_N | v2.7 Bottom 由 IR_S 控制的红外发射支路 | 图 257641dd1a48 / 第 1 页 / C2-D3 LED11 IR12-21C、R10 与 Q1 AO3400A_N |
| J1/J2/J3 [Bottom] | UART_Socket_4P/GPIO_Socket_4P/SOCKET_POWER_4P | v2.7 Bottom UART、GPIO 与 I2C 扩展插座 | 图 257641dd1a48 / 第 1 页 / A4-C4 Socket 区域 J1/J2/J3 四针插座 |
| J4 [Bottom] | M5Stack_BUS | v2.7 Bottom 至 Core 的 30 针总线连接器 | 图 257641dd1a48 / 第 1 页 / C3-D4 M5Bus 区域 J4 M5Stack_BUS |
| U1 [2017 Core] | ESP32-D0WDQ6 | 2017 共用 Core 附图主控 SoC | 图 d81402da2106 / 第 1 页 / A1-C2 ESP32 区域 U1 ESP32-D0WDQ6 |
| U2 [2017 Core] | GD25Q32C | 2017 共用 Core 附图外部 SPI Flash，不直接代表 v2.7 的 16MB 器件 | 图 d81402da2106 / 第 1 页 / B2 U2 GD25Q32C 与 SD_CMD/SD_CLK/SD_DATA0-3 |
| U4 [2017 Core] | EA3036 | 2017 共用 Core 附图三路同步降压转换器 | 图 91b865957940 / 第 1 页 / A1-B2 Speaker/Power 区域 U4 EA3036 与三路电感输出 |
| U10 [2017 Core] | IP5306 | 2017 共用 Core 附图 USB、电池与 5V 电源管理器 | 图 91b865957940 / 第 1 页 / C1-D2 Power 区域 U10 IP5306 与 0x75 注记 |
| U3 [2017 Core] | CP2104 | 2017 共用 Core 附图 USB-UART，不直接代表 v2.7 的 CH9102F | 图 2f5b17c1e346 / 第 1 页 / A2-C3 U3 CP2104、USB_DP/DN 与 TXD/RXD |
| U5 [2017 Core] | USB_Micro | 2017 共用 Core 附图 USB 连接器符号，不直接代表 v2.7 Type-C 实装 | 图 2f5b17c1e346 / 第 1 页 / A3-A4 Type-C USB 标题区 U5 USB_Micro 符号 |
| U6 [2017 Core] | M5-LCD | 2017 共用 Core 附图 SPI LCD 接口 | 图 2f5b17c1e346 / 第 1 页 / B3-C4 LCD 区域 U6 M5-LCD 与 GPIO 网络 |
| U8 [2017 Core] | MicroSD-SPI | 2017 共用 Core 附图 microSD 卡座 | 图 2f5b17c1e346 / 第 1 页 / C1-D2 TF Card 区域 U8 MicroSD-SPI |
| P1 [2017 Core] | Header 15X2 | 2017 共用 Core 附图 30 针 M5-Bus | 图 72aa5b4d2f89 / 第 1 页 / A1-B1 P1 Header 15X2 与 30 针定义 |
| U9 [2017 Core] | NS4148 | 2017 共用 Core 附图 GPIO25 输入差分 D 类功放 | 图 8d7498c3a5a7 / 第 1 页 / A1-B2 U9 NS4148 与 AUDIO_OUT_P/N |

## 系统结构

### v2.7 资源组成

本产品资源由一页 K006-V27-A014 M5GO Bottom 图和六页 M5 Stack Core 附图组成；六页 Core 封面标题栏标 Revision A、Date 2017/12/6，修订表标 A13 OFFICIAL RELEASE VERSION、10/11/2017。

- 参数与网络：`bottom_resource=K006-V27-A014_Sch_M5GO_page_01`；`core_revision=Revision A`；`core_title_date=2017/12/6`；`core_release_record=A13 10/11/2017`
- 证据：图 257641dd1a48 / 第 1 页 / A1-D4 v2.7 Bottom 完整页，URL/资源名含 K006-V27-A014; 图 a44d9e10f49e / 第 1 页 / A1-D4 M5 STACK CORE 封面、修订记录与标题栏

### 2017 共用 Core 附图分区

六页封面目录依次列出 COVER PAGE、POWER MANAGEMENT、ESP32 SUBSYSTEM、USB-UART & ACCESSORY、M.BUS DEFINITION 和 AUDIO AMPLIFIER。

- 参数与网络：`pages=1:COVER PAGE,2:POWER MANAGEMENT,3:ESP32 SUBSYSTEM,4:USB-UART & ACCESSORY,5:M.BUS DEFINITION,6:AUDIO AMPLIFIER`
- 证据：图 a44d9e10f49e / 第 1 页 / B3-C4 SCHEMATIC PAGE 目录表

## 核心器件

### 2017 共用 Core 图主控

2017 Core 附图 U1 标为 ESP32-D0WDQ6，CHIP_PU 接 EN，射频端接 ESP_LNA，外部 Flash 总线为 SD_CMD、SD_CLK 与 SD_DATA0-3。

- 参数与网络：`reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0-3`；`scope=2017 shared Core drawing`
- 证据：图 d81402da2106 / 第 1 页 / A1-C2 U1 ESP32-D0WDQ6 全部主控网络

## 电源

### Bottom TP4057 充电电路

U3 TP4057 的 VCC 接 VIN、BAT 输出 BAT+，PROG 经 R12 2 kΩ 接地；CHRG/STDBY 通过 D1 1615RG 与 R11 1 kΩ 提供充电状态指示。

- 参数与网络：`charger=U3 TP4057`；`input=VIN`；`battery_node=BAT+`；`program_resistor=R12 2k`；`status_led=D1 1615RG via R11 1k`
- 证据：图 257641dd1a48 / 第 1 页 / C1-D2 Power 区域 U3 TP4057、D1、R11/R12 与 BAT+

### 2017 共用 Core 图 EA3036 三路电源

U4 EA3036 以 VCC_5V 供电，SW1/SW2/SW3 经 L2/L3/L5 输出 VCC_3V3、VDD_3V3、AMP_PWR，三路反馈分压均为 510 kΩ/110 kΩ。

- 参数与网络：`converter=U4 EA3036`；`input=VCC_5V`；`outputs=SW1:VCC_3V3,SW2:VDD_3V3,SW3:AMP_PWR`；`feedback=510k/110k each`；`scope=2017 shared Core drawing`
- 证据：图 91b865957940 / 第 1 页 / A1-B2 U4 EA3036、L2/L3/L5 与三组反馈分压

### 2017 共用 Core 图功放关闭测试点

EA3036 EN3 由 R23 10 kΩ 上拉至 VCC_5V，T1 为接地 0 Ω 测试断点，图面标注 Test Break for Disabling Audio Amplifer。

- 参数与网络：`enable=EN3`；`pullup=R23 10k to VCC_5V`；`test_link=T1 0R to GND`；`scope=2017 shared Core drawing`
- 证据：图 91b865957940 / 第 1 页 / A1 EA3036 EN3、R23/T1 与关闭功放注记

### 2017 共用 Core 图 IP5306

U10 IP5306 的 VIN 接 VIN_USB、VOUT 接 VCC_5V、SW/BAT 接 VBAT、KEY 接 PWR_KEY，图面注记为 5V 2.4A Sync Boost 与 2.1A Sync Buck Charger。

- 参数与网络：`reference=U10`；`part_number=IP5306`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`scope=2017 shared Core drawing`
- 证据：图 91b865957940 / 第 1 页 / C1-D2 U10 IP5306、VIN_USB/VCC_5V/VBAT/PWR_KEY 与功能注记

## 接口

### Bottom 三组四针插座

J1 的 1-4 脚为 U2_RXD、U2_TXD、+5V、GND；J2 为 GPIO36、GPIO26、+5V、GND；J3 为 GND、+5V、I2C_SDA、I2C_SCL，I2C_SDA/SCL 分别由 R3/R4 4.7 kΩ 上拉至 +3.3V。

- 参数与网络：`j1=1:U2_RXD,2:U2_TXD,3:+5V,4:GND`；`j2=1:GPIO36,2:GPIO26,3:+5V,4:GND`；`j3=1:GND,2:+5V,3:I2C_SDA,4:I2C_SCL`；`i2c_pullups=R3=4.7k,R4=4.7k to +3.3V`
- 证据：图 257641dd1a48 / 第 1 页 / A3-C4 Socket 区域 J1/J2/J3 与 R3/R4

### Bottom 有效 M5-Bus 连接

J4 明确连接 GND、GPIO35、GPIO36、EN、GPIO26、+3.3V、U2_RXD、U2_TXD、I2C_SDA、I2C_SCL、IR_S、SK6812、GPIO34、+5V 与 BAT+；其余画有红色未连接标记的脚位未接入 Bottom 电路。

- 参数与网络：`connected_pins=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,10:GPIO26,12:+3.3V,15:U2_RXD,16:U2_TXD,17:I2C_SDA,18:I2C_SCL,22:IR_S,23:SK6812,26:GPIO34,28:+5V,30:BAT+`
- 证据：图 257641dd1a48 / 第 1 页 / C3-D4 M5Bus 区域 J4 外部网络与红色未连接标记

### 2017 共用 Core 图 USB 电路

图面 Type-C USB 分区内的 U5 器件值为 USB_Micro，VCC 经 FUSE1 2 A 接 VIN_USB，D-/D+ 经 R9/R11 两只 22 Ω 接 USB_DN/USB_DP，并由 D1/D2 RLSD52A031V 保护；USB_CC_1/2 各通过 5.10 kΩ 接地。

- 参数与网络：`section_title=Type-C USB`；`connector_value=USB_Micro`；`power=FUSE1 2A to VIN_USB`；`data=D- via R9 22R,D+ via R11 22R`；`esd=D1,D2 RLSD52A031V`；`cc_pulldowns=USB_CC_1=5.10k,USB_CC_2=5.10k`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / A3-B4 Type-C USB 区域 U5 USB_Micro、FUSE1、R9/R11、D1/D2 与 CC 电阻

### 2017 共用 Core 图 LCD

U6 M5-LCD 的 #RST、R/S、MOSI、SCK、CS 分别接 GPIO33、GPIO27、GPIO23、GPIO18、GPIO14；背光由 GPIO32 控制 FET1 AO3402。

- 参数与网络：`interface=M5-LCD`；`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`chip_select=GPIO14`；`backlight=GPIO32 via FET1 AO3402`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / B3-C4 LCD 区域 U6、FET1 与 GPIO14/18/23/27/32/33

## 总线

### 2017 共用 Core 图 30 针 M5-Bus

P1 的 1-30 脚依次为 GND、GPIO35、GND、GPIO36、GND、EN、GPIO23、GPIO25、GPIO19、GPIO26、EXT_SCK、VDD_3V3、GPIO3、GPIO1、GPIO16、GPIO17、GPIO21、GPIO22、GPIO2、GPIO5、GPIO12、GPIO13、GPIO15、GPIO0、HPWR、GPIO34、HPWR、VCC_5V、HPWR、VBAT。

- 参数与网络：`pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:EXT_SCK,12:VDD_3V3,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:VCC_5V,29:HPWR,30:VBAT`；`scope=2017 shared Core drawing`
- 证据：图 72aa5b4d2f89 / 第 1 页 / A1-B3 P1 Header 15X2 与右侧 M5-Bus 功能表

## 总线地址

### IP5306 I2C 地址

2017 Core 附图注释明确说明该定制 IP5306 通过 IIC 与 ESP32 通信，IIC 地址为 0x75。

- 参数与网络：`part_number=IP5306`；`i2c_address=0x75`；`scope=2017 shared Core drawing`
- 证据：图 91b865957940 / 第 1 页 / C1-D2 U10 下方 customized IP5306 IIC address is 0x75 注记

## GPIO 与控制信号

### Bottom 十颗 SK6812

LED1 至 LED10 均为 SK6812，DOUT 逐级连接下一颗 DIN，首颗输入网络为 SK6812，供电为 +5V，LED10 DOUT 末端未连接。

- 参数与网络：`references=LED1-LED10`；`part_number=SK6812`；`count=10`；`data_input=SK6812`；`supply=+5V`；`last_output=NC`
- 证据：图 257641dd1a48 / 第 1 页 / A1-A4 RGB LED * 10 区域完整 LED1-LED10 数据链

### 2017 共用 Core 图按键

S3/S2/S1 按下分别将 GPIO39/GPIO38/GPIO37 接地，对应 Btn A/Btn B/Btn C；S4 按下将 PWR 接地，各节点带上拉和钳位或 RC 元件。

- 参数与网络：`button_a=S3 GPIO39`；`button_b=S2 GPIO38`；`button_c=S1 GPIO37`；`power=S4 PWR`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / A1-B1 Button 区域 S1-S4、GPIO37/38/39 与 PWR

## 时钟

### 2017 共用 Core 图主晶振

X1 标注 40 MHz、±10 ppm、22 pF，连接 ESP_XTAL_N/P，C21/C22 各 22 pF 接地。

- 参数与网络：`reference=X1`；`frequency_hz=40000000`；`tolerance_ppm=10`；`load_capacitance_pf=22`；`capacitors=C21=22pF,C22=22pF`；`scope=2017 shared Core drawing`
- 证据：图 d81402da2106 / 第 1 页 / C1-D2 X1、C21/C22 与 ESP_XTAL_N/P

## 保护电路

### 2017 共用 Core 图 M5-Bus 信号保护

P1 多路 GPIO、EN 与 EXT_SCK 通过 RLSD52A031V 阵列钳位至 GND，EXT_SCK 经 R2 22 Ω 连接 GPIO18。

- 参数与网络：`protection=RLSD52A031V diode array to GND`；`clock_series=EXT_SCK to GPIO18 via R2 22R`；`scope=2017 shared Core drawing`
- 证据：图 72aa5b4d2f89 / 第 1 页 / B1-D1 R2 与 D2-D23 RLSD52A031V 阵列

## 存储

### 2017 共用 Core 图 Flash

2017 Core 附图 U2 标为 GD25Q32C，nCS/CLK/DI/DO/nWP/nHOLD 分别连接 SD_CMD、SD_CLK、SD_DATA1、SD_DATA0、SD_DATA3、SD_DATA2。

- 参数与网络：`reference=U2`；`part_number=GD25Q32C`；`chip_select=SD_CMD`；`clock=SD_CLK`；`io=IO0:SD_DATA1,IO1:SD_DATA0,IO2:SD_DATA3,IO3:SD_DATA2`；`scope=2017 shared Core drawing`
- 证据：图 d81402da2106 / 第 1 页 / B2 U2 GD25Q32C 与 SD_CMD/SD_CLK/SD_DATA0-3

### 2017 共用 Core 图 microSD

U8 MicroSD-SPI 的 CS、DI、SCLK、DO 分别接 GPIO4、GPIO23、GPIO18、GPIO19；LCD 与 microSD 共用 GPIO23 MOSI 和 GPIO18 SCK。

- 参数与网络：`chip_select=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`shared_with_lcd=GPIO23,GPIO18`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / C1-D2 TF Card 区域 U8 与 SPI_SDC(S/DI/CLK/DO) 网络

## 音频

### 2017 共用 Core 图 NS4148 功放

U9 NS4148 的 INP 经 C43 100 nF 接 GPIO25，INN 经 C44 100 nF 接 PGND，VCC/CTRL 接 AMP_PWR，VOP/VON 经 FB1/FB2 形成 AUDIO_OUT_P/N。

- 参数与网络：`reference=U9`；`part_number=NS4148`；`input=GPIO25 via C43 100nF`；`power_enable=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`scope=2017 shared Core drawing`
- 证据：图 8d7498c3a5a7 / 第 1 页 / A1-B2 U9 NS4148、C43/C44、AMP_PWR 与 AUDIO_OUT_P/N

## 射频

### 2017 共用 Core 图天线匹配

ESP_LNA 经 L1/C1/C9 匹配位连接 ANT1，L1、C1、C9 的元件值均标 TBD。

- 参数与网络：`input=ESP_LNA`；`antenna=ANT1`；`matching=L1 TBD,C1 TBD,C9 TBD`；`scope=2017 shared Core drawing`
- 证据：图 d81402da2106 / 第 1 页 / A2 ESP_LNA、L1/C1/C9 与 ANT1

## 调试与烧录

### Bottom 红外发射

+5V 经 LED11 IR12-21C 和 R10 49.9 Ω 接 Q1 AO3400A_N 漏极，Q1 栅极由 IR_S 经 R13 1 kΩ 驱动，并由 R14 10 kΩ 下拉。

- 参数与网络：`emitter=LED11 IR12-21C`；`switch=Q1 AO3400A_N`；`control=IR_S via R13 1k`；`pulldown=R14 10k`；`series_resistor=R10 49.9R`
- 证据：图 257641dd1a48 / 第 1 页 / C2-D3 LED11、R10、Q1、R13/R14 与 IR_S

### 2017 共用 Core 图 CP2104

U3 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD 经 R8 470 Ω 接 GPIO3，RXD 接 GPIO1，RTS/DTR 引至自动下载电路。

- 参数与网络：`reference=U3`；`part_number=CP2104`；`usb=USB_DP,USB_DN`；`txd=GPIO3 via R8 470R`；`rxd=GPIO1`；`handshake=RTS,DTR`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / A2-C3 U3 CP2104 全部 USB、UART 与握手信号

### 2017 共用 Core 图自动下载

DTR/RTS 通过 R16/R19 两只 12 kΩ 驱动两只 NPN-S8050，交叉控制 EN 与 GPIO0。

- 参数与网络：`inputs=DTR,RTS`；`resistors=R16=12k,R19=12k`；`transistors=2 x NPN-S8050`；`outputs=EN,GPIO0`；`scope=2017 shared Core drawing`
- 证据：图 2f5b17c1e346 / 第 1 页 / C2-D3 Auto-Download 区域 DTR/RTS、R16/R19 与两只 NPN-S8050

## 模拟电路

### Bottom 麦克风与前置放大

U1 SPQ2410 的 OUT 经 C6 10 nF 交流耦合到 U2 MAX4466，R2/R5 各 1 MΩ 建立输入偏置，U2 OUT 输出 GPIO34，R7 100 kΩ、R9 1 kΩ 与 C8 100 pF 构成反馈网络。

- 参数与网络：`microphone=U1 SPQ2410`；`amplifier=U2 MAX4466`；`coupling=C6 10nF`；`output=GPIO34`；`bias=R2=1M,R5=1M`；`feedback=R7=100k,R9=1k,C8=100pF`
- 证据：图 257641dd1a48 / 第 1 页 / B1-C3 Microphone & AP 区域 U1/U2、C6、偏置与反馈网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | v2.7 资源组成 | `bottom_resource=K006-V27-A014_Sch_M5GO_page_01`；`core_revision=Revision A`；`core_title_date=2017/12/6`；`core_release_record=A13 10/11/2017` |
| GPIO 与控制信号 | Bottom 十颗 SK6812 | `references=LED1-LED10`；`part_number=SK6812`；`count=10`；`data_input=SK6812`；`supply=+5V`；`last_output=NC` |
| 模拟电路 | Bottom 麦克风与前置放大 | `microphone=U1 SPQ2410`；`amplifier=U2 MAX4466`；`coupling=C6 10nF`；`output=GPIO34`；`bias=R2=1M,R5=1M`；`feedback=R7=100k,R9=1k,C8=100pF` |
| 电源 | Bottom TP4057 充电电路 | `charger=U3 TP4057`；`input=VIN`；`battery_node=BAT+`；`program_resistor=R12 2k`；`status_led=D1 1615RG via R11 1k` |
| 接口 | Bottom 三组四针插座 | `j1=1:U2_RXD,2:U2_TXD,3:+5V,4:GND`；`j2=1:GPIO36,2:GPIO26,3:+5V,4:GND`；`j3=1:GND,2:+5V,3:I2C_SDA,4:I2C_SCL`；`i2c_pullups=R3=4.7k,R4=4.7k to +3.3V` |
| 接口 | Bottom 有效 M5-Bus 连接 | `connected_pins=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,10:GPIO26,12:+3.3V,15:U2_RXD,16:U2_TXD,17:I2C_SDA,18:I2C_SCL,22:IR_S,23:SK6812,26:GPIO34,28:+5V,30:BAT+` |
| 调试与烧录 | Bottom 红外发射 | `emitter=LED11 IR12-21C`；`switch=Q1 AO3400A_N`；`control=IR_S via R13 1k`；`pulldown=R14 10k`；`series_resistor=R10 49.9R` |
| 系统结构 | 2017 共用 Core 附图分区 | `pages=1:COVER PAGE,2:POWER MANAGEMENT,3:ESP32 SUBSYSTEM,4:USB-UART & ACCESSORY,5:M.BUS DEFINITION,6:AUDIO AMPLIFIER` |
| 核心器件 | 2017 共用 Core 图主控 | `reference=U1`；`part_number=ESP32-D0WDQ6`；`enable=EN`；`rf=ESP_LNA`；`flash_bus=SD_CMD,SD_CLK,SD_DATA0-3`；`scope=2017 shared Core drawing` |
| 存储 | 2017 共用 Core 图 Flash | `reference=U2`；`part_number=GD25Q32C`；`chip_select=SD_CMD`；`clock=SD_CLK`；`io=IO0:SD_DATA1,IO1:SD_DATA0,IO2:SD_DATA3,IO3:SD_DATA2`；`scope=2017 shared Core drawing` |
| 时钟 | 2017 共用 Core 图主晶振 | `reference=X1`；`frequency_hz=40000000`；`tolerance_ppm=10`；`load_capacitance_pf=22`；`capacitors=C21=22pF,C22=22pF`；`scope=2017 shared Core drawing` |
| 射频 | 2017 共用 Core 图天线匹配 | `input=ESP_LNA`；`antenna=ANT1`；`matching=L1 TBD,C1 TBD,C9 TBD`；`scope=2017 shared Core drawing` |
| 电源 | 2017 共用 Core 图 EA3036 三路电源 | `converter=U4 EA3036`；`input=VCC_5V`；`outputs=SW1:VCC_3V3,SW2:VDD_3V3,SW3:AMP_PWR`；`feedback=510k/110k each`；`scope=2017 shared Core drawing` |
| 电源 | 2017 共用 Core 图功放关闭测试点 | `enable=EN3`；`pullup=R23 10k to VCC_5V`；`test_link=T1 0R to GND`；`scope=2017 shared Core drawing` |
| 电源 | 2017 共用 Core 图 IP5306 | `reference=U10`；`part_number=IP5306`；`input=VIN_USB`；`output=VCC_5V`；`battery=VBAT`；`key=PWR_KEY`；`scope=2017 shared Core drawing` |
| 总线地址 | IP5306 I2C 地址 | `part_number=IP5306`；`i2c_address=0x75`；`scope=2017 shared Core drawing` |
| 接口 | 2017 共用 Core 图 USB 电路 | `section_title=Type-C USB`；`connector_value=USB_Micro`；`power=FUSE1 2A to VIN_USB`；`data=D- via R9 22R,D+ via R11 22R`；`esd=D1,D2 RLSD52A031V`；`cc_pulldowns=USB_CC_1=5.10k,USB_CC_2=5.10k`；`scope=2017 shared Core drawing` |
| 调试与烧录 | 2017 共用 Core 图 CP2104 | `reference=U3`；`part_number=CP2104`；`usb=USB_DP,USB_DN`；`txd=GPIO3 via R8 470R`；`rxd=GPIO1`；`handshake=RTS,DTR`；`scope=2017 shared Core drawing` |
| 调试与烧录 | 2017 共用 Core 图自动下载 | `inputs=DTR,RTS`；`resistors=R16=12k,R19=12k`；`transistors=2 x NPN-S8050`；`outputs=EN,GPIO0`；`scope=2017 shared Core drawing` |
| GPIO 与控制信号 | 2017 共用 Core 图按键 | `button_a=S3 GPIO39`；`button_b=S2 GPIO38`；`button_c=S1 GPIO37`；`power=S4 PWR`；`scope=2017 shared Core drawing` |
| 接口 | 2017 共用 Core 图 LCD | `interface=M5-LCD`；`reset=GPIO33`；`data_command=GPIO27`；`mosi=GPIO23`；`clock=GPIO18`；`chip_select=GPIO14`；`backlight=GPIO32 via FET1 AO3402`；`scope=2017 shared Core drawing` |
| 存储 | 2017 共用 Core 图 microSD | `chip_select=GPIO4`；`mosi=GPIO23`；`clock=GPIO18`；`miso=GPIO19`；`shared_with_lcd=GPIO23,GPIO18`；`scope=2017 shared Core drawing` |
| 总线 | 2017 共用 Core 图 30 针 M5-Bus | `pinout=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:EXT_SCK,12:VDD_3V3,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:VCC_5V,29:HPWR,30:VBAT`；`scope=2017 shared Core drawing` |
| 保护电路 | 2017 共用 Core 图 M5-Bus 信号保护 | `protection=RLSD52A031V diode array to GND`；`clock_series=EXT_SCK to GPIO18 via R2 22R`；`scope=2017 shared Core drawing` |
| 音频 | 2017 共用 Core 图 NS4148 功放 | `reference=U9`；`part_number=NS4148`；`input=GPIO25 via C43 100nF`；`power_enable=AMP_PWR`；`outputs=AUDIO_OUT_P,AUDIO_OUT_N`；`scope=2017 shared Core drawing` |
| 系统结构 | 2017 Core 附图与 v2.7 的版本关系 | `target=M5GO IoT Kit v2.7 K006-V27`；`attached_core_revision=Revision A 2017`；`impact=exact v2.7 Core BOM and connector revision not established` |
| 核心器件 | v2.7 主控具体版本 | `source_document=ESP32-D0WDQ6-V3`；`attached_core_drawing=ESP32-D0WDQ6`；`difference=V3 suffix` |
| 存储 | v2.7 16MB Flash | `source_document_capacity=16MB`；`attached_core_part=GD25Q32C`；`drawing_bus=SD_CMD,SD_CLK,SD_DATA0-3` |
| 调试与烧录 | v2.7 USB-UART | `source_document=CH9102F`；`attached_core_drawing=CP2104`；`drawing_handshake=RTS,DTR to EN,GPIO0` |
| 接口 | v2.7 USB Type-C 接口 | `source_document=USB Type-C`；`drawing_section=Type-C USB`；`drawing_connector_value=USB_Micro`；`drawing_cc=USB_CC_1/2 5.10k pulldowns not connected to U5 symbol` |
| 核心器件 | v2.7 LCD 控制器 | `source_document=ILI9342C 320x240 IPS`；`attached_core_drawing=U6 M5-LCD`；`drawing_spi=GPIO14,GPIO18,GPIO23,GPIO27,GPIO33` |
| 传感器 | v2.7 MPU6886 | `source_document_imu=MPU6886 0x68`；`source_document_magnetometer=BMM150 removed since v2.6`；`schematic_coverage=no sensor page in seven local assets` |
| 电源 | v2.7 500mAh 电池 | `source_document=3.7V 500mAh`；`bottom_drawing=TP4057 to BAT+`；`core_drawing=IP5306 to VBAT` |
| 音频 | v2.7 扬声器规格 | `source_document=1W-0928`；`attached_core_amplifier=NS4148`；`drawing_output=AUDIO_OUT_P,AUDIO_OUT_N` |
| 电源 | v2.7 Grove 5.1V 升压 | `source_document=Grove boost, stable 5.1V output`；`bottom_socket_rail=+5V`；`drawing_boost_component=not shown` |
| 存储 | v2.7 microSD 最大容量 | `source_document_limit=16GB`；`drawing_interface=MicroSD-SPI`；`drawing_capacity_limit=not specified` |

## 待确认事项

- `system.v27-core-revision-scope`：配套 Core 六页图的标题栏和修订记录均为 2017 Rev A，而目标产品是 M5GO IoT Kit v2.7；这些页可确认图面连接，但无法单独确认其中器件型号和连接器均沿用到 v2.7。（证据：图 a44d9e10f49e / 第 1 页 / A1-D4 六页 Core 封面 Revision A、2017 日期与 A13 修订记录）
- `component.v27-soc`：v2.7 源文档标注 ESP32-D0WDQ6-V3，而 2017 Core 附图 U1 标为 ESP32-D0WDQ6；需要当前 v2.7 BOM 或 PCB 丝印确认是否为 V3。（证据：图 d81402da2106 / 第 1 页 / A1-C2 2017 Core 附图 U1 标注 ESP32-D0WDQ6）
- `storage.v27-flash`：v2.7 源文档标注 16MB Flash，2017 Core 附图却绘制 U2 GD25Q32C；当前 16MB Flash 的具体型号和是否保持 SD_CMD/SD_CLK/SD_DATA0-3 连接需确认。（证据：图 d81402da2106 / 第 1 页 / B2 2017 Core 附图 U2 GD25Q32C 与外部 Flash 总线）
- `debug.v27-usb-uart`：v2.7 源文档规格表标注 CH9102F，2017 Core 附图只绘制 U3 CP2104；v2.7 实装 USB-UART 型号、自动下载握手连接和外围值需用当前图或 PCB 确认。（证据：图 2f5b17c1e346 / 第 1 页 / A2-C3 2017 Core 附图 U3 CP2104 与自动下载握手网络）
- `interface.v27-usb-connector`：v2.7 源文档明确为 USB Type-C，但 2017 Core 图的分区标题为 Type-C USB、U5 器件值却为 USB_Micro，且 CC1/CC2 下拉没有连入 U5 符号；当前 Type-C 连接器引脚和 C2C 支持电路需确认。（证据：图 2f5b17c1e346 / 第 1 页 / A3-B4 Type-C USB 标题、U5 USB_Micro 符号与独立 CC1/CC2 电阻框）
- `component.v27-display`：v2.7 源文档标注 ILI9342C 320x240 IPS，2017 Core 附图只把接口器件标为 M5-LCD；ILI9342C 的具体模组料号、背光额定值和面板版本未在本地原理图中给出。（证据：图 2f5b17c1e346 / 第 1 页 / B3-C4 2017 Core 附图 U6 仅标 M5-LCD）
- `sensor.v27-imu`：v2.7 源文档标注 MPU6886、I2C 地址 0x68，并记录 v2.6 已取消 BMM150；七页本地资源没有 MPU6886 或 BMM150 电路页，当前 IMU 供电、总线和地址选择连接需确认。（证据：图 a44d9e10f49e / 第 1 页 / B3-C4 六页 Core 目录未列出传感器或 IMU 页面; 图 257641dd1a48 / 第 1 页 / A1-D4 v2.7 Bottom 页仅含 LED、麦克风、充电、插座、红外和 M5-Bus）
- `power.v27-battery`：v2.7 源文档标注 3.7V 500mAh，Bottom 图只显示 TP4057 与 BAT+，2017 Core 图只显示 IP5306/VBAT；电芯料号、保护电路和容量未在本地原理图中标出。（证据：图 257641dd1a48 / 第 1 页 / C1-D2 Bottom U3 TP4057 与 BAT+，无电芯容量或料号; 图 91b865957940 / 第 1 页 / C1-D2 2017 Core U10 IP5306 与 VBAT，未标电芯容量）
- `audio.v27-speaker`：v2.7 源文档标注 1W-0928 扬声器，2017 Core 附图只给出 NS4148 与 AUDIO_OUT_P/N，没有扬声器器件、阻抗和额定条件；当前扬声器料号与负载参数需确认。（证据：图 8d7498c3a5a7 / 第 1 页 / A1-B2 NS4148 输出停在 AUDIO_OUT_P/N，未绘制扬声器器件）
- `power.v27-grove-boost`：v2.7 版本变更说明称 Grove 口增加升压并稳定输出 5.1V，但 Bottom 图的 J1/J2/J3 只标 +5V，未显示独立升压器件或 5.1V 网络；该升级电路的位置、器件和使能方式需确认。（证据：图 257641dd1a48 / 第 1 页 / A3-C4 Bottom J1/J2/J3 均标 +5V，页面无独立 5.1V 升压器件）
- `storage.v27-microsd-limit`：v2.7 源文档称 microSD 最大支持 16GB，2017 Core 附图只显示 SPI 卡座与信号，没有容量、介质类型或文件系统限制；16GB 上限来源需确认。（证据：图 2f5b17c1e346 / 第 1 页 / C1-D2 U8 MicroSD-SPI 只标 SPI 网络，未标容量限制）
- `review.v27-core-revision-scope`：2017 Revision A 的 M5 Stack Core 六页附图中，哪些器件和连接仍适用于 K006-V27 当前主机？；原因：目标为 v2.7，但附图标题栏早于 v2.6/v2.7 版本变更，且已出现 Flash、USB-UART 和连接器冲突。
- `review.v27-soc`：K006-V27 实装主控是否确认为 ESP32-D0WDQ6-V3？；原因：源文档带 V3 后缀，2017 Core 附图只标 ESP32-D0WDQ6。
- `review.v27-flash`：K006-V27 的 16MB Flash 具体型号和总线连接是什么？；原因：源文档标 16MB，2017 Core 附图绘制 GD25Q32C，容量和版本不一致。
- `review.v27-usb-uart`：K006-V27 的 CH9102F 原理图、自动下载连接和外围参数是什么？；原因：v2.7 源文档标 CH9102F，附带 2017 Core 图只有 CP2104。
- `review.v27-usb-connector`：K006-V27 Type-C 连接器的 CC1/CC2、VBUS 和数据引脚实际连接是什么？；原因：2017 Core 图分区标题写 Type-C USB，但 U5 值为 USB_Micro，CC 下拉也未接入 U5 符号。
- `review.v27-display`：K006-V27 的 ILI9342C 模组料号、背光参数和玻璃屏版本是什么？；原因：2017 Core 附图只标 M5-LCD，没有控制器和面板料号。
- `review.v27-imu`：K006-V27 的 MPU6886 供电、I2C 连接和地址选择电路在哪里？；原因：源文档标 MPU6886 0x68，但七页本地资源没有传感器电路。
- `review.v27-battery`：K006-V27 的 3.7V 500mAh 电芯料号、保护电路和充电参数是什么？；原因：本地原理图只显示 TP4057、IP5306 和 BAT+/VBAT 网络，未标电芯参数。
- `review.v27-speaker`：K006-V27 的 1W-0928 扬声器料号、阻抗和 NS4148 负载条件是什么？；原因：附图只到 AUDIO_OUT_P/N，没有扬声器器件或负载规格。
- `review.v27-grove-boost`：v2.7 新增的 Grove 5.1V 升压器件、网络和使能方式是什么？；原因：版本说明称新增升压，但 Bottom 图只标 +5V 插座电源，未显示 5.1V 升压电路。
- `review.v27-microsd-limit`：K006-V27 的 16GB microSD 上限来自硬件、固件还是文件系统？；原因：原理图只给出 SPI 卡座和信号，没有容量或介质限制。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `257641dd1a48c91b73085574de27e2e06ebfcde06599fa0ed865fe3c733da01e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/661/K006-V27-A014_Sch_M5GO_page_01.png` |
| 2 | 1 | `a44d9e10f49eba739a7d1b57e10ddb75ee06740af6339dda71801119e0ff3e95` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_01.png` |
| 3 | 1 | `91b865957940b7595eb4abcbb1d34ab61b82753b0035267d860ef1a3cfd453bb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_02.png` |
| 4 | 1 | `d81402da2106664255e50b82ad9e519d7f0f6b1844ddefc24b5aecc28a7ccdbf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_03.png` |
| 5 | 1 | `2f5b17c1e346f2498049eb882140037528b100afbf6854879dbc91605c44a0f6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_04.png` |
| 6 | 1 | `72aa5b4d2f89ab1e81f41d1b5916bfa3b7a527a19c21ca6ee946c882f6d8ce5c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_05.png` |
| 7 | 1 | `8d7498c3a5a7fd1010952eda7a2742715f09a8abc789055f9d1e77f7900af32f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_06.png` |

---

源文档：`zh_CN/core/m5go_v2.7.md`

源文档 SHA-256：`0fd57a6a6ec23035e1237944c93ac1d8ab7b9e11601b50d2a6c391a5c0b6f5a5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
