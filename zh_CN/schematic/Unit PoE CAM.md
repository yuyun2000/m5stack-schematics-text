# Unit PoE CAM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PoE CAM |
| SKU | U121 |
| 产品 ID | `unit-poe-cam-457508024666` |
| 源文档 | `zh_CN/unit/poe_cam.md` |

## 概述

Unit PoE CAM 以 ESP32-D0WDQ6（U3）为主控，通过 SPI 连接 W5500（U2），W5500 经 HY601742 网络变压器（T1）连接 RJ45。U4 是 24 Pin 摄像头 FPC，连接 8 位并行像素数据、PCLK/HREF/VSYNC、XCLK 和 SIO_C/SIO_D；板上另有 ESP-PSRAM64H（U5）与 XM25QH128BHIQ（U6）。+5V 经 SY8003ADFC 降压为 +3.3V，XC6421AB3SER-G 生成 +1.2V 与 +2.8V；P1/P4 引出 PoE 变压器抽头与 5V@1.2A 电源接口。

## 检索关键词

`Unit PoE CAM`、`U121`、`ESP32-D0WDQ6`、`W5500`、`ESP-PSRAM64H`、`XM25QH128BHIQ`、`FPC0.5-24P`、`OV2640`、`SY8003ADFC`、`XC6421AB3SER-G`、`HY601742`、`RJ45`、`PoE`、`IEEE802.3af`、`SPI`、`SCS/CMD`、`SCK/CLK`、`GPIO13`、`GPIO38`、`GPIO23`、`GPIO4`、`XCLK`、`PCLK`、`HREF`、`VSYNC`、`SIO_C`、`SIO_D`、`VDD_SDIO`、`+5V`、`+3.3V`、`+2.8V`、`+1.2V`、`SWP/SD3`、`SHD/SD2`、`U0TX`、`U0RX`、`GPIO0`、`GPIO37`、`25MHZ`、`40M`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-D0WDQ6 | 主控 SoC，连接摄像头、W5500、PSRAM、Flash、按键、LED 和串口 | 图 e91dc57cc0c3 / 第 1 页 / 左中至左下：U3 ESP32-D0WDQ6 的 48 脚符号与 GPIO/SDIO/晶振/串口网络 |
| U2 | W5500 | SPI 以太网控制器，连接 ESP32 与 10/100M 以太网模拟前端 | 图 e91dc57cc0c3 / 第 1 页 / 上中：U2 W5500，SPI、25MHz 晶振、TX/RX 差分与 LED 引脚 |
| U4 | FPC0.5-24P | 24 Pin 摄像头接口，连接并行像素总线、同步、时钟、SCCB 类控制和三路电源 | 图 e91dc57cc0c3 / 第 1 页 / 右中至右下：U4 FPC0.5-24P，Y0~Y9、PCLK、XCLK、HREF、VSYNC、SIO_C、SIO_D 与电源脚 |
| U5 | ESP-PSRAM64H | 连接 ESP32 SDIO 网络的外部 PSRAM | 图 e91dc57cc0c3 / 第 1 页 / 右中：U5 ESP-PSRAM64H，CE/SIO0~3/SCLK/VCC/GND 与 GPIO16/GPIO17/SDIO 网络 |
| U6 | XM25QH128BHIQ | 连接 ESP32 SDIO 网络的外部串行 Flash | 图 e91dc57cc0c3 / 第 1 页 / 右中：U6 XM25QH128BHIQ，CE/SO/WP/HOLD/SCK/SI/VCC/GND 与 SDIO 网络 |
| U1 | SY8003ADFC | 将 +5V 降压生成 +3.3V | 图 e91dc57cc0c3 / 第 1 页 / 左上：U1 SY8003ADFC、L2、R5/R9、C3~C7 组成的 +5V 到 +3.3V 降压电路 |
| U7 | XC6421AB3SER-G | 由 +5V 生成 +1.2V 和 +2.8V 的双路稳压器 | 图 e91dc57cc0c3 / 第 1 页 / 左上偏中：U7 XC6421AB3SER-G，VIN/EN1/EN2、VOUT1 +1.2V、VOUT2 +2.8V |
| T1 | HY601742 | W5500 与 RJ45 之间的以太网隔离变压器/共模磁性器件 | 图 e91dc57cc0c3 / 第 1 页 / 右上：T1 HY601742，左接 RX_N/RX_P/TX_N/TX_P，右接 RJ45 RX-/RX+/TX-/TX+ 与 VA/VB 抽头 |
| RJ45 | 未标注 | 以太网线缆接口，包含 TX±、RX±、VA/VB PoE 导体连接 | 图 e91dc57cc0c3 / 第 1 页 / 右上角：RJ45 符号及 J1 TX+、J2 TX-、J3 RX+、J6 RX-、VA1/VA2/VB1/VB2 |
| Y1 | 25MHZ 12PF 10PPM | W5500 的 25MHz 晶体 | 图 e91dc57cc0c3 / 第 1 页 / 上中偏右：Y1 标注 25MHZ 12PF 10PPM，连接 W5500 XO/XI 与 C11/C17 |
| Y2 | 40M | ESP32 的 40MHz 晶体 | 图 e91dc57cc0c3 / 第 1 页 / 下中：Y2 标注 40M，连接 X_P/X_N，配 C32/C31 12pF 和 R35 0Ω |
| J1 | HY-2.0_IIC | Grove 扩展接口，连接 GPIO23、GPIO25、+5V、GND | 图 e91dc57cc0c3 / 第 1 页 / 右中：J1 HY-2.0_IIC 四脚及 GPIO23/GPIO25/+5V/GND 网络，D4~D6 保护支路 |
| P1, P4 | Header 4 / Header 2 | PoE 磁性器件抽头与 5V@1.2A 电源连接接口 | 图 e91dc57cc0c3 / 第 1 页 / 右中：P1 Header4 的 VA1/VA2/VB1/VB2；P4 Header2 的 GND 与 5V@1.2A，D3 SS22 接 +5V |
| P2, P3 | Header 3 | ESP32 下载/调试接口，分别引出 GND/GPIO0/EN 与 +3.3V/U0TX/U0RX | 图 e91dc57cc0c3 / 第 1 页 / 右中：P2 Header3 GND/GPIO0/EN 与 P3 Header3 +3.3V/U0TX/U0RX |
| S1, S2 | SW-PB | GPIO37 用户按键与 EN 复位按键 | 图 e91dc57cc0c3 / 第 1 页 / 左下：S1 将 GPIO37 拉至 GND；S2 将 EN 拉至 GND |
| D4, D5, D6, D7 | RLSD52A031V | Grove 信号/电源与 GPIO37 按键网络的对地保护器件 | 图 e91dc57cc0c3 / 第 1 页 / 右中 J1 下方 D4/D5/D6 与左下 S1 旁 D7，均标注 RLSD52A031V 并接 GND |

## 系统结构

### Unit PoE CAM

U3 ESP32-D0WDQ6 连接 U4 摄像头 FPC、U2 W5500、U5 PSRAM 和 U6 Flash；W5500 经 T1 HY601742 接 RJ45。

- 参数与网络：`controller=U3 ESP32-D0WDQ6`；`ethernet=U2 W5500`；`camera=U4 FPC0.5-24P`；`psram=U5 ESP-PSRAM64H`；`flash=U6 XM25QH128BHIQ`；`magnetics=T1 HY601742`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 全页：U3 与 U2/U4/U5/U6 的同名网络，以及 U2-T1-RJ45 路径

## 电源

### U4 摄像头电源

U4.DVDD.10 接 +1.2V，DOVDD.11 与 AVDD.4 接 +2.8V；PWDN.8 经 R31（10KΩ）连接 +2.8V，AGND.2 接 GND。

- 参数与网络：`DVDD=+1.2V / pin 10`；`DOVDD=+2.8V / pin 11`；`AVDD=+2.8V / pin 4`；`PWDN=pin 8 via R31 10KΩ to +2.8V`；`AGND=pin 2 GND`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右下 U4 的 DOVDD/DVDD/AVDD/PWDN/AGND 与 +2.8V/+1.2V/R31/GND 网络

### U1 SY8003ADFC

U1 由 +5V 输入并通过 L2（WPN3012H2R2MT）输出 +3.3V；R5 68KΩ、R9 15KΩ 构成 FB 分压，C3/C4 为 22uF 输入电容，C6/C7 为 22uF 输出电容。

- 参数与网络：`input=+5V`；`output=+3.3V`；`inductor=L2 WPN3012H2R2MT`；`feedback=R5 68KΩ, R9 15KΩ`；`input_caps=C3 22uF, C4 22uF`；`output_caps=C6 22uF, C7 22uF`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左上：+5V-U1-L2-+3.3V 路径及 R5/R9、C3~C7

### U7 XC6421AB3SER-G

U7 的 VIN.2、EN1.3、EN2.1 接 +5V，VOUT1.5 输出 +1.2V，VOUT2.6 输出 +2.8V；C35/C36/C37 均为 1.0uF。

- 参数与网络：`input_enable=+5V to VIN/EN1/EN2`；`VOUT1=+1.2V`；`VOUT2=+2.8V`；`input_cap=C35 1.0uF`；`output_caps=C36 1.0uF, C37 1.0uF`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左上偏中：U7 与 +5V/+1.2V/+2.8V、C35/C36/C37

### A3V3 与 AGND

+3.3V 经 FB1（600Ω@100M）生成 A3V3，GND 经 R22（0Ω）连接 AGND。

- 参数与网络：`analog_supply_filter=FB1 600Ω@100M between +3.3V and A3V3`；`ground_link=R22 0Ω between GND and AGND`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左中：FB1 的 +3.3V/A3V3 与 R22 的 GND/AGND 网络

### P1/P4 PoE 接口

P1 四脚连接 T1/RJ45 的 VA1、VA2、VB1、VB2 抽头；P4 两脚为 GND 与 5V@1.2A，后者经 D3（SS22）连接板上 +5V。

- 参数与网络：`P1=VA1, VA2, VB1, VB2`；`P4=GND, 5V@1.2A`；`diode=D3 SS22 between 5V@1.2A and +5V`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右上 T1/RJ45 的 VA/VB 抽头与右中 P1/P4、D3/+5V

## 接口

### W5500 至 RJ45

U2 的 RX_N/RX_P 与 TX_N/TX_P 经 49.9Ω/耦合网络进入 T1，T1 的 RX-/RX+/TX-/TX+ 连接 RJ45 对应导体。

- 参数与网络：`receive=RX_N, RX_P -> T1 -> RJ45 RX-, RX+`；`transmit=TX_N, TX_P -> T1 -> RJ45 TX-, TX+`；`magnetics=T1 HY601742`；`termination=R6/R7/R15/R16 49.9Ω; R17~R20 75Ω`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 上中至右上：U2 RX/TX 差分线、R6/R7/R15/R16、T1、R17~R20 与 RJ45

### J1 HY-2.0_IIC

J1.1 IIC_SCL 接 GPIO23，J1.2 IIC_SDA 接 GPIO25，J1.3 VCC 接 +5V，J1.4 接 GND。

- 参数与网络：`pin_1=IIC_SCL / GPIO23`；`pin_2=IIC_SDA / GPIO25`；`pin_3=+5V`；`pin_4=GND`；`protection=D4/D5/D6 RLSD52A031V`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中：J1 四脚、GPIO23/GPIO25/+5V/GND 网络与 D4/D5/D6

## 总线

### U3 与 U2 W5500

W5500 的 MOSI、MISO、SCLK、SCSn 分别连接 GPIO13、GPIO38、GPIO23、GPIO4。

- 参数与网络：`MOSI=GPIO13`；`MISO=GPIO38`；`SCLK=GPIO23`；`CS=GPIO4 / SCSn`；`controller=U3`；`device=U2 W5500`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 上中 U2.35~U2.32 的 MOSI/MISO/SCLK/SCSn 与 GPIO13/GPIO38/GPIO23/GPIO4；左中 U3 同名 GPIO

### U4 摄像头像素数据

U4 的 Y2.19、Y1.23、Y0.24、Y3.21、Y4.22、Y5.20、Y6.18、Y7.16 分别连接 GPIO32、GPIO35、GPIO34、GPIO5、GPIO39、GPIO18、GPIO36、GPIO19。

- 参数与网络：`D0_Y2=GPIO32 / U4.19`；`D1_Y1=GPIO35 / U4.23`；`D2_Y0=GPIO34 / U4.24`；`D3_Y3=GPIO5 / U4.21`；`D4_Y4=GPIO39 / U4.22`；`D5_Y5=GPIO18 / U4.20`；`D6_Y6=GPIO36 / U4.18`；`D7_Y7=GPIO19 / U4.16`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中 U4.16/U4.18~U4.24 的 Y0~Y7 与左侧 GPIO19/36/32/18/5/39/35/34 网络

## GPIO 与控制信号

### U4 摄像头控制与同步

PCLK.17 经 R28 47Ω 接 GPIO21，XCLK.13 经 R29 47Ω 接 GPIO27，HREF.9 接 GPIO26，VSYNC.7 接 GPIO22，RESET.6 接 GPIO15，SIO_C.5 接 GPIO12，SIO_D.3 接 GPIO14。

- 参数与网络：`PCLK=GPIO21 via R28 47Ω`；`XCLK=GPIO27 via R29 47Ω`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO12`；`SIO_D=GPIO14`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中至右下：U4.17/13/9/7/6/5/3 与 R28/R29 及 GPIO21/27/26/22/15/12/14

### S1

S1 按下时将 GPIO37 拉至 GND；R32（10KΩ）将 GPIO37 上拉至 +3.3V，D7（RLSD52A031V）对地保护。

- 参数与网络：`gpio=GPIO37`；`button=S1 SW-PB to GND`；`pullup=R32 10KΩ to +3.3V`；`protection=D7 RLSD52A031V to GND`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左下：S1、GPIO37、R32、D7 与 GND

### D1 与 D2

W5500.ACTLED.27 连接 D1（绿灯 0603）支路，LINKLED.25 连接 D2（蓝灯 0603）支路；R12/R14 均为 1KΩ 并接 +3.3V。

- 参数与网络：`activity=U2.27 ACTLED -> D1 绿灯 0603, R12 1KΩ`；`link=U2.25 LINKLED -> D2 蓝灯 0603, R14 1KΩ`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 上中偏右：U2 ACTLED/LINKLED 与 D1/D2、R12/R14、+3.3V

## 时钟

### U2 W5500

Y1（25MHZ 12PF 10PPM）连接 U2.XO.31 与 XI/CLKIN.30，C11/C17 均为 12pF，R21 为 1MΩ。

- 参数与网络：`crystal=Y1 25MHZ 12PF 10PPM`；`XO=U2.31`；`XI_CLKIN=U2.30`；`load_caps=C11 12pF, C17 12pF`；`bias_resistor=R21 1MΩ`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 上中偏右：XO/XI 网络的 Y1、C11、C17、R21

### U3 ESP32

U3.XTAL_P.45 与 XTAL_N.44 通过 X_P/X_N 连接 Y2（40M）；R35 为 0Ω，C32/C31 均为 12pF。

- 参数与网络：`crystal=Y2 40M`；`XTAL_P=U3.45`；`XTAL_N=U3.44`；`series_resistor=R35 0Ω`；`load_caps=C32 12pF, C31 12pF`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左中 U3 XTAL_P/XTAL_N 与下中 Y2/R35/C31/C32 的 X_P/X_N 网络

## 复位

### U3 EN

U3.EN.47 由 R24（10KΩ）上拉至 +3.3V、C30（100nF）接 GND，S2 按下时将 EN 拉至 GND。

- 参数与网络：`enable_pin=U3.47 EN`；`pullup=R24 10KΩ`；`capacitor=C30 100nF`；`button=S2 SW-PB to GND`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 左中 U3.EN 与 R24/C30，左下 S2-EN-GND

## 保护电路

### Grove、按键与以太网

J1 使用 D4/D5/D6（RLSD52A031V）对地保护，GPIO37 按键使用 D7（RLSD52A031V）；RJ45 侧 R17~R20（75Ω）汇接并经 C14（1nF 2kV）到 GND。

- 参数与网络：`grove=D4/D5/D6 RLSD52A031V`；`button=D7 RLSD52A031V`；`ethernet_bob_smith=R17~R20 75Ω, C14 1nF 2kV`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中 J1/D4~D6、左下 S1/D7、右上 RJ45/R17~R20/C14

## 存储

### U6 XM25QH128BHIQ

U6 由 VDD_SDIO 供电，CE/SO/WP/HOLD/SCK/SI 分别连接 SCS/CMD、SDO/SD0、SWP/SD3、SHD/SD2、SCK/CLK、SDI/SD1。

- 参数与网络：`VCC=VDD_SDIO`；`CE=SCS/CMD`；`SO=SDO/SD0`；`WP=SWP/SD3`；`HOLD=SHD/SD2`；`SCK=SCK/CLK`；`SI=SDI/SD1`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中：U6 XM25QH128BHIQ 的 1~8 脚与 VDD_SDIO、SCS/CMD、SDO/SD0、SWP/SD3、SHD/SD2、SCK/CLK、SDI/SD1

## 内存与 Flash

### U5 ESP-PSRAM64H

U5 由 VDD_SDIO 供电，CE 接 GPIO16、SCLK 接 GPIO17，SIO0~SIO3 接 SDI/SD1、SDO/SD0、SWP/SD3、SHD/SD2 网络。

- 参数与网络：`VCC=VDD_SDIO`；`CE=GPIO16`；`SCLK=GPIO17`；`SIO0=SDI/SD1`；`SIO1=SDO/SD0`；`SIO2=SWP/SD3`；`SIO3=SHD/SD2`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中：U5 ESP-PSRAM64H 的 1~8 脚与 GPIO16/GPIO17/VDD_SDIO/SDIO 网络

## 调试与烧录

### P2 与 P3

P2 引出 GND、GPIO0、EN；P3 引出 +3.3V、U0TX、U0RX，U0TX/U0RX 分别连接 U3.U0TXD.41 与 U0RXD.40。

- 参数与网络：`P2=GND, GPIO0, EN`；`P3=+3.3V, U0TX, U0RX`；`UART_TX=U3.41 U0TXD`；`UART_RX=U3.40 U0RXD`；`series=R30 499Ω on U0TX`
- 证据：图 e91dc57cc0c3 / 第 1 页 / 右中 P2/P3 与左下 U3.40/U3.41 的 U0RX/U0TX 网络、R30 499Ω

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PoE CAM | `controller=U3 ESP32-D0WDQ6`；`ethernet=U2 W5500`；`camera=U4 FPC0.5-24P`；`psram=U5 ESP-PSRAM64H`；`flash=U6 XM25QH128BHIQ`；`magnetics=T1 HY601742` |
| 总线 | U3 与 U2 W5500 | `MOSI=GPIO13`；`MISO=GPIO38`；`SCLK=GPIO23`；`CS=GPIO4 / SCSn`；`controller=U3`；`device=U2 W5500` |
| 接口 | W5500 至 RJ45 | `receive=RX_N, RX_P -> T1 -> RJ45 RX-, RX+`；`transmit=TX_N, TX_P -> T1 -> RJ45 TX-, TX+`；`magnetics=T1 HY601742`；`termination=R6/R7/R15/R16 49.9Ω; R17~R20 75Ω` |
| 时钟 | U2 W5500 | `crystal=Y1 25MHZ 12PF 10PPM`；`XO=U2.31`；`XI_CLKIN=U2.30`；`load_caps=C11 12pF, C17 12pF`；`bias_resistor=R21 1MΩ` |
| 时钟 | U3 ESP32 | `crystal=Y2 40M`；`XTAL_P=U3.45`；`XTAL_N=U3.44`；`series_resistor=R35 0Ω`；`load_caps=C32 12pF, C31 12pF` |
| 总线 | U4 摄像头像素数据 | `D0_Y2=GPIO32 / U4.19`；`D1_Y1=GPIO35 / U4.23`；`D2_Y0=GPIO34 / U4.24`；`D3_Y3=GPIO5 / U4.21`；`D4_Y4=GPIO39 / U4.22`；`D5_Y5=GPIO18 / U4.20`；`D6_Y6=GPIO36 / U4.18`；`D7_Y7=GPIO19 / U4.16` |
| GPIO 与控制信号 | U4 摄像头控制与同步 | `PCLK=GPIO21 via R28 47Ω`；`XCLK=GPIO27 via R29 47Ω`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO12`；`SIO_D=GPIO14` |
| 电源 | U4 摄像头电源 | `DVDD=+1.2V / pin 10`；`DOVDD=+2.8V / pin 11`；`AVDD=+2.8V / pin 4`；`PWDN=pin 8 via R31 10KΩ to +2.8V`；`AGND=pin 2 GND` |
| 传感器 | U4 摄像头模组 | `documented_sensor=OV2640`；`schematic_designation=U4 FPC0.5-24P`；`resolution_claim=2MegaPixel; not shown` |
| 内存与 Flash | U5 ESP-PSRAM64H | `VCC=VDD_SDIO`；`CE=GPIO16`；`SCLK=GPIO17`；`SIO0=SDI/SD1`；`SIO1=SDO/SD0`；`SIO2=SWP/SD3`；`SIO3=SHD/SD2` |
| 存储 | U6 XM25QH128BHIQ | `VCC=VDD_SDIO`；`CE=SCS/CMD`；`SO=SDO/SD0`；`WP=SWP/SD3`；`HOLD=SHD/SD2`；`SCK=SCK/CLK`；`SI=SDI/SD1` |
| 内存与 Flash | U5 与 U6 容量 | `documented_psram=8MB`；`documented_flash=16MB`；`psram_part=ESP-PSRAM64H`；`flash_part=XM25QH128BHIQ` |
| 电源 | U1 SY8003ADFC | `input=+5V`；`output=+3.3V`；`inductor=L2 WPN3012H2R2MT`；`feedback=R5 68KΩ, R9 15KΩ`；`input_caps=C3 22uF, C4 22uF`；`output_caps=C6 22uF, C7 22uF` |
| 电源 | U7 XC6421AB3SER-G | `input_enable=+5V to VIN/EN1/EN2`；`VOUT1=+1.2V`；`VOUT2=+2.8V`；`input_cap=C35 1.0uF`；`output_caps=C36 1.0uF, C37 1.0uF` |
| 电源 | A3V3 与 AGND | `analog_supply_filter=FB1 600Ω@100M between +3.3V and A3V3`；`ground_link=R22 0Ω between GND and AGND` |
| 接口 | J1 HY-2.0_IIC | `pin_1=IIC_SCL / GPIO23`；`pin_2=IIC_SDA / GPIO25`；`pin_3=+5V`；`pin_4=GND`；`protection=D4/D5/D6 RLSD52A031V` |
| 调试与烧录 | P2 与 P3 | `P2=GND, GPIO0, EN`；`P3=+3.3V, U0TX, U0RX`；`UART_TX=U3.41 U0TXD`；`UART_RX=U3.40 U0RXD`；`series=R30 499Ω on U0TX` |
| 复位 | U3 EN | `enable_pin=U3.47 EN`；`pullup=R24 10KΩ`；`capacitor=C30 100nF`；`button=S2 SW-PB to GND` |
| GPIO 与控制信号 | S1 | `gpio=GPIO37`；`button=S1 SW-PB to GND`；`pullup=R32 10KΩ to +3.3V`；`protection=D7 RLSD52A031V to GND` |
| GPIO 与控制信号 | D1 与 D2 | `activity=U2.27 ACTLED -> D1 绿灯 0603, R12 1KΩ`；`link=U2.25 LINKLED -> D2 蓝灯 0603, R14 1KΩ` |
| 电源 | P1/P4 PoE 接口 | `P1=VA1, VA2, VB1, VB2`；`P4=GND, 5V@1.2A`；`diode=D3 SS22 between 5V@1.2A and +5V` |
| 电源 | PoE 输入规格 | `documented_standard=IEEE 802.3af`；`documented_input=DC 37-57V`；`documented_max_power=6W`；`schematic_visible_output=5V@1.2A on P4` |
| 保护电路 | Grove、按键与以太网 | `grove=D4/D5/D6 RLSD52A031V`；`button=D7 RLSD52A031V`；`ethernet_bob_smith=R17~R20 75Ω, C14 1nF 2kV` |

## 待确认事项

- `sensor.ov2640-unconfirmed`：产品正文称图像传感器为 OV2640，但原理图仅将 U4 标为 FPC0.5-24P，没有显示 OV2640 型号。（证据：图 e91dc57cc0c3 / 第 1 页 / 右中至右下：U4 仅标注 FPC0.5-24P 及接口信号，未见 OV2640 或分辨率文字）
- `memory.documented-capacities-unconfirmed`：产品正文称 PSRAM 为 8MB、Flash 为 16MB；原理图显示器件型号但未直接标注容量，容量需由器件资料或 BOM 复核。（证据：图 e91dc57cc0c3 / 第 1 页 / 右中：U5/U6 仅标器件型号及引脚网络，未见 MB/Mbit 容量标注）
- `power.poe-standard-unconfirmed`：产品正文称支持 IEEE 802.3af、DC 37~57V、最大 6W；本页未显示 PoE PD 控制器或这些额定值，只显示 P1/P4 接口，因此无法由原理图确认。（证据：图 e91dc57cc0c3 / 第 1 页 / 右上至右中：RJ45/T1/P1/P4 路径仅标 VA/VB 与 5V@1.2A，未见 PD 控制器和 37~57V/802.3af 标注）
- `review.camera-sensor`：U4 所连接的量产摄像头模组是否为正文所列 OV2640、2M 像素版本？；原因：原理图只给出 24 Pin FPC 接口和信号，没有传感器型号或分辨率；需以摄像头模组 BOM、丝印或实物确认。
- `review.memory-capacity`：U5/U6 对应的装配容量是否分别为正文所列 8MB PSRAM 与 16MB Flash？；原因：本页只显示 ESP-PSRAM64H 和 XM25QH128BHIQ 型号，未直接标容量；需由器件数据手册或 BOM 确认。
- `review.poe-standard`：外接/配套 PoE 电源级是否满足 IEEE 802.3af、DC 37~57V、最大 6W？；原因：原理图只显示以太网抽头 P1 与 5V@1.2A P4，缺少 PoE PD 电源级及其型号/额定参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e91dc57cc0c3ef0dd32e99dacac851abd2b3bfd884e4852b319dbeaa31f0a073` | `https://static-cdn.m5stack.com/resource/docs/products/unit/poe_cam/poe_cam_sch_01.webp` |

---

源文档：`zh_CN/unit/poe_cam.md`

源文档 SHA-256：`7dd5e7fedfc277915dffe4af15f433e7e910d5f6f774d8109e2518364949b7c5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
