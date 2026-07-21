# AtomS3R

<span class="product-sku">SKU:C126</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/15.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/C126_weight.jpg">
</PictureViewer>

## 描述

**AtomS3R** 是一款基于 ESP32-S3 主控的高度集成的物联网可编程控制器。内部集成了 **ESP32-S3-PICO-1-N8R8** 主控、集成 Wi-Fi 功能、8 MB 片上 **Flash** 和 8 MB **PSRAM**；配有 0.85 英寸的彩色 **IPS 屏幕** ，屏幕下方有一个可编程按钮；内部有 5V 转 3.3V 的电路；内置三轴 **BMM150** 地磁传感器和六轴 **BMI270** 姿态传感器；配备 **USB Type-C** 接口用于供电和固件下载；带有一个 **HY2.0-4P** 扩展端口；底部有六个 **GPIO** 和电源引脚，便于扩展。与之前的产品相比，**AtomS3R** 的 **3D 天线** 经过增强，提供了更好的性能和更高的稳定性。产品尺寸仅为 **24.0 x 24.0 x 12.9mm** ，适用于各种嵌入式智能设备应用。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atoms3r/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 AtomS3R 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atoms3r/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomS3R 设备。 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/voice_assistant/atoms3r_with_atomic_echo_base_voice_assistant) | 本教程介绍如何将 AtomS3R + Atomic Voice Base 结合，集成语音助手功能进入 Home Assistant。|

## 产品特性

- 集成 ESP32-S3-PICO-1-N8R8 主控
- 九轴传感器系统 (BMI270 六轴 + BMM150 三轴地磁传感器)
- 8MB Flash 和 8MB PSRAM
- 支持红外发射控制功能
- 可编程按键
- 0.85 寸 LCD 屏幕
- 可扩展的引脚与接口
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3R

## 应用场景

- 运动检测方向感知
- 智能设备控制
- 物联网应用

## 规格参数

| 规格                      | 参数                                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| SoC                       | ESP32-S3-PICO-1-N8R8@双核 Xtensa LX7 处理器，主频高达 240MHz                                                    |
| USB                       | USB OTG, USB Serial/JTAG                                                                                        |
| Flash                     | 8MB                                                                                                             |
| PSRAM                     | 8MB Octal                                                                                                       |
| Wi-Fi                     | 2.4 GHz Wi-Fi                                                                                                   |
| TFT 驱动                  | ST7735                                                                                                          |
| 彩色 IPS 分辨率           | 128 x 128                                                                                                       |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% (加速度)，0.05°/s (角速度) <br/>I2C 地址：0x68                                                      |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/>挂载在 BMI270 上，通过 BMI270 获取磁力计数据                                                  |
| 红外 IR                   | ∠180° 时红外线发射距离：12.46m (无遮挡情况下)                                                                   |
| 休眠电流                  | GPIO-5V 供电：DC 5V@11.63 uA<br/>Grove-5V 供电：DC 5V@10.75 uA<br/>USB-5V 供电：DC 5V@92.50 uA (含 PD 电阻损耗) |
| 底部预留 GPIO             | G5/G6/G7/G8/G38/G39                                                                                             |
| 工作温度                  | 0 ~ 40°C                                                                                                        |
| 产品尺寸                  | 24.0 x 24.0 x 12.9mm                                                                                            |
| 产品重量                  | 6.8g                                                                                                            |
| 包装尺寸                  | 85.0 x 65.0 x 15.5mm                                                                                            |
| 毛重                      | 12.5g                                                                                                           |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%" />

\#> LCD 屏幕背光控制 | LCD 屏幕背光驱动的 PWM 信号频率推荐使用 500Hz，过高可能导致亮度调节功能异常。

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/IMU-AtomS3R.jpg" width="70%">

## 原理图

- [AtomS3R 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/C126_PinMap_01.jpg" width="100%" />

### RGB & BMI270 & IR & BUTTON

| ESP32-S3-PICO-1-N8R8  | G0      | G45     | G47        | G41      |
| --------------------- | ------- | ------- | ---------- | -------- |
| LP5562 (RGB 控制芯片) | SYS_SCL | SYS_SDA |            |          |
| BMI270 (0x68)         | SYS_SCL | SYS_SDA |            |          |
| IR                    |         |         | IR_LED_DRV |          |
| BUTTON                |         |         |            | USER_BUT |

### BMM150

| BMI270 | BMI270_ASDx | BMI270_ASCx |
| ------ | ----------- | ----------- |
| BMM150 | A_SDA       | A_SCL       |

\#> BMM150 挂载于 BMI270 | 通过 BMI270 的 Sensor Hub 辅助 I2C 接口接入 BMM150，实现统一的 9 轴传感数据采集。

### SCREEN

| ESP32-S3-PICO-1-N8R8 | LP5562_W | G48      | G42     | G21      | G15     | G14     |
| -------------------- | -------- | -------- | ------- | -------- | ------- | ------- |
| 0.85Inch IPS         | LCD_BL   | DISP_RST | DISP_RS | SPI_MOSI | SPI_SCK | DISP_CS |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/img-0cb94b8e-5cfc-4e52-930b-833ba8438078.png" width="100%" />

## 结构文件

- [AtomS3R 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C126_AtomS3R/Structures)

## 数据手册

- [ESP32-S3-PICO-1-N8R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/esp32-s3-pico-1_datasheet_en.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)

## 软件开发

## 快速上手

- [AtomS3R + Atomic Voice Base 语音助手](/zh_CN/homeassistant/voice_assistant/atoms3r_with_atomic_echo_base_voice_assistant)

### Arduino

- [AtomS3R Arduino 快速上手](/zh_CN/arduino/m5atoms3r/program)
- [AtomS3R Arduino 驱动库](https://github.com/m5stack/M5AtomS3)

### UiFlow2

- [AtomS3R UiFlow2 快速上手](/zh_CN/uiflow2/atoms3r/program)

### PlatformIO

```bash
[env:m5stack-atoms3r]
platform = espressif32@6.7.0
board = esp32-s3-devkitc-1
framework = arduino
board_build.arduino.memory_type = qio_opi
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### ESP-IDF

- [AtomS3R 出厂固件](https://github.com/m5stack/M5AtomS3-UserDemo/tree/atoms3r)

### Easyloader

| Easyloader                   | 下载链接                                                                                                               | 备注 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---- |
| AtomS3R User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/AtomS3R-UserDemo-V0.1.exe) | /    |

## 相关视频

- AtomS3R 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/C126.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113203023447456&bvid=BV1vGxjeFEDx&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Td_kx5qPO9M?si=Pdrj4op5yRmWhLfB" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare | [AtomS3R](/zh_CN/core/AtomS3R) ![AtomS3R](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/12.webp) | [AtomS3](/zh_CN/core/AtomS3) ![AtomS3](https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3/img-3e6a45a9-8d09-4a01-bb70-a7e39ad77cb6.webp) |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC             | ESP32-S3-PICO-1-N8R8                                                                                                                | ESP32-S3FN8                                                                                                                                             |
| Memory          | 8MB Flash + 8MB PSRAM                                                                                                               | 8MB Flash                                                                                                                                               |
| Sensor          | BMI270 + BMM150                                                                                                                     | MPU6886                                                                                                                                                 |
| Antenna         | Enhanced 3D Antenna                                                                                                                 | Standard 3D Antenna                                                                                                                                     |
::

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C126)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期   | 产品变更                                |
| ---------- | --------------------------------------- |
| 2026.05.14 | 屏幕驱动 IC 型号由 GC9107 变更为 ST7735 |
| 2025.09.19 | 首次发布                                |
