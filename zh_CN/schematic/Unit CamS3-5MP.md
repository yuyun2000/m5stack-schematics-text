# Unit CamS3-5MP 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CamS3-5MP |
| SKU | U174-B |
| 产品 ID | `unit-cams3-5mp-7f472b7f6963` |
| 源文档 | `zh_CN/unit/Unit-CAMS3 5MP.md` |

## 概述

Unit CamS3-5MP 以 U5 ESP32-S3-WROOM-1-N16R8 为主控，连接 U2 24 针并行摄像头 FPC、U6 TF CARD 和 U7 PDM 麦克风。J1 HY-2.0_UART 将 GPIO19/GPIO20 以 RX/D-、TX/D+ 形式引出，P1/P2 还提供 UART0、GPIO0、EN、SDA/SCL 与电源。+5V 经 U1 SY8089AAAC 生成 +3V，U3/U4 再生成摄像头所需 +1.2V 和 +2.8V。板上还包含 GPIO14 可编程蓝色 LED、EN RC 复位网络、TF 卡 SPI 上拉和摄像头控制/数据串阻。

## 检索关键词

`Unit CamS3-5MP`、`U174-B`、`ESP32-S3-WROOM-1-N16R8`、`ESP32-S3`、`PY260`、`5MP`、`FPC-0.5-24P`、`SY8089AAAC`、`HX6306P122MR`、`XC6206P282MR`、`MSM261DHP006`、`MSM1261D4030HCPM`、`TF CARD`、`microSD`、`HY-2.0_UART`、`RX/D-`、`TX/D+`、`GPIO19`、`GPIO20`、`GPIO0`、`EN`、`SIO_C`、`SIO_D`、`XCLK`、`PCLK`、`VSYNC`、`HREF`、`SPI_CS`、`SPI_MOSI`、`SPI_CLK`、`SPI_MISO`、`MIC_CLK`、`MIC_DATA`、`GPIO14`、`+5V`、`+3V`、`+2.8V`、`+1.2V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-S3-WROOM-1-N16R8 | 主控与无线模组，连接摄像头、TF 卡、PDM 麦克风、LED、USB/UART 和下载排针 | 图 6d038a574215 / 第 1 页 / 网格 B1-C2，U5 ESP32-S3-WROOM-1-N16R8 及 pins 1-41 |
| U2 | FPC-0.5-24P | 24 针摄像头连接器，承载 8 位像素数据、同步、时钟、SCCB、复位和三路电源 | 图 6d038a574215 / 第 1 页 / 网格 A4-B4，U2 FPC-0.5-24P 的 Y2-Y9/PCLK/XCLK/HREF/VSYNC/SIO_C/SIO_D/RESET/PWDN 与电源 |
| U6 | TF CARD | SPI 模式 microSD/TF 卡座 | 图 6d038a574215 / 第 1 页 / 网格 C3，U6 TF CARD 的 DAT2/CD-DAT3/CMD-MOSI/VDD/CLK/VSS/DAT0-MISO/DAT1 |
| U7 | MSM261DHP006 | PDM 数字麦克风，使用 MIC_CLK 和 MIC_DATA | 图 6d038a574215 / 第 1 页 / 网格 D1-D2，U7 MSM261DHP006 的 VDD/L-R/CLK/DATA/GND 引脚 |
| U1,L1 | SY8089AAAC / WPN252012H2R2MT | +5V 至 +3V 降压电源 | 图 6d038a574215 / 第 1 页 / 网格 A1-A2，U1 SY8089AAAC、L1 WPN252012H2R2MT 与 +5V/+3V |
| U3 | HX6306P122MR | +3V 至 +1.2V、300mA 摄像头数字核心 LDO | 图 6d038a574215 / 第 1 页 / 网格 B1-B2，U3 标注 LDO HX6306P122MR 1.2V 300mA SOT23-3 |
| U4 | XC6206P282MR | +3V 至 +2.8V、150mA 摄像头模拟/IO LDO | 图 6d038a574215 / 第 1 页 / 网格 B2，U4 标注 XC6206P282MR/2.8V LDO 150mA |
| J1 | HY-2.0_UART | GPIO19 RX/D-、GPIO20 TX/D+、+5V 和 GND 的四针 Grove 接口 | 图 6d038a574215 / 第 1 页 / 网格 C4-D4，J1 HY-2.0_UART pins 1-4 |
| P1,P2 | Header 4 / Header 4 | UART0、GPIO0、EN、GPIO3/SDA、GPIO8/SCL 与电源下载/调试排针 | 图 6d038a574215 / 第 1 页 / 网格 C3-C4，P1/P2 Header 4 及各脚网络 |
| D1,R7 | Blue 0603 / 1K | GPIO14 控制的可编程蓝色 LED 支路 | 图 6d038a574215 / 第 1 页 / 网格 C2-D2，U5 GPIO14、R7 1K、D1 Blue 0603 与 +3V |
| R6,C11 | 10KΩ / 100nF | ESP32-S3 EN 的 +3V 上拉与对地 RC 复位网络 | 图 6d038a574215 / 第 1 页 / 网格 B1，R6 10KΩ、EN、C11 100nF 与 +3V/GND |

## 系统结构

### Unit CamS3-5MP 系统架构

U5 ESP32-S3-WROOM-1-N16R8 连接 U2 并行摄像头 FPC、U6 TF 卡、U7 PDM 麦克风、D1 LED、J1 Grove 和 P1/P2 下载排针；U1/U3/U4 从 +5V 生成 +3V、+1.2V、+2.8V。

- 参数与网络：`controller=U5 ESP32-S3-WROOM-1-N16R8`；`camera=U2 FPC-0.5-24P`；`storage=U6 TF CARD`；`audio=U7 MSM261DHP006`；`host_interface=J1 HY-2.0_UART`；`power_tree=+5V -> +3V -> +1.2V/+2.8V`
- 证据：图 6d038a574215 / 第 1 页 / 第 1 页完整原理图，电源、U5、摄像头、TF、麦克风、LED 和接口分区

## 核心器件

### U5 ESP32-S3 外部 GPIO

U5 左侧 pins 4-14 为 GPIO4、5、6、7、15、16、17、18、8、19、20；底部 pins 15-26 为 GPIO3、46、9、10、11、12、13、14、21、47、48、45；右侧 pins 27、31-39 为 GPIO0、38、39、40、41、42、RXD0、TXD0、GPIO2、GPIO1，pins 28-30 GPIO35/36/37 标记未连接。

- 参数与网络：`left_pins=4 GPIO4;5 GPIO5;6 GPIO6;7 GPIO7;8 GPIO15;9 GPIO16;10 GPIO17;11 GPIO18;12 GPIO8;13 GPIO19;14 GPIO20`；`bottom_pins=15 GPIO3;16 GPIO46;17 GPIO9;18 GPIO10;19 GPIO11;20 GPIO12;21 GPIO13;22 GPIO14;23 GPIO21;24 GPIO47;25 GPIO48;26 GPIO45`；`right_pins=27 GPIO0;31 GPIO38;32 GPIO39;33 GPIO40;34 GPIO41;35 GPIO42;36 RXD0;37 TXD0;38 GPIO2;39 GPIO1`；`nc_pins=28 GPIO35,29 GPIO36,30 GPIO37`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B1-C2，U5 pins 4-39 与蓝/红网络标注

## 电源

### +5V 至 +3V 降压

+5V 连接 U1 SY8089AAAC IN pin 4 和 EN pin 1，LX pin 3 经 L1 WPN252012H2R2MT 输出 +3V；FB pin 5 使用 R1 43KΩ、R2 10KΩ 分压和 C12 22pF 补偿。

- 参数与网络：`converter=U1 SY8089AAAC`；`input=+5V -> IN pin 4`；`enable=+5V -> EN pin 1`；`switch_node=LX pin 3 -> L1 WPN252012H2R2MT`；`output=+3V`；`feedback=R1 43K,R2 10K,C12 22pF`
- 证据：图 6d038a574215 / 第 1 页 / 网格 A1-A2，+5V/U1/L1/R1/R2/C12/+3V

### +5V 与 +3V 滤波及 U5 供电

U1 输入侧 C1 22uF 接地，+3V 输出侧 C2、C3 各 22uF 接地；U5 3V3 pin 2 接 +3V，旁路 C10 100nF 对地，U5 GND pins 1、40、41 接 GND。

- 参数与网络：`input_capacitor=C1 22uF`；`output_capacitors=C2 22uF,C3 22uF`；`module_supply=U5 pin 2 3V3 -> +3V`；`module_decoupling=C10 100nF`；`module_ground_pins=1,40,41`
- 证据：图 6d038a574215 / 第 1 页 / 网格 A1-A2 的 C1-C3 与网格 B1-C3 的 U5 pin 2/C10/GND pins

### 摄像头 +1.2V 电源

U3 HX6306P122MR 从 +3V 生成 +1.2V，标称 300mA；输入 C4 22uF、输出 C5 47uF 均接地，+1.2V 连接 U2 DVDD pin 10。

- 参数与网络：`regulator=U3 HX6306P122MR`；`input=+3V`；`output=+1.2V`；`rated_current_ma=300`；`input_capacitor=C4 22uF`；`output_capacitor=C5 47uF`；`camera_pin=U2 pin 10 DVDD`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B1-B2 U3/C4/C5 与网格 B4 U2 DVDD pin 10

### 摄像头 +2.8V 电源

U4 XC6206P282MR 从 +3V 生成 +2.8V，标称 150mA；输入 C6 47uF，输出 C7 100nF、C8 47uF 接地，+2.8V 连接 U2 DOVDD pin 11 与 AVDD pin 4。

- 参数与网络：`regulator=U4 XC6206P282MR`；`input=+3V`；`output=+2.8V`；`rated_current_ma=150`；`input_capacitor=C6 47uF`；`output_capacitors=C7 100nF,C8 47uF`；`camera_pins=U2 pin 11 DOVDD,pin 4 AVDD`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B2 U4/C6-C8 与网格 B4 U2 DOVDD/AVDD

### U2 摄像头供电与地

U2 AVDD pin 4 与 DOVDD pin 11 接 +2.8V，DVDD pin 10 接 +1.2V，AGND pin 2 与 DGND pin 15 接 GND；pin 1 标 NC。

- 参数与网络：`avdd=pin 4 +2.8V`；`dovdd=pin 11 +2.8V`；`dvdd=pin 10 +1.2V`；`grounds=pin 2 AGND,pin 15 DGND`；`nc=pin 1`
- 证据：图 6d038a574215 / 第 1 页 / 网格 A4-B4，U2 AVDD/DOVDD/DVDD/AGND/DGND/NC

## 接口

### J1 Grove USB/UART 接口

J1 pin 1 RX/D- 连接 GPIO19，pin 2 TX/D+ 连接 GPIO20，pin 3 VCC 连接 +5V，pin 4 GND 接地；信号从 U5 到 J1 之间未画串联电阻、ESD 或电平转换器。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pinout=1:GPIO19/RX/D-,2:GPIO20/TX/D+,3:+5V,4:GND`；`signal_paths=direct`；`external_protection=null`
- 证据：图 6d038a574215 / 第 1 页 / 网格 C4-D4，U5 GPIO19/GPIO20 同名网络与 J1 pins 1-4

## 总线

### U2 摄像头并行像素数据

U2 Y2、Y3、Y4、Y5、Y6、Y7、Y8、Y9 分别连接 U5 GPIO6、GPIO15、GPIO16、GPIO7、GPIO5、GPIO10、GPIO4、GPIO13，构成 8 位像素数据总线。

- 参数与网络：`mapping=Y2:GPIO6,Y3:GPIO15,Y4:GPIO16,Y5:GPIO7,Y6:GPIO5,Y7:GPIO10,Y8:GPIO4,Y9:GPIO13`；`width_bits=8`；`connector=U2 FPC-0.5-24P`
- 证据：图 6d038a574215 / 第 1 页 / 网格 A4-B4，U2 Y2-Y9 左侧 GPIO 网络与 U5 同名 GPIO

### 摄像头时钟与同步

U2 PCLK pin 17 经 R3 47Ω 连接 GPIO12，XCLK pin 13 经 R4 47Ω 连接 GPIO11，HREF pin 9 连接 GPIO18，VSYNC pin 7 连接 GPIO42。

- 参数与网络：`pclk=U2 pin 17 -> R3 47R -> GPIO12`；`xclk=GPIO11 -> R4 47R -> U2 pin 13`；`href=U2 pin 9 -> GPIO18`；`vsync=U2 pin 7 -> GPIO42`
- 证据：图 6d038a574215 / 第 1 页 / 网格 A4-B4，U2 PCLK/XCLK/HREF/VSYNC、R3/R4 与 GPIO 网络

### 摄像头 SCCB 与控制

U2 SIO_C pin 5 连接 GPIO41，SIO_D pin 3 连接 GPIO17，RESET pin 6 连接 GPIO21；PWDN pin 8 通过 R5 10KΩ 接 GND。

- 参数与网络：`sccb_clock=U2 pin 5 SIO_C -> GPIO41`；`sccb_data=U2 pin 3 SIO_D -> GPIO17`；`reset=U2 pin 6 RESET -> GPIO21`；`power_down=U2 pin 8 PWDN -> R5 10K -> GND`；`address=null`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B4，U2 SIO_C/SIO_D/RESET/PWDN、R5 与 GPIO/GND

## GPIO 与控制信号

### GPIO0 下载模式

U5 GPIO0 pin 27 直接引出到 P2 pin 3，本页未绘制 BOOT 按键或固定上拉/下拉电阻。

- 参数与网络：`module_pin=U5 pin 27 GPIO0`；`header_pin=P2 pin 3`；`boot_button=false`；`external_strap=null`
- 证据：图 6d038a574215 / 第 1 页 / 网格 C2-C4，U5 GPIO0 网络至 P2 pin 3

### D1 可编程蓝色 LED

U5 GPIO14 pin 22 通过 R7 1KΩ 和 D1 Blue 0603 串联到 +3V。

- 参数与网络：`controller_pin=U5 pin 22 GPIO14`；`resistor=R7 1K`；`led=D1 Blue 0603`；`rail=+3V`
- 证据：图 6d038a574215 / 第 1 页 / 网格 C2-D2，GPIO14、R7、D1 与 +3V

## 时钟

### 板级时钟

本页未绘制 ESP32-S3 外部晶振；摄像头 XCLK 由 U5 GPIO11 经 R4 47Ω 输出，PCLK 由摄像头经 R3 47Ω 输入 GPIO12。

- 参数与网络：`external_mcu_crystal=false`；`camera_xclk=GPIO11 -> R4 47R -> U2 pin 13`；`camera_pclk=U2 pin 17 -> R3 47R -> GPIO12`；`frequencies=null`
- 证据：图 6d038a574215 / 第 1 页 / 第 1 页全部时钟相关器件；仅见 U2 XCLK/PCLK 和 SPI_CLK/MIC_CLK 网络，无独立晶振

## 复位

### U5 EN 复位网络

U5 EN pin 3 由 R6 10KΩ 上拉到 +3V，并由 C11 100nF 接地；EN 还引出至 P2 pin 2。

- 参数与网络：`module_pin=U5 pin 3 EN`；`pullup=R6 10K to +3V`；`capacitor=C11 100nF to GND`；`header_pin=P2 pin 2`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B1 的 R6/C11/EN 与网格 C4 的 P2 pin 2

## 保护电路

### 外部接口保护

本页未显示 J1、P1/P2、TF 卡或摄像头接口的 TVS/ESD、保险丝、反接保护或负载开关；仅显示信号串阻、上拉、滤波和电源去耦。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`camera_series_resistors=R3,R4 47R`；`tf_pullups=R8-R11 10K`
- 证据：图 6d038a574215 / 第 1 页 / 第 1 页完整原理图的 J1、P1/P2、U2、U6 和电源输入区域

## 存储

### U6 TF 卡 SPI 映射

U6 CD/DAT3 pin 2 作为 SPI_CS 连接 U5 GPIO9，CMD/MOSI pin 3 作为 SPI_MOSI 连接 GPIO38，CLK pin 5 作为 SPI_CLK 连接 GPIO39，DAT0/MISO pin 7 作为 SPI_MISO 连接 GPIO40；VDD pin 4 接 +3V，VSS pin 6 接 GND。

- 参数与网络：`chip_select=U6 pin 2 SPI_CS -> GPIO9`；`mosi=U6 pin 3 SPI_MOSI -> GPIO38`；`clock=U6 pin 5 SPI_CLK -> GPIO39`；`miso=U6 pin 7 SPI_MISO -> GPIO40`；`supply=pin 4 +3V`；`ground=pin 6 GND`；`bus=SPI`
- 证据：图 6d038a574215 / 第 1 页 / 网格 C3，U6 TF CARD 与 SPI_CS/MOSI/CLK/MISO/+3V/GND

### TF 卡上拉与接地

R11、R10、R9、R8 均为 10KΩ 并上拉到 +3V，分别服务 DAT2、SPI_CS/CD-DAT3、SPI_MOSI/CMD 和 SPI_MISO/DAT0；U6 pins 8-10 接 GND。

- 参数与网络：`pullups=R11 DAT2,R10 SPI_CS,R9 SPI_MOSI,R8 SPI_MISO`；`resistance_ohm=10000`；`rail=+3V`；`grounded_pins=U6 pins 8,9,10`
- 证据：图 6d038a574215 / 第 1 页 / 网格 B3-C3，R8-R11 10KΩ、+3V 与 U6 DAT2/DAT3/CMD/DAT0 和 pins 8-10

## 音频

### U7 PDM 麦克风

U7 原理图型号为 MSM261DHP006；VDD pin 1 接 +3V 并由 C9 1uF 对地去耦，L/R pin 2 接 GND，CLK pin 3 通过 MIC_CLK 连接 U5 GPIO47，DATA pin 4 通过 MIC_DATA 连接 GPIO48，pins 5-8 接 GND。

- 参数与网络：`reference=U7`；`part_number=MSM261DHP006`；`supply=pin 1 +3V`；`decoupling=C9 1uF`；`channel_select=pin 2 L/R -> GND`；`clock=pin 3 MIC_CLK -> GPIO47`；`data=pin 4 MIC_DATA -> GPIO48`；`ground_pins=5,6,7,8`
- 证据：图 6d038a574215 / 第 1 页 / 网格 D1-D2，U7 MSM261DHP006、C9、MIC_CLK/MIC_DATA、+3V/GND

## 调试与烧录

### P1/P2 下载与调试排针

P1 pins 1-4 分别为 GPIO3/SDA、RXD0、TXD0、+5V；P2 pins 1-4 分别为 GPIO8/SCL、EN、GPIO0、GND。

- 参数与网络：`P1=1:GPIO3/SDA,2:RXD0,3:TXD0,4:+5V`；`P2=1:GPIO8/SCL,2:EN,3:GPIO0,4:GND`；`uart0=U5 pin 36 RXD0,pin 37 TXD0`；`boot_pin=U5 pin 27 GPIO0`
- 证据：图 6d038a574215 / 第 1 页 / 网格 C3-C4，P1/P2 Header 4 与 U5 RXD0/TXD0/GPIO0/EN 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CamS3-5MP 系统架构 | `controller=U5 ESP32-S3-WROOM-1-N16R8`；`camera=U2 FPC-0.5-24P`；`storage=U6 TF CARD`；`audio=U7 MSM261DHP006`；`host_interface=J1 HY-2.0_UART`；`power_tree=+5V -> +3V -> +1.2V/+2.8V` |
| 核心器件 | U5 ESP32-S3 外部 GPIO | `left_pins=4 GPIO4;5 GPIO5;6 GPIO6;7 GPIO7;8 GPIO15;9 GPIO16;10 GPIO17;11 GPIO18;12 GPIO8;13 GPIO19;14 GPIO20`；`bottom_pins=15 GPIO3;16 GPIO46;17 GPIO9;18 GPIO10;19 GPIO11;20 GPIO12;21 GPIO13;22 GPIO14;23 GPIO21;24 GPIO47;25 GPIO48;26 GPIO45`；`right_pins=27 GPIO0;31 GPIO38;32 GPIO39;33 GPIO40;34 GPIO41;35 GPIO42;36 RXD0;37 TXD0;38 GPIO2;39 GPIO1`；`nc_pins=28 GPIO35,29 GPIO36,30 GPIO37` |
| 电源 | +5V 至 +3V 降压 | `converter=U1 SY8089AAAC`；`input=+5V -> IN pin 4`；`enable=+5V -> EN pin 1`；`switch_node=LX pin 3 -> L1 WPN252012H2R2MT`；`output=+3V`；`feedback=R1 43K,R2 10K,C12 22pF` |
| 电源 | +5V 与 +3V 滤波及 U5 供电 | `input_capacitor=C1 22uF`；`output_capacitors=C2 22uF,C3 22uF`；`module_supply=U5 pin 2 3V3 -> +3V`；`module_decoupling=C10 100nF`；`module_ground_pins=1,40,41` |
| 电源 | 摄像头 +1.2V 电源 | `regulator=U3 HX6306P122MR`；`input=+3V`；`output=+1.2V`；`rated_current_ma=300`；`input_capacitor=C4 22uF`；`output_capacitor=C5 47uF`；`camera_pin=U2 pin 10 DVDD` |
| 电源 | 摄像头 +2.8V 电源 | `regulator=U4 XC6206P282MR`；`input=+3V`；`output=+2.8V`；`rated_current_ma=150`；`input_capacitor=C6 47uF`；`output_capacitors=C7 100nF,C8 47uF`；`camera_pins=U2 pin 11 DOVDD,pin 4 AVDD` |
| 接口 | J1 Grove USB/UART 接口 | `connector=J1 HY-2.0_UART`；`pinout=1:GPIO19/RX/D-,2:GPIO20/TX/D+,3:+5V,4:GND`；`signal_paths=direct`；`external_protection=null` |
| 调试与烧录 | P1/P2 下载与调试排针 | `P1=1:GPIO3/SDA,2:RXD0,3:TXD0,4:+5V`；`P2=1:GPIO8/SCL,2:EN,3:GPIO0,4:GND`；`uart0=U5 pin 36 RXD0,pin 37 TXD0`；`boot_pin=U5 pin 27 GPIO0` |
| 复位 | U5 EN 复位网络 | `module_pin=U5 pin 3 EN`；`pullup=R6 10K to +3V`；`capacitor=C11 100nF to GND`；`header_pin=P2 pin 2` |
| GPIO 与控制信号 | GPIO0 下载模式 | `module_pin=U5 pin 27 GPIO0`；`header_pin=P2 pin 3`；`boot_button=false`；`external_strap=null` |
| 总线 | U2 摄像头并行像素数据 | `mapping=Y2:GPIO6,Y3:GPIO15,Y4:GPIO16,Y5:GPIO7,Y6:GPIO5,Y7:GPIO10,Y8:GPIO4,Y9:GPIO13`；`width_bits=8`；`connector=U2 FPC-0.5-24P` |
| 总线 | 摄像头时钟与同步 | `pclk=U2 pin 17 -> R3 47R -> GPIO12`；`xclk=GPIO11 -> R4 47R -> U2 pin 13`；`href=U2 pin 9 -> GPIO18`；`vsync=U2 pin 7 -> GPIO42` |
| 总线 | 摄像头 SCCB 与控制 | `sccb_clock=U2 pin 5 SIO_C -> GPIO41`；`sccb_data=U2 pin 3 SIO_D -> GPIO17`；`reset=U2 pin 6 RESET -> GPIO21`；`power_down=U2 pin 8 PWDN -> R5 10K -> GND`；`address=null` |
| 电源 | U2 摄像头供电与地 | `avdd=pin 4 +2.8V`；`dovdd=pin 11 +2.8V`；`dvdd=pin 10 +1.2V`；`grounds=pin 2 AGND,pin 15 DGND`；`nc=pin 1` |
| 存储 | U6 TF 卡 SPI 映射 | `chip_select=U6 pin 2 SPI_CS -> GPIO9`；`mosi=U6 pin 3 SPI_MOSI -> GPIO38`；`clock=U6 pin 5 SPI_CLK -> GPIO39`；`miso=U6 pin 7 SPI_MISO -> GPIO40`；`supply=pin 4 +3V`；`ground=pin 6 GND`；`bus=SPI` |
| 存储 | TF 卡上拉与接地 | `pullups=R11 DAT2,R10 SPI_CS,R9 SPI_MOSI,R8 SPI_MISO`；`resistance_ohm=10000`；`rail=+3V`；`grounded_pins=U6 pins 8,9,10` |
| 音频 | U7 PDM 麦克风 | `reference=U7`；`part_number=MSM261DHP006`；`supply=pin 1 +3V`；`decoupling=C9 1uF`；`channel_select=pin 2 L/R -> GND`；`clock=pin 3 MIC_CLK -> GPIO47`；`data=pin 4 MIC_DATA -> GPIO48`；`ground_pins=5,6,7,8` |
| GPIO 与控制信号 | D1 可编程蓝色 LED | `controller_pin=U5 pin 22 GPIO14`；`resistor=R7 1K`；`led=D1 Blue 0603`；`rail=+3V` |
| 时钟 | 板级时钟 | `external_mcu_crystal=false`；`camera_xclk=GPIO11 -> R4 47R -> U2 pin 13`；`camera_pclk=U2 pin 17 -> R3 47R -> GPIO12`；`frequencies=null` |
| 保护电路 | 外部接口保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`load_switch_visible=false`；`camera_series_resistors=R3,R4 47R`；`tf_pullups=R8-R11 10K` |
| 内存与 Flash | ESP32-S3 模组 Flash 与 PSRAM 容量 | `schematic_module=ESP32-S3-WROOM-1-N16R8`；`documented_flash_mb=16`；`documented_psram_mb=8`；`external_memory_components=null` |
| 传感器 | 摄像头型号与光学性能 | `documented_sensor=PY260`；`documented_megapixels=5`；`documented_max_resolution=2592x1944`；`documented_dfov_deg=88`；`documented_fixed_focus_m=0.6`；`documented_output=JPEG`；`schematic_sensor_model=null` |
| 音频 | 麦克风型号差异 | `schematic_part_number=MSM261DHP006`；`documented_part_number=MSM1261D4030HCPM`；`interface=PDM`；`clock_gpio=GPIO47`；`data_gpio=GPIO48` |

## 待确认事项

- `memory.documented-capacity`：原理图确认 U5 型号为 ESP32-S3-WROOM-1-N16R8，但没有展开内部存储器或直接标注容量；产品正文所列 16MB Flash 和 8MB PSRAM 需由模组资料或 BOM 复核。（证据：图 6d038a574215 / 第 1 页 / 网格 B1-C2，U5 仅标 ESP32-S3-WROOM-1-N16R8，未展开 Flash/PSRAM）
- `sensor.documented-camera`：产品正文称摄像头为 PY260、5MP、最高 2592x1944、88° DFoV、0.6m 固定焦距并支持 JPEG；原理图只显示 U2 FPC-0.5-24P 接口和电气信号，没有传感器型号、分辨率、镜头或输出格式。（证据：图 6d038a574215 / 第 1 页 / 网格 A4-B4，U2 器件值仅为 FPC-0.5-24P）
- `audio.documented-microphone-model`：原理图将 U7 标为 MSM261DHP006，而产品正文规格表写 MSM1261D4030HCPM；两者文本不一致，当前量产麦克风型号需由 BOM 或实物确认。（证据：图 6d038a574215 / 第 1 页 / 网格 D1-D2，U7 下方明确标注 MSM261DHP006）
- `review.memory-capacity`：请用当前 U5 模组 BOM 或 ESP32-S3-WROOM-1-N16R8 资料确认 16MB Flash 与 8MB PSRAM。；原因：板级原理图只给出模组订货型号，没有展开或标注内部存储容量。
- `review.camera-specification`：请用当前摄像头 BOM、模组丝印或规格书确认 PY260、5MP、2592x1944、88° DFoV、0.6m 焦距和 JPEG 支持。；原因：原理图只画出通用 24 针 FPC 电气接口，没有摄像头传感器和镜头料号。
- `review.microphone-model`：当前量产 U7 是原理图所示 MSM261DHP006，还是正文所列 MSM1261D4030HCPM？；原因：原理图与产品正文的麦克风型号直接冲突，应以当前版本 BOM 或实物为准。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6d038a57421555617a6e921e34227f68dbaae10a8a25f5e04b8335089d89a9ef` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/SCH_UNIT_CAMS3_V1.0_page_01.png` |

---

源文档：`zh_CN/unit/Unit-CAMS3 5MP.md`

源文档 SHA-256：`e1d4f88d5625215c123bcc04be557345e0e25015e00b3eed26bc39dd28fc7ff9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
