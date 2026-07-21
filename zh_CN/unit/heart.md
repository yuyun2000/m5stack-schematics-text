# Unit Heart

<span class="product-sku">SKU:U029</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_06.webp">
</PictureViewer>

## 描述

**Unit Heart**是一款血氧心率传感器。集成 **MAX30100**，提供完整的脉搏血氧仪和心率传感器系统解决方案。这是一款非插入式的血氧心率传感器，集成了两个红外发光二极管和一个光检测器。其检测原理是通过红外 LED 灯照射，检测携带氧气和非携带氧气的红血球数量比例，从而得到血氧含量。

**测试方式：程序运行后，将手指放置在检测区域。**

**Heart Unit 通过 I2C 协议与 Core 进行通信，I2C 地址：0x57**

## 产品特性

- 可编程采样率和 LED 电流，以节省功耗
- 超低关断电流 (0.7µA，典型值)
- 高测量性能
- 高采样率
- 内置温度传感器校准
- 快速数据输出
- 血氧浓度检测、心率检测
- 2 x LEGO 兼容孔
- 软件开发平台: Arduino

## 包装内容

- 1 x Unit Heart
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x57      |
| 产品尺寸 | 32.0 x 24.0 x 8.0mm  |
| 产品重量 | 4.9g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 10.0g                |

## 原理图

- [Unit Heart 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/716/Unit_Heart.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/716/Unit_Heart_page_01.png" width="100%">

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/heart/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%">

## 结构文件

- [Unit Heart 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U209_Unit_Heart/Structures)

## 数据手册

- [MAX30100](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MAX30100.pdf)
- [MAX30100 lib](https://github.com/oxullo/Arduino-MAX30100)

## 软件开发

### Arduino

- [Unit Heart 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/HEART_MAX30100)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_arduino_01.webp">

- [Unit Heart Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_heart)

### UiFlow1

- [Unit Heart UiFlow1 文档](/zh_CN/uiflow/blockly/unit/heart)

### UiFlow2

- [Unit Heart UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/heart.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                            | 备注 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Heart Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Heart_UNIT_With_M5Core.exe) | /    |

### 相关视频

- 屏幕显示血氧心率传感器检测值

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Heart_UNIT.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113185927465790&bvid=BV1J9sUetEyi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/cNdnfA9QMUU?si=mU4o4OWq0VDslhkR" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
