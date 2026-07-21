# AtomS3

<span class="product-sku">SKU:C123</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/6.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/C123-PACKAEG.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/5.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/C123-weight.jpg">
</PictureViewer>

## 描述

**AtomS3** 是一款基于 **ESP32-S3** 主控的高集成度可编程控制器，内部集成了 ESP32-S3 主控，集成 **Wi-Fi** 功能、8 MB 片上 Flash、**0.85** 寸 **IPS 屏幕**。屏幕下方具有**可编程按键功能**，内置 5V 转 3.3V 电路、6 轴陀螺仪传感器 **MPU6886** 。板载 **USB Type-C** 接口，用于供电及固件下载，还有一个 **HY2.0-4P** 扩展端口 。底部预留 6 个 **GPIO 以及电源引脚**，方便扩展应用。产品大小为 24.0 x 24.0 x 13.0mm，适用于各种**嵌入式**的智能设备应用。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atoms3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 AtomS3 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atoms3/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomS3 设备。 |

## 产品特性

- 基于 ESP32-S3FN8 开发
- 自带 USB 下载功能
- 内置 3 轴陀螺仪和 3 轴加速计 (MPU6886)(I2CAddress: 0x68)
- 可编程按键
- 0.85 寸 LCD 屏幕
- 红外发射功能
- 可扩展的引脚与接口
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3

## 应用场景

- 物联网节点
- 微型控制器

## 规格参数

| 规格         | 参数                       |
| ------------ | -------------------------- |
| SoC          | ESP32-S3FN8                |
| Flash        | 8MB                        |
| DC-DC        | SY8089                     |
| IMU          | MPU6886 (I2CAddress: 0x68) |
| TFT 驱动 IC  | GC9107                     |
| 分辨率       | 128 x 128                  |
| 工作温度     | 0 ~ 40°C                   |
| 供电电压     | 5V                         |
| 供电方式     | TYPE C                     |
| 输出电压     | 3.3V                       |
| GPIO         | G5/G6/G7/G8/G38/G39        |
| 屏幕通讯协议 | SPI                        |
| 产品尺寸     | 24.0 x 24.0 x 12.9mm       |
| 产品重量     | 6.9g                       |
| 包装尺寸     | 85.0 x 65.0 x 16.0mm       |
| 毛重         | 11.2g                      |

## 操作说明

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/download%20mode1.gif" width="30%" />

\#> 注意 |**LCD 背光控制的时候，pwm 频率建议使用 500hz。**

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/IMU-AtomS3.jpg" width="70%">

## 原理图

- [AtomS3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_M5_AtomS3_v1.0.pdf)
- [AtomS3 IMU 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_AtomS3_IMU.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_M5_AtomS3_v1.0_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/Sch_AtomS3_IMU_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/C123_PinMap_01.jpg" width="100%">

### MPU6886

\#> 背部的 I2C 引脚共用总线

| ESP32-S3       | IO38 | IO39 |
| -------------- | ---- | ---- |
| MPU6886 (0x68) | SDA  | SCL  |

### LCD

| ESP32-S3 | G21  | G17 | G15 | G33 | G34 | G16    |
| -------- | ---- | --- | --- | --- | --- | ------ |
| MPU6886  | MOSI | SCK | CS  | RS  | RST | LCD_BL |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3/img-abe8d8b0-3d8c-4f42-a84a-093bfed0aa38.png" width="100%" />

## 结构文件

- [AtomS3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C123_AtomS3/Structures)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)
- [SY8089](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/ATOMS3/sy8089.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)

## 软件开发

### Arduino

- [AtomS3 Arduino 快速上手](/zh_CN/arduino/m5atomecho/program)
- [AtomS3 Arduino 驱动库](https://github.com/m5stack/M5AtomS3)

### UiFlow2

- [AtomS3 UiFlow2 快速上手](/zh_CN/uiflow2/atoms3/program)

### PlatformIO

- [AtomS3 出厂固件](https://github.com/m5stack/M5AtomS3-UserDemo)

```bash
[env:m5stack-atoms3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### Easyloader

| Easyloader       | 下载链接                                                                                   | 备注 |
| ---------------- | ------------------------------------------------------------------------------------------ | ---- |
| AtomS3 User Demo | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/ATOM/ATOMS3%20DEMO.exe) | /    |

## 相关视频

- 用 UiFlow 编程在 ATOMS3 中显示图片

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/ATOMS3%20UIFlow%E4%BD%BF%E7%94%A8%E4%BB%8B%E7%BB%8D.mp4" type="video/mp4"></video>

- 烧录 UiFlow 2X Alpha 固件到 AtomS3

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/Burning%20UIFlow%202X%20Alpha%20Firmware%20to%20AtomS3%20(1)-en.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1705468608&bvid=BV1ZT421v7UR&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/JHmTkAL8FlM?si=jOIcx0heRx1u45Bj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C123)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
