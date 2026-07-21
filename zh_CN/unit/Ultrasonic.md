# Unit Ultrasonic

<span class="product-sku">SKU:U098</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-91d34281-668c-41fa-9344-a4e02e1d8106.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-16d68e44-64ca-4aa4-bfa1-289932609bf5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-9b48a69a-d5b4-4858-9aee-612246d5f863.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-f0d23965-f04d-403a-b67d-3c40408cc688.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-92af735f-ce98-4e37-a93b-f67fd4c07c53.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-2660f302-e060-4d19-9507-b48c0b1edeec.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-d71639a0-41f7-4919-be98-4d8e5af952ce.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-e6f86e7d-84eb-43de-a012-663280322afc.webp">
</PictureViewer>

## 描述

**Unit Ultrasonic** 是一款超声波测距传感器单元，采用收发分体式设计。其中超声波探头的声波频率 40Khz，方向角 ±20°，精度可达 1mm，内部由 RCWL-9600 超声波测距芯片运算，通过 I2C 接口（0x57）可直接获得测量结果。测量有效距离为 30 ~ 150cm。

## 产品特性

- 分体式收发
- 有效距离 30-150cm
- 方向角范围广
- I2C 通讯，结果直接输出

## 包装内容

- 1 x Unit Ultrasonic
- 1 x PORT 连接线 (20cm)

## 应用场景

- 距离测量
- 避障

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 测距芯片     | RCWL-9600            |
| 通信接口     | I2C 通信 @ 0x57      |
| 测量距离     | 30 ~ 150cm           |
| 发射端声压级 | 108dB                |
| 接收端灵敏度 | 68dB                 |
| 盲区         | 20mm                 |
| 精度         | 1mm                  |
| 产品尺寸     | 56.0 x 24.0 x 12.0mm |
| 产品重量     | 9.0g                 |
| 包装尺寸     | 60.0 x 55.0 x 16.0mm |
| 毛重         | 23.0g                |

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/img-b4a6c370-33b7-4329-8d52-201f9353c1f0.png" width="100%" />

## 数据手册

- [Ceramic Ultrasonic Sensor TC40-10T/R](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/TC40-10T-R.pdf)

## 软件开发

### Arduino

- [Unit Ultrasonic-I2C Test Example with M5Atom](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Atom/Unit_SonicI2C_M5Atom.ino)
- [Unit Ultrasonic-I2C Test Example with M5Core](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Core/Unit_SonicI2C_M5Core.ino)
- [Unit Ultrasonic-I2C Test Example with M5Core2](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5Core2/Unit_SonicI2C_M5Core2.ino)
- [Unit Ultrasonic-I2C Test Example with M5StickC](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5StickC/Unit_SonicI2C_M5StickC.ino)
- [Unit Ultrasonic-I2C Test Example with M5StickCPlus](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicI2C_M5StickCPlus/Unit_SonicI2C_M5StickCPlus.ino)

### UiFlow1

- [Unit Ultrasonic UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ultrasonic)

### UiFlow2

- [Unit Ultrasonic UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ultrasonic.html)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                            | 备注 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Ultrasonic Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/Ultrasonic/ezLoader-7e880c47-7898-49a7-8204-f36f17d99734.exe) | /    |

## 相关视频

- 使用教程

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/ULTRASONIC.mp4" type="video/mp4"></video>

- UiFlow2 Unit Ultrasonic

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112828639938791&bvid=BV1FE8QemESG&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/01NXj78hIIA?si=oxXqdOmyWeW9TFe6" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
