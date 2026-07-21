# Air Quality v1.1

<span class="product-sku">SKU:K131-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_12.jpg">
</PictureViewer>

## 描述

Air Quality v1.1 是一款一体化低功耗空气质量监测装置。相对上一代，新版产品采用 Stamp-S3A 主控，在整机功耗与 Wi-Fi 天线上都进行优化提升。
设备配备 1.54 寸墨水屏，分辨率为 200 x 200 。内置多功能空气质量传感器 SEN55 和 CO2 传感器 SCD40，能监测空气中的 PM1.0、PM2.5、PM4、PM10 颗粒物、温度、湿度、VOC 和 CO2 浓度。内置 600mAh 锂电池及 RTC 低功耗电源管理电路，能实现休眠及定时唤醒。出厂固件支持上传空气质量数据至 M5Stack Ezdata 云平台，为用户提供便捷的远程云端数据查看功能。底部结构提供 LEGO 兼容安装孔、吸附磁铁和 4 个插拔式挂耳，支持多种固定方式。适用于家庭、学校、工业现场、医学环境的等环境的空气监测。

## 教程 & 快速上手

learn>| ![快速上手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_10.jpg) | [快速上手](/zh_CN/guide/iot_tools/air_quality/usage) | 介绍 Air Quality v1.1 的使用教程。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5air_quality/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Air Quality v1.1 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/airq/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Air Quality v1.1 设备。 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/kit/air_quality_v1.1) | 本教程介绍如何将 Air Quality V1.1 添加至 Home Assistant。 |

## 产品特性

- Stamp-S3A 主控
- SEN55 和 SCD40 传感器
- 1.54 寸墨水屏 (分辨率 200 x 200)
- 内置 600mAh 锂电池
- HY2.0-4P 接口
- EZDATA 云平台访问
- RTC 定时唤醒
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Air Quality v1.1
- 1 x 操作说明书

## 应用场景

- 家庭环境监测
- 工业自动化
- 医疗场所
- 科研实验室
- 远程监测应用
- 空调系统优化
- 建筑工地

## 规格参数

| 规格         | 参数                                                        |
| ------------ | ----------------------------------------------------------- |
| SoC          | ESP32-S3FN8 @双核 Xtensa LX7 处理器                         |
| Flash        | 8MB                                                         |
| 显示屏       | GDEY0154D67@1.54"                                           |
| 分辨率       | 200 x 200px                                                 |
| SEN55        | I2C 地址：0x69                                              |
| SCD40        | I2C 地址：0x62                                              |
| 环境检测类型 | PM1.0、PM2.5、PM4、PM10 颗粒物、温度、湿度、VOC 和 CO2 浓度 |
| RTC          | RTC8563                                                     |
| 电池         | 600mAh@3.7V                                                 |
| 按键         | 按键 A，按键 B，开机按键，复位与关机                        |
| Grove 接口   | HY2.0-4P                                                    |
| 蜂鸣器       | 板载无源蜂鸣器                                              |
| 固定结构     | 乐高安装孔、吸附磁铁和 4 个 M3 插拔式挂耳                   |
| 工作温度     | 0 ~ 40°C                                                    |
| 产品尺寸     | 72.0 x 56.0 x 26.5mm                                        |
| 产品重量     | 91.4g                                                       |
| 包装尺寸     | 100.0 x 73.0 x 32.0mm                                       |
| 毛重         | 120.0g                                                      |

## 操作说明

### 开关机操作

- 开机：可通过按 "WAKE" 按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G46) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入休眠状态。

  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/K131-V11_Air_Quality_01.jpg" width="50%" />

- 关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD (GPIO46)=0，即实现断电关机。

  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/K131-V11_Air_Quality_02.jpg" width="50%" />

### 进入下载模式

如果要进入下载模式，请在先关机，然后按住 Stamp-S3A 上的 BooT 按键或 Air Quality v1.1 上 G0 键的同时插入 USB，通电之后再松开。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/AirQ_v1.1_operation.gif" width="50%" />

### 使用手册

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/K131-V11_Air_Quality_Monitor_v1.1_User_Manual_ZH.png" width="100%" />

## 原理图

- [Air Quality v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0.pdf)
- [Stamp-S3A 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png">
</SchViewer>

## 管脚映射

### 电源控制

| ESP32-S3           | G10      | G46  | G42  | G14 |
| ------------------ | -------- | ---- | ---- | --- |
| SEN55 POWER SWITCH | AirPWREN |      |      |     |
| HOLD               |          | HOLD |      |     |
| WAKE               |          |      | WAKE |     |
| BATTERY DETECT     |          |      |      | G14 |

### 显示屏

| ESP32-S3    | G1   | G2  | G3  | G4  | G5  | G6   |
| ----------- | ---- | --- | --- | --- | --- | ---- |
| GDEY0154D67 | BUSY | RST | D/C | CS  | SCK | MOSI |

### 输入交互

| ESP32-S3 | G9   | G0     | G8     |
| -------- | ---- | ------ | ------ |
| BEEP     | beep |        |        |
| BUTTON A |      | USER_A |        |
| BUTTON B |      |        | USER_B |

### 传感器

| ESP32-S3 | G11 | G12 |
| -------- | --- | --- |
| SEN55    | SDA | SCL |
| SCD40    | SDA | SCL |
| RTC8563  | SDA | SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G13    | G15   |
::

## 尺寸图

- [Air Quality v1.1模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/AIRQ-00.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/AIRQ-K131-V11_page_01.png" width="100%">

## 结构文件

- [Air Quality v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K131-V11_Air_Quality_v1.1/Structures)

## 数据手册

- [SEN55 Datasheet](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf-9e2861345ac4a2cd640cc28e0e2d2a07.pdf)
- [SCD40 Datasheet](https://static-cdn.m5stack.com/resource/docs/datasheet/unit/co2/SCD40.pdf)
- [GDEY0154D67 Datasheet](<https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/GDEY0154D67(1).pdf>)

## 软件开发

### Arduino

- [Air Quality v1.1 Arduino 快速上手](/zh_CN/arduino/m5air_quality/program)
- [Air Quality v1.1 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [Air Quality v1.1 Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)

### UiFlow2

- [Air Quality v1.1 UiFlow2 快速上手](/zh_CN/uiflow2/airq/program)

### PlatformIO

- [Air Quality v1.1 出厂固件](https://github.com/m5stack/AirQUserDemo)

```bash
[env:m5stack-stamp-s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1

lib_deps =
    https://github.com/m5stack/M5Unified.git#develop
    https://github.com/m5stack/M5GFX.git#develop
    sensirion/Sensirion I2C SEN5X@^0.3.0
    sensirion/Sensirion I2C SCD4x@^0.4.0
    tanakamasayuki/I2C BM8563 RTC@^1.0.4
    mathertel/OneButton@^2.0.3
    bblanchon/ArduinoJson @ ^6.21.3
```

### Easyloader

| Easyloader                 | 下载链接                                                                                                                      | 备注 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| Air Quality v1.1 User Demo | [download](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/ezLoader-4d75c8e2-f671-4d2a-bb1d-9f8b7fea5da8.exe) | /    |

### 其他

- [Air Quality v1.1 恢复出厂固件](/zh_CN/guide/restore_factory/air_quality)

?> 恢复出厂固件 | 若 Air Quality v1.1 设备先前烧录了 UiFlow 固件并进行了用户绑定，请在重新烧录 Air Quality v1.1 出厂固件前，在 UiFlow2 设备列表中对设备进行解绑，否则出厂固件运行时，数据可能无法正常上传至 Ezdata。

## 相关视频

- Air Quality 产品功能介绍

<video class="video-container" controls><source src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/K131%20AirQ%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1355860383&bvid=BV1mz421B7M9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/DkgFmuna7PM?si=oedpEcYs8zJLHzbw" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表     | [Air Quality v1.1](/zh_CN/core/Air_Quality_v1.1) ![Air Quality v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air_Quality_02.webp) | [Air Quality](/zh_CN/core/Air_Quality) ![Air Quality](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-5e0c9a17-efe3-46af-8322-c6f7c143fc2c.webp) |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------           | -------------------------------------------------------------------------------------------------------------------------------------------------------------        |
| 核心模组       | Stamp-S3A                                                                                                                                       | Stamp-S3                                                                                                                                                             |
| 天线设计       | 优化天线设计，信号接收更佳                                                                                                                      | 常规天线设计                                                                                                                                                         |
| 模组 Boot 按键 | 优化按键手感，按键采用 4.0 x 3.0 x 2.0mm 规格                                                                                                   | 按键规格 2.6 x 1.6 x 0.55mm                                                                                                                                          |
::
