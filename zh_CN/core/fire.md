# Fire

<span class="product-sku">SKU:K007</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_07.webp">
</PictureViewer>

## 描述

**Fire** 是 M5Stack 开发套件系列中的一款，主打高性能的开发套件。它作为 Gray 套件的升级版，提供九轴运动传感器 (六轴姿态加速度计 + 三轴磁力计)，配备更强性能的硬件资源：16M Flash，8M PSRAM，增强型 Base ( M5GO 底座和 M5GO 充电底座) ，更大容量的电池等。对于对硬件性能方面有所要求的开发者来说，Fire 是一个非常不错的选择。

我们可以在很多的应用场景中使用姿态传感器用作：检测加速度、角度、轨迹延伸等数据。根据这些去制作出相关的产品，如运动数据采集器，3D 远程手势控制器等。

Fire 配有三个可分离部件。顶部与其他的 M5 主机一样，放置了电路板，芯片，LCD 屏幕，2.4G 天线，各种电子元器件以及一些接口组件。中间部分称为 M5GO 底座，提供锂电池，M5-Bus 总线母座，LED 条和三个 GROVE 拓展端口。位于最底部的是充电底座，可以与 M5GO 底座通过 POGO 引脚进行连接，进行充电。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5fire/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 Fire 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5fire/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Fire 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5fire/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Fire 设备 |

## 产品特性

- 基于 ESP32 开发
- 外挂 PSRAM
- 内集成 3 轴陀螺仪、3 轴加速计和 3 轴磁力计
- 内置扬声器，按键，LCD 屏幕，电源 / 复位按键
- microSD 插槽 (最大可拓展 16GB)
- 内置锂电池
- 背部磁吸式设计
- 可拓展的引脚与接口
- M5-Bus 总线母座
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Fire
- 1 x M5GO 充电底座
- 2 x LEGO 积木
- 5 x LEGO 连接件
- 1 x M3 六角扳手
- 1 x USB Type-C 连接线 (100cm)
- 1 x 使用手册

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备

## 规格参数

| 主控资源 | 参数                                                        |
| -------- | ----------------------------------------------------------- |
| SoC      | ESP32-D0WDQ6@双核处理器，主频 240MHz                        |
| DMIPS    | 600                                                         |
| SRAM     | 520KB                                                       |
| Flash    | 16MB                                                        |
| PSRAM    | 8MB Quad                                                    |
| Wi-Fi    | 2.4 GHz Wi-Fi                                               |
| 输入电压 | 5V@500mA                                                    |
| 主机接口 | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                    |
| IPS 屏幕 | 2 inch，320x240 Colorful TFT LCD，ILI9342C，最高亮度 853nit |
| 扬声器   | 1W-0928                                                     |
| 麦克风   | MEMS Analog BSE3729 Microphone                              |
| LED      | SK6812 3535 RGB LED x 10                                    |
| MEMS     | BMM150 + SH200Q/MPU6886                                     |
| 天线     | 2.4G 3D 天线                                                |
| 底座接口 | PortA (I2C)、PortB (GPIO)、PortC (UART)                     |
| 电池     | 500 mAh @ 3.7V，inside vb                                   |
| 工作温度 | 0 ~ 60°C                                                    |
| 外壳材质 | Plastic ( PC )                                              |
| 产品尺寸 | 54.0 x 54.0 x 28.6mm                                        |
| 产品重量 | 62.6g                                                       |
| 包装尺寸 | 106.7 x 69.1 x 40.4mm                                       |
| 毛重     | 123.8g                                                      |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 开关机

- 开机：单击左侧红色电源键
- 关机：快速双击左侧红色电源键
- USB 供电：默认情况下，USB 供电时，无法进行关机

\#> 注意 | FIRE 中的 GPIO 16 / 17 默认与 PSRAM 连接，因此当你在连接或是堆叠其他功能模块时，需要注意避免与这两个引脚冲突，防止设备不正常工作，产生不稳定的现象。

## 原理图

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

| ESP32-D0WDQ6 | G23       | G19  | G18 | G14 | G27 | G33 | G32 | G4  |
| ------------ | --------- | ---- | --- | --- | --- | --- | --- | --- |
| ILI9342C     | MOSI/MISO | /    | CLK | CS  | DC  | RST | BL  |     |
| microSD      | MOSI      | MISO | CLK |     |     |     |     | CS  |

### 按键 & 喇叭

| ESP32-D0WDQ6 | G39      | G38      | G37      | G25      |
| ------------ | -------- | -------- | -------- | -------- |
| 按键引脚     | BUTTON A | BUTTON B | BUTTON C |          |
| 喇叭         |          |          |          | 喇叭引脚 |

### GROVE 接口 A & IP5306

电源管理芯片 (IP5306) 是定制 I2C 版本，它的 I2C 地址是 0x75。点击[这里](https://github.com/m5stack/M5-Schematic/blob/master/Core/IIC_IP5306_REG_V1.4.pdf)查看 IP5306 的寄存器手册。

| ESP32-D0WDQ6  | G22 | G21 | 5V  | GND |
| ------------- | --- | --- | --- | --- |
| GROVE A       | SCL | SDA | 5V  | GND |
| IP5306 (0x75) | SCL | SDA | 5V  | GND |

### IP5306 充 / 放电，电压参数

| 充电                | 放电                 |
| ------------------- | -------------------- |
| 0.00 ~ 3.40V -> 0%  | 4.20 ~ 4.07V -> 100% |
| 3.40 ~ 3.61V -> 25% | 4.07 ~ 3.81V -> 75%  |
| 3.61 ~ 3.88V -> 50% | 3.81 ~ 3.55V -> 50%  |
| 3.88 ~ 4.12V -> 75% | 3.55 ~ 3.33V -> 25%  |
| 4.12 ~ /-> 100%     | 3.33 ~ 0.00V -> 0%   |

### MPU6886

MPU6886 I2C address 0x68

| ESP32-D0WDQ6   | G22 | G21 | 5V  | GND |
| -------------- | --- | --- | --- | --- |
| MPU6886 (0x68) | SCL | SDA | 5V  | GND |

### BMM150 3 轴磁力计

BMM150 I2C address 0x10

| ESP32-D0WDQ6  | G22 | G21 | 5V  | GND |
| ------------- | --- | --- | --- | --- |
| BMM150 (0x10) | SCL | SDA | 5V  | GND |

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/gray/mpu6886_bmm150_axis.webp">

## M5GO 底座管脚

### LED 灯条 & 麦克风 & 扬声器

| ESP32-D0WDQ6 | G15     | G34     | G25         |
| ------------ | ------- | ------- | ----------- |
| 硬件         | SIG Pin | MIC Pin | Speaker Pin |

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

在使用 GPIO15 的 RGB LED 时，建议初始化引脚 pinMode (15，OUTPUT_OPEN_DRAIN)；
有关引脚分配和引脚重新映射的更多信息，请参考[ESP32 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)。

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/fire/module%20size.jpg" width="80%">

## 数据手册

- **Datasheet**

  - [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
  - [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
  - [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
  - [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)
  - [SH200Q](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SH200Q_en.pdf)
  - [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [Fire Arduino 快速上手](/zh_CN/arduino/m5fire/program)
- [Fire Arduino API](/zh_CN/arduino/m5core/button)
- [Fire Arduino 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Basics)

### UiFlow1

- [Fire UiFlow1 快速上手](/zh_CN/uiflow/m5fire/program)

### UiFlow2

- [Fire UiFlow2 快速上手](/zh_CN/uiflow2/m5fire/program)

### PlatformIO

```
[env:m5stack-fire]
platform = espressif32@6.12.0
board = m5stack-fire
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

### USB 驱动

\#> 点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader               | 下载链接                                                                                   | 备注 |
| ------------------------ | ------------------------------------------------------------------------------------------ | ---- |
| Fire 出厂固件 Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/656/Fire_Factory_Firmware.exe) | /    |

## 相关视频

**m5stack 的简介**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/m5stack%E7%AE%80%E4%BB%8B%EF%BC%88%E4%B8%AD%E6%96%87%EF%BC%89.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009380885079&bvid=BV1CFWSe8ExQ&p=1&autoplay=0" loading="lazy"  scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/19Me3u3n5mg?si=bNX2KL0n8KEERtW2" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/3Gfp4XLOH_o?si=FrwXJhYDbYSci92Z" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K007)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                                             | 备注：                                                               |
| -------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| 2020.4   | PSRAM 大小 4MB 变更为 8MB                            | /                                                                    |
| 2019.11  | 电池容量 600mAh 变更为 500mAh                        | /                                                                    |
| 2019.8   | SH200Q 变更为 MPU6886                                | /                                                                    |
| 2019.7   | MPU9250 变更为 SH200Q+BMM150、TN 屏幕变更为 IPS 屏幕 | 请将您的 M5Stack 库升级到最新版本(v0.2.8 以上)，以解决屏幕反色问题。 |
| 2018.6   | 首次发售                                             | /                                                                    |

!> 说明 |**2018.2A**PCB 版本的设备不支持 C2C (Type-C to Type-C) 连接及 PD 供电。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.6/basic_v2.6_2018.2a.webp" width="50%">
