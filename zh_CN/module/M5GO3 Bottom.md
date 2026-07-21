# Base M5GO Bottom3

<span class="product-sku">SKU:A014-D</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-68005a1e-c064-4573-a6ba-bd8745581064.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-c12d2485-41f6-438d-b836-7c6cc142877a.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/A014-D_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-fbf40860-d068-43aa-a5d7-e2b33d3bcec7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-beee25bf-6734-4d90-bfc3-2def5a24f2fb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-70b5c65b-1d66-4db8-89da-2e302b3fb439.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-6e845a1b-1f0c-49e7-b7a1-2c07a4bbbcc3.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/A014-D-1.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/A014-D-2.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-81359bc5-a051-4e9c-b713-130134a1d08f.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/A014-D-weight.jpg">
</PictureViewer>

## 描述

**Base M5GO Bottom3** 是一款专为 CoreS3 系列产品设计的拓展型底座，集成了红外发射 LED 和 500mAh 锂电池。两组 HY2.0-4P 拓展接口将常用的 ADC/DAC/UART 引脚进行了引出，能够用于各类型传感器的接入。底座两侧分别有 5 颗可编程 RGB 灯 (WS2812)，配合磨砂透光材质遮光条，能够提供柔和舒适发光效果。底部采用 pogo pin 磁吸充电接口，当吸附充电底座时，电流将经过内置的 TP4057 充电芯片安全的流入内部电池。除充电功能外 pogo pin 接口对主控 I2C 总线进行了引出，这使得用户能够通过磁吸的方式去外接拓展。内置吸附磁铁，背面采用兼容 LEGO 孔设计，能够与 LEGO 结构设计无缝对接。

## 产品特性

- 适用于 CoreS3 系列产品
- 红外发射器
- 可编程 LED 灯条
- 500mAh 锂电池
- HY2.0-4P 拓展接口
- 兼容乐高积木结构
- 适配磁吸充电底座

## 包装内容

- 1 x Base M5GO Bottom3
- 2 x M3\*16 螺丝
- 2 x M3\*18 螺丝

## 应用场景

- CoreS3 系列产品拓展
- CoreS3 系列产品 IOT 套件
- STEAM 教育

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 灯珠     | 10 x WS2812           |
| 电池     | 3.7V@500mAh           |
| 产品尺寸 | 54.0 x 54.0 x 15.0mm  |
| 包装尺寸 | 132.0 x 95.0 x 16.0mm |
| 产品重量 | 30.0g                 |
| 毛重     | 48.9g                 |

## 原理图

- [Base M5GO Bottom3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/M5GO3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/M5GO3_sch_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P   | Black   | Red   | Yellow   | White   |
| ---------- | ------- | ----- | -------- | ------- |
| PORT.B     | GND     | 5V    | G9       | G8      |
| PORT.C     | GND     | 5V    | G17      | G18     |
::

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     | PORT.B   |
| GND      | 5    | 6     |          |
|          | 7    | 8     | RGB      |
|          | 9    | 10    | PORT.B   |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
| RXD      | 15   | 16    | TXD      |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    | IR       |
|          | 23   | 24    |          |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    | BAT+     |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-c2558938-5e94-482b-9c59-02df14bb3088.jpg" width="100%" />

## 结构文件

- [Base M5GO Bottom3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/A014-D_Base_M5GO_Bottom3/Structures)

## 数据手册

- [TP4057](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/M5GO%20BATT%20Bottom3/7EEA633644BAFD22D2FBC132F5380171.pdf)

## 软件开发

### Arduino

[FastLED Library](https://github.com/FastLED/FastLED)

## 相关视频

- Base M5GO Bottom3 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/531/A014-D-Base-M5GO-Bottom3-ZH-Video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表   | [Base M5GO Bottom](/zh_CN/base/m5go_bottom) ![Base M5GO Bottom](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_cover_01.webp) | [Base M5GO Bottom2](/zh_CN/base/m5go_bottom2) ![Base M5GO Bottom2](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_cover_01.webp) | [Base M5GO Bottom3](/zh_CN/module/M5GO3%20Bottom) ![Base M5GO Bottom3](https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3%20Bottom/img-911850a0-1162-493a-8e2f-fa6493b6a9af.webp) |
| ------------ | ------------------                                                                                                                                                | -------------------                                                                                                                                                    | -------------------                                                                                                                                                                               |
| Core         | Basic (Core)                                                                                                                                                      | Core2                                                                                                                                                                  | CoreS3                                                                                                                                                                                            |
| RGB          | 10*SK6812                                                                                                                                                         | 10*SK6812                                                                                                                                                              | 10\*WS2812                                                                                                                                                                                        |
| IMU          | /                                                                                                                                                                 | MPU6886                                                                                                                                                                | /                                                                                                                                                                                                 |
| IR           | IR                                                                                                                                                                | /                                                                                                                                                                      | IR                                                                                                                                                                                                |
| BATTERY      | 500mAh                                                                                                                                                            | 500mAh                                                                                                                                                                 | 500mAh                                                                                                                                                                                            |
| MIC          | SPQ2410                                                                                                                                                           | SPM1423                                                                                                                                                                | /                                                                                                                                                                                                 |
::
