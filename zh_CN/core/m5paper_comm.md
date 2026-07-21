# Paper Comm Edition

<span class="product-sku">SKU:K049-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_07.webp">
</PictureViewer>

## 描述

**Paper Comm Edition** 是 M5Stack 推出的一款纪念版可触控墨水屏开发板，内置 **ESP32** 主控。正面嵌入了一块分辨率为 **540 x 960 @4.7"** 的电子墨水屏，**支持 16 级灰度显示**。搭配 **GT911 电容式触控面板**，支持**两点触控**与多种手势操作。相较于普通的 LCD 屏幕，电子墨水屏能够为用户提供更优质的文本阅读体验，同时具备**低功耗**、掉电图像保持等特性。

该开发板集成了**拨轮开关**、 **SHT30 温湿度传感器**与物理按键。在数据储存方面，预留了 **TF-card** （microSD） 接口，并集成了 **FM24C02** 储存芯片，提供 2K-bit （256x8）-EEPROM 用于用户数据的断电存储。

它内置了 1150mAh 锂电池，结合内部的 **RTC（BM8563）** 可实现休眠与唤醒功能，能够为设备提供强大的续航能力。此外，开放了 3 组 HY2.0-4P 外设接口，能够拓展各式各样的传感器设备，为后续的应用功能开发提供了无限可能。

## 注意事顶

- 请勿长时间暴露在紫外线下，否则有可能对墨水屏造成不可逆的损害。
- M5Paper 采用的低功耗电源管理方案与 CORE 与 StickC 设备有所不同，使用时，**PWR 按键**(按下拨轮开关) 作为**开机**按键使用 (**长按 2s**)，如需要使设备关机，则需要通过软件**API**或是按下背部的**复位按键**实现，当使用 USB 供电时，则无法关机。
- 在使用时，若出现无法正常下载程序（提示超时或者是 Failed to write to target RAM）的情况，可尝试重新安装设备驱动，驱动下载请查看文档下方内容。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5paper/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 M5Paper 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5paper/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 M5Paper 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5paper/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 M5Paper 设备 |

## 产品特性

- 内嵌 ESP32，支持 Wi-Fi
- 内置 16MB Flash
- E-Ink 低功耗显示面板
- 支持两点触控
- 近 180 度可视角
- 背面磁吸设计
- 内置 1150mAh 大容量锂电池
- HY2.0-4P 外设接口 x 3
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x M5Paper COMM Edition

## 应用场景

- 物联网控制器
- 电子书阅读器
- 工业仪器显示面板
- 电子标签

## 规格参数

| 主控资源   | 参数                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| SoC        | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                                                                                   |
| DMIPS      | 600                                                                                                                       |
| SRAM       | 520KB                                                                                                                     |
| Flash      | 16MB                                                                                                                      |
| PSRAM      | 8MB                                                                                                                       |
| Wi-Fi      | 2.4 GHz Wi-Fi                                                                                                             |
| 输入电压   | 5V@500mA                                                                                                                  |
| 接口       | USB Type-C x 1，HY2.0-4P x 3 ，TF-card (microSD) 卡槽                                                                     |
| 墨水屏     | 型号：EPD_ED047TC1 <br/> 540 x 960@4.7" <br/> 灰度 : 16 级 <br/> 显示区域 : 58.32 x 103.68mm <br/> 显示驱动芯片 : IT8951E |
| 物理按键   | 拨轮开关 \*1 ，复位按键 \*1                                                                                               |
| RTC        | BM8563                                                                                                                    |
| 触控       | GT911 电容式触控面板                                                                                                      |
| 天线       | 2.4G 3D 天线                                                                                                              |
| PIN 脚引出 | G25，G32，G26，G33，G18，G19                                                                                              |
| 电池       | 1150mAh@3.7V                                                                                                              |
| 工作温度   | 0 ~ 60°C                                                                                                                  |
| 产品尺寸   | 118.6 x 67.0 x 10.0mm                                                                                                     |
| 产品重量   | 86.0g                                                                                                                     |
| 包装尺寸   | 147.3 x 73.7 x 13.2mm                                                                                                     |
| 毛重       | 100.0g                                                                                                                    |

## 原理图

- [Paper Comm Edition 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/m5paper/M5_PAPER_SCH.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/688/M5_PAPER_SCH_page_07.png">
</SchViewer>

## 管脚映射

### 墨水屏幕 & TF-card (microSD)

屏幕像素：540 x 960

| ESP32-D0WDQ6-V3  | G13  | G12  | G14 | G15 | G4  |
| ---------------- | ---- | ---- | --- | --- | --- |
| IT8951E          | MISO | MOSI | SCK | CS  | /   |
| TF-card(microSD) | MISO | MOSI | SCK | /   | CS  |

### 拨轮开关

| ESP32-D0WDQ6-V3 | G37 | G38               | G39 | G2  |
| --------------- | --- | ----------------- | --- | --- |
| 拨轮开关        | 右  | 中按钮 / 电源按钮 | 左  | /   |
| 电源控制        | /   | /                 | /   | MOS |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3 | G21 | G22 | G36 |
| --------------- | --- | --- | --- |
| GT911           | SDA | SCL | INT |
| SHT30           | SDA | SCL | /   |
| BM8563          | SDA | SCL | /   |
| FM24C02         | SDA | SCL | /   |

### USB 转串口下载

| ESP32-D0WDQ6-V3 | G1  | G3  |
| --------------- | --- | --- |
| CH9102          | RXD | TXD |

#### ESP32 ADC/DAC 可映射引脚

| ADC1   | ADC2               | DAC1   | DAC2   |
| ------ | ------------------ | ------ | ------ |
| 8 通道 | 10 通道            | 2 通道 | 2 通道 |
| G32-39 | G0/2/4/12-15/25-27 | G25    | G26    |

有关引脚分配和引脚重新映射的更多信息，请参考[ESP32 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)。

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G25    | G32   |
| PORT.B   | GND   | 5V  | G26    | G33   |
| PORT.C   | GND   | 5V  | G18    | G19   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5paper_comm/module%20size%20comm.jpg" width="100%" />

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [SHT30 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY7088-Silergy.pdf)
- [GT911-datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/m5paper/gt911_datasheet.pdf)

## 软件开发

### Arduino

- [M5EPD_Todo](https://github.com/m5stack/M5EPD_Todo)

- [M5EPD_Calculator](https://github.com/m5stack/M5EPD_Calculator)

- [M5EPD_TTFExample](https://github.com/m5stack/M5EPD_TTFExample)

- [M5EPD Arduino 驱动库](https://github.com/m5stack/M5EPD)

- Arduino API & Examples

  - [touch](/zh_CN/arduino/m5paper/touch)
  - [epd_canvas](/zh_CN/arduino/m5paper/button)
  - [rtc](/zh_CN/arduino/m5paper/button)
  - [system_api](/zh_CN/arduino/m5paper/button)
  - [sht30](/zh_CN/arduino/m5paper/button)

- Tools
  - [image2gray tool](https://github.com/m5stack/M5EPD/tree/main/tools)

> 在使用 FactoryTest 加载特殊字符 (如中文，日文) 时，请向 TF 卡根目录放入字体文件，并命名为**font.ttf**。[ttf 文件下载地址](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/example/Font.ttf)

### UiFlow1

- [Paper UiFlow1 快速上手](/zh_CN/uiflow/m5paper/program)

### UiFlow2

- [Paper UiFlow2 快速上手](/zh_CN/uiflow2/m5paper/program)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者是 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

- **Windows**

| Easyloader  | 下载链接                                                                                                            | 备注 |
| ----------- | ------------------------------------------------------------------------------------------------------------------- | ---- |
| FactoryTest | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Paper_FactoryTest.exe) | /    |
| ToDo        | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Paper_Todo.exe)        |
| Calculator  | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Paper_Calculator.exe)  |

- **MacOS**

| Easyloader  | 下载链接                                                                                                          | 备注 |
| ----------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| FactoryTest | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/MacOS/CORE/EasyLoader_M5Paper_FactoryTest.dmg) | /    |
| ToDo        | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/MacOS/CORE/EasyLoader_M5Paper_Todo.dmg)        |
| Calculator  | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/MacOS/CORE/EasyLoader_M5Paper_Calculator.dmg)  |

### 其他

- [Paper 恢复出厂固件教程](https://github.com/m5stack/M5Paper_FactoryTest)

## 相关视频

- 产品介绍

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5PAPER.mp4" type="video/mp4">
</video>

- Paper 背板拆解教程

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/paper_open_shell.mp4" type="video/mp4">
</video>

## 产品对比

相对于前两代 M5Paper 产品，该纪念版采用了第一代电子墨水屏面板（显示效果上会更加柔和），白色外壳更换为更具特色的黑色透明外壳，实拍对比效果如下图所示。

<img class="pic" src="https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_comm/m5paper_comm_04.webp" width="100%">

### 版本区分

| 版本               | 外壳颜色 | 电子墨水屏                   |
| ------------------ | -------- | ---------------------------- |
| Paper Comm Edition | 黑色透明 | 第一代电子墨水屏硬性面板     |
| M5Paper            | 白色     | 第二代电子墨水屏硬性显示面板 |
| M5Paper v1.1       | 白色     | 第三代电子墨水屏柔性显示面板 |
