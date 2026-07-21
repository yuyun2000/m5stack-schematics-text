# Core2 For AWS v1.3

<span class="product-sku">SKU:K010-AWS-V13</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13-weight.jpg">
</PictureViewer>

## 描述

Core2 For AWS v1.3 是一款专为 AWS 物联网学习与安全项目开发的套件，包含 M5Stack Core2 主控和集成加密芯片的 Base M5GO Bottom2 v1.3 拓展底座。
主控搭载双核 240MHz 的 ESP32-D0WDQ6-V3 芯片，配备 16MB Flash 与 8MB PSRAM，以及一块 2.0 英寸电容触摸屏，支持 Wi-Fi 无线连接。内置震动马达、RTC 计时模块、AXP192 电源管理芯片及绿色电源指示灯。预留 TF 卡槽，集成 I2C 音频功放与扬声器。机身左侧设电源键，底部设重启键，正面提供 3 个虚拟可编程按键。
拓展底座集成 ATECC608 加密芯片、BMI270 六轴姿态传感器、SPM1423 数字麦克风及 500mAh 锂电池。提供两组支持 ADC、DAC 和 UART 的 HY2.0-4P 接口。两侧共 10 颗采用磨砂导光的 SK6812 RGB 灯。底部配备 Pogo Pin 磁吸充电口，内置 TP4057 充电芯片，同时该接口引出 I2C 总线。底座内置磁铁与 LEGO 兼容孔位，并预留 CP2104 及锂电池接口，便于后续扩展，适用于智能家居安全终端原型设计，或边缘计算设备的可信数据采集与云端数据上传。

## 教程 & 快速上手

learn>| ![AWS IoT Core](https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_08.webp) | [AWS IoT Core](https://core2-for-aws-docs.m5stack.com) | 本教程介绍如何配置 Core2 For AWS 设备快速连接至 AWS IoT Core。 |

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core2/program) | 本教程介绍如何通过 UiFlow 图形化编程平台控制 Core2 For AWS 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core2/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Core2 For AWS 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core2/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Core2 For AWS 设备。 |

## 注意事项

- M5Core2 自带的震动马达与 M5 Base 系列底座在结构上存在干涉，为防止损坏设备，请勿将 M5Core2 与 M5 Base 系列功能底座堆叠使用。

- 部分屏幕边缘会存在触摸非线性的问题，可尝试使用 [M5Tool](https://github.com/m5stack/M5Tools) 来升级屏幕固件解决此问题。

## 产品特性

- ESP32-D0WDQ6-V3 核心主控
- 内置 ATECC608 硬件加密芯片
- 16MB Flash
- 8MB PSRAM
- 2.4 GHz Wi-Fi
- 内置扬声器
- 电源指示灯
- 震动马达
- RTC 时钟
- 电容式触摸屏幕
- 内置 500mAh 锂电池
- 独立外设拓展小板
  - 内置 BMI270 六轴姿态传感器
  - PDM 麦克风
- AXP192 电源管理
- microSD 插槽
- HY2.0-4P 拓展接口
- 开发平台：
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Core2 For AWS v1.3
- 1 x USB Type-C 连接线 (50cm)
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)

## 应用场景

- 物联网控制器
- DIY 作品制作

## 规格参数

| 规格            | 参数                                                 |
| --------------- | ---------------------------------------------------- |
| SoC             | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz              |
| SRAM            | 520KB                                                |
| Flash           | 16MB                                                 |
| PSRAM           | 8MB                                                  |
| Wi-Fi           | 2.4 GHz Wi-Fi                                        |
| 硬件加密芯片    | ATECC608B-TNGTLSU-G (addr 0x35)                      |
| 输入电压        | 5V @ 500mA                                           |
| 主机接口        | USB Type-C x1，Pogo Pin x1，I2C x1，GPIO x1，UART x1 |
| 可编程 LED 灯   | SK6812 x 10                                          |
| 按键            | 电源键、RST 键、屏幕虚拟按键 x 3                     |
| 震动提醒        | 震动马达                                             |
| IPS LCD 屏幕    | 2.0"@320 x 240 ILI9342C                              |
| 电容式触摸屏 IC | FT6336U                                              |
| 扬声器          | 1W-0928                                              |
| 麦克风          | SPM1423                                              |
| I2S 功放        | NS4168                                               |
| IMU             | BMI270                                               |
| RTC             | BM8563                                               |
| PMU             | AXP192                                               |
| USB-TTL         | CH9102F                                              |
| DC-DC 升压      | SY7088                                               |
| 锂电池          | 500mAh @ 3.7V                                        |
| 天线            | 2.4G 3D 天线                                         |
| 工作温度        | 0 ~ 40°C                                             |
| 外壳材质        | Plastic ( PC )                                       |
| 产品尺寸        | 54.0 x 54.0 x 23.7mm                                 |
| 产品重量        | 72.1g                                                |
| 包装尺寸        | 90.0 x 60.0 x 30.0mm                                 |
| 毛重            | 114.9g                                               |

## 操作说明

### 开关机操作

- 开机：单击左侧电源键
- 关机：长按左侧电源键
- 复位：单击底侧 RST 按键

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/Core2_For_AWS_v1.3.gif" width="40%">

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/IMU-Core2-For-AWS-v1.3.jpg" width="70%">

## 原理图

- [Core2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH.pdf)
- [M5GO-Bottom For AWS v1.3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/SCH_M5GO_Bottom2_SCH_Main_V1.3_AWS_Version_2026_01_30_10_06_42.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png" width="100%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/SCH_M5GO_Bottom2_SCH_Main_V1.3_AWS_Version_2026_01_30_10_06_42_page_01.png" width="100%">
</SchViewer>

## 管脚映射

### LCD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G5  | G15 |
| --------------- | ---- | ---- | --- | --- | --- |
| ILI9342C        | MISO | MOSI | SCK | CS  | DC  |

| AXP192 Chip | AXP_IO4 | AXP_DC3 | AXP_LDO2 |
| ----------- | ------- | ------- | -------- |
| ILI9342C    | RST     | BL      | PWR      |

### microSD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G4  |
| --------------- | ---- | ---- | --- | --- |
| microSD         | MISO | MOSI | SCK | CS  |

### Touch

| ESP32-D0WDQ6-V3 | G21 | G22 | G39 |
| --------------- | --- | --- | --- |
| FT6336U (0x38)  | SDA | SCL | INT |

| AXP192  | AXP_IO4 |
| ------- | ------- |
| FT6336U | RST     |

### Audio

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
| Green LED       | VCC     | /        |
| Vibration Motor |         | VCC      |

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
| BMI270 (0x68)   | SDA | SCL |
| Pogo Pin        | SDA | SCL |

### SK6812-LED

| ESP32-D0WDQ6-V3 | G25  |
| --------------- | ---- |
| SK6812-LED      | DATA |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BMI270 (0x68)   | SDA | SCL |
| AXP192 (0x34)   | SDA | SCL |
| BM8563 (0x51)   | SDA | SCL |
| FT6336U (0x38)  | SDA | SCL |
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

## 尺寸图

- [Core2 For AWS v1.3 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_Core2_For_AWS_v1.3_Dimension_Diagram.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_Core2_For_AWS_v1.3_Dimension_Diagram_page_01.png">
</SchViewer>

## 结构文件

- [Core2 For AWS v1.3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K010-AWS-V13_Core2_For_AWS_v1.3/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [FT6336U](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112.xlsx)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
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

请按所使用的操作系统，从下表下载并安装 **CH9102** USB 串口（VCP）驱动。安装 **CH9102_VCP_SER_MacOS v1.7** 时，安装程序可能提示报错，多为误报，驱动通常已正确安装，可忽略该提示并继续。 烧录或下载固件时出现失败、超时，或提示 `Failed to write to target RAM` 等异常时，可先尝试重新安装驱动、更换 USB 线或接口。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                              | 下载链接                                                                                                 | 备注 |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---- |
| Core2 For AWS v1.3 User Demo Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/Core2_For_AWS_User_Demo_Easyloader.exe) | /    |

## 相关视频

- Core2 For AWS v1.3 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_Core2_For_AWS_v1.3_video_ZH.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| Product Compare | [Core2 For AWS v1.3](/zh_CN/core/Core2_For_AWS_v1.3) ![Core2 For AWS v1.3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1226/K010-AWS-V13_main_pictures_02.webp) | [Core2 For AWS](/zh_CN/core/core2_for_aws) ![Core2 For AWS](https://static-cdn.m5stack.com/resource/docs/products/core/core2_for_aws/core2_for_aws_cover_01.webp) |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IMU             | BMI270                                                                                                                                                               | MPU6886                                                                                                                                                           |
| USB-TTL         | CH9102                                                                                                                                                               | CP2104/CH9102                                                                                                                                                     |
::

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K010-AWS)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
