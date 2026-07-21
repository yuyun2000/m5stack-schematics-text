# Atomic SPK Base

<span class="product-sku">SKU:A098</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-f5cdbea1-3dac-4d19-90be-949fb4d0f859.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-98ff8029-5cc4-4efd-b82c-46f55cd35f5d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-ecc3bb6b-7fbb-4a64-b638-889757470ac3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-f3b2c2e2-6979-41ff-8604-e25fb20c95dd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-2ff0c47c-06e5-4fa7-b25e-933f4fee25fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-acbcd538-466f-4bd0-9040-4ee9847c874c.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/924/A098_Atomic_SPK_Base_weight.jpg">
</PictureViewer>

## 描述

**Atomic SPK Base** 是一款适配 ATOM 系列主控的音频播放器，内置 I2S 数字音频接口的功放芯片 NS4168，具备自动采样率检测，自适应功能，并能够有效防止音频信号失真。集成 microSD 卡槽，便于音频文件的保存与读取。提供 3.5mm 耳机接口与外部扬声器接口，用户可通过外接耳机或是扬声器进行音频播放。

## 产品特性

- 功放芯片 NS4168
- I2S 串行数字音频输入接口
- 支持宽范围采样速率：8kHz~96kHz
- 自动采样率检测，自适应功能
- microSD Card 卡槽
- 耳机接口
- 扬声器接口

## 包装内容

- 1 x Atomic SPK Base
- 1 x 1W@8Ω 扬声器

## 应用场景

- 音频播放器
- 无线音响
- Wi-Fi 音响

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 功放芯片     | NS4168               |
| 功放输出功率 | 1W (VDD=3.3V)        |
| 耳机接口     | 3.5mm                |
| 扬声器接口   | 1.25mm-2P            |
| 扬声器功率   | 1W@8Ω                |
| 产品尺寸     | 24.0 x 48.0 x 18.0mm |
| 产品重量     | 12.3g                |
| 包装尺寸     | 136.0 x 92.0 x 8.0mm |
| 毛重         | 14.4g                |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-315f8e96-ce32-4861-809c-cb02f5def6b5.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN   | LEFT | RIGHT | PIN      |
| ----- | ---- | ----- | -------- |
|       |      | 1     | 3V3      |
| LRCLK | 2    | 3     | BLCK     |
| DATA  | 4    | 5     | SPI_MOSI |
| 5V    | 6    | 7     | SPI_CLK  |
| GND   | 8    | 9     | SPI_MISO |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic SPK Base/img-456067b7-e4b1-4520-8304-c8f93672c118.jpg" width="100%" />

## 数据手册

- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)

## 软件开发

### Arduino

- [Atomic SPK Base Play RawPCM Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_SPK/PlayRawPCM)
- [Atomic SPK Base Play MP3 From microSD Card Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_SPK/PlayMP3FromSD)
- [Atomic SPK Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_spk_base)

### UiFlow1

- [Atomic SPK Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/spk)

### UiFlow2

- [Atomic SPK Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/speaker.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                                     | 备注 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic SPK Base Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20SPK%20Base/ezLoader-d59a8b92-2f0f-497e-a3d2-3ed69bb8d51d.exe) | /    |

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_SPK_VIDEO.mp4" type="video/mp4"></video>
