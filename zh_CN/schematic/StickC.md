# StickC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StickC |
| SKU | K016-C |
| 产品 ID | `stickc-03f0da06c74a` |
| 源文档 | `zh_CN/core/m5stickc.md` |

## 概述

StickC 系统图以 ESP32-PICO(4M) 为主控，连接 AXP192 PMU、MPU6886、BM8563、SPM1423、ST7735S LCD、红外、红色 LED、两枚按键、USB-UART 和 Grove。AXP192 从 USB-C/外部 5V 与电池路径供电，通过 DCDC1、LDO0/LDO1/LDO2/LDO3 和 IPSOUT 分别为主控/IMU、麦克风、RTC、LCD 背光/逻辑与 Grove 供电。内部 I2C 使用 GPIO21/GPIO22，LCD 使用 GPIO15/13/23/18/5，麦克风使用 GPIO0/GPIO34。

## 检索关键词

`StickC`、`K016-C`、`ESP32-PICO-D4`、`ESP32 PICO(4M)`、`AXP192`、`MPU6886`、`BM8563`、`SPM1423`、`ST7735S`、`USB Type-C`、`USB-UART`、`GPIO21 SDA`、`GPIO22 SCL`、`GPIO35 IRQ`、`GPIO0 MIC_CLK`、`GPIO34 MIC_DATA`、`GPIO15 LCD_MOSI`、`GPIO13 LCD_CLK`、`GPIO23 LCD_DC`、`GPIO18 LCD_RST`、`GPIO5 LCD_CS`、`GPIO9 IR`、`GPIO10 Red LED`、`GPIO37 BUTTONA`、`GPIO39 BUTTONB`、`GPIO32`、`GPIO33`、`Grove`、`DCDC1`、`LDO0`、`LDO1`、`LDO2`、`LDO3`、`IPSOUT`、`VBUS_USB`、`VBUS_VIN`、`VBAT_Li_Ion`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ESP32 | ESP32-PICO-D4 / PICO(4M) | StickC 主控，连接 LCD、I2C、麦克风、IR、LED、按键和扩展 GPIO | 图 89392b541840 / 第 1 页 / 系统图中央 ESP32 方框; 图 6b63be17565b / 第 1 页 / 丝印图 ESP32 PICO(4M) |
| PMU | AXP192 | 系统电源管理、充电与多路电源轨控制 | 图 89392b541840 / 第 1 页 / 系统图左侧 PMU AXP192; 图 082caba5b06c / 第 1 页 / 电源图中央 AXP192 |
| IMU | MPU6886 | GPIO21/GPIO22 I2C 六轴 IMU，IRQ 接 GPIO35 | 图 89392b541840 / 第 1 页 / 系统图右下 MPU6886; 图 6b63be17565b / 第 1 页 / 丝印图 6-Axis IMU MPU6886 |
| RTC | BM8563 | GPIO21/GPIO22 I2C 实时时钟，IRQ 接 GPIO35 | 图 89392b541840 / 第 1 页 / 系统图右下 RTC BM8563; 图 082caba5b06c / 第 1 页 / 电源图 RTC 模块 |
| MIC | SPM1423 | GPIO0 时钟、GPIO34 数据的数字麦克风 | 图 89392b541840 / 第 1 页 / 系统图右侧 I2S_MIC; 图 6b63be17565b / 第 1 页 / 丝印图 MIC SPM1423 D:G34/C:G0 |
| LCD | ST7735S | 80x160 0.96 inch SPI TFT LCD | 图 89392b541840 / 第 1 页 / 系统图 LCD 方框; 图 6b63be17565b / 第 1 页 / 丝印图 LCD 80x160@0.96 ST7735S |
| USB-C | USB Type-C | VBUS_USB 与 USB DP/DM 输入接口 | 图 89392b541840 / 第 1 页 / 系统图左侧 USB typeC |
| USB-UART | 未标注 | USB DP/DM 到 UART_TXD/RXD 的下载串口桥 | 图 89392b541840 / 第 1 页 / 系统图 USB to UART 与 UART protection |
| GROVE | HY2.0-4P | GPIO32/GPIO33、EXT_VDD 与 GND 扩展接口 | 图 89392b541840 / 第 1 页 / 系统图右侧 GROVE; 图 6b63be17565b / 第 1 页 / 丝印图 HY2.0-4P G/VOUT/G32/G33 |
| BUTTONA,BUTTONB | SW-PB | GPIO37/GPIO39 低有效用户按键 | 图 89392b541840 / 第 1 页 / 系统图右侧 BUTTONA/B; 图 6b63be17565b / 第 1 页 / 丝印图 BTN G37/G39 |
| IR_LED,RED_LED | IR LED / Red LED | GPIO9 红外与 GPIO10 红色状态 LED | 图 89392b541840 / 第 1 页 / 系统图上方 IR_LED/RED_LED; 图 6b63be17565b / 第 1 页 / 丝印图 IR G9 / LED G10 |

## 系统结构

### StickC 系统架构

ESP32-PICO(4M) 连接 AXP192、MPU6886、BM8563、SPM1423、ST7735S LCD、USB-UART、Grove、IR、LED 和两枚按键。

- 参数与网络：`controller=ESP32-PICO-D4 / PICO(4M)`；`pmu=AXP192`；`imu=MPU6886`；`rtc=BM8563`；`mic=SPM1423`；`display=ST7735S`
- 证据：图 89392b541840 / 第 1 页 / 完整系统连接图; 图 6b63be17565b / 第 1 页 / 完整设备丝印图; 图 082caba5b06c / 第 1 页 / 完整电源结构图

## 核心器件

### LCD 型号与分辨率

本地丝印图直接标注 ST7735S、80x160@0.96 inch。

- 参数与网络：`driver=ST7735S`；`resolution=80x160`；`size=0.96 inch`
- 证据：图 6b63be17565b / 第 1 页 / 丝印图 LCD 80x160@0.96 ST7735S

## 电源

### AXP192 电源轨

AXP192 DCDC1 为 ESP32/MPU6886 提供 VESP_3V3，LDO0 为麦克风供电，LDO1 为 RTC 供电，LDO2 为 LCD LED 背光供电，LDO3 为 LCD 逻辑供电，IPSOUT 为 Grove/外部 5V 路径。

- 参数与网络：`DCDC1=VESP_3V3 ESP32+IMU`；`LDO0=MIC_VCC`；`LDO1=RTC_VDD`；`LDO2=LCD_BL_VCC 2.8V shown`；`LDO3=LCD_LOGIC_VCC 3V shown`；`IPSOUT=external/Grove 5V`
- 证据：图 89392b541840 / 第 1 页 / 系统图 AXP192 output labels; 图 082caba5b06c / 第 1 页 / 电源结构图 AXP192 rails

### USB/外部5V与电池路径

AXP192 ACIN 接 VBUS_VIN，VBUS 接 VBUS_USB，BAT 接 VBAT_Li_Ion；系统图另画 RTC 备份电池 VBAT_RTC。

- 参数与网络：`external_5v=VBUS_VIN -> AXP192 ACIN`；`usb_5v=VBUS_USB -> AXP192 VBUS`；`main_battery=VBAT_Li_Ion -> BAT`；`rtc_battery=VBAT_RTC`
- 证据：图 89392b541840 / 第 1 页 / 系统图 AXP192/USB/Main BAT/RTC BAT; 图 082caba5b06c / 第 1 页 / 电源图 USB-C/DC-DC/BAT paths

## 接口

### ST7735S LCD SPI

LCD MOSI=GPIO15、SCK=GPIO13、D/C=GPIO23、RST=GPIO18、CS=GPIO5；背光与逻辑分别由 AXP192 LDO2/LDO3 供电。

- 参数与网络：`driver=ST7735S`；`mosi=GPIO15`；`sck=GPIO13`；`dc=GPIO23`；`reset=GPIO18`；`cs=GPIO5`；`backlight=AXP192 LDO2`；`logic=AXP192 LDO3`
- 证据：图 89392b541840 / 第 1 页 / 系统图 LCD/ESP32; 图 6b63be17565b / 第 1 页 / 丝印图 LCD ST7735S G15/13/23/18/5

### Grove 扩展口

Grove 引出 GPIO32、GPIO33、EXT_VDD 与 GND；电源结构图显示 EXT_VDD 来自 AXP192 IPSOUT/5V 输出路径。

- 参数与网络：`io1=GPIO32`；`io2=GPIO33`；`vcc=EXT_VDD / VOUT 5V`；`ground=GND`
- 证据：图 89392b541840 / 第 1 页 / 系统图 GROVE GPIO32/GPIO33; 图 082caba5b06c / 第 1 页 / 电源图 Grove G/VOUT/G32/G33

### HAT 扩展接口

HAT 图块引出 GND、EXT_VDD、GPIO26、GPIO36、GPIO0、VBAT_Li_Ion、VESP_3V3 与 VBUS_VIN。

- 参数与网络：`signals=GND,EXT_VDD,GPIO26,GPIO36,GPIO0,VBAT_Li_Ion,VESP_3V3,VBUS_VIN`
- 证据：图 89392b541840 / 第 1 页 / 系统图右侧 HAT block

### USB-UART 下载链路

USB Type-C 的 USB_DP/USB_DM 进入 USB-to-UART，UART_TXD/RXD 经过 UART protection 连接 ESP32 U0RXD/U0TXD，并有 UART_GPIO_CTRL/UART_EN_CTRL 自动控制 GPIO0/ESP32_EN。

- 参数与网络：`usb=USB_DP/USB_DM`；`bridge=USB to UART`；`uart=UART_TXD/RXD -> ESP32 U0RXD/U0TXD`；`auto_boot=GPIO0 and ESP32_EN control`
- 证据：图 89392b541840 / 第 1 页 / 系统图 USB typeC/USB to UART/UART protection

## 总线

### 内部 I2C 总线

ESP32 GPIO21=SYS_SDA、GPIO22=SYS_SCL，连接 AXP192、BM8563 与 MPU6886；三者中断汇入 SYS_INT/GPIO35。

- 参数与网络：`sda=GPIO21 / SYS_SDA`；`scl=GPIO22 / SYS_SCL`；`interrupt=GPIO35 / SYS_INT`；`devices=AXP192,BM8563,MPU6886`
- 证据：图 89392b541840 / 第 1 页 / 系统图 ESP32/AXP192/RTC/MPU6886; 图 6b63be17565b / 第 1 页 / 丝印图 SDA:G21/SCL:G22/INT:G35

## GPIO 与控制信号

### IR、LED 与用户按键

GPIO9 驱动 IR_LED，GPIO10 驱动 RED_LED；BUTTONA 接 GPIO37、BUTTONB 接 GPIO39，按下均接 GND。

- 参数与网络：`ir=GPIO9`；`red_led=GPIO10`；`button_a=GPIO37 low`；`button_b=GPIO39 low`
- 证据：图 89392b541840 / 第 1 页 / 系统图 IR/LED/BUTTONA/B; 图 6b63be17565b / 第 1 页 / 丝印图 IR G9/LED G10/BTN G37/G39

## 关键网络

### 主要电源域

图中可检索电源域包括 VBUS_USB、VBUS_VIN、VBAT_Li_Ion、VBAT_RTC、VESP_3V3、RTC_VDD、MIC_VCC、LCD_BL_VCC、LCD_LOGIC_VCC、IPSOUT 与 EXT_VDD。

- 参数与网络：`inputs=VBUS_USB,VBUS_VIN,VBAT_Li_Ion`；`core=VESP_3V3`；`peripheral=RTC_VDD,MIC_VCC,LCD_BL_VCC,LCD_LOGIC_VCC`；`external=IPSOUT,EXT_VDD`
- 证据：图 89392b541840 / 第 1 页 / 系统图所有红色电源网络; 图 082caba5b06c / 第 1 页 / 电源图全部电源轨

## 内存与 Flash

### ESP32-PICO 存储标识

设备丝印资源直接标注 ESP32 PICO(4M)，但未展示独立 Flash 器件或总线连接。

- 参数与网络：`marking=ESP32 PICO(4M)`；`external_flash_shown=false`
- 证据：图 6b63be17565b / 第 1 页 / 丝印图 ESP32 PICO(4M)

## 音频

### SPM1423 数字麦克风

SPM1423 DATA 接 GPIO34，CLK 接 GPIO0，电源由 AXP192 LDO0/MIC_VCC 提供。

- 参数与网络：`device=SPM1423`；`data=GPIO34`；`clock=GPIO0`；`supply=AXP192 LDO0 / MIC_VCC`；`interface=PDM`
- 证据：图 89392b541840 / 第 1 页 / 系统图 I2S_MIC; 图 6b63be17565b / 第 1 页 / 丝印图 MIC D:G34/C:G0

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StickC 系统架构 | `controller=ESP32-PICO-D4 / PICO(4M)`；`pmu=AXP192`；`imu=MPU6886`；`rtc=BM8563`；`mic=SPM1423`；`display=ST7735S` |
| 电源 | AXP192 电源轨 | `DCDC1=VESP_3V3 ESP32+IMU`；`LDO0=MIC_VCC`；`LDO1=RTC_VDD`；`LDO2=LCD_BL_VCC 2.8V shown`；`LDO3=LCD_LOGIC_VCC 3V shown`；`IPSOUT=external/Grove 5V` |
| 电源 | USB/外部5V与电池路径 | `external_5v=VBUS_VIN -> AXP192 ACIN`；`usb_5v=VBUS_USB -> AXP192 VBUS`；`main_battery=VBAT_Li_Ion -> BAT`；`rtc_battery=VBAT_RTC` |
| 总线 | 内部 I2C 总线 | `sda=GPIO21 / SYS_SDA`；`scl=GPIO22 / SYS_SCL`；`interrupt=GPIO35 / SYS_INT`；`devices=AXP192,BM8563,MPU6886` |
| 音频 | SPM1423 数字麦克风 | `device=SPM1423`；`data=GPIO34`；`clock=GPIO0`；`supply=AXP192 LDO0 / MIC_VCC`；`interface=PDM` |
| 接口 | ST7735S LCD SPI | `driver=ST7735S`；`mosi=GPIO15`；`sck=GPIO13`；`dc=GPIO23`；`reset=GPIO18`；`cs=GPIO5`；`backlight=AXP192 LDO2`；`logic=AXP192 LDO3` |
| 核心器件 | LCD 型号与分辨率 | `driver=ST7735S`；`resolution=80x160`；`size=0.96 inch` |
| GPIO 与控制信号 | IR、LED 与用户按键 | `ir=GPIO9`；`red_led=GPIO10`；`button_a=GPIO37 low`；`button_b=GPIO39 low` |
| 接口 | Grove 扩展口 | `io1=GPIO32`；`io2=GPIO33`；`vcc=EXT_VDD / VOUT 5V`；`ground=GND` |
| 接口 | HAT 扩展接口 | `signals=GND,EXT_VDD,GPIO26,GPIO36,GPIO0,VBAT_Li_Ion,VESP_3V3,VBUS_VIN` |
| 接口 | USB-UART 下载链路 | `usb=USB_DP/USB_DM`；`bridge=USB to UART`；`uart=UART_TXD/RXD -> ESP32 U0RXD/U0TXD`；`auto_boot=GPIO0 and ESP32_EN control` |
| 内存与 Flash | ESP32-PICO 存储标识 | `marking=ESP32 PICO(4M)`；`external_flash_shown=false` |
| 总线地址 | AXP192、MPU6886、BM8563 地址 | `devices=AXP192,MPU6886,BM8563`；`address_text_shown=false` |
| 电源 | 95mAh 电池容量 | `documented_capacity=95mAh`；`documented_voltage=3.7V`；`schematic_capacity_text=false` |
| 关键网络 | 主要电源域 | `inputs=VBUS_USB,VBUS_VIN,VBAT_Li_Ion`；`core=VESP_3V3`；`peripheral=RTC_VDD,MIC_VCC,LCD_BL_VCC,LCD_LOGIC_VCC`；`external=IPSOUT,EXT_VDD` |

## 待确认事项

- `address.documented-i2c`：三张本地资源只显示 I2C 网络和器件型号，未打印 AXP192、MPU6886 或 BM8563 的数值地址。（证据：图 89392b541840 / 第 1 页 / 系统图内部 I2C，无地址文字）
- `power.documented-battery-capacity`：产品正文写 95mAh@3.7V，三张本地资源只标 VBAT_Li_Ion/Main BAT，没有容量字段。（证据：图 89392b541840 / 第 1 页 / 系统图 Main BAT/VBAT_Li_Ion; 图 082caba5b06c / 第 1 页 / 电源图 VBAT/Main BAT）
- `review.i2c-addresses`：K016-C 当前 AXP192、MPU6886 与 BM8563 的正式 7-bit I2C 地址分别是什么？；原因：本地资源未打印数值地址。
- `review.battery-capacity`：K016-C 当前内置电池容量是否固定为 95mAh@3.7V？；原因：容量来自正文，本地资源只显示电池网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `89392b541840bff0c61fba5bebfdea73d840db1781bb1531aa8dcadae5e31e71` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/670/SCHE_StickC_page_01.png` |
| 2 | 1 | `6b63be17565bb9bb9fe937fd29a98dfa496ea834a9beb3334b0322aa1aa3a2b4` | `https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_04.webp` |
| 3 | 1 | `082caba5b06cdb32bfeaacf1a82b53ddd74b42656d5bea874d376e3728fea5d1` | `https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_05.webp` |

---

源文档：`zh_CN/core/m5stickc.md`

源文档 SHA-256：`b471d573081eaa0d029f215ce4cced31a56c8c4fdf1cdb33c5fbeb804b830e93`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
