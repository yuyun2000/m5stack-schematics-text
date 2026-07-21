# TimerCamera 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | TimerCamera |
| SKU | U082 |
| 产品 ID | `timercamera-56ad239d7994` |
| 源文档 | `zh_CN/unit/timercam.md` |

## 概述

TimerCamera 以 U1 ESP32 为主控，连接 U2 OV-Camera 并行接口、U3 ESPSRAM64H、U4 W25Q32、40MHz 晶振、GPIO2 蓝灯、Grove 和 Proant_440/IPEX 可选射频路径。第二页由 U7 CH552T 提供 USB 下载/UART桥接，U6 BM8563 提供 RTC_ALM 定时唤醒，U11 TP4057 管理电池充电，FET3/FET4 与二极管网络实现电池电源保持。VUSB/VBAT 经 D8/D6 或接为 VSYS_VIN，U5 SY8089AAC 生成 3.3V，U8/U9 再生成摄像头 1.5V/2.8V。

## 检索关键词

`TimerCamera`、`U082`、`ESP32`、`ESP32-D0WDQ6-V3`、`OV-Camera`、`OV3660`、`ESPSRAM64H`、`W25Q32`、`CH552T`、`BM8563`、`TP4057`、`SY8089AAC`、`HX6306P152`、`HX6306P282`、`VCC_3V3`、`VCC_1V5`、`VCC_2V8`、`VSYS_VIN`、`VBAT_IN`、`VUSB_VCC`、`RTC_ALM`、`GPIO33`、`GPIO37`、`GPIO38`、`GPIO13`、`GPIO4`、`USB_DP`、`USB_DM`、`U0TXD`、`U0RXD`、`ANT1 PROANT_440`、`J1 IPEX`、`40MHz`、`FPC camera`、`SCCB`、`power hold`、`battery charger`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 主控 SoC，连接摄像头、存储、RF、RTC、Grove、UART、LED 与电源控制 | 图 d59e37772926 / 第 1 页 / 页面 1 A1-B2 U1 ESP32 全部 GPIO、电源、SDIO、UART、RF 和时钟引脚 |
| U2 | OV-Camera | 24 针并行摄像头接口/模组符号，连接像素总线、SCCB、同步与三路电源 | 图 d59e37772926 / 第 1 页 / 页面 1 A4-C4 U2 OV-Camera pins1-24 |
| U3 | ESPSRAM64H | VDD_SDIO 供电的外部 PSRAM | 图 d59e37772926 / 第 1 页 / 页面 1 C2-C3 U3 ESPSRAM64H 与 GPIO16/GPIO17/SD_DATA* |
| U4 | W25Q32 | VDD_SDIO 供电的外部串行 Flash | 图 d59e37772926 / 第 1 页 / 页面 1 D2-D3 U4 W25Q32 与 SD_CMD/SD_CLK/SD_DATA* |
| X1 | TXC/8Z40000017 | ESP32 XTAL_P/XTAL_N 外部 40MHz 晶振 | 图 d59e37772926 / 第 1 页 / 页面 1 C1 X1 TXC/8Z40000017、R35 100R、C17/C18 12pF |
| ANT1/J1 | PROANT_440 / IPEX | ESP_LNA 的默认板载天线与 DNP 可选 IPEX 射频接口 | 图 d59e37772926 / 第 1 页 / 页面 1 A2-A3 ESP_LNA 匹配网络、R2 0R-ANT1 PROANT_440 与 R3 DNP-J1 IPEX |
| J2 | PH2.0_4P_SMT | GPIO13/GPIO4、VSYS_VIN、GND 的四针扩展接口 | 图 d59e37772926 / 第 1 页 / 页面 1 C4-D4 J2 PH2.0_4P_SMT 与 R7/R8、D1/D2 |
| LED1 | 蓝灯 | GPIO2 驱动的状态指示灯 | 图 d59e37772926 / 第 1 页 / 页面 1 A4 GPIO2-LED1 蓝灯-R31 470R-GND |
| U5 | SY8089AAC | 将 VSYS_VIN 降压为 VCC_3V3 | 图 6f41535b5573 / 第 1 页 / 页面 2 A1-A2 U5 SY8089AAC、L2、R14/R15、C24/C25 |
| U6 | BM8563 | 电池域供电的 RTC，通过 GPIO14/GPIO12 I2C 并输出 RTC_ALM | 图 6f41535b5573 / 第 1 页 / 页面 2 A3-A4 U6 BM8563、Y1、GPIO14/GPIO12、RTC_ALM、VBAT_IN |
| U7 | CH552T | USB 设备、ESP32 UART 桥接及 GPIO0/EN 自动下载控制器 | 图 6f41535b5573 / 第 1 页 / 页面 2 A2-B3 U7 CH552T、USB_DP/DM、CH552_TXD/RXD、GPIO0_IN/ESP32_EN_IN |
| U8/U9 | HX6306P152/1.5V LDO 300mA / HX6306P282/2.8V LDO 300mA | 由 VCC_3V3 生成摄像头 VCC_1V5 与 VCC_2V8 | 图 6f41535b5573 / 第 1 页 / 页面 2 C3-D4 U8/U9 及 C33/C34/C41/C37/C38/C42 |
| U11 | TP4057 | VUSB_VCC 输入到 VBAT_IN 的单节电池充电器 | 图 6f41535b5573 / 第 1 页 / 页面 2 C2-D3 U11 TP4057、R30 5.1K、C36/C40、VBAT_IN |
| J3 | USB-TYPEC | USB VBUS、DP/DM 与 CC 下拉接口 | 图 6f41535b5573 / 第 1 页 / 页面 2 B2-B3 J3 USB-TYPEC、R22/R23 5.1K、USB_DP/USB_DM/VUSB_VCC |
| J4 | SMT_HDR_2x1.25mm | VBAT_IN 与 GND 的两针电池接口 | 图 6f41535b5573 / 第 1 页 / 页面 2 C2 J4 pin2 VBAT_IN、pin1 GND |
| FET3/FET4 | CJ2301/PMOS / CJ2302-NMOS | VBAT_IN 到 VBAT 的高侧电源保持与 GPIO33 控制下拉 | 图 6f41535b5573 / 第 1 页 / 页面 2 C1-C2 FET3/FET4、PWR_EN、GPIO33、R25/R26 与 D3-D5 |
| FET1/FET2 | CJ2302 / CJ2302 | CH552T 对 ESP32 GPIO0 与 EN 的自动下载开漏控制 | 图 6f41535b5573 / 第 1 页 / 页面 2 A1-B1 FET1/FET2、GPIO0_IN/ESP32_EN_IN 与 R12/R17 |
| U10/S2 | Reset supervisor / SMT_SW_PTS_820 | ESP32_EN 上拉、手动复位及对地 ESD 保护 | 图 6f41535b5573 / 第 1 页 / 页面 2 D1-D2 U10、R27 10K、S2、D9 与 ESP32_EN |

## 系统结构

### TimerCamera

U1 ESP32 连接 U2 摄像头、U3 PSRAM、U4 Flash、RF 天线、Grove 和 LED；U7 CH552T 负责 USB/UART 下载控制，U6 BM8563 提供 RTC 唤醒，U11 与 FET3/FET4 构成电池充电和保持电源。

- 参数与网络：`controller=U1 ESP32`；`camera=U2 OV-Camera`；`memory=U3 ESPSRAM64H,U4 W25Q32`；`usb_bridge=U7 CH552T`；`rtc=U6 BM8563`；`charger=U11 TP4057`；`power_hold=FET3/FET4`；`rails=VCC_3V3,VCC_1V5,VCC_2V8`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 全页 ESP32/摄像头/存储/RF/Grove; 图 6f41535b5573 / 第 1 页 / 页面 2 全页 USB/RTC/电池/电源管理

## 电源

### 摄像头三路电源

U2 DOVDD pin 11 使用 VCC_3V3，DVDD pin 10 使用 VCC_1V5，AVDD pin 4 使用 VCC_2V8，DGND/AGND 接 GND。

- 参数与网络：`DOVDD=pin11 VCC_3V3`；`DVDD=pin10 VCC_1V5`；`AVDD=pin4 VCC_2V8`；`DGND=pin15 GND`；`AGND=pin2 GND`；`pin1=NC`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 U2 pins1/2/4/10/11/15 电源与地

### VBAT/VUSB 到 VSYS_VIN

VBAT 经 D6 1N5819、VUSB_VCC 经 D8 1N5819 汇合到 VSYS_VIN，实现电池与 USB 的肖特基或接供电；C43/C44 各 10uF 从 VSYS_VIN 接 GND。

- 参数与网络：`battery_path=VBAT -> D6 1N5819 -> VSYS_VIN`；`usb_path=VUSB_VCC -> D8 1N5819 -> VSYS_VIN`；`bulk_caps=C43,C44 10uF to GND`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 C2-C3 D6/D8、VSYS_VIN、C43/C44

### U5 SY8089AAC

VSYS_VIN 连接 U5 IN pin 4 与 EN pin 1，LX pin 3 经 L2 WPN3012H2R2MT 输出 VCC_3V3；R14 11.5K/R15 2.55K 构成反馈，C24/C25 各 22uF。

- 参数与网络：`input=VSYS_VIN`；`converter=U5 SY8089AAC`；`enable=pin1 tied VSYS_VIN`；`inductor=L2 WPN3012H2R2MT`；`output=VCC_3V3`；`feedback=R14 11.5K 1%,R15 2.55K 1%`；`output_caps=C24,C25 22uF/6.3V`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 A1-A2 U5/L2/R14/R15/C24/C25

### U8/U9 摄像头 LDO

U8 HX6306P152 由 VCC_3V3 生成 VCC_1V5，U9 HX6306P282 由 VCC_3V3 生成 VCC_2V8；两者均标注 LDO 300mA 并配置输入/输出电容。

- 参数与网络：`core_ldo=U8 HX6306P152/1.5V LDO 300mA`；`analog_ldo=U9 HX6306P282/2.8V LDO 300mA`；`input=VCC_3V3`；`outputs=VCC_1V5,VCC_2V8`；`u8_caps=C33 4.7uF,C34 4.7uF,C41 22uF`；`u9_caps=C37 4.7uF,C38 4.7uF,C42 22uF`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 C3-D4 U8/U9 与 VCC_1V5/VCC_2V8 电容

### U11 TP4057

U11 VCC pin 4 接 VUSB_VCC，BAT pin 3 输出 VBAT_IN，PROG pin 6 经 R30 5.1K 接 GND；CHRG/STDBY pins1/5 未连接，C36/C40 分别为输入/电池端电容。

- 参数与网络：`charger=U11 TP4057`；`input=pin4 VUSB_VCC`；`battery_output=pin3 VBAT_IN`；`program=pin6 R30 5.1K to GND`；`status=pins1/5 NC`；`caps=C36 4.7uF,C40 10uF`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 C2-D3 U11 TP4057、R30、C36/C40

### FET3/FET4 电源保持

FET3 CJ2301/PMOS 位于 VBAT_IN 到 VBAT 高侧路径，PWR_EN 控制其栅极；FET4 CJ2302-NMOS 由 GPIO33 控制并可下拉 PWR_EN，RTC_ALM、GPIO37 与 USER_SVC 通过 D3/D4/D5 二极管网络参与启动/保持。

- 参数与网络：`high_side=FET3 CJ2301/PMOS VBAT_IN-to-VBAT`；`gate=PWR_EN with R25 100K`；`hold_transistor=FET4 CJ2302-NMOS`；`hold_gpio=GPIO33 with R26 100K pulldown`；`wake_sources=RTC_ALM,GPIO37,USER_SVC via D3/D4/D5 1N4148`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 C1-C2 FET3/FET4、PWR_EN、GPIO33、RTC_ALM/GPIO37/USER_SVC、D3-D5

## 接口

### U2 并行像素总线

U2 Y2/Y3/Y4/Y5/Y6/Y7/Y8/Y9 分别连接 GPIO32/GPIO35/GPIO34/GPIO5/GPIO39/GPIO18/GPIO36/GPIO19；PCLK 经 R36 47R 接 GPIO21，XCLK 经 R37 47R 接 GPIO27。

- 参数与网络：`Y2=pin19 GPIO32`；`Y3=pin21 GPIO35`；`Y4=pin22 GPIO34`；`Y5=pin20 GPIO5`；`Y6=pin18 GPIO39`；`Y7=pin16 GPIO18`；`Y8=pin14 GPIO36`；`Y9=pin12 GPIO19`；`PCLK=pin17 GPIO21 via R36 47R`；`XCLK=pin13 GPIO27 via R37 47R`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 A4-C4 U2 pins12-22 与 GPIO 标签

### J2 PH2.0_4P_SMT

J2 pin 1 经 R7 22R 接 GPIO13 并有 D1 3.3V/ESD 对地，pin 2 经 R8 22R 接 GPIO4 并有 D2 3.3V/ESD 对地，pin 3 接 VSYS_VIN，pin 4 接 GND。

- 参数与网络：`pin_1=GPIO13 via R7 22R, D1 ESD`；`pin_2=GPIO4 via R8 22R, D2 ESD`；`pin_3=VSYS_VIN`；`pin_4=GND`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 C4-D4 J2、R7/R8、D1/D2 与 GPIO13/GPIO4/VSYS_VIN/GND

### J3 USB Type-C

J3 VCC/VBUS 形成 VUSB_VCC，A6/B6 接 USB_DP，A7/B7 接 USB_DM，CC1/CC2 分别经 R22/R23 5.1K 接 GND，屏蔽和地接 GND。

- 参数与网络：`VBUS=VUSB_VCC`；`DP=USB_DP`；`DM=USB_DM`；`CC1=R22 5.1K to GND`；`CC2=R23 5.1K to GND`；`shield=GND`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 B2-B3 J3 USB-TYPEC 与 R22/R23

## 总线

### 摄像头 SCCB/同步控制

U2 SIO_C pin 5 接 GPIO23、SIO_D pin 3 接 GPIO25，并分别由 R32/R33 2K 上拉到 VCC_3V3；HREF pin 9 接 GPIO26，VSYNC pin 7 接 GPIO22，RESET pin 6 接 GPIO15，PWDN pin 8 经 R4 10K 下拉。

- 参数与网络：`SIO_C=pin5 GPIO23, R32 2K pullup`；`SIO_D=pin3 GPIO25, R33 2K pullup`；`HREF=pin9 GPIO26`；`VSYNC=pin7 GPIO22`；`RESET=pin6 GPIO15`；`PWDN=pin8 R4 10K to GND`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 B4-C4 U2 control pins 与 R4/R32/R33

### U7 CH552T USB/UART

U7 USB_DP pin 14 与 USB_DM pin 15 接 J3；CH552_TXD pin 9 经 R19 1K 接 ESP32 U0RXD，CH552_RXD pin 10 经 R20 1K 接 ESP32 U0TXD，并由 R34 10K 偏置到 VCC_3V3。

- 参数与网络：`usb_dp=U7 pin14 USB_DP`；`usb_dm=U7 pin15 USB_DM`；`bridge_tx=U7 pin9 CH552_TXD via R19 1K to U0RXD`；`bridge_rx=U7 pin10 CH552_RXD via R20 1K to U0TXD`；`bias=R34 10K to VCC_3V3`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 A2-B3 U7 USB/UART 与 R19/R20/R34

### U6 BM8563

U6 SCL pin 6 接 GPIO14，SDA pin 5 接 GPIO12，INT pin 3 输出 RTC_ALM；VDD pin 8 接 VBAT_IN，VSS pin 4 接 GND，CLKOUT pin 7 未连接。

- 参数与网络：`controller=U1 ESP32`；`SCL=U6 pin6 GPIO14`；`SDA=U6 pin5 GPIO12`；`interrupt=U6 pin3 RTC_ALM`；`supply=U6 pin8 VBAT_IN`；`ground=U6 pin4 GND`；`clkout=pin7 NC`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 A3-A4 U6 pins3-8 与 GPIO14/GPIO12/RTC_ALM/VBAT_IN

## GPIO 与控制信号

### GPIO2 蓝色 LED

GPIO2 连接 LED1 蓝灯上端，LED1 下端经 R31 470R 接 GND，因此 GPIO2 高电平可为状态灯提供正向电流。

- 参数与网络：`gpio=GPIO2`；`led=LED1 blue`；`series_resistor=R31 470R`；`return=GND`；`active_level=high`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 A4 GPIO2-LED1-R31-GND

## 时钟

### ESP32 外部晶振

U1 ESP_XTAL_N/P 连接 X1 TXC/8Z40000017，X1 为 40MHz 器件；C17/C18 各 12pF 接 GND，ESP_XTAL_P 路串 R35 100R。

- 参数与网络：`crystal=X1 TXC/8Z40000017 40MHz`；`negative=ESP_XTAL_N`；`positive=ESP_XTAL_P via R35 100R`；`load_caps=C17 12pF,C18 12pF`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 C1 X1 与 ESP_XTAL_N/P、R35、C17/C18

## 复位

### ESP32_EN 手动复位

ESP32_EN 由 R27 10K 上拉到 VCC_3V3，并连接 U10 RESET 输出、S2 对地按键和 D9 3.3V/ESD 对地保护；按下 S2 将 ESP32_EN 拉低。

- 参数与网络：`net=ESP32_EN`；`pullup=R27 10K to VCC_3V3`；`supervisor=U10 RESET`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D9 3.3V/ESD`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 D1-D2 U10/R27/S2/D9/ESP32_EN

## 内存与 Flash

### U3/U4 外部存储总线

U3 ESPSRAM64H 与 U4 W25Q32 由 VDD_SDIO 供电并连接 SD_DATA0-3、SD_CMD、SD_CLK；U3 nCS 由 GPIO16 控制、SCLK 经 R6 200R 接 GPIO17，U4 SD_CMD/SD_CLK 分别有 R9 10K 与 R10 200R。

- 参数与网络：`psram=U3 ESPSRAM64H`；`flash=U4 W25Q32`；`supply=VDD_SDIO`；`bus=SD_DATA0,SD_DATA1,SD_DATA2,SD_DATA3,SD_CMD,SD_CLK`；`psram_cs=GPIO16 via R5 10K pullup`；`psram_clk=GPIO17 via R6 200R`；`flash_cmd_pullup=R9 10K`；`flash_clk_series=R10 200R`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 C2-D3 U3/U4 与 U1 SD_* 网络

## 射频

### ESP_LNA 天线路径

ESP_LNA 经过 TBD 匹配位 L1/C1/C3 后到选择节点；R2 0R 接 ANT1 PROANT_440，R3 标 DNP 接 J1 IPEX，因此图示装配默认使用 ANT1，IPEX 为未装可选路径。

- 参数与网络：`source=ESP_LNA`；`matching=L1/C1/C3 TBD`；`default_path=R2 0R to ANT1 PROANT_440`；`optional_path=R3 DNP to J1 IPEX`；`ipex_ground=J1 pins2/3 GND`
- 证据：图 d59e37772926 / 第 1 页 / 页面 1 A2-A3 ESP_LNA-L1/C1/C3-R2/R3-ANT1/J1

## 调试与烧录

### ESP32 GPIO0/EN 自动下载

U7 GPIO0_IN 与 ESP32_EN_IN 控制 FET1/FET2，分别经 R12/R17 2.2K 作用于 ESP32 GPIO0 与 ESP32_EN；R13/R16 和 R18/R21 为 1K 分压/偏置网络。

- 参数与网络：`boot_control=GPIO0_IN -> FET1 -> GPIO0 via R12 2.2K`；`reset_control=ESP32_EN_IN -> FET2 -> ESP32_EN via R17 2.2K`；`boot_bias=R13/R16 1K`；`reset_bias=R18/R21 1K`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 A1-B1 FET1/FET2 与 U7 GPIO0_IN/ESP32_EN_IN

## 模拟电路

### J4 与 GPIO38 电池采样

J4 pin 2 接 VBAT_IN、pin 1 接 GND；VBAT 经 R28 1.37K 到 GPIO38，GPIO38 经 R29 2.67K 接 GND，形成电池电压分压采样。

- 参数与网络：`connector=J4 SMT_HDR_2x1.25mm`；`pin_2=VBAT_IN`；`pin_1=GND`；`adc_pin=GPIO38`；`upper_resistor=R28 1.37K`；`lower_resistor=R29 2.67K`
- 证据：图 6f41535b5573 / 第 1 页 / 页面 2 C2-D2 J4 与 VBAT-R28-GPIO38-R29-GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | TimerCamera | `controller=U1 ESP32`；`camera=U2 OV-Camera`；`memory=U3 ESPSRAM64H,U4 W25Q32`；`usb_bridge=U7 CH552T`；`rtc=U6 BM8563`；`charger=U11 TP4057`；`power_hold=FET3/FET4`；`rails=VCC_3V3,VCC_1V5,VCC_2V8` |
| 内存与 Flash | U3/U4 外部存储总线 | `psram=U3 ESPSRAM64H`；`flash=U4 W25Q32`；`supply=VDD_SDIO`；`bus=SD_DATA0,SD_DATA1,SD_DATA2,SD_DATA3,SD_CMD,SD_CLK`；`psram_cs=GPIO16 via R5 10K pullup`；`psram_clk=GPIO17 via R6 200R`；`flash_cmd_pullup=R9 10K`；`flash_clk_series=R10 200R` |
| 时钟 | ESP32 外部晶振 | `crystal=X1 TXC/8Z40000017 40MHz`；`negative=ESP_XTAL_N`；`positive=ESP_XTAL_P via R35 100R`；`load_caps=C17 12pF,C18 12pF` |
| 射频 | ESP_LNA 天线路径 | `source=ESP_LNA`；`matching=L1/C1/C3 TBD`；`default_path=R2 0R to ANT1 PROANT_440`；`optional_path=R3 DNP to J1 IPEX`；`ipex_ground=J1 pins2/3 GND` |
| 接口 | U2 并行像素总线 | `Y2=pin19 GPIO32`；`Y3=pin21 GPIO35`；`Y4=pin22 GPIO34`；`Y5=pin20 GPIO5`；`Y6=pin18 GPIO39`；`Y7=pin16 GPIO18`；`Y8=pin14 GPIO36`；`Y9=pin12 GPIO19`；`PCLK=pin17 GPIO21 via R36 47R`；`XCLK=pin13 GPIO27 via R37 47R` |
| 总线 | 摄像头 SCCB/同步控制 | `SIO_C=pin5 GPIO23, R32 2K pullup`；`SIO_D=pin3 GPIO25, R33 2K pullup`；`HREF=pin9 GPIO26`；`VSYNC=pin7 GPIO22`；`RESET=pin6 GPIO15`；`PWDN=pin8 R4 10K to GND` |
| 电源 | 摄像头三路电源 | `DOVDD=pin11 VCC_3V3`；`DVDD=pin10 VCC_1V5`；`AVDD=pin4 VCC_2V8`；`DGND=pin15 GND`；`AGND=pin2 GND`；`pin1=NC` |
| 接口 | J2 PH2.0_4P_SMT | `pin_1=GPIO13 via R7 22R, D1 ESD`；`pin_2=GPIO4 via R8 22R, D2 ESD`；`pin_3=VSYS_VIN`；`pin_4=GND` |
| GPIO 与控制信号 | GPIO2 蓝色 LED | `gpio=GPIO2`；`led=LED1 blue`；`series_resistor=R31 470R`；`return=GND`；`active_level=high` |
| 接口 | J3 USB Type-C | `VBUS=VUSB_VCC`；`DP=USB_DP`；`DM=USB_DM`；`CC1=R22 5.1K to GND`；`CC2=R23 5.1K to GND`；`shield=GND` |
| 总线 | U7 CH552T USB/UART | `usb_dp=U7 pin14 USB_DP`；`usb_dm=U7 pin15 USB_DM`；`bridge_tx=U7 pin9 CH552_TXD via R19 1K to U0RXD`；`bridge_rx=U7 pin10 CH552_RXD via R20 1K to U0TXD`；`bias=R34 10K to VCC_3V3` |
| 调试与烧录 | ESP32 GPIO0/EN 自动下载 | `boot_control=GPIO0_IN -> FET1 -> GPIO0 via R12 2.2K`；`reset_control=ESP32_EN_IN -> FET2 -> ESP32_EN via R17 2.2K`；`boot_bias=R13/R16 1K`；`reset_bias=R18/R21 1K` |
| 总线 | U6 BM8563 | `controller=U1 ESP32`；`SCL=U6 pin6 GPIO14`；`SDA=U6 pin5 GPIO12`；`interrupt=U6 pin3 RTC_ALM`；`supply=U6 pin8 VBAT_IN`；`ground=U6 pin4 GND`；`clkout=pin7 NC` |
| 电源 | VBAT/VUSB 到 VSYS_VIN | `battery_path=VBAT -> D6 1N5819 -> VSYS_VIN`；`usb_path=VUSB_VCC -> D8 1N5819 -> VSYS_VIN`；`bulk_caps=C43,C44 10uF to GND` |
| 电源 | U5 SY8089AAC | `input=VSYS_VIN`；`converter=U5 SY8089AAC`；`enable=pin1 tied VSYS_VIN`；`inductor=L2 WPN3012H2R2MT`；`output=VCC_3V3`；`feedback=R14 11.5K 1%,R15 2.55K 1%`；`output_caps=C24,C25 22uF/6.3V` |
| 电源 | U8/U9 摄像头 LDO | `core_ldo=U8 HX6306P152/1.5V LDO 300mA`；`analog_ldo=U9 HX6306P282/2.8V LDO 300mA`；`input=VCC_3V3`；`outputs=VCC_1V5,VCC_2V8`；`u8_caps=C33 4.7uF,C34 4.7uF,C41 22uF`；`u9_caps=C37 4.7uF,C38 4.7uF,C42 22uF` |
| 电源 | U11 TP4057 | `charger=U11 TP4057`；`input=pin4 VUSB_VCC`；`battery_output=pin3 VBAT_IN`；`program=pin6 R30 5.1K to GND`；`status=pins1/5 NC`；`caps=C36 4.7uF,C40 10uF` |
| 模拟电路 | J4 与 GPIO38 电池采样 | `connector=J4 SMT_HDR_2x1.25mm`；`pin_2=VBAT_IN`；`pin_1=GND`；`adc_pin=GPIO38`；`upper_resistor=R28 1.37K`；`lower_resistor=R29 2.67K` |
| 电源 | FET3/FET4 电源保持 | `high_side=FET3 CJ2301/PMOS VBAT_IN-to-VBAT`；`gate=PWR_EN with R25 100K`；`hold_transistor=FET4 CJ2302-NMOS`；`hold_gpio=GPIO33 with R26 100K pulldown`；`wake_sources=RTC_ALM,GPIO37,USER_SVC via D3/D4/D5 1N4148` |
| 复位 | ESP32_EN 手动复位 | `net=ESP32_EN`；`pullup=R27 10K to VCC_3V3`；`supervisor=U10 RESET`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D9 3.3V/ESD` |
| 核心器件 | ESP32-D0WDQ6-V3 | `documented_model=ESP32-D0WDQ6-V3`；`schematic_model=ESP32`；`confirmed_revision=null` |
| 核心器件 | OV3660 与成像参数 | `documented_model=OV3660`；`documented_resolution=3MP 2048x1536`；`documented_dfov=66.5deg`；`documented_formats=8/10-bit RAW,RGB,YCbCr,compression`；`schematic_model=OV-Camera` |
| 内存与 Flash | 8MB PSRAM 与 4M Flash | `documented_psram=8MB Quad`；`documented_flash=4M`；`psram_part=ESPSRAM64H`；`flash_part=W25Q32`；`explicit_capacity_field=false` |
| 总线地址 | BM8563 I2C 地址 | `rtc=U6 BM8563`；`SCL=GPIO14`；`SDA=GPIO12`；`address_label=null`；`address_select=null` |
| 时钟 | BM8563 Y1 晶体 | `crystal=Y1 TCX/QH0320`；`load_caps=C23,C28 7pF`；`frequency=null`；`rtc_pins=OSCI pin1,OSCO pin2` |
| 电源 | 2uA 休眠与定时开关行为 | `documented_sleep_current=2uA`；`documented_power_button=long press 2s`；`wake_signal=RTC_ALM`；`hold_gpio=GPIO33`；`measurement_conditions=null`；`firmware_sequence=null` |
| 射频 | Wi-Fi 图像传输能力 | `documented_capability=Wi-Fi image transmission`；`rf_path=ESP_LNA to ANT1/J1`；`band=null`；`standard=null`；`tx_power=null`；`throughput=null`；`antenna_gain=null` |

## 待确认事项

- `component.documented-soc-version`：正文称主控为 ESP32-D0WDQ6-V3，但原理图 U1 器件值只写 ESP32，没有 D0WDQ6 或 V3 revision 字段。（证据：图 d59e37772926 / 第 1 页 / 页面 1 U1 下方仅标 ESP32）
- `component.documented-camera`：正文称摄像头为 OV3660、3MP、2048x1536、66.5° DFOV 并列出格式；原理图 U2 只标 OV-Camera，没有传感器型号、分辨率或光学参数。（证据：图 d59e37772926 / 第 1 页 / 页面 1 U2 仅标 OV-Camera 和 pinout）
- `memory.documented-capacities`：正文列出 8MB Quad PSRAM 和 4M Flash；原理图只标 U3 ESPSRAM64H、U4 W25Q32，没有独立 MB 容量或装配容量字段。（证据：图 d59e37772926 / 第 1 页 / 页面 1 U3/U4 仅显示料号）
- `address.rtc-i2c-address`：原理图确认 BM8563 通过 GPIO14/GPIO12 的 SCL/SDA 通信，但页面未标注 I2C 地址或地址选择网络，地址不能仅凭两页确定。（证据：图 6f41535b5573 / 第 1 页 / 页面 2 U6 SCL/SDA，无地址文字）
- `clock.rtc-crystal-frequency`：U6 OSCI/OSCO 连接 Y1 TCX/QH0320 与 C23/C28 7pF，但原理图未打印晶体频率，因此不能仅凭本页确认 RTC 晶体为具体频率。（证据：图 6f41535b5573 / 第 1 页 / 页面 2 A3-A4 Y1/C23/C28/U6 OSCI/OSCO，无 Hz 标注）
- `power.documented-sleep-current`：正文称休眠电流可低至 2uA，并描述长按开机、软件关机和 RTC 定时唤醒；原理图只显示硬件保持与 RTC_ALM 网络，没有电流预算、固件时序或测量条件。（证据：图 6f41535b5573 / 第 1 页 / 页面 2 FET3/FET4/RTC_ALM/USER_SVC 电路，无 uA 或时间标注）
- `rf.documented-wifi`：正文称支持 Wi-Fi 图像传输；原理图只确认 ESP_LNA 到 PROANT_440/IPEX 的射频路径，没有频段、制式、功率、吞吐量或天线性能。（证据：图 d59e37772926 / 第 1 页 / 页面 1 ESP_LNA 匹配与天线选择，无 RF 性能参数）
- `review.soc-version`：请用 BOM、芯片丝印或采购料号确认 TimerCamera 主控是否固定为 ESP32-D0WDQ6-V3。；原因：原理图只写 ESP32。
- `review.camera-model`：请用摄像头 BOM/丝印/datasheet 确认 OV3660 与 3MP、2048x1536、DFOV 和格式参数。；原因：原理图只标 OV-Camera。
- `review.memory-capacities`：请用 U3/U4 datasheet、BOM 或实机确认 8MB PSRAM 和 4M Flash 容量。；原因：页面只有料号，没有容量字段。
- `review.rtc-address`：请依据 BM8563 datasheet 或固件确认 RTC I2C 地址。；原因：原理图没有地址值或选择网络。
- `review.rtc-crystal`：请用 Y1 料号/BOM 或测量确认 BM8563 晶体频率与负载参数。；原因：原理图未打印晶体频率。
- `review.sleep-current`：请用当前固件、电池配置和实测确认 2uA 休眠、长按 2s 开机、软件关机及 RTC 唤醒时序。；原因：这些属于系统/固件行为，原理图没有电流与时序条件。
- `review.wifi`：请用确认后的 ESP32、天线 BOM 和射频/吞吐测试确认 Wi-Fi 频段、制式与图像传输性能。；原因：原理图仅显示 RF 连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d59e377729269ff9861c98e94ea64c868010a7c625075e734628b2cae40d4c33` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1042/Sch_M5TimerCAM_page_01.png` |
| 2 | 1 | `6f41535b5573e4bb7000ff81b2558046dbfdc208c6f3b55c810658823d28749b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1042/Sch_M5TimerCAM_page_02.png` |

---

源文档：`zh_CN/unit/timercam.md`

源文档 SHA-256：`2e4eae3a2ac0d5fa0e74123ae4daddd4ae6738a67a1e34415af58856b11e441a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
