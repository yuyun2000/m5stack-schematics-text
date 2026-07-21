# AtomU

<span class="product-sku">SKU:K117</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-70ca8b36-bd91-4760-af0b-ae247bbb30b7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-382faa2f-1b7c-4a41-a9a9-b046d13f8869.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-e6df25ab-3845-45bf-bb2c-d9fe13332494.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-944b662c-3dfb-4f98-8fb7-dd7b9f571809.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-45e173cb-bac8-41b1-acc5-bcf1a63b7e43.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM U/img-9989012c-fc1b-4df3-91ec-9eba3ce0f281.webp">
</PictureViewer>

## 描述

**AtomU** 是一款非常小巧灵活的物联网语音识别开发板，采用乐鑫 **ESP32** 主控芯片，搭载 2 个低功耗 **Xtensa® 32-bit LX6** 微处理器，主频高达 **240 MHz** 。集成 USB Type-A 接口、IR 发射管、可编程 LED 灯等外设，即插即用，便于程序上传下载调试。集成 **Wi-Fi** 模块，搭配内置的数字麦克风 SPM1423 (PDM) ，可实现清晰音频录制，适用于各种物联网人机交互、语音输入识别场景 (STT) 。

## 教程 & 快速上手

learn>| ![UiFlow1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow1](/zh_CN/uiflow/m5atomu/program) | 本教程将向你介绍，如何通过 UiFlow1 图形化编程平台控制 AtomU 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atomu/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomU 设备 |

## 产品特性

- ESP32-PICO-D4(2.4GHz Wi-Fi)
- USB-A 编程 / 供电接口
- 集成可编程 RGB LED 与按键
- 机身小巧
- 内置红外发射器
- 可扩展的引脚与 GROVE 接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomU

## 应用场景

- 物联网控制器
- 语音录制、云端 STT 识别

## 规格参数

| 规格              | 参数                                  |
| ----------------- | ------------------------------------- |
| SoC               | ESP32-PICO-D4@双核处理器，主频 240MHz |
| DMIPS             | 600                                   |
| SRAM              | 520KB                                 |
| Wi-Fi             | 2.4 GHz Wi-Fi                         |
| 麦克风            | SPM1423                               |
| 麦克风灵敏度      | 94dB SPL@1KHz 典型值：-22dBFS         |
| 麦克风信噪比      | 94dB SPL@1KHz，A 加权 典型值：61.4dB  |
| 待机工作电流      | 40.4mA                                |
| 支持输入声音频率  | 100Hz ~ 10KHz                         |
| 支持 PDM 时钟频率 | 1.0 ~ 3.25MHz                         |
| 产品尺寸          | 53.0 x 20.0 x 10.3mm                  |
| 产品重量          | 8.6g                                  |
| 包装尺寸          | 114.2 x 65.6 x 20.6mm                 |
| 毛重              | 16.6g                                 |

## 原理图

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/675/Sch_AtomU_01.jpg" width="100%" />

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/675/K117_PinMap_01.jpg" width="100%" />

### SPM1423 - PDM

| ESP32-PICO-D4 | G5      | G19      | 3.3V | GND |
| ------------- | ------- | -------- | ---- | --- |
| SPM1423       | MIC_CLK | MIC_DATA | VCC  | GND |

### IR & SK6812 & BUTTON

| ESP32-PICO-D4 | G12 | G27 | G39 |
| ------------- | --- | --- | --- |
| IR            | TX  |     |     |
| SK6812        |     | DIN |     |
| BUTTON        |     |     | SW  |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G26    | G32   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/ATOM%20U/module%20size.jpg" width="80%">

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [AtomU STT 测试程序 ](https://github.com/m5stack/M5AtomU/tree/master/examples/Audio/STT)

### UiFlow1

- [AtomU UiFlow1 快速上手](/zh_CN/uiflow/m5atomu/program)

### UiFlow2

- [AtomU UiFlow2 快速上手](/zh_CN/uiflow2/atomu/program)

### PlatformIO

```bash
[env:m5stack-atom]
platform = espressif32@6.7.0
board = m5stack-atom
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### USB 驱动

> AtomU 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-02.png" width="100%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

## 相关视频

- AtomU STT Tutorial

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/ATOMU_STT_TUTORIAL_EN_480P.mp4" type="video/mp4"></video>

- STT Example

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/ATOM_U_STT.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1955779166&bvid=BV1xy411z7kW&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/5VX-CrjKkiY?si=_LOPN_gwNYxKWYPH" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=K117)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
