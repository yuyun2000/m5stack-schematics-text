# StickC

<span class="product-sku">SKU:K016-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_03.webp">
</PictureViewer>

## 描述

**StickC** 是一款精致小巧的开发板。作为 Stick 的升级版本，它增设了更多的拓展接口与按键，不仅具备出色的性能，还拥有低功耗的特性。无论是用于编程学习，还是开展项目开发，StickC 都能提供可靠的硬件支撑。

它能实现哪些功能呢？这个小巧精致的开发工具，能够充分激发无限的创作潜能。StickC 有助于快速搭建物联网产品原型，极大地简化整个开发流程。即便对于刚接触编程开发的初学者而言，也能够借助它搭建出一些饶有趣味的应用，并将其应用到实际生活当中。

StickC 是 M5Stack 产品系列中的核心设备之一，该产品系列构建于不断发展的硬件和软件生态系统之上。它拥有众多兼容的拓展功能模块、丰富的开源代码以及活跃的论坛社区，这些资源能够在开发过程中为使用者提供全方位的优质服务。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5stickc/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 StickC 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5stickc/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 StickC 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stickc/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 StickC 设备。 |

## 产品特性

- 基于 ESP32 开发
- 内置 3 轴加速计与 3 轴陀螺仪
- 内置 Red LED
- 集成红外发射管
- 内置 RTC
- 集成麦克风
- 用户按键，LCD (0.96 寸)，电源 / 复位按键
- 95 mAh 锂电池
- 拓展接口
- 可穿戴 & 可固定
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x StickC
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 可穿戴设备
- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备

## 规格参数

| 主控资源 | 参数                                           |
| -------- | ---------------------------------------------- |
| SoC      | ESP32-PICO-D4@双核处理器，主频 240MHz          |
| Flash    | 4MB                                            |
| Wi-Fi    | 2.4 GHz Wi-Fi                                  |
| DMIPS    | 600                                            |
| SRAM     | 520KB                                          |
| 输入电压 | 5V@500mA                                       |
| 接口     | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1       |
| LCD 屏幕 | 0.96 inch，80 x 160 Colorful TFT LCD，ST7735SV |
| 麦克风   | SPM1423                                        |
| 按键     | 自定义按键 x 2                                 |
| LED      | 红色 LED x 1                                   |
| RTC      | BM8563                                         |
| PMU      | AXP192                                         |
| IR       | Infrared transmission                          |
| MEMS     | MPU6886                                        |
| 天线     | 2.4G 3D 天线                                   |
| PIN 接口 | G0，G26，G36                                   |
| 电池     | 95 mAh @ 3.7V，inside vb                       |
| 工作温度 | 0 ~ 60°C                                       |
| 外壳材质 | Plastic ( PC )                                 |
| 产品尺寸 | 48.2 x 25.5 x 13.7mm                           |
| 产品重量 | 15.1g                                          |
| 包装尺寸 | 55.0 x 55.0 x 20.0mm                           |
| 毛重     | 33.0g                                          |

## 操作说明

### 开关机操作

- 开机：按复位按键，持续至少 2 秒
- 关机：按复位按键，持续至少 6 秒

**注意：**

- M5StickC 支持的波特率： 1200 ~115200，250K，500K，750K，1500K
- VBUS_VIN 与 VBUS_USB 的输入范围限制在 4.8-5.5V，VBUS 供电时将通过 AXP192 电源管理为内置电池进行充电。

## 原理图

- [StickC 原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/M5StickC/20191118__StickC_A04_3110_Schematic_Rebuild_PinMap.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/670/SCHE_StickC_page_01.png">

**电源结构框图**

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_04.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_05.webp" width="30%">

## 管脚映射

### 红色 LED & 红外发射管 IR & 按键 BUTTON

| ESP32-PICO-D4 | G10      | G9         | G37      | G39      |
| ------------- | -------- | ---------- | -------- | -------- |
| 红色 LED      | LED 管脚 |            |          |          |
| 红外发射管 IR |          | 发射管引脚 |          |          |
| 按键 BUTTON A |          |            | 按键管脚 |          |
| 按键 BUTTON B |          |            |          | 按键管脚 |

### 彩色 TFT 屏幕

驱动芯片：ST7735S

分辨率：80 x 160

| ESP32-PICO-D4 | G15      | G13     | G23    | G18     | G5     |
| ------------- | -------- | ------- | ------ | ------- | ------ |
| TFT 屏幕      | TFT_MOSI | TFT_CLK | TFT_DC | TFT_RST | TFT_CS |

### 麦克风 MIC (SPM1423)

| ESP32-PICO-D4 | G0  | G34  |
| ------------- | --- | ---- |
| 麦克风 MIC    | CLK | DATA |

### 六轴 IMU (SH200Q/MPU6886) & AXP192 & RTC (BM8563)

| ESP32-PICO-D4 | G21 | G22 | G35 |
| ------------- | --- | --- | --- |
| AXP192        | SDA | SCL | IRQ |
| MPU6886       | SDA | SCL | IRQ |
| BM8563        | SDA | SCL | IRQ |

### 电源管理芯片 (AXP192)

| Microphone | RTC  | TFT backlight | TFT IC | ESP32/3.3V MPU6886/SH200Q | 5V GROVE |
| ---------- | ---- | ------------- | ------ | ------------------------- | -------- |
| LDOio0     | LDO1 | LDO2          | LDO3   | DC-DC1                    | IPSOUT   |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G32    | G33   |
::

**充电电流测量值**

| 充电电流 | 充满后电流 (关机) | 充满电 (开机) |
| -------- | ----------------- | ------------- |
| 0.488A   | 0.066A            | 0.181A        |

## 结构文件

- [StickC 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K016-C_StickC/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [ST7735SV](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7735SV_V1.3.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [SH200Q](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SH200Q_en.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [StickC Arduino 快速上手](/zh_CN/arduino/m5stickc/program)
- [StickC Arduino 驱动库](https://github.com/m5stack/M5StickC)

### UiFlow1

- [StickC UiFlow1 快速上手](/zh_CN/uiflow/m5stickc/program)

### UiFlow2

- [StickC UiFlow2 快速上手](/zh_CN/uiflow2/m5stickc/program)

### USB 驱动

?> 波特率限制 | 在进行设备程序下载操作时，推荐选用以下串口波特率选项。若采用其他速度，可能导致程序无法正常下载。<br/>**1500000 bps** / **750000 bps** / **500000 bps** / **250000 bps** / **115200 bps**

将设备连接至 PC，打开设备管理器为设备安装[FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装（自定义更新），可执行文件安装方式可能无法正常工作)。[点击此处，前往下载 FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

### Easyloader

| Easyloader                 | 下载链接                                                                                                             | 备注 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---- |
| StickC Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5StickC_FactoryTest.exe) | /    |

## 相关视频

- 加速计，麦克风，LED，IR，RTC，无线连接等硬件测试，单击 A 键或 B 键可切换测试项。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5StickC.mp4" type="video/mp4">
</video>

- **M5StickC 的案例 - 自动贩卖机**

<video width="500" height="315" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201904/M5StickC%20Slot%20machine%20demo.mp4" type="video/mp4">
</video>

- 智能设备通过 StickC 进行验证，连接至公共 Wi-Fi

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5stickc_plus/%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87%E9%80%9A%E8%BF%87M5Stack%20StickC%E5%85%AC%E5%85%B1Wi-Fi%E8%BF%9E%E6%8E%A5-en.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1055479573&bvid=BV17n4y197jg&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/mcZHoT0x6UE?si=-QH1cCDGYzXved9L" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Stick 系列产品信息，可访问[产品选型表](/en/products_selector/m5stick_compare?select=K016-C)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                    |
| -------- | --------------------------- |
| 2020.3   | 电池容量 80mAh 变更为 95mAh |
| 2019.10  | 升级底部，添加铜螺母        |
| 2019.8   | SH200Q 变更为 MPU6886       |
| 2019.3   | 首次发售                    |