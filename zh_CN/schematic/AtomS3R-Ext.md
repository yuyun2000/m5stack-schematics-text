# AtomS3R-Ext 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R-Ext |
| SKU | C126-Ext |
| 产品 ID | `atoms3r-ext-d9543400b982` |
| 源文档 | `zh_CN/core/AtomS3R Ext.md` |

## 概述

AtomS3R-Ext 主板以 U1 ESP32-S3-PICO-1-N8R8 为主控，U2 JW5712 将 VIN_5V 转换为 VDD_3V3，并连接 BMI270/BMM150 九轴传感器、USB-C、红外驱动、用户按键及多个扩展连接器。BMI270 通过 SYS_SCL/SYS_SDA 接 ESP32，BMM150 连接 BMI270 的 A_SCL/A_SDA 辅助总线。扩展板通过 BTB1/J4 24 针连接器取得 GPIO、电源与系统 I2C，使用 LP3992-12B5F 和 WL2863E28-5/TR 生成 1.2V/2.8V，并引到 FPC1 24 针原型接口。

## 检索关键词

`AtomS3R-Ext`、`C126-Ext`、`ESP32-S3-PICO-1-N8R8`、`BMI270`、`BMM150`、`JW5712`、`LP3992-12B5F`、`WL2863E28-5/TR`、`IMP809S`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`GPIO47 IR_LED_DRV`、`GPIO41 USER_BUT`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`VDD_3V3`、`VIN_5V`、`VDDD 1.2V`、`AVDD 2.8V`、`FPC-0.5-24P`、`X0400VVS-24-LPV01`、`GPIO1`、`GPIO2`、`GPIO5`、`GPIO6`、`GPIO7`、`GPIO8`、`GPIO38`、`GPIO39`、`GPIO46`、`GPIO48`、`ESP-H0920-PIFA`、`IR LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3-PICO-1-N8R8 | 主控 SoC/模组，连接传感器、USB、射频、红外、按键和扩展 GPIO | 图 f49bdafb26fd / 第 1 页 / 主板页 A3-B3 U1 ESP32-S3-PICO-1-N8R8，GPIO0-48、USB、LNA_IN 与电源引脚 |
| U2 | JW5712 | VIN_5V 到 VDD_3V3 的 DC/DC 转换器 | 图 f49bdafb26fd / 第 1 页 / 主板页 C1-C3 U2 JW5712、L1 MWT201608S2R2 与 VDD_3V3 |
| U6 | BMI270 | 连接 SYS_SCL/SYS_SDA 的六轴 IMU，并以辅助 I2C 连接 BMM150 | 图 f49bdafb26fd / 第 1 页 / 主板页 C5-D6 U6 BMI270，SCx/SDx、ASCL/ASDx、IMU_INT |
| U9 | BMM150 | 通过 BMI270 A_SCL/A_SDA 辅助总线连接的三轴地磁传感器 | 图 f49bdafb26fd / 第 1 页 / 主板页 C5 小型 U9 BMM150，SCK/SDI 接 A_SCL/A_SDA |
| J2,F1,D3,D4 | USB-TYPEC / 6V 2A PPTC / ESD5Z3V3 | USB-C 供电、USB_D_P/N 数据与过流/ESD 保护 | 图 f49bdafb26fd / 第 1 页 / 主板页 A6-A7 J2 USB-TYPEC、F1、D3/D4、R19/R20、CC 电阻 |
| ANT1,R1,C1,C2 | ESP-H0920-PIFA / 2.4nH / 2.7pF / 2.0pF | ESP32-S3 LNA_IN 的板载 3D/PIFA 天线匹配网络 | 图 f49bdafb26fd / 第 1 页 / 主板页 A1-A2 ANT1 ESP-H0920-PIFA、R1 2.4nH、C1/C2 到 ESP_LNA |
| D2,FET2 | XMEIHUA/MHS153IRCT / CJ3134K_KF | 由 GPIO47/IR_LED_DRV 控制的低端 MOSFET 红外发射级 | 图 f49bdafb26fd / 第 1 页 / 主板页 B7 D2 红外 LED、R2 15R、FET2 CJ3134K_KF、R3 100K 与 IR_LED_DRV |
| S2 | SMT_SW_TS_015 | 将 ESP_EN 拉低到 GND 的复位/下载按键 | 图 f49bdafb26fd / 第 1 页 / 主板页 C4 S2 SMT_SW_TS_015，ESP_EN 到 GND，C17 1nF |
| J4 | XKB_X0400FVS-24 | 主板到扩展板的 24 针板对板接口 | 图 f49bdafb26fd / 第 1 页 / 主板页 A5-B5 J4 24 针，GPIO46/42/40/48/21/3/14/4/10/17/9/11/12/13/18、SYS_SCL/SDA、电源和地 |
| J5,J6,J7 | THT headers / GPIO-4P | 底部 GPIO5/6/7/8、GPIO39/38 和 Grove GPIO1/2 扩展接口 | 图 f49bdafb26fd / 第 1 页 / 主板页 B5-C6 J5 1x5、J6 1x4、J7 GPIO-4P 引脚网络 |
| FPC1 | FPC-0.5-24P | 扩展板 24 针原型/FPC 接口，承载 GPIO、1.2V、2.8V、3.3V 和控制信号 | 图 ad976aa0df7f / 第 1 页 / 扩展板页 A1-B2 FPC1 FPC-0.5-24P，pin1-26 网络 |
| BTB1 | X0400VVS-24-LPV01 | 扩展板到主板的 24 针板对板连接器 | 图 ad976aa0df7f / 第 1 页 / 扩展板页 C1-D2 BTB1，GPIO42/46/48/40/3/21/4/14/17/10/11/9/13/12/18、SYS_SCL/SDA、电源与地 |
| U1 | LP3992-12B5F | 扩展板 VDD_3V3 到 VDDD 1.2V/300mA LDO | 图 ad976aa0df7f / 第 1 页 / 扩展板页 B3 U1 LP3992-12B5F，Vout 1.2V Imax 300mA |
| U2 | WL2863E28-5/TR | 扩展板 VDD_3V3 到 AVDD 2.8V/250mA LDO | 图 ad976aa0df7f / 第 1 页 / 扩展板页 C3 U2 WL2863E28-5/TR，Vout 2.8V Imax 250mA |
| U3 | IMP809S/CN809S | 扩展板 CAM_RST 复位监控器 | 图 ad976aa0df7f / 第 1 页 / 扩展板页 D3 U3 IMP809S/CN809S，VCC VDD_3V3、/RST CAM_RST、R2/C8 |
| Q1 | CJ2301 | GPIO18 控制 VDD_3V3_IN 到 VDD_3V3 的高边电源开关 | 图 ad976aa0df7f / 第 1 页 / 扩展板页 A3 Q1 CJ2301，VDD_3V3_IN/VDD_3V3、GPIO18 与 R4 |

## 系统结构

### AtomS3R-Ext 架构

ESP32-S3-PICO-1-N8R8 主板集成 USB、电源、BMI270/BMM150、红外与扩展接口；扩展板经 24 针 BTB 连接并生成 1.2V/2.8V 后送至 FPC1。

- 参数与网络：`soc=U1 ESP32-S3-PICO-1-N8R8`；`imu=U6 BMI270 + U9 BMM150`；`main_btb=J4`；`ext_btb=BTB1`；`proto_fpc=FPC1`；`ext_rails=VDDD 1.2V; AVDD 2.8V`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板完整页; 图 ad976aa0df7f / 第 1 页 / 扩展板完整页

## 电源

### 主板 5V 到 3.3V

U2 JW5712 VIN/EN 接 VIN_5V，SW 经 L1 MWT201608S2R2 输出 VDD_3V3，R14 100KΩ/R15 22.1KΩ 构成反馈。

- 参数与网络：`input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWT201608S2R2`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VDD_3V3`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 C1-C3 U2/L1/R14/R15

### 扩展板 1.2V 与 2.8V

U1 LP3992-12B5F 从 VDD_3V3 生成 VDDD 1.2V/300mA；U2 WL2863E28-5/TR 从 VDD_3V3 生成 AVDD 2.8V/250mA。

- 参数与网络：`digital=U1 LP3992-12B5F -> VDDD 1.2V 300mA`；`analog=U2 WL2863E28-5/TR -> AVDD 2.8V 250mA`
- 证据：图 ad976aa0df7f / 第 1 页 / 扩展板页 B3/C3 U1/U2 与红字 Vout/Imax

### 扩展板 3.3V 高边开关

Q1 CJ2301 将 VDD_3V3_IN 切换到 VDD_3V3，GPIO18 通过 R4 10KΩ 控制其栅极。

- 参数与网络：`input=VDD_3V3_IN`；`output=VDD_3V3`；`switch=Q1 CJ2301`；`control=GPIO18 via R4 10KΩ`
- 证据：图 ad976aa0df7f / 第 1 页 / 扩展板页 A3 Q1/R4/GPIO18

## 接口

### USB-C 接口

J2 USB-TYPEC 的 DP/DN 经 R19/R20 22Ω 接 USB_D_P/N，CC1/CC2 各由 R4/R5 5.1KΩ 下拉，VBUS 经 F1 6V/2A PPTC 形成 VIN_5V。

- 参数与网络：`data=USB_D_P/N via R19/R20 22Ω`；`cc=R4/R5 5.1KΩ`；`vbus=F1 6V/2A PPTC -> VIN_5V`；`esd=D3/D4 ESD5Z3V3`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 A6-A7 J2/F1/R4/R5/R19/R20/D3/D4

### 底部扩展接口

J5 引出 VDD_3V3、GPIO5/6/7/8；J6 引出 GPIO39、GPIO38、VIN_5V、GND；J7 引出 GPIO1、GPIO2、VIN_5V、GND。

- 参数与网络：`J5=pin1 VDD_3V3; pin2 GPIO5; pin3 GPIO6; pin4 GPIO7; pin5 GPIO8`；`J6=GPIO39, GPIO38, VIN_5V, GND`；`J7=GPIO1, GPIO2, VIN_5V, GND`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 B5-C6 J5/J6/J7

### 主板到扩展板 24 针映射

J4/BTB1 共同传递 GPIO46/42/40/48/21/3/14/4/10/17/9/11/12/13/18、SYS_SCL、SYS_SDA、VDD_3V3 和 GND。

- 参数与网络：`main=J4 XKB_X0400FVS-24`；`extension=BTB1 X0400VVS-24-LPV01`；`signals=GPIO46,42,40,48,21,3,14,4,10,17,9,11,12,13,18,SYS_SCL,SYS_SDA`；`power=VDD_3V3/GND`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 J4 1-24; 图 ad976aa0df7f / 第 1 页 / 扩展板页 BTB1 1-28

### FPC1 原型接口

FPC1 引出 GPIO12/9/10/14/13/21/11/17/40/4/3/48/42/46、CAM_RST、SYS_SCL/SYS_SDA 所在的辅助信号，以及 AVDD、DVDD、VDD_3V3、VDDD 和 GND。

- 参数与网络：`connector=FPC1 FPC-0.5-24P`；`gpio=12,9,10,14,13,21,11,17,40,4,3,48,42,46`；`control=CAM_RST`；`rails=AVDD, DVDD, VDD_3V3, VDDD, GND`
- 证据：图 ad976aa0df7f / 第 1 页 / 扩展板页 A1-B2 FPC1 pin1-26

## 总线

### BMI270 主 I2C

ESP32 GPIO0 经 L2 33Ω 连接 SYS_SCL，GPIO45 连接 SYS_SDA；R10/R11 各 2.2KΩ 将两线拉到 VDD_3V3，U6 BMI270 SCx/SDx 接入。

- 参数与网络：`scl=GPIO0 -> L2 33Ω -> SYS_SCL`；`sda=GPIO45 -> SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U1 GPIO0/GPIO45 与 U6 SYS_SCL/SYS_SDA/R10/R11

### BMM150 辅助 I2C

BMM150 的 SCK/SDI 网络 A_SCL/A_SDA 连接 BMI270 的 ASCx/ASDx，引脚间由 R12 2.2KΩ 上拉 VDD_3V3。

- 参数与网络：`controller=U6 BMI270 sensor hub`；`scl=A_SCL`；`sda=A_SDA`；`device=U9 BMM150`；`pullup=R12 2.2KΩ shown on A_SDA/A_SCL network`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 C5-D6 U9 BMM150 与 U6 ASDx/ASCx

## GPIO 与控制信号

### BMI270 中断

U6 INT1 连接 IMU_INT，IMU_INT 对应 ESP32 GPIO15；INT2 未连接。

- 参数与网络：`interrupt=U6 INT1 -> IMU_INT -> GPIO15`；`int2_connected=false`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U6 INT1/INT2 与 U1 GPIO15 IMU_INT

### 红外发射控制

ESP32 GPIO47 连接 IR_LED_DRV，经 R3 100KΩ 控制 FET2；VDD_3V3 经 D2 与 R2 15Ω 到 FET2 漏极。

- 参数与网络：`gpio=GPIO47`；`net=IR_LED_DRV`；`mosfet=FET2 CJ3134K_KF`；`emitter=D2 XMEIHUA/MHS153IRCT`；`series=R2 15Ω`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 B7 IR LED 驱动与 U1 GPIO47

### 用户按键

ESP32 GPIO41 连接 USER_BUT，R6 10KΩ 上拉到 VDD_3V3，C11 1nF 接 GND。

- 参数与网络：`gpio=GPIO41`；`net=USER_BUT`；`pullup=R6 10KΩ`；`capacitor=C11 1nF`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U1 GPIO41 USER_BUT 与 R6/C11

## 时钟

### 外部晶振

ESP32-S3-PICO-1-N8R8 的 XTAL_P/XTAL_N 在当前主板页标记未连接，未画出外部晶振。

- 参数与网络：`xtal_p=NC`；`xtal_n=NC`；`external_crystal_shown=false`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U1 XTAL_P pin54、XTAL_N pin53 未连接标记

## 复位

### ESP32 复位

ESP_EN 由 R14 10KΩ 上拉与 C24 1uF 下拉形成 RC，S2 按下将 ESP_EN 接 GND。

- 参数与网络：`net=ESP_EN`；`pullup=R14 10KΩ`；`capacitor=C24 1uF`；`switch=S2 to GND`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 C4/D4 ESP_EN/R14/C24/S2

### 扩展接口 CAM_RST

U3 IMP809S/CN809S 由 VDD_3V3 供电，/RST 输出 CAM_RST，R2 10KΩ 上拉且 C8 1uF 接 GND。

- 参数与网络：`supervisor=U3 IMP809S/CN809S`；`output=CAM_RST`；`pullup=R2 10KΩ`；`capacitor=C8 1uF`
- 证据：图 ad976aa0df7f / 第 1 页 / 扩展板页 D3 U3/R2/C8/CAM_RST

## 内存与 Flash

### 集成 Flash 与 PSRAM

主控型号明确为 ESP32-S3-PICO-1-N8R8，原理图未画出外部 Flash/PSRAM，SPI 存储引脚标记未连接。

- 参数与网络：`soc=ESP32-S3-PICO-1-N8R8`；`external_flash_shown=false`；`external_psram_shown=false`；`integrated_marking=N8R8`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U1 型号与 SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID 未连接

## 射频

### 板载 PIFA 天线

U1 LNA_IN 通过 ESP_LNA 网络连接 ANT1 ESP-H0920-PIFA，匹配器件为 R1 2.4nH、C1 2.7pF、C2 2.0pF。

- 参数与网络：`antenna=ANT1 ESP-H0920-PIFA`；`soc_pin=U1 LNA_IN`；`matching=R1 2.4nH; C1 2.7pF; C2 2.0pF`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 A1-A3 ANT1/ESP_LNA/U1 LNA_IN

## 调试与烧录

### USB 下载调试

ESP32 GPIO19/GPIO20 分别连接 USB_D_N/USB_D_P 到 J2，GPIO0 与 ESP_EN 提供下载/复位控制。

- 参数与网络：`usb_dn=GPIO19`；`usb_dp=GPIO20`；`boot=GPIO0`；`reset=ESP_EN`
- 证据：图 f49bdafb26fd / 第 1 页 / 主板页 U1 GPIO19/20 USB_D_N/P、GPIO0 与 ESP_EN/S2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3R-Ext 架构 | `soc=U1 ESP32-S3-PICO-1-N8R8`；`imu=U6 BMI270 + U9 BMM150`；`main_btb=J4`；`ext_btb=BTB1`；`proto_fpc=FPC1`；`ext_rails=VDDD 1.2V; AVDD 2.8V` |
| 内存与 Flash | 集成 Flash 与 PSRAM | `soc=ESP32-S3-PICO-1-N8R8`；`external_flash_shown=false`；`external_psram_shown=false`；`integrated_marking=N8R8` |
| 电源 | 主板 5V 到 3.3V | `input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWT201608S2R2`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VDD_3V3` |
| 接口 | USB-C 接口 | `data=USB_D_P/N via R19/R20 22Ω`；`cc=R4/R5 5.1KΩ`；`vbus=F1 6V/2A PPTC -> VIN_5V`；`esd=D3/D4 ESD5Z3V3` |
| 总线 | BMI270 主 I2C | `scl=GPIO0 -> L2 33Ω -> SYS_SCL`；`sda=GPIO45 -> SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270` |
| 总线 | BMM150 辅助 I2C | `controller=U6 BMI270 sensor hub`；`scl=A_SCL`；`sda=A_SDA`；`device=U9 BMM150`；`pullup=R12 2.2KΩ shown on A_SDA/A_SCL network` |
| 总线地址 | BMI270 I2C 地址 | `documented_address=0x68`；`schematic_address_shown=false`；`address_pin=U6 SDO visible` |
| GPIO 与控制信号 | BMI270 中断 | `interrupt=U6 INT1 -> IMU_INT -> GPIO15`；`int2_connected=false` |
| GPIO 与控制信号 | 红外发射控制 | `gpio=GPIO47`；`net=IR_LED_DRV`；`mosfet=FET2 CJ3134K_KF`；`emitter=D2 XMEIHUA/MHS153IRCT`；`series=R2 15Ω` |
| GPIO 与控制信号 | 用户按键 | `gpio=GPIO41`；`net=USER_BUT`；`pullup=R6 10KΩ`；`capacitor=C11 1nF` |
| 复位 | ESP32 复位 | `net=ESP_EN`；`pullup=R14 10KΩ`；`capacitor=C24 1uF`；`switch=S2 to GND` |
| 射频 | 板载 PIFA 天线 | `antenna=ANT1 ESP-H0920-PIFA`；`soc_pin=U1 LNA_IN`；`matching=R1 2.4nH; C1 2.7pF; C2 2.0pF` |
| 接口 | 底部扩展接口 | `J5=pin1 VDD_3V3; pin2 GPIO5; pin3 GPIO6; pin4 GPIO7; pin5 GPIO8`；`J6=GPIO39, GPIO38, VIN_5V, GND`；`J7=GPIO1, GPIO2, VIN_5V, GND` |
| 接口 | 主板到扩展板 24 针映射 | `main=J4 XKB_X0400FVS-24`；`extension=BTB1 X0400VVS-24-LPV01`；`signals=GPIO46,42,40,48,21,3,14,4,10,17,9,11,12,13,18,SYS_SCL,SYS_SDA`；`power=VDD_3V3/GND` |
| 电源 | 扩展板 1.2V 与 2.8V | `digital=U1 LP3992-12B5F -> VDDD 1.2V 300mA`；`analog=U2 WL2863E28-5/TR -> AVDD 2.8V 250mA` |
| 接口 | FPC1 原型接口 | `connector=FPC1 FPC-0.5-24P`；`gpio=12,9,10,14,13,21,11,17,40,4,3,48,42,46`；`control=CAM_RST`；`rails=AVDD, DVDD, VDD_3V3, VDDD, GND` |
| 电源 | 扩展板 3.3V 高边开关 | `input=VDD_3V3_IN`；`output=VDD_3V3`；`switch=Q1 CJ2301`；`control=GPIO18 via R4 10KΩ` |
| 复位 | 扩展接口 CAM_RST | `supervisor=U3 IMP809S/CN809S`；`output=CAM_RST`；`pullup=R2 10KΩ`；`capacitor=C8 1uF` |
| 时钟 | 外部晶振 | `xtal_p=NC`；`xtal_n=NC`；`external_crystal_shown=false` |
| 调试与烧录 | USB 下载调试 | `usb_dn=GPIO19`；`usb_dp=GPIO20`；`boot=GPIO0`；`reset=ESP_EN` |

## 待确认事项

- `address.documented-bmi270`：产品正文给出 BMI270 地址 0x68，但当前原理图未直接标注地址值或明确 SDO 地址绑带状态。（证据：图 f49bdafb26fd / 第 1 页 / 主板页 U6 BMI270，SDO/CSB/SYS_SCL/SYS_SDA 可见但无 0x68 文本）
- `review.bmi270-address`：AtomS3R-Ext 当前 BMI270 的 SDO/地址绑带是否确保 I2C 地址固定为 0x68？；原因：0x68 来自产品正文，原理图没有直接标注地址数值，SDO 状态也未清晰给出地址含义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f49bdafb26fd74eea17cd01f86c09f6aca443b63c24d1f5eb280b9f7da32f9d9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic_page_01.png` |
| 2 | 1 | `ad976aa0df7f263e73a6ce7dda91308f7f9e9cff3d15b03f7e1906afb0fd2a97` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic_page_01.png` |

---

源文档：`zh_CN/core/AtomS3R Ext.md`

源文档 SHA-256：`0a1f27cf4cf250164677ceb181249fe6da641bcb9f2b092b8bb0d07724d8faa9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
