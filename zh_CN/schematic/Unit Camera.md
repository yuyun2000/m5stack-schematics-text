# Unit Camera 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Camera |
| SKU | U109-B |
| 产品 ID | `unit-camera-5eca3cc8e61e` |
| 源文档 | `zh_CN/unit/Unit Camera.md` |

## 概述

Unit Camera 以 ESP-WROOM-32E（U5）为主控，连接 24 Pin 摄像头 FPC（U2）、GPIO16/GPIO17 UART 接口、外接下载针座和 GPIO4 蓝色 LED。摄像头使用 8 位并行数据、PCLK/HREF/VSYNC、XCLK 与 SIO_C/SIO_D 控制信号。SY8089AAAC（U1）将 +5V 降压为 +3V，U3/U4 再分别生成 +1.2V 与 +2.8V，为 ESP 模组和摄像头三路电源供电。原理图不含 USB 下载桥、外部时钟或分立存储器。

## 检索关键词

`Unit Camera`、`U109-B`、`ESP-WROOM-32E`、`ESP32`、`OV2640`、`FPC0.5-24P`、`SY8089AAAC`、`HX6306P122`、`HX6306P282`、`GPIO16`、`GPIO17`、`RX`、`TX`、`RXD0`、`TXD0`、`EN`、`GPIO0`、`GPIO4`、`GPIO23`、`GPIO25`、`GPIO27`、`GPIO21`、`GPIO22`、`GPIO26`、`XCLK`、`PCLK`、`VSYNC`、`HREF`、`SIO_C`、`SIO_D`、`+5V`、`+3V`、`+1.2V`、`+2.8V`、`HY-2.0_UART`、`4MB Flash`、`2MP`、`65° DFOV`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP-WROOM-32E | Wi-Fi 摄像头主控模组，连接相机、UART、下载接口、复位/启动和蓝色 LED | 图 62b5862e5c19 / 第 1 页 / 页面下中：U5 标注 ESP-WROOM-32E，GPIO/EN/TXD0/RXD0/电源/GND 引脚 |
| U2 | FPC0.5-24P | 24 Pin 摄像头 FPC，连接并行像素数据、同步、时钟、控制和多路电源 | 图 62b5862e5c19 / 第 1 页 / 页面右上：U2 FPC0.5-24P，Y0~Y9/PCLK/XCLK/HREF/PWDN/VSYNC/RESET/SIO_C/SIO_D 与电源脚 |
| U1 | SY8089AAAC | 将 +5V 降压为 +3V 的开关稳压器 | 图 62b5862e5c19 / 第 1 页 / 页面左上：U1 SY8089AAAC、L1、R1/R2、C1~C3 的 +5V 到 +3V 电路 |
| U3 | HX6306P122/1.2V LDO 300mA | 从 +5V 生成 +1.2V 摄像头 DVDD | 图 62b5862e5c19 / 第 1 页 / 页面左中：U3 HX6306P122/1.2V LDO 300mA 与 C4/C5 |
| U4 | HX6306P282/2.8V LDO 300mA | 从 +5V 生成 +2.8V 摄像头 DOVDD/AVDD | 图 62b5862e5c19 / 第 1 页 / 页面中部：U4 HX6306P282/2.8V LDO 300mA 与 C6/C7/C8 |
| J1 | HY-2.0_UART | GPIO16 RX、GPIO17 TX、+5V、GND UART 与供电接口 | 图 62b5862e5c19 / 第 1 页 / 页面右中：J1 HY-2.0_UART，1~4 脚 RX/TX/VCC/GND 与 GPIO16/GPIO17/+5V/GND |
| P1 | Header 3 | ESP32 RXD0、TXD0 与 +5V 下载接口针座 | 图 62b5862e5c19 / 第 1 页 / 页面右下：P1 Header3 的 RXD0、TXD0、+5V |
| P2 | Header 3 | ESP32 EN、GPIO0 与 GND 下载控制针座 | 图 62b5862e5c19 / 第 1 页 / 页面右下：P2 Header3 的 EN、GPIO0、GND |
| D1 | 蓝灯 0603 | 由 GPIO4 驱动的蓝色 LED | 图 62b5862e5c19 / 第 1 页 / 页面中下偏右：+3V-D1(蓝灯 0603)-R7(1KΩ)-GPIO4 支路 |
| L1 | WPN3012H2R2MT | SY8089AAAC 降压输出电感 | 图 62b5862e5c19 / 第 1 页 / 页面左上：L1 WPN3012H2R2MT 连接 U1.LX 与 +3V |
| R3, R4 | 47Ω | 摄像头 PCLK 与 XCLK 串联阻尼电阻 | 图 62b5862e5c19 / 第 1 页 / 页面右上：GPIO21-R3(47Ω)-U2.PCLK 与 GPIO27-R4(47Ω)-U2.XCLK |
| R6, C11 | 10KΩ / 100nF | U5 EN 的 +3V 上拉与对地 RC 复位网络 | 图 62b5862e5c19 / 第 1 页 / 页面左下：+3V-R6(10KΩ)-EN-C11(100nF)-GND |

## 系统结构

### Unit Camera

U5 ESP-WROOM-32E 连接 U2 摄像头 FPC、J1 UART、P1/P2 下载针座和 D1 蓝色 LED；U1/U3/U4 生成 +3V/+1.2V/+2.8V。

- 参数与网络：`controller=U5 ESP-WROOM-32E`；`camera=U2 FPC0.5-24P`；`host_uart=J1`；`download=P1/P2`；`indicator=D1 GPIO4`；`power=U1 +3V, U3 +1.2V, U4 +2.8V`
- 证据：图 62b5862e5c19 / 第 1 页 / 完整单页各功能区及同名 GPIO/电源网络

## 核心器件

### U5 ESP-WROOM-32E

U5.2/37 接 +3V，U5.1/15/38/39 接 GND，EN.3 接 EN 网络，TXD0.35/RXD0.34 接下载针座，GPIO16.27/GPIO17.28 接 J1。

- 参数与网络：`supply=pins 2/37 +3V`；`grounds=pins 1/15/38/39`；`enable=pin3 EN`；`uart0=pin35 TXD0, pin34 RXD0`；`host_uart=pin27 GPIO16, pin28 GPIO17`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面下中：U5 的电源/GND/EN/TXD0/RXD0/GPIO16/GPIO17 引脚

## 电源

### U2 摄像头电源

U2.DOVDD.11 与 AVDD.4 接 +2.8V，DVDD.10 接 +1.2V，DGND.15 与 AGND.2 接 GND；PWDN.8 经 R5 10KΩ 接 GND。

- 参数与网络：`DOVDD=+2.8V pin11`；`AVDD=+2.8V pin4`；`DVDD=+1.2V pin10`；`DGND=pin15`；`AGND=pin2`；`PWDN=pin8 via R5 10KΩ to GND`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右上：U2 DOVDD/DVDD/AVDD/DGND/AGND/PWDN 与 +2.8V/+1.2V/GND/R5

### U1 SY8089AAAC

U1.IN.4 与 EN.1 接 +5V，LX.3 经 L1（WPN3012H2R2MT）生成 +3V，FB.5 使用 R1 40.2KΩ 与 R2 10KΩ 分压；C1/C2/C3 均为 22uF。

- 参数与网络：`input=+5V`；`output=+3V`；`inductor=L1 WPN3012H2R2MT`；`feedback=R1 40.2KΩ, R2 10KΩ`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面左上：+5V-U1-L1-+3V 与 R1/R2/C1/C2/C3

### U3/U4

U3 将 +5V 转为 +1.2V，U4 将 +5V 转为 +2.8V；两者均标 300mA LDO，并配置输入/输出电容。

- 参数与网络：`U3=HX6306P122 1.2V LDO 300mA; C4/C5 1uF`；`U4=HX6306P282 2.8V LDO 300mA; C6/C7 1uF, C8 22uF`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面左中：U3/U4 与 +5V/+1.2V/+2.8V、C4~C8

## 接口

### J1

J1.1 RX 接 GPIO16，J1.2 TX 接 GPIO17，J1.3 VCC 接 +5V，J1.4 GND 接地。

- 参数与网络：`connector=HY-2.0_UART`；`pin_1=RX / GPIO16`；`pin_2=TX / GPIO17`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_type=UART`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右中：J1.1~4 与 GPIO16/GPIO17/+5V/GND

## 总线

### U2 摄像头像素数据

U2.Y2.19、Y1.23、Y0.24、Y3.21、Y4.22、Y5.20、Y6.18、Y7.16 分别连接 GPIO32、GPIO35、GPIO34、GPIO5、GPIO39、GPIO18、GPIO36、GPIO19。

- 参数与网络：`D0_Y2=GPIO32`；`D1_Y1=GPIO35`；`D2_Y0=GPIO34`；`D3_Y3=GPIO5`；`D4_Y4=GPIO39`；`D5_Y5=GPIO18`；`D6_Y6=GPIO36`；`D7_Y7=GPIO19`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右上 U2.16/U2.18~24 与 GPIO19/36/32/18/5/39/35/34

### J1 与 U5

J1.RX 网络连接 U5.GPIO16.27，J1.TX 网络连接 U5.GPIO17.28，中间没有串联器件或电平转换器。

- 参数与网络：`RX=J1.1 -> GPIO16 / U5.27`；`TX=J1.2 -> GPIO17 / U5.28`；`level_shifter=none shown`；`series_components=none shown`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面中下至右中：U5 GPIO16/GPIO17 与 J1 RX/TX 同名网络

## GPIO 与控制信号

### U2 相机控制与同步

PCLK.17 经 R3 47Ω 接 GPIO21，XCLK.13 经 R4 47Ω 接 GPIO27，HREF.9 接 GPIO26，VSYNC.7 接 GPIO22，RESET.6 接 GPIO15，SIO_C.5 接 GPIO23，SIO_D.3 接 GPIO25。

- 参数与网络：`PCLK=GPIO21 via R3 47Ω`；`XCLK=GPIO27 via R4 47Ω`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO23`；`SIO_D=GPIO25`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右上：U2 PCLK/XCLK/HREF/VSYNC/RESET/SIO_C/SIO_D 与 R3/R4/GPIO 网络

### D1 蓝色 LED

+3V 经 D1（蓝灯 0603）和 R7（1KΩ）连接 GPIO4，形成由 GPIO4 控制的状态灯支路。

- 参数与网络：`supply=+3V`；`led=D1 蓝灯 0603`；`resistor=R7 1KΩ`；`gpio=GPIO4 / U5.26`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面中下：+3V-D1-R7-GPIO4/U5.26

## 时钟

### U5 模组时钟与射频

本页未展开 ESP-WROOM-32E 内部晶体、Flash、射频匹配和天线连接；板上也未显示外部晶体或天线座。

- 参数与网络：`external_crystal=none shown`；`external_antenna_connector=none shown`；`module_internals=not expanded`
- 证据：图 62b5862e5c19 / 第 1 页 / 完整单页：U5 为黑盒 ESP-WROOM-32E，外围无晶体/射频器件

## 复位

### U5 EN

EN 网络由 R6（10KΩ）上拉至 +3V，并由 C11（100nF）连接 GND，同时引出到 P2.1。

- 参数与网络：`enable_pin=U5.3 EN`；`pullup=R6 10KΩ to +3V`；`capacitor=C11 100nF to GND`；`download_header=P2.1`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面左下至右下：R6/C11/EN/U5.3/P2.1

## 保护电路

### J1 与电源输入

本页未显示 J1 RX/TX/+5V 的 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`uart_esd=none shown`；`power_tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`
- 证据：图 62b5862e5c19 / 第 1 页 / J1 至 U5/U1/U3/U4 的完整 UART 和 +5V 路径，无保护器件

## 调试与烧录

### P1/P2

P1.1 接 RXD0、P1.2 接 TXD0、P1.3 接 +5V；P2.1 接 EN、P2.2 接 GPIO0、P2.3 接 GND。

- 参数与网络：`P1=pin1 RXD0, pin2 TXD0, pin3 +5V`；`P2=pin1 EN, pin2 GPIO0, pin3 GND`；`onboard_usb_bridge=none shown`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右下：P1/P2 Header3 的 RXD0/TXD0/+5V 与 EN/GPIO0/GND

## 其他事实

### 程序下载实现

原理图提供 P1/P2 下载针座，但未显示 USB 接口、USB-UART 桥或自动下载晶体管电路。

- 参数与网络：`download_headers=P1/P2`；`usb_connector=none shown`；`usb_uart_bridge=none shown`；`auto_boot_reset=none shown`
- 证据：图 62b5862e5c19 / 第 1 页 / 页面右下 P1/P2 及完整单页，无 USB/桥接器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Camera | `controller=U5 ESP-WROOM-32E`；`camera=U2 FPC0.5-24P`；`host_uart=J1`；`download=P1/P2`；`indicator=D1 GPIO4`；`power=U1 +3V, U3 +1.2V, U4 +2.8V` |
| 核心器件 | U5 ESP-WROOM-32E | `supply=pins 2/37 +3V`；`grounds=pins 1/15/38/39`；`enable=pin3 EN`；`uart0=pin35 TXD0, pin34 RXD0`；`host_uart=pin27 GPIO16, pin28 GPIO17` |
| 总线 | U2 摄像头像素数据 | `D0_Y2=GPIO32`；`D1_Y1=GPIO35`；`D2_Y0=GPIO34`；`D3_Y3=GPIO5`；`D4_Y4=GPIO39`；`D5_Y5=GPIO18`；`D6_Y6=GPIO36`；`D7_Y7=GPIO19` |
| GPIO 与控制信号 | U2 相机控制与同步 | `PCLK=GPIO21 via R3 47Ω`；`XCLK=GPIO27 via R4 47Ω`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO23`；`SIO_D=GPIO25` |
| 电源 | U2 摄像头电源 | `DOVDD=+2.8V pin11`；`AVDD=+2.8V pin4`；`DVDD=+1.2V pin10`；`DGND=pin15`；`AGND=pin2`；`PWDN=pin8 via R5 10KΩ to GND` |
| 传感器 | U2 摄像头模组 | `documented_sensor=OV2640`；`documented_resolution=2MP`；`documented_dfov=65°`；`documented_lens=4.8±5% mm, aperture 2.4±5%, distortion <1%`；`schematic=FPC0.5-24P only` |
| 接口 | J1 | `connector=HY-2.0_UART`；`pin_1=RX / GPIO16`；`pin_2=TX / GPIO17`；`pin_3=VCC / +5V`；`pin_4=GND`；`signal_type=UART` |
| 总线 | J1 与 U5 | `RX=J1.1 -> GPIO16 / U5.27`；`TX=J1.2 -> GPIO17 / U5.28`；`level_shifter=none shown`；`series_components=none shown` |
| 调试与烧录 | P1/P2 | `P1=pin1 RXD0, pin2 TXD0, pin3 +5V`；`P2=pin1 EN, pin2 GPIO0, pin3 GND`；`onboard_usb_bridge=none shown` |
| 复位 | U5 EN | `enable_pin=U5.3 EN`；`pullup=R6 10KΩ to +3V`；`capacitor=C11 100nF to GND`；`download_header=P2.1` |
| GPIO 与控制信号 | D1 蓝色 LED | `supply=+3V`；`led=D1 蓝灯 0603`；`resistor=R7 1KΩ`；`gpio=GPIO4 / U5.26` |
| 电源 | U1 SY8089AAAC | `input=+5V`；`output=+3V`；`inductor=L1 WPN3012H2R2MT`；`feedback=R1 40.2KΩ, R2 10KΩ`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF` |
| 电源 | U3/U4 | `U3=HX6306P122 1.2V LDO 300mA; C4/C5 1uF`；`U4=HX6306P282 2.8V LDO 300mA; C6/C7 1uF, C8 22uF` |
| 内存与 Flash | ESP-WROOM-32E Flash | `module=U5 ESP-WROOM-32E`；`documented_flash=4MB`；`schematic_flash=not expanded` |
| 时钟 | U5 模组时钟与射频 | `external_crystal=none shown`；`external_antenna_connector=none shown`；`module_internals=not expanded` |
| 保护电路 | J1 与电源输入 | `uart_esd=none shown`；`power_tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown` |
| 其他事实 | 程序下载实现 | `download_headers=P1/P2`；`usb_connector=none shown`；`usb_uart_bridge=none shown`；`auto_boot_reset=none shown` |

## 待确认事项

- `sensor.camera-model-optics-unconfirmed`：正文称传感器为 OV2640、2MP、DFOV 65°，并列出焦距/光圈/畸变；原理图只显示 U2 FPC0.5-24P，没有传感器或镜头型号。（证据：图 62b5862e5c19 / 第 1 页 / 页面右上：U2 仅标 FPC0.5-24P 和电气引脚）
- `memory.flash-capacity-unconfirmed`：正文称 Flash 为 4MB；原理图只显示 ESP-WROOM-32E 模组，没有展开内部 Flash 或标注容量。（证据：图 62b5862e5c19 / 第 1 页 / 页面下中：U5 仅为 ESP-WROOM-32E 黑盒模组，无 Flash 器件/容量）
- `review.camera-model-optics`：U2 所装摄像头是否为 OV2640 2MP、DFOV 65° 且镜头参数符合正文规格？；原因：原理图只提供 FPC 电气接口，没有传感器和镜头料号，需要摄像头 BOM/丝印或实物确认。
- `review.flash-capacity`：U5 当前装配的 ESP-WROOM-32E 变体是否含 4MB Flash？；原因：模组内部存储未在板级原理图展开，需根据完整模组订货号、BOM 或固件读取确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `62b5862e5c194b7367270176b87ab08ebe4b791a613665159b89775899c9cc8e` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_sch_01.webp` |

---

源文档：`zh_CN/unit/Unit Camera.md`

源文档 SHA-256：`9960829e5be6967c697431a936a9b8da6a13191f0a7424cbcdd4ee72d2b6a122`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
