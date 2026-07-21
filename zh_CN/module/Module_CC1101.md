# Module CC1101

<span class="product-sku">SKU:M146</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-weight.jpg">
</PictureViewer>

## 描述

Module CC1101 是一款高性能无线通信模块。采用 E07-900M10S 模组方案 (内置 CC1101 低功耗 Sub-1 GHz 射频收发器)，工作频段为 855 ~ 925MHz，支持配置 2-FSK、4-FSK、GFSK、MSK、ASK、OOK 调制方式，提供稳定的无线数据传输功能的同时，保持较低的功耗水平。
模块采用 SPI 通信接口，同时板载拨码开关，用于灵活切换通信引脚，支持多个模块堆叠同时使用，实现功能拓展。适用于工业自动化、智能家居、自动化照明及机器人设备等无线控制应用场景。

## 产品特性

- SPI 串行通信协议
- E07-900M10S 模组 (基于 CC1101)
- 内置拨码开关切换引脚
- 可多个堆叠使用
- CC1101 低功耗 Sub-1 GHz 射频收发器
- 独立的 64 字节 RX FIFO 和 TX FIFO
- 支持 RSSI（接收信号强度指示）和 LQI（链路质量指示）
- 工作频段 855 ~ 925 MHz
- 支持 2-FSK、4-FSK、GFSK、MSK、ASK、OOK 调制方式
- 接收灵敏度：可达 -109 dBm（1.2kbps 速率）
- 休眠模式下功耗低
- 外置 SMA 天线接口
- 开发平台:
  - Arduino
  - UiFlow2

## 包装内容

- 1 x Module CC1101
- 1 x SMA 胶棒天线

## 应用场景

- 工业自动化
- 智能家居
- 自动化照明
- 机器人设备

## 规格参数

| 规格         | 参数                                                                       |
| ------------ | -------------------------------------------------------------------------- |
| 射频收发模组 | E07-900M10S 模组 (基于 CC1101)                                             |
| 工作频段     | 855 ~ 925 MHz                                                              |
| 通讯接口     | SPI                                                                        |
| 可编程比特率 | 0.6 ~ 500kbps                                                              |
| 天线         | 胶棒天线 @2.5dBi 长度: 110 x 8 mm                                          |
| 通讯距离     | 430m（频率 868MHz，BW 58kHz）                                              |
| 发射功率     | +10 dBm                                                                    |
| 接收灵敏度   | 最高 -109 dBm                                                              |
| 休眠功耗     | DC 5V@26.48uA                                                              |
| 待机功耗     | DC 5V@1.74mA                                                               |
| 工作功耗     | 接收模式：DC 5V@17.11mA<br>发送模式：DC 5V@30mA<br>休眠模式：DC 5V@26.48uA |
| 产品尺寸     | 54.0 x 63.6 x 13.1mm                                                       |
| 产品重量     | 15.8g                                                                      |
| 包装尺寸     | 134.0 x 95.0 x 15.7mm                                                      |
| 毛重         | 38.9g                                                                      |

## 原理图

- [Module CC1101 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/SCH_Module_CC1101_SCH_Main_V0.1_20241230_2025_07_04_19_47_33.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/SCH_Module_CC1101_SCH_Main_V0.1_20241230_2025_07_04_19_47_33_page_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。其中 `GD00` 和 `GD02` 可供选择的三个 IO 引脚相同，请注意选择不同的引脚，避免功能冲突。

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN              |
| -------- | ---- | ----- | --------------   |
| GND      | 1    | 2     | GD00 / GD02 (SW) |
| GND      | 3    | 4     |                  |
| GND      | 5    | 6     |                  |
| MOSI     | 7    | 8     | CSN (SW)         |
| MISO     | 9    | 10    |                  |
| SCK      | 11   | 12    |                  |
|          | 13   | 14    |                  |
|          | 15   | 16    |                  |
|          | 17   | 18    |                  |
|          | 19   | 20    | GD00 / GD02 (SW) |
| CSN (SW) | 21   | 22    | GD00 / GD02 (SW) |
| CSN (SW) | 23   | 24    | CSN (SW)         |
| HPWR     | 25   | 26    |                  |
| HPWR     | 27   | 28    | 5V               |
| HPWR     | 29   | 30    |                  |
::

## 尺寸图

- [Module CC1101 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M135-and-M146-model-size-GNSS-1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M135-and-M146-model-size-GNSS-1_page_01.png" width="100%">

## 数据手册

- [Module CC1101 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/CC1101_Datasheet.pdf)
- [E07-900M10S](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/E07-M_UserManual_CN_v1.0.pdf)

## 软件开发

### Arduino

- [Module CC1101 Arduino 驱动库](https://github.com/jgromes/RadioLib)
- [Module CC1101 Arduino 快速上手](/zh_CN/arduino/projects/module/module_cc1101)

### UiFlow2

- [Module CC1101 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/cc1101.html)

## 相关视频

- Module CC1101 产品介绍以及功能展示 <!--注意中英文视频链接不同-->

<video class="video-container" controls poster="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-video-cover-zh.jpg"><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M146-Module-CC1101-video-zh.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115524738484563&bvid=BV1B5kfBKEEj&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Hr5w7Ajny8I?si=VbAzHrZqAeWaBeOK" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
