# Faces Gamepad3

<span class="product-sku">SKU:A004-V3</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3-weight.png">
</PictureViewer>

## 描述

**Faces Gamepad3** 是适配 Faces Bottom 系列的游戏控制输入面板，提供经典的方向控制、A/B 按键以及暂停/开始等交互按键，适合用于游戏控制和快捷操作场景。
内部集成 STM32 核心主控，通过 I2C 通信协议与中断引脚和主机进行交互，具备响应快、集成度高的特点。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/faces/faces_gamepad3) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Faces Gamepad3 设备。 |

## 产品特性

- 内置 STM32 核心主控: STM32F030F4P6
- I2C 通信接口
- 游戏手柄按键布局

## 包装内容

- 1x Faces Gamepad3

## 应用场景

- 游戏控制输入场景
- 方向控制与快捷操作场景
- 需要按键交互的嵌入式项目

## 规格参数

| 规格               | 参数                   |
| ------------------ | ---------------------- |
| MCU                | STM32F030F4P6          |
| 通信接口           | I2C 通信 @ 0x08        |
| 按键布局           | 方向键、A/B、开始/选择 |
| 按键数量           | 8 键                   |
| 待机功耗（仅面板） | 3.3V@4.91mA            |
| 产品尺寸           | 57.0 x 54.1 x 10.7mm   |
| 产品重量           | 19.2g                  |
| 包装尺寸           | 56.0 x 59.0 x 19.0mm   |
| 毛重               | 24.0g                  |

## 原理图

- [Faces Gamepad3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_Sche.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_Sche_page_01.png">
</SchViewer>

## 管脚映射

### Faces Panel Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
| GND | 1    | 2     | 5V  |
| INT | 3    | 4     | 3V3 |
|     | 5    | 6     |     |
|     | 7    | 8     |     |
|     | 9    | 10    |     |
|     | 11   | 12    |     |
|     | 13   | 14    |     |
|     | 15   | 16    | SDA |
|     | 17   | 18    | SCL |
|     | 19   | 20    |     |
|     | 21   | 22    |     |
::

## 尺寸图

- [Faces Gamepad3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Faces Gamepad3 Arduino 快速上手](/zh_CN/arduino/projects/faces/faces_gamepad3)
- [Faces Gamepad3 驱动库](https://github.com/m5stack/M5Faces)

### UiFlow2

- [Faces Gamepad3 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/develop/module/faces_gamepad3.html)

### 内置固件

- [Faces Gamepad3 内置固件](https://github.com/m5stack/M5Faces-Gamepad3-Internal-FW)

### 内置固件升级

- [Faces Gamepad3 内置固件升级工具 - ESP32](https://burner.m5stack.com/firmware/2095418985687408641/)
- [Faces Gamepad3 内置固件升级工具 - ESP32-S3](https://burner.m5stack.com/firmware/2095420693247287297/)
- [Faces Gamepad3 内置固件升级教程](/zh_CN/learn/firmware/internal_fw_upgrade)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/A004-V3/I2C" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="第三代 Face系列产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1273/Faces_Series_Video-CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比表 | [Faces Gamepad3](/zh_CN/faces/Faces_Gamepad3) ![Faces Gamepad3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1271/A004-V3_Faces_Gamepad3_main_pictures_02.webp) | [Faces Gamepad](/zh_CN/module/faces_gameboy) ![Faces Gamepad](https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_cover_01.webp) |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU        | STM32F030F4P6                                                                                                                                                       | MEGA328                                                                                                                                                               |
::
