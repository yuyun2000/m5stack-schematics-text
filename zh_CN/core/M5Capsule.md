# Capsule

<span class="product-sku">SKU:K129</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Capsule/4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-2456a4fc-6a0c-4dcd-9998-ddfee4d62674.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-0100484c-ceff-4535-ae3d-d100ec29b9ba.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-41307d5a-3458-4ae0-8f88-c25d9aeafeac.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-87ba2e7b-62bb-484b-a504-8c7be28cfe31.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-3adcab97-5c42-4498-8728-f8e0d41b1799.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-b29adf1c-1774-49fb-8895-8d0f73713a0c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-b75490b8-6642-451d-a653-910b7a5e4768.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-fb90adcc-1bf4-4101-8565-3cfcf5b8751a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-f45c787e-77fe-4c02-a660-ebf9d11f910c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-c9ebe579-3de2-4b6f-9bdc-4318c933e68a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-c96df413-9f9c-411f-9162-b0384f4a5f54.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/K129-weight.jpg">
</PictureViewer>

## 描述

**Capsule** 是一款以 **Stamp-S3** 作为核心控制器的多功能嵌入式开发平台，汇集了传感器、供电、存储和控制等关键功能。它内置了高性能的 BMI270 **IMU**，支持精确的运动追踪和姿态控制，同时具备 SPM1423 **麦克风**传感器，可进行录音、声音识别和唤醒，以及**红外传感器**用于遥控。供电方面，平台内置 250mAh **电池**并支持可外扩电池，确保设备长时间运行。存储数据方面， **microSD 槽**扩展了存储容量，用于数据记录和媒体存储。由 RTC8563 实时**时钟模块**提供高精度的时间和日期信息，还支持定时唤醒实现低功耗功能。此外，**蜂鸣器**提供音频反馈，而 **Proto 排母**提供额外的可扩展性，可连接自定义传感器和扩展板，以满足各种项目需求。结构方面，内嵌 4 个磁铁和 2 个 M3 螺丝孔，可以用于吸附，增加了使用的场景。该产品适用于构建物联网、嵌入式系统和传感器应用，智能设备的数据采集系统等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5capsule/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Capsule 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5capsule/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Capsule 设备 |

## 产品特性

- 多功能性：集合 IMU、MIC、红外、存储、时钟、蜂鸣器和 Proto 拓展等功能
- 灵活的扩展性：通过 Proto 排母和 microSD 卡槽，Capsule 提供了可扩展性，可连接自定义传感器和扩展板，满足特定项目需求。
- 声音识别和音频处理：SPM1423 麦克风传感器支持声音识别、录音和唤醒功能，适用于语音控制和音频分析。
- 姿态控制和运动追踪：BMI270 IMU 提供了精确的姿态控制和运动追踪功能，适用于虚拟现实和游戏控制等应用。
- 时间及低功耗管理：RTC8563 实时时钟模块支持高精度的时间和日期信息，以及定时唤醒功能，适用于时间戳和自动控制任务。
- 数据采集和存储：microSD 卡槽扩展了存储容量，用于数据记录和事件记录，适用于大规模数据采集。
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Capsule

## 应用场景

- 物联网 (IoT) 应用
- 嵌入式系统开发
- 声音识别和音频处理
- 姿态控制和运动追踪
- 时间戳和定时任务
- 数据采集和存储
- 智能设备和原型开发

## 规格参数

| 规格           | 参数                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| SoC            | ESP32-S3FN8                                                                                                 |
| Flash          | 8MB                                                                                                         |
| 六轴姿态传感器 | BMI270 <br/>I2C 地址：0x69                                                                                  |
| MEME 麦克风    | SPM1423                                                                                                     |
| 时钟芯片       | BM8563<br/>I2C 地址：0x51                                                                                   |
| 电池容量大小   | 250mAh                                                                                                      |
| 红外遥控距离   | ∠180° 时红外线发射距离 (直线距离)：330CM <br/>∠90° 时红外线发射距离：48CM <br/>∠45° 时红外线发射距离：134CM |
| 休眠电流       | 电池供电 DC 4.2V@35uA                                                                                       |
| 工作电流       | 电池供电 DC 4.2V@144mA                                                                                      |
| 产品尺寸       | 40.0 x 24.0 x 16.2mm                                                                                        |
| 产品重量       | 18.6g                                                                                                       |
| 包装尺寸       | 99.2 x 63.1 x 17.4mm                                                                                        |
| 毛重           | 26.8g                                                                                                       |

## 操作说明

### 开关机操作

- 开机：可通过按 "WAKE" 按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G46) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入休眠状态。
- 关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD (G46)=0，即实现断电关机。

### 进入下载模式

进入下载模式请在开机的时候按 StampS3 上的 G0 按键。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Capsule/capsule%20(2).gif" width="30%" />

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/IMU-Capsule.jpg" width="70%">

## 原理图

- [Capsule 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_02.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/K129_CAPSILE-pin-sticker.png" width="40%" />

### Capsule Bus

::m5-bus-table
| FUNC | PIN   | LEFT | RIGHT | PIN     | FUNC    |
| ---- | ----- | ---- | ----- | ------- | ------- |
|      | G1    | 1    | 2     | 5V_OUT  |         |
|      | G3    | 3    | 4     | VBAT_IN |         |
|      | G5    | 5    | 6     | WAKE    |         |
|      | G7    | 7    | 8     | 3V3     |         |
|      | G9    | 9    | 10    | G43     | UART_TX |
|      | GND   | 11   | 12    | G44     | UART_RX |
|      | 5V_IN | 13   | 14    | EN      |         |
|      | G13   | 15   | 16    | Boot    |         |
|      | G15   | 17   | 18    | GND     |         |
::

### 功能外设

| Capsule      | G10 | G8  | G40 | G41 | G4    | G42    | G2     |
| ------------ | --- | --- | --- | --- | ----- | ------ | ------ |
| BMI270(0x69) | SCL | SDA |     |     |       |        |        |
| BM8563(0x51) | SCL | SDA |     |     |       |        |        |
| SPM1423      |     |     | CLK | DAT |       |        |        |
| IR           |     |     |     |     | IR_TX |        |        |
| Wake Button  |     |     |     |     |       | Button |        |
| Buzzer       |     |     |     |     |       |        | Signal |

### microSD

| Capsule | G11 | G12  | G14 | G39  |
| ------- | --- | ---- | --- | ---- |
| microSD | CS  | MOSI | CLK | MISO |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G13    | G15   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Capsule/img-d0063962-c4a3-4f3a-8ce1-b0ebcc998220.png" width="100%" />

## 结构文件

- [Capsule 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K129_Capsule/Structures)

## 数据手册

- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)

## 软件开发

### Arduino

- [Capsule Arduino 快速上手](/zh_CN/arduino/m5capsule/program)
- [Capsule Arduino 支持库文件](https://github.com/m5stack/M5Unified)

### UiFlow2

- [Capsule UiFlow2 快速上手](/zh_CN/uiflow2/m5capsule/program)

## 相关视频

- Capsule 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Capsule/M5Capsule%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009330488467&bvid=BV1nPWSeoEJE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/LEAsN6MnNeI?si=CA58mbmvTqDOFKB_" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<!-- <TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009330488467&bvid=BV1nPWSeoEJE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Rnx3sDPfTCc?si=wWvSOBb2EepEGBJz" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel> -->

<!-- <TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1455802445&bvid=BV1xi421e7ph&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/DgZreVxqrv8?si=3W8ZvcVByyIKZFMY" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel> -->
