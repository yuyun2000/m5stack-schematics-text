# Unit 8Encoder

<span class="product-sku">SKU:U153</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-f745fc18-6237-4bc8-8500-6c91ce7e2d75.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-39bbe78d-4415-4a18-92b4-4c0e34dde190.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-b1784732-4389-4ddf-8808-b4f90b6e6d00.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-f58d98c0-09a8-4f57-b884-b75fee80c118.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-d69a78f9-230b-44cc-be35-09c2b50060f9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-421a38df-45cc-478f-9501-7aba4e9fc29a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-8dd7a2f6-b40d-4782-a012-4dd6927011f2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-3f5f0005-ea48-4ab7-9dbc-4f864e935cbc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-878d09f7-aab2-4fda-a1f6-ecaab4a6cbf6.webp">
</PictureViewer>

## 描述

**Unit 8Encoder** 是一款集 8 路旋转编码器为一体的输入单元，内部采用 STM32 单片机作为采集及通信处理器，与上位机采用 I2C 通信接口。每路旋转编码器对应着 1 个 RGB LED 灯，编码器除了左右旋转，还能径向按下；另外还有一路物理拨动开关及其对应的 RGB LED 灯，内含 5V->3V3 的 DC-DC 电路。该单元可用于多通道相对控制值的输入，对应的 RGB 灯能显示不同的状态，拨动开关可以用于多通道开关量的输入，可用作多自由度机器人或音乐均衡方面的应用。

## 产品特性

- 8 通道旋转编码器
- 8 路对应可调 RGB 灯
- I2C 通讯
- 拨动开关可以用于多通道开关量的输入
- 径向按下功能
- HY2.0-4P 接口
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit 8Encoder
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 多自由度机器人关节控制
- 音乐均衡控制方面
- 多通道灯光控制

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030C8T6         |
| RGB      | WS2812C-2020          |
| 输入电压 | 5v                    |
| 通信接口 | I2C 通信 @ 0x41       |
| 按压寿命 | ＞50000 次            |
| 产品尺寸 | 128.0 x 24.0 x 25.0mm |
| 产品重量 | 43.9g                 |
| 包装尺寸 | 131.0 x 27.0 x 27.0mm |
| 毛重     | 52.7g                 |

## 原理图

- [Unit 8Encoder 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/607/SCH_UNIT_8Encoder_V1.01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/607/SCH_UNIT_8Encoder_V1.01_sch_01.png">
</SchViewer>

## 管脚映射

### Unit 8Encoder

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/img-55ebb676-2b3c-4b9a-a192-b85bf0d1a87c.png" width="100%" />

## 数据手册

- [STM32F030C8T6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/Unit%208Encoder/STM32F030C8T6.pdf)

## 软件开发

### Arduino

- [Unit 8Encoder Arduino 驱动库](https://github.com/m5stack/M5Unit-8Encoder)

### UiFlow1

- [Unit 8Encoder UiFlow1 文档](/zh_CN/uiflow/blockly/unit/8encoder)

### UiFlow2

- [Unit 8Encoder UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/encoder8.html)

### 内置固件

- [Unit 8Encoder 内置固件](https://github.com/m5stack/M5Unit-8Encoder-Internal-FW)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Encoder/arduinoCase-1668582336160map.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113382371886188&bvid=BV1LE1GYEErt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/7iQhhMxEBRE?si=WA9gcATE4Fi3runv" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
