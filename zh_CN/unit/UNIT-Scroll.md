# Unit Scroll

<span class="product-sku">SKU:U186</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/11.webp">
</PictureViewer>

## 描述

**Unit Scroll** 是一款滚轮形态的旋转编码器拓展单元。它集成了 12 位脉冲贯通轴编码器、按键输入以及 WS2812C 可编程 RGB LED。内置的 STM32F030 主控集成了编码器脉冲信号采集固件，用户通过 I2C 读取操作就能直接获取编码数值，大大简化了操作流程。该单元适用于刻度数值控制、音量调整等控制场景。

## 产品特性

- 基于 STM32 微控制器
- AB 相输出 (12 脉冲 / 转)
- 内置按键
- 多彩 WS2812C RGB LED 指示灯
- I2C 通信接口

## 包装内容

- 1 x Unit Scroll
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 工业自动化
- 智能家居
- 机器人技术
- 人机交互

## 规格参数

| 规格             | 参数                                     |
| ---------------- | ---------------------------------------- |
| MCU              | STM32F030F4P6@32 位 ARM Cortex-M0 处理器 |
| 旋转编码器       | EC10E                                    |
| 旋转编码器输出   | AB 两相正交输出                          |
| 旋转编码器脉冲数 | 12 脉冲 / 转                             |
| RGB 灯珠         | 1x WS2812C                               |
| 按键             | 1x 按键                                  |
| I2C 通讯地址     | 0x40                                     |
| 工作温度         | 0 ~ 40°C                                 |
| 产品尺寸         | 32.0 x 24.0 x 18.9mm                     |
| 产品重量         | 7.5g                                     |
| 包装尺寸         | 138.0 x 93.0 x 19.9mm                    |
| 毛重             | 12.7g                                    |

## 原理图

- [Unit Scroll 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/U186_SCH_SCH_UNIT_Scroll_V1.0_2024_07_01_18_29_10.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/U186_SCH_SCH_UNIT_Scroll_V1.0_2024_07_01_18_29_10_page_01.png">
</SchViewer>

## 管脚映射

### Unit Scroll

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### STM32F030F4P6 内部外设连接引脚

| STM32F030F4P6   | PA6 | PA7 | PA9 | PA10 | PA0 | PA5  |
| --------------- | --- | --- | --- | ---- | --- | ---- |
| Encoder         | A1  | B1  |     |      |     |      |
| I2C             |     |     | SCL | SDA  |     |      |
| WS2812C RGB LED |     |     |     |      | RGB |      |
| Button          |     |     |     |      |     | BTN1 |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-Scroll/img-4ec8cc89-5f89-401c-80a9-4e0c27c9f36e.jpg" width="100%" />

## 结构文件

- [Unit Scroll 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U186_Unit_Scroll/Structures)

## 数据手册

- [旋转编码器EC10E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/ENCODER%20EC10E.pdf)

## 软件开发

### Arduino

- [Unit Scroll Arduino 驱动库](https://github.com/m5stack/M5Unit-Scroll)

### 内置固件

- [Unit Scroll 内置固件](https://github.com/m5stack/M5Unit-Scroll-Internal-FW)

### 通信协议

<img style="width:100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/a956f5806067b326d0d8330a33710cc.png" alt="detail" />

### UiFlow2

- [Unit Scroll UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/scroll.html)

## 视频

- Unit Scroll 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/U186%20Scroll%20Unit%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- UiFlow2 Unit Scroll

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112970742958841&bvid=BV1qKe3eMEHj&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/yke5if5jCgU?si=YheqkMcsGJ-WYFuH" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare    | [Unit Scroll](/zh_CN/unit/UNIT-Scroll) ![Unit Scroll](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-Scroll/3.webp) | [Unit Encoder](/zh_CN/unit/encoder) ![Unit Encoder](https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_05.webp) | [Unit 8Encoder](/zh_CN/unit/8Encoder) ![Unit 8Encoder](https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-f58d98c0-09a8-4f57-b884-b75fee80c118.webp) |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Form               | Wheel                                                                                                                                              | Knob                                                                                                                                    | Knob                                                                                                                                                                      |
| Channels           | 1                                                                                                                                                  | 1                                                                                                                                       | 8                                                                                                                                                                         |
| Resolution         | 12 pulses/rotation                                                                                                                                 | 30 pulses/rotation                                                                                                                      | 15 pulses/rotation                                                                                                                                                        |
| Position           | AB Quadrature Output                                                                                                                               | AB Quadrature Output                                                                                                                    | AB Quadrature Output                                                                                                                                                      |
| Communication Mode | I2C (0x40)                                                                                                                                         | I2C (0x40)                                                                                                                              | I2C (0x41)                                                                                                                                                                |
::
