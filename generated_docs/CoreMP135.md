# CoreMP135 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CoreMP135 |
| SKU | K135 |
| 产品 ID | `coremp135-98360de80ed5` |
| 源文档 | `zh_CN/core/M5CoreMP135.md` |

## 概述

CoreMP135 的 12 页主板与 4 页 MidLayer 原理图组成一套 STM32MP135DAE7 Linux 控制系统。主板集成 DDR3L、AXP2101 电源管理、RTL8188FTV Wi-Fi、双 RTL8211F-CG 以太网 PHY、GL852G USB Hub、LT8618SXB 视频桥、BM8563 RTC、microSD 和 LCD/触摸连接器；MidLayer 提供双 RJ45、双 SIT1051T/3 CAN、MAX3485EIM RS485、Grove、M5-Bus、外部电源转换和 NS4168 扬声器链路。正文中的 DDR 容量、显示/触摸具体型号与参数、音频额定值、输入额定范围及以太网速率未全部直接印在原理图上，且数据手册链接的 STM32MP135DAF7 与图面 STM32MP135DAE7 存在料号冲突。

## 检索关键词

`CoreMP135`、`K135`、`STM32MP135DAE7`、`STM32MP135DAF7`、`DDR3L_DRAM`、`AXP2101`、`RTL8188FTV`、`RTL8211F-CG`、`GL852G`、`LT8618SXB`、`BM8563`、`NS4168`、`MAX3485EIM`、`SIT1051T/3`、`SCT9330`、`SY7088`、`microSD`、`HDMI`、`USB OTG`、`USB Hub`、`GbE`、`CAN FD`、`RS485`、`M5-Bus`、`Grove I2C`、`Grove UART`、`I2C3`、`SAI1`、`SPI1`、`SPI4`、`FDCAN1`、`FDCAN2`、`VDD_3V3`、`VDD_CPU`、`VDD_DDR`、`VDD_1V8`、`VCC_BST_5V`、`BUS_OUT`、`AXP_VBUS`、`MidLayer`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U7A-U7E | STM32MP135DAE7 | 主处理器，连接 DDR3L、双 RGMII、USB、RGB 显示、SD、音频、CAN、UART、I2C、SPI 与调试网络 | 图 17ad800da5d3 / 第 1 页 / source_004 左上 U7E 电源单元，器件标注 STM32MP135DAE7; 图 32529857ea6d / 第 1 页 / source_011 上部 U7A/U7B GPIO 与复用功能单元 |
| U9 | DDR3L_DRAM | 16-bit DDR3L 存储器，连接 STM32MP135 DDR 控制器 | 图 ae9e1037fa30 / 第 1 页 / source_007 右侧 U9 DDR3L_DRAM，DQ0-DQ15、地址、时钟与控制网络 |
| U1 | AXP2101 | PMIC，生成 VDD_3V3、VDD_CPU、VDD_1V8、VDD_DDR、Wi-Fi、LCD 背光、RTC 与 USB HS 电源轨 | 图 aa0621b243a7 / 第 1 页 / source_005 左侧 U1 AXP2101 与 DCDC/ALDO/BLDO/DLDO 输出 |
| U6 | SY7088 | 由 AXP_PS 升压生成 VCC_BST_5V，受 ALDO2_OUT 使能 | 图 aa0621b243a7 / 第 1 页 / source_005 右下 U6 SY7088 与 L6、VCC_BST_5V |
| U8 | BM8563 | RTC，连接 I2C3、晶体 Y1、RTC_VDD、AXP_WAKEUP 与后备电池 BAT1 | 图 406350a698b1 / 第 1 页 / source_006 左下 U8 BM8563、Y1、BAT1 与 I2C3 |
| U10 | MicroSD | 3.3V microSD 卡座，使用 DAT0-DAT3、CMD 与 CLK 六条 SD 信号 | 图 8262f47a5d77 / 第 1 页 / source_008 中部 U10 MicroSD 与 SD_DAT0-DAT3、SD_CMD、SD_CLK |
| U23 | RTL8188FTV | USB Wi-Fi 控制器，连接 40MHz 晶体、RF_OUT 与 IPEX 天线座 | 图 302e2a3a2e24 / 第 1 页 / source_002 左中 U23 RTL8188FTV，DS_USB2_D_N/P、X4 与 RF_OUT |
| J7 | IPEX | RTL8188FTV 的 RF_OUT 射频天线连接器 | 图 302e2a3a2e24 / 第 1 页 / source_002 右侧 J7 IPEX 与 RF_OUT 匹配网络 |
| U12,U13 | RTL8211F-CG | 两颗 RGMII 以太网 PHY，分别连接 ETH1/ETH2 与四对 MDI 差分线 | 图 6450e97913a5 / 第 1 页 / source_009 左右 ETH1/ETH2，U12/U13 RTL8211F-CG |
| U14 | LT8618SXB | 24 路 RGB 与 SAI1 音频到 HDMI TMDS 的视频桥 | 图 284f113b1baf / 第 1 页 / source_010 左侧 U14 LT8618SXB，RGB_D0-D23、SAI1 与 HDMI TMDS |
| J1 [main board] | BOOMELL HDMI-001 | HDMI 输出连接器，承接三组 TMDS、时钟、CEC、DDC、5V 与 HPD | 图 284f113b1baf / 第 1 页 / source_010 右侧 J1 HDMI 连接器 |
| U18 | GL852G | 一上行四下行 USB 2.0 Hub，连接 USB1_D_N/P 与 DS_USB1-D4 | 图 6b81d573e1d5 / 第 1 页 / source_012 左上 U18 GL852G 与 DM0/DP0、DM1-DM4/DP1-DP4 |
| U20,U22 | USB Type-A | GL852G 下行 DS_USB3 与 DS_USB4 的两个外部 USB-A 端口 | 图 6b81d573e1d5 / 第 1 页 / source_012 右侧 U20/U22 USB-A 端口与 VBUS1/VBUS2 |
| J6 [main board] | USB Type-C | USB2_D_P/N OTG 数据与 VUSB 电源连接器，CC1/CC2 各接 5.1K 下拉 | 图 99fed790f48e / 第 1 页 / source_003 中部 J6 USB Type-C、USB2_D_P/N、VUSB 与 CC 电阻 |
| J3 [main board] | Header 16P | LCD/触摸连接器，引出 SPI1、I2C3、TOUCH_INT、VCC_BL、VDD_3V3 与 GND | 图 1651951f9ae7 / 第 1 页 / source_001 左侧 J3 LCD/Touch 16-pin Header |
| J3,J4,J5,U24 [main board] | BTB/40P connectors | 主板到 MidLayer 的双以太网、电源、USB、音频与扩展总线连接器 | 图 99fed790f48e / 第 1 页 / source_003 J4/J5/U24 三组 40-pin 连接器与板间网络 |
| J7A,J7B [MidLayer] | HY911261C | ETH1/ETH2 带磁性器件与 LED 的双 RJ45 网络连接器 | 图 803d75c0f85c / 第 1 页 / source_013 下部 J7A/J7B HY911261C 与 EMDI1/EMDI2 四对差分线 |
| U6,U9 [MidLayer] | SIT1051T/3 | FDCAN1/FDCAN2 收发器，3.3V 逻辑供电、VCC_BST_5V 总线侧供电 | 图 bf87e025097f / 第 1 页 / source_014 左上/左中 U6/U9 SIT1051T/3 |
| U10 [MidLayer] | MAX3485EIM | USART3 到 RS485_P/N 的半双工收发器 | 图 bf87e025097f / 第 1 页 / source_014 左下 U10 MAX3485EIM，USART3_RX/TX/DE 与 RS485_P/N |
| U12 [MidLayer] | SCT9330 | 将 EXT_VIN 降压为 AXP_VBUS 的外部输入转换器 | 图 3f5af84c5eac / 第 1 页 / source_015 中下 U12 SCT9330、L1 与 AXP_VBUS |
| U13 [MidLayer] | NS4168 | SAI1 数字音频到 VON/VOP 差分扬声器输出的功放 | 图 ad2679ae4a5c / 第 1 页 / source_016 上部 U13 NS4168 与 J11 扬声器接口 |
| P1 [MidLayer] | Header 15x2 | M5-Bus，提供电源、USB、I2C1/I2C2、USART2、SPI4、GPIO 与 ADC 网络 | 图 803d75c0f85c / 第 1 页 / source_013 上部 P1 Header 15x2 |
| J3,J4 [MidLayer] | GROVE-4P | I2C5 与 USART6 Grove 扩展端口，信号经过串联磁珠和 PESD3V3 保护 | 图 803d75c0f85c / 第 1 页 / source_013 右上 J3 I2C5 Grove、右中 J4 USART6 Grove |
| J8,J9,J10 [MidLayer] | CON2/GROVE-4P | 两路 CAN 与一组 PWR485 外部端子 | 图 bf87e025097f / 第 1 页 / source_014 右侧 J8 CAN1、J9 CAN2、J10 RS485/BUS_IN |
| U2-U5 [main board] | ME1502AM5G/ME1502CM5G | USB OTG 与 M5-Bus 电源方向控制开关 | 图 aa0621b243a7 / 第 1 页 / source_005 右上 U2-U5，USB_OTG_EN 与 BUS_OUT_EN 控制的四个开关 |

## 系统结构

### CoreMP135 双板系统架构

系统由 12 页主板和 4 页 MidLayer 组成；主板承载 STM32MP135DAE7、DDR3L、PMIC、Wi-Fi、双以太网 PHY、USB Hub、视频桥、RTC、microSD 与 LCD/触摸接口，MidLayer 承载 RJ45、CAN、RS485、Grove、M5-Bus、外部输入电源和音频功放。

- 参数与网络：`main_board_pages=source_001-source_012`；`midlayer_pages=source_013-source_016`；`processor=STM32MP135DAE7`；`interconnect=J3/J4/J5/U24 to J1/J2/U1`
- 证据：图 99fed790f48e / 第 1 页 / source_003 主板连接器总览; 图 803d75c0f85c / 第 1 页 / source_013 MidLayer 接口与连接器总览

## 核心器件

### 主处理器原理图料号

主处理器 U7A-U7E 的电源、系统、DDR 与 GPIO 单元均标注 STM32MP135DAE7。

- 参数与网络：`reference=U7A-U7E`；`part_number=STM32MP135DAE7`；`power_unit=U7E`；`ddr_unit=U7D`；`gpio_units=U7A/U7B`；`system_unit=U7C`
- 证据：图 17ad800da5d3 / 第 1 页 / source_004 U7E 底部 STM32MP135DAE7 标注; 图 32529857ea6d / 第 1 页 / source_011 U7A/U7B 底部 STM32MP135DAE7 标注

## 电源

### AXP2101 主电源轨

U1 AXP2101 的 DCDC1、DCDC2、DCDC3、DCDC4 分别形成 VDD_3V3 3.3V、VDD_CPU 1.25V、VDD_1V8 1.8V、VDD_DDR 1.35V；BLDO1 输出 WIFI_1V2，DLDO1/DC1SW 输出 VCC_BL，ALDO1 输出 VUSB_HS_3V3。

- 参数与网络：`dcdc1=VDD_3V3 3.3V`；`dcdc2=VDD_CPU 1.25V`；`dcdc3=VDD_1V8 1.8V`；`dcdc4=VDD_DDR 1.35V`；`bldo1=WIFI_1V2`；`dldo1=VCC_BL`；`aldo1=VUSB_HS_3V3`
- 证据：图 aa0621b243a7 / 第 1 页 / source_005 左侧 U1 AXP2101 与各输出标注

### 5V 升压与电源路径开关

U6 SY7088 从 AXP_PS 生成 VCC_BST_5V；U2/U4 在 USB_OTG_EN 控制下切换 VUSB 与 AXP_VBUS，U3/U5 在 BUS_OUT_EN 控制下切换 BUS_OUT、AXP_VBUS 与 VCC_BST_5V。

- 参数与网络：`boost=U6 SY7088 AXP_PS to VCC_BST_5V`；`otg_switches=U2 ME1502AM5G,U4 ME1502CM5G`；`bus_switches=U3 ME1502CM5G,U5 ME1502AM5G`；`controls=USB_OTG_EN,BUS_OUT_EN`
- 证据：图 aa0621b243a7 / 第 1 页 / source_005 右半 U2-U6 电源路径

### MidLayer 外部输入电源

MidLayer J6 DC-JACK 将 BUS_IN 通过 L2 和输入滤波形成 EXT_VIN，U12 SCT9330 再通过 L1 与反馈网络生成 AXP_VBUS；J10 同时引出 BUS_IN 与 BUS_GND。

- 参数与网络：`input_connector=J6 DC-JACK`；`input_net=BUS_IN to EXT_VIN`；`converter=U12 SCT9330`；`output=AXP_VBUS`；`pwr485_connector=J10 BUS_IN/BUS_GND`
- 证据：图 803d75c0f85c / 第 1 页 / source_013 左中 J6 DC-JACK 与 EXT_VIN; 图 3f5af84c5eac / 第 1 页 / source_015 U12 SCT9330 EXT_VIN 到 AXP_VBUS; 图 bf87e025097f / 第 1 页 / source_014 J10 RS485/BUS_IN/BUS_GND

### M5-Bus 电源方向控制

BUS_OUT_EN 同时控制 U3 ME1502CM5G 与 U5 ME1502AM5G，构成 BUS_OUT、AXP_VBUS、VCC_BST_5V 之间的受控双向路径；控制信号连接 STM32MP135 PI3。

- 参数与网络：`control=BUS_OUT_EN`；`gpio=PI3`；`low_side_switch=U3 ME1502CM5G`；`high_side_switch=U5 ME1502AM5G`；`nets=BUS_OUT,AXP_VBUS,VCC_BST_5V`
- 证据：图 aa0621b243a7 / 第 1 页 / source_005 U3/U5 BUS_OUT_EN 电源开关; 图 406350a698b1 / 第 1 页 / source_006 U7C PI3-BUS_OUT_EN

## 接口

### LT8618SXB HDMI 输出链

U14 LT8618SXB 接收 RGB_D0-D23、RGB_DE/IDCK/HSYNC/VSYNC 与 SAI1_SCK_B/FS_B/SD_B/MCLK_B，通过三组数据 TMDS 与一组时钟 TMDS 驱动 J1 HDMI，并连接 DDC、CEC、HPD 与 HDMI_5V。

- 参数与网络：`bridge=U14 LT8618SXB`；`rgb_width=24 lines D0-D23`；`audio=SAI1_SCK_B,FS_B,SD_B,MCLK_B`；`output=HDMI_TX0-2,HDMI_CLK`；`control=HDMI_SCL,SDA,CEC,HPD`；`power=HDMI_5V via FUSE1 0.5A/16V`
- 证据：图 284f113b1baf / 第 1 页 / source_010 U14 LT8618SXB 到 J1 HDMI 完整链路

### USB Type-C OTG

STM32MP135 USB2_D_P/N 与 USB2_VBUS 连接 J6 USB Type-C；CC1/CC2 各通过 5.1K 接地，U25 SRV05-4 对 USB 与 CC 网络提供保护，USB_OTG_EN 控制 VUSB/AXP_VBUS 电源路径。

- 参数与网络：`connector=J6 USB Type-C`；`data=USB2_D_P/N`；`vbus=VUSB/USB2_VBUS`；`cc=CC1/CC2 5.1K to GND`；`protection=U25 SRV05-4`；`power_control=USB_OTG_EN`
- 证据：图 99fed790f48e / 第 1 页 / source_003 J6 USB Type-C 与 U25; 图 aa0621b243a7 / 第 1 页 / source_005 U2/U4 USB_OTG_EN 电源开关

### LCD 与触摸连接器

J3 16-pin Header 为显示模组提供 VCC_BL、VDD_3V3、SPI1_DC/SCK/CS/RST/MOSI、I2C3_SCL/SDA、TOUCH_INT 与 GND。

- 参数与网络：`connector=J3 Header 16P`；`display_bus=SPI1_DC,SCK,CS,RST,MOSI`；`touch_bus=I2C3_SCL,SDA,TOUCH_INT`；`rails=VCC_BL,VDD_3V3`
- 证据：图 1651951f9ae7 / 第 1 页 / source_001 左侧 J3 16-pin LCD/Touch Header

### M5-Bus 扩展信号

MidLayer P1 15x2 引出 VCC_3V3、VCC_BST_5V、VBAT、BUS_OUT、USART2、I2C1、I2C2、SPI4、DS_USB1、ADC、GPIO 与定时器网络；STM32 侧 USART2 为 PF11/PH8，I2C1 为 PB8/PE8，I2C2 为 PF2/PG9，SPI4 为 PB4/PE11/PE13。

- 参数与网络：`connector=P1 Header 15x2`；`uart2=TX PF11,RX PH8`；`i2c1=SCL PB8,SDA PE8`；`i2c2=SCL PF2,SDA PG9`；`spi4=SCK PB4,MOSI PE11,MISO PE13`；`usb=DS_USB1_D_P/N`；`power=VCC_3V3,VCC_BST_5V,VBAT,BUS_OUT`
- 证据：图 803d75c0f85c / 第 1 页 / source_013 上部 P1 M5-Bus 引脚; 图 32529857ea6d / 第 1 页 / source_011 U7A/U7B USART2、I2C1/2、SPI4 复用映射

### Grove I2C 与 UART

MidLayer J3 Grove 引出 VCC_BST_5V、I2C5_SDA/SCL 与 GND，J4 Grove 引出 VCC_BST_5V、USART6_TX/RX 与 GND；I2C5 对应 PF3/PA11，USART6 对应 PC7/PC6。

- 参数与网络：`i2c_grove=J3 I2C5_SDA/SCL`；`uart_grove=J4 USART6_TX/RX`；`i2c_gpio=SDA PF3,SCL PA11`；`uart_gpio=TX PC7,RX PC6`；`supply=VCC_BST_5V`；`protection=PESD3V3 plus NFZ15SG331`
- 证据：图 803d75c0f85c / 第 1 页 / source_013 J3/J4 Grove 接口; 图 32529857ea6d / 第 1 页 / source_011 U7A/U7B I2C5 与 USART6 映射

## 总线

### 双 RGMII 以太网链路

STM32MP135 的 ETH1/ETH2 RGMII 网络分别连接 U12/U13 RTL8211F-CG；每颗 PHY 通过 MDI0-MDI3 四对差分线跨板到 MidLayer，经 PSCIAQ4532-101Z 共模器件进入 J7B/J7A HY911261C RJ45。

- 参数与网络：`eth1_phy=U12 RTL8211F-CG`；`eth2_phy=U13 RTL8211F-CG`；`host=RGMII ETH1/ETH2`；`mdi_pairs=4 per port`；`connectors=J7B/J7A HY911261C`；`phy_strap_label=3'b001`
- 证据：图 6450e97913a5 / 第 1 页 / source_009 ETH1/ETH2 U12/U13 与 MDI/RGMII; 图 803d75c0f85c / 第 1 页 / source_013 下部双 MDI 共模器件与 J7A/J7B RJ45

### GL852G 四端口 USB Hub

U18 GL852G 以上行 USB1_D_N/P 连接 STM32MP135 USB Host 1，生成 DS_USB1-D4 四组下行差分线；DS_USB3/4 连接两个 USB-A，DS_USB1/2 经板间连接器分发。

- 参数与网络：`hub=U18 GL852G`；`upstream=USB1_D_N/P`；`downstream=DS_USB1-D4`；`external_type_a=DS_USB3 to U20,DS_USB4 to U22`；`distributed=DS_USB1,DS_USB2`；`crystal=X3 12MHz`
- 证据：图 6b81d573e1d5 / 第 1 页 / source_012 U18 GL852G、U20/U22 与 DS_USB1-D4; 图 99fed790f48e / 第 1 页 / source_003 J5/U24 上的 DS_USB1/DS_USB2 网络

### 双 FDCAN 物理层

FDCAN1 使用 PE10 TX 与 PE3 RX 连接 U6 SIT1051T/3，FDCAN2 使用 PG0 TX 与 PE0 RX 连接 U9 SIT1051T/3；两路 CANH/CANL 均经过 SP03-3.3/LC03-3.3 保护和 PSCIAQ4532-101Z 共模器件后到 J8/J9。

- 参数与网络：`fdcan1_gpio=TX PE10,RX PE3`；`fdcan2_gpio=TX PG0,RX PE0`；`transceivers=U6/U9 SIT1051T/3`；`protection=U7/U8 SP03-3.3/LC03-3.3`；`filters=L12/L13 PSCIAQ4532-101Z`；`connectors=J8/J9`
- 证据：图 32529857ea6d / 第 1 页 / source_011 U7B FDCAN1/FDCAN2 GPIO; 图 bf87e025097f / 第 1 页 / source_014 上半双 SIT1051T/3、保护、共模器件与 J8/J9

### USART3 RS485 链路

USART3_TX PD8、USART3_RX PG4 与 USART3_DE PD12 连接 U10 MAX3485EIM；A/B 输出标为 RS485_P/N，经过 U11 SP03-3.3/LC03-3.3 和 L14 PSCIAQ4532-101Z 后进入 J10。

- 参数与网络：`transceiver=U10 MAX3485EIM`；`tx=PD8`；`rx=PG4`；`de_re=PD12`；`bus=RS485_P/N`；`protection=U11 SP03-3.3/LC03-3.3`；`filter=L14 PSCIAQ4532-101Z`；`connector=J10`
- 证据：图 32529857ea6d / 第 1 页 / source_011 USART3_RX/TX/DE GPIO; 图 bf87e025097f / 第 1 页 / source_014 下部 U10 MAX3485EIM 到 J10

### I2C3 共享总线

I2C3_SCL/SDA 由 STM32MP135 PH12/PH7 提供，并连接 AXP2101、BM8563、LCD/触摸 Header 与 LT8618SXB；R101/R102 以 1K 上拉到 VDD_3V3。

- 参数与网络：`controller_gpio=SCL PH12,SDA PH7`；`devices=AXP2101,BM8563,J3 LCD/Touch,LT8618SXB`；`pullups=R101/R102 1K to VDD_3V3`
- 证据：图 aa0621b243a7 / 第 1 页 / source_005 AXP2101 I2C3; 图 406350a698b1 / 第 1 页 / source_006 BM8563 与 R101/R102 I2C3 上拉; 图 284f113b1baf / 第 1 页 / source_010 LT8618SXB CSCK/CSDA

## GPIO 与控制信号

### LCD 与触摸 GPIO 映射

SPI1_MOSI/SCK/DC/CS 分别位于 PC0/PC3/PH4/PH5，SPI1_RST 与 TOUCH_INT 分别位于 PI0/PI1；I2C3_SDA/SCL 分别位于 PH7/PH12。

- 参数与网络：`mosi=PC0`；`sck=PC3`；`dc=PH4`；`cs=PH5`；`reset=PI0`；`touch_int=PI1`；`touch_sda=PH7`；`touch_scl=PH12`
- 证据：图 406350a698b1 / 第 1 页 / source_006 U7C PI0-PI3 控制信号; 图 32529857ea6d / 第 1 页 / source_011 U7A/U7B PC0/PC3/PH4/PH5/PH7/PH12 网络

## 时钟

### 处理器、RTC、以太网、Wi-Fi 与 USB Hub 时钟

STM32MP135 使用 X1 24MHz 晶体；BM8563 使用 Y1 晶体；RTL8188FTV 使用 X4 40MHz 晶体；两颗 RTL8211F-CG 分别使用 X6/X5 25MHz 晶体；GL852G 使用 X3 12MHz 晶体。

- 参数与网络：`soc=X1 24MHz`；`rtc=Y1 TXC/9H0320`；`wifi=X4 40MHz`；`eth1=X6 25MHz`；`eth2=X5 25MHz`；`usb_hub=X3 12MHz`
- 证据：图 406350a698b1 / 第 1 页 / source_006 X1 与 BM8563/Y1; 图 302e2a3a2e24 / 第 1 页 / source_002 X4 40MHz; 图 6450e97913a5 / 第 1 页 / source_009 X6/X5 25MHz; 图 6b81d573e1d5 / 第 1 页 / source_012 X3 12MHz

## 复位

### 复位与启动绑带

STM32MP135 NRST 由 AXP_PWROK 驱动并通过 R41 10K 上拉到 VDD_3V3；ST_BOOT0 通过 R11 10K 上拉，ST_BOOT1 通过 R15 10K 下拉，ST_BOOT2 通过 R13 10K 上拉。

- 参数与网络：`reset=AXP_PWROK to NRST,10K pull-up`；`boot0=10K pull-up`；`boot1=10K pull-down`；`boot2=10K pull-up`
- 证据：图 406350a698b1 / 第 1 页 / source_006 上部 U7C NRST 与 ST_BOOT0/1/2 电阻

## 保护电路

### HDMI 与 USB 保护

HDMI 三组 TMDS、时钟、CEC、SCL、SDA 与 HPD 通过 U15-U17 PESDALC10N5VU 保护，HDMI_5V 串联 FUSE1 0.5A/16V；USB Type-C 使用 U25 SRV05-4，MidLayer DS_USB1 使用 U14 SP3050。

- 参数与网络：`hdmi_esd=U15-U17 PESDALC10N5VU`；`hdmi_fuse=FUSE1 0.5A/16V`；`type_c_esd=U25 SRV05-4`；`midlayer_usb_esd=U14 SP3050`
- 证据：图 284f113b1baf / 第 1 页 / source_010 U15-U17 与 FUSE1; 图 99fed790f48e / 第 1 页 / source_003 U25 SRV05-4; 图 803d75c0f85c / 第 1 页 / source_013 U14 SP3050

### CAN、RS485、Grove 与以太网保护

两路 CAN 与 RS485 均配置 SP03-3.3/LC03-3.3 阵列和 PSCIAQ4532-101Z 共模器件；两路以太网四对 MDI 使用 PSCIAQ4532-101Z；Grove I2C5/USART6 信号配置 PESD3V3 和 NFZ15SG331。

- 参数与网络：`can_rs485=SP03-3.3/LC03-3.3 plus PSCIAQ4532-101Z`；`ethernet=PSCIAQ4532-101Z per MDI pair`；`grove=PESD3V3 plus NFZ15SG331`
- 证据：图 bf87e025097f / 第 1 页 / source_014 CAN/RS485 保护与共模器件; 图 803d75c0f85c / 第 1 页 / source_013 Ethernet 与 Grove 保护器件

## 存储

### microSD 四位接口

U10 microSD 由 VDD_3V3 供电，DAT0-DAT3 与 CMD 各经 10K 上拉，CLK 串联 R28 22R 并通过 R100 10K 下拉。

- 参数与网络：`reference=U10`；`bus=SD_DAT0-DAT3,SD_CMD,SD_CLK`；`supply=VDD_3V3`；`data_pullups=R103-R107 10K`；`clock_series=R28 22R`；`clock_pulldown=R100 10K`
- 证据：图 8262f47a5d77 / 第 1 页 / source_008 U10 microSD 全部连接

## 内存与 Flash

### DDR3L 接口

U7D 通过 DQ0-DQ15、DQS0/1、CLK、A0-A15、BA0-BA2、RAS/CAS/CS/CKE/WE/ODT/RESET 等网络连接 U9 DDR3L_DRAM，构成 16-bit 数据总线。

- 参数与网络：`controller=U7D STM32MP135DAE7`；`memory=U9 DDR3L_DRAM`；`data_width=16-bit`；`rail=VDD_DDR`；`capacity=null`
- 证据：图 ae9e1037fa30 / 第 1 页 / source_007 U7D 与 U9 的完整 DDR3L 网络

## 音频

### NS4168 扬声器链路

U13 NS4168 由 VCC_3V3 供电且 CTRL 接 VCC_3V3，接收 SAI1_FS_A、SAI1_SCK_A、SAI1_SD_A，VON/VOP 经 FB1/FB2 后差分连接 J11 两针扬声器接口。

- 参数与网络：`amplifier=U13 NS4168`；`supply=VCC_3V3`；`lrclk=SAI1_FS_A`；`bclk=SAI1_SCK_A`；`sdata=SAI1_SD_A`；`output=VON/VOP to J11`；`filters=FB1/FB2 1kR@100MHz`
- 证据：图 ad2679ae4a5c / 第 1 页 / source_016 U13 NS4168、FB1/FB2 与 J11

## 射频

### USB Wi-Fi 与天线链路

U23 RTL8188FTV 通过 DS_USB2_D_N/P 接入 USB Hub 下行网络，WIFI_EN 控制使能，WIFI_1V2 与 VDD_3V3 供电，RF_OUT 经匹配网络连接 J7 IPEX。

- 参数与网络：`controller=U23 RTL8188FTV`；`host_bus=DS_USB2_D_N/P`；`enable=WIFI_EN`；`rails=WIFI_1V2,VDD_3V3`；`antenna=RF_OUT to J7 IPEX`；`crystal=X4 40MHz`
- 证据：图 302e2a3a2e24 / 第 1 页 / source_002 U23、RF_OUT、J7、X4 与电源网络

## 调试与烧录

### STM32 调试信号

STM_SWCLK 与 STM_SWDIO 分别连接 STM32MP135 PF14 与 PF15，并通过 U24 40-pin 板间连接器引出到 MidLayer。

- 参数与网络：`swclk=PF14`；`swdio=PF15`；`interconnect=U24 40-pin`
- 证据：图 32529857ea6d / 第 1 页 / source_011 U7B PF14/PF15 STM_SWCLK/STM_SWDIO; 图 99fed790f48e / 第 1 页 / source_003 U24 STM_SWCLK/STM_SWDIO 引脚

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CoreMP135 双板系统架构 | `main_board_pages=source_001-source_012`；`midlayer_pages=source_013-source_016`；`processor=STM32MP135DAE7`；`interconnect=J3/J4/J5/U24 to J1/J2/U1` |
| 核心器件 | 主处理器原理图料号 | `reference=U7A-U7E`；`part_number=STM32MP135DAE7`；`power_unit=U7E`；`ddr_unit=U7D`；`gpio_units=U7A/U7B`；`system_unit=U7C` |
| 内存与 Flash | DDR3L 接口 | `controller=U7D STM32MP135DAE7`；`memory=U9 DDR3L_DRAM`；`data_width=16-bit`；`rail=VDD_DDR`；`capacity=null` |
| 电源 | AXP2101 主电源轨 | `dcdc1=VDD_3V3 3.3V`；`dcdc2=VDD_CPU 1.25V`；`dcdc3=VDD_1V8 1.8V`；`dcdc4=VDD_DDR 1.35V`；`bldo1=WIFI_1V2`；`dldo1=VCC_BL`；`aldo1=VUSB_HS_3V3` |
| 电源 | 5V 升压与电源路径开关 | `boost=U6 SY7088 AXP_PS to VCC_BST_5V`；`otg_switches=U2 ME1502AM5G,U4 ME1502CM5G`；`bus_switches=U3 ME1502CM5G,U5 ME1502AM5G`；`controls=USB_OTG_EN,BUS_OUT_EN` |
| 时钟 | 处理器、RTC、以太网、Wi-Fi 与 USB Hub 时钟 | `soc=X1 24MHz`；`rtc=Y1 TXC/9H0320`；`wifi=X4 40MHz`；`eth1=X6 25MHz`；`eth2=X5 25MHz`；`usb_hub=X3 12MHz` |
| 复位 | 复位与启动绑带 | `reset=AXP_PWROK to NRST,10K pull-up`；`boot0=10K pull-up`；`boot1=10K pull-down`；`boot2=10K pull-up` |
| 存储 | microSD 四位接口 | `reference=U10`；`bus=SD_DAT0-DAT3,SD_CMD,SD_CLK`；`supply=VDD_3V3`；`data_pullups=R103-R107 10K`；`clock_series=R28 22R`；`clock_pulldown=R100 10K` |
| 射频 | USB Wi-Fi 与天线链路 | `controller=U23 RTL8188FTV`；`host_bus=DS_USB2_D_N/P`；`enable=WIFI_EN`；`rails=WIFI_1V2,VDD_3V3`；`antenna=RF_OUT to J7 IPEX`；`crystal=X4 40MHz` |
| 总线 | 双 RGMII 以太网链路 | `eth1_phy=U12 RTL8211F-CG`；`eth2_phy=U13 RTL8211F-CG`；`host=RGMII ETH1/ETH2`；`mdi_pairs=4 per port`；`connectors=J7B/J7A HY911261C`；`phy_strap_label=3'b001` |
| 接口 | LT8618SXB HDMI 输出链 | `bridge=U14 LT8618SXB`；`rgb_width=24 lines D0-D23`；`audio=SAI1_SCK_B,FS_B,SD_B,MCLK_B`；`output=HDMI_TX0-2,HDMI_CLK`；`control=HDMI_SCL,SDA,CEC,HPD`；`power=HDMI_5V via FUSE1 0.5A/16V` |
| 总线 | GL852G 四端口 USB Hub | `hub=U18 GL852G`；`upstream=USB1_D_N/P`；`downstream=DS_USB1-D4`；`external_type_a=DS_USB3 to U20,DS_USB4 to U22`；`distributed=DS_USB1,DS_USB2`；`crystal=X3 12MHz` |
| 接口 | USB Type-C OTG | `connector=J6 USB Type-C`；`data=USB2_D_P/N`；`vbus=VUSB/USB2_VBUS`；`cc=CC1/CC2 5.1K to GND`；`protection=U25 SRV05-4`；`power_control=USB_OTG_EN` |
| 接口 | LCD 与触摸连接器 | `connector=J3 Header 16P`；`display_bus=SPI1_DC,SCK,CS,RST,MOSI`；`touch_bus=I2C3_SCL,SDA,TOUCH_INT`；`rails=VCC_BL,VDD_3V3` |
| GPIO 与控制信号 | LCD 与触摸 GPIO 映射 | `mosi=PC0`；`sck=PC3`；`dc=PH4`；`cs=PH5`；`reset=PI0`；`touch_int=PI1`；`touch_sda=PH7`；`touch_scl=PH12` |
| 接口 | M5-Bus 扩展信号 | `connector=P1 Header 15x2`；`uart2=TX PF11,RX PH8`；`i2c1=SCL PB8,SDA PE8`；`i2c2=SCL PF2,SDA PG9`；`spi4=SCK PB4,MOSI PE11,MISO PE13`；`usb=DS_USB1_D_P/N`；`power=VCC_3V3,VCC_BST_5V,VBAT,BUS_OUT` |
| 接口 | Grove I2C 与 UART | `i2c_grove=J3 I2C5_SDA/SCL`；`uart_grove=J4 USART6_TX/RX`；`i2c_gpio=SDA PF3,SCL PA11`；`uart_gpio=TX PC7,RX PC6`；`supply=VCC_BST_5V`；`protection=PESD3V3 plus NFZ15SG331` |
| 总线 | 双 FDCAN 物理层 | `fdcan1_gpio=TX PE10,RX PE3`；`fdcan2_gpio=TX PG0,RX PE0`；`transceivers=U6/U9 SIT1051T/3`；`protection=U7/U8 SP03-3.3/LC03-3.3`；`filters=L12/L13 PSCIAQ4532-101Z`；`connectors=J8/J9` |
| 总线 | USART3 RS485 链路 | `transceiver=U10 MAX3485EIM`；`tx=PD8`；`rx=PG4`；`de_re=PD12`；`bus=RS485_P/N`；`protection=U11 SP03-3.3/LC03-3.3`；`filter=L14 PSCIAQ4532-101Z`；`connector=J10` |
| 电源 | MidLayer 外部输入电源 | `input_connector=J6 DC-JACK`；`input_net=BUS_IN to EXT_VIN`；`converter=U12 SCT9330`；`output=AXP_VBUS`；`pwr485_connector=J10 BUS_IN/BUS_GND` |
| 电源 | M5-Bus 电源方向控制 | `control=BUS_OUT_EN`；`gpio=PI3`；`low_side_switch=U3 ME1502CM5G`；`high_side_switch=U5 ME1502AM5G`；`nets=BUS_OUT,AXP_VBUS,VCC_BST_5V` |
| 音频 | NS4168 扬声器链路 | `amplifier=U13 NS4168`；`supply=VCC_3V3`；`lrclk=SAI1_FS_A`；`bclk=SAI1_SCK_A`；`sdata=SAI1_SD_A`；`output=VON/VOP to J11`；`filters=FB1/FB2 1kR@100MHz` |
| 总线 | I2C3 共享总线 | `controller_gpio=SCL PH12,SDA PH7`；`devices=AXP2101,BM8563,J3 LCD/Touch,LT8618SXB`；`pullups=R101/R102 1K to VDD_3V3` |
| 调试与烧录 | STM32 调试信号 | `swclk=PF14`；`swdio=PF15`；`interconnect=U24 40-pin` |
| 保护电路 | HDMI 与 USB 保护 | `hdmi_esd=U15-U17 PESDALC10N5VU`；`hdmi_fuse=FUSE1 0.5A/16V`；`type_c_esd=U25 SRV05-4`；`midlayer_usb_esd=U14 SP3050` |
| 保护电路 | CAN、RS485、Grove 与以太网保护 | `can_rs485=SP03-3.3/LC03-3.3 plus PSCIAQ4532-101Z`；`ethernet=PSCIAQ4532-101Z per MDI pair`；`grove=PESD3V3 plus NFZ15SG331` |
| 核心器件 | STM32MP135 完整料号冲突 | `documented_product_part=STM32MP135DAE7`；`schematic_part=STM32MP135DAE7`；`datasheet_link_text=STM32MP135DAF7`；`assembly_part=null` |
| 内存与 Flash | DDR3L 容量 | `documented_capacity=4Gbit`；`schematic_part=DDR3L_DRAM`；`schematic_capacity=null`；`bom_part=null` |
| 核心器件 | LCD 与触摸模组参数 | `documented_lcd=ILI9342C`；`documented_touch=FT6336U`；`documented_size=2.0 inch`；`documented_resolution=240 x 320`；`schematic_module_parts=null` |
| 音频 | 音频额定值与采样能力 | `documented_speaker=1W@8ohm`；`documented_sample_rate=8kHz-96kHz`；`amplifier=NS4168`；`schematic_rating=null` |
| 电源 | 外部电源输入额定范围 | `documented_pwr485=9-24V`；`documented_dc=12V@2A`；`documented_usb_c=5V@3A`；`schematic_input_rating=null` |
| 总线地址 | I2C3 器件地址 | `bus=I2C3`；`devices=AXP2101,BM8563,LT8618SXB,external touch module`；`numeric_addresses=null` |
| 总线 | 以太网数据速率 | `documented_ports=2`；`documented_rate=1Gbps`；`phys=U12/U13 RTL8211F-CG`；`host_bus=RGMII`；`schematic_rate_text=null` |

## 待确认事项

- `component.soc-document-conflict`：产品正文与原理图器件单元标注 STM32MP135DAE7，但数据手册链接文字标为 STM32MP135DAF7；现有图面不能证明 DAF7 变体装配。（证据：图 17ad800da5d3 / 第 1 页 / source_004 U7E 标注 STM32MP135DAE7; 图 32529857ea6d / 第 1 页 / source_011 U7A/U7B 标注 STM32MP135DAE7）
- `memory.documented-capacity`：产品正文称 DDR3L 容量为 4Gbit；原理图 U9 只标 DDR3L_DRAM 与 16-bit 总线，没有具体料号或容量。（证据：图 ae9e1037fa30 / 第 1 页 / source_007 U9 仅标 DDR3L_DRAM）
- `component.display-module-parameters`：产品正文称显示控制器为 ILI9342C、触摸控制器为 FT6336U，并给出 2.0 英寸和 240 x 320；原理图只显示 J3 LCD/Touch Header，没有画出这两颗器件或面板参数。（证据：图 1651951f9ae7 / 第 1 页 / source_001 仅有 J3 LCD/Touch Header 与外部信号）
- `audio.documented-rating`：产品正文称扬声器为 1W@8ohm，NS4168 支持 8kHz-96kHz；原理图只确认 NS4168、3.3V 供电、SAI1 输入和差分扬声器接口，没有打印扬声器阻抗、功率或采样率范围。（证据：图 ad2679ae4a5c / 第 1 页 / source_016 U13 NS4168 与 J11，无功率/阻抗/采样率文字）
- `power.documented-input-rating`：产品正文给出 PWR485 9-24V、DC 12V@2A 与 USB-C 5V@3A；原理图只显示 BUS_IN/EXT_VIN 经 SCT9330 到 AXP_VBUS，以及 VUSB 电源路径，没有标出这些额定输入范围。（证据：图 803d75c0f85c / 第 1 页 / source_013 J6 DC-JACK 与 BUS_IN/EXT_VIN，无额定范围; 图 3f5af84c5eac / 第 1 页 / source_015 U12 SCT9330 与反馈网络，无输入范围文字; 图 99fed790f48e / 第 1 页 / source_003 J6 Type-C，仅 VUSB/CC/USB2 网络）
- `address.i2c3-devices`：AXP2101、BM8563、LT8618SXB 与外部触摸接口共享 I2C3，但四组相关原理图没有打印 7-bit 数值地址。（证据：图 aa0621b243a7 / 第 1 页 / source_005 AXP2101 I2C3 引脚，无数值地址; 图 406350a698b1 / 第 1 页 / source_006 BM8563 I2C3 引脚，无数值地址; 图 284f113b1baf / 第 1 页 / source_010 LT8618SXB CSCK/CSDA，无数值地址; 图 1651951f9ae7 / 第 1 页 / source_001 外部触摸 I2C3 Header，无控制器地址）
- `bus.documented-ethernet-rate`：产品正文称两路以太网最高 1Gbps；原理图确认双 RTL8211F-CG、RGMII、每端口四对 MDI 与双 RJ45，但页面没有打印速率数字。（证据：图 6450e97913a5 / 第 1 页 / source_009 双 RTL8211F-CG 与 RGMII/MDI，无速率数字; 图 803d75c0f85c / 第 1 页 / source_013 J7A/J7B 双 RJ45，无速率数字）
- `review.soc-part`：请用当前量产 BOM、芯片丝印与正式 datasheet 确认实际装配为 STM32MP135DAE7 还是 STM32MP135DAF7。；原因：产品正文和全部原理图单元标 DAE7，数据手册链接文字标 DAF7。
- `review.ddr-capacity`：请用 U9 量产料号、BOM 或系统内存检测确认 DDR3L 容量为 4Gbit。；原因：原理图只标 DDR3L_DRAM，没有容量字段。
- `review.display-module`：请补充 LCD/触摸模组 BOM、模组原理图或实物丝印，确认 ILI9342C、FT6336U、2.0 英寸与 240 x 320 参数。；原因：当前原理图只画出外部 Header 和信号，没有显示控制器本体与面板参数。
- `review.audio-rating`：请用扬声器 BOM、NS4168 datasheet 与整机测试确认 1W@8ohm 和 8kHz-96kHz。；原因：原理图只给出器件型号与电气连接，未标额定功率、阻抗或采样率。
- `review.input-rating`：请用 SCT9330 设计计算、BOM 与整机电源测试确认 PWR485 9-24V、DC 12V@2A 和 USB-C 5V@3A。；原因：这些额定值出现在产品正文，原理图只显示电源拓扑。
- `review.i2c-addresses`：请依据 AXP2101、BM8563、LT8618SXB 和触摸控制器的当前 datasheet/strap/固件确认各自 7-bit I2C 地址。；原因：原理图展示 I2C3 连接但未打印数值地址。
- `review.ethernet-rate`：请用 RTL8211F-CG datasheet、PHY 配置和链路测试确认两个端口均支持并工作于最高 1Gbps。；原因：原理图确认双 PHY/RGMII/四对 MDI，但没有打印速率数字。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1651951f9ae713bc1aa308e480a04f9831ff2656b925ff472ecf119f237b867c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_01.png` |
| 2 | 1 | `302e2a3a2e24db566e249cac71e10b33ce21a6ab625f20f87db5a704aeff51c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_02.png` |
| 3 | 1 | `99fed790f48e791f598b735007c457e87275eb533c8a7a257a3bcf5ad2cccdd6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_03.png` |
| 4 | 1 | `17ad800da5d3b3d80d50cfbce00ed9ff4a1b0c68995978bfaedfd04675493a9c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_04.png` |
| 5 | 1 | `aa0621b243a762355fe162ac24768b216da3643294980d0d0c2ad468cb18bc37` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_05.png` |
| 6 | 1 | `406350a698b162438ac89f993c5ad7ac89f2ef1dd7d2f74fb81673f6e041c1f4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_06.png` |
| 7 | 1 | `ae9e1037fa302f00044ff0762388c07dea86343e288f8f922aec8d23236436d4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_07.png` |
| 8 | 1 | `8262f47a5d7798d8163a3ed7a49d851e75396378cd499766736c377e8f811d74` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_08.png` |
| 9 | 1 | `6450e97913a5767be9cc79ebdbc75d3b3fcd40d486a8221c410910ee51ab1085` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_09.png` |
| 10 | 1 | `284f113b1baf992f80dbc14cf39eb20ec38735525f89b38d39e8b6f73c3488b8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_10.png` |
| 11 | 1 | `32529857ea6d6898aa6dc978dd70d01026cd95a9e3b3b9f13155d828cd5ae91d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_11.png` |
| 12 | 1 | `6b81d573e1d52525e8f2c04f720ac8256d01ed985e8a76dd6374eacd1374a308` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_12.png` |
| 13 | 1 | `803d75c0f85cf3b7fb2f64d3695aa21ab3c1bc6cc453f131c156d54192301ab6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_01.png` |
| 14 | 1 | `bf87e025097fd4e82a7412979f398bb049173f41cb3efdf62b1d2492f7283ee4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_02.png` |
| 15 | 1 | `3f5af84c5eac1162e40b6becd7cf81b7053ea709d1a20b062eeeb8a9f469919f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_03.png` |
| 16 | 1 | `ad2679ae4a5c5efeea80ad85a1c6eea716cc1a7ac1126e3053376c1d0440230c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_04.png` |

---

源文档：`zh_CN/core/M5CoreMP135.md`

源文档 SHA-256：`2fe82015a14c75233c3358dae59555b6a0334e9b952380671eecc099ce9455c1`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
