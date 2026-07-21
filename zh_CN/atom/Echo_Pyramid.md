# Voice Pyramid

<span class="product-sku">SKU:A167</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167-weight.jpg">
</PictureViewer>

## 描述

Voice Pyramid 是一款面向智能语音交互应用的功能底座。专为 M5Stack 的 **Atom** 系列主控设计 (不兼容 Atom Voice)，即插即用，快速构建具备高性能音频交互能力的语音设备。外接 Atom 系列主控单元实现音频数据处理、无线通信、业务逻辑控制以及物联网连接，适用于远场语音识别、语音助手、语音控制等多种智能交互场景。
设备内置独立 **STM32G030F6P6** 微控制器，专门负责管理双侧电容触摸滑动区与 RGB 指示灯，实现低延迟触控响应与多彩、可编程的灯效反馈。通过直观的触摸操作结合丰富的视觉指示，用户能够轻松感知设备状态、语音交互结果或系统提示，提升整体使用体验与产品表现力。音频系统采用高性能 **ES8311** 音频编解码器，搭配 **ES7210** 麦克风输入采集 + AEC 回声消除，实现高效的声学回声消除、噪声抑制与清晰远场语音采集，为语音识别和全双工交互提供可靠保障；通过 AW87559 高效 Class-D 扬声器驱动芯片，驱动内置扬声器，提供动态范围出色、音质清晰的音频输出。系统引入 **Si5351** 可编程时钟发生器作为主时钟源（MCLK），为音频 ADC 与 DAC 提供低抖动、可灵活配置的时钟信号，有效提高语音识别准确率与整体音频表现。
Voice Pyramid 适用于智能音箱、桌面语音助手、语音控制中枢、本地 / 云端语音交互原型以及物联网语音网关等开发场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/atomic/echo_pyramid) | 本教程介绍如何通过 Arduino IDE 编程控制 Voice Pyramid。|

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_HA_tutorial_01.jpg) | [Home Assistant](/zh_CN/homeassistant/voice_assistant/echo_pyramid) | 本教程介绍在 Home Assistant 集成 Voice Pyramid 的方法。 |

learn>| ![Voice Pyramid 小智语音助手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/Echo_Pyramid_Xiaozhi_Cover_01.jpg) | [Voice Pyramid 小智语音助手](/zh_CN/guide/realtime/xiaozhi/echo_pyramid) | 本教程介绍使用 AtomS3R 设备搭配 Voice Pyramid 开发底座，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。 |

learn>| ![Voice Pyramid 蓝牙音箱](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/Echo_Pyramid_BT_Audio_Cover_01.jpg) | [Voice Pyramid 蓝牙音箱](/zh_CN/guide/input_device/echo_pyramid) | 本教程介绍使用 Atom-Matrix 设备搭配 Voice Pyramid 开发底座，通过 M5Burner 烧录 Voice Pyramid 蓝牙音箱固件的方法。 |

## 注意事项

!>注意|请勿将 Voice Pyramid 与 Atom Voice 搭配使用，否则可能导致设备损坏。

## 产品特性

- 独立 STM32G030F6P6 辅助 MCU 管理触控与 RGB 灯效
- ES8311 高性能音频编解码器（支持高保真播放与采集）
- ES7210 麦克风输入采集 + AEC 回声消除
- AW87559 高效扬声器功放 + 内置扬声器
- Si5351 可编程低抖动主时钟发生器
- 可编程 RGB 指示灯
- 两侧触摸滑动区
- 1x HY2.0-4P Grove 扩展接口（I2C）

## 包装内容

- 1x Voice Pyramid

## 应用场景

- 智能音箱与桌面语音助手
- 语音控制中枢
- 本地 / 云端语音交互原型
- 物联网语音网关

## 规格参数

| 规格         | 参数                                                |
| ------------ | --------------------------------------------------- |
| MCU          | STM32G030F6P6                                       |
| 音频解码芯片 | ES8311                                              |
| 音频采集芯片 | ES7210                                              |
| 麦克风       | LMA3729T381-0Y3S                                    |
| 放大器       | AW87559                                             |
| 指示灯       | 28 x WS2812 RGB LED（单条 RGB Bar 内嵌 7 颗灯珠）   |
| 触控功能     | 两侧触摸滑动区包含四个触摸检测点，每侧分别集成 2 个 |
| 输入电源     | DC 5V                                               |
| 扩展接口     | 1x HY2.0-4P                                         |
| 待机功耗     | 14.92mA（无主控供电待机）                           |
| 工作功耗     | 578.47mA （连接主控最大音量输出）                   |
| 工作温度     | -10°C ~ 60°C                                        |
| 产品尺寸     | 83.6 x 83.6 x 56.7mm                                |
| 产品重量     | 100.7g                                              |
| 包装尺寸     | 93.0 x 86.0 x 56.0mm                                |
| 毛重         | 145.1g                                              |

## 操作说明

### 安装 Atom 系列主控

将 Atom 系列主控与 Voice Pyramid 的预留排针接口对齐，垂直平稳插入，确保连接可靠。

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/pyramid.gif" width="30%" />

### RGB LED 灯条与触控点说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_doc_operate_01.png" width="60%">

- Voice Pyramid 设备内部的 RGB LED 灯条分为两组（RGB CH1 / RGB CH2），通过 STM32 协处理器控制，每组的内部灯珠连续编号为 0~13（如图所示）。
- Voice Pyramid 两侧共配备 4 个触控检测点（如上图所示的 TP1、TP2、TP3、TP4），可用于实现滑动或单点触控交互。

### 供电说明

?> 注意 | 请使用 Voice Pyramid 底部 的 USB Type-C 或 HY2.0-4P 接口进行供电，否则设备无法正常启动。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_doc_operate_02.png" width="60%">

## 原理图

- [Voice Pyramid 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_04.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
| SCL | 2    | 3     | I2S_DOUT |
| SDA | 4    | 5     | I2S_SCLK |
| 5V  | 6    | 7     | I2S_DIN  |
| GND | 8    | 9     | I2S_LRCK |
::

### Voice Pyramid

| Voice Pyramid        | SCL | SDA | I2S_SCLK | I2S_LRCK | I2S_DOUT | I2S_DIN |
| -------------------- | --- | --- | -------- | -------- | -------- | ------- |
| SI5351 (0x60)        | SCL | SDA |          |          |          |         |
| ES8311 (0x18)        | SCL | SDA | SCLK     | LRCK     |          | DSDIN   |
| ES7210 (0x40)        | SCL | SDA | SCLK     | LRCK     | ASDOUT   |         |
| STM32G030F6P6 (0x1A) | SCL | SDA |          |          |          |         |
| AW87559 (0x5B)       | SCL | SDA |          |          |          |         |

### SI5351

| SI5351 (0x60) | CLK1         |
| ------------- | ------------ |
| ES7210 (0x40) | I2S_MCLK_ADC |
| ES8311 (0x18) | I2S_MCLK_DAC |

### AW87559

| AW87559 (0x5B)       | SPK_RST |
| -------------------- | ------- |
| STM32G030F6P6 (0x1A) | GPIOB 7 |
|                      |

### WS2812C

| STM32G030F6P6 (0x1A) | PA6 | PA7 |
| -------------------- | --- | --- |
| NEOPIXEL1            |     | DIN |
| NEOPIXEL2            | DIN |     |

### PT2042AD4

| STM32G030F6P6 (0x1A) | PA0      | PA1      | PA4      | PA5      |
| -------------------- | -------- | -------- | -------- | -------- |
| TP_1                 | TP_1_OUT |          |          |          |
| TP_2                 |          | TP_2_OUT |          |          |
| TP_3                 |          |          |          | TP_3_OUT |
| TP_4                 |          |          | TP_4_OUT |          |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SCL    | SDA   |
::

## 尺寸图

- [Voice Pyramid 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_echo-pyramid_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_echo-pyramid_model_size_page_01.png" width="100%">

## 数据手册

- [ES7210](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/ES7210.PDF)
- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [AW87559](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/DS_AW87559_EN_V1.4.pdf)
- [SI5351](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/Si5351-B.pdf)
- [STM32G030F6P6](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/stm32g030c6.pdf)

## 软件开发

### 快速上手

- [Voice Pyramid Home Assistant教程](/zh_CN/homeassistant/voice_assistant/echo_pyramid)
- [Voice Pyramid 小智语音助手](/zh_CN/guide/realtime/xiaozhi/echo_pyramid)
- [Voice Pyramid 蓝牙音箱](/zh_CN/guide/input_device/echo_pyramid)

### Arduino

- [Voice Pyramid Arduino 快速上手](/zh_CN/arduino/projects/atomic/echo_pyramid)
- [Voice Pyramid Arduino 驱动库](https://github.com/m5stack/M5Echo-Pyramid)

### ESP-IDF

- [BT Audio Player 源码](https://github.com/hlym123/esp-adf/tree/master/examples/player/bt_speaker_echo_pyramid)

### 内置固件

- [Voice Pyramid 内置固件](https://github.com/m5stack/M5Echo-Pyramid-Internal-FW)

## 相关视频

- Voice Pyramid 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/A167_Echo_Pyramid_video_ZH.mp4" type="video/mp4"></video>
