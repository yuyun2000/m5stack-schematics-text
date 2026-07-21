# Base Node

<span class="product-sku">SKU:M017</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_04.webp">
</PictureViewer>

## 描述

**Base Node**，是一款物联网智能节点底座。内置高保真音频解码芯片、麦克风、DHT12、IR 收发器、LED 灯（SK6812）等硬件资源。与 M5Core 结合使用能够支持多节点终端互联、设备控制与信息传输。

不仅如此，功能强大的 **Base Node** 同样适用于智能音频设备开发。使用 M5Core 作为控制核心，运用 EPS32 提供的 ESP - ADF 音频开发平台，能够以最全面的方式进行 Espressif Systems ESP32 芯片的音频应用开发，丰富的应用案例能够逐步指导添加新的功能，完成由简单到复杂的音频应用功能：

- 支持多种音频格式，如 MP3、AAC、FLAC、WAV、OGG、AMR、TS、EQ、Downmixer、Sonic、G.711、SPEEX 等
- 多种音频播放源：HTTP、HLS（HTTP 直播）、SPIFFS、SDCARD、A2DP - Source、A2DP - Sink、HFP 等
- 整合媒体服务，如：DLNA、WeChat、Internet Radio 等
- 语音识别、集成 Alexa、DuerOS 等在线服务

## 产品特性

- 12 个 RGB LED
- 温湿度传感器 (DHT12)
- 4 路红外发射器 (位于边缘四角),1x 红外接收器 (位于底边).
- 2 路麦克风
- HiFi 立体声编解码芯片 (24 位分辨率)
- 500mAh 锂电池

## 包装内容

- 1 x Node Module
- 1 x 固定底座
- 4 x 螺丝
    - 2 x M3x12
    - 2 x M3x18
- 1 x USB Type-C 连接线 (1m)

## 应用场景

- 物联网智能节点
- 网络收音机
- 智能音箱

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_sch_01.webp" width="80%">

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_sch_02.webp" width="80%">

## 管脚映射

| ESP32      | G0      | G13    | G5      | G2     | G34     | G21     | G22     | G25    |
| ---------- | ------- | ------ | ------- | ------ | ------- | ------- | ------- | ------ |
| Codec Chip | I2S_CLK | I2S_WS | I2S_BCK | I2S_IN | I2S_OUT | I2C_SDA | I2C_SCL | L_OUT1 |

| ESP32     | G15            | G35        | G12     | G21       | G22       |
| --------- | -------------- | ---------- | ------- | --------- | --------- |
| node base | RGBLed(SK6812) | IR_Receive | IR_Send | DHT12_SDA | DHT12_SCL |

## 数据手册

- [WM8978](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/WM8978%20_en.pdf)

## 软件开发

### ESP-IDF

- [Base Node Play MP3](https://github.com/m5stack/esp-adf/blob/master/examples/get-started/M5Node/main/play_mp3_example.c)

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_05.webp">

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201812/Node%20Module.mp4" type="video/mp4">
</video>
