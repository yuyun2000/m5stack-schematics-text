# Unit ExtEncoder

<span class="product-sku">SKU:U161</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-d6cf0ce3-d72b-4638-b3c3-3181eeb7cd36.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-ae5618c3-38aa-4048-a93d-f4ecbe5c0fee.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-98caf964-42de-4b2e-85b4-f11b8314e32b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-b26ce91a-bb07-4184-8584-65823bf9f0ef.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-f2dd14da-aa18-47ee-a961-8b020a0e7dfd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-ba7871a4-e141-45fc-96c6-406aac6d1bcc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-f048fc71-2b2c-4c7a-b459-fb67b0abeb31.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-78613d61-e762-4fff-a001-0a67edaab86a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/img-70ad0a8a-b326-4cfc-80a9-0cba659479e5.webp">
</PictureViewer>

## 描述

**Unit ExtEncoder** 是一个用于 外接旋转编码器 的采集单元，支持 AB/ABZ 信号输入，内采用 STM32F030 主控集成编码器信号采集和解码固件，用户可通过 I2C 读取操作直接获取编码数值，适用于例如机器人臂的位置控制、工业自动化领域的自动化切割、计米轮等。

## 产品特性

- 支持外接旋转编码器的信号采集
- 支持 AB/ABZ 信号输入
- 内置 STM32F030 主控，集成编码器信号采集和解码固件
- 可通过 I2C 读取操作直接获取编码数值

## 包装内容

- 1 x Unit ExtEncoder
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 × VH2.54-5P

## 应用场景

- 计米应用
- 编码器
- 自动化切割

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| MCU          | STM32F030F4P6         |
| 采样精度     | 12 位                 |
| 信号输入类型 | AB/ABZ                |
| 通信接口     | I2C 通信 @ 0x59       |
| 产品尺寸     | 32.0 x 24.0 x 10.7mm  |
| 产品重量     | 5.0g                  |
| 包装尺寸     | 138.0 x 93.0 x 11.7mm |
| 毛重         | 12.2g                 |

## 原理图

- [Unit ExtEncoder 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/616/SCH_UNIT_EXTEncoder.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/616/SCH_UNIT_EXTEncoder_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ExtEncoder

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ExtEncoder%20Unit/model%20size.jpg" width="100%" />

## 数据手册

- [STM32F030F4P6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)

## 软件开发

### Arduino

- [Unit ExtEncoder Arduino 驱动库](https://github.com/m5stack/M5Unit-ExtEncoder)

### UiFlow1

- [Unit ExtEncoder UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ext_encoder)

### UiFlow2

- [Unit ExtEncoder UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/extencoder.html)

### 内置固件

- [Unit ExtEncoder 内置固件](https://github.com/m5stack/M5Unit-ExtEncoder-Internal-FW)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ExtEncoder Unit/arduinoCase-1683862277316pinmap.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113089005486411&bvid=BV1MdHSeNE3g&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/wRS9A5Hi1Dc?si=c8yxQqBHHVSv6Aqi" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
