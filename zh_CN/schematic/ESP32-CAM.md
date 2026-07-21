# ESP32-CAM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | ESP32-CAM |
| SKU | U007 |
| 产品 ID | `esp32-cam-88744061cd2f` |
| 源文档 | `zh_CN/unit/esp32cam.md` |

## 概述

ESP32-CAM（U007）以 U4 裸 ESP32 为主控，U5 GD25Q32C 通过 SD_CMD/SD_CLK/SD_DATA0-3 连接外部 Flash，X1 提供 40MHz 时钟，ESP_LNA 经未定值匹配网络连接 ANT1。电源页使用 U3 IP5306 管理 VIN_USB/VBAT/5VBUS，U1 SY8089 生成 VCC_3V3，U2 RT9182-G 再生成 VDD_2V5 与 VDD_1V8；这些电源共同服务 ESP32 与摄像头 FPC。J1 24 针摄像头接口连接多路 GPIO、PWDN 和三路电源；U6 CP2104 经 USB_D+/D- 和 GPIO1/GPIO3 提供调试串口，并由 VT1/VT2 完成 EN/GPIO0 自动下载控制。第 4 页的 MPU6050、SPQ2410HR5H 和 BME280 电路均明确标 NC；正文中的 OV2640/2MP、4MB/520KB、Grove、LED 与部分 GPIO 信号语义未全部由原理图直接证明。

## 检索关键词

`ESP32-CAM`、`U007`、`ESP32`、`GD25Q32C`、`SY8089`、`RT9182-G`、`IP5306`、`CP2104`、`OV2640`、`FPC0.5-SMT-24P-T`、`40MHz`、`ANT1`、`ESP_LNA`、`SD_CMD`、`SD_CLK`、`SD_DATA0`、`SD_DATA1`、`SD_DATA2`、`SD_DATA3`、`VIN_USB`、`VBAT`、`5VBUS`、`VCC_3V3`、`VDD_2V5`、`VDD_1V8`、`VDD_SDIO`、`USB_DP`、`USB_DM`、`GPIO0`、`EN`、`DTR`、`RTS`、`GPIO1`、`GPIO3`、`PWDN`、`GPIO23`、`GPIO25`、`GPIO27`、`GPIO22`、`GPIO26`、`GPIO21`、`GPIO32`、`BME280 NC`、`MPU6050 NC`、`SPQ2410HR5H NC`、`0x75`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | ESP32 | 主控 SoC，连接外部 Flash、摄像头、UART、射频、40MHz 晶振和预留外设 | 图 2347347004d7 / 第 1 页 / source_003.png 网格 A1-B1，U4 ESP32 pin1-pin49 与 GPIO/SDIO/RF/时钟/电源网络 |
| U5 | GD25Q32C | ESP32 外部六线串行 Flash，连接 SD_CMD/SD_CLK/SD_DATA0-3 | 图 2347347004d7 / 第 1 页 / source_003.png 网格 B2，U5 GD25Q32C pin1-pin8 |
| X1 | 40MHz +/-10ppm/22pF | ESP32 XTAL_N/XTAL_P 外部主晶振 | 图 2347347004d7 / 第 1 页 / source_003.png 网格 C1，X1 40MHz +/-10ppm/22pF 与 C30/C31 22pF |
| ANT1,L3,C14,C19 | Antenna / TBD matching | ESP_LNA 射频输出到 ANT1 的串并联匹配网络，三只匹配值均标 TBD | 图 2347347004d7 / 第 1 页 / source_003.png 网格 A2，ESP_LNA、L3 TBD、C14 TBD、C19 TBD 与 ANT1 |
| U1 (Power sheet) | SY8089 | 5VBUS 至 VCC_3V3 的同步降压转换器 | 图 d793c702a91b / 第 1 页 / source_002.png 网格 A1-A2，U1 SY8089、L1 2.2uH、R1 100K、R2 22K 与 VCC_3V3 |
| U2 (Power sheet) | RT9182-G | 由 VCC_3V3 生成 VDD_2V5 和 VDD_1V8 的双路 LDO | 图 d793c702a91b / 第 1 页 / source_002.png 网格 B1-B2，U2 RT9182-G，VOUT1 VDD_2V5、VOUT2 VDD_1V8 |
| U3 (Power sheet) | IP5306 | VIN_USB/VBAT/5VBUS 电池充电、升压和电源管理器 | 图 d793c702a91b / 第 1 页 / source_002.png 网格 C1-D2，U3 IP5306、L2 1uH、VIN_USB/VBAT/5VBUS/SW_KEY |
| J1 (Camera sheet) | FPC0.5-SMT-24P-T | 24 针摄像头 FPC，连接 GPIO 数据/时序、PWDN、GND 与 3.3V/1.8V/2.5V | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A1-B1，J1 FPC0.5-SMT-24P-T pin1-pin24 |
| U6 | CP2104 | USB-UART 桥接器，连接 USB_DP/USB_DM、GPIO1/GPIO3 与 DTR/RTS 自动下载网络 | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A3-B4，U6 CP2104，DP/DM/TXD/RXD/RTS/DTR/REGIN/VBUS/VIO/VDD |
| U7 | VCMH2 / USB_Micro | VIN_USB 与 USB_DN/USB_DP 的外部 USB 连接器；图块标题同时标 Type-C USB | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B3-C4，Type-C USB 图块中的 U7，符号文字 VCMH2/USB_Micro |
| VT1,VT2 | NPN-S8050-贴片 | 由 CP2104 DTR/RTS 控制 EN 与 GPIO0 的自动下载晶体管网络 | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A2，Auto-Download 的 VT1/VT2 NPN-S8050-贴片 与 R7/R9 10K |
| S1 | SMT_SW_TS_015 | SW_KEY 到 GND 的用户/电源按键，带 R16 上拉、D3 和 C37 | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 D2，S1 SMT_SW_TS_015、SW_KEY、R16 10K、D3、C37 100nF |
| D1,D2,R14,R15 | RLSD52A031V / 22R | USB_DN/USB_DP 的对地 ESD 钳位与串联阻抗网络 | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B3-C3，D1/D2 RLSD52A031V 与 R14/R15 22R |
| U9,U8,U1 (Accessory sheet) | MPU6050 / SPQ2410HR5H / BME280 | 明确标 NC 的预留 IMU、麦克风和环境传感器电路，不应视为已装配器件 | 图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B1-D4，MPU6050、MicroPhone、BME280 三个图块均带红框 NC |

## 系统结构

### ESP32-CAM 系统架构

U4 ESP32 通过六线 SDIO/SPI 网络连接 U5 GD25Q32C，通过 24 针 J1 连接摄像头，通过 GPIO1/GPIO3 连接 CP2104 UART，并通过 ESP_LNA 接 ANT1。IP5306、SY8089、RT9182-G 形成 VIN_USB/VBAT/5VBUS、VCC_3V3、VDD_2V5 与 VDD_1V8 电源树；第 4 页 MPU6050、麦克风与 BME280 图块均标 NC。

- 参数与网络：`controller=U4 ESP32`；`flash=U5 GD25Q32C`；`camera=J1 FPC0.5-SMT-24P-T`；`usb_uart=U6 CP2104`；`rf=ESP_LNA -> ANT1`；`power=IP5306,SY8089,RT9182-G`；`not_populated=MPU6050,SPQ2410HR5H,BME280`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 完整 Power Management 页; 图 2347347004d7 / 第 1 页 / source_003.png 完整 ESP32 Subsystem 页; 图 c1372f4af2c4 / 第 1 页 / source_004.png 完整 USB-UART & Accessory 页

## 核心器件

### NC 预留外设

Accessory 页将 U9 MPU6050 图块、U8 SPQ2410HR5H MicroPhone 图块和 U1 BME280 图块均用红框 NC 标注；这些网络是预留设计，不应描述为当前板已装配的 IMU、麦克风或环境传感器。

- 参数与网络：`imu=U9 MPU6050 NC`；`microphone=U8 SPQ2410HR5H NC`；`environment=U1 BME280 NC`；`assembly_status=not populated`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B1-D4，三个红框 NC 标记

## 电源

### IP5306 USB/电池/5VBUS 路径

U3 IP5306 VIN pin1 接 VIN_USB 并由 C9 22uF/6.3V 去耦，BAT pin6 接 VBAT，SW pin7 经 L2 1uH/0420 接 VBAT，VOUT pin8 输出 5VBUS；KEY pin5 接 SW_KEY，GND pin9 接地，5VBUS 侧使用 C10/C11/C12 各 22uF/6.3V。页面注释称其为 2.1A Charge、2.4A Boost Power Management SoC。

- 参数与网络：`pmic=U3 IP5306`；`usb_input=VIN_USB pin1`；`battery=VBAT pin6`；`switch_node=pin7 SW -> L2 1uH -> VBAT`；`output=pin8 VOUT -> 5VBUS`；`key=pin5 SW_KEY`；`output_caps=C10/C11/C12 22uF/6.3V`；`page_annotation=2.1A Charge,2.4A Boost`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 网格 C1-D2 BAT PMIC 图块

### 5VBUS 至 VCC_3V3 降压

U1 SY8089 的 INLX pin4 与 EN pin1 接 5VBUS，LX pin3 经 L1 2.2uH/0420 输出 VCC_3V3，FB pin5 使用 R1 100K/R2 22K 分压，GND pin2 接地。C4 22uF 与 C5 2.2uF 位于输入，C2/C3 各 22uF 位于输出，C1 22pF 标 DNW。

- 参数与网络：`converter=U1 SY8089`；`input=5VBUS`；`enable=pin1 tied 5VBUS`；`inductor=L1 2.2uH/0420`；`output=VCC_3V3`；`feedback=R1 100K,R2 22K`；`optional_cap=C1 22pF/DNW`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 网格 A1-A2 5V -> 3.3V DCDC Buck

### VDD_2V5 与 VDD_1V8 双 LDO

U2 RT9182-G VIN pin5 接 VCC_3V3，EN1 pin4 与 EN2 pin3 均接 VCC_3V3；VOUT1 pin6 输出 VDD_2V5，VOUT2 pin1 输出 VDD_1V8，GND pin2 接地。C8、C6、C7 均为 2.2uF/6.3V，分别用于输入与两个输出。

- 参数与网络：`ldo=U2 RT9182-G`；`input=VCC_3V3 pin5`；`enables=pins3/4 tied VCC_3V3`；`output1=pin6 VDD_2V5`；`output2=pin1 VDD_1V8`；`caps=C8/C6/C7 2.2uF/6.3V`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 网格 B1-B2 3.3V -> 2V5 & 1V8 LDO

## 接口

### 摄像头 J1 电源与保留引脚

Camera 页 J1 为 FPC0.5-SMT-24P-T：pin11 接 VCC_3V3，pin10 接 VDD_1V8，pin4 接 VDD_2V5，pin15 与 pin1 接 GND；pin24、pin23、pin2 未连接。pin8 PWDN 由 R10 12K 下拉到 GND。

- 参数与网络：`connector=J1 FPC0.5-SMT-24P-T`；`pin11=VCC_3V3`；`pin10=VDD_1V8`；`pin4=VDD_2V5`；`ground=pins15/1 GND`；`no_connect=pins24/23/2`；`power_down=pin8 PWDN,R10 12K to GND`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A1-B1，Camera J1 pin1-pin24 的电源/GND/PWDN/NC

### USB 电源与数据路径

U7 pin1 将外部 USB 电源接 VIN_USB，pin2 D- 经 R14 22R 接 USB_DN，pin3 D+ 经 R15 22R 接 USB_DP，pin5 与屏蔽 pins6/7 接 GND。USB_DN/USB_DP 连接 U6 CP2104 DM/DP，R4/R5 各 33K 将 USB_CC_1/USB_CC_2 接 GND。

- 参数与网络：`connector=U7`；`vbus=pin1 VIN_USB`；`d_minus=pin2 -> R14 22R -> USB_DN -> CP2104 DM`；`d_plus=pin3 -> R15 22R -> USB_DP -> CP2104 DP`；`ground=pin5,pins6/7 shield`；`cc_resistors=R4/R5 33K to GND`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B2-C4，USB_CC_1/2、U7、R14/R15、USB_DN/DP 与 U6

## 总线

### CP2104 到 ESP32 UART

U6 CP2104 TXD pin21 经 R8 470R 连接 RXD0/GPIO3，RXD pin20 连接 TXD0/GPIO1；RTS pin19 输出 RTS，DTR pin23 输出 DTR，分别进入自动下载网络。

- 参数与网络：`bridge=U6 CP2104`；`cp_tx=pin21 -> R8 470R -> ESP32 GPIO3 RXD0`；`cp_rx=pin20 -> ESP32 GPIO1 TXD0`；`rts=pin19 RTS`；`dtr=pin23 DTR`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A3-B4，U6 TXD/RXD/RTS/DTR 与 GPIO3/GPIO1

### NC 外设预留 GPIO

未装配 MPU6050 的 SCL/SCLK 接 GPIO4、SDA/SDI 接 GPIO13；未装配 BME280 的 SCK 接 GPIO4、SDI 接 GPIO13，CSB 接 VCC_3V3、SDO 接 GND；未装配 SPQ2410HR5H 的 VOUT 经 C35 100nF 接 GPIO32。

- 参数与网络：`mpu6050=GPIO4 SCL,GPIO13 SDA`；`bme280=GPIO4 SCK,GPIO13 SDI,CSB VCC_3V3,SDO GND`；`microphone=VOUT -> C35 100nF -> GPIO32`；`status=all NC`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png MPU6050/MicroPhone/BME280 NC 图块中的 GPIO4/GPIO13/GPIO32

## 总线地址

### IP5306 I2C 地址标注

Power 页在 IP5306 图块旁明确印有 IIC address: 0x75，并注释 IP5306 communicates with ESP32 through IIC for ESP32CAM。

- 参数与网络：`device=U3 IP5306`；`address=0x75`；`annotation=communicates with ESP32 through IIC`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 网格 D2，IP5306 下方 IIC address: 0x75 注释

## GPIO 与控制信号

### 摄像头 FPC 到 ESP32 GPIO 映射

J1 pin22=GPIO32、pin21=GPIO33、pin20=GPIO5、pin19=GPIO17、pin18=GPIO39、pin17=GPIO21、pin16=GPIO18、pin14=GPIO36、pin13=GPIO27、pin12=GPIO19、pin9=GPIO26、pin7=GPIO22、pin6=GPIO15、pin5=GPIO23、pin3=GPIO25；pin8 为独立 PWDN。

- 参数与网络：`pin22=GPIO32`；`pin21=GPIO33`；`pin20=GPIO5`；`pin19=GPIO17`；`pin18=GPIO39`；`pin17=GPIO21`；`pin16=GPIO18`；`pin14=GPIO36`；`pin13=GPIO27`；`pin12=GPIO19`；`pin9=GPIO26`；`pin8=PWDN`；`pin7=GPIO22`；`pin6=GPIO15`；`pin5=GPIO23`；`pin3=GPIO25`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A1-B1，Camera J1 左侧 GPIOxx+pin 编号标注

### SW_KEY 按键网络

SW_KEY 由 R16 10K 上拉到 VCC_3V3，S1 SMT_SW_TS_015 按下时接 GND；C37 100nF 与 D3 从 SW_KEY 接 GND。SW_KEY 同名网络连接 Power 页 IP5306 KEY pin5。

- 参数与网络：`key=S1 SMT_SW_TS_015`；`signal=SW_KEY`；`pullup=R16 10K to VCC_3V3`；`press=to GND`；`capacitor=C37 100nF to GND`；`pmic=IP5306 pin5 KEY`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 D2，SW_KEY/R16/S1/D3/C37; 图 d793c702a91b / 第 1 页 / source_002.png U3 IP5306 pin5 KEY/SW_KEY

## 时钟

### ESP32 40MHz 外部时钟

U4 XTAL_N pin44 与 XTAL_P pin45 连接 X1 40MHz +/-10ppm/22pF，C30/C31 各 22pF 从晶振两端接 GND；晶振外壳/辅助端接地。

- 参数与网络：`controller=U4 ESP32`；`xtal_n=pin44 ESP_XTAL_N`；`xtal_p=pin45 ESP_XTAL_P`；`crystal=X1 40MHz +/-10ppm/22pF`；`load_caps=C30/C31 22pF`
- 证据：图 2347347004d7 / 第 1 页 / source_003.png 网格 C1，X1/C30/C31 与 U4 XTAL_N/XTAL_P

## 复位

### DTR/RTS 自动下载控制

DTR 经 R7 10K 驱动 VT1 NPN-S8050，RTS 经 R9 10K 驱动 VT2 NPN-S8050；交叉耦合网络分别控制 EN 与 GPIO0。GPIO0 由 R11 10K 上拉到 VCC_3V3，EN 由 R12 10K 上拉并由 C34 100nF 接 GND。

- 参数与网络：`dtr=DTR -> R7 10K -> VT1`；`rts=RTS -> R9 10K -> VT2`；`targets=EN,GPIO0`；`gpio0_pullup=R11 10K to VCC_3V3`；`en_pullup=R12 10K to VCC_3V3`；`en_cap=C34 100nF to GND`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 A2-B2，Auto-Download 与 GPIO0/EN 上拉网络

## 保护电路

### USB 数据线保护

USB_DN/USB_DP 各经 R14/R15 22R 串联，D1/D2 RLSD52A031V 分别从两条数据线钳位到 GND。图中未在 VIN_USB 上显示保险丝、TVS 或反接保护。

- 参数与网络：`d_minus_series=R14 22R`；`d_plus_series=R15 22R`；`d_minus_esd=D1 RLSD52A031V to GND`；`d_plus_esd=D2 RLSD52A031V to GND`；`vbus_fuse=null`；`vbus_tvs=null`
- 证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B3-C3，USB_DN/DP 的 D1/D2 与 R14/R15

## 关键网络

### 关键电源与信号索引

VIN_USB 进入 IP5306 与 CP2104，IP5306 连接 VBAT 并输出 5VBUS；SY8089 输出 VCC_3V3，RT9182-G 输出 VDD_2V5/VDD_1V8。ESP32 使用 SD_CMD/SD_CLK/SD_DATA0-3 连接 Flash，GPIO1/3 连接 UART，EN/GPIO0 连接自动下载，ESP_LNA 连接 ANT1，摄像头 J1 使用多路 GPIO 和三路电源。

- 参数与网络：`power=VIN_USB,VBAT,5VBUS,VCC_3V3,VDD_2V5,VDD_1V8,VDD_SDIO`；`flash=SD_CMD,SD_CLK,SD_DATA0-3`；`uart=GPIO1 TXD0,GPIO3 RXD0`；`download=EN,GPIO0,DTR,RTS`；`rf=ESP_LNA,ANT1`；`usb=USB_DP,USB_DM`；`camera=J1 GPIO/PWDN rails`
- 证据：图 d793c702a91b / 第 1 页 / source_002.png 电源网络; 图 2347347004d7 / 第 1 页 / source_003.png ESP32/Flash/RF/时钟网络; 图 c1372f4af2c4 / 第 1 页 / source_004.png 摄像头/USB/UART/自动下载网络

## 内存与 Flash

### GD25Q32C 外部 Flash 连接

U5 GD25Q32C pin1 nCS 接 SD_CMD，pin6 CLK 接 SD_CLK，pin5 DI/IO0 接 SD_DATA1，pin2 DO/IO1 接 SD_DATA0，pin3 nWP/IO2 接 SD_DATA3，pin7 nHOLD/IO3 接 SD_DATA2，pin8 接 VCC_3V3 并由 C20 0.1uF 去耦，pin4 接 GND。

- 参数与网络：`part_number=GD25Q32C`；`chip_select=pin1 SD_CMD`；`clock=pin6 SD_CLK`；`io0=pin5 SD_DATA1`；`io1=pin2 SD_DATA0`；`io2=pin3 SD_DATA3`；`io3=pin7 SD_DATA2`；`power=pin8 VCC_3V3,pin4 GND`
- 证据：图 2347347004d7 / 第 1 页 / source_003.png 网格 B2，U5 GD25Q32C 与 U4 SD_DATA0-3/SD_CMD/SD_CLK

## 射频

### ESP32 射频天线网络

U4 LNA pin2 的 ESP_LNA 网络先经过 L3 对地支路、再经过 C14 串联、C19 对地后连接 ANT1；L3/C14/C19 的值全部标 TBD，ANT1 型号和天线参数未标。

- 参数与网络：`source=U4 pin2 LNA ESP_LNA`；`shunt1=L3 TBD to GND`；`series=C14 TBD`；`shunt2=C19 TBD to GND`；`antenna=ANT1`；`matching_values=TBD`
- 证据：图 2347347004d7 / 第 1 页 / source_003.png 网格 A2 ESP_LNA 匹配与 ANT1

## 其他事实

### 原理图版本与页结构

封面修订表为 A1 First Release、日期 6/1/2018、BY MH；图纸 Number 20180601A0_REV1、Revision REV1。封面列出 Power Management、ESP32 Subsystem、USB-UART & Accessory 三个电路页。

- 参数与网络：`revision_entry=A1 First Release`；`date=6/1/2018`；`by=MH`；`number=20180601A0_REV1`；`revision=REV1`；`circuit_pages=Power Management,ESP32 Subsystem,USB-UART & Accessory`
- 证据：图 bc0abcb61627 / 第 1 页 / source_001.png 封面 REV 表、SCHEMATIC PAGE 表与右下图框

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-CAM 系统架构 | `controller=U4 ESP32`；`flash=U5 GD25Q32C`；`camera=J1 FPC0.5-SMT-24P-T`；`usb_uart=U6 CP2104`；`rf=ESP_LNA -> ANT1`；`power=IP5306,SY8089,RT9182-G`；`not_populated=MPU6050,SPQ2410HR5H,BME280` |
| 电源 | IP5306 USB/电池/5VBUS 路径 | `pmic=U3 IP5306`；`usb_input=VIN_USB pin1`；`battery=VBAT pin6`；`switch_node=pin7 SW -> L2 1uH -> VBAT`；`output=pin8 VOUT -> 5VBUS`；`key=pin5 SW_KEY`；`output_caps=C10/C11/C12 22uF/6.3V`；`page_annotation=2.1A Charge,2.4A Boost` |
| 电源 | 5VBUS 至 VCC_3V3 降压 | `converter=U1 SY8089`；`input=5VBUS`；`enable=pin1 tied 5VBUS`；`inductor=L1 2.2uH/0420`；`output=VCC_3V3`；`feedback=R1 100K,R2 22K`；`optional_cap=C1 22pF/DNW` |
| 电源 | VDD_2V5 与 VDD_1V8 双 LDO | `ldo=U2 RT9182-G`；`input=VCC_3V3 pin5`；`enables=pins3/4 tied VCC_3V3`；`output1=pin6 VDD_2V5`；`output2=pin1 VDD_1V8`；`caps=C8/C6/C7 2.2uF/6.3V` |
| 总线地址 | IP5306 I2C 地址标注 | `device=U3 IP5306`；`address=0x75`；`annotation=communicates with ESP32 through IIC` |
| 内存与 Flash | GD25Q32C 外部 Flash 连接 | `part_number=GD25Q32C`；`chip_select=pin1 SD_CMD`；`clock=pin6 SD_CLK`；`io0=pin5 SD_DATA1`；`io1=pin2 SD_DATA0`；`io2=pin3 SD_DATA3`；`io3=pin7 SD_DATA2`；`power=pin8 VCC_3V3,pin4 GND` |
| 时钟 | ESP32 40MHz 外部时钟 | `controller=U4 ESP32`；`xtal_n=pin44 ESP_XTAL_N`；`xtal_p=pin45 ESP_XTAL_P`；`crystal=X1 40MHz +/-10ppm/22pF`；`load_caps=C30/C31 22pF` |
| 射频 | ESP32 射频天线网络 | `source=U4 pin2 LNA ESP_LNA`；`shunt1=L3 TBD to GND`；`series=C14 TBD`；`shunt2=C19 TBD to GND`；`antenna=ANT1`；`matching_values=TBD` |
| 接口 | 摄像头 J1 电源与保留引脚 | `connector=J1 FPC0.5-SMT-24P-T`；`pin11=VCC_3V3`；`pin10=VDD_1V8`；`pin4=VDD_2V5`；`ground=pins15/1 GND`；`no_connect=pins24/23/2`；`power_down=pin8 PWDN,R10 12K to GND` |
| GPIO 与控制信号 | 摄像头 FPC 到 ESP32 GPIO 映射 | `pin22=GPIO32`；`pin21=GPIO33`；`pin20=GPIO5`；`pin19=GPIO17`；`pin18=GPIO39`；`pin17=GPIO21`；`pin16=GPIO18`；`pin14=GPIO36`；`pin13=GPIO27`；`pin12=GPIO19`；`pin9=GPIO26`；`pin8=PWDN`；`pin7=GPIO22`；`pin6=GPIO15`；`pin5=GPIO23`；`pin3=GPIO25` |
| 接口 | USB 电源与数据路径 | `connector=U7`；`vbus=pin1 VIN_USB`；`d_minus=pin2 -> R14 22R -> USB_DN -> CP2104 DM`；`d_plus=pin3 -> R15 22R -> USB_DP -> CP2104 DP`；`ground=pin5,pins6/7 shield`；`cc_resistors=R4/R5 33K to GND` |
| 总线 | CP2104 到 ESP32 UART | `bridge=U6 CP2104`；`cp_tx=pin21 -> R8 470R -> ESP32 GPIO3 RXD0`；`cp_rx=pin20 -> ESP32 GPIO1 TXD0`；`rts=pin19 RTS`；`dtr=pin23 DTR` |
| 复位 | DTR/RTS 自动下载控制 | `dtr=DTR -> R7 10K -> VT1`；`rts=RTS -> R9 10K -> VT2`；`targets=EN,GPIO0`；`gpio0_pullup=R11 10K to VCC_3V3`；`en_pullup=R12 10K to VCC_3V3`；`en_cap=C34 100nF to GND` |
| GPIO 与控制信号 | SW_KEY 按键网络 | `key=S1 SMT_SW_TS_015`；`signal=SW_KEY`；`pullup=R16 10K to VCC_3V3`；`press=to GND`；`capacitor=C37 100nF to GND`；`pmic=IP5306 pin5 KEY` |
| 保护电路 | USB 数据线保护 | `d_minus_series=R14 22R`；`d_plus_series=R15 22R`；`d_minus_esd=D1 RLSD52A031V to GND`；`d_plus_esd=D2 RLSD52A031V to GND`；`vbus_fuse=null`；`vbus_tvs=null` |
| 核心器件 | NC 预留外设 | `imu=U9 MPU6050 NC`；`microphone=U8 SPQ2410HR5H NC`；`environment=U1 BME280 NC`；`assembly_status=not populated` |
| 总线 | NC 外设预留 GPIO | `mpu6050=GPIO4 SCL,GPIO13 SDA`；`bme280=GPIO4 SCK,GPIO13 SDI,CSB VCC_3V3,SDO GND`；`microphone=VOUT -> C35 100nF -> GPIO32`；`status=all NC` |
| 关键网络 | 关键电源与信号索引 | `power=VIN_USB,VBAT,5VBUS,VCC_3V3,VDD_2V5,VDD_1V8,VDD_SDIO`；`flash=SD_CMD,SD_CLK,SD_DATA0-3`；`uart=GPIO1 TXD0,GPIO3 RXD0`；`download=EN,GPIO0,DTR,RTS`；`rf=ESP_LNA,ANT1`；`usb=USB_DP,USB_DM`；`camera=J1 GPIO/PWDN rails` |
| 其他事实 | 原理图版本与页结构 | `revision_entry=A1 First Release`；`date=6/1/2018`；`by=MH`；`number=20180601A0_REV1`；`revision=REV1`；`circuit_pages=Power Management,ESP32 Subsystem,USB-UART & Accessory` |
| 传感器 | 正文中的 OV2640 摄像头与信号语义 | `documented_sensor=OV2640`；`documented_resolution=2MP`；`documented_fov=65°`；`documented_control=SIOC GPIO23,SIOD GPIO25,XCLK GPIO27,RESET GPIO15`；`documented_timing=VSYNC GPIO22,HREF GPIO26,PCLK GPIO21`；`documented_data=D2 GPIO17,D3 GPIO35,D4 GPIO34,D5 GPIO5,D6 GPIO39,D7 GPIO18,D8 GPIO36,D9 GPIO19`；`schematic_sensor_model=null` |
| 接口 | 正文中的 HY2.0-4P 接口 | `documented_connector=HY2.0-4P`；`documented_scl=GPIO4`；`documented_sda=GPIO13`；`documented_power=5V,GND`；`schematic_connector_reference=null`；`schematic_gpio_usage=NC MPU6050/BME280` |
| GPIO 与控制信号 | 正文中的 GPIO16 LED | `documented_led_gpio=GPIO16`；`led_reference=null`；`led_driver=null`；`schematic_gpio16=U4 GPIO16 network only` |
| 接口 | USB 连接器类型标注冲突 | `section_title=Type-C USB`；`symbol_text=USB_Micro`；`part_text=VCMH2`；`cc_network=USB_CC_1/2,R4/R5 33K to GND`；`resolved_connector_type=null` |
| 总线 | IP5306 I2C 连接路径 | `annotation=IP5306 communicates with ESP32 through IIC`；`address=0x75`；`schematic_scl=null`；`schematic_sda=null`；`esp32_gpio_map=null` |
| 内存与 Flash | 正文中的 Flash 与 RAM 容量 | `documented_flash=4MB`；`schematic_flash=U5 GD25Q32C`；`documented_ram=520KB`；`psram=null`；`schematic_capacity_text=null` |

## 待确认事项

- `sensor.documented-camera-module`：产品正文称摄像头为 OV2640、2MP、65° 视角，并给出 SCCB、XCLK、VSYNC、HREF、PCLK、D2-D9、RESET 的 GPIO 语义；原理图只显示无传感器型号的 J1 24 针 FPC 及 GPIO/电源连接，没有 OV2640 文字、分辨率、视角、格式或 FPC pin 到具体摄像头信号名称。（证据：图 c1372f4af2c4 / 第 1 页 / source_004.png Camera J1 FPC 仅标 GPIO/电源/PWDN，无 OV2640 或信号语义）
- `interface.documented-grove-port`：产品正文称 HY2.0-4P 使用 SCL=GPIO4、SDA=GPIO13、5V、GND；四张原理图中未显示 HY2.0/Grove 连接器。GPIO4/GPIO13 只在 Accessory 页连接标 NC 的 MPU6050/BME280 预留电路。（证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 全页无 HY2.0；GPIO4/GPIO13 仅见 NC 外设）
- `gpio.documented-led`：产品正文列出 LED_Pin=GPIO16；四张原理图没有 LED 位号、LED 驱动支路或 GPIO16 到 LED 的连接，只在 ESP32 页显示 GPIO16 网络、摄像头 J1 pin16 则连接 GPIO18。（证据：图 2347347004d7 / 第 1 页 / source_003.png U4 GPIO16；整页无 LED）
- `interface.usb-connector-type`：Accessory 页图块标题写 Type-C USB，并画出 USB_CC_1/USB_CC_2 各经 33K 到 GND；同一图块 U7 符号下方却标 USB_Micro，器件内部文字为 VCMH2，且 U7 只画 VBUS/D-/D+/ID/GND 与屏蔽脚。仅凭本页无法唯一确定量产连接器类型。（证据：图 c1372f4af2c4 / 第 1 页 / source_004.png 网格 B2-C4，Type-C USB 标题、U7 USB_Micro/VCMH2 与 CC 电阻）
- `bus.ip5306-i2c-route`：Power 页文字称 IP5306 通过 IIC 与 ESP32 通信并标地址 0x75，但 U3 符号只画 VIN/LED1-3/VOUT/SW/BAT/KEY/GND，没有 SDA/SCL 引脚或到 ESP32 GPIO 的网络；其他页也未画 IP5306 专用 I2C 路由。（证据：图 d793c702a91b / 第 1 页 / source_002.png IP5306 符号与 IIC 注释，未画 SDA/SCL）
- `memory.documented-capacities`：产品正文列出 4MB Flash 与 520KB RAM；原理图确认外部 Flash 型号 GD25Q32C 和 ESP32 芯片，但页面没有直接印出容量换算、ESP32 内部 RAM 容量或额外 PSRAM 器件。（证据：图 2347347004d7 / 第 1 页 / source_003.png U4 ESP32 与 U5 GD25Q32C，图中无容量文字或 PSRAM）
- `review.camera-module-map`：请用当前摄像头模组 BOM/OV2640 datasheet 与实板确认传感器型号、2MP/65° 参数、FPC pin 定义及各 GPIO 信号语义。；原因：原理图只给 FPC 的 GPIO/电源映射，没有摄像头型号和信号名。
- `review.grove-port`：请用 PCB/BOM 或实板确认是否装配 HY2.0-4P、其位号，以及 GPIO4/GPIO13/5V/GND 的实际连接。；原因：四张原理图没有 Grove 连接器，GPIO4/GPIO13 只画在 NC 预留外设。
- `review.led-gpio16`：请用 PCB/BOM 或实板确认 GPIO16 是否连接板载 LED，并补充 LED 位号、极性、限流与驱动方式。；原因：原理图未显示 LED 电路。
- `review.usb-connector`：请用当前 PCB/BOM 确认量产 USB 连接器是 Type-C、Micro-USB 还是 VCMH2 对应器件，并核对 CC 电阻值与连接。；原因：图块标题、符号名称和器件文字互相不一致。
- `review.ip5306-i2c-route`：请用 PCB 网表、IP5306 具体料号变体或固件确认 0x75 I2C 的 SDA/SCL 引脚及 ESP32 GPIO 映射。；原因：原理图文字声明 I2C 通信，但 U3 符号和跨页网络没有画出 SDA/SCL。
- `review.memory-capacities`：请用 GD25Q32C datasheet、ESP32 具体芯片版本或固件启动日志确认 4MB Flash、520KB 内部 RAM 及是否不存在 PSRAM。；原因：原理图只给器件型号，没有直接标容量。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `bc0abcb61627503db89f5726d9e1a8f542443496918a759fc85dc7a35e59c038` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_01.png` |
| 2 | 1 | `d793c702a91b829a1ed0443879111d486c9096659a4f332009fda0bf957b5a99` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_02.png` |
| 3 | 1 | `2347347004d730ed2c13ecf63f3b37dbd4aa67bf316b4a611537ef5693ac0c53` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_03.png` |
| 4 | 1 | `c1372f4af2c403bf4c90a89570bd4298f2f3798321d992ec22775ff20096fe26` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1043/M5CAM-ESP32-A1-POWER_page_04.png` |

---

源文档：`zh_CN/unit/esp32cam.md`

源文档 SHA-256：`9d865a633284524e0677716fb57ceea1fa4df3770e60e7fd3d8e40bec00acb7c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
