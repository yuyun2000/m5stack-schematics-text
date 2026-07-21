# Unit Synth

<span class="product-sku">SKU:U178</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-980d32fe-96a2-41d2-86ba-9909bb5bfba4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-b3b857cf-d615-4404-8aa5-d7f3b52609a7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-b23048d9-aa74-46ae-bc5f-5183340a8e31.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-fe511f44-85db-4d2c-aabb-189ba2d24de7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-2aa61223-8769-4734-be2d-578c18ddb2b6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-e24d0d40-7beb-41eb-b767-b6478c3ba23f.webp">
</PictureViewer>

## 描述

**Unit Synth** 是一款专为 MIDI 声音系统设计的单元，内置 SAM2695 音频合成器。它通过串口通讯接收标准 MIDI 信号，进而实现多种音频合成与处理功能，涵盖音频合成、混音、音效处理等方面。该单元支持配置多通道乐器音源输出，还能对四段 EQ、混响等参数进行调节。此外，它搭载了 NS4150B D 类功放芯片，可提供清晰的音频输出。此产品适用于即兴演奏、音乐制作工作室、电子音乐舞台以及 STEAM 教育等领域。

## 产品特性

- SAM2695 音频合成芯片
- 串口通信
- D 类功放
- MIDI 标准协议
- 支持配置多通道乐器音源输出
- 支持四段 EQ，混响等参数调节
- 编程环境：Arduino、UiFlow 等

## 包装内容

- 1 x Unit Synth
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 即兴演奏
- 音乐制作工作室
- 电子音乐舞台
- STEAM 教育

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| 音频合成芯片 | SAM2695               |
| 功放芯片     | NS4150B               |
| 音效标准协议 | MIDI                  |
| 扬声器       | 8Ω@1W                 |
| 工作温度     | 0 ~ 40°C              |
| 产品尺寸     | 48.0 x 24.0 x 16.0mm  |
| 产品重量     | 10.1g                 |
| 包装尺寸     | 138.0 x 93.0 x 17.0mm |
| 毛重         | 15.4g                 |

## 操作说明

- Unit Synth 与 MIDI 5P-DIN 连接

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Synth/ce011b38fec2df99e81a3b934adc187.png" width="60%" />

## 原理图

- [Unit Synth 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/630/Sch_Unit_Synth_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/630/Sch_Unit_Synth_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Synth

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White |
| -------- | ----- | --- | ------- | ----- |
| PORT.C   | GND   | 5V  | UART_RX | NC    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Synth/img-642ddcd8-20df-4fcf-bdfe-14cfb4991268.jpg" width="100%" />

## 数据手册

- [SAM2695](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Synth/SAM2695.pdf)

## 软件开发

### Arduino

- [Unit Synth Arduino 驱动库](https://github.com/m5stack/M5Unit-Synth)

### UiFlow1

- [Unit Synth UiFlow1 文档](/zh_CN/uiflow/blockly/unit/synth)

### UiFlow2

- [Unit Synth UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/synth.html)

## 相关视频

- Unit Synth 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Synth/U178%20Synth%20UNIT.mp4" type="video/mp4"></video>

- UiFlow2 Unit Synth

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112947540001652&bvid=BV18JeFefEZJ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/lc8_02LPxP0?si=SFnz7P_vL9Ymemw0" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
