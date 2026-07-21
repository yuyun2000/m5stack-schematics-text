# Base M5GO Bottom2 v1.3

<span class="product-sku">SKU:A014-C-V13</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**Base M5GO Bottom2 v1.3** 是专为 Core2 v1.3 定制的扩展底座。
底座板载 **BMI270 六轴姿态传感器**、**SPM1423 数字麦克风** 及 **500 mAh 内置锂电池**；配备两组 HY2.0-4P 扩展接口，引出 ADC、DAC、UART 常用外设引脚，可便捷外接各类传感器模块。

底座双侧共集成 10 颗可编程 SK6812 RGB 灯珠，搭配磨砂透光导光条，呈现柔和均匀的灯光效果。底部采用 Pogo Pin 磁吸充电接口，接入磁吸充电底座后，可通过板载 **TP4057 充电管理芯片** 为内置电池安全稳压充电。同时 Pogo Pin 复用引出主控 **I2C 总线**，支持磁吸式外接扩展；底座内置吸附磁铁，背部预留乐高兼容安装孔位，可与乐高结构件无缝拼接适配。**适用于物联网开发、姿态感应交互及声光创意项目等场景。**

## 产品特性

- 兼容 Core2 v1.3
- 数字麦克风
- 可编程 LED 灯条
- 500mAh 锂电池
- HY2.0-4P 拓展接口
- 兼容乐高积木结构
- 适配磁吸充电底座

## 包装内容

- 1 x Base M5GO Bottom2 v1.3
- 2 x M3\*16 螺丝
- 2 x M3\*18 螺丝

## 应用场景

- Core2 v1.3 拓展
- 物联网开发
- 姿态感应交互
- 声光创意项目

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| 麦克风   | SPM1423                |
| LED      | SK6812 x 10            |
| IMU      | BMI270                 |
| 产品尺寸 | 54.0 x 54.0 x 15.0mm   |
| 产品重量 | 30.0g                  |
| 包装尺寸 | 132.0 x 95.0 x 16.0 mm |
| 毛重     | 47.4g                  |

## 原理图

[Base M5GO Bottom2 v1.3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1227/SCH_M5GO-Bottom2_SCH_Main_V1.31_2026_03_16_10_32_04.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1227/SCH_M5GO_Bottom2_SCH_Main_V1.31_2026_03_16_10_32_04_page_01.png" width="100%"/>
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

### BMI270 & Pogo Pin

| ESP32 Chip | G21 | G22 |
| ---------- | --- | --- |
| BMI270     | SDA | SCL |
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
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)

## 软件开发

### Arduino

- [Base M5GO Bottom2 v1.3 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Base/M5GO_BOTTOM2)

### EasyLoader

| Easyloader                             | Download                                                                                                     | Note |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Base M5GO Bottom2 v1.3 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/BASE/EasyLoader_M5GO_BOTTOM2.exe) | /    |

## 产品对比

::compare-table
| 产品对比表 | [Base M5GO Bottom2 v1.3](/zh_CN/base/m5go_bottom2_v1.3) ![Base M5GO Bottom2 v1.3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png) | [Base M5GO Bottom](/zh_CN/base/m5go_bottom) ![Base M5GO Bottom](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_cover_01.webp) | [Base M5GO Bottom2](/zh_CN/base/m5go_bottom2) ![Base M5GO Bottom2](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_cover_01.webp) | [Base M5GO Bottom3](/zh_CN/module/M5GO3%20Bottom) ![Base M5GO Bottom3](https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3%20Bottom/img-911850a0-1162-493a-8e2f-fa6493b6a9af.webp) |
| ---        | ----------                                                                                                                                               | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core       | Core2 v1.3                                                                                                                                                    | Basic (Core)                                                                                                                                                      | Core2                                                                                                                                                                  | CoreS3                                                                                                                                                                                            |
| RGB        | 10*SK6812                                                                                                                                                | 10*SK6812                                                                                                                                                         | 10\*SK6812                                                                                                                                                             | 10\*WS2812                                                                                                                                                                                        |
| IMU        | BMI270                                                                                                                                                   | /                                                                                                                                                                 | MPU6886                                                                                                                                                                | /                                                                                                                                                                                                 |
| IR         | ---                                                                                                                                                      | IR                                                                                                                                                                | /                                                                                                                                                                      | IR                                                                                                                                                                                                |
| BATTERY    | 500mAh                                                                                                                                                   | 500mAh                                                                                                                                                            | 500mAh                                                                                                                                                                 | 500mAh                                                                                                                                                                                            |
| MIC        | SPM1423                                                                                                                                                  | SPQ2410                                                                                                                                                           | SPM1423                                                                                                                                                                | /                                                                                                                                                                                                 |
::
