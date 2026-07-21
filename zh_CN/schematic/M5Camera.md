# M5Camera 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5Camera |
| SKU | U017 |
| 产品 ID | `m5camera-24cee0cc02a5` |
| 源文档 | `zh_CN/unit/m5camera.md` |

## 概述

M5Camera 的三张原理图页面分别覆盖电源、ESP32-Wrover 与摄像头接口外围、USB 转串口和下载控制。VIN_USB 与 VBAT 经二极管汇入 VBUS，SY8089 生成 VCC_3V3，RT9182-G 再生成 2.5V 与 1.8V 电源；TP4057 提供电池充电路径。ESP32-Wrover 连接 24 针摄像头 FPC、SPM1423 数字麦克风、GPIO14 红蓝指示灯及未装的 MPU60X0/BME280，CP2104 负责 USB-UART、DTR/RTS 自动下载与复位。图面未画 OV2640 器件本体、存储容量、HY2.0-4P 接口或机械信息，且电源轨命名、SY8089 分压旁注和 USB 连接器版本存在待确认差异。

## 检索关键词

`M5Camera`、`U017`、`ESP32-Wrover`、`OV2640`、`FPC0.5-SMT-24P-B`、`SY8089`、`RT9182-G`、`TP4057`、`CP2104`、`SPM1423HM4H-B`、`MPU60X0`、`BME280`、`VIN_USB`、`VBAT`、`VBUS`、`VCC_3V3`、`VDD_2V5`、`VDD_1V8`、`VCC_2V5`、`VCC_1V8`、`USB_DP`、`USB_DN`、`USB_Micro`、`USB_CC_1`、`USB_CC_2`、`TXD0`、`RXD0`、`DTR`、`RTS`、`GPIO0`、`EN`、`GPIO14`、`GPIO23`、`GPIO22`、`GPIO4`、`GPIO2`、`DVP`、`SCCB`、`HY2.0-4P`、`4MB PSRAM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SY8089 | VBUS 到 VCC_3V3 的同步降压转换器 | 图 46c05cd332c8 / 第 1 页 / 页面上方 5V -> 3.3V DCDC Buck 区，U1 SY8089、L1 与 VCC_3V3 |
| U2 | RT9182-G | VCC_3V3 到 VDD_2V5 和 VDD_1V8 的双路 LDO | 图 46c05cd332c8 / 第 1 页 / 页面中左 3.3V -> 2V5 & 1V8 LDO 区，U2 RT9182-G |
| U3 | TP4057 | VIN_USB 到 VBAT 的电池充电管理器 | 图 46c05cd332c8 / 第 1 页 / 页面左下 U3 TP4057、VIN_USB、VBAT、LED1 与 R4 |
| D1,D2 | 1N5819 | VIN_USB 与 VBAT 到 VBUS 的双路二极管汇流 | 图 46c05cd332c8 / 第 1 页 / 页面下中 D1/D2 1N5819，VIN_USB/VBAT/VBUS 网络 |
| U4 | ESP32-Wrover | 无线主控模组，连接摄像头 FPC、USB-UART、LED、麦克风与可选传感器 | 图 794cbb7a3c54 / 第 1 页 / 页面上左 U4 ESP32-Wrover pins1-39 |
| J1 | FPC0.5-SMT-24P-B | 摄像头数据、控制、时钟和电源的 24 针 FPC 接口 | 图 794cbb7a3c54 / 第 1 页 / 页面上中 J1 FPC0.5-SMT-24P-B pins1-24 |
| U5 | SPM1423HM4H-B | DAT 接 GPIO2、CLK 接 GPIO4 的数字麦克风 | 图 794cbb7a3c54 / 第 1 页 / 页面中右 U5 SPM1423HM4H-B、DAT GPIO2、CLK GPIO4 |
| U6 | MPU60X0 | 标注为 Not Installed Optional 的惯性传感器预留位置 | 图 794cbb7a3c54 / 第 1 页 / 页面下左 U6 MPU60X0 与红色 Not Installed Optional 标注 |
| U7 | BME280 | 标注为 Not Installed Optional 的环境传感器预留位置 | 图 794cbb7a3c54 / 第 1 页 / 页面下右 U7 BME280 与红色 Not Installed Optional 标注 |
| LED2,LED3 | BLUE / RED | GPIO14 公共节点上的红蓝指示灯 | 图 794cbb7a3c54 / 第 1 页 / 页面右上 GPIO14、LED2 BLUE 与 LED3 RED |
| U8 | CP2104 | USB 到 ESP32 UART0 的串口桥及下载控制信号源 | 图 e5ccaeec1a54 / 第 1 页 / 页面中上 U8 CP2104，USB DP/DN、TXD/RXD、DTR/RTS |
| U9 | USB_Micro | VIN_USB 与 USB_DP/USB_DN 的 USB 连接器图符 | 图 e5ccaeec1a54 / 第 1 页 / 页面下中 U9 USB_Micro pins1-7 |
| VT1,VT2 | NPN-S8050 | DTR/RTS 到 EN/GPIO0 的自动下载与复位控制晶体管 | 图 e5ccaeec1a54 / 第 1 页 / 页面左上 VT1/VT2 NPN-S8050、DTR/RTS、EN/GPIO0 |
| D3,D4 | RLSD52A031V | USB_DN 与 USB_DP 的静电保护器件 | 图 e5ccaeec1a54 / 第 1 页 / 页面下中 USB_DN/USB_DP 上的 D3/D4 RLSD52A031V |
| S1 | SMT_SW_TS_015 | 将 EN 拉低的手动复位按键 | 图 e5ccaeec1a54 / 第 1 页 / 页面左下 EN、S1 SMT_SW_TS_015、R18 与 C1 |

## 系统结构

### M5Camera 硬件架构

三张页面共同描述 ESP32-Wrover 主控、J1 摄像头 FPC、SPM1423 数字麦克风、可选未装 MPU60X0/BME280、SY8089/RT9182-G/TP4057 电源链路，以及 CP2104 USB-UART 和自动下载电路。

- 参数与网络：`controller=U4 ESP32-Wrover`；`camera_connector=J1 FPC0.5-SMT-24P-B`；`microphone=U5 SPM1423HM4H-B`；`power=U1 SY8089,U2 RT9182-G,U3 TP4057`；`debug=U8 CP2104`
- 证据：图 46c05cd332c8 / 第 1 页 / 电源页全部功能区; 图 794cbb7a3c54 / 第 1 页 / 主控与外围页全部功能区; 图 e5ccaeec1a54 / 第 1 页 / USB-UART 与下载页全部功能区

### ESP32-Wrover 主控模组

U4 标为 ESP32-Wrover，由 VCC_3V3 供电并引出 EN、GPIO0-GPIO39、TXD0/RXD0；模块外部 SD0-SD3、CMD、CLK 引脚在该页标为未连接。

- 参数与网络：`reference=U4`；`module=ESP32-Wrover`；`supply=VCC_3V3`；`uart=TXD0,RXD0`；`external_flash_bus=SD0-SD3,CMD,CLK marked NC`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面上左 U4 ESP32-Wrover pins1-39

## 电源

### VBUS 到 VCC_3V3 降压

U1 SY8089 的 IN 与 EN 接 VBUS，LX 经 L1 2.2uH 输出 VCC_3V3；输入侧 C4 22uF/C5 2.2uF，输出侧 C2/C3 各 22uF，FB 分压器图符为 R1/R2。

- 参数与网络：`converter=U1 SY8089`；`input=VBUS`；`enable=VBUS`；`inductor=L1 2.2uH/0420`；`output=VCC_3V3`；`input_caps=C4 22uF/6.3V,C5 2.2uF/6.3V`；`output_caps=C2 22uF/6.3V,C3 22uF/6.3V`
- 证据：图 46c05cd332c8 / 第 1 页 / 页面上方 U1/L1/C2-C5/R1/R2 与 VBUS/VCC_3V3

### VCC_3V3 到 VDD_2V5 与 VDD_1V8

U2 RT9182-G 的 VIN、EN1 与 EN2 接 VCC_3V3，VOUT1 输出 VDD_2V5，VOUT2 输出 VDD_1V8；C8 为输入去耦，C6/C7 分别连接两路输出。

- 参数与网络：`regulator=U2 RT9182-G`；`input=VCC_3V3`；`outputs=VDD_2V5,VDD_1V8`；`capacitors=C8/C6/C7 2.2uF/6.3V`；`page_annotation=Dual Low-Noise 200mA LDO Regulator`
- 证据：图 46c05cd332c8 / 第 1 页 / 页面中左 U2 RT9182-G、C6/C7/C8、VDD_2V5/VDD_1V8

### VIN_USB 到 VBAT 充电路径

U3 TP4057 的 VCC 接 VIN_USB，BAT 输出 VBAT，PROG 经 R4 3K 接 GND；C9/C10 各 2.2uF 分别位于 VIN_USB 与 VBAT 侧，LED1/R3 连接充电状态端。

- 参数与网络：`charger=U3 TP4057`；`input=VIN_USB`；`battery_net=VBAT`；`program_resistor=R4 3K`；`input_cap=C9 2.2uF/6.3V`；`battery_cap=C10 2.2uF/6.3V`；`indicator=LED1 RED,R3 3K`
- 证据：图 46c05cd332c8 / 第 1 页 / 页面左下 U3 TP4057、R3/R4、LED1、C9/C10

### VIN_USB 与 VBAT 到 VBUS 的二极管汇流

VIN_USB 经 D1 1N5819 接入 VBUS，VBAT 经 D2 1N5819 接入同一 VBUS 网络，VBUS 再供给 SY8089。

- 参数与网络：`usb_source=VIN_USB via D1 1N5819`；`battery_source=VBAT via D2 1N5819`；`merged_net=VBUS`；`load=U1 SY8089`
- 证据：图 46c05cd332c8 / 第 1 页 / 页面下中 D1/D2 与 VIN_USB/VBAT/VBUS

### CP2104 USB 与内部电源连接

U8 的 REGIN pin7 与 VBUS pin8 接 VIN_USB，VIO pin5 与 VDD pin6 接 VDD_3V45；C19 连接 VIN_USB，C20 连接 VDD_3V45，RST pin9 由 R8 10K 上拉到 VDD_3V45。

- 参数与网络：`regin=pin7 VIN_USB`；`vbus=pin8 VIN_USB`；`vio=pin5 VDD_3V45`；`vdd=pin6 VDD_3V45`；`reset_pullup=R8 10K to VDD_3V45`；`caps=C19/C20 2.2uF/6.3V`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面中上 U8 pins5-9、R8、C19/C20

## 接口

### J1 摄像头 FPC 引脚网络

J1 为 24 针 FPC0.5-SMT-24P-B，图面引出 GPIO34、GPIO35、GPIO5、GPIO32、GPIO39、GPIO21、GPIO18、GPIO36、GPIO27、GPIO19、GPIO26、GPIO22、GPIO23、GPIO25，以及 VCC_3V3、VCC_1V8、VCC_2V5 和 GND。

- 参数与网络：`connector=J1 FPC0.5-SMT-24P-B`；`pins=24`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,23,25`；`power_labels=VCC_3V3,VCC_1V8,VCC_2V5,GND`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面上中 J1 pins1-24 的 GPIO 与电源网络标注

### GPIO14 红蓝指示灯

GPIO14 连接 LED2 BLUE 与 LED3 RED 的公共节点；LED2 另一端接 GND，LED3 另一端接 VCC_3V3，该图未在两支路画出串联限流电阻。

- 参数与网络：`gpio=14`；`blue_led=LED2 to GND`；`red_led=LED3 to VCC_3V3`；`series_resistor_shown=false`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面右上 GPIO14、LED2 BLUE、LED3 RED

### U9 USB 数据与供电连接

U9 图符标为 USB_Micro，pin1 接 VIN_USB，pin2/pin3 分别接 D-/D+，pin4 ID 未连接，pin5 及外壳脚接 GND；D-/D+ 经 R16/R17 22ohm 接 USB_DN/USB_DP。

- 参数与网络：`connector=U9 USB_Micro`；`vbus=pin1 VIN_USB`；`data_minus=pin2 via R16 22ohm to USB_DN`；`data_plus=pin3 via R17 22ohm to USB_DP`；`id=pin4 NC`；`ground=pin5 and shell`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面下中 U9 USB_Micro、R16/R17 与 USB_DN/USB_DP

## 总线

### 可选传感器 GPIO23/GPIO22 总线

U6 的 SCL/SCLK 接 GPIO23、SDA/SDI 接 GPIO22；U7 的 SCK 接 GPIO23、SDI/SDO 接 GPIO22，CSB 接 VCC_3V3、SDO 接 GND。

- 参数与网络：`clock=GPIO23`；`data=GPIO22`；`mpu60x0=SCL/SCLK=GPIO23,SDA/SDI=GPIO22`；`bme280=SCK=GPIO23,SDI/SDO=GPIO22,CSB=VCC_3V3,SDO=GND`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面下方 U6/U7 的 GPIO23/GPIO22 与配置引脚

## 复位

### EN 手动复位网络

S1 SMT_SW_TS_015 按下时将 EN 接 GND，R18 10K 将 EN 上拉到 VCC_3V3，C1 2.2uF 接在 EN 与 GND 之间，D5 并接于该节点。

- 参数与网络：`reset_net=EN`；`button=S1 SMT_SW_TS_015 to GND`；`pullup=R18 10K to VCC_3V3`；`capacitor=C1 2.2uF/6.3V`；`diode=D5`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面左下 EN、S1、R18、C1、D5

## 保护电路

### USB 数据线静电保护

USB_DN 与 USB_DP 分别连接 D3 与 D4，图面器件值标为 RLSD52A031V，两器件的公共参考端接 GND。

- 参数与网络：`usb_dn_protection=D3 RLSD52A031V`；`usb_dp_protection=D4 RLSD52A031V`；`reference=GND`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面下中 R16/R17 左侧 D3/D4 与 GND

## 音频

### SPM1423HM4H-B 数字麦克风

U5 SPM1423HM4H-B 由 VCC_3V3 供电，DAT pin5 接 GPIO2，CLK pin4 接 GPIO4，SEL pin2 与 GND pins1/3 接地，C13 2.2uF 位于供电侧。

- 参数与网络：`reference=U5`；`part=SPM1423HM4H-B`；`supply=VCC_3V3`；`data=GPIO2`；`clock=GPIO4`；`select=GND`；`decoupling=C13 2.2uF/6.3V`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面中右 U5 pins1-6 与 C13

## 传感器

### 未装的 MPU60X0 与 BME280 预留电路

U6 MPU60X0 与 U7 BME280 被红色箭头统一标注 Not Installed Optional；两者由 VCC_3V3 供电，并将 GPIO23/GPIO22 用作串行时钟和数据网络。

- 参数与网络：`population=Not Installed Optional`；`imu=U6 MPU60X0`；`environment_sensor=U7 BME280`；`clock_gpio=23`；`data_gpio=22`
- 证据：图 794cbb7a3c54 / 第 1 页 / 页面下方 U6/U7 与 Not Installed Optional 红色标注

## 调试与烧录

### CP2104 USB-UART 到 ESP32 UART0

U8 CP2104 的 DP/DM 接 USB_DP/USB_DN，TXD pin21 经 R10 470ohm 接 RXD0，RXD pin20 接 TXD0；RTS pin19 与 DTR pin23 引至自动下载电路。

- 参数与网络：`bridge=U8 CP2104`；`usb=DP=USB_DP,DM=USB_DN`；`tx_path=TXD pin21 -> R10 470ohm -> RXD0`；`rx_path=RXD pin20 -> TXD0`；`control=RTS pin19,DTR pin23`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面中上 U8 CP2104 pins3/4/19/20/21/23 与 R10

### DTR/RTS 自动下载控制

DTR 与 RTS 经 R9/R12 两只 10K 电阻进入 VT1/VT2 NPN-S8050 交叉控制网络，输出连接 ESP32 的 EN 与 GPIO0。

- 参数与网络：`inputs=DTR,RTS`；`base_resistors=R9 10K,R12 10K`；`transistors=VT1/VT2 NPN-S8050`；`targets=EN,GPIO0`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 页面左上 DTR/RTS、R9/R12、VT1/VT2、EN/GPIO0

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M5Camera 硬件架构 | `controller=U4 ESP32-Wrover`；`camera_connector=J1 FPC0.5-SMT-24P-B`；`microphone=U5 SPM1423HM4H-B`；`power=U1 SY8089,U2 RT9182-G,U3 TP4057`；`debug=U8 CP2104` |
| 系统结构 | ESP32-Wrover 主控模组 | `reference=U4`；`module=ESP32-Wrover`；`supply=VCC_3V3`；`uart=TXD0,RXD0`；`external_flash_bus=SD0-SD3,CMD,CLK marked NC` |
| 电源 | VBUS 到 VCC_3V3 降压 | `converter=U1 SY8089`；`input=VBUS`；`enable=VBUS`；`inductor=L1 2.2uH/0420`；`output=VCC_3V3`；`input_caps=C4 22uF/6.3V,C5 2.2uF/6.3V`；`output_caps=C2 22uF/6.3V,C3 22uF/6.3V` |
| 电源 | VCC_3V3 到 VDD_2V5 与 VDD_1V8 | `regulator=U2 RT9182-G`；`input=VCC_3V3`；`outputs=VDD_2V5,VDD_1V8`；`capacitors=C8/C6/C7 2.2uF/6.3V`；`page_annotation=Dual Low-Noise 200mA LDO Regulator` |
| 电源 | VIN_USB 到 VBAT 充电路径 | `charger=U3 TP4057`；`input=VIN_USB`；`battery_net=VBAT`；`program_resistor=R4 3K`；`input_cap=C9 2.2uF/6.3V`；`battery_cap=C10 2.2uF/6.3V`；`indicator=LED1 RED,R3 3K` |
| 电源 | VIN_USB 与 VBAT 到 VBUS 的二极管汇流 | `usb_source=VIN_USB via D1 1N5819`；`battery_source=VBAT via D2 1N5819`；`merged_net=VBUS`；`load=U1 SY8089` |
| 接口 | J1 摄像头 FPC 引脚网络 | `connector=J1 FPC0.5-SMT-24P-B`；`pins=24`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,23,25`；`power_labels=VCC_3V3,VCC_1V8,VCC_2V5,GND` |
| 音频 | SPM1423HM4H-B 数字麦克风 | `reference=U5`；`part=SPM1423HM4H-B`；`supply=VCC_3V3`；`data=GPIO2`；`clock=GPIO4`；`select=GND`；`decoupling=C13 2.2uF/6.3V` |
| 传感器 | 未装的 MPU60X0 与 BME280 预留电路 | `population=Not Installed Optional`；`imu=U6 MPU60X0`；`environment_sensor=U7 BME280`；`clock_gpio=23`；`data_gpio=22` |
| 总线 | 可选传感器 GPIO23/GPIO22 总线 | `clock=GPIO23`；`data=GPIO22`；`mpu60x0=SCL/SCLK=GPIO23,SDA/SDI=GPIO22`；`bme280=SCK=GPIO23,SDI/SDO=GPIO22,CSB=VCC_3V3,SDO=GND` |
| 接口 | GPIO14 红蓝指示灯 | `gpio=14`；`blue_led=LED2 to GND`；`red_led=LED3 to VCC_3V3`；`series_resistor_shown=false` |
| 接口 | U9 USB 数据与供电连接 | `connector=U9 USB_Micro`；`vbus=pin1 VIN_USB`；`data_minus=pin2 via R16 22ohm to USB_DN`；`data_plus=pin3 via R17 22ohm to USB_DP`；`id=pin4 NC`；`ground=pin5 and shell` |
| 保护电路 | USB 数据线静电保护 | `usb_dn_protection=D3 RLSD52A031V`；`usb_dp_protection=D4 RLSD52A031V`；`reference=GND` |
| 调试与烧录 | CP2104 USB-UART 到 ESP32 UART0 | `bridge=U8 CP2104`；`usb=DP=USB_DP,DM=USB_DN`；`tx_path=TXD pin21 -> R10 470ohm -> RXD0`；`rx_path=RXD pin20 -> TXD0`；`control=RTS pin19,DTR pin23` |
| 电源 | CP2104 USB 与内部电源连接 | `regin=pin7 VIN_USB`；`vbus=pin8 VIN_USB`；`vio=pin5 VDD_3V45`；`vdd=pin6 VDD_3V45`；`reset_pullup=R8 10K to VDD_3V45`；`caps=C19/C20 2.2uF/6.3V` |
| 调试与烧录 | DTR/RTS 自动下载控制 | `inputs=DTR,RTS`；`base_resistors=R9 10K,R12 10K`；`transistors=VT1/VT2 NPN-S8050`；`targets=EN,GPIO0` |
| 复位 | EN 手动复位网络 | `reset_net=EN`；`button=S1 SMT_SW_TS_015 to GND`；`pullup=R18 10K to VCC_3V3`；`capacitor=C1 2.2uF/6.3V`；`diode=D5` |
| 电源 | SY8089 反馈分压标值 | `schematic_values=R1 267K,R2 59K`；`annotation_values=R1 100K,R2 22.22K or 22K`；`annotation_output=3.327V`；`production_values=null` |
| 电源 | LDO 输出与摄像头 FPC 电源网络命名 | `ldo_outputs=VDD_2V5,VDD_1V8`；`fpc_rails=VCC_2V5,VCC_1V8`；`cross_sheet_equivalence=null` |
| 内存与 Flash | Flash、RAM 与 PSRAM 容量 | `documented_flash=4M`；`documented_ram=520K`；`documented_psram=4M / 4MB Quad`；`module_subtype=null`；`schematic_capacity=null` |
| 传感器 | OV2640 与成像参数 | `documented_sensor=OV2640`；`documented_megapixels=2`；`documented_fov_deg=65`；`documented_formats=YUV422/420,YCbCr422,8-bit compressed,RGB565/555,8-/10-bit Raw RGB` |
| 接口 | OV2640 DVP/SCCB 映射与 PWDN | `documented_control=SIOC=G23,SIOD=G22,XCLK=G27,VSYNC=G25,HREF=G26,PCLK=G21,RESET=G15`；`documented_data=D2=G32,D3=G35,D4=G34,D5=G5,D6=G39,D7=G18,D8=G36,D9=G19`；`documented_pwdn=12K pulldown`；`schematic_signal_semantics=null` |
| 接口 | HY2.0-4P 扩展接口 | `documented_scl=IO13`；`documented_sda=IO4`；`documented_power=5V,GND`；`schematic_connector=null` |
| 系统结构 | Wi-Fi 摄像头预装固件 | `documented_ssid_prefix=m5stack-`；`documented_ip=192.168.4.1`；`documented_resolution=600x800`；`documented_fps=5-6`；`firmware_version=null` |
| 系统结构 | 产品尺寸与重量 | `documented_size_mm=40.0x48.0x11.0`；`documented_weight_g=17.0`；`mechanical_drawing=null` |
| 接口 | USB 连接器硬件版本 | `schematic_connector=U9 USB_Micro`；`cc_networks=USB_CC_1 via R7 5.1K to GND; USB_CC_2 via R11 5.1K to GND`；`cc_connected_to_u9=false`；`documented_cable=USB Type-C` |
| 电源 | VBAT 电池实现与充电参数 | `charger=U3 TP4057`；`battery_net=VBAT`；`program_resistor=R4 3K`；`battery_connector=null`；`cell=null`；`protection=null`；`charge_current=null` |
| 系统结构 | 原理图与 U017 量产版本对应关系 | `product=M5Camera`；`sku=U017`；`page_date=2019/3/1`；`schematic_revision=null`；`title_block_product=null` |

## 待确认事项

- `power.sy8089-feedback-conflict`：U1 电路图中的 R1/R2 标为 267K/59K，而同页计算旁注列出 R1=100K、R2=22.22K 并以 22K 得到 3.327V；量产采用的反馈阻值不能由该页唯一确定。（证据：图 46c05cd332c8 / 第 1 页 / 页面上方 U1 右侧 R1/R2 与下方反馈计算旁注）
- `power.camera-rail-name-mismatch`：电源页把 U2 两路输出命名为 VDD_2V5/VDD_1V8，主控页 J1 使用 VCC_2V5/VCC_1V8；两组不同网络名之间没有跨页连接说明，不能由当前页面确认其电气等价关系。（证据：图 46c05cd332c8 / 第 1 页 / 页面中左 U2 输出 VDD_2V5/VDD_1V8; 图 794cbb7a3c54 / 第 1 页 / 页面上中 J1 电源脚 VCC_2V5/VCC_1V8）
- `memory.documented-capacities`：源文档描述称 ESP32 配置 4M Flash、520K RAM、4M PSRAM，规格表列 4M Flash 与 4MB Quad PSRAM；原理图只标 ESP32-Wrover，没有模组子型号、存储颗粒或容量标注。（证据：图 794cbb7a3c54 / 第 1 页 / 页面上左 U4 仅标 ESP32-Wrover，无容量或存储颗粒）
- `sensor.documented-ov2640-imaging`：源文档称图像传感器为 OV2640、最大 2MP、视角 65 度，并列出 YUV/YCbCr、RGB565/555 和 Raw RGB 输出；三张原理图只有 J1 摄像头 FPC，没有 OV2640 器件、镜头或成像参数标注。（证据：图 794cbb7a3c54 / 第 1 页 / 页面仅有 J1 摄像头 FPC，无 OV2640 图符或镜头参数）
- `interface.documented-camera-map-pwdn`：源文档把 SIOC/SIOD/XCLK/VSYNC/HREF/PCLK 映射到 G23/G22/G27/G25/G26/G21，把 D2-D9 映射到 G32/G35/G34/G5/G39/G18/G36/G19，并称 RESET 接 G15、PWDN 由 12K 下拉；图面 J1 只标 GPIO 与电源，未显示 OV2640 信号名、G15 连接或 12K PWDN 电阻。（证据：图 794cbb7a3c54 / 第 1 页 / 页面上中 J1 pins1-24 仅标 GPIO 与电源网络）
- `interface.documented-hy2-port`：源文档称 HY2.0-4P 引出 SCL=IO13、SDA=IO4、5V 与 GND；当前三张原理图没有 HY2.0-4P 连接器或这些引脚的接口连线。（证据：图 794cbb7a3c54 / 第 1 页 / 主控外围完整页面未见 HY2.0-4P 连接器）
- `system.documented-wifi-camera-firmware`：源文档称预装 ESP-IDF Wi-Fi 相机应用，创建 m5stack- 前缀 AP，在 192.168.4.1 提供 600x800、约 5-6fps 视频；原理图不包含固件镜像、SSID、IP、分辨率或帧率配置。（证据：图 794cbb7a3c54 / 第 1 页 / ESP32-Wrover 硬件页无固件或网络配置）
- `system.documented-mechanical`：源文档规格列产品尺寸 40.0x48.0x11.0mm、重量 17.0g；当前电气原理图没有板框、外壳、摄像头高度、机械公差或质量信息。（证据：图 46c05cd332c8 / 第 1 页 / 电源页无机械尺寸或质量信息）
- `interface.usb-connector-version`：USB 页的 U9 图符明确标为 USB_Micro，同时另有 USB_CC_1/USB_CC_2 各经 5.1K 接 GND 的独立支路，但两条 CC 网络未画到 U9；源文档包装内容列 USB Type-C 连接线，量产 U017 的实际连接器类型不能由这些信息唯一确定。（证据：图 e5ccaeec1a54 / 第 1 页 / 页面右上 USB_CC_1/USB_CC_2/R7/R11 与下中 U9 USB_Micro）
- `power.battery-implementation`：电源页显示 TP4057、VBAT、R4 3K 与二极管汇流，但没有电池连接器、电芯型号、容量、保护电路、温度监测或充电电流数值；源文档也未列电池规格。（证据：图 46c05cd332c8 / 第 1 页 / 页面下方 U3/TP4057/VBAT/R4，整页无电池连接器或电芯）
- `system.asset-version-binding`：三张资源的标题栏没有产品名、SKU 或修订号，主控页与 USB 页仅显示日期 2019/3/1；图面无法独立证明这些页面与当前 U017 量产版本的精确对应关系。（证据：图 46c05cd332c8 / 第 1 页 / 电源页右下空白标题栏; 图 794cbb7a3c54 / 第 1 页 / 主控页右下标题栏仅见 Date 2019/3/1; 图 e5ccaeec1a54 / 第 1 页 / USB 页右下标题栏仅见 Date 2019/3/1）
- `review.sy8089-feedback`：U017 量产板的 SY8089 反馈电阻应采用 R1/R2=267K/59K，还是旁注中的 100K/22K 组合？；原因：同一页面的器件标值与计算旁注不一致。
- `review.camera-rail-names`：VDD_2V5/VDD_1V8 与 J1 的 VCC_2V5/VCC_1V8 是否在 PCB 网表中实际相连？；原因：跨页网络名称不同，当前图片没有层次端口或网表证明其等价。
- `review.memory-capacities`：ESP32-Wrover 的具体子型号、Flash/PSRAM 容量与单位是什么？；原因：容量来自源文档，原理图未标模组子型号、存储颗粒或容量。
- `review.ov2640-imaging`：量产摄像头是否为 OV2640 2MP、65 度视角，且支持源文档列出的全部输出格式？；原因：当前原理图只有摄像头 FPC，没有传感器本体、镜头或成像参数。
- `review.camera-map-pwdn`：OV2640 的 DVP/SCCB/RESET/PWDN 在当前 U017 硬件上的完整网表连接是什么？；原因：图面只标 J1 GPIO，未显示 OV2640 信号语义、G15 或 12K PWDN 下拉。
- `review.hy2-port`：U017 的 HY2.0-4P 连接器位号、实际装配状态及 IO13/IO4 电气连接是什么？；原因：源文档列出该接口，但三张原理图均未画出。
- `review.wifi-camera-firmware`：量产预装固件的版本、SSID、IP、默认分辨率和实际帧率是什么？；原因：这些行为由固件镜像和运行环境决定，电气原理图无法确认。
- `review.mechanical`：40.0x48.0x11.0mm 外形与 17.0g 重量由哪份当前机械图和量产配置确认？；原因：电气原理图没有板框、外壳、机械公差或质量信息。
- `review.usb-connector-version`：当前 U017 量产板实际使用 Micro-USB 还是 USB Type-C，USB_CC_1/2 是否接到实际连接器？；原因：图面 U9 标为 USB_Micro，CC 下拉网络悬空，源文档包装列 Type-C 线缆。
- `review.battery-implementation`：U017 是否实际装配电池或电池接口，TP4057 的充电电流、保护与电芯边界是什么？；原因：图面只有 VBAT 与充电器，未画电池连接器、电芯、保护或充电电流。
- `review.asset-version-binding`：这三张 2019/3/1 页面对应 U017 的哪个 PCB 修订版，是否仍与当前量产硬件一致？；原因：标题栏没有产品名、SKU 或 Revision，无法从图片建立精确版本绑定。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `46c05cd332c8c7e51b5650844de2a7bceb43307c6e40f703f728119ac8562180` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp` |
| 2 | 1 | `794cbb7a3c5418d5d9ff7d5d33747368cd8abb6d109ea2d2c1f15f8c4992c8da` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp` |
| 3 | 1 | `e5ccaeec1a54e3359ebda4eef57a310709c03edeca5872b60e1ed6128bc12b6e` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp` |

---

源文档：`zh_CN/unit/m5camera.md`

源文档 SHA-256：`b574e1db9b63c1ab0c4cb69a3a2895ce50302c612d4ec549f46ec2eb44ff8682`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
