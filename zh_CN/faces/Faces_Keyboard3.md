# Faces Keyboard3

<span class="product-sku">SKU:A003-V3</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3-weight.png">
</PictureViewer>

## 描述

**Faces Keyboard3** 是适配 Faces Bottom 系列的键盘输入面板，采用 35 键布局，支持通过组合键实现多字符输入，满足基础文本输入与快捷控制需求。内部集成 STM32 核心主控，通过 I2C 通信协议与中断引脚和主机进行交互，具备响应快、集成度高的特点。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/faces/faces_keyboard3) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Faces Keyboard3 设备。 |

## 产品特性

- 内置 STM32 核心主控: STM32F030C8T6
- I2C 通信接口
- 按键布局: QWERTY 键盘
- 输入状态指示灯: 蓝色 LED x2

## 包装内容

- 1x Faces Keyboard3

## 应用场景

- 人机交互输入场景
- 参数配置与快捷操作
- 文本输入与菜单控制

## 规格参数

| 规格               | 参数                 |
| ------------------ | -------------------- |
| MCU                | STM32F030C8T6        |
| 通信接口           | I2C 通信 @ 0x08      |
| 按键布局           | QWERTY 全键盘        |
| 按键数量           | 35 键                |
| 输入状态指示灯     | 蓝色 LED x2          |
| 待机功耗（仅面板） | 3.3V@5.51mA          |
| 产品尺寸           | 57.0 x 54.1 x 10.0mm |
| 产品重量           | 21.4g                |
| 包装尺寸           | 56.0 x 59.0 x 19.0mm |
| 毛重               | 26.4g                |

## 操作说明

#>指示灯说明|键盘的**左侧蓝色指示灯常亮**表示当前为基底层（黑色字符）；**右侧蓝色指示灯常亮**表示当前为符号层（蓝色字符）；**左右指示灯交替闪烁**表示当前为功能层（红色字符）。请根据指示灯状态判断当前所处输入层级。

## 原理图

- [Faces Keyboard3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_page_01.png">
</SchViewer>

## 管脚映射

### Faces Panel Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
| GND | 1    | 2     |     |
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

- [Faces Keyboard3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Faces Keyboard3 Arduino 快速上手](/zh_CN/arduino/projects/faces/faces_keyboard3)
- [Faces Keyboard3 驱动库](https://github.com/m5stack/M5Faces)

### UiFlow2

- [Faces Keyboard3 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/develop/module/faces_keyboard3.html)

### 内置固件

- [Faces Keyboard3 内置固件](https://github.com/m5stack/M5Faces-Keyboard3-Internal-FW)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/A003-V3/I2C" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="第三代 Face系列产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1273/Faces_Series_Video-CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比表 | [Faces Keyboard3](/zh_CN/faces/Faces_Keyboard3) ![Faces Keyboard3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1270/A003-V3_Faces_Keyboard3_main_pictures_02.webp) | [Faces QWERTY](/zh_CN/module/faces_keyboard) ![Faces QWERTY](https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_cover_01.webp) |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU        | STM32F030C8T6                                                                                                                                                           | MEGA328                                                                                                                                                                |
::
