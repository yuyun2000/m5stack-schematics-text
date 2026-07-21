# Cardputer

<span class="product-sku">SKU:K132</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/K132-main-pictures_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-60261bcd-a23f-40e6-994d-ad97477dcec4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-bceba3da-490a-41d8-9927-64d0279a3cb1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-7e59fa08-5dec-48db-acc9-18559185ac7c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-8147e39a-60dc-478c-af36-52c1953c438e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-e3288169-9100-44f4-becd-afe1556f56b0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-a354b178-8c1e-4e60-8338-77efe96ea8df.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-200999cf-cf5d-463d-911d-7b4c2f4222c1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-e095a0f7-0c8c-414e-86bb-55e0148e55e9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/16.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/17.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/18.webp">
</PictureViewer>

## 描述

**Cardputer** 是一款适合工程师的卡片电脑，采用 Stamp-S3 作为主控。在控制交互方面，配备 56 按键键盘与 1.14 寸 TFT 屏幕进行显示交互，另外板载 SPM1423 数字 MEMS 麦克风可以进行录音或者唤醒等操作，此外还连接腔体喇叭进行声音的播放，搭载一个红外发射管对外进行红外控制交互。扩展方面，板载一个 Grove 口，可以自定义扩展传感器。存储方面，板载一个 microSD 卡槽，可以进行存储空间的扩容。供电方面，内部配备 120mAh + 1400mAh（底座中）的锂电池的方案对整机进行供电，大大提高续航能力，内含锂电池充电和升压降压电路。结构方面，底座含磁铁可以进行金属吸附，结构设置兼容乐高孔扩展。该产品适用于工程师快速功能验证设计、工业控制、家居控制系统等场景。

## 注意事项

!> 拆除注意事项 | 如果需要拆除面板上的 StampS3 的时候，务必小心背面的 FPC 线和 connector，轻轻拔起，否则容易损坏屏幕连接的座子。可参考[Cardputer Accessory Kit](/zh_CN/accessory/Cardputer%20Accessory%20Kit)中的操作视频。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5cardputer/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Cardputer 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/cardputer/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Cardputer 设备 |

## 产品特性

- Stamp-S3 微控制器。
- 56 按键键盘。
- 1.14 寸 TFT 屏幕。
- 腔体喇叭和 SPM1423 数字 MEMS 麦克风。
- 红外发射管用于红外控制交互。
- HY2.0-4P 接口，可连接和扩展 I2C 传感器。
- microSD 卡槽，用于扩展存储空间。
- 内置 120mAh 和底座中的 1400mAh 锂电池，提供长时间续航能力。
- 底座带有磁铁，兼容乐高孔扩展。
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Cardputer
- 1 x M2 内六角扳手

## 应用场景

- 快速功能验证和原型设计
- 工业控制和自动化
- 家居控制系统
- 数据采集和传感器监测
- 嵌入式系统开发和学习
- 无线通信和物联网 (IoT) 项目

## 规格参数

| 规格         | 参数                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| SoC          | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz                                                                  |
| USB          | USB OTG, USB Serial/JTAG                                                                                  |
| Flash        | 8MB                                                                                                       |
| Wi-Fi        | 2.4 GHz Wi-Fi                                                                                             |
| 存储         | SD Card                                                                                                   |
| 键盘         | 56 按键 (4 x 14)                                                                                          |
| 按键         | 1 x 复位按键 + 1 x 用户按键                                                                               |
| Grove        | 1 x HY2.0-4P                                                                                              |
| 电池容量     | 120mAh+1400mAh（底座中）                                                                                  |
| 屏幕         | ST7789V2@1.14 Inch, 240 x 135px                                                                           |
| 腔体喇叭     | 8Ω@1W<br/>I2S@NS4168                                                                                      |
| 麦克风       | MEMS 麦克风 @SPM1423                                                                                      |
| 红外发射距离 | ∠0° 时红外线发射距离（直线距离）：410cm <br/>∠90° 时红外线发射距离：66cm<br/>∠45° 时红外线发射距离：170cm |
| 休眠电流     | DC 4.2V@0.26uA                                                                                            |
| 工作电流     | IR 发射模式下：DC 4.2V@255.6mA <br/>按键模式下：DC 4.2V@165.7mA                                           |
| 工作温度     | 0 ~ 40°C                                                                                                  |
| 产品尺寸     | 84.0 x 54.0 x 19.7mm                                                                                      |
| 产品重量     | 92.3g                                                                                                     |
| 包装尺寸     | 145.7 x 95.0 x 20.7mm                                                                                     |
| 毛重         | 109.9g                                                                                                    |

## 操作说明

### 进入下载模式

如果要进入下载模式，请将 Cardputer 侧面的开关键置于`OFF`状态，然后在开机前按住`G0`按键，在设备后通电后释放，之后设备将进入下载模式。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/cardputer%20(2).gif" width="30%" />

### 充电注意事项

Cardputer 充电时，请将电源开关切换至`ON`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/K132-01.jpg" width="60%" />

## 原理图

- [Cardputer 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer.pdf)
- [Cardputer Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5cardputer_Base.pdf)
- [Stamp-S3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5cardputer_Base_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2_sch_01.png">
</SchViewer>

## 管脚映射

### SPM1423 MIC

| ESP32-S3FN8 | G46 | G43 | 3.3V | GND |
| ----------- | --- | --- | ---- | --- |
| SPM1423     | DAT | CLK | VCC  | GND |

### microSD Socket

| ESP32-S3FN8    | G12 | G14  | G40 | G39  |
| -------------- | --- | ---- | --- | ---- |
| microSD Socket | CS  | MOSI | CLK | MISO |

### ST7789V2 & RGB LED

| ESP32-S3FN8 | G38     | G33 | G34 | G35 | G36 | G37 |
| ----------- | ------- | --- | --- | --- | --- | --- |
| ST7789V2    | DISP_BL | RST | RS  | DAT | SCK | CS  |
| RGB LED     | VDD     |     |     |     |     |     |

### Keyboard & Battery Detect

| ESP32-S3FN8         | G10 | G7/G6/G5/G4/G3/G15/G13 | G11/G9/G8 |
| ------------------- | --- | ---------------------- | --------- |
| Battery Detect(ADC) | ADC |                        |           |
| 74HC138             |     | Y7~Y0                  | A2/A1/A0  |

### Speaker & IR

| ESP32-S3FN8      | G41  | G42   | G43   | G44 |
| ---------------- | ---- | ----- | ----- | --- |
| NS4168 (Speaker) | BCLK | SDATA | LRCLK |     |
| IR               |      |       |       | TX  |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-401ac270-d997-4164-ae79-d28be7a3dfaf.png" width="100%" />

## 结构文件

- [Cardputer 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K132_Cardputer/Structures)

## 数据手册

- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lcd/ST7789V2_SPEC_V1.0.pdf)

## 软件开发

### Arduino

- [Cardputer Arduino 快速上手](/zh_CN/arduino/m5cardputer/program)
- [Cardputer Arduino 驱动库](https://github.com/m5stack/M5Cardputer)

### UiFlow2

- [Cardputer UiFlow2 快速上手](/zh_CN/uiflow2/cardputer/program)

### PlatformIO

```bash
[env:m5stack-cardputer]
platform = espressif32@6.7.0
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1

lib_deps =
    M5Cardputer=https://github.com/m5stack/M5Cardputer
```

### ESP-IDF

- [Cardputer 出厂固件](https://github.com/m5stack/M5Cardputer-UserDemo)

### Easyloader

| Easyloader                     | 下载链接                                                                                                     | 备注 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---- |
| Cardputer User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/Cardputer.exe) | /    |

## 相关视频

- Cardputer 介绍片

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/K132%20Cardputer.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
    <div class="video-iframe">
      <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009414505683&bvid=BV1cAWSebEfC&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
    </div>
  </template>
  <template #tab-Youtube>
    <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/Kz3LPUdRwhQ?si=PodUTxrDKkZbksQB" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Cardputer 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5cardputer_compare?select=K132)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
