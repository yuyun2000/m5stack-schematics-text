# Base M5GO Bottom2

<span class="product-sku">SKU:A014-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1007/A014-C_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_06.webp">
</PictureViewer>

## 描述

**Base M5GO Bottom2** 是一款专为 Core2 设计的拓展型底座。底座集成了 MPU6886 六轴姿态传感器、数字麦克风（SPM1423）、500 mAh 锂电池。两组 HY2.0-4P 拓展接口将常用的 ADC/DAC/UART 引脚进行了引出，能够用于各类型传感器的接入。底座左右两侧一共 10 颗可编程 RGB 灯（SK6812），配合磨砂透光材质遮光条，能够提供柔和舒适发光效果。底部采用 pogo pin 磁吸充电接口，当吸附充电底座时，电流将经过内置的 TP4057 充电芯片安全的流入内部电池。除充电功能外，pogo pin 接口对主控 I2C 总线进行了引出，这使得你能够通过磁吸的方式去外接拓展。内置吸附磁铁，背面采用兼容 LEGO 孔设计，能够与你的其他的 LEGO 结构设计无缝对接。

## 产品特性

- 兼容 Core2
- 数字麦克风
- 可编程 LED 灯条
- 500mAh 锂电池
- HY2.0-4P 拓展接口
- 兼容乐高积木结构
- 适配磁吸充电底座

## 包装内容

- 1 x Base M5GO Bottom2
- 2 x M3\*16 螺丝
- 2 x M3\*18 螺丝

## 应用场景

- CORE2 拓展

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| 麦克风   | SPM1423                |
| LED      | SK6812 x 10            |
| IMU      | MPU6886                |
| 产品尺寸 | 54.0 x 54.0 x 15.0mm   |
| 产品重量 | 30.0g                  |
| 包装尺寸 | 132.0 x 95.0 x 16.0 mm |
| 毛重     | 47.4g                  |

## 原理图

[Base M5GO Bottom2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1007/A014-C_Sch_M5GO2.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1007/A014-C_Sch_M5GO2_page_01.png" width="100%"/>
</SchViewer>

## 管脚映射

### SK6812-LED Bar

| ESP32 Chip | G25  |
| ---------- | ---- |
| SK6812     | DATA |

### SPM1423 - 麦克风

| ESP32 Chip | G34 | G0  |
| ---------- | --- | --- |
| SPM1423    | DAT | CLK |

### MPU6886 & Pogo Pin

| ESP32 Chip | G21 | G22 |
| ---------- | --- | --- |
| MPU6886    | SDA | SCL |
| Pogo Pin   | SDA | SCL |

### HY2.0-4P

| ESP32 Chip | G26      | G36      |
| ---------- | -------- | -------- |
| PORT.B     | G26(DAC) | G36(ADC) |

| ESP32 Chip | G13       | G14       |
| ---------- | --------- | --------- |
| PORT.C     | G13(RXD2) | G14(TXD2) |

### M5-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN      |
| ------- | ---- | ----- | -------- |
| GND     | 1    | 2     | NC       |
| GND     | 3    | 4     | PORT.B   |
| GND     | 5    | 6     | NC       |
| NC      | 7    | 8     | RGB LED  |
| NC      | 9    | 10    | PORT.B   |
| NC      | 11   | 12    | 3V3      |
| NC      | 13   | 14    | NC       |
| UART_RX | 15   | 16    | UART_TX  |
| IMU_SDA | 17   | 18    | IMU_SCL  |
| NC      | 19   | 20    | NC       |
| NC      | 21   | 22    | NC       |
| NC      | 23   | 24    | I2S_LRCK |
| NC      | 25   | 26    | I2S_DIN  |
| NC      | 27   | 28    | 5V       |
| NC      | 29   | 30    | BAT      |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-c2558938-5e94-482b-9c59-02df14bb3088.jpg" width="100%" />

## 数据手册

- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)

## 软件开发

### Arduino

- [Base M5GO Bottom2 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Base/M5GO_BOTTOM2)

### EasyLoader

| Easyloader                        | Download                                                                                                     | Note |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Base M5GO Bottom2 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/BASE/EasyLoader_M5GO_BOTTOM2.exe) | /    |

## 相关视频

- IMU 数据获取，麦克风数据获取显示频谱，控制 LED 灯闪烁.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Base/M5GO_BOTTOM2_video.mp4" type="video/mp4">
</video>

## 产品对比

::compare-table
| 产品对比表 | [Base M5GO Bottom](/zh_CN/base/m5go_bottom) ![Base M5GO Bottom](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_cover_01.webp) | [Base M5GO Bottom2](/zh_CN/base/m5go_bottom2) ![Base M5GO Bottom2](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_cover_01.webp) | [Base M5GO Bottom3](/zh_CN/module/M5GO3%20Bottom) ![Base M5GO Bottom3](https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3%20Bottom/img-911850a0-1162-493a-8e2f-fa6493b6a9af.webp) |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core       | Basic (Core)                                                                                                                                                      | Core2                                                                                                                                                                  | CoreS3                                                                                                                                                                                            |
| RGB        | 10*SK6812                                                                                                                                                         | 10*SK6812                                                                                                                                                              | 10\*WS2812                                                                                                                                                                                        |
| IMU        | /                                                                                                                                                                 | MPU6886                                                                                                                                                                | /                                                                                                                                                                                                 |
| IR         | IR                                                                                                                                                                | /                                                                                                                                                                      | IR                                                                                                                                                                                                |
| BATTERY    | 500mAh                                                                                                                                                            | 500mAh                                                                                                                                                                 | 500mAh                                                                                                                                                                                            |
| MIC        | SPQ2410                                                                                                                                                           | SPM1423                                                                                                                                                                | /                                                                                                                                                                                                 |
::
