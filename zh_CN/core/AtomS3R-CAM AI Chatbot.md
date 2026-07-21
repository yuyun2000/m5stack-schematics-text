# AtomS3R-CAM AI Chatbot

<span class="product-sku">SKU:K147-CAM</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM.webp">
</PictureViewer>

## 描述

AtomS3R-CAM AI Chatbot 是一款 AI 视觉语音开发套件。套件由控制器与语音底座两大核心部分组成，控制器部分采用 AtomS3R-CAM ，其核心采用 ESP32-S3 芯片。 提供了 8MB Flash + 8MB PSRAM 的大内存组合。同时集成 0.3MP GC0308 摄像头， 9 轴 IMU (BMI270 + BMM150) ，IR 发射管等丰富外设。语音底座部分采用 Atomic Voice Base， 基于 ES8311 音频编解码芯片，能够提供高保真音频解码与麦克风与扬声器驱动能力。套件支持接入小智语音助手，OpenAI 语音助手与火山引擎语音助手等多种语音助手功能，可应用于语音助手、智能家居等嵌入式场景。

## 教程 & 快速上手

learn>| ![AtomS3R-CAM AI Chatbot](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_wifi_config_01.jpg) | [Quick Start](/zh_CN/guide/realtime/xiaozhi/atomic_echo_base) | 本教程将向你介绍使用 AtomS3 系列设备 + Atomic Voice Base 硬件组合，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。 |

## 产品特性

- 集成 ESP32-S3-PICO-1-N8R8 主控
- 0.3MP GC0308 摄像头
- 九轴传感器系统
- 8MB Flash 和 8MB PSRAM
- 集成红外发射管
- 可扩展的引脚与接口
- 全双工 I2S 语音
- 24‑bit 音频编解码
- MEMS 数字麦克风
- D 类功放 (8Ω @ 1W 扬声器)
- 开发平台
  - ESP-IDF
  - PlatformIO
  - Arduino
  - UiFlow2

## 包装内容

- 1 x AtomS3R-CAM
- 1 x Atomic Voice Base

## 应用场景

- 语音助手
- 智能家居

## 规格参数

| 规格                      | 参数                                                                            |
| ------------------------- | ------------------------------------------------------------------------------- |
| SoC                       | ESP32-S3-PICO-1-N8R8@双核 Xtensa LX7 处理器，主频高达 240MHz                    |
| USB                       | USB OTG, USB Serial/JTAG                                                        |
| Flash                     | 8MB                                                                             |
| PSRAM                     | 8MB                                                                             |
| Wi-Fi                     | 2.4 GHz Wi-Fi                                                                   |
| 摄像头                    | GC0308，0.3 MP，F2.6，57.6° FOV                                                 |
| 红外 IR                   | 180° 发射角，无遮挡最远 12.46 m                                                 |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% (加速度)，0.05°/s (角速度) <br/>I2C 地址：0x68                      |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/>挂载在 BMI270 上，通过 BMI270 获取磁力计数据                  |
| 扩展接口                  | 底部 GPIO: G5/G6/G7/G8/G38/G39 以及 HY2.0-4P 扩展端口                           |
| 音频编解码器              | ES8311：24 位分辨率，采用 I2S 协议                                              |
| MEMS 麦克风               | MSM381A3729H9BPC，信噪比 (SNR)：≥65 dB                                          |
| 功率放大器                | NS4150B：D 类功率放大器                                                         |
| 扬声器                    | 2014 型腔体喇叭：1W@8Ω                                                          |
| 工作温度                  | 0 ~ 40°C                                                                        |
| 产品尺寸                  | AtomS3R-CAM: 24.0 x 24.0 x 13.5mm <br/>Atomic Voice Base: 24.0 x 24.0 x 14.14mm |
| 产品重量                  | AtomS3R-CAM: 7.4g <br/>Atomic Voice Base: 6.3g                                  |
| 包装尺寸                  | 120.0 x 65.0 x 16.0mm                                                           |
| 毛重                      | 22.1g                                                                           |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/AtomS3R-CAM_download_mode.gif" width="30%" />

## 原理图

- [AtomS3R-CAM main board schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/Sch_M5_AtomS3R_v0.4.1.pdf)
- [AtomS3R-CAM ext board schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/Sch_M5_AtomS3R_CAM%E5%B0%8F%E6%9D%BF.pdf)
- [Atomic Voice Base 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/Sch_ECHO%20Base_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_v0.4.1_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_page_01.png">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/schematic.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/%E5%8E%9F%E7%90%86%E5%9B%BE-pixel.jpg" width="100%" />

### BMI270 & IR

| ESP32-S3-PICO-1-N8R8 | G0      | G45     | G47        |
| -------------------- | ------- | ------- | ---------- |
| BMI270               | SYS_SCL | SYS_SDA |            |
| IR                   |         |         | IR_LED_DRV |

### BMM150

| BMI270 | BMI270_ASDx | BMI270_ASCx |
| ------ | ----------- | ----------- |
| BMM150 | A_SDA       | A_SCL       |

\#> BMM150 挂载于 BMI270 | 通过 BMI270 的 Sensor Hub 辅助 I2C 接口接入 BMM150，实现统一的 9 轴传感数据采集。

### GC0308

| GC0308  | ESP32-S3-PICO-1-N8R8 |
| ------- | -------------------- |
| CAM_SDA | G12                  |
| CAM_SCL | G9                   |
| VSYNC   | G10                  |
| HREF    | G14                  |
| Y9      | G13                  |
| XCLK    | G21                  |
| Y8      | G11                  |
| Y7      | G17                  |
| PCLK    | G40                  |
| Y6      | G4                   |
| Y2      | G3                   |
| Y5      | G48                  |
| Y3      | G42                  |
| Y4      | G46                  |
| POWER_N | G18                  |

### HY2.0-4P

::grove-table
| HY2.0-4P      | Black   | Red   | Yellow   | White   |
| ------------- | ------- | ----- | -------- | ------- |
| PORT.CUSTOM   | GND     | 5V    | G2       | G1      |
::

### Atomic Voice Base

| Atomic Voice Base | SCL | SDA | SD/DSDIN | WS/LRCK | ASDOUT | SCK/SCLK |
| ----------------- | --- | --- | -------- | ------- | ------ | -------- |
| AtomS3R CAM       | G39 | G38 | G5       | G6      | G7     | G8       |

## 尺寸图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R Cam/img-1f8b0888-c56b-424c-95d3-b67a45015569.png">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/model%20size.jpg">
</SchViewer>

## 结构文件

- [AtomS3R-CAM AI Chatbot 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K147-CAM_AtomS3R-CAM_AI_Chatbot/Structures)

## 数据手册

- [ESP32-S3-PICO-1-N8R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/esp32-s3-pico-1_datasheet_en.pdf)
- [GC0308](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/GC0308.PDF)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)
- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [MEMS MIC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/MEMS.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)

## 软件开发

### 快速上手

[Atomic Voice Base 小智语音助手教程](/zh_CN/guide/realtime/xiaozhi/atomic_echo_base)

### Arduino

- [Atomic Voice Base Arduino 驱动库](https://github.com/m5stack/M5Atomic-EchoBase)
- [AtomS3R-CAM 网络摄像头示例](https://github.com/m5stack/M5AtomS3/blob/main/examples/Basics/camera/camera.ino)

### UiFlow2

- [Atomic Voice Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/echo.html)

### ESP-IDF

- [Open RealtimeAPI Embedded SDK](https://github.com/m5stack/openai-realtime-embedded-sdk)

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

## 相关视频

- AtomS3R-CAM AI Chatbot 产品介绍及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1148/K147-CAM-AtomS3R-CAM-AI-Chatbot_2.mp4"></video>

- Atomic Voice Base 产品介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/Atomic%20Echo%20Base.mp4" type="video/mp4"></video>
