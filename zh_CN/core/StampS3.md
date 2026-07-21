# Stamp-S3

<span class="product-sku">SKU:S007</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-964c4df6-26ff-49e0-9950-87ee1a0f3b18.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-97fc4580-17dd-4deb-8103-6823bd7e76b2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-5e82cbcd-aacc-4671-937d-120d2616d4af.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-a8f7e59f-bd84-470a-99f3-172b38d3ec6f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-4fe7e00d-6a3e-414c-bd03-805fb0089f0d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-f2652c40-0376-468d-9c2f-a9bc4fdee211.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-4aaf7195-c36f-4576-aba4-e30405195f3b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-c69bd4fd-8ca3-43b5-b8cb-aa9c6e1b941e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/StampS3/img-75d61153-2094-4567-8076-dc60a6d02c72.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/684/S007_weight.jpg">
</PictureViewer>

## 描述

**Stamp-S3** 是一款高集成度的内嵌式主控核心模组。采用乐鑫 **ESP32-S3FN8** 主控芯片，配备 **8MSPI 闪存**，搭载高性能的 Xtensa 32 位 LX7 双核处理器，主频高达 240MHz 。其内置了 **高集成度的 5V 转 3.3V 电路**、 **RGB 状态指示灯** 以及 **可编程按键** 。模块将 **ESP32-S3 上 23 个 GPIO** 引出，并以 **1.27MM/2.54MM** 间距的形式呈现，支持 **SMT、DIP 排针、DIP 排母以及飞线** 等多种使用方式。

该产品具有体积紧凑、性能强劲、扩展 IO 丰富以及低功耗等特点。此模组适用于 **内嵌主控模块的 IoT** 应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stamps3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Stamp-S3 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/stamps3/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Stamp-S3 设备。 |

## 产品特性

- ESP32-S3FN8(2.4GHz Wi-Fi)
- 最小系统板
- 多 IO 引出，支持多种应用形态 (SMT，DIP，飞线)
- 集成可编程 RGB LED 与按键
- 支持 UiFlow 图形化编程
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Stamp-S3
- 1 x HY2.0-4P 端子
- 1 x 2.54-9 排针
- 1 x 2.54-6P 排针
- 1 x 六角扳手
- 1 x 用户手册

## 应用场景

- 智能家居
- 可穿戴设备
- 医疗设备

## 规格参数

| 规格         | 参数                                                                                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC          | ESP32-S3FN8@Xtensa LX7 双核，主频高达 240MHz                                                                                                                                |
| DC-DC        | MUN3CAD01-SC                                                                                                                                                                |
| Flash        | 8MB                                                                                                                                                                         |
| Wi-Fi        | 2.4 GHz Wi-Fi                                                                                                                                                               |
| 输入电压     | 5V                                                                                                                                                                          |
| 功耗         | 睡眠模式：<br/>- USB Type-C 供电： DC 5V@400.67uA<br/>- VIN_5V 供电：DC 5V@310.89uA；<br/>待机模式：<br/>- USB Type-C 供电：DC 5V@33.04mA;<br/>- VIN_5V 供电：DC 5V@33.56mA |
| 人机交互     | 可编程物理按键 x 1，可编程 RGB LED (WS2812B-2020) x 1                                                                                                                       |
| 天线类型     | 2.4G 3D 天线                                                                                                                                                                |
| 模组资源接口 | 触摸传感器、SD/SDIO/MMC 主机控制器、SPI、SDIO/SPI 从机控制器、EMAC、电机 PWM、LED PWM、UART、I2C、I2S、GPIO、脉冲计数器                                                     |
| IO 接口 x23  | G0/G1/G2/G3/G4/G5/G6/G7/G8/G9/G10/G11/G12/G13/G14/G15/G39/G40/G41/G42/G43/G44/G46                                                                                           |
| 连接方式     | SMT/DIP (间距 2.54mm 和 1.27mm)/ 飞线                                                                                                                                       |
| IO 接口间距  | 2.54mm 和 1.27mm                                                                                                                                                            |
| lcd 接口间距 | 0.5mm@12pin 或 8pin                                                                                                                                                         |
| 工作温度     | 0 ~ 40°C                                                                                                                                                                    |
| 产品尺寸     | 24.0 x 18.0 x 4.7mm                                                                                                                                                         |
| 产品重量     | 3.0g                                                                                                                                                                        |
| 包装尺寸     | 138.0 x 93.0 x 10.5mm                                                                                                                                                       |
| 毛重         | 7.5g                                                                                                                                                                        |

## 操作说明

### 进入下载模式

如果要进入下载模式，请在开机前按住 StampS3 上的 G0 按键，通电之后再松开。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/StampS3/stamps3.gif" width="30%" />

\#> 补充说明 |- GPIO46 默认是下拉的。<br/>- PCB 背部预留了 TFT 屏幕 SPI 接口，接口 FPC 连接器规格为[8PIN](https://so.szlcsc.com/global.html?k=C2919492&hot-key=ADM3053BRWZ-REEL7)和[12PIN](https://so.szlcsc.com/global.html?k=C2919494&hot-key=ADM3053BRWZ-REEL7)。

## 原理图

- [Stamp-S3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/522/Sch_M5StampS3_v0.2_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/684/S007_PinMap_01.jpg" width="100%" />

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/StampS3/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## PCB

- [Stamp-S3 DIP KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp-S3-DIP.kicad_mod)
- [Stamp-S3 SMD KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp-S3-SMD.kicad_mod)

## 结构文件

- [Stamp-S3 KiCad 3D](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/3D/M5Stack.3dshapes/Stamp-S3.step)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)
- [MUN3CAD01-SC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/Stamp/S007%20StampS3/MUN3CAD01-SC.pdf)

## 软件开发

### Arduino

- [Stamp-S3 Arduino 快速上手](/zh_CN/arduino/m5stamps3/program)
- [Stamp-S3 Arduino 测试程序](https://github.com/m5stack/STAMP-S3/blob/main/examples/Led/Led.ino)
- [Stamp-S3 LED 测试程序](https://github.com/m5stack/STAMP-S3/blob/main/examples/Led/Led.ino)

### UiFlow2

- [StampS3 UiFlow2 快速上手](/zh_CN/uiflow2/stamps3/program)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009431218222&bvid=BV1rcWSefEfX&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/iqG21yPjaGY?si=_JN0gmwdeaipGNKf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/stamp/对比.png" width="80%">

如需对比 Stamp 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5stamp_compare?select=S007)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
