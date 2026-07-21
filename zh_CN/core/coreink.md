# CoreInk

<span class="product-sku">SKU:K048</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/K048-weight.jpg">
</PictureViewer>

## 描述

**CoreInk** 是 M5Stack 推出的一款带有电子墨水屏（E-Ink）的主控设备，控制器采用 ESP32-PICO-D4。正面嵌入了一块分辨率为 200x200 @ 1.54" 的电子墨水屏，支持黑 / 白显示。相对于普通的 LCD 的屏幕，电子墨水屏能够提供用户更好的文本阅读体验，同时具有低功耗，掉电图像保持等特性。人机交互方面提供了拨轮开关，与物理按键，集成 LED 指示灯与蜂鸣器。内置了 390mAh 锂电池，结合内部的 RTC (BM8563) 可实现定时休眠与唤醒功能，能够为设备提供较为优秀的续航能力。在机身的左侧和底部配有独立的电源按键与复位 (RST) 按键，方便使用与调试。开放了丰富的外设接口 (HY2.0-4P，M5-Bus，HAT 模块接口) 能够拓展各式各样的传感器设备，为后续的应用功能开发提供无限可能。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5coreink/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 CoreInk 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5coreink/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 CoreInk 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5coreink/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 CoreInk 设备。 |

### 注意事项

使用时请注意避免长时间高频刷新，建议刷新间隔为 (15s / 次)，请勿长时间暴露在紫外线下，否则有可能对墨水屏造成不可逆的损害。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_note_01.webp" width="30%">

## 产品特性

- 基于 ESP32 开发，支持 Wi-Fi
- 内置 4M Flash
- 低功耗显示面板
- 近 180 度可视角
- 人机交互接口
- 背面磁吸设计
- 内置锂电池
- 丰富的拓展接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x CoreInk

## 应用场景

- 物联网控制器
- 电子书阅读器
- 工业仪器显示面板
- 电子标签

## 规格参数

| 规格       | 参数                                                                                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC        | ESP32-PICO-D4@双核处理器，主频 240MHz                                                                                                                                  |
| DMIPS      | 600                                                                                                                                                                    |
| SRAM       | 520KB                                                                                                                                                                  |
| Flash      | 4MB                                                                                                                                                                    |
| Wi-Fi      | 2.4 GHz Wi-Fi                                                                                                                                                          |
| 输入电压   | 5V @ 500mA                                                                                                                                                             |
| 接口       | USB Type-C x 1，HY2.0-4P x 1 ，M5-Bus 总线母座，顶部 HAT 拓展接口                                                                                                      |
| 墨水屏     | GDEW0154M09, SPI 接口，200 x 200@1.54", Dpi:184 , 1-bit 黑 / 白显示 (灰阶：2) 视域尺寸 (mm):27.6x27.6 , 点间距 (mm) 0.138x0.138, 刷新时间 (s) 0.82 , 局刷时间 (s) 0.24 |
| 物理按键   | 可编程按键 x1 ，复位按键 x1，电源按键 x1                                                                                                                               |
| LED        | 绿色 LED x 1                                                                                                                                                           |
| RTC        | BM8563                                                                                                                                                                 |
| 蜂鸣器     | 无源蜂鸣器 \* 1                                                                                                                                                        |
| 天线       | 2.4G 3D 天线                                                                                                                                                           |
| PIN 脚引出 | G25，G26，G36，G23，G34，G18，G21，G22，G14，G13                                                                                                                       |
| 电池       | 390mAh@3.7V                                                                                                                                                            |
| 工作温度   | 0 ~ 60°C                                                                                                                                                               |
| 外壳材质   | Plastic ( PC )                                                                                                                                                         |
| 产品尺寸   | 56.0 x 40.0 x 16.0mm                                                                                                                                                   |
| 产品重量   | 31.5g                                                                                                                                                                  |
| 包装尺寸   | 80.0 x 45.0 x 20.0mm                                                                                                                                                   |
| 毛重       | 42.6g                                                                                                                                                                  |

## 操作说明

### 开关机说明

- 长按 PWR 按键 2 秒开机

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/coreink-operate_01.gif" width="30%">

- 设备关机需通过软件 API 控制或是按下背部的复位按键。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/coreink-operate_02.gif" width="30%">

## 原理图

- [CoreInk 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/coreink/coreink_sch.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/coreink_sch_page_01.png" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_sch_01.webp" width="80%">
</SchViewer>

## 管脚映射

### 墨水屏幕

屏幕像素：200x200

| ESP32-PICO-D4 | G4   | G0  | G15 | G9  | G18 | G23  |
| ------------- | ---- | --- | --- | --- | --- | ---- |
| GDEW0154M09   | BUSY | RST | D/C | CS  | SCK | MOSI |

### 拨轮开关 & 物理按键

| ESP32-PICO-D4   | G37    | G38    | G39    | G5       |
| --------------- | ------ | ------ | ------ | -------- |
| 拨轮开关 & 按键 | 拨轮上 | 拨轮中 | 拨轮下 | 用户按键 |

### LED & 蜂鸣器

| ESP32-PICO-D4 | G10 | G2     |
| ------------- | --- | ------ |
| LED           | LED | /      |
| 蜂鸣器        | /   | 蜂鸣器 |

### 电源控制

| ESP32-PICO-D4 | G12  |
| ------------- | ---- |
| 电源控制      | HOLD |

### RTC

| ESP32-PICO-D4 | G21 | G22 |
| ------------- | --- | --- |
| BM8563        | SDA | SCL |

### USB to TTL

| ESP32-PICO-D4 | G1  | G3  |
| ------------- | --- | --- |
| CP2104        | RXD | TXD |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G32    | G33   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/coreink/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="80%">

## 结构文件

- [CoreInk 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K048_CoreInk/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY7088-Silergy.pdf)
- [GDEW0154M09](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/CoreInk-K048-GDEW0154M09%20V2.0%20Specification.pdf)

## 软件开发

### Arduino

- [CoreInk Arduino 快速上手](/zh_CN/arduino/m5coreink/program)
- [CoreInk Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [CoreInk Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)
- [CoreInk 出厂测试](https://github.com/m5stack/M5Core-Ink/tree/master/examples/Basics/FactoryTest)

### UiFlow1

- [CoreInk UiFlow1 快速上手](/zh_CN/uiflow/m5coreink/program)

### UiFlow2

- [CoreInk UiFlow2 快速上手](/zh_CN/uiflow2/m5coreink/program)

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

| Easyloader                             | 下载链接                                                                                                   | 备注 |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| CoreInk Factory Test Easyloader v1.0.1 | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/687/Easyloader_CoreInk_FactoryTest_v1.0.1.exe) | /    |

## 相关视频

演示 CoreInk 的一些基本特性。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/CoreInk.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009397663711&bvid=BV1CfWUecEXd&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sj-mXNTW_GE?si=iY477W-ciB49wXwB" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Paper / CoreInk 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5paper_compare?select=K048)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
