# Cardputer v1.1

<span class="product-sku">SKU:K132-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_15.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_16.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_17.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_17.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132-V11.webp">
</PictureViewer>

## 描述

**Cardputer v1.1** 是一款面向工程师的高性能卡片电脑，在原有 Cardputer 的基础上实现了全面升级。新版产品采用全新的 **Stamp-S3A** 主控，并针对核心模组天线与按键进行了优化，从而显著提升了系统稳定性与用户操作体验。
在控制交互方面，产品配置了 **56 按键**键盘和 1.14 寸 **TFT** 屏幕，实现高效的显示与操作；板载 SPM1423 数字 MEMS **麦克风**支持录音及唤醒功能，并通过腔体**喇叭**输出音频；同时，红外发射管提供对外**红外**控制交互能力。
扩展功能上，内置 Grove 接口便于自定义传感器扩展；存储方面配备了 Micro **SD** 卡槽，方便扩容存储空间。供电系统采用内部 120mAh 与底座 1400mAh **锂电池**供电方案，并集成了锂电池充电及升压降压电路，大幅提升续航能力。结构设计上，底座配有磁铁实现金属吸附，且兼容乐高孔扩展。
该产品适用于工程师快速功能验证、工业控制、家居控制系统等多种应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5cardputer/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Cardputer v1.1 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/cardputer/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Cardputer v1.1 设备 |

## 注意事项

- LCD 与 RGB LED 使用注意事项：由于 RGB 与 LCD 背光共用电源，当 LCD 背光亮度低于 100% 时，RGB 无法正常供电，请在背光亮度全开的状态下使用 RGB 功能。

## 产品特性

- Stamp-S3A 微控制器
- 56 按键键盘
- 1.14 寸 TFT 屏幕
- 腔体喇叭和 SPM1423 数字 MEMS 麦克风
- 红外发射管用于红外控制交互
- HY2.0-4P 接口
- microSD 卡槽
- 内置 120mAh 和底座中的 1400mAh 锂电池
- 底座带有磁铁
- 兼容乐高孔扩
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Cardputer V1.1
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- 快速功能验证和原型设计
- 工业控制和自动化
- 家居控制系统
- 数据采集和传感器监测
- 嵌入式系统开发和学习
- 无线通信和物联网 (IoT) 项目

## 规格参数

| 规格         | 参数                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| SoC          | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz                                                                 |
| USB          | USB OTG, USB Serial/JTAG                                                                                 |
| Flash        | 8MB                                                                                                      |
| Wi-Fi        | 2.4 GHz Wi-Fi                                                                                            |
| 外部存储扩展 | microSD                                                                                                  |
| 键盘         | 56 按键 (4 x 14)                                                                                         |
| 按键         | 1 x 复位按键 + 1 x 用户按键                                                                              |
| Grove        | 1 x HY2.0-4P                                                                                             |
| 电池容量     | 120mAh+1400mAh（底座中）                                                                                 |
| 屏幕         | ST7789V2@1.14 Inch,240 x 135px                                                                           |
| 腔体喇叭     | 8Ω@1W<br/>I2S@NS4168                                                                                     |
| 麦克风       | MEMS 麦克风 @SPM1423                                                                                     |
| 红外发射距离 | ∠0° 时红外线发射距离 (直线距离)：410cm <br/>∠90° 时红外线发射距离：66cm<br/>∠45° 时红外线发射距离：170cm |
| 休眠电流     | DC 4.2V@0.15uA                                                                                           |
| 工作电流     | IR 发射模式下：DC 4.2V/148.07mA <br/>按键模式下：DC 4.2V/138.93mA                                        |
| 工作温度     | 0 ~ 40°C                                                                                                 |
| 产品尺寸     | 84.0 x 54.0 x 19.7mm                                                                                     |
| 产品重量     | 90.0g                                                                                                    |
| 包装尺寸     | 145.7 x 95.0 x 20.7mm                                                                                    |
| 毛重         | 106.8g                                                                                                   |

## 操作说明

### 进入下载模式

如果要进入下载模式，请将 Cardputer v1.1 侧面的开关键置于`OFF`状态，然后在开机前按住`G0`按键，在设备后通电后释放，之后设备将进入下载模式。

 <img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/cardputer%20(2).gif" width="30%" />

### 充电注意事项

Cardputer v1.1 充电时，请将电源开关切换至`ON`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132-V11_21.jpg" width="60%" />

### 拆除注意事项

如果需要拆除面板上的 Stamp-S3A 的时候，务必小心背面的 FPC 线和 connector，轻轻拔起，否则容易损坏屏幕连接的座子。可参考[Cardputer Accessory Kit](/zh_CN/accessory/Cardputer%20Accessory%20Kit)中的操作视频。

## 原理图

- [Cardputer V1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/Sch_M5Cardputer.pdf)
- [Cardputer V1.1 Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/M5Cardputer_Base.pdf)
- [Stamp-S3A 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/Sch_M5Cardputer_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/Sch_M5Cardputer_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/M5Cardputer_Base_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png">
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

- [Cardputer v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K132-V11_Cardputer_v1.1/Structures)

## 数据手册

- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lcd/ST7789V2_SPEC_V1.0.pdf)

## 软件开发

### Arduino

- [Cardputer v1.1 Arduino 快速上手](/zh_CN/arduino/m5cardputer/program)
- [Cardputer v1.1 Arduino 驱动库](https://github.com/m5stack/M5Cardputer)

### UiFlow2

- [Cardputer v1.1 UiFlow2 快速上手](/zh_CN/uiflow2/cardputer/program)

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

- [Cardputer v1.1 出厂固件](https://github.com/m5stack/M5Cardputer-UserDemo)

### Easyloader

| Easyloader                          | 下载链接                                                                                                     | 备注 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Cardputer v1.1 User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/Cardputer.exe) | /    |

## 相关视频

- Cardputer v1.1 产品介绍与案例展示

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

::compare-table
| 产品对比项             | [Cardputer v1.1](/zh_CN/core/Cardputer%20V1.1)<br/>![Cardputer v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1127/K132_v11_04.webp) | [Cardputer](/zh_CN/core/Cardputer)<br/>![Cardputer](https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-a02d6727-4fa1-4b38-90e6-75e401d507de.webp) |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 核心模组               | Stamp-S3A                                                                                                                                    | StampS3                                                                                                                                                                 |
| RGB LED 控制逻辑       | RGB LED 与屏幕背光共用电源，控制逻辑经过优化                                                                                                 | 通电即供电                                                                                                                                                              |
| 天线设计               | 优化天线设计，信号接收更佳                                                                                                                   | 常规天线设计                                                                                                                                                            |
| StampS3 模组 Boot 按键 | 优化按键手感，按键采用 4.0 x 3.0 x 2.0mm 规格                                                                                                | 按键规格 2.6 x 1.6 x 0.55mm                                                                                                                                             |
| 功耗表现               | 经过优化，实现更低功耗                                                                                                                       | 常规设计                                                                                                                                                                |
::

如需对比 Cardputer 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5cardputer_compare?select=K132-V11)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                        |
| -------- | ------------------------------- |
| 2025.8.2 | 按键操作力由 260gf 变更为 160gf |
| /        | 首次发售                        |
