# DinMeter

<span class="product-sku">SKU:K134</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-ae5aaf34-6458-47c7-89ee-280ec06fb542.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-d8f8f858-0614-4829-b462-d1b1c4decfab.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-a76fdd1f-9d4c-46a6-b112-ea0c2119f1dc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-852a5a75-f6b9-4ec7-8a5a-9f402b73d568.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-f6f2cf5f-8b72-49b4-8d6c-c48467810e89.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-71baa86c-292a-4905-ad68-f2733320e4ab.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-1f3aa8b5-36dd-4dd7-8359-9f13f1f399dc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-e313bbbd-0330-430b-9aee-3f8d54ba8d8f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5DinMeter/img-af3c8884-3669-4305-af73-979e32fe176f.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/K134-weight.jpg">
</PictureViewer>

## 描述

**DinMeter** 是一款采用 1/32DIN 标准的嵌入式开发板，配备 1.14 寸 ST7789 屏幕，内置带按键的旋转编码器，可精确记录旋钮位置。此外，RTC 电路，板载蜂鸣器以及按键用于设备互动和提醒唤醒等功能。供电方面，产品设计支持 DC 6 ~ 36V 直流电输入，并预留了锂电池接口和充电电路，以提供不同供电需求。此外，预留的 PORT.A 和 PORT.B 接口可方便扩展 I2C 和 GPIO 设备。该产品适用于参数测量检测、智能家居控制、物联网项目、智能穿戴、门禁、工业控制和教育创客项目等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5dinmeter/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 DinMeter 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5dinmeter/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 DinMeter 设备。 |

## 产品特性

- ST7789v2 屏幕
- Stamp-S3 作为主控
- 旋转编码器
- 宽电压输入
- 预留的 PORTA 和 PORTB 接口
- 锂电池接口 (可充电)
- 1/32DIN 标准 (45 x 22.5mm)
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x DinMeter
- 1 x 粘贴胶带
- 1 x 250mAh 聚合物锂电池
- 1 x 丝印贴纸
- 1 x DC-JACK 端子输入 (6-36V)
- 1 x 背部支架

## 应用场景

- 智能家居检测控制系统
- 门禁系统
- 工业控制
- 创客和 DIY 项目

## 规格参数

| 规格                           | 参数                                                                   |
| ------------------------------ | ---------------------------------------------------------------------- |
| SoC                            | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz                               |
| Flash                          | 8MB                                                                    |
| Wi-Fi                          | 2.4 GHz Wi-Fi                                                          |
| USB                            | USB OTG, USB Serial/JTAG                                               |
| 宽电压输入范围                 | 6 ~ 36V                                                                |
| 屏幕驱动                       | ST7789V2                                                               |
| 屏幕分辨率                     | 135 x 240                                                              |
| 充电电流                       | 100mA                                                                  |
| Grove 带载能力                 | PORT.A 带载能力 ：DC 5V/Max:220mA<br/>PORT.B 带载能力：DC 5V/Max:220mA |
| 待机电流（电池供电的待机电流） | DC4.2V@38.4uA                                                          |
| 电池座子规格                   | 1.25mm-2p                                                              |
| 供电方式                       | USB/DC 直流电源 / 电池                                                 |
| 工作温度                       | 0 ~ 40°C                                                               |
| 产品尺寸                       | 53.0 x 30.0 x 32.0mm                                                   |
| 产品重量                       | 17.6g                                                                  |
| 包装尺寸                       | 136.0 x 93.0 x 23.0mm                                                  |
| 毛重                           | 47.0g                                                                  |

## 操作说明

### 开关机操作

- 开机：可通过按 "WAKE" 按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G46) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入休眠状态。
- 关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD (GPIO46)=0，即实现断电关机。

### 进入下载模式

如果要进入下载模式，请在开机前按住 StampS3 上的 G0 按键，通电之后再松开。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/dinmeter%20(2).gif" width="30%" />

### 供电方式

提供三种供电方式：USB/DC/BAT

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/3power%20supply.png" width="50%" />

Din 尺寸标准

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/b1cdc3d710ba9431994c2ba507f4ec1.png" width="50%" />

## 原理图

- [DinMeter 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/DIN_Meter_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/DIN_Meter_v1.0_sch_01.png">
</SchViewer>

## 管脚映射

### RTC8563 & ENCODER

| ESP32-S3FN8      | G12 | G11 | G40 | G41 | G3   | G42       |
| ---------------- | --- | --- | --- | --- | ---- | --------- |
| RTC8563          | SCL | SDA |     |     |      |           |
| ENCODER          |     |     | B   | A   |      |           |
| BEEP             |     |     |     |     | beep |           |
| BUTTON (ENCODER) |     |     |     |     |      | BTN(WAKE) |

### ST7789V2

| ESP32-S3FN8 | G7  | G6  | G4  | G5   | G8    | G9  |
| ----------- | --- | --- | --- | ---- | ----- | --- |
| ST7789V2    | CS  | SCK | RS  | MOSI | RESET | BL  |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G13    | G15   |
| PORT.B   | GND   | 5V  | G2     | G1    |
::

## 尺寸图

- [DinMeter 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1211/K134-din_meter_asm_v1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1211/K134-din_meter_asm_v1_page_01.png" width="100%">

## 结构文件

- [DinMeter 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K134_DinMeter/Structures)

## 数据手册

- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [tp4057](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/tp4057.pdf)
- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lcd/ST7789V2_SPEC_V1.0.pdf)
- [Spec of external DC power connector](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/DB2EK-2.54-2P-GN-S%202.54mm%202Pin%20Green.pdf)
- [Lithium battery seat](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/1.25WT-2P.pdf)

## 软件开发

### 快速上手

- [DinMeter Arduino 快速上手](/zh_CN/arduino/m5dinmeter/program)

### Arduino

- [DinMeter Arduino 驱动库](https://github.com/m5stack/M5DinMeter)
- [DinMeter 出厂固件](https://github.com/m5stack/M5DinMeter-UserDemo)

### UiFlow2

- [DinMeter UiFlow2 快速上手](/zh_CN/uiflow2/m5dinmeter/program)

### Easyloader

| Easyloader                    | 下载链接                                                                                                            | 备注 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---- |
| DinMeter User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/DinMeter%20Demo.exe) | /    |

## 相关视频

- DinMeter 介绍以及应用

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5DinMeter/26b28d0db6cf742266c39fc651093c71.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009313711320&bvid=BV1JKWSexEvt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/_i_uhCbis1I?si=VJ1nsrN0WaMNsXxa" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<!-- <TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009313711320&bvid=BV1JKWSexEvt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/VgnBRAquaUA?si=sRjxd6BCicR7NkpG" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1855682192&bvid=BV1Bs421u7wt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/zdk4YYdTIVw?si=ArUo1C2Q9myjow6w" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel> -->
