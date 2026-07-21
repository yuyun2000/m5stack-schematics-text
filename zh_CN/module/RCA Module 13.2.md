# Module13.2 RCA

<span class="product-sku">SKU:M125</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-047dda32-31a1-4ce6-a6d4-910aa511caa5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-b61871cb-84ef-443c-938e-cb74fb64c83a.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/985/M125-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-95d097e0-acc0-4905-a1aa-12a654d495b3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-28b6ae0d-eb10-448d-82dd-1e1077d5798e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-27594f4c-8cd3-4dd9-a50f-8f43dc33dc4e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-037a2e12-a60a-4f4c-868e-9cdbfc8c9235.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/img-8407d8f0-1c26-416d-a334-f5aea37b18e8.webp">
</PictureViewer>

## 描述

**Module13.2 RCA** 是一款用于音视频复合信号扩展模块，采用常见的 S 端子 RCA 连接器，分为两路 (左右声道) 音频以及一路视频输出。音频部分采用 I2S 功放芯片 PCM5102APWR 方案，能实现 32 位立体声音频信号输出。视频方面，应用了主控 ESP32 的 DAC 模拟视频信号的功能，能产生分辨率不高于 864 x 576 (PAL,PAL_M) 的模拟视频信号。模块内含有 DC 插座，以及 9-24V 转 5V 的 DC/DC 电路，为整机供电。本产品适用于驱动 S 端子接口的音视频设备。

## 产品特性

- RCA 复合视频音频输出 (左右声道音频接口)
- RCA 母插孔接线端子
- 1 路 CVBS 视频输出接口 (GPIO25\&GPIO26 二选一切换)
- 3.5mm 耳机插口音频输出
- Port C 接口
- PCM5102 音频立体声 DAC
- DC 9-24V 转 5V 输出 (<5V,3A)

## 包装内容

- 1 x Module13.2 RCA

## 应用场景

- RCA 立体声输出
- 复合视频和音频输出

## 规格参数

| 规格                | 参数                                               |
| ------------------- | -------------------------------------------------- |
| 音频立体声 DAC 芯片 | PCM5102APWR                                        |
| 接口                | RCA 母座                                           |
| 通道                | 1 路 CVBS 视频输出接口 (GPIO25\&GPIO26 二选一切换) |
| 输出信号            | 音频和视频 (也可选择 3.5mm 耳机插口输出)           |
| DC-DC               | MP1584EN                                           |
| 音频立体声 DAC 芯片 | PCM5102APWR                                        |
| 产品尺寸            | 54.0 x 54.0 x 13.2mm                               |
| 产品重量            | 22.6g                                              |
| 包装尺寸            | 134.0 x 95.0 x 20.0mm                              |
| 毛重                | 42.2g                                              |

## 原理图

- [Module13.2 RCA 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/552/SCH_Module_RCA_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/552/SCH_Module_RCA_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     | VIDEO_SIG |
|           | 9    | 10    | VIDEO_SIG |
|           | 11   | 12    |           |
|           | 13   | 14    |           |
| PORT.C    | 15   | 16    | PORT.C    |
|           | 17   | 18    |           |
|           | 19   | 20    |           |
|           | 21   | 22    | BCK       |
| DIN       | 23   | 24    | LRCK      |
| HPWR      | 25   | 26    |           |
| HPWR      | 27   | 28    | 5V        |
| HPWR      | 29   | 30    | BAT       |
::

## 尺寸图

- [Module13.2 RCA 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/985/M125-rcamoudle.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/985/M125-rcamoudle_page_01.png" width="100%">

## 数据手册

- [MP1584EN_LF_Z](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/RCA%20Module%2013.2/MP1584EN_LF_Z.pdf)
- [PCM5102APWR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/RCA%20Module%2013.2/PCM5102APWR.pdf)

## 软件开发

### Arduino

- [Module13.2 RCA Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/RCA)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RCA Module 13.2/arduinoCase-1670481406252M5PPT.png" width="100%"/>

### UiFlow2

- [Module RCA UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/rca.html)
