# Unit DMX

<span class="product-sku">SKU:U183</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/01.jpg">
</PictureViewer>

## 描述

**Unit DMX** 是一款专为 DMX-512 数据传输场景设计的通信单元，集成 CA-IS3092W 隔离式半双工 RS-485 收发器，提供高达 5kVrms 的电气隔离保障。板载 120Ω 终端电阻接入开关，可根据使用场景接入线路，以匹配信号传输线的特性阻抗，防止信号反射和失真。通过 Grove 接口，该单元能与 M5 主机进行串口通讯。设备配备 XLR-3 母头接口，方便用户连接 DMX 设备。该产品适用于舞台灯光控制、景观照明控制、调光器控制等场景。

## 产品特性

- 隔离式 RS-485 收发器 CA-IS3092W
- Grove 接口串口通讯
- 配备 XLR-3 母头接口
- 120Ω 终端电阻匹配

## 包装内容

- 1 x Unit DMX
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 舞台灯光控制
- 景观照明控制
- 彩灯控制

## 规格参数

| 规格         | 参数                                       |
| ------------ | ------------------------------------------ |
| 通讯协议     | DMX512                                     |
| 隔离收发器   | CA-IS3092W                                 |
| 隔离电压     | 5kVrms                                     |
| 数据传输速率 | 高达 500Kbps (DMX 协议固定速率：250 Kbps)  |
| 通讯协议     | RS-485，半双工                             |
| Grove 接口   | 用于 RS-485 通信和控制，串口通讯           |
| 终端电阻     | 120Ω，配置在 RS-485 总线两端，防止信号反射 |
| DMX 接口     | XLR-3 母头                                 |
| 工作温度     | 0 ~ 40°C                                   |
| 产品尺寸     | 51.6 x 24.0 x 32.0mm                       |
| 产品重量     | 14.5g                                      |
| 包装尺寸     | 138.0 x 93.0 x 33.0mm                      |
| 毛重         | 20.0g                                      |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DMX/img-a9577c01-030e-414c-a485-a37d14fa26b1.png" width="100%" />

## 管脚映射

### Unit DMX

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [CA-IS3092W Datasheet (隔离式RS485收发器) ](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/CA-IS3092W.pdf)

## 软件开发

### Arduino

- [Unit DMX Arduino 驱动库](https://github.com/m5stack/M5Unit-DMX512)
- [Unit DMX Tools Demo](https://github.com/m5stack/M5Module-DMX512/tree/master/examples/DMX512Tools)

### UiFlow1

- [Unit DMX UiFlow1 文档](/zh_CN/uiflow/blockly/unit/dmx)

### UiFlow2

- [Unit DMX UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dmx.html)

## 相关视频

- Unit DMX 产品示例介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DMX/2983aefead903db9d8f07154b6551e62.mp4" type="video/mp4" type="video/mp4"></video>

- UiFlow2 Unit DMX

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113066456910829&bvid=BV1NyHre6Ehm&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/0Ajy1_f4zMc?si=zhlkjTtWej8gIR2E" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
