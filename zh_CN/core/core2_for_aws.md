# Core2 For AWS

<span class="product-sku">SKU:K010-AWS</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/K010-AWS-package-01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/K010-AWS-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_09.webp">
</PictureViewer>

## 描述

**Core2 for AWS**是 AWS 物联网学习项目的专属套件。它由**M5Stack Core2**核心主控和**M5GO-Bottom For AWS**拓展底座组成，并且额外定制集成了 ATECC608 [Trust\&GO](https://www.microchip.com/design-centers/security-ics/trust-platform/trust-go) 硬件加密，是物联网学习和安全项目构建的理想套件。

其核心主控**Core2**配备了 ESP32-D0WDQ6-V3，具有两个可以单独控制的 Xtensa® 32-bit LX6 处理器，主频高达 240Mhz，支持 Wi-Fi 功能，板载 16MB Flash 与 8MB PSRAM，可通过 TYPE-C 接口下载程序，强劲的配置满足复杂应用的资源开销。正面搭载一块 2.0 寸一体化电容式触摸屏，为用户带来更流畅的人机交互体验。机身内置震动马达，可提供触觉回馈和震动提醒功能。内建的 RTC 模块可提供精准计时功能。电源部分搭载 AXP192 电源管理芯片可有效控制机身功耗，内置绿色电源指示灯。同时机身内配备了 TF-card (microSD) 卡槽与扬声器，为了保证获得更高质量的声音效果，采用 I2S 数字音频接口的功放芯片，能有效防止信号失真。在机身的左侧和底部配有独立的电源按键与重启 (RST) 按键，屏幕正面的 3 个圆点属于触摸屏的一部分，可通过编写程序设置热区映射为 3 个虚拟按键。

**M5GO-Bottom For AWS 是专为该定制款设计的拓展型底座，底座集成了 MPU6886 六轴姿态传感器，数字麦克风 (SPM1423)，500mAh 锂电池。提供两组 HY2.0-4P 拓展接口将常用的 ADC/DAC/UART 引脚进行了引出，能够用于各类型传感器的接入。底座两侧分别为 10 颗可编程 RGB 灯 (SK6812)，配合磨砂透光材质遮光条，能够提供柔和舒适发光效果。底部采用 pogo pin 磁吸充电接口，当吸附充电底座时，电流将经过内置的 TP4057 充电芯片安全的流入内部电池。除充电功能外 pogo pin 接口对主控 I2C 总线进行了引出，这使得你能够通过磁吸的方式去外接拓展。内置吸附磁铁，背面采用兼容 LEGO 孔设计，能够与你的其他的 LEGO 结构设计无缝对接。Core2 for AWS 的 PCB 板上预留了 CP2104 芯片的接口，与锂电池接口。**
**AWS 定制款嵌入了 ATECC608 硬件加密芯片，能够以硬件层次密钥的方式加强设备物联网通信过程的安全**

## 教程 & 快速上手

learn>| ![AWS IoT Core](https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_08.webp) | [AWS IoT Core](https://core2-for-aws-docs.m5stack.com) | 本教程介绍如何配置 Core2 For AWS 设备快速连接至 AWS IoT Core。 |

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core2/program) | 本教程介绍如何通过 UiFlow 图形化编程平台控制 Core2 For AWS 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core2/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Core2 For AWS 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core2/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Core2 For AWS 设备。 |

## 注意事项

- M5Core2 自带的震动马达与 M5 Base 系列底座在结构上存在干涉，为防止损坏设备，请勿将 M5Core2 与 M5 Base 系列功能底座堆叠使用。

- 部分屏幕边缘会存在触摸非线性的问题，你可以尝试使用 [M5Tool](https://github.com/m5stack/M5Tools) 来升级屏幕固件解决此问题。

## 产品特性

- 基于 ESP32 开发，支持 Wi-Fi
- 内置 ATECC608 硬件加密芯片
- 16MB Flash，8MB PSRAM
- 内置扬声器，电源指示灯，震动马达，RTC，I2S 功放，电容式触摸屏幕，电源键，复位按键
- microSD 插槽 (支持最大 16GB)
- 内置锂电池，配备电源管理芯片
- 内置 6 轴 IMU，PDM 麦克风
- M5-Bus socket
- 开发平台：
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x M5Stack Core2
- 1 x M5GO Bottom2 for AWS
- 1 x USB Type-C 连接线 (50cm)
- 1 x Hex wrench

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品制作

## 规格参数

| 规格            | 参数                                             |
| --------------- | ------------------------------------------------ |
| SoC             | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz          |
| DMIPS           | 600                                              |
| SRAM            | 520KB                                            |
| Flash           | 16MB                                             |
| PSRAM           | 8MB                                              |
| Wi-Fi           | 2.4 GHz Wi-Fi                                    |
| 硬件加密芯片    | ATECC608B-TNGTLSU-G (addr 0x35)                  |
| 输入电压        | 5V @ 500mA                                       |
| 主机接口        | Type-C x1，POGO PIN x1，I2C x1，GPIO x1，UART x1 |
| 可编程 LED 灯   | SK6812\*10                                       |
| 按键            | 电源键、RST 键、屏幕虚拟按键 \* 3                |
| 震动提醒        | 震动马达                                         |
| IPS LCD 屏幕    | 2.0"@320 x 240 ILI9342C                          |
| 电容式触摸屏 IC | FT6336U                                          |
| 扬声器          | 1W-0928                                          |
| 麦克风          | SPM1423                                          |
| I2S 功放        | NS4168                                           |
| IMU             | MPU6886                                          |
| RTC             | BM8563                                           |
| PMU             | AXP192                                           |
| USB 芯片        | CP2104                                           |
| DC-DC 升压      | SY7088                                           |
| microSD 槽      | 支持最大 16G                                     |
| 锂电池          | 500mAh @ 3.7V                                    |
| 天线            | 2.4G 3D 天线                                     |
| 工作温度        | 0 ~ 40°C                                         |
| 外壳材质        | Plastic ( PC )                                   |
| 产品尺寸        | 54.0 x 54.0 x 23.5mm                             |
| 产品重量        | 69.5g                                            |
| 包装尺寸        | 90.0 x 60.0 x 30.0mm                             |
| 毛重            | 110.0g                                           |

## 操作说明

### 开关机操作

- 开机：单击左侧电源键
- 关机：长按 6 秒左侧电源键
- 复位： 单击底侧 RST 按键

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/IMU-Core2-For-AWS.jpg" width="70%">

## 原理图

- [Core2 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/CORE2_V1.0_SCH.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/CORE2_V1.0_SCH_page_01.png" width="100%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_sch_01.webp" width="100%">
</SchViewer>

## 管脚映射

### LCD 屏幕 & TF Card

LCD 像素：320x240
microSD 最大支持 16GB

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G5  | G15 |
| --------------- | ---- | ---- | --- | --- | --- |
| ILI9342C        | MISO | MOSI | SCK | CS  | DC  |

| AXP192 Chip | AXP_IO4 | AXP_DC3 | AXP_LDO2 |
| ----------- | ------- | ------- | -------- |
| ILI9342C    | RST     | BL      | PWR      |

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G4  |
| --------------- | ---- | ---- | --- | --- |
| TF Card         | MISO | MOSI | SCK | CS  |

### CAP.TOUCH (I2C Addr: 0x38)

| ESP32-D0WDQ6-V3 | G21 | G22 | G39 |
| --------------- | --- | --- | --- |
| FT6336U (0x38)  | SDA | SCL | INT |

| AXP192  | AXP_IO4 |
| ------- | ------- |
| FT6336U | RST     |

### 麦克风 & NS4168 功放

| ESP32-D0WDQ6-V3 | G12  | G0   | G2   | G34  |
| --------------- | ---- | ---- | ---- | ---- |
| NS4168          | BCLK | LRCK | DATA |      |
| SPM1423         |      | CLK  |      | DATA |

| AXP192 | AXP_IO2 |
| ------ | ------- |
| NS4168 | SPK_EN  |

### AXP 电源指示灯 & 震动马达

| AXP192          | AXP_IO1 | AXP_LDO3 |
| --------------- | ------- | -------- |
| Green LED       | Vcc     | /        |
| Vibration motor |         | Vcc      |

### RTC

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BM8563 (0x51)   | SDA | SCL |

| AXP192 | AXP_PWR |
| ------ | ------- |
| BM8563 | INT     |

### IMU（3 轴陀螺仪 + 3 轴加速计） \&Pogo Pin

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| MPU6886 (0x68)  | SDA | SCL |
| Pogo Pin        | SDA | SCL |

### USB 转串口下载

| ESP32-D0WDQ6-V3 | G1  | G3  |
| --------------- | --- | --- |
| CP2104          | RXD | TXD |

### SK6812-LED

| ESP32-D0WDQ6-V3 | G25  |
| --------------- | ---- |
| SK6812-LED      | DATA |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| MPU6886         | SDA | SCL |
| AXP192 (0x34)   | SDA | SCL |
| BM8563          | SDA | SCL |
| FT6336U         | SDA | SCL |
| ATECC608 (0x35) | SDA | SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G32    | G33   |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G14    | G13   |
::

### M5-Bus

::m5-bus-table
| FUNC       | PIN | LEFT | RIGHT | PIN | FUNC       |
| ---------- | --- | ---- | ----- | --- | ---------- |
|            | GND | 1    | 2     | G35 | ADC        |
|            | GND | 3    | 4     | G36 | ADC        |
|            | GND | 5    | 6     | RST | EN         |
| MOSI       | G23 | 7    | 8     | G25 | DAC        |
| MISO       | G38 | 9    | 10    | G26 | DAC        |
| SCK        | G18 | 11   | 12    | 3V3 |            |
| RXD0       | G3  | 13   | 14    | G1  | TXD0       |
| RXD2       | G13 | 15   | 16    | G14 | TXD2       |
| Int SDA    | G21 | 17   | 18    | G22 | Int SCL    |
| PORT.A SDA | G32 | 19   | 20    | G33 | PORT.A SCL |
| GPIO       | G27 | 21   | 22    | G19 | GPIO       |
| I2S_DOUT   | G2  | 23   | 24    | G0  | I2S_LRCK   |
|            | NC  | 25   | 26    | G34 | I2S_DATA   |
|            | NC  | 27   | 28    | 5V  |            |
|            | NC  | 29   | 30    | BAT |            |
::

### M5Core2 端口说明

**HY2.0-4P-PortA(Red)**

| ESP32 Chip | G32      | G33      |
| ---------- | -------- | -------- |
| PortA      | G32(SDA) | G33(SCL) |

### M5GO-Bottom For AWS 端口说明

**HY2.0-4P-PortB(black)**

| ESP32 Chip | G26      | G36      |
| ---------- | -------- | -------- |
| PortB      | G26(DAC) | G36(ADC) |

**HY2.0-4P-PortC(blue)**

| ESP32 Chip | G13       | G14       |
| ---------- | --------- | --------- |
| PortC      | G13(RXD2) | G14(TXD2) |

**充电电流测量值**

| 充电电流 | 充满后电流（关机） | 充满电（开机） |
| -------- | ------------------ | -------------- |
| 0.219A   | 0.055A             | 0.147A         |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/core2_for_aws/img-dea808fa-615c-41c0-9d1c-b1c4d56f3900.jpg" width="100%" />

## 结构文件

- [Core2 For AWS 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K010-AWS_Core2_For_AWS/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [FT6336U](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112.xlsx)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY7088-Silergy.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [ATECC608](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ATECC608A-TNGTLS-CryptoAuthentication-Data-Sheet-DS40002112B.pdf)
- [1027DC Motor](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/1027RFN01-33d.pdf)

## 软件开发

### 快速上手

- [连接 AWS IoT Core](https://core2-for-aws-docs.m5stack.com)

### Arduino

- [Core2 for AWS Arduino 快速上手](/zh_CN/arduino/m5core2/program)
- [Core2 for AWS Arduino 驱动库](https://github.com/m5stack/M5Core2)
- [Core2 for AWS Arduino API](/zh_CN/arduino/m5core2/button)

### UiFlow1

- [Core2 For AWS UiFlow1 快速上手](/zh_CN/uiflow/m5core2/program)

### UiFlow2

- [Core2 For AWS UiFlow2 快速上手](/zh_CN/uiflow2/m5core2/program)

### PlatformIO

```
[env:m5stack-core2-for-aws]
platform = espressif32@6.12.0
board = m5stack-core2
framework = arduino
upload_speed = 921600
monitor_speed = 115200
board_build.partitions = default_16MB.csv
build_type = debug
build_flags =
    -DBOARD_HAS_PSRAM
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### ESP-IDF

[Core2 For AWS ESP-IDF 案例程序](https://github.com/m5stack/Core2-for-AWS-IoT-Kit)
[Core2 For AWS ESP-IDF 出厂程序](https://github.com/m5stack/Core2-for-AWS-IoT-Kit/tree/master/Factory-Firmware)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                         | 下载链接                                                                                                              | 备注 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Core2 For AWS User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_Core2_for_AWS_Default.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/CORE2_FOR_AWS.mp4" type="video/mp4">
</video>

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/CORE2_FOR_AWS_FACTORY2.mp4" type="video/mp4">
</video>

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K010-AWS)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动          | 备注：         |
| -------- | ----------------- | -------------- |
| 2023.2   | 取消 RTC 纽扣电池 | 不影响定时功能 |
