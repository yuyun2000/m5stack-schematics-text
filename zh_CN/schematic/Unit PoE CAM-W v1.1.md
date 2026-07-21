# Unit PoE CAM-W v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PoE CAM-W v1.1 |
| SKU | U121-B-V11 |
| 产品 ID | `unit-poe-cam-w-v1-1-32186dd0cb2c` |
| 源文档 | `zh_CN/unit/M5PoECAM-W V1.1.md` |

## 概述

Unit PoE CAM-W v1.1 以 U3 ESP32-D0WDQ6 为主控，连接 U5 ESP-PSRAM64H、U6 XM25QH128BHIQ、U4 24 针摄像头 FPC、E1 Wi-Fi IPEX、Grove、下载口、按键与 LED。U2 W5500 通过 GPIO13/GPIO38/GPIO23/GPIO4 的 SPI 接入 ESP32，并经 25MHz 晶振、T1 HY601742 磁性器件和 RJ45 连接以太网；VA1/VA2/VB1/VB2 与 P1/P4 构成外部 PoE 受电模块接口。+5V 经 U1 SY8003ADFC 生成 +3.3V，U7 XC6421AB38ER-G 生成摄像头 +1.2V/+2.8V；摄像头型号/性能、存储容量、PoE 与网络/Wi-Fi 能力需结合 BOM、datasheet 或实测确认。

## 检索关键词

`Unit PoE CAM-W v1.1`、`U121-B-V11`、`ESP32-D0WDQ6`、`ESP32-D0WDQ6-V3`、`W5500`、`OV3660`、`ESP-PSRAM64H`、`XM25QH128BHIQ`、`SY8003ADFC`、`XC6421AB38ER-G`、`HY601742`、`RJ45`、`PoE`、`IEEE802.3af`、`SPI`、`GPIO13 MOSI`、`GPIO38 MISO`、`GPIO23 SCLK`、`GPIO4 SCSn`、`25MHz`、`Y1`、`40M`、`Y2`、`ANT_IPEX`、`E1`、`FPC-0.5-24P`、`VDD_SDIO`、`+5V`、`+3.3V`、`+1.2V`、`+2.8V`、`A3V3`、`AGND`、`VA1`、`VA2`、`VB1`、`VB2`、`EXT_PORT`、`GPIO33 SCL`、`GPIO25 SDA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-D0WDQ6 | 主控 SoC，连接 W5500、摄像头、外部 Flash/PSRAM、Wi-Fi、Grove、UART、按键和 LED | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B2-D4：U3 ESP32-D0WDQ6 全部电源、GPIO、存储、RF、时钟和 UART 引脚 |
| U2 | W5500 | SPI 以太网控制器，连接 ESP32、25MHz 时钟、PHY 差分线和链路/活动 LED | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A3-B4：U2 W5500 pins1-48 |
| U4 | FPC-0.5-24P | 并行摄像头 24 针接口，引出 Y2-Y8、PCLK/XCLK、HREF/VSYNC、SIO_C/SIO_D、RESET/PWDN 与摄像头电源 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C7-D8：U4 FPC-0.5-24P pin1-pin24 |
| U5 | ESP-PSRAM64H | VDD_SDIO 供电、连接 ESP32 专用存储总线的外部 PSRAM | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C5-C6：U5 ESP-PSRAM64H 与 GPIO16/GPIO17/SD_* |
| U6 | XM25QH128BHIQ | VDD_SDIO 供电、连接 ESP32 专用存储总线的外部串行 Flash | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C5-D6：U6 XM25QH128BHIQ 与 SCS/CMD、SD0、SWP、SHD、SCK、SDI |
| U1 | SY8003ADFC | 将 +5V 降压为系统 +3.3V | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A1-A3：U1 SY8003ADFC、L2、反馈与 +5V/+3.3V |
| U7 | XC6421AB38ER-G | 由 +5V 生成摄像头 +1.2V 与 +2.8V 的双路稳压器 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A1-B2：U7 XC6421AB38ER-G，VOUT1=+1.2V、VOUT2=+2.8V |
| T1 | HY601742 | W5500 PHY 与 RJ45 线缆侧之间的双通道以太网隔离磁性器件 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A5-B7：T1 HY601742 与 RX/TX 两组绕组、中心抽头 |
| RJ45 | 未标注 | 连接 RX+/RX-/TX+/TX- 及 PoE 空闲对 VB1/VB2 的十针以太网接口 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A7-B8：RJ45 符号 Pin1-Pin10、RX/TX 与 VB1/VB2 |
| P1,P4,D3 | Header4 / Header2 / SS22 | PoE 中心抽头/空闲对输入与 5V@1.2A 输出接口，输出经 D3 汇入 +5V | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B6-C7：P1 VA1/VA2/VB1/VB2、P4 GND/VO5、D3 SS22 与 +5V |
| Y1 | 25MHZ 12PF 10PPM | W5500 XI/XO 外部 25MHz 晶振 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B4：Y1 25MHZ 12PF 10PPM、C11/C17 12pF、R21 1MΩ |
| Y2 | 40M | ESP32 X_P/X_N 外部 40MHz 晶振 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 D5-D6：Y2 40M、R35 0Ω、C31/C32 12pF 与 X_P/X_N |
| E1,L1,C1,C2 | ANT_IPEX / 1.2nH / 3.0pF / 2.2pF | ESP32 LAN_IN 至 IPEX 的 Wi-Fi 射频匹配与天线接口 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C3-C5：U3 LAN_IN-L1-E1 与 C1/C2 |
| J1 | HY-2.0_IIC | GPIO33/GPIO25 的 Grove I2C 与 +5V/GND 接口 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B6-C7：J1 HY-2.0_IIC pin1-pin4 与 GPIO33/GPIO25/+5V/GND |
| P2,P3 | Header3 / Header3 | EN/GPIO0/GND 与 +3.3V/U0TX/U0RX 下载调试接口 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B6-C7：P2 GND/GPIO0/EN 与 P3 +3.3V/U0TX/U0RX |
| S1,S2 | SW-PB / SW-PB | GPIO37 用户按键与 EN 复位按键 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C1-D2：S1 GPIO37、S2 EN 与 GND |
| D1,D2 | 绿灯 0603 / 黄灯 0603 | W5500 ACTLED 与 LINKLED 状态指示 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A4-B5：W5500 ACTLED/LINKLED 至 D1/D2 与 R12/R14 |
| D4,D5,D6,D7 | LESD3Z5.0CMT1G / RLSD52A031V | Grove 电源/信号与 GPIO37 按键节点的对地 ESD/瞬态保护 | 图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C1-D2 与 B6-C7：D4-D7 对地保护支路 |

## 系统结构

### Unit PoE CAM-W v1.1 系统结构

U3 ESP32-D0WDQ6 连接 U2 W5500、U4 摄像头 FPC、U5 PSRAM、U6 Flash、E1 Wi-Fi 天线、Grove、下载口、按键和 LED；RJ45/T1/P1/P4 构成以太网及外部 PoE 受电路径。U1/U7 由 +5V 生成 +3.3V、+1.2V、+2.8V。

- 参数与网络：`controller=U3 ESP32-D0WDQ6`；`ethernet=U2 W5500,T1 HY601742,RJ45`；`camera=U4 FPC-0.5-24P`；`memory=U5 ESP-PSRAM64H,U6 XM25QH128BHIQ`；`wifi=E1 ANT_IPEX`；`power=+5V -> U1 +3.3V; U7 +1.2V/+2.8V`；`poe=P1/P4 external module interface`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页完整 A1-D8 原理图

## 电源

### +5V 至 +3.3V 主电源

+5V 接 U1 SY8003ADFC IN pin3 与 EN pin7，LX pin6 经 L2 WPN3012H2R2MT 输出 +3.3V；R5 68KΩ/R9 15KΩ 构成反馈，C3/C4 为输入电容，C5/C6/C7 为输出电容。

- 参数与网络：`input=+5V`；`converter=U1 SY8003ADFC`；`enable=pin7 tied +5V`；`inductor=L2 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R5 68KΩ,R9 15KΩ`；`input_caps=C3 22uF,C4 22uF`；`output_caps=C5 22pF,C6 22uF,C7 22uF`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A1-A3 U1/L2/R5/R9/C3-C7

### 摄像头 +1.2V/+2.8V 电源

+5V 同时连接 U7 XC6421AB38ER-G VIN pin2 与 EN1/EN2 pins3/6；VOUT1 pin5 输出 +1.2V，VOUT2 pin1 输出 +2.8V，C35/C36/C37 各 1uF。

- 参数与网络：`input=+5V`；`regulator=U7 XC6421AB38ER-G`；`enable=EN1 pin3,EN2 pin6 tied +5V`；`output1=pin5 +1.2V`；`output2=pin1 +2.8V`；`caps=C35,C36,C37 1uF`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A1-B2 U7 与 +5V/+1.2V/+2.8V

### W5500 A3V3/AGND 分区

+3.3V 经 FB1 600Ω@100MHz 形成 A3V3，GND 经 R22 0Ω 连接 AGND；W5500 模拟电源使用 A3V3/AGND，数字电源使用 +3.3V/GND。

- 参数与网络：`digital_rail=+3.3V`；`analog_rail=A3V3`；`ferrite=FB1 600Ω@100M`；`digital_ground=GND`；`analog_ground=AGND`；`ground_bridge=R22 0Ω`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B1-B2 FB1/R22 与 U2 电源网络

### PoE 受电模块接口

T1 中心抽头 VA1/VA2 与 RJ45 空闲对 VB1/VB2 引至 P1 Header4；P4 Header2 提供 GND 与 VO5（标注 5V@1.2A），VO5 经 D3 SS22 汇入板上 +5V。PoE DC/DC 模块本体未在本页展开。

- 参数与网络：`poe_input_header=P1 VA1,VA2,VB1,VB2`；`poe_output_header=P4 GND,VO5`；`output_label=5V@1.2A`；`series_diode=D3 SS22`；`board_rail=+5V`；`poe_converter_on_page=null`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A6-C7 VA/VB、P1/P4、D3 与 +5V

### 摄像头 FPC 电源

U4 DVDD pin10 接 +1.2V、DVDD pin11 接 +2.8V，AVDD pin4 接 +2.8V；DGND/AGND 接地，Y0(AF-GND)、Y1(AF-VDD) 与 NC 脚标为未连接。

- 参数与网络：`dvdd_core=pin10 +1.2V`；`dvdd_io=pin11 +2.8V`；`avdd=pin4 +2.8V`；`grounds=DGND/AGND`；`autofocus_pins=Y0/Y1 NC`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C7-D8 U4 电源、地与 NC 标记

## 接口

### W5500 至 RJ45 以太网 PHY

W5500 TXP/TXN 与 RXP/RXN 经偏置/交流耦合网络进入 T1 HY601742，T1 线缆侧连接 RJ45 的 TX+/TX-/RX+/RX-；VA1/VA2 为变压器中心抽头。

- 参数与网络：`phy=U2 W5500`；`magnetics=T1 HY601742`；`tx=TXP/TXN -> T1 -> RJ45 TX+/TX-`；`rx=RJ45 RX+/RX- -> T1 -> RXP/RXN`；`center_taps=VA1,VA2`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A4-B8 U2/T1/RJ45 全部差分线

### 摄像头并行数据与时钟

U4 FPC 将 Y2/Y3/Y4/Y5/Y6/Y7/Y8 分别连接 GPIO34/GPIO35/GPIO5/GPIO32/GPIO39/GPIO18/GPIO36，PCLK 连接 GPIO21；XCLK pin14 由主控 GPIO 经 R29 47Ω 驱动。

- 参数与网络：`y2=GPIO34`；`y3=GPIO35`；`y4=GPIO5`；`y5=GPIO32`；`y6=GPIO39`；`y7=GPIO18`；`y8=GPIO36`；`pclk=GPIO21`；`xclk=pin14 via R29 47Ω`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C7-D8 U4 Y2-Y8/PCLK/XCLK 与左侧 GPIO 标签

### J1 Grove I2C

J1 HY-2.0_IIC pin1=IIC_SCL/GPIO33、pin2=IIC_SDA/GPIO25、pin3=+5V、pin4=GND；GPIO33、GPIO25 和 +5V 各有对地保护器件。

- 参数与网络：`pin1=IIC_SCL GPIO33`；`pin2=IIC_SDA GPIO25`；`pin3=+5V`；`pin4=GND`；`protection=D4/D5/D6 to GND`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B6-C7 J1 与 GPIO33/GPIO25/+5V/D4-D6

## 总线

### ESP32 至 W5500 SPI

U2 MOSI pin35 接 GPIO13，MISO pin34 接 GPIO38，SCLK pin33 接 GPIO23，SCSn pin32 接 GPIO4；MOSI 与 SCSn 各有 10KΩ 上拉到 +3.3V，INTn pin36 未接外部网络。

- 参数与网络：`controller=U3 ESP32-D0WDQ6`；`mosi=U2 pin35 GPIO13`；`miso=U2 pin34 GPIO38`；`sclk=U2 pin33 GPIO23`；`chip_select=U2 pin32 GPIO4`；`interrupt=U2 pin36 NC`；`pullups=10KΩ on GPIO13 and GPIO4`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A3-A5 U2 SPI/INTn 与 GPIO13/38/23/4

## GPIO 与控制信号

### W5500 模式与复位绑带

U2 RSTn 与 PMODE0/PMODE1/PMODE2 由上方四个 10KΩ 电阻上拉到 +3.3V；具体 PMODE 编码含义未在原理图打印。

- 参数与网络：`signals=RSTn,PMODE0,PMODE1,PMODE2`；`resistors=four 10KΩ pullups`；`rail=+3.3V`；`decoded_mode=null`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A3-A4 U2 pins37/43/44/45 与四联 10KΩ 上拉

### W5500 活动与链路 LED

U2 ACTLED pin27 驱动 D1 绿灯 0603，LINKLED pin25 驱动 D2 黄灯 0603；两支路分别经 R12/R14 1KΩ 上拉到 +3.3V，DUPLED pin26 未接。

- 参数与网络：`activity=U2 pin27 -> D1 green -> R12 1KΩ -> +3.3V`；`link=U2 pin25 -> D2 yellow -> R14 1KΩ -> +3.3V`；`duplex=U2 pin26 NC`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 A4-B5 U2 ACTLED/DUPLED/LINKLED 与 D1/D2

### 摄像头同步与控制信号

U4 HREF pin9 接 GPIO26、PWDN pin8 接 GPIO22、VSYNC pin7 接 GPIO25、RESET pin6 接 GPIO2、SIO_D pin3 接 GPIO14；HREF 由 R31 10KΩ 下拉，SIO_C pin5 连接主控 GPIO 网络。

- 参数与网络：`href=pin9 GPIO26 with R31 10KΩ pulldown`；`pwdn=pin8 GPIO22`；`vsync=pin7 GPIO25`；`reset=pin6 GPIO2`；`sio_d=pin3 GPIO14`；`sio_c=pin5 host GPIO`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C7-D8 U4 pins3/5/6/7/8/9 与 GPIO/R31

## 时钟

### W5500 25MHz 时钟

Y1 标注 25MHZ 12PF 10PPM，连接 U2 XO pin31 与 XI pin30；R21 1MΩ 跨接晶振，C11/C17 各 12pF 接 GND，XO 路另串 R38 200Ω。

- 参数与网络：`crystal=Y1 25MHZ 12PF 10PPM`；`xo=U2 pin31 via R38 200Ω`；`xi=U2 pin30`；`feedback=R21 1MΩ`；`load_caps=C11,C17 12pF`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B4-B5 U2 XO/XI 与 Y1/R21/R38/C11/C17

### ESP32 40MHz 时钟

U3 X_P/X_N 连接 Y2 40M，R35 0Ω 位于 X_P 路，C31/C32 各 12pF 接 GND。

- 参数与网络：`crystal=Y2 40M`；`pins=U3 X_P/X_N`；`series=R35 0Ω`；`load_caps=C31,C32 12pF`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 D5-D6 U3 X_P/X_N 与 Y2/R35/C31/C32

## 复位

### EN 复位与 GPIO37 用户按键

S2 按下将 EN 接 GND；S1 按下将 GPIO37 接 GND，R32 10KΩ 将 GPIO37 上拉到 +3.3V，D7 对 GPIO37 提供对地保护。

- 参数与网络：`reset_button=S2 EN to GND`；`user_button=S1 GPIO37 to GND`；`user_pullup=R32 10KΩ to +3.3V`；`user_esd=D7 RLSD52A031V`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C1-D2 S1/S2/R32/D7

## 保护电路

### Grove、按键和以太网保护

Grove GPIO33/GPIO25/+5V 与 GPIO37 按键节点配置对地 ESD 器件；W5500 与 RJ45 之间由 T1 磁性隔离。页面未显示 RJ45 线缆侧专用 TVS 阵列或 PoE 高压前端保护，因为 PoE 模块未展开。

- 参数与网络：`grove_esd=D4-D6`；`button_esd=D7`；`ethernet_isolation=T1 HY601742`；`rj45_tvs_shown=false`；`poe_frontend_protection_on_page=null`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 T1/RJ45 与 J1/D4-D7/P1/P4

## 内存与 Flash

### ESP32 外部 Flash/PSRAM 总线

U5 ESP-PSRAM64H 与 U6 XM25QH128BHIQ 共用 SCS/CMD、SD0/SD0、SWP/SD3、SHD/SD2、SCK/CLK、SDI/SD1 存储总线并由 VDD_SDIO 供电；U5 CE 由 GPIO16 控制、SCLK 接 GPIO17。

- 参数与网络：`psram=U5 ESP-PSRAM64H`；`flash=U6 XM25QH128BHIQ`；`shared_bus=SCS/CMD,SD0/SD0,SWP/SD3,SHD/SD2,SCK/CLK,SDI/SD1`；`supply=VDD_SDIO`；`psram_ce=GPIO16`；`psram_sclk=GPIO17`；`ce_pullup=R25 10KΩ`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B3-D6 U3 SD_* 与 U5/U6

## 射频

### ESP32 Wi-Fi 天线路径

U3 LAN_IN 经 L1 1.2nH 串联至 E1 ANT_IPEX，C1 3.0pF 与 C2 2.2pF 分别在匹配网络两侧对地。

- 参数与网络：`source=U3 LAN_IN`；`series=L1 1.2nH`；`shunt_caps=C1 3.0pF,C2 2.2pF`；`connector=E1 ANT_IPEX`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 C3-C5 U3 LAN_IN/L1/C1/C2/E1

## 调试与烧录

### ESP32 下载接口

P2 pin1=GND、pin2=GPIO0、pin3=EN；P3 pin1=U0RX、pin2=U0TX、pin3=+3.3V。U3 U0TXD 经 R30 499Ω 形成 U0TX，U0RXD 连接 U0RX。

- 参数与网络：`p2=pin1 GND,pin2 GPIO0,pin3 EN`；`p3=pin1 U0RX,pin2 U0TX,pin3 +3.3V`；`uart_tx=U3 U0TXD via R30 499Ω`；`uart_rx=U3 U0RXD`
- 证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页网格 B6-C7 P2/P3 与 C3-D4 U3 UART

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PoE CAM-W v1.1 系统结构 | `controller=U3 ESP32-D0WDQ6`；`ethernet=U2 W5500,T1 HY601742,RJ45`；`camera=U4 FPC-0.5-24P`；`memory=U5 ESP-PSRAM64H,U6 XM25QH128BHIQ`；`wifi=E1 ANT_IPEX`；`power=+5V -> U1 +3.3V; U7 +1.2V/+2.8V`；`poe=P1/P4 external module interface` |
| 电源 | +5V 至 +3.3V 主电源 | `input=+5V`；`converter=U1 SY8003ADFC`；`enable=pin7 tied +5V`；`inductor=L2 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R5 68KΩ,R9 15KΩ`；`input_caps=C3 22uF,C4 22uF`；`output_caps=C5 22pF,C6 22uF,C7 22uF` |
| 电源 | 摄像头 +1.2V/+2.8V 电源 | `input=+5V`；`regulator=U7 XC6421AB38ER-G`；`enable=EN1 pin3,EN2 pin6 tied +5V`；`output1=pin5 +1.2V`；`output2=pin1 +2.8V`；`caps=C35,C36,C37 1uF` |
| 电源 | W5500 A3V3/AGND 分区 | `digital_rail=+3.3V`；`analog_rail=A3V3`；`ferrite=FB1 600Ω@100M`；`digital_ground=GND`；`analog_ground=AGND`；`ground_bridge=R22 0Ω` |
| 总线 | ESP32 至 W5500 SPI | `controller=U3 ESP32-D0WDQ6`；`mosi=U2 pin35 GPIO13`；`miso=U2 pin34 GPIO38`；`sclk=U2 pin33 GPIO23`；`chip_select=U2 pin32 GPIO4`；`interrupt=U2 pin36 NC`；`pullups=10KΩ on GPIO13 and GPIO4` |
| GPIO 与控制信号 | W5500 模式与复位绑带 | `signals=RSTn,PMODE0,PMODE1,PMODE2`；`resistors=four 10KΩ pullups`；`rail=+3.3V`；`decoded_mode=null` |
| 时钟 | W5500 25MHz 时钟 | `crystal=Y1 25MHZ 12PF 10PPM`；`xo=U2 pin31 via R38 200Ω`；`xi=U2 pin30`；`feedback=R21 1MΩ`；`load_caps=C11,C17 12pF` |
| 接口 | W5500 至 RJ45 以太网 PHY | `phy=U2 W5500`；`magnetics=T1 HY601742`；`tx=TXP/TXN -> T1 -> RJ45 TX+/TX-`；`rx=RJ45 RX+/RX- -> T1 -> RXP/RXN`；`center_taps=VA1,VA2` |
| 电源 | PoE 受电模块接口 | `poe_input_header=P1 VA1,VA2,VB1,VB2`；`poe_output_header=P4 GND,VO5`；`output_label=5V@1.2A`；`series_diode=D3 SS22`；`board_rail=+5V`；`poe_converter_on_page=null` |
| GPIO 与控制信号 | W5500 活动与链路 LED | `activity=U2 pin27 -> D1 green -> R12 1KΩ -> +3.3V`；`link=U2 pin25 -> D2 yellow -> R14 1KΩ -> +3.3V`；`duplex=U2 pin26 NC` |
| 内存与 Flash | ESP32 外部 Flash/PSRAM 总线 | `psram=U5 ESP-PSRAM64H`；`flash=U6 XM25QH128BHIQ`；`shared_bus=SCS/CMD,SD0/SD0,SWP/SD3,SHD/SD2,SCK/CLK,SDI/SD1`；`supply=VDD_SDIO`；`psram_ce=GPIO16`；`psram_sclk=GPIO17`；`ce_pullup=R25 10KΩ` |
| 内存与 Flash | 16MB Flash 与 8MB PSRAM | `documented_flash=16MB`；`documented_psram=8MB`；`flash_part=XM25QH128BHIQ`；`psram_part=ESP-PSRAM64H`；`explicit_capacity_fields=false` |
| 时钟 | ESP32 40MHz 时钟 | `crystal=Y2 40M`；`pins=U3 X_P/X_N`；`series=R35 0Ω`；`load_caps=C31,C32 12pF` |
| 射频 | ESP32 Wi-Fi 天线路径 | `source=U3 LAN_IN`；`series=L1 1.2nH`；`shunt_caps=C1 3.0pF,C2 2.2pF`；`connector=E1 ANT_IPEX` |
| 接口 | 摄像头并行数据与时钟 | `y2=GPIO34`；`y3=GPIO35`；`y4=GPIO5`；`y5=GPIO32`；`y6=GPIO39`；`y7=GPIO18`；`y8=GPIO36`；`pclk=GPIO21`；`xclk=pin14 via R29 47Ω` |
| GPIO 与控制信号 | 摄像头同步与控制信号 | `href=pin9 GPIO26 with R31 10KΩ pulldown`；`pwdn=pin8 GPIO22`；`vsync=pin7 GPIO25`；`reset=pin6 GPIO2`；`sio_d=pin3 GPIO14`；`sio_c=pin5 host GPIO` |
| 电源 | 摄像头 FPC 电源 | `dvdd_core=pin10 +1.2V`；`dvdd_io=pin11 +2.8V`；`avdd=pin4 +2.8V`；`grounds=DGND/AGND`；`autofocus_pins=Y0/Y1 NC` |
| 核心器件 | 正文 OV3660 与成像性能 | `documented_model=OV3660`；`documented_resolution=3MP`；`documented_dfov=66.5deg`；`documented_pixel=1.75um x 1.75um`；`documented_formats=RAW,RGB565/555/444,YUV422/420,YCbCr422,JPEG`；`schematic_model=null` |
| 接口 | J1 Grove I2C | `pin1=IIC_SCL GPIO33`；`pin2=IIC_SDA GPIO25`；`pin3=+5V`；`pin4=GND`；`protection=D4/D5/D6 to GND` |
| 调试与烧录 | ESP32 下载接口 | `p2=pin1 GND,pin2 GPIO0,pin3 EN`；`p3=pin1 U0RX,pin2 U0TX,pin3 +3.3V`；`uart_tx=U3 U0TXD via R30 499Ω`；`uart_rx=U3 U0RXD` |
| 复位 | EN 复位与 GPIO37 用户按键 | `reset_button=S2 EN to GND`；`user_button=S1 GPIO37 to GND`；`user_pullup=R32 10KΩ to +3.3V`；`user_esd=D7 RLSD52A031V` |
| 保护电路 | Grove、按键和以太网保护 | `grove_esd=D4-D6`；`button_esd=D7`；`ethernet_isolation=T1 HY601742`；`rj45_tvs_shown=false`；`poe_frontend_protection_on_page=null` |
| 核心器件 | ESP32-D0WDQ6-V3 型号后缀 | `documented_soc=ESP32-D0WDQ6-V3`；`schematic_soc=ESP32-D0WDQ6`；`revision_confirmed=false` |
| 电源 | 正文 PoE IEEE802.3af 与 6W | `documented_standard=IEEE802.3af`；`documented_max_power=6W`；`schematic_output_label=5V@1.2A`；`pd_controller=null`；`classification=null`；`dc_dc_part=null`；`input_range=null` |
| 总线 | 正文以太网速率与协议 | `documented_speed=10/100M`；`documented_protocols=TCP,UDP,ICMP,IPv4,ARP,IGMP,PPPoE`；`firmware_version=null`；`measured_throughput=null` |
| 射频 | 正文 2.4GHz Wi-Fi 能力 | `documented_band=2.4GHz`；`documented_standard=802.11 b/g/n`；`tx_power=null`；`sensitivity=null`；`antenna_gain=null`；`certification=null` |

## 待确认事项

- `memory.documented-capacities`：正文称 Flash=16MB、PSRAM=8MB；原理图打印 U6 XM25QH128BHIQ 与 U5 ESP-PSRAM64H 型号，但没有独立 MB 容量字段。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 U5/U6 仅标料号，无容量文字）
- `component.documented-camera`：正文称摄像头为 OV3660、3MP、66.5° DFOV、1.75um 像素并支持多种 RAW/RGB/YUV/JPEG 格式和自动图像控制；原理图只显示 U4 FPC-0.5-24P，没有摄像头芯片型号或光学/成像参数。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 U4 仅标 FPC-0.5-24P，无 OV3660 或光学参数）
- `component.documented-soc-version`：正文将 SoC 标为 ESP32-D0WDQ6-V3；原理图 U3 只打印 ESP32-D0WDQ6，没有 -V3 后缀或芯片 revision 字段。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 U3 下方型号仅 ESP32-D0WDQ6）
- `power.documented-poe`：正文称支持 IEEE 802.3af、最大功耗 6W；原理图只显示 P1/P4 与 5V@1.2A 标签，没有 PoE PD 控制器、分类电阻、隔离 DC/DC 型号、输入电压范围或热设计。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 P1/P4/D3 外部 PoE 接口，未展开转换模块）
- `bus.documented-ethernet`：正文列出 10/100M 以及 TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE；原理图只确认 W5500、SPI、PHY 和 RJ45，不能证明固件协议配置、吞吐量或链路行为。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 U2/T1/RJ45，无速率或协议表）
- `rf.documented-wifi`：正文称 ESP32 支持 2.4G Wi-Fi 802.11 b/g/n；原理图只确认 ESP32 LAN_IN 匹配网络与 IPEX 接口，没有频段、协议、发射功率、灵敏度、天线增益或认证信息。（证据：图 cfb606eb8cbd / 第 1 页 / 第 1 页 U3 LAN_IN-L1-C1/C2-E1，仅硬件射频路径）
- `review.memory-capacities`：请用 U5/U6 datasheet、BOM 或实机确认 8MB PSRAM 与 16MB Flash 容量。；原因：原理图只打印器件料号，没有 MB 容量字段。
- `review.camera-model`：请用摄像头模组 BOM/丝印/datasheet 确认 U4 所接是否为 OV3660，并复核 3MP、DFOV、像素尺寸、格式与自动控制能力。；原因：本页只有 FPC 电气接口，没有摄像头型号或光学参数。
- `review.soc-revision`：请确认 U121-B-V11 量产 SoC 是否固定为 ESP32-D0WDQ6-V3。；原因：原理图省略 -V3 后缀。
- `review.poe-module`：请提供当前 PoE 子模块型号/BOM，确认 IEEE 802.3af、分类、隔离、输入范围、5V@1.2A/6W 与保护边界。；原因：PoE 转换模块本体未在本页展开。
- `review.ethernet-capabilities`：请用 W5500 datasheet、固件与链路测试确认 10/100M、协议支持和实际吞吐量。；原因：原理图不能证明协议栈配置或性能。
- `review.wifi-capabilities`：请用 ESP32 revision、天线 BOM 与射频测试确认 2.4GHz 802.11 b/g/n、功率、灵敏度、增益和认证。；原因：板级图只展示 RF 匹配与 IPEX。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cfb606eb8cbd872a4ad30698433f93d3ae445324582e94df2967c6b6695a38cf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/595/Sch_M5PoECAM-W_sch_01.png` |

---

源文档：`zh_CN/unit/M5PoECAM-W V1.1.md`

源文档 SHA-256：`068d985765e46681c7b2472529c830b5cdbe9b1f36dded1c91d187a8215d8335`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
