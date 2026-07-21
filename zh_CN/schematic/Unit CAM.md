# Unit CAM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CAM |
| SKU | U109 |
| 产品 ID | `unit-cam-0e7a4ce648c7` |
| 源文档 | `zh_CN/unit/unit_cam.md` |

## 概述

Unit CAM 以 ESP-WROOM-32E（U5）为控制核心，经 U2 24 针摄像头 FPC 连接 8 位像素数据、PCLK/HREF/VSYNC、XCLK、RESET 及 SIO_C/SIO_D 控制信号，并通过 J1 提供 GPIO16/GPIO17 UART。SY8089AAAC（U1）从 +5V 生成 +3V，HX6306P122（U3）和 HX6306P282（U4）分别生成摄像头 +1.2V 与 +2.8V。P1/P2 引出 UART0、EN 和 GPIO0 供外部下载，GPIO4 还连接一颗蓝色 LED。原理图未打印摄像头型号/光学参数、模组 Flash 容量、UART 默认速率或 SCCB 地址。

## 检索关键词

`Unit CAM`、`U109`、`ESP-WROOM-32E`、`ESP32`、`FPC-0.5-24P`、`OV2640`、`2MP`、`SY8089AAAC`、`HX6306P122`、`HX6306P282`、`WPN3012H2R2MT`、`HY-2.0_UART`、`UART 115200 8N1`、`GPIO16`、`GPIO17`、`RXD0`、`TXD0`、`EN`、`GPIO0`、`GPIO4`、`SIO_C`、`SIO_D`、`XCLK`、`PCLK`、`HREF`、`VSYNC`、`RESET`、`PWDN`、`GPIO21`、`GPIO23`、`GPIO25`、`GPIO27`、`+5V`、`+3V`、`+2.8V`、`+1.2V`、`4M Flash`、`blue LED`、`R3 47Ω`、`R4 47Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP-WROOM-32E | 摄像头主控模组，连接并行摄像头、UART、下载接口与蓝色 LED | 图 62b5862e5c19 / 第 1 页 / 页 1 下中 U5 ESP-WROOM-32E，pins 1~39 与 GPIO/EN/TXD0/RXD0/+3V/GND 网络 |
| U2 | FPC-0.5-24P | 24 针摄像头连接器，承载并行像素、同步、时钟、SCCB 控制与三路电源 | 图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 FPC-0.5-24P，pins 1~24 的 Y0~Y9/PCLK/XCLK/HREF/PWDN/VSYNC/RESET/SIO_C/SIO_D/电源 |
| U1 | SY8089AAAC | 将 +5V 降压为 +3V 的开关稳压器 | 图 62b5862e5c19 / 第 1 页 / 页 1 左上 U1 SY8089AAAC、L1、R1/R2 与 C1~C3 的 +5V 到 +3V 电路 |
| U3 | HX6306P122/1.2V LDO 300mA | 从 +5V 生成摄像头 DVDD 使用的 +1.2V | 图 62b5862e5c19 / 第 1 页 / 页 1 左中 U3 HX6306P122/1.2V LDO 300mA，VDD pin 3、VOUT pin 2、GND pin 1 与 C4/C5 |
| U4 | HX6306P282/2.8V LDO 300mA | 从 +5V 生成摄像头 DOVDD/AVDD 使用的 +2.8V | 图 62b5862e5c19 / 第 1 页 / 页 1 中上 U4 HX6306P282/2.8V LDO 300mA，VDD pin 3、VOUT pin 2、GND pin 1 与 C6/C7/C8 |
| J1 | HY-2.0_UART | GPIO16 RX、GPIO17 TX、+5V 和 GND 的外部 UART/Grove 接口 | 图 62b5862e5c19 / 第 1 页 / 页 1 右中 J1 HY-2.0_UART pins 1~4 与 GPIO16/GPIO17/+5V/GND |
| P1 | Header 3 | 引出 RXD0、TXD0 与 +5V 的下载针座 | 图 62b5862e5c19 / 第 1 页 / 页 1 右下 P1 Header 3 pins 1~3 接 RXD0、TXD0、+5V |
| P2 | Header 3 | 引出 EN、GPIO0 与 GND 的下载控制针座 | 图 62b5862e5c19 / 第 1 页 / 页 1 右下 P2 Header 3 pins 1~3 接 EN、GPIO0、GND |
| D1/R7 | 蓝灯 0603 / 1KΩ | 由 U5 GPIO4 控制的 +3V 蓝色 LED 支路 | 图 62b5862e5c19 / 第 1 页 / 页 1 中下 +3V-D1 蓝灯0603-R7 1KΩ-GPIO4/U5 pin 26 支路 |
| L1 | WPN3012H2R2MT | U1 LX 到 +3V 输出的降压电感 | 图 62b5862e5c19 / 第 1 页 / 页 1 左上 L1 WPN3012H2R2MT 位于 U1 LX pin 3 与 +3V 之间 |
| R1/R2 | 40.2KΩ / 10KΩ | SY8089AAAC +3V 输出反馈分压网络 | 图 62b5862e5c19 / 第 1 页 / 页 1 左上 +3V-R1 40.2KΩ-U1 FB pin 5-R2 10KΩ-GND |
| R3/R4 | 47Ω | 摄像头 PCLK 与 XCLK 串联阻尼电阻 | 图 62b5862e5c19 / 第 1 页 / 页 1 右上 GPIO21-R3 47Ω-U2 PCLK pin 17 与 GPIO27-R4 47Ω-U2 XCLK pin 13 |
| R5 | 10KΩ | U2 PWDN pin 8 到 GND 的下拉电阻 | 图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 PWDN pin 8-R5 10KΩ-GND |
| R6/C11 | 10KΩ / 100nF | U5 EN 的 +3V 上拉与对地 RC 复位网络 | 图 62b5862e5c19 / 第 1 页 / 页 1 左下 +3V-R6 10KΩ-EN/U5 pin 3-C11 100nF-GND |
| C1~C10 | 22uF / 1uF / 100nF | +5V、+3V、+1.2V、+2.8V 与 U5 的输入输出去耦和储能 | 图 62b5862e5c19 / 第 1 页 / 页 1 各电源区：C1/C2/C3 22uF，C4/C5/C6/C7 1uF，C8/C9 22uF，C10 100nF |

## 系统结构

### Unit CAM

U5 ESP-WROOM-32E 连接 U2 摄像头 FPC、J1 UART、P1/P2 下载针座和 D1 蓝色 LED；U1/U3/U4 分别生成 +3V、+1.2V、+2.8V。

- 参数与网络：`controller=U5 ESP-WROOM-32E`；`camera_connector=U2 FPC-0.5-24P`；`external_uart=J1 HY-2.0_UART`；`download=P1/P2`；`indicator=D1 GPIO4`；`power=U1 +3V,U3 +1.2V,U4 +2.8V`
- 证据：图 62b5862e5c19 / 第 1 页 / 整页：U1~U5/J1/P1/P2/D1 与全部同名 GPIO、电源和摄像头网络

## 核心器件

### U5 ESP-WROOM-32E 关键引脚

U5 pin 2 接 +3V，pins 1/15/38/39 接 GND，pin 3 接 EN，pins 34/35 接 RXD0/TXD0，pins 27/28 接 GPIO16/GPIO17，pin 25 接 GPIO0，pin 26 接 GPIO4。

- 参数与网络：`supply=pin 2,+3V`；`grounds=pins 1,15,38,39`；`enable=pin 3,EN`；`uart0=pin 34 RXD0,pin 35 TXD0`；`host_uart=pin 27 GPIO16,pin 28 GPIO17`；`boot=pin 25 GPIO0`；`led=pin 26 GPIO4`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 下中 U5 pins 1~39 的电源/GND/EN/RXD0/TXD0/GPIO16/GPIO17/GPIO0/GPIO4

## 电源

### U2 摄像头电源

U2 DOVDD pin 11 与 AVDD pin 4 接 +2.8V，DVDD pin 10 接 +1.2V，DGND pin 15 与 AGND pin 2 接 GND；Y0(AF_GND) pin 24、Y1(AF_VDD) pin 23 和 NC pin 1 未连接。

- 参数与网络：`dovdd=pin 11,+2.8V`；`avdd=pin 4,+2.8V`；`dvdd=pin 10,+1.2V`；`dgnd=pin 15,GND`；`agnd=pin 2,GND`；`unused=pins 24 Y0(AF_GND),23 Y1(AF_VDD),1 NC`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 pins 1/2/4/10/11/15/23/24 与 +2.8V/+1.2V/GND/未连接标记

### U1 +5V 到 +3V 降压

U1 IN pin 4 与 EN pin 1 接 +5V，LX pin 3 经 L1 WPN3012H2R2MT 连接 +3V；FB pin 5 使用 R1 40.2KΩ 与 R2 10KΩ 分压，C1 22uF 位于输入，C2/C3 各 22uF 位于输出。

- 参数与网络：`input=IN.4/EN.1,+5V`；`switch_node=LX.3`；`inductor=L1 WPN3012H2R2MT`；`output=+3V`；`feedback=R1 40.2KΩ,R2 10KΩ`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 左上 +5V/U1/L1/+3V/R1/R2/C1/C2/C3 完整降压区

### U3/U4 摄像头 LDO

U3 HX6306P122 从 +5V 生成 +1.2V，输入/输出分别配置 C4/C5 1uF；U4 HX6306P282 从 +5V 生成 +2.8V，配置 C6/C7 1uF 与 C8 22uF。两器件图面均标 LDO 300mA。

- 参数与网络：`U3=+5V->HX6306P122->+1.2V,300mA`；`U3_caps=C4/C5 1uF`；`U4=+5V->HX6306P282->+2.8V,300mA`；`U4_caps=C6/C7 1uF,C8 22uF`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 左中 U3/U4 与 +5V/+1.2V/+2.8V/C4~C8

### U5 +3V 电源

U5 3V3 pin 2 接 +3V，GND pins 1/15/38/39 接地；C9 22uF 与 C10 100nF 跨接 +3V 和 GND。

- 参数与网络：`supply=U5 pin 2,+3V`；`grounds=U5 pins 1,15,38,39`；`decoupling=C9 22uF,C10 100nF`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 下中 U5 3V3/GND pins 2/1/15/38/39 与 C9/C10

### 电池、充电与电源监测

本页未绘出电池、充电器、负载开关、电量计或电源监测器；三路稳压器也未显示独立外部使能控制。

- 参数与网络：`battery=null`；`charger=null`；`load_switch=null`；`fuel_gauge=null`；`power_monitor=null`；`external_regulator_enable=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 整页电源区域，仅 U1/U3/U4 与阻容电感

## 接口

### J1 HY-2.0_UART

J1 pin 1 标 RX 并接 U5 GPIO16 pin 27，pin 2 标 TX 并接 GPIO17 pin 28，pin 3 标 VCC 并接 +5V，pin 4 接 GND。

- 参数与网络：`pin_1=RX,GPIO16,U5.27`；`pin_2=TX,GPIO17,U5.28`；`pin_3=VCC,+5V`；`pin_4=GND`；`directions=connector labels RX/TX`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右中 J1 pins 1~4 与 U5 GPIO16/GPIO17 同名网络

## 总线

### U2 8 位摄像头像素数据

U2 Y2 pin 19、Y3 pin 21、Y4 pin 22、Y5 pin 20、Y6 pin 18、Y7 pin 16、Y8 pin 14、Y9 pin 12 分别连接 GPIO32、GPIO35、GPIO34、GPIO5、GPIO39、GPIO18、GPIO36、GPIO19。

- 参数与网络：`D0_Y2=U2.19->GPIO32`；`D1_Y3=U2.21->GPIO35`；`D2_Y4=U2.22->GPIO34`；`D3_Y5=U2.20->GPIO5`；`D4_Y6=U2.18->GPIO39`；`D5_Y7=U2.16->GPIO18`；`D6_Y8=U2.14->GPIO36`；`D7_Y9=U2.12->GPIO19`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 pins 12/14/16/18/19/20/21/22 与 GPIO19/36/18/39/32/5/35/34

### 摄像头同步与时钟

U2 PCLK pin 17 经 R3 47Ω 接 U5 GPIO21 pin 33，XCLK pin 13 经 R4 47Ω 接 GPIO27 pin 12，HREF pin 9 接 GPIO26 pin 11，VSYNC pin 7 接 GPIO22 pin 36。

- 参数与网络：`PCLK=U2.17-R3 47Ω-GPIO21/U5.33`；`XCLK=U2.13-R4 47Ω-GPIO27/U5.12`；`HREF=U2.9-GPIO26/U5.11`；`VSYNC=U2.7-GPIO22/U5.36`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 PCLK/XCLK/HREF/VSYNC 与 R3/R4/GPIO21/GPIO27/GPIO26/GPIO22

### 摄像头 SIO_C/SIO_D 控制总线

U2 SIO_C pin 5 连接 U5 GPIO23 pin 37，SIO_D pin 3 连接 U5 GPIO25 pin 10；两线未绘出外部上拉、电平转换或串联器件。

- 参数与网络：`clock=U2.5 SIO_C->GPIO23/U5.37`；`data=U2.3 SIO_D->GPIO25/U5.10`；`pullups=null`；`level_shifter=null`；`series_components=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上/下中 U2 SIO_C/SIO_D 与 U5 GPIO23/GPIO25 同名网络

### J1 UART

J1 RX/TX 分别直接连接 U5 GPIO16/GPIO17，中间未绘出电平转换、串联电阻或保护器件；该 UART 与 U5 RXD0/TXD0 下载串口分开。

- 参数与网络：`rx=J1.1->GPIO16/U5.27`；`tx=J1.2->GPIO17/U5.28`；`level_shifter=null`；`series_resistor=null`；`separate_download_uart=RXD0/TXD0 at P1`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 下中至右中 U5 GPIO16/GPIO17-J1 与 U5 RXD0/TXD0-P1 两组网络

## GPIO 与控制信号

### 摄像头 RESET/PWDN

U2 RESET pin 6 连接 U5 GPIO15 pin 23；PWDN pin 8 经 R5 10KΩ 下拉到 GND，未连接 U5 GPIO。

- 参数与网络：`reset=U2.6->GPIO15/U5.23`；`power_down=U2.8-R5 10KΩ-GND`；`pwdn_controller_gpio=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 RESET/PWDN pins 6/8 与 GPIO15/R5/GND

### D1 蓝色 LED

+3V 经 D1 蓝灯 0603 与 R7 1KΩ 连接 U5 GPIO4 pin 26。

- 参数与网络：`supply=+3V`；`led=D1 蓝灯 0603`；`resistor=R7 1KΩ`；`gpio=GPIO4,U5 pin 26`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 中下 +3V-D1-R7-GPIO4/U5 pin 26

## 时钟

### 摄像头与 ESP 模组时钟

摄像头 XCLK 由 U5 GPIO27 经 R4 47Ω 送往 U2 pin 13，PCLK 从 U2 pin 17 经 R3 47Ω 连接 U5 GPIO21；板级原理图未绘出 U5 外部晶振或振荡器。

- 参数与网络：`camera_xclk=GPIO27-R4 47Ω-U2.13`；`camera_pclk=U2.17-R3 47Ω-GPIO21`；`external_crystal=null`；`external_oscillator=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 XCLK/PCLK 与整页 U5 外围，无晶振位号

## 复位

### U5 EN

U5 EN pin 3 由 R6 10KΩ 上拉到 +3V，并由 C11 100nF 接 GND；EN 同时引至 P2 pin 1。

- 参数与网络：`enable_pin=U5 pin 3 EN`；`pullup=R6 10KΩ to +3V`；`capacitor=C11 100nF to GND`；`header=P2 pin 1`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 左下/右下 +3V-R6-EN-C11-GND 与 P2 EN

## 保护电路

### J1、下载接口与 +5V 保护

本页未绘出 J1/P1/P2 或 +5V 输入的 TVS、ESD 阵列、保险丝、反接保护或过压保护。

- 参数与网络：`uart_esd=null`；`download_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 整页 J1/P1/P2 与 +5V 到 U1/U3/U4 路径，无专用保护器件

## 关键网络

### Unit CAM 关键网络索引

关键路径包括 +5V→U1/U3/U4→+3V/+1.2V/+2.8V，U5→Y2~Y9/PCLK/XCLK/HREF/VSYNC/SIO_C/SIO_D/RESET→U2，GPIO16/17→J1，以及 RXD0/TXD0/EN/GPIO0→P1/P2。

- 参数与网络：`power=+5V-U1/U3/U4-+3V/+1.2V/+2.8V`；`camera_data=GPIO32/35/34/5/39/18/36/19-U2 Y2~Y9`；`camera_control=GPIO21/27/26/22/23/25/15-U2`；`host_uart=GPIO16/17-J1`；`download=RXD0/TXD0/EN/GPIO0-P1/P2`；`indicator=+3V-D1-R7-GPIO4`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 整页全部电源、摄像头、UART、下载和 LED 同名网络

## 存储

### 外部存储连接

本页未绘出 SD 卡、eMMC、独立存储连接器或 SDIO/SPI 存储路径。

- 参数与网络：`sd_card=null`；`emmc=null`；`storage_connector=null`；`sdio=null`；`spi_storage=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 整页，无存储卡/存储芯片或存储接口

## 音频

### 音频链路

本页未绘出麦克风、扬声器、音频编解码器、放大器或 I2S 音频连接。

- 参数与网络：`microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 整页，无音频器件或 I2S 网络

## 射频

### U5 射频部分

本页只显示 ESP-WROOM-32E 模组边界，未展开模组内部射频匹配或天线连接，板上也未绘出外部天线座。

- 参数与网络：`module=U5 ESP-WROOM-32E`；`rf_matching=not expanded`；`antenna_connection=not expanded`；`external_antenna_connector=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 下中 U5 黑盒模组及整页外围，无 RF/ANT 网络或天线连接器

## 调试与烧录

### P1/P2 下载接口

P1 pins 1/2/3 依次接 U5 RXD0 pin 34、TXD0 pin 35、+5V；P2 pins 1/2/3 依次接 EN、GPIO0/U5 pin 25、GND。

- 参数与网络：`P1_pin1=RXD0,U5.34`；`P1_pin2=TXD0,U5.35`；`P1_pin3=+5V`；`P2_pin1=EN,U5.3`；`P2_pin2=GPIO0,U5.25`；`P2_pin3=GND`；`usb_uart_bridge=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右下 P1/P2 Header 3 与 U5 RXD0/TXD0/EN/GPIO0 同名网络

## 模拟电路

### 摄像头模拟电源域

U2 AVDD pin 4 接 +2.8V、AGND pin 2 接 GND；可选 Y0(AF_GND) pin 24 与 Y1(AF_VDD) pin 23 在页面未连接，未绘出其他外部模拟前端。

- 参数与网络：`avdd=U2 pin 4,+2.8V`；`agnd=U2 pin 2,GND`；`af_ground=U2 pin 24 no-connect`；`af_supply=U2 pin 23 no-connect`；`external_analog_front_end=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 AVDD/AGND/Y0(AF_GND)/Y1(AF_VDD) pins 4/2/24/23

## 其他事实

### 程序下载实现

原理图提供 P1/P2 外接下载针座，但未绘出 USB 连接器、USB-UART 桥或自动下载晶体管电路。

- 参数与网络：`download_headers=P1/P2`；`usb_connector=null`；`usb_uart_bridge=null`；`auto_boot_reset=null`
- 证据：图 62b5862e5c19 / 第 1 页 / 页 1 右下 P1/P2 及整页器件，无 USB 或自动下载电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CAM | `controller=U5 ESP-WROOM-32E`；`camera_connector=U2 FPC-0.5-24P`；`external_uart=J1 HY-2.0_UART`；`download=P1/P2`；`indicator=D1 GPIO4`；`power=U1 +3V,U3 +1.2V,U4 +2.8V` |
| 核心器件 | U5 ESP-WROOM-32E 关键引脚 | `supply=pin 2,+3V`；`grounds=pins 1,15,38,39`；`enable=pin 3,EN`；`uart0=pin 34 RXD0,pin 35 TXD0`；`host_uart=pin 27 GPIO16,pin 28 GPIO17`；`boot=pin 25 GPIO0`；`led=pin 26 GPIO4` |
| 总线 | U2 8 位摄像头像素数据 | `D0_Y2=U2.19->GPIO32`；`D1_Y3=U2.21->GPIO35`；`D2_Y4=U2.22->GPIO34`；`D3_Y5=U2.20->GPIO5`；`D4_Y6=U2.18->GPIO39`；`D5_Y7=U2.16->GPIO18`；`D6_Y8=U2.14->GPIO36`；`D7_Y9=U2.12->GPIO19` |
| 总线 | 摄像头同步与时钟 | `PCLK=U2.17-R3 47Ω-GPIO21/U5.33`；`XCLK=U2.13-R4 47Ω-GPIO27/U5.12`；`HREF=U2.9-GPIO26/U5.11`；`VSYNC=U2.7-GPIO22/U5.36` |
| 总线 | 摄像头 SIO_C/SIO_D 控制总线 | `clock=U2.5 SIO_C->GPIO23/U5.37`；`data=U2.3 SIO_D->GPIO25/U5.10`；`pullups=null`；`level_shifter=null`；`series_components=null` |
| 总线地址 | 摄像头 SCCB 地址 | `interface=SIO_C,SIO_D`；`schematic_address=null`；`address_selector=null`；`sensor_model=not printed on schematic` |
| GPIO 与控制信号 | 摄像头 RESET/PWDN | `reset=U2.6->GPIO15/U5.23`；`power_down=U2.8-R5 10KΩ-GND`；`pwdn_controller_gpio=null` |
| 电源 | U2 摄像头电源 | `dovdd=pin 11,+2.8V`；`avdd=pin 4,+2.8V`；`dvdd=pin 10,+1.2V`；`dgnd=pin 15,GND`；`agnd=pin 2,GND`；`unused=pins 24 Y0(AF_GND),23 Y1(AF_VDD),1 NC` |
| 传感器 | U2 所接摄像头 | `schematic_sensor=null`；`product_document_sensor=OV2640`；`product_document_resolution=2MP`；`product_document_frame_rate=12fps`；`product_document_dfov=66.5°`；`output_format=not shown on schematic` |
| 接口 | J1 HY-2.0_UART | `pin_1=RX,GPIO16,U5.27`；`pin_2=TX,GPIO17,U5.28`；`pin_3=VCC,+5V`；`pin_4=GND`；`directions=connector labels RX/TX` |
| 总线 | J1 UART | `rx=J1.1->GPIO16/U5.27`；`tx=J1.2->GPIO17/U5.28`；`level_shifter=null`；`series_resistor=null`；`separate_download_uart=RXD0/TXD0 at P1` |
| 总线 | J1 UART 默认参数 | `schematic_baud=null`；`schematic_frame=null`；`product_document_baud=115200bps`；`product_document_frame=8N1` |
| 调试与烧录 | P1/P2 下载接口 | `P1_pin1=RXD0,U5.34`；`P1_pin2=TXD0,U5.35`；`P1_pin3=+5V`；`P2_pin1=EN,U5.3`；`P2_pin2=GPIO0,U5.25`；`P2_pin3=GND`；`usb_uart_bridge=null` |
| 复位 | U5 EN | `enable_pin=U5 pin 3 EN`；`pullup=R6 10KΩ to +3V`；`capacitor=C11 100nF to GND`；`header=P2 pin 1` |
| GPIO 与控制信号 | D1 蓝色 LED | `supply=+3V`；`led=D1 蓝灯 0603`；`resistor=R7 1KΩ`；`gpio=GPIO4,U5 pin 26` |
| 电源 | U1 +5V 到 +3V 降压 | `input=IN.4/EN.1,+5V`；`switch_node=LX.3`；`inductor=L1 WPN3012H2R2MT`；`output=+3V`；`feedback=R1 40.2KΩ,R2 10KΩ`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF` |
| 电源 | U3/U4 摄像头 LDO | `U3=+5V->HX6306P122->+1.2V,300mA`；`U3_caps=C4/C5 1uF`；`U4=+5V->HX6306P282->+2.8V,300mA`；`U4_caps=C6/C7 1uF,C8 22uF` |
| 电源 | U5 +3V 电源 | `supply=U5 pin 2,+3V`；`grounds=U5 pins 1,15,38,39`；`decoupling=C9 22uF,C10 100nF` |
| 电源 | 电池、充电与电源监测 | `battery=null`；`charger=null`；`load_switch=null`；`fuel_gauge=null`；`power_monitor=null`；`external_regulator_enable=null` |
| 内存与 Flash | U5 Flash 容量 | `module=U5 ESP-WROOM-32E`；`schematic_flash_capacity=null`；`product_document_value=4M`；`external_flash=null` |
| 存储 | 外部存储连接 | `sd_card=null`；`emmc=null`；`storage_connector=null`；`sdio=null`；`spi_storage=null` |
| 时钟 | 摄像头与 ESP 模组时钟 | `camera_xclk=GPIO27-R4 47Ω-U2.13`；`camera_pclk=U2.17-R3 47Ω-GPIO21`；`external_crystal=null`；`external_oscillator=null` |
| 射频 | U5 射频部分 | `module=U5 ESP-WROOM-32E`；`rf_matching=not expanded`；`antenna_connection=not expanded`；`external_antenna_connector=null` |
| 保护电路 | J1、下载接口与 +5V 保护 | `uart_esd=null`；`download_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null` |
| 音频 | 音频链路 | `microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null` |
| 模拟电路 | 摄像头模拟电源域 | `avdd=U2 pin 4,+2.8V`；`agnd=U2 pin 2,GND`；`af_ground=U2 pin 24 no-connect`；`af_supply=U2 pin 23 no-connect`；`external_analog_front_end=null` |
| 其他事实 | 程序下载实现 | `download_headers=P1/P2`；`usb_connector=null`；`usb_uart_bridge=null`；`auto_boot_reset=null` |
| 关键网络 | Unit CAM 关键网络索引 | `power=+5V-U1/U3/U4-+3V/+1.2V/+2.8V`；`camera_data=GPIO32/35/34/5/39/18/36/19-U2 Y2~Y9`；`camera_control=GPIO21/27/26/22/23/25/15-U2`；`host_uart=GPIO16/17-J1`；`download=RXD0/TXD0/EN/GPIO0-P1/P2`；`indicator=+3V-D1-R7-GPIO4` |

## 待确认事项

- `address.camera-sccb-not-shown`：原理图显示 SIO_C/SIO_D 控制连接，但未打印摄像头 SCCB/I2C 地址或地址选择网络。（证据：图 62b5862e5c19 / 第 1 页 / 页 1 U2 SIO_C/SIO_D 与整页标注，无 0x 地址或 ADDR 网络）
- `sensor.camera-model-performance-not-shown`：原理图只显示 U2 FPC-0.5-24P 及电气信号，没有打印图像传感器型号、像素数、输出格式、帧率或视场角。（证据：图 62b5862e5c19 / 第 1 页 / 页 1 右上 U2 仅标 FPC-0.5-24P、针脚和网络，无传感器/镜头料号或性能文字）
- `bus.host-uart-rate-not-shown`：原理图给出 GPIO16/GPIO17 与 RX/TX 连接，但未打印波特率、数据位、停止位或校验方式。（证据：图 62b5862e5c19 / 第 1 页 / 页 1 J1 RX/TX 与 U5 GPIO16/GPIO17 区域，无 baud/8N1/时序文字）
- `memory.flash-capacity-not-shown`：原理图以 ESP-WROOM-32E 黑盒模组表示 U5，没有展开内部 Flash 器件或打印容量。（证据：图 62b5862e5c19 / 第 1 页 / 页 1 下中 U5 ESP-WROOM-32E 模组与整页器件，无 Flash 位号或容量标注）
- `review.camera-sccb-address`：U2 所接摄像头的 SCCB/I2C 地址是什么，是否存在可配置地址机制？；原因：原理图只显示 SIO_C/SIO_D 连接，未打印地址，且传感器型号也未在图面确认。
- `review.camera-model-performance`：U2 当前装配的摄像头是否为 OV2640 2MP，且帧率、输出格式与 66.5° DFOV 是否符合产品正文？；原因：原理图仅提供 24 针 FPC 电气接口，需 BOM、摄像头模组料号或实物确认传感器和镜头规格。
- `review.host-uart-rate`：当前出厂固件的 J1 UART 默认参数是否为 115200bps 8N1？；原因：原理图只确认 RX/TX 引脚映射，串口参数由固件决定且未在图面标注。
- `review.flash-capacity`：U5 当前装配的 ESP-WROOM-32E 变体是否包含产品正文所列的 4M Flash？；原因：板级原理图没有展开模组内部 Flash 或完整订货后缀，需要 BOM、模组料号或固件读取确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `62b5862e5c194b7367270176b87ab08ebe4b791a613665159b89775899c9cc8e` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_sch_01.webp` |

---

源文档：`zh_CN/unit/unit_cam.md`

源文档 SHA-256：`51bfa3b0caf9743133aa28103b2911970252e5d42f9f05f7a9e39da28a461e9b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
