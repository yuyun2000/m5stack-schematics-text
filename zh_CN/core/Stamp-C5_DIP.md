# Stamp-C5 DIP

<span class="product-sku">SKU:S016-DIP</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_weight.jpg">
</PictureViewer>

## 描述

**Stamp-C5 DIP** 是一款基于乐鑫 ESP32-C5HF4 的高集成度无线连接模组，面向需要高效、稳定通信的物联网应用。其支持 2.4 & 5 GHz 双频 Wi-Fi 6、BLE 5 以及 IEEE 802.15.4（Zigbee、Thread）多协议连接，可满足设备在不同网络场景下的接入需求。模组采用 RISC-V 32 位单核处理器，主频最高 240MHz，板载 4MB Flash，并集成 USB Type-C、电池供电接口、FPC 扩展接口与 IPEX-1 天线座等硬件资源；整体采用 2.54mm 焊盘间距设计，配备 2 个 2.54-7P 标准排针，便于快速接入各类外设与功能扩展。在保证连接性能与安全性的同时，能够帮助开发者更高效地完成原型验证与产品落地。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stampc5/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Stamp-C5 DIP。 |

## 产品特性

- ESP32-C5HF4 核心主控
  - RISC-V 32 位单核处理器，主频高达 240MHz
  - 4MB Flash
- 无线连接能力
  - 2.4 & 5 GHz 双频 Wi-Fi 6
  - BLE 5
  - IEEE 802.15.4（Zigbee、Thread）
- 接口与硬件设计
  - USB Type-C
  - DC 3.7V 电池供电接口
  - 2.54mm 焊盘间距
  - IPEX-1 天线座
  - 背部 FPC 0.5mm-12P 接口
  - SGM40567-4.2XG/TR 充电 IC
  - 2.4 & 5 GHz 天线复用
- 状态指示灯
  - RED：充电指示灯（充电时闪烁；充满后灯灭）
  - BLUE：G28 / BOOT 指示灯

## 包装内容

- 1 x Stamp-C5 DIP
- 2 x 2.54-7P 排针

## 应用场景

- 双频 Wi-Fi 6 物联网设备
- Zigbee / Thread 边缘节点
- 低功耗无线传感设备

## 规格参数

| 规格          | 参数                                                                                                                                                                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC           | ESP32-C5HF4 @ RISC-V 32 位单核处理器，主频高达 240MHz                                                                                                                                                                        |
| SRAM          | 384KB                                                                                                                                                                                                                        |
| Flash         | 4MB                                                                                                                                                                                                                          |
| Wi-Fi         | 2.4 & 5 GHz 双频 Wi-Fi 6                                                                                                                                                                                                     |
| BLE           | BLE 5                                                                                                                                                                                                                        |
| IEEE 802.15.4 | 支持 Zigbee、Thread                                                                                                                                                                                                          |
| USB 接口      | USB Type-C                                                                                                                                                                                                                   |
| 电池供电接口  | DC 3.7V                                                                                                                                                                                                                      |
| 天线接口      | IPEX-1                                                                                                                                                                                                                       |
| 双频段双工器  | LFD182G45DCHD481（2.4 & 5 GHz 共用天线）                                                                                                                                                                                     |
| 充电 IC       | SGM40567-4.2XG/TR                                                                                                                                                                                                            |
| 状态指示灯    | 2 x LED（RED：充电；BLUE：G28 / BOOT）                                                                                                                                                                                       |
| GPIO 引出     | 总计 19x GPIO（焊盘 11x GPIO + FPC 8x GPIO）                                                                                                                                                                                 |
| 焊盘 GPIO     | G1、G2、G3、G4、G5、G6、G7、G8、G9、G10、G28                                                                                                                                                                                 |
| FPC GPIO      | G23、G0、G24、G25、G26、G27、G11、G12                                                                                                                                                                                        |
| 焊盘间距      | 2.54mm                                                                                                                                                                                                                       |
| 背部扩展接口  | FPC 0.5mm-12P                                                                                                                                                                                                                |
| 充电电流      | 约200mA                                               |
| 功耗          | 深度休眠：3.7V@13uA                                                                                                                                                                                                          |
| 产品尺寸      | 17.6 x 19.1 x 3.4mm                                                                                                                                                                                                          |
| 产品重量      | 2.4g                                                                                                                                                                                                                         |
| 包装尺寸      | 138.0 x 93.0 x 8.0mm                                                                                                                                                                                                         |
| 毛重          | 7.4g                                                                                                                                                                                                                         |

## 操作说明

### 进入下载模式

把 G28 连接 GND 后，给设备上电，进入下载模式。

## 原理图

- [Stamp-C5 DIP 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/S016_StampC5_V0.3_SCH_PDF_20260207_2026_02_07_11_34_57.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/S016_StampC5_V0.3_SCH_PDF_20260207_2026_02_07_11_34_57_page_02.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP-Stamp-C5_DIP-Pinmap.jpg" width="100%">

!>注意|连接设备 FPC 排线时，请严格检查线序是否正确对应，否则会造成硬件烧毁损坏。

| EXT.FPC | Stamp-C5 |
| :-------: | :--------: |
| Pin1    | 3V3      |
| Pin2    | 3V3      |
| Pin3    | G23      |
| Pin4    | G0       |
| Pin5    | G24      |
| Pin6    | G25      |
| Pin7    | GND      |
| Pin8    | G26      |
| Pin9    | G27      |
| Pin10   | TXD(G11) |
| Pin11   | GND      |
| Pin12   | RXD(G12) |

## 尺寸图

- [Stamp-C5 DIP 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP-Stamp-C5_DIP_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP-Stamp-C5_DIP_model_size.png" width="100%">

## PCB

- [Stamp-C5 DIP PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/S016_Stamp-C5/Footprint)
- [Stamp-C5 DIP KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp-C5.kicad_mod)

## 数据手册

- [ESP32-C5](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/esp32-c5_datasheet_cn.pdf)  <!--中英链接不同-->

## 软件开发

### Arduino

- [Stamp-C5 Arduino 快速上手](/zh_CN/arduino/m5stampc5/program)

## 相关视频

- Stamp-C5 / Stamp-C5 DIP 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/S016_StampC5_video_cn.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表              | [Stamp-C5 DIP](/zh_CN/core/Stamp-C5_DIP) ![Stamp-C5 DIP](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1259/S016-DIP_Stamp-C5_DIP_main_pictures_02.webp) | [Stamp-C5](/zh_CN/core/Stamp-C5) ![Stamp-C5](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/S016_Stamp-C5_main_pictures_02.webp) |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 是否有默认焊接 FPC 座子 | 是                                                                                                                              | 否                                                                                                                  |
| 是否配备排针            | 配备 2 x 2.54-7P 排针                                                                                                           | 否                                                                                                                  |
::

如需对比 Stamp 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5stamp_compare)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
