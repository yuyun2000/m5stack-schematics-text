# AtomS3U

<span class="product-sku">SKU:K125</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-82d5d251-1bfd-4133-9324-404242e5acc7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-124f9a3e-8989-48e9-aded-9f2cca323b11.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-4d075660-3410-4d6a-8bca-5400b6bbc556.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-d9f0b34e-c3dc-441a-811d-7c520d4b1455.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-304bcd6a-2945-4346-b1ab-9ffc2277bf93.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-75eb069c-7e00-41d9-9f67-09474c05a7cd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-b209b0a7-76b0-4cc5-b7cd-d91d1c0f89c0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-04a23241-99a6-4f7a-9456-b26adad60c98.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3U/img-9a1857d7-9c83-48cb-a36d-9ca1901db8e7.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/K125-weight.jpg">
</PictureViewer>

## 描述

**AtomS3U** 是一款**U 盘**形态的 **ESP32-S3** 多功能开发板，采用乐鑫 ESP32-S3 主控芯片，双核 Xtensa LX7 处理器，主频 240 MHz ，自带 Wi-Fi 功能。其接口包括 USB Type-A 接口 **(支持 OTG)** ，1 个 Grove 口，6Pin@2.54mm 排母 (含 4 个 GPIO) ，外设包括 1 个 **PDM 麦克风** ，1 个**红外发射管**，1 个可编程 **RGB-LED** 。该产品可用于物联网人机交互、语音输入 / 识别 (STT) 、IO 控制等场景。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atoms3u/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomS3U 设备。 |

## 产品特性

- ESP32-S3FN8@240Mhz，Xtensa LX7，WIFI，USB-OTG
- 集成可编程 RGB LED 与按键
- 内置红外发射器
- 可扩展的引脚与 GROVE 接口
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3U

## 应用场景

- 物联网控制器
- 语音录制、云端 STT 识别

## 规格参数

| 规格              | 参数                                     |
| ----------------- | ---------------------------------------- |
| SoC               | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz |
| USB               | USB OTG, USB Serial/JTAG                 |
| Wi-Fi             | 2.4 GHz Wi-Fi                            |
| 麦克风            | SPM1423                                  |
| 接口              | USB Type-A                               |
| Grove 接口        | PORT.A                                   |
| 2.54-6P 接口      | GND/VIN_5V/G14/G17/G42/G40               |
| 麦克风灵敏度      | 94dB SPL@1KHz 典型值：-22dBFS            |
| 麦克风信噪比      | 94dB SPL@1KHz，A 加权 典型值：61.4dB     |
| 支持输入声音频率  | 100Hz ~ 10KHz                            |
| 支持 PDM 时钟频率 | 1.0 ~ 3.25MHz                            |
| RGB 灯            | WS2812                                   |
| 产品尺寸          | 53.0 x 20.0 x 10.3mm                     |
| 产品重量          | 8.5g                                     |
| 包装尺寸          | 114.2 x 65.6 x 20.6mm                    |
| 毛重              | 16.3g                                    |

## 原理图

- [AtomS3U 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/Sch_AtomS3U_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/Sch_AtomS3U_v1.0_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/K125_PinMap_01.jpg" width="100%" />

### SPM1423 - PDM

| AtomS3U | G38     | G39      | 3.3V | GND |
| ------- | ------- | -------- | ---- | --- |
| SPM1423 | MIC_CLK | MIC_DATA | VCC  | GND |

### IR & WS2812 & BUTTON

| AtomS3U | G12 | G35 | G41 |
| ------- | --- | --- | --- |
| IR      | TX  |     |     |
| WS2812  |     | DIN |     |
| BUTTON  |     |     | SW  |

### Ext Port-2.54 6P

| AtomS3U | GND | VIN_5V | G14 | G17 | G42 | G40 |
| ------- | --- | ------ | --- | --- | --- | --- |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3U/module%20size.jpg" width="100%" />

## 结构文件

- [AtomS3U 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K125_AtomS3U/Structures)

## 数据手册

- [ESP32S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/esp32-s3_technical_reference_manual_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [AtomS3U Arduino 快速上手](/zh_CN/arduino/m5atoms3u/program)
- [AtomS3U Arduino 测试程序](https://github.com/Tinyu-Zhao/M5AtomS3/tree/main/examples/AtomS3U)

### UiFlow2

- [AtomS3U UiFlow2 快速上手](/zh_CN/uiflow2/atoms3u/program)

### PlatformIO

```bash
[env:m5stack-atoms3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1555785253&bvid=BV1r1421C7WZ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uSegl6cDDMY?si=staGGMgKf-v85Dyr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
