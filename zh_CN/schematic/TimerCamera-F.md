# TimerCamera-F 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | TimerCamera-F |
| SKU | U082-F |
| 产品 ID | `timercamera-f-964a85b1021e` |
| 源文档 | `zh_CN/unit/timercam_f.md` |

## 概述

TimerCamera-F（U082-F）以 U1 ESP32 为主控，连接 U3 ESPPSRAM64H、U4 W25Q32、U2 OV-Camera 并行摄像头、BM8563 RTC、CH552T USB-UART 和外部/Grove 接口。摄像头使用 8 位 Y2~Y9 数据、PCLK/HREF/VSYNC、XCLK、RESET 与 SIO_C/SIO_D，并由 3.3V、1.5V、2.8V 三路供电。VBAT 与 USB 经 1N5819 二极管汇合成 VSYS_VIN，SY8089AAC 生成 VCC_3V3，TP4057 为电池充电，GPIO33/RTC_ALM/按键构成电源保持与唤醒链。原理图只将主控标为 ESP32、相机标为 OV-Camera，未直接确认 ESP32-D0WDQ6-V3、OV3660、存储容量、光学性能或 270mAh 电池。

## 检索关键词

`TimerCamera-F`、`U082-F`、`ESP32`、`ESPPSRAM64H`、`W25Q32`、`OV-Camera`、`BM8563`、`CH552T`、`SY8089AAC`、`TP4057`、`HX6306P152`、`HX6306P282`、`camera DVP`、`SIO_C`、`SIO_D`、`PCLK`、`XCLK`、`VSYNC`、`HREF`、`Y2-Y9`、`GPIO23`、`GPIO25`、`GPIO27`、`GPIO22`、`GPIO26`、`GPIO21`、`GPIO15`、`PROANT_440`、`IPEX`、`USB-TYPEC`、`PH2.0_4P_SMT`、`RTC_ALM`、`PWR_EN`、`VBAT`、`VSYS_VIN`、`VCC_3V3`、`VCC_1V5`、`VCC_2V8`、`GPIO38 BAT_ADC`、`GPIO33 BAT_HOLD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 主控 SoC，连接摄像头、外部存储、PSRAM、RTC、USB-UART、RF、LED 与电源控制 | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 A1:B1 U1 ESP32，GPIO0~39、SD_DATA/CLK/CMD、晶振、UART 与电源引脚 |
| U2 | OV-Camera | 并行 DVP 摄像头模块，连接 8 位像素数据、同步、时钟、SCCB、复位和三路电源 | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 A3:C3 U2 OV-Camera pins 1~24，Y2~Y9/PCLK/XCLK/HREF/VSYNC/RESET/SIO_C/SIO_D |
| U3 | ESPPSRAM64H | 外部 Quad PSRAM，连接 SD_DATA0~3、GPIO16 片选与 GPIO17 时钟 | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 C2 U3 ESPPSRAM64H，nCS/SI-SIO0/SO-SIO1/SIO2/SIO3/SCLK |
| U4 | W25Q32 | 外部 Quad SPI Flash，连接 SD_CMD、SD_CLK 与 SD_DATA0~3 | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 D2 U4 W25Q32 与 SD_CMD/SD_CLK/SD_DATA0~3 |
| ANT1/J1 | PROANT_440/IPEX | 板载天线与可选 IPEX 射频路径 | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 A2 ESP_LNA、TBD 匹配、R2 0Ω 到 ANT1 PROANT_440、R3 DNP 到 J1 IPEX |
| J2 | PH2.0_4P_SMT | 四针 GPIO13/GPIO4/VSYS_VIN/GND 扩展接口，信号带 22Ω 与 ESD | 图 d59e37772926 / 第 1 页 / 第 1 张第 1 页 C4 J2 pins 1~4、R7/R8 22Ω、D1/D2 3.3V/ESD |
| U5 | SY8089AAC | VSYS_VIN 到 VCC_3V3 的同步降压转换器 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 A1:A2 U5 SY8089AAC、L2 2.2uH、R14/R15、C24/C25 |
| U6 | BM8563 | 低功耗 RTC，SCL/SDA 接 GPIO14/GPIO12，INT 输出 RTC_ALM | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 A3 U6 BM8563、Y1/C23/C28、GPIO14/GPIO12/RTC_ALM/VBAT_IN |
| U7 | CH552T | USB 到 ESP32 UART/自动下载辅助控制器 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 A2:B3 U7 CH552T，USB_DP/USB_DM、CH552_TXD/RXD、GPIO0_IN/ESP32_EN_IN |
| J3 | USB-TYPEC | USB-C 电源与 USB D+/D- 接口，CC1/CC2 各 5.1KΩ 下拉 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 B3 J3 USB-TYPEC、R22/R23 5.1KΩ、USB_DP/USB_DM/VUSB_VCC |
| U8/U9 | HX6306P152/1.5V LDO 300mA; HX6306P282/2.8V LDO 300mA | 从 VCC_3V3 生成摄像头 VCC_1V5 与 VCC_2V8 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 C3:D4 U8/U9 与 VCC_3V3/VCC_1V5/VCC_2V8 |
| U11 | TP4057 | VUSB_VCC 到 VBAT_IN 的锂电池充电器 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 D2 U11 TP4057，VCC/BAT/PROG/GND、R30 5.1KΩ、C36/C40 |
| J4 | SMT_HDR_2x1.25mm | 两针 VBAT_IN/GND 电池连接器 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 B2 J4 pin2 VBAT_IN、pin1 GND |
| FET1-FET4 | CJ2302/CJ2301 | USB 自动下载、ESP32 EN 与电池电源保持控制 MOSFET | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 A1:B1 FET1/FET2 CJ2302 与 C1:C2 FET3 CJ2301 PMOS/FET4 CJ2302 NMOS |
| S1/S2 | SMT_SW_TS_015/SMT_SW_PTS_820 | 用户电源按键与 ESP32 复位按键 | 图 6f41535b5573 / 第 1 页 / 第 2 张第 1 页 C2 S1 USER_SWC 与 D1 S2 ESP32_EN 到 GND |

## 系统结构

### TimerCamera-F 系统架构

U1 ESP32 连接 U3 PSRAM、U4 Flash、U2 摄像头、BM8563 RTC、CH552T USB-UART、RF 天线、Grove、LED 与多级电源/电池管理。

- 参数与网络：`controller=U1 ESP32`；`camera=U2 OV-Camera`；`psram=U3 ESPPSRAM64H`；`flash=U4 W25Q32`；`rtc=U6 BM8563`；`usb_uart=U7 CH552T`；`power=VBAT/VUSB -> VSYS_VIN -> U5 VCC_3V3 -> U8/U9 camera rails`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张完整主控/存储/摄像头/RF/Grove; 图 6f41535b5573 / 第 1 页 / 第 2 张完整电源/RTC/USB/电池/控制

## 电源

### 摄像头三路电源

U2 DOVDD 接 VCC_3V3、DVDD 接 VCC_1V5、AVDD 接 VCC_2V8；U8/U9 从 VCC_3V3 分别生成 1.5V 和 2.8V。

- 参数与网络：`dovdd=VCC_3V3`；`dvdd=VCC_1V5 via U8 HX6306P152`；`avdd=VCC_2V8 via U9 HX6306P282`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 U2 DOVDD/DVDD/AVDD; 图 6f41535b5573 / 第 1 页 / 第 2 张 U8/U9 3.3V to 1.5V/2.8V LDO

### VBAT/VUSB 电源汇合

VBAT 经 D6 1N5819、VUSB_VCC 经 D8 1N5819 汇合为 VSYS_VIN，C43/C44 各 10uF 对地。

- 参数与网络：`battery=VBAT -> D6 1N5819`；`usb=VUSB_VCC -> D8 1N5819`；`output=VSYS_VIN`；`capacitors=C43,C44 10uF`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 C2 D6/D8/VSYS_VIN/C43/C44

### VSYS_VIN 到 VCC_3V3

U5 SY8089AAC、L2 2.2uH、R14 11.5KΩ/R15 2.55KΩ 与 C24/C25 22uF 构成 VCC_3V3 降压电源。

- 参数与网络：`input=VSYS_VIN`；`converter=U5 SY8089AAC`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 11.5KΩ,R15 2.55KΩ`；`output=VCC_3V3`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 A1:A2 U5/L2/R14/R15/C24/C25

### 电池充电路径

U11 TP4057 从 VUSB_VCC 充电到 VBAT_IN，BAT pin3 接 VBAT_IN，PROG pin6 经 R30 5.1KΩ 接 GND，J4 引出 VBAT_IN/GND。

- 参数与网络：`input=VUSB_VCC`；`charger=U11 TP4057`；`battery_net=VBAT_IN`；`program=R30 5.1KΩ`；`connector=J4 pin2 VBAT_IN,pin1 GND`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 B2/D2 J4 与 U11 TP4057

### 电源保持与唤醒

FET3 CJ2301 PMOS 控制 VBAT 到 VBAT_IN，FET4 CJ2302 由 GPIO33 控制 PWR_EN；RTC_ALM、GPIO37 与 USER_SWC 通过 D3/D4/D5 1N4148 汇合到 PWR_EN。

- 参数与网络：`high_side=FET3 CJ2301`；`hold=GPIO33 -> FET4 -> PWR_EN`；`wake_sources=RTC_ALM via D3,GPIO37 via D4,USER_SWC via D5`；`button=S1`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 C1:C2 FET3/FET4/D3-D5/S1/PWR_EN

## 接口

### J2 HY2.0-4P

J2 pin1 经 R7 22Ω 接 GPIO13 并有 D1 3.3V/ESD，pin2 经 R8 22Ω 接 GPIO4 并有 D2 3.3V/ESD，pin3 为 VSYS_VIN，pin4 为 GND。

- 参数与网络：`pin_1=GPIO13 via 22Ω and ESD`；`pin_2=GPIO4 via 22Ω and ESD`；`pin_3=VSYS_VIN`；`pin_4=GND`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 C4 J2/R7/R8/D1/D2

## 总线

### 摄像头 8 位并行像素总线

U2 Y2~Y9 分别连接 GPIO32、GPIO35、GPIO34、GPIO5、GPIO39、GPIO18、GPIO36、GPIO19，PCLK 连接 GPIO21。

- 参数与网络：`Y2=GPIO32`；`Y3=GPIO35`；`Y4=GPIO34`；`Y5=GPIO5`；`Y6=GPIO39`；`Y7=GPIO18`；`Y8=GPIO36`；`Y9=GPIO19`；`PCLK=GPIO21 via R36 47Ω`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 B3 U2 Y2~Y9/PCLK 与 GPIO 网络

### 摄像头同步与 SCCB 控制

XCLK/HREF/VSYNC/RESET 分别连接 GPIO27/GPIO26/GPIO22/GPIO15；SIO_C/SIO_D 分别连接 GPIO23/GPIO25，并由 R32/R33 2KΩ 上拉到 VCC_3V3。

- 参数与网络：`xclk=GPIO27 via R37 47Ω`；`href=GPIO26`；`vsync=GPIO22`；`reset=GPIO15`；`sioc=GPIO23,R32 2KΩ pullup`；`siod=GPIO25,R33 2KΩ pullup`；`pwdn=R4 10KΩ to GND`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 B3:C3 U2 XCLK/HREF/VSYNC/RESET/SIO_C/SIO_D/PWDN

### BM8563 RTC 总线与中断

U6 BM8563 SCL/SDA 分别接 GPIO14/GPIO12，INT pin3 输出 RTC_ALM，VDD pin8 接 VBAT_IN。

- 参数与网络：`scl=GPIO14`；`sda=GPIO12`；`interrupt=RTC_ALM`；`supply=VBAT_IN`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 A3 U6 BM8563

### CH552T USB-UART

J3 USB_DP/USB_DM 接 U7 CH552T；CH552_TXD 经 R19 1KΩ 接 ESP32 U0RXD，CH552_RXD 经 R20 1KΩ 接 ESP32 U0TXD。

- 参数与网络：`usb=J3 USB_DP/USB_DM -> U7`；`to_esp_rx=CH552_TXD-R19-U0RXD`；`from_esp_tx=U0TXD-R20-CH552_RXD`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 A2:B3 U7/J3/R19/R20

## GPIO 与控制信号

### 状态 LED

GPIO2 驱动 LED1 BLUE，LED 下端经 R31 470Ω 接 GND。

- 参数与网络：`gpio=GPIO2`；`led=LED1 BLUE`；`resistor=R31 470Ω to GND`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 A4 GPIO2-LED1 BLUE-R31-GND

## 时钟

### RTC 32kHz 晶振

BM8563 OSCI/OSCO 连接 Y1 TXC/9H0320，C23/C28 各 7pF 对地。

- 参数与网络：`rtc=U6 BM8563`；`crystal=Y1 TXC/9H0320`；`load_caps=C23,C28 7pF`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 A3 U6/Y1/C23/C28

## 复位

### ESP32 EN/复位

ESP32_EN 由 R27 10KΩ 上拉到 VCC_3V3，S2 可将其拉低，D9 提供 3.3V ESD；FET2/CH552T 也可控制 ESP32_EN_IN。

- 参数与网络：`pullup=R27 10KΩ`；`button=S2 to GND`；`protection=D9 3.3V/ESD`；`auto_download=FET2 CJ2302 via CH552T`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 B1/D1 ESP32_EN/FET2/R27/S2/D9

## 保护电路

### Grove 与按键保护

Grove GPIO13/GPIO4 各有 22Ω 串联与 3.3V ESD 二极管，USER_SWC 与 ESP32_EN 也分别有 D7/D9 3.3V ESD。

- 参数与网络：`grove=R7/R8 22Ω,D1/D2 ESD`；`power_button=D7 ESD`；`reset=D9 ESD`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 C4 Grove ESD; 图 6f41535b5573 / 第 1 页 / 第 2 张 C2/D1 D7/D9

## 存储

### W25Q32 Quad Flash

U4 W25Q32 使用 SD_CMD 片选、SD_CLK 时钟和 SD_DATA0~3 Quad 数据线，由 VDD_SDIO 供电。

- 参数与网络：`chip_select=SD_CMD`；`clock=SD_CLK via R10 200Ω`；`data=SD_DATA0-3`；`supply=VDD_SDIO`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 D2 U4 W25Q32 与 SD_CMD/SD_CLK/SD_DATA0~3

## 内存与 Flash

### ESPPSRAM64H Quad PSRAM

U3 使用 SD_DATA0~3 数据线，GPIO16 作为 nCS 并由 R5 10KΩ 上拉到 VDD_SDIO，GPIO17 经 R6 200Ω 驱动 SCLK。

- 参数与网络：`data=SD_DATA0-3`；`chip_select=GPIO16 nCS,R5 10KΩ to VDD_SDIO`；`clock=GPIO17-R6 200Ω-SCLK`；`supply=VDD_SDIO`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 C2 U3 ESPPSRAM64H 与 R5/R6/SD_DATA0~3

## 射频

### ESP32 天线网络

ESP_LNA 经 TBD 匹配网络后通过 R2 0Ω 接 ANT1 PROANT_440；到 J1 IPEX 的 R3 标 DNP，因此图示默认为板载天线路径。

- 参数与网络：`source=ESP_LNA`；`matching=L1/C1/C3 TBD`；`onboard=R2 0Ω -> ANT1 PROANT_440`；`external=R3 DNP -> J1 IPEX`
- 证据：图 d59e37772926 / 第 1 页 / 第 1 张 A2 ESP_LNA 匹配与 ANT1/J1

## 模拟电路

### 电池电压 ADC

VBAT 通过 R28 1.37KΩ 与 R29 2.67KΩ 分压，中心节点连接 GPIO38。

- 参数与网络：`source=VBAT`；`upper=R28 1.37KΩ`；`lower=R29 2.67KΩ to GND`；`adc=GPIO38`
- 证据：图 6f41535b5573 / 第 1 页 / 第 2 张 D2 VBAT-R28-GPIO38-R29-GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | TimerCamera-F 系统架构 | `controller=U1 ESP32`；`camera=U2 OV-Camera`；`psram=U3 ESPPSRAM64H`；`flash=U4 W25Q32`；`rtc=U6 BM8563`；`usb_uart=U7 CH552T`；`power=VBAT/VUSB -> VSYS_VIN -> U5 VCC_3V3 -> U8/U9 camera rails` |
| 内存与 Flash | ESPPSRAM64H Quad PSRAM | `data=SD_DATA0-3`；`chip_select=GPIO16 nCS,R5 10KΩ to VDD_SDIO`；`clock=GPIO17-R6 200Ω-SCLK`；`supply=VDD_SDIO` |
| 存储 | W25Q32 Quad Flash | `chip_select=SD_CMD`；`clock=SD_CLK via R10 200Ω`；`data=SD_DATA0-3`；`supply=VDD_SDIO` |
| 总线 | 摄像头 8 位并行像素总线 | `Y2=GPIO32`；`Y3=GPIO35`；`Y4=GPIO34`；`Y5=GPIO5`；`Y6=GPIO39`；`Y7=GPIO18`；`Y8=GPIO36`；`Y9=GPIO19`；`PCLK=GPIO21 via R36 47Ω` |
| 总线 | 摄像头同步与 SCCB 控制 | `xclk=GPIO27 via R37 47Ω`；`href=GPIO26`；`vsync=GPIO22`；`reset=GPIO15`；`sioc=GPIO23,R32 2KΩ pullup`；`siod=GPIO25,R33 2KΩ pullup`；`pwdn=R4 10KΩ to GND` |
| 电源 | 摄像头三路电源 | `dovdd=VCC_3V3`；`dvdd=VCC_1V5 via U8 HX6306P152`；`avdd=VCC_2V8 via U9 HX6306P282` |
| 接口 | J2 HY2.0-4P | `pin_1=GPIO13 via 22Ω and ESD`；`pin_2=GPIO4 via 22Ω and ESD`；`pin_3=VSYS_VIN`；`pin_4=GND` |
| 射频 | ESP32 天线网络 | `source=ESP_LNA`；`matching=L1/C1/C3 TBD`；`onboard=R2 0Ω -> ANT1 PROANT_440`；`external=R3 DNP -> J1 IPEX` |
| GPIO 与控制信号 | 状态 LED | `gpio=GPIO2`；`led=LED1 BLUE`；`resistor=R31 470Ω to GND` |
| 电源 | VBAT/VUSB 电源汇合 | `battery=VBAT -> D6 1N5819`；`usb=VUSB_VCC -> D8 1N5819`；`output=VSYS_VIN`；`capacitors=C43,C44 10uF` |
| 电源 | VSYS_VIN 到 VCC_3V3 | `input=VSYS_VIN`；`converter=U5 SY8089AAC`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 11.5KΩ,R15 2.55KΩ`；`output=VCC_3V3` |
| 电源 | 电池充电路径 | `input=VUSB_VCC`；`charger=U11 TP4057`；`battery_net=VBAT_IN`；`program=R30 5.1KΩ`；`connector=J4 pin2 VBAT_IN,pin1 GND` |
| 模拟电路 | 电池电压 ADC | `source=VBAT`；`upper=R28 1.37KΩ`；`lower=R29 2.67KΩ to GND`；`adc=GPIO38` |
| 电源 | 电源保持与唤醒 | `high_side=FET3 CJ2301`；`hold=GPIO33 -> FET4 -> PWR_EN`；`wake_sources=RTC_ALM via D3,GPIO37 via D4,USER_SWC via D5`；`button=S1` |
| 总线 | BM8563 RTC 总线与中断 | `scl=GPIO14`；`sda=GPIO12`；`interrupt=RTC_ALM`；`supply=VBAT_IN` |
| 时钟 | RTC 32kHz 晶振 | `rtc=U6 BM8563`；`crystal=Y1 TXC/9H0320`；`load_caps=C23,C28 7pF` |
| 总线 | CH552T USB-UART | `usb=J3 USB_DP/USB_DM -> U7`；`to_esp_rx=CH552_TXD-R19-U0RXD`；`from_esp_tx=U0TXD-R20-CH552_RXD` |
| 复位 | ESP32 EN/复位 | `pullup=R27 10KΩ`；`button=S2 to GND`；`protection=D9 3.3V/ESD`；`auto_download=FET2 CJ2302 via CH552T` |
| 保护电路 | Grove 与按键保护 | `grove=R7/R8 22Ω,D1/D2 ESD`；`power_button=D7 ESD`；`reset=D9 ESD` |
| 核心器件 | ESP32 完整型号 | `schematic=ESP32`；`candidate_from_product_doc=ESP32-D0WDQ6-V3`；`confirmed_suffix=null` |
| 核心器件 | 摄像头完整型号 | `schematic=OV-Camera`；`candidate_from_product_doc=OV3660`；`lens=null`；`fisheye=null` |
| 内存与 Flash | PSRAM 与 Flash 容量 | `psram_part=ESPPSRAM64H`；`flash_part=W25Q32`；`psram_capacity_field=null`；`flash_capacity_field=null`；`candidate_from_product_doc=8MB PSRAM,4MB Flash` |
| 传感器 | 摄像头光学与成像性能 | `megapixels=null`；`maximum_resolution=null`；`dfov=null`；`formats=null`；`compression=null` |
| 电源 | 电池容量与低功耗性能 | `battery_capacity=null`；`sleep_current=null`；`timed_capture_endurance=null` |

## 待确认事项

- `component.esp32-full-model`：原理图只将 U1 标为 ESP32，没有显示 D0WDQ6-V3 后缀，因此不能仅凭图纸确认完整芯片型号。（证据：图 d59e37772926 / 第 1 页 / 第 1 张 U1 下方型号仅 ESP32）
- `component.camera-model`：原理图只将 U2 标为 OV-Camera，没有出现 OV3660 型号、镜头或鱼眼版本。（证据：图 d59e37772926 / 第 1 页 / 第 1 张 U2 下方型号 OV-Camera）
- `memory.capacity`：原理图给出 ESPPSRAM64H 与 W25Q32 型号，但未以容量字段明确标注 8MB PSRAM 和 4MB Flash。（证据：图 d59e37772926 / 第 1 页 / 第 1 张 U3/U4 型号文字与总线连接，无容量注释）
- `sensor.camera-performance`：原理图未标注 3MP、2048x1536、DFOV 120°、RAW/RGB/YCbCr 格式或图像压缩能力。（证据：图 d59e37772926 / 第 1 页 / 第 1 张 U2 OV-Camera 仅电气引脚，无成像性能文字）
- `power.battery-performance`：原理图显示电池、RTC 与电源保持/充电路径，但未标注 270mAh、2uA 休眠电流或每小时拍照续航。（证据：图 6f41535b5573 / 第 1 页 / 第 2 张完整 VBAT/RTC/充电/电源保持电路，无容量或功耗注释）
- `review.esp32-full-model`：U1 的完整订货型号是否为 ESP32-D0WDQ6-V3？；原因：原理图仅标 ESP32，需 BOM 或实物确认后缀。
- `review.camera-model`：U2 实装传感器是否为 OV3660，鱼眼镜头/DFOV 的准确料号是什么？；原因：原理图只写 OV-Camera。
- `review.memory-capacity`：ESPPSRAM64H 与 W25Q32 在本板上的可用容量是否分别为 8MB 和 4MB？；原因：图纸只有器件型号，没有容量字段或地址空间说明。
- `review.camera-performance`：实际摄像头的分辨率、DFOV、输出格式与压缩能力是什么？；原因：这些光学/成像参数未出现在原理图。
- `review.battery-performance`：电池实际容量、休眠电流和定时拍摄续航分别是多少？；原因：原理图确认电源结构但不提供整机性能。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d59e377729269ff9861c98e94ea64c868010a7c625075e734628b2cae40d4c33` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1041/Sch_M5TimerCAM_page_01.png` |
| 2 | 1 | `6f41535b5573e4bb7000ff81b2558046dbfdc208c6f3b55c810658823d28749b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1041/Sch_M5TimerCAM_page_02.png` |

---

源文档：`zh_CN/unit/timercam_f.md`

源文档 SHA-256：`13cd587883c79e3b6c88cd554fe32d0c83e4500fcf1386aa60255cc30eee4113`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
