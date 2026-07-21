# PaperS3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PaperS3 |
| SKU | C139 |
| 产品 ID | `papers3-d121b5ce3fad` |
| 源文档 | `zh_CN/core/PaperS3.md` |

## 概述

PaperS3 以 U2 ESP32_S3R8 为主控，直接驱动 8位电子纸数据/时序接口，并连接外部 XM25QH128 系列 NOR Flash、BMI270、BM8563、microSD、GT911 触摸接口、蜂鸣器和 HC1.25-4P。USB-C 输入配合 LGS4056H 充电、MT9700 电源路径、SY8089 主 3.3V、ME6203A33 IMU LDO 与 MT3608/二极管 EPD 高压网络。PMS150G-U6 处理按键、下载状态和电源保持，ESP32 通过原生 USB D+/D- 下载。

## 检索关键词

`PaperS3`、`C139`、`ESP32_S3R8`、`XM25QH128`、`PMS150G-U6`、`LGS4056H`、`MT9700`、`SY8089`、`ME6203A33`、`MT3608`、`BMI270`、`BM8563`、`GT911`、`EPD_ED047TC1`、`microSD`、`USB Type-C`、`USB_DP`、`USB_DM`、`SOC_VDD`、`SYS_BAT`、`SYS_MAIN`、`EPD_VPOS`、`EPD_VNEG`、`EPD_VGH`、`EPD_VGL`、`VCOM`、`GPIO41 SDA`、`GPIO42 SCL`、`GPIO48 TP_INT`、`GPIO47 SD_CS`、`GPIO39 SD_SCK`、`GPIO38 SD_MOSI`、`GPIO40 SD_MISO`、`GPIO21 BUZ_PWM`、`GPIO3 ADC_VBAT`、`HC1.25-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ESP32_S3R8 | 主控 SoC，直接驱动 EPD 并连接存储、触摸、RTC、IMU、TF、蜂鸣器和扩展接口 | 图 eb876cb53109 / 第 1 页 / 单页网格 C1-D4：U2 ESP32_S3R8 |
| U6 | XM25QH128CH | ESP32 外部 QSPI NOR Flash | 图 eb876cb53109 / 第 1 页 / 单页网格 D3-D4：U6 XM25QH128CH、NOR_* |
| U1 | PMS150G-U6 | 开关机、按键、下载状态与电源保持控制器 | 图 eb876cb53109 / 第 1 页 / 单页网格 B1-B3：U1 PMS150G-U6 |
| U3 | SY8089 | SYS_MAIN 到 SOC_VDD 的主 3.3V 降压转换器 | 图 eb876cb53109 / 第 1 页 / 单页网格 B3-B4：U3 SY8089/L3 |
| U10 | ME6203A33M3G | VBUS_PRE 到 IMU_VDD 的 3.3V LDO | 图 eb876cb53109 / 第 1 页 / 单页网格 C5：U10 ME6203A33M3G |
| U11 | BMI270 | SYS_SDA/SYS_SCL I2C 六轴 IMU | 图 eb876cb53109 / 第 1 页 / 单页网格 C5-D6：U11 BMI270 |
| U5 | BM8563 | SYS_SDA/SYS_SCL RTC 与 INT 唤醒源 | 图 eb876cb53109 / 第 1 页 / 单页网格 B3：U5 BM8563/Y1 |
| USB_C | USB Type-C Horizontal | USB 5V 与 ESP32 原生 USB 数据输入 | 图 eb876cb53109 / 第 1 页 / 单页网格 A1-A2：USB_C/D14/R6/R7 |
| U4 | LGS4056H | USB_5V 到 SYS_BAT 的锂电池充电器 | 图 eb876cb53109 / 第 1 页 / 单页网格 A2-A3：U4 LGS4056H |
| U7,U8 | MT9700 | USB/SYS_BAT 到 SYS_MAIN 与 EPD 前级的受控电源路径开关 | 图 eb876cb53109 / 第 1 页 / 单页网格 A4-A6：U7/U8 MT9700 |
| U9 | MT3608 | EPD_VPOS 高压升压转换器 | 图 eb876cb53109 / 第 1 页 / 单页网格 A6：U9 MT3608/L4 |
| EPD1 | AYE544127 | 电子纸 44针数据、时序与高压接口 | 图 eb876cb53109 / 第 1 页 / 单页网格 A8-C8：EPD1 AYE544127 |
| J4 | FPC_8P | GT911 触摸 I2C/INT/RESET 接口 | 图 eb876cb53109 / 第 1 页 / 单页网格 C8：J4 FPC_8P SYS_SDA/SCL/TP_INT/TP_RST |
| J3 | TF | GPIO47/39/38/40 SPI microSD 卡座 | 图 eb876cb53109 / 第 1 页 / 单页网格 D8：J3 TF |
| BZ1 | BUZZER | GPIO21/BUZ_PWM 驱动的无源蜂鸣器 | 图 eb876cb53109 / 第 1 页 / 单页网格 C6-D6：BZ1 BUZZER 与驱动管 |
| J5 | CON4_SMD | SOC_VDD、GND、GPIO1、GPIO2 四针扩展接口 | 图 eb876cb53109 / 第 1 页 / 单页网格 D8：J5 CON4_SMD |
| S1 | TS_015 | PWRON_PULSE 物理电源/控制按键 | 图 eb876cb53109 / 第 1 页 / 单页网格 B1-B2：S1 TS_015 |

## 系统结构

### PaperS3 系统架构

U2 ESP32_S3R8 直接驱动 EPD1，连接外部 NOR Flash、BMI270、BM8563、GT911 接口、microSD、蜂鸣器和扩展口；U1 PMS150G-U6 处理电源/下载控制。

- 参数与网络：`soc=ESP32_S3R8`；`flash=U6 XM25QH128CH`；`imu=BMI270`；`rtc=BM8563`；`epd=EPD1 AYE544127`；`power_control=PMS150G-U6`
- 证据：图 eb876cb53109 / 第 1 页 / 完整单页全部功能分区

## 电源

### USB 与电池充电

USB-C VBUS 形成 USB_5V 并由 D14 SRV05-4 保护；U4 LGS4056H 从 USB_5V 给 SYS_BAT 充电，J1 为 SYS_BAT 电池接口。

- 参数与网络：`usb=USB_C -> USB_5V`；`esd=D14 SRV05-4`；`charger=U4 LGS4056H`；`battery=SYS_BAT / J1`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A1-A3 USB_C/U4/J1

### SYS_MAIN 与 SOC_VDD

Q3 与 D4 汇合 USB_5V/SYS_BAT 到 VBUS_PRE，U7 MT9700 输出 SYS_MAIN；U3 SY8089 经 L3 生成 SOC_VDD。

- 参数与网络：`input_mux=Q3/D4 -> VBUS_PRE`；`switch=U7 MT9700 -> SYS_MAIN`；`buck=U3 SY8089 -> SOC_VDD`；`inductor=L3 WPN3012H2R2MT`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A4-B4 Q3/D4/U7/U3

### EPD 高压电源

U8 MT9700 控制 EPD 前级，U9 MT3608/L4 生成 EPD_VPOS，D9/L5 生成 EPD_VNEG，D6-D13 网络派生 EPD_VGH/EPD_VGL，VCOM 由分压滤波生成。

- 参数与网络：`switch=U8 MT9700`；`boost=U9 MT3608 -> EPD_VPOS`；`negative=D9/L5 -> EPD_VNEG`；`high=D6-D8 -> EPD_VGH`；`low=D11-D13 -> EPD_VGL`；`vcom=R37/R38/C42`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A5-B8 EPD power networks

## 接口

### ESP32 直驱 EPD

EPD DB0-DB7 分别接 GPIO6/14/7/12/9/11/8/10，XSTL=GPIO13、XLE=GPIO15、SPV=GPIO17、CKV=GPIO18，EPD_PWR=GPIO45。

- 参数与网络：`db0=GPIO6`；`db1=GPIO14`；`db2=GPIO7`；`db3=GPIO12`；`db4=GPIO9`；`db5=GPIO11`；`db6=GPIO8`；`db7=GPIO10`；`xstl=GPIO13`；`xle=GPIO15`；`spv=GPIO17`；`ckv=GPIO18`；`power=GPIO45`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 U2 EPD_D0-D7/EPD_XST/EPD_XLE/EPD_SPV/EPD_CKV 与 EPD1

### HC1.25-4P 外设接口

J5 四针接口引出 GND、SOC_VDD、EXT_GPIO1/GPIO1 与 EXT_GPIO2/GPIO2。

- 参数与网络：`pin1=GND`；`pin2=SOC_VDD 3.3V`；`pin3=GPIO1`；`pin4=GPIO2`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 D8 J5 CON4_SMD

## 总线

### 触摸、RTC 与 IMU I2C

ESP32 GPIO41=SYS_SDA、GPIO42=SYS_SCL；J4 触摸与 U5 BM8563 连接该总线，BMI270 使用同名 SYS_SDA/SYS_SCL。

- 参数与网络：`sda=GPIO41 / SYS_SDA`；`scl=GPIO42 / SYS_SCL`；`devices=GT911 interface, BM8563, BMI270`；`touch_interrupt=GPIO48 / TP_INT`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 U2/U5/U11/J4 SYS_SDA/SYS_SCL

### ESP32-S3 原生 USB

USB_C DP/DM 直接形成 USB_DP/USB_DM 并连接 ESP32 GPIO20/GPIO19，页面未画 USB-UART 桥。

- 参数与网络：`dp=USB_C -> USB_DP -> GPIO20`；`dm=USB_C -> USB_DM -> GPIO19`；`bridge_shown=false`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A1 USB_C 与 U2 GPIO19/20

## GPIO 与控制信号

### 蜂鸣器输出

GPIO21 形成 BUZ_PWM，经 C50 与晶体管/二极管网络驱动 BZ1 BUZZER。

- 参数与网络：`gpio=GPIO21`；`net=BUZ_PWM`；`load=BZ1 BUZZER`；`driver=Q10/Q11 + D18/D19`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 C6-D6 BZ1/BUZ_PWM

## 时钟

### BM8563 RTC

U5 BM8563 SDA/SCL 接内部 I2C，INT 输出 INT_STA_RTC 到 PMS150G-U6，OSCI/OSCO 连接 32.768kHz 晶体与 12pF 电容。

- 参数与网络：`rtc=U5 BM8563`；`sda=GPIO41`；`scl=GPIO42`；`interrupt=INT_STA_RTC -> U1`；`crystal=32.768kHz / C15/C16 12pF`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 B3 U5 BM8563

## 保护电路

### USB 与电源路径保护

D14 SRV05-4 保护 USB 数据/电源；D4 B5819W 与 Q3 负责 USB/SYS_BAT 汇合，EPD 高压使用 D6-D13 二极管网络。

- 参数与网络：`usb=D14 SRV05-4`；`power_or=D4 B5819W + Q3`；`epd=D6-D13`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A1-A5 USB/power 与 A6-B8 EPD power

## 存储

### microSD SPI

J3 TF 卡座 CARD_CS=GPIO47、CARD_SCK=GPIO39、CARD_MOSI=GPIO38、CARD_MISO=GPIO40，由 SOC_VDD 供电。

- 参数与网络：`cs=GPIO47`；`sck=GPIO39`；`mosi=GPIO38`；`miso=GPIO40`；`supply=SOC_VDD`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 D8 J3 TF

## 内存与 Flash

### 外部 QSPI NOR Flash

U6 XM25QH128CH 由 VDD_NOR 供电，NOR_CS/CLK/D0/D1/D2/D3 连接 ESP32 SPIIO4-SPIIO7、SPICLK_N/P 与 SPICS0。

- 参数与网络：`device=U6 XM25QH128CH`；`supply=VDD_NOR`；`signals=NOR_CS,NOR_CLK,NOR_D0-D3`；`series=R32-R36 16R/NC options`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 D3-D4 U2/U6 NOR networks

## 传感器

### BMI270 连接

U11 BMI270 SCK pin13 接 SYS_SCL、SDA pin14 接 SYS_SDA，VDD/VDDIO 接 IMU_VDD，SDO pin10 接 GND，INT1/INT2 未连接。

- 参数与网络：`scl=GPIO42`；`sda=GPIO41`；`supply=IMU_VDD`；`sdo=GND`；`interrupts=INT1/INT2 NC`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 C5-D6 U11 BMI270

## 模拟电路

### 电池电压检测

SYS_BAT 经 R20/R22 分压和 C21 滤波形成 ADC_VBAT，并接 ESP32 GPIO3。

- 参数与网络：`source=SYS_BAT`；`divider=R20/R22`；`filter=C21`；`adc=GPIO3 / ADC_VBAT`
- 证据：图 eb876cb53109 / 第 1 页 / 单页 A4-B5 ADC_VBAT 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | PaperS3 系统架构 | `soc=ESP32_S3R8`；`flash=U6 XM25QH128CH`；`imu=BMI270`；`rtc=BM8563`；`epd=EPD1 AYE544127`；`power_control=PMS150G-U6` |
| 内存与 Flash | 外部 QSPI NOR Flash | `device=U6 XM25QH128CH`；`supply=VDD_NOR`；`signals=NOR_CS,NOR_CLK,NOR_D0-D3`；`series=R32-R36 16R/NC options` |
| 内存与 Flash | ESP32-S3R8 PSRAM 可见性 | `soc=ESP32_S3R8`；`external_psram_shown=false`；`documented_psram=8MB`；`capacity_text_shown=false` |
| 电源 | USB 与电池充电 | `usb=USB_C -> USB_5V`；`esd=D14 SRV05-4`；`charger=U4 LGS4056H`；`battery=SYS_BAT / J1` |
| 电源 | SYS_MAIN 与 SOC_VDD | `input_mux=Q3/D4 -> VBUS_PRE`；`switch=U7 MT9700 -> SYS_MAIN`；`buck=U3 SY8089 -> SOC_VDD`；`inductor=L3 WPN3012H2R2MT` |
| 电源 | EPD 高压电源 | `switch=U8 MT9700`；`boost=U9 MT3608 -> EPD_VPOS`；`negative=D9/L5 -> EPD_VNEG`；`high=D6-D8 -> EPD_VGH`；`low=D11-D13 -> EPD_VGL`；`vcom=R37/R38/C42` |
| 接口 | ESP32 直驱 EPD | `db0=GPIO6`；`db1=GPIO14`；`db2=GPIO7`；`db3=GPIO12`；`db4=GPIO9`；`db5=GPIO11`；`db6=GPIO8`；`db7=GPIO10`；`xstl=GPIO13`；`xle=GPIO15`；`spv=GPIO17`；`ckv=GPIO18`；`power=GPIO45` |
| 总线 | 触摸、RTC 与 IMU I2C | `sda=GPIO41 / SYS_SDA`；`scl=GPIO42 / SYS_SCL`；`devices=GT911 interface, BM8563, BMI270`；`touch_interrupt=GPIO48 / TP_INT` |
| 传感器 | BMI270 连接 | `scl=GPIO42`；`sda=GPIO41`；`supply=IMU_VDD`；`sdo=GND`；`interrupts=INT1/INT2 NC` |
| 时钟 | BM8563 RTC | `rtc=U5 BM8563`；`sda=GPIO41`；`scl=GPIO42`；`interrupt=INT_STA_RTC -> U1`；`crystal=32.768kHz / C15/C16 12pF` |
| 存储 | microSD SPI | `cs=GPIO47`；`sck=GPIO39`；`mosi=GPIO38`；`miso=GPIO40`；`supply=SOC_VDD` |
| 模拟电路 | 电池电压检测 | `source=SYS_BAT`；`divider=R20/R22`；`filter=C21`；`adc=GPIO3 / ADC_VBAT` |
| GPIO 与控制信号 | 蜂鸣器输出 | `gpio=GPIO21`；`net=BUZ_PWM`；`load=BZ1 BUZZER`；`driver=Q10/Q11 + D18/D19` |
| 接口 | HC1.25-4P 外设接口 | `pin1=GND`；`pin2=SOC_VDD 3.3V`；`pin3=GPIO1`；`pin4=GPIO2` |
| 总线 | ESP32-S3 原生 USB | `dp=USB_C -> USB_DP -> GPIO20`；`dm=USB_C -> USB_DM -> GPIO19`；`bridge_shown=false` |
| 总线地址 | BMI270 与 BM8563 地址 | `BMI270=0x68 documented`；`BM8563=0x51 documented`；`numeric_text_shown=false` |
| 核心器件 | EPD 与触摸规格 | `documented_panel=EPD_ED047TC1`；`documented_resolution=960x540`；`documented_size=4.7 inch`；`documented_grayscale=16`；`documented_touch=GT911`；`schematic_epd=AYE544127` |
| 电源 | 1800mAh 电池容量 | `documented_voltage=3.7V`；`documented_capacity=1800mAh`；`schematic_capacity_text=false` |
| 保护电路 | USB 与电源路径保护 | `usb=D14 SRV05-4`；`power_or=D4 B5819W + Q3`；`epd=D6-D13` |

## 待确认事项

- `memory.psram-visibility`：原理图主控料号为 ESP32_S3R8，未画独立 PSRAM 器件；页面未单独打印 PSRAM 容量字段。（证据：图 eb876cb53109 / 第 1 页 / 单页 U2 与完整存储器范围）
- `address.documented-i2c`：正文写 BMI270=0x68、BM8563=0x51，原理图显示 BMI270 SDO 接地和 I2C 连接，但未直接打印数值地址。（证据：图 eb876cb53109 / 第 1 页 / 单页 U5/U11，无数值地址文字）
- `component.documented-epd-touch`：正文写 EPD_ED047TC1、960x540、4.7 inch、16灰阶和 GT911；原理图只显示 EPD1 AYE544127 接口和 J4 触摸 FPC，未打印这些完整规格。（证据：图 eb876cb53109 / 第 1 页 / 单页 EPD1/J4）
- `power.documented-battery`：正文写 3.7V 1800mAh，原理图只显示 J1 SYS_BAT 接口和 LGS4056H 充电路径，没有容量字段。（证据：图 eb876cb53109 / 第 1 页 / 单页 J1/U4 SYS_BAT）
- `review.psram-capacity`：C139 当前 ESP32-S3R8 集成 PSRAM 容量是否固定为 8MB？；原因：原理图未单独打印容量字段。
- `review.i2c-addresses`：C139 当前 BMI270 与 BM8563 的正式 7-bit 地址是否为 0x68 和 0x51？；原因：地址来自正文，原理图未直接打印数值。
- `review.epd-touch-spec`：C139 当前面板是否固定为 EPD_ED047TC1 960x540/4.7 inch/16灰阶且触摸 IC 为 GT911？；原因：原理图只显示接口料号与网络。
- `review.battery-capacity`：C139 当前内置电池容量是否固定为 1800mAh@3.7V？；原因：容量只出现在正文。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `eb876cb53109d478422d72f1d4f7d4062167c4712a6679096f9910b21c6fd3c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/sch_papers3_V1.0_page_01.png` |

---

源文档：`zh_CN/core/PaperS3.md`

源文档 SHA-256：`19f15a73cd300c62e8231e7d0102afb6a85ec9d5f70feb58081d3faa99768e74`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
