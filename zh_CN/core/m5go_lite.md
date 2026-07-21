# M5GO-Lite

<span class="product-sku">SKU:K022</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go_lite/m5go_lite_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go_lite/m5go_lite_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go_lite/m5go_lite_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go_lite/m5go_lite_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go_lite/m5go_lite_05.webp">
</PictureViewer>

## 描述

**M5GO-Lite** 是 M5Stack 开发套件系列中的一款轻量级的 STEM 教育套件。M5GO Lite 提供了 1 个 ENV Unit （用作环境温湿度、气压检测） 。与 “M5GO IoT Kit” 相比，它在 Unit 以及配件的数量上进行了删减，以此换取一定的搭配自由，对于想要自己购买其他 Unit 或是开展小型 STEM 课程的用户来说，M5GO-Lite 是一个不错的选择。

提供线上版本的 WebIDE UiFlow 编程平台，通过网络推送程序的方式，让学生切身体会物联网的强大。支持多种编程方式，帮助学生逐步由图形化编程进阶到对实际代码的理解。

作为一款专为 STEM 教育而设计的套件，M5GO 想要做到的是使学生在获得知识的同时，收获乐趣，收获那份将自己的创意一步一步转换为现实的荣誉感。让学生可以自由地探索工程世界，制作自己的物联网产品，并将精彩的创意融入到现实生活中。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 M5GO 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 M5GO 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 M5GO 设备 |

learn>| ![Micropython](https://static-cdn.m5stack.com/resource/docs/static/assets/micropython_banner_01.png) | [Micropython](/zh_CN/mpy/official/machine) | 本教程将向你介绍，如何通过 Micropython 编程控制 M5GO 设备 |

## 产品特性

- 基于 ESP32 开发
- 集成 3 轴加速计、3 轴陀螺仪和 3 轴磁力计
- 内置扬声器，按键，LCD 屏幕、电源 / 复位按键
- microSD 卡插槽 (最大可拓展 16GB)
- 可拓展的引脚与接口
- M5-Bus 总线母座
- 内置锂电池
- 背部磁吸式充电设计
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x M5GO
- 1 x ENV Unit
- 1 x GROVE 线
- 1 x USB Type-C 连接线 (20cm)
- 1 x 使用手册

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备

## 规格参数

| 主控资源 | 参数                                                        |
| -------- | ----------------------------------------------------------- |
| SoC      | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                     |
| DMIPS    | 600                                                         |
| SRAM     | 520KB                                                       |
| Flash    | 16MB                                                        |
| Wi-Fi    | 2.4 GHz Wi-Fi                                               |
| 输入电压 | 5V@500mA                                                    |
| 主机接口 | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                    |
| IPS 屏幕 | 2 inch，320x240 Colorful TFT LCD，ILI9342C，最高亮度 853nit |
| 扬声器   | 1W-0928                                                     |
| 麦克风   | MEMS Analog BSE3729 Microphone                              |
| 按键     | 自定义按键 x 3                                              |
| LED      | SK6812 3535 RGB LED x 10                                    |
| MEMS     | BMM150 + MPU6886                                            |
| 天线     | 2.4G 3D 天线                                                |
| 底座接口 | PORT.A (I2C)、PORT.B (GPIO)、PORT.C (UART)                  |
| 电池     | 500mAh@3.7V，inside vb                                      |
| 工作温度 | 0 ~ 60°C                                                    |
| 外壳材质 | Plastic ( PC )                                              |
| 产品尺寸 | 54.0 x 54.0 x 21.0 mm                                       |
| 产品重量 | 56.4g                                                       |
| 包装尺寸 | 105.0 x 65.0 x 40.0 mm                                      |
| 毛重     | 159.0g                                                      |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 开关机

\#> 开关机操作 | 开机：单击左侧红色电源键<br/>关机：快速双击左侧红色电源键<br/>注意：默认情况下，USB 供电时，无法进行关机

## 原理图

- [M5GO 原理图 PDF](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/M5-Core-Schematic(20171206).pdf>)

## 管脚映射

### LCD & TF card

LCD :320x240
TF card Maximum size 16GB

| ESP32-D0WDQ6-V3 | G23       | G19  | G18 | G14 | G27 | G33 | G32 | G4  |
| --------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| ILI9342C        | MOSI/MISO | /    | CLK | CS  | DC  | RST | BL  |     |
| TF Card         | MOSI      | MISO | CLK |     |     |     |     | CS  |

### Button & Speaker

| ESP32-D0WDQ6-V3 | G39      | G38      | G37      | G25         |
| --------------- | -------- | -------- | -------- | ----------- |
| Button Pin      | BUTTON A | BUTTON B | BUTTON C |
| Speaker         |          |          |          | Speaker Pin |

### GROVE Port A & IP5306

We’ve use the customized I2C version of IP5306 in power management.
Its I2C address is 0x75. Click [here](https://github.com/m5stack/M5-Schematic/blob/master/Core/IIC_IP5306_REG_V1.4.pdf) to check its datasheet.

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| GROVE A         | SCL | SDA | 5V  | GND |
| IP5306          | SCL | SDA | 5V  | GND |

### IP5306 charging/discharging,Voltage parameter

| charging            | discharging          |
| ------------------- | -------------------- |
| 0.00 ~ 3.40V -> 0%  | 4.20 ~ 4.07V -> 100% |
| 3.40 ~ 3.61V -> 25% | 4.07 ~ 3.81V -> 75%  |
| 3.61 ~ 3.88V -> 50% | 3.81 ~ 3.55V -> 50%  |
| 3.88 ~ 4.12V -> 75% | 3.55 ~ 3.33V -> 25%  |
| 4.12 ~ / -> 100%    | 3.33 ~ 0.00V -> 0%   |

### 6-Axis MotionTracking Sensor MPU6886

MPU6886 I2C address 0x68

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| MPU6886         | SCL | SDA | 5V  | GND |

### 3-Axis Geomagnetic Sensor BMM150

BMM150 I2C address 0x10

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| BMM150          | SCL | SDA | 5V  | GND |

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/gray/mpu6886_bmm150_axis.webp">

### M5GO 底座

[点击查看详情参数](/zh_CN/base/m5go_bottom)

## 外设的管脚映射

### LCD 屏幕 & microSD

_LCD 像素：320x240_
_microSD 最大支持 16GB_

| ESP32-D0WDQ6-V3 | G23       | G19  | G18 | G14 | G27 | G33 | G32 | G4  |
| --------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| ILI9342C        | MOSI/MISO | /    | CLK | CS  | DC  | RST | BL  |     |
| TF Card         | MOSI      | MISO | CLK |     |     |     |     | CS  |

### 按键 & 喇叭

| ESP32-D0WDQ6-V3 | G39      | G38      | G37      | G25      |
| --------------- | -------- | -------- | -------- | -------- |
| 按键引脚        | BUTTON A | BUTTON B | BUTTON C |          |
| 喇叭            |          |          |          | 喇叭引脚 |

### GROVE 接口 A & IP5306

电源管理芯片 (IP5306) 是定制 I2C 版本，它的 I2C 地址是 0x75。点击[这里](https://github.com/m5stack/M5-Schematic/blob/master/Core/I2C_IP5306_REG_V1.4.pdf)查看 IP5306 的寄存器手册。

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| GROVE A         | SCL | SDA | 5V  | GND |
| IP5306          | SCL | SDA | 5V  | GND |

### IP5306 充 / 放电，电压参数

| 充电                | 放电                 |
| ------------------- | -------------------- |
| 0.00 ~ 3.40V -> 0%  | 4.20 ~ 4.07V -> 100% |
| 3.40 ~ 3.61V -> 25% | 4.07 ~ 3.81V -> 75%  |
| 3.61 ~ 3.88V -> 50% | 3.81 ~ 3.55V -> 50%  |
| 3.88 ~ 4.12V -> 75% | 3.55 ~ 3.33V -> 25%  |
| 4.12 ~ /-> 100%     | 3.33 ~ 0.00V -> 0%   |

### MPU6886 陀螺仪加速计

MPU6886 I2C address 0x68

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| MPU6886         | SCL | SDA | 5V  | GND |

### BMM150 3 轴磁力计

BMM150 I2C address 0x10

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| BMM150          | SCL | SDA | 5V  | GND |

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/gray/mpu6886_bmm150_axis.webp">

## M5GO 底座管脚

### LED 灯条 & 麦克风 MIC & 喇叭 Speaker

| ESP32-D0WDQ6-V3 | G15      | G34      | G25          |
| --------------- | -------- | -------- | ------------ |
| LED 灯条        | SIG 管脚 |          |              |
| 麦克风 MIC      |          | MIC 管脚 |              |
| 喇叭            |          |          | Speaker 管脚 |

### ESP32 ADC/DAC

| ADC1   | ADC2               | DAC1   | DAC2   |
| ------ | ------------------ | ------ | ------ |
| 8 通道 | 10 通道            | 2 通道 | 2 通道 |
| G32-39 | G0/2/4/12-15/25-27 | G25    | G26    |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G21    | G22   |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G16    | G17   |
::

### M5-Bus

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/common/core1_mbus.webp" alt="M_BUS"  width="60%" height="36%">

在使用 GPIO15 的 RGB LED 时，建议初始化引脚 pinMode (15，OUTPUT_OPEN_DRAIN);
有关引脚分配和引脚重新映射的更多信息，请参考[ESP32 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)

## 数据手册

- **Datasheet**

  - [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
  - [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
  - [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
  - [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)
  - [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [M5GO Arduino 快速上手](/zh_CN/arduino/m5core/button)
- [M5GO Arduino 测试程序](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/M5-Core-Schematic(20171206).pdf>)
- [Arduino API](/zh_CN/arduino/m5core/button)

### UiFlow1

- [M5GO UiFlow1 快速上手](/zh_CN/uiflow/m5core/program)
- [UiFlow1 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/ENV/UiFlow)

### UiFlow2

- [M5GO UiFlow2 快速上手](/zh_CN/uiflow2/m5core/program)

### Easyloader

| Easyloader                | 下载链接                                                                                   | 备注 |
| ------------------------- | ------------------------------------------------------------------------------------------ | ---- |
| M5GO User Demo Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/656/Fire_Factory_Firmware.exe) | /    |

### USB 驱动

\#>Click the link below to download the driver that matches the operating system. There are currently two driver chip versions (CP210X/CH9102). Please download the corresponding driver compressed package according to the version you are using. After decompressing the compressed package, select the installation package corresponding to the number of operating systems to install. (If you are not sure of the USB chip used by your device, you can install both drivers at the same time. During the installation process of **CH9102_VCP_SER_MacOS v1.7**, an error may occur, but the installation is actually completed, just ignore it.)

| Driver name               | Applicable driver chip | Download link                                                                                        |
| ------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102                 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

\\

## 相关视频

- **m5stack 的简介**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/m5stack%E7%AE%80%E4%BB%8B%EF%BC%88%E4%B8%AD%E6%96%87%EF%BC%89.mp4" type="video/mp4">
</video>

\#> 注意：**2018.2A**PCB 版本的设备不支持 C2C (Type-C to Type-C) 连接及 PD 供电。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.6/basic_v2.6_2018.2a.webp" width="50%">

## 版本变更

| 上市日期 | 产品变动                          | 备注：                                                               |
| -------- | --------------------------------- | -------------------------------------------------------------------- |
| 2019.11  | 电池容量 600mAh 变更为 500mAh     | /                                                                    |
| 2019.7   | TN 屏幕变更为 IPS 屏幕            | 请将您的 M5Stack 库升级到最新版本(v0.2.8 以上)，以解决屏幕反色问题。 |
| 2019.6   | MPU9250 变更为 MPU6886+BMM150     | /                                                                    |
| 2018.4   | 首次发售                          | /                                                                    |
