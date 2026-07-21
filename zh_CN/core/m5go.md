# M5GO IoT Kit

<span class="product-sku">SKU:K006</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_05.webp">
</PictureViewer>

## 描述

**M5GO IoT Kit** 是 M5Stack 开发套件系列中面向 STEM 教育的一款开发套件。除了主机 M5GO 之外，套件内还包含 6 个不同功能的 Unit 以及一些乐高积木等配件。M5GO 不仅具备丰富的硬件资源，还拥有大量的教学视频、教科书、技术文档等资料。在针对各年龄段学生的 STEM 教育方面，它发挥着重要作用。

套件提供线上版本的 WebIDE UiFlow 编程平台，通过网络推送程序的方式，让学生切实体会物联网的强大之处。同时，其支持多种编程方式，能够帮助学生逐步从图形化编程过渡到对实际代码的理解。

作为一款专为 STEM 教育设计的套件，M5GO 旨在让学生在获取知识的同时收获乐趣，以及将创意逐步转化为现实的荣誉感。它让学生能够自由地探索工程世界，制作属于自己的物联网产品，并将精彩的创意融入到现实生活当中。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 M5GO 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 M5GO 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5go_kit/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 M5GO 设备 |

## 产品特性

- 基于 ESP32 开发
- 集成 3 轴磁力计、3 轴陀螺仪和 3 轴加速计
- 内置扬声器，按键，LCD 屏幕，电源 / 复位按键
- microSD 插槽 (最大可拓展 16GB)
- 可拓展的引脚与接口
- M5-Bus 总线母座
- 内置电池
- 背部磁吸式充电设计
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x M5GO
- 6 x Units（Unit ENV-II，Unit PIR，Unit Angle，Unit IR，Unit RGB，Unit Hub）
- 4 x LEGO 积木
- 12 x LEGO 连接件
- 4 x GROVE 线
- 1 x USB Type-C 连接线 (20cm)
- 1 x M2\*12 机械牙螺丝
- 2 x M3\*16 机械牙螺丝
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
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
| 按键     | 自定义按键 x 3                                              |
| 喇叭     | 1W-0928                                                     |
| 麦克风   | MEMS Analog BSE3729 Microphone                              |
| LED      | SK6812 3535 RGB LED x 10                                    |
| MEMS     | BMM150 + MPU6886                                            |
| 电池     | 500mAh@3.7V，inside vb                                      |
| 天线     | 2.4G 3D 天线                                                |
| 工作温度 | 0 ~ 60°C                                                    |
| 外壳材质 | Plastic ( PC )                                              |
| 产品尺寸 | 54.0 x 54.0 x 21.0 mm                                       |
| 产品重量 | 56.4g                                                       |
| 包装尺寸 | 147.0 x 90.0 x 40.0 mm                                      |
| 毛重     | 228.0g                                                      |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 开关机

开机：单击左侧红色电源键
关机：快速双击左侧红色电源键
USB 供电：默认情况下，USB 供电时，无法进行关机

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5go/m5go_sch_01.webp" width="80%">

- [M5Core 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206_sch_06.png">
</SchViewer>

## 管脚映射

### LCD 屏幕 & microSD

LCD 像素：320x240
microSD 最大支持 16GB

| ESP32-D0WDQ6-V3 | G23       | G19  | G18 | G14 | G27 | G33 | G32 | G4  |
| --------------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| ILI9342C        | MOSI/MISO | /    | CLK | CS  | DC  | RST | BL  |     |
| microSD         | MOSI      | MISO | CLK |     |     |     |     | CS  |

### 按键 & 喇叭

| ESP32-D0WDQ6-V3 | G39      | G38      | G37      | G25      |
| --------------- | -------- | -------- | -------- | -------- |
| 按键引脚        | BUTTON A | BUTTON B | BUTTON C |
| 喇叭            |          |          |          | 喇叭引脚 |

### GROVE 接口 A & IP5306

电源管理芯片 (IP5306) 是定制 I2C 版本，它的 I2C 地址是 0x75。点击[这里](https://github.com/m5stack/M5-Schematic/blob/master/Core/I2C_IP5306_REG_V1.4.pdf)查看 IP5306 的寄存器手册。

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| GROVE A         | SCL | SDA | 5V  | GND |
| IP5306 (0x75)   | SCL | SDA | 5V  | GND |

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
| MPU6886 (0x68)  | SCL | SDA | 5V  | GND |

### BMM150 3 轴磁力计

BMM150 I2C address 0x10

| ESP32-D0WDQ6-V3 | G22 | G21 | 5V  | GND |
| --------------- | --- | --- | --- | --- |
| BMM150 (0x10)   | SCL | SDA | 5V  | GND |

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/gray/mpu6886_bmm150_axis.webp">

## M5GO 底座管脚

### LED 灯条 & 麦克风 MIC

| ESP32-D0WDQ6-V3 | G15      | G34      | G25 |
| --------------- | -------- | -------- | --- |
| LED 灯条        | SIG 管脚 |          |     |
| 麦克风 MIC      |          | MIC 管脚 |     |

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
| PORT.C   | GND   | 5V  | G17    | G16   |
::

### M5-Bus

::m5-bus-table
| FUNC    | PIN  | LEFT | RIGHT | PIN | FUNC    |
| ------- | ---- | ---- | ----- | --- | ------- |
|         | GND  | 1    | 2     | G35 | ADC     |
|         | GND  | 3    | 4     | G36 | ADC     |
|         | GND  | 5    | 6     | RST | EN      |
| MOSI    | G23  | 7    | 8     | G25 | DAC/SPK |
| MISO    | G19  | 9    | 10    | G26 | DAC     |
| SCK     | G18  | 11   | 12    | 3V3 |         |
| RXD0    | G3   | 13   | 14    | G1  | TXD0    |
| RXD2    | G16  | 15   | 16    | G17 | TXD2    |
| Int SDA | G21  | 17   | 18    | G22 | Int SCL |
| GPIO    | G2   | 19   | 20    | G5  | GPIO    |
| I2S_SK  | G12  | 21   | 22    | G13 | I2S_WS  |
| I2S_OUT | G15  | 23   | 24    | G0  | I2S_MK  |
|         | HPWR | 25   | 26    | G34 | I2S_IN  |
|         | HPWR | 27   | 28    | 5V  |         |
|         | HPWR | 29   | 30    | BAT |         |
::

在使用 G15 的 RGB LED 时，建议初始化引脚 pinMode (15，OUTPUT_OPEN_DRAIN);
有关引脚分配和引脚重新映射的更多信息，请参考[ESP32 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)
- [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [M5GO Arduino 快速上手](/zh_CN/arduino/m5go_kit/program)
- [M5GO 传感器套件 Arduino 案例程序](/zh_CN/arduino/m5go_kit/sensor)
- [M5GO IoT Kit Arduino 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Basics)
- [M5GO Arduino API](/zh_CN/arduino/m5core/button)

### UiFlow1

- [M5GO UiFlow1 快速上手](/zh_CN/uiflow/m5core/program)

### UiFlow2

- [M5GO UiFlow2 快速上手](/zh_CN/uiflow2/m5core/program)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

EasyLoader 是一个简洁快速的程序烧录器，其内置了一个产品相关的案例程序，通过简单步骤将其烧录至主控，即可进行一系列的功能验证。

| Easyloader                        | 下载链接                                                                                                                             | 备注 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| M5GO IoT Kit User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5go_v2.7/M5GO%20IoT%20Starter%20Kit%20v2.7.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5GO.mp4" type="video/mp4">
</video>

\#> 案例描述 | 加载 UiFlow 固件，内置演示程序支持加速计，LED BAR，麦克风，按键及部分外设传感器的测试，固件可用于 UiFlow 图形化编程。

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K006)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                              | 备注：                                                               |
| -------- | ------------------------------------- | -------------------------------------------------------------------- |
| 2020.6   | 套件内 ENV Unit 更改为 Unit ENV-II    | /                                                                    |
| 2019.11  | 电池容量 600mAh 变更为 500mAh         | /                                                                    |
| 2019.7   | TN 屏幕变更为 IPS 屏幕                | 请将您的 M5Stack 库升级到最新版本(v0.2.8 以上)，以解决屏幕反色问题。 |
| 2019.6   | MPU9250 变更为 MPU6886+BMM150         | /                                                                    |
| 2018.4   | 首次发售                              | /                                                                    |

\#> 注意：**2018.2A**PCB 版本的设备不支持 C2C (Type-C to Type-C) 连接及 PD 供电。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.6/basic_v2.6_2018.2a.webp" width="50%">
