# AtomS3R-AI Chatbot

<span class="product-sku">SKU:K147</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147.webp">
</PictureViewer>

## 描述

AtomS3R-AI Chatbot 是一款 AI 语音开发套件。套件由控制器与语音底座两大核心部分组成，控制器部分采用 AtomS3R ，其核心采用 ESP32-S3 芯片。 提供了 8MB Flash + 8MB PSRAM 的大内存组合。同时集成 9 轴 IMU (BMI270 + BMM150) ，IR 发射管等丰富外设。语音底座部分采用 Atomic Voice Base， 基于 ES8311 音频编解码芯片，能够提供高保真音频解码与麦克风与扬声器驱动能力。
套件支持接入小智语音助手，OpenAI 语音助手与火山引擎语音助手等多种语音助手，实现实时语音交互、自定义唤醒词，以及低时延识别等功能。

## 教程 & 快速上手

learn>| ![AtomS3R小聆语音助手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-10.jpg) | [AtomS3R小聆语音助手](/zh_CN/guide/realtime/xiaoling/atomic_echo_base) | 本教程将向你介绍使用 AtomS3R+Atomic Voice Base 硬件组合，通过 M5Burner 烧录 小聆语音助手 固件，构建个人语音助手应用。 |

learn>| ![AtomS3R-AI Chatbot](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/realtime/openai/atomic_echo_base/atoms3r_openai_assistant_01.jpg) | [Atomic Voice Base OpenAI 语音助手](/zh_CN/guide/realtime/openai/atomic_echo_base) | 本教程将向你介绍使用 AtomS3R+Atomic Voice Base 硬件组合，通过 M5Burner 烧录 OpenAI Voice Assistant 固件，构建个人语音助手应用。 |

learn>| ![AtomS3R-AI Chatbot](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_xiaozhi_assistant_wifi_config_01.jpg) | [AtomS3 / AtomS3R 系列小智语音助手](/zh_CN/guide/realtime/xiaozhi/atomic_echo_base) | 本教程将向你介绍使用 AtomS3 系列设备 + Atomic Voice Base 硬件组合，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。 |

## 产品特性

- 支持小智语音，OpenAI 语音助手等
- AI 语音识别
- 端云协同与模型管理
- 集成 ESP32-S3 主控
- 九轴传感器系统
- 边缘 AI 推理
- 8MB Flash 和 8MB PSRAM
- 支持红外发射控制功能
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

## 包含

- 1 x AtomS3R
- 1 x Atomic Voice Base

## 应用

- 语音助手
- 智能家居

## 规格参数

| 规格                      | 参数                                                                        |
| ------------------------- | --------------------------------------------------------------------------- |
| SoC                       | ESP32-S3-PICO-1-N8R8@双核 Xtensa LX7, 主频 240MHz                           |
| USB                       | USB OTG, USB Serial/JTAG                                                    |
| Flash                     | 8MB                                                                         |
| PSRAM                     | 8MB                                                                         |
| Wi-Fi                     | 2.4 GHz Wi-Fi                                                               |
| TFT 驱动                  | GC9107                                                                      |
| 彩色 IPS 分辨率           | 128 x 128                                                                   |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% (加速度)，0.05°/s (角速度) <br/>I2C 地址：0x68                  |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/>挂载在 BMI270 上，通过 BMI270 获取磁力计数据              |
| 红外 IR                   | ∠180° 时红外线发射距离：12.46m (无遮挡情况下)                               |
| 扩展接口                  | 底部 GPIO: G5/G6/G7/G8/G38/G39 以及 HY2.0-4P 扩展端口                       |
| 音频编解码器              | ES8311：24 位分辨率，采用 I2S 协议                                          |
| MEMS 麦克风               | MSM381A3729H9BPC, 信噪比 (SNR)：≥65 dB                                      |
| 功率放大器                | NS4150B：D 类功率放大器                                                     |
| 扬声器                    | 2014 型腔体喇叭：1W@8Ω                                                      |
| 工作温度                  | 0 ~ 40°C                                                                    |
| 产品尺寸                  | AtomS3R: 24.0 x 24.0 x 12.9mm <br/>Atomic Voice Base: 24.0 x 24.0 x 14.14mm |
| 产品重量                  | AtomS3R: 6.6g <br/>Atomic Voice Base:6.3g                                   |
| 包装尺寸                  | 120.0 x 65.0 x 16.0mm                                                       |
| 毛重                      | 21.6g                                                                       |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%" />

\#> 注意 |**LCD 背光控制时，pwm 频率建议使用 500Hz。**

## 原理图

- [AtomS3R 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/Sch_M5_AtomS3R_v0.4.1.pdf)
- [Atomic Voice Base 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/Sch_ECHO%20Base_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1_page_01.png">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/schematic.png" width="100%">
</SchViewer>

## 管脚映射

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/%E5%8E%9F%E7%90%86%E5%9B%BE-pixel.jpg" width="100%"/>

### RGB & BMI270 & IR & BUTTON

| ESP32-S3-PICO-1-N8R8  | G0      | G45     | G47        | G41      |
| --------------------- | ------- | ------- | ---------- | -------- |
| LP5562 (RGB 控制芯片) | SYS_SCL | SYS_SDA |            |          |
| BMI270                | SYS_SCL | SYS_SDA |            |          |
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

### Atomic Voice Base

| Atomic Voice Base | SCL | SDA | SD/DSDIN | WS/LRCK | ASDOUT | SCK/SCLK |
| ----------------- | --- | --- | -------- | ------- | ------ | -------- |
| AtomS3R           | G39 | G38 | G5       | G6      | G7     | G8       |

## 尺寸图

<SchViewer>
<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/img-0cb94b8e-5cfc-4e52-930b-833ba8438078.png" width="100%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/model%20size.jpg">
</SchViewer>

## 结构文件

- [AtomS3R-AI Chatbot 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K147_AtomS3R-AI_Chatbot/Structures)

## 数据手册

- [ESP32-S3-PICO-1-N8R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/esp32-s3-pico-1_datasheet_en.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)
- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [MEMS MIC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/MEMS.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)

## 软件开发

### 快速上手

- [OpenAI Voice Assistant For AtomS3R + Atomic Voice Base 教程](/zh_CN/guide/realtime/openai/atomic_echo_base)
- [XiaoZhi Voice Assistant For AtomS3R + Atomic Voice Base 教程](/zh_CN/guide/realtime/xiaozhi/atomic_echo_base)

### Arduino

- [Atomic Voice Base Arduino 驱动库](https://github.com/m5stack/M5Atomic-EchoBase)

### UiFlow2

- [Atomic Voice Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/echo.html)

### ESP-IDF

- [Open RealtimeAPI Embedded SDK](https://github.com/m5stack/openai-realtime-embedded-sdk)

## 相关视频

- AtomS3R-AI Chatbot 产品介绍及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1149/K147-AtomS3R-AI-Chatbot_video.mp4" type="video/mp4"></video>

- OpenAI Voice Assistant For AtomS3R + Atomic Voice Base

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/OpenAI%20Voice%20Assistant%20For%20AtomS3R.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113858492567265&bvid=BV1bsw1e3EBS&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/RqMJ2y-FQpw?si=rb4tgfRx7iI9SDzu" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
