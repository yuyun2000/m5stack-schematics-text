# AtomS3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3 |
| SKU | C123 |
| 产品 ID | `atoms3-183970e4065c` |
| 源文档 | `zh_CN/core/AtomS3.md` |

## 概述

AtomS3 以 U1 ESP32-S3FN8 为核心，配置 40MHz 晶体、PROANT440 板载天线、原生 USB Type-C、WS2812 RGB、GPIO4 红外、用户/复位按键和 SPI LCD 接口。VIN_5V 经 U4 SY8089 生成 VDD_3V3，LCD 背光由 U2 SGM2578/WS4622C-4/TR 控制；J3/J4/J6 引出 GPIO、I2C 与电源。独立 IMU 页使用 TPAP7343D-33FS4 从 VIN_5V 生成 +3.3V，为 U1 MPU-6886 供电，GPIO38/GPIO39 构成 I2C 且页面明确标注 7-bit 地址 0x68。

## 检索关键词

`AtomS3`、`C123`、`ESP32-S3FN8`、`SY8089`、`MPU-6886`、`0x68`、`TPAP7343D-33FS4`、`WS2812`、`SGM2578`、`WS4622C-4/TR`、`GS321`、`PROANT440`、`IPEX`、`40MHz`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`GPIO38 SDA`、`GPIO39 SCL`、`GPIO21 SPI_MOSI`、`GPIO17 SPI_SCK`、`DISP_CS`、`DISP_RS`、`DISP_RST`、`LCD_BL`、`LCD_BL_DRV`、`GPIO35 SK_DIN`、`GPIO4 IR`、`USER_BUT`、`ESP_EN`、`GPIO0`、`GC9107`、`128x128`、`GH2.0-4P`、`ANT1 PROANT440`、`8MB Flash`、`I2C`、`SPI LCD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (main) | ESP32-S3FN8 | 主控 SoC，连接 USB、射频、显示、RGB、红外、按键和扩展 GPIO | 图 5669c9c29e16 / 第 1 页 / 主板页网格 A2-C2：U1 ESP32-S3FN8 全部电源、时钟与 GPIO |
| U4 | SY8089 | VIN_5V 到 VDD_3V3 的降压转换器 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 D1-D2：U4 SY8089、L4、R11/R12 |
| X1 | 40MHz | ESP32-S3 主时钟晶体 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B1：X1 40MHz、L3、C9/C14 |
| ANT1 | PROANT440 | ESP32-S3 板载射频天线 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 A1：ANT1 PROANT440、L1/R1/C1/C2 |
| J1 | IPEX | 经 R2 NC 隔离的预留外置天线接口 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 A1：J1 IPEX 与 R2 NC |
| J5 | USB-TYPEC | 原生 USB 数据与 5V 电源输入 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 C4：J5 USB-TYPEC、CC/DP/DN/F1/ESD |
| U3 | WS2812 | GPIO35 控制的单线 RGB LED | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B3：U3 WS2812、SK_DIN/SK_DOUT |
| IR,R16 | IR LED / 22R | GPIO4 红外发射支路 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B3：GPIO4-IR-R16-GND |
| S1 | SMT_SW_PTS_820 | 低有效 USER_BUT 用户/屏幕按键 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B3-C3：S1 USER_BUT、R4、D1 |
| S2 | SMT_SW_TS_015 | ESP_EN 复位按键 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 C3：S2 ESP_EN、D3 |
| U5 | GS321 | 监测 ESP_EN 并驱动 GPIO0/下载指示的比较器 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 D3：U5 GS321、GPIO0、LED1 |
| U2 (LCD) | SGM2578 / WS4622C-4/TR | LCD_BL_DRV 控制的背光负载开关 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 A3：U2 SGM2578/WS4622C-4/TR |
| J2 | HDGC/0.5K-HX-8PWB | LCD 背光、电源、复位、命令和 SPI 八针接口 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 A4：J2 pins1-8 |
| J3 | THT_Male_P_1x5 | VDD_3V3 与 GPIO5-GPIO8 五针扩展 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B4：J3 pins1-5 |
| J4 (main) | THT_Male_P_1x4 | GPIO39、GPIO38、VIN_5V、GND 的 IMU/扩展接口 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 B4：J4 pins1-4 GPIO39/GPIO38/VIN_5V/GND |
| J6 | GH2.0-4P | GPIO1、GPIO2、VIN_5V、GND 扩展接口 | 图 5669c9c29e16 / 第 1 页 / 主板页网格 D4：J6 与 D5/D8 |
| U1 (IMU) | MPU-6886 | I2C 六轴惯性传感器，地址 0x68 | 图 19d7a8293628 / 第 1 页 / IMU 页网格 B2-C3：U1 MPU-6886 与 I2C Addr(7-bit): 0x68 |
| U2 (IMU) | TPAP7343D-33FS4 | VIN_5V 到 IMU +3.3V 的 LDO | 图 19d7a8293628 / 第 1 页 / IMU 页网格 C2-C3：U2 TPAP7343D-33FS4、VIN/EN/VOUT/GND/EP |
| J4 (IMU) | THT_Male_P_1x4 | SCL/GPIO39、SDA/GPIO38、VIN_5V、GND 接口 | 图 19d7a8293628 / 第 1 页 / IMU 页网格 B1-B2：J4 pins1-4 |

## 系统结构

### AtomS3 系统架构

U1 ESP32-S3FN8 连接射频、40MHz 晶体、原生 USB、SPI LCD、RGB、红外、按键和扩展 GPIO；独立 IMU 页通过 J4 的 GPIO38/GPIO39 和 VIN_5V 连接 MPU-6886。

- 参数与网络：`soc=ESP32-S3FN8`；`display=J2 SPI LCD interface`；`imu=MPU-6886 0x68`；`usb=native USB`；`power=SY8089 main + TPAP7343D-33FS4 IMU`；`antenna=PROANT440`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板完整单页; 图 19d7a8293628 / 第 1 页 / IMU 完整单页

## 电源

### USB 5V 输入

J5 VCC 经 F1 6V/1A/PPTC 形成 VIN_5V，C19 10uF/C20 100nF 去耦后进入 U4。

- 参数与网络：`connector=J5`；`fuse=F1 6V/1A/PPTC`；`rail=VIN_5V`；`caps=C19 10uF; C20 100nF`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页 J5/F1 与 U4 输入

### 主板 VDD_3V3

U4 SY8089 从 VIN_5V 降压，经 L4 2.2uH/1.2A/0806 输出 VDD_3V3，反馈为 R11 100K/1% 与 R12 22.1K/1%。

- 参数与网络：`converter=U4 SY8089`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 2.2uH/1.2A/0806`；`feedback=R11 100K/1%; R12 22.1K/1%`；`output_caps=C21/C22 10uF`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 D1-D2：U4/L4/R11/R12/C21/C22

### LCD 背光开关

U2 VIN 接 VDD_3V3，VOUT 输出 LCD_BL，EN 由 GPIO16 的 LCD_BL_DRV 控制，C3 100nF 从输入接 GND。

- 参数与网络：`switch=U2 SGM2578 / WS4622C-4/TR`；`input=VDD_3V3`；`output=LCD_BL`；`enable=LCD_BL_DRV / GPIO16`；`capacitor=C3 100nF`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 A3：U2/C3/LCD_BL_DRV

### IMU +3.3V LDO

U2 TPAP7343D-33FS4 的 VIN pin4 与 EN pin3 接 VIN_5V，VOUT pin1 输出 +3.3V，GND pin2 与 EP pin5 接地；C5 100nF/C6 22uF 为输入，C7 1uF 为输出电容。

- 参数与网络：`input=VIN_5V`；`ldo=U2 TPAP7343D-33FS4`；`enable=VIN_5V`；`output=+3.3V`；`input_caps=C5 100nF; C6 22uF`；`output_cap=C7 1uF`
- 证据：图 19d7a8293628 / 第 1 页 / IMU 页网格 C2-C3：U2/C5/C6/C7

## 接口

### J2 LCD 接口

J2 pins1-8 为 LCD_BL、GND、DISP_RST、DISP_RS、SPI_MOSI、SPI_SCK、VDD_3V3、DISP_CS；对应 GPIO34、GPIO33、GPIO21、GPIO17 与 U1 pin21 XTAL_32K_P。

- 参数与网络：`pin1=LCD_BL`；`pin2=GND`；`pin3=DISP_RST / GPIO34`；`pin4=DISP_RS / GPIO33`；`pin5=SPI_MOSI / GPIO21`；`pin6=SPI_SCK / GPIO17`；`pin7=VDD_3V3`；`pin8=DISP_CS / U1 pin21 XTAL_32K_P`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 A3-A4：U2/J2 与 U1 显示网络

### GPIO 扩展接口

J3 pins1-5 为 VDD_3V3/GPIO5/GPIO6/GPIO7/GPIO8；J4 pins1-4 为 GPIO39/GPIO38/VIN_5V/GND；J6 pins1-4 为 GPIO1/GPIO2/VIN_5V/GND。

- 参数与网络：`J3=VDD_3V3,GPIO5,GPIO6,GPIO7,GPIO8`；`J4=GPIO39,GPIO38,VIN_5V,GND`；`J6=GPIO1,GPIO2,VIN_5V,GND`；`J6_protection=D5 GPIO1; D8 GPIO2`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 B4/D4：J3/J4/J6

## 总线

### ESP32-S3 原生 USB

J5 DP1/DP2 接 USB_D_P 并连接 U1 GPIO20，DN1/DN2 接 USB_D_N 并连接 GPIO19；R5/R6 5.1KΩ 下拉 CC1/CC2，D2/D4 ESD5Z3V3 保护 D+/D-。

- 参数与网络：`dp=J5 -> USB_D_P -> GPIO20`；`dm=J5 -> USB_D_N -> GPIO19`；`cc=R5/R6 5.1KΩ to GND`；`esd=D2 USB_D_P; D4 USB_D_N`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页 U1 GPIO19/20 与 J5/R5/R6/D2/D4

### 主板与 IMU I2C

J4 pin1 SCL/GPIO39 与 pin2 SDA/GPIO38 连接 MPU-6886，并分别由 R1/R2 10K 上拉到 +3.3V；pin3 为 VIN_5V，pin4 为 GND。

- 参数与网络：`controller=ESP32-S3FN8`；`device=MPU-6886 0x68`；`scl=GPIO39 / J4 pin1`；`sda=GPIO38 / J4 pin2`；`pullups=R1/R2 10K to +3.3V`；`power=J4 pin3 VIN_5V`；`ground=J4 pin4`
- 证据：图 19d7a8293628 / 第 1 页 / IMU 页 J4/R1/R2/U1 I2C 网络

## 总线地址

### MPU-6886 I2C 地址

IMU 页在 U1 下方直接标注 I2C Addr(7-bit): 0x68。

- 参数与网络：`device=U1 MPU-6886`；`address=0x68`；`address_width=7-bit`；`ad0=GND`
- 证据：图 19d7a8293628 / 第 1 页 / IMU 页 U1 下方文字 I2C Addr(7-bit): 0x68

## GPIO 与控制信号

### RGB 与红外输出

U3 WS2812 的 DI=SK_DIN 连接 GPIO35并由 VDD_3V3 供电；GPIO4 驱动 IR LED，后串 R16 22Ω 到 GND。

- 参数与网络：`rgb=GPIO35 -> SK_DIN -> U3 WS2812`；`rgb_out=SK_DOUT`；`ir=GPIO4 -> IR LED -> R16 22Ω -> GND`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 B3：U3/IR/R16 与 U1 GPIO4/GPIO35

### USER_BUT 按键

S1 按下将 USER_BUT 拉低，R4 10K 上拉 VDD_3V3，D1 ESD5Z3V3 对地保护；USER_BUT 连接 U1 MTDI pin47。

- 参数与网络：`switch=S1`；`soc_pin=U1 MTDI pin47`；`active=low`；`pullup=R4 10K`；`esd=D1 ESD5Z3V3`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 B3-C3：S1/R4/D1/USER_BUT

## 时钟

### 40MHz 主时钟

X1 40MHz 连接 U1 XTAL_P/XTAL_N，XTAL_P 串 L3 24nH，C9 10pF 与 C14 12pF 分别接地。

- 参数与网络：`crystal=X1 40MHz`；`pins=U1 XTAL_P pin54; XTAL_N pin53`；`series=L3 24nH`；`loads=C9 10pF; C14 12pF`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 B1：X1/L3/C9/C14

## 复位

### 复位与下载辅助

ESP_EN 由 R7 10K 上拉、C23 1uF 延时，S2 拉低复位并由 D3 防护；U5 GS321 监测 ESP_EN 并驱动 GPIO0 与绿色 LED1。

- 参数与网络：`enable=U1 CHIP_PU / ESP_EN`；`pullup=R7 10K`；`delay=C23 1uF`；`reset_button=S2`；`comparator=U5 GS321`；`boot_output=GPIO0`；`indicator=LED1 GREEN`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 C3-D3：S2/U5/ESP_EN/GPIO0

## 内存与 Flash

### ESP32-S3 Flash 供电

U1 VDD_SPI pin29 由 FLASH_VCC 供电并由 C4 1uF 去耦；SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID pins30-35 标为未连接，页面未画外部 Flash。

- 参数与网络：`flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`external_flash_shown=false`；`unconnected=pins30-35`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页 U1 pin29 与 pins30-35

## 传感器

### MPU-6886 I2C 连接

IMU U1 SCL/SCLK pin23 接 GPIO39，SDA/SDI pin24 接 GPIO38，CS pin22 接 +3.3V，AD0/SDO pin9 与 GND pin18 接地，VDD pin13/VDDIO pin8 接 +3.3V；INT pin12 未连接。

- 参数与网络：`scl=GPIO39`；`sda=GPIO38`；`cs=+3.3V`；`ad0=GND`；`supply=VDD/VDDIO +3.3V`；`interrupt=INT NC`；`decoupling=C1/C4 100nF; C2 10nF; C3 2.2uF`
- 证据：图 19d7a8293628 / 第 1 页 / IMU 页网格 B2-C3：U1 MPU-6886 全部连接

## 射频

### 板载天线与 IPEX 选项

U1 LNA_IN 经 R1 0Ω、L1 2.4nH 接 ANT1 PROANT440，C1 2.0pF/C2 1.8pF 对地；J1 IPEX 经 R2 NC 与射频节点隔离。

- 参数与网络：`onboard=ANT1 PROANT440`；`series=R1 0Ω; L1 2.4nH`；`shunt=C1 2.0pF; C2 1.8pF`；`optional=J1 IPEX via R2 NC`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页网格 A1：ANT1/J1/R1/R2/L1/C1/C2

## 调试与烧录

### UART0 测试点

U1 U0TXD pin49 与 U0RXD pin50 分别形成 TX_JP1 和 RX_JP2 测试点网络。

- 参数与网络：`tx=U0TXD -> TX_JP1`；`rx=U0RXD -> RX_JP2`
- 证据：图 5669c9c29e16 / 第 1 页 / 主板页 U1 pins49/50 TX_JP1/RX_JP2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3 系统架构 | `soc=ESP32-S3FN8`；`display=J2 SPI LCD interface`；`imu=MPU-6886 0x68`；`usb=native USB`；`power=SY8089 main + TPAP7343D-33FS4 IMU`；`antenna=PROANT440` |
| 内存与 Flash | ESP32-S3 Flash 供电 | `flash_supply=FLASH_VCC`；`decoupling=C4 1uF/10V`；`external_flash_shown=false`；`unconnected=pins30-35` |
| 时钟 | 40MHz 主时钟 | `crystal=X1 40MHz`；`pins=U1 XTAL_P pin54; XTAL_N pin53`；`series=L3 24nH`；`loads=C9 10pF; C14 12pF` |
| 射频 | 板载天线与 IPEX 选项 | `onboard=ANT1 PROANT440`；`series=R1 0Ω; L1 2.4nH`；`shunt=C1 2.0pF; C2 1.8pF`；`optional=J1 IPEX via R2 NC` |
| 电源 | USB 5V 输入 | `connector=J5`；`fuse=F1 6V/1A/PPTC`；`rail=VIN_5V`；`caps=C19 10uF; C20 100nF` |
| 电源 | 主板 VDD_3V3 | `converter=U4 SY8089`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 2.2uH/1.2A/0806`；`feedback=R11 100K/1%; R12 22.1K/1%`；`output_caps=C21/C22 10uF` |
| 总线 | ESP32-S3 原生 USB | `dp=J5 -> USB_D_P -> GPIO20`；`dm=J5 -> USB_D_N -> GPIO19`；`cc=R5/R6 5.1KΩ to GND`；`esd=D2 USB_D_P; D4 USB_D_N` |
| 接口 | J2 LCD 接口 | `pin1=LCD_BL`；`pin2=GND`；`pin3=DISP_RST / GPIO34`；`pin4=DISP_RS / GPIO33`；`pin5=SPI_MOSI / GPIO21`；`pin6=SPI_SCK / GPIO17`；`pin7=VDD_3V3`；`pin8=DISP_CS / U1 pin21 XTAL_32K_P` |
| 电源 | LCD 背光开关 | `switch=U2 SGM2578 / WS4622C-4/TR`；`input=VDD_3V3`；`output=LCD_BL`；`enable=LCD_BL_DRV / GPIO16`；`capacitor=C3 100nF` |
| GPIO 与控制信号 | RGB 与红外输出 | `rgb=GPIO35 -> SK_DIN -> U3 WS2812`；`rgb_out=SK_DOUT`；`ir=GPIO4 -> IR LED -> R16 22Ω -> GND` |
| GPIO 与控制信号 | USER_BUT 按键 | `switch=S1`；`soc_pin=U1 MTDI pin47`；`active=low`；`pullup=R4 10K`；`esd=D1 ESD5Z3V3` |
| 复位 | 复位与下载辅助 | `enable=U1 CHIP_PU / ESP_EN`；`pullup=R7 10K`；`delay=C23 1uF`；`reset_button=S2`；`comparator=U5 GS321`；`boot_output=GPIO0`；`indicator=LED1 GREEN` |
| 接口 | GPIO 扩展接口 | `J3=VDD_3V3,GPIO5,GPIO6,GPIO7,GPIO8`；`J4=GPIO39,GPIO38,VIN_5V,GND`；`J6=GPIO1,GPIO2,VIN_5V,GND`；`J6_protection=D5 GPIO1; D8 GPIO2` |
| 传感器 | MPU-6886 I2C 连接 | `scl=GPIO39`；`sda=GPIO38`；`cs=+3.3V`；`ad0=GND`；`supply=VDD/VDDIO +3.3V`；`interrupt=INT NC`；`decoupling=C1/C4 100nF; C2 10nF; C3 2.2uF` |
| 总线地址 | MPU-6886 I2C 地址 | `device=U1 MPU-6886`；`address=0x68`；`address_width=7-bit`；`ad0=GND` |
| 电源 | IMU +3.3V LDO | `input=VIN_5V`；`ldo=U2 TPAP7343D-33FS4`；`enable=VIN_5V`；`output=+3.3V`；`input_caps=C5 100nF; C6 22uF`；`output_cap=C7 1uF` |
| 总线 | 主板与 IMU I2C | `controller=ESP32-S3FN8`；`device=MPU-6886 0x68`；`scl=GPIO39 / J4 pin1`；`sda=GPIO38 / J4 pin2`；`pullups=R1/R2 10K to +3.3V`；`power=J4 pin3 VIN_5V`；`ground=J4 pin4` |
| 调试与烧录 | UART0 测试点 | `tx=U0TXD -> TX_JP1`；`rx=U0RXD -> RX_JP2` |
| 核心器件 | LCD 驱动 IC 与分辨率 | `documented_driver=GC9107`；`documented_resolution=128x128`；`schematic_connector=J2 HDGC/0.5K-HX-8PWB`；`driver_ic_shown=false`；`resolution_shown=false` |
| 内存与 Flash | 8MB Flash 容量 | `soc=ESP32-S3FN8`；`documented_flash=8MB`；`external_flash_shown=false`；`schematic_capacity_text=null` |

## 待确认事项

- `component.display-driver-spec`：产品正文写 GC9107 和 128x128，原理图只画 J2 显示连接器、SPI/控制网络和背光开关，没有显示面板驱动 IC 型号或分辨率标注。（证据：图 5669c9c29e16 / 第 1 页 / 主板页 J2/U2 显示区，未见 GC9107 或分辨率文字）
- `memory.documented-flash-capacity`：产品正文写 8MB Flash，原理图标主控为 ESP32-S3FN8 且未画外部 Flash，但页面没有独立容量字段或存储器 BOM，量产容量需由器件资料确认。（证据：图 5669c9c29e16 / 第 1 页 / 主板页 U1 ESP32-S3FN8、FLASH_VCC 与未用 SPI Flash pins）
- `review.display-driver`：C123 当前 0.85 寸 LCD 的量产驱动 IC 是否为 GC9107，分辨率是否固定为 128x128？；原因：原理图只展示连接器和背光/控制网络，没有面板内部驱动器或分辨率字段。
- `review.flash-capacity`：C123 当前 ESP32-S3FN8 的正式集成 Flash 容量是否为 8MB？；原因：容量来自正文，原理图未打印容量字段或外部存储器料号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5669c9c29e1660fe11f49c8e407ac3269586d16bdda798acc319171cd285bd6c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_M5_AtomS3_v1.0_sch_01.png` |
| 2 | 1 | `19d7a829362883027e72d48eca4523f5412fff772c95b2e2a962204029a24831` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_AtomS3_IMU_sch_01.png` |

---

源文档：`zh_CN/core/AtomS3.md`

源文档 SHA-256：`0dd6ed2d6be26962810d666ade70905b41e426b43820ec9b798485f1235a8930`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
