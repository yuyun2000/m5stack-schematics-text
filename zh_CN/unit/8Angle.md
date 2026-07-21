# Unit 8Angle

<span class="product-sku">SKU:U154</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-b698604d-29dd-4506-b662-4752e1f03a28.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-90a7a546-2472-4f0a-8d8a-8e895963bbc3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-0a5654d0-27e6-4412-863a-c93bbb6b565f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-0429282b-d8cb-42f0-84f4-2191a6685622.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-d1261679-1f72-4615-8d83-b5bc6be59502.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-75a3647b-6ed6-44ff-8a6b-f15b6c77f0ae.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-55f9289a-53b8-4708-a0f0-86fc7566419a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-1fa89582-f023-4500-bd24-6893270d9e33.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-dad0216e-e1c3-4258-b84e-4b70cbb6d5b2.webp">
</PictureViewer>

## 描述

**Unit 8Angle** 是一款集 8 路可调电位器为一体的输入单元，内部采用 STM32F030 单片机作为采集及通信处理器，与上位机采用 I2C 通信接口。每路可调电位器对应 1 个 RGB LED 灯，另外还有一个物理拨动开关及其对应的 RGB LED 灯，内含 5V->3V3 的 DC-DC 电路。该单元可用于多通道绝对控制值的输入，对应的 RGB 灯能显示不同的状态，拨动开关可以用于多通道开关量的输入，可用作多自由度机器人或音乐均衡方面的应用。

## 产品特性

- 8 通道可调电位器
- 8 路对应可调 RGB 灯
- I2C 通讯
- 拨动开关

## 包装内容

- 1 x Unit 8Angle
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 多自由度机器人关节控制
- 音乐均衡控制方面

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 主控     | STM32F030F4P6         |
| LDO      | ME6210A33M3G          |
| RGB      | SK6812-3535           |
| 输入电压 | 5v                    |
| 通信接口 | I2C 通信 @ 0x43       |
| 产品尺寸 | 128.0 x 24.0 x 23.0mm |
| 产品重量 | 34.5g                 |
| 包装尺寸 | 131.0 x 27.0 x 27.0mm |
| 毛重     | 43.9g                 |

## 原理图

- [Unit 8Angle 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/608/SCH_UNIT_8Angle_V1.01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/608/SCH_UNIT_8Angle_V1.01_sch_01.png">
</SchViewer>

## 管脚映射

### Unit 8Angle

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-4b39398e-5590-43b9-8dfe-84eb4aec5312.png" width="100%" />

## 数据手册

- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/STM32F030F4P6.pdf)
- [LDO:ME6210A33M3G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/Unit%208Angle/ME6210A33M3G.pdf)

## 软件开发

### Arduino

- [Unit 8Angle Arduino 驱动库](https://github.com/m5stack/M5Unit-8Angle)

### UiFlow1

- [Unit 8Angle UiFlow1 文档](/zh_CN/uiflow/blockly/unit/8angle)

### UiFlow2

- [Unit 8Angle UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/angle8.html)

### 内置固件

- [Unit 8Angle 内置固件](https://github.com/m5stack/M5Unit-8Angle-Internal-FW)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/arduinoCase-1668070916820Address.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112868301277207&bvid=BV1XgvPeLEEn&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/8a6Qt6yiusg?si=Ro66MyEOw--1bxLc" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
