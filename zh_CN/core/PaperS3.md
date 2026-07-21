# PaperS3

<span class="product-sku">SKU:C139</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/15.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139-main-pic_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139-main-pic_01.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139_Weight.jpg">
</PictureViewer>

## 描述

**PaperS3** 是 M5Stack 推出的一款极具特色的可触控低功耗墨水屏主控设备。控制器采用 **ESP32-S3** 。设备正面嵌入了一块分辨率为 **960 x 540 @ 4.7"** 的 （触摸和屏幕一体化） 电子墨水屏，支持 **16 级灰度显示**。搭配 **GT911** 电容式触控面板，能够支持两点触控以及多种手势操作。与之前的产品相比，PaperS3 采用了全面屏结构。相较于普通的 LCD 屏幕，电子墨水屏不仅能为用户带来更优质的文本阅读体验，还具有低功耗、掉电图像保持等优势特性。

在功能配置方面，它集成了 **陀螺仪传感器、板载蜂鸣器、物理按键** ，可以实现诸如抬起唤醒等互动操作以及开关机操作。在数据存储上，PaperS3 配备了 **microSD** 接口，并且 **ESP32-S3R8** 芯片自带 **8MB** 的 **PSRAM** 。此外，还外置了 **16MB** 的闪存芯片用于扩展存储，这既保证了更高的存储容量，又能实现更快的数据访问速度。

它内置了 **1800mAh** 锂电池且具备充电功能，结合内部的 **RTC（BM8563）** 可实现休眠与唤醒功能，为设备提供了强劲的续航能力。同时，设备板载的**电池检测电路**，能够实时监控电池状态，保障电池的健康管理。

设备背部开放了 **HC1.25-4PLT** 外设接口，可用于拓展各种各样的传感器设备，为后续的应用功能开发赋予了无限的可能性。并且还支持 **OTG 功能**，为外部设备的连接和数据交换提供了更多选择。

在性能优化上，相比之前的产品，PaperS3 在天线方面进行了优化增强，从而具备了更好的无线性能和信号稳定性。在设计上，配备了 **挂耳设计** ，方便用户携带和挂置，提升了产品的便捷性与实用性，而且整体设备更薄。另外，PaperS3 还具备 **磁吸功能** ，便于用户将设备固定在金属表面，进一步增强了设备使用的便捷性和灵活性。

PaperS3 适用于物联网监控、智能家居、环境监测、健康监测、电子标签、数据记录等多种低功耗显示和交互应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5papers3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 PaperS3 设备 |

learn>| ![UiFlow2](https://static-cdn.m5stack.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5papers3/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 PaperS3 设备 |

## 注意事项

!> 早期批次的 PaperS3 设备，其 USB 接口由于 QC3.0/2.0 协议的时序问题，可能会因 PD 产生的高电压而导致设备损坏。因此，请不要使用 QC3.0/2.0 充电器为 PaperS3 充电。而 v1.1/v1.2 或以上版本的设备则不存在该问题。

\#> PaperS3 结构背面为大面积平面出模工艺，因材质特性可能存在轻微自然弯曲现象，此属正常结构特征，并非电池问题，不影响产品功能与使用安全。

## 产品特性

- ESP32-S3R8 SoC
- 内置陀螺仪，蜂鸣器，物理按键
- 8MB PSRAM，16MB 外部闪存
- 4.7" 触控电子墨水屏 960×540 分辨率
- 背部磁吸
- 1800mAh 锂电池
- RTC 芯片 休眠唤醒
- 低功耗
- 开发平台：
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x PaperS3

## 应用场景

- 物联网监控
- 智能家居控制面板
- 电子标签
- 教育与学习工具

## 规格参数

| 规格     | 参数                                                                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC      | ESP32S3R8@Xtensa 32 位 LX7 双核处理器，主频 240MHz                                                                                                            |
| Flash    | 16MB                                                                                                                                                          |
| PSRAM    | 8MB Quad                                                                                                                                                      |
| Wi-Fi    | 2.4 GHz Wi-Fi                                                                                                                                                 |
| 存储     | 支持 microSD 卡扩展存储                                                                                                                                       |
| 显示屏   | 4.7" 触控电子墨水屏（全面屏）@EPD_ED047TC1<br/>分辨率：960x540 像素 <br/>16 级灰度显示                                                                        |
| 触摸功能 | 支持两点触控与多种手势操作（GT911 电容式触摸面板）                                                                                                            |
| 传感器   | 内置陀螺仪传感器 BMI270@通讯地址：0x68                                                                                                                        |
| USB 功能 | OTG/CDC/MSC/Firmware Flashing                                                                                                                                 |
| 电源输入 | 5V@500mA                                                                                                                                                      |
| 外设接口 | HC1.25-4PLT（3v3+GND+2xGPIO） 外设接口（用于扩展传感器和设备），规格：1 x 4P 1.25 间距                                                                        |
| 电池     | 3.7V@1800mAh 锂电池 @充电芯片：LGS4056H                                                                                                                       |
| 电池接口 | HY1.25-2P                                                                                                                                                     |
| 充电电流 | DC 5V@331.5mA                                                                                                                                                 |
| 电源管理 | PMS150G（开关机以及下载程序控制）<br/>内置 BM8563 RTC 芯片（支持休眠与唤醒功能）@通讯地址：0x51                                                               |
| 按键     | 1x 物理按键（用于设备控制，开关机，复位，下载模式）                                                                                                           |
| 蜂鸣器   | 板载无源蜂鸣器                                                                                                                                                |
| Wi-Fi    | 通讯距离 111 米（空旷地，天线与地面垂直 90°）                                                                                                                 |
| 功耗     | 低功耗模式：DC4.2V/9.28uA（主电源关闭，陀螺仪低功耗模式）<br/>待机模式：DC4.2V/949.58uA（主电源关闭，陀螺仪打开）<br/>工作模式：DC4.2V/154.02mA（主电源打开） |
| 工作温度 | 0 ~ 40°C                                                                                                                                                      |
| 产品尺寸 | 127.5 x 67.7 x 7.7mm                                                                                                                                          |
| 产品重量 | 89.0g                                                                                                                                                         |
| 包装尺寸 | 132.2 x 77.4 x 19.7mm                                                                                                                                         |
| 毛重     | 111.7g                                                                                                                                                        |

## 操作说明

### 开关机操作

单击侧面按键开机，双击侧面按键关机。

### 进入下载模式

将设备通过 USB 线连接至电脑，长按 M5PaperS3 上的电源按键，当背部状态灯红色闪烁时表示设备已进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/download.gif" width="30%" />

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/IMU-PaperS3.jpg" width="70%">

### 版本信息

PaperS3 v1.1、v1.2 及以上版本可通过产品背部贴纸查询版本信息；v1.0 版本的贴纸未印制版本信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/papers3-operate_01.png" width="30%" />

## 认证信息

- CE/FCC/MIC 认证

## 原理图

- [PaperS3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/sch_papers3_V1.0.pdf)

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/sch_papers3_V1.0_page_01.png" width="100%" />

## 管脚映射

### EPD_ED047TC1

| EPD_ED047TC1 | ESP32S3R8 |
| ------------ | --------- |
| DB0          | G6        |
| DB1          | G14       |
| DB2          | G7        |
| DB3          | G12       |
| DB4          | G9        |
| DB5          | G11       |
| DB6          | G8        |
| DB7          | G10       |
| XSTL         | G13       |
| XLE          | G15       |
| SPV          | G17       |
| CKV          | G18       |
| PWR          | G45       |

### GT911 & BM8563 & BMI270 & BAT_ADC & BUZZER

| ESP32S3R8      | G41 | G42 | G48 | PMS150GU06-PA6/CIN- | G3       | G21     |
| -------------- | --- | --- | --- | ------------------- | -------- | ------- |
| GT911          | SDA | SCL | INT |                     |          |         |
| BM8563         | SDA | SCL |     | INT                 |          |         |
| Battery Detech |     |     |     |                     | ADC_VBAT |         |
| Buzzer         |     |     |     |                     |          | BUZ_PWM |

### microSD

| microSD   | CS  | SCK | MOSI | MISO |
| --------- | --- | --- | ---- | ---- |
| ESP32S3R8 | G47 | G39 | G38  | G40  |

### USB 供电检测

| ESP32S3R8    | G5      |
| ------------ | ------- |
| USB 供电检测 | USB_DET |

### HC1.25-4PLT

::grove-table
| HC1.25-4PLT | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 3V3 | G1     | G2    |
::

## 尺寸图

[PaperS3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139_page_01.png" width="100%">

## 结构文件

- [PaperS3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C139_PaperS3/Structures)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)
- [GT911](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/m5paper/gt911_datasheet.pdf)
- [EPD_ED047TC1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139_ED047TC1_datasheet.pdf)

## 软件开发

\#>PaperS3 开发注意事项 | 1. 需要开启 PSRAM<br/>2. 需要设置 PSRAM 为 Octal 模式<br/>3. 需要依赖 EPDIY 库的最低版本为 2.0.0

### Arduino

- [PaperS3 Arduino 快速上手](/zh_CN/arduino/m5papers3/program)
- [PaperS3 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [PaperS3 Arduino M5GFX驱动库](https://github.com/m5stack/M5GFX)

### UiFlow2

- [PaperS3 UiFlow2 快速上手](/zh_CN/uiflow2/m5papers3/program)

### ESP-IDF

- [PaperS3 出厂固件](https://github.com/m5stack/M5PaperS3-UserDemo)

### PlatformIO

- PlatformIO 配置

```bash
[env:PaperS3]
platform = espressif32
board = esp32-s3-devkitm-1
framework = arduino
board_build.partitions = default_16MB.csv
board_upload.flash_size = 16MB
board_upload.maximum_size = 16777216
board_build.arduino.memory_type = qio_opi
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
lib_deps =
    epdiy=https://github.com/vroland/epdiy.git#d84d26ebebd780c4c9d4218d76fbe2727ee42b47
    M5Unified=https://github.com/m5stack/M5Unified
```

### Easyloader

| Easyloader       | 下载链接                                                                                                                      | 备注 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| PaperS3 出厂固件 | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/PaperS3%20Factory%20Firmware.exe) | /    |

## 相关视频

- PaperS3 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/papers3%20video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113791584962597&bvid=BV1RJrhYREWb&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/4WYvo21fSW4?si=GZWGwDjOocA8Wo1m" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare | [PaperS3](/zh_CN/core/PaperS3) ![PaperS3](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/12.webp) | [Paper](/zh_CN/core/m5paper_v1.1) ![Paper V1.1](https://static-cdn.m5stack.com/resource/docs/products/core/m5paper_v1.1/m5paper_v1.1_03.webp)                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 芯片方案        | ESP32-S3R8                                                                                                                          | ESP32-D0WDQ6-V3                                                                                                                                                   |
| 墨水屏控制方式  | ESP32S3R8 直接驱动                                                                                                                  | IT8951                                                                                                                                                            |
| 传感器          | BMI270，BM8563                                                                                                                      | BM8653                                                                                                                                                            |
| 屏幕            | 全面屏                                                                                                                              | 边框屏                                                                                                                                                            |
| 开关机方式      | 单击侧面按键开机，双击关机，下载模式：长按按键，背部右下角红灯闪烁即可进入下载模式。                                                | PWR 按键 (按下拨轮开关) 作为开机按键使用 (长按 2s)，如需要使设备关机，则需要通过软件 API 或是按下背部的复位按键实现。下载程序：安装驱动，识别端口之后方可下载程序 |
| 存储            | Flash:16MB PSRAM:8MB                                                                                                                | Flash:16MB PSRAM:8MB                                                                                                                                              |
| 电池            | 1800mAh                                                                                                                             | 1150mAh                                                                                                                                                           |
| 下载连接方式    | 直连 ESP32S3，自动识别端口                                                                                                          | CH9102 串口芯片                                                                                                                                                   |
| 天线            | 升级天线，信号更稳定                                                                                                                | 第一代天线                                                                                                                                                        |
| 尺寸            | 121.5 x 67.7 x 7.7mm                                                                                                                | 118 x 66 x 10mm                                                                                                                                                   |
::

如需对比 Paper / CoreInk 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5paper_compare?select=C139)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
