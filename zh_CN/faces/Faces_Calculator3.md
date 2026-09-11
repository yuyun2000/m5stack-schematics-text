# Faces Calculator3

<span class="product-sku">SKU:A005-V3</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncls.com/1272/A005-V3-weight.png">
</PictureViewer>

## 描述

Faces Calculator3 是一款适配 Faces Bottom 系列的计算器输入面板，采用 4 × 5 按键布局设计，覆盖常用数字、运算符和功能键，适合构建带本地计算能力的交互终端。面板通过 I2C 与主机通信，可用于提供数字录入、简易运算和计算结果显示等交互能力。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/faces/faces_calculator3) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Faces Calculator3 设备。 |

## 产品特性

- 内置 STM32 核心主控: STM32G031G8U6
- I2C 通信接口
- 计算器按键布局

## 包装内容

- 1x Faces Calculator3

## 应用场景

- 数字输入与运算交互场景
- 本地计算与参数录入场景
- 教学演示与原型验证项目

## 规格参数

| 规格               | 参数                 |
| ------------------ | -------------------- |
| MCU                | STM32G031G8U6        |
| 通信接口           | I2C 通信 @ 0x08      |
| 按键布局           | 4 x 5 计算器键盘     |
| 按键数量           | 20 键                |
| 待机功耗（仅面板） | 3.3V@1.79mA          |
| 产品尺寸           | 57.0 x 54.1 x 10.6mm |
| 产品重量           | 20.7g                |
| 包装尺寸           | 56.0 x 59.0 x 19.0mm |
| 毛重               | 25.5g                |

## 原理图

- [Faces Calculator3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3-Faces_Calculator3_Sche.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3-Faces_Calculator3_Sche_page_01.png">
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

- [Faces Calculator3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Faces Calculator3 Arduino 快速上手](/zh_CN/arduino/projects/faces/faces_calculator3)
- [Faces Calculator3 驱动库](https://github.com/m5stack/M5Faces)

### UiFlow2

- [Faces Calculator3 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/develop/module/faces_calculator3.html)

### 内置固件

- [Faces Calculator3 内置固件](https://github.com/m5stack/M5Faces-Calculator3-Internal-FW)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/A005-V3/I2C" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="第三代 Face系列产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1273/Faces_Series_Video-CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比表 | [Faces Calculator3](/zh_CN/faces/Faces_Calculator3) ![Faces Calculator3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3_Faces_Calculator3_main_pictures_02.webp) | [Faces Calculator](/zh_CN/module/faces_calculator) ![Faces Calculator](https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_cover_01.webp) |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MCU        | STM32G031G8U6                                                                                                                                                                   | MEGA328                                                                                                                                                                              |
::
