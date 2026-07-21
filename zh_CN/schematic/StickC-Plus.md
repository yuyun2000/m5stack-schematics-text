# StickC-Plus 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC-Plus |
| SKU | K016-P |
| 产品 ID | `stickc-plus-12af40664144` |
| 源文档 | `zh_CN/core/m5stickc_plus.md` |

## 概述

StickC-Plus 以 ESP32-PICO-D4 为主控，连接 AXP192 PMU、BM8563 RTC、MPU6886 IMU、SPI LCD、SPM1423 I2S 麦克风、LED/IR、按键及 Grove/HAT 扩展。USB Type-C 数据先进入 CH552，再以 UART 和自动下载控制连接 ESP32；AXP192 通过 DCDC1/LDO1-3 分配 VESP_3V3、RTC_VDD、LCD 背光/逻辑与 MIC_VCC。IPSOUT 另经 SGM6603-5.0 受控升压形成 EXT_VDD，供 Grove 和外部 5V 使用。

## 检索关键词

`StickC-Plus`、`K016-P`、`ESP32-PICO-D4`、`AXP192`、`BM8563`、`MPU6886`、`CH552`、`SPM1423HM4H-B`、`SGM6603-5.0`、`USB Type-C`、`SYS_SDA`、`SYS_SCL`、`SYS_INT`、`RTC_INT`、`PWR_KEY`、`VESP_3V3`、`IPSOUT`、`RTC_VDD`、`LCD_BL_VCC`、`LCD_LOGIC_VCC`、`MIC_VCC`、`EXT_VDD`、`GPIO0 MIC_CLK`、`GPIO34 MIC_DATA`、`GPIO5 LCD_CS`、`GPIO13 LCD_SCK`、`GPIO15 LCD_MOSI`、`GPIO18 LCD_RST`、`GPIO23 LCD_DC`、`GPIO9 IR`、`GPIO10 LED`、`GPIO37 BUTTON_A`、`GPIO39 BUTTON_B`、`GROVE`、`HAT`、`CH552_TXD`、`CH552_RXD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-D4 | 主控 SiP，连接显示、I2C 设备、麦克风、LED/IR、按键、UART 和扩展接口 | 图 bf4d2d939b03 / 第 1 页 / A2-B3 ESP32-PICO 区，PICO_D4 |
| U2 | AXP192 | 系统 PMU，管理 USB/电池输入、充电、DCDC/LDO、电源键和 I2C 监控 | 图 bf4d2d939b03 / 第 1 页 / A1-C1 PMU 区，U2 AXP192 |
| U4 | BM8563 | 电池备份 RTC，通过 SYS_SDA/SYS_SCL 连接主控并输出 RTC_INT | 图 bf4d2d939b03 / 第 1 页 / C1 RTC 区，U4 BM8563 |
| U7 | MPU6886 | 六轴 IMU，通过 SYS_SDA/SYS_SCL 连接主控并输出 SYS_INT | 图 bf4d2d939b03 / 第 1 页 / A4-B4 IMU 区，U7 MPU6886 |
| U6 | CH552 | USB 转 UART/下载控制协处理器，连接 USB DP/DM 与 ESP32 UART/EN/GPIO0 | 图 bf4d2d939b03 / 第 1 页 / C2-D2 CH552 区，U6 CH552 |
| J2 | TYPEC | USB Type-C 5V 输入与 USB 2.0 数据接口 | 图 bf4d2d939b03 / 第 1 页 / D1-D2 USB TYPE-C 区，J2 TYPEC |
| U5 | LCD | SPI TFT LCD 连接器/模组，使用独立背光和逻辑电源 | 图 bf4d2d939b03 / 第 1 页 / C4-D4 IPS_LCD 区，U5 LCD |
| U3 | SPM1423HM4H-B | I2S/PDM 数字麦克风，CLK 接 GPIO0、DATA 接 GPIO34 | 图 bf4d2d939b03 / 第 1 页 / D3-D4 I2S_MIC 区，U3 SPM1423HM4H-B |
| U8 | SGM6603-5.0 | 由 IPSOUT 升压生成 EXT_VDD 的 5V 转换器 | 图 bf4d2d939b03 / 第 1 页 / C3-D3 5VOUT_BOOST 区，U8 SGM6603-5.0 |
| J1 | GROVE | 4 针 Grove 接口，提供 GPIO32/GPIO33、EXT_VDD 和 GND | 图 bf4d2d939b03 / 第 1 页 / D3 GROVE 区，J1 pins 1-4 |
| BAT1/Li_Ion | DMS_3R3 / 2-pin | 锂电池与 RTC 备份电池接口，连接 VBAT_Li_Ion 与 VBAT_RTC | 图 bf4d2d939b03 / 第 1 页 / C1 电池接口区，Li_Ion 与 BAT1 DMS_3R3 |
| S1/S2/S3 | TS_1015POWER/TS-1109S | 电源键与 GPIO39/GPIO37 两个用户按键 | 图 bf4d2d939b03 / 第 1 页 / D2-D3 POWER/按键区，S1/S2/S3 |
| E1 | ANT | ESP32 射频天线，带 L1/C1/C2 匹配网络 | 图 bf4d2d939b03 / 第 1 页 / A3，E1 ANT 与 L1/C1/C2 |
| LED1/LED2 | IR/RED LED | GPIO9 红外发射与 GPIO10 红色状态 LED | 图 bf4d2d939b03 / 第 1 页 / C3-D3 LED/IR 区 |

## 系统结构

### StickC-Plus 系统架构

ESP32-PICO-D4 连接 AXP192、BM8563、MPU6886、CH552、LCD、SPM1423 麦克风、LED/IR、按键及 Grove/HAT；AXP192 和 SGM6603-5.0 形成多路系统与扩展电源。

- 参数与网络：`mcu=U1 ESP32-PICO-D4`；`pmu=U2 AXP192`；`rtc=U4 BM8563`；`imu=U7 MPU6886`；`usb_bridge=U6 CH552`；`mic=U3 SPM1423HM4H-B`
- 证据：图 bf4d2d939b03 / 第 1 页 / 完整原理图页

## 核心器件

### ESP32-PICO-D4

主控块明确标 PICO_D4，EN 接 ESP32_EN，GPIO0-39 分配给 LCD、麦克风、I2C、按键、LED/IR、UART 与扩展接口。

- 参数与网络：`part_number=ESP32-PICO-D4`；`reset=ESP32_EN`；`power=VESP_3V3`；`uart=ESP32_U0TXD/ESP32_U0RXD`
- 证据：图 bf4d2d939b03 / 第 1 页 / A2-B3 ESP32-PICO 区

### U4 BM8563

U4 BM8563 的 SDA/SCL 接 SYS_SDA/SYS_SCL，VDD 接 RTC_VDD，INT 输出 RTC_INT，OSCI/OSCO 连接 Y1 32.768K。

- 参数与网络：`reference=U4`；`part_number=BM8563`；`power=RTC_VDD`；`interrupt=RTC_INT`；`crystal=Y1 32.768K`
- 证据：图 bf4d2d939b03 / 第 1 页 / C1 RTC 区 U4 BM8563

## 电源

### AXP192 输入与电池

AXP192 ACIN 接 VBUS_VIN、VBUS 接 VBUS_USB、BAT 接 VBAT_Li_Ion、BACKUP 接 VBAT_RTC，并通过 SYS_SDA/SYS_SCL I2C 管理。

- 参数与网络：`reference=U2`；`ac_input=VBUS_VIN`；`usb_input=VBUS_USB`；`battery=VBAT_Li_Ion`；`backup=VBAT_RTC`；`sda=SYS_SDA`；`scl=SYS_SCL`
- 证据：图 bf4d2d939b03 / 第 1 页 / A1-B1 U2 AXP192 左侧输入

### AXP192 电源轨分配

AXP192 DCDC1 经 L2 2.2uH 输出 VESP_3V3；LDO1 输出 RTC_VDD，LDO2 输出 LCD_BL_VCC，LDO3 输出 LCD_LOGIC_VCC，GPIO2 输出 MIC_VCC，IPSOUT 为系统/扩展电源源。

- 参数与网络：`dcdc1=VESP_3V3`；`ldo1=RTC_VDD`；`ldo2=LCD_BL_VCC`；`ldo3=LCD_LOGIC_VCC`；`gpio2_ldo=MIC_VCC`；`system_output=IPSOUT`
- 证据：图 bf4d2d939b03 / 第 1 页 / A1-C1 U2 DCDC/LDO/GPIO 输出

### EXT_VDD 升压

U8 SGM6603-5.0 以 IPSOUT 为输入，经 L4 4.7uH 生成 EXT_VDD，EN 由 EXT_BOOST_EN 控制并以 R18 100K 下拉。

- 参数与网络：`reference=U8`；`input=IPSOUT`；`output=EXT_VDD`；`enable=EXT_BOOST_EN`；`inductor=L4 4.7uH`；`pulldown=R18 100K`
- 证据：图 bf4d2d939b03 / 第 1 页 / C3-D3 5VOUT_BOOST 区

## 接口

### J2 USB Type-C

J2 VCC 接 VBUS_USB，A6/B6 与 A7/B7 分别汇入 USB_DP/USB_DM，CC1/CC2 经 R13/R19 5.1K 接地，数据线由 D3/D4 ESD3.3V 保护。

- 参数与网络：`reference=J2`；`power=VBUS_USB`；`dp=A6/B6 USB_DP`；`dm=A7/B7 USB_DM`；`cc=R13/R19 5.1K to GND`；`protection=D3/D4 ESD/3.3V`
- 证据：图 bf4d2d939b03 / 第 1 页 / D1-D2 USB TYPE-C 区

### J1 Grove

J1 Grove 的 1 脚 GND、2 脚 EXT_VDD、3 脚 GPIO32、4 脚 GPIO33；GPIO32/33 各有 ESD3.3V 保护与 C37 10uF 电源去耦。

- 参数与网络：`reference=J1`；`pin_1=GND`；`pin_2=EXT_VDD`；`pin_3=GPIO32`；`pin_4=GPIO33`；`signal_level=VESP_3V3`；`power=EXT_VDD`
- 证据：图 bf4d2d939b03 / 第 1 页 / D3 GROVE 区

### HAT/测试焊盘

底部焊盘引出 VESP_3V3、GPIO2、GPIO38、GPIO25、GPIO26、GPIO36、GPIO0、GND、VIN/VBUS_VIN 与 5VOUT/EXT_VDD。

- 参数与网络：`pads=PAD1 3V3; PAD2 GPIO2; PAD3 GPIO38; PAD4 GPIO36; PAD5 GPIO0; PAD6 VIN; PAD7 5VOUT; PAD8 GND; PAD9 GPIO26; PAD10 GPIO25`；`power=VESP_3V3; VBUS_VIN; EXT_VDD`
- 证据：图 bf4d2d939b03 / 第 1 页 / C1-D1 HAT/PAD 区

## 总线

### 内部 I2C 总线

ESP32 GPIO21/GPIO22 分别连接 SYS_SDA/SYS_SCL；R4/R3 各 2.2K 上拉至 VESP_3V3，总线连接 AXP192、BM8563 与 MPU6886。

- 参数与网络：`controller=ESP32-PICO-D4`；`sda=GPIO21 / SYS_SDA`；`scl=GPIO22 / SYS_SCL`；`pullups=R4/R3 2.2K`；`devices=U2 AXP192; U4 BM8563; U7 MPU6886`；`logic_level=VESP_3V3`
- 证据：图 bf4d2d939b03 / 第 1 页 / B1 PMU I2C、B3 ESP GPIO21/22、C1 RTC、A4 IMU

### LCD SPI

LCD U5 的 SCK/MOSI/RS/CS/RESET 分别连接 GPIO13/GPIO15/GPIO23/GPIO5/GPIO18，LEDA 使用 LCD_BL_VCC，VDD 使用 LCD_LOGIC_VCC。

- 参数与网络：`device=U5 LCD`；`sck=GPIO13 / LCD_SCK`；`mosi=GPIO15 / LCD_MOSI`；`dc=GPIO23 / LCD_DC`；`cs=GPIO5 / LCD_CS`；`reset=GPIO18 / LCD_RST`；`backlight=LCD_BL_VCC`；`logic=LCD_LOGIC_VCC`；`miso=null`
- 证据：图 bf4d2d939b03 / 第 1 页 / B2-B3 ESP LCD nets 与 C4-D4 U5 LCD

## 总线地址

### I2C 设备地址

原理图未标注 AXP192、BM8563 或 MPU6886 的数值 I2C 地址。

- 参数与网络：`devices=AXP192; BM8563; MPU6886`；`bus=SYS_SDA/SYS_SCL`；`addresses_visible=false`；`addresses=null`
- 证据：图 bf4d2d939b03 / 第 1 页 / PMU/RTC/IMU 区，未见地址标注

## GPIO 与控制信号

### 电源与用户按键

S1 将 PWR_KEY 拉低；S2 接 GPIO39、S3 接 GPIO37，两路用户按键均有 10K 上拉至 VESP_3V3 与 ESD3.3V 保护。

- 参数与网络：`power=S1 -> PWR_KEY`；`button_b=S2 -> GPIO39`；`button_a=S3 -> GPIO37`；`pullups=10K`；`protection=ESD3.3V`
- 证据：图 bf4d2d939b03 / 第 1 页 / D2-D3 POWER/按键区

### 红色 LED 与红外发射

GPIO9 连接 LED1_IR 支路，GPIO10 连接 LED2_RED 支路，两路均串联至 VESP_3V3 并带 ESD3.3V 保护。

- 参数与网络：`ir=GPIO9 / LED1_IR`；`red_led=GPIO10 / LED2_RED`；`supply=VESP_3V3`；`protection=ESD3.3V`
- 证据：图 bf4d2d939b03 / 第 1 页 / C3-D3 LED/IR 区

## 时钟

### BM8563 RTC 晶振

BM8563 OSCI/OSCO 使用 Y1 32.768K/6pF 晶振，C9/C12 各 6pF 接地。

- 参数与网络：`crystal=Y1`；`frequency=32.768K`；`load_label=6pF`；`capacitors=C9/C12 6pF`
- 证据：图 bf4d2d939b03 / 第 1 页 / C1 RTC 区 Y1/C9/C12

## 保护电路

### USB、按键与扩展口保护

USB DP/DM、GPIO0/25/26/32/33/36、GPIO9/10 与用户按键网络均使用 ESD3.3V 钳位器件，USB CC1/CC2 以 5.1K 下拉。

- 参数与网络：`usb=D3/D4 ESD3.3V`；`external_gpio=D14-D16 and Grove ESD3.3V`；`led_ir=D6/D7 ESD3.3V`；`buttons=D8-D10 ESD3.3V`；`cc=R13/R19 5.1K`
- 证据：图 bf4d2d939b03 / 第 1 页 / D1-D3 USB/GPIO/LED/按键/Grove 保护区

## 关键网络

### RTC 唤醒与电源键

RTC_INT 通过 R401 10K 接到 PWR_KEY，PWR_KEY 同时连接 AXP192 PWRON 与 S1 电源按键。

- 参数与网络：`rtc_interrupt=RTC_INT`；`resistor=R401 10K`；`destination=PWR_KEY`；`pmu_pin=AXP192 PWRON`；`switch=S1`
- 证据：图 bf4d2d939b03 / 第 1 页 / B1-C1 AXP PWRON/RTC_INT 与 D4 R401/PWR_KEY

## 音频

### U3 SPM1423 麦克风

U3 SPM1423HM4H-B 的 CLK 接 GPIO0，DATA 接 GPIO34，VCC 接 MIC_VCC，SELECT 与 GND 接地。

- 参数与网络：`reference=U3`；`part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`power=MIC_VCC`；`select=GND`
- 证据：图 bf4d2d939b03 / 第 1 页 / D3-D4 I2S_MIC 区

## 传感器

### U7 MPU6886

MPU6886 由 VESP_3V3 供电，SCL/SDA 接 SYS_SCL/SYS_SDA，INT 输出 SYS_INT 并连接 ESP32 GPIO35。

- 参数与网络：`reference=U7`；`part_number=MPU6886`；`power=VESP_3V3`；`scl=SYS_SCL`；`sda=SYS_SDA`；`interrupt=SYS_INT -> GPIO35`
- 证据：图 bf4d2d939b03 / 第 1 页 / A4-B4 IMU 区与 B3 ESP GPIO35

## 射频

### ESP32 天线路径

ESP32 LNA_IN 经 L1 1.8nH/HQ 和 C1/C2 匹配网络连接 E1 ANT。

- 参数与网络：`source=LNA_IN`；`inductor=L1 1.8nH/HQ`；`capacitors=C1/C2`；`antenna=E1 ANT`
- 证据：图 bf4d2d939b03 / 第 1 页 / A3 射频匹配区

## 调试与烧录

### CH552 USB-UART

J2 USB_DP/USB_DM 连接 CH552 U6；CH552_TXD/CH552_RXD 连接 ESP32_U0RXD/ESP32_U0TXD，并通过 MOS 管网络控制 ESP32_EN 与 GPIO0。

- 参数与网络：`bridge=U6 CH552`；`usb=USB_DP/USB_DM`；`tx=CH552_TXD -> ESP32_U0RXD`；`rx=CH552_RXD <- ESP32_U0TXD`；`auto_download=CH552 GPIO0/EN CTRL -> MOS -> GPIO0/ESP32_EN`
- 证据：图 bf4d2d939b03 / 第 1 页 / C2-D2 CH552 与 GPO/EN/UART 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StickC-Plus 系统架构 | `mcu=U1 ESP32-PICO-D4`；`pmu=U2 AXP192`；`rtc=U4 BM8563`；`imu=U7 MPU6886`；`usb_bridge=U6 CH552`；`mic=U3 SPM1423HM4H-B` |
| 核心器件 | ESP32-PICO-D4 | `part_number=ESP32-PICO-D4`；`reset=ESP32_EN`；`power=VESP_3V3`；`uart=ESP32_U0TXD/ESP32_U0RXD` |
| 内存与 Flash | ESP32-PICO-D4 Flash | `module=ESP32-PICO-D4`；`documented_capacity=4MB`；`schematic_capacity_label=null` |
| 电源 | AXP192 输入与电池 | `reference=U2`；`ac_input=VBUS_VIN`；`usb_input=VBUS_USB`；`battery=VBAT_Li_Ion`；`backup=VBAT_RTC`；`sda=SYS_SDA`；`scl=SYS_SCL` |
| 电源 | AXP192 电源轨分配 | `dcdc1=VESP_3V3`；`ldo1=RTC_VDD`；`ldo2=LCD_BL_VCC`；`ldo3=LCD_LOGIC_VCC`；`gpio2_ldo=MIC_VCC`；`system_output=IPSOUT` |
| 总线 | 内部 I2C 总线 | `controller=ESP32-PICO-D4`；`sda=GPIO21 / SYS_SDA`；`scl=GPIO22 / SYS_SCL`；`pullups=R4/R3 2.2K`；`devices=U2 AXP192; U4 BM8563; U7 MPU6886`；`logic_level=VESP_3V3` |
| 总线地址 | I2C 设备地址 | `devices=AXP192; BM8563; MPU6886`；`bus=SYS_SDA/SYS_SCL`；`addresses_visible=false`；`addresses=null` |
| 核心器件 | U4 BM8563 | `reference=U4`；`part_number=BM8563`；`power=RTC_VDD`；`interrupt=RTC_INT`；`crystal=Y1 32.768K` |
| 时钟 | BM8563 RTC 晶振 | `crystal=Y1`；`frequency=32.768K`；`load_label=6pF`；`capacitors=C9/C12 6pF` |
| 关键网络 | RTC 唤醒与电源键 | `rtc_interrupt=RTC_INT`；`resistor=R401 10K`；`destination=PWR_KEY`；`pmu_pin=AXP192 PWRON`；`switch=S1` |
| 传感器 | U7 MPU6886 | `reference=U7`；`part_number=MPU6886`；`power=VESP_3V3`；`scl=SYS_SCL`；`sda=SYS_SDA`；`interrupt=SYS_INT -> GPIO35` |
| 总线 | LCD SPI | `device=U5 LCD`；`sck=GPIO13 / LCD_SCK`；`mosi=GPIO15 / LCD_MOSI`；`dc=GPIO23 / LCD_DC`；`cs=GPIO5 / LCD_CS`；`reset=GPIO18 / LCD_RST`；`backlight=LCD_BL_VCC`；`logic=LCD_LOGIC_VCC`；`miso=null` |
| 核心器件 | LCD 型号与规格 | `schematic_label=U5 LCD`；`documented_driver=ST7789v2`；`documented_size=1.14 inch`；`documented_resolution=135x240` |
| 音频 | U3 SPM1423 麦克风 | `reference=U3`；`part_number=SPM1423HM4H-B`；`clock=GPIO0`；`data=GPIO34`；`power=MIC_VCC`；`select=GND` |
| 调试与烧录 | CH552 USB-UART | `bridge=U6 CH552`；`usb=USB_DP/USB_DM`；`tx=CH552_TXD -> ESP32_U0RXD`；`rx=CH552_RXD <- ESP32_U0TXD`；`auto_download=CH552 GPIO0/EN CTRL -> MOS -> GPIO0/ESP32_EN` |
| 接口 | J2 USB Type-C | `reference=J2`；`power=VBUS_USB`；`dp=A6/B6 USB_DP`；`dm=A7/B7 USB_DM`；`cc=R13/R19 5.1K to GND`；`protection=D3/D4 ESD/3.3V` |
| 电源 | EXT_VDD 升压 | `reference=U8`；`input=IPSOUT`；`output=EXT_VDD`；`enable=EXT_BOOST_EN`；`inductor=L4 4.7uH`；`pulldown=R18 100K` |
| 接口 | J1 Grove | `reference=J1`；`pin_1=GND`；`pin_2=EXT_VDD`；`pin_3=GPIO32`；`pin_4=GPIO33`；`signal_level=VESP_3V3`；`power=EXT_VDD` |
| 接口 | HAT/测试焊盘 | `pads=PAD1 3V3; PAD2 GPIO2; PAD3 GPIO38; PAD4 GPIO36; PAD5 GPIO0; PAD6 VIN; PAD7 5VOUT; PAD8 GND; PAD9 GPIO26; PAD10 GPIO25`；`power=VESP_3V3; VBUS_VIN; EXT_VDD` |
| GPIO 与控制信号 | 电源与用户按键 | `power=S1 -> PWR_KEY`；`button_b=S2 -> GPIO39`；`button_a=S3 -> GPIO37`；`pullups=10K`；`protection=ESD3.3V` |
| GPIO 与控制信号 | 红色 LED 与红外发射 | `ir=GPIO9 / LED1_IR`；`red_led=GPIO10 / LED2_RED`；`supply=VESP_3V3`；`protection=ESD3.3V` |
| 音频 | 无源蜂鸣器 | `documented_gpio=GPIO2`；`buzzer_reference=null`；`driver_visible=false`；`pad=PAD2 GPIO2` |
| 电源 | 内置电池容量 | `documented_capacity=120mAh`；`documented_voltage=3.7V`；`battery_net=VBAT_Li_Ion`；`capacity_visible=false` |
| 射频 | ESP32 天线路径 | `source=LNA_IN`；`inductor=L1 1.8nH/HQ`；`capacitors=C1/C2`；`antenna=E1 ANT` |
| 保护电路 | USB、按键与扩展口保护 | `usb=D3/D4 ESD3.3V`；`external_gpio=D14-D16 and Grove ESD3.3V`；`led_ir=D6/D7 ESD3.3V`；`buttons=D8-D10 ESD3.3V`；`cc=R13/R19 5.1K` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash，原理图未放置独立 Flash 或标注 SiP 内部容量。（证据：图 bf4d2d939b03 / 第 1 页 / ESP32-PICO 区与完整页，无 Flash 容量）
- `component.lcd-spec`：产品正文称 LCD 为 ST7789v2、1.14 英寸、135x240；原理图 U5 仅标 LCD 与信号脚，未标驱动器或分辨率。（证据：图 bf4d2d939b03 / 第 1 页 / C4-D4 U5 LCD，未标型号/规格）
- `audio.buzzer-not-visible`：产品正文称 GPIO2 连接板载无源蜂鸣器，但当前完整原理图只在焊盘区引出 GPIO2，未见 BZ/BUZZER 位号或驱动电路。（证据：图 bf4d2d939b03 / 第 1 页 / 完整页与 PAD2 GPIO2，未见蜂鸣器位号）
- `power.battery-capacity`：产品正文称内置 120mAh@3.7V 电池；原理图仅显示 Li_Ion/BAT1 接口与 VBAT_Li_Ion，未标容量。（证据：图 bf4d2d939b03 / 第 1 页 / C1 电池接口与 A1 PMU BAT，未标容量）
- `review.flash-capacity`：ESP32-PICO-D4 内部 Flash 是否固定为 4MB？；原因：容量来自产品正文，原理图未标。
- `review.lcd-spec`：U5 LCD 是否固定采用 ST7789v2、1.14 英寸、135x240 面板？；原因：这些参数来自正文，原理图只标 LCD。
- `review.buzzer`：板载无源蜂鸣器的位号、驱动器和 GPIO2 连接位于哪一版原理图？；原因：正文称有蜂鸣器，当前图只引出 GPIO2。
- `review.battery-capacity`：内置电池是否为 120mAh@3.7V？；原因：容量来自正文，原理图未标。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `bf4d2d939b030d91d2bd5394f76e44c48b14b036eab8da3f2c6dcdbffcdff682` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/SCH_StickC_Plus_page_01.png` |

---

源文档：`zh_CN/core/m5stickc_plus.md`

源文档 SHA-256：`38b8d04e06ad929fbff8911bada63f5c1445295119db08a4ca29f64e67814a14`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
