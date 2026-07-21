# NanoH2

<span class="product-sku">SKU:C149</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-main-pictures-11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-weight.jpg">
</PictureViewer>

## 描述

**NanoH2** 是 M5Stack 开发套件系列中一款超小型的 IoT 开发板。搭载 ESP32-H2FH4S 作为 SoC ，具备安全启动与 Flash 加密等硬件安全机制，集成 IEEE 802.15.4 无线通信功能，支持 Zigbee、Thread 以及基于 Thread 的 Matter 互联协议。硬件上集成 LED、IR 红外发射、RGB、Grove 接口、USB Type-C 和用户按键，Grove 接⼝能够灵活扩展多种 M5 设备，为开发者提供了丰富的硬件拓展可能性，适配各类轻量化物联网场景的功能拓展需求，可应用于智能家居、工业控制、低功耗无线通信节点等场景，以及各类基于 IEEE 802.15.2 的低功耗物联网终端的开发。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://static-cdn.m5stack.com/resource/docs/static/assets/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5nanoh2/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 NanoH2 设备。 |

## 产品特性

- 支持 Zigbee 和 Thread，Matter 无线协议
- 内置 LED、IR 红外发射以及 RGB
- 配备 Grove 口，支持多种外设扩展
- USB Type-C 接口，支持供电与编程
- 尺寸小巧
- 开发平台
  - Arduino
  - ESP-IDF

## 包装内容

- 1 x NanoH2

## 应用场景

- 智能家居
- 工业控制
- 消费电子产品
- 低功耗无线通信节点

## 规格参数

| 规格               | 参数                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC                | ESP32-H2FH4S@RISC-V 32 位单核，主频 96 MHz                                                                                                                                 |
| Flash              | 4MB                                                                                                                                                                        |
| RGB                | WS2812                                                                                                                                                                     |
| 通信协议           | IEEE 805.15.4 （包括 Zigbee 3.0，Thread 1.4，Matter）                                                                                                                      |
| OpenThread 拉距    | 最大距离 225m，丢包率 0%                                                                                                                                                   |
| IR 遥控参数        | ∠0° 时红外线发射距离 395CM<br/>∠45° 时红外线发射距离 70CM<br/>∠90° 时红外线发射距离 10CM                                                                                   |
| Grove 最大带载能力 | DC 4.43V@2A (5min、25.2℃)                                                                                                                                                  |
| 工作功耗           | IEEE 805.15.4 无线通信：发送功耗：DC 5V@18.68mA / 接收功耗：DC 5V@18.82mA <br> 红外遥控：DC 5V@6.80mA <br> RGB （白色）：DC 5V@10.79mA <br> LED：DC 5V@12.34mA（最大亮度） |
| 产品尺寸           | 23.5 x 12.0 x 9.5mm                                                                                                                                                        |
| 产品重量           | 2.6g                                                                                                                                                                       |
| 包装尺寸           | 100.6 x 80.0 x 10.5mm                                                                                                                                                      |
| 毛重               | 10.8g                                                                                                                                                                      |

## 操作说明

### 进入下载模式

烧录程序需要进入下载模式：按住按键 GPIO9，然后接上数据线即可进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/nanoH2-download-mode.gif" width="50%" />

## 原理图

- [NanoH2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/SCH_M5NanoH2_v0.0.3_2025_08_20_17_17_26.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/SCH_M5NanoH2_v0.0.3_2025_08_20_17_17_26_page_01.png">
</SchViewer>

## 管脚映射

### IR & RGB & Button & LED

| ESP32-C6FH4 | G3  | G4        | G9     | G10        | G11     |
| ----------- | --- | --------- | ------ | ---------- | ------- |
| IR          | IR  |           |        |            |         |
| LED         |     | LED(Blue) |        |            |         |
| BUTTON      |     |           | BUTTON |            |         |
| WS2812      |     |           |        | EN(RGBPWR) | DI(RGB) |

?> RGB 灯使用注意：| 使用 RGB 功能时，需将 G10 引脚设置为高电平，以开启 RGB 供电。

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

- [NanoH2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/C125-staedddv7p.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/C125-staedddv7p_page_01.png" width="100%">

## 结构文件

- [NanoH2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C149_NanoH2/Structures)

## 数据手册

- [ESP32-H2 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/esp32-h2_datasheet_cn.pdf)

<!-- 英文版链接：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/esp32-h2_datasheet_en.pdf -->

## 软件开发

### Arduino

- [NanoH2 Arduino 快速上手](/zh_CN/arduino/m5nanoh2/program)

## 相关视频

- NanoH2 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/C149-NanoH2-video-ZH.mp4" type="video/mp4"></video>
