# Basic v2.7

<span class="product-sku">SKU:K001-V27</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.7/basic_v2.7_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.7/basic_v2.7_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/654/K001-V27_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.7/basic_v2.7_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/654/K001-V27_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/654/K001-V27-weight.jpg">
</PictureViewer>

## 描述

**Basic v2.7** 是一款高性价比的物联网入门级主控。采用乐鑫 **ESP32** 芯片，搭载 2 个低功耗 **Xtensa® 32-bit LX6** 微处理器，主频高达 **240 MHz** 。板载 **16 MB Flash** 内存组合，集成 **2.0 英寸全彩高清 IPS 显示面板**、**扬声器**、**TFCard 槽**等外设。全覆盖外壳，即便是在复杂的工业应用场景也能够保障电路运行的稳定性。内部总线提供多种常用接口资源 (ADC/DAC/I2C/UART/SPI 等) ，底部总线 15 x IO 引出，可拓展性强。适用于各种产品原型研发、工业控制、智能楼宇应用场景。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core/program) | 本教程介绍如何通过 UiFlow1 图形化编程平台控制 Basic 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Basic 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Basic 设备。 |

## 产品特性

- 基于 ESP32 开发
- 2.0 英寸 IPS 显示面板、扬声器、自定义按键 \*3
- 内置锂电池供电、集成电源管理芯片，支持 Type-C 接口
- 16M Flash
- 15x IO 引出
- 集成全彩高清 IPS 显示面板与多种硬件外设
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Basic v2.7
- 10 x 杜邦线
- 1 x USB Type-C 连接线 (20cm)
- 1 x 使用手册

## 应用场景

- 物联网控制器
- 创客 DIY 作品
- 智能家居控制

## 规格参数

| 规格     | 参数                                                                  |
| -------- | --------------------------------------------------------------------- |
| SoC      | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                               |
| DMIPS    | 600                                                                   |
| SRAM     | 520KB                                                                 |
| Flash    | 16MB                                                                  |
| Wi-Fi    | 2.4 GHz Wi-Fi                                                         |
| 输入电源 | 5V@500mA                                                              |
| 接口     | USB Type-C x1，I2C x1                                                 |
| IO       | G21，G22，G23，G19，G18，G3，G1，G16，G17，G2，G5，G25，G26，G35，G36 |
| 按键     | 物理按键 x 3                                                          |
| LCD 屏幕 | 2.0"@320 x 240 ILI9342C IPS 面板，最高亮度 853nit                     |
| 扬声器   | 1W-0928                                                               |
| USB 芯片 | CH9102F                                                               |
| 天线     | 2.4G 3D 天线                                                          |
| 电池     | 110mAh @ 3.7V                                                         |
| 外壳材质 | Plastic (PC)                                                          |
| 产品尺寸 | 54.0 x 54.0 x 17.0mm                                                  |
| 产品重量 | 49.4g                                                                 |
| 包装尺寸 | 88.0 x 56.0 x 22.0mm                                                  |
| 毛重     | 76.0g                                                                 |

## 操作说明

### 开关机操作

- 开机：底部开关波动至**1**，单击左侧红色电源键
- 关机：在无 USB 供电的情况下，快速双击左侧红色电源键，或者将底部的开关拨动至**0**。

?> 注意 | 默认情况下，USB 供电时，无法进行关机。

## 原理图

- [Basic v2.7 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206.pdf)

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
| ILI9342C        | MOSI/MISO |      | CLK | CS  | DC  | RST | BL  |     |
| TF Card         | MOSI      | MISO | CLK |     |     |     |     | CS  |

### 按键 & 喇叭

| ESP32-D0WDQ6-V3 | G39      | G38      | G37      | G25      |
| --------------- | -------- | -------- | -------- | -------- |
| 按键引脚        | BUTTON A | BUTTON B | BUTTON C |          |
| 喇叭            |          |          |          | 喇叭引脚 |

### GROVE 接口 A & IP5306

电源管理芯片 (IP5306) 是定制 I2C 版本，它的 I2C 地址是 0x75. 点击[这里](https://github.com/m5stack/M5-Schematic/blob/master/Core/IIC_IP5306_REG_V1.4.pdf)查看 IP5306 的寄存器手册。

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

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/BASIC%20v2.6/module%20size.jpg" width="100%" />

## 结构文件

- [Basic v2.7 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K001-V27_Basic_v2.7/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [Basic v2.7 Arduino 快速上手](/zh_CN/arduino/m5core/program)
- [Basic v2.7 Arduino 驱动库](https://github.com/m5stack/M5Stack/tree/master/examples/Basics)
- [Basic v2.7 Arduino API](/zh_CN/arduino/m5core/button)

### UiFlow1

- [Basic v2.7 UiFlow1 快速上手](/zh_CN/uiflow/m5core/program)

### UiFlow2

- [Basic v2.7 UiFlow2 快速上手](/zh_CN/uiflow2/m5core/program)

### PlatformIO

```bash
[env:m5stack-core]
platform = espressif32@6.7.0
board = m5stack-core-esp32
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP34X（适用于**CH9102**）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                 | 下载链接                                                                                                           | 备注 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Basic v2.7 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Core_FactoryTest.exe) | /    |

## 相关视频

- 喇叭，Wi-Fi，按键，加速计，TF-card (microSD) 卡，屏幕等硬件运行测试。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/BASIC.mp4" type="video/mp4">
</video>

**M5Stack 的简介**

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/m5stack%E7%AE%80%E4%BB%8B%EF%BC%88%E4%B8%AD%E6%96%87%EF%BC%89.mp4" type="video/mp4">
</video>

- 将传感器连接到 EzData 组建智能家居

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/basic_v2.7/%E5%B0%86%E4%BC%A0%E6%84%9F%E5%99%A8%E8%BF%9E%E6%8E%A5%E5%88%B0EzData%E7%BB%84%E5%BB%BA%E6%99%BA%E8%83%BD%E5%AE%B6%E5%B1%85.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009229957638&bvid=BV1NdWUePEbD&p=1&autoplay=0" loading="lazy"  scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/N7tFjTKBu-I?si=yZk7DfIQd-7leFl6" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K001-V27)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/basic_v2.7/compare.webp"  width="60%" height="36%">

## 版本变更

| 上市日期 | 产品变动                                                   | 备注                                                                                               |
| -------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 2023.4   | 升级 v2.7 版本                                             | 屏幕改为玻璃屏，显示更清晰，Grove 口增加了升压功能，稳定 5.1v 输出，带负载更稳定；增加电池供电开关 |
| 2021.10  | 升级为 v2.6，改变 CP2104 为 CH9102，优化结构细节 (Core2.6) | /                                                                                                  |
| 2020.6   | Flash 大小由 4MB 变更为 16MB (Core2.5)                     | /                                                                                                  |
| 2020.3   | 电池容量 150mAh 变更为 110mAh (Core2.4)                    | /                                                                                                  |
| 2019.7   | TN 屏幕变更为 IPS 屏幕 (Core2.2)                           | 请将您的 M5Stack 库升级到最新版本 (v0.2.8 以上)，以解决屏幕反色问题                                |
| 2017.7   | 首次发售 (Core1.4)                                         | /                                                                                                  |

\#> 注意 |**2018.2A**PCB 版本的设备不支持 C2C (Type-C to Type-C) 连接及 PD 供电。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.6/basic_v2.6_2018.2a.webp" width="50%">
