# Atomic Voice Base

<span class="product-sku">SKU:A149</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_Atomic_Voice_Base_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/A149_weight.jpg">
</PictureViewer>

## 描述

**Atomic Voice Base** 是一款专为 M5 Atom 系列主机设计的**语音识别**底座，采用了 ES8311 单声道音频解码器、MEMS 麦克风和 NS4150B 功率放大器的集成方案。ES8311 提供 24 位音频分辨率和 16KHz ~ 64KHz 的采样率，支持 I2S 通信和高保真音频处理。具有高信噪比和数字输出功能的 MEMS **麦克风** 适用于自动语音识别，而内置 **扬声器** 确保高效的音频输出。该设备支持**全双工**通信，允许同时进行声音的发送和接收，增强了互动功能如语音识别、唤醒和录音播放等，非常适合智能家居和教育领域的应用。

## 教程 & 快速上手

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/voice_assistant/atoms3r_with_atomic_echo_base_voice_assistant) | 本教程介绍如何将 AtomS3R + Atomic Voice Base 结合，集成语音助手功能进入 Home Assistant。 |

## 产品特性

- 语音识别
- 单声道音频编解码
- MEMS 麦克风
- D 类功放
- 扬声器
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Atomic Voice Base

## 应用场景

- AI 语音识别交互系统
- 智能家居控制

## 规格参数

| 规格         | 参数                                   |
| ------------ | -------------------------------------- |
| 音频编解码器 | ES8311：24 位分辨率，采用 I2S 协议     |
| MEMS 麦克风  | MSM381A3729H9BPC, 信噪比 (SNR)：≥65 dB |
| 功率放大器   | NS4150B：D 类功率放大器                |
| 扬声器       | 2014 型腔体喇叭：1W@8Ω                 |
| 待机电流     | DC3.3V/3.36mA                          |
| 工作电流     | DC3.3V/14.84mA                         |
| 工作温度     | 0 ~ 40°C                               |
| 产品尺寸     | 24.0 x 24.0 x 14.1mm                   |
| 产品重量     | 6.5g                                   |
| 包装尺寸     | 85.0 x 65.5 x 15.0mm                   |
| 毛重         | 12.5g                                  |

## 原理图

- [Atomic Voice Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/Sch_ECHO_Base_v1.0.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/Sch_ECHO_Base_v1.0_page_01.png" width="100%">

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN  |
| --- | ---- | ----- | ---- |
|     |      | 1     | 3V3  |
| SCL | 2    | 3     | DIN  |
| SDA | 4    | 5     | LRCK |
| 5V  | 6    | 7     | DOUT |
| GND | 8    | 9     | SCK  |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/model%20size.jpg" width="100%">

## 数据手册

- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [MEMS MIC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/MEMS.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)

## 软件开发

?>MIC 采样率 | Atomic Voice Base 麦克风支持的采样率范围为 16KHz-64KHz

### 快速上手

- [OpenAI Voice Assistant For AtomS3R + Atomic Voice Base 教程](/zh_CN/guide/realtime/openai/atomic_echo_base)
- [Atomic Voice Base XiaoZhi Voice Assistant](/zh_CN/guide/realtime/xiaozhi/atomic_echo_base)
- [AtomS3R + Atomic Voice Base 语音助手](/zh_CN/homeassistant/voice_assistant/atoms3r_with_atomic_echo_base_voice_assistant)

### Arduino

- [Atomic Voice Base Arduino 驱动库](https://github.com/m5stack/M5Atomic-EchoBase)

### UiFlow1

coming soon

### UiFlow2

- [Atomic Voice Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/echo.html)

### ESP-IDF

- [Open RealtimeAPI Embedded SDK](https://github.com/m5stack/openai-realtime-embedded-sdk)

## 相关视频

- Atomic Voice Base 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/Atomic%20Echo%20Base.mp4" type="video/mp4"></video>

- OpenAI Voice Assistant For AtomS3R + Atomic Voice Base

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/OpenAI%20Voice%20Assistant%20For%20AtomS3R.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113954558839361&bvid=BV1tsNEeTEu1&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/g9F9NfFElAA?si=n2PbjudBH2tFIQph" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表        | [Atomic Voice Base](/zh_CN/atom/Atomic%20Echo%20Base) ![Atomic Voice Base](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/5.webp) | [Atom Voice](/zh_CN/atom/atomecho) ![Atom Voice](https://static-cdn.m5stack.com/resource/docs/products/atom/atomecho/atomecho_02.webp) |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 方案              | 底座 (无 SoC)                                                                                                                                                                    | 内置 SoC (ESP32-PICO-D4)                                                                                                               |
| MIC               | MSM381A3729H9BPC                                                                                                                                                                 | SPM1423                                                                                                                                |
| 功放              | NS4150B@D 类功放                                                                                                                                                                 | NS4150B@D 类功放                                                                                                                       |
| 扬声器            | 1W@8Ω                                                                                                                                                                            | 0.5W@8Ω                                                                                                                                |
| 音频采样率        | 16KHz-64KHz                                                                                                                                                                      | 8kHz-96kHz                                                                                                                             |
| 可编程 RGB / 按钮 | /                                                                                                                                                                                | SK6812                                                                                                                                 |
| 通信工作模式      | 全双工                                                                                                                                                                           | 半双工                                                                                                                                 |
::
