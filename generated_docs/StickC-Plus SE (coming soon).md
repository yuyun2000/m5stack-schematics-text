# StickC-Plus SE (coming soon) 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC-Plus SE (coming soon) |
| SKU | K016-P-SE |
| 产品 ID | `stickc-plus-se-coming-soon-7629b95652fc` |
| 源文档 | `zh_CN/core/StickC-Plus_SE.md` |

## 概述

StickC-Plus SE 单页原理图以 PICO_D4 主控连接 AXP192 电源、BM8563 RTC、CH552T USB 下载控制、SPM1423HM4H-B 数字麦克风、SGM6603-5.0 外部 5V 升压、LCD、Grove、Hat pads、用户按键和 LED/IR。图面修订注记明确写明 MPU6886 已在 SE 版本移除，U7 及外围均标 NC。AXP192 从 VBUS_VIN、VBUS_USB、VBAT_Li_Ion 管理 VESP_3V3、RTC_VDD、LCD_BL_VCC、LCD_LOGIC_VCC、MIC_VCC 与 EXT_BOOST_EN。产品仍标为 coming soon，因此正文中的 4MB Flash、240MHz/Wi-Fi、ST7789v2 135x240、120mAh、无源蜂鸣器、透明橙色外壳、尺寸重量、输入额定值、FTDI 驱动和 GPIO25/GPIO36 约束均未当作已确认量产事实。

## 检索关键词

`StickC-Plus SE`、`coming soon`、`K016-P-SE`、`PICO_D4`、`ESP32-PICO-D4`、`AXP192`、`BM8563`、`CH552T`、`SPM1423HM4H-B`、`SGM6603-5.0`、`MPU6886 removed`、`U7 NC`、`ST7789v2`、`LCD`、`Grove`、`Hat Bus`、`USB Type-C`、`GPIO0`、`GPIO2`、`GPIO9`、`GPIO10`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO26`、`GPIO32`、`GPIO33`、`GPIO34`、`GPIO35`、`GPIO36`、`GPIO37`、`GPIO38`、`GPIO39`、`SYS_SDA`、`SYS_SCL`、`SYS_INT`、`RTC_INT`、`PWR_KEY`、`LCD_SCK`、`LCD_MOSI`、`LCD_DC`、`LCD_CS`、`LCD_RST`、`LCD_BL_VCC`、`LCD_LOGIC_VCC`、`MIC_VCC`、`EXT_VDD`、`VBUS_VIN`、`VBUS_USB`、`VBAT_Li_Ion`、`VESP_3V3`、`IPSOUT`、`2.4GHz`、`4MB Flash`、`120mAh`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| PICO_D4 block | PICO_D4 | ESP32 主控 SiP，连接显示、I2C、麦克风、LED/IR、按键、UART、USB 与扩展接口 | 图 3189ab7f7aa1 / 第 1 页 / 网格 A2-C3，ESP32-PICO/PICO_D4 主控块 |
| U2 | AXP192 | 系统 PMU，管理 USB/电池输入、DCDC/LDO、电源键、扩展 5V 使能和 I2C | 图 3189ab7f7aa1 / 第 1 页 / 网格 A1-C2，U2 AXP192 |
| U4 | BM8563 | RTC_VDD 供电的 I2C 实时时钟，输出 RTC_INT | 图 3189ab7f7aa1 / 第 1 页 / 网格 C1，U4 BM8563 RTC |
| U7 [NC] | 未标注 | SE 版本未装配的原 MPU6886 IMU 占位，器件与外围均标 NC | 图 3189ab7f7aa1 / 第 1 页 / 网格 A3-A4，U7 NC 与 IMU removal revision note |
| U6 | CH552T | USB 下载与 UART/EN/GPIO0 控制协处理器 | 图 3189ab7f7aa1 / 第 1 页 / 网格 C2-D2，U6 CH552T |
| J2 | TYPEC | USB Type-C 5V 输入与 USB D+/D- 接口 | 图 3189ab7f7aa1 / 第 1 页 / 网格 D2，J2 TYPEC |
| U5 | LCD | SPI LCD 模组接口，使用独立背光与逻辑电源 | 图 3189ab7f7aa1 / 第 1 页 / 网格 C4-D4，U5 LCD |
| U3 | SPM1423HM4H-B | 数字麦克风，CLK 接 GPIO0、DATA 接 GPIO34 | 图 3189ab7f7aa1 / 第 1 页 / 网格 D3-D4，U3 SPM1423HM4H-B |
| U8 | SGM6603-5.0 | IPSOUT 至 EXT_VDD 的 5V 升压转换器 | 图 3189ab7f7aa1 / 第 1 页 / 网格 C3-D3，U8 SGM6603-5.0 |
| J1 | GROVE | GPIO32/GPIO33、EXT_VDD 与 GND 的 4 针 Grove 接口 | 图 3189ab7f7aa1 / 第 1 页 / 网格 D3，J1 GROVE |
| BAT1,Li_Ion | DMS_3R3 / 2-pin | RTC 备份与锂电池接口，连接 VBAT_RTC 与 VBAT_Li_Ion | 图 3189ab7f7aa1 / 第 1 页 / 网格 C1，BAT1 DMS_3R3 与 Li_Ion |
| S1,S2,S3 | TS_1015POWER / TS_015BUTTONB / PTS_820BUTTONA | 电源键与 GPIO39/GPIO37 两个用户按键 | 图 3189ab7f7aa1 / 第 1 页 / 网格 D2-D3，S1 Power、S2 BUTTONB、S3 BUTTONA |
| E1,L1,C1,C2 | ANT / 1.8nH / 1.2pF / 1.5pF | ESP32 LNA_IN 的板载天线匹配网络 | 图 3189ab7f7aa1 / 第 1 页 / 网格 A3，E1 ANT 与 L1/C1/C2 |
| LED1,LED2 | IR / RED LED | GPIO9 红外发射与 GPIO10 红色状态 LED 支路 | 图 3189ab7f7aa1 / 第 1 页 / 网格 C3，LED/IR 区 |

## 系统结构

### StickC-Plus SE 图面架构

PICO_D4 主控连接 AXP192、BM8563、CH552T、LCD、SPM1423HM4H-B、LED/IR、三个按键、Grove 和 Hat pads；AXP192 与 SGM6603-5.0 提供系统和扩展电源。

- 参数与网络：`controller=PICO_D4`；`pmu=U2 AXP192`；`rtc=U4 BM8563`；`usb_controller=U6 CH552T`；`microphone=U3 SPM1423HM4H-B`；`boost=U8 SGM6603-5.0`；`interfaces=LCD,Grove,Hat,USB Type-C`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 完整单页各功能区

### SE 版本删除 MPU6886

IMU 区的 U7 器件值标为 NC，C21、C28、C29 也标 NC；修订注记明确写明 MPU6886 was removed in version SE and only exists in versions V1.1 and earlier。

- 参数与网络：`se_imu=removed`；`legacy_imu=MPU6886`；`legacy_versions=V1.1 and earlier`；`reference=U7 NC`；`optional_parts=C21/C28/C29 NC`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 A3-A4，IMU U7 NC 与 Revision Note

## 核心器件

### PICO_D4 主控

主控块明确标 PICO_D4，EN 接 ESP32_EN，GPIO0-GPIO39 分配给 LCD、麦克风、I2C、按键、LED/IR、UART 与扩展网络。

- 参数与网络：`part_number=PICO_D4`；`enable=ESP32_EN`；`uart=ESP32_U0TXD/ESP32_U0RXD`；`i2c=GPIO21 SYS_SDA,GPIO22 SYS_SCL`；`microphone=GPIO0/GPIO34`；`buttons=GPIO37/GPIO39`；`led_ir=GPIO10/GPIO9`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 A2-C3，PICO_D4 GPIO 与电源引脚

### BM8563 RTC

U4 BM8563 的 SDA/SCL 接 SYS_SDA/SYS_SCL，VDD 接 RTC_VDD，INT 输出 RTC_INT，OSCI/OSCO 连接 Y1 32.768K。

- 参数与网络：`reference=U4`；`part_number=BM8563`；`supply=RTC_VDD`；`bus=SYS_SDA/SYS_SCL`；`interrupt=RTC_INT`；`crystal=Y1 32.768K`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C1，U4 BM8563

## 电源

### AXP192 输入与电池

U2 AXP192 的 ACIN 接 VBUS_VIN、VBUS 接 VBUS_USB、BAT 接 VBAT_Li_Ion、BACKUP 接 VBAT_RTC，并通过 SYS_SDA/SYS_SCL 连接系统 I2C。

- 参数与网络：`acin=VBUS_VIN`；`vbus=VBUS_USB`；`battery=VBAT_Li_Ion`；`backup=VBAT_RTC`；`sda=SYS_SDA`；`scl=SYS_SCL`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 A1-B2，U2 AXP192 输入与 I2C

### AXP192 电源输出

AXP192 DCDC1 经 L2 2.2uH 输出 VESP_3V3；LDO1 输出 RTC_VDD，LDO2 输出 LCD_BL_VCC，LDO3 输出 LCD_LOGIC_VCC，GPIO0 输出 MIC_VCC，EXTEN 输出 EXT_BOOST_EN，IPSOUT 为系统和扩展电源源。

- 参数与网络：`dcdc1=VESP_3V3`；`ldo1=RTC_VDD`；`ldo2=LCD_BL_VCC`；`ldo3=LCD_LOGIC_VCC`；`gpio0=MIC_VCC`；`exten=EXT_BOOST_EN`；`main_output=IPSOUT`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 A1-C2，U2 DCDC/LDO/GPIO0/EXTEN/IPSOUT

### EXT_VDD 5V 升压

U8 SGM6603-5.0 以 IPSOUT 为输入，经 L4 4.7uH 生成 EXT_VDD，EN 由 EXT_BOOST_EN 控制并由 R18 100K 下拉。

- 参数与网络：`input=IPSOUT`；`output=EXT_VDD`；`inductor=L4 4.7uH`；`enable=EXT_BOOST_EN`；`pulldown=R18 100K`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C3-D3，U8 5VOUT_BOOST

## 接口

### LCD SPI 接口

LCD U5 的 SCK、MOSI、RS、CS、RESET 分别连接 GPIO13、GPIO15、GPIO23、GPIO5、GPIO18，LEDA 使用 LCD_BL_VCC，VDD 使用 LCD_LOGIC_VCC。

- 参数与网络：`sck=GPIO13`；`mosi=GPIO15`；`dc=GPIO23`；`cs=GPIO5`；`reset=GPIO18`；`backlight=LCD_BL_VCC`；`logic=LCD_LOGIC_VCC`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C4-D4，U5 LCD 与 PICO_D4 LCD nets

### USB Type-C

J2 VCC 接 VBUS_USB，A6/B6 与 A7/B7 分别汇入 USB_DP/USB_DM，CC1/CC2 经 R13/R19 5.1K 接地，D3/D4 ESD3.3V 保护数据线。

- 参数与网络：`vbus=VBUS_USB`；`dp=USB_DP`；`dm=USB_DM`；`cc1=R13 5.1K`；`cc2=R19 5.1K`；`esd=D3/D4 ESD3.3V`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D2，J2 USB TYPE-C

### Grove 接口

J1 Grove 的 pin1 为 GND、pin2 为 EXT_VDD、pin3 为 GPIO32、pin4 为 GPIO33；GPIO32/33 各有 ESD3.3V 保护，C37 10uF 为电源去耦。

- 参数与网络：`pin1=GND`；`pin2=EXT_VDD`；`pin3=GPIO32`；`pin4=GPIO33`；`protection=D1/D2 ESD3.3V`；`capacitor=C37 10uF`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D3，J1 GROVE

### Hat 与测试焊盘

底部焊盘引出 VESP_3V3、GPIO2、GPIO38、GPIO25、GPIO26、GPIO36、GPIO0、GND、VIN/VBUS_VIN 与 5VOUT/EXT_VDD。

- 参数与网络：`pad1=VESP_3V3`；`pad2=GPIO2`；`pad3=GPIO38`；`pad4=GPIO36`；`pad5=GPIO0`；`pad6=VIN/VBUS_VIN`；`pad7=5VOUT/EXT_VDD`；`pad8=GND`；`pad9=GPIO26`；`pad10=GPIO25`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D1，PAD1-PAD10

## 总线

### 系统 I2C 总线

PICO_D4 GPIO21/GPIO22 分别连接 SYS_SDA/SYS_SCL，R4/R3 各 2.2K 上拉至 VESP_3V3；总线连接 AXP192 与 BM8563，SE 版本 U7 IMU 位为 NC。

- 参数与网络：`sda=GPIO21/SYS_SDA`；`scl=GPIO22/SYS_SCL`；`pullups=R4/R3 2.2K`；`installed_devices=AXP192,BM8563`；`imu_slot=U7 NC`
- 证据：图 3189ab7f7aa1 / 第 1 页 / U2/U4/PICO_D4 SYS_SDA/SCL 与 U7 NC

## 总线地址

### I2C 地址可见性

原理图没有为 AXP192 或 BM8563 标注数值 I2C 地址，已删除的 U7 IMU 位也没有有效器件地址。

- 参数与网络：`AXP192=null`；`BM8563=null`；`IMU=not installed`
- 证据：图 3189ab7f7aa1 / 第 1 页 / U2 AXP192、U4 BM8563 与 U7 NC，无地址注释

## GPIO 与控制信号

### 电源键与用户按键

S1 将 PWR_KEY 拉低；S2 BUTTONB 接 GPIO39，S3 BUTTONA 接 GPIO37，两个用户按键均有 VESP_3V3 上拉与 ESD3.3V 保护。

- 参数与网络：`power=S1/PWR_KEY`；`button_b=S2/GPIO39`；`button_a=S3/GPIO37`；`protection=ESD3.3V`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D2-D3，S1/S2/S3

### 红外发射与红色 LED

GPIO9 连接 LED1_IR 支路，GPIO10 连接 LED2_RED 支路，两路连接 VESP_3V3 并带 ESD3.3V 保护。

- 参数与网络：`infrared=GPIO9/LED1_IR`；`red_led=GPIO10/LED2_RED`；`supply=VESP_3V3`；`protection=D6/D7 ESD3.3V`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C3，LED/IR

## 时钟

### RTC 32.768K 时钟

BM8563 OSCI/OSCO 使用 Y1 32.768K/6pF 晶振，C9/C12 各 6pF 接地。

- 参数与网络：`frequency=32.768K`；`load=6pF`；`capacitors=C9/C12 6pF`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C1，Y1/C9/C12

## 保护电路

### 外部信号 ESD 保护

USB DP/DM、GPIO0/25/26/32/33/36、GPIO9/10 与两个用户按键网络均配置 ESD3.3V 钳位器件，USB CC1/CC2 各以 5.1K 下拉。

- 参数与网络：`protected=USB_DP,USB_DM,GPIO0,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36,GPIO9,GPIO10,BUTTONA,BUTTONB`；`usb_cc=5.1K pulldown`
- 证据：图 3189ab7f7aa1 / 第 1 页 / USB、GPO/EN/UART、LED/IR、GROVE 与按键各 ESD 区

## 关键网络

### RTC_INT 与电源键

RTC_INT 通过 R401 10K 与 C401 10uF 网络连接 PWR_KEY，PWR_KEY 同时连接 AXP192 PWRON 与 S1 电源按键。

- 参数与网络：`rtc_interrupt=RTC_INT`；`resistor=R401 10K`；`capacitor=C401 10uF`；`power_key=PWR_KEY`；`pmu=AXP192 PWRON`；`button=S1`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D4，RTC_INT/R401/C401/PWR_KEY 与 U2/S1

## 音频

### SPM1423 数字麦克风

U3 SPM1423HM4H-B 的 CLK 接 GPIO0，DATA 接 GPIO34，VCC 接 MIC_VCC，SELECT 与两只 GND 引脚接地。

- 参数与网络：`part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`supply=MIC_VCC`；`select=GND`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 D3-D4，U3 I2S_MIC

## 射频

### 板载天线匹配

PICO_D4 LNA_IN 经 L1 1.8nH/HQ 和 C1 1.2pF、C2 1.5pF 匹配网络连接 E1 ANT。

- 参数与网络：`source=PICO_D4 LNA_IN`；`inductor=L1 1.8nH/HQ`；`capacitors=C1 1.2pF,C2 1.5pF`；`antenna=E1 ANT`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 A3，LNA_IN/L1/C1/C2/E1

## 调试与烧录

### CH552T 下载控制

J2 USB_DP/USB_DM 连接 U6 CH552T；CH552_TXD/CH552_RXD 连接 ESP32_U0RXD/ESP32_U0TXD，并通过 CJ2302 MOS 管网络控制 ESP32_EN 与 GPIO0。

- 参数与网络：`controller=U6 CH552T`；`usb=USB_DP/USB_DM`；`uart=CH552_TXD/RXD to ESP32_U0RXD/TXD`；`auto_download=CJ2302 MOS network to ESP32_EN/GPIO0`
- 证据：图 3189ab7f7aa1 / 第 1 页 / 网格 C2-D3，CH552 与 GPO/EN/UART 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StickC-Plus SE 图面架构 | `controller=PICO_D4`；`pmu=U2 AXP192`；`rtc=U4 BM8563`；`usb_controller=U6 CH552T`；`microphone=U3 SPM1423HM4H-B`；`boost=U8 SGM6603-5.0`；`interfaces=LCD,Grove,Hat,USB Type-C` |
| 系统结构 | SE 版本删除 MPU6886 | `se_imu=removed`；`legacy_imu=MPU6886`；`legacy_versions=V1.1 and earlier`；`reference=U7 NC`；`optional_parts=C21/C28/C29 NC` |
| 核心器件 | PICO_D4 主控 | `part_number=PICO_D4`；`enable=ESP32_EN`；`uart=ESP32_U0TXD/ESP32_U0RXD`；`i2c=GPIO21 SYS_SDA,GPIO22 SYS_SCL`；`microphone=GPIO0/GPIO34`；`buttons=GPIO37/GPIO39`；`led_ir=GPIO10/GPIO9` |
| 电源 | AXP192 输入与电池 | `acin=VBUS_VIN`；`vbus=VBUS_USB`；`battery=VBAT_Li_Ion`；`backup=VBAT_RTC`；`sda=SYS_SDA`；`scl=SYS_SCL` |
| 电源 | AXP192 电源输出 | `dcdc1=VESP_3V3`；`ldo1=RTC_VDD`；`ldo2=LCD_BL_VCC`；`ldo3=LCD_LOGIC_VCC`；`gpio0=MIC_VCC`；`exten=EXT_BOOST_EN`；`main_output=IPSOUT` |
| 总线 | 系统 I2C 总线 | `sda=GPIO21/SYS_SDA`；`scl=GPIO22/SYS_SCL`；`pullups=R4/R3 2.2K`；`installed_devices=AXP192,BM8563`；`imu_slot=U7 NC` |
| 总线地址 | I2C 地址可见性 | `AXP192=null`；`BM8563=null`；`IMU=not installed` |
| 核心器件 | BM8563 RTC | `reference=U4`；`part_number=BM8563`；`supply=RTC_VDD`；`bus=SYS_SDA/SYS_SCL`；`interrupt=RTC_INT`；`crystal=Y1 32.768K` |
| 时钟 | RTC 32.768K 时钟 | `frequency=32.768K`；`load=6pF`；`capacitors=C9/C12 6pF` |
| 关键网络 | RTC_INT 与电源键 | `rtc_interrupt=RTC_INT`；`resistor=R401 10K`；`capacitor=C401 10uF`；`power_key=PWR_KEY`；`pmu=AXP192 PWRON`；`button=S1` |
| 接口 | LCD SPI 接口 | `sck=GPIO13`；`mosi=GPIO15`；`dc=GPIO23`；`cs=GPIO5`；`reset=GPIO18`；`backlight=LCD_BL_VCC`；`logic=LCD_LOGIC_VCC` |
| 音频 | SPM1423 数字麦克风 | `part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`supply=MIC_VCC`；`select=GND` |
| 调试与烧录 | CH552T 下载控制 | `controller=U6 CH552T`；`usb=USB_DP/USB_DM`；`uart=CH552_TXD/RXD to ESP32_U0RXD/TXD`；`auto_download=CJ2302 MOS network to ESP32_EN/GPIO0` |
| 接口 | USB Type-C | `vbus=VBUS_USB`；`dp=USB_DP`；`dm=USB_DM`；`cc1=R13 5.1K`；`cc2=R19 5.1K`；`esd=D3/D4 ESD3.3V` |
| 电源 | EXT_VDD 5V 升压 | `input=IPSOUT`；`output=EXT_VDD`；`inductor=L4 4.7uH`；`enable=EXT_BOOST_EN`；`pulldown=R18 100K` |
| 接口 | Grove 接口 | `pin1=GND`；`pin2=EXT_VDD`；`pin3=GPIO32`；`pin4=GPIO33`；`protection=D1/D2 ESD3.3V`；`capacitor=C37 10uF` |
| 接口 | Hat 与测试焊盘 | `pad1=VESP_3V3`；`pad2=GPIO2`；`pad3=GPIO38`；`pad4=GPIO36`；`pad5=GPIO0`；`pad6=VIN/VBUS_VIN`；`pad7=5VOUT/EXT_VDD`；`pad8=GND`；`pad9=GPIO26`；`pad10=GPIO25` |
| GPIO 与控制信号 | 电源键与用户按键 | `power=S1/PWR_KEY`；`button_b=S2/GPIO39`；`button_a=S3/GPIO37`；`protection=ESD3.3V` |
| GPIO 与控制信号 | 红外发射与红色 LED | `infrared=GPIO9/LED1_IR`；`red_led=GPIO10/LED2_RED`；`supply=VESP_3V3`；`protection=D6/D7 ESD3.3V` |
| 射频 | 板载天线匹配 | `source=PICO_D4 LNA_IN`；`inductor=L1 1.8nH/HQ`；`capacitors=C1 1.2pF,C2 1.5pF`；`antenna=E1 ANT` |
| 保护电路 | 外部信号 ESD 保护 | `protected=USB_DP,USB_DM,GPIO0,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36,GPIO9,GPIO10,BUTTONA,BUTTONB`；`usb_cc=5.1K pulldown` |
| 系统结构 | coming soon 产品状态与量产版本 | `product=StickC-Plus SE`；`sku=K016-P-SE`；`status=coming soon`；`schematic_resource=K016-P-SE-SCH_StickC-Plus-SE_SCH`；`production_revision=null`；`release_date=null`；`final_bom=null` |
| 内存与 Flash | ESP32-PICO-D4 4MB Flash | `documented_capacity=4MB`；`schematic_part=PICO_D4`；`external_flash=null`；`capacity_label=null` |
| 核心器件 | ST7789v2 LCD 参数 | `documented_driver=ST7789v2`；`documented_size=1.14 inch`；`documented_resolution=135x240`；`schematic=U5 LCD generic` |
| 音频 | GPIO2 无源蜂鸣器 | `documented_signal=GPIO2`；`documented_device=passive buzzer`；`schematic=PAD2 GPIO2 only`；`buzzer_reference=null`；`driver=null` |
| 电源 | 3.7V 120mAh 电池 | `documented_voltage=3.7V`；`documented_capacity=120mAh`；`schematic=Li_Ion/VBAT_Li_Ion`；`battery_part=null`；`protection=null` |
| 系统结构 | 主频与 Wi-Fi 规格 | `documented_cpu=dual-core 240MHz`；`documented_dmips=600`；`documented_sram=520KB`；`documented_radio=2.4GHz Wi-Fi`；`schematic=PICO_D4 and E1 antenna path` |
| 调试与烧录 | USB 驱动与 CH552T | `documented_driver=FTDI VCP`；`schematic_controller=U6 CH552T`；`usb_vid_pid=null`；`production_firmware=null` |
| GPIO 与控制信号 | GPIO25/GPIO36 共用约束 | `documented_constraint=GPIO25/GPIO36 shared port`；`pad_gpio25=PAD10`；`pad_gpio36=PAD4`；`schematic_shared_path=null` |
| 电源 | 5V 输入额定范围 | `documented_nominal=5V@500mA`；`documented_range=4.8-5.5V`；`schematic_inputs=VBUS_VIN,VBUS_USB`；`schematic_rating=null` |
| 其他事实 | 外壳、尺寸、重量与工作温度 | `documented_shell=transparent orange`；`documented_size=48.0x24.0x13.5mm`；`documented_weight=16.9g`；`documented_temperature=0-60C`；`schematic_mechanical_data=null` |

## 待确认事项

- `system.release-status`：产品清单名称与源文档标题均标 StickC-Plus SE (coming soon)，产品图片为 coming-soon 占位；原理图资源名含 K016-P-SE，但图面没有量产修订号、发布日期、最终 BOM 或认证状态。（证据：图 3189ab7f7aa1 / 第 1 页 / 完整图面无标题栏、量产修订号或日期）
- `memory.documented-flash`：产品源文档标注 4MB Flash，图面只标 PICO_D4 封装块，没有独立 Flash 或内部容量字段，尚未确认 coming-soon 量产批次的存储容量。（证据：图 3189ab7f7aa1 / 第 1 页 / PICO_D4 主控块，无 Flash 容量标注）
- `component.documented-lcd`：产品源文档标注 1.14 英寸 135x240 ST7789v2 彩色 TFT，图面 U5 只标 LCD 与信号/电源脚，没有驱动器型号、尺寸或分辨率。（证据：图 3189ab7f7aa1 / 第 1 页 / U5 LCD，无驱动器/尺寸/分辨率）
- `audio.documented-buzzer`：产品源文档称 GPIO2 连接板载无源蜂鸣器，当前完整原理图只在 PAD2 引出 GPIO2，未见蜂鸣器位号、器件或驱动电路。（证据：图 3189ab7f7aa1 / 第 1 页 / PAD2 GPIO2，整页无蜂鸣器电路）
- `power.documented-battery`：产品源文档标注内置 3.7V 120mAh 锂电池，图面只显示 Li_Ion 两针接口与 VBAT_Li_Ion 网络，没有容量、料号、保护参数或连接器实物规格。（证据：图 3189ab7f7aa1 / 第 1 页 / Li_Ion 两针接口与 U2 BAT）
- `system.documented-performance-radio`：产品源文档标注 ESP32-PICO-D4 双核 240MHz、600 DMIPS、520KB SRAM 与 2.4GHz Wi-Fi；图面确认 PICO_D4 和天线链路，但未直接标这些性能、内存或无线参数。（证据：图 3189ab7f7aa1 / 第 1 页 / PICO_D4 与 E1 ANT，无性能/协议参数）
- `debug.documented-ftdi-driver`：产品源文档要求安装 FTDI 驱动，图面 USB 下载控制器明确标为 U6 CH552T；coming-soon 产品实际 USB 设备标识、驱动需求和量产固件需确认。（证据：图 3189ab7f7aa1 / 第 1 页 / U6 CH552T 与 USB_DP/DM）
- `gpio.documented-g25-g36-sharing`：产品源文档称 GPIO36 与 GPIO25 共用同一端口，使用一者时需将另一者设为浮空；图面将 GPIO25 和 GPIO36 分别引到 PAD10 与 PAD4，没有画出两者之间的共用模拟开关或连接。（证据：图 3189ab7f7aa1 / 第 1 页 / PAD10 GPIO25 与 PAD4 GPIO36，图中无共用连接）
- `power.documented-input-rating`：产品源文档标注 5V@500mA，并另称 VBUS_VIN 与 VBUS_USB 输入限制为 4.8-5.5V；图面显示两路输入接 AXP192，但未标额定电流、输入范围或保护边界。（证据：图 3189ab7f7aa1 / 第 1 页 / U2 AXP192 VBUS_VIN/VBUS_USB，无输入额定值）
- `other.documented-mechanical`：产品源文档标注透明橙色外壳、48.0x24.0x13.5mm、16.9g 和 0-60°C；当前电气原理图没有机械外观、尺寸、重量、材料或温度额定信息。（证据：图 3189ab7f7aa1 / 第 1 页 / 完整电气原理图，无机械/温度信息）
- `review.release-status`：请在正式发布后提供 K016-P-SE 量产修订号、发布日期、最终 BOM 与认证状态。；原因：当前产品仍标 coming soon，图面无量产版本信息。
- `review.flash`：请确认 K016-P-SE 量产 PICO_D4 的内部 Flash 是否固定为 4MB。；原因：容量仅来自 coming-soon 正文，图面未标。
- `review.lcd`：请提供量产 LCD BOM 或子板原理图，确认 ST7789v2、1.14 英寸和 135x240 分辨率。；原因：U5 只标 LCD。
- `review.buzzer`：请确认 GPIO2 无源蜂鸣器的料号、驱动方式与原理图位置。；原因：当前整页只引出 GPIO2，未画蜂鸣器。
- `review.battery`：请确认量产内置电池的 3.7V 120mAh 料号、保护参数、连接器与充放电额定值。；原因：图面只显示 Li_Ion/VBAT_Li_Ion。
- `review.performance-radio`：请确认量产主频、DMIPS、SRAM、2.4GHz Wi-Fi 与天线性能参数。；原因：这些参数未在图面标注。
- `review.usb-driver`：请确认量产 CH552T 的 USB VID/PID、固件与实际驱动需求，正文 FTDI 驱动说明是否应保留。；原因：正文驱动说明与图面 U6 CH552T 不一致。
- `review.g25-g36-sharing`：请提供 GPIO25/GPIO36 共用端口的实际电路或硬件约束来源。；原因：图面只显示两个独立焊盘。
- `review.input-rating`：请确认 VBUS_VIN/VBUS_USB 的 4.8-5.5V、500mA 额定值、浪涌与保护边界。；原因：图面未标输入额定值。
- `review.mechanical`：请在正式发布后用机械图、实物与规格书确认外壳颜色、尺寸、重量和工作温度。；原因：当前原理图不包含这些信息，产品仍处于 coming soon。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3189ab7f7aa1c69f1568c46e554b9d91de9fd0000ca9395b334b1eee5ed80ed5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-SCH_StickC-Plus-SE_SCH.png` |

---

源文档：`zh_CN/core/StickC-Plus_SE.md`

源文档 SHA-256：`bf92592651295707bab09886668667b9f06edd206f5a20a3845206fa3065ae96`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
