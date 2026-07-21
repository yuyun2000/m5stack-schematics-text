# Unit AudioPlayer

<span class="product-sku">SKU:U197</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-13.webp">
</PictureViewer>

## 描述

Unit AudioPlayer 是一款自带解码的 MP3 音频播放单元，配有音频解码芯片 N9301 ，自带 microSD 卡座。该产品采用 UART 通信接口，通过配置指令实现音频播放功能，声音信号由 3.5mm 插座输出，可提供清晰的音频输出，并支持循环播放和组合播放。此产品适用于智能语音交互设备（如智能家居中控、语音导览器）、工业自动化报警系统、医疗设备语音提示终端、STEAM 教育等场景，可满足多行业对音频播放与灵活控制的需求，尤其适合需通过串口指令触发音频、集成微型化音频解决方案的嵌入式项目。

## 产品特性

- N9301 音频解码芯片
- UART 通信接口
- 3.5mm 立体声插孔
- 支持 MP3 和 WAV 音频格式
- 支持 FAT16 / FAT32 文件系统
- 最大支持 32GB 的 microSD 卡
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit AudioPlayer
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能语音交互设备（如智能家居中控、语音导览器）
- 工业自动化报警系统
- 医疗设备语音提示终端
- STEAM 教育

## 规格参数

| 规格         | 参数                                                                              |
| ------------ | --------------------------------------------------------------------------------- |
| 音频解码芯片 | N9301                                                                             |
| 存储接口     | microSD 卡槽                                                                      |
| 通信方式     | UART 串口通信 波特率默认: 9600bps@8N1                                             |
| 音频输出接口 | 3.5mm 立体声插孔                                                                  |
| 功耗         | 工作功耗：DC 5.01V@25.17mA；待机功耗：DC5.01V@7.33mA；休眠功耗：DV 5.02V@871.24uA |
| 产品尺寸     | 48.0 x 24.0 x 8.0mm                                                               |
| 产品重量     | 6.9g                                                                              |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                                                              |
| 毛重         | 12.8g                                                                             |

## 操作说明

\#> 初始化注意事项 | Unit AudioPlayer 上电前，需先插入 microSD 卡，否则将无法正常初始化。

## 原理图

[Unit AudioPlayer 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/Unit_AudioPlayer_U197_page_01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/Unit_AudioPlayer_U197_page_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P   | Black   | Red   | Yellow    | White     |
| ---------- | ------- | ----- | --------- | --------- |
| PORT.C     | GND     | 5V    | UART_RX   | UART_TX   |
::

## 尺寸图

[Unit AudioPlayer 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/unitaudioplayer.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197_unitaudioplayer_page_size_01.png" width="100%">

## 软件开发

### UiFlow2

- [Unit AudioPlayer UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/audioplayer.html)

### Arduino

- [Unit AudioPlayer Arduino 教程](/zh_CN/arduino/projects/unit/unit_audioplayer)
- [Unit AudioPlayer Arduino 驱动库](https://github.com/m5stack/M5Unit-AudioPlayer)

### 通信协议

- [Unit AudioPlayer UART 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/Unit-AudioPlayer-Protocol-CN.pdf)

## 相关视频

Unit AudioPlayer 产品介绍以及案例展示

<video class="video-container" controls><source src="
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1155/U197-Unit-AudioPlayer.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114781390376910&bvid=BV1uC3WzhEc6&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/RH5ocvx8yCM?si=LKS4ru0GTTeO11du" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
