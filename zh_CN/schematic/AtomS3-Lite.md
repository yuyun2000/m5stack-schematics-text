# AtomS3-Lite 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3-Lite |
| SKU | C124 |
| 产品 ID | `atoms3-lite-26b960545806` |
| 源文档 | `zh_CN/core/AtomS3 Lite.md` |

## 概述

AtomS3-Lite 以 ESP32-S3FN8 为核心，使用 40 MHz 晶体和板载 PROANT440 天线，并预留由 NC 电阻隔离的 IPEX 射频接口。USB Type-C 提供 VIN_5V 和原生 USB D+/D-，SY8089 将 5V 转换为 VDD_3V3。板上还包含 WS2812 RGB、GPIO4 红外发射、用户键与复位键、USB 下载辅助电路，以及 GPIO 排针和 GH2.0-4P 扩展接口。原理图另画有一组 LCD 背光开关及 8 针显示连接器，但其在 C124 Lite 硬件上的实际装配状态需人工确认。

## 检索关键词

`AtomS3-Lite`、`C124`、`ESP32-S3FN8`、`SY8089`、`WS2812`、`SGM2578`、`WS4022C-4/TR`、`GS321`、`PROANT440`、`IPEX`、`40MHz`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`GPIO0`、`GPIO1`、`GPIO2`、`GPIO4`、`GPIO5`、`GPIO6`、`GPIO7`、`GPIO8`、`GPIO35`、`GPIO38`、`GPIO39`、`USER_BUT`、`ESP_EN`、`SK_DIN`、`LCD_BL_DRV`、`GH2.0-4P`、`红外发射`、`RGB LED`、`ESD5Z3V3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | 主控 SoC，承载 USB、GPIO、射频、按键、RGB、红外和扩展接口 | 图 5669c9c29e16 / 第 1 页 / 网格 2A-C，U1 ESP32-S3FN8 主控符号及全部电源、时钟和 GPIO 网络 |
| U4 | SY8089 | VIN_5V 到 VDD_3V3 的降压转换器 | 图 5669c9c29e16 / 第 1 页 / 网格 1D-2D，U4 SY8089、L4、R11、R12 与 VIN_5V/VDD_3V3 |
| X1 | 40MHz | ESP32-S3 主时钟晶体 | 图 5669c9c29e16 / 第 1 页 / 网格 1B，X1 40MHz、L3、C9、C14 与 XTAL_40M_P/N |
| ANT1 | PROANT440 | 板载 2.4 GHz 射频天线 | 图 5669c9c29e16 / 第 1 页 / 网格 1A，ANT1 PROANT440 经 L1、R1 接 ESP_LNA |
| J1 | IPEX | 预留外置射频天线连接器 | 图 5669c9c29e16 / 第 1 页 / 网格 1A-B，J1 IPEX 的信号端通过 R2 NC 接 ESP_LNA 匹配节点，外壳接地 |
| U3 | WS2812 | 单线可编程 RGB 状态 LED | 图 5669c9c29e16 / 第 1 页 / 网格 3B，U3 WS2812，DI=SK_DIN、DO=SK_DOUT、VDD=VDD_3V3 |
| IR | 未标注 | GPIO4 控制的红外发射 LED | 图 5669c9c29e16 / 第 1 页 / 网格 3B，IR 发射 LED 串联 R16 22Ω，输入网络为 GPIO4 |
| S1 | SMT_SW_P1S_820 | 低有效用户按键 | 图 5669c9c29e16 / 第 1 页 / 网格 3B-C，S1 将 USER_BUT 接地，R4 10kΩ 上拉并由 D1 防护 |
| S2 | SMT_SW_TS_015 | ESP32-S3 复位按键 | 图 5669c9c29e16 / 第 1 页 / 网格 3C，S2 将 ESP_EN 接地，ESP_EN 由 R7 上拉、C23 延时并由 D3 防护 |
| U5 | GS321 | 监测 ESP_EN 并驱动 GPIO0/下载指示网络的比较器电路 | 图 5669c9c29e16 / 第 1 页 / 网格 3D，U5 GS321、D6/D7、R8/R10/R13/R14 与 GPIO0、LED1 |
| J5 | USB-TYPEC | USB 2.0 设备与 5V 电源输入连接器 | 图 5669c9c29e16 / 第 1 页 / 网格 3C-4C，J5 USB-TYPEC、CC1/CC2、USB_D_P/N、F1 与 ESD 器件 |
| F1 | 6V/1A/PPTC | USB VBUS 到 VIN_5V 的可恢复保险丝 | 图 5669c9c29e16 / 第 1 页 / 网格 3C，F1 6V/1A/PPTC 串联于 J5 VCC 与 VIN_5V |
| U2 | SGM2578 / WS4022C-4/TR | VDD_3V3 控制到 LCD_BL 的背光负载开关 | 图 5669c9c29e16 / 第 1 页 / 网格 3A，U2 标注 SGM2578、WS4022C-4/TR，VIN=VDD_3V3、VOUT=LCD_BL、EN=LCD_BL_DRV |
| J2 | HDGC/0.5K-HX-8PWB | 原理图中的 8 针 SPI 显示连接器 | 图 5669c9c29e16 / 第 1 页 / 网格 4A，J2 8 针连接器，LCD_BL、GND、DISP_RST、DISP_RS、SPI_MOSI、SPI_SCK、VDD_3V3、DISP_CS |
| J3 | THT_Male_P_1x5 | 3.3V 与 GPIO5-GPIO8 扩展排针 | 图 5669c9c29e16 / 第 1 页 / 网格 4B，J3 pin1=VDD_3V3、pin2=GPIO5、pin3=GPIO6、pin4=GPIO7、pin5=GPIO8 |
| J4 | THT_Male_P_1x4 | TTL3.3V、GPIO39、GPIO38 与 VIN_5V 扩展排针 | 图 5669c9c29e16 / 第 1 页 / 网格 4B，J4 pin1=TTL3.3V、pin2=GPIO39、pin3=GPIO38、pin4=VIN_5V |
| J6 | GH2.0-4P | GPIO1/GPIO2、5V 和 GND 扩展接口 | 图 5669c9c29e16 / 第 1 页 / 网格 4D，J6 pin1=GPIO1、pin2=GPIO2、pin3=VIN_5V、pin4=GND，GPIO 线带 D5/D8 ESD |

## 系统结构

### ESP32-S3FN8 主控架构

U1 ESP32-S3FN8 连接射频天线、40MHz 晶体、原生 USB、RGB LED、红外 LED、用户键、复位/下载电路和全部外部 GPIO 接口。

- 参数与网络：`reference=U1`；`part_number=ESP32-S3FN8`；`core_supply=VDD_3V3`；`rf_net=ESP_LNA`；`enable_net=ESP_EN`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1A-2C，U1 与周围时钟、射频、电源及右侧功能网络

## 电源

### USB 5V 输入路径

J5 USB Type-C 的 VCC 经 F1 6V/1A PPTC 自恢复保险丝输出到 VIN_5V，VIN_5V 由 C19 10uF 和 C20 100nF 去耦后进入 U4。

- 参数与网络：`connector=J5`；`fuse=F1 6V/1A/PPTC`；`output_net=VIN_5V`；`input_decoupling=C19 10uF, C20 100nF`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 3C 的 J5/F1 与网格 1D 的 VIN_5V、C19、C20、U4 IN

### VDD_3V3 降压电源

U4 SY8089 从 VIN_5V 降压，经 L4 2.2uH 输出 VDD_3V3，反馈分压由 R11 100kΩ 和 R12 22.1kΩ 构成。

- 参数与网络：`converter=U4 SY8089`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 2.2uH/1.2A/0806`；`feedback=R11 100kΩ, R12 22.1kΩ`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1D-2D，U4、L4、R11、R12 和 VDD_3V3 输出电容

## 接口

### USB Type-C 数据与角色配置

J5 的 DP1/DP2 并接 USB_D_P，DN1/DN2 并接 USB_D_N；CC1 和 CC2 各通过 5.1kΩ 电阻接地。

- 参数与网络：`connector=J5 USB-TYPEC`；`dp_net=USB_D_P`；`dm_net=USB_D_N`；`cc1_pulldown=R5 5.1kΩ`；`cc2_pulldown=R6 5.1kΩ`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 3C-4C，J5 DP/DN/CC 引脚及 R5、R6

### J3 五针扩展排针

J3 pin1 提供 VDD_3V3，pin2-pin5 依次引出 GPIO5、GPIO6、GPIO7、GPIO8。

- 参数与网络：`connector=J3`；`pin1=VDD_3V3`；`pin2=GPIO5`；`pin3=GPIO6`；`pin4=GPIO7`；`pin5=GPIO8`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 4B，J3 THT_Male_P_1x5 与五个引出网络

### J4 四针扩展排针

J4 pin1 提供 TTL3.3V，pin2 引出 GPIO39，pin3 引出 GPIO38，pin4 提供 VIN_5V。

- 参数与网络：`connector=J4`；`pin1=TTL3.3V`；`pin2=GPIO39`；`pin3=GPIO38`；`pin4=VIN_5V`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 4B，J4 THT_Male_P_1x4 与 TTL3.3V/GPIO39/GPIO38/VIN_5V

### J6 GH2.0-4P 扩展接口

J6 pin1=GPIO1、pin2=GPIO2、pin3=VIN_5V、pin4=GND；GPIO1 和 GPIO2 分别由 D5、D8 ESD5Z3V3 对地防护。

- 参数与网络：`connector=J6 GH2.0-4P`；`pin1=GPIO1`；`pin2=GPIO2`；`pin3=VIN_5V`；`pin4=GND`；`protection=D5 on GPIO1, D8 on GPIO2`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 4D，J6、D5、D8 与 GPIO1/GPIO2/VIN_5V/GND

### 原理图中的 SPI 显示连接器

J2 八针连接器在原理图中引出 LCD_BL、GND、DISP_RST、DISP_RS、SPI_MOSI、SPI_SCK、VDD_3V3 和 DISP_CS；U2 由 LCD_BL_DRV 控制 LCD_BL。

- 参数与网络：`connector=J2`；`backlight_switch=U2 SGM2578 / WS4022C-4/TR`；`spi_mosi=U1 GPIO21`；`spi_sck=U1 GPIO17`；`display_cs=U1 pin21 XTAL_32K_P`；`display_rs=U1 GPIO33`；`display_reset=U1 GPIO34`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 3A-4A，U2 和 J2；网格 2B-C 对应 U1 DISP_CS/LCD_BL_DRV/SPI_SCK/SPI_MOSI/DISP_RS/DISP_RST 网络

## 总线

### ESP32-S3 原生 USB

USB_D_N 连接 U1 GPIO19，USB_D_P 连接 U1 GPIO20，数据线在 Type-C 端分别由 D4 和 D2 ESD5Z3V3 对地防护。

- 参数与网络：`dm_gpio=19`；`dp_gpio=20`；`dm_protection=D4 ESD5Z3V3`；`dp_protection=D2 ESD5Z3V3`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 2B 的 U1 GPIO19/20 与网格 4C 的 USB_D_N/P、D4、D2

## GPIO 与控制信号

### WS2812 RGB LED

U3 WS2812 由 VDD_3V3 供电，DI 接 SK_DIN，SK_DIN 连接 U1 GPIO35；DO 形成未继续连接的 SK_DOUT。

- 参数与网络：`reference=U3`；`data_gpio=35`；`data_net=SK_DIN`；`supply=VDD_3V3`；`daisy_chain_out=SK_DOUT`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 2B U1 GPIO35/SK_DIN 与网格 3B U3 WS2812

### 红外发射 LED

GPIO4 直接驱动 IR 发射 LED，LED 后串联 R16 22Ω 到 GND。

- 参数与网络：`gpio=4`；`reference=IR`；`series_resistor=R16 22Ω`；`return=GND`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 3B，GPIO4、IR LED、R16 22R 和 GND

### 用户按键

S1 按下时将 USER_BUT 拉低，R4 10kΩ 将 USER_BUT 上拉到 VDD_3V3，D1 ESD5Z3V3 对该网络提供防护；USER_BUT 连接 U1 MTDI 引脚 47。

- 参数与网络：`switch=S1`；`net=USER_BUT`；`soc_pin=U1 pin47 MTDI`；`active_level=low`；`pullup=R4 10kΩ`；`protection=D1 ESD5Z3V3`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 2C 的 U1 USER_BUT 与网格 3B-C 的 S1、R4、D1

## 时钟

### ESP32-S3 主时钟

X1 40MHz 晶体连接 U1 XTAL_P/XTAL_N，XTAL_P 一侧串联 L3 24nH，两个晶体端分别配置 C9 10pF 和 C14 12pF 对地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`series_inductor=L3 24nH`；`load_capacitors=C9 10pF, C14 12pF`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1B-2B，X1、L3、C9、C14 与 U1 XTAL_40M_P/N

## 复位

### ESP32-S3 使能与复位

ESP_EN 连接 U1 CHIP_PU，R7 10kΩ 上拉到 VDD_3V3，C23 1uF 接地形成上电延时；S2 按下将 ESP_EN 接地，D3 ESD5Z3V3 提供防护。

- 参数与网络：`soc_pin=U1 CHIP_PU`；`net=ESP_EN`；`pullup=R7 10kΩ`；`capacitor=C23 1uF`；`switch=S2`；`protection=D3 ESD5Z3V3`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 2A U1 CHIP_PU/ESP_EN 与网格 3C-D R7、C23、S2、D3

### GPIO0 下载辅助与指示

U5 GS321 由 VDD_3V3 供电，其输出连接 GPIO0，并由 R9 10kΩ 上拉；同一输出节点通过 LED1 GREEN 和 R15 2kΩ 接 VDD_3V3，输入网络由 ESP_EN、D6、D7、R8、R10、R13、R14 构成。

- 参数与网络：`comparator=U5 GS321`；`output_net=GPIO0`；`output_pullup=R9 10kΩ`；`indicator=LED1 GREEN with R15 2kΩ`；`observed_net=ESP_EN`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 3D，U5 GS321、GPIO0、LED1、D6/D7 与电阻网络

## 内存与 Flash

### ESP32-S3FN8 Flash 供电与未用外部引脚

U1 VDD_SPI 由 FLASH_VCC 供电并配置 C4 1uF 去耦；SPIHD、SPIWP、SPICS0、SPICLK、SPIQ、SPID 在原理图中标记为未连接。

- 参数与网络：`flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`unconnected_pins=SPIHD, SPIWP, SPICS0, SPICLK, SPIQ, SPID`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1A-2B，U1 pin29 VDD_SPI、C4 与 pin30-pin35 未连接标记

## 射频

### 板载天线射频路径

U1 LNA_IN 通过 ESP_LNA、R1 0Ω 和 L1 2.4nH 连接 ANT1 PROANT440，匹配节点配置 C1 2.0pF 和 C2 1.8pF 对地。

- 参数与网络：`antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 0Ω, L1 2.4nH`；`shunt=C1 2.0pF, C2 1.8pF`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1A-2A，ANT1、L1、R1、C1、C2 与 U1 LNA_IN

### 预留 IPEX 射频接口

J1 IPEX 的信号端通过标记 NC 的 R2 接到 ESP_LNA 匹配节点，因此当前装配定义下该外置天线路径与主射频节点隔离。

- 参数与网络：`connector=J1 IPEX`；`selection_resistor=R2 NC`；`rf_net=ESP_LNA`；`default_connected=false`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 1A，J1 IPEX pin1、R2 NC 与 ESP_LNA 节点

## 调试与烧录

### UART0 调试引出

U1 U0TXD 和 U0RXD 分别形成 TX_JP1 与 RX_JP2 测试点网络。

- 参数与网络：`tx=U0TXD -> TX_JP1`；`rx=U0RXD -> RX_JP2`
- 证据：图 5669c9c29e16 / 第 1 页 / 网格 2C，U1 pin49 U0TXD/TX_JP1 与 pin50 U0RXD/RX_JP2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-S3FN8 主控架构 | `reference=U1`；`part_number=ESP32-S3FN8`；`core_supply=VDD_3V3`；`rf_net=ESP_LNA`；`enable_net=ESP_EN` |
| 内存与 Flash | ESP32-S3FN8 Flash 供电与未用外部引脚 | `flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`unconnected_pins=SPIHD, SPIWP, SPICS0, SPICLK, SPIQ, SPID` |
| 时钟 | ESP32-S3 主时钟 | `reference=X1`；`frequency=40MHz`；`series_inductor=L3 24nH`；`load_capacitors=C9 10pF, C14 12pF` |
| 射频 | 板载天线射频路径 | `antenna=ANT1 PROANT440`；`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 0Ω, L1 2.4nH`；`shunt=C1 2.0pF, C2 1.8pF` |
| 射频 | 预留 IPEX 射频接口 | `connector=J1 IPEX`；`selection_resistor=R2 NC`；`rf_net=ESP_LNA`；`default_connected=false` |
| 电源 | USB 5V 输入路径 | `connector=J5`；`fuse=F1 6V/1A/PPTC`；`output_net=VIN_5V`；`input_decoupling=C19 10uF, C20 100nF` |
| 电源 | VDD_3V3 降压电源 | `converter=U4 SY8089`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 2.2uH/1.2A/0806`；`feedback=R11 100kΩ, R12 22.1kΩ` |
| 接口 | USB Type-C 数据与角色配置 | `connector=J5 USB-TYPEC`；`dp_net=USB_D_P`；`dm_net=USB_D_N`；`cc1_pulldown=R5 5.1kΩ`；`cc2_pulldown=R6 5.1kΩ` |
| 总线 | ESP32-S3 原生 USB | `dm_gpio=19`；`dp_gpio=20`；`dm_protection=D4 ESD5Z3V3`；`dp_protection=D2 ESD5Z3V3` |
| GPIO 与控制信号 | WS2812 RGB LED | `reference=U3`；`data_gpio=35`；`data_net=SK_DIN`；`supply=VDD_3V3`；`daisy_chain_out=SK_DOUT` |
| GPIO 与控制信号 | 红外发射 LED | `gpio=4`；`reference=IR`；`series_resistor=R16 22Ω`；`return=GND` |
| GPIO 与控制信号 | 用户按键 | `switch=S1`；`net=USER_BUT`；`soc_pin=U1 pin47 MTDI`；`active_level=low`；`pullup=R4 10kΩ`；`protection=D1 ESD5Z3V3` |
| 复位 | ESP32-S3 使能与复位 | `soc_pin=U1 CHIP_PU`；`net=ESP_EN`；`pullup=R7 10kΩ`；`capacitor=C23 1uF`；`switch=S2`；`protection=D3 ESD5Z3V3` |
| 复位 | GPIO0 下载辅助与指示 | `comparator=U5 GS321`；`output_net=GPIO0`；`output_pullup=R9 10kΩ`；`indicator=LED1 GREEN with R15 2kΩ`；`observed_net=ESP_EN` |
| 接口 | J3 五针扩展排针 | `connector=J3`；`pin1=VDD_3V3`；`pin2=GPIO5`；`pin3=GPIO6`；`pin4=GPIO7`；`pin5=GPIO8` |
| 接口 | J4 四针扩展排针 | `connector=J4`；`pin1=TTL3.3V`；`pin2=GPIO39`；`pin3=GPIO38`；`pin4=VIN_5V` |
| 接口 | J6 GH2.0-4P 扩展接口 | `connector=J6 GH2.0-4P`；`pin1=GPIO1`；`pin2=GPIO2`；`pin3=VIN_5V`；`pin4=GND`；`protection=D5 on GPIO1, D8 on GPIO2` |
| 调试与烧录 | UART0 调试引出 | `tx=U0TXD -> TX_JP1`；`rx=U0RXD -> RX_JP2` |
| 接口 | 原理图中的 SPI 显示连接器 | `connector=J2`；`backlight_switch=U2 SGM2578 / WS4022C-4/TR`；`spi_mosi=U1 GPIO21`；`spi_sck=U1 GPIO17`；`display_cs=U1 pin21 XTAL_32K_P`；`display_rs=U1 GPIO33`；`display_reset=U1 GPIO34` |
| 核心器件 | C124 Lite 的显示电路装配状态 | `references=U2,J2`；`schematic_presence=true`；`assembly_status=null` |

## 待确认事项

- `component.display-population`：原理图画出了 U2 背光开关和 J2 SPI 显示连接器，但图中未给出明确 DNP/NC 装配标记，无法仅凭该原理图确认 C124 AtomS3-Lite 是否实际装配这些器件。（证据：图 5669c9c29e16 / 第 1 页 / 网格 3A-4A，U2 与 J2 均正常绘制且未见 DNP/NC 标注）
- `review.display-population`：C124 AtomS3-Lite 的量产 BOM 中是否装配 U2 和 J2 显示相关器件？；原因：产品定位为 Lite 无屏版本，但共享原理图仍完整画出背光开关和显示连接器，原理图没有给出装配状态。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5669c9c29e1660fe11f49c8e407ac3269586d16bdda798acc319171cd285bd6c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/Sch_M5_AtomS3_v1.0_sch_01.png` |

---

源文档：`zh_CN/core/AtomS3 Lite.md`

源文档 SHA-256：`486ce82562528cb1f16dfcf8e89475132c99fe0a03ccb6b82e89d17a0b10b58d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
