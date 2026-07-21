# Core2 For AWS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core2 For AWS |
| SKU | K010-AWS |
| 产品 ID | `core2-for-aws-2e685fb3f300` |
| 源文档 | `zh_CN/core/core2_for_aws.md` |

## 概述

Core2 For AWS 以 ESP32-D0WDQ6 为主控，主板集成 AXP192、16MB Flash、8MB PSRAM、CP2104、BM8563、LCD/触摸、TF 卡、NS4168 和 USB Type-C。AWS 底座通过 M5Bus 接入 ATECC608A-TNGTLSU-B、MPU-6886、SPM1423、TP4057 电池充电和 10 颗 SK6812。内部 I2C 使用 GPIO21/GPIO22，外部扩展与电源轨通过 M5 Bus、Port A 和底座插座引出。

## 检索关键词

`Core2 For AWS`、`K010-AWS`、`ESP32-D0WDQ6`、`AXP192`、`ATECC608A-TNGTLSU-B`、`MPU-6886`、`SPM1423HM4H-B`、`TP4057`、`SK6812`、`CP2104`、`BM8563`、`NS4168`、`XM25QH128B`、`ESPPSRAM64H`、`SY7088`、`USB Type-C`、`M5 Bus`、`GPIO21 SDA`、`GPIO22 SCL`、`I2C`、`SPI`、`I2S`、`TF Card`、`LCD`、`CAP1`、`0x35`、`0x68`、`0x51`、`0x34`、`MCU_VDD`、`PERI_VDD`、`RTC_VDD`、`SYS_VBAT`、`BUS_5V`、`GPIO25 RGB`、`GPIO34 DAT`、`GPIO0 CLK`、`GPIO2 SDATA`、`GPIO12 BCLK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 (MCU) | ESP32-D0WDQ6 | 主控 SoC，连接存储、USB-UART、LCD、TF、I2C、音频和扩展总线 | 图 6c305db1571c / 第 1 页 / Core2 页网格 A2-C2：MCU 区 U2 ESP32-D0WDQ6 |
| U4 | AXP192 | 系统 PMU，生成 MCU_VDD、LCD_BL、PERI_VDD、RTC_VDD 和马达/扬声器控制 | 图 6c305db1571c / 第 1 页 / Core2 页网格 A1-B2：PMU 区 U4 AXP192 |
| U1 | XM25QH128B | ESP32 外部 SPI Flash | 图 6c305db1571c / 第 1 页 / Core2 页网格 D1：FLASH 区 U1 XM25QH128B |
| U2 (PSRAM) | ESPPSRAM64H | ESP32 外部 PSRAM | 图 6c305db1571c / 第 1 页 / Core2 页网格 D1：PSRAM 区 U2 ESPPSRAM64H |
| U3 | CP2104-F03-GMR | USB 到 ESP32 UART 下载调试桥 | 图 6c305db1571c / 第 1 页 / Core2 页网格 C1：USB2UART 区 U3 CP2104 |
| U7 | BM8563 | I2C 实时时钟 | 图 6c305db1571c / 第 1 页 / Core2 页网格 D2：RTC 区 U7 BM8563/X1 |
| U6 | NS4168 | I2S 数字功放 | 图 6c305db1571c / 第 1 页 / Core2 页网格 C2：SPEAKER 区 U6 NS4168 |
| LCD1,CTP1 | M5_CORE2_LCD_10P / CTP_2.0Inch | SPI LCD 与 I2C 电容触摸连接器 | 图 6c305db1571c / 第 1 页 / Core2 页网格 C4-D4：LCD 与 C-TP 区 |
| U8 | SY7088 | IPS_BUS 到 BUS_5V 的升压转换器 | 图 6c305db1571c / 第 1 页 / Core2 页网格 C2-C3：5V_BOOST 区 U8 SY7088 |
| U4 (AWS) | ATECC608A-TNGTLSU-B | GPIO21/GPIO22 I2C 硬件安全芯片 | 图 feed9faed66e / 第 1 页 / AWS 底座页右下 U4 ATECC608A-TNGTLSU-B |
| U1 (AWS) | MPU-6886 | GPIO21/GPIO22 I2C 六轴 IMU | 图 feed9faed66e / 第 1 页 / AWS 底座页中央 U1 MPU-6886 |
| U2 (AWS) | SPM1423HM4H-B | GPIO34 数据、GPIO0 时钟的 PDM 麦克风 | 图 feed9faed66e / 第 1 页 / AWS 底座页左中 U2 SPM1423HM4H-B |
| U3 (AWS) | TP4057 | VIN 到 BAT+ 的底座锂电池充电器 | 图 feed9faed66e / 第 1 页 / AWS 底座页左下 Power 区 U3 TP4057 |
| LED1-LED10 | SK6812 | GPIO25/RGB 控制的十颗级联 RGB LED | 图 feed9faed66e / 第 1 页 / AWS 底座页顶部 RGB LED x10 |
| BUS1/J4 | M5_BUS / M5Stack_BUS2 | Core2 与 AWS 底座的 30 针扩展总线 | 图 6c305db1571c / 第 1 页 / Core2 页网格 A3-B3：BUS1 M5_BUS; 图 feed9faed66e / 第 1 页 / AWS 底座页右下 J4 M5Stack_BUS2 |

## 系统结构

### Core2 For AWS 架构

Core2 主板以 ESP32-D0WDQ6、AXP192、外部 Flash/PSRAM、LCD/触摸、RTC、TF、USB-UART 和音频为核心；AWS 底座经 M5Bus 增加 ATECC608A、MPU-6886、PDM 麦克风、TP4057 和 10 颗 SK6812。

- 参数与网络：`mcu=ESP32-D0WDQ6`；`pmu=AXP192`；`security=ATECC608A-TNGTLSU-B`；`imu=MPU-6886`；`bus=M5Bus`
- 证据：图 6c305db1571c / 第 1 页 / Core2 完整单页; 图 feed9faed66e / 第 1 页 / AWS 底座完整单页

## 核心器件

### ATECC608A 安全芯片

AWS U4 ATECC608A-TNGTLSU-B 由 +3.3V 供电，SCL pin6 接 I2C_SCL，SDA pin5 接 I2C_SDA。

- 参数与网络：`device=ATECC608A-TNGTLSU-B`；`scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`supply=+3.3V`
- 证据：图 feed9faed66e / 第 1 页 / AWS 底座右下 U4

## 电源

### AXP192 电源轨

AXP192 DCDC1 经 L3 生成 MCU_VDD，DCDC3 经 L2 生成 LCD_BL，LDO1 输出 RTC_VDD，LDO2 输出 PERI_VDD，LDO3 输出 VIB_MOTOR；IPSOUT 形成 IPS_BUS。

- 参数与网络：`dcdc1=MCU_VDD`；`dcdc3=LCD_BL`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 A1-B2 PMU 区 U4

### BUS_5V 升压

U8 SY7088 由 IPS_BUS 供电，L4 2.2uH 与反馈网络生成 BUS_5V。

- 参数与网络：`converter=U8 SY7088`；`input=IPS_BUS`；`inductor=L4 2.2uH`；`output=BUS_5V`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 C2-C3 5V_BOOST 区

### AWS 底座电池充电

U3 TP4057 VCC 接 VIN，BAT pin3 输出 BAT+，PROG pin6 经 R9 2KΩ 接地，C6/C7 各 10uF；D1 1615RC 显示充电/待机状态。

- 参数与网络：`charger=U3 TP4057`；`input=VIN`；`battery=BAT+`；`program=R9 2KΩ`；`caps=C6/C7 10uF`；`indicator=D1 1615RC`
- 证据：图 feed9faed66e / 第 1 页 / AWS 底座左下 Power 区

## 接口

### USB Type-C 与 CP2104 UART

J3 Type-C 的 USB DP/DM 连接 CP2104 DP/DM；CP2104 TXD 形成 CP_TX 并经 R7 47Ω 接 GPIO3，RXD 形成 CP_RX 并经 R8 47Ω 接 GPIO1。

- 参数与网络：`usb=J3 TYPEC_16P`；`bridge=U3 CP2104-F03-GMR`；`tx=CP_TX -> GPIO3`；`rx=CP_RX -> GPIO1`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 B3-C1 USB/USB2UART 区

### LCD 与电容触摸

LCD1 SPI 使用 GPIO23 MOSI、GPIO38 MISO、GPIO18 SCK、GPIO5 CS、GPIO15 D/C；CTP1 使用 GPIO21 SDA、GPIO22 SCL、GPIO39 INT 和 LCD_RST。

- 参数与网络：`lcd_mosi=GPIO23`；`lcd_miso=GPIO38`；`lcd_sck=GPIO18`；`lcd_cs=GPIO5`；`lcd_dc=GPIO15`；`touch_sda=GPIO21`；`touch_scl=GPIO22`；`touch_int=GPIO39`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 C4-D4 LCD/C-TP 区

### M5 Bus 跨板连接

Core2 BUS1 与 AWS J4 共同引出 GND、GPIO、EN、3.3V、5V、BAT、I2C、UART 和音频网络；AWS J4 GPIO25 对应 RGB，GPIO21/22 对应 I2C。

- 参数与网络：`core=BUS1 M5_BUS`；`base=J4 M5Stack_BUS2`；`i2c=GPIO21 SDA; GPIO22 SCL`；`rgb=GPIO25`；`power=+3.3V,+5V,BAT`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 BUS1; 图 feed9faed66e / 第 1 页 / AWS 底座 J4 M5Stack_BUS2

## 总线

### 内部 I2C 总线

ESP32 GPIO21=SYS_SDA、GPIO22=SYS_SCL；主板连接 AXP192、BM8563 和 CTP1，AWS 底座连接 MPU-6886 与 ATECC608A。

- 参数与网络：`controller=ESP32-D0WDQ6`；`sda=GPIO21`；`scl=GPIO22`；`devices=AXP192, BM8563, CTP1, MPU-6886, ATECC608A`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 MCU/BUS1/INTERNAL I2C PULLUP; 图 feed9faed66e / 第 1 页 / AWS 底座 U1/U4 I2C_SDA/SCL

## GPIO 与控制信号

### AWS 底座 RGB

GPIO25 经 M5Bus RGB 网络和 R8/Q1 驱动 LED1 DIN，LED1-LED10 SK6812 串联，均由 +5V 供电。

- 参数与网络：`gpio=GPIO25`；`driver=R8 1KΩ + Q1 SS8550 Y2`；`leds=LED1-LED10 SK6812`；`supply=+5V`
- 证据：图 feed9faed66e / 第 1 页 / AWS 底座顶部 RGB LED x10 与下部 Q1/R8

## 保护电路

### M5 Bus ESD 保护

D3-D8 SRV05-4 通过 R34-R56 47Ω 保护 M5 Bus 多路 GPIO、USB DP/DM 与 MCU_RST。

- 参数与网络：`arrays=D3-D8 SRV05-4`；`series=R34-R56 47Ω`；`rails=MCU_VDD/GND`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 A4-B4 ESD 区

## 存储

### TF 卡 SPI

TF_CARD_SOCKET 使用 GPIO38 DAT0/MISO、GPIO4 DAT3/CS、GPIO18 CLK/SCK、GPIO23 CMD/MOSI，由 PERI_VDD 供电。

- 参数与网络：`miso=GPIO38`；`cs=GPIO4`；`sck=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 D3 CARD 区

## 内存与 Flash

### Flash 与 PSRAM

U1 XM25QH128B 连接 GPIO11/7/6/8，U2 ESPPSRAM64H 连接 GPIO8/7/10/9/17/16；两颗器件由 MCU_VDD 供电。

- 参数与网络：`flash=XM25QH128B`；`flash_pins=GPIO11 CS#, GPIO7 SO, GPIO6 SCLK, GPIO8 SI`；`psram=ESPPSRAM64H`；`psram_pins=GPIO8 SIO0, GPIO7 SIO1, GPIO10 SIO2, GPIO9 SIO3, GPIO17 SCLK, GPIO16 CS#`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 D1 FLASH/PSRAM 区

## 音频

### 麦克风与扬声器

AWS U2 SPM1423 DAT 接 GPIO34、CLK 接 GPIO0；Core2 U6 NS4168 LRCLK=GPIO0、BCLK=GPIO12、SADATA=GPIO2，SPK_EN 由 AXP192 控制。

- 参数与网络：`mic_data=GPIO34`；`mic_clock=GPIO0`；`speaker_lrclk=GPIO0`；`speaker_bclk=GPIO12`；`speaker_data=GPIO2`；`amplifier=NS4168`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 C2 SPEAKER 区; 图 feed9faed66e / 第 1 页 / AWS 底座 U2 Microphone 区

## 传感器

### MPU-6886 连接

AWS U1 MPU-6886 SCL/SCLK pin23 接 I2C_SCL，SDA/SDI pin24 接 I2C_SDA，AD0/SDO pin9 经 R5 4.7KΩ 接地，VDD/VDDIO 接 +3.3V。

- 参数与网络：`scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`ad0=GND via R5 4.7KΩ`；`supply=+3.3V`；`interrupt=NC`
- 证据：图 feed9faed66e / 第 1 页 / AWS 底座中央 U1 MPU-6886

## 射频

### ESP32 射频路径

ESP32 LNA_IN 经可选匹配网络连接 ANT1 与 ANT2 IPEX。

- 参数与网络：`soc=ESP32-D0WDQ6 LNA_IN`；`onboard=ANT1`；`external=ANT2 IPEX`；`selection=R1/R2 DNP options`
- 证据：图 6c305db1571c / 第 1 页 / Core2 页 A2 ANT 区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Core2 For AWS 架构 | `mcu=ESP32-D0WDQ6`；`pmu=AXP192`；`security=ATECC608A-TNGTLSU-B`；`imu=MPU-6886`；`bus=M5Bus` |
| 内存与 Flash | Flash 与 PSRAM | `flash=XM25QH128B`；`flash_pins=GPIO11 CS#, GPIO7 SO, GPIO6 SCLK, GPIO8 SI`；`psram=ESPPSRAM64H`；`psram_pins=GPIO8 SIO0, GPIO7 SIO1, GPIO10 SIO2, GPIO9 SIO3, GPIO17 SCLK, GPIO16 CS#` |
| 电源 | AXP192 电源轨 | `dcdc1=MCU_VDD`；`dcdc3=LCD_BL`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`；`ipsout=IPS_BUS` |
| 电源 | BUS_5V 升压 | `converter=U8 SY7088`；`input=IPS_BUS`；`inductor=L4 2.2uH`；`output=BUS_5V` |
| 总线 | 内部 I2C 总线 | `controller=ESP32-D0WDQ6`；`sda=GPIO21`；`scl=GPIO22`；`devices=AXP192, BM8563, CTP1, MPU-6886, ATECC608A` |
| 总线地址 | I2C 地址 | `AXP192=0x34`；`ATECC608=0x35`；`FT6336U=0x38`；`BM8563=0x51`；`MPU6886=0x68`；`schematic_address_text=false` |
| 音频 | 麦克风与扬声器 | `mic_data=GPIO34`；`mic_clock=GPIO0`；`speaker_lrclk=GPIO0`；`speaker_bclk=GPIO12`；`speaker_data=GPIO2`；`amplifier=NS4168` |
| 传感器 | MPU-6886 连接 | `scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`ad0=GND via R5 4.7KΩ`；`supply=+3.3V`；`interrupt=NC` |
| 核心器件 | ATECC608A 安全芯片 | `device=ATECC608A-TNGTLSU-B`；`scl=GPIO22/I2C_SCL`；`sda=GPIO21/I2C_SDA`；`supply=+3.3V` |
| GPIO 与控制信号 | AWS 底座 RGB | `gpio=GPIO25`；`driver=R8 1KΩ + Q1 SS8550 Y2`；`leds=LED1-LED10 SK6812`；`supply=+5V` |
| 电源 | AWS 底座电池充电 | `charger=U3 TP4057`；`input=VIN`；`battery=BAT+`；`program=R9 2KΩ`；`caps=C6/C7 10uF`；`indicator=D1 1615RC` |
| 接口 | USB Type-C 与 CP2104 UART | `usb=J3 TYPEC_16P`；`bridge=U3 CP2104-F03-GMR`；`tx=CP_TX -> GPIO3`；`rx=CP_RX -> GPIO1` |
| 接口 | LCD 与电容触摸 | `lcd_mosi=GPIO23`；`lcd_miso=GPIO38`；`lcd_sck=GPIO18`；`lcd_cs=GPIO5`；`lcd_dc=GPIO15`；`touch_sda=GPIO21`；`touch_scl=GPIO22`；`touch_int=GPIO39` |
| 存储 | TF 卡 SPI | `miso=GPIO38`；`cs=GPIO4`；`sck=GPIO18`；`mosi=GPIO23`；`supply=PERI_VDD` |
| 接口 | M5 Bus 跨板连接 | `core=BUS1 M5_BUS`；`base=J4 M5Stack_BUS2`；`i2c=GPIO21 SDA; GPIO22 SCL`；`rgb=GPIO25`；`power=+3.3V,+5V,BAT` |
| 射频 | ESP32 射频路径 | `soc=ESP32-D0WDQ6 LNA_IN`；`onboard=ANT1`；`external=ANT2 IPEX`；`selection=R1/R2 DNP options` |
| 保护电路 | M5 Bus ESD 保护 | `arrays=D3-D8 SRV05-4`；`series=R34-R56 47Ω`；`rails=MCU_VDD/GND` |

## 待确认事项

- `address.documented-i2c`：正文给出 AXP192=0x34、ATECC608=0x35、FT6336U=0x38、BM8563=0x51、MPU6886=0x68，但两张原理图未直接打印这些数值地址。（证据：图 6c305db1571c / 第 1 页 / Core2 页 I2C 器件与网络，无数值地址; 图 feed9faed66e / 第 1 页 / AWS 底座 U1/U4，无数值地址）
- `review.i2c-addresses`：K010-AWS 当前 AXP192、ATECC608、FT6336U、BM8563 和 MPU6886 的正式 7-bit 地址是否分别为 0x34/0x35/0x38/0x51/0x68？；原因：地址来自产品正文，两张原理图未直接打印数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6c305db1571c5d0b2bf6bf88a747719ac07a7be236002d15e44fc5974aa50204` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/CORE2_V1.0_SCH_page_01.png` |
| 2 | 1 | `feed9faed66efe07cc0154b96b20f4f8065edaffc9781a93fd10b215f30eed63` | `https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_sch_01.webp` |

---

源文档：`zh_CN/core/core2_for_aws.md`

源文档 SHA-256：`a3848d60556b6f6ffe8f70c80e1e481dd566b6b72b18647f2adb57df2a1982b9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
