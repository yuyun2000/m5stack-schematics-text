# Unit MIDI

<span class="product-sku">SKU:U187</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/774/U187_Weight.jpg">
</PictureViewer>

## 描述

**Unit MIDI** 是一款基于 MIDI 接口的通道控制及音频合成单元。能通过产品正面的拨选开关设置左 / 右 MIDI 端口的通断模式，Bypass 模式时左 / 右端口直通，Separate 模式时左 / 右端口分离；左 / 右 MIDI 端口同时支持标准 5 脚 DIN 接口和 3.5mm 耳机接口；Grove 端口上 TXD 连接到左 MIDI 端口信号，Grove 上 RXD 连接到内部音频合成器 SAM2695 数字输入上，借此外部的 M5 主机能通过 Grove 接口侦听或输出 MIDI 信号，也能同时输出合成的音频；音频信号采用 3.5MM 耳机插座输出。该产品适用于电子音乐创作与制作、音乐现场控制、互动音乐装置等领域。

\#> 模式说明 |**分离模式**:<br/>Unit MIDI RX (控制器的 TX 引脚) 连接至 SAM2695 合成器芯片和 OUTPUT 接口<br/>Unit MIDI TX (控制器的 RX 引脚) 连接至 INPUT，此时该引脚悬空无作用。<br/>**旁通模式**:<br/>Unit MIDI RX (控制器的 TX 引脚) 连接仅至 SAM2695 合成器芯片<br/>Unit MIDI TX (控制器的 RX 引脚) 接收 INPUT 的 MIDI 信号，此时 INPUT 和 OUTPUT 直接连通。

## 产品特性

- SAM2695 音频合成芯片
- 串口通信
- 标准 MIDI 1.0 协议 (16 通道)
- 标准 3.5 音频接口和 DIN 母座
- 光耦隔离
- Bypass/Separate 模式切换

## 包装内容

- 1 x Unit MIDI
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 电子乐器
- 乐队演出设备
- 音乐教育与研究
- 互动音乐装置

## 规格参数

| 规格          | 参数                                    |
| ------------- | --------------------------------------- |
| MIDI 处理芯片 | SAM2695                                 |
| 通信协议      | MIDI 1.0 标准协议 (16 通道)             |
| 复音数        | 64 复音 (无效果) / 38 复音 (带效果)     |
| 通信接口      | 串口通信 (UART) 波特率：31520 bps       |
| 音频输出接口  | 3x3.5mm 立体声耳机接口 + 2xDIN 5 针母座 |
| 待机电流      | DC 5V@18.59mA                           |
| 工作温度      | 0 ~ 40°C                                |
| 产品尺寸      | 48.0 x 40.0 x 25.0mm                    |
| 产品重量      | 28.2g                                   |
| 包装尺寸      | 138.0 x 93.0 x 26.0mm                   |
| 毛重          | 33.1g                                   |

## 原理图

- [Unit MIDI 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/774/SCH_UnitMIDI_B04_sch_2024_07_08_15_41_29.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/774/SCH_UnitMIDI_B04_sch_2024_07_08_15_41_29_page_01.png">
</SchViewer>

## 管脚映射

### Unit MIDI

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-MIDI/img-781316ed-8117-4315-bc6f-35cb02fac563.jpg" width="100%" />

## 数据手册

- [MIDI音频合成芯片SAM2695](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Synth/SAM2695.pdf)

## 软件开发

### Arduino

- [Unit MIDI Arduino 驱动库](https://github.com/m5stack/M5-SAM2695)
- [Unit MIDI Drum Example](https://github.com/m5stack/M5Unit-Synth/tree/main/examples/drum)
- [Unit MIDI Piano Example](https://github.com/m5stack/M5Unit-Synth/tree/main/examples/piano)

### UiFlow2

- [Unit MIDI UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/midi.html)

## 相关视频

- Unit MIDI 产品示例介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MIDI/be86fc1545b8a68f1a564380ddbed469.mp4" type="video/mp4"</video>

- UiFlow2 Unit MIDI

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113088988712934&bvid=BV1uDHSeBEYe&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/fZsOSC-k9jw?si=29F7XcjFz1aQp09-" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
