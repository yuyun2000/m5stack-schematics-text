# Stamp-P4

<span class="product-sku">SKU:S013</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013_main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013-weight.jpg">
</PictureViewer>

## 描述

Stamp‑P4 是一款基于 ESP32‑P4NRW32 芯片的高性能嵌入式模组。模组搭载 32‑bit RISC‑V 高性能双核处理器（360 MHz） 与 单核低功耗协处理器（40 MHz），集成 16MB Flash + 32MB PSRAM 存储组合，可稳定支撑图像处理、UI 渲染与边缘 AI 推理等复杂应用。在多媒体与人机交互层面，芯片集成 MIPI‑CSI 摄像头接口、MIPI‑DSI 高清显示接口，搭配硬件级 H.264 编码器、ISP 图像信号处理器及 PPA 像素处理加速器，可实现流畅的音视频采集、编码与图形 UI 显示。模组接口兼容 1.27mm/2.00mm 间距 SMT 封装 与 2.54mm 间距 DIP 排针 / 排母，支持 USB 2.0 OTG HS、以太网（GMAC）、SDIO 3.0 等高速通信外设，易于集成至各类 PCB 设计，帮助开发者快速完成产品原型与应用落地。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/stamp_p4/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Stamp-P4 设备。 |

## 产品特性

- ESP32‑P4NRW32 核心主控:
  - 16MB Flash
  - 32MB PSRAM
- AI 向量扩展指令集，适合边缘端 AI 识别与数据处理
- 外设接口:
  - MIPI CSI (2-lane) 摄像头接口
  - MIPI DSI (2-lane) 高清显示屏接口
  - SDIO 拓展接口 (可拓展 Stamp-AddOn C6 For P4, 快速集成 2.4GHz Wi-Fi 6)
  - RMII 以太网拓展接口
- 模组封装:
  - 1.27mm/2.00mm 间距 SMT 封装
  - 2.54mm 间距 DIP 排针 / 排母
  - 支持多种应用形态 (SMT，DIP，飞线)
- 集成 USB 过压保护设计，支持大于 6V 输入电压保护
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Stamp-P4

## 应用场景

- 智能家居
- 工业人机界面（HMI）
- 视觉采集节点
- 边缘计算设备

## 规格参数

| 规格           | 参数                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| SoC            | ESP32-P4NRW32（RISC-V 32 位高性能双核处理器 360 MHz + RISC-V 32 位单核低功耗协处理器 40 MHz）         |
| Flash          | 16MB                                                                                                  |
| PSRAM          | 32MB Octal                                                                                            |
| DC-DC          | SY8089AAAC                                                                                            |
| 过压保护       | AW32901FCR，支持大于 6V 输入电压保护                                                                  |
| 输入电压       | DC 5V                                                                                                 |
| 功耗           | 裸板运行：5V@30.76mA<br>裸板深度休眠：5V@360.84uA / 3.3V@343.90uA                                     |
| 模组资源接口   | USB、UART、I2C、RMII、GPIO、MIPI CSI、MIPI DSI                                                        |
| 邮票孔引出接口 | 44 x GPIO（G0-G39，G41，G49，G50，G52）<br>MIPI DSI（2-lane）<br>USB HOST（USB2 OTG D+/-）<br>CHIP_EN |
| 模组封装       | SMT：1.27/2.00mm<br>DIP：2.54mm                                                                       |
| BTB 拓展接口   | SDIO、MIPI CSI (2-lane)                                                                               |
| BTB 接口规格   | MIPI CSI：AXE516127D<br>SDIO：HC-PBB40C-20DS-0.4V-2.5-02                                              |
| 工作温度       | 0 ~ 40°C                                                                                              |
| 产品尺寸       | 29.8 x 22.0 x 4.3mm                                                                                   |
| 产品重量       | 2.7g                                                                                                  |
| 包装尺寸       | 138.0 x 93.0 x 7.5mm                                                                                  |
| 毛重           | 6.1g                                                                                                  |

## 原理图

- [Stamp-P4 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/SCH_Stamp-P4_2026_03_16_17_23_06.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/SCH_Stamp-P4_2026_03_16_17_23_06_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013-stamp-p4-pinmap.jpg" width="100%" />

## 尺寸图

[Stamp-P4 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013-model-size-stampp4.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/S013-model-size-stampp4_page_01.png" width="100%">

## PCB

- [Stamp-P4 PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/S013_Stamp-P4/Footprint)
- [Stamp-P4 KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp-P4.kicad_mod)

## 数据手册

- [ESP32-P4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/esp32-p4_datasheet_cn.pdf)
- [AXE616124D](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/AXE616124D.pdf)
- [HC-PBB40C-20DP-0.4V-02](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/HC-PBB40C-20DP-0.4V-02.pdf)

## 软件开发

### UiFlow2

- [Stamp-P4 UiFlow2 快速上手](/zh_CN/uiflow2/stamp_p4/program)

### Arduino

- [Stamp-P4 Arduino 快速上手](/zh_CN/arduino/m5stampp4/program)

### PlatformIO

```bash
[env:esp32p4_pioarduino]
platform = https://github.com/pioarduino/platform-espressif32.git#54.03.21
upload_speed = 1500000
monitor_speed = 115200
build_type = debug
framework = arduino
board = esp32-p4-evboard
board_build.mcu = esp32p4
board_build.flash_mode = qio

build_flags =
    -DBOARD_HAS_PSRAM
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
```

## 相关视频

- Stamp-P4 与 Stamp-AddOn C6 For P4 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1218/A172_and_S013_introduce_video_ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116327025019572&bvid=BV15g9VBaEdi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/bzAGxQxv1fQ?si=F6FNdXtr0VAh7Q0n" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
